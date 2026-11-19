# Guía Maestra de Excelencia Operacional: Marco Maestro para la Oficina del CISO, SOC Moderno y Gobierno NIST CSF 2.0

## 1. Portada y Ficha de Control Documental

| Atributo Documental | Valor Oficial / Definición |
|---|---|
| **Identificador del Módulo** | `00_Marco_Maestro_CISO_SOC_y_NIST` |
| **Slug Canónico** | `Marco_Maestro_CISO_SOC_y_NIST` |
| **Nombre Completo** | Marco Maestro de Excelencia Operacional para la Oficina del CISO, SOC Moderno y Gobierno NIST CSF 2.0 |
| **Categoría Maestra** | Marco Transversal CISO, SOC y NIST |
| **Versión Documental** | 2.0 — Edición Consolidada y Revalidada |
| **Fecha de Validación Técnica** | `2026-11-11` |
| **Origen y Trazabilidad** | Compilado `MSEOP-MD` (*Secop agnóstico: Dupla 1, Dupla 2, Dupla 3, Manifiesto de Excelencia Operacional* + *NIST Mapeado SAFVAL 12 bloques y matriz transversal*) + Revalidado Microsoft Learn MCP y Web Oficial (Noviembre 2026) |
| **Relación con Microsoft 365 E5** | **Marco Arquitectónico y Operativo Transversal sobre Microsoft 365 E5** — Gobierna la inversión fundacional en **M365 E5** (o la combinación **Microsoft Defender Suite** + **Microsoft Purview Suite**), sus add-ons especializados (**Microsoft Entra Suite**, **Microsoft Intune Suite**, **Microsoft Sentinel**, **Microsoft Security Copilot**) y su evolución hacia **Microsoft 365 E7: The Frontier Suite** (**Microsoft Agent 365**) `[Verificado MS Learn]` |
| **Portales Principales de Operación** | `https://security.microsoft.com` (Unified SecOps Platform: Defender XDR, Sentinel, Exposure Management, Security Copilot), `https://entra.microsoft.com` (Identidad, Acceso, Red y Agentes), `https://purview.microsoft.com` (Seguridad de Datos, Riesgo Interno y Cumplimiento), `https://intune.microsoft.com` (Endpoints y Plataforma), `https://portal.azure.com` (Suscripciones, IAM Azure RBAC, FinOps y Logic Apps) `[Verificado MS Learn]` |
| **Audiencia Objetivo** | CISO y Oficina del CISO, Consejo de Administración (Board) y Comité de Auditoría/Riesgos, Arquitectos Empresariales y de Ciberseguridad, SOC Manager, Líderes de GRC, Líderes de IAM, Endpoints, Datos/Purview, FinOps y Gestores de MSSP/MXDR |
| **Marcos Normativos Alineados** | NIST Cybersecurity Framework (CSF) 2.0 (CSWP 29 y NIST SP 1303 ERM), Microsoft Security Adoption Framework (SAF), Microsoft Cybersecurity Reference Architectures (MCRA — Junio 2026), Microsoft Secure Future Initiative (SFI), Zero Trust Architecture, MITRE ATT&CK Enterprise v18, DOE C2M2 v2.1, CMMI, The Open Group (SABSA, TOGAF, O-ISM3, Open FAIR) |

> **Nota de consolidación documental:** Este módulo inaugural constituye la constitución arquitectónica, metodológica y de gobierno para los **23 módulos (`00` a `22`)** del repositorio maestro de Excelencia Operacional Microsoft. Unifica orgánicamente cuatro fuentes estructurales: (1) el modelo de liderazgo de la **Oficina del CISO** y el **Manifiesto de Excelencia Operacional**; (2) el diseño de **SecOps Híbrido / Co-Gestionado** (equipo interno vs. MSSP/MXDR) anclado en la función transversal **GOVERN** de **NIST CSF 2.0**; (3) la arquitectura **Unified SecOps Platform** y la transición gobernada hacia el **SOC Agéntico**; y (4) el mapa maestro de licenciamiento y cobertura normativa de las **22 tecnologías del ecosistema Microsoft** revalidado al `2026-11-11`. Se aplica rigurosamente `[Verificado MS Learn]` para capacidades, portales, esquemas, fechas de disponibilidad/retiro y términos de licenciamiento oficiales de Microsoft, y `[Decisión / Propuesta Editorial]` para SLAs objetivos, metas porcentuales de KPIs, matrices RACI, modelos de madurez de cinco niveles y criterios probatorios consultivos.

---

## 2. Resumen Ejecutivo y Posicionamiento en Arquitectura Zero Trust / M365 E5

### 2.1 El Triple Pivote de la Oficina del CISO en 2026

La convergencia de ataques asistidos por inteligencia artificial a velocidad de máquina, la explosión de identidades no humanas y agentes autónomos en procesos de negocio, la exigencia regulatoria sobre directorios corporativos y la escasez global de talento especializado han tornado inviable el paradigma histórico del CISO como mero administrador reactivo de controles técnicos `[Decisión / Propuesta Editorial]`.

En este repositorio, la **Excelencia Operacional (OpEx)** se define como la propiedad sistémica emergente que permite a una organización **entregar protección, detección, respuesta, recuperación y confianza digital de forma predecible, escalable, auditable y humana y financieramente sostenible**, minimizando la fricción con el negocio mientras maximiza la reducción verificable del riesgo `[Decisión / Propuesta Editorial]`.

Para alcanzar dicho estado, la Oficina del CISO ejecuta un **triple pivote estratégico** alineado con el **Microsoft Security Adoption Framework (SAF)**, la **Secure Future Initiative (SFI)** y **NIST CSF 2.0** `[Verificado MS Learn]`:

1. **De ejecutor táctico aislado a gobernador fiduciario del riesgo empresarial:** La publicación de **NIST CSF 2.0 (CSWP 29)** posicionó **GOVERN (`GV`)** como el eje central que dirige e informa a **IDENTIFY (`ID`)**, **PROTECT (`PR`)**, **DETECT (`DE`)**, **RESPOND (`RS`)** y **RECOVER (`RC`)** `[Verificado MS Learn]`. La comprensión del contexto legal y de misión (`GV.OC`), el apetito de riesgo (`GV.RM`), la asignación de autoridades (`GV.RR`), las políticas corporativas (`GV.PO`), la supervisión ante el Directorio (`GV.OV`) y la gestión de riesgos de terceros incluyendo al propio MSSP (`GV.SC`) constituyen **deberes fiduciarios indelegables** `[Decisión / Propuesta Editorial]`.
2. **De fragmentación multi-vendor a plataformización unificada Zero Trust:** Microsoft procesa más de **100 billones (100+ trillion) de señales diarias** en su grafo global de inteligencia y articula mediante **SAF** y **MCRA (edición junio de 2026)** una plataforma convergente donde identidad (`entra.microsoft.com`), operaciones unificadas SIEM+XDR+CTEM (`security.microsoft.com`), endpoints (`intune.microsoft.com`) y seguridad de datos/cumplimiento (`purview.microsoft.com`) operan sobre telemetría y políticas nativamente integradas, reduciendo drásticamente la carga cognitiva de cambio de consola (*swivel-chair*) `[Verificado MS Learn]`.
3. **De triaje manual insostenible a SOC Agéntico con cultura Kaizen:** La automatización determinística en **Logic Apps**, la contención autónoma de alta confianza (**Automatic Attack Disruption**, con relación señal-ruido documentada **>= 99%**) y la orquestación supervisada de agentes de **Microsoft Security Copilot** y **Microsoft Agent 365** absorben entre el 60% y el 70% del trabajo repetitivo de Nivel 1 `[Verificado MS Learn]` `[Decisión / Propuesta Editorial]`. Esto protege la salud mental del analista, previene el *burnout* y redirige el intelecto humano hacia *Threat Hunting*, ingeniería de detección, arquitectura y cuantificación de riesgo `[Decisión / Propuesta Editorial]`.

```
+---------------------------------------------------------------------------------------------------+
|                        GOBIERNO FIDUCIARIO INDELEGABLE: NIST CSF 2.0 GOVERN (GV)                  |
|      GV.OC Contexto  |  GV.RM Riesgo/FAIR  |  GV.RR Roles  |  GV.PO Políticas  |  GV.OV / GV.SC   |
+---------------------------------------------------------------------------------------------------+
          |                       |                     |                     |                 |
          v                       v                     v                     v                 v
+-------------------+   +-------------------+   +-------------------+   +-----------+   +-----------+
|   IDENTIFY (ID)   |   |   PROTECT (PR)    |   |    DETECT (DE)    |   |  RESPOND  |   |  RECOVER  |
| MSEM Attack Paths |   | Entra CA/Passkeys |   | Unified SecOps    |   | Attack    |   | Action    |
| Purview Data Map  |   | Intune / Windows  |   | Defender XDR +    |   | Disruption|   | Center +  |
| Agent 365 Registry|   | Purview MIP / DLP |   | Sentinel DataLake |   | + SOAR IA |   | BCDR Clean|
+-------------------+   +-------------------+   +-------------------+   +-----------+   +-----------+
          ^                       ^                     ^                     ^                 ^
          +-----------------------+---------------------+---------------------+-----------------+
                                                |
                 ORQUESTACIÓN HUMANO-IA (Security Copilot + MCP + Agent 365) & KAIZEN SOC
```

### 2.2 Arquitectura de Licenciamiento Microsoft 2026: M365 E5, Suites Renombradas y M365 E7

Una falla recurrente en auditorías y casos de negocio es confundir los derechos incluidos en **Microsoft 365 E5** frente a suites modulares renombradas entre finales de 2025 y 2026, consumos en Azure o la suite **Microsoft 365 E7: The Frontier Suite** (disponible comercialmente desde el **1 de mayo de 2026**) `[Verificado MS Learn]`. La siguiente tabla establece la línea base contractual exacta al `2026-11-11`:

| Suite / SKU Oficial (Noviembre 2026) | Relación con M365 E5 y Renombres Vigentes | Cobertura Exacta sobre los Módulos `01` a `22` | Reglas Críticas de Prerrequisitos y Auditoría | Etiqueta |
|---|---|---|---|---|
| **Microsoft 365 E5** *(Full Enterprise Suite)* | Base de referencia del repositorio. Combina productividad empresarial con las capacidades completas de *Defender Suite* y *Purview Suite*. | Habilita nativamente `01` (Entra ID P2), base P2 de `02`, `03` (Defender XDR), `04` (MDE P2), `05` (MDO P2), `06` (MDI), `07` (MDCA), `10` (Intune P1), `12` (Windows Enterprise E5), `13` a `21` (bloque completo Purview), dotación base acotada de SCUs para funciones embebidas seleccionadas y **Data Grant de hasta 5 MB/usuario/día** en `08` (Sentinel). | Licencia por usuario/mes. Requiere atributo `UsageLocation` poblado en Entra ID. **No incluye** el consumo base de Sentinel en Azure, *Intune Suite* (`11`), *Entra Suite* completa ni *Agent 365* (`22`). | `[Verificado MS Learn]` |
| **Microsoft Defender Suite** *(antes Microsoft 365 E5 Security)* | Renombre oficial del add-on **Microsoft 365 E5 Security** (disponible sobre M365 E3 y en edición para M365 Business Premium). | Incluye **Microsoft Entra ID P2** (`01`), **Defender XDR** (`03`), **MDE P2** (`04`), **MDO P2** (`05`), **MDI** (`06`), **MDCA** (`07`) y elegibilidad para el **Data Grant de 5 MB/usuario/día** en Microsoft Sentinel (`08`). | **No incluye** capacidades avanzadas de cumplimiento o seguridad de datos de Purview (`13`–`21`). Si el cliente requiere ambos dominios sin ir a E5 completo, debe asignar *Defender Suite* + *Purview Suite*. | `[Verificado MS Learn]` |
| **Microsoft Purview Suite** *(antes Microsoft 365 E5 Compliance)* | Renombre oficial del add-on **Microsoft 365 E5 Compliance**. | Incluye **Purview Information Protection** (`14`), **DLP** (`15`), **Data Lifecycle & Records Management** (`16`), **Insider Risk Management** (`17`), **Communication Compliance** (`18`), **Audit Premium** (`19`), **eDiscovery Premium** (`20`) y **Customer Lockbox / Customer Key / M365 PAM** (`21`). | **Regla crítica de auditoría:** *Microsoft Purview Suite* **NO incluye Entra ID P2**, Risk-based Conditional Access ni PIM (`01`, `02`). No puede sustentar controles `PR.AA` de identidad avanzada por sí sola. | `[Verificado MS Learn]` |
| **Microsoft Entra Suite** *(Add-on de Identidad y Red Zero Trust)* | Complemento sobre Entra ID P1 (M365 E3 o M365 E5) e incluido dentro de **Microsoft 365 E7**. | Habilita **Entra Private Access** y **Entra Internet Access** (*Global Secure Access* SSE), **Entra ID Governance** completo (`02`: Lifecycle Workflows, Entitlement Management avanzado, recomendaciones ML en Access Reviews), **Entra ID Protection** y **Verified ID** premium. | Requiere licencia base con al menos **Microsoft Entra ID P1**. Extiende Zero Trust hacia el plano de red e identidad gobernada integral. | `[Verificado MS Learn]` |
| **Microsoft Intune Suite** *(Add-on Avanzado de Endpoints)* | Complemento sobre **Intune Plan 1** (`10`), documentado en el Módulo `11`. | Añade **Endpoint Privilege Management (EPM)**, **Intune Remote Help**, **Enterprise Application Management**, **Microsoft Cloud PKI**, **Advanced Analytics** e **Intune Plan 2**. *(Nota: EMS E5 incluye Intune Plan 2, Remote Help y Advanced Analytics).* | Requiere **Microsoft Intune Plan 1** activo. Elimina privilegios de administrador local en estaciones de trabajo (`PR.AA-05`, `PR.PS-01`). | `[Verificado MS Learn]` |
| **Microsoft Sentinel** *(Consumo Azure Asociado a M365 E5)* | Plataforma SIEM, SOAR, Graph y **Sentinel Data Lake** (`08`). No es licencia por usuario. | Facturado en Azure en **Analytics Tier** (PAYG o *Simplified Commitment Tiers* desde 100 GB/día) y **Data Lake Tier** (integrado por defecto desde el `2026-09-23`, compresión 6:1, hasta 12 años). Recibe **hasta 5 MB/usuario/día gratuitos** con M365 E5/E7 o *Defender Suite* y fuentes gratuitas (`AzureActivity`, `OfficeActivity`, `SentinelHealth`, `SecurityAlert`, `SecurityIncident`). | Requiere suscripción Azure y workspace incorporado a `security.microsoft.com` (experiencia en Azure Portal se retira tras el **31 de marzo de 2027**). | `[Verificado MS Learn]` |
| **Microsoft Security Copilot** *(Dotación E5/E7 + Consumo SCU Azure)* | Plataforma de IA generativa y agentes para operaciones de seguridad (`09`). | M365 E5/E7 incluyen un volumen acotado de **SCUs** para agentes y experiencias embebidas seleccionadas en Defender, Entra, Intune y Purview sobre telemetría licenciada; el portal standalone, capacidad adicional, agentes de partners y fuentes de terceros se facturan por consumo en Azure (*Provisioned / Overage SCUs*). | Requiere aprovisionamiento de capacidad en Azure para operación transversal completa y monitoreo estricto de consumo SCU. | `[Verificado MS Learn]` |
| **Microsoft Agent 365 y Microsoft 365 E7: The Frontier Suite** | Anunciados en marzo de 2026 y disponibles desde el **1 de mayo de 2026** (`22`). | **Microsoft 365 E7** ($99 USD/usuario/mes ERP referencial) consolida **4 en 1**: **M365 E5 + Microsoft 365 Copilot + Microsoft Entra Suite + Microsoft Agent 365**. **Agent 365** también está disponible como add-on sobre M365 E5/A5/Business Premium (o *Defender Suite* + *Purview Suite*) para aplicar Conditional Access, ID Protection, Purview DSPM/DLP y Defender a agentes IA. | Mientras **Entra Agent ID** base (blueprints/identidad) está disponible para todo cliente Entra, extender políticas de seguridad/gobierno a agentes exige licencia **Microsoft Agent 365** o **M365 E7**. | `[Verificado MS Learn]` |

### 2.3 Mapa Arquitectónico Maestro de las 22 Tecnologías del Repositorio (`01` a `22`)

La Oficina del CISO gobierna este repositorio como un sistema interconectado donde cada módulo tecnológico entrega telemetría, controles preventivos y evidencia auditable al marco común `[Decisión / Propuesta Editorial]`:

| Módulo | Slug Canónico | Categoría Maestra | Licencia Base / Add-on | Portal Primario | Rol Arquitectónico en Zero Trust y NIST CSF 2.0 |
|---|---|---|---|---|---|
| `00` | `Marco_Maestro_CISO_SOC_y_NIST` | Marco Transversal CISO, SOC y NIST | Transversal M365 E5 / E7 + Azure | Todos los portales | Gobierno ejecutivo CISO, modelo SecOps híbrido, métricas en 3 altitudes y matriz NIST CSF 2.0 (`GV`–`RC`). |
| `01` | `Microsoft_Entra_ID` | Identidad y Acceso (Microsoft Entra) | M365 E5 / *Defender Suite* / Entra P2 | `entra.microsoft.com` | Plano de control IAM: Authentication Methods, Passkeys FIDO2, Conditional Access (CAE/Token Protection), ITDR y Break-Glass. |
| `02` | `Microsoft_Entra_ID_Governance` | Identidad y Acceso (Microsoft Entra) | Base P2 en E5 + Add-on *Entra ID Governance / Entra Suite / E7* | `entra.microsoft.com` | Gobierno de ciclo de vida JML (*Lifecycle Workflows*), *Entitlement Management*, *Access Reviews* y gobierno de privilegios. |
| `03` | `Microsoft_Defender_XDR` | SecOps, XDR y SIEM | M365 E5 / *Defender Suite* | `security.microsoft.com` | Fusión de incidentes multi-dominio, *Automatic Attack Disruption*, *Unified RBAC* y *Exposure Management (MSEM)*. |
| `04` | `Microsoft_Defender_for_Endpoint` | SecOps, XDR y SIEM | M365 E5 / *Defender Suite* (MDE P2) | `security.microsoft.com` | EDR/EPP, *Threat & Vulnerability Management (TVM)*, reglas ASR, *Live Response* y contención de red en estaciones/servidores. |
| `05` | `Microsoft_Defender_for_Office_365` | SecOps, XDR y SIEM | M365 E5 / *Defender Suite* (MDO P2) | `security.microsoft.com` | Protección anti-phishing/BEC/Prompt Injection, *Safe Links/Attachments*, *ZAP*, *Threat Explorer*, *AIR* y *Attack Simulation Training*. |
| `06` | `Microsoft_Defender_for_Identity` | SecOps, XDR y SIEM | M365 E5 / *Defender Suite* | `security.microsoft.com` | ITDR sobre Active Directory/AD FS/AD CS: detección de *DCSync*, *Kerberoasting*, *Pass-the-Hash*, postura AD y deshabilitación híbrida. |
| `07` | `Microsoft_Defender_for_Cloud_Apps` | SecOps, XDR y SIEM | M365 E5 / *Defender Suite* | `security.microsoft.com` | CASB, descubrimiento *Shadow IT / Shadow AI*, SSPM, *App Governance* para OAuth y control de sesión en tiempo real. |
| `08` | `Microsoft_Sentinel` | SecOps, XDR y SIEM | Consumo Azure + *5 MB/u/día E5 Data Grant* | `security.microsoft.com` | SIEM/SOAR multicloud, *Sentinel Data Lake* (hasta 12 años), normalización ASIM, *Hunts*, *SOC Optimization* y *Sentinel Graph*. |
| `09` | `Microsoft_Security_Copilot` | SecOps, XDR y SIEM | SCUs base limitadas E5/E7 + SCUs Azure | `security.microsoft.com` | Asistente generativo y agentes autónomos (Phishing, CA, TVM, DLP, Threat Intel) integrados vía MCP para acelerar triaje y caza. |
| `10` | `Microsoft_Intune_Plan_1` | Endpoints, Dispositivos y Plataforma Windows | M365 E3 / M365 E5 | `intune.microsoft.com` | MDM/MAM multiplataforma, políticas de cumplimiento para Conditional Access, *Security Baselines*, Windows Autopilot y parches. |
| `11` | `Microsoft_Intune_Suite` | Endpoints, Dispositivos y Plataforma Windows | Add-on *Microsoft Intune Suite* | `intune.microsoft.com` | *Endpoint Privilege Management (EPM)* JIT local, *Remote Help* seguro, *Enterprise App Management*, *Cloud PKI* y analítica avanzada. |
| `12` | `Windows_Enterprise_Security_y_Cifrado` | Endpoints, Dispositivos y Plataforma Windows | M365 E5 (Windows 11 Enterprise E5) | `intune.microsoft.com` | Seguridad de silicio a nube: *Windows Hello for Business*, *Credential Guard*, *BitLocker*, *Windows LAPS* y *App Control for Business*. |
| `13` | `Microsoft_Purview_Suite_Arquitectura_y_Gobierno` | Seguridad de Datos, Cumplimiento y Gobierno (Microsoft Purview) | M365 E5 / *Purview Suite* | `purview.microsoft.com` | Gobierno integral de datos e IA (*DSPM for AI*), *Data Map*, *Compliance Manager* (evaluaciones NIST/ISO) y arquitectura de roles Purview. |
| `14` | `Purview_Information_Protection` | Seguridad de Datos, Cumplimiento y Gobierno (Microsoft Purview) | M365 E5 / *Purview Suite* | `purview.microsoft.com` | Descubrimiento de datos sensibles (SITs/Trainable Classifiers), etiquetado manual/automático, cifrado persistente Rights Management y marcas. |
| `15` | `Purview_Data_Loss_Prevention` | Seguridad de Datos, Cumplimiento y Gobierno (Microsoft Purview) | M365 E5 / *Purview Suite* | `purview.microsoft.com` | Prevención unificada de exfiltración en Exchange, SharePoint, OneDrive, Teams, Endpoints (Endpoint DLP), navegadores e IA generativa. |
| `16` | `Purview_Data_Lifecycle_y_Records_Management` | Seguridad de Datos, Cumplimiento y Gobierno (Microsoft Purview) | M365 E5 / *Purview Suite* | `purview.microsoft.com` | Retención regulatoria inmutable (*Preservation Lock*), disposición defensiva de datos obsoletos y gestión formal de récords legales. |
| `17` | `Purview_Insider_Risk_Management` | Seguridad de Datos, Cumplimiento y Gobierno (Microsoft Purview) | M365 E5 / *Purview Suite* | `purview.microsoft.com` | Detección con privacidad por diseño (seudonimización) de robo de propiedad intelectual, sabotaje y *Adaptive Protection* dinámica. |
| `18` | `Purview_Communication_Compliance` | Seguridad de Datos, Cumplimiento y Gobierno (Microsoft Purview) | M365 E5 / *Purview Suite* | `purview.microsoft.com` | Detección de violaciones de código de conducta, colusión financiera, acoso, fuga de secretos e interacciones riesgosas con Copilot/IA. |
| `19` | `Purview_Audit_Premium` | Seguridad de Datos, Cumplimiento y Gobierno (Microsoft Purview) | M365 E5 / *Purview Suite* | `purview.microsoft.com` | Registro forense de alta fidelidad (*MailItemsAccessed*, *SearchQueryInitiated*), retención de 1 año por defecto (hasta 10 años) y ancho de banda API. |
| `20` | `Purview_eDiscovery_Premium` | Seguridad de Datos, Cumplimiento y Gobierno (Microsoft Purview) | M365 E5 / *Purview Suite* | `purview.microsoft.com` | Preservación legal (*Legal Hold*), recolección multi-carga en M365, revisión analítica asistida y exportación probatoria con cadena de custodia. |
| `21` | `Customer_Lockbox_Customer_Key_y_M365_PAM` | Seguridad de Datos, Cumplimiento y Gobierno (Microsoft Purview) | M365 E5 / *Purview Suite* | `admin.microsoft.com` / `purview.microsoft.com` | Soberanía criptográfica BYOK (*Customer Key*), aprobación explícita de soporte Microsoft (*Customer Lockbox*) y *Privileged Access Management* en M365. |
| `22` | `Microsoft_Agent_365` | Gobierno y Seguridad de Agentes IA | Add-on *Agent 365* / Incluido en **M365 E7** | `admin.microsoft.com` / `entra.microsoft.com` | Registro unificado de agentes IA, gobierno de ciclo de vida y extensión de controles Entra, Purview y Defender XDR a agentes autónomos. |

### 2.4 Principios Rectores del Manifiesto de Excelencia Operacional y Microsoft SAF

El **Microsoft Security Adoption Framework (SAF)** articula cuatro bloques operativos —*Business scenarios*, *Security disciplines*, *Technologies* y *Technical solutions*— que convergen con los seis principios del **Manifiesto de Excelencia Operacional de la Oficina del CISO** `[Verificado MS Learn]` `[Decisión / Propuesta Editorial]`:

1. **Plataformización sobre fragmentación (*Verify Explicitly & Single Unified Fabric*):** Reducir sistemáticamente la fricción cognitiva y los silos de telemetría consolidando la detección, postura y respuesta sobre la arquitectura de referencia **MCRA (junio 2026)** y exigiendo integración nativa vía API/ASIM cuando coexistan herramientas de nicho `[Verificado MS Learn]`.
2. **Mínimo privilegio universal y acceso Just-In-Time (*Zero Standing Privileges*):** Ninguna identidad humana, de carga de trabajo o de agente IA conserva permisos administrativos permanentes innecesarios; todo acceso privilegiado es efímero, trazable y protegido por credenciales resistentes a phishing `[Verificado MS Learn]`.
3. **Orquestación calibrada Humano-IA (*Assume Breach at Machine Speed*):** Automatizar lo determinístico y repetible para que el juicio humano se concentre en decisiones contextuales de alto impacto, operando bajo tres modos formales (*Human-IN*, *Human-ON* y *Human-OUT-of-the-Loop*) `[Decisión / Propuesta Editorial]`.
4. **Gobierno anual integrado con NIST CSF 2.0 y ERM (*SFI Governance Pattern*):** Ejecutar autoevaluaciones anuales basadas en alcance de riesgo siguiendo el patrón oficial de SFI (`integrate-nist-2-governance`), registrando brechas en el *Risk Register* corporativo y reportando en tres altitudes diferenciadas (SOC, C-Level y Board) `[Verificado MS Learn]`.
5. **Externalización gobernada por resultados (*Outcome-Driven Co-Management*):** Cuando se delega operación 24x7 a un MSSP o servicio MXDR, la organización retiene el 100% de la función **GOVERN** y exige SLAs contractuales basados en precisión y velocidad de contención real, jamás en cantidad de tickets cerrados `[Decisión / Propuesta Editorial]`.
6. **Sostenibilidad humana y mejora continua Kaizen:** Planificar la capacidad operativa manteniendo al menos un **15% de holgura** sobre la carga esperada y reservando tiempo formal para capacitación, ingeniería y retrospectivas sin culpa (*blameless post-mortems*) `[Decisión / Propuesta Editorial]`.

---

## 3. Arquitectura Operativa, Componentes Clave e Integraciones del Ecosistema

### 3.1 Convergencia en Unified SecOps Platform (`https://security.microsoft.com`)

A noviembre de 2026, la arquitectura operativa de Microsoft ha completado la transición desde portales separados hacia una **Unified SecOps Platform** alojada en `https://security.microsoft.com` `[Verificado MS Learn]`:

- **Cola Única de Incidentes y Correlación Multi-Dominio:** Las alertas provenientes de **Microsoft Defender for Endpoint**, **Defender for Office 365**, **Defender for Identity**, **Defender for Cloud Apps**, **Defender for Cloud**, **Microsoft Entra ID Protection**, **Microsoft Purview DLP / Insider Risk** y **Microsoft Sentinel** se fusionan automáticamente en expedientes únicos (*Incidents*) con grafo visual de activos, *Blast Radius* y mapeo **MITRE ATT&CK v18** `[Verificado MS Learn]`.
- **Hito Mandatorio de Retiro de Sentinel en Azure Portal (`2027-03-31`):** Microsoft Sentinel opera en disponibilidad general dentro de `security.microsoft.com`. **Después del 31 de marzo de 2027, Microsoft Sentinel dejará de recibir soporte en Azure Portal (`portal.azure.com`)**, quedando únicamente los controles de infraestructura Azure (facturación, RG IAM, Logic Apps subyacentes) en el portal de Azure `[Verificado MS Learn]`.
- **Microsoft Sentinel Data Lake Integrado (`2026-09-23`):** Desde el **23 de septiembre de 2026**, el lago de datos de Sentinel se habilita de forma integrada en el flujo de incorporación estándar, espejando automáticamente las tablas del **Analytics tier** sin doble cargo de ingesta, con **compresión 6:1**, retención de hasta **12 años**, consultas KQL interactivas directas en *Advanced Hunting*, *KQL jobs*, notebooks Spark y federación sin copia hacia **Microsoft Fabric OneLake** `[Verificado MS Learn]`.
- **Microsoft Security Exposure Management (MSEM) como Motor CTEM:** Reemplaza la dependencia exclusiva en puntajes estáticos al construir continuamente un grafo de exposición (*Exposure Graph*) que vincula vulnerabilidades CVSS/EPSS, configuraciones inseguras, permisos excesivos e identidades expuestas con rutas de ataque reales hacia los activos críticos del negocio (*Chokepoints* e *Initiatives*) `[Verificado MS Learn]`.
- **Esquema Nativo de Identidad Revalidado (`2026-10-19`):** En *Advanced Hunting* del portal unificado, la tabla en vista previa `AADSignInEventsBeta` quedó oficialmente en desuso el **19 de octubre de 2026**, siendo reemplazada automáticamente por **`EntraIdSignInEvents`** (junto con `EntraIdSpnSignInEvents`, `EntraIdDirectoryAuditEvents` y la columna `EntraIdDeviceId` en sustitución de `AadDeviceId`) `[Verificado MS Learn]`.

### 3.2 Arquitectura del SOC Agéntico: Security Copilot, MCP y Microsoft Agent 365

La evolución más trascendental de 2025–2026 es el paso de la IA meramente conversacional hacia **agentes especializados gobernados por humanos** `[Verificado MS Learn]`:

1. **Agentes Operativos en Security Copilot, Entra, Intune y Purview:** Agentes preconstruidos y personalizados analizan correos de phishing (*Phishing Triage Agent*), evalúan brechas y superposiciones en acceso condicional (*Conditional Access Optimization Agent*), priorizan parches críticos (*Vulnerability Remediation Agent*), pre-clasifican alertas de seguridad de datos (*Purview Triage Agents*) y consultan el **Sentinel Graph / MCP Server** para enriquecer investigaciones complejas en segundos `[Verificado MS Learn]`.
2. **Gobierno de Identidad y Acceso para Agentes (Entra Agent ID + Agent 365):** Todo agente empresarial descubierto en **Microsoft Agent 365** recibe una identidad de primera clase en **Microsoft Entra Agent ID** estructurada mediante *Agent Identity Blueprints*, patrocinadores humanos (*Sponsors*), políticas específicas de **Conditional Access for agents** (cubriendo flujos delegados *On-Behalf-Of*, identidades autónomas de agente y cuentas *Agent User*), detección de anomalías en **ID Protection for agents** y auditoría completa de actividad `[Verificado MS Learn]`.
3. **Tres Modos Formales de Supervisión Humana:**
   - **Human-OUT-of-the-Loop (Autonomía Determinística / >=99% SNR):** Reservado para **Automatic Attack Disruption** (contención inmediata de dispositivo/IP en MDE, revocación de sesión y suspensión de cuenta en Entra ID/AD ante ransomware activo, BEC o robo de token AiTM) y bloqueos automáticos de riesgo alto en Conditional Access, siempre respaldados por reversibilidad instantánea en `Action center` y listas de exclusión de activos ultra-críticos `[Verificado MS Learn]`.
   - **Human-ON-the-Loop (Autonomía Supervisada):** Aplicado a agentes de triaje y optimización de políticas; el agente investiga, clasifica borradores o genera políticas en modo `Report-only`, mientras el analista L2/L3 audita muestras diarias, mide *AI Agent Accuracy* y autoriza promociones a producción `[Decisión / Propuesta Editorial]`.
   - **Human-IN-the-Loop (Aprobación Humana Explícita):** Obligatorio para acciones con impacto operativo mayor (aislamiento de servidores core/OT, cambios masivos de políticas, activación Break-Glass, aprobación **Customer Lockbox** y comunicaciones regulatorias) `[Decisión / Propuesta Editorial]`.

### 3.3 Modelo Operativo Co-Gestionado (Equipo Interno vs. MSSP / MXDR)

Alineado con **NIST CSF 2.0**, **SABSA** y **The Open Group O-ISM3**, el árbol de decisión de aprovisionamiento (*sourcing*) establece tres capas complementarias `[Decisión / Propuesta Editorial]`:

| Función NIST CSF 2.0 | Modelo Recomendado | Responsabilidad del Equipo Interno (Oficina del CISO / Ingeniería / CSIRT) | Responsabilidad Delegable al Socio Externo (MSSP / MXDR) | Controles técnicos Microsoft de Frontera |
|---|---|---|---|---|
| **GOVERN (`GV`)** | **100% Interno** *(No delegable)* | Contexto regulatorio, apetito de riesgo FAIR, matriz RACI, autoría de políticas, comités con el Board y supervisión contractual del propio MSSP. | Cumplir políticas del cliente, entregar telemetría transparente y participar en revisiones trimestrales (QBR). | Roles de lectura GRC; **prohibición total** de asignar roles de dueño de políticas o Global Admin al MSSP. |
| **IDENTIFY (`ID`)** | **Co-Gestionado** *(Decisión interna)* | Definir *Crown Jewels* (BIA), priorizar riesgos según impacto al negocio, mantener el *Risk Register* y liderar modelado de amenazas. | Operar escaneos continuos de vulnerabilidades, descubrimiento técnico de activos e ingesta de feeds globales CTI. | **Exposure Management** (*Critical Assets* administrados internamente; vistas acotadas para el MSSP). |
| **PROTECT (`PR`)** | **Co-Gestionado** *(Diseño interno)* | Arquitectura IAM/Conditional Access, PIM, claves de cifrado (*Customer Key*), etiquetas MIP/DLP y aprobación de cambios mayores. | Mantenimiento operativo de agentes EDR, soporte en despliegue de parches aprobados y ejecución logística de simulaciones AST. | **PIM Approval**, **Intune RBAC Scope Tags** y flujos CI/CD con aprobación interna obligatoria. |
| **DETECT (`DE`)** | **Híbrido** *(Escala MSSP + Contexto interno)* | Ingeniería fina de reglas específicas del negocio, **Threat Hunting** sobre activos críticos y validación *Purple Team*. | Monitoreo ininterrumpido **24x7x365**, triaje L1/L2 en minutos, salud de conectores y propuestas de ajuste de reglas genéricas. | **Azure Lighthouse** con rol `Microsoft Sentinel Responder` y **Defender URBAC** acotado por grupos de activos. |
| **RESPOND (`RS`)** | **Liderazgo Interno + Soporte Externo** | Declarar incidente mayor, dirigir el CSIRT, autorizar contenciones disruptivas de negocio y liderar toda comunicación legal/ejecutiva/pública. | Contención técnica inmediata pre-aprobada (ej. aislar laptop estándar) en <=15 min y apoyo forense especializado (*IR Retainer*). | Runbooks codificados en **Automation Rules / Logic Apps** y traspaso formal auditado en *Case Management*. |
| **RECOVER (`RC`)** | **Principalmente Interno** | Priorizar orden de restauración según RTO/RPO, validar limpieza antes de reconectar, comunicar cierre y actualizar arquitectura/políticas. | Proveer indicadores forenses de erradicación completa e informe técnico post-incidente. | Validación en **Defender Action Center**, políticas de contingencia CA y pruebas de restauración limpia. |

### 3.4 Matriz Maestra de las 22 Categorías Oficiales de NIST CSF 2.0 (CSWP 29) × Stack Microsoft

> **Corrección taxonómica obligatoria `[Verificado MS Learn]`:** El estándar oficial **NIST CSWP 29** contiene exactamente **22 categorías y 106 subcategorías** distribuidas en **6 funciones** (`GV`: 6, `ID`: 3, `PR`: 5, `DE`: 2, `RS`: 4, `RC`: 2). Documentos preliminares del mercado que listaban una categoría 23 (`RC.IM`) son incorrectos frente al texto normativo definitivo, dado que NIST unificó toda la gestión de mejoras (incluidas las lecciones aprendidas de respuesta y recuperación) bajo **`ID.IM` (Improvement)**.

| Función | Código y Nombre Oficial de Categoría (CSWP 29) | Subcategorías | Módulos Primarios del Repositorio (`01`–`22`) | Contribución Técnica Verificable y Límite Consultivo |
|---|---|---|---|---|
| **GV** | `GV.OC` — Organizational Context | 5 (`01`–`05`) | `13` Purview Compliance Manager · `07` MDCA · `16` DLM | Mapea obligaciones regulatorias y dependencias críticas SaaS/datos; misión y expectativas de stakeholders requieren gobierno ejecutivo interno `[Decisión / Propuesta Editorial]`. |
| **GV** | `GV.RM` — Risk Management Strategy | 7 (`01`–`07`) | `03` MSEM · `01` Entra ID Protection · `17` Purview IRM · `08` Sentinel | Instrumenta umbrales de riesgo técnicos y priorización; la declaración financiera de apetito/tolerancia (FAIR) e integración ERM es interna `[Decisión / Propuesta Editorial]`. |
| **GV** | `GV.RR` — Roles, Responsibilities, and Authorities | 4 (`01`–`04`) | `01`/`02` Entra RBAC & PIM · `03` Defender URBAC · `13` Purview RBAC · `22` Agent 365 | Impone mínimo privilegio, segregación de funciones y *Sponsors* de agentes IA con trazabilidad total; las descripciones de puesto RRHH son internas `[Verificado MS Learn]`. |
| **GV** | `GV.PO` — Policy | 2 (`01`–`02`) | `01` Conditional Access · `10` Intune · `14`/`15`/`16` Purview · `03`/`08` SecOps | Traduce políticas escritas en cumplimiento técnico automático (*Policy-as-Code*); el cuerpo normativo corporativo debe aprobarse en comité interno `[Decisión / Propuesta Editorial]`. |
| **GV** | `GV.OV` — Oversight | 3 (`01`–`03`) | `03` MSEM/Secure Score · `08` Workbooks · `13` Compliance Manager · `02` Access Reviews | Provee tableros continuos de cumplimiento, KPIs operativos y recertificaciones periódicas para supervisión del CISO y del Directorio `[Verificado MS Learn]`. |
| **GV** | `GV.SC` — Cybersecurity Supply Chain Risk Management | 10 (`01`–`10`) | `07` MDCA (App Governance) · `01`/`02` B2B Cross-Tenant · `08` Sentinel · `21` Lockbox | Monitorea apps OAuth de terceros, proveedores B2B, MSSP vía Lighthouse y soporte Microsoft; cláusulas legales y debida diligencia previa requieren TPRM/Compras `[Decisión / Propuesta Editorial]`. |
| **ID** | `ID.AM` — Asset Management | 8 (`01`–`08`) | `03` MSEM · `04` MDE · `10` Intune · `01` Entra · `07` MDCA · `13` Purview · `22` Agent 365 | Inventario continuo de dispositivos, software, identidades humanas/workloads/agentes, apps SaaS y mapa de datos; criticidad BIA requiere validación de negocio `[Verificado MS Learn]`. |
| **ID** | `ID.RA` — Risk Assessment | 10 (`01`–`10`) | `03` MSEM Attack Paths · `04` TVM · `01` ID Protection · `06` MDI · `08` Sentinel TI/UEBA | Correlaciona CVEs (CVSS/EPSS/KEV), inteligencia de amenazas (MDTI), rutas de ataque y anomalías conductuales para priorizar mitigación `[Verificado MS Learn]`. |
| **ID** | `ID.IM` — Improvement | 4 (`01`–`04`) | `08` SOC Optimization · `03` MSEM Initiatives · `05` AST · `09` Security Copilot | Ciclo cerrado de mejora continua a partir de auditorías, ejercicios *Purple Team*, optimización de reglas SIEM e incidentes cerrados `[Verificado MS Learn]`. |
| **PR** | `PR.AA` — Identity Management, Authentication, and Access Control | 6 (`01`–`06`) | `01` Entra ID · `02` ID Governance · `11` Intune EPM · `21` Lockbox/PAM · `22` Agent 365 | Autenticación resistente a phishing (Passkeys FIDO2/WHfB/CBA), Conditional Access adaptativo, Token Protection, CAE, PIM JIT y gobierno de agentes `[Verificado MS Learn]`. |
| **PR** | `PR.AT` — Awareness and Training | 2 (`01`–`02`) | `05` MDO Attack Simulation Training · `17` Purview IRM · Ninja Trainings | Simulaciones realistas de ingeniería social, micro-aprendizaje dirigido por comportamiento de riesgo y rutas técnicas por rol SOC/IAM/Datos `[Verificado MS Learn]`. |
| **PR** | `PR.DS` — Data Security | 11 (`01`–`11`) | `14` MIP · `15` DLP · `16` DLM · `17` IRM · `21` Customer Key · `12` BitLocker · `07` MDCA | Clasificación, cifrado en reposo/tránsito/uso, prevención de fuga en endpoints/nube/IA, soberanía de claves e integridad del ciclo de vida documental `[Verificado MS Learn]`. |
| **PR** | `PR.PS` — Platform Security | 6 (`01`–`06`) | `10`/`11` Intune · `12` Windows E5 · `04` MDE ASR · `06` MDI · `07` MDCA SSPM | Líneas base de endurecimiento OS, gestión de parches/aplicaciones, reducción de superficie ASR, LAPS, seguridad de controladores AD y postura SaaS `[Verificado MS Learn]`. |
| **PR** | `PR.IR` — Technology Infrastructure Resilience | 4 (`01`–`04`) | `08` Sentinel/Data Lake · `16` Purview Preservation Lock · `01` Entra Resilience | Resiliencia de autenticación (CAE, Break-Glass), retención inmutable de logs/datos; debe complementarse con backups dedicados (M365 Backup/Azure Backup) y redes redundantes `[Decisión / Propuesta Editorial]`. |
| **DE** | `DE.CM` — Continuous Monitoring | 9 (`01`–`09`) | Todos los módulos `01` a `22` convergentes en `03` Defender XDR y `08` Sentinel | Vigilancia 24x7 de red, identidad, endpoints, correo, datos, actividades de proveedores y agentes autónomos `[Verificado MS Learn]`. |
| **DE** | `DE.AE` — Adverse Event Analysis | 8 (`01`–`08`) | `03` Defender XDR · `08` Sentinel Analytics/UEBA/ASIM · `09` Security Copilot | Correlación automática multi-señal, enriquecimiento contextual con CTI, reconstrucción de línea de tiempo y priorización por severidad `[Verificado MS Learn]`. |
| **RS** | `RS.MA` — Incident Management | 5 (`01`–`05`) | `03` Defender XDR Unified Queue · `08` Sentinel Case Mgmt & Automation Rules | Gestión centralizada de extremo a extremo de incidentes, asignación RACI, triaje estandarizado y coordinación con terceros `[Verificado MS Learn]`. |
| **RS** | `RS.AN` — Incident Analysis | 5 (`01`–`05`) | `03` Advanced Hunting · `04` Live Response · `08` Data Lake · `09` Copilot · `19`/`20` Purview | Investigación forense profunda sobre años de telemetría, preservación con cadena de custodia legal e identificación de causa raíz `[Verificado MS Learn]`. |
| **RS** | `RS.CO` — Incident Reporting and Communication | 2 (`01`–`02`) | `08` Workbooks/Logic Apps · `20` eDiscovery · `13` Purview | Automatiza notificaciones técnicas internas y recopilación de alcance afectado; la notificación formal a reguladores, prensa y clientes es jurídico-ejecutiva `[Decisión / Propuesta Editorial]`. |
| **RS** | `RS.MI` — Incident Mitigation | 2 (`01`–`02`) | `03` Automatic Attack Disruption · `01` Entra · `04`–`07` Defender · `08` Logic Apps SOAR | Contención en tiempo real (aislar host, suspender usuario/agente, revocar tokens, purgar emails ZAP, bloquear OAuth/IP) y erradicación guiada `[Verificado MS Learn]`. |
| **RC** | `RC.RP` — Incident Recovery Plan Execution | 6 (`01`–`06`) | `03` Action Center · `01` Entra ID · `10`/`12` Intune/Autopilot · `16` Purview DLM | Liberación verificada de activos contenidos, rotación masiva de credenciales, reprovisionamiento limpio e integridad previa a vuelta a operación `[Verificado MS Learn]`. |
| **RC** | `RC.CO` — Incident Recovery Communication | 2 (`01`–`02`) | `03`/`08` Reportes ejecutivos de estado de recuperación + Canales corporativos | Provee evidencia técnica objetiva de restablecimiento seguro para respaldar comunicados internos, a clientes, reguladores y mercado `[Decisión / Propuesta Editorial]`. |

---

## 4. Modelo de Gobierno, Roles y Matriz RBAC de Mínimo Privilegio (PIM / JIT)

El gobierno transversal prohíbe el uso cotidiano de `Global Administrator` y exige mapear cada responsabilidad a roles específicos en **Entra RBAC**, **Defender Unified RBAC (URBAC)**, **Azure RBAC**, **Purview Role Groups** e **Intune RBAC** `[Verificado MS Learn]`:

| Rol de Gobierno / Operación | Nivel / Dominio | Roles Mínimos Oficiales Recomendados | Estrategia de Asignación PIM / JIT | Segregación de Funciones (SoD) y Controles Críticos | Etiqueta |
|---|---|---|---|---|---|
| **CISO / Office of the CISO** | Ejecutivo / `GOVERN` | Entra: `Reports Reader` o `Security Reader`; Purview: lectura ejecutiva de *Compliance Manager* | **Activa de solo lectura** (protegida con MFA resistente a phishing). | No posee permisos de escritura técnica ni aprueba sus propios cambios; ejerce supervisión independiente (`GV.OV`). | `[Verificado MS Learn]` / `[Decisión / Propuesta Editorial]` |
| **Enterprise Cybersecurity Architect** | Estratégico / `IDENTIFY` & `PROTECT` | Entra: `Security Reader` (activo) + `Conditional Access Administrator` (elegible para ventana CAB); Defender URBAC: lectura de postura/MSEM | **Eligible en PIM** (máximo **4 horas**, justificación con ticket CAB + MFA FIDO2/WHfB). | Diseña políticas y evalúa *Attack Paths*, pero otro administrador revisa/aprueba el pase a producción (*four-eyes principle*). | `[Verificado MS Learn]` / `[Decisión / Propuesta Editorial]` |
| **GRC, Risk & Audit Manager** | Gobierno / `GOVERN` & `IDENTIFY` | Purview: `Compliance Administrator` (elegible) y `View-Only Audit Logs`; Entra: `Directory Readers` | Lectura permanente para auditoría; escritura en *Compliance Manager* vía **PIM Eligible (8 horas)**. | Audita configuraciones, *Access Reviews* y SLAs del MSSP sin capacidad de alterar logs ni desactivar alertas. | `[Verificado MS Learn]` / `[Decisión / Propuesta Editorial]` |
| **SOC Manager / CSIRT Lead** | Dirección Táctica / `DETECT` & `RESPOND` | Defender URBAC: rol *SOC Lead* (Incidentes + aprobación *Action Center* + *Live Response*); Azure RBAC: `Microsoft Sentinel Responder` | **Eligible en PIM** por turno de **8 horas** con MFA resistente a phishing. | Autoriza contenciones mayores y dirige crisis, pero no administra identidades globales ni borra espacios de Log Analytics. | `[Verificado MS Learn]` / `[Decisión / Propuesta Editorial]` |
| **SOC Analysts L1 / L2 y Equipo MSSP** | Operación 24x7 / `DETECT` & `RESPOND` | Defender URBAC acotado por *Scope* (`Alerts & investigation`); Azure RBAC: `Microsoft Sentinel Responder` (vía **Azure Lighthouse** para MSSP) | *PIM for Groups* por turno de **8 horas**; acceso condicional exigiendo ubicación/dispositivo conforme del SOC. | Ejecutan triaje, enriquecimiento con Copilot y respuesta pre-autorizada; **impedidos** de modificar reglas analíticas, conectores o retención. | `[Verificado MS Learn]` / `[Decisión / Propuesta Editorial]` |
| **SOC L3 / Detection Engineer & Threat Hunter** | Avanzado / `DETECT` & `IMPROVE` | Defender URBAC: `Custom detections`, `Advanced hunting`, `Advanced live response`; Azure RBAC: `Microsoft Sentinel Contributor` + `Logic App Contributor` | **Eligible en PIM** (**4 a 8 horas**, justificación obligatoria + MFA resistente a phishing). | Despliegue de detecciones y playbooks gobernado como código (GitHub/Azure DevOps con Pull Request aprobado); consultas auditadas en `LAQueryLogs`. | `[Verificado MS Learn]` / `[Decisión / Propuesta Editorial]` |
| **Domain Platform Admins (IAM, Endpoint, Purview)** | Ingeniería / `PROTECT` | Entra: `Authentication Policy Admin`, `Conditional Access Admin`; Intune: `Intune Administrator`; Purview: `Information Protection Admin`, `DLP Compliance Admin` | **100% Eligible en PIM** (máximo **4 horas**; `Privileged Role Administrator` exige **aprobación dual** y *Authentication Context* FIDO2). | Separación estricta entre administración de Identidad, Endpoints y Datos; menos de **5** `Global Administrators` elegibles en todo el tenant. | `[Verificado MS Learn]` / `[Decisión / Propuesta Editorial]` |
| **AI & Agent Governance Lead** | Gobierno Agéntico / `GOVERN` & `PROTECT` | Admin Center / Entra: `Agent ID Administrator` / `Application Administrator` + `Security Copilot Contributor` | **Eligible en PIM** (**4 horas**, ticket de alta de *Blueprint* + MFA resistente a phishing). | Aprueba *Agent Identity Blueprints*, *Sponsors* en **Agent 365** y cuotas SCU; segregado de los creadores funcionales de agentes en unidades de negocio. | `[Verificado MS Learn]` / `[Decisión / Propuesta Editorial]` |

---

## 5. Cadencia Operativa Diaria

### D-01: Supervisión Matutina de Cola Unificada de Incidentes Críticos y Traspaso 24x7 (SIEM + XDR)
- **Objetivo:** Garantizar control diario sobre todo incidente `Critical` o `High`, verificando ausencia de casos huérfanos, adherencia a `MTTA <= 15 min` y calidad del traspaso nocturno o del MSSP `[Decisión / Propuesta Editorial]`.
- **Consola y Ruta Exacta:** `https://security.microsoft.com` > `Investigation & response` > `Incidents & alerts` > `Incidents` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC Manager / Analista Líder de Turno (SOC L2) `[Decisión / Propuesta Editorial]`.
- **Procedimiento Operativo Numerado:**
  1. Aplicar filtro `Severity: Critical, High` y `Status: New, In progress`, ordenando de más antiguo a más reciente `[Verificado MS Learn]`.
  2. Verificar que el 100% de los incidentes tengan propietario nominal asignado, etiquetas de contexto y lista de tareas activa en *Case Management* `[Verificado MS Learn]`.
  3. Revisar el resumen ejecutivo generado por **Microsoft Security Copilot** en cada incidente mayor y contrastarlo con las evidencias crudas del grafo de ataque `[Verificado MS Learn]`.
  4. Escalar de inmediato al CSIRT Lead cualquier incidente con afectación sobre activos etiquetados como *Crown Jewels* o cuentas privilegiadas `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Captura/exportación diaria de `SecurityIncident` demostrando cero incidentes `Critical/High` sin propietario > 15 minutos (`DE.AE-02`, `RS.MA-02`) `[Decisión / Propuesta Editorial]`.

### D-02: Revisión Human-ON-the-Loop del Action Center y Contenciones de Automatic Attack Disruption
- **Objetivo:** Auditar todas las respuestas autónomas ejecutadas a velocidad de máquina en las últimas 24 horas y destrabar acciones pendientes de aprobación humana `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://security.microsoft.com` > `Investigation & response` > `Actions & submissions` > `Action center` (`Pending` y `History`) `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L2 / SOC L3 `[Decisión / Propuesta Editorial]`.
- **Procedimiento Operativo Numerado:**
  1. Inspeccionar en `Incidents` todos los expedientes marcados con el banner amarillo y etiqueta **`Attack Disruption`** `[Verificado MS Learn]`.
  2. Verificar en `Action center > History` el alcance de las acciones automáticas ejecutadas (`Contain device`, `Isolate device`, `Contain user`, `Disable user` en AD/Entra, `Revoke user session`, `OAuth app compromise`) `[Verificado MS Learn]`.
  3. Aprobar o rechazar en menos de 2 horas las remediaciones pendientes en `Action center > Pending` originadas por investigaciones automatizadas (`AIR`) o agentes supervisados `[Decisión / Propuesta Editorial]`.
  4. Confirmar que ningún activo contenido sea liberado (*Undo*) sin haber completado previamente la erradicación forense de persistencia `[Verificado MS Learn]`.
- **Evidencia Auditable:** Exportación del historial diario de `Action center` con usuario aprobador, activo afectado y timestamp (`RS.MI-01`) `[Verificado MS Learn]`.

### D-03: Verificación Diaria de Salud de Conectores, Telemetría XDR y Consumo en Sentinel
- **Objetivo:** Detectar en menos de 24 horas interrupciones silenciosas en conectores de datos, sensores de dominio o desvíos anómalos de facturación `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://security.microsoft.com` > `Microsoft Sentinel` > `Configuration` > `Data connectors` y `System` > `Settings` > `Microsoft Defender XDR` `[Verificado MS Learn]`.
- **Rol Responsable:** Platform / SIEM Engineer `[Decisión / Propuesta Editorial]`.
- **Procedimiento Operativo Numerado:**
  1. Consultar la tabla `SentinelHealth` filtrando `Status != "Success"` en las últimas 24 horas para detectar fallos de autenticación o API en conectores CCF, AMA/DCR o multicloud `[Verificado MS Learn]`.
  2. Verificar latencia y flujo continuo en tablas críticas (`EntraIdSignInEvents`, `DeviceProcessEvents`, `EmailEvents`, `IdentityLogonEvents`, `OfficeActivity`) y salud de sensores de **Defender for Identity** `[Verificado MS Learn]`.
  3. Validar la ingesta diaria acumulada en GB frente a la línea base presupuestada y la absorción del **M365 E5 Data Grant** `[Verificado MS Learn]`.
- **Evidencia Auditable:** Resultado diario de consulta KQL de salud de ingesta registrado en Workbook operativo (`DE.CM-01`, `PR.IR-01`) `[Verificado MS Learn]`.

### D-04: Vigilancia de Cuentas Break-Glass y Elevaciones Privilegiadas Fuera de Estándar
- **Objetivo:** Confirmar ausencia absoluta de actividad no autorizada en cuentas de emergencia y auditar toda elevación administrativa sensible del día anterior `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://entra.microsoft.com` > `Identity` > `Monitoring & health` > `Sign-in logs` / `Audit logs` y `Identity governance` > `Privileged Identity Management` > `Resource audit` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L2 + Identity Security Analyst `[Decisión / Propuesta Editorial]`.
- **Procedimiento Operativo Numerado:**
  1. Verificar que las cuentas **Break-Glass** (`*.onmicrosoft.com`) registren cero inicios de sesión o intentos fallidos no programados `[Verificado MS Learn]`.
  2. Auditar en `PIM > Resource audit` todas las activaciones de roles Tier-0 (`Global Administrator`, `Privileged Role Administrator`, `Security Administrator`, `Conditional Access Administrator`), validando justificación y correspondencia con tickets reales `[Decisión / Propuesta Editorial]`.
  3. Investigar como incidente potencial cualquier evento `Add member to role` ejecutado directamente fuera del flujo de `MS-PIM` o fuera de ventana horaria habitual `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Bitácora diaria conciliada de `AuditLogs` para cambios de roles y estado de alerta Severidad 0 Break-Glass (`PR.AA-05`, `GV.OV-03`) `[Verificado MS Learn]`.

### D-05: Triaje Integrado de Riesgo de Usuarios, Workload Identities y Agentes IA
- **Objetivo:** Remediación rápida de identidades humanas, principales de servicio y agentes autónomos marcados en riesgo medio/alto en **Microsoft Entra ID Protection** `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://entra.microsoft.com` > `ID Protection` > `Risky users`, `Risky workload identities` y `Risky agents` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L1/L2 (ITDR) `[Decisión / Propuesta Editorial]`.
- **Procedimiento Operativo Numerado:**
  1. Filtrar entidades con `Risk state == At risk` y `Risk level == High` que no hayan sido remediadas automáticamente por políticas de Conditional Access `[Verificado MS Learn]`.
  2. Investigar detecciones críticas (`anomalousToken`, `leakedCredentials`, `mcasImpossibleTravel`, `earlyLifeMaliciousActivity`, `entraDirectoryReconnaissance`, `suspiciousCredentialUsage`) cruzando con `EntraIdSignInEvents` y `EntraIdSpnSignInEvents` `[Verificado MS Learn]`.
  3. Ejecutar `Confirm compromise`, revocación de tokens o deshabilitación inmediata en caso de compromiso real, o `Dismiss risk` documentado tras verificación fehaciente `[Verificado MS Learn]`.
- **Evidencia Auditable:** Exportación de colas de riesgo mostrando remediación de 100% de casos `High` en `< 4 horas` (`DE.CM-03`, `RS.MI-01`) `[Decisión / Propuesta Editorial]`.

### D-06: Monitoreo Diario de Alertas de Exfiltración (Purview DLP) e Insider Risk Adaptive Protection
- **Objetivo:** Conectar la telemetría de seguridad de datos de **Microsoft Purview** con la operación diaria de respuesta para frenar fugas críticas de información `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com` > `Solutions` > `Data Loss Prevention` > `Alerts` y cola integrada en `https://security.microsoft.com` `[Verificado MS Learn]`.
- **Rol Responsable:** Data Security Analyst / SOC L2 autorizado `[Decisión / Propuesta Editorial]`.
- **Procedimiento Operativo Numerado:**
  1. Revisar alertas DLP de severidad `High` por carga a dominios cloud no corporativos, copiado a USB, impresión masiva o pegado de datos confidenciales en prompts de IA no autorizados `[Verificado MS Learn]`.
  2. Verificar que los usuarios asignados dinámicamente al nivel *Elevated risk* en **Insider Risk Management** estén recibiendo controles preventivos automáticos vía **Adaptive Protection** `[Verificado MS Learn]`.
  3. Escalar incidentes confirmados de exfiltración dolosa al protocolo confidencial conjunto con Legal, Privacidad y Recursos Humanos `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Registro de triaje de alertas DLP de severidad alta dentro del SLA de 24 horas en `Purview Audit` (`PR.DS-01`, `PR.DS-10`) `[Verificado MS Learn]`.

### D-07: Evaluación Diaria de Inteligencia de Amenazas Críticas y Zero-Days (Threat Analytics / KEV)
- **Objetivo:** Determinar diariamente la exposición real de la organización frente a nuevas campañas globales de actores de amenaza y vulnerabilidades en explotación activa `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://security.microsoft.com` > `Threat intelligence` > `Threat analytics` y `Exposure management` > `Vulnerability management` `[Verificado MS Learn]`.
- **Rol Responsable:** Threat Intelligence Analyst / SOC L3 `[Decisión / Propuesta Editorial]`.
- **Procedimiento Operativo Numerado:**
  1. Revisar los boletines de **Threat analytics** publicados en las últimas 24 horas ordenando por activos expuestos o mal configurados en el propio tenant `[Verificado MS Learn]`.
  2. Identificar presencia de CVEs recién añadidos a CISA KEV o con puntaje EPSS crítico sobre activos expuestos a internet o servidores Tier-0 `[Verificado MS Learn]`.
  3. Disparar orden de mitigación inmediata (parche fuera de banda en Intune/Azure Update Manager, regla ASR o bloqueo de indicadores) con SLA de 24 a 48 horas `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Bitácora diaria de inteligencia evaluada y órdenes de parchado de emergencia vinculadas (`ID.RA-01`, `ID.RA-02`) `[Decisión / Propuesta Editorial]`.

---

## 6. Cadencia Operativa Semanal

### S-01: Sincronización Operativa Semanal SOC Interno + MSSP y Calibración de Falsos Positivos
- **Objetivo:** Gobernar semanalmente la eficiencia operativa del modelo híbrido, validando tiempos de respuesta, precisión de escalamiento y reducción sistemática de ruido `[Decisión / Propuesta Editorial]`.
- **Consola y Ruta Exacta:** `https://security.microsoft.com` > `Microsoft Sentinel` > `Threat management` > `Workbooks` (*Security Operations Efficiency*) `[Verificado MS Learn]`.
- **Rol Responsable:** SOC Manager + Líder Operativo del MSSP + Detection Lead `[Decisión / Propuesta Editorial]`.
- **Procedimiento Operativo Numerado:**
  1. Analizar las métricas semanales de MTTA, MTTC, volumen de alertas a incidentes y porcentaje de cierres por `FalsePositive` y `BenignPositive` `[Verificado MS Learn]`.
  2. Revisar muestra aleatoria del 10% de incidentes cerrados por el MSSP para auditar calidad investigativa y adherencia a runbooks aprobados `[Decisión / Propuesta Editorial]`.
  3. Seleccionar las 5 reglas o políticas más ruidosas de la semana e ingresarlas al backlog semanal de ajuste (*tuning*) sin degradar cobertura real `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Acta semanal de sincronización SOC-MSSP y backlog de tuning ejecutado (`GV.SC-07`, `ID.IM-02`) `[Decisión / Propuesta Editorial]`.

### S-02: Gestión Semanal de Rutas de Ataque Críticas y Chokepoints en Exposure Management
- **Objetivo:** Reducir proactivamente el riesgo de compromiso lateral cerrando los cuellos de botella técnicos (*chokepoints*) que exponen activos críticos `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://security.microsoft.com` > `Exposure management` > `Exposure insights` > `Attack paths` / `Chokepoints` / `Initiatives` `[Verificado MS Learn]`.
- **Rol Responsable:** Cybersecurity Architect + Vulnerability Management Lead `[Decisión / Propuesta Editorial]`.
- **Procedimiento Operativo Numerado:**
  1. Inspeccionar las rutas de ataque activas que finalizan en activos críticos (*Crown Jewels*), tales como dispositivos con credenciales privilegiadas cacheadas, VMs con IPs públicas o permisos excesivos en la nube `[Verificado MS Learn]`.
  2. Priorizar la remediación de los **Chokepoints** principales para maximizar el número de rutas de ataque rotas por cada hora de ingeniería invertida `[Verificado MS Learn]`.
  3. Seguimiento del puntaje de progreso semanal en las **Initiatives** estratégicas (*Zero Trust*, *Ransomware Protection*, *Cloud Security*) `[Verificado MS Learn]`.
- **Evidencia Auditable:** Exportación semanal de rutas de ataque críticas mitigadas y evolución de *Initiatives* en MSEM (`ID.RA-05`, `ID.IM-01`) `[Verificado MS Learn]`.

### S-03: Optimización Semanal del SOC y Disciplina FinOps (SOC Optimization + Data Lake + SCUs)
- **Objetivo:** Maximizar la cobertura de detección por dólar invertido optimizando niveles de almacenamiento en Sentinel y consumo de **Security Copilot** `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://security.microsoft.com` > `Microsoft Sentinel` > `Configuration` > `SOC optimization` y `https://securitycopilot.microsoft.com` `[Verificado MS Learn]`.
- **Rol Responsable:** Sentinel Platform Engineer + FinOps Security Analyst `[Decisión / Propuesta Editorial]`.
- **Procedimiento Operativo Numerado:**
  1. Revisar y aplicar recomendaciones de **SOC optimization** para cubrir tácticas MITRE ATT&CK v18 deficitarias y detectar tablas de baja utilidad analítica `[Verificado MS Learn]`.
  2. Mover fuentes verbosas secundarias desde el **Analytics tier** hacia el **Sentinel Data Lake** mediante transformaciones pre-ingesta en **Data Collection Rules (DCR)** `[Verificado MS Learn]`.
  3. Auditar el consumo semanal de **SCUs** (incluidas en E5/E7 vs. aprovisionadas/overage en Azure) identificando agentes o prompts ineficientes `[Verificado MS Learn]`.
- **Evidencia Auditable:** Reporte semanal FinOps SecOps con GB/día ahorrados, utilización de *E5 Data Grant* y consumo de SCUs (`GV.RM-03`, `ID.IM-02`) `[Verificado MS Learn]`.

### S-04: Campaña Semanal Estructurada de Threat Hunting Guiado por Hipótesis
- **Objetivo:** Detectar adversarios persistentes que operan con credenciales válidas o herramientas nativas sin disparar reglas estáticas `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://security.microsoft.com` > `Investigation & response` > `Hunting` > `Advanced hunting` y `Microsoft Sentinel` > `Hunting` `[Verificado MS Learn]`.
- **Rol Responsable:** Threat Hunter interno (SOC L3) `[Decisión / Propuesta Editorial]`.
- **Procedimiento Operativo Numerado:**
  1. Definir hipótesis semanal anclada en inteligencia sectorial reciente o técnicas de evasión sobre identidad, endpoints, SaaS o agentes IA `[Decisión / Propuesta Editorial]`.
  2. Ejecutar caza KQL correlacionando tablas XDR (30 días interactivos) e histórico en **Sentinel Data Lake** con apoyo de **Security Copilot** `[Verificado MS Learn]`.
  3. Registrar hallazgos con *Bookmarks*, abrir incidente si se detecta compromiso y promover la consulta validada como nueva regla programada o **Custom Detection Rule** `[Verificado MS Learn]`.
- **Evidencia Auditable:** Registro semanal de campaña *Hunt* completada y nuevas detecciones incorporadas al catálogo (`DE.CM-09`, `DE.AE-05`) `[Verificado MS Learn]`.

### S-05: Control Semanal de Deriva de Configuración y Promoción de Políticas Report-Only
- **Objetivo:** Evitar regresiones en la postura preventiva y completar el ciclo seguro de despliegue de políticas nuevas o administradas por Microsoft `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://entra.microsoft.com` > `Conditional Access`, `https://intune.microsoft.com` y `https://purview.microsoft.com` `[Verificado MS Learn]`.
- **Rol Responsable:** Cybersecurity Architect + Líderes de IAM, Endpoints y Purview `[Decisión / Propuesta Editorial]`.
- **Procedimiento Operativo Numerado:**
  1. Ejecutar batería automatizada de pruebas de postura como código (ej. **Maester** sobre Entra/M365) para detectar modificaciones no autorizadas o exclusiones vencidas `[Decisión / Propuesta Editorial]`.
  2. Evaluar telemetría de impacto de políticas en `Report-only` (incluyendo **Microsoft-managed Conditional Access policies** antes de su ventana de auto-activación de 45 días) `[Verificado MS Learn]`.
  3. Promover a estado `On` las políticas validadas sin bloqueo accidental de procesos críticos `[Verificado MS Learn]`.
- **Evidencia Auditable:** Reporte HTML/JSON semanal de pruebas automatizadas de postura y bitácora CAB de políticas promovidas (`GV.PO-02`, `PR.PS-01`) `[Decisión / Propuesta Editorial]`.

### S-06: Gobierno Semanal del Inventario de Agentes IA (Agent 365), Apps OAuth y Shadow AI
- **Objetivo:** Mantener visibilidad y control continuo sobre la proliferación de agentes autónomos, aplicaciones OAuth de terceros y servicios GenAI externos `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://admin.microsoft.com` > `Agents` (**Microsoft Agent 365**), `https://entra.microsoft.com` > `Agent ID` y `https://security.microsoft.com` > `Cloud apps` `[Verificado MS Learn]`.
- **Rol Responsable:** AI & Agent Governance Lead + Cloud App Security Admin `[Decisión / Propuesta Editorial]`.
- **Procedimiento Operativo Numerado:**
  1. Revisar altas semanales en **Microsoft Agent 365** y **Entra Agent ID**, verificando que ningún agente opere sin *Sponsor* humano válido, *Blueprint* autorizado ni políticas de **Conditional Access for agents** `[Verificado MS Learn]`.
  2. Auditar en **Defender for Cloud Apps** nuevos consentimientos OAuth con alcances de lectura/escritura amplia y tráfico descubierto hacia aplicaciones de IA generativa de alto riesgo `[Verificado MS Learn]`.
  3. Revocar aplicaciones o agentes fuera de política y ajustar controles de bloqueo o advertencia en **Purview DSPM for AI** y **Global Secure Access** `[Verificado MS Learn]`.
- **Evidencia Auditable:** Inventario semanal conciliado de agentes IA y aplicaciones OAuth gobernadas (`ID.AM-02`, `PR.AA-05`, `GV.SC-04`) `[Verificado MS Learn]`.

---

## 7. Cadencia Operativa Mensual

### M-01: Comité Operativo Mensual de la Oficina del CISO (Métricas de Altitud 2 y Sostenibilidad)
- **Objetivo:** Evaluar mensualmente la efectividad operativa, reducción de deuda técnica y salud organizacional del equipo de ciberseguridad junto a líderes de TI y Operaciones `[Decisión / Propuesta Editorial]`.
- **Consola y Ruta Exacta:** Tablero Operacional Power BI / Workbooks consolidados de `Exposure Management`, `Sentinel`, `Entra` y `Purview` `[Decisión / Propuesta Editorial]`.
- **Rol Responsable:** CISO + Reportes Directos de Seguridad `[Decisión / Propuesta Editorial]`.
- **Procedimiento Operativo Numerado:**
  1. Analizar la evolución mensual de los KPIs maestros (MTTA/MTTC, cobertura MFA phishing-resistant, rutas críticas MSEM, tasa de automatización e incidentes por dominio) `[Decisión / Propuesta Editorial]`.
  2. Revisar indicadores humanos de sostenibilidad: relación carga de trabajo vs. capacidad disponible (meta <=85%), horas en guardia nocturna y cumplimiento del 20% de tiempo de formación Kaizen `[Decisión / Propuesta Editorial]`.
  3. Aprobar reasignaciones de prioridad y planes correctivos a 30 días para cualquier indicador en desviación `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Paquete mensual de gestión de la Oficina del CISO y seguimiento de acciones CAPA (`GV.OV-01`, `GV.RR-03`) `[Decisión / Propuesta Editorial]`.

### M-02: Revisión Mensual de Postura Preventiva en Secure Score y Purview Compliance Manager
- **Objetivo:** Verificar el avance continuo del endurecimiento técnico multi-carga y el grado de cumplimiento frente a marcos normativos activos `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://security.microsoft.com` > `Exposure management` > `Secure score` y `https://purview.microsoft.com` > `Solutions` > `Compliance Manager` `[Verificado MS Learn]`.
- **Rol Responsable:** GRC Manager + Cybersecurity Architect `[Decisión / Propuesta Editorial]`.
- **Procedimiento Operativo Numerado:**
  1. Registrar el puntaje mensual de **Microsoft Secure Score** global y por pilar (Identidad, Dispositivos, Apps, Datos), investigando cualquier caída superior a 2 puntos `[Verificado MS Learn]`.
  2. Revisar el **Compliance Score** y el estado de pruebas de controles técnicos en las evaluaciones de **NIST CSF 2.0**, **ISO 27001** y normativas sectoriales dentro de **Compliance Manager** `[Verificado MS Learn]`.
  3. Comprometer con los equipos de plataforma el cierre mensual de un lote priorizado de acciones de mejora `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Reporte mensual exportado de *Secure Score* y *Compliance Manager* archivado con control de versiones (`ID.IM-01`, `GV.OV-02`) `[Verificado MS Learn]`.

### M-03: Auditoría Mensual de Higiene Privilegiada (PIM) y Revisiones de Acceso Críticas
- **Objetivo:** Garantizar la ausencia de acumulación de privilegios (*privilege creep*) en los cinco portales de administración `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://entra.microsoft.com` > `Identity governance` > `Privileged Identity Management` > `Alerts` y `Access reviews` `[Verificado MS Learn]`.
- **Rol Responsable:** Identity Governance Lead + GRC Auditor `[Decisión / Propuesta Editorial]`.
- **Procedimiento Operativo Numerado:**
  1. Auditar y remediar todas las alertas de configuración en **PIM**, asegurando cero roles críticos sin exigencia de MFA y cero asignaciones permanentes fuera de las dos cuentas Break-Glass `[Verificado MS Learn]`.
  2. Confirmar que la cantidad de usuarios elegibles para `Global Administrator` se mantenga en `< 5` `[Verificado MS Learn]`.
  3. Validar la finalización y remoción automática de permisos no renovados en campañas mensuales de **Access Reviews** sobre invitados B2B y grupos operativos del MSSP (articulado con el Módulo `02`) `[Verificado MS Learn]`.
- **Evidencia Auditable:** Instantánea mensual CSV de asignaciones PIM (`Active`/`Eligible`) e informes firmados de *Access Reviews* (`PR.AA-05`, `GV.RR-02`) `[Verificado MS Learn]`.

### M-04: Auditoría Mensual de Adopción, Licenciamiento y ROI del Ecosistema M365 E5 / E7
- **Objetivo:** Asegurar el aprovechamiento pleno de las capacidades contratadas, evitando tanto brechas de cumplimiento de licencias como gasto ocioso `[Decisión / Propuesta Editorial]`.
- **Consola y Ruta Exacta:** `https://admin.microsoft.com` > `Billing` > `Licenses` y `https://portal.azure.com` > `Cost Management + Billing` `[Verificado MS Learn]`.
- **Rol Responsable:** FinOps Security Lead + Office of the CISO `[Decisión / Propuesta Editorial]`.
- **Procedimiento Operativo Numerado:**
  1. Verificar que el 100% de los usuarios cubiertos por políticas avanzadas (Entra ID P2, Defender Suite, Purview Suite, Intune Suite, Agent 365 / M365 E7) cuenten con la licencia correspondiente correctamente asignada `[Verificado MS Learn]`.
  2. Recuperar licencias asignadas a cuentas dadas de baja, buzones compartidos que no las requieran o usuarios inactivos > 60 días `[Decisión / Propuesta Editorial]`.
  3. Evaluar la eficiencia de los **Commitment Tiers** de Sentinel y la capacidad aprovisionada de **Security Copilot** frente a la demanda real del mes `[Verificado MS Learn]`.
- **Evidencia Auditable:** Conciliación mensual FinOps de licenciamiento y consumo cloud de seguridad (`GV.RM-01`, `GV.RR-03`) `[Decisión / Propuesta Editorial]`.

### M-05: Evaluación Mensual Independiente de SLAs de Resultado del MSSP / MXDR
- **Objetivo:** Auditar objetivamente al proveedor de operaciones externalizadas contra cláusulas basadas en resultados (*outcomes*) `[Decisión / Propuesta Editorial]`.
- **Consola y Ruta Exacta:** `https://security.microsoft.com` > `Microsoft Sentinel` > `Workbooks` y repositorio contractual TPRM `[Verificado MS Learn]`.
- **Rol Responsable:** Vendor Performance Manager (Oficina del CISO) + SOC Manager `[Decisión / Propuesta Editorial]`.
- **Procedimiento Operativo Numerado:**
  1. Extraer directamente de `SecurityIncident` y `AuditLogs` las métricas independientes del mes: tiempo de notificación P1 (`<= 15 min`), tasa de falsos positivos escalados (`< 10%`) y calidad narrativa de investigaciones `[Decisión / Propuesta Editorial]`.
  2. Verificar que toda nueva detección o runbook desarrollado para el entorno haya quedado documentado en el repositorio interno del cliente `[Decisión / Propuesta Editorial]`.
  3. Celebrar reunión mensual de gobierno de servicio documentando penalizaciones, créditos o mejoras acordadas `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Scorecard mensual independiente del MSSP y acta firmada de revisión de servicio (`GV.SC-07`, `GV.OV-03`) `[Decisión / Propuesta Editorial]`.

### M-06: Medición Mensual de Resiliencia Humana mediante Attack Simulation Training
- **Objetivo:** Reducir de forma sostenida la tasa de compromiso humano ante vectores modernos de ingeniería social `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://security.microsoft.com` > `Email & collaboration` > `Attack simulation training` `[Verificado MS Learn]`.
- **Rol Responsable:** Security Awareness Lead + MDO Administrator `[Decisión / Propuesta Editorial]`.
- **Procedimiento Operativo Numerado:**
  1. Ejecutar simulación mensual dirigida empleando técnicas realistas (captura de credenciales, adjunto malicioso, código QR, consentimiento OAuth) `[Verificado MS Learn]`.
  2. Analizar la tasa de clics/compromiso frente a la tasa de reporte activo de correos sospechosos por departamento y rol crítico `[Verificado MS Learn]`.
  3. Auditar el cumplimiento dentro de plazo de las cápsulas formativas asignadas automáticamente a los usuarios que fallaron la prueba `[Verificado MS Learn]`.
- **Evidencia Auditable:** Informe mensual exportado de *Attack Simulation Training* con tendencia histórica de reducción de compromiso (`PR.AT-01`) `[Verificado MS Learn]`.

---

## 8. Cadencias Trimestral, Semestral y Anual

### T-01 (Trimestral): Presentación Ejecutiva al Comité de Riesgos y Board of Directors (Altitud 1)
- **Objetivo:** Informar al Consejo de Administración el estado fiduciario del riesgo cibernético en términos financieros (**Open FAIR**), cumplimiento regulatorio y retorno de inversión `[Decisión / Propuesta Editorial]`.
- **Consola y Ruta Exacta:** Scorecard Ejecutivo Trimestral alimentado por `Exposure Management`, `Purview Compliance Manager`, `Sentinel` y `Risk Register` `[Decisión / Propuesta Editorial]`.
- **Rol Responsable:** CISO `[Decisión / Propuesta Editorial]`.
- **Procedimiento Operativo Numerado:**
  1. Recalcular la exposición financiera residual (*ALE*) de los escenarios de riesgo principales y contrastarla con el umbral de apetito de riesgo vigente `[Decisión / Propuesta Editorial]`.
  2. Exponer la evolución intertrimestral del *Cyber Resilience Scorecard*: alineación con apetito de riesgo, cumplimiento regulatorio, incidentes materiales contenidos, tiempo de recuperación de negocio y madurez del SOC Agéntico `[Decisión / Propuesta Editorial]`.
  3. Documentar formalmente en acta del Directorio las decisiones de inversión, transferencia aseguradora o aceptación explícita de riesgo `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Presentación ejecutiva al Board y acta firmada del Comité de Riesgos/Auditoría (`GV.OV-01`, `GV.RM-02`, `GV.RR-01`) `[Decisión / Propuesta Editorial]`.

### T-02 (Trimestral): Ejercicio Purple Team Multi-Dominio y Prueba Obligatoria Break-Glass (90 Días)
- **Objetivo:** Validar en producción controlada la eficacia real de detección/bloqueo frente a TTPs adversarias vigentes y la disponibilidad operativa de las cuentas de emergencia `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://security.microsoft.com` y `https://entra.microsoft.com` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L3 / Purple Team Lead + Identity Lead `[Decisión / Propuesta Editorial]`.
- **Procedimiento Operativo Numerado:**
  1. Ejecutar campaña trimestral *Purple Team* simulando cadenas completas de ataque (ej. phishing AiTM -> robo de sesión -> reconocimiento en Entra -> movimiento lateral -> intento de exfiltración SharePoint) `[Decisión / Propuesta Editorial]`.
  2. Ejecutar el simulacro trimestral mandatorio (**al menos cada 90 días**) de las cuentas **Break-Glass** autenticando con llave física **FIDO2** o **CBA** desde una **PAW**, verificando que no sean bloqueadas por Conditional Access y que disparen la alerta crítica Severidad 0 al SOC `[Verificado MS Learn]`.
  3. Registrar y cerrar brechas de detección o telemetría identificadas durante las pruebas `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Reporte trimestral *Purple Team* con delta de cobertura MITRE ATT&CK y acta firmada de prueba Break-Glass (`ID.IM-02`, `PR.AA-01`, `DE.AE-02`) `[Verificado MS Learn]`.

### SM-01 (Semestral): Simulacro Integral de Crisis Ejecutiva, Continuidad (BCP/DRP) y Traspaso MSSP
- **Objetivo:** Validar de extremo a extremo la capacidad de comando de crisis, comunicación externa, coordinación con el MSSP/IR Retainer y recuperación tecnológica ante un evento disruptivo severo `[Decisión / Propuesta Editorial]`.
- **Consola y Ruta Exacta:** Entorno de crisis out-of-band + `https://security.microsoft.com` + infraestructura de respaldo `[Decisión / Propuesta Editorial]`.
- **Rol Responsable:** CISO + CSIRT Lead + Líder Corporativo BCDR + Legal/Comunicaciones `[Decisión / Propuesta Editorial]`.
- **Procedimiento Operativo Numerado:**
  1. Conducir simulacro ejecutivo (*Tabletop*) con participación activa de C-Level, Legal, RRPP, TI y representantes del MSSP sobre un escenario de extorsión cibernética o indisponibilidad crítica `[Decisión / Propuesta Editorial]`.
  2. Ejecutar en paralelo validación técnica de restauración limpia de cargas críticas verificando el cumplimiento real de objetivos RTO/RPO y escaneo de seguridad previo a reconexión `[Decisión / Propuesta Editorial]`.
  3. Incorporar hallazgos al Plan de Respuesta a Incidentes (IRP), planes DRP y anexos operativos del contrato MSSP `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Informe semestral de ejercicio de crisis y continuidad junto con versiones actualizadas del IRP/BCP (`GV.SC-08`, `RS.MA-01`, `RC.RP-01`, `RC.CO-01`) `[Decisión / Propuesta Editorial]`.

### A-01 (Anual): Autoevaluación Anual NIST CSF 2.0 (Patrón SFI), Zero Trust Assessment y Revisión del Manifiesto
- **Objetivo:** Medir formalmente la madurez anual en las 6 funciones y 22 categorías de NIST CSF 2.0 conforme al patrón oficial de Microsoft SFI, actualizando la estrategia plurianual `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com` > `Compliance Manager` y herramienta **Microsoft Zero Trust Assessment** `[Verificado MS Learn]`.
- **Rol Responsable:** CISO + GRC Lead + Enterprise Cybersecurity Architect `[Decisión / Propuesta Editorial]`.
- **Procedimiento Operativo Numerado:**
  1. Definir el alcance anual basado en riesgo y calificar el *Perfil Actual* vs. *Perfil Objetivo* en las 106 subcategorías de **NIST CSF 2.0** empleando *Implementation Tiers* (1 a 4) y dominios **C2M2** `[Verificado MS Learn]`.
  2. Correr la evaluación técnica automatizada **Microsoft Zero Trust Assessment** sobre el tenant para respaldar cada calificación con configuración verificable `[Verificado MS Learn]`.
  3. Renovar la Declaración de Apetito de Riesgo, actualizar el **Manifiesto de Excelencia Operacional**, alinear el roadmap a **SAF / MCRA** y presentar el presupuesto anual ante el Directorio `[Verificado MS Learn]`.
- **Evidencia Auditable:** Informe anual completo *NIST CSF 2.0 Maturity Assessment*, exportación *Zero Trust Assessment* y Plan Estratégico Anual aprobado (`GV.OC-01`, `GV.RM-01`, `GV.PO-02`, `ID.IM-03`) `[Verificado MS Learn]`.

---

## 9. Operaciones Ad-Hoc y Playbooks de Respuesta a Incidentes / Eventos Críticos

### AH-01: Activación de Crisis Mayor (P1), Contención Coordinada XDR y Gobierno Ejecutivo de Respuesta
- **Disparador:** Ataque activo de ransomware humano, compromiso confirmado de plano de control (Entra ID / AD Tier-0 / Suscripción Azure raíz), exfiltración crítica en curso o múltiples contenciones simultáneas de **Automatic Attack Disruption** `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://security.microsoft.com` > `Incidents`, puente de comunicaciones out-of-band y activación de **IR Retainer / Microsoft Incident Response** `[Verificado MS Learn]`.
- **Secuencia Operativa Numerada:**
  1. Declarar incidente mayor P1 en `<= 15 minutos`, designar formalmente al Incident Commander interno y activar sala de guerra fuera de banda si existe sospecha sobre canales colaborativos habituales `[Decisión / Propuesta Editorial]`.
  2. Validar y extender la contención inmediata en `security.microsoft.com`: aislar máquinas comprometidas en MDE, suspender cuentas y revocar sesiones en Entra ID/AD y bloquear IPs/dominios/apps OAuth maliciosas `[Verificado MS Learn]`.
  3. Activar preservación probatoria inmutable (*Legal Hold* en **Purview eDiscovery Premium** y congelamiento de logs en **Purview Audit** / **Sentinel Data Lake**) `[Verificado MS Learn]`.
  4. Coordinar con Legal, Privacidad y Dirección Ejecutiva las notificaciones obligatorias a reguladores, aseguradora cibernética y partes afectadas dentro de los plazos legales `[Decisión / Propuesta Editorial]`.
  5. Dirigir la erradicación total de persistencia, autorizar la recuperación escalonada validando integridad (`RC.RP-05`) y emitir el informe Post-Incident Review (PIR) en un máximo de 7 días hábiles post-cierre `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Expediente integral del incidente P1, preservación forense con cadena de custodia, notificaciones legales y acta PIR con acciones CAPA (`RS.MA-01`, `RS.MI-01`, `RS.CO-02`, `RC.RP-05`) `[Verificado MS Learn]`.

### AH-02: Contención y Respuesta ante Compromiso o Deriva Maliciosa de Agentes de IA
- **Disparador:** Detección de riesgo alto en **ID Protection for agents** (`earlyLifeMaliciousActivity`, `entraDirectoryReconnaissance`, `suspiciousCredentialUsage`, `signInSpike`, `unfamiliarResourceAccess`), ataque exitoso de *Indirect Prompt Injection* o acceso anómalo de un agente a datos restringidos `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://entra.microsoft.com` > `ID Protection` > `Risky agents` y `https://admin.microsoft.com` > `Agents` (**Microsoft Agent 365**) `[Verificado MS Learn]`.
- **Secuencia Operativa Numerada:**
  1. En `Risky agents`, ejecutar de inmediato **Confirm compromise** (activando políticas de bloqueo de **Conditional Access for agents**) y **Disable** sobre la identidad del agente afectado (y su *Agent User* vinculado, si existiera) `[Verificado MS Learn]`.
  2. Si el incidente ocurrió en un flujo delegado *On-Behalf-Of (OBO)*, revocar inmediatamente los tokens de sesión del usuario humano sujeto e inspeccionar las credenciales del **Agent Identity Blueprint** padre `[Verificado MS Learn]`.
  3. Consultar los logs de inicio de sesión de agentes y **Purview Audit / DSPM for AI** para reconstruir todos los prompts, llamadas a servidores MCP y archivos accedidos o compartidos `[Verificado MS Learn]`.
  4. Convocar al *Sponsor* responsable registrado en **Agent 365** para corregir permisos excesivos, filtros de inyección de prompts y etiquetas de sensibilidad antes de considerar su reactivación `[Verificado MS Learn]`.
- **Evidencia Auditable:** Registro de evento `adminConfirmedAgentCompromised`, trazas forenses de actividad del agente e informe de remediación firmado por el *Sponsor* (`PR.AA-05`, `DE.CM-03`, `RS.MI-01`) `[Verificado MS Learn]`.

### AH-03: Ejecución de Emergencia y Auditoría Post-Mortem de Cuenta Break-Glass
- **Disparador:** Indisponibilidad total del proveedor de identidad federado, bloqueo administrativo accidental por política de Conditional Access, pérdida de todos los aprobadores PIM o disparo no planificado de la alerta crítica de monitoreo Break-Glass `[Verificado MS Learn]`.
- **Consola y Ruta:** Caja fuerte ignífuga física + **Privileged Access Workstation (PAW)** + `https://entra.microsoft.com` + `https://portal.azure.com` `[Verificado MS Learn]`.
- **Secuencia Operativa Numerada:**
  1. Si la alerta Severidad 0 se dispara sin autorización previa conocida, tratar el hecho como brecha crítica activa de Tier-0, bloquear el acceso desde la cuenta de emergencia secundaria y activar `AH-01` `[Verificado MS Learn]`.
  2. En emergencia operativa legítima autorizada por el CISO, retirar bajo custodia dual la llave **FIDO2** (o credencial **CBA**) de la bóveda segura e iniciar sesión exclusivamente desde una **PAW** `[Verificado MS Learn]`.
  3. Ejecutar únicamente el cambio mínimo indispensable para restaurar la administración nominal (ej. deshabilitar la política CA defectuosa o restablecer aprobadores PIM) y cerrar inmediatamente la sesión `[Verificado MS Learn]`.
  4. Extraer y resguardar `SigninLogs` y `AuditLogs` completos de la intervención, rotar combinaciones de custodia física si corresponde y celebrar sesión formal **Post-Mortem** dentro de las 48 horas siguientes `[Verificado MS Learn]`.
- **Evidencia Auditable:** Orden de apertura de emergencia, exportación inmutable de logs de la cuenta Break-Glass y dictamen del comité Post-Mortem (`PR.AA-01`, `GV.OV-03`) `[Verificado MS Learn]`.

### AH-04: Gobierno de Seguridad en Fusiones/Adquisiciones (M&A), Interconexión B2B o Cambio de MSSP
- **Disparador:** Integración de una empresa adquirida, apertura de colaboración `Cross-tenant` sensible con un proveedor Tier-1 o transición/terminación contractual del socio **MSSP** `[Decisión / Propuesta Editorial]`.
- **Consola y Ruta:** `https://entra.microsoft.com` > `External Identities` > `Cross-tenant access settings`, `https://security.microsoft.com` (Multi-tenant) y `https://portal.azure.com` (`Azure Lighthouse`) `[Verificado MS Learn]`.
- **Secuencia Operativa Numerada:**
  1. Ejecutar evaluación previa de diligencia debida (`GV.SC-06`) y correr **Microsoft Zero Trust Assessment** sobre el tenant externo antes de habilitar relaciones de confianza `[Verificado MS Learn]`.
  2. Configurar políticas restrictivas en `Cross-tenant access settings`, exigiendo reconocimiento explícito de MFA resistente a phishing y dispositivos conformes únicamente para organizaciones auditadas `[Verificado MS Learn]`.
  3. Conectar el nuevo entorno a **Defender Multi-Tenant Management** y **Sentinel** para visibilidad inmediata del SOC `[Verificado MS Learn]`.
  4. En caso de baja o reemplazo de un MSSP (`GV.SC-10`), eliminar en ventana coordinada todas las delegaciones **Azure Lighthouse / GDAP**, cuentas invitadas B2B, registros de aplicación API y verificar la entrega íntegra de playbooks y documentación en el repositorio propio `[Verificado MS Learn]`.
- **Evidencia Auditable:** Informe de debida diligencia cibernética, exportación de políticas *Cross-tenant* y acta de revocación limpia de accesos del proveedor saliente (`GV.SC-06`, `GV.SC-10`) `[Decisión / Propuesta Editorial]`.

### AH-05: Revisión y Decisión sobre Solicitudes de Customer Lockbox o Elevación Excepcional M365 PAM
- **Disparador:** Solicitud formal de acceso temporal a datos del cliente emitida por ingeniería de soporte de Microsoft (**Customer Lockbox**) o requerimiento interno de tarea administrativa crítica en cargas M365 (**Privileged Access Management**) `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://admin.microsoft.com` > `Settings` > `Org settings` > `Security & privacy` > `Customer Lockbox` / `Privileged access` `[Verificado MS Learn]`.
- **Secuencia Operativa Numerada:**
  1. Validar la existencia y legitimidad del ticket de soporte institucional que origina la solicitud, el alcance mínimo de los datos involucrados y la ventana estricta de expiración `[Verificado MS Learn]`.
  2. Someter la solicitud a aprobación por un responsable autorizado distinto de quien abrió el ticket (segregación de funciones) `[Verificado MS Learn]`.
  3. Auditar al cierre de la ventana todas las acciones registradas en **Purview Audit** bajo registros `CustomerLockbox` o `PrivilegedAccess` `[Verificado MS Learn]`.
- **Evidencia Auditable:** Historial de decisión de *Customer Lockbox / M365 PAM* y trazas de auditoría asociadas en Purview (`PR.DS-01`, `GV.SC-07`) `[Verificado MS Learn]`.

---

## 10. Consultas Técnicas, Telemetría y Verificación de Uso

### 10.1 Catálogo de Consultas KQL y Microsoft Graph para Gobierno Transversal

#### Consulta 1: Tablero Ejecutivo de Desempeño del SOC Unificado (MTTA, MTTC y Tasa de Falsos Positivos)
- **Plataforma / Tabla Principal:** Microsoft Sentinel / Defender Portal (`SecurityIncident`) `[Verificado MS Learn]`.
- **Propósito:** Medir de forma auditable e independiente (incluyendo supervisión sobre el MSSP) los tiempos medianos de atención y cierre junto con la precisión de las detecciones en los últimos 30 días.
```kql
// Deduplica por última actualización de cada incidente y calcula métricas reales por severidad
SecurityIncident
| where TimeGenerated > ago(30d)
| summarize arg_max(TimeGenerated, *) by IncidentNumber
| extend AckMinutes = iff(isnotempty(FirstModifiedTime), datetime_diff('minute', FirstModifiedTime, CreatedTime), real(null)),
         CloseHours = iff(Status == "Closed" and isnotempty(ClosedTime), round(datetime_diff('minute', ClosedTime, CreatedTime) / 60.0, 2), real(null))
| summarize TotalIncidents = count(),
            ActiveOpen = countif(Status != "Closed"),
            MedianMTTA_Min = percentile(AckMinutes, 50),
            P90_MTTA_Min = percentile(AckMinutes, 90),
            MedianMTTC_Hours = percentile(CloseHours, 50),
            TruePositives = countif(Classification == "TruePositive"),
            BenignPositives = countif(Classification == "BenignPositive"),
            FalsePositives = countif(Classification == "FalsePositive")
            by Severity
| extend FalsePositivePct = round(todouble(FalsePositives) * 100.0 / todouble(TotalIncidents), 2)
| order by case(Severity == "High", 1, Severity == "Medium", 2, Severity == "Low", 3, 4) asc
```

#### Consulta 2: Supervisión Human-ON-the-Loop de Incidentes Contenidos por Automatic Attack Disruption
- **Plataforma / Tabla Principal:** Microsoft Defender XDR / Sentinel (`SecurityIncident`) `[Verificado MS Learn]`.
- **Propósito:** Auditar todos los incidentes donde la IA de alta confianza (>=99% SNR) contuvo automáticamente activos para verificar remediación de causa raíz.
```kql
// Lista incidentes interrumpidos automáticamente en los últimos 14 días y su estado de investigación
SecurityIncident
| where TimeGenerated > ago(14d)
| summarize arg_max(TimeGenerated, *) by IncidentNumber
| where Title has "(attack disruption)" or tostring(Labels) has "Attack Disruption" or tostring(AdditionalData) has "AttackDisruption"
| project CreatedTime,
          IncidentNumber,
          Title,
          Severity,
          Status,
          AssignedTo = tostring(Owner.assignedTo),
          Classification,
          IncidentUrl
| order by CreatedTime desc
```

#### Consulta 3: Cobertura de MFA y Dispositivos Conformes sobre `EntraIdSignInEvents` (Esquema Vigente Post-Octubre 2026)
- **Plataforma / Tabla Principal:** Microsoft Defender XDR Advanced Hunting (`EntraIdSignInEvents`) `[Verificado MS Learn]`.
- **Propósito:** Validar cumplimiento Zero Trust sobre la nueva tabla nativa `EntraIdSignInEvents` (que reemplazó a `AADSignInEventsBeta` el `2026-10-19`).
```kql
// Mide proporción de autenticaciones interactivas internas protegidas con MFA y dispositivos conformes
EntraIdSignInEvents
| where Timestamp > ago(7d)
| where ErrorCode == 0 and LogonType has "interactive" and IsExternalUser == 0
| summarize TotalSignIns = count(),
            DistinctUsers = dcount(AccountUpn),
            MfaSignIns = countif(AuthenticationRequirement == "multiFactorAuthentication"),
            CompliantDeviceSignIns = countif(IsCompliant == 1),
            ManagedDevices = dcountif(EntraIdDeviceId, IsManaged == 1),
            HighRiskEvents = countif(RiskLevelAggregated == 100)
            by Application
| where TotalSignIns >= 50
| extend MfaPct = round(todouble(MfaSignIns) * 100.0 / todouble(TotalSignIns), 2),
         CompliantDevicePct = round(todouble(CompliantDeviceSignIns) * 100.0 / todouble(TotalSignIns), 2)
| order by TotalSignIns desc
```

#### Consulta 4: Control Financiero (FinOps) del Beneficio Microsoft 365 E5 Data Grant en Sentinel
- **Plataforma / Tabla Principal:** Microsoft Sentinel / Log Analytics (`Usage`) `[Verificado MS Learn]`.
- **Propósito:** Cuantificar los GB diarios absorbidos por tablas elegibles al beneficio gratuito de hasta 5 MB/usuario/día de M365 E5/E7/*Defender Suite* frente al consumo facturable neto.
```kql
// Clasifica el consumo facturable de 30 días entre tablas cubiertas por M365 E5 Data Grant y resto del SIEM
let E5EligibleTables = dynamic([
    "SigninLogs", "AuditLogs", "AADNonInteractiveUserSignInLogs", "AADServicePrincipalSignInLogs",
    "AADManagedIdentitySignInLogs", "AADProvisioningLogs", "ADFSSignInLogs",
    "DeviceEvents", "DeviceFileEvents", "DeviceImageLoadEvents", "DeviceInfo", "DeviceLogonEvents",
    "DeviceNetworkEvents", "DeviceNetworkInfo", "DeviceProcessEvents", "DeviceRegistryEvents",
    "EmailAttachmentInfo", "EmailEvents", "EmailPostDeliveryEvents", "EmailUrlInfo",
    "UrlClickEvents", "CloudAppEvents", "IdentityInfo", "IdentityLogonEvents",
    "IdentityQueryEvents", "IdentityDirectoryEvents", "AlertEvidence", "McasShadowItReporting"
]);
Usage
| where TimeGenerated > ago(30d)
| where IsBillable == true
| extend BillingCategory = iff(DataType in (E5EligibleTables), "Elegible M365 E5 Data Grant", "Facturable Neto Azure / Terceros")
| summarize TotalGB_30d = round(sum(Quantity) / 1024.0, 2),
            AvgDailyGB = round(sum(Quantity) / 1024.0 / 30.0, 2)
            by BillingCategory, DataType
| order by TotalGB_30d desc
```

#### Consulta 5: Identificación de Activos Críticos (Crown Jewels) con Rutas de Ataque Entrantes en MSEM
- **Plataforma / Tabla Principal:** Microsoft Defender XDR Advanced Hunting (`ExposureGraphNodes` + `ExposureGraphEdges`) `[Verificado MS Learn]`.
- **Propósito:** Priorizar remediaciones preventivas consultando directamente el grafo de **Microsoft Security Exposure Management**.
```kql
// Cruza nodos de alta criticidad con aristas de exposición entrantes para detectar cuellos de botella de riesgo
ExposureGraphNodes
| where NodeLabel in ("device", "user", "serviceprincipal", "virtualmachine")
| extend CriticalityLevel = toint(parse_json(NodeProperties).rawData.criticalityLevel.criticalityLevel)
| where CriticalityLevel <= 2 or tostring(NodeProperties) has_any ("CrownJewel", "CriticalAsset", "Tier0")
| join kind=inner (
    ExposureGraphEdges
    | project SourceNodeId, TargetNodeId, EdgeLabel
) on $left.NodeId == $right.TargetNodeId
| summarize InboundVectors = count(),
            DistinctSources = dcount(SourceNodeId),
            RelationshipTypes = make_set(EdgeLabel, 10)
            by NodeName, NodeLabel, CriticalityLevel
| order by InboundVectors desc
```

#### Consulta 6: Auditoría Unificada de Cambios Administrativos en Políticas Zero Trust (Entra + Purview)
- **Plataforma / Tabla Principal:** Microsoft Sentinel (`AuditLogs` + `OfficeActivity`) `[Verificado MS Learn]`.
- **Propósito:** Detectar modificaciones en políticas críticas de identidad y protección de datos para control de cambios y auditoría `GV.PO-02`.
```kql
// Unifica trazas de auditoría de cambios en Conditional Access / Auth Methods y políticas Purview DLP/Retención
let IdentityPolicyAudit = AuditLogs
| where TimeGenerated > ago(7d)
| where Category == "Policy" and OperationName has_any ("Conditional Access", "authentication method", "Authentication Strength")
| project TimeGenerated, Domain = "Entra ID", OperationName, Initiator = tostring(InitiatedBy.user.userPrincipalName), TargetPolicy = tostring(TargetResources[0].displayName), Result;
let DataPolicyAudit = OfficeActivity
| where TimeGenerated > ago(7d)
| where Operation has_any ("New-DlpCompliancePolicy", "Set-DlpCompliancePolicy", "Remove-DlpCompliancePolicy", "Set-DlpComplianceRule", "New-RetentionCompliancePolicy", "Set-RetentionCompliancePolicy")
| project TimeGenerated, Domain = "Microsoft Purview", OperationName = Operation, Initiator = UserId, TargetPolicy = OfficeObjectId, Result = ResultStatus;
union IdentityPolicyAudit, DataPolicyAudit
| order by TimeGenerated desc
```

#### Consulta 7: Auditoría Programática de Agentes IA en Riesgo vía Microsoft Graph PowerShell (`riskyAgents`)
- **Plataforma / Tabla Principal:** Microsoft Graph API (`identityProtection/riskyAgents` y `agentRiskDetections`) `[Verificado MS Learn]`.
- **Propósito:** Extraer evidencia auditable del estado de riesgo de agentes autónomos registrados en **Entra Agent ID** / **Microsoft Agent 365**.
```powershell
# Conecta con mínimo privilegio de lectura de riesgo sobre identidades de agentes
Connect-MgGraph -Scopes "IdentityRiskyAgent.Read.All", "IdentityRiskEvent.Read.All" -NoWelcome

# Obtiene agentes actualmente en riesgo y sus últimas detecciones asociadas
$riskyAgentsUri = "https://graph.microsoft.com/beta/identityProtection/riskyAgents?`$filter=riskState eq 'atRisk'"
$agents = (Invoke-MgGraphRequest -Method GET -Uri $riskyAgentsUri).value

$detectionsUri = "https://graph.microsoft.com/beta/identityProtection/agentRiskDetections?`$top=50"
$detections = (Invoke-MgGraphRequest -Method GET -Uri $detectionsUri).value

$agents | Select-Object id, agentDisplayName, riskLevel, riskState, riskLastUpdatedDateTime | Format-Table -AutoSize
$detections | Select-Object detectedDateTime, agentDisplayName, riskEventType, riskLevel, riskState | Format-Table -AutoSize
```

### 10.2 Matriz de Verificación Operativa ("Proof of Life") de los Cinco Planos

| Plano Arquitectónico | Módulos Asociados | Prueba Objetiva de Operación Efectiva ("Proof of Life") | Ruta de Verificación Directa | Etiqueta |
|---|---|---|---|---|
| **1. Identidad, Acceso y Red** | `01`, `02`, `22` | Directiva unificada `Authentication methods` en `Migration Complete`; >=2 cuentas Break-Glass cloud-only con FIDO2/CBA probadas <=90 días; Conditional Access aplicando *Phishing-resistant MFA* a admins; >98% elevaciones vía PIM; inventario activo en `Entra Agent ID`. | `entra.microsoft.com` > `Authentication methods` / `Conditional Access` / `PIM` / `Agent ID` | `[Verificado MS Learn]` |
| **2. Unified SecOps & SIEM** | `03`–`08` | Workspace primario incorporado en `security.microsoft.com`, **Sentinel Data Lake** habilitado, **Automatic Attack Disruption** activo, tablas `EntraIdSignInEvents` y XDR fluyendo sin errores en `SentinelHealth` y **MSEM** calculando *Attack Paths*. | `security.microsoft.com` > `Incidents` / `Exposure management` / `Microsoft Sentinel` | `[Verificado MS Learn]` |
| **3. IA para SOC (Agéntica)** | `09`, `22` | Capacidad SCU activa y monitoreada, agentes aprobados operando bajo modo definido (*Human-ON-the-Loop*) y registro unificado en **Microsoft Agent 365** con *Sponsors* asignados. | `security.microsoft.com` / `securitycopilot.microsoft.com` / `admin.microsoft.com > Agents` | `[Verificado MS Learn]` |
| **4. Endpoints y Plataforma** | `10`, `11`, `12` | Flota inscrita en Intune evaluando cumplimiento en tiempo real, sensores MDE activos, cifrado BitLocker + claves Windows LAPS rotadas y elevación local gobernada por **Intune EPM**. | `intune.microsoft.com` > `Devices` / `Endpoint security` | `[Verificado MS Learn]` |
| **5. Datos, Riesgo y GRC** | `13`–`21` | Etiquetas de sensibilidad con cifrado desplegadas, DLP + **Insider Risk Adaptive Protection** activos, **Purview Audit (Premium)** reteniendo >=1 año, **Customer Lockbox** activo y evaluación NIST CSF 2.0 viva en **Compliance Manager**. | `purview.microsoft.com` > `Compliance Manager` / `DLP` / `Audit` | `[Verificado MS Learn]` |

---

## 11. Indicadores Clave de Desempeño (KPIs) y Modelo de Madurez Operacional

### 11.1 Tabla Maestra de 8 KPIs Diferenciados en Tres Altitudes

| ID | Indicador Clave (KPI) | Fórmula de Cálculo Auditable | Meta Objetivo | Frecuencia | Audiencia (Altitud) | Etiqueta |
|---|---|---|---|---|---|---|
| **KPI-01** | **Velocidad de Reconocimiento y Contención Crítica (MTTA / MTTC P1)** | `Mediana(FirstModifiedTime - CreatedTime)` y `Mediana(ContainmentTime - CreatedTime)` en incidentes `Critical/High` verdaderos positivos | `MTTA <= 15 min` · `MTTC <= 60 min` | Diaria / Semanal | Altitud 3: SOC Manager y SecOps | `[Decisión / Propuesta Editorial]` |
| **KPI-02** | **Adopción de Autenticación Resistente a Phishing** | `(Usuarios activos autenticando con Passkeys FIDO2, WHfB o CBA / Total de usuarios activos en alcance) * 100` | `100%` Admins · `>= 85%` Usuarios Generales | Mensual | Altitud 2: CISO, IAM Lead y CIO | `[Decisión / Propuesta Editorial]` |
| **KPI-03** | **Mitigación de Rutas de Ataque Críticas y Postura (MSEM)** | `(Rutas críticas hacia Crown Jewels cerradas en SLA / Total rutas críticas detectadas) * 100` y `Microsoft Secure Score` | `>= 90%` rutas mitigadas · `Secure Score >= 85%` | Semanal / Mensual | Altitud 2: CISO, Arquitectos y CTO | `[Decisión / Propuesta Editorial]` |
| **KPI-04** | **Tasa de Automatización Tier-1 y Precisión de Agentes IA** | `(Incidentes Tier-1 enriquecidos/resueltos automáticamente / Total Tier-1) * 100` y `% decisiones válidas en muestreo de agentes IA` | `60% – 70%` automatización Tier-1 · `>= 95%` precisión IA | Semanal / Mensual | Altitud 3 y 2: SOC Manager y CISO | `[Decisión / Propuesta Editorial]` |
| **KPI-05** | **Índice de Cero Privilegio Permanente (Zero Standing Privilege)** | `(Sesiones administrativas elevadas vía PIM JIT / Total de sesiones con rol administrativo en el tenant) * 100` | `>= 98%` vía PIM JIT (`< 5` Global Admins elegibles) | Mensual | Altitud 2: CISO, IAM Lead y Auditoría | `[Decisión / Propuesta Editorial]` |
| **KPI-06** | **Precisión y Cumplimiento de Resultados del MSSP (Outcome SLA)** | `(Escalamientos verdaderos positivos con contexto completo dentro de SLA / Total de escalamientos del MSSP) * 100` | `>= 90%` precisión de escalamiento · `>= 95%` SLA P1 | Mensual | Altitud 2: CISO, Compras y SOC Manager | `[Decisión / Propuesta Editorial]` |
| **KPI-07** | **Índice de Sostenibilidad Operativa y Retención del Talento** | `((Capacidad Horas Analista - Carga Esperada) / Capacidad Horas Analista) * 100` y `Retención anual del equipo interno` | Holgura `>= 15%` · Retención anual `>= 88%` | Mensual / Trimestral | Altitud 2 y 1: CISO, RRHH y C-Suite | `[Decisión / Propuesta Editorial]` |
| **KPI-08** | **Alineación al Apetito de Riesgo (FAIR) y Madurez NIST CSF 2.0** | `% escenarios top dentro del umbral financiero ALE aprobado por el Board` y `% subcategorías NIST CSF 2.0 en Tier >= 3` | `100%` dentro de tolerancia · `>= 85%` en `Tier 3+` | Trimestral / Anual | Altitud 1: Board of Directors, CEO y CFO | `[Decisión / Propuesta Editorial]` |

### 11.2 Modelo de Madurez Operacional de Cinco Niveles

| Nivel | Equivalencia Normativa | Gobernanza CISO y Gestión de Riesgo | Plataforma Microsoft, Automatización e IA | Talento Humano y Modelo Híbrido MSSP | Etiqueta |
|---|---|---|---|---|---|
| **Nivel 1 — Inicial / Reactivo** | NIST Tier 1 · CMMI 1 · C2M2 MIL0–1 | Sin comité directivo ni apetito de riesgo; ciberseguridad confinada a soporte TI; licencias E5 fragmentadas sin adopción real. | Consolas aisladas; Sentinel aún en Azure Portal sin XDR unificado; MFA débil (SMS/Voz); respuesta manual improvisada. | Sobrecarga crónica (*alert fatigue*), rotación >30% o MSSP sin supervisión operando con SLAs de volumen de tickets. | `[Decisión / Propuesta Editorial]` |
| **Nivel 2 — Gestionado** | NIST Tier 2 · CMMI 2 · C2M2 MIL1–2 | Políticas fundacionales aprobadas; inventario inicial de activos; reportes técnicos mensuales sin cuantificación financiera. | Cola unificada en `security.microsoft.com`; Conditional Access básico; 5–8 playbooks iniciales en Logic Apps; DLP en modo auditoría. | Roles L1/L2 documentados; SLAs básicos con MSSP pero con fricción en escalamientos y brechas de contexto de negocio. | `[Decisión / Propuesta Editorial]` |
| **Nivel 3 — Definido y Repetible** *(Objetivo Base)* | NIST Tier 3 · CMMI 3 · C2M2 MIL2 (MIL3 en IAM/IR) | Comité trimestral activo; apetito de riesgo aprobado; evaluación anual SFI/NIST CSF 2.0; supervisión TPRM rigurosa sobre el MSSP. | **Unified SecOps Platform** completa con Sentinel Data Lake, PIM JIT universal, Passkeys FIDO2 en admins, Purview MIP/DLP activo y 60%+ auto-triaje. | Modelo co-gestionado maduro con SLAs de *outcome*; rotación de tareas, *blameless post-mortems* y certificaciones SC-200/300/401/100. | `[Decisión / Propuesta Editorial]` |
| **Nivel 4 — Cuantitativo y Predictivo** | NIST Tier 3+ · CMMI 4 · C2M2 MIL3 | Cuantificación **Open FAIR** integrada al ERM corporativo; reportes en tres altitudes; inversiones decididas por reducción marginal de ALE. | **Exposure Management** cerrando *Chokepoints* hacia *Crown Jewels*, **Token Protection**, **CAE** estricto, *Adaptive Protection* y *Purple Team* trimestral. | Control estadístico de métricas SOC; holgura de capacidad >=15% sostenida; *Threat Hunters* internos retroalimentando arquitectura. | `[Decisión / Propuesta Editorial]` |
| **Nivel 5 — Adaptativo y Agéntico** | NIST Tier 4 · CMMI 5 · C2M2 MIL3 sostenido | Ciberresiliencia y confianza digital integradas al negocio y M&A; gobernanza completa de ética/regulación IA y preparación criptográfica post-cuántica (PQC). | Orquestación *Human-IN / ON / OUT-of-the-Loop* con **Security Copilot**, MCP y **Microsoft Agent 365** (`M365 E7`); postura como código continua. | Cultura Kaizen autónoma; analistas evolucionados a directores de agentes IA e ingenieros de resiliencia; retención >90%. | `[Decisión / Propuesta Editorial]` |

---

## 12. Mapeo de Auditoría a NIST CSF 2.0 y MITRE ATT&CK

Esta tabla consolida 12 subcategorías auditables representativas de las **6 funciones de NIST CSF 2.0 (CSWP 29)** como guía maestra de evidencia para auditores internos, externos y reguladores `[Decisión / Propuesta Editorial]`:

| Función NIST CSF 2.0 | Subcategoría (CSWP 29) | Descripción Oficial del Resultado | Capacidades Habilitadoras Transversales (`00`–`22`) | Evidencia Auditable Reproducible | Etiqueta |
|---|---|---|---|---|---|
| **GOVERN (GV)** | `GV.OC-03` | Los requisitos legales, regulatorios y contractuales en materia de ciberseguridad y privacidad se comprenden y gestionan. | **Purview Compliance Manager** (`13`), retención regulatoria **Purview DLM** (`16`) y matriz legal de la Oficina del CISO (`00`). | Exportación fechada de evaluaciones regulatorias activas en *Compliance Manager* con controles técnicos vinculados y propietarios internos. | `[Decisión / Propuesta Editorial]` |
| **GOVERN (GV)** | `GV.RM-02` | Las declaraciones de apetito y tolerancia al riesgo se establecen, comunican y mantienen. | Metodología **Open FAIR** materializada técnicamente en umbrales de bloqueo de **Entra ID Protection** (`01`), **MSEM** (`03`) y **Adaptive Protection** (`17`). | Acta anual del Board aprobando el Apetito de Riesgo + configuración exportada de políticas automáticas alineadas a dichos umbrales. | `[Decisión / Propuesta Editorial]` |
| **GOVERN (GV)** | `GV.RR-02` | Los roles, responsabilidades y autoridades de ciberseguridad se establecen, comunican, aplican y revisan. | **Entra RBAC**, **PIM** (`01`, `02`), **Defender Unified RBAC** (`03`), **Purview Role Groups** (`13`) y patrocinio en **Agent 365** (`22`). | Reporte de asignaciones `Eligible` vs. `Active` en PIM, matriz RACI firmada y contrato MSSP con separación explícita de funciones. | `[Decisión / Propuesta Editorial]` |
| **GOVERN (GV)** | `GV.SC-07` | Los riesgos derivados de proveedores, sus productos y servicios se comprenden, priorizan y monitorean a lo largo de la relación. | **Sentinel Workbooks** sobre desempeño MSSP (`08`), **Azure Lighthouse**, **MDCA OAuth Governance** (`07`) y **Customer Lockbox** (`21`). | Scorecard mensual recalculado en KQL sobre SLAs del MSSP, inventario de apps OAuth de terceros y bitácora *Customer Lockbox*. | `[Decisión / Propuesta Editorial]` |
| **IDENTIFY (ID)** | `ID.AM-05` | Los activos se priorizan según clasificación, criticidad, recursos y valor de impacto para la misión. | *Critical Asset Management* en **Exposure Management** (`03`), taxonomía **Purview MIP** (`14`) e inventario unificado **Agent 365** (`22`). | Catálogo exportado de *Crown Jewels* en MSEM cruzado con BIA corporativo y reporte de distribución de etiquetas confidenciales. | `[Decisión / Propuesta Editorial]` |
| **IDENTIFY (ID)** | `ID.RA-05` | Amenazas, vulnerabilidades, probabilidades e impactos se integran para comprender el riesgo y guiar la priorización. | **MSEM Attack Paths & Chokepoints** (`03`), **Defender Vulnerability Management** (`04`) y **Threat Analytics** *(MITRE Initial Access / Lateral Movement)*. | Informe semanal de rutas de ataque críticas remediadas y cola de vulnerabilidades priorizada por explotabilidad KEV/EPSS e impacto. | `[Decisión / Propuesta Editorial]` |
| **IDENTIFY (ID)** | `ID.IM-02` | Se identifican mejoras a partir de pruebas de seguridad, ejercicios y revisiones operativas. | **Sentinel SOC Optimization** (`08`), ejercicios *Purple Team* (`T-02`), simulacros ejecutivos (`SM-01`) y autoevaluación anual SFI (`A-01`). | Historial auditable de mejoras aplicadas en *SOC Optimization*, informes *Purple Team* y seguimiento cerrado de acciones post-incidente. | `[Decisión / Propuesta Editorial]` |
| **PROTECT (PR)** | `PR.AA-05` | Los permisos, derechos y autorizaciones se definen, gestionan, aplican y revisan bajo mínimo privilegio y segregación. | **Conditional Access** (`Authentication Strengths`, `Token Protection`, `CAE`), **PIM JIT** (`01`, `02`), **Intune EPM** (`11`) y **CA for agents** (`22`) *(MITRE Valid Accounts)*. | Exportación JSON/Maester de políticas CA, reportes CSV de *Access Reviews* con revocación automática y trazas de activación JIT. | `[Decisión / Propuesta Editorial]` |
| **PROTECT (PR)** | `PR.DS-01` | Se protegen la confidencialidad, integridad y disponibilidad de los datos en reposo. | Cifrado **Purview Information Protection** (`14`), **BitLocker** (`12`), **Customer Key** (`21`) y retención inmutable **Preservation Lock** (`16`). | Dashboard de cumplimiento de cifrado en Intune, métricas de archivos protegidos con MIP y políticas inmutables verificadas. | `[Decisión / Propuesta Editorial]` |
| **DETECT (DE)** | `DE.AE-02` | Los eventos potencialmente adversos se analizan para comprender las actividades asociadas y detectar incidentes. | Correlación XDR (`03`), reglas KQL/ASIM/UEBA en **Sentinel** (`08`), tabla `EntraIdSignInEvents` y **Security Copilot** (`09`) *(MITRE todas las tácticas)*. | Expedientes unificados de incidentes con *Attack Story*, mapeo MITRE ATT&CK v18 y auditoría de consultas en `LAQueryLogs`. | `[Decisión / Propuesta Editorial]` |
| **RESPOND (RS)** | `RS.MI-01` | Los incidentes de ciberseguridad son contenidos oportunamente para impedir la expansión del daño. | **Automatic Attack Disruption** (`03`), playbooks **Logic Apps** con Managed Identity (`08`), suspensión en **Entra ID / Agent ID** (`01`, `22`) y aislamiento MDE (`04`). | Historial del `Action center` y `SecurityIncident` evidenciando tiempos reales de contención (`MTTC <= 60 min` en críticos) *(MITRE Impact / Exfiltration)*. | `[Decisión / Propuesta Editorial]` |
| **RECOVER (RC)** | `RC.RP-05` | Se verifica la integridad de los activos restaurados, se restablecen servicios y se confirma la vuelta a la normalidad. | Liberación controlada en **Action Center** (`03`), reprovisionamiento **Windows Autopilot / Intune** (`10`), prueba Break-Glass y rotación de secretos (`01`). | Listas de verificación firmadas previas a reconexión productiva, registros de des-aislamiento y acta formal de cierre de recuperación. | `[Decisión / Propuesta Editorial]` |

---

## 13. Habilitación y Ruta de Formación por Rol

| Rol en el Ecosistema | Recursos Oficiales Microsoft Learn y SAF | Ninja Trainings y Comunidad Experta (2026) | Certificaciones Vigentes Recomendadas | Cadencia de Acreditación | Etiqueta |
|---|---|---|---|---|---|
| **CISO y Líderes de Oficina del CISO** | **Microsoft Security Adoption Framework (SAF)**, **The CISO Workshop**, **Integrate NIST CSF 2.0 governance (SFI)** | *Microsoft Digital Defense Report*, *Entra.News* (Merill Fernando), foros CISO de Microsoft | **SC-900**, **CISSP**, **CISM**, **CRISC**, **Open FAIR** | Taller SAF/CISO en primeros 60 días; actualización ejecutiva semestral. | `[Verificado MS Learn]` / `[Decisión / Propuesta Editorial]` |
| **Enterprise & Cloud Security Architects** | **MCRA (Junio 2026)**, **Zero Trust Architecture**, rutas oficiales de diseño **SC-100** y **Exposure Management** | *Microsoft Security Exposure Management Ninja Training*, publicaciones de Mark Simos y Thomas Naunheim | **SC-100: Microsoft Cybersecurity Architect Expert**, **SABSA SCF** | Certificación anual renovada en Learn + revisión de cada release de MCRA. | `[Verificado MS Learn]` / `[Decisión / Propuesta Editorial]` |
| **SOC Manager, Analistas L1–L3 y Threat Hunters** | **Defender XDR SecOps Guide**, **Microsoft Sentinel Operational Guide**, **Advanced Hunting KQL** | *Defender XDR Ninja Training*, *Microsoft Sentinel Ninja Training*, *Security Copilot Ninja Training*, blog de Jeffrey Appel | **SC-200: Microsoft Security Operations Analyst Associate** | `SC-200` en primeros 90–120 días; 20% de horas semanales reservadas a laboratorio Kaizen. | `[Verificado MS Learn]` / `[Decisión / Propuesta Editorial]` |
| **Identity, Access & Agent Governance Leads** | **Microsoft Entra SecOps Guide**, **Authentication Methods & Passkeys**, **Entra Agent ID & Agent 365** | *Microsoft Entra Identity & Agents Ninja Training 2026*, *Maester.dev*, blogs de Merill Fernando y Jan Bakker | **SC-300: Microsoft Identity and Access Administrator Associate** | `SC-300` vigente + ejercicios trimestrales de políticas como código y Break-Glass. | `[Verificado MS Learn]` / `[Decisión / Propuesta Editorial]` |
| **Data Security, Purview & GRC Specialists** | Rutas **Microsoft Purview (MIP, DLP, IRM, Audit, eDiscovery, Compliance Manager, DSPM for AI)** | *Microsoft Purview Ninja Trainings*, guías oficiales **NIST CSWP 29** y **NIST SP 1303** | **SC-401: Administering Information Security in Microsoft 365**, **CISA / CRISC** | `SC-401` activa (reemplazo oficial de SC-400) y simulacro semestral de auditoría/eDiscovery. | `[Verificado MS Learn]` / `[Decisión / Propuesta Editorial]` |

---

## 14. Registro de Revalidación Técnica (Noviembre 2026) y Decisiones Editoriales

### 14.1 Correcciones y Actualizaciones Verificadas contra Microsoft Learn MCP al `2026-11-11`

| # | Área Técnica / Normativa | Estado en Borradores Locales Previos (`MSEOP-MD`) | Corrección Verificada a Noviembre de 2026 Aplicada en esta Guía | Etiqueta |
|---|---|---|---|---|
| **1** | **Estructura exacta de NIST CSF 2.0 (CSWP 29)** | El documento previo `Mapeado NIST x 23` contabilizaba **23 categorías**, manteniendo una categoría inexistente `RC.IM` en *Recover*. | Verificado contra **NIST CSWP 29**: existen exactamente **6 funciones, 22 categorías y 106 subcategorías**. La mejora continua se unificó íntegramente en **`ID.IM`**, quedando `RECOVER` con `RC.RP` y `RC.CO`. | `[Verificado MS Learn]` |
| **2** | **Renombre oficial de suites E5 Security y E5 Compliance** | Se citaban exclusivamente los nombres históricos *Microsoft 365 E5 Security* y *Microsoft 365 E5 Compliance*. | Incorporado el renombre oficial vigente en las guías de licenciamiento de Microsoft: **Microsoft Defender Suite** (antes *M365 E5 Security*) y **Microsoft Purview Suite** (antes *M365 E5 Compliance*, confirmando que no incluye Entra ID P2). | `[Verificado MS Learn]` |
| **3** | **Disponibilidad general de Microsoft Agent 365 y M365 E7** | Los documentos de enero de 2026 trataban los agentes autónomos como proyección futura hacia 2027 sin paquete comercial unificado. | Incorporados **Microsoft Agent 365** y **Microsoft 365 E7: The Frontier Suite** (disponible desde el **1 de mayo de 2026**, combinando M365 E5 + M365 Copilot + Entra Suite + Agent 365) y su integración con **Entra Agent ID**. | `[Verificado MS Learn]` |
| **4** | **Lanzamiento del sitio Microsoft SAF y MCRA Junio 2026** | Referencias previas apuntaban a recursos antiguos de CAF/MCRA 2023–2024 y 65–78 billones de señales diarias. | Actualizado al portal oficial **Microsoft Security Adoption Framework (SAF)** (`learn.microsoft.com/en-us/security/adoption/adoption`), **MCRA Junio 2026**, **100+ billones de señales diarias** y el patrón SFI `integrate-nist-2-governance`. | `[Verificado MS Learn]` |
| **5** | **Retiro de Sentinel en Azure Portal y Data Lake Integrado** | Se asumía coexistencia indefinida entre Azure Portal y Defender Portal para operaciones diarias de SIEM. | Documentado el retiro definitivo de soporte de Sentinel en Azure Portal después del **31 de marzo de 2027** y el **Sentinel Data Lake** integrado por defecto en el onboarding desde el **23 de septiembre de 2026**. | `[Verificado MS Learn]` |
| **6** | **Reemplazo de `AADSignInEventsBeta` por `EntraIdSignInEvents`** | Consultas de caza avanzada en XDR empleaban la tabla en vista previa `AADSignInEventsBeta` y la columna `AadDeviceId`. | Verificado que el **19 de octubre de 2026** `AADSignInEventsBeta` quedó en desuso y migró automáticamente a **`EntraIdSignInEvents`** (y `EntraIdDeviceId`). Todas las consultas fueron actualizadas. | `[Verificado MS Learn]` |
| **7** | **Posicionamiento de Microsoft Security Exposure Management** | El seguimiento de postura se apoyaba casi únicamente en *Microsoft Secure Score*. | Alineado a MCRA 2025/2026 ubicando a **Exposure Management (MSEM)** (*Attack Paths*, *Chokepoints*, *Critical Assets* e *Initiatives*) como motor primario CTEM, manteniendo *Secure Score* como indicador complementario de higiene. | `[Verificado MS Learn]` |
| **8** | **Renovación del portafolio de certificaciones de datos** | Se citaba la certificación retirada `SC-400` para especialistas de información. | Actualizada la matriz formativa a **`SC-401: Administering Information Security in Microsoft 365`**, alineada a seguridad de datos y Purview para IA. | `[Verificado MS Learn]` |

### 14.2 Decisiones y Propuestas Editoriales Adoptadas

| Decisión Editorial | Clasificación | Justificación Ejecutiva y Arquitectónica |
|---|---|---|
| **Inalienabilidad de la función GOVERN (100% Interna) y Modelo de Tres Zonas** | `Propuesta Editorial` | Resuelve el riesgo fiduciario y de conflicto de interés cuando una organización delega erróneamente la definición de políticas, apetito de riesgo o supervisión en el mismo MSSP que ejecuta la operación. |
| **Gobierno Humano-IA en Tres Modos (Human-IN / ON / OUT-of-the-Loop)** | `Propuesta Editorial` | Proporciona un marco auditable y defendible ante directorios y reguladores para aprovechar la velocidad de **Automatic Attack Disruption** y los agentes de **Security Copilot / Agent 365** sin perder control ni trazabilidad humana. |
| **Arquitectura de Métricas en Tres Altitudes y Umbrales Numéricos de KPIs** | `Propuesta Editorial` | Evita las métricas de vanidad traduciendo telemetría técnica al idioma específico del SOC, del C-Suite y del Board; valores como `MTTA <= 15 min`, `MTTC <= 60 min`, `>= 85% Secure Score` y `>= 98% PIM JIT` representan estándares consultivos de alta madurez. |
| **Compromiso Kaizen de Capacidad (Holgura >= 15% y 20% Upskilling)** | `Propuesta Editorial` | Convierte la prevención del agotamiento humano del Manifiesto de Excelencia Operacional en un indicador auditable de resiliencia operativa. |
| **Mapeo Maestro de los 23 Módulos a las 22 Categorías de NIST CSF 2.0** | `Propuesta Editorial` | Establece una arquitectura común sin solapamientos entre los 23 documentos del repositorio, declarando con transparencia qué resultados se logran en consola y cuáles exigen gobierno legal, físico o corporativo complementario. |

---

## 15. Directorio de Referencias Públicas Verificadas

### Documentación Oficial Microsoft Learn y Licenciamiento
- **REF-01:** *Microsoft Security Adoption Framework (SAF)* — Microsoft Learn (`https://learn.microsoft.com/en-us/security/adoption/adoption`). Modelo operativo oficial para conectar prioridades de negocio, riesgo y Zero Trust con implementación y operación sostenible `[Verificado MS Learn]`.
- **REF-02:** *Integrate NIST CSF 2.0 governance into annual cybersecurity assessments (Secure Future Initiative)* — Microsoft Learn (`https://learn.microsoft.com/en-us/security/zero-trust/sfi/integrate-nist-2-governance`). Patrón oficial SFI para evaluaciones anuales estructuradas sobre las 6 funciones de NIST CSF 2.0 `[Verificado MS Learn]`.
- **REF-03:** *Microsoft Cybersecurity Reference Architectures (MCRA)* — Microsoft Learn (`https://learn.microsoft.com/en-us/security/adoption/mcra`). Arquitectura técnica maestra de capacidades e integraciones de seguridad Microsoft (edición junio de 2026) `[Verificado MS Learn]`.
- **REF-04:** *The Chief Information Security Officer (CISO) Workshop* — Microsoft Learn (`https://learn.microsoft.com/en-us/security/zero-trust/workshop-business-security-leaders`). Guía estructurada de estrategia ejecutiva, modernización del SOC y adopción Zero Trust `[Verificado MS Learn]`.
- **REF-05:** *Microsoft Sentinel in the Microsoft Defender portal* — Microsoft Learn (`https://learn.microsoft.com/en-us/azure/sentinel/microsoft-sentinel-defender-portal`). Operación unificada SIEM+XDR y fecha oficial de retiro en Azure Portal (`2027-03-31`) `[Verificado MS Learn]`.
- **REF-06:** *Automatic attack disruption in Microsoft Defender XDR* — Microsoft Learn (`https://learn.microsoft.com/en-us/defender-xdr/automatic-attack-disruption`). Contención automática basada en IA con confianza >=99% SNR sobre Entra ID, AD, MDE, MDA, Okta y AWS `[Verificado MS Learn]`.
- **REF-07:** *What is Microsoft Security Exposure Management?* — Microsoft Learn (`https://learn.microsoft.com/en-us/security-exposure-management/overview`). Gestión continua de exposición a amenazas (CTEM), activos críticos, *chokepoints* y rutas de ataque `[Verificado MS Learn]`.
- **REF-08:** *What is Microsoft Entra Agent ID? & Protect agent identities with Microsoft Entra (Agent 365)* — Microsoft Learn (`https://learn.microsoft.com/en-us/entra/agent-id/what-is-microsoft-entra-agent-id` y `https://learn.microsoft.com/en-us/microsoft-agent-365/admin/capabilities-entra`). Marco de identidad, acceso condicional, protección de riesgo y ciclo de vida para agentes de IA `[Verificado MS Learn]`.
- **REF-09:** *Subscription Suites Licensing Guidance (Microsoft 365 E5, E7, Microsoft Defender Suite & Microsoft Purview Suite)* — Microsoft Licensing (`https://www.microsoft.com/licensing/guidance/subscription-suites`). Referencia contractual de suites empresariales y renombres vigentes en 2026 `[Verificado MS Learn]`.
- **REF-10:** *AADSignInEventsBeta (deprecated) & EntraIdSignInEvents in Defender XDR Advanced Hunting* — Microsoft Learn (`https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-aadsignineventsbeta-table`). Documentación oficial de migración de tabla de eventos de inicio de sesión el `2026-10-19` `[Verificado MS Learn]`.

### Blogs Oficiales y Líderes de Producto / Arquitectura en Microsoft
- **REF-11:** Vasu Jakkal (Corporate Vice President, Microsoft Security) — *Secure agentic AI for your Frontier Transformation*, Microsoft Security Blog, 9 de marzo de 2026 (`https://www.microsoft.com/en-us/security/blog/2026/03/09/secure-agentic-ai-for-your-frontier-transformation/`). Anuncio oficial de **Microsoft Agent 365** y **Microsoft 365 E7: The Frontier Suite** `[Verificado MS Learn]`.
- **REF-12:** Mark Simos (Principal Lead Cybersecurity Architect, Microsoft) — *Microsoft Security Adoption Framework (SAF) & MCRA Releases* (`https://aka.ms/SAF` y `https://aka.ms/MCRA`). Liderazgo arquitectónico sobre SAF, MCRA, CISO Workshop y alineación con The Open Group `[Verificado MS Learn]`.
- **REF-13:** Alex Simons (Corporate Vice President, Microsoft Identity & Network Access) — *Announcing Microsoft Entra Agent ID: Secure and manage your AI agents*, Microsoft Entra Blog (`https://techcommunity.microsoft.com/blog/microsoft-entra-blog/announcing-microsoft-entra-agent-id-secure-and-manage-your-ai-agents/3827392`). Fundamentos de gobierno de identidades de agentes en Microsoft Entra `[Verificado MS Learn]`.
- **REF-14:** Merill Fernando (Principal Product Manager, Microsoft Entra) — *Entra.News & Maester PowerShell Security Testing Framework* (`https://entra.news` y `https://maester.dev`). Síntesis semanal de cambios en Microsoft Entra, licenciamiento E7 y validación continua de controles como código `[Verificado MS Learn]`.

### Comunidad MVP de Seguridad Microsoft
- **REF-15:** Jeffrey Appel (Microsoft Security MVP) — *Defender Monthly News & Integrating Microsoft Defender/Sentinel Data Lake with Microsoft Fabric* (`https://jeffreyappel.nl`). Cobertura técnica profunda sobre Unified SecOps, Data Lake integrado (sep-2026) y detección avanzada `[Verificado MS Learn]`.
- **REF-16:** Jan Bakker (Microsoft Security & Entra MVP) — *JanBakker.tech — Microsoft Entra, Conditional Access & Passkeys* (`https://janbakker.tech`). Guías operativas verificadas sobre endurecimiento de registro de Passkeys, Conditional Access y Global Secure Access `[Verificado MS Learn]`.

### Marcos Normativos e Industria
- **REF-17:** National Institute of Standards and Technology (NIST) — *The NIST Cybersecurity Framework (CSF) 2.0 (NIST CSWP 29)*, 26 de febrero de 2024 (`https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf`). Estándar normativo oficial de las 6 funciones, 22 categorías y 106 subcategorías `[Verificado MS Learn]`.
- **REF-18:** National Institute of Standards and Technology (NIST) — *NIST CSF 2.0: Enterprise Risk Management (ERM) Quick-Start Guide (NIST SP 1303)* (`https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.1303.pdf`). Integración formal de ciberseguridad con riesgos empresariales `[Verificado MS Learn]`.
- **REF-19:** U.S. Department of Energy (DOE) — *Cybersecurity Capability Maturity Model (C2M2) v2.1* (`https://www.energy.gov/ceser/cybersecurity-capability-maturity-model-c2m2`). Modelo táctico de evaluación de madurez por niveles MIL0–MIL3 `[Verificado MS Learn]`.
- **REF-20:** The Open Group — *Open FAIR Risk Analysis & SABSA / O-ISM3 Architecture Standards* (`https://www.opengroup.org/certifications/openfair`) y MITRE — *MITRE ATT&CK Enterprise v18* (`https://attack.mitre.org`). Marcos de cuantificación económica de riesgo y matriz de técnicas adversarias `[Verificado MS Learn]`.

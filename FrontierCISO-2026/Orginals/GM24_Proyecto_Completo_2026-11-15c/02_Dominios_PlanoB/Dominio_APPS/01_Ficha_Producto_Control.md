# 01 · Ficha de producto-control: Seguridad de aplicaciones SaaS y OAuth (Microsoft Defender for Cloud Apps + app governance + Conditional Access app control)

> **GM-24 V7.1 · Sub-plan PO-GAC · Instancia de dominio: Seguridad de aplicaciones SaaS y OAuth (Microsoft Defender for Cloud Apps + app governance + Conditional Access app control)** · 2026-11-14 · v1.0. Plano B (*ProductPractice* / escenario). No agrega ni modifica conceptos de la V7 (379): los instancia. Escenario 100 % Microsoft sobre bases agnósticas; estado GA/preview/verificar según Microsoft Learn. Referencias DD/K4x/R/eo:OP/COE: marco interno.

| Campo | Contenido |
|---|---|
| Producto-control | Seguridad de aplicaciones SaaS y OAuth (Microsoft Defender for Cloud Apps + app governance + Conditional Access app control) |
| Dominio Zero Trust | Aplicaciones (pilar Zero Trust); SaaS sancionadas y no sancionadas (shadow IT), apps OAuth y sus permisos (incl. agentes de IA conectados), sesiones a apps críticas; interfaz con Identidades (consentimiento, CA), Datos (file policies → Purview DLP desde ene-2027), XDR (alertas en la cola unificada) y con las flotas de agentes (OAuth apps de los propios agentes) |
| Tecnología | Microsoft Defender for Cloud Apps (cloud discovery, cloud app catalog con categoría Generative AI, app connectors, activity/anomaly policies, access/session policies vía CA app control, governance actions) + app governance (OAuth apps, políticas predefinidas/personalizadas, hygiene, detección de amenazas) + Microsoft Entra Conditional Access; Defender XDR (incidentes, hunting, Unified RBAC) |
| Funciones CSF 2.0 | ID.AM (inventario de apps y OAuth) · ID.RA (riesgo de apps, shadow IT, consentimientos) · PR.AA (acceso/sesión, consentimiento, permisos de apps) · PR.PS (configuración de políticas) · DE.CM/DE.AE (anomalías, actividad de apps) · RS.AN/RS.MI (deshabilitar app, revocar consentimiento, suspender usuario) · ID.IM (tuning, policy assessments) |
| Fuente oficial del modelo operativo | Microsoft Defender for Cloud Apps operational guide (daily/weekly/monthly/ad hoc) + app governance (manage, policies, hygiene, alerts) + cloud discovery policies + CA app control + anomaly detection policies + roles admin |
| Objetivo del control | Que las apps SaaS en uso estén descubiertas y clasificadas (sancionada / no sancionada / monitoreada, incl. apps de IA generativa), que toda app OAuth con permisos altos tenga dueño y justificación, que las sesiones a apps críticas estén controladas por políticas, que las anomalías se triajen en SLA y que las apps y credenciales inactivas se deshabiliten |
| SLO | Apps OAuth de alto privilegio sin dueño = 0; apps no sancionadas de alto riesgo con uso >N usuarios bloqueadas o justificadas ≤7 días; alertas High de anomalías/app governance triadas ≤4 h; apps y credenciales inactivas >90 días deshabilitadas ≤30 días; conectores de apps saludables 100 %; apps de IA generativa descubiertas con decisión (sancionar/bloquear/monitorear) ≤14 días |
| Owner | PO-GAC Apps (sponsor de los agentes PA-xx en Entra Agent ID) |
| Diferencia frente a otros dominios | Apps es el dominio donde conviven la mayor cantidad de decisiones de **negocio sobre tecnología** (sancionar o bloquear una app que un área usa) y el gobierno de la **cadena de consentimiento OAuth**, que es exactamente el mecanismo por el que los agentes de IA obtienen poder en el tenant. App governance ya muestra qué agentes de IA están conectados a qué apps OAuth: este dominio es el que ve a las flotas de agentes **desde afuera**, como apps con permisos. Hito: las file policies de MDA se retiran el 6-ene-2027; la protección de archivos pasa íntegramente a Purview DLP (Dominio_DATOS). |
| Interfaz con otros owners | Owner Identidades: consentimiento de usuarios, CA (las access/session policies requieren una política de CA en Entra; los cambios de CA los ejecuta IAM). Owner Datos: file policies hasta ene-2027 → Purview DLP; etiquetas en archivos SaaS. Owner XDR: alertas de MDA/app governance en la cola unificada. PO-GAC de cada flota: las identidades/apps OAuth de sus agentes aparecen en app governance; este dominio audita sus permisos. Dueños de negocio: decisión de sancionar/bloquear apps. |
| Personas (Learn) | SOC analysts (alertas y anomalías) · Security administrators / Cloud App Security administrator (políticas, discovery, OAuth) · Security & Compliance administrators (file policies hasta ene-2027) · IAM/Entra admins (CA) · Dueños de negocio (sanción de apps) |
| Permisos | Entra: Security Reader (lectura), Security Operator (alertas), Cloud App Security administrator (políticas, acciones, discovery), Compliance administrator (lectura + file policies), Conditional Access Administrator (solo humano); Unified RBAC en portal Defender; Graph: Policy.Read.All, ThreatHunting.Read.All |

## Grilla de ownership CSF 2.0 × dominio

| Categoría CSF 2.0 | Tareas del modelo operativo |
|---|---|
| DE.AE | AP-D01, AP-D05 |
| DE.CM | AP-D06, AP-W04 |
| GV.OV | AP-W01, AP-W02, AP-M04, AP-Q02, AP-A04 |
| GV.PO | AP-M02, AP-M03, AP-Q01 |
| GV.RM | AP-Q01 |
| GV.RR | AP-W06, AP-M05 |
| ID.AM | AP-D03, AP-D04, AP-W03, AP-W05 |
| ID.IM | AP-W01, AP-M01, AP-Q02, AP-Q04, AP-A05 |
| ID.RA | AP-D04, AP-W05, AP-A03 |
| PR.AA | AP-D03, AP-D05, AP-W03, AP-W06, AP-M02, AP-M03, AP-M05, AP-Q03, AP-A02 |
| PR.DS | AP-A04 |
| PR.PS | AP-D06, AP-A02, AP-A03 |
| RS | AP-D01, AP-D02, AP-W02, AP-M04, AP-A01, AP-A05 |
| RS.AN | AP-D02 |
| RS.CO | AP-M04, AP-A01 |
| RS.MA | AP-D01 |
| RS.MI | AP-D02, AP-W02, AP-A01 |

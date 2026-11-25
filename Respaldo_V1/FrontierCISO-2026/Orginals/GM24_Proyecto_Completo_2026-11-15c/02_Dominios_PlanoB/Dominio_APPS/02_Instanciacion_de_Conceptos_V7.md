# 02 · Cómo el dominio Apps instancia los conceptos V7 (sin modificarlos)

> **GM-24 V7.1 · Sub-plan PO-GAC · Instancia de dominio: Seguridad de aplicaciones SaaS y OAuth (Microsoft Defender for Cloud Apps + app governance + Conditional Access app control)** · 2026-11-14 · v1.0. Plano B (*ProductPractice* / escenario). No agrega ni modifica conceptos de la V7 (379): los instancia. Escenario 100 % Microsoft sobre bases agnósticas; estado GA/preview/verificar según Microsoft Learn. Referencias DD/K4x/R/eo:OP/COE: marco interno.

| Concepto V7 | Tipo | Unidad(es) | Concepto | Instancia |
|---|---|---|---|---|
| G2.2-PA03 | PA | G2.2 | Baseline, excepciones y overrides de un control técnico | Baseline = políticas de OAuth + access/session policies por app crítica + etiquetas sancionada/no sancionada; excepciones = IPs corporativas y alcances de anomalías con vencimiento. |
| G3.2-PA01 | PA | G3.2 | Aseguramiento continuo de la configuración del control (deriva) | Deriva: apps prohibidas re-habilitadas, políticas de sesión en report-only, conectores caídos. |
| M2.1-PA01 | PA | M2.1 | Registro de agentes como clase de activo | Inventario de apps SaaS y OAuth (incl. las de los agentes) como activos y fuentes de señal. |
| M2.2-PA01 | PA | M2.2 | Permisos de humanos y agentes en el control: RBAC unificado, roles y conectores | Permisos de humanos (roles MDA, CA Administrator solo humano) y de agentes (Graph scopes acotados). |
| AMP-33 | AMP | M2.2 | Identidades no humanas | Identidades no humanas: las apps OAuth son la forma en que las NHI y los agentes obtienen poder; app governance es su inventario externo. |
| AMP-36 | AMP | M3.1 | Límites de herramientas y permisos | Herramientas y conectores definen lo que un agente puede tocar: este dominio audita los permisos OAuth de las flotas desde afuera. |
| AMP-50 | AMP | M6.2 | Seguridad de herramientas y conectores | Conectores y MCP: los conectores de Power Platform y las apps OAuth de los agentes son objetos de app governance. |
| AMP-06 | AMP | G1.2 | Gobierno de la IA | Gobierno de la IA: cloud discovery con categoría Generative AI responde 'quién usa qué IA' (Shadow AI). |
| M6.2-K06 | K | M6.2 | Shadow AI | Shadow AI: instancia directa (apps de IA generativa descubiertas y gobernadas). |
| M3.1-PA02 | PA | M3.1 | Arquitectura de protección del dominio Zero Trust (instancias: correo y colaboración · detección y respuesta unificada · endpoints · identidades · datos) | Instancia Apps: arquitectura de protección (discovery → catálogo → sanción → conector → políticas de actividad/anomalía → CA app control → governance). |
| M4.1-PA01 | PA | M4.1 | Modelo operativo del producto-control por cadencias (instancias: Defender for Office 365 · Defender XDR · Defender for Endpoint · Defender for Identity/Entra · Purview · Sentinel · Defender for Cloud) | Instancia Apps del modelo operativo (26 tareas). |
| M4.1-PA03 | PA | M4.1 | Gestión de la calidad de detección del dominio: FP/FN, tuning, listas, indicadores y supresiones (instancias: MDO · XDR · MDE · MDI/ID Protection · Purview DLP · Sentinel) | Instancia Apps: FP de anomalías, IPs corporativas, policy assessments. |
| M4.2-PA01 | PA | M4.2 | Amenazas del dominio Zero Trust (instancias: correo y colaboración · cross-domain · endpoints · identidades · datos) | Instancia Apps: consentimiento ilícito, apps OAuth maliciosas, exfiltración vía SaaS, abuso de apps de IA. |
| M4.2-K11 | K | M4.2 | Escalamiento de privilegios en identidades humanas y no humanas como táctica adversaria | Escalamiento de privilegios vía consentimiento de apps y permisos de aplicación: camino agéntico típico. |
| HC-009 | HC | G4.1 · M2.2 | Gobierno de identidades no humanas | Accountability de identidades no humanas: cada app OAuth con dueño. |
| AMP-25 | AMP | G6.2 | Ética de autonomía | Ética: bloquear una app que un área usa o suspender a un usuario exige proporcionalidad y revisión humana. |
| M6.2-PA03 | PA | M6.2 | Bases multiplataforma, multicloud y multimodelo | Portabilidad: OAuth2/OIDC y CASB como bases agnósticas; CA app control como implementación. |
| G3.1-PA01 | PA | G3.1 | Panorama regulatorio de IA y agentes | Exposición regulatoria: apps SaaS con datos personales; decisiones sobre usuarios. |

## Hitos de plataforma que condicionan esta instancia

| Fecha | Hito | Efecto en el dominio |
|---|---|---|
| 6-ene-2027 | Retiro de file policies de Defender for Cloud Apps | Migrar protección de archivos a Purview DLP / auto-labeling (Dominio_DATOS); tarea AP-A04 |
| 15-oct-2026 | Retiro de detecciones EWS de app governance | Ajustar expectativas de cobertura de amenazas OAuth; usar detecciones Graph-based |
| jun-2025 → | Anomaly detection en modelo dinámico | Varias políticas legacy deshabilitadas; revisar tuning y alcance (AP-M01) |
| vigente | App governance incluido en la licencia de MDA; muestra agentes de IA conectados a OAuth apps | Base de AP-D03 y AP-W06: auditoría de las flotas desde afuera |

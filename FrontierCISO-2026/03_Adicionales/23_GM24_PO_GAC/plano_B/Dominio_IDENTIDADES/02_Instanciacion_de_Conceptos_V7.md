# 02 · Cómo el dominio Identidades instancia los conceptos V7 (sin modificarlos)

> **GM-24 V7.1 · Sub-plan PO-GAC · Instancia de dominio: Protección de identidades y acceso (Microsoft Defender for Identity + Microsoft Entra ID Protection + Conditional Access + Entra ID Governance)** · 2026-11-14 · v1.0. Plano B (*ProductPractice* / escenario). No agrega ni modifica conceptos de la V7 (379): los instancia. Escenario 100 % Microsoft sobre bases agnósticas; estado GA/preview/verificar según Microsoft Learn. Referencias DD/K4x/R/eo:OP/COE: marco interno.

| Concepto V7 | Tipo | Unidad(es) | Concepto | Instancia |
|---|---|---|---|---|
| G2.2-PA03 | PA | G2.2 | Baseline, excepciones y overrides de un control técnico | Baseline = políticas de CA basadas en riesgo + break-glass + exclusiones con vencimiento; excepciones = reglas de tuning. |
| G3.2-PA01 | PA | G3.2 | Aseguramiento continuo de la configuración del control (deriva) | Deriva: políticas CA en report-only que debían estar on; admins fuera de PIM. |
| M2.1-PA01 | PA | M2.1 | Registro de agentes como clase de activo | Inventario de identidades (humanas, NHI, agentes) y sensores. |
| M2.2-PA01 | PA | M2.2 | Permisos de humanos y agentes en el control: RBAC unificado, roles y conectores | Permisos de humanos (roles Entra) y agentes (Graph scopes acotados). |
| AMP-33 | AMP | M2.2 | Identidades no humanas | Identidades no humanas: owner natural; instancia directa. |
| AMP-34 | AMP | M2.2 | Identidad y autorización de agentes | Identidad propia, permisos mínimos, CA y ciclo de vida de agentes: sostiene AGC-05/06/18 de todas las flotas. |
| HC-009 | HC | G4.1 · M2.2 | Gobierno de identidades no humanas | Accountability de identidades no humanas: instancia directa. |
| M3.1-PA02 | PA | M3.1 | Arquitectura de protección del dominio Zero Trust (instancias: correo y colaboración · detección y respuesta unificada · endpoints · identidades · datos) | Instancia Identidades: arquitectura de protección (sensores MDI → ID Protection → unified risk → CA → Governance). |
| M4.1-PA01 | PA | M4.1 | Modelo operativo del producto-control por cadencias (instancias: Defender for Office 365 · Defender XDR · Defender for Endpoint · Defender for Identity/Entra · Purview · Sentinel · Defender for Cloud) | Instancia Identidades del modelo operativo (23 tareas). |
| M4.1-PA03 | PA | M4.1 | Gestión de la calidad de detección del dominio: FP/FN, tuning, listas, indicadores y supresiones (instancias: MDO · XDR · MDE · MDI/ID Protection · Purview DLP · Sentinel) | Instancia Identidades: tuning de MDI y FP de riesgo. |
| M4.2-PA01 | PA | M4.2 | Amenazas del dominio Zero Trust (instancias: correo y colaboración · cross-domain · endpoints · identidades · datos) | Instancia Identidades: credential theft, impossible travel, Golden Ticket, abuso de PIM. |
| M4.2-K11 | K | M4.2 | Escalamiento de privilegios en identidades humanas y no humanas como táctica adversaria | Escalamiento de privilegios: dominio donde la táctica se detecta y previene. |
| M4.1-K11 | K | M4.1 | Deception y señuelos como control detectivo | Señuelos: cuentas honeytoken en AD (MDI). |
| AMP-25 | AMP | G6.2 | Ética de autonomía | Ética de autonomía: bloquear personas es la acción más sensible. |
| G3.1-PA01 | PA | G3.1 | Panorama regulatorio de IA y agentes | Exposición regulatoria: agentes que deciden sobre acceso de personas. |

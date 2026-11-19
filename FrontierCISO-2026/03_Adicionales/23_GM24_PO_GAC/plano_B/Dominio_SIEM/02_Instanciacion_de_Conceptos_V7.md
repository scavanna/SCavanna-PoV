# 02 · Cómo el dominio Siem instancia los conceptos V7 (sin modificarlos)

> **GM-24 V7.1 · Sub-plan PO-GAC · Instancia de dominio: SIEM/SOAR y data lake de seguridad (Microsoft Sentinel en el portal de Microsoft Defender)** · 2026-11-14 · v1.0. Plano B (*ProductPractice* / escenario). No agrega ni modifica conceptos de la V7 (379): los instancia. Escenario 100 % Microsoft sobre bases agnósticas; estado GA/preview/verificar según Microsoft Learn. Referencias DD/K4x/R/eo:OP/COE: marco interno.

| Concepto V7 | Tipo | Unidad(es) | Concepto | Instancia |
|---|---|---|---|---|
| M4.1-PA01 | PA | M4.1 | Modelo operativo del producto-control por cadencias (instancias: Defender for Office 365 · Defender XDR · Defender for Endpoint · Defender for Identity/Entra · Purview · Sentinel · Defender for Cloud) | Instancia SIEM del modelo operativo (24 tareas). |
| M4.1-PA04 | PA | M4.1 | Hunting y detecciones personalizadas | Hunting y detecciones personalizadas: instancia natural. |
| M4.1-PA05 | PA | M4.1 | Observabilidad de la flota de agentes: telemetría, trazas y tableros | Observabilidad de la flota: Sentinel la realiza. |
| M4.1-K05 | K | M4.1 | SOAR | SOAR: automation rules y playbooks como antecedente determinista. |
| AMP-40 | AMP | M4.1 | Human-in-the-loop | HITL por riesgo aplicado a playbooks. |
| M1.2-PA01 | PA | M1.2 | FinOps de agentes: presupuesto, costo por tarea y alertas de consumo | FinOps: ingesta y retención como costo variable. |
| G2.2-PA03 | PA | G2.2 | Baseline, excepciones y overrides de un control técnico | Baseline = reglas versionadas; excepciones = supresiones con vencimiento. |
| G3.2-PA01 | PA | G3.2 | Aseguramiento continuo de la configuración del control (deriva) | Deriva: reglas deshabilitadas, conectores caídos. |
| M2.1-PA01 | PA | M2.1 | Registro de agentes como clase de activo | Inventario de fuentes de datos. |
| M2.2-PA01 | PA | M2.2 | Permisos de humanos y agentes en el control: RBAC unificado, roles y conectores | Roles de Sentinel/Logic Apps para humanos y agentes. |
| M4.2-K11 | K | M4.2 | Escalamiento de privilegios en identidades humanas y no humanas como táctica adversaria | Detección de escalamiento con reglas cross-source. |
| M4.1-K11 | K | M4.1 | Deception y señuelos como control detectivo | Señuelos: reglas sobre honeytokens. |
| M6.1-PA01 | PA | M6.1 | Operación degradada del SOC sin agentes ni modelos | Operación degradada: pérdida de visibilidad. |
| M6.2-PA03 | PA | M6.2 | Bases multiplataforma, multicloud y multimodelo | Portabilidad: ASIM, KQL, STIX, OTel. |
| HC-017 | HC | G5.1 · G6.1 · M4.1 | Inteligencia que modifica decisiones | Inteligencia y detección integradas: instancia directa. |

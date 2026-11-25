# 02 · Cómo el dominio Nube instancia los conceptos V7 (sin modificarlos)

> **GM-24 V7.1 · Sub-plan PO-GAC · Instancia de dominio: Postura y protección de cargas de trabajo en la nube (Microsoft Defender for Cloud: CSPM, CWPP, Defender for AI Services)** · 2026-11-14 · v1.0. Plano B (*ProductPractice* / escenario). No agrega ni modifica conceptos de la V7 (379): los instancia. Escenario 100 % Microsoft sobre bases agnósticas; estado GA/preview/verificar según Microsoft Learn. Referencias DD/K4x/R/eo:OP/COE: marco interno.

| Concepto V7 | Tipo | Unidad(es) | Concepto | Instancia |
|---|---|---|---|---|
| M4.1-PA01 | PA | M4.1 | Modelo operativo del producto-control por cadencias (instancias: Defender for Office 365 · Defender XDR · Defender for Endpoint · Defender for Identity/Entra · Purview · Sentinel · Defender for Cloud) | Instancia Nube del modelo operativo (23 tareas). |
| AMP-51 | AMP | M6.2 | Postura de IA en nube | Postura de IA en nube: instancia directa. |
| M6.2-K02 | K | M6.2 | Seguridad Nube | Seguridad nube / multicloud: instancia directa. |
| M6.2-K07 | K | M6.2 | Responsabilidad Compartida | Responsabilidad compartida. |
| G2.2-PA03 | PA | G2.2 | Baseline, excepciones y overrides de un control técnico | Baseline = MCSB + estándares + governance rules; excepciones = exenciones con vencimiento. |
| G3.2-PA01 | PA | G3.2 | Aseguramiento continuo de la configuración del control (deriva) | Deriva: vencidas, exenciones acumuladas, recursos sin plan. |
| HC-005 | HC | G3.1 · G3.2 · M3.2 · M4.1 | Cumplimiento continuo orientado a resultados | Cumplimiento continuo: regulatory compliance dashboard como evidencia. |
| G4.2-PA01 | PA | G4.2 | KRIs de la flota de agentes y umbrales de intervención | KRIs: attack paths críticos, vencidas, sin plan. |
| M1.1-PA02 | PA | M1.1 | Portafolio de productos-control con owners | Portafolio: el owner Nube delega remediación a dueños de suscripción. |
| M2.1-PA01 | PA | M2.1 | Registro de agentes como clase de activo | Inventario multicloud. |
| M2.2-PA01 | PA | M2.2 | Permisos de humanos y agentes en el control: RBAC unificado, roles y conectores | Azure RBAC + cloud scopes. |
| M4.2-K11 | K | M4.2 | Escalamiento de privilegios en identidades humanas y no humanas como táctica adversaria | Permisos excesivos en rutas de ataque. |
| M3.1-K12 | K | M3.1 | Seguridad física, ambiental y mantenimiento como dependencias del control | Dependencias físicas: responsabilidad del proveedor. |
| M1.2-PA01 | PA | M1.2 | FinOps de agentes: presupuesto, costo por tarea y alertas de consumo | FinOps: DWU y planes. |
| HC-038 | HC | G2.2 · M2.2 · M3.1 · M3.2 | Aseguramiento de la arquitectura Zero Trust | Zero Trust como aseguramiento en nube: JIT, deny, mínimo privilegio. |

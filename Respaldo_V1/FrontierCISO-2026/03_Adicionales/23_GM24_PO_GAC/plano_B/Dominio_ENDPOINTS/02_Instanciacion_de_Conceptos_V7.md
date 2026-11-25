# 02 · Cómo el dominio Endpoints instancia los conceptos V7 (sin modificarlos)

> **GM-24 V7.1 · Sub-plan PO-GAC · Instancia de dominio: Protección, detección y respuesta en endpoints (Microsoft Defender for Endpoint + Defender Vulnerability Management + Intune)** · 2026-11-14 · v1.0. Plano B (*ProductPractice* / escenario). No agrega ni modifica conceptos de la V7 (379): los instancia. Escenario 100 % Microsoft sobre bases agnósticas; estado GA/preview/verificar según Microsoft Learn. Referencias DD/K4x/R/eo:OP/COE: marco interno.

| Concepto V7 | Tipo | Unidad(es) | Concepto | Instancia |
|---|---|---|---|---|
| G2.2-PA03 | PA | G2.2 | Baseline, excepciones y overrides de un control técnico | Baseline = ASR en block + Intune security baselines + niveles de automatización por grupo; excepciones = indicadores/exclusiones con vencimiento. |
| G3.2-PA01 | PA | G3.2 | Aseguramiento continuo de la configuración del control (deriva) | Deriva: ASR audit vs. block, baselines de Intune, device groups y RBAC. |
| M2.1-PA01 | PA | M2.1 | Registro de agentes como clase de activo | Inventario de dispositivos gestionados/no gestionados; discovery. |
| M2.2-PA01 | PA | M2.2 | Permisos de humanos y agentes en el control: RBAC unificado, roles y conectores | Permisos por device group (Unified RBAC) para humanos y agentes. |
| M3.1-PA02 | PA | M3.1 | Arquitectura de protección del dominio Zero Trust (instancias: correo y colaboración · detección y respuesta unificada · endpoints · identidades · datos) | Instancia Endpoints: arquitectura de protección en capas (ASR → NGP → EDR → attack disruption → TVM). |
| M4.1-PA01 | PA | M4.1 | Modelo operativo del producto-control por cadencias (instancias: Defender for Office 365 · Defender XDR · Defender for Endpoint · Defender for Identity/Entra · Purview · Sentinel · Defender for Cloud) | Instancia Endpoints del modelo operativo (26 tareas). |
| M4.1-PA03 | PA | M4.1 | Gestión de la calidad de detección del dominio: FP/FN, tuning, listas, indicadores y supresiones (instancias: MDO · XDR · MDE · MDI/ID Protection · Purview DLP · Sentinel) | Instancia Endpoints: FP/FN, indicadores, exclusiones ASR/AV. |
| M4.2-PA01 | PA | M4.2 | Amenazas del dominio Zero Trust (instancias: correo y colaboración · cross-domain · endpoints · identidades · datos) | Instancia Endpoints: ransomware humano-operado, LOLBins, abuso de USB/web. |
| M4.2-K11 | K | M4.2 | Escalamiento de privilegios en identidades humanas y no humanas como táctica adversaria | Escalamiento de privilegios en dispositivos detectado por EDR. |
| M5.2-PA01 | PA | M5.2 | Ejecución de respuesta en correo: AIR, acciones manuales y acciones de agentes con aprobación | Respuesta con acciones de dispositivo y agentes con aprobación. |
| AMP-38 | AMP | M3.2 | Pruebas de controles autónomos | Probar controles autónomos: attack disruption y remediación embebida. |
| HC-030 | HC | M3.1 · M5.1 · M6.1 · M6.2 | Seguridad industrial y continuidad de negocio | OT/IoT: dispositivos descubiertos no gestionables como frontera del control. |
| M3.1-K12 | K | M3.1 | Seguridad física, ambiental y mantenimiento como dependencias del control | Dependencias físicas y mantenimiento: parches, hardware. |

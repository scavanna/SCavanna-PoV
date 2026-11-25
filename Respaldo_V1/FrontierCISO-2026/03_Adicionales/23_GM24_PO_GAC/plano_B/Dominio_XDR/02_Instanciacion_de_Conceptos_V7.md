# 02 · Cómo el dominio XDR instancia los conceptos V7 (sin modificarlos)

> **GM-24 V7.1 · Sub-plan PO-GAC · Instancia de dominio: Detección y respuesta unificada (Microsoft Defender XDR)** · 2026-11-14 · Dominio_XDR v1.0. Nivel de abstracción: *ProductPractice* / escenario (plano B). No agrega ni modifica conceptos de la V7 (379): los instancia. Escenario 100 % Microsoft sobre bases agnósticas; estado GA/preview/verificar según Microsoft Learn. Referencias DD/K4x/R/eo:OP/COE: marco interno.

## 1. Principio

Los 379 conceptos son el nivel curricular. Un dominio es el nivel de **instancia**: el mismo concepto se ejercita con otra tecnología, otro modelo operativo y otros agentes (`ProductPractice` EXEMPLIFIES `eo:OP`; agente REALIZED_WITH capacidad). Construir XDR **no agrega conceptos**.

## 2. Tabla de instanciación (31)

| Concepto V7 | Tipo | Unidad(es) | Concepto | Instancia XDR |
|---|---|---|---|---|
| G1.1-PA01 | PA | G1.1 | Rol dual especialista/manager y Product Owner de control | Ficha de rol PO-GAC XDR: owner de la cola, la automatización, Unified RBAC y la salud de ingesta. |
| G2.1-PA01 | PA | G2.1 | Grilla de ownership: NIST CSF 2.0 × dominios Zero Trust | Grilla CSF × ZT para el pilar SecOps. |
| G2.2-PA03 | PA | G2.2 | Baseline, excepciones y overrides de un control técnico | Baseline de automatización (AIR por grupo) y de políticas de alertas; excepciones = reglas de tuning con vencimiento. |
| G3.2-PA01 | PA | G3.2 | Aseguramiento continuo de la configuración del control (deriva) | Deriva: niveles AIR, políticas de alertas, RBAC vs. baseline. |
| G4.2-PA01 | PA | G4.2 | KRIs de la flota de agentes y umbrales de intervención | KRIs de la flota XDR: acciones revertidas, aislamientos erróneos, tuning sin vencimiento. |
| M1.1-PA02 | PA | M1.1 | Portafolio de productos-control con owners | El owner XDR como integrador del portafolio de productos-control. |
| M1.1-PA03 | PA | M1.1 | Modelo operativo por cadencias y excelencia operacional como requisito del programa | Modelo operativo por cadencias derivado de la SecOps guide de Defender XDR + guías MDE/MDI/MDA. |
| M2.2-PA01 | PA | M2.2 | Permisos de humanos y agentes en el control: RBAC unificado, roles y conectores | Matriz tarea→rol→permiso con Unified RBAC para humanos y agentes. |
| M3.1-PA01 | PA | M3.1 | Arquitectura de referencia del SOC agéntico con control plane | Arquitectura del SOC agéntico: XDR es la capa de plataforma. |
| M3.1-PA02 | PA | M3.1 | Arquitectura de protección del dominio Zero Trust (instancias: correo y colaboración · detección y respuesta unificada · endpoints · identidades · datos) | Instancia XDR: arquitectura de correlación (sensores → incidentes → AIR → Action center → Sentinel). |
| M3.2-PA01 | PA | M3.2 | El control como producto: objetivo → configuración → evidencia | Cadena objetivo → configuración → evidencia para 5 controles XDR. |
| M3.2-PA02 | PA | M3.2 | Catálogo de controles de gobierno y gestión de agentes (AGC) | Evaluación de la flota XDR contra los 24 AGC. |
| M3.2-PA03 | PA | M3.2 | Evaluación de calidad de agentes: datasets dorados, regresión y criterios de aceptación | Dataset dorado de incidentes unificados para XA-01. |
| M4.1-PA01 | PA | M4.1 | Modelo operativo del producto-control por cadencias (instancias: Defender for Office 365 · Defender XDR · Defender for Endpoint · Defender for Identity/Entra · Purview · Sentinel · Defender for Cloud) | Instancia XDR del modelo operativo (28 tareas). |
| M4.1-PA02 | PA | M4.1 | Gestión de incidentes y alertas en Defender XDR | Gestión de incidentes en Defender XDR: instancia natural. |
| M4.1-PA03 | PA | M4.1 | Gestión de la calidad de detección del dominio: FP/FN, tuning, listas, indicadores y supresiones (instancias: MDO · XDR · MDE · MDI/ID Protection · Purview DLP · Sentinel) | Instancia XDR: tuning multi-sensor y FP/FN. |
| M4.1-PA04 | PA | M4.1 | Hunting y detecciones personalizadas | Hunting cross-domain y detecciones personalizadas. |
| M4.1-PA05 | PA | M4.1 | Observabilidad de la flota de agentes: telemetría, trazas y tableros | Observabilidad de la flota XDR en Sentinel. |
| M4.1-PA06 | PA | M4.1 | Gestión del desempeño de agentes: revisión periódica y drift | Revisión trimestral de desempeño de los 15 agentes XDR. |
| M4.2-PA01 | PA | M4.2 | Amenazas del dominio Zero Trust (instancias: correo y colaboración · cross-domain · endpoints · identidades · datos) | Instancia XDR: amenazas cross-domain. |
| M4.2-PA02 | PA | M4.2 | Catálogos de amenazas a sistemas agénticos aplicados a la flota | Matriz amenaza→agente→control para los 15 agentes XDR. |
| M5.1-PA01 | PA | M5.1 | Playbooks de incidentes de correo con roles humano/agente | Playbooks híbridos del CSIRT con ejecutores humano/AIR/agente. |
| M5.2-PA01 | PA | M5.2 | Ejecución de respuesta en correo: AIR, acciones manuales y acciones de agentes con aprobación | Respuesta con AIR, acciones manuales y acciones de agentes con aprobación. |
| M6.1-PA01 | PA | M6.1 | Operación degradada del SOC sin agentes ni modelos | Operación degradada del SOC sin agentes ni AIR. |
| M6.2-PA01 | PA | M6.2 | Plataformas y rutas de construcción de agentes y responsabilidad compartida en IA | Rutas de construcción: XA-01/02/06 preferentemente R1. |
| AMP-39 | AMP | M4.1 | SOC agéntico | SOC agéntico: redistribución del runbook XDR. |
| AMP-40 | AMP | M4.1 | Human-in-the-loop | HITL por riesgo aplicado a acciones de respuesta cross-domain. |
| AMP-44 | AMP | M5.1 | Kill switch y escalamiento | Kill switch probado para agentes con permisos Response (Manage). |
| HC-019 | HC | M4.1 · M5.2 | SOC agéntico con supervisión humana | XDR, SOAR, IA y decisiones de contención gobernadas: instancia directa. |
| M4.1-K11 | K | M4.1 | Deception y señuelos como control detectivo | Señuelos (cuentas honeytoken en MDI, dispositivos señuelo) en la cola unificada. |
| M4.2-K11 | K | M4.2 | Escalamiento de privilegios en identidades humanas y no humanas como táctica adversaria | Escalamiento de privilegios detectado cross-domain. |

## 3. Generalización V7.1

| ID | Título V7 | Título V7.1 |
|---|---|---|
| M3.1-PA02 | Arquitectura de protección de correo y colaboración | Arquitectura de protección del dominio Zero Trust (instancias: correo y colaboración · detección y respuesta unificada · endpoints · identidades · datos) |
| M4.2-PA01 | Amenazas al correo y la colaboración | Amenazas del dominio Zero Trust (instancias: correo y colaboración · cross-domain · endpoints · identidades · datos) |
| M4.1-PA01 | Modelo operativo de Defender for Office 365 en Defender XDR | Modelo operativo del producto-control por cadencias (instancias: Defender for Office 365 · Defender XDR · Defender for Endpoint · Defender for Identity/Entra · Purview · Sentinel · Defender for Cloud) |
| M4.1-PA03 | Gestión de falsos positivos/negativos y listas | Gestión de la calidad de detección del dominio: FP/FN, tuning, listas, indicadores y supresiones (instancias: MDO · XDR · MDE · MDI/ID Protection · Purview DLP · Sentinel) |

# 01 · Ficha de producto-control: Detección y respuesta unificada (Microsoft Defender XDR)

> **GM-24 V7.1 · Sub-plan PO-GAC · Instancia de dominio: Detección y respuesta unificada (Microsoft Defender XDR)** · 2026-11-14 · Dominio_XDR v1.0. Nivel de abstracción: *ProductPractice* / escenario (plano B). No agrega ni modifica conceptos de la V7 (379): los instancia. Escenario 100 % Microsoft sobre bases agnósticas; estado GA/preview/verificar según Microsoft Learn. Referencias DD/K4x/R/eo:OP/COE: marco interno.

## 1. Respuestas previas (por qué esta instancia no toca los 379)

- **Productividad fue un ejemplo.** El rol PO-GAC se define como función CSF × dominio Zero Trust × tecnología × modelo operativo; productividad fue un valor del eje "dominio".
- **XDR es la segunda instancia.** Mismo rol, mismas competencias, mismos conceptos; cambian el dominio (SecOps), la tecnología (Defender XDR) y el modelo operativo.
- **Nivel de abstracción.** Los 379 son conceptos-lección; este paquete es su instancia de dominio. 4 PA promovidos en V7 tenían título específico de correo: la V7.1 los generalizó sin cambiar IDs ni cantidad (ver §6).

## 2. Ficha

| Campo | Contenido |
|---|---|
| Producto-control | Detección y respuesta unificada (Microsoft Defender XDR) |
| Dominio Zero Trust | SecOps — visibilidad, automatización y orquestación (pilar transversal de Zero Trust); protege incidentes que cruzan identidades, endpoints, correo, apps en la nube e identidades híbridas |
| Tecnología | Microsoft Defender XDR (portal unificado: cola de incidentes, AIR, Action center, Advanced Hunting, Threat analytics, custom detections, Unified RBAC, Exposure Management) + sensores: Defender for Endpoint, Defender for Identity, Defender for Office 365, Defender for Cloud Apps; integración con Microsoft Sentinel |
| Funciones CSF 2.0 | GV.RR/GV.OV · ID.RA/ID.IM · PR.PS · DE.CM/DE.AE · RS.MA/RS.AN/RS.MI/RS.CO · RC.RP |
| Fuente oficial del modelo operativo | Microsoft Defender XDR Security Operations Guide (pasos 1–6) + guías operativas de Defender for Endpoint, Defender for Identity y Defender for Cloud Apps |
| Objetivo del control | Que todo incidente multi-señal sea triado, investigado, contenido y resuelto dentro del SLA, con automatización gobernada (AIR, automation rules, agentes) y con la cadena de sensores saludable |
| SLO | Incidentes High triados ≤30 min, Medium ≤4 h; MTTR High ≤8 h; sensores EDR saludables ≥98 %; AIR en nivel 'full' en grupos acordados |
| Owner | PO-GAC XDR (sponsor de los 15 agentes XA-01…XA-15 en Entra Agent ID) |
| Diferencia frente a productividad | Productividad protege un canal con un sensor; XDR gobierna la correlación entre sensores y la automatización transversal. El owner XDR es dueño de la cola, de la automatización, de Unified RBAC y de la salud de la ingesta; no de la configuración de cada sensor. |
| Interfaz con otros owners | Owners de dominio (productividad, endpoints, identidades, apps) configuran sus sensores; el owner XDR gobierna cómo sus alertas se correlacionan y automatizan. Es el 'integrador' del portafolio. |
| Personas SOC (Learn, step 4) | SOC Oversight · Threat Intelligence & Analytics · Monitoring (Tier 1-3) · Engineering & SecOps · CSIRT |
| Permisos (Unified RBAC) | Security data basics (Read) · Alerts (Manage) · Response (Manage) · Basic/Advanced live response · File collection · Email & collaboration quarantine/advanced actions · Automation rules · Playbooks · Integrations |

## 3. Grilla de ownership CSF 2.0 × dominio SecOps (XDR)

| Categoría CSF 2.0 | Qué hace el control XDR | Tarea(s) | Dueño |
|---|---|---|---|
| GV.RR | Roles SOC y Unified RBAC para humanos y agentes | XDR-M02 | PO-GAC XDR + IAM |
| GV.OV | Supervisión de la automatización, informes, cambios de plataforma | XDR-D03, XDR-M04, XDR-W05 | PO-GAC XDR |
| GV.PO | Casos de uso, playbooks, baseline de automatización | XDR-Q01, XDR-M01 | PO-GAC XDR + CSIRT |
| ID.RA | Threat analytics, hunting, exposición | XDR-D07, XDR-W01, XDR-W03 | TI + Monitoring |
| ID.AM | Inventario de fuentes de señal | XDR-A04 | Engineering |
| ID.IM | Clasificación, tuning, lecciones, Secure Score | XDR-D04, XDR-D05, XDR-M05 | Monitoring + SOC Oversight |
| PR.PS | Niveles AIR, políticas de alertas, salud de sensores | XDR-M01, XDR-D06 | Security Administration |
| PR.AA | Unified RBAC, recertificación, identidades de agentes | XDR-M02, XDR-Q03 | IAM |
| DE.CM | Cola unificada, hunting, informes de amenazas | XDR-D01, XDR-W01, XDR-W04 | Monitoring |
| DE.AE | Correlación, detecciones personalizadas, automation rules | XDR-W02, XDR-D04 | Engineering + Monitoring |
| RS.MA | Gestión de incidentes y casos, escalamiento ITSM | XDR-D01, XDR-D08, XDR-A03 | Monitoring |
| RS.AN | Investigación, live response, forense | XDR-D02, XDR-A02 | Tier 2-3 + CSIRT |
| RS.MI | Acciones de respuesta, AIR | XDR-D02, XDR-D03, XDR-A01 | Monitoring + CSIRT |
| RS.CO | Notificaciones, comunicación de incidentes mayores | XDR-D08, XDR-A01 | SOC Oversight |
| RC.RP | Recuperación tras contención | XDR-A01 | CSIRT + owners de dominio |

## 4. KPIs / KRIs del control XDR

| ID | Indicador | Definición | Meta | Cadencia | Tipo |
|---|---|---|---|---|---|
| XKPI-01 | SLA de triaje High/Medium | Incidentes H/M triados en SLA | ≥95 % | Semanal | KPI control |
| XKPI-02 | MTTR por severidad | Creación→resolución | High ≤8 h | Mensual | KPI control |
| XKPI-03 | Acciones AIR pendientes >4 h | Sin decisión | 0 | Diaria | KRI control |
| XKPI-04 | Salud de sensores | % EDR/AV saludables; MDI sin issues | ≥98 %; 0 | Diaria | KPI control |
| XKPI-05 | Dispositivos no onboarded | Sin EDR | Tendencia ↓ | Semanal | KRI control |
| XKPI-06 | Reglas de tuning sin vencimiento | Supresiones huérfanas | 0 | Mensual | KRI control |
| XKPI-07 | Grupos fuera del baseline AIR | Desviaciones | 0 | Mensual | KRI control |
| XKPI-08 | Asignaciones RBAC sin justificación | Humanos y agentes | 0 | Mensual | KRI gobierno |
| XKPI-09 | Precisión del agente de triaje | Propuestas aceptadas | ≥90 % | Mensual | KPI agente |
| XKPI-10 | Acciones de respuesta revertidas | Aislamientos/revocaciones revertidos | <2 % | Mensual | KRI agente |
| XKPI-11 | Tasa de escalamiento a humano | Fuera de alcance | 10–30 % | Mensual | KPI agente |
| XKPI-12 | Costo por incidente asistido | SCU/tokens / incidentes | Según presupuesto | Mensual | KPI FinOps |
| XKPI-13 | Cobertura de observabilidad | Agentes con telemetría en Sentinel | 100 % | Mensual | KPI gobierno |
| XKPI-14 | Horas humanas liberadas (medidas) | Tareas ejecutadas por agentes | Según caso de negocio | Trimestral | KPI valor |

## 5. Permisos mínimos por grupo de tareas (Unified RBAC)

| Grupo | Humano | Agente |
|---|---|---|
| Triaje / clasificación / casos | Security data basics + Alerts (Manage) | Security data basics (Read); clasificación tras aprobación |
| Investigación y respuesta | Alerts + Response (Manage); live response según tier | Lectura + acciones acotadas tras aprobación; nunca live response |
| Action center | Response (Manage) | Response (Read); prepara decisión |
| Tuning / detecciones / automation | Alerts (Manage), Custom detections, Automation rules | Lectura + propuestas; creación con aprobación |
| Salud / postura / informes | Security data basics; Security Administrator | Solo lectura |
| RBAC / baseline | Authorization (Manage) | RoleManagement.Read.Defender (lectura) |

## 6. Generalización V7.1 (editorial, sin impacto en IDs ni cantidad)

| ID | Título V7 (específico de correo) | Título V7.1 |
|---|---|---|
| M3.1-PA02 | Arquitectura de protección de correo y colaboración | Arquitectura de protección del dominio Zero Trust (instancias: correo y colaboración · detección y respuesta unificada · endpoints · identidades · datos) |
| M4.2-PA01 | Amenazas al correo y la colaboración | Amenazas del dominio Zero Trust (instancias: correo y colaboración · cross-domain · endpoints · identidades · datos) |
| M4.1-PA01 | Modelo operativo de Defender for Office 365 en Defender XDR | Modelo operativo del producto-control por cadencias (instancias: Defender for Office 365 · Defender XDR · Defender for Endpoint · Defender for Identity/Entra · Purview · Sentinel · Defender for Cloud) |
| M4.1-PA03 | Gestión de falsos positivos/negativos y listas | Gestión de la calidad de detección del dominio: FP/FN, tuning, listas, indicadores y supresiones (instancias: MDO · XDR · MDE · MDI/ID Protection · Purview DLP · Sentinel) |

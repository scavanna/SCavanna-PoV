# 03 · Mapeo al GM-24 y análisis de brecha (V7.1)

> **GM-24 V7.1 · The Next CISO + Sub-plan PO-GAC** · 2026-11-14. Catálogo: 379 conceptos (245 K · 52 AMP · 40 HC · 42 PA), todos con pre-ensayo íntegro y mapeados a 17 marcos (NIST/ISACA/MITRE/OWASP/CIS/CSA). V7.1 = ChangeSet editorial CS-GM24-V7.1-001 (4 títulos generalizados; sin cambio de IDs, cantidad ni mapeo). Plano A (corpus académico). Referencias DD/K4x/R/eo:OP/COE: marco interno.

## 1. Conceptos PA (42)
| ID | Unidad | Concepto | Definición | Brecha frente a los 331 | Relaciones | h | Competencias | Origen |
|---|---|---|---|---|---|---|---|---|
| G1.1-PA01 | G1.1 | Rol dual especialista/manager y Product Owner de control | El analista evoluciona a owner de un producto-control (CSF 2.0 × dominio Zero Trust × tecnología × modelo operativo) y a manager de la fuerza de trabajo híbrida que lo opera. | Ningún K/AMP/HC define el ownership de un control como producto ni el rol intermedio entre analista y CISO. | G1.1-K03 (EXTIENDE); AMP-27 (SE_APOYA_EN); AMP-29 (SE_APOYA_EN); HC-037 (SE_RELACIONA) | 4 | C1.1, C6.1 | G1.1-PA02 (V5) |
| G1.2-PA01 | G1.2 | Economía unitaria de agentes: caso de negocio y TCO | Caso de negocio con costos variables de consumo (SCU, créditos, tokens), costo por tarea, capacidad liberada medida, riesgo reducido e introducido. | K05/K06 y HC-006 no consideran costos variables de IA ni costo por tarea. | G1.2-K05 (EXTIENDE); G1.2-K06 (EXTIENDE); HC-006 (PROFUNDIZA); AMP-29 (SE_RELACIONA) | 4 | C8.2, C6.4 | G1.2-PA01 (V5) |
| G2.1-PA01 | G2.1 | Grilla de ownership: NIST CSF 2.0 × dominios Zero Trust | Funciones/categorías del CSF 2.0 y pilares Zero Trust como coordenadas para asignar ownership de productos-control. | El CSF se enseña como marco y Zero Trust como arquitectura; ninguno los usa como instrumento de asignación de ownership. | G2.1-K04 (OPERACIONALIZA); AMP-07 (SE_APOYA_EN); HC-015 (COMPLEMENTA); M2.2-K05 (SE_RELACIONA) | 6 | C1.2, C1.1 | G2.1-PA01 + G2.1-PA04 (V5) |
| G2.1-PA02 | G2.1 | Marcos de gobierno de IA aplicados: NIST AI RMF e ISO/IEC 42001 | GOVERN/MAP/MEASURE/MANAGE y el sistema de gestión de IA de ISO/IEC 42001 aplicados a los agentes del SOC y conectados con el SGSI. | AMP-06 y HC-012 no nombran ni aplican los marcos. | AMP-06 (OPERACIONALIZA); HC-012 (SE_APOYA_EN); G2.1-K05 (INSTANCIA_DE); AMP-08 (SE_RELACIONA) | 4 | C5.1 | G2.1-PA02 (V5) |
| G2.2-PA01 | G2.2 | Política de uso y gobierno de agentes | Documento normativo con alcance, autorizaciones, prohibiciones, autonomía permitida, identidad, datos, evidencia y revisión para agentes. | Falta el artefacto normativo concreto para agentes en la jerarquía documental. | AMP-06 (OPERACIONALIZA); G2.2-K02 (INSTANCIA_DE); AMP-09 (SE_RELACIONA) | 4 | C5.1, C1.5 | G2.2-PA01 (V5) |
| G2.2-PA02 | G2.2 | Estándar de ficha de agente (charter) y runbooks de agentes | Estándar que describe cada agente (propósito, tareas, herramientas, límites, autonomía, dueño, KPIs, escalamiento) y sus procedimientos de operación. | AMP-28/36 piden roles y límites pero no definen el estándar documental. | G2.2-K03 (INSTANCIA_DE); G2.2-K04 (INSTANCIA_DE); AMP-28 (SE_APOYA_EN); AMP-36 (SE_APOYA_EN) | 4 | C4.2, C3.1 | G2.2-PA02 (V5) |
| G2.2-PA03 | G2.2 | Baseline, excepciones y overrides de un control técnico | Baseline (Standard/Strict), excepciones, overrides y revisiones periódicas como instancias de la jerarquía documental, con vencimiento y evidencia. | HC-028 y AMP-10 son generales; falta el puente política → configuración de producto. | G2.2-K09 (INSTANCIA_DE); HC-028 (PROFUNDIZA); AMP-10 (SE_APOYA_EN); AMP-09 (SE_RELACIONA) | 4 | C1.5, C2.4 | G2.2-PA03 (V5) |
| G3.1-PA01 | G3.1 | Panorama regulatorio de IA y agentes | Obligaciones (EU AI Act, normas locales, privacidad) que afectan a agentes que procesan datos personales o toman decisiones. | K01/K03 y AMP-11/12 no recorren la regulación específica de IA. | G3.1-K01 (EXTIENDE); G3.1-K03 (EXTIENDE); AMP-11 (SE_RELACIONA); AMP-12 (SE_RELACIONA) | 3 | C5.4, C5.1 | G3.1-PA01 (V5) |
| G3.2-PA01 | G3.2 | Aseguramiento continuo de la configuración del control (deriva) | Verificación continua de que la configuración se mantiene en baseline; detección y corrección de deriva con KPI. | K02 y AMP-13 enuncian aseguramiento y evidencia continua sin instrumentos. | G3.2-K02 (INSTANCIA_DE); AMP-13 (SE_APOYA_EN); HC-005 (SE_RELACIONA); HC-018 (SE_RELACIONA) | 4 | C2.4, C1.4 | G3.2-PA02 (V5) |
| G4.1-PA01 | G4.1 | Tres líneas de defensa para la flota de agentes | Owner (1ª), gobierno de IA/riesgo (2ª), auditoría (3ª); derechos de decisión y escalamiento. | K03/K08 se enseñan para personas; HC-009 no asigna líneas. | G4.1-K03 (INSTANCIA_DE); G4.1-K08 (INSTANCIA_DE); HC-009 (PROFUNDIZA) | 4 | C5.5, C8.1 | G4.1-PA01 (V5) |
| G4.1-PA02 | G4.1 | Taxonomía y registro de riesgos de agentes | Taxonomía operativa (agencia excesiva, inyección, fuga, drift, costo, dependencia, cascada) y registro con dueño y tratamiento. | AMP-20/15 cubren modelos y riesgo sistémico; falta la taxonomía operativa de agentes. | AMP-20 (EXTIENDE); AMP-15 (SE_RELACIONA); G4.1-K05 (INSTANCIA_DE); HC-016 (SE_RELACIONA) | 4 | C8.1, C4.6 | G4.1-PA02 (V5) |
| G4.2-PA01 | G4.2 | KRIs de la flota de agentes y umbrales de intervención | Indicadores de riesgo de la flota con umbrales que disparan revisión o pausa. | K09 es general; AMP-17/18 fijan límites sin indicadores. | G4.2-K09 (INSTANCIA_DE); AMP-18 (OPERACIONALIZA); HC-027 (SE_APOYA_EN) | 4 | C8.1, C6.2 | G4.2-PA02 (V5) |
| G6.1-PA01 | G6.1 | Reporte ejecutivo del producto-control y de la fuerza de trabajo híbrida | Valor, costo, riesgo, incidentes, desempeño de humanos, agentes y proveedores, decisiones requeridas. | Ningún concepto reporta agentes como fuerza de trabajo. | G6.1-K05 (INSTANCIA_DE); G6.1-K06 (INSTANCIA_DE); AMP-23 (SE_APOYA_EN); HC-027 (SE_APOYA_EN) | 3 | C8.3 | G6.1-PA01 (V5) |
| G6.2-PA01 | G6.2 | Métricas de efectividad del gobierno de la flota | Cobertura del registro, agentes con dueño, revisiones a tiempo, incidentes evitados, hallazgos de auditoría. | K05/K06 miden gobierno sin agentes; AMP-26 sin métricas. | G6.2-K05 (INSTANCIA_DE); G6.2-K06 (INSTANCIA_DE); AMP-26 (SE_RELACIONA); HC-027 (SE_APOYA_EN) | 3 | C6.2, C5.1 | G6.2-PA03 (V5) |
| M1.1-PA01 | M1.1 | Diseño organizativo híbrido: roles, RACI y span of control | Roles, funciones y supervisión entre humanos, agentes y proveedores; organigrama híbrido; RACI; span of control. | K03 describe la oficina humana; AMP-27/29 no diseñan la estructura. | M1.1-K03 (EXTIENDE); AMP-27 (SE_APOYA_EN); AMP-29 (SE_APOYA_EN); AMP-28 (SE_RELACIONA) | 6 | C6.1, C7.3 | G1.1-PA01 + M1.1-PA01 (V5) |
| M1.1-PA02 | M1.1 | Portafolio de productos-control con owners | Conjunto de controles como productos con owner, métricas, backlog y presupuesto. | HC-036 integra el portafolio sin owner por producto. | HC-036 (PROFUNDIZA); M1.1-K02 (SE_RELACIONA); M1.1-K05 (SE_RELACIONA) | 4 | C1.1, C1.3 | M1.1-PA02 (V5) |
| M1.1-PA03 | M1.1 | Modelo operativo por cadencias y excelencia operacional como requisito del programa | Cadencias, runbooks, SLAs, evidencia y rituales por control; prácticas agnósticas (eo:OP). | K05 advierte el abandono del mantenimiento; nadie formaliza el modelo operativo por control. | M1.1-K05 (PROFUNDIZA); M1.1-K07 (SE_RELACIONA); AMP-27 (SE_APOYA_EN) | 5 | C3.1 | M1.1-PA03 (V5) |
| M1.2-PA01 | M1.2 | FinOps de agentes: presupuesto, costo por tarea y alertas de consumo | Presupuesto de consumo (SCU, créditos, tokens), costo por tarea, forecasting, alertas, optimización y chargeback. | K01/K02 no incluyen costos variables de IA; ningún AMP/HC trata FinOps. | M1.2-K01 (EXTIENDE); M1.2-K02 (EXTIENDE); HC-036 (SE_RELACIONA) | 5 | C6.4, C8.2 | M1.2-PA01 (V5) |
| M1.2-PA02 | M1.2 | Requisitos de IA y agentes en contratos de servicios gestionados | Requisitos, SLAs, KPIs, evidencia, interoperabilidad con agentes propios y salida para MSSP/MDR y plataformas de IA. | K03 es genérico; HC-008 y AMP-12 no bajan al anexo contractual. | M1.2-K03 (EXTIENDE); HC-008 (SE_APOYA_EN); AMP-12 (SE_RELACIONA); M6.2-K08 (SE_RELACIONA) | 3 | C7.2 | M1.2-PA03 (V5) |
| M1.2-PA03 | M1.2 | Itinerario de desarrollo: de analista a PO-GAC | Itinerario de competencias, evidencias y evaluación del rol; autoevaluación y plan individual. | HC-037 y AMP-29 no definen el itinerario de carrera hacia la gestión de agentes. | HC-037 (INSTANCIA_DE); AMP-29 (OPERACIONALIZA); M1.2-K07 (SE_RELACIONA); M1.2-K08 (SE_RELACIONA) | 3 | C7.1 | M1.2-PA04 (V5) |
| M2.1-PA01 | M2.1 | Registro de agentes como clase de activo | Registro de agentes propios y de terceros con dueño, criticidad, datos, dependencias y estado de ciclo de vida. | K03 inventaría activos clásicos; AMP-33 solo la credencial. | M2.1-K03 (EXTIENDE); AMP-33 (SE_RELACIONA); AMP-28 (SE_RELACIONA) | 4 | C5.3 | M2.1-PA01 (V5) |
| M2.2-PA01 | M2.2 | Permisos de humanos y agentes en el control: RBAC unificado, roles y conectores | Permisos mínimos por tarea para personas (Unified RBAC, roles de Exchange/Defender) y agentes (conectores, API permissions). | K03 y AMP-34/36 fijan principios; falta la práctica tarea→rol→permiso. | M2.2-K03 (INSTANCIA_DE); AMP-34 (OPERACIONALIZA); AMP-36 (OPERACIONALIZA); M2.2-K04 (SE_RELACIONA) | 4 | C2.6, C5.2 | Nuevo V6 |
| M3.1-PA01 | M3.1 | Arquitectura de referencia del SOC agéntico con control plane | Capas: señales, XDR/SIEM, orquestación, agentes, control plane de gobierno, humanos; límites de confianza. | AMP-35/39 y HC-019 no dibujan el control plane como capa explícita. | AMP-35 (PROFUNDIZA); AMP-39 (SE_APOYA_EN); HC-019 (SE_APOYA_EN); M3.1-K03 (SE_RELACIONA) | 5 | C3.1, C4.2 | M3.1-PA01 (V5) |
| M3.1-PA02 | M3.1 | Arquitectura de protección del dominio Zero Trust (instancias: correo y colaboración · detección y respuesta unificada · endpoints · identidades · datos) | Capas de protección y flujo de correo; autenticación (SPF/DKIM/DMARC/ARC); cobertura de Teams/SharePoint/OneDrive; remediación post-entrega. | Ningún concepto de los 331 trata la arquitectura del dominio productividad. | M3.1-K08 (INSTANCIA_DE); M3.1-K04 (SE_RELACIONA) | 5 | C2.1 | M3.1-PA03 (V5) |
| M3.2-PA01 | M3.2 | El control como producto: objetivo → configuración → evidencia | Cadena que une objetivo de control, configuración concreta y evidencia de operación efectiva, con owner continuo. | K01/K09 y HC-018 sin ownership continuo ni cadena explícita. | M3.2-K01 (INSTANCIA_DE); M3.2-K09 (SE_RELACIONA); HC-018 (SE_APOYA_EN) | 4 | C1.1, C2.4 | M3.2-PA01 (V5) |
| M3.2-PA02 | M3.2 | Catálogo de controles de gobierno y gestión de agentes (AGC) | 24 controles mapeados a AI RMF, ISO 42001 y OWASP con implementación Microsoft y base agnóstica. | No existe catálogo de controles para agentes. | M3.2-K03 (INSTANCIA_DE); HC-010 (OPERACIONALIZA); AMP-06 (OPERACIONALIZA); AMP-38 (SE_RELACIONA) | 5 | C5.1, C5.5 | M3.2-PA02 (V5) |
| M3.2-PA03 | M3.2 | Evaluación de calidad de agentes: datasets dorados, regresión y criterios de aceptación | Evaluación funcional con datasets dorados, regresión por versión y criterios de aceptación. | AMP-37/38 cubren lo adversarial y las pruebas de controles autónomos; falta la calidad funcional. | AMP-37 (COMPLEMENTA); AMP-38 (COMPLEMENTA); M3.2-K04 (INSTANCIA_DE); M4.1-K08 (SE_RELACIONA) | 4 | C4.5 | M3.2-PA03 (V5) |
| M4.1-PA01 | M4.1 | Modelo operativo del producto-control por cadencias (instancias: Defender for Office 365 · Defender XDR · Defender for Endpoint · Defender for Identity/Entra · Purview · Sentinel · Defender for Cloud) | Tareas diarias, semanales, mensuales, trimestrales y por evento con persona, evidencia y KPI; versión agnóstica (eo:OP). | K01/K02 describen el SOC en general; no existe el modelo operativo de un control concreto. | M4.1-K01 (INSTANCIA_DE); M4.1-K02 (INSTANCIA_DE); M1.1-K05 (SE_RELACIONA); AMP-39 (SE_RELACIONA) | 6 | C3.1, C2.2 | M4.1-PA01 (V5) |
| M4.1-PA02 | M4.1 | Gestión de incidentes y alertas en Defender XDR | Cola de incidentes, prioridad, investigación, AIR, Action center, clasificación y resolución. | K06 y M5.1-K07 son genéricos. | M4.1-K06 (INSTANCIA_DE); M5.1-K07 (SE_RELACIONA); HC-019 (SE_RELACIONA) | 5 | C2.2, C3.2 | M4.1-PA02 (V5) |
| M4.1-PA03 | M4.1 | Gestión de la calidad de detección del dominio: FP/FN, tuning, listas, indicadores y supresiones (instancias: MDO · XDR · MDE · MDI/ID Protection · Purview DLP · Sentinel) | Submissions, Tenant Allow/Block List, cuarentena, mensajes reportados; causa raíz; precision/recall. | No existe la gestión de calidad de detección de un control. | M4.1-K02 (PROFUNDIZA); HC-027 (SE_APOYA_EN) | 4 | C2.3 | M4.1-PA03 (V5) |
| M4.1-PA04 | M4.1 | Hunting y detecciones personalizadas | Threat Explorer, Advanced Hunting (KQL), Threat analytics, consultas compartidas, Threat trackers y detecciones personalizadas. | K07/K03 son conceptuales; falta la práctica con KQL y detection-as-code. | M4.1-K07 (INSTANCIA_DE); M4.1-K03 (SE_RELACIONA) | 4 | C2.2, C3.4 | M4.1-PA04 (V5) |
| M4.1-PA05 | M4.1 | Observabilidad de la flota de agentes: telemetría, trazas y tableros | Telemetría, trazas, tableros y alertas de comportamiento de agentes integrados a la detección del SOC. | HC-018 y AMP-45/46 no cubren la observabilidad operativa de agentes como flota. | HC-018 (PROFUNDIZA); AMP-46 (SE_APOYA_EN); AMP-45 (SE_RELACIONA); M4.1-K02 (SE_RELACIONA) | 4 | C6.3 | M4.1-PA06 (V5) |
| M4.1-PA06 | M4.1 | Gestión del desempeño de agentes: revisión periódica y drift | Revisión de calidad por muestreo, drift, retroalimentación y decisión de mantener/ajustar/pausar/retirar. | AMP-39/26 no cubren la gestión de desempeño de trabajadores no humanos. | AMP-39 (PROFUNDIZA); AMP-26 (SE_APOYA_EN); AMP-40 (SE_RELACIONA) | 4 | C6.2 | M4.1-PA07 (V5) |
| M4.2-PA01 | M4.2 | Amenazas del dominio Zero Trust (instancias: correo y colaboración · cross-domain · endpoints · identidades · datos) | Phishing, BEC, malware, QR phishing, campañas, abuso de colaboración; Campaign Views, Threat analytics, simulaciones. | Ningún concepto trata las amenazas del dominio productividad. | M4.2-K06 (INSTANCIA_DE); M4.2-K10 (SE_RELACIONA); HC-016 (SE_RELACIONA) | 5 | C2.2 | M4.2-PA01 (V5) |
| M4.2-PA02 | M4.2 | Catálogos de amenazas a sistemas agénticos aplicados a la flota | OWASP Agentic/LLM, MITRE ATLAS y CSA aplicados a los agentes del control: amenaza → agente → control. | AMP-41/42 desarrollan dos amenazas; no hay uso sistemático de los catálogos. | AMP-41 (SE_APOYA_EN); AMP-42 (SE_APOYA_EN); M6.2-K04 (PROFUNDIZA); HC-032 (SE_RELACIONA) | 5 | C4.6, C5.1 | G2.1-PA03 + M4.2-PA02 (V5) |
| M5.1-PA01 | M5.1 | Playbooks de incidentes de correo con roles humano/agente | Phishing, BEC y malware entregado: pasos, ejecutor (humano, AIR, agente) y evidencia. | K07 y HC-019 no distinguen ejecutores por paso en un dominio concreto. | M5.1-K07 (INSTANCIA_DE); HC-019 (SE_APOYA_EN); AMP-40 (SE_APOYA_EN) | 4 | C3.2, C3.5 | M5.1-PA01 (V5) |
| M5.2-PA01 | M5.2 | Ejecución de respuesta en correo: AIR, acciones manuales y acciones de agentes con aprobación | Contención y erradicación en correo; supervisión de acciones propuestas por agentes; límites de lote. | K01/K07 genéricos; AMP-38 pide probar controles autónomos. | M5.2-K01 (INSTANCIA_DE); M5.2-K07 (SE_RELACIONA); AMP-38 (SE_RELACIONA) | 4 | C2.2, C3.5 | M5.2-PA01 (V5) |
| M5.2-PA02 | M5.2 | Mejora gobernada de agentes: del post-mortem al ChangeSet con regresión | Causa raíz de errores de agentes convertida en cambios versionados con aprobación y regresión. | K05 y HC-035 conectan post-mortem con políticas; falta el ciclo de cambio versionado del agente. | M5.2-K05 (EXTIENDE); HC-035 (OPERACIONALIZA); AMP-45 (SE_APOYA_EN); HC-034 (SE_RELACIONA) | 4 | C6.6, C6.5 | M5.2-PA02 (V5) |
| M6.1-PA01 | M6.1 | Operación degradada del SOC sin agentes ni modelos | Modo manual, prioridades, dependencias de plataforma y pruebas de operación sin IA. | AMP-47/48 cubren recuperación y dependencias; falta el runbook degradado. | AMP-48 (OPERACIONALIZA); AMP-47 (SE_APOYA_EN); M6.1-K10 (SE_RELACIONA); HC-023 (SE_RELACIONA) | 4 | C6.5 | M6.1-PA01 (V5) |
| M6.2-PA01 | M6.2 | Plataformas y rutas de construcción de agentes y responsabilidad compartida en IA | Tres rutas (Security Copilot custom; Copilot Studio + MCP/Security Copilot; Foundry Agent Service + MCP); qué asegura la plataforma y qué el owner. | K07 y AMP-51 no comparan plataformas ni dan criterios de ruta. | M6.2-K07 (INSTANCIA_DE); M6.2-K04 (SE_RELACIONA); AMP-51 (SE_RELACIONA); AMP-50 (SE_RELACIONA) | 5 | C4.3, C4.4, C7.2 | M6.2-PA01 (V5) |
| M6.2-PA02 | M6.2 | AgentOps / ALM de agentes | Entornos, soluciones, versionado, pruebas, despliegue y ChangeSets gobernados para agentes. | K03 y HC-034/AMP-21 no cubren el ciclo de vida de desarrollo de agentes. | M6.2-K03 (EXTIENDE); HC-034 (OPERACIONALIZA); AMP-21 (SE_APOYA_EN) | 4 | C6.6, C4.3 | M6.2-PA02 (V5) |
| M6.2-PA03 | M6.2 | Bases multiplataforma, multicloud y multimodelo | Estándares abiertos que hacen portable el modelo: OpenTelemetry, OpenAPI/MCP, identidades de carga de trabajo, evidencia portable, prácticas eo:OP. | HC-023/AMP-48 advierten sobre concentración; falta la base técnica de portabilidad. | G2.1-K07 (EXTIENDE); HC-023 (SE_RELACIONA); AMP-48 (SE_RELACIONA); M6.2-K07 (SE_RELACIONA) | 4 | C4.1, C6.3 | M6.2-PA04 (V5) |

## 2. Lente PO-GAC sobre conceptos existentes (91, 175 h)
| ID | Unidad | Concepto | h | Lectura PO-GAC | Instrumento | Competencias |
|---|---|---|---|---|---|---|
| AMP-03 | G1.1 | Autoridad frente a responsabilidad | 3 | Cuando actúa un agente, el PO-GAC responde: autoridad delegada explícita, responsabilidad no transferible. | Declaración de accountability del PO-GAC | C8.4, C5.5 |
| AMP-02 | G1.1 | Sesgos y límites cognitivos | 1 | Sesgo de automatización en el triaje asistido: diseñar la verificación humana. | Checklist de verificación en aprobaciones L2 | C8.4 |
| G1.2-K05 | G1.2 | Casos de Negocio | 1 | El caso de negocio de agentes compara alternativas bajo supuestos explícitos. | Insumo de G1.2-PA01 | C8.2 |
| G1.2-K06 | G1.2 | ROI en Seguridad | 1 | ROSI con beneficios medidos, no estimados. | KPI-18 | C8.2 |
| AMP-04 | G1.2 | Estrategia adaptativa | 2 | Hoja de ruta de adopción agéntica como cartera de opciones con hitos. | Hoja de ruta a 12 meses | C1.3, C8.2 |
| AMP-06 | G1.2 | Gobierno de la IA | 2 | Quién usa agentes, con qué datos, autonomía y evidencia: base de la política. | Principios de la política de agentes | C5.1 |
| AMP-07 | G2.1 | NIST CSF 2.0 Govern | 2 | Resultados GV del control como filas de la grilla de ownership. | Fila GV de la grilla | C1.2 |
| AMP-08 | G2.1 | Referencias informativas y no equivalencia | 1 | Los mapeos AGC↔AI RMF↔ISO 42001 son referencias informativas. | Columna 'nivel de correspondencia' | C5.1 |
| G2.2-K09 | G2.2 | Excepciones | 1 | Excepciones del control con evaluación de riesgo, autoridad y vigencia. | Registro de excepciones | C1.5 |
| AMP-09 | G2.2 | Policy-as-code | 2 | Presets y baselines como política expresada en configuración verificable. | Baseline versionado | C1.5 |
| AMP-10 | G2.2 | Gobierno de excepciones automatizadas | 2 | Entradas de bloqueo/permiso con caducidad automática. | Reglas de caducidad de TABL | C1.5 |
| AMP-12 | G3.1 | Responsabilidad por agentes | 3 | Dueño identificable, límites contractuales y trazabilidad para agentes propios y del MDR. | Cláusulas tipo | C8.4, C7.2 |
| AMP-11 | G3.1 | Soberanía de datos | 1 | Ubicación, jurisdicción y claves de los datos que leen los agentes. | Checklist de soberanía por agente | C5.4 |
| G3.2-K02 | G3.2 | Aseguramiento Continuo | 1 | Señales recurrentes sobre diseño y operación del control. | — | C2.4 |
| G3.2-K06 | G3.2 | Gestión de Evidencia | 1 | Qué registros respaldan cada afirmación del control y de los agentes. | Esquema de evidencia | C5.6 |
| AMP-13 | G3.2 | Evidencia continua | 2 | Evidencia generada por los propios controles: alcance, integridad y responsable. | Inventario de evidencias continuas | C5.6, C2.4 |
| AMP-46 | M5.2 | Trazabilidad de decisiones autónomas | 3 | Registrar qué vio, qué decidió y con qué autoridad actuó cada agente. | Esquema de evidencia de un agente | C5.6 |
| HC-005 | G3.2 | Cumplimiento continuo orientado a resultados | 2 | Cumplir una vez, reportar muchas: evidencias mapeadas a ISO 27001/42001. | Mapa de 5 evidencias | C5.1, C5.6 |
| G4.1-K03 | G4.1 | Tres Líneas de Defensa | 1 | Separar gestión, supervisión y aseguramiento de la flota. | Insumo de G4.1-PA01 | C5.5 |
| G4.1-K08 | G4.1 | Roles y Responsabilidades | 1 | Propietario, custodio, ejecutor, asesor y autoridad de aceptación por agente. | RACI | C5.5 |
| HC-009 | G4.1 | Gobierno de identidades no humanas | 3 | Autorización, ciclo de vida, privilegios y accountability de identidades no humanas. | Inventario de NHI con sponsor | C5.2 |
| AMP-15 | G4.1 | Riesgo sistémico | 1 | Riesgo sistémico por dependencias compartidas. | Fila en el registro de riesgos | C8.1 |
| AMP-17 | G4.2 | Autoridad delegada | 3 | Delegar autoridad en agentes es una decisión de apetito. | Declaración de apetito de autonomía | C8.1, C3.5 |
| AMP-18 | G4.2 | Límites de autonomía | 3 | Acciones permitidas, umbrales, aprobaciones y detención: escala L0–L4. | Escala L0–L4 + árbol de decisión | C3.5 |
| HC-010 | G4.2 | Autonomía delegada y límites de acción | 3 | Capacidad ≠ permiso ≠ delegación ≠ ejecución: clasificar cada tarea. | Matriz tarea→nivel→agente | C3.5 |
| G4.2-K09 | G4.2 | Métricas de Apetito | 1 | KRIs con definiciones, umbrales y calidad de datos. | — | C8.1 |
| G4.2-K10 | G4.2 | Aceptación Formal | 1 | Aceptación explícita por autoridad competente: antecedente del ATO. | — | C5.5 |
| G5.1-K05 | G5.1 | Monitorización Continua | 2 | Actualizar el riesgo cuando cambian amenazas, agentes, modelos o plataforma. | Tablero de KRIs | C6.3, C8.1 |
| AMP-20 | G5.1 | Riesgo de modelos de IA | 2 | Error, deriva, sesgo, manipulación y dependencia de proveedor de los modelos. | Evaluación de riesgo de modelos | C8.1 |
| AMP-19 | G5.1 | Calidad epistemológica de evidencia | 1 | Observación, inferencia y supuesto en la evidencia que producen los agentes. | Etiquetado de evidencias | C5.6 |
| AMP-22 | G5.2 | Aceptación de riesgo de agentes | 4 | Aceptar el riesgo residual de un agente exige autoridad, condiciones, caducidad y monitoreo. | Plantilla de expediente ATO | C5.5 |
| HC-028 | G5.2 | Gestión de excepciones y compensaciones | 3 | HITL, límites, sandbox y kill switch como compensaciones del residual. | Diseño de compensatorios | C5.5, C4.6 |
| AMP-21 | G5.2 | Decisiones reversibles | 2 | Preferir y probar la reversibilidad: criterio para otorgar L3. | Prueba de rollback | C3.5 |
| G6.1-K05 | G6.1 | Reportes Factuales | 1 | Separar hechos e inferencias en el reporte. | — | C8.3 |
| AMP-23 | G6.1 | Narrativa de riesgo basada en evidencia | 2 | Narrativa de riesgo con hechos verificables, incertidumbre y decisiones pendientes. | Reporte trimestral | C8.3 |
| AMP-24 | G6.1 | Comunicación de incertidumbre | 1 | Rangos, supuestos y disparadores de revisión en el reporte. | — | C8.3 |
| HC-020 | G6.1 | Respuesta y comunicación bajo incertidumbre | 2 | Comunicar incidentes causados o agravados por agentes bajo incertidumbre. | Simulación de comunicación | C8.3, C6.5 |
| HC-027 | G6.1 | Métricas que no engañan | 2 | Indicadores que distinguen actividad, uso y efectividad. | Revisión crítica de los 20 KPIs | C1.4, C8.3 |
| AMP-25 | G6.2 | Ética de autonomía | 2 | Proporcionalidad, transparencia y derecho a revisión humana. | Análisis de 3 dilemas | C8.4 |
| AMP-26 | G6.2 | Supervisión humana efectiva | 3 | Supervisar es efectivo solo con información, tiempo, autoridad y capacidad de detener. | Condiciones de supervisión por agente | C8.4, C6.2 |
| G6.2-K06 | G6.2 | Efectividad Programa | 1 | Efectividad del programa incluyendo la flota. | — | C3.3 |
| M1.1-K05 | M1.1 | Ciclo de Vida | 2 | Se celebra el despliegue y se abandona el mantenimiento: el modelo operativo es el antídoto. | Insumo de M1.1-PA03 | C3.1 |
| AMP-27 | M1.1 | CISO-OS | 2 | CISO-OS: datos, decisiones, agentes y evidencia como servicio continuo. | Mapa de componentes del CISO-OS | C6.1 |
| AMP-28 | M1.1 | Orquestación de agentes | 2 | Orquestar varios agentes: roles, límites, traspasos y trazabilidad. | Diagrama de traspasos | C4.2, C6.1 |
| HC-036 | M1.1 | Portafolio de controles y capacidades | 2 | Portafolio de controles: inversión, selección, adopción, pruebas, sostenibilidad. | Insumo de M1.1-PA02 | C1.3 |
| M1.2-K01 | M1.2 | Presupuesto | 1 | Presupuesto con costos variables de IA. | Insumo de M1.2-PA01 | C6.4 |
| M1.2-K03 | M1.2 | RFI/RFP | 1 | RFI/RFP con requisitos de IA. | Insumo de M1.2-PA02 | C7.2 |
| AMP-29 | M1.2 | Competencias humanas y agentes | 3 | Equipo híbrido: menos tareas de primer nivel, más supervisión y ajuste. | Plan de transición de un analista | C7.1 |
| AMP-30 | M1.2 | Adopción responsable de IA | 2 | Adopción responsable como gestión del cambio. | Plan de adopción de los 3 primeros agentes | C7.1, C8.2 |
| HC-037 | M1.2 | Alineación entre competencias y decisiones | 1 | Competencias y decisiones alineadas: base del itinerario. | — | C7.1 |
| M2.1-K03 | M2.1 | Inventario | 1 | Inventario de activos extendido a agentes. | Insumo de M2.1-PA01 | C5.3 |
| AMP-31 | M2.1 | DSPM | 2 | DSPM for AI: dónde está el dato sensible que alcanzan los agentes. | Informe DSPM del alcance de la flota | C5.4 |
| AMP-32 | M2.1 | Gobierno de datos para RAG | 3 | Los agentes heredan permisos y calidad de los datos que recuperan. | Política de datos de los agentes | C5.4 |
| HC-011 | M2.1 | Seguridad de datos en la IA empresarial | 2 | Flujo de información sensible en una aplicación de IA. | Diagrama de flujo de datos de AG-02 | C5.4 |
| M2.2-K03 | M2.2 | Autorización | 2 | Un agente autenticado no debe invocar herramientas con facultades mayores que su ficha. | Insumo de M2.2-PA01 | C5.2, C2.6 |
| AMP-33 | M2.2 | Identidades no humanas | 3 | Inventario, dueño, credenciales gestionadas y caducidad de identidades no humanas. | Inventario de NHI del control | C5.2 |
| AMP-34 | M2.2 | Identidad y autorización de agentes | 4 | Identidad propia, permisos mínimos, acceso condicional y ciclo de vida. | Ficha de identidad + recertificación | C5.2 |
| HC-015 | M2.2 | Gobierno y operación de Zero Trust | 2 | Zero Trust para el dominio productividad. | Insumo de G2.1-PA01 | C1.2 |
| M3.1-K03 | M3.1 | Zero Trust (Arquitectura) | 1 | Zero Trust como arquitectura del control. | — | C1.2 |
| AMP-35 | M3.1 | Arquitectura de sistemas agénticos | 3 | Separar planificación, herramientas, datos y permisos; patrones agénticos. | Decisión de patrón para la flota | C4.1, C4.2 |
| AMP-36 | M3.1 | Límites de herramientas y permisos | 3 | Herramientas y conectores definen lo que el agente puede tocar: allowlist, aprobación, registro. | Allowlist de conectores por agente | C2.6, C4.6 |
| M3.2-K03 | M3.2 | Selección y Adaptación | 1 | Selección y adaptación de controles para agentes. | Insumo de M3.2-PA02 | C2.4 |
| AMP-37 | M3.2 | Evaluación adversarial de agentes | 3 | Pruebas adversariales con criterios de aceptación antes de producción. | Informe de red teaming de AG-03 | C4.5, C4.6 |
| AMP-38 | M3.2 | Pruebas de controles autónomos | 2 | Controles que actúan solos se prueban en escenarios de falla y con rollback. | Prueba de AIR y de AG-10 | C4.5 |
| HC-018 | M3.2 | Observabilidad y aseguramiento de controles | 2 | Telemetría, evaluación y evidencia para sostener afirmaciones de efectividad. | Insumo de M4.1-PA05 | C6.3, C2.4 |
| M4.1-K05 | M4.1 | SOAR | 1 | SOAR determinista como antecedente de los agentes. | — | C3.5 |
| M4.1-K08 | M4.1 | IA en SecOps | 2 | Evaluar un asistente de triaje con escenarios de error, aprobación humana y trazabilidad. | Protocolo de evaluación de AG-01 | C4.5, C3.5 |
| AMP-39 | M4.1 | SOC agéntico | 3 | Agentes que priorizan, investigan y proponen; personas que supervisan y deciden. | Redistribución del runbook | C3.5, C6.2 |
| AMP-40 | M4.1 | Human-in-the-loop | 3 | HITL por riesgo: aprobación previa, auditoría posterior o nunca delegar. | Matriz tarea→nivel→gate | C3.5 |
| HC-019 | M4.1 | SOC agéntico con supervisión humana | 3 | XDR, SOAR, IA y decisiones de contención gobernadas. | Caso integrador del capstone | C3.5, C2.2 |
| M4.2-K02 | M4.2 | Modelado de Amenazas | 2 | Modelar un agente con RAG, APIs y autoridad delegada. | Insumo de HC-032 | C4.6 |
| HC-032 | M4.2 | Evaluación adversarial de sistemas autónomos | 3 | Threat modeling, pentesting, IA y autorización integrados sobre un agente. | Modelo de amenazas de AG-03 | C4.6 |
| AMP-41 | M4.2 | Prompt injection | 2 | El contenido del correo que lee un agente puede ser una orden. | Pruebas de inyección sobre AG-01/AG-02 | C4.6 |
| AMP-42 | M4.2 | Envenenamiento de datos y modelos | 1 | Integridad de knowledge sources y datos de recuperación. | Control de procedencia de fuentes | C4.6 |
| M5.1-K07 | M5.1 | Playbooks | 1 | Playbooks con ejecutores humanos y automatizados. | Insumo de M5.1-PA01 | C3.2 |
| AMP-43 | M5.1 | Tabletop de incidentes con agentes | 3 | Tabletop donde el agente es víctima o vector. | Playbook 'agente comprometido' + tabletop | C6.5 |
| AMP-44 | M5.1 | Kill switch y escalamiento | 2 | Kill switch probado y ruta de escalamiento. | Prueba trimestral del kill switch | C6.5 |
| M5.2-K05 | M5.2 | Post-Mortem | 1 | Post-mortem de fallos de agentes. | Insumo de M5.2-PA02 | C6.6 |
| AMP-45 | M5.2 | Forense de agentes | 2 | Reconstruir instrucciones, herramientas, datos y decisiones del agente. | Requisitos de telemetría forense | C5.6, C6.5 |
| HC-035 | M5.2 | Aprendizaje desde incidentes hasta políticas | 2 | Del post-mortem a la política y al cambio gobernado. | Insumo de M5.2-PA02 | C6.6 |
| M6.1-K10 | M6.1 | Dependencias | 1 | Dependencias de la operación respecto de plataformas de IA. | — | C6.5 |
| AMP-47 | M6.1 | Recuperación de servicios de IA | 2 | Recuperar un agente incluye modelos, índices, instrucciones, conectores e identidades. | Plan de recuperación de la flota | C6.5 |
| AMP-48 | M6.1 | Dependencias de modelos | 2 | Dependencia de un modelo o proveedor: mapa y alternativas. | Mapa de dependencias de modelos | C6.5 |
| HC-023 | M6.1 | Riesgo de concentración tecnológica | 1 | Concentración tecnológica como riesgo estratégico de la flota. | — | C6.5 |
| M6.2-K04 | M6.2 | Seguridad IA | 2 | Proteger modelos, datos, herramientas, agentes y procesos. | Insumo de M4.2-PA02 | C4.6 |
| M6.2-K06 | M6.2 | Shadow AI | 1 | Shadow AI: agentes del SOC fuera del registro. | Regla de detección de agentes no registrados | C5.3 |
| M6.2-K07 | M6.2 | Responsabilidad Compartida | 1 | Responsabilidad compartida con el proveedor de la plataforma. | Insumo de M6.2-PA01 | C7.2 |
| M6.2-K08 | M6.2 | Riesgo Terceros (TPRM) | 1 | TPRM durante selección, operación, cambios y salida de proveedores de IA. | Insumo de M1.2-PA02 | C7.2 |
| AMP-49 | M6.2 | Supply chain de modelos | 2 | Procedencia, licencias, integridad y evaluación de modelos y componentes. | AI BOM de la flota | C7.2 |
| AMP-50 | M6.2 | Seguridad de herramientas y conectores | 3 | Conectores y MCP servers: inventario, autenticación, permisos mínimos, monitoreo. | Inventario de conectores/MCP aprobados | C7.2, C4.6 |
| AMP-51 | M6.2 | Postura de IA en nube | 2 | Postura de IA en nube: modelos, endpoints y configuraciones riesgosas. | Informe AI-SPM del alcance | C4.4 |

## 3. PA retirados o fusionados respecto de V5
| PA V5 | Tratamiento V6 |
|---|---|
| G1.1-PA01 (V5) | Fusionado en M1.1-PA01 |
| G1.1-PA03 (V5) | Cubierto por AMP-03 |
| G1.2-PA02 (V5) | Cubierto por AMP-04 |
| G2.1-PA03 (V5) | Fusionado en M4.2-PA02 |
| G2.1-PA04 (V5) | Fusionado en G2.1-PA01 |
| G3.1-PA02 (V5) | Cubierto por AMP-11 |
| G3.2-PA01 (V5) | Cubierto por AMP-13 |
| G3.2-PA03 (V5) | Cubierto por HC-005 |
| G4.2-PA01 (V5) | Cubierto por AMP-17/18 |
| G5.1-PA01 (V5) | Cubierto por AMP-20 |
| G5.1-PA02 (V5) | Cubierto por AMP-19 |
| G5.2-PA01 (V5) | Cubierto por AMP-22 |
| G5.2-PA02 (V5) | Cubierto por HC-028 |
| G6.1-PA02 (V5) | Cubierto por AMP-23/24 |
| G6.2-PA01 (V5) | Cubierto por AMP-25 |
| G6.2-PA02 (V5) | Cubierto por AMP-26 |
| M1.2-PA02 (V5) | Cubierto por AMP-30 |
| M2.1-PA02 (V5) | Cubierto por AMP-31/32 |
| M2.2-PA01 (V5) | Cubierto por AMP-33 |
| M2.2-PA02 (V5) | Cubierto por AMP-34 |
| M2.2-PA03 (V5) | Cubierto por AMP-36 |
| M3.1-PA02 (V5) | Cubierto por AMP-35 |
| M4.1-PA05 (V5) | Cubierto por AMP-40 |
| M4.2-PA03 (V5) | Cubierto por AMP-41/42 |
| M5.1-PA02 (V5) | Cubierto por AMP-43/44 |
| M6.2-PA03 (V5) | Cubierto por AMP-49/50 |

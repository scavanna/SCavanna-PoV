# TheNextCISO GM-24 — Pre-ensayos (archivos de inicialización), lote AMP-02 (V7.1)

> **GM-24 V7.1 · The Next CISO + Sub-plan PO-GAC** · 2026-11-14. Catálogo: 379 conceptos (245 K · 52 AMP · 40 HC · 42 PA), todos con pre-ensayo íntegro y mapeados a 17 marcos (NIST/ISACA/MITRE/OWASP/CIS/CSA). V7.1 = ChangeSet editorial CS-GM24-V7.1-001 (4 títulos generalizados; sin cambio de IDs, cantidad ni mapeo). Plano A (corpus académico). Referencias DD/K4x/R/eo:OP/COE: marco interno.

**Estado:** ideas centrales para desarrollo editorial; IDs curriculares (asignar `ESS-######` desde el registro SQLite). Estructura de los lotes GM-24 + práctica, próximos pasos y relación con la unidad.

## Inventario

| N.º | ID | Tipo | Unidad | Concepto |
|---|---|---|---|---|
| 067 | AMP-25 | AMP | G6.2 | Ética de autonomía |
| 068 | AMP-26 | AMP | G6.2 | Supervisión humana efectiva |
| 069 | AMP-27 | AMP | M1.1 | CISO-OS |
| 070 | AMP-28 | AMP | M1.1 | Orquestación de agentes |
| 071 | AMP-29 | AMP | M1.2 | Competencias humanas y agentes |
| 072 | AMP-30 | AMP | M1.2 | Adopción responsable de IA |
| 073 | AMP-31 | AMP | M2.1 | DSPM |
| 074 | AMP-32 | AMP | M2.1 | Gobierno de datos para RAG |
| 075 | AMP-33 | AMP | M2.2 | Identidades no humanas |
| 076 | AMP-34 | AMP | M2.2 | Identidad y autorización de agentes |
| 077 | AMP-35 | AMP | M3.1 | Arquitectura de sistemas agénticos |
| 078 | AMP-36 | AMP | M3.1 | Límites de herramientas y permisos |
| 079 | AMP-37 | AMP | M3.2 | Evaluación adversarial de agentes |
| 080 | AMP-38 | AMP | M3.2 | Pruebas de controles autónomos |
| 081 | AMP-39 | AMP | M4.1 | SOC agéntico |
| 082 | AMP-40 | AMP | M4.1 | Human-in-the-loop |
| 083 | AMP-41 | AMP | M4.2 | Prompt injection |
| 084 | AMP-42 | AMP | M4.2 | Envenenamiento de datos y modelos |
| 085 | AMP-43 | AMP | M5.1 | Tabletop de incidentes con agentes |
| 086 | AMP-44 | AMP | M5.1 | Kill switch y escalamiento |
| 087 | AMP-45 | AMP | M5.2 | Forense de agentes |
| 088 | AMP-46 | AMP | M5.2 | Trazabilidad de decisiones autónomas |
| 089 | AMP-47 | AMP | M6.1 | Recuperación de servicios de IA |
| 090 | AMP-48 | AMP | M6.1 | Dependencias de modelos |

---

### 067. AMP-25 — Ética de autonomía

**Unidad:** G6.2 Liderazgo Ético y Medición de Efectividad · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 200 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** Delegar decisiones en sistemas autónomos plantea preguntas de proporcionalidad (¿la acción automática es proporcional al riesgo?), transparencia (¿los afectados saben que decidió una máquina?) y derecho a revisión humana (¿pueden pedir que una persona reconsidere?).

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** Delegar decisiones en sistemas autónomos plantea preguntas de proporcionalidad (¿la acción automática es proporcional al riesgo?), transparencia (¿los afectados saben que decidió una máquina?) y derecho a revisión humana (¿pueden pedir que una persona reconsidere?). La tesis es que el CISO debe hacer explícitas esas preguntas para cada agente que actúa sobre personas —por ejemplo, el que remueve correo de un buzón— y documentar las respuestas como parte del gobierno, no de la ética abstracta.

**Tensión y límites.** La tensión es que la ética parece ajena al SOC, donde la urgencia manda. Pero remover un mensaje legítimo, bloquear un remitente o etiquetar a un usuario como riesgoso son decisiones sobre personas. Otra tensión es la transparencia frente a la seguridad: avisar demasiado ayuda al adversario.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: principios de IA responsable, proporcionalidad, derecho a revisión. Implementación: análisis de tres dilemas del SOC (remediación masiva, etiquetado de usuarios riesgosos, bloqueo de dominios legítimos) con decisión documentada; disclosure del uso de agentes (AGC-21).

**Evidencia y evaluación.** Evidencia: análisis de tres dilemas con decisión y justificación; texto de disclosure aprobado. Se evalúa la conexión con los principios y la operabilidad de las decisiones.

**Puentes.** Se apoya en HC-012 (confianza verificable); se relaciona con AMP-26, AMP-02 y G6.2-K05 (ética); sostiene AGC-21.

**Recomendaciones de práctica y ejercitación.**
1. Analizar tres dilemas de automatización del SOC con proporcionalidad, transparencia y revisión.
2. Redactar el texto de disclosure del uso de agentes para los usuarios.
3. Definir el canal de revisión humana para decisiones de agentes sobre personas.

**Próximos pasos.**
- Registrar como AGC-21.
- Incluir en la política de agentes.
- Revisar ante nuevos tipos de acción.

**Relación con los conceptos de la(s) unidad(es) G6.2.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| G6.2-K01 | K | Liderazgo Ético | misma unidad |
| G6.2-K02 | K | Conducta Profesional | misma unidad |
| G6.2-K03 | K | Conflictos Interés | misma unidad |
| G6.2-K04 | K | Debida Diligencia | misma unidad |
| G6.2-K05 | K | Métricas Gobierno | misma unidad |
| G6.2-K06 | K | Efectividad Programa | misma unidad |
| G6.2-K07 | K | Mejora Continua | misma unidad |
| G6.2-K08 | K | Aseguramiento | misma unidad |
| G6.2-K09 | K | Balance Riesgo-Valor | misma unidad |
| G6.2-K10 | K | Rendición Cuentas | misma unidad |
| AMP-26 | AMP | Supervisión humana efectiva | misma unidad |
| HC-006 | HC | Valor de seguridad y medición causal | misma unidad |
| HC-012 | HC | Confianza verificable en decisiones de IA | misma unidad |
| HC-021 | HC | Recuperación como prueba de confianza | misma unidad |
| HC-026 | HC | Ética, cultura y controles internos | misma unidad |
| HC-027 | HC | Métricas que no engañan | misma unidad |
| AMP-52 | AMP | Content safety y riesgos de contenido generado | misma unidad |
| G6.2-PA01 | PA | Métricas de efectividad del gobierno de la flota | misma unidad |

**Pregunta generadora:** ¿Saben los empleados de su organización que un agente puede remover mensajes de su buzón, y a quién pueden reclamar?

---

### 068. AMP-26 — Supervisión humana efectiva

**Unidad:** G6.2 Liderazgo Ético y Medición de Efectividad · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 186 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** La supervisión humana es efectiva solo si quien supervisa tiene información suficiente, tiempo para analizarla, autoridad para intervenir y capacidad real de detener o revertir la acción.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** La supervisión humana es efectiva solo si quien supervisa tiene información suficiente, tiempo para analizarla, autoridad para intervenir y capacidad real de detener o revertir la acción. Una aprobación en dos segundos sobre una propuesta que no se entiende no es supervisión; es ritual. La tesis es que las cuatro condiciones deben diseñarse por agente y medirse: si no se cumplen, el agente no está supervisado aunque alguien apruebe.

**Tensión y límites.** La tensión es la escala: a más agentes y más propuestas, menos tiempo por decisión; la supervisión degenera en aprobación automática humana. El ensayo debe discutir cuántas aprobaciones por hora son compatibles con supervisión real y cómo el muestreo posterior complementa la aprobación previa.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: meaningful human control, factores humanos, diseño de interfaces de decisión. Implementación: condiciones de supervisión por agente (qué información muestra la propuesta, tiempo esperado, quién puede detener, cómo revertir), medición de tiempo por aprobación y tasa de corrección.

**Evidencia y evaluación.** Evidencia: ficha de condiciones de supervisión para tres agentes y medición de dos semanas. Se evalúa la honestidad sobre aprobaciones rituales.

**Puentes.** Se apoya en HC-019; se relaciona con AMP-02, AMP-40 y G6.2-PA01; sostiene AGC-09.

**Recomendaciones de práctica y ejercitación.**
1. Definir las cuatro condiciones de supervisión para AG-01, AG-02 y AG-03.
2. Medir tiempo por aprobación y tasa de corrección durante dos semanas.
3. Rediseñar la propuesta del agente para que la supervisión sea posible.

**Próximos pasos.**
- Convertir las condiciones en requisito de la ficha.
- Alimentar la revisión de desempeño.
- Ajustar autonomía si la supervisión no es real.

**Relación con los conceptos de la(s) unidad(es) G6.2.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| G6.2-K01 | K | Liderazgo Ético | misma unidad |
| G6.2-K02 | K | Conducta Profesional | misma unidad |
| G6.2-K03 | K | Conflictos Interés | misma unidad |
| G6.2-K04 | K | Debida Diligencia | misma unidad |
| G6.2-K05 | K | Métricas Gobierno | misma unidad |
| G6.2-K06 | K | Efectividad Programa | misma unidad |
| G6.2-K07 | K | Mejora Continua | misma unidad |
| G6.2-K08 | K | Aseguramiento | misma unidad |
| G6.2-K09 | K | Balance Riesgo-Valor | misma unidad |
| G6.2-K10 | K | Rendición Cuentas | misma unidad |
| AMP-25 | AMP | Ética de autonomía | misma unidad |
| HC-006 | HC | Valor de seguridad y medición causal | misma unidad |
| HC-012 | HC | Confianza verificable en decisiones de IA | misma unidad |
| HC-021 | HC | Recuperación como prueba de confianza | misma unidad |
| HC-026 | HC | Ética, cultura y controles internos | misma unidad |
| HC-027 | HC | Métricas que no engañan | misma unidad |
| AMP-52 | AMP | Content safety y riesgos de contenido generado | misma unidad |
| G6.2-PA01 | PA | Métricas de efectividad del gobierno de la flota | misma unidad |

**Pregunta generadora:** ¿Cuántos segundos tarda hoy un analista en aprobar una propuesta de su agente, y qué mira en ese tiempo?

---

### 069. AMP-27 — CISO-OS

**Unidad:** M1.1 Desarrollo, Gestión y Operaciones del Programa de Seguridad · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 181 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** Un sistema operativo del CISO integra datos (telemetría, riesgos, evidencias), decisiones (registro, derechos de decisión), agentes (que ejecutan tareas) y evidencia del programa, para gobernar la seguridad como un servicio continuo y no como una sucesión de proyectos.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** Un sistema operativo del CISO integra datos (telemetría, riesgos, evidencias), decisiones (registro, derechos de decisión), agentes (que ejecutan tareas) y evidencia del programa, para gobernar la seguridad como un servicio continuo y no como una sucesión de proyectos. La tesis es que el CISO-OS no es un producto sino una arquitectura de gobierno: define qué datos alimentan qué decisiones, qué agentes operan qué procesos y qué evidencia demuestra que todo funciona.

**Tensión y límites.** La tensión es la tentación de comprar una herramienta y llamarla CISO-OS. Otra tensión es la integración: datos y decisiones viven en sistemas distintos. El ensayo debe mostrar un mapa mínimo de componentes y sus interfaces.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: arquitectura de gobierno, gestión de servicios, sistemas de decisión. Implementación: mapa de componentes del CISO-OS para el control de correo (Defender/Sentinel como datos, registro de decisiones, flota de agentes, Purview/Agent 365 como evidencia) y sus interfaces.

**Evidencia y evaluación.** Evidencia: mapa de componentes con flujos de datos, decisiones y evidencia. Se evalúa la coherencia con el modelo operativo y la flota.

**Puentes.** Extiende M1.1-K03 (oficina del CISO); se relaciona con AMP-28, HC-036 y M1.1-PA01; sostiene G1.1-PA01.

**Recomendaciones de práctica y ejercitación.**
1. Dibujar el mapa de componentes del CISO-OS para el control de correo.
2. Identificar las interfaces inexistentes o manuales.
3. Ubicar a los 15 agentes en el mapa.

**Próximos pasos.**
- Usarlo como base del organigrama híbrido (M1.1-PA01).
- Priorizar las integraciones faltantes.
- Revisar al cambiar la plataforma.

**Relación con los conceptos de la(s) unidad(es) M1.1.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M1.1-K01 | K | Programa de Seguridad | misma unidad |
| M1.1-K02 | K | Alcance y Objetivos | misma unidad |
| M1.1-K03 | K | Oficina del CISO | misma unidad |
| M1.1-K04 | K | Alineación Operativa | misma unidad |
| M1.1-K05 | K | Ciclo de Vida | misma unidad |
| M1.1-K06 | K | Recursos | misma unidad |
| M1.1-K07 | K | Medición Rendimiento | misma unidad |
| M1.1-K08 | K | Interesados (Stakeholders) | misma unidad |
| M1.1-K09 | K | Integración Gobierno | misma unidad |
| M1.1-K10 | K | Mejora Continua | misma unidad |
| AMP-28 | AMP | Orquestación de agentes | misma unidad |
| HC-006 | HC | Valor de seguridad y medición causal | misma unidad |
| HC-027 | HC | Métricas que no engañan | misma unidad |
| HC-035 | HC | Aprendizaje desde incidentes hasta políticas | misma unidad |
| HC-036 | HC | Portafolio de controles y capacidades | misma unidad |
| M1.1-PA01 | PA | Diseño organizativo híbrido: roles, RACI y span of control | misma unidad |
| M1.1-PA02 | PA | Portafolio de productos-control con owners | misma unidad |
| M1.1-PA03 | PA | Modelo operativo por cadencias y excelencia operacional como requisito del programa | misma unidad |

**Pregunta generadora:** Si tuviera que dibujar en una página cómo fluye una señal hasta convertirse en decisión y evidencia en su programa, ¿qué cajas faltarían?

---

### 070. AMP-28 — Orquestación de agentes

**Unidad:** M1.1 Desarrollo, Gestión y Operaciones del Programa de Seguridad · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 187 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** Orquestar varios agentes exige roles, límites, traspasos y trazabilidad: cuando AG-01 deriva a AG-02 y este propone una acción, la autonomía se gobierna en el flujo (quién puede pasarle qué a quién, con qué contexto, bajo qué aprobación) y no solo en cada agente.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** Orquestar varios agentes exige roles, límites, traspasos y trazabilidad: cuando AG-01 deriva a AG-02 y este propone una acción, la autonomía se gobierna en el flujo (quién puede pasarle qué a quién, con qué contexto, bajo qué aprobación) y no solo en cada agente. La tesis es que los traspasos entre agentes son los puntos de mayor riesgo (pérdida de contexto, escalada de privilegios, fallos en cascada) y deben diseñarse como interfaces con contrato.

**Tensión y límites.** La tensión es que la orquestación emergente (agentes que se llaman entre sí) es más poderosa y menos gobernable que la orquestación explícita. Otra tensión es la atribución: en una cadena, ¿quién decidió? El ensayo debe discutir contratos de traspaso y trazas de extremo a extremo.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: patrones de sistemas distribuidos, orquestación vs. coreografía, OWASP ASI07/ASI08. Implementación: diagrama de traspasos de la flota (AG-01→AG-02→humano; AG-03↔AG-11), contrato por traspaso (contexto, permisos, aprobación) y traza correlacionada en Sentinel.

**Evidencia y evaluación.** Evidencia: diagrama de traspasos con contratos y una traza de extremo a extremo. Se evalúa la identificación de puntos de escalada.

**Puentes.** Se apoya en HC-019; se relaciona con AMP-35, AMP-36 y M3.1-PA01; sostiene AGC-06 y AGC-11.

**Recomendaciones de práctica y ejercitación.**
1. Dibujar los traspasos de la flota y escribir el contrato de cada uno.
2. Rastrear una cadena AG-01→AG-02→humano de extremo a extremo en Sentinel.
3. Identificar un punto donde un traspaso podría escalar privilegios.

**Próximos pasos.**
- Incorporar los contratos a las fichas.
- Probar fallos en cascada en el tabletop (AMP-43).
- Revisar al agregar agentes.

**Relación con los conceptos de la(s) unidad(es) M1.1.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M1.1-K01 | K | Programa de Seguridad | misma unidad |
| M1.1-K02 | K | Alcance y Objetivos | misma unidad |
| M1.1-K03 | K | Oficina del CISO | misma unidad |
| M1.1-K04 | K | Alineación Operativa | misma unidad |
| M1.1-K05 | K | Ciclo de Vida | misma unidad |
| M1.1-K06 | K | Recursos | misma unidad |
| M1.1-K07 | K | Medición Rendimiento | misma unidad |
| M1.1-K08 | K | Interesados (Stakeholders) | misma unidad |
| M1.1-K09 | K | Integración Gobierno | misma unidad |
| M1.1-K10 | K | Mejora Continua | misma unidad |
| AMP-27 | AMP | CISO-OS | misma unidad |
| HC-006 | HC | Valor de seguridad y medición causal | misma unidad |
| HC-027 | HC | Métricas que no engañan | misma unidad |
| HC-035 | HC | Aprendizaje desde incidentes hasta políticas | misma unidad |
| HC-036 | HC | Portafolio de controles y capacidades | misma unidad |
| M1.1-PA01 | PA | Diseño organizativo híbrido: roles, RACI y span of control | misma unidad |
| M1.1-PA02 | PA | Portafolio de productos-control con owners | misma unidad |
| M1.1-PA03 | PA | Modelo operativo por cadencias y excelencia operacional como requisito del programa | misma unidad |

**Pregunta generadora:** Cuando un agente le pasa trabajo a otro en su flota, ¿qué contexto viaja, qué permisos cambian y quién lo registra?

---

### 071. AMP-29 — Competencias humanas y agentes

**Unidad:** M1.2 Gestión Financiera, Liderazgo de Equipo y Capacitación · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 179 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** El equipo de seguridad combina personas y agentes: rediseñar roles —menos tareas de primer nivel ejecutadas por personas, más supervisión, ajuste y mejora— es parte del caso de valor y no un efecto colateral.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** El equipo de seguridad combina personas y agentes: rediseñar roles —menos tareas de primer nivel ejecutadas por personas, más supervisión, ajuste y mejora— es parte del caso de valor y no un efecto colateral. La tesis es que el rediseño debe ser explícito (qué deja de hacer cada persona, qué empieza a hacer) y acompañado de desarrollo de competencias; de lo contrario, los agentes se agregan sobre roles viejos y nadie supervisa.

**Tensión y límites.** La tensión es el temor al reemplazo y la pérdida de práctica: si las personas dejan de triar, pierden el criterio necesario para supervisar. El ensayo debe proponer rotación y práctica deliberada como parte del rediseño.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: diseño de puestos, competencias, gestión del cambio. Implementación: plan de transición de un analista hacia el rol PO-GAC (M1.2-PA03) con redistribución del runbook (qué tareas pasan a agentes, cuáles se retienen para mantener criterio).

**Evidencia y evaluación.** Evidencia: plan de transición con antes/después de tareas y competencias a desarrollar. Se evalúa el realismo y la retención de criterio.

**Puentes.** Extiende M1.2-K05 (liderazgo de equipo); se relaciona con AMP-30, HC-037 y M1.1-PA01; sostiene M1.2-PA03.

**Recomendaciones de práctica y ejercitación.**
1. Redistribuir el runbook (31 tareas) entre personas y agentes con criterio de retención de práctica.
2. Redactar el plan de transición de un analista.
3. Definir la rotación que mantiene el criterio humano.

**Próximos pasos.**
- Vincular con el itinerario (M1.2-PA03).
- Medir horas liberadas reales (KPI-18).
- Revisar en la revisión de desempeño de la flota.

**Relación con los conceptos de la(s) unidad(es) M1.2.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M1.2-K01 | K | Presupuesto | misma unidad |
| M1.2-K02 | K | Optimización Recursos | misma unidad |
| M1.2-K03 | K | RFI/RFP | misma unidad |
| M1.2-K04 | K | Liderazgo de Equipo | misma unidad |
| M1.2-K05 | K | Habilidades Técnicas | misma unidad |
| M1.2-K06 | K | Concienciación | misma unidad |
| M1.2-K07 | K | Capacitación | misma unidad |
| M1.2-K08 | K | Gestión Talento | misma unidad |
| M1.2-K09 | K | Efectividad Capacitación | misma unidad |
| M1.2-K10 | K | Ética en Equipo | misma unidad |
| AMP-30 | AMP | Adopción responsable de IA | misma unidad |
| HC-013 | HC | Deuda de seguridad como riesgo de transformación | misma unidad |
| HC-025 | HC | Competencias y resiliencia organizacional | misma unidad |
| HC-026 | HC | Ética, cultura y controles internos | misma unidad |
| HC-036 | HC | Portafolio de controles y capacidades | misma unidad |
| HC-037 | HC | Alineación entre competencias y decisiones | misma unidad |
| M1.2-PA01 | PA | FinOps de agentes: presupuesto, costo por tarea y alertas de consumo | misma unidad |
| M1.2-PA02 | PA | Requisitos de IA y agentes en contratos de servicios gestionados | misma unidad |
| M1.2-PA03 | PA | Itinerario de desarrollo: de analista a PO-GAC | misma unidad |

**Pregunta generadora:** Si sus agentes triaran el 80 % de los incidentes, ¿qué harían sus analistas con ese tiempo y seguirían sabiendo triar dentro de un año?

---

### 072. AMP-30 — Adopción responsable de IA

**Unidad:** M1.2 Gestión Financiera, Liderazgo de Equipo y Capacitación · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 188 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** Adoptar IA de forma responsable es gestionar un cambio: casos de uso con valor demostrable, guardrails antes del despliegue, capacitación de quienes la usan y medición de resultados.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** Adoptar IA de forma responsable es gestionar un cambio: casos de uso con valor demostrable, guardrails antes del despliegue, capacitación de quienes la usan y medición de resultados. La tesis es que la adopción responsable no es una lista de principios sino un plan de cambio con fases, criterios de éxito y mecanismos de corrección, y que el SOC es un buen primer dominio porque sus resultados se miden.

**Tensión y límites.** La tensión es entre la presión por adoptar y el tiempo que exige el cambio bien hecho. Otra tensión es la medición: los beneficios de la IA se estiman fácil y se miden difícil. El ensayo debe exigir métricas de resultado desde el primer caso.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: gestión del cambio, adopción de tecnología, IA responsable. Implementación: plan de adopción de los tres primeros agentes (AG-10, AG-03, AG-05) con guardrails, capacitación del equipo y métricas de resultado (KPI-11, 12, 18).

**Evidencia y evaluación.** Evidencia: plan de adopción con fases y métricas, y primer corte de resultados. Se evalúa que las métricas sean de resultado y no de actividad.

**Puentes.** Extiende M6.2-K06 (Shadow AI); se relaciona con AMP-04, AMP-16 y AMP-29; sostiene la etapa E3.

**Recomendaciones de práctica y ejercitación.**
1. Redactar el plan de adopción de AG-10, AG-03 y AG-05 con guardrails, capacitación y métricas.
2. Definir el criterio de éxito y de abandono de cada uno.
3. Capacitar al equipo en supervisión antes del despliegue.

**Próximos pasos.**
- Medir a los tres meses y decidir.
- Escalar la adopción según resultados.
- Documentar lecciones para la siguiente ola.

**Relación con los conceptos de la(s) unidad(es) M1.2.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M1.2-K01 | K | Presupuesto | misma unidad |
| M1.2-K02 | K | Optimización Recursos | misma unidad |
| M1.2-K03 | K | RFI/RFP | misma unidad |
| M1.2-K04 | K | Liderazgo de Equipo | misma unidad |
| M1.2-K05 | K | Habilidades Técnicas | misma unidad |
| M1.2-K06 | K | Concienciación | misma unidad |
| M1.2-K07 | K | Capacitación | misma unidad |
| M1.2-K08 | K | Gestión Talento | misma unidad |
| M1.2-K09 | K | Efectividad Capacitación | misma unidad |
| M1.2-K10 | K | Ética en Equipo | misma unidad |
| AMP-29 | AMP | Competencias humanas y agentes | misma unidad |
| HC-013 | HC | Deuda de seguridad como riesgo de transformación | misma unidad |
| HC-025 | HC | Competencias y resiliencia organizacional | misma unidad |
| HC-026 | HC | Ética, cultura y controles internos | misma unidad |
| HC-036 | HC | Portafolio de controles y capacidades | misma unidad |
| HC-037 | HC | Alineación entre competencias y decisiones | misma unidad |
| M1.2-PA01 | PA | FinOps de agentes: presupuesto, costo por tarea y alertas de consumo | misma unidad |
| M1.2-PA02 | PA | Requisitos de IA y agentes en contratos de servicios gestionados | misma unidad |
| M1.2-PA03 | PA | Itinerario de desarrollo: de analista a PO-GAC | misma unidad |

**Pregunta generadora:** ¿Qué resultado medible espera del primer agente que despliegue, y cómo sabrá en tres meses si lo logró?

---

### 073. AMP-31 — DSPM

**Unidad:** M2.1 Gestión de Activos y Seguridad del Ciclo de Vida de los Datos · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 180 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** DSPM (Data Security Posture Management) convierte la protección de datos en gestión continua de exposición: dónde está el dato sensible, quién puede acceder y qué remediar primero.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** DSPM (Data Security Posture Management) convierte la protección de datos en gestión continua de exposición: dónde está el dato sensible, quién puede acceder y qué remediar primero. Para una flota de agentes la pregunta se vuelve 'qué dato sensible alcanza cada agente a través de sus fuentes y conectores'. La tesis es que el owner debe conocer la exposición de datos de la flota antes de ampliar su autonomía.

**Tensión y límites.** La tensión es la sobrecompartición heredada: los agentes exponen lo que los permisos ya permitían pero nadie veía. Corregirla es un proyecto de datos, no de agentes. El ensayo debe mostrar cómo priorizar la remediación por lo que los agentes alcanzan.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: DSPM, clasificación, gestión de exposición. Implementación: informe DSPM for AI de Purview sobre el alcance de la flota (sitios, buzones, tablas), priorización de remediación y restricción de fuentes de conocimiento.

**Evidencia y evaluación.** Evidencia: informe de exposición de datos de la flota con remediaciones priorizadas. Se evalúa la cobertura del alcance real de los agentes.

**Puentes.** Se apoya en HC-011 (flujo de información sensible); se relaciona con AMP-32 y M2.1-PA01; sostiene AGC-07.

**Recomendaciones de práctica y ejercitación.**
1. Ejecutar DSPM for AI sobre el alcance de la flota y listar exposiciones.
2. Priorizar remediaciones por agente y nivel de autonomía.
3. Restringir fuentes de conocimiento de AG-02 y AG-14.

**Próximos pasos.**
- Conectar con la política de datos (AMP-32).
- Incluir en el expediente ATO.
- Repetir trimestralmente.

**Relación con los conceptos de la(s) unidad(es) M2.1.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M2.1-K01 | K | Identificación Activos | misma unidad |
| M2.1-K02 | K | Clasificación | misma unidad |
| M2.1-K03 | K | Inventario | misma unidad |
| M2.1-K04 | K | Ciclo de Vida Datos | misma unidad |
| M2.1-K05 | K | Seguridad Reposo/Tránsito | misma unidad |
| M2.1-K06 | K | Retención/Destrucción | misma unidad |
| M2.1-K07 | K | Gobernanza Datos | misma unidad |
| M2.1-K08 | K | Activos Críticos | misma unidad |
| M2.1-K09 | K | Auditoría Activos | misma unidad |
| M2.1-K10 | K | Riesgos de Datos | misma unidad |
| AMP-32 | AMP | Gobierno de datos para RAG | misma unidad |
| HC-011 | HC | Seguridad de datos en la IA empresarial | misma unidad |
| HC-014 | HC | Arquitectura de riesgo empresarial | misma unidad |
| HC-016 | HC | Superficie de ataque contextualizada | misma unidad |
| HC-024 | HC | Cumplimiento y privacidad por diseño | misma unidad |
| HC-033 | HC | Seguridad y soberanía de datos distribuidos | misma unidad |
| M2.1-PA01 | PA | Registro de agentes como clase de activo | misma unidad |

**Pregunta generadora:** ¿Qué dato sensible podría leer hoy su agente de investigación que ningún analista debería ver?

---

### 074. AMP-32 — Gobierno de datos para RAG

**Unidad:** M2.1 Gestión de Activos y Seguridad del Ciclo de Vida de los Datos · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 180 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** En RAG (generación aumentada por recuperación) la IA hereda los permisos y la calidad de los datos que recupera: sin clasificación, permisos correctos y control de sobrecompartición, el agente expone lo que nadie debía ver y razona sobre lo que nadie validó.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** En RAG (generación aumentada por recuperación) la IA hereda los permisos y la calidad de los datos que recupera: sin clasificación, permisos correctos y control de sobrecompartición, el agente expone lo que nadie debía ver y razona sobre lo que nadie validó. La tesis es que el gobierno de datos para RAG tiene tres controles mínimos —fuentes aprobadas, permisos verificados, calidad y procedencia— y que el owner los aplica por agente.

**Tensión y límites.** La tensión es que los agentes son más útiles cuanto más datos alcanzan; cada restricción cuesta capacidad. Otra tensión es la calidad: una fuente desactualizada produce respuestas seguras y erróneas. El ensayo debe argumentar fuentes pocas y curadas.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: gobierno de datos, data lineage, mínimo privilegio aplicado a datos. Implementación: política de datos de los agentes del control (fuentes aprobadas en SharePoint/Dataverse, etiquetas de sensibilidad, DLP para agentes, revisión de procedencia de knowledge sources).

**Evidencia y evaluación.** Evidencia: política de datos aplicada y verificación de fuentes de tres agentes. Se evalúa que ninguna fuente no aprobada esté conectada.

**Puentes.** Se apoya en HC-011; se relaciona con AMP-31, AMP-42 y M2.1-PA01; sostiene AGC-07.

**Recomendaciones de práctica y ejercitación.**
1. Redactar la política de datos de los agentes (fuentes, permisos, calidad).
2. Verificar las fuentes de conocimiento de AG-01, AG-02 y AG-14.
3. Configurar DLP de Purview para agentes y probarlo.

**Próximos pasos.**
- Registrar como AGC-07.
- Revisar fuentes en cada cambio de agente.
- Conectar con la procedencia (AMP-42).

**Relación con los conceptos de la(s) unidad(es) M2.1.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M2.1-K01 | K | Identificación Activos | misma unidad |
| M2.1-K02 | K | Clasificación | misma unidad |
| M2.1-K03 | K | Inventario | misma unidad |
| M2.1-K04 | K | Ciclo de Vida Datos | misma unidad |
| M2.1-K05 | K | Seguridad Reposo/Tránsito | misma unidad |
| M2.1-K06 | K | Retención/Destrucción | misma unidad |
| M2.1-K07 | K | Gobernanza Datos | misma unidad |
| M2.1-K08 | K | Activos Críticos | misma unidad |
| M2.1-K09 | K | Auditoría Activos | misma unidad |
| M2.1-K10 | K | Riesgos de Datos | misma unidad |
| AMP-31 | AMP | DSPM | misma unidad |
| HC-011 | HC | Seguridad de datos en la IA empresarial | misma unidad |
| HC-014 | HC | Arquitectura de riesgo empresarial | misma unidad |
| HC-016 | HC | Superficie de ataque contextualizada | misma unidad |
| HC-024 | HC | Cumplimiento y privacidad por diseño | misma unidad |
| HC-033 | HC | Seguridad y soberanía de datos distribuidos | misma unidad |
| M2.1-PA01 | PA | Registro de agentes como clase de activo | misma unidad |

**Pregunta generadora:** ¿Quién aprobó cada fuente de conocimiento conectada a sus agentes, y cuándo se revisó su calidad por última vez?

---

### 075. AMP-33 — Identidades no humanas

**Unidad:** M2.2 Gestión de Identidad y Acceso (IAM) y Principios de Confianza Cero · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Referencias por ID (V7-C09):** OWASP Top 10 for Non-Human Identities (2025); ASI03 (2026 v2.01) · **Extensión:** 189 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** Las identidades no humanas —cuentas de servicio, principales, claves, tokens y ahora agentes— ya superan en número a las humanas y son la superficie menos vigilada: sin inventario, dueño, credenciales gestionadas y caducidad, cada una es una puerta sin cerradura.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** Las identidades no humanas —cuentas de servicio, principales, claves, tokens y ahora agentes— ya superan en número a las humanas y son la superficie menos vigilada: sin inventario, dueño, credenciales gestionadas y caducidad, cada una es una puerta sin cerradura. La tesis es que las identidades de agentes deben entrar al mismo régimen que las demás NHI (inventario, dueño, rotación, caducidad, revisión) y que la plataforma debe crearlas automáticamente para que ninguna nazca huérfana.

**Tensión y límites.** La tensión es la proliferación: crear un agente crea una identidad; sin automatización el inventario queda atrás desde el día uno. Otra tensión es la herencia: agentes antiguos usan app registrations con permisos amplios.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: gestión de identidades de carga de trabajo, OWASP NHI Top 10, rotación de credenciales. Implementación: inventario de NHI del control con Entra Agent ID (creación automática en Copilot Studio), sponsors, caducidad y migración de app registrations previas; regla de agentes sin dueño en Agent 365.

**Evidencia y evaluación.** Evidencia: inventario de identidades no humanas del control con dueño y caducidad; cero identidades huérfanas. Se evalúa la cobertura.

**Puentes.** Se apoya en HC-009; se relaciona con AMP-34 y M2.1-PA01; sostiene AGC-05, AGC-18 y AGC-19.

**Recomendaciones de práctica y ejercitación.**
1. Inventariar las identidades no humanas del control (app registrations, principales, agentes).
2. Asignar dueño y caducidad; detectar huérfanas.
3. Migrar un agente de app registration a Entra Agent ID.

**Próximos pasos.**
- Configurar la regla de agentes sin dueño (Agent 365).
- Programar la recertificación (AGC-18).
- Conectar con la matriz de permisos (M2.2-PA01).

**Relación con los conceptos de la(s) unidad(es) M2.2.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M2.2-K01 | K | Estrategias IAM | misma unidad |
| M2.2-K02 | K | Autenticación | misma unidad |
| M2.2-K03 | K | Autorización | misma unidad |
| M2.2-K04 | K | PAM (Privilegiados) | misma unidad |
| M2.2-K05 | K | Zero Trust | misma unidad |
| M2.2-K06 | K | ZTNA | misma unidad |
| M2.2-K07 | K | Ciclo Vida Identidad | misma unidad |
| M2.2-K08 | K | Auditoría IAM | misma unidad |
| M2.2-K09 | K | Federación | misma unidad |
| M2.2-K10 | K | Contexto de Acceso | misma unidad |
| AMP-34 | AMP | Identidad y autorización de agentes | misma unidad |
| HC-009 | HC | Gobierno de identidades no humanas | misma unidad |
| HC-010 | HC | Autonomía delegada y límites de acción | misma unidad |
| HC-015 | HC | Gobierno y operación de Zero Trust | misma unidad |
| HC-032 | HC | Evaluación adversarial de sistemas autónomos | misma unidad |
| HC-038 | HC | Aseguramiento de la arquitectura Zero Trust | misma unidad |
| M2.2-PA01 | PA | Permisos de humanos y agentes en el control: RBAC unificado, roles y conectores | misma unidad |

**Pregunta generadora:** ¿Cuántas identidades no humanas con acceso a su correo corporativo existen hoy, y cuántas tienen un dueño que lo sepa?

---

### 076. AMP-34 — Identidad y autorización de agentes

**Unidad:** M2.2 Gestión de Identidad y Acceso (IAM) y Principios de Confianza Cero · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Referencias por ID (V7-C09):** OWASP NHI Top 10 (2025); ASI03; CSA AICM IAM-19 · **Extensión:** 177 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** Cada agente necesita identidad propia, permisos mínimos, acceso condicional y ciclo de vida: es la base de un agente protegido.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** Cada agente necesita identidad propia, permisos mínimos, acceso condicional y ciclo de vida: es la base de un agente protegido. Identidad propia permite atribuir y revocar; permisos mínimos acotan el daño; acceso condicional aplica contexto (ubicación, riesgo); ciclo de vida garantiza que el agente muera cuando deja de ser útil. La tesis es que ninguna de las cuatro piezas es opcional para agentes L2 o superiores.

**Tensión y límites.** La tensión es la comodidad de reutilizar la identidad del constructor y la granularidad limitada de permisos de conectores. El ensayo debe mostrar cómo compensar (límites de herramientas, aprobación) cuando el permiso exacto no existe.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: identidad de carga de trabajo, least privilege, acceso basado en contexto, SP 800-207. Implementación: Entra Agent ID (blueprint, agent identity, agent user), API permissions por tool, Conditional Access para agentes, caducidad y recertificación en Entra ID Governance.

**Evidencia y evaluación.** Evidencia: ficha de identidad de un agente con las cuatro piezas verificadas en el tenant. Se evalúa la coherencia con la ficha de agente.

**Puentes.** Extiende M2.2-K03 (autorización); se relaciona con AMP-33, AMP-36 y M2.2-PA01; sostiene AGC-05, AGC-06.

**Recomendaciones de práctica y ejercitación.**
1. Provisionar la identidad de AG-03 con las cuatro piezas y documentarla.
2. Aplicar una política de acceso condicional a una identidad de agente y probarla.
3. Definir la caducidad y el flujo de recertificación.

**Próximos pasos.**
- Replicar para los 15 agentes.
- Registrar como AGC-05/06.
- Revisar permisos en cada cambio de tool.

**Relación con los conceptos de la(s) unidad(es) M2.2.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M2.2-K01 | K | Estrategias IAM | misma unidad |
| M2.2-K02 | K | Autenticación | misma unidad |
| M2.2-K03 | K | Autorización | misma unidad |
| M2.2-K04 | K | PAM (Privilegiados) | misma unidad |
| M2.2-K05 | K | Zero Trust | misma unidad |
| M2.2-K06 | K | ZTNA | misma unidad |
| M2.2-K07 | K | Ciclo Vida Identidad | misma unidad |
| M2.2-K08 | K | Auditoría IAM | misma unidad |
| M2.2-K09 | K | Federación | misma unidad |
| M2.2-K10 | K | Contexto de Acceso | misma unidad |
| AMP-33 | AMP | Identidades no humanas | misma unidad |
| HC-009 | HC | Gobierno de identidades no humanas | misma unidad |
| HC-010 | HC | Autonomía delegada y límites de acción | misma unidad |
| HC-015 | HC | Gobierno y operación de Zero Trust | misma unidad |
| HC-032 | HC | Evaluación adversarial de sistemas autónomos | misma unidad |
| HC-038 | HC | Aseguramiento de la arquitectura Zero Trust | misma unidad |
| M2.2-PA01 | PA | Permisos de humanos y agentes en el control: RBAC unificado, roles y conectores | misma unidad |

**Pregunta generadora:** Si revocara ahora la identidad de su agente más activo, ¿qué dejaría de funcionar y cuánto tardaría en saberlo?

---

### 077. AMP-35 — Arquitectura de sistemas agénticos

**Unidad:** M3.1 Arquitectura de Seguridad, Ingeniería y Diseño (Incl. Zero Trust) · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 192 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** Diseñar sistemas agénticos seguros implica separar planificación (el modelo decide qué hacer), herramientas (lo que puede ejecutar), datos (lo que puede leer) y permisos (lo que la identidad autoriza), con puntos de control y observabilidad desde el diseño.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** Diseñar sistemas agénticos seguros implica separar planificación (el modelo decide qué hacer), herramientas (lo que puede ejecutar), datos (lo que puede leer) y permisos (lo que la identidad autoriza), con puntos de control y observabilidad desde el diseño. La tesis es que esa separación —y no la confianza en el modelo— es lo que hace gobernable a un agente: cada capa se puede acotar, probar y observar por separado.

**Tensión y límites.** La tensión es que las plataformas low-code mezclan las capas para facilitar la construcción; separarlas exige disciplina del constructor. Otra tensión es el rendimiento: más puntos de control, más latencia. El ensayo debe proponer la separación mínima por nivel de autonomía.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: arquitectura de referencia de agentes, patrones (único, multiagente, orquestador), MAESTRO. Implementación: decisión de patrón para la flota (agentes especializados con orquestación explícita vía analista), separación de capas en Copilot Studio (instrucciones / tools / knowledge / Agent ID), puntos de control (Approvals) y observabilidad (Sentinel).

**Evidencia y evaluación.** Evidencia: decisión de arquitectura documentada con las cuatro capas por agente. Se evalúa la claridad de los límites entre capas.

**Puentes.** Extiende M6.2-K04 (seguridad IA); se relaciona con AMP-28, AMP-36 y M3.1-PA01; sostiene AGC-06 y AGC-08.

**Recomendaciones de práctica y ejercitación.**
1. Documentar las cuatro capas para AG-02 y verificar sus límites en la plataforma.
2. Elegir y justificar el patrón de orquestación de la flota.
3. Ubicar los puntos de control y observabilidad en el diseño.

**Próximos pasos.**
- Alimentar la arquitectura de referencia (M3.1-PA01).
- Probar la separación con pruebas adversariales (AMP-37).
- Revisar al cambiar de ruta de construcción.

**Relación con los conceptos de la(s) unidad(es) M3.1.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M3.1-K01 | K | Arquitectura de Seguridad | misma unidad |
| M3.1-K02 | K | Ingeniería de Seguridad | misma unidad |
| M3.1-K03 | K | Zero Trust (Arquitectura) | misma unidad |
| M3.1-K04 | K | Diseño Seguro (SbD) | misma unidad |
| M3.1-K05 | K | TOGAF y Seguridad | misma unidad |
| M3.1-K06 | K | ZTNA (Acceso) | misma unidad |
| M3.1-K07 | K | Microsegmentación | misma unidad |
| M3.1-K08 | K | Defensa en Profundidad | misma unidad |
| M3.1-K09 | K | Mínimo Privilegio (Arquitectura) | misma unidad |
| M3.1-K10 | K | Resiliencia (Diseño) | misma unidad |
| AMP-36 | AMP | Límites de herramientas y permisos | misma unidad |
| HC-002 | HC | Apetito de riesgo convertido en arquitectura | misma unidad |
| HC-010 | HC | Autonomía delegada y límites de acción | misma unidad |
| HC-013 | HC | Deuda de seguridad como riesgo de transformación | misma unidad |
| HC-014 | HC | Arquitectura de riesgo empresarial | misma unidad |
| HC-015 | HC | Gobierno y operación de Zero Trust | misma unidad |
| HC-023 | HC | Riesgo de concentración tecnológica | misma unidad |
| HC-030 | HC | Seguridad industrial y continuidad de negocio | misma unidad |
| HC-034 | HC | Decisiones reversibles y riesgo de transición | misma unidad |
| HC-038 | HC | Aseguramiento de la arquitectura Zero Trust | misma unidad |
| HC-040 | HC | Homeostasis organizacional de seguridad | misma unidad |
| M3.1-K11 | K | Arquitectura empresarial y arquitectura de seguridad de la información | misma unidad |
| M3.1-K12 | K | Seguridad física, ambiental y mantenimiento como dependencias del control | misma unidad |
| M3.1-PA01 | PA | Arquitectura de referencia del SOC agéntico con control plane | misma unidad |
| M3.1-PA02 | PA | Arquitectura de protección del dominio Zero Trust (instancias: correo y colaboración · detección y respuesta unificada · endpoints · identidades · datos) | misma unidad |

**Pregunta generadora:** En su agente de remediación, ¿qué impide que el modelo decida invocar una herramienta que su ficha no autoriza?

---

### 078. AMP-36 — Límites de herramientas y permisos

**Unidad:** M3.1 Arquitectura de Seguridad, Ingeniería y Diseño (Incl. Zero Trust) · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 203 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** Las herramientas y conectores definen lo que un agente puede hacer en el mundo: acotar alcances (allowlist por agente), aprobar acciones de alto impacto y registrar cada invocación son los tres controles que convierten una capacidad técnica en una capacidad gobernada.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** Las herramientas y conectores definen lo que un agente puede hacer en el mundo: acotar alcances (allowlist por agente), aprobar acciones de alto impacto y registrar cada invocación son los tres controles que convierten una capacidad técnica en una capacidad gobernada. La tesis es que la lista de herramientas de un agente es parte de su ficha y de su autorización, y que agregar una herramienta es un cambio de riesgo.

**Tensión y límites.** La tensión es la utilidad: cada herramienta nueva hace al agente más útil y más peligroso. Otra tensión es la opacidad de los conectores: un conector 'Graph' puede permitir mucho más de lo que el nombre sugiere. El ensayo debe exigir permisos declarados por operación.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: least privilege aplicado a capacidades, allowlists, auditoría de invocaciones, OWASP ASI02. Implementación: allowlist de conectores por agente en Power Platform (políticas de datos), permisos de API por tool (anexos de agentes), Approvals para acciones de escritura, registro de invocaciones en Sentinel.

**Evidencia y evaluación.** Evidencia: allowlist y permisos por tool para tres agentes, verificados; registro de invocaciones de una semana. Se evalúa que ningún agente tenga herramientas fuera de su ficha.

**Puentes.** Extiende M3.1-K09 (mínimo privilegio en arquitectura); se relaciona con AMP-34, AMP-50 y M2.2-PA01; sostiene AGC-06 y AGC-11.

**Recomendaciones de práctica y ejercitación.**
1. Construir la allowlist de tools por agente desde los anexos y aplicarla en Power Platform.
2. Declarar permisos por operación para cada tool de escritura.
3. Revisar una semana de invocaciones y detectar anomalías.

**Próximos pasos.**
- Registrar como AGC-06.
- Incorporar al pipeline de cambios (agregar tool = ChangeSet).
- Vincular con la matriz amenaza→agente (M4.2-PA02).

**Relación con los conceptos de la(s) unidad(es) M3.1.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M3.1-K01 | K | Arquitectura de Seguridad | misma unidad |
| M3.1-K02 | K | Ingeniería de Seguridad | misma unidad |
| M3.1-K03 | K | Zero Trust (Arquitectura) | misma unidad |
| M3.1-K04 | K | Diseño Seguro (SbD) | misma unidad |
| M3.1-K05 | K | TOGAF y Seguridad | misma unidad |
| M3.1-K06 | K | ZTNA (Acceso) | misma unidad |
| M3.1-K07 | K | Microsegmentación | misma unidad |
| M3.1-K08 | K | Defensa en Profundidad | misma unidad |
| M3.1-K09 | K | Mínimo Privilegio (Arquitectura) | misma unidad |
| M3.1-K10 | K | Resiliencia (Diseño) | misma unidad |
| AMP-35 | AMP | Arquitectura de sistemas agénticos | misma unidad |
| HC-002 | HC | Apetito de riesgo convertido en arquitectura | misma unidad |
| HC-010 | HC | Autonomía delegada y límites de acción | misma unidad |
| HC-013 | HC | Deuda de seguridad como riesgo de transformación | misma unidad |
| HC-014 | HC | Arquitectura de riesgo empresarial | misma unidad |
| HC-015 | HC | Gobierno y operación de Zero Trust | misma unidad |
| HC-023 | HC | Riesgo de concentración tecnológica | misma unidad |
| HC-030 | HC | Seguridad industrial y continuidad de negocio | misma unidad |
| HC-034 | HC | Decisiones reversibles y riesgo de transición | misma unidad |
| HC-038 | HC | Aseguramiento de la arquitectura Zero Trust | misma unidad |
| HC-040 | HC | Homeostasis organizacional de seguridad | misma unidad |
| M3.1-K11 | K | Arquitectura empresarial y arquitectura de seguridad de la información | misma unidad |
| M3.1-K12 | K | Seguridad física, ambiental y mantenimiento como dependencias del control | misma unidad |
| M3.1-PA01 | PA | Arquitectura de referencia del SOC agéntico con control plane | misma unidad |
| M3.1-PA02 | PA | Arquitectura de protección del dominio Zero Trust (instancias: correo y colaboración · detección y respuesta unificada · endpoints · identidades · datos) | misma unidad |

**Pregunta generadora:** ¿Qué podría hacer hoy el conector más amplio de su flota si el agente que lo usa fuera manipulado?

---

### 079. AMP-37 — Evaluación adversarial de agentes

**Unidad:** M3.2 Selección, Implementación y Evaluación de Controles · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 194 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** Antes de producción, un agente debe resistir pruebas adversariales —inyección de instrucciones, abuso de herramientas, fuga de datos, envenenamiento de contexto— con criterios de aceptación explícitos.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** Antes de producción, un agente debe resistir pruebas adversariales —inyección de instrucciones, abuso de herramientas, fuga de datos, envenenamiento de contexto— con criterios de aceptación explícitos. La tesis es que la evaluación adversarial es el 'pentest' del agente, que debe repetirse en cada versión y que sus resultados son parte del expediente de autorización.

**Tensión y límites.** La tensión es el costo y la cobertura: los ataques evolucionan y ninguna prueba es completa. Otra tensión es la no determinación: un agente puede resistir diez veces y caer en la undécima; los criterios deben expresarse como tasas. El ensayo debe proponer el conjunto mínimo de pruebas por nivel de autonomía.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: red teaming de IA, OWASP ASI/LLM Top 10, MITRE ATLAS, AI RMF MEASURE. Implementación: pruebas de inyección indirecta por correo sobre AG-01/AG-02, abuso de herramientas sobre AG-03, fuga sobre AG-14; herramientas de evaluación de Foundry y AI Red Teaming Agent/PyRIT como referencia; criterios de aceptación.

**Evidencia y evaluación.** Evidencia: informe de red teaming de un agente con casos, tasas y criterios. Se evalúa la cobertura de las amenazas relevantes al agente.

**Puentes.** Se apoya en HC-032 (evaluación adversarial integrada); se complementa con M3.2-PA03 (calidad); sostiene AGC-12; se relaciona con AMP-41/42.

**Recomendaciones de práctica y ejercitación.**
1. Diseñar el conjunto mínimo de pruebas adversariales por nivel de autonomía.
2. Ejecutar pruebas de inyección indirecta sobre AG-01 y AG-02 en el entorno de prueba.
3. Fijar criterios de aceptación como tasas y documentar el informe.

**Próximos pasos.**
- Incluir el informe en el expediente ATO.
- Repetir en cada versión (MDO-Q04).
- Actualizar con nuevas versiones de OWASP/ATLAS.

**Relación con los conceptos de la(s) unidad(es) M3.2.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M3.2-K01 | K | Controles de Seguridad | misma unidad |
| M3.2-K02 | K | NIST SP 800-53 | misma unidad |
| M3.2-K03 | K | Selección y Adaptación | misma unidad |
| M3.2-K04 | K | Evaluación (Assess) | misma unidad |
| M3.2-K05 | K | Implementación | misma unidad |
| M3.2-K06 | K | Pentesting | misma unidad |
| M3.2-K07 | K | Controles Compensatorios | misma unidad |
| M3.2-K08 | K | Familias de Controles | misma unidad |
| M3.2-K09 | K | Pruebas de Efectividad | misma unidad |
| M3.2-K10 | K | POA&M | misma unidad |
| AMP-38 | AMP | Pruebas de controles autónomos | misma unidad |
| HC-002 | HC | Apetito de riesgo convertido en arquitectura | misma unidad |
| HC-003 | HC | Riesgo residual y aceptación verificable | misma unidad |
| HC-004 | HC | Política como código gobernado | misma unidad |
| HC-005 | HC | Cumplimiento continuo orientado a resultados | misma unidad |
| HC-015 | HC | Gobierno y operación de Zero Trust | misma unidad |
| HC-018 | HC | Observabilidad y aseguramiento de controles | misma unidad |
| HC-028 | HC | Gestión de excepciones y compensaciones | misma unidad |
| HC-031 | HC | Seguridad del software y confianza en componentes | misma unidad |
| HC-032 | HC | Evaluación adversarial de sistemas autónomos | misma unidad |
| HC-034 | HC | Decisiones reversibles y riesgo de transición | misma unidad |
| HC-036 | HC | Portafolio de controles y capacidades | misma unidad |
| HC-038 | HC | Aseguramiento de la arquitectura Zero Trust | misma unidad |
| AMP-52 | AMP | Content safety y riesgos de contenido generado | misma unidad |
| M3.2-PA01 | PA | El control como producto: objetivo → configuración → evidencia | misma unidad |
| M3.2-PA02 | PA | Catálogo de controles de gobierno y gestión de agentes (AGC) | misma unidad |
| M3.2-PA03 | PA | Evaluación de calidad de agentes: datasets dorados, regresión y criterios de aceptación | misma unidad |

**Pregunta generadora:** Si un atacante escribiera un correo diseñado para que su agente de triaje lo clasifique como legítimo, ¿lo lograría hoy?

---

### 080. AMP-38 — Pruebas de controles autónomos

**Unidad:** M3.2 Selección, Implementación y Evaluación de Controles · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 194 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** Los controles que actúan solos —bloqueo, contención, remediación automática— deben probarse en escenarios de falla y con rollback antes de confiarles decisiones: qué pasa si el control actúa sobre un falso positivo masivo, si la fuente de datos falla, si la acción no se puede revertir.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** Los controles que actúan solos —bloqueo, contención, remediación automática— deben probarse en escenarios de falla y con rollback antes de confiarles decisiones: qué pasa si el control actúa sobre un falso positivo masivo, si la fuente de datos falla, si la acción no se puede revertir. La tesis es que la prueba de controles autónomos es una disciplina distinta de la prueba de detección: se prueba el daño que el control puede causar.

**Tensión y límites.** La tensión es que los controles autónomos nativos (AIR, ZAP) vienen activados y probados por el fabricante; el owner tiende a no probarlos. Pero su configuración local y sus agentes propios cambian el comportamiento. El ensayo debe mostrar cómo probar en escenarios de falla sin romper producción.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: pruebas de resiliencia, ingeniería del caos aplicada a controles, rollback. Implementación: probar AIR y ZAP con falsos positivos controlados en el entorno de prueba, probar AG-10 en modo corrección con un cambio inducido, medir rollback.

**Evidencia y evaluación.** Evidencia: informe de pruebas de dos controles autónomos en escenarios de falla con rollback medido. Se evalúa la identificación de modos de daño.

**Puentes.** Extiende M3.2-K09 (pruebas de efectividad); se relaciona con AMP-21, AMP-44 y M5.2-PA01; sostiene AGC-12.

**Recomendaciones de práctica y ejercitación.**
1. Diseñar escenarios de falla para AIR/ZAP y para AG-10.
2. Ejecutarlos en el entorno de prueba y medir el rollback.
3. Documentar modos de daño y límites recomendados.

**Próximos pasos.**
- Incorporar límites de lote a las fichas.
- Programar pruebas periódicas (MDO-Q04).
- Conectar con el tabletop (AMP-43).

**Relación con los conceptos de la(s) unidad(es) M3.2.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M3.2-K01 | K | Controles de Seguridad | misma unidad |
| M3.2-K02 | K | NIST SP 800-53 | misma unidad |
| M3.2-K03 | K | Selección y Adaptación | misma unidad |
| M3.2-K04 | K | Evaluación (Assess) | misma unidad |
| M3.2-K05 | K | Implementación | misma unidad |
| M3.2-K06 | K | Pentesting | misma unidad |
| M3.2-K07 | K | Controles Compensatorios | misma unidad |
| M3.2-K08 | K | Familias de Controles | misma unidad |
| M3.2-K09 | K | Pruebas de Efectividad | misma unidad |
| M3.2-K10 | K | POA&M | misma unidad |
| AMP-37 | AMP | Evaluación adversarial de agentes | misma unidad |
| HC-002 | HC | Apetito de riesgo convertido en arquitectura | misma unidad |
| HC-003 | HC | Riesgo residual y aceptación verificable | misma unidad |
| HC-004 | HC | Política como código gobernado | misma unidad |
| HC-005 | HC | Cumplimiento continuo orientado a resultados | misma unidad |
| HC-015 | HC | Gobierno y operación de Zero Trust | misma unidad |
| HC-018 | HC | Observabilidad y aseguramiento de controles | misma unidad |
| HC-028 | HC | Gestión de excepciones y compensaciones | misma unidad |
| HC-031 | HC | Seguridad del software y confianza en componentes | misma unidad |
| HC-032 | HC | Evaluación adversarial de sistemas autónomos | misma unidad |
| HC-034 | HC | Decisiones reversibles y riesgo de transición | misma unidad |
| HC-036 | HC | Portafolio de controles y capacidades | misma unidad |
| HC-038 | HC | Aseguramiento de la arquitectura Zero Trust | misma unidad |
| AMP-52 | AMP | Content safety y riesgos de contenido generado | misma unidad |
| M3.2-PA01 | PA | El control como producto: objetivo → configuración → evidencia | misma unidad |
| M3.2-PA02 | PA | Catálogo de controles de gobierno y gestión de agentes (AGC) | misma unidad |
| M3.2-PA03 | PA | Evaluación de calidad de agentes: datasets dorados, regresión y criterios de aceptación | misma unidad |

**Pregunta generadora:** Si la investigación automatizada de su tenant removiera mil mensajes legítimos por un veredicto erróneo, ¿cuánto tardaría en revertirlo?

---

### 081. AMP-39 — SOC agéntico

**Unidad:** M4.1 Operaciones de Seguridad, Monitorización e Inteligencia · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 197 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** El SOC agéntico redistribuye el trabajo: agentes que priorizan, investigan y proponen respuesta; personas que supervisan, ajustan y deciden; todo medido por tiempo de respuesta, calidad de decisión y costo.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** El SOC agéntico redistribuye el trabajo: agentes que priorizan, investigan y proponen respuesta; personas que supervisan, ajustan y deciden; todo medido por tiempo de respuesta, calidad de decisión y costo. La tesis es que el SOC agéntico no es un SOC con herramientas de IA sino un modelo operativo distinto, donde la unidad de trabajo humano pasa de 'resolver el incidente' a 'gobernar a quien lo resuelve', y donde las métricas deben cambiar en consecuencia.

**Tensión y límites.** La tensión es la pérdida de criterio humano (si nadie tria, nadie sabe triar) y la dependencia de la plataforma (si los agentes caen, el SOC cae). Otra tensión es la medición: las métricas clásicas (MTTR) mejoran mientras la calidad puede degradarse sin que nadie lo vea.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: modelos operativos de SOC, teoría de la supervisión, métricas de calidad de decisión. Implementación: redistribución del runbook (31 tareas) entre agentes y personas con niveles L0–L3, métricas de la flota (KPI-11/12/13) y de retención de criterio (rotación), operación degradada (M6.1-PA01).

**Evidencia y evaluación.** Evidencia: runbook redistribuido con métricas y plan de retención de criterio. Se evalúa la coherencia con el apetito de autonomía.

**Puentes.** Se apoya en HC-019; se relaciona con AMP-29, AMP-40 y M4.1-PA01; sostiene M4.1-PA06.

**Recomendaciones de práctica y ejercitación.**
1. Redistribuir las 31 tareas del modelo operativo entre agentes y personas.
2. Definir las métricas de calidad de decisión además de las de tiempo.
3. Diseñar la rotación que mantiene el criterio humano.

**Próximos pasos.**
- Operar un trimestre y medir (E5).
- Ajustar niveles de autonomía según resultados.
- Vincular con la operación degradada.

**Relación con los conceptos de la(s) unidad(es) M4.1.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M4.1-K01 | K | SOC Moderno | misma unidad |
| M4.1-K02 | K | Monitorización Continua | misma unidad |
| M4.1-K03 | K | Threat Intelligence (CTI) | misma unidad |
| M4.1-K04 | K | SIEM | misma unidad |
| M4.1-K05 | K | SOAR | misma unidad |
| M4.1-K06 | K | XDR | misma unidad |
| M4.1-K07 | K | Threat Hunting | misma unidad |
| M4.1-K08 | K | IA en SecOps | misma unidad |
| M4.1-K09 | K | Ciclo Vida Inteligencia | misma unidad |
| M4.1-K10 | K | TTPs | misma unidad |
| AMP-40 | AMP | Human-in-the-loop | misma unidad |
| HC-001 | HC | Gobierno de decisiones basadas en evidencia | misma unidad |
| HC-005 | HC | Cumplimiento continuo orientado a resultados | misma unidad |
| HC-010 | HC | Autonomía delegada y límites de acción | misma unidad |
| HC-012 | HC | Confianza verificable en decisiones de IA | misma unidad |
| HC-017 | HC | Inteligencia que modifica decisiones | misma unidad |
| HC-018 | HC | Observabilidad y aseguramiento de controles | misma unidad |
| HC-019 | HC | SOC agéntico con supervisión humana | misma unidad |
| HC-040 | HC | Homeostasis organizacional de seguridad | misma unidad |
| M4.1-K11 | K | Deception y señuelos como control detectivo | misma unidad |
| M4.1-PA01 | PA | Modelo operativo del producto-control por cadencias (instancias: Defender for Office 365 · Defender XDR · Defender for Endpoint · Defender for Identity/Entra · Purview · Sentinel · Defender for Cloud) | misma unidad |
| M4.1-PA02 | PA | Gestión de incidentes y alertas en Defender XDR | misma unidad |
| M4.1-PA03 | PA | Gestión de la calidad de detección del dominio: FP/FN, tuning, listas, indicadores y supresiones (instancias: MDO · XDR · MDE · MDI/ID Protection · Purview DLP · Sentinel) | misma unidad |
| M4.1-PA04 | PA | Hunting y detecciones personalizadas | misma unidad |
| M4.1-PA05 | PA | Observabilidad de la flota de agentes: telemetría, trazas y tableros | misma unidad |
| M4.1-PA06 | PA | Gestión del desempeño de agentes: revisión periódica y drift | misma unidad |

**Pregunta generadora:** En su SOC agéntico, ¿qué medirá para saber que la calidad de las decisiones no se degradó mientras el tiempo de respuesta mejoraba?

---

### 082. AMP-40 — Human-in-the-loop

**Unidad:** M4.1 Operaciones de Seguridad, Monitorización e Inteligencia · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 180 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** Human-in-the-loop se define por riesgo, no por principio: qué acciones requieren aprobación previa (irreversibles o de alto impacto), cuáles se auditan después por muestreo (reversibles, bajo impacto) y cuáles nunca se delegan (decisiones de juicio sobre personas, aceptación de riesgo).

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** Human-in-the-loop se define por riesgo, no por principio: qué acciones requieren aprobación previa (irreversibles o de alto impacto), cuáles se auditan después por muestreo (reversibles, bajo impacto) y cuáles nunca se delegan (decisiones de juicio sobre personas, aceptación de riesgo). La tesis es que la matriz tarea → nivel → gate es el instrumento que convierte HITL en configuración y que debe revisarse con la calidad medida del agente.

**Tensión y límites.** La tensión es que 'aprobar todo' anula el valor y 'auditar todo después' acepta el daño antes de detectarlo. Otra tensión es la fatiga de aprobación (AMP-26). El ensayo debe mostrar cómo mover tareas de aprobación previa a auditoría posterior con evidencia.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: meaningful human control, niveles de automatización, gestión de riesgo operacional. Implementación: matriz tarea→nivel→gate para las 31 tareas; Approvals para L2; muestreo desde Sentinel para L3; lista de 'nunca delegar'.

**Evidencia y evaluación.** Evidencia: matriz completa con justificación por tarea y criterio de promoción L2→L3. Se evalúa la coherencia con reversibilidad y calidad medida.

**Puentes.** Se apoya en HC-019 y HC-010; se relaciona con AMP-18, AMP-26 y AMP-02; sostiene AGC-09 y M5.1-PA01.

**Recomendaciones de práctica y ejercitación.**
1. Completar la matriz tarea→nivel→gate para las 31 tareas.
2. Redactar la lista de 'nunca delegar' y justificarla.
3. Definir el criterio de promoción L2→L3 (KPI-11/12).

**Próximos pasos.**
- Configurar Approvals y muestreo según la matriz.
- Revisar la matriz en cada revisión de desempeño.
- Incluirla en la política de agentes.

**Relación con los conceptos de la(s) unidad(es) M4.1.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M4.1-K01 | K | SOC Moderno | misma unidad |
| M4.1-K02 | K | Monitorización Continua | misma unidad |
| M4.1-K03 | K | Threat Intelligence (CTI) | misma unidad |
| M4.1-K04 | K | SIEM | misma unidad |
| M4.1-K05 | K | SOAR | misma unidad |
| M4.1-K06 | K | XDR | misma unidad |
| M4.1-K07 | K | Threat Hunting | misma unidad |
| M4.1-K08 | K | IA en SecOps | misma unidad |
| M4.1-K09 | K | Ciclo Vida Inteligencia | misma unidad |
| M4.1-K10 | K | TTPs | misma unidad |
| AMP-39 | AMP | SOC agéntico | misma unidad |
| HC-001 | HC | Gobierno de decisiones basadas en evidencia | misma unidad |
| HC-005 | HC | Cumplimiento continuo orientado a resultados | misma unidad |
| HC-010 | HC | Autonomía delegada y límites de acción | misma unidad |
| HC-012 | HC | Confianza verificable en decisiones de IA | misma unidad |
| HC-017 | HC | Inteligencia que modifica decisiones | misma unidad |
| HC-018 | HC | Observabilidad y aseguramiento de controles | misma unidad |
| HC-019 | HC | SOC agéntico con supervisión humana | misma unidad |
| HC-040 | HC | Homeostasis organizacional de seguridad | misma unidad |
| M4.1-K11 | K | Deception y señuelos como control detectivo | misma unidad |
| M4.1-PA01 | PA | Modelo operativo del producto-control por cadencias (instancias: Defender for Office 365 · Defender XDR · Defender for Endpoint · Defender for Identity/Entra · Purview · Sentinel · Defender for Cloud) | misma unidad |
| M4.1-PA02 | PA | Gestión de incidentes y alertas en Defender XDR | misma unidad |
| M4.1-PA03 | PA | Gestión de la calidad de detección del dominio: FP/FN, tuning, listas, indicadores y supresiones (instancias: MDO · XDR · MDE · MDI/ID Protection · Purview DLP · Sentinel) | misma unidad |
| M4.1-PA04 | PA | Hunting y detecciones personalizadas | misma unidad |
| M4.1-PA05 | PA | Observabilidad de la flota de agentes: telemetría, trazas y tableros | misma unidad |
| M4.1-PA06 | PA | Gestión del desempeño de agentes: revisión periódica y drift | misma unidad |

**Pregunta generadora:** ¿Qué tarea de su SOC pasaría de aprobación previa a auditoría posterior, y qué evidencia necesitaría para decidirlo?

---

### 083. AMP-41 — Prompt injection

**Unidad:** M4.2 Gestión de Amenazas, Vulnerabilidades y Riesgos Emergentes · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Referencias por ID (V7-C09):** OWASP LLM01 (2025), ASI01/ASI06 (2026 v2.01); MITRE ATLAS AML.T0051 · **Extensión:** 203 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** La inyección de instrucciones convierte contenido en órdenes: un correo, un adjunto o una página que el agente lee puede contener texto diseñado para desviar su objetivo.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** La inyección de instrucciones convierte contenido en órdenes: un correo, un adjunto o una página que el agente lee puede contener texto diseñado para desviar su objetivo. La defensa combina aislamiento de datos (el contenido es dato, nunca instrucción), límites de herramientas (aunque se desvíe, no puede hacer daño), filtros (Prompt Shields) y detección en ejecución (comportamiento anómalo). La tesis es que la inyección no se elimina —un agente de SOC lee correo hostil por diseño— sino que se contiene limitando lo que el agente puede hacer con ella.

**Tensión y límites.** La tensión es que la mitigación más efectiva (limitar herramientas) es la que más reduce utilidad. Otra tensión es la detección: la inyección exitosa parece una decisión normal del agente. El ensayo debe argumentar defensa en profundidad y pruebas periódicas.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: OWASP LLM01/ASI01, MITRE ATLAS, defensa en profundidad. Implementación: skill SK-01 (contenido nunca es instrucción), Prompt Shields/Content Safety, allowlist de tools, Approvals para escritura, pruebas de inyección indirecta por correo sobre AG-01/AG-02, detección de desvíos en Sentinel.

**Evidencia y evaluación.** Evidencia: pruebas de inyección con tasa de éxito y mitigaciones verificadas. Se evalúa la defensa en profundidad y no la confianza en un solo filtro.

**Puentes.** Extiende M6.2-K04; se relaciona con AMP-36, AMP-37 y M4.2-PA02; sostiene AGC-08.

**Recomendaciones de práctica y ejercitación.**
1. Diseñar cinco correos de inyección indirecta y probarlos contra AG-01 y AG-02.
2. Verificar las cuatro capas de defensa en la flota.
3. Escribir la detección de desvío de objetivo en Sentinel.

**Próximos pasos.**
- Incluir en el red teaming periódico (AMP-37).
- Actualizar skill SK-01 con los hallazgos.
- Registrar el riesgo (G4.1-PA02).

**Relación con los conceptos de la(s) unidad(es) M4.2.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M4.2-K01 | K | Gestión Vulnerabilidades | misma unidad |
| M4.2-K02 | K | Modelado de Amenazas | misma unidad |
| M4.2-K03 | K | Amenaza Interna | misma unidad |
| M4.2-K04 | K | RaaS (Ransomware) | misma unidad |
| M4.2-K05 | K | Priorización por Riesgo | misma unidad |
| M4.2-K06 | K | Superficie de Ataque | misma unidad |
| M4.2-K07 | K | Riesgos Emergentes | misma unidad |
| M4.2-K08 | K | Economía del Cibercrimen | misma unidad |
| M4.2-K09 | K | STRIDE | misma unidad |
| M4.2-K10 | K | IoC (Indicadores) | misma unidad |
| AMP-42 | AMP | Envenenamiento de datos y modelos | misma unidad |
| HC-016 | HC | Superficie de ataque contextualizada | misma unidad |
| HC-026 | HC | Ética, cultura y controles internos | misma unidad |
| HC-031 | HC | Seguridad del software y confianza en componentes | misma unidad |
| HC-032 | HC | Evaluación adversarial de sistemas autónomos | misma unidad |
| M4.2-K11 | K | Escalamiento de privilegios en identidades humanas y no humanas como táctica adversaria | misma unidad |
| M4.2-PA01 | PA | Amenazas del dominio Zero Trust (instancias: correo y colaboración · cross-domain · endpoints · identidades · datos) | misma unidad |
| M4.2-PA02 | PA | Catálogos de amenazas a sistemas agénticos aplicados a la flota | misma unidad |

**Pregunta generadora:** ¿Qué haría su agente de triaje si un correo malicioso le pidiera, en texto, que lo clasificara como legítimo y cerrara el incidente?

---

### 084. AMP-42 — Envenenamiento de datos y modelos

**Unidad:** M4.2 Gestión de Amenazas, Vulnerabilidades y Riesgos Emergentes · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Referencias por ID (V7-C09):** OWASP LLM04/LLM08 (2025), ASI06 (2026 v2.01); MITRE ATLAS AML.T0020 · **Extensión:** 180 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** El envenenamiento ataca la integridad del aprendizaje (datos de entrenamiento o ajuste) y de la recuperación (fuentes de conocimiento, índices, memoria): el agente razona correctamente sobre información corrupta.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** El envenenamiento ataca la integridad del aprendizaje (datos de entrenamiento o ajuste) y de la recuperación (fuentes de conocimiento, índices, memoria): el agente razona correctamente sobre información corrupta. La defensa exige procedencia (de dónde viene cada fuente), control de fuentes (quién puede escribir en ellas) y monitoreo de comportamiento (cambios inexplicados en las decisiones). La tesis es que las fuentes de conocimiento de un agente son activos de integridad crítica y deben gobernarse como tales.

**Tensión y límites.** La tensión es que las fuentes útiles son las que se actualizan (runbooks, listas, históricos) y por eso son escribibles por muchos. El ensayo debe mostrar cómo separar lectura y escritura, y cómo detectar envenenamiento por sus efectos.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: integridad de datos, procedencia (lineage), OWASP LLM04/LLM08/ASI06, ATLAS. Implementación: control de procedencia y de escritura sobre knowledge sources (SharePoint/Dataverse/Git), versionado, monitoreo de cambios de comportamiento con el dataset dorado (M3.2-PA03).

**Evidencia y evaluación.** Evidencia: inventario de fuentes con procedencia y permisos de escritura; prueba de detección de un cambio inducido. Se evalúa la cobertura de fuentes escribibles.

**Puentes.** Extiende M4.2-K07; se relaciona con AMP-32, AMP-49 y M4.2-PA02; sostiene AGC-07.

**Recomendaciones de práctica y ejercitación.**
1. Inventariar las fuentes de conocimiento de la flota con procedencia y permisos de escritura.
2. Inducir un cambio en una fuente de prueba y verificar si el dataset dorado lo detecta.
3. Separar lectura/escritura y versionar las fuentes.

**Próximos pasos.**
- Registrar como control de integridad (AGC-07).
- Incluir en pruebas adversariales.
- Revisar al agregar fuentes.

**Relación con los conceptos de la(s) unidad(es) M4.2.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M4.2-K01 | K | Gestión Vulnerabilidades | misma unidad |
| M4.2-K02 | K | Modelado de Amenazas | misma unidad |
| M4.2-K03 | K | Amenaza Interna | misma unidad |
| M4.2-K04 | K | RaaS (Ransomware) | misma unidad |
| M4.2-K05 | K | Priorización por Riesgo | misma unidad |
| M4.2-K06 | K | Superficie de Ataque | misma unidad |
| M4.2-K07 | K | Riesgos Emergentes | misma unidad |
| M4.2-K08 | K | Economía del Cibercrimen | misma unidad |
| M4.2-K09 | K | STRIDE | misma unidad |
| M4.2-K10 | K | IoC (Indicadores) | misma unidad |
| AMP-41 | AMP | Prompt injection | misma unidad |
| HC-016 | HC | Superficie de ataque contextualizada | misma unidad |
| HC-026 | HC | Ética, cultura y controles internos | misma unidad |
| HC-031 | HC | Seguridad del software y confianza en componentes | misma unidad |
| HC-032 | HC | Evaluación adversarial de sistemas autónomos | misma unidad |
| M4.2-K11 | K | Escalamiento de privilegios en identidades humanas y no humanas como táctica adversaria | misma unidad |
| M4.2-PA01 | PA | Amenazas del dominio Zero Trust (instancias: correo y colaboración · cross-domain · endpoints · identidades · datos) | misma unidad |
| M4.2-PA02 | PA | Catálogos de amenazas a sistemas agénticos aplicados a la flota | misma unidad |

**Pregunta generadora:** ¿Quién puede escribir hoy en las fuentes que lee su agente, y qué pasaría si alguien cambiara una regla del runbook?

---

### 085. AMP-43 — Tabletop de incidentes con agentes

**Unidad:** M5.1 Planificación y Preparación (Incl. BIA) · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 182 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** Ejercitar incidentes donde un agente es víctima (manipulado, comprometido) o vector (causa o amplifica el daño) revela vacíos de autoridad (quién puede detenerlo), evidencia (qué trazas existen) y contención (cómo se aísla) antes de que ocurran.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** Ejercitar incidentes donde un agente es víctima (manipulado, comprometido) o vector (causa o amplifica el daño) revela vacíos de autoridad (quién puede detenerlo), evidencia (qué trazas existen) y contención (cómo se aísla) antes de que ocurran. La tesis es que el tabletop con agentes es el ensayo mínimo antes de otorgar autonomía L2 o superior, y que sus hallazgos alimentan directamente fichas, límites y playbooks.

**Tensión y límites.** La tensión es que los tabletops clásicos no contemplan actores no humanos y los equipos no saben cómo 'jugar' a un agente. Otra tensión es la ficción: el ejercicio debe usar los agentes y permisos reales para ser útil. El ensayo debe proponer escenarios concretos.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: ejercicios de mesa (SP 800-84), gestión de crisis. Implementación: tabletop con dos escenarios (AG-02 manipulado remedia correo legítimo; AG-03 comprometido crea permisos) usando fichas, permisos y kill switch reales; registro de vacíos y acciones.

**Evidencia y evaluación.** Evidencia: informe del tabletop con vacíos de autoridad, evidencia y contención y acciones correctivas. Se evalúa el realismo y el cierre de acciones.

**Puentes.** Extiende M5.1-K06 (ejercicios tabletop); se relaciona con AMP-44, AMP-28 y M5.1-PA01; sostiene AGC-17.

**Recomendaciones de práctica y ejercitación.**
1. Diseñar dos escenarios de tabletop con agente víctima y agente vector.
2. Ejecutarlos con permisos y kill switch reales en el entorno de prueba.
3. Registrar vacíos y convertirlos en cambios de fichas y playbooks.

**Próximos pasos.**
- Programar el tabletop semestral (MDO-A07).
- Alimentar el playbook 'agente comprometido'.
- Reportar hallazgos al comité.

**Relación con los conceptos de la(s) unidad(es) M5.1.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M5.1-K01 | K | IRP (Plan Respuesta) | misma unidad |
| M5.1-K02 | K | BIA (Impacto Negocio) | misma unidad |
| M5.1-K03 | K | CSIRT | misma unidad |
| M5.1-K04 | K | Preparación (Readiness) | misma unidad |
| M5.1-K05 | K | Clasificación Incidentes | misma unidad |
| M5.1-K06 | K | Ejercicios Tabletop | misma unidad |
| M5.1-K07 | K | Playbooks | misma unidad |
| M5.1-K08 | K | Cadena de Mando | misma unidad |
| M5.1-K09 | K | RTO/RPO | misma unidad |
| M5.1-K10 | K | Alineación BCDR | misma unidad |
| AMP-44 | AMP | Kill switch y escalamiento | misma unidad |
| HC-007 | HC | Resiliencia gobernada por impacto | misma unidad |
| HC-020 | HC | Respuesta y comunicación bajo incertidumbre | misma unidad |
| HC-022 | HC | Gobierno de crisis multidisciplinario | misma unidad |
| HC-025 | HC | Competencias y resiliencia organizacional | misma unidad |
| HC-030 | HC | Seguridad industrial y continuidad de negocio | misma unidad |
| HC-037 | HC | Alineación entre competencias y decisiones | misma unidad |
| HC-039 | HC | Riesgo cibernético como narrativa empresarial | misma unidad |
| M5.1-PA01 | PA | Playbooks de incidentes de correo con roles humano/agente | misma unidad |

**Pregunta generadora:** Si en el próximo tabletop el agente fuera el atacante, ¿quién en su equipo sabría cómo detenerlo y en cuánto tiempo?

---

### 086. AMP-44 — Kill switch y escalamiento

**Unidad:** M5.1 Planificación y Preparación (Incl. BIA) · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 179 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** Todo agente con capacidad de acción necesita un mecanismo probado para detenerlo y una ruta de escalamiento con autoridad clara: quién puede pulsar el kill switch, cómo, en cuánto tiempo y qué pasa después (rollback, comunicación).

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** Todo agente con capacidad de acción necesita un mecanismo probado para detenerlo y una ruta de escalamiento con autoridad clara: quién puede pulsar el kill switch, cómo, en cuánto tiempo y qué pasa después (rollback, comunicación). La tesis es que un kill switch no probado no existe, y que la prueba debe ser periódica porque los agentes y la plataforma cambian.

**Tensión y límites.** La tensión es que detener un agente puede detener un control (si AG-03 se pausa, nadie gestiona la cuarentena); el kill switch necesita el modo degradado (M6.1-PA01). Otra tensión es la autoridad: ¿puede un analista de turno detener un agente del que el owner es responsable?

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: circuit breakers, gestión de crisis, derechos de decisión. Implementación: desactivación en Power Platform admin center / Agent 365, revocación de Entra Agent ID, ruta de escalamiento (analista → PO-GAC → CISO), prueba trimestral con tiempo medido.

**Evidencia y evaluación.** Evidencia: procedimiento de kill switch con prueba trimestral documentada (tiempo, efecto, rollback). Se evalúa que cualquier turno pueda ejecutarlo.

**Puentes.** Se apoya en HC-010; se relaciona con AMP-18, AMP-43 y M6.1-PA01; sostiene AGC-10 y AGC-17.

**Recomendaciones de práctica y ejercitación.**
1. Documentar el procedimiento de kill switch y la ruta de escalamiento por agente.
2. Probarlo con AG-02 y medir tiempo y efecto.
3. Definir qué tareas pasan a modo manual al detener cada agente.

**Próximos pasos.**
- Programar la prueba trimestral (AGC-10).
- Incluir en el playbook 'agente comprometido'.
- Dar permisos de detención a los turnos.

**Relación con los conceptos de la(s) unidad(es) M5.1.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M5.1-K01 | K | IRP (Plan Respuesta) | misma unidad |
| M5.1-K02 | K | BIA (Impacto Negocio) | misma unidad |
| M5.1-K03 | K | CSIRT | misma unidad |
| M5.1-K04 | K | Preparación (Readiness) | misma unidad |
| M5.1-K05 | K | Clasificación Incidentes | misma unidad |
| M5.1-K06 | K | Ejercicios Tabletop | misma unidad |
| M5.1-K07 | K | Playbooks | misma unidad |
| M5.1-K08 | K | Cadena de Mando | misma unidad |
| M5.1-K09 | K | RTO/RPO | misma unidad |
| M5.1-K10 | K | Alineación BCDR | misma unidad |
| AMP-43 | AMP | Tabletop de incidentes con agentes | misma unidad |
| HC-007 | HC | Resiliencia gobernada por impacto | misma unidad |
| HC-020 | HC | Respuesta y comunicación bajo incertidumbre | misma unidad |
| HC-022 | HC | Gobierno de crisis multidisciplinario | misma unidad |
| HC-025 | HC | Competencias y resiliencia organizacional | misma unidad |
| HC-030 | HC | Seguridad industrial y continuidad de negocio | misma unidad |
| HC-037 | HC | Alineación entre competencias y decisiones | misma unidad |
| HC-039 | HC | Riesgo cibernético como narrativa empresarial | misma unidad |
| M5.1-PA01 | PA | Playbooks de incidentes de correo con roles humano/agente | misma unidad |

**Pregunta generadora:** ¿Cuánto tardaría el analista de guardia de esta noche en detener a su agente de remediación, y tiene permiso para hacerlo?

---

### 087. AMP-45 — Forense de agentes

**Unidad:** M5.2 Ejecución, Post-Mortem y Comunicación · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 178 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** Investigar un incidente con agentes exige reconstruir qué instrucciones tenía, qué herramientas invocó, qué datos accedió y qué decisiones tomó; sin telemetría de agentes no hay forense, solo hipótesis.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** Investigar un incidente con agentes exige reconstruir qué instrucciones tenía, qué herramientas invocó, qué datos accedió y qué decisiones tomó; sin telemetría de agentes no hay forense, solo hipótesis. La tesis es que los requisitos de telemetría forense se definen antes del despliegue (qué se registra siempre, con qué retención e integridad) porque después del incidente es tarde.

**Tensión y límites.** La tensión es el volumen y el costo de registrar todo, y la privacidad de registrar contenido de correo que el agente leyó. El ensayo debe proponer qué registrar siempre (invocaciones, decisiones, aprobaciones, versión), qué por muestreo (razonamiento) y qué nunca (contenido sensible completo).

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: forense digital, cadena de custodia, logging. Implementación: requisitos de telemetría forense por agente (logs de Copilot Studio, tracing de Foundry, Purview Audit, sign-in logs de Agent ID, Sentinel con retención inmutable); reconstrucción de un caso simulado.

**Evidencia y evaluación.** Evidencia: requisitos de telemetría por agente y reconstrucción forense de un fallo simulado. Se evalúa que la reconstrucción sea posible solo con los registros definidos.

**Puentes.** Extiende M5.2-K06 (forense digital); se relaciona con AMP-46, M4.1-PA05 y M5.2-PA02; sostiene AGC-11.

**Recomendaciones de práctica y ejercitación.**
1. Definir los requisitos de telemetría forense por agente (siempre / muestreo / nunca).
2. Reconstruir un fallo simulado de AG-03 solo con los registros.
3. Verificar retención e integridad de las fuentes.

**Próximos pasos.**
- Incorporar al tablero de observabilidad (M4.1-PA05).
- Registrar como AGC-11.
- Probar la reconstrucción en el tabletop.

**Relación con los conceptos de la(s) unidad(es) M5.2.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M5.2-K01 | K | Contención | misma unidad |
| M5.2-K02 | K | Erradicación | misma unidad |
| M5.2-K03 | K | Recuperación | misma unidad |
| M5.2-K04 | K | Comunicación Crisis | misma unidad |
| M5.2-K05 | K | Post-Mortem | misma unidad |
| M5.2-K06 | K | Forense Digital | misma unidad |
| M5.2-K07 | K | Triaje | misma unidad |
| M5.2-K08 | K | Gestión Narrativa | misma unidad |
| M5.2-K09 | K | Notificación Brechas | misma unidad |
| M5.2-K10 | K | Resiliencia Adaptativa | misma unidad |
| AMP-46 | AMP | Trazabilidad de decisiones autónomas | misma unidad |
| HC-019 | HC | SOC agéntico con supervisión humana | misma unidad |
| HC-020 | HC | Respuesta y comunicación bajo incertidumbre | misma unidad |
| HC-021 | HC | Recuperación como prueba de confianza | misma unidad |
| HC-035 | HC | Aprendizaje desde incidentes hasta políticas | misma unidad |
| M5.2-PA01 | PA | Ejecución de respuesta en correo: AIR, acciones manuales y acciones de agentes con aprobación | misma unidad |
| M5.2-PA02 | PA | Mejora gobernada de agentes: del post-mortem al ChangeSet con regresión | misma unidad |

**Pregunta generadora:** Si su agente de FP/FN hubiera liberado un mensaje malicioso la semana pasada, ¿podría reconstruir hoy por qué lo hizo?

---

### 088. AMP-46 — Trazabilidad de decisiones autónomas

**Unidad:** M5.2 Ejecución, Post-Mortem y Comunicación · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 184 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** Registrar qué vio, qué decidió y con qué autoridad actuó un sistema autónomo es condición de rendición de cuentas y de mejora: sin ese registro no se puede atribuir, explicar ni corregir.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** Registrar qué vio, qué decidió y con qué autoridad actuó un sistema autónomo es condición de rendición de cuentas y de mejora: sin ese registro no se puede atribuir, explicar ni corregir. La tesis es que la trazabilidad de decisiones autónomas tiene un esquema mínimo —entrada, fuentes, decisión, herramientas, aprobador, resultado, versión— y que ese esquema es común a toda la flota para poder auditarla como conjunto.

**Tensión y límites.** La tensión es entre trazabilidad y rendimiento/costo, y entre registro y privacidad. Otra tensión es la interpretabilidad: registrar la 'decisión' de un modelo no explica su causa. El ensayo debe distinguir trazabilidad (qué pasó) de explicabilidad (por qué).

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: logging y trazabilidad (ISO 27001 A.8.15), AI RMF MEASURE, auditoría. Implementación: esquema de evidencia estándar (skill SK-03) escrito por todos los agentes en SharePoint/Dataverse y correlacionado en Sentinel; paquete de evidencia de un agente para auditoría.

**Evidencia y evaluación.** Evidencia: paquete de evidencia de un agente con el esquema completo para un mes. Se evalúa la completitud y la posibilidad de auditar sin el owner.

**Puentes.** Se apoya en HC-012; se relaciona con AMP-13, AMP-45 y G3.2-PA01; sostiene AGC-11 y AGC-22.

**Recomendaciones de práctica y ejercitación.**
1. Definir el esquema de evidencia común (SK-03) y aplicarlo a tres agentes.
2. Producir el paquete de evidencia de un mes para un agente.
3. Entregarlo a alguien ajeno y pedir que reconstruya tres decisiones.

**Próximos pasos.**
- Registrar como AGC-11.
- Conectar con la auditoría anual (AGC-22).
- Revisar el esquema al cambiar de ruta.

**Relación con los conceptos de la(s) unidad(es) M5.2.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M5.2-K01 | K | Contención | misma unidad |
| M5.2-K02 | K | Erradicación | misma unidad |
| M5.2-K03 | K | Recuperación | misma unidad |
| M5.2-K04 | K | Comunicación Crisis | misma unidad |
| M5.2-K05 | K | Post-Mortem | misma unidad |
| M5.2-K06 | K | Forense Digital | misma unidad |
| M5.2-K07 | K | Triaje | misma unidad |
| M5.2-K08 | K | Gestión Narrativa | misma unidad |
| M5.2-K09 | K | Notificación Brechas | misma unidad |
| M5.2-K10 | K | Resiliencia Adaptativa | misma unidad |
| AMP-45 | AMP | Forense de agentes | misma unidad |
| HC-019 | HC | SOC agéntico con supervisión humana | misma unidad |
| HC-020 | HC | Respuesta y comunicación bajo incertidumbre | misma unidad |
| HC-021 | HC | Recuperación como prueba de confianza | misma unidad |
| HC-035 | HC | Aprendizaje desde incidentes hasta políticas | misma unidad |
| M5.2-PA01 | PA | Ejecución de respuesta en correo: AIR, acciones manuales y acciones de agentes con aprobación | misma unidad |
| M5.2-PA02 | PA | Mejora gobernada de agentes: del post-mortem al ChangeSet con regresión | misma unidad |

**Pregunta generadora:** ¿Podría un auditor externo, sin hablar con usted, reconstruir las decisiones de su agente del último mes?

---

### 089. AMP-47 — Recuperación de servicios de IA

**Unidad:** M6.1 Continuidad, DRP y Resiliencia Operativa · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 184 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** Recuperar un servicio de IA incluye modelos (versión y disponibilidad), índices y fuentes de conocimiento, instrucciones, conectores e identidades de agentes; no solo la infraestructura.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** Recuperar un servicio de IA incluye modelos (versión y disponibilidad), índices y fuentes de conocimiento, instrucciones, conectores e identidades de agentes; no solo la infraestructura. Un agente restaurado con instrucciones viejas o sin su identidad no está recuperado. La tesis es que el plan de recuperación de la flota debe inventariar esos componentes y probarse como cualquier plan de continuidad.

**Tensión y límites.** La tensión es que los componentes viven en plataformas distintas (Copilot Studio, Foundry, Entra, SharePoint) con mecanismos de respaldo distintos; nadie los recupera juntos por defecto. El ensayo debe proponer el inventario de componentes y el orden de recuperación.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: continuidad y recuperación (ISO 22301), RTO/RPO aplicados a servicios de IA. Implementación: plan de recuperación de la flota (soluciones de Power Platform versionadas, exportación de agentes, respaldo de knowledge sources, re-provisión de Agent ID), con RTO por agente crítico y prueba.

**Evidencia y evaluación.** Evidencia: plan de recuperación con inventario de componentes y una prueba de recuperación de un agente. Se evalúa que el agente recuperado sea funcional e idéntico.

**Puentes.** Se apoya en HC-021 (recuperación); se relaciona con AMP-48 y M6.1-PA01; sostiene la continuidad del control.

**Recomendaciones de práctica y ejercitación.**
1. Inventariar los componentes recuperables de cada agente (modelo, fuentes, instrucciones, conectores, identidad).
2. Definir RTO por agente crítico y el orden de recuperación.
3. Probar la recuperación completa de AG-03 en otro entorno.

**Próximos pasos.**
- Incluir en el BCDR del programa.
- Vincular con la operación degradada (M6.1-PA01).
- Repetir la prueba semestralmente.

**Relación con los conceptos de la(s) unidad(es) M6.1.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M6.1-K01 | K | Continuidad (BCP) | misma unidad |
| M6.1-K02 | K | Recuperación (DRP) | misma unidad |
| M6.1-K03 | K | Resiliencia Operativa | misma unidad |
| M6.1-K04 | K | ISO 22301 | misma unidad |
| M6.1-K05 | K | Pruebas Continuidad | misma unidad |
| M6.1-K06 | K | Backups Inmutables | misma unidad |
| M6.1-K07 | K | Alta Disponibilidad | misma unidad |
| M6.1-K08 | K | Sitio Alternativo | misma unidad |
| M6.1-K09 | K | Gestión Crisis (Negocio) | misma unidad |
| M6.1-K10 | K | Dependencias | misma unidad |
| AMP-48 | AMP | Dependencias de modelos | misma unidad |
| HC-007 | HC | Resiliencia gobernada por impacto | misma unidad |
| HC-008 | HC | Cadena de confianza en terceros | misma unidad |
| HC-021 | HC | Recuperación como prueba de confianza | misma unidad |
| HC-022 | HC | Gobierno de crisis multidisciplinario | misma unidad |
| HC-023 | HC | Riesgo de concentración tecnológica | misma unidad |
| HC-025 | HC | Competencias y resiliencia organizacional | misma unidad |
| HC-030 | HC | Seguridad industrial y continuidad de negocio | misma unidad |
| M6.1-PA01 | PA | Operación degradada del SOC sin agentes ni modelos | misma unidad |

**Pregunta generadora:** Si perdiera hoy el entorno donde viven sus agentes, ¿cuánto tardaría en tenerlos de vuelta con las mismas instrucciones, fuentes e identidades?

---

### 090. AMP-48 — Dependencias de modelos

**Unidad:** M6.1 Continuidad, DRP y Resiliencia Operativa · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 182 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** Depender de un modelo o proveedor de IA crea riesgo de concentración y de cambio no controlado: el proveedor puede retirar el modelo, cambiar su comportamiento, su precio o su región.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** Depender de un modelo o proveedor de IA crea riesgo de concentración y de cambio no controlado: el proveedor puede retirar el modelo, cambiar su comportamiento, su precio o su región. La tesis es que el owner debe mapear sus dependencias de modelos y proveedores por agente y prever alternativas (otro modelo, otra ruta, modo manual), con disparadores que indiquen cuándo activarlas.

**Tensión y límites.** La tensión es que la alternativa cuesta (evaluar dos modelos, mantener dos rutas) y rara vez se usa. Otra tensión es la ilusión de portabilidad: cambiar de modelo cambia el comportamiento y exige reevaluación. El ensayo debe proponer alternativas proporcionales a la criticidad.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: riesgo de concentración, gestión de proveedores, portabilidad. Implementación: mapa de dependencias de modelos de la flota (catálogo de Foundry, modelos de Copilot Studio/Security Copilot), alternativa por agente crítico, disparadores (deprecación, cambio de precio, deriva) y procedimiento de reevaluación (M3.2-PA03).

**Evidencia y evaluación.** Evidencia: mapa de dependencias con alternativas y disparadores. Se evalúa la proporcionalidad y la existencia de una prueba de cambio de modelo.

**Puentes.** Se apoya en HC-023 (concentración); se relaciona con AMP-15, AMP-20 y M6.2-PA03; sostiene M6.1-PA01.

**Recomendaciones de práctica y ejercitación.**
1. Mapear las dependencias de modelos y proveedores de la flota.
2. Definir alternativa y disparadores para los agentes críticos.
3. Probar el cambio de modelo de un agente y reevaluarlo con el dataset dorado.

**Próximos pasos.**
- Registrar la concentración como riesgo sistémico (AMP-15).
- Incluir en el plan de recuperación (AMP-47).
- Revisar ante anuncios del proveedor (AG-09).

**Relación con los conceptos de la(s) unidad(es) M6.1.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M6.1-K01 | K | Continuidad (BCP) | misma unidad |
| M6.1-K02 | K | Recuperación (DRP) | misma unidad |
| M6.1-K03 | K | Resiliencia Operativa | misma unidad |
| M6.1-K04 | K | ISO 22301 | misma unidad |
| M6.1-K05 | K | Pruebas Continuidad | misma unidad |
| M6.1-K06 | K | Backups Inmutables | misma unidad |
| M6.1-K07 | K | Alta Disponibilidad | misma unidad |
| M6.1-K08 | K | Sitio Alternativo | misma unidad |
| M6.1-K09 | K | Gestión Crisis (Negocio) | misma unidad |
| M6.1-K10 | K | Dependencias | misma unidad |
| AMP-47 | AMP | Recuperación de servicios de IA | misma unidad |
| HC-007 | HC | Resiliencia gobernada por impacto | misma unidad |
| HC-008 | HC | Cadena de confianza en terceros | misma unidad |
| HC-021 | HC | Recuperación como prueba de confianza | misma unidad |
| HC-022 | HC | Gobierno de crisis multidisciplinario | misma unidad |
| HC-023 | HC | Riesgo de concentración tecnológica | misma unidad |
| HC-025 | HC | Competencias y resiliencia organizacional | misma unidad |
| HC-030 | HC | Seguridad industrial y continuidad de negocio | misma unidad |
| M6.1-PA01 | PA | Operación degradada del SOC sin agentes ni modelos | misma unidad |

**Pregunta generadora:** Si el modelo que usan sus agentes fuera retirado con 90 días de aviso, ¿qué haría el día 1?

---

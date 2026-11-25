# TheNextCISO GM-24 — Pre-ensayos (archivos de inicialización), lote AMP-01 (V7.1)

> **GM-24 V7.1 · The Next CISO + Sub-plan PO-GAC** · 2026-11-14. Catálogo: 379 conceptos (245 K · 52 AMP · 40 HC · 42 PA), todos con pre-ensayo íntegro y mapeados a 17 marcos (NIST/ISACA/MITRE/OWASP/CIS/CSA). V7.1 = ChangeSet editorial CS-GM24-V7.1-001 (4 títulos generalizados; sin cambio de IDs, cantidad ni mapeo). Plano A (corpus académico). Referencias DD/K4x/R/eo:OP/COE: marco interno.

**Estado:** ideas centrales para desarrollo editorial; IDs curriculares (asignar `ESS-######` desde el registro SQLite). Estructura de los lotes GM-24 + práctica, próximos pasos y relación con la unidad.

## Inventario

| N.º | ID | Tipo | Unidad | Concepto |
|---|---|---|---|---|
| 043 | AMP-01 | AMP | G1.1 | Metacognición del CISO |
| 044 | AMP-02 | AMP | G1.1 | Sesgos y límites cognitivos |
| 045 | AMP-03 | AMP | G1.1 | Autoridad frente a responsabilidad |
| 046 | AMP-04 | AMP | G1.2 | Estrategia adaptativa |
| 047 | AMP-05 | AMP | G1.2 | Evolución contextual H |
| 048 | AMP-06 | AMP | G1.2 | Gobierno de la IA |
| 049 | AMP-07 | AMP | G2.1 | NIST CSF 2.0 Govern |
| 050 | AMP-08 | AMP | G2.1 | Referencias informativas y no equivalencia |
| 051 | AMP-09 | AMP | G2.2 | Policy-as-code |
| 052 | AMP-10 | AMP | G2.2 | Gobierno de excepciones automatizadas |
| 053 | AMP-11 | AMP | G3.1 | Soberanía de datos |
| 054 | AMP-12 | AMP | G3.1 | Responsabilidad por agentes |
| 055 | AMP-13 | AMP | G3.2 | Evidencia continua |
| 056 | AMP-14 | AMP | G3.2 | Aseguramiento de decisiones de IA |
| 057 | AMP-15 | AMP | G4.1 | Riesgo sistémico |
| 058 | AMP-16 | AMP | G4.1 | Homeostasis y fuerzas de cambio |
| 059 | AMP-17 | AMP | G4.2 | Autoridad delegada |
| 060 | AMP-18 | AMP | G4.2 | Límites de autonomía |
| 061 | AMP-19 | AMP | G5.1 | Calidad epistemológica de evidencia |
| 062 | AMP-20 | AMP | G5.1 | Riesgo de modelos de IA |
| 063 | AMP-21 | AMP | G5.2 | Decisiones reversibles |
| 064 | AMP-22 | AMP | G5.2 | Aceptación de riesgo de agentes |
| 065 | AMP-23 | AMP | G6.1 | Narrativa de riesgo basada en evidencia |
| 066 | AMP-24 | AMP | G6.1 | Comunicación de incertidumbre |

---

### 043. AMP-01 — Metacognición del CISO

**Unidad:** G1.1 Principios de Gobierno, Contexto Organizacional y Arquetipos CISO · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 296 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** El CISO decide mejor cuando examina cómo decide.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** El CISO decide mejor cuando examina cómo decide. La metacognición aplicada al gobierno de la seguridad consiste en hacer explícitos, antes de decidir, tres cosas: los supuestos sobre los que se apoya la decisión, las fuentes a las que se les concede confianza y los criterios que harían revisarla. Cuando la IA entra en el circuito de decisión —resúmenes, recomendaciones, priorizaciones— ese examen deja de ser un lujo intelectual y se vuelve un control: si el CISO no sabe cómo decide, no puede saber qué parte de su juicio está delegando a un modelo.

**Tensión y límites.** La tensión está en el tiempo y en la cultura: la agenda de un CISO premia decidir rápido y proyectar seguridad; detenerse a declarar supuestos parece debilidad. Otra tensión es la ilusión de objetividad que produce un asistente de IA: una recomendación bien redactada se percibe como más fundada de lo que está. El ensayo debe mostrar que la metacognición no ralentiza las decisiones rutinarias sino que concentra el esfuerzo en las pocas decisiones irreversibles o de alto impacto.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: modelos de decisión bajo incertidumbre, listas de verificación pre-decisión, registro de decisiones (decision log). Implementación en el escenario: un registro de decisiones del programa (SharePoint/Dataverse) con campos de supuestos, fuentes, criterios de revisión y participación de IA; uso del propio asistente para generar la 'contraargumentación' antes de cerrar una decisión.

**Evidencia y evaluación.** Evidencia: cinco decisiones del último trimestre reconstruidas con supuestos, fuentes y criterios de revisión; identificación de cuáles habrían cambiado con un supuesto distinto. Se evalúa la honestidad del registro y la capacidad de distinguir lo que se sabía de lo que se suponía.

**Puentes.** Se apoya en G1.1-K03 (arquetipos y rol del CISO) y prepara AMP-02 (sesgos) y AMP-19 (calidad epistemológica de la evidencia); se relaciona con G6.1-K05 (separar hechos e inferencias).

**Recomendaciones de práctica y ejercitación.**
1. Reconstruir cinco decisiones recientes con la plantilla supuestos / fuentes / criterios de revisión / participación de IA.
2. Pedir a un asistente de IA la contraargumentación de una decisión pendiente y registrar qué cambió.
3. Definir qué tipos de decisión del programa requieren registro metacognitivo obligatorio.

**Próximos pasos.**
- Incorporar el registro de decisiones al CISO-OS (AMP-27).
- Usarlo como insumo de la narrativa de riesgo (AMP-23).
- Revisar trimestralmente qué supuestos se cumplieron.

**Relación con los conceptos de la(s) unidad(es) G1.1.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| G1.1-K01 | K | Principios de Gobierno | misma unidad |
| G1.1-K02 | K | Contexto Organizacional | misma unidad |
| G1.1-K03 | K | Arquetipos CISO | misma unidad |
| G1.1-K04 | K | Alineación Estratégica | misma unidad |
| G1.1-K05 | K | Cultura de Seguridad | misma unidad |
| G1.1-K06 | K | Visión Holística | misma unidad |
| G1.1-K07 | K | CISO como Socio de Negocio | misma unidad |
| G1.1-K08 | K | Gestión Estratégica del Riesgo | misma unidad |
| G1.1-K09 | K | Liderazgo de Influencia | misma unidad |
| G1.1-K10 | K | Mejora Continua (Gobierno) | misma unidad |
| AMP-02 | AMP | Sesgos y límites cognitivos | misma unidad |
| AMP-03 | AMP | Autoridad frente a responsabilidad | misma unidad |
| HC-001 | HC | Gobierno de decisiones basadas en evidencia | misma unidad |
| HC-037 | HC | Alineación entre competencias y decisiones | misma unidad |
| HC-040 | HC | Homeostasis organizacional de seguridad | misma unidad |
| G1.1-PA01 | PA | Rol dual especialista/manager y Product Owner de control | misma unidad |

**Pregunta generadora:** ¿Cuál fue la última decisión de seguridad importante que tomó, qué supuesto la sostenía y qué tendría que ocurrir para que la revisara?

---

### 044. AMP-02 — Sesgos y límites cognitivos

**Unidad:** G1.1 Principios de Gobierno, Contexto Organizacional y Arquetipos CISO · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 254 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** Anclaje, confirmación y sesgo de automatización distorsionan las decisiones de riesgo de forma predecible: el primer número fija la estimación, la evidencia que confirma pesa más que la que contradice y la recomendación de una máquina se acepta con menos escrutinio que la de una persona.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** Anclaje, confirmación y sesgo de automatización distorsionan las decisiones de riesgo de forma predecible: el primer número fija la estimación, la evidencia que confirma pesa más que la que contradice y la recomendación de una máquina se acepta con menos escrutinio que la de una persona. Con asistentes de IA en el SOC y en el comité de riesgo, el tercer sesgo se vuelve dominante. La tesis es que la verificación humana debe diseñarse como proceso —quién verifica, con qué información, en cuánto tiempo— y no suponerse como actitud.

**Tensión y límites.** La tensión es que la verificación cuesta: si cada recomendación del asistente se revisa a fondo, el asistente no ahorra nada; si ninguna se revisa, el sesgo de automatización gobierna. El diseño debe graduar la verificación por riesgo y reversibilidad (lo que AMP-40 llama HITL por riesgo) y medir la tasa de corrección humana como señal de salud, no de fracaso.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: psicología de la decisión aplicada al riesgo; listas de verificación; muestreo. Implementación: en el triaje asistido por AG-01, una checklist de verificación en las aprobaciones L2 (¿qué evidencia miré además de la propuesta?, ¿qué habría decidido sin ella?) y la métrica de propuestas corregidas (KPI-11 leído al revés).

**Evidencia y evaluación.** Evidencia: un experimento de dos semanas comparando decisiones con y sin recomendación del asistente en los mismos casos; informe de sesgo observado. Se evalúa el diseño del experimento y la lectura prudente de los resultados.

**Puentes.** Extiende M4.1-K08 (IA en SecOps) y AMP-01 (metacognición); sostiene AMP-26 (supervisión efectiva) y AMP-40 (HITL); se relaciona con G6.1-K05.

**Recomendaciones de práctica y ejercitación.**
1. Diseñar la checklist de verificación para aprobaciones L2 de AG-01 y AG-02.
2. Correr un experimento A/B de dos semanas sobre decisiones de triaje con y sin recomendación.
3. Definir la tasa de corrección humana esperada y qué significa que sea 0 %.

**Próximos pasos.**
- Incorporar la checklist a la ficha de agente (G2.2-PA02).
- Vincular con la evaluación de calidad del agente (M3.2-PA03).
- Revisar el sesgo de automatización en la revisión trimestral (M4.1-PA06).

**Relación con los conceptos de la(s) unidad(es) G1.1.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| G1.1-K01 | K | Principios de Gobierno | misma unidad |
| G1.1-K02 | K | Contexto Organizacional | misma unidad |
| G1.1-K03 | K | Arquetipos CISO | misma unidad |
| G1.1-K04 | K | Alineación Estratégica | misma unidad |
| G1.1-K05 | K | Cultura de Seguridad | misma unidad |
| G1.1-K06 | K | Visión Holística | misma unidad |
| G1.1-K07 | K | CISO como Socio de Negocio | misma unidad |
| G1.1-K08 | K | Gestión Estratégica del Riesgo | misma unidad |
| G1.1-K09 | K | Liderazgo de Influencia | misma unidad |
| G1.1-K10 | K | Mejora Continua (Gobierno) | misma unidad |
| AMP-01 | AMP | Metacognición del CISO | misma unidad |
| AMP-03 | AMP | Autoridad frente a responsabilidad | misma unidad |
| HC-001 | HC | Gobierno de decisiones basadas en evidencia | misma unidad |
| HC-037 | HC | Alineación entre competencias y decisiones | misma unidad |
| HC-040 | HC | Homeostasis organizacional de seguridad | misma unidad |
| G1.1-PA01 | PA | Rol dual especialista/manager y Product Owner de control | misma unidad |

**Pregunta generadora:** Si el asistente de triaje se equivocara el 10 % de las veces con total seguridad en su redacción, ¿cuántas de esas veces su equipo lo notaría hoy?

---

### 045. AMP-03 — Autoridad frente a responsabilidad

**Unidad:** G1.1 Principios de Gobierno, Contexto Organizacional y Arquetipos CISO · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 261 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** Responder sin autoridad, o decidir sin responder, es la falla de gobierno más frecuente, y la llegada de agentes la vuelve aguda: un agente ejecuta una acción con autoridad delegada, pero no puede responder por ella.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** Responder sin autoridad, o decidir sin responder, es la falla de gobierno más frecuente, y la llegada de agentes la vuelve aguda: un agente ejecuta una acción con autoridad delegada, pero no puede responder por ella. La tesis es que toda delegación a un agente debe tener un humano identificable que responde por el resultado y por el proceso, que esa persona debe tener autoridad real sobre el agente (configurarlo, limitarlo, detenerlo) y que la organización debe poder nombrarla antes del despliegue y no después del incidente.

**Tensión y límites.** La tensión aparece cuando el agente es compartido entre equipos, construido por uno y usado por otro, o provisto por un tercero: la autoridad se fragmenta y la responsabilidad se diluye. Otra tensión es la asimetría de competencia: el responsable formal puede no entender lo que el agente hace. El ensayo debe discutir el sponsor como figura mínima y los límites de la delegación hacia abajo.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: accountability y derechos de decisión; teoría de agencia. Implementación: sponsor obligatorio en Entra Agent ID, owner en Agent 365, declaración de accountability firmada por el PO-GAC para cada agente, y matriz de derechos de decisión de tres niveles (owner / dueño del riesgo / CISO).

**Evidencia y evaluación.** Evidencia: declaración de accountability de la flota y verificación de que cada agente registrado tiene sponsor con autoridad efectiva (puede detenerlo). Se evalúa la ausencia de agentes sin responsable y la coherencia entre autoridad declarada y permisos reales.

**Puentes.** Extiende G6.2-K10 (rendición de cuentas) y G1.1-K03; es la base de AGC-02 y de G4.1-PA01 (tres líneas); se relaciona con AMP-12 y HC-009.

**Recomendaciones de práctica y ejercitación.**
1. Redactar la declaración de accountability del PO-GAC para la flota.
2. Verificar en Entra/Agent 365 que cada agente tiene sponsor con capacidad real de detenerlo.
3. Simular un incidente y recorrer la cadena de responsabilidad hasta el CISO.

**Próximos pasos.**
- Registrar la declaración como evidencia de AGC-02.
- Incluirla en el expediente ATO (AMP-22).
- Revisar la cadena cuando un agente cambie de owner.

**Relación con los conceptos de la(s) unidad(es) G1.1.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| G1.1-K01 | K | Principios de Gobierno | misma unidad |
| G1.1-K02 | K | Contexto Organizacional | misma unidad |
| G1.1-K03 | K | Arquetipos CISO | misma unidad |
| G1.1-K04 | K | Alineación Estratégica | misma unidad |
| G1.1-K05 | K | Cultura de Seguridad | misma unidad |
| G1.1-K06 | K | Visión Holística | misma unidad |
| G1.1-K07 | K | CISO como Socio de Negocio | misma unidad |
| G1.1-K08 | K | Gestión Estratégica del Riesgo | misma unidad |
| G1.1-K09 | K | Liderazgo de Influencia | misma unidad |
| G1.1-K10 | K | Mejora Continua (Gobierno) | misma unidad |
| AMP-01 | AMP | Metacognición del CISO | misma unidad |
| AMP-02 | AMP | Sesgos y límites cognitivos | misma unidad |
| HC-001 | HC | Gobierno de decisiones basadas en evidencia | misma unidad |
| HC-037 | HC | Alineación entre competencias y decisiones | misma unidad |
| HC-040 | HC | Homeostasis organizacional de seguridad | misma unidad |
| G1.1-PA01 | PA | Rol dual especialista/manager y Product Owner de control | misma unidad |

**Pregunta generadora:** Si mañana un agente de su flota tomara una decisión equivocada con impacto en un cliente, ¿quién daría la cara, y esa persona sabe hoy que lo haría?

---

### 046. AMP-04 — Estrategia adaptativa

**Unidad:** G1.2 Desarrollo de Estrategia y Alineación con el Negocio · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 227 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** En la era de la IA la estrategia de seguridad deja de ser un plan a tres años y pasa a ser una cartera de opciones: iniciativas con hitos de revisión y criterios explícitos para acelerar, pausar o revertir.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** En la era de la IA la estrategia de seguridad deja de ser un plan a tres años y pasa a ser una cartera de opciones: iniciativas con hitos de revisión y criterios explícitos para acelerar, pausar o revertir. La tesis es que la adaptabilidad no es ausencia de estrategia sino una estrategia con mecanismos de corrección incorporados, y que esos mecanismos —señales que disparan revisión, decisiones reversibles, presupuesto por tramos— deben estar escritos antes de empezar.

**Tensión y límites.** La tensión es con la gobernanza clásica, que exige planes cerrados para aprobar presupuesto, y con la credibilidad del CISO, a quien se le pide certeza. También existe el riesgo de usar 'adaptativo' como excusa para no comprometerse. El ensayo debe mostrar cómo una cartera de opciones se presenta a un comité con la misma seriedad que un plan fijo.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: opciones reales, planificación por escenarios, OKR con revisión trimestral. Implementación: hoja de ruta de adopción agéntica del control de correo a doce meses, con tres fases (asistido, semi-autónomo, autónomo supervisado), señales de avance (KPI-11/12) y criterios de pausa o reversión.

**Evidencia y evaluación.** Evidencia: hoja de ruta con hitos, señales y criterios de decisión, presentada en formato de comité. Se evalúa que cada fase tenga criterio de salida y que la reversión esté prevista.

**Puentes.** Extiende G1.2-K08 (planificación estratégica); se apoya en AMP-21 (decisiones reversibles) y AMP-16 (homeostasis); alimenta G1.2-PA01 y M1.1-PA02.

**Recomendaciones de práctica y ejercitación.**
1. Redactar la hoja de ruta agéntica a doce meses con fases, señales y criterios de acelerar/pausar/revertir.
2. Presentarla en formato de comité y registrar las objeciones.
3. Definir el presupuesto por tramos asociado a cada fase.

**Próximos pasos.**
- Vincular las señales con los KRIs de la flota (G4.2-PA01).
- Revisar la cartera trimestralmente con el reporte ejecutivo.
- Conectar con la estrategia del programa (G1.2-K01).

**Relación con los conceptos de la(s) unidad(es) G1.2.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| G1.2-K01 | K | Estrategia de Ciberseguridad | misma unidad |
| G1.2-K02 | K | Alineación con Negocio | misma unidad |
| G1.2-K03 | K | Influencias y Tendencias | misma unidad |
| G1.2-K04 | K | Conexión de Valor | misma unidad |
| G1.2-K05 | K | Casos de Negocio | misma unidad |
| G1.2-K06 | K | ROI en Seguridad | misma unidad |
| G1.2-K07 | K | Visión de Negocio | misma unidad |
| G1.2-K08 | K | Planificación Estratégica | misma unidad |
| G1.2-K09 | K | Integración ERM | misma unidad |
| G1.2-K10 | K | Comunicación a la Junta | misma unidad |
| AMP-05 | AMP | Evolución contextual H | misma unidad |
| AMP-06 | AMP | Gobierno de la IA | misma unidad |
| HC-006 | HC | Valor de seguridad y medición causal | misma unidad |
| HC-013 | HC | Deuda de seguridad como riesgo de transformación | misma unidad |
| HC-014 | HC | Arquitectura de riesgo empresarial | misma unidad |
| HC-023 | HC | Riesgo de concentración tecnológica | misma unidad |
| HC-034 | HC | Decisiones reversibles y riesgo de transición | misma unidad |
| HC-035 | HC | Aprendizaje desde incidentes hasta políticas | misma unidad |
| HC-039 | HC | Riesgo cibernético como narrativa empresarial | misma unidad |
| G1.2-PA01 | PA | Economía unitaria de agentes: caso de negocio y TCO | misma unidad |

**Pregunta generadora:** ¿Qué señal, observable en los próximos seis meses, lo haría pausar la adopción de agentes en su SOC, y está escrita en algún lugar?

---

### 047. AMP-05 — Evolución contextual H

**Unidad:** G1.2 Desarrollo de Estrategia y Alineación con el Negocio · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 200 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** La evolución de las capacidades de seguridad es situada: avanza por catalizadores (un incidente, un regulador, un sponsor), se frena por inhibidores (deuda, cultura, presupuesto) y se estabiliza por mecanismos (rituales, métricas, roles) que la vuelven permanente.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** La evolución de las capacidades de seguridad es situada: avanza por catalizadores (un incidente, un regulador, un sponsor), se frena por inhibidores (deuda, cultura, presupuesto) y se estabiliza por mecanismos (rituales, métricas, roles) que la vuelven permanente. Esa lectura explica el avance real mejor que una escalera universal de madurez. La tesis es que el CISO debe leer su contexto —qué catalizadores tiene, qué inhibidores lo frenan— antes de fijar objetivos de madurez copiados de un modelo.

**Tensión y límites.** La tensión es con los modelos de madurez, útiles para comunicar y comparar pero engañosos como plan: dos organizaciones en el mismo 'nivel 3' pueden necesitar caminos opuestos. El ensayo debe conciliar ambos: el modelo como vocabulario, la lectura situada como método.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: modelos de madurez (CMMI, O-ISM3) leídos críticamente; análisis de fuerzas; teoría del cambio. Implementación: mapa de catalizadores, inhibidores y mecanismos de estabilización para la adopción del modelo operativo y de los agentes en el control de correo.

**Evidencia y evaluación.** Evidencia: mapa de fuerzas del programa con tres catalizadores, tres inhibidores y los mecanismos que estabilizarían los avances. Se evalúa la especificidad y la conexión con decisiones concretas.

**Puentes.** Extiende G2.1-K08 (medición de madurez); se relaciona con AMP-16 (homeostasis) y AMP-04 (estrategia adaptativa).

**Recomendaciones de práctica y ejercitación.**
1. Dibujar el mapa de catalizadores, inhibidores y mecanismos de estabilización del programa.
2. Contrastarlo con la autoevaluación de madurez vigente y anotar las divergencias.
3. Diseñar un mecanismo de estabilización para la adopción de agentes.

**Próximos pasos.**
- Usarlo en la hoja de ruta adaptativa (AMP-04).
- Revisarlo tras cada catalizador relevante (incidente, auditoría).
- Integrarlo al reporte ejecutivo como contexto.

**Relación con los conceptos de la(s) unidad(es) G1.2.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| G1.2-K01 | K | Estrategia de Ciberseguridad | misma unidad |
| G1.2-K02 | K | Alineación con Negocio | misma unidad |
| G1.2-K03 | K | Influencias y Tendencias | misma unidad |
| G1.2-K04 | K | Conexión de Valor | misma unidad |
| G1.2-K05 | K | Casos de Negocio | misma unidad |
| G1.2-K06 | K | ROI en Seguridad | misma unidad |
| G1.2-K07 | K | Visión de Negocio | misma unidad |
| G1.2-K08 | K | Planificación Estratégica | misma unidad |
| G1.2-K09 | K | Integración ERM | misma unidad |
| G1.2-K10 | K | Comunicación a la Junta | misma unidad |
| AMP-04 | AMP | Estrategia adaptativa | misma unidad |
| AMP-06 | AMP | Gobierno de la IA | misma unidad |
| HC-006 | HC | Valor de seguridad y medición causal | misma unidad |
| HC-013 | HC | Deuda de seguridad como riesgo de transformación | misma unidad |
| HC-014 | HC | Arquitectura de riesgo empresarial | misma unidad |
| HC-023 | HC | Riesgo de concentración tecnológica | misma unidad |
| HC-034 | HC | Decisiones reversibles y riesgo de transición | misma unidad |
| HC-035 | HC | Aprendizaje desde incidentes hasta políticas | misma unidad |
| HC-039 | HC | Riesgo cibernético como narrativa empresarial | misma unidad |
| G1.2-PA01 | PA | Economía unitaria de agentes: caso de negocio y TCO | misma unidad |

**Pregunta generadora:** ¿Qué cambio de seguridad logró su organización en los últimos dos años que sigue vivo, y qué mecanismo lo mantiene vivo?

---

### 048. AMP-06 — Gobierno de la IA

**Unidad:** G1.2 Desarrollo de Estrategia y Alineación con el Negocio · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 231 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** Gobernar la IA es decidir quién la usa, con qué datos, con qué autonomía y con qué evidencia.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** Gobernar la IA es decidir quién la usa, con qué datos, con qué autonomía y con qué evidencia. Esas cuatro decisiones son el núcleo de cualquier marco (AI RMF, ISO/IEC 42001) y, sin ellas, Copilot y los agentes se adoptan sin dueños ni límites. La tesis es que el gobierno de la IA no requiere un comité nuevo sino cuatro respuestas escritas y aplicadas por la plataforma y por las personas, integradas al SGSI existente.

**Tensión y límites.** La tensión es la velocidad de adopción frente a la lentitud del gobierno: los usuarios ya crean agentes mientras el comité discute la política. La respuesta es gobernar primero lo que la plataforma permite aplicar (entornos, conectores, DLP, identidad) y después el resto. Otra tensión es la duplicación de estructuras de gobierno (SGSI, privacidad, IA).

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: NIST AI RMF (GOVERN), ISO/IEC 42001, principios de IA responsable. Implementación: las cuatro respuestas para la flota del control (quién: PO-GAC con sponsor; datos: fuentes aprobadas vía Purview; autonomía: L0–L3 con apetito declarado; evidencia: trazas en Sentinel/Agent 365), aplicadas en Power Platform admin center y Copilot Control System.

**Evidencia y evaluación.** Evidencia: documento de principios de gobierno de IA del programa (dos páginas) y matriz de aplicación técnica. Se evalúa que cada principio tenga un control de plataforma o un control humano asignado.

**Puentes.** Extiende M6.2-K06 (Shadow AI); es la base de G2.1-PA02 (marcos) y G2.2-PA01 (política de agentes); se relaciona con AMP-30.

**Recomendaciones de práctica y ejercitación.**
1. Escribir las cuatro respuestas (quién, datos, autonomía, evidencia) para la flota del control.
2. Mapear cada respuesta a un control de plataforma o humano.
3. Inventariar quién puede crear agentes hoy y con qué conectores.

**Próximos pasos.**
- Derivar la política de agentes (G2.2-PA01).
- Mapear a AI RMF e ISO 42001 (G2.1-PA02).
- Revisar tras cambios de plataforma (AG-09).

**Relación con los conceptos de la(s) unidad(es) G1.2.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| G1.2-K01 | K | Estrategia de Ciberseguridad | misma unidad |
| G1.2-K02 | K | Alineación con Negocio | misma unidad |
| G1.2-K03 | K | Influencias y Tendencias | misma unidad |
| G1.2-K04 | K | Conexión de Valor | misma unidad |
| G1.2-K05 | K | Casos de Negocio | misma unidad |
| G1.2-K06 | K | ROI en Seguridad | misma unidad |
| G1.2-K07 | K | Visión de Negocio | misma unidad |
| G1.2-K08 | K | Planificación Estratégica | misma unidad |
| G1.2-K09 | K | Integración ERM | misma unidad |
| G1.2-K10 | K | Comunicación a la Junta | misma unidad |
| AMP-04 | AMP | Estrategia adaptativa | misma unidad |
| AMP-05 | AMP | Evolución contextual H | misma unidad |
| HC-006 | HC | Valor de seguridad y medición causal | misma unidad |
| HC-013 | HC | Deuda de seguridad como riesgo de transformación | misma unidad |
| HC-014 | HC | Arquitectura de riesgo empresarial | misma unidad |
| HC-023 | HC | Riesgo de concentración tecnológica | misma unidad |
| HC-034 | HC | Decisiones reversibles y riesgo de transición | misma unidad |
| HC-035 | HC | Aprendizaje desde incidentes hasta políticas | misma unidad |
| HC-039 | HC | Riesgo cibernético como narrativa empresarial | misma unidad |
| G1.2-PA01 | PA | Economía unitaria de agentes: caso de negocio y TCO | misma unidad |

**Pregunta generadora:** ¿Quién, en su organización, puede hoy crear un agente que lea correo corporativo, y qué lo detiene?

---

### 049. AMP-07 — NIST CSF 2.0 Govern

**Unidad:** G2.1 Selección e Integración de Marcos y Estándares · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 185 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** La función Govern del CSF 2.0 convierte el gobierno en resultados verificables —contexto organizacional, estrategia de riesgo, roles y autoridades, políticas, supervisión y cadena de suministro— en lugar de tratarlo como prerrequisito difuso de las otras funciones.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** La función Govern del CSF 2.0 convierte el gobierno en resultados verificables —contexto organizacional, estrategia de riesgo, roles y autoridades, políticas, supervisión y cadena de suministro— en lugar de tratarlo como prerrequisito difuso de las otras funciones. La tesis es que GV.OC, GV.RM, GV.RR, GV.PO, GV.OV y GV.SC son la lista de verificación mínima de un gobierno de seguridad operable y que cada una puede tener evidencia.

**Tensión y límites.** La tensión es que Govern puede leerse como burocracia (documentos) en vez de como resultados (decisiones tomadas, roles ejercidos, supervisión realizada). El ensayo debe distinguir el artefacto de la práctica y mostrar cómo auditar Govern por resultados.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: NIST CSF 2.0 (Govern y sus categorías). Implementación: fila GV de la grilla de ownership del control de correo (G2.1-PA01): para cada categoría, quién la ejerce, qué evidencia la demuestra y qué decisión produjo en el último trimestre.

**Evidencia y evaluación.** Evidencia: tabla GV con seis filas, responsable, evidencia y última decisión. Se evalúa que la evidencia sea de resultado y no de documento.

**Puentes.** Extiende G2.1-K04 (NIST CSF); se completa con G2.1-K11 (CSF 2.0 completo, V7); se relaciona con HC-015 y HC-038.

**Recomendaciones de práctica y ejercitación.**
1. Completar la fila GV de la grilla de ownership para el control de correo.
2. Para cada categoría, citar una decisión reciente y su evidencia.
3. Identificar la categoría de Govern sin dueño.

**Próximos pasos.**
- Extender a las 22 categorías con G2.1-K11.
- Alimentar el reporte ejecutivo con los resultados de Govern.
- Usar GV.SC para el anexo de proveedores (M1.2-PA02).

**Relación con los conceptos de la(s) unidad(es) G2.1.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| G2.1-K01 | K | Marcos de Gobierno | misma unidad |
| G2.1-K02 | K | COBIT | misma unidad |
| G2.1-K03 | K | ISO 27001 (SGSI) | misma unidad |
| G2.1-K04 | K | NIST CSF | misma unidad |
| G2.1-K05 | K | Estándares Relevantes | misma unidad |
| G2.1-K06 | K | Adaptación (Tailoring) | misma unidad |
| G2.1-K07 | K | Interoperabilidad | misma unidad |
| G2.1-K08 | K | Medición de Madurez | misma unidad |
| G2.1-K09 | K | Tendencias en Marcos | misma unidad |
| G2.1-K10 | K | Evolución Histórica | misma unidad |
| AMP-08 | AMP | Referencias informativas y no equivalencia | misma unidad |
| G2.1-K11 | K | CSF 2.0 completo: funciones, categorías y perfiles organizacionales | misma unidad |
| G2.1-PA01 | PA | Grilla de ownership: NIST CSF 2.0 × dominios Zero Trust | misma unidad |
| G2.1-PA02 | PA | Marcos de gobierno de IA aplicados: NIST AI RMF e ISO/IEC 42001 | misma unidad |

**Pregunta generadora:** Para cada categoría de Govern, ¿qué decisión concreta tomó su organización este trimestre, y quién la tomó?

---

### 050. AMP-08 — Referencias informativas y no equivalencia

**Unidad:** G2.1 Selección e Integración de Marcos y Estándares · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 177 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** Un mapeo entre marcos es una referencia informativa, no una equivalencia: indica dónde dos marcos hablan de lo mismo, no que cumplir uno cumple el otro.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** Un mapeo entre marcos es una referencia informativa, no una equivalencia: indica dónde dos marcos hablan de lo mismo, no que cumplir uno cumple el otro. Tratar los mapeos como homologación produce coberturas ilusorias: controles declarados cumplidos porque 'mapean' a algo implementado. La tesis es que todo mapeo debe declarar su nivel de correspondencia y que la conformidad solo se afirma con evidencia específica del marco destino.

**Tensión y límites.** La tensión es práctica: los mapeos ahorran trabajo y los auditores los aceptan; la tentación de usarlos como atajo es permanente. El ensayo debe proponer una disciplina mínima: nivel (fuerte, parcial, informativo), dirección y evidencia requerida.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: crosswalks (NIST OLIR, CSA CCM mappings). Implementación: la matriz de mapeo del GM-24 a NIST/ISACA/MITRE/OWASP/CIS/CSA de este proyecto, con niveles ●/◐/○ y vínculo (cubre/instancia/referencia); la matriz AGC × AI RMF × ISO 42001.

**Evidencia y evaluación.** Evidencia: revisión crítica de diez celdas de la matriz de mapeo: ¿cuáles son equivalencias reales y cuáles solo referencias? Se evalúa el rigor y la honestidad.

**Puentes.** Extiende G2.1-K07 (interoperabilidad); gobierna G2.1-PA02 y toda la matriz de estándares del programa.

**Recomendaciones de práctica y ejercitación.**
1. Revisar diez celdas de la matriz de mapeo y reclasificarlas por nivel de correspondencia.
2. Definir la regla de evidencia por nivel para el GRC.
3. Detectar en el GRC un control 'cumplido por mapeo' y verificarlo.

**Próximos pasos.**
- Aplicar la regla a la matriz AGC (G2.1-PA02).
- Documentar el nivel en cada mapeo del Atlas.
- Revisar cuando cambie la versión de un marco.

**Relación con los conceptos de la(s) unidad(es) G2.1.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| G2.1-K01 | K | Marcos de Gobierno | misma unidad |
| G2.1-K02 | K | COBIT | misma unidad |
| G2.1-K03 | K | ISO 27001 (SGSI) | misma unidad |
| G2.1-K04 | K | NIST CSF | misma unidad |
| G2.1-K05 | K | Estándares Relevantes | misma unidad |
| G2.1-K06 | K | Adaptación (Tailoring) | misma unidad |
| G2.1-K07 | K | Interoperabilidad | misma unidad |
| G2.1-K08 | K | Medición de Madurez | misma unidad |
| G2.1-K09 | K | Tendencias en Marcos | misma unidad |
| G2.1-K10 | K | Evolución Histórica | misma unidad |
| AMP-07 | AMP | NIST CSF 2.0 Govern | misma unidad |
| G2.1-K11 | K | CSF 2.0 completo: funciones, categorías y perfiles organizacionales | misma unidad |
| G2.1-PA01 | PA | Grilla de ownership: NIST CSF 2.0 × dominios Zero Trust | misma unidad |
| G2.1-PA02 | PA | Marcos de gobierno de IA aplicados: NIST AI RMF e ISO/IEC 42001 | misma unidad |

**Pregunta generadora:** ¿Cuántos controles de su organización están 'cumplidos' solo porque un mapeo dice que otro control equivalente lo está?

---

### 051. AMP-09 — Policy-as-code

**Unidad:** G2.2 Ciclo de Vida de Políticas, Estándares y Procedimientos · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 194 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** Expresar políticas como código —configuraciones declarativas, baselines, reglas evaluables— vuelve verificable su aplicación: se puede comprobar en cualquier momento si el estado real coincide con el declarado.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** Expresar políticas como código —configuraciones declarativas, baselines, reglas evaluables— vuelve verificable su aplicación: se puede comprobar en cualquier momento si el estado real coincide con el declarado. Pero policy-as-code exige lo que todo código exige: control de versiones, gestión de excepciones y revisión humana para cambios de alto impacto. La tesis es que la política escrita en prosa y la política aplicada en configuración deben ser el mismo objeto gobernado.

**Tensión y límites.** La tensión es que la configuración vive en consolas y la política en documentos; quien cambia una no cambia la otra. Otra tensión es la ilusión de que todo se puede codificar: la autoridad, las prohibiciones y las excepciones siguen necesitando texto y firma.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: policy-as-code, configuration management, GitOps. Implementación: presets Standard/Strict de Defender for Office 365 como baseline versionado, Configuration Analyzer como verificación, políticas de Power Platform (DLP, conectores) como aplicación de la política de agentes; ChangeSets para cambios.

**Evidencia y evaluación.** Evidencia: baseline versionado del control con historial de cambios y procedimiento de revisión para cambios de alto impacto. Se evalúa la trazabilidad entre texto normativo y configuración.

**Puentes.** Se apoya en HC-004 (políticas y configuración) y G2.2-K03; sostiene G2.2-PA03 (baseline, excepciones) y G3.2-PA01 (deriva).

**Recomendaciones de práctica y ejercitación.**
1. Versionar el baseline de Defender for Office 365 (exportar configuración, Git) y definir la revisión por tipo de cambio.
2. Mapear tres reglas de la política de agentes a políticas de Power Platform.
3. Ejecutar Configuration Analyzer y conciliar con el baseline versionado.

**Próximos pasos.**
- Integrar con el control continuo de deriva (G3.2-PA01).
- Conectar con el ALM de agentes (M6.2-PA02).
- Revisar la política en prosa cuando cambie el baseline.

**Relación con los conceptos de la(s) unidad(es) G2.2.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| G2.2-K01 | K | Jerarquía Documental | misma unidad |
| G2.2-K02 | K | Desarrollo de Políticas | misma unidad |
| G2.2-K03 | K | Estándares de Seguridad | misma unidad |
| G2.2-K04 | K | Procedimientos | misma unidad |
| G2.2-K05 | K | Comunicación | misma unidad |
| G2.2-K06 | K | Aplicación (Enforcement) | misma unidad |
| G2.2-K07 | K | Mantenimiento | misma unidad |
| G2.2-K08 | K | Control de Versiones | misma unidad |
| G2.2-K09 | K | Excepciones | misma unidad |
| G2.2-K10 | K | Rol de Auditoría | misma unidad |
| AMP-10 | AMP | Gobierno de excepciones automatizadas | misma unidad |
| HC-004 | HC | Política como código gobernado | misma unidad |
| HC-013 | HC | Deuda de seguridad como riesgo de transformación | misma unidad |
| HC-015 | HC | Gobierno y operación de Zero Trust | misma unidad |
| HC-028 | HC | Gestión de excepciones y compensaciones | misma unidad |
| HC-035 | HC | Aprendizaje desde incidentes hasta políticas | misma unidad |
| HC-038 | HC | Aseguramiento de la arquitectura Zero Trust | misma unidad |
| G2.2-PA01 | PA | Política de uso y gobierno de agentes | misma unidad |
| G2.2-PA02 | PA | Estándar de ficha de agente (charter) y runbooks de agentes | misma unidad |
| G2.2-PA03 | PA | Baseline, excepciones y overrides de un control técnico | misma unidad |

**Pregunta generadora:** Si alguien cambiara hoy una política de correo en la consola, ¿qué documento quedaría desactualizado y quién lo notaría?

---

### 052. AMP-10 — Gobierno de excepciones automatizadas

**Unidad:** G2.2 Ciclo de Vida de Políticas, Estándares y Procedimientos · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 186 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** Cuando las excepciones se conceden y vencen automáticamente —entradas de permiso, overrides, reglas de bypass— la automatización puede normalizar el desvío: lo excepcional se vuelve permanente porque nadie vuelve a mirar.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** Cuando las excepciones se conceden y vencen automáticamente —entradas de permiso, overrides, reglas de bypass— la automatización puede normalizar el desvío: lo excepcional se vuelve permanente porque nadie vuelve a mirar. La tesis es que toda excepción automatizada necesita dueño, caducidad y evidencia de la razón, y que el informe de excepciones vigentes es un control de gobierno, no un detalle administrativo.

**Tensión y límites.** La tensión es operativa: las excepciones resuelven problemas reales bajo presión y su revisión no tiene urgencia. Otra tensión es la escala: cientos de entradas no se revisan a mano; la caducidad por defecto y el agente auditor (AG-11) son la respuesta.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: gestión de excepciones, caducidad por defecto, revisión periódica. Implementación: Tenant Allow/Block List con vencimiento obligatorio, informe de overrides mensual (MDO-M02), registro de excepciones en Dataverse con dueño y justificación, KPI-07 (overrides sin justificación = 0).

**Evidencia y evaluación.** Evidencia: registro de excepciones del control con dueño, caducidad y justificación; informe mensual con excepciones vencidas y depuradas. Se evalúa que ninguna excepción carezca de fecha ni dueño.

**Puentes.** Se apoya en HC-028 (excepciones y compensaciones); sostiene G2.2-PA03 y el agente AG-11; se relaciona con AMP-09.

**Recomendaciones de práctica y ejercitación.**
1. Inventariar las excepciones vigentes del control y clasificarlas por antigüedad y justificación.
2. Definir la regla de caducidad por defecto y el flujo de renovación.
3. Diseñar el informe mensual de excepciones (MDO-M02) y su KPI.

**Próximos pasos.**
- Asignar AG-11 como auditor de overrides.
- Conectar con el registro de riesgos (excepciones como riesgo aceptado).
- Revisar la regla en la revisión trimestral de políticas (MDO-Q01).

**Relación con los conceptos de la(s) unidad(es) G2.2.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| G2.2-K01 | K | Jerarquía Documental | misma unidad |
| G2.2-K02 | K | Desarrollo de Políticas | misma unidad |
| G2.2-K03 | K | Estándares de Seguridad | misma unidad |
| G2.2-K04 | K | Procedimientos | misma unidad |
| G2.2-K05 | K | Comunicación | misma unidad |
| G2.2-K06 | K | Aplicación (Enforcement) | misma unidad |
| G2.2-K07 | K | Mantenimiento | misma unidad |
| G2.2-K08 | K | Control de Versiones | misma unidad |
| G2.2-K09 | K | Excepciones | misma unidad |
| G2.2-K10 | K | Rol de Auditoría | misma unidad |
| AMP-09 | AMP | Policy-as-code | misma unidad |
| HC-004 | HC | Política como código gobernado | misma unidad |
| HC-013 | HC | Deuda de seguridad como riesgo de transformación | misma unidad |
| HC-015 | HC | Gobierno y operación de Zero Trust | misma unidad |
| HC-028 | HC | Gestión de excepciones y compensaciones | misma unidad |
| HC-035 | HC | Aprendizaje desde incidentes hasta políticas | misma unidad |
| HC-038 | HC | Aseguramiento de la arquitectura Zero Trust | misma unidad |
| G2.2-PA01 | PA | Política de uso y gobierno de agentes | misma unidad |
| G2.2-PA02 | PA | Estándar de ficha de agente (charter) y runbooks de agentes | misma unidad |
| G2.2-PA03 | PA | Baseline, excepciones y overrides de un control técnico | misma unidad |

**Pregunta generadora:** ¿Cuántas excepciones vigentes en su control de correo tienen más de un año, y cuántas recuerda alguien por qué existen?

---

### 053. AMP-11 — Soberanía de datos

**Unidad:** G3.1 Requisitos Legales, Regulatorios y Contractuales · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 190 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** La soberanía de datos es una restricción de diseño, no un trámite posterior: ubicación, jurisdicción, control de claves y acceso de terceros se deciden antes de desplegar IA, porque después el costo de cambiarlos es prohibitivo.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** La soberanía de datos es una restricción de diseño, no un trámite posterior: ubicación, jurisdicción, control de claves y acceso de terceros se deciden antes de desplegar IA, porque después el costo de cambiarlos es prohibitivo. Con agentes que recuperan datos de múltiples fuentes y los envían a modelos, la pregunta '¿dónde se procesa y bajo qué ley?' se multiplica por cada conector. La tesis es que el owner debe poder responderla para cada agente.

**Tensión y límites.** La tensión es entre soberanía y capacidad: los mejores modelos y servicios pueden no estar en la región; la restricción cuesta funcionalidad o dinero. El ensayo debe mostrar cómo decidir con criterios explícitos y cómo documentar la decisión para auditoría.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: residencia de datos, jurisdicción, gestión de claves (BYOK/HYOK), transferencias internacionales. Implementación: checklist de soberanía por agente (región de Foundry, residencia de Copilot Studio, claves en Purview/Key Vault, subprocesadores), aplicada a los quince agentes.

**Evidencia y evaluación.** Evidencia: checklist completada para la flota con decisiones y excepciones documentadas. Se evalúa la trazabilidad de cada decisión a un requisito legal o contractual.

**Puentes.** Se apoya en HC-033 (soberanía y transferencias); se relaciona con AMP-12 y G3.1-PA01; alimenta M6.2-PA01 (rutas).

**Recomendaciones de práctica y ejercitación.**
1. Completar la checklist de soberanía para los 15 agentes.
2. Identificar los conectores que mueven datos fuera de la jurisdicción.
3. Documentar la decisión de región y claves para Foundry y Copilot Studio.

**Próximos pasos.**
- Incluirla en el expediente ATO (AMP-22).
- Revisar ante cambios de región o de proveedor.
- Conectar con el anexo contractual (M1.2-PA02).

**Relación con los conceptos de la(s) unidad(es) G3.1.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| G3.1-K01 | K | Identificación de Requisitos | misma unidad |
| G3.1-K02 | K | Leyes de Privacidad | misma unidad |
| G3.1-K03 | K | Regulaciones Sectoriales | misma unidad |
| G3.1-K04 | K | Obligaciones Contractuales | misma unidad |
| G3.1-K05 | K | Implicaciones CISO | misma unidad |
| G3.1-K06 | K | Gestión de Privacidad | misma unidad |
| G3.1-K07 | K | Cumplimiento Integrado | misma unidad |
| G3.1-K08 | K | Riesgos Legales | misma unidad |
| G3.1-K09 | K | Auditorías de Cumplimiento | misma unidad |
| G3.1-K10 | K | Responsabilidad Legal | misma unidad |
| AMP-12 | AMP | Responsabilidad por agentes | misma unidad |
| HC-005 | HC | Cumplimiento continuo orientado a resultados | misma unidad |
| HC-008 | HC | Cadena de confianza en terceros | misma unidad |
| HC-011 | HC | Seguridad de datos en la IA empresarial | misma unidad |
| HC-024 | HC | Cumplimiento y privacidad por diseño | misma unidad |
| HC-029 | HC | Aseguramiento de terceros y cadena de suministro | misma unidad |
| HC-033 | HC | Seguridad y soberanía de datos distribuidos | misma unidad |
| G3.1-PA01 | PA | Panorama regulatorio de IA y agentes | misma unidad |

**Pregunta generadora:** ¿En qué región se procesa hoy el contenido de correo que lee su agente de triaje, y quién lo decidió?

---

### 054. AMP-12 — Responsabilidad por agentes

**Unidad:** G3.1 Requisitos Legales, Regulatorios y Contractuales · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 208 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** Cuando un agente actúa, la responsabilidad no se transfiere al software: debe existir un dueño identificable, límites contractuales claros cuando el agente es de un tercero y trazabilidad de lo actuado para poder atribuir.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** Cuando un agente actúa, la responsabilidad no se transfiere al software: debe existir un dueño identificable, límites contractuales claros cuando el agente es de un tercero y trazabilidad de lo actuado para poder atribuir. La tesis es que la responsabilidad por agentes se construye con tres piezas —dueño, contrato, traza— y que la ausencia de cualquiera deja a la organización sin posibilidad de responder ante un regulador, un cliente o un tribunal.

**Tensión y límites.** La tensión es la cadena de proveedores: modelo de un proveedor, plataforma de otro, agente construido por un integrador, operado por el cliente. La responsabilidad se reparte contractualmente pero la accountability ante el afectado no. El ensayo debe discutir qué cláusulas mínimas y qué evidencia necesita la organización para no quedar sola.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: responsabilidad civil y contractual, TPRM, principios de IA responsable. Implementación: cláusulas tipo para contratos de MDR con agentes y para plataformas (identidad propia del agente del proveedor, límites, trazas entregadas, derecho a desactivar), sponsor en Entra Agent ID, trazas en Sentinel.

**Evidencia y evaluación.** Evidencia: cláusulas tipo revisadas por Legal y verificación de trazabilidad para un agente de terceros. Se evalúa la completitud de las tres piezas.

**Puentes.** Se apoya en HC-009 (identidades no humanas) y AMP-03; sostiene M1.2-PA02 (contratos) y AGC-02; se relaciona con G3.1-PA01.

**Recomendaciones de práctica y ejercitación.**
1. Redactar las cláusulas tipo (identidad, límites, trazas, desactivación) para agentes de terceros.
2. Verificar la trazabilidad de un agente provisto por un tercero hasta el nivel de acción.
3. Recorrer un caso hipotético con Legal: quién responde ante quién.

**Próximos pasos.**
- Incorporar las cláusulas al anexo RFP (M1.2-PA02).
- Registrar a los agentes de terceros en el inventario (M2.1-PA01).
- Revisar anualmente con Legal.

**Relación con los conceptos de la(s) unidad(es) G3.1.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| G3.1-K01 | K | Identificación de Requisitos | misma unidad |
| G3.1-K02 | K | Leyes de Privacidad | misma unidad |
| G3.1-K03 | K | Regulaciones Sectoriales | misma unidad |
| G3.1-K04 | K | Obligaciones Contractuales | misma unidad |
| G3.1-K05 | K | Implicaciones CISO | misma unidad |
| G3.1-K06 | K | Gestión de Privacidad | misma unidad |
| G3.1-K07 | K | Cumplimiento Integrado | misma unidad |
| G3.1-K08 | K | Riesgos Legales | misma unidad |
| G3.1-K09 | K | Auditorías de Cumplimiento | misma unidad |
| G3.1-K10 | K | Responsabilidad Legal | misma unidad |
| AMP-11 | AMP | Soberanía de datos | misma unidad |
| HC-005 | HC | Cumplimiento continuo orientado a resultados | misma unidad |
| HC-008 | HC | Cadena de confianza en terceros | misma unidad |
| HC-011 | HC | Seguridad de datos en la IA empresarial | misma unidad |
| HC-024 | HC | Cumplimiento y privacidad por diseño | misma unidad |
| HC-029 | HC | Aseguramiento de terceros y cadena de suministro | misma unidad |
| HC-033 | HC | Seguridad y soberanía de datos distribuidos | misma unidad |
| G3.1-PA01 | PA | Panorama regulatorio de IA y agentes | misma unidad |

**Pregunta generadora:** Si el agente de su proveedor removiera correo legítimo de un ejecutivo, ¿qué cláusula se aplicaría y qué traza tendría usted para demostrarlo?

---

### 055. AMP-13 — Evidencia continua

**Unidad:** G3.2 Gestión del Cumplimiento y Aseguramiento Continuo · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 191 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** El aseguramiento moderno se apoya en evidencia continua generada por los propios controles —informes automáticos, logs, estados de configuración— pero su valor depende de tres atributos: alcance (qué cubre y qué no), integridad (que nadie la haya alterado) y responsable (quién responde por ella).

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** El aseguramiento moderno se apoya en evidencia continua generada por los propios controles —informes automáticos, logs, estados de configuración— pero su valor depende de tres atributos: alcance (qué cubre y qué no), integridad (que nadie la haya alterado) y responsable (quién responde por ella). La tesis es que la evidencia continua no reemplaza al aseguramiento sino que cambia su objeto: ya no se audita el control, se audita la evidencia y su cadena.

**Tensión y límites.** La tensión es la abundancia: miles de registros que nadie lee producen una falsa sensación de control. Otra tensión es la circularidad: el control genera la evidencia de su propio funcionamiento; sin verificación independiente, un control roto puede reportar que funciona.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: continuous controls monitoring, cadena de custodia de evidencia, integridad de logs. Implementación: inventario de evidencias continuas del control (Configuration Analyzer, informes de protección, logs de agentes en Sentinel, Purview Audit) con alcance, integridad (retención inmutable) y responsable.

**Evidencia y evaluación.** Evidencia: inventario de evidencias continuas con los tres atributos y una prueba de integridad. Se evalúa la identificación de evidencias circulares y su compensación.

**Puentes.** Extiende G3.2-K02 (aseguramiento continuo); sostiene G3.2-PA01 y AGC-11; se relaciona con AMP-46 y HC-005.

**Recomendaciones de práctica y ejercitación.**
1. Inventariar las evidencias continuas del control con alcance, integridad y responsable.
2. Identificar evidencias circulares y proponer la verificación independiente.
3. Probar la integridad de una fuente de evidencia (retención, inmutabilidad).

**Próximos pasos.**
- Conectar con la auditoría interna (AGC-22).
- Usar el inventario en el expediente ATO.
- Mapear a ISO 27001/42001 (HC-005).

**Relación con los conceptos de la(s) unidad(es) G3.2.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| G3.2-K01 | K | Procesos de Gestión | misma unidad |
| G3.2-K02 | K | Aseguramiento Continuo | misma unidad |
| G3.2-K03 | K | Supervisión de Auditorías | misma unidad |
| G3.2-K04 | K | Reporte de Incumplimiento | misma unidad |
| G3.2-K05 | K | Estrategias Proactivas | misma unidad |
| G3.2-K06 | K | Gestión de Evidencia | misma unidad |
| G3.2-K07 | K | Automatización | misma unidad |
| G3.2-K08 | K | KPIs de Cumplimiento | misma unidad |
| G3.2-K09 | K | Formación en Cumplimiento | misma unidad |
| G3.2-K10 | K | Relación con Reguladores | misma unidad |
| AMP-14 | AMP | Aseguramiento de decisiones de IA | misma unidad |
| HC-003 | HC | Riesgo residual y aceptación verificable | misma unidad |
| HC-004 | HC | Política como código gobernado | misma unidad |
| HC-005 | HC | Cumplimiento continuo orientado a resultados | misma unidad |
| HC-012 | HC | Confianza verificable en decisiones de IA | misma unidad |
| HC-018 | HC | Observabilidad y aseguramiento de controles | misma unidad |
| HC-024 | HC | Cumplimiento y privacidad por diseño | misma unidad |
| HC-029 | HC | Aseguramiento de terceros y cadena de suministro | misma unidad |
| G3.2-PA01 | PA | Aseguramiento continuo de la configuración del control (deriva) | misma unidad |

**Pregunta generadora:** De las evidencias que su control produce automáticamente, ¿cuál podría estar diciendo que todo funciona mientras el control está roto?

---

### 056. AMP-14 — Aseguramiento de decisiones de IA

**Unidad:** G3.2 Gestión del Cumplimiento y Aseguramiento Continuo · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 188 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** Afirmar que una decisión asistida por IA es confiable exige pruebas, registros y revisión independiente, no solo métricas de desempeño del modelo.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** Afirmar que una decisión asistida por IA es confiable exige pruebas, registros y revisión independiente, no solo métricas de desempeño del modelo. Una precisión del 92 % no dice nada sobre los casos en que el modelo se equivoca con seguridad ni sobre si el humano que revisa realmente revisa. La tesis es que el aseguramiento de decisiones de IA combina evaluación del sistema, trazabilidad de cada decisión y una tercera línea que muestrea.

**Tensión y límites.** La tensión es que las métricas del modelo son fáciles de obtener y las otras dos piezas son caras. También está la opacidad: no siempre se puede explicar por qué el modelo decidió. El ensayo debe mostrar qué nivel de aseguramiento corresponde a cada nivel de autonomía.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: AI RMF MEASURE, auditoría de algoritmos, muestreo estadístico. Implementación: para AG-01, combinar evaluación con dataset dorado (M3.2-PA03), trazas por decisión (AMP-46) y muestreo trimestral independiente por la segunda línea.

**Evidencia y evaluación.** Evidencia: plan de aseguramiento de decisiones para un agente con las tres piezas y el primer muestreo. Se evalúa la independencia del muestreo.

**Puentes.** Se apoya en HC-012 (confianza verificable); se relaciona con M3.2-PA03, AMP-46 y G4.1-PA01.

**Recomendaciones de práctica y ejercitación.**
1. Diseñar el plan de aseguramiento de decisiones de AG-01 (evaluación, trazas, muestreo).
2. Ejecutar un muestreo de 30 decisiones por alguien ajeno al equipo.
3. Comparar la precisión declarada con la precisión observada en el muestreo.

**Próximos pasos.**
- Institucionalizar el muestreo en la revisión trimestral (M4.1-PA06).
- Entregar resultados a auditoría (AGC-22).
- Ajustar el nivel de autonomía según resultados.

**Relación con los conceptos de la(s) unidad(es) G3.2.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| G3.2-K01 | K | Procesos de Gestión | misma unidad |
| G3.2-K02 | K | Aseguramiento Continuo | misma unidad |
| G3.2-K03 | K | Supervisión de Auditorías | misma unidad |
| G3.2-K04 | K | Reporte de Incumplimiento | misma unidad |
| G3.2-K05 | K | Estrategias Proactivas | misma unidad |
| G3.2-K06 | K | Gestión de Evidencia | misma unidad |
| G3.2-K07 | K | Automatización | misma unidad |
| G3.2-K08 | K | KPIs de Cumplimiento | misma unidad |
| G3.2-K09 | K | Formación en Cumplimiento | misma unidad |
| G3.2-K10 | K | Relación con Reguladores | misma unidad |
| AMP-13 | AMP | Evidencia continua | misma unidad |
| HC-003 | HC | Riesgo residual y aceptación verificable | misma unidad |
| HC-004 | HC | Política como código gobernado | misma unidad |
| HC-005 | HC | Cumplimiento continuo orientado a resultados | misma unidad |
| HC-012 | HC | Confianza verificable en decisiones de IA | misma unidad |
| HC-018 | HC | Observabilidad y aseguramiento de controles | misma unidad |
| HC-024 | HC | Cumplimiento y privacidad por diseño | misma unidad |
| HC-029 | HC | Aseguramiento de terceros y cadena de suministro | misma unidad |
| G3.2-PA01 | PA | Aseguramiento continuo de la configuración del control (deriva) | misma unidad |

**Pregunta generadora:** ¿Qué sabe hoy de las decisiones de su asistente de triaje además de su tasa de acierto?

---

### 057. AMP-15 — Riesgo sistémico

**Unidad:** G4.1 Gobernanza del Riesgo: Marcos y Estructuras · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 182 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** Los riesgos que se propagan por dependencias compartidas —identidad, nube, proveedores, modelos— no se gobiernan activo por activo sino a nivel de ecosistema: una falla en el proveedor de identidad o en el modelo que usan todos los agentes afecta a todo a la vez.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** Los riesgos que se propagan por dependencias compartidas —identidad, nube, proveedores, modelos— no se gobiernan activo por activo sino a nivel de ecosistema: una falla en el proveedor de identidad o en el modelo que usan todos los agentes afecta a todo a la vez. La tesis es que el registro de riesgos debe incluir riesgos sistémicos con su mapa de dependencias y que el apetito debe fijar límites de concentración.

**Tensión y límites.** La tensión es que el riesgo sistémico es difícil de cuantificar y fácil de ignorar porque 'nunca pasó'. Otra tensión es que la concentración suele ser racional (un proveedor, un modelo) y la diversificación cuesta. El ensayo debe argumentar cómo decidir cuánta concentración aceptar.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: riesgo sistémico, análisis de dependencias, concentración. Implementación: mapa de dependencias de la flota (Copilot Studio, Foundry, Entra, Sentinel, modelos) y fila de riesgo sistémico en el registro con KRI de concentración.

**Evidencia y evaluación.** Evidencia: mapa de dependencias y registro con al menos un riesgo sistémico tratado. Se evalúa la identificación de puntos únicos de falla.

**Puentes.** Se apoya en HC-023 (concentración); se relaciona con AMP-48, M6.1-PA01 y G4.1-PA02.

**Recomendaciones de práctica y ejercitación.**
1. Dibujar el mapa de dependencias compartidas de la flota.
2. Registrar el riesgo sistémico con KRI de concentración y tratamiento.
3. Simular la caída de una dependencia y medir el alcance.

**Próximos pasos.**
- Vincular con la operación degradada (M6.1-PA01).
- Revisar el apetito de concentración con el comité.
- Actualizar al incorporar proveedores.

**Relación con los conceptos de la(s) unidad(es) G4.1.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| G4.1-K01 | K | Enfoque Organizacional | misma unidad |
| G4.1-K02 | K | Integración ERM | misma unidad |
| G4.1-K03 | K | Tres Líneas de Defensa | misma unidad |
| G4.1-K04 | K | Gestión Avanzada | misma unidad |
| G4.1-K05 | K | Marcos de Riesgo | misma unidad |
| G4.1-K06 | K | Evaluación Organizacional | misma unidad |
| G4.1-K07 | K | Enfoque en Negocio | misma unidad |
| G4.1-K08 | K | Roles y Responsabilidades | misma unidad |
| G4.1-K09 | K | Supervisión | misma unidad |
| G4.1-K10 | K | Reporte a Dirección | misma unidad |
| AMP-16 | AMP | Homeostasis y fuerzas de cambio | misma unidad |
| HC-009 | HC | Gobierno de identidades no humanas | misma unidad |
| HC-014 | HC | Arquitectura de riesgo empresarial | misma unidad |
| HC-022 | HC | Gobierno de crisis multidisciplinario | misma unidad |
| G4.1-PA01 | PA | Tres líneas de defensa para la flota de agentes | misma unidad |
| G4.1-PA02 | PA | Taxonomía y registro de riesgos de agentes | misma unidad |

**Pregunta generadora:** Si su proveedor de identidad fallara una hora, ¿cuántos de sus agentes y controles seguirían funcionando?

---

### 058. AMP-16 — Homeostasis y fuerzas de cambio

**Unidad:** G4.1 Gobernanza del Riesgo: Marcos y Estructuras · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 176 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** Toda organización tiende a volver a su equilibrio: los cambios de seguridad que no se anclan en estructuras, incentivos y rutinas se revierten solos.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** Toda organización tiende a volver a su equilibrio: los cambios de seguridad que no se anclan en estructuras, incentivos y rutinas se revierten solos. Comprender qué fuerzas sostienen el estado actual y cuáles empujan el cambio permite diseñar transformaciones que perduren. La tesis es que el CISO debe diseñar la estabilización —rituales, métricas, roles— con el mismo cuidado que el cambio.

**Tensión y límites.** La tensión es que la estabilización parece burocracia y el cambio parece progreso; los equipos celebran el despliegue y abandonan el mantenimiento (M1.1-K05). Otra tensión es que algunas fuerzas homeostáticas son saludables: protegen de modas. El ensayo debe distinguirlas.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: análisis de campo de fuerzas, gestión del cambio, aprendizaje organizacional. Implementación: para la adopción del modelo operativo y de los agentes, identificar las fuerzas que lo revertirían (presión por liberar correo, rotación, costo) y los mecanismos que lo estabilizan (cadencias, KPIs, revisión trimestral).

**Evidencia y evaluación.** Evidencia: análisis de fuerzas de la transformación agéntica con mecanismos de estabilización diseñados. Se evalúa el realismo.

**Puentes.** Se apoya en HC-040 (dinámica organizacional); se relaciona con AMP-05 y AMP-30; sostiene M1.1-PA03.

**Recomendaciones de práctica y ejercitación.**
1. Analizar las fuerzas que revertirían la adopción del modelo operativo y de la flota.
2. Diseñar tres mecanismos de estabilización (ritual, métrica, rol).
3. Revisar una práctica abandonada y explicar su reversión.

**Próximos pasos.**
- Incorporar los mecanismos al sub-plan (etapa E5).
- Medir la estabilización en la revisión trimestral.
- Conectar con la cultura (G1.1-K05).

**Relación con los conceptos de la(s) unidad(es) G4.1.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| G4.1-K01 | K | Enfoque Organizacional | misma unidad |
| G4.1-K02 | K | Integración ERM | misma unidad |
| G4.1-K03 | K | Tres Líneas de Defensa | misma unidad |
| G4.1-K04 | K | Gestión Avanzada | misma unidad |
| G4.1-K05 | K | Marcos de Riesgo | misma unidad |
| G4.1-K06 | K | Evaluación Organizacional | misma unidad |
| G4.1-K07 | K | Enfoque en Negocio | misma unidad |
| G4.1-K08 | K | Roles y Responsabilidades | misma unidad |
| G4.1-K09 | K | Supervisión | misma unidad |
| G4.1-K10 | K | Reporte a Dirección | misma unidad |
| AMP-15 | AMP | Riesgo sistémico | misma unidad |
| HC-009 | HC | Gobierno de identidades no humanas | misma unidad |
| HC-014 | HC | Arquitectura de riesgo empresarial | misma unidad |
| HC-022 | HC | Gobierno de crisis multidisciplinario | misma unidad |
| G4.1-PA01 | PA | Tres líneas de defensa para la flota de agentes | misma unidad |
| G4.1-PA02 | PA | Taxonomía y registro de riesgos de agentes | misma unidad |

**Pregunta generadora:** ¿Qué práctica de seguridad introdujo su equipo hace un año que ya nadie hace, y qué fuerza la deshizo?

---

### 059. AMP-17 — Autoridad delegada

**Unidad:** G4.2 Definición y Comunicación del Apetito de Riesgo · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 198 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** Delegar autoridad en sistemas autónomos es una decisión de apetito de riesgo: qué acciones puede ejecutar el agente, con qué límites, bajo qué supervisión y quién puede revocar la delegación.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** Delegar autoridad en sistemas autónomos es una decisión de apetito de riesgo: qué acciones puede ejecutar el agente, con qué límites, bajo qué supervisión y quién puede revocar la delegación. No es una decisión técnica del constructor sino una decisión de gobierno del dueño del riesgo. La tesis es que el apetito de autonomía debe declararse por tipo de acción (reversible/irreversible, impacto, alcance) antes de construir el agente.

**Tensión y límites.** La tensión es que el apetito se expresa en términos de negocio y la autonomía en términos técnicos; traducir uno a otro es el trabajo del owner. Otra tensión es la deriva: la autonomía se amplía 'porque funciona' sin volver a pasar por el dueño del riesgo.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: apetito de riesgo (ISO 31000), derechos de decisión, delegación. Implementación: declaración de apetito de autonomía del control de correo (qué puede hacer un agente en L1, L2, L3; qué nunca), firmada por el dueño del riesgo; registrada como DD18 (referencia interna).

**Evidencia y evaluación.** Evidencia: declaración de apetito de autonomía aprobada y aplicada a los quince agentes. Se evalúa que cada agente tenga nivel coherente con la declaración.

**Puentes.** Se apoya en HC-010 (capacidad, permiso, delegación, ejecución); se concreta en AMP-18; sostiene AGC-04 y G4.2-PA01.

**Recomendaciones de práctica y ejercitación.**
1. Redactar la declaración de apetito de autonomía por tipo de acción.
2. Clasificar los 15 agentes contra la declaración y detectar incoherencias.
3. Definir el procedimiento para ampliar autonomía (quién, con qué evidencia).

**Próximos pasos.**
- Operacionalizar en límites (AMP-18) y KRIs (G4.2-PA01).
- Incluir en el expediente ATO.
- Revisar en MDO-Q01.

**Relación con los conceptos de la(s) unidad(es) G4.2.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| G4.2-K01 | K | Apetito de Riesgo | misma unidad |
| G4.2-K02 | K | Tolerancia al Riesgo | misma unidad |
| G4.2-K03 | K | Documentación | misma unidad |
| G4.2-K04 | K | Comunicación | misma unidad |
| G4.2-K05 | K | Rol Ejecutivo | misma unidad |
| G4.2-K06 | K | Impacto en Estrategia | misma unidad |
| G4.2-K07 | K | Talleres de Definición | misma unidad |
| G4.2-K08 | K | Relación Apetito-Residual | misma unidad |
| G4.2-K09 | K | Métricas de Apetito | misma unidad |
| G4.2-K10 | K | Aceptación Formal | misma unidad |
| AMP-18 | AMP | Límites de autonomía | misma unidad |
| HC-002 | HC | Apetito de riesgo convertido en arquitectura | misma unidad |
| HC-003 | HC | Riesgo residual y aceptación verificable | misma unidad |
| HC-007 | HC | Resiliencia gobernada por impacto | misma unidad |
| HC-010 | HC | Autonomía delegada y límites de acción | misma unidad |
| HC-027 | HC | Métricas que no engañan | misma unidad |
| HC-040 | HC | Homeostasis organizacional de seguridad | misma unidad |
| G4.2-PA01 | PA | KRIs de la flota de agentes y umbrales de intervención | misma unidad |

**Pregunta generadora:** ¿Qué acción de su SOC jamás permitiría que un agente ejecute sin aprobación, y está escrito?

---

### 060. AMP-18 — Límites de autonomía

**Unidad:** G4.2 Definición y Comunicación del Apetito de Riesgo · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 178 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** Los límites de autonomía —acciones permitidas, umbrales, aprobaciones requeridas y mecanismo de detención— traducen el apetito de riesgo en reglas operables para agentes.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** Los límites de autonomía —acciones permitidas, umbrales, aprobaciones requeridas y mecanismo de detención— traducen el apetito de riesgo en reglas operables para agentes. Sin ellos el apetito es una declaración; con ellos es configuración. La tesis es que los límites deben ser verificables en la plataforma (permisos de conectores, aprobaciones, cuotas, kill switch) y medibles con indicadores (KRIs) que avisen antes de la transgresión.

**Tensión y límites.** La tensión es la granularidad: la plataforma no siempre permite el límite exacto que el apetito pide; hay que compensar con aprobación humana o con alcance reducido. Otra tensión es la rigidez: límites demasiado estrictos hacen inútil al agente.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: control de acceso, cuotas, circuit breakers, HITL. Implementación: escala L0–L4 del sub-plan con árbol de decisión; permisos de conectores en Power Platform, Approvals para L2, límites de lote, kill switch en PPAC/Agent 365; KRIs en Sentinel.

**Evidencia y evaluación.** Evidencia: ficha de límites por agente con verificación en plataforma y KRI asociado. Se evalúa que cada límite declarado sea comprobable.

**Puentes.** Se apoya en HC-010 y AMP-17; sostiene AGC-04, AGC-09, AGC-10 y G4.2-PA01; se relaciona con AMP-44.

**Recomendaciones de práctica y ejercitación.**
1. Definir los límites de AG-02 y AG-03 (acciones, umbrales, aprobaciones, detención) y verificarlos en la plataforma.
2. Aplicar el árbol de decisión L0–L4 a las 31 tareas del modelo operativo.
3. Probar el kill switch de un agente y medir el tiempo.

**Próximos pasos.**
- Derivar los KRIs (G4.2-PA01).
- Documentar los límites en la ficha (G2.2-PA02).
- Revisar límites en cada revisión de desempeño.

**Relación con los conceptos de la(s) unidad(es) G4.2.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| G4.2-K01 | K | Apetito de Riesgo | misma unidad |
| G4.2-K02 | K | Tolerancia al Riesgo | misma unidad |
| G4.2-K03 | K | Documentación | misma unidad |
| G4.2-K04 | K | Comunicación | misma unidad |
| G4.2-K05 | K | Rol Ejecutivo | misma unidad |
| G4.2-K06 | K | Impacto en Estrategia | misma unidad |
| G4.2-K07 | K | Talleres de Definición | misma unidad |
| G4.2-K08 | K | Relación Apetito-Residual | misma unidad |
| G4.2-K09 | K | Métricas de Apetito | misma unidad |
| G4.2-K10 | K | Aceptación Formal | misma unidad |
| AMP-17 | AMP | Autoridad delegada | misma unidad |
| HC-002 | HC | Apetito de riesgo convertido en arquitectura | misma unidad |
| HC-003 | HC | Riesgo residual y aceptación verificable | misma unidad |
| HC-007 | HC | Resiliencia gobernada por impacto | misma unidad |
| HC-010 | HC | Autonomía delegada y límites de acción | misma unidad |
| HC-027 | HC | Métricas que no engañan | misma unidad |
| HC-040 | HC | Homeostasis organizacional de seguridad | misma unidad |
| G4.2-PA01 | PA | KRIs de la flota de agentes y umbrales de intervención | misma unidad |

**Pregunta generadora:** Para el agente más autónomo de su flota, ¿qué límite concreto de plataforma le impediría hoy hacer algo que su ficha prohíbe?

---

### 061. AMP-19 — Calidad epistemológica de evidencia

**Unidad:** G5.1 Supervisión de la Evaluación y Análisis · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 191 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** No toda evidencia vale lo mismo: distinguir observación (lo que se registró), inferencia (lo que se dedujo) y supuesto (lo que se asumió) evita decisiones de riesgo construidas sobre datos débiles.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** No toda evidencia vale lo mismo: distinguir observación (lo que se registró), inferencia (lo que se dedujo) y supuesto (lo que se asumió) evita decisiones de riesgo construidas sobre datos débiles. Con agentes que resumen, correlacionan y proponen, la mezcla de los tres niveles se vuelve invisible en una redacción fluida. La tesis es que toda salida de un agente que alimenta una decisión debe etiquetar qué es observación, qué inferencia y qué supuesto.

**Tensión y límites.** La tensión es que etiquetar cuesta y los lectores prefieren conclusiones. Otra tensión es que los modelos confabulan con la misma fluidez con que observan. El ensayo debe mostrar cómo el formato de salida fijo y la cita de fuentes convierten la epistemología en práctica.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: epistemología de la evidencia, análisis de inteligencia (niveles de confianza). Implementación: formato de salida de AG-01/AG-06 con secciones 'observado', 'inferido', 'supuesto' y fuentes; etiquetado de evidencias en el registro.

**Evidencia y evaluación.** Evidencia: diez salidas de agentes reetiquetadas por un analista y comparación con el etiquetado del agente. Se evalúa la tasa de inferencias presentadas como hechos.

**Puentes.** Se apoya en HC-001 (datos y decisiones); se relaciona con AMP-01, AMP-14 y G6.1-K05; alimenta G5.1-K05.

**Recomendaciones de práctica y ejercitación.**
1. Definir el formato de salida con etiquetas epistemológicas para AG-01 y AG-06.
2. Reetiquetar diez salidas y medir el desvío.
3. Incorporar la regla a las instrucciones (skill SK-06).

**Próximos pasos.**
- Usar el etiquetado en la revisión de desempeño.
- Conectar con la narrativa de riesgo (AMP-23).
- Revisar tras cambios de modelo.

**Relación con los conceptos de la(s) unidad(es) G5.1.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| G5.1-K01 | K | Supervisión del Proceso | misma unidad |
| G5.1-K02 | K | Metodologías | misma unidad |
| G5.1-K03 | K | Revisión de Resultados | misma unidad |
| G5.1-K04 | K | Identificación de Brechas | misma unidad |
| G5.1-K05 | K | Monitorización Continua | misma unidad |
| G5.1-K06 | K | Análisis Cuanti/Cuali | misma unidad |
| G5.1-K07 | K | Evaluación Amenazas | misma unidad |
| G5.1-K08 | K | Escenarios de Riesgo | misma unidad |
| G5.1-K09 | K | Herramientas GRC | misma unidad |
| G5.1-K10 | K | Auditoría Interna | misma unidad |
| AMP-20 | AMP | Riesgo de modelos de IA | misma unidad |
| HC-001 | HC | Gobierno de decisiones basadas en evidencia | misma unidad |
| HC-016 | HC | Superficie de ataque contextualizada | misma unidad |
| HC-017 | HC | Inteligencia que modifica decisiones | misma unidad |
| HC-039 | HC | Riesgo cibernético como narrativa empresarial | misma unidad |

**Pregunta generadora:** En el último brief que recibió de un asistente, ¿cuántas afirmaciones eran observaciones y cuántas inferencias disfrazadas?

---

### 062. AMP-20 — Riesgo de modelos de IA

**Unidad:** G5.1 Supervisión de la Evaluación y Análisis · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 184 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** Los modelos introducen riesgos propios —error, deriva, sesgo, manipulación y dependencia de proveedor— que deben evaluarse como riesgo empresarial, no como detalle técnico.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** Los modelos introducen riesgos propios —error, deriva, sesgo, manipulación y dependencia de proveedor— que deben evaluarse como riesgo empresarial, no como detalle técnico. Un modelo que clasifica incidentes puede degradarse sin aviso cuando cambian las amenazas o cuando el proveedor lo actualiza. La tesis es que cada modelo que usa la flota tiene un perfil de riesgo propio que el registro debe recoger y que la evaluación periódica debe vigilar.

**Tensión y límites.** La tensión es la opacidad: el owner no controla el modelo del proveedor ni conoce sus cambios. Otra tensión es la novedad del vocabulario para el comité de riesgo. El ensayo debe traducir los cinco riesgos a escenarios de negocio.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: AI RMF MAP/MEASURE, model risk management (origen financiero), NIST AI 600-1. Implementación: evaluación de riesgo de los modelos del catálogo de Foundry usados por la flota (error, deriva, sesgo, manipulación, dependencia), con KRIs y plan de evaluación periódica.

**Evidencia y evaluación.** Evidencia: perfil de riesgo de dos modelos en uso con escenarios, KRIs y tratamiento. Se evalúa la traducción a escenarios de negocio.

**Puentes.** Extiende M4.2-K07 (riesgos emergentes); se relaciona con AMP-48, AMP-42, G4.1-PA02 y M3.2-PA03.

**Recomendaciones de práctica y ejercitación.**
1. Perfilar el riesgo de dos modelos de la flota con los cinco riesgos y escenarios.
2. Definir KRIs de deriva y su fuente (evaluación periódica).
3. Registrar la dependencia de proveedor con plan alternativo.

**Próximos pasos.**
- Incorporar al registro de riesgos (G4.1-PA02).
- Programar la reevaluación (MDO-Q04).
- Vincular con la cadena de suministro de modelos (AMP-49).

**Relación con los conceptos de la(s) unidad(es) G5.1.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| G5.1-K01 | K | Supervisión del Proceso | misma unidad |
| G5.1-K02 | K | Metodologías | misma unidad |
| G5.1-K03 | K | Revisión de Resultados | misma unidad |
| G5.1-K04 | K | Identificación de Brechas | misma unidad |
| G5.1-K05 | K | Monitorización Continua | misma unidad |
| G5.1-K06 | K | Análisis Cuanti/Cuali | misma unidad |
| G5.1-K07 | K | Evaluación Amenazas | misma unidad |
| G5.1-K08 | K | Escenarios de Riesgo | misma unidad |
| G5.1-K09 | K | Herramientas GRC | misma unidad |
| G5.1-K10 | K | Auditoría Interna | misma unidad |
| AMP-19 | AMP | Calidad epistemológica de evidencia | misma unidad |
| HC-001 | HC | Gobierno de decisiones basadas en evidencia | misma unidad |
| HC-016 | HC | Superficie de ataque contextualizada | misma unidad |
| HC-017 | HC | Inteligencia que modifica decisiones | misma unidad |
| HC-039 | HC | Riesgo cibernético como narrativa empresarial | misma unidad |

**Pregunta generadora:** Si el proveedor actualizara mañana el modelo que usa su agente de triaje, ¿cómo se enteraría y qué haría?

---

### 063. AMP-21 — Decisiones reversibles

**Unidad:** G5.2 Supervisión del Tratamiento y Aceptación · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 174 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** Preferir decisiones reversibles reduce el costo de equivocarse en transformaciones inciertas: si se puede volver atrás, se puede avanzar con menos información.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** Preferir decisiones reversibles reduce el costo de equivocarse en transformaciones inciertas: si se puede volver atrás, se puede avanzar con menos información. Pero la reversibilidad debe diseñarse y probarse: una acción 'reversible' que nadie revirtió nunca no lo es. La tesis es que la reversibilidad es un criterio de diseño para otorgar autonomía (L3 solo a acciones reversibles) y un control que se ensaya.

**Tensión y límites.** La tensión es que la reversibilidad cuesta (eliminación suave en vez de definitiva, versiones, respaldos) y que algunas acciones son irreversibles por naturaleza (una notificación enviada). El ensayo debe mostrar cómo clasificar y cómo tratar lo irreversible.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: decisiones de una y dos vías, rollback, versionado. Implementación: clasificar las acciones de los agentes por reversibilidad; preferir soft delete, bloqueos con vencimiento y despliegue por versiones; probar la reversión de una acción de AG-02 y de un cambio de agente (ALM).

**Evidencia y evaluación.** Evidencia: clasificación de acciones por reversibilidad y dos pruebas de reversión documentadas. Se evalúa el realismo de la clasificación.

**Puentes.** Se apoya en HC-034; sostiene AMP-04, AMP-18, M5.2-PA01 y M6.2-PA02.

**Recomendaciones de práctica y ejercitación.**
1. Clasificar las acciones de los 15 agentes por reversibilidad e impacto.
2. Probar la reversión de una remediación de correo y de un cambio de instrucción.
3. Definir qué acciones irreversibles quedan en L1.

**Próximos pasos.**
- Usar la clasificación en el árbol de decisión de autonomía.
- Incluir pruebas de reversión en el pipeline (M6.2-PA02).
- Revisar en el post-mortem (M5.2-PA02).

**Relación con los conceptos de la(s) unidad(es) G5.2.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| G5.2-K01 | K | Supervisión de Respuestas | misma unidad |
| G5.2-K02 | K | Alineación con Apetito | misma unidad |
| G5.2-K03 | K | Autorización Residual | misma unidad |
| G5.2-K04 | K | Mitigación | misma unidad |
| G5.2-K05 | K | Transferencia | misma unidad |
| G5.2-K06 | K | Evitación | misma unidad |
| G5.2-K07 | K | Gestión Residual | misma unidad |
| G5.2-K08 | K | Comunicación Decisiones | misma unidad |
| G5.2-K09 | K | Métricas Mitigación | misma unidad |
| G5.2-K10 | K | Auditoría Tratamiento | misma unidad |
| AMP-22 | AMP | Aceptación de riesgo de agentes | misma unidad |
| HC-003 | HC | Riesgo residual y aceptación verificable | misma unidad |
| HC-028 | HC | Gestión de excepciones y compensaciones | misma unidad |
| HC-034 | HC | Decisiones reversibles y riesgo de transición | misma unidad |

**Pregunta generadora:** ¿Qué acción de su flota considera reversible, y cuándo fue la última vez que alguien la revirtió de verdad?

---

### 064. AMP-22 — Aceptación de riesgo de agentes

**Unidad:** G5.2 Supervisión del Tratamiento y Aceptación · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 173 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** Aceptar el riesgo residual de un agente exige autoridad de negocio, condiciones de operación, caducidad y monitoreo; no una aprobación técnica implícita del constructor.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** Aceptar el riesgo residual de un agente exige autoridad de negocio, condiciones de operación, caducidad y monitoreo; no una aprobación técnica implícita del constructor. La tesis es que la aceptación debe formalizarse como autorización para operar (ATO) con expediente: ficha, clasificación de autonomía, evaluación, identidad y datos, modelo de amenazas, compensatorios, kill switch, presupuesto, exposición regulatoria y firma del dueño del riesgo con vigencia.

**Tensión y límites.** La tensión es la fricción: un ATO por agente puede frenar la adopción; la respuesta es proporcionalidad (expediente ligero para L1, completo para L2+). Otra tensión es la caducidad: un agente autorizado hace un año sobre un modelo distinto no debería seguir autorizado.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: NIST RMF Authorize, aceptación de riesgo (G4.2-K10). Implementación: plantilla de expediente ATO del sub-plan; registro en Agent 365; comité de ciberriesgo (DD17, referencia interna) para alto riesgo; revocación por desactivación en PPAC/Agent 365.

**Evidencia y evaluación.** Evidencia: tres expedientes ATO firmados con vigencia y condiciones. Se evalúa la proporcionalidad y la claridad de las condiciones.

**Puentes.** Extiende G5.2-K03 (autorización residual); sostiene AGC-13; se relaciona con HC-028 y AMP-17.

**Recomendaciones de práctica y ejercitación.**
1. Preparar el expediente ATO de AG-03 con las diez piezas.
2. Defenderlo ante un par que haga de dueño del riesgo.
3. Definir la proporcionalidad del expediente por nivel de autonomía.

**Próximos pasos.**
- Registrar la autorización en Agent 365 (AGC-13).
- Programar la caducidad y la re-autorización.
- Conectar con la revisión de desempeño.

**Relación con los conceptos de la(s) unidad(es) G5.2.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| G5.2-K01 | K | Supervisión de Respuestas | misma unidad |
| G5.2-K02 | K | Alineación con Apetito | misma unidad |
| G5.2-K03 | K | Autorización Residual | misma unidad |
| G5.2-K04 | K | Mitigación | misma unidad |
| G5.2-K05 | K | Transferencia | misma unidad |
| G5.2-K06 | K | Evitación | misma unidad |
| G5.2-K07 | K | Gestión Residual | misma unidad |
| G5.2-K08 | K | Comunicación Decisiones | misma unidad |
| G5.2-K09 | K | Métricas Mitigación | misma unidad |
| G5.2-K10 | K | Auditoría Tratamiento | misma unidad |
| AMP-21 | AMP | Decisiones reversibles | misma unidad |
| HC-003 | HC | Riesgo residual y aceptación verificable | misma unidad |
| HC-028 | HC | Gestión de excepciones y compensaciones | misma unidad |
| HC-034 | HC | Decisiones reversibles y riesgo de transición | misma unidad |

**Pregunta generadora:** ¿Quién autorizó al agente que hoy remedia correo en su tenant, con qué condiciones y hasta cuándo?

---

### 065. AMP-23 — Narrativa de riesgo basada en evidencia

**Unidad:** G6.1 Comunicación Estratégica · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 181 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** Una narrativa de riesgo persuade cuando conecta hechos verificables, incertidumbre declarada y decisiones pendientes; no cuando dramatiza amenazas.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** Una narrativa de riesgo persuade cuando conecta hechos verificables, incertidumbre declarada y decisiones pendientes; no cuando dramatiza amenazas. El CISO que exagera pierde credibilidad al primer trimestre sin incidentes; el que presenta hechos, rangos y decisiones gana autoridad. La tesis es que la narrativa es un género con reglas: cada afirmación tiene evidencia, cada incertidumbre tiene rango y cada sección termina en una decisión que la dirección debe tomar.

**Tensión y límites.** La tensión es que la dramatización funciona a corto plazo para obtener presupuesto. Otra tensión es la de los agentes: el entusiasmo por las horas ahorradas y el miedo a la IA son dos dramatizaciones simétricas. El ensayo debe mostrar cómo narrar la flota con hechos.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: comunicación de riesgos, storytelling con datos, reporting ejecutivo. Implementación: plantilla de reporte trimestral del control (G6.1-PA01) con las tres reglas; narrativa de un trimestre con un error de agente relevante.

**Evidencia y evaluación.** Evidencia: reporte trimestral de dos páginas evaluado con las tres reglas. Se evalúa la ausencia de afirmaciones sin evidencia.

**Puentes.** Se apoya en HC-039 (comunicación con la dirección); se relaciona con AMP-24, G6.1-K05 y HC-027.

**Recomendaciones de práctica y ejercitación.**
1. Reescribir el último reporte aplicando las tres reglas.
2. Narrar el caso difícil (más tareas de agentes, un error relevante).
3. Identificar las decisiones pendientes que el reporte pide a la dirección.

**Próximos pasos.**
- Adoptar la plantilla para el reporte trimestral.
- Vincular con la comunicación de incertidumbre (AMP-24).
- Incorporar métricas que no engañan (HC-027).

**Relación con los conceptos de la(s) unidad(es) G6.1.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| G6.1-K01 | K | Estrategia Comunicación | misma unidad |
| G6.1-K02 | K | Comunicación Junta | misma unidad |
| G6.1-K03 | K | Comunicación Ejecutiva | misma unidad |
| G6.1-K04 | K | Lenguaje de Negocio | misma unidad |
| G6.1-K05 | K | Reportes Factuales | misma unidad |
| G6.1-K06 | K | Métricas Clave | misma unidad |
| G6.1-K07 | K | Gestión Expectativas | misma unidad |
| G6.1-K08 | K | Comunicación Crisis | misma unidad |
| G6.1-K09 | K | Responsabilidad Legal | misma unidad |
| G6.1-K10 | K | Cultura Abierta | misma unidad |
| AMP-24 | AMP | Comunicación de incertidumbre | misma unidad |
| HC-001 | HC | Gobierno de decisiones basadas en evidencia | misma unidad |
| HC-017 | HC | Inteligencia que modifica decisiones | misma unidad |
| HC-018 | HC | Observabilidad y aseguramiento de controles | misma unidad |
| HC-020 | HC | Respuesta y comunicación bajo incertidumbre | misma unidad |
| HC-022 | HC | Gobierno de crisis multidisciplinario | misma unidad |
| HC-026 | HC | Ética, cultura y controles internos | misma unidad |
| HC-027 | HC | Métricas que no engañan | misma unidad |
| HC-039 | HC | Riesgo cibernético como narrativa empresarial | misma unidad |
| G6.1-PA01 | PA | Reporte ejecutivo del producto-control y de la fuerza de trabajo híbrida | misma unidad |

**Pregunta generadora:** ¿Qué afirmación de su último reporte al comité no podría respaldar con un dato si se lo pidieran?

---

### 066. AMP-24 — Comunicación de incertidumbre

**Unidad:** G6.1 Comunicación Estratégica · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 168 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** Comunicar incertidumbre con rangos, supuestos y disparadores de revisión fortalece la credibilidad del CISO ante la dirección: una estimación con rango y condiciones se puede defender; un número exacto sin base, no.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** Comunicar incertidumbre con rangos, supuestos y disparadores de revisión fortalece la credibilidad del CISO ante la dirección: una estimación con rango y condiciones se puede defender; un número exacto sin base, no. La tesis es que la incertidumbre bien comunicada es una señal de competencia y que los disparadores de revisión convierten la incertidumbre en gobierno (qué nos haría cambiar la estimación).

**Tensión y límites.** La tensión es que los ejecutivos piden un número y castigan los rangos como evasivas. El ensayo debe mostrar cómo presentar rangos con decisiones claras asociadas y cómo educar al comité en la lectura de incertidumbre.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: estimación probabilística, FAIR introductorio, comunicación de riesgos. Implementación: en el caso de negocio de agentes (G1.2-PA01) y en los KPIs de la flota, presentar rangos, supuestos y disparadores; incluir la sección 'qué cambiaría esta estimación' en el reporte.

**Evidencia y evaluación.** Evidencia: caso de negocio o estimación de riesgo presentada con rangos, supuestos y disparadores. Se evalúa la utilidad para decidir.

**Puentes.** Extiende G6.1-K05 (reportes factuales); se relaciona con AMP-23 y G1.2-PA01.

**Recomendaciones de práctica y ejercitación.**
1. Convertir tres cifras del caso de negocio de agentes en rangos con supuestos.
2. Definir disparadores de revisión para cada una.
3. Ensayar la presentación ante un par escéptico.

**Próximos pasos.**
- Incorporar la sección de incertidumbre al reporte trimestral.
- Usar los disparadores como KRIs.
- Revisar las estimaciones al cumplirse un disparador.

**Relación con los conceptos de la(s) unidad(es) G6.1.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| G6.1-K01 | K | Estrategia Comunicación | misma unidad |
| G6.1-K02 | K | Comunicación Junta | misma unidad |
| G6.1-K03 | K | Comunicación Ejecutiva | misma unidad |
| G6.1-K04 | K | Lenguaje de Negocio | misma unidad |
| G6.1-K05 | K | Reportes Factuales | misma unidad |
| G6.1-K06 | K | Métricas Clave | misma unidad |
| G6.1-K07 | K | Gestión Expectativas | misma unidad |
| G6.1-K08 | K | Comunicación Crisis | misma unidad |
| G6.1-K09 | K | Responsabilidad Legal | misma unidad |
| G6.1-K10 | K | Cultura Abierta | misma unidad |
| AMP-23 | AMP | Narrativa de riesgo basada en evidencia | misma unidad |
| HC-001 | HC | Gobierno de decisiones basadas en evidencia | misma unidad |
| HC-017 | HC | Inteligencia que modifica decisiones | misma unidad |
| HC-018 | HC | Observabilidad y aseguramiento de controles | misma unidad |
| HC-020 | HC | Respuesta y comunicación bajo incertidumbre | misma unidad |
| HC-022 | HC | Gobierno de crisis multidisciplinario | misma unidad |
| HC-026 | HC | Ética, cultura y controles internos | misma unidad |
| HC-027 | HC | Métricas que no engañan | misma unidad |
| HC-039 | HC | Riesgo cibernético como narrativa empresarial | misma unidad |
| G6.1-PA01 | PA | Reporte ejecutivo del producto-control y de la fuerza de trabajo híbrida | misma unidad |

**Pregunta generadora:** ¿Qué estimación presentó usted como número exacto que en realidad era un rango, y qué pasó cuando no se cumplió?

---

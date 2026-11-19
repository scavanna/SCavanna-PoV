<!-- generado-ciso-excel sha256:5a034ae0c19161f8457935fb2768066df4fe5fbef28e69f747c1f3d1d68eca79 -->
# Sesgo de automatización

**ID:** `BIAS-0196` · **Categoría:** Sesgos cognitivos · **Prioridad editorial:** 2 · **Base de definición:** Apoyada por fuentes del catálogo

## Definición y alcance

Tendencia a favorecer recomendaciones de sistemas automatizados y descartar información humana contradictoria, incluso cuando esta es correcta.

**Límites:** No implica rechazar automatización; exige calibrar su alcance, calidad y condiciones de supervisión.

## Alias

- Automation Bias
- automation bias
- Sesgo de automatizaciÃ³n

## Relevancia para el CISO

**Por qué:** Una recomendación automatizada parece más fiable que la evidencia humana discordante.

**Caso específico:** El agente propone cerrar una alerta, pero un analista detecta una señal no capturada.

**Pregunta guía:** ¿Podemos demostrar cuándo y cómo se desobedece al sistema?

**Dominios:** SOC agéntico, Trust Framework

**Casos CISO adicionales:**

- Incluir Sesgo de automatización en revisiones de arquitectura, incidentes, proveedores y excepciones.
- Vincular decisiones a evidencia operativa, propietario, fecha de revisión y criterio de salida.

## Aplicación para arquitectura, SOC agéntico y Trust Framework

**Arquitectura:**

- Diseñar controles compensatorios, telemetría y puertas de revisión que hagan visible el supuesto sesgado.

**SOC agéntico — Alta:** Puede alterar autonomía, triage, respuesta y aprendizaje en un SOC agéntico.

**Trust Framework — Alta:** Afecta gobernanza, responsabilidad, evidencia y aseguramiento de decisiones técnicas.

## Práctica y evaluación

**Ejercicios:**

- Realizar un pre-mortem de una arquitectura o respuesta afectada por el sesgo.
- Rediseñar una decisión eliminando el supuesto dominante y comparando alternativas.

**Métodos de evaluación:**

- Auditar decisiones reales contra resultados, evidencia disponible y criterios declarados.
- Ejecutar un tabletop con una variante que active deliberadamente el sesgo.

**Controles o compensaciones:**

- Establecer revisión independiente y criterios de reversión.
- Usar telemetría, pruebas y evidencia contraria antes de aceptar excepciones.

## Pensadores y bibliografía identificados

**Personas y atribución documentada:**

- No consta en los documentos analizados.

**Referencias bibliográficas mencionadas en el corpus:**

- Automation bias - Wikipedia, acceso: julio 22, 2025, https://en.wikipedia.org/wiki/Automation_bias
- AI Safety and Automation Bias | CSET, acceso: noviembre 2, 2025, https://cset.georgetown.edu/wp-content/uploads/CSET-AI-Safety-and-Automation-Bias.pdf

## Trazabilidad documental

**Documentos contabilizados en el catálogo:** 25. **Localizadores representativos listados:** 3.

- 202508 - Cognitive Biases_ Comprehensive Analysis.docx — line:540 (Pasaje directo identificado)
- 250824 - CISO_ Sesgos y Modelos Mentales.docx — line:156 (Pasaje directo identificado)
- 48 Sesgos Cognitivos para un CISO.docx — line:23 (Pasaje directo identificado)

## Nota metodológica

La definición y las referencias se registran desde el catálogo; la prioridad, el caso concreto y la pregunta son adaptación editorial para el CISO, no evidencia experimental de eficacia. Un sesgo se gestiona con controles compensatorios y revisión independiente, no se promete eliminarlo mediante entrenamiento.

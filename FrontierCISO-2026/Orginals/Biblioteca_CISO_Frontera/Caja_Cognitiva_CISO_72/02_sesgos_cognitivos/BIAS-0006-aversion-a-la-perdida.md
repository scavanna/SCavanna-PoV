<!-- generado-ciso-excel sha256:21cb6c1510407ae67047d947ef08694ab11e00ebf7bdb20a16460cc134294c0f -->
# Aversión a la pérdida

**ID:** `BIAS-0006` · **Categoría:** Sesgos cognitivos · **Prioridad editorial:** 12 · **Base de definición:** Apoyada por fuentes del catálogo

## Definición y alcance

Tendencia a sentir o ponderar una pérdida con mayor intensidad que una ganancia equivalente, alterando elecciones entre alternativas.

**Límites:** No equivale a toda prudencia ante pérdidas; requiere una asimetría que exceda la diferencia objetiva entre opciones. Las aplicaciones, métodos y ejercicios siguientes son recomendaciones profesionales derivadas, no afirmaciones textuales de las fuentes.

## Alias

- loss
  aversion
- Loss Aversion
- loss aversion
- Sesgo de aversión a la pérdida
- Sesgo de Aversión a la Pérdida
- Sesgo de Aversión a la Pérdida (Loss Aversion)

## Relevancia para el CISO

**Por qué:** Evitar una pérdida visible puede pesar más que obtener una reducción mayor de riesgo.

**Caso específico:** Se conserva tecnología heredada para no registrar una pérdida contable aunque exponga datos.

**Pregunta guía:** ¿Qué opción elegiríamos si las dos se contrataran hoy?

**Dominios:** Gobierno, Terceros

**Casos CISO adicionales:**

- Derivado: exigir tasas base, rangos y supuestos cuantificados en decisiones expuestas a Aversión a la pérdida.
- Derivado: solicitar una vista externa y al menos un escenario alternativo antes de aprobar riesgo o inversión.

## Aplicación para arquitectura, SOC agéntico y Trust Framework

**Arquitectura:**

- Derivado: mostrar probabilidades, incertidumbre y sensibilidad, evitando interfaces que oculten supuestos o impongan un único encuadre.

**SOC agéntico — Alta:** Puede distorsionar probabilidad, impacto y prioridad de alertas o escenarios en un SOC asistido por agentes.

**Trust Framework — Alta:** La confianza calibrada requiere probabilidades, supuestos y alternativas explícitas, no solo intuición.

## Práctica y evaluación

**Ejercicios:**

- Derivado: estimar una probabilidad antes de leer el caso narrativo y revisarla después con tasas base.
- Derivado: resolver el mismo riesgo con marcos de ganancia, pérdida y valor esperado.

**Métodos de evaluación:**

- Observable: presentar evidencia equivalente con distinto encuadre u orden y comparar las estimaciones resultantes.
- Observable: registrar pronósticos probabilísticos y medir su calibración frente a resultados observados.

**Controles o compensaciones:**

- Usar tasas base, rangos, valor esperado y análisis de sensibilidad.
- Aplicar revisión independiente, premortem y escenarios contrafactuales.

## Pensadores y bibliografía identificados

**Personas y atribución documentada:**

- No consta en los documentos analizados.

**Referencias bibliográficas mencionadas en el corpus:**

- No consta en los documentos analizados.

## Trazabilidad documental

**Documentos contabilizados en el catálogo:** 78. **Localizadores representativos listados:** 3.

- 202508 - Cognitive Biases_ Comprehensive Analysis.docx — line:665 (Pasaje directo identificado)
- 250824 - 500 Mental Models.docx — line:97 (Pasaje directo identificado)
- 250824 - Sesgos - Cyber.docx — line:42 (Pasaje directo identificado)

## Nota metodológica

La definición y las referencias se registran desde el catálogo; la prioridad, el caso concreto y la pregunta son adaptación editorial para el CISO, no evidencia experimental de eficacia. Un sesgo se gestiona con controles compensatorios y revisión independiente, no se promete eliminarlo mediante entrenamiento.

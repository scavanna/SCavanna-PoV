<!-- generado-ciso-excel sha256:c27c3f0628d57a06d2ef54c829f063c0f7dd53ad81f94f22e3826cec24ea2059 -->
# Negligencia de la tasa base

**ID:** `BIAS-0141` · **Categoría:** Sesgos cognitivos · **Prioridad editorial:** 5 · **Base de definición:** Apoyada por fuentes del catálogo

## Definición y alcance

Tendencia a ignorar información estadística de tasa base y dar más peso a información específica o individualizante al juzgar probabilidades.

**Límites:** La información individual puede ser diagnóstica; debe combinarse con la tasa base en lugar de reemplazarla. Las aplicaciones, métodos y ejercicios siguientes son recomendaciones profesionales derivadas, no afirmaciones textuales de las fuentes.

## Alias

- Base Rate Fallacy
- Base Rate Fallacy / Neglect
- base rate neglect
- base-rate neglect
- falacia de la tasa base
- Falacia de la tasa base
- Falacia de la Tasa Base (Base Rate Fallacy)

## Relevancia para el CISO

**Por qué:** Se descarta la prevalencia previa al interpretar una señal aislada.

**Caso específico:** Una alerta con aspecto muy convincente genera escalamiento masivo en un proceso de baja tasa de abuso.

**Pregunta guía:** ¿Qué probabilidad previa falta en este cálculo?

**Dominios:** SOC agéntico, Directorio

**Casos CISO adicionales:**

- Derivado: exigir tasas base, rangos y supuestos cuantificados en decisiones expuestas a Negligencia de la tasa base.
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

- Base Rate Fallacy - The Decision Lab, acceso: julio 22, 2025, https://thedecisionlab.com/biases/base-rate-fallacy

## Trazabilidad documental

**Documentos contabilizados en el catálogo:** 23. **Localizadores representativos listados:** 3.

- 202508 - Cognitive Biases_ Comprehensive Analysis.docx — line:104 (Pasaje directo identificado)
- 250824 - Sesgos cognitivos en adultos mayores(1).docx — line:352 (Pasaje directo identificado)
- 250824 - Sesgos cognitivos en adultos.docx — paragraph:413;style:Heading3 (Pasaje directo identificado)

## Nota metodológica

La definición y las referencias se registran desde el catálogo; la prioridad, el caso concreto y la pregunta son adaptación editorial para el CISO, no evidencia experimental de eficacia. Un sesgo se gestiona con controles compensatorios y revisión independiente, no se promete eliminarlo mediante entrenamiento.

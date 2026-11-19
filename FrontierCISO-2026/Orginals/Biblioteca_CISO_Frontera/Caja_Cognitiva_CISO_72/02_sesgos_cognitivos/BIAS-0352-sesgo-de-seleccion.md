<!-- generado-ciso-excel sha256:490c388b04a1dc793b973a9322ed5b1d407647563aa25b09d2648e9ba75dd387 -->
# Sesgo de selección

**ID:** `BIAS-0352` · **Categoría:** Sesgos cognitivos · **Prioridad editorial:** 20 · **Base de definición:** Apoyada por fuentes del catálogo

## Definición y alcance

El Sesgo de selección surge cuando personas, grupos o datos se eligen de forma que la muestra deja de representar la población o favorece una conclusión.

**Límites:** Toda selección implica criterios; el sesgo aparece cuando estos distorsionan la inferencia y no se controlan.

## Alias

- selection bias
- Selection Bias

## Relevancia para el CISO

**Por qué:** La muestra de alertas, equipos o incidentes no representa al universo que se quiere gobernar.

**Caso específico:** Se valida el agente con incidentes bien etiquetados, pero no con alertas difíciles no clasificadas.

**Pregunta guía:** ¿Cómo fueron elegidos estos ejemplos y qué faltó?

**Dominios:** SOC agéntico, Trust Framework

**Casos CISO adicionales:**

- Verificar representatividad de métricas, encuestas y pruebas de control.
- Incluir activos, usuarios e incidentes que contradigan la narrativa.

## Aplicación para arquitectura, SOC agéntico y Trust Framework

**Arquitectura:**

- Diseñar muestreo estratificado y cobertura observable para pruebas.

**SOC agéntico — Alta:** Datos de entrenamiento y evaluación no representativos degradan detección y respuesta.

**Trust Framework — Alta:** La validez y equidad de sistemas dependen de datos representativos y trazables.

## Práctica y evaluación

**Ejercicios:**

- Detectar exclusiones sistemáticas en un conjunto de incidentes.
- Diseñar un plan de muestreo para controles distribuidos.

**Métodos de evaluación:**

- Comparar distribución de la muestra con la población objetivo.
- Repetir el análisis con criterios de selección alternativos.

**Controles o compensaciones:**

- Documentar población, inclusión, exclusión y cobertura.
- Usar muestreo aleatorio o estratificado cuando corresponda.

## Pensadores y bibliografía identificados

**Personas y atribución documentada:**

- Daniel Kahneman — La evidencia de la fuente 185 lo lista explícitamente junto al concepto.
- Amos Tversky — La evidencia de la fuente 185 lo lista explícitamente junto al concepto.

**Referencias bibliográficas mencionadas en el corpus:**

- No consta en los documentos analizados.

## Trazabilidad documental

**Documentos contabilizados en el catálogo:** 18. **Localizadores representativos listados:** 3.

- 202508 - Cognitive Biases_ Comprehensive Analysis 2.docx — line:47 (Pasaje directo identificado)
- 202508 - Cognitive Biases_ Comprehensive Analysis.docx — line:78 (Pasaje directo identificado)
- 250824 - CISO_ Sesgos y Modelos Mentales.docx — line:122 (Pasaje directo identificado)

## Nota metodológica

La definición y las referencias se registran desde el catálogo; la prioridad, el caso concreto y la pregunta son adaptación editorial para el CISO, no evidencia experimental de eficacia. Un sesgo se gestiona con controles compensatorios y revisión independiente, no se promete eliminarlo mediante entrenamiento.

<!-- generado-ciso-excel sha256:560e221055cb8dabd85eac92edf7699b312a855b2cbc6a324c5500a5c08b12bd -->
# Sesgo de autoridad

**ID:** `BIAS-0197` · **Categoría:** Sesgos cognitivos · **Prioridad editorial:** 10 · **Base de definición:** Apoyada por fuentes del catálogo

## Definición y alcance

Tendencia a otorgar mayor precisión o influencia a opiniones de figuras de autoridad y aceptarlas sin evaluación crítica suficiente.

**Límites:** La experiencia y responsabilidad formal pueden ser evidencia pertinente, pero no sustituyen la justificación.

## Alias

- authority bias
- Authority Bias
- Sesgo de Autoridad (Authority Bias)

## Relevancia para el CISO

**Por qué:** La jerarquía o prestigio sustituyen la comprobación de una afirmación.

**Caso específico:** La recomendación de un proveedor influyente se adopta sin una prueba reproducible.

**Pregunta guía:** ¿Aceptaríamos el mismo argumento sin saber quién lo dijo?

**Dominios:** Terceros, Directorio

**Casos CISO adicionales:**

- Revisar si Sesgo de autoridad altera selección de personas, proveedores o credibilidad de interlocutores.
- Aplicar criterios comunes y revisión diversa antes de decisiones sensibles a identidad o estatus.

## Aplicación para arquitectura, SOC agéntico y Trust Framework

**Arquitectura:**

- Separar atributos personales no pertinentes de los datos usados en flujos de evaluación y aprobación.

**SOC agéntico — Indirecta:** Tiene efecto directo limitado en automatización, pero puede contaminar datos humanos y escalaciones.

**Trust Framework — Alta:** Es relevante para equidad, legitimidad y ausencia de discriminación en marcos de confianza.

## Práctica y evaluación

**Ejercicios:**

- Evaluar pares de casos equivalentes con identidades distintas y discutir diferencias.
- Practicar una revisión ciega con rúbrica antes de revelar contexto personal.

**Métodos de evaluación:**

- Comparar resultados ante perfiles equivalentes que solo cambian en el atributo social relevante.
- Auditar dispersión de decisiones por grupo, rol o procedencia con criterios previamente definidos.

**Controles o compensaciones:**

- Usar rúbricas estructuradas y evaluación ciega cuando sea viable.
- Incluir revisión independiente y perspectivas diversas en decisiones de alto impacto.

## Pensadores y bibliografía identificados

**Personas y atribución documentada:**

- No consta en los documentos analizados.

**Referencias bibliográficas mencionadas en el corpus:**

- Authority Bias - The Decision Lab, acceso: julio 22, 2025, https://thedecisionlab.com/biases/authority-bias

## Trazabilidad documental

**Documentos contabilizados en el catálogo:** 50. **Localizadores representativos listados:** 3.

- 202508 - Cognitive Biases_ Comprehensive Analysis.docx — line:34 (Pasaje directo identificado)
- 250824 - CISO_ Sesgos y Modelos Mentales.docx — line:110 (Pasaje directo identificado)
- 250824 - Sesgos cognitivos en adultos mayores(1).docx — line:293 (Pasaje directo identificado)

## Nota metodológica

La definición y las referencias se registran desde el catálogo; la prioridad, el caso concreto y la pregunta son adaptación editorial para el CISO, no evidencia experimental de eficacia. Un sesgo se gestiona con controles compensatorios y revisión independiente, no se promete eliminarlo mediante entrenamiento.

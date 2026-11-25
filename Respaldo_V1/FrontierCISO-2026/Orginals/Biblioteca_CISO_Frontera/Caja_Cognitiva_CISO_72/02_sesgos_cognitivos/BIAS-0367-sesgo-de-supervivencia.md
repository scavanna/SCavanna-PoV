<!-- generado-ciso-excel sha256:059d5c893730eceb9e23f0576a07320dd1e75a122f5d72e25d7548b2e7487e32 -->
# Sesgo de supervivencia

**ID:** `BIAS-0367` · **Categoría:** Sesgos cognitivos · **Prioridad editorial:** 19 · **Base de definición:** Apoyada por fuentes del catálogo

## Definición y alcance

El Sesgo de supervivencia se concentra en quienes o aquello que superó un proceso e ignora casos no visibles que fracasaron.

**Límites:** Se solapa con evidencia silenciosa; debe analizarse el mecanismo que excluyó los no supervivientes.

## Alias

- Sesgo de Sobrevivencia
- Sesgo de Supervivencia (Survivorship Bias)
- Survivorship bias
- survivorship bias
- Survivorship Bias

## Relevancia para el CISO

**Por qué:** Los casos visibles exitosos ocultan los fallos que quedaron fuera de la muestra.

**Caso específico:** El benchmark de SOC usa solo clientes que completaron la migración.

**Pregunta guía:** ¿Quién desapareció del conjunto y por qué?

**Dominios:** Terceros, Gobierno

**Casos CISO adicionales:**

- Estudiar organizaciones y controles que fallaron, no solo casos exitosos.
- Incluir incidentes no detectados y proyectos cancelados en lecciones aprendidas.

## Aplicación para arquitectura, SOC agéntico y Trust Framework

**Arquitectura:**

- Diseñar métricas con denominadores completos y registros de fallos.

**SOC agéntico — Alta:** Entrenamiento con alertas e incidentes visibles puede ocultar fallos no detectados.

**Trust Framework — Alta:** La validez de evidencia exige representar éxitos y fracasos.

## Práctica y evaluación

**Ejercicios:**

- Revisar un caso de éxito buscando la población ausente.
- Construir una base de controles fallidos y causas.

**Métodos de evaluación:**

- Verificar presencia de casos fallidos en análisis comparativos.
- Recalcular conclusiones incluyendo no supervivientes.

**Controles o compensaciones:**

- Buscar evidencia silenciosa y datos de abandono.
- Declarar el proceso de selección y su denominador.

## Pensadores y bibliografía identificados

**Personas y atribución documentada:**

- No consta en los documentos analizados.

**Referencias bibliográficas mencionadas en el corpus:**

- No consta en los documentos analizados.

## Trazabilidad documental

**Documentos contabilizados en el catálogo:** 49. **Localizadores representativos listados:** 3.

- 202508 - Cognitive Biases_ Comprehensive Analysis.docx — line:252 (Pasaje directo identificado)
- 250824 - CISO_ Sesgos y Modelos Mentales.docx — line:153 (Pasaje directo identificado)
- 250824 - Sesgos - Cyber.docx — line:28 (Pasaje directo identificado)

## Nota metodológica

La definición y las referencias se registran desde el catálogo; la prioridad, el caso concreto y la pregunta son adaptación editorial para el CISO, no evidencia experimental de eficacia. Un sesgo se gestiona con controles compensatorios y revisión independiente, no se promete eliminarlo mediante entrenamiento.

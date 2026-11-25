<!-- generado-ciso-excel sha256:fff9571233de7aaa3977b2ca40740c74d1191cf1f5061337a266b32d2c325938 -->
# Tasa base

**ID:** `MM-0150` · **Categoría:** Modelos mentales · **Prioridad editorial:** 8 · **Base de definición:** Apoyada por fuentes del catálogo

## Definición y alcance

Información estadística general sobre la prevalencia previa de un resultado antes de incorporar evidencia específica de un caso. La evidencia la contrasta con su negligencia en la falacia de tasa base.

**Límites:** Una tasa base depende de población, periodo y contexto; no debe dominar evidencia específica altamente diagnóstica.

## Alias

- base rate
- prior probability

## Relevancia para el CISO

**Por qué:** Protege de conclusiones basadas sólo en una señal espectacular.

**Caso específico:** Un caso de fraude parece convincente, pero la tasa base de fraude en ese flujo es muy baja.

**Pregunta guía:** ¿Cuál era la prevalencia antes de observar esta señal?

**Dominios:** SOC agéntico, Directorio

**Casos CISO adicionales:**

- Usar prevalencia histórica al evaluar amenazas y falsos positivos.
- Exigir población de referencia en estimaciones ejecutivas.

## Aplicación para arquitectura, SOC agéntico y Trust Framework

**Arquitectura:**

- Incorporar priors contextuales en reglas y modelos de detección.

**SOC agéntico — Alta:** Reduce sobre-reacción agéntica a señales llamativas.

**Trust Framework — Alta:** Mejora calibración y transparencia de inferencias.

## Práctica y evaluación

**Ejercicios:**

- Resolver casos con y sin tasa base.
- Calcular impacto de cambiar el prior.

**Métodos de evaluación:**

- Las estimaciones declaran población y periodo.
- La decisión compara posterior con tasa base.

**Controles o compensaciones:**

- Evitar tasas de poblaciones no comparables.
- Combinar tasa base y evidencia diagnóstica.

## Pensadores y bibliografía identificados

**Personas y atribución documentada:**

- No consta en los documentos analizados.

**Referencias bibliográficas mencionadas en el corpus:**

- Base Rate Fallacy - The Decision Lab, acceso: julio 22, 2025, https://thedecisionlab.com/biases/base-rate-fallacy

## Trazabilidad documental

**Documentos contabilizados en el catálogo:** 34. **Localizadores representativos listados:** 3.

- analiza la siguiente planilla y de termina cuales.._.xlsx — [sheet analiza la siguiente planilla y] (Mención taxonómica (no definición))
- BiaCodex_Reordenado.xlsx — [sheet biacodex_reordenado] (Mención taxonómica (no definición))
- Codex1.xlsx — [sheet biacodex] (Mención taxonómica (no definición))

## Nota metodológica

La definición y las referencias se registran desde el catálogo; la prioridad, el caso concreto y la pregunta son adaptación editorial para el CISO, no evidencia experimental de eficacia. Aplicar como herramienta situada, no como explicación universal.

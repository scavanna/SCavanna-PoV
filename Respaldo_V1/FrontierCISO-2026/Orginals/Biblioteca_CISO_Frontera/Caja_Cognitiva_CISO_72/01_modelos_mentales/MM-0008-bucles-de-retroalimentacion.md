<!-- generado-ciso-excel sha256:6ce4b5097c0bbbf7bb23020a42ae78b0e03da9f62c20a2271883406cb989a191 -->
# Bucles de retroalimentación

**ID:** `MM-0008` · **Categoría:** Modelos mentales · **Prioridad editorial:** 2 · **Base de definición:** Apoyada por fuentes del catálogo

## Definición y alcance

Los bucles de retroalimentación son relaciones en las que una salida modifica entradas posteriores, reforzando o equilibrando el comportamiento del sistema.

**Límites:** No toda correlación temporal es retroalimentación; deben identificarse causalidad, polaridad y demoras.

## Alias

- balancing loop
- feedback loop
- Feedback Loops
- feedback loops
- reinforcing loop

## Relevancia para el CISO

**Por qué:** Hace visibles los ciclos que amplifican o corrigen riesgo y deuda de seguridad.

**Caso específico:** Cada falso positivo reduce la atención del analista y aumenta los errores de clasificación del agente.

**Pregunta guía:** ¿Qué resultado vuelve a alimentar la entrada y con qué demora?

**Dominios:** SOC agéntico, Trust Framework

**Casos CISO adicionales:**

- Aplicar el modelo para aprender sistemáticamente de incidentes, métricas y decisiones.
- Incluir una comprobación de variable de salida, ruta de retorno, polaridad y demora en decisiones de riesgo, estrategia o incidentes.

## Aplicación para arquitectura, SOC agéntico y Trust Framework

**Arquitectura:**

- Usar el modelo para mapear bucles reforzadores y compensadores antes de automatizar respuestas.

**SOC agéntico — Alta:** Puede incorporarse como regla o bucle observable para aprender sistemáticamente de incidentes, métricas y decisiones.

**Trust Framework — Alta:** Aporta directamente a trazabilidad, control o rendición de cuentas al usarlo para mapear bucles reforzadores y compensadores antes de automatizar respuestas.

## Práctica y evaluación

**Ejercicios:**

- Resolver un caso breve aplicando el modelo para aprender sistemáticamente de incidentes, métricas y decisiones y explicitar los supuestos.
- Reanalizar una decisión pasada, identificar variable de salida, ruta de retorno, polaridad y demora y describir qué habría cambiado.

**Métodos de evaluación:**

- Auditar 10 decisiones y registrar si quedó documentado lo siguiente: variable de salida, ruta de retorno, polaridad y demora.
- Comparar dos casos similares, con y sin aplicación explícita del modelo, mediante una métrica de resultado acordada.

**Controles o compensaciones:**

- Usar el modelo como lente, no como regla; contrastarlo con datos y con un modelo alternativo.
- Documentar las condiciones donde no aplica y someter la conclusión a revisión independiente.

## Pensadores y bibliografía identificados

**Personas y atribución documentada:**

- No consta en los documentos analizados.

**Referencias bibliográficas mencionadas en el corpus:**

- Employee feedback loops: The secret to employee engagement - Workleap, acceso: agosto 3, 2025, https://workleap.com/blog/employee-feedback-loop
- Mental Model: Feedback Loops - Farnam Street, acceso: julio 22, 2025, https://fs.blog/mental-model-feedback-loops/
- Anshul Khare y Vishal Khandelwal, Mental Models, Investing, And You, Safal Niveshak (fecha no explícita en el PDF)

## Trazabilidad documental

**Documentos contabilizados en el catálogo:** 43. **Localizadores representativos listados:** 3.

- Mental_Models_Investing_and_You.pdf — chapter:32;pdf-page:264;printed-page:262 (Capítulo dedicado)
- 251002 - Mental Models_ 500 Model Compilation.docx — table:1;row:151;column:1 (Pasaje directo identificado)
- 251002 - Mental Models_ Analysis and Synthesis.docx — paragraph:64;style:Normal (Pasaje directo identificado)

## Nota metodológica

La definición y las referencias se registran desde el catálogo; la prioridad, el caso concreto y la pregunta son adaptación editorial para el CISO, no evidencia experimental de eficacia. Aplicar como herramienta situada, no como explicación universal.

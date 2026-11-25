<!-- generado-ciso-excel sha256:dec146dc0201ff557a51df2e1c55bc20b0db5a22dc0ba7ee887525696f3654d8 -->
# Regresión a la media

**ID:** `MM-0141` · **Categoría:** Modelos mentales · **Prioridad editorial:** 24 · **Base de definición:** Apoyada por fuentes del catálogo

## Definición y alcance

La regresión a la media describe que, cuando una medición extrema incluye variación aleatoria, una medición posterior del mismo proceso tiende a ser menos extrema. No basta una mejora posterior para atribuir causalidad a una intervención.

**Límites:** Requiere mediciones comparables y variación aleatoria; no garantiza que el sistema vuelva a un valor fijo ni descarta cambios causales.

## Alias

- Regression to the Mean

## Relevancia para el CISO

**Por qué:** Evita atribuir a un control una mejora que pudo ser fluctuación aleatoria.

**Caso específico:** Tras cambiar el proveedor, los incidentes bajan desde un mes excepcionalmente malo.

**Pregunta guía:** ¿La tendencia se explica por intervención o por retorno estadístico esperado?

**Dominios:** Gobierno, Directorio

**Casos CISO adicionales:**

- Evitar atribuir una mejora posterior a una intervención sin comparación.
- Interpretar picos de incidentes y rendimiento con una línea base.

## Aplicación para arquitectura, SOC agéntico y Trust Framework

**Arquitectura:**

- Diseñar métricas con ventanas y controles que separen tendencia de variación.

**SOC agéntico — Media:** Evita que agentes sobreajusten tras eventos extremos.

**Trust Framework — Alta:** Protege la integridad de métricas y evaluaciones.

## Práctica y evaluación

**Ejercicios:**

- Simular series con valores extremos.
- Reanalizar una mejora aparente tras un pico.

**Métodos de evaluación:**

- Se compara con historia y grupo de referencia.
- Las conclusiones sobreviven a una ventana temporal alternativa.

**Controles o compensaciones:**

- Usar líneas base y grupos comparables.
- No premiar o culpar por un único extremo.

## Pensadores y bibliografía identificados

**Personas y atribución documentada:**

- No consta en los documentos analizados.

**Referencias bibliográficas mencionadas en el corpus:**

- Anshul Khare y Vishal Khandelwal, Mental Models, Investing, And You, Safal Niveshak (fecha no explícita en el PDF)

## Trazabilidad documental

**Documentos contabilizados en el catálogo:** 8. **Localizadores representativos listados:** 3.

- Mental_Models_Investing_and_You.pdf — chapter:19;pdf-page:161;printed-page:159 (Capítulo dedicado)
- 250824 - 500 Mental Models.docx — paragraph:128;style:Heading4 (Pasaje directo identificado)
- 250824 - Applying Mental Models to Cybersecurity(1).docx — paragraph:35;style:Heading2 (Pasaje directo identificado)

## Nota metodológica

La definición y las referencias se registran desde el catálogo; la prioridad, el caso concreto y la pregunta son adaptación editorial para el CISO, no evidencia experimental de eficacia. Aplicar como herramienta situada, no como explicación universal.

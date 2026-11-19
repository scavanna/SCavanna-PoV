<!-- generado-ciso-excel sha256:8f06c9e6f4648289e5530930482de75d1dc88c3eb80b996bdf54e0dba21b13b3 -->
# Sesgo de acción

**ID:** `BIAS-0169` · **Categoría:** Sesgos cognitivos · **Prioridad editorial:** 15 · **Base de definición:** Apoyada por fuentes del catálogo

## Definición y alcance

Tendencia a preferir actuar antes que no intervenir, incluso cuando esperar, observar o no actuar sería más eficaz.

**Límites:** No desaconseja la respuesta rápida cuando está justificada; cuestiona la acción impulsada por presión psicológica y no por evidencia.

## Alias

- Action Bias
- action bias
- Sesgo de Acción (Action Bias)

## Relevancia para el CISO

**Por qué:** La presión por 'hacer algo' sustituye la comparación de opciones.

**Caso específico:** En una alerta ambigua el CISO ordena aislar una red crítica sin revisar impactos.

**Pregunta guía:** ¿Actuar ahora mejora el resultado esperado respecto de observar o acotar?

**Dominios:** Crisis, SOC agéntico

**Casos CISO adicionales:**

- Incluir Sesgo de acción en revisiones de arquitectura, incidentes, proveedores y excepciones.
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

- Anshul Khare y Vishal Khandelwal, Mental Models, Investing, And You, Safal Niveshak (fecha no explícita en el PDF)

## Trazabilidad documental

**Documentos contabilizados en el catálogo:** 31. **Localizadores representativos listados:** 3.

- Mental_Models_Investing_and_You.pdf — chapter:6;pdf-page:59;printed-page:58 (Capítulo dedicado)
- 202508 - Cognitive Biases_ Comprehensive Analysis.docx — line:24 (Pasaje directo identificado)
- 250824 - Sesgos cognitivos en adultos mayores(1).docx — line:234 (Pasaje directo identificado)

## Nota metodológica

La definición y las referencias se registran desde el catálogo; la prioridad, el caso concreto y la pregunta son adaptación editorial para el CISO, no evidencia experimental de eficacia. Un sesgo se gestiona con controles compensatorios y revisión independiente, no se promete eliminarlo mediante entrenamiento.

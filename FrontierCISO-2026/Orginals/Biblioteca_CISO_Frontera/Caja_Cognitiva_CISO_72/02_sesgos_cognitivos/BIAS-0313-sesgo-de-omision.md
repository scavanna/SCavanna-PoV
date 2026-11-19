<!-- generado-ciso-excel sha256:76cc9e78cf6c8a7289b6ed337137249a634bf53efa1c341565a4297e87e79510 -->
# Sesgo de omisión

**ID:** `BIAS-0313` · **Categoría:** Sesgos cognitivos · **Prioridad editorial:** 16 · **Base de definición:** Apoyada por fuentes del catálogo

## Definición y alcance

El Sesgo de omisión juzga una acción dañina como peor que una inacción con consecuencias similares y favorece no actuar para evitar responsabilidad percibida.

**Límites:** La inacción puede ser correcta; debe evaluarse como una decisión con consecuencias, no como ausencia de decisión.

## Alias

- Omission Bias
- omission bias
- Sesgo de omisiÃ³n
- Sesgo de Omisión (Omission Bias)
- Sesgo por omisión

## Relevancia para el CISO

**Por qué:** No actuar parece menos culpable que una acción con el mismo daño esperado.

**Caso específico:** Se pospone revocar privilegios peligrosos porque una revocación podría interrumpir servicio.

**Pregunta guía:** ¿Se miden consecuencias de la inacción con el mismo rigor?

**Dominios:** Gobierno, Arquitectura

**Casos CISO adicionales:**

- Registrar el costo de no remediar junto al costo del cambio.
- Asignar responsables y plazos explícitos a decisiones de espera.

## Aplicación para arquitectura, SOC agéntico y Trust Framework

**Arquitectura:**

- Modelar riesgos de mantener el estado actual en cada alternativa.

**SOC agéntico — Alta:** Puede retrasar contención o escalamiento cuando la acción parece más arriesgada que esperar.

**Trust Framework — Alta:** La rendición de cuentas debe incluir decisiones de no actuar y su riesgo residual.

## Práctica y evaluación

**Ejercicios:**

- Resolver un caso presentando la inacción como una opción activa.
- Redactar un pre-mortem de no implementar un control.

**Métodos de evaluación:**

- Comparar daños esperados de acción e inacción con la misma escala.
- Auditar riesgos vencidos que permanecen sin decisión explícita.

**Controles o compensaciones:**

- Aplicar simetría de consecuencias entre hacer y no hacer.
- Usar fechas de caducidad para excepciones y aplazamientos.

## Pensadores y bibliografía identificados

**Personas y atribución documentada:**

- No consta en los documentos analizados.

**Referencias bibliográficas mencionadas en el corpus:**

- No consta en los documentos analizados.

## Trazabilidad documental

**Documentos contabilizados en el catálogo:** 31. **Localizadores representativos listados:** 3.

- 202508 - Cognitive Biases_ Comprehensive Analysis.docx — line:694 (Pasaje directo identificado)
- 250824 - Sesgos cognitivos en adultos mayores(1).docx — line:187 (Pasaje directo identificado)
- 250824 - Sesgos cognitivos en adultos.docx — line:647 (Pasaje directo identificado)

## Nota metodológica

La definición y las referencias se registran desde el catálogo; la prioridad, el caso concreto y la pregunta son adaptación editorial para el CISO, no evidencia experimental de eficacia. Un sesgo se gestiona con controles compensatorios y revisión independiente, no se promete eliminarlo mediante entrenamiento.

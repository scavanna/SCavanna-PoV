<!-- generado-gm24 sha256:85e4d22365e58ffe8c6ec5bdfc24aad3b796a9a85088fea47315729270ee7763 -->
# AMP-20 — Riesgo de modelos de IA

**Clase:** Ampliación Atlas propuesta · **Estado:** ampliación Atlas: título original; tesis propuesta [P], no aprobada · **Unidades:** G5.1.

## Enunciado y fuerza de la evidencia

Los modelos introducen riesgos propios —error, deriva, sesgo, manipulación y dependencia de proveedor— que deben evaluarse como riesgo empresarial.

**Importante:** en el Documento Maestro se documentó el **título** de `AMP-20`; la oración precedente es una **tesis propuesta [P]** en la matriz posterior, no una definición aprobada del programa.

## Desarrollo para el aprendizaje (derivación editorial)

Esta ampliación examina «Riesgo de modelos de IA» en la unidad `G5.1` (Supervisión de la Evaluación y Análisis). Su pregunta de diseño es qué cambiaría en la decisión de supervisar método, evidencia y escenarios alternativos antes de aceptar la puntuación al tomar en serio la tesis [P]. El vínculo `M4.2-K07` —Riesgos Emergentes— aporta una lente vecina: «Los riesgos emergentes surgen de cambios tecnológicos, adversariales, regulatorios o empresariales cuya frecuencia y consecuencias aún son inciertas». La relación no implica identidad de conceptos, aprobación del nuevo tema ni eficacia demostrada de una intervención.

En la organización ficticia del programa: Un modelo marca como improbable una intrusión en un proveedor crítico, pero la telemetría es parcial y el modelo no informa calibración. Una solución defendible debe contrastar estas alternativas: Priorizar por score opaco frente a comparar evidencia con hipótesis rivales y tasas base; las observaciones iniciales serían escenarios de riesgo, cobertura de logs, supuestos y datos de incidentes. El estudiante separa lo observado, lo inferido y lo aún no verificable antes de sugerir cambios de arquitectura, gobierno u operación.

El producto de aprendizaje propuesto es «dictamen de evaluación con incertidumbre, sesgos y pruebas refutatorias». Debe poder explicar por qué su recomendación es revisable y cómo verificaría que «No se confunde ausencia de detección con ausencia de riesgo». La propuesta permanece abierta a revisión curricular y técnica.

## Ejercicio y criterio de evaluación

**Práctica:** Ante «Un modelo marca como improbable una intrusión en un proveedor crítico, pero la telemetría es parcial y el modelo no informa calibración», explica qué aporta «Riesgo de modelos de IA» frente a las opciones «Priorizar por score opaco frente a comparar evidencia con hipótesis rivales y tasas base». Usa escenarios de riesgo, cobertura de logs, supuestos y datos de incidentes y entrega dictamen de evaluación con incertidumbre, sesgos y pruebas refutatorias. Distingue tesis [P] de evidencia obtenida y de supuestos de diseño.

**Validación:** Se acepta para revisión si identifica autoridad y límites, documenta fuentes y supuestos, compara al menos dos decisiones y demuestra «No se confunde ausencia de detección con ausencia de riesgo». La rúbrica de la unidad es una propuesta docente, no un estándar aprobado.

La guía de unidad desarrolla el escenario longitudinal, las ocho modalidades de ejercicio y la rúbrica: [abrir unidad](../../01_unidades/G5.1/Unidad_G5.1.md).

## Preguntas del método y comprobación

**Preguntas originales consolidadas (si hay vínculo directo o de corpus):**
- `PC-115` (interrogativa): ¿Cómo clasificamos los sistemas de IA por nivel de riesgo y qué controles mínimos exige cada nivel? — vínculo `AMP-20`.
- `PC-233` (interrogativa): ¿Qué responsabilidad asumimos como organización que despliega IA cuando falla un modelo o un proveedor, y está integrada en la gestión de riesgos empresariales? — vínculo `AMP-20`.
- `PC-286` (interrogativa): ¿Protegemos los modelos que entrenamos, ajustamos o alojamos (pesos, serialización, acceso e inferencia) con controles específicos, y no solo con los de infraestructura? — vínculo `AMP-20`.

**Ejemplos generados con plantillas mayéuticas documentadas:**
- `BM-0957` [Esencial]: ¿Qué problema de gobierno, riesgo o capacidad intenta resolver realmente «Riesgo de modelos de IA», y qué decisión debería mejorar si se comprende correctamente?
- `BM-0958` [Tensión]: ¿Qué supuesto habitual sobre «Riesgo de modelos de IA» podría ser falso o incompleto, y qué consecuencia tendría diseñar la seguridad como si fuera cierto?
- `BM-0959` [Decisión]: ¿Qué alternativa concreta elegiríamos a partir de «Riesgo de modelos de IA», quién debería decidirla y qué señal obligaría a revisarla?

Las preguntas de banco son construcciones mediante plantilla; no se presentan como citas de entrevistas. Fuente original: [preguntas consolidadas](../../../Curado02/02_metodo_mayeutico/src-preguntas-consolidadas__37298ee439f0.json).

## Procedencia y límites

[Matriz de 331 pre-ensayos](../../../Curado02/01_noviembre_2026/src-ai-ciso-atlas-ensayos-thenextciso-x-core-accountabilities-fy27-2026-11-05__5528a05eb5dd.xlsx), `06Ensayos!A304:T304` (idea `[P]`: `06Ensayos!I304`); [registro de consulta y estado [P]](../../00_control/AMP_ideas_propuestas_2026-11.json).

El nombre del marco, su aparición en el corpus y una alineación temática no acreditan dominio profesional, cumplimiento ni aprobación formal. Las referencias bibliográficas individuales solo se atribuyen si la fuente las identifica; véase el documento maestro para bibliografía general de NIST e ISACA y para la condición propuesta de sus mapeos.

[Documento Maestro](../../../Curado02/01_noviembre_2026/src-thenextciso-gm-24-documento-maestro__9b8c53df319d.md), sección `G5.1` (línea 392).

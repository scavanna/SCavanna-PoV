<!-- generado-gm24 sha256:7527126f33d9fc717f6c37b731516a433c0e30ca7b5373ab0e98e1f35c06d6f0 -->
# AMP-45 — Forense de agentes

**Clase:** Ampliación Atlas propuesta · **Estado:** ampliación Atlas: título original; tesis propuesta [P], no aprobada · **Unidades:** M5.2.

## Enunciado y fuerza de la evidencia

Investigar un incidente con agentes exige reconstruir instrucciones, herramientas invocadas, datos accedidos y decisiones; sin telemetría de agentes no hay forense.

**Importante:** en el Documento Maestro se documentó el **título** de `AMP-45`; la oración precedente es una **tesis propuesta [P]** en la matriz posterior, no una definición aprobada del programa.

## Desarrollo para el aprendizaje (derivación editorial)

Esta ampliación examina «Forense de agentes» en la unidad `M5.2` (Ejecución, Post-Mortem y Comunicación). Su pregunta de diseño es qué cambiaría en la decisión de reconstruir hechos, preservar evidencia, resolver contención y escalar decisiones de notificación al tomar en serio la tesis [P]. El vínculo `M5.2-K06` —Forense Digital— aporta una lente vecina: «La forense digital preserva y analiza evidencia de manera íntegra, contextual y trazable para reconstruir hechos y apoyar decisiones». La relación no implica identidad de conceptos, aprobación del nuevo tema ni eficacia demostrada de una intervención.

En la organización ficticia del programa: Tras contener un agente, faltan trazas sobre la secuencia de herramientas invocadas y se debate notificar una brecha. Una solución defendible debe contrastar estas alternativas: Restaurar de inmediato y perder registros frente a conservar trazas y recuperar por fases; las observaciones iniciales serían línea temporal, logs de agentes, cadena de custodia y evaluación de impacto. El estudiante separa lo observado, lo inferido y lo aún no verificable antes de sugerir cambios de arquitectura, gobierno u operación.

El producto de aprendizaje propuesto es «expediente de incidente con incertidumbre, autorizaciones y lecciones verificables». Debe poder explicar por qué su recomendación es revisable y cómo verificaría que «No se declara erradicación completa ni ausencia de exfiltración sin evidencia proporcionada». La propuesta permanece abierta a revisión curricular y técnica.

## Ejercicio y criterio de evaluación

**Práctica:** Ante «Tras contener un agente, faltan trazas sobre la secuencia de herramientas invocadas y se debate notificar una brecha», explica qué aporta «Forense de agentes» frente a las opciones «Restaurar de inmediato y perder registros frente a conservar trazas y recuperar por fases». Usa línea temporal, logs de agentes, cadena de custodia y evaluación de impacto y entrega expediente de incidente con incertidumbre, autorizaciones y lecciones verificables. Distingue tesis [P] de evidencia obtenida y de supuestos de diseño.

**Validación:** Se acepta para revisión si identifica autoridad y límites, documenta fuentes y supuestos, compara al menos dos decisiones y demuestra «No se declara erradicación completa ni ausencia de exfiltración sin evidencia proporcionada». La rúbrica de la unidad es una propuesta docente, no un estándar aprobado.

La guía de unidad desarrolla el escenario longitudinal, las ocho modalidades de ejercicio y la rúbrica: [abrir unidad](../../01_unidades/M5.2/Unidad_M5.2.md).

## Preguntas del método y comprobación

**Preguntas originales consolidadas (si hay vínculo directo o de corpus):**
- `PC-175` (interrogativa): ¿Podemos reconstruir de forma forense una cadena de acciones de varios agentes y herramientas con evidencia válida? — vínculo `AMP-45`.

**Ejemplos generados con plantillas mayéuticas documentadas:**
- `BM-1057` [Esencial]: ¿Qué problema de gobierno, riesgo o capacidad intenta resolver realmente «Forense de agentes», y qué decisión debería mejorar si se comprende correctamente?
- `BM-1058` [Tensión]: ¿Qué supuesto habitual sobre «Forense de agentes» podría ser falso o incompleto, y qué consecuencia tendría diseñar la seguridad como si fuera cierto?
- `BM-1059` [Consecuencia]: ¿Qué ocurre si una decisión sobre «Forense de agentes» resulta equivocada, qué impacto es tolerable y quién tiene autoridad para aceptarlo?

Las preguntas de banco son construcciones mediante plantilla; no se presentan como citas de entrevistas. Fuente original: [preguntas consolidadas](../../../Curado02/02_metodo_mayeutico/src-preguntas-consolidadas__37298ee439f0.json).

## Procedencia y límites

[Matriz de 331 pre-ensayos](../../../Curado02/01_noviembre_2026/src-ai-ciso-atlas-ensayos-thenextciso-x-core-accountabilities-fy27-2026-11-05__5528a05eb5dd.xlsx), `06Ensayos!A329:T329` (idea `[P]`: `06Ensayos!I329`); [registro de consulta y estado [P]](../../00_control/AMP_ideas_propuestas_2026-11.json).

El nombre del marco, su aparición en el corpus y una alineación temática no acreditan dominio profesional, cumplimiento ni aprobación formal. Las referencias bibliográficas individuales solo se atribuyen si la fuente las identifica; véase el documento maestro para bibliografía general de NIST e ISACA y para la condición propuesta de sus mapeos.

[Documento Maestro](../../../Curado02/01_noviembre_2026/src-thenextciso-gm-24-documento-maestro__9b8c53df319d.md), sección `M5.2` (línea 925).

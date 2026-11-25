<!-- generado-gm24 sha256:8d06f2d03f5be6af6518cbe620ce0ba2d531e1f18a1e6f1e6ef47e43c8bc6f55 -->
# AMP-46 — Trazabilidad de decisiones autónomas

**Clase:** Ampliación Atlas propuesta · **Estado:** ampliación Atlas: título original; tesis propuesta [P], no aprobada · **Unidades:** M5.2.

## Enunciado y fuerza de la evidencia

Registrar qué vio, qué decidió y con qué autoridad actuó un sistema autónomo es condición de rendición de cuentas y de mejora.

**Importante:** en el Documento Maestro se documentó el **título** de `AMP-46`; la oración precedente es una **tesis propuesta [P]** en la matriz posterior, no una definición aprobada del programa.

## Desarrollo para el aprendizaje (derivación editorial)

Esta ampliación examina «Trazabilidad de decisiones autónomas» en la unidad `M5.2` (Ejecución, Post-Mortem y Comunicación). Su pregunta de diseño es qué cambiaría en la decisión de reconstruir hechos, preservar evidencia, resolver contención y escalar decisiones de notificación al tomar en serio la tesis [P]. El vínculo `HC-012` —Confianza verificable en decisiones de IA— aporta una lente vecina: «Combina assurance, evidencia, ética y supervisión de sistemas cognitivos». La relación no implica identidad de conceptos, aprobación del nuevo tema ni eficacia demostrada de una intervención.

En la organización ficticia del programa: Tras contener un agente, faltan trazas sobre la secuencia de herramientas invocadas y se debate notificar una brecha. Una solución defendible debe contrastar estas alternativas: Restaurar de inmediato y perder registros frente a conservar trazas y recuperar por fases; las observaciones iniciales serían línea temporal, logs de agentes, cadena de custodia y evaluación de impacto. El estudiante separa lo observado, lo inferido y lo aún no verificable antes de sugerir cambios de arquitectura, gobierno u operación.

El producto de aprendizaje propuesto es «expediente de incidente con incertidumbre, autorizaciones y lecciones verificables». Debe poder explicar por qué su recomendación es revisable y cómo verificaría que «No se declara erradicación completa ni ausencia de exfiltración sin evidencia proporcionada». La propuesta permanece abierta a revisión curricular y técnica.

## Ejercicio y criterio de evaluación

**Práctica:** Ante «Tras contener un agente, faltan trazas sobre la secuencia de herramientas invocadas y se debate notificar una brecha», explica qué aporta «Trazabilidad de decisiones autónomas» frente a las opciones «Restaurar de inmediato y perder registros frente a conservar trazas y recuperar por fases». Usa línea temporal, logs de agentes, cadena de custodia y evaluación de impacto y entrega expediente de incidente con incertidumbre, autorizaciones y lecciones verificables. Distingue tesis [P] de evidencia obtenida y de supuestos de diseño.

**Validación:** Se acepta para revisión si identifica autoridad y límites, documenta fuentes y supuestos, compara al menos dos decisiones y demuestra «No se declara erradicación completa ni ausencia de exfiltración sin evidencia proporcionada». La rúbrica de la unidad es una propuesta docente, no un estándar aprobado.

La guía de unidad desarrolla el escenario longitudinal, las ocho modalidades de ejercicio y la rúbrica: [abrir unidad](../../01_unidades/M5.2/Unidad_M5.2.md).

## Preguntas del método y comprobación

**Preguntas originales consolidadas (si hay vínculo directo o de corpus):**
- `PC-140` (interrogativa): ¿Retenemos, auditamos y podemos buscar los prompts, respuestas y acciones de la IA según nuestras obligaciones legales? — vínculo `AMP-46`.
- `PC-172` (interrogativa): ¿Registramos de forma correlacionable quién pidió qué, qué hizo el agente, con qué identidad, herramientas y datos, sin depender del razonamiento interno del modelo? — vínculo `AMP-46`.
- `PA-018` (interrogativa): Si un regulador o un tribunal lo pide, ¿podemos explicar y reconstruir una decisión tomada o asistida por la IA? — vínculo `AMP-46`.

**Ejemplos generados con plantillas mayéuticas documentadas:**
- `BM-1061` [Esencial]: ¿Qué problema de gobierno, riesgo o capacidad intenta resolver realmente «Trazabilidad de decisiones autónomas», y qué decisión debería mejorar si se comprende correctamente?
- `BM-1062` [Tensión]: ¿Qué supuesto habitual sobre «Trazabilidad de decisiones autónomas» podría ser falso o incompleto, y qué consecuencia tendría diseñar la seguridad como si fuera cierto?
- `BM-1063` [Evidencia]: ¿Qué evidencia sería suficiente para sostener una afirmación sobre «Trazabilidad de decisiones autónomas», y qué evidencia aparentemente convincente no debería aceptarse como prueba?

Las preguntas de banco son construcciones mediante plantilla; no se presentan como citas de entrevistas. Fuente original: [preguntas consolidadas](../../../Curado02/02_metodo_mayeutico/src-preguntas-consolidadas__37298ee439f0.json).

## Procedencia y límites

[Matriz de 331 pre-ensayos](../../../Curado02/01_noviembre_2026/src-ai-ciso-atlas-ensayos-thenextciso-x-core-accountabilities-fy27-2026-11-05__5528a05eb5dd.xlsx), `06Ensayos!A330:T330` (idea `[P]`: `06Ensayos!I330`); [registro de consulta y estado [P]](../../00_control/AMP_ideas_propuestas_2026-11.json).

El nombre del marco, su aparición en el corpus y una alineación temática no acreditan dominio profesional, cumplimiento ni aprobación formal. Las referencias bibliográficas individuales solo se atribuyen si la fuente las identifica; véase el documento maestro para bibliografía general de NIST e ISACA y para la condición propuesta de sus mapeos.

[Documento Maestro](../../../Curado02/01_noviembre_2026/src-thenextciso-gm-24-documento-maestro__9b8c53df319d.md), sección `M5.2` (línea 925).

<!-- generado-gm24 sha256:ace4fad63d3ba50f1ef8cf2cabeb39b1970d8337827e5c8f8fafbb7157c735c3 -->
# AMP-38 — Pruebas de controles autónomos

**Clase:** Ampliación Atlas propuesta · **Estado:** ampliación Atlas: título original; tesis propuesta [P], no aprobada · **Unidades:** M3.2.

## Enunciado y fuerza de la evidencia

Los controles que actúan solos —bloqueo, contención, remediación— deben probarse en escenarios de falla y con rollback antes de confiarles decisiones.

**Importante:** en el Documento Maestro se documentó el **título** de `AMP-38`; la oración precedente es una **tesis propuesta [P]** en la matriz posterior, no una definición aprobada del programa.

## Desarrollo para el aprendizaje (derivación editorial)

Esta ampliación examina «Pruebas de controles autónomos» en la unidad `M3.2` (Selección, Implementación y Evaluación de Controles). Su pregunta de diseño es qué cambiaría en la decisión de elegir controles, escenarios de prueba, límites de despliegue y compensaciones al tomar en serio la tesis [P]. El vínculo `M3.2-K09` —Pruebas de Efectividad— aporta una lente vecina: «Las pruebas de efectividad verifican resultados bajo escenarios definidos, distinguiendo cobertura, operación y consecuencia observable». La relación no implica identidad de conceptos, aprobación del nuevo tema ni eficacia demostrada de una intervención.

En la organización ficticia del programa: Un control autónomo contiene malware en laboratorio, pero un falso positivo en producción podría detener la facturación. Una solución defendible debe contrastar estas alternativas: Activar bloqueo global frente a piloto por fases con rollback y test adversarial; las observaciones iniciales serían requisitos de control, casos de prueba, fallo simulado y POA&M. El estudiante separa lo observado, lo inferido y lo aún no verificable antes de sugerir cambios de arquitectura, gobierno u operación.

El producto de aprendizaje propuesto es «plan de aseguramiento con criterios de aceptación y reversión medibles». Debe poder explicar por qué su recomendación es revisable y cómo verificaría que «Un control configurado no se acredita como efectivo sin prueba independiente relevante». La propuesta permanece abierta a revisión curricular y técnica.

## Ejercicio y criterio de evaluación

**Práctica:** Ante «Un control autónomo contiene malware en laboratorio, pero un falso positivo en producción podría detener la facturación», explica qué aporta «Pruebas de controles autónomos» frente a las opciones «Activar bloqueo global frente a piloto por fases con rollback y test adversarial». Usa requisitos de control, casos de prueba, fallo simulado y POA&M y entrega plan de aseguramiento con criterios de aceptación y reversión medibles. Distingue tesis [P] de evidencia obtenida y de supuestos de diseño.

**Validación:** Se acepta para revisión si identifica autoridad y límites, documenta fuentes y supuestos, compara al menos dos decisiones y demuestra «Un control configurado no se acredita como efectivo sin prueba independiente relevante». La rúbrica de la unidad es una propuesta docente, no un estándar aprobado.

La guía de unidad desarrolla el escenario longitudinal, las ocho modalidades de ejercicio y la rúbrica: [abrir unidad](../../01_unidades/M3.2/Unidad_M3.2.md).

## Preguntas del método y comprobación

**Preguntas originales consolidadas (si hay vínculo directo o de corpus):**
- `PC-166` (interrogativa): ¿Comprobamos de forma recurrente que los filtros y guardrails bloquean lo que deben y no bloquean lo legítimo? — vínculo `AMP-38`.
- `PA-077` (interrogativa): ¿Cómo validan que los filtros y controles de la IA funcionan como esperan? — vínculo `AMP-38`.

**Ejemplos generados con plantillas mayéuticas documentadas:**
- `BM-1029` [Esencial]: ¿Qué problema de gobierno, riesgo o capacidad intenta resolver realmente «Pruebas de controles autónomos», y qué decisión debería mejorar si se comprende correctamente?
- `BM-1030` [Tensión]: ¿Qué supuesto habitual sobre «Pruebas de controles autónomos» podría ser falso o incompleto, y qué consecuencia tendría diseñar la seguridad como si fuera cierto?
- `BM-1031` [Evidencia]: ¿Qué evidencia sería suficiente para sostener una afirmación sobre «Pruebas de controles autónomos», y qué evidencia aparentemente convincente no debería aceptarse como prueba?

Las preguntas de banco son construcciones mediante plantilla; no se presentan como citas de entrevistas. Fuente original: [preguntas consolidadas](../../../Curado02/02_metodo_mayeutico/src-preguntas-consolidadas__37298ee439f0.json).

## Procedencia y límites

[Matriz de 331 pre-ensayos](../../../Curado02/01_noviembre_2026/src-ai-ciso-atlas-ensayos-thenextciso-x-core-accountabilities-fy27-2026-11-05__5528a05eb5dd.xlsx), `06Ensayos!A322:T322` (idea `[P]`: `06Ensayos!I322`); [registro de consulta y estado [P]](../../00_control/AMP_ideas_propuestas_2026-11.json).

El nombre del marco, su aparición en el corpus y una alineación temática no acreditan dominio profesional, cumplimiento ni aprobación formal. Las referencias bibliográficas individuales solo se atribuyen si la fuente las identifica; véase el documento maestro para bibliografía general de NIST e ISACA y para la condición propuesta de sus mapeos.

[Documento Maestro](../../../Curado02/01_noviembre_2026/src-thenextciso-gm-24-documento-maestro__9b8c53df319d.md), sección `M3.2` (línea 761).

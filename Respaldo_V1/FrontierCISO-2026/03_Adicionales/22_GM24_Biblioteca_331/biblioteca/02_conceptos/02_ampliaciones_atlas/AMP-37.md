<!-- generado-gm24 sha256:a6595b671c075914537c4febe61fa8ff0bdad5e19bed18ffccd5da278297255f -->
# AMP-37 — Evaluación adversarial de agentes

**Clase:** Ampliación Atlas propuesta · **Estado:** ampliación Atlas: título original; tesis propuesta [P], no aprobada · **Unidades:** M3.2.

## Enunciado y fuerza de la evidencia

Antes de producción, un agente debe resistir pruebas adversariales —inyección, abuso de herramientas, fuga de datos— con criterios de aceptación explícitos.

**Importante:** en el Documento Maestro se documentó el **título** de `AMP-37`; la oración precedente es una **tesis propuesta [P]** en la matriz posterior, no una definición aprobada del programa.

## Desarrollo para el aprendizaje (derivación editorial)

Esta ampliación examina «Evaluación adversarial de agentes» en la unidad `M3.2` (Selección, Implementación y Evaluación de Controles). Su pregunta de diseño es qué cambiaría en la decisión de elegir controles, escenarios de prueba, límites de despliegue y compensaciones al tomar en serio la tesis [P]. El vínculo `HC-032` —Evaluación adversarial de sistemas autónomos— aporta una lente vecina: «Integra threat modeling, pentesting, IA y autorización». La relación no implica identidad de conceptos, aprobación del nuevo tema ni eficacia demostrada de una intervención.

En la organización ficticia del programa: Un control autónomo contiene malware en laboratorio, pero un falso positivo en producción podría detener la facturación. Una solución defendible debe contrastar estas alternativas: Activar bloqueo global frente a piloto por fases con rollback y test adversarial; las observaciones iniciales serían requisitos de control, casos de prueba, fallo simulado y POA&M. El estudiante separa lo observado, lo inferido y lo aún no verificable antes de sugerir cambios de arquitectura, gobierno u operación.

El producto de aprendizaje propuesto es «plan de aseguramiento con criterios de aceptación y reversión medibles». Debe poder explicar por qué su recomendación es revisable y cómo verificaría que «Un control configurado no se acredita como efectivo sin prueba independiente relevante». La propuesta permanece abierta a revisión curricular y técnica.

## Ejercicio y criterio de evaluación

**Práctica:** Ante «Un control autónomo contiene malware en laboratorio, pero un falso positivo en producción podría detener la facturación», explica qué aporta «Evaluación adversarial de agentes» frente a las opciones «Activar bloqueo global frente a piloto por fases con rollback y test adversarial». Usa requisitos de control, casos de prueba, fallo simulado y POA&M y entrega plan de aseguramiento con criterios de aceptación y reversión medibles. Distingue tesis [P] de evidencia obtenida y de supuestos de diseño.

**Validación:** Se acepta para revisión si identifica autoridad y límites, documenta fuentes y supuestos, compara al menos dos decisiones y demuestra «Un control configurado no se acredita como efectivo sin prueba independiente relevante». La rúbrica de la unidad es una propuesta docente, no un estándar aprobado.

La guía de unidad desarrolla el escenario longitudinal, las ocho modalidades de ejercicio y la rúbrica: [abrir unidad](../../01_unidades/M3.2/Unidad_M3.2.md).

## Preguntas del método y comprobación

**Preguntas originales consolidadas (si hay vínculo directo o de corpus):**
- `PA-053` (interrogativa): ¿Cómo probamos un agente antes de ponerlo en producción y cada vez que cambia? — vínculo `AMP-37`.

**Ejemplos generados con plantillas mayéuticas documentadas:**
- `BM-1025` [Esencial]: ¿Qué problema de gobierno, riesgo o capacidad intenta resolver realmente «Evaluación adversarial de agentes», y qué decisión debería mejorar si se comprende correctamente?
- `BM-1026` [Tensión]: ¿Qué supuesto habitual sobre «Evaluación adversarial de agentes» podría ser falso o incompleto, y qué consecuencia tendría diseñar la seguridad como si fuera cierto?
- `BM-1027` [Evidencia]: ¿Qué evidencia sería suficiente para sostener una afirmación sobre «Evaluación adversarial de agentes», y qué evidencia aparentemente convincente no debería aceptarse como prueba?

Las preguntas de banco son construcciones mediante plantilla; no se presentan como citas de entrevistas. Fuente original: [preguntas consolidadas](../../../Curado02/02_metodo_mayeutico/src-preguntas-consolidadas__37298ee439f0.json).

## Procedencia y límites

[Matriz de 331 pre-ensayos](../../../Curado02/01_noviembre_2026/src-ai-ciso-atlas-ensayos-thenextciso-x-core-accountabilities-fy27-2026-11-05__5528a05eb5dd.xlsx), `06Ensayos!A321:T321` (idea `[P]`: `06Ensayos!I321`); [registro de consulta y estado [P]](../../00_control/AMP_ideas_propuestas_2026-11.json).

El nombre del marco, su aparición en el corpus y una alineación temática no acreditan dominio profesional, cumplimiento ni aprobación formal. Las referencias bibliográficas individuales solo se atribuyen si la fuente las identifica; véase el documento maestro para bibliografía general de NIST e ISACA y para la condición propuesta de sus mapeos.

[Documento Maestro](../../../Curado02/01_noviembre_2026/src-thenextciso-gm-24-documento-maestro__9b8c53df319d.md), sección `M3.2` (línea 761).

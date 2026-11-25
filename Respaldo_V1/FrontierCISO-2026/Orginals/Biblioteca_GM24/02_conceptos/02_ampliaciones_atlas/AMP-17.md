<!-- generado-gm24 sha256:a5c00075a065fc8bf71bf9a948e8a93d0ef97ae5a1719f65295ad894382f9f07 -->
# AMP-17 — Autoridad delegada

**Clase:** Ampliación Atlas propuesta · **Estado:** ampliación Atlas: título original; tesis propuesta [P], no aprobada · **Unidades:** G4.2.

## Enunciado y fuerza de la evidencia

Delegar autoridad en sistemas autónomos es una decisión de apetito de riesgo: qué acciones, con qué límites, bajo qué supervisión y quién puede revocarlas.

**Importante:** en el Documento Maestro se documentó el **título** de `AMP-17`; la oración precedente es una **tesis propuesta [P]** en la matriz posterior, no una definición aprobada del programa.

## Desarrollo para el aprendizaje (derivación editorial)

Esta ampliación examina «Autoridad delegada» en la unidad `G4.2` (Definición y Comunicación del Apetito de Riesgo). Su pregunta de diseño es qué cambiaría en la decisión de traducir apetito y tolerancia a acciones permitidas, sujetas a aprobación y prohibidas al tomar en serio la tesis [P]. El vínculo `HC-010` —Autonomía delegada y límites de acción— aporta una lente vecina: «Distingue capacidad técnica, permiso, delegación y ejecución de agentes de IA». La relación no implica identidad de conceptos, aprobación del nuevo tema ni eficacia demostrada de una intervención.

En la organización ficticia del programa: Un agente propone aislar cuentas y cargas de producción; el comité definió una tolerancia de interrupción, pero no umbrales para acciones automáticas. Una solución defendible debe contrastar estas alternativas: Aislamiento autónomo sin límites frente a autonomía graduada con aprobación, kill switch y registro; las observaciones iniciales serían declaración de apetito, BIA, procedimientos de escalamiento y prueba de impacto. El estudiante separa lo observado, lo inferido y lo aún no verificable antes de sugerir cambios de arquitectura, gobierno u operación.

El producto de aprendizaje propuesto es «matriz de autonomía y límites de riesgo con autoridad revocable». Debe poder explicar por qué su recomendación es revisable y cómo verificaría que «El agente nunca puede autoaprobar una acción fuera del apetito fijado por autoridad competente». La propuesta permanece abierta a revisión curricular y técnica.

## Ejercicio y criterio de evaluación

**Práctica:** Ante «Un agente propone aislar cuentas y cargas de producción; el comité definió una tolerancia de interrupción, pero no umbrales para acciones automáticas», explica qué aporta «Autoridad delegada» frente a las opciones «Aislamiento autónomo sin límites frente a autonomía graduada con aprobación, kill switch y registro». Usa declaración de apetito, BIA, procedimientos de escalamiento y prueba de impacto y entrega matriz de autonomía y límites de riesgo con autoridad revocable. Distingue tesis [P] de evidencia obtenida y de supuestos de diseño.

**Validación:** Se acepta para revisión si identifica autoridad y límites, documenta fuentes y supuestos, compara al menos dos decisiones y demuestra «El agente nunca puede autoaprobar una acción fuera del apetito fijado por autoridad competente». La rúbrica de la unidad es una propuesta docente, no un estándar aprobado.

La guía de unidad desarrolla el escenario longitudinal, las ocho modalidades de ejercicio y la rúbrica: [abrir unidad](../../01_unidades/G4.2/Unidad_G4.2.md).

## Preguntas del método y comprobación

**Preguntas originales consolidadas (si hay vínculo directo o de corpus):**
- `PC-128` (interrogativa): ¿Cuándo actúa un agente en nombre de un usuario y cuándo con autoridad propia, y cómo queda registrada esa diferencia? — vínculo `AMP-17`.
- `PC-133` (interrogativa): ¿Cómo controlamos la delegación entre agentes para que no se escalen privilegios ni se oculte quién originó una acción? — vínculo `AMP-17`.
- `PC-293` (interrogativa): ¿Nuestra gestión de identidades puede representar la delegación entre agentes sin que la autoridad se propague ni se diluya la responsabilidad? — vínculo `AMP-17`.

**Ejemplos generados con plantillas mayéuticas documentadas:**
- `BM-0945` [Esencial]: ¿Qué problema de gobierno, riesgo o capacidad intenta resolver realmente «Autoridad delegada», y qué decisión debería mejorar si se comprende correctamente?
- `BM-0946` [Tensión]: ¿Qué supuesto habitual sobre «Autoridad delegada» podría ser falso o incompleto, y qué consecuencia tendría diseñar la seguridad como si fuera cierto?
- `BM-0947` [Decisión]: ¿Qué alternativa concreta elegiríamos a partir de «Autoridad delegada», quién debería decidirla y qué señal obligaría a revisarla?

Las preguntas de banco son construcciones mediante plantilla; no se presentan como citas de entrevistas. Fuente original: [preguntas consolidadas](../../../Curado02/02_metodo_mayeutico/src-preguntas-consolidadas__37298ee439f0.json).

## Procedencia y límites

[Matriz de 331 pre-ensayos](../../../Curado02/01_noviembre_2026/src-ai-ciso-atlas-ensayos-thenextciso-x-core-accountabilities-fy27-2026-11-05__5528a05eb5dd.xlsx), `06Ensayos!A301:T301` (idea `[P]`: `06Ensayos!I301`); [registro de consulta y estado [P]](../../00_control/AMP_ideas_propuestas_2026-11.json).

El nombre del marco, su aparición en el corpus y una alineación temática no acreditan dominio profesional, cumplimiento ni aprobación formal. Las referencias bibliográficas individuales solo se atribuyen si la fuente las identifica; véase el documento maestro para bibliografía general de NIST e ISACA y para la condición propuesta de sus mapeos.

[Documento Maestro](../../../Curado02/01_noviembre_2026/src-thenextciso-gm-24-documento-maestro__9b8c53df319d.md), sección `G4.2` (línea 351).

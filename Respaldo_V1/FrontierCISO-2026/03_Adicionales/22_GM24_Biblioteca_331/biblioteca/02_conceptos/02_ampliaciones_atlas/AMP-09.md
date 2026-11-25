<!-- generado-gm24 sha256:6f5bdb74e2b1942f3a31a2c3b70aa2a9f8aacbcee7e98d10b83d9c0b234e480e -->
# AMP-09 — Policy-as-code

**Clase:** Ampliación Atlas propuesta · **Estado:** ampliación Atlas: título original; tesis propuesta [P], no aprobada · **Unidades:** G2.2.

## Enunciado y fuerza de la evidencia

Expresar políticas como código vuelve verificable su aplicación, pero exige control de versiones, gestión de excepciones y revisión humana para cambios de alto impacto.

**Importante:** en el Documento Maestro se documentó el **título** de `AMP-09`; la oración precedente es una **tesis propuesta [P]** en la matriz posterior, no una definición aprobada del programa.

## Desarrollo para el aprendizaje (derivación editorial)

Esta ampliación examina «Policy-as-code» en la unidad `G2.2` (Ciclo de Vida de Políticas, Estándares y Procedimientos). Su pregunta de diseño es qué cambiaría en la decisión de diseñar aprobación, caducidad, rollback y prueba de eficacia de la excepción automatizada al tomar en serio la tesis [P]. El vínculo `HC-004` —Política como código gobernado— aporta una lente vecina: «Une mandatos normativos con automatización verificable, excepciones y rollback». La relación no implica identidad de conceptos, aprobación del nuevo tema ni eficacia demostrada de una intervención.

En la organización ficticia del programa: Una política como código deshabilita credenciales de agentes, pero una excepción permanente deja abierto el acceso de emergencia. Una solución defendible debe contrastar estas alternativas: Excepciones sin vencimiento frente a excepciones con dueño, compensación y revisión automática; las observaciones iniciales serían política aprobada, repositorio de versiones, registros de excepción. El estudiante separa lo observado, lo inferido y lo aún no verificable antes de sugerir cambios de arquitectura, gobierno u operación.

El producto de aprendizaje propuesto es «jerarquía documental y flujo de cambios con control de excepciones». Debe poder explicar por qué su recomendación es revisable y cómo verificaría que «Un cambio en producción no hereda autoridad de un commit técnico ni elimina el deber de supervisión». La propuesta permanece abierta a revisión curricular y técnica.

## Ejercicio y criterio de evaluación

**Práctica:** Ante «Una política como código deshabilita credenciales de agentes, pero una excepción permanente deja abierto el acceso de emergencia», explica qué aporta «Policy-as-code» frente a las opciones «Excepciones sin vencimiento frente a excepciones con dueño, compensación y revisión automática». Usa política aprobada, repositorio de versiones, registros de excepción y entrega jerarquía documental y flujo de cambios con control de excepciones. Distingue tesis [P] de evidencia obtenida y de supuestos de diseño.

**Validación:** Se acepta para revisión si identifica autoridad y límites, documenta fuentes y supuestos, compara al menos dos decisiones y demuestra «Un cambio en producción no hereda autoridad de un commit técnico ni elimina el deber de supervisión». La rúbrica de la unidad es una propuesta docente, no un estándar aprobado.

La guía de unidad desarrolla el escenario longitudinal, las ocho modalidades de ejercicio y la rúbrica: [abrir unidad](../../01_unidades/G2.2/Unidad_G2.2.md).

## Preguntas del método y comprobación

**Preguntas originales consolidadas (si hay vínculo directo o de corpus):**
- Sin pregunta original vinculada explícitamente.

**Ejemplos generados con plantillas mayéuticas documentadas:**
- `BM-0913` [Esencial]: ¿Qué problema de gobierno, riesgo o capacidad intenta resolver realmente «Policy-as-code», y qué decisión debería mejorar si se comprende correctamente?
- `BM-0914` [Tensión]: ¿Qué supuesto habitual sobre «Policy-as-code» podría ser falso o incompleto, y qué consecuencia tendría diseñar la seguridad como si fuera cierto?
- `BM-0915` [Validación]: ¿Cómo probaríamos que «Policy-as-code» funciona en condiciones reales, incluidas fallas, excepciones y dependencias, en lugar de asumir eficacia por configuración?

Las preguntas de banco son construcciones mediante plantilla; no se presentan como citas de entrevistas. Fuente original: [preguntas consolidadas](../../../Curado02/02_metodo_mayeutico/src-preguntas-consolidadas__37298ee439f0.json).

## Procedencia y límites

[Matriz de 331 pre-ensayos](../../../Curado02/01_noviembre_2026/src-ai-ciso-atlas-ensayos-thenextciso-x-core-accountabilities-fy27-2026-11-05__5528a05eb5dd.xlsx), `06Ensayos!A293:T293` (idea `[P]`: `06Ensayos!I293`); [registro de consulta y estado [P]](../../00_control/AMP_ideas_propuestas_2026-11.json).

El nombre del marco, su aparición en el corpus y una alineación temática no acreditan dominio profesional, cumplimiento ni aprobación formal. Las referencias bibliográficas individuales solo se atribuyen si la fuente las identifica; véase el documento maestro para bibliografía general de NIST e ISACA y para la condición propuesta de sus mapeos.

[Documento Maestro](../../../Curado02/01_noviembre_2026/src-thenextciso-gm-24-documento-maestro__9b8c53df319d.md), sección `G2.2` (línea 187).

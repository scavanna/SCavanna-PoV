<!-- generado-gm24 sha256:9b090ced128c61f73d468a2a8c887785970e7881aaf1ce47d5f3cc492904e58e -->
# AMP-10 — Gobierno de excepciones automatizadas

**Clase:** Ampliación Atlas propuesta · **Estado:** ampliación Atlas: título original; tesis propuesta [P], no aprobada · **Unidades:** G2.2.

## Enunciado y fuerza de la evidencia

Cuando las excepciones se conceden y vencen automáticamente, la automatización puede normalizar el desvío; se requieren dueño, caducidad y evidencia.

**Importante:** en el Documento Maestro se documentó el **título** de `AMP-10`; la oración precedente es una **tesis propuesta [P]** en la matriz posterior, no una definición aprobada del programa.

## Desarrollo para el aprendizaje (derivación editorial)

Esta ampliación examina «Gobierno de excepciones automatizadas» en la unidad `G2.2` (Ciclo de Vida de Políticas, Estándares y Procedimientos). Su pregunta de diseño es qué cambiaría en la decisión de diseñar aprobación, caducidad, rollback y prueba de eficacia de la excepción automatizada al tomar en serio la tesis [P]. El vínculo `HC-028` —Gestión de excepciones y compensaciones— aporta una lente vecina: «Conecta política, aceptación residual, controles alternativos y caducidad». La relación no implica identidad de conceptos, aprobación del nuevo tema ni eficacia demostrada de una intervención.

En la organización ficticia del programa: Una política como código deshabilita credenciales de agentes, pero una excepción permanente deja abierto el acceso de emergencia. Una solución defendible debe contrastar estas alternativas: Excepciones sin vencimiento frente a excepciones con dueño, compensación y revisión automática; las observaciones iniciales serían política aprobada, repositorio de versiones, registros de excepción. El estudiante separa lo observado, lo inferido y lo aún no verificable antes de sugerir cambios de arquitectura, gobierno u operación.

El producto de aprendizaje propuesto es «jerarquía documental y flujo de cambios con control de excepciones». Debe poder explicar por qué su recomendación es revisable y cómo verificaría que «Un cambio en producción no hereda autoridad de un commit técnico ni elimina el deber de supervisión». La propuesta permanece abierta a revisión curricular y técnica.

## Ejercicio y criterio de evaluación

**Práctica:** Ante «Una política como código deshabilita credenciales de agentes, pero una excepción permanente deja abierto el acceso de emergencia», explica qué aporta «Gobierno de excepciones automatizadas» frente a las opciones «Excepciones sin vencimiento frente a excepciones con dueño, compensación y revisión automática». Usa política aprobada, repositorio de versiones, registros de excepción y entrega jerarquía documental y flujo de cambios con control de excepciones. Distingue tesis [P] de evidencia obtenida y de supuestos de diseño.

**Validación:** Se acepta para revisión si identifica autoridad y límites, documenta fuentes y supuestos, compara al menos dos decisiones y demuestra «Un cambio en producción no hereda autoridad de un commit técnico ni elimina el deber de supervisión». La rúbrica de la unidad es una propuesta docente, no un estándar aprobado.

La guía de unidad desarrolla el escenario longitudinal, las ocho modalidades de ejercicio y la rúbrica: [abrir unidad](../../01_unidades/G2.2/Unidad_G2.2.md).

## Preguntas del método y comprobación

**Preguntas originales consolidadas (si hay vínculo directo o de corpus):**
- Sin pregunta original vinculada explícitamente.

**Ejemplos generados con plantillas mayéuticas documentadas:**
- `BM-0917` [Esencial]: ¿Qué problema de gobierno, riesgo o capacidad intenta resolver realmente «Gobierno de excepciones automatizadas», y qué decisión debería mejorar si se comprende correctamente?
- `BM-0918` [Tensión]: ¿Qué supuesto habitual sobre «Gobierno de excepciones automatizadas» podría ser falso o incompleto, y qué consecuencia tendría diseñar la seguridad como si fuera cierto?
- `BM-0919` [Consecuencia]: ¿Qué ocurre si una decisión sobre «Gobierno de excepciones automatizadas» resulta equivocada, qué impacto es tolerable y quién tiene autoridad para aceptarlo?

Las preguntas de banco son construcciones mediante plantilla; no se presentan como citas de entrevistas. Fuente original: [preguntas consolidadas](../../../Curado02/02_metodo_mayeutico/src-preguntas-consolidadas__37298ee439f0.json).

## Procedencia y límites

[Matriz de 331 pre-ensayos](../../../Curado02/01_noviembre_2026/src-ai-ciso-atlas-ensayos-thenextciso-x-core-accountabilities-fy27-2026-11-05__5528a05eb5dd.xlsx), `06Ensayos!A294:T294` (idea `[P]`: `06Ensayos!I294`); [registro de consulta y estado [P]](../../00_control/AMP_ideas_propuestas_2026-11.json).

El nombre del marco, su aparición en el corpus y una alineación temática no acreditan dominio profesional, cumplimiento ni aprobación formal. Las referencias bibliográficas individuales solo se atribuyen si la fuente las identifica; véase el documento maestro para bibliografía general de NIST e ISACA y para la condición propuesta de sus mapeos.

[Documento Maestro](../../../Curado02/01_noviembre_2026/src-thenextciso-gm-24-documento-maestro__9b8c53df319d.md), sección `G2.2` (línea 187).

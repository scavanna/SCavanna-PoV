<!-- generado-gm24 sha256:375d3233b6df35740f7523fdb46801d245419aaf945857304cbd354f35a99f5c -->
# AMP-48 — Dependencias de modelos

**Clase:** Ampliación Atlas propuesta · **Estado:** ampliación Atlas: título original; tesis propuesta [P], no aprobada · **Unidades:** M6.1.

## Enunciado y fuerza de la evidencia

Depender de un modelo o proveedor de IA crea riesgo de concentración y de cambio no controlado: hay que mapearlo y prever alternativas.

**Importante:** en el Documento Maestro se documentó el **título** de `AMP-48`; la oración precedente es una **tesis propuesta [P]** en la matriz posterior, no una definición aprobada del programa.

## Desarrollo para el aprendizaje (derivación editorial)

Esta ampliación examina «Dependencias de modelos» en la unidad `M6.1` (Continuidad, DRP y Resiliencia Operativa). Su pregunta de diseño es qué cambiaría en la decisión de definir la restauración completa de un servicio ia con objetivos y pruebas funcionales al tomar en serio la tesis [P]. El vínculo `HC-023` —Riesgo de concentración tecnológica— aporta una lente vecina: «Integra dependencias de proveedores, resiliencia, arquitectura y estrategia». La relación no implica identidad de conceptos, aprobación del nuevo tema ni eficacia demostrada de una intervención.

En la organización ficticia del programa: Las copias de seguridad restauran servidores, pero los índices RAG y las instrucciones de agentes provienen de una versión comprometida. Una solución defendible debe contrastar estas alternativas: Recuperar solo infraestructura frente a restaurar datos, modelos, identidades, conectores e índices verificados; las observaciones iniciales serían BIA, backups inmutables, pruebas DRP, inventario de dependencias de modelos. El estudiante separa lo observado, lo inferido y lo aún no verificable antes de sugerir cambios de arquitectura, gobierno u operación.

El producto de aprendizaje propuesto es «plan de recuperación de IA con secuencia, pruebas y criterios de aceptación». Debe poder explicar por qué su recomendación es revisable y cómo verificaría que «Una copia disponible no prueba que el servicio de negocio vuelva a operar de forma íntegra». La propuesta permanece abierta a revisión curricular y técnica.

## Ejercicio y criterio de evaluación

**Práctica:** Ante «Las copias de seguridad restauran servidores, pero los índices RAG y las instrucciones de agentes provienen de una versión comprometida», explica qué aporta «Dependencias de modelos» frente a las opciones «Recuperar solo infraestructura frente a restaurar datos, modelos, identidades, conectores e índices verificados». Usa BIA, backups inmutables, pruebas DRP, inventario de dependencias de modelos y entrega plan de recuperación de IA con secuencia, pruebas y criterios de aceptación. Distingue tesis [P] de evidencia obtenida y de supuestos de diseño.

**Validación:** Se acepta para revisión si identifica autoridad y límites, documenta fuentes y supuestos, compara al menos dos decisiones y demuestra «Una copia disponible no prueba que el servicio de negocio vuelva a operar de forma íntegra». La rúbrica de la unidad es una propuesta docente, no un estándar aprobado.

La guía de unidad desarrolla el escenario longitudinal, las ocho modalidades de ejercicio y la rúbrica: [abrir unidad](../../01_unidades/M6.1/Unidad_M6.1.md).

## Preguntas del método y comprobación

**Preguntas originales consolidadas (si hay vínculo directo o de corpus):**
- `PC-184` (interrogativa): ¿Qué haríamos si un proveedor cambia, retira o degrada un modelo del que depende un proceso crítico, o cambia sus políticas de datos? — vínculo `AMP-48`.
- `PA-054` (interrogativa): ¿Qué pasa si el proveedor retira o cambia el modelo del que depende un proceso crítico? — vínculo `AMP-48`.

**Ejemplos generados con plantillas mayéuticas documentadas:**
- `BM-1069` [Esencial]: ¿Qué problema de gobierno, riesgo o capacidad intenta resolver realmente «Dependencias de modelos», y qué decisión debería mejorar si se comprende correctamente?
- `BM-1070` [Tensión]: ¿Qué supuesto habitual sobre «Dependencias de modelos» podría ser falso o incompleto, y qué consecuencia tendría diseñar la seguridad como si fuera cierto?
- `BM-1071` [Consecuencia]: ¿Qué ocurre si una decisión sobre «Dependencias de modelos» resulta equivocada, qué impacto es tolerable y quién tiene autoridad para aceptarlo?

Las preguntas de banco son construcciones mediante plantilla; no se presentan como citas de entrevistas. Fuente original: [preguntas consolidadas](../../../Curado02/02_metodo_mayeutico/src-preguntas-consolidadas__37298ee439f0.json).

## Procedencia y límites

[Matriz de 331 pre-ensayos](../../../Curado02/01_noviembre_2026/src-ai-ciso-atlas-ensayos-thenextciso-x-core-accountabilities-fy27-2026-11-05__5528a05eb5dd.xlsx), `06Ensayos!A332:T332` (idea `[P]`: `06Ensayos!I332`); [registro de consulta y estado [P]](../../00_control/AMP_ideas_propuestas_2026-11.json).

El nombre del marco, su aparición en el corpus y una alineación temática no acreditan dominio profesional, cumplimiento ni aprobación formal. Las referencias bibliográficas individuales solo se atribuyen si la fuente las identifica; véase el documento maestro para bibliografía general de NIST e ISACA y para la condición propuesta de sus mapeos.

[Documento Maestro](../../../Curado02/01_noviembre_2026/src-thenextciso-gm-24-documento-maestro__9b8c53df319d.md), sección `M6.1` (línea 966).

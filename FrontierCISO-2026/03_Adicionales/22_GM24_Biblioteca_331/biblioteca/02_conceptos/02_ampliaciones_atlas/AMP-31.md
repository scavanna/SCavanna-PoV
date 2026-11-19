<!-- generado-gm24 sha256:5a23ca5ce004c4fe8b75d61d00025e216437a9eb70315edcea8f177e3608a622 -->
# AMP-31 — DSPM

**Clase:** Ampliación Atlas propuesta · **Estado:** ampliación Atlas: título original; tesis propuesta [P], no aprobada · **Unidades:** M2.1.

## Enunciado y fuerza de la evidencia

DSPM convierte la protección de datos en gestión continua de exposición: dónde está el dato sensible, quién accede y qué remediar primero.

**Importante:** en el Documento Maestro se documentó el **título** de `AMP-31`; la oración precedente es una **tesis propuesta [P]** en la matriz posterior, no una definición aprobada del programa.

## Desarrollo para el aprendizaje (derivación editorial)

Esta ampliación examina «DSPM» en la unidad `M2.1` (Gestión de Activos y Seguridad del Ciclo de Vida de los Datos). Su pregunta de diseño es qué cambiaría en la decisión de inventariar, clasificar, restringir y verificar acceso a datos usados por ia al tomar en serio la tesis [P]. El vínculo `HC-011` —Seguridad de datos en la IA empresarial— aporta una lente vecina: «Relaciona clasificación, finalidad, permisos, flujos y controles de aplicaciones de IA». La relación no implica identidad de conceptos, aprobación del nuevo tema ni eficacia demostrada de una intervención.

En la organización ficticia del programa: Un asistente RAG recupera documentos compartidos en exceso y retiene fragmentos sensibles más tiempo del permitido. Una solución defendible debe contrastar estas alternativas: Apagar toda búsqueda frente a segmentar corpus por sensibilidad y corregir permisos heredados; las observaciones iniciales serían inventario de repositorios, clasificación, permisos, retención y logs de recuperación. El estudiante separa lo observado, lo inferido y lo aún no verificable antes de sugerir cambios de arquitectura, gobierno u operación.

El producto de aprendizaje propuesto es «mapa de exposición de datos con remediaciones priorizadas y prueba de acceso». Debe poder explicar por qué su recomendación es revisable y cómo verificaría que «Clasificar datos sin corregir su acceso no demuestra que la IA respete su alcance». La propuesta permanece abierta a revisión curricular y técnica.

## Ejercicio y criterio de evaluación

**Práctica:** Ante «Un asistente RAG recupera documentos compartidos en exceso y retiene fragmentos sensibles más tiempo del permitido», explica qué aporta «DSPM» frente a las opciones «Apagar toda búsqueda frente a segmentar corpus por sensibilidad y corregir permisos heredados». Usa inventario de repositorios, clasificación, permisos, retención y logs de recuperación y entrega mapa de exposición de datos con remediaciones priorizadas y prueba de acceso. Distingue tesis [P] de evidencia obtenida y de supuestos de diseño.

**Validación:** Se acepta para revisión si identifica autoridad y límites, documenta fuentes y supuestos, compara al menos dos decisiones y demuestra «Clasificar datos sin corregir su acceso no demuestra que la IA respete su alcance». La rúbrica de la unidad es una propuesta docente, no un estándar aprobado.

La guía de unidad desarrolla el escenario longitudinal, las ocho modalidades de ejercicio y la rúbrica: [abrir unidad](../../01_unidades/M2.1/Unidad_M2.1.md).

## Preguntas del método y comprobación

**Preguntas originales consolidadas (si hay vínculo directo o de corpus):**
- `PC-037` (interrogativa): ¿Sabemos dónde están nuestros datos sensibles, quién accede a ellos y cuán sobreexpuestos están? — vínculo `AMP-31`.
- `PA-070` (interrogativa): ¿Cómo protegen los datos de los clientes y cómo saben quién accede a ellos? — vínculo `AMP-31`.

**Ejemplos generados con plantillas mayéuticas documentadas:**
- `BM-1001` [Esencial]: ¿Qué problema de gobierno, riesgo o capacidad intenta resolver realmente «DSPM», y qué decisión debería mejorar si se comprende correctamente?
- `BM-1002` [Tensión]: ¿Qué supuesto habitual sobre «DSPM» podría ser falso o incompleto, y qué consecuencia tendría diseñar la seguridad como si fuera cierto?
- `BM-1003` [Validación]: ¿Cómo probaríamos que «DSPM» funciona en condiciones reales, incluidas fallas, excepciones y dependencias, en lugar de asumir eficacia por configuración?

Las preguntas de banco son construcciones mediante plantilla; no se presentan como citas de entrevistas. Fuente original: [preguntas consolidadas](../../../Curado02/02_metodo_mayeutico/src-preguntas-consolidadas__37298ee439f0.json).

## Procedencia y límites

[Matriz de 331 pre-ensayos](../../../Curado02/01_noviembre_2026/src-ai-ciso-atlas-ensayos-thenextciso-x-core-accountabilities-fy27-2026-11-05__5528a05eb5dd.xlsx), `06Ensayos!A315:T315` (idea `[P]`: `06Ensayos!I315`); [registro de consulta y estado [P]](../../00_control/AMP_ideas_propuestas_2026-11.json).

El nombre del marco, su aparición en el corpus y una alineación temática no acreditan dominio profesional, cumplimiento ni aprobación formal. Las referencias bibliográficas individuales solo se atribuyen si la fuente las identifica; véase el documento maestro para bibliografía general de NIST e ISACA y para la condición propuesta de sus mapeos.

[Documento Maestro](../../../Curado02/01_noviembre_2026/src-thenextciso-gm-24-documento-maestro__9b8c53df319d.md), sección `M2.1` (línea 638).

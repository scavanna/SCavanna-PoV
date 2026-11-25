<!-- generado-gm24 sha256:dc45a0e10ede46db96d587a6ea05325e538b3a5aeb120d978dd863218300516a -->
# AMP-35 — Arquitectura de sistemas agénticos

**Clase:** Ampliación Atlas propuesta · **Estado:** ampliación Atlas: título original; tesis propuesta [P], no aprobada · **Unidades:** M3.1.

## Enunciado y fuerza de la evidencia

Diseñar sistemas agénticos seguros implica separar planificación, herramientas, datos y permisos, con puntos de control y observabilidad desde el diseño.

**Importante:** en el Documento Maestro se documentó el **título** de `AMP-35`; la oración precedente es una **tesis propuesta [P]** en la matriz posterior, no una definición aprobada del programa.

## Desarrollo para el aprendizaje (derivación editorial)

Esta ampliación examina «Arquitectura de sistemas agénticos» en la unidad `M3.1` (Arquitectura de Seguridad, Ingeniería y Diseño (Incl. Zero Trust)). Su pregunta de diseño es qué cambiaría en la decisión de diseñar límites de confianza, aislamiento y puntos de observación antes de producción al tomar en serio la tesis [P]. El vínculo `M6.2-K04` —Seguridad IA— aporta una lente vecina: «La seguridad de IA protege modelos, datos, herramientas, agentes y procesos ante amenazas específicas y consecuencias de autonomía». La relación no implica identidad de conceptos, aprobación del nuevo tema ni eficacia demostrada de una intervención.

En la organización ficticia del programa: Un agente puede invocar conectores de correo, endpoints y repositorios desde un mismo plano de control sin separación de permisos. Una solución defendible debe contrastar estas alternativas: Acceso amplio para acelerar integración frente a herramientas acotadas por identidad, entorno y riesgo; las observaciones iniciales serían diagrama de flujos, permisos de herramientas, dependencias y requisitos de rollback. El estudiante separa lo observado, lo inferido y lo aún no verificable antes de sugerir cambios de arquitectura, gobierno u operación.

El producto de aprendizaje propuesto es «arquitectura de agentes con threat model y controles por límite». Debe poder explicar por qué su recomendación es revisable y cómo verificaría que «La separación de funciones y el mínimo privilegio se prueban, no se infieren del diagrama». La propuesta permanece abierta a revisión curricular y técnica.

## Ejercicio y criterio de evaluación

**Práctica:** Ante «Un agente puede invocar conectores de correo, endpoints y repositorios desde un mismo plano de control sin separación de permisos», explica qué aporta «Arquitectura de sistemas agénticos» frente a las opciones «Acceso amplio para acelerar integración frente a herramientas acotadas por identidad, entorno y riesgo». Usa diagrama de flujos, permisos de herramientas, dependencias y requisitos de rollback y entrega arquitectura de agentes con threat model y controles por límite. Distingue tesis [P] de evidencia obtenida y de supuestos de diseño.

**Validación:** Se acepta para revisión si identifica autoridad y límites, documenta fuentes y supuestos, compara al menos dos decisiones y demuestra «La separación de funciones y el mínimo privilegio se prueban, no se infieren del diagrama». La rúbrica de la unidad es una propuesta docente, no un estándar aprobado.

La guía de unidad desarrolla el escenario longitudinal, las ocho modalidades de ejercicio y la rúbrica: [abrir unidad](../../01_unidades/M3.1/Unidad_M3.1.md).

## Preguntas del método y comprobación

**Preguntas originales consolidadas (si hay vínculo directo o de corpus):**
- `PC-153` (interrogativa): ¿Conocemos los modos de falla propios de los sistemas agénticos (memoria envenenada, objetivos secuestrados, colusión entre agentes, fallos en cascada) y cuáles aplican a nuestros casos? — vínculo `AMP-35`.
- `PC-230` (interrogativa): Antes de escalar agentes, ¿tenemos inventario de agentes, modelos, herramientas, memorias y proveedores, con fronteras de confianza y dueños que aprueben permisos y riesgos? — vínculo `AMP-35`.
- `PC-262` (interrogativa): Cuando varios agentes colaboran, ¿qué evalúa cada acción propuesta antes de ejecutarla, y cómo evitamos bucles y escaladas de autoridad entre agentes? — vínculo `AMP-35`.

**Ejemplos generados con plantillas mayéuticas documentadas:**
- `BM-1017` [Esencial]: ¿Qué problema de gobierno, riesgo o capacidad intenta resolver realmente «Arquitectura de sistemas agénticos», y qué decisión debería mejorar si se comprende correctamente?
- `BM-1018` [Tensión]: ¿Qué supuesto habitual sobre «Arquitectura de sistemas agénticos» podría ser falso o incompleto, y qué consecuencia tendría diseñar la seguridad como si fuera cierto?
- `BM-1019` [Decisión]: ¿Qué alternativa concreta elegiríamos a partir de «Arquitectura de sistemas agénticos», quién debería decidirla y qué señal obligaría a revisarla?

Las preguntas de banco son construcciones mediante plantilla; no se presentan como citas de entrevistas. Fuente original: [preguntas consolidadas](../../../Curado02/02_metodo_mayeutico/src-preguntas-consolidadas__37298ee439f0.json).

## Procedencia y límites

[Matriz de 331 pre-ensayos](../../../Curado02/01_noviembre_2026/src-ai-ciso-atlas-ensayos-thenextciso-x-core-accountabilities-fy27-2026-11-05__5528a05eb5dd.xlsx), `06Ensayos!A319:T319` (idea `[P]`: `06Ensayos!I319`); [registro de consulta y estado [P]](../../00_control/AMP_ideas_propuestas_2026-11.json).

El nombre del marco, su aparición en el corpus y una alineación temática no acreditan dominio profesional, cumplimiento ni aprobación formal. Las referencias bibliográficas individuales solo se atribuyen si la fuente las identifica; véase el documento maestro para bibliografía general de NIST e ISACA y para la condición propuesta de sus mapeos.

[Documento Maestro](../../../Curado02/01_noviembre_2026/src-thenextciso-gm-24-documento-maestro__9b8c53df319d.md), sección `M3.1` (línea 720).

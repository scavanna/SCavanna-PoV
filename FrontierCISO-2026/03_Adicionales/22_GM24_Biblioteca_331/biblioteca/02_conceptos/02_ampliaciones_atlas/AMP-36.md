<!-- generado-gm24 sha256:d213033883464102a4400454cd55f7d23facc9c5ef9b7fd6fea790abd0001f09 -->
# AMP-36 — Límites de herramientas y permisos

**Clase:** Ampliación Atlas propuesta · **Estado:** ampliación Atlas: título original; tesis propuesta [P], no aprobada · **Unidades:** M3.1.

## Enunciado y fuerza de la evidencia

Las herramientas y conectores definen lo que un agente puede hacer: acotar alcances, aprobar acciones de alto impacto y registrar cada invocación.

**Importante:** en el Documento Maestro se documentó el **título** de `AMP-36`; la oración precedente es una **tesis propuesta [P]** en la matriz posterior, no una definición aprobada del programa.

## Desarrollo para el aprendizaje (derivación editorial)

Esta ampliación examina «Límites de herramientas y permisos» en la unidad `M3.1` (Arquitectura de Seguridad, Ingeniería y Diseño (Incl. Zero Trust)). Su pregunta de diseño es qué cambiaría en la decisión de diseñar límites de confianza, aislamiento y puntos de observación antes de producción al tomar en serio la tesis [P]. El vínculo `M3.1-K09` —Mínimo Privilegio (Arquitectura)— aporta una lente vecina: «El mínimo privilegio debe diseñarse en identidades, APIs, herramientas, datos y procesos con mecanismos de revisión y revocación». La relación no implica identidad de conceptos, aprobación del nuevo tema ni eficacia demostrada de una intervención.

En la organización ficticia del programa: Un agente puede invocar conectores de correo, endpoints y repositorios desde un mismo plano de control sin separación de permisos. Una solución defendible debe contrastar estas alternativas: Acceso amplio para acelerar integración frente a herramientas acotadas por identidad, entorno y riesgo; las observaciones iniciales serían diagrama de flujos, permisos de herramientas, dependencias y requisitos de rollback. El estudiante separa lo observado, lo inferido y lo aún no verificable antes de sugerir cambios de arquitectura, gobierno u operación.

El producto de aprendizaje propuesto es «arquitectura de agentes con threat model y controles por límite». Debe poder explicar por qué su recomendación es revisable y cómo verificaría que «La separación de funciones y el mínimo privilegio se prueban, no se infieren del diagrama». La propuesta permanece abierta a revisión curricular y técnica.

## Ejercicio y criterio de evaluación

**Práctica:** Ante «Un agente puede invocar conectores de correo, endpoints y repositorios desde un mismo plano de control sin separación de permisos», explica qué aporta «Límites de herramientas y permisos» frente a las opciones «Acceso amplio para acelerar integración frente a herramientas acotadas por identidad, entorno y riesgo». Usa diagrama de flujos, permisos de herramientas, dependencias y requisitos de rollback y entrega arquitectura de agentes con threat model y controles por límite. Distingue tesis [P] de evidencia obtenida y de supuestos de diseño.

**Validación:** Se acepta para revisión si identifica autoridad y límites, documenta fuentes y supuestos, compara al menos dos decisiones y demuestra «La separación de funciones y el mínimo privilegio se prueban, no se infieren del diagrama». La rúbrica de la unidad es una propuesta docente, no un estándar aprobado.

La guía de unidad desarrolla el escenario longitudinal, las ocho modalidades de ejercicio y la rúbrica: [abrir unidad](../../01_unidades/M3.1/Unidad_M3.1.md).

## Preguntas del método y comprobación

**Preguntas originales consolidadas (si hay vínculo directo o de corpus):**
- `PC-129` (interrogativa): ¿Aplicamos mínimo privilegio y agencia mínima a los agentes: solo los datos, herramientas y acciones necesarios para su propósito? — vínculo `AMP-36`.
- `PC-147` (interrogativa): ¿Limitamos las capacidades del modelo a lo que el caso de uso necesita y validamos sus salidas antes de que desencadenen acciones? — vínculo `AMP-36`.
- `PC-260` (interrogativa): ¿Cada agente tiene una lista cerrada de herramientas, identidad y control de acceso en cada invocación, intervención humana en acciones de alto impacto y trazabilidad completa? — vínculo `AMP-36`.

**Ejemplos generados con plantillas mayéuticas documentadas:**
- `BM-1021` [Esencial]: ¿Qué problema de gobierno, riesgo o capacidad intenta resolver realmente «Límites de herramientas y permisos», y qué decisión debería mejorar si se comprende correctamente?
- `BM-1022` [Tensión]: ¿Qué supuesto habitual sobre «Límites de herramientas y permisos» podría ser falso o incompleto, y qué consecuencia tendría diseñar la seguridad como si fuera cierto?
- `BM-1023` [Decisión]: ¿Qué alternativa concreta elegiríamos a partir de «Límites de herramientas y permisos», quién debería decidirla y qué señal obligaría a revisarla?

Las preguntas de banco son construcciones mediante plantilla; no se presentan como citas de entrevistas. Fuente original: [preguntas consolidadas](../../../Curado02/02_metodo_mayeutico/src-preguntas-consolidadas__37298ee439f0.json).

## Procedencia y límites

[Matriz de 331 pre-ensayos](../../../Curado02/01_noviembre_2026/src-ai-ciso-atlas-ensayos-thenextciso-x-core-accountabilities-fy27-2026-11-05__5528a05eb5dd.xlsx), `06Ensayos!A320:T320` (idea `[P]`: `06Ensayos!I320`); [registro de consulta y estado [P]](../../00_control/AMP_ideas_propuestas_2026-11.json).

El nombre del marco, su aparición en el corpus y una alineación temática no acreditan dominio profesional, cumplimiento ni aprobación formal. Las referencias bibliográficas individuales solo se atribuyen si la fuente las identifica; véase el documento maestro para bibliografía general de NIST e ISACA y para la condición propuesta de sus mapeos.

[Documento Maestro](../../../Curado02/01_noviembre_2026/src-thenextciso-gm-24-documento-maestro__9b8c53df319d.md), sección `M3.1` (línea 720).

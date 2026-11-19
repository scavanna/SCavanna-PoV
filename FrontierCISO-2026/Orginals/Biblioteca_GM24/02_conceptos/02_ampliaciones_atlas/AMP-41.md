<!-- generado-gm24 sha256:4fd444356f3a1d155a19de05d94e8258805d2f25e52cb09d6da2c51e5a9bb8a1 -->
# AMP-41 — Prompt injection

**Clase:** Ampliación Atlas propuesta · **Estado:** ampliación Atlas: título original; tesis propuesta [P], no aprobada · **Unidades:** M4.2.

## Enunciado y fuerza de la evidencia

La inyección de instrucciones convierte contenido en órdenes; la defensa combina aislamiento de datos, límites de herramientas, filtros y detección en ejecución.

**Importante:** en el Documento Maestro se documentó el **título** de `AMP-41`; la oración precedente es una **tesis propuesta [P]** en la matriz posterior, no una definición aprobada del programa.

## Desarrollo para el aprendizaje (derivación editorial)

Esta ampliación examina «Prompt injection» en la unidad `M4.2` (Gestión de Amenazas, Vulnerabilidades y Riesgos Emergentes). Su pregunta de diseño es qué cambiaría en la decisión de modelar amenaza de prompt injection y envenenamiento, priorizar defensas y señales de detección al tomar en serio la tesis [P]. El vínculo `M6.2-K04` —Seguridad IA— aporta una lente vecina: «La seguridad de IA protege modelos, datos, herramientas, agentes y procesos ante amenazas específicas y consecuencias de autonomía». La relación no implica identidad de conceptos, aprobación del nuevo tema ni eficacia demostrada de una intervención.

En la organización ficticia del programa: Un documento de incidente en la base RAG contiene instrucciones falsas para un agente y referencias manipuladas de indicadores. Una solución defendible debe contrastar estas alternativas: Confiar en filtrado de texto frente a limitar herramientas, procedencia de datos y validación de acciones; las observaciones iniciales serían datos RAG, threat model, trazas de invocación y catálogo de vulnerabilidades. El estudiante separa lo observado, lo inferido y lo aún no verificable antes de sugerir cambios de arquitectura, gobierno u operación.

El producto de aprendizaje propuesto es «modelo de amenazas actualizado con pruebas adversariales y riesgo residual». Debe poder explicar por qué su recomendación es revisable y cómo verificaría que «Contenido recuperado no se convierte en instrucción autorizada por su formato o su supuesta fuente». La propuesta permanece abierta a revisión curricular y técnica.

## Ejercicio y criterio de evaluación

**Práctica:** Ante «Un documento de incidente en la base RAG contiene instrucciones falsas para un agente y referencias manipuladas de indicadores», explica qué aporta «Prompt injection» frente a las opciones «Confiar en filtrado de texto frente a limitar herramientas, procedencia de datos y validación de acciones». Usa datos RAG, threat model, trazas de invocación y catálogo de vulnerabilidades y entrega modelo de amenazas actualizado con pruebas adversariales y riesgo residual. Distingue tesis [P] de evidencia obtenida y de supuestos de diseño.

**Validación:** Se acepta para revisión si identifica autoridad y límites, documenta fuentes y supuestos, compara al menos dos decisiones y demuestra «Contenido recuperado no se convierte en instrucción autorizada por su formato o su supuesta fuente». La rúbrica de la unidad es una propuesta docente, no un estándar aprobado.

La guía de unidad desarrolla el escenario longitudinal, las ocho modalidades de ejercicio y la rúbrica: [abrir unidad](../../01_unidades/M4.2/Unidad_M4.2.md).

## Preguntas del método y comprobación

**Preguntas originales consolidadas (si hay vínculo directo o de corpus):**
- `PC-146` (interrogativa): ¿Cómo nos protegemos de la inyección indirecta de instrucciones desde correos, documentos, páginas web o respuestas de herramientas? — vínculo `AMP-41`.
- `PC-208` (interrogativa): ¿Qué fuentes externas leen nuestros asistentes y agentes (correos, documentos, sitios web) y qué controles bloquean las instrucciones ocultas en ellas? — vínculo `AMP-41`.
- `PC-232` (interrogativa): ¿Qué contenido no confiable ingieren nuestros agentes, qué herramientas pueden invocar con ese contenido y qué privilegios tendría un atacante que los manipule? — vínculo `AMP-41`.

**Ejemplos generados con plantillas mayéuticas documentadas:**
- `BM-1041` [Esencial]: ¿Qué problema de gobierno, riesgo o capacidad intenta resolver realmente «Prompt injection», y qué decisión debería mejorar si se comprende correctamente?
- `BM-1042` [Tensión]: ¿Qué supuesto habitual sobre «Prompt injection» podría ser falso o incompleto, y qué consecuencia tendría diseñar la seguridad como si fuera cierto?
- `BM-1043` [Decisión]: ¿Qué alternativa concreta elegiríamos a partir de «Prompt injection», quién debería decidirla y qué señal obligaría a revisarla?

Las preguntas de banco son construcciones mediante plantilla; no se presentan como citas de entrevistas. Fuente original: [preguntas consolidadas](../../../Curado02/02_metodo_mayeutico/src-preguntas-consolidadas__37298ee439f0.json).

## Procedencia y límites

[Matriz de 331 pre-ensayos](../../../Curado02/01_noviembre_2026/src-ai-ciso-atlas-ensayos-thenextciso-x-core-accountabilities-fy27-2026-11-05__5528a05eb5dd.xlsx), `06Ensayos!A325:T325` (idea `[P]`: `06Ensayos!I325`); [registro de consulta y estado [P]](../../00_control/AMP_ideas_propuestas_2026-11.json).

El nombre del marco, su aparición en el corpus y una alineación temática no acreditan dominio profesional, cumplimiento ni aprobación formal. Las referencias bibliográficas individuales solo se atribuyen si la fuente las identifica; véase el documento maestro para bibliografía general de NIST e ISACA y para la condición propuesta de sus mapeos.

[Documento Maestro](../../../Curado02/01_noviembre_2026/src-thenextciso-gm-24-documento-maestro__9b8c53df319d.md), sección `M4.2` (línea 843).

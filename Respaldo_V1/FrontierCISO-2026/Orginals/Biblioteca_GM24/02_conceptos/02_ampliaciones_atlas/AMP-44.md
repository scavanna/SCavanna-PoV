<!-- generado-gm24 sha256:b8ad2f23a456f8cc53787b9466e68fc4f25ad9e17a5b203e8c2a9cc7e6650ed0 -->
# AMP-44 — Kill switch y escalamiento

**Clase:** Ampliación Atlas propuesta · **Estado:** ampliación Atlas: título original; tesis propuesta [P], no aprobada · **Unidades:** M5.1.

## Enunciado y fuerza de la evidencia

Todo agente con capacidad de acción necesita un mecanismo probado para detenerlo y una ruta de escalamiento con autoridad clara.

**Importante:** en el Documento Maestro se documentó el **título** de `AMP-44`; la oración precedente es una **tesis propuesta [P]** en la matriz posterior, no una definición aprobada del programa.

## Desarrollo para el aprendizaje (derivación editorial)

Esta ampliación examina «Kill switch y escalamiento» en la unidad `M5.1` (Planificación y Preparación (Incl. BIA)). Su pregunta de diseño es qué cambiaría en la decisión de diseñar mando de incidentes, rto/rpo, reglas de kill switch y escalamiento al tomar en serio la tesis [P]. El vínculo `HC-010` —Autonomía delegada y límites de acción— aporta una lente vecina: «Distingue capacidad técnica, permiso, delegación y ejecución de agentes de IA». La relación no implica identidad de conceptos, aprobación del nuevo tema ni eficacia demostrada de una intervención.

En la organización ficticia del programa: En un tabletop de ransomware, un agente comprometido intenta aislar servidores de respaldo durante una restauración crítica. Una solución defendible debe contrastar estas alternativas: Mantener al agente para conservar velocidad frente a suspender su autonomía y operar en modo degradado; las observaciones iniciales serían BIA, plan IRP, inventario de permisos, datos de prueba y criterios de severidad. El estudiante separa lo observado, lo inferido y lo aún no verificable antes de sugerir cambios de arquitectura, gobierno u operación.

El producto de aprendizaje propuesto es «guion de tabletop con injects, decisiones por minuto y matriz de autoridad». Debe poder explicar por qué su recomendación es revisable y cómo verificaría que «El mecanismo de detención se demuestra en ejercicio y preserva registros para investigación». La propuesta permanece abierta a revisión curricular y técnica.

## Ejercicio y criterio de evaluación

**Práctica:** Ante «En un tabletop de ransomware, un agente comprometido intenta aislar servidores de respaldo durante una restauración crítica», explica qué aporta «Kill switch y escalamiento» frente a las opciones «Mantener al agente para conservar velocidad frente a suspender su autonomía y operar en modo degradado». Usa BIA, plan IRP, inventario de permisos, datos de prueba y criterios de severidad y entrega guion de tabletop con injects, decisiones por minuto y matriz de autoridad. Distingue tesis [P] de evidencia obtenida y de supuestos de diseño.

**Validación:** Se acepta para revisión si identifica autoridad y límites, documenta fuentes y supuestos, compara al menos dos decisiones y demuestra «El mecanismo de detención se demuestra en ejercicio y preserva registros para investigación». La rúbrica de la unidad es una propuesta docente, no un estándar aprobado.

La guía de unidad desarrolla el escenario longitudinal, las ocho modalidades de ejercicio y la rúbrica: [abrir unidad](../../01_unidades/M5.1/Unidad_M5.1.md).

## Preguntas del método y comprobación

**Preguntas originales consolidadas (si hay vínculo directo o de corpus):**
- `PC-158` (interrogativa): ¿Podemos suspender, aislar o revocar un agente, o todos los de una clase, en minutos, y lo hemos ensayado? — vínculo `AMP-44`.
- `PC-159` (interrogativa): ¿Qué límites operativos (presupuesto, cantidad de llamadas, montos, frecuencia, alcance) actúan como cortacircuitos ante comportamientos anómalos o en cascada? — vínculo `AMP-44`.
- `PC-161` (interrogativa): ¿Cuál es nuestro presupuesto de tiempo de contención para un agente comprometido, y es menor que el tiempo en que el daño se vuelve material? — vínculo `AMP-44`.

**Ejemplos generados con plantillas mayéuticas documentadas:**
- `BM-1053` [Esencial]: ¿Qué problema de gobierno, riesgo o capacidad intenta resolver realmente «Kill switch y escalamiento», y qué decisión debería mejorar si se comprende correctamente?
- `BM-1054` [Tensión]: ¿Qué supuesto habitual sobre «Kill switch y escalamiento» podría ser falso o incompleto, y qué consecuencia tendría diseñar la seguridad como si fuera cierto?
- `BM-1055` [Decisión]: ¿Qué alternativa concreta elegiríamos a partir de «Kill switch y escalamiento», quién debería decidirla y qué señal obligaría a revisarla?

Las preguntas de banco son construcciones mediante plantilla; no se presentan como citas de entrevistas. Fuente original: [preguntas consolidadas](../../../Curado02/02_metodo_mayeutico/src-preguntas-consolidadas__37298ee439f0.json).

## Procedencia y límites

[Matriz de 331 pre-ensayos](../../../Curado02/01_noviembre_2026/src-ai-ciso-atlas-ensayos-thenextciso-x-core-accountabilities-fy27-2026-11-05__5528a05eb5dd.xlsx), `06Ensayos!A328:T328` (idea `[P]`: `06Ensayos!I328`); [registro de consulta y estado [P]](../../00_control/AMP_ideas_propuestas_2026-11.json).

El nombre del marco, su aparición en el corpus y una alineación temática no acreditan dominio profesional, cumplimiento ni aprobación formal. Las referencias bibliográficas individuales solo se atribuyen si la fuente las identifica; véase el documento maestro para bibliografía general de NIST e ISACA y para la condición propuesta de sus mapeos.

[Documento Maestro](../../../Curado02/01_noviembre_2026/src-thenextciso-gm-24-documento-maestro__9b8c53df319d.md), sección `M5.1` (línea 884).

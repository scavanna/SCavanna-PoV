<!-- generado-gm24 sha256:86ce3b67940262efcf483f4cd8c77c7e533bee06480239ea1262becb2953e6bd -->
# APN-01 — Medición agregada del uso de asistentes de IA por área

**Tipo:** tesis ampliada por pregunta · **Estado:** propuesta editorial del corpus mayéutico, no concepto original GM-24 · **Ubicación:** `M1.2` (especialización explícita).

## Pregunta original (sin sustituirla)

`PN-01` · interrogativa: ¿Qué parte del trabajo diario de cada área ya pasa por asistentes de IA, con qué herramientas y con qué tipo de información, y cómo lo medimos sin vigilar a las personas?

La formulación anterior es contenido de la fuente. La tesis siguiente no es una cita literal de esa pregunta: es el **enunciado declarativo ya registrado como propuesta** en el corpus de pre-ensayos.

## Tesis propuesta

El CISO debe acordar con el CIO y los líderes de área una medición agregada del uso de asistentes de IA, por área, herramienta y clase de información, basada en telemetría de plataforma y no en el seguimiento de personas, porque sin ese mapa no se pueden priorizar controles de datos ni decidir qué herramientas aprobar.

## Tensión, prueba y limitación

**Tensión documentada:** cuanto más detallada es la medición del uso, más útil resulta para proteger datos, pero más se parece a la vigilancia del desempeño y más incentiva a las personas a usar herramientas fuera de la vista corporativa

**Desarrollo/investigación propuesto:** diseñar con un área piloto un tablero que muestre tareas asistidas, herramientas y clases de información solo con umbrales mínimos de agregación, y validar con representantes del personal qué cruces de datos quedan prohibidos

**Error a evitar:** medir la adopción por licencias asignadas o encuestas de percepción, que no revelan qué información fluye hacia los asistentes, o en el extremo opuesto, revisar las conversaciones individuales

**Producto observable:** un mapa de uso de asistentes por área, herramienta y clase de información, un protocolo de medición acordado con representantes del personal y un tablero agregado con umbrales de anonimato

## Relaciones candidatas

- `AMP-30` — `ESPECIALIZA`: mide la adopción real de asistentes por área sin vigilar personas
- `M2.1-K02` — `REQUIERE`: necesita clases de información comunes para saber qué datos fluyen
- `M6.2-K06` — `PRIORIZA`: orienta la respuesta al uso no autorizado según área e información expuesta
- `G3.1-K06` — `SE_SUPERVISA_CON`: la protección de datos del personal fija los límites de la medición

**Especializa:** `AMP-30`.

## Ejercicio de método

Conserva la pregunta inicial. En un caso real, identifica qué datos la harían relevante, prueba la tesis contra al menos una interpretación alternativa y explica cuál sería la decisión revisable. Entrega un mapa de uso de asistentes por área, herramienta y clase de información, un protocolo de medición acordado con representantes del personal y un tablero agregado con umbrales de anonimato. Se considera logrado solo si la evidencia documenta la tesis sin transformar la pregunta original en hecho establecido.

## Procedencia

[corpus de pre-ensayos mayéuticos](../../../Curado02/02_metodo_mayeutico/src-corpus-preensayos__4e216917f657.json), `preensayos[id=APN-01]`.

Pregunta original: [src-preguntas-consolidadas__37298ee439f0.json](../../../Curado02/02_metodo_mayeutico/src-preguntas-consolidadas__37298ee439f0.json), `preguntas[id=PN-01]`. Toda relación marcada en la fuente sigue siendo candidata para revisión por expertos, no una arista aprobada de la ontología.

<!-- generado-gm24 sha256:40425d958ab71558d7b6b55760079e1ff3d07d9d5bbfa2e53e73e93395bba6f0 -->
# APN-07 — Indicadores de decisión sobre el despliegue de asistentes por área

**Tipo:** tesis ampliada por pregunta · **Estado:** propuesta editorial del corpus mayéutico, no concepto original GM-24 · **Ubicación:** Vínculo transversal; sin asignación exclusiva a unidad.

## Pregunta original (sin sustituirla)

`PN-07` · interrogativa: ¿Con qué indicadores (adopción, incidentes de datos, sobreexposición corregida, satisfacción, costo por licencia usada) decidimos ampliar, mantener o restringir los asistentes en cada área, y quién toma esa decisión?

La formulación anterior es contenido de la fuente. La tesis siguiente no es una cita literal de esa pregunta: es el **enunciado declarativo ya registrado como propuesta** en el corpus de pre-ensayos.

## Tesis propuesta

El CISO debe proponer al consejo de IA y al CFO un tablero por área que combine uso efectivo, eventos de fuga de datos, permisos excesivos remediados, percepción de los usuarios y costo por licencia activa, con umbrales acordados para extender, sostener o limitar los asistentes y un responsable designado que decida con esa evidencia, para que el riesgo pese junto al valor.

## Tensión, prueba y limitación

**Tensión documentada:** los indicadores de adopción y satisfacción mejoran cuanto más se amplía el acceso, mientras que los de exposición de datos empeoran con la misma ampliación, y quien decide suele ver solo una de las dos series

**Desarrollo/investigación propuesto:** comparar dos áreas con igual costo de licencias, una con uso alto y sobreexposición sin corregir y otra con uso bajo y datos ordenados, y decidir con el tablero cuál ampliar, cuál restringir y bajo qué condiciones

**Error a evitar:** decidir la expansión de asistentes solo por adopción o por costo, sin incorporar indicadores de exposición de datos, o medirlo todo sin designar quién decide y con qué umbral

**Producto observable:** un tablero por área con indicadores de valor, riesgo y costo, una tabla de umbrales con la acción asociada a cada uno y actas del consejo de IA con las decisiones

## Relaciones candidatas

- `HC-006` — `ESPECIALIZA`: aplica la medición causal a decisiones de despliegue de asistentes
- `HC-027` — `REQUIERE`: evita indicadores de adopción que oculten la exposición de datos
- `AMP-31` — `RECIBE_EVIDENCIA_DE`: la sobreexposición corregida proviene de la gestión de postura de datos
- `G6.2-K05` — `SE_COMUNICA_MEDIANTE`: el tablero se integra en las métricas de gobierno que revisa el consejo

**Especializa:** `HC-006`.

## Ejercicio de método

Conserva la pregunta inicial. En un caso real, identifica qué datos la harían relevante, prueba la tesis contra al menos una interpretación alternativa y explica cuál sería la decisión revisable. Entrega un tablero por área con indicadores de valor, riesgo y costo, una tabla de umbrales con la acción asociada a cada uno y actas del consejo de IA con las decisiones. Se considera logrado solo si la evidencia documenta la tesis sin transformar la pregunta original en hecho establecido.

## Procedencia

[corpus de pre-ensayos mayéuticos](../../../Curado02/02_metodo_mayeutico/src-corpus-preensayos__4e216917f657.json), `preensayos[id=APN-07]`.

Pregunta original: [src-preguntas-consolidadas__37298ee439f0.json](../../../Curado02/02_metodo_mayeutico/src-preguntas-consolidadas__37298ee439f0.json), `preguntas[id=PN-07]`. Toda relación marcada en la fuente sigue siendo candidata para revisión por expertos, no una arista aprobada de la ontología.

<!-- generado-gm24 sha256:5851925a2898877d353685aff55eebb047e584afee59f9617799164bb29dec5b -->
# APN-48 — Informe al directorio de fugas por IA y cambios aplicados

**Tipo:** tesis ampliada por pregunta · **Estado:** propuesta editorial del corpus mayéutico, no concepto original GM-24 · **Ubicación:** `M2.1` (especialización explícita).

## Pregunta original (sin sustituirla)

`PN-48` · interrogativa: «¿Tuvimos fugas de datos por el uso de IA en el último año, y qué cambiamos?»

La formulación anterior es contenido de la fuente. La tesis siguiente no es una cita literal de esa pregunta: es el **enunciado declarativo ya registrado como propuesta** en el corpus de pre-ensayos.

## Tesis propuesta

El directorio necesita saber qué incidentes de datos vinculados al uso de IA se detectaron, cómo se clasificaron, qué se notificó y qué controles cambiaron como consecuencia. El CISO responde con un informe que distingue incidentes confirmados, eventos sin pérdida y zonas sin capacidad de detección, porque no haber registrado fugas no prueba que no hayan ocurrido.

## Tensión, prueba y limitación

**Tensión documentada:** reportar pocas fugas puede reflejar buenos controles o simple falta de detección, y el directorio tiende a leer la ausencia de incidentes como éxito sin preguntar por la capacidad de verlos

**Desarrollo/investigación propuesto:** revisar los incidentes de datos del último año, reclasificar los que involucraron herramientas de IA y verificar para cada uno qué cambio de control se aprobó y si está implementado y probado

**Error a evitar:** presentar el número de incidentes como indicador de seguridad sin informar la cobertura de detección sobre el uso de IA ni el estado de los cambios comprometidos

**Producto observable:** un informe anual de incidentes de datos vinculados a IA con su clasificación, un registro de cambios de control con estado de implementación y un indicador de cobertura de detección

## Relaciones candidatas

- `M2.1-K10` — `ESPECIALIZA`: acota los riesgos de datos a las fugas vinculadas al uso de IA
- `HC-035` — `VERIFICA`: comprueba que cada incidente haya producido un cambio de control implementado
- `G6.1-K05` — `SE_COMUNICA_MEDIANTE`: el informe al directorio se apoya en hechos verificables y no en percepciones
- `HC-027` — `REQUIERE`: evita leer la ausencia de incidentes registrados como prueba de control

**Especializa:** `M2.1-K10`.

## Ejercicio de método

Conserva la pregunta inicial. En un caso real, identifica qué datos la harían relevante, prueba la tesis contra al menos una interpretación alternativa y explica cuál sería la decisión revisable. Entrega un informe anual de incidentes de datos vinculados a IA con su clasificación, un registro de cambios de control con estado de implementación y un indicador de cobertura de detección. Se considera logrado solo si la evidencia documenta la tesis sin transformar la pregunta original en hecho establecido.

## Procedencia

[corpus de pre-ensayos mayéuticos](../../../Curado02/02_metodo_mayeutico/src-corpus-preensayos__4e216917f657.json), `preensayos[id=APN-48]`.

Pregunta original: [src-preguntas-consolidadas__37298ee439f0.json](../../../Curado02/02_metodo_mayeutico/src-preguntas-consolidadas__37298ee439f0.json), `preguntas[id=PN-48]`. Toda relación marcada en la fuente sigue siendo candidata para revisión por expertos, no una arista aprobada de la ontología.

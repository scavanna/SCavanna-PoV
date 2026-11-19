<!-- generado-gm24 sha256:2ec69ffe1cbea1eb38bd50a4525896bc48eb4624de7d4f81942b156d117b9795 -->
# APN-24 — Gobierno de la captura e indexación de pantalla con IA

**Tipo:** tesis ampliada por pregunta · **Estado:** propuesta editorial del corpus mayéutico, no concepto original GM-24 · **Ubicación:** `M6.2` (especialización explícita).

## Pregunta original (sin sustituirla)

`PN-24` · interrogativa: ¿Las funciones de IA que capturan o indexan la pantalla y la actividad local del equipo están desactivadas o gobernadas en los dispositivos corporativos, y cómo protegemos ese índice si el equipo se ve comprometido?

La formulación anterior es contenido de la fuente. La tesis siguiente no es una cita literal de esa pregunta: es el **enunciado declarativo ya registrado como propuesta** en el corpus de pre-ensayos.

## Tesis propuesta

Capturar e indexar con IA la pantalla y la actividad del equipo crea un registro concentrado de todo lo que la persona vio, incluso de datos nunca guardados. En equipos corporativos estas funciones deben quedar desactivadas por defecto y habilitarse solo con justificación, cifrado ligado al usuario, exclusión de aplicaciones sensibles y un plan de respuesta que incluya ese índice.

## Tensión, prueba y limitación

**Tensión documentada:** el índice local promete recuperar cualquier cosa vista en el equipo, pero esa misma capacidad entrega a quien compromete el dispositivo un historial ordenado de información que los controles de datos nunca llegaron a clasificar

**Desarrollo/investigación propuesto:** simular el compromiso de un equipo con la indexación activa y comprobar qué puede extraer el atacante del índice, qué cifrado lo impide y si el plan de respuesta incluye ese índice en su alcance

**Error a evitar:** suponer que una función incluida en el sistema operativo ya viene gobernada por el proveedor, o que desactivarla en la imagen base impide que una actualización la vuelva a habilitar

**Producto observable:** una decisión documentada de activación por perfil de usuario, la configuración de cifrado y exclusiones del índice y un procedimiento de respuesta que trata el índice local como dato expuesto

## Relaciones candidatas

- `M6.2-K04` — `ESPECIALIZA`: concreta la seguridad de IA en funciones que indexan la actividad local
- `M3.1-K04` — `OPERACIONALIZA`: aplica la seguridad por defecto a funciones de IA del sistema operativo
- `M2.1-K05` — `REQUIERE`: el índice debe cifrarse en reposo con claves ligadas al usuario
- `M5.2-K06` — `CONDICIONA`: el índice local amplía el alcance del análisis forense de un equipo comprometido

**Especializa:** `M6.2-K04`.

## Ejercicio de método

Conserva la pregunta inicial. En un caso real, identifica qué datos la harían relevante, prueba la tesis contra al menos una interpretación alternativa y explica cuál sería la decisión revisable. Entrega una decisión documentada de activación por perfil de usuario, la configuración de cifrado y exclusiones del índice y un procedimiento de respuesta que trata el índice local como dato expuesto. Se considera logrado solo si la evidencia documenta la tesis sin transformar la pregunta original en hecho establecido.

## Procedencia

[corpus de pre-ensayos mayéuticos](../../../Curado02/02_metodo_mayeutico/src-corpus-preensayos__4e216917f657.json), `preensayos[id=APN-24]`.

Pregunta original: [src-preguntas-consolidadas__37298ee439f0.json](../../../Curado02/02_metodo_mayeutico/src-preguntas-consolidadas__37298ee439f0.json), `preguntas[id=PN-24]`. Toda relación marcada en la fuente sigue siendo candidata para revisión por expertos, no una arista aprobada de la ontología.

<!-- generado-gm24 sha256:c9f92fc06ecd8dffae01d60fc5c5c796885931e04d2a9d8d407343d927e4bb0b -->
# APN-20 — Detección y contención de cuentas robadas con asistente de IA

**Tipo:** tesis ampliada por pregunta · **Estado:** propuesta editorial del corpus mayéutico, no concepto original GM-24 · **Ubicación:** `M4.1` (especialización explícita).

## Pregunta original (sin sustituirla)

`PN-20` · interrogativa: ¿Cómo detectamos y contenemos el robo de una cuenta cuando el atacante puede usar el asistente de esa persona para buscar y resumir en minutos todo lo que ella puede ver?

La formulación anterior es contenido de la fuente. La tesis siguiente no es una cita literal de esa pregunta: es el **enunciado declarativo ya registrado como propuesta** en el corpus de pre-ensayos.

## Tesis propuesta

Cuando una cuenta robada tiene asistente de IA, el atacante comprime en minutos un reconocimiento que antes le exigía mucho más tiempo, por lo que la detección debe vigilar patrones de consulta y no solo inicios de sesión. La contención debe revocar sesiones y tokens del asistente en el mismo acto que los de la cuenta, con tiempos medidos.

## Tensión, prueba y limitación

**Tensión documentada:** las búsquedas amplias y los resúmenes masivos son también el uso legítimo que se promueve, y una detección sensible a ese patrón genera alertas sobre las personas más productivas antes que sobre los atacantes

**Desarrollo/investigación propuesto:** simular con el equipo rojo el robo de sesión de un usuario con asistente, ejecutar consultas de reconocimiento sobre temas sensibles y medir cuánto tardan la alerta, la revocación de tokens y el cierre de sesiones

**Error a evitar:** suponer que cambiar la contraseña contiene el incidente, cuando las sesiones y tokens del asistente pueden seguir activos y lo ya resumido quedó fuera del alcance de cualquier revocación

**Producto observable:** una regla de detección probada para consultas anómalas al asistente, un playbook de contención que incluye sesiones y tokens del asistente y el registro de tiempos del ejercicio

## Relaciones candidatas

- `M4.1-K06` — `ESPECIALIZA`: lleva la detección extendida al abuso del asistente tras el robo de una cuenta
- `M5.2-K01` — `OPERACIONALIZA`: define la contención de sesiones y tokens del asistente comprometido
- `M4.1-K07` — `SE_ALIMENTA_DE`: la búsqueda proactiva aporta hipótesis sobre consultas de reconocimiento con el asistente
- `AMP-45` — `REQUIERE`: necesita reconstruir qué consultó y resumió el atacante con el asistente

**Especializa:** `M4.1-K06`.

## Ejercicio de método

Conserva la pregunta inicial. En un caso real, identifica qué datos la harían relevante, prueba la tesis contra al menos una interpretación alternativa y explica cuál sería la decisión revisable. Entrega una regla de detección probada para consultas anómalas al asistente, un playbook de contención que incluye sesiones y tokens del asistente y el registro de tiempos del ejercicio. Se considera logrado solo si la evidencia documenta la tesis sin transformar la pregunta original en hecho establecido.

## Procedencia

[corpus de pre-ensayos mayéuticos](../../../Curado02/02_metodo_mayeutico/src-corpus-preensayos__4e216917f657.json), `preensayos[id=APN-20]`.

Pregunta original: [src-preguntas-consolidadas__37298ee439f0.json](../../../Curado02/02_metodo_mayeutico/src-preguntas-consolidadas__37298ee439f0.json), `preguntas[id=PN-20]`. Toda relación marcada en la fuente sigue siendo candidata para revisión por expertos, no una arista aprobada de la ontología.

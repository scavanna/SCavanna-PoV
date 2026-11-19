<!-- generado-gm24 sha256:d924b58f7e409e61e80c9d2adb90fa5f6a53d084a8fd071a2ecafb272c2a0653 -->
# APN-29 — Modelo de amenazas del asistente como vector de entrada

**Tipo:** tesis ampliada por pregunta · **Estado:** propuesta editorial del corpus mayéutico, no concepto original GM-24 · **Ubicación:** `M4.2` (especialización explícita).

## Pregunta original (sin sustituirla)

`PN-29` · interrogativa: «¿El asistente de IA puede convertirse en la puerta de entrada de un ataque?»

La formulación anterior es contenido de la fuente. La tesis siguiente no es una cita literal de esa pregunta: es el **enunciado declarativo ya registrado como propuesta** en el corpus de pre-ensayos.

## Tesis propuesta

Sí: el asistente puede ser la puerta de entrada porque lee contenido externo, actúa con los permisos de la persona y se conecta con otras herramientas. El CISO responde al CEO con un modelo de amenazas que muestra las vías de entrada plausibles, qué controles las cortan, cuáles siguen abiertas y qué consecuencia tendría cada una.

## Tensión, prueba y limitación

**Tensión documentada:** el asistente vale más cuanto más contenido lee y más herramientas conecta, y cada fuente o conector adicional amplía la superficie por la que un atacante puede introducir instrucciones

**Desarrollo/investigación propuesto:** construir con el comité ejecutivo tres cadenas de ataque plausibles, desde un correo con instrucciones ocultas hasta un conector comprometido, y marcar en cada eslabón qué control existe y quién lo opera

**Error a evitar:** responder con un sí o un no tranquilizador, en lugar de mostrar qué vías de entrada existen, cuáles están controladas y qué riesgo residual se está aceptando

**Producto observable:** un modelo de amenazas del asistente con vías de entrada y controles, un mapa de riesgo residual con dueño y un resumen ejecutivo de consecuencias por escenario

## Relaciones candidatas

- `M4.2-K07` — `ESPECIALIZA`: concreta los riesgos emergentes en el asistente como vía de entrada
- `M4.2-K02` — `OPERACIONALIZA`: aplica el modelado de amenazas a fuentes, permisos y conectores del asistente
- `AMP-41` — `SE_ALIMENTA_DE`: la inyección de instrucciones es la vía de entrada más característica del asistente
- `G4.1-K10` — `SE_COMUNICA_MEDIANTE`: el riesgo residual se reporta a la dirección con dueño y consecuencia

**Especializa:** `M4.2-K07`.

## Ejercicio de método

Conserva la pregunta inicial. En un caso real, identifica qué datos la harían relevante, prueba la tesis contra al menos una interpretación alternativa y explica cuál sería la decisión revisable. Entrega un modelo de amenazas del asistente con vías de entrada y controles, un mapa de riesgo residual con dueño y un resumen ejecutivo de consecuencias por escenario. Se considera logrado solo si la evidencia documenta la tesis sin transformar la pregunta original en hecho establecido.

## Procedencia

[corpus de pre-ensayos mayéuticos](../../../Curado02/02_metodo_mayeutico/src-corpus-preensayos__4e216917f657.json), `preensayos[id=APN-29]`.

Pregunta original: [src-preguntas-consolidadas__37298ee439f0.json](../../../Curado02/02_metodo_mayeutico/src-preguntas-consolidadas__37298ee439f0.json), `preguntas[id=PN-29]`. Toda relación marcada en la fuente sigue siendo candidata para revisión por expertos, no una arista aprobada de la ontología.

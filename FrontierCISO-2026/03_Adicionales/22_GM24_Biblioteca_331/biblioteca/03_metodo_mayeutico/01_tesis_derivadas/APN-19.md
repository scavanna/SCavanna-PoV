<!-- generado-gm24 sha256:00dc6aa7cd622e9d1fe2d3838ebcceff84a8363eaec92867a4530613b9ca393f -->
# APN-19 — Gobierno de extensiones y complementos de IA del navegador

**Tipo:** tesis ampliada por pregunta · **Estado:** propuesta editorial del corpus mayéutico, no concepto original GM-24 · **Ubicación:** `M6.2` (especialización explícita).

## Pregunta original (sin sustituirla)

`PN-19` · interrogativa: ¿Qué extensiones de navegador y complementos con IA usan las personas, qué permisos tienen (leer todas las páginas, el portapapeles, el correo) y cómo los aprobamos, bloqueamos y revisamos?

La formulación anterior es contenido de la fuente. La tesis siguiente no es una cita literal de esa pregunta: es el **enunciado declarativo ya registrado como propuesta** en el corpus de pre-ensayos.

## Tesis propuesta

Las extensiones y complementos con IA deben gobernarse como software con acceso privilegiado a la información, porque pueden leer cada página visitada, el portapapeles y el correo. Corresponde mantener un inventario por permisos, una lista de permitidas basada en el destino de los datos y una revisión periódica que detecte cambios de propietario, permisos o comportamiento.

## Tensión, prueba y limitación

**Tensión documentada:** una lista estricta de extensiones permitidas reduce la exposición, pero las extensiones cambian de dueño y de permisos con actualizaciones automáticas, y la aprobación inicial pierde validez sin que nadie lo note

**Desarrollo/investigación propuesto:** reconstruir el caso de una extensión aprobada que, tras una actualización, empieza a enviar el contenido de cada página a un servidor externo, y medir cuánto tardaría la organización en detectarla y retirarla

**Error a evitar:** evaluar las extensiones por su utilidad declarada y no por los permisos que solicitan, el destino de los datos que leen y quién controla sus actualizaciones

**Producto observable:** un inventario de extensiones instaladas con permisos y destino de datos, una lista de permitidas con criterios de revisión y una alerta probada ante cambios de permisos

## Relaciones candidatas

- `AMP-50` — `ESPECIALIZA`: concentra la seguridad de conectores en extensiones y complementos del navegador
- `M3.1-K09` — `REQUIERE`: limita los permisos de lectura de páginas, portapapeles y correo al mínimo necesario
- `M2.1-K03` — `SE_ALIMENTA_DE`: parte del inventario de software instalado en los puestos de trabajo
- `M6.2-K01` — `GESTIONA`: aborda el riesgo de cadena de suministro que traen las actualizaciones automáticas

**Especializa:** `AMP-50`.

## Ejercicio de método

Conserva la pregunta inicial. En un caso real, identifica qué datos la harían relevante, prueba la tesis contra al menos una interpretación alternativa y explica cuál sería la decisión revisable. Entrega un inventario de extensiones instaladas con permisos y destino de datos, una lista de permitidas con criterios de revisión y una alerta probada ante cambios de permisos. Se considera logrado solo si la evidencia documenta la tesis sin transformar la pregunta original en hecho establecido.

## Procedencia

[corpus de pre-ensayos mayéuticos](../../../Curado02/02_metodo_mayeutico/src-corpus-preensayos__4e216917f657.json), `preensayos[id=APN-19]`.

Pregunta original: [src-preguntas-consolidadas__37298ee439f0.json](../../../Curado02/02_metodo_mayeutico/src-preguntas-consolidadas__37298ee439f0.json), `preguntas[id=PN-19]`. Toda relación marcada en la fuente sigue siendo candidata para revisión por expertos, no una arista aprobada de la ontología.

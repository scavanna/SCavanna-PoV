<!-- generado-gm24 sha256:c09b26361bf54e521d8bb9fcff56c0dc1c15e13d76635e9a3dff4ce8998e4c41 -->
# APN-27 — Procedimiento ante sobreexposición de datos revelada por el asistente

**Tipo:** tesis ampliada por pregunta · **Estado:** propuesta editorial del corpus mayéutico, no concepto original GM-24 · **Ubicación:** Vínculo transversal; sin asignación exclusiva a unidad.

## Pregunta original (sin sustituirla)

`PN-27` · interrogativa: «Una persona reporta que el asistente le mostró información que no debería ver. ¿Qué hacemos?»

La formulación anterior es contenido de la fuente. La tesis siguiente no es una cita literal de esa pregunta: es el **enunciado declarativo ya registrado como propuesta** en el corpus de pre-ensayos.

## Tesis propuesta

El CISO debe dar a la mesa de ayuda un procedimiento que trate el reporte como incidente de datos: registrar la evidencia, escalar a seguridad y al dueño de la información, corregir el permiso de origen y revisar quién más accedió. El asistente no creó la exposición, la reveló, y por eso el reporte merece agradecimiento y no sospecha.

## Tensión, prueba y limitación

**Tensión documentada:** valorar el reporte incentiva que las personas avisen, pero cada aviso abre preguntas incómodas sobre quién más vio la información y obliga a corregir permisos que el negocio consideraba normales

**Desarrollo/investigación propuesto:** recorrer el caso de una analista que recibe en un resumen datos salariales de otra área, desde la llamada a la mesa de ayuda hasta la corrección del permiso, la revisión de accesos previos y la decisión de notificar

**Error a evitar:** cerrar el ticket ajustando el asistente o pidiendo a la persona que no vuelva a consultar, sin corregir el permiso sobreexpuesto que cualquier otra búsqueda puede volver a revelar

**Producto observable:** un guion de atención para la mesa de ayuda con criterios de escalamiento, un procedimiento de corrección de permisos de origen y un registro de reportes con causa y acción

## Relaciones candidatas

- `HC-011` — `ESPECIALIZA`: aplica la seguridad de datos en IA al reporte de una sobreexposición
- `M5.2-K07` — `OPERACIONALIZA`: define cómo la mesa de ayuda clasifica y escala el reporte recibido
- `AMP-31` — `REQUIERE`: la gestión de postura de datos busca sobreexposiciones similares en otras fuentes
- `M5.2-K09` — `CONDICIONA`: la revisión de accesos previos determina si corresponde notificar una brecha

**Especializa:** `HC-011`.

## Ejercicio de método

Conserva la pregunta inicial. En un caso real, identifica qué datos la harían relevante, prueba la tesis contra al menos una interpretación alternativa y explica cuál sería la decisión revisable. Entrega un guion de atención para la mesa de ayuda con criterios de escalamiento, un procedimiento de corrección de permisos de origen y un registro de reportes con causa y acción. Se considera logrado solo si la evidencia documenta la tesis sin transformar la pregunta original en hecho establecido.

## Procedencia

[corpus de pre-ensayos mayéuticos](../../../Curado02/02_metodo_mayeutico/src-corpus-preensayos__4e216917f657.json), `preensayos[id=APN-27]`.

Pregunta original: [src-preguntas-consolidadas__37298ee439f0.json](../../../Curado02/02_metodo_mayeutico/src-preguntas-consolidadas__37298ee439f0.json), `preguntas[id=PN-27]`. Toda relación marcada en la fuente sigue siendo candidata para revisión por expertos, no una arista aprobada de la ontología.

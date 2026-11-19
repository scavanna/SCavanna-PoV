<!-- generado-gm24 sha256:1c87312141df40f6c1913322a42864b12d13b642e880c6ea1f9b73ec26cb4691 -->
# APN-23 — Controles del asistente corporativo en dispositivos no gestionados

**Tipo:** tesis ampliada por pregunta · **Estado:** propuesta editorial del corpus mayéutico, no concepto original GM-24 · **Ubicación:** Vínculo transversal; sin asignación exclusiva a unidad.

## Pregunta original (sin sustituirla)

`PN-23` · interrogativa: ¿Con qué controles se usan los asistentes corporativos desde dispositivos personales y móviles (aplicación gestionada, bloqueo de copiar y pegar hacia aplicaciones no gestionadas, cifrado, borrado selectivo)?

La formulación anterior es contenido de la fuente. La tesis siguiente no es una cita literal de esa pregunta: es el **enunciado declarativo ya registrado como propuesta** en el corpus de pre-ensayos.

## Tesis propuesta

En dispositivos personales y móviles, el asistente corporativo solo debería operar dentro de una aplicación gestionada que cifre los datos, impida copiar contenido hacia aplicaciones no gestionadas y permita el borrado selectivo sin tocar la información personal. Si esos controles no pueden verificarse en un dispositivo, el acceso debe limitarse a modos sin descarga ni copia.

## Tensión, prueba y limitación

**Tensión documentada:** las personas aceptan proteger datos corporativos en su teléfono pero rechazan que la organización administre el dispositivo completo, y los controles a nivel de aplicación respetan más su privacidad pero dependen del cliente y pueden eludirse

**Desarrollo/investigación propuesto:** probar en un teléfono personal protegido solo a nivel de aplicación si un resumen del asistente puede copiarse a una aplicación de mensajería, capturarse en pantalla o persistir después de un borrado selectivo

**Error a evitar:** dar por protegido el uso móvil porque la aplicación exige credenciales corporativas, sin verificar qué ocurre con el contenido generado una vez que aparece en pantalla

**Producto observable:** una política de protección de aplicación para el asistente con controles de copia, cifrado y borrado, resultados de prueba por sistema operativo móvil y un registro de dispositivos excluidos

## Relaciones candidatas

- `HC-011` — `ESPECIALIZA`: aplica la seguridad de datos en IA al uso desde dispositivos no gestionados
- `M2.2-K10` — `REQUIERE`: condiciona el acceso según el estado y el nivel de gestión del dispositivo
- `G2.2-K06` — `OPERACIONALIZA`: traduce la política de uso móvil en controles técnicos verificables
- `M3.2-K09` — `RECIBE_EVIDENCIA_DE`: las pruebas de efectividad confirman copia bloqueada y borrado selectivo

**Especializa:** `HC-011`.

## Ejercicio de método

Conserva la pregunta inicial. En un caso real, identifica qué datos la harían relevante, prueba la tesis contra al menos una interpretación alternativa y explica cuál sería la decisión revisable. Entrega una política de protección de aplicación para el asistente con controles de copia, cifrado y borrado, resultados de prueba por sistema operativo móvil y un registro de dispositivos excluidos. Se considera logrado solo si la evidencia documenta la tesis sin transformar la pregunta original en hecho establecido.

## Procedencia

[corpus de pre-ensayos mayéuticos](../../../Curado02/02_metodo_mayeutico/src-corpus-preensayos__4e216917f657.json), `preensayos[id=APN-23]`.

Pregunta original: [src-preguntas-consolidadas__37298ee439f0.json](../../../Curado02/02_metodo_mayeutico/src-preguntas-consolidadas__37298ee439f0.json), `preguntas[id=PN-23]`. Toda relación marcada en la fuente sigue siendo candidata para revisión por expertos, no una arista aprobada de la ontología.

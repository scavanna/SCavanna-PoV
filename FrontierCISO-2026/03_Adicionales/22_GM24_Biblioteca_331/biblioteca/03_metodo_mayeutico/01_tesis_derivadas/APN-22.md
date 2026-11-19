<!-- generado-gm24 sha256:ee4862522c23fad95e7bf4cbac97f9e77fb8902c9e4549b0f384e7cecd337b0a -->
# APN-22 — Detección y revocación de secretos expuestos en prompts y código

**Tipo:** tesis ampliada por pregunta · **Estado:** propuesta editorial del corpus mayéutico, no concepto original GM-24 · **Ubicación:** Vínculo transversal; sin asignación exclusiva a unidad.

## Pregunta original (sin sustituirla)

`PN-22` · interrogativa: ¿Cómo detectamos, revocamos y rotamos las contraseñas, claves y tokens que las personas pegan en asistentes de IA o que aparecen en código sugerido por ellos?

La formulación anterior es contenido de la fuente. La tesis siguiente no es una cita literal de esa pregunta: es el **enunciado declarativo ya registrado como propuesta** en el corpus de pre-ensayos.

## Tesis propuesta

Todo secreto pegado en un asistente de IA o aparecido en código sugerido debe tratarse como comprometido: se detecta en el prompt, el repositorio y los registros, se revoca y se rota con un procedimiento ya probado. La prevención ayuda, pero la capacidad que importa es reducir el tiempo entre la exposición y la revocación.

## Tensión, prueba y limitación

**Tensión documentada:** inspeccionar prompts para encontrar secretos exige observar lo que las personas escriben, y cuando la detección ocurre el secreto ya salió del perímetro, por lo que solo sirve si la rotación es inmediata

**Desarrollo/investigación propuesto:** sembrar una clave de prueba en un prompt y en una sugerencia de código aceptada, y medir qué control la detecta, quién recibe la alerta y cuánto tarda la rotación sin interrumpir el servicio

**Error a evitar:** suponer que borrar el prompt o el historial elimina la exposición, cuando el secreto pudo quedar en registros del proveedor, en el contexto del asistente o en ramas del repositorio

**Producto observable:** un patrón de detección de secretos aplicado a prompts y repositorios, un procedimiento de revocación y rotación probado con tiempos registrados y un inventario de secretos con dueño

## Relaciones candidatas

- `HC-011` — `ESPECIALIZA`: acota la seguridad de datos en IA a secretos expuestos en prompts y código
- `AMP-33` — `REQUIERE`: necesita saber a qué identidad no humana pertenece cada secreto para rotarlo
- `M6.2-K03` — `SE_ALIMENTA_DE`: los controles del ciclo de desarrollo detectan secretos en código sugerido
- `M5.1-K07` — `OPERACIONALIZA`: traduce la exposición de secretos en un playbook de revocación ejecutable

**Especializa:** `HC-011`.

## Ejercicio de método

Conserva la pregunta inicial. En un caso real, identifica qué datos la harían relevante, prueba la tesis contra al menos una interpretación alternativa y explica cuál sería la decisión revisable. Entrega un patrón de detección de secretos aplicado a prompts y repositorios, un procedimiento de revocación y rotación probado con tiempos registrados y un inventario de secretos con dueño. Se considera logrado solo si la evidencia documenta la tesis sin transformar la pregunta original en hecho establecido.

## Procedencia

[corpus de pre-ensayos mayéuticos](../../../Curado02/02_metodo_mayeutico/src-corpus-preensayos__4e216917f657.json), `preensayos[id=APN-22]`.

Pregunta original: [src-preguntas-consolidadas__37298ee439f0.json](../../../Curado02/02_metodo_mayeutico/src-preguntas-consolidadas__37298ee439f0.json), `preguntas[id=PN-22]`. Toda relación marcada en la fuente sigue siendo candidata para revisión por expertos, no una arista aprobada de la ontología.

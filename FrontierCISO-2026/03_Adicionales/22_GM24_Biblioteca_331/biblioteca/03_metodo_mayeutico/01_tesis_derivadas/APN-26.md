<!-- generado-gm24 sha256:fae659ea2f742ec1089577ed93fee95a03e340d59b6e087b3c423fa186100dad -->
# APN-26 — Escenario de cuenta ejecutiva comprometida con asistente de IA

**Tipo:** tesis ampliada por pregunta · **Estado:** propuesta editorial del corpus mayéutico, no concepto original GM-24 · **Ubicación:** Vínculo transversal; sin asignación exclusiva a unidad.

## Pregunta original (sin sustituirla)

`PN-26` · interrogativa: «Si roban la cuenta de un ejecutivo, ¿el atacante puede usar su asistente de IA para encontrar todo lo confidencial?»

La formulación anterior es contenido de la fuente. La tesis siguiente no es una cita literal de esa pregunta: es el **enunciado declarativo ya registrado como propuesta** en el corpus de pre-ensayos.

## Tesis propuesta

La respuesta al directorio es que el atacante podrá encontrar con el asistente todo lo que el ejecutivo tiene permiso de ver, y mucho más rápido. Por eso el CISO debe presentar un escenario con el alcance real de esos permisos, la sobreexposición ya corregida, la fortaleza de la autenticación ejecutiva y el tiempo de contención probado.

## Tensión, prueba y limitación

**Tensión documentada:** los ejecutivos necesitan acceso amplio para decidir y rechazan fricción adicional, pero ese mismo acceso, sumado al asistente, convierte su cuenta en el atajo más eficiente hacia toda la información confidencial

**Desarrollo/investigación propuesto:** simular con una cuenta de prueba que replica los permisos de un ejecutivo las consultas que haría un atacante sobre adquisiciones, salarios y litigios, y mostrar al directorio qué devolvió el asistente antes y después de corregir permisos

**Error a evitar:** responder que el asistente respeta los permisos como si eso tranquilizara, cuando el problema es precisamente que los permisos acumulados del ejecutivo exceden lo que necesita

**Producto observable:** un análisis de escenario con alcance de permisos y consecuencias para el negocio, un plan de reducción de sobreexposición en cuentas ejecutivas y el resultado de una simulación de contención

## Relaciones candidatas

- `HC-011` — `ESPECIALIZA`: aplica la seguridad de datos en IA al caso de una cuenta ejecutiva
- `G5.1-K08` — `OPERACIONALIZA`: construye un escenario concreto con alcance, consecuencia y controles existentes
- `M3.1-K09` — `REQUIERE`: exige reducir permisos acumulados que el asistente vuelve fácilmente explotables
- `G1.2-K10` — `SE_COMUNICA_MEDIANTE`: el escenario se presenta a la junta en lenguaje de consecuencias de negocio

**Especializa:** `HC-011`.

## Ejercicio de método

Conserva la pregunta inicial. En un caso real, identifica qué datos la harían relevante, prueba la tesis contra al menos una interpretación alternativa y explica cuál sería la decisión revisable. Entrega un análisis de escenario con alcance de permisos y consecuencias para el negocio, un plan de reducción de sobreexposición en cuentas ejecutivas y el resultado de una simulación de contención. Se considera logrado solo si la evidencia documenta la tesis sin transformar la pregunta original en hecho establecido.

## Procedencia

[corpus de pre-ensayos mayéuticos](../../../Curado02/02_metodo_mayeutico/src-corpus-preensayos__4e216917f657.json), `preensayos[id=APN-26]`.

Pregunta original: [src-preguntas-consolidadas__37298ee439f0.json](../../../Curado02/02_metodo_mayeutico/src-preguntas-consolidadas__37298ee439f0.json), `preguntas[id=PN-26]`. Toda relación marcada en la fuente sigue siendo candidata para revisión por expertos, no una arista aprobada de la ontología.

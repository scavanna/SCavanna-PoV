<!-- generado-gm24 sha256:0f1d1fe1aa5a71489f1695e3471131e7cd63ed938a6a4b0302dfededaa789c95 -->
# APN-32 — Línea base de funciones de IA nativas en equipos corporativos

**Tipo:** tesis ampliada por pregunta · **Estado:** propuesta editorial del corpus mayéutico, no concepto original GM-24 · **Ubicación:** `M6.2` (especialización explícita).

## Pregunta original (sin sustituirla)

`PN-32` · interrogativa: «¿Qué funciones de IA del sistema operativo y del navegador dejamos activadas en los equipos corporativos?»

La formulación anterior es contenido de la fuente. La tesis siguiente no es una cita literal de esa pregunta: es el **enunciado declarativo ya registrado como propuesta** en el corpus de pre-ensayos.

## Tesis propuesta

El equipo de puesto de trabajo necesita una línea base aprobada que indique, función por función, qué capacidades de IA incluidas en el sistema operativo y en el navegador quedan activas, cuáles se desactivan y por qué. El CISO responde con esa decisión documentada, su dueño y una verificación periódica, porque cada actualización puede agregar funciones nuevas activadas por defecto.

## Tensión, prueba y limitación

**Tensión documentada:** desactivar todo por defecto es fácil de justificar pero priva a las personas de mejoras útiles, mientras decidir función por función exige un análisis continuo que el equipo de puesto de trabajo no tiene previsto

**Desarrollo/investigación propuesto:** revisar las notas de versión recientes del navegador y del sistema operativo, identificar cada función de IA agregada y decidir con los dueños de datos cuáles se activan, restringen o bloquean

**Error a evitar:** creer que la configuración aprobada en la imagen inicial sigue vigente, cuando cada actualización puede incorporar funciones de IA activadas sin aviso

**Producto observable:** una línea base de funciones de IA con decisión y justificación por función, un control de deriva en el parque de equipos y un procedimiento de revisión ante cada actualización

## Relaciones candidatas

- `M6.2-K04` — `ESPECIALIZA`: aplica la seguridad de IA a funciones nativas del sistema operativo y del navegador
- `G2.2-K03` — `OPERACIONALIZA`: convierte el estándar de configuración en decisiones por función de IA
- `G2.2-K07` — `REQUIERE`: exige revisar la línea base ante cada actualización del proveedor
- `M4.2-K06` — `GESTIONA`: controla la superficie que agregan funciones de IA activadas por defecto

**Especializa:** `M6.2-K04`.

## Ejercicio de método

Conserva la pregunta inicial. En un caso real, identifica qué datos la harían relevante, prueba la tesis contra al menos una interpretación alternativa y explica cuál sería la decisión revisable. Entrega una línea base de funciones de IA con decisión y justificación por función, un control de deriva en el parque de equipos y un procedimiento de revisión ante cada actualización. Se considera logrado solo si la evidencia documenta la tesis sin transformar la pregunta original en hecho establecido.

## Procedencia

[corpus de pre-ensayos mayéuticos](../../../Curado02/02_metodo_mayeutico/src-corpus-preensayos__4e216917f657.json), `preensayos[id=APN-32]`.

Pregunta original: [src-preguntas-consolidadas__37298ee439f0.json](../../../Curado02/02_metodo_mayeutico/src-preguntas-consolidadas__37298ee439f0.json), `preguntas[id=PN-32]`. Toda relación marcada en la fuente sigue siendo candidata para revisión por expertos, no una arista aprobada de la ontología.

<!-- generado-gm24 sha256:f480873bbf4fafdb77c782801a08d198e09f13904bf73fcd837bbad274d23355 -->
# APN-04 — Gobierno de funciones de IA activadas por defecto

**Tipo:** tesis ampliada por pregunta · **Estado:** propuesta editorial del corpus mayéutico, no concepto original GM-24 · **Ubicación:** `M6.2` (especialización explícita).

## Pregunta original (sin sustituirla)

`PN-04` · interrogativa: ¿Qué funciones de IA llegan activadas por defecto en el software que ya usamos (navegador, sistema operativo, ofimática, reuniones), quién decide habilitarlas y con qué evaluación previa?

La formulación anterior es contenido de la fuente. La tesis siguiente no es una cita literal de esa pregunta: es el **enunciado declarativo ya registrado como propuesta** en el corpus de pre-ensayos.

## Tesis propuesta

El CISO debe acordar con Tecnología y Compras que ninguna función de IA incorporada en el software existente quede activa por decisión del proveedor: cada una debe inventariarse, evaluarse según los datos que procesa y adónde los envía, y habilitarse por decisión explícita de un responsable, con configuración centralizada y revisión en cada actualización.

## Tensión, prueba y limitación

**Tensión documentada:** desactivar por defecto todas las funciones de IA protege los datos pero priva a las personas de mejoras que pagamos y las empuja a alternativas no controladas, mientras que aceptarlas como llegan cede al proveedor la decisión de riesgo

**Desarrollo/investigación propuesto:** revisar las notas de la última actualización del navegador, el sistema operativo, la suite de oficina y la herramienta de reuniones, listar las funciones de IA nuevas y decidir para cada una habilitar, restringir o bloquear

**Error a evitar:** suponer que una herramienta ya aprobada sigue aprobada después de que el proveedor le agrega funciones de IA, cuando cambian los datos que procesa, adónde los envía y quién los ve

**Producto observable:** un inventario de funciones de IA incorporadas con su estado de habilitación, un procedimiento de evaluación previo a cada activación y cláusulas de compra que exijan aviso previo y control administrativo

## Relaciones candidatas

- `M6.2-K06` — `ESPECIALIZA`: trata la IA que el proveedor activa sin pedido como uso no gobernado
- `G3.1-K04` — `REQUIERE`: los contratos deben obligar al aviso y control de nuevas funciones
- `HC-011` — `CONDICIONA`: la habilitación condiciona qué datos quedan expuestos a la IA incorporada
- `G2.2-K06` — `OPERACIONALIZA`: la decisión se aplica con configuración centralizada en los equipos

**Especializa:** `M6.2-K06`.

## Ejercicio de método

Conserva la pregunta inicial. En un caso real, identifica qué datos la harían relevante, prueba la tesis contra al menos una interpretación alternativa y explica cuál sería la decisión revisable. Entrega un inventario de funciones de IA incorporadas con su estado de habilitación, un procedimiento de evaluación previo a cada activación y cláusulas de compra que exijan aviso previo y control administrativo. Se considera logrado solo si la evidencia documenta la tesis sin transformar la pregunta original en hecho establecido.

## Procedencia

[corpus de pre-ensayos mayéuticos](../../../Curado02/02_metodo_mayeutico/src-corpus-preensayos__4e216917f657.json), `preensayos[id=APN-04]`.

Pregunta original: [src-preguntas-consolidadas__37298ee439f0.json](../../../Curado02/02_metodo_mayeutico/src-preguntas-consolidadas__37298ee439f0.json), `preguntas[id=PN-04]`. Toda relación marcada en la fuente sigue siendo candidata para revisión por expertos, no una arista aprobada de la ontología.

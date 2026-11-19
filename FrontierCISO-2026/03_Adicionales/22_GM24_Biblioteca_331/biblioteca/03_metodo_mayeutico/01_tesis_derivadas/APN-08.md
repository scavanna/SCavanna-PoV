<!-- generado-gm24 sha256:b7c7121d72c30ec3faab15286b030924d48c2e90cbe8a8dc8ba09d95ef1b4600 -->
# APN-08 — Uso compartido y promoción de agentes personales

**Tipo:** tesis ampliada por pregunta · **Estado:** propuesta editorial del corpus mayéutico, no concepto original GM-24 · **Ubicación:** `M6.2` (especialización explícita).

## Pregunta original (sin sustituirla)

`PN-08` · interrogativa: ¿Qué agentes y automatizaciones personales comparten las personas con colegas o con externos, con qué datos de base, y quién aprueba que pasen de uso personal a uso de equipo?

La formulación anterior es contenido de la fuente. La tesis siguiente no es una cita literal de esa pregunta: es el **enunciado declarativo ya registrado como propuesta** en el corpus de pre-ensayos.

## Tesis propuesta

El CISO debe acordar con el COE de IA y la plataforma de productividad que compartir con colegas o externos un agente o automatización personal requiere conocer sus datos de base, porque puede exponer a otros los archivos de su creador, y que pasar a uso de equipo exige aprobación, dueño asignado, revisión de conectores e ingreso al inventario.

## Tensión, prueba y limitación

**Tensión documentada:** compartir agentes personales difunde buenas prácticas y multiplica su valor sin pasar por proyectos formales, pero cada copia hereda permisos y datos pensados para una sola persona y queda sin dueño cuando su creador cambia de puesto

**Desarrollo/investigación propuesto:** rastrear un agente creado por una analista con sus propios archivos y compartido luego con su equipo y un proveedor, verificando qué datos ven los demás, con qué permisos actúa y qué control habría exigido aprobarlo

**Error a evitar:** tratar los agentes personales como documentos que se comparten libremente, ignorando que actúan con permisos y datos del creador y pueden ejecutar acciones en nombre de quien los usa

**Producto observable:** un inventario de agentes compartidos con sus datos de base y destinatarios, un procedimiento de promoción a uso de equipo con criterios de aprobación y una prueba de revocación del acceso compartido

## Relaciones candidatas

- `M6.2-K06` — `ESPECIALIZA`: aborda el uso no gobernado que surge al compartir agentes personales
- `AMP-36` — `OPERACIONALIZA`: aplica límites de permisos al momento de compartir o promover un agente
- `AMP-12` — `REQUIERE`: cada agente de equipo necesita un dueño que responda por él
- `AMP-32` — `SE_ALIMENTA_DE`: aplica criterios de gobierno sobre los datos de base de cada agente

**Especializa:** `M6.2-K06`.

## Ejercicio de método

Conserva la pregunta inicial. En un caso real, identifica qué datos la harían relevante, prueba la tesis contra al menos una interpretación alternativa y explica cuál sería la decisión revisable. Entrega un inventario de agentes compartidos con sus datos de base y destinatarios, un procedimiento de promoción a uso de equipo con criterios de aprobación y una prueba de revocación del acceso compartido. Se considera logrado solo si la evidencia documenta la tesis sin transformar la pregunta original en hecho establecido.

## Procedencia

[corpus de pre-ensayos mayéuticos](../../../Curado02/02_metodo_mayeutico/src-corpus-preensayos__4e216917f657.json), `preensayos[id=APN-08]`.

Pregunta original: [src-preguntas-consolidadas__37298ee439f0.json](../../../Curado02/02_metodo_mayeutico/src-preguntas-consolidadas__37298ee439f0.json), `preguntas[id=PN-08]`. Toda relación marcada en la fuente sigue siendo candidata para revisión por expertos, no una arista aprobada de la ontología.

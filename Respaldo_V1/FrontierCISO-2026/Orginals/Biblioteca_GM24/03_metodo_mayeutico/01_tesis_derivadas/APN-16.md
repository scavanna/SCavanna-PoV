<!-- generado-gm24 sha256:267a20846ea55c10b79edd45292164fafe5ecd05dc46019e0395539b24097ff2 -->
# APN-16 — Condiciones para compartir agentes basados en archivos personales

**Tipo:** tesis ampliada por pregunta · **Estado:** propuesta editorial del corpus mayéutico, no concepto original GM-24 · **Ubicación:** `M6.2` (especialización explícita).

## Pregunta original (sin sustituirla)

`PN-16` · interrogativa: «¿Puedo compartir con mi equipo el agente que armé con mis archivos?»

La formulación anterior es contenido de la fuente. La tesis siguiente no es una cita literal de esa pregunta: es el **enunciado declarativo ya registrado como propuesta** en el corpus de pre-ensayos.

## Tesis propuesta

Compartir un agente personal es aceptable cuando quienes lo reciben ya tienen acceso a cada archivo que lo alimenta, el agente no actúa con los permisos de su creador y existe un dueño que lo mantiene. El CISO responde con una regla clara y una aprobación ágil, y demuestra su cumplimiento con el registro de agentes compartidos.

## Tensión, prueba y limitación

**Tensión documentada:** prohibir compartir agentes frena una práctica útil y empuja a copias informales, pero permitirlo sin revisión convierte archivos personales en una base de conocimiento abierta a personas que nunca tuvieron permiso para verlos

**Desarrollo/investigación propuesto:** simular que un analista comparte con su equipo un agente alimentado con contratos de su carpeta personal, y verificar qué documentos revela el agente a cada colega según los permisos de ese colega

**Error a evitar:** suponer que el acceso legítimo del creador a los archivos se extiende a quienes reciben el agente, o que compartir un agente no equivale a compartir sus datos

**Producto observable:** una regla de publicación de agentes con criterios sobre permisos heredados, un flujo de aprobación con dueño designado y un registro de agentes compartidos con sus fuentes de datos

## Relaciones candidatas

- `M6.2-K06` — `ESPECIALIZA`: aborda el uso no gobernado que surge cuando un agente personal se comparte
- `AMP-34` — `REQUIERE`: define con qué identidad y permisos actúa el agente ante cada usuario
- `AMP-32` — `OPERACIONALIZA`: aplica el gobierno de fuentes de conocimiento a agentes creados por usuarios
- `G2.2-K05` — `SE_COMUNICA_MEDIANTE`: la regla para compartir agentes llega a las personas por la comunicación de políticas

**Especializa:** `M6.2-K06`.

## Ejercicio de método

Conserva la pregunta inicial. En un caso real, identifica qué datos la harían relevante, prueba la tesis contra al menos una interpretación alternativa y explica cuál sería la decisión revisable. Entrega una regla de publicación de agentes con criterios sobre permisos heredados, un flujo de aprobación con dueño designado y un registro de agentes compartidos con sus fuentes de datos. Se considera logrado solo si la evidencia documenta la tesis sin transformar la pregunta original en hecho establecido.

## Procedencia

[corpus de pre-ensayos mayéuticos](../../../Curado02/02_metodo_mayeutico/src-corpus-preensayos__4e216917f657.json), `preensayos[id=APN-16]`.

Pregunta original: [src-preguntas-consolidadas__37298ee439f0.json](../../../Curado02/02_metodo_mayeutico/src-preguntas-consolidadas__37298ee439f0.json), `preguntas[id=PN-16]`. Toda relación marcada en la fuente sigue siendo candidata para revisión por expertos, no una arista aprobada de la ontología.

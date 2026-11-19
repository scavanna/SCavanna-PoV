<!-- generado-gm24 sha256:3923d4514da92d6237bebb69141f96c10f9531ffb7837d0236b3ab63a9eb18d5 -->
# APN-30 — Modelo operativo para alertas y tareas de los asistentes

**Tipo:** tesis ampliada por pregunta · **Estado:** propuesta editorial del corpus mayéutico, no concepto original GM-24 · **Ubicación:** Vínculo transversal; sin asignación exclusiva a unidad.

## Pregunta original (sin sustituirla)

`PN-30` · interrogativa: «¿Qué alertas y tareas nuevas nos traen los asistentes de productividad, y quién las atiende?»

La formulación anterior es contenido de la fuente. La tesis siguiente no es una cita literal de esa pregunta: es el **enunciado declarativo ya registrado como propuesta** en el corpus de pre-ensayos.

## Tesis propuesta

Los asistentes traen alertas y tareas nuevas, como sobreexposición de datos, uso anómalo, solicitudes de excepción e intentos de manipulación, y cada tipo necesita un dueño explícito antes del despliegue. El CISO responde a su equipo con un catálogo de casos de detección, la asignación por tipo, la capacidad estimada y criterios para retirar alertas que no cambian decisiones.

## Tensión, prueba y limitación

**Tensión documentada:** agregar detecciones para cada riesgo nuevo de la IA parece prudente, pero sin retirar otras ni asignar dueños fuera del SOC, la carga cae sobre el mismo equipo que ya no alcanza a atender lo existente

**Desarrollo/investigación propuesto:** registrar durante un piloto cada alerta, tarea y solicitud que generan los asistentes, clasificarlas por tipo y dueño natural, y estimar qué parte deberían resolver protección de datos, la mesa de ayuda o el negocio

**Error a evitar:** asumir que toda alerta relacionada con la IA pertenece al SOC, cuando gran parte de la carga es corrección de permisos, gestión de excepciones y respuesta a consultas de las personas

**Producto observable:** un catálogo de alertas y tareas de los asistentes con dueño asignado, una estimación de capacidad por equipo y acuerdos de nivel de servicio probados en el piloto

## Relaciones candidatas

- `HC-018` — `ESPECIALIZA`: aplica la observabilidad de controles a la carga operativa que generan los asistentes
- `M4.1-K01` — `CONDICIONA`: redefine qué atiende el SOC y qué se deriva a otros equipos
- `M1.1-K06` — `REQUIERE`: exige capacidad asignada y no solo nuevas reglas de detección
- `G4.1-K08` — `OPERACIONALIZA`: asigna dueños explícitos a cada tipo de alerta y tarea

**Especializa:** `HC-018`.

## Ejercicio de método

Conserva la pregunta inicial. En un caso real, identifica qué datos la harían relevante, prueba la tesis contra al menos una interpretación alternativa y explica cuál sería la decisión revisable. Entrega un catálogo de alertas y tareas de los asistentes con dueño asignado, una estimación de capacidad por equipo y acuerdos de nivel de servicio probados en el piloto. Se considera logrado solo si la evidencia documenta la tesis sin transformar la pregunta original en hecho establecido.

## Procedencia

[corpus de pre-ensayos mayéuticos](../../../Curado02/02_metodo_mayeutico/src-corpus-preensayos__4e216917f657.json), `preensayos[id=APN-30]`.

Pregunta original: [src-preguntas-consolidadas__37298ee439f0.json](../../../Curado02/02_metodo_mayeutico/src-preguntas-consolidadas__37298ee439f0.json), `preguntas[id=PN-30]`. Toda relación marcada en la fuente sigue siendo candidata para revisión por expertos, no una arista aprobada de la ontología.

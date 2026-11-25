<!-- generado-gm24 sha256:7f0e03d76f5d60fc0f777b382fac54400aaf3ad65162fce9c6dd46e34d34cf63 -->
# APN-05 — Señalización de usos restringidos en herramientas de IA autorizadas

**Tipo:** tesis ampliada por pregunta · **Estado:** propuesta editorial del corpus mayéutico, no concepto original GM-24 · **Ubicación:** `M1.2` (especialización explícita).

## Pregunta original (sin sustituirla)

`PN-05` · interrogativa: ¿Qué usos siguen prohibidos o requieren aprobación aunque la herramienta de IA esté autorizada (evaluar personas, decidir créditos o beneficios, redactar documentos legales, tratar datos de salud), y cómo lo sabe la persona en el momento de usarla?

La formulación anterior es contenido de la fuente. La tesis siguiente no es una cita literal de esa pregunta: es el **enunciado declarativo ya registrado como propuesta** en el corpus de pre-ensayos.

## Tesis propuesta

El CISO debe acordar con Legal, Recursos Humanos y Cumplimiento que autorizar una herramienta de IA no habilita todos sus usos: valorar candidatos o desempeño, otorgar créditos o prestaciones, elaborar textos jurídicos o procesar información médica requieren aprobación específica, y la persona debe recibir ese aviso dentro de la herramienta mientras trabaja, no solo en una política.

## Tensión, prueba y limitación

**Tensión documentada:** un aviso en cada uso sensible protege a la persona y a la organización, pero si aparece con demasiada frecuencia se ignora, y si depende de detectar el propósito puede fallar justo en los casos de mayor impacto

**Desarrollo/investigación propuesto:** simular que un analista de selección pide al asistente autorizado que ordene candidatos según sus currículos, y decidir qué debería ver en ese momento, a quién debería pedir aprobación y qué quedaría registrado

**Error a evitar:** suponer que publicar una política de uso aceptable basta para que las personas reconozcan un uso restringido, cuando la decisión se toma en segundos y dentro de la herramienta

**Producto observable:** una lista de usos restringidos con su nivel de aprobación, mensajes en contexto configurados en las herramientas autorizadas y un circuito de aprobación con registro de excepciones

## Relaciones candidatas

- `AMP-30` — `ESPECIALIZA`: distingue la herramienta autorizada de los usos que siguen restringidos
- `AMP-25` — `SE_ALIMENTA_DE`: los usos restringidos derivan del impacto en derechos de las personas
- `G2.2-K05` — `OPERACIONALIZA`: lleva la comunicación de la política al momento exacto de uso
- `G2.2-K09` — `REQUIERE`: los usos restringidos aprobados se gestionan como excepciones registradas

**Especializa:** `AMP-30`.

## Ejercicio de método

Conserva la pregunta inicial. En un caso real, identifica qué datos la harían relevante, prueba la tesis contra al menos una interpretación alternativa y explica cuál sería la decisión revisable. Entrega una lista de usos restringidos con su nivel de aprobación, mensajes en contexto configurados en las herramientas autorizadas y un circuito de aprobación con registro de excepciones. Se considera logrado solo si la evidencia documenta la tesis sin transformar la pregunta original en hecho establecido.

## Procedencia

[corpus de pre-ensayos mayéuticos](../../../Curado02/02_metodo_mayeutico/src-corpus-preensayos__4e216917f657.json), `preensayos[id=APN-05]`.

Pregunta original: [src-preguntas-consolidadas__37298ee439f0.json](../../../Curado02/02_metodo_mayeutico/src-preguntas-consolidadas__37298ee439f0.json), `preguntas[id=PN-05]`. Toda relación marcada en la fuente sigue siendo candidata para revisión por expertos, no una arista aprobada de la ontología.

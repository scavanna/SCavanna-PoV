<!-- generado-gm24 sha256:e2786080be15d319d1e31c47ee1081141cb41eb08aae15d49f9df01aaa04ec34 -->
# APN-34 — Aplicación técnica de reglas de datos por herramienta de IA

**Tipo:** tesis ampliada por pregunta · **Estado:** propuesta editorial del corpus mayéutico, no concepto original GM-24 · **Ubicación:** `G2.2` (especialización explícita).

## Pregunta original (sin sustituirla)

`PN-34` · interrogativa: ¿Las reglas sobre qué datos se pueden escribir o subir a cada herramienta de IA se aplican con controles técnicos en el navegador, el endpoint y la red, o dependen solo de la política?

La formulación anterior es contenido de la fuente. La tesis siguiente no es una cita literal de esa pregunta: es el **enunciado declarativo ya registrado como propuesta** en el corpus de pre-ensayos.

## Tesis propuesta

Una regla sobre los datos que pueden entregarse a la IA solo protege cuando se aplica técnicamente para cada herramienta, con controles coherentes entre navegador, puesto de trabajo y red, diferenciados según el tipo de cuenta. Si depende solo de la política, sirve para asignar culpas después del incidente, pero no para evitarlo ni para demostrar control.

## Tensión, prueba y limitación

**Tensión documentada:** inspeccionar lo que se escribe y se sube en cada herramienta permite aplicar la regla con precisión, pero exige descifrar tráfico y observar contenido sensible, con costos de privacidad, rendimiento y falsos positivos que frenan el trabajo

**Desarrollo/investigación propuesto:** probar una misma regla, como impedir que un archivo con datos de clientes llegue a una herramienta no aprobada, mediante carga en el navegador, copia desde una aplicación de escritorio y envío desde un móvil

**Error a evitar:** contar las políticas de prevención de pérdida configuradas como prueba de aplicación, sin verificar si cubren pegado de texto, cargas de archivos y aplicaciones de escritorio

**Producto observable:** una matriz de reglas por herramienta, tipo de dato y punto de control, resultados de pruebas por canal y un registro de excepciones con justificación y vencimiento

## Relaciones candidatas

- `G2.2-K06` — `ESPECIALIZA`: aplica la exigibilidad de políticas a los datos que ingresan a herramientas de IA
- `M2.1-K02` — `REQUIERE`: las reglas dependen de etiquetas de datos que los controles puedan leer
- `HC-011` — `OPERACIONALIZA`: lleva la seguridad de datos en IA a controles técnicos en cada canal
- `M3.2-K09` — `SE_SUPERVISA_CON`: las pruebas por canal confirman que la regla se aplica realmente

**Especializa:** `G2.2-K06`.

## Ejercicio de método

Conserva la pregunta inicial. En un caso real, identifica qué datos la harían relevante, prueba la tesis contra al menos una interpretación alternativa y explica cuál sería la decisión revisable. Entrega una matriz de reglas por herramienta, tipo de dato y punto de control, resultados de pruebas por canal y un registro de excepciones con justificación y vencimiento. Se considera logrado solo si la evidencia documenta la tesis sin transformar la pregunta original en hecho establecido.

## Procedencia

[corpus de pre-ensayos mayéuticos](../../../Curado02/02_metodo_mayeutico/src-corpus-preensayos__4e216917f657.json), `preensayos[id=APN-34]`.

Pregunta original: [src-preguntas-consolidadas__37298ee439f0.json](../../../Curado02/02_metodo_mayeutico/src-preguntas-consolidadas__37298ee439f0.json), `preguntas[id=PN-34]`. Toda relación marcada en la fuente sigue siendo candidata para revisión por expertos, no una arista aprobada de la ontología.

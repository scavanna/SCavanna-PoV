<!-- generado-gm24 sha256:7b7f104af679c7867d50659a03aaa89422ebc8787c028ef6c7fc594b8cf2f3ed -->
# APN-18 — Paridad de acceso condicional en clientes y API del asistente

**Tipo:** tesis ampliada por pregunta · **Estado:** propuesta editorial del corpus mayéutico, no concepto original GM-24 · **Ubicación:** `M2.2` (especialización explícita).

## Pregunta original (sin sustituirla)

`PN-18` · interrogativa: ¿Los asistentes, sus aplicaciones de escritorio y móviles, sus API y sus extensiones exigen los mismos controles de acceso que el resto de las aplicaciones (MFA resistente al phishing, dispositivo conforme, acceso condicional), o abren una puerta lateral?

La formulación anterior es contenido de la fuente. La tesis siguiente no es una cita literal de esa pregunta: es el **enunciado declarativo ya registrado como propuesta** en el corpus de pre-ensayos.

## Tesis propuesta

Cada vía de acceso al asistente, sea web, escritorio, móvil, API o extensión, debe exigir los mismos controles que las demás aplicaciones corporativas: autenticación resistente al phishing, dispositivo conforme y evaluación de riesgo de la sesión. Una sola vía con autenticación heredada o tokens de larga duración anula esos controles y debe tratarse como exposición abierta.

## Tensión, prueba y limitación

**Tensión documentada:** endurecer todas las vías protege el canal más débil, pero los clientes móviles, las API y las extensiones suelen usar flujos de autenticación propios, y cerrarlos puede romper integraciones que el negocio ya adoptó

**Desarrollo/investigación propuesto:** levantar todas las vías de acceso al asistente y probar cada una con un dispositivo no conforme y un factor débil, documentando cuáles exigen el control, cuáles lo omiten y qué tokens persisten

**Error a evitar:** verificar el acceso condicional solo en el portal web y suponer que se hereda en aplicaciones de escritorio, clientes móviles, llamadas a la API y extensiones

**Producto observable:** un inventario de vías de acceso al asistente con su flujo de autenticación, una matriz de cobertura de controles por vía y evidencia de pruebas negativas repetibles

## Relaciones candidatas

- `M2.2-K10` — `ESPECIALIZA`: aplica el contexto de acceso a cada vía de entrada al asistente
- `M2.2-K02` — `REQUIERE`: exige autenticación resistente al phishing también en clientes, API y extensiones
- `M4.2-K06` — `GESTIONA`: reduce la superficie de ataque que agregan los clientes y las API del asistente
- `HC-038` — `SE_SUPERVISA_CON`: el aseguramiento Zero Trust detecta vías del asistente que quedaron fuera de la política

**Especializa:** `M2.2-K10`.

## Ejercicio de método

Conserva la pregunta inicial. En un caso real, identifica qué datos la harían relevante, prueba la tesis contra al menos una interpretación alternativa y explica cuál sería la decisión revisable. Entrega un inventario de vías de acceso al asistente con su flujo de autenticación, una matriz de cobertura de controles por vía y evidencia de pruebas negativas repetibles. Se considera logrado solo si la evidencia documenta la tesis sin transformar la pregunta original en hecho establecido.

## Procedencia

[corpus de pre-ensayos mayéuticos](../../../Curado02/02_metodo_mayeutico/src-corpus-preensayos__4e216917f657.json), `preensayos[id=APN-18]`.

Pregunta original: [src-preguntas-consolidadas__37298ee439f0.json](../../../Curado02/02_metodo_mayeutico/src-preguntas-consolidadas__37298ee439f0.json), `preguntas[id=PN-18]`. Toda relación marcada en la fuente sigue siendo candidata para revisión por expertos, no una arista aprobada de la ontología.

<!-- generado-gm24 sha256:f222ffe71d229423fbfb60239d5fba82ad36fcd1dcf480b9c9e6af7123d86d89 -->
# APN-17 — Acceso a servicios de IA solo con identidad corporativa

**Tipo:** tesis ampliada por pregunta · **Estado:** propuesta editorial del corpus mayéutico, no concepto original GM-24 · **Ubicación:** `M6.2` (especialización explícita).

## Pregunta original (sin sustituirla)

`PN-17` · interrogativa: ¿Impedimos el ingreso con cuentas personales a servicios de IA desde equipos y redes corporativas, y permitimos solo el acceso con la identidad corporativa y sus protecciones?

La formulación anterior es contenido de la fuente. La tesis siguiente no es una cita literal de esa pregunta: es el **enunciado declarativo ya registrado como propuesta** en el corpus de pre-ensayos.

## Tesis propuesta

En equipos y redes de la organización, todo servicio de IA debe usarse con la identidad corporativa, sujeta a controles de autenticación, registro y protección de datos, y el acceso mediante cuentas personales a esos servicios debe bloquearse técnicamente. Sin esa separación, la organización no puede auditar, retener ni recuperar lo que se comparte, aunque la herramienta esté aprobada.

## Tensión, prueba y limitación

**Tensión documentada:** bloquear cuentas personales cierra un canal de fuga difícil de ver, pero desplaza el uso hacia dispositivos y redes no gestionados, donde la organización pierde toda visibilidad y control

**Desarrollo/investigación propuesto:** probar desde un equipo gestionado el ingreso a un servicio de IA aprobado con cuenta personal y con cuenta corporativa, por red interna, acceso remoto y conexión doméstica, anotando qué capa bloquea y qué evidencia queda

**Error a evitar:** suponer que aprobar la versión corporativa de un servicio impide usar su versión de consumo, cuando ambas suelen compartir dominio, aplicación y pantalla de inicio de sesión

**Producto observable:** una matriz de servicios de IA con el control aplicado para restringir cuentas no corporativas, resultados de prueba por canal de conexión y un registro de excepciones con vencimiento

## Relaciones candidatas

- `M6.2-K06` — `ESPECIALIZA`: convierte el control del uso no gobernado en restricción de cuentas personales
- `M2.2-K09` — `REQUIERE`: depende de que los servicios acepten solo identidades federadas de la organización
- `G2.2-K06` — `OPERACIONALIZA`: aplica técnicamente la política de uso de IA en el punto de acceso
- `M3.2-K09` — `SE_SUPERVISA_CON`: pruebas periódicas confirman que el bloqueo funciona en cada canal de conexión

**Especializa:** `M6.2-K06`.

## Ejercicio de método

Conserva la pregunta inicial. En un caso real, identifica qué datos la harían relevante, prueba la tesis contra al menos una interpretación alternativa y explica cuál sería la decisión revisable. Entrega una matriz de servicios de IA con el control aplicado para restringir cuentas no corporativas, resultados de prueba por canal de conexión y un registro de excepciones con vencimiento. Se considera logrado solo si la evidencia documenta la tesis sin transformar la pregunta original en hecho establecido.

## Procedencia

[corpus de pre-ensayos mayéuticos](../../../Curado02/02_metodo_mayeutico/src-corpus-preensayos__4e216917f657.json), `preensayos[id=APN-17]`.

Pregunta original: [src-preguntas-consolidadas__37298ee439f0.json](../../../Curado02/02_metodo_mayeutico/src-preguntas-consolidadas__37298ee439f0.json), `preguntas[id=PN-17]`. Toda relación marcada en la fuente sigue siendo candidata para revisión por expertos, no una arista aprobada de la ontología.

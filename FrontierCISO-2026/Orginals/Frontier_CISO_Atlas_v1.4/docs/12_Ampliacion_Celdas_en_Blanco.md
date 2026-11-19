> **Registro de la versión 1.3 (16 de noviembre de 2026).** Este documento se conserva tal como se publicó. Las cifras, los estados y los archivos que cita corresponden a esa versión. El estado vigente está en `docs/15_Decisiones_delegadas_y_relectura_1_4.md` y en los documentos 16 a 19.

# Ampliación para las celdas en blanco (serie APX)

**Frontier CISO Atlas 1.3** · Taxonomía 6.0 (reglas de asignación, revisión 2) · Ontología 2.1.0 · GM-24 V7.1 · 16 de noviembre de 2026 · Estado: decisiones de diseño confirmadas por el autor; reglas adoptadas según la lectura del curador y corpus releído a ciegas por lectores automáticos, con una lectura para todos y dos donde la primera difería; contenido candidato, sin validación humana

## 1. Qué es esto

Son **16 pre-ensayos** escritos para las celdas del Atlas que no tenían contenido o tenían un solo pre-ensayo: el dominio D19, el dominio D27 y la subfunción RC05.

**Estado.** Tu aceptación en bloque se leyó como un «sí» a la serie (decisión D-10) y el 16 de noviembre de 2026 confirmaste esa lectura (D-14.3). La revisión crítica de la versión 1.2 la leyó entera: 4 pre-ensayos quedaron como estaban y 12 se corrigieron. 4 cambiaron un valor primario de su coordenada o su horizonte (5 valores) y 1 más cambiaron solo fuerzas, mecanismos o secundarios; las 22 filas están en `data/cambios_1_1_a_1_2.csv`. La redacción corregida no tuvo una nueva lectura completa. Entran al grafo candidato como **capa de ampliación** (conjunto de cambios CHG-CAND-16). No integran el corpus base de 739 pre-ensayos, no cuentan en sus estadísticas y no cuentan como evidencia para admitir un dominio. Los cambios que les hizo la revisión crítica quedaron confirmados en bloque el 16 de noviembre (D-13.4, leído de la frase «Confirmo el resto de los cambios»). Podés corregir o descartar cualquiera cuando quieras.

**Relectura de la versión 1.3.** Los 16 se releyeron a ciegas con las reglas adoptadas, y cada uno tuvo dos lecturas. Cambiaron 10 coordenadas primarias en 8 pre-ensayos. APX-02 (ahora en D17), APX-05 (ahora en D14), APX-06 (ahora en D15) y APX-07 (ahora en D12) salieron del dominio D19, para el que se habían escrito: D19 les queda como secundario. Cada ficha dice qué cambió y con qué motivo.

- **Formato:** el de tus ampliaciones por pregunta, con tesis, tensión, desarrollo, error frecuente y producto. Tienen entre 156 y 202 palabras.
- **Voz:** los escribí yo siguiendo el formato. No son tu voz.
- **Coordenada:** la propuse al redactar y la leyó un revisor independiente. Cada ficha trae la justificación, la confianza y qué cambió. No tiene revisión humana.
- **Referencias:** indican afinidad temática con elementos de la base de referencia. No respaldan cada afirmación del pre-ensayo. Tres pre-ensayos citan además la subcategoría de NIST CSF 2.0 que la verificación externa confirmó en la fuente.
- **Relación con el corpus:** cada ficha dice a qué pre-ensayos existentes especializa o con cuáles se relaciona.

**Tres límites que conviene tener presentes.**

1. Llenar una celda vacía con texto que no es tuyo borra una señal útil: que todavía no escribiste sobre ese tema. Por eso la serie queda aparte del corpus.
2. Las fuentes que la revisión propone sumar a la base antes de aceptar APX-10 y APX-11 (una guía de saneamiento de soportes y una norma de informes de aseguramiento) no se incorporaron.
3. La versión 1.2 advertía que 6 de los 7 pre-ensayos alojados en D19 aplican una disciplina a los dispositivos conectados y que, con la regla RP-01, su dominio primario pasaría a ser el de la disciplina. La regla quedó adoptada, según la lectura que el curador hizo de «Acepto el cambio de reglas», y la relectura la aplicó en 4 de ellos. 2 de los 3 que siguen en D19 tienen una función de disciplina. En ellos la relectura no cambió el dominio: o las dos lecturas sostuvieron D19, o una lo llevó a otro dominio y la otra no. Cada ficha dice cuál es el caso. La celda que la serie venía a llenar vuelve a tener poco contenido.

## 2. Resumen

| Celda | Pre-ensayos del corpus base (versión 1.3) | De la serie APX | Identificadores | Revisión crítica 1.2 | Siguen en la celda después de la relectura 1.3 |
|---|---|---|---|---|---|
| Dominio D19 · IoT & Cyber-Physical Systems Security | 0 | 7 | APX-01 a APX-07 | 2 sin cambios y 5 corregidos | 3 |
| Dominio D27 · Physical, Environmental & Facility Security | 1 | 5 | APX-08 a APX-12 | 2 sin cambios y 3 corregidos | 5 |
| Subfunción RC05 · Comunicación de la recuperación y restitución de la confianza | 0 | 3 | APX-13, APX-15, APX-16 | 3 corregidos | 3 |
| Subfunción RC03 · Validación de recuperación y retorno seguro | 5 | 1 | APX-14 | 1 corregido | 1 |

La tabla agrupa los pre-ensayos por la celda en que los dejó la revisión crítica de la versión 1.2; la última columna dice cuántos siguen en ella después de la relectura. Con la capa de ampliación y con las coordenadas de la versión 1.3, D19 pasa de 0 a 3 pre-ensayos, D27 de 1 a 6 y RC05 de 0 a 3. Las estadísticas del corpus base no cuentan la serie.

No hay propuestas para el territorio T01. La Biblioteca cognitiva tiene 883 conceptos que llevan ese territorio, pero en la base es un valor por categoría y no una clasificación por concepto: elegir cuáles se desarrollan como pre-ensayos sigue sin decidir. No es una de las cinco proposiciones de la decisión D-12, que cerraste sin revisar la Biblioteca.

## 3. Dominio D19 · IoT & Cyber-Physical Systems Security

### APX-01 · Inventario y propiedad de los dispositivos conectados que nadie gestiona

**Pregunta que responde.** ¿Cuántos dispositivos conectados hay en nuestras sedes que no figuran en ningún inventario, y quién responde por cada uno?

**Tesis.** Cámaras, impresoras, sensores de edificio, pantallas, equipos médicos o de laboratorio y otros dispositivos conectados forman parte de la superficie de ataque aunque no los compre ni los opere Tecnología; el CISO debe lograr que cada uno tenga dueño, función, ubicación en la red y fecha de fin de soporte registrados, porque lo que no tiene dueño no se actualiza ni se retira.

**Tensión.** Quienes compran y usan estos dispositivos son áreas como mantenimiento, servicios generales o salud, que no se ven a sí mismas como responsables de un activo digital, mientras que Seguridad no tiene autoridad sobre sus compras.

**Desarrollo.** Descubrir los dispositivos de una sede por su tráfico, cruzar el resultado con los registros de compras y de mantenimiento, y asignar a cada clase de dispositivo un dueño de negocio y un responsable técnico.

**Error frecuente.** Confiar en el inventario de equipos gestionados y dar por inexistente lo que no tiene agente instalado.

**Producto.** Un inventario de dispositivos conectados por sede con dueño, función, segmento de red, versión de software y fin de soporte, y una regla de alta y de baja acordada con Compras.

| Eje | Coordenada |
|---|---|
| Territorio | T04 Risk & Resilience (secundarios: T05) |
| Dominio | D19 IoT & Cyber-Physical Systems Security (secundarios: D13) |
| Subfunción | ID01 Inventario y clasificación de activos (secundarios: GV02) |
| Horizonte | H02 Evolving |
| Fuerzas y mecanismos | INH04 Silos organizacionales |
| Pilar MCCS | DO Entrega y operación |
| Confianza | media |

**Por qué esa coordenada.** La tesis pide que cada dispositivo conectado tenga dueño, función, ubicación en la red y fin de soporte registrados: es inventario de activos (ID01) de dispositivos conectados (D19), visto desde el diseño de controles (T05).

**Relación con el corpus.** Se relaciona con M2.1-K03 («Inventario»); se relaciona con M6.2-K05 («IoT/OT Security»).

**Afinidad temática con la base de referencia.** CyBOK 1.2: Cyber-Physical Systems Security; ETSI EN 303 645 V3.1.3; Microsoft SAF: OT/IoT Security; NIST CSF 2.0: ID.AM Asset Management.

**Resultado de la revisión crítica.** Quedó como estaba.

**Relectura de la versión 1.3.** Dos lecturas a ciegas coincidieron en otro valor y la coordenada cambió: territorio T05 → T04. El valor anterior queda como secundario. La tabla de arriba muestra la coordenada nueva; el texto de «Por qué esa coordenada» es anterior al cambio.

*Motivo de los lectores para el cambio de territorio.* El objeto es el inventario y la propiedad de los dispositivos conectados que Tecnología no compra ni opera (cámaras, impresoras, sensores de edificio, equipos médicos), con dueño, función, ubicación en la red y fin de soporte: es el inventario de un tipo de activo (D19, ID01) y la tesis parte de que son superficie de ataque sin dueño (T04). / El objeto es el inventario y la propiedad de los dispositivos conectados que Tecnología no compra ni opera (cámaras, impresoras, sensores de edificio, equipos médicos), que son superficie de ataque: es el inventario de un tipo de activo, que queda en el dominio de ese activo (D19) con ID01, visto desde la exposición que crean sin dueño (T04).

### APX-02 · Requisitos de seguridad en la compra de dispositivos conectados

**Pregunta que responde.** ¿Qué le exigimos a un fabricante antes de conectar su dispositivo a nuestra red, y cómo lo comprobamos?

**Tesis.** La seguridad de un dispositivo conectado se decide en buena parte en la compra: el CISO debe llevar a pliegos y contratos requisitos mínimos y verificables —sin contraseñas universales por defecto, canal para reportar vulnerabilidades, actualizaciones durante un período de soporte declarado y almacenamiento seguro de credenciales— y lograr que un producto que no los cumple solo se admita con una excepción aprobada.

**Tensión.** El área que compra prioriza precio, funcionalidad y plazo, y el fabricante rara vez negocia con un cliente individual; el requisito solo pesa si es condición de admisión y no un criterio más de puntaje, y la regulación que en algunas jurisdicciones obliga a los fabricantes no reemplaza la comprobación propia.

**Desarrollo.** Tomar una compra reciente de dispositivos conectados, contrastar la documentación del fabricante con la lista de requisitos y registrar qué se puede comprobar antes de comprar y qué solo se descubre en operación.

**Error frecuente.** Evaluar el servicio en la nube del proveedor y olvidar el dispositivo, su software y su ciclo de actualización.

**Producto.** Una cláusula tipo de requisitos de seguridad para dispositivos conectados, una comprobación antes de comprar y otra al recibir el equipo, y el registro de excepciones con dueño y vencimiento.

| Eje | Coordenada |
|---|---|
| Territorio | T08 Trust & Assurance (secundarios: T03) |
| Dominio | D17 Third-Party & Supply Chain Security (secundarios: D19, D03) |
| Subfunción | GV09 Gobierno de terceros y ecosistemas (secundarios: GV03) |
| Horizonte | H02 Evolving |
| Fuerzas y mecanismos | CAT03 Presión regulatoria, HOM08 Gobierno y supervisión |
| Pilar MCCS | OS Sistema operativo |
| Confianza | media |

**Por qué esa coordenada.** La tesis lleva requisitos mínimos y verificables a pliegos y contratos: es gestión de requisitos a terceros (GV09) sobre dispositivos conectados (D19), desde la evidencia exigible al proveedor (T08).

**Relación con el corpus.** Ninguna declarada.

**Afinidad temática con la base de referencia.** ETSI EN 303 645 V3.1.3; Reglamento (UE) 2024/2847 de Ciberresiliencia (CRA); CyBOK 1.2: Cyber-Physical Systems Security.

**Resultado de la revisión crítica.** Se corrigió: producto, tensión, tesis y título.

**Relectura de la versión 1.3.** Dos lecturas a ciegas coincidieron en otro valor y la coordenada cambió: dominio D19 → D17. El valor anterior queda como secundario. La tabla de arriba muestra la coordenada nueva; el texto de «Por qué esa coordenada» es anterior al cambio. Con este cambio el pre-ensayo sale de la celda D19, para la que se escribió.

*Motivo de los lectores para el cambio de dominio.* El objeto son los requisitos de seguridad mínimos y verificables que se llevan a pliegos y contratos al comprar dispositivos conectados, con admisión solo por excepción aprobada: la tesis trata la relación de compra con el fabricante y no el control técnico del dispositivo (D17 con D19 secundario), cómo se comprueba al tercero antes de admitirlo (T08) y los requisitos y contratos de la cadena de suministro (GV09). / El objeto son los requisitos mínimos y verificables que se llevan a pliegos y contratos al comprar dispositivos conectados, con comprobación propia y excepción aprobada: es gobierno de proveedores aplicado a un dispositivo, y la tesis trata cómo se exige y se comprueba al fabricante.

### APX-03 · Aislar lo que no puede protegerse a sí mismo

**Pregunta que responde.** Si mañana se compromete una cámara o una impresora, ¿hasta dónde puede llegar el atacante desde ahí?

**Tesis.** Muchos dispositivos conectados no admiten agente, autenticación fuerte ni parches frecuentes; como no pueden protegerse a sí mismos, la protección debe venir sobre todo de la arquitectura: segmentos propios por clase de dispositivo, comunicaciones permitidas solo hacia los destinos que su función requiere, ningún acceso entrante directo desde internet y salida a internet solo hacia destinos declarados y por un punto controlado.

**Tensión.** Cada segmento y cada regla agregan costo operativo y fricción con los proveedores que piden acceso remoto amplio para dar soporte; sin segmentación, un dispositivo comprometido puede servir de punto de entrada al resto de la red.

**Desarrollo.** Elegir una clase de dispositivo, documentar con qué sistemas necesita comunicarse, aplicar la regla mínima y observar qué deja de funcionar antes de generalizarla.

**Error frecuente.** Ubicar los dispositivos en la red de usuarios por comodidad y dejar el acceso del proveedor abierto de forma permanente.

**Producto.** Un patrón de segmentación por clase de dispositivo, la matriz de comunicaciones permitidas y un procedimiento de acceso remoto de terceros aprobado, temporal y registrado.

| Eje | Coordenada |
|---|---|
| Territorio | T05 Security Architecture |
| Dominio | D19 IoT & Cyber-Physical Systems Security (secundarios: D08, D25) |
| Subfunción | PR03 Hardening y arquitectura segura (secundarios: PR01) |
| Horizonte | H01 Foundational |
| Fuerzas y mecanismos | INH01 Deuda tecnológica |
| Pilar MCCS | DO Entrega y operación |
| Confianza | media |

**Por qué esa coordenada.** La tesis ubica la protección en la arquitectura de red por clase de dispositivo: es arquitectura segura (PR03) para dispositivos conectados (D19), desde el diseño de controles (T05).

**Relación con el corpus.** Ninguna declarada.

**Afinidad temática con la base de referencia.** ETSI EN 303 645 V3.1.3; CyBOK 1.2: Cyber-Physical Systems Security; Microsoft SAF: OT/IoT Security.

**Resultado de la revisión crítica.** Se corrigió: tensión y tesis.

**Relectura de la versión 1.3.** Dos lecturas a ciegas coinciden con la coordenada en los tres ejes primarios.

### APX-04 · Actualización, fin de soporte y retiro de dispositivos conectados

**Pregunta que responde.** ¿Qué dispositivos conectados siguen en producción sin soporte del fabricante, y quién aceptó ese riesgo?

**Tesis.** Un dispositivo conectado suele vivir más que el soporte de su fabricante; el CISO debe exigir que cada clase de dispositivo tenga una decisión explícita sobre cómo se actualiza, qué se hace cuando el fabricante deja de publicar correcciones y cuándo se retira, porque un equipo sin soporte que sigue en producción es un riesgo que la organización asume de hecho sin que nadie con autoridad lo haya aceptado.

**Tensión.** El equipo funciona y reemplazarlo cuesta; el área usuaria no ve motivo para cambiar algo que cumple su tarea, y actualizarlo puede exigir detener un servicio.

**Desarrollo.** Listar los dispositivos de una sede con su versión y su fecha de fin de soporte, identificar los que ya la superaron y decidir caso por caso entre actualizar, aislar, reemplazar o aceptar el riesgo con vencimiento y con la firma del dueño del proceso que usa el equipo.

**Error frecuente.** Actualizar una sola vez, durante la instalación, y no volver a hacerlo.

**Producto.** Un calendario de fin de soporte por clase de dispositivo, la decisión registrada y firmada por el dueño del proceso para cada equipo fuera de soporte, y el presupuesto de reemplazo asociado.

| Eje | Coordenada |
|---|---|
| Territorio | T04 Risk & Resilience (secundarios: T05) |
| Dominio | D19 IoT & Cyber-Physical Systems Security (secundarios: D13) |
| Subfunción | GV04 Apetito, tolerancia y aceptación de riesgo (secundarios: PR04) |
| Horizonte | H01 Foundational |
| Fuerzas y mecanismos | INH01 Deuda tecnológica, HOM01 Apetito y tolerancia al riesgo |
| Pilar MCCS | DO Entrega y operación |
| Confianza | media |

**Por qué esa coordenada.** La tesis exige una decisión explícita y firmada sobre los equipos que superan el soporte del fabricante: es aceptación de riesgo (GV04) sobre dispositivos conectados (D19), desde la gestión del riesgo (T04).

**Relación con el corpus.** Especializa APC-023 («Decisión de aislar, reemplazar o aceptar sistemas heredados»); especializa APA-052 («Tratamiento de sistemas heredados sin actualización posible»).

**Afinidad temática con la base de referencia.** ETSI EN 303 645 V3.1.3; Reglamento (UE) 2024/2847 de Ciberresiliencia (CRA).

**Resultado de la revisión crítica.** Se corrigió: desarrollo, producto y tesis. Cambió la coordenada (subfunciones secundarias y subfunción): El revisor señala que la tesis es una decisión de riesgo sobre equipos sin soporte y que el corpus ya codifica esa tesis en GV04 (APC-023 y APA-052). Se acepta: GV04 pasa a primaria y PR04 a secundaria.

**Relectura de la versión 1.3.** En dominio y subfunción, una lectura difiere y la otra sostiene el valor vigente: no cambiaron.

### APX-05 · Vigilar por el comportamiento lo que no admite agente

**Pregunta que responde.** ¿Cómo nos enteraríamos de que un dispositivo conectado empezó a comportarse de otra manera?

**Tesis.** Como muchos dispositivos conectados no admiten un agente de detección, la vigilancia debe apoyarse en lo que sí se observa: su tráfico de red, sus consultas de nombres y los registros de los sistemas con los que se comunican; el CISO debe asegurar que cada clase de dispositivo tenga un perfil de comportamiento esperado y que el desvío genere una alerta que alguien atiende.

**Tensión.** El comportamiento de estos equipos suele ser repetitivo y por eso más fácil de perfilar que el de un equipo de usuario, pero su volumen y su variedad superan lo que el centro de operaciones conoce, y rara vez alguien definió qué es normal para una cámara o un sensor.

**Desarrollo.** Perfilar una clase de dispositivo durante un período, definir tres desvíos que justifican una alerta, como un destino nuevo en internet, y probar la detección con un caso simulado.

**Error frecuente.** Dar por vigilado un dispositivo porque figura en el inventario.

**Producto.** Perfiles de comportamiento por clase de dispositivo, casos de uso de detección con dueño y prueba, y el criterio de escalamiento de cada alerta: quién la atiende, en qué plazo y quién decide actuar sobre un equipo que presta un servicio físico.

| Eje | Coordenada |
|---|---|
| Territorio | T06 Security Operations |
| Dominio | D14 Security Monitoring & Detection (secundarios: D19) |
| Subfunción | DE01 Telemetría y observabilidad (secundarios: DE02) |
| Horizonte | H02 Evolving |
| Fuerzas y mecanismos | INH09 Limitaciones operativas, HOM04 Monitoreo continuo |
| Pilar MCCS | DO Entrega y operación |
| Confianza | media |

**Por qué esa coordenada.** La tesis apoya la vigilancia en el tráfico y los registros de los dispositivos que no admiten agente: es telemetría y observabilidad (DE01) de dispositivos conectados (D19), desde la operación (T06).

**Relación con el corpus.** Ninguna declarada.

**Afinidad temática con la base de referencia.** ETSI EN 303 645 V3.1.3; CyBOK 1.2: Cyber-Physical Systems Security; NIST CSF 2.0: DE.CM Continuous Monitoring.

**Resultado de la revisión crítica.** Se corrigió: producto, tensión y tesis.

**Relectura de la versión 1.3.** Dos lecturas a ciegas coincidieron en otro valor y la coordenada cambió: dominio D19 → D14. El valor anterior queda como secundario. La tabla de arriba muestra la coordenada nueva; el texto de «Por qué esa coordenada» es anterior al cambio. Con este cambio el pre-ensayo sale de la celda D19, para la que se escribió.

*Motivo de los lectores para el cambio de dominio.* La tesis aplica la disciplina de vigilancia y detección a los dispositivos conectados que no admiten agente: cada clase debe tener un perfil de comportamiento esperado y el desvío debe generar una alerta atendida, apoyándose en el tráfico de red, las consultas de nombres y los registros; por eso el dominio es el monitoreo, con el dispositivo conectado como objeto secundario. / El objeto es la vigilancia de dispositivos conectados que no admiten agente, apoyada en tráfico de red, consultas de nombres y registros, con perfil esperado y alerta por desvío: es monitoreo aplicado a IoT (D14 con D19 secundario) y su primera prescripción es la telemetría.

En subfunción, una lectura difiere y la otra sostiene el valor vigente: no cambió.

### APX-06 · Cuando el incidente digital tiene efecto físico

**Pregunta que responde.** Si hay que desconectar un sistema que controla algo físico, ¿quién lo decide y cómo sigue funcionando el servicio?

**Tesis.** Un incidente en dispositivos conectados puede abrir una puerta, detener un ascensor, alterar la temperatura de una cámara de frío o dejar sin servicio a un equipo médico; el plan de respuesta debe anteponer la seguridad de las personas, definir quién decide desconectar un equipo y prever cómo sigue funcionando el servicio físico mientras tanto.

**Tensión.** La respuesta habitual de aislar el equipo comprometido puede causar un daño mayor que el ataque, y quienes conocen el proceso físico no forman parte del equipo de respuesta.

**Desarrollo.** Recorrer con mantenimiento, seguridad física y el área usuaria un escenario de compromiso de un sistema de edificio, y acordar qué se puede desconectar, quién lo autoriza y cuál es el modo manual.

**Error frecuente.** Aplicar el procedimiento de respuesta de la tecnología de oficina a equipos cuyo fallo afecta a personas o a instalaciones.

**Producto.** Un anexo del plan de respuesta para dispositivos con efecto físico, con criterios de desconexión, autoridad de decisión, contactos y modo de operación manual probado.

| Eje | Coordenada |
|---|---|
| Territorio | T06 Security Operations (secundarios: T04) |
| Dominio | D15 Incident Response & Crisis Management (secundarios: D19, D18) |
| Subfunción | RS01 Preparación y coordinación de respuesta (secundarios: RC02) |
| Horizonte | H04 Convergent |
| Fuerzas y mecanismos | INH04 Silos organizacionales, HOM05 Respuesta a incidentes |
| Pilar MCCS | DO Entrega y operación |
| Confianza | media |

**Por qué esa coordenada.** La tesis trata la respuesta cuando contener en lo digital tiene efecto físico: es preparación y coordinación de la respuesta (RS01) en sistemas ciberfísicos (D19), desde el riesgo y la resiliencia (T04).

**Relación con el corpus.** Se relaciona con M6.2-K05 («IoT/OT Security»).

**Afinidad temática con la base de referencia.** CyBOK 1.2: Cyber-Physical Systems Security; Microsoft SAF: OT/IoT Security.

**Resultado de la revisión crítica.** Quedó como estaba.

**Relectura de la versión 1.3.** Dos lecturas a ciegas coincidieron en otro valor y la coordenada cambió: territorio T04 → T06 y dominio D19 → D15. El valor anterior queda como secundario. La tabla de arriba muestra la coordenada nueva; el texto de «Por qué esa coordenada» es anterior al cambio. Con este cambio el pre-ensayo sale de la celda D19, para la que se escribió.

*Motivo de los lectores para el cambio de territorio.* El objeto es el plan de respuesta a incidentes en dispositivos conectados con efecto físico: anteponer la seguridad de las personas, definir quién decide desconectar un equipo y prever cómo sigue el servicio; se aplica la disciplina de respuesta (D15, T06, RS01: plan y roles) a un objeto ciberfísico (D19 secundario), con la operación degradada como secundaria (RC02). / La tesis prescribe un plan de respuesta para incidentes en dispositivos conectados con efecto físico que anteponga la seguridad de las personas, fije quién decide desconectar y prevea el modo manual: es la disciplina de respuesta aplicada a IoT (D15 con D19 secundario), en la operación (T06) y como preparación de la respuesta (RS01).

*Motivo de los lectores para el cambio de dominio.* El objeto es el plan de respuesta a incidentes en dispositivos conectados con efecto físico: anteponer la seguridad de las personas, definir quién decide desconectar un equipo y prever cómo sigue el servicio; se aplica la disciplina de respuesta (D15, T06, RS01: plan y roles) a un objeto ciberfísico (D19 secundario), con la operación degradada como secundaria (RC02). / La tesis prescribe un plan de respuesta para incidentes en dispositivos conectados con efecto físico que anteponga la seguridad de las personas, fije quién decide desconectar y prevea el modo manual: es la disciplina de respuesta aplicada a IoT (D15 con D19 secundario), en la operación (T06) y como preparación de la respuesta (RS01).

### APX-07 · Modelar las amenazas del dispositivo antes de integrarlo

**Pregunta que responde.** ¿Qué amenazas se derivan de las propiedades de los dispositivos que fabricamos o integramos, y cuáles quedan sin mitigar?

**Tesis.** Cuando la organización fabrica, integra o adapta dispositivos conectados, el análisis de amenazas debe partir de las propiedades del propio dispositivo —su hardware, su software de sistema, sus aplicaciones y sus interfaces de red— y no solo del servicio al que se conecta; el CISO debe exigir ese análisis antes de la puesta en producción y un nivel de mitigación acordado para cada amenaza relevante.

**Tensión.** El equipo que integra el dispositivo conoce su función, pero no sus componentes internos, y el fabricante no siempre los documenta.

**Desarrollo.** Tomar un dispositivo de uso extendido, enumerar sus propiedades, derivar las amenazas que le aplican y clasificar cada mitigación como presente, ausente o no verificable.

**Error frecuente.** Limitar la evaluación a un escaneo de vulnerabilidades de la interfaz de red.

**Producto.** Un modelo de amenazas por tipo de dispositivo, la lista de mitigaciones exigidas al fabricante o al integrador y las brechas aceptadas con dueño y fecha.

| Eje | Coordenada |
|---|---|
| Territorio | T05 Security Architecture (secundarios: T04) |
| Dominio | D12 Threat Intelligence & Threat Modeling (secundarios: D19, D11) |
| Subfunción | ID03 Amenazas, vulnerabilidades y exposición (secundarios: PR04) |
| Horizonte | Indeterminado: el texto no describe una fuerza de cambio que permita fijarlo |
| Fuerzas y mecanismos | Ninguno nombrado |
| Pilar MCCS | DO Entrega y operación |
| Confianza | media |

**Por qué esa coordenada.** La tesis pide derivar las amenazas de las propiedades del dispositivo antes de integrarlo: es análisis de amenazas y exposición (ID03) sobre dispositivos conectados (D19), desde el diseño (T05).

**Relación con el corpus.** Ninguna declarada.

**Afinidad temática con la base de referencia.** MITRE EMB3D 2.0.2; CyBOK 1.2: Cyber-Physical Systems Security; Reglamento (UE) 2024/2847 de Ciberresiliencia (CRA).

**Resultado de la revisión crítica.** Se corrigió: pregunta. Cambió la coordenada (horizonte): El revisor señala que el texto no da ninguna evidencia evolutiva que sostenga H03. La regla de asignación pide horizonte solo cuando el texto lo sustenta: pasa a «indeterminado». El dominio D12 como primario quedó a criterio del curador y no se cambia.

**Relectura de la versión 1.3.** Dos lecturas a ciegas coincidieron en otro valor y la coordenada cambió: dominio D19 → D12. El valor anterior queda como secundario. La tabla de arriba muestra la coordenada nueva; el texto de «Por qué esa coordenada» es anterior al cambio. Con este cambio el pre-ensayo sale de la celda D19, para la que se escribió.

*Motivo de los lectores para el cambio de dominio.* La tesis pide que el análisis de amenazas de un dispositivo conectado parta de sus propias propiedades (hardware, software de sistema, aplicaciones e interfaces) y se exija antes de la puesta en producción: es modelado de amenazas (D12 con ID03) aplicado a un dispositivo, como práctica de ingeniería previa a la integración (T05). / El objeto es el análisis de amenazas de un dispositivo conectado a partir de sus propias propiedades (hardware, software de sistema, aplicaciones e interfaces), exigido antes de la puesta en producción: es modelado de amenazas (D12 con ID03) aplicado a un objeto de D19, que queda como secundario, y la perspectiva es la ingeniería del control antes de integrar (T05).

## 4. Dominio D27 · Physical, Environmental & Facility Security

### APX-08 · Perímetros físicos por zonas y acceso verificable

**Pregunta que responde.** ¿Quién puede entrar hoy a nuestras salas críticas, y cuándo se revisó esa lista por última vez?

**Tesis.** El acceso físico a las áreas donde se procesan o se guardan activos críticos debe organizarse por zonas con requisitos crecientes y con registro de quién entró, cuándo y con qué autorización; el CISO no opera las puertas, pero debe poder demostrar que el acceso físico a un centro de datos, a una sala de comunicaciones o a un puesto de operaciones se concede, se revisa y se revoca con el mismo rigor que el acceso lógico.

**Tensión.** La seguridad física depende de otra área y de proveedores de vigilancia, con sistemas, criterios y registros propios que Seguridad de la información no ve.

**Desarrollo.** Elegir una sala crítica y comparar la lista de personas autorizadas con las que ingresaron en un mes y con las bajas de personal del mismo período.

**Error frecuente.** Revisar con cuidado las credenciales lógicas y no revisar nunca las tarjetas de acceso de exempleados y contratistas.

**Producto.** Un mapa de zonas con sus requisitos, el registro de ingresos conservado y revisado, una revisión periódica de autorizaciones físicas y la conciliación de altas y bajas entre recursos humanos, el registro de contratistas, accesos lógicos y accesos físicos.

| Eje | Coordenada |
|---|---|
| Territorio | T05 Security Architecture (secundarios: T08) |
| Dominio | D27 Physical, Environmental & Facility Security (secundarios: D05) |
| Subfunción | PR06 Resiliencia de la infraestructura y protección física y ambiental (secundarios: PR01) |
| Horizonte | H01 Foundational |
| Fuerzas y mecanismos | INH04 Silos organizacionales |
| Pilar MCCS | DO Entrega y operación |
| Confianza | media |

**Por qué esa coordenada.** La tesis exige que el acceso físico se conceda, se revise y se revoque con evidencia: es protección física (PR06) de instalaciones (D27), desde el diseño de controles (T05). El ancla de PR06 en CSF 2.0 para el acceso físico es PR.AA-06.

**Relación con el corpus.** Ninguna declarada.

**Afinidad temática con la base de referencia.** NIST SP 800-53: PE Physical and Environmental Protection; ISO/IEC 27002: controles físicos; PCI DSS: requisito 9; Swift CSCF: 3 Physically Secure the Environment; DoD CMMC: PE Physical Protection; NIST CSF 2.0: PR.AA Identity Management, Authentication, and Access Control.

**Resultado de la revisión crítica.** Se corrigió: producto.

**Relectura de la versión 1.3.** Dos lecturas a ciegas coinciden con la coordenada en los tres ejes primarios.

### APX-09 · Energía, clima y entorno como condiciones del control

**Pregunta que responde.** ¿Cuánto tiempo siguen funcionando nuestros servicios críticos si falla la energía o la climatización, y cuándo lo probamos?

**Tesis.** Los controles lógicos dependen de condiciones físicas —energía, climatización, detección y extinción de incendios, protección contra el agua— que pueden fallar por causas que no son ataques; el CISO debe tratar esas condiciones como dependencias del programa: saber qué las protege, cómo se vigilan y cuándo se probaron por última vez, tanto en instalaciones propias como en las de terceros.

**Tensión.** Son sistemas a cargo de la infraestructura edilicia, con presupuesto y mantenimiento propios, y su falla suele quedar fuera del análisis de riesgo de ciberseguridad hasta que detiene un servicio.

**Desarrollo.** Identificar, para una sala crítica, las protecciones ambientales, la autonomía real de la energía de respaldo, quién recibe la alarma y qué servicios caen primero si fallan.

**Error frecuente.** Asumir que la energía de respaldo funciona porque existe, sin una prueba con carga.

**Producto.** Un registro de dependencias ambientales por instalación crítica, con responsable, vigilancia, última prueba y su vínculo con los objetivos de recuperación del negocio.

| Eje | Coordenada |
|---|---|
| Territorio | T04 Risk & Resilience (secundarios: T05) |
| Dominio | D27 Physical, Environmental & Facility Security (secundarios: D16) |
| Subfunción | PR06 Resiliencia de la infraestructura y protección física y ambiental (secundarios: RC02) |
| Horizonte | H01 Foundational |
| Fuerzas y mecanismos | HOM06 Continuidad |
| Pilar MCCS | DO Entrega y operación |
| Confianza | media |

**Por qué esa coordenada.** La tesis trata energía, clima y entorno como dependencias del programa: es protección ambiental y resiliencia de la infraestructura (PR06) en instalaciones (D27), desde el riesgo y la resiliencia (T04).

**Relación con el corpus.** Especializa M3.1-K12 («Seguridad física, ambiental y mantenimiento como dependencias del control»).

**Afinidad temática con la base de referencia.** NIST CSF 2.0: PR.IR Technology Infrastructure Resilience; NIST SP 800-53: PE Physical and Environmental Protection; Reglamento de Ejecución (UE) 2024/2690 (NIS2), anexo, sección 13; CSA CCM v4.1: DCS Datacenter Security.

**Resultado de la revisión crítica.** Quedó como estaba.

**Relectura de la versión 1.3.** Dos lecturas a ciegas coinciden con la coordenada en los tres ejes primarios.

### APX-10 · Soportes y equipos: custodia, traslado, reutilización y destrucción

**Pregunta que responde.** ¿Podemos demostrar qué pasó con la información de cada equipo que dimos de baja este año?

**Tesis.** La información sale de la organización también en discos, cintas, equipos que van a reparación y dispositivos que se reasignan o se descartan; el CISO debe asegurar que cada soporte tenga custodia conocida durante toda su vida, que el traslado quede registrado y que el borrado o la destrucción se verifiquen antes de que el equipo cambie de manos.

**Tensión.** El descarte y la reparación los gestionan áreas y proveedores que miden costo y rapidez, no trazabilidad; exigir evidencia de borrado encarece un proceso que nadie considera crítico.

**Desarrollo.** Seguir el recorrido de los equipos dados de baja en un trimestre, desde el retiro hasta el destino final, y comprobar en cuántos existe evidencia de borrado verificado.

**Error frecuente.** Confiar en el formateo o en un certificado genérico del proveedor de descarte.

**Producto.** Un procedimiento de custodia y saneamiento de soportes por nivel de clasificación, el registro de destrucciones con verificación y las cláusulas exigidas a quienes reparan o descartan equipos.

| Eje | Coordenada |
|---|---|
| Territorio | T05 Security Architecture (secundarios: T08) |
| Dominio | D27 Physical, Environmental & Facility Security (secundarios: D06) |
| Subfunción | PR06 Resiliencia de la infraestructura y protección física y ambiental (secundarios: PR02) |
| Horizonte | H01 Foundational |
| Fuerzas y mecanismos | HOM09 Assurance y validación |
| Pilar MCCS | DO Entrega y operación |
| Confianza | media |

**Por qué esa coordenada.** La tesis pide custodia conocida, traslado registrado y borrado o destrucción verificados: es protección de datos en los soportes (PR02) dentro de la seguridad física (D27), desde el diseño de controles (T05).

**Relación con el corpus.** Se relaciona con M2.1-K06 («Retención/Destrucción»).

**Afinidad temática con la base de referencia.** NIST SP 800-53: MP Media Protection; ISO/IEC 27002: controles físicos; DoD CMMC: MP Media Protection.

**Resultado de la revisión crítica.** Quedó como estaba.

**Relectura de la versión 1.3.** Dos lecturas a ciegas coincidieron en otro valor y la coordenada cambió: subfunción PR02 → PR06. El valor anterior queda como secundario. La tabla de arriba muestra la coordenada nueva; el texto de «Por qué esa coordenada» es anterior al cambio.

*Motivo de los lectores para el cambio de subfunción.* El objeto es el destino de los soportes y equipos (custodia conocida, traslado registrado y borrado o destrucción verificados antes de cambiar de manos), que frente a la protección del dato es D27, y la práctica es la protección física con el mantenimiento y el retiro del equipo (PR06), vista como exigencia de diseño del control (T05). / El objeto es la custodia, el traslado, la reutilización y la destrucción de soportes y equipos, con borrado o destrucción verificados antes de que cambien de manos: el destino y la sanitización de los soportes es D27 y la protección del dato que contienen queda como secundaria (D06), es diseño de un control de protección (T05) y corresponde a la protección física con el retiro de equipos como referencia (PR06).

### APX-11 · Evidencia de la seguridad física de la nube y de la colocación

**Pregunta que responde.** ¿Qué evidencia tenemos de la seguridad física de los centros de datos donde están nuestros datos, y qué deja afuera?

**Tesis.** En la nube, la seguridad física y ambiental la opera un tercero y la organización solo puede conocerla por evidencia; en la colocación, el proveedor responde por el edificio, la energía y el clima, y la organización por su jaula, sus equipos y las personas que autoriza, y puede visitar la instalación. En ambos casos el CISO debe decidir qué evidencia acepta —informes de aseguramiento independientes, certificaciones con alcance verificable, derecho de auditoría o de visita—, comprobar que cubra las instalaciones donde residen sus datos y registrar lo que esa evidencia no cubre.

**Tensión.** El proveedor de nube rara vez admite inspecciones individuales y ofrece informes estandarizados cuyo alcance no siempre coincide con las regiones y los servicios contratados.

**Desarrollo.** Tomar el informe de aseguramiento de un proveedor crítico, ubicar los controles físicos y ambientales, verificar el período y las instalaciones cubiertas, y anotar las excepciones que informa el auditor y los controles que el informe deja a cargo de subproveedores o del cliente.

**Error frecuente.** Archivar el certificado sin leer su alcance ni sus excepciones.

**Producto.** Una matriz de evidencia de seguridad física por proveedor e instalación, con vigencia, alcance, excepciones y la decisión tomada sobre cada brecha.

| Eje | Coordenada |
|---|---|
| Territorio | T08 Trust & Assurance (secundarios: T05) |
| Dominio | D27 Physical, Environmental & Facility Security (secundarios: D17, D10) |
| Subfunción | GV09 Gobierno de terceros y ecosistemas (secundarios: GV08) |
| Horizonte | H02 Evolving |
| Fuerzas y mecanismos | HOM09 Assurance y validación |
| Pilar MCCS | OS Sistema operativo |
| Confianza | media |

**Por qué esa coordenada.** La tesis decide qué evidencia se acepta de la seguridad física de un tercero: es gestión de requisitos y evidencia de terceros (GV09) sobre instalaciones (D27), desde el aseguramiento (T08).

**Relación con el corpus.** Ninguna declarada.

**Afinidad temática con la base de referencia.** CSA CCM v4.1: DCS Datacenter Security; NIST SP 800-53: PE Physical and Environmental Protection; ISO/IEC 27002: controles físicos.

**Resultado de la revisión crítica.** Se corrigió: desarrollo, tensión y tesis.

**Relectura de la versión 1.3.** En subfunción, una lectura difiere y la otra sostiene el valor vigente: no cambió.

### APX-12 · El mantenimiento como vía de acceso

**Pregunta que responde.** ¿Quién entró a mantener nuestros equipos críticos el mes pasado, con qué cuenta y quién lo autorizó?

**Tesis.** Quien mantiene un equipo accede a él con privilegios y a menudo sin la vigilancia que se aplica a un usuario; el CISO debe asegurar que todo mantenimiento, presencial o remoto, esté autorizado y quede registrado, que el técnico que no tiene acceso habilitado trabaje acompañado o supervisado, que las herramientas que trae o conecta se controlen y que un equipo que sale a reparación no lleve información recuperable.

**Tensión.** El mantenimiento urgente se resuelve con atajos, como una cuenta compartida o una sesión remota que queda abierta, porque el servicio debe volver cuanto antes, y el contrato de soporte rara vez describe cómo se controla al técnico.

**Desarrollo.** Revisar las intervenciones de mantenimiento de un mes en una instalación crítica y comprobar quién autorizó cada una, con qué cuenta se hizo y qué registro quedó.

**Error frecuente.** Tratar la sesión remota del fabricante como parte del soporte y no como el acceso privilegiado de un tercero.

**Producto.** Un procedimiento de mantenimiento controlado, con autorización previa, cuentas nominales, sesión registrada y cerrada al terminar, control de las herramientas del técnico, una vía de urgencia con revisión posterior, y saneamiento de los equipos antes de que salgan de la instalación.

| Eje | Coordenada |
|---|---|
| Territorio | T05 Security Architecture (secundarios: T06) |
| Dominio | D27 Physical, Environmental & Facility Security (secundarios: D17, D05) |
| Subfunción | PR06 Resiliencia de la infraestructura y protección física y ambiental (secundarios: PR01) |
| Horizonte | H01 Foundational |
| Fuerzas y mecanismos | INH09 Limitaciones operativas, HOM08 Gobierno y supervisión |
| Pilar MCCS | DO Entrega y operación |
| Confianza | media |

**Por qué esa coordenada.** La tesis trata el mantenimiento como vía de acceso privilegiado: es protección física y mantenimiento como dependencia del control (PR06, D27), desde la operación (T06). El revisor dejó PR01 como alternativa a criterio del curador.

**Relación con el corpus.** Se relaciona con M3.1-K12 («Seguridad física, ambiental y mantenimiento como dependencias del control»).

**Afinidad temática con la base de referencia.** NIST SP 800-53: MA Maintenance; DoD CMMC: MA Maintenance; ISO/IEC 27002: controles físicos.

**Resultado de la revisión crítica.** Se corrigió: producto y tesis.

**Relectura de la versión 1.3.** Dos lecturas a ciegas coincidieron en otro valor y la coordenada cambió: territorio T06 → T05. El valor anterior queda como secundario. La tabla de arriba muestra la coordenada nueva; el texto de «Por qué esa coordenada» es anterior al cambio.

*Motivo de los lectores para el cambio de territorio.* El objeto es el mantenimiento de equipos como acceso privilegiado poco vigilado (autorización y registro, técnico acompañado, control de herramientas y saneamiento del equipo que sale a reparación): mantenimiento como dependencia del control (D27 por la regla 5) con las medidas de PR06, visto como diseño de controles sobre una frontera técnica (T05). / El objeto es el control del mantenimiento de los equipos (autorizado y registrado, técnico acompañado, herramientas controladas, equipo saneado antes de salir a reparación), es decir, el mantenimiento como dependencia del control: D27, con el acceso privilegiado del técnico o del fabricante como D05 y D17 secundarios y la subfunción PR06 que recoge el mantenimiento del hardware.

## 5. Subfunción RC05 · Comunicación de la recuperación y restitución de la confianza

### APX-13 · Informar el avance de la recuperación

**Pregunta que responde.** Durante una recuperación larga, ¿quién le dice qué a quién, y cada cuánto?

**Tesis.** Mientras dura la recuperación, las partes interesadas deciden con la información que reciben: cuándo vuelve cada servicio, qué pueden hacer mientras tanto y qué riesgos persisten; el CISO debe asegurar que el avance se comunique con una cadencia fija, por un canal previsto y a partir de una única versión de los hechos, con el detalle que corresponde a cada destinatario y distinguiendo lo confirmado de lo estimado.

**Tensión.** El equipo técnico necesita concentración y evita comprometer plazos que no controla, mientras que el negocio, los clientes y el regulador necesitan fechas para decidir; el silencio lo llenan versiones no oficiales.

**Desarrollo.** Emitir, en un ejercicio de recuperación, tres partes de avance con estado por servicio, próxima actualización y decisiones pendientes, y revisar después qué estimaciones se cumplieron.

**Error frecuente.** Comunicar solo al inicio del incidente y al cierre.

**Producto.** Una plantilla de parte de avance de la recuperación, la lista de destinatarios por tipo de servicio afectado con el nivel de detalle que recibe cada uno, la cadencia acordada y un canal alternativo si el habitual no está disponible.

| Eje | Coordenada |
|---|---|
| Territorio | T04 Risk & Resilience (secundarios: T02) |
| Dominio | D16 Business Continuity & Cyber Recovery (secundarios: D15) |
| Subfunción | RC05 Comunicación de la recuperación y restitución de la confianza (secundarios: RS03) |
| Horizonte | H01 Foundational |
| Fuerzas y mecanismos | Ninguno nombrado |
| Pilar MCCS | DO Entrega y operación |
| Confianza | media |

**Por qué esa coordenada.** La tesis pide comunicar el avance de la recuperación a las partes designadas con cadencia y versión única de los hechos: es comunicación de la recuperación (RC05) dentro de la continuidad (D16), desde el riesgo y la resiliencia (T04).

**Relación con el corpus.** Se relaciona con M5.2-K04 («Comunicación Crisis»); se relaciona con G6.1-K08 («Comunicación Crisis»).

**Afinidad temática con la base de referencia.** NIST CSF 2.0: RC.CO-03, subcategoría de RC.CO Incident Recovery Communication.

**Resultado de la revisión crítica.** Se corrigió: producto y tesis. Cambió la coordenada (mecanismos homeostáticos): El revisor señala que HOM07 (rollback y recuperación) se asignó por la palabra «recuperación» y que el texto no trata el mecanismo de reversión. Se acepta: se retira.

**Relectura de la versión 1.3.** Dos lecturas a ciegas coinciden con la coordenada en los tres ejes primarios.

### APX-15 · Restituir la confianza después del incidente

**Pregunta que responde.** Después de un incidente grave, ¿qué prometemos, a quién, y cómo demostramos que lo cumplimos?

**Tesis.** La confianza de clientes, socios, reguladores y empleados no vuelve sola con el servicio: empieza a restituirse cuando la organización explica qué ocurrió, qué cambió y cómo se puede comprobar; el CISO debe proponer a la dirección que las lecciones del incidente se conviertan en compromisos acotados, con fecha y con verificación independiente cuando el daño lo justifica, y aportar la evidencia con la que la organización rinde cuentas de su cumplimiento.

**Tensión.** El área legal busca limitar lo que se afirma, el negocio quiere cerrar el tema cuanto antes y los afectados piden detalle; prometer de más crea una nueva exposición y prometer de menos confirma la desconfianza.

**Desarrollo.** Redactar, a partir de un incidente pasado, tres compromisos verificables, acordar con la dirección y con el área legal quién los asume ante cada parte interesada, asignarles dueño y fecha, y definir cómo se informará su cumplimiento.

**Error frecuente.** Cerrar la comunicación con el aviso de que el servicio volvió.

**Producto.** Un plan de restitución de confianza aprobado por la dirección, con compromisos, dueños, fechas y forma de verificación, y los informes de cumplimiento en las fechas comprometidas.

| Eje | Coordenada |
|---|---|
| Territorio | T08 Trust & Assurance (secundarios: T03) |
| Dominio | D15 Incident Response & Crisis Management (secundarios: D01) |
| Subfunción | RC05 Comunicación de la recuperación y restitución de la confianza (secundarios: GV07) |
| Horizonte | Indeterminado: el texto no describe una fuerza de cambio que permita fijarlo |
| Fuerzas y mecanismos | HOM10 Aprendizaje organizacional |
| Pilar MCCS | DO Entrega y operación |
| Confianza | media |

**Por qué esa coordenada.** La tesis propone convertir las lecciones del incidente en compromisos verificables ante las partes interesadas: es restitución de la confianza (RC05) tras un incidente (D15), desde la confianza y el aseguramiento (T08). La restitución de la confianza es una ampliación editorial del Atlas: la categoría RC.CO de CSF 2.0 trata la comunicación de la recuperación.

**Relación con el corpus.** Ninguna declarada.

**Afinidad temática con la base de referencia.** NIST CSF 2.0: RC.CO Incident Recovery Communication.

**Resultado de la revisión crítica.** Se corrigió: desarrollo, producto y tesis. Cambió la coordenada (catalizadores, horizonte, territorios secundarios y territorio): El revisor señala que el objeto es la confianza sostenida por evidencia y verificación, que corresponde a T08, y que el texto no describe ninguna fuerza de cambio que sostenga H02 ni CAT09. Se acepta: T08 pasa a primario, T03 a secundario, el horizonte queda «indeterminado» y se retira el catalizador.

**Relectura de la versión 1.3.** Dos lecturas a ciegas coinciden con la coordenada en los tres ejes primarios.

### APX-16 · Mensajes públicos de la recuperación: aprobados, coherentes y con una sola voz

**Pregunta que responde.** ¿Lo que decimos en público sobre la recuperación coincide con lo que le informamos al regulador y a los clientes?

**Tesis.** Las actualizaciones públicas sobre la recuperación deben salir por métodos acordados de antemano y con mensajes aprobados antes de emitirse; el CISO debe lograr que la dirección designe un vocero y su suplente, que exista un circuito corto de aprobación entre seguridad, legal y comunicación y que quede registro de lo dicho, y debe asegurar que el contenido técnico del mensaje público coincida con lo que se informa al regulador y a los clientes.

**Tensión.** La rapidez que exige la comunicación pública choca con la validación técnica y legal, y distintas áreas responden a sus propios interlocutores con versiones diferentes.

**Desarrollo.** Preparar, en un simulacro, la primera actualización pública de la recuperación en un tiempo límite, hacerla pasar por el circuito de aprobación y comparar su contenido con el parte interno y con la notificación regulatoria.

**Error frecuente.** Improvisar el mensaje durante la crisis y corregirlo después en público.

**Producto.** Plantillas de mensaje por escenario y métodos de difusión acordados de antemano, el circuito de aprobación con sus suplentes, la designación del vocero y de su suplente, y el registro de las comunicaciones emitidas.

| Eje | Coordenada |
|---|---|
| Territorio | T08 Trust & Assurance (secundarios: T02, T03) |
| Dominio | D16 Business Continuity & Cyber Recovery (secundarios: D15, D03) |
| Subfunción | RC05 Comunicación de la recuperación y restitución de la confianza (secundarios: RS03) |
| Horizonte | H01 Foundational |
| Fuerzas y mecanismos | HOM08 Gobierno y supervisión |
| Pilar MCCS | DO Entrega y operación |
| Confianza | media |

**Por qué esa coordenada.** La tesis trata las actualizaciones públicas sobre la recuperación con métodos acordados y mensajes aprobados: es comunicación de la recuperación (RC05) en la gestión de incidentes (D15), desde el liderazgo y la organización (T02).

**Relación con el corpus.** Especializa M5.2-K04 («Comunicación Crisis»); especializa G6.1-K08 («Comunicación Crisis»); se relaciona con M5.2-K08 («Gestión Narrativa»); se relaciona con APC-072 («Coordinación con autoridades y pares sectoriales durante incidentes»).

**Afinidad temática con la base de referencia.** NIST CSF 2.0: RC.CO-04, subcategoría de RC.CO Incident Recovery Communication.

**Resultado de la revisión crítica.** Se corrigió: producto, tesis y título.

**Relectura de la versión 1.3.** Dos lecturas a ciegas coincidieron en otro valor y la coordenada cambió: territorio T02 → T08 y dominio D15 → D16. El valor anterior queda como secundario. La tabla de arriba muestra la coordenada nueva; el texto de «Por qué esa coordenada» es anterior al cambio.

*Motivo de los lectores para el cambio de territorio.* La tesis exige que las actualizaciones públicas sobre la recuperación salgan por métodos acordados, con mensajes aprobados, vocero designado y contenido coherente con lo informado al regulador y a los clientes: es la comunicación de la recuperación (RC05, D16) vista desde la confianza y la coherencia de lo que se dice (T08). / La tesis pide que las actualizaciones públicas sobre la recuperación salgan por métodos acordados, con mensajes aprobados, un vocero designado, registro de lo dicho y coherencia con lo informado al regulador y a los clientes: es la comunicación de la recuperación (RC05) dentro de la recuperación (D16), vista desde la confiabilidad y la transparencia ante el público (T08).

*Motivo de los lectores para el cambio de dominio.* La tesis exige que las actualizaciones públicas sobre la recuperación salgan por métodos acordados, con mensajes aprobados, vocero designado y contenido coherente con lo informado al regulador y a los clientes: es la comunicación de la recuperación (RC05, D16) vista desde la confianza y la coherencia de lo que se dice (T08). / La tesis pide que las actualizaciones públicas sobre la recuperación salgan por métodos acordados, con mensajes aprobados, un vocero designado, registro de lo dicho y coherencia con lo informado al regulador y a los clientes: es la comunicación de la recuperación (RC05) dentro de la recuperación (D16), vista desde la confiabilidad y la transparencia ante el público (T08).

## 6. Subfunción RC03 · Validación de recuperación y retorno seguro

### APX-14 · Declarar el retorno a la normalidad con criterios y evidencia

**Pregunta que responde.** ¿Quién declara que volvimos a la normalidad, con qué criterios y con qué evidencia?

**Tesis.** El fin de la recuperación no es solo un hecho técnico, sino una declaración que alguien firma sobre hechos comprobados: el CISO debe acordar de antemano qué criterios permiten afirmar que un servicio volvió a operar de forma segura —integridad verificada, accesos restablecidos y revisados, vigilancia activa, vía de entrada cerrada y ningún indicio de presencia del atacante tras una búsqueda definida— y quién tiene autoridad para declararlo ante el negocio, los clientes y el regulador.

**Tensión.** La presión por volver a operar empuja a declarar la normalidad antes de comprobarla, y una segunda caída o una reinfección después del anuncio daña la confianza más que la demora.

**Desarrollo.** Definir para un servicio crítico los criterios de retorno, la evidencia que respalda cada uno y la persona que firma, y probarlos en el próximo ejercicio.

**Error frecuente.** Dar por recuperado un servicio porque responde, sin verificar la integridad de los datos ni buscar indicios de que el atacante sigue presente.

**Producto.** Una lista de criterios de retorno por servicio crítico, el acta de declaración con su evidencia y el registro de los riesgos residuales que se comunican junto con el anuncio.

| Eje | Coordenada |
|---|---|
| Territorio | T08 Trust & Assurance (secundarios: T04) |
| Dominio | D16 Business Continuity & Cyber Recovery (secundarios: D28) |
| Subfunción | RC03 Validación de recuperación y retorno seguro (secundarios: RC05) |
| Horizonte | H01 Foundational |
| Fuerzas y mecanismos | HOM09 Assurance y validación |
| Pilar MCCS | OS Sistema operativo |
| Confianza | media |

**Por qué esa coordenada.** La tesis fija criterios comprobados y autoridad para declarar el retorno a la operación: es validación de la recuperación y retorno seguro (RC03) dentro de la continuidad (D16), desde el aseguramiento (T08).

**Relación con el corpus.** Se relaciona con M5.2-K03 («Recuperación»); se relaciona con HC-021 («Recuperación como prueba de confianza»); se relaciona con APA-104 («Verificación de copias limpias antes de la restauración»); se relaciona con APC-203 («Verificación de integridad de los activos de restauración»).

**Afinidad temática con la base de referencia.** NIST CSF 2.0: RC.RP-06, subcategoría de RC.RP Incident Recovery Plan Execution; NIST CSF 2.0: RC.CO Incident Recovery Communication.

**Resultado de la revisión crítica.** Se corrigió: error frecuente y tesis. Cambió la coordenada (subfunciones secundarias y subfunción): El revisor señala que la tesis es la declaración del fin de la recuperación con criterios y evidencia, que el Atlas ubica en RC03 (validación de recuperación y retorno seguro), donde el corpus ya tiene M5.2-K03, HC-021, APA-104 y APC-203. Se acepta: RC03 pasa a primaria y RC05 a secundaria. El pre-ensayo se había escrito para la celda RC05.

**Nota.** Se escribió para la celda RC05 y la revisión lo ubicó en RC03.

**Relectura de la versión 1.3.** En territorio, una lectura difiere y la otra sostiene el valor vigente: no cambió.

## 7. Cómo incorporarlos

1. Decidir si los cambios de la relectura quedan o se revierten (documento 14, sección 7.1). La regla RP-01 ya está adoptada y aplicada.
2. Corregir o descartar los pre-ensayos que quieras. Los cambios de la revisión crítica ya están confirmados en bloque (D-13.4).
3. Asignar a los que queden un identificador definitivo en la serie que elijas y agregarlos al banco de pre-ensayos.
4. Volver a ejecutar la unión de la categorización y la construcción del grafo: dejan de ser capa de ampliación y entran al corpus base.
5. Recién entonces considerarlos para una tanda de ensayos. Hoy no participan de la primera tanda, cuya regla exige confianza alta.

## 8. Archivos

- `data/ampliacion_celdas_en_blanco.json`: los pre-ensayos con todos sus campos, el resultado de la revisión y el motivo de cada cambio.
- `data/ampliacion_celdas_en_blanco.csv`: una fila por pre-ensayo.
- `data/relectura_1_3_por_eje.csv`: las dos lecturas a ciegas de cada pre-ensayo de la serie, eje por eje.
- `changesets/proposed/CHG-CAND-16.json`: el conjunto de cambios con que entran al grafo candidato.

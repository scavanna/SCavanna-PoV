> **Registro de la versión 1.3 (16 de noviembre de 2026).** Este documento se conserva tal como se publicó. Las cifras, los estados y los archivos que cita corresponden a esa versión. El estado vigente está en `docs/15_Decisiones_delegadas_y_relectura_1_4.md` y en los documentos 16 a 19.

# Revisión crítica y versión 1.2

> **Documento de la versión 1.2, publicado sin cambios.** Describe la revisión crítica de esa versión con las cifras de entonces. Lo que plantea como pendiente (las decisiones D-11 a D-14) tuvo respuesta del autor el 16 de noviembre de 2026, y el estado vigente está en `14_Decisiones_y_relectura_1_3.md`. Tres cosas que describe ya no son como las describe: la muestra para la revisión humana de la sección 8.5 fue reemplazada (documento 14, sección 7.3); el grafo de la sección 6.8 tenía un defecto de procedencia que se corrigió en la versión 1.3 (documento 14, sección 5); y las instrucciones del agente curador son ahora las 7.3.

**Frontier CISO Atlas 1.2** · Taxonomía 6.0 · Ontología 2.1.0 · GM-24 V7.1 · 16 de noviembre de 2026 · Estado: decisiones de diseño aceptadas por el autor en bloque y con una condición, a confirmar; contenido candidato, con revisión crítica automática de contexto independiente y sin validación humana

## 1. En una página

**Qué escribiste.** El 15 de noviembre de 2026 mandaste un mensaje con cuatro partes. Aceptaste «las decisiones propuestas», con un supuesto: que no fueran contradictorias y apuntaran a la excelencia y al rigor. Aceptaste que nada de esto tiene validación humana. Pediste, en condicional, que si hacía falta el escrutinio de un agente crítico se propusiera cómo implementar la revisión y la mejora. Y dijiste cómo entendés que funciona el Atlas: como guía, que un CISO lee sin creer nada por defecto y acepta bajo una responsabilidad final que no se delega. El mensaje está completo en la sección 2.

**Cómo se leyó.** Para poder seguir hubo que interpretar cuatro cosas, y las cuatro quedan a confirmar por vos (decisión D-14): que la aceptación vale aunque su supuesto se cumplió en parte; que las dos decisiones planteadas como preguntas (D-03 y D-10) se contestan con un «sí»; que «propone una forma de implementar […] informa y continua» autorizaba a ejecutar la revisión sin otra consulta; y que tu reflexión sobre cómo leer el Atlas puede redactarse como principio.

**Qué se hizo.** 13 revisores automáticos, cada uno con contexto propio y un encargo escrito, leyeron una copia congelada de la versión 1.1 sin ver el trabajo de los demás. Dos verificaciones externas contrastaron 35 puntos del paquete con las páginas de los organismos emisores, y una tercera, 9 citas que proponían los revisores. Cada hallazgo recibió una decisión escrita, que tomó quien había generado los artefactos. Con eso se construyó la versión 1.2, y cuatro revisores más la leyeron antes de publicarla (sección 11).

**Qué encontró.** 364 hallazgos: 2 críticos, 46 altos, 213 medios, 70 bajos y 33 observaciones. Los dos críticos eran un catálogo de agentes cargado al grafo con los campos corridos y diez decisiones de las cuales cinco no podían resolverse con un «sí».

**Qué se hizo con los hallazgos.** 163 se corrigieron, 39 se corrigieron en parte, 129 quedaron como propuestas para vos, 21 se difirieron y 12 se documentaron como límite. Todos los hallazgos críticos y altos tienen una decisión escrita: 33 corregidos, 5 corregidos en parte y 10 que esperan una decisión tuya.

**Qué cambió respecto de la versión 1.1.** `data/cambios_1_1_a_1_2.csv` tiene 183 filas: 171 son cambios de un elemento y 12 resumen cambios hechos en bloque. La Taxonomía 6.0 y la Ontología 2.1.0 conservan sus códigos. Cambiaron la coordenada de 37 pre-ensayos, el tipo de 81 conceptos de la Biblioteca, la ubicación de varios indicadores y qué vínculos se cargan al grafo.

**Qué queda en tus manos.** Cuatro decisiones, en este orden: confirmar lo que se leyó en tu mensaje (D-14), decidir las 18 reglas propuestas (D-11), confirmar o revertir lo que cambió (D-13) y decidir cómo se revisa la Biblioteca (D-12). Y la revisión humana de la categorización, para la que este documento propone una muestra de 246 pre-ensayos, una regla de decisión y un camino mínimo de 108. La sección 8 las ordena.

**Qué sigue igual.** La versión 1.2 no tiene validación humana. Sobre tu segundo párrafo: no hay una tasa de error medida. Las iteraciones anteriores no detectaron los dos errores críticos ni los 46 altos que encontró esta revisión, y la verificación de cierre encontró 139 problemas más en la versión ya corregida. Los revisores son agentes automáticos con la misma configuración que quien generó los artefactos: donde dos lecturas coinciden es menos probable un desliz, y eso no dice nada de un error que compartan. Lo único medido es cuánto coincide una lectura automática a ciegas con la coordenada vigente (sección 6.1).

## 2. Tu mensaje: qué dice, cómo se leyó y qué cubre

Tus palabras, con la ortografía normalizada. La transcripción literal está en `data/decisiones_del_autor.json`.

> «Por cuestiones de coherencia, voy a aceptar las decisiones propuestas, suponiendo que no son contradictorias y apuntan hacia la excelencia y el rigor que me caracterizan.»

> «Acepto que todo esto no tenga validación humana, pero también comprendo que las fuentes utilizadas y las diferentes iteraciones, más el modelo que estamos usando, reducen la tasa de error y la probabilidad de alucinaciones.»

> «Si es necesario someter todo al escrutinio de un agente crítico, cuyas conclusiones puedan mejorar el estado actual de lo propuesto, entonces proponé una forma de implementar la revisión crítica y la mejora posterior para obtener al final una nueva versión aún más consistente.»

> «Yo entiendo que estos niveles de abstracción son difíciles de llevar a la práctica y en consecuencia funcionan como guías y orientación. Un CISO va a tener que leer todo con atención, no creer nada por defecto y, contrastando con su conocimiento y formación, ir aceptando los distintos elementos, artefactos, recomendaciones, con la responsabilidad final indelegable. ¿Me explico? Informá y continuá.»

**Cómo se leyó cada parte.** Ninguna de estas lecturas queda firme hasta que la confirmes.

| Pasaje | Cómo se leyó | Se confirma en |
|---|---|---|
| «voy a aceptar las decisiones propuestas» | Aceptación en bloque de D-01 a D-10 y de las ADR-013 a ADR-025 que las registran. El mensaje no nombra ninguna decisión ni ninguna ADR. | D-14.1 |
| D-03 y D-10, que la versión 1.1 planteaba como preguntas | Se contestaron con un «sí» en nombre del autor y se aplicaron. | D-14.2 y D-14.3 |
| «Si es necesario […] entonces propone una forma de implementar […]. Informa y continua» | Se tomó como autorización para ejecutar la revisión y la mejora el mismo día, sin una consulta intermedia. El pedido estaba en condicional y pedía una propuesta. | D-14.5 |
| «Yo entiendo que estos niveles de abstracción […] responsabilidad final indelegable. Me explico?» | Se redactó como principio de uso (ADR-029). El autor lo enunció como una reflexión y cerró con una pregunta; no vio el texto de la ADR. | D-14.6 |

**Qué cubre la aceptación.** La aceptación cubre las decisiones de diseño. Las tareas de validación (D-07, D-09 y parte de D-03, D-08 y D-10) se registran como «aceptadas como base de trabajo, sin validar»: aceptar que algo no tiene validación humana no lo valida. Los conjuntos de cambios siguen en estado «propuesto» (ADR-019).

La revisión encontró que cinco de las diez decisiones no eran proposiciones: dos preguntaban «si» y tres pedían validar contenido que el propio paquete declaraba sin revisar. Por eso cada una se reescribió como proposición, con la opción que se tomó. La tabla trae el texto que tenía cada decisión en la versión 1.1, que es el que tuviste delante, y la proposición reescrita.

| N.º | Lo que pedía la versión 1.1 | Proposición | Opción tomada | Estado | Qué pasó en la versión 1.2 |
|---|---|---|---|---|---|
| D-01 | Aprobar el cambio de nombre y la continuidad con el AI CISO Atlas | El producto se llama Frontier CISO Atlas y continúa al AI CISO Atlas: conserva sus códigos, su arquitectura y sus decisiones anteriores. | Sí. | Aceptada; a confirmar con la advertencia a la vista (D-14.4) | La versión 1.1 pidió aprobar el nombre sin una advertencia que la revisión señaló después: «Frontier» coincide con un concepto comercial de un proveedor y con el nombre de una de sus suites, que la propia base de referencia registra. El plano A se propone agnóstico de proveedor, pero 77 de sus pre-ensayos nombran productos o al proveedor: quedaron marcados «revisar». El corpus no es neutral respecto de un proveedor. |
| D-04 | Confirmar la lectura del pilar OS en dos escalas: individual (T01) y de oficina (T03) | El pilar OS del MCCS se lee en dos escalas del mismo pilar: individual (T01) y de oficina (T03). | Sí. | Aceptada | Aplicada a la Biblioteca: 59 conceptos pasan al pilar OS. En el corpus la lectura no puede verificarse todavía, porque los pre-ensayos no registran la escala (regla propuesta RP-14). |
| D-06 | Aprobar las variables homeostáticas HV01–HV06, que son una propuesta de diseño sin respaldo normativo externo | Se adoptan las seis variables homeostáticas (HV01 a HV06) como propuesta de diseño, sin respaldo normativo externo. | Sí. | Aceptada | La definición de HV01 se precisó con la tolerancia que se deriva del apetito. El modelo de referencia no cierra en varios puntos (regla propuesta RP-15). |
| D-02 | Aprobar la Taxonomía 6.0; en particular D27, admitido con reserva, y D26, admitido por materialidad | Se adopta la Taxonomía 6.0: 8 territorios, 28 dominios, 6 funciones, 34 subfunciones y el eje H ampliado. D27 se admite con reserva y D26 por materialidad. | Sí. | Aceptada | La Taxonomía 6.0 ya contiene lo que D-03, D-04 y D-06 presentaban aparte: la regla 7, las anclas del pilar OS y las variables homeostáticas. La revisión corrigió textos y conteos y dejó 18 reglas propuestas sin aplicar (decisión D-11). |
| D-03 | Decidir si el gobierno y el riesgo de la IA alojados en D20 pasan a D01 y D02 con territorio T07. La lectura de los 71 pre-ensayos de D20 está hecha: 14 se moverían con claridad, 11 quedan a criterio del curador y 45 se quedan | El gobierno, el riesgo y el cumplimiento de la IA que estaban alojados en D20 pasan a D01, D02 o D03 (regla 7). | Interpretada como «sí». La versión 1.1 lo planteaba como pregunta y el mensaje del autor no la nombra: su aceptación en bloque se leyó como «sí, aplicar la regla». | Interpretada como «sí» y aplicada; a confirmar por el autor (D-14.2) | De los 71 pre-ensayos de D20, 26 salieron (16 a D01, 6 a D02, 2 a D17, 1 a D28, 1 a D14) y 45 quedan. De los que salieron, en 13 las dos lecturas deciden el mismo destino, en 9 la primera lo dejaba a criterio del curador y la segunda propone el destino, y 4 se adjudicaron por escrito. 22 fueron a los dominios que nombra la regla 7 y 4 a otros, por reglas de alcance distintas. En 11 de los que quedan las lecturas no coinciden: se listan para el autor (D-13.1). El territorio no se cambió en ningún caso. |
| D-05 | Aprobar la Ontología 2.1.0, que contiene a la 2.0.0 de la versión anterior y es un cambio mayor respecto de la 1.0.0 | Se adopta la Ontología 2.1.0, que contiene a la 2.0.0 y es un cambio mayor respecto de la 1.0.0. | Sí, como línea base propuesta. | Aceptada | La ontología no cambió en la versión 1.2. Lo que la revisión propone para la próxima revisión está en la solicitud OCR-CAND-03. |
| D-08 | Aceptar cómo entró la Biblioteca cognitiva al grafo candidato: tipos por categoría, territorios, cobertura por unidad y prácticas contra sesgos | La Biblioteca cognitiva entra al grafo candidato con tipos del módulo de cognición. | Sí a que entre. Los tipos, la cobertura y las prácticas contra sesgos son contenido que el paquete declaraba sin revisar: se aceptan como base de trabajo. | Aceptada como base de trabajo; modificada por la revisión | La revisión cambió el tipo de 81 conceptos, dejó de afirmar los territorios como clasificación, redujo la cobertura a 165 vínculos y las prácticas contra sesgos a 57. Lo que falta revisar por concepto es la decisión D-12. |
| D-09 | Validar qué indicadores miden cada variable homeostática y la ubicación de indicadores en PR06 y RC05 | Los indicadores asignados miden cada variable homeostática, y las subfunciones PR06 y RC05 tienen indicadores. | Aceptada como base de trabajo: un «sí» no valida el contenido. | Base de trabajo; corregida por la revisión | PR06 queda sin indicadores y RC05 conserva uno (K189). De los 71 vínculos cargados entre indicadores y variables, en 49 las dos lecturas coinciden en el vínculo y en el papel, en 14 solo en el vínculo, 5 los consideró y descartó la segunda lectura y 3 tienen una sola lectura; la segunda lectura propuso además 36 que no se cargaron. Son indicadores candidatos: ninguna variable tiene unidad, umbral ni responsable del límite. |
| D-10 | Decidir sobre las propuestas editoriales: el remapeo del GM-24 a las matrices vigentes y los 16 pre-ensayos para celdas en blanco | Se acepta la propuesta de remapeo como pedido para la próxima versión del GM-24, y los 16 pre-ensayos de la serie APX como capa de ampliación. | Interpretada como «sí» a las dos. La versión 1.1 pedía «decidir sobre las propuestas editoriales»: la aceptación en bloque se leyó como aceptarlas. | Interpretada como «sí»; la serie APX se corrigió; a confirmar por el autor (D-14.3) | El GM-24 no se modificó. La serie APX entra como capa de ampliación, fuera de las estadísticas del corpus base: 4 pre-ensayos quedaron como estaban y 12 se corrigieron. Seis de los siete alojados en D19 dependen de la regla propuesta RP-01. La propuesta de remapeo cambió después de la aceptación: los casos R2 y R4, que estaban «a revisar», tienen ahora una resolución propuesta a partir de la verificación externa. |
| D-07 | Validar la categorización y elegir la primera tanda de ensayos | La categorización de los 739 pre-ensayos es válida y la primera tanda de ensayos es la propuesta. | Aceptada como base de trabajo: un «sí» no la valida. | Base de trabajo; validación humana pendiente | Medida disponible: en una muestra a ciegas de 87 pre-ensayos, estratificada por la confianza del clasificador, el segundo lector eligió el mismo territorio en 31 de 40 casos de confianza alta, 26 de 40 de confianza media y 2 de 7 de confianza baja; el mismo dominio, en 37 de 40, 29 de 40 y 2 de 7; y la misma subfunción, en 33 de 40, 30 de 40 y 5 de 7. Ponderado para los 595 pre-ensayos del marco (el corpus sin los que estaban en D20 ni las migraciones), con su intervalo del 95 %: territorio 73 % (64–83), dominio 86 % (80–93) y subfunción 80 % (72–89). La muestra mide el acuerdo de un lector automático con la coordenada vigente, que en territorio y dominio es casi siempre la heredada. La primera tanda se recalculó después de aplicar D-03. |

### 2.1 ¿Se contradicen?

El supuesto de tu aceptación no se cumplía del todo. Aplicadas a la vez, las diez decisiones chocaban en 4 puntos: dos se resolvieron (uno con el orden de aplicación y otro con un recorte de alcance), uno se resolvió en parte y uno sigue abierto. Si apuntan a la excelencia y al rigor es un juicio tuyo, que el paquete no puede certificar.

| Entre | Qué pasaba | Qué se hizo | Estado |
|---|---|---|---|
| D-02 y D-07 | Aprobar la taxonomía y validar la categorización a la vez aprobaba una regla (la regla 7) y un corpus que no la cumplía. | D-03 se aplicó antes y D-07 quedó para el final, como base de trabajo. | Resuelto con el orden de aplicación |
| D-02 y D-08 | La regla de cardinalidad de la taxonomía admite un territorio primario y dos secundarios, y la Biblioteca entraba con hasta siete territorios por concepto. | Los territorios de la Biblioteca dejaron de afirmarse como clasificación (decisión D-12). | Resuelto con un recorte de alcance |
| D-04 y D-08 | D-04 pone la energía, la atención y la resiliencia en la escala individual del pilar OS, y D-08 cargaba los 1.404 conceptos de la Biblioteca, incluidos esos, en el pilar MM. | Se decidió D-04 primero y se escribió una regla de pilar por categoría. La regla deja en MM las habilidades socioemocionales y las mentalidades de resiliencia, que la definición del pilar OS ubica en su escala individual. | Resuelto en parte; sigue abierto en D-12.2 |
| D-03 y D-10 | La regla 7 hace prevalecer la disciplina sobre la tecnología, y seis de los siete pre-ensayos APX alojados en D19 aplican el criterio contrario. | No se resolvió: depende de la regla general RP-01 (decisión D-11). La serie APX quedó como capa de ampliación. | Abierto |

**Orden en que se aplicaron:** D-01 → D-04 y D-06 → D-02 → D-03 → D-05 → D-08 y D-09 → D-10 → D-07.

### 2.2 Lo que la aceptación no hace

- No aprueba los conjuntos de cambios del grafo: siguen en estado «propuesto», y el grafo sigue siendo candidato.
- No valida el contenido. Aceptar que algo no tiene validación humana no lo valida.
- No confirma lo que el paquete tuvo que interpretar: eso es la decisión D-14.
- No cierra las decisiones que la revisión abrió (D-11, D-12 y D-13).

## 3. Cómo leer el Atlas

Lo escribiste así:

> «Yo entiendo que estos niveles de abstracción son difíciles de llevar a la práctica y en consecuencia funcionan como guías y orientación. Un CISO va a tener que leer todo con atención, no creer nada por defecto y, contrastando con su conocimiento y formación, ir aceptando los distintos elementos, artefactos, recomendaciones, con la responsabilidad final indelegable.»

Lo redacté como principio de uso en ADR-029. Queda como propuesta hasta que lo confirmes (D-14.6): lo enunciaste como una reflexión, cerraste con una pregunta y no viste el texto de esa decisión. Para este paquete significa tres compromisos:

1. **El Atlas es una guía, no una fuente validada.** Ordena, orienta y propone. No reemplaza el juicio de quien decide.
2. **El paquete procura que cada cifra lleve el estado de su evidencia.** Donde una cifra no lo lleva, es un defecto que hay que corregir. La tabla que sigue dice, para cada componente, quién lo generó, si tuvo una segunda lectura y si tuvo revisión humana; `data/evidencia_por_preensayo.csv` lo dice para cada pre-ensayo.
3. **Nada debería presentarse como validado si no lo está.** Donde un revisor y el paquete no coinciden, el caso queda a la vista con las dos lecturas. La verificación de cierre encontró lugares donde esto no se cumplía y se corrigieron; puede haber otros.

| Componente | Quién lo generó | Segunda lectura o verificación | Revisión humana |
|---|---|---|---|
| Taxonomía 6.0: códigos, reglas y criterios | Diseño asistido, sobre la 5.3 del autor | Un revisor (82 hallazgos); 17 textos corregidos y 18 reglas propuestas sin aplicar | No |
| Base de referencia: 146 artefactos | Verificación contra las páginas de los organismos: 99 verificados, 37 en parte, 8 internos y 2 sin verificar | Segunda verificación de 35 puntos: dos registros corregidos, cinco fichas precisadas y cuatro conteos sin confirmar. Los demás registros no se releyeron | No |
| Categorización de 739 pre-ensayos: territorio, dominio y subfunción | Clasificadores automáticos, con política de migración: la mayor parte del territorio y del dominio es la coordenada heredada | 237 pre-ensayos con otra lectura, 87 de ellos a ciegas; los otros 502 tienen una sola. En la muestra a ciegas, 15 de 40 casos de confianza alta y 24 de 40 de confianza media difieren en algún eje | No |
| Horizonte, fuerzas y pilar de los pre-ensayos | Clasificadores automáticos | No | No |
| Biblioteca cognitiva: tipo de 1.404 conceptos | Regla por categoría | Lectura de 213 conceptos de categorías mixtas y una muestra de 120 de las demás, con 8 tipos equivocados; 1.071 conceptos no se leyeron | No |
| Biblioteca: territorios | Valor por categoría de la base del autor | Muestra de 100: 49 dudosos. Ya no se afirman como clasificación | No |
| Biblioteca: 57 prácticas contra sesgos | Extracción de lo que la base enuncia | Los 142 vínculos de la versión 1.1, leídos uno por uno: se cargan los que la lectura sostuvo | No |
| Indicadores: coordenada de 67 heredados sin cambios | Catálogo 1.2 del autor | No | No consta |
| Indicadores: dominio de 3 heredados, corregido | Un revisor | No: una sola lectura | No |
| Indicadores: coordenada de 154 nuevos | Un revisor | No: una sola lectura | No |
| Indicadores por variable homeostática: 71 vínculos | Propuesta de diseño | 49 coinciden en vínculo y papel, 14 solo en el vínculo, 5 descartados por la segunda lectura y 3 con una lectura | No |
| Grafo candidato: 5.058 nodos y 28.142 relaciones | Guiones deterministas | Validación estructural: 19 de 37 reglas; un revisor (64 hallazgos) | No |
| Serie APX: 16 pre-ensayos | Redactados por el asistente | Leídos enteros por un revisor; 12 con redacción corregida después, sin nueva lectura completa | No |
| Reglas propuestas y textos corregidos de la taxonomía | Escritos durante la corrección | La verificación de cierre leyó una parte | No |
| Ontología 2.1.0 | Diseño asistido, sobre la 1.0.0 del autor | Un revisor; 16 propuestas sin aplicar | No |

## 4. Cómo se hizo la revisión

**Principio.** Quien genera un artefacto no es buen revisor del mismo artefacto. Por eso los revisores trabajaron con contexto propio: recibieron una copia congelada de la versión 1.1, su encargo y un extracto de las reglas, y nada más.

**Lo que ese principio no cubre.** Quien generó los artefactos preparó también los insumos de cada revisor, adjudicó los desacuerdos entre lecturas y decidió qué hacer con cada uno de los 364 hallazgos. Ese triaje no tuvo una lectura independiente hasta la verificación de cierre, que revisó los 48 hallazgos críticos y altos y una muestra de 60 de los demás.

**Encargos.** Cada uno dice qué leer, qué buscar y qué no hacer. Están en la carpeta `revision_critica/` del paquete, junto con lo que cada revisor entregó.

| Revisor | Encargo | Hallazgos | Corregido | Corregido en parte | Propuesta al autor | Diferido | Documentado |
|---|---|---|---|---|---|---|---|
| C1 | Consistencia entre documentos y datos | 42 | 41 | — | — | — | 1 |
| C2 | Taxonomía y decisiones | 82 | 28 | 10 | 43 | — | 1 |
| C3 | Ontología y grafo | 64 | 39 | 11 | 10 | 2 | 2 |
| C4a | Segunda lectura de D20 | 13 | 2 | 1 | 9 | — | 1 |
| C4b | Segunda lectura de las migraciones | 17 | — | — | 16 | — | 1 |
| C4c | Muestra a ciegas del corpus | 19 | — | — | 18 | — | 1 |
| C5a | Biblioteca: tipos y pilar | 15 | 5 | 3 | 7 | — | — |
| C5b | Biblioteca: prácticas contra sesgos y territorios | 17 | 13 | — | 4 | — | — |
| C5c | Biblioteca: duplicados y equivalencias | 9 | 2 | 1 | 4 | — | 2 |
| C6a | Medición: indicadores y variables homeostáticas | 19 | — | 2 | — | 17 | — |
| C6b | Medición: territorio y dominio de los indicadores | 14 | 3 | 3 | 7 | — | 1 |
| C6c | Medición: subfunción de los indicadores | 11 | 2 | 1 | 7 | — | 1 |
| C8 | Lectura escéptica de un CISO y serie APX | 42 | 28 | 7 | 4 | 2 | 1 |

**Segundas lecturas del corpus.** Fueron cuatro, y solo una fue a ciegas.

- **D20.** En los 71 pre-ensayos que estaban en D20, el revisor sabía que estaban en ese dominio y conocía su territorio y su subfunción. No conocía la primera lectura.
- **Migraciones.** En las 73 migraciones a dominios nuevos, el revisor conocía el dominio 5.3, sabía que todos los casos habían migrado y elegía entre ese dominio y los dominios nuevos. La coincidencia que resultó hay que leerla con esa ayuda.
- **Muestra a ciegas.** 87 pre-ensayos clasificados desde cero, sin ninguna coordenada a la vista: 47 en la revisión y 40 más, de confianza media, en la verificación de cierre.
- **Sugerencias.** En 7 pre-ensayos, un segundo lector tuvo a la vista la coordenada vigente y la sugerencia del clasificador, y respondió si la aceptaba. Es una confirmación, no una segunda lectura independiente.

En total, 237 de los 739 pre-ensayos tienen alguna lectura además de la del clasificador, y 502 tienen una sola. El detalle por pre-ensayo está en `data/evidencia_por_preensayo.csv`.

**Verificación externa.** Tres informes contra las páginas de los organismos emisores. Los dos primeros contrastaron 35 puntos del paquete: 9 sobre MITRE ATT&CK, MITRE ATLAS y CSA CCM (6 afirmaciones y 3 preguntas abiertas) y 26 afirmaciones sobre otras normas y marcos. El tercero verificó 9 citas que proponían los revisores: confirmó ocho citas de subcategorías de NIST CSF 2.0 y las definiciones de apetito y de tolerancia de NIST IR 8286r1; la atribución de esas definiciones a ISO no se pudo confirmar. Están en el anexo A7. Sus puntos no se cuentan entre los 364 hallazgos, que son todos de los 13 revisores.

**Reglas para decidir, tal como se aplicaron.**

- Una coordenada heredada del corpus cambia cuando dos lecturas coinciden o cuando una adjudicación escrita se apoya en la tesis del texto y en una regla explícita. De los 37 cambios del corpus, en 13 las dos lecturas deciden lo mismo, en 9 la primera lectura lo dejaba a criterio del curador y la segunda propone el destino, 7 son sugerencias confirmadas por un lector que las conocía y 8 se adjudicaron por escrito. Solo el primer grupo cumple la regla en su forma estricta.
- Fuera del corpus la regla no se aplicó así: en la Biblioteca, la medición y la serie APX, 97 filas de cambios descansan en una sola lectura y están rotuladas. K50, K51 y K60, por ejemplo, cambiaron de dominio con una lectura. La razón es que en esos componentes no había una coordenada heredada del autor que proteger, o la regla anterior era del propio paquete. El costo es que esos cambios tienen menos respaldo, y por eso son los primeros que conviene mirar en la decisión D-13.
- Si las lecturas no coinciden y no hay regla que decida, la coordenada queda como estaba y el caso se informa con las dos lecturas.
- Lo que la revisión propone sobre reglas de la taxonomía no se aplica: se escribe y lo decidís vos.
- Las fuentes del autor (el GM-24, el banco de pre-ensayos, la base de la Biblioteca y el catálogo CISO 365) no se modifican.
- Todo hallazgo crítico o alto recibe una decisión escrita.

## 5. Qué encontró

| Severidad | Hallazgos | Corregido | Corregido en parte | Propuesta al autor | Diferido | Documentado |
|---|---|---|---|---|---|---|
| Crítica | 2 | 2 | — | — | — | — |
| Alta | 46 | 31 | 5 | 10 | — | — |
| Media | 213 | 77 | 28 | 91 | 12 | 5 |
| Baja | 70 | 46 | 3 | 20 | — | 1 |
| Observación | 33 | 7 | 3 | 8 | 9 | 6 |
| **Total** | 364 | 163 | 39 | 129 | 21 | 12 |

Las cinco decisiones posibles: **corregido**; **corregido en parte**, cuando se corrigió lo que podía corregirse sin decidir por vos; **propuesta al autor**, cuando el hallazgo pide una regla o un cambio que te corresponde; **diferido**, cuando toca una fuente tuya que este paquete no modifica o queda para un trabajo posterior que se nombra; y **documentado**, cuando es un límite que se declara. «Diferido» no tiene fecha: quiere decir que se te remite.

### 5.1 Los dos hallazgos críticos

**C2-055 · Taxonomía y decisiones.** Cinco de las diez decisiones no son proposiciones que se resuelvan con un «sí»: D-03 y D-10 preguntan «si», y D-07, D-09 y parte de D-08 piden validar contenido que el propio paquete declara sin revisar. Una aceptación en bloque no les da resultado, y ADR-019 y las reglas del grafo impiden leerla como aprobación del contenido.

*Qué se hizo.* Las diez decisiones se reformularon como proposiciones con la opción tomada, separadas en decisiones de diseño y tareas de validación (aceptadas como base de trabajo, sin validar). Las dos que la versión 1.1 planteaba como preguntas (D-03 y D-10) se registran como interpretadas y aplicadas, a confirmar por el autor en la decisión D-14. Se publican el texto original de cada decisión, sus dependencias y el orden en que se aplicaron. Se ve en: docs/01, 08 y 13; data/decisiones_del_autor.json.

**C3-001 · Ontología y grafo.** Los 85 registros de agentes del plano B tienen las claves corridas dos posiciones y el grafo carga cada dato con otro nombre. Los 85 nodos ApprovalGate no son puntos de control humano sino categorías de costo, y se pierden la autonomía de los agentes, sus riesgos OWASP, sus dueños y las herramientas de 70 agentes.

*Qué se hizo.* Se corrigió la correspondencia de campos de los 85 agentes en el extracto del GM-24 (835 campos comprobados contra los anexos, sin diferencias) y se rehízo la carga: los puntos de control son ahora los que declara cada anexo. Se ve en: scripts/corregir_extracto_agentes.py; graph.

### 5.2 Los hallazgos altos

| Hallazgo | Qué se encontró | Decisión | Qué se hizo |
|---|---|---|---|
| C1-001 | El documento afirma dos veces que «cada fuerza presiona al menos una» variable homeostática, pero 5 de las 22 fuerzas del catálogo (CAT08, INH02, INH04, INH05 e INH10) no presionan ninguna. La frase es texto fijo de los guiones y contradice la tabla de la misma sección y el grafo. | Corregido | La frase pasa a «17 de las 22 fuerzas presionan al menos una variable» y nombra las cinco que no. El modelo de referencia no se completó: queda en la regla propuesta RP-15. |
| C1-013 | El catálogo de 85 agentes del plano B entró al grafo con las columnas corridas. Los 85 nodos ApprovalGate, que deberían ser puntos de control humano, llevan valores de costo («Bajo», «Tokens», «Tokens/SCU», «Medio»). La pregunta P13, publicada como respondible, devuelve esos costos en la columna «punto_de_control». | Corregido | Se corrigió la correspondencia de campos de los 85 agentes en el extracto del GM-24 (835 campos comprobados contra los anexos, sin diferencias) y se rehízo la carga: los puntos de control son ahora los que declara cada anexo. |
| C1-031 | El resultado «0 errores y 0 advertencias» se presenta como validación contra la ontología 2.1.0, pero el validador evalúa 13 de las 37 reglas. Una de las reglas de nivel error que no evalúa, SV-003, exige descripción en todo nodo, y 1.809 de los 5.041 nodos no la tienen. | Corregido | El validador comprueba ahora 19 de las 37 reglas, entre ellas SV-003 y SV-112, más una comprobación propia del paquete (PAQ-01), y la lista de comprobadas y no comprobadas se publica. El README y los documentos dicen que la validación es estructural. |
| C1-040 | El paquete afirma que cada vínculo entre el corpus y un marco declara contra qué versión del artefacto se hizo. En el grafo, las 7.559 aristas del mapeo del GM-24 llevan en esa propiedad un mismo texto genérico que no nombra ninguna versión, y apuntan a elementos rotulados con la versión vigente hoy, no con la del mapeo. | Corregido | Cada mapeo declara la versión contra la que el GM-24 dice haberlo hecho, o que el GM-24 no la declara; cada elemento de marco guarda la versión de la que procede su código y su nombre. |
| C2-001 | El criterio C2 se aplicó con dos varas: W02 se rechaza porque su objeto «es una función (ID01, PR04) que cruza dominios», pero D28 se admite aunque el propio texto lo describe como una perspectiva (T08) más una función (GV08), y D25 aunque ya existían T05 y PR03 «arquitectura segura». W02 tiene más respaldo externo que tres de los cuatro dominios admitidos y 16 pre-ensayos de inventario, por encima del umbral de C3. | Propuesta al autor | Regla propuesta RP-16 (criterios de admisión de dominios). No se aplicó. |
| C2-008 | C5 pide una regla de precedencia «frente a cada dominio vecino», pero la de D28 solo nombra a D03, D02 y D22, cuando sus 54 migraciones llegaron desde 13 dominios. El resultado es desparejo: objetos casi idénticos quedaron a un lado y al otro de la frontera. | Propuesta al autor | Regla propuesta RP-02 (cláusula de pilar y fronteras de D28). No se aplicó. |
| C2-016 | El eje Y mezcla dominios de disciplina (gobierno, riesgo, monitoreo, respuesta, aseguramiento) con dominios de objeto o tecnología (identidad, datos, nube, IoT, IA), y no hay una regla general que diga cuál manda cuando un tema es una disciplina aplicada a un objeto. Las reglas parciales resuelven casos equivalentes en sentidos opuestos. | Propuesta al autor | Regla propuesta RP-01 (precedencia general entre disciplina y objeto). No se aplicó: cambia el alojamiento de pre-ensayos y necesita la decisión del autor. |
| C2-021 | Los ajustes de alcance que D-02 aprueba no se aplicaron al corpus y, salvo el que toca a D20, no tienen una decisión que ordene aplicarlos. La columna «Corpus 6.0» cuenta códigos de la 6.0 con el alojamiento de la 5.3, de modo que no mide los alcances ajustados. | Propuesta al autor | Regla propuesta RP-18 (fronteras y alcances heredados). No se aplicó. La columna del documento 07 pasa a llamarse «Corpus 6.0 (códigos 6.0, alojamiento heredado)»: solo D20 tuvo una lectura completa. |
| C2-026 | RC04 es una subfunción de Recuperar cuya única categoría de CSF 2.0 es ID.IM, que pertenece a Identificar. Por eso el Atlas cuenta como recuperación contenido de mejora continua y de auditoría, y mide el mismo objeto con dos funciones distintas. | Propuesta al autor | Regla propuesta RP-13 (RC04 bajo la función Recuperar). No se aplicó. |
| C2-033 | La afirmación de que «cada fuerza presiona al menos una» variable es falsa: cinco de las 22 fuerzas no presionan ninguna (CAT08, INH02, INH04, INH05 e INH10). Entre ellas está INH04, el segundo inhibidor más usado del corpus. | Corregido | La frase pasa a «17 de las 22 fuerzas presionan al menos una variable» y nombra las cinco que no. El modelo de referencia no se completó: queda en la regla propuesta RP-15. |
| C2-042 | Las anclas de los pilares no describen dónde está cada pilar en el corpus: los territorios de ancla primaria reúnen 14,6 % de MM, 10,4 % de OS, 33,3 % de DO y 15,0 % de NX. El glosario define ancla como el territorio donde el pilar «tiene su asiento principal». | Corregido en parte | Las anclas de los pilares se declaran como hipótesis de diseño y se publica su medición en el corpus. Si deben derivarse de la definición del pilar lo decide el autor (RP-14). |
| C2-043 | La lectura de OS en dos escalas que D-04 pide confirmar no puede verificarse con el corpus: no existe un atributo de escala, la escala individual tiene dos pre-ensayos, y la de oficina se clasificó con una definición distinta de la del catálogo, que la vuelve casi equivalente a la función Gobernar. | Propuesta al autor | Regla propuesta RP-14 (anclas del MCCS y escala del pilar OS). No se aplicó. |
| C2-044 | D-04 y D-08 se contradicen si se aceptan juntas: D-04 pone la energía, la atención y la resiliencia en la escala individual del pilar OS, y D-08 carga los 1.404 conceptos de la Biblioteca, incluidos los de atención, fatiga y resiliencia, con el pilar MM. | Corregido en parte | La lectura de OS en dos escalas se aplicó a la Biblioteca con una regla por categoría: las funciones ejecutivas y los factores humanos que son estados o condiciones van al pilar OS (59 conceptos); los demás quedan en MM. Por ser una regla por categoría, las habilidades socioemocionales y las mentalidades de resiliencia siguen en MM: el choque entre D-04 y D-08 queda abierto para ellas (decisión D-12.2). La corrección del ancla de HumanCapability en el diccionario se pide en OCR-CAND-03. |
| C2-056 | D-02 ya contiene lo que D-03, D-04 y D-06 presentan como decisiones aparte: la Taxonomía 6.0 incluye la regla 7 y los alcances de D01 y D02, las anclas de OS en T01 y T03, y las seis variables homeostáticas. Aprobar D-02 tal como está resuelve las otras tres, y resolver cualquiera de ellas en sentido contrario obliga a cambiar la taxonomía. | Corregido | Las diez decisiones se reformularon como proposiciones con la opción tomada, separadas en decisiones de diseño y tareas de validación (aceptadas como base de trabajo, sin validar). Las dos que la versión 1.1 planteaba como preguntas (D-03 y D-10) se registran como interpretadas y aplicadas, a confirmar por el autor en la decisión D-14. Se publican el texto original de cada decisión, sus dependencias y el orden en que se aplicaron. |
| C2-057 | Validar la categorización (D-07) junto con la taxonomía (D-02) aprueba a la vez una regla y un corpus que la incumple: 14 pre-ensayos de D20 son, según la lectura del propio paquete, gobierno o riesgo de la IA, y otros 16 del mismo tema ya están en D01, D02 o D03 con T07. La primera tanda de ensayos depende de esa decisión. | Corregido | Orden aplicado: D-01; D-04 y D-06; D-02; D-03; D-05; D-08 y D-09; D-10; D-07 al final. D-03 se aplicó antes de fijar la categorización y la primera tanda. |
| C2-058 | Si D-03 se resuelve como manda la regla 7 (la disciplina prevalece sobre la tecnología), seis de los siete pre-ensayos que D-10 propone para D19 aplican el criterio contrario: alojan en el dominio de la tecnología el inventario, la compra, el parcheo, el monitoreo, la respuesta y el modelado de amenazas de los dispositivos conectados. | Propuesta al autor | Regla propuesta RP-01 (precedencia general entre disciplina y objeto). No se aplicó: cambia el alojamiento de pre-ensayos y necesita la decisión del autor. Los pre-ensayos APX quedan como capa de ampliación, fuera de las estadísticas del corpus base, hasta que se decida la regla. |
| C2-059 | Las diez decisiones se presentan como una lista plana, pero tienen dependencias de orden que ningún documento declara para ellas: D-08 depende de D-04 y D-05; D-09, de D-02, D-05 y D-06; D-07, de D-02, D-03, D-04 y D-10; y D-02, de D-04 y D-06. El paquete solo ordena los requisitos R1 a R12 del grafo. | Corregido | Orden aplicado: D-01; D-04 y D-06; D-02; D-03; D-05; D-08 y D-09; D-10; D-07 al final. D-03 se aplicó antes de fijar la categorización y la primera tanda. |
| C2-076 | ADR-016 afirma que el plano A sigue siendo agnóstico de proveedor y docs/02 que los productos aparecen solo en el plano B, pero los 739 pre-ensayos están clasificados en el plano A y al menos 53 nombran productos de Microsoft, tres de ellos en el título. | Corregido | Se detectan los nombres de producto y de proveedor en el plano A: 77 pre-ensayos (72 nombran productos y 5 solo al proveedor) quedan marcados «revisar» y el paquete lo informa como advertencia de una comprobación propia (PAQ-01), que no es una de las 37 reglas de la ontología. Los documentos dicen que el plano A se propone agnóstico de proveedor y que el corpus no lo es. Si esos pre-ensayos pasan al plano B lo decide el autor (RP-17). |
| C3-002 | La regla SV-112 (autonomía L2 o superior con punto de control o justificación) nunca se pone a prueba. El guion inserta en cada tarea L2 o L3 la misma justificación genérica y la validación la acepta; ninguna tarea tiene una compuerta propia y siete tareas L2 no tienen agente que las ejecute. | Corregido | La regla SV-112 se comprueba con los puntos de control que declaran los agentes, sin justificación automática: 92 asignaciones de nivel L2 o superior a agentes y 132 tareas tienen punto de control; 7 tareas no tienen agente ejecutor y lo dicen. |
| C3-003 | De las 37 reglas de semantic_rules.json el guion comprueba 13, una de ellas solo en parte, y 24 se declaran sin comprobarse. La frase «valida contra la ontología 2.1.0 con 0 errores» y el estado «passed» de las 15 cabeceras solo valen para ese subconjunto. | Corregido | El validador comprueba ahora 19 de las 37 reglas, entre ellas SV-003 y SV-112, más una comprobación propia del paquete (PAQ-01), y la lista de comprobadas y no comprobadas se publica. El README y los documentos dicen que la validación es estructural. |
| C3-004 | La regla SV-003, de severidad error, y los 84 tipos exigen descripción, pero 1.809 de los 5.041 nodos (35,9 %) tienen la definición vacía, entre ellos los 379 conceptos del GM-24, las 595 preguntas y los 468 elementos de marco. El resultado publicado de 0 errores no lo refleja porque SV-003 no se comprueba. | Corregido | Los 5.058 nodos tienen definición, tomada de la fuente cuando existe, y SV-003 se comprueba. |
| C3-005 | SV-113 exige la versión del artefacto en cada MAPS_TO, pero 7.628 de las 8.422 aristas (90,6 %) llevan un texto que no es una versión. La validación solo comprueba que el campo no esté vacío, de modo que la regla se cumple de nombre y el mapeo no dice contra qué versión de cada marco se hizo. | Corregido | Cada mapeo declara la versión contra la que el GM-24 dice haberlo hecho, o que el GM-24 no la declara; cada elemento de marco guarda la versión de la que procede su código y su nombre. |
| C3-006 | El estado de cada pregunta de competencia es una constante escrita en el guion y no el resultado de una prueba. Ninguna consulta tiene criterio de aceptación: una que devolviera cero filas o datos erróneos se publicaría igual como «Respondible», y eso ocurre con P13. | Corregido | El estado de cada pregunta de competencia se deriva de un criterio: si puede expresarse con la ontología, la cobertura de la consulta sobre su universo y el límite declarado. Resultado: 7 respondibles, 9 en parte y 6 todavía no (sobre las 20 originales: 6, 8 y 6). |
| C3-007 | Las notas de las preguntas sin respuesta citan relaciones y tipos que no sirven o no existen, y tres preguntas (P02, P05 y P08) no pueden expresarse con la ontología aunque se carguen instancias. La conclusión de que solo faltan datos de una organización y de que el Atlas sirve como vocabulario para las preguntas 1 a 5 no se sostiene. | Corregido | Las notas de P01 a P06 usan tipos y relaciones del diccionario. P02 y P05 se declaran no expresables con la ontología 2.1.0, y la relación que falta queda pedida en OCR-CAND-03. |
| C3-008 | Las operaciones UPSERT_NODE no incluyen la definición del nodo. Los conjuntos de cambios, que son la unidad que se revisa, se firma con SHA-256 y se aprueba, no alcanzan para reconstruir el grafo: 3.232 definiciones quedan fuera de la huella y de la aprobación. | Corregido | Las operaciones llevan definición, versión y estado del nodo e identificador estable de arista; una prueba rearma el grafo solo con los archivos de operaciones y lo compara. |
| C4a-001 | La política de migración solo admite cambios causados por un dominio nuevo o una subfunción nueva, y la ficha de D20 dice que su aclaración no cambia la frontera, pero la regla 7 y los ajustes de D01 y D02 sacan de D20 el gobierno y el riesgo de la IA hacia dominios que no son nuevos. Con los tres textos vigentes a la vez no se puede saber si los casos de gobierno que hoy están en D20 deben moverse. | Corregido | La política de migración admite los ajustes de alcance de la Taxonomía 6.0 y una vía de corrección (ADR-028, que rige de forma provisoria). Se aplicaron las siete sugerencias del clasificador que un segundo lector, que las tenía a la vista, confirmó: es una confirmación, no una segunda lectura independiente. |
| C4a-002 | Los 11 pre-ensayos de D20 con territorio T08 tratan de evidencia, pruebas, umbrales, auditoría, monitoreo o reevaluación de sistemas de IA. En 8 de ellos el objeto es el método para demostrar o medir, que corresponde a D28, pero todos siguen en D20. D28 es nuevo en 6.0, de modo que la política de migración sí admite ese cambio. La regla 6 solo resuelve el caso de la IA como instrumento de prueba (D22) y no dice qué corresponde cuando la IA es el objeto probado. | Propuesta al autor | Los pre-ensayos de D20 con territorio T08 no se movieron donde las lecturas no coinciden: quedan listados para el autor, con las dos lecturas (decisión D-13 y regla RP-02). |
| C4a-003 | No hay regla de precedencia entre D20 y los dominios de disciplina cuando una disciplina se aplica a un objeto de IA y la ficha de esa disciplina no nombra la IA. La 6.0 lo resuelve para identidades (D05), observabilidad (D14) y cadena de suministro (D17), pero no para inventario (D13), amenazas (D12), ciclo de vida y cambios (D11), detención y reversión (D15 y D16) ni autorización (D05). El resultado es incoherente: el inventario general iría a D13 y el inventario de agentes de la misma unidad quedaría en D20. | Propuesta al autor | Regla propuesta RP-01 (precedencia general entre disciplina y objeto). No se aplicó: cambia el alojamiento de pre-ensayos y necesita la decisión del autor. |
| C4a-010 | Cuatro errores de clasificación que el propio clasificador llamó evidentes siguen sin corregirse. La política de migración conserva la coordenada 5.3 salvo cambios causados por el catálogo 6.0 y no prevé una vía para corregir errores, de modo que el paquete mantiene coordenadas que contradicen la tesis. | Corregido | La política de migración admite los ajustes de alcance de la Taxonomía 6.0 y una vía de corrección (ADR-028, que rige de forma provisoria). Se aplicaron las siete sugerencias del clasificador que un segundo lector, que las tenía a la vista, confirmó: es una confirmación, no una segunda lectura independiente. |
| C4b-001 | La regla 6 no tiene la cláusula de pilar que sí tiene la regla 3: solo enumera tres excepciones (D03, D02 y D22). No decide si la auditoría, la prueba o la métrica de un dominio concreto migra a D28 o queda en ese dominio, y es la frontera que más ítems del lote afecta. | Propuesta al autor | Regla propuesta RP-02 (cláusula de pilar y fronteras de D28). No se aplicó. |
| C5a-001 | La Biblioteca contiene el mismo concepto en más de una categoría, y la regla por categoría le da a cada copia un tipo distinto. Encontré 30 grupos que suman 70 conceptos, sin búsqueda exhaustiva; en 18 la definición es casi idéntica. | Corregido en parte | Se unificó el tipo en siete conceptos de grupos con definición casi idéntica; los demás grupos se publican para que el autor decida si los fusiona (decisión D-12). |
| C5a-002 | Los 172 conceptos que la regla dejó como Concept no son un residuo homogéneo: leyendo nombre y definición, 71 corresponden a un tipo específico. Las cifras publicadas por tipo cambian en los cinco tipos. | Corregido | Se aplicaron los veredictos de tipo de confianza alta o media (66 conceptos) y las ocho excepciones de la muestra; los cinco de confianza baja quedan como estaban. |
| C5a-004 | Los 1.404 conceptos llevan el pilar MM, incluidos los 388 HumanCapability, pero el diccionario de entidades del propio paquete ancla HumanCapability en el pilar OS a escala individual. Con la lectura de OS en dos escalas ya aceptada, cerca de 270 conceptos corresponden a otro pilar y el pilar OS queda vacío para la Biblioteca. | Corregido en parte | La lectura de OS en dos escalas se aplicó a la Biblioteca con una regla por categoría: las funciones ejecutivas y los factores humanos que son estados o condiciones van al pilar OS (59 conceptos); los demás quedan en MM. Por ser una regla por categoría, las habilidades socioemocionales y las mentalidades de resiliencia siguen en MM: el choque entre D-04 y D-08 queda abierto para ellas (decisión D-12.2). La corrección del ancla de HumanCapability en el diccionario se pide en OCR-CAND-03. |
| C5b-001 | De los 142 vínculos «la práctica contrarresta el sesgo», leídos uno por uno, 57 se sostienen, 77 son débiles y 8 son incorrectos. La tabla de prácticas con más sesgos asociados cambia de orden cuando se cuentan solo los vínculos que se sostienen. | Corregido | Se cargan solo los 57 vínculos que la segunda lectura juzgó sostenibles; los 77 débiles y los 8 incorrectos quedan en el CSV, con su motivo. El emparejamiento por nombres contenidos se corrigió. |
| C5b-002 | El emparejamiento cuenta dos veces el texto «checklist de desesgo»: lo vincula con la práctica que nombra (DP-0016) y además con «Listas de verificación» (DP-0064), porque el alias «checklist» está contenido en ese nombre. Los seis vínculos con DP-0064 atribuyen a la base algo que no dice. | Corregido | Se cargan solo los 57 vínculos que la segunda lectura juzgó sostenibles; los 77 débiles y los 8 incorrectos quedan en el CSV, con su motivo. El emparejamiento por nombres contenidos se corrigió. |
| C5b-012 | Los territorios de la Biblioteca no se asignaron por concepto sino por categoría: cada categoría tiene un valor por defecto y el concepto lo hereda. Eso contradice la regla 1 (se clasifica por el objeto y la tesis). En la muestra de 100 conceptos, 49 asignaciones son dudosas. Las cifras por territorio describen la composición por categorías de la Biblioteca. | Corregido | Los territorios de la Biblioteca no se cargan como clasificación: quedan como propiedad del nodo y en el CSV, rotulados como valor por categoría de la base. Derivarlos por concepto es la decisión D-12. |
| C5b-013 | Hay 97 conceptos con más de tres territorios, 45 de ellos con siete de los ocho. La regla 2 admite un primario y hasta dos secundarios. La cantidad de territorios depende de la prioridad editorial y no del concepto, de modo que los conceptos más importantes son los que el eje X menos distingue. | Corregido | Los territorios de la Biblioteca no se cargan como clasificación: quedan como propiedad del nodo y en el CSV, rotulados como valor por categoría de la base. Derivarlos por concepto es la decisión D-12. |
| C5b-014 | El criterio «primario solo cuando la base declara un único territorio» da un resultado contrario a la lente que el mismo conjunto de cambios asigna. Los 1.404 conceptos llevan el pilar MM, cuya ancla primaria es T01, pero el mayor territorio primario de la Biblioteca resulta T03, y ningún sesgo tiene primario. | Corregido | Los territorios de la Biblioteca no se cargan como clasificación: quedan como propiedad del nodo y en el CSV, rotulados como valor por categoría de la base. Derivarlos por concepto es la decisión D-12. |
| C6b-001 | Ninguno de los 64 indicadores con coordenada usa un dominio nuevo de la 6.0, aunque la política de migración manda cambiar la coordenada cuando el cambio lo causa un dominio nuevo. K60 mide la prueba de efectividad de los controles, que por la regla 6 es D28, y sigue en D03 con la nota «vigente en 6.0». | Corregido en parte | K60 pasa a D28 con D03 como secundario. La revisión de K59, K43 y K54 queda para el autor (decisión D-13). Ninguno de los otros 69 indicadores heredados usa un dominio nuevo de la 6.0: no tuvieron una lectura de migración. |
| C6c-001 | Los cuatro indicadores ubicados en PR06 miden controles de acceso y de segmentación de red, no resiliencia de la infraestructura ni protección física o ambiental; se ubicaron por una regla mecánica (PR.IR lleva a PR06 salvo en la función GES-M3.1) que contradice la ubicación de esos mismos objetos en el corpus. Ubicados por objeto van a PR03, PR06 queda sin indicadores y dejan de sostenerse la afirmación de que las 34 subfunciones tienen indicador y el descarte de crear indicadores para PR06. | Corregido | PR06 queda sin indicadores: K36 vuelve a PR03 y K159, K160 y K193 se ubican en PR03. Dos revisores coincidieron por separado. |
| C6c-002 | La regla documentada dice que un indicador nuevo recibe subfunción solo cuando su categoría de CSF corresponde a una sola subfunción, pero el script también la asigna cuando corresponde a varias: toma la única de la misma función cuyo primer vínculo es esa categoría. Por eso 41 de los 89 indicadores con subfunción automática son de categorías con más de una subfunción, y las cifras publicadas (153 con subfunción y 71 solo con función) no salen de la regla documentada. | Corregido | ADR-024 y el documento 06 describen la regla que el guion aplica. La subfunción derivada de la categoría de CSF sin lectura del indicador queda rotulada como tal, con confianza baja. |
| C8-001 | El resumen dice que «el corpus está cargado hacia la ejecución» porque el pilar DO reúne 65,9 %, pero por función la mitad del corpus es gobierno y la operación es lo menos desarrollado. El pilar DO funciona como categoría residual y el rótulo «ejecución» lleva a la conclusión contraria a la que dan los ejes del propio Atlas. | Corregido | El resumen informa el corpus por función: la mitad es gobierno y la operación es lo menos desarrollado. Las proporciones por pilar se dan sin decimales y con su reserva. |
| C8-003 | La cifra de 883 conceptos de la Biblioteca con territorio T01 se compara con los 9 pre-ensayos de T01, pero los 9 llevan T01 como territorio primario y los 883 lo llevan en cualquier posición. Además, el 92 % de esos conceptos tiene la prioridad más baja de la propia base y más de la mitad es una lista de sesgos y falacias. | Corregido | Se retira la comparación de 9 con 883. Los territorios de la Biblioteca son un valor por categoría de la base y ya no se afirman como clasificación; el documento da las cifras con su papel (315 con T01 como único territorio y 568 con T01 entre varios). |
| C8-004 | El documento afirma que los productos aparecen solo en el plano B, pero 65 pre-ensayos del corpus académico nombran productos de un único proveedor. Ninguno está marcado para revisión de la edición pública. | Corregido | Se detectan los nombres de producto y de proveedor en el plano A: 77 pre-ensayos (72 nombran productos y 5 solo al proveedor) quedan marcados «revisar» y el paquete lo informa como advertencia de una comprobación propia (PAQ-01), que no es una de las 37 reglas de la ontología. Los documentos dicen que el plano A se propone agnóstico de proveedor y que el corpus no lo es. Si esos pre-ensayos pasan al plano B lo decide el autor (RP-17). |
| C8-005 | La muestra de control casi no mide la asignación de territorio y dominio: en 45 de 48 casos el clasificador recibió el valor vigente con la instrucción de conservarlo y solo decidió si migraba a un dominio nuevo. La confianza declarada, que ordena la revisión del curador y filtra la primera tanda, es el dato menos fiable del método. | Corregido | La muestra de control ya no se presenta como medida de reproducibilidad. La medida es la muestra a ciegas, que la verificación de cierre completó con un estrato de confianza media: 87 pre-ensayos en tres estratos, informados por estrato y con su intervalo, con una estimación ponderada para los 595 pre-ensayos del marco. Los documentos dicen qué mide: el acuerdo de un lector automático con la coordenada vigente. |
| C8-006 | El único ejemplo de uso del Atlas no se reproduce con el corpus: la coordenada que propone no devuelve ningún pre-ensayo y el pre-ensayo que trata ese mismo caso está clasificado en otro territorio y otro dominio. La navegación por coordenada no fue probada. | Corregido | El ejemplo de uso se rehízo con una coordenada que el corpus resuelve y se agregaron casos de navegación con lo que devuelve cada uno. |

Los 316 hallazgos restantes están en `data/revision_critica_hallazgos.csv`, cada uno con su decisión, la acción y dónde se ve.

## 6. Lo que la revisión midió

### 6.1 Cuánto coincide una lectura a ciegas con la coordenada vigente

**Qué mide.** El acuerdo entre una lectura automática a ciegas y la coordenada de la versión 1.1. En territorio y en dominio esa coordenada es casi siempre la heredada de la Taxonomía 5.3, que la política de migración mandaba conservar: la muestra mide sobre todo cuánto coincide un lector automático con la coordenada heredada, y no la reproducibilidad del método de clasificación. No es una revisión humana.

**Cómo se eligió.** Es una muestra estratificada sobre los 595 pre-ensayos que en la versión 1.1 no estaban en D20 ni eran migraciones a un dominio nuevo; esos 144 tuvieron su propia segunda lectura, que no fue a ciegas. Los estratos son la confianza que el clasificador declaró: alta (40 sorteados de 419), media (40 sorteados de 169) y baja (los 7, sin sorteo). La revisión leyó los de confianza alta y baja; la verificación de cierre señaló que faltaba la confianza media, que es el 31 % del corpus, y se agregó.

| Eje | Confianza alta (419 en el marco) | Confianza media (169 en el marco) | Confianza baja (7 en el marco) | Estimación para los 595 del marco |
|---|---|---|---|---|
| Territorio | 31 de 40 (78 %; 62–88) | 26 de 40 (65 %; 50–78) | 2 de 7 | 73 % (64–83) |
| Dominio | 37 de 40 (93 %; 80–97) | 29 de 40 (73 %; 57–84) | 2 de 7 | 86 % (80–93) |
| Subfunción | 33 de 40 (83 %; 68–91) | 30 de 40 (75 %; 60–86) | 5 de 7 | 80 % (72–89) |
| Función | 37 de 40 (93 %; 80–97) | 35 de 40 (88 %; 74–95) | 7 de 7 | 91 % (85–97) |
| Los tres ejes a la vez | 25 de 40 (63 %; 47–76) | 16 de 40 (40 %; 26–55) | 0 de 7 | 55 % (45–66) |

Cada celda da los casos en que el segundo lector eligió el mismo primario, el porcentaje y, entre paréntesis, el intervalo de confianza del 95 %. La última columna pondera los tres estratos por su tamaño.

**Según de dónde viene la coordenada.** En territorio y en dominio, casi todo lo que se compara es coordenada heredada de la Taxonomía 5.3; en subfunción, la mayor parte la asignó el clasificador.

| Eje | Coordenada heredada de la Taxonomía 5.3 | Coordenada asignada por el clasificador |
|---|---|---|
| Territorio | 53 de 78 (68 %; 57–77) | 6 de 9 (67 %; 35–88) |
| Dominio | 60 de 78 (77 %; 66–85) | 8 de 9 (89 %; 56–98) |
| Subfunción | 18 de 27 (67 %; 48–81) | 50 de 60 (83 %; 72–91) |

Qué se puede decir y qué no:

- **El dominio coincide más que el territorio** en los dos estratos sorteados. Con estos tamaños los intervalos se tocan: la diferencia es probable y no segura.
- **La confianza que declara el clasificador ordena los resultados**: el acuerdo baja de confianza alta a media y a baja en territorio y en dominio. Entre alta y media los intervalos también se tocan.
- **Coincidir en los tres ejes a la vez es mucho menos frecuente.** En 46 de los 87 casos la lectura a ciegas difiere en algún eje. Ninguno se cambió por esa lectura. M6.2-K10 (dominio D11 → D17) cambió en la versión 1.2 por otra vía, una sugerencia confirmada, y está en el estrato E1. Los otros 45 son el estrato E2 de la revisión humana (sección 8.5).
- **El desacuerdo no dice quién se equivoca.** Puede fallar la coordenada vigente, el segundo lector o la regla, que en varios casos no decide: el revisor de la muestra complementaria dejó 15 hallazgos sobre reglas que no alcanzan para elegir, que se publican como insumo de la decisión D-11 (`data/reglas_D11_hallazgos_de_la_muestra_complementaria.csv`), y uno sobre el insumo que recibió.

Límites de esta medida:

- Los textos se entregaron recortados: 1.100 caracteres del texto y 600 de la tesis.
- En 52 de los 87 registros (20 de 47 en la primera muestra y 32 de 40 en la complementaria), el campo «tesis» que recibió el lector repite el comienzo del texto y no es una tesis propia.
- El marco deja afuera los pre-ensayos que estaban en D20 y las migraciones: de ellos no hay lectura a ciegas.
- Cada estrato tiene pocos casos: los intervalos son amplios, y con los 7 casos de confianza baja solo corresponde leer las fracciones.
- En territorio y dominio casi todo lo que se compara es coordenada heredada: la muestra dice poco sobre las coordenadas que asignó el clasificador.
- Los dos lectores son agentes automáticos con la misma configuración y pueden compartir un mismo error: el acuerdo no prueba que la coordenada sea correcta, y el desacuerdo no dice cuál de las dos lecturas se equivoca.
- Los dos estratos sorteados los leyeron dos revisores distintos, en dos momentos, con el mismo extracto de reglas.

### 6.2 Migraciones a dominios nuevos

De las 73 migraciones a D25, D26 y D28, la segunda lectura coincidió en 69 (94,5 %). El revisor sabía que todos los casos habían migrado, de modo que la cifra no es comparable con la de la muestra a ciegas. Las otras 4 se adjudicaron por escrito:

| Pre-ensayo | Título | Dominio 5.3 | Dominio en la 1.1 | Segunda lectura | Dominio en la 1.2 |
|---|---|---|---|---|---|
| HC-038 | Aseguramiento de la arquitectura Zero Trust | D05 | D25 | D28 | D28 |
| APC-088 | Gobierno de la validación del modelo de riesgo cibernético | D02 | D28 | D02 | D02 |
| APA-175 | Validación del modelo de estimación de pérdidas cibernéticas | D02 | D28 | D02 | D02 |
| APF-12 | Evidencia sobre la administración de la IA ante auditoría | D05 | D28 | D05 | D05 |

### 6.3 El dominio D20 y la decisión D-03

De los 71 pre-ensayos que estaban en D20, 26 salieron (16 a D01, 6 a D02, 2 a D17, 1 a D28 y 1 a D14) y 45 quedan. De los que salieron, en 13 las dos lecturas deciden el mismo destino, en 9 la primera lectura lo dejaba a criterio del curador y la segunda propone el destino, y 4 se adjudicaron por escrito. 22 fueron a los dominios que nombra la regla 7 y 4 a otros dominios, por reglas de alcance distintas. El territorio no se cambió en ningún caso, aunque la regla nombra T07. En 11 de los que quedan las dos lecturas no coinciden: están en la sección 8.4.

### 6.4 La Biblioteca cognitiva

- **Tipos.** De los 213 conceptos de las tres categorías que la regla no resolvía, 71 corresponden a un tipo específico. Se aplicaron los veredictos de confianza alta o media y las excepciones halladas en la muestra: 81 conceptos cambiaron de tipo. En la muestra de 120 conceptos de las demás categorías, 8 tenían un tipo equivocado; a esa tasa cabe esperar del orden de 70 más entre los 1.071 que nadie leyó.
- **Prácticas contra sesgos.** De 142 vínculos leídos uno por uno, 57 se sostienen, 77 son débiles y 8 son incorrectos. Se cargan solo los que se sostienen. El CSV trae los 142 con su veredicto; 6 de ellos salían de un emparejamiento por nombre que la versión 1.2 corrigió, y al repetir la extracción aparecieron 6 vínculos nuevos, que no se cargan y no tienen segunda lectura. Ninguno tiene evidencia de eficacia: dicen lo que la Biblioteca propone.
- **Territorios.** En una muestra de 100 conceptos, 49 asignaciones son dudosas. La causa es de origen: en la base, el territorio es un valor por categoría y no una lectura de cada concepto. Ya no se cargan como clasificación.
- **Cobertura por unidad.** Se cargan 165 vínculos, los de selección editorial o de ancla expresa. Los de coincidencia temática quedaron fuera.
- **Equivalencias con el corpus.** De 138 pares examinados, 21 son el mismo concepto, 91 están relacionados y 26 son distintos. La similitud de nombre no alcanza para encontrarlos.
- **Repeticiones dentro de la Biblioteca.** 45 grupos de conceptos nombran la misma idea: 31 en más de una categoría y 14 dentro de una misma categoría. Hay además 27 pares repetidos: 25 verificados leyendo las dos definiciones y 2 detectados porque sus nombres difieren solo en el singular o el plural.

### 6.5 La medición

- **Coordenada.** De los 70 indicadores que venían del catálogo 1.2, 67 heredan su coordenada sin cambios y 3 (K50, K51 y K60) tienen el dominio corregido por un revisor, con una lectura. Los otros 154 recibieron territorio y dominio de un revisor: 96 con confianza alta, 55 con confianza media y 3 con confianza baja. Es una sola lectura.
- **Subfunción.** De dónde sale la subfunción de los 224 indicadores: derivada de la categoría de CSF 2.0 que declara el catálogo 2.0, sin lectura del indicador (80); heredada del catálogo 1.2 (70); subfunción propuesta por la revisión crítica 1.2 (una lectura) (66); ubicada en PR03 por dos revisores, cada uno por separado (revisión crítica 1.2) (3); subfunción reubicada por la revisión crítica 1.2 (una lectura) (3); regla del paquete: los indicadores de arquitectura con categoría PR.IR van en PR03; sin lectura del indicador (2). PR06 quedó sin indicadores: los que tenía miden acceso y segmentación de red.
- **Variables homeostáticas.** De los 71 vínculos cargados, en 49 las dos lecturas coinciden en el vínculo y en el papel, en 14 coinciden solo en el vínculo, 5 los consideró y descartó la segunda lectura y 3 tienen una sola lectura. La segunda lectura propuso además 36 vínculos que no se cargaron. Son indicadores candidatos: ninguna variable tiene todavía unidad, umbral ni responsable del límite.
- **Dominios sin indicador primario:** D19, D22, D23 y D27. Tres de ellos aparecen como dominio secundario de algún indicador; D27 no aparece en ninguno.

### 6.6 La serie APX

De los 16 pre-ensayos, 4 quedaron como estaban y 12 se corrigieron. Cuatro cambiaron un valor primario de su coordenada o su horizonte (cinco valores en total) y uno más, APX-13, perdió un mecanismo homeostático; cambiaron además secundarios y un catalizador. Las 22 filas están en el archivo de cambios. Doce de los dieciséis tienen redacción corregida durante la revisión, que ningún revisor volvió a leer entera. Entran como capa de ampliación, aparte del corpus base.

### 6.7 La verificación externa

Segunda verificación independiente de 35 puntos que sostienen decisiones de la taxonomía o del remapeo (32 afirmaciones y 3 preguntas abiertas: 9 puntos sobre ATT&CK, ATLAS y CCM y 26 sobre otras normas y marcos), hecha contra las páginas de los organismos emisores durante la revisión crítica de la versión 1.2. Sin errores que cambien una decisión de la taxonomía. Se corrigieron dos registros (las versiones de Open FAIR y la identificación de las áreas de CyBOK), se confirmaron dos cambios de nombre de proyectos de NIST que estaban a revalidar y se precisaron cinco fichas. Cuatro conteos no se pudieron confirmar en fuente oficial pública: los controles de ISO/IEC 27002 y del Anexo A de ISO/IEC 42001, los 32 controles de Swift CSCF y las 11 áreas de competencia de NICE.

### 6.8 El grafo

| Medida | Versión 1.1 | Versión 1.2 |
|---|---|---|
| Nodos | 5.041 | 5.058 |
| Relaciones | 29.887 | 28.142 |
| Conjuntos de cambios | 15 | 16 |
| Reglas comprobadas por el validador | 13 de 37 | 19 de 37 |
| Errores y advertencias | 0 y 0 | 0 y 77 |
| Nodos sin descripción | 1.809 | 0 |
| Preguntas de competencia respondibles, de 22 | 13 (estado escrito a mano) | 7 (estado derivado de una prueba) |
| Preguntas respondibles en parte | 4 | 9 |
| Preguntas todavía sin respuesta | 5 | 6 |

El grafo tiene menos relaciones porque se dejaron de cargar vínculos que la revisión no sostuvo. Y responde menos preguntas porque en la versión 1.1 el estado de cada pregunta estaba escrito a mano, y ahora se deriva de una prueba. El validador comprueba 19 de las 37 reglas de la ontología y una comprobación propia del paquete (PAQ-01, sobre nombres de producto en el plano A).

## 7. Qué cambió respecto de la versión 1.1

La versión 1.1 era la base sobre la que aceptaste las decisiones. La 1.2 la corrige. `data/cambios_1_1_a_1_2.csv` registra cada cambio con el valor anterior, el nuevo, el motivo y el respaldo: 183 filas, de las que 171 son cambios de un elemento y 12 resumen un cambio hecho en bloque sobre 2.429 elementos (cada fila agregada dice cuántos elementos cubre y en qué archivo está el detalle). La tabla cuenta filas.

| Ámbito | Filas | Dos o más lecturas coinciden | La primera lectura no decidió | Sugerencia confirmada | Adjudicación escrita | Una lectura | Heredado del catálogo del autor | Las lecturas no coinciden | Verificación externa | Corrección de texto o de conteo |
|---|---|---|---|---|---|---|---|---|---|---|
| Corpus | 37 | 13 | 9 | 7 | 8 | — | — | — | — | — |
| Biblioteca | 86 | 3 | — | — | 7 | 76 | — | — | — | — |
| Medición | 20 | 4 | — | — | — | 8 | 2 | 6 | — | — |
| Serie APX | 22 | — | — | — | 10 | 12 | — | — | — | — |
| Cruce con dominios | 3 | — | — | — | 2 | — | — | — | 1 | — |
| Cruce con territorios | 1 | — | — | — | — | 1 | — | — | — | — |
| Taxonomía (texto) | 13 | — | — | — | — | — | — | — | — | 13 |
| Propuesta de remapeo | 1 | — | — | — | — | — | — | — | 1 | — |
| **Total** | 183 | 20 | 9 | 7 | 27 | 97 | 2 | 6 | 2 | 13 |

Cómo leer las columnas:

- **Dos o más lecturas coinciden:** dos lectores llegaron por separado al mismo resultado.
- **La primera lectura no decidió:** la primera lectura dejaba el caso a criterio del curador y la segunda propone el destino. Hay una sola lectura que decide.
- **Sugerencia confirmada:** un segundo lector aceptó una sugerencia del clasificador que tenía a la vista.
- **Adjudicación escrita:** las lecturas no coincidían o había una sola, y quien generó los artefactos decidió por escrito con la tesis y una regla explícita.
- **Una lectura:** el cambio descansa en un solo revisor. Son 97 filas (92 de un elemento y 5 agregadas, que cubren 283 elementos), y son las que más conviene que mires.
- **Heredado del catálogo del autor:** el valor ya estaba en el catálogo 1.2 y la versión 1.1 no lo había leído. No es la lectura de un revisor.
- **Las lecturas no coinciden:** el paquete afirmaba algo que la segunda lectura no acompañó, y se dejó la afirmación más débil.

**Cómo confirmar o revertir.** El archivo trae dos columnas vacías, `decision_del_autor` y `nota_del_autor`. Anotar «revertir» en la columna decision_del_autor de la fila. El curador quita el ajuste correspondiente de scripts/datos_de_trabajo/ajustes_revision_1_2.json y regenera el paquete con el orden del documento 10: el valor vuelve al de la versión 1.1 y los conteos, el grafo y los documentos se recalculan. Las filas agregadas se revierten en bloque, con el parámetro que las gobierna en ese mismo archivo. Revertir un cambio del corpus saca al pre-ensayo del estrato E1 de la revisión humana.

**Lo que se agregó.** Además de lo que cambió de valor, la versión 1.2 suma contenido que la 1.1 no tenía:

- Territorio y dominio para 154 indicadores que no los tenían, y subfunción por lectura para 66. Es una sola lectura. Los indicadores del sistema de gestión heredan los suyos del catálogo 1.2. Están en la tabla como filas agregadas.
- La serie APX en el grafo candidato, como capa de ampliación.
- Descripción en todos los nodos del grafo, tomada de la fuente cuando existe.
- Las 18 reglas propuestas, los casos de navegación resueltos y la muestra para la revisión humana.

**Lo que sigue igual:** los códigos y las cardinalidades de la Taxonomía 6.0, la Ontología 2.1.0, el GM-24, el banco de pre-ensayos, la base de la Biblioteca y el catálogo CISO 365.

## 8. Lo que queda en tus manos

### 8.1 En qué orden

Las decisiones dependen unas de otras. Este es el orden que el paquete propone, y es el mismo en el resumen ejecutivo, en el documento 10 y en el README:

| Paso | Qué | Por qué en ese lugar |
|---|---|---|
| 1 | D-14: confirmar lo que el paquete leyó en tu mensaje y lo que hizo en tu nombre. | Si alguna respuesta es «no», cambia la base sobre la que se apoya todo lo demás. |
| 2 | D-11.1: las reglas propuestas que cambian coordenadas. | Los once casos de D20 sin coincidencia (nueve de ellos, por RP-02) y la serie APX dependen de ellas. |
| 3 | D-11.3: releer los pre-ensayos que alcanzan las reglas adoptadas. | La revisión humana debe hacerse sobre la categorización ya ajustada. |
| 4 | Revisión humana por muestra, con el estrato E1, que resuelve D-13.1 y D-13.2. | Es la única fuente de validación humana. Si la relectura del paso 3 cambia coordenadas, la muestra se sortea de nuevo. |
| 5 | D-13.3 a D-13.6 y D-11.2: lo que queda de los cambios y las reglas que no mueven coordenadas. | No dependen de la muestra. |
| 6 | D-12: la Biblioteca, por separado. | No bloquea a las demás; la solicitud OCR-CAND-03 se decide con la próxima revisión de la ontología. |

Cada decisión se parte en proposiciones que se contestan con un sí o un no, y en tareas, con una estimación de esfuerzo. Las estimaciones son supuestos de quien armó el paquete, no medidas. El registro completo, con columnas para anotar tu respuesta, está en `data/decisiones_del_autor.json`.

### 8.2 Decisión D-14 · Confirmar lo que se leyó en tu mensaje

La aceptación fue en bloque y con una condición. El paquete tuvo que interpretar cuatro cosas para poder seguir, y las aplicó. Ninguna queda firme hasta que el autor la confirme.

| N.º | Tipo | Proposición o tarea | Respuestas | Si la respuesta es no | Esfuerzo estimado | Insumos |
|---|---|---|---|---|---|---|
| D-14.1 | Decisión | La aceptación en bloque de D-01 a D-10 vale aunque su condición se cumplió en parte: las diez decisiones chocaban en cuatro puntos, de los que dos se resolvieron, uno se resolvió en parte y uno sigue abierto; y que «apunten a la excelencia y al rigor» no lo puede certificar el paquete. | sí / no | Las diez decisiones vuelven a quedar abiertas y la versión 1.2 pasa a ser una propuesta. No hay que deshacer nada en los datos: los conjuntos de cambios ya están en estado «propuesto». | 15 minutos: sección 2 del documento 13. | docs/13_Revision_critica_1_2.md, sección 2 |
| D-14.2 | Decisión | D-03 era una pregunta. Se confirma el «sí»: el gobierno, el riesgo y el cumplimiento de la IA que estaban alojados en D20 pasan a D01, D02 o D03. | sí / no | Se revierten los 22 cambios del corpus cuyo origen empieza con «decisión D-03» (procedimiento de reversión, más abajo). Los otros cambios de pre-ensayos de D20 no dependen de esta decisión. | 30 minutos: la regla 7 y la tabla de la sección 7 del documento 07. | docs/07_Categorizacion_del_Corpus.md, sección 7; data/analisis_D20_decision_D03.csv |
| D-14.3 | Decisión | D-10 pedía «decidir sobre las propuestas editoriales». Se confirman las dos lecturas: (a) la propuesta de remapeo es el pedido para la próxima versión del GM-24, y (b) los 16 pre-ensayos de la serie APX entran como capa de ampliación, fuera del corpus base. | (a) sí / no; (b) sí / no | (a) La propuesta de remapeo queda como análisis, sin destinatario. (b) La serie APX se retira del grafo candidato (su conjunto de cambios) y de los documentos 06 y 12. | 1 hora: documento 12 y data/propuesta_remapeo_gm24.csv. | docs/12_Ampliacion_Celdas_en_Blanco.md; docs/04_Base_de_Referencia.md |
| D-14.4 | Decisión | D-01 se confirma con la advertencia a la vista: el nombre coincide con un concepto comercial de un proveedor y con el nombre de una de sus suites, y 77 pre-ensayos del plano A, que se propone agnóstico de proveedor, nombran productos o al proveedor. | sí / no / otro nombre | Cambiar el nombre obliga a regenerar todos los documentos; los códigos y los datos no cambian. | 10 minutos. | docs/02_De_AI_CISO_Atlas_a_Frontier_CISO_Atlas.md; ADR-013 |
| D-14.5 | Decisión | «Propone una forma de implementar […] informa y continua» se leyó como autorización para ejecutar la revisión crítica y la mejora sin una consulta intermedia, y así se hizo el mismo día. | sí / no | La versión 1.2 queda como propuesta de revisión y la 1.1 sigue siendo la vigente. Ningún archivo de la 1.1 se modificó. | 5 minutos. | docs/13_Revision_critica_1_2.md, sección 2 |
| D-14.6 | Decisión | ADR-029 redacta el principio que enunciaste: el Atlas funciona como guía y orientación; quien lo usa lee con atención, no cree nada por defecto, contrasta con su conocimiento y su formación y acepta cada elemento bajo una responsabilidad final que no se delega. | sí / corregir la redacción | Se corrige el texto de ADR-029 y de la sección «Uso previsto y límites» del README. | 10 minutos. | docs/08_Decisiones_de_Arquitectura.md, ADR-029 |
| D-14.7 | Decisión | ADR-026 (qué efecto tiene la aceptación en bloque), ADR-027 (revisión crítica antes de publicar) y ADR-028 (vía de corrección de una coordenada heredada: dos lecturas o una adjudicación escrita) rigen de forma provisoria desde la versión 1.2, junto con las instrucciones 7.2 del agente curador, que las recogen. | sí / no, por cada ADR | ADR-026: equivale a un «no» en D-14.1. ADR-028: se revierten los 37 cambios del corpus, que entraron todos por esa vía, y la política vuelve a ser la de ADR-020 (la coordenada heredada no se toca). ADR-027: no hay nada que deshacer; deja de ser práctica. | 20 minutos. | docs/08_Decisiones_de_Arquitectura.md, ADR-026 a ADR-028 |

### 8.3 Decisión D-11 · Reglas propuestas

Ninguna se aplicó. Las 18 reglas suman 95 enunciados: 60 son reglas con texto listo, 11 son preguntas para el autor y 24 son encargos de trabajo (clasificación automática por el verbo inicial, orientativa). 13 reglas cambian coordenadas ya asignadas (RP-01, RP-02, RP-03, RP-04, RP-05, RP-06, RP-07, RP-08, RP-09, RP-10, RP-12, RP-13, RP-18) y piden releer parte del corpus. Ninguna trae ejemplos ni estima cuántos pre-ensayos cambiarían: es un límite de esta propuesta. Para las que cambian coordenadas, la columna alcance_de_la_relectura da una cota superior de los pre-ensayos alcanzados.

| N.º | Tipo | Proposición o tarea | Respuestas | Si la respuesta es no | Esfuerzo estimado | Insumos |
|---|---|---|---|---|---|---|
| D-11.1 | Decisión | Reglas que cambian coordenadas ya asignadas (RP-01, RP-02, RP-03, RP-04, RP-05, RP-06, RP-07, RP-08, RP-09, RP-10, RP-12, RP-13, RP-18): adoptar, modificar o rechazar cada enunciado. | por enunciado: adoptar / modificar / rechazar | La regla rechazada no se aplica y los pre-ensayos quedan como están. | Medio día: 69 enunciados. | data/reglas_propuestas_D11_enunciados.csv (columna para anotar la decisión), data/reglas_propuestas_D11.csv y data/reglas_D11_hallazgos_de_la_muestra_complementaria.csv (16 hallazgos sobre reglas que no deciden, con la regla relacionada) |
| D-11.2 | Decisión | Reglas que aclaran un texto o tocan lentes, planos, el modelo del eje H o los criterios de admisión (las demás): adoptar, modificar o rechazar cada enunciado. | por enunciado: adoptar / modificar / rechazar | El texto de la Taxonomía 6.0 queda como está. | Medio día: 26 enunciados. | los mismos archivos |
| D-11.3 | Tarea | Releer con las reglas adoptadas en D-11.1 los pre-ensayos que cada regla alcanza. | la hace el curador, con una segunda lectura; el autor revisa el resultado dentro de la revisión humana | — | Depende de las reglas adoptadas. La columna alcance_de_la_relectura da, para cada regla, los códigos que nombra y cuántos pre-ensayos los tienen como primario: es una cota superior, sin lectura. | data/reglas_propuestas_D11.csv, columna alcance_de_la_relectura |

| Regla | Tema | Efecto si se adopta | Enunciados | Hallazgos que la motivan |
|---|---|---|---|---|
| RP-01 | Precedencia general entre disciplina y objeto | Cambia coordenadas ya asignadas: pide releer parte del corpus | 2 | 4 |
| RP-02 | Regla 6: cláusula de pilar y fronteras de D28 | Cambia coordenadas ya asignadas: pide releer parte del corpus | 7 | 14 |
| RP-03 | La auditoría en D03 y en D28 | Cambia coordenadas ya asignadas: pide releer parte del corpus | 2 | 4 |
| RP-04 | Regla 7: desempate, territorio y alcance | Cambia coordenadas ya asignadas: pide releer parte del corpus | 7 | 15 |
| RP-05 | Regla 3: qué es un pilar y qué es un principio transversal | Cambia coordenadas ya asignadas: pide releer parte del corpus | 5 | 5 |
| RP-06 | Regla 4: fronteras de D26 | Cambia coordenadas ya asignadas: pide releer parte del corpus | 4 | 2 |
| RP-07 | Regla 5: fronteras de D27 | Cambia coordenadas ya asignadas: pide releer parte del corpus | 4 | 2 |
| RP-08 | Inventario, activos, configuración y ciclo de vida de los controles | Cambia coordenadas ya asignadas: pide releer parte del corpus | 4 | 5 |
| RP-09 | Territorios: de quién es la perspectiva y desempates | Cambia coordenadas ya asignadas: pide releer parte del corpus | 7 | 7 |
| RP-10 | Regla 1: pruebas de aplicación | Cambia coordenadas ya asignadas: pide releer parte del corpus | 8 | 10 |
| RP-11 | Regla 2: desempates de cardinalidad | Aclara una regla; puede cambiar secundarios | 2 | 2 |
| RP-12 | Subfunciones: definición y delimitación | Cambia coordenadas ya asignadas: pide releer parte del corpus | 10 | 17 |
| RP-13 | RC04 bajo la función Recuperar | Cambia coordenadas ya asignadas: pide releer parte del corpus | 2 | 3 |
| RP-14 | Anclas del MCCS y escala del pilar OS | Lentes: no cambia la coordenada | 3 | 7 |
| RP-15 | Eje H: completar el modelo de referencia | Modelo de referencia del eje H | 9 | 14 |
| RP-16 | Criterios de admisión de dominios | Criterios de admisión de dominios | 8 | 21 |
| RP-17 | Lentes y agrupaciones | Lentes y planos: no cambia la coordenada | 4 | 5 |
| RP-18 | Fronteras y alcances heredados | Cambia coordenadas ya asignadas: pide releer parte del corpus | 7 | 11 |

El texto de cada regla está en `data/reglas_propuestas_D11.csv` y en el documento 03. `data/reglas_propuestas_D11_enunciados.csv` trae los 95 enunciados, uno por fila, con una columna para tu decisión. En tres reglas (RP-13, RP-14 y RP-16) la versión 1.2 ya hizo, como corrección, una parte de lo que pedían los hallazgos; el archivo lo dice en cada una.

### 8.4 Decisión D-13 · Confirmar o revertir lo que cambió

Los cambios están en data/cambios_1_1_a_1_2.csv: 183 filas, de las que 171 son cambios de un elemento y 12 resumen cambios en bloque. El archivo trae dos columnas vacías para anotar la decisión. Los indicadores K59, K43 y K54 no son casos sin coincidencia: el revisor pidió revisarlos y no propuso otra coordenada; quedan como estaban.

| N.º | Tipo | Proposición o tarea | Respuestas | Si la respuesta es no | Esfuerzo estimado | Insumos |
|---|---|---|---|---|---|---|
| D-13.1 | Decisión | Los 11 pre-ensayos de D20 en que las lecturas no coinciden (AMP-46, HC-010, APC-210, APC-212, APA-053, APA-068, APA-075, APA-108, APA-111, APA-113, APA-158): elegir el dominio de cada uno. | por caso: queda en D20 / pasa al dominio que propone la segunda lectura / otro | — | 1 hora: una ficha por caso. | data/casos_sin_coincidencia_D13.csv (tesis, las dos lecturas con su argumento y la regla de la que depende cada caso). Los once dependen de reglas propuestas (nueve, de RP-02; los otros dos, de RP-04 y de RP-03 con RP-04): conviene decidirlas antes. |
| D-13.2 | Decisión | Los 37 cambios de coordenada del corpus: confirmar o revertir. | por fila: confirmar / revertir | Se revierte la fila (procedimiento de reversión). | Incluido en la revisión humana: son el estrato E1 de la muestra. | data/cambios_1_1_a_1_2.csv, ámbito «Corpus»: sus filas son, con los casos de data/casos_sin_coincidencia_D13.csv, el estrato E1 de la revisión humana |
| D-13.3 | Decisión | Los cambios de la Biblioteca (86 filas): tipos de 81 conceptos, pilar OS de 59, territorios, cobertura y prácticas contra sesgos. | en bloque o por fila: confirmar / revertir | Se revierte el bloque o la fila. | Medio día para decidir en bloque; la lectura por concepto es la decisión D-12. | data/cambios_1_1_a_1_2.csv, ámbito «Biblioteca» |
| D-13.4 | Decisión | Los cambios de la medición (20 filas) y de la serie APX (22 filas): confirmar o revertir. | en bloque o por fila: confirmar / revertir | Se revierte el bloque o la fila. | 2 horas. | data/cambios_1_1_a_1_2.csv, ámbitos «Medición» y «Serie APX»; docs/12_Ampliacion_Celdas_en_Blanco.md |
| D-13.5 | Decisión | Los cambios de texto de la taxonomía (13 filas), de los cruces (4 filas) y de la propuesta de remapeo (1 fila): confirmar o revertir. | en bloque o por fila: confirmar / revertir | Se revierte el bloque o la fila. Las correcciones de texto se revierten en el guion de la taxonomía. | 1 hora. | data/cambios_1_1_a_1_2.csv, ámbitos «Taxonomía (texto)», «Cruce con dominios», «Cruce con territorios» y «Propuesta de remapeo»; docs/03_Taxonomia_6_0.md, sección de correcciones |
| D-13.6 | Tarea | Los indicadores K59, K43 y K54, que un revisor pidió revisar sin proponer otra coordenada: revisarlos al leer el catálogo. | la hace el autor o el curador al revisar la medición | — | 15 minutos. | data/indicadores_ciso365_en_el_atlas.csv |

Los 11 casos de D20 en que las lecturas no coinciden quedaron como estaban. `data/casos_sin_coincidencia_D13.csv` trae una ficha de cada uno, con la tesis, las dos lecturas con su argumento y la regla de la que depende:

| Pre-ensayo | Título | Territorio | Por qué no se movió |
|---|---|---|---|
| AMP-46 | Trazabilidad de decisiones autónomas | T08 | La segunda lectura propone D28; sin coincidencia, a decisión del autor |
| HC-010 | Autonomía delegada y límites de acción | T07 | La segunda lectura no acompaña el movimiento de la primera; a decisión del autor |
| APC-210 | Umbrales de desempeño y aseguramiento para aprobar despliegues de IA | T08 | La segunda lectura propone D28; sin coincidencia, a decisión del autor |
| APC-212 | Compensación de mitigaciones adversariales sin garantía formal | T08 | La segunda lectura propone D28; sin coincidencia, a decisión del autor |
| APA-053 | Pruebas de agentes antes de producción y tras cada cambio | T08 | La segunda lectura propone D28; sin coincidencia, a decisión del autor |
| APA-068 | Inventario de sistemas de IA con impacto en clientes | T07 | La segunda lectura propone D03; sin coincidencia, a decisión del autor |
| APA-075 | Registro auditable de agentes en producción y sus permisos | T08 | La segunda lectura propone D28; sin coincidencia, a decisión del autor |
| APA-108 | Criterio de inclusión y completitud del inventario de IA | T07 | La segunda lectura propone D28; sin coincidencia, a decisión del autor |
| APA-111 | Expediente de aprobación para producción de sistemas de IA | T08 | La segunda lectura propone D28; sin coincidencia, a decisión del autor |
| APA-113 | Aseguramiento razonable frente a la manipulación de la IA | T08 | La segunda lectura propone D28; sin coincidencia, a decisión del autor |
| APA-158 | Cobertura y adaptación de controles ante riesgos de IA | T08 | La segunda lectura propone D28; sin coincidencia, a decisión del autor |

### 8.5 La revisión humana de la categorización

La decisión D-07 pedía validar la categorización, pero no decía cuánto revisar, cómo decidir ni quién revisa. Esta es una propuesta. Los umbrales los fijás vos.

**Quién.** El autor, o una persona con formación de CISO que él designe. El agente curador mantiene el paquete y no hace esta revisión. Con una sola persona, que además es el autor del banco del que se heredan casi todas las coordenadas, el resultado es «revisada por el autor en una muestra»: mide cuánto coincide él con la coordenada vigente. Para decir «validada» hace falta una segunda persona, que lea al menos un tercio de la muestra sin ver la lectura de la primera. Se informa cuánto coinciden las dos.

**Qué.** Territorio primario, dominio primario y subfunción primaria de cada pre-ensayo de la muestra. El horizonte, las fuerzas y el pilar no entran.

**Con qué reglas.** Con las reglas de asignación vigentes de la Taxonomía 6.0 (documento 03; el mismo extracto que recibieron los revisores automáticos está en revision_critica/comun/REGLAS_ATLAS.md). Si antes se adoptan reglas de la decisión D-11 que cambian coordenadas, primero se relee lo que esas reglas alcanzan y después se sortea de nuevo.

**Qué cuenta como cambio.** Que el primario que asigna el revisor sea distinto del primario vigente. Se informa aparte cuántos de esos cambios coinciden con un secundario vigente: son un cambio de orden y no de contenido. Se registra el desacuerdo, se discute con la tesis a la vista y decide el autor. La tasa de acuerdo entre las dos personas se publica junto al resultado.

**Cuánto.** 246 pre-ensayos en cinco estratos:

| Estrato | Qué es | Pre-ensayos | En la muestra | Cómo | ¿A ciegas? | ¿Entra en la estimación? |
|---|---|---|---|---|---|---|
| E1 | Cambió en la versión 1.2, o es uno de los casos de D20 en que las dos lecturas no coinciden | 48 | 48 | Todos | No: sus coordenadas están publicadas en los documentos 07 y 13 y en el archivo de cambios | No |
| E2 | La lectura a ciegas de un segundo lector automático difiere de la coordenada vigente en algún eje | 45 | 45 | Todos | Sí, si se lee antes de abrir data/muestra_a_ciegas_1_2.csv | No |
| E3 | Confianza media o baja del clasificador | 177 | 49 | Sorteo simple sin reposición | Sí | Sí |
| E4 | Confianza alta, clases con mayoría de texto de plantilla (K y HC) | 160 | 48 | Sorteo simple sin reposición | Sí | Sí |
| E5 | Confianza alta, demás clases | 309 | 56 | Sorteo simple sin reposición | Sí | Sí |
| **Total** |  | 739 | 246 |  |  |  |

El tamaño de los estratos sorteados sale de una fórmula estándar para estimar una proporción (n0 = z² · p · (1 − p) / e², corregido por población finita: n = n0 / (1 + (n0 − 1) / N)), con un nivel de confianza del 95 % y p = 0,5. p = 0,5 es el valor que no supone ninguna tasa y da el tamaño más grande. No se usa el desacuerdo de la muestra a ciegas porque esa muestra no midió la tasa de cambio de un revisor humano. 12 puntos es el margen de cada estrato sorteado, tomado solo. La regla de decisión usa la estimación ponderada de los tres estratos, cuyo margen es de 7,2 puntos con el diseño completo y de 13,0 con el camino mínimo. Con otros márgenes:

| Margen de cada estrato, en puntos | Pre-ensayos sorteados | Margen de la estimación ponderada, en puntos |
|---|---|---|
| 10 | 198 | 6,0 |
| 12 | 153 | 7,2 |
| 15 | 107 | 9,1 |

**En qué orden leer.** La muestra está partida en tandas, para que puedas detenerte:

| Tanda | Qué | Pre-ensayos | Archivos | Para qué |
|---|---|---|---|---|
| E1 | Los cambios de la versión 1.2 y los casos de D20 sin coincidencia. No es a ciegas: se revisa con las fichas. | 48 | data/cambios_1_1_a_1_2.csv (ámbito «Corpus») y data/casos_sin_coincidencia_D13.csv | D-13.1 y D-13.2 |
| 1 | Los primeros 20 casos sorteados de cada estrato (E3, E4 y E5), mezclados. | 60 | data/revision_humana_muestra.csv, columna tanda = 1 | Una primera estimación, con un margen amplio |
| 2 | Los casos en que la lectura a ciegas automática difiere de la coordenada vigente (E2). | 45 | la misma, tanda = 2 | Desempata dos lecturas que no coinciden |
| 3 | El resto de los casos sorteados. | 93 | la misma, tanda = 3 | Lleva la estimación al margen del diseño completo |

**Cuánto lleva.** 5 minutos por pre-ensayo. Es un supuesto, no una medida: conviene cronometrar los primeros diez. El camino mínimo (E1 con las fichas y la tanda 1) son 108 pre-ensayos, unas 9,0 horas: resuelve la parte del corpus de la decisión D-13 y detecta un problema grande. Con ese margen, casi cualquier umbral queda «no concluyente». El diseño completo son 246 pre-ensayos, unas 20,5 horas, y lleva el margen de la estimación a 7,2 puntos.

**¿Se puede aceptar sin validar?** Sí. El autor puede dejar la categorización como base de trabajo, sin validar, y redactar ensayos sabiendo que la coordenada de cada uno se revisa al escribirlo.

**Regla de decisión.** Tasa de cambio por eje: parte de los pre-ensayos sorteados (E3, E4 y E5) en que el revisor asigna un primario distinto del vigente, ponderada por el tamaño de cada estrato, con su intervalo de confianza del 95 %. Los umbrales los fija el autor, antes de mirar la clave. Este paquete no propone valores.

- **Cumple.** El límite superior del intervalo queda por debajo del umbral. La categorización pasa de «base de trabajo» a «revisada por el autor en una muestra», con la tasa medida y su intervalo a la vista. Los cambios del revisor se aplican.
- **No cumple.** El límite inferior del intervalo queda por encima del umbral. Se relee completo, empezando por el estrato con la tasa más alta, antes de redactar ensayos con sus pre-ensayos. La tasa por estrato orienta el orden y no decide: su margen es de unos 12 puntos.
- **No concluyente.** El umbral queda dentro del intervalo: la muestra no alcanza para decidir. Se amplía el sorteo de los tres estratos o se acepta seguir con la categorización como base de trabajo. No se la llama revisada.
- **Los estratos E1 y E2.** Se revisan completos y no entran en la estimación. En E1 cada cambio se confirma o se revierte (decisión D-13). En E2 el revisor desempata dos lecturas automáticas que no coinciden.

**Qué cabe esperar.** La muestra a ciegas midió cuánto difiere un lector automático de la coordenada vigente, en el corpus sin D20 ni las migraciones: 26,6 % en territorio (intervalo de 17 a 36), 13,9 % en dominio (7 a 20) y 19,8 % en subfunción (11 a 28). No es la tasa de un revisor humano, pero es la única referencia disponible: un umbral más bajo que esos valores probablemente no se cumpla. Con el diseño completo, la tasa observada tiene que quedar unos 7,2 puntos por debajo del umbral para que el resultado sea «cumple».

**Cómo leer a ciegas.** La muestra no trae identificadores, porque el identificador de muchos pre-ensayos nombra su unidad curricular: cada caso lleva un número de orden y la clave lo une con su identificador. Conviene leer la muestra antes de abrir la clave, el documento 07 y data/muestra_a_ciegas_1_2.csv. Algunos textos nombran su unidad o su tema en el cuerpo: eso no se quitó.

**Archivos.** `data/revision_humana_muestra.csv` trae los pre-ensayos en el orden de lectura, con columnas vacías para tu coordenada y sin la vigente. `data/revision_humana_clave.csv` trae la coordenada vigente, los secundarios y el estrato. `data/revision_humana_propuesta.json` trae el plan completo.

**Límites.** La revisión mide el acuerdo entre el revisor y la categorización vigente. No prueba que la taxonomía sea la correcta. Con un solo revisor, que es el autor del banco heredado, la medida no es independiente de la coordenada que revisa. El horizonte, las fuerzas y el pilar no entran en esta revisión. El estrato E1 no se lee a ciegas.

### 8.6 Decisión D-12 · La Biblioteca

La base de la Biblioteca es del autor y este paquete no la modificó. El choque entre D-04 y D-08 sigue abierto en las habilidades socioemocionales y en las mentalidades de resiliencia, que la regla de pilar por categoría deja en MM. Los defectos que la revisión señaló en la base están en data/biblioteca_defectos_senalados.csv.

| N.º | Tipo | Proposición o tarea | Respuestas | Si la respuesta es no | Esfuerzo estimado | Insumos |
|---|---|---|---|---|---|---|
| D-12.1 | Decisión | Los territorios de un concepto de la Biblioteca se derivan por lectura del concepto, y no por su categoría. | sí / no | Los territorios siguen como propiedad del nodo, sin cargarse como clasificación. | 10 minutos para decidir; la lectura es la tarea D-12.5. | docs/06_Grafo_de_Conocimiento.md, sección 2.5 |
| D-12.2 | Decisión | El pilar de las habilidades socioemocionales y de las mentalidades de resiliencia se asigna por lectura del concepto: OS a escala individual, DO o MM. | por lectura / se quedan en MM | Quedan en MM y el choque entre D-04 y D-08 se da por aceptado. | 10 minutos para decidir; la lectura alcanza a 226 conceptos de dos categorías. | data/biblioteca_cognitiva_1404.csv, columnas categoria y pilar_mccs |
| D-12.3 | Decisión | Las categorías de mentalidades y de prácticas de decisión se releen completas antes de fijar el tipo de sus conceptos. | sí / no | Conservan el tipo por regla, con las excepciones ya aplicadas. | 10 minutos para decidir; la relectura alcanza a 288 conceptos. | docs/13_Revision_critica_1_2.md, sección 6.4 |
| D-12.4 | Decisión | Los 45 grupos de conceptos que nombran la misma idea y los 27 pares repetidos se resuelven en la base: fusionar, declarar equivalentes o dejar separados. | por grupo: fusionar / equivalentes / separados | — | Medio día. | data/biblioteca_grupos_mismo_concepto.csv; data/biblioteca_dobletes_internos.csv; data/equivalencias_biblioteca_corpus.csv |
| D-12.5 | Tarea | Revisar por muestra los tipos y los territorios de la Biblioteca. | la hace el autor o una persona que él designe | — | Sin diseñar: falta definir la muestra y el criterio. La revisión midió 8 tipos equivocados en una muestra de 120 conceptos de las categorías que la regla daba por resueltas. | data/biblioteca_cognitiva_1404.csv |

Además, 355 definiciones de la base no están respaldadas por una fuente.

### 8.7 Otras cosas que la revisión deja escritas

Las 129 propuestas que quedaron para vos van a estos destinos:

| Destino | Propuestas |
|---|---|
| D-11: reglas propuestas | 103 |
| Solicitud OCR-CAND-03 (ontología) | 12 |
| D-12: la Biblioteca | 11 |
| D-13: casos de D20 sin coincidencia | 1 |
| Revisión humana: el criterio lo fija el autor | 1 |
| D-14.4: el nombre, con la advertencia | 1 |

- **Ontología.** La solicitud OCR-CAND-03 reúne 16 propuestas para la próxima revisión. No se aplicó ninguna. No es una decisión numerada. La decide el autor, como dueño de la ontología, cuando abra su próxima revisión; no bloquea a las demás decisiones.
- **Catálogo CISO 365.** 22 observaciones sobre el catálogo, que es tuyo y este paquete no modifica: `data/observaciones_catalogo_ciso365.csv`.
- **Celdas vacías.** De las 132 combinaciones de territorio y dominio sin pre-ensayos, la cifra no distingue las que no pueden darse de las que no tienen contenido. Separarlas necesita tu juicio.

## 9. Límites que siguen en pie

1. Los revisores son agentes automáticos con la misma configuración que quien generó los artefactos: tienen contexto independiente, no juicio independiente. Donde hubo dos lecturas y coincidieron es menos probable un desliz de lectura; eso no dice nada de un error que compartan.
2. La mayor parte del contenido tiene una sola lectura: 502 de los 739 pre-ensayos, los 154 indicadores que no heredan su coordenada y 97 de las 183 filas de cambios.
3. Quien generó los artefactos preparó también los insumos de cada revisor, adjudicó los desacuerdos y decidió qué hacer con cada hallazgo. El triaje y las adjudicaciones no tuvieron una lectura independiente hasta la verificación de cierre, que revisó una parte.
4. La regla «dos lecturas coincidentes o una adjudicación escrita» se aplicó a las coordenadas heredadas del corpus. Lo demás se cambió con una lectura, y así está rotulado.
5. El horizonte, las fuerzas y el pilar de los pre-ensayos no tuvieron segunda lectura. El territorio y la subfunción solo la tuvieron en la muestra a ciegas.
6. Lo que se escribió durante la corrección (las reglas propuestas, la redacción corregida de 12 pre-ensayos de la serie APX y los textos de la taxonomía) no lo había leído ningún revisor. La verificación de cierre leyó una parte.
7. La muestra a ciegas mide el acuerdo de un lector automático con la coordenada vigente, que en territorio y dominio es casi siempre la heredada. Deja afuera los pre-ensayos que estaban en D20 y las migraciones, y sus intervalos son amplios.
8. Las segundas lecturas trabajaron con textos recortados (1.100 caracteres del texto y 600 de la tesis).
9. En 285 de los 739 pre-ensayos (clases K y HC), la mayor parte del texto es de plantilla (mediana del 70 % o más): su clasificación descansa en el título y en pocas oraciones.
10. El corpus no es neutral respecto de un proveedor: 77 pre-ensayos del plano A nombran sus productos o al proveedor, y es el organismo con más artefactos en la base de referencia.
11. Los cambios aplicados sin segunda lectura quedan rotulados «una lectura» y el autor puede revertirlos (decisión D-13).
12. Ningún elemento tiene validación humana.
13. El validador comprueba 19 de las 37 reglas de la ontología. La validación es estructural: no dice si el contenido es correcto.
14. 1.069 clasificaciones del grafo siguen declarando la Taxonomía 5.3 y no pasaron por la política de migración: 705 son de preguntas heredadas de la matriz y 364 son de indicadores del catálogo 1.2.
15. El contenido del MCCS no está cargado: el Atlas dice dónde está cada cosa, pero el instrumento que responde «cómo decido» sigue fuera del grafo.
16. No hay una guía para instanciar el Atlas en una organización ni un caso resuelto de punta a punta.

## 10. Incidencias del proceso

- Dos revisores terminaron sin entregar resultados: su respuesta final quedó retenida y no habían guardado nada en disco, aunque el formato común pide guardar por tramos. Se relanzaron una vez, con el encargo dividido en dos y con guardado por tramos; los cuatro encargos resultantes cerraron. La causa no se estableció: pudo ser el tamaño del encargo, la forma de trabajar del revisor o la retención de la respuesta.
- Por falsas alarmas sobre la configuración de los lanzamientos se detuvieron, en tres ocasiones, agentes que estaban bien lanzados: 3 en la versión 1.0, 14 al empezar la revisión y 4 en la verificación de cierre. Hubo una falsa alarma más, sin detención, al lanzar la lectura final de consistencia. El registro de eventos de la sesión muestra que, de los 53 agentes auxiliares lanzados entre el 15 y el 16 de noviembre, en 40 la configuración la agregó la plataforma y en 13 de la revisión crítica la escribió quien despachaba, sin que el autor lo pidiera y con el mismo valor que agrega la plataforma. Todos corrieron con la misma configuración y no se perdió ningún resultado, pero las detenciones y los relanzamientos costaron tiempo de trabajo, que no se midió. La nota de incidencia de las versiones 1.0 y 1.1 era inexacta en la atribución, y la primera rectificación que se le comunicó al autor durante el cierre también lo fue: se corrigió con el registro a la vista. El detalle está en las incidencias 12 y 13 de la bitácora.
- Hubo dos desconexiones de la sesión durante el día, que impidieron iniciar 18 lanzamientos. Los lanzamientos se repitieron después de cada desconexión. No se perdió ningún resultado.
- En la verificación de cierre, el revisor de la muestra complementaria terminó su primer turno con la respuesta retenida y sin guardar nada. Se le pidió por mensaje que guardara en disco y completó el encargo: 40 veredictos y 16 hallazgos sobre las reglas.

El detalle está en `09_Bitacora_de_Tareas.md`, sección 2.

## 11. Verificación de cierre y regresión

**Verificación de cierre.** Cuatro revisores que no habían participado leyeron una copia congelada de la versión corregida. Uno recalculó las cifras de los documentos; otro comprobó el cierre de los 48 hallazgos críticos y altos; otro hizo una lectura escéptica de lo que se escribió durante la corrección, con tu mensaje literal a la vista; y otro comprobó una muestra de 60 hallazgos medios y bajos. De los 108 hallazgos comprobados, dieron por cerrados 85 y por cerrados en parte 23. Dejaron 139 hallazgos nuevos: 11 altos, 61 medios, 61 bajos y 6 observaciones.

Los hallazgos altos fueron de cinco clases, y ninguna la había visto la revisión anterior:

- **La muestra a ciegas no era lo que se decía.** Se presentaba como un sorteo del corpus y como el acuerdo entre dos lecturas automáticas. Era una muestra de confianza alta y baja, sin la media, y casi todo lo que comparaba en territorio y dominio era coordenada heredada. Se agregó el estrato que faltaba y se cambió la descripción (sección 6.1).
- **La aceptación se había registrado con más alcance del que tuvo.** Dos decisiones que eran preguntas figuraban como «aceptadas», y la condición de la aceptación figuraba como cumplida. Se registraron como lecturas a confirmar y se abrió la decisión D-14 (sección 2).
- **Las decisiones abiertas no se podían decidir.** Dos estaban escritas como tareas y el orden propuesto no se podía ejecutar. Se partieron en proposiciones y se fijó un solo orden (sección 8).
- **El criterio de la revisión humana no era coherente con lo que la muestra podía medir.** Se rehízo con una regla de decisión de tres resultados, sin proponer umbrales (sección 8.5).
- **La recarga del catálogo de agentes perdía 15 vínculos.** Se corrigió el orden de creación de los nodos.

De los 139 hallazgos de cierre, 132 se corrigieron, 6 se corrigieron en parte y 1 se documentó, según quien los corrigió. De los 16 hallazgos que dejó la segunda lectura complementaria, 15 son sobre reglas que no deciden y se publican como insumo de la decisión D-11 (`data/reglas_D11_hallazgos_de_la_muestra_complementaria.csv`); el otro es un límite del método. El detalle está en `revision_critica/cierre/libro_de_cierre.csv`. La nota de cierre de cada revisor, sus hallazgos y sus veredictos están en `revision_critica/cierre/`.

**Lectura final.** Después de esa segunda corrección, un revisor más hizo una lectura final de consistencia de los documentos reescritos (README, documentos 01 y 13, el registro de decisiones y partes de los documentos 07 a 10), recalculando sus cifras desde los datos. Dejó 16 hallazgos (2 altos, 14 medios): 14 corregidos, 2 corregidos en parte. En su nota de cierre listó además cuatro observaciones menores, que también se corrigieron. Sus hallazgos y su nota de cierre están en `revision_critica/cierre/v5/`.

**Lo que esta verificación no cubre.** Los revisores de cierre son agentes automáticos con la misma configuración que los demás. Leyeron la versión candidata, no la publicada: lo que se corrigió a partir de sus hallazgos, que incluye la reescritura de buena parte de este documento, tuvo una sola lectura más, la final, que fue parcial; y lo que se corrigió a partir de la lectura final no tuvo ninguna. Tampoco ejecutaron los guiones ni comprobaron hechos externos.

**Regresión.** 10 de 10 verificaciones sin diferencias.

| Verificación | Resultado |
|---|---|
| Manifiesto del paquete | 348 archivos con su huella SHA-256; 0 no coinciden y 0 no figuran en el manifiesto |
| Versiones 1.0 y 1.1 publicadas | versión 1.0: 115 archivos, 0 diferencias con su manifiesto; versión 1.1: 146 archivos, 0 diferencias con su manifiesto. No se modificaron |
| Archivos citados en los documentos | 278 citas en 17 documentos; 0 no existen |
| Estadísticas contra los datos | 23 cifras recalculadas desde los archivos de datos y desde la base del grafo; 0 no coinciden |
| Cifras clave de los documentos | 37 cifras clave buscadas en 9 documentos, cada una junto a la palabra que la nombra; 0 no aparecen. No comprueba las demás cifras de los documentos |
| Hallazgos críticos y altos | 48 hallazgos; 0 sin decisión, acción o lugar donde se ve |
| Grafo candidato | 0 errores de validación; reconstrucción desde los conjuntos de cambios igual al grafo |
| Versión que declaran los archivos de datos | 0 archivos declaran una versión del producto distinta de la 1.2 |
| Rastros del entorno de trabajo | 347 archivos de texto revisados; 0 con rutas internas |
| Regeneración en una copia limpia | 26 pasos ejecutados con los guiones del paquete y las fuentes del autor; 349 archivos comparados, 0 diferencias |

La regresión comprueba que el paquete se regenera igual, que los archivos y los manifiestos cierran y que un conjunto de cifras clave aparece en los documentos. No comprueba que cada cifra de los documentos esté bien informada: eso lo leyó la verificación de cierre, en parte.

## 12. Cómo repetir la revisión

La revisión queda como práctica propuesta (ADR-027, a confirmar en D-14.7): antes de publicar una versión, revisores con contexto independiente leen una copia congelada.

1. Congelar la versión que se va a revisar.
2. Entregar a cada revisor su encargo (`revision_critica/<revisor>/ENCARGO.md`), el formato de los hallazgos y el extracto de las reglas (`revision_critica/comun/`).
3. Validar cada salida con el validador de `revision_critica/comun/`.
4. Integrar las segundas lecturas con la primera (`revision_critica/integrar.py`).
5. Escribir una decisión para cada hallazgo (`revision_critica/triaje/`).
6. Aplicar los ajustes y regenerar con los guiones de `scripts/`.
7. Hacer leer la versión corregida por revisores que no hayan participado, y recién entonces publicar.

Lo que una próxima revisión debería hacer distinto: usar revisores humanos donde importa el criterio profesional, hacer que el triaje lo lea alguien que no generó los artefactos, entregar los textos completos y no recortados, y sortear la muestra a ciegas sobre todo el corpus.

## 13. Archivos de esta versión

| Archivo | Contenido |
|---|---|
| `data/revision_critica.json` | Resumen de la revisión, con las cifras de este documento |
| `data/revision_critica_hallazgos.csv` | Los 364 hallazgos con su decisión |
| `data/cambios_1_1_a_1_2.csv` | Las 183 filas de cambios, con columnas para tu decisión |
| `data/decisiones_del_autor.json` | Tu mensaje, cómo se leyó y las decisiones D-01 a D-14 como proposiciones |
| `data/reglas_propuestas_D11.csv` y `data/reglas_propuestas_D11_enunciados.csv` | Las 18 reglas propuestas y sus 95 enunciados |
| `data/casos_sin_coincidencia_D13.csv` | Las fichas de los 11 casos de D20 sin coincidencia |
| `data/evidencia_por_preensayo.csv` | Qué lecturas tuvo cada pre-ensayo y con qué resultado |
| `data/muestra_a_ciegas_1_2.csv` y `data/muestra_a_ciegas_1_2.json` | La muestra a ciegas, caso por caso y por estrato |
| `data/segunda_lectura_migraciones.csv` | La segunda lectura de las migraciones |
| `data/analisis_D20_decision_D03.csv` | Las dos lecturas de D20 y la resolución de cada caso |
| `data/revision_humana_muestra.csv`, `data/revision_humana_clave.csv` y `data/revision_humana_propuesta.json` | Muestra y regla de decisión propuestas para la revisión humana |
| `data/equivalencias_biblioteca_corpus.csv`, `data/biblioteca_grupos_mismo_concepto.csv`, `data/biblioteca_dobletes_internos.csv` y `data/biblioteca_defectos_senalados.csv` | Insumos de la decisión D-12 |
| `data/observaciones_catalogo_ciso365.csv` | Observaciones sobre el catálogo de indicadores |
| `data/solicitud_cambio_ontologia_OCR-CAND-03.json` | Propuestas para la próxima revisión de la ontología |
| `data/casos_de_navegacion.json` | Casos de navegación resueltos con el corpus |
| `revision_critica/` | Encargos, insumos, veredictos, hallazgos y notas de cierre de cada revisor; en `revision_critica/cierre/`, la verificación de cierre |
| `anexos/A7_Revision_critica_verificacion_externa.md` | Los tres informes de verificación externa |
| `anexos/A8_Revision_critica_encargos_y_cierres.md` | Los encargos y las notas de cierre, reunidos |

# Decisiones de arquitectura, bitácora, glosario y continuidad · versión 1.4

**Frontier CISO Atlas 1.4** · Taxonomía 6.1 (reglas de asignación, revisión 3) · Ontología 2.2.0 (propuesta) · GM-24 V7.1 · 16 de noviembre de 2026 · Estado: respuestas del autor registradas de forma literal; lo que decidió el curador en esta versión espera su confirmación (D-16); corpus releído por lectores automáticos con una vara de tres lecturas, que el curador endureció después de leer; contenido candidato, sin validación humana

Este documento suma a los documentos 08, 09 y 10, que se conservan como registro de la versión 1.3, lo que corresponde a la versión 1.4: las decisiones de arquitectura ADR-032 a ADR-041, la bitácora de lo que se hizo, los términos nuevos y cómo retomar el trabajo.

## 1. Decisiones de arquitectura

Las ADR-001 a ADR-031 están en `docs/08_Decisiones_de_Arquitectura.md`. Dos cambiaron de estado: ADR-030, Aceptada (D-15.4). Su condición de confianza es «ninguna lectura declara confianza baja». En la versión 1.4 el curador aplicó una más estricta (ADR-033), después de ver los resultados; cuál vale lo decide el autor en D-16.2 y ADR-031, Aceptada (D-15.5).

### ADR-032 · Criterio de mayor rigor

**Estado.** Lectura del curador de una frase del autor; a confirmar en D-16.1 y D-16.14.

**Decisión.** El autor respondió tres líneas con la frase «Procede con la decision de mayor rigurosidad», que alcanzan cuatro asuntos, y no definió qué es esa rigurosidad. El curador leyó la frase como una delegación y escribió un criterio antes de decidir, con seis partes en orden de precedencia: (a) fidelidad a la fuente, (b) coherencia con lo ya decidido, (c) una regla, todos los casos, (d) prueba que puede fallar, (e) parsimonia, (f) si nada decide, no cambia. El texto de cada parte está en la taxonomía y en el documento 16, sección 3.1.

**Cómo se revierte.** Si el autor cambia un criterio o su orden, se revisan las decisiones que se apoyan en él: cada regla decidida declara qué criterios usó (data/reglas_de_asignacion_rev3.csv).

### ADR-033 · Vara de tres lecturas para cambiar una coordenada

**Estado.** Decisión del curador sobre una línea que leyó como delegada; la relectura se confirma en D-16.20 y la vara la elige el autor en D-16.2.

**Decisión.** Los cambios que la versión 1.3 había aplicado no se dieron por buenos. La base es la coordenada de la versión 1.2. Todo el corpus se volvió a leer con las reglas revisión 3: dos lecturas a ciegas completas, con repartos distintos y en carpetas separadas, y una tercera lectura de elección entre dos valores. Un eje cambia solo si las dos lecturas coinciden en un valor distinto del de la base, las dos declaran confianza alta en ese eje, ninguna de las dos anota un vacío declarado de ese eje y la tercera lectura, que no sabe cuál es el valor vigente, prefiere el nuevo. Los 37 cambios de la versión 1.2 que el autor confirmó quedan protegidos. Excepción: en los pre-ensayos que tenían RC04, cuyo alcance cambió, vale el valor en que coinciden dos lecturas, con cualquier confianza. Esa excepción se escribió cinco minutos después de lanzar las lecturas, cuando ningún lector había entregado todavía una salida; hasta entonces esos pre-ensayos seguían la vara. La cronología de lo que se escribió antes de leer y de lo que cambió después está en relectura_1_4/vara/LEEME.md; es la declaración del curador, tomada del registro de su sesión de trabajo, que no viaja en el paquete. Antes de lanzar la lectura, dos revisores leyeron las reglas y se corrigieron los defectos que encontraron. La condición de la confianza se endureció después de leer. La vara fijada antes de leer decía «ninguna de las dos declara confianza baja», que es la condición de ADR-030, confirmada por el autor en D-15.4; con ella habrían cambiado 480 coordenadas en 338 pre-ensayos. El curador la cambió al ver los resultados. Lo que vio: las tres lecturas son corridas del mismo lector automático, de modo que la coincidencia y la tercera lectura casi no filtran (la tercera prefirió el valor nuevo en 470 de 494 candidatos); y en 381 de esos cambios alguna lectura declaró confianza media, que según el encargo quiere decir que una regla decide pero otro código se puede defender. En 240 de ellos el código que alguna lectura anota como defendible es el valor vigente; en 141, no. El curador eligió conservar el valor vigente, que en la mayoría de los casos es el que el pre-ensayo traía en el banco del autor, salvo donde el lector no ve otra lectura defendible. Es la opción más conservadora, no una opción demostrada. La revisión de la versión candidata mostró cinco cosas que el autor tiene que saber para elegir. Primera: la condición reemplazada es una que el autor había confirmado, de modo que el criterio de coherencia con lo decidido juega para los dos lados. Segunda: el criterio «si nada decide, no cambia» no cubre la confianza media, porque ahí una regla decide. Tercera: la etiqueta de confianza no es estable entre corridas del mismo lector: en las dos tandas que se leyeron dos veces cambió en 12 de 48 ejes con el mismo código, y entre las lecturas A y B coincide en el 85,3 % de los ejes con el mismo código. Cuarta: no cambiar también puede ser un error: en 594 coordenadas del corpus las dos lecturas coinciden en un valor distinto del que se publica. Quinta: los 37 ejes que el autor confirmó no sirven para elegir entre las varas: la tercera lectura no se corrió sobre ellos, el autor los confirmó en bloque y en ese conjunto cualquier vara más estricta sale mejor. Cambiar la vara después de leer contradice la regla de trabajo de esta versión. La vara fijada queda calculada, sin aplicar, y la elección es del autor (D-16.2).

**Cómo se revierte.** Las alternativas están calculadas: cada una es una lista de cambios ya escrita. La vara fijada antes de leer: las listas «corpus» y «apx» de scripts/datos_de_trabajo/ajustes_relectura_1_4_vara_fijada_antes_de_leer.json. La categorización de la versión 1.3: las de scripts/datos_de_trabajo/v13/ajustes_relectura_1_3.json. La de la versión 1.2: las listas vacías. Con esas listas en scripts/datos_de_trabajo/ajustes_relectura_1_4.json, merge_clasif.py y propuestas_editoriales.py dejan el corpus y la serie APX con esa categorización: está probado en la regresión para las tres. El resto del paquete no se regenera con otra alternativa: el resumen de la relectura, la muestra de la revisión humana, el registro de decisiones y los documentos describen la vara aplicada, y los dos primeros se detienen con un aviso. Aplicar otra alternativa es armar una versión nueva, sin volver a leer; lo hace el curador. Las opciones de las versiones 1.2 y 1.3 deshacen también los diez cambios de RC04 a ID06: si el autor confirma D-16.3, esas diez entradas se conservan en la lista. La lista de la versión 1.3 trae APC-122 con el dominio D20, que contradice un cambio que el autor confirmó (D17): esa entrada se quita.

### ADR-034 · Taxonomía 6.1

**Estado.** Decisiones del curador de distinto origen; a confirmar en D-16.3 a D-16.6, D-16.15, D-16.16, D-16.18 y D-16.21.

**Decisión.** El catálogo cambia en cuatro puntos y ninguno retira ni reutiliza un código: subfunción nueva ID06 «Mejora continua y lecciones aprendidas»; RC04 pasa a «Lecciones y cierre de la recuperación»; H04 deja de ser un horizonte y pasa a ser el marcador de convergencia; INH11 pasa a «Volumen de alertas y de decisiones». Quedan 8 territorios, 28 dominios, 6 funciones y 35 subfunciones. Las reglas de asignación pasan a su revisión 3: 24 reglas decididas (RD-01 a RD-24) y 15 vacíos declarados.

**Cómo se revierte.** No es un parámetro: hay que tocar varios guiones. Cada cambio de catálogo está definido en scripts/reglas_1_4.py o scripts/modelo_1_4.py. Lo aplica al catálogo scripts/taxonomia_6_1.py, que trae la lista «cambios_de_catalogo» y retira H04 de los horizontes. scripts/merge_clasif.py tiene fija la función de ID06 y la conversión de H04 en marcador. scripts/extraer_medicion.py tiene la asignación de cuatro indicadores a ID06. Revertir ID06 y RC04 exige además volver a leer los pre-ensayos que cambiaron por el nuevo alcance.

### ADR-035 · El MCCS es la biblioteca metacognitiva

**Estado.** Registro de una declaración del autor; la consecuencia se confirma en D-16.13.

**Decisión.** El autor declaró que el MCCS son los 1.404 elementos de su biblioteca. El Atlas lo define así. La lente de cuatro pilares (ADR-017) se conserva como la forma en que el Atlas proyecta el MCCS sobre los pre-ensayos; las anclas de MM y OS se derivan de los territorios que traen los elementos de la biblioteca. DO y NX no tienen elementos: queda una pregunta para el autor (D-17.1).

**Cómo se revierte.** Volver a las anclas de la Taxonomía 6.0: están conservadas en el campo anclas_6_0 de cada pilar.

### ADR-036 · Modelo de equilibrio del eje H, revisión 2

**Estado.** Resultado de un encargo que el autor aprobó; a confirmar en D-16.7.

**Decisión.** El contexto es un parámetro de la organización, con un valor de una escala; la fuerza es una causa de cambio que el texto nombra; los mecanismos no son fuerzas. Cada vínculo «presiona» declara el término (demanda o capacidad) y el sentido; cada «regula», el papel del mecanismo (referencia, sensor, decisor o efector). Las cinco fuerzas que no presionaban ninguna variable quedan vinculadas con seis vínculos nuevos. Los factores HX01 a HX07 tienen escala. Se evaluaron dos variables nuevas y quedan propuestas, sin admitir.

**Cómo se revierte.** El modelo está en scripts/modelo_1_4.py; la tabla de la Taxonomía 6.0 se conserva en data/taxonomia_v6_0.json.

### ADR-037 · Criterios de admisión de dominios, revisión 2

**Estado.** Resultado de un encargo que el autor aprobó; a confirmar en D-16.8.

**Decisión.** C1 define qué es un artefacto independiente y qué es primer nivel en cada norma. C2 tiene una prueba que se calcula sobre el cruce de elementos y dominios. C3 se mide sin contar migraciones. C4 declara qué evidencia está verificada. La completitud pasa a ser el criterio C6. Los nueve candidatos tienen la misma tabla que los admitidos. Ningún dominio se admite ni se retira con estos criterios en esta versión.

**Cómo se revierte.** Volver a los cinco criterios de la Taxonomía 6.0, que se conservan en el bloque de decisiones del catálogo.

### ADR-038 · Lentes y planos

**Estado.** Resultado de dos encargos que el autor aprobó y de dos preguntas; a confirmar en D-16.6 y D-16.9.

**Decisión.** La lente de la agenda de IA se deriva de la coordenada con una regla por pilar (RD-21). El plano es una propiedad del nodo en los tipos que pertenecen a un plano. Un pre-ensayo que nombra un producto no pasa al plano B: queda marcado y fuera de la promoción a ensayo hasta que se reescriba (RD-22). Los elementos de la biblioteca no llevan dominio (RD-23). El aseguramiento como objeto lo expresa solo el dominio D28 (RD-24). Las cinco familias de dominios quedan definidas y ninguna regla las usa.

**Cómo se revierte.** Cada regla se revierte por separado; las derivaciones están en scripts/construir_grafo.py y scripts/modelo_1_4.py.

### ADR-039 · Ontología 2.2.0

**Estado.** Aprobada por el autor como solicitud (OCR-CAND-03); la forma en que se implementó se confirma en D-16.10.

**Decisión.** El autor aprobó la solicitud de cambio OCR-CAND-03. La propuesta 2.2.0 aplica sus dieciséis propuestas, y ocho quedaron aplicadas en parte (documento 17, sección 4.1): 86 tipos, 98 relaciones y 42 reglas. La solicitud dejaba una alternativa abierta en cinco propuestas (las número 2, 3, 12, 13 y 15), que eligió el curador, y en dos (la 6 y la 7) el curador agregó algo que la solicitud no pedía. Además hay decisiones de implementación que son del curador: la regla que reconoce un estado por la primera palabra de su definición (14 elementos de la biblioteca), la carga de las 112 equivalencias entre la biblioteca y el corpus como candidatas de una lectura, y el vínculo de cada tarea de autonomía L2 o superior con el punto de control de su agente.

**Cómo se revierte.** Volver a la propuesta 2.1.0: los cambios están en un bloque aparte de scripts/build_ontology.py.

### ADR-040 · Revisión humana: diseño completo

**Estado.** Decisión del curador sobre una línea que leyó como delegada; a confirmar en D-16.11.

**Decisión.** Entre el camino mínimo y el diseño completo, se toma el diseño completo: 193 pre-ensayos en 4 estratos, con un margen de 6,4 puntos para la estimación ponderada. La revisión la hace el autor o quien él designe; los umbrales los fija él antes de abrir la clave. El curador no la hace.

**Cómo se revierte.** El camino mínimo es la tanda 1 de la misma muestra: no hay que volver a sortear.

### ADR-041 · El candidato W02 como dominio D29

**Estado.** Pregunta para el autor (D-17.2); no aplicada.

**Decisión.** Con los criterios revisión 2, la gestión de activos, configuración y cambios cumple los cinco criterios (C1 a C5). C3 se cumple en el límite: las dos lecturas anotan el vacío de este candidato en 10 pre-ensayos y el umbral es 10; con uno menos no cumpliría. Una sola lectura lo anota en 2 más. De esos 10 pre-ensayos, 2 (M2.1-K01 y M2.1-K03) tienen un dominio que el autor confirmó el 16 de noviembre de 2026: sin ellos la medida es 8 y C3 no se cumple; el candidato quedaría «admisible con reserva». En la Taxonomía 6.0, que el autor confirmó, este candidato figuraba como «no cumple C2». El resultado cambió porque el curador reescribió el criterio en la revisión 2, no porque haya cambiado el respaldo. No se admite en esta versión porque el cambio de catálogo no se le había planteado al autor con esa opción. La medida depende de que los lectores anoten un vacío, que es un instrumento ruidoso.

**Cómo se revierte.** No hay nada que revertir: no se aplicó.

## 2. Bitácora de la versión 1.4

Las tareas están en el orden en que se hicieron. Lo que hicieron los agentes auxiliares está en `relectura_1_4/` y en `revision_1_4/`.

| N.º | Tarea | Qué se hizo | Resultado |
|---|---|---|---|
| 1 | Registrar las respuestas del autor | Se guardó el mensaje literal y la respuesta a la que contesta, y se separó lo literal de lo delegado. | Tres respuestas literales y tres delegaciones. Lo delegado no figura en los campos del autor. |
| 2 | Comparar las dos ediciones de la biblioteca que adjuntó el autor | Se compararon con la base cargada, identificador por identificador. | La de 1.404 coincide con la base; la de 1.356 está contenida. No hubo nada que cargar. La biblioteca no se revisó. |
| 3 | Escribir el criterio de mayor rigor | Seis partes en orden de precedencia, escritas antes de decidir (ADR-032). | Es una lectura del curador de la frase del autor; queda para confirmar en D-16.1. |
| 4 | Decidir los seis puntos de la revisión y las once preguntas | Se escribieron 24 reglas decididas, 15 vacíos declarados y las definiciones de trabajo de 35 subfunciones, con las citas de NIST CSF 2.0 verificadas en la fuente. | Taxonomía 6.1, con cuatro cambios de catálogo. Decisiones delegadas, a confirmar en D-16.3 a D-16.6. |
| 5 | Verificar las ediciones anteriores de cinco artefactos | Un agente consultó las páginas de los organismos emisores para el criterio C4 del candidato W02. | 4 de 5 artefactos quedaron con las dos ediciones verificadas abriendo el documento oficial: NIST CSF, NIST SP 800-53, CIS Controls y C2M2. ISO/IEC 27002 no quedó verificada en ninguna de las dos ediciones: iso.org en directo solo muestra el resumen y la muestra con el índice exige aceptar los términos de uso de ISO; los nombres («8 Asset management» en 2013; «5.9 Inventory of information and other associated assets», 5.10 y 5.11 en 2022) los leí únicamente en el texto de esa muestra oficial que devuelve el buscador. Salvedad de nivel: el elemento es de primer nivel en SP 800-53 (familia), CIS (control), C2M2 (dominio) e ISO/IEC 27002:2013 (cláusula 8, según el índice visto); no lo es en el CSF (categoría bajo la función Identify, en la 1.1 y en la 2.0) ni en ISO/IEC 27002:2022 (controles dentro de la cláusula 5). En CIS, entre la v7.1 y la v8.1 el Control 1 pasa de «Hardware Assets» a «Enterprise Assets» y la configuración segura pasa del Control 5 al 4. «Abierto» significa: texto que la herramienta de lectura web devolvió para la URL oficial el 2026-11-16. |
| 6 | Ejecutar los encargos en cola | Modelo del eje H revisión 2, criterios de admisión revisión 2 con la misma tabla para los nueve candidatos, lentes y planos. | 21 encargos ejecutados. Dos propuestas no se aplican y quedan para el autor: el candidato W02 y las variables HV07 y HV08. |
| 7 | Revisar las reglas antes de leer | Dos revisores: uno contrastó las reglas con 123 patrones de los lectores de la versión 1.3; el otro clasificó una muestra piloto de 30 pre-ensayos. | 45 contradicciones anotadas y 69 hallazgos del piloto. Se corrigieron las reglas, los vacíos, las definiciones y el encargo. La corrección no tuvo una segunda revisión. |
| 8 | Leer el corpus dos veces a ciegas | 38 lotes: dos lecturas completas de 755 pre-ensayos, con repartos distintos y en carpetas separadas. | Los 38 lotes pasaron la validación. Las dos lecturas coinciden en el 94,0 % de los territorios, el 95,0 % de los dominios y el 93,1 % de las subfunciones. |
| 9 | Comprobar si las lecturas son independientes | Se compararon los motivos, las confianzas, las reglas citadas y los secundarios de las dos lecturas, lote por lote. | Ningún motivo idéntico y 1 con similitud mayor a 0,90. Sin señales de copia. El acuerdo se informa como lo que es: dos corridas del mismo lector. |
| 10 | Registrar la escala del pilar OS | Dos lecturas completas de 147 pre-ensayos. | Coinciden en 137: 2 a escala individual, 75 de oficina y 60 en que la tesis no trata ninguna de las dos; 10 sin determinar. |
| 11 | Hacer la tercera lectura | 556 casos en 14 lotes: el lector elige entre dos valores sin saber cuál es el vigente. | En los candidatos a cambiar prefirió el valor nuevo en 470, el de la base en 15, dijo que valen los dos en 9 y no eligió ninguno en 0. |
| 12 | Integrar con la vara de tres lecturas | Se integró primero con la vara fijada antes de leer. Al ver que admitía cambios en que el propio lector veía otra lectura defendible, se exigió confianza alta en las dos lecturas. La vara fijada quedó calculada y sin aplicar. | Cambian 99 coordenadas primarias en 90 pre-ensayos. Con la vara fijada antes de leer habrían cambiado 480 en 338. De los 270 cambios de la versión 1.3, 39 se volvieron a derivar. En 737 ejes alguna lectura apunta a otro valor y el cambio no entró. |
| 13 | Aplicar la solicitud de cambio de la ontología | Las dieciséis propuestas de la solicitud OCR-CAND-03. | Propuesta 2.2.0: 86 tipos, 98 relaciones y 42 reglas. |
| 14 | Regenerar el corpus, el grafo y sus derivados | Corpus, taxonomía, biblioteca, medición, propuestas editoriales, grafo, consultas de aceptación, primera tanda y casos de navegación. | Grafo candidato de 5.059 nodos y 28.553 relaciones, con 0 errores y 80 advertencias de validación estructural. Preguntas de competencia: 7 respondibles, 9 en parte y 6 todavía no. |
| 15 | Preparar la revisión humana | Muestra sorteada sobre la categorización de esta versión, planilla a ciegas, clave aparte y guion de cálculo sin umbral por defecto. | 193 pre-ensayos en 4 estratos. No se ejecutó: la hace el autor. |
| 16 | Conservar la versión 1.3 como registro | Los documentos 01 a 14 se copiaron de la versión publicada, con una línea de aviso; los análisis de las versiones 1.2 y 1.3 no se recalcularon. | 14 documentos con aviso y 27 archivos de datos iguales a los publicados. |
| 17 | Documentar | Documentos 15 a 19, plan de la versión, README e instrucciones 7.4 del agente curador. | Cada cifra de los documentos se toma de los datos al generarlos. |
| 18 | Revisar la versión candidata | Seis revisores automáticos que no habían participado en la versión leyeron una copia congelada de la versión candidata (983 archivos), cada uno con una pregunta distinta. | Seis revisores automáticos que no habían participado en la versión leyeron una copia congelada de la versión candidata, cada uno con una pregunta distinta. Dejaron 128 hallazgos: 15 altos, 72 medios y 41 bajos. De ellos, 98 corregidos, 16 corregidos en parte y 14 documentados. Son revisores del mismo tipo que quien generó el paquete: encuentran contradicciones, cifras que no coinciden y afirmaciones sin respaldo, y no validan el contenido. |
| 19 | Comprobar el paquete | Regresión: manifiesto, archivos citados, cifras de los documentos contra los datos, registro histórico y regeneración en una copia. | 13 de 14 verificaciones sin diferencias. Las que fallan: Archivos citados en los documentos. |

### 2.1 Agentes auxiliares

El registro de la sesión guarda 85 pedidos de agentes auxiliares de esta versión: 8 de escala del pilar OS; 19 de lectura A; 27 de lectura B; 3 de notas de cierre de la versión 1.4; 2 de notas de los lectores de la versión 1.3; 8 de revisión de la versión candidata; 2 de revisión previa de las reglas; 14 de tercera lectura; 2 de verificación de ediciones. Seis pedidos de la lectura B fueron rechazados por el tope de agentes simultáneos y se repitieron después. En 4 pedidos el curador escribió una selección de modelo que el autor no pidió; esos agentes se detuvieron y se volvieron a encargar. Los demás se emitieron con los cinco campos; ocho lanzamientos de revisores se detuvieron por una lectura equivocada del registro y seis se retomaron (sección 2.2). Todos los agentes son automáticos y del mismo tipo que quien generó los artefactos.

### 2.2 Incidencias

- **La vara de la relectura se endureció después de leer.** El curador se había comprometido a fijarla antes de leer y a no cambiarla. La vara fijada admitía cambios en que alguna lectura declaraba confianza media, y habría cambiado 480 coordenadas en 338 pre-ensayos. Al ver los resultados, el curador exigió confianza alta en las dos lecturas: cambian 99 en 90. Las razones están en el documento 15, sección 3.1. El cambio va en el sentido de aplicar menos, y eso no lo hace seguro: no cambiar también puede ser un error. La vara fijada queda calculada aparte; aplicarla es una versión nueva. Es una desviación de lo comprometido, y la decisión entre las dos varas es del autor (D-16.2). Otra regla se tocó después de lanzar las lecturas: la de los pre-ensayos que tenían RC04 se reescribió cinco minutos después del lanzamiento, cuando ningún lector había entregado todavía una salida. La cronología, con horas, está en relectura_1_4/vara/LEEME.md.
- **Una selección de modelo que el autor no pidió, en 4 pedidos, y una lectura equivocada del registro.** Los agentes auxiliares se lanzan con cinco campos, y el autor no pidió ninguna selección de modelo. El registro de la sesión guarda 85 pedidos de agentes de esta versión. En 4 el curador escribió además un campo de modelo: el agente que verificó las ediciones anteriores de los marcos para el candidato W02, el lector del lote 14 de la lectura B, el lector del lote 15 de la lectura B y el agente que ordena las notas de cierre de la lectura A. Los 4 se detuvieron y se volvieron a encargar. El campo pedía el mismo modelo con que trabajan todos los agentes de la sesión: no hay motivo para pensar que el trabajo de esos agentes fuera distinto. En los otros 81 pedidos el curador emitió solo los cinco campos: el registro lo muestra en el mensaje emitido y en el pedido recibido. Después de ejecutar cada pedido, la plataforma informa los argumentos con el modelo agregado (79 de los 79 pedidos que llegaron a ejecutarse), y así es como el curador ve su propia llamada. Durante buena parte del trabajo el curador leyó ese agregado como si lo hubiera escrito él, y llegó a anotar que lo escribía en todos los pedidos. No era así.
- **Ocho lanzamientos de revisores detenidos por error.** Por esa misma lectura equivocada, el curador detuvo los 8 lanzamientos de revisores de la versión candidata entre 20 y 33 segundos después de arrancar (22:21 y 22:23 UTC). El registro muestra que los 8 se habían emitido con los cinco campos. Ninguno había escrito un archivo. Seis se retomaron a los cuatro minutos (22:27 UTC) y son los que hicieron la revisión; los otros dos, que eran una primera tanda de los revisores V1 y V2, quedaron descartados. Mientras tanto el curador le informó al autor, en el curso del trabajo, que la revisión quedaba frenada a la espera de una decisión suya; lo corrigió al encontrar la evidencia en el registro.
- **Dos tandas de lectura descartadas.** Los lectores de los lotes 14 y 15 de la lectura B habían escrito una tanda de 8 pre-ensayos cada uno cuando se detuvieron; el del lote 15 la escribió después de que se le pidió detenerse, porque el pedido le llegó al terminar ese paso. Las dos tandas no se usan: están en `relectura_1_4/incidencias/`, y los dos lotes se leyeron de nuevo desde cero. Se descartan para que los 38 lotes tengan un pedido registrado de la misma manera, y no porque se les haya encontrado un defecto.
- **La lectura B se lanzó en dos tiempos.** El entorno admite un número limitado de agentes a la vez. De los 19 lectores de la lectura B, 13 arrancaron junto con los de la lectura A y 6 pedidos fueron rechazados; esos lotes se lanzaron media hora después, cuando hubo lugar. Los lotes y las reglas eran los mismos.
- **Un movimiento de archivo que falló.** Al apartar la tanda descartada del lote 14, un movimiento entre carpetas dio un error de entrada y salida y la carpeta mostró por unos segundos un listado inconsistente. El archivo no se había movido. Se copió leyendo y escribiendo, se comprobó la huella de la copia y recién entonces se borró el original.
- **El tablero de tareas dio por cerrada una etapa que no lo estaba.** Al poner en curso otra tarea, el tablero marcó como terminada la lectura a ciegas cuando todavía faltaban lectores por cerrar. Se corrigió en el momento; la etapa se marcó como terminada cuando los 38 lotes estuvieron validados y cerrados.
- **Tres agentes no dejaron su archivo.** Los dos agentes que inventariaron los patrones de las notas de los lectores de la versión 1.3 cerraron su primer turno sin archivos, y los escribieron después de un mensaje que se lo pidió. El agente que verificó las ediciones de los marcos no pudo escribir el suyo: el curador lo guardó a partir de la respuesta del agente, sin cambios.
- **Un criterio que tenía el resultado escrito de antemano.** El guion que evalúa a los candidatos a dominio daba «no cumple C3» para el candidato W02 sin comparar la medida con el umbral. Apareció al ensayar la cadena con las lecturas reales: la medida es 10 y el umbral, que estaba escrito antes de medir, es «al menos 10». Se corrigió para que el sí o el no salgan de la medida, y con eso W02 cumple los cinco criterios, con C3 en el límite. Antes de esta corrección el curador lo había informado como «admisible con reserva».
- **Una afirmación de la entrega anterior que no se cumplió.** La entrega de la versión 1.3 decía que cada respuesta del autor aplicaría o descartaría los cambios frenados «sin volver a leer». Las reglas decididas cambian definiciones, y hubo que leer todo el corpus de nuevo.
- **El acuerdo entre las dos lecturas resultó mucho más alto de lo esperado.** Antes de seguir, el curador comprobó sobre las salidas si una lectura había copiado a la otra. No encontró señales de copia. El acuerdo se explica porque las dos son corridas del mismo lector con el mismo encargo, y así se informa: no se presenta como una medida de acierto. Diseñar la vara con tres lecturas del mismo lector fue un defecto de diseño: dos de sus cuatro condiciones casi no filtran.

## 3. Glosario de la versión 1.4

El glosario general está en `docs/10_Glosario_y_Continuidad.md`. Estos son los términos nuevos o que cambian:

| Término | Qué significa |
|---|---|
| Base de la relectura | La coordenada de la versión 1.2. Los cambios que aplicó la versión 1.3 no se dieron por buenos. |
| Biblioteca metacognitiva | La base de 1.404 elementos del autor: modelos mentales, sesgos cognitivos, mindsets y las demás categorías. En las versiones anteriores el paquete la llamaba «Biblioteca cognitiva». |
| Confianza alta, media y baja | Lo que declara el lector en cada eje. Alta: una regla o la definición decide y no ve otro código defendible. Media: una regla o la definición decide, pero otro código se puede defender. Baja: ninguna regla decide, dos reglas chocan o el eje depende de un vacío. |
| Criterio de mayor rigor | Las seis partes, en orden de precedencia, con que el curador decidió lo delegado: fidelidad a la fuente, coherencia con lo ya decidido, una regla para todos los casos, una prueba que puede fallar, parsimonia y, si nada decide, vacío declarado. Es una lectura del curador (ADR-032). |
| Decisión delegada | Decisión que tomó el curador después de que el autor respondió con una frase general («Procede con la decision de mayor rigurosidad»), sin definir esa rigurosidad. Que la frase sea una delegación es una lectura del curador, que el autor todavía no confirmó (D-16.14). Figura como decisión del curador, con criterio y justificación escritos, y espera la confirmación del autor (D-16). No todo lo que el curador decidió en esta versión sale de esa frase: una parte sale de los encargos que el autor aprobó, y otra la decidió por su cuenta. |
| Dominio en observación | Dominio vigente que no cumpliría el criterio C1 o el C3 si se evaluara hoy como candidato. No se retira ninguno. |
| Eje protegido | Eje de un pre-ensayo que la versión 1.2 cambió y que el autor confirmó. Una lectura en contra se informa y no se aplica. |
| Escala del pilar OS | Si la tesis de un pre-ensayo del pilar OS trata lo que sostiene la decisión de una persona (individual), el aparato con que decide la oficina (oficina) o ninguna de las dos. Es un dato del pre-ensayo; no cambia su coordenada. |
| Familia de dominios | Agrupación de los dominios por el tipo de objeto que nombra su definición. Es una ayuda de navegación: ninguna regla la usa. |
| Hueco de regulación | Papel que ningún mecanismo cumple para una variable. |
| Lectura A y lectura B | Las dos lecturas a ciegas completas del corpus, hechas con repartos distintos y en carpetas separadas. |
| Lente de cuatro pilares | MM, OS, DO y NX: la forma en que el Atlas proyecta el MCCS sobre los pre-ensayos. La biblioteca tiene elementos en MM y en OS. |
| Marcador de convergencia | H04. Dice si la tesis es la integración de disciplinas o de capacidades que antes iban separadas. Desde la Taxonomía 6.1 es un marcador aparte y no un horizonte. |
| MCCS | Metacognitive CISO System. Según el autor, los 1.404 elementos de su biblioteca metacognitiva, en once categorías. |
| Papel | En un vínculo «regula», lo que hace el mecanismo respecto de la variable: referencia, sensor, decisor o efector. |
| Registro histórico | Los documentos 01 a 14 y los análisis de las versiones 1.2 y 1.3, que la versión 1.4 conserva tal como se publicaron y no recalcula. |
| Regla decidida (RD) | Regla de asignación que escribió el curador. Van de RD-01 a RD-24. RD-01 a RD-14 y RD-20 a RD-24 resuelven un punto abierto o una pregunta que el autor dejó en manos del curador. RD-15 a RD-19 no resuelven nada de eso: precisan enunciados que el autor había adoptado, las decidió el curador por su cuenta y, al leer, prevalecen sobre esos enunciados (D-16.15). |
| Tercera lectura | Lectura de elección forzada: el lector recibe dos valores en orden sorteado, sin saber cuál es el vigente, y dice cuál prefiere, si valen los dos o si no vale ninguno. |
| Término y sentido | En un vínculo «presiona», el término de la variable sobre el que actúa la fuerza (demanda o capacidad) y si lo aumenta o lo reduce. |
| Vacío declarado (VC) | Caso para el que se sabe que ninguna regla decide. Cuando una lectura anota uno, el eje que depende de él no cambia. Van de VC-01 a VC-15. |
| Vara de tres lecturas | La regla con que un eje cambia en la versión 1.4: dos lecturas a ciegas coinciden en un valor distinto del de la base, las dos declaran confianza alta, ninguna anota un vacío de ese eje, y una tercera lectura, que no sabe cuál es el valor vigente, prefiere el nuevo (ADR-033). Las tres son corridas del mismo lector automático. |
| Vara fijada antes de leer | La versión de la vara que se escribió antes de la lectura: en lugar de exigir confianza alta, pedía que ninguna lectura declarara confianza baja, y admitía la confianza media. No se aplicó. Sus cambios están calculados en un archivo aparte. Aplicarlos es una versión nueva: hay que rehacer el resumen de la relectura, la muestra de la revisión humana y los documentos. |

## 4. Continuidad

### 4.1 Cómo retomar

1. Leer `docs/15_Decisiones_delegadas_y_relectura_1_4.md`: dice qué está decidido, qué espera al autor y en qué orden.
2. Registrar las respuestas del autor a D-16 en `scripts/decisiones_1_4.py`, de forma literal, y regenerar.
3. Si el autor rechaza una regla decidida, mirar en `data/reglas_de_asignacion_rev3.csv` cuántos ejes cambiaron citándola y en `data/relectura_1_4_por_eje.csv` cuáles son.
4. Si el autor hace la revisión humana, calcular el resultado con `scripts/evaluar_revision_humana.py` sobre la copia de la planilla en que anotó, y registrar el umbral que fijó. La planilla anotada se guarda fuera de la carpeta `data/`: regenerar el paquete vuelve a escribir la del paquete.
5. No tocar las versiones publicadas: cada versión nueva va en una carpeta nueva.

### 4.2 Cómo cambiar de vara o revertir la relectura

No es un paso. El archivo de cambios se reemplaza en un paso, pero lo que sigue es una versión nueva.

Las alternativas están calculadas: cada una es una lista de cambios ya escrita. La vara fijada antes de leer: las listas «corpus» y «apx» de scripts/datos_de_trabajo/ajustes_relectura_1_4_vara_fijada_antes_de_leer.json. La categorización de la versión 1.3: las de scripts/datos_de_trabajo/v13/ajustes_relectura_1_3.json. La de la versión 1.2: las listas vacías. Con esas listas en scripts/datos_de_trabajo/ajustes_relectura_1_4.json, merge_clasif.py y propuestas_editoriales.py dejan el corpus y la serie APX con esa categorización: está probado en la regresión para las tres. El resto del paquete no se regenera con otra alternativa: el resumen de la relectura, la muestra de la revisión humana, el registro de decisiones y los documentos describen la vara aplicada, y los dos primeros se detienen con un aviso. Aplicar otra alternativa es armar una versión nueva, sin volver a leer; lo hace el curador. Las opciones de las versiones 1.2 y 1.3 deshacen también los diez cambios de RC04 a ID06: si el autor confirma D-16.3, esas diez entradas se conservan en la lista. La lista de la versión 1.3 trae APC-122 con el dominio D20, que contradice un cambio que el autor confirmó (D17): esa entrada se quita. Después se ejecuta el orden de regeneración desde `merge_clasif.py`.

### 4.3 Orden de regeneración

Hay un solo orden, el mismo que trae `scripts/LEEME.md`. Se ejecuta desde la carpeta `scripts/`.

| Orden | Guion | Produce | Necesita además del paquete | Variable de entorno |
|---|---|---|---|---|
| 1 | `congelar_1_3.py` | Registro histórico: los documentos 01 a 14 de la versión 1.3 con su línea de aviso, y la comprobación de que los datos históricos son los publicados | — | — |
| 2 | `build_ontology.py` | Diccionarios de la propuesta de ontología 2.2.0 | Los cuatro diccionarios de la ontología 1.0.0 del AI CISO Atlas (`ontology.json`, `entity_dictionary.json`, `relationship_dictionary.json` y `semantic_rules.json`) | `FCA_FUENTES` |
| 3 | `merge_clasif.py` | Corpus categorizado y estadísticas, con los ajustes de la revisión 1.2 y los de la relectura 1.4 | — | — |
| 4 | `build_taxonomy.py` | Taxonomía 6.1: catálogo, reglas de asignación revisión 3, vacíos declarados, definiciones de las subfunciones, modelo del eje H, criterios de admisión y cruces (usa `fca_model.py`, `cruces.py`, `reglas_adoptadas.py`, `reglas_1_4.py`, `vacios_1_4.py`, `modelo_1_4.py` y `taxonomia_6_1.py`) | — | — |
| 5 | `build_reference.py` | Base de referencia | — | — |
| 6 | `extraer_biblioteca.py` | Extracto de la biblioteca metacognitiva (MCCS), con tipos, pilar, cobertura y prácticas contra sesgos | `Base_1404_Atlas_GM24.json` y `Cruce_editorial_72_GM24.json`, de la carpeta de integración de la biblioteca | `FCA_BIBLIOTECA` |
| 7 | `extraer_medicion.py` | Indicadores del catálogo CISO 365 2.0 ubicados en el Atlas y sus vínculos con las variables homeostáticas | Los catálogos de indicadores 1.2 y del Modelo Operativo CISO 365 2.0 (JSON) | `FCA_FUENTES` |
| 8 | `propuestas_editoriales.py` | Remapeo propuesto, lectura de D20 y serie APX | — | — |
| 9 | `construir_grafo.py` | Grafo candidato, validación y conjuntos de cambios | La matriz consolidada de preguntas (CSV) | `FCA_FUENTES` |
| 10 | `consultas_de_aceptacion.py` | Preguntas de competencia y su resultado | — | — |
| 11 | `primera_tanda.py` | Primera tanda de ensayos propuesta | — | — |
| 12 | `comparar_control.py 12` | Comparación de la muestra de control | — | — |
| 13 | `casos_de_navegacion.py` | Casos de navegación resueltos | — | — |
| 14 | `relectura_1_4.py` | Resumen de la relectura del corpus con la vara de tres lecturas, casos para el autor, qué pasó con los cambios de la versión 1.3 y cambios de la 1.3 a la 1.4 | — | — |
| 15 | `muestra_revision_humana.py` | Muestra, planilla y regla de decisión de la revisión humana | — | — |
| 16 | `decisiones_1_4.py` | Registro de decisiones: respuestas literales del autor, decisiones delegadas con la forma de revertirlas y lo que queda en sus manos | — | — |
| 17 | `docgen/` | Documentos 15 a 19, plan de la versión, README e instrucciones del agente curador | — | — |

13 de los 17 pasos no necesitan nada más que el paquete. Los otros 4 leen fuentes del autor que no viajan aquí; sus resultados ya están en el paquete.

Guiones fuera del orden:

| Guion | Para qué sirve |
|---|---|
| `evaluar_revision_humana.py` | Calcula el resultado de la revisión humana a partir de la planilla completada y de la clave. Lo ejecuta el autor al terminar la revisión; el umbral se pasa por parámetro y se fija antes de abrir la clave |
| `reglas_1_4.py` | Criterio de mayor rigor, reglas decididas (RD-01 a RD-24), definiciones de las subfunciones y estado de los 95 enunciados. No se ejecuta: lo lee `build_taxonomy.py` |
| `vacios_1_4.py` | Los vacíos declarados (VC-01 a VC-15). No se ejecuta: lo lee `reglas_1_4.py` |
| `modelo_1_4.py` | Modelo del eje H revisión 2, criterios de admisión revisión 2, MCCS, lentes y planos. No se ejecuta: lo leen `build_taxonomy.py` y `construir_grafo.py` |
| `taxonomia_6_1.py` | Aplica a la taxonomía los cambios de la versión 6.1. No se ejecuta: lo lee `build_taxonomy.py` |
| `reglas_adoptadas.py` | Estado de los 95 enunciados de las reglas después de la decisión del autor del 16-nov-2026 (versión 1.3). No se ejecuta: lo leen `build_taxonomy.py` y `reglas_1_4.py` |
| `build_corpus.py` | Corpus unificado (`datos_de_trabajo/corpus_unificado_raw.json`). Sirve para volver a extraer si cambian las fuentes |
| `corregir_extracto_agentes.py` | Catálogo de agentes del GM-24 con los campos en su lugar; con el paquete del GM-24 lo comprueba contra los anexos |
| `prep_batches.py` | Lotes de clasificación de la versión 1.0 (`clasificacion/lote_N.jsonl`). Es el registro de cómo se armaron: volver a ejecutarlo los sobrescribe y no hace falta para regenerar el paquete |
| `regresion.py` | Comprueba el paquete: manifiesto, archivos citados, cifras clave de los documentos contra los datos, registro histórico de la versión 1.3 y, con las fuentes del autor, regeneración en una copia limpia |
| `orden.py` | Este orden de regeneración. No se ejecuta: lo leen el documento 19 y esta guía, para que no haya dos listas |

### 4.4 Lo que la versión 1.4 no recalcula

Los documentos 01 a 14 son los de la versión 1.3, byte a byte, precedidos por una línea de aviso. Los datos históricos y el material de las versiones anteriores son iguales a los publicados en la versión 1.3.

- Documentos con aviso: `01_Resumen_Ejecutivo.md`, `02_De_AI_CISO_Atlas_a_Frontier_CISO_Atlas.md`, `03_Taxonomia_6_0.md`, `04_Base_de_Referencia.md`, `05_Ontologia_2_1.md`, `06_Grafo_de_Conocimiento.md`, `07_Categorizacion_del_Corpus.md`, `08_Decisiones_de_Arquitectura.md`, `09_Bitacora_de_Tareas.md`, `10_Glosario_y_Continuidad.md`, `11_Iteracion_1_1.md`, `12_Ampliacion_Celdas_en_Blanco.md`, `13_Revision_critica_1_2.md`, `14_Decisiones_y_relectura_1_3.md`.
- Datos históricos: `analisis_D20_decision_D03.csv`, `analisis_D20_decision_D03.json`, `biblioteca_defectos_senalados.csv`, `biblioteca_dobletes_internos.csv`, `biblioteca_grupos_mismo_concepto.csv`, `cambios_1_1_a_1_2.csv`, `cambios_1_2_a_1_3.csv`, `cambios_1_2_a_1_3_resumen.json`, `casos_sin_coincidencia_D13.csv`, `equivalencias_biblioteca_corpus.csv`, `escala_del_pilar_OS_1_3.csv`, `evidencia_por_preensayo.csv`, `muestra_a_ciegas_1_2.csv`, `muestra_a_ciegas_1_2.json`, `muestra_de_control.json`, `observaciones_catalogo_ciso365.csv`, `preguntas_abiertas_1_3.csv`, `reglas_D11_hallazgos_de_la_muestra_complementaria.csv`, `relectura_1_3_casos_para_el_autor.csv`, `relectura_1_3_por_eje.csv`, `relectura_1_3_resumen.json`, `revision_critica.json`, `revision_critica_hallazgos.csv`, `segunda_lectura_migraciones.csv`, `solicitud_cambio_ontologia_OCR-CAND-03.json`, `taxonomia_v6_0.json`, `taxonomia_v6_0_catalogo.csv`.
- Carpetas que no cambian: `anexos/`, `relectura_1_3/`, `revision_1_3/`, `revision_critica/`.
- Guiones de las versiones anteriores que este paquete no trae: `revision_critica.py` (análisis de la revisión crítica de la versión 1.2); `relectura_1_3.py` (resumen de la relectura de la versión 1.3); `docgen/d01_02.py a docgen/d14.py` (generadores de los documentos 01 a 14). Están en el paquete de la versión 1.3.

### 4.5 Pendientes

- Las dos reglas para indicadores que el autor adoptó (RP-09.5 y RP-11.2) no se aplicaron todavía a los 224 indicadores del catálogo de medición.
- 8 indicadores (K81, K100, K101, K122, K131, K144, K166 y KX18) quedaron sin subfunción: su categoría de NIST CSF 2.0 corresponde ahora a dos subfunciones, ID05 e ID06, y la regla de derivación ya no elige. Conservan la función.
- La regla RD-20 (el liderazgo de personas y la gestión de equipos van al pilar MM; el diseño de la oficina, al pilar OS a escala de oficina) está decidida y no se aplicó a los pre-ensayos: el pilar no se releyó en esta versión.
- Las 112 equivalencias entre la biblioteca y el corpus que carga el grafo tienen una sola lectura.
- Los 15 vacíos declarados: casos para los que ninguna regla decide. Donde una de las dos lecturas a ciegas anota uno, el eje no cambia por la vara. La condición no mira la tercera lectura y no rige para los pre-ensayos que tenían RC04: hay 2 cambios aplicados con un vacío anotado por alguna lectura (documento 15, sección 4.2).
- Las reglas se corrigieron después de la revisión previa y esa corrección no tuvo una segunda revisión antes de la lectura.
- Los indicadores K59, K43 y K54, que un revisor de la versión 1.2 pidió revisar (tarea D-13.6), siguen sin revisar.
- La escala del pilar OS se registra en una planilla; el grafo no la carga.
- El pilar de los pre-ensayos no se releyó. La pasada de escala muestra que 60 de los 147 pre-ensayos del pilar OS no tratan ninguna de sus dos escalas según dos lecturas: su pilar queda en duda y no se cambió.
- Dos pre-ensayos del corpus citan el Atlas con cifras de una versión anterior: G2.1-K04 habla de 32 subfunciones y G2.1-K08, de los horizontes H01 a H04. El corpus es una fuente del autor y no se modificó.
- Los lectores señalaron en sus notas de cierre reglas que no deciden, choques entre reglas y casos sin regla que no están entre los vacíos declarados. Están ordenados en relectura_1_4/notas_de_cierre/ y no se incorporaron a las reglas en esta versión.
- Los documentos 01 a 14 no se actualizaron: se conservan como registro de la versión 1.3.
- No hay una regla para los ejes que las reglas atan (territorio y dominio, subfunción y dominio). En 35 de los 90 pre-ensayos que cambian, la coordenada que queda no es la de la versión 1.2 ni la que leyó ningún lector (data/relectura_1_4_ternas_mixtas.csv; D-17.9).
- La revisión de la versión candidata observó cinco reglas decididas que los lectores ya habían usado: RD-24 y RD-02 (caso a) se contradicen sobre T08 y D28; RD-03 no reparte la mejora como las citas que usa de ancla; RD-06 deja en GV04 lo que las citas ubican en la evaluación de riesgos; RD-15 y RD-17 modifican enunciados que el autor adoptó. No se cambiaron después de leer: la observación está en data/reglas_de_asignacion_rev3.csv, donde el autor decide cada regla.
- El vacío VC-11 dice que vale para los tres ejes y el catálogo le da el eje «dominio»: la condición de los vacíos solo lo mira en ese eje. En los datos de esta versión no cambia nada.
- La confianza que la planilla y el grafo traen junto a cada coordenada es la que declaró el clasificador de la versión 1.0. Las lecturas de la versión 1.4 no la reemplazaron; su confianza, eje por eje, está en data/relectura_1_4_por_eje.csv. La consulta P11 devuelve solo la confianza de la clasificación de dominio.
- La regla RD-21 nombra a los indicadores y no se les aplicó: la lente de la agenda de IA solo se deriva en los pre-ensayos. En las preguntas del banco, la lente es la de la matriz de origen, y no siempre coincide con la que daría la regla.
- La ontología 2.2.0 tiene ocho propuestas aplicadas en parte (documento 17, sección 4.1). Entre ellas: 61 pares de tipos admitidos en más de una relación no tienen criterio escrito; las equivalencias «mismo concepto» están cargadas sobre el pre-ensayo y no sobre su concepto; ninguna relación usa la confianza «sin evaluar»; la regla SV-119 solo mira los pre-ensayos; y 16 de 85 puntos de control quedan «sin clase declarada».
- Las listas alternativas de cambios (la categorización de la versión 1.2 y la de la 1.3) son anteriores al cambio de RC04: aplicadas tal cual, devuelven a RC04 los diez pre-ensayos de mejora continua, y la de la 1.3 trae además un cambio que contradice uno de los 37 que el autor confirmó. Elegir una de ellas en D-16.2 exige corregir eso antes.
- El grafo rotula con la Taxonomía 6.1 las coordenadas que los pre-ensayos heredan de versiones anteriores: los códigos son válidos en la 6.1, y la asignación no se hizo de nuevo con ella.
- El estado de cada pregunta de competencia sale de una prueba de cobertura y de un límite que el curador escribe en cada pregunta: dos salvedades de la misma clase pueden dar estados distintos según dónde se anotaron.
- Lo que se corrigió después de la revisión de la versión candidata no tuvo otra lectura independiente: lo comprueba solo la regresión.

### 4.6 Archivos respecto de la versión 1.3

El paquete tiene 1083 archivos. Respecto de la versión 1.3 (559 archivos): 445 iguales, 100 actualizados, 538 nuevos y 14 que solo están en esa versión. El detalle está en `data/archivos_por_version.csv`. Los conteos incluyen el manifiesto de cada versión, que siempre cambia. Se compara por ruta y por huella SHA-256.

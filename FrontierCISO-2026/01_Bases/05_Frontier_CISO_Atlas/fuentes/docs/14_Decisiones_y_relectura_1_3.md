> **Registro de la versión 1.3 (16 de noviembre de 2026).** Este documento se conserva tal como se publicó. Las cifras, los estados y los archivos que cita corresponden a esa versión. El estado vigente está en `docs/15_Decisiones_delegadas_y_relectura_1_4.md` y en los documentos 16 a 19.

# Frontier CISO Atlas 1.3 · Tus decisiones del 16 de noviembre y la relectura del corpus

**Frontier CISO Atlas 1.3** · Taxonomía 6.0 (reglas de asignación, revisión 2) · Ontología 2.1.0 · GM-24 V7.1 · 16 de noviembre de 2026 · Estado: decisiones de diseño confirmadas por el autor; reglas adoptadas según la lectura del curador y corpus releído a ciegas por lectores automáticos, con una lectura para todos y dos donde la primera difería; contenido candidato, sin validación humana

## 1. En una página

**Qué escribiste.** El 16 de noviembre de 2026 respondiste con cuatro frases: «Confirmo las siete.», «Acepto el cambio de reglas», «Confirmo el resto de los cambios.» y «No revisar la biblioteca».

**Cómo se leyó.** La primera es literal: un «sí» a las siete proposiciones de la decisión D-14. Las otras tres son frases generales, y hubo que traducirlas a una respuesta por proposición. Quedan marcadas como lectura del curador, para que las corrijas si no es lo que quisiste decir. No mencionaste la revisión humana de la categorización. Los cambios que la versión 1.2 hizo en el corpus (D-13.1 y D-13.2) se leyeron como sin respuesta, y eso también es una lectura (sección 2.2).

**Qué se hizo.** Se registraron tus respuestas. Las reglas que aceptaste entraron a la taxonomía: 60 enunciados con texto listo quedaron adoptados, 11 preguntas siguen abiertas porque una aceptación no las contesta, y de los 24 encargos de trabajo, 3 se hicieron en esta versión y 21 quedan en cola. El corpus se releyó a ciegas con las reglas adoptadas. Se corrigió un defecto de la versión 1.2 publicada. Antes de publicar, revisores que no habían participado leyeron la versión candidata, como pide ADR-027, que confirmaste. Lo que encontraron cambió esta versión (sección 10).

**Qué cambió.** Cambiaron 260 coordenadas primarias en 204 de los 739 pre-ensayos del corpus (27,6 %): 96 territorios, 87 dominios y 77 subfunciones. En la serie APX cambiaron 10 coordenadas en 8 de sus 16 pre-ensayos. Un eje cambia solo si las dos lecturas coinciden entre sí, difieren del valor vigente, ninguna anotó una pregunta abierta que afecte a ese eje, ninguna declaró confianza baja y el cambio no cae en uno de los 6 puntos que la revisión de la versión candidata dejó abiertos. No se aplicaron 312 casos en que las lecturas apuntan fuera de la coordenada vigente: 154 que caen en un punto que la revisión dejó abierto, 99 en que coinciden pero una declaró confianza baja, 22 frenados por una pregunta abierta y 37 en que las dos difieren de la vigente y entre sí. En otros 116, una lectura difiere y la otra sostiene la coordenada vigente.

**Qué frenó la revisión.** Antes de esa revisión la relectura cambiaba 414 coordenadas en 294 pre-ensayos del corpus. Los revisores encontraron en las reglas adoptadas 6 puntos sin decidir: una pregunta que se entregó recortada a los lectores, fronteras entre subfunciones que las propias definiciones declaran abiertas, una regla que se te había presentado como una que no mueve coordenadas, dos pares de reglas que se contradicen y una serie en que el encargo de los lectores hizo tomar como tesis la primera oración y no la tesis que el texto declara. Los 154 cambios que dependen de esos puntos se retiraron y quedan a tu decisión.

**Qué queda en tus manos.** Primero, decir si las lecturas de tus tres frases son las que quisiste (decisión D-15, sección 2.4). Después, contestar los 6 puntos que dejó abiertos la revisión y las 11 preguntas de las reglas, decidir si los cambios aplicados quedan, que se pueden revertir enteros en un paso, y hacer la revisión humana de una muestra, que sigue sin hacerse. La sección 7 lo ordena en 6 pasos. Los 312 casos en que el cambio no entró están en `data/relectura_1_3_casos_para_el_autor.csv`, con una columna para tu decisión.

**Qué sigue igual.** Nada de esto tiene validación humana. Las dos lecturas son automáticas y tienen la misma configuración que quien generó los artefactos: que coincidan hace menos probable un desliz y no dice nada de un error que compartan. La relectura es el cambio más grande que tuvo la categorización, y lo decidieron dos lecturas automáticas con reglas adoptadas ese mismo día.

## 2. Tu mensaje: qué dice, cómo se leyó y qué cubre

Tus palabras, tal como las escribiste:

> «Confirmo las siete.»
> «Acepto el cambio de reglas»
> «Confirmo el resto de los cambios.»
> «No revisar la biblioteca»

| Frase | Cómo se leyó |
|---|---|
| «Confirmo las siete.» | Respuesta «sí» a las siete proposiciones de la decisión D-14. Es literal. |
| «Acepto el cambio de reglas» | Adopción de las 18 reglas propuestas (D-11), las que cambian coordenadas y las que no. Es una lectura: la frase no nombra reglas ni enunciados. Vale para lo que era regla con texto listo; las preguntas siguen abiertas y los encargos quedan aceptados. Queda para confirmar en D-15.1. |
| «Confirmo el resto de los cambios.» | Confirmación en bloque de D-13.3, D-13.4 y D-13.5. Es una lectura: la frase repite el paso 4 de la lista que se le presentó al autor, que no incluía los cambios del corpus (estaban en el paso 3). La otra lectura posible, que la frase confirma toda la decisión D-13, queda planteada en D-15.2. |
| «No revisar la biblioteca» | Cierre de la decisión D-12 sin revisión de la Biblioteca. Es una lectura: se tradujo a una consecuencia por proposición, que el autor no eligió una por una. Queda para confirmar en D-15.3. |

### 2.1 Respuesta por proposición

De las 21 proposiciones y tareas de las decisiones D-11 a D-14, 7 tienen una respuesta literal, 10 una respuesta leída de una frase general, 2 se leyeron como sin respuesta y 2 son tareas. En el registro (`data/decisiones_del_autor.json`), el campo `decision_del_autor` lleva solo lo que respondiste de forma literal, y `nota_del_autor` quedó vacío: los dos son tuyos. Lo que leyó el curador está en `lectura_del_curador` y en `nota_del_curador`.

| N.º | Proposición | Respuesta del autor | Lectura del curador | Clase | Nota del curador |
|---|---|---|---|---|---|
| D-14.1 | La aceptación en bloque de D-01 a D-10 vale aunque su condición se cumplió en parte: las diez decisiones chocaban en cuatro puntos, de los que dos se resolvieron, uno se… | sí | — | literal | — |
| D-14.2 | D-03 era una pregunta. Se confirma el «sí»: el gobierno, el riesgo y el cumplimiento de la IA que estaban alojados en D20 pasan a D01, D02 o D03. | sí | — | literal | — |
| D-14.3 | D-10 pedía «decidir sobre las propuestas editoriales». Se confirman las dos lecturas: (a) la propuesta de remapeo es el pedido para la próxima versión del GM-24, y (b)… | sí | — | literal | La proposición tiene partes y el «sí» las alcanza a todas: (a) sí; (b) sí. |
| D-14.4 | D-01 se confirma con la advertencia a la vista: el nombre coincide con un concepto comercial de un proveedor y con el nombre de una de sus suites, y 77 pre-ensayos del… | sí | — | literal | — |
| D-14.5 | «Propone una forma de implementar […] informa y continua» se leyó como autorización para ejecutar la revisión crítica y la mejora sin una consulta intermedia, y así se… | sí | — | literal | — |
| D-14.6 | ADR-029 redacta el principio que enunciaste: el Atlas funciona como guía y orientación; quien lo usa lee con atención, no cree nada por defecto, contrasta con su… | sí | — | literal | — |
| D-14.7 | ADR-026 (qué efecto tiene la aceptación en bloque), ADR-027 (revisión crítica antes de publicar) y ADR-028 (vía de corrección de una coordenada heredada: dos lecturas o… | sí | — | literal | La proposición tiene partes y el «sí» las alcanza a todas: sí a ADR-026, ADR-027 y ADR-028, y a las instrucciones 7.2 del agente curador. ADR-027 queda vigente: la versión 1.3 también pasa por una revisión antes de publicarse. |
| D-11.1 | Reglas que cambian coordenadas ya asignadas (RP-01, RP-02, RP-03, RP-04, RP-05, RP-06, RP-07, RP-08, RP-09, RP-10, RP-12, RP-13, RP-18): adoptar, modificar o rechazar… | — | adoptar | lectura de una frase general | El autor no respondió enunciado por enunciado. De los 95 enunciados, 60 son reglas con texto listo y quedan adoptados; 11 son preguntas, que una aceptación no contesta, y siguen abiertas (RP-13 ofrece dos opciones que se excluyen), igual que la cláusula final de RP-10.6; 24 son encargos de trabajo, que quedan aceptados: 4 se hacen en la versión 1.3 y 20 quedan en cola. La clase de cada enunciado (regla, pregunta o encargo) la asignó la versión 1.2 de forma automática, por el verbo inicial, y la versión 1.3 la usó como criterio; el autor no la revisó. Tres enunciados adoptados dejan una disyuntiva que se resuelve por lectura (RP-04.6, RP-06.3 y RP-12.10). |
| D-11.2 | Reglas que aclaran un texto o tocan lentes, planos, el modelo del eje H o los criterios de admisión (las demás): adoptar, modificar o rechazar cada enunciado. | — | adoptar | lectura de una frase general | La frase no distingue las reglas que cambian coordenadas de las que no: se leyó como adopción de las 18. El autor no respondió enunciado por enunciado. De los 95 enunciados, 60 son reglas con texto listo y quedan adoptados; 11 son preguntas, que una aceptación no contesta, y siguen abiertas (RP-13 ofrece dos opciones que se excluyen), igual que la cláusula final de RP-10.6; 24 son encargos de trabajo, que quedan aceptados: 4 se hacen en la versión 1.3 y 20 quedan en cola. Las reglas de este grupo se le presentaron al autor como reglas que no mueven coordenadas. Una de ellas, RP-11.1, fija la subfunción primaria: los cambios que la citan quedaron frenados (punto RV-3) hasta que el autor confirme que se aplica a los primarios. |
| D-11.3 | Releer con las reglas adoptadas en D-11.1 los pre-ensayos que cada regla alcanza. | — | — | tarea | La relectura se hace en la versión 1.3, con dos lecturas a ciegas. |
| D-13.1 | Los 11 pre-ensayos de D20 en que las lecturas no coinciden (AMP-46, HC-010, APC-210, APC-212, APA-053, APA-068, APA-075, APA-108, APA-111, APA-113, APA-158): elegir el… | — | — | leído como sin respuesta | Leído como sin respuesta (ver D-13.2). La relectura de la versión 1.3 volvió a leer los once casos y cambió el dominio de algunos por la vía de ADR-028: el detalle está en data/relectura_1_3_resumen.json (clave los_11_casos_de_D20) y en el documento 14, sección 4.7. Lo que la versión 1.2 ofrecía como insumo (el estrato E1 de su muestra) ya no existe: lo reemplazan los archivos de la relectura. |
| D-13.2 | Los 37 cambios de coordenada del corpus: confirmar o revertir. | — | — | leído como sin respuesta | Es una lectura. La frase «el resto de los cambios» repite el paso 4 de la lista que se le presentó al autor (scripts/datos_de_trabajo/respuesta_presentada_al_autor_2026_11_16.md): «Confirmar o revertir el resto de los cambios (Biblioteca, medición, celdas en blanco y textos de la taxonomía)». En esa lista los 37 cambios del corpus y los once casos de D20 estaban en el paso 3, la revisión de la muestra, que el autor no mencionó. La otra lectura posible es que la frase responde a la decisión D-13 entera: si es esa, el autor lo dice en D-15.2 y los 37 cambios quedan confirmados. La relectura de la versión 1.3 volvió a cambiar algunos de los 37 (data/relectura_1_3_resumen.json, clave los_37_cambios_de_la_version_1_2). El estrato E1 de la muestra de la versión 1.2 ya no existe. |
| D-13.3 | Los cambios de la Biblioteca (86 filas): tipos de 81 conceptos, pilar OS de 59, territorios, cobertura y prácticas contra sesgos. | — | confirmar, en bloque | lectura de una frase general | — |
| D-13.4 | Los cambios de la medición (20 filas) y de la serie APX (22 filas): confirmar o revertir. | — | confirmar, en bloque | lectura de una frase general | — |
| D-13.5 | Los cambios de texto de la taxonomía (13 filas), de los cruces (4 filas) y de la propuesta de remapeo (1 fila): confirmar o revertir. | — | confirmar, en bloque | lectura de una frase general | — |
| D-13.6 | Los indicadores K59, K43 y K54, que un revisor pidió revisar sin proponer otra coordenada: revisarlos al leer el catálogo. | — | — | tarea | No es una decisión: es una revisión de tres indicadores. |
| D-12.1 | Los territorios de un concepto de la Biblioteca se derivan por lectura del concepto, y no por su categoría. | — | no | lectura de una frase general | Es la consecuencia de no revisar la Biblioteca, no una elección que el autor haya hecho sobre esta proposición. Los territorios siguen como propiedad del nodo, sin cargarse como clasificación. |
| D-12.2 | El pilar de las habilidades socioemocionales y de las mentalidades de resiliencia se asigna por lectura del concepto: OS a escala individual, DO o MM. | — | se quedan en MM | lectura de una frase general | Es la consecuencia de no revisar la Biblioteca, no una elección que el autor haya hecho sobre esta proposición. El autor no habló del pilar ni del choque entre D-04 y D-08: el choque queda como estaba, sin resolver. |
| D-12.3 | Las categorías de mentalidades y de prácticas de decisión se releen completas antes de fijar el tipo de sus conceptos. | — | no | lectura de una frase general | Es la consecuencia de no revisar la Biblioteca, no una elección que el autor haya hecho sobre esta proposición. Conservan el tipo por regla, con las excepciones ya aplicadas. |
| D-12.4 | Los 45 grupos de conceptos que nombran la misma idea y los 27 pares repetidos se resuelven en la base: fusionar, declarar equivalentes o dejar separados. | — | separados | lectura de una frase general | Es la consecuencia de no revisar la Biblioteca, no una elección que el autor haya hecho sobre esta proposición. Los 45 grupos y los 27 pares repetidos quedan como están en la base. |
| D-12.5 | Revisar por muestra los tipos y los territorios de la Biblioteca. | — | no se hace | lectura de una frase general | Es la consecuencia de no revisar la Biblioteca, no una elección que el autor haya hecho sobre esta proposición. La Biblioteca queda como base de trabajo sin revisar, y así se declara. |

### 2.2 Lo que quedó sin respuesta

- La revisión humana de una muestra de la categorización (paso 3 de la lista que se le presentó).
- D-13.1 y D-13.2, leídas como sin respuesta: los once casos de D20 y los 37 cambios de coordenada del corpus.
- La solicitud de cambio de la ontología OCR-CAND-03.
- Las preguntas abiertas de las reglas.

Que D-13.1 y D-13.2 quedaron sin respuesta es también una lectura. Se apoya en la respuesta que recibiste antes de escribir tu mensaje, que el paquete trae literal en `scripts/datos_de_trabajo/respuesta_presentada_al_autor_2026_11_16.md`. Su lista tenía cinco pasos, y tus cuatro frases siguen el 1, el 2, el 4 y el 5. El paso 4 decía «Confirmar o revertir el resto de los cambios (Biblioteca, medición, celdas en blanco y textos de la taxonomía)»; los 37 cambios del corpus y los once casos de D20 estaban en el paso 3, la revisión de la muestra. La otra lectura posible es que «el resto de los cambios» responde a toda la decisión D-13: si es esa, alcanza con que lo digas (D-15.2) y los 37 cambios quedan confirmados.

### 2.3 Qué cambia con tu confirmación

| Decisión | Estado en la versión 1.2 | Estado en la versión 1.3 |
|---|---|---|
| D-01 | Aceptada; a confirmar con la advertencia a la vista (D-14.4) | Aceptada, con la advertencia a la vista |
| D-03 | Interpretada como «sí» y aplicada; a confirmar por el autor (D-14.2) | Aceptada y aplicada |
| D-10 | Interpretada como «sí»; la serie APX se corrigió; a confirmar por el autor (D-14.3) | Aceptada |
| D-11 | Abierta; conviene decidir primero las reglas que cambian coordenadas | Abierta en parte: los enunciados con texto listo quedan adoptados (lectura del curador, a confirmar en D-15.1); siguen abiertas las preguntas y los puntos que dejó la revisión, y en cola parte de los encargos |
| D-12 | Abierta; no bloquea a las demás | Cerrada sin revisión: la Biblioteca queda como estaba (lectura del curador, a confirmar en D-15.3) |
| D-13 | Abierta; la parte del corpus se resuelve dentro de la revisión humana | Abierta en parte: los cambios de la Biblioteca, la medición, la serie APX y los textos se leyeron como confirmados en bloque (a confirmar en D-15.2); la parte del corpus (D-13.1 y D-13.2) se leyó como sin respuesta |
| D-14 | Abierta; es la primera que conviene decidir | Confirmada por el autor el 16 de noviembre de 2026 |

- Las decisiones ADR-026 a ADR-029 pasan de propuestas a aceptadas. Con ellas quedan vigentes las instrucciones del agente curador, que esta versión actualiza a la 7.3.
- ADR-027 obliga a revisar cada versión antes de publicarla. Esta también se revisó (sección 10).
- ADR-028 es la regla con la que la relectura cambia una coordenada: dos lecturas que coinciden en el destino. La relectura le sumó condiciones que no viste (ADR-030), y por eso figura en D-15.4.
- Tu confirmación no valida el contenido. Los conjuntos de cambios del grafo siguen en estado «propuesto» y el grafo sigue siendo candidato.
- De los cuatro choques entre decisiones que encontró la versión 1.2, el que seguía abierto (D-03 con D-10) dependía de la regla RP-01, que ahora está adoptada: quedó resuelto en parte, y la sección 4.8 muestra cómo. El choque entre D-04 y D-08 sigue sin resolver: cerraste D-12 sin revisar la Biblioteca y no hablaste de él.

### 2.4 Lo que te pido confirmar o corregir (decisión D-15)

En la versión 1.2, lo que el paquete había interpretado de tu mensaje no quedó firme hasta que lo confirmaste con la decisión D-14. Esta versión aplicó lo que leyó: tus tres frases contestan decisiones que ya se te habían presentado, y todo lo aplicado se revierte en un paso. Es un criterio distinto, y por eso va una decisión nueva que te pide lo mismo que la D-14: decir si cada lectura es la que quisiste. También lleva a confirmar las reglas de trabajo que esta versión puso a regir sin que las vieras.

| N.º | Qué se leyó o se puso a regir | Qué podés responder | Qué pasa si la respuesta es no |
|---|---|---|---|
| D-15.1 | «Acepto el cambio de reglas» se leyó como adopción de las 18 reglas propuestas, las que cambian coordenadas y las que no: quedan adoptados los 60 enunciados que tenían texto listo, siguen abiertas las preguntas y quedan aceptados los encargos. | sí / no | Los enunciados que el autor indique vuelven a «propuestos» y se retiran los cambios de la relectura que los citan. |
| D-15.2 | «Confirmo el resto de los cambios» se leyó como el paso 4 de la lista que se le presentó: los cambios de la Biblioteca, la medición, la serie APX y los textos (D-13.3 a D-13.5). No alcanza a los 37 cambios de coordenada del corpus ni a los once casos de D20 (D-13.1 y D-13.2), que en esa lista estaban en el paso 3. | sí / no: quise confirmar también los cambios del corpus | D-13.2 queda confirmada: los 37 cambios de la versión 1.2 quedan como están. D-13.1 pide elegir un dominio por caso y sigue abierta. |
| D-15.3 | «No revisar la biblioteca» se leyó como cierre de la decisión D-12. Sus cinco proposiciones quedan con la consecuencia de no revisar, que el autor no eligió una por una: los territorios no se releen, las habilidades socioemocionales y las mentalidades de resiliencia quedan en el pilar MM, los tipos no se releen, los grupos de conceptos repetidos quedan separados y no se hace la muestra. | sí / no | La proposición que el autor indique vuelve a quedar abierta. |
| D-15.4 | La regla con que la relectura decide un cambio (ADR-030) es más estricta que la que el autor confirmó (ADR-028): además de dos lecturas que coinciden, pide que ninguna declare confianza baja, que ninguna anote una pregunta abierta y que el cambio no caiga en un punto que la revisión de la versión candidata dejó abierto. Rige de forma provisoria. | sí / no | Vale ADR-028 sola: entran los cambios retenidos por confianza baja y los frenados. |
| D-15.5 | Los análisis de la versión 1.2 se conservan calculados sobre el corpus de esa versión (ADR-031) y las instrucciones del agente curador pasan a la versión 7.3. Rigen de forma provisoria. | sí / no | Los análisis se recalculan sobre el corpus vigente, o vuelven a regir las instrucciones 7.2, según lo que el autor indique. |
| D-15.6 | La relectura alcanzó a todo el corpus y usó todos los enunciados adoptados. La tarea D-11.3 hablaba de releer, con las reglas que cambian coordenadas, los pre-ensayos que cada regla alcanza. | sí / no | Se retiran los cambios que solo citan enunciados de las reglas que se habían presentado como las que no mueven coordenadas. |
| D-15.7 | Las 34 definiciones de trabajo de las subfunciones las redactó el curador (encargo RP-12.1) y los lectores las usaron. El autor no las vio. La mayoría de los cambios de subfunción que no citan un enunciado adoptado se apoyan en ellas. | confirmar / corregir las que indique | Se corrigen las definiciones y se releen las subfunciones que dependan de ellas. |

## 3. Las reglas adoptadas

La frase «Acepto el cambio de reglas» se leyó como adopción de las 18 reglas que proponía la revisión crítica (RP-01 a RP-18). Las 18 suman 95 enunciados de tres clases, y una aceptación no vale igual para las tres.

| Clase de enunciado | Enunciados | Qué pasa con ellos |
|---|---|---|
| Regla con texto listo | 60 | Quedan adoptados. Son las reglas de asignación, revisión 2 |
| Pregunta para el autor | 11 | Siguen abiertas: aceptar no elige entre opciones. Dos de los enunciados son las dos opciones de una misma pregunta (RP-13). También sigue abierta la cláusula final de RP-10.6. En total son 11 preguntas |
| Encargo de trabajo | 24 | Quedan aceptados: 3 se hicieron en esta versión y 21 quedan en cola |

| Regla | Tema | Adoptados | Preguntas abiertas | Encargos hechos | Encargos en cola |
|---|---|---|---|---|---|
| RP-01 | Precedencia general entre disciplina y objeto | 2 | — | — | — |
| RP-02 | Regla 6: cláusula de pilar y fronteras de D28 | 7 | — | — | — |
| RP-03 | La auditoría en D03 y en D28 | 2 | — | — | — |
| RP-04 | Regla 7: desempate, territorio y alcance | 7 | — | — | — |
| RP-05 | Regla 3: qué es un pilar y qué es un principio transversal | 5 | — | — | — |
| RP-06 | Regla 4: fronteras de D26 | 4 | — | — | — |
| RP-07 | Regla 5: fronteras de D27 | 4 | — | — | — |
| RP-08 | Inventario, activos, configuración y ciclo de vida de los controles | 3 | 1 | — | — |
| RP-09 | Territorios: de quién es la perspectiva y desempates | 7 | — | — | — |
| RP-10 | Regla 1: pruebas de aplicación | 8 | — | — | — |
| RP-11 | Regla 2: desempates de cardinalidad | 2 | — | — | — |
| RP-12 | Subfunciones: definición y delimitación | 9 | — | 1 | — |
| RP-13 | RC04 bajo la función Recuperar | — | 2 | — | — |
| RP-14 | Anclas del MCCS y escala del pilar OS | — | 1 | — | 2 |
| RP-15 | Eje H: completar el modelo de referencia | — | — | — | 9 |
| RP-16 | Criterios de admisión de dominios | — | — | — | 8 |
| RP-17 | Lentes y agrupaciones | — | 2 | — | 2 |
| RP-18 | Fronteras y alcances heredados | — | 5 | 2 | — |

El estado de cada enunciado está en `data/reglas_propuestas_D11_enunciados.csv`, columna `estado_1_3`. Las columnas `decision_del_autor` y `nota_del_autor` de ese archivo siguen vacías.

### 3.1 Qué cambió en la taxonomía

- **Nombre.** Taxonomía 6.0, reglas de asignación revisión 2. Los códigos, los catálogos y las cardinalidades no cambian: 8 territorios, 28 dominios, 6 funciones y 34 subfunciones.
- **Definición de D03.** Decía «Obligaciones aplicables, auditoría y conformidad». Ahora dice «Obligaciones aplicables y su conformidad, incluida la auditoría de conformidad con una obligación» (enunciado RP-03.1).
- **Reglas de asignación.** Las ocho reglas base siguen. Los 60 enunciados adoptados las precisan y, donde las precisan, prevalecen. Están en el documento 03.
- **Definiciones de las subfunciones.** Las 34 tienen ahora una definición de trabajo: qué incluye, qué excluye y, en 10 de ellas, qué frontera no decide ninguna regla adoptada. Las redactó el curador con el nombre, la categoría de CSF 2.0 y los enunciados adoptados. No las viste antes de que se usaran en la relectura.

### 3.2 Las preguntas que siguen abiertas

| Enunciado | Afecta a | Pregunta | Pre-ensayos que dependen de ella, según los lectores |
|---|---|---|---|
| RP-08.4 | dominio | ¿Dónde van el catálogo y el ciclo de vida de los controles: D01, D28 o un dominio nuevo (candidato W02)? | 29 |
| RP-14.3 | pilar MCCS | ¿En qué pilar van el liderazgo de personas y la gestión de equipos? | no se midió: es una pregunta de modelo |
| RP-17.1 | lente de IA | ¿A qué tipo de elemento se asigna la lente de la agenda de IA y con qué regla? | no se midió: es una pregunta de modelo |
| RP-17.4 | plano | Los pre-ensayos que desarrollan un producto de un proveedor, ¿pasan al plano B o se reescriben sin marca? | no se midió: es una pregunta de modelo |
| RP-18.2 | dominio | ¿Dónde está la frontera entre D18 y D19, o se consolidan? | 4 |
| RP-18.4 | dominio | ¿Dónde van la carga y la capacidad del equipo? | 9 |
| RP-18.5 | Biblioteca | ¿Los conceptos de la Biblioteca llevan dominio? | no se midió: es una pregunta de modelo |
| RP-18.6 | modelo | ¿Qué eje expresa el aseguramiento, que hoy se marca en cuatro (T08, D28, GV08 y HOM09)? | no se midió: es una pregunta de modelo |
| RP-18.7 | dominio | ¿En qué dominio va la automatización de seguridad que no usa IA? | 11 |
| RP-13 (dos opciones que se excluyen) | subfunción | ¿La mejora continua pasa a la función Identificar con un código nuevo y RC04 queda para las lecciones de la recuperación (RP-13.1, opción a), o se mantiene RC04 y el Atlas cuenta como recuperación el aprendizaje posterior al incidente (RP-13.2, opción b)? | 8 |
| RP-10.6 (cláusula final) | dominio | ¿En qué dominio va el catálogo de controles como modelo? | 15 |

Los lectores podían anotar seis de estas preguntas en un caso concreto, y lo hicieron en 64 pre-ensayos. Las demás son preguntas sobre el modelo y no se miden caso por caso. RP-13 ofrece dos opciones que se excluyen. Mientras no las contestes vale lo que estaba. El freno tiene tres límites: el lector solo podía anotar seis preguntas, cada una frena un solo eje, y depende de que el lector la haya visto. RP-13 se entregó además recortada, y por eso la cubre un punto de la revisión (sección 3.3). El archivo `data/preguntas_abiertas_1_3.csv` trae los identificadores y una columna para tu respuesta.

### 3.3 Los puntos que dejó abiertos la revisión de la versión candidata

La revisión de la versión candidata (sección 10) encontró en las reglas adoptadas 6 puntos sin decidir. No son preguntas que ya estuvieran planteadas: salieron de comparar los enunciados entre sí y con lo que los lectores escribieron en sus notas de cierre. Antes de esa revisión la relectura cambiaba 414 coordenadas en 294 pre-ensayos del corpus. Los revisores encontraron en las reglas adoptadas 6 puntos sin decidir: una pregunta que se entregó recortada a los lectores, fronteras entre subfunciones que las propias definiciones declaran abiertas, una regla que se te había presentado como una que no mueve coordenadas, dos pares de reglas que se contradicen y una serie en que el encargo de los lectores hizo tomar como tesis la primera oración y no la tesis que el texto declara. Los 154 cambios que dependen de esos puntos se retiraron y quedan a tu decisión.

| Punto | Eje | Qué falta decidir | Qué cambios frena | Cambios frenados |
|---|---|---|---|---|
| RV-1 | subfunción | La pregunta RP-13 se entregó recortada a los lectores: el texto daba por incluido en RC04 el aprendizaje posterior al incidente, que es lo que propone la opción b. Falta que el autor elija entre las dos opciones. | El valor vigente o el destino es RC04. | 5 |
| RV-2 | subfunción | Las definiciones de trabajo nombran esas fronteras como no decididas y el lector no tenía un código para anotarlas. Falta que el autor las fije. | El cambio cruza una frontera que las definiciones de trabajo declaran sin decidir: GV08 con ID05, GV03 con PR05, GV04 con ID04, PR02 con RC01, y GV02, GV10 y PR05 entre sí cuando el dominio es D24. | 20 |
| RV-3 | subfunción | RP-11.1 se le presentó al autor entre las reglas que no mueven coordenadas, con el efecto «aclara una regla; puede cambiar secundarios», y su texto fija la subfunción primaria. Falta que el autor confirme que se aplica a los primarios. | Alguna de las dos lecturas cita RP-11.1 para la subfunción. | 40 |
| RV-4 | territorio | RP-10.1 (prueba de sustitución) y RP-04.2 con RP-04.6 dan respuestas opuestas sobre el territorio de una tesis de gobierno o de riesgo de la IA, y RP-04.2 no dice cuándo una tesis «adopta otra perspectiva». Falta el orden entre esas reglas. | El valor vigente o el destino es T07. | 63 |
| RV-5 | dominio | RP-02.2 deja la prueba o la medición de una capacidad con dominio propio en el dominio de esa capacidad; RP-01.1, RP-03.2 y RP-04.4 la llevan a D28; y RP-02.1 choca con RP-02.2 cuando la tesis mide una capacidad y discute la medición. Falta la precedencia. | El valor vigente o el destino es D28. | 11 |
| RV-6 | los tres ejes | El encargo de los lectores extendió a todo registro sin el campo de tesis una regla que se adoptó solo para la serie K (RP-10.2): tomar como tesis la primera oración y el título. En la serie AMP el texto declara su tesis más abajo. Falta que el autor diga qué texto manda, o releer la serie con la tesis declarada. | El pre-ensayo es de la serie AMP. | 15 |
| Total |  |  |  | 154 |

Cada punto es una pregunta para vos. Si la contestás, los cambios que frenó se aplican o se descartan según la respuesta, sin volver a leer. Los identificadores están en `data/preguntas_abiertas_1_3.csv` y cada caso, con las dos lecturas, en `data/relectura_1_3_casos_para_el_autor.csv` (columna `punto_de_la_revision`).

El criterio de cada punto es deliberadamente ancho: frena todo cambio que toca el valor en discusión, cite o no la regla. Se eligió así porque los lectores no citan las reglas de modo uniforme.

### 3.4 Los encargos

Hechos en esta versión:

| Enunciado | Encargo | Qué se hizo |
|---|---|---|
| RP-12.1 | Dar a cada subfunción una definición de una línea con lo que incluye y lo que excluye. | Hecho en la versión 1.3: 34 definiciones de trabajo, redactadas con el nombre, la categoría de CSF 2.0 y los enunciados adoptados; donde ninguna regla adoptada fija la frontera, la definición lo dice. Las redactó el curador y el autor no las vio (decisión D-15.7); la revisión de la versión candidata señaló que algunas se pisan sin criterio de desempate. |
| RP-18.1 | Aplicar al corpus, con una lectura dedicada, los ajustes de alcance de D09, D13, D17 y D24. | Hecho en la versión 1.3 con la relectura general y no con una lectura dedicada, como pedía el encargo: los lectores recibieron los alcances ajustados de D09, D13, D17 y D24. El efecto en esos cuatro dominios está en el documento 14, sección 3.4. |
| RP-18.3 | Revisar el alojamiento en D10 de los pre-ensayos de red antes de tratar a D08 como espacio en blanco. | Hecho en la versión 1.3 con la relectura general: los pre-ensayos de red alojados en D10 se volvieron a leer con el resto del corpus. |

En cola:

| Enunciado | Encargo | Por qué queda en cola |
|---|---|---|
| RP-14.1 | Derivar las anclas de los elementos de la definición de cada pilar. | trabajo de diseño sobre las anclas del MCCS |
| RP-14.2 | Registrar la escala, individual o de oficina, de cada pre-ensayo del pilar OS. | hecho en parte: la relectura registró la escala que vio cada lector, pero la mayoría de los pre-ensayos del pilar OS quedó sin escala y las dos lecturas no se conciliaron (documento 14, sección 4.9) |
| RP-15.1 | Vincular con una variable las cinco fuerzas que hoy no presionan ninguna o declararlas fuera del modelo. | trabajo de diseño sobre el modelo de referencia del eje H |
| RP-15.2 | Definir INH11 como causa (volumen de alertas y de decisiones) y no como el estado que mide HV05. | trabajo de diseño sobre el modelo de referencia del eje H |
| RP-15.3 | Dar a «presiona» el sentido del efecto y el término de la variable sobre el que actúa (demanda o capacidad). | trabajo de diseño sobre el modelo de referencia del eje H |
| RP-15.4 | Dar a «regula» el papel de cada mecanismo: referencia, sensor, decisor o efector. | trabajo de diseño sobre el modelo de referencia del eje H |
| RP-15.5 | Distinguir contexto (condición de partida medible) de fuerza (cambio en curso). | trabajo de diseño sobre el modelo de referencia del eje H |
| RP-15.6 | Separar la convergencia del horizonte o admitir dos valores. | trabajo de diseño sobre el modelo de referencia del eje H |
| RP-15.7 | Evaluar una variable de calidad de la decisión y otra de equilibrio económico del programa. | trabajo de diseño sobre el modelo de referencia del eje H |
| RP-15.8 | Fijar en el glosario si «fuerza» incluye a los mecanismos. | trabajo de diseño sobre el modelo de referencia del eje H |
| RP-15.9 | Dar valores a los factores de contexto HX01 a HX07. | trabajo de diseño sobre el modelo de referencia del eje H |
| RP-16.1 | Reescribir C2 con una prueba verificable y aplicarla del mismo modo a todos los candidatos. | trabajo de diseño sobre los criterios de admisión de dominios; puede reabrir la cantidad de dominios |
| RP-16.2 | Incorporar la completitud como criterio explícito o retirar el argumento. | trabajo de diseño sobre los criterios de admisión de dominios; puede reabrir la cantidad de dominios |
| RP-16.3 | Evaluar C3 y C4 sobre el mismo objeto. | trabajo de diseño sobre los criterios de admisión de dominios; puede reabrir la cantidad de dominios |
| RP-16.4 | Documentar la evidencia de C4. | trabajo de diseño sobre los criterios de admisión de dominios; puede reabrir la cantidad de dominios |
| RP-16.5 | Definir qué es un artefacto independiente y qué es «primer nivel» en cada norma. | trabajo de diseño sobre los criterios de admisión de dominios; puede reabrir la cantidad de dominios |
| RP-16.6 | Publicar para los nueve candidatos la misma tabla de cinco criterios que tienen los admitidos. | trabajo de diseño sobre los criterios de admisión de dominios; puede reabrir la cantidad de dominios |
| RP-16.7 | Agregar al cruce de territorios una prueba que pueda fallar, por ejemplo la proporción de elementos externos que necesitan dos o más territorios. | trabajo de diseño sobre los criterios de admisión de dominios; puede reabrir la cantidad de dominios |
| RP-16.8 | Medir C3 con un criterio que no dependa de la migración, por ejemplo los pre-ensayos cuya coordenada 5.3 los clasificadores marcaron como forzada. | trabajo de diseño sobre los criterios de admisión de dominios; puede reabrir la cantidad de dominios |
| RP-17.2 | Registrar el plano como propiedad del nodo. | incluye una decisión de alcance: a qué tipos de nodo se les registra el plano. Hoy lo llevan, como vínculo con la lente, los 755 pre-ensayos y los 7 productos-control, y como propiedad solo esos 7 |
| RP-17.3 | Definir las familias de dominios (Gobierno, Protección, Operaciones, Ecosistemas, Personas) y su criterio, o quitar el campo. | incluye una elección: definir las familias de dominios o quitar el campo |

Los encargos en cola son trabajo de diseño sobre el modelo: el eje H, los criterios de admisión de dominios, las anclas del MCCS y las familias de dominios. Quedaron fuera de esta versión para no mezclar, en una misma versión, una recategorización del corpus con un rediseño del modelo. Los que tocan los criterios de admisión pueden reabrir la cantidad de dominios.

## 4. La relectura del corpus

### 4.1 Cómo se hizo

- **Qué se leyó.** 755 pre-ensayos: los 739 del corpus y los 16 de la serie APX. Cada lector recibió el identificador, la serie, el título, la tesis y el texto completo, sin la coordenada vigente. La tarea D-11.3 hablaba de releer, con las reglas que cambian coordenadas, los pre-ensayos que cada regla alcanza; se releyó todo el corpus con todos los enunciados adoptados, porque el alcance de una regla de territorio o de dominio no se conoce sin leer el texto. Es una ampliación del alcance que no viste (D-15.6).
- **Con qué reglas.** La Taxonomía 6.0, las ocho reglas base, los 60 enunciados adoptados, las definiciones de trabajo de las subfunciones y seis preguntas abiertas que el lector podía anotar (`relectura_1_3/REGLAS.md`).
- **Primera lectura.** Los 755, en 19 lotes, con un lector automático por lote. Ningún lector vio el trabajo de otro.
- **Segunda lectura.** 483 pre-ensayos, en 13 lotes, con otros lectores: los 430 en que la primera lectura difiere de la coordenada vigente en algún eje, los 6 de la serie APX en que coincide y 47 de control, sorteados entre los que coinciden en los tres ejes.
- **Regla de decisión.** Un eje cambia solo si las dos lecturas coinciden entre sí, difieren del valor vigente, ninguna anotó una pregunta abierta que afecte a ese eje, ninguna declaró confianza baja y el cambio no cae en uno de los 6 puntos que la revisión de la versión candidata dejó abiertos. En cualquier otro caso el valor queda como estaba y el caso se informa. La condición de la confianza baja es más estricta que el mínimo de ADR-028: la agregó el curador con la primera lectura incompleta y antes de que existiera la segunda, para no ajustarla al resultado.
- **Secundarios.** Cuando cambia un primario, el valor anterior pasa a ser el primer secundario.
- **Después de la revisión.** La revisión de la versión candidata agregó una condición a la regla: un cambio no entra si cae en uno de los 6 puntos que dejó abiertos (sección 3.3). Antes de esa condición la relectura aplicaba 414 cambios en el corpus; con ella aplica 260.

Límites del método:

- Los lectores son agentes automáticos con la misma configuración que quien generó los artefactos. La lectura es a ciegas respecto de la coordenada vigente y de la otra lectura; no es un juicio independiente.
- Las definiciones de las subfunciones nombran fronteras sin decidir, pero el encargo no dio a los lectores un código para anotarlas. El freno por pregunta abierta no las cubre. Es una omisión del encargo, que no se corrigió a mitad de la lectura para no romper la comparación entre las dos.
- Los lectores no citan las reglas de modo uniforme. «Regla adoptada citada» es un indicio, no una atribución.
- **El texto no era del todo ciego.** Treinta registros de la serie K traen en su plantilla la oración «En el AI CISO Atlas, la idea puede clasificarse principalmente desde Gobierno…», que sugiere una función. Doce lectores lo señalaron en sus notas. No se quitó.
- **La tesis de la serie AMP.** El encargo decía que, si el campo de tesis venía vacío, la tesis era la primera oración con el título. Esa regla se adoptó solo para la serie K (RP-10.2). En 50 de los 52 registros de la serie AMP el campo llegó vacío y el texto declara su tesis más abajo. Los cambios de esa serie quedaron frenados (punto RV-6).
- **Las reglas que recibieron los lectores tenían defectos que ellos señalaron.** La regla base 8 no se podía aplicar al leer un pre-ensayo; RP-09.5 y RP-11.2 son reglas para indicadores; RP-10.6 figura a la vez como enunciado adoptado y como pregunta abierta; y dos preguntas llegaron sin una de sus opciones.
- **Los enunciados se clasificaron por su verbo inicial.** Qué enunciado es regla, pregunta o encargo lo decidió la versión 1.2 de forma automática y lo llamó orientativo; esta versión lo usó como criterio y solo revisó a mano RP-10.6. Tres enunciados adoptados dejan una disyuntiva que el lector resuelve por lectura: RP-04.6 («D06 o D09»), RP-06.3 («D06 o D11») y RP-12.10 («GV02 o GV03»).
- **Los cambios de subfunción descansan en las definiciones de trabajo.** De los 91 cambios aplicados en que ningún lector citó un enunciado adoptado, 46 son de subfunción, un eje sobre el que las reglas base no dicen nada. Se apoyan en las 34 definiciones que redactó el curador y que no viste (D-15.7). La revisión señaló además que algunas se pisan sin criterio de desempate (GV02, GV03 y GV10, entre otras).
- La segunda lectura se armó cuando cuatro lectores de la primera todavía podían corregir su salida. Al cerrar la primera, un pre-ensayo había pasado a diferir de la coordenada vigente y no estaba en la segunda: se leyó en un lote adicional, junto con siete de control.
- Un lector de la primera lectura declaró que listó una vez su carpeta de salida; el comando devolvió solo un número.
- En buena parte del corpus el texto es plantilla repetida, y la lectura se apoya en el título y en la primera oración.

### 4.2 La primera lectura frente a la coordenada vigente

| Eje | Coincide con la coordenada vigente | Parte |
|---|---|---|
| territorio | 511 de 755 | 67,7 % |
| dominio | 575 de 755 | 76,2 % |
| subfunción | 523 de 755 | 69,3 % |
| los tres ejes | 325 de 755 | 43,0 % |

La primera lectura difiere de la coordenada vigente en algún eje en 430 de los 755 pre-ensayos. Los lectores declararon confianza alta en 212 lecturas, media en 457 y baja en 86, y en 543 de las 755 anotaron otra opción defendible: las reglas adoptadas todavía dejan mucho sin decidir.

La muestra a ciegas de la versión 1.2 había estimado una coincidencia de 73 % en territorio, 86 % en dominio y 80 % en subfunción. Las cifras no se comparan de forma directa: aquella muestra era de 87 pre-ensayos, excluía D20 y las migraciones, y se leyó con las reglas base.

| Serie | Qué es | Pre-ensayos | La primera lectura difiere en algún eje | Cambian en la versión 1.3 | Parte que cambia |
|---|---|---|---|---|---|
| K | Concepto base del GM-24 | 245 | 110 | 64 | 26 % |
| APC | Pregunta que hace el CISO | 156 | 99 | 49 | 31 % |
| APA | Pregunta que le hacen al CISO | 111 | 79 | 38 | 34 % |
| AMP | Ampliación del GM-24 | 52 | 29 | 0 | 0 % |
| PA | Sub-plan PO-GAC | 42 | 18 | 9 | 21 % |
| APN | Productividad individual | 41 | 28 | 17 | 41 % |
| HC | Híbrido del GM-24 | 40 | 26 | 12 | 30 % |
| APS | Agenda de IA, temas vacíos | 28 | 16 | 7 | 25 % |
| APF | Agenda de IA 4.0 | 24 | 15 | 8 | 33 % |
| APX | Ampliación para celdas en blanco | 16 | 10 | 8 | 50 % |

### 4.3 Resultado por eje

Cada pre-ensayo tiene tres ejes primarios: son 2.265 resultados.

| Resultado | Territorio | Dominio | Subfunción | Total |
|---|---|---|---|---|
| Las dos lecturas coinciden con la vigente | 229 | 290 | 232 | 751 |
| La única lectura coincide con la vigente | 272 | 272 | 272 | 816 |
| **Cambia**: las dos coinciden en otro valor | 100 | 92 | 78 | 270 |
| Coinciden en otro valor, pero una declaró confianza baja: no cambia | 34 | 26 | 39 | 99 |
| Coinciden en otro valor, pero el caso depende de una pregunta abierta: no cambia | 0 | 21 | 1 | 22 |
| Coinciden en otro valor, pero el cambio cae en un punto que la revisión dejó abierto: no cambia | 65 | 20 | 69 | 154 |
| Una difiere y la otra sostiene la vigente: no cambia | 39 | 28 | 49 | 116 |
| Las dos difieren de la vigente y entre sí: no cambia | 16 | 6 | 15 | 37 |
| Total | 755 | 755 | 755 | 2265 |

### 4.4 Lo que cambió

Cambiaron 260 coordenadas primarias en 204 de los 739 pre-ensayos del corpus (27,6 %): 96 territorios, 87 dominios y 77 subfunciones. En la serie APX cambiaron 10 coordenadas en 8 de sus 16 pre-ensayos. De los pre-ensayos que cambiaron, contando la serie APX, 162 cambiaron en un eje, 42 en dos y 8 en los tres.

En 179 de los 270 ejes cambiados, alguno de los dos lectores citó un enunciado adoptado que decide una coordenada; en 91 ninguno lo hizo, y el cambio se apoya en las reglas base y en las definiciones. Esos 91 no salen de las reglas nuevas: salen de que dos lecturas a ciegas coinciden contra la coordenada heredada, que es lo que ADR-028 admite.

| Enunciado adoptado | Ejes cambiados en que algún lector lo citó |
|---|---|
| RP-09.1 | 33 |
| RP-04.1 | 29 |
| RP-09.3 | 27 |
| RP-10.1 | 24 |
| RP-01.1 | 18 |
| RP-10.5 | 16 |
| RP-12.5 | 14 |
| RP-09.6 | 11 |
| RP-04.6 | 10 |
| RP-02.3 | 9 |

Los movimientos de dominio más frecuentes:

| Dominio en la 1.2 | Dominio en la 1.3 | Pre-ensayos |
|---|---|---|
| D04 | D01 | 8 |
| D04 | D02 | 7 |
| D02 | D01 | 5 |
| D20 | D01 | 4 |
| D07 | D03 | 3 |
| D06 | D01 | 2 |
| D03 | D01 | 2 |
| D14 | D15 | 2 |
| D10 | D05 | 2 |
| D01 | D04 | 2 |

Cada cambio está en `data/cambios_1_2_a_1_3.csv`, y el resultado eje por eje, con las dos lecturas, en `data/relectura_1_3_por_eje.csv`. En el grafo, la arista primaria del eje cambiado lleva el respaldo de la versión 1.3, la menor de las dos confianzas declaradas y el valor anterior.

### 4.5 Lo que no se aplicó

| Por qué no cambió | Territorio | Dominio | Subfunción | Total |
|---|---|---|---|---|
| Coinciden en otro valor, pero una lectura declaró confianza baja | 34 | 26 | 39 | 99 |
| Coinciden en otro valor, pero el caso depende de una pregunta abierta | 0 | 21 | 1 | 22 |
| Coinciden en otro valor, pero el cambio cae en un punto que la revisión de la versión candidata dejó abierto | 65 | 20 | 69 | 154 |
| Las dos difieren de la vigente y entre sí | 16 | 6 | 15 | 37 |
| Una difiere y la otra sostiene la vigente | 39 | 28 | 49 | 116 |

De los frenados por una pregunta abierta, 16 tienen además una lectura con confianza baja: contestar la pregunta no alcanza para aplicarlos. Los cuatro primeros grupos, 312 casos, están en `data/relectura_1_3_casos_para_el_autor.csv`, con el motivo de cada lectura y una columna para tu decisión.

### 4.6 Cuánto coinciden las dos lecturas

En los 47 pre-ensayos de control, las dos lecturas coinciden en 45 territorios, 45 dominios y 45 subfunciones, y en los tres ejes en 41. En los 430 en que la primera lectura difiere de la coordenada vigente, coinciden en 377 territorios, 398 dominios y 369 subfunciones.

La muestra de control se sorteó entre los pre-ensayos en que la primera lectura coincide con la vigente en los tres ejes; los otros son, por construcción, los casos difíciles. Ninguna de las dos cifras estima el acuerdo en todo el corpus.

### 4.7 Los cambios de la versión 1.2 y los once casos de D20, vistos por la relectura

No contestaste la decisión D-13.2 (confirmar o revertir, uno por uno, los 37 cambios de coordenada de la versión 1.2). La relectura los volvió a leer a ciegas, y esto es lo que encontró:

| Qué dice la primera lectura sobre el eje que cambió en la 1.2 | Cambios |
|---|---|
| Coincide con el valor de la 1.2 | 33 |
| Da otro valor | 3 |
| Coincide con el valor anterior a la 1.2 | 1 |

| Resultado de ese eje en la versión 1.3 | Cambios |
|---|---|
| Las dos lecturas coinciden con la vigente | 18 |
| La única lectura coincide con la vigente | 15 |
| Coinciden en otro valor, pero el cambio cae en un punto que la revisión dejó abierto: no cambia | 1 |
| Cambia: las dos coinciden en otro valor | 1 |
| Coinciden en otro valor, pero una declaró confianza baja: no cambia | 1 |
| Una difiere y la otra sostiene la vigente: no cambia | 1 |

Tampoco contestaste D-13.1, sobre los once pre-ensayos de D20 en que las lecturas de la versión 1.2 no coincidían:

| Pre-ensayo | Título | Dominio en la 1.2 | Primera lectura | Segunda lectura | Resultado | Dominio en la 1.3 |
|---|---|---|---|---|---|---|
| AMP-46 | Trazabilidad de decisiones autónomas | D20 | D28 | D28 | Coinciden en otro valor, pero una declaró confianza baja: no cambia | D20 |
| HC-010 | Autonomía delegada y límites de acción | D20 | D01 | D01 | Cambia: las dos coinciden en otro valor | D01 |
| APC-210 | Umbrales de desempeño y aseguramiento para aprobar despliegues de IA | D20 | D01 | D01 | Cambia: las dos coinciden en otro valor | D01 |
| APC-212 | Compensación de mitigaciones adversariales sin garantía formal | D20 | D20 | D20 | Las dos lecturas coinciden con la vigente | D20 |
| APA-053 | Pruebas de agentes antes de producción y tras cada cambio | D20 | D28 | D28 | Coinciden en otro valor, pero el cambio cae en un punto que la revisión dejó abierto: no cambia | D20 |
| APA-068 | Inventario de sistemas de IA con impacto en clientes | D20 | D20 | — | La única lectura coincide con la vigente | D20 |
| APA-075 | Registro auditable de agentes en producción y sus permisos | D20 | D20 | D20 | Las dos lecturas coinciden con la vigente | D20 |
| APA-108 | Criterio de inclusión y completitud del inventario de IA | D20 | D20 | — | La única lectura coincide con la vigente | D20 |
| APA-111 | Expediente de aprobación para producción de sistemas de IA | D20 | D01 | D01 | Cambia: las dos coinciden en otro valor | D01 |
| APA-113 | Aseguramiento razonable frente a la manipulación de la IA | D20 | D28 | D28 | Coinciden en otro valor, pero una declaró confianza baja: no cambia | D20 |
| APA-158 | Cobertura y adaptación de controles ante riesgos de IA | D20 | D28 | D28 | Coinciden en otro valor, pero el caso depende de una pregunta abierta: no cambia | D20 |

### 4.8 La serie APX y el choque entre D-03 y D-10

La serie APX se escribió para llenar celdas en blanco: siete pre-ensayos para D19, cinco para D27 y cuatro para RC05. La regla 7 hace prevalecer la disciplina sobre el objeto y la serie aplicaba el criterio contrario; el choque dependía de RP-01, que ahora está adoptada.

| Pre-ensayo | Se escribió para | Territorio | Dominio | Subfunción | Sigue en su celda |
|---|---|---|---|---|---|
| APX-01 | D19 | T05 → T04 | D19 | ID01 | sí |
| APX-02 | D19 | T08 | D19 → D17 | GV09 | no |
| APX-03 | D19 | T05 | D19 | PR03 | sí |
| APX-04 | D19 | T04 | D19 | GV04 | sí |
| APX-05 | D19 | T06 | D19 → D14 | DE01 | no |
| APX-06 | D19 | T04 → T06 | D19 → D15 | RS01 | no |
| APX-07 | D19 | T05 | D19 → D12 | ID03 | no |
| APX-08 | D27 | T05 | D27 | PR06 | sí |
| APX-09 | D27 | T04 | D27 | PR06 | sí |
| APX-10 | D27 | T05 | D27 | PR02 → PR06 | sí |
| APX-11 | D27 | T08 | D27 | GV09 | sí |
| APX-12 | D27 | T06 → T05 | D27 | PR06 | sí |
| APX-13 | RC05 | T04 | D16 | RC05 | sí |
| APX-14 | RC05 | T08 | D16 | RC03 | no |
| APX-15 | RC05 | T08 | D15 | RC05 | sí |
| APX-16 | RC05 | T02 → T08 | D15 → D16 | RC05 | sí |

De los siete pre-ensayos que se escribieron para D19, 3 siguen en D19. En total, 4 de los 16 salen de la celda para la que se escribieron (APX-02, APX-05, APX-06 y APX-07): dejan de llenarla, y el archivo conserva la celda para la que se escribió cada uno. APX-14 ya había salido de la suya en la versión 1.2, por la revisión crítica. El choque queda resuelto por la regla adoptada y por la relectura, no por una decisión caso por caso.

### 4.9 La escala del pilar OS

De los 147 pre-ensayos del pilar OS (144 del corpus y 3 de la serie APX), la primera lectura registró escala individual en 2, de oficina en 39 y «no aplica» en 106: la mayoría quedó sin escala. El encargo RP-14.2 pedía registrarla en cada uno; quedó hecho en parte y sigue en cola. 92 tienen dos lecturas, que coinciden en 79. La escala sale de una lectura que no conoce el pilar asignado, y un lector informó que el criterio deja casos de borde: es un registro de trabajo, en `data/escala_del_pilar_OS_1_3.csv`, y no una clasificación.

### 4.10 Cómo queda el corpus

Por territorio:

| Territorio | Versión 1.2 | Versión 1.3 | Diferencia |
|---|---|---|---|
| T01 | 9 | 5 | -4 |
| T02 | 70 | 90 | +20 |
| T03 | 80 | 80 | 0 |
| T04 | 136 | 139 | +3 |
| T05 | 104 | 88 | -16 |
| T06 | 80 | 84 | +4 |
| T07 | 102 | 102 | 0 |
| T08 | 158 | 151 | -7 |

Por función:

| Función | Versión 1.2 | Versión 1.3 | Diferencia |
|---|---|---|---|
| DE | 34 | 31 | -3 |
| GV | 369 | 366 | -3 |
| ID | 100 | 115 | +15 |
| PR | 162 | 151 | -11 |
| RC | 29 | 28 | -1 |
| RS | 45 | 48 | +3 |

Los dominios que más cambian:

| Dominio | Versión 1.2 | Versión 1.3 | Diferencia |
|---|---|---|---|
| D01 | 98 | 126 | +28 |
| D04 | 63 | 52 | -11 |
| D02 | 85 | 94 | +9 |
| D07 | 16 | 7 | -9 |
| D06 | 26 | 20 | -6 |
| D17 | 33 | 28 | -5 |
| D21 | 16 | 11 | -5 |
| D15 | 38 | 42 | +4 |
| D24 | 47 | 43 | -4 |
| D25 | 14 | 18 | +4 |

Las celdas territorio × dominio vacías pasan de 132 a 136. Dominios sin pre-ensayos: D19. Subfunciones sin pre-ensayos: RC05.

## 5. El grafo candidato

El grafo tiene 5.058 nodos y 28.249 relaciones (en la versión 1.2, 5.058 y 28.142), en 16 conjuntos de cambios, todos en estado «propuesto». La validación contra la ontología da 0 errores y 77 advertencias, como en la versión 1.2 (0 y 77). De las 22 preguntas de competencia: 7 respondibles, 9 en parte y 6 no (en la versión 1.2: 7 respondibles, 9 en parte y 6 no).

**Errata de la versión 1.2.** En el grafo publicado con la versión 1.2, los 37 pre-ensayos cuya coordenada había cambiado tenían 394 aristas de clasificación además de la del valor que cambió (las de los ejes que no habían cambiado y las secundarias del eje que cambió), y las 394 declaraban en su método un cambio ocurrido en otro eje. La historia de cambios del pre-ensayo se copiaba al método de todas sus aristas. No afectaba ninguna coordenada ni ningún conteo, pero era procedencia equivocada. No lo detectaron los revisores de cierre de la versión 1.2 ni su regresión: apareció al probar esta versión. Se corrigió para los cambios de las dos versiones: las aristas de los ejes que no cambiaron llevan el método del clasificador, y la historia queda en el nodo. La versión 1.2 publicada no se modificó.

## 6. Qué cambió respecto de la versión 1.2

`data/cambios_1_2_a_1_3.csv` tiene 287 filas: 284 son cambios de un elemento y 3 resumen cambios hechos en bloque, que cubren 488 elementos. Trae dos columnas vacías para tu decisión.

| Ámbito | Filas |
|---|---|
| Corpus | 260 |
| Registro de decisiones | 11 |
| Serie APX | 10 |
| Taxonomía (reglas) | 3 |
| Grafo | 2 |
| Documentos | 1 |
| Total | 287 |

No cambiaron la Ontología 2.1.0, la Biblioteca cognitiva, la medición, la base de referencia ni la propuesta de remapeo. Los análisis de la versión 1.2 (la revisión crítica, la lectura de D20 y la propuesta de remapeo) se conservan calculados sobre el corpus de esa versión. Los documentos 11 y 13 y los planes anteriores se publican como estaban, con una nota.

## 7. Lo que queda en tus manos

### 7.1 En qué orden

| Paso | Qué | Por qué en ese lugar |
|---|---|---|
| 1 | D-15: confirmar o corregir cómo se leyeron tus tres frases generales y las reglas de trabajo que esta versión puso a regir. | Todo lo demás se apoya en esas lecturas. Si alguna no es la que quisiste, cambia lo que quedó adoptado, confirmado o cerrado. |
| 2 | Contestar los puntos que la revisión dejó abiertos (RV-1 a RV-5) y las preguntas abiertas de las reglas. | Cada respuesta destraba los cambios que ese punto frenó, sin volver a leer. |
| 3 | Decidir si los cambios que la relectura aplicó quedan: dejarlos, revertirlos enteros o revertir filas. | Es el cambio más grande de la versión 1.3 y se revierte en un paso. |
| 4 | La revisión humana de una muestra. | Es la única fuente de validación humana, y conviene hacerla sobre la categorización que quede después de los pasos 1 a 3. |
| 5 | D-13.1 y D-13.2: los once casos de D20 y los 37 cambios de coordenada de la versión 1.2. | La relectura trae evidencia nueva para decidirlos, y D-15.2 puede dejar contestada la segunda. |
| 6 | Los encargos en cola y la próxima revisión de la ontología (solicitud OCR-CAND-03). | Son trabajo de diseño y no bloquean lo anterior. |

### 7.2 Cómo revertir la relectura

- **Entera.** Los cambios entran desde un solo archivo, `scripts/datos_de_trabajo/ajustes_relectura_1_3.json`. Vaciando sus listas `corpus` y `apx` y ejecutando tres guiones (`merge_clasif.py`, `propuestas_editoriales.py` y `construir_grafo.py`), el corpus, la serie APX y el grafo vuelven a las coordenadas de la versión 1.2; la prueba de regresión lo comprueba. Los pasos que siguen en el orden de regeneración (el resumen de la relectura, la muestra para la revisión humana y los documentos) describen la relectura aplicada y no corren sobre el corpus revertido: los rehace el curador en la versión que publique la reversión. Las reglas adoptadas y el registro de tus decisiones no se tocan.
- **Por fila o por punto.** Anotando «revertir» en la columna `decision_del_autor` de `data/cambios_1_2_a_1_3.csv`, el curador quita esas entradas del archivo de ajustes y regenera. Al revés, contestando un punto de la revisión o una pregunta abierta (`data/preguntas_abiertas_1_3.csv`), el curador aplica o descarta los cambios que ese punto frenó.

### 7.3 La revisión humana propuesta

No respondiste sobre la revisión humana, así que sigue siendo una propuesta. La de la versión 1.2 (246 pre-ensayos en cinco estratos) se apoyaba en la evidencia de esa versión; esta la reemplaza, porque después de la relectura cada pre-ensayo tiene al menos una lectura a ciegas.

| Estrato | Qué es | Pre-ensayos | En la muestra | Margen del estrato |
|---|---|---|---|---|
| R1 | Cambió con la relectura: en algún eje, las dos lecturas a ciegas coincidieron en un valor distinto del que tenía | 204 | 51 | 12,0 puntos |
| R2 | Alguna lectura a ciegas apunta fuera de la coordenada vigente y el cambio no entró (no coinciden, una declaró confianza baja o el caso depende de una pregunta abierta) | 222 | 52 | 12,0 puntos |
| R3 | Las lecturas a ciegas coinciden con la coordenada vigente en los tres ejes | 313 | 56 | 12,0 puntos |

- **Cuánto lleva.** 5 minutos por pre-ensayo. Es un supuesto, no una medida: conviene cronometrar los primeros diez. El camino mínimo son 60 pre-ensayos, unas 5,0 horas, con un margen de 12,7 puntos para todo el corpus: detecta un problema grande y casi cualquier umbral queda «no concluyente». El diseño completo son 159 pre-ensayos, unas 13,2 horas, con un margen de 7,1 puntos.
- **Qué mide.** En qué parte de los pre-ensayos el revisor asigna el mismo primario que la coordenada vigente, por estrato y por eje. Y, en el estrato R1, si el revisor coincide con el valor nuevo, con el que tenía en la versión 1.2 o con ninguno: es la medida que dice si la relectura mejoró o empeoró lo que cambió.
- **Regla de decisión.** Los umbrales los fija el autor, antes de mirar la clave. Este paquete no propone valores. Con tres resultados: cumple, no cumple o no concluyente.
- **Archivos.** `data/revision_humana_muestra.csv` (sin identificadores ni coordenadas) y `data/revision_humana_clave.csv`. Conviene leer la muestra antes de abrir la clave y los archivos de la relectura.

## 8. Límites que siguen en pie

- Ningún contenido tiene validación humana.
- Las dos lecturas de la relectura son automáticas y comparten configuración con quien generó los artefactos. No hay una tasa de error medida.
- Quien armó la relectura también escribió las definiciones de las subfunciones, fijó la regla de decisión y redactó este documento.
- La relectura cambió coordenadas que venían del banco del autor. Que dos lecturas automáticas coincidan no prueba que el valor nuevo sea mejor que el anterior: eso lo mide la revisión humana, en el estrato R1.
- La lectura cubrió los tres ejes primarios. El horizonte, las fuerzas y el pilar del MCCS no se releyeron. Los lectores propusieron secundarios, pero no se usaron: los secundarios vigentes son los del clasificador, más el valor anterior de cada eje que cambió. En 6 cambios, al entrar ese valor salió por el tope de cardinalidad un secundario que ya estaba; el archivo de cambios lo dice en cada fila.
- Los indicadores, las preguntas de la matriz y la Biblioteca no se releyeron con las reglas adoptadas.
- Las reglas adoptadas tienen puntos sin decidir que esta versión no resuelve: los 6 que encontró la revisión (sección 3.3) y tres listas distintas de qué es un objeto «con dominio propio» (RP-01.1, RP-02.2 y RP-05.1). La taxonomía publicada conserva en D01 y D02 la condición «cuando X = T07», que el enunciado adoptado RP-04.2 niega: los lectores recibieron esos alcances sin la condición.
- El encargo RP-18.1 pedía una lectura dedicada de los alcances ajustados de D09, D13, D17 y D24, y se hizo con la relectura general. El resultado en esos cuatro dominios: D09 pasó de 11 a 8 pre-ensayos, D13 quedó en 16, D17 pasó de 33 a 28 pre-ensayos y D24 pasó de 47 a 43 pre-ensayos.
- La verificación «regeneración en una copia limpia» regenera el paquete sobre una copia del propio paquete. Al menos un archivo de datos (`data/predicados_editoriales.json`) se hereda de versiones anteriores y ningún guion lo crea. La versión 1.2 lo decía sin esa precisión.

## 9. Incidencias del proceso

- **Seis avisos de una selección de modelo que el registro no confirma.** Durante esta versión el curador le avisó seis veces al autor que los lanzamientos de agentes auxiliares llevaban una selección de modelo que él no había pedido. El registro de eventos de la sesión guarda los 42 lanzamientos de esta versión (19 lectores de la primera lectura, 13 de la segunda, 5 revisores que se cancelaron y 5 que hicieron la revisión), y los 42 llevan exactamente los cinco campos que admite la regla de este trabajo; ninguno lleva una selección de modelo. Los avisos se basaban en lo que el curador veía en el eco de sus llamadas. La regla escrita en la versión 1.2 era comprobar el registro antes de avisar; el curador lo consultó con un filtro mal hecho, no encontró los lanzamientos y le dijo al autor que el registro no los guardaba. Era falso, y se lo corrigió en el mismo turno, cuando lo comprobó bien.
- **Cinco revisores detenidos sin necesidad.** Por una de esas falsas alarmas, el curador les pidió a los cinco revisores recién lanzados que se detuvieran, cuando no habían escrito nada, y los relanzó en carpetas nuevas. La regla escrita era no detener agentes por esa señal.
- **El conteo de lanzamientos de la versión 1.2 se sostiene.** Esa versión informó 53 agentes, 13 de ellos con una configuración escrita por quien despachaba. El registro de toda la sesión muestra 113 lanzamientos y 13 con ese parámetro, todos anteriores a esta versión.
- **Tres lectores terminaron un turno sin escribir su salida.** El lector del lote adicional de la segunda lectura y los dos lectores de la tercera lectura cerraron su primer turno sin archivos. Los escribieron después de un mensaje que se lo pidió, y sus salidas pasaron la validación.
- **La segunda lectura se armó antes de que cerrara la primera.** Las 755 lecturas estaban en disco y validadas, pero cuatro lectores todavía podían corregir su salida, y lo hicieron. Al cerrar la primera lectura, un pre-ensayo (APC-066) había pasado a diferir de la coordenada vigente y no estaba en la segunda. Se leyó en un lote adicional, con siete pre-ensayos de control más.
- **Un lector listó la carpeta de salidas.** El del lote 04 de la primera lectura declaró en su cierre que ejecutó un listado de esa carpeta para contar sus archivos. El encargo pedía no abrir nada fuera de los propios. Su nota dice que no leyó otras salidas; eso no se puede comprobar.
- **El archivo de reglas se reescribió durante la primera lectura.** Una prueba del curador volvió a generar el archivo que los lectores estaban usando. El contenido era idéntico (misma huella) y los lotes no cambiaron.
- **Una omisión en el encargo de los lectores.** Las definiciones de las subfunciones nombran fronteras sin decidir, y el encargo no dio un código para anotarlas. Lo señalaron en su nota de cierre 27 de los 32 lectores. No se corrigió a mitad de la lectura.
- **El defecto del grafo de la versión 1.2 apareció por una prueba.** Las 394 aristas con procedencia equivocada se vieron al listar todas las aristas de un pre-ensayo de prueba, no por una verificación diseñada para encontrarlas.
- **El árbol de trabajo arrancó de una carpeta vacía.** Varios pasos fallaron hasta que se lo sembró con el paquete 1.2. De ahí sale la precisión sobre la «copia limpia» de la sección 8 del documento 14.
- **Tres pasos de la cadena suponían que solo la versión 1.2 cambiaba coordenadas.** Fallaron en el ensayo con cambios de prueba. Se corrigieron para que los análisis de la versión 1.2 se calculen sobre el corpus de esa versión.

## 10. Revisión de esta versión y regresión

**Revisión de la versión candidata (ADR-027).** Cinco revisores automáticos que no habían participado en esta versión trabajaron sobre una copia congelada de la versión candidata. Tres buscaron errores y dejaron 69 hallazgos: 4 altos, 40 medios y 25 bajos.

| Revisor | Pregunta | Altos | Medios | Bajos |
|---|---|---|---|---|
| V1 | ¿El registro dice lo que el autor dijo? | 2 | 14 | 9 |
| V2 | ¿Las cifras y el estado coinciden entre documentos y con los datos? | 0 | 14 | 9 |
| V4 | ¿Las reglas adoptadas entraron bien a la taxonomía? | 2 | 12 | 7 |

Decisión sobre cada hallazgo: 58 corregidos, 6 corregidos en parte y 5 documentados. Lo que se corrigió a partir de esta revisión no tuvo otra lectura.

Los hallazgos altos y lo que se hizo con cada uno:

- **V1-001.** El campo `decision_del_autor`, que la versión 1.2 publicó vacío como lugar para que el autor anotara su respuesta, trae en diez proposiciones un valor que escribió el curador. El documento 14 y la bitácora afirman que la lectura del curador está en campos aparte, y para ese campo no es cierto. *Corregido:* El campo `decision_del_autor` lleva solo lo que el autor respondió de forma literal; las lecturas del curador pasaron a `lectura_del_curador`. La regresión lo comprueba.
- **V1-002.** La regla RP-11 se le presentó al autor con el efecto «Aclara una regla; puede cambiar secundarios», dentro de D-11.2 («las reglas que no mueven coordenadas»), y la tarea D-11.3 anunciaba releer solo con las reglas de D-11.1. En la relectura, su enunciado RP-11.1 es el segundo más citado en los ejes primarios que cambiaron, y el documento 14 no lo advierte. *Corregido:* RP-11.1 quedó como punto RV-3: los cambios de subfunción que la citan se retiraron y esperan la confirmación del autor. El estado del enunciado y el documento 14 (secciones 1 y 3.3) lo dicen.
- **V4-001.** Hay enunciados adoptados que le dan respuestas opuestas al mismo caso y ningún texto dice cuál prevalece: RP-01.1, RP-03.2 y RP-04.4 llevan a D28 el aseguramiento o la auditoría de un objeto con dominio propio, y RP-02.2 lo deja en el dominio de ese objeto; RP-02.1 y RP-02.2 chocan cuando la tesis mide una capacidad y discute la medición. Los lectores lo escribieron en sus notas de cierre, el documento 14 no se lo informa al autor y la relectura aplicó cambios de dominio en sentidos contrarios. *Corregido en parte:* Punto RV-5: no entra ni sale ningún pre-ensayo de D28 hasta que el autor fije la precedencia. Se retiraron 11 cambios. El choque entre RP-02.1 y RP-02.2 fuera de D28 queda informado, sin freno.
- **V4-002.** RP-11 se le presentó al autor entre «las reglas que no mueven coordenadas», con el efecto «Aclara una regla; puede cambiar secundarios», y en la relectura RP-11.1 es el segundo enunciado más citado en los cambios de coordenada primaria: 50 cambios de subfunción, 37 de ellos con cambio de función. El documento 14 da la cifra y no dice que contradice el efecto con que la regla se presentó y quedó adoptada. *Corregido:* Igual que V1-002.

**Tercera lectura de una muestra.** Otros dos lectores recibieron 80 casos sorteados: 60 ejes que la versión candidata cambiaba, veinte por eje, y 20 que quedaron retenidos porque una lectura declaró confianza baja. El sorteo es anterior a los frenos de la revisión: de esos 60, 42 siguen aplicados en esta versión y 18 quedaron frenados. Cada caso traía el pre-ensayo, el eje y dos valores en orden al azar, el de la versión 1.2 y el de las dos lecturas, sin decir cuál era cuál.

| Casos | Prefiere el valor de las dos lecturas | Prefiere el valor de la versión 1.2 | Los dos son defendibles | Ninguno de los dos |
|---|---|---|---|---|
| Cambiaban en la versión candidata (60) | 52 | 4 | 4 | 0 |
| · territorio (20) | 16 | 2 | 2 | 0 |
| · dominio (20) | 18 | 1 | 1 | 0 |
| · subfunción (20) | 18 | 1 | 1 | 0 |
| · siguen aplicados en esta versión (42) | 37 | 2 | 3 | 0 |
| · la revisión los frenó (18) | 15 | 2 | 1 | 0 |
| Retenidos por confianza baja (20) | 16 | 2 | 2 | 0 |

Es una tercera opinión automática, con la misma configuración que los dos lectores y con el mismo texto de reglas: no mide una tasa de error. Que prefiera el valor de las dos lecturas en los casos que la revisión frenó no resuelve los puntos que quedaron abiertos, porque leyó con las mismas reglas. Sirve como indicio para tu decisión de dejar o revertir la relectura (sección 7.1). Cada caso, con el motivo del tercer lector, está en `revision_1_3/tercera_lectura/resultado.csv`.

El material de la revisión está en `revision_1_3/`.

**Regresión.** 14 de 14 verificaciones sin diferencias.

| Verificación | Resultado |
|---|---|
| Manifiesto del paquete | 558 archivos con su huella SHA-256; 0 no coinciden y 0 no figuran en el manifiesto |
| Versiones 1.0, 1.1 y 1.2 publicadas | versión 1.0: 115 archivos, 0 diferencias con su manifiesto; versión 1.1: 146 archivos, 0 diferencias con su manifiesto; versión 1.2: 349 archivos, 0 diferencias con su manifiesto. No se modificaron |
| Archivos citados en los documentos | 375 citas en 21 documentos; 0 no existen |
| Estadísticas contra los datos | 34 cifras recalculadas desde los archivos de datos y desde la base del grafo; 0 no coinciden |
| Cifras clave de los documentos | 49 cifras clave buscadas en 11 documentos, cada una junto a la palabra que la nombra; 0 no aparecen. No comprueba las demás cifras de los documentos |
| Hallazgos críticos y altos | 48 hallazgos; 0 sin decisión, acción o lugar donde se ve |
| Grafo candidato | 0 errores de validación; reconstrucción desde los conjuntos de cambios igual al grafo |
| Errata del grafo de la versión 1.2 | 0 relaciones de clasificación de ejes que no cambiaron dicen en su método que el eje cambió (en el grafo publicado de la 1.2 eran 394) |
| Columnas reservadas al autor | 4 archivos con columnas para la decisión o la nota del autor; 0 tienen algo escrito por el curador; 0 campos del autor con algo que él no respondió de forma literal en el registro de decisiones |
| Versión que declaran los archivos de datos | 0 archivos declaran una versión del producto distinta de la 1.3 |
| Rastros del entorno de trabajo | 555 archivos de texto revisados; 0 con rutas internas |
| Regeneración en una copia del paquete | 28 pasos ejecutados con los guiones del paquete y las fuentes del autor, sobre una copia del paquete y no sobre una carpeta vacía; 559 archivos comparados, 0 diferencias |
| Integración de la relectura | El integrador del paquete vuelve a escribir el archivo de ajustes a partir de las lecturas guardadas; el resultado es idéntico al que viaja en el paquete |
| Reversión de la relectura | Con las listas de cambios vacías y tres guiones ejecutados, 739 de 739 pre-ensayos del corpus y 16 de 16 de la serie APX vuelven a la coordenada de la versión 1.2, y el grafo vuelve a 5.058 nodos y 28.142 relaciones, los de esa versión |

## 11. Archivos de esta versión

| Archivo | Qué trae |
|---|---|
| `data/decisiones_del_autor.json` | El registro de decisiones, con tu mensaje del 16 de noviembre, la respuesta por proposición y los estados |
| `data/reglas_propuestas_D11_enunciados.csv` | Los 95 enunciados, con su estado en la versión 1.3 |
| `data/preguntas_abiertas_1_3.csv` | Las preguntas que siguen abiertas, con los pre-ensayos que dependen de cada una |
| `data/relectura_1_3_resumen.json` | Todas las cifras de la sección 4 |
| `data/relectura_1_3_por_eje.csv` | El resultado de cada eje de cada pre-ensayo, con las dos lecturas |
| `data/relectura_1_3_casos_para_el_autor.csv` | Los casos en que las lecturas apuntan fuera de la coordenada vigente y el cambio no entró |
| `data/escala_del_pilar_OS_1_3.csv` | La escala registrada para los pre-ensayos del pilar OS |
| `data/cambios_1_2_a_1_3.csv` | Lo que cambió respecto de la versión 1.2, fila por fila |
| `data/revision_humana_propuesta.json`, `data/revision_humana_muestra.csv`, `data/revision_humana_clave.csv` | La propuesta de revisión humana, la muestra a ciegas y su clave |
| `relectura_1_3/` | El encargo, las reglas, los lotes, las salidas y las notas de cierre de los lectores, y el integrador que decide eje por eje |
| `revision_1_3/` | El material de la revisión de esta versión |
| `scripts/datos_de_trabajo/ajustes_relectura_1_3.json` | El archivo desde el que entran todos los cambios de la relectura |

> **Registro de la versión 1.3 (16 de noviembre de 2026).** Este documento se conserva tal como se publicó. Las cifras, los estados y los archivos que cita corresponden a esa versión. El estado vigente está en `docs/15_Decisiones_delegadas_y_relectura_1_4.md` y en los documentos 16 a 19.

# Decisiones de arquitectura del Frontier CISO Atlas

**Frontier CISO Atlas 1.3** · Taxonomía 6.0 (reglas de asignación, revisión 2) · Ontología 2.1.0 · GM-24 V7.1 · 16 de noviembre de 2026 · Estado: decisiones de diseño confirmadas por el autor; reglas adoptadas según la lectura del curador y corpus releído a ciegas por lectores automáticos, con una lectura para todos y dos donde la primera difería; contenido candidato, sin validación humana

Las decisiones ADR-001 a ADR-012 del AI CISO Atlas siguen vigentes. Este documento agrega diecinueve. ADR-013 a ADR-021 son de la versión 1.0 y ADR-022 a ADR-025, de la versión 1.1. El 15 de noviembre de 2026 el autor aceptó en bloque «las decisiones propuestas»: su mensaje no nombra las ADR, y aquí se las considera alcanzadas por esa aceptación porque registran las decisiones D-01 a D-10. ADR-026 a ADR-029 son de la versión 1.2: registran cómo se leyó esa aceptación, cómo se revisa una versión, cómo se corrige una coordenada heredada y cómo se propone leer el Atlas. El autor no las vio antes de que se aplicaran, y las confirmó el 16 de noviembre de 2026, junto con la lectura de su aceptación (decisión D-14). ADR-030 y ADR-031 son de la versión 1.3: registran cómo se releyó el corpus con las reglas adoptadas y cómo se conservan los análisis de las versiones anteriores. El autor no las vio: rigen de forma provisoria y están entre lo que tiene que confirmar o corregir (decisión D-15, proposiciones 4 y 5).

**Cómo leer el estado de cada ADR.**

- **Aceptada:** el autor la aceptó en bloque el 15 de noviembre de 2026 o la confirmó el 16.
- **Sustituida:** otra ADR la reemplaza.
- **Propuesta; rige de forma provisoria:** la versión 1.3 ya la aplica, porque sin ella no podía hacerse lo que se seguía de las decisiones del autor, y el autor puede no confirmarla. Cada una dice qué se deshace en ese caso.

**Texto congelado.** El contexto, la decisión, las consecuencias y la alternativa descartada de ADR-013 a ADR-025 son los de la versión 1.1, sin cambios: es el texto que estaba publicado cuando el autor aceptó. Lo que cambió después está en la «Nota de la versión 1.2» y en la «Nota de la versión 1.3» de cada una.

| Decisión | Título | Estado | Decisiones del autor |
|---|---|---|---|
| ADR-013 | Renombrar el producto a Frontier CISO Atlas | Aceptada: la alcanza la aceptación en bloque del 15 de noviembre de 2026, y el autor confirmó esa lectura el 16 (D-14.1) | D-01 |
| ADR-014 | Adoptar la Taxonomía 6.0 | Aceptada: la alcanza la aceptación en bloque del 15 de noviembre de 2026, y el autor confirmó esa lectura el 16 (D-14.1) | D-02 |
| ADR-015 | Adoptar la Frontier CISO Atlas Core Ontology 2.0.0 | Sustituida por ADR-022, que adopta la versión 2.1.0 y contiene a la 2.0.0 | D-05 |
| ADR-016 | Separar el plano A (corpus académico) del plano B (capacidades contratadas) | Aceptada: la alcanza la aceptación en bloque del 15 de noviembre de 2026, y el autor confirmó esa lectura el 16 (D-14.1) | D-01 |
| ADR-017 | Tratar el MCCS como lente y leer el pilar OS en dos escalas | Aceptada: la alcanza la aceptación en bloque del 15 de noviembre de 2026, y el autor confirmó esa lectura el 16 (D-14.1) | D-04 |
| ADR-018 | Introducir variables homeostáticas y un modelo de referencia del eje H | Aceptada: la alcanza la aceptación en bloque del 15 de noviembre de 2026, y el autor confirmó esa lectura el 16 (D-14.1) | D-06 |
| ADR-019 | Construir un grafo candidato sobre pre-ensayos y no asignar identificadores de ensayo | Aceptada: la alcanza la aceptación en bloque del 15 de noviembre de 2026, y el autor confirmó esa lectura el 16 (D-14.1) | D-07 |
| ADR-020 | Política de migración de 5.3 a 6.0 y clasificación asistida | Aceptada: la alcanza la aceptación en bloque del 15 de noviembre de 2026, y el autor confirmó esa lectura el 16 (D-14.1) | D-02, D-03, D-07 |
| ADR-021 | Base de referencia verificada, con versión y fecha, y discrepancias a la vista | Aceptada: la alcanza la aceptación en bloque del 15 de noviembre de 2026, y el autor confirmó esa lectura el 16 (D-14.1) | D-10 |
| ADR-022 | Revisar la propuesta de ontología a la versión 2.1.0 | Aceptada: la alcanza la aceptación en bloque del 15 de noviembre de 2026, y el autor confirmó esa lectura el 16 (D-14.1) | D-05 |
| ADR-023 | Incorporar la Biblioteca cognitiva al grafo candidato con tipos por categoría | Aceptada: la alcanza la aceptación en bloque del 15 de noviembre de 2026, y el autor confirmó esa lectura el 16 (D-14.1) | D-08, D-12 |
| ADR-024 | Medir con el catálogo 2.0 y proponer indicadores por variable homeostática | Aceptada: la alcanza la aceptación en bloque del 15 de noviembre de 2026, y el autor confirmó esa lectura el 16 (D-14.1) | D-09 |
| ADR-025 | Entregar como propuestas, sin aplicar, el remapeo, la lectura de D20 y la ampliación de celdas en blanco | Aceptada: la alcanza la aceptación en bloque del 15 de noviembre de 2026, y el autor confirmó esa lectura el 16 (D-14.1) | D-03, D-10 |
| ADR-026 | Efecto de la aceptación en bloque | Aceptada: rige desde la versión 1.2 y el autor la confirmó el 16 de noviembre de 2026 (D-14.7) | D-14 |
| ADR-027 | Revisión crítica antes de publicar una versión, con revisores de contexto independiente | Aceptada: rige desde la versión 1.2 y el autor la confirmó el 16 de noviembre de 2026 (D-14.7) | D-14 |
| ADR-028 | Vía de corrección de coordenadas heredadas | Aceptada: rige desde la versión 1.2 y el autor la confirmó el 16 de noviembre de 2026 (D-14.7) | D-03, D-14 |
| ADR-029 | Lectura crítica y responsabilidad indelegable | Aceptada: redacta el principio que el autor enunció el 15 de noviembre de 2026, y el autor confirmó la redacción el 16 (D-14.6) | D-14 |
| ADR-030 | Relectura del corpus con las reglas adoptadas: dos lecturas a ciegas y cuándo cambia una coordenada | Propuesta; rige de forma provisoria desde la versión 1.3. El autor no la vio | D-15 |
| ADR-031 | Los análisis y los documentos de una versión se conservan con los datos de esa versión | Propuesta; rige de forma provisoria desde la versión 1.3. El autor no la vio | D-15 |

## Correspondencia entre las decisiones del autor y las decisiones de arquitectura

Las decisiones D son las que se le pidieron al autor; las ADR son el registro de arquitectura. La aceptación cubre las decisiones de diseño. Las tareas de validación (D-07, D-09 y parte de D-03, D-08 y D-10) se registran como «aceptadas como base de trabajo, sin validar»: aceptar que algo no tiene validación humana no lo valida. Los conjuntos de cambios siguen en estado «propuesto» (ADR-019). Las instrucciones 7.2 del agente curador quedaron confirmadas con la decisión D-14.7; las 7.3 las suceden para recoger las reglas adoptadas.

| N.º | Clase | Proposición | Estado | ADR | Depende de |
|---|---|---|---|---|---|
| D-01 | diseño | El producto se llama Frontier CISO Atlas y continúa al AI CISO Atlas: conserva sus códigos, su arquitectura y sus decisiones anteriores. | Aceptada, con la advertencia a la vista | ADR-013, ADR-016 | — |
| D-04 | diseño | El pilar OS del MCCS se lee en dos escalas del mismo pilar: individual (T01) y de oficina (T03). | Aceptada | ADR-017 | — |
| D-06 | diseño | Se adoptan las seis variables homeostáticas (HV01 a HV06) como propuesta de diseño, sin respaldo normativo externo. | Aceptada | ADR-018 | — |
| D-02 | diseño | Se adopta la Taxonomía 6.0: 8 territorios, 28 dominios, 6 funciones, 34 subfunciones y el eje H ampliado. D27 se admite con reserva y D26 por materialidad. | Aceptada | ADR-014, ADR-020 | D-04, D-06 |
| D-03 | diseño y aplicación | El gobierno, el riesgo y el cumplimiento de la IA que estaban alojados en D20 pasan a D01, D02 o D03 (regla 7). | Aceptada y aplicada | ADR-020, ADR-025, ADR-028 | D-02 |
| D-05 | diseño | Se adopta la Ontología 2.1.0, que contiene a la 2.0.0 y es un cambio mayor respecto de la 1.0.0. | Aceptada | ADR-015, ADR-022 | D-02 |
| D-08 | diseño y validación | La Biblioteca cognitiva entra al grafo candidato con tipos del módulo de cognición. | Aceptada como base de trabajo; modificada por la revisión | ADR-023 | D-04, D-05 |
| D-09 | validación | Los indicadores asignados miden cada variable homeostática, y las subfunciones PR06 y RC05 tienen indicadores. | Base de trabajo; corregida por la revisión | ADR-024 | D-02, D-05, D-06 |
| D-10 | diseño y validación | Se acepta la propuesta de remapeo como pedido para la próxima versión del GM-24, y los 16 pre-ensayos de la serie APX como capa de ampliación. | Aceptada | ADR-021, ADR-025 | D-02, D-03 |
| D-07 | validación | La categorización de los 739 pre-ensayos es válida y la primera tanda de ensayos es la propuesta. | Base de trabajo; validación humana pendiente | ADR-019, ADR-020 | D-02, D-03, D-10 |
| D-14 | confirmación | Confirmar lo que el paquete leyó en el mensaje del autor del 15 de noviembre de 2026 y lo que hizo en su nombre. | Confirmada por el autor el 16 de noviembre de 2026 | ADR-026, ADR-027, ADR-028, ADR-029 | — |
| D-15 | confirmación | Confirmar o corregir lo que la versión 1.3 leyó en las tres frases generales del mensaje del 16 de noviembre de 2026 y las reglas de trabajo que esa versión puso a regir sin que el autor las viera. | Abierta: a confirmar o corregir por el autor; es la primera que conviene decidir | ADR-030, ADR-031 | D-14 |
| D-11 | diseño | Adoptar, modificar o rechazar las 18 reglas y aclaraciones que la revisión propone (RP-01 a RP-18), enunciado por enunciado. | Abierta en parte: los enunciados con texto listo quedan adoptados (lectura del curador, a confirmar en D-15.1); siguen abiertas las preguntas y los puntos que dejó la revisión, y en cola parte de los encargos | — | D-02, D-14 |
| D-13 | validación | Confirmar o revertir los cambios que la revisión aplicó sin la lectura del autor, y resolver los casos en que las lecturas no coinciden. | Abierta en parte: los cambios de la Biblioteca, la medición, la serie APX y los textos se leyeron como confirmados en bloque (a confirmar en D-15.2); la parte del corpus (D-13.1 y D-13.2) se leyó como sin respuesta | — | D-14, D-11 |
| D-12 | validación | Decidir cómo se revisa la Biblioteca cognitiva y qué se corrige en la base, que es del autor. | Cerrada sin revisión: la Biblioteca queda como estaba (lectura del curador, a confirmar en D-15.3) | ADR-023 | D-08 |

**Orden en que se aplicaron D-01 a D-10:** D-01 → D-04 y D-06 → D-02 → D-03 → D-05 → D-08 y D-09 → D-10 → D-07.

**Orden propuesto para las decisiones abiertas:**

| Paso | Qué | Por qué en ese lugar |
|---|---|---|
| 1 | D-15: confirmar o corregir cómo se leyeron tus tres frases generales y las reglas de trabajo que esta versión puso a regir. | Todo lo demás se apoya en esas lecturas. Si alguna no es la que quisiste, cambia lo que quedó adoptado, confirmado o cerrado. |
| 2 | Contestar los puntos que la revisión dejó abiertos (RV-1 a RV-5) y las preguntas abiertas de las reglas. | Cada respuesta destraba los cambios que ese punto frenó, sin volver a leer. |
| 3 | Decidir si los cambios que la relectura aplicó quedan: dejarlos, revertirlos enteros o revertir filas. | Es el cambio más grande de la versión 1.3 y se revierte en un paso. |
| 4 | La revisión humana de una muestra. | Es la única fuente de validación humana, y conviene hacerla sobre la categorización que quede después de los pasos 1 a 3. |
| 5 | D-13.1 y D-13.2: los once casos de D20 y los 37 cambios de coordenada de la versión 1.2. | La relectura trae evidencia nueva para decidirlos, y D-15.2 puede dejar contestada la segunda. |
| 6 | Los encargos en cola y la próxima revisión de la ontología (solicitud OCR-CAND-03). | Son trabajo de diseño y no bloquean lo anterior. |

## ADR-013 · Renombrar el producto a Frontier CISO Atlas

**Estado:** Aceptada: la alcanza la aceptación en bloque del 15 de noviembre de 2026, y el autor confirmó esa lectura el 16 (D-14.1). En la versión 1.1 su estado era «propuesta».

**Contexto.** El nombre AI CISO Atlas ata el mapa a una tecnología. La IA es el principal motor del cambio, pero el objeto del Atlas es el rol del CISO y el territorio en el que se ejerce. El autor busca completitud y un nombre que describa un tipo de empresa y un tipo de CISO.

**Decisión.** El producto pasa a llamarse Frontier CISO Atlas, versión 1.0, como evolución directa del AI CISO Atlas. La frontera se define como condición evolutiva (eje H), no como territorio ni como tecnología. Se conservan los códigos, la arquitectura y las decisiones ADR-001 a ADR-012.

**Consecuencias.** Los documentos, la ontología y las instrucciones del agente cambian de nombre. Los artefactos publicados con el nombre anterior siguen siendo válidos como versión previa. El territorio T07 no se renombra.

**Alternativa descartada.** Mantener el nombre y ampliar el alcance en silencio: se descartó porque el nombre seguiría sugiriendo un Atlas solo de IA.

**Nota de la versión 1.2.** El producto está hoy en la versión 1.2. El nombre coincide con un concepto comercial de un proveedor y con el de una de sus suites; el Atlas lo toma como referencia de contexto y no como definición propia. La versión 1.1 pidió aprobar el nombre sin esa advertencia: se confirma en D-14.4.

**Nota de la versión 1.3.** El autor confirmó el nombre con la advertencia a la vista (D-14.4). El producto está en la versión 1.3.

## ADR-014 · Adoptar la Taxonomía 6.0

**Estado:** Aceptada: la alcanza la aceptación en bloque del 15 de noviembre de 2026, y el autor confirmó esa lectura el 16 (D-14.1). En la versión 1.1 su estado era «propuesta».

**Contexto.** La versión 5.3 no alojaba cuatro disciplinas que la base de referencia trata en primer nivel, dejaba dos categorías oficiales de CSF 2.0 sin subfunción propia y nombraba mecanismos homeostáticos sin decir qué regulan.

**Decisión.** Se adopta la Taxonomía 6.0: 8 territorios, 28 dominios (se suman D25, D26, D27 y D28), 6 funciones y 34 subfunciones (se suman PR06 y RC05). El eje H suma CAT11, INH11, HOM11, HOM12, HX08 y seis variables homeostáticas. Los dominios nuevos se admiten con cinco criterios explícitos; D26 se admite por materialidad y D27 con reserva.

**Consecuencias.** Hay que migrar el corpus, completar indicadores para PR06 y RC05 y escribir contenido para D27 y D19. Los candidatos no admitidos quedan en una lista de vigilancia que se revisa en cada versión.

**Alternativa descartada.** Mantener 24 dominios y resolver con reglas de alcance: se descartó porque el aseguramiento y la arquitectura quedaban repartidos en más de diez dominios. Crear un dominio de gobierno de la IA: se descartó porque se expresa como T07 con D01, D02 o D03.

**Nota de la versión 1.2.** RC05 tiene un indicador y PR06 no tiene ninguno. D19 y D27 tienen 12 pre-ensayos en la capa de ampliación. La revisión crítica corrigió textos y conteos sin cambiar códigos y dejó 18 reglas propuestas, entre ellas la reescritura de los criterios de admisión (decisión D-11). Los criterios aplicados difieren de los que fijó el plan de trabajo; el documento 03 dice en qué.

**Nota de la versión 1.3.** El autor escribió «Acepto el cambio de reglas», y el curador lo leyó como la adopción de las reglas que tenían texto listo (a confirmar en D-15.1): 60 enunciados, que son las reglas de asignación, revisión 2. Los códigos no cambian. Siguen abiertas 11 preguntas, y los encargos sobre los criterios de admisión quedan en cola.

## ADR-015 · Adoptar la Frontier CISO Atlas Core Ontology 2.0.0

**Estado:** Sustituida por ADR-022, que adopta la versión 2.1.0 y contiene a la 2.0.0. En la versión 1.1 su estado era «propuesta».

**Contexto.** La ontología 1.0.0 no podía representar el producto-control, la flota de agentes, los niveles de autonomía, los planos del GM-24, los pre-ensayos como algo distinto de los ensayos, la medición ni la metacognición.

**Decisión.** Se adopta la versión 2.0.0: 10 módulos, 84 tipos de entidad, 92 relaciones y 36 reglas. Es una versión mayor porque cambia el nombre y porque CLASSIFIED_IN y MAPS_TO pasan a exigir propiedades. No se elimina ni se renombra nada de la 1.0.0.

**Consecuencias.** Los datos anteriores que usen esas dos relaciones sin propiedades deben completarse. En la versión 1.1 la propuesta se revisó a 2.1.0 (ADR-022) y los tipos del módulo de cognición recibieron la Biblioteca cognitiva (ADR-023).

**Alternativa descartada.** Una versión menor 1.1.0: se descartó porque las propiedades obligatorias rompen compatibilidad.

## ADR-016 · Separar el plano A (corpus académico) del plano B (capacidades contratadas)

**Estado:** Aceptada: la alcanza la aceptación en bloque del 15 de noviembre de 2026, y el autor confirmó esa lectura el 16 (D-14.1). En la versión 1.1 su estado era «propuesta».

**Contexto.** El GM-24 V7.1 distingue el corpus académico de siete instancias de dominio con productos concretos. Mezclarlos haría que un producto pareciera evidencia de un concepto.

**Decisión.** El plano es una lente del Atlas. Una instancia del plano B se ubica en un dominio, se vincula a los conceptos que instancia y nunca se usa como evidencia del plano A. Los nodos del plano B se marcan para revisión antes de una edición pública.

**Consecuencias.** El Atlas sigue siendo agnóstico de proveedor en su plano A. La edición pública necesita una decisión sobre qué del plano B se publica.

**Alternativa descartada.** Dejar el plano B fuera del grafo: se descartó porque impediría responder qué agentes ejecutan qué tareas y con qué autonomía.

**Nota de la versión 1.2.** La revisión encontró 77 pre-ensayos del plano A que nombran productos de un proveedor o al proveedor. Quedaron marcados «revisar», y el paquete lo informa con una comprobación propia (PAQ-01), que no es una de las 37 reglas de la ontología. El corpus no es neutral respecto de un proveedor. Falta decidir si los pre-ensayos que desarrollan una instancia de producto pasan al plano B.

## ADR-017 · Tratar el MCCS como lente y leer el pilar OS en dos escalas

**Estado:** Aceptada: la alcanza la aceptación en bloque del 15 de noviembre de 2026, y el autor confirmó esa lectura el 16 (D-14.1). En la versión 1.1 su estado era «propuesta».

**Contexto.** El MCCS es el método con el que el CISO navega el Atlas. Sus pilares (MM, OS, DO y NX) no son disciplinas ni perspectivas de responsabilidad. En las notas del autor, OS aparece como sustrato personal y como sistema operativo de la oficina.

**Decisión.** El pilar MCCS es una lente: cada pre-ensayo lleva uno y cada pilar se ancla en territorios. OS se lee en dos escalas del mismo pilar: individual (T01) y de oficina (T03).

**Consecuencias.** La lectura de OS necesita confirmación del autor. Si son dos pilares distintos, hay que separarlos y reclasificar los pre-ensayos con OS.

**Alternativa descartada.** Convertir el MCCS en un quinto eje: se descartó porque duplicaría el territorio T01 y obligaría a clasificar todo dos veces.

**Nota de la versión 1.2.** La aceptación en bloque alcanzó la lectura de OS en dos escalas (decisión D-04). Se aplicó a la Biblioteca con una regla por categoría: 59 conceptos llevan el pilar OS. Las habilidades socioemocionales y las mentalidades de resiliencia siguen en MM, aunque la definición del pilar las ubica en su escala individual: queda para la decisión D-12.2. Las anclas de los pilares son una hipótesis de diseño; su medición en el corpus está en el documento 02.

**Nota de la versión 1.3.** La relectura registró la escala de los pre-ensayos del pilar OS como dato de trabajo (encargo RP-14.2); no es una clasificación revisada.

## ADR-018 · Introducir variables homeostáticas y un modelo de referencia del eje H

**Estado:** Aceptada: la alcanza la aceptación en bloque del 15 de noviembre de 2026, y el autor confirmó esa lectura el 16 (D-14.1). En la versión 1.1 su estado era «propuesta».

**Contexto.** El autor describe la homeostasis, con sus fuerzas de aceleración e inhibición y el cambio del contexto de ejecución, como el ámbito natural del CISO de frontera. La 5.3 tenía fuerzas y mecanismos, pero no lo que se mantiene estable.

**Decisión.** Se introducen seis variables homeostáticas (HV01 a HV06) y dos relaciones: un mecanismo regula una variable y una fuerza la presiona. Entre categorías de la taxonomía expresan un modelo de referencia; en una organización se verifican con evidencia.

**Consecuencias.** Es una propuesta de diseño sin respaldo normativo externo y así queda declarada. Hay que vincular indicadores a cada variable.

**Alternativa descartada.** Dejar H como estaba: se descartó porque no permitía decir qué protege cada mecanismo.

**Nota de la versión 1.2.** Hay 71 vínculos candidatos entre indicadores y variables. Ninguna variable tiene todavía unidad, umbral ni responsable, y 5 de las 22 fuerzas no presionan ninguna: completar el modelo es la regla propuesta RP-15.

**Nota de la versión 1.3.** Completar el modelo de referencia del eje H es un encargo aceptado por el autor, en cola (RP-15).

## ADR-019 · Construir un grafo candidato sobre pre-ensayos y no asignar identificadores de ensayo

**Estado:** Aceptada: la alcanza la aceptación en bloque del 15 de noviembre de 2026, y el autor confirmó esa lectura el 16 (D-14.1). En la versión 1.1 su estado era «propuesta».

**Contexto.** Existen pre-ensayos, no ensayos. La arquitectura del Atlas exige que el grafo aprobado se apoye en ensayos aprobados.

**Decisión.** Se construye un grafo candidato: todos los nodos y relaciones llevan estado «candidato» y los conjuntos de cambios, «propuesto». El pre-ensayo es un tipo propio, distinto del ensayo. No se asignan identificadores de ensayo.

**Consecuencias.** El grafo sirve para explorar, medir cobertura y preparar la redacción, pero no para afirmar conocimiento aprobado. La promoción exige las aprobaciones y la revisión descritas en el documento 06.

**Alternativa descartada.** Esperar a tener ensayos para construir cualquier grafo: se descartó porque el grafo candidato es lo que permite elegir qué ensayos escribir primero.

**Nota de la versión 1.2.** La aceptación del autor no es la aprobación de los conjuntos de cambios: siguen en estado «propuesto» y el grafo sigue siendo candidato (ADR-026).

**Nota de la versión 1.3.** Los conjuntos de cambios siguen en estado «propuesto» y el grafo sigue siendo candidato. La versión 1.3 corrigió un defecto de procedencia del grafo de la 1.2 (documento 14, sección 5).

## ADR-020 · Política de migración de 5.3 a 6.0 y clasificación asistida

**Estado:** Aceptada: la alcanza la aceptación en bloque del 15 de noviembre de 2026, y el autor confirmó esa lectura el 16 (D-14.1). En la versión 1.1 su estado era «propuesta».

**Contexto.** Los clasificadores pueden discrepar de la coordenada vigente por razones ajenas al cambio de taxonomía. Aplicar esas discrepancias cambiaría decisiones previas sin revisión.

**Decisión.** La coordenada vigente se conserva salvo que el cambio lo cause el catálogo 6.0 (dominios D25 a D28, subfunciones PR06 y RC05). Todo otro desacuerdo queda como sugerencia. Cada clasificación guarda método, confianza, justificación y versión de taxonomía, y es candidata hasta que un curador la revise.

**Consecuencias.** Se heredan los posibles errores de la 5.3; los detectados quedan en la lista de sugerencias. Las reglas de alcance de la 6.0 que obligarían a reubicar pre-ensayos (en especial, de D20 a D01 y D02) no se aplican hasta que el autor decida.

**Alternativa descartada.** Aceptar todas las propuestas del clasificador: se descartó porque solo algunos clasificadores aplicaron las reglas de alcance y el resultado sería desparejo.

**Nota de la versión 1.2.** El texto de arriba es el de la versión 1.1, sin cambios. Sus consecuencias dicen, en presente, que los errores detectados quedan como sugerencias y que las reglas de alcance no se aplican hasta que el autor decida: eso dejó de valer. La decisión D-03 se interpretó como «sí» y se aplicó: 26 pre-ensayos salieron de D20 (13 con dos lecturas que deciden lo mismo, 9 en que la primera no había decidido y 4 adjudicados por escrito). Siete sugerencias de los clasificadores se aplicaron por la vía de corrección (ADR-028). La revisión observó que las instrucciones daban las reglas de alcance a todos los clasificadores y que la misma disparidad existe en las migraciones a D28; la regla propuesta RP-02 pide una cláusula que las empareje.

**Nota de la versión 1.3.** La relectura de la versión 1.3 leyó todo el corpus a ciegas con las reglas adoptadas y cambió 260 coordenadas (ADR-030).

## ADR-021 · Base de referencia verificada, con versión y fecha, y discrepancias a la vista

**Estado:** Aceptada: la alcanza la aceptación en bloque del 15 de noviembre de 2026, y el autor confirmó esa lectura el 16 (D-14.1). En la versión 1.1 su estado era «propuesta».

**Contexto.** La taxonomía se justifica contra artefactos externos que cambian. El mapeo del GM-24 V7.1 usa estructuras que ya no rigen en MITRE ATT&CK, MITRE ATLAS y CSA CCM.

**Decisión.** Se mantiene una base de 145 artefactos de 42 organismos con versión, fecha, estado, fuente y estado de verificación. Solo fuentes oficiales; lo no verificado se declara. Las discrepancias se registran y no se corrigen en silencio: el mapeo existente conserva la versión del artefacto contra la que se hizo.

**Consecuencias.** Hay un calendario de revalidación. Rehacer los cruces envejecidos es un requisito para el grafo aprobado.

**Alternativa descartada.** Actualizar el mapeo del GM-24 dentro de este trabajo: se descartó porque cambia un artefacto vigente del autor sin su decisión.

**Nota de la versión 1.2.** La base tiene 146 artefactos. Segunda verificación independiente de 35 puntos que sostienen decisiones de la taxonomía o del remapeo (32 afirmaciones y 3 preguntas abiertas: 9 puntos sobre ATT&CK, ATLAS y CCM y 26 sobre otras normas y marcos), hecha contra las páginas de los organismos emisores durante la revisión crítica de la versión 1.2. Sin errores que cambien una decisión de la taxonomía. Se corrigieron dos registros (las versiones de Open FAIR y la identificación de las áreas de CyBOK), se confirmaron dos cambios de nombre de proyectos de NIST que estaban a revalidar y se precisaron cinco fichas. Cuatro conteos no se pudieron confirmar en fuente oficial pública: los controles de ISO/IEC 27002 y del Anexo A de ISO/IEC 42001, los 32 controles de Swift CSCF y las 11 áreas de competencia de NICE. El cruce propio del Atlas ya usa CCM v4.1; el mapeo del GM-24 no se modificó.

## ADR-022 · Revisar la propuesta de ontología a la versión 2.1.0

**Estado:** Aceptada: la alcanza la aceptación en bloque del 15 de noviembre de 2026, y el autor confirmó esa lectura el 16 (D-14.1). En la versión 1.1 su estado era «propuesta».

**Contexto.** Al cargar la Biblioteca cognitiva y la medición aparecieron tres límites de la 2.0.0: los tipos cognitivos no podían clasificarse en la taxonomía; un indicador solo podía medir instancias de una variable homeostática, y el catálogo las tiene como categorías; y no existía la relación entre unidad de aprendizaje y concepto que pide la base «Integración Atlas 1404 – GM-24».

**Decisión.** La propuesta pasa a 2.1.0: se amplían CLASSIFIED_IN y MEASURES, se agregan la relación COVERS_CONCEPT y la regla SV-118, se precisa la definición de MetacognitivePractice y se suman dos preguntas de competencia. Quedan 84 tipos de entidad, 93 relaciones, 37 reglas y 22 preguntas. La 2.1.0 contiene a la 2.0.0 y todo el cambio es aditivo.

**Consecuencias.** Como ninguna de las dos versiones está aprobada, la decisión D-05 pasa a referirse a la 2.1.0. La pregunta de competencia 16, que con la 2.0.0 no podía responderse con aristas válidas, ahora se responde para el modelo de referencia.

**Alternativa descartada.** Conservar el número 2.0.0 y cambiar su contenido: se descartó porque dos paquetes tendrían la misma versión con contenido distinto.

**Nota de la versión 1.2.** La ontología no cambió en la versión 1.2. Lo que la revisión propone está en la solicitud OCR-CAND-03.

## ADR-023 · Incorporar la Biblioteca cognitiva al grafo candidato con tipos por categoría

**Estado:** Aceptada: la alcanza la aceptación en bloque del 15 de noviembre de 2026, y el autor confirmó esa lectura el 16 (D-14.1). En la versión 1.1 su estado era «propuesta».

**Contexto.** La Biblioteca cognitiva del CISO de frontera tiene 1.404 conceptos y una base de integración propia, con corte al 12-nov-2026, que los propone como nodos de tipo Concept porque la ontología 1.0.0 no tenía tipos cognitivos. Esa base se declara propuesta para revisión y no aplicada al grafo. La versión 1.0 de este paquete no la había localizado.

**Decisión.** Los conceptos entran al grafo candidato en un conjunto de cambios propuesto. Cada uno recibe el tipo del módulo de cognición que corresponde a su categoría, con una regla determinista, y conserva el tipo original como propiedad. Los territorios editoriales se cargan como están, con primario solo cuando la base declara un único territorio. De los 1.653 vínculos con unidades del GM-24 se cargan los 792 de confianza media o alta editorial. Los vínculos entre prácticas y sesgos se toman solo de lo que la base enuncia.

**Consecuencias.** El territorio T01 y el pilar MM dejan de estar vacíos en el grafo. Siguen pendientes las validaciones que la propia base exige: duplicados y alias, aprobación de la relación y de sus propiedades, reserva de identificadores definitivos y revisión humana de cada vínculo. Los identificadores del grafo candidato son provisionales.

**Alternativa descartada.** Cargar todo como Concept, como propone la base: se descartó porque impediría preguntar qué prácticas contrarrestan qué sesgos. Cargar todos los vínculos con unidades: se descartó porque la base marca 861 como débiles.

**Nota de la versión 1.2.** El texto de arriba es el de la versión 1.1, sin cambios. Dice que los territorios editoriales se cargan como están y que se cargan los vínculos de confianza media o alta: en la versión 1.2 ninguna de las dos cosas vale. 81 conceptos recibieron su tipo por lectura y no por la regla. Los territorios ya no se cargan como clasificación: quedan como propiedad del nodo. La cobertura se redujo de 792 vínculos a los 165 de selección editorial o de ancla expresa, y las prácticas contra sesgos, de 142 a los 57 que la segunda lectura sostuvo. La Biblioteca no llena el vacío del pilar OS en el corpus: no está vinculada con los pre-ensayos. Lo que falta revisar es la decisión D-12.

**Nota de la versión 1.3.** El autor escribió «No revisar la biblioteca» (D-12): queda como base de trabajo sin revisar. Los cambios que la versión 1.2 le hizo se leyeron como confirmados en bloque (D-13.3; lectura del curador, a confirmar en D-15.2).

## ADR-024 · Medir con el catálogo 2.0 y proponer indicadores por variable homeostática

**Estado:** Aceptada: la alcanza la aceptación en bloque del 15 de noviembre de 2026, y el autor confirmó esa lectura el 16 (D-14.1). En la versión 1.1 su estado era «propuesta».

**Contexto.** El catálogo vigente del proyecto ya no es el 1.2, de 64 indicadores, sino el del Modelo Operativo CISO 365 2.0, de 224. Las variables homeostáticas no tenían indicadores y las subfunciones PR06 y RC05 tampoco.

**Decisión.** El grafo candidato usa el catálogo 2.0. Los indicadores K01 a K64 conservan su coordenada; K36 migra a PR06 porque la Taxonomía 6.0 da subfunción propia a PR.IR. Los demás se ubican por la categoría de CSF 2.0 que declara el catálogo y reciben subfunción solo cuando esa categoría corresponde a una sola. Se proponen 71 vínculos entre indicadores y variables homeostáticas, con papel principal o de apoyo, como modelo de referencia. Las audiencias que son órganos de gobierno se representan como tales.

**Consecuencias.** Cada variable homeostática tiene indicadores propuestos y cada subfunción tiene al menos un indicador. 71 indicadores quedan solo con función. Los vínculos con variables son una propuesta de diseño, igual que las variables. Falta un indicador para la protección física y ambiental.

**Alternativa descartada.** Crear indicadores nuevos para PR06 y RC05: se descartó porque el catálogo 2.0 ya los tiene.

**Nota de la versión 1.2.** El texto de arriba es el de la versión 1.1, sin cambios. En la versión 1.2: el catálogo 1.2 tenía 70 indicadores (64 y seis del sistema de gestión), de los que 67 heredan su coordenada sin cambios y 3 tienen el dominio corregido por un revisor. PR06 quedó sin indicadores y RC05 conserva uno (K189): la alternativa descartada, que daba por cubiertas las dos subfunciones, solo vale para RC05 y queda reabierta para PR06. La regla de subfunción está descrita como se aplica, y el método de cada indicador está en el catálogo. Los indicadores sin territorio ni dominio los recibieron de un revisor, con una sola lectura. De los 71 vínculos con variables, en 49 las dos lecturas coinciden en el vínculo y en el papel.

**Nota de la versión 1.3.** Los cambios de la medición se leyeron como confirmados en bloque (D-13.4; lectura del curador de «Confirmo el resto de los cambios», a confirmar en D-15.2). Los indicadores no se releyeron con las reglas adoptadas.

## ADR-025 · Entregar como propuestas, sin aplicar, el remapeo, la lectura de D20 y la ampliación de celdas en blanco

**Estado:** Aceptada: la alcanza la aceptación en bloque del 15 de noviembre de 2026, y el autor confirmó esa lectura el 16 (D-14.1). En la versión 1.1 su estado era «propuesta».

**Contexto.** Tres pendientes de la versión 1.0 tocan artefactos o decisiones del autor: el mapeo del GM-24 a marcos, la ubicación del gobierno y el riesgo de la IA, y el contenido de los dominios sin pre-ensayos.

**Decisión.** Se entregan como propuestas separadas. El remapeo alcanza a 78 vínculos existentes y agrega 2, y queda para la próxima versión del GM-24. La lectura de D20 clasifica sus 71 pre-ensayos según la regla de alcance, sin cambiar la categorización. La ampliación propone 16 pre-ensayos para D19, D27 y RC05, fuera del corpus y del grafo.

**Consecuencias.** El GM-24, el corpus y la categorización quedan como estaban. Cada propuesta se puede aceptar, corregir o descartar por separado.

**Alternativa descartada.** Aplicar las tres dentro de este trabajo: se descartó por la misma razón que en ADR-021 y en la política de migración.

**Nota de la versión 1.2.** El texto de arriba es el de la versión 1.1, sin cambios. La aceptación en bloque se leyó como un «sí» a las tres propuestas, y esa lectura queda a confirmar (D-14.2 y D-14.3). La lectura de D20 se aplicó (ADR-028). La serie APX se corrigió y entra al grafo candidato como capa de ampliación, aparte del corpus base: el texto de arriba decía «fuera del corpus y del grafo». La propuesta de remapeo cambió después de la aceptación: alcanza hoy a 91 vínculos existentes y agrega 7, porque los casos R2 y R4, que estaban «a revisar», tienen una resolución propuesta a partir de la verificación externa. Sigue sin aplicarse al GM-24.

**Nota de la versión 1.3.** El autor confirmó las dos lecturas de D-10 (D-14.3). La serie APX se releyó a ciegas (documento 14, sección 4.8). La propuesta de remapeo y la lectura de D20 se conservan calculadas sobre el corpus de la versión 1.2 (ADR-031).

## ADR-026 · Efecto de la aceptación en bloque

**Estado:** Aceptada: rige desde la versión 1.2 y el autor la confirmó el 16 de noviembre de 2026 (D-14.7).

**Contexto.** El 15 de noviembre de 2026 el autor aceptó en bloque «las decisiones propuestas», con el supuesto de que no fueran contradictorias y apuntaran a la excelencia y al rigor, y aceptó que el contenido no tiene validación humana. Su mensaje no nombra ninguna decisión ni ninguna ADR. La revisión crítica encontró que cinco de las diez decisiones no eran proposiciones que un «sí» resuelva: dos preguntaban «si» y tres pedían validar contenido que el propio paquete declaraba sin revisar. Y encontró que, aplicadas a la vez, las diez chocaban en cuatro puntos.

**Decisión.** La aceptación se lee como aceptación de las decisiones de diseño. Las tareas de validación se registran como «aceptadas como base de trabajo, sin validar». Cada decisión se reformula como proposición, con la opción tomada, y conserva a la vista el texto que tenía en la versión 1.1. Las dos que eran preguntas (D-03 y D-10) se contestan con un «sí» y quedan a confirmar. Las decisiones se aplican en un orden. Los conjuntos de cambios siguen en estado «propuesto».

**Consecuencias.** La condición de la aceptación se cumplió en parte: de los cuatro choques, dos se resolvieron, uno se resolvió en parte y uno sigue abierto. Todo lo que hubo que interpretar se le pregunta al autor en la decisión D-14. Si no confirma esta lectura, las diez decisiones vuelven a quedar abiertas y la versión 1.2 pasa a ser una propuesta; no hay nada que deshacer en los datos. El grafo sigue siendo candidato.

**Alternativa descartada.** Tratar la aceptación como validación de todo el contenido: se descartó porque aceptar que algo no tiene validación humana no lo valida. Esperar una confirmación decisión por decisión antes de seguir: se descartó porque el mensaje pedía continuar; por eso la confirmación se pide ahora.

**Nota de la versión 1.3.** El autor confirmó esta lectura (D-14.1 y D-14.7).

## ADR-027 · Revisión crítica antes de publicar una versión, con revisores de contexto independiente

**Estado:** Aceptada: rige desde la versión 1.2 y el autor la confirmó el 16 de noviembre de 2026 (D-14.7).

**Contexto.** El autor escribió que, si hacía falta someter todo al escrutinio de un agente crítico, se propusiera una forma de implementar la revisión y la mejora. Quien genera un artefacto no es buen revisor del mismo artefacto.

**Decisión.** Antes de publicar una versión, revisores con contexto propio leen una copia congelada del paquete, cada uno con un encargo escrito y sin ver el trabajo de los demás. Las clasificaciones reciben una segunda lectura, a ciegas cuando el caso lo permite. Las afirmaciones sobre marcos externos se verifican contra las páginas de sus organismos. Cada hallazgo recibe una decisión escrita. La versión corregida la leen revisores que no participaron, antes de publicarla. El material de la revisión se publica con el paquete.

**Consecuencias.** La revisión cuesta tiempo y puede fallar: tres revisores tuvieron que retomarse. Tiene dos límites que no se resuelven con más revisores del mismo tipo. Comparten configuración con quien generó los artefactos: tienen contexto independiente, no juicio independiente, y pueden compartir un mismo error. Y quien decide qué hacer con cada hallazgo es quien generó los artefactos. La revisión humana sigue siendo necesaria. Si el autor no confirma esta práctica, no hay nada que deshacer: deja de ser práctica.

**Alternativa descartada.** Un solo revisor que lea todo: se descartó porque un solo contexto no cubre el paquete y no puede dar segundas lecturas.

**Nota de la versión 1.3.** El autor la confirmó (D-14.7). La versión 1.3 se revisó antes de publicarse (documento 14, sección 10).

## ADR-028 · Vía de corrección de coordenadas heredadas

**Estado:** Aceptada: rige desde la versión 1.2 y el autor la confirmó el 16 de noviembre de 2026 (D-14.7).

**Contexto.** La política de migración solo admitía cambios causados por un dominio o una subfunción nuevos. Con eso, cuatro errores que el propio clasificador llamó evidentes seguían sin corregirse, y la regla 7 no podía aplicarse.

**Decisión.** Una coordenada heredada cambia cuando dos lecturas coinciden en el destino, o cuando una adjudicación escrita se apoya en la tesis y en una regla explícita. Cuando las lecturas no coinciden, la coordenada queda como estaba y el caso se informa con las dos lecturas. Cada cambio registra su origen y su motivo.

**Consecuencias.** La versión 1.2 aplicó 37 cambios al corpus. La regla se cumplió en su forma estricta en 13, donde dos lecturas deciden lo mismo. En 9 la primera lectura no había decidido y la segunda propone el destino; 7 son sugerencias confirmadas por un lector que las conocía; y 8 se adjudicaron por escrito, por quien generó los artefactos. Fuera del corpus (Biblioteca, medición y serie APX) esta regla no se aplicó: allí hay cambios con una sola lectura, rotulados. Todos son reversibles y están en `data/cambios_1_1_a_1_2.csv`. Si el autor no confirma esta vía, los cambios del corpus se revierten y la política vuelve a ser la de ADR-020.

**Alternativa descartada.** Esperar a una revisión humana para cualquier cambio: se descartó porque dejaba sin aplicar una decisión que se leyó como aceptada. Aplicar todo lo que propone la segunda lectura: se descartó porque una sola lectura no alcanza.

**Nota de la versión 1.3.** El autor la confirmó (D-14.7). Es la regla con que la relectura de la versión 1.3 cambia coordenadas, con una condición más (ADR-030). Los 37 cambios de la versión 1.2 no tienen todavía una confirmación uno por uno (D-13.2).

## ADR-029 · Lectura crítica y responsabilidad indelegable

**Estado:** Aceptada: redacta el principio que el autor enunció el 15 de noviembre de 2026, y el autor confirmó la redacción el 16 (D-14.6).

**Contexto.** El autor escribió: «Yo entiendo que estos niveles de abstracción son difíciles de llevar a la práctica y en consecuencia funcionan como guías y orientación. Un CISO va a tener que leer todo con atención, no creer nada por defecto y, contrastando con su conocimiento y formación, ir aceptando los distintos elementos, artefactos, recomendaciones, con la responsabilidad final indelegable.» Y cerró con una pregunta: «¿Me explico?». Lo enunció como una reflexión sobre cómo funciona el Atlas, no como una decisión de arquitectura, y no vio este texto.

**Decisión.** El Atlas se declara guía y no fuente validada. El README tiene una sección de uso previsto y límites. El paquete procura que cada cifra lleve el estado de su evidencia (quién la generó, si tiene segunda lectura y si tiene revisión humana) y que nada se presente como validado si no lo está; donde no lo logra, es un defecto a corregir.

**Consecuencias.** Los documentos muestran los límites junto a las cifras, y eso los hace más largos. El lector acepta cada elemento por decisión propia.

**Alternativa descartada.** Presentar el paquete como referencia validada después de la revisión crítica: se descartó porque ningún elemento tiene revisión humana.

**Nota de la versión 1.3.** El autor confirmó la redacción (D-14.6).

## ADR-030 · Relectura del corpus con las reglas adoptadas: dos lecturas a ciegas y cuándo cambia una coordenada

**Estado:** Propuesta; rige de forma provisoria desde la versión 1.3. El autor no la vio.

**Contexto.** El 16 de noviembre de 2026 el autor escribió «Acepto el cambio de reglas». Las reglas con texto listo quedaron adoptadas, y varias cambian el alojamiento de pre-ensayos: el corpus tenía que releerse con ellas. ADR-028, que el autor confirmó ese día, dice cuándo cambia una coordenada: cuando dos lecturas coinciden en el destino.

**Decisión.** Cada pre-ensayo se lee a ciegas, sin la coordenada vigente a la vista, con la taxonomía, las reglas base, los enunciados adoptados y las definiciones de trabajo de las subfunciones. Donde la primera lectura difiere de la coordenada vigente, otro lector hace una segunda, también a ciegas. Un eje cambia solo si las dos lecturas coinciden entre sí, difieren del valor vigente, ninguna anotó una pregunta abierta que afecte a ese eje, ninguna declaró confianza baja y el cambio no cae en uno de los puntos que la revisión de la versión candidata dejó abiertos. En cualquier otro caso el valor queda como estaba y el caso se informa con las dos lecturas. El valor anterior pasa a secundario. Todos los cambios entran desde un solo archivo, y vaciándolo se revierten.

**Consecuencias.** La relectura cambió 260 coordenadas en 204 de los 739 pre-ensayos del corpus y dejó 312 casos sin aplicar, que se le informan al autor. Las condiciones sobre la confianza baja y sobre las preguntas abiertas son más estrictas que ADR-028: las agregó el curador con la primera lectura incompleta y antes de que existiera la segunda. La condición sobre los puntos de la revisión se agregó después de revisar la versión candidata, y retiró 154 cambios que esa versión ya aplicaba. Los lectores son automáticos y comparten configuración con quien generó los artefactos. El autor no vio esta regla: está entre lo que tiene que confirmar (D-15.4). Si no confirma los agregados, vale ADR-028 sola; si no quiere la relectura, se revierte entera y el corpus vuelve a las coordenadas de la versión 1.2.

**Alternativa descartada.** Aplicar solo los cambios en que un lector cita una regla adoptada: se descartó porque los lectores no citan las reglas de modo uniforme y ADR-028 no lo exige. Una sola lectura: se descartó porque ADR-028 pide dos. Esperar la revisión humana antes de cambiar nada: se descartó porque dejaba adoptadas unas reglas y un corpus que no las cumplía, que es el choque que la versión 1.2 había encontrado entre D-02 y D-07.

## ADR-031 · Los análisis y los documentos de una versión se conservan con los datos de esa versión

**Estado:** Propuesta; rige de forma provisoria desde la versión 1.3. El autor no la vio.

**Contexto.** La relectura cambia coordenadas. Varios análisis de la versión 1.2 (la revisión crítica, la lectura de D20, la propuesta de remapeo y las cifras con que se presentaron las reglas) se calculaban sobre el corpus vigente: con el corpus releído habrían cambiado en silencio cifras que la versión 1.2 ya había publicado.

**Decisión.** Los análisis de una versión se calculan sobre una copia congelada de los datos de esa versión. Los documentos que describen una versión (el 11 y el 13, y los planes) se publican como estaban, con una nota. Lo nuevo va en un documento nuevo.

**Consecuencias.** El paquete guarda una copia de los datos de las versiones anteriores y pesa más. Un mismo paquete trae cifras de dos momentos, cada una en el documento de su versión, y la nota de cada documento histórico lo dice. Lo que la versión 1.2 afirmaba sobre sí misma no se reescribe: las erratas se informan aparte.

**Alternativa descartada.** Recalcular todo sobre el corpus vigente: se descartó porque altera cifras ya publicadas. Quitar los documentos históricos: se descartó porque son el registro de lo que se decidió y por qué.

## Registro de aceptación

| Decisión | Resultado | Fecha | Nota |
|---|---|---|---|
| ADR-013 | Aceptada | 15-nov-2026; lectura confirmada el 16-nov-2026 | Aceptación en bloque, confirmada con D-14.1 |
| ADR-014 | Aceptada | 15-nov-2026; lectura confirmada el 16-nov-2026 | Aceptación en bloque, confirmada con D-14.1 |
| ADR-015 | Sustituida | 15-nov-2026; lectura confirmada el 16-nov-2026 | Aceptación en bloque, confirmada con D-14.1 |
| ADR-016 | Aceptada | 15-nov-2026; lectura confirmada el 16-nov-2026 | Aceptación en bloque, confirmada con D-14.1 |
| ADR-017 | Aceptada | 15-nov-2026; lectura confirmada el 16-nov-2026 | Aceptación en bloque, confirmada con D-14.1 |
| ADR-018 | Aceptada | 15-nov-2026; lectura confirmada el 16-nov-2026 | Aceptación en bloque, confirmada con D-14.1 |
| ADR-019 | Aceptada | 15-nov-2026; lectura confirmada el 16-nov-2026 | Aceptación en bloque, confirmada con D-14.1 |
| ADR-020 | Aceptada | 15-nov-2026; lectura confirmada el 16-nov-2026 | Aceptación en bloque, confirmada con D-14.1 |
| ADR-021 | Aceptada | 15-nov-2026; lectura confirmada el 16-nov-2026 | Aceptación en bloque, confirmada con D-14.1 |
| ADR-022 | Aceptada | 15-nov-2026; lectura confirmada el 16-nov-2026 | Aceptación en bloque, confirmada con D-14.1 |
| ADR-023 | Aceptada | 15-nov-2026; lectura confirmada el 16-nov-2026 | Aceptación en bloque, confirmada con D-14.1 |
| ADR-024 | Aceptada | 15-nov-2026; lectura confirmada el 16-nov-2026 | Aceptación en bloque, confirmada con D-14.1 |
| ADR-025 | Aceptada | 15-nov-2026; lectura confirmada el 16-nov-2026 | Aceptación en bloque, confirmada con D-14.1 |
| ADR-026 | Aceptada | 16-nov-2026 | Confirmada con D-14.7 |
| ADR-027 | Aceptada | 16-nov-2026 | Confirmada con D-14.7 |
| ADR-028 | Aceptada | 16-nov-2026 | Confirmada con D-14.7 |
| ADR-029 | Aceptada | 16-nov-2026 | Confirmada con D-14.6 |
| ADR-030 | Propuesta; rige de forma provisoria | — | El autor no la vio |
| ADR-031 | Propuesta; rige de forma provisoria | — | El autor no la vio |

La aceptación no es la aprobación de los conjuntos de cambios del grafo, que tienen su propio registro en `changesets/proposed/`.

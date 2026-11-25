> **Registro de la versión 1.3 (16 de noviembre de 2026).** Este documento se conserva tal como se publicó. Las cifras, los estados y los archivos que cita corresponden a esa versión. El estado vigente está en `docs/15_Decisiones_delegadas_y_relectura_1_4.md` y en los documentos 16 a 19.

# Grafo de conocimiento del Frontier CISO Atlas

**Frontier CISO Atlas 1.3** · Taxonomía 6.0 (reglas de asignación, revisión 2) · Ontología 2.1.0 · GM-24 V7.1 · 16 de noviembre de 2026 · Estado: decisiones de diseño confirmadas por el autor; reglas adoptadas según la lectura del curador y corpus releído a ciegas por lectores automáticos, con una lectura para todos y dos donde la primera difería; contenido candidato, sin validación humana

## 1. Estado

Existe un **grafo candidato** con 5.058 nodos y 28.249 relaciones, construido a partir de la Taxonomía 6.0, la base de referencia, el GM-24 V7.1, los 739 pre-ensayos categorizados, la Biblioteca cognitiva y el catálogo de indicadores del Modelo Operativo CISO 365 2.0. Desde la versión 1.2 incluye también, como capa de ampliación, los 16 pre-ensayos de la serie APX.

**Qué significa que valida.** La estructura del grafo se comprueba contra la ontología 2.1.0 con 19 de sus 37 reglas, y el resultado es de 0 errores y 77 advertencias. Es una validación de estructura: tipos, pares permitidos, propiedades obligatorias, catálogos y cardinalidades. No dice nada sobre si el contenido es correcto, y las otras 18 reglas piden juicio humano o datos que el grafo no tiene (sección 3). Las 77 advertencias son los pre-ensayos del plano A que nombran productos de un proveedor.

En la versión 1.1 tenía 5.041 nodos y 29.887 relaciones; en la 1.2, 5.058 y 28.142. La versión 1.2 tiene menos relaciones que la 1.1 porque la revisión crítica retiró del grafo afirmaciones que no se sostenían (sección 2.4). La versión 1.3 tiene los mismos 5.058 nodos y 107 relaciones más: la diferencia está en las clasificaciones secundarias, porque el valor anterior de cada eje que cambió con la relectura queda como secundario (sección 2.8).

No es un grafo aprobado. Cuatro razones:

1. Se apoya en **pre-ensayos**, no en ensayos. No hay ningún ensayo cargado.
2. La categorización es una **propuesta** asistida por agentes. La versión 1.3 la releyó completa a ciegas con lectores automáticos, y esa relectura cambió parte de las coordenadas. No tiene ninguna revisión humana.
3. Aceptaste la taxonomía y la ontología como base de trabajo el 15 de noviembre de 2026 y confirmaste esa lectura el 16. **Ni la aceptación ni la confirmación son la aprobación de los conjuntos de cambios**, que siguen el procedimiento de la sección 8.
4. Lo que vino de tus otras bases hereda su estado: la base de la Biblioteca se declara «propuesta para revisión, no aplicada al grafo», y el catálogo de indicadores, «propuesta de base, sujeta a validación».

Por eso todos los nodos y relaciones llevan estado «candidato» y los 16 conjuntos de cambios llevan estado «propuesto».

## 2. Qué contiene

### 2.1 Nodos por tipo

| Tipo de entidad | Módulo | Nodos |
|---|---|---|
| `Precursor` | OT | 755 |
| `Question` | OT | 595 |
| `CognitiveBias` | O09 | 524 |
| `Concept` | OT | 487 |
| `FrameworkElement` | OT | 469 |
| `HumanCapability` | O09 | 392 |
| `SecurityIndicator` | O10 | 244 |
| `MentalModel` | O09 | 214 |
| `ProductPractice` | O06 | 180 |
| `MetacognitivePractice` | O09 | 166 |
| `ReferenceArtifact` | OT | 146 |
| `TaxonomyCategory` | OT | 137 |
| `Role` | O02 | 85 |
| `AIAgent` | O05 | 85 |
| `ApprovalGate` | O05 | 85 |
| `Tool` | O05 | 82 |
| `KeyResult` | O10 | 72 |
| `KnowledgeSource` | O05 | 51 |
| `OperationalPractice` | O06 | 50 |
| `AgentSkill` | O05 | 46 |
| `ReferenceBody` | OT | 42 |
| `Competency` | O07 | 41 |
| `LearningUnit` | O07 | 24 |
| `SecurityControl` | O04 | 24 |
| `Objective` | O10 | 24 |
| `ControlProduct` | O04 | 7 |
| `TechnologyProduct` | O04 | 7 |
| `OperatingModel` | O06 | 7 |
| `AgentFleet` | O05 | 7 |
| `AutonomyLevel` | O05 | 5 |
| `GovernanceBody` | O02 | 3 |
| `LearningPath` | O07 | 2 |

### 2.2 Relaciones por tipo

| Relación | Relaciones |
|---|---|
| `CLASSIFIED_IN` | 12.957 |
| `MAPS_TO` | 8.430 |
| `RELATES_TO` | 1.305 |
| `PART_OF` | 1.270 |
| `ADDRESSES` | 595 |
| `SPECIALIZES` | 413 |
| `EXPLAINS` | 379 |
| `INFORMS` | 371 |
| `PERFORMS` | 336 |
| `OPERATES_AT` | 283 |
| `INVOKES` | 268 |
| `EXEMPLIFIES` | 180 |
| `COVERS_CONCEPT` | 165 |
| `SUSTAINED_BY` | 154 |
| `USES_KNOWLEDGE` | 150 |
| `PUBLISHES` | 146 |
| `MEASURES` | 122 |
| `INSTANTIATES` | 120 |
| `EXPOSED_TO` | 117 |
| `TRACKED_BY` | 108 |
| `GATED_BY` | 85 |
| `ADVANCES` | 72 |
| `COUNTERS` | 57 |
| `REQUIRES_COMPETENCY` | 41 |
| `SEQUENCES` | 29 |
| `PRESSURES` | 21 |
| `APPLIES_SKILL` | 21 |
| `REGULATES` | 19 |
| `OWNS` | 14 |
| `REALIZED_BY` | 7 |
| `OPERATED_UNDER` | 7 |
| `SERVES` | 7 |

### 2.3 Conjuntos de cambios propuestos

| Orden | Conjunto | Contenido | Nodos | Relaciones | Depende de |
|---|---|---|---|---|---|
| 1 | CHG-CAND-01 | Taxonomía 6.0: categorías, jerarquía y lentes | 137 | 91 | — |
| 2 | CHG-CAND-02 | Base de referencia: organismos, artefactos, elementos y cruce con dominios | 657 | 1.093 | 01 |
| 3 | CHG-CAND-03 | Currículo TheNextCISO GM-24 V7.1: itinerarios, unidades, conceptos y competencias | 447 | 726 | — |
| 4 | CHG-CAND-04 | Pre-ensayos (739) y su categorización con la Taxonomía 6.0 | 739 | 8.436 | 01, 03 |
| 5 | CHG-CAND-05 | Vínculos editoriales entre pre-ensayos (predicado original y familia normalizada) | 0 | 1.700 | 04 |
| 6 | CHG-CAND-06 | Mapeo de conceptos del GM-24 V7.1 a elementos de marcos (tres niveles; no afirma conformidad) | 0 | 7.559 | 02, 03 |
| 7 | CHG-CAND-07 | Preguntas del CISO, al CISO y de los marcos (595) y su cobertura directa | 595 | 2.765 | 01, 04 |
| 8 | CHG-CAND-08 | Productos-control, modelos operativos y tareas por cadencia (siete instancias de dominio) | 347 | 1.189 | 01, 02, 03 |
| 9 | CHG-CAND-09 | Agentes, flotas, herramientas, conocimiento, habilidades, autonomía y controles de gobierno de agentes | 373 | 1.054 | 02, 08 |
| 10 | CHG-CAND-10 | Indicadores: sub-plan PO-GAC (20, sin coordenada en el Atlas) y catálogo del Modelo Operativo CISO 365 2.0 (224, con coordenada) | 244 | 1.181 | 01, 08 |
| 11 | CHG-CAND-11 | Medición: indicadores que miden las variables homeostáticas, órganos de gobierno a los que informan, objetivos y resultados clave | 99 | 622 | 01, 10 |
| 12 | CHG-CAND-12 | Biblioteca cognitiva del CISO de frontera: 1.404 conceptos tipificados, con su pilar del MCCS (los territorios de la base quedan como propiedad, sin afirmarse como clasificación) | 1.404 | 1.403 | 01 |
| 13 | CHG-CAND-13 | Cobertura pedagógica propuesta entre unidades del GM-24 y conceptos de la Biblioteca (solo los vínculos de selección editorial o de ancla expresa) | 0 | 165 | 03, 12 |
| 14 | CHG-CAND-14 | Prácticas que la Biblioteca propone para contrarrestar sesgos (solo los vínculos que la segunda lectura juzgó sostenibles; no afirman eficacia probada) | 0 | 57 | 12 |
| 15 | CHG-CAND-15 | Propuesta de remapeo a matrices vigentes: vínculos que se agregan (no aplicada al GM-24) | 0 | 7 | 02, 03 |
| 16 | CHG-CAND-16 | Capa de ampliación: 16 pre-ensayos de la serie APX para celdas en blanco (decisión D-10 confirmada por el autor el 16-nov-2026, D-14.3; redacción asistida) | 16 | 201 | 01, 04 |

Cada conjunto tiene un archivo de cabecera y un archivo de operaciones en `changesets/proposed/`, con su huella SHA-256. Desde la versión 1.2 la cabecera declara de qué conjuntos depende y en qué orden se aplica, y cada operación lleva lo necesario para rearmar el grafo: la definición, la versión y el estado del nodo, y un identificador estable de arista derivado de su contenido. Una prueba rearma el grafo solo con los archivos de operaciones y lo compara con el original: los 5.058 nodos y las 28.249 relaciones coinciden.

### 2.4 Qué cambió de la versión 1.1 a la 1.2

- **Agentes del plano B.** El catálogo de 85 agentes había entrado con los campos corridos. Se corrigió en la fuente de trabajo y se comprobó contra los anexos del GM-24. Los puntos de control son ahora los que declara cada anexo, llevan una clase derivada de su texto, y los 85 agentes tienen sus herramientas y sus fuentes de conocimiento. Las habilidades están vinculadas solo en 15 agentes, los de una flota: para las demás, el extracto de los anexos no trae habilidades por agente, y no se comprobó si los anexos las declaran. Los nodos sin ninguna relación bajaron de 145 a 49.
- **Definiciones.** En la versión 1.1, 1.809 nodos no tenían definición. Ahora la tienen todos: la tesis del pre-ensayo para los conceptos del GM-24, el texto de la fuente para preguntas, tareas, objetivos y resultados clave, y una descripción de procedencia donde la fuente no define.
- **Versiones del mapeo.** Cada uno de los 8.430 mapeos lleva la versión contra la que se hizo. En 459 el GM-24 no declara ninguna y el mapeo lo dice; en 855 declara una familia de versiones y no una versión («v4.x»); y 29 van a artefactos que la base registra sin número de versión. Antes llevaban un mismo texto genérico. La validación rechaza un mapeo cuya versión no nombre una versión ni declare su ausencia.
- **Corpus.** 37 pre-ensayos cambiaron de coordenada: por la decisión D-03, que se interpretó como «sí» y que confirmaste el 16 de noviembre de 2026, y por la vía de corrección. El respaldo de cada cambio está en el anexo del documento 07. 77 pre-ensayos que nombran productos de un proveedor o al proveedor quedaron marcados «revisar».
- **Biblioteca.** Los territorios de la base ya no se cargan como clasificación; la cobertura por unidad pasó de 792 vínculos a 165; las prácticas contra sesgos, de 142 a 57; 81 conceptos cambiaron de tipo y 59 pasaron al pilar OS.
- **Medición.** Los 224 indicadores tienen ahora territorio, dominio y subfunción; PR06 quedó sin indicadores; cada vínculo con una variable homeostática dice cuántas lecturas lo sostienen.
- **Serie APX.** Los 16 pre-ensayos entran como capa de ampliación (CHG-CAND-16), con una propiedad que los distingue del corpus base.

El detalle, fila por fila, está en `data/cambios_1_1_a_1_2.csv`.

### 2.5 Biblioteca cognitiva (CHG-CAND-12 a CHG-CAND-14)

Los 1.404 conceptos de tu base «Integración Atlas 1404 – GM-24» entran como nodos candidatos. La base los propone a todos como `Concept`, porque la ontología 1.0.0 no tenía tipos cognitivos; aquí reciben un tipo del módulo de cognición y el tipo original queda como propiedad.

| Tipo | Conceptos | Categorías de la Biblioteca de las que provienen |
|---|---|---|
| `CognitiveBias` | 524 | sesgo cognitivo (430), falacia lógica (45), factor humano (19), otro constructo cognitivo (15), metacognición y juicio epistémico (6), modelo mental (4), mindset (4), práctica de decisión (1) |
| `HumanCapability` | 392 | mindset (135), capacidad cognitiva (121), habilidad socioemocional (85), metacognición y juicio epistémico (23), función ejecutiva (22), factor humano (3), otro constructo cognitivo (3) |
| `MentalModel` | 214 | modelo mental (195), otro constructo cognitivo (7), metacognición y juicio epistémico (5), factor humano (3), práctica de decisión (2), mindset (2) |
| `MetacognitivePractice` | 166 | práctica de decisión (143), metacognición y juicio epistémico (23) |
| `Concept` | 108 | otro constructo cognitivo (65), factor humano (37), metacognición y juicio epistémico (4), práctica de decisión (1), función ejecutiva (1) |

- **Tipos.** La regla asigna el tipo por categoría. Un revisor leyó los 213 conceptos de las tres categorías mixtas y una muestra de 120 de las demás, y 81 conceptos cambiaron de tipo. Todas las categorías mezclan tipos; las de mentalidades y prácticas de decisión necesitan una revisión completa (decisión D-12). Las 45 falacias se cargan con el tipo de sesgo.
- **Definiciones.** 1.049 de las 1.404 definiciones están respaldadas por una fuente en la base; las otras 355, una de cada cuatro, son derivadas del nombre. El estado está en cada nodo y en el CSV.
- **Pilar.** 59 conceptos llevan el pilar OS (funciones ejecutivas y factores humanos que son estados o condiciones de la decisión) y 1.344, el pilar MM; uno más, META-0060, figura con MM en la base pero es un alias del propio pilar y no se clasifica. La habilidad socioemocional quedó en MM: el revisor propone llevarla a OS o a DO, y lo decidís vos.
- **Territorios.** No se cargan como clasificación. En la base son un valor por categoría y no una lectura del concepto: 97 % de la categoría «sesgo cognitivo» lleva T01 y T04, 89 % de la categoría «modelo mental» lleva solo T03, y 97 conceptos llevan más de tres territorios, por encima de la cardinalidad de la taxonomía. Quedan como propiedad del nodo y en el CSV. Con esa reserva, 315 conceptos tienen T01 como único territorio y 568 lo llevan entre varios. Derivarlos por lectura es la decisión D-12.
- **Cobertura por unidad (CHG-CAND-13).** De los 1.653 vínculos que propone la base se cargan 165: 141 por selección editorial de la caja de 72 y 24 por ancla expresa de la guía de caso. No se cargan los 627 de coincidencia temática o de etiqueta, donde los revisores encontraron homonimias (la palabra que une el concepto con la unidad significa otra cosa en cada lado), ni los 861 que la propia base marca como débiles. 72 conceptos quedan con al menos una unidad. La confianza es la editorial de la base (141 con confianza media y 24 con confianza alta editorial) y el método se informa aparte.
- **Prácticas contra sesgos (CHG-CAND-14).** La versión 1.1 cargaba 142 vínculos. Una segunda lectura, uno por uno, sostuvo 57, encontró débiles 77 (textos genéricos o fórmulas aplicadas a sesgos que la práctica no trata) e incorrectos 8. Se cargan los 57: 27 con un texto propio de la ficha del sesgo, 24 con una fórmula que la base repite en varias fichas y 6 con el texto de la definición de la práctica. Unen 14 prácticas con 51 sesgos, es decir, 10 % de los 524 sesgos de la Biblioteca. Dicen qué práctica propone la base frente a un sesgo; no afirman eficacia probada. Al repetir la extracción con los tipos corregidos aparecen 6 pares más, que no se cargan porque no tienen segunda lectura.
- **Equivalencias con el corpus.** Un revisor comparó la Biblioteca con el currículo y encontró 21 conceptos que nombran lo mismo que un concepto del GM-24 y 91 relacionados. No se cargan, porque la ontología 2.1.0 no tiene una relación para declararlos; están en `data/equivalencias_biblioteca_corpus.csv`. La Biblioteca tiene además conceptos repetidos dentro de sí misma: 45 grupos y 27 pares, en `data/biblioteca_grupos_mismo_concepto.csv` y `data/biblioteca_dobletes_internos.csv`.

### 2.6 Medición (CHG-CAND-10 y CHG-CAND-11)

El grafo usa el catálogo de 224 indicadores del Modelo Operativo CISO 365 2.0. El catálogo 1.2 tenía 70: los 64 indicadores K01 a K64 y seis del sistema de gestión (KSG01 a KSG06), que la versión 1.1 no había reconocido como heredados.

- **Coordenada.** Los 70 indicadores del catálogo 1.2 heredan territorio, dominio y subfunción. En tres la revisión corrigió el dominio: K60 pasa a D28 (mide la prueba de eficacia de los controles) y K50 y K51 pasan a D01 y D02 por la regla 7. Los otros 154 recibieron territorio y dominio de un revisor que leyó cada indicador (96 con confianza alta, 55 con confianza media y 3 con confianza baja); es una sola lectura y así queda rotulada.
- **Subfunción.** 66 indicadores que no tenían subfunción la recibieron por lectura (43 con confianza alta, 21 con confianza media y 2 con confianza baja). En los demás indicadores nuevos la subfunción se deriva de la categoría de CSF 2.0 que declara el catálogo: se asigna la única subfunción de su función cuyo primer vínculo es esa categoría. Esa es la regla que el guion aplica; la versión 1.1 la describía mal. Como no hay lectura del indicador, esas clasificaciones llevan confianza baja.
- **Función.** La función de un indicador es la de su subfunción en el Atlas, que puede diferir de la función de su categoría de CSF. Difieren en 13 indicadores; el CSV trae las dos columnas.
- **PR06 y RC05.** PR06 queda **sin indicadores**. Los cuatro que la versión 1.1 ubicaba allí (K36, K159, K160 y K193) miden segmentación y acceso de red, no resiliencia de la infraestructura ni protección física o ambiental: volvieron a PR03. Dos revisores llegaron a eso por separado. RC05 conserva K189. Dominios sin indicador primario: D19, D22, D23 y D27.
- **Comprobación.** Los seis indicadores KSG sirven de control, porque los revisores propusieron su coordenada sin conocer la del catálogo 1.2: coincidieron en el territorio en 4 de 6, en el dominio en 4 de 6 y en la subfunción en 4 de 5.
- **Variables homeostáticas.** 71 vínculos entre indicadores y variables, con papel principal o de apoyo. Son **indicadores candidatos**: ninguna variable tiene unidad, umbral ni responsable del límite. En 49 las dos lecturas coinciden en el vínculo y en el papel, en 14 coinciden solo en el vínculo, 5 los consideró y descartó la segunda lectura y 3 tienen una sola lectura. El papel principal se conserva solo donde las dos lecturas coinciden: 6 pasaron a apoyo. La segunda lectura propuso además 36 vínculos que no se cargaron; están en el CSV como candidatos.

| Variable | Indicadores principales | Indicadores de apoyo |
|---|---|---|
| HV01 Exposición residual frente al apetito de riesgo | K24, K25, K26, K87, K93 | K86, K140, K188, K63 |
| HV02 Autoridad delegada frente a capacidad de supervisión | K50, K88, K98, KX13, KX15, K167 | K175, KX01, KX05, KX06, KSG03, K165 |
| HV03 Ritmo de cambio frente a capacidad de absorción | K20, K90, K116 | K69, K78, K101, K121, K119, K18, K70, K128 |
| HV04 Confianza de las partes interesadas sostenida por evidencia | K57, K58, K60, K96, KSG05 | K59, K80, K23, K61, K189, K191, KSG06, KX04, K14, K82 |
| HV05 Carga cognitiva frente a capacidad de decisión | K125, K101, K95 | K01, K02, K03, K168, K169, K12, K13, K05, K170 |
| HV06 Continuidad de los servicios críticos | K29, K30, K47, K28 | K21, K27, K56, K181, K186, KX08, K16, K185 |

- **Órganos de gobierno.** 212 indicadores informan al menos a uno de tres órganos (Directorio y síndicos: 70; CEO, CFO y comité ejecutivo: 92; CISO y comité de seguridad: 209). Esos tres nodos son audiencias del catálogo y mezclan roles y órganos. Un revisor observó que ningún órgano puede atender esa cantidad de indicadores; es una observación sobre el catálogo, que este paquete no modifica (`data/observaciones_catalogo_ciso365.csv`).
- **Objetivos y resultados clave.** 24 objetivos y 72 resultados clave del plan de referencia; 69 tienen un indicador que los sigue y el resto son hitos.
- **Catálogo.** Este paquete carga el catálogo 2.0. El proyecto tiene además una edición 2.1 del modelo operativo; no se comprobó si modifica el catálogo.

### 2.7 Propuesta de remapeo (CHG-CAND-15)

Solo los 7 vínculos que la propuesta agrega, rotulados como propuesta. Los cambios de nombre y los retiros no generan aristas: el mapeo heredado del GM-24 no se modificó. El detalle está en `04_Base_de_Referencia.md`.

### 2.8 Qué cambió de la versión 1.2 a la 1.3

- **Clasificación primaria de los pre-ensayos.** La relectura cambió 270 clasificaciones primarias: 260 en 204 pre-ensayos del corpus y 10 en 8 de la serie APX. Cada una de esas relaciones `CLASSIFIED_IN` lleva el valor nuevo, el método «versión 1.3: …», la menor de las confianzas que declararon los dos lectores y el valor anterior en `previous_value`. En 37 de los cambios de subfunción cambia también la función, y la relación de función lleva el mismo respaldo. El valor anterior queda como clasificación secundaria, y por eso el grafo tiene 107 relaciones de clasificación más que en la versión 1.2. Ningún otro tipo de relación cambió de cantidad.
- **Una errata de la versión 1.2, corregida.** En el grafo publicado de la 1.2, los 37 pre-ensayos que habían cambiado de coordenada tienen 394 relaciones de clasificación además de la del valor que cambió (las de los ejes que no cambiaron y las secundarias del eje que cambió), y las 394 dicen en el campo `method` que el eje fue cambiado. Es un error del guion de esa versión: el valor de esas relaciones es correcto y el rótulo no. Aquí esas relaciones llevan el método del clasificador. La versión 1.2 publicada no se modificó.
- **Lo que no cambió.** La ontología, los tipos de nodo, la Biblioteca, la medición, los mapeos a marcos y la propuesta de remapeo son los de la versión 1.2. Decidiste no revisar la Biblioteca (D-12), y lo que está cargado de ella queda como estaba.
- **Lo que la relectura no tocó en el grafo.** El horizonte, las fuerzas, los mecanismos y el pilar MCCS de cada pre-ensayo son los del clasificador. Las preguntas, los indicadores y los conceptos de la Biblioteca conservan su coordenada: no se releyeron.

El detalle, fila por fila, está en `data/cambios_1_2_a_1_3.csv`.

## 3. Cómo se construyó y cómo se validó

El guion `scripts/construir_grafo.py` lee los catálogos de `data/`, crea nodos y relaciones y aplica la validación determinista antes de escribir. De las 37 reglas de la ontología comprueba 19:

| Regla | Nombre | Cómo se comprueba |
|---|---|---|
| SV-001 | Identificador válido | en parte: un identificador repetido con otro tipo es error; las repeticiones del mismo tipo se cuentan y se conserva la primera declaración |
| SV-002 | Tipo reconocido | tipo de nodo y de relación contra los diccionarios |
| SV-003 | Propiedades obligatorias | nombre y descripción no vacíos en todos los nodos; identificador, tipo, versión y estado los fija la carga |
| SV-004 | Integridad referencial | origen y destino de cada arista existen |
| SV-006 | Versionado | por construcción: cada conjunto de cambios declara esquema, ontología y taxonomía |
| SV-007 | Catálogo de la versión declarada | cada clasificación apunta a una categoría del eje que declara, y el eje está en el catálogo de ejes |
| SV-008 | Par permitido | par de tipos permitido cuando la relación lo define |
| SV-101 | Compatibilidad de dominio | tipo de origen permitido |
| SV-102 | Compatibilidad de rango | tipo de destino permitido |
| SV-105 | Evidencia material | en parte: el campo de evidencia no está vacío; no se comprueba que sea evidencia y no solo procedencia |
| SV-106 | Contexto obligatorio | contexto presente en las relaciones que lo exigen |
| SV-109 | Pre-ensayo no es ensayo | en parte: ningún nodo que no sea ensayo lleva identificador de ensayo; no hay ensayos cargados |
| SV-112 | Autonomía con compuerta | cada agente en L2 o superior tiene punto de control; cada tarea en L2 o superior tiene un agente ejecutor con punto de control o no tiene agente |
| SV-113 | Mapeo con fuerza y versión | fuerza, tipo de vínculo, versión del artefacto y método presentes en cada MAPS_TO |
| SV-114 | Clasificación con rol | rol, versión de taxonomía, método y confianza presentes y dentro de catálogo; a lo sumo un primario por eje |
| SV-117 | Modelo de referencia de la homeostasis | ejes permitidos en REGULATES y PRESSURES entre categorías |
| SV-118 | Medición en el modelo de referencia | MEASURES hacia una categoría solo sobre el eje HV y como modelo de referencia |
| SV-208 | Estado de candidato | todos los nodos y aristas quedan en estado candidato |
| SV-209 | Vigencia de la referencia | cada artefacto de referencia tiene versión, fecha, estado y fecha de verificación |

No comprueba 18: SV-005, SV-103, SV-104, SV-107, SV-108, SV-110, SV-111, SV-115, SV-116, SV-201, SV-202, SV-203, SV-204, SV-205, SV-206, SV-207, SV-210, SV-211. Piden juicio humano (por ejemplo, que una relación potencial no se presente como hecho, o que no se fusionen conceptos distintos) o datos que el grafo candidato no tiene.

**Autonomía con punto de control (SV-112).** La versión 1.1 daba por cumplida esta regla con una justificación que el propio guion insertaba. Ahora se comprueba con los datos: 92 de las 92 asignaciones de nivel L2 o superior a agentes tienen un punto de control declarado en su anexo; de las 139 tareas con ese nivel, 132 tienen un agente ejecutor con punto de control y 7 no tienen agente en el catálogo (las ejecutan personas, y la arista lo dice).

**Resultado:** 0 errores, 77 advertencias (de la comprobación propia PAQ-01, que no es una de las 37 reglas: pre-ensayos del plano A que nombran un producto o un proveedor), 0 relaciones duplicadas descartadas, y todos los elementos de marco citados por el mapeo del GM-24 resueltos.

**Límites de la validación que conviene tener presentes.**

- El campo de evidencia contiene, en 15.906 de las 28.249 relaciones (56 %), un rótulo de procedencia de la carga y no la evidencia del vínculo. La regla que exige evidencia se cumple porque el campo no está vacío. Separar los dos campos queda pendiente.
- 1.069 clasificaciones declaran la versión 5.3 de la taxonomía: son las de las preguntas heredadas de la matriz consolidada y las de los indicadores del catálogo 1.2. Sus códigos siguen vigentes en la 6.0, pero no pasaron por una lectura de migración.
- La confianza de una clasificación es la que declaró quien la propuso. No es una medida.
- El mapeo del GM-24 a marcos entra con los valores del GM-24: 4.326 de sus 7.559 vínculos llevan fuerza «fuerte» y vínculo «cubre». 4.128 se generaron por herencia de la unidad y regla por palabra clave, sin vínculo explícito: indican afinidad, no cobertura comprobada. La consulta P12 muestra el método junto a la fuerza.

## 4. Qué quedó fuera y qué falta integrar

- **123 vínculos editoriales** apuntan a identificadores que no están en el corpus de 739 pre-ensayos y no se cargaron.
- **52 tipos de entidad** de la ontología no tienen instancias. 39 describen una organización concreta (activos, escenarios de riesgo, evidencia, decisiones, autoridad delegada, acciones de agentes), que el Atlas de referencia no contiene. Los otros 13 son tipos del propio Atlas o del currículo que todavía no tienen instancias: `LearningOutcome`, `LearningActivity`, `Assessment`, `LearningArtifact`, `Catalyst`, `Inhibitor`, `HomeostaticMechanism`, `Essay`, `Claim`, `Source`, `OntologyVersion`, `ChangeSet`, `HomeostaticVariable`. Las fuerzas, los mecanismos y las variables del eje H existen como categorías de la taxonomía y no como instancias de su tipo; las fuentes, las versiones y los conjuntos de cambios están en tablas y en propiedades, no en nodos.
- **La Biblioteca y la medición están en el grafo casi sin integrar.** 1.280 de los 1.404 conceptos de la Biblioteca solo tienen su tipo y su pilar. No hay ninguna relación entre la Biblioteca y el corpus, ni entre los indicadores y el corpus: se encuentran solo a través de la taxonomía.
- **2.555 nodos** están marcados «revisar» para la edición pública. La marca se aplica por procedencia: todo lo del plano B, que nombra productos; todo lo de la Biblioteca y lo del catálogo CISO 365, que son bases tuyas sin publicar; los pre-ensayos que nombran productos de un proveedor, y los 16 pre-ensayos de la serie APX, que son de redacción asistida.
- **49 nodos no tienen ninguna relación:** 33 `AgentSkill`, 8 `TaxonomyCategory`, 5 `Tool`, 2 `AutonomyLevel` y 1 `Concept`. Los ocho factores de contexto del eje H no participan del modelo de referencia.
- **Etiquetas repetidas.** 34 grupos de nodos del mismo tipo comparten etiqueta (93 nodos). Seis títulos del corpus se repiten en pre-ensayos de unidades distintas; esos nodos llevan además una etiqueta calificada con su unidad.
- **Roles.** Los 85 nodos de rol salen de los textos de las tareas, y muchos son combinaciones de roles. Cargar roles atómicos y la matriz de responsabilidades del plano B queda pendiente.
- **Ensayos:** ninguno.

## 5. Qué preguntas responde hoy

De las 22 preguntas de competencia, 7 se responden, 9 en parte y 6 todavía no. Sobre las 20 originales son 6, 8 y 6.

La versión 1.1 informaba 13 respondibles. No hubo retroceso: cambió el criterio. Antes el estado era una etiqueta escrita en el guion, y bastaba con que la consulta devolviera filas. Ahora el guion lo deriva de tres datos: si la pregunta puede expresarse con la ontología, qué parte de su universo cubre la consulta (umbral: 90 %) y si hay un límite declarado. El SQL y las muestras están en `graph/consultas_de_aceptacion.sql` y `graph/resultados_de_aceptacion.md`.

| N.º | Pregunta | Estado | Motivo | Cobertura |
|---|---|---|---|---|
| P01 | ¿Qué activos sostienen una capacidad empresarial crítica? | Todavía no | sin instancias en el grafo | — |
| P02 | ¿Qué escenarios de riesgo pueden afectarla? | Todavía no | no puede expresarse con la ontología 2.1.0 | — |
| P03 | ¿Qué controles contribuyen a mitigar esos escenarios? | Todavía no | sin instancias en el grafo | — |
| P04 | ¿Qué evidencia respalda la efectividad de los controles? | Todavía no | sin instancias en el grafo | — |
| P05 | ¿Qué autoridad puede aceptar el riesgo residual? | Todavía no | no puede expresarse con la ontología 2.1.0 | — |
| P06 | ¿Qué agentes poseen autoridad sobre determinados activos? | Todavía no | sin instancias en el grafo | — |
| P07 | ¿Qué herramientas y acciones están disponibles para esos agentes? | En parte | límite declarado | 85 de 85 |
| P08 | ¿Qué fuerzas condicionan la evolución de una capacidad? | En parte | límite declarado | 27 de 28 |
| P09 | ¿Qué competencias necesita desarrollar un responsable? | En parte | cobertura menor que 90 % | 1 de 85 |
| P10 | ¿Qué unidades GM-24 desarrollan y evalúan esas competencias? | En parte | límite declarado | 41 de 41 |
| P11 | ¿Qué pre-ensayos cubren una coordenada (territorio × dominio × subfunción) y con qué confianza? | Respondible | cobertura de al menos 90 % | 755 de 755 |
| P12 | ¿Qué elementos de qué artefactos de referencia respaldan un concepto y con qué fuerza? | Respondible | cobertura de al menos 90 % | 379 de 379 |
| P13 | ¿Qué agentes ejecutan tareas de un producto-control, con qué nivel de autonomía y bajo qué puntos de control? | Respondible | cobertura de al menos 90 % | 156 de 156 |
| P14 | ¿Qué conceptos del corpus instancia cada producto-control? | Respondible | cobertura de al menos 90 % | 7 de 7 |
| P15 | ¿Qué fuerzas y qué mecanismos homeostáticos tratan los pre-ensayos de un dominio? | Respondible | cobertura de al menos 90 % | 27 de 27 |
| P16 | ¿Qué indicadores miden una variable homeostática y a qué decisión informan? | En parte | límite declarado | 6 de 6 |
| P17 | ¿Qué prácticas metacognitivas contrarrestan los sesgos que pueden distorsionar una decisión? | En parte | límite declarado | 51 de 524 |
| P18 | ¿Qué preguntas tienen un pre-ensayo directo y todavía no tienen un ensayo aprobado? | Respondible | cobertura de al menos 90 % | 595 de 595 |
| P19 | ¿Qué competencias requiere un rol y qué conceptos y unidades las sostienen? | En parte | cobertura menor que 90 % | 1 de 85 |
| P20 | ¿Qué celdas del Atlas no tienen conocimiento (silencios)? | En parte | límite declarado | 224 de 224 |
| P21 | ¿Qué conceptos de la Biblioteca cognitiva propone cubrir cada unidad del GM-24 y con qué confianza editorial? | Respondible | cobertura de al menos 90 % | 24 de 24 |
| P22 | ¿Qué indicadores miden cada subfunción del Atlas y qué subfunciones no tienen indicador? | En parte | límite declarado | 224 de 244 |

Las seis sin respuesta son las que un CISO necesita para decidir en su organización: qué activos sostienen una capacidad, qué escenarios la afectan, qué controles los mitigan, con qué evidencia y quién acepta el riesgo residual. Cuatro necesitan instancias de una organización. Dos (P02 y P05) no pueden expresarse con la ontología 2.1.0 ni siquiera con esas instancias: la relación que falta está pedida en la solicitud OCR-CAND-03.

## 6. Qué se requiere para llegar al grafo aprobado

| N.º | Requisito | Estado en la versión 1.3 | Qué falta | Quién |
|---|---|---|---|---|
| R1 | Aprobar las bases | Aceptadas el 15-nov-2026 como base de trabajo (D-01 a D-10) y confirmadas el 16-nov-2026 (D-14). Reglas adoptadas (D-11) y Biblioteca sin revisar (D-12), según la lectura del curador | Confirmar esas lecturas (D-15), contestar los puntos que dejó abiertos la revisión y las 11 preguntas de las reglas, y decidir D-13.1 y D-13.2 | Autor |
| R2 | Resolver la decisión sobre D20 | Confirmada el 16-nov-2026 (D-14.2). En la versión 1.2 salieron de D20 26 pre-ensayos; después de la relectura D20 tiene 43 | Decidir los 11 casos de la versión 1.2 sin coincidencia (D-13.1) y los que la relectura deja sin resolver | Autor |
| R3 | Revisar la categorización | Releída completa a ciegas en la versión 1.3: 755 pre-ensayos, 483 de ellos con dos lecturas | Revisión humana medida: el documento 14 (sección 7.3) propone la muestra y la regla de decisión. Tu mensaje del 16-nov-2026 no la menciona | Autor, o una persona que él designe |
| R4 | Redactar los ensayos | Sin empezar | Convertir pre-ensayos en ensayos con la plantilla del Atlas, por tandas | Autor |
| R5 | Asignar identificadores de ensayo | Sin empezar | Abrir el registro de identificadores `ESS` | Curador |
| R6 | Extraer conocimiento de cada ensayo | Sin empezar | Por ensayo: afirmaciones, fuentes, conceptos y relaciones | Agente curador, con aprobación |
| R7 | Cargar el contenido del MCCS | Biblioteca cargada y revisada en parte; el 16-nov-2026 decidiste no revisarla (D-12) | Cargar las notas del MCCS y el Documento Maestro del CISO-OS | Autor y agente curador |
| R8 | Vincular indicadores con variables | 71 vínculos candidatos, 49 con dos lecturas que coinciden en el vínculo y en el papel | Unidad, umbral y responsable de cada variable; un indicador para PR06 | Autor |
| R9 | Actualizar los cruces envejecidos | Propuesta de remapeo con sus casos abiertos resueltos; el autor confirmó el 16-nov-2026 que es el pedido para la próxima versión del GM-24 (D-14.3); el cruce propio del Atlas ya usa CCM v4.1 | Adoptarla en la próxima versión del GM-24; revalidar COBIT después del 19-nov-2026 | Autor y curador |
| R10 | Separar la edición pública | 2.555 nodos marcados «revisar» por procedencia | Decidir qué se publica y si los pre-ensayos que desarrollan un producto pasan al plano B | Autor |
| R11 | Poner el flujo bajo control de versiones | Sin empezar | Repositorio con validación automática en cada cambio | Autor |
| R12 | Cumplir las validaciones que exige tu base de la Biblioteca | Duplicados y equivalencias hallados y publicados. Con D-12 cerrada quedan separados | Si se retoma la Biblioteca: resolverlos, aprobar `COVERS_CONCEPT` y reservar identificadores definitivos | Autor y curador |
| R13 | Revisar la ontología | Solicitud OCR-CAND-03 escrita | Decidir sus 16 propuestas en la próxima revisión de la ontología | Autor |
| R14 | Completar la carga | Declarado como pendiente | Migrar las clasificaciones heredadas de preguntas, cargar roles atómicos y la matriz de responsabilidades, y separar evidencia de procedencia | Agente curador |

Las instancias de una organización concreta no son un requisito del Atlas de referencia. Si se quieren responder las preguntas 1 a 6, van en un grafo aparte que usa el Atlas como vocabulario, una vez que la ontología pueda expresarlas.

## 7. Del pre-ensayo al ensayo, y del ensayo al grafo

1. **Elegir** el pre-ensayo y confirmar su coordenada (territorio, dominio, subfunción, horizonte y pilar MCCS).
2. **Redactar** el ensayo en Markdown. El ensayo es la fuente de verdad; el pre-ensayo queda como su origen (`DERIVED_FROM`).
3. **Registrar** el ensayo: identificador, título, versión, ruta y huella.
4. **Extraer** en un archivo acompañante las afirmaciones, las fuentes, los conceptos y las relaciones que el ensayo sostiene.
5. **Proponer** un conjunto de cambios con esos nodos y relaciones, en estado «propuesto».
6. **Validar** con las reglas deterministas. Si hay un error, el conjunto no avanza.
7. **Aprobar.** Una persona revisa y aprueba o rechaza; la decisión queda registrada.
8. **Cargar** en el grafo aprobado. El ensayo hereda la clasificación del pre-ensayo y la relación `ADDRESSES` con sus preguntas pasa del pre-ensayo al ensayo.

### Primera tanda propuesta

Para empezar propongo **35 ensayos**, elegidos con una regla escrita: el pre-ensayo con más preguntas directas de cada dominio; los necesarios para tener al menos 2 por territorio, 2 por función y 4 por pilar MCCS; y los de confianza alta del dominio nuevo D26 y del territorio T01. Solo entran pre-ensayos con confianza alta del clasificador y, desde la versión 1.3, con los tres ejes primarios sostenidos por la relectura: 250 de los 503 de confianza alta. Quedan fuera los que cambiaron de coordenada, porque la confianza del clasificador no vale para el valor nuevo, los que tienen un caso pendiente y aquellos en que una lectura difiere. Por eso D18, D22, D26 y D27 queda sin cubrir: ninguno de sus pre-ensayos tiene confianza alta y la coordenada sostenida por la relectura. La tanda se recalculó después de la relectura.

- Cubre 23 de los 27 dominios que tienen pre-ensayos y responde de forma directa 68 de las 595 preguntas.
- Por territorio: T01 2, T02 3, T03 2, T04 6, T05 6, T06 6, T07 6, T08 4.
- Por pilar MCCS: DO 23, MM 4, NX 4, OS 4.

La confianza es la que el clasificador declaró para la coordenada; no mide la calidad del pre-ensayo. La lista está en `data/primera_tanda_propuesta.csv`. Es una propuesta: podés reemplazarla por otro criterio.

## 8. Cómo se promueve un conjunto de cambios

1. Revisar la cabecera y las operaciones en `changesets/proposed/`.
2. Verificar la huella SHA-256 del archivo de operaciones.
3. Aplicar los conjuntos en su orden: un conjunto depende de los que definen los nodos que sus relaciones usan, y la cabecera los lista.
4. Ejecutar la validación determinista.
5. Registrar la aprobación: quién, cuándo y con qué nota.
6. Mover el conjunto a aprobados y cargarlo. Los nodos y relaciones pasan de «candidato» a «aprobado».

Un conjunto rechazado no se borra: queda con su motivo. Los identificadores `CHG-CAND` son provisionales y no se conservan entre paquetes.

## 9. Archivos

- `graph/frontier_ciso_atlas_candidato.sqlite`: el grafo candidato con el catálogo ontológico.
- `graph/nodos.csv` y `graph/aristas.csv`: exportación plana, con definición, evidencia y contexto.
- `graph/esquema.sql`: esquema de la base.
- `graph/estadisticas_grafo.json`: conteos, reglas comprobadas y resultado de la validación.
- `graph/consultas_de_aceptacion.sql`, `graph/resultados_de_aceptacion.md` y `graph/resultados_de_aceptacion.json`: preguntas de competencia.
- `changesets/proposed/`: 16 conjuntos de cambios con sus operaciones.
- `data/biblioteca_cognitiva_1404.csv`, `data/biblioteca_cognitiva_estadisticas.json` y `data/practicas_contra_sesgos.csv`: la Biblioteca tal como entró al grafo.
- `data/equivalencias_biblioteca_corpus.csv`, `data/biblioteca_grupos_mismo_concepto.csv` y `data/biblioteca_dobletes_internos.csv`: lo que la revisión halló y no se cargó.
- `data/indicadores_ciso365_en_el_atlas.csv`, `data/indicadores_y_variables_homeostaticas.csv`, `data/medicion_estadisticas.json` y `data/observaciones_catalogo_ciso365.csv`: la medición.
- `data/casos_de_navegacion.json`: casos resueltos con el grafo.
- `data/primera_tanda_propuesta.csv`: la primera tanda de ensayos propuesta.
- `data/cambios_1_2_a_1_3.csv` y `data/cambios_1_1_a_1_2.csv`: lo que cambió en cada versión.

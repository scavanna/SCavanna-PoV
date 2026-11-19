> **Registro de la versión 1.3 (16 de noviembre de 2026).** Este documento se conserva tal como se publicó. Las cifras, los estados y los archivos que cita corresponden a esa versión. El estado vigente está en `docs/15_Decisiones_delegadas_y_relectura_1_4.md` y en los documentos 16 a 19.

# Frontier CISO Atlas Core Ontology 2.1.0

**Frontier CISO Atlas 1.3** · Taxonomía 6.0 (reglas de asignación, revisión 2) · Ontología 2.1.0 · GM-24 V7.1 · 16 de noviembre de 2026 · Estado: decisiones de diseño confirmadas por el autor; reglas adoptadas según la lectura del curador y corpus releído a ciegas por lectores automáticos, con una lectura para todos y dos donde la primera difería; contenido candidato, sin validación humana

## 1. Qué cambia

La ontología pasa de la versión 1.0.0 a la 2.1.0 para poder representar tres cosas que la anterior no podía: el GM-24 V7.1 completo, con sus dos planos y su sub-plan de dueño de producto-control y gerente de agentes; el sistema metacognitivo del CISO (MCCS); y la homeostasis del eje H.

**La 2.1.0 contiene a la 2.0.0.** La 2.0.0 fue la propuesta del paquete 1.0. Al cargar la Biblioteca cognitiva y la medición aparecieron tres límites, y la propuesta se revisó. Los cambios están en la sección 1.1.

**Estado en la versión 1.3.** Aceptaste la 2.1.0 como línea base propuesta (decisión D-05) y confirmaste esa aceptación el 16 de noviembre de 2026 (D-14.1). Ni la versión 1.2 ni la 1.3 cambian ningún tipo, ninguna relación ni ninguna regla. La 1.2 corrigió tres metadatos (el control de versiones figura como previsto, OT se declara como grupo transversal y se precisa la definición de una familia de predicados) y dejó una solicitud de cambio, OCR-CAND-03, con lo que la revisión crítica propone para la próxima revisión (sección 1.2). La solicitud sigue sin decidir: tu mensaje del 16 de noviembre no la menciona. De los encargos que aceptaste con las reglas, uno toca el modelo de datos (RP-17.2, registrar el plano como propiedad) y queda en cola, porque antes hay que decidir a qué tipos de nodo se aplica.

| Elemento | 1.0.0 | 2.1.0 | Diferencia |
|---|---|---|---|
| Módulos | 8 | 10 | +2 |
| Tipos de entidad | 57 | 84 | +27 |
| Relaciones | 58 | 93 | +35 (14 más se ampliaron) |
| Reglas semánticas | 21 | 37 | +16 |
| Preguntas de competencia | 10 | 22 | +12 |

**Por qué es una versión mayor.** Casi todo el cambio es aditivo: no se elimina ni se renombra ningún tipo de entidad ni ninguna relación. Es mayor por tres razones que rompen compatibilidad:

1. El producto cambia de nombre: de «AI CISO Atlas Core Ontology» a «Frontier CISO Atlas Core Ontology».
2. Las relaciones `CLASSIFIED_IN` y `MAPS_TO` pasan a exigir propiedades. Una clasificación sin rol, versión de taxonomía, método y confianza ya no es válida; tampoco un cruce sin fuerza, tipo de vínculo, versión del artefacto y método.
3. Se incorpora el estado «candidato» como paso obligatorio previo a «aprobado».

### 1.1 Cambios de la 2.1.0 respecto de la 2.0.0

| Cambio | Elemento | Qué cambia |
|---|---|---|
| Relación ampliada | `CLASSIFIED_IN` | Admite como origen los cuatro tipos cognitivos del módulo O09, para ubicar los conceptos de la Biblioteca cognitiva en territorios y en el pilar del MCCS. |
| Relación ampliada | `MEASURES` | Admite como destino una variable homeostática del catálogo (categoría del eje HV) para expresar el modelo de referencia; la regla SV-118 lo limita a ese eje. La medición de una organización concreta sigue usando instancias de HomeostaticVariable. |
| Relación nueva | `COVERS_CONCEPT` | Cobertura pedagógica propuesta entre una unidad del GM-24 y un concepto; exige confianza editorial y método. No equivale a DEVELOPS ni a CLASSIFIED_IN. |
| Definición precisada | `MetacognitivePractice` | Incluye de forma expresa las prácticas de decisión y análisis, que son una categoría propia de la Biblioteca cognitiva. |
| Regla nueva | `SV-118` | Limita MEASURES hacia categorías de la taxonomía al eje HV y al modelo de referencia. |
| Preguntas de competencia nuevas | P21 y P22 | Cobertura cognitiva por unidad del GM-24 (COVERS_CONCEPT) e indicadores por subfunción. |

Los tres primeros responden a necesidades concretas. `CLASSIFIED_IN` no admitía los tipos cognitivos como origen, de modo que la Biblioteca no podía ubicarse en territorios. `MEASURES` solo apuntaba a instancias de una variable homeostática, y el catálogo las tiene como categorías: la pregunta 16 no podía responderse con aristas válidas. Y la relación entre una unidad de aprendizaje y un concepto es la extensión que pide tu base «Integración Atlas 1404 – GM-24».

### 1.2 Lo que la revisión crítica propone y no se aplicó (OCR-CAND-03)

Los revisores encontraron cosas que la ontología 2.1.0 no puede expresar o que define de forma ambigua. Ninguna se aplicó: cambiar la ontología es una decisión tuya y pide una versión nueva. El detalle, con los hallazgos de origen, está en `data/solicitud_cambio_ontologia_OCR-CAND-03.json`.

| N.º | Tema | Cambio propuesto | Hallazgos |
|---|---|---|---|
| 1 | Relación de equivalencia declarada | Agregar una relación simétrica para declarar que dos nodos nombran el mismo concepto sin fusionarlos, y otra para «relacionado», entre los tipos cognitivos y los conceptos y pre-ensayos del corpus. | C5c-001, C5c-002 |
| 2 | Tipos cognitivos en los vínculos entre conceptos | Admitir los tipos del módulo de cognición como origen y destino de RELATES_TO y SPECIALIZES, y decidir si los vínculos editoriales viven en los conceptos o en los pre-ensayos. | C3-027, C5c-002 |
| 3 | Tipo para las falacias | Dar a las falacias un tipo propio o un subtipo: una falacia es un defecto del argumento y un sesgo, una desviación sistemática del juicio. | C8-016 |
| 4 | Tipo para estados y condiciones | Agregar al módulo de cognición un tipo para los estados y las condiciones que degradan la decisión (fatiga, estrés, carga cognitiva), que hoy quedan como Concept. | C5a-010 |
| 5 | COUNTERS como posibilidad | Redactar la definición como «se propone para contrarrestar», asociarle la regla de posibilidad frente a observación y exigirle una propiedad de evidencia. | C3-025, C8-017 |
| 6 | Rol propio para los mecanismos | Agregar «mecanismo» al catálogo de roles de CLASSIFIED_IN: hoy los mecanismos homeostáticos se cargan con el rol «fuerza». | C3-012 |
| 7 | Catálogos de valores | Declarar en el diccionario los valores admitidos de confianza, rol, fuerza y tipo de vínculo, y el catálogo de ejes. | C3-017, C3-062, C3-045 |
| 8 | Propiedades obligatorias por tipo y por relación | Declarar por tipo las propiedades que su definición enuncia, y como obligatorias las propiedades de arista de las que dependen las reglas (eje, nivel, etapa). | C3-035, C3-036 |
| 9 | Punto de control con clase y con su par de agente y tarea | Dar a ApprovalGate una propiedad obligatoria de clase y un vínculo con el par de agente y tarea al que se aplica. | C3-013 |
| 10 | Relación de delegación | Agregar la relación por la que un rol o una autoridad delega en un agente, con condiciones: es el objeto de la variable HV02. | C3-055 |
| 11 | Escenario de riesgo y lo que afecta; autoridad y aceptación del riesgo; estado y su capacidad | Agregar los vínculos que faltan para que las preguntas de competencia P02, P05 y P08 puedan expresarse. | C3-007 |
| 12 | Pares duplicados y definiciones | Diferenciar con un criterio escrito los 20 pares de tipos admitidos en más de una relación, reescribir las definiciones circulares y las de las relaciones ampliadas, dar notas de frontera a los grupos de tipos que se solapan y renombrar o documentar los pares de relaciones que parecen inversos y no lo son. | C3-033, C3-034, C3-059, C3-060 |
| 13 | Categorías del eje H como catálogo | Elegir una sola representación para variables, fuerzas, mecanismos y contextos: categoría de la taxonomía o tipo de entidad. | C3-037 |
| 14 | Reformular la pregunta P22 y la separación de planos | P22 pregunta qué indicadores «miden» una subfunción y la regla SV-118 no lo admite. Registrar el plano como propiedad obligatoria del nodo para que SV-110 pueda comprobarse. | C3-015, C3-028 |
| 15 | Ancla de HumanCapability | El diccionario ancla HumanCapability en «MCCS (pilar OS a escala individual)», pero la regla de pilar deja en MM a la mayoría de los nodos de ese tipo. Corregir el ancla o la regla de pilar, según lo que el autor decida en D-12.2. | C5a-004 |
| 16 | Regla de neutralidad del plano A | Agregar una regla semántica que compruebe que los nodos del plano A no nombran productos ni proveedores. Hoy el paquete lo comprueba por fuera de las 37 reglas, con la comprobación propia PAQ-01. | C2-076, C8-004 |

## 2. Principios

1. Identidad: todo nodo tiene un identificador único y estable.
2. Semántica explícita: cada tipo y cada relación tiene definición.
3. Separación conceptual: un concepto no es su ensayo ni su control.
4. Procedencia: todo dato dice de dónde salió.
5. Contexto: una afirmación vale en un contexto declarado.
6. Evolución controlada: los cambios pasan por un conjunto de cambios y una aprobación.
7. Sin equivalencia automática: un cruce entre marcos no es una igualdad.
8. Gobierno humano: los agentes proponen y las personas aprueban.
9. **Nuevo.** Separación de planos: el corpus académico (A) y las capacidades contratadas (B) no se mezclan, y B no prueba A.
10. **Nuevo.** Candidato antes que aprobado: todo lo generado entra como candidato y solo una aprobación lo promueve.

## 3. Módulos

| Módulo | Nombre | Responsabilidad | Tipos de entidad |
|---|---|---|---|
| O01 | Enterprise & Strategy | Organización, objetivos, capacidades y procesos empresariales. | 6 |
| O02 | Governance & Accountability | Gobierno, autoridad, políticas, decisiones y excepciones. | 7 |
| O03 | Risk & Resilience | Riesgos, amenazas, consecuencias y tolerancias. | 6 |
| O04 | Technology & Security | Activos, sistemas, identidades, datos, controles y productos-control. | 9 |
| O05 | AI & Autonomous Systems | Modelos, agentes, flotas, herramientas, autonomía y acciones autónomas. | 13 |
| O06 | Operations & Assurance | Eventos, incidentes, modelos operativos, prácticas y evidencia. | 9 |
| O07 | Competency & Learning | Competencias, formación, itinerarios y evaluación. | 7 |
| O08 | Evolution & Transformation | Estados, fuerzas, variables, contextos y transiciones. | 7 |
| O09 | Cognition & Metacognition | Modelos mentales, sesgos, prácticas metacognitivas y capacidades humanas. | 5 |
| O10 | Measurement & Value | Indicadores, objetivos y resultados clave. | 3 |
| OT | Transversales | Conceptos, pre-ensayos, ensayos, preguntas, fuentes, referencias, taxonomía y cambios. | 12 |

Los 84 tipos de entidad se reparten en los 10 módulos y en OT, que es un grupo transversal y no se cuenta como módulo.

## 4. Cómo se representa el GM-24 V7.1

| Elemento del GM-24 V7.1 | Representación en la ontología 2.1.0 |
|---|---|
| Programa GM-24 y sub-plan PO-GAC | `LearningPath` |
| Unidades (24) | `LearningUnit`, con `PART_OF` hacia el programa |
| Conceptos (379) | `Concept`, con `PART_OF` hacia su unidad |
| Pre-ensayos | `Precursor`, con `EXPLAINS` hacia su concepto. Un pre-ensayo no es un ensayo |
| Vínculos editoriales (116 predicados) | Se cargan entre pre-ensayos, no entre conceptos: `SPECIALIZES` para toda la familia de especialización y `RELATES_TO` para las demás, con el predicado original y su familia. Los 379 conceptos del GM-24 se vinculan con sus pre-ensayos por `EXPLAINS` |
| Mapeo a 17 marcos en tres niveles | `MAPS_TO` hacia `FrameworkElement`, con fuerza, tipo de vínculo, versión del artefacto y método. La versión es la que declara el GM-24, o la indicación de que no la declara |
| Rol de dueño de producto-control y gerente de agentes | `Role` |
| Competencias (41) | `Competency`, con `REQUIRES_COMPETENCY` desde el rol y `SUSTAINED_BY` hacia los conceptos |
| Etapas E0 a E5 | `SEQUENCES`, con la etapa como propiedad |
| Controles de gobierno de agentes (24) | `SecurityControl`, con `MAPS_TO` hacia NIST AI RMF, ISO/IEC 42001 y el Top 10 agéntico de OWASP |
| Indicadores (20) | `SecurityIndicator`, con `MEASURES` |
| Niveles de autonomía L0 a L3 (L4 es una extensión del Atlas que el sub-plan no prevé) | `AutonomyLevel`, con `OPERATES_AT` |
| Plano B: ficha del dominio | `ControlProduct`, con `REALIZED_BY` hacia `TechnologyProduct` y `CLASSIFIED_IN` hacia su dominio |
| Plano B: modelo operativo | `OperatingModel`, con `OPERATED_UNDER` |
| Plano B: tareas por cadencia (180) | `ProductPractice`, con `EXEMPLIFIES` hacia una `OperationalPractice` canónica |
| Plano B: catálogo de agentes (85) | `AIAgent`, con `PART_OF` hacia `AgentFleet`, `PERFORMS` hacia las tareas y `GATED_BY` hacia `ApprovalGate`, que lleva el texto del anexo del agente y una clase derivada de ese texto |
| Plano B: herramientas, conocimiento y habilidades | `Tool`, `KnowledgeSource` y `AgentSkill`, con `INVOKES`, `USES_KNOWLEDGE` y `APPLIES_SKILL` |
| Plano B: matriz de responsabilidades | No está cargada. Los roles (`Role`, con `PERFORMS`) salen de las tareas del modelo operativo, y la propiedad del rol PO-GAC sobre productos y flotas (`OWNS`) la fija el guion de carga. Cargar la matriz queda pendiente |
| Plano B: matriz de instanciación | `INSTANTIATES`, del producto-control al concepto |

Dos reglas cuidan la frontera entre planos: una instancia del plano B nunca se presenta como evidencia de un concepto del plano A (SV-110), y una tarea o un agente con autonomía L2 o superior necesita un punto de control humano o la justificación registrada de su ausencia (SV-112). La versión 1.2 comprueba SV-112 con los puntos de control que declaran los agentes: 92 de 92 asignaciones de nivel L2 o superior a agentes y 132 de 139 tareas tienen punto de control; las otras 7 tareas no tienen agente ejecutor en el catálogo y lo dicen. SV-110 no se comprueba, porque el plano no es todavía una propiedad de cada nodo. Lo que el paquete hace es una comprobación propia, fuera de las 37 reglas (PAQ-01): avisa cuando un pre-ensayo del plano A nombra un producto o un proveedor (77).

## 5. Cómo se representan el MCCS y la homeostasis

- **Módulo O09, cognición y metacognición.** Tipos `MentalModel`, `CognitiveBias`, `MetacognitivePractice`, `HumanCapability` y `DecisionRecord`. Relaciones `INFORMED_BY`, `DISTORTS`, `COUNTERS`, `RECORDED_IN`, `REQUIRES_CAPABILITY` y `STRENGTHENS`. Un sesgo «puede distorsionar»: la relación expresa posibilidad y solo se presenta como observada con evidencia. `COUNTERS` se usa aquí con la misma reserva: dice qué práctica propone la Biblioteca frente a un sesgo, no que su eficacia esté probada.
- **Pilar MCCS como lente.** Los pilares MM, OS, DO y NX son categorías de taxonomía; un pre-ensayo o un concepto de la Biblioteca se vincula a su pilar con `CLASSIFIED_IN` y rol «lente».
- **Variables homeostáticas.** Tipo `HomeostaticVariable` y relaciones `REGULATES` (un mecanismo mantiene una variable) y `PRESSURES` (una fuerza la empuja). Entre categorías de la taxonomía expresan el modelo de referencia; entre instancias, lo observado en un contexto.
- **Medición y valor (módulo O10).** Tipos `SecurityIndicator`, `Objective` y `KeyResult`, con `MEASURES`, `INFORMS`, `TRACKED_BY` y `ADVANCES`. Medir no prueba el resultado. Un indicador puede medir una variable homeostática del catálogo; en ese caso la arista declara que expresa el modelo de referencia (regla SV-118).
- **Cobertura pedagógica.** `COVERS_CONCEPT` une una unidad del GM-24 con un concepto que la unidad propone enseñar o ejercitar. No afirma competencia adquirida y no equivale a `DEVELOPS` ni a `CLASSIFIED_IN`.

En el paquete 1.0 los tipos del módulo O09 no tenían instancias. Ahora alojan la Biblioteca cognitiva del CISO de frontera: 1.404 conceptos, tipificados por su categoría.

| Categoría de la Biblioteca | Conceptos | Tipo que da la regla | Tipos en la versión 1.2 |
|---|---|---|---|
| Sesgos cognitivos | 430 | `CognitiveBias` | `CognitiveBias` 430 |
| Modelos mentales | 199 | `MentalModel` | `MentalModel` 195, `CognitiveBias` 4 |
| Prácticas de decisión y análisis | 147 | `MetacognitivePractice` | `MetacognitivePractice` 143, `MentalModel` 2, `Concept` 1, `CognitiveBias` 1 |
| Mentalidades | 141 | `HumanCapability` | `HumanCapability` 135, `CognitiveBias` 4, `MentalModel` 2 |
| Capacidades cognitivas e intelectuales | 121 | `HumanCapability` | `HumanCapability` 121 |
| Otros constructos cognitivos | 90 | `Concept` | `Concept` 65, `CognitiveBias` 15, `MentalModel` 7, `HumanCapability` 3 |
| Habilidades socioemocionales | 85 | `HumanCapability` | `HumanCapability` 85 |
| Factores humanos | 62 | `Concept` | `Concept` 37, `CognitiveBias` 19, `HumanCapability` 3, `MentalModel` 3 |
| Metacognición y virtudes epistémicas | 61 | según la primera palabra de la definición | `HumanCapability` 23, `MetacognitivePractice` 23, `CognitiveBias` 6, `MentalModel` 5, `Concept` 4 |
| Falacias lógicas | 45 | `CognitiveBias` | `CognitiveBias` 45 |
| Funciones ejecutivas | 23 | `HumanCapability` | `HumanCapability` 22, `Concept` 1 |

La regla por categoría es determinista y está en `data/biblioteca_cognitiva_estadisticas.json`. En la versión 1.2 un revisor leyó uno por uno los 213 conceptos de las tres categorías mixtas y una muestra de 120 de las otras ocho: 81 conceptos cambiaron de tipo respecto de la regla y el motivo de cada cambio está en `data/biblioteca_cognitiva_1404.csv`. Tres límites quedan declarados. Todas las categorías mezclan tipos, no solo las tres mixtas: la muestra encontró 8 excepciones en 120, y las categorías mindset y práctica de decisión necesitan una revisión completa (decisión D-12). Las 45 falacias lógicas se cargan como `CognitiveBias`, porque la definición aceptada del tipo las incluye, aunque una falacia es un defecto del argumento y no una desviación del juicio. Y 108 conceptos siguen como `Concept` porque el módulo no tiene un tipo para los estados y las condiciones que degradan la decisión. `DecisionRecord` sigue sin instancias.

## 6. Tipos de entidad nuevos (27)

La última columna indica cuántos nodos de ese tipo hay en el grafo candidato.

| Tipo | Módulo | Definición | Nodos en el grafo candidato |
|---|---|---|---|
| `PolicyException` | O02 | Excepción o anulación aprobada de una política, una línea base o un control, con alcance, justificación y vencimiento. | 0 |
| `ControlProduct` | O04 | Control de seguridad tratado como producto: resultado esperado (función y categoría), alcance (dominio), tecnología que lo realiza y modelo operativo que lo mantiene efectivo; tiene dueño, backlog y evidencia. | 7 |
| `TechnologyProduct` | O04 | Producto o servicio tecnológico contratado que realiza uno o más controles; cambia con las versiones y las licencias del proveedor. | 7 |
| `AutonomyLevel` | O05 | Nivel de autonomía permitido para una acción o un agente (L0 informa; L1 propone; L2 ejecuta con aprobación; L3 ejecuta acciones reversibles con auditoría posterior; L4 autónomo con límites estrictos). | 5 |
| `AgentFleet` | O05 | Conjunto de agentes que opera un producto-control bajo un mismo dueño, con registro, indicadores de riesgo y revisión de desempeño comunes. | 7 |
| `AgentCharter` | O05 | Ficha aprobada de un agente: propósito, tareas, herramientas, límites, autonomía, dueño, indicadores y escalamiento. | 0 |
| `ApprovalGate` | O05 | Punto de control humano asociado a una acción: aprobación previa, auditoría posterior o prohibición de delegar. | 85 |
| `KnowledgeSource` | O05 | Fuente de conocimiento aprobada para un agente, con dueño, etiqueta y procedencia. | 51 |
| `AgentSkill` | O05 | Instrucción o habilidad reutilizable que orienta el comportamiento de un agente en una clase de tareas. | 46 |
| `OperatingAuthorization` | O05 | Autorización formal para operar un agente o una flota, con expediente, vigencia y autoridad que la otorga. | 0 |
| `OperatingModel` | O06 | Modelo operativo de un producto-control: tareas por cadencia, responsables, evidencia e indicadores. | 7 |
| `OperationalPractice` | O06 | Práctica operativa independiente de producto que una tarea concreta ejemplifica. | 50 |
| `ProductPractice` | O06 | Tarea concreta del modelo operativo sobre un producto, con cadencia, responsable, nivel de autonomía recomendado, agente e indicador. | 180 |
| `LearningPath` | O07 | Itinerario formativo que ordena unidades y conceptos por etapas con evidencias de avance. | 2 |
| `HomeostaticVariable` | O08 | Variable esencial que el sistema debe mantener dentro de límites aceptables mientras cambia. | 0 |
| `MentalModel` | O09 | Modelo o marco de razonamiento que orienta cómo se interpreta una situación y se decide. | 214 |
| `CognitiveBias` | O09 | Sesgo, heurística defectuosa o falacia que puede distorsionar un juicio. | 524 |
| `MetacognitivePractice` | O09 | Práctica deliberada de decisión, de análisis o de revisión del propio razonamiento antes, durante o después de decidir. *(definición precisada en la 2.1.0)* | 166 |
| `HumanCapability` | O09 | Capacidad humana que sostiene el desempeño: función ejecutiva, capacidad cognitiva, habilidad socioemocional o mentalidad. | 392 |
| `DecisionRecord` | O09 | Registro de una decisión con sus supuestos, fuentes, alternativas, criterios de revisión y participación de IA. | 0 |
| `SecurityIndicator` | O10 | Indicador de desempeño o de riesgo con definición, fuente, cadencia, umbrales y dueño. | 244 |
| `Objective` | O10 | Objetivo cualitativo y acotado en el tiempo al que contribuyen resultados clave. | 24 |
| `KeyResult` | O10 | Resultado clave medible que evidencia el avance de un objetivo. | 72 |
| `Precursor` | OT | Pre-ensayo: idea central desarrollada de un concepto o de una pregunta; todavía no es un ensayo ni tiene identificador ESS. | 755 |
| `Question` | OT | Pregunta que el CISO formula, que le formulan, que plantea un marco o que integra una serie mayéutica. | 595 |
| `ReferenceBody` | OT | Organismo que publica artefactos de referencia: normalizador, regulador, asociación profesional, fabricante o comunidad. | 42 |
| `ReferenceArtifact` | OT | Artefacto de referencia versionado: marco, norma, catálogo de controles, matriz de técnicas, regulación, cuerpo de conocimiento o informe. | 146 |

## 7. Relaciones nuevas (35)

| Relación | Familia | Definición | Origen → destino | Aristas en el grafo candidato |
|---|---|---|---|---|
| `DERIVED_FROM` | epistemic | Un ensayo deriva de un pre-ensayo; la derivación no traslada aprobación. | Essay → Precursor | 0 |
| `ADDRESSES` | epistemic | Un pre-ensayo o un ensayo aborda de forma directa una pregunta. | Precursor, Essay → Question | 595 |
| `PROBES` | epistemic | Una pregunta interroga un concepto o un pre-ensayo. | Question → Concept, Precursor | 0 |
| `RELATES_TO` | epistemic | Vínculo editorial entre conceptos o pre-ensayos; conserva el predicado original y su familia normalizada. | Concept, Precursor → Concept, Precursor | 1.305 |
| `PUBLISHES` | mapping | Un organismo publica un artefacto de referencia. | ReferenceBody → ReferenceArtifact | 146 |
| `REALIZED_BY` | technology | Una tecnología realiza un producto-control. | ControlProduct → TechnologyProduct | 7 |
| `OPERATED_UNDER` | operations | Un producto-control se opera bajo un modelo operativo. | ControlProduct → OperatingModel | 7 |
| `EXEMPLIFIES` | operations | Una tarea sobre un producto ejemplifica una práctica operativa independiente de producto. | ProductPractice → OperationalPractice | 180 |
| `PERFORMS` | operations | Un rol o un agente ejecuta una tarea del modelo operativo. | Role, AIAgent → ProductPractice | 336 |
| `OPERATES_AT` | ai | Un agente, una tarea o una acción opera en un nivel de autonomía. | AIAgent, ProductPractice, AutonomousAction → AutonomyLevel | 283 |
| `GATED_BY` | ai | Un agente, una tarea o una acción queda sujeta a un punto de control humano. | AIAgent, ProductPractice, AutonomousAction → ApprovalGate | 85 |
| `CHARTERED_BY` | ai | Un agente se rige por su ficha aprobada. | AIAgent → AgentCharter | 0 |
| `AUTHORIZED_BY` | governance | Un agente o una flota opera con una autorización formal vigente. | AIAgent, AgentFleet → OperatingAuthorization | 0 |
| `USES_KNOWLEDGE` | ai | Un agente usa una fuente de conocimiento aprobada. | AIAgent → KnowledgeSource | 150 |
| `APPLIES_SKILL` | ai | Un agente aplica una habilidad reutilizable. | AIAgent → AgentSkill | 21 |
| `SERVES` | ai | Una flota de agentes sirve a un producto-control. | AgentFleet → ControlProduct | 7 |
| `INSTANTIATES` | mapping | Un producto-control (plano B) instancia un concepto del corpus (plano A) sin modificarlo. | ControlProduct, ProductPractice → Concept | 120 |
| `EXPOSED_TO` | risk | Un agente o una herramienta queda expuesto a una clase de riesgo catalogada. | AIAgent, Tool → FrameworkElement, RiskScenario | 117 |
| `EXCEPTS` | governance | Una excepción suspende o modifica la aplicación de una política, un control o un objetivo, con vencimiento. | PolicyException → Policy, SecurityControl, ControlObjective | 0 |
| `REQUIRES_COMPETENCY` | learning | Un rol requiere una competencia. | Role → Competency | 41 |
| `SUSTAINED_BY` | learning | Una competencia se sostiene en conceptos del corpus. | Competency → Concept | 154 |
| `SEQUENCES` | learning | Un itinerario ordena unidades o conceptos en etapas. | LearningPath → LearningUnit, Concept | 29 |
| `MEASURES` | measurement | Un indicador mide un resultado, un control, un producto-control, un agente, una flota o una variable homeostática; medir no prueba el resultado. | SecurityIndicator → SecurityOutcome, SecurityControl, ControlProduct, AIAgent, AgentFleet, HomeostaticVariable, ProductPractice, TaxonomyCategory | 122 |
| `INFORMS` | measurement | Un indicador informa una decisión o a un órgano de gobierno. | SecurityIndicator → Decision, GovernanceBody | 371 |
| `TRACKED_BY` | measurement | Un resultado clave se sigue con un indicador. | KeyResult → SecurityIndicator | 108 |
| `ADVANCES` | measurement | Un resultado clave hace avanzar un objetivo; un objetivo hace avanzar un objetivo empresarial o un resultado de seguridad. | KeyResult, Objective → Objective, BusinessObjective, SecurityOutcome | 72 |
| `REGULATES` | evolution | Un mecanismo homeostático mantiene una variable dentro de límites aceptables. Entre categorías de la taxonomía expresa el modelo de referencia; entre instancias, lo observado en un contexto. | HomeostaticMechanism, TaxonomyCategory → HomeostaticVariable, TaxonomyCategory | 19 |
| `PRESSURES` | evolution | Una fuerza empuja una variable homeostática fuera de sus límites o la restringe. Entre categorías de la taxonomía expresa el modelo de referencia; entre instancias, lo observado en un contexto. | Catalyst, Inhibitor, TaxonomyCategory → HomeostaticVariable, TaxonomyCategory | 21 |
| `INFORMED_BY` | cognition | Una decisión se apoya en un modelo mental o en evidencia. | Decision → MentalModel, Evidence | 0 |
| `DISTORTS` | cognition | Un sesgo puede distorsionar una decisión o un resultado de evaluación; es potencial salvo evidencia. | CognitiveBias → Decision, AssessmentResult | 0 |
| `COUNTERS` | cognition | Una práctica metacognitiva contrarresta un sesgo. | MetacognitivePractice → CognitiveBias | 57 |
| `RECORDED_IN` | cognition | Una decisión queda asentada en un registro de decisión. | Decision → DecisionRecord | 0 |
| `REQUIRES_CAPABILITY` | cognition | Un rol o una competencia requiere una capacidad humana. | Role, Competency → HumanCapability | 0 |
| `STRENGTHENS` | cognition | Una práctica o una actividad fortalece una capacidad humana. | MetacognitivePractice, LearningActivity → HumanCapability | 0 |
| `COVERS_CONCEPT` *(2.1.0)* | learning | Una unidad de aprendizaje propone enseñar o ejercitar un concepto en un contexto definido; no afirma competencia adquirida, eficacia de un control ni causalidad. | LearningUnit → Concept, MentalModel, CognitiveBias, MetacognitivePractice, HumanCapability | 165 |

## 8. Relaciones ampliadas (14)

| Relación | Qué se amplió |
|---|---|
| `PART_OF` | Pertenencia estructural extendida con pares permitidos. |
| `SPECIALIZES` | Especialización entre pre-ensayos (vínculo ESPECIALIZA de las ampliaciones por pregunta). |
| `OWNS` | Propiedad extendida a productos-control, agentes, flotas, excepciones e indicadores. |
| `ACCOUNTABLE_FOR` | Rendición de cuentas sobre productos-control y flotas. |
| `MITIGATES` | Un producto-control reduce exposición a un escenario. |
| `IMPLEMENTS` | Un producto-control implementa objetivos de control. |
| `EVALUATES` | La evaluación alcanza a productos-control y agentes. |
| `SUPPORTED_BY` | Respaldo por evidencia extendido. |
| `ASSERTS` | Un pre-ensayo formula afirmaciones candidatas. |
| `EXPLAINS` | Un pre-ensayo también desarrolla un concepto. |
| `SUPERSEDES` | Reemplazo entre versiones o artefactos de referencia. |
| `DEVELOPS` | Un itinerario desarrolla competencias. |
| `CLASSIFIED_IN` | Clasificación con rol, versión de taxonomía, método y confianza. **2.1.0:** Admite como origen los cuatro tipos cognitivos del módulo O09, para ubicar los conceptos de la Biblioteca cognitiva en territorios y en el pilar del MCCS. |
| `MAPS_TO` | El mapeo exige fuerza, tipo de vínculo, versión del artefacto y método; nunca afirma conformidad. |

Además, `MEASURES`, que es nueva en la 2.0.0, se amplió en la 2.1.0: admite como destino una variable homeostática del catálogo (categoría del eje HV) para expresar el modelo de referencia; la regla SV-118 lo limita a ese eje. La medición de una organización concreta sigue usando instancias de HomeostaticVariable.

Propiedades obligatorias por relación: `CLASSIFIED_IN`: role, taxonomy_version, method, confidence; `MAPS_TO`: strength, link_type, artifact_version, method; `RELATES_TO`: editorial_predicate, predicate_family; `COVERS_CONCEPT`: confidence, method.

## 9. Reglas semánticas nuevas (16)

| Regla | Nivel | Nombre | Qué exige | Severidad |
|---|---|---|---|---|
| SV-007 | structural | Catálogo de la versión declarada | Todo código de categoría (territorio, dominio, función, subfunción, horizonte, fuerza, contexto, variable o lente) debe existir en la versión de taxonomía declarada. | error |
| SV-008 | structural | Par permitido | Cuando la relación define pares permitidos, el par (tipo origen, tipo destino) debe figurar en la lista. | error |
| SV-109 | semantic | Pre-ensayo no es ensayo | Un pre-ensayo no recibe identificador ESS ni se presenta como ensayo; la derivación se expresa con DERIVED_FROM y no traslada aprobación. | error |
| SV-110 | semantic | Separación de planos | Una instancia del plano B puede instanciar un concepto del plano A, pero ningún cambio originado en el plano B modifica un concepto; una brecha se tramita como candidato. | error |
| SV-111 | semantic | Capacidad, permiso, delegación y ejecución | No fusionar la capacidad técnica (Tool), el permiso, la delegación (DelegatedAuthority) y la ejecución (AutonomousAction). | error |
| SV-112 | semantic | Autonomía con compuerta | Toda relación OPERATES_AT con nivel L2 o superior exige una ApprovalGate o la justificación registrada de su ausencia. | error |
| SV-113 | semantic | Mapeo con fuerza y versión | MAPS_TO exige fuerza, tipo de vínculo, versión del artefacto y método; un mapeo nunca afirma conformidad ni equivalencia. | error |
| SV-114 | semantic | Clasificación con rol | CLASSIFIED_IN exige rol (primario, secundario, fuerza o lente), versión de taxonomía, método y confianza; a lo sumo un primario por eje. | error |
| SV-115 | semantic | Indicador no es resultado | Que un indicador mida un resultado no prueba el resultado; la afirmación de eficacia requiere evidencia. | error |
| SV-116 | semantic | Sesgo como posibilidad | DISTORTS expresa una posibilidad; solo se presenta como observada con evidencia. | error |
| SV-117 | semantic | Modelo de referencia de la homeostasis | Entre categorías de la taxonomía, REGULATES solo une un mecanismo homeostático (HOM) con una variable (HV), y PRESSURES solo une un catalizador (CAT) o un inhibidor (INH) con una variable (HV). | error |
| SV-118 *(2.1.0)* | semantic | Medición en el modelo de referencia | Cuando MEASURES apunta a una categoría de la taxonomía, esa categoría debe ser una variable homeostática (eje HV) y la arista debe declarar que expresa el modelo de referencia; medir una organización concreta requiere instancias de HomeostaticVariable. | error |
| SV-208 | governance | Estado de candidato | Los nodos y aristas generados por carga masiva o por un agente quedan como candidatos hasta la aprobación humana y no integran el grafo aprobado. | warning |
| SV-209 | governance | Vigencia de la referencia | Todo artefacto de referencia registra versión, fecha, estado y fecha de verificación; lo no verificado se marca. | warning |
| SV-210 | governance | Silencio declarado | La ausencia de fuente o de dato se registra como silencio; no se completa por inferencia. | warning |
| SV-211 | governance | Edición pública | Los atributos con fuente interna se marcan y se excluyen de la exportación pública. | warning |

## 10. Predicados editoriales

El GM-24 V7.1 usa 116 predicados distintos para vincular conceptos y tenía pendiente decidir cómo normalizarlos. La ontología no los convierte en 116 tipos de relación: los conserva como dato y los agrupa en familias.

| Familia | Definición | Predicados |
|---|---|---|
| FUNDAMENTO | Un concepto da base, origen o marco a otro. | 14 |
| ESPECIALIZACION | Un concepto es un caso, una extensión o una profundización de otro. | 6 |
| OPERACIONALIZACION | Un concepto convierte a otro en práctica, diseño o artefacto. | 24 |
| EVALUACION_Y_EVIDENCIA | Un concepto mide, prueba, verifica o aporta evidencia sobre otro. | 18 |
| CONDICION_Y_DEPENDENCIA | Un concepto requiere, limita, habilita o sostiene a otro. | 15 |
| GOBIERNO_Y_SUPERVISION | Un concepto gobierna, prioriza, asigna o supervisa a otro. | 15 |
| FLUJO_DE_INFORMACION | Un concepto alimenta, informa o comunica a otro. | 11 |
| ASOCIACION | Vínculo de afinidad o integración sin dirección causal declarada. | 12 |
| AFINIDAD_CON_DOMINIO | Afinidad declarada por una ampliación. Cuando el destino es un dominio del Atlas, queda registrada en el corpus y no se carga en el grafo; cuando el destino es otro pre-ensayo, se carga como vínculo de la familia ASOCIACION y conserva el predicado original. | 1 |

Regla de carga: toda la familia ESPECIALIZACION usa la relación `SPECIALIZES` y las demás, `RELATES_TO`. La familia AFINIDAD_CON_DOMINIO reúne afinidades declaradas por las ampliaciones: cuando el destino es un dominio, la afinidad queda en el corpus y no se carga; cuando es otro pre-ensayo, se carga en la familia ASOCIACION. El detalle está en `data/predicados_editoriales.json`.

## 11. Preguntas de competencia

Una ontología sirve si el grafo puede responder las preguntas para las que fue diseñada. Son 22: las 10 originales, 10 de la 2.0.0 y 2 de la 2.1.0. Desde la versión 1.2 el estado no es una etiqueta puesta a mano: se deriva de si la pregunta puede expresarse con la ontología, de la cobertura de la consulta sobre su universo y del límite declarado. Resultado: 7 respondibles, 9 en parte y 6 todavía no. P02 y P05 no pueden expresarse con la ontología 2.1.0 aunque se carguen instancias de una organización.

| N.º | Pregunta | Estado | Motivo del estado | Cobertura | Nota |
|---|---|---|---|---|---|
| P01 | ¿Qué activos sostienen una capacidad empresarial crítica? | Todavía no | sin instancias en el grafo | — | No hay instancias de Asset ni de BusinessCapability: el Atlas es conocimiento de referencia y no contiene los activos de una organización. La ontología permite expresar el vínculo con PART_OF. |
| P02 | ¿Qué escenarios de riesgo pueden afectarla? | Todavía no | no puede expresarse con la ontología 2.1.0 | — | No puede expresarse con la ontología 2.1.0, aunque se carguen instancias: ninguna relación une un escenario de riesgo con la capacidad, el activo o el servicio que afecta. Queda pedido en la solicitud OCR-CAND-03. |
| P03 | ¿Qué controles contribuyen a mitigar esos escenarios? | Todavía no | sin instancias en el grafo | — | Hay controles de gobierno de agentes cargados, pero ningún escenario de riesgo contra el cual declarar que mitigan. |
| P04 | ¿Qué evidencia respalda la efectividad de los controles? | Todavía no | sin instancias en el grafo | — | No hay instancias de Evidence ni de AssessmentResult. Las fichas de producto-control dicen qué evidencia se espera, no la evidencia. |
| P05 | ¿Qué autoridad puede aceptar el riesgo residual? | Todavía no | no puede expresarse con la ontología 2.1.0 | — | No puede expresarse con la ontología 2.1.0, aunque se carguen instancias: una autoridad solo se une a una decisión, y la decisión no se vincula con el escenario de riesgo ni con la tolerancia. Queda pedido en la solicitud OCR-CAND-03. |
| P06 | ¿Qué agentes poseen autoridad sobre determinados activos? | Todavía no | sin instancias en el grafo | — | No hay instancias de Asset ni de DelegatedAuthority. El grafo sí dice qué flota de agentes sirve a qué producto-control (consulta de abajo), pero eso no es autoridad sobre un activo; el rol dueño de cada flota lo fija el guion de carga, no la fuente. |
| P07 | ¿Qué herramientas y acciones están disponibles para esos agentes? | En parte | límite declarado | 85 de 85 | Herramientas declaradas en los anexos de los agentes del plano B. Límite: El grafo no tiene instancias de AutonomousAction: la consulta devuelve las herramientas de cada agente, no sus acciones. |
| P08 | ¿Qué fuerzas condicionan la evolución de una capacidad? | En parte | límite declarado | 27 de 28 | Ejemplo con el dominio D20. Los mecanismos homeostáticos no son fuerzas y quedan fuera de esta consulta (están en P15). La cobertura no cuenta la capa de ampliación APX: D19 solo tiene pre-ensayos de esa capa. Límite: A nivel de capacidad la pregunta no puede expresarse: CapabilityState no es origen de ninguna relación. La consulta responde a nivel de dominio, con las fuerzas (catalizadores e inhibidores) que tratan sus pre-ensayos. |
| P09 | ¿Qué competencias necesita desarrollar un responsable? | En parte | cobertura menor que 90 % | 1 de 85 | Solo el rol PO-GAC tiene competencias declaradas; los demás roles del grafo son personas operativas citadas por los modelos operativos. |
| P10 | ¿Qué unidades GM-24 desarrollan y evalúan esas competencias? | En parte | límite declarado | 41 de 41 | Competencia → conceptos que la sostienen → unidades del GM-24 a las que pertenecen esos conceptos. Límite: La unidad se infiere de los conceptos que sostienen la competencia: el grafo no tiene relaciones de desarrollo ni de evaluación (0 aristas DEVELOPS y ASSESSES). Que un concepto pertenezca a una unidad no prueba que la unidad desarrolle la competencia, y la parte «evalúan» no tiene respuesta. |
| P11 | ¿Qué pre-ensayos cubren una coordenada (territorio × dominio × subfunción) y con qué confianza? | Respondible | cobertura de al menos 90 % | 755 de 755 | Ejemplo con la coordenada T08 × D28 × GV08. La categorización es candidata: no tiene revisión humana. |
| P12 | ¿Qué elementos de qué artefactos de referencia respaldan un concepto y con qué fuerza? | Respondible | cobertura de al menos 90 % | 379 de 379 | Ejemplo con el concepto M3.1-K03. La fuerza y el vínculo son los del mapeo del GM-24 V7.1, que en su mayor parte se generó por herencia de la unidad y regla por palabra clave: «fuerte» y «cubre» indican afinidad, no conformidad ni cobertura comprobada. Por eso la consulta muestra el método junto a la fuerza. |
| P13 | ¿Qué agentes ejecutan tareas de un producto-control, con qué nivel de autonomía y bajo qué puntos de control? | Respondible | cobertura de al menos 90 % | 156 de 156 | Ejemplo con el producto-control de identidades (plano B). El punto de control es el que declara el anexo de cada agente. |
| P14 | ¿Qué conceptos del corpus instancia cada producto-control? | Respondible | cobertura de al menos 90 % | 7 de 7 | Una fila por concepto. La instancia no prueba el concepto. |
| P15 | ¿Qué fuerzas y qué mecanismos homeostáticos tratan los pre-ensayos de un dominio? | Respondible | cobertura de al menos 90 % | 27 de 27 | El universo y la cobertura son del corpus base: la capa de ampliación APX no cuenta, y D19 solo tiene pre-ensayos de esa capa. Ejemplo con el dominio D28. El eje distingue catalizadores (HC), inhibidores (HI) y mecanismos homeostáticos (HR). |
| P16 | ¿Qué indicadores miden una variable homeostática y a qué decisión informan? | En parte | límite declarado | 6 de 6 | La columna «lecturas» dice si el vínculo lo sostienen dos lecturas independientes o una sola. Límite: Son indicadores candidatos de un modelo de referencia: ninguna variable tiene unidad, umbral ni responsable del límite. No hay decisiones instanciadas, de modo que «a qué decisión informa» se responde solo con el órgano de gobierno que recibe el indicador. |
| P17 | ¿Qué prácticas metacognitivas contrarrestan los sesgos que pueden distorsionar una decisión? | En parte | límite declarado | 51 de 524 | Una fila por vínculo. Solo se cargaron los que la segunda lectura independiente juzgó sostenibles. Límite: No hay decisiones instanciadas sobre las que declarar qué sesgo las distorsiona. Los vínculos expresan lo que la Biblioteca propone, no eficacia probada, y cubren una parte menor de los sesgos. |
| P18 | ¿Qué preguntas tienen un pre-ensayo directo y todavía no tienen un ensayo aprobado? | Respondible | cobertura de al menos 90 % | 595 de 595 | Antiunión: preguntas a las que responde un pre-ensayo y a las que no responde ningún ensayo aprobado. El ensayo se representa como nodo Essay; hoy no hay ninguno, de modo que la lista son todas las que tienen pre-ensayo directo. La cobertura es total por construcción: el estado de esta pregunta depende solo de que la consulta pueda expresarse. |
| P19 | ¿Qué competencias requiere un rol y qué conceptos y unidades las sostienen? | En parte | cobertura menor que 90 % | 1 de 85 | Rol → competencias → conceptos → unidades, para el rol PO-GAC, el único con competencias declaradas. Una fila por competencia y concepto. |
| P20 | ¿Qué celdas del Atlas no tienen conocimiento (silencios)? | En parte | límite declarado | 224 de 224 | Celdas territorio × dominio sin ningún pre-ensayo del corpus base de 739 con ambas coordenadas primarias. La cobertura es total por construcción; el estado lo decide el límite declarado. Límite: la consulta no distingue las combinaciones de territorio y dominio que no pueden darse de las que no tienen contenido |
| P21 | ¿Qué conceptos de la Biblioteca cognitiva propone cubrir cada unidad del GM-24 y con qué confianza editorial? | Respondible | cobertura de al menos 90 % | 24 de 24 | Una fila por concepto. Solo los vínculos de selección editorial o de ancla expresa de la base; los de coincidencia temática no se cargaron. Es cobertura propuesta, no aprendizaje comprobado. |
| P22 | ¿Qué indicadores miden cada subfunción del Atlas y qué subfunciones no tienen indicador? | En parte | límite declarado | 224 de 244 | Una fila por indicador, con el método con que recibió la subfunción. Las subfunciones sin indicador están en el resumen. Límite: La consulta responde «qué indicadores están clasificados en cada subfunción», no «cuáles la miden»: la regla SV-118 no admite MEASURES hacia una subfunción. Los 20 indicadores del sub-plan PO-GAC no tienen coordenada en el Atlas. |

## 12. Compatibilidad y migración desde la 1.0.0

- Ningún tipo de entidad ni relación de la 1.0.0 se elimina o se renombra.
- Los datos existentes que usen `CLASSIFIED_IN` o `MAPS_TO` sin las propiedades obligatorias deben completarse antes de cargarse.
- Las relaciones ampliadas aceptan más tipos de origen o destino; lo que era válido sigue siéndolo.
- La ontología 2.1.0 declara la Taxonomía 6.0 y el GM-24 V7.1 como versiones asociadas.
- De la 2.0.0 a la 2.1.0 todo es aditivo: lo que validaba con la 2.0.0 valida con la 2.1.0.

## 13. Archivos

- `data/ontology.json`: metadatos, principios, módulos y preguntas de competencia.
- `data/entity_dictionary.json`: los 84 tipos de entidad.
- `data/relationship_dictionary.json`: las 93 relaciones, con tipos de origen y destino, pares permitidos y propiedades obligatorias.
- `data/semantic_rules.json`: las 37 reglas.
- `data/predicados_editoriales.json`: predicados y familias.
- `data/solicitud_cambio_ontologia_OCR-CAND-03.json`: lo que la revisión crítica propone para la próxima revisión.

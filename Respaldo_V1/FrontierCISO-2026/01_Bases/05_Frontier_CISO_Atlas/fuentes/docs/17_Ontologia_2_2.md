# Ontología 2.2 del Frontier CISO Atlas (propuesta)

**Frontier CISO Atlas 1.4** · Taxonomía 6.1 (reglas de asignación, revisión 3) · Ontología 2.2.0 (propuesta) · GM-24 V7.1 · 16 de noviembre de 2026 · Estado: respuestas del autor registradas de forma literal; lo que decidió el curador en esta versión espera su confirmación (D-16); corpus releído por lectores automáticos con una vara de tres lecturas, que el curador endureció después de leer; contenido candidato, sin validación humana

Este documento describe qué cambia de la propuesta de ontología 2.1.0 a la 2.2.0. La descripción completa de la 2.1.0 está en `docs/05_Ontologia_2_1.md`, que se conserva como registro de la versión 1.3. Los diccionarios vigentes son `data/ontology.json`, `data/entity_dictionary.json`, `data/relationship_dictionary.json` y `data/semantic_rules.json`.

## 1. Qué estado tiene

- **La solicitud de cambio está aprobada.** La revisión crítica de la versión 1.2 dejó 16 propuestas en la solicitud OCR-CAND-03. El autor la aprobó el 16 de noviembre de 2026 («Si, confirmo, procede»). Esta versión aplica las 16 propuestas, y no todas quedaron completas: la sección 4.1 dice cuáles quedaron aplicadas en parte y qué falta.
- **La ontología sigue siendo una propuesta.** Su estado es «proposed baseline (extensión gobernada; requiere aprobación humana)». El autor aprobó los cambios pedidos; la línea base 2.2.0 completa no tiene una aprobación propia y el grafo sigue siendo candidato.
- **Lo que la solicitud no decía lo decidió el curador** y espera la confirmación del autor (D-16.10): cinco elecciones que la solicitud dejaba abiertas, dos agregados y cuatro decisiones de implementación. Están en la sección 4.
- **El archivo de la solicitud se conserva como se presentó.** `data/solicitud_cambio_ontologia_OCR-CAND-03.json` dice «no aplicada» porque ese era su estado en la versión 1.3. Cómo se aplicó cada propuesta está en `data/aplicacion_de_la_solicitud_OCR-CAND-03.csv`.

## 2. En números

| Elemento | Ontología 1.0.0 del AI CISO Atlas | Propuesta 2.1.0 | Propuesta 2.2.0 |
|---|---|---|---|
| Módulos | 8 | 10 | 10 |
| Tipos de entidad | 57 | 84 | 86 |
| Relaciones | 58 | 93 | 98 |
| Reglas semánticas | 21 | 37 | 42 |
| Preguntas de competencia | 10 | 22 | 22 |

El grafo candidato usa 34 de los 86 tipos y 33 de las 98 relaciones. De los demás, una parte espera instancias de una organización, que el Atlas no tiene. Otra parte es contenido del propio Atlas, del currículo o de la biblioteca que todavía no se cargó: por ejemplo `Essay` y `Claim` (el Atlas tiene pre-ensayos y ningún ensayo), o las relaciones `DEVELOPS` y `ASSESSES`.

## 3. Qué cambia

### 3.1 Tipos nuevos

| Tipo | Módulo | Definición |
|---|---|---|
| `LogicalFallacy` | O09 | Defecto de un argumento: una inferencia que parece válida y no lo es. Se distingue del sesgo cognitivo, que es una desviación sistemática del juicio. |
| `CognitiveState` | O09 | Estado o condición de una persona o de un equipo que sostiene o degrada la calidad de la decisión: fatiga, estrés, carga cognitiva, flujo. |

### 3.2 Relaciones nuevas

| Relación | Familia | Definición | Origen | Destino |
|---|---|---|---|---|
| `SAME_CONCEPT_AS` | epistemic | Dos nodos nombran el mismo concepto y no se fusionan. Es una declaración candidata: exige evidencia, método y confianza, y vale en los dos sentidos. | Concept, Precursor, MentalModel, CognitiveBias, LogicalFallacy, MetacognitivePractice … | Concept, Precursor, MentalModel, CognitiveBias, LogicalFallacy, MetacognitivePractice … |
| `DELEGATES_TO` | governance | Un rol, un órgano o una autoridad delega en un agente o en una flota una tarea o una decisión, con condiciones: nivel de autonomía, límites y punto de control. Es el objeto de la variable HV02. | Role, GovernanceBody, Authority | AIAgent, AgentFleet |
| `MAY_AFFECT` | risk | Un escenario de riesgo puede afectar una capacidad, un servicio, un activo o un sistema. Es una posibilidad salvo evidencia. | RiskScenario | BusinessCapability, BusinessService, Asset, System |
| `ACCEPTS_RISK` | governance | Una autoridad acepta el riesgo residual de un escenario dentro de una tolerancia y con vencimiento. | Authority | RiskScenario |
| `STATE_OF` | evolution | Un estado es la condición de una capacidad, de un control o de un producto-control en un contexto. | CapabilityState | BusinessCapability, ResilienceCapability, SecurityControl, ControlProduct |

### 3.3 Reglas nuevas

| Regla | Nombre | Qué comprueba | Severidad |
|---|---|---|---|
| SV-009 | Valor de catálogo | Cuando una propiedad tiene catálogo de valores en la ontología (confianza, rol, fuerza, tipo de vínculo, eje, nivel, papel, término, sentido, base, clase y plano), el valor debe figurar en él. | error |
| SV-119 | Neutralidad del plano A | Un nodo del plano A no nombra productos ni proveedores. El que los nombra queda marcado y no se promueve a ensayo hasta que se reescriba sin marca. | warning |
| SV-120 | Equivalencia declarada | SAME_CONCEPT_AS no fusiona nodos ni traslada clasificaciones, definiciones ni aprobación de uno a otro; exige evidencia, método y confianza. | error |
| SV-121 | Una representación para el eje H | Las fuerzas, los mecanismos, las variables y los factores de contexto del catálogo son categorías de la taxonomía. Los tipos Catalyst, Inhibitor, HomeostaticMechanism, HomeostaticVariable y ContextProfile solo se usan para instancias observadas en una organización. | error |
| SV-212 | Propiedades que la definición enuncia | Cada tipo declara las propiedades que su definición enuncia. La validación informa, por tipo, cuántos nodos no las traen. | warning |

### 3.4 Todos los cambios, por propuesta

| N.º | Propuesta | Tipo de cambio | Elemento | Cómo se aplicó |
|---|---|---|---|---|
| 1 | Relación de equivalencia declarada | relación nueva | SAME_CONCEPT_AS | Relación simétrica para declarar que dos nodos nombran el mismo concepto sin fusionarlos. |
| 1 | Relación de equivalencia declarada | regla nueva | SV-120 | Equivalencia declarada: SAME_CONCEPT_AS no fusiona nodos ni traslada clasificaciones, definiciones ni aprobación de uno a otro; exige evidencia, método y confianza. |
| 2 | Tipos cognitivos en los vínculos entre conceptos | relación ampliada o precisada | RELATES_TO | Admite los tipos del módulo de cognición como origen y como destino. «Relacionado» entre un elemento de la biblioteca y un pre-ensayo se carga con esta relación, familia ASOCIACION. Los vínculos editoriales viven en los nodos que los declaran: no se copian de los pre-ensayos a los conceptos. |
| 2 | Tipos cognitivos en los vínculos entre conceptos | relación ampliada o precisada | SPECIALIZES | Admite la especialización entre elementos del mismo tipo cognitivo y de un elemento cognitivo respecto de un concepto. |
| 3 | Tipo para las falacias | tipo nuevo | LogicalFallacy | Las falacias dejan de cargarse como sesgos. |
| 3 | Tipo para las falacias | relación ampliada o precisada | DISTORTS | Una falacia también puede distorsionar una decisión o un resultado de evaluación. |
| 3 | Tipo para las falacias | definición reescrita | CognitiveBias | Deja de incluir a las falacias, que tienen tipo propio. |
| 4 | Tipo para estados y condiciones | tipo nuevo | CognitiveState | Estados y condiciones que sostienen o degradan la decisión; antes quedaban como Concept. |
| 5 | COUNTERS como posibilidad | relación ampliada o precisada | COUNTERS | La definición pasa a expresar una posibilidad, se le asocia la regla de posibilidad frente a observación (SV-116) y exige la propiedad «basis»: propuesto por la fuente u observado con evidencia. |
| 5 | COUNTERS como posibilidad | regla precisada | SV-116 | Alcanza también a COUNTERS. |
| 6 | Rol propio para los mecanismos | regla precisada | SV-114 | Agrega los roles «mecanismo» y «marcador»: los mecanismos homeostáticos ya no se cargan con el rol «fuerza». |
| 7 | Catálogos de valores | catálogos de valores | confianza, rol, fuerza, tipo de vínculo, eje y otras siete propiedades | Los valores admitidos se declaran en la ontología y la regla SV-009 los comprueba. |
| 7 | Catálogos de valores | regla nueva | SV-009 | Valor de catálogo: Cuando una propiedad tiene catálogo de valores en la ontología (confianza, rol, fuerza, tipo de vínculo, eje, nivel, papel, término, sentido, base, clase y plano), el valor debe figurar en él. |
| 8 | Propiedades obligatorias por tipo y por relación | relación ampliada o precisada | CLASSIFIED_IN | Admite los dos tipos cognitivos nuevos. La propiedad «axis» pasa a ser obligatoria: de ella depende la regla de un primario por eje. La definición nombra ahora los ejes, las fuerzas, los mecanismos y las lentes. |
| 8 | Propiedades obligatorias por tipo y por relación | relación ampliada o precisada | COVERS_CONCEPT | Admite los dos tipos cognitivos nuevos y pasa a exigir contexto, como dice su definición: la unidad y la edición del currículo. |
| 8 | Propiedades obligatorias por tipo y por relación | relación ampliada o precisada | SEQUENCES | La etapa pasa a ser obligatoria. |
| 8 | Propiedades obligatorias por tipo y por relación | relación ampliada o precisada | REGULATES | Exige el nivel (modelo de referencia u observado) y el papel del mecanismo: referencia, sensor, decisor o efector (encargo RP-15.4). |
| 8 | Propiedades obligatorias por tipo y por relación | relación ampliada o precisada | PRESSURES | Exige el nivel (modelo de referencia u observado), el término de la variable sobre el que actúa la fuerza (demanda o capacidad) y el sentido (aumenta o reduce) (encargo RP-15.3). |
| 8 | Propiedades obligatorias por tipo y por relación | propiedades por tipo | 11 tipos | Cada tipo declara las propiedades que su definición enuncia. La regla SV-212 informa, por tipo, cuántos nodos del grafo candidato no las traen. |
| 8 | Propiedades obligatorias por tipo y por relación | regla nueva | SV-212 | Propiedades que la definición enuncia: Cada tipo declara las propiedades que su definición enuncia. La validación informa, por tipo, cuántos nodos no las traen. |
| 9 | Punto de control con clase y con su par de agente y tarea | relación ampliada o precisada | GATED_BY | Cuando el origen es una tarea, la arista lleva en la propiedad «agente» el agente que la ejecuta: el punto de control queda unido al par de agente y tarea. |
| 9 | Punto de control con clase y con su par de agente y tarea | propiedad obligatoria | ApprovalGate | La clase del punto de control pasa a ser obligatoria. |
| 10 | Relación de delegación | relación nueva | DELEGATES_TO | Quién delega la autoridad que ejerce un agente. |
| 11 | Escenario de riesgo y lo que afecta; autoridad y aceptación del riesgo; estado y su capacidad | relación ampliada o precisada | BOUNDS | Una tolerancia también limita un escenario de riesgo, además de una consecuencia. |
| 11 | Escenario de riesgo y lo que afecta; autoridad y aceptación del riesgo; estado y su capacidad | relación nueva | MAY_AFFECT | Un escenario de riesgo puede afectar una capacidad, un servicio, un activo o un sistema. Es una posibilidad salvo evidencia. |
| 11 | Escenario de riesgo y lo que afecta; autoridad y aceptación del riesgo; estado y su capacidad | relación nueva | ACCEPTS_RISK | Una autoridad acepta el riesgo residual de un escenario dentro de una tolerancia y con vencimiento. |
| 11 | Escenario de riesgo y lo que afecta; autoridad y aceptación del riesgo; estado y su capacidad | relación nueva | STATE_OF | Un estado es la condición de una capacidad, de un control o de un producto-control en un contexto. |
| 12 | Pares duplicados y definiciones | pares permitidos | ENABLES | Se declaran los pares de tipos admitidos: BusinessCapability → BusinessObjective; Catalyst → Transition. |
| 12 | Pares duplicados y definiciones | pares permitidos | DEPENDS_ON | Se declaran los pares de tipos admitidos: System → Asset; System → System; System → BusinessCapability; Application → System; BusinessCapability → BusinessCapability; BusinessCapability → System. |
| 12 | Pares duplicados y definiciones | pares permitidos | CONTRIBUTES_TO | Se declaran los pares de tipos admitidos: Vulnerability → RiskScenario; SecurityControl → SecurityOutcome. |
| 12 | Pares duplicados y definiciones | pares permitidos | EVALUATES | Se declaran los pares de tipos admitidos: AssessmentResult → SecurityControl; AssessmentResult → ControlProduct; AssessmentResult → AIAgent. |
| 12 | Pares duplicados y definiciones | pares permitidos | EXPOSED_TO | Se declaran los pares de tipos admitidos: AIAgent → FrameworkElement; AIAgent → RiskScenario; Tool → FrameworkElement; Tool → RiskScenario. |
| 12 | Pares duplicados y definiciones | definiciones reescritas | 13 relaciones | Nombran todos los tipos que admiten y dicen qué afirma la relación: ACCOUNTABLE_FOR, ASSERTS, DEVELOPS, EVALUATES, EXPLAINS, IMPLEMENTS, MAPS_TO, MEASURES, MITIGATES, OWNS, PART_OF, SUPERSEDES, SUPPORTED_BY. |
| 12 | Pares duplicados y definiciones | definiciones reescritas | Concept, Essay y TaxonomyCategory | Se definen por lo que son y no por su nombre o su identificador. |
| 12 | Pares duplicados y definiciones | definición reescrita | CONTRIBUTES_TO | Dice qué afirma la relación y remite a MITIGATES para el control que reduce un escenario. |
| 12 | Pares duplicados y definiciones | notas de frontera | 17 tipos | Cada tipo de un grupo que se solapa dice qué lo distingue de sus vecinos. |
| 12 | Pares duplicados y definiciones | pares que parecen inversos | SUPPORTS y SUPPORTED_BY; IMPLEMENTS y REALIZES; CONTRIBUTES_TO y ENABLES | Se documenta que no son inversos. No se renombran para conservar la compatibilidad con la ontología 1.0.0. |
| 12 | Pares duplicados y definiciones | criterio por par | 20 pares de tipos que la ontología 2.1.0 admitía en más de una relación | Cada par tiene un criterio escrito; dos se resolvieron quitando el par de una de las relaciones (EVALUATES y CONTRIBUTES_TO). Con el diccionario 2.2.0 los pares admitidos en más de una relación son 80, y 61 no tienen criterio escrito: los crean los cambios de esta revisión. |
| 13 | Categorías del eje H como catálogo | representación única | Catalyst, Inhibitor, HomeostaticMechanism, HomeostaticVariable y ContextProfile | Las categorías del eje H son categorías de la taxonomía; los tipos quedan para instancias observadas (regla SV-121). |
| 13 | Categorías del eje H como catálogo | regla nueva | SV-121 | Una representación para el eje H: Las fuerzas, los mecanismos, las variables y los factores de contexto del catálogo son categorías de la taxonomía. Los tipos Catalyst, Inhibitor, HomeostaticMechanism, HomeostaticVariable y ContextProfile solo se usan para instancias observadas en una organización. |
| 14 | Reformular la pregunta P22 y la separación de planos | propiedad obligatoria | plano | Los 28 tipos que pertenecen a un plano llevan la propiedad «plano» (A o B); con ella la regla SV-110 se puede comprobar. |
| 14 | Reformular la pregunta P22 y la separación de planos | regla precisada | SV-110 | Se apoya en la propiedad «plano» y dice qué comprueba. |
| 14 | Reformular la pregunta P22 y la separación de planos | pregunta de competencia reformulada | P22 | Decía «qué indicadores miden cada subfunción»; la regla SV-118 no admite MEASURES hacia una subfunción. Ahora pregunta qué indicadores están clasificados en cada una. |
| 15 | Ancla de HumanCapability | ancla corregida | HumanCapability | El ancla decía «pilar OS a escala individual» y la regla de pilar, que escribió el curador, deja en MM a la mayoría de los nodos de ese tipo. El ancla sigue ahora a la regla. El autor no confirmó la regla: confirmó que no revisar la biblioteca deja esas categorías en MM como consecuencia (D-15.3), y si la regla queda como está lo decide en D-17.1. |
| 15 | Ancla de HumanCapability | ancla precisada | MentalModel, CognitiveBias y MetacognitivePractice | El ancla nombra la biblioteca metacognitiva del autor, que es lo que él declaró que es el MCCS. |
| 16 | Regla de neutralidad del plano A | regla nueva | SV-119 | Neutralidad del plano A: Un nodo del plano A no nombra productos ni proveedores. El que los nombra queda marcado y no se promueve a ensayo hasta que se reescriba sin marca. |
| 16 | Regla de neutralidad del plano A | origen de la regla | SV-119 | La comprobación PAQ-01, que el paquete hacía por fuera de las reglas, pasa a ser la regla SV-119. |

### 3.5 Catálogos de valores

Desde la 2.2.0 la ontología declara los valores que admite cada propiedad con catálogo, y la regla SV-009 los comprueba:

| Propiedad | Valores admitidos |
|---|---|
| confidence | alta, media, baja, alta_editorial y sin evaluar |
| role | primario, secundario, fuerza, mecanismo, marcador y lente |
| strength | fuerte, parcial, afinidad, informativo, ancla primaria y ancla secundaria |
| link_type | cubre, referencia y ancla de lente |
| axis | X, Y, Z, Zs, H, HCV, HC, HI, HR, HX, HV, L-MCCS, L-PLANO y L-IA |
| nivel | modelo de referencia y observado |
| papel (REGULATES) | referencia, sensor, decisor y efector |
| termino | demanda y capacidad |
| sentido | aumenta y reduce |
| basis | propuesto por la fuente y observado con evidencia |
| clase (ApprovalGate) | aprobación previa, auditoría posterior, prohibición de delegar y sin clase declarada |
| plano | A y B |

## 4. Lo que decidió el curador al aplicar la solicitud

El autor aprobó la solicitud de cambio OCR-CAND-03. La propuesta 2.2.0 aplica sus dieciséis propuestas, y ocho quedaron aplicadas en parte (documento 17, sección 4.1): 86 tipos, 98 relaciones y 42 reglas. La solicitud dejaba una alternativa abierta en cinco propuestas (las número 2, 3, 12, 13 y 15), que eligió el curador, y en dos (la 6 y la 7) el curador agregó algo que la solicitud no pedía. Además hay decisiones de implementación que son del curador: la regla que reconoce un estado por la primera palabra de su definición (14 elementos de la biblioteca), la carga de las 112 equivalencias entre la biblioteca y el corpus como candidatas de una lectura, y el vínculo de cada tarea de autonomía L2 o superior con el punto de control de su agente.

La proposición D-16.10 las pide confirmar una por una:

> La ontología 2.2.0 tal como se implementó. Aprobaste la solicitud OCR-CAND-03; al aplicarla tomé decisiones que no estaban en ella. Cinco propuestas dejaban una alternativa abierta y la elegí yo (las número 2, 3, 12, 13 y 15); en dos agregué algo que la solicitud no pedía (la 6 y la 7); y hay cuatro decisiones de implementación: la regla que reconoce un estado por la primera palabra de su definición (14 elementos), la carga de 112 equivalencias entre la biblioteca y el corpus como candidatas de una sola lectura, el vínculo de 134 pares de tarea y punto de control, y la clase del punto de control, que sale de una regla de palabras.

Las tres primeras decisiones de implementación, con su alcance y su límite:

| Decisión | Qué alcance tiene | Qué límite tiene |
|---|---|---|
| Reconocer un estado por la primera palabra de su definición | 14 elementos de la biblioteca pasan al tipo `CognitiveState` | Es una regla sobre el texto, no una lectura de cada elemento. El autor pidió no revisar la biblioteca: los tipos se asignan por regla |
| Cargar las equivalencias entre la biblioteca y el corpus | 21 vínculos `SAME_CONCEPT_AS` y 91 vínculos `RELATES_TO` | Son candidatas de una sola lectura, hecha en la revisión de la versión 1.2. La regla SV-120 impide que una equivalencia traslade clasificaciones o aprobación de un nodo a otro |
| Unir cada tarea de autonomía L2 o superior con el punto de control de su agente | 134 pares de tarea y punto de control, con el agente como propiedad del vínculo | 7 tareas de ese nivel no tienen agente ejecutor en el catálogo y quedan sin vínculo |

Cómo se revierte: Volver a la propuesta 2.1.0: los cambios están en un bloque aparte de scripts/build_ontology.py.

### 4.1 Propuestas aplicadas en parte

La revisión de la versión candidata encontró que estas propuestas no quedaron completas. Las cuentas que llevan la marca «según la revisión» son del revisor y no se volvieron a calcular.

| N.º | Qué pedía | Qué se hizo | Qué falta |
|---|---|---|---|
| 1 | Una relación de equivalencia declarada | Se creó `SAME_CONCEPT_AS` y se cargaron las equivalencias | Las equivalencias «mismo concepto» se cargaron sobre el nodo del pre-ensayo, que es un texto, y no sobre el nodo del concepto que ese texto desarrolla |
| 4 | Un tipo para los estados que degradan la decisión | Se creó `CognitiveState`, y su definición incluye también los estados que la sostienen | La regla mira la primera palabra de la definición: «Estrés», que la definición del tipo da como ejemplo, queda como `Concept` |
| 7 | Catálogos de valores, con «sin evaluar» como estado distinto de un nivel de confianza | Los catálogos están declarados y la regla SV-009 los comprueba | Ninguna relación usa «sin evaluar». Varias cargas llevan una confianza fijada por el guion y no declarada por una lectura: 3.041 de 13.017 clasificaciones, según la revisión |
| 8 | Declarar obligatorias las propiedades de las que dependen las reglas | Se declararon en parte | SV-118 depende de una propiedad «nivel» que `MEASURES` no declara obligatoria, y SV-112 de dos propiedades de `OPERATES_AT` que tampoco lo están |
| 9 | Clase obligatoria del punto de control | Todos los puntos de control llevan clase. La asigna una regla de palabras sobre el texto del anexo de cada agente | 16 de 85 quedan «sin clase declarada», un valor de relleno que la definición del tipo no nombra. La regla SV-112 los cuenta igual como punto de control |
| 12 | Un criterio para cada par de tipos admitido en más de una relación | Se escribió para los 20 pares de la ontología 2.1.0 | Con el diccionario 2.2.0 son 80 pares, y 61 no tienen criterio escrito |
| 13 | Una sola representación para variables, fuerzas, mecanismos y contextos | Se conservaron las dos, separadas por nivel: categorías para el modelo de referencia y tipos para instancias de una organización | Ninguna relación permite decir de qué categoría es instancia un nodo |
| 16 | Que ningún nodo del plano A nombre productos ni proveedores (SV-119) | La regla repite la marca que ya traen los pre-ensayos | No mira los demás nodos del plano A. Según la revisión, 11 nombran un producto y no llevan marca |

## 5. Qué comprueba la validación y qué no

De las 42 reglas, la validación del grafo comprueba 25. Las demás necesitan instancias que el Atlas no tiene, o un juicio que una prueba automática no puede hacer. Resultado sobre el grafo candidato: 0 errores y 80 advertencias (77 de SV-119 y 3 de SV-212).

La validación es estructural: dice que los nodos y las relaciones respetan los diccionarios y las reglas. No dice si el contenido es correcto.

Entre las reglas «comprobadas» hay cuatro que hay que leer con cuidado. SV-119 se comprueba en parte: solo en los pre-ensayos. SV-120 se comprueba en parte: la prueba mira que cada equivalencia traiga evidencia, método y confianza, y no que no se trasladen clasificaciones de un nodo a otro. SV-110 y SV-208 se cumplen por construcción, igual que SV-006: el guion asigna el valor y después comprueba que esté, de modo que no pueden fallar.

Las advertencias de SV-212 son una por tipo. Detrás hay más nodos, y la regla solo mira el nombre de la propiedad, de modo que mezcla faltas reales con faltas que no lo son:

| Tipo | Propiedad que falta | Nodos |
|---|---|---|
| ControlProduct | alcance | 7 |
| ControlProduct | modelo_operativo | 7 |
| ControlProduct | dueño | 7 |
| KnowledgeSource | dueño | 51 |
| KnowledgeSource | etiqueta | 51 |
| KnowledgeSource | procedencia | 51 |
| SecurityIndicator | definicion | 244 |
| SecurityIndicator | fuente | 20 |
| SecurityIndicator | umbrales | 244 |
| SecurityIndicator | dueño | 244 |

La falta real es que ningún indicador tiene umbrales ni dueño. Los indicadores sí tienen definición, en otro campo, y los productos-control tienen dueño y modelo operativo por una relación.

| Regla | Qué se comprueba |
|---|---|
| SV-001 | en parte: un identificador repetido con otro tipo es error; las repeticiones del mismo tipo se cuentan y se conserva la primera declaración |
| SV-002 | tipo de nodo y de relación contra los diccionarios |
| SV-003 | nombre y descripción no vacíos en todos los nodos; identificador, tipo, versión y estado los fija la carga |
| SV-004 | origen y destino de cada arista existen |
| SV-006 | por construcción: cada conjunto de cambios declara esquema, ontología y taxonomía |
| SV-007 | cada clasificación apunta a una categoría del eje que declara, y el eje está en el catálogo de ejes |
| SV-008 | par de tipos permitido cuando la relación lo define |
| SV-101 | tipo de origen permitido |
| SV-102 | tipo de destino permitido |
| SV-105 | en parte: el campo de evidencia no está vacío; no se comprueba que sea evidencia y no solo procedencia |
| SV-106 | contexto presente en las relaciones que lo exigen |
| SV-109 | en parte: ningún nodo que no sea ensayo lleva identificador de ensayo; no hay ensayos cargados |
| SV-112 | cada agente en L2 o superior tiene punto de control; cada tarea en L2 o superior tiene un agente ejecutor con punto de control o no tiene agente |
| SV-113 | fuerza, tipo de vínculo, versión del artefacto y método presentes en cada MAPS_TO |
| SV-114 | rol, versión de taxonomía, método y confianza presentes y dentro de catálogo; a lo sumo un primario por eje |
| SV-117 | ejes permitidos en REGULATES y PRESSURES entre categorías |
| SV-118 | MEASURES hacia una categoría solo sobre el eje HV y como modelo de referencia |
| SV-208 | todos los nodos y aristas quedan en estado candidato |
| SV-209 | cada artefacto de referencia tiene versión, fecha, estado y fecha de verificación |
| SV-009 | cada propiedad con catálogo de valores (confianza, rol, fuerza, tipo de vínculo, eje, nivel, papel, término, sentido, base, clase y plano) trae un valor del catálogo |
| SV-110 | en parte: cada nodo de un tipo que pertenece a un plano declara su plano; no se comprueba que un cambio del plano B no modifique un concepto |
| SV-119 | los pre-ensayos del plano A que nombran un producto o un proveedor quedan marcados (advertencia) |
| SV-120 | cada equivalencia declarada trae evidencia, método y confianza; ninguna fusiona nodos |
| SV-121 | ningún nodo usa los tipos reservados para instancias observadas del eje H |
| SV-212 | por tipo, cuántos nodos no traen las propiedades que la definición enuncia (advertencia por tipo) |

## 6. Preguntas de competencia

De las 22 preguntas, 7 son respondibles con el grafo candidato, 9 en parte y 6 todavía no. En la versión 1.3 eran 7, 9 y 6. El estado se deriva de una prueba: respondible = expresable, cobertura mayor o igual al umbral y sin límite declarado; en parte = cobertura menor o límite declarado; todavía no = no expresable o sin instancias.

| N.º | Pregunta | Estado | Por qué |
|---|---|---|---|
| 1 | ¿Qué activos sostienen una capacidad empresarial crítica? | todavía no | sin instancias en el grafo |
| 2 | ¿Qué escenarios de riesgo pueden afectarla? | todavía no | sin instancias en el grafo |
| 3 | ¿Qué controles contribuyen a mitigar esos escenarios? | todavía no | sin instancias en el grafo |
| 4 | ¿Qué evidencia respalda la efectividad de los controles? | todavía no | sin instancias en el grafo |
| 5 | ¿Qué autoridad puede aceptar el riesgo residual? | todavía no | sin instancias en el grafo |
| 6 | ¿Qué agentes poseen autoridad sobre determinados activos? | todavía no | sin instancias en el grafo |
| 7 | ¿Qué herramientas y acciones están disponibles para esos agentes? | en parte | límite declarado El grafo no tiene instancias de AutonomousAction: la consulta devuelve las herramientas de cada agente, no sus acciones. |
| 8 | ¿Qué fuerzas condicionan la evolución de una capacidad? | en parte | límite declarado A nivel de capacidad la pregunta no puede expresarse: no hay capacidades instanciadas. La consulta responde a nivel de dominio, con las fuerzas (catalizadores e inhibidores) que tratan sus pre-ensayos. |
| 9 | ¿Qué competencias necesita desarrollar un responsable? | en parte | cobertura menor que 90 % |
| 10 | ¿Qué unidades GM-24 desarrollan y evalúan esas competencias? | en parte | límite declarado La unidad se infiere de los conceptos que sostienen la competencia: el grafo no tiene relaciones de desarrollo ni de evaluación (0 aristas DEVELOPS y ASSESSES). Que un concepto pertenezca a una unidad no prueba que la unidad desarrolle la competencia, y la parte «evalúan» no tiene respuesta. |
| 11 | ¿Qué pre-ensayos cubren una coordenada (territorio × dominio × subfunción) y con qué confianza? | respondible | cobertura de al menos 90 % |
| 12 | ¿Qué elementos de qué artefactos de referencia respaldan un concepto y con qué fuerza? | respondible | cobertura de al menos 90 % |
| 13 | ¿Qué agentes ejecutan tareas de un producto-control, con qué nivel de autonomía y bajo qué puntos de control? | respondible | cobertura de al menos 90 % |
| 14 | ¿Qué conceptos del corpus instancia cada producto-control? | respondible | cobertura de al menos 90 % |
| 15 | ¿Qué fuerzas y qué mecanismos homeostáticos tratan los pre-ensayos de un dominio? | respondible | cobertura de al menos 90 % |
| 16 | ¿Qué indicadores miden una variable homeostática y a qué decisión informan? | en parte | límite declarado Son indicadores candidatos de un modelo de referencia: ninguna variable tiene unidad, umbral ni responsable del límite. No hay decisiones instanciadas, de modo que «a qué decisión informa» se responde solo con el órgano de gobierno que recibe el indicador. |
| 17 | ¿Qué prácticas metacognitivas contrarrestan los sesgos que pueden distorsionar una decisión? | en parte | límite declarado No hay decisiones instanciadas sobre las que declarar qué sesgo las distorsiona. Los vínculos expresan lo que la Biblioteca propone, no eficacia probada, y cubren una parte menor de los sesgos. |
| 18 | ¿Qué preguntas tienen un pre-ensayo directo y todavía no tienen un ensayo aprobado? | respondible | cobertura de al menos 90 % |
| 19 | ¿Qué competencias requiere un rol y qué conceptos y unidades las sostienen? | en parte | cobertura menor que 90 % |
| 20 | ¿Qué celdas del Atlas no tienen conocimiento (silencios)? | en parte | límite declarado la consulta no distingue las combinaciones de territorio y dominio que no pueden darse de las que no tienen contenido |
| 21 | ¿Qué conceptos de la Biblioteca cognitiva propone cubrir cada unidad del GM-24 y con qué confianza editorial? | respondible | cobertura de al menos 90 % |
| 22 | ¿Qué indicadores están clasificados en cada subfunción del Atlas y qué subfunciones no tienen ninguno? | en parte | límite declarado La consulta responde «qué indicadores están clasificados en cada subfunción», no «cuáles la miden»: la regla SV-118 no admite MEASURES hacia una subfunción. Los 20 indicadores del sub-plan PO-GAC no tienen coordenada en el Atlas. |

Las preguntas que siguen en «todavía no» piden instancias de una organización: activos, escenarios, autoridades. La ontología 2.2.0 ya puede expresarlas; el Atlas no tiene con qué responderlas.

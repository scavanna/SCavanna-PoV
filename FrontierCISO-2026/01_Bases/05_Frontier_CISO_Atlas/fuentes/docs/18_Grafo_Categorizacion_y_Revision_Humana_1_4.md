# Grafo, categorización y revisión humana · versión 1.4

**Frontier CISO Atlas 1.4** · Taxonomía 6.1 (reglas de asignación, revisión 3) · Ontología 2.2.0 (propuesta) · GM-24 V7.1 · 16 de noviembre de 2026 · Estado: respuestas del autor registradas de forma literal; lo que decidió el curador en esta versión espera su confirmación (D-16); corpus releído por lectores automáticos con una vara de tres lecturas, que el curador endureció después de leer; contenido candidato, sin validación humana

Este documento describe cómo quedó categorizado el corpus después de la relectura, qué contiene el grafo candidato, qué hace falta para pasar de un grafo candidato a un grafo aprobado con ensayos, y cómo se hace la revisión humana. Los documentos 06 y 07 se conservan como registro de la versión 1.3.

## 1. La categorización del corpus

Los 739 pre-ensayos tienen una coordenada primaria: territorio, dominio y subfunción. La comparación es con la versión 1.3, que es la publicada anterior; la base de la relectura fue la versión 1.2 (documento 15, sección 3).

### 1.1 Por territorio

| Código | Territorio | Versión 1.3 | Versión 1.4 | Diferencia |
|---|---|---|---|---|
| T01 | SELF & JUDGMENT | 5 | 8 | +3 |
| T02 | LEADERSHIP & ORGANIZATION | 90 | 70 | -20 |
| T03 | STRATEGY & BUSINESS | 80 | 80 | = |
| T04 | RISK & RESILIENCE | 139 | 131 | -8 |
| T05 | SECURITY ARCHITECTURE | 88 | 103 | +15 |
| T06 | SECURITY OPERATIONS | 84 | 79 | -5 |
| T07 | AI & AUTONOMOUS SYSTEMS | 102 | 119 | +17 |
| T08 | TRUST & ASSURANCE | 151 | 149 | -2 |

### 1.2 Por dominio

| Código | Dominio | Versión 1.3 | Versión 1.4 | Diferencia |
|---|---|---|---|---|
| D01 | Cybersecurity Governance | 126 | 105 | -21 |
| D02 | Cyber Risk Management | 94 | 88 | -6 |
| D03 | Compliance & Regulatory Security | 42 | 37 | -5 |
| D04 | Security Program & Investment Management | 52 | 62 | +10 |
| D05 | Identity & Access Security | 30 | 30 | = |
| D06 | Data Security & Information Protection | 20 | 22 | +2 |
| D07 | Privacy & Data Protection Engineering | 7 | 15 | +8 |
| D08 | Network & Infrastructure Security | 3 | 3 | = |
| D09 | Endpoint & Workplace Security | 8 | 11 | +3 |
| D10 | Cloud & Platform Security | 4 | 5 | +1 |
| D11 | Application & Software Security | 7 | 8 | +1 |
| D12 | Threat Intelligence & Threat Modeling | 24 | 22 | -2 |
| D13 | Vulnerability & Exposure Management | 16 | 15 | -1 |
| D14 | Security Monitoring & Detection | 23 | 23 | = |
| D15 | Incident Response & Crisis Management | 42 | 39 | -3 |
| D16 | Business Continuity & Cyber Recovery | 23 | 24 | +1 |
| D17 | Third-Party & Supply Chain Security | 28 | 32 | +4 |
| D18 | Operational Technology & Industrial Control Security | 4 | 4 | = |
| D19 | IoT & Cyber-Physical Systems Security | 0 | 0 | = |
| D20 | AI & Agent Security | 43 | 43 | = |
| D21 | AI for Cyber Defense & Security Operations | 11 | 15 | +4 |
| D22 | AI for Security Assessment & Testing | 3 | 3 | = |
| D23 | AI for Security Engineering & Automation | 5 | 6 | +1 |
| D24 | Security Workforce & Human Factors | 43 | 47 | +4 |
| D25 | Enterprise Security Architecture & Zero Trust | 18 | 16 | -2 |
| D26 | Cryptography, Key Management & Post-Quantum Readiness | 5 | 5 | = |
| D27 | Physical, Environmental & Facility Security | 1 | 1 | = |
| D28 | Security Assurance, Testing & Measurement | 57 | 58 | +1 |

### 1.3 Por función y subfunción

| Código | Función | Versión 1.3 | Versión 1.4 | Diferencia |
|---|---|---|---|---|
| GV | Gobernar | 366 | 358 | -8 |
| ID | Identificar | 115 | 126 | +11 |
| PR | Proteger | 151 | 160 | +9 |
| DE | Detectar | 31 | 33 | +2 |
| RS | Responder | 48 | 45 | -3 |
| RC | Recuperar | 28 | 17 | -11 |

| Código | Subfunción | Versión 1.3 | Versión 1.4 | Diferencia |
|---|---|---|---|---|
| GV01 | Contexto empresarial y estrategia | 18 | 22 | +4 |
| GV02 | Estructura de gobierno y autoridad | 43 | 28 | -15 |
| GV03 | Políticas y estándares | 58 | 55 | -3 |
| GV04 | Apetito, tolerancia y aceptación de riesgo | 47 | 43 | -4 |
| GV05 | Gobierno de programas, recursos e inversión | 39 | 38 | -1 |
| GV06 | Obligaciones legales y contractuales | 32 | 35 | +3 |
| GV07 | Supervisión y reporting ejecutivo | 34 | 37 | +3 |
| GV08 | Assurance y revisión independiente | 46 | 45 | -1 |
| GV09 | Gobierno de terceros y ecosistemas | 27 | 31 | +4 |
| GV10 | Ética, cultura y rendición de cuentas | 22 | 24 | +2 |
| ID01 | Inventario y clasificación de activos | 17 | 17 | = |
| ID02 | Dependencias y criticidad del negocio | 6 | 8 | +2 |
| ID03 | Amenazas, vulnerabilidades y exposición | 33 | 36 | +3 |
| ID04 | Análisis de escenarios y cuantificación de riesgos | 33 | 26 | -7 |
| ID05 | Evaluación de capacidades y brechas | 26 | 27 | +1 |
| ID06 | Mejora continua y lecciones aprendidas | 0 | 12 | +12 |
| PR01 | Identidad y autorización | 36 | 36 | = |
| PR02 | Protección de datos y privacidad por diseño | 28 | 31 | +3 |
| PR03 | Hardening y arquitectura segura | 45 | 50 | +5 |
| PR04 | Desarrollo seguro y gestión de cambios | 18 | 21 | +3 |
| PR05 | Preparación de personas y procedimientos | 21 | 19 | -2 |
| PR06 | Resiliencia de la infraestructura y protección física y ambiental | 3 | 3 | = |
| DE01 | Telemetría y observabilidad | 5 | 6 | +1 |
| DE02 | Ingeniería de detección y análisis | 16 | 16 | = |
| DE03 | Hunting, validación y mejora de detecciones | 4 | 4 | = |
| DE04 | Evaluación de cobertura y calidad de detección | 6 | 7 | +1 |
| RS01 | Preparación y coordinación de respuesta | 22 | 20 | -2 |
| RS02 | Contención, erradicación y preservación de evidencia | 13 | 12 | -1 |
| RS03 | Comunicación de crisis y decisiones ejecutivas | 11 | 10 | -1 |
| RS04 | Gestión de incidentes con terceros | 2 | 3 | +1 |
| RC01 | Restauración y recuperación técnica | 7 | 6 | -1 |
| RC02 | Continuidad y operación degradada | 6 | 7 | +1 |
| RC03 | Validación de recuperación y retorno seguro | 5 | 4 | -1 |
| RC04 | Lecciones y cierre de la recuperación | 10 | 0 | -10 |
| RC05 | Comunicación de la recuperación y restitución de la confianza | 0 | 0 | = |

Dominios sin pre-ensayos: D19. Subfunciones sin pre-ensayos: RC04 y RC05. De las 224 celdas de territorio por dominio, 137 no tienen pre-ensayos. Una celda vacía no es por sí sola un hueco: muchas combinaciones no tienen sentido.

### 1.4 Horizonte, convergencia y pilar

| Horizonte | Versión 1.3 | Versión 1.4 |
|---|---|---|
| H01 | 341 | 352 |
| H02 | 240 | 250 |
| H03 | 123 | 123 |
| H04 | 22 | 0 |
| indeterminado | 13 | 14 |

En la versión 1.3, H04 era un horizonte. En la 1.4 es un marcador aparte: 11 pre-ensayos lo tienen en «sí». Los que tenían H04 recibieron un horizonte donde las dos lecturas coincidieron y quedaron como «indeterminado» donde no (documento 15, sección 4.6).

| Pilar del MCCS | Pre-ensayos |
|---|---|
| DO | 487 |
| MM | 48 |
| NX | 60 |
| OS | 144 |

El pilar no se releyó en esta versión.

### 1.5 De dónde sale cada coordenada

| Origen del cambio en la versión 1.4 | Ejes |
|---|---|
| relectura 1.4: nuevo alcance de RC04 (RD-03), las dos lecturas a ciegas coinciden (ADR-028) | 9 |
| relectura 1.4: dos lecturas a ciegas coinciden, con confianza alta, y la tercera lectura prefiere el valor nuevo | 86 |
| relectura 1.4: nuevo alcance de RC04 (RD-03), dos de las tres lecturas coinciden (ADR-028) | 1 |

En total, la versión 1.4 cambia 96 coordenadas primarias del corpus en 87 pre-ensayos, y conserva los 37 cambios de la versión 1.2 que el autor confirmó. Cada pre-ensayo trae en el corpus (`data/corpus_frontier_739.json`) la lista de sus cambios, con la versión y el origen. La planilla es `data/categorizacion_739.csv`.

**Contra qué versión se cuenta.** Esos cambios se cuentan contra la versión 1.2. Contra la versión 1.3, que es la publicada, difieren 282 coordenadas del corpus en 229 pre-ensayos, porque esta versión no dio por buenos los cambios de la 1.3 y volvió a leer todo. Y en 594 coordenadas del corpus las dos lecturas de esta versión coinciden en un valor distinto del que queda (documento 15, sección 4).

**La confianza que acompaña a cada coordenada no es la de esta relectura.** La planilla y el grafo traen la confianza que declaró el clasificador de la versión 1.0, que figura «alta» en 503 de los 739 pre-ensayos. Las lecturas de la versión 1.4 no la reemplazaron: su confianza, eje por eje, está en `data/relectura_1_4_por_eje.csv`. Es un pendiente declarado.

**Pre-ensayos que nombran un producto o un proveedor.** Son 77 (33 de la serie AMP, 5 de la serie K y 39 de la serie PA). El plano A se propone agnóstico de proveedor: quedan marcados y fuera de la promoción a ensayo hasta que se reescriban (regla SV-119).

## 2. El grafo candidato

| Elemento | Versión 1.3 | Versión 1.4 |
|---|---|---|
| Nodos | 5.058 | 5.059 |
| Relaciones | 28.249 | 28.553 |
| Conjuntos de cambios | 16 | 17 |
| Tipos usados | 32 de 84 | 34 de 86 |
| Relaciones usadas | 32 de 93 | 33 de 98 |
| Reglas comprobadas | 19 de 37 | 25 de 42 |
| Errores de validación | 0 | 0 |
| Advertencias | 77 | 80 |

La validación es estructural. Dice que los nodos y las relaciones respetan los diccionarios y las reglas; no dice si el contenido es correcto. Las 80 advertencias son: 77 de la regla SV-119 y 3 de la regla SV-212. El grafo se puede reconstruir desde los conjuntos de cambios: la reconstrucción da los mismos nodos y las mismas relaciones.

### 2.1 Conjuntos de cambios

Todos están en estado «propuesto». Ninguno se aprueba sin una decisión del autor.

| Conjunto | Qué trae | Nodos | Relaciones |
|---|---|---|---|
| CHG-CAND-01 | Taxonomía 6.1: categorías, jerarquía, modelo de equilibrio y lentes | 138 | 104 |
| CHG-CAND-02 | Base de referencia: organismos, artefactos, elementos y cruce con dominios | 657 | 1.093 |
| CHG-CAND-03 | Currículo TheNextCISO GM-24 V7.1: itinerarios, unidades, conceptos y competencias | 447 | 726 |
| CHG-CAND-04 | Pre-ensayos (739) y su categorización con la Taxonomía 6.1 | 739 | 8.492 |
| CHG-CAND-05 | Vínculos editoriales entre pre-ensayos (predicado original y familia normalizada) | 0 | 1.700 |
| CHG-CAND-06 | Mapeo de conceptos del GM-24 V7.1 a elementos de marcos (tres niveles; no afirma conformidad) | 0 | 7.559 |
| CHG-CAND-07 | Preguntas del CISO, al CISO y de los marcos (595) y su cobertura directa | 595 | 2.765 |
| CHG-CAND-08 | Productos-control, modelos operativos y tareas por cadencia (siete instancias de dominio) | 347 | 1.189 |
| CHG-CAND-09 | Agentes, flotas, herramientas, conocimiento, habilidades, autonomía y controles de gobierno de agentes | 373 | 1.188 |
| CHG-CAND-10 | Indicadores: sub-plan PO-GAC (20, sin coordenada en el Atlas) y catálogo del Modelo Operativo CISO 365 2.0 (224, con coordenada) | 244 | 1.173 |
| CHG-CAND-11 | Medición: indicadores que miden las variables homeostáticas, órganos de gobierno a los que informan, objetivos y resultados clave | 99 | 622 |
| CHG-CAND-12 | Biblioteca metacognitiva (MCCS): 1.404 elementos tipificados, con su categoría y su pilar (los territorios de la base quedan como propiedad, sin afirmarse como clasificación) | 1.404 | 1.403 |
| CHG-CAND-13 | Cobertura pedagógica propuesta entre unidades del GM-24 y conceptos de la Biblioteca (solo los vínculos de selección editorial o de ancla expresa) | 0 | 165 |
| CHG-CAND-14 | Prácticas que la Biblioteca propone para contrarrestar sesgos (solo los vínculos que la segunda lectura juzgó sostenibles; no afirman eficacia probada) | 0 | 57 |
| CHG-CAND-15 | Propuesta de remapeo a matrices vigentes: vínculos que se agregan (no aplicada al GM-24) | 0 | 7 |
| CHG-CAND-16 | Capa de ampliación: 16 pre-ensayos de la serie APX para celdas en blanco (decisión D-10 confirmada por el autor el 16-nov-2026, D-14.3; redacción asistida) | 16 | 198 |
| CHG-CAND-17 | Equivalencias entre pre-ensayos y elementos de la biblioteca metacognitiva halladas por la revisión crítica de la versión 1.2 (una lectura; no se fusionan nodos) | 0 | 112 |

### 2.2 Nodos y relaciones

| Tipo de nodo | Nodos |
|---|---|
| `Precursor` | 755 |
| `Question` | 595 |
| `CognitiveBias` | 479 |
| `Concept` | 473 |
| `FrameworkElement` | 469 |
| `HumanCapability` | 392 |
| `SecurityIndicator` | 244 |
| `MentalModel` | 214 |
| `ProductPractice` | 180 |
| `MetacognitivePractice` | 166 |
| `ReferenceArtifact` | 146 |
| `TaxonomyCategory` | 138 |
| `Role` | 85 |
| `AIAgent` | 85 |
| `ApprovalGate` | 85 |
| `Tool` | 82 |
| `KeyResult` | 72 |
| `KnowledgeSource` | 51 |
| `OperationalPractice` | 50 |
| `AgentSkill` | 46 |
| `LogicalFallacy` | 45 |
| `ReferenceBody` | 42 |
| `Competency` | 41 |
| `LearningUnit` | 24 |
| `SecurityControl` | 24 |
| `Objective` | 24 |
| `CognitiveState` | 14 |
| `ControlProduct` | 7 |
| `TechnologyProduct` | 7 |
| `OperatingModel` | 7 |
| `AgentFleet` | 7 |
| `AutonomyLevel` | 5 |
| `GovernanceBody` | 3 |
| `LearningPath` | 2 |

| Relación | Cantidad |
|---|---|
| `CLASSIFIED_IN` | 13.002 |
| `MAPS_TO` | 8.434 |
| `RELATES_TO` | 1.396 |
| `PART_OF` | 1.271 |
| `ADDRESSES` | 595 |
| `SPECIALIZES` | 413 |
| `EXPLAINS` | 379 |
| `INFORMS` | 371 |
| `PERFORMS` | 336 |
| `OPERATES_AT` | 283 |
| `INVOKES` | 268 |
| `GATED_BY` | 219 |
| `EXEMPLIFIES` | 180 |
| `COVERS_CONCEPT` | 165 |
| `SUSTAINED_BY` | 154 |
| `USES_KNOWLEDGE` | 150 |
| `PUBLISHES` | 146 |
| `MEASURES` | 122 |
| `INSTANTIATES` | 120 |
| `EXPOSED_TO` | 117 |
| `TRACKED_BY` | 108 |
| `ADVANCES` | 72 |
| `COUNTERS` | 57 |
| `REQUIRES_COMPETENCY` | 41 |
| `SEQUENCES` | 29 |
| `PRESSURES` | 27 |
| `REGULATES` | 21 |
| `APPLIES_SKILL` | 21 |
| `SAME_CONCEPT_AS` | 21 |
| `OWNS` | 14 |
| `REALIZED_BY` | 7 |
| `OPERATED_UNDER` | 7 |
| `SERVES` | 7 |

### 2.3 Qué cambió en el grafo respecto de la versión 1.3

- Las falacias son un tipo propio (`LogicalFallacy`, 45 nodos) y dejan de cargarse como sesgos; 14 elementos de la biblioteca pasan a `CognitiveState`.
- Se cargan 112 equivalencias entre la biblioteca y el corpus: 21 como `SAME_CONCEPT_AS` y 91 como `RELATES_TO`. Tienen una sola lectura y no fusionan nodos.
- Cada vínculo «regula» lleva el papel del mecanismo y cada vínculo «presiona», el término y el sentido. Los mecanismos homeostáticos se cargan con el rol «mecanismo» y ya no con el rol «fuerza».
- H04 se carga como marcador de convergencia, en un eje propio, y no como horizonte.
- 134 pares de tarea y punto de control quedan unidos, con el agente como propiedad del vínculo.
- El plano es una propiedad del nodo en los tipos que pertenecen a un plano, y la lente de la agenda de IA se deriva de la coordenada.
- Los códigos del corpus son válidos en la Taxonomía 6.1. La asignación es la de la versión 1.2, con los cambios que aplicó la relectura de la versión 1.4 (sección 1.5): no es una categorización hecha de nuevo con la 6.1.

### 2.4 Qué no tiene el grafo

- **Ensayos.** No hay ningún nodo de tipo `Essay`: el Atlas tiene pre-ensayos. La primera tanda propuesta está en la sección 4.
- **Instancias de una organización.** No hay activos, escenarios de riesgo, autoridades ni mediciones de una organización concreta. Por eso seis preguntas de competencia siguen sin respuesta (documento 17, sección 6).
- **Territorios afirmados para la biblioteca.** Los 1.404 elementos de la biblioteca traen sus territorios como propiedad, sin afirmarse como clasificación. No llevan dominio (RD-23).
- **Vínculos entre la medición y el corpus.** Hay 0: los indicadores se ubican en la taxonomía, y no se vinculan con pre-ensayos.

## 3. Qué hace falta para construir el grafo de conocimiento con ensayos

El grafo que este paquete trae es candidato. Para pasar a un grafo aprobado que incorpore ensayos, en este orden. La lista no es corta ni cercana: la única validación humana prevista cubre los tres ejes primarios de los pre-ensayos de una muestra, y el resto del grafo (los cruces con marcos, la biblioteca, los agentes, la medición) no tiene ninguna revisión humana prevista en este paquete.

1. **Decidir D-16**, salvo la vara (D-16.2), que puede esperar a la revisión humana. Confirmar, corregir o revertir lo que decidió el curador. Una regla que el autor rechace cambia la categorización.
2. **Hacer la revisión humana** de la muestra (193 pre-ensayos), con el umbral fijado antes de abrir la clave (sección 5). Es lo único que puede llevar la categorización de «base de trabajo» a «revisada por el autor en una muestra».
3. **Redactar los ensayos.** Cada ensayo desarrolla la tesis de un pre-ensayo. La primera tanda propuesta tiene 34 (sección 4). La coordenada de cada ensayo se revisa al escribirlo.
4. **Cargar cada ensayo** como nodo `Essay`, unido a su pre-ensayo y clasificado con la Taxonomía 6.1, en un conjunto de cambios propio. La ontología ya define el tipo y sus relaciones.
5. **Reescribir o separar los 77 pre-ensayos que nombran un producto o un proveedor** antes de promoverlos.
6. **Decidir las equivalencias** entre la biblioteca y el corpus: las 112 cargadas tienen una sola lectura.
7. **Aprobar los conjuntos de cambios.** Hoy todos están en estado «propuesto». La aprobación es una decisión del autor, conjunto por conjunto, y pide revisar el contenido de cada uno: la revisión humana de la muestra no alcanza para aprobar los que cargan los cruces, la biblioteca, los agentes o la medición. Este paquete no trae un procedimiento de revisión para ellos.
8. **Poner el paquete bajo control de versiones.** La ontología lo declara como requisito pendiente: «previsto: Git (requisito R11, pendiente; el paquete no contiene un repositorio)».
9. **Elegir el motor de grafo.** El paquete entrega el grafo en SQLite y en CSV, con su esquema y con las consultas de aceptación en SQL. La planilla de nodos trae las propiedades en una columna. La carga a un motor de grafo de propiedades es un paso posterior.
10. **Sumar instancias de una organización**, si se quiere responder las preguntas de competencia que hoy no tienen con qué responderse.

## 4. La primera tanda de ensayos propuesta

Son 34 pre-ensayos, que cubren 22 de los 27 dominios con pre-ensayos y 53 preguntas directas. Regla: (1) el pre-ensayo con más preguntas directas de cada dominio poblado; (2) completar hasta 2 por territorio, 2 por función y 4 por pilar MCCS;
(3) sumar los pre-ensayos de confianza alta de los dominios nuevos con pocos pre-ensayos (D26 y D27) y del territorio T01, el menos poblado.
Solo entran pre-ensayos con confianza alta: un dominio cuyos pre-ensayos tienen todos confianza media o baja queda sin cubrir y se informa.
Desde la versión 1.3, además, la coordenada tiene que haber quedado sostenida por la relectura en sus tres ejes primarios.
Versión 1.4: «sostenida» quiere decir que las dos lecturas a ciegas de esta versión coinciden con el valor de la base en los tres ejes. Quedan fuera los pre-ensayos
que cambiaron de coordenada (la confianza del clasificador no vale para el valor nuevo), aquellos en que una lectura difiere y, por la regla SV-119, los que nombran
un producto o un proveedor: no se promueven a ensayo hasta que se reescriban sin marca.

| Territorio | T01 | T02 | T03 | T04 | T05 | T06 | T07 | T08 |
|---|---|---|---|---|---|---|---|---|
| Pre-ensayos | 1 | 3 | 2 | 8 | 8 | 5 | 3 | 4 |

De los 503 pre-ensayos con confianza alta del clasificador, 195 tienen la coordenada sostenida por las dos lecturas de la versión 1.4 en los tres ejes; de esos, 23 quedan fuera por nombrar un producto o un proveedor, y quedan 172 candidatos. La confianza es la que el clasificador declaró para la coordenada; no mide la calidad del pre-ensayo. La tanda se recalculó en la versión 1.2, después de aplicar la decisión D-03, y otra vez en las versiones 1.3 y 1.4, después de cada relectura: solo entran pre-ensayos cuyos tres ejes primarios quedaron sostenidos por las dos lecturas a ciegas de la versión 1.4 y que no nombran productos ni proveedores (regla SV-119).

Dominios sin cubrir: D10 (ninguno de sus pre-ensayos tiene confianza alta y la coordenada sostenida por la relectura), D18 (ninguno de sus pre-ensayos tiene confianza alta y la coordenada sostenida por la relectura), D22 (ninguno de sus pre-ensayos tiene confianza alta y la coordenada sostenida por la relectura), D26 (ninguno de sus pre-ensayos tiene confianza alta y la coordenada sostenida por la relectura) y D27 (ninguno de sus pre-ensayos tiene confianza alta y la coordenada sostenida por la relectura). La lista está en `data/primera_tanda_propuesta.csv`.

## 5. La revisión humana

**Estado.** kit preparado para el autor; la revisión no se ejecutó. Sobre el tamaño, el autor respondió el 16 de noviembre de 2026 «Procede con la decision de mayor rigurosidad»; el curador lo leyó como una delegación y tomó el diseño completo. Entre el camino mínimo y el diseño completo, el curador tomó el diseño completo: la estimación para todo el corpus tiene un margen de 6,4 puntos, contra 11,3 del camino mínimo, y con el camino mínimo los resultados por estrato, de veinte casos cada uno, casi nunca concluyen. El camino mínimo también puede dar «cumple» o «no cumple» para todo el corpus. El autor puede revertirlo: el camino mínimo es la tanda 1 de esta misma muestra.

**Qué se revisa.** Territorio primario, dominio primario y subfunción primaria de cada pre-ensayo de la muestra. El horizonte, las fuerzas y el pilar no entran.

**Quién.** El autor, o una persona con formación de CISO que él designe. El agente curador mantiene el paquete y no hace esta revisión. Con una sola persona, que además es el autor del banco, el resultado es «revisada por el autor en una muestra». Para decir «validada» hace falta una segunda persona, que lea al menos un tercio de la muestra sin ver la lectura de la primera. Se informa cuánto coinciden las dos.

**Con qué reglas.** Con la Taxonomía 6.1 y sus reglas de asignación, revisión 3: las reglas base, los enunciados adoptados, las reglas decididas por delegación y las definiciones de trabajo de las 35 subfunciones (documento 16). El documento 16 trae las reglas decididas y las definiciones; el texto completo, con las reglas base y los enunciados adoptados, es el que recibieron los lectores automáticos: relectura_1_4/lectura_a/REGLAS.md. Las reglas decididas por el curador no las vio el autor: si al leer no está de acuerdo con una, conviene anotarlo en la columna de observaciones, porque eso también es un resultado.

### 5.1 La muestra

| Estrato | Qué es | Pre-ensayos | En la muestra | Cómo se eligieron | Margen del estrato, en puntos |
|---|---|---|---|---|---|
| R1 | Cambió con la relectura de la versión 1.4: en algún eje, las dos lecturas a ciegas coincidieron en otro valor con confianza alta y la tercera lo prefirió, o el cambio salió del nuevo alcance de RC04 | 87 | 39 | sorteo simple sin reposición | 11,8 |
| R2a | No cambió, y habría cambiado con la vara fijada antes de leer: en algún eje, las dos lecturas coincidieron en otro valor, la tercera lo prefirió y alguna de las dos declaró confianza media | 243 | 53 | sorteo simple sin reposición | 12,0 |
| R2b | Alguna lectura a ciegas apunta fuera de la coordenada y el cambio no entró por otro motivo: las lecturas no coinciden, una declaró confianza baja, la tercera lectura no prefirió el valor nuevo o el eje está protegido | 164 | 48 | sorteo simple sin reposición | 12,0 |
| R3 | Las dos lecturas a ciegas sostienen la coordenada en los tres ejes | 245 | 53 | sorteo simple sin reposición | 12,0 |

Total: 193 pre-ensayos. Semilla del sorteo: 20261126. La propuesta de la versión 1.3 (159 pre-ensayos en tres estratos), que se apoyaba en la relectura de esa versión. La categorización cambió con la relectura de la versión 1.4 y la muestra se volvió a sortear sobre ella, con cuatro estratos: uno reúne los pre-ensayos que habrían cambiado con la vara fijada antes de leer y no cambiaron, para que la revisión pueda decir cuál de las dos varas convenía.

**Tamaño.** n0 = z² · p · (1 − p) / e², corregido por población finita: n = n0 / (1 + (n0 − 1) / N), con un nivel de confianza del 95 %. p = 0,5 es el valor que no supone ninguna tasa y da el tamaño más grande. 12 puntos es el margen de cada estrato, tomado solo. La estimación para todo el corpus pondera los cuatro estratos: su margen es de 6,4 puntos con el diseño completo y de 11,3 con el camino mínimo.

| Tanda | Qué | Pre-ensayos | Para qué alcanza |
|---|---|---|---|
| 1 | Los primeros 20 casos sorteados de cada estrato, mezclados. | 80 | Una primera estimación, con un margen amplio, y una primera mirada a si la relectura mejoró o empeoró lo que cambió |
| 2 | El resto de los casos sorteados. | 113 | Lleva la estimación al margen del diseño completo |

**Esfuerzo.** 5 minutos por pre-ensayo. Es un supuesto, no una medida: conviene cronometrar los primeros diez. El diseño completo son 193 pre-ensayos, unas 16,1 horas, con un margen de 6,4 puntos para la estimación de todo el corpus. El camino mínimo es la tanda 1: 80 pre-ensayos, unas 6,7 horas y un margen de 11,3 puntos. Da una estimación para todo el corpus con ese margen. Los resultados por estrato, de veinte casos cada uno, casi nunca concluyen. Sí. El autor puede dejar la categorización como base de trabajo, sin validar, y redactar ensayos sabiendo que la coordenada de cada uno se revisa al escribirlo.

### 5.2 El protocolo, paso por paso

El protocolo está también en un archivo aparte, `data/revision_humana_protocolo.md`, que no muestra resultados de la relectura. Este documento sí los muestra: quien quiera leer a ciegas tiene que usar ese archivo y no este.

1. **Fijar el umbral antes de abrir la clave.** El autor escribe qué parte de coincidencia considera suficiente: un umbral para los tres ejes, o uno por eje. Los umbrales los fija el autor, antes de mirar la clave. Este paquete no propone valores.
2. **Leer a ciegas.** La planilla trae el mismo registro que recibieron los lectores automáticos: el título, la tesis ya ubicada y de dónde se tomó, las oraciones que la preceden y el texto, con la oración de plantilla reemplazada por una marca donde la había. La muestra no trae identificadores ni coordenadas: cada caso lleva un número de orden y la clave lo une con su identificador, su estrato y sus valores en las versiones 1.2 y 1.4. Para leer a ciegas hay que leer la muestra antes de abrir la clave, los documentos 15 y 18 y los archivos de la relectura: esos documentos nombran pre-ensayos que están en la muestra y dicen qué lectura tuvo cada uno. El protocolo está aparte, en data/revision_humana_protocolo.md, y no muestra resultados. Si ya abriste el documento 15, sus tablas nombran con sus valores algunos pre-ensayos de la muestra (los casos de D20, los ejes protegidos y los cambios de RC04): esos casos ya no se leen a ciegas, y hay que decirlo al informar el resultado. Algunos textos nombran su unidad o su tema en el cuerpo: eso no se quitó.
3. **Anotar en una copia.** Copiar data/revision_humana_muestra.csv con otro nombre, fuera de la carpeta data/, y anotar en la copia. En cada celda va solo el código: por ejemplo T04, D12 o ID03. Una celda vacía deja ese eje sin evaluar en ese caso. Se guarda como CSV. El guion de cálculo rechaza, con un aviso, una anotación que no sea un código del catálogo. Se puede dejar una observación. No conviene anotar sobre el archivo del paquete: el guion que arma la muestra lo escribe de nuevo cada vez que se regenera. Como resguardo, ese guion se detiene si encuentra anotaciones en el archivo.
4. **Calcular.** scripts/evaluar_revision_humana.py lee la planilla completada, que se le pasa por argumento, y la clave, y calcula las medidas y sus intervalos. Los umbrales se le pasan como argumento: no trae valores por defecto. Desde la raíz del paquete: `python3 scripts/evaluar_revision_humana.py <copia anotada.csv> --umbral <valor entre 0 y 1>`; con `--tanda 1` evalúa solo la primera tanda.
5. **Decidir.** Cumple: El límite inferior del intervalo de coincidencia queda por encima del umbral. No cumple: El límite superior del intervalo queda por debajo del umbral. No concluyente: El umbral queda dentro del intervalo: la muestra no alcanza para decidir. El guion entrega un resultado por eje para todo el corpus y uno por eje para cada estrato. El del corpus responde si la categorización, en conjunto, cumple el umbral. El de cada estrato dice dónde están las diferencias: R1 es el de los ejes que la relectura cambió y R2a, el de los que habrían cambiado con la vara fijada antes de leer. Pueden no coincidir: si el corpus cumple y un estrato no, la categorización cumple en conjunto y ese estrato se relee. Si un estrato tiene menos de dos casos con un eje anotado, no hay resultado para el corpus en ese eje. Esta lectura la propone el curador: el autor puede fijar otra antes de abrir la clave.

| Resultado | Qué se hace |
|---|---|
| Cumple | La categorización pasa de «base de trabajo» a «revisada por el autor en una muestra», con la medida y su intervalo a la vista. Las diferencias del revisor se aplican. |
| No cumple | Los pre-ensayos del estrato que no cumple no se usan para redactar ensayos hasta que una persona los relea. Que los relea el mismo lector automático con las mismas reglas no alcanza: daría el acuerdo entre corridas que este paquete ya midió, y ese acuerdo no dice si la coordenada es correcta. Antes de releer se corrigen las reglas en que el revisor y las lecturas difieren, que es lo que la revisión deja a la vista. |
| No concluyente | Se amplía el sorteo o se acepta seguir con la categorización como base de trabajo. No se la llama revisada. |

**Sobre los cambios de la relectura.** Hay dos comparaciones, y el guion da para cada una el conteo y un intervalo. En los ejes que cambiaron: si el intervalo queda entero del lado del valor de la versión 1.2, el revisor coincide más con el valor anterior y los cambios de la relectura quedan en duda. En los ejes que habrían cambiado con la vara fijada antes de leer: si el intervalo queda entero del lado del valor de las lecturas, el revisor coincide más con la vara fijada. Si el intervalo incluye la mitad, la muestra no alcanza para decidir entre las dos. Qué diferencia alcanza para cambiar de vara lo decide el autor antes de abrir la clave: este paquete no fija ese número. Los casos en que el revisor no coincide con ninguno de los dos se informan aparte y dicen cuánto queda sin resolver con cualquiera de las dos varas.

**Qué se mide.** Por estrato y por eje: en qué parte de los pre-ensayos el revisor asigna el mismo primario que la coordenada vigente, con su intervalo de confianza del 95 %. Para todo el corpus: la misma medida, ponderada por el tamaño de cada estrato. En cada eje que la relectura cambió: si el revisor coincide con el valor nuevo, con el que tenía en la versión 1.2 o con ninguno de los dos. Dice si los cambios aplicados mejoraron o empeoraron la categorización. En cada eje que habría cambiado con la vara fijada antes de leer y no cambió: si el revisor coincide con el valor vigente, con el de las lecturas o con ninguno de los dos. Dice si convenía la vara que se aplicó o la que se había fijado.

**Límites.** La revisión mide el acuerdo entre el revisor y la categorización vigente. No prueba que la taxonomía ni sus reglas sean las correctas. Con un solo revisor, que es el autor del banco, la medida no es independiente de las coordenadas que él mismo asignó antes. El horizonte, las fuerzas y el pilar no entran en esta revisión. Los estratos salen de tres lecturas automáticas con la misma configuración: separan los casos en que esas lecturas dudan, no los casos en que se equivocan. La subfunción ID06 es nueva y RC04 cambió de alcance: en esos casos el valor de la versión 1.2 no se puede comparar sin más con el de la 1.4.

## 6. La medición

El catálogo de medición tiene 224 indicadores ubicados en la taxonomía. 8 quedaron sin subfunción en esta versión: su categoría de NIST CSF 2.0 corresponde ahora a dos subfunciones (ID05 e ID06) y la regla que derivaba la subfunción ya no elige. Conservan la función. Cuatro indicadores de mejora continua (K06, K48, K182 y K184) pasaron a ID06 por una adjudicación escrita, que está en `scripts/extraer_medicion.py`.

Las dos reglas para indicadores que el autor adoptó (RP-09.5 y RP-11.2) no se aplicaron todavía al catálogo. Es una lectura que no se hizo (decisión D-17.6).

## 7. Casos de navegación

Casos resueltos con consultas sobre el grafo candidato. Muestran qué devuelve el Atlas para una coordenada y qué no devuelve. No son recomendaciones. Los casos se recalcularon con la categorización de la versión 1.4 y están en `data/casos_de_navegacion.json`.

| Caso | Problema | Coordenada | Pre-ensayos |
|---|---|---|---|
| N1 | Delegar en un agente la contención del correo malicioso | T06 SECURITY OPERATIONS × D15 Incident Response & Crisis Management × RS02 Contención, erradicación y preservación de evidencia | 7 |
| N2 | Aceptar el riesgo de dar más autonomía a un agente | T07 AI & AUTONOMOUS SYSTEMS × D02 Cyber Risk Management × GV04 Apetito, tolerancia y aceptación de riesgo | 6 |
| N3 | Un proveedor crítico sufre un incidente | T04 RISK & RESILIENCE × D17 Third-Party & Supply Chain Security × RS04 Gestión de incidentes con terceros | 2 |
| N4 | Preparar la transición a la criptografía poscuántica | T05 SECURITY ARCHITECTURE × D26 Cryptography, Key Management & Post-Quantum Readiness × PR02 Protección de datos y privacidad por diseño | 5 |
| N5 | Demostrar al directorio que los controles funcionan | T08 TRUST & ASSURANCE × D28 Security Assurance, Testing & Measurement × GV08 Assurance y revisión independiente | 31 |
| N0 | La coordenada del ejemplo de la versión 1.1: delegar en un agente la remediación del correo, leída como T07 × D09 × RS02 | T07 AI & AUTONOMOUS SYSTEMS × D09 Endpoint & Workplace Security × RS02 Contención, erradicación y preservación de evidencia | 0 |

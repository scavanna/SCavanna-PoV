> **Registro de la versión 1.3 (16 de noviembre de 2026).** Este documento se conserva tal como se publicó. Las cifras, los estados y los archivos que cita corresponden a esa versión. El estado vigente está en `docs/15_Decisiones_delegadas_y_relectura_1_4.md` y en los documentos 16 a 19.

# De AI CISO Atlas a Frontier CISO Atlas

**Frontier CISO Atlas 1.3** · Taxonomía 6.0 (reglas de asignación, revisión 2) · Ontología 2.1.0 · GM-24 V7.1 · 16 de noviembre de 2026 · Estado: decisiones de diseño confirmadas por el autor; reglas adoptadas según la lectura del curador y corpus releído a ciegas por lectores automáticos, con una lectura para todos y dos donde la primera difería; contenido candidato, sin validación humana

## 1. Por qué cambia el nombre

El AI CISO Atlas nació para ordenar lo que la inteligencia artificial le cambia al rol del CISO. El nombre terminó atando el mapa a una tecnología. La IA es hoy el principal motor del cambio, pero no es el objeto del Atlas: el objeto es el rol y el territorio en el que ese rol se ejerce.

**Frontier CISO Atlas** nombra otra cosa: un tipo de empresa y un tipo de CISO.

- **La frontera** es el borde donde una práctica deja de estar consolidada. Hoy la mueven la IA y los agentes; mañana puede moverla la criptografía poscuántica, la soberanía digital u otra fuerza. Por eso la frontera no es un territorio del Atlas: es una condición evolutiva de todos los territorios y se expresa con el eje H.
- **La empresa de frontera** trabaja en ese borde y lo incorpora de forma deliberada a su modelo operativo.
- **El CISO de frontera** se para de frente al cambio tecnológico: lo evalúa, decide con evidencia si lo adopta, lo condiciona o lo difiere, y adecua sus modelos mentales, sus capacidades individuales y las de su oficina para convertir el desafío en una oportunidad de crecimiento. Lo define la calidad de la decisión, no su sentido: diferir con fundamento también es propio de la frontera.

El cambio de nombre busca completitud. El Atlas deja de estar asociado en exclusiva a la IA y pasa a cubrir todo el oficio, incluidas disciplinas que la versión anterior no alojaba (arquitectura, criptografía, seguridad física, aseguramiento).

### Referencia externa: la «Frontier Firm» de Microsoft

Microsoft usa «Frontier Firm» desde su Work Trend Index de 2025 para describir empresas organizadas sobre inteligencia a demanda y equipos de personas y agentes. Es un marco estratégico y comercial de un proveedor, no un estándar, y el Atlas lo toma como referencia de contexto, no como definición propia. El nombre del Atlas coincide con ese concepto y con el de una suite del mismo proveedor; el plano A del Atlas se propone agnóstico de proveedor, y hoy no lo es del todo (sección 2). Tres datos de esa fuente son útiles aquí:

- Describe tres fases que no son lineales: personas con asistente, equipos de personas y agentes, y operación dirigida por personas y ejecutada por agentes. El Atlas las adopta como valores del factor de contexto HX08. Fuente: [Work Trend Index 2025](https://www.microsoft.com/en-us/worklab/work-trend-index/2025-the-year-the-frontier-firm-is-born).
- En el estudio de IDC de 2026 que Microsoft cita, 87 % de las empresas de frontera dice tener un proceso para gobernar agentes, frente a 51 % de las rezagadas. La cifra hay que leerla con su origen: el grupo se define como el 10 % superior de una escala de madurez de IA, los datos son declarados por los encuestados y la edición de 2025 fue encargada por el proveedor. Sirve de contexto y no prueba que gobernar agentes produzca el resultado. Fuente: [blog oficial de Microsoft, 12-nov-2026](https://blogs.microsoft.com/blog/2026/11/12/scaling-ai-value-without-losing-control-lessons-from-frontier-firms/).
- El Microsoft Digital Defense Report 2026 afirma que los CISO gestionan hoy ecosistemas y no solo entornos. Fuente: [MDDR 2026](https://www.microsoft.com/en-us/security/security-insider/threat-landscape/2026-digital-defense-report).

El detalle verificado está en `anexos/A4_Verificacion_Microsoft_y_Frontier.md`.

## 2. Los cuatro instrumentos

El CISO de frontera necesita saber dónde está, cómo se mueve el terreno, por dónde ir y cómo decidir. Cada pregunta tiene su instrumento.

| Pregunta | Instrumento | Qué aporta |
|---|---|---|
| ¿Dónde estoy? | **El Atlas** (ejes X, Y y Z) | La coordenada: desde qué responsabilidad miro (territorio), sobre qué disciplina u objeto (dominio) y para lograr qué (función y subfunción) |
| ¿Cómo se mueve el terreno? | **El eje H** | El horizonte de la práctica, las fuerzas que la aceleran y la frenan, el contexto de ejecución y lo que hay que mantener estable mientras cambia |
| ¿Por dónde voy? | **El GM-24 V7.1** | La ruta de formación: 24 unidades y 379 conceptos, con su sub-plan para el dueño de producto-control y gerente de agentes (PO-GAC) |
| ¿Cómo decido? | **El MCCS** | El método del navegante: cómo pienso (MM), qué sostiene mi decisión (OS), cómo la convierto en resultado (DO) y cómo me adapto (NX) |

### El Atlas: X, Y y Z

- **X, territorio** (8): la perspectiva o responsabilidad. No cambia de cantidad.
- **Y, dominio** (28): la disciplina o el objeto. Suma cuatro.
- **Z, función** (6) **y subfunción** (34): lo que se busca lograr. Las funciones son las de NIST CSF 2.0; las subfunciones son editoriales del Atlas.

### El eje H: evolución y homeostasis

H no mide madurez. Describe cómo cambia una práctica y qué la mantiene dentro de límites aceptables mientras cambia. Tiene seis catálogos:

1. **Horizontes** (4): consolidada, en evolución, emergente y convergente. «Indeterminado» es una respuesta válida.
2. **Catalizadores** (11): las fuerzas de aceleración.
3. **Inhibidores** (11): las fuerzas de inhibición.
4. **Mecanismos homeostáticos** (12): lo que la organización hace para no perder el control durante el cambio. No son fuerzas.
5. **Factores de contexto** (8): las condiciones de partida.
6. **Variables homeostáticas** (6): lo que hay que mantener estable.

La homeostasis es la idea central: un organismo sobrevive al cambio porque regula unas pocas variables vitales. La versión 5.3 nombraba los mecanismos pero no decía qué regulan. La 6.0 lo explicita con seis variables: exposición residual frente a la tolerancia que se deriva del apetito, autoridad delegada frente a capacidad de supervisión, ritmo de cambio frente a capacidad de absorción, confianza sostenida por evidencia, carga cognitiva frente a capacidad de decisión y continuidad de los servicios críticos. Es una propuesta de diseño: cada mecanismo regula al menos una variable y 17 de las 22 fuerzas presionan al menos una.

### El GM-24 V7.1: la ruta

El GM-24 es el currículo. La versión 7.1 tiene 379 conceptos, todos con pre-ensayo, mapeados a 17 marcos, y separa dos planos:

- **Plano A, corpus académico**: conceptos y pre-ensayos. Se propone agnóstico de proveedor; hoy 77 de sus 739 pre-ensayos nombran productos de un proveedor o al proveedor, y están marcados para revisión.
- **Plano B, capacidades contratadas**: siete instancias de dominio (productividad, XDR, endpoints, identidades, datos, SIEM y nube) con 180 tareas y 85 agentes.

El Atlas conserva esa separación. Una instancia del plano B se ubica en un dominio del Atlas, pero nunca se usa como evidencia del corpus académico.

### El MCCS: el navegante

El Meta-Cognitive CISO System tiene cuatro pilares. En el Atlas funcionan como **lente**, no como eje: cada pre-ensayo lleva un pilar, y cada pilar tiene territorios donde se ancla. Las anclas son una **hipótesis de diseño**: dicen dónde se espera que viva cada pilar, no dónde está hoy. La última columna muestra qué parte de los pre-ensayos de cada pilar tiene su territorio primario en un ancla primaria.

| Pilar | Qué mira | Ancla primaria | Anclas secundarias | Pre-ensayos | En el ancla primaria |
|---|---|---|---|---|---|
| **MM** Modelos mentales | Cómo se piensa y se decide: metacognición, sesgos, marcos de razonamiento e higiene de decisión. | T01 | T02, T04 | 48 (6 %) | 4 de 48 (8 %) |
| **OS** Sistema operativo | Qué sostiene la calidad de la decisión: a escala individual, energía, atención y resiliencia; a escala de oficina, derechos de decisión, cadencias, datos, agentes y evidencia. | T01, T03 | T02 | 144 (19 %) | 14 de 144 (10 %) |
| **DO** Entrega y operación | Cómo el criterio se convierte en resultados: arquitectura, programas, operación y comunicación ejecutiva. | T05, T06 | T03, T08 | 487 (66 %) | 155 de 487 (32 %) |
| **NX** Evolución | Cómo se adapta el sistema: exploración, adopción de IA y agentes, antifragilidad y legado. | T07 | T03 | 60 (8 %) | 9 de 60 (15 %) |

**La Biblioteca cognitiva es el acervo cognitivo del MCCS.** Tus 1.404 conceptos (modelos mentales, sesgos, falacias, prácticas de decisión, capacidades y mentalidades) están en el grafo candidato con tipos propios del módulo de cognición. 59 llevan el pilar OS (las funciones ejecutivas y los factores humanos que son estados o condiciones de la decisión) y los demás, el pilar MM.

**El pilar OS se lee en dos escalas.** En tus notas el pilar OS aparece con dos sentidos: el sustrato personal del líder (energía, atención, resiliencia) y el sistema operativo de la oficina (derechos de decisión, cadencias, datos, agentes y evidencia). Los traté como dos escalas del mismo pilar, la individual anclada en T01 y la de oficina en T03, y aceptaste esa lectura (decisión D-04). Queda un límite: la escala de cada pre-ensayo no está clasificada. Desde la versión 1.3 hay un registro de trabajo para los del pilar OS, tomado de la relectura (`data/escala_del_pilar_OS_1_3.csv`), que no es una clasificación revisada (encargo RP-14.2).

## 3. Cómo se navega

1. **Ubicar.** Fijar la coordenada del problema: territorio, dominio y subfunción. La tesis manda: se ubica por el objeto de la decisión, no por las palabras que aparecen.
2. **Leer el terreno.** Mirar el horizonte, las fuerzas que empujan y frenan, los mecanismos que mantienen el control y la variable homeostática en juego.
3. **Elegir la ruta.** Tomar los pre-ensayos de esa coordenada, las preguntas que cubren y, si existen, las instancias del plano B.
4. **Decidir con método.** Pasar la decisión por los cuatro pilares del MCCS.
5. **Registrar y aprender.** Dejar constancia de la decisión y revisar sus supuestos.

### Un caso resuelto con el grafo

Los casos que siguen no están escritos a mano: salen de consultas sobre el grafo candidato (`scripts/casos_de_navegacion.py`; resultado completo en `data/casos_de_navegacion.json`). Muestran lo que el Atlas devuelve y lo que no devuelve.

**Delegar en un agente la contención del correo malicioso.**

- *Ubicar.* T06 × D15 × RS02: T06 SECURITY OPERATIONS, D15 Incident Response & Crisis Management y RS02 Contención, erradicación y preservación de evidencia. El objeto de la decisión es la respuesta al incidente; el agente es el medio. Por eso la coordenada es de operaciones y respuesta, y la autonomía aparece como mecanismo (HOM12), no como territorio.
- *Leer el terreno.* Los 8 pre-ensayos de la coordenada se reparten entre H02 (5) y H01 (3). Los mecanismos que más nombran son HOM05 Respuesta a incidentes (5), HOM07 Rollback y recuperación (3) y HOM12 Gobierno de la autonomía (niveles, aprobación humana e interruptor probado) (3); la única fuerza que nombran es CAT01 Innovación tecnológica, INH02 Presupuesto e INH09 Limitaciones operativas. El gobierno de la autonomía (HOM12) regula HV02 Autoridad delegada frente a capacidad de supervisión, que es la variable en juego cuando se delega en un agente. Sus indicadores candidatos son, entre otros, K167 «Agentes con detención de emergencia probada», K50 «Agentes con dueño humano y autoridad delegada acotada», K88 «Tipos de acción de agentes con nivel de autonomía aprobado» y K98 «Decisiones automatizadas de alto impacto con supervisión humana verificada».
- *Elegir la ruta.* Pre-ensayos: AMP-45 «Forense de agentes» (confianza del clasificador: alta); APC-066 «Límite entre contención automatizada y aprobación humana» (confianza del clasificador: alta); APC-161 «Presupuesto de tiempo de contención de agentes comprometidos» (coordenada cambiada por la relectura: la confianza del clasificador no vale); APS-02 «Cadena de custodia en investigaciones asistidas por IA» (coordenada cambiada por la relectura: la confianza del clasificador no vale); M5.2-K01 «Contención» (confianza del clasificador: alta); M5.2-K02 «Erradicación» (confianza del clasificador: alta); M5.2-K06 «Forense Digital» (confianza del clasificador: alta); M5.2-PA01 «Ejecución de respuesta en correo: AIR, acciones manuales y acciones de agentes con aprobación» (confianza del clasificador: alta). Cubren 6 preguntas de la matriz. Sus conceptos están instanciados en los productos-control de endpoints, productividad y XDR del plano B, donde el grafo dice qué agentes ejecutan qué tareas, con qué nivel de autonomía y bajo qué punto de control. En la misma subfunción y el mismo dominio hay 4 indicadores: K178, K179, K190 y K45.
- *Decidir con método.* El grafo no devuelve qué sesgo puede estar operando ni qué práctica lo contrarresta para esta coordenada: la Biblioteca cognitiva no está vinculada con el corpus. Ese paso lo hace hoy el CISO con su criterio. Los pre-ensayos de la coordenada llevan el pilar DO (7) y OS (1).
- *Registrar.* La decisión queda escrita, con sus supuestos y la fecha de revisión.

**Lo que este caso enseña.** La versión 1.1 ubicaba el mismo problema en T07 × D09 × RS02, porque interviene un agente y el objeto es el correo. Esa coordenada es válida y el corpus no tiene nada en ella: el Atlas devuelve un silencio. El corpus trata el caso como respuesta a incidentes, con la autonomía del agente como mecanismo. Las dos lecturas son defendibles, y la diferencia entre ellas es la que resuelve la regla RP-01, adoptada el 16 de noviembre de 2026.

### Otros cuatro casos y un silencio

| Problema | Coordenada | Pre-ensayos | Cuáles | Fuerzas y mecanismos más nombrados | Preguntas que cubren | Indicadores con el mismo dominio y la misma subfunción |
|---|---|---|---|---|---|---|
| Aceptar el riesgo de dar más autonomía a un agente | T07 × D02 × GV04 | 3 | AMP-17, AMP-22 y G4.2-PA01 | HOM01 (3), HOM12 (3) e INH07 (1) | 7 | 9 |
| Un proveedor crítico sufre un incidente | T04 × D17 × RS04 | 1 | APC-063 | HOM05 (1), HOM06 (1) e INH06 (1) | 1 | 2 |
| Preparar la transición a la criptografía poscuántica | T05 × D26 × PR02 | 1 | APC-042 | CAT01 (1), HOM03 (1) e INH09 (1) | 1 | 1 |
| Demostrar al directorio que los controles funcionan | T08 × D28 × GV08 | 33 | AMP-13, AMP-14, APA-014 y otros | HOM09 (33), HOM03 (8) y CAT01 (7) | 26 | 4 |
| La coordenada del ejemplo de la versión 1.1: delegar en un agente la remediación del correo, leída como T07 × D09 × RS02 | T07 × D09 × RS02 | 0 | ninguno: silencio | — | 0 | 0 |

En los cinco casos el paso «leer el terreno» devuelve varias variables homeostáticas a la vez, porque cada mecanismo regula más de una: el modelo de referencia orienta, no discrimina. Y en ninguno el grafo devuelve una respuesta sobre la organización del lector: para eso hacen falta sus activos, sus escenarios y su evidencia.

## 4. Qué se conserva y qué cambia

**Se conserva** la arquitectura del AI CISO Atlas: los ensayos en Markdown como fuente de verdad, los catálogos en JSON, el grafo de propiedades en SQLite, los conjuntos de cambios con aprobación humana, las reglas semánticas deterministas y las decisiones de arquitectura ADR-001 a ADR-012. También se conservan todos los códigos: ninguno se renumera ni se reutiliza.

**Cambia** lo siguiente:

| Elemento | AI CISO Atlas | Frontier CISO Atlas 1.3 |
|---|---|---|
| Taxonomía | 5.3: 8 territorios, 24 dominios, 6 funciones, 32 subfunciones | 6.0: 8 territorios, 28 dominios, 6 funciones, 34 subfunciones; reglas de asignación revisión 2, con 60 enunciados adoptados y 11 preguntas abiertas |
| Eje H | 4 horizontes; 10 catalizadores, 10 inhibidores, 10 mecanismos homeostáticos; 7 factores de contexto | 4 horizontes; 11 catalizadores, 11 inhibidores, 12 mecanismos; 8 factores de contexto; 6 variables homeostáticas |
| Lentes | No tenía | Pilar MCCS (MM, OS, DO, NX), plano (A académico, B capacidades contratadas) y pilar de la agenda de IA |
| Ontología | 1.0.0: 8 módulos, 57 tipos de entidad, 58 relaciones, 21 reglas | 2.1.0: 10 módulos y un grupo transversal, 84 tipos de entidad, 93 relaciones, 37 reglas |
| Base de referencia | 17 marcos del mapeo del GM-24 | 146 artefactos de 42 organismos, con versión, fecha y estado de verificación al 15-nov-2026: 99 verificados, 37 en parte, 8 internos y 2 sin verificar |
| Corpus | 691 pre-ensayos en el banco del Atlas | 739 pre-ensayos: los 379 del GM-24 V7.1 y 360 ampliaciones del Atlas; más 16 de la serie APX como capa de ampliación. Releídos a ciegas con las reglas adoptadas: 204 cambiaron en algún eje |
| Grafo | Diseñado, sin carga | Grafo candidato: 5.058 nodos y 28.249 relaciones en 16 conjuntos de cambios propuestos; 0 errores con 19 de las 37 reglas comprobadas |
| Conocimiento cognitivo | Fuera del Atlas | 1.404 conceptos de la Biblioteca cognitiva en el grafo candidato, con tipos propios; sin vínculo todavía con el corpus |
| Medición | Catálogo 1.2: 70 indicadores (64 y seis del sistema de gestión), sin vínculo con el eje H | Catálogo 2.0: 224 indicadores con coordenada, 71 vínculos propuestos con las seis variables homeostáticas, 24 objetivos y 72 resultados clave |
| Revisión | Sin revisión independiente | 13 revisores automáticos, de contexto independiente, dejaron 364 hallazgos, todos con decisión escrita; tres verificaciones externas revisaron 44 puntos más; cuatro revisores leyeron la versión corregida antes de publicarla. En la 1.3, dos lecturas automáticas a ciegas del corpus y una revisión de la versión candidata |
| Agente curador | Instrucciones 6.0 | Instrucciones 7.3 |

## 5. Lo que el Frontier CISO Atlas no es

- **No es un modelo de madurez.** H describe evolución y equilibrio, no niveles.
- **No es una matriz de conformidad.** Un cruce entre un concepto y un elemento de un marco indica afinidad, con fuerza, versión y método declarados; no afirma cumplimiento. En el mapeo heredado del GM-24, «fuerte» y «cubre» son valores generados en su mayor parte por herencia de la unidad y regla por palabra clave.
- **No es un catálogo de productos.** Los productos corresponden al plano B. En el plano A quedan 77 pre-ensayos que nombran productos y están marcados para revisión.
- **No es todavía un grafo aprobado.** Es un grafo candidato construido sobre pre-ensayos.
- **No es una fuente validada.** Ningún elemento tiene revisión humana. Es una guía para un profesional que la contrasta con su criterio.

## 6. Versiones

| Componente | Versión | Estado |
|---|---|---|
| Frontier CISO Atlas | 1.3 (continúa la 1.2) | Decisiones de diseño confirmadas el 16-nov-2026; contenido candidato |
| Taxonomía | 6.0, reglas de asignación revisión 2 (sucede a la 5.3) | Confirmada; 60 enunciados adoptados y 11 preguntas abiertas |
| Frontier CISO Atlas Core Ontology | 2.1.0 (sucede a la 1.0.0 y contiene a la 2.0.0 del paquete 1.0) | Confirmada como línea base; solicitud de cambio OCR-CAND-03 pendiente |
| Instrucciones del agente curador | 7.3 (suceden a las 7.2) | Vigentes; lo que cambia respecto de las 7.2 lo redactó el curador |
| TheNextCISO GM-24 | V7.1 | Vigente, sin cambios |

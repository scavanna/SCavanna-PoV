# Taxonomía 6.1 del Frontier CISO Atlas

**Frontier CISO Atlas 1.4** · Taxonomía 6.1 (reglas de asignación, revisión 3) · Ontología 2.2.0 (propuesta) · GM-24 V7.1 · 16 de noviembre de 2026 · Estado: respuestas del autor registradas de forma literal; lo que decidió el curador en esta versión espera su confirmación (D-16); corpus releído por lectores automáticos con una vara de tres lecturas, que el curador endureció después de leer; contenido candidato, sin validación humana

Este documento describe la Taxonomía 6.1 completa: el catálogo, las reglas de asignación, los vacíos declarados, el modelo del eje H, los criterios de admisión de dominios y las lentes. Reemplaza, como descripción vigente, a `docs/03_Taxonomia_6_0.md`, que se conserva como registro de la versión 1.3.

**Quién decidió qué.** La Taxonomía 6.0 la confirmó el autor (decisiones D-14 y D-15). La 6.1 es la 6.0 con lo que decidió el curador en esta versión. No todo tiene el mismo origen: las reglas RD-01 a RD-14 y RD-20 a RD-24 y el cambio de ID06 y RC04 salen de la línea que el autor respondió con «Procede con la decision de mayor rigurosidad», que el curador leyó como delegación; H04, INH11, el modelo del eje H, los criterios de admisión, el plano y las familias salen de los encargos que el autor aprobó con «Si, confirmo, procede», y el resultado es del curador; y las reglas RD-15 a RD-19 y la revisión 2 de las definiciones de trabajo las decidió el curador por su cuenta. Todo tiene criterio y justificación escritos, no figura como palabra del autor y él puede confirmarlo, corregirlo o revertirlo (decisión D-16).

**Cómo leerla.** El autor lo escribió así: estos niveles de abstracción funcionan como guías y orientación; un CISO tiene que leer todo con atención, no creer nada por defecto y, contrastando con su conocimiento y su formación, ir aceptando los distintos elementos, con la responsabilidad final indelegable.

## 1. Qué cambia de la 6.0 a la 6.1

| Elemento | 5.3 | 6.0 | 6.1 |
|---|---|---|---|
| territorios | 8 | 8 | 8 |
| dominios | 24 | 28 | 28 |
| funciones | 6 | 6 | 6 |
| subfunciones | 32 | 34 | 35 |
| horizontes | 4 | 4 | 3 |
| catalizadores | 10 | 11 | 11 |
| inhibidores | 10 | 11 | 11 |
| homeostaticos | 10 | 12 | 12 |
| factores de contexto | 7 | 8 | 8 |
| variables homeostaticas | 0 | 6 | 6 |
| marcador de convergencia | 0 | 0 | 1 |

Cuatro cambios de catálogo. Ninguno retira ni reutiliza un código:

| Eje | Código | Cambio | Qué dice | Regla |
|---|---|---|---|---|
| Z-subfunción | ID06 | nuevo | Mejora continua y lecciones aprendidas (ID.IM-03 e ID.IM-04). | RD-03 |
| Z-subfunción | RC04 | nombre y alcance | De «Aprendizaje, corrección y mejora continua» a «Lecciones y cierre de la recuperación» (RC.RP-06). | RD-03 |
| H | H04 | cambia de eje | Deja de ser un horizonte y pasa a ser el marcador de convergencia. | RP-15.6 |
| H-inhibidor | INH11 | nombre y definición | De «Carga cognitiva y fatiga de decisión» a «Volumen de alertas y de decisiones». | RP-15.2 |

**Lo que no cambia.** 8 territorios, 28 dominios, 6 funciones, 11 catalizadores, 11 inhibidores, 12 mecanismos, 8 factores de contexto y 6 variables. Ningún código se retira ni se reutiliza.

**Lo que solo se propone.** Admitir el candidato W02 como dominio D29 «Gestión de activos, configuración y cambios»: no se aplica. Es un cambio de catálogo que no se le planteó al autor con esa opción (criterio e). Admitir las variables HV07 y HV08: no se aplica. Es un cambio de catálogo que decide el autor. Las dos quedan para el autor en la decisión D-17.

**Sobre la regla de gobierno.** La taxonomía dice que todo cambio de catálogo exige una decisión de arquitectura, un conjunto de cambios propuesto y aprobación humana. Los cuatro cambios tienen su decisión de arquitectura (ADR-034) y las cuatro opciones se le habían planteado al autor en la versión 1.3. Ninguno de los cuatro tiene todavía aprobación humana. Dos (ID06 y RC04) salen de una frase que el curador leyó como delegación, y dos (H04 e INH11), de los encargos que el autor aprobó sin ver su resultado. Están aplicados de forma provisoria y quedan para confirmar, uno por uno, en D-16.3 y D-16.4. Si el autor no los confirma, se revierten.

## 2. El catálogo

### 2.1 Territorios (eje X)

| Código | Nombre | Alcance |
|---|---|---|
| T01 | SELF & JUDGMENT | Criterio individual, metacognición, sesgos y decisiones. |
| T02 | LEADERSHIP & ORGANIZATION | Personas, incentivos, roles, cultura, liderazgo y accountability. |
| T03 | STRATEGY & BUSINESS | Outcomes, estrategia, inversión y priorización empresarial. |
| T04 | RISK & RESILIENCE | Exposición, escenarios, apetito, continuidad y riesgo de transición. |
| T05 | SECURITY ARCHITECTURE | Diseño de controles, Zero Trust, ingeniería y fronteras técnicas. |
| T06 | SECURITY OPERATIONS | SOC, monitoreo, investigación, respuesta y operación. |
| T07 | AI & AUTONOMOUS SYSTEMS | Modelos, agentes, autonomía, herramientas y autoridad no humana. |
| T08 | TRUST & ASSURANCE | Evidencia, auditoría, legitimidad, confiabilidad y transparencia. |

### 2.2 Dominios (eje Y)

Los 28 dominios, agrupados en 5 familias. La familia es una ayuda de navegación: agrupa los dominios por el tipo de objeto que nombra su definición. Ninguna regla de asignación la usa y no forma parte de la coordenada.

**Gobierno.** El objeto del dominio es dirigir el programa y dar cuenta de él: decidir, priorizar, cumplir, financiar y demostrar.

| Código | Nombre | Definición | Estado |
|---|---|---|---|
| D01 | Cybersecurity Governance | Políticas, dirección, responsabilidades y supervisión. | vigente |
| D02 | Cyber Risk Management | Identificación, evaluación, tratamiento y aceptación del riesgo. | vigente |
| D03 | Compliance & Regulatory Security | Obligaciones aplicables y su conformidad, incluida la auditoría de conformidad con una obligación. | ajustado |
| D04 | Security Program & Investment Management | Portafolio, presupuesto, prioridades y valor. | vigente |
| D28 | Security Assurance, Testing & Measurement | Evaluación de controles, pruebas técnicas (pruebas de penetración, equipos rojo y púrpura, validación continua), auditoría y atestaciones, métricas, indicadores y evidencia de eficacia. | nuevo |

**Protección.** El objeto es una clase de activo o una capa que se salvaguarda, o el diseño de esas salvaguardas.

| Código | Nombre | Definición | Estado |
|---|---|---|---|
| D05 | Identity & Access Security | Identidades humanas/no humanas, autenticación, autorización y PAM. | vigente |
| D06 | Data Security & Information Protection | Clasificación, DLP, cifrado y protección de información. | ajustado |
| D07 | Privacy & Data Protection Engineering | Finalidad legítima, minimización, derechos y tratamiento de datos personales. | vigente |
| D08 | Network & Infrastructure Security | Redes, segmentación y componentes de infraestructura. | vigente |
| D09 | Endpoint & Workplace Security | Endpoints, dispositivos de usuario y puesto de trabajo. | ajustado |
| D10 | Cloud & Platform Security | Cloud, servicios de plataforma, workloads y configuraciones. | vigente |
| D11 | Application & Software Security | Aplicaciones, SDLC, DevSecOps y seguridad de código. | vigente |
| D25 | Enterprise Security Architecture & Zero Trust | Arquitectura empresarial de seguridad, principios y modelos de referencia, estrategia Zero Trust, seguro por diseño y por defecto, e ingeniería de resiliencia. | nuevo |
| D26 | Cryptography, Key Management & Post-Quantum Readiness | Inventario criptográfico, PKI y certificados, gestión de claves y secretos, agilidad criptográfica y transición poscuántica. | nuevo |
| D27 | Physical, Environmental & Facility Security | Seguridad física de instalaciones y centros de datos, protección ambiental, mantenimiento y soportes, y su evidencia como dependencia del control (incluida la del proveedor de nube). | nuevo |

**Operaciones.** El objeto es el ciclo continuo frente al adversario y al incidente: conocer la amenaza, reducir la exposición, detectar, responder y recuperar.

| Código | Nombre | Definición | Estado |
|---|---|---|---|
| D12 | Threat Intelligence & Threat Modeling | Adversarios, TTP, escenarios y modelado de amenazas. | vigente |
| D13 | Vulnerability & Exposure Management | Descubrimiento, evaluación y reducción de exposición. | ajustado |
| D14 | Security Monitoring & Detection | Telemetría, reglas, analítica, detección y hunting. | vigente |
| D15 | Incident Response & Crisis Management | Investigación, contención, erradicación y coordinación de crisis. | vigente |
| D16 | Business Continuity & Cyber Recovery | Continuidad, restauración y recuperación comprobada. | vigente |

**Ecosistemas.** El objeto es un entorno con reglas propias que la organización no controla del todo o que extiende su perímetro: terceros, tecnología operativa, dispositivos conectados e IA, como objeto protegido y como instrumento.

| Código | Nombre | Definición | Estado |
|---|---|---|---|
| D17 | Third-Party & Supply Chain Security | Proveedores, dependencias y cadena de suministro. | ajustado |
| D18 | Operational Technology & Industrial Control Security | ICS/SCADA/PLC, procesos industriales, safety y continuidad OT. | vigente |
| D19 | IoT & Cyber-Physical Systems Security | Dispositivos conectados y sistemas ciberfísicos no exclusivamente industriales. | vigente |
| D20 | AI & Agent Security | Proteger modelos, agentes, herramientas, datos y runtime de IA. | vigente |
| D21 | AI for Cyber Defense & Security Operations | IA para detectar, investigar, priorizar y responder. | vigente |
| D22 | AI for Security Assessment & Testing | IA para pruebas autorizadas, evaluación y descubrimiento de debilidades. | vigente |
| D23 | AI for Security Engineering & Automation | IA para crear reglas, políticas, configuraciones y automatizaciones. | vigente |

**Personas.** El objeto son las personas que hacen y sostienen la seguridad.

| Código | Nombre | Definición | Estado |
|---|---|---|---|
| D24 | Security Workforce & Human Factors | Profesión, talento, cultura, sesgos y capacidades humanas. | ajustado |

### 2.3 Funciones y subfunciones (eje Z)

Las seis funciones son las de NIST CSF 2.0. Las 35 subfunciones son editoriales del Atlas: cada una declara la categoría de NIST CSF 2.0 que le sirve de ancla, y no son categorías oficiales de NIST.

| Código | Función | Nombre | Ancla en CSF 2.0 | Estado | Incluye | Excluye | Frontera fijada por |
|---|---|---|---|---|---|---|---|
| GV01 | GV | Contexto empresarial y estrategia | GV.OC | vigente | El contexto del negocio (misión, objetivos, partes interesadas) y la estrategia de seguridad que se deriva de él. | Las obligaciones legales y contractuales (GV06) y la criticidad y las dependencias del negocio (ID02). | — |
| GV02 | GV | Estructura de gobierno y autoridad | GV.RR | vigente | La estructura de gobierno: roles, responsabilidades, autoridad y derechos de decisión, incluido el diseño de roles del equipo de seguridad; para los agentes, quién supervisa o aprueba y con qué autoridad. | Las sesiones de órganos con acta y decisiones (GV07), la gestión del programa y de sus recursos, incluida la dotación (GV05), la norma que fija los niveles de autonomía (GV03) y la cultura y la conducta de quien lidera (GV10). | RD-08 y RD-17 |
| GV03 | GV | Políticas y estándares | GV.PO | vigente | Las políticas, los estándares, las normas internas y los procedimientos como norma general: su aprobación, comunicación, revisión y actualización; el catálogo de controles que la organización adopta y los marcos de referencia de los que sale; para los agentes, la política que fija los niveles de autonomía y la exigencia del interruptor. | Las obligaciones externas (GV06), el procedimiento propio de una función operativa (RS01, RC01, RC02) y la preparación de quienes lo ejecutan (PR05). | RD-05, RD-11 y RD-17 |
| GV04 | GV | Apetito, tolerancia y aceptación de riesgo | GV.RM | vigente | La estrategia de gestión del riesgo: apetito, tolerancia, dirección sobre las opciones de respuesta y aceptación del riesgo por quien tiene la autoridad. | La identificación de amenazas y exposición (ID03) y el análisis del riesgo con la elección, la planificación y el seguimiento de su respuesta (ID04). | RD-06 |
| GV05 | GV | Gobierno de programas, recursos e inversión | GV.RR · GV.OV | vigente | El gobierno del programa de seguridad: portafolio, recursos, dotación, presupuesto e inversión, las cadencias de gestión del programa, y la contratación, la retención y las prácticas de recursos humanos del equipo. | Las sesiones de órganos con acta y decisiones (GV07). | RD-08 |
| GV06 | GV | Obligaciones legales y contractuales | GV.OC | vigente | La identificación y la gestión de las obligaciones legales, regulatorias y contractuales. | El contexto del negocio y la estrategia (GV01) y las notificaciones obligatorias de un incidente (RS03). | — |
| GV07 | GV | Supervisión y reporting ejecutivo | GV.OV | vigente | La supervisión por la dirección y por los órganos de gobierno: sesiones con acta y decisiones, informes ejecutivos y revisión del desempeño de la estrategia. | Las cadencias de gestión del programa (GV05) y la revisión independiente (GV08). | — |
| GV08 | GV | Assurance y revisión independiente | GV.OV | vigente | El aseguramiento y la revisión que hace quien no depende de la función evaluada ni es dirigido por ella: auditoría interna y externa y atestaciones. | El informe ejecutivo de gestión (GV07), la prueba o la medición que hace o encarga la propia función (ID05) y la evaluación de un proveedor (GV09). | RD-04 |
| GV09 | GV | Gobierno de terceros y ecosistemas | GV.SC | vigente | El gobierno de proveedores, terceros y ecosistemas: estrategia, requisitos, contratos, evaluación y supervisión de la cadena de suministro. | La coordinación de un incidente con terceros (RS04). | RD-04 |
| GV10 | GV | Ética, cultura y rendición de cuentas | GV.RR · GV.OC | vigente | La ética, la cultura de seguridad y la rendición de cuentas; el liderazgo que las forma y la conducta de quien lidera al decidir. | La estructura formal de roles y autoridad (GV02) y la formación de las personas (PR05). | RD-08 |
| ID01 | ID | Inventario y clasificación de activos | ID.AM | vigente | El inventario, la clasificación y la propiedad de los activos: equipos, software, datos, servicios, identidades y sistemas de IA. | La criticidad y las dependencias del negocio (ID02) y quién tiene qué acceso (PR01). | — |
| ID02 | ID | Dependencias y criticidad del negocio | ID.AM · GV.OC | vigente | Las dependencias, la criticidad y el impacto en el negocio de los activos y los servicios. | El inventario (ID01) y el análisis de escenarios de riesgo (ID04). | — |
| ID03 | ID | Amenazas, vulnerabilidades y exposición | ID.RA | vigente | La identificación de amenazas, vulnerabilidades y exposición técnica; el escenario de amenaza, con el adversario y sus técnicas. | El análisis y la cuantificación del riesgo (ID04). | — |
| ID04 | ID | Análisis de escenarios y cuantificación de riesgos | ID.RA | vigente | El análisis y la cuantificación del riesgo, el escenario de riesgo con la pérdida y su probabilidad, y la elección, la priorización, la planificación, el seguimiento y la comunicación de la respuesta al riesgo; la evaluación, el registro y el seguimiento de las excepciones. | La identificación de amenazas y exposición (ID03), el apetito, la tolerancia y la aceptación del riesgo (GV04) y el plan de acción sobre hallazgos (ID06). | RD-06 y RD-03 |
| ID05 | ID | Evaluación de capacidades y brechas | ID.IM | vigente | La evaluación de capacidades, de madurez y de brechas, y la prueba o la medición de eficacia que hace o encarga la propia función: evaluaciones, pruebas y ejercicios como instrumento para saber dónde se está. | La revisión independiente (GV08), la prueba y la medición de la detección (DE03, DE04), la prueba de los respaldos (PR02), la validación de la recuperación (RC03) y la conversión de lo aprendido en cambios (ID06). | RD-03 y RD-04 |
| ID06 | ID | Mejora continua y lecciones aprendidas | ID.IM | nuevo en 6.1 | La mejora que sale de la operación, de los incidentes y de los ejercicios: lecciones aprendidas, el plan de acción sobre hallazgos, las acciones correctivas y su seguimiento hasta el cierre, y el mantenimiento y la mejora de los planes. | La evaluación que mide la brecha (ID05), el plan de tratamiento que sale de un análisis de riesgo (ID04) y el cierre de una recuperación concreta (RC04). | RD-03 |
| PR01 | PR | Identidad y autorización | PR.AA | vigente | La gestión de identidades, la autenticación, la autorización y el control de acceso de personas, cargas de trabajo y agentes, incluida la revisión de accesos y de privilegios. | El acceso físico a las instalaciones (PR06). | — |
| PR02 | PR | Protección de datos y privacidad por diseño | PR.DS | vigente | La protección de los datos en reposo, en tránsito y en uso, la privacidad por diseño y los respaldos como medida previa: crearlos, protegerlos, mantenerlos y probarlos. | El control de acceso (PR01) y el uso de los respaldos para restaurar (RC01). | RD-07 |
| PR03 | PR | Hardening y arquitectura segura | PR.PS · PR.IR | vigente | La arquitectura segura, el hardening y la segmentación (PR.PS y PR.IR-01). | La resiliencia de la infraestructura y la protección física y ambiental (PR06) y el desarrollo seguro y la gestión de cambios (PR04). | — |
| PR04 | PR | Desarrollo seguro y gestión de cambios | PR.PS | vigente | El desarrollo seguro de software y la gestión de cambios y de configuración a lo largo del ciclo de vida. | El hardening y la arquitectura (PR03). | — |
| PR05 | PR | Preparación de personas y procedimientos | PR.AT | vigente | La concientización, la formación y el desarrollo de competencias, y la preparación de quienes ejecutan: práctica e instrucciones de trabajo en el punto de uso. | La cultura y la rendición de cuentas (GV10) y el procedimiento como norma (GV03). | RD-05 y RD-08 |
| PR06 | PR | Resiliencia de la infraestructura y protección física y ambiental | PR.IR | nuevo | La resiliencia de la infraestructura y la protección física y ambiental: las medidas previas al evento (PR.IR-02 a PR.IR-04, con PR.AA-06, DE.CM-02 y PR.PS-03 como referencias de subcategoría). | La operación degradada durante el incidente (RC02) y la segmentación (PR03). | — |
| DE01 | DE | Telemetría y observabilidad | DE.CM | vigente | La telemetría, el monitoreo continuo y la observabilidad de redes, sistemas, personas, proveedores y agentes. | La construcción y la operación de las detecciones (DE02). | — |
| DE02 | DE | Ingeniería de detección y análisis | DE.AE | vigente | Construir y operar la detección: reglas, analítica, correlación y análisis de eventos adversos. | Ponerla a prueba y buscar lo que no detecta (DE03) y medir su cobertura y su calidad (DE04). | — |
| DE03 | DE | Hunting, validación y mejora de detecciones | DE.AE · DE.CM | vigente | Poner a prueba la detección y buscar lo que no detecta: hunting, validación y mejora de las detecciones. | Construirla y operarla (DE02) y medir su cobertura y su calidad (DE04). | — |
| DE04 | DE | Evaluación de cobertura y calidad de detección | DE.AE · ID.IM | vigente | Medir la cobertura y la calidad de la detección. | La evaluación general de capacidades (ID05). | — |
| RS01 | RS | Preparación y coordinación de respuesta | RS.MA | vigente | La preparación y la coordinación de la respuesta: plan, roles, triaje y priorización de incidentes. | La contención y la erradicación (RS02) y la comunicación de crisis (RS03). | — |
| RS02 | RS | Contención, erradicación y preservación de evidencia | RS.MI · RS.AN | vigente | El análisis del incidente, la contención, la erradicación y la preservación de la evidencia. | El triaje y la priorización (RS01). | — |
| RS03 | RS | Comunicación de crisis y decisiones ejecutivas | RS.CO | vigente | La comunicación de crisis, las decisiones ejecutivas durante el incidente y las notificaciones obligatorias. | La coordinación con terceros y las notificaciones contractuales (RS04) y la comunicación de la recuperación (RC05). | — |
| RS04 | RS | Gestión de incidentes con terceros | RS.CO · GV.SC | vigente | La coordinación del incidente con terceros, incluidas las notificaciones contractuales. | El gobierno de terceros fuera del incidente (GV09). | — |
| RC01 | RC | Restauración y recuperación técnica | RC.RP | vigente | La capacidad técnica de restaurar, con sus objetivos de tiempo y de punto de recuperación, incluido el uso de los respaldos para restaurar. | La continuidad durante la perturbación (RC02), la validación del retorno (RC03) y los respaldos como medida previa (PR02). | RD-07 |
| RC02 | RC | Continuidad y operación degradada | RC.RP | vigente | La continuidad del negocio y la operación degradada durante la perturbación. | Las medidas de resiliencia previas al evento (PR06) y la restauración técnica (RC01). | — |
| RC03 | RC | Validación de recuperación y retorno seguro | RC.RP | vigente | La validación de la recuperación y del retorno seguro a la operación. | La restauración (RC01). | — |
| RC04 | RC | Lecciones y cierre de la recuperación | RC.RP | ajustado en 6.1 | El cierre de la recuperación: declarar su fin con criterios, completar la documentación del incidente y registrar las lecciones de esa recuperación. | La mejora continua y la conversión de lo aprendido en cambios del programa, de los planes o de los controles (ID06). | RD-03 |
| RC05 | RC | Comunicación de la recuperación y restitución de la confianza | RC.CO | nuevo | La comunicación de la recuperación a las partes interesadas y la restitución de la confianza. | La comunicación durante la crisis (RS03). | — |

Las definiciones de trabajo están en `data/subfunciones_definiciones_rev2.csv`. Las de la versión 1.3, que el autor confirmó en D-15.7, se conservan en cada subfunción del catálogo (`definicion_de_trabajo_1_3`).

## 3. Reglas de asignación, revisión 3

### 3.1 El criterio de mayor rigor

El autor respondió tres líneas con una misma frase, que alcanzan cuatro asuntos, y no definió qué es «mayor rigurosidad». El curador escribió un criterio antes de decidir, en este orden de precedencia:

|  | Criterio | Qué dice |
|---|---|---|
| a | Fidelidad a la fuente | Entre dos opciones, la que sigue el texto de la fuente normativa que el eje declara como ancla (para las subfunciones, las categorías y subcategorías de NIST CSF 2.0; para el MCCS, la biblioteca del autor). |
| b | Coherencia con lo ya decidido | No contradice una regla adoptada ni una decisión que el autor confirmó. Si dos reglas adoptadas chocan, prevalece la más específica y se escribe cuándo rige cada una. |
| c | Una regla, todos los casos | El mismo criterio se aplica igual a todos los casos, a los admitidos y a los candidatos. |
| d | Prueba que puede fallar | La regla trae una prueba que dos lectores pueden aplicar por separado y que puede dar negativo. |
| e | Parsimonia | No se agrega un elemento al catálogo si uno vigente expresa el objeto sin perderlo; un cambio de catálogo solo se aplica si la pregunta se le había planteado al autor con esa opción. |
| f | Si nada decide, no cambia | Cuando los criterios anteriores no alcanzan, el punto queda declarado como vacío, con un código, y ningún cambio que dependa de él se aplica. |

Es una lectura del curador de lo que significa «mayor rigurosidad» (D-16.1).

### 3.2 Las reglas decididas

Son 24. Las primeras 19 las recibieron los lectores de la relectura; las demás no son reglas de lectura. El texto completo, con su justificación, está en `data/reglas_de_asignacion_rev3.csv`, que trae dos columnas vacías para que el autor anote su decisión regla por regla.

| Código | Eje | De dónde sale | Qué decide | Criterios | Ejes que cambiaron citándola |
|---|---|---|---|---|---|
| RD-01 | territorio y dominio | RV-4, RP-10.1, RP-04.2, RP-04.6, RP-09.2 | Cuando el texto trata de IA se decide, en este orden, qué papel tiene la IA en la tesis. (a) Objeto, sin prueba. La IA es el objeto en cuatro casos: cuando lo que la tesis gobierna, autoriza, somete a una obligación o cuyo riesgo trata es un sistema de IA o su uso (R7, RP-04.1); cuando fija la autonomía o la autoridad de un agente, es decir, qué puede hacer solo y qué aprueba una persona (RP-09.2); cuando es la regla de uso de herramientas de IA por los empleados: qué herramientas se pueden usar, para qué y con qué datos (RP-04.6); y cuando trata un control técnico que solo existe por la naturaleza de la IA (RD-19). El territorio es T07, con dos salvedades, que son las únicas y que precisan la «otra perspectiva» de RP-04.2: T02 cuando la tesis trata a las personas que supervisan agentes o trabajan con ellos (su rol, su carga, su competencia) y da por fijada la autonomía del agente; y T08, con T07 como secundario, cuando el objeto de la tesis es el método con que se evalúa o se evidencia la IA (RD-02, caso a). (b) Instrumento. La IA es el medio con que se hace una práctica de seguridad (detectar, responder, probar, construir reglas) o con que ataca el adversario, y la tesis trata lo que la IA aporta: pierde su contenido si la tarea se hace sin IA. El dominio es D21, D22 o D23 (RP-04.4, RP-04.5), o D12 si es del adversario. El territorio es el de la práctica (la definición de T06 nombra el SOC con agentes) y T07 queda como secundario. Si la tesis trata la práctica misma (el procedimiento, la regla, la cola) y la IA es un ejecutor más, el dominio es el de la práctica y D21, D22 o D23 quedan como secundarios. (c) En los demás casos se aplica la prueba de sustitución (RP-10.1): se reemplaza el sistema de IA por «un sistema» cualquiera. Si la tesis conserva su prescripción principal, la IA es contexto: el territorio y el dominio son los del control o la disciplina que la tesis prescribe, y T07 y D20 quedan como secundarios. Es el caso de un control general aplicado a un sistema de IA (segmentación, cifrado, control de acceso: RD-19), de una disciplina operativa aplicada a la IA (monitoreo, respuesta, continuidad: RP-01.1) y del programa, la adopción o la economía de la IA. Si la tesis pierde su prescripción principal, la IA es el objeto y se sigue por (a). Qué cuenta como IA: la tesis la nombra con cualquier término que designe un sistema de IA (modelo, agente, asistente, copiloto, herramienta de IA) o remite a la IA nombrada en el título o en la oración anterior («la adopción», «la herramienta»). No cuenta cuando aparece solo en el título o en el cuerpo y la tesis se sostiene sin ella. «Automatización» y «velocidad de máquina» no son IA. Las menciones de IA en las definiciones de T03 (economía de la automatización), T04 (riesgo de las transiciones) y T06 (SOC con agentes) valen como territorio primario en los casos (b) y (c), y como secundario en el caso (a). La responsabilidad de una persona por lo que produce con una herramienta de IA, y su formación, no son la regla de uso: se deciden por (c). El interlocutor ante quien se responde no cambia el territorio (RP-09.1). | b, c, d | 31 |
| RD-02 | dominio | RV-5, RP-02.1, RP-02.2, RP-01.1, RP-03.2, RP-04.4 | Cuando la tesis prueba, mide, audita o reúne evidencia sobre algo, se mira cuál es su objeto. (a) El método: cómo se prueba, qué cuenta como evidencia, quién atesta, qué mide un indicador y qué no; también el programa de pruebas, la auditoría o la medición como disciplina. El dominio es D28 y el de lo probado queda como secundario; el territorio es T08 por su definición. (b) Una capacidad concreta que tiene dominio propio, y la prueba o la medición es el medio para saber si funciona. El dominio es el de la capacidad, con D28 como secundario (RP-02.2), y el territorio es el de la capacidad. «Capacidad con dominio propio» es cualquier práctica con dominio en el catálogo, incluidos el gobierno (D01), el riesgo (D02), los terceros (D17) y las personas (D24). (c) La decisión que usa la prueba (aprobar, autorizar, aceptar). El dominio es el de la decisión, con D28 como secundario: D01 si autoriza y D02 si acepta un riesgo (RP-04.1). Prueba entre (a) y (b): reemplazar la capacidad nombrada por «un control cualquiera» (o «una práctica cualquiera»). Si la tesis conserva todas sus exigencias, el objeto es el método: (a). Si alguna exigencia es propia de la capacidad, es (b). Si la tesis no nombra ninguna capacidad, o la que nombra no tiene dominio, es (a). Si mide una capacidad concreta y además discute la validez de la medida o del método, manda el método: (a) (RP-02.1). Entre (a) y (c): es (c) si la tesis fija quién decide o con qué umbral se aprueba; es (a) si fija cómo se obtiene la evidencia o qué vale. RP-02.5, RP-02.6, RP-03.2 y RP-04.4 nombran casos de (a): valen cuando el objeto es la auditoría o el aseguramiento como método. Para la IA rige la misma prueba: si la tesis trata cómo se evalúa o se evidencia la IA (método, criterios, quién atesta), es (a), con D20 como secundario; si prescribe un control propio de la IA y la medición es el medio para saber si funciona, es (b) y queda en D20. La IA como instrumento de la prueba es D22 cuando la tesis trata lo que la IA aporta; si además discute la validez del método, manda el método. El destinatario no cambia el dominio ni el territorio (RP-02.3, RP-09.1): «ante el auditor» o «debe poder demostrar» no llevan a D28. Si la prueba da (b), el dominio es el de la capacidad aunque la tesis enumere la evidencia que se entrega. La evidencia de cumplimiento de una obligación sigue en D03 (RP-02.4). El informe como instrumento de supervisión queda en D01 y el informe de riesgo, en D02; pasan a D28 solo cuando la tesis discute qué se puede afirmar y con qué respaldo. Evaluar a un tercero como parte de su gestión (clasificarlo, pedirle evidencia, seguirlo) es (b): D17 (RP-09.4). | b, c, d | 11 |
| RD-03 | subfunción | RP-13, RV-1 | La mejora continua pasa a la función Identificar con un código nuevo, ID06 «Mejora continua y lecciones aprendidas»: la mejora que sale de la operación, de los incidentes y de los ejercicios, las acciones correctivas y su seguimiento, y el mantenimiento de los planes. RC04 no se reutiliza para otra cosa y queda acotada: «Lecciones y cierre de la recuperación», es decir, declarar el fin de una recuperación con criterios, completar la documentación del incidente y registrar las lecciones de esa recuperación. El aprendizaje posterior a un incidente que cambia prácticas, planes o controles es ID06. ID05 queda para evaluar y medir la brecha; ID06, para decidir qué se corrige a partir de lo aprendido o de un hallazgo y seguirlo hasta el cierre, en cualquier dominio. El plan de acción sobre los hallazgos de una evaluación, una auditoría, un incidente o un ejercicio es ID06; el plan de tratamiento que sale de un análisis de riesgo es ID04 (RD-06). La corrección misma va como secundaria a su subfunción (PR05 si es formación, PR04 si es un cambio técnico). La revisión periódica de una política o de un procedimiento como norma es GV03; el cambio de un plan a partir de un incidente, un ejercicio o una evaluación es ID06; el contenido del plan de respuesta es RS01. | a, c, e | 14 |
| RD-04 | subfunción | RV-2 | La prueba o la medición de eficacia va a GV08 solo cuando quien revisa no depende de la función evaluada ni es dirigido por ella: auditoría interna o externa y atestación. Cuando la hace la propia función de seguridad o su segunda línea, va a ID05, aunque lo evaluado lo opere otra área y aunque la ejecute un tercero que la función contrata y dirige. Tres salvedades: si pone a prueba la detección es DE03 y si mide su cobertura o su calidad es DE04 (RP-12.4); si prueba los respaldos o su restauración es PR02 (RD-07); si valida el retorno tras una recuperación real es RC03. El ejercicio de recuperación sin incidente es ID05. Si la tesis no dice quién prueba o mide, se presume la propia función (ID05). Las palabras «auditoría» o «atestación», o un auditor que ejecuta la prueba, cuentan como independencia; un auditor que solo recibe la evidencia, no. La evaluación que la organización hace de un proveedor es supervisión de la cadena de suministro: GV09; GV08 queda para la atestación o la auditoría independiente que el proveedor entrega. | a, d | 11 |
| RD-05 | subfunción | RV-2 | El procedimiento como norma general (qué exige, quién lo aprueba, cuándo se revisa) es GV03. El procedimiento propio de una función operativa va a la subfunción de esa función: el plan o el procedimiento de respuesta es RS01 y el de recuperación, RC01 o RC02. La preparación de quienes lo ejecutan (formación, práctica, instrucciones de trabajo en el punto de uso) es PR05. El ejercicio o la simulación es PR05 cuando la tesis busca que las personas sepan ejecutar e ID05 cuando busca medir la brecha; sus correcciones son ID06 (RD-03). | a, d | 2 |
| RD-06 | subfunción | RV-2 | Elegir, priorizar, planificar, seguir y comunicar la respuesta a un riesgo identificado (mitigar, transferir, evitar, elegir el control que lo trata) es ID04. GV04 queda para el apetito, la tolerancia, la dirección sobre las opciones de respuesta y la aceptación del riesgo. «Dirección sobre las opciones» es el criterio general de la organización: qué respuestas admite, con qué umbrales y quién las aprueba. De las decisiones sobre un riesgo concreto, solo la aceptación va a GV04, con sus condiciones y su vencimiento; quién tiene la autoridad para aceptar es GV02. La excepción a una norma: evaluarla por su efecto en el riesgo, registrarla y seguirla hasta su vencimiento es ID04; la decisión de aceptarla, por quien tiene la autoridad, es GV04; elegir el control que la compensa es ID04. Seleccionar controles para el catálogo o la línea base de la organización es GV03 (RD-11). Comunicar una decisión de tratamiento a quienes la ejecutan es parte de seguir la respuesta (ID04); informar el riesgo al órgano que decide es GV07. | a, b | 6 |
| RD-07 | subfunción | RV-2 | Los respaldos como medida previa (crearlos, protegerlos, mantenerlos y probarlos) son PR02. Usarlos para restaurar, con sus objetivos de tiempo y de punto de recuperación, es RC01. La prueba periódica de restauración es parte de probar los respaldos (PR02); verificar su integridad al usarlos en una recuperación en curso es RC01; validar lo restaurado y el retorno a la operación es RC03. | a, d | 1 |
| RD-08 | subfunción | RV-2 | En el dominio D24: el diseño de roles, responsabilidades y autoridad del equipo es GV02; el liderazgo que forma cultura, ética y rendición de cuentas, y la conducta de quien lidera al decidir, es GV10; la formación y el desarrollo de competencias es PR05; la contratación, la retención y las prácticas de recursos humanos del equipo son GV05. La lista no es cerrada: lo que no nombra se decide por las definiciones. La dotación y los recursos tratados como recurso del programa también son GV05, pero su dominio es D04 (RD-13). Asignar quién es responsable de qué es GV02; responder por lo hecho (consecuencias, reporte de errores) es GV10. La carga, la fatiga o el desgaste de las personas no tienen subfunción que los nombre (VC-15). | a, d | — |
| RD-09 | subfunción | RV-3, RP-11.1, RP-12.8 | RP-11.1 se aplica a la subfunción primaria: cuando la tesis prescribe dos o más resultados de subfunciones distintas, sean o no de la misma función, la primaria es la de la primera prescripción. Hay una sola excepción: cuando la tesis declara un propósito con una marca expresa («para», «a fin de», «de modo que», «con el objetivo de»), manda la subfunción del propósito y lo demás son medios. El orden que cuenta es el de la tesis; el título no declara el propósito, tampoco en las series K y HC. Una tesis que exige un instrumento (una norma, un plan, un procedimiento) y enumera lo que debe contener tiene una sola prescripción: la del instrumento. El destinatario del texto no cambia la subfunción, igual que no cambia el dominio ni el territorio (RP-02.3, RP-09.1): «ante el directorio» no lleva a GV07. GV07 es primaria cuando el objeto de la tesis es el informe o la sesión del órgano: qué se informa, con qué cadencia y qué decide el órgano (RP-12.8). | b, d | 7 |
| RD-10 | método de lectura | RV-6, RP-10.2 | Manda la tesis que el texto declara. Dónde está: en las ampliaciones por pregunta (series APC, APA, APN, APS, APF y APX), en el bloque «Tesis:», que cuenta entero; en la oración «La tesis es que…» cuando el texto la trae (series AMP y PA, y algunos K); en la serie K, en la primera oración junto con el título (RP-10.2); en los puentes (serie HC), en la primera oración, que es la propia del puente, junto con el título (RP-10.3). En AMP y PA sin tesis declarada rige el campo de tesis. Cuando la oración de tesis remite a algo dicho antes («responderla», «la adopción»), las oraciones anteriores fijan de qué habla; si llevan a coordenadas distintas, manda la oración de tesis. Cuando la tesis define o describe en lugar de prescribir, las reglas que hablan de lo que la tesis prescribe, fija o exige se aplican a lo que la tesis presenta como propio de la práctica. | b, c | 2 |
| RD-11 | dominio y territorio | RP-08.4, RP-10.6 | El catálogo de controles de la organización (qué controles adopta, de qué marcos y versiones, cómo los selecciona y adapta, con qué línea base y cuándo los actualiza o los retira) es D01, igual que el marco como sistema de gestión (RP-10.6). Pasa a D28 cuando la tesis evalúa la cobertura o la eficacia de los controles, o la validez de un mapeo como evidencia, y su objeto es el método (RD-02, caso a); a D04 cuando trata los controles como portafolio o como producto, con inversión y dueño; a D02 cuando trata la excepción, la compensación o la aceptación del riesgo residual; y al dominio del objeto cuando es la implementación del control de un pilar (R3, RP-01.2). El marco, el estándar de referencia o la norma interna propios de una disciplina con dominio (continuidad, respuesta a incidentes, privacidad, riesgo) van al dominio de esa disciplina; la obligación legal sigue en D03 (RP-10.7); D01 es para el sistema de gestión de la seguridad en conjunto. Quién decide dentro de una disciplina no lo fija esta regla (VC-03). Con D01 por esta regla, el territorio es T05 cuando la tesis decide qué controles y con qué línea base, y sigue RP-09.3 en los demás casos. | a, b, e | 7 |
| RD-12 | dominio | RP-18.2 | D18 cuando la tesis trata el control o la supervisión de un proceso industrial o de una infraestructura operada (una planta, una red de servicio) y su operación: sistemas de control industrial, seguridad de proceso y operación del proceso. D19 cuando trata el dispositivo conectado o el producto ciberfísico (un vehículo, un dispositivo médico, un sistema de edificio) como producto o como flota: identidad, actualización, configuración, ciclo de vida y datos del dispositivo, en cualquier sector, también dentro de una planta. Prueba dentro de un entorno industrial: si al quitar el proceso controlado la tesis sigue en pie, es D19. La continuidad del proceso industrial es D18 cuando la tesis trata la operación del proceso (modo manual, parada segura) y D16 cuando trata el plan de continuidad o la restauración de los sistemas (RP-01.1). Los dos dominios no se consolidan. | a, d, e | 2 |
| RD-13 | dominio | RP-18.4 | La carga y la capacidad del equipo son D04 cuando la tesis las trata como recurso del programa (dotación, horas, asignación, capacidad frente a demanda, costo) y D24 cuando las trata como condición de las personas (fatiga, desgaste, carga cognitiva, retención, competencias). Si trata las dos, manda lo que prescribe cambiar: dimensionar o asignar (D04) o cuidar a las personas (D24). Si prescribe reducir la carga cambiando la práctica que la genera (ajustar las detecciones, ordenar la cola), el dominio es el de esa práctica. | b, d | — |
| RD-14 | dominio | RP-18.7 | La automatización de seguridad que no usa IA se clasifica en el dominio de la práctica que automatiza (por ejemplo: respuesta, D15; detección, D14; configuración y exposición, D13; canalización de software, D11) y en D04 cuando la tesis es el programa o la economía de la automatización. La política aplicada como código es D01 cuando la tesis trata el mandato que se codifica y sus excepciones, y D11 o D13 cuando trata la canalización o la configuración que lo verifica. D23 queda para la IA que crea reglas, políticas, configuraciones y automatizaciones. Si la tesis no dice que la automatización usa IA, se presume que no. | a, b | 1 |
| RD-15 | dominio | RP-04.6 | El control técnico que hace cumplir la regla de uso de herramientas de IA va al dominio del pilar donde actúa: D06 cuando actúa sobre los datos que se entregan a la herramienta, aunque se ejecute en el navegador; D09 cuando controla qué herramientas, aplicaciones o extensiones se pueden usar en el puesto de trabajo; D05 cuando actúa sobre la identidad y el acceso; y D14 cuando es el monitoreo del uso o el descubrimiento de las herramientas por el tráfico o los registros. El inventario de las herramientas de IA en uso es D20 (RP-08.2). El territorio de estos controles se decide por RD-01 (c): es el del control, con T07 como secundario. | b, d | 1 |
| RD-16 | dominio | RP-06.3 | La detección de la fuga de secretos es D11 cuando el secreto está en código, repositorios o canalizaciones, y D06 cuando está en documentos, mensajes o instrucciones a un modelo. La revocación y la rotación del secreto son D26 (RP-06.1); la baja de la identidad que lo usa es D05 (RP-06.2). | b, d | — |
| RD-17 | subfunción | RP-12.10 | En la supervisión humana de agentes: GV02 cuando la tesis fija quién supervisa o aprueba y con qué autoridad; GV03 cuando fija la norma (los niveles de autonomía o la exigencia del interruptor como política). Cuando la tesis lleva esa supervisión a un procedimiento operativo (un procedimiento de respuesta, una cola), manda la subfunción operativa (RD-05) y GV02 o GV03 quedan como secundarias. Cuando exige el mecanismo técnico y no la norma (RD-18, D20), la subfunción no tiene regla (VC-10), salvo que fije quién acciona el interruptor (GV02). | a, d | 1 |
| RD-18 | dominio | RP-04.1, RP-04.3 | Entre RP-04.1 y RP-04.3 manda lo que la tesis prescribe. Es D01 cuando dice quién fija o aprueba el límite, por qué ruta, o lo enuncia como regla (la decisión). Es D20 cuando dice dónde o cómo se hace cumplir: en la plataforma, en el entorno de ejecución, en el conector (el mecanismo: interruptor, límites de lote, compuertas). La autorización de un agente a herramientas, conectores y datos, expresada como identidad y permisos (credenciales, alcances, mínimo privilegio), es control de acceso: D05 con D20 como secundario (RD-19). El inventario de sistemas de IA y de agentes es D20 (RP-08.2) aunque lo exija una política; es D01 cuando la tesis decide quién autoriza el alta o quién responde por cada agente. | b, d | — |
| RD-19 | dominio | RP-01.2, RP-05.3 | En RP-01.2, el control técnico propio de un objeto es el que solo existe por la naturaleza de ese objeto (para la IA: filtros de instrucciones y de salidas, protección de la memoria del agente, límites de lote y compuertas del entorno de ejecución). Un control general que se aplica a ese objeto queda en el dominio del pilar donde actúa, con el del objeto como secundario: la segmentación en D08, el cifrado en D06 o D08 (RP-06.4) y el control de acceso en D05. La gestión de cambios como disciplina general no tiene dominio (VC-05). La gobernanza de identidades como práctica de identidad (altas, bajas, revisión y certificación de accesos) es un control propio de D05; el gobierno de la seguridad aplicado a la identidad (quién decide y con qué política) es D01 (RP-01.1). Cuando una disciplina de RP-01.1 se ejerce mediante un control propio del objeto, manda lo que la tesis prescribe: el resultado de la disciplina (contener, decidir el tratamiento) sigue RP-01.1; cómo debe ser el control sigue RP-01.2. La arquitectura de referencia de un objeto (sus capas y fronteras) es D25 (RP-05.3) aunque sus piezas sean controles propios; el dominio del objeto es para cada control que la implementa. El territorio de un control general aplicado a la IA se decide por RD-01 (c). | b, d | 4 |
| RD-20 | pilar del MCCS | RP-14.3 | El liderazgo de personas y la gestión de equipos son elementos de la biblioteca metacognitiva del autor, en la categoría de habilidades socioemocionales («Liderazgo», SOFT-0035; «Gestión de equipos», SOFT-0026; «Construcción de equipos», SOFT-0015; «Motivación y desarrollo de equipos», SOFT-0062, entre otros), con territorio editorial T02. Llevan el pilar que la regla de pilar da a esa categoría: MM. Un pre-ensayo cuya tesis es la habilidad de quien lidera lleva el pilar MM. Cuando la tesis no es la habilidad sino el diseño de la oficina (roles, derechos de decisión, cadencias, dotación), es el pilar OS a escala de oficina. | a, b | no es de lectura |
| RD-21 | lente de la agenda de IA | RP-17.1 | La lente de la agenda de IA se deriva de la coordenada y no se asigna a mano. Se aplica a los elementos que tienen coordenada (pre-ensayos, ensayos e indicadores). IA-P1, seguridad de la IA: dominio D20, o territorio T07 con dominio D01, D02, D03 o D28. IA-P2, IA para la seguridad: dominio D21, D22 o D23. IA-P3, IA adversaria: dominio D12 con T07 como territorio primario o secundario, o con D20 como dominio secundario. Un elemento que no cumple ninguna condición no lleva la lente. | c, d | no es de lectura |
| RD-22 | plano | RP-17.4 | Un pre-ensayo que desarrolla una instancia de producto de un proveedor no pasa al plano B: el plano B es de instancias de dominio del GM-24 (tareas, agentes, herramientas), y un pre-ensayo no lo es. Queda en el plano A marcado como «nombra producto o proveedor» y fuera de la promoción a ensayo hasta que se reescriba sin marca. La instancia de producto, si hace falta, se expresa en el plano B y se vincula al pre-ensayo. | b, c | no es de lectura |
| RD-23 | Biblioteca | RP-18.5 | Los elementos de la biblioteca metacognitiva no llevan dominio. Llevan su categoría, sus territorios editoriales y su pilar. Un elemento se relaciona con un dominio solo a través de los pre-ensayos, los ensayos o las unidades que lo usan. | a, b, e | no es de lectura |
| RD-24 | modelo | RP-18.6 | El aseguramiento como objeto lo expresa un solo eje: el dominio D28. Los otros tres no lo expresan ni se derivan de él: T08 es la perspectiva de quien necesita confiar y con qué evidencia; GV08 es el resultado de gobierno cuando la revisión es independiente (RD-04); HOM09 es el mecanismo, y se asigna solo si el texto nombra la validación como lo que mantiene estable una variable. Ninguno de los cuatro implica a otro: cada uno se asigna con su propia prueba. | b, c | no es de lectura |

**Una corrección de fondo: RD-06.** Antes de la lectura, la regla mandaba toda la gestión de excepciones a la subfunción de decisión sobre el riesgo. NIST CSF 2.0 ubica la gestión de las excepciones en la evaluación de riesgos (ID.RA-07). La regla quedó así: gestionar la excepción es ID04; solo la decisión de aceptarla es GV04.

### 3.3 Cómo quedaron los seis puntos de la revisión y las once preguntas

| Punto | Reglas | Decisión |
|---|---|---|
| RV-1 | RD-03 | Opción a de RP-13: ID06 nueva y RC04 acotada. |
| RV-2 | RD-04, RD-05, RD-06, RD-07, RD-08 | Las cinco fronteras entre subfunciones quedan fijadas con el texto de NIST CSF 2.0. |
| RV-3 | RD-09 | RP-11.1 se aplica a la subfunción primaria: cuando la tesis prescribe dos o más resultados de subfunciones distintas, sean o no de la misma función, la primaria es la de la primera prescripción, con una sola excepción. Antes de la revisión previa de las reglas el texto decía «solo como desempate»: la regla vigente extiende RP-11.1, que hablaba de dos funciones, a las subfunciones de una misma función. |
| RV-4 | RD-01 | Orden entre las reglas de IA: primero el objeto de la tesis, después la prueba de sustitución y recién entonces T07. |
| RV-5 | RD-02 | Precedencia en D28: manda el objeto de la tesis (método, capacidad o decisión), con una prueba. |
| RV-6 | RD-10 | Manda la tesis que el texto declara; RP-10.2 vale solo para la serie K. Toda la serie AMP se volvió a leer con su tesis declarada. |

| Pregunta | Regla | Decisión |
|---|---|---|
| RP-08.4 | RD-11 | El catálogo y el ciclo de vida de los controles van a D01; a D28, D04 o D02 según el objeto de la tesis. No se crea un dominio. |
| RP-13.1 | RD-03 | Opción tomada: la mejora continua pasa a Identificar con el código nuevo ID06 y RC04 queda acotada a las lecciones y el cierre de la recuperación. |
| RP-13.2 | RD-03 | Opción no tomada: mantenía bajo Recuperar un contenido que NIST CSF 2.0 ubica en Identificar (ID.IM). |
| RP-14.3 | RD-20 | El liderazgo de personas y la gestión de equipos son habilidades socioemocionales de la biblioteca: pilar MM. El diseño de la oficina es OS a escala de oficina. |
| RP-17.1 | RD-21 | La lente de la agenda de IA se deriva de la coordenada con una regla escrita; no se asigna a mano. |
| RP-17.4 | RD-22 | Los pre-ensayos que desarrollan un producto de un proveedor no pasan al plano B: quedan marcados y fuera de la promoción a ensayo hasta que se reescriban sin marca. |
| RP-18.2 | RD-12 | Frontera escrita con una prueba: D18, el proceso físico controlado; D19, el dispositivo como producto o flota. No se consolidan. |
| RP-18.4 | RD-13 | La carga y la capacidad del equipo: D04 como recurso del programa; D24 como condición de las personas. |
| RP-18.5 | RD-23 | Los conceptos de la biblioteca no llevan dominio. |
| RP-18.6 | RD-24 | El aseguramiento como objeto lo expresa solo el eje Y (D28). T08, GV08 y HOM09 dicen otra cosa, cada uno en su eje. |
| RP-18.7 | RD-14 | La automatización de seguridad que no usa IA va al dominio de la práctica que automatiza, o a D04 cuando la tesis es el programa o la economía de la automatización. |
| RP-10.6 (cláusula final) | RD-11 | El catálogo de controles como modelo va a D01, igual que el marco como sistema de gestión. |

### 3.4 Estado de los 95 enunciados

| Estado en la versión 1.4 | Enunciados |
|---|---|
| adoptada y confirmada | 58 |
| pregunta decidida por delegación | 11 |
| adoptada, sin aplicar | 2 |
| encargo hecho en la 1.3 | 3 |
| encargo ejecutado en la 1.4 | 21 |

El estado de cada enunciado está en `data/reglas_propuestas_D11_enunciados.csv`.

### 3.5 La revisión previa de las reglas y sus límites

Antes de lanzar la lectura, dos revisores leyeron las reglas: uno las contrastó con los patrones que habían dejado anotados los lectores de la versión 1.3 y buscó contradicciones; el otro clasificó una muestra piloto de 30 pre-ensayos y anotó lo que no se podía aplicar. El primero contrastó 123 patrones: 22 resuelto, 52 resuelto en parte, 28 sin cubrir y 21 declarado como vacío; y anotó 45 contradicciones entre reglas. El segundo clasificó 30 pre-ensayos y dejó 69 hallazgos.

Con eso se corrigieron las reglas, los vacíos, las definiciones y el encargo de lectura. Las reglas se corrigieron después de la revisión previa y esa corrección no tuvo una segunda revisión antes de la lectura.

No se incorporó lo que pedía una regla nueva, porque eso queda fuera de lo que el autor delegó: una regla de territorio para cada dominio (queda como vacío VC-13), el acceso de red de confianza cero, entre identidad y red, precisiones a los enunciados RP-10.3, RP-10.5, RP-10.7 y RP-10.8, el dominio de los respaldos y la corrección de vulnerabilidades, entre exposición e infraestructura. Esos casos se leen con las definiciones; cuando no alcanzan, el lector declara confianza baja o anota un vacío, y el eje no cambia.

## 4. Vacíos declarados

Un vacío declarado es un caso para el que se sabe que ninguna regla decide. Son 15. Cuando una lectura anota uno, el eje que depende de él no cambia. Cada vacío es una decisión que el autor puede tomar (D-17.4): `data/vacios_declarados.csv` trae dos columnas para anotarla.

| Código | Eje | Caso sin regla | Pre-ensayos en que lo anotan las dos lecturas | Pre-ensayos en que lo anota una |
|---|---|---|---|---|
| VC-01 | territorio | Una tesis de cumplimiento (D03) o de privacidad (D07) fuera de la IA: las definiciones no dicen si se mira desde la evidencia (T08), el riesgo (T04) o la organización (T02 o T03). | 27 | 2 |
| VC-02 | territorio | Una tesis de D01 fuera de la IA que no trata quién decide, cómo opera la oficina ni cómo se demuestra (las tres opciones de RP-09.3), o que admite más de una, y que tampoco es la decisión de qué controles y con qué línea base (RD-11). | 25 | 16 |
| VC-03 | dominio | La precedencia entre dos dominios cuando RP-01.1 no nombra a alguno de los dos, ni como disciplina ni como objeto (terceros, personas, aplicaciones, redes, inteligencia de amenazas), o cuando los dos son disciplinas, incluido quién decide dentro de una disciplina que tiene dominio. No vale para los pares que decide una regla (RP-10.5, RD-02, RD-11, RD-13, RD-14). | 31 | 24 |
| VC-04 | dominio | Un control de proceso sobre un proceso de negocio (por ejemplo, verificar pagos ante fraude o suplantación): ningún dominio lo tiene por objeto. | 2 | 1 |
| VC-05 | dominio | La gestión de activos, de la configuración o de los cambios como disciplina general: el proceso de registrar, aprobar y controlar activos, configuraciones o cambios. No es el inventario de un tipo de activo (RP-08.2), ni la postura como exposición o la línea base segura y sus desvíos (D13: RP-08.1 y RP-08.3). Ningún dominio la tiene por objeto. | 10 | 2 |
| VC-06 | dominio | El reparto de responsabilidad entre la organización y un proveedor o una plataforma (quién opera cada control): cabe en D01, en D17 y en D10. | 2 | 2 |
| VC-07 | dominio | Un puente (serie HC) cuyo título nombra dos temas de dominios distintos, no deja claro si el propósito es la disciplina o el objeto, o apunta a un dominio distinto del de su primera oración (RP-10.3). | 13 | 5 |
| VC-08 | subfunción | La subfunción de un puente (serie HC), que relaciona prácticas en lugar de prescribir una. | 40 | 0 |
| VC-09 | subfunción | Una función de gobierno (repartir autoridad, supervisar, decidir) aplicada a una función operativa: las reglas no dicen si la subfunción es la de gobierno o la de la función que es su objeto. No vale donde la definición de la subfunción operativa ya nombra los roles o las decisiones (RS01, RS03) ni para la supervisión de agentes (RD-17). | 4 | 2 |
| VC-10 | subfunción | El mecanismo técnico que limita o filtra a un modelo o a un agente y no es un permiso de acceso (filtros de instrucciones y de salidas, límites de lote, compuertas del entorno de ejecución, interruptor): ninguna subfunción de Proteger lo nombra. Los permisos de acceso de un agente son PR01. | 9 | 3 |
| VC-11 | dominio | Un texto cuyo objeto es el propio Atlas, su método o el currículo, y no una práctica de seguridad. Vale para los tres ejes. Un programa de formación de una organización no es este caso. | 1 | 0 |
| VC-12 | territorio | La operación por cadencias de un control cuando el dominio es D01, D04 o D28: RP-09.7 lleva a T06 y el dominio lleva a T02, T03 o T08. | 3 | 2 |
| VC-13 | territorio | Una tesis cuyo dominio no tiene regla de territorio (los que no son D01, D03, D07 ni D17, fuera de los casos de IA) y cuyo objeto toca dos definiciones de territorio: por ejemplo, la inteligencia de amenazas entre T04 y T06, la decisión ejecutiva durante un incidente entre T06 y T02, o la comunicación de una decisión de riesgo entre T04 y T02. | 49 | 44 |
| VC-14 | dominio | Una tesis que prescribe a la vez dos cosas que las reglas mandan a dominios distintos, sin que una sea el propósito declarado de la otra: por ejemplo, la regla y el control técnico que la hace cumplir, la evaluación y la decisión que la usa, la autorización de un agente y la aceptación de su riesgo, o detectar un secreto expuesto y revocarlo. | 15 | 13 |
| VC-15 | subfunción | La carga, la fatiga o el desgaste de las personas (que RD-13 manda a D24): ninguna subfunción los nombra. | 3 | 0 |

En total, 274 pre-ensayos tienen algún vacío anotado por alguna lectura.

## 5. El eje H, revisión 2

El eje H dice cómo cambia una práctica y qué la mantiene estable. Es una propuesta de diseño del Atlas, sin respaldo normativo externo, y no mide madurez.

| Término | Qué significa en el Atlas |
|---|---|
| fuerza | Lo que un texto nombra como causa de que una práctica cambie (catalizador) o de que no pueda cambiar (inhibidor). Los mecanismos homeostáticos no son fuerzas: son lo que regula (RP-15.8). |
| contexto | Parámetro de la organización que usa el Atlas: se describe con un valor de una escala, se puede medir en una fecha y vale para todas las decisiones del período. No se asigna a un pre-ensayo por lo que prescribe (RP-15.5). |
| presiona | Una fuerza presiona una variable cuando cambia uno de sus dos términos. Cada vínculo declara el término (demanda o capacidad) y el sentido (lo aumenta o lo reduce) (RP-15.3). |
| regula | Un mecanismo regula una variable con uno o más papeles: referencia (fija el límite aceptable), sensor (observa la variable), decisor (compara y decide la corrección) o efector (ejecuta la corrección) (RP-15.4). |
| convergencia | Marcador, aparte del horizonte: la tesis es la integración de disciplinas o de capacidades que antes iban separadas. No es una etapa (RP-15.6). |

### 5.1 Horizontes y marcador de convergencia

| Código | Nombre | Definición |
|---|---|---|
| H01 | Foundational | Práctica consolidada y vigente; no significa madurez baja. |
| H02 | Evolving | Práctica existente modificada por fuerzas de transformación. |
| H03 | Emerging | Práctica o capacidad nueva o en consolidación; no implica superioridad. |

«Indeterminado» es una respuesta válida. **H04 (Convergent)** ya no es un horizonte: Marcador de convergencia: la tesis es la integración de disciplinas o de capacidades que antes iban separadas. No es un horizonte ni una etapa obligatoria. Un pre-ensayo tiene un horizonte y, aparte, el marcador en «sí» o «no».

### 5.2 Fuerzas, mecanismos y contexto

| Código | Catalizador | Definición |
|---|---|---|
| CAT01 | Innovación tecnológica | Capacidades técnicas nuevas (IA generativa y agéntica, nube, automatización) que habilitan o exigen prácticas nuevas. |
| CAT02 | Presión competitiva | Pares o competidores que adoptan antes y vuelven costoso esperar. |
| CAT03 | Presión regulatoria | Obligaciones nuevas o plazos regulatorios que fuerzan el cambio. |
| CAT04 | Evolución de amenazas | Adversarios que cambian de técnica, de escala o de velocidad. |
| CAT05 | Transformación empresarial | Cambios del modelo de negocio o de operación que arrastran a la seguridad. |
| CAT06 | Presión económica | Exigencia de eficiencia, de costo por resultado o de retorno demostrable. |
| CAT07 | Incidentes y crisis | Eventos propios o ajenos que abren una ventana de cambio. |
| CAT08 | Proveedores y ecosistema | Hojas de ruta de proveedores, plataformas y socios que empujan la adopción. |
| CAT09 | Expectativas de clientes | Clientes y contrapartes que exigen garantías o evidencia. |
| CAT10 | Patrocinio ejecutivo | Directorio o alta dirección que impulsa y financia el cambio. |
| CAT11 | Geopolítica y soberanía digital | Tensiones entre Estados, sanciones, requisitos de localización y control soberano de datos, infraestructura y proveedores. |

| Código | Inhibidor | Definición |
|---|---|---|
| INH01 | Deuda tecnológica | Sistemas heredados y complejidad acumulada que encarecen el cambio. |
| INH02 | Presupuesto | Fondos insuficientes o no asignados. |
| INH03 | Déficit de capacidades | Faltan habilidades o personas para ejecutar. |
| INH04 | Silos organizacionales | Fronteras entre áreas que impiden decidir u operar en conjunto. |
| INH05 | Restricciones regulatorias | Normas que limitan o demoran la adopción. |
| INH06 | Concentración y lock-in | Dependencia de pocos proveedores que reduce las opciones. |
| INH07 | Calidad insuficiente de datos | Datos incompletos, sin dueño o sin clasificar. |
| INH08 | Resistencia cultural | Hábitos, incentivos y temores que frenan la adopción. |
| INH09 | Limitaciones operativas | Capacidad operativa saturada: no hay margen para cambiar mientras se opera. |
| INH10 | Incertidumbre tecnológica | Madurez, estándares o rumbo todavía inestables. |
| INH11 | Volumen de alertas y de decisiones | Cantidad de alertas, aprobaciones y decisiones por persona y por hora que exige la operación, incluida la supervisión de agentes. Es la causa; el estado que produce lo describe la variable HV05. |

| Código | Mecanismo homeostático | Definición |
|---|---|---|
| HOM01 | Apetito y tolerancia al riesgo | Límites declarados que indican cuánto riesgo se acepta mientras se cambia. |
| HOM02 | Gestión de cambios | Control de qué cambia, cuándo y con qué reversibilidad. |
| HOM03 | Segregación de funciones | Separación entre quien propone, quien aprueba y quien ejecuta. |
| HOM04 | Monitoreo continuo | Observación permanente que detecta los desvíos a tiempo. |
| HOM05 | Respuesta a incidentes | Capacidad de contener y corregir cuando el desvío ocurre. |
| HOM06 | Continuidad | Sostener los servicios críticos durante la perturbación. |
| HOM07 | Rollback y recuperación | Volver a un estado conocido y bueno. |
| HOM08 | Gobierno y supervisión | Órganos y cadencias que revisan y corrigen el rumbo. |
| HOM09 | Assurance y validación | Prueba independiente de que los controles funcionan. |
| HOM10 | Aprendizaje organizacional | Convertir incidentes y resultados en cambios de práctica. |
| HOM11 | Metacognición y revisión de supuestos | Práctica deliberada de revisar cómo se decide: supuestos, sesgos y modelos mentales. |
| HOM12 | Gobierno de la autonomía (niveles, aprobación humana e interruptor probado) | Niveles de autonomía, aprobación humana registrada e interruptor probado para agentes. |

Los factores de contexto tienen ahora una escala. HX08 ya la tenía.

| Código | Factor de contexto | Definición | Escala | Valores |
|---|---|---|---|---|
| HX01 | Industria | Sector y modelo de negocio. | nominal | Sector según la clasificación oficial de la jurisdicción de la organización; más un marcador: servicio esencial o infraestructura crítica (sí o no). |
| HX02 | Jurisdicción | Países y regímenes regulatorios aplicables. | nominal | Lista de países y regímenes aplicables; más un marcador: más de un régimen (sí o no). |
| HX03 | Postura tecnológica | Plataformas, nube y deuda técnica de partida. | ordinal | ['predominan los sistemas heredados', 'mixta', 'predominan las plataformas actuales'] |
| HX04 | Criticidad | Criticidad de los servicios y de los datos afectados. | ordinal | ['baja', 'media', 'alta', 'crítica'] |
| HX05 | Dependencia | Dependencia de terceros, plataformas y proveedores. | ordinal | ['baja', 'media', 'alta', 'concentrada en un tercero sin sustituto práctico'] |
| HX06 | Presión de adopción | Urgencia con que el negocio pide adoptar. | ordinal | ['baja', 'media', 'alta, con plazo impuesto'] |
| HX07 | Preparación | Preparación de personas, procesos y datos. | ordinal | ['inicial', 'parcial', 'suficiente'] |
| HX08 | Configuración de la fuerza de trabajo (humana, híbrida, operada por agentes) | Cómo se reparte el trabajo entre personas y agentes. | nominal | ['humana', 'híbrida', 'operada por agentes'] |

### 5.3 Variables homeostáticas

Cada variable se escribe como una demanda frente a una capacidad o un límite.

| Código | Variable | Demanda | Capacidad o límite | Papeles sin mecanismo |
|---|---|---|---|---|
| HV01 | Exposición residual frente al apetito de riesgo | exposición residual | tolerancia que se deriva del apetito declarado (es un límite) | efector |
| HV02 | Autoridad delegada frente a capacidad de supervisión | autoridad delegada | capacidad de supervisar y revertir | ninguno |
| HV03 | Ritmo de cambio frente a capacidad de absorción | ritmo de cambio | capacidad de absorción | referencia, sensor |
| HV04 | Confianza de las partes interesadas sostenida por evidencia | evidencia que las partes interesadas exigen para confiar | evidencia vigente | referencia |
| HV05 | Carga cognitiva frente a capacidad de decisión | carga de atención y de decisión | capacidad de decisión | referencia, decisor |
| HV06 | Continuidad de los servicios críticos | perturbación de los servicios críticos | tolerancias de impacto (es un límite) y capacidad de sostener el servicio | referencia, sensor, decisor |

**Presiona.** 27 vínculos entre una fuerza y una variable; cada uno dice sobre qué término actúa y en qué sentido. 6 son nuevos en la 6.1: vinculan las cinco fuerzas que no presionaban ninguna variable. El detalle está en `data/modelo_h_presiona.csv`.

| Fuerza | Variable | Término | Sentido | Desde |
|---|---|---|---|---|
| CAT04 | HV01 | demanda | aumenta | 6.0 |
| CAT01 | HV01 | demanda | aumenta | 6.0 |
| INH01 | HV01 | demanda | aumenta | 6.0 |
| INH02 | HV01 | demanda | aumenta | 6.1 |
| CAT01 | HV02 | demanda | aumenta | 6.0 |
| CAT06 | HV02 | demanda | aumenta | 6.0 |
| INH03 | HV02 | capacidad | reduce | 6.0 |
| INH04 | HV02 | capacidad | reduce | 6.1 |
| CAT02 | HV03 | demanda | aumenta | 6.0 |
| CAT05 | HV03 | demanda | aumenta | 6.0 |
| CAT10 | HV03 | demanda | aumenta | 6.0 |
| CAT08 | HV03 | demanda | aumenta | 6.1 |
| INH05 | HV03 | demanda | reduce | 6.1 |
| INH08 | HV03 | capacidad | reduce | 6.0 |
| INH09 | HV03 | capacidad | reduce | 6.0 |
| INH10 | HV03 | capacidad | reduce | 6.1 |
| INH02 | HV03 | capacidad | reduce | 6.1 |
| CAT03 | HV04 | demanda | aumenta | 6.0 |
| CAT09 | HV04 | demanda | aumenta | 6.0 |
| CAT07 | HV04 | demanda | aumenta | 6.0 |
| INH07 | HV04 | capacidad | reduce | 6.0 |
| INH11 | HV05 | demanda | aumenta | 6.0 |
| INH03 | HV05 | capacidad | reduce | 6.0 |
| CAT04 | HV05 | demanda | aumenta | 6.0 |
| CAT07 | HV06 | demanda | aumenta | 6.0 |
| CAT11 | HV06 | demanda | aumenta | 6.0 |
| INH06 | HV06 | capacidad | reduce | 6.0 |

**Regula.** 19 vínculos entre un mecanismo y una variable, con el papel que cumple: referencia, sensor, decisor o efector. El detalle está en `data/modelo_h_regula.csv`.

| Mecanismo | Variable | Papeles |
|---|---|---|
| HOM01 | HV01 | referencia |
| HOM04 | HV01 | sensor |
| HOM09 | HV01 | sensor |
| HOM08 | HV01 | decisor |
| HOM12 | HV02 | referencia, decisor, efector |
| HOM03 | HV02 | decisor |
| HOM08 | HV02 | decisor |
| HOM04 | HV02 | sensor |
| HOM02 | HV03 | decisor |
| HOM07 | HV03 | efector |
| HOM10 | HV03 | efector |
| HOM09 | HV04 | sensor |
| HOM08 | HV04 | decisor |
| HOM05 | HV04 | efector |
| HOM11 | HV05 | sensor |
| HOM10 | HV05 | efector |
| HOM06 | HV06 | efector |
| HOM05 | HV06 | efector |
| HOM07 | HV06 | efector |

**Huecos de regulación.** Papeles que ningún mecanismo cumple hoy: HV01, sin efector; HV03, sin referencia y sensor; HV04, sin referencia; HV05, sin referencia y decisor; HV06, sin referencia, sensor y decisor. El alcance de este resultado es corto. Sale de ponerle un papel a los vínculos entre mecanismos y variables que la Taxonomía 6.0 ya traía; no se evaluaron los demás pares posibles, y los papeles los asignó el curador. Dice qué falta en esa tabla de vínculos, y no demuestra que al eje H le falte ese papel.

### 5.4 Variables propuestas, sin admitir

Criterios para admitir una variable: (1) se puede escribir como una demanda frente a una capacidad o un límite; (2) al menos un mecanismo del catálogo la regula; (3) al menos una fuerza del catálogo la presiona; (4) no se deriva de una variable vigente.

| Código | Variable | Definición | Veredicto |
|---|---|---|---|
| HV07 (propuesta) | Calidad de la decisión frente a la incertidumbre | La calidad de las decisiones (calibración, oportunidad y trazabilidad) se sostiene cuando aumenta la incertidumbre. | Cumple los cuatro criterios. Se propone. Es la variable que le da al MCCS algo propio que regular: hoy el mecanismo HOM11 solo regula la carga (HV05). |
| HV08 (propuesta) | Costo del programa frente al valor demostrado | El costo del programa de seguridad se mantiene dentro de lo que su valor demostrado justifica. | Cumple tres criterios y el cuarto en parte. Se propone con esa reserva: conviene decidirla junto con el nombre de HV04. |

Admitirlas es un cambio de catálogo que decide el autor (D-17.3).

## 6. Criterios de admisión de dominios, revisión 2

| Criterio | Nombre | Qué exige | Qué cambió respecto de la 6.0 |
|---|---|---|---|
| C1 | Respaldo externo | Al menos 5 artefactos independientes de al menos 3 organismos lo tratan como elemento de primer nivel o le dedican un artefacto completo. | Sin cambio en el umbral. Se definen «artefacto independiente» y «primer nivel» (RP-16.5). |
| C2 | No representable | Prueba de representación: se toman los elementos externos de primer nivel que respaldan al candidato. Es representable, y no cumple C2, si la mitad o más tiene como dominio primario un mismo dominio vigente cuya definición ya nombraba el objeto. No es representable, y cumple C2, si para alojarlos hizo falta un ajuste de alcance o quedan repartidos en tres o más dominios. Un candidato que no es un objeto ni una disciplina, sino una perspectiva, una función o una fuerza, no cumple C2. | Reescrito con una prueba que se calcula sobre el cruce de elementos y dominios (RP-16.1). |
| C3 | Presión del corpus o materialidad emergente | Al menos 10 pre-ensayos cuyo dominio queda forzado, medidos sin depender de la migración: pre-ensayos en que las dos lecturas a ciegas anotan el vacío que corresponde al candidato o, para los dominios ya admitidos, pre-ensayos alojados en el dominio. O bien una obligación o un plazo externo nuevo y verificable. | La medida ya no sale de contar migraciones (RP-16.8). C3 y C4 se evalúan sobre el mismo objeto: el que define la frontera de C5 (RP-16.3). |
| C4 | Permanencia | El objeto figura como elemento de primer nivel en dos ediciones sucesivas de al menos dos artefactos. La evidencia se rotula: verificada en la base de referencia de este paquete, o citada sin verificar en esta versión. | Se documenta la evidencia y se dice qué está verificado (RP-16.4). |
| C5 | Frontera clara | La regla de precedencia frente a cada dominio vecino se escribe en una oración. | Sin cambio. |
| C6 | Completitud | Un candidato que cumple C1, C2, C4 y C5 y no cumple C3 puede admitirse con reserva, como espacio en blanco: la completitud del mapa es el propósito declarado del Atlas. La reserva se revisa en la versión siguiente del catálogo con la medida de C3. | Nuevo: el argumento de completitud, que la 6.0 usó para admitir D27, pasa a ser un criterio escrito (RP-16.2). |

Definiciones que usa C1: **artefacto independiente**: Publicación con identificador y organismo emisor propios, que figura en la base de referencia del paquete. Dos ediciones del mismo artefacto cuentan una vez. Un perfil o un derivado cuenta aparte solo si lo emite otro organismo. **primer nivel**: El nivel superior de la estructura propia de cada artefacto, tal como está en el cruce de elementos y dominios: familias en NIST SP 800-53 y en CMMC; categorías en NIST CSF 2.0 (las funciones son el eje Z del Atlas); controles en CIS Controls; dominios en CSA CCM, C2M2 y CISSP; objetivos en el CAF del NCSC; requisitos en PCI DSS; pilares en los modelos de Zero Trust; prácticas en el SDL; capacidades operativas en ISO/IEC 27002; áreas de conocimiento en CyBOK. **dedicado completo**: Artefacto independiente cuyo objeto entero es el del candidato.

### 6.1 Los nueve candidatos, con la misma tabla

La tabla no aplica la misma prueba a todos con el mismo detalle, y hay que leerla sabiendo tres cosas. La celda C2 de W01 no sale del cálculo: está por decidir, porque el curador aplicó una cláusula que el criterio no trae (D-17.10). C5 no es una medida: es una frontera que escribe el curador. Y a los 28 dominios vigentes solo se les aplicaron C1 y C3 (sección 6.2).

| Código | Candidato | C1 | C2 | C3 | C4 | C5 | C6 | Resultado |
|---|---|---|---|---|---|---|---|---|
| W01 | Gobierno, riesgo y cumplimiento de la IA como dominio propio | Sí: ISO/IEC 42001, el Reglamento de IA de la UE y el Cyber AI Profile (borrador) lo tratan en primer nivel, y la base tiene además artefactos dedicados a la IA. | Por decidir. Con la prueba escrita cumpliría C2, porque sus elementos de primer nivel quedan repartidos en tres o más dominios. El curador lo dio por representable con una cláusula que el criterio no trae: el objeto ya tiene territorio propio (T07), y sus elementos reciben coordenada con T07 y D01, D02 o D03 (regla base 7 y RD-01) sin ningún ajuste de alcance. Si esa cláusula se agrega a C2 lo decide el autor (D-17.10). | No se evaluó. | No se evaluó. | No se evaluó. | Sin determinar: depende de C2. | Sigue en vigilancia |
| W02 | Gestión de activos, configuración y cambios | Sí: 16 elementos de primer nivel de 13 artefactos de 11 organismos. | Sí: 16 de esos 16 elementos solo encontraron dominio por el ajuste de alcance que la 6.0 le hizo a D13. Con la misma prueba que se aplicó a D28, el objeto no era representable. | Sí: 10 pre-ensayos en que las dos lecturas a ciegas anotan el vacío VC-05; el umbral es 10. Se alcanza justo: con uno menos no cumpliría. No hay obligación ni plazo externo nuevo. | Sí: verificado el 16-nov-2026 en la fuente del organismo emisor para 4 artefactos, en dos ediciones sucesivas de cada uno: NIST CSF (1.1 y 2.0, categoría ID.AM); NIST SP 800-53 (Rev. 4 y Rev. 5, familia CM); CIS Controls (v7.1 y v8.1, controles de inventario y de configuración segura); C2M2 (2.0 y 2.1, dominio ASSET). No se pudo verificar: ISO/IEC 27002 (2013 y 2022) (el sitio del organismo solo muestra el resumen). En NIST CSF el elemento es una categoría, que es el primer nivel para este eje según la definición del paquete; un lector que cuente como primer nivel las funciones no lo contaría. | Sí, a juicio del curador (C5 no se mide: es una frontera que se escribe): Gestión de activos, configuración y cambios cuando el objeto es el inventario, la propiedad, la línea base de configuración o el control de cambios de los activos como disciplina general; el inventario de un tipo de activo queda en el dominio de ese activo (RP-08.2) y el inventario o la configuración leídos como exposición quedan en D13 (RP-08.1 y RP-08.3). | No hace falta: cumple C1 a C5. | Admisible: cumple los cinco criterios, C3 en el límite (10 pre-ensayos y el umbral es 10). No se admite en esta versión: el cambio de catálogo no se le planteó al autor. Queda propuesto (ADR-041). |
| W03 | Seguridad del correo y la colaboración | No: 1 artefacto lo trata en primer nivel (CIS Controls, control 9). | No se evalúa: no cumple C1. | No se evalúa. | No se evalúa. | No se evalúa. | No aplica: no cumple C1. | Sigue en vigilancia; está en el alcance de D09 |
| W04 | Fraude y confianza digital | No: ningún artefacto del cruce lo trata en primer nivel. | No se evalúa: no cumple C1. | Se informa aparte: 2 pre-ensayos en que las dos lecturas a ciegas anotan el vacío VC-04. | No se evalúa. | No se evalúa. | No aplica: no cumple C1. | Sigue en vigilancia |
| W05 | Protocolos e interoperabilidad de agentes (MCP, A2A) | No: ningún artefacto del cruce lo trata en primer nivel. | No se evalúa: no cumple C1. | No se evalúa. | No: son especificaciones de 2026 sin dos ediciones sucesivas. | No se evalúa. | No aplica. | Sigue en vigilancia; está en el alcance de D20 |
| W06 | Soberanía digital y geopolítica | No se evalúa. | No: no es un objeto ni una disciplina, sino una fuerza. Está en el catálogo como CAT11 y se lee con el factor de contexto HX02. | No se evalúa. | No se evalúa. | No se evalúa. | No aplica. | Sigue en vigilancia |
| W07 | Resiliencia operativa como dominio | Sí: 5 elementos de primer nivel de 5 artefactos de 4 organismos. | No: la mitad o más de los elementos (3 de 5) está en un mismo dominio, D25, sin ajuste de alcance (D25: 3, D16: 1, D28: 1). Están en tres dominios, pero la cláusula de los tres dominios rige solo cuando ninguno aloja a la mitad. | No se evalúa: no cumple C2. | No se evalúa. | No se evalúa. | No aplica. | Sigue en vigilancia |
| W08 | Identidades no humanas y de agentes como dominio | No se evalúa. | No: la definición de D05 ya nombra las identidades no humanas. | No se evalúa. | No se evalúa. | No se evalúa. | No aplica. | Sigue en vigilancia |
| W09 | Consolidar D21, D22 y D23 (IA para la seguridad) | No, ni por separado ni en conjunto: D21 tiene un elemento de primer nivel (Cyber AI Profile, borrador) y D22, ninguno; los dos de D23 son los pilares de automatización y orquestación de los modelos de Zero Trust, que no son específicos de la IA (RD-14). | No se evalúa. | No se evalúa. | No se evalúa. | No se evalúa. | No aplica. | No se recomienda consolidar: unir los tres dominios no les da el respaldo externo que no tienen por separado. Quedan en observación. |

**El candidato W02.** Admisible: cumple los cinco criterios, C3 en el límite (10 pre-ensayos y el umbral es 10). No se admite en esta versión: el cambio de catálogo no se le planteó al autor. Queda propuesto (ADR-041). Frontera propuesta: Gestión de activos, configuración y cambios cuando el objeto es el inventario, la propiedad, la línea base de configuración o el control de cambios de los activos como disciplina general; el inventario de un tipo de activo queda en el dominio de ese activo (RP-08.2) y el inventario o la configuración leídos como exposición quedan en D13 (RP-08.1 y RP-08.3). La evidencia de C4: Sí: verificado el 16-nov-2026 en la fuente del organismo emisor para 4 artefactos, en dos ediciones sucesivas de cada uno: NIST CSF (1.1 y 2.0, categoría ID.AM); NIST SP 800-53 (Rev. 4 y Rev. 5, familia CM); CIS Controls (v7.1 y v8.1, controles de inventario y de configuración segura); C2M2 (2.0 y 2.1, dominio ASSET). No se pudo verificar: ISO/IEC 27002 (2013 y 2022) (el sitio del organismo solo muestra el resumen). En NIST CSF el elemento es una categoría, que es el primer nivel para este eje según la definición del paquete; un lector que cuente como primer nivel las funciones no lo contaría. La medida de C3 depende de que los lectores anoten un vacío, que es un instrumento ruidoso: una sola lectura lo anota en 2 pre-ensayos más. **La medida de C3 con y sin lo que el autor confirmó.** Los 10 pre-ensayos que cuenta C3 son APA-159, APC-258, APF-17, APS-18, M2.1-K01, M2.1-K03, M2.1-K08, M2.1-K09, M3.2-K05, M5.2-PA02. De ellos, 2 (M2.1-K01 y M2.1-K03) tienen un dominio que el autor confirmó el 16 de noviembre de 2026. Sin ellos la medida es 8 y el umbral es 10: C3 no se cumple, y el candidato quedaría «admisible con reserva», la situación con que la Taxonomía 6.0 admitió D27. Decir que cumple los cinco criterios depende, entonces, de contar como forzada una ubicación que el autor confirmó. Si se admite D29, esos pre-ensayos son los que se moverían. En la Taxonomía 6.0, que el autor confirmó, este candidato figuraba como «no cumple C2». El resultado cambió porque el curador reescribió el criterio en la revisión 2, no porque haya cambiado el respaldo. La decisión es del autor (D-17.2).

Cómo se calculan: Sobre el cruce de elementos y dominios, en este orden: si la mitad o más de los elementos solo encontró dominio por un ajuste de alcance, el objeto no era representable (cumple C2); si no, y la mitad o más está en un mismo dominio sin ajuste, es representable (no cumple C2); si no, y quedan repartidos en tres o más dominios, no es representable. Un elemento alojado sin ajuste de alcance cuenta como alojado por un dominio cuya definición ya nombraba el objeto. Se cuentan los pre-ensayos en que las dos lecturas a ciegas anotan el vacío del candidato. Cumple con 10 o más. El sí o el no sale de esa cuenta.

### 6.2 Dominios en observación

Dominios vigentes que no cumplirían C1 o C3 si se evaluaran hoy como candidatos. No se retira ninguno: el Atlas no tiene un criterio de retiro y esa decisión no se le planteó al autor.

| Dominio | Nombre | No cumpliría | Artefactos | Organismos | Pre-ensayos |
|---|---|---|---|---|---|
| D04 | Security Program & Investment Management | C1 | 4 | 4 | 62 |
| D07 | Privacy & Data Protection Engineering | C1 | 4 | 3 | 15 |
| D08 | Network & Infrastructure Security | C3 por corpus | 15 | 11 | 3 |
| D10 | Cloud & Platform Security | C3 por corpus | 6 | 4 | 5 |
| D11 | Application & Software Security | C3 por corpus | 21 | 14 | 8 |
| D18 | Operational Technology & Industrial Control Security | C3 por corpus | 5 | 4 | 4 |
| D19 | IoT & Cyber-Physical Systems Security | C1, C3 por corpus | 4 | 4 | 0 |
| D21 | AI for Cyber Defense & Security Operations | C1 | 1 | 1 | 15 |
| D22 | AI for Security Assessment & Testing | C1, C3 por corpus | 0 | 0 | 3 |
| D23 | AI for Security Engineering & Automation | C1, C3 por corpus | 2 | 2 | 6 |
| D26 | Cryptography, Key Management & Post-Quantum Readiness | C3 por corpus | 8 | 6 | 5 |
| D27 | Physical, Environmental & Facility Security | C3 por corpus | 7 | 7 | 1 |

### 6.3 La prueba del cruce de territorios

De 80 elementos del cruce, 51 son externos y 29 son de marcos del autor. De los externos, 18 (35,3 %) necesitan dos o más territorios. La prueba falla si más de la mitad de los elementos externos necesita dos o más territorios (el eje no discriminaría) o si algún territorio no es primario de ningún elemento externo. Resultado: No falla por la primera condición; falla por la segunda: T01 no es primario de ningún elemento externo. El umbral se fijó conociendo la proporción del conjunto completo (35 de 80), no la de los elementos externos.

| Territorio | T01 | T02 | T03 | T04 | T05 | T06 | T07 | T08 |
|---|---|---|---|---|---|---|---|---|
| Elementos externos de los que es primario | 0 | 2 | 6 | 8 | 16 | 10 | 3 | 6 |

La prueba estaba escrita para poder fallar, y falla para T01: no es el territorio primario de ningún elemento externo. Ese territorio lo sostienen las fuentes del autor (su biblioteca) y no los marcos externos de la base. El curador no cambió nada por eso, y tampoco le dio a T01 el estado «en observación» que reciben los dominios que no cumplen C1 o C3. Qué se hace con T01 lo decide el autor (D-17.8).

## 7. El MCCS, las lentes y los planos

### 7.1 El MCCS

Metacognitive CISO System. Según el autor (16-nov-2026), el MCCS son los 1.404 elementos de su biblioteca metacognitiva: modelos mentales, sesgos cognitivos, mindsets y las demás categorías, once en total. La declaración del autor: «el MCCS son los 1404 elementos relacionados a modelos mentales, sesgos cognitivos, mindsets y otras categorias del metacognitivecisosystem» (16-nov-2026).

| Categoría | Elementos | Pilar que le asigna el Atlas |
|---|---|---|
| Sesgo cognitivo | 430 | MM 430 |
| Capacidad cognitiva | 121 | MM 121 |
| Práctica de decisión | 147 | MM 147 |
| Función ejecutiva | 23 | OS 23 |
| Factor humano | 62 | MM 26, OS 36 |
| Falacia lógica | 45 | MM 45 |
| Modelo mental | 199 | MM 199 |
| Metacognición y juicio epistémico | 61 | MM 61 |
| Mindset | 141 | MM 141 |
| Otro constructo cognitivo | 90 | MM 90 |
| Habilidad socioemocional | 85 | MM 85 |

La lente de cuatro pilares (MM, OS, DO y NX) es la forma en que el Atlas proyecta el MCCS sobre los pre-ensayos (ADR-017, aceptada). De los cuatro, la biblioteca tiene elementos en dos: MM y OS a escala individual. DO y NX no tienen elementos en la biblioteca.

| Pilar | Nombre | Definición | Elementos en la biblioteca | Ancla primaria | Anclas secundarias | De dónde salen las anclas |
|---|---|---|---|---|---|---|
| MM | Modelos mentales | Cómo se piensa y se decide: metacognición, sesgos, marcos de razonamiento e higiene de decisión. | 1.345 | T01 | T04, T03 | derivadas de los territorios que traen los elementos de la biblioteca |
| OS | Sistema operativo | Qué sostiene la calidad de la decisión: a escala individual, energía, atención y resiliencia; a escala de oficina, derechos de decisión, cadencias, datos, agentes y evidencia. | 59 | T01, T04 | T07, T05, T06, T08, T02 | derivadas de los territorios que traen los elementos de la biblioteca |
| DO | Entrega y operación | Cómo el criterio se convierte en resultados: arquitectura, programas, operación y comunicación ejecutiva. | ninguno | T05, T06 | T03, T08 | hipótesis de diseño: el pilar no tiene elementos en la biblioteca |
| NX | Evolución | Cómo se adapta el sistema: exploración, adopción de IA y agentes, antifragilidad y legado. | ninguno | T07 | T03 | hipótesis de diseño: el pilar no tiene elementos en la biblioteca |

**Pregunta para el autor (D-17.1).** Que DO y NX no tengan elementos de la biblioteca es el resultado de una regla del curador, y no un dato de la biblioteca: la regla de pilar de la versión 1.2 solo asigna MM u OS, y no toma el pilar de la base del autor. OS a escala de oficina tampoco tiene elementos de la biblioteca, y es donde están casi todos los pre-ensayos del pilar. Queda por decidir si DO, NX y OS de oficina son parte del MCCS, o si son solo la lente con que el Atlas ordena los pre-ensayos, y si la regla de pilar queda como está.

### 7.2 La lente de la agenda de IA

En los pre-ensayos la lente se deriva de la coordenada con la regla de cada pilar (RD-21) y no se asigna a mano. En las preguntas del banco, la lente es la que traía la matriz de origen. Los indicadores no la llevan todavía, aunque RD-21 los nombra: es un pendiente declarado.

| Pilar | Nombre | Regla |
|---|---|---|
| IA-P1 | Seguridad de la IA | Dominio D20, o territorio T07 con dominio D01, D02, D03 o D28. |
| IA-P2 | IA para la seguridad | Dominio D21, D22 o D23. |
| IA-P3 | IA adversaria | Dominio D12 con T07 como territorio primario o secundario, o con D20 como dominio secundario. |

### 7.3 Los planos

| Plano | Qué contiene |
|---|---|
| Plano A: corpus académico | Conceptos, pre-ensayos y, a futuro, ensayos. Agnóstico de proveedor. |
| Plano B: capacidades contratadas | Instancias de dominio del GM-24 V7.1 (tareas, agentes, herramientas). No prueba el corpus académico. |

Llevan plano los tipos que pertenecen a uno de los dos por definición. Los catálogos de la taxonomía, la base de referencia, los indicadores y los objetivos no pertenecen a ningún plano y no llevan la propiedad. Tipos del plano A: `Concept`, `Precursor`, `Essay`, `Question`, `LearningUnit`, `LearningPath`, `Competency`, `MentalModel`, `CognitiveBias`, `LogicalFallacy`, `MetacognitivePractice`, `HumanCapability`, `CognitiveState`. Tipos del plano B: `ControlProduct`, `TechnologyProduct`, `ProductPractice`, `OperatingModel`, `OperationalPractice`, `AIAgent`, `AgentFleet`, `AgentCharter`, `ApprovalGate`, `KnowledgeSource`, `AgentSkill`, `Tool`, `OperatingAuthorization`, `Role`, `SecurityControl`.

Un pre-ensayo que nombra un producto o un proveedor no pasa al plano B: queda marcado y fuera de la promoción a ensayo hasta que se reescriba (RD-22). Hoy son 77.

## 8. Fuentes que se verificaron para decidir

| Fuente | Organismo | Fecha | Dónde | Verificado |
|---|---|---|---|---|
| The NIST Cybersecurity Framework (CSF) 2.0, NIST CSWP 29 | NIST | 26 de febrero de 2024 | https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf | 2026-11-16 |
| Glosario del CSRC de NIST, término «operational technology», definición de NIST SP 800-82r3 | NIST | — | https://csrc.nist.gov/glossary/term/operational_technology | 2026-11-16 |
| Glosario del CSRC de NIST, término «IoT device», definición de NISTIR 8425 | NIST | — | https://csrc.nist.gov/glossary/term/iot_device | 2026-11-16 |
| Biblioteca metacognitiva del autor: «Biblioteca cognitiva CISO: 1.404 conceptos explicados y puente GM-24» (corte 12-nov-2026) y «Biblioteca completa para el CISO de frontera» (1.356 conceptos, 8-nov-2026) | el autor | — | — | 2026-11-16 |

Las citas literales que respaldan cada regla están en el catálogo (`data/taxonomia_v6_1.json`, clave `revision_1_4.fuentes_verificadas`).

## 9. Lo que queda en manos del autor

| N.º | Qué se le pide | Respuestas posibles |
|---|---|---|
| D-16.3 | La mejora continua pasa a la función Identificar con el código nuevo ID06, y RC04 queda para las lecciones y el cierre de una recuperación (opción a de RP-13). Son 35 subfunciones. Los 10 pre-ensayos que tenían RC04 tomaron el valor en que coinciden dos lecturas, con cualquier confianza, y pasan a ID06: en 4, alguna lectura no declaró confianza alta. RC04 se retiró también de las subfunciones secundarias, que no se releyeron. | sí / no: prefiero la opción b (se mantiene RC04) |
| D-16.5 | Las reglas RD-01 a RD-14, que recibieron los lectores: adoptar, modificar o rechazar cada una. Resuelven los seis puntos de la revisión y las preguntas de dominio y de subfunción. La planilla trae, por regla, cuántos cambios la citan, lo que los lectores señalaron de ella y lo que observó la revisión de la versión candidata. | por regla: adoptar / modificar / rechazar |
| D-16.6 | Las reglas RD-20 a RD-24, que no son de lectura y salen de cinco de las once preguntas: el pilar del liderazgo de personas, la lente de la agenda de IA, el plano de los pre-ensayos con marca, la biblioteca sin dominio y el eje del aseguramiento. | por regla: adoptar / modificar / rechazar |
| D-16.4 | Dos cambios de catálogo del eje H: H04 deja de ser un horizonte y pasa a ser el marcador de convergencia (RP-15.6); INH11 pasa a llamarse «Volumen de alertas y de decisiones» (RP-15.2). | por cambio: sí / no |
| D-16.7 | El modelo de equilibrio del eje H, revisión 2: contexto y fuerza definidos, «presiona» con término y sentido, «regula» con papel, seis vínculos nuevos para las cinco fuerzas que no presionaban nada y escalas para HX01 a HX07. | sí / no |
| D-16.8 | Los criterios de admisión de dominios, revisión 2 (C1 a C6), y la tabla de los nueve candidatos. Reescribí el criterio C2, y con eso cambió el resultado del candidato W02 respecto de la Taxonomía 6.0. C5 no es una medida: es una frontera que escribí. La celda C2 del candidato W01 no sale del cálculo y queda por decidir (D-17.10). | sí / no |
| D-16.9 | Dos definiciones de la taxonomía: el plano como propiedad del nodo, y las cinco familias de dominios. | por cada una: sí / no |
| D-16.13 | Registré tu declaración: el MCCS son los 1.404 elementos de la biblioteca. Conservé la lente de cuatro pilares como lente del Atlas y derivé de la biblioteca las anclas de MM y de OS. Las anclas derivadas de OS son T01 y T04: ya no incluyen T03, que en D-04 habías aceptado para la escala de oficina. Las anclas de la Taxonomía 6.0 se conservan al lado. | sí / no |
| D-17.1 | Con la regla de pilar que escribí en la versión 1.2, que a los elementos de tu biblioteca solo les asigna MM u OS, ningún elemento queda en DO ni en NX. OS a escala de oficina tampoco tiene elementos de la biblioteca, y es donde están casi todos los pre-ensayos del pilar. ¿DO, NX y OS de oficina son parte del MCCS, o son la lente con que el Atlas ordena los pre-ensayos? ¿Y la regla de pilar queda como está? | parte del MCCS / solo lente del Atlas; la regla de pilar: queda / se revisa |
| D-17.2 | Admitir el candidato W02 como dominio D29 «Gestión de activos, configuración y cambios». Cumple C1, C2, C4 y C5. C3 da 10 pre-ensayos, justo el umbral, contando 2 cuyo dominio confirmaste el 16 de noviembre; sin ellos da 8 y no se cumple: quedaría admitido con reserva, como D27. Si se admite, los pre-ensayos que cuenta C3 son los que se moverían. | sí / no |
| D-17.3 | Admitir las variables homeostáticas propuestas: HV07 (calidad de la decisión frente a la incertidumbre) y HV08 (costo del programa frente al valor demostrado). No tienen el mismo respaldo: HV07 cumple los cuatro criterios, y HV08 cumple tres y el cuarto en parte, y conviene decidirla junto con el nombre de HV04. Los vínculos que las sostendrían son supuestos del curador. | por variable: sí / no |
| D-17.4 | Los 15 vacíos declarados: casos para los que ninguna regla decide. Para cada uno se puede decidir una regla o dejarlo como vacío. Los lectores señalaron además casos sin regla que no están entre los declarados. | por vacío: regla … / queda como vacío |

# Reglas y catálogos para la lectura (Frontier CISO Atlas · Taxonomía 6.0 con las reglas adoptadas el 16 de noviembre de 2026)

Los códigos son los de la Taxonomía 6.0. Las reglas base (R1 a R8) son las de la 6.0. Los enunciados RP son los que el autor adoptó el 16-nov-2026: precisan las reglas base y, donde las precisan, prevalecen.

## Territorios (eje X: de quién es la perspectiva o la responsabilidad)

- **T01 SELF & JUDGMENT**: Criterio individual, metacognición, sesgos y decisiones. Explicita el sistema operativo personal del líder (energía, atención, carga cognitiva) y la higiene de decisión. Ancla de MCCS-MM y de MCCS-OS a escala individual.
- **T02 LEADERSHIP & ORGANIZATION**: Personas, incentivos, roles, cultura, liderazgo y accountability. Incluye la fuerza de trabajo híbrida (personas, agentes y proveedores), la distribución de autoridad y la gestión de agentes como equipo.
- **T03 STRATEGY & BUSINESS**: Outcomes, estrategia, inversión y priorización empresarial. Incluye el sistema operativo de la oficina del CISO, el producto-control como unidad de valor y la economía de la automatización (costo por tarea, capacidad liberada).
- **T04 RISK & RESILIENCE**: Exposición, escenarios, apetito, continuidad y riesgo de transición. Incluye riesgo sistémico y de concentración, y el riesgo de las transiciones tecnológicas (IA, agentes, criptografía poscuántica).
- **T05 SECURITY ARCHITECTURE**: Diseño de controles, Zero Trust, ingeniería y fronteras técnicas. Sin cambio de significado. Su disciplina transversal ahora tiene dominio propio (D25).
- **T06 SECURITY OPERATIONS**: SOC, monitoreo, investigación, respuesta y operación. Incluye la operación por cadencias de productos-control y el SOC agéntico (humanos y agentes en la misma cola).
- **T07 AI & AUTONOMOUS SYSTEMS**: Modelos, agentes, autonomía, herramientas y autoridad no humana. Sin cambio de significado. No se asigna por mera mención de IA. No absorbe otras tecnologías de frontera: esas se expresan con H.
- **T08 TRUST & ASSURANCE**: Evidencia, auditoría, legitimidad, confiabilidad y transparencia. Sin cambio de significado. Su disciplina transversal ahora tiene dominio propio (D28).

## Dominios (eje Y: disciplina u objeto)

- **D01 Cybersecurity Governance**: Políticas, dirección, responsabilidades y supervisión. *Alcance 6.0:* Incluye el gobierno de la IA y de los agentes. (ver RP-04).
- **D02 Cyber Risk Management**: Identificación, evaluación, tratamiento y aceptación del riesgo. *Alcance 6.0:* Incluye el riesgo de la IA y de los agentes, y la cuantificación y transferencia del riesgo. (ver RP-04).
- **D03 Compliance & Regulatory Security**: Obligaciones aplicables y su conformidad, incluida la auditoría de conformidad con una obligación (RP-03.1). *Alcance 6.0:* Se delimita a las obligaciones (legales, regulatorias, contractuales) y su conformidad. La evidencia de eficacia, las pruebas y la medición van a D28.
- **D04 Security Program & Investment Management**: Portafolio, presupuesto, prioridades y valor. *Alcance 6.0:* Incluye el modelo operativo de la oficina, el portafolio de productos-control y la economía de agentes.
- **D05 Identity & Access Security**: Identidades humanas/no humanas, autenticación, autorización y PAM. *Alcance 6.0:* Explicita identidades de cargas de trabajo y de agentes.
- **D06 Data Security & Information Protection**: Clasificación, DLP, cifrado y protección de información. *Alcance 6.0:* AJUSTE: el cifrado como control sobre los datos permanece; la disciplina criptográfica (claves, PKI, agilidad, transición poscuántica) pasa a D26.
- **D07 Privacy & Data Protection Engineering**: Finalidad legítima, minimización, derechos y tratamiento de datos personales.
- **D08 Network & Infrastructure Security**: Redes, segmentación y componentes de infraestructura.
- **D09 Endpoint & Workplace Security**: Endpoints, dispositivos de usuario y puesto de trabajo. *Alcance 6.0:* AJUSTE: el puesto de trabajo incluye de forma explícita el correo, la colaboración y la navegación.
- **D10 Cloud & Platform Security**: Cloud, servicios de plataforma, workloads y configuraciones.
- **D11 Application & Software Security**: Aplicaciones, SDLC, DevSecOps y seguridad de código.
- **D12 Threat Intelligence & Threat Modeling**: Adversarios, TTP, escenarios y modelado de amenazas. *Alcance 6.0:* Incluye el uso adversarial de la IA.
- **D13 Vulnerability & Exposure Management**: Descubrimiento, evaluación y reducción de exposición. *Alcance 6.0:* AJUSTE: explicita el inventario de activos, la configuración segura y la postura como insumos de la exposición.
- **D14 Security Monitoring & Detection**: Telemetría, reglas, analítica, detección y hunting. *Alcance 6.0:* Incluye la observabilidad de agentes.
- **D15 Incident Response & Crisis Management**: Investigación, contención, erradicación y coordinación de crisis.
- **D16 Business Continuity & Cyber Recovery**: Continuidad, restauración y recuperación comprobada.
- **D17 Third-Party & Supply Chain Security**: Proveedores, dependencias y cadena de suministro. *Alcance 6.0:* AJUSTE: explicita la cadena de suministro de software y de IA (componentes, modelos, conectores) y el riesgo de concentración.
- **D18 Operational Technology & Industrial Control Security**: ICS/SCADA/PLC, procesos industriales, safety y continuidad OT.
- **D19 IoT & Cyber-Physical Systems Security**: Dispositivos conectados y sistemas ciberfísicos no exclusivamente industriales.
- **D20 AI & Agent Security**: Proteger modelos, agentes, herramientas, datos y runtime de IA. *Alcance 6.0:* Nota de alcance: cede a D01, D02 y D03 el gobierno, el riesgo y el cumplimiento de la IA (regla 7); incluye los protocolos y pasarelas de agentes (MCP, A2A) y la memoria de agentes como superficie.
- **D21 AI for Cyber Defense & Security Operations**: IA para detectar, investigar, priorizar y responder.
- **D22 AI for Security Assessment & Testing**: IA para pruebas autorizadas, evaluación y descubrimiento de debilidades. *Alcance 6.0:* Precedencia: la IA como instrumento de evaluación es D22; la disciplina de aseguramiento es D28.
- **D23 AI for Security Engineering & Automation**: IA para crear reglas, políticas, configuraciones y automatizaciones.
- **D24 Security Workforce & Human Factors**: Profesión, talento, cultura, sesgos y capacidades humanas. *Alcance 6.0:* AJUSTE: explicita la fuerza de trabajo híbrida (personas y agentes), las competencias y el riesgo humano.
- **D25 Enterprise Security Architecture & Zero Trust**: Arquitectura empresarial de seguridad, principios y modelos de referencia, estrategia Zero Trust, seguro por diseño y por defecto, e ingeniería de resiliencia. *Alcance 6.0:* NUEVO en 6.0.
- **D26 Cryptography, Key Management & Post-Quantum Readiness**: Inventario criptográfico, PKI y certificados, gestión de claves y secretos, agilidad criptográfica y transición poscuántica. *Alcance 6.0:* NUEVO en 6.0.
- **D27 Physical, Environmental & Facility Security**: Seguridad física de instalaciones y centros de datos, protección ambiental, mantenimiento y soportes, y su evidencia como dependencia del control (incluida la del proveedor de nube). *Alcance 6.0:* NUEVO en 6.0.
- **D28 Security Assurance, Testing & Measurement**: Evaluación de controles, pruebas técnicas (pruebas de penetración, equipos rojo y púrpura, validación continua), auditoría y atestaciones, métricas, indicadores y evidencia de eficacia. *Alcance 6.0:* Nuevo en 6.0. La auditoría como disciplina, con sus atestaciones, es D28 (RP-03.2).

## Funciones y subfunciones (eje Z)

La función sale de la subfunción. Cada subfunción tiene una definición de trabajo: qué incluye, qué excluye y, si la hay, qué frontera no está decidida.

**GV Gobernar** — Gobierno de estrategia, responsabilidades y riesgo.

- **GV01 Contexto empresarial y estrategia** [GV.OC]. Incluye: El contexto del negocio (misión, objetivos, partes interesadas) y la estrategia de seguridad que se deriva de él. Excluye: Las obligaciones legales y contractuales (GV06) y la criticidad y las dependencias del negocio (ID02).
- **GV02 Estructura de gobierno y autoridad** [GV.RR]. Incluye: La estructura de gobierno: roles, responsabilidades, autoridad y derechos de decisión; para los agentes, quién supervisa y con qué nivel de autonomía. Excluye: Las sesiones de órganos con acta y decisiones (GV07) y la gestión del programa y de sus recursos (GV05). Sin decidir: El liderazgo y el diseño de roles del equipo en D24, que hoy se reparte entre GV02, GV10 y PR05 (hallazgo C4d-014).
- **GV03 Políticas y estándares** [GV.PO]. Incluye: Las políticas, los estándares y las normas internas: su aprobación, comunicación y actualización; para los agentes, la política que fija los niveles de autonomía y el interruptor. Excluye: Las obligaciones externas (GV06). Sin decidir: El procedimiento, que también nombra PR05 (hallazgo C4d-010).
- **GV04 Apetito, tolerancia y aceptación de riesgo** [GV.RM]. Incluye: La estrategia de gestión del riesgo: apetito, tolerancia y aceptación. Excluye: La identificación de amenazas y exposición (ID03) y el análisis y la cuantificación del riesgo con el seguimiento de su tratamiento (ID04). Sin decidir: La elección de la respuesta al riesgo (mitigar, transferir, seleccionar controles), que ninguna subfunción nombra (hallazgo C4d-001).
- **GV05 Gobierno de programas, recursos e inversión** [GV.RR · GV.OV]. Incluye: El gobierno del programa de seguridad: portafolio, recursos, presupuesto e inversión, y las cadencias de gestión del programa. Excluye: Las sesiones de órganos con acta y decisiones (GV07).
- **GV06 Obligaciones legales y contractuales** [GV.OC]. Incluye: La identificación y la gestión de las obligaciones legales, regulatorias y contractuales. Excluye: El contexto del negocio y la estrategia (GV01) y las notificaciones obligatorias de un incidente (RS03).
- **GV07 Supervisión y reporting ejecutivo** [GV.OV]. Incluye: La supervisión por la dirección y por los órganos de gobierno: sesiones con acta y decisiones, informes ejecutivos y revisión del desempeño de la estrategia. Excluye: Las cadencias de gestión del programa (GV05) y la revisión independiente (GV08).
- **GV08 Assurance y revisión independiente** [GV.OV]. Incluye: El aseguramiento y la revisión independiente: auditoría interna y externa, atestaciones y evaluación por terceros. Excluye: El informe ejecutivo de gestión (GV07). Sin decidir: La prueba o la medición de eficacia que no es independiente ni de detección ni de recuperación: ID05 o GV08 (hallazgo C4d-012).
- **GV09 Gobierno de terceros y ecosistemas** [GV.SC]. Incluye: El gobierno de proveedores, terceros y ecosistemas: estrategia, requisitos, contratos y supervisión de la cadena de suministro. Excluye: La coordinación de un incidente con terceros (RS04).
- **GV10 Ética, cultura y rendición de cuentas** [GV.RR · GV.OC]. Incluye: La ética, la cultura de seguridad y la rendición de cuentas. Excluye: La estructura formal de roles y autoridad (GV02) y la formación de las personas (PR05). Sin decidir: El liderazgo y la calidad de la decisión individual en D24 (hallazgo C4d-014).

**ID Identificar** — Conocer activos, exposición, dependencias y riesgos.

- **ID01 Inventario y clasificación de activos** [ID.AM]. Incluye: El inventario, la clasificación y la propiedad de los activos: equipos, software, datos, servicios, identidades y sistemas de IA. Excluye: La criticidad y las dependencias del negocio (ID02).
- **ID02 Dependencias y criticidad del negocio** [ID.AM · GV.OC]. Incluye: Las dependencias, la criticidad y el impacto en el negocio de los activos y los servicios. Excluye: El inventario (ID01) y el análisis de escenarios de riesgo (ID04).
- **ID03 Amenazas, vulnerabilidades y exposición** [ID.RA]. Incluye: La identificación de amenazas, vulnerabilidades y exposición técnica; el escenario de amenaza, con el adversario y sus técnicas. Excluye: El análisis y la cuantificación del riesgo (ID04).
- **ID04 Análisis de escenarios y cuantificación de riesgos** [ID.RA]. Incluye: El análisis y la cuantificación del riesgo, el escenario de riesgo con la pérdida y su probabilidad, y el seguimiento del tratamiento. Excluye: La identificación de amenazas y exposición (ID03) y la decisión de apetito, tolerancia y aceptación (GV04).
- **ID05 Evaluación de capacidades y brechas** [ID.IM]. Incluye: La evaluación de capacidades, de madurez y de brechas, y las mejoras que identifica. Excluye: La evaluación de la detección (DE04) y la validación de la recuperación (RC03). Sin decidir: La mejora continua que no nace de un incidente (pregunta RP-13 y hallazgo C4d-002) y la prueba de eficacia que no es independiente (hallazgo C4d-012).

**PR Proteger** — Implementar salvaguardas.

- **PR01 Identidad y autorización** [PR.AA]. Incluye: La gestión de identidades, la autenticación, la autorización y el control de acceso de personas, cargas de trabajo y agentes. Excluye: El acceso físico a las instalaciones (PR06).
- **PR02 Protección de datos y privacidad por diseño** [PR.DS]. Incluye: La protección de los datos en reposo, en tránsito y en uso, y la privacidad por diseño. Excluye: El control de acceso (PR01). Sin decidir: Los respaldos, que caben también en RC01 (hallazgo C4d-015).
- **PR03 Hardening y arquitectura segura** [PR.PS · PR.IR]. Incluye: La arquitectura segura, el hardening y la segmentación (PR.PS y PR.IR-01). Excluye: La resiliencia de la infraestructura y la protección física y ambiental (PR06) y el desarrollo seguro y la gestión de cambios (PR04).
- **PR04 Desarrollo seguro y gestión de cambios** [PR.PS]. Incluye: El desarrollo seguro de software y la gestión de cambios y de configuración a lo largo del ciclo de vida. Excluye: El hardening y la arquitectura (PR03).
- **PR05 Preparación de personas y procedimientos** [PR.AT]. Incluye: La concientización, la formación y la preparación de las personas, y los procedimientos que usan quienes ejecutan. Excluye: La cultura y la rendición de cuentas (GV10). Sin decidir: El procedimiento como documento normativo, que también cabe en GV03 (hallazgo C4d-010).
- **PR06 Resiliencia de la infraestructura y protección física y ambiental** [PR.IR]. Incluye: La resiliencia de la infraestructura y la protección física y ambiental: las medidas previas al evento (PR.IR-02 a PR.IR-04, con PR.AA-06, DE.CM-02 y PR.PS-03 como referencias de subcategoría). Excluye: La operación degradada durante el incidente (RC02) y la segmentación (PR03).

**DE Detectar** — Identificar condiciones y eventos adversos.

- **DE01 Telemetría y observabilidad** [DE.CM]. Incluye: La telemetría, el monitoreo continuo y la observabilidad de redes, sistemas, personas, proveedores y agentes. Excluye: La construcción y la operación de las detecciones (DE02).
- **DE02 Ingeniería de detección y análisis** [DE.AE]. Incluye: Construir y operar la detección: reglas, analítica, correlación y análisis de eventos adversos. Excluye: Ponerla a prueba y buscar lo que no detecta (DE03) y medir su cobertura y su calidad (DE04).
- **DE03 Hunting, validación y mejora de detecciones** [DE.AE · DE.CM]. Incluye: Poner a prueba la detección y buscar lo que no detecta: hunting, validación y mejora de las detecciones. Excluye: Construirla y operarla (DE02) y medir su cobertura y su calidad (DE04).
- **DE04 Evaluación de cobertura y calidad de detección** [DE.AE · ID.IM]. Incluye: Medir la cobertura y la calidad de la detección. Excluye: La evaluación general de capacidades (ID05).

**RS Responder** — Gestionar incidentes y limitar consecuencias.

- **RS01 Preparación y coordinación de respuesta** [RS.MA]. Incluye: La preparación y la coordinación de la respuesta: plan, roles, triaje y priorización de incidentes. Excluye: La contención y la erradicación (RS02) y la comunicación de crisis (RS03).
- **RS02 Contención, erradicación y preservación de evidencia** [RS.MI · RS.AN]. Incluye: El análisis del incidente, la contención, la erradicación y la preservación de la evidencia. Excluye: El triaje y la priorización (RS01).
- **RS03 Comunicación de crisis y decisiones ejecutivas** [RS.CO]. Incluye: La comunicación de crisis, las decisiones ejecutivas durante el incidente y las notificaciones obligatorias. Excluye: La coordinación con terceros y las notificaciones contractuales (RS04) y la comunicación de la recuperación (RC05).
- **RS04 Gestión de incidentes con terceros** [RS.CO · GV.SC]. Incluye: La coordinación del incidente con terceros, incluidas las notificaciones contractuales. Excluye: El gobierno de terceros fuera del incidente (GV09).

**RC Recuperar** — Restaurar servicios y capacidades.

- **RC01 Restauración y recuperación técnica** [RC.RP]. Incluye: La capacidad técnica de restaurar, con sus objetivos de tiempo y de punto de recuperación. Excluye: La continuidad durante la perturbación (RC02) y la validación del retorno (RC03). Sin decidir: Los respaldos como protección del dato, que caben también en PR02 (hallazgo C4d-015).
- **RC02 Continuidad y operación degradada** [RC.RP]. Incluye: La continuidad del negocio y la operación degradada durante la perturbación. Excluye: Las medidas de resiliencia previas al evento (PR06) y la restauración técnica (RC01).
- **RC03 Validación de recuperación y retorno seguro** [RC.RP]. Incluye: La validación de la recuperación y del retorno seguro a la operación. Excluye: La restauración (RC01).
- **RC04 Aprendizaje, corrección y mejora continua** [ID.IM]. Incluye: El aprendizaje posterior al incidente, la corrección y la mejora continua. Sin decidir: Si la mejora continua queda bajo la función Recuperar (pregunta RP-13) y a qué subfunción va la que no nace de un incidente (hallazgo C4d-002).
- **RC05 Comunicación de la recuperación y restitución de la confianza** [RC.CO]. Incluye: La comunicación de la recuperación a las partes interesadas y la restitución de la confianza. Excluye: La comunicación durante la crisis (RS03).

## Reglas base de la Taxonomía 6.0

- **R1.** La tesis manda: se clasifica por el objeto y la tesis, no por palabras sueltas. La mera mención de IA no lleva a T07 ni a D20–D23.
- **R2.** Cardinalidad: un territorio primario y hasta 2 secundarios; un dominio primario y hasta 3 secundarios; una subfunción primaria y hasta 2 secundarias; un horizonte o «indeterminado»; como máximo 1 catalizador, 1 inhibidor y 2 mecanismos homeostáticos, solo si el texto los nombra; un pilar MCCS.
- **R3.** D25 cuando el objeto es la arquitectura o un principio transversal; si es el control de un pilar concreto, queda en el dominio del pilar.
- **R4.** D26 cuando el objeto es la disciplina criptográfica; el cifrado como un control más de protección de datos queda en D06.
- **R5.** D27 cuando el objeto es la seguridad física, ambiental o de instalaciones, o el mantenimiento como dependencia del control.
- **R6.** D28 cuando el objeto es el método para demostrar o medir la eficacia; la obligación y su conformidad quedan en D03; el riesgo con la métrica como medio queda en D02; la IA como instrumento de prueba queda en D22.
- **R7.** Gobierno, riesgo y cumplimiento de la IA: D01, D02 o D03 con territorio T07.
- **R8.** Plano B: una instancia de dominio se ubica en el dominio del Atlas que indica lentes.plano_b y no se usa como evidencia del corpus académico.

## Enunciados adoptados el 16-nov-2026

Se citan por su código (por ejemplo, RP-09.1).


**RP-01 · Precedencia general entre disciplina y objeto**

- **RP-01.1** (dominio): Cuando la tesis aplica una disciplina (gobierno, riesgo, cumplimiento, monitoreo, respuesta, continuidad o aseguramiento) a un objeto que tiene dominio propio (identidad, datos, nube, OT, IoT o IA), el dominio primario es el de la disciplina y el del objeto queda como secundario.
- **RP-01.2** (dominio): El dominio del objeto es primario cuando la tesis trata el control técnico propio de ese objeto.

**RP-02 · Regla 6: cláusula de pilar y fronteras de D28**

- **RP-02.1** (dominio): D28 es primario cuando la tesis discute la validez del método de prueba, de medición o de evidencia.
- **RP-02.2** (dominio): Si lo que se prueba o se mide es la eficacia de una capacidad concreta que tiene dominio propio, queda en el dominio de esa capacidad con D28 como secundario.
- **RP-02.3** (dominio): El destinatario del texto («ante el auditor», «debe poder demostrar») no cambia el dominio.
- **RP-02.4** (dominio): La evidencia de cumplimiento de una obligación queda en D03; la gestión de la evidencia como disciplina es D28.
- **RP-02.5** (dominio): La auditoría de la gestión del riesgo es D28; la validación de un modelo de cuantificación queda en D02.
- **RP-02.6** (dominio): El aseguramiento de una arquitectura o de un principio es D28; su diseño es D25.
- **RP-02.7** (dominio): La evidencia sobre controles físicos es D27 cuando el objeto es el control y D28 cuando es el método.

**RP-03 · La auditoría en D03 y en D28**

- **RP-03.1** (dominio (definición de D03)): Definición de D03: «Obligaciones aplicables y su conformidad, incluida la auditoría de conformidad con una obligación».
- **RP-03.2** (dominio): La auditoría como disciplina, con sus atestaciones, es D28.

**RP-04 · Regla 7: desempate, territorio y alcance**

- **RP-04.1** (dominio): Gobierno, riesgo y cumplimiento de la IA: D01 cuando la tesis decide quién autoriza, por qué ruta y con qué límites; D02 cuando identifica, cuantifica, acepta o transfiere el riesgo; D03 cuando trata una obligación.
- **RP-04.2** (territorio): El territorio es T07 salvo que la tesis adopte otra perspectiva: T07 es la consecuencia habitual de la regla, no su condición.
- **RP-04.3** (dominio): El mecanismo técnico que hace cumplir la autonomía (interruptor, límites de lote, compuertas en el entorno de ejecución) queda en D20.
- **RP-04.4** (dominio): El aseguramiento de la IA (pruebas, evaluación y evidencia de sus controles) es D28; la IA como instrumento de prueba es D22 cuando la tesis trata lo que la IA aporta a la prueba.
- **RP-04.5** (dominio): D21 y D23 llevan frente a D14, D15, D11 y D13 la misma precedencia que D22 frente a D28.
- **RP-04.6** (dominio y territorio): La regla de uso de herramientas de IA por los empleados es D01 con T07; su control técnico es D06 o D09.
- **RP-04.7** (subfunción): Cuando el dominio cambia por esta regla, la subfunción se revisa con él.

**RP-05 · Regla 3: qué es un pilar y qué es un principio transversal**

- **RP-05.1** (dominio): «Pilar» designa un dominio de protección o de ecosistema con objeto propio (D05 a D11 y D18 a D20).
- **RP-05.2** (dominio): Son principios transversales Zero Trust, seguro por diseño y por defecto, defensa en profundidad, mínimo privilegio como principio y resiliencia por diseño.
- **RP-05.3** (dominio): La arquitectura de referencia es D25 aunque su alcance sea un solo dominio; el control que la implementa queda en el pilar.
- **RP-05.4** (dominio): En el acceso Zero Trust, el control que decide quién accede va a D05 y el que define por dónde va a D08.
- **RP-05.5** (dominio): La ingeniería de seguridad de sistemas es D25.

**RP-06 · Regla 4: fronteras de D26**

- **RP-06.1** (dominio): Las claves, los certificados y los secretos como material criptográfico son D26.
- **RP-06.2** (dominio): La identidad de máquina que los usa es D05.
- **RP-06.3** (dominio): La detección de la fuga de secretos es D06 o D11.
- **RP-06.4** (dominio): El cifrado de red como control queda en D08 y el cifrado de datos como control, en D06.

**RP-07 · Regla 5: fronteras de D27**

- **RP-07.1** (dominio): Frente a D08, D27 es la instalación y D08 la infraestructura lógica.
- **RP-07.2** (dominio): Frente a D06, el destino y la sanitización de los soportes es D27 y la protección de los datos que contienen es D06.
- **RP-07.3** (dominio): La evidencia física del proveedor es D27 cuando el objeto es el control físico y D17 cuando es la relación con el proveedor.
- **RP-07.4** (dominio): Los sistemas de edificio conectados son D19 cuando el objeto es el dispositivo y D27 cuando es la instalación.

**RP-08 · Inventario, activos, configuración y ciclo de vida de los controles**

- **RP-08.1** (dominio): El inventario como insumo de la exposición es D13.
- **RP-08.2** (dominio): El inventario de un tipo de activo queda en el dominio de ese activo.
- **RP-08.3** (dominio): La configuración es D13 cuando la postura es transversal a los entornos y D10 cuando es específica de la plataforma de nube.

**RP-09 · Territorios: de quién es la perspectiva y desempates**

- **RP-09.1** (territorio): El territorio sigue al objeto de la tesis; el interlocutor ante quien responde el CISO no lo cambia.
- **RP-09.2** (territorio): T02 cuando lo que se diseña es el rol, la carga o la competencia de las personas que supervisan agentes; T07 cuando es la autoridad del agente.
- **RP-09.3** (territorio): Para D01 fuera de la IA: T02 si la tesis es quién decide y quién responde, T03 si es cómo opera la oficina y T08 si es cómo se demuestra.
- **RP-09.4** (territorio): Para D17: T04 cuando la tesis es qué dependencia o exposición existe y T08 cuando es cómo se evalúa al tercero.
- **RP-09.5** (territorio (indicadores)): Para indicadores: el estado del control (cobertura, conformidad, diseño) va en T05 y su operación en el tiempo (plazos, cadencias, corrección), en T06.
- **RP-09.6** (territorio): T01 cubre el juicio de una persona; la oportunidad y la calidad de la decisión de un órgano van en T02.
- **RP-09.7** (territorio): Las cadencias de los controles van en T06 y las de la oficina, en T03.

**RP-10 · Regla 1: pruebas de aplicación**

- **RP-10.1** (territorio y dominio): Prueba de sustitución: si la tesis sigue siendo válida al reemplazar «IA» por «sistema», la IA es contexto y no objeto.
- **RP-10.2** (método de lectura): En la serie K, la tesis es la primera oración junto con el título.
- **RP-10.3** (dominio): En los puentes, el dominio primario es el del propósito declarado en el título.
- **RP-10.4** (método de lectura): La alineación con el resto de la unidad no es un motivo de clasificación.
- **RP-10.5** (dominio y subfunción): El escenario de amenaza (el adversario y sus técnicas) es D12 con ID03; el escenario de riesgo (la pérdida y su probabilidad) es D02 con ID04.
- **RP-10.6** (dominio): Un marco como sistema de gestión va a D01 y la obligación de certificarlo, a D03. (El dominio del catálogo de controles como modelo no está decidido: pregunta abierta RP-10.6.)
- **RP-10.7** (dominio): La obligación legal de privacidad va a D03 con D07 como secundario; la ingeniería de privacidad, a D07.
- **RP-10.8** (dominio): Cuando la tesis declarada habla del programa de formación, se clasifica por la práctica de seguridad que el programa enseña.

**RP-11 · Regla 2: desempates de cardinalidad**

- **RP-11.1** (subfunción): Cuando la tesis prescribe dos funciones, la subfunción primaria es la de la primera prescripción.
- **RP-11.2** (subfunción (indicadores)): La coordenada de un indicador admite hasta dos subfunciones secundarias, como la de un pre-ensayo.

**RP-12 · Subfunciones: definición y delimitación**

- **RP-12.2** (subfunción): Delimitaciones propuestas por los revisores: PR03 es arquitectura segura, hardening y segmentación (PR.PS y PR.IR-01) y PR06 es resiliencia de la infraestructura y protección física y ambiental (PR.IR-02 a PR.IR-04, con PR.AA-06, DE.CM-02 y PR.PS-03 como referencias de subcategoría).
- **RP-12.3** (subfunción): PR06 reúne las medidas previas y RC02 la operación degradada durante el incidente.
- **RP-12.4** (subfunción): DE02 construye y opera la detección; DE03 la pone a prueba y busca lo que no detecta; DE04 mide su cobertura y su calidad.
- **RP-12.5** (subfunción): ID03 identifica amenazas, vulnerabilidades y exposición técnica; ID04 analiza y cuantifica el riesgo y sigue su tratamiento.
- **RP-12.6** (subfunción): RC01 es la capacidad técnica de restaurar con sus objetivos; RC02 es la continuidad durante la perturbación; RC03 valida el retorno.
- **RP-12.7** (subfunción): RS03 es la comunicación de crisis y las notificaciones obligatorias; RS04 es la coordinación con terceros, incluidas las notificaciones contractuales.
- **RP-12.8** (subfunción): Las sesiones de órganos con acta y decisiones van a GV07 y las cadencias de gestión del programa, a GV05.
- **RP-12.9** (subfunción): El triaje y la priorización de incidentes van a RS01.
- **RP-12.10** (subfunción): La supervisión humana de agentes, los niveles de autonomía y el interruptor se expresan con GV02 o GV03 y con el mecanismo HOM12.

## Preguntas abiertas

El autor todavía no las decidió. Si un caso depende de una de ellas, clasificalo con la mejor lectura de las reglas de arriba y anotá el código en el campo `abiertas`.

- **RP-08.4** (dominio): El catálogo y el ciclo de vida de los controles (seleccionar, adaptar, mantener el catálogo de controles): D01, D28 o un dominio nuevo.
- **RP-10.6** (dominio): El catálogo de controles como modelo (por ejemplo, un catálogo normativo tomado como referencia de diseño): su dominio no está decidido.
- **RP-13** (subfunción): La mejora continua que no nace de un incidente: hoy va a RC04; no está decidido si pasa a la función Identificar.
- **RP-18.2** (dominio): La frontera entre D18 (OT e ICS) y D19 (IoT y sistemas ciberfísicos).
- **RP-18.4** (dominio): La carga y la capacidad del equipo de seguridad.
- **RP-18.7** (dominio): La automatización de seguridad que no usa IA.

## Escala del sistema operativo (campo `escala_os`)

Solo si el texto trata de lo que sostiene la calidad de la decisión: `individual` cuando es la energía, la atención, la carga o la resiliencia de una persona; `oficina` cuando son los derechos de decisión, las cadencias, los datos, los agentes o la evidencia de la oficina del CISO. En cualquier otro caso, `no aplica`.


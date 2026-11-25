# Resultados de las consultas de aceptación

Las 22 preguntas de competencia de la ontología 2.2.0 ejecutadas contra el grafo candidato. El SQL está en `consultas_de_aceptacion.sql`.

**Cómo se decide el estado.** El guion calcula para cada pregunta (a) si puede expresarse con los tipos y las relaciones de la ontología, (b) qué parte de su universo cubre la consulta y (c) si hay un límite declarado que impide responderla como está formulada. Es «Respondible» cuando puede expresarse, la cobertura llega al 90 % y no hay límite; «Respondible en parte» cuando la cobertura es menor o hay un límite; «Todavía no respondible» cuando no puede expresarse o no hay instancias. Que una consulta devuelva filas no alcanza.

| N.º | Pregunta | Estado | Motivo del estado | Cobertura | Filas | Nota |
|---|---|---|---|---|---|---|
| P01 | ¿Qué activos sostienen una capacidad empresarial crítica? | Todavía no respondible | sin instancias en el grafo | 0 instancias | 1 | No hay instancias de Asset ni de BusinessCapability: el Atlas es conocimiento de referencia y no contiene los activos de una organización. La ontología permite expresar el vínculo con PART_OF. |
| P02 | ¿Qué escenarios de riesgo pueden afectarla? | Todavía no respondible | sin instancias en el grafo | 0 instancias | 1 | No hay instancias de RiskScenario: el Atlas es conocimiento de referencia. Desde la ontología 2.2.0 la pregunta puede expresarse con MAY_AFFECT (propuesta 11 de la solicitud OCR-CAND-03). |
| P03 | ¿Qué controles contribuyen a mitigar esos escenarios? | Todavía no respondible | sin instancias en el grafo | 0 instancias | 1 | Hay controles de gobierno de agentes cargados, pero ningún escenario de riesgo contra el cual declarar que mitigan. |
| P04 | ¿Qué evidencia respalda la efectividad de los controles? | Todavía no respondible | sin instancias en el grafo | 0 instancias | 1 | No hay instancias de Evidence ni de AssessmentResult. Las fichas de producto-control dicen qué evidencia se espera, no la evidencia. |
| P05 | ¿Qué autoridad puede aceptar el riesgo residual? | Todavía no respondible | sin instancias en el grafo | 0 instancias | 1 | No hay instancias de Authority ni de Decision. Desde la ontología 2.2.0 la pregunta puede expresarse con ACCEPTS_RISK: una autoridad acepta el riesgo residual de un escenario dentro de una tolerancia y con vencimiento. |
| P06 | ¿Qué agentes poseen autoridad sobre determinados activos? | Todavía no respondible | sin instancias en el grafo | 0 instancias | 7 | No hay instancias de Asset ni de DelegatedAuthority. El grafo sí dice qué flota de agentes sirve a qué producto-control (consulta de abajo), pero eso no es autoridad sobre un activo; el rol dueño de cada flota lo fija el guion de carga, no la fuente. |
| P07 | ¿Qué herramientas y acciones están disponibles para esos agentes? | Respondible en parte | límite declarado | 85 de 85 agentes con herramientas declaradas | 268 | Herramientas declaradas en los anexos de los agentes del plano B. Límite: El grafo no tiene instancias de AutonomousAction: la consulta devuelve las herramientas de cada agente, no sus acciones. |
| P08 | ¿Qué fuerzas condicionan la evolución de una capacidad? | Respondible en parte | límite declarado | 27 de 28 dominios con alguna fuerza tratada por sus pre-ensayos | 8 | Ejemplo con el dominio D20. Los mecanismos homeostáticos no son fuerzas y quedan fuera de esta consulta (están en P15). La cobertura no cuenta la capa de ampliación APX: D19 solo tiene pre-ensayos de esa capa. Límite: A nivel de capacidad la pregunta no puede expresarse: no hay capacidades instanciadas. La consulta responde a nivel de dominio, con las fuerzas (catalizadores e inhibidores) que tratan sus pre-ensayos. |
| P09 | ¿Qué competencias necesita desarrollar un responsable? | Respondible en parte | cobertura menor que 90 % | 1 de 85 roles con competencias declaradas | 41 | Solo el rol PO-GAC tiene competencias declaradas; los demás roles del grafo son personas operativas citadas por los modelos operativos. |
| P10 | ¿Qué unidades GM-24 desarrollan y evalúan esas competencias? | Respondible en parte | límite declarado | 41 de 41 competencias con alguna unidad inferida | 133 | Competencia → conceptos que la sostienen → unidades del GM-24 a las que pertenecen esos conceptos. Límite: La unidad se infiere de los conceptos que sostienen la competencia: el grafo no tiene relaciones de desarrollo ni de evaluación (0 aristas DEVELOPS y ASSESSES). Que un concepto pertenezca a una unidad no prueba que la unidad desarrolle la competencia, y la parte «evalúan» no tiene respuesta. |
| P11 | ¿Qué pre-ensayos cubren una coordenada (territorio × dominio × subfunción) y con qué confianza? | Respondible | cobertura de al menos 90 % | 755 de 755 pre-ensayos con territorio, dominio y subfunción primarios y con confianza | 31 | Ejemplo con la coordenada T08 × D28 × GV08. La categorización es candidata: no tiene revisión humana. |
| P12 | ¿Qué elementos de qué artefactos de referencia respaldan un concepto y con qué fuerza? | Respondible | cobertura de al menos 90 % | 379 de 379 conceptos del GM-24 con algún mapeo que declara fuerza, versión y método | 19 | Ejemplo con el concepto M3.1-K03. La fuerza y el vínculo son los del mapeo del GM-24 V7.1, que en su mayor parte se generó por herencia de la unidad y regla por palabra clave: «fuerte» y «cubre» indican afinidad, no conformidad ni cobertura comprobada. Por eso la consulta muestra el método junto a la fuerza. |
| P13 | ¿Qué agentes ejecutan tareas de un producto-control, con qué nivel de autonomía y bajo qué puntos de control? | Respondible | cobertura de al menos 90 % | 156 de 156 pares de agente y tarea con nivel de autonomía y punto de control | 20 | Ejemplo con el producto-control de identidades (plano B). El punto de control es el que declara el anexo de cada agente. |
| P14 | ¿Qué conceptos del corpus instancia cada producto-control? | Respondible | cobertura de al menos 90 % | 7 de 7 productos-control con conceptos instanciados | 120 | Una fila por concepto. La instancia no prueba el concepto. |
| P15 | ¿Qué fuerzas y qué mecanismos homeostáticos tratan los pre-ensayos de un dominio? | Respondible | cobertura de al menos 90 % | 27 de 27 dominios con pre-ensayos en los que alguno trata una fuerza o un mecanismo | 22 | El universo y la cobertura son del corpus base: la capa de ampliación APX no cuenta, y D19 solo tiene pre-ensayos de esa capa. Ejemplo con el dominio D28. La columna «eje» distingue catalizadores (HC), inhibidores (HI) y mecanismos homeostáticos (HR): las fuerzas se cargan con el rol «fuerza» y los mecanismos, con el rol «mecanismo». |
| P16 | ¿Qué indicadores miden una variable homeostática y a qué decisión informan? | Respondible en parte | límite declarado | 6 de 6 variables con indicadores candidatos | 71 | La columna «lecturas» dice si el vínculo lo sostienen dos lecturas independientes o una sola. Límite: Son indicadores candidatos de un modelo de referencia: ninguna variable tiene unidad, umbral ni responsable del límite. No hay decisiones instanciadas, de modo que «a qué decisión informa» se responde solo con el órgano de gobierno que recibe el indicador. |
| P17 | ¿Qué prácticas metacognitivas contrarrestan los sesgos que pueden distorsionar una decisión? | Respondible en parte | límite declarado | 51 de 479 sesgos con alguna práctica propuesta | 57 | Una fila por vínculo. Solo se cargaron los que la segunda lectura independiente juzgó sostenibles. Límite: No hay decisiones instanciadas sobre las que declarar qué sesgo las distorsiona. Los vínculos expresan lo que la Biblioteca propone, no eficacia probada, y cubren una parte menor de los sesgos. |
| P18 | ¿Qué preguntas tienen un pre-ensayo directo y todavía no tienen un ensayo aprobado? | Respondible | cobertura de al menos 90 % | 595 de 595 preguntas evaluadas | 595 | Antiunión: preguntas a las que responde un pre-ensayo y a las que no responde ningún ensayo aprobado. El ensayo se representa como nodo Essay; hoy no hay ninguno, de modo que la lista son todas las que tienen pre-ensayo directo. La cobertura es total por construcción: el estado de esta pregunta depende solo de que la consulta pueda expresarse. |
| P19 | ¿Qué competencias requiere un rol y qué conceptos y unidades las sostienen? | Respondible en parte | cobertura menor que 90 % | 1 de 85 roles con competencias, conceptos y unidades | 202 | Rol → competencias → conceptos → unidades, para el rol PO-GAC, el único con competencias declaradas. Una fila por competencia y concepto. |
| P20 | ¿Qué celdas del Atlas no tienen conocimiento (silencios)? | Respondible en parte | límite declarado | 224 de 224 celdas territorio × dominio evaluadas | 137 | Celdas territorio × dominio sin ningún pre-ensayo del corpus base de 739 con ambas coordenadas primarias. La cobertura es total por construcción; el estado lo decide el límite declarado. Límite: la consulta no distingue las combinaciones de territorio y dominio que no pueden darse de las que no tienen contenido |
| P21 | ¿Qué conceptos de la Biblioteca cognitiva propone cubrir cada unidad del GM-24 y con qué confianza editorial? | Respondible | cobertura de al menos 90 % | 24 de 24 unidades con conceptos propuestos | 165 | Una fila por concepto. Solo los vínculos de selección editorial o de ancla expresa de la base; los de coincidencia temática no se cargaron. Es cobertura propuesta, no aprendizaje comprobado. |
| P22 | ¿Qué indicadores están clasificados en cada subfunción del Atlas y qué subfunciones no tienen ninguno? | Respondible en parte | límite declarado | 216 de 244 indicadores con subfunción | 216 | Una fila por indicador, con el método con que recibió la subfunción. Las subfunciones sin indicador están en el resumen. Límite: La consulta responde «qué indicadores están clasificados en cada subfunción», no «cuáles la miden»: la regla SV-118 no admite MEASURES hacia una subfunción. Los 20 indicadores del sub-plan PO-GAC no tienen coordenada en el Atlas. |

Resumen: 7 respondibles, 9 respondibles en parte y 6 todavía no respondibles. Sobre las 20 preguntas originales de la ontología: 6, 8 y 6.

Las 6 que no se responden necesitan instancias de una organización: activos, capacidades, escenarios de riesgo, evidencia y autoridades. Desde la ontología 2.2.0 todas pueden expresarse: P02 y P05, que antes no podían, tienen ahora una relación (MAY_AFFECT y ACCEPTS_RISK). Son las preguntas que un CISO necesita para decidir en su organización: el Atlas de referencia no las responde.

## Muestras de resultado

### P06. ¿Qué agentes poseen autoridad sobre determinados activos?

| flota | producto_control |
|---|---|
| Flota de agentes · DATOS | Protección de la información y de los datos (Microsoft Purview: clasificación, etiquetado, DLP, DSPM / DSPM fo |
| Flota de agentes · ENDPOINTS | Protección, detección y respuesta en endpoints (Microsoft Defender for Endpoint + Defender Vulnerability Manag |
| Flota de agentes · IDENTIDADES | Protección de identidades y acceso (Microsoft Defender for Identity + Microsoft Entra ID Protection + Conditio |
| Flota de agentes · NUBE | Postura y protección de cargas de trabajo en la nube (Microsoft Defender for Cloud: CSPM, CWPP, Defender for A |
| Flota de agentes · PRODUCTIVIDAD | Seguridad de correo y colaboración (Microsoft Defender for Office 365 sobre Exchange Online Protection, en Mic |
| Flota de agentes · SIEM | SIEM/SOAR y data lake de seguridad (Microsoft Sentinel en el portal de Microsoft Defender) |

Se muestran 6 de 7 filas.

### P07. ¿Qué herramientas y acciones están disponibles para esos agentes?

| agente | nombre | herramienta | permiso |
|---|---|---|---|
| AGT:AG-01 | Triage Copilot de incidentes de correo | Microsoft Graph · security/incidents y alerts_v2 | SecurityIncident.Read.All / ReadWrite.All; Unified RBAC |
| AGT:AG-01 | Triage Copilot de incidentes de correo | Microsoft Graph · security/runHuntingQuery | ThreatHunting.Read.All |
| AGT:AG-01 | Triage Copilot de incidentes de correo | Microsoft Sentinel MCP server | Entra ID integrated; RBAC de Sentinel (lectura) |
| AGT:AG-02 | Asistente de investigación y remediación | Defender for Cloud Apps / Defender ATP (conectores) | Lectura de alertas |
| AGT:AG-02 | Asistente de investigación y remediación | Exchange Online PowerShell vía runbook (TABL, cuarentena, políticas) | Identidad administrada con rol Exchange acotado; el agente solo invoca el flujo |
| AGT:AG-02 | Asistente de investigación y remediación | Microsoft Graph · security/incidents y alerts_v2 | SecurityIncident.Read.All / ReadWrite.All; Unified RBAC |

Se muestran 6 de 268 filas.

### P08. ¿Qué fuerzas condicionan la evolución de una capacidad?

| eje | codigo | fuerza | pre_ensayos |
|---|---|---|---|
| HC | TAX:CAT01 | CAT01 Innovación tecnológica | 5 |
| HI | TAX:INH09 | INH09 Limitaciones operativas | 5 |
| HI | TAX:INH10 | INH10 Incertidumbre tecnológica | 4 |
| HI | TAX:INH08 | INH08 Resistencia cultural | 2 |
| HC | TAX:CAT03 | CAT03 Presión regulatoria | 1 |
| HC | TAX:CAT04 | CAT04 Evolución de amenazas | 1 |

Se muestran 6 de 8 filas.

### P09. ¿Qué competencias necesita desarrollar un responsable?

| id | competencia | dominio |
|---|---|---|
| CMP:C1.1 | Definir y mantener la ficha del producto-control (objetivo, alcance, métricas, backlog) | D1 |
| CMP:C1.2 | Usar CSF 2.0 × Zero Trust como grilla de ownership | D1 |
| CMP:C1.3 | Priorizar el backlog del control por riesgo y valor | D1 |
| CMP:C1.4 | Definir KPIs del control que no engañen | D1 |
| CMP:C1.5 | Gestionar baseline, excepciones y overrides con vencimiento | D1 |
| CMP:C2.1 | Explicar la arquitectura de protección de correo y colaboración | D2 |

Se muestran 6 de 41 filas.

### P10. ¿Qué unidades GM-24 desarrollan y evalúan esas competencias?

| competencia | unidad | conceptos |
|---|---|---|
| CMP:C1.1 | M3.2 Selección, Implementación y Evaluación de Controles | 1 |
| CMP:C1.1 | M1.1 Desarrollo, Gestión y Operaciones del Programa de Seguridad | 1 |
| CMP:C1.1 | G1.1 Principios de Gobierno, Contexto Organizacional y Arquetipos CISO | 1 |
| CMP:C1.2 | G2.1 Selección e Integración de Marcos y Estándares | 2 |
| CMP:C1.2 | M3.2 Selección, Implementación y Evaluación de Controles | 1 |
| CMP:C1.2 | M3.1 Arquitectura de Seguridad, Ingeniería y Diseño (Incl. Zero Trust) | 1 |

Se muestran 6 de 133 filas.

### P11. ¿Qué pre-ensayos cubren una coordenada (territorio × dominio × subfunción) y con qué confianza?

| id | pre_ensayo | confianza |
|---|---|---|
| PRE:AMP-13 | Evidencia continua | alta |
| PRE:AMP-14 | Aseguramiento de decisiones de IA | alta |
| PRE:APA-014 | Mapa de aseguramiento de controles sobre IA y agentes | media |
| PRE:APA-039 | Biblioteca de evidencia para cuestionarios de seguridad de clientes | alta |
| PRE:APA-082 | Portafolio de atestaciones independientes para clientes | alta |
| PRE:APA-136 | Clasificación de controles de IA según evidencia auditable | alta |

Se muestran 6 de 31 filas.

### P12. ¿Qué elementos de qué artefactos de referencia respaldan un concepto y con qué fuerza?

| artefacto | elemento | fuerza | vinculo | version_del_mapeo | metodo |
|---|---|---|---|---|---|
| CISM, esquema de examen 2026 | CISM-1B | fuerte | cubre | ECO 2026 | herencia de unidad + regla por palabra clave |
| CISM, esquema de examen 2026 | CISM-3A | fuerte | cubre | ECO 2026 | herencia de unidad + regla por palabra clave |
| CRISC, esquema de examen 2025 | CRISC-4A | fuerte | cubre | ECO 2025 | herencia de unidad + regla por palabra clave |
| CSA Cloud Controls Matrix | AIS Application & Interface Security | fuerte | cubre | v4.x (el GM-24 no precisa; usa el código IVS, anterior a la v4.1) | herencia de unidad + regla por palabra clave |
| CSA Cloud Controls Matrix | IAM Identity & Access Management | fuerte | cubre | v4.x (el GM-24 no precisa; usa el código IVS, anterior a la v4.1) | herencia de unidad + regla por palabra clave |
| CSA Cloud Controls Matrix | IVS Infrastructure & Virtualization Security | fuerte | cubre | v4.x (el GM-24 no precisa; usa el código IVS, anterior a la v4.1) | herencia de unidad + regla por palabra clave |

Se muestran 6 de 19 filas.

### P13. ¿Qué agentes ejecutan tareas de un producto-control, con qué nivel de autonomía y bajo qué puntos de control?

| agente | tarea | autonomia_de_la_tarea | punto_de_control | clase |
|---|---|---|---|---|
| Analista de Conditional Access | Revisar baseline de CA y excepciones (break-glass) con vencimiento | AUL:L2 | Solo propuestas; cambios de CA los ejecuta un humano | ["aprobación previa"] |
| Analista de Conditional Access | Revisar efectos de Conditional Access (report-only) y proponer ajustes | AUL:L2 | Solo propuestas; cambios de CA los ejecuta un humano | ["aprobación previa"] |
| Analista de la flota Identidades | Revisar desempeño y costo de la flota Identidades | AUL:L1 | Decisiones humanas | ["aprobación previa"] |
| Analista de tuning de alertas de identidad | Configurar reglas de tuning para benign true positives de MDI | AUL:L2 | Con aprobación | ["aprobación previa"] |
| Analista de tuning de alertas de identidad | Revisar alertas tuned y retirar reglas sin coincidencias | AUL:L2 | Con aprobación | ["aprobación previa"] |
| Asistente de investigación y remediación de identidad | Investigar risky users / sign-ins; confirmar o descartar; remediar o dejar que CA auto-remedie | AUL:L2 | Toda acción con aprobación; nunca sobre break-glass ni admins sin segunda aprobación | ["aprobación previa","prohibición de delegar"] |

Se muestran 6 de 20 filas.

### P14. ¿Qué conceptos del corpus instancia cada producto-control?

| producto_control | concepto | titulo |
|---|---|---|
| PCT:DATOS | CON:AMP-11 | Soberanía de datos |
| PCT:DATOS | CON:AMP-25 | Ética de autonomía |
| PCT:DATOS | CON:AMP-31 | DSPM |
| PCT:DATOS | CON:AMP-32 | Gobierno de datos para RAG |
| PCT:DATOS | CON:AMP-52 | Content safety y riesgos de contenido generado |
| PCT:DATOS | CON:G2.2-PA03 | Baseline, excepciones y overrides de un control técnico |

Se muestran 6 de 120 filas.

Resumen:

| producto_control | conceptos |
|---|---|
| PCT:DATOS | 18 |
| PCT:ENDPOINTS | 13 |
| PCT:IDENTIDADES | 15 |
| PCT:NUBE | 15 |
| PCT:PRODUCTIVIDAD | 13 |
| PCT:SIEM | 15 |
| PCT:XDR | 31 |

### P15. ¿Qué fuerzas y qué mecanismos homeostáticos tratan los pre-ensayos de un dominio?

| eje | codigo | fuerza_o_mecanismo | pre_ensayos |
|---|---|---|---|
| HR | TAX:HOM09 | HOM09 Assurance y validación | 51 |
| HR | TAX:HOM08 | HOM08 Gobierno y supervisión | 9 |
| HR | TAX:HOM03 | HOM03 Segregación de funciones | 8 |
| HC | TAX:CAT01 | CAT01 Innovación tecnológica | 7 |
| HC | TAX:CAT09 | CAT09 Expectativas de clientes | 4 |
| HR | TAX:HOM02 | HOM02 Gestión de cambios | 4 |

Se muestran 6 de 22 filas.

### P16. ¿Qué indicadores miden una variable homeostática y a qué decisión informan?

| variable | indicador | nombre | papel | lecturas | informa_a |
|---|---|---|---|---|---|
| TAX:HV01 | IND:K24 | Pérdidas por incidentes frente a la tolerancia anual | principal | dos lecturas | Directorio y síndicos · CISO y comité de seguridad |
| TAX:HV01 | IND:K25 | Riesgos residuales fuera del apetito | principal | dos lecturas | Directorio y síndicos · CEO, CFO y comité ejecutivo · CISO y comité de seguridad |
| TAX:HV01 | IND:K26 | Pérdida esperada de los escenarios prioritarios frente al apetito | principal | dos lecturas | Directorio y síndicos · CEO, CFO y comité ejecutivo · CISO y comité de seguridad |
| TAX:HV01 | IND:K87 | Umbrales de apetito superados con decisión en plazo | principal | dos lecturas | Directorio y síndicos · CEO, CFO y comité ejecutivo · CISO y comité de seguridad |
| TAX:HV01 | IND:K93 | Aceptaciones de riesgo vencidas sin renovar | principal | dos lecturas | Directorio y síndicos · CEO, CFO y comité ejecutivo · CISO y comité de seguridad |
| TAX:HV01 | IND:K140 | Rutas de ataque abiertas hacia activos críticos | apoyo | dos lecturas | CISO y comité de seguridad |

Se muestran 6 de 71 filas.

### P17. ¿Qué prácticas metacognitivas contrarrestan los sesgos que pueden distorsionar una decisión?

| practica | sesgo | confianza | metodo |
|---|---|---|---|
| Abogado del diablo | Sesgo de autoría propia | media | la ficha del sesgo nombra la práctica como control compensatorio |
| Abogado del diablo | Sesgo de búsqueda de coherencia artificial | baja | la ficha del sesgo nombra la práctica como control compensatorio |
| Abogado del diablo | Sesgo de coherencia | media | la ficha del sesgo nombra la práctica como control compensatorio |
| Abogado del diablo | Sesgo de compromiso | media | la ficha del sesgo nombra la práctica como control compensatorio |
| Abogado del diablo | Sesgo de compromiso y consistencia | baja | la ficha del sesgo nombra la práctica como control compensatorio |
| Abogado del diablo | Sesgo de consistencia forzada | media | la ficha del sesgo nombra la práctica como control compensatorio |

Se muestran 6 de 57 filas.

Resumen:

| practica | sesgos |
|---|---|
| Valor esperado | 13 |
| Calibración | 10 |
| Listas de verificación | 8 |
| Abogado del diablo | 7 |
| Premortem | 5 |
| Análisis de hipótesis competidoras | 2 |
| Checklist de desesgo | 2 |
| Red teaming | 2 |

Se muestran 8 de 14 filas.

### P18. ¿Qué preguntas tienen un pre-ensayo directo y todavía no tienen un ensayo aprobado?

| pregunta | texto |
|---|---|
| QST:PA-001 | ¿Estamos más o menos expuestos que hace un año, y cómo lo sabemos? |
| QST:PA-002 | ¿Cuáles son los tres escenarios que podrían causarnos un daño material y qué tan preparados estamos para cada  |
| QST:PA-003 | ¿Nuestro riesgo cibernético está dentro del apetito que aprobamos? ¿Dónde no, y qué nos propone? |
| QST:PA-004 | ¿Cómo supervisamos la IA y los agentes que ya operan en la compañía, y quién responde por ellos? |
| QST:PA-005 | ¿Estamos adoptando IA a la velocidad correcta, o el miedo al riesgo nos está dejando atrás? |
| QST:PA-006 | Si mañana sufrimos un ataque grave, ¿qué decisiones tendremos que tomar nosotros y estamos preparados para tom |

Se muestran 6 de 595 filas.

### P19. ¿Qué competencias requiere un rol y qué conceptos y unidades las sostienen?

| competencia | concepto | titulo | unidad |
|---|---|---|---|
| CMP:C1.1 | CON:G1.1-PA01 | Rol dual especialista/manager y Product Owner de control | G1.1 Principios de Gobierno, Contexto Organizacional y Arquetipos CISO |
| CMP:C1.1 | CON:M1.1-PA02 | Portafolio de productos-control con owners | M1.1 Desarrollo, Gestión y Operaciones del Programa de Seguridad |
| CMP:C1.1 | CON:M3.2-PA01 | El control como producto: objetivo → configuración → evidencia | M3.2 Selección, Implementación y Evaluación de Controles |
| CMP:C1.2 | CON:AMP-07 | NIST CSF 2.0 Govern | G2.1 Selección e Integración de Marcos y Estándares |
| CMP:C1.2 | CON:G2.1-PA01 | Grilla de ownership: NIST CSF 2.0 × dominios Zero Trust | G2.1 Selección e Integración de Marcos y Estándares |
| CMP:C1.2 | CON:HC-015 | Gobierno y operación de Zero Trust | G2.2 Ciclo de Vida de Políticas, Estándares y Procedimientos |

Se muestran 6 de 202 filas.

Resumen:

| dominio_de_competencia | competencias | conceptos | unidades |
|---|---|---|---|
| D1 | 5 | 13 | 13 |
| D2 | 6 | 12 | 8 |
| D3 | 5 | 11 | 8 |
| D4 | 6 | 18 | 9 |
| D5 | 6 | 28 | 17 |
| D6 | 6 | 29 | 17 |
| D7 | 3 | 13 | 6 |
| D8 | 4 | 22 | 12 |

### P20. ¿Qué celdas del Atlas no tienen conocimiento (silencios)?

| territorio | dominio |
|---|---|
| TAX:T01 | TAX:D02 |
| TAX:T01 | TAX:D03 |
| TAX:T01 | TAX:D04 |
| TAX:T01 | TAX:D05 |
| TAX:T01 | TAX:D06 |
| TAX:T01 | TAX:D07 |

Se muestran 6 de 137 filas.

### P21. ¿Qué conceptos de la Biblioteca cognitiva propone cubrir cada unidad del GM-24 y con qué confianza editorial?

| unidad | concepto | tipo | confianza_editorial | metodo |
|---|---|---|---|---|
| G1.1 Principios de Gobierno, Contexto Organizacional y Arquetipos CISO | Círculo de competencia | MentalModel | media | editorial_curation_72 |
| G1.1 Principios de Gobierno, Contexto Organizacional y Arquetipos CISO | Mentalidad de crecimiento | HumanCapability | media | editorial_curation_72 |
| G1.1 Principios de Gobierno, Contexto Organizacional y Arquetipos CISO | Mentalidad de propiedad | HumanCapability | media | editorial_curation_72 |
| G1.1 Principios de Gobierno, Contexto Organizacional y Arquetipos CISO | Metacognición | HumanCapability | alta_editorial | source_crosswalk |
| G1.1 Principios de Gobierno, Contexto Organizacional y Arquetipos CISO | Pensamiento grupal | CognitiveBias | media | editorial_curation_72 |
| G1.2 Desarrollo de Estrategia y Alineación con el Negocio | Decisiones reversibles e irreversibles | MentalModel | media | editorial_curation_72 |

Se muestran 6 de 165 filas.

Resumen:

| unidad | conceptos |
|---|---|
| G1.1 Principios de Gobierno, Contexto Organizacional y Arquetipos CISO | 5 |
| G1.2 Desarrollo de Estrategia y Alineación con el Negocio | 8 |
| G2.1 Selección e Integración de Marcos y Estándares | 2 |
| G2.2 Ciclo de Vida de Políticas, Estándares y Procedimientos | 1 |
| G3.1 Requisitos Legales, Regulatorios y Contractuales | 1 |
| G3.2 Gestión del Cumplimiento y Aseguramiento Continuo | 5 |
| G4.1 Gobernanza del Riesgo: Marcos y Estructuras | 8 |
| G4.2 Definición y Comunicación del Apetito de Riesgo | 7 |

Se muestran 8 de 24 filas.

### P22. ¿Qué indicadores están clasificados en cada subfunción del Atlas y qué subfunciones no tienen ninguno?

| subfuncion | indicador | nombre | metodo | confianza |
|---|---|---|---|---|
| TAX:DE01 | IND:K125 | Carga por analista | derivada de la categoría de CSF 2.0 que declara el catálogo 2.0, sin lectura del indicador | baja |
| TAX:DE01 | IND:K152 | Tiempo de retiro de mensajes maliciosos entregados | derivada de la categoría de CSF 2.0 que declara el catálogo 2.0, sin lectura del indicador | baja |
| TAX:DE01 | IND:K173 | Fuentes críticas con registro íntegro y retención conforme | derivada de la categoría de CSF 2.0 que declara el catálogo 2.0, sin lectura del indicador | baja |
| TAX:DE01 | IND:K174 | Registros ingeridos sin uso en detección ni investigación | derivada de la categoría de CSF 2.0 que declara el catálogo 2.0, sin lectura del indicador | baja |
| TAX:DE01 | IND:K175 | Acciones de agentes revertidas | derivada de la categoría de CSF 2.0 que declara el catálogo 2.0, sin lectura del indicador | baja |
| TAX:DE01 | IND:K183 | Cobertura horaria efectiva de la vigilancia | derivada de la categoría de CSF 2.0 que declara el catálogo 2.0, sin lectura del indicador | baja |

Se muestran 6 de 216 filas.

Resumen:

| subfuncion | nombre | indicadores |
|---|---|---|
| TAX:PR06 | PR06 Resiliencia de la infraestructura y protección física y ambiental | 0 |
| TAX:RC04 | RC04 Lecciones y cierre de la recuperación | 0 |
| TAX:DE03 | DE03 Hunting, validación y mejora de detecciones | 1 |
| TAX:RC05 | RC05 Comunicación de la recuperación y restitución de la confianza | 1 |
| TAX:ID02 | ID02 Dependencias y criticidad del negocio | 2 |
| TAX:RC03 | RC03 Validación de recuperación y retorno seguro | 2 |
| TAX:RS03 | RS03 Comunicación de crisis y decisiones ejecutivas | 2 |
| TAX:DE02 | DE02 Ingeniería de detección y análisis | 3 |

Se muestran 8 de 35 filas.

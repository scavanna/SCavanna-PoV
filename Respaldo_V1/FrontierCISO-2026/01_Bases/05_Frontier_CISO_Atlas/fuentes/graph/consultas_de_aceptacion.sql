-- Frontier CISO Atlas · consultas de aceptación (22 preguntas de competencia de la ontología 2.2.0)
-- Base: graph/frontier_ciso_atlas_candidato.sqlite (grafo CANDIDATO).
-- El estado se deriva de tres datos: si la pregunta puede expresarse con la ontología, la cobertura de la consulta sobre su universo (umbral: 90 %) y el límite declarado.

-- P01. ¿Qué activos sostienen una capacidad empresarial crítica?
-- Estado: Todavía no respondible (sin instancias en el grafo). Cobertura: 0 instancias.
-- No hay instancias de Asset ni de BusinessCapability: el Atlas es conocimiento de referencia y no contiene los activos de una organización. La ontología permite expresar el vínculo con PART_OF.
SELECT COUNT(*) AS instancias FROM nodes WHERE type IN ('Asset','BusinessCapability');

-- P02. ¿Qué escenarios de riesgo pueden afectarla?
-- Estado: Todavía no respondible (sin instancias en el grafo). Cobertura: 0 instancias.
-- No hay instancias de RiskScenario: el Atlas es conocimiento de referencia. Desde la ontología 2.2.0 la pregunta puede expresarse con MAY_AFFECT (propuesta 11 de la solicitud OCR-CAND-03).
SELECT COUNT(*) AS instancias FROM nodes WHERE type IN ('RiskScenario');

-- P03. ¿Qué controles contribuyen a mitigar esos escenarios?
-- Estado: Todavía no respondible (sin instancias en el grafo). Cobertura: 0 instancias.
-- Hay controles de gobierno de agentes cargados, pero ningún escenario de riesgo contra el cual declarar que mitigan.
SELECT (SELECT COUNT(*) FROM nodes WHERE type='SecurityControl') AS controles, (SELECT COUNT(*) FROM nodes WHERE type='RiskScenario') AS escenarios, (SELECT COUNT(*) FROM edges WHERE type='MITIGATES') AS mitigaciones;

-- P04. ¿Qué evidencia respalda la efectividad de los controles?
-- Estado: Todavía no respondible (sin instancias en el grafo). Cobertura: 0 instancias.
-- No hay instancias de Evidence ni de AssessmentResult. Las fichas de producto-control dicen qué evidencia se espera, no la evidencia.
SELECT COUNT(*) AS instancias FROM nodes WHERE type IN ('Evidence','AssessmentResult');

-- P05. ¿Qué autoridad puede aceptar el riesgo residual?
-- Estado: Todavía no respondible (sin instancias en el grafo). Cobertura: 0 instancias.
-- No hay instancias de Authority ni de Decision. Desde la ontología 2.2.0 la pregunta puede expresarse con ACCEPTS_RISK: una autoridad acepta el riesgo residual de un escenario dentro de una tolerancia y con vencimiento.
SELECT COUNT(*) AS instancias FROM nodes WHERE type IN ('Authority','Decision');

-- P06. ¿Qué agentes poseen autoridad sobre determinados activos?
-- Estado: Todavía no respondible (sin instancias en el grafo). Cobertura: 0 instancias.
-- No hay instancias de Asset ni de DelegatedAuthority. El grafo sí dice qué flota de agentes sirve a qué producto-control (consulta de abajo), pero eso no es autoridad sobre un activo; el rol dueño de cada flota lo fija el guion de carga, no la fuente.
SELECT f.label AS flota, p.label AS producto_control FROM edges s JOIN nodes f ON f.id=s.source JOIN nodes p ON p.id=s.target WHERE s.type='SERVES' ORDER BY 1;

-- P07. ¿Qué herramientas y acciones están disponibles para esos agentes?
-- Estado: Respondible en parte (límite declarado). Cobertura: 85 de 85 agentes con herramientas declaradas.
-- Herramientas declaradas en los anexos de los agentes del plano B. Límite: El grafo no tiene instancias de AutonomousAction: la consulta devuelve las herramientas de cada agente, no sus acciones.
SELECT a.id AS agente, a.label AS nombre, t.label AS herramienta, json_extract(t.properties,'$.permiso') AS permiso FROM edges e JOIN nodes a ON a.id=e.source JOIN nodes t ON t.id=e.target WHERE e.type='INVOKES' ORDER BY 1,3;

-- P08. ¿Qué fuerzas condicionan la evolución de una capacidad?
-- Estado: Respondible en parte (límite declarado). Cobertura: 27 de 28 dominios con alguna fuerza tratada por sus pre-ensayos.
-- Ejemplo con el dominio D20. Los mecanismos homeostáticos no son fuerzas y quedan fuera de esta consulta (están en P15). La cobertura no cuenta la capa de ampliación APX: D19 solo tiene pre-ensayos de esa capa. Límite: A nivel de capacidad la pregunta no puede expresarse: no hay capacidades instanciadas. La consulta responde a nivel de dominio, con las fuerzas (catalizadores e inhibidores) que tratan sus pre-ensayos.
SELECT json_extract(f.properties,'$.axis') AS eje, t.id AS codigo, t.label AS fuerza, COUNT(*) AS pre_ensayos FROM edges d JOIN edges f ON f.source=d.source AND f.type='CLASSIFIED_IN' AND json_extract(f.properties,'$.axis') IN ('HC','HI') JOIN nodes t ON t.id=f.target WHERE d.type='CLASSIFIED_IN' AND d.target='TAX:D20' AND json_extract(d.properties,'$.role')='primario' GROUP BY 1,2,3 ORDER BY 4 DESC, 2;

-- P09. ¿Qué competencias necesita desarrollar un responsable?
-- Estado: Respondible en parte (cobertura menor que 90 %). Cobertura: 1 de 85 roles con competencias declaradas.
-- Solo el rol PO-GAC tiene competencias declaradas; los demás roles del grafo son personas operativas citadas por los modelos operativos.
SELECT c.id, c.label AS competencia, json_extract(c.properties,'$.dominio_competencia') AS dominio FROM edges e JOIN nodes c ON c.id=e.target WHERE e.type='REQUIRES_COMPETENCY' AND e.source='ROL:PO-GAC' ORDER BY 1;

-- P10. ¿Qué unidades GM-24 desarrollan y evalúan esas competencias?
-- Estado: Respondible en parte (límite declarado). Cobertura: 41 de 41 competencias con alguna unidad inferida.
-- Competencia → conceptos que la sostienen → unidades del GM-24 a las que pertenecen esos conceptos. Límite: La unidad se infiere de los conceptos que sostienen la competencia: el grafo no tiene relaciones de desarrollo ni de evaluación (0 aristas DEVELOPS y ASSESSES). Que un concepto pertenezca a una unidad no prueba que la unidad desarrolle la competencia, y la parte «evalúan» no tiene respuesta.
SELECT c.id AS competencia, u.label AS unidad, COUNT(DISTINCT k.id) AS conceptos FROM edges ck JOIN nodes c ON c.id=ck.source JOIN nodes k ON k.id=ck.target JOIN edges ku ON ku.source=k.id AND ku.type='PART_OF' JOIN nodes u ON u.id=ku.target AND u.type='LearningUnit' WHERE ck.type='SUSTAINED_BY' GROUP BY 1,2 ORDER BY 1,3 DESC;

-- P11. ¿Qué pre-ensayos cubren una coordenada (territorio × dominio × subfunción) y con qué confianza?
-- Estado: Respondible (cobertura de al menos 90 %). Cobertura: 755 de 755 pre-ensayos con territorio, dominio y subfunción primarios y con confianza.
-- Ejemplo con la coordenada T08 × D28 × GV08. La categorización es candidata: no tiene revisión humana.
SELECT p.id, p.label AS pre_ensayo, json_extract(ey.properties,'$.confidence') AS confianza FROM nodes p JOIN edges ex ON ex.source=p.id AND ex.type='CLASSIFIED_IN' AND ex.target='TAX:T08' AND json_extract(ex.properties,'$.role')='primario' JOIN edges ey ON ey.source=p.id AND ey.type='CLASSIFIED_IN' AND ey.target='TAX:D28' AND json_extract(ey.properties,'$.role')='primario' JOIN edges ez ON ez.source=p.id AND ez.type='CLASSIFIED_IN' AND ez.target='TAX:GV08' AND json_extract(ez.properties,'$.role')='primario' WHERE p.type='Precursor' ORDER BY 1;

-- P12. ¿Qué elementos de qué artefactos de referencia respaldan un concepto y con qué fuerza?
-- Estado: Respondible (cobertura de al menos 90 %). Cobertura: 379 de 379 conceptos del GM-24 con algún mapeo que declara fuerza, versión y método.
-- Ejemplo con el concepto M3.1-K03. La fuerza y el vínculo son los del mapeo del GM-24 V7.1, que en su mayor parte se generó por herencia de la unidad y regla por palabra clave: «fuerte» y «cubre» indican afinidad, no conformidad ni cobertura comprobada. Por eso la consulta muestra el método junto a la fuerza.
SELECT a.label AS artefacto, f.label AS elemento, json_extract(e.properties,'$.strength') AS fuerza, json_extract(e.properties,'$.link_type') AS vinculo, json_extract(e.properties,'$.artifact_version') AS version_del_mapeo, json_extract(e.properties,'$.method') AS metodo FROM edges e JOIN nodes f ON f.id=e.target JOIN edges pa ON pa.source=f.id AND pa.type='PART_OF' JOIN nodes a ON a.id=pa.target WHERE e.type='MAPS_TO' AND e.source='CON:M3.1-K03' ORDER BY 3,1;

-- P13. ¿Qué agentes ejecutan tareas de un producto-control, con qué nivel de autonomía y bajo qué puntos de control?
-- Estado: Respondible (cobertura de al menos 90 %). Cobertura: 156 de 156 pares de agente y tarea con nivel de autonomía y punto de control.
-- Ejemplo con el producto-control de identidades (plano B). El punto de control es el que declara el anexo de cada agente.
SELECT a.label AS agente, t.label AS tarea, l.id AS autonomia_de_la_tarea, g.label AS punto_de_control, json_extract(g.properties,'$.clase') AS clase FROM edges pf JOIN nodes a ON a.id=pf.source AND a.type='AIAgent' JOIN nodes t ON t.id=pf.target LEFT JOIN edges oa ON oa.source=t.id AND oa.type='OPERATES_AT' LEFT JOIN nodes l ON l.id=oa.target LEFT JOIN edges gb ON gb.source=a.id AND gb.type='GATED_BY' LEFT JOIN nodes g ON g.id=gb.target JOIN edges po ON po.source=t.id AND po.type='PART_OF' JOIN edges ou ON ou.target=po.target AND ou.type='OPERATED_UNDER' AND ou.source='PCT:IDENTIDADES' WHERE pf.type='PERFORMS' ORDER BY 1,2;

-- P14. ¿Qué conceptos del corpus instancia cada producto-control?
-- Estado: Respondible (cobertura de al menos 90 %). Cobertura: 7 de 7 productos-control con conceptos instanciados.
-- Una fila por concepto. La instancia no prueba el concepto.
SELECT p.id AS producto_control, k.id AS concepto, k.label AS titulo FROM edges e JOIN nodes p ON p.id=e.source JOIN nodes k ON k.id=e.target WHERE e.type='INSTANTIATES' ORDER BY 1,2;
-- Resumen de P14:
SELECT p.id AS producto_control, COUNT(*) AS conceptos FROM edges e JOIN nodes p ON p.id=e.source WHERE e.type='INSTANTIATES' GROUP BY 1 ORDER BY 1;

-- P15. ¿Qué fuerzas y qué mecanismos homeostáticos tratan los pre-ensayos de un dominio?
-- Estado: Respondible (cobertura de al menos 90 %). Cobertura: 27 de 27 dominios con pre-ensayos en los que alguno trata una fuerza o un mecanismo.
-- El universo y la cobertura son del corpus base: la capa de ampliación APX no cuenta, y D19 solo tiene pre-ensayos de esa capa. Ejemplo con el dominio D28. La columna «eje» distingue catalizadores (HC), inhibidores (HI) y mecanismos homeostáticos (HR): las fuerzas se cargan con el rol «fuerza» y los mecanismos, con el rol «mecanismo».
SELECT json_extract(f.properties,'$.axis') AS eje, t.id AS codigo, t.label AS fuerza_o_mecanismo, COUNT(*) AS pre_ensayos FROM edges d JOIN edges f ON f.source=d.source AND f.type='CLASSIFIED_IN' AND json_extract(f.properties,'$.role') IN ('fuerza','mecanismo') JOIN nodes t ON t.id=f.target WHERE d.type='CLASSIFIED_IN' AND d.target='TAX:D28' AND json_extract(d.properties,'$.role')='primario' GROUP BY 1,2,3 ORDER BY 4 DESC, 2;

-- P16. ¿Qué indicadores miden una variable homeostática y a qué decisión informan?
-- Estado: Respondible en parte (límite declarado). Cobertura: 6 de 6 variables con indicadores candidatos.
-- La columna «lecturas» dice si el vínculo lo sostienen dos lecturas independientes o una sola. Límite: Son indicadores candidatos de un modelo de referencia: ninguna variable tiene unidad, umbral ni responsable del límite. No hay decisiones instanciadas, de modo que «a qué decisión informa» se responde solo con el órgano de gobierno que recibe el indicador.
SELECT v.id AS variable, i.id AS indicador, i.label AS nombre, json_extract(m.properties,'$.papel') AS papel, json_extract(m.properties,'$.lecturas') AS lecturas, (SELECT group_concat(g.label,' · ') FROM edges f JOIN nodes g ON g.id=f.target WHERE f.type='INFORMS' AND f.source=i.id) AS informa_a FROM edges m JOIN nodes i ON i.id=m.source JOIN nodes v ON v.id=m.target WHERE m.type='MEASURES' AND json_extract(v.properties,'$.axis')='HV' ORDER BY 1, 4 DESC, 2;

-- P17. ¿Qué prácticas metacognitivas contrarrestan los sesgos que pueden distorsionar una decisión?
-- Estado: Respondible en parte (límite declarado). Cobertura: 51 de 479 sesgos con alguna práctica propuesta.
-- Una fila por vínculo. Solo se cargaron los que la segunda lectura independiente juzgó sostenibles. Límite: No hay decisiones instanciadas sobre las que declarar qué sesgo las distorsiona. Los vínculos expresan lo que la Biblioteca propone, no eficacia probada, y cubren una parte menor de los sesgos.
SELECT p.label AS practica, s.label AS sesgo, json_extract(e.properties,'$.confidence') AS confianza, json_extract(e.properties,'$.method') AS metodo FROM edges e JOIN nodes p ON p.id=e.source JOIN nodes s ON s.id=e.target WHERE e.type='COUNTERS' ORDER BY 1,2;
-- Resumen de P17:
SELECT p.label AS practica, COUNT(*) AS sesgos FROM edges e JOIN nodes p ON p.id=e.source WHERE e.type='COUNTERS' GROUP BY 1 ORDER BY 2 DESC, 1;

-- P18. ¿Qué preguntas tienen un pre-ensayo directo y todavía no tienen un ensayo aprobado?
-- Estado: Respondible (cobertura de al menos 90 %). Cobertura: 595 de 595 preguntas evaluadas.
-- Antiunión: preguntas a las que responde un pre-ensayo y a las que no responde ningún ensayo aprobado. El ensayo se representa como nodo Essay; hoy no hay ninguno, de modo que la lista son todas las que tienen pre-ensayo directo. La cobertura es total por construcción: el estado de esta pregunta depende solo de que la consulta pueda expresarse.
SELECT q.id AS pregunta, q.label AS texto FROM nodes q WHERE q.type='Question' AND EXISTS (SELECT 1 FROM edges a JOIN nodes p ON p.id=a.source AND p.type='Precursor' WHERE a.type='ADDRESSES' AND a.target=q.id) AND NOT EXISTS (SELECT 1 FROM edges a JOIN nodes s ON s.id=a.source AND s.type='Essay' AND s.status='approved' WHERE a.type='ADDRESSES' AND a.target=q.id) ORDER BY 1;

-- P19. ¿Qué competencias requiere un rol y qué conceptos y unidades las sostienen?
-- Estado: Respondible en parte (cobertura menor que 90 %). Cobertura: 1 de 85 roles con competencias, conceptos y unidades.
-- Rol → competencias → conceptos → unidades, para el rol PO-GAC, el único con competencias declaradas. Una fila por competencia y concepto.
SELECT c.id AS competencia, k.id AS concepto, k.label AS titulo, u.label AS unidad FROM edges rc JOIN nodes c ON c.id=rc.target JOIN edges ck ON ck.source=c.id AND ck.type='SUSTAINED_BY' JOIN nodes k ON k.id=ck.target LEFT JOIN edges ku ON ku.source=k.id AND ku.type='PART_OF' LEFT JOIN nodes u ON u.id=ku.target AND u.type='LearningUnit' WHERE rc.type='REQUIRES_COMPETENCY' AND rc.source='ROL:PO-GAC' ORDER BY 1,2;
-- Resumen de P19:
SELECT json_extract(c.properties,'$.dominio_competencia') AS dominio_de_competencia, COUNT(DISTINCT c.id) AS competencias, COUNT(DISTINCT k.id) AS conceptos, COUNT(DISTINCT u.id) AS unidades FROM edges rc JOIN nodes c ON c.id=rc.target LEFT JOIN edges ck ON ck.source=c.id AND ck.type='SUSTAINED_BY' LEFT JOIN nodes k ON k.id=ck.target LEFT JOIN edges ku ON ku.source=k.id AND ku.type='PART_OF' LEFT JOIN nodes u ON u.id=ku.target AND u.type='LearningUnit' WHERE rc.type='REQUIRES_COMPETENCY' AND rc.source='ROL:PO-GAC' GROUP BY 1 ORDER BY 1;

-- P20. ¿Qué celdas del Atlas no tienen conocimiento (silencios)?
-- Estado: Respondible en parte (límite declarado). Cobertura: 224 de 224 celdas territorio × dominio evaluadas.
-- Celdas territorio × dominio sin ningún pre-ensayo del corpus base de 739 con ambas coordenadas primarias. La cobertura es total por construcción; el estado lo decide el límite declarado. Límite: la consulta no distingue las combinaciones de territorio y dominio que no pueden darse de las que no tienen contenido
SELECT t.id AS territorio, d.id AS dominio FROM nodes t JOIN nodes d ON json_extract(d.properties,'$.axis')='Y' WHERE json_extract(t.properties,'$.axis')='X' AND NOT EXISTS (SELECT 1 FROM edges ex JOIN edges ey ON ey.source=ex.source JOIN nodes p ON p.id=ex.source WHERE ex.type='CLASSIFIED_IN' AND ex.target=t.id AND json_extract(ex.properties,'$.role')='primario' AND ey.type='CLASSIFIED_IN' AND ey.target=d.id AND json_extract(ey.properties,'$.role')='primario' AND p.type='Precursor' AND json_extract(p.properties,'$.capa') IS NULL) ORDER BY 1,2;

-- P21. ¿Qué conceptos de la Biblioteca cognitiva propone cubrir cada unidad del GM-24 y con qué confianza editorial?
-- Estado: Respondible (cobertura de al menos 90 %). Cobertura: 24 de 24 unidades con conceptos propuestos.
-- Una fila por concepto. Solo los vínculos de selección editorial o de ancla expresa de la base; los de coincidencia temática no se cargaron. Es cobertura propuesta, no aprendizaje comprobado.
SELECT u.label AS unidad, b.label AS concepto, b.type AS tipo, json_extract(e.properties,'$.confidence') AS confianza_editorial, json_extract(e.properties,'$.method') AS metodo FROM edges e JOIN nodes u ON u.id=e.source JOIN nodes b ON b.id=e.target WHERE e.type='COVERS_CONCEPT' ORDER BY 1,2;
-- Resumen de P21:
SELECT u.label AS unidad, COUNT(*) AS conceptos FROM edges e JOIN nodes u ON u.id=e.source WHERE e.type='COVERS_CONCEPT' GROUP BY 1 ORDER BY 1;

-- P22. ¿Qué indicadores están clasificados en cada subfunción del Atlas y qué subfunciones no tienen ninguno?
-- Estado: Respondible en parte (límite declarado). Cobertura: 216 de 244 indicadores con subfunción.
-- Una fila por indicador, con el método con que recibió la subfunción. Las subfunciones sin indicador están en el resumen. Límite: La consulta responde «qué indicadores están clasificados en cada subfunción», no «cuáles la miden»: la regla SV-118 no admite MEASURES hacia una subfunción. Los 20 indicadores del sub-plan PO-GAC no tienen coordenada en el Atlas.
SELECT s.id AS subfuncion, i.id AS indicador, i.label AS nombre, json_extract(e.properties,'$.method') AS metodo, json_extract(e.properties,'$.confidence') AS confianza FROM edges e JOIN nodes i ON i.id=e.source AND i.type='SecurityIndicator' JOIN nodes s ON s.id=e.target WHERE e.type='CLASSIFIED_IN' AND json_extract(e.properties,'$.axis')='Zs' ORDER BY 1,2;
-- Resumen de P22:
SELECT s.id AS subfuncion, s.label AS nombre, (SELECT COUNT(*) FROM edges e WHERE e.type='CLASSIFIED_IN' AND e.target=s.id AND e.source LIKE 'IND:%') AS indicadores FROM nodes s WHERE json_extract(s.properties,'$.axis')='Zs' ORDER BY 3, 1;

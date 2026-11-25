# Anexo A8 · Revisión crítica 1.2: encargos y notas de cierre

> **Anexo del Frontier CISO Atlas 1.2.** Reúne, para cada revisor, el encargo que recibió y la nota con que cerró su trabajo. Los insumos, los veredictos y los hallazgos están en la carpeta `revision_critica/`.

## C1 · Encargo

### Encargo C1 · Consistencia interna y cifras

**Objetivo.** Encontrar cifras de los documentos que no coinciden con los datos, contradicciones entre documentos, referencias rotas y afirmaciones que quedaron desactualizadas. No evalúes el fondo conceptual: eso lo hacen otros revisores.

**Qué revisar.** `README.md`, `00_Plan_de_Continuacion_1_1.md`, `docs/01` a `docs/12`, `config/`, `graph/resultados_de_aceptacion.md` y `scripts/LEEME.md`, contra `data/` (JSON y CSV), `graph/` (SQLite y JSON) y `changesets/proposed/`.

**Cómo.** Usá guiones (Python y SQLite), no lectura a ojo:

1. Recalculá desde los datos y compará con lo que dicen los documentos: cardinalidades de la taxonomía; tipos, relaciones, reglas y preguntas de la ontología; organismos, artefactos, discrepancias y silencios de la base de referencia; distribuciones del corpus (territorio, dominio, función, horizonte, pilar, confianza, migraciones, sugerencias); nodos y relaciones del grafo por tipo y por conjunto de cambios; preguntas de competencia por estado; Biblioteca cognitiva (tipos, territorios, vínculos con unidades, vínculos entre prácticas y sesgos); medición (indicadores, subfunciones, variables, órganos, objetivos y resultados clave); remapeo; lectura de D20; pre-ensayos propuestos.
2. Compará tablas equivalentes entre documentos (por ejemplo «Qué cambia» del 01 con «Antes y después» del 11, y las cifras del README con las del 06).
3. Verificá que cada archivo y cada sección que un documento cita exista con ese nombre.
4. Buscá restos de la versión anterior: «1.0» donde debería decir «1.1», «2.0.0» donde debería decir «2.1.0», «7.0», «diez conjuntos», «20 preguntas», «todavía no cargado», pendientes que ya se hicieron.
5. Verificá sumas y porcentajes, y que los CSV y los JSON equivalentes digan lo mismo.
6. Verificá `MANIFEST_SHA256.txt` contra los archivos.

**Salida.** `hallazgos.jsonl` con identificadores `C1-001`, `C1-002`, … y `cierre.md`, en `c1/`.

## C1 · Nota de cierre

### Cierre del revisor C1 · Consistencia interna y cifras

**Qué revisé.** El README, el plan de continuación, los documentos 01 a 12, las instrucciones del curador, los resultados de aceptación y el LEEME, contra `data/`, `graph/` y `changesets/proposed/`. Recalculé con guiones la taxonomía, la ontología, la base de referencia, el corpus, el grafo, las 22 consultas, la Biblioteca, la medición y las tres propuestas. Comparé cada CSV con su JSON, verifiqué el manifiesto, contrasté con el paquete 1.0 y regeneré una copia. El guion `verificar_c1.py` reproduce las cifras.

**Qué no pude revisar.** La regeneración completa: `build_ontology.py` y `construir_grafo.py` necesitan fuentes que no viajan en el paquete. Tampoco los catálogos de origen ni los hechos externos. No evalué el fondo conceptual.

**Los cinco hallazgos más importantes.**

1. C1-013: el catálogo de 85 agentes entró con las columnas corridas; los «puntos de control» del grafo son valores de costo.
2. C1-031: «0 errores» sale de evaluar 13 de las 37 reglas; 1.809 nodos no tienen la descripción que exige SV-003.
3. C1-040: las 7.559 aristas del mapeo llevan un texto genérico en lugar de la versión del artefacto.
4. C1-001: cinco de las 22 fuerzas no presionan ninguna variable, contra lo que afirma el documento 03.
5. C1-010: de los 883 conceptos «con T01», 568 lo llevan como secundario.

**Juicio general.** Las cifras de los documentos salen de los datos y casi todas cierran. Los errores están en frases escritas a mano en los generadores, en la base de referencia, que no se actualizó, y en defectos del grafo que el validador no mira.

**Sin problemas.** El manifiesto, los archivos declarados sin cambio, las distribuciones del corpus, la muestra de control, los conteos de la ontología y del grafo y la reejecución de las 22 consultas, que devuelve lo publicado.

## C2 · Encargo

### Encargo C2 · Taxonomía, decisiones y coherencia

**Contexto.** El autor aceptó en bloque las decisiones D-01 a D-10 «suponiendo que no son contradictorias y apuntan hacia la excelencia y el rigor». Parte de tu tarea es decir si son contradictorias.

**Qué revisar.** `docs/01` (tabla de decisiones), `docs/02`, `docs/03`, `docs/08`, `docs/10` y `docs/11`; `data/taxonomia_v6_0.json`, `data/cruce_elementos_*.csv` y `data/cobertura_dominios_artefactos.csv`.

**Preguntas.**

1. **Criterios de admisión.** ¿Los criterios C1 a C5 se aplicaron igual a los cuatro dominios admitidos (D25 a D28) y a los nueve candidatos de la lista de vigilancia? ¿Hay un candidato rechazado que cumple lo mismo que uno admitido, o uno admitido que no cumple lo que se le exigió a un rechazado?
2. **Fronteras entre dominios.** Buscá solapamientos sin regla de frontera clara: D25 con D08, D10 y D11; D26 con D06; D27 con D08 y D16; D28 con D03, D13 y D22; D19 con D18; D20 con D01, D02, D21, D22 y D23.
3. **Subfunciones.** ¿El vínculo de cada subfunción con las categorías de NIST CSF 2.0 es coherente? Mirá en particular PR03 y PR06, RC04 con ID.IM, y las subfunciones que comparten categoría. ¿Queda alguna categoría de CSF 2.0 sin subfunción?
4. **Eje H.** ¿Cada variable homeostática tiene mecanismos y fuerzas coherentes con su definición? ¿Hay mecanismos, catalizadores o inhibidores que no regulan ni presionan ninguna variable? ¿Las seis variables cubren lo que el propio texto dice que debe mantenerse estable?
5. **Lentes.** ¿Las anclas de los pilares del MCCS son coherentes con sus definiciones y con la decisión D-04 (pilar OS en dos escalas)?
6. **Decisiones.** D-01 a D-10 y ADR-013 a ADR-025: contradicciones, dependencias de orden y decisiones que se pisan. Mirá al menos D-03 con D-07, D-04 con D-08, D-02 con D-10, y ADR-019 con una aceptación en bloque.
7. **Evidencia.** Afirmaciones de la taxonomía que los cruces no respaldan.

**Salida.** `hallazgos.jsonl` con identificadores `C2-001`, … y `cierre.md`, en `c2/`. En el cierre respondé de forma expresa: ¿las diez decisiones son contradictorias entre sí? ¿Qué orden de aplicación exigen?

## C2 · Nota de cierre

### Cierre C2

**Qué revisé.** docs/01, 02, 03, 08, 10 y 11, `taxonomia_v6_0.json`, los cruces y la matriz de cobertura, contrastados con el plan, los anexos A1, A2 y A6, las instrucciones de clasificación, la categorización y el grafo. Registré 82 hallazgos (1 crítico, 14 altos).

**Qué no pude revisar.** Los artefactos externos (sin red), el catálogo 5.3 (ausente del paquete) y cada categorización. Los juicios sobre CSF 2.0 son míos.

**Cinco hallazgos principales.**

1. C2-055: cinco decisiones son preguntas o tareas de validación; la aceptación en bloque no las resuelve ni aprueba el grafo.
2. C2-056 y C2-057: D-02 contiene a D-03, D-04 y D-06; validar la categorización antes de aplicar D-03 aprueba una regla y un corpus que la incumple.
3. C2-044 y C2-058: D-04 choca con D-08, y D-03 con los pre-ensayos de D-10.
4. C2-001 y C2-008: C2 y C5 se aplicaron con dos varas (D28 admitido, W02 rechazado).
5. C2-033 y C2-026: cinco fuerzas no presionan ninguna variable; RC04 depende de una categoría de Identificar.

**¿Las diez decisiones son contradictorias entre sí?** Como textos, no. Aplicadas juntas y sin orden, sí, en cuatro puntos: D-02 con D-07, D-04 con D-08, D-03 con D-10 y la cardinalidad de D-02 con D-08.

**Orden que exigen.** D-01; D-04 y D-06; D-02; D-03 (decidir y aplicar); D-05; D-08 y D-09; D-10; D-07 al final.

**Sin problemas.** Las tablas de docs/03 coinciden con el JSON y el corpus; la matriz de cobertura, con el cruce (salvo NIS2); las 22 categorías de CSF 2.0 tienen subfunción; los 12 mecanismos regulan alguna variable; C1 se sostiene para D25 a D28.

**Juicio general.** El resultado es defendible, pero no por el procedimiento declarado: los criterios cambiaron, se aplicaron de forma desigual y varias reglas usadas no están en lo aprobado.

## C3 · Encargo

### Encargo C3 · Ontología y grafo

**Qué revisar.** `docs/05` y `docs/06`; `data/ontology.json`, `data/entity_dictionary.json`, `data/relationship_dictionary.json` y `data/semantic_rules.json`; `graph/frontier_ciso_atlas_candidato.sqlite`, `graph/consultas_de_aceptacion.sql` y `graph/resultados_de_aceptacion.md`; `changesets/proposed/*.json`; y `scripts/construir_grafo.py`, para entender qué valida.

**Preguntas.**

1. **Diccionarios.** Tipos o relaciones redundantes; definiciones circulares o ambiguas; relaciones cuyos tipos de origen y destino no permiten el uso que el documento describe; propiedades obligatorias incoherentes; reglas de `semantic_rules.json` que la función `validate()` del guion no implementa (listá cuáles se declaran y no se comprueban).
2. **Grafo.** Con SQL sobre la base: nodos sin ninguna relación; etiquetas duplicadas dentro de un tipo y entre tipos; relaciones con evidencia vacía donde la relación la exige; valores de propiedades fuera de catálogo (`role`, `confidence`, `axis`); más de un primario por eje; nodos con rol secundario y sin primario en el mismo eje; indicadores sin función; conceptos de la Biblioteca sin territorio; pre-ensayos sin alguna de sus coordenadas; uso dudoso de una relación (`INFORMS` hacia órganos, `MEASURES` hacia variables, `COVERS_CONCEPT`, `COUNTERS`, `TRACKED_BY`, `ADVANCES`).
3. **Preguntas de competencia.** Ejecutá cada consulta. ¿La consulta responde de verdad la pregunta? ¿El estado declarado (respondible, en parte, todavía no) es honesto?
4. **Conjuntos de cambios.** ¿Las cabeceras coinciden con el contenido (conteos, huella SHA-256 del archivo de operaciones, estados)?
5. **Documentos.** Lo que `docs/05` o `docs/06` afirman y el grafo o los diccionarios no respaldan.

**Salida.** `hallazgos.jsonl` con identificadores `C3-001`, … y `cierre.md`, en `c3/`.

## C3 · Nota de cierre

### Cierre C3 · Ontología y grafo

**Qué revisé.** Revisé docs/05, docs/06, los cuatro diccionarios, los guiones de construcción y de aceptación, la base SQLite (copia; 22 consultas reejecutadas), las 15 cabeceras con sus operaciones y el paquete 1.0. Registré 64 hallazgos: 1 crítico, 7 altos, 34 medios, 17 bajos y 5 observaciones.

**Los cinco más importantes.**

1. C3-001. Los 85 agentes del plano B se cargaron con las columnas corridas: las «compuertas» son costos, y P13 los publica.
2. C3-003 a C3-005. El validador comprueba 13 de 37 reglas; 1.809 nodos no tienen definición y el 90,6 % de los mapeos no registra versión.
3. C3-002. SV-112 se cumple con una justificación que escribe el propio guion.
4. C3-006 y C3-007. El estado de las preguntas de competencia es una constante, y P02, P05 y P08 no pueden expresarse con la ontología.
5. C3-008. Las operaciones de los conjuntos de cambios no llevan la definición de los nodos.

**Sin problemas.** Las tablas de docs/05 (§6 a §9) y docs/06 (§2) coinciden con los diccionarios y la base, igual que las huellas, los conteos y los estados de las 15 cabeceras. Se cumplen dominio, rango, pares, integridad referencial y un primario por eje.

**Qué no pude revisar.** No tuve las fuentes ausentes del paquete (matriz de preguntas, GM-24, base 1404, catálogo CISO 365), por lo que no reejecuté la construcción. Tampoco verifiqué los nombres vigentes de ATT&CK, ATLAS y CCM ni cada clasificación o vínculo. Copié la base en mi carpeta, porque el entorno impide escribir en `/tmp`, y la borré.

**Juicio.** Las cifras son coherentes entre sí, pero la validación y las preguntas de competencia prueban menos de lo que los documentos afirman. Antes de aprobar conviene corregir el plano B y hacer verificables las reglas.

## C4a · Encargo

### Encargo C4a · Segunda lectura independiente del dominio D20

Tu lectura debe ser independiente. **No abras** `docs/07_Categorizacion_del_Corpus.md`, `docs/11_Iteracion_1_1.md`, `data/analisis_D20_decision_D03.*`, `data/corpus_frontier_739.json` ni `data/categorizacion_739.csv`: contienen otra lectura de los mismos casos. Usá solo los archivos de tu carpeta y `comun/REGLAS_ATLAS.md`.

#### Tarea 1 · `d20.jsonl` (71 pre-ensayos que hoy están en D20)

Para cada uno decidí el **dominio primario** con estas reglas de la Taxonomía 6.0:

- **D20 AI & Agent Security:** proteger modelos, agentes, herramientas, datos y entorno de ejecución de IA.
- **Gobierno, riesgo y cumplimiento de la IA:** D01, D02 o D03, con territorio T07.
- Valen las demás reglas de `REGLAS_ATLAS.md` (por ejemplo D17 para cadena de suministro y D28 para el método de aseguramiento o de medición).
- **La tesis manda:** se clasifica por el objeto y la tesis, no por palabras sueltas.

Salida `veredictos_d20.jsonl`, una línea por pre-ensayo:

```
{"id":"AMP-06","dominio":"D01","territorio":"T07","confianza":"alta","motivo":"Una oración basada en la tesis."}
```

`territorio`: si movés el pre-ensayo por la regla de gobierno, riesgo o cumplimiento, corresponde T07; si queda en D20, dejá `territorio_actual` salvo que sea claramente incorrecto.

#### Tarea 2 · `sugerencias.jsonl` (7 pre-ensayos fuera de D20)

Un clasificador anterior sugirió un cambio de dominio o de territorio que no se aplicó. Decidí si la sugerencia es correcta.

Salida `veredictos_sugerencias.jsonl`: `{"id":"…","veredicto":"aceptar|rechazar|dudoso","motivo":"…"}`

#### Hallazgos

Si la regla misma es ambigua o produce resultados incoherentes, registralo en `hallazgos.jsonl` con identificadores `C4a-001`, …

Carpeta de salida: `c4a/`. Incluí `cierre.md`.

## C4a · Nota de cierre

### Cierre C4a

**Qué revisé.** Leí la tesis y el texto de los 71 pre-ensayos de D20 y de las 7 sugerencias, y decidí con `REGLAS_ATLAS.md`. Resultado: 35 quedan en D20; 15 pasan a D01, 6 a D02 y 1 a D03, todos con T07; 11 pasan a D28, 2 a D17 y 1 a D14, con su territorio vigente. Confianza: 30 alta, 33 media y 8 baja. Acepté las 7 sugerencias, juzgadas por la tesis y no por la política de migración.

**Qué no pude revisar.** Por el encargo no abrí el paquete ni la otra lectura, así que no sé cómo aplicó el paquete la regla 7. Los textos llegan cortados a 1.100 caracteres.

**Cinco hallazgos principales.**

1. C4a-001: la política de migración y la nota de D20 contradicen la regla 7.
2. C4a-002: los 11 casos de D20 con territorio T08 siguen en D20 y 8 corresponden a D28.
3. C4a-003: falta la precedencia entre D20 y las disciplinas que no nombran la IA (11 casos).
4. C4a-010: cuatro errores que el clasificador llamó evidentes siguen sin corregir.
5. C4a-004: cinco pares casi gemelos se separan por el marco «Ante el auditor».

**Juicio general.** El núcleo de D20 es sólido: 18 casos de protección de modelos, agentes, herramientas y memoria quedan con confianza alta, igual que 7 de gobierno y 4 de riesgo. La frontera es débil en tres zonas: aseguramiento (D28), inventarios y compuertas de aprobación. Allí el veredicto depende de un criterio que las reglas no escriben, y lo declaré en cada motivo.

**Sin problemas.** La regla 3 (D25) resolvió el caso de arquitectura agéntica, las reglas 4 y 5 no hicieron falta, y la mención explícita de MCP, A2A y memoria en D20 resolvió los casos de conectores y memoria.

## C4b · Encargo

### Encargo C4b · Segunda lectura independiente de 73 migraciones de dominio

Esta lectura es independiente de otra que ya existe. **No abras** `docs/07_Categorizacion_del_Corpus.md`, `data/corpus_frontier_739.json`, `data/categorizacion_739.csv` ni `anexos/A6_Notas_de_los_clasificadores.md` del paquete: contienen la otra lectura. Usá solo `migraciones.jsonl` y `comun/REGLAS_ATLAS.md`.

#### Tarea · `migraciones.jsonl` (73 pre-ensayos, cada uno con su dominio de la versión 5.3 en `dominio_5_3`)

Para cada pre-ensayo decidí el **dominio primario en la Taxonomía 6.0**. Regla: se conserva el dominio 5.3 salvo que el objeto del texto corresponda a un dominio nuevo de la 6.0:

- **D25** cuando el objeto es la arquitectura empresarial de seguridad o un principio transversal (Zero Trust, seguro por diseño); el control de un pilar concreto queda en el dominio del pilar.
- **D26** cuando el objeto es la disciplina criptográfica (claves, certificados, poscuántica); el cifrado como un control más de protección de datos queda en D06.
- **D27** cuando el objeto es la seguridad física, ambiental o de instalaciones, o el mantenimiento como dependencia del control.
- **D28** cuando el objeto es el método para demostrar o medir la eficacia (auditoría, pruebas, evidencia, métricas); la obligación y su conformidad quedan en D03; el riesgo con la métrica como medio queda en D02; la IA como instrumento de prueba queda en D22.

Salida `veredictos_migraciones.jsonl`, una línea por pre-ensayo: `{"id":"…","dominio":"D28","confianza":"alta|media|baja","motivo":"Una oración apoyada en la tesis."}`

Guardá cada 12 ítems.

#### Hallazgos

Problemas de las reglas (ambigüedades, fronteras que no deciden) en `hallazgos.jsonl`, con identificadores `C4b-001`, …

Carpeta de salida: `c4b/`. Incluí `cierre.md`.

## C4b · Nota de cierre

### Cierre C4b

**Qué revisé.** Leí la tesis y el texto de los 73 pre-ensayos de `migraciones.jsonl` y decidí su dominio 6.0 solo con `REGLAS_ATLAS.md` y el encargo. Resultado: D28 52, D25 13, D26 5; tres conservan el dominio 5.3 (APC-088 y APA-175 en D02, APF-12 en D05). Confianza: alta 44, media 28 (el motivo nombra la lectura rival) y baja 1 (la regla no decide).

**Qué no pude revisar.** No abrí el paquete ni la otra lectura: no sé cuántos veredictos coinciden. La regla de D27 quedó sin probar porque ningún texto trata la seguridad física. Llegan cortados 52 textos y 26 tesis; no pude comprobar si el texto completo cambiaría algún veredicto.

**Cinco hallazgos principales** (17 en total).

1. C4b-001: la regla 6 no tiene la cláusula de pilar de la regla 3; doce ítems dependen de ella.
2. C4b-002: D03 conserva «auditoría» y se superpone con D28.
3. C4b-004: la IA como instrumento de prueba no tiene destino coherente si el origen es D03.
4. C4b-005: la regla 7 no ubica el aseguramiento de la IA, objeto de 8 de los 10 ítems de D20.
5. C4b-006: la validación de modelos de riesgo queda entre D02 y D28.

**Sin problemas.** Las reglas de D26 y D25 deciden bien sus casos nucleares: criptografía y poscuántica (4 ítems) y arquitectura, Zero Trust y seguro por diseño (10) salieron con confianza alta. También las pruebas y el aseguramiento genéricos (M3.2, G3.2-K02, AMP-13).

**Juicio general.** Las reglas de D25 y D26 deciden la migración con solidez. La de D28 decide el núcleo, pero D28 se define por el método y los demás dominios por el objeto: 22 de sus 52 ítems dependen de fronteras que las reglas no fijan. Conviene resolver C4b-001 antes de publicar el recuento de D28.

## C4c · Encargo

### Encargo C4c · Segunda lectura independiente de una muestra de 47 pre-ensayos

Esta lectura es independiente de otra que ya existe. **No abras** `docs/07_Categorizacion_del_Corpus.md`, `data/corpus_frontier_739.json`, `data/categorizacion_739.csv` ni `anexos/A6_Notas_de_los_clasificadores.md` del paquete: contienen la otra lectura. Usá solo `muestra.jsonl` y `comun/REGLAS_ATLAS.md`.

#### Tarea · `muestra.jsonl` (47 pre-ensayos)

Asigná a cada uno, desde cero, **territorio, dominio y subfunción primarios**, con los catálogos y las reglas de asignación de `comun/REGLAS_ATLAS.md`. Se clasifica por el objeto y la tesis del texto, no por palabras sueltas.

Salida `veredictos_muestra.jsonl`, una línea por pre-ensayo: `{"id":"…","territorio":"T04","dominio":"D02","subfuncion":"GV04","confianza":"alta|media|baja","motivo":"Una oración apoyada en la tesis."}`

Guardá cada 12 ítems.

#### Hallazgos

Problemas de las reglas (ambigüedades, fronteras que no deciden) en `hallazgos.jsonl`, con identificadores `C4c-001`, …

Carpeta de salida: `c4c/`. Incluí `cierre.md`.

## C4c · Nota de cierre

### Cierre C4c

**Qué revisé.** Clasifiqué desde cero los 47 pre-ensayos de `muestra.jsonl` (territorio, dominio y subfunción primarios) solo con `comun/REGLAS_ATLAS.md`: 14 veredictos de confianza alta, 24 media y 9 baja. Registré 19 hallazgos sobre las reglas.

**Qué no pude revisar.** Por encargo no abrí la categorización existente ni el corpus: no comparé lecturas ni medí el efecto sobre cifras publicadas, y por eso ningún hallazgo lleva severidad alta. Leí textos cortados (40 de 47 miden 1.100 caracteres) y no comprobé si el campo «tesis» del paquete tiene ese corte.

**Cinco hallazgos.**

1. C4c-001: el eje Y mezcla disciplina y objeto sin regla de precedencia (5 ítems).
2. C4c-002: la regla 7 no fija el territorio de las disciplinas operativas aplicadas a agentes.
3. C4c-005: la regla 6 no dice si medir una capacidad concreta va a D28 o a su dominio.
4. C4c-007: el eje X no distingue la perspectiva del objeto de la del interlocutor (9 tesis).
5. C4c-018: en 20 ítems el campo «tesis» no contiene una tesis utilizable, contra la regla 1.

**Juicio general.** Los catálogos alcanzan para ubicar cada texto, pero las reglas deciden pocos cruces. El territorio es la coordenada menos estable: concentra la duda en 14 de los 24 veredictos de confianza media. No ubiqué ningún ítem en D20: en 17 de las 18 tesis que nombran la IA el dominio fue la disciplina o el pilar. Espero desacuerdo con la otra lectura en T07 frente a T06, T04 frente a T08 y D20 o D28 frente a la disciplina.

**Sin problemas.** La regla 6 decidió G4.2-K09. Identidad (D05 con PR01), hunting (D14 con DE03) y apetito (D02 con GV04) dieron confianza alta en sus 8 ítems. Las reglas 4, 5 y 8 no se pusieron a prueba.

## C4d · Encargo

### Encargo C4d · Segunda lectura independiente de una muestra de 40 pre-ensayos

Esta lectura es independiente de otra que ya existe. **No abras** `docs/07_Categorizacion_del_Corpus.md`, `data/corpus_frontier_739.json`, `data/categorizacion_739.csv` ni `anexos/A6_Notas_de_los_clasificadores.md` del paquete: contienen la otra lectura. Usá solo `muestra.jsonl` y `comun/REGLAS_ATLAS.md`.

#### Tarea · `muestra.jsonl` (40 pre-ensayos)

Asigná a cada uno, desde cero, **territorio, dominio y subfunción primarios**, con los catálogos y las reglas de asignación de `comun/REGLAS_ATLAS.md`. Se clasifica por el objeto y la tesis del texto, no por palabras sueltas.

Salida `veredictos_muestra.jsonl`, una línea por pre-ensayo: `{"id":"…","territorio":"T04","dominio":"D02","subfuncion":"GV04","confianza":"alta|media|baja","motivo":"Una oración apoyada en la tesis."}`

Guardá cada 12 ítems.

#### Hallazgos

Problemas de las reglas (ambigüedades, fronteras que no deciden) en `hallazgos.jsonl`, con identificadores `C4d-001`, …

Carpeta de salida: `c4d/`. Incluí `cierre.md`.

## C4d · Nota de cierre

### Cierre C4d · Segunda lectura independiente de 40 pre-ensayos

**Qué revisé.** Leí `comun/FORMATO.md`, `comun/REGLAS_ATLAS.md`, el encargo y los 40 registros de `muestra.jsonl`. Clasifiqué cada pre-ensayo por su tesis y su caso, uno por uno, sin guiones de asignación. No abrí el paquete, `sorteo.json` ni las carpetas de otros revisores. Guardé 40 veredictos: 4 con confianza alta, 31 con media y 5 con baja.

**Qué no pude revisar.** Los textos llegan cortados (C4d-016): no leí el desarrollo completo de 37 pre-ensayos. No contrasté las subcategorías del CSF 2.0 con su fuente, porque no usé la red; me apoyé en las categorías entre corchetes del catálogo. No comparé con la otra lectura, por diseño.

**Cinco hallazgos principales.**

1. C4d-003: el gobierno (D01) no tiene territorio y ninguna regla elige entre T02, T03 y T08.
2. C4d-001: el eje Z no tiene subfunción para el tratamiento del riesgo.
3. C4d-004: un texto sobre un marco entero (CSF, Govern, ISO 22301) no tiene subfunción primaria que decida.
4. C4d-009 y C4d-008: las reglas 1 y 7 chocan cuando la IA es materia y no objeto, y la regla 7 no cubre disciplinas fuera de D01 a D03.
5. C4d-006: T03 y T06 reclaman el producto-control.

**Sin problemas.** La regla 6 bastó para decidir D28 en M3.2-PA03 y D03 en APN-43. La regla 1 descartó D21 y D23 en SOAR. Los dominios D16 y D17 se asignaron sin alternativa.

**Juicio general.** El dominio es el eje más estable y la subfunción el más débil: nombré una subfunción alternativa en 27 de los 40 motivos, un territorio alternativo en 20 y un dominio alternativo en 13. Las discrepancias de subfunción con la otra lectura deberían leerse primero como falta de regla. Los 16 hallazgos son de severidad media (11) o baja (5); ninguno invalida la taxonomía.

## C5a · Encargo

### Encargo C5a · Biblioteca cognitiva: tipos y pilar del MCCS

**Contexto.** La Biblioteca cognitiva del CISO de frontera tiene 1.404 conceptos en 11 categorías (`categorias.json`). Entraron al grafo candidato con un tipo asignado por categoría. Los tipos disponibles son:

- `MentalModel`: modelo o marco de razonamiento que orienta cómo se interpreta una situación y se decide.
- `CognitiveBias`: sesgo, heurística defectuosa o falacia que puede distorsionar un juicio.
- `MetacognitivePractice`: práctica deliberada de decisión, de análisis o de revisión del propio razonamiento antes, durante o después de decidir.
- `HumanCapability`: capacidad humana que sostiene el desempeño: función ejecutiva, capacidad cognitiva, habilidad socioemocional o mentalidad.
- `Concept`: concepto abstracto; se usa solo cuando ninguno de los cuatro anteriores corresponde.

#### Tarea 1 · `mixtos.jsonl` (213 conceptos de tres categorías que mezclan cosas distintas)

Asigná el tipo leyendo el nombre y la definición.

Salida `veredictos_mixtos.jsonl`: `{"id":"META-0009","tipo":"MetacognitivePractice","confianza":"alta|media|baja","motivo":"Una oración."}`

#### Tarea 2 · `muestra_tipos.jsonl` (120 conceptos de las otras ocho categorías, con el tipo que les dio la regla)

Decí si el tipo de la regla es correcto para ese concepto.

Salida `veredictos_muestra_tipos.jsonl`: `{"id":"…","veredicto":"conforme|excepcion","tipo":"el tipo correcto","motivo":"…"}`

#### Tarea 3 · Pilar del MCCS por categoría

Hoy las 11 categorías llevan el pilar MM. El autor aceptó que el pilar OS se lee en dos escalas: individual (energía, atención y resiliencia) y de oficina (derechos de decisión, cadencias, datos, agentes y evidencia). Las definiciones de los cuatro pilares están en `comun/REGLAS_ATLAS.md`. Recomendá el pilar de cada categoría y decí si alguna necesita dividirse.

Salida `pilares_por_categoria.json`: `{"sesgo cognitivo":{"pilar":"MM","motivo":"…","excepciones":"…"}, …}` con las 11 categorías de `categorias.json`.

#### Hallazgos

Problemas de la regla de tipos o de la lente, en `hallazgos.jsonl` con identificadores `C5a-001`, …

Carpeta de salida: `c5a/`. Incluí `cierre.md`.

## C5a · Nota de cierre

### Cierre del revisor C5a

**Qué revisé.** Leí nombre y definición de los 213 conceptos mixtos y de los 120 de la muestra, con un veredicto por concepto. Para los pilares leí además nombres y comienzos de definición de otras cinco categorías completas. Contrasté con el grafo y el diccionario de entidades.

**Resultado.** Los 213 quedan en 101 Concept, 41 CognitiveBias, 31 HumanCapability, 24 MetacognitivePractice y 16 MentalModel; 71 cambian respecto de la regla. En los 120 hay 8 excepciones. Recomiendo OS para función ejecutiva, factor humano y habilidad socioemocional, y MM para las otras ocho. Necesitan dividirse mindset, factor humano y habilidad socioemocional.

**Criterio.** CognitiveBias cubre toda distorsión sistemática de percepción, memoria, creencia o juicio; MentalModel va en sentido estricto.

**Cinco hallazgos principales.**
1. C5a-001: un mismo concepto recibe tipos distintos según la categoría (30 grupos, 70 conceptos).
2. C5a-004: los 1.404 llevan MM contra el ancla del diccionario; unos 270 corresponden a otro pilar.
3. C5a-002: 71 de los 172 Concept tienen tipo específico; cambian las cinco cifras por tipo.
4. C5a-007 y C5a-006: práctica de decisión y mindset también mezclan cosas distintas.
5. C5a-010: falta un tipo para estados como la fatiga o la carga cognitiva.

**Sin problemas.** Sesgo cognitivo, falacia lógica, capacidad cognitiva y habilidad socioemocional dieron 60 conformes de 60. La regla de la primera palabra acertó en los 41 casos en que asignó un tipo.

**No pude comprobar.** Los conteos por pilar de cinco categorías son aproximados. No medí cuántos vínculos entre prácticas y sesgos se pierden, porque la base original no está en el paquete. Los 126 veredictos de confianza media o baja piden decisión del curador.

**Juicio general.** La regla por categoría sirve como primera carga, no como tipificación aceptable. Conviene deduplicar y tipar por concepto antes de aprobar D-08.

## C5b · Encargo

### Encargo C5b · Biblioteca cognitiva: prácticas contra sesgos y territorios

#### Tarea 1 · `practicas_contra_sesgos.jsonl` (142 pares práctica → sesgo)

Cada par dice que una práctica contrarresta un sesgo. Salen de dos lugares de la base del autor: de la definición de la práctica (7) o de los «controles compensatorios» de la ficha del sesgo (135, con textos que se repiten por familias de sesgos). El emparejamiento se hizo por coincidencia de nombre.

Veredicto por par:

- `sostenible`: por las definiciones de ambos y por el texto de la base, la práctica contrarresta de forma específica ese sesgo.
- `debil`: la relación es genérica (la práctica mejoraría cualquier decisión) o el texto es una fórmula repetida que no dice nada propio de ese sesgo.
- `incorrecto`: no hay relación, o la coincidencia de nombre tomó un concepto equivocado.

Salida `veredictos_practicas.jsonl`: `{"practica":"DP-0098","sesgo":"BIAS-0103","veredicto":"sostenible","motivo":"…"}`

#### Tarea 2 · `territorios_muestra.jsonl` (100 conceptos con sus territorios editoriales)

Decí si los territorios asignados son plausibles para el concepto, con los alcances de `comun/REGLAS_ATLAS.md`.

Salida `veredictos_territorios.jsonl`: `{"id":"…","veredicto":"plausible|dudoso","territorios_sugeridos":["T01"],"motivo":"…"}`

#### Hallazgos

Patrones de error (por ejemplo, una fórmula de control compensatorio que se aplica a sesgos donde no corresponde) en `hallazgos.jsonl`, con identificadores `C5b-001`, …

Carpeta de salida: `c5b/`. Incluí `cierre.md`.

## C5b · Nota de cierre

### Cierre del revisor C5b

**Qué revisé.** Leí uno por uno los 142 vínculos «la práctica contrarresta el sesgo» y los 100 conceptos de la muestra de territorios. Consulté en solo lectura la base del autor (`Base_1404_Atlas_GM24.json`), el guion de extracción y el grafo candidato.

**Resultado.** Prácticas: 57 sostenibles, 77 débiles y 8 incorrectos. Territorios: 51 plausibles y 49 dudosos. Hallazgos: 17.

**Los cinco hallazgos principales.**

1. C5b-001: solo 57 de los 142 vínculos se sostienen y cambia el orden de las prácticas más conectadas.
2. C5b-002: seis vínculos de «Listas de verificación» son duplicados que creó la subcadena «checklist».
3. C5b-012: los territorios son el valor por defecto de cada categoría en el 92 % de los conceptos.
4. C5b-013: 97 conceptos tienen de cuatro a siete territorios, según su prioridad editorial.
5. C5b-014: ningún sesgo tiene territorio primario y 316 modelos y prácticas reciben T03, contra la lente MM.

**Sin problemas.** Las cifras publicadas (142, 16, 103, 35 y 883, 598, 346) coinciden con los datos. Se sostienen seis de los siete vínculos tomados de definiciones y 27 de los 32 que vienen de textos escritos para un solo sesgo. T01 es correcto en 67 de sus 70 asignaciones de la muestra.

**Qué no pude revisar.** Los otros 1.304 conceptos, los 792 vínculos con unidades del GM-24 y los vínculos que la extracción no generó, que solo conté. Mis veredictos son juicio sobre definiciones: no consulté literatura externa, y 10 vínculos sostenibles se apoyan en definiciones que la base declara provisionales.

**Juicio general.** La carga es fiel a la base y declara sus límites, pero ni los vínculos COUNTERS ni los territorios son conocimiento curado. Conviene conservar los vínculos sostenibles, retirar los incorrectos y reasignar los territorios por concepto antes de decidir D-08.

## C5c · Encargo

### Encargo C5c · Duplicados entre la Biblioteca cognitiva y el corpus de pre-ensayos

**Contexto.** El grafo candidato tiene dos familias de nodos que pueden nombrar lo mismo: los 1.404 conceptos de la Biblioteca cognitiva del CISO de frontera (`biblioteca_nombres.txt`: identificador | nombre | tipo) y los 739 pre-ensayos del corpus (`corpus_titulos.txt`: identificador | título). Nadie buscó duplicados entre ambas. Un duplicado no se fusiona: se declara con una relación de equivalencia para que el curador decida.

#### Tarea 1 · `candidatos.jsonl` (60 pares hallados por similitud de nombre)

Decí si nombran lo mismo.

#### Tarea 2 · Búsqueda propia

Con las dos listas, buscá pares que nombren el mismo concepto con otras palabras (por ejemplo, un sesgo de la Biblioteca y un pre-ensayo sobre ese sesgo; un modelo mental y un pre-ensayo con el nombre en inglés). Podés apoyarte en guiones para generar candidatos, pero el veredicto lo das leyendo. Agregá hasta 80 pares con la clave `"hallado_por":"revisor"`. Priorizá los que son el mismo concepto.

#### Salida

`veredictos_duplicados.jsonl`: `{"biblioteca":"MM-0021","corpus":"M3.1-K08","veredicto":"mismo_concepto|relacionado|distinto","motivo":"…","hallado_por":"similitud|revisor"}`

- `mismo_concepto`: nombran lo mismo; el curador debería tratarlos como equivalentes.
- `relacionado`: el pre-ensayo trata el concepto, pero su objeto es más amplio o distinto.
- `distinto`: la coincidencia es solo de palabras.

#### Hallazgos

Patrones (por ejemplo, familias enteras duplicadas) en `hallazgos.jsonl`, con identificadores `C5c-001`, …

Carpeta de salida: `c5c/`. Incluí `cierre.md`.

## C5c · Nota de cierre

### Cierre C5c · Duplicados entre la Biblioteca y el corpus

**Qué revisé.** Los 60 candidatos por similitud de nombre y 78 pares de búsqueda propia. Leí las dos listas completas, generé candidatos con guiones (nombre normalizado, mención en la tesis, parecido entre definición y tesis) y di cada veredicto leyendo la definición y la tesis. Criterio: «mismo concepto» si coinciden objeto y nivel; «relacionado» si el pre-ensayo aplica, especializa o presupone el concepto; «distinto» si solo coinciden palabras.

**Resultado.** Candidatos: 11 mismo concepto, 31 relacionados y 18 distintos. Búsqueda propia: 10, 60 y 8. Total: 21 equivalencias.

**Qué no pude revisar.** No comparé cada concepto con cada pre-ensayo: puede haber más pares relacionados. Cinco equivalencias lo son por definición y no por nombre; necesitan confirmación del curador. No revisé los 618 vínculos de cobertura temática ni busqué dobletes internos de forma sistemática.

**Hallazgos principales.**

1. C5c-001: 21 equivalencias sin declarar; cada concepto existe tres veces en el grafo.
2. C5c-002: la ontología 2.1.0 no tiene relación para declararlas ni para vincular tipos cognitivos con conceptos.
3. C5c-003: al menos 28 vínculos de cobertura nacen de homonimias («activo», «identidad», «prueba»).
4. C5c-004: la Biblioteca tiene al menos 25 dobletes internos, 4 con dos tipos.
5. C5c-006: la similitud de nombre acertó en el 18 % de sus candidatos y omitió el 48 % de las equivalencias.

**Sin problemas.** Las listas coinciden con el paquete en identificadores, nombres y títulos. Las seis coincidencias exactas de nombre que no son «Comunicación» resultaron equivalentes. No encontré homonimias en los 7 vínculos de cobertura por ancla de la guía de caso que vi.

**Juicio general.** Las dos familias son complementarias: la duplicación real es pequeña y está acotada. Lo pendiente es vincular más que deduplicar, y hoy la ontología no lo permite.

## C6a · Encargo

### Encargo C6a · Medición: indicadores por variable homeostática

Esta lectura es independiente de otra que ya existe. **No abras** `data/indicadores_y_variables_homeostaticas.csv`, `data/indicadores_ciso365_en_el_atlas.csv`, `docs/06_Grafo_de_Conocimiento.md` ni `docs/11_Iteracion_1_1.md` del paquete: contienen la otra lectura. Usá `indicadores.jsonl` (224 indicadores con nombre y fórmula) y `comun/REGLAS_ATLAS.md`.

#### Tarea

Las seis variables homeostáticas (HV01 a HV06) están definidas en `comun/REGLAS_ATLAS.md`, sección «Variables homeostáticas». Para cada variable elegí, entre los 224 indicadores:

- `principal`: los indicadores cuya fórmula mide de forma directa lo que define la variable (hasta 8).
- `apoyo`: los indicadores que dan una señal indirecta (hasta 10).

#### Salida

`variables.json`, con un fundamento de una oración por indicador:

```
{"HV01":{"principal":[{"indicador":"K25","motivo":"…"}],"apoyo":[{"indicador":"K63","motivo":"…"}]}, "HV02":{…}, "HV03":{…}, "HV04":{…}, "HV05":{…}, "HV06":{…}}
```

Guardá el archivo después de completar cada variable, para no perder trabajo.

#### Hallazgos

Si una variable no tiene ningún indicador que la mida de forma directa, o si un indicador tiene una categoría de CSF que parece equivocada, registralo en `hallazgos.jsonl` con identificadores `C6a-001`, …

Carpeta de salida: `c6a/`. Incluí `cierre.md`.

## C6a · Nota de cierre

### Cierre C6a · Medición: indicadores por variable homeostática

**Qué revisé.** Leí los 224 indicadores de `indicadores.jsonl` (nombre, fórmula y categoría de CSF) contra las seis variables de `REGLAS_ATLAS.md`. En `variables.json` propongo 39 principales y 60 de apoyo. Es principal el indicador cuya fórmula contiene la relación que define la variable (en HV06, la continuidad o la recuperación comprobada de lo crítico); es de apoyo el que mide una condición previa, un regulador, una presión o un resultado parcial. Los candidatos excluidos por el tope están en `trabajo/candidatos_completos.json`.

**Qué no pude revisar.** No abrí los cuatro archivos vedados del paquete; cito el catálogo por su extracto. Usé de memoria las definiciones de CSF 2.0: no hay red y las reglas solo traen códigos. K04, K38, K50 y K58 remiten a criterios que el extracto no enumera. No sé si los 22 indicadores KX, sin función de CISO365, son una omisión o una familia aparte.

**Cinco hallazgos principales.**
1. C6a-001: HV03 no mide el ritmo de cambio ni los cambios fallidos o revertidos.
2. C6a-006: K54 y K144 miden lo mismo con categorías distintas.
3. C6a-007: K185 y K186 están en RC.RP y no miden ejecución de la recuperación.
4. C6a-005: K152 mide contención y está en DE.CM.
5. C6a-003 y C6a-002: HV04 no mide la confianza del equipo y HV05 casi no mide al CISO.

**Juicio general.** Las seis variables tienen al menos un indicador directo. HV01, HV02 y HV06 quedan bien medidas; HV04, salvo para el equipo; HV03 y HV05, de forma parcial. Objeto la categoría de CSF de 14 indicadores con severidad media y dejo cuatro observaciones sobre casos dudosos.

**Sin problemas.** No encontré categorías dudosas en GV.RR, GV.SC, ID.AM, PR.AA, PR.AT, PR.IR, DE.AE, RS.AN, RS.CO ni RC.CO (89 indicadores).

## C6b · Encargo

### Encargo C6b · Medición: territorio y dominio de 160 indicadores

**Contexto.** El catálogo tiene 224 indicadores. Sesenta y cuatro ya tienen territorio y dominio del Atlas (`ejemplos_con_coordenada.jsonl`: sirven de ejemplo). Los otros 160 (`indicadores_sin_coordenada.jsonl`) solo tienen función y, a veces, subfunción.

**Tarea.** Asigná a cada uno de los 160 un **territorio primario** y un **dominio primario**, y hasta dos dominios secundarios, con los catálogos y reglas de `comun/REGLAS_ATLAS.md`. El territorio es la perspectiva o responsabilidad desde la que se mira; el dominio es la disciplina u objeto que el indicador mide. Clasificá por lo que el indicador mide (nombre y fórmula), no por palabras sueltas.

Salida `veredictos_coordenada.jsonl`: `{"id":"K65","territorio":"T03","dominio":"D01","dominios_secundarios":["D04"],"confianza":"alta|media|baja","motivo":"Una oración."}`

**Hallazgos.** Indicadores que no encajan en ningún dominio, o reglas que no deciden, en `hallazgos.jsonl` con identificadores `C6b-001`, …

Carpeta de salida: `c6b/`. Incluí `cierre.md`.

## C6b · Nota de cierre

### Cierre C6b

**Qué revisé.** Leí los 64 ejemplos, con su definición en el grafo, y los 160 indicadores sin coordenada, uno por uno, por nombre y fórmula. Coordenada propuesta: T01 2, T02 16, T03 18, T04 25, T05 34, T06 34, T07 8 y T08 23. Confianza: 98 alta, 59 media y 3 baja (K101, KX19 y KX22).

**Criterios propios.** Donde las reglas callan: estado de un control en T05 y corrección medida en el tiempo en T06 (K35, K39, K46, K47); dominio del pilar cuando la verificación recae sobre un pilar, con D28 secundario; regla 7 para K88 y K98.

**Qué no pude revisar.** No vi el catálogo de origen. No revisé las subfunciones de forma sistemática ni hubo segunda lectura.

**Hallazgos principales.**
1. C6b-001: los 64 ejemplos no usan dominios nuevos; K60 es D28 y sigue en D03.
2. C6b-002: la frontera T05/T06 no está decidida para 12 indicadores de corrección.
3. C6b-003: la regla 6 no da precedencia entre D28 y el dominio del pilar (11 indicadores).
4. C6b-004: la postura queda entre D13 y D10: K35 y K141 miden lo mismo.
5. C6b-007: la subfunción salió de la categoría CSF; ID.IM no puede caer en RC04, donde están los ejemplos.

**Sin problemas.** Ningún indicador quedó sin dominio posible; K101 y K125 encajan solo por extensión. El lote coincide con el CSV del paquete en categoría y subfunción. Las reglas 3 y 4 decidieron sin ambigüedad K116, K117 y K156.

**Juicio general.** La coordenada es asignable: 98 veredictos son firmes y 62 dependen de fronteras que las reglas no cierran; conviene decidirlas antes de cargarla al grafo. Los 64 ejemplos necesitan la misma migración a 6.0 que el corpus, o quedarán dos criterios.

## C6c · Encargo

### Encargo C6c · Medición: subfunción de 71 indicadores y siete ubicaciones a confirmar

Usá los archivos de tu carpeta y `comun/REGLAS_ATLAS.md` (sección «Funciones y subfunciones», con la categoría de NIST CSF 2.0 de cada subfunción).

#### Tarea 1 · `indicadores_sin_subfuncion.jsonl` (71 indicadores)

Estos indicadores tienen función pero no subfunción, porque su categoría de NIST CSF 2.0 corresponde a más de una subfunción del Atlas. Para cada uno elegí la subfunción entre `subfunciones_candidatas`, según lo que mide (nombre y fórmula). Si ninguna candidata corresponde, proponé otra subfunción de la misma función.

Salida `veredictos_subfuncion.jsonl`, una línea por indicador: `{"id":"K65","subfuncion":"GV02","confianza":"alta|media|baja","motivo":"Una oración."}`

Guardá cada 20 indicadores.

#### Tarea 2 · `ubicaciones_a_confirmar.jsonl` (7 indicadores)

Se propuso: K36, K159, K160 y K193 en PR06 (resiliencia de la infraestructura y protección física y ambiental); K189 en RC05 (comunicación de la recuperación); K117 y K119 en PR03 (hardening y arquitectura segura). Decí si cada ubicación es correcta.

Salida `veredictos_ubicacion.jsonl`: `{"id":"K36","subfuncion":"la que corresponde","veredicto":"de_acuerdo|en_desacuerdo","motivo":"Una oración."}`

#### Hallazgos

Problemas de las reglas (por ejemplo, dos subfunciones que no se distinguen para un tipo de indicador) en `hallazgos.jsonl`, con identificadores `C6c-001`, …

Carpeta de salida: `c6c/`. Incluí `cierre.md`.

## C6c · Nota de cierre

### Cierre C6c

**Qué revisé.** Los 71 indicadores sin subfunción y las siete ubicaciones, por nombre y fórmula. Contrasté cada elección con los 64 precedentes del catálogo 1.2, la categorización del corpus y `scripts/extraer_medicion.py`.

**Resultado.** 71 subfunciones propuestas: 46 con confianza alta, 23 media y 2 baja (K116 y K128). K72 (GV03) y K98 (GV02) quedan fuera de las candidatas porque ninguna corresponde. Ubicaciones: de acuerdo con K117 y K119 en PR03 y con K189 en RC05; en desacuerdo con K36, K159, K160 y K193, que corresponden a PR03 y no a PR06.

**Qué no pude revisar.** El catálogo de origen no está en el paquete: usé su extracto. No revisé los 36 indicadores con subfunción automática de DE.CM, ID.IM y GV.SC ni los vínculos con variables homeostáticas. Sin definición de las subfunciones, los veredictos de confianza media o baja se apoyan en precedentes y necesitan al curador.

**Cinco hallazgos principales.**

1. C6c-001: los cuatro indicadores de PR06 miden red y acceso; ubicados por objeto, PR06 queda sin indicadores.
2. C6c-002: el script asigna subfunción a 41 indicadores cuya categoría corresponde a varias, contra la regla documentada.
3. C6c-003: conviven dos criterios de ubicación; KX07 «equivale a K62» y están en GV09 y RS04.
4. C6c-004: las 34 subfunciones no tienen definición.
5. C6c-005: DE02, DE03 y DE04 no se distinguen para la prueba y la revisión de detecciones.

**Sin problemas.** K189 en RC05 y K117 y K119 en PR03. Los grupos ID.AM, GV.RR y GV.OC se resolvieron con confianza alta en 19 de 23 casos.

**Juicio general.** La categoría de CSF sirve como punto de partida, pero no reemplaza la ubicación por objeto que exige la regla 1. Las propuestas de confianza alta pueden integrarse; las demás requieren definir antes las subfunciones.

## C7a · Encargo

### Encargo C7a · Verificación externa: ATT&CK, ATLAS y CCM

Fecha de referencia: 15 de noviembre de 2026. Solo fuentes oficiales (attack.mitre.org, atlas.mitre.org, cloudsecurityalliance.org y sus repositorios oficiales). No uses blogs de terceros como prueba. Si no podés confirmar algo, decilo: no completes con memoria.

#### A. Afirmaciones a confirmar o refutar

1. La versión vigente de MITRE ATT&CK es la v20 y la matriz Enterprise tiene 15 tácticas.
2. En la v19 (28 de abril de 2026) la táctica TA0005 dejó de llamarse «Defense Evasion» y pasó a llamarse «Stealth», y se agregó la táctica TA0112 «Defense Impairment».
3. La versión vigente de MITRE ATLAS es la v2026.10 y tiene 16 tácticas.
4. En ATLAS v2026.08 la táctica «AI Attack Staging» pasó a llamarse «AI Attack Adaptation».
5. En ATLAS, «Command and Control» es AML.TA0014 y «Lateral Movement» es AML.TA0015.
6. La versión vigente de CSA Cloud Controls Matrix es la v4.1; tiene 207 objetivos de control en 17 dominios; el dominio «Infrastructure & Virtualization Security (IVS)» de la v4 pasó a identificarse como «I&S».

#### B. Preguntas

7. Definición oficial vigente de TA0005 Stealth y de TA0112 Defense Impairment (cita breve y URL). ¿Qué criterio separa las técnicas de una y otra? Nombrá entre cinco y diez técnicas representativas de cada una.
8. Cinco conceptos de un programa de formación de CISO (inteligencia de amenazas, threat hunting, ciclo de vida de la inteligencia, tácticas-técnicas-procedimientos e indicadores de compromiso) tenían un vínculo con «TA0005 Defense Evasion» en un mapeo hecho con ATT&CK de 14 tácticas. Con las definiciones vigentes, ¿corresponde que ese vínculo pase a TA0005 Stealth, a TA0112 Defense Impairment o a las dos? Respondé con lo que dicen las fuentes y señalá qué parte es tu inferencia.
9. Definición oficial vigente de la táctica de ATLAS «AI Attack Adaptation» (antes «AI Attack Staging») y de «AI Model Access». ¿ATLAS ofrece algún criterio de uso que justifique vincular esas tácticas con conceptos de gestión que no tratan de IA (por ejemplo, tolerancia al riesgo, análisis de impacto en el negocio o estrategia de comunicación)?

#### Formato de la respuesta final (máximo 900 palabras)

Una tabla con una fila por punto (1 a 9): **veredicto** (confirmada, contradicha, no se pudo confirmar o, en las preguntas, la respuesta), **qué dice la fuente** (cita de menos de 15 palabras o dato), **URL** y **fecha de la página o de la versión**. Debajo, hasta cinco líneas con las correcciones que el paquete debería hacer. Nada más.

## C7b · Encargo

### Encargo C7b · Verificación externa: hechos que sostienen decisiones de la taxonomía

Fecha de referencia: 15 de noviembre de 2026. Solo fuentes oficiales del organismo emisor (nist.gov, iso.org, isaca.org, isc2.org, etsi.org, eur-lex.europa.eu, cisa.gov, energy.gov, mitre.org, opengroup.org, cybok.org, pcisecuritystandards.org, swift.com). No uses blogs de terceros como prueba. Si no podés confirmar algo, decilo: no completes con memoria.

#### Afirmaciones a confirmar o refutar

1. NIST CSF 2.0 (CSWP 29, 26-feb-2024): 6 funciones, 22 categorías y 106 subcategorías. La función Protect tiene las categorías PR.AA, PR.AT, PR.DS, PR.PS y PR.IR. El acceso físico se trata en PR.AA-06 y las amenazas ambientales en PR.IR-02. La categoría RC.CO se llama «Incident Recovery Communication».
2. ISO/IEC 27002:2022: 93 controles en 4 temas (37 organizacionales, 8 de personas, 14 físicos y 34 tecnológicos).
3. NIST SP 800-53 Rev. 5: 20 familias de controles; última entrega, Release 5.2.0, del 27-ago-2025. Las familias PE (Physical and Environmental Protection), MA (Maintenance) y MP (Media Protection) existen con esos nombres.
4. ISACA CISM: esquema de examen vigente desde el 3-nov-2026, con 4 dominios que pesan 18, 20, 33 y 29 %, y que incorpora arquitectura empresarial y de seguridad.
5. ISC2 CISSP: esquema vigente desde el 15-abr-2024 con 8 dominios; nuevo esquema anunciado para el 15-abr-2027.
6. DOE C2M2 versión 2.1 (junio de 2022): 10 dominios, uno de ellos Cybersecurity Architecture (ARCHITECTURE).
7. NIST IR 8547 (Transition to Post-Quantum Cryptography Standards): estado actual (borrador o final) y fecha; si fija «deprecated after 2030» y «disallowed after 2035» para RSA, ECDSA, EdDSA y Diffie-Hellman.
8. NIST FIPS 203, 204 y 205 se publicaron el 13-ago-2024.
9. NIST SP 800-55 Vol. 1 y Vol. 2 (medición) se publicaron el 4-dic-2024 y reemplazan a SP 800-55 Rev. 1.
10. CyBOK: versión vigente y cantidad de áreas de conocimiento (el paquete dice «1.2, septiembre de 2026, 21 áreas»); si existe un área «Cyber-Physical Systems Security» y qué número lleva (el paquete la cita como KA18).
11. ETSI EN 303 645: versión vigente (el paquete dice V3.1.3, septiembre de 2024).
12. ETSI EN 304 223: versión vigente y fecha (el paquete dice V2.1.1, diciembre de 2025, 13 principios de seguridad para sistemas de IA).
13. Reglamento (UE) 2024/2847 (Cyber Resilience Act): las obligaciones de notificación se aplican desde el 11-sep-2026 y el resto desde el 11-dic-2027.
14. Reglamento de Ejecución (UE) 2024/2690 (NIS2): la sección 13 del anexo trata la seguridad ambiental y física.
15. MITRE EMB3D: versión vigente (el paquete dice 2.0.2).
16. ISO/IEC 27090 (seguridad de sistemas de IA): si está publicada y cuándo (el paquete dice octubre de 2026).
17. ISO/IEC 42001:2023, Anexo A: objetivos A.2 a A.10 con 38 controles.
18. NIST AI RMF 1.0 (AI 100-1): 4 funciones y 19 categorías.
19. COBIT: COBIT 2019 tiene 40 objetivos en 5 dominios; ¿ISACA mantiene el lanzamiento de COBIT 7 para el 19-nov-2026?
20. The Open Group, Open FAIR: versiones vigentes de O-RA y de O-RT (el paquete registra O-RA 2.0.1 y O-RT 3.0.1, y una fuente interna dice O-RA 2.1 y O-RT 3.1).
21. NIST «Control Overlays for Securing AI Systems» (COSAiS): nombre y estado actuales (el paquete registra un posible cambio de nombre a «COSIS» que no pudo confirmar).
22. NIST IR 8596 «Cyber AI Profile»: estado y nombre actuales (el paquete registra que el proyecto del NCCoE figura como «Cyber SI Profile», sin confirmar).
23. CISA BOD 26-04 (10-jun-2026): existe y revoca BOD 19-02 y BOD 22-01.
24. PCI DSS v4.0.1 (junio de 2024): 12 requisitos; el requisito 9 restringe el acceso físico a los datos de titulares de tarjetas.
25. Swift CSCF v2026: 3 objetivos, 7 principios y 32 controles.
26. NICE Framework Components v2.2.0: fecha y conteos (el paquete dice 28-abr-2026, 5 categorías de roles, 42 roles y 11 áreas de competencia).

#### Formato de la respuesta final (máximo 1.000 palabras)

Una tabla con una fila por afirmación (1 a 26): **veredicto** (confirmada, contradicha, no se pudo confirmar), **qué dice la fuente** (dato o cita de menos de 15 palabras), **URL**. Debajo, la lista de correcciones que el paquete debería hacer, ordenadas por importancia. Nada más.

## C8 · Encargo

### Encargo C8 · Lectura de un CISO escéptico

**Tu papel.** Sos un CISO con veinte años de experiencia. No creés nada por defecto. Contrastás cada afirmación con tu conocimiento y tu formación, y sabés que la responsabilidad final de lo que adoptes es tuya y no se delega. Leés para decidir qué aceptar, qué corregir y qué descartar.

**Qué leer.** Completos: `README.md`, `docs/01`, `docs/02`, `docs/11` y `docs/12`. En diagonal: `docs/03`, `docs/06` y `docs/07`.

#### Tarea 1 · Hallazgos

Buscá:

- afirmaciones que no aceptarías sin evidencia, y conclusiones que van más allá de lo que los datos permiten;
- lugares donde el texto suena más seguro de lo que debería;
- conceptos mal usados o contrarios al conocimiento profesional establecido (normas, marcos, práctica);
- recomendaciones que no se pueden llevar a la práctica;
- lo que necesitarías para poder usar el Atlas y no está;
- advertencias que faltan para que un lector no tome una propuesta por un hecho.

`hallazgos.jsonl`, con identificadores `C8-001`, …

#### Tarea 2 · Los 16 pre-ensayos propuestos (`docs/12` y `data/ampliacion_celdas_en_blanco.json`)

Por cada uno, revisá la exactitud técnica, la coherencia entre la tesis y el producto, si la coordenada propuesta corresponde al texto y si afirma algo sin respaldo.

Salida `veredictos_apx.jsonl`:

```
{"id":"APX-01","veredicto":"aceptar|corregir|descartar","problemas":["…"],"correcciones":{"tesis":"texto corregido","producto":"texto corregido"},"motivo":"…"}
```

En `correcciones` poné solo los campos que cambiarías (`titulo`, `tesis`, `tension`, `desarrollo`, `error_frecuente`, `producto`, `pregunta`), con el texto completo corregido. Si cambiarías la coordenada, decilo en `problemas`.

Carpeta de salida: `c8/`. Incluí `cierre.md`.

## C8 · Nota de cierre

### Cierre · Revisor C8

**Qué revisé.** Completos: `README.md`, `docs/01`, `02`, `11` y `12` y el JSON de los 16 pre-ensayos. En diagonal: `docs/03`, `06` y `07`. Contrasté las afirmaciones con los datos del paquete y con NIST CSF 2.0, ISO/IEC 27001 y 27002 y SP 800-53. Dejo 42 hallazgos (5 altos, 31 medios, 4 bajos y 2 observaciones) y 16 veredictos (4 aceptar, 12 corregir y 0 descartar).

**Qué no pude revisar.** Nada fechado en 2026 (IR 8547 final, CCM v4.1, CyBOK 1.2, ATT&CK y ATLAS, encuestas de IDC, WEF y ENISA): el encargo prohíbe la red. Cito de memoria CSF 2.0, ETSI EN 303 645, el CRA y el Reglamento 2024/2690. No leí completos `docs/04`, `05`, `08` a `10` ni los anexos, ni revisé las 739 clasificaciones.

**Cinco hallazgos principales.**

1. C8-001: el corpus no está «cargado hacia la ejecución»; por función, la mitad es gobierno.
2. C8-003: los 883 conceptos de T01 no se comparan con los 9 pre-ensayos; 315 son primarios.
3. C8-004: 65 pre-ensayos del plano académico nombran productos de un proveedor.
4. C8-005: la muestra de control casi no mide la asignación de territorio y dominio, y la confianza declarada (kappa 0,5) ordena la revisión.
5. C8-006: el ejemplo de navegación no se reproduce con el corpus.

**Sin problemas.** Las sumas que recalculé coinciden (nodos, migraciones, relaciones del eje H, cobertura de las 22 categorías de CSF 2.0). `docs/12` y su JSON son idénticos y no citan cifras ni plazos. `docs/07` y `docs/11` declaran sus límites con honestidad. APX-01, 06, 09 y 10 son aceptables como están.

**Juicio general.** El paquete es ordenado y franco sobre su estado, pero su resumen afirma más de lo que sus datos sostienen. Sirve como propuesta; no lo adoptaría como referencia sin una revisión humana medida.

# Verificación de cierre

Cuatro revisores leyeron una copia congelada de la versión 1.2 candidata, y un quinto hizo una lectura final después de la segunda corrección. Sus hallazgos, sus veredictos y el libro de cierre están en `revision_critica/cierre/`.

## V1 · Encargo

### Encargo V1 · Consistencia de la versión 1.2 candidata

El paquete «Frontier CISO Atlas 1.2» es el resultado de corregir la versión 1.1 después de una revisión crítica. Tu tarea es comprobar que **lo que dicen los documentos coincide con lo que dicen los datos**, y que los documentos no se contradicen entre sí. Recalculá: no confíes en los archivos de estadísticas, que son la fuente de las cifras de los documentos.

#### Qué leer (en este orden de prioridad)

1. `README.md`, `docs/13_Revision_critica_1_2.md` y `docs/01_Resumen_Ejecutivo.md`.
2. `docs/06_Grafo_de_Conocimiento.md`, `docs/07_Categorizacion_del_Corpus.md`, `docs/08_Decisiones_de_Arquitectura.md`.
3. `docs/09_Bitacora_de_Tareas.md` (solo las fases 15 a 20 y las secciones 2 a 5), `docs/10_Glosario_y_Continuidad.md`, `docs/12_Ampliacion_Celdas_en_Blanco.md`, `00_Plan_de_Continuacion_1_2.md`, `scripts/LEEME.md` y `config/Instrucciones_Agente_Curador_v7_2.md`.
4. Si te queda tiempo: `docs/02`, `docs/03`, `docs/04` y `docs/05`.

#### Contra qué comparar

- `graph/frontier_ciso_atlas_candidato.sqlite` (tablas `nodes`, `edges`, `changesets`), `graph/nodos.csv`, `graph/aristas.csv`, `graph/resultados_de_aceptacion.json`.
- `data/corpus_frontier_739.json`, `data/categorizacion_739.csv`, `data/revision_critica_hallazgos.csv`, `data/cambios_1_1_a_1_2.csv`, `data/decisiones_del_autor.json`, `data/reglas_propuestas_D11.csv`, `data/biblioteca_cognitiva_1404.csv`, `data/practicas_contra_sesgos.csv`, `data/indicadores_ciso365_en_el_atlas.csv`, `data/indicadores_y_variables_homeostaticas.csv`, `data/base_de_referencia_artefactos.csv`, `data/ampliacion_celdas_en_blanco.json`, `data/analisis_D20_decision_D03.csv`, `data/segunda_lectura_migraciones.csv`, `data/muestra_a_ciegas_1_2.csv`, `data/revision_humana_muestra.csv`, `data/revision_humana_clave.csv`, `data/archivos_por_version.csv`, `changesets/proposed/`.

#### Qué buscar

1. **Cifras que no coinciden** entre un documento y los datos. Cada hallazgo trae la cifra del documento, la cifra recalculada y dónde está cada una.
2. **Contradicciones entre documentos**: la misma cifra o el mismo estado dichos de dos maneras.
3. **Tablas que no suman** su total.
4. **Restos de la versión 1.1 presentados como vigentes** (por ejemplo: «pendiente de aprobación» para decisiones ya aceptadas, indicadores en PR06, 13 preguntas respondibles, territorios de la Biblioteca como clasificación, 792 vínculos de cobertura, 142 prácticas cargadas). No cuentan los textos históricos que indica el formato.
5. **Archivos citados** que no existen o que no contienen lo que el documento dice (columnas, cantidad de filas).
6. **Afirmaciones sobre el propio proceso** que los archivos desmienten (por ejemplo, cuántos revisores, cuántos hallazgos por revisor o por decisión, cuántos cambios por ámbito).

Identificadores `V1-001`, `V1-002`, … Carpeta de salida: `v1/`. Incluí `cierre.md`.

## V1 · Nota de cierre

### Cierre V1

**Qué revisé.** Leí completos el README, los documentos 01, 06, 07, 08, 10 y 13, lo indicado del 09, el plan 1.2, `scripts/LEEME.md` y las instrucciones 7.2; los documentos 02 a 05 y 12, en parte. Recalculé las cifras con guiones desde el SQLite, `data/`, los conjuntos de cambios y `revision_critica/`. Dejo 42 hallazgos: 2 altos, 18 medios, 21 bajos y 1 observación.

**Lo principal.**

- La muestra a ciegas no es un sorteo (40 de confianza alta, las 7 bajas del corpus, ninguna media) y, en territorio y dominio, 44 de 47 casos se comparan con la coordenada 5.3 heredada, no con otra lectura automática (V1-001, V1-035).
- El archivo de los «180 cambios» tiene 4 duplicados y 7 filas agregadas (V1-004, V1-005).
- De las 26 salidas de D20, 13 son coincidencias estrictas; las 7 sugerencias no tuvieron segunda lectura a ciegas (V1-008, V1-020).
- Los 37 pre-ensayos cambiados conservan la justificación, el método y la confianza de la coordenada anterior (V1-041).
- Hay restos de la 1.1 en el documento 08 y una tabla del 07 suma 741 (V1-002, V1-011 a V1-013).

**Sin problemas.** Cierran los 364 hallazgos por severidad, decisión y revisor; el grafo (5.058 nodos, 28.127 relaciones); las distribuciones del corpus; la Biblioteca; la medición; la base de referencia; las preguntas de competencia y el manifiesto.

**No pude revisar.** Faltan en el paquete las fuentes del autor, las versiones 1.0 y 1.1 completas y el guion que eligió la muestra. No ejecuté los guiones, no comprobé hechos externos y no revisé los anexos A1 a A6.

**Juicio.** Las cifras centrales se reproducen. Fallan la descripción de la muestra a ciegas y de las reglas de decisión, y el archivo de cambios. Conviene resolver los dos altos antes de publicar.

## V2 · Encargo

### Encargo V2 · Cierre de los hallazgos críticos y altos

La revisión crítica de la versión 1.1 dejó 48 hallazgos de severidad crítica o alta. El paquete 1.2 candidato dice qué hizo con cada uno. Tu tarea es comprobar, uno por uno, que **lo que dice que hizo se ve en el paquete y responde al hallazgo**.

#### Entrada

`criticos_y_altos.jsonl`, en tu carpeta: 48 líneas con `id`, `severidad`, `artefacto`, `hallazgo`, `propuesta_del_revisor`, `decision`, `accion` y `donde_se_ve`.

#### Qué hacer con cada uno

1. Leé el hallazgo y la acción declarada.
2. Andá al lugar que indica `donde_se_ve` (y a donde haga falta) en el paquete candidato y comprobá con tus ojos, con una consulta o con un cálculo.
3. Decidí:
   - `cerrado`: la acción declarada se ve y responde al hallazgo. Para una decisión «Propuesta al autor», vale `cerrado` si la propuesta está escrita donde dice, con texto suficiente para que el autor decida, y si el paquete no la presenta como aplicada.
   - `cerrado_en_parte`: se ve, pero no cubre todo lo que la acción declara o deja el problema en otro lugar del paquete.
   - `no_cerrado`: la acción declarada no se ve, o el problema sigue igual.
4. Si al comprobar ves que la corrección introdujo un error nuevo, registralo como hallazgo.

#### Salidas

- `veredictos_cierre.jsonl`, una línea por hallazgo: `{"id":"C3-001","veredicto":"cerrado","evidencia":"Archivo y lugar exacto, o la consulta y su resultado.","motivo":"Una oración."}`
- `hallazgos.jsonl`: un hallazgo por cada `cerrado_en_parte` o `no_cerrado`, y por cada error nuevo. Identificadores `V2-001`, … En `ubicacion` poné el identificador del hallazgo original.
- `cierre.md`.

Carpeta de salida: `v2/`. Guardá cada 10 veredictos.

## V2 · Nota de cierre

### Cierre V2: hallazgos críticos y altos

**Qué revisé.** Los 48 hallazgos, uno por uno, contra documentos, guiones y datos del paquete. Consulté el grafo en solo lectura, lo rearmé desde los 16 archivos de operaciones, reejecuté las 22 consultas de aceptación y recalculé las cifras del corpus, la Biblioteca y los indicadores.

**Resultado.** 38 cerrados, 10 cerrados en parte y ninguno sin cerrar. Registré 20 hallazgos: 2 altos, 8 medios, 8 bajos y 2 observaciones. Diez corresponden a los cierres parciales.

**Lo más importante.**

- V2-001 (C3-001): la recarga de agentes pierde 15 vínculos de herramientas y de conocimiento por el orden en que el guion crea los nodos. Cambia cifras publicadas.
- V2-007 (C8-005): la muestra a ciegas no es al azar. Tiene los 7 casos de confianza baja, 40 de alta y ninguno de los 229 de media: sus porcentajes no miden el corpus.
- Residuos de lo corregido: 69 mapeos sin versión (V2-003), el ancla de HumanCapability (V2-005), «el plano A sigue siendo agnóstico» (V2-006) y la excepción de PR.IR (V2-009).

**Sin problemas.** Las fuerzas; las decisiones reformuladas y su orden; SV-112; las definiciones de los nodos; la reconstrucción desde los conjuntos de cambios; las preguntas no expresables; los tipos y los territorios de la Biblioteca; K60, y el resumen por función. Con reparos menores: las reglas propuestas, la aplicación de D-03 y los casos de navegación.

**Qué no pude revisar.** La comprobación de 835 campos contra los anexos del GM-24 y la regeneración en copia limpia: esas fuentes no están en el paquete. No ejecuté los guiones, porque escriben en él.

**Juicio.** Las correcciones son reales y se reproducen. Antes de publicar conviene corregir V2-001 y V2-007 y ajustar las frases que afirman más de lo que el grafo tiene.

## V3 · Encargo

### Encargo V3 · Lectura escéptica de lo nuevo de la versión 1.2

Leé como un CISO con experiencia que además sabe de método: no creas nada por defecto. El autor del Atlas aceptó en bloque diez decisiones, pidió una revisión crítica y fijó cómo debe leerse el Atlas. El paquete 1.2 candidato dice cómo interpretó ese pedido y qué hizo. Tu tarea es juzgar si **lo que el paquete afirma sobre sí mismo es exacto, prudente y útil para quien tiene que decidir**.

#### Qué leer

- `README.md` (sobre todo «Uso previsto y límites» y «En números, con el estado de la evidencia»).
- `docs/13_Revision_critica_1_2.md`, completo.
- `docs/01_Resumen_Ejecutivo.md`.
- `docs/08_Decisiones_de_Arquitectura.md`: la tabla de correspondencia y ADR-026 a ADR-029.
- `docs/10_Glosario_y_Continuidad.md`, secciones 2, 5 y 6.
- `data/decisiones_del_autor.json`, `data/revision_humana_propuesta.json` y `config/Instrucciones_Agente_Curador_v7_2.md`.
- `mensaje_del_autor.md`, en tu carpeta: el mensaje literal del autor.

#### Qué juzgar

1. **Fidelidad a lo que dijo el autor.** Compará las citas y la interpretación con el mensaje literal. ¿Alguna «opción tomada» va más allá de lo que aceptó? ¿Se le atribuye algo que no dijo? ¿Se omitió algo que pidió?
2. **Prudencia.** ¿Hay alguna frase que presente como validado, probado o medido algo que no lo está? ¿Las advertencias están junto a las cifras que califican? ¿Algún número sugiere más precisión de la que tiene?
3. **Exactitud del método.** ¿Está bien descrito qué fue una segunda lectura a ciegas y qué no? ¿Los límites están completos? ¿La distinción entre error aleatorio y error sistemático está bien usada?
4. **La propuesta de revisión humana** (sección 8.4 del documento 13 y el JSON). Recalculá los tamaños de muestra con la fórmula que declara y los dos valores de «sin errores». ¿El criterio de aceptación es coherente con lo que la muestra puede medir? ¿Es practicable para una persona?
5. **Decidibilidad.** Para D-11, D-12 y D-13: ¿el autor tiene lo que necesita para decidir? ¿Qué le falta?
6. **Claridad.** Frases que un CISO no entendería sin haber seguido el trabajo, jerga sin definir, pasajes donde hay que releer.
7. **Tono de las incidencias.** ¿Las incidencias del proceso están contadas con exactitud y sin minimizar ni dramatizar?

No revises la taxonomía ni la clasificación de casos: otros lo hicieron. Identificadores `V3-001`, … Carpeta de salida: `v3/`. Incluí `cierre.md`.

## V3 · Nota de cierre

### Cierre V3

**Qué revisé.** Leí el README, los documentos 13 y 01, la correspondencia y las ADR-026 a ADR-029 del documento 08, las secciones 2, 5 y 6 del documento 10, los dos JSON y las instrucciones 7.2, contra el mensaje literal. Recalculé con Python los tamaños de muestra, los dos valores de «sin errores», la muestra a ciegas y las tablas del documento 13.

**Qué no pude revisar.** No están en el paquete las versiones 1.0 y 1.1, las fuentes del autor ni el registro de sesión que respalda las incidencias. Por encargo no revisé la taxonomía ni la clasificación de casos.

**Hallazgos.** Son 56: 7 altos, 30 medios, 17 bajos y 2 observaciones. Los principales:

1. La aceptación era condicional y se da por cumplida; D-03 y D-10 eran preguntas que contestó el paquete (V3-001 y V3-002).
2. La muestra a ciegas no es un sorteo, omite la confianza media y no compara dos lecturas automáticas (V3-006 y V3-007).
3. El criterio de aceptación de la revisión humana no es coherente con lo que la muestra puede medir (V3-031).
4. El orden de D-11 a D-13 no se puede ejecutar, y D-12 y D-13 son tareas, no decisiones (V3-039 y V3-040).

**Sin problemas.** Son correctos los tamaños 183, 227 y 142 y los valores 29 y 59, y el sorteo se reproduce con la semilla. Coinciden con los datos los porcentajes de la muestra a ciegas, las tablas del documento 13, las cifras del grafo y el manifiesto.

**Juicio.** El paquete declara límites y publica su material, y eso permitió verificarlo. Pero varias frases sobre sí mismo dicen más de lo que se midió, y lo que deja al autor todavía no tiene forma de decisión. Conviene corregir los siete hallazgos altos antes de publicar.

## V4 · Encargo

### Encargo V4 · Cierre de una muestra de hallazgos medios y bajos

La revisión crítica de la versión 1.1 dejó 364 hallazgos. De los que no son críticos ni altos, 164 figuran como «Corregido» o «Corregido en parte». Se sortearon 60. Tu tarea es comprobar, uno por uno, que **lo que el paquete 1.2 candidato dice que hizo se ve y responde al hallazgo**.

#### Entrada

`muestra_medios_y_bajos.jsonl`, en tu carpeta: 60 líneas con `id`, `severidad`, `artefacto`, `hallazgo`, `propuesta_del_revisor`, `decision`, `accion` y `donde_se_ve`.

#### Qué hacer con cada uno

1. Leé el hallazgo y la acción declarada.
2. Andá al lugar que indica `donde_se_ve` (y a donde haga falta) en el paquete candidato y comprobá con tus ojos, con una consulta o con un cálculo.
3. Decidí:
   - `cerrado`: la acción declarada se ve y responde al hallazgo.
   - `cerrado_en_parte`: se ve, pero no cubre todo lo que la acción declara o deja el problema en otro lugar del paquete. Si la decisión ya es «Corregido en parte» y el paquete dice con claridad qué quedó sin hacer, vale `cerrado`.
   - `no_cerrado`: la acción declarada no se ve, o el problema sigue igual.
4. Si al comprobar ves que la corrección introdujo un error nuevo, registralo como hallazgo.

#### Salidas

- `veredictos_cierre.jsonl`, una línea por hallazgo: `{"id":"C1-002","veredicto":"cerrado","evidencia":"Archivo y lugar exacto, o la consulta y su resultado.","motivo":"Una oración."}`
- `hallazgos.jsonl`: un hallazgo por cada `cerrado_en_parte` o `no_cerrado`, y por cada error nuevo. Identificadores `V4-001`, … En `ubicacion` poné el identificador del hallazgo original.
- `cierre.md`.

Carpeta de salida: `v4/`. Guardá cada 10 veredictos.

## V4 · Nota de cierre

### Cierre del revisor V4

**Qué revisé.** Los 60 hallazgos de la muestra contra el paquete 1.2 candidato: documentos, datos, conjuntos de cambios, guiones y grafo, con consultas de sqlite3 y recuentos propios.

**Resultado.** 47 cerrados, 13 cerrados en parte y ninguno sin cerrar. Registré 21 hallazgos: 5 medios, 15 bajos y 1 observación. Doce explican los cierres en parte y nueve son errores nuevos que dejó alguna corrección.

**Lo más importante.**

- V4-011: el desglose del origen del dominio en el documento 07 suma 741 y el corpus tiene 739.
- V4-016: el paquete dice que el CSV de prácticas conserva los 8 vínculos incorrectos; trae 2.
- V4-013 y V4-008: se afirma que ninguna regla propuesta se aplicó, pero la 1.2 aplicó partes de RP-13, RP-14 y RP-16; además, RP-16 no contiene la prueba que el documento 03 dice dejar allí.
- V4-007: la nota nueva de CHG-CAND-10 describe mal lo que ese conjunto tenía en el paquete 1.0.
- Lo demás es menor: un archivo citado que no existe, una nota «a confirmar por el autor» sobre una decisión aceptada y códigos viejos de NIS2.

**Revisado sin problemas.** La decisión D-03 aplicada a D20, el respaldo externo por dominio, el catálogo de 137 códigos, las preguntas de competencia, TRACKED_BY, los nodos aislados y las 29 correcciones de la serie APX.

**Qué no pude revisar.** No contrasté con su fuente lo que el paquete dice de normas externas (NIST IR 8547 y NIST IR 8286r1): no usé la red. No tuve el paquete 1.0: V4-007 se apoya en lo que el candidato dice de él. No ejecuté los guiones.

**Juicio.** Las correcciones declaradas existen y casi todas responden al hallazgo. Los cierres en parte son acotados. Conviene corregir los cinco hallazgos medios antes de publicar.

## V5 · Encargo

### Encargo V5 · Lectura final de consistencia

La versión 1.2 del Frontier CISO Atlas tuvo una revisión crítica, una corrección, una verificación de cierre y una segunda corrección. La segunda corrección reescribió buena parte de los documentos y **ningún revisor la leyó todavía**. Tu trabajo es leerla antes de que se publique.

El paquete está en `cierre/paquete_v1_2_final/` y es de **solo lectura**. No leas otras carpetas de el árbol de trabajo.

#### Qué leer

Completos: `README.md`, `docs/01_Resumen_Ejecutivo.md`, `docs/13_Revision_critica_1_2.md` y `data/decisiones_del_autor.json`.
En parte: `docs/07_Categorizacion_del_Corpus.md` (secciones 3 y 6 a 11), `docs/08_Decisiones_de_Arquitectura.md` (introducción, tablas, ADR-020, ADR-023 a ADR-029), `docs/09_Bitacora_de_Tareas.md` (fases 15 a 21 y secciones 2 y 5), `docs/10_Glosario_y_Continuidad.md` (secciones 5 y 6) y `00_Plan_de_Continuacion_1_2.md`.

#### Qué buscar

1. **Cifras que no coinciden con los datos.** Recalculá con guiones propios, desde `data/` y `graph/frontier_ciso_atlas_candidato.sqlite`, las cifras de los documentos que leíste: muestra a ciegas (`data/muestra_a_ciegas_1_2.csv` y `.json`), cambios (`data/cambios_1_1_a_1_2.csv`), D20 (`data/analisis_D20_decision_D03.csv`), evidencia por pre-ensayo (`data/evidencia_por_preensayo.csv`), revisión humana (`data/revision_humana_*.csv` y `.json`), hallazgos (`data/revision_critica_hallazgos.csv`), verificación de cierre (`revision_critica/cierre/libro_de_cierre.csv`), medición y Biblioteca. Los intervalos de la muestra a ciegas son de Wilson al 95 %, y la estimación ponderada usa los tamaños de estrato 419, 169 y 7 con corrección por población finita: comprobalos.
2. **Contradicciones entre documentos**, o entre un documento y `data/decisiones_del_autor.json`: estados de las decisiones D-01 a D-14, orden propuesto, correspondencia con las ADR, cantidades de proposiciones.
3. **Afirmaciones que dicen más de lo que los datos sostienen**, o que atribuyen al autor algo que su mensaje no dice. El mensaje literal está en `data/decisiones_del_autor.json`, clave `mensaje_del_autor`.
4. **Texto roto**: frases cortadas, marcadores sin reemplazar, tablas con columnas corridas, referencias a secciones o archivos que no existen, concordancias que el generador dejó mal.

No propongas reescrituras de estilo ni cambios de diseño. No repitas lo que el paquete ya declara como límite.

#### Cómo entregar

- `hallazgos.jsonl` en tu carpeta, una línea por hallazgo, con el formato de `cierre/comun/FORMATO.md` e identificadores `V5-001`, `V5-002`, …
- Como máximo 30 hallazgos: los más graves primero. Para cada uno, cita literal del texto, el archivo y la sección, el valor recalculado y la corrección concreta.
- `cierre.md`, de una página: qué leíste, qué recalculaste y coincide, qué no pudiste revisar y tu juicio.
- Escribí solo en `cierre/v5/`, con Python o con el intérprete de comandos, y guardá de forma incremental.
- Al terminar ejecutá `python3 cierre/comun/validar.py cierre/v5` hasta que diga VÁLIDO.

## V5 · Nota de cierre

### Cierre V5 · Lectura final de consistencia

**Qué leí.** Completos: README, docs/01, docs/13 y data/decisiones_del_autor.json. En parte: docs/07 (secciones 3 y 6 a 11), docs/08 (introducción, tablas, ADR-020 y ADR-023 a ADR-029), docs/09 (fases 15 a 21, secciones 2 y 5), docs/10 (secciones 5 y 6, y la 2 al contrastar el orden) y el plan 1.2.

**Qué recalculé y coincide.** Muestra a ciegas: conteos por estrato, intervalos de Wilson, marco de 595 (419, 169 y 7) y estimación ponderada con corrección por población finita. Las 182 filas de cambios; los 37 cambios del corpus contra la categorización 1.1; D20; migraciones; evidencia por pre-ensayo (237 y 502); los 364 hallazgos; el libro de cierre (139; 85 y 23); la revisión humana; medición, Biblioteca, grafo, base de referencia, taxonomía y manifiesto. Las tablas de decisiones y de orden son iguales al JSON. El texto congelado de ADR-013 a ADR-025 es igual al de la versión 1.1.

**Hallazgos.** 16: 2 altos y 14 medios. Los altos son una cifra vieja de las preguntas de competencia (docs/13, 5.2) y un orden de decisiones distinto en docs/10, sección 2. Varios medios son restos de hallazgos de cierre dados por corregidos. Corregí V5-009 después de guardarlo: un ejemplo era inexacto.

**Qué no revisé.** No ejecuté los guiones ni comprobé hechos externos. No verifiqué las cifras del registro de la sesión, las «cinco fichas precisadas» ni las de la regresión. No leí los documentos 02 a 06, 11 y 12. Por el pedido de cierre no guardé cuatro hallazgos bajos: un «Sí.» suelto en docs/13 (8.5), la remisión a «sección 8.3» en 6.3 (es 8.4), «fases 15 a 20» en docs/09 y la enumeración sin concordancia de 6.5.

**Juicio.** Las cifras centrales cierran con los datos. Falta limpiar restos de la versión candidata.

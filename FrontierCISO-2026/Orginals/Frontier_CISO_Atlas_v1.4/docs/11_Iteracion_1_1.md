> **Registro de la versión 1.3 (16 de noviembre de 2026).** Este documento se conserva tal como se publicó. Las cifras, los estados y los archivos que cita corresponden a esa versión. El estado vigente está en `docs/15_Decisiones_delegadas_y_relectura_1_4.md` y en los documentos 16 a 19.

# Iteración 1.1 · Estado y continuación (registro histórico)

**Frontier CISO Atlas 1.3** · Taxonomía 6.0 (reglas de asignación, revisión 2) · Ontología 2.1.0 · GM-24 V7.1 · 16 de noviembre de 2026 · Estado: decisiones de diseño confirmadas por el autor; reglas adoptadas según la lectura del curador y corpus releído a ciegas por lectores automáticos, con una lectura para todos y dos donde la primera difería; contenido candidato, sin validación humana

> **Este documento no se actualiza.** Es el informe de la versión 1.1 tal como se publicó, y sus cifras son las de aquel momento. Se conserva para que pueda verse qué se afirmó entonces. El estado vigente está en `01_Resumen_Ejecutivo.md` y en `13_Revision_critica_1_2.md`.

## Fe de erratas

La revisión crítica de la versión 1.2 encontró 16 problemas en lo que este documento afirma. La tabla dice cuáles y qué se hizo con cada uno. El texto de abajo no se corrigió.

| Hallazgo | Severidad | Qué se encontró | Qué se hizo en la versión 1.2 |
|---|---|---|---|
| C1-031 | Alta | El resultado «0 errores y 0 advertencias» se presenta como validación contra la ontología 2.1.0, pero el validador evalúa 13 de las 37 reglas. Una de las reglas de nivel error que no evalúa, SV-003, exige descripción en todo nodo, y 1.809 de los 5.041 nodos no la tienen. | Corregido. El validador comprueba ahora 19 de las 37 reglas, entre ellas SV-003 y SV-112, más una comprobación propia del paquete (PAQ-01), y la lista de comprobadas y no comprobadas se publica. El README y los documentos dicen que la validación es estructural. |
| C5a-002 | Alta | Los 172 conceptos que la regla dejó como Concept no son un residuo homogéneo: leyendo nombre y definición, 71 corresponden a un tipo específico. Las cifras publicadas por tipo cambian en los cinco tipos. | Corregido. Se aplicaron los veredictos de tipo de confianza alta o media (66 conceptos) y las ocho excepciones de la muestra; los cinco de confianza baja quedan como estaban. |
| C1-006 | Media | Los documentos dicen que el catálogo 1.2 tenía 64 indicadores y que los otros 160 son nuevos del catálogo 2.0. Los datos del paquete rotulan 70 indicadores con origen «Catálogo v1.2» y 154 como «Nuevo en v2.0». Las dos particiones suman 224 pero no coinciden. | Corregido. Verificado en la fuente: el catálogo 1.2 traía 64 indicadores K y seis del sistema de gestión (KSG01 a KSG06), 70 en total. Los 70 heredan ahora su coordenada y los documentos lo dicen. |
| C1-009 | Media | La columna «De la caja de 72» no cuenta los conceptos de la caja de 72 vinculados a cada unidad: cuenta los vínculos cuyo método es editorial_curation_72. Cada una de las 24 unidades tiene además un concepto de la caja de 72 vinculado por otro método (source_crosswalk), de modo que la columna queda uno por debajo en todas las filas. | Corregido. La columna se informa como «por selección editorial» y la cobertura cargada se limita a esos vínculos y a los de ancla expresa. |
| C1-010 | Media | La cifra de 883 conceptos de la Biblioteca que «llevan el territorio T01» se presenta junto a los 9 pre-ensayos de T01 como si midieran lo mismo, pero usan criterios distintos: los pre-ensayos se cuentan por territorio primario y los conceptos por cualquier mención. Con territorio primario T01 hay 315 conceptos; los otros 568 lo llevan como secundario. | Corregido. Se retira la comparación de 9 con 883. Los territorios de la Biblioteca son un valor por categoría de la base y ya no se afirman como clasificación; el documento da las cifras con su papel (315 con T01 como único territorio y 568 con T01 entre varios). |
| C1-011 | Media | El resumen de la lectura de D20 no cierra: se anuncian 71 pre-ensayos y se desglosan 14, 11 y 45, que suman 70. Falta el pre-ensayo clasificado como «Otro dominio (fuera de D-03)». | Corregido. El texto se reescribió con la decisión D-03 aplicada: de los 71 pre-ensayos, 26 se movieron y 45 quedan en D20, y el desglose suma 71. |
| C1-016 | Media | El archivo de la propuesta de remapeo declara que no se aplicó «ni al mapeo del grafo», pero el grafo candidato contiene las dos aristas MAPS_TO que la propuesta agrega. El total de MAPS_TO publicado ya las incluye. | Corregido. El estado de la propuesta dice que los vínculos que agrega están en el grafo candidato, aparte y rotulados como propuesta (CHG-CAND-15). |
| C1-024 | Media | El criterio declarado para marcar nodos «revisar» antes de una edición pública no se aplicó de forma pareja a lo que sumó la versión 1.1. Los 224 indicadores del catálogo CISO 365 están marcados «revisar», pero los 24 objetivos, los 72 resultados clave y los 3 órganos de gobierno del mismo catálogo quedaron como «publica». | Corregido. La marca «revisar» se aplica por procedencia: todos los nodos del catálogo CISO 365 (indicadores, objetivos, resultados clave y órganos) la llevan, igual que los del plano B, los de la Biblioteca y los pre-ensayos que nombran productos. |
| C5a-005 | Media | La limitación declarada dice que tres categorías mezclan cosas distintas, pero las otras ocho también mezclan. En la muestra de 120 hay 8 conceptos cuyo tipo por regla no corresponde, concentrados en mindset y en práctica de decisión. | Corregido en parte. La limitación declarada dice que todas las categorías mezclan tipos. La revisión completa de las categorías mindset y práctica de decisión queda en la decisión D-12. |
| C5b-004 | Media | No es exacto que los 135 vínculos tomados de las fichas salgan de 35 textos repetidos por familias. Solo 7 de los 35 textos están en más de una ficha; los otros 28 se escribieron para un solo sesgo. Al dar a todos confianza «baja», el paquete trata igual dos grupos que se comportan de manera opuesta. | Corregido. El CSV dice si el texto es propio de la ficha o una fórmula repetida, y el documento ya no afirma que los 135 vínculos salen de 35 textos repetidos. |
| C8-008 | Media | Informar «6 de 6» variables homeostáticas con indicadores sugiere que ya se pueden medir, pero ninguna tiene unidad, umbral ni responsable del límite, y los indicadores no miden los dos términos de cada relación. El «fundamento» de la mayoría de los vínculos repite el nombre del indicador. | Corregido. Los documentos dicen «variables con indicadores candidatos»: ninguna tiene unidad, umbral ni responsable del límite. Cada vínculo dice si lo sostienen dos lecturas o una. |
| C8-017 | Media | La relación `COUNTERS` afirma que una práctica contrarresta un sesgo, pero ninguno de los 142 vínculos tiene evidencia de eficacia y el 95 % tiene confianza baja. La tabla que atribuye 44 sesgos al «abogado del diablo» se lee como una recomendación. | Corregido en parte. El conjunto de cambios presenta los vínculos como lo que la Biblioteca propone, sin afirmar eficacia. Redactar la definición de la relación como posibilidad queda pedido en OCR-CAND-03. |
| C8-018 | Media | La cobertura pedagógica propuesta no se puede llevar a la práctica: tres unidades concentran la mitad de los vínculos y una sola recibe 158 conceptos. El rótulo «confianza media o alta editorial» oculta que el 97 % es media y el 78 % sale de una coincidencia temática. | Corregido. Se cargan como cobertura solo los 165 vínculos de selección editorial o de ancla expresa; los 627 de coincidencia temática quedan en el CSV de la base, fuera del grafo. |
| C1-028 | Baja | El paquete dice que el proyecto entregó el Modelo Operativo CISO 365 2.0 «y su edición 2.1» y que el catálogo vigente tiene 224 indicadores, pero todo lo cargado proviene del catálogo 2.0. No se dice si la edición 2.1 cambia el catálogo ni por qué se usó la 2.0. | Documentado. La ficha del catálogo dice que el paquete carga la versión 2.0 y que no comprobó si la edición 2.1 del modelo operativo la modifica. |
| C6b-012 | Baja | Los documentos dicen que el catálogo 1.2 tenía 64 indicadores y los datos atribuyen 70 al «Catálogo v1.2». Los seis de diferencia son KSG01 a KSG06, que figuran con ese origen y aun así no tienen territorio ni dominio. | Corregido. Verificado en la fuente: el catálogo 1.2 traía 64 indicadores K y seis del sistema de gestión (KSG01 a KSG06), 70 en total. Los 70 heredan ahora su coordenada y los documentos lo dicen. |
| C5c-007 | Observación | Las dos familias se solapan poco: la duplicación se concentra en una veintena de conceptos y el resto de la Biblioteca no tiene contraparte en el corpus. Ningún pre-ensayo está dedicado a un sesgo concreto; solo AMP-02 nombra sesgos cognitivos (tres), y el corpus no menciona los modelos con nombre propio de la Biblioteca. | Documentado. Límite declarado: la similitud de nombre no alcanza para la revisión de duplicados; la relación entre la Biblioteca y el corpus es de vinculación más que de deduplicación. |

## Texto publicado en la versión 1.1

**Frontier CISO Atlas 1.1** · Taxonomía 6.0 · Ontología 2.1.0 · GM-24 V7.1 · 15 de noviembre de 2026 · Estado: propuesta pendiente de aprobación

Este documento responde a tu pedido de informar el estado y continuar. Dice cómo estaba el trabajo al retomarlo, qué se continuó, qué quedó igual y qué decisiones siguen abiertas.

### 1. Estado al retomar

| Tema | Estado |
|---|---|
| Versión 1.0 | Publicada e íntegra: 115 archivos, con el manifiesto verificado archivo por archivo. No se modificó |
| Decisiones D-01 a D-07 | Abiertas. No hay ninguna registrada |
| Proyecto | Después de la 1.0 se entregaron el Modelo Operativo CISO 365 2.0 y su edición 2.1. El catálogo vigente tiene 224 indicadores; la 1.0 usaba el anterior, de 64 |
| Fuentes | Apareció tu base de integración de la Biblioteca (`Base_1404_Atlas_GM24.json`, en la carpeta `Integracion_Atlas_1404_GM24` de tu OneDrive), con corte al 12-nov-2026. La 1.0 no la había localizado e informó la Biblioteca como «no incorporada», con una cifra anterior (1.356 conceptos) |

### 2. Qué se continuó y qué no

La versión 1.0 dejó nueve pendientes ordenados. Los tres primeros dependen de vos. De los demás, se trabajaron los cuatro que no necesitan una decisión tuya ni modifican un artefacto vigente. Todo quedó como propuesta.

| N.º | Pendiente de la versión 1.0 | Qué pasó en la 1.1 |
|---|---|---|
| 1 | Decisiones D-01 a D-07 | Siguen abiertas. Se agregan D-08, D-09 y D-10 |
| 2 | Revisión del curador sobre la categorización | Sigue pendiente. La lectura completa de D20 le ahorra esa pasada |
| 3 | Primera tanda de ensayos | Sigue pendiente. La propuesta de 40 no cambió |
| 4 | Carga del contenido del MCCS y de la Biblioteca | **Hecho en parte.** La Biblioteca cognitiva está en el grafo candidato. Faltan las notas del MCCS y el Documento Maestro del CISO-OS |
| 5 | Indicadores para PR06 y RC05, e indicadores por variable homeostática | **Hecho como propuesta**, con el catálogo 2.0 |
| 6 | Mapeo del GM-24 a las matrices vigentes | **Propuesta lista**, no aplicada |
| 7 | Contenido para los dominios en blanco | **16 pre-ensayos propuestos**, fuera del corpus |
| 8 | Revisión de D21, D22 y D23 | Sin cambios. Queda para la taxonomía 6.1 |
| 9 | Edición pública | Sin cambios. Ahora alcanza también a la Biblioteca y a los indicadores |

### 3. Lo que no cambió

- **Taxonomía 6.0.** Los mismos archivos: 8 territorios, 28 dominios, 6 funciones y 34 subfunciones.
- **Base de referencia.** Los mismos archivos. Las revalidaciones posteriores a Ignite 2026 y a COBIT 7 siguen en el calendario: todavía no ocurrieron.
- **Categorización.** Los 739 pre-ensayos tienen la misma coordenada. La lectura de D20 es un análisis y no movió nada.
- **Conjuntos de cambios 01 a 09.** Sus archivos de operaciones tienen la misma huella que en la versión 1.0.
- **Artefactos vigentes del proyecto.** No se modificó el GM-24, el banco de pre-ensayos, tu base de la Biblioteca ni el catálogo de indicadores.

### 4. Antes y después

| Elemento | Versión 1.0 | Versión 1.1 |
|---|---|---|
| Ontología | 2.0.0: 84 tipos de entidad, 92 relaciones, 36 reglas | 2.1.0: 84 tipos de entidad, 93 relaciones, 37 reglas |
| Grafo candidato | 3.378 nodos y 24.108 relaciones en 10 conjuntos de cambios | 5.041 nodos y 29.887 relaciones en 15 conjuntos de cambios |
| Errores de validación | 0 | 0 |
| Tipos de entidad con instancias | 25 | 32 |
| Relaciones en uso | 26 | 31 |
| Preguntas de competencia | De 20: 11 respondibles, 2 en parte, 7 todavía no | De 22: 13 respondibles, 4 en parte, 5 todavía no |
| Territorio T01 en el grafo | 9 pre-ensayos | 9 pre-ensayos y 883 conceptos de la Biblioteca |
| Indicadores en el grafo | 84: 20 del sub-plan PO-GAC y 64 del catálogo 1.2 | 244: 20 del sub-plan PO-GAC y 224 del catálogo 2.0 |
| Variables homeostáticas con indicadores | 0 de 6 | 6 de 6, como propuesta |
| Subfunciones con indicador | 32 de 34 | 34 de 34 |
| Nodos marcados «revisar» para la edición pública | 800 | 2.364 |
| Pre-ensayos en el corpus | 739 | 739, más 16 propuestos fuera del corpus |

### 5. La Biblioteca cognitiva en el grafo

Tu base propone 1.404 conceptos como nodos candidatos y pide una relación nueva entre unidades de aprendizaje y conceptos. Esta versión hace las dos cosas dentro del grafo candidato, sin aplicar nada.

- **Tipos.** 475 `CognitiveBias`, 388 `HumanCapability`, 199 `MentalModel`, 172 `Concept`, 170 `MetacognitivePractice`. La regla va por categoría y está en `06_Grafo_de_Conocimiento.md`.
- **Territorios.** 883 conceptos llevan T01, 598 T04 y 346 T03. Se cargaron como están en la base.
- **Cobertura por unidad.** 792 vínculos de confianza media o alta editorial. Las unidades con más conceptos propuestos:

| Unidad del GM-24 | Conceptos propuestos | De la caja de 72 |
|---|---|---|
| M1.2 Gestión Financiera, Liderazgo de Equipo y Capacitación | 158 | 8 |
| G5.1 Supervisión de la Evaluación y Análisis | 133 | 30 |
| G6.2 Liderazgo Ético y Medición de Efectividad | 105 | 14 |
| M3.1 Arquitectura de Seguridad, Ingeniería y Diseño (Incl. Zero Trust) | 47 | 8 |
| G6.1 Comunicación Estratégica | 38 | 5 |
| G1.2 Desarrollo de Estrategia y Alineación con el Negocio | 34 | 7 |

- **Prácticas que contrarrestan sesgos.** 142 vínculos. Las prácticas con más sesgos asociados:

| Práctica | Sesgos |
|---|---|
| Abogado del diablo | 44 |
| Premortem | 22 |
| Valor esperado | 22 |
| Listas de verificación | 14 |
| Calibración | 11 |
| Revisión por pares | 8 |

Lo que ahora se puede preguntar al grafo: qué sesgos, modelos mentales y prácticas propone cubrir una unidad del GM-24; qué prácticas nombra la Biblioteca contra un sesgo; qué conceptos de la caja de 72 tocan un territorio.

### 6. La medición en el grafo

Cada variable homeostática tiene ahora indicadores propuestos. Los principales:

| Variable | Indicadores principales propuestos |
|---|---|
| HV01 Exposición residual frente al apetito de riesgo | K24 Pérdidas por incidentes frente a la tolerancia anual; K25 Riesgos residuales fuera del apetito; K26 Pérdida esperada de los escenarios prioritarios frente al apetito; K87 Umbrales de apetito superados con decisión en plazo; K93 Aceptaciones de riesgo vencidas sin renovar |
| HV02 Autoridad delegada frente a capacidad de supervisión | K50 Agentes con dueño humano y autoridad delegada acotada; K88 Tipos de acción de agentes con nivel de autonomía aprobado; K98 Decisiones automatizadas de alto impacto con supervisión humana verificada; KX13 Decisiones reservadas ejecutadas sin aprobación; KX15 Funciones externalizadas con capacidad interna de supervisión; K167 Agentes con detención de emergencia probada |
| HV03 Ritmo de cambio frente a capacidad de absorción | K20 Tiempo de habilitación segura de iniciativas; K70 Deuda de seguridad con dueño, costo y fecha; K90 Evaluaciones de riesgo actualizadas ante cambios materiales; K116 Iniciativas con revisión de arquitectura antes de producción; K128 Riesgos emergentes evaluados en plazo |
| HV04 Confianza de las partes interesadas sostenida por evidencia | K57 Obligaciones aplicables mapeadas a controles con evidencia vigente; K58 Calidad del reporte de ciberriesgo al Directorio; K60 Controles clave con efectividad probada; K82 Cobertura del plan de aseguramiento; K96 Utilidad del reporte de ciberriesgo para sus destinatarios; KSG05 Nivel de evidencia de las prácticas de gobierno y gestión |
| HV05 Carga cognitiva frente a capacidad de decisión | K125 Carga por analista; K101 Trabajo no planificado del equipo; K95 Decisiones solicitadas a la dirección resueltas en plazo; K05 Tiempo hasta la decisión ejecutiva en crisis; K170 Falsos positivos de las detecciones prioritarias |
| HV06 Continuidad de los servicios críticos | K29 Operación degradada probada en procesos críticos; K30 Pruebas de recuperación que cumplen RTO y RPO; K47 Tiempo de restauración de servicios críticos frente al RTO; K185 Servicios críticos con objetivos de recuperación aprobados por el negocio; K28 Respaldos inmutables de sistemas críticos con restauración probada |

Los indicadores de apoyo y el fundamento de cada vínculo están en `data/indicadores_y_variables_homeostaticas.csv`. Es una propuesta de diseño: las variables no tienen respaldo normativo externo y los vínculos tampoco.

Además: PR06 tiene K36, K159, K160 y K193 y RC05 tiene K189; las 34 subfunciones tienen al menos un indicador; y 212 indicadores declaran a qué órgano de gobierno informan.

### 7. La ontología pasó a 2.1.0

Tres límites de la 2.0.0 aparecieron al cargar contenido real, y la propuesta se revisó: una relación nueva (`COVERS_CONCEPT`), dos ampliadas (`CLASSIFIED_IN` y `MEASURES`), una regla (SV-118), una definición precisada y dos preguntas de competencia. La 2.1.0 contiene a la 2.0.0. El detalle está en `05_Ontologia_2_1.md`.

### 8. Tres propuestas editoriales

Ninguna se aplicó.

1. **Remapeo del GM-24 a las matrices vigentes.** Alcanza a 78 vínculos existentes y agrega 2; 18 necesitan revisión del curador. Detalle en `04_Base_de_Referencia.md`.
2. **Lectura de D20 para la decisión D-03.** De 71 pre-ensayos, 14 se moverían con claridad, 11 quedan a criterio del curador y 45 se quedan. Detalle en `07_Categorizacion_del_Corpus.md`, sección 11.
3. **Pre-ensayos para celdas en blanco.** 16: 7 para D19, 5 para D27, 4 para RC05. Texto completo en `12_Ampliacion_Celdas_en_Blanco.md`.

### 9. Decisiones

Las siete de la versión 1.0 siguen abiertas y están en `01_Resumen_Ejecutivo.md`. Dos cambian de contenido: D-03 tiene ahora la lectura completa de D20 y D-05 se refiere a la ontología 2.1.0. Las nuevas:

| N.º | Decisión | Qué necesito de vos |
|---|---|---|
| D-08 | Biblioteca cognitiva en el grafo candidato | Aceptar o corregir la regla de tipos por categoría, el criterio de territorio primario y la exclusión de los vínculos débiles |
| D-09 | Indicadores por variable homeostática | Validar o corregir los 71 vínculos, y confirmar K36 en PR06 |
| D-10 | Propuestas editoriales | Decidir si el remapeo entra en la próxima versión del GM-24 y si los 16 pre-ensayos se incorporan al corpus |

### 10. Límites de esta iteración

- **Los tipos de la Biblioteca salen de una regla por categoría.** Tres categorías mezclan cosas distintas; 172 conceptos quedaron como `Concept` hasta que el curador decida.
- **Los territorios son los de tu base**, sin revisión. Su confianza figura como «no declarada».
- **135 de los 142 vínculos entre prácticas y sesgos** vienen de textos que la base repite por familias de sesgos. Sirven para explorar, no para afirmar.
- **Los indicadores por variable homeostática los propuse yo**, leyendo el nombre y la fórmula de cada indicador.
- **71 indicadores solo tienen función** y 160 no tienen territorio ni dominio.
- **La división de técnicas de MITRE ATT&CK** entre Stealth y Defense Impairment no se verificó.
- **La lectura de D20 y los pre-ensayos propuestos** son trabajo asistido. Los pre-ensayos usan el formato de tus ampliaciones, pero no tu voz: conviene que los revises antes de aceptarlos.
- **No se buscaron duplicados** entre los conceptos de la Biblioteca y los del GM-24.
- **Nada tiene revisión humana.**

### 11. Archivos nuevos o actualizados

- Nuevos en `docs/`: `11_Iteracion_1_1.md` y `12_Ampliacion_Celdas_en_Blanco.md`. `05_Ontologia_2_1.md` reemplaza a `05_Ontologia_2_0.md`. Los demás documentos se actualizaron.
- Nuevos en `data/`: `biblioteca_cognitiva_1404.csv`, `biblioteca_cognitiva_estadisticas.json`, `practicas_contra_sesgos.csv`, `indicadores_ciso365_en_el_atlas.csv`, `indicadores_y_variables_homeostaticas.csv`, `medicion_estadisticas.json`, `propuesta_remapeo_gm24.csv`, `propuesta_remapeo_gm24.json`, `analisis_D20_decision_D03.csv`, `analisis_D20_decision_D03.json`, `ampliacion_celdas_en_blanco.csv` y `ampliacion_celdas_en_blanco.json`.
- Actualizados en `data/`: los cuatro archivos de la ontología.
- En `graph/` y `changesets/proposed/`: el grafo reconstruido y los conjuntos 10 a 15.
- En `config/`: las instrucciones 7.1 del agente curador.
- En la raíz: `00_Plan_de_Continuacion_1_1.md`.

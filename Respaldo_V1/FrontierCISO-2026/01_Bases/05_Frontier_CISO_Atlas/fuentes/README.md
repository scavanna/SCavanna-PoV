# Frontier CISO Atlas 1.4

**Frontier CISO Atlas 1.4** · Taxonomía 6.1 (reglas de asignación, revisión 3) · Ontología 2.2.0 (propuesta) · GM-24 V7.1 · 16 de noviembre de 2026 · Estado: respuestas del autor registradas de forma literal; lo que decidió el curador en esta versión espera su confirmación (D-16); corpus releído por lectores automáticos con una vara de tres lecturas, que el curador endureció después de leer; contenido candidato, sin validación humana

Evolución del AI CISO Atlas. Este paquete contiene la taxonomía, la base de referencia, la ontología, el corpus categorizado, el grafo de conocimiento candidato y la documentación de lo que se hizo.

La versión 1.4 registra las respuestas que el autor dio el 16 de noviembre de 2026 a los seis pasos que cerraban la versión 1.3. Tres respuestas son literales: confirmó las lecturas del curador (D-15), los 37 cambios de la versión 1.2 y los encargos en cola con la solicitud de cambio de la ontología. Las otras tres llevan la misma frase: «Procede con la decision de mayor rigurosidad». El autor no definió esa rigurosidad. El curador la leyó como una delegación, decidió con un criterio que escribió él, volvió a leer todo el corpus y dejó cada decisión a la vista, con su origen y con la forma de revertirla. Todo eso espera la confirmación del autor (D-16).

**Lo primero que hay que saber.** El curador endureció la vara de la relectura después de ver los resultados, y se había comprometido a no cambiarla. Con la vara aplicada cambian 99 coordenadas; con la que había fijado antes de leer habrían cambiado 480. La condición que reemplazó es una que el autor había confirmado ese mismo día (ADR-030, D-15.4). La vara aplicada es la más conservadora de las dos, y no está demostrado que sea la mejor: con ella, en 594 coordenadas del corpus las dos lecturas coinciden en un valor distinto del que se publica. Cuál vale lo elige el autor (D-16.2). Esa elección no tiene un «sí» por defecto y puede esperar a la revisión humana.

**Siglas y términos que este README usa.** *GM-24*: el currículo TheNextCISO, de 24 unidades. *Eje H*: el eje de evolución y homeostasis, que dice cómo se mueve una práctica y qué la acelera, la frena o la mantiene bajo control. *MCCS*: el sistema metacognitivo del CISO; según el autor, los 1.404 elementos de su biblioteca metacognitiva. *Pre-ensayo*: la idea central de un concepto, todavía sin desarrollar como ensayo. *Coordenada*: el territorio, el dominio y la subfunción donde el Atlas ubica un elemento. *Serie APX*: dieciséis pre-ensayos redactados para celdas sin contenido. *Conjunto de cambios*: un paquete de nodos y relaciones que se propone cargar al grafo. *Decisión delegada*: la que tomó el curador después de que el autor respondió con una frase general; que esa frase sea una delegación es una lectura del curador, que el autor todavía no confirmó (D-16.14). El glosario de esta versión está en `docs/19_Arquitectura_Bitacora_y_Glosario_1_4.md`.

## Uso previsto y límites

**Para qué sirve.** El Atlas es una guía. Ayuda a un CISO a ubicar un problema (territorio, dominio y función), a leer cómo se mueve el terreno (eje H), a elegir qué estudiar (GM-24) y a ordenar su conocimiento en un grafo. Sirve para orientar, comparar y preguntar mejor.

**Cómo leerlo.** El autor lo escribió así: estos niveles de abstracción funcionan como guías y orientación; un CISO tiene que leer todo con atención, no creer nada por defecto y, contrastando con su conocimiento y su formación, ir aceptando los distintos elementos, con la responsabilidad final indelegable. Cada elemento se acepta por decisión de quien lo usa.

**Para qué no sirve.**

- No es una norma ni un marco de conformidad. Un cruce con un marco indica afinidad temática; no afirma cumplimiento.
- No describe el estado de ninguna organización. Los indicadores tienen fórmula y unidad, pero no meta ni responsable en una organización; las variables homeostáticas son un modelo de referencia.
- No reemplaza el juicio profesional ni la evaluación de riesgo de un caso concreto.
- No prueba que una práctica funcione. Los vínculos entre prácticas y sesgos dicen lo que la biblioteca propone.
- No es neutral respecto de un proveedor. El plano A se propone agnóstico, pero 77 de sus pre-ensayos nombran productos de un proveedor o al proveedor, y ese proveedor es el organismo con más artefactos en la base de referencia.

**Qué estado tiene.** El autor confirmó el diseño (D-01 a D-10, D-14 y D-15). Lo que cambió en esta versión lo decidió el curador: una parte, leyendo tres respuestas del autor como una delegación; otra, al ejecutar los encargos que el autor aprobó; y otra, por su cuenta. Todo espera su confirmación (D-16), y ningún cambio de catálogo tiene todavía aprobación humana. El contenido es candidato: ningún elemento tiene validación humana. Las lecturas y las revisiones las hicieron agentes automáticos con la misma configuración que quien generó los artefactos. Que dos lecturas coincidan dice que el encargo determina la respuesta; no dice que la respuesta sea correcta, ni descarta un error que las lecturas compartan. No hay una tasa de error medida. Los conjuntos de cambios del grafo siguen en estado «propuesto».

**Qué falta para usarlo en una organización.** Una guía de instanciación y un caso resuelto de punta a punta. `docs/18_Grafo_Categorizacion_y_Revision_Humana_1_4.md` trae seis casos de navegación resueltos con el corpus y dice qué hace falta para pasar a un grafo aprobado con ensayos.

## En números, con el estado de la evidencia

| Elemento | Valor | Estado de la evidencia |
|---|---|---|
| Taxonomía 6.1, reglas de asignación revisión 3 | 8 territorios, 28 dominios, 6 funciones y 35 subfunciones | La 6.0 está confirmada por el autor. Los cuatro cambios de catálogo de la 6.1, las 24 reglas decididas y los 15 vacíos declarados son decisiones delegadas, a confirmar. Las reglas se corrigieron después de una revisión previa, y esa corrección no tuvo una segunda revisión |
| Eje H, revisión 2 | 3 horizontes y un marcador de convergencia, 11 catalizadores, 11 inhibidores, 12 mecanismos, 8 factores de contexto y 6 variables | Propuesta de diseño, sin respaldo normativo externo. Decisión delegada. 5 de las 6 variables tienen algún papel de regulación sin mecanismo |
| Ontología 2.2.0 | 10 módulos, 86 tipos de entidad, 98 relaciones y 42 reglas | Propuesta. Aplica la solicitud de cambio que el autor aprobó. Cinco elecciones que la solicitud dejaba abiertas, dos agregados y cuatro decisiones de implementación son del curador (D-16.10) |
| Base de referencia | 146 artefactos de 42 organismos | Los artefactos y su verificación no cambiaron en esta versión: son los del 15 de noviembre de 2026. Solo se recalculó un silencio (SIL-08), que depende de la categorización. El estado de verificación está en el documento 04 |
| Corpus | 739 pre-ensayos categorizados | Clasificación automática, releída completa dos veces a ciegas en esta versión, con una tercera lectura donde las dos coincidían en otro valor. Cambiaron 96 coordenadas primarias en 87 pre-ensayos respecto de la versión 1.2: 86 por la vara, que exige confianza alta en las dos lecturas, y 10 por el nuevo alcance de RC04, que sigue otra regla y admite cualquier confianza. Con la vara fijada antes de leer, que admitía la confianza media, habrían cambiado 471 en 330; no se aplicó y queda calculada aparte. En 737 ejes, contando la serie APX, alguna lectura apunta a otro valor y el cambio no entró. Sin revisión humana |
| Biblioteca metacognitiva (MCCS) | 1.404 elementos en el grafo candidato | No se revisó, por pedido del autor. Tipos por regla, salvo 81 que vienen de la revisión crítica de la versión 1.2. Los territorios no se afirman. Las 112 equivalencias con el corpus tienen una sola lectura |
| Medición | 224 indicadores | Las dos reglas para indicadores que el autor adoptó no se aplicaron todavía. 8 indicadores quedaron sin subfunción en esta versión |
| Grafo candidato | 5.059 nodos y 28.553 relaciones en 17 conjuntos de cambios | Validación estructural: 25 de 42 reglas comprobadas, 0 errores y 80 advertencias. No dice si el contenido es correcto. No tiene ensayos |
| Preguntas de competencia | De 22: 7 respondibles, 9 en parte y 6 todavía no | El estado sale de una prueba de cobertura y de un límite que el curador declara en cada pregunta |
| Revisión humana | Kit preparado: 193 pre-ensayos en 4 estratos | No se ejecutó. La hace el autor, que fija el umbral antes de abrir la clave |
| Revisión de la versión candidata | 128 hallazgos de 6 revisores automáticos | 15 altos, 72 medios y 41 bajos; 98 corregidos, 16 corregidos en parte y 14 documentados. Lo que se corrigió a partir de esta revisión no tuvo otra lectura |

## Por dónde empezar

**Antes de seguir, si vas a hacer la revisión humana a ciegas.** Leé primero `data/revision_humana_protocolo.md` y la planilla, y recién después los documentos 15 y 18: esos documentos nombran pre-ensayos que están en la muestra y dicen qué lectura tuvo cada uno. Si eso no te importa, seguí en este orden.

1. `docs/15_Decisiones_delegadas_y_relectura_1_4.md`: qué respondió el autor, qué se decidió por delegación y cómo se revierte, qué cambió con la relectura y qué queda por decidir.
2. `docs/16_Taxonomia_6_1.md`: la taxonomía completa, con las reglas decididas, los vacíos declarados, el eje H y los criterios de admisión.
3. `docs/18_Grafo_Categorizacion_y_Revision_Humana_1_4.md`: la categorización, el grafo candidato, lo que hace falta para llegar a un grafo con ensayos y el protocolo de la revisión humana.
4. `docs/17_Ontologia_2_2.md`: qué cambió en la ontología.
5. `docs/19_Arquitectura_Bitacora_y_Glosario_1_4.md`: las decisiones de arquitectura de esta versión, la bitácora, el glosario y cómo retomar.
6. `docs/02_De_AI_CISO_Atlas_a_Frontier_CISO_Atlas.md`: el porqué del nombre y cómo se navega con el Atlas. Es un registro de la versión 1.3: su razonamiento sigue valiendo y sus cifras son las de esa versión.

## Decisiones que esperan al autor

| Paso | Qué | Por qué en ese lugar |
|---|---|---|
| 1 | D-16, salvo D-16.2: confirmar, corregir o revertir lo que decidí. Son 21 proposiciones, y cada una dice de dónde sale. | Todo lo que cambió en esta versión se apoya en ellas, y ninguna la viste. |
| 2 | La revisión humana de la muestra (193 pre-ensayos): fijar el umbral, leer a ciegas y calcular. | Es la única fuente de validación humana. Si querés leer a ciegas, conviene hacerla antes de abrir los documentos 15 y 18. Una regla que rechaces en el paso 1 cambia la categorización y obliga a volver a sortear. |
| 3 | D-16.2: qué vara vale para cambiar una coordenada. | No tiene un «sí» por defecto. La revisión humana trae la única comparación con una lectura humana entre las dos varas, y por eso conviene decidirla después. También se puede decidir antes. |
| 4 | D-17: las decisiones nuevas (el alcance del MCCS, el candidato W02, las dos variables propuestas, los vacíos declarados, los casos sin cambio, la lectura de los indicadores, la relectura del pilar, el territorio T01, la regla para los ejes atados y la cláusula del criterio C2). | Son cambios de catálogo o lecturas que no bloquean el uso del Atlas. |

- **D-16:** 21 proposiciones, agrupadas por su origen: lo que el curador leyó como delegado, el resultado de los encargos que el autor aprobó y lo que el curador decidió por su cuenta (`docs/15_Decisiones_delegadas_y_relectura_1_4.md`, sección 7.1). Cada una dice qué pasa con cada respuesta. D-16.2, la de la vara, es una elección entre opciones y no tiene un «sí» por defecto.
- **Revisión humana:** `data/revision_humana_muestra.csv` para leer y `data/revision_humana_clave.csv` para abrir después. Se anota en una copia de la planilla, con otro nombre y fuera de `data/`.
- **D-17:** 10 decisiones nuevas. Ninguna bloquea el uso del Atlas.

## Estructura

| Carpeta o archivo | Qué contiene |
|---|---|
| `README.md`, `MANIFEST_SHA256.txt` | Esta guía y la huella de cada archivo |
| `00_Plan_de_Trabajo.md` y `00_Plan_de_Continuacion_1_1.md` a `00_Plan_de_Continuacion_1_4.md` | El plan de cada versión. El de la 1.4 dice qué se propuso hacer y qué se hizo |
| `docs/01` a `docs/14` | Registro de la versión 1.3, con una línea de aviso. No se actualizaron |
| `docs/15` a `docs/19` | Los documentos de esta versión |
| `data/` | Catálogos y planillas: taxonomía, ontología, corpus, relectura, decisiones, medición, biblioteca y revisión humana. Los análisis de las versiones 1.2 y 1.3 se conservan como se publicaron |
| `graph/` | El grafo candidato en SQLite y en CSV, el esquema, las consultas de aceptación y sus resultados |
| `changesets/` | Los conjuntos de cambios, en estado «propuesto» |
| `config/` | Las instrucciones del agente curador: la 7.4 rige de forma provisoria, hasta que el autor la confirme (D-16.17); la 7.2 y la 7.3 se conservan |
| `relectura_1_4/` | Todo lo que recibió y devolvió cada lector de esta versión: reglas, encargos, lotes, salidas y notas de cierre de las dos lecturas, la tercera lectura con su clave, la escala del pilar OS, la revisión previa de las reglas y las incidencias |
| `revision_1_4/` | La revisión de la versión candidata: encargos, hallazgos y triaje |
| `relectura_1_3/`, `revision_1_3/`, `revision_critica/` | Material de las versiones 1.3 y 1.2, sin cambios |
| `anexos/` | Informes de verificación de las versiones 1.0 y 1.2, sin cambios |
| `scripts/` | Los guiones que regeneran el paquete y sus datos de trabajo. `scripts/LEEME.md` trae el orden |

## Formatos

- Los archivos CSV usan punto y coma como separador y codificación UTF-8 con marca de orden de bytes, para abrirlos directamente en Excel.
- El grafo es una base SQLite. Se puede consultar con cualquier cliente de SQLite; las consultas de ejemplo están en `graph/consultas_de_aceptacion.sql`.

## Relación con el AI CISO Atlas

Se conservan la arquitectura, los códigos y las decisiones ADR-001 a ADR-012. Cambian el nombre, la taxonomía (5.3 a 6.1), la ontología (1.0.0 a 2.2.0) y las instrucciones del agente curador (6.0 a 7.4). Ningún artefacto vigente del proyecto se modificó: ni el GM-24, ni el banco de pre-ensayos, ni la base de la biblioteca, ni el catálogo CISO 365.

## Relación con las versiones anteriores

Las carpetas `Frontier_CISO_Atlas_v1.0` a `Frontier_CISO_Atlas_v1.3` siguen publicadas y no se tocaron. Esta versión las reemplaza como propuesta de trabajo, pero no las contiene archivo por archivo.

| Respecto de | Archivos de aquella versión | Iguales en la 1.4 | Actualizados en la 1.4 | No están en la 1.4 | Nuevos en la 1.4 |
|---|---|---|---|---|---|
| Versión 1.3 | 559 | 445 | 100 | 14 | 538 |
| Versión 1.2 | 349 | 235 | 102 | 12 | 746 |
| Versión 1.1 | 146 | 32 | 104 | 10 | 947 |
| Versión 1.0 | 115 | 31 | 74 | 10 | 978 |

El paquete 1.4 tiene 1083 archivos. El detalle, archivo por archivo, está en `data/archivos_por_version.csv`.

Lo que solo está en el paquete de la versión 1.3 (14 archivos): los generadores de los documentos 01 a 14 y los dos guiones que calculaban los análisis de las versiones 1.2 y 1.3. La muestra para la revisión humana que proponía la versión 1.3 se reemplazó por la de esta versión, con el mismo nombre de archivo: la anterior está en aquel paquete.

## Navegación de archivos

[Consultar el índice de archivos y subcarpetas](indice-catalogo.md).

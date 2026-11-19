> **Registro de la versión 1.3 (16 de noviembre de 2026).** Este documento se conserva tal como se publicó. Las cifras, los estados y los archivos que cita corresponden a esa versión. El estado vigente está en `docs/15_Decisiones_delegadas_y_relectura_1_4.md` y en los documentos 16 a 19.

# Glosario y continuidad

**Frontier CISO Atlas 1.3** · Taxonomía 6.0 (reglas de asignación, revisión 2) · Ontología 2.1.0 · GM-24 V7.1 · 16 de noviembre de 2026 · Estado: decisiones de diseño confirmadas por el autor; reglas adoptadas según la lectura del curador y corpus releído a ciegas por lectores automáticos, con una lectura para todos y dos donde la primera difería; contenido candidato, sin validación humana

## 1. Glosario

| Término | Significado |
|---|---|
| A2A | Agent2Agent. Protocolo abierto de comunicación entre agentes. |
| Adjudicación | Decisión escrita sobre un caso en que dos lecturas no coinciden. Se apoya en la tesis del texto y en una regla explícita, y queda registrada con su motivo. |
| ADR | Decisión de arquitectura registrada con contexto, decisión y consecuencias. |
| Ancla | Territorio donde el diseño espera que viva un pilar del MCCS. Es una hipótesis de diseño y no una descripción del corpus: hoy el ancla primaria reúne entre el 8 % y el 32 % de los pre-ensayos de cada pilar. |
| Artefacto de referencia | Documento publicado por un organismo: marco, norma, guía, catálogo, regulación o informe. |
| Base de trabajo | Estado de un contenido que el autor aceptó usar sin haberlo validado. No equivale a aprobado. |
| Biblioteca cognitiva | Acervo del autor con 1.404 conceptos sobre cómo se piensa y se decide: modelos mentales, sesgos, falacias, prácticas de decisión, capacidades y mentalidades. Es el contenido del pilar MM del MCCS y, en 59 conceptos, de la escala individual del pilar OS. |
| Caja cognitiva de 72 | Selección editorial de 72 conceptos de la Biblioteca cognitiva priorizados para el CISO. |
| Candidato | Estado de un nodo o una relación que todavía no fue aprobado por una persona. |
| Capa de ampliación | Pre-ensayos propuestos para celdas en blanco (serie APX). Están en el grafo candidato, aparte del corpus base de 739, y no cuentan para sus estadísticas. |
| Catalizador | Fuerza que acelera el cambio de una práctica. Códigos CAT. |
| CISO de frontera | El líder de seguridad que se para de frente al cambio tecnológico: lo evalúa, decide con evidencia si lo adopta, lo condiciona o lo difiere, y adecua sus modelos mentales, sus capacidades y las de su oficina. Lo define la calidad de la decisión, no su sentido. |
| Cobertura pedagógica | Vínculo propuesto entre una unidad del GM-24 y un concepto que la unidad enseña o ejercita. No afirma competencia adquirida. |
| Conjunto de cambios | Paquete de nodos y relaciones que se propone, se valida, se aprueba y se carga como una unidad. |
| Contexto de ejecución | Condiciones de partida de una organización que cambian cómo operan las fuerzas. Códigos HX. |
| Coordenada | La ubicación de un elemento en el Atlas: un territorio, un dominio y una subfunción primarios, con sus secundarios, más su horizonte y las fuerzas que trata. |
| Coordenada heredada | La que un pre-ensayo o un indicador ya traía de la Taxonomía 5.3 o del catálogo 1.2 del autor. La política de migración manda conservarla. |
| Definición de trabajo | Texto que el curador redactó para cada subfunción con su nombre, su categoría de NIST CSF 2.0 y los enunciados adoptados. El autor no las vio. |
| Dominio | Eje Y. La disciplina o el objeto. Códigos D01 a D28. |
| Empresa de frontera | Organización que trabaja en el borde del cambio tecnológico y lo incorpora de forma deliberada a su modelo operativo. |
| Ensayo | Texto completo y aprobado que desarrolla un concepto. Es la fuente de verdad del Atlas. |
| Enunciado adoptado | Enunciado de una regla propuesta que tenía texto listo y quedó como regla de asignación cuando el autor aceptó «el cambio de reglas». La adopción es una lectura del curador, a confirmar en la decisión D-15.1. |
| Estados de un hallazgo | «Corregido», «Corregido en parte», «Propuesta al autor», «Diferido» (se remite al autor, sin fecha) y «Documentado» (es un límite que se declara). |
| Estados de una ADR | «Alcanzada por la aceptación en bloque», «Sustituida», «Propuesta; rige de forma provisoria» y «Propuesta». El documento 08 define cada uno. |
| Estados de una decisión | «Aceptada»: el autor la aceptó en bloque y es de diseño. «Base de trabajo»: es una tarea de validación; se usa sin estar validada. «Confirmada»: el autor la confirmó de forma literal. «Abierta»: espera al autor. «Abierta en parte»: una parte tiene respuesta, literal o leída por el curador, y otra no. «Cerrada sin revisión»: el autor decidió no hacer lo que la decisión proponía. En la versión 1.2 existía además «Interpretada como sí; a confirmar». |
| Estrato | Parte del marco que se sortea por separado. En la muestra a ciegas, los estratos son la confianza que declaró el clasificador. |
| Frontera | El borde donde una práctica deja de estar consolidada. Es una condición evolutiva, no una tecnología. |
| Fuerza | Un catalizador o un inhibidor. Los mecanismos homeostáticos no son fuerzas: regulan, y se nombran aparte. |
| Función | Eje Z. Una de las seis funciones de NIST CSF 2.0: gobernar, identificar, proteger, detectar, responder y recuperar. |
| GM-24 | TheNextCISO GM-24. Currículo de 24 unidades en dos pilares y doce ejes. Versión vigente: V7.1. |
| H | Eje de evolución y homeostasis. Tiene seis catálogos: horizontes, catalizadores, inhibidores, mecanismos homeostáticos, factores de contexto y variables homeostáticas. |
| Hallazgo | Observación escrita de un revisor, con severidad, ubicación, evidencia y propuesta. Cada hallazgo recibe una decisión. |
| Homeostasis | Capacidad de mantener unas pocas variables vitales dentro de límites aceptables mientras todo lo demás cambia. |
| Horizonte | Estado evolutivo de una práctica: consolidada (H01), en evolución (H02), emergente (H03) o convergente (H04). |
| Inhibidor | Fuerza que frena el cambio de una práctica. Códigos INH. |
| Lente | Vista que no forma parte de la coordenada y no interviene en las reglas de precedencia: pilar MCCS, plano y pilar de la agenda de IA. Permite filtrar, no ubicar. |
| Marco de la muestra | El conjunto del que se sortea una muestra. El de la muestra a ciegas son los 595 pre-ensayos que no estaban en D20 ni eran migraciones. |
| MCCS | Meta-Cognitive CISO System. Sistema metacognitivo del CISO, con cuatro pilares. |
| MCP | Model Context Protocol. Protocolo abierto para conectar agentes con herramientas y datos. |
| Mecanismo homeostático | Lo que la organización hace para no perder el control durante el cambio. Códigos HOM. |
| MM, OS, DO, NX | Pilares del MCCS: modelos mentales, sistema operativo, entrega y operación, y evolución. |
| Nivel de autonomía | Grado de independencia de un agente, de L0 (solo informa) a L4 (autónomo con límites estrictos). |
| PAQ-01 | Comprobación propia del paquete, fuera de las 37 reglas de la ontología: avisa cuando un pre-ensayo del plano A nombra un producto o un proveedor. |
| Plano A | Corpus académico: conceptos, pre-ensayos y ensayos. Se propone agnóstico de proveedor; hoy 77 pre-ensayos nombran productos y están marcados para revisión. |
| Plano B | Capacidades contratadas: instancias de dominio con productos, tareas y agentes concretos. |
| PO-GAC | Dueño de producto-control y gerente de agentes cognitivos. Rol del sub-plan del GM-24 V7.1. |
| Pre-ensayo | Idea central desarrollada de un concepto. Es el origen de un ensayo; no es un ensayo. |
| Pregunta abierta | Enunciado que pide elegir entre opciones. Una aceptación no lo contesta. Si afecta a una coordenada y un lector lo anotó, el cambio de ese eje no se aplica. |
| Producto-control | Un control de seguridad tratado como producto: con objetivo, dueño, métricas, tareas y evidencia. |
| Punto abierto por la revisión | Punto que la revisión de la versión candidata 1.3 encontró sin decidir en las reglas adoptadas (RV-1 a RV-5). Los cambios de la relectura que caen en uno de ellos no se aplicaron. |
| Punto de control humano | Control humano asociado a una acción de un agente. Tiene tres modalidades: aprobación previa, auditoría posterior o prohibición de delegar. |
| Regla propuesta | Regla o aclaración de la taxonomía que la revisión crítica de la versión 1.2 propuso. Códigos RP-01 a RP-18, con 95 enunciados. Desde la versión 1.3 cada enunciado tiene un estado: adoptado, pregunta abierta, encargo hecho o encargo en cola. |
| Revisada por el autor en una muestra | Estado que tendría la categorización si el autor revisa la muestra propuesta y la regla de decisión se cumple. «Validada» se reserva para una revisión con una segunda persona. |
| Revisión crítica | Lectura de una copia congelada del paquete por revisores automáticos, cada uno con contexto propio y un encargo escrito, antes de publicar una versión. Tienen contexto independiente, no juicio independiente: comparten configuración con quien generó los artefactos. |
| Segunda lectura a ciegas | Clasificación de un mismo texto por un segundo lector que no conoce la clasificación vigente. Mide acuerdo entre lecturas, no acierto. |
| Serie APX | Dieciséis pre-ensayos de redacción asistida, propuestos para celdas sin contenido. Forman la capa de ampliación. |
| Subfunción | Subdivisión editorial de una función. Son 34 y no son categorías oficiales de NIST. |
| Territorio | Eje X. La perspectiva o responsabilidad desde la que se mira. Códigos T01 a T08. |
| Variable homeostática | Lo que hay que mantener dentro de límites aceptables mientras se cambia. Códigos HV. Hoy ninguna tiene unidad, umbral ni responsable del límite. |
| Vía de corrección | Regla de la versión 1.2 para cambiar una coordenada heredada: dos lecturas que coinciden, o una adjudicación escrita (ADR-028). El autor la confirmó el 16 de noviembre de 2026. La relectura le sumó condiciones (ADR-030), que rigen de forma provisoria. |

## 2. Cómo retomar el trabajo

El paquete alcanza para leer, consultar y decidir. Para regenerarlo completo hacen falta además algunas fuentes del autor, que la sección 3 enumera.

1. Leer `14_Decisiones_y_relectura_1_3.md` y `01_Resumen_Ejecutivo.md`.
2. Decidir si la relectura del corpus queda: dejarla, revertirla entera o revertir filas (`data/cambios_1_2_a_1_3.csv`; el documento 14, sección 7.2, dice cómo).
3. Contestar las 11 preguntas que siguen abiertas en las reglas (`data/preguntas_abiertas_1_3.csv`). Con cada respuesta se releen solo los pre-ensayos que esa pregunta frenó.
4. Hacer la revisión humana de la categorización con la muestra que propone el documento 14 (`data/revision_humana_muestra.csv`). Su estrato R1 dice si la relectura mejoró o empeoró lo que cambió.
5. Resolver lo que queda de la decisión D-13: los once casos de D20 y los 37 cambios de coordenada de la versión 1.2, con lo que la relectura dijo de cada uno (documento 14, sección 4.7).
6. Hacer los encargos en cola y abrir la próxima revisión de la ontología (solicitud OCR-CAND-03).
7. Redactar la primera tanda de ensayos (`data/primera_tanda_propuesta.csv`).
8. Regenerar el grafo con los guiones de `scripts/`, en el orden de la sección 3.

El orden importa, y es el de la sección 5: la decisión sobre la relectura fija la categorización sobre la que se apoya todo lo demás, y la revisión humana conviene hacerla sobre la categorización que quede.

## 3. Qué se regenera y con qué

Hay un solo orden de ejecución, y es el mismo que trae `scripts/LEEME.md`. La cuarta columna dice qué necesita cada paso además del paquete. Los pasos que no necesitan nada se regeneran solo con el paquete.

| Orden | Guion | Produce | Necesita además del paquete | Variable de entorno |
|---|---|---|---|---|
| 1 | `build_ontology.py` | Diccionarios de la ontología 2.1.0 | Los cuatro diccionarios de la ontología 1.0.0 del AI CISO Atlas (`ontology.json`, `entity_dictionary.json`, `relationship_dictionary.json` y `semantic_rules.json`) | `FCA_FUENTES` |
| 2 | `merge_clasif.py` | Corpus categorizado y estadísticas, con los ajustes de la revisión 1.2 y de la relectura 1.3 | — | — |
| 3 | `build_taxonomy.py` | Taxonomía 6.0 con decisiones, evidencia, cruces, reglas adoptadas y definiciones de trabajo de las subfunciones (usa `fca_model.py`, `cruces.py` y `reglas_adoptadas.py`) | — | — |
| 4 | `build_reference.py` | Base de referencia | — | — |
| 5 | `extraer_biblioteca.py` | Extracto de la Biblioteca cognitiva, con tipos, pilar, cobertura y prácticas contra sesgos | `Base_1404_Atlas_GM24.json` y `Cruce_editorial_72_GM24.json`, de la carpeta de integración de la Biblioteca | `FCA_BIBLIOTECA` |
| 6 | `extraer_medicion.py` | Indicadores del catálogo CISO 365 2.0 ubicados en el Atlas y sus vínculos con las variables homeostáticas | Los catálogos de indicadores 1.2 y del Modelo Operativo CISO 365 2.0 (JSON) | `FCA_FUENTES` |
| 7 | `propuestas_editoriales.py` | Remapeo propuesto, lectura de D20 y serie APX | — | — |
| 8 | `construir_grafo.py` | Grafo candidato, validación y conjuntos de cambios | La matriz consolidada de preguntas (CSV) | `FCA_FUENTES` |
| 9 | `consultas_de_aceptacion.py` | Preguntas de competencia y su resultado | — | — |
| 10 | `primera_tanda.py` | Primera tanda de ensayos propuesta | — | — |
| 11 | `comparar_control.py 12` | Comparación de la muestra de control | — | — |
| 12 | `casos_de_navegacion.py` | Casos de navegación resueltos | — | — |
| 13 | `revision_critica.py` | Resumen de la revisión crítica de la versión 1.2, calculado sobre la copia congelada de esa versión; registro de decisiones con las respuestas del autor del 16-nov-2026; cambios de la 1.1 a la 1.2 | — | — |
| 14 | `relectura_1_3.py` | Resumen de la relectura del corpus con las reglas adoptadas, casos para el autor, preguntas abiertas y cambios de la 1.2 a la 1.3 | — | — |
| 15 | `muestra_revision_humana.py` | Muestra y regla de decisión propuestas para la revisión humana, con la evidencia de la relectura | — | — |
| 16 | `docgen/` | Documentos, README e instrucciones del agente curador | — | — |

Las fuentes del proyecto se indican con la variable de entorno `FCA_FUENTES` y la carpeta de la Biblioteca con `FCA_BIBLIOTECA`. Sin esas fuentes pueden regenerarse 12 de los 16 pasos; los otros 4 ya dejaron sus resultados en el paquete, de modo que los pasos siguientes funcionan igual.

6 guiones no forman parte del orden. La lista sale del mismo archivo que el orden (`scripts/orden.py`) y es la que trae `scripts/LEEME.md`:

| Guion | Produce | Necesita | Variable de entorno |
|---|---|---|---|
| `reglas_adoptadas.py` | Estado de los 95 enunciados de las reglas después de la decisión del autor del 16-nov-2026 y definiciones de trabajo de las subfunciones. No se ejecuta: lo lee `build_taxonomy.py` | — | — |
| `build_corpus.py` | Corpus unificado (`datos_de_trabajo/corpus_unificado_raw.json`). Sirve para volver a extraer si cambian las fuentes | El paquete del GM-24 V7.1 y el banco de pre-ensayos | `FCA_FUENTES` y `FCA_GM24` |
| `corregir_extracto_agentes.py` | Catálogo de agentes del GM-24 con los campos en su lugar; con el paquete del GM-24 lo comprueba contra los anexos | Opcional: el archivo comprimido del GM-24 V7.1 | `FCA_GM24_ZIP` |
| `prep_batches.py` | Lotes de clasificación (`clasificacion/lote_N.jsonl`). Es el registro de cómo se armaron: volver a ejecutarlo los sobrescribe y no hace falta para regenerar el paquete | — | — |
| `regresion.py` | Comprueba el paquete: manifiesto, archivos citados, cifras clave de los documentos contra los datos y, con las fuentes del autor, regeneración en una copia limpia | Opcional: las fuentes del autor y las versiones publicadas | `FCA_FUENTES` y `FCA_BIBLIOTECA` y `FCA_PUBLICADO` |
| `orden.py` | Este orden de regeneración. No se ejecuta: lo leen el documento 10 y esta guía, para que no haya dos listas | — | — |

## 4. Calendario de revalidación

| Fecha | Qué revalidar | Qué puede cambiar |
|---|---|---|
| 17 al 20-nov-2026 | Microsoft Ignite 2026 | Estado del benchmark de nube v2, Agent 365, pilar de IA de Zero Trust |
| 19-nov-2026 | COBIT 7 | Cruce de COBIT con dominios; pre-ensayo APC-223 |
| 24-nov-2026 | Proyecto de ley británico | Estado de la regulación |
| 1-dic-2026 | Ley 21.719 de Chile | Vigencia |
| 2-dic-2026 | Reglamento de IA de la UE | Nuevas prohibiciones y fin de un plazo de gracia |
| 15-abr-2027 | CISSP | Cruce de CISSP con territorios y dominios |
| Cuando se publique | Cyber AI Profile de NIST (hoy borrador) | Respaldo de D20, D21 y D12; revisión de D21 a D23 |

## 5. Decisiones

La aceptación cubre las decisiones de diseño. Las tareas de validación (D-07, D-09 y parte de D-03, D-08 y D-10) se registran como «aceptadas como base de trabajo, sin validar»: aceptar que algo no tiene validación humana no lo valida. Los conjuntos de cambios siguen en estado «propuesto» (ADR-019).

| N.º | Proposición | Estado |
|---|---|---|
| D-01 | El producto se llama Frontier CISO Atlas y continúa al AI CISO Atlas: conserva sus códigos, su arquitectura y sus decisiones anteriores. | Aceptada, con la advertencia a la vista |
| D-04 | El pilar OS del MCCS se lee en dos escalas del mismo pilar: individual (T01) y de oficina (T03). | Aceptada |
| D-06 | Se adoptan las seis variables homeostáticas (HV01 a HV06) como propuesta de diseño, sin respaldo normativo externo. | Aceptada |
| D-02 | Se adopta la Taxonomía 6.0: 8 territorios, 28 dominios, 6 funciones, 34 subfunciones y el eje H ampliado. D27 se admite con reserva y D26 por materialidad. | Aceptada |
| D-03 | El gobierno, el riesgo y el cumplimiento de la IA que estaban alojados en D20 pasan a D01, D02 o D03 (regla 7). | Aceptada y aplicada |
| D-05 | Se adopta la Ontología 2.1.0, que contiene a la 2.0.0 y es un cambio mayor respecto de la 1.0.0. | Aceptada |
| D-08 | La Biblioteca cognitiva entra al grafo candidato con tipos del módulo de cognición. | Aceptada como base de trabajo; modificada por la revisión |
| D-09 | Los indicadores asignados miden cada variable homeostática, y las subfunciones PR06 y RC05 tienen indicadores. | Base de trabajo; corregida por la revisión |
| D-10 | Se acepta la propuesta de remapeo como pedido para la próxima versión del GM-24, y los 16 pre-ensayos de la serie APX como capa de ampliación. | Aceptada |
| D-07 | La categorización de los 739 pre-ensayos es válida y la primera tanda de ensayos es la propuesta. | Base de trabajo; validación humana pendiente |
| D-14 | Confirmar lo que el paquete leyó en el mensaje del autor del 15 de noviembre de 2026 y lo que hizo en su nombre. | Confirmada por el autor el 16 de noviembre de 2026 |
| D-15 | Confirmar o corregir lo que la versión 1.3 leyó en las tres frases generales del mensaje del 16 de noviembre de 2026 y las reglas de trabajo que esa versión puso a regir sin que el autor las viera. | Abierta: a confirmar o corregir por el autor; es la primera que conviene decidir |
| D-11 | Adoptar, modificar o rechazar las 18 reglas y aclaraciones que la revisión propone (RP-01 a RP-18), enunciado por enunciado. | Abierta en parte: los enunciados con texto listo quedan adoptados (lectura del curador, a confirmar en D-15.1); siguen abiertas las preguntas y los puntos que dejó la revisión, y en cola parte de los encargos |
| D-13 | Confirmar o revertir los cambios que la revisión aplicó sin la lectura del autor, y resolver los casos en que las lecturas no coinciden. | Abierta en parte: los cambios de la Biblioteca, la medición, la serie APX y los textos se leyeron como confirmados en bloque (a confirmar en D-15.2); la parte del corpus (D-13.1 y D-13.2) se leyó como sin respuesta |
| D-12 | Decidir cómo se revisa la Biblioteca cognitiva y qué se corrige en la base, que es del autor. | Cerrada sin revisión: la Biblioteca queda como estaba (lectura del curador, a confirmar en D-15.3) |

**Orden propuesto para las decisiones abiertas.** Es el mismo en el resumen ejecutivo, en el documento 14 y en el README:

| Paso | Qué | Por qué en ese lugar |
|---|---|---|
| 1 | D-15: confirmar o corregir cómo se leyeron tus tres frases generales y las reglas de trabajo que esta versión puso a regir. | Todo lo demás se apoya en esas lecturas. Si alguna no es la que quisiste, cambia lo que quedó adoptado, confirmado o cerrado. |
| 2 | Contestar los puntos que la revisión dejó abiertos (RV-1 a RV-5) y las preguntas abiertas de las reglas. | Cada respuesta destraba los cambios que ese punto frenó, sin volver a leer. |
| 3 | Decidir si los cambios que la relectura aplicó quedan: dejarlos, revertirlos enteros o revertir filas. | Es el cambio más grande de la versión 1.3 y se revierte en un paso. |
| 4 | La revisión humana de una muestra. | Es la única fuente de validación humana, y conviene hacerla sobre la categorización que quede después de los pasos 1 a 3. |
| 5 | D-13.1 y D-13.2: los once casos de D20 y los 37 cambios de coordenada de la versión 1.2. | La relectura trae evidencia nueva para decidirlos, y D-15.2 puede dejar contestada la segunda. |
| 6 | Los encargos en cola y la próxima revisión de la ontología (solicitud OCR-CAND-03). | Son trabajo de diseño y no bloquean lo anterior. |

Las instrucciones 7.2 del agente curador quedaron confirmadas con la decisión D-14.7. Las 7.3 las suceden para recoger las reglas adoptadas; lo que cambia lo redactó el curador.

## 6. Pendientes ordenados

1. Decidir si la relectura del corpus queda, y con eso confirmar o no la regla con que se hizo (ADR-030).
2. Contestar las 11 preguntas abiertas de las reglas.
3. Revisión humana de la categorización: la muestra, la regla de decisión, el camino mínimo y quién revisa están propuestos en el documento 14. El autor no respondió sobre ella.
4. Lo que queda de la decisión D-13: los once casos de D20 y los 37 cambios de coordenada de la versión 1.2.
5. Los 21 encargos en cola: el modelo de referencia del eje H, con la unidad, el umbral y el responsable de cada variable homeostática (RP-15); los criterios de admisión de dominios (RP-16); las anclas del MCCS (RP-14.1); las familias de dominios (RP-17.3); y el registro del plano en los nodos (RP-17.2).
6. Releer con las reglas adoptadas los indicadores y las preguntas de la matriz, y decidir si se releen el horizonte, las fuerzas y el pilar de los pre-ensayos.
7. Primera tanda de ensayos y registro de identificadores de ensayo.
8. Indicador para la subfunción PR06 y para los dominios sin indicador primario (D19, D22, D23 y D27).
9. Aplicar la política de migración a las preguntas heredadas de la matriz y a los indicadores heredados del catálogo 1.2, que siguen declarando la Taxonomía 5.3.
10. Carga de las notas del MCCS y del Documento Maestro del CISO-OS.
11. Guía para instanciar el Atlas en una organización.
12. Adopción del remapeo en la próxima versión del GM-24 y revalidación de COBIT después del 19-nov-2026.
13. Revalidación de la base de referencia después de Ignite 2026.
14. Próxima revisión de la ontología con la solicitud OCR-CAND-03.
15. Edición pública: decisión sobre el plano B, la Biblioteca, los indicadores y los pre-ensayos que nombran productos.
16. La Biblioteca queda sin revisar por decisión del autor (D-12). Si más adelante se decide revisarla, lo que la revisión crítica de la versión 1.2 dejó escrito sigue en `data/biblioteca_defectos_senalados.csv`.

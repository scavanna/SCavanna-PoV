> **Registro de la versión 1.3 (16 de noviembre de 2026).** Este documento se conserva tal como se publicó. Las cifras, los estados y los archivos que cita corresponden a esa versión. El estado vigente está en `docs/15_Decisiones_delegadas_y_relectura_1_4.md` y en los documentos 16 a 19.

# Bitácora de tareas realizadas

**Frontier CISO Atlas 1.3** · Taxonomía 6.0 (reglas de asignación, revisión 2) · Ontología 2.1.0 · GM-24 V7.1 · 16 de noviembre de 2026 · Estado: decisiones de diseño confirmadas por el autor; reglas adoptadas según la lectura del curador y corpus releído a ciegas por lectores automáticos, con una lectura para todos y dos donde la primera difería; contenido candidato, sin validación humana

Este documento registra qué se hizo, en qué orden, con qué resultado y qué desvíos hubo. Las fases 0 a 8 son la versión 1.0, cuyo plan está en `00_Plan_de_Trabajo.md`. Las fases 9 a 14 son la versión 1.1 (`00_Plan_de_Continuacion_1_1.md`). Las fases 15 a 21 son la versión 1.2 (`00_Plan_de_Continuacion_1_2.md`). Las fases 22 a 27 son la versión 1.3 (`00_Plan_de_Continuacion_1_3.md`).

Las fases 0 a 21, las incidencias 1 a 17 y las verificaciones de las versiones 1.0 a 1.2 se reproducen tal como se publicaron en la versión 1.2. Son registro histórico y no se reescriben: sus cifras son las de aquel momento. Lo que después se encontró equivocado en ese registro está en la sección 3.

## 1. Tareas por fase

### Fase 0 · Relevamiento de la base

| Tarea | Resultado |
|---|---|
| Leer la memoria del proyecto y los 12 documentos base del AI CISO Atlas | Línea base confirmada: Taxonomía 5.3 (8 territorios, 24 dominios, 6 funciones, 32 subfunciones) y Core Ontology 1.0.0 (8 módulos, 57 tipos de entidad, 58 relaciones, 21 reglas) |
| Abrir los paquetes del proyecto y elegir la fuente del GM-24 | Se usó el paquete maestro de 721 archivos del 15-nov-2026: GM-24 V7.1 con 379 conceptos, todos con pre-ensayo |
| Buscar versiones posteriores y anexos del GM-24 | No hay versión posterior a la V7.1. Los anexos son el sub-plan PO-GAC y las siete instancias de dominio del plano B |
| Localizar las fuentes del MCCS | Leídas las notas del MCCS, el Documento Maestro Consolidado del CISO-OS y el índice de la Biblioteca del CISO de frontera |
| Hallazgo | El pilar OS tiene dos lecturas en las notas; se adoptó la de dos escalas, a confirmar |

### Fase 1 · Plan de trabajo

| Tarea | Resultado |
|---|---|
| Escribir el plan antes de ejecutar | `00_Plan_de_Trabajo.md`: fases, criterios de admisión, riesgos y entregables |

### Fase 2 · Base de referencia

| Tarea | Resultado |
|---|---|
| Verificar artefactos de NIST, CISA, DoD y SEC | 26 entradas; anexo A1 |
| Verificar artefactos de ISO/IEC, ISA/IEC, ETSI, ISACA, ISC2, The Open Group, SABSA, FAIR, SFIA, ENISA, NACD–ISA, CyBOK y marcos sectoriales | 35 entradas; anexo A2 |
| Verificar artefactos de MITRE, OWASP, CIS, CSA, FIRST, cadena de suministro y protocolos de agentes | 28 entradas; anexo A3 |
| Verificar marcos de Microsoft y el concepto de empresa de frontera | 23 entradas; anexo A4 |
| Verificar regulación y informes de evidencia | 26 entradas; anexo A5 |
| Consolidar la base | 42 organismos y 145 artefactos: 99 verificados, 37 en parte, 2 no verificados y 7 internos |
| Registrar discrepancias y silencios | 14 discrepancias y 11 silencios |

### Fase 3 · Revisión de la taxonomía

| Tarea | Resultado |
|---|---|
| Medir la presión del corpus sobre la 5.3 | T08 es el territorio más poblado y no tenía dominio; arquitectura, criptografía y seguridad física no tenían alojamiento |
| Cruzar los elementos de primer nivel de los artefactos con dominios, territorios y funciones | 327 elementos con dominios, 80 con territorios y 54 con funciones |
| Definir criterios de admisión y aplicarlos | Cinco criterios; cuatro dominios admitidos; nueve candidatos en lista de vigilancia |
| Revisar funciones y subfunciones | 6 funciones sin cambio; 2 subfunciones nuevas por regla de cobertura de CSF 2.0 |
| Revisar el eje H | 5 elementos nuevos y 6 variables homeostáticas |
| Generar los catálogos | `data/taxonomia_v6_0.json` y sus tablas |

### Fase 4 · Ontología

| Tarea | Resultado |
|---|---|
| Extender la ontología 1.0.0 | Versión 2.0.0: 10 módulos, 84 tipos de entidad, 92 relaciones y 36 reglas |
| Normalizar los predicados editoriales del GM-24 | 116 predicados agrupados en familias; se conservan como dato |
| Verificar la coherencia interna | Ningún tipo inexistente citado, ningún par fuera de rango y ninguna regla inexistente citada |

### Fase 5 · Categorización del corpus

| Tarea | Resultado |
|---|---|
| Unificar el corpus | 739 pre-ensayos: 331 compartidos, 48 solo del GM-24 V7.1 y 360 solo del banco del Atlas |
| Escribir las instrucciones y el validador | Un documento de instrucciones y un validador determinista |
| Categorizar en ocho lotes | Los ocho lotes validan |
| Aplicar la política de migración | 73 migraciones a dominios nuevos; 18 sugerencias no aplicadas |
| Revisar las migraciones a dominios nuevos | Leídas una por una: todas tienen un motivo específico y ninguna se revirtió; 34 son de confianza media o baja y quedan primeras en la lista del curador |
| Muestra de control | Un clasificador independiente volvió a categorizar una muestra aleatoria: 48 pre-ensayos completados de 48 previstos. Acuerdo en horizonte: 93,8 %; en pilar MCCS: 87,5 %. Mide reproducibilidad, no acierto. |

### Fase 6 · Grafo de conocimiento

| Tarea | Resultado |
|---|---|
| Construir el grafo candidato | 3.378 nodos y 24.108 relaciones en 10 conjuntos de cambios propuestos |
| Validar contra la ontología | 0 errores y 0 advertencias |
| Ejecutar las preguntas de competencia | De 20: 11 respondibles, 2 en parte y 7 todavía no |
| Proponer una primera tanda de ensayos | 40 pre-ensayos elegidos con una regla transparente |
| Documentar los requisitos del grafo aprobado | 11 requisitos en `06_Grafo_de_Conocimiento.md` |

### Fase 7 · Documentación

| Tarea | Resultado |
|---|---|
| Redactar los documentos | Diez documentos, el archivo de presentación y las instrucciones 7.0 del agente curador |
| Generar los documentos desde los catálogos | Las cifras de los documentos salen de los archivos de `data/` y `graph/`, no se escribieron a mano |

### Fase 8 · Verificación y publicación

| Tarea | Resultado |
|---|---|
| Controles de integridad | Ver sección 3 |
| Empaquetar | Carpeta del paquete, archivo comprimido y manifiesto con huellas SHA-256 |

### Fase 9 · Versión 1.1: estado al retomar y fuentes nuevas

| Tarea | Resultado |
|---|---|
| Comprobar la entrega 1.0 | 115 archivos publicados; manifiesto y archivo comprimido íntegros; la copia de trabajo es idéntica a lo publicado |
| Releer la memoria y los archivos del proyecto | Después de la 1.0 se entregaron el Modelo Operativo CISO 365 2.0 y su edición 2.1, con un catálogo de 224 indicadores |
| Volver a buscar las fuentes del MCCS | Apareció la base «Integración Atlas 1404 – GM-24», con corte al 12-nov-2026 y 1.404 conceptos, que la versión 1.0 no había localizado |
| Escribir el plan de la continuación | `00_Plan_de_Continuacion_1_1.md`: qué pendientes se abordan, cuáles no y con qué reglas |

### Fase 10 · Versión 1.1: ontología 2.1.0

| Tarea | Resultado |
|---|---|
| Revisar la propuesta 2.0.0 | Versión 2.1.0: 84 tipos de entidad, 93 relaciones, 37 reglas y 22 preguntas de competencia. Una relación nueva, dos ampliadas, una regla, una definición precisada |
| Verificar la coherencia interna | Sin tipos, pares ni reglas inexistentes |

### Fase 11 · Versión 1.1: Biblioteca cognitiva

| Tarea | Resultado |
|---|---|
| Extraer la base sin modificarla | 1.404 conceptos de 11 categorías; huella SHA-256 de la base registrada |
| Tipificar con una regla determinista | 475 `CognitiveBias`, 388 `HumanCapability`, 199 `MentalModel`, 172 `Concept`, 170 `MetacognitivePractice` |
| Cargar territorios y pilar | 2.332 vínculos con territorios; primario solo con territorio único |
| Cargar la cobertura por unidad | 792 de 1.653 vínculos; 861 débiles quedaron fuera |
| Extraer los vínculos entre prácticas y sesgos | 142: 7 de la definición de la práctica, revisados uno por uno, y 135 de los controles compensatorios de las fichas |

### Fase 12 · Versión 1.1: medición

| Tarea | Resultado |
|---|---|
| Incorporar el catálogo 2.0 | 224 indicadores, 24 objetivos y 72 resultados clave |
| Ubicar los indicadores en el Atlas | 153 con subfunción y 71 solo con función; PR06 y RC05 con indicadores; K36 migra a PR06 |
| Proponer indicadores por variable homeostática | 71 vínculos, entre 9 y 15 por variable |
| Representar los órganos de gobierno | 3 órganos; 212 indicadores informan al menos a uno |

### Fase 13 · Versión 1.1: propuestas editoriales

| Tarea | Resultado |
|---|---|
| Preparar el remapeo a las matrices vigentes | 78 vínculos existentes y 2 nuevos; 18 para revisión del curador |
| Leer todo D20 con la regla de alcance | 14 se moverían, 11 a criterio del curador y 45 se quedan |
| Proponer pre-ensayos para celdas en blanco | 16: 7 para D19, 5 para D27, 4 para RC05 |

### Fase 14 · Versión 1.1: grafo, documentación y publicación

| Tarea | Resultado |
|---|---|
| Reconstruir el grafo candidato | 5.041 nodos y 29.887 relaciones en 15 conjuntos de cambios; 0 errores y 0 advertencias |
| Comprobar que lo anterior no cambió | Los archivos de operaciones de los conjuntos 01 a 09 tienen la misma huella que en la versión 1.0 |
| Ejecutar las preguntas de competencia | De 22: 13 respondibles, 4 en parte y 5 todavía no |
| Actualizar los documentos y agregar dos | Documentos 01 a 10 actualizados; 11 y 12 nuevos; instrucciones 7.1 del agente curador |
| Empaquetar y publicar | Paquete 1.1 publicado junto a la versión 1.0, que no se modificó |

### Fase 15 · Versión 1.2: aceptación del autor y coherencia de las decisiones

| Tarea | Resultado |
|---|---|
| Registrar la aceptación | El 15 de noviembre de 2026 aceptaste en bloque «las decisiones propuestas», con el supuesto de que no fueran contradictorias y apuntaran a la excelencia y al rigor. Tu mensaje literal, las citas normalizadas y cómo se leyó cada parte están en `data/decisiones_del_autor.json` |
| Registrar lo que hubo que interpretar | D-03 y D-10 eran preguntas y se contestaron con un «sí» en tu nombre. «Propone una forma de implementar […] informa y continua» se leyó como autorización para ejecutar la revisión sin otra consulta. Tu reflexión sobre cómo leer el Atlas se redactó como principio (ADR-029). Las cuatro lecturas quedan a confirmar en la decisión D-14, que se agregó en la verificación de cierre |
| Comprobar si se contradicen | El supuesto de tu aceptación no se cumplía del todo. Aplicadas a la vez, las diez decisiones chocaban en 4 puntos: dos se resolvieron (uno con el orden de aplicación y otro con un recorte de alcance), uno se resolvió en parte y uno sigue abierto. Si apuntan a la excelencia y al rigor es un juicio tuyo, que el paquete no puede certificar. Los cuatro puntos están en `13_Revision_critica_1_2.md` |
| Separar diseño de validación | La aceptación cubre las decisiones de diseño. Las tareas de validación (D-07, D-09 y parte de D-03, D-08 y D-10) se registran como «aceptadas como base de trabajo, sin validar»: aceptar que algo no tiene validación humana no lo valida. Los conjuntos de cambios siguen en estado «propuesto» (ADR-019). |
| Fijar el orden de aplicación | D-01 → D-04 y D-06 → D-02 → D-03 → D-05 → D-08 y D-09 → D-10 → D-07 |
| Escribir el plan | `00_Plan_de_Continuacion_1_2.md` |

### Fase 16 · Versión 1.2: diseño de la revisión crítica

| Tarea | Resultado |
|---|---|
| Congelar lo que se revisa | Copia de la versión 1.1 publicada: 146 archivos. Los revisores leyeron esa copia y no el trabajo en curso |
| Escribir los encargos | Un encargo por revisor, con qué leer, qué buscar y qué no hacer. Están en `revision_critica/` |
| Fijar el formato y el validador | Cada hallazgo lleva severidad, ubicación, evidencia y propuesta. Un validador rechaza los que no cumplen el formato |
| Fijar las reglas de decisión | Una coordenada heredada del corpus cambia cuando dos lecturas coinciden o cuando una adjudicación escrita se apoya en la tesis y en una regla explícita. Si no, queda como estaba y se informa. La fase 19 dice cuántos cambios cumplieron la regla en su forma estricta |

### Fase 17 · Versión 1.2: ejecución de la revisión

| Tarea | Resultado |
|---|---|
| Revisores | 13 encargos cerrados y válidos: Consistencia entre documentos y datos (42 hallazgos); Taxonomía y decisiones (82 hallazgos); Ontología y grafo (64 hallazgos); Segunda lectura de D20 (13 hallazgos); Segunda lectura de las migraciones (17 hallazgos); Muestra a ciegas del corpus (19 hallazgos); Biblioteca: tipos y pilar (15 hallazgos); Biblioteca: prácticas contra sesgos y territorios (17 hallazgos); Biblioteca: duplicados y equivalencias (9 hallazgos); Medición: indicadores y variables homeostáticas (19 hallazgos); Medición: territorio y dominio de los indicadores (14 hallazgos); Medición: subfunción de los indicadores (11 hallazgos); Lectura escéptica de un CISO y serie APX (42 hallazgos) |
| Segundas lecturas | D20 (71 pre-ensayos), migraciones a dominios nuevos (73), muestra del corpus (87 pre-ensayos), tipos de la Biblioteca (213 conceptos), prácticas contra sesgos (142 vínculos), territorios de la Biblioteca (100 conceptos), equivalencias entre la Biblioteca y el corpus (138 pares), subfunción de indicadores (71), territorio y dominio de indicadores (160) y serie APX (16 pre-ensayos). Solo la muestra del corpus se clasificó a ciegas, desde cero: en D20 y en las migraciones el revisor conocía parte de la coordenada, y las siete sugerencias se confirmaron con la propuesta a la vista |
| Verificaciones externas | 3 informes contra las páginas de los organismos emisores. Dos contrastaron 35 puntos del paquete: 9 sobre MITRE ATT&CK, MITRE ATLAS y CSA CCM (6 afirmaciones y 3 preguntas) y 26 afirmaciones sobre otras normas y marcos. El tercero verificó 9 citas que proponían los revisores, sobre subcategorías de NIST CSF 2.0 y las definiciones de apetito y tolerancia. Están en el anexo A7 y no se cuentan entre los hallazgos |
| Hallazgos | 364: 2 críticos, 46 altos, 213 medios, 70 bajos y 33 observaciones |

### Fase 18 · Versión 1.2: decisión sobre cada hallazgo

| Tarea | Resultado |
|---|---|
| Leer los 364 hallazgos y decidir | 163 corregidos, 39 corregidos en parte, 129 convertidos en propuestas para vos, 21 diferidos y 12 documentados como límite |
| Criterio de cierre | Todo hallazgo crítico o alto tiene una decisión escrita. Críticos: 2 corregidos. Altos: 31 corregidos, 5 corregidos en parte y 10 convertidos en propuestas para vos. Las decisiones las tomó quien generó los artefactos |
| Registro | `data/revision_critica_hallazgos.csv`: cada hallazgo con su decisión, la acción y dónde se ve |

### Fase 19 · Versión 1.2: correcciones

| Qué | Resultado |
|---|---|
| Taxonomía | Sigue siendo la 6.0: no cambian códigos ni cardinalidades. 17 correcciones de texto y de conteo, la prueba de los criterios C1 y C3 en los 28 dominios y 18 reglas propuestas que no se aplicaron |
| Base de referencia | 146 artefactos: 99 verificados, 37 en parte, 8 internos y 2 sin verificar. El cruce propio usa CCM v4.1 |
| Corpus | 37 pre-ensayos cambiaron de coordenada: en 13 dos lecturas deciden lo mismo, en 9 la primera lectura no había decidido y la segunda propone el destino, 7 son sugerencias confirmadas por un lector que las conocía y 8 se adjudicaron por escrito. D20 pasó de 71 a 45 |
| Biblioteca | 81 conceptos con el tipo corregido, 59 con el pilar OS, territorios como propiedad, 165 vínculos de cobertura y 57 de prácticas contra sesgos |
| Medición | De los 70 indicadores del catálogo 1.2, 67 heredan su coordenada sin cambios y 3 tienen el dominio corregido. Los otros 154 recibieron territorio y dominio de un revisor. Todo con una sola lectura. PR06 quedó sin indicadores. De 71 vínculos con variables, en 49 dos lecturas coinciden en el vínculo y en el papel |
| Propuestas editoriales | Remapeo resuelto con la verificación externa: 26 vínculos a retirar y 7 a agregar; no se aplicó al GM-24. Serie APX: 4 pre-ensayos quedaron como estaban y 12 se corrigieron |
| Ontología | No cambió: sigue la 2.1.0. La solicitud OCR-CAND-03 reúne 16 propuestas para la próxima revisión |
| Grafo candidato | 5.058 nodos y 28.142 relaciones en 16 conjuntos de cambios. La versión 1.1 tenía 5.041 y 29.887: hay menos relaciones porque se dejaron de cargar vínculos que la revisión no sostuvo |
| Validación | 0 errores y 77 advertencias, con 19 de 37 reglas comprobadas. Las advertencias son de una comprobación propia del paquete (PAQ-01): los pre-ensayos del plano A que nombran productos o al proveedor |
| Preguntas de competencia | De 22: 7 respondibles, 9 en parte y 6 todavía no |
| Primera tanda | 41 ensayos propuestos, recalculados después de aplicar la decisión D-03 |

### Fase 20 · Versión 1.2: documentación y armado del paquete candidato

| Tarea | Resultado |
|---|---|
| Actualizar los documentos | Documentos 01 a 10 y 12 actualizados; 11 conservado como registro de la versión 1.1, con una nota de erratas; 13 nuevo, con el informe de la revisión. README con una sección de uso previsto y límites; instrucciones 7.2 del agente curador |
| Armar el paquete candidato | Paquete completo, regenerado en una copia limpia sin diferencias. Se congeló una copia para la verificación de cierre |

### Fase 21 · Versión 1.2: verificación de cierre, segunda corrección y publicación

| Tarea | Resultado |
|---|---|
| Verificación de cierre | Cuatro revisores que no habían participado leyeron una copia congelada de la versión corregida. Uno recalculó las cifras de los documentos; otro comprobó el cierre de los 48 hallazgos críticos y altos; otro hizo una lectura escéptica de lo que se escribió durante la corrección, con tu mensaje literal a la vista; y otro comprobó una muestra de 60 hallazgos medios y bajos. De los 108 hallazgos comprobados, dieron por cerrados 85 y por cerrados en parte 23. Dejaron 139 hallazgos nuevos: 11 altos, 61 medios, 61 bajos y 6 observaciones. Después de esa segunda corrección, un revisor más hizo una lectura final de consistencia de los documentos reescritos (README, documentos 01 y 13, el registro de decisiones y partes de los documentos 07 a 10), recalculando sus cifras desde los datos. Dejó 16 hallazgos (2 altos, 14 medios): 14 corregidos, 2 corregidos en parte. En su nota de cierre listó además cuatro observaciones menores, que también se corrigieron |
| Muestra a ciegas complementaria | La verificación señaló que la muestra a ciegas no tenía ningún pre-ensayo de confianza media. Se sortearon 40 entre los 169 del marco y un revisor los clasificó desde cero. La muestra pasó a tener 87 pre-ensayos en tres estratos, y se informa por estrato y con intervalos |
| Segunda corrección | De los 139 hallazgos de cierre, 132 se corrigieron, 6 se corrigieron en parte y 1 se documentó, según quien los corrigió. De los 16 hallazgos que dejó la segunda lectura complementaria, 15 son sobre reglas que no deciden y se publican como insumo de la decisión D-11 (`data/reglas_D11_hallazgos_de_la_muestra_complementaria.csv`); el otro es un límite del método. El detalle está en `revision_critica/cierre/libro_de_cierre.csv`. De los 16 hallazgos de la lectura final, 14 corregidos, 2 corregidos en parte; esas últimas correcciones no tuvieron otra lectura |
| Regresión | 10 de 10 verificaciones sin diferencias. |
| Publicar | Paquete 1.2 publicado el 16 de noviembre de 2026, junto a las versiones 1.0 y 1.1, que no se modificaron |

### Fase 22 · Versión 1.3: registro de las decisiones del autor

| Tarea | Resultado |
|---|---|
| Registrar el mensaje del 16 de noviembre | Cuatro frases, guardadas como se escribieron. 7 respuestas literales, 10 leídas de una frase general y 2 proposiciones sin respuesta |
| Separar lo que el autor dijo de lo que se leyó | La columna de notas del autor queda vacía; la lectura del curador va en campos propios |
| Actualizar los estados | D-14 confirmada; D-01, D-03 y D-10 aceptadas; D-12 cerrada; D-11 y D-13 abiertas en parte; ADR-026 a ADR-029 aceptadas |

### Fase 23 · Versión 1.3: reglas adoptadas

| Tarea | Resultado |
|---|---|
| Clasificar los 95 enunciados de las 18 reglas | 60 adoptados, 11 preguntas, más la cláusula final de RP-10.6, y 24 encargos |
| Pasar las reglas a la taxonomía | Reglas de asignación, revisión 2; definición de D03; estado de cada regla y de cada enunciado |
| Redactar las definiciones de trabajo de las subfunciones (encargo RP-12.1) | 34 definiciones; 10 declaran una frontera que ninguna regla adoptada decide |

### Fase 24 · Versión 1.3: relectura del corpus

| Tarea | Resultado |
|---|---|
| Preparar la lectura a ciegas | Reglas para los lectores, encargo, validador y 19 lotes con los 755 pre-ensayos |
| Primera lectura | 755 lecturas validadas. Coincide con la coordenada vigente en 511 territorios, 575 dominios y 523 subfunciones |
| Fijar la regla de decisión | Antes de que existiera la segunda lectura: no entra un cambio si una lectura declaró confianza baja o anotó una pregunta abierta |
| Segunda lectura | 483 pre-ensayos en 13 lotes |
| Integrar las dos lecturas | Cambian 260 coordenadas en 204 pre-ensayos del corpus y 10 en 8 de la serie APX; 312 casos quedan para el autor |

### Fase 25 · Versión 1.3: aplicación, grafo y muestra

| Tarea | Resultado |
|---|---|
| Aplicar los cambios | Entran desde un solo archivo de ajustes; el valor anterior pasa a secundario |
| Conservar los análisis de la versión 1.2 | Se calculan sobre la copia congelada de esa versión (ADR-031) |
| Corregir la errata del grafo de la versión 1.2 | 394 aristas dejaron de declarar un cambio ocurrido en otro eje |
| Reconstruir el grafo | 5.058 nodos y 28.249 relaciones; 0 errores y 77 advertencias |
| Rediseñar la muestra para la revisión humana | 159 pre-ensayos en tres estratos; camino mínimo de 60 |

### Fase 26 · Versión 1.3: revisión de la versión candidata

| Tarea | Resultado |
|---|---|
| Revisión antes de publicar (ADR-027) | Cinco revisores automáticos sobre la versión candidata: 69 hallazgos (4 altos); 58 corregidos, 6 corregidos en parte y 5 documentados. Tercera lectura de 80 casos: en los 60 ejes que la versión candidata cambiaba, prefiere el valor nuevo en 52 y el anterior en 4. Después de la revisión se retiraron los cambios que dependen de seis puntos sin decidir |
| Corregir lo que encontró la revisión | El registro dejó de llevar lecturas del curador en el campo del autor; se abrió la decisión D-15, que le pide confirmar esas lecturas; el paquete trae literal la respuesta a la que contesta su mensaje |
| Frenar los cambios que dependen de puntos sin decidir | La revisión encontró 6 puntos sin decidir en las reglas adoptadas. Los 154 cambios que caen en ellos se retiraron: la relectura aplicaba 414 coordenadas en el corpus y ahora aplica 260 |
| Corregir la procedencia de las relaciones de función | Cuando cambia la subfunción cambia la función; esa relación llevaba el método del clasificador y ahora lleva el respaldo del cambio |

### Fase 27 · Versión 1.3: documentación y publicación

| Tarea | Resultado |
|---|---|
| Documentos | Documento 14 nuevo; documentos 01 a 10 y 12 actualizados; documentos 11 y 13 y planes anteriores, como se publicaron |
| Regresión | 14 de 14 verificaciones sin diferencias. |
| Publicar | Paquete 1.3, que se publica junto a las versiones 1.0, 1.1 y 1.2, sin modificarlas, después de la revisión y de la regresión de las dos filas anteriores |

## 2. Desvíos e incidencias

1. **Desconexión de la sesión.** A mitad del trabajo se perdió el área temporal. Se volvieron a extraer las fuentes y a lanzar las verificaciones; no se perdió ningún resultado final.
2. **Configuración de los agentes auxiliares.** Para las cinco verificaciones, los ocho lotes de categorización y la muestra de control usé agentes auxiliares. Al lanzarlos fijé de forma explícita el modelo en lugar de dejar la configuración predeterminada del espacio de trabajo, sin que lo hubieras pedido. Al advertirlo intenté relanzar la muestra de control con la configuración predeterminada y repetí el mismo ajuste: cancelé tres lanzamientos y dejé correr el cuarto. Si tu configuración indica otra cosa para los agentes auxiliares, estos trabajos no la respetaron y conviene que lo sepas antes de darlos por buenos.
3. **Informes de verificación.** Los agentes de verificación no pudieron guardar archivos. Sus informes se recuperaron del registro de la sesión y están completos en los anexos A1 a A5.
4. **Libros de Excel con etiqueta de confidencialidad.** No se pudieron leer. Se usaron las exportaciones JSON y CSV de los mismos datos.
5. **Versiones de Open FAIR.** La verificación de hoy no coincide con lo que registra la memoria del proyecto. Queda como discrepancia abierta.
6. **Reglas de alcance aplicadas de forma despareja.** 2 de los ocho clasificadores aplicaron la regla que lleva el gobierno y el riesgo de la IA de D20 a D01 y D02. Por eso esos cambios quedaron como sugerencia y no se aplicaron.

De la versión 1.1:

7. **La versión 1.0 subestimó la Biblioteca.** Informó 1.356 conceptos «no incorporados» a partir de un índice anterior y no localizó la base de integración de 1.404 conceptos que ya estaba en tu OneDrive desde el 12-nov-2026. Esta versión la usa. Los documentos de la 1.0 publicada conservan la cifra anterior.
8. **Una cifra fija estaba mal en la 1.0.** La solicitud de cambio de ontología registrada en el grafo decía que la 2.0.0 agregaba 14 reglas; son 15. Era un texto escrito a mano en un guion. Ahora se calcula.
9. **Un límite de la ontología 2.0.0.** La pregunta de competencia 16 no podía responderse con aristas válidas, porque `MEASURES` no admitía una variable homeostática del catálogo como destino. Se corrigió en la 2.1.0.
10. **Pérdida del entorno de ejecución entre sesiones.** Al retomar, el entorno donde corrían los comandos se había perdido. Antes de continuar se comprobó que lo publicado y los archivos de trabajo estaban íntegros.
11. **Agentes auxiliares.** En la versión 1.1 no se usó ninguno: todo se hizo con guiones deterministas y lectura directa.

De la versión 1.2:

12. **La incidencia 2 era inexacta, y mi primera corrección también.** La incidencia 2 decía que al lanzar los agentes auxiliares de la versión 1.0 yo había fijado su configuración de forma explícita, sin que lo pidieras. El registro de eventos de la sesión muestra otra cosa, y más matizada de lo que anoté al empezar esta revisión. Entre el 15 y el 16 de noviembre se lanzaron 53 agentes auxiliares. En 40 el pedido que quedó registrado no lleva ninguna configuración: la agregó un paso de la plataforma, siempre con el mismo valor, que es el de la conversación principal. Entre esos 40 están los 20 de la versión 1.0 (cinco verificaciones, tres comprobaciones puntuales que la incidencia 2 no mencionaba, ocho lotes de categorización y cuatro lanzamientos de la muestra de control), de modo que la incidencia 2 se equivocaba en la atribución. En 13 sí la escribí yo, sin que lo pidieras: fueron lanzamientos de la revisión crítica, entre las 20:26 y las 21:15 del 15 de noviembre, hechos después de anotar la regla de no indicarla. El valor que escribí es el mismo que la plataforma agrega cuando no escribo nada, de modo que esos revisores corrieron con la misma configuración que todos los demás y no veo motivo para descartar sus resultados. Son C5a, C5b, C5c, C6a (dos lanzamientos), C6b, C6c, C8, el relanzamiento de C4b, C4c y las tres verificaciones externas; C1, C2, C3 y C4a trabajaron en agentes lanzados sin esa indicación. No puedo ver cuál es tu preferencia para los agentes auxiliares: solo puedo informar qué hizo la plataforma y qué escribí yo.
13. **Veintiuna detenciones innecesarias.** Cuando releo un lanzamiento ya hecho lo veo con la configuración que agregó la plataforma, y a simple vista no se distingue de una que hubiera escrito yo. Por creer que el error era mío detuve agentes que estaban bien lanzados: tres en la versión 1.0 (la muestra de control), catorce al empezar la revisión crítica y cuatro al lanzar la verificación de cierre, cuando ya conocía el problema. En esa última ocasión además te informé el error como propio antes de comprobarlo, y lo rectifiqué al mirar el registro; los cuatro revisores retomaron su encargo. Ningún agente detenido había producido resultados: no se perdió trabajo, se perdió tiempo. Hubo una falsa alarma más, esta vez sin detención: al lanzar la lectura final de consistencia volví a ver la configuración en el lanzamiento, te dije que la había escrito yo y lo retiré al mirar el registro, que muestra ese pedido sin ella. La regla que queda es comprobar en el registro de eventos antes de detener un agente y antes de informar un error como propio, y no indicar nunca esa configuración. Estas cifras salen del registro de la sesión, que es lo único que puedo comprobar: no puedo explicar por qué veo esa configuración en mis propios lanzamientos.
14. **Tres revisores que hubo que retomar.** Dos revisores de la revisión crítica terminaron sin entregar nada: su respuesta final quedó retenida y no habían guardado en disco, aunque el formato común pide guardar por tramos. Los relancé una sola vez, con el encargo dividido en dos y con guardado por tramos. Por eso los encargos son 13 y no 11. Los cuatro resultantes cerraron. En la verificación de cierre pasó algo parecido con el revisor de la muestra complementaria: su primera respuesta quedó retenida y no había guardado; le pedí por mensaje que guardara en disco y completó el encargo. No establecí la causa: pudo ser el tamaño del encargo, la forma de trabajar del revisor o la retención de la respuesta. Decir que fue solo la plataforma, como decía la primera redacción de esta incidencia, era decir de más.
15. **Desconexiones de la sesión.** Hubo dos durante el día, que impidieron iniciar 18 lanzamientos. El estado se guardaba en archivos a medida que avanzaba, y las llamadas que no se ejecutaron se repitieron. No se perdió ningún resultado; se perdió tiempo, que no medí.
16. **Errores propios que encontró la revisión.** Los más graves no eran de criterio sino de ejecución: un catálogo cargado con los campos corridos, estados escritos a mano que se presentaban como resultados, y frases fijas que contradecían los datos. La sección 3 los enumera. Ninguna de mis verificaciones anteriores los había detectado.
17. **Errores propios que encontró la verificación de cierre.** La versión corregida también tenía errores, y de otro tipo: describía la muestra a ciegas como un sorteo del corpus cuando no lo era; presentaba como «aceptadas» dos decisiones que yo había contestado en tu nombre; daba por resuelto un choque entre decisiones que seguía abierto; contaba como «dos lecturas» cambios que tenían una; y el texto de las ADR alcanzadas por tu aceptación se había regenerado con cifras nuevas. Fueron 139 hallazgos, 11 de ellos altos, y 16 más en la lectura final. Los corregí antes de publicar, y los que no corregí están listados en el material de cierre.

De la versión 1.3 (son las mismas que trae el documento 14, sección 9):

18. **Seis avisos de una selección de modelo que el registro no confirma.** Durante esta versión el curador le avisó seis veces al autor que los lanzamientos de agentes auxiliares llevaban una selección de modelo que él no había pedido. El registro de eventos de la sesión guarda los 42 lanzamientos de esta versión (19 lectores de la primera lectura, 13 de la segunda, 5 revisores que se cancelaron y 5 que hicieron la revisión), y los 42 llevan exactamente los cinco campos que admite la regla de este trabajo; ninguno lleva una selección de modelo. Los avisos se basaban en lo que el curador veía en el eco de sus llamadas. La regla escrita en la versión 1.2 era comprobar el registro antes de avisar; el curador lo consultó con un filtro mal hecho, no encontró los lanzamientos y le dijo al autor que el registro no los guardaba. Era falso, y se lo corrigió en el mismo turno, cuando lo comprobó bien.
19. **Cinco revisores detenidos sin necesidad.** Por una de esas falsas alarmas, el curador les pidió a los cinco revisores recién lanzados que se detuvieran, cuando no habían escrito nada, y los relanzó en carpetas nuevas. La regla escrita era no detener agentes por esa señal.
20. **El conteo de lanzamientos de la versión 1.2 se sostiene.** Esa versión informó 53 agentes, 13 de ellos con una configuración escrita por quien despachaba. El registro de toda la sesión muestra 113 lanzamientos y 13 con ese parámetro, todos anteriores a esta versión.
21. **Tres lectores terminaron un turno sin escribir su salida.** El lector del lote adicional de la segunda lectura y los dos lectores de la tercera lectura cerraron su primer turno sin archivos. Los escribieron después de un mensaje que se lo pidió, y sus salidas pasaron la validación.
22. **La segunda lectura se armó antes de que cerrara la primera.** Las 755 lecturas estaban en disco y validadas, pero cuatro lectores todavía podían corregir su salida, y lo hicieron. Al cerrar la primera lectura, un pre-ensayo (APC-066) había pasado a diferir de la coordenada vigente y no estaba en la segunda. Se leyó en un lote adicional, con siete pre-ensayos de control más.
23. **Un lector listó la carpeta de salidas.** El del lote 04 de la primera lectura declaró en su cierre que ejecutó un listado de esa carpeta para contar sus archivos. El encargo pedía no abrir nada fuera de los propios. Su nota dice que no leyó otras salidas; eso no se puede comprobar.
24. **El archivo de reglas se reescribió durante la primera lectura.** Una prueba del curador volvió a generar el archivo que los lectores estaban usando. El contenido era idéntico (misma huella) y los lotes no cambiaron.
25. **Una omisión en el encargo de los lectores.** Las definiciones de las subfunciones nombran fronteras sin decidir, y el encargo no dio un código para anotarlas. Lo señalaron en su nota de cierre 27 de los 32 lectores. No se corrigió a mitad de la lectura.
26. **El defecto del grafo de la versión 1.2 apareció por una prueba.** Las 394 aristas con procedencia equivocada se vieron al listar todas las aristas de un pre-ensayo de prueba, no por una verificación diseñada para encontrarlas.
27. **El árbol de trabajo arrancó de una carpeta vacía.** Varios pasos fallaron hasta que se lo sembró con el paquete 1.2. De ahí sale la precisión sobre la «copia limpia» de la sección 8 del documento 14.
28. **Tres pasos de la cadena suponían que solo la versión 1.2 cambiaba coordenadas.** Fallaron en el ensayo con cambios de prueba. Se corrigieron para que los análisis de la versión 1.2 se calculen sobre el corpus de esa versión.

## 3. Correcciones al registro de las versiones anteriores

Lo que sigue estaba mal o incompleto en lo que informaron las versiones 1.0 y 1.1. Los paquetes publicados no se modificaron: conservan el texto original.

| Dónde | Qué decía | Qué se comprobó | Hallazgos |
|---|---|---|---|
| Fases 6 y 14, y verificaciones | El grafo «valida contra la ontología con 0 errores y 0 advertencias» | El validador evaluaba 13 de las 37 reglas, y una de las que no evaluaba exige descripción en todo nodo: 1.809 de los 5.041 nodos de la versión 1.1 no la tenían. La validación es estructural. La versión 1.2 comprueba 19 de 37 reglas y publica cuáles | C1-031, C3-003, C8-020 |
| Fases 6 y 14 | Preguntas de competencia: 11 respondibles de 20 en la versión 1.0 y 13 de 22 en la 1.1 | El estado de cada pregunta era un valor escrito en el guion, no el resultado de una prueba. Con un criterio (si puede expresarse, cobertura y límite declarado) son 7 respondibles, 9 en parte y 6 todavía no; sobre las 20 originales, 6, 8 y 6 | C3-006, C8-027 |
| Fases 6 y 14 | El catálogo de agentes del plano B, cargado al grafo | Los 85 registros de agentes tenían los campos corridos dos posiciones: los puntos de control humano eran en realidad categorías de costo, y se perdían la autonomía, los riesgos, los dueños y las herramientas de 70 agentes. Se corrigió la correspondencia de campos y se comprobó contra los anexos del GM-24 | C3-001, C1-013 |
| Fase 5 | Migraciones a dominios nuevos: «leídas una por una; ninguna se revirtió» | Una segunda lectura, que no conocía el dominio al que se había migrado cada pre-ensayo, coincidió en 69 de 73. Las otras 4 se adjudicaron por escrito y cambiaron de dominio | C4b |
| Fase 5 | La muestra de control «mide reproducibilidad» | En 45 de sus 48 casos el clasificador recibió el valor vigente con la instrucción de conservarlo: casi no mide la asignación de territorio ni de dominio. La medida que vale es la muestra a ciegas: muestra a ciegas de 87 pre-ensayos en tres estratos; acuerdo estimado para los 595 del marco, con intervalo del 95 %: territorio 73 % (64–83), dominio 86 % (80–93), subfunción 80 % (72–89) | C8-005 |
| Fase 11 | Biblioteca: tipos por una regla determinista, territorios cargados y cobertura por unidad | La regla por categoría no alcanza: 81 conceptos recibieron otro tipo por lectura. Los territorios eran un valor por categoría de la base, no una clasificación por concepto, y ya no se cargan como clasificación. La cobertura se redujo de 792 a 165 vínculos: los de coincidencia temática quedaron fuera | C5a-002, C5b-012, C5b-013, C5c-003, C8-018 |
| Fase 11 y verificaciones | Los vínculos entre prácticas y sesgos de confianza media, «revisados uno por uno» | De los 142 vínculos, la segunda lectura sostuvo 57, juzgó débiles 77 e incorrectos 8. Uno de los siete de confianza media era verdadero por definición. Se cargan solo los que se sostienen | C5b-001, C5b-010 |
| Fase 12 | «PR06 y RC05 con indicadores; K36 migra a PR06» | Los cuatro indicadores ubicados en PR06 miden acceso y segmentación de red, no resiliencia de la infraestructura ni protección física: pasaron a PR03 y PR06 quedó sin indicadores. Además, el catálogo 1.2 tenía 70 indicadores con coordenada y no 64 | C6c-001, C8-009, C1-006 |
| Fase 13 | Lectura de D20: 14 se moverían, 11 a criterio del curador y 45 se quedan | El desglose sumaba 70 de 71. Con la decisión D-03 aplicada, 26 se movieron y 45 quedan | C1-011 |
| Verificaciones | «El paquete se regeneró desde sus propios guiones en una copia limpia» | Es cierto con las fuentes del autor a mano: dos guiones del orden de regeneración leían archivos que no viajan en el paquete, y el documento 10 y el LEEME daban órdenes distintos. Ahora hay un solo orden y dice qué necesita cada paso | C1-018 |
| Incidencia 2 | «Fijé de forma explícita el modelo» de los agentes auxiliares de la versión 1.0 | En esos lanzamientos no fue así: la configuración la agregó la plataforma. Sí la escribí en 13 lanzamientos de la revisión crítica, con el mismo valor. Ver la incidencia 12 | — |

De la versión 1.2, encontrado en la versión 1.3:

- **El grafo publicado tenía 394 aristas con procedencia equivocada.** En los 37 pre-ensayos cuya coordenada cambió, las demás aristas de clasificación (las de los ejes que no habían cambiado y las secundarias del eje que cambió) declaraban en su método un cambio ocurrido en otro eje. La versión 1.2 había corregido la arista del eje cambiado y no las demás. No afectaba coordenadas ni conteos. Se corrigió en la versión 1.3.
- **«Regeneración en una copia limpia» decía más de lo que era.** La verificación regenera el paquete sobre una copia del propio paquete, no desde una carpeta vacía; al menos un archivo de datos se hereda de versiones anteriores y ningún guion lo crea.
- **El documento 06 decía 14 propuestas en la solicitud de cambio de la ontología.** El archivo de la solicitud OCR-CAND-03 tiene 16. Se corrigió en la versión 1.3.

## 4. Verificaciones realizadas

**Versiones 1.0 y 1.1**, tal como se informaron:

| Verificación | Resultado |
|---|---|
| Validador determinista de los ocho lotes de categorización | Los ocho válidos |
| Coherencia interna de la ontología | Sin tipos, pares ni reglas inexistentes |
| Validación del grafo contra la ontología | 0 errores y 0 advertencias |
| Resolución de los elementos de marco del mapeo del GM-24 | Todos resueltos |
| Independencia de la muestra de control | El clasificador de control leyó solo las instrucciones, el validador y su lote |
| Cifras de los documentos | Generadas desde los catálogos |
| Integridad del paquete | Manifiesto con huella SHA-256 de cada archivo |
| Versión 1.1: entrega anterior | Manifiesto de la 1.0 verificado archivo por archivo antes de continuar |
| Versión 1.1: conjuntos de cambios 01 a 09 | Misma huella de operaciones que en la 1.0 |
| Versión 1.1: taxonomía, base de referencia y categorización | Sin cambios respecto de la 1.0 |
| Versión 1.1: códigos de los pre-ensayos propuestos | Todos existen en la Taxonomía 6.0 y respetan las cardinalidades |
| Versión 1.1: vínculos práctica→sesgo de confianza media | Leídos uno por uno contra el texto de la base |
| Versión 1.1: regeneración | El paquete se regeneró desde sus propios guiones en una copia limpia |

**Versión 1.2:**

| Verificación | Resultado |
|---|---|
| Validación estructural del grafo | 0 errores y 77 advertencias; 19 de 37 reglas comprobadas |
| Reconstrucción del grafo desde los conjuntos de cambios | Los nodos y las relaciones reconstruidos son iguales a los del grafo |
| Punto de control en tareas y agentes de nivel L2 o superior | 92 de 92 agentes y 132 de 139 tareas; 7 tareas no tienen agente ejecutor |
| Catálogo de agentes del GM-24 | 835 campos de los 85 agentes comprobados contra los anexos del GM-24, sin diferencias |
| Hallazgos críticos y altos | 48 de 48 con decisión escrita |
| Manifiesto del paquete | 348 archivos con su huella SHA-256; 0 no coinciden y 0 no figuran en el manifiesto |
| Versiones 1.0 y 1.1 publicadas | versión 1.0: 115 archivos, 0 diferencias con su manifiesto; versión 1.1: 146 archivos, 0 diferencias con su manifiesto. No se modificaron |
| Archivos citados en los documentos | 278 citas en 17 documentos; 0 no existen |
| Estadísticas contra los datos | 23 cifras recalculadas desde los archivos de datos y desde la base del grafo; 0 no coinciden |
| Cifras clave de los documentos | 37 cifras clave buscadas en 9 documentos, cada una junto a la palabra que la nombra; 0 no aparecen. No comprueba las demás cifras de los documentos |
| Hallazgos críticos y altos | 48 hallazgos; 0 sin decisión, acción o lugar donde se ve |
| Grafo candidato | 0 errores de validación; reconstrucción desde los conjuntos de cambios igual al grafo |
| Versión que declaran los archivos de datos | 0 archivos declaran una versión del producto distinta de la 1.2 |
| Rastros del entorno de trabajo | 347 archivos de texto revisados; 0 con rutas internas |
| Regeneración en una copia limpia | 26 pasos ejecutados con los guiones del paquete y las fuentes del autor; 349 archivos comparados, 0 diferencias |
| Verificación de cierre | Cuatro revisores que no habían participado leyeron una copia congelada de la versión corregida. Uno recalculó las cifras de los documentos; otro comprobó el cierre de los 48 hallazgos críticos y altos; otro hizo una lectura escéptica de lo que se escribió durante la corrección, con tu mensaje literal a la vista; y otro comprobó una muestra de 60 hallazgos medios y bajos. De los 108 hallazgos comprobados, dieron por cerrados 85 y por cerrados en parte 23. Dejaron 139 hallazgos nuevos: 11 altos, 61 medios, 61 bajos y 6 observaciones. Después de esa segunda corrección, un revisor más hizo una lectura final de consistencia de los documentos reescritos (README, documentos 01 y 13, el registro de decisiones y partes de los documentos 07 a 10), recalculando sus cifras desde los datos. Dejó 16 hallazgos (2 altos, 14 medios): 14 corregidos, 2 corregidos en parte. En su nota de cierre listó además cuatro observaciones menores, que también se corrigieron |

**Versión 1.3:**

| Verificación | Resultado |
|---|---|
| Las decisiones de la relectura están en el corpus | Cada eje de cada pre-ensayo tiene en el corpus el valor que decidió el integrador de las dos lecturas: comprobado al generar el resumen |
| Los análisis de la versión 1.2 no cambiaron | Calculados sobre la copia congelada de esa versión |
| Validación estructural del grafo | 0 errores y 77 advertencias; 19 de 37 reglas comprobadas |
| Reconstrucción del grafo desde los conjuntos de cambios | Los nodos y las relaciones reconstruidos son iguales a los del grafo |
| Manifiesto del paquete | 558 archivos con su huella SHA-256; 0 no coinciden y 0 no figuran en el manifiesto |
| Versiones 1.0, 1.1 y 1.2 publicadas | versión 1.0: 115 archivos, 0 diferencias con su manifiesto; versión 1.1: 146 archivos, 0 diferencias con su manifiesto; versión 1.2: 349 archivos, 0 diferencias con su manifiesto. No se modificaron |
| Archivos citados en los documentos | 375 citas en 21 documentos; 0 no existen |
| Estadísticas contra los datos | 34 cifras recalculadas desde los archivos de datos y desde la base del grafo; 0 no coinciden |
| Cifras clave de los documentos | 49 cifras clave buscadas en 11 documentos, cada una junto a la palabra que la nombra; 0 no aparecen. No comprueba las demás cifras de los documentos |
| Hallazgos críticos y altos | 48 hallazgos; 0 sin decisión, acción o lugar donde se ve |
| Grafo candidato | 0 errores de validación; reconstrucción desde los conjuntos de cambios igual al grafo |
| Errata del grafo de la versión 1.2 | 0 relaciones de clasificación de ejes que no cambiaron dicen en su método que el eje cambió (en el grafo publicado de la 1.2 eran 394) |
| Columnas reservadas al autor | 4 archivos con columnas para la decisión o la nota del autor; 0 tienen algo escrito por el curador; 0 campos del autor con algo que él no respondió de forma literal en el registro de decisiones |
| Versión que declaran los archivos de datos | 0 archivos declaran una versión del producto distinta de la 1.3 |
| Rastros del entorno de trabajo | 555 archivos de texto revisados; 0 con rutas internas |
| Regeneración en una copia del paquete | 28 pasos ejecutados con los guiones del paquete y las fuentes del autor, sobre una copia del paquete y no sobre una carpeta vacía; 559 archivos comparados, 0 diferencias |
| Integración de la relectura | El integrador del paquete vuelve a escribir el archivo de ajustes a partir de las lecturas guardadas; el resultado es idéntico al que viaja en el paquete |
| Reversión de la relectura | Con las listas de cambios vacías y tres guiones ejecutados, 739 de 739 pre-ensayos del corpus y 16 de 16 de la serie APX vuelven a la coordenada de la versión 1.2, y el grafo vuelve a 5.058 nodos y 28.142 relaciones, los de esa versión |
| Revisión de la versión candidata | Cinco revisores automáticos sobre la versión candidata: 69 hallazgos (4 altos); 58 corregidos, 6 corregidos en parte y 5 documentados. Tercera lectura de 80 casos: en los 60 ejes que la versión candidata cambiaba, prefiere el valor nuevo en 52 y el anterior en 4. Después de la revisión se retiraron los cambios que dependen de seis puntos sin decidir |

## 5. Lo que no se hizo

- No se redactó ningún ensayo ni se asignó ningún identificador de ensayo.
- No se modificó ningún artefacto vigente del proyecto: ni el GM-24, ni el banco de pre-ensayos, ni las matrices, ni el catálogo CISO 365, ni la base de la Biblioteca, ni el sitio.
- No se cambiaron los códigos ni las cardinalidades de la Taxonomía 6.0, ni la Ontología 2.1.0.
- No se contestaron las 11 preguntas que siguen abiertas en las reglas, ni se hicieron los 21 encargos en cola: el modelo de referencia del eje H, los criterios de admisión, las anclas del MCCS, las familias de dominios y el registro del plano.
- No se revisaron los indicadores K59, K43 y K54, que un revisor pidió revisar sin proponer otra coordenada.
- No se revisó la Biblioteca concepto por concepto: el autor decidió no revisarla (decisión D-12).
- No se releyeron con las reglas adoptadas los indicadores, las preguntas de la matriz ni la Biblioteca. Tampoco el horizonte, las fuerzas, el pilar ni los secundarios de los pre-ensayos.
- No se aplicó la política de migración a las preguntas heredadas de la matriz ni a los indicadores del catálogo 1.2: 1.069 clasificaciones del grafo siguen declarando la Taxonomía 5.3 (705 son de preguntas heredadas de la matriz y 364 son de indicadores del catálogo 1.2).
- No se separaron las 136 celdas vacías de territorio y dominio entre las que no pueden darse y las que no tienen contenido.
- No se escribió la guía para instanciar el Atlas en una organización.
- No se cargaron las notas del MCCS ni el Documento Maestro del CISO-OS, que son texto sin estructurar.
- No se aplicó el remapeo al GM-24: sigue siendo una propuesta.
- No se comprobó si la edición 2.1 del Modelo Operativo CISO 365 modifica el catálogo de indicadores.
- No se revalidó lo que depende de Ignite 2026 ni de COBIT 7, que todavía no ocurrieron.
- No hubo una segunda ronda completa de revisión sobre la versión 1.2: hubo una verificación de cierre, y lo que se corrigió después de ella no lo volvió a leer ningún revisor.
- La revisión de la versión 1.3 se limitó a lo que cambió en ella; lo que se corrigió después tampoco tuvo otra lectura.
- Las lecturas del mensaje del 15 de noviembre quedaron confirmadas (D-14). Las del mensaje del 16 de noviembre que salen de una frase general no tienen confirmación del autor.
- No hubo revisión humana de ningún elemento.
- Los entregables están en Markdown, JSON, CSV y SQLite. No se generaron libros de Excel, documentos de Word ni presentaciones.

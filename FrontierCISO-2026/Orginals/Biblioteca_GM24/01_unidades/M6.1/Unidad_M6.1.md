<!-- generado-gm24 sha256:a8bb6d92a5876fe3e1861945d9d7192682a07e5f85cec87ead2b231811c940a4 -->
# M6.1 — Continuidad, DRP y Resiliencia Operativa

**Pilar:** Gestión · **Eje:** Resiliencia, tecnologías y cadena de suministro · **Atlas:** `D16` (alineación editorial, no identidad de dominio).

**Pregunta rectora de fuente:** ¿Cómo puede un CISO diseñar, ejecutar y verificar continuidad, drp y resiliencia operativa sin perder de vista el riesgo empresarial, las responsabilidades y la evidencia?

**Alcance:** diez conceptos base con idea central desarrollada; 2 ampliaciones Atlas cuyo título pertenece al Documento Maestro y cuya tesis es propuesta [P]. Los puentes HC relacionados son candidatos transversales; ninguna extensión altera por sí sola el número de unidades.

## Situación longitudinal y decisión

**Organización ficticia:** Las copias de seguridad restauran servidores, pero los índices RAG y las instrucciones de agentes provienen de una versión comprometida.

**Decisión a sostener:** Definir la restauración completa de un servicio IA con objetivos y pruebas funcionales.

**Cursos de acción en tensión:** Recuperar solo infraestructura frente a restaurar datos, modelos, identidades, conectores e índices verificados.

**Información inicial:** BIA, backups inmutables, pruebas DRP, inventario de dependencias de modelos

**Interesados:** continuidad, plataformas, datos y proveedor de IA

**Producto acumulativo:** plan de recuperación de IA con secuencia, pruebas y criterios de aceptación

**Regla de seguridad y responsabilidad:** Una copia disponible no prueba que el servicio de negocio vuelva a operar de forma íntegra.

## Desarrollo de los diez conceptos base

### M6.1-K01 — Continuidad (BCP)

La continuidad del negocio establece cómo sostener procesos críticos durante perturbaciones mediante prioridades y capacidades de operación alternativa. El escenario que conviene examinar es el siguiente: un plan enumera servidores sin contemplar procesos y personas. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M6.1-K01.md) (435 palabras de borrador, no ensayo final).

### M6.1-K02 — Recuperación (DRP)

El plan de recuperación tecnológica define secuencia, dependencias, recursos y pruebas para restaurar sistemas de soporte al negocio. El escenario que conviene examinar es el siguiente: la restauración depende de identidades o claves inaccesibles. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M6.1-K02.md) (434 palabras de borrador, no ensayo final).

### M6.1-K03 — Resiliencia Operativa

La resiliencia operativa integra anticipación, absorción, adaptación y recuperación para mantener servicios dentro de tolerancias. El escenario que conviene examinar es el siguiente: una arquitectura redundante falla por dependencia compartida. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M6.1-K03.md) (432 palabras de borrador, no ensayo final).

### M6.1-K04 — ISO 22301

ISO 22301 proporciona requisitos de un sistema de gestión de continuidad que deben adaptarse a alcance, contexto y evidencia. El escenario que conviene examinar es el siguiente: la certificación se confunde con garantía de disponibilidad. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M6.1-K04.md) (434 palabras de borrador, no ensayo final).

### M6.1-K05 — Pruebas Continuidad

Las pruebas de continuidad deben demostrar capacidades bajo escenarios relevantes y revelar brechas antes de una crisis real. El escenario que conviene examinar es el siguiente: el ejercicio se limita a revisar documentos sin activar equipos. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M6.1-K05.md) (436 palabras de borrador, no ensayo final).

### M6.1-K06 — Backups Inmutables

Los backups inmutables reducen la posibilidad de alteración maliciosa, pero requieren aislamiento, claves, retención y pruebas de restauración. El escenario que conviene examinar es el siguiente: se presume recuperabilidad porque existe copia inmutable. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M6.1-K06.md) (434 palabras de borrador, no ensayo final).

### M6.1-K07 — Alta Disponibilidad

La alta disponibilidad reduce interrupciones por fallas específicas, pero no reemplaza continuidad ni recuperación frente a corrupción o ataques. El escenario que conviene examinar es el siguiente: la replicación propaga datos cifrados por ransomware. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M6.1-K07.md) (434 palabras de borrador, no ensayo final).

### M6.1-K08 — Sitio Alternativo

Un sitio alternativo permite sostener o recuperar servicios bajo condiciones de indisponibilidad del entorno principal, con dependencias probadas. El escenario que conviene examinar es el siguiente: el sitio alternativo comparte la misma identidad o conectividad fallida. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M6.1-K08.md) (436 palabras de borrador, no ensayo final).

### M6.1-K09 — Gestión Crisis (Negocio)

La gestión de crisis coordina decisiones empresariales, comunicación y prioridades durante perturbaciones más allá de la respuesta técnica. El escenario que conviene examinar es el siguiente: el SOC decide restauración sin consultar prioridades del negocio. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M6.1-K09.md) (439 palabras de borrador, no ensayo final).

### M6.1-K10 — Dependencias

Las dependencias de servicios, datos, personas y terceros determinan qué puede recuperarse y en qué secuencia. El escenario que conviene examinar es el siguiente: un componente pequeño bloquea múltiples servicios críticos. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M6.1-K10.md) (429 palabras de borrador, no ensayo final).

## Ampliaciones Atlas de esta unidad: tesis para discutir, no definiciones aprobadas

- **[AMP-47 — Recuperación de servicios de IA](../../02_conceptos/02_ampliaciones_atlas/AMP-47.md) [P].** Recuperar un servicio de IA incluye modelos, índices, instrucciones, conectores e identidades de agentes, no solo infraestructura. Vínculo propuesto: `HC-021`; fuente `06Ensayos!I331`.
- **[AMP-48 — Dependencias de modelos](../../02_conceptos/02_ampliaciones_atlas/AMP-48.md) [P].** Depender de un modelo o proveedor de IA crea riesgo de concentración y de cambio no controlado: hay que mapearlo y prever alternativas. Vínculo propuesto: `HC-023`; fuente `06Ensayos!I332`.

## Conceptos híbridos candidatos que conectan esta unidad

- [HC-007 — Resiliencia gobernada por impacto](../../02_conceptos/03_hibridos_candidatos/HC-007.md): conecta `M5.1-K02`, `G4.2-K02`, `M6.1-K01`, `M6.1-K05`. **Candidato**, no unidad ni arista aprobada.
- [HC-008 — Cadena de confianza en terceros](../../02_conceptos/03_hibridos_candidatos/HC-008.md): conecta `G3.1-K04`, `M6.2-K01`, `M6.2-K07`, `M6.1-K10`. **Candidato**, no unidad ni arista aprobada.
- [HC-021 — Recuperación como prueba de confianza](../../02_conceptos/03_hibridos_candidatos/HC-021.md): conecta `M6.1-K02`, `M6.1-K06`, `M5.2-K03`, `G6.2-K08`. **Candidato**, no unidad ni arista aprobada.
- [HC-022 — Gobierno de crisis multidisciplinario](../../02_conceptos/03_hibridos_candidatos/HC-022.md): conecta `G4.1-K08`, `M5.1-K08`, `M6.1-K09`, `G6.1-K09`. **Candidato**, no unidad ni arista aprobada.
- [HC-023 — Riesgo de concentración tecnológica](../../02_conceptos/03_hibridos_candidatos/HC-023.md): conecta `M6.1-K10`, `M6.2-K08`, `M3.1-K10`, `G1.2-K05`. **Candidato**, no unidad ni arista aprobada.
- [HC-025 — Competencias y resiliencia organizacional](../../02_conceptos/03_hibridos_candidatos/HC-025.md): conecta `M1.2-K07`, `M1.2-K08`, `M5.1-K04`, `M6.1-K03`. **Candidato**, no unidad ni arista aprobada.
- [HC-030 — Seguridad industrial y continuidad de negocio](../../02_conceptos/03_hibridos_candidatos/HC-030.md): conecta `M6.2-K05`, `M3.1-K07`, `M5.1-K02`, `M6.1-K05`. **Candidato**, no unidad ni arista aprobada.

## Puente con TheMetaCognitiveCISO

Se propone entrenar la lente cognitiva `MM-0075` junto a las decisiones de `M6.1`. Esta es una **relación pedagógica derivada**, no una equivalencia canónica con el GM-24. Consulte [la caja cognitiva del CISO](../../../Biblioteca_CISO_Frontera/Caja_Cognitiva_CISO_72/00_Indice.md) para la ficha y su evidencia.

## Laboratorio: ocho modalidades de ejercicio

Las tareas comparten el mismo caso; no son ocho horas añadidas por separado. Se practican en la asignación indicativa de 3 h de seminario, 8 h de investigación y lectura, 12 h de laboratorio y 8 h de aplicación por unidad. Los tiempos requieren aprobación académica.

### 1. Comprensión conceptual

**Consigna:** Define `M6.1-K01` (Continuidad (BCP)) y `M6.1-K06` (Backups Inmutables) con tus palabras. Señala una frontera de responsabilidad, una confusión habitual y cómo la ampliación `AMP-47` altera la interpretación del caso «Las copias de seguridad restauran servidores, pero los índices RAG y las instrucciones de agentes provienen de una versión comprometida.».

**Producto:** cuadro de contraste con dos decisiones distintas y citas a las fichas.

**Comprobación:** No declara como sinónimos dos títulos vecinos ni toma la tesis [P] como definición aprobada.

### 2. Relaciones y contextualización

**Consigna:** Dibuja la cadena de decisiones entre `M6.1-K01`, `M6.1-K06`, `AMP-47` y `HC-021` — Recuperación como prueba de confianza. Anota en cada conexión dirección, evidencia textual, posible solapamiento y qué cambiaría al variar el contexto de negocio. Las aristas nuevas son hipótesis hasta que se validen.

**Producto:** mapa de relaciones G–M y tabla de procedencia de cada enlace.

**Comprobación:** No transforma cercanía temática en causalidad ni convierte HC en requisito aprobado.

### 3. Práctica aplicada

**Consigna:** Trabaja en «Las copias de seguridad restauran servidores, pero los índices RAG y las instrucciones de agentes provienen de una versión comprometida.». Con BIA, backups inmutables, pruebas DRP, inventario de dependencias de modelos, construye plan de recuperación de IA con secuencia, pruebas y criterios de aceptación; incluye propietario, condiciones de entrada y salida, hipótesis adversa y prueba de funcionamiento.

**Producto:** plan de recuperación de IA con secuencia, pruebas y criterios de aceptación.

**Comprobación:** Una copia disponible no prueba que el servicio de negocio vuelva a operar de forma íntegra.

### 4. Investigación y fuentes

**Consigna:** Investiga esta pregunta acotada: contrastar RTO/RPO con objetivos reales de procesos y fallos de proveedores compartidos. Localiza al menos dos fuentes primarias con fecha y versión; distingue obligación, recomendación, definición, ejemplo y opinión.

**Producto:** ficha de fuentes con extractos breves, localizador y discrepancias.

**Comprobación:** No cita un borrador editorial o mapeo informativo como norma obligatoria.

### 5. Orquestación de actores y agentes

**Consigna:** Con continuidad, plataformas, datos y proveedor de IA, construye un flujo de tres hitos para «Definir la restauración completa de un servicio IA con objetivos y pruebas funcionales.». Define qué puede proponer un agente, qué requiere aprobación humana, quién responde y cómo detener, registrar y revertir una acción errónea.

**Producto:** RACI/DACI, diagrama de traspasos y plan de supervisión.

**Comprobación:** Hay autoridad, trazas y camino de escalamiento para cada acción de alto impacto.

### 6. Análisis y contrafactual

**Consigna:** Compara «Recuperar solo infraestructura frente a restaurar datos, modelos, identidades, conectores e índices verificados.» usando datos de BIA, backups inmutables, pruebas DRP, inventario de dependencias de modelos. Contrasta la primera impresión con la lente cognitiva `MM-0075` del programa metacognitivo; plantea qué evidencia falsaría cada hipótesis y un efecto de segundo orden.

**Producto:** matriz de alternativas, incertidumbres y pruebas refutatorias.

**Comprobación:** La comparación conserva supuestos, costos de reversión y consecuencias no observadas.

### 7. Toma de decisiones

**Consigna:** Redacta para el responsable competente una recomendación sobre «Definir la restauración completa de un servicio IA con objetivos y pruebas funcionales.», con dos opciones, beneficio, riesgo residual, autoridad de aceptación, indicador temprano y condición explícita de pausa o rollback.

**Producto:** memorando ejecutivo de una página más expediente de evidencia.

**Comprobación:** Una copia disponible no prueba que el servicio de negocio vuelva a operar de forma íntegra.

### 8. Exposición y defensa

**Consigna:** Defiende la decisión ante continuidad, plataformas, datos y proveedor de IA en siete minutos; reserva tres para objeciones. Un par cambia un dato del escenario a mitad de la exposición: revisa la postura sin ocultar el supuesto que deja de sostenerse.

**Producto:** presentación oral, preguntas difíciles y registro de revisiones.

**Comprobación:** La defensa distingue certeza, incertidumbre, decisión y propiedad del riesgo.

## Rúbrica formativa y evidencia de logro

| Criterio | 0 — insuficiente | 2 — parcial | 4 — sólido |
|---|---|---|---|
| Precisión | Confunde conceptos, categorías o estados editoriales | Explica definiciones sin límites | Distingue base, propuesta y candidato; explica límites y relaciones sin equivalencias ficticias |
| Evidencia | Cita sin procedencia ni prueba | Traza fuentes pero no su calidad | Localiza fuente, versión, modalidad, incertidumbre y prueba de eficacia |
| Decisión y autoridad | No compara opciones ni propietario | Compara pero sin residual o escalamiento | Justifica alternativas, derecho de decisión, residual, parada y revisión |
| Transferencia | Entrega teórica sin caso | Caso parcial sin contraprueba | Artefacto operable, prueba adversa y defensa ajustada a la audiencia |

**Condición crítica de esta unidad:** Una copia disponible no prueba que el servicio de negocio vuelva a operar de forma íntegra. La práctica se devuelve para revisión si incumple este criterio, aunque el promedio sea alto. Para aprendizaje se propone al menos 3/4 en cada dimensión; no es una acreditación aprobada.

## Preguntas mayéuticas, sin confundirlas con afirmaciones

**Pregunta original consolidada (muestras):**
- `PC-075`: ¿Nuestras copias de seguridad son inmutables, aisladas, cifradas y están protegidas frente a administradores comprometidos? (vínculo `M6.1-K06`).
- `PC-076`: ¿Tenemos un plan para recuperar el proveedor de identidad y operar si este falla o queda comprometido? (vínculo `M6.1-K02`).
- `PC-079`: ¿Cómo aseguramos la resiliencia de endpoints y servidores ante fallas masivas (por ejemplo, una actualización defectuosa) y no solo ante ataques? (vínculo `M6.1-K03`).
- `PC-080`: ¿Podemos operar los procesos críticos con mecanismos manuales o alternativos durante varios días? (vínculo `M6.1-K01`).
- `PC-184`: ¿Qué haríamos si un proveedor cambia, retira o degrada un modelo del que depende un proceso crítico, o cambia sus políticas de datos? (vínculo `AMP-48`).
- `PC-289`: Si un servicio de IA del que depende un proceso se cae o se degrada, ¿pasamos a un modelo alternativo o a un proceso manual, y lo ejercitamos? (vínculo `AMP-47`).

**Serie de banco construida desde plantillas documentadas (muestras):**
- `BM-0661` — ¿Qué problema de gobierno, riesgo o capacidad intenta resolver realmente «Continuidad (BCP)», y qué decisión debería mejorar si se comprende correctamente?
- `BM-0662` — ¿Qué supuesto habitual sobre «Continuidad (BCP)» podría ser falso o incompleto, y qué consecuencia tendría diseñar la seguridad como si fuera cierto?
- `BM-0664` — ¿Qué problema de gobierno, riesgo o capacidad intenta resolver realmente «Recuperación (DRP)», y qué decisión debería mejorar si se comprende correctamente?
- `BM-0665` — ¿Qué supuesto habitual sobre «Recuperación (DRP)» podría ser falso o incompleto, y qué consecuencia tendría diseñar la seguridad como si fuera cierto?
- `BM-1065` — ¿Qué problema de gobierno, riesgo o capacidad intenta resolver realmente «Recuperación de servicios de IA», y qué decisión debería mejorar si se comprende correctamente?
- `BM-1066` — ¿Qué supuesto habitual sobre «Recuperación de servicios de IA» podría ser falso o incompleto, y qué consecuencia tendría diseñar la seguridad como si fuera cierto?

**Tesis propuestas por pregunta asignadas explícitamente a esta unidad: 3.**
- [APC-076 — Recuperación del proveedor de identidad comprometido o caído](../../03_metodo_mayeutico/01_tesis_derivadas/APC-076.md) ← `PC-076`
- [APC-079 — Resiliencia de equipos y servidores ante fallas masivas no maliciosas](../../03_metodo_mayeutico/01_tesis_derivadas/APC-079.md) ← `PC-079`
- [APA-036 — Impacto financiero de la falla prolongada de un proveedor crítico](../../03_metodo_mayeutico/01_tesis_derivadas/APA-036.md) ← `PA-036`

**Tesis transversales relacionadas sin asignación principal (muestras):**
- [APC-063](../../03_metodo_mayeutico/01_tesis_derivadas/APC-063.md) (relación transversal, no asignación principal)
- [APC-097](../../03_metodo_mayeutico/01_tesis_derivadas/APC-097.md) (relación transversal, no asignación principal)
- [APC-203](../../03_metodo_mayeutico/01_tesis_derivadas/APC-203.md) (relación transversal, no asignación principal)
- [APC-244](../../03_metodo_mayeutico/01_tesis_derivadas/APC-244.md) (relación transversal, no asignación principal)
- [APC-253](../../03_metodo_mayeutico/01_tesis_derivadas/APC-253.md) (relación transversal, no asignación principal)

El banco completo conserva 543 preguntas originales y 2.395 preguntas derivadas mecánicamente de plantillas; 308 tesis AP forman un **anexo provisional**, distinto de los 331 conceptos del corpus de trabajo.

## Lecturas, investigación y modalidad

**Lecturas internas verificables:**
- [Documento Maestro](../../../Curado02/01_noviembre_2026/src-thenextciso-gm-24-documento-maestro__9b8c53df319d.md), unidad `M6.1` desde línea 966.
- [lote de ideas base](../../../Curado02/01_noviembre_2026/src-thenextciso-gm24-ensayos-bases-211-240__be3ff9fea8f4.md)
- Las 51 tesis Atlas [P] proceden de `06Ensayos!I285:I335` en [matriz de pre-ensayos](../../../Curado02/01_noviembre_2026/src-ai-ciso-atlas-ensayos-thenextciso-x-core-accountabilities-fy27-2026-11-05__5528a05eb5dd.xlsx).

**Lecturas complementarias por cotejar:** NIST CSF 2.0, NIST RMF y dominios CISM/CRISC según la unidad y las fuentes listadas por el Documento Maestro. El mapeo de este documento es una propuesta temática: `CISM C4; CRISC R1,R4; NIST CSF 2.0 RC.RP,RC.CO,ID.AM; NIST RMF Prepare,Implement,Monitor.`. La fuente oficial, edición y pertinencia deben comprobarse al preparar cada clase; no se presume cobertura íntegra de examen o norma.

**Recursos audiovisuales:** no se identificó un video específico, vigente y verificable por unidad en los documentos base. Existe un [inventario complementario de enlaces observados](../../../Biblioteca_CISO_Frontera/Consolidado_2026_MM_2026-11-11/03_programa_1200h/Videos_Observados_en_Fuentes.md), aún sin comprobación de contenido, disponibilidad, duración ni correspondencia con esta unidad. El equipo docente deberá seleccionarlos, comprobar derechos y documentar el vínculo antes de asignarlos.

**Carga de diseño:** 31 h por unidad; 24 unidades más capstone integrador de 56 h = escenario de 800 h. No es acreditación.

<!-- generado-gm24 sha256:ceeaf074f137639c4fb64798480ce562c51a6cc84b6cc38810871e5437ed46a5 -->
# M5.1 — Planificación y Preparación (Incl. BIA)

**Pilar:** Gestión · **Eje:** Respuesta a incidentes y crisis · **Atlas:** `D15,D16` (alineación editorial, no identidad de dominio).

**Pregunta rectora de fuente:** ¿Cómo puede un CISO diseñar, ejecutar y verificar planificación y preparación (incl. bia) sin perder de vista el riesgo empresarial, las responsabilidades y la evidencia?

**Alcance:** diez conceptos base con idea central desarrollada; 2 ampliaciones Atlas cuyo título pertenece al Documento Maestro y cuya tesis es propuesta [P]. Los puentes HC relacionados son candidatos transversales; ninguna extensión altera por sí sola el número de unidades.

## Situación longitudinal y decisión

**Organización ficticia:** En un tabletop de ransomware, un agente comprometido intenta aislar servidores de respaldo durante una restauración crítica.

**Decisión a sostener:** Diseñar mando de incidentes, RTO/RPO, reglas de kill switch y escalamiento.

**Cursos de acción en tensión:** Mantener al agente para conservar velocidad frente a suspender su autonomía y operar en modo degradado.

**Información inicial:** BIA, plan IRP, inventario de permisos, datos de prueba y criterios de severidad

**Interesados:** CSIRT, negocio, continuidad, proveedores y junta

**Producto acumulativo:** guion de tabletop con injects, decisiones por minuto y matriz de autoridad

**Regla de seguridad y responsabilidad:** El mecanismo de detención se demuestra en ejercicio y preserva registros para investigación.

## Desarrollo de los diez conceptos base

### M5.1-K01 — IRP (Plan Respuesta)

Un plan de respuesta a incidentes establece autoridad, activación, coordinación, procedimientos y criterios de escalamiento antes de una crisis. El problema aparece cuando el documento existe pero los equipos desconocen quién puede contener sistemas o notificar a clientes. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M5.1-K01.md) (447 palabras de borrador, no ensayo final).

### M5.1-K02 — BIA (Impacto Negocio)

El análisis de impacto al negocio identifica procesos críticos, consecuencias de interrupción, dependencias y tolerancias para orientar continuidad y respuesta. El problema aparece cuando se prioriza restaurar servidores por orden técnico y no por servicio empresarial. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M5.1-K02.md) (443 palabras de borrador, no ensayo final).

### M5.1-K03 — CSIRT

Un CSIRT coordina competencias, autoridades y flujos para investigar, contener y comunicar incidentes con responsabilidades explícitas. El problema aparece cuando la respuesta depende de voluntarios y carece de enlace con legal, comunicaciones o negocio. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M5.1-K03.md) (439 palabras de borrador, no ensayo final).

### M5.1-K04 — Preparación (Readiness)

La preparación para incidentes consiste en comprobar recursos, permisos, procedimientos, evidencia y capacidad de actuar antes de que ocurra un evento grave. El problema aparece cuando la organización dispone de herramientas pero no tiene acceso de emergencia ni copias verificadas. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M5.1-K04.md) (447 palabras de borrador, no ensayo final).

### M5.1-K05 — Clasificación Incidentes

La clasificación de incidentes permite decidir severidad, prioridad, escalamiento y obligaciones de respuesta mediante criterios consistentes y revisables. El problema aparece cuando cada analista asigna severidad diferente o una alerta se declara incidente sin evaluación. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M5.1-K05.md) (441 palabras de borrador, no ensayo final).

### M5.1-K06 — Ejercicios Tabletop

Los ejercicios tabletop prueban decisiones, coordinación y comunicación en escenarios simulados sin asumir que sustituyen pruebas técnicas. El problema aparece cuando un ejercicio sin objetivos ni observadores termina en conversación sin aprendizajes verificables. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M5.1-K06.md) (440 palabras de borrador, no ensayo final).

### M5.1-K07 — Playbooks

Los playbooks traducen escenarios recurrentes en pasos de investigación, contención y recuperación, con decisiones y límites explícitos. El problema aparece cuando la automatización ejecuta una contención destructiva sin revisión o rollback. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M5.1-K07.md) (436 palabras de borrador, no ensayo final).

### M5.1-K08 — Cadena de Mando

La cadena de mando en crisis define quién decide, quién ejecuta, quién informa y cómo se resuelven conflictos bajo presión temporal. El problema aparece cuando la respuesta se demora por disputas de autoridad o decisiones contradictorias. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M5.1-K08.md) (445 palabras de borrador, no ensayo final).

### M5.1-K09 — RTO/RPO

RTO y RPO expresan objetivos de recuperación temporal y pérdida de datos tolerable que deben derivarse de necesidades del negocio y probarse. El problema aparece cuando se establecen valores aspiracionales sin arquitectura, presupuesto ni pruebas que los sostengan. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M5.1-K09.md) (447 palabras de borrador, no ensayo final).

### M5.1-K10 — Alineación BCDR

Alinear respuesta, continuidad y recuperación evita que la contención de un incidente comprometa la restauración o la operación degradada. El problema aparece cuando el equipo de seguridad aísla recursos críticos sin coordinar con continuidad y negocio. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M5.1-K10.md) (446 palabras de borrador, no ensayo final).

## Ampliaciones Atlas de esta unidad: tesis para discutir, no definiciones aprobadas

- **[AMP-43 — Tabletop de incidentes con agentes](../../02_conceptos/02_ampliaciones_atlas/AMP-43.md) [P].** Ejercitar incidentes donde un agente es víctima o vector revela vacíos de autoridad, evidencia y contención antes de que ocurran. Vínculo propuesto: `M5.1-K06`; fuente `06Ensayos!I327`.
- **[AMP-44 — Kill switch y escalamiento](../../02_conceptos/02_ampliaciones_atlas/AMP-44.md) [P].** Todo agente con capacidad de acción necesita un mecanismo probado para detenerlo y una ruta de escalamiento con autoridad clara. Vínculo propuesto: `HC-010`; fuente `06Ensayos!I328`.

## Conceptos híbridos candidatos que conectan esta unidad

- [HC-007 — Resiliencia gobernada por impacto](../../02_conceptos/03_hibridos_candidatos/HC-007.md): conecta `M5.1-K02`, `G4.2-K02`, `M6.1-K01`, `M6.1-K05`. **Candidato**, no unidad ni arista aprobada.
- [HC-020 — Respuesta y comunicación bajo incertidumbre](../../02_conceptos/03_hibridos_candidatos/HC-020.md): conecta `M5.1-K05`, `M5.2-K06`, `G6.1-K08`, `M5.2-K09`. **Candidato**, no unidad ni arista aprobada.
- [HC-022 — Gobierno de crisis multidisciplinario](../../02_conceptos/03_hibridos_candidatos/HC-022.md): conecta `G4.1-K08`, `M5.1-K08`, `M6.1-K09`, `G6.1-K09`. **Candidato**, no unidad ni arista aprobada.
- [HC-025 — Competencias y resiliencia organizacional](../../02_conceptos/03_hibridos_candidatos/HC-025.md): conecta `M1.2-K07`, `M1.2-K08`, `M5.1-K04`, `M6.1-K03`. **Candidato**, no unidad ni arista aprobada.
- [HC-030 — Seguridad industrial y continuidad de negocio](../../02_conceptos/03_hibridos_candidatos/HC-030.md): conecta `M6.2-K05`, `M3.1-K07`, `M5.1-K02`, `M6.1-K05`. **Candidato**, no unidad ni arista aprobada.
- [HC-037 — Alineación entre competencias y decisiones](../../02_conceptos/03_hibridos_candidatos/HC-037.md): conecta `G1.1-K03`, `M1.2-K05`, `M1.2-K09`, `M5.1-K06`. **Candidato**, no unidad ni arista aprobada.
- [HC-039 — Riesgo cibernético como narrativa empresarial](../../02_conceptos/03_hibridos_candidatos/HC-039.md): conecta `G1.2-K09`, `M5.1-K02`, `G6.1-K04`, `G5.1-K03`. **Candidato**, no unidad ni arista aprobada.

## Puente con TheMetaCognitiveCISO

Se propone entrenar la lente cognitiva `DP-0098` junto a las decisiones de `M5.1`. Esta es una **relación pedagógica derivada**, no una equivalencia canónica con el GM-24. Consulte [la caja cognitiva del CISO](../../../Biblioteca_CISO_Frontera/Caja_Cognitiva_CISO_72/00_Indice.md) para la ficha y su evidencia.

## Laboratorio: ocho modalidades de ejercicio

Las tareas comparten el mismo caso; no son ocho horas añadidas por separado. Se practican en la asignación indicativa de 3 h de seminario, 8 h de investigación y lectura, 12 h de laboratorio y 8 h de aplicación por unidad. Los tiempos requieren aprobación académica.

### 1. Comprensión conceptual

**Consigna:** Define `M5.1-K01` (IRP (Plan Respuesta)) y `M5.1-K02` (BIA (Impacto Negocio)) con tus palabras. Señala una frontera de responsabilidad, una confusión habitual y cómo la ampliación `AMP-44` altera la interpretación del caso «En un tabletop de ransomware, un agente comprometido intenta aislar servidores de respaldo durante una restauración crítica.».

**Producto:** cuadro de contraste con dos decisiones distintas y citas a las fichas.

**Comprobación:** No declara como sinónimos dos títulos vecinos ni toma la tesis [P] como definición aprobada.

### 2. Relaciones y contextualización

**Consigna:** Dibuja la cadena de decisiones entre `M5.1-K01`, `M5.1-K02`, `AMP-44` y `HC-022` — Gobierno de crisis multidisciplinario. Anota en cada conexión dirección, evidencia textual, posible solapamiento y qué cambiaría al variar el contexto de negocio. Las aristas nuevas son hipótesis hasta que se validen.

**Producto:** mapa de relaciones G–M y tabla de procedencia de cada enlace.

**Comprobación:** No transforma cercanía temática en causalidad ni convierte HC en requisito aprobado.

### 3. Práctica aplicada

**Consigna:** Trabaja en «En un tabletop de ransomware, un agente comprometido intenta aislar servidores de respaldo durante una restauración crítica.». Con BIA, plan IRP, inventario de permisos, datos de prueba y criterios de severidad, construye guion de tabletop con injects, decisiones por minuto y matriz de autoridad; incluye propietario, condiciones de entrada y salida, hipótesis adversa y prueba de funcionamiento.

**Producto:** guion de tabletop con injects, decisiones por minuto y matriz de autoridad.

**Comprobación:** El mecanismo de detención se demuestra en ejercicio y preserva registros para investigación.

### 4. Investigación y fuentes

**Consigna:** Investiga esta pregunta acotada: comprobar qué dependencia tiene el plan de respuesta respecto de continuidad y recuperación. Localiza al menos dos fuentes primarias con fecha y versión; distingue obligación, recomendación, definición, ejemplo y opinión.

**Producto:** ficha de fuentes con extractos breves, localizador y discrepancias.

**Comprobación:** No cita un borrador editorial o mapeo informativo como norma obligatoria.

### 5. Orquestación de actores y agentes

**Consigna:** Con CSIRT, negocio, continuidad, proveedores y junta, construye un flujo de tres hitos para «Diseñar mando de incidentes, RTO/RPO, reglas de kill switch y escalamiento.». Define qué puede proponer un agente, qué requiere aprobación humana, quién responde y cómo detener, registrar y revertir una acción errónea.

**Producto:** RACI/DACI, diagrama de traspasos y plan de supervisión.

**Comprobación:** Hay autoridad, trazas y camino de escalamiento para cada acción de alto impacto.

### 6. Análisis y contrafactual

**Consigna:** Compara «Mantener al agente para conservar velocidad frente a suspender su autonomía y operar en modo degradado.» usando datos de BIA, plan IRP, inventario de permisos, datos de prueba y criterios de severidad. Contrasta la primera impresión con la lente cognitiva `DP-0098` del programa metacognitivo; plantea qué evidencia falsaría cada hipótesis y un efecto de segundo orden.

**Producto:** matriz de alternativas, incertidumbres y pruebas refutatorias.

**Comprobación:** La comparación conserva supuestos, costos de reversión y consecuencias no observadas.

### 7. Toma de decisiones

**Consigna:** Redacta para el responsable competente una recomendación sobre «Diseñar mando de incidentes, RTO/RPO, reglas de kill switch y escalamiento.», con dos opciones, beneficio, riesgo residual, autoridad de aceptación, indicador temprano y condición explícita de pausa o rollback.

**Producto:** memorando ejecutivo de una página más expediente de evidencia.

**Comprobación:** El mecanismo de detención se demuestra en ejercicio y preserva registros para investigación.

### 8. Exposición y defensa

**Consigna:** Defiende la decisión ante CSIRT, negocio, continuidad, proveedores y junta en siete minutos; reserva tres para objeciones. Un par cambia un dato del escenario a mitad de la exposición: revisa la postura sin ocultar el supuesto que deja de sostenerse.

**Producto:** presentación oral, preguntas difíciles y registro de revisiones.

**Comprobación:** La defensa distingue certeza, incertidumbre, decisión y propiedad del riesgo.

## Rúbrica formativa y evidencia de logro

| Criterio | 0 — insuficiente | 2 — parcial | 4 — sólido |
|---|---|---|---|
| Precisión | Confunde conceptos, categorías o estados editoriales | Explica definiciones sin límites | Distingue base, propuesta y candidato; explica límites y relaciones sin equivalencias ficticias |
| Evidencia | Cita sin procedencia ni prueba | Traza fuentes pero no su calidad | Localiza fuente, versión, modalidad, incertidumbre y prueba de eficacia |
| Decisión y autoridad | No compara opciones ni propietario | Compara pero sin residual o escalamiento | Justifica alternativas, derecho de decisión, residual, parada y revisión |
| Transferencia | Entrega teórica sin caso | Caso parcial sin contraprueba | Artefacto operable, prueba adversa y defensa ajustada a la audiencia |

**Condición crítica de esta unidad:** El mecanismo de detención se demuestra en ejercicio y preserva registros para investigación. La práctica se devuelve para revisión si incumple este criterio, aunque el promedio sea alto. Para aprendizaje se propone al menos 3/4 en cada dimensión; no es una acreditación aprobada.

## Preguntas mayéuticas, sin confundirlas con afirmaciones

**Pregunta original consolidada (muestras):**
- `PC-067`: ¿Tenemos un plan de respuesta a incidentes vigente y ensayado con la dirección, legal, comunicación y proveedores? (vínculo `M5.1-K01`).
- `PC-073`: ¿Cuáles son nuestras funciones críticas de negocio, sus tolerancias de interrupción y sus dependencias tecnológicas y de terceros? (vínculo `M5.1-K02`).
- `PC-078`: ¿Cuándo fue el último ejercicio de crisis con el comité ejecutivo y qué cambió como resultado? (vínculo `M5.1-K06`).
- `PC-158`: ¿Podemos suspender, aislar o revocar un agente, o todos los de una clase, en minutos, y lo hemos ensayado? (vínculo `AMP-44`).
- `PC-159`: ¿Qué límites operativos (presupuesto, cantidad de llamadas, montos, frecuencia, alcance) actúan como cortacircuitos ante comportamientos anómalos o en cascada? (vínculo `AMP-44`).
- `PC-161`: ¿Cuál es nuestro presupuesto de tiempo de contención para un agente comprometido, y es menor que el tiempo en que el daño se vuelve material? (vínculo `AMP-44`).

**Serie de banco construida desde plantillas documentadas (muestras):**
- `BM-0601` — ¿Qué problema de gobierno, riesgo o capacidad intenta resolver realmente «IRP (Plan Respuesta)», y qué decisión debería mejorar si se comprende correctamente?
- `BM-0602` — ¿Qué supuesto habitual sobre «IRP (Plan Respuesta)» podría ser falso o incompleto, y qué consecuencia tendría diseñar la seguridad como si fuera cierto?
- `BM-0604` — ¿Qué problema de gobierno, riesgo o capacidad intenta resolver realmente «BIA (Impacto Negocio)», y qué decisión debería mejorar si se comprende correctamente?
- `BM-0605` — ¿Qué supuesto habitual sobre «BIA (Impacto Negocio)» podría ser falso o incompleto, y qué consecuencia tendría diseñar la seguridad como si fuera cierto?
- `BM-1049` — ¿Qué problema de gobierno, riesgo o capacidad intenta resolver realmente «Tabletop de incidentes con agentes», y qué decisión debería mejorar si se comprende correctamente?
- `BM-1050` — ¿Qué supuesto habitual sobre «Tabletop de incidentes con agentes» podría ser falso o incompleto, y qué consecuencia tendría diseñar la seguridad como si fuera cierto?

**Tesis propuestas por pregunta asignadas explícitamente a esta unidad: 8.**
- [APC-159 — Límites operativos como cortacircuitos para agentes](../../03_metodo_mayeutico/01_tesis_derivadas/APC-159.md) ← `PC-159`
- [APC-161 — Presupuesto de tiempo de contención de agentes comprometidos](../../03_metodo_mayeutico/01_tesis_derivadas/APC-161.md) ← `PC-161`
- [APC-174 — Playbooks de respuesta a incidentes de IA y agentes](../../03_metodo_mayeutico/01_tesis_derivadas/APC-174.md) ← `PC-174`
- [APC-178 — Umbral de declaración y notificación de incidentes de IA](../../03_metodo_mayeutico/01_tesis_derivadas/APC-178.md) ← `PC-178`
- [APC-243 — Taxonomía de incidentes con IA como herramienta u objetivo](../../03_metodo_mayeutico/01_tesis_derivadas/APC-243.md) ← `PC-243`
- [APA-006 — Preparación del directorio para decidir en una crisis cibernética](../../03_metodo_mayeutico/01_tesis_derivadas/APA-006.md) ← `PA-006`
- [APA-067 — Plazos de detección, clasificación y notificación de incidentes graves](../../03_metodo_mayeutico/01_tesis_derivadas/APA-067.md) ← `PA-067`
- [APA-144 — Trazabilidad de incidentes de IA hasta los cambios adoptados](../../03_metodo_mayeutico/01_tesis_derivadas/APA-144.md) ← `PA-144`

**Tesis transversales relacionadas sin asignación principal (muestras):**
- [APC-097](../../03_metodo_mayeutico/01_tesis_derivadas/APC-097.md) (relación transversal, no asignación principal)
- [APC-244](../../03_metodo_mayeutico/01_tesis_derivadas/APC-244.md) (relación transversal, no asignación principal)
- [APA-145](../../03_metodo_mayeutico/01_tesis_derivadas/APA-145.md) (relación transversal, no asignación principal)

El banco completo conserva 543 preguntas originales y 2.395 preguntas derivadas mecánicamente de plantillas; 308 tesis AP forman un **anexo provisional**, distinto de los 331 conceptos del corpus de trabajo.

## Lecturas, investigación y modalidad

**Lecturas internas verificables:**
- [Documento Maestro](../../../Curado02/01_noviembre_2026/src-thenextciso-gm-24-documento-maestro__9b8c53df319d.md), unidad `M5.1` desde línea 884.
- [lote de ideas base](../../../Curado02/01_noviembre_2026/src-thenextciso-gm-24-ensayos-base-181210__69cc0f303c88.md)
- Las 51 tesis Atlas [P] proceden de `06Ensayos!I285:I335` en [matriz de pre-ensayos](../../../Curado02/01_noviembre_2026/src-ai-ciso-atlas-ensayos-thenextciso-x-core-accountabilities-fy27-2026-11-05__5528a05eb5dd.xlsx).

**Lecturas complementarias por cotejar:** NIST CSF 2.0, NIST RMF y dominios CISM/CRISC según la unidad y las fuentes listadas por el Documento Maestro. El mapeo de este documento es una propuesta temática: `CISM C4; CRISC R1,R2; NIST CSF 2.0 RS.MA,GV.RR,ID.AM; NIST RMF Prepare,Monitor.`. La fuente oficial, edición y pertinencia deben comprobarse al preparar cada clase; no se presume cobertura íntegra de examen o norma.

**Recursos audiovisuales:** no se identificó un video específico, vigente y verificable por unidad en los documentos base. Existe un [inventario complementario de enlaces observados](../../../Biblioteca_CISO_Frontera/Consolidado_2026_MM_2026-11-11/03_programa_1200h/Videos_Observados_en_Fuentes.md), aún sin comprobación de contenido, disponibilidad, duración ni correspondencia con esta unidad. El equipo docente deberá seleccionarlos, comprobar derechos y documentar el vínculo antes de asignarlos.

**Carga de diseño:** 31 h por unidad; 24 unidades más capstone integrador de 56 h = escenario de 800 h. No es acreditación.

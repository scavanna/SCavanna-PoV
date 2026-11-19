<!-- generado-gm24 sha256:7da42ec8a7e7bf26cd4760a8ac5fce5ed4e4fdd6acb5966e43ebb6e135895342 -->
# M5.2 — Ejecución, Post-Mortem y Comunicación

**Pilar:** Gestión · **Eje:** Respuesta a incidentes y crisis · **Atlas:** `D15` (alineación editorial, no identidad de dominio).

**Pregunta rectora de fuente:** ¿Cómo puede un CISO diseñar, ejecutar y verificar ejecución, post-mortem y comunicación sin perder de vista el riesgo empresarial, las responsabilidades y la evidencia?

**Alcance:** diez conceptos base con idea central desarrollada; 2 ampliaciones Atlas cuyo título pertenece al Documento Maestro y cuya tesis es propuesta [P]. Los puentes HC relacionados son candidatos transversales; ninguna extensión altera por sí sola el número de unidades.

## Situación longitudinal y decisión

**Organización ficticia:** Tras contener un agente, faltan trazas sobre la secuencia de herramientas invocadas y se debate notificar una brecha.

**Decisión a sostener:** Reconstruir hechos, preservar evidencia, resolver contención y escalar decisiones de notificación.

**Cursos de acción en tensión:** Restaurar de inmediato y perder registros frente a conservar trazas y recuperar por fases.

**Información inicial:** línea temporal, logs de agentes, cadena de custodia y evaluación de impacto

**Interesados:** forense, legal, continuidad y portavoces

**Producto acumulativo:** expediente de incidente con incertidumbre, autorizaciones y lecciones verificables

**Regla de seguridad y responsabilidad:** No se declara erradicación completa ni ausencia de exfiltración sin evidencia proporcionada.

## Desarrollo de los diez conceptos base

### M5.2-K01 — Contención

La contención limita propagación y consecuencias de un incidente con decisiones proporcionales, reversibles cuando sea posible y coordinadas con negocio. El escenario que conviene examinar es el siguiente: aislar un servicio detiene al adversario pero interrumpe una operación crítica. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M5.2-K01.md) (438 palabras de borrador, no ensayo final).

### M5.2-K02 — Erradicación

La erradicación elimina persistencia y causas explotables después de preservar evidencia y comprender el alcance suficiente del incidente. El escenario que conviene examinar es el siguiente: se reinstala un servidor sin corregir credenciales comprometidas. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M5.2-K02.md) (431 palabras de borrador, no ensayo final).

### M5.2-K03 — Recuperación

La recuperación tras incidentes restaura servicios confiables y datos íntegros mediante criterios de retorno seguro, no solo encendido de sistemas. El escenario que conviene examinar es el siguiente: un backup restaura malware o permisos comprometidos. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M5.2-K03.md) (433 palabras de borrador, no ensayo final).

### M5.2-K04 — Comunicación Crisis

La comunicación de crisis coordina hechos, incertidumbres, audiencias, tiempos y autoridad para evitar mensajes contradictorios. El escenario que conviene examinar es el siguiente: un portavoz anuncia causa e impacto antes de validarlos. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M5.2-K04.md) (432 palabras de borrador, no ensayo final).

### M5.2-K05 — Post-Mortem

El post-mortem identifica fallas sistémicas y decisiones mejorables sin reducir el aprendizaje a asignar culpas individuales. El escenario que conviene examinar es el siguiente: el cierre del incidente no modifica controles ni procesos. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M5.2-K05.md) (434 palabras de borrador, no ensayo final).

### M5.2-K06 — Forense Digital

La forense digital preserva y analiza evidencia de manera íntegra, contextual y trazable para reconstruir hechos y apoyar decisiones. El escenario que conviene examinar es el siguiente: se alteran registros al responder sin cadena de custodia. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M5.2-K06.md) (436 palabras de borrador, no ensayo final).

### M5.2-K07 — Triaje

El triaje prioriza señales e incidentes potenciales según evidencia, impacto, urgencia y recursos, evitando equiparar alerta con confirmación. El escenario que conviene examinar es el siguiente: un volumen de alertas consume la capacidad de respuesta sin criterios claros. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M5.2-K07.md) (435 palabras de borrador, no ensayo final).

### M5.2-K08 — Gestión Narrativa

La gestión narrativa en crisis busca coherencia y transparencia responsable entre hechos conocidos, hipótesis y compromisos de comunicación. El escenario que conviene examinar es el siguiente: la organización promete certeza para controlar reputación y luego debe retractarse. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M5.2-K08.md) (437 palabras de borrador, no ensayo final).

### M5.2-K09 — Notificación Brechas

La notificación de brechas depende de obligaciones, materialidad, plazos y hechos verificados, en coordinación con Legal y Privacidad. El escenario que conviene examinar es el siguiente: un equipo comunica demasiado tarde o afirma incumplimiento sin evaluación competente. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M5.2-K09.md) (438 palabras de borrador, no ensayo final).

### M5.2-K10 — Resiliencia Adaptativa

La resiliencia adaptativa convierte incidentes en cambios de diseño, operación y gobierno para responder mejor a amenazas futuras. El escenario que conviene examinar es el siguiente: se restablece servicio pero persisten dependencias frágiles. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M5.2-K10.md) (434 palabras de borrador, no ensayo final).

## Ampliaciones Atlas de esta unidad: tesis para discutir, no definiciones aprobadas

- **[AMP-45 — Forense de agentes](../../02_conceptos/02_ampliaciones_atlas/AMP-45.md) [P].** Investigar un incidente con agentes exige reconstruir instrucciones, herramientas invocadas, datos accedidos y decisiones; sin telemetría de agentes no hay forense. Vínculo propuesto: `M5.2-K06`; fuente `06Ensayos!I329`.
- **[AMP-46 — Trazabilidad de decisiones autónomas](../../02_conceptos/02_ampliaciones_atlas/AMP-46.md) [P].** Registrar qué vio, qué decidió y con qué autoridad actuó un sistema autónomo es condición de rendición de cuentas y de mejora. Vínculo propuesto: `HC-012`; fuente `06Ensayos!I330`.

## Conceptos híbridos candidatos que conectan esta unidad

- [HC-019 — SOC agéntico con supervisión humana](../../02_conceptos/03_hibridos_candidatos/HC-019.md): conecta `M4.1-K06`, `M4.1-K05`, `M4.1-K08`, `M5.2-K01`. **Candidato**, no unidad ni arista aprobada.
- [HC-020 — Respuesta y comunicación bajo incertidumbre](../../02_conceptos/03_hibridos_candidatos/HC-020.md): conecta `M5.1-K05`, `M5.2-K06`, `G6.1-K08`, `M5.2-K09`. **Candidato**, no unidad ni arista aprobada.
- [HC-021 — Recuperación como prueba de confianza](../../02_conceptos/03_hibridos_candidatos/HC-021.md): conecta `M6.1-K02`, `M6.1-K06`, `M5.2-K03`, `G6.2-K08`. **Candidato**, no unidad ni arista aprobada.
- [HC-035 — Aprendizaje desde incidentes hasta políticas](../../02_conceptos/03_hibridos_candidatos/HC-035.md): conecta `M5.2-K05`, `M1.1-K10`, `G2.2-K07`, `G1.2-K01`. **Candidato**, no unidad ni arista aprobada.

## Puente con TheMetaCognitiveCISO

Se propone entrenar la lente cognitiva `EF-0011` junto a las decisiones de `M5.2`. Esta es una **relación pedagógica derivada**, no una equivalencia canónica con el GM-24. Consulte [la caja cognitiva del CISO](../../../Biblioteca_CISO_Frontera/Caja_Cognitiva_CISO_72/00_Indice.md) para la ficha y su evidencia.

## Laboratorio: ocho modalidades de ejercicio

Las tareas comparten el mismo caso; no son ocho horas añadidas por separado. Se practican en la asignación indicativa de 3 h de seminario, 8 h de investigación y lectura, 12 h de laboratorio y 8 h de aplicación por unidad. Los tiempos requieren aprobación académica.

### 1. Comprensión conceptual

**Consigna:** Define `M5.2-K01` (Contención) y `M5.2-K06` (Forense Digital) con tus palabras. Señala una frontera de responsabilidad, una confusión habitual y cómo la ampliación `AMP-45` altera la interpretación del caso «Tras contener un agente, faltan trazas sobre la secuencia de herramientas invocadas y se debate notificar una brecha.».

**Producto:** cuadro de contraste con dos decisiones distintas y citas a las fichas.

**Comprobación:** No declara como sinónimos dos títulos vecinos ni toma la tesis [P] como definición aprobada.

### 2. Relaciones y contextualización

**Consigna:** Dibuja la cadena de decisiones entre `M5.2-K01`, `M5.2-K06`, `AMP-45` y `HC-020` — Respuesta y comunicación bajo incertidumbre. Anota en cada conexión dirección, evidencia textual, posible solapamiento y qué cambiaría al variar el contexto de negocio. Las aristas nuevas son hipótesis hasta que se validen.

**Producto:** mapa de relaciones G–M y tabla de procedencia de cada enlace.

**Comprobación:** No transforma cercanía temática en causalidad ni convierte HC en requisito aprobado.

### 3. Práctica aplicada

**Consigna:** Trabaja en «Tras contener un agente, faltan trazas sobre la secuencia de herramientas invocadas y se debate notificar una brecha.». Con línea temporal, logs de agentes, cadena de custodia y evaluación de impacto, construye expediente de incidente con incertidumbre, autorizaciones y lecciones verificables; incluye propietario, condiciones de entrada y salida, hipótesis adversa y prueba de funcionamiento.

**Producto:** expediente de incidente con incertidumbre, autorizaciones y lecciones verificables.

**Comprobación:** No se declara erradicación completa ni ausencia de exfiltración sin evidencia proporcionada.

### 4. Investigación y fuentes

**Consigna:** Investiga esta pregunta acotada: contrastar deberes de notificación por jurisdicción con hallazgos observados y asesoría legal. Localiza al menos dos fuentes primarias con fecha y versión; distingue obligación, recomendación, definición, ejemplo y opinión.

**Producto:** ficha de fuentes con extractos breves, localizador y discrepancias.

**Comprobación:** No cita un borrador editorial o mapeo informativo como norma obligatoria.

### 5. Orquestación de actores y agentes

**Consigna:** Con forense, legal, continuidad y portavoces, construye un flujo de tres hitos para «Reconstruir hechos, preservar evidencia, resolver contención y escalar decisiones de notificación.». Define qué puede proponer un agente, qué requiere aprobación humana, quién responde y cómo detener, registrar y revertir una acción errónea.

**Producto:** RACI/DACI, diagrama de traspasos y plan de supervisión.

**Comprobación:** Hay autoridad, trazas y camino de escalamiento para cada acción de alto impacto.

### 6. Análisis y contrafactual

**Consigna:** Compara «Restaurar de inmediato y perder registros frente a conservar trazas y recuperar por fases.» usando datos de línea temporal, logs de agentes, cadena de custodia y evaluación de impacto. Contrasta la primera impresión con la lente cognitiva `EF-0011` del programa metacognitivo; plantea qué evidencia falsaría cada hipótesis y un efecto de segundo orden.

**Producto:** matriz de alternativas, incertidumbres y pruebas refutatorias.

**Comprobación:** La comparación conserva supuestos, costos de reversión y consecuencias no observadas.

### 7. Toma de decisiones

**Consigna:** Redacta para el responsable competente una recomendación sobre «Reconstruir hechos, preservar evidencia, resolver contención y escalar decisiones de notificación.», con dos opciones, beneficio, riesgo residual, autoridad de aceptación, indicador temprano y condición explícita de pausa o rollback.

**Producto:** memorando ejecutivo de una página más expediente de evidencia.

**Comprobación:** No se declara erradicación completa ni ausencia de exfiltración sin evidencia proporcionada.

### 8. Exposición y defensa

**Consigna:** Defiende la decisión ante forense, legal, continuidad y portavoces en siete minutos; reserva tres para objeciones. Un par cambia un dato del escenario a mitad de la exposición: revisa la postura sin ocultar el supuesto que deja de sostenerse.

**Producto:** presentación oral, preguntas difíciles y registro de revisiones.

**Comprobación:** La defensa distingue certeza, incertidumbre, decisión y propiedad del riesgo.

## Rúbrica formativa y evidencia de logro

| Criterio | 0 — insuficiente | 2 — parcial | 4 — sólido |
|---|---|---|---|
| Precisión | Confunde conceptos, categorías o estados editoriales | Explica definiciones sin límites | Distingue base, propuesta y candidato; explica límites y relaciones sin equivalencias ficticias |
| Evidencia | Cita sin procedencia ni prueba | Traza fuentes pero no su calidad | Localiza fuente, versión, modalidad, incertidumbre y prueba de eficacia |
| Decisión y autoridad | No compara opciones ni propietario | Compara pero sin residual o escalamiento | Justifica alternativas, derecho de decisión, residual, parada y revisión |
| Transferencia | Entrega teórica sin caso | Caso parcial sin contraprueba | Artefacto operable, prueba adversa y defensa ajustada a la audiencia |

**Condición crítica de esta unidad:** No se declara erradicación completa ni ausencia de exfiltración sin evidencia proporcionada. La práctica se devuelve para revisión si incumple este criterio, aunque el promedio sea alto. Para aprendizaje se propone al menos 3/4 en cada dimensión; no es una acreditación aprobada.

## Preguntas mayéuticas, sin confundirlas con afirmaciones

**Pregunta original consolidada (muestras):**
- `PC-072`: ¿Hemos definido cómo interactuamos con los CERT nacionales, reguladores, fuerzas de seguridad y pares sectoriales durante un incidente? (vínculo `M5.2-K04`).
- `PC-140`: ¿Retenemos, auditamos y podemos buscar los prompts, respuestas y acciones de la IA según nuestras obligaciones legales? (vínculo `AMP-46`).
- `PC-172`: ¿Registramos de forma correlacionable quién pidió qué, qué hizo el agente, con qué identidad, herramientas y datos, sin depender del razonamiento interno del modelo? (vínculo `AMP-46`).
- `PC-175`: ¿Podemos reconstruir de forma forense una cadena de acciones de varios agentes y herramientas con evidencia válida? (vínculo `AMP-45`).
- `PA-015`: ¿Qué tenemos que divulgar sobre ciberseguridad y cómo se decide si un incidente es material? (vínculo `M5.2-K09`).
- `PA-018`: Si un regulador o un tribunal lo pide, ¿podemos explicar y reconstruir una decisión tomada o asistida por la IA? (vínculo `AMP-46`).

**Serie de banco construida desde plantillas documentadas (muestras):**
- `BM-0631` — ¿Qué problema de gobierno, riesgo o capacidad intenta resolver realmente «Contención», y qué decisión debería mejorar si se comprende correctamente?
- `BM-0632` — ¿Qué supuesto habitual sobre «Contención» podría ser falso o incompleto, y qué consecuencia tendría diseñar la seguridad como si fuera cierto?
- `BM-0634` — ¿Qué problema de gobierno, riesgo o capacidad intenta resolver realmente «Erradicación», y qué decisión debería mejorar si se comprende correctamente?
- `BM-0635` — ¿Qué supuesto habitual sobre «Erradicación» podría ser falso o incompleto, y qué consecuencia tendría diseñar la seguridad como si fuera cierto?
- `BM-1057` — ¿Qué problema de gobierno, riesgo o capacidad intenta resolver realmente «Forense de agentes», y qué decisión debería mejorar si se comprende correctamente?
- `BM-1058` — ¿Qué supuesto habitual sobre «Forense de agentes» podría ser falso o incompleto, y qué consecuencia tendría diseñar la seguridad como si fuera cierto?

**Tesis propuestas por pregunta asignadas explícitamente a esta unidad: 5.**
- [APC-072 — Coordinación con autoridades y pares sectoriales durante incidentes](../../03_metodo_mayeutico/01_tesis_derivadas/APC-072.md) ← `PC-072`
- [APC-140 — Retención, auditoría y búsqueda legal de interacciones con IA](../../03_metodo_mayeutico/01_tesis_derivadas/APC-140.md) ← `PC-140`
- [APA-015 — Determinación de materialidad y divulgación de incidentes cibernéticos](../../03_metodo_mayeutico/01_tesis_derivadas/APA-015.md) ← `PA-015`
- [APA-080 — Análisis de causa raíz de hallazgos recurrentes](../../03_metodo_mayeutico/01_tesis_derivadas/APA-080.md) ← `PA-080`
- [APA-087 — Compromiso de notificación de incidentes a clientes afectados](../../03_metodo_mayeutico/01_tesis_derivadas/APA-087.md) ← `PA-087`

**Tesis transversales relacionadas sin asignación principal (muestras):**
- [APC-179](../../03_metodo_mayeutico/01_tesis_derivadas/APC-179.md) (relación transversal, no asignación principal)
- [APC-192](../../03_metodo_mayeutico/01_tesis_derivadas/APC-192.md) (relación transversal, no asignación principal)
- [APC-203](../../03_metodo_mayeutico/01_tesis_derivadas/APC-203.md) (relación transversal, no asignación principal)
- [APA-104](../../03_metodo_mayeutico/01_tesis_derivadas/APA-104.md) (relación transversal, no asignación principal)

El banco completo conserva 543 preguntas originales y 2.395 preguntas derivadas mecánicamente de plantillas; 308 tesis AP forman un **anexo provisional**, distinto de los 331 conceptos del corpus de trabajo.

## Lecturas, investigación y modalidad

**Lecturas internas verificables:**
- [Documento Maestro](../../../Curado02/01_noviembre_2026/src-thenextciso-gm-24-documento-maestro__9b8c53df319d.md), unidad `M5.2` desde línea 925.
- [lote de ideas base](../../../Curado02/01_noviembre_2026/src-thenextciso-gm24-ensayos-bases-211-240__be3ff9fea8f4.md)
- Las 51 tesis Atlas [P] proceden de `06Ensayos!I285:I335` en [matriz de pre-ensayos](../../../Curado02/01_noviembre_2026/src-ai-ciso-atlas-ensayos-thenextciso-x-core-accountabilities-fy27-2026-11-05__5528a05eb5dd.xlsx).

**Lecturas complementarias por cotejar:** NIST CSF 2.0, NIST RMF y dominios CISM/CRISC según la unidad y las fuentes listadas por el Documento Maestro. El mapeo de este documento es una propuesta temática: `CISM C4; CRISC R3,R4; NIST CSF 2.0 RS.AN,RS.MI,RS.CO,RC.RP; NIST RMF Monitor.`. La fuente oficial, edición y pertinencia deben comprobarse al preparar cada clase; no se presume cobertura íntegra de examen o norma.

**Recursos audiovisuales:** no se identificó un video específico, vigente y verificable por unidad en los documentos base. Existe un [inventario complementario de enlaces observados](../../../Biblioteca_CISO_Frontera/Consolidado_2026_MM_2026-11-11/03_programa_1200h/Videos_Observados_en_Fuentes.md), aún sin comprobación de contenido, disponibilidad, duración ni correspondencia con esta unidad. El equipo docente deberá seleccionarlos, comprobar derechos y documentar el vínculo antes de asignarlos.

**Carga de diseño:** 31 h por unidad; 24 unidades más capstone integrador de 56 h = escenario de 800 h. No es acreditación.

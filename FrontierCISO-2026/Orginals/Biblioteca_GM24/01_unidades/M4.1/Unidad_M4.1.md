<!-- generado-gm24 sha256:2e54f4f031e5bf03e296c004e4f4f322e19ebc5fc281912dc0e9b3473640459a -->
# M4.1 — Operaciones de Seguridad, Monitorización e Inteligencia

**Pilar:** Gestión · **Eje:** Operaciones proactivas y amenazas · **Atlas:** `D14,D21` (alineación editorial, no identidad de dominio).

**Pregunta rectora de fuente:** ¿Cómo puede un CISO diseñar, ejecutar y verificar operaciones de seguridad, monitorización e inteligencia sin perder de vista el riesgo empresarial, las responsabilidades y la evidencia?

**Alcance:** diez conceptos base con idea central desarrollada; 2 ampliaciones Atlas cuyo título pertenece al Documento Maestro y cuya tesis es propuesta [P]. Los puentes HC relacionados son candidatos transversales; ninguna extensión altera por sí sola el número de unidades.

## Situación longitudinal y decisión

**Organización ficticia:** El agente de triage reduce tiempo de cierre, pero su justificación oculta señales de intrusión que el analista raramente cuestiona.

**Decisión a sostener:** Fijar qué triage se automatiza y cuándo la supervisión humana debe detenerlo.

**Cursos de acción en tensión:** Aceptar recomendaciones con un clic frente a doble lectura de casos de alto impacto y muestreo ciego.

**Información inicial:** telemetría SIEM, registros de decisiones, falsos negativos y flujo de escalamiento

**Interesados:** analistas, SOC manager, dueños de activos y comité de riesgo

**Producto acumulativo:** playbook SOC agéntico con medidas de calidad y control de overrides

**Regla de seguridad y responsabilidad:** No se usa el cierre de alertas como único indicador de calidad ni se asume supervisión efectiva por presencia humana nominal.

## Desarrollo de los diez conceptos base

### M4.1-K01 — SOC Moderno

Un SOC moderno integra personas, procesos, telemetría, detección, investigación y respuesta alrededor de escenarios de riesgo priorizados. El problema aparece cuando la organización invierte en un SIEM sin disponer de fuentes confiables, casos de uso ni responsabilidades claras. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M4.1-K01.md) (455 palabras de borrador, no ensayo final).

### M4.1-K02 — Monitorización Continua

La monitorización continua observa cambios relevantes en activos, amenazas y controles para apoyar decisiones oportunas. El problema aparece cuando se confunde el volumen de eventos recopilados con la capacidad real de identificar conductas adversas. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M4.1-K02.md) (449 palabras de borrador, no ensayo final).

### M4.1-K03 — Threat Intelligence (CTI)

La inteligencia de amenazas convierte datos sobre adversarios, capacidades, intenciones y TTP en conocimiento contextual que modifica prioridades defensivas. El problema aparece cuando una lista de indicadores externos se presenta como inteligencia relevante sin vincularla con activos o escenarios propios. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M4.1-K03.md) (453 palabras de borrador, no ensayo final).

### M4.1-K04 — SIEM

Un SIEM centraliza y correlaciona eventos de seguridad para producir señales investigables y evidencia de incidentes potenciales. El problema aparece cuando la ingestión indiscriminada eleva costos y ruido sin mejorar la capacidad de detectar amenazas relevantes. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M4.1-K04.md) (447 palabras de borrador, no ensayo final).

### M4.1-K05 — SOAR

SOAR orquesta flujos de investigación y respuesta repetibles, con decisiones automáticas acotadas y escalamiento humano cuando las consecuencias lo requieren. El problema aparece cuando un playbook automatizado bloquea identidades legítimas o destruye evidencia al actuar sin condiciones de seguridad. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M4.1-K05.md) (446 palabras de borrador, no ensayo final).

### M4.1-K06 — XDR

XDR correlaciona señales de diferentes superficies para enriquecer detección, investigación y respuesta sobre escenarios que atraviesan identidades, endpoints y aplicaciones. El problema aparece cuando una plataforma integrada se confunde con visibilidad completa cuando faltan sensores o cobertura de terceros. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M4.1-K06.md) (450 palabras de borrador, no ensayo final).

### M4.1-K07 — Threat Hunting

Threat hunting formula y contrasta hipótesis sobre actividad adversa que puede no haber disparado alertas existentes. El problema aparece cuando la actividad se mide por cantidad de consultas en lugar de hallazgos, mejoras de detección o reducción de incertidumbre. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M4.1-K07.md) (447 palabras de borrador, no ensayo final).

### M4.1-K08 — IA en SecOps

La IA aplicada a operaciones puede acelerar análisis y tareas repetitivas, pero necesita límites de autoridad, calidad de datos y evaluación de resultados. El problema aparece cuando un copiloto o agente resume alertas con seguridad aparente y propone acciones incorrectas sin revisión. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M4.1-K08.md) (455 palabras de borrador, no ensayo final).

### M4.1-K09 — Ciclo Vida Inteligencia

El ciclo de inteligencia transforma necesidades de decisión en requerimientos, recolección, procesamiento, análisis, difusión y retroalimentación. El problema aparece cuando los informes se producen por rutina sin verificar si respondieron preguntas del negocio o mejoraron controles. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M4.1-K09.md) (444 palabras de borrador, no ensayo final).

### M4.1-K10 — TTPs

Las tácticas, técnicas y procedimientos describen patrones de comportamiento adversario útiles para modelar amenazas, diseñar detecciones y probar defensas. El problema aparece cuando una técnica se convierte en alerta universal sin evaluar contexto, variantes o falsos positivos. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M4.1-K10.md) (444 palabras de borrador, no ensayo final).

## Ampliaciones Atlas de esta unidad: tesis para discutir, no definiciones aprobadas

- **[AMP-39 — SOC agéntico](../../02_conceptos/02_ampliaciones_atlas/AMP-39.md) [P].** El SOC agéntico redistribuye el trabajo: agentes que priorizan, investigan y proponen respuesta; personas que supervisan, ajustan y deciden, medidas por tiempo de respuesta y calidad. Vínculo propuesto: `HC-019`; fuente `06Ensayos!I323`.
- **[AMP-40 — Human-in-the-loop](../../02_conceptos/02_ampliaciones_atlas/AMP-40.md) [P].** Human-in-the-loop se define por riesgo: qué acciones requieren aprobación previa, cuáles se auditan después y cuáles nunca se delegan. Vínculo propuesto: `HC-019`; fuente `06Ensayos!I324`.

## Conceptos híbridos candidatos que conectan esta unidad

- [HC-001 — Gobierno de decisiones basadas en evidencia](../../02_conceptos/03_hibridos_candidatos/HC-001.md): conecta `G1.1-K01`, `G5.1-K03`, `G6.1-K05`, `M4.1-K02`. **Candidato**, no unidad ni arista aprobada.
- [HC-005 — Cumplimiento continuo orientado a resultados](../../02_conceptos/03_hibridos_candidatos/HC-005.md): conecta `G3.1-K01`, `G3.2-K02`, `M4.1-K02`, `M3.2-K04`. **Candidato**, no unidad ni arista aprobada.
- [HC-010 — Autonomía delegada y límites de acción](../../02_conceptos/03_hibridos_candidatos/HC-010.md): conecta `G4.2-K05`, `M2.2-K03`, `M3.1-K09`, `M4.1-K08`. **Candidato**, no unidad ni arista aprobada.
- [HC-012 — Confianza verificable en decisiones de IA](../../02_conceptos/03_hibridos_candidatos/HC-012.md): conecta `G6.2-K01`, `G6.2-K08`, `G3.2-K06`, `M4.1-K08`. **Candidato**, no unidad ni arista aprobada.
- [HC-017 — Inteligencia que modifica decisiones](../../02_conceptos/03_hibridos_candidatos/HC-017.md): conecta `G6.1-K02`, `M4.1-K03`, `M4.1-K09`, `G5.1-K07`. **Candidato**, no unidad ni arista aprobada.
- [HC-018 — Observabilidad y aseguramiento de controles](../../02_conceptos/03_hibridos_candidatos/HC-018.md): conecta `M4.1-K02`, `M3.2-K04`, `G3.2-K02`, `G6.1-K05`. **Candidato**, no unidad ni arista aprobada.
- [HC-019 — SOC agéntico con supervisión humana](../../02_conceptos/03_hibridos_candidatos/HC-019.md): conecta `M4.1-K06`, `M4.1-K05`, `M4.1-K08`, `M5.2-K01`. **Candidato**, no unidad ni arista aprobada.
- [HC-040 — Homeostasis organizacional de seguridad](../../02_conceptos/03_hibridos_candidatos/HC-040.md): conecta `G4.2-K02`, `M4.1-K02`, `G1.1-K05`, `M3.1-K10`. **Candidato**, no unidad ni arista aprobada.

## Puente con TheMetaCognitiveCISO

Se propone entrenar la lente cognitiva `EF-0012` junto a las decisiones de `M4.1`. Esta es una **relación pedagógica derivada**, no una equivalencia canónica con el GM-24. Consulte [la caja cognitiva del CISO](../../../Biblioteca_CISO_Frontera/Caja_Cognitiva_CISO_72/00_Indice.md) para la ficha y su evidencia.

## Laboratorio: ocho modalidades de ejercicio

Las tareas comparten el mismo caso; no son ocho horas añadidas por separado. Se practican en la asignación indicativa de 3 h de seminario, 8 h de investigación y lectura, 12 h de laboratorio y 8 h de aplicación por unidad. Los tiempos requieren aprobación académica.

### 1. Comprensión conceptual

**Consigna:** Define `M4.1-K01` (SOC Moderno) y `M4.1-K08` (IA en SecOps) con tus palabras. Señala una frontera de responsabilidad, una confusión habitual y cómo la ampliación `AMP-40` altera la interpretación del caso «El agente de triage reduce tiempo de cierre, pero su justificación oculta señales de intrusión que el analista raramente cuestiona.».

**Producto:** cuadro de contraste con dos decisiones distintas y citas a las fichas.

**Comprobación:** No declara como sinónimos dos títulos vecinos ni toma la tesis [P] como definición aprobada.

### 2. Relaciones y contextualización

**Consigna:** Dibuja la cadena de decisiones entre `M4.1-K01`, `M4.1-K08`, `AMP-40` y `HC-019` — SOC agéntico con supervisión humana. Anota en cada conexión dirección, evidencia textual, posible solapamiento y qué cambiaría al variar el contexto de negocio. Las aristas nuevas son hipótesis hasta que se validen.

**Producto:** mapa de relaciones G–M y tabla de procedencia de cada enlace.

**Comprobación:** No transforma cercanía temática en causalidad ni convierte HC en requisito aprobado.

### 3. Práctica aplicada

**Consigna:** Trabaja en «El agente de triage reduce tiempo de cierre, pero su justificación oculta señales de intrusión que el analista raramente cuestiona.». Con telemetría SIEM, registros de decisiones, falsos negativos y flujo de escalamiento, construye playbook SOC agéntico con medidas de calidad y control de overrides; incluye propietario, condiciones de entrada y salida, hipótesis adversa y prueba de funcionamiento.

**Producto:** playbook SOC agéntico con medidas de calidad y control de overrides.

**Comprobación:** No se usa el cierre de alertas como único indicador de calidad ni se asume supervisión efectiva por presencia humana nominal.

### 4. Investigación y fuentes

**Consigna:** Investiga esta pregunta acotada: comparar operaciones SIEM/SOAR/XDR y el efecto real de automatizar investigación. Localiza al menos dos fuentes primarias con fecha y versión; distingue obligación, recomendación, definición, ejemplo y opinión.

**Producto:** ficha de fuentes con extractos breves, localizador y discrepancias.

**Comprobación:** No cita un borrador editorial o mapeo informativo como norma obligatoria.

### 5. Orquestación de actores y agentes

**Consigna:** Con analistas, SOC manager, dueños de activos y comité de riesgo, construye un flujo de tres hitos para «Fijar qué triage se automatiza y cuándo la supervisión humana debe detenerlo.». Define qué puede proponer un agente, qué requiere aprobación humana, quién responde y cómo detener, registrar y revertir una acción errónea.

**Producto:** RACI/DACI, diagrama de traspasos y plan de supervisión.

**Comprobación:** Hay autoridad, trazas y camino de escalamiento para cada acción de alto impacto.

### 6. Análisis y contrafactual

**Consigna:** Compara «Aceptar recomendaciones con un clic frente a doble lectura de casos de alto impacto y muestreo ciego.» usando datos de telemetría SIEM, registros de decisiones, falsos negativos y flujo de escalamiento. Contrasta la primera impresión con la lente cognitiva `EF-0012` del programa metacognitivo; plantea qué evidencia falsaría cada hipótesis y un efecto de segundo orden.

**Producto:** matriz de alternativas, incertidumbres y pruebas refutatorias.

**Comprobación:** La comparación conserva supuestos, costos de reversión y consecuencias no observadas.

### 7. Toma de decisiones

**Consigna:** Redacta para el responsable competente una recomendación sobre «Fijar qué triage se automatiza y cuándo la supervisión humana debe detenerlo.», con dos opciones, beneficio, riesgo residual, autoridad de aceptación, indicador temprano y condición explícita de pausa o rollback.

**Producto:** memorando ejecutivo de una página más expediente de evidencia.

**Comprobación:** No se usa el cierre de alertas como único indicador de calidad ni se asume supervisión efectiva por presencia humana nominal.

### 8. Exposición y defensa

**Consigna:** Defiende la decisión ante analistas, SOC manager, dueños de activos y comité de riesgo en siete minutos; reserva tres para objeciones. Un par cambia un dato del escenario a mitad de la exposición: revisa la postura sin ocultar el supuesto que deja de sostenerse.

**Producto:** presentación oral, preguntas difíciles y registro de revisiones.

**Comprobación:** La defensa distingue certeza, incertidumbre, decisión y propiedad del riesgo.

## Rúbrica formativa y evidencia de logro

| Criterio | 0 — insuficiente | 2 — parcial | 4 — sólido |
|---|---|---|---|
| Precisión | Confunde conceptos, categorías o estados editoriales | Explica definiciones sin límites | Distingue base, propuesta y candidato; explica límites y relaciones sin equivalencias ficticias |
| Evidencia | Cita sin procedencia ni prueba | Traza fuentes pero no su calidad | Localiza fuente, versión, modalidad, incertidumbre y prueba de eficacia |
| Decisión y autoridad | No compara opciones ni propietario | Compara pero sin residual o escalamiento | Justifica alternativas, derecho de decisión, residual, parada y revisión |
| Transferencia | Entrega teórica sin caso | Caso parcial sin contraprueba | Artefacto operable, prueba adversa y defensa ajustada a la audiencia |

**Condición crítica de esta unidad:** No se usa el cierre de alertas como único indicador de calidad ni se asume supervisión efectiva por presencia humana nominal. La práctica se devuelve para revisión si incumple este criterio, aunque el promedio sea alto. Para aprendizaje se propone al menos 3/4 en cada dimensión; no es una acreditación aprobada.

## Preguntas mayéuticas, sin confundirlas con afirmaciones

**Pregunta original consolidada (muestras):**
- `PC-033`: ¿Cómo detectamos y respondemos al robo de tokens, sesiones y credenciales, y en cuánto tiempo revocamos un acceso comprometido? (vínculo `M4.1-K06`).
- `PC-064`: ¿Qué cobertura de telemetría tiene el SOC (identidad, endpoint, correo, nube, SaaS, datos, red, OT) y qué puntos ciegos aceptamos de forma consciente? (vínculo `M4.1-K02`).
- `PC-065`: ¿Cuáles son nuestros tiempos de detección, contención y recuperación para incidentes graves, y cómo evolucionan? (vínculo `M4.1-K01`).
- `PC-066`: ¿Qué acciones de contención están automatizadas, cuáles requieren aprobación humana y quién decide ese límite? (vínculo `M4.1-K05`).
- `PC-070`: ¿Qué retención y calidad de registros necesitamos para investigaciones forenses, obligaciones regulatorias y caza retrospectiva, y a qué costo? (vínculo `M4.1-K04`).
- `PC-071`: ¿Cómo está organizado el SOC (roles, niveles, turnos, servicios gestionados) y cómo cuidamos la carga y el desgaste del equipo? (vínculo `M4.1-K01`).

**Serie de banco construida desde plantillas documentadas (muestras):**
- `BM-0541` — ¿Qué problema de gobierno, riesgo o capacidad intenta resolver realmente «SOC Moderno», y qué decisión debería mejorar si se comprende correctamente?
- `BM-0542` — ¿Qué supuesto habitual sobre «SOC Moderno» podría ser falso o incompleto, y qué consecuencia tendría diseñar la seguridad como si fuera cierto?
- `BM-0544` — ¿Qué problema de gobierno, riesgo o capacidad intenta resolver realmente «Monitorización Continua», y qué decisión debería mejorar si se comprende correctamente?
- `BM-0545` — ¿Qué supuesto habitual sobre «Monitorización Continua» podría ser falso o incompleto, y qué consecuencia tendría diseñar la seguridad como si fuera cierto?
- `BM-1033` — ¿Qué problema de gobierno, riesgo o capacidad intenta resolver realmente «SOC agéntico», y qué decisión debería mejorar si se comprende correctamente?
- `BM-1034` — ¿Qué supuesto habitual sobre «SOC agéntico» podría ser falso o incompleto, y qué consecuencia tendría diseñar la seguridad como si fuera cierto?

**Tesis propuestas por pregunta asignadas explícitamente a esta unidad: 12.**
- [APC-033 — Detección y revocación ante robo de tokens y sesiones](../../03_metodo_mayeutico/01_tesis_derivadas/APC-033.md) ← `PC-033`
- [APC-065 — Medición de tiempos de detección, contención y recuperación](../../03_metodo_mayeutico/01_tesis_derivadas/APC-065.md) ← `PC-065`
- [APC-066 — Límite entre contención automatizada y aprobación humana](../../03_metodo_mayeutico/01_tesis_derivadas/APC-066.md) ← `PC-066`
- [APC-070 — Retención y calidad de registros para investigación y cumplimiento](../../03_metodo_mayeutico/01_tesis_derivadas/APC-070.md) ← `PC-070`
- [APC-177 — Vista unificada de señales de IA en el SOC](../../03_metodo_mayeutico/01_tesis_derivadas/APC-177.md) ← `PC-177`
- [APC-191 — Criterios de paso a producción de agentes de seguridad](../../03_metodo_mayeutico/01_tesis_derivadas/APC-191.md) ← `PC-191`
- [APC-193 — Medición del aporte de IA al SOC con línea base](../../03_metodo_mayeutico/01_tesis_derivadas/APC-193.md) ← `PC-193`
- [APC-195 — Gestión de exposición asistida por IA con aprobación humana](../../03_metodo_mayeutico/01_tesis_derivadas/APC-195.md) ← `PC-195`

**Tesis transversales relacionadas sin asignación principal (muestras):**
- [APC-050](../../03_metodo_mayeutico/01_tesis_derivadas/APC-050.md) (relación transversal, no asignación principal)
- [APC-068](../../03_metodo_mayeutico/01_tesis_derivadas/APC-068.md) (relación transversal, no asignación principal)
- [APC-155](../../03_metodo_mayeutico/01_tesis_derivadas/APC-155.md) (relación transversal, no asignación principal)
- [APC-163](../../03_metodo_mayeutico/01_tesis_derivadas/APC-163.md) (relación transversal, no asignación principal)
- [APC-164](../../03_metodo_mayeutico/01_tesis_derivadas/APC-164.md) (relación transversal, no asignación principal)

El banco completo conserva 543 preguntas originales y 2.395 preguntas derivadas mecánicamente de plantillas; 308 tesis AP forman un **anexo provisional**, distinto de los 331 conceptos del corpus de trabajo.

## Lecturas, investigación y modalidad

**Lecturas internas verificables:**
- [Documento Maestro](../../../Curado02/01_noviembre_2026/src-thenextciso-gm-24-documento-maestro__9b8c53df319d.md), unidad `M4.1` desde línea 802.
- [lote de ideas base](../../../Curado02/01_noviembre_2026/src-thenextciso-gm-24-ensayos-base-181210__69cc0f303c88.md)
- Las 51 tesis Atlas [P] proceden de `06Ensayos!I285:I335` en [matriz de pre-ensayos](../../../Curado02/01_noviembre_2026/src-ai-ciso-atlas-ensayos-thenextciso-x-core-accountabilities-fy27-2026-11-05__5528a05eb5dd.xlsx).

**Lecturas complementarias por cotejar:** NIST CSF 2.0, NIST RMF y dominios CISM/CRISC según la unidad y las fuentes listadas por el Documento Maestro. El mapeo de este documento es una propuesta temática: `CISM C3,C4; CRISC R2,R4; NIST CSF 2.0 DE.CM,DE.AE,RS.MA; NIST RMF Monitor.`. La fuente oficial, edición y pertinencia deben comprobarse al preparar cada clase; no se presume cobertura íntegra de examen o norma.

**Recursos audiovisuales:** no se identificó un video específico, vigente y verificable por unidad en los documentos base. Existe un [inventario complementario de enlaces observados](../../../Biblioteca_CISO_Frontera/Consolidado_2026_MM_2026-11-11/03_programa_1200h/Videos_Observados_en_Fuentes.md), aún sin comprobación de contenido, disponibilidad, duración ni correspondencia con esta unidad. El equipo docente deberá seleccionarlos, comprobar derechos y documentar el vínculo antes de asignarlos.

**Carga de diseño:** 31 h por unidad; 24 unidades más capstone integrador de 56 h = escenario de 800 h. No es acreditación.

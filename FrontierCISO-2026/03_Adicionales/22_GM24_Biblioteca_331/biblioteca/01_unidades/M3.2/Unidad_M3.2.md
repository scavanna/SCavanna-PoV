<!-- generado-gm24 sha256:dd61d4fbe8c88cf05c519f921f1ac63870d008632c30abb5029f15754a53a902 -->
# M3.2 — Selección, Implementación y Evaluación de Controles

**Pilar:** Gestión · **Eje:** Arquitectura y controles técnicos · **Atlas:** `D13,D22` (alineación editorial, no identidad de dominio).

**Pregunta rectora de fuente:** ¿Cómo puede un CISO diseñar, ejecutar y verificar selección, implementación y evaluación de controles sin perder de vista el riesgo empresarial, las responsabilidades y la evidencia?

**Alcance:** diez conceptos base con idea central desarrollada; 2 ampliaciones Atlas cuyo título pertenece al Documento Maestro y cuya tesis es propuesta [P]. Los puentes HC relacionados son candidatos transversales; ninguna extensión altera por sí sola el número de unidades.

## Situación longitudinal y decisión

**Organización ficticia:** Un control autónomo contiene malware en laboratorio, pero un falso positivo en producción podría detener la facturación.

**Decisión a sostener:** Elegir controles, escenarios de prueba, límites de despliegue y compensaciones.

**Cursos de acción en tensión:** Activar bloqueo global frente a piloto por fases con rollback y test adversarial.

**Información inicial:** requisitos de control, casos de prueba, fallo simulado y POA&M

**Interesados:** QA, red team, ingeniería y propietario de facturación

**Producto acumulativo:** plan de aseguramiento con criterios de aceptación y reversión medibles

**Regla de seguridad y responsabilidad:** Un control configurado no se acredita como efectivo sin prueba independiente relevante.

## Desarrollo de los diez conceptos base

### M3.2-K01 — Controles de Seguridad

Un control de seguridad es una salvaguarda con propósito, condiciones y evidencia; no debe confundirse con el resultado que intenta producir. El escenario que conviene examinar es el siguiente: un producto se registra como control efectivo sin configuración ni pruebas. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M3.2-K01.md) (445 palabras de borrador, no ensayo final).

### M3.2-K02 — NIST SP 800-53

NIST SP 800-53 ofrece un catálogo de controles que requiere selección y adaptación según sistema, riesgo y obligaciones, no aplicación literal indiscriminada. El escenario que conviene examinar es el siguiente: se declara cumplimiento de una familia por haber comprado una plataforma. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M3.2-K02.md) (449 palabras de borrador, no ensayo final).

### M3.2-K03 — Selección y Adaptación

Seleccionar y adaptar controles exige evaluar aplicabilidad, costo, dependencias, riesgos y medidas compensatorias. El escenario que conviene examinar es el siguiente: un control estándar interrumpe operaciones industriales sin alternativa. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M3.2-K03.md) (433 palabras de borrador, no ensayo final).

### M3.2-K04 — Evaluación (Assess)

Evaluar controles implica comprobar diseño e implementación con procedimientos y evidencia suficientes para sostener conclusiones limitadas. El escenario que conviene examinar es el siguiente: un dashboard favorable sustituye pruebas de funcionamiento. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M3.2-K04.md) (431 palabras de borrador, no ensayo final).

### M3.2-K05 — Implementación

La implementación requiere traducir diseños a configuraciones, procesos, responsabilidades y despliegues controlados con rollback. El escenario que conviene examinar es el siguiente: una política se habilita globalmente sin piloto ni comunicación. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M3.2-K05.md) (428 palabras de borrador, no ensayo final).

### M3.2-K06 — Pentesting

Las pruebas de penetración exploran rutas de explotación en un alcance autorizado, complementando pero no sustituyendo evaluación de controles y gestión de riesgos. El escenario que conviene examinar es el siguiente: un resultado sin hallazgos se interpreta como ausencia de vulnerabilidades. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M3.2-K06.md) (439 palabras de borrador, no ensayo final).

### M3.2-K07 — Controles Compensatorios

Un control compensatorio reduce exposición cuando el requisito primario no puede cumplirse, con justificación, límite temporal y evidencia. El escenario que conviene examinar es el siguiente: una excepción temporal se convierte en deuda permanente. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M3.2-K07.md) (435 palabras de borrador, no ensayo final).

### M3.2-K08 — Familias de Controles

Las familias de controles permiten organizar objetivos relacionados y responsabilidades sin asumir equivalencia entre controles individuales. El escenario que conviene examinar es el siguiente: se contabilizan controles por cantidad y no por cobertura de escenarios. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M3.2-K08.md) (438 palabras de borrador, no ensayo final).

### M3.2-K09 — Pruebas de Efectividad

Las pruebas de efectividad verifican resultados bajo escenarios definidos, distinguiendo cobertura, operación y consecuencia observable. El escenario que conviene examinar es el siguiente: un control configurado se declara eficaz sin ejercicio de ataque o recuperación. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M3.2-K09.md) (438 palabras de borrador, no ensayo final).

### M3.2-K10 — POA&M

El Plan of Action and Milestones conecta hallazgos con responsables, recursos, fechas, riesgos y evidencia de cierre verificable. El escenario que conviene examinar es el siguiente: los hallazgos se cierran administrativamente sin corregir causas. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M3.2-K10.md) (435 palabras de borrador, no ensayo final).

## Ampliaciones Atlas de esta unidad: tesis para discutir, no definiciones aprobadas

- **[AMP-37 — Evaluación adversarial de agentes](../../02_conceptos/02_ampliaciones_atlas/AMP-37.md) [P].** Antes de producción, un agente debe resistir pruebas adversariales —inyección, abuso de herramientas, fuga de datos— con criterios de aceptación explícitos. Vínculo propuesto: `HC-032`; fuente `06Ensayos!I321`.
- **[AMP-38 — Pruebas de controles autónomos](../../02_conceptos/02_ampliaciones_atlas/AMP-38.md) [P].** Los controles que actúan solos —bloqueo, contención, remediación— deben probarse en escenarios de falla y con rollback antes de confiarles decisiones. Vínculo propuesto: `M3.2-K09`; fuente `06Ensayos!I322`.

## Conceptos híbridos candidatos que conectan esta unidad

- [HC-002 — Apetito de riesgo convertido en arquitectura](../../02_conceptos/03_hibridos_candidatos/HC-002.md): conecta `G4.2-K01`, `G4.2-K02`, `M3.1-K01`, `M3.2-K03`. **Candidato**, no unidad ni arista aprobada.
- [HC-003 — Riesgo residual y aceptación verificable](../../02_conceptos/03_hibridos_candidatos/HC-003.md): conecta `G5.2-K03`, `G4.2-K10`, `M3.2-K09`, `G3.2-K06`. **Candidato**, no unidad ni arista aprobada.
- [HC-004 — Política como código gobernado](../../02_conceptos/03_hibridos_candidatos/HC-004.md): conecta `G2.2-K02`, `G2.2-K09`, `G3.2-K07`, `M3.2-K05`. **Candidato**, no unidad ni arista aprobada.
- [HC-005 — Cumplimiento continuo orientado a resultados](../../02_conceptos/03_hibridos_candidatos/HC-005.md): conecta `G3.1-K01`, `G3.2-K02`, `M4.1-K02`, `M3.2-K04`. **Candidato**, no unidad ni arista aprobada.
- [HC-015 — Gobierno y operación de Zero Trust](../../02_conceptos/03_hibridos_candidatos/HC-015.md): conecta `G2.2-K03`, `M2.2-K05`, `M3.1-K03`, `M3.2-K09`. **Candidato**, no unidad ni arista aprobada.
- [HC-018 — Observabilidad y aseguramiento de controles](../../02_conceptos/03_hibridos_candidatos/HC-018.md): conecta `M4.1-K02`, `M3.2-K04`, `G3.2-K02`, `G6.1-K05`. **Candidato**, no unidad ni arista aprobada.
- [HC-028 — Gestión de excepciones y compensaciones](../../02_conceptos/03_hibridos_candidatos/HC-028.md): conecta `G2.2-K09`, `G5.2-K03`, `M3.2-K07`, `M3.2-K10`. **Candidato**, no unidad ni arista aprobada.
- [HC-031 — Seguridad del software y confianza en componentes](../../02_conceptos/03_hibridos_candidatos/HC-031.md): conecta `M6.2-K09`, `M6.2-K10`, `M3.2-K03`, `M4.2-K01`. **Candidato**, no unidad ni arista aprobada.
- [HC-032 — Evaluación adversarial de sistemas autónomos](../../02_conceptos/03_hibridos_candidatos/HC-032.md): conecta `M4.2-K02`, `M3.2-K06`, `M6.2-K04`, `M2.2-K03`. **Candidato**, no unidad ni arista aprobada.
- [HC-034 — Decisiones reversibles y riesgo de transición](../../02_conceptos/03_hibridos_candidatos/HC-034.md): conecta `G1.2-K08`, `M3.2-K05`, `M3.1-K10`, `G5.2-K07`. **Candidato**, no unidad ni arista aprobada.
- [HC-036 — Portafolio de controles y capacidades](../../02_conceptos/03_hibridos_candidatos/HC-036.md): conecta `M1.2-K01`, `M3.2-K03`, `M1.1-K05`, `M3.2-K09`. **Candidato**, no unidad ni arista aprobada.
- [HC-038 — Aseguramiento de la arquitectura Zero Trust](../../02_conceptos/03_hibridos_candidatos/HC-038.md): conecta `G2.2-K03`, `M2.2-K05`, `M3.1-K03`, `M3.2-K04`. **Candidato**, no unidad ni arista aprobada.

## Puente con TheMetaCognitiveCISO

Se propone entrenar la lente cognitiva `DP-0110` junto a las decisiones de `M3.2`. Esta es una **relación pedagógica derivada**, no una equivalencia canónica con el GM-24. Consulte [la caja cognitiva del CISO](../../../Biblioteca_CISO_Frontera/Caja_Cognitiva_CISO_72/00_Indice.md) para la ficha y su evidencia.

## Laboratorio: ocho modalidades de ejercicio

Las tareas comparten el mismo caso; no son ocho horas añadidas por separado. Se practican en la asignación indicativa de 3 h de seminario, 8 h de investigación y lectura, 12 h de laboratorio y 8 h de aplicación por unidad. Los tiempos requieren aprobación académica.

### 1. Comprensión conceptual

**Consigna:** Define `M3.2-K03` (Selección y Adaptación) y `M3.2-K09` (Pruebas de Efectividad) con tus palabras. Señala una frontera de responsabilidad, una confusión habitual y cómo la ampliación `AMP-38` altera la interpretación del caso «Un control autónomo contiene malware en laboratorio, pero un falso positivo en producción podría detener la facturación.».

**Producto:** cuadro de contraste con dos decisiones distintas y citas a las fichas.

**Comprobación:** No declara como sinónimos dos títulos vecinos ni toma la tesis [P] como definición aprobada.

### 2. Relaciones y contextualización

**Consigna:** Dibuja la cadena de decisiones entre `M3.2-K03`, `M3.2-K09`, `AMP-38` y `HC-032` — Evaluación adversarial de sistemas autónomos. Anota en cada conexión dirección, evidencia textual, posible solapamiento y qué cambiaría al variar el contexto de negocio. Las aristas nuevas son hipótesis hasta que se validen.

**Producto:** mapa de relaciones G–M y tabla de procedencia de cada enlace.

**Comprobación:** No transforma cercanía temática en causalidad ni convierte HC en requisito aprobado.

### 3. Práctica aplicada

**Consigna:** Trabaja en «Un control autónomo contiene malware en laboratorio, pero un falso positivo en producción podría detener la facturación.». Con requisitos de control, casos de prueba, fallo simulado y POA&M, construye plan de aseguramiento con criterios de aceptación y reversión medibles; incluye propietario, condiciones de entrada y salida, hipótesis adversa y prueba de funcionamiento.

**Producto:** plan de aseguramiento con criterios de aceptación y reversión medibles.

**Comprobación:** Un control configurado no se acredita como efectivo sin prueba independiente relevante.

### 4. Investigación y fuentes

**Consigna:** Investiga esta pregunta acotada: contrastar la selección de controles NIST SP 800-53 con su evaluación y la evidencia de efectividad. Localiza al menos dos fuentes primarias con fecha y versión; distingue obligación, recomendación, definición, ejemplo y opinión.

**Producto:** ficha de fuentes con extractos breves, localizador y discrepancias.

**Comprobación:** No cita un borrador editorial o mapeo informativo como norma obligatoria.

### 5. Orquestación de actores y agentes

**Consigna:** Con QA, red team, ingeniería y propietario de facturación, construye un flujo de tres hitos para «Elegir controles, escenarios de prueba, límites de despliegue y compensaciones.». Define qué puede proponer un agente, qué requiere aprobación humana, quién responde y cómo detener, registrar y revertir una acción errónea.

**Producto:** RACI/DACI, diagrama de traspasos y plan de supervisión.

**Comprobación:** Hay autoridad, trazas y camino de escalamiento para cada acción de alto impacto.

### 6. Análisis y contrafactual

**Consigna:** Compara «Activar bloqueo global frente a piloto por fases con rollback y test adversarial.» usando datos de requisitos de control, casos de prueba, fallo simulado y POA&M. Contrasta la primera impresión con la lente cognitiva `DP-0110` del programa metacognitivo; plantea qué evidencia falsaría cada hipótesis y un efecto de segundo orden.

**Producto:** matriz de alternativas, incertidumbres y pruebas refutatorias.

**Comprobación:** La comparación conserva supuestos, costos de reversión y consecuencias no observadas.

### 7. Toma de decisiones

**Consigna:** Redacta para el responsable competente una recomendación sobre «Elegir controles, escenarios de prueba, límites de despliegue y compensaciones.», con dos opciones, beneficio, riesgo residual, autoridad de aceptación, indicador temprano y condición explícita de pausa o rollback.

**Producto:** memorando ejecutivo de una página más expediente de evidencia.

**Comprobación:** Un control configurado no se acredita como efectivo sin prueba independiente relevante.

### 8. Exposición y defensa

**Consigna:** Defiende la decisión ante QA, red team, ingeniería y propietario de facturación en siete minutos; reserva tres para objeciones. Un par cambia un dato del escenario a mitad de la exposición: revisa la postura sin ocultar el supuesto que deja de sostenerse.

**Producto:** presentación oral, preguntas difíciles y registro de revisiones.

**Comprobación:** La defensa distingue certeza, incertidumbre, decisión y propiedad del riesgo.

## Rúbrica formativa y evidencia de logro

| Criterio | 0 — insuficiente | 2 — parcial | 4 — sólido |
|---|---|---|---|
| Precisión | Confunde conceptos, categorías o estados editoriales | Explica definiciones sin límites | Distingue base, propuesta y candidato; explica límites y relaciones sin equivalencias ficticias |
| Evidencia | Cita sin procedencia ni prueba | Traza fuentes pero no su calidad | Localiza fuente, versión, modalidad, incertidumbre y prueba de eficacia |
| Decisión y autoridad | No compara opciones ni propietario | Compara pero sin residual o escalamiento | Justifica alternativas, derecho de decisión, residual, parada y revisión |
| Transferencia | Entrega teórica sin caso | Caso parcial sin contraprueba | Artefacto operable, prueba adversa y defensa ajustada a la audiencia |

**Condición crítica de esta unidad:** Un control configurado no se acredita como efectivo sin prueba independiente relevante. La práctica se devuelve para revisión si incumple este criterio, aunque el promedio sea alto. Para aprendizaje se propone al menos 3/4 en cada dimensión; no es una acreditación aprobada.

## Preguntas mayéuticas, sin confundirlas con afirmaciones

**Pregunta original consolidada (muestras):**
- `PC-054`: ¿Hacemos pruebas ofensivas (pruebas de penetración, red team, purple team, simulación de ataques) y cómo cerramos el ciclo de los hallazgos? (vínculo `M3.2-K06`).
- `PC-166`: ¿Comprobamos de forma recurrente que los filtros y guardrails bloquean lo que deben y no bloquean lo legítimo? (vínculo `AMP-38`).
- `PC-251`: ¿Cumplimos hoy las 56 salvaguardas del IG1 en todos los activos, y cuáles faltan? (vínculo `M3.2-K04`).
- `PC-254`: ¿Qué cobertura tenemos de configuración segura y de las salvaguardas que más técnicas de ataque mitigan? (vínculo `M3.2-K03`).
- `PA-012`: ¿Qué hallazgos de auditoría y de pruebas de seguridad siguen abiertos, y por qué? (vínculo `M3.2-K10`).
- `PA-053`: ¿Cómo probamos un agente antes de ponerlo en producción y cada vez que cambia? (vínculo `AMP-37`).

**Serie de banco construida desde plantillas documentadas (muestras):**
- `BM-0511` — ¿Qué problema de gobierno, riesgo o capacidad intenta resolver realmente «Controles de Seguridad», y qué decisión debería mejorar si se comprende correctamente?
- `BM-0512` — ¿Qué supuesto habitual sobre «Controles de Seguridad» podría ser falso o incompleto, y qué consecuencia tendría diseñar la seguridad como si fuera cierto?
- `BM-0514` — ¿Qué problema de gobierno, riesgo o capacidad intenta resolver realmente «NIST SP 800-53», y qué decisión debería mejorar si se comprende correctamente?
- `BM-0515` — ¿Qué supuesto habitual sobre «NIST SP 800-53» podría ser falso o incompleto, y qué consecuencia tendría diseñar la seguridad como si fuera cierto?
- `BM-1025` — ¿Qué problema de gobierno, riesgo o capacidad intenta resolver realmente «Evaluación adversarial de agentes», y qué decisión debería mejorar si se comprende correctamente?
- `BM-1026` — ¿Qué supuesto habitual sobre «Evaluación adversarial de agentes» podría ser falso o incompleto, y qué consecuencia tendría diseñar la seguridad como si fuera cierto?

**Tesis propuestas por pregunta asignadas explícitamente a esta unidad: 7.**
- [APC-166 — Verificación recurrente de filtros y barreras de protección de IA](../../03_metodo_mayeutico/01_tesis_derivadas/APC-166.md) ← `PC-166`
- [APC-251 — Verificación de salvaguardas esenciales en todos los activos](../../03_metodo_mayeutico/01_tesis_derivadas/APC-251.md) ← `PC-251`
- [APC-254 — Medición de cobertura de configuración segura por técnicas mitigadas](../../03_metodo_mayeutico/01_tesis_derivadas/APC-254.md) ← `PC-254`
- [APA-053 — Pruebas de agentes antes de producción y tras cada cambio](../../03_metodo_mayeutico/01_tesis_derivadas/APA-053.md) ← `PA-053`
- [APA-077 — Validación auditable de filtros y salvaguardas de IA](../../03_metodo_mayeutico/01_tesis_derivadas/APA-077.md) ← `PA-077`
- [APA-152 — Verificación de cumplimiento de la higiene cibernética esencial](../../03_metodo_mayeutico/01_tesis_derivadas/APA-152.md) ← `PA-152`
- [APA-155 — Priorización de controles según los ataques que frenan](../../03_metodo_mayeutico/01_tesis_derivadas/APA-155.md) ← `PA-155`

**Tesis transversales relacionadas sin asignación principal (muestras):**
- [APC-025](../../03_metodo_mayeutico/01_tesis_derivadas/APC-025.md) (relación transversal, no asignación principal)
- [APC-050](../../03_metodo_mayeutico/01_tesis_derivadas/APC-050.md) (relación transversal, no asignación principal)
- [APC-062](../../03_metodo_mayeutico/01_tesis_derivadas/APC-062.md) (relación transversal, no asignación principal)
- [APC-164](../../03_metodo_mayeutico/01_tesis_derivadas/APC-164.md) (relación transversal, no asignación principal)
- [APC-173](../../03_metodo_mayeutico/01_tesis_derivadas/APC-173.md) (relación transversal, no asignación principal)

El banco completo conserva 543 preguntas originales y 2.395 preguntas derivadas mecánicamente de plantillas; 308 tesis AP forman un **anexo provisional**, distinto de los 331 conceptos del corpus de trabajo.

## Lecturas, investigación y modalidad

**Lecturas internas verificables:**
- [Documento Maestro](../../../Curado02/01_noviembre_2026/src-thenextciso-gm-24-documento-maestro__9b8c53df319d.md), unidad `M3.2` desde línea 761.
- [lote de ideas base](../../../Curado02/01_noviembre_2026/src-thenextciso-gm24-ensayos-bases-151-180__be034906f333.md)
- Las 51 tesis Atlas [P] proceden de `06Ensayos!I285:I335` en [matriz de pre-ensayos](../../../Curado02/01_noviembre_2026/src-ai-ciso-atlas-ensayos-thenextciso-x-core-accountabilities-fy27-2026-11-05__5528a05eb5dd.xlsx).

**Lecturas complementarias por cotejar:** NIST CSF 2.0, NIST RMF y dominios CISM/CRISC según la unidad y las fuentes listadas por el Documento Maestro. El mapeo de este documento es una propuesta temática: `CISM C3; CRISC R3,R4; NIST CSF 2.0 PR.PS,ID.IM; NIST RMF Select,Implement,Assess.`. La fuente oficial, edición y pertinencia deben comprobarse al preparar cada clase; no se presume cobertura íntegra de examen o norma.

**Recursos audiovisuales:** no se identificó un video específico, vigente y verificable por unidad en los documentos base. Existe un [inventario complementario de enlaces observados](../../../Biblioteca_CISO_Frontera/Consolidado_2026_MM_2026-11-11/03_programa_1200h/Videos_Observados_en_Fuentes.md), aún sin comprobación de contenido, disponibilidad, duración ni correspondencia con esta unidad. El equipo docente deberá seleccionarlos, comprobar derechos y documentar el vínculo antes de asignarlos.

**Carga de diseño:** 31 h por unidad; 24 unidades más capstone integrador de 56 h = escenario de 800 h. No es acreditación.

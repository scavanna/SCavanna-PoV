<!-- generado-gm24 sha256:15c87ff40ad5d3e1133552c4fa967403a68640098394c46fc35a69260baba223 -->
# M4.2 — Gestión de Amenazas, Vulnerabilidades y Riesgos Emergentes

**Pilar:** Gestión · **Eje:** Operaciones proactivas y amenazas · **Atlas:** `D12,D13` (alineación editorial, no identidad de dominio).

**Pregunta rectora de fuente:** ¿Cómo puede un CISO diseñar, ejecutar y verificar gestión de amenazas, vulnerabilidades y riesgos emergentes sin perder de vista el riesgo empresarial, las responsabilidades y la evidencia?

**Alcance:** diez conceptos base con idea central desarrollada; 2 ampliaciones Atlas cuyo título pertenece al Documento Maestro y cuya tesis es propuesta [P]. Los puentes HC relacionados son candidatos transversales; ninguna extensión altera por sí sola el número de unidades.

## Situación longitudinal y decisión

**Organización ficticia:** Un documento de incidente en la base RAG contiene instrucciones falsas para un agente y referencias manipuladas de indicadores.

**Decisión a sostener:** Modelar amenaza de prompt injection y envenenamiento, priorizar defensas y señales de detección.

**Cursos de acción en tensión:** Confiar en filtrado de texto frente a limitar herramientas, procedencia de datos y validación de acciones.

**Información inicial:** datos RAG, threat model, trazas de invocación y catálogo de vulnerabilidades

**Interesados:** threat intel, data engineering y respuesta a incidentes

**Producto acumulativo:** modelo de amenazas actualizado con pruebas adversariales y riesgo residual

**Regla de seguridad y responsabilidad:** Contenido recuperado no se convierte en instrucción autorizada por su formato o su supuesta fuente.

## Desarrollo de los diez conceptos base

### M4.2-K01 — Gestión Vulnerabilidades

La gestión de vulnerabilidades prioriza descubrimiento, evaluación, remediación y verificación según explotabilidad, exposición y consecuencias. El problema aparece cuando se cierran vulnerabilidades de alto score mientras una ruta de ataque crítica permanece abierta. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M4.2-K01.md) (444 palabras de borrador, no ensayo final).

### M4.2-K02 — Modelado de Amenazas

El modelado de amenazas identifica objetivos adversarios, superficies, límites de confianza y fallas plausibles durante el diseño y la evolución de sistemas. El problema aparece cuando el equipo aplica una checklist genérica que omite identidades no humanas y herramientas de agentes. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M4.2-K02.md) (450 palabras de borrador, no ensayo final).

### M4.2-K03 — Amenaza Interna

La amenaza interna incluye abuso intencional, errores y accesos legítimos mal utilizados, y exige protección proporcional de datos y derechos. El problema aparece cuando un programa de vigilancia interpreta cualquier anomalía laboral como intención maliciosa. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M4.2-K03.md) (442 palabras de borrador, no ensayo final).

### M4.2-K04 — RaaS (Ransomware)

Ransomware-as-a-Service industrializa extorsión y ataques mediante ecosistemas de afiliados, herramientas y modelos económicos especializados. El problema aparece cuando una organización se enfoca únicamente en cifrado y omite robo de datos, acceso inicial y presión sobre terceros. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M4.2-K04.md) (449 palabras de borrador, no ensayo final).

### M4.2-K05 — Priorización por Riesgo

Priorizar por riesgo significa decidir qué exposición tratar primero según probabilidad condicionada, consecuencias, dependencias y opciones de mitigación. El problema aparece cuando una puntuación CVSS aislada determina todo el backlog sin considerar el negocio. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M4.2-K05.md) (443 palabras de borrador, no ensayo final).

### M4.2-K06 — Superficie de Ataque

La superficie de ataque comprende activos, identidades, servicios, interfaces y relaciones explotables desde diferentes posiciones del adversario. El problema aparece cuando el inventario externo ignora rutas internas, SaaS, terceros y agentes conectados. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M4.2-K06.md) (442 palabras de borrador, no ensayo final).

### M4.2-K07 — Riesgos Emergentes

Los riesgos emergentes surgen de cambios tecnológicos, adversariales, regulatorios o empresariales cuya frecuencia y consecuencias aún son inciertas. El problema aparece cuando se convierte una tendencia en prioridad universal sin evaluar exposición o preparación local. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M4.2-K07.md) (444 palabras de borrador, no ensayo final).

### M4.2-K08 — Economía del Cibercrimen

La economía del cibercrimen explica incentivos, mercados, especialización y monetización que condicionan campañas y objetivos adversarios. El problema aparece cuando el análisis se limita a herramientas técnicas sin considerar incentivos y oportunidad económica. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M4.2-K08.md) (442 palabras de borrador, no ensayo final).

### M4.2-K09 — STRIDE

STRIDE organiza preguntas de modelado sobre suplantación, manipulación, repudio, divulgación, denegación de servicio y elevación de privilegios. El problema aparece cuando la taxonomía se usa como sustituto de comprender flujos, activos y límites de confianza. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M4.2-K09.md) (444 palabras de borrador, no ensayo final).

### M4.2-K10 — IoC (Indicadores)

Los indicadores de compromiso aportan señales observables de actividad sospechosa, pero requieren contexto, caducidad y correlación para sostener conclusiones. El problema aparece cuando una coincidencia de hash o dirección IP se interpreta automáticamente como incidente confirmado. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M4.2-K10.md) (444 palabras de borrador, no ensayo final).

## Ampliaciones Atlas de esta unidad: tesis para discutir, no definiciones aprobadas

- **[AMP-41 — Prompt injection](../../02_conceptos/02_ampliaciones_atlas/AMP-41.md) [P].** La inyección de instrucciones convierte contenido en órdenes; la defensa combina aislamiento de datos, límites de herramientas, filtros y detección en ejecución. Vínculo propuesto: `M6.2-K04`; fuente `06Ensayos!I325`.
- **[AMP-42 — Envenenamiento de datos y modelos](../../02_conceptos/02_ampliaciones_atlas/AMP-42.md) [P].** El envenenamiento ataca la integridad del aprendizaje y de la recuperación: exige procedencia, control de fuentes y monitoreo de comportamiento. Vínculo propuesto: `M4.2-K07`; fuente `06Ensayos!I326`.

## Conceptos híbridos candidatos que conectan esta unidad

- [HC-016 — Superficie de ataque contextualizada](../../02_conceptos/03_hibridos_candidatos/HC-016.md): conecta `M2.1-K03`, `M4.2-K06`, `M4.2-K08`, `G5.1-K08`. **Candidato**, no unidad ni arista aprobada.
- [HC-026 — Ética, cultura y controles internos](../../02_conceptos/03_hibridos_candidatos/HC-026.md): conecta `G6.2-K01`, `G6.1-K10`, `M4.2-K03`, `M1.2-K10`. **Candidato**, no unidad ni arista aprobada.
- [HC-031 — Seguridad del software y confianza en componentes](../../02_conceptos/03_hibridos_candidatos/HC-031.md): conecta `M6.2-K09`, `M6.2-K10`, `M3.2-K03`, `M4.2-K01`. **Candidato**, no unidad ni arista aprobada.
- [HC-032 — Evaluación adversarial de sistemas autónomos](../../02_conceptos/03_hibridos_candidatos/HC-032.md): conecta `M4.2-K02`, `M3.2-K06`, `M6.2-K04`, `M2.2-K03`. **Candidato**, no unidad ni arista aprobada.

## Puente con TheMetaCognitiveCISO

Se propone entrenar la lente cognitiva `MM-0077` junto a las decisiones de `M4.2`. Esta es una **relación pedagógica derivada**, no una equivalencia canónica con el GM-24. Consulte [la caja cognitiva del CISO](../../../Biblioteca_CISO_Frontera/Caja_Cognitiva_CISO_72/00_Indice.md) para la ficha y su evidencia.

## Laboratorio: ocho modalidades de ejercicio

Las tareas comparten el mismo caso; no son ocho horas añadidas por separado. Se practican en la asignación indicativa de 3 h de seminario, 8 h de investigación y lectura, 12 h de laboratorio y 8 h de aplicación por unidad. Los tiempos requieren aprobación académica.

### 1. Comprensión conceptual

**Consigna:** Define `M4.2-K02` (Modelado de Amenazas) y `M4.2-K05` (Priorización por Riesgo) con tus palabras. Señala una frontera de responsabilidad, una confusión habitual y cómo la ampliación `AMP-41` altera la interpretación del caso «Un documento de incidente en la base RAG contiene instrucciones falsas para un agente y referencias manipuladas de indicadores.».

**Producto:** cuadro de contraste con dos decisiones distintas y citas a las fichas.

**Comprobación:** No declara como sinónimos dos títulos vecinos ni toma la tesis [P] como definición aprobada.

### 2. Relaciones y contextualización

**Consigna:** Dibuja la cadena de decisiones entre `M4.2-K02`, `M4.2-K05`, `AMP-41` y `HC-016` — Superficie de ataque contextualizada. Anota en cada conexión dirección, evidencia textual, posible solapamiento y qué cambiaría al variar el contexto de negocio. Las aristas nuevas son hipótesis hasta que se validen.

**Producto:** mapa de relaciones G–M y tabla de procedencia de cada enlace.

**Comprobación:** No transforma cercanía temática en causalidad ni convierte HC en requisito aprobado.

### 3. Práctica aplicada

**Consigna:** Trabaja en «Un documento de incidente en la base RAG contiene instrucciones falsas para un agente y referencias manipuladas de indicadores.». Con datos RAG, threat model, trazas de invocación y catálogo de vulnerabilidades, construye modelo de amenazas actualizado con pruebas adversariales y riesgo residual; incluye propietario, condiciones de entrada y salida, hipótesis adversa y prueba de funcionamiento.

**Producto:** modelo de amenazas actualizado con pruebas adversariales y riesgo residual.

**Comprobación:** Contenido recuperado no se convierte en instrucción autorizada por su formato o su supuesta fuente.

### 4. Investigación y fuentes

**Consigna:** Investiga esta pregunta acotada: separar indicadores observables de inferencias sobre TTPs y prevalencia del atacante. Localiza al menos dos fuentes primarias con fecha y versión; distingue obligación, recomendación, definición, ejemplo y opinión.

**Producto:** ficha de fuentes con extractos breves, localizador y discrepancias.

**Comprobación:** No cita un borrador editorial o mapeo informativo como norma obligatoria.

### 5. Orquestación de actores y agentes

**Consigna:** Con threat intel, data engineering y respuesta a incidentes, construye un flujo de tres hitos para «Modelar amenaza de prompt injection y envenenamiento, priorizar defensas y señales de detección.». Define qué puede proponer un agente, qué requiere aprobación humana, quién responde y cómo detener, registrar y revertir una acción errónea.

**Producto:** RACI/DACI, diagrama de traspasos y plan de supervisión.

**Comprobación:** Hay autoridad, trazas y camino de escalamiento para cada acción de alto impacto.

### 6. Análisis y contrafactual

**Consigna:** Compara «Confiar en filtrado de texto frente a limitar herramientas, procedencia de datos y validación de acciones.» usando datos de datos RAG, threat model, trazas de invocación y catálogo de vulnerabilidades. Contrasta la primera impresión con la lente cognitiva `MM-0077` del programa metacognitivo; plantea qué evidencia falsaría cada hipótesis y un efecto de segundo orden.

**Producto:** matriz de alternativas, incertidumbres y pruebas refutatorias.

**Comprobación:** La comparación conserva supuestos, costos de reversión y consecuencias no observadas.

### 7. Toma de decisiones

**Consigna:** Redacta para el responsable competente una recomendación sobre «Modelar amenaza de prompt injection y envenenamiento, priorizar defensas y señales de detección.», con dos opciones, beneficio, riesgo residual, autoridad de aceptación, indicador temprano y condición explícita de pausa o rollback.

**Producto:** memorando ejecutivo de una página más expediente de evidencia.

**Comprobación:** Contenido recuperado no se convierte en instrucción autorizada por su formato o su supuesta fuente.

### 8. Exposición y defensa

**Consigna:** Defiende la decisión ante threat intel, data engineering y respuesta a incidentes en siete minutos; reserva tres para objeciones. Un par cambia un dato del escenario a mitad de la exposición: revisa la postura sin ocultar el supuesto que deja de sostenerse.

**Producto:** presentación oral, preguntas difíciles y registro de revisiones.

**Comprobación:** La defensa distingue certeza, incertidumbre, decisión y propiedad del riesgo.

## Rúbrica formativa y evidencia de logro

| Criterio | 0 — insuficiente | 2 — parcial | 4 — sólido |
|---|---|---|---|
| Precisión | Confunde conceptos, categorías o estados editoriales | Explica definiciones sin límites | Distingue base, propuesta y candidato; explica límites y relaciones sin equivalencias ficticias |
| Evidencia | Cita sin procedencia ni prueba | Traza fuentes pero no su calidad | Localiza fuente, versión, modalidad, incertidumbre y prueba de eficacia |
| Decisión y autoridad | No compara opciones ni propietario | Compara pero sin residual o escalamiento | Justifica alternativas, derecho de decisión, residual, parada y revisión |
| Transferencia | Entrega teórica sin caso | Caso parcial sin contraprueba | Artefacto operable, prueba adversa y defensa ajustada a la audiencia |

**Condición crítica de esta unidad:** Contenido recuperado no se convierte en instrucción autorizada por su formato o su supuesta fuente. La práctica se devuelve para revisión si incumple este criterio, aunque el promedio sea alto. Para aprendizaje se propone al menos 3/4 en cada dimensión; no es una acreditación aprobada.

## Preguntas mayéuticas, sin confundirlas con afirmaciones

**Pregunta original consolidada (muestras):**
- `PC-040`: ¿Cómo gestionamos el riesgo interno, negligente o malicioso, con proporcionalidad y respeto por la privacidad de las personas? (vínculo `M4.2-K03`).
- `PC-047`: ¿Cuánto tiempo permanecen expuestos nuestros activos críticos a vulnerabilidades explotables y cuál es nuestra meta? (vínculo `M4.2-K01`).
- `PC-048`: ¿Priorizamos la remediación por explotabilidad, rutas de ataque y criticidad del activo, o solo por severidad nominal? (vínculo `M4.2-K05`).
- `PC-052`: ¿Podríamos absorber un volumen de vulnerabilidades diez veces mayor al actual, ahora que atacantes y defensores las descubren con IA? (vínculo `M4.2-K01`).
- `PC-141`: ¿Cómo detectamos el uso riesgoso de IA por parte de personas internas (búsqueda de información sensible, exfiltración a través de la IA, uso de IA no autorizada)? (vínculo `M4.2-K03`).
- `PC-143`: ¿Cómo garantizamos la calidad, procedencia e integridad de los datos que alimentan a la IA para evitar envenenamiento y respuestas sin fundamento? (vínculo `AMP-42`).

**Serie de banco construida desde plantillas documentadas (muestras):**
- `BM-0571` — ¿Qué problema de gobierno, riesgo o capacidad intenta resolver realmente «Gestión Vulnerabilidades», y qué decisión debería mejorar si se comprende correctamente?
- `BM-0572` — ¿Qué supuesto habitual sobre «Gestión Vulnerabilidades» podría ser falso o incompleto, y qué consecuencia tendría diseñar la seguridad como si fuera cierto?
- `BM-0574` — ¿Qué problema de gobierno, riesgo o capacidad intenta resolver realmente «Modelado de Amenazas», y qué decisión debería mejorar si se comprende correctamente?
- `BM-0575` — ¿Qué supuesto habitual sobre «Modelado de Amenazas» podría ser falso o incompleto, y qué consecuencia tendría diseñar la seguridad como si fuera cierto?
- `BM-1041` — ¿Qué problema de gobierno, riesgo o capacidad intenta resolver realmente «Prompt injection», y qué decisión debería mejorar si se comprende correctamente?
- `BM-1042` — ¿Qué supuesto habitual sobre «Prompt injection» podría ser falso o incompleto, y qué consecuencia tendría diseñar la seguridad como si fuera cierto?

**Tesis propuestas por pregunta asignadas explícitamente a esta unidad: 13.**
- [APC-052 — Capacidad de remediación ante vulnerabilidades descubiertas con IA](../../03_metodo_mayeutico/01_tesis_derivadas/APC-052.md) ← `PC-052`
- [APC-141 — Detección de uso interno riesgoso de la IA](../../03_metodo_mayeutico/01_tesis_derivadas/APC-141.md) ← `PC-141`
- [APC-152 — Defensa frente a ataques potenciados por IA](../../03_metodo_mayeutico/01_tesis_derivadas/APC-152.md) ← `PC-152`
- [APC-213 — Tiempos de detección y contención ante ataques agénticos](../../03_metodo_mayeutico/01_tesis_derivadas/APC-213.md) ← `PC-213`
- [APC-232 — Mapa de contenido no confiable, herramientas y privilegios de agentes](../../03_metodo_mayeutico/01_tesis_derivadas/APC-232.md) ← `PC-232`
- [APC-292 — Análisis de cadenas de ataque entre capas de la IA](../../03_metodo_mayeutico/01_tesis_derivadas/APC-292.md) ← `PC-292`
- [APC-297 — Escenarios y controles para la IA atacante y atacada](../../03_metodo_mayeutico/01_tesis_derivadas/APC-297.md) ← `PC-297`
- [APA-114 — Preparación medible ante ataques automatizados con IA](../../03_metodo_mayeutico/01_tesis_derivadas/APA-114.md) ← `PA-114`

**Tesis transversales relacionadas sin asignación principal (muestras):**
- [APC-050](../../03_metodo_mayeutico/01_tesis_derivadas/APC-050.md) (relación transversal, no asignación principal)
- [APC-051](../../03_metodo_mayeutico/01_tesis_derivadas/APC-051.md) (relación transversal, no asignación principal)
- [APC-062](../../03_metodo_mayeutico/01_tesis_derivadas/APC-062.md) (relación transversal, no asignación principal)
- [APC-198](../../03_metodo_mayeutico/01_tesis_derivadas/APC-198.md) (relación transversal, no asignación principal)
- [APC-281](../../03_metodo_mayeutico/01_tesis_derivadas/APC-281.md) (relación transversal, no asignación principal)

El banco completo conserva 543 preguntas originales y 2.395 preguntas derivadas mecánicamente de plantillas; 308 tesis AP forman un **anexo provisional**, distinto de los 331 conceptos del corpus de trabajo.

## Lecturas, investigación y modalidad

**Lecturas internas verificables:**
- [Documento Maestro](../../../Curado02/01_noviembre_2026/src-thenextciso-gm-24-documento-maestro__9b8c53df319d.md), unidad `M4.2` desde línea 843.
- [lote de ideas base](../../../Curado02/01_noviembre_2026/src-thenextciso-gm-24-ensayos-base-181210__69cc0f303c88.md)
- Las 51 tesis Atlas [P] proceden de `06Ensayos!I285:I335` en [matriz de pre-ensayos](../../../Curado02/01_noviembre_2026/src-ai-ciso-atlas-ensayos-thenextciso-x-core-accountabilities-fy27-2026-11-05__5528a05eb5dd.xlsx).

**Lecturas complementarias por cotejar:** NIST CSF 2.0, NIST RMF y dominios CISM/CRISC según la unidad y las fuentes listadas por el Documento Maestro. El mapeo de este documento es una propuesta temática: `CISM C2,C3; CRISC R2,R4; NIST CSF 2.0 ID.RA,ID.IM,DE.AE; NIST RMF Assess,Monitor.`. La fuente oficial, edición y pertinencia deben comprobarse al preparar cada clase; no se presume cobertura íntegra de examen o norma.

**Recursos audiovisuales:** no se identificó un video específico, vigente y verificable por unidad en los documentos base. Existe un [inventario complementario de enlaces observados](../../../Biblioteca_CISO_Frontera/Consolidado_2026_MM_2026-11-11/03_programa_1200h/Videos_Observados_en_Fuentes.md), aún sin comprobación de contenido, disponibilidad, duración ni correspondencia con esta unidad. El equipo docente deberá seleccionarlos, comprobar derechos y documentar el vínculo antes de asignarlos.

**Carga de diseño:** 31 h por unidad; 24 unidades más capstone integrador de 56 h = escenario de 800 h. No es acreditación.

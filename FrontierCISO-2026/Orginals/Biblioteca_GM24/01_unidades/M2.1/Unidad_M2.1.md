<!-- generado-gm24 sha256:96bc6b9a013ee26682142c59405a60237c5d82663644a289277b7f0ae0b96699 -->
# M2.1 — Gestión de Activos y Seguridad del Ciclo de Vida de los Datos

**Pilar:** Gestión · **Eje:** Protección de activos e identidades · **Atlas:** `D06,D07` (alineación editorial, no identidad de dominio).

**Pregunta rectora de fuente:** ¿Cómo puede un CISO diseñar, ejecutar y verificar gestión de activos y seguridad del ciclo de vida de los datos sin perder de vista el riesgo empresarial, las responsabilidades y la evidencia?

**Alcance:** diez conceptos base con idea central desarrollada; 2 ampliaciones Atlas cuyo título pertenece al Documento Maestro y cuya tesis es propuesta [P]. Los puentes HC relacionados son candidatos transversales; ninguna extensión altera por sí sola el número de unidades.

## Situación longitudinal y decisión

**Organización ficticia:** Un asistente RAG recupera documentos compartidos en exceso y retiene fragmentos sensibles más tiempo del permitido.

**Decisión a sostener:** Inventariar, clasificar, restringir y verificar acceso a datos usados por IA.

**Cursos de acción en tensión:** Apagar toda búsqueda frente a segmentar corpus por sensibilidad y corregir permisos heredados.

**Información inicial:** inventario de repositorios, clasificación, permisos, retención y logs de recuperación

**Interesados:** data owners, privacidad, arquitectura de IA

**Producto acumulativo:** mapa de exposición de datos con remediaciones priorizadas y prueba de acceso

**Regla de seguridad y responsabilidad:** Clasificar datos sin corregir su acceso no demuestra que la IA respete su alcance.

## Desarrollo de los diez conceptos base

### M2.1-K01 — Identificación Activos

La identificación de activos busca reconocer recursos, servicios, identidades, datos y dependencias que sostienen resultados empresariales. El riesgo aparece cuando el inventario tradicional omite workloads efímeros, agentes o servicios de terceros. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M2.1-K01.md) (467 palabras de borrador, no ensayo final).

### M2.1-K02 — Clasificación

La clasificación permite aplicar niveles de protección proporcionales al valor, sensibilidad, criticidad y obligaciones de la información y los activos. El riesgo aparece cuando etiquetas excesivas o ambiguas impiden su uso consistente en procesos reales. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M2.1-K02.md) (467 palabras de borrador, no ensayo final).

### M2.1-K03 — Inventario

El inventario de activos es un registro vivo de recursos y relaciones que debe mantenerse mediante descubrimiento, ownership y validación periódica. El riesgo aparece cuando una CMDB aparentemente completa no refleja recursos cloud o dispositivos desconectados. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M2.1-K03.md) (466 palabras de borrador, no ensayo final).

### M2.1-K04 — Ciclo de Vida Datos

El ciclo de vida de datos abarca creación, uso, intercambio, almacenamiento, archivo y eliminación bajo criterios de seguridad y privacidad. El riesgo aparece cuando la organización protege datos en reposo pero pierde control durante exportación o uso en IA. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M2.1-K04.md) (478 palabras de borrador, no ensayo final).

### M2.1-K05 — Seguridad Reposo/Tránsito

La seguridad de datos en reposo y tránsito combina cifrado, autenticación, gestión de claves y controles de acceso adaptados a amenazas y requisitos. El riesgo aparece cuando se considera suficiente activar cifrado sin gestionar claves, permisos o puntos de exposición. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M2.1-K05.md) (472 palabras de borrador, no ensayo final).

### M2.1-K06 — Retención/Destrucción

La retención y destrucción gobiernan cuánto tiempo deben conservarse datos y cómo eliminarlos de forma verificable al finalizar su finalidad o plazo aplicable. El riesgo aparece cuando copias de seguridad y repositorios secundarios preservan información más allá de lo autorizado. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M2.1-K06.md) (475 palabras de borrador, no ensayo final).

### M2.1-K07 — Gobernanza Datos

La gobernanza de datos define roles, calidad, metadatos, acceso y políticas para que la información sea utilizable y protegida durante todo su ciclo. El riesgo aparece cuando el CISO intenta controlar datos sin coordinación con propietarios, privacidad o arquitectura. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M2.1-K07.md) (473 palabras de borrador, no ensayo final).

### M2.1-K08 — Activos Críticos

La criticidad de activos se determina por las consecuencias de su pérdida o degradación para servicios, obligaciones y personas, no únicamente por su costo técnico. El riesgo aparece cuando un componente compartido de bajo costo concentra dependencias de múltiples servicios esenciales. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M2.1-K08.md) (470 palabras de borrador, no ensayo final).

### M2.1-K09 — Auditoría Activos

La auditoría de activos verifica existencia, clasificación, propiedad, controles y consistencia entre inventarios y realidad operativa. El riesgo aparece cuando un inventario declara cobertura completa sin reconciliar activos huérfanos o shadow IT. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M2.1-K09.md) (463 palabras de borrador, no ensayo final).

### M2.1-K10 — Riesgos de Datos

Los riesgos de datos combinan exposición, accesos, usos indebidos, integridad, disponibilidad y obligaciones según contextos de negocio y tecnología. El riesgo aparece cuando se reduce el análisis a DLP sin considerar inferencias de IA, proveedores o abuso autorizado. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M2.1-K10.md) (474 palabras de borrador, no ensayo final).

## Ampliaciones Atlas de esta unidad: tesis para discutir, no definiciones aprobadas

- **[AMP-31 — DSPM](../../02_conceptos/02_ampliaciones_atlas/AMP-31.md) [P].** DSPM convierte la protección de datos en gestión continua de exposición: dónde está el dato sensible, quién accede y qué remediar primero. Vínculo propuesto: `HC-011`; fuente `06Ensayos!I315`.
- **[AMP-32 — Gobierno de datos para RAG](../../02_conceptos/02_ampliaciones_atlas/AMP-32.md) [P].** En RAG la IA hereda permisos y calidad de los datos que recupera; sin clasificación, permisos correctos y control de sobrecompartición expone lo que nadie debía ver. Vínculo propuesto: `HC-011`; fuente `06Ensayos!I316`.

## Conceptos híbridos candidatos que conectan esta unidad

- [HC-011 — Seguridad de datos en la IA empresarial](../../02_conceptos/03_hibridos_candidatos/HC-011.md): conecta `M2.1-K02`, `M2.1-K04`, `G3.1-K02`, `M6.2-K04`. **Candidato**, no unidad ni arista aprobada.
- [HC-014 — Arquitectura de riesgo empresarial](../../02_conceptos/03_hibridos_candidatos/HC-014.md): conecta `G1.2-K07`, `G4.1-K06`, `M3.1-K05`, `M2.1-K08`. **Candidato**, no unidad ni arista aprobada.
- [HC-016 — Superficie de ataque contextualizada](../../02_conceptos/03_hibridos_candidatos/HC-016.md): conecta `M2.1-K03`, `M4.2-K06`, `M4.2-K08`, `G5.1-K08`. **Candidato**, no unidad ni arista aprobada.
- [HC-024 — Cumplimiento y privacidad por diseño](../../02_conceptos/03_hibridos_candidatos/HC-024.md): conecta `G3.1-K02`, `M2.1-K04`, `M6.2-K09`, `G3.2-K06`. **Candidato**, no unidad ni arista aprobada.
- [HC-033 — Seguridad y soberanía de datos distribuidos](../../02_conceptos/03_hibridos_candidatos/HC-033.md): conecta `G3.1-K02`, `M2.1-K07`, `M6.2-K02`, `M6.2-K07`. **Candidato**, no unidad ni arista aprobada.

## Puente con TheMetaCognitiveCISO

Se propone entrenar la lente cognitiva `COG-0104` junto a las decisiones de `M2.1`. Esta es una **relación pedagógica derivada**, no una equivalencia canónica con el GM-24. Consulte [la caja cognitiva del CISO](../../../Biblioteca_CISO_Frontera/Caja_Cognitiva_CISO_72/00_Indice.md) para la ficha y su evidencia.

## Laboratorio: ocho modalidades de ejercicio

Las tareas comparten el mismo caso; no son ocho horas añadidas por separado. Se practican en la asignación indicativa de 3 h de seminario, 8 h de investigación y lectura, 12 h de laboratorio y 8 h de aplicación por unidad. Los tiempos requieren aprobación académica.

### 1. Comprensión conceptual

**Consigna:** Define `M2.1-K02` (Clasificación) y `M2.1-K04` (Ciclo de Vida Datos) con tus palabras. Señala una frontera de responsabilidad, una confusión habitual y cómo la ampliación `AMP-32` altera la interpretación del caso «Un asistente RAG recupera documentos compartidos en exceso y retiene fragmentos sensibles más tiempo del permitido.».

**Producto:** cuadro de contraste con dos decisiones distintas y citas a las fichas.

**Comprobación:** No declara como sinónimos dos títulos vecinos ni toma la tesis [P] como definición aprobada.

### 2. Relaciones y contextualización

**Consigna:** Dibuja la cadena de decisiones entre `M2.1-K02`, `M2.1-K04`, `AMP-32` y `HC-011` — Seguridad de datos en la IA empresarial. Anota en cada conexión dirección, evidencia textual, posible solapamiento y qué cambiaría al variar el contexto de negocio. Las aristas nuevas son hipótesis hasta que se validen.

**Producto:** mapa de relaciones G–M y tabla de procedencia de cada enlace.

**Comprobación:** No transforma cercanía temática en causalidad ni convierte HC en requisito aprobado.

### 3. Práctica aplicada

**Consigna:** Trabaja en «Un asistente RAG recupera documentos compartidos en exceso y retiene fragmentos sensibles más tiempo del permitido.». Con inventario de repositorios, clasificación, permisos, retención y logs de recuperación, construye mapa de exposición de datos con remediaciones priorizadas y prueba de acceso; incluye propietario, condiciones de entrada y salida, hipótesis adversa y prueba de funcionamiento.

**Producto:** mapa de exposición de datos con remediaciones priorizadas y prueba de acceso.

**Comprobación:** Clasificar datos sin corregir su acceso no demuestra que la IA respete su alcance.

### 4. Investigación y fuentes

**Consigna:** Investiga esta pregunta acotada: estudiar diferencia entre ubicación, clasificación, ciclo de vida y control de sobrecompartición. Localiza al menos dos fuentes primarias con fecha y versión; distingue obligación, recomendación, definición, ejemplo y opinión.

**Producto:** ficha de fuentes con extractos breves, localizador y discrepancias.

**Comprobación:** No cita un borrador editorial o mapeo informativo como norma obligatoria.

### 5. Orquestación de actores y agentes

**Consigna:** Con data owners, privacidad, arquitectura de IA, construye un flujo de tres hitos para «Inventariar, clasificar, restringir y verificar acceso a datos usados por IA.». Define qué puede proponer un agente, qué requiere aprobación humana, quién responde y cómo detener, registrar y revertir una acción errónea.

**Producto:** RACI/DACI, diagrama de traspasos y plan de supervisión.

**Comprobación:** Hay autoridad, trazas y camino de escalamiento para cada acción de alto impacto.

### 6. Análisis y contrafactual

**Consigna:** Compara «Apagar toda búsqueda frente a segmentar corpus por sensibilidad y corregir permisos heredados.» usando datos de inventario de repositorios, clasificación, permisos, retención y logs de recuperación. Contrasta la primera impresión con la lente cognitiva `COG-0104` del programa metacognitivo; plantea qué evidencia falsaría cada hipótesis y un efecto de segundo orden.

**Producto:** matriz de alternativas, incertidumbres y pruebas refutatorias.

**Comprobación:** La comparación conserva supuestos, costos de reversión y consecuencias no observadas.

### 7. Toma de decisiones

**Consigna:** Redacta para el responsable competente una recomendación sobre «Inventariar, clasificar, restringir y verificar acceso a datos usados por IA.», con dos opciones, beneficio, riesgo residual, autoridad de aceptación, indicador temprano y condición explícita de pausa o rollback.

**Producto:** memorando ejecutivo de una página más expediente de evidencia.

**Comprobación:** Clasificar datos sin corregir su acceso no demuestra que la IA respete su alcance.

### 8. Exposición y defensa

**Consigna:** Defiende la decisión ante data owners, privacidad, arquitectura de IA en siete minutos; reserva tres para objeciones. Un par cambia un dato del escenario a mitad de la exposición: revisa la postura sin ocultar el supuesto que deja de sostenerse.

**Producto:** presentación oral, preguntas difíciles y registro de revisiones.

**Comprobación:** La defensa distingue certeza, incertidumbre, decisión y propiedad del riesgo.

## Rúbrica formativa y evidencia de logro

| Criterio | 0 — insuficiente | 2 — parcial | 4 — sólido |
|---|---|---|---|
| Precisión | Confunde conceptos, categorías o estados editoriales | Explica definiciones sin límites | Distingue base, propuesta y candidato; explica límites y relaciones sin equivalencias ficticias |
| Evidencia | Cita sin procedencia ni prueba | Traza fuentes pero no su calidad | Localiza fuente, versión, modalidad, incertidumbre y prueba de eficacia |
| Decisión y autoridad | No compara opciones ni propietario | Compara pero sin residual o escalamiento | Justifica alternativas, derecho de decisión, residual, parada y revisión |
| Transferencia | Entrega teórica sin caso | Caso parcial sin contraprueba | Artefacto operable, prueba adversa y defensa ajustada a la audiencia |

**Condición crítica de esta unidad:** Clasificar datos sin corregir su acceso no demuestra que la IA respete su alcance. La práctica se devuelve para revisión si incumple este criterio, aunque el promedio sea alto. Para aprendizaje se propone al menos 3/4 en cada dimensión; no es una acreditación aprobada.

## Preguntas mayéuticas, sin confundirlas con afirmaciones

**Pregunta original consolidada (muestras):**
- `PC-011`: ¿Cuáles son nuestras joyas de la corona (procesos, datos, sistemas e identidades) y qué escenarios de pérdida material las amenazan, según los adversarios relevantes para nuestro sector y país? (vínculo `M2.1-K08`).
- `PC-037`: ¿Sabemos dónde están nuestros datos sensibles, quién accede a ellos y cuán sobreexpuestos están? (vínculo `AMP-31`).
- `PC-038`: ¿Tenemos una taxonomía de clasificación aprobada, aplicada automáticamente y comprensible para los usuarios? (vínculo `M2.1-K02`).
- `PC-041`: ¿Retenemos solo lo necesario, eliminamos lo obsoleto y podemos responder a requerimientos legales y de titulares de datos? (vínculo `M2.1-K06`).
- `PC-042`: ¿Cómo gestionamos claves, secretos y certificados (custodia, rotación, separación de funciones, módulos de seguridad de hardware)? (vínculo `M2.1-K05`).
- `PC-043`: ¿Tenemos un inventario criptográfico y una hoja de ruta hacia la criptografía poscuántica, con fechas y dependencias de proveedores? (vínculo `M2.1-K05`).

**Serie de banco construida desde plantillas documentadas (muestras):**
- `BM-0421` — ¿Qué problema de gobierno, riesgo o capacidad intenta resolver realmente «Identificación Activos», y qué decisión debería mejorar si se comprende correctamente?
- `BM-0422` — ¿Qué supuesto habitual sobre «Identificación Activos» podría ser falso o incompleto, y qué consecuencia tendría diseñar la seguridad como si fuera cierto?
- `BM-0424` — ¿Qué problema de gobierno, riesgo o capacidad intenta resolver realmente «Clasificación», y qué decisión debería mejorar si se comprende correctamente?
- `BM-0425` — ¿Qué supuesto habitual sobre «Clasificación» podría ser falso o incompleto, y qué consecuencia tendría diseñar la seguridad como si fuera cierto?
- `BM-1001` — ¿Qué problema de gobierno, riesgo o capacidad intenta resolver realmente «DSPM», y qué decisión debería mejorar si se comprende correctamente?
- `BM-1002` — ¿Qué supuesto habitual sobre «DSPM» podría ser falso o incompleto, y qué consecuencia tendría diseñar la seguridad como si fuera cierto?

**Tesis propuestas por pregunta asignadas explícitamente a esta unidad: 10.**
- [APC-042 — Custodia y rotación de claves, secretos y certificados](../../03_metodo_mayeutico/01_tesis_derivadas/APC-042.md) ← `PC-042`
- [APC-043 — Inventario criptográfico y hoja de ruta poscuántica](../../03_metodo_mayeutico/01_tesis_derivadas/APC-043.md) ← `PC-043`
- [APC-118 — Inventario único de activos de IA con dueño y criticidad](../../03_metodo_mayeutico/01_tesis_derivadas/APC-118.md) ← `PC-118`
- [APC-142 — Protección de memoria, contexto e índices vectoriales de agentes](../../03_metodo_mayeutico/01_tesis_derivadas/APC-142.md) ← `PC-142`
- [APC-215 — Migración poscuántica priorizada desde el inventario criptográfico](../../03_metodo_mayeutico/01_tesis_derivadas/APC-215.md) ← `PC-215`
- [APA-062 — Retención y acceso a registros de interacciones con IA](../../03_metodo_mayeutico/01_tesis_derivadas/APA-062.md) ← `PA-062`
- [APA-070 — Protección y trazabilidad del acceso a datos de clientes](../../03_metodo_mayeutico/01_tesis_derivadas/APA-070.md) ← `PA-070`
- [APA-116 — Protección de datos de larga vida frente al descifrado cuántico](../../03_metodo_mayeutico/01_tesis_derivadas/APA-116.md) ← `PA-116`

**Tesis transversales relacionadas sin asignación principal (muestras):**
- [APC-039](../../03_metodo_mayeutico/01_tesis_derivadas/APC-039.md) (relación transversal, no asignación principal)
- [APC-176](../../03_metodo_mayeutico/01_tesis_derivadas/APC-176.md) (relación transversal, no asignación principal)
- [APC-182](../../03_metodo_mayeutico/01_tesis_derivadas/APC-182.md) (relación transversal, no asignación principal)
- [APA-037](../../03_metodo_mayeutico/01_tesis_derivadas/APA-037.md) (relación transversal, no asignación principal)
- [APA-057](../../03_metodo_mayeutico/01_tesis_derivadas/APA-057.md) (relación transversal, no asignación principal)

El banco completo conserva 543 preguntas originales y 2.395 preguntas derivadas mecánicamente de plantillas; 308 tesis AP forman un **anexo provisional**, distinto de los 331 conceptos del corpus de trabajo.

## Lecturas, investigación y modalidad

**Lecturas internas verificables:**
- [Documento Maestro](../../../Curado02/01_noviembre_2026/src-thenextciso-gm-24-documento-maestro__9b8c53df319d.md), unidad `M2.1` desde línea 638.
- [lote de ideas base](../../../Curado02/01_noviembre_2026/src-thenextciso-gm-24-ensayos-base-121150__54712613f117.md)
- Las 51 tesis Atlas [P] proceden de `06Ensayos!I285:I335` en [matriz de pre-ensayos](../../../Curado02/01_noviembre_2026/src-ai-ciso-atlas-ensayos-thenextciso-x-core-accountabilities-fy27-2026-11-05__5528a05eb5dd.xlsx).

**Lecturas complementarias por cotejar:** NIST CSF 2.0, NIST RMF y dominios CISM/CRISC según la unidad y las fuentes listadas por el Documento Maestro. El mapeo de este documento es una propuesta temática: `CISM C3; CRISC R2,R4; NIST CSF 2.0 ID.AM,PR.DS; NIST RMF Categorize,Select,Implement.`. La fuente oficial, edición y pertinencia deben comprobarse al preparar cada clase; no se presume cobertura íntegra de examen o norma.

**Recursos audiovisuales:** no se identificó un video específico, vigente y verificable por unidad en los documentos base. Existe un [inventario complementario de enlaces observados](../../../Biblioteca_CISO_Frontera/Consolidado_2026_MM_2026-11-11/03_programa_1200h/Videos_Observados_en_Fuentes.md), aún sin comprobación de contenido, disponibilidad, duración ni correspondencia con esta unidad. El equipo docente deberá seleccionarlos, comprobar derechos y documentar el vínculo antes de asignarlos.

**Carga de diseño:** 31 h por unidad; 24 unidades más capstone integrador de 56 h = escenario de 800 h. No es acreditación.

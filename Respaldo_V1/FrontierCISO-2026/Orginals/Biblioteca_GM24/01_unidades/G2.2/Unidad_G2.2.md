<!-- generado-gm24 sha256:6637abfe17554dcb9f42d68381a1c67e3a764028e43006829db7602c6675a68f -->
# G2.2 — Ciclo de Vida de Políticas, Estándares y Procedimientos

**Pilar:** Gobierno · **Eje:** Marcos normativos y políticos · **Atlas:** `D01,D03` (alineación editorial, no identidad de dominio).

**Pregunta rectora de fuente:** ¿Cómo puede un CISO definir y supervisar ciclo de vida de políticas, estándares y procedimientos sin perder de vista el riesgo empresarial, las responsabilidades y la evidencia?

**Alcance:** diez conceptos base con idea central desarrollada; 2 ampliaciones Atlas cuyo título pertenece al Documento Maestro y cuya tesis es propuesta [P]. Los puentes HC relacionados son candidatos transversales; ninguna extensión altera por sí sola el número de unidades.

## Situación longitudinal y decisión

**Organización ficticia:** Una política como código deshabilita credenciales de agentes, pero una excepción permanente deja abierto el acceso de emergencia.

**Decisión a sostener:** Diseñar aprobación, caducidad, rollback y prueba de eficacia de la excepción automatizada.

**Cursos de acción en tensión:** Excepciones sin vencimiento frente a excepciones con dueño, compensación y revisión automática.

**Información inicial:** política aprobada, repositorio de versiones, registros de excepción

**Interesados:** riesgo, ingeniería, mesa de ayuda y auditoría

**Producto acumulativo:** jerarquía documental y flujo de cambios con control de excepciones

**Regla de seguridad y responsabilidad:** Un cambio en producción no hereda autoridad de un commit técnico ni elimina el deber de supervisión.

## Desarrollo de los diez conceptos base

### G2.2-K01 — Jerarquía Documental

La jerarquía documental ordena políticas, estándares, procedimientos, guías y registros según su autoridad, nivel de detalle y destinatario. La tensión que merece análisis es que una política estratégica se confunde con una instrucción operativa y termina siendo imposible de aplicar o auditar La cuestión no se resuelve únicamente redactando un documento o adquiriendo una plataforma. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/G2.2-K01.md) (427 palabras de borrador, no ensayo final).

### G2.2-K02 — Desarrollo de Políticas

Desarrollar políticas implica traducir objetivos, obligaciones y apetito de riesgo en reglas organizacionales claras, legítimas y sostenibles. La tensión que merece análisis es que un documento se aprueba por cumplimiento formal sin consultar a quienes deberán aplicarlo ni evaluar sus efectos La cuestión no se resuelve únicamente redactando un documento o adquiriendo una plataforma. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/G2.2-K02.md) (429 palabras de borrador, no ensayo final).

### G2.2-K03 — Estándares de Seguridad

Los estándares convierten principios de política en requisitos verificables para arquitecturas, plataformas, procesos y proveedores. La tensión que merece análisis es que se confunde un estándar corporativo con una configuración única, ignorando distintas tecnologías y riesgos La cuestión no se resuelve únicamente redactando un documento o adquiriendo una plataforma. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/G2.2-K03.md) (421 palabras de borrador, no ensayo final).

### G2.2-K04 — Procedimientos

Los procedimientos especifican actividades, secuencias, responsables y puntos de control que permiten ejecutar una política de manera consistente. La tensión que merece análisis es que el procedimiento puede quedar obsoleto antes que la política o depender de personas que no están disponibles La cuestión no se resuelve únicamente redactando un documento o adquiriendo una plataforma. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/G2.2-K04.md) (423 palabras de borrador, no ensayo final).

### G2.2-K05 — Comunicación

La comunicación de políticas debe crear comprensión de propósito, conducta esperada y consecuencias, no limitarse a distribuir documentos. La tensión que merece análisis es que los empleados pueden aceptar formalmente reglas que no entienden o que contradicen sus incentivos La cuestión no se resuelve únicamente redactando un documento o adquiriendo una plataforma. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/G2.2-K05.md) (416 palabras de borrador, no ensayo final).

### G2.2-K06 — Aplicación (Enforcement)

La aplicación de políticas combina mecanismos técnicos, responsabilidades, supervisión y respuesta proporcional ante incumplimientos. La tensión que merece análisis es que una regla estricta puede bloquear procesos esenciales o generar rutas informales para eludir controles La cuestión no se resuelve únicamente redactando un documento o adquiriendo una plataforma. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/G2.2-K06.md) (420 palabras de borrador, no ensayo final).

### G2.2-K07 — Mantenimiento

Mantener políticas y estándares implica revisar su vigencia frente a cambios tecnológicos, legales, organizacionales y de amenazas. La tensión que merece análisis es que las revisiones periódicas pueden convertirse en trámite mientras las capacidades cambian rápidamente La cuestión no se resuelve únicamente redactando un documento o adquiriendo una plataforma. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/G2.2-K07.md) (417 palabras de borrador, no ensayo final).

### G2.2-K08 — Control de Versiones

El control de versiones preserva la historia de decisiones, definiciones, aprobaciones y vigencia de cada documento normativo. La tensión que merece análisis es que una versión más reciente puede difundirse parcialmente mientras equipos siguen ejecutando la anterior La cuestión no se resuelve únicamente redactando un documento o adquiriendo una plataforma. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/G2.2-K08.md) (422 palabras de borrador, no ensayo final).

### G2.2-K09 — Excepciones

Las excepciones permiten tratar casos donde un requisito no puede cumplirse, mediante evaluación de riesgo, autoridad y vigencia delimitada. La tensión que merece análisis es que la excepción puede convertirse en permiso indefinido o en una aprobación del CISO sin autoridad de riesgo La cuestión no se resuelve únicamente redactando un documento o adquiriendo una plataforma. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/G2.2-K09.md) (423 palabras de borrador, no ensayo final).

### G2.2-K10 — Rol de Auditoría

La auditoría aporta revisión independiente sobre diseño, aplicación y efectividad de políticas sin asumir responsabilidad de operar los controles. La tensión que merece análisis es que se confunde la opinión de auditoría con aprobación de riesgo o se transforma al auditor en dueño del proceso La cuestión no se resuelve únicamente redactando un documento o adquiriendo una plataforma. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/G2.2-K10.md) (427 palabras de borrador, no ensayo final).

## Ampliaciones Atlas de esta unidad: tesis para discutir, no definiciones aprobadas

- **[AMP-09 — Policy-as-code](../../02_conceptos/02_ampliaciones_atlas/AMP-09.md) [P].** Expresar políticas como código vuelve verificable su aplicación, pero exige control de versiones, gestión de excepciones y revisión humana para cambios de alto impacto. Vínculo propuesto: `HC-004`; fuente `06Ensayos!I293`.
- **[AMP-10 — Gobierno de excepciones automatizadas](../../02_conceptos/02_ampliaciones_atlas/AMP-10.md) [P].** Cuando las excepciones se conceden y vencen automáticamente, la automatización puede normalizar el desvío; se requieren dueño, caducidad y evidencia. Vínculo propuesto: `HC-028`; fuente `06Ensayos!I294`.

## Conceptos híbridos candidatos que conectan esta unidad

- [HC-004 — Política como código gobernado](../../02_conceptos/03_hibridos_candidatos/HC-004.md): conecta `G2.2-K02`, `G2.2-K09`, `G3.2-K07`, `M3.2-K05`. **Candidato**, no unidad ni arista aprobada.
- [HC-013 — Deuda de seguridad como riesgo de transformación](../../02_conceptos/03_hibridos_candidatos/HC-013.md): conecta `G2.2-K09`, `M1.2-K02`, `M3.1-K01`, `G1.2-K08`. **Candidato**, no unidad ni arista aprobada.
- [HC-015 — Gobierno y operación de Zero Trust](../../02_conceptos/03_hibridos_candidatos/HC-015.md): conecta `G2.2-K03`, `M2.2-K05`, `M3.1-K03`, `M3.2-K09`. **Candidato**, no unidad ni arista aprobada.
- [HC-028 — Gestión de excepciones y compensaciones](../../02_conceptos/03_hibridos_candidatos/HC-028.md): conecta `G2.2-K09`, `G5.2-K03`, `M3.2-K07`, `M3.2-K10`. **Candidato**, no unidad ni arista aprobada.
- [HC-035 — Aprendizaje desde incidentes hasta políticas](../../02_conceptos/03_hibridos_candidatos/HC-035.md): conecta `M5.2-K05`, `M1.1-K10`, `G2.2-K07`, `G1.2-K01`. **Candidato**, no unidad ni arista aprobada.
- [HC-038 — Aseguramiento de la arquitectura Zero Trust](../../02_conceptos/03_hibridos_candidatos/HC-038.md): conecta `G2.2-K03`, `M2.2-K05`, `M3.1-K03`, `M3.2-K04`. **Candidato**, no unidad ni arista aprobada.

## Puente con TheMetaCognitiveCISO

Se propone entrenar la lente cognitiva `DP-0034` junto a las decisiones de `G2.2`. Esta es una **relación pedagógica derivada**, no una equivalencia canónica con el GM-24. Consulte [la caja cognitiva del CISO](../../../Biblioteca_CISO_Frontera/Caja_Cognitiva_CISO_72/00_Indice.md) para la ficha y su evidencia.

## Laboratorio: ocho modalidades de ejercicio

Las tareas comparten el mismo caso; no son ocho horas añadidas por separado. Se practican en la asignación indicativa de 3 h de seminario, 8 h de investigación y lectura, 12 h de laboratorio y 8 h de aplicación por unidad. Los tiempos requieren aprobación académica.

### 1. Comprensión conceptual

**Consigna:** Define `G2.2-K02` (Desarrollo de Políticas) y `G2.2-K09` (Excepciones) con tus palabras. Señala una frontera de responsabilidad, una confusión habitual y cómo la ampliación `AMP-09` altera la interpretación del caso «Una política como código deshabilita credenciales de agentes, pero una excepción permanente deja abierto el acceso de emergencia.».

**Producto:** cuadro de contraste con dos decisiones distintas y citas a las fichas.

**Comprobación:** No declara como sinónimos dos títulos vecinos ni toma la tesis [P] como definición aprobada.

### 2. Relaciones y contextualización

**Consigna:** Dibuja la cadena de decisiones entre `G2.2-K02`, `G2.2-K09`, `AMP-09` y `HC-004` — Política como código gobernado. Anota en cada conexión dirección, evidencia textual, posible solapamiento y qué cambiaría al variar el contexto de negocio. Las aristas nuevas son hipótesis hasta que se validen.

**Producto:** mapa de relaciones G–M y tabla de procedencia de cada enlace.

**Comprobación:** No transforma cercanía temática en causalidad ni convierte HC en requisito aprobado.

### 3. Práctica aplicada

**Consigna:** Trabaja en «Una política como código deshabilita credenciales de agentes, pero una excepción permanente deja abierto el acceso de emergencia.». Con política aprobada, repositorio de versiones, registros de excepción, construye jerarquía documental y flujo de cambios con control de excepciones; incluye propietario, condiciones de entrada y salida, hipótesis adversa y prueba de funcionamiento.

**Producto:** jerarquía documental y flujo de cambios con control de excepciones.

**Comprobación:** Un cambio en producción no hereda autoridad de un commit técnico ni elimina el deber de supervisión.

### 4. Investigación y fuentes

**Consigna:** Investiga esta pregunta acotada: comparar la política vigente con una regla ejecutable y enumerar lo que el código no puede decidir. Localiza al menos dos fuentes primarias con fecha y versión; distingue obligación, recomendación, definición, ejemplo y opinión.

**Producto:** ficha de fuentes con extractos breves, localizador y discrepancias.

**Comprobación:** No cita un borrador editorial o mapeo informativo como norma obligatoria.

### 5. Orquestación de actores y agentes

**Consigna:** Con riesgo, ingeniería, mesa de ayuda y auditoría, construye un flujo de tres hitos para «Diseñar aprobación, caducidad, rollback y prueba de eficacia de la excepción automatizada.». Define qué puede proponer un agente, qué requiere aprobación humana, quién responde y cómo detener, registrar y revertir una acción errónea.

**Producto:** RACI/DACI, diagrama de traspasos y plan de supervisión.

**Comprobación:** Hay autoridad, trazas y camino de escalamiento para cada acción de alto impacto.

### 6. Análisis y contrafactual

**Consigna:** Compara «Excepciones sin vencimiento frente a excepciones con dueño, compensación y revisión automática.» usando datos de política aprobada, repositorio de versiones, registros de excepción. Contrasta la primera impresión con la lente cognitiva `DP-0034` del programa metacognitivo; plantea qué evidencia falsaría cada hipótesis y un efecto de segundo orden.

**Producto:** matriz de alternativas, incertidumbres y pruebas refutatorias.

**Comprobación:** La comparación conserva supuestos, costos de reversión y consecuencias no observadas.

### 7. Toma de decisiones

**Consigna:** Redacta para el responsable competente una recomendación sobre «Diseñar aprobación, caducidad, rollback y prueba de eficacia de la excepción automatizada.», con dos opciones, beneficio, riesgo residual, autoridad de aceptación, indicador temprano y condición explícita de pausa o rollback.

**Producto:** memorando ejecutivo de una página más expediente de evidencia.

**Comprobación:** Un cambio en producción no hereda autoridad de un commit técnico ni elimina el deber de supervisión.

### 8. Exposición y defensa

**Consigna:** Defiende la decisión ante riesgo, ingeniería, mesa de ayuda y auditoría en siete minutos; reserva tres para objeciones. Un par cambia un dato del escenario a mitad de la exposición: revisa la postura sin ocultar el supuesto que deja de sostenerse.

**Producto:** presentación oral, preguntas difíciles y registro de revisiones.

**Comprobación:** La defensa distingue certeza, incertidumbre, decisión y propiedad del riesgo.

## Rúbrica formativa y evidencia de logro

| Criterio | 0 — insuficiente | 2 — parcial | 4 — sólido |
|---|---|---|---|
| Precisión | Confunde conceptos, categorías o estados editoriales | Explica definiciones sin límites | Distingue base, propuesta y candidato; explica límites y relaciones sin equivalencias ficticias |
| Evidencia | Cita sin procedencia ni prueba | Traza fuentes pero no su calidad | Localiza fuente, versión, modalidad, incertidumbre y prueba de eficacia |
| Decisión y autoridad | No compara opciones ni propietario | Compara pero sin residual o escalamiento | Justifica alternativas, derecho de decisión, residual, parada y revisión |
| Transferencia | Entrega teórica sin caso | Caso parcial sin contraprueba | Artefacto operable, prueba adversa y defensa ajustada a la audiencia |

**Condición crítica de esta unidad:** Un cambio en producción no hereda autoridad de un commit técnico ni elimina el deber de supervisión. La práctica se devuelve para revisión si incumple este criterio, aunque el promedio sea alto. Para aprendizaje se propone al menos 3/4 en cada dimensión; no es una acreditación aprobada.

## Preguntas mayéuticas, sin confundirlas con afirmaciones

**Pregunta original consolidada (muestras):**
- `PC-005`: ¿Nuestras políticas de seguridad son pocas, vigentes, comprensibles y verificables, y cómo detectamos su incumplimiento? (vínculo `G2.2-K02`).
- `PC-049`: ¿Están definidas y aplicadas configuraciones seguras de referencia, y cómo detectamos y corregimos los desvíos? (vínculo `G2.2-K03`).
- `PN-34`: ¿Las reglas sobre qué datos se pueden escribir o subir a cada herramienta de IA se aplican con controles técnicos en el navegador, el endpoint y la red, o dependen solo de la política? (vínculo `G2.2-K06`).

**Serie de banco construida desde plantillas documentadas (muestras):**
- `BM-0091` — ¿Qué problema de gobierno, riesgo o capacidad intenta resolver realmente «Jerarquía Documental», y qué decisión debería mejorar si se comprende correctamente?
- `BM-0092` — ¿Qué supuesto habitual sobre «Jerarquía Documental» podría ser falso o incompleto, y qué consecuencia tendría diseñar la seguridad como si fuera cierto?
- `BM-0094` — ¿Qué problema de gobierno, riesgo o capacidad intenta resolver realmente «Desarrollo de Políticas», y qué decisión debería mejorar si se comprende correctamente?
- `BM-0095` — ¿Qué supuesto habitual sobre «Desarrollo de Políticas» podría ser falso o incompleto, y qué consecuencia tendría diseñar la seguridad como si fuera cierto?
- `BM-0913` — ¿Qué problema de gobierno, riesgo o capacidad intenta resolver realmente «Policy-as-code», y qué decisión debería mejorar si se comprende correctamente?
- `BM-0914` — ¿Qué supuesto habitual sobre «Policy-as-code» podría ser falso o incompleto, y qué consecuencia tendría diseñar la seguridad como si fuera cierto?

**Tesis propuestas por pregunta asignadas explícitamente a esta unidad: 2.**
- [APC-049 — Configuraciones seguras de referencia y corrección de desvíos](../../03_metodo_mayeutico/01_tesis_derivadas/APC-049.md) ← `PC-049`
- [APN-34 — Aplicación técnica de reglas de datos por herramienta de IA](../../03_metodo_mayeutico/01_tesis_derivadas/APN-34.md) ← `PN-34`

**Tesis transversales relacionadas sin asignación principal (muestras):**
- [APC-023](../../03_metodo_mayeutico/01_tesis_derivadas/APC-023.md) (relación transversal, no asignación principal)
- [APC-050](../../03_metodo_mayeutico/01_tesis_derivadas/APC-050.md) (relación transversal, no asignación principal)
- [APC-179](../../03_metodo_mayeutico/01_tesis_derivadas/APC-179.md) (relación transversal, no asignación principal)
- [APC-216](../../03_metodo_mayeutico/01_tesis_derivadas/APC-216.md) (relación transversal, no asignación principal)
- [APC-256](../../03_metodo_mayeutico/01_tesis_derivadas/APC-256.md) (relación transversal, no asignación principal)

El banco completo conserva 543 preguntas originales y 2.395 preguntas derivadas mecánicamente de plantillas; 308 tesis AP forman un **anexo provisional**, distinto de los 331 conceptos del corpus de trabajo.

## Lecturas, investigación y modalidad

**Lecturas internas verificables:**
- [Documento Maestro](../../../Curado02/01_noviembre_2026/src-thenextciso-gm-24-documento-maestro__9b8c53df319d.md), unidad `G2.2` desde línea 187.
- [lote de ideas base](../../../Curado02/01_noviembre_2026/src-thenextciso-gm-24-ensayos-base-031060__d65b02f13325.md)
- Las 51 tesis Atlas [P] proceden de `06Ensayos!I285:I335` en [matriz de pre-ensayos](../../../Curado02/01_noviembre_2026/src-ai-ciso-atlas-ensayos-thenextciso-x-core-accountabilities-fy27-2026-11-05__5528a05eb5dd.xlsx).

**Lecturas complementarias por cotejar:** NIST CSF 2.0, NIST RMF y dominios CISM/CRISC según la unidad y las fuentes listadas por el Documento Maestro. El mapeo de este documento es una propuesta temática: `CISM C1,C3; CRISC R1,R3; NIST CSF 2.0 GV.PO,GV.OV; NIST RMF Prepare,Monitor.`. La fuente oficial, edición y pertinencia deben comprobarse al preparar cada clase; no se presume cobertura íntegra de examen o norma.

**Recursos audiovisuales:** no se identificó un video específico, vigente y verificable por unidad en los documentos base. Existe un [inventario complementario de enlaces observados](../../../Biblioteca_CISO_Frontera/Consolidado_2026_MM_2026-11-11/03_programa_1200h/Videos_Observados_en_Fuentes.md), aún sin comprobación de contenido, disponibilidad, duración ni correspondencia con esta unidad. El equipo docente deberá seleccionarlos, comprobar derechos y documentar el vínculo antes de asignarlos.

**Carga de diseño:** 31 h por unidad; 24 unidades más capstone integrador de 56 h = escenario de 800 h. No es acreditación.

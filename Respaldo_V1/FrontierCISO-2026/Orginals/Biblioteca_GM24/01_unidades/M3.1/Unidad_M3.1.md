<!-- generado-gm24 sha256:6bb1167dd67d44deafc68e4f175e4b484c34c688a38635c97478a2b9a98ba35f -->
# M3.1 — Arquitectura de Seguridad, Ingeniería y Diseño (Incl. Zero Trust)

**Pilar:** Gestión · **Eje:** Arquitectura y controles técnicos · **Atlas:** `D08,D10,D11` (alineación editorial, no identidad de dominio).

**Pregunta rectora de fuente:** ¿Cómo puede un CISO diseñar, ejecutar y verificar arquitectura de seguridad, ingeniería y diseño (incl. zero trust) sin perder de vista el riesgo empresarial, las responsabilidades y la evidencia?

**Alcance:** diez conceptos base con idea central desarrollada; 2 ampliaciones Atlas cuyo título pertenece al Documento Maestro y cuya tesis es propuesta [P]. Los puentes HC relacionados son candidatos transversales; ninguna extensión altera por sí sola el número de unidades.

## Situación longitudinal y decisión

**Organización ficticia:** Un agente puede invocar conectores de correo, endpoints y repositorios desde un mismo plano de control sin separación de permisos.

**Decisión a sostener:** Diseñar límites de confianza, aislamiento y puntos de observación antes de producción.

**Cursos de acción en tensión:** Acceso amplio para acelerar integración frente a herramientas acotadas por identidad, entorno y riesgo.

**Información inicial:** diagrama de flujos, permisos de herramientas, dependencias y requisitos de rollback

**Interesados:** arquitectos de plataforma, ingeniería y seguridad de aplicaciones

**Producto acumulativo:** arquitectura de agentes con threat model y controles por límite

**Regla de seguridad y responsabilidad:** La separación de funciones y el mínimo privilegio se prueban, no se infieren del diagrama.

## Desarrollo de los diez conceptos base

### M3.1-K01 — Arquitectura de Seguridad

La arquitectura de seguridad organiza principios, patrones, componentes y decisiones para que los sistemas alcancen resultados verificables. El escenario que conviene examinar es el siguiente: cada proyecto incorpora controles incompatibles y sin modelo de confianza común. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M3.1-K01.md) (441 palabras de borrador, no ensayo final).

### M3.1-K02 — Ingeniería de Seguridad

La ingeniería de seguridad traduce requisitos de riesgo en mecanismos implementables, medibles y sostenibles durante el ciclo de vida. El escenario que conviene examinar es el siguiente: los controles se diseñan sin capacidad de operación ni pruebas. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M3.1-K02.md) (443 palabras de borrador, no ensayo final).

### M3.1-K03 — Zero Trust (Arquitectura)

Zero Trust como arquitectura distribuye decisiones continuas de acceso y protección entre identidades, dispositivos, aplicaciones, redes y datos. El escenario que conviene examinar es el siguiente: una iniciativa solo reemplaza la VPN sin revisar autorizaciones ni protección de datos. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M3.1-K03.md) (442 palabras de borrador, no ensayo final).

### M3.1-K04 — Diseño Seguro (SbD)

Secure by Design incorpora requisitos de seguridad desde decisiones iniciales de producto, evitando trasladar riesgos innecesarios a usuarios y operadores. El escenario que conviene examinar es el siguiente: el equipo descubre amenazas críticas después del despliegue. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M3.1-K04.md) (441 palabras de borrador, no ensayo final).

### M3.1-K05 — TOGAF y Seguridad

TOGAF puede conectar arquitectura empresarial y seguridad al relacionar capacidades, procesos, datos, aplicaciones y tecnología con decisiones de gobierno. El escenario que conviene examinar es el siguiente: la arquitectura se documenta como inventario de componentes sin resultados empresariales. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M3.1-K05.md) (442 palabras de borrador, no ensayo final).

### M3.1-K06 — ZTNA (Acceso)

El diseño de acceso Zero Trust para aplicaciones privadas exige políticas por identidad y contexto, aislamiento y continuidad operativa. El escenario que conviene examinar es el siguiente: se implementa ZTNA sin contemplar dependencias de aplicaciones heredadas. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M3.1-K06.md) (437 palabras de borrador, no ensayo final).

### M3.1-K07 — Microsegmentación

La microsegmentación limita movimientos laterales y propagación mediante límites de comunicación basados en dependencias reales. El escenario que conviene examinar es el siguiente: reglas demasiado estrictas interrumpen servicios y reglas amplias mantienen rutas de ataque. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M3.1-K07.md) (434 palabras de borrador, no ensayo final).

### M3.1-K08 — Defensa en Profundidad

La defensa en profundidad combina controles complementarios para reducir fallas comunes y limitar consecuencias cuando una barrera no funciona. El escenario que conviene examinar es el siguiente: varias herramientas dependen de la misma identidad comprometida y generan falsa redundancia. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M3.1-K08.md) (444 palabras de borrador, no ensayo final).

### M3.1-K09 — Mínimo Privilegio (Arquitectura)

El mínimo privilegio debe diseñarse en identidades, APIs, herramientas, datos y procesos con mecanismos de revisión y revocación. El escenario que conviene examinar es el siguiente: un agente hereda permisos globales para simplificar una integración. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M3.1-K09.md) (440 palabras de borrador, no ensayo final).

### M3.1-K10 — Resiliencia (Diseño)

La resiliencia por diseño incorpora degradación controlada, aislamiento, recuperación y observabilidad desde la arquitectura inicial. El escenario que conviene examinar es el siguiente: un servicio crítico carece de ruta de recuperación ante pérdida de proveedor. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M3.1-K10.md) (436 palabras de borrador, no ensayo final).

## Ampliaciones Atlas de esta unidad: tesis para discutir, no definiciones aprobadas

- **[AMP-35 — Arquitectura de sistemas agénticos](../../02_conceptos/02_ampliaciones_atlas/AMP-35.md) [P].** Diseñar sistemas agénticos seguros implica separar planificación, herramientas, datos y permisos, con puntos de control y observabilidad desde el diseño. Vínculo propuesto: `M6.2-K04`; fuente `06Ensayos!I319`.
- **[AMP-36 — Límites de herramientas y permisos](../../02_conceptos/02_ampliaciones_atlas/AMP-36.md) [P].** Las herramientas y conectores definen lo que un agente puede hacer: acotar alcances, aprobar acciones de alto impacto y registrar cada invocación. Vínculo propuesto: `M3.1-K09`; fuente `06Ensayos!I320`.

## Conceptos híbridos candidatos que conectan esta unidad

- [HC-002 — Apetito de riesgo convertido en arquitectura](../../02_conceptos/03_hibridos_candidatos/HC-002.md): conecta `G4.2-K01`, `G4.2-K02`, `M3.1-K01`, `M3.2-K03`. **Candidato**, no unidad ni arista aprobada.
- [HC-010 — Autonomía delegada y límites de acción](../../02_conceptos/03_hibridos_candidatos/HC-010.md): conecta `G4.2-K05`, `M2.2-K03`, `M3.1-K09`, `M4.1-K08`. **Candidato**, no unidad ni arista aprobada.
- [HC-013 — Deuda de seguridad como riesgo de transformación](../../02_conceptos/03_hibridos_candidatos/HC-013.md): conecta `G2.2-K09`, `M1.2-K02`, `M3.1-K01`, `G1.2-K08`. **Candidato**, no unidad ni arista aprobada.
- [HC-014 — Arquitectura de riesgo empresarial](../../02_conceptos/03_hibridos_candidatos/HC-014.md): conecta `G1.2-K07`, `G4.1-K06`, `M3.1-K05`, `M2.1-K08`. **Candidato**, no unidad ni arista aprobada.
- [HC-015 — Gobierno y operación de Zero Trust](../../02_conceptos/03_hibridos_candidatos/HC-015.md): conecta `G2.2-K03`, `M2.2-K05`, `M3.1-K03`, `M3.2-K09`. **Candidato**, no unidad ni arista aprobada.
- [HC-023 — Riesgo de concentración tecnológica](../../02_conceptos/03_hibridos_candidatos/HC-023.md): conecta `M6.1-K10`, `M6.2-K08`, `M3.1-K10`, `G1.2-K05`. **Candidato**, no unidad ni arista aprobada.
- [HC-030 — Seguridad industrial y continuidad de negocio](../../02_conceptos/03_hibridos_candidatos/HC-030.md): conecta `M6.2-K05`, `M3.1-K07`, `M5.1-K02`, `M6.1-K05`. **Candidato**, no unidad ni arista aprobada.
- [HC-034 — Decisiones reversibles y riesgo de transición](../../02_conceptos/03_hibridos_candidatos/HC-034.md): conecta `G1.2-K08`, `M3.2-K05`, `M3.1-K10`, `G5.2-K07`. **Candidato**, no unidad ni arista aprobada.
- [HC-038 — Aseguramiento de la arquitectura Zero Trust](../../02_conceptos/03_hibridos_candidatos/HC-038.md): conecta `G2.2-K03`, `M2.2-K05`, `M3.1-K03`, `M3.2-K04`. **Candidato**, no unidad ni arista aprobada.
- [HC-040 — Homeostasis organizacional de seguridad](../../02_conceptos/03_hibridos_candidatos/HC-040.md): conecta `G4.2-K02`, `M4.1-K02`, `G1.1-K05`, `M3.1-K10`. **Candidato**, no unidad ni arista aprobada.

## Puente con TheMetaCognitiveCISO

Se propone entrenar la lente cognitiva `MM-0021` junto a las decisiones de `M3.1`. Esta es una **relación pedagógica derivada**, no una equivalencia canónica con el GM-24. Consulte [la caja cognitiva del CISO](../../../Biblioteca_CISO_Frontera/Caja_Cognitiva_CISO_72/00_Indice.md) para la ficha y su evidencia.

## Laboratorio: ocho modalidades de ejercicio

Las tareas comparten el mismo caso; no son ocho horas añadidas por separado. Se practican en la asignación indicativa de 3 h de seminario, 8 h de investigación y lectura, 12 h de laboratorio y 8 h de aplicación por unidad. Los tiempos requieren aprobación académica.

### 1. Comprensión conceptual

**Consigna:** Define `M3.1-K01` (Arquitectura de Seguridad) y `M3.1-K09` (Mínimo Privilegio (Arquitectura)) con tus palabras. Señala una frontera de responsabilidad, una confusión habitual y cómo la ampliación `AMP-35` altera la interpretación del caso «Un agente puede invocar conectores de correo, endpoints y repositorios desde un mismo plano de control sin separación de permisos.».

**Producto:** cuadro de contraste con dos decisiones distintas y citas a las fichas.

**Comprobación:** No declara como sinónimos dos títulos vecinos ni toma la tesis [P] como definición aprobada.

### 2. Relaciones y contextualización

**Consigna:** Dibuja la cadena de decisiones entre `M3.1-K01`, `M3.1-K09`, `AMP-35` y `HC-038` — Aseguramiento de la arquitectura Zero Trust. Anota en cada conexión dirección, evidencia textual, posible solapamiento y qué cambiaría al variar el contexto de negocio. Las aristas nuevas son hipótesis hasta que se validen.

**Producto:** mapa de relaciones G–M y tabla de procedencia de cada enlace.

**Comprobación:** No transforma cercanía temática en causalidad ni convierte HC en requisito aprobado.

### 3. Práctica aplicada

**Consigna:** Trabaja en «Un agente puede invocar conectores de correo, endpoints y repositorios desde un mismo plano de control sin separación de permisos.». Con diagrama de flujos, permisos de herramientas, dependencias y requisitos de rollback, construye arquitectura de agentes con threat model y controles por límite; incluye propietario, condiciones de entrada y salida, hipótesis adversa y prueba de funcionamiento.

**Producto:** arquitectura de agentes con threat model y controles por límite.

**Comprobación:** La separación de funciones y el mínimo privilegio se prueban, no se infieren del diagrama.

### 4. Investigación y fuentes

**Consigna:** Investiga esta pregunta acotada: comparar arquitectura Zero Trust y defensa en profundidad sin tratarlas como sinónimos. Localiza al menos dos fuentes primarias con fecha y versión; distingue obligación, recomendación, definición, ejemplo y opinión.

**Producto:** ficha de fuentes con extractos breves, localizador y discrepancias.

**Comprobación:** No cita un borrador editorial o mapeo informativo como norma obligatoria.

### 5. Orquestación de actores y agentes

**Consigna:** Con arquitectos de plataforma, ingeniería y seguridad de aplicaciones, construye un flujo de tres hitos para «Diseñar límites de confianza, aislamiento y puntos de observación antes de producción.». Define qué puede proponer un agente, qué requiere aprobación humana, quién responde y cómo detener, registrar y revertir una acción errónea.

**Producto:** RACI/DACI, diagrama de traspasos y plan de supervisión.

**Comprobación:** Hay autoridad, trazas y camino de escalamiento para cada acción de alto impacto.

### 6. Análisis y contrafactual

**Consigna:** Compara «Acceso amplio para acelerar integración frente a herramientas acotadas por identidad, entorno y riesgo.» usando datos de diagrama de flujos, permisos de herramientas, dependencias y requisitos de rollback. Contrasta la primera impresión con la lente cognitiva `MM-0021` del programa metacognitivo; plantea qué evidencia falsaría cada hipótesis y un efecto de segundo orden.

**Producto:** matriz de alternativas, incertidumbres y pruebas refutatorias.

**Comprobación:** La comparación conserva supuestos, costos de reversión y consecuencias no observadas.

### 7. Toma de decisiones

**Consigna:** Redacta para el responsable competente una recomendación sobre «Diseñar límites de confianza, aislamiento y puntos de observación antes de producción.», con dos opciones, beneficio, riesgo residual, autoridad de aceptación, indicador temprano y condición explícita de pausa o rollback.

**Producto:** memorando ejecutivo de una página más expediente de evidencia.

**Comprobación:** La separación de funciones y el mínimo privilegio se prueban, no se infieren del diagrama.

### 8. Exposición y defensa

**Consigna:** Defiende la decisión ante arquitectos de plataforma, ingeniería y seguridad de aplicaciones en siete minutos; reserva tres para objeciones. Un par cambia un dato del escenario a mitad de la exposición: revisa la postura sin ocultar el supuesto que deja de sostenerse.

**Producto:** presentación oral, preguntas difíciles y registro de revisiones.

**Comprobación:** La defensa distingue certeza, incertidumbre, decisión y propiedad del riesgo.

## Rúbrica formativa y evidencia de logro

| Criterio | 0 — insuficiente | 2 — parcial | 4 — sólido |
|---|---|---|---|
| Precisión | Confunde conceptos, categorías o estados editoriales | Explica definiciones sin límites | Distingue base, propuesta y candidato; explica límites y relaciones sin equivalencias ficticias |
| Evidencia | Cita sin procedencia ni prueba | Traza fuentes pero no su calidad | Localiza fuente, versión, modalidad, incertidumbre y prueba de eficacia |
| Decisión y autoridad | No compara opciones ni propietario | Compara pero sin residual o escalamiento | Justifica alternativas, derecho de decisión, residual, parada y revisión |
| Transferencia | Entrega teórica sin caso | Caso parcial sin contraprueba | Artefacto operable, prueba adversa y defensa ajustada a la audiencia |

**Condición crítica de esta unidad:** La separación de funciones y el mínimo privilegio se prueban, no se infieren del diagrama. La práctica se devuelve para revisión si incumple este criterio, aunque el promedio sea alto. Para aprendizaje se propone al menos 3/4 en cada dimensión; no es una acreditación aprobada.

## Preguntas mayéuticas, sin confundirlas con afirmaciones

**Pregunta original consolidada (muestras):**
- `PC-019`: ¿Tenemos una arquitectura de referencia de seguridad de extremo a extremo, conectada a la arquitectura empresarial y gobernada en cada cambio relevante? (vínculo `M3.1-K01`).
- `PC-021`: ¿Qué principios de seguridad son obligatorios en el diseño (mínimo privilegio, segmentación, asumir compromiso, seguro por defecto) y quién verifica su cumplimiento? (vínculo `M3.1-K04`).
- `PC-022`: ¿Cómo segmentamos redes, entornos y planos de administración para limitar el movimiento lateral? (vínculo `M3.1-K07`).
- `PC-129`: ¿Aplicamos mínimo privilegio y agencia mínima a los agentes: solo los datos, herramientas y acciones necesarios para su propósito? (vínculo `AMP-36`).
- `PC-147`: ¿Limitamos las capacidades del modelo a lo que el caso de uso necesita y validamos sus salidas antes de que desencadenen acciones? (vínculo `AMP-36`).
- `PC-153`: ¿Conocemos los modos de falla propios de los sistemas agénticos (memoria envenenada, objetivos secuestrados, colusión entre agentes, fallos en cascada) y cuáles aplican a nuestros casos? (vínculo `AMP-35`).

**Serie de banco construida desde plantillas documentadas (muestras):**
- `BM-0481` — ¿Qué problema de gobierno, riesgo o capacidad intenta resolver realmente «Arquitectura de Seguridad», y qué decisión debería mejorar si se comprende correctamente?
- `BM-0482` — ¿Qué supuesto habitual sobre «Arquitectura de Seguridad» podría ser falso o incompleto, y qué consecuencia tendría diseñar la seguridad como si fuera cierto?
- `BM-0484` — ¿Qué problema de gobierno, riesgo o capacidad intenta resolver realmente «Ingeniería de Seguridad», y qué decisión debería mejorar si se comprende correctamente?
- `BM-0485` — ¿Qué supuesto habitual sobre «Ingeniería de Seguridad» podría ser falso o incompleto, y qué consecuencia tendría diseñar la seguridad como si fuera cierto?
- `BM-1017` — ¿Qué problema de gobierno, riesgo o capacidad intenta resolver realmente «Arquitectura de sistemas agénticos», y qué decisión debería mejorar si se comprende correctamente?
- `BM-1018` — ¿Qué supuesto habitual sobre «Arquitectura de sistemas agénticos» podría ser falso o incompleto, y qué consecuencia tendría diseñar la seguridad como si fuera cierto?

**Tesis propuestas por pregunta asignadas explícitamente a esta unidad: 6.**
- [APC-147 — Capacidad mínima del modelo y validación previa de salidas](../../03_metodo_mayeutico/01_tesis_derivadas/APC-147.md) ← `PC-147`
- [APC-153 — Análisis de modos de falla en sistemas agénticos propios](../../03_metodo_mayeutico/01_tesis_derivadas/APC-153.md) ← `PC-153`
- [APC-230 — Inventario agéntico con fronteras de confianza y dueños](../../03_metodo_mayeutico/01_tesis_derivadas/APC-230.md) ← `PC-230`
- [APC-262 — Control previo de acciones, bucles y escaladas entre agentes](../../03_metodo_mayeutico/01_tesis_derivadas/APC-262.md) ← `PC-262`
- [APA-131 — Condiciones de control para escalar agentes de IA](../../03_metodo_mayeutico/01_tesis_derivadas/APA-131.md) ← `PA-131`
- [APA-163 — Encadenamiento seguro de agentes propios y de terceros](../../03_metodo_mayeutico/01_tesis_derivadas/APA-163.md) ← `PA-163`

**Tesis transversales relacionadas sin asignación principal (muestras):**
- [APC-023](../../03_metodo_mayeutico/01_tesis_derivadas/APC-023.md) (relación transversal, no asignación principal)
- [APC-051](../../03_metodo_mayeutico/01_tesis_derivadas/APC-051.md) (relación transversal, no asignación principal)
- [APC-063](../../03_metodo_mayeutico/01_tesis_derivadas/APC-063.md) (relación transversal, no asignación principal)
- [APC-155](../../03_metodo_mayeutico/01_tesis_derivadas/APC-155.md) (relación transversal, no asignación principal)
- [APC-216](../../03_metodo_mayeutico/01_tesis_derivadas/APC-216.md) (relación transversal, no asignación principal)

El banco completo conserva 543 preguntas originales y 2.395 preguntas derivadas mecánicamente de plantillas; 308 tesis AP forman un **anexo provisional**, distinto de los 331 conceptos del corpus de trabajo.

## Lecturas, investigación y modalidad

**Lecturas internas verificables:**
- [Documento Maestro](../../../Curado02/01_noviembre_2026/src-thenextciso-gm-24-documento-maestro__9b8c53df319d.md), unidad `M3.1` desde línea 720.
- [lote de ideas base](../../../Curado02/01_noviembre_2026/src-thenextciso-gm24-ensayos-bases-151-180__be034906f333.md)
- Las 51 tesis Atlas [P] proceden de `06Ensayos!I285:I335` en [matriz de pre-ensayos](../../../Curado02/01_noviembre_2026/src-ai-ciso-atlas-ensayos-thenextciso-x-core-accountabilities-fy27-2026-11-05__5528a05eb5dd.xlsx).

**Lecturas complementarias por cotejar:** NIST CSF 2.0, NIST RMF y dominios CISM/CRISC según la unidad y las fuentes listadas por el Documento Maestro. El mapeo de este documento es una propuesta temática: `CISM C3; CRISC R4; NIST CSF 2.0 PR.PS,PR.AA,ID.RA; NIST RMF Prepare,Select,Implement.`. La fuente oficial, edición y pertinencia deben comprobarse al preparar cada clase; no se presume cobertura íntegra de examen o norma.

**Recursos audiovisuales:** no se identificó un video específico, vigente y verificable por unidad en los documentos base. Existe un [inventario complementario de enlaces observados](../../../Biblioteca_CISO_Frontera/Consolidado_2026_MM_2026-11-11/03_programa_1200h/Videos_Observados_en_Fuentes.md), aún sin comprobación de contenido, disponibilidad, duración ni correspondencia con esta unidad. El equipo docente deberá seleccionarlos, comprobar derechos y documentar el vínculo antes de asignarlos.

**Carga de diseño:** 31 h por unidad; 24 unidades más capstone integrador de 56 h = escenario de 800 h. No es acreditación.

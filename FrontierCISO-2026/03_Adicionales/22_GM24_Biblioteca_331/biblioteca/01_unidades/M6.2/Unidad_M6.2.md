<!-- generado-gm24 sha256:4e16089432903b7407b2da64394288edd08a99d3afdad07cc7f4d064dc44af59 -->
# M6.2 — Seguridad en Redes, Nube, Tecnologías Emergentes y SCRM

**Pilar:** Gestión · **Eje:** Resiliencia, tecnologías y cadena de suministro · **Atlas:** `D08,D10,D11,D17,D18,D19,D20,D23` (alineación editorial, no identidad de dominio).

**Pregunta rectora de fuente:** ¿Cómo puede un CISO diseñar, ejecutar y verificar seguridad en redes, nube, tecnologías emergentes y scrm sin perder de vista el riesgo empresarial, las responsabilidades y la evidencia?

**Alcance:** diez conceptos base con idea central desarrollada; 3 ampliaciones Atlas cuyo título pertenece al Documento Maestro y cuya tesis es propuesta [P]. Los puentes HC relacionados son candidatos transversales; ninguna extensión altera por sí sola el número de unidades.

## Situación longitudinal y decisión

**Organización ficticia:** Un modelo externo y un conector MCP actualizan silenciosamente dependencias; el proveedor delega controles que la empresa creía incluidos.

**Decisión a sostener:** Gobernar supply chain de modelos, postura de nube y responsabilidades de terceros.

**Cursos de acción en tensión:** Aceptar atestados genéricos frente a exigir procedencia, SBOM, permisos y pruebas de actualización.

**Información inicial:** contrato cloud, SBOM, inventario de conectores, rutas de datos y licencias

**Interesados:** compras, legal, ingeniería cloud y dueños de datos

**Producto acumulativo:** expediente de tercero con matriz de responsabilidad y plan de verificación

**Regla de seguridad y responsabilidad:** Responsabilidad compartida y licencias no se infieren del nombre comercial del servicio.

## Desarrollo de los diez conceptos base

### M6.2-K01 — C-SCRM (Cadena Suministro)

La gestión del riesgo de cadena de suministro examina dependencias, integridad, contratos y continuidad de proveedores y componentes. El escenario que conviene examinar es el siguiente: una evaluación inicial no detecta cambios posteriores de subproveedores. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M6.2-K01.md) (441 palabras de borrador, no ensayo final).

### M6.2-K02 — Seguridad Nube

La seguridad cloud combina responsabilidad compartida, identidad, configuración, datos y protección de workloads en arquitecturas dinámicas. El escenario que conviene examinar es el siguiente: se asume que el proveedor cubre todas las responsabilidades del cliente. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M6.2-K02.md) (436 palabras de borrador, no ensayo final).

### M6.2-K03 — DevSecOps

DevSecOps integra controles y evidencia de seguridad en desarrollo y entrega continua sin convertir cada pipeline en una barrera burocrática. El escenario que conviene examinar es el siguiente: un escaneo se considera garantía de código seguro. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M6.2-K03.md) (433 palabras de borrador, no ensayo final).

### M6.2-K04 — Seguridad IA

La seguridad de IA protege modelos, datos, herramientas, agentes y procesos ante amenazas específicas y consecuencias de autonomía. El escenario que conviene examinar es el siguiente: se protege solo el modelo y se ignoran permisos de herramientas. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M6.2-K04.md) (438 palabras de borrador, no ensayo final).

### M6.2-K05 — IoT/OT Security

La seguridad IoT y OT debe preservar seguridad física, disponibilidad y control de procesos además de confidencialidad digital. El escenario que conviene examinar es el siguiente: un parche urgente interrumpe un proceso industrial crítico. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M6.2-K05.md) (437 palabras de borrador, no ensayo final).

### M6.2-K06 — Shadow AI

Shadow AI surge cuando personas y equipos utilizan herramientas de IA fuera del gobierno previsto, generando exposición de datos y decisiones. El escenario que conviene examinar es el siguiente: se prohíbe IA sin ofrecer alternativas seguras y el uso oculto aumenta. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M6.2-K06.md) (441 palabras de borrador, no ensayo final).

### M6.2-K07 — Responsabilidad Compartida

La responsabilidad compartida exige asignar controles entre proveedor, cliente, integradores y operadores según servicio y contrato. El escenario que conviene examinar es el siguiente: cada parte presume que la otra administra claves o incidentes. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M6.2-K07.md) (434 palabras de borrador, no ensayo final).

### M6.2-K08 — Riesgo Terceros (TPRM)

TPRM evalúa y supervisa riesgos de terceros durante selección, operación, cambios y salida, no solo al firmar contratos. El escenario que conviene examinar es el siguiente: un proveedor crítico pierde controles sin activar revisión. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M6.2-K08.md) (437 palabras de borrador, no ensayo final).

### M6.2-K09 — SDLC Seguro

El ciclo de desarrollo seguro integra requisitos, modelado de amenazas, implementación, pruebas y mantenimiento desde el diseño. El escenario que conviene examinar es el siguiente: la seguridad se revisa solo antes de producción. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M6.2-K09.md) (434 palabras de borrador, no ensayo final).

### M6.2-K10 — SBOM

Un software bill of materials mejora visibilidad de componentes y dependencias, pero necesita calidad, actualización y procesos de respuesta a vulnerabilidades. El escenario que conviene examinar es el siguiente: el SBOM existe pero no se usa para priorizar riesgos reales. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M6.2-K10.md) (437 palabras de borrador, no ensayo final).

## Ampliaciones Atlas de esta unidad: tesis para discutir, no definiciones aprobadas

- **[AMP-49 — Supply chain de modelos](../../02_conceptos/02_ampliaciones_atlas/AMP-49.md) [P].** Modelos y componentes de IA tienen cadena de suministro: procedencia, licencias, integridad y evaluación antes de su uso. Vínculo propuesto: `HC-031`; fuente `06Ensayos!I333`.
- **[AMP-50 — Seguridad de herramientas y conectores](../../02_conceptos/02_ampliaciones_atlas/AMP-50.md) [P].** Conectores (incluido MCP) y herramientas amplían lo que un agente puede tocar: requieren inventario, autenticación, permisos mínimos y monitoreo. Vínculo propuesto: `M6.2-K04`; fuente `06Ensayos!I334`.
- **[AMP-51 — Postura de IA en nube](../../02_conceptos/02_ampliaciones_atlas/AMP-51.md) [P].** La postura de IA en la nube descubre modelos, endpoints, datos y configuraciones riesgosas en servicios como Foundry u OpenAI, y prioriza su corrección. Vínculo propuesto: `M6.2-K02`; fuente `06Ensayos!I335`.

## Conceptos híbridos candidatos que conectan esta unidad

- [HC-008 — Cadena de confianza en terceros](../../02_conceptos/03_hibridos_candidatos/HC-008.md): conecta `G3.1-K04`, `M6.2-K01`, `M6.2-K07`, `M6.1-K10`. **Candidato**, no unidad ni arista aprobada.
- [HC-011 — Seguridad de datos en la IA empresarial](../../02_conceptos/03_hibridos_candidatos/HC-011.md): conecta `M2.1-K02`, `M2.1-K04`, `G3.1-K02`, `M6.2-K04`. **Candidato**, no unidad ni arista aprobada.
- [HC-023 — Riesgo de concentración tecnológica](../../02_conceptos/03_hibridos_candidatos/HC-023.md): conecta `M6.1-K10`, `M6.2-K08`, `M3.1-K10`, `G1.2-K05`. **Candidato**, no unidad ni arista aprobada.
- [HC-024 — Cumplimiento y privacidad por diseño](../../02_conceptos/03_hibridos_candidatos/HC-024.md): conecta `G3.1-K02`, `M2.1-K04`, `M6.2-K09`, `G3.2-K06`. **Candidato**, no unidad ni arista aprobada.
- [HC-029 — Aseguramiento de terceros y cadena de suministro](../../02_conceptos/03_hibridos_candidatos/HC-029.md): conecta `G3.1-K04`, `M6.2-K08`, `M6.2-K10`, `G3.2-K09`. **Candidato**, no unidad ni arista aprobada.
- [HC-030 — Seguridad industrial y continuidad de negocio](../../02_conceptos/03_hibridos_candidatos/HC-030.md): conecta `M6.2-K05`, `M3.1-K07`, `M5.1-K02`, `M6.1-K05`. **Candidato**, no unidad ni arista aprobada.
- [HC-031 — Seguridad del software y confianza en componentes](../../02_conceptos/03_hibridos_candidatos/HC-031.md): conecta `M6.2-K09`, `M6.2-K10`, `M3.2-K03`, `M4.2-K01`. **Candidato**, no unidad ni arista aprobada.
- [HC-032 — Evaluación adversarial de sistemas autónomos](../../02_conceptos/03_hibridos_candidatos/HC-032.md): conecta `M4.2-K02`, `M3.2-K06`, `M6.2-K04`, `M2.2-K03`. **Candidato**, no unidad ni arista aprobada.
- [HC-033 — Seguridad y soberanía de datos distribuidos](../../02_conceptos/03_hibridos_candidatos/HC-033.md): conecta `G3.1-K02`, `M2.1-K07`, `M6.2-K02`, `M6.2-K07`. **Candidato**, no unidad ni arista aprobada.

## Puente con TheMetaCognitiveCISO

Se propone entrenar la lente cognitiva `MM-0136` junto a las decisiones de `M6.2`. Esta es una **relación pedagógica derivada**, no una equivalencia canónica con el GM-24. Consulte [la caja cognitiva del CISO](../../../Biblioteca_CISO_Frontera/Caja_Cognitiva_CISO_72/00_Indice.md) para la ficha y su evidencia.

## Laboratorio: ocho modalidades de ejercicio

Las tareas comparten el mismo caso; no son ocho horas añadidas por separado. Se practican en la asignación indicativa de 3 h de seminario, 8 h de investigación y lectura, 12 h de laboratorio y 8 h de aplicación por unidad. Los tiempos requieren aprobación académica.

### 1. Comprensión conceptual

**Consigna:** Define `M6.2-K01` (C-SCRM (Cadena Suministro)) y `M6.2-K07` (Responsabilidad Compartida) con tus palabras. Señala una frontera de responsabilidad, una confusión habitual y cómo la ampliación `AMP-49` altera la interpretación del caso «Un modelo externo y un conector MCP actualizan silenciosamente dependencias; el proveedor delega controles que la empresa creía incluidos.».

**Producto:** cuadro de contraste con dos decisiones distintas y citas a las fichas.

**Comprobación:** No declara como sinónimos dos títulos vecinos ni toma la tesis [P] como definición aprobada.

### 2. Relaciones y contextualización

**Consigna:** Dibuja la cadena de decisiones entre `M6.2-K01`, `M6.2-K07`, `AMP-49` y `HC-029` — Aseguramiento de terceros y cadena de suministro. Anota en cada conexión dirección, evidencia textual, posible solapamiento y qué cambiaría al variar el contexto de negocio. Las aristas nuevas son hipótesis hasta que se validen.

**Producto:** mapa de relaciones G–M y tabla de procedencia de cada enlace.

**Comprobación:** No transforma cercanía temática en causalidad ni convierte HC en requisito aprobado.

### 3. Práctica aplicada

**Consigna:** Trabaja en «Un modelo externo y un conector MCP actualizan silenciosamente dependencias; el proveedor delega controles que la empresa creía incluidos.». Con contrato cloud, SBOM, inventario de conectores, rutas de datos y licencias, construye expediente de tercero con matriz de responsabilidad y plan de verificación; incluye propietario, condiciones de entrada y salida, hipótesis adversa y prueba de funcionamiento.

**Producto:** expediente de tercero con matriz de responsabilidad y plan de verificación.

**Comprobación:** Responsabilidad compartida y licencias no se infieren del nombre comercial del servicio.

### 4. Investigación y fuentes

**Consigna:** Investiga esta pregunta acotada: contrastar fuentes oficiales del proveedor con el contrato, la postura propia y una prueba independiente. Localiza al menos dos fuentes primarias con fecha y versión; distingue obligación, recomendación, definición, ejemplo y opinión.

**Producto:** ficha de fuentes con extractos breves, localizador y discrepancias.

**Comprobación:** No cita un borrador editorial o mapeo informativo como norma obligatoria.

### 5. Orquestación de actores y agentes

**Consigna:** Con compras, legal, ingeniería cloud y dueños de datos, construye un flujo de tres hitos para «Gobernar supply chain de modelos, postura de nube y responsabilidades de terceros.». Define qué puede proponer un agente, qué requiere aprobación humana, quién responde y cómo detener, registrar y revertir una acción errónea.

**Producto:** RACI/DACI, diagrama de traspasos y plan de supervisión.

**Comprobación:** Hay autoridad, trazas y camino de escalamiento para cada acción de alto impacto.

### 6. Análisis y contrafactual

**Consigna:** Compara «Aceptar atestados genéricos frente a exigir procedencia, SBOM, permisos y pruebas de actualización.» usando datos de contrato cloud, SBOM, inventario de conectores, rutas de datos y licencias. Contrasta la primera impresión con la lente cognitiva `MM-0136` del programa metacognitivo; plantea qué evidencia falsaría cada hipótesis y un efecto de segundo orden.

**Producto:** matriz de alternativas, incertidumbres y pruebas refutatorias.

**Comprobación:** La comparación conserva supuestos, costos de reversión y consecuencias no observadas.

### 7. Toma de decisiones

**Consigna:** Redacta para el responsable competente una recomendación sobre «Gobernar supply chain de modelos, postura de nube y responsabilidades de terceros.», con dos opciones, beneficio, riesgo residual, autoridad de aceptación, indicador temprano y condición explícita de pausa o rollback.

**Producto:** memorando ejecutivo de una página más expediente de evidencia.

**Comprobación:** Responsabilidad compartida y licencias no se infieren del nombre comercial del servicio.

### 8. Exposición y defensa

**Consigna:** Defiende la decisión ante compras, legal, ingeniería cloud y dueños de datos en siete minutos; reserva tres para objeciones. Un par cambia un dato del escenario a mitad de la exposición: revisa la postura sin ocultar el supuesto que deja de sostenerse.

**Producto:** presentación oral, preguntas difíciles y registro de revisiones.

**Comprobación:** La defensa distingue certeza, incertidumbre, decisión y propiedad del riesgo.

## Rúbrica formativa y evidencia de logro

| Criterio | 0 — insuficiente | 2 — parcial | 4 — sólido |
|---|---|---|---|
| Precisión | Confunde conceptos, categorías o estados editoriales | Explica definiciones sin límites | Distingue base, propuesta y candidato; explica límites y relaciones sin equivalencias ficticias |
| Evidencia | Cita sin procedencia ni prueba | Traza fuentes pero no su calidad | Localiza fuente, versión, modalidad, incertidumbre y prueba de eficacia |
| Decisión y autoridad | No compara opciones ni propietario | Compara pero sin residual o escalamiento | Justifica alternativas, derecho de decisión, residual, parada y revisión |
| Transferencia | Entrega teórica sin caso | Caso parcial sin contraprueba | Artefacto operable, prueba adversa y defensa ajustada a la audiencia |

**Condición crítica de esta unidad:** Responsabilidad compartida y licencias no se infieren del nombre comercial del servicio. La práctica se devuelve para revisión si incumple este criterio, aunque el promedio sea alto. Para aprendizaje se propone al menos 3/4 en cada dimensión; no es una acreditación aprobada.

## Preguntas mayéuticas, sin confundirlas con afirmaciones

**Pregunta original consolidada (muestras):**
- `PC-026`: ¿Cómo protegemos los entornos OT e IoT y la convergencia entre tecnología operativa y TI? (vínculo `M6.2-K05`).
- `PC-055`: ¿Entendemos y documentamos el modelo de responsabilidad compartida de cada servicio en la nube que usamos? (vínculo `M6.2-K07`).
- `PC-056`: ¿Cómo gestionamos la postura de seguridad y la protección de las cargas de trabajo en todas nuestras nubes? (vínculo `M6.2-K02`).
- `PC-057`: ¿Está integrada la seguridad en el ciclo de desarrollo (modelado de amenazas, análisis de código, secretos, dependencias, pruebas) con criterios de bloqueo? (vínculo `M6.2-K09`).
- `PC-059`: ¿Cómo evaluamos, contratamos y monitoreamos a los terceros críticos, incluidos los proveedores de nuestros proveedores? (vínculo `M6.2-K08`).
- `PC-095`: ¿La seguridad forma parte de la cultura de ingeniería y producto (referentes, revisiones de diseño, responsabilidad compartida)? (vínculo `M6.2-K03`).

**Serie de banco construida desde plantillas documentadas (muestras):**
- `BM-0691` — ¿Qué problema de gobierno, riesgo o capacidad intenta resolver realmente «C-SCRM (Cadena Suministro)», y qué decisión debería mejorar si se comprende correctamente?
- `BM-0692` — ¿Qué supuesto habitual sobre «C-SCRM (Cadena Suministro)» podría ser falso o incompleto, y qué consecuencia tendría diseñar la seguridad como si fuera cierto?
- `BM-0694` — ¿Qué problema de gobierno, riesgo o capacidad intenta resolver realmente «Seguridad Nube», y qué decisión debería mejorar si se comprende correctamente?
- `BM-0695` — ¿Qué supuesto habitual sobre «Seguridad Nube» podría ser falso o incompleto, y qué consecuencia tendría diseñar la seguridad como si fuera cierto?
- `BM-1073` — ¿Qué problema de gobierno, riesgo o capacidad intenta resolver realmente «Supply chain de modelos», y qué decisión debería mejorar si se comprende correctamente?
- `BM-1074` — ¿Qué supuesto habitual sobre «Supply chain de modelos» podría ser falso o incompleto, y qué consecuencia tendría diseñar la seguridad como si fuera cierto?

**Tesis propuestas por pregunta asignadas explícitamente a esta unidad: 33.**
- [APC-095 — Seguridad integrada en la cultura de ingeniería y producto](../../03_metodo_mayeutico/01_tesis_derivadas/APC-095.md) ← `PC-095`
- [APC-103 — Estrategia de seguridad ante las tres caras de la IA](../../03_metodo_mayeutico/01_tesis_derivadas/APC-103.md) ← `PC-103`
- [APC-107 — Postura sobre IA de consumo e IA incorporada por proveedores](../../03_metodo_mayeutico/01_tesis_derivadas/APC-107.md) ← `PC-107`
- [APC-112 — Política de uso aceptable de IA para colaboradores](../../03_metodo_mayeutico/01_tesis_derivadas/APC-112.md) ← `PC-112`
- [APC-121 — Descubrimiento de agentes de bajo código creados por usuarios](../../03_metodo_mayeutico/01_tesis_derivadas/APC-121.md) ← `PC-121`
- [APC-122 — Lista de materiales de IA para sistemas críticos](../../03_metodo_mayeutico/01_tesis_derivadas/APC-122.md) ← `PC-122`
- [APC-125 — Visibilidad de IA en dispositivos y entornos de desarrollo](../../03_metodo_mayeutico/01_tesis_derivadas/APC-125.md) ← `PC-125`
- [APC-151 — Protección de modelos contra robo, extracción y abuso de consumo](../../03_metodo_mayeutico/01_tesis_derivadas/APC-151.md) ← `PC-151`

**Tesis transversales relacionadas sin asignación principal (muestras):**
- [APC-039](../../03_metodo_mayeutico/01_tesis_derivadas/APC-039.md) (relación transversal, no asignación principal)
- [APC-062](../../03_metodo_mayeutico/01_tesis_derivadas/APC-062.md) (relación transversal, no asignación principal)
- [APC-063](../../03_metodo_mayeutico/01_tesis_derivadas/APC-063.md) (relación transversal, no asignación principal)
- [APC-176](../../03_metodo_mayeutico/01_tesis_derivadas/APC-176.md) (relación transversal, no asignación principal)
- [APC-182](../../03_metodo_mayeutico/01_tesis_derivadas/APC-182.md) (relación transversal, no asignación principal)

El banco completo conserva 543 preguntas originales y 2.395 preguntas derivadas mecánicamente de plantillas; 308 tesis AP forman un **anexo provisional**, distinto de los 331 conceptos del corpus de trabajo.

## Lecturas, investigación y modalidad

**Lecturas internas verificables:**
- [Documento Maestro](../../../Curado02/01_noviembre_2026/src-thenextciso-gm-24-documento-maestro__9b8c53df319d.md), unidad `M6.2` desde línea 1007.
- [lote de ideas base](../../../Curado02/01_noviembre_2026/src-thenextciso-gm24-ensayos-bases-211-240__be3ff9fea8f4.md)
- Las 51 tesis Atlas [P] proceden de `06Ensayos!I285:I335` en [matriz de pre-ensayos](../../../Curado02/01_noviembre_2026/src-ai-ciso-atlas-ensayos-thenextciso-x-core-accountabilities-fy27-2026-11-05__5528a05eb5dd.xlsx).

**Lecturas complementarias por cotejar:** NIST CSF 2.0, NIST RMF y dominios CISM/CRISC según la unidad y las fuentes listadas por el Documento Maestro. El mapeo de este documento es una propuesta temática: `CISM C3; CRISC R1,R4; NIST CSF 2.0 GV.SC,PR.PS,ID.RA; NIST RMF Prepare,Select,Implement,Monitor.`. La fuente oficial, edición y pertinencia deben comprobarse al preparar cada clase; no se presume cobertura íntegra de examen o norma.

**Recursos audiovisuales:** no se identificó un video específico, vigente y verificable por unidad en los documentos base. Existe un [inventario complementario de enlaces observados](../../../Biblioteca_CISO_Frontera/Consolidado_2026_MM_2026-11-11/03_programa_1200h/Videos_Observados_en_Fuentes.md), aún sin comprobación de contenido, disponibilidad, duración ni correspondencia con esta unidad. El equipo docente deberá seleccionarlos, comprobar derechos y documentar el vínculo antes de asignarlos.

**Carga de diseño:** 31 h por unidad; 24 unidades más capstone integrador de 56 h = escenario de 800 h. No es acreditación.

<!-- generado-gm24 sha256:a8394973a95508f054cc95b51c4657b05747e6c465459329d5ab54f352dcdfb5 -->
# M2.2 — Gestión de Identidad y Acceso (IAM) y Principios de Confianza Cero

**Pilar:** Gestión · **Eje:** Protección de activos e identidades · **Atlas:** `D05` (alineación editorial, no identidad de dominio).

**Pregunta rectora de fuente:** ¿Cómo puede un CISO diseñar, ejecutar y verificar gestión de identidad y acceso (iam) y principios de confianza cero sin perder de vista el riesgo empresarial, las responsabilidades y la evidencia?

**Alcance:** diez conceptos base con idea central desarrollada; 2 ampliaciones Atlas cuyo título pertenece al Documento Maestro y cuya tesis es propuesta [P]. Los puentes HC relacionados son candidatos transversales; ninguna extensión altera por sí sola el número de unidades.

## Situación longitudinal y decisión

**Organización ficticia:** Cuentas de servicio de agentes mantienen tokens permanentes y el mismo permiso privilegiado en desarrollo y producción.

**Decisión a sostener:** Asignar identidad por agente, limitar credenciales y registrar autorización por contexto.

**Cursos de acción en tensión:** Credencial compartida perpetua frente a identidad y permisos de menor privilegio con rotación y revocación.

**Información inicial:** inventario de identidades, roles, permisos, registros de acceso y break-glass

**Interesados:** IAM, DevOps, propietarios de aplicaciones y auditoría

**Producto acumulativo:** modelo IAM de agentes con ciclo de vida, controles y prueba de revocación

**Regla de seguridad y responsabilidad:** Autenticación fuerte no sustituye autorización para la acción concreta.

## Desarrollo de los diez conceptos base

### M2.2-K01 — Estrategias IAM

IAM debe conectar identidades humanas y no humanas, recursos y autorizaciones con responsabilidades y riesgos del negocio. El escenario que conviene examinar es el siguiente: una empresa integra aplicaciones heredadas y agentes con permisos persistentes. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M2.2-K01.md) (437 palabras de borrador, no ensayo final).

### M2.2-K02 — Autenticación

La autenticación establece evidencia de identidad y nivel de confianza adecuado a la operación, sin garantizar por sí misma que una acción esté autorizada. El escenario que conviene examinar es el siguiente: una autenticación resistente al phishing convive con sesiones robadas y excepciones de emergencia. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M2.2-K02.md) (444 palabras de borrador, no ensayo final).

### M2.2-K03 — Autorización

La autorización limita acciones y recursos conforme a propósito, contexto y mínimo privilegio, y debe revisarse a lo largo del ciclo de vida. El escenario que conviene examinar es el siguiente: un agente autenticado invoca una herramienta con facultades mayores que las delegadas. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M2.2-K03.md) (442 palabras de borrador, no ensayo final).

### M2.2-K04 — PAM (Privilegiados)

La gestión de accesos privilegiados reduce exposición al limitar, registrar y supervisar elevaciones administrativas. El escenario que conviene examinar es el siguiente: administradores conservan privilegios permanentes por razones de continuidad. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M2.2-K04.md) (431 palabras de borrador, no ensayo final).

### M2.2-K05 — Zero Trust

Zero Trust requiere verificar explícitamente, usar mínimo privilegio y asumir compromiso, articulando identidad, dispositivos, redes, aplicaciones y datos. El escenario que conviene examinar es el siguiente: la organización confunde Zero Trust con comprar una solución de acceso. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M2.2-K05.md) (440 palabras de borrador, no ensayo final).

### M2.2-K06 — ZTNA

ZTNA restringe acceso a aplicaciones privadas por identidad, contexto y política, sin asumir confianza por ubicación de red. El escenario que conviene examinar es el siguiente: una VPN concede acceso amplio a servicios internos no relacionados con el trabajo. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M2.2-K06.md) (437 palabras de borrador, no ensayo final).

### M2.2-K07 — Ciclo Vida Identidad

El ciclo de vida de identidad gobierna creación, cambios, privilegios y baja de sujetos humanos, servicios y agentes. El escenario que conviene examinar es el siguiente: una identidad de servicio queda activa después del retiro de la aplicación. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M2.2-K07.md) (442 palabras de borrador, no ensayo final).

### M2.2-K08 — Auditoría IAM

La auditoría de IAM evalúa autorizaciones, cambios, privilegios y controles de acceso con evidencia independiente y contextual. El escenario que conviene examinar es el siguiente: el inventario de cuentas parece correcto pero las autorizaciones efectivas difieren. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M2.2-K08.md) (438 palabras de borrador, no ensayo final).

### M2.2-K09 — Federación

La federación permite establecer confianza entre dominios de identidad con protocolos, acuerdos y límites de responsabilidad explícitos. El escenario que conviene examinar es el siguiente: una aplicación externa acepta tokens sin validar audiencia o condiciones de emisión. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M2.2-K09.md) (435 palabras de borrador, no ensayo final).

### M2.2-K10 — Contexto de Acceso

El contexto de acceso integra señales de identidad, dispositivo, ubicación, riesgo y operación para decidir políticas proporcionales. El escenario que conviene examinar es el siguiente: una regla demasiado amplia bloquea procesos críticos o permite accesos de alto riesgo. El desarrollo completo y sus límites están en [la ficha de idea central](../../02_conceptos/01_base_gm24/M2.2-K10.md) (442 palabras de borrador, no ensayo final).

## Ampliaciones Atlas de esta unidad: tesis para discutir, no definiciones aprobadas

- **[AMP-33 — Identidades no humanas](../../02_conceptos/02_ampliaciones_atlas/AMP-33.md) [P].** Las identidades no humanas ya superan a las humanas; sin inventario, dueño, credenciales gestionadas y caducidad son la superficie menos vigilada. Vínculo propuesto: `HC-009`; fuente `06Ensayos!I317`.
- **[AMP-34 — Identidad y autorización de agentes](../../02_conceptos/02_ampliaciones_atlas/AMP-34.md) [P].** Cada agente necesita identidad propia, permisos mínimos, acceso condicional y ciclo de vida: es la base de un agente protegido. Vínculo propuesto: `M2.2-K03`; fuente `06Ensayos!I318`.

## Conceptos híbridos candidatos que conectan esta unidad

- [HC-009 — Gobierno de identidades no humanas](../../02_conceptos/03_hibridos_candidatos/HC-009.md): conecta `M2.2-K01`, `M2.2-K03`, `M2.2-K07`, `G4.1-K08`. **Candidato**, no unidad ni arista aprobada.
- [HC-010 — Autonomía delegada y límites de acción](../../02_conceptos/03_hibridos_candidatos/HC-010.md): conecta `G4.2-K05`, `M2.2-K03`, `M3.1-K09`, `M4.1-K08`. **Candidato**, no unidad ni arista aprobada.
- [HC-015 — Gobierno y operación de Zero Trust](../../02_conceptos/03_hibridos_candidatos/HC-015.md): conecta `G2.2-K03`, `M2.2-K05`, `M3.1-K03`, `M3.2-K09`. **Candidato**, no unidad ni arista aprobada.
- [HC-032 — Evaluación adversarial de sistemas autónomos](../../02_conceptos/03_hibridos_candidatos/HC-032.md): conecta `M4.2-K02`, `M3.2-K06`, `M6.2-K04`, `M2.2-K03`. **Candidato**, no unidad ni arista aprobada.
- [HC-038 — Aseguramiento de la arquitectura Zero Trust](../../02_conceptos/03_hibridos_candidatos/HC-038.md): conecta `G2.2-K03`, `M2.2-K05`, `M3.1-K03`, `M3.2-K04`. **Candidato**, no unidad ni arista aprobada.

## Puente con TheMetaCognitiveCISO

Se propone entrenar la lente cognitiva `BIAS-0196` junto a las decisiones de `M2.2`. Esta es una **relación pedagógica derivada**, no una equivalencia canónica con el GM-24. Consulte [la caja cognitiva del CISO](../../../Biblioteca_CISO_Frontera/Caja_Cognitiva_CISO_72/00_Indice.md) para la ficha y su evidencia.

## Laboratorio: ocho modalidades de ejercicio

Las tareas comparten el mismo caso; no son ocho horas añadidas por separado. Se practican en la asignación indicativa de 3 h de seminario, 8 h de investigación y lectura, 12 h de laboratorio y 8 h de aplicación por unidad. Los tiempos requieren aprobación académica.

### 1. Comprensión conceptual

**Consigna:** Define `M2.2-K02` (Autenticación) y `M2.2-K03` (Autorización) con tus palabras. Señala una frontera de responsabilidad, una confusión habitual y cómo la ampliación `AMP-34` altera la interpretación del caso «Cuentas de servicio de agentes mantienen tokens permanentes y el mismo permiso privilegiado en desarrollo y producción.».

**Producto:** cuadro de contraste con dos decisiones distintas y citas a las fichas.

**Comprobación:** No declara como sinónimos dos títulos vecinos ni toma la tesis [P] como definición aprobada.

### 2. Relaciones y contextualización

**Consigna:** Dibuja la cadena de decisiones entre `M2.2-K02`, `M2.2-K03`, `AMP-34` y `HC-009` — Gobierno de identidades no humanas. Anota en cada conexión dirección, evidencia textual, posible solapamiento y qué cambiaría al variar el contexto de negocio. Las aristas nuevas son hipótesis hasta que se validen.

**Producto:** mapa de relaciones G–M y tabla de procedencia de cada enlace.

**Comprobación:** No transforma cercanía temática en causalidad ni convierte HC en requisito aprobado.

### 3. Práctica aplicada

**Consigna:** Trabaja en «Cuentas de servicio de agentes mantienen tokens permanentes y el mismo permiso privilegiado en desarrollo y producción.». Con inventario de identidades, roles, permisos, registros de acceso y break-glass, construye modelo IAM de agentes con ciclo de vida, controles y prueba de revocación; incluye propietario, condiciones de entrada y salida, hipótesis adversa y prueba de funcionamiento.

**Producto:** modelo IAM de agentes con ciclo de vida, controles y prueba de revocación.

**Comprobación:** Autenticación fuerte no sustituye autorización para la acción concreta.

### 4. Investigación y fuentes

**Consigna:** Investiga esta pregunta acotada: contrastar identidad humana, no humana y agente; comprobar dependencias de federación. Localiza al menos dos fuentes primarias con fecha y versión; distingue obligación, recomendación, definición, ejemplo y opinión.

**Producto:** ficha de fuentes con extractos breves, localizador y discrepancias.

**Comprobación:** No cita un borrador editorial o mapeo informativo como norma obligatoria.

### 5. Orquestación de actores y agentes

**Consigna:** Con IAM, DevOps, propietarios de aplicaciones y auditoría, construye un flujo de tres hitos para «Asignar identidad por agente, limitar credenciales y registrar autorización por contexto.». Define qué puede proponer un agente, qué requiere aprobación humana, quién responde y cómo detener, registrar y revertir una acción errónea.

**Producto:** RACI/DACI, diagrama de traspasos y plan de supervisión.

**Comprobación:** Hay autoridad, trazas y camino de escalamiento para cada acción de alto impacto.

### 6. Análisis y contrafactual

**Consigna:** Compara «Credencial compartida perpetua frente a identidad y permisos de menor privilegio con rotación y revocación.» usando datos de inventario de identidades, roles, permisos, registros de acceso y break-glass. Contrasta la primera impresión con la lente cognitiva `BIAS-0196` del programa metacognitivo; plantea qué evidencia falsaría cada hipótesis y un efecto de segundo orden.

**Producto:** matriz de alternativas, incertidumbres y pruebas refutatorias.

**Comprobación:** La comparación conserva supuestos, costos de reversión y consecuencias no observadas.

### 7. Toma de decisiones

**Consigna:** Redacta para el responsable competente una recomendación sobre «Asignar identidad por agente, limitar credenciales y registrar autorización por contexto.», con dos opciones, beneficio, riesgo residual, autoridad de aceptación, indicador temprano y condición explícita de pausa o rollback.

**Producto:** memorando ejecutivo de una página más expediente de evidencia.

**Comprobación:** Autenticación fuerte no sustituye autorización para la acción concreta.

### 8. Exposición y defensa

**Consigna:** Defiende la decisión ante IAM, DevOps, propietarios de aplicaciones y auditoría en siete minutos; reserva tres para objeciones. Un par cambia un dato del escenario a mitad de la exposición: revisa la postura sin ocultar el supuesto que deja de sostenerse.

**Producto:** presentación oral, preguntas difíciles y registro de revisiones.

**Comprobación:** La defensa distingue certeza, incertidumbre, decisión y propiedad del riesgo.

## Rúbrica formativa y evidencia de logro

| Criterio | 0 — insuficiente | 2 — parcial | 4 — sólido |
|---|---|---|---|
| Precisión | Confunde conceptos, categorías o estados editoriales | Explica definiciones sin límites | Distingue base, propuesta y candidato; explica límites y relaciones sin equivalencias ficticias |
| Evidencia | Cita sin procedencia ni prueba | Traza fuentes pero no su calidad | Localiza fuente, versión, modalidad, incertidumbre y prueba de eficacia |
| Decisión y autoridad | No compara opciones ni propietario | Compara pero sin residual o escalamiento | Justifica alternativas, derecho de decisión, residual, parada y revisión |
| Transferencia | Entrega teórica sin caso | Caso parcial sin contraprueba | Artefacto operable, prueba adversa y defensa ajustada a la audiencia |

**Condición crítica de esta unidad:** Autenticación fuerte no sustituye autorización para la acción concreta. La práctica se devuelve para revisión si incumple este criterio, aunque el promedio sea alto. Para aprendizaje se propone al menos 3/4 en cada dimensión; no es una acreditación aprobada.

## Preguntas mayéuticas, sin confundirlas con afirmaciones

**Pregunta original consolidada (muestras):**
- `PC-024`: ¿Cómo protegemos el acceso de personas que trabajan desde cualquier lugar sin depender del perímetro de red? (vínculo `M2.2-K06`).
- `PC-028`: ¿Qué porcentaje de usuarios, administradores y accesos externos usa autenticación multifactor resistente al phishing, y cuál es la fecha objetivo para el 100%? (vínculo `M2.2-K02`).
- `PC-029`: ¿Cómo gestionamos el acceso privilegiado: cuentas separadas, elevación justo a tiempo, estaciones de administración protegidas y revisión continua? (vínculo `M2.2-K04`).
- `PC-030`: ¿Las políticas de acceso condicional cubren a todos los usuarios, aplicaciones e identidades de carga de trabajo, y cómo detectamos sus brechas? (vínculo `M2.2-K10`).
- `PC-032`: ¿Cómo gobernamos el ciclo de vida de las identidades (alta, cambio, baja) y las revisiones de acceso, incluidos terceros e invitados? (vínculo `M2.2-K07`).
- `PC-034`: ¿Cómo protegemos los sistemas que gobiernan la identidad (proveedor de identidad, federación, Active Directory híbrido, cuentas de emergencia)? (vínculo `M2.2-K09`).

**Serie de banco construida desde plantillas documentadas (muestras):**
- `BM-0451` — ¿Qué problema de gobierno, riesgo o capacidad intenta resolver realmente «Estrategias IAM», y qué decisión debería mejorar si se comprende correctamente?
- `BM-0452` — ¿Qué supuesto habitual sobre «Estrategias IAM» podría ser falso o incompleto, y qué consecuencia tendría diseñar la seguridad como si fuera cierto?
- `BM-0454` — ¿Qué problema de gobierno, riesgo o capacidad intenta resolver realmente «Autenticación», y qué decisión debería mejorar si se comprende correctamente?
- `BM-0455` — ¿Qué supuesto habitual sobre «Autenticación» podría ser falso o incompleto, y qué consecuencia tendría diseñar la seguridad como si fuera cierto?
- `BM-1009` — ¿Qué problema de gobierno, riesgo o capacidad intenta resolver realmente «Identidades no humanas», y qué decisión debería mejorar si se comprende correctamente?
- `BM-1010` — ¿Qué supuesto habitual sobre «Identidades no humanas» podría ser falso o incompleto, y qué consecuencia tendría diseñar la seguridad como si fuera cierto?

**Tesis propuestas por pregunta asignadas explícitamente a esta unidad: 15.**
- [APC-034 — Protección del plano de control de la identidad](../../03_metodo_mayeutico/01_tesis_derivadas/APC-034.md) ← `PC-034`
- [APC-035 — Verificación de identidad resistente a suplantación con IA](../../03_metodo_mayeutico/01_tesis_derivadas/APC-035.md) ← `PC-035`
- [APC-036 — Indicadores de madurez de identidad con responsables asignados](../../03_metodo_mayeutico/01_tesis_derivadas/APC-036.md) ← `PC-036`
- [APC-061 — Gobierno del consentimiento OAuth y de aplicaciones SaaS](../../03_metodo_mayeutico/01_tesis_derivadas/APC-061.md) ← `PC-061`
- [APC-130 — Permisos temporales, revisables y revocables para agentes](../../03_metodo_mayeutico/01_tesis_derivadas/APC-130.md) ← `PC-130`
- [APC-131 — Acceso condicional y protección por riesgo para agentes](../../03_metodo_mayeutico/01_tesis_derivadas/APC-131.md) ← `PC-131`
- [APC-132 — Eliminación y resguardo de secretos estáticos en agentes](../../03_metodo_mayeutico/01_tesis_derivadas/APC-132.md) ← `PC-132`
- [APC-134 — Segregación de funciones entre construir, autorizar y desplegar agentes](../../03_metodo_mayeutico/01_tesis_derivadas/APC-134.md) ← `PC-134`

**Tesis transversales relacionadas sin asignación principal (muestras):**
- [APC-062](../../03_metodo_mayeutico/01_tesis_derivadas/APC-062.md) (relación transversal, no asignación principal)
- [APC-155](../../03_metodo_mayeutico/01_tesis_derivadas/APC-155.md) (relación transversal, no asignación principal)
- [APC-198](../../03_metodo_mayeutico/01_tesis_derivadas/APC-198.md) (relación transversal, no asignación principal)
- [APC-281](../../03_metodo_mayeutico/01_tesis_derivadas/APC-281.md) (relación transversal, no asignación principal)
- [APC-296](../../03_metodo_mayeutico/01_tesis_derivadas/APC-296.md) (relación transversal, no asignación principal)

El banco completo conserva 543 preguntas originales y 2.395 preguntas derivadas mecánicamente de plantillas; 308 tesis AP forman un **anexo provisional**, distinto de los 331 conceptos del corpus de trabajo.

## Lecturas, investigación y modalidad

**Lecturas internas verificables:**
- [Documento Maestro](../../../Curado02/01_noviembre_2026/src-thenextciso-gm-24-documento-maestro__9b8c53df319d.md), unidad `M2.2` desde línea 679.
- [lote de ideas base](../../../Curado02/01_noviembre_2026/src-thenextciso-gm24-ensayos-bases-151-180__be034906f333.md)
- Las 51 tesis Atlas [P] proceden de `06Ensayos!I285:I335` en [matriz de pre-ensayos](../../../Curado02/01_noviembre_2026/src-ai-ciso-atlas-ensayos-thenextciso-x-core-accountabilities-fy27-2026-11-05__5528a05eb5dd.xlsx).

**Lecturas complementarias por cotejar:** NIST CSF 2.0, NIST RMF y dominios CISM/CRISC según la unidad y las fuentes listadas por el Documento Maestro. El mapeo de este documento es una propuesta temática: `CISM C3; CRISC R4; NIST CSF 2.0 PR.AA,GV.RR; NIST RMF Select,Implement,Monitor.`. La fuente oficial, edición y pertinencia deben comprobarse al preparar cada clase; no se presume cobertura íntegra de examen o norma.

**Recursos audiovisuales:** no se identificó un video específico, vigente y verificable por unidad en los documentos base. Existe un [inventario complementario de enlaces observados](../../../Biblioteca_CISO_Frontera/Consolidado_2026_MM_2026-11-11/03_programa_1200h/Videos_Observados_en_Fuentes.md), aún sin comprobación de contenido, disponibilidad, duración ni correspondencia con esta unidad. El equipo docente deberá seleccionarlos, comprobar derechos y documentar el vínculo antes de asignarlos.

**Carga de diseño:** 31 h por unidad; 24 unidades más capstone integrador de 56 h = escenario de 800 h. No es acreditación.

# Modelo Operativo CISO 365 · 07 · Sistema de medición: KPIs y OKR

**AI CISO Atlas · v1.0 · 10 de noviembre de 2026** · Relación con el catálogo de KPIs y OKRs, indicadores del sistema de gestión, tablero y OKR del año 1.


## 1. La relación con el catálogo de KPIs y OKRs

El catálogo y el plan se complementan en tres capas:

| Capa | Responde | Dónde |
|---|---|---|
| Catálogo de KPIs y OKRs | Qué se mide: definición, fórmula, estadios E1 a E5, umbrales, OKR de referencia y arreglos por sector | AI_CISO_Atlas_KPIs_OKRs_CISO_de_Frontera_v1.1_2026-11-10.xlsx |
| Plan 365 y ciclo anual | Cuándo y cómo se instala, se mide, se revisa y se compromete cada indicador | AI_CISO_Atlas_CISO365_Plan_y_Ciclo_Anual_v1.0.xlsx (hojas Plan 365, Ciclo anual, Indicadores del plan y OKR del año 1) |
| Tablero de rendición de cuentas | Cómo se rinde cuentas: hitos, indicadores por pregunta del directorio y OKR del año 1 | AI_CISO_Atlas_CISO365_Tablero_Rendicion_de_Cuentas_v1.0.xlsx |

| Pieza del plan | Relación con los indicadores |
|---|---|
| 130 actividades | 116 declaran los indicadores que instalan o usan (columna Indicadores del Plan 365). |
| 54 rituales | 54 declaran los indicadores que revisan; además rige la regla de revisión (sección 7). |
| 51 prácticas de evaluación | Todas tienen indicador de verificación. |
| 7 hitos con 40 criterios | KSG01 mide su cumplimiento; el criterio H180-4 exige el tablero v1 con línea base y metas, y el H100-4, los OKR del año 1. |
| Tablero del año 1 | 39 indicadores agrupados en seis preguntas del directorio (Q1 a Q6). |
| OKR del año 1 | 6 objetivos y 18 resultados clave, alineados a los hitos. |
| 18 servicios | Cada servicio declara los indicadores que mueve. |

## 2. Qué mostró la validación y qué se corrigió

| Hallazgo con el catálogo v1.0 | Corrección (catálogo v1.1 y libros del plan) |
|---|---|
| 61 de 64 KPIs estaban en el plan; K08, K44, K55 no tenían uso. | Los tres quedan vinculados a actividades, rituales y prácticas: 70 de 70 indicadores en uso. |
| 15 KPIs sin ritual que los revisara y 24 revisados con menos frecuencia que la que se miden (12 en el tablero). | Regla de revisión (R06, R12, R08 y R13) y rituales explícitos nuevos: 35 indicadores coherentes por sus rituales y 35 por la regla; ninguno sin revisión suficiente. |
| Los OKR del catálogo apuntan a E4 en cuatro trimestres; el plan no tenía OKR propios para el año 1. | OKR del año 1 con metas E3 (o E4 si la línea base ya alcanza E3); los OKR del catálogo pasan a ser de régimen, desde el año 2. |
| Seis componentes del modelo operativo sin indicador (hitos, rituales, derechos de decisión, tablero, prácticas y compromisos). | Nueva familia KSG01 a KSG06, incluida en el catálogo v1.1. |
| El tablero cargaba porcentajes de 0 a 100 y el catálogo, como fracción. | Misma convención en todos los libros: 75% = 0,75 (en el JSON, de 0 a 100). |
| Faltaban K51 en el tablero y una pregunta de rendición de cuentas. | Q5 suma K51; Q6 pasa a «¿Cumplimos lo que prometimos?» con KSG01 a KSG06, K02 y K01. |

## 3. El año de la medición, hito por hito

| Hito | Qué pasa con la medición |
|---|---|
| H0 · Mandato acordado | Se acuerda el objetivo A1-O1 (primeros 100 días) y el acceso a los datos. |
| H30 · Acta de recepción | Se registra el estado de los rubros recibidos y las métricas heredadas. |
| H60 · Diagnóstico base | Primera línea base: perfil actual, escenarios, activos críticos, exposición. |
| H100 · Informe de los 100 días | Tablero v0 con línea base y metas del año 1; OKR A1-O2 a A1-O6 acordados (criterio H100-4). |
| H180 · Sistema de gobierno operando | Tablero v1 en uso mensual (criterio H180-4); rituales y decisiones medidos (KSG02 y KSG03). |
| H270 · Capacidades probadas | Ejercicios de crisis, recuperación y controles probados (K15, K30, K60). |
| H365 · Rendición de cuentas anual | Lo prometido frente a lo cumplido (KSG01, KSG06), nivel de evidencia de las prácticas (KSG05) y OKR de régimen del año 2 (R44). |

## 4. Indicadores del sistema de gestión del CISO (KSG)

Miden si el modelo operativo funciona: cada componente del modelo tiene su indicador.

| ID | Indicador | Componente | Fórmula | E3 (año 1) | E4 (año 2) | Frecuencia | Se instala con | Se revisa en |
|---|---|---|---|---|---|---|---|---|
| KSG01 | Criterios de salida de los hitos cumplidos en fecha | Fases, hitos y criterios de salida | (Criterios cumplidos + valor parcial × criterios parciales) ÷ criterios exigibles a la fecha × 100. Valor parcial por defecto: 0,5. | ≥ 70% | ≥ 85% | Por hito · trimestral | ACT-072; ACT-102; ACT-116; ACT-126 | R14; R21; R43 |
| KSG02 | Rituales del ciclo de gobierno realizados según el calendario | Ciclo anual de gobierno y gestión | Rituales realizados en ventana y con acta ÷ rituales programados para el período × 100. | ≥ 70% | ≥ 85% | Trimestral | ACT-057; ACT-073; ACT-127 | R14; R45 |
| KSG03 | Decisiones materiales tomadas por el rol con autoridad | Derechos de decisión | Decisiones de la muestra tomadas por el rol con autoridad (A) y en plazo ÷ decisiones materiales de la muestra × 100. | ≥ 60% | ≥ 80% | Trimestral | ACT-057; ACT-075 | R12 |
| KSG04 | Indicadores del tablero con línea base, dueño y fuente | Sistema de medición (tablero) | Indicadores del tablero con línea base, dueño, fuente y fórmula documentados ÷ indicadores del tablero × 100. | ≥ 60% | ≥ 80% | Trimestral | ACT-051; ACT-061; ACT-077 | R08 |
| KSG05 | Nivel de evidencia de las prácticas de gobierno y gestión | Evaluación de la gestión (51 prácticas) | Promedio del nivel actual (0 a 4) de las prácticas evaluadas; se informa junto con la cantidad de prácticas críticas en nivel 0. | ≥ 2,0 | ≥ 3,0 | Anual · línea base en H100 | ACT-119; ACT-127 | R42; R45 |
| KSG06 | Compromisos de rendición de cuentas cumplidos o renegociados a tiempo | Rendición de cuentas (lo prometido frente a lo cumplido) | (Compromisos cumplidos en fecha + compromisos renegociados antes del vencimiento) ÷ compromisos con vencimiento en el período × 100. | ≥ 70% | ≥ 85% | Trimestral | ACT-002; ACT-071; ACT-074; ACT-129 | R13; R14; R43 |

## 5. Tablero del año 1 por pregunta del directorio

### Q1 · ¿Cuál es nuestro nivel real de riesgo?

| ID | Indicador | Frecuencia | Meta año 1 (E3) | Meta año 2 (E4) | Primera actividad | Rituales |
|---|---|---|---|---|---|---|
| K25 | Riesgos residuales fuera del apetito | Trimestral | ≤ 10% | ≤ 5% | ACT-063 | R08; R12; R23; R26; R27; R13 |
| K26 | Pérdida esperada de los escenarios prioritarios frente al apetito | Semestral | ≤ 100% | ≤ 75% | ACT-035 | R27; R12; R08; R13 |
| K46 | Vulnerabilidades explotadas y exposiciones críticas remediadas en plazo | Mensual | ≥ 70% | ≥ 85% | ACT-038 | R03; R06; R08; R13 |
| K33 | Autenticación resistente al phishing | Mensual | ≥ 50% | ≥ 80% | ACT-039 | R06; R08; R13 |
| K39 | Cobertura del inventario de activos (TI, nube, OT e IoT) | Mensual | ≥ 75% | ≥ 90% | ACT-032 | R32; R06; R08; R13 |

### Q2 · ¿Estamos mejorando?

| ID | Indicador | Frecuencia | Meta año 1 (E3) | Meta año 2 (E4) | Primera actividad | Rituales |
|---|---|---|---|---|---|---|
| K22 | Resultados del perfil objetivo alcanzados (NIST CSF 2.0) | Anual | ≥ 50% | ≥ 70% | ACT-028 | R28; R39; R12; R08; R13 |
| K18 | Avance del roadmap estratégico de seguridad | Trimestral | ≥ 70% | ≥ 85% | ACT-026 | R06; R14; R21; R24; R44; R08; R13 |
| K60 | Controles clave con efectividad probada | Trimestral | ≥ 60% | ≥ 80% | ACT-045 | R31; R35; R06; R08; R13 |
| K42 | Tiempo medio de detección (MTTD) | Mensual | ≤ 24 | ≤ 8 | ACT-037 | R03; R04; R06; R08; R13 |
| K45 | Tiempo medio de contención (MTTC) | Mensual | ≤ 12 | ≤ 4 | ACT-037 | R03; R04; R06; R08; R13 |

### Q3 · ¿Estamos invirtiendo correctamente?

| ID | Indicador | Frecuencia | Meta año 1 (E3) | Meta año 2 (E4) | Primera actividad | Rituales |
|---|---|---|---|---|---|---|
| K17 | Inversión en seguridad trazada a riesgos y objetivos del negocio | Semestral | ≥ 60% | ≥ 80% | ACT-017 | R10; R24; R25; R12; R08; R13 |
| K19 | Reducción de riesgo por unidad de inversión | Anual | ≥ 1 | ≥ 2 | ACT-060 | R25; R12; R08; R13 |
| K20 | Tiempo de habilitación segura de iniciativas | Trimestral | ≤ 10 | ≤ 5 | ACT-086 | R52; R06; R08; R13 |
| K12 | Cobertura de capacidades críticas del equipo de seguridad | Semestral | ≥ 70% | ≥ 85% | ACT-014 | R02; R40; R49; R06; R08; R13 |

### Q4 · ¿Estamos preparados para una interrupción significativa?

| ID | Indicador | Frecuencia | Meta año 1 (E3) | Meta año 2 (E4) | Primera actividad | Rituales |
|---|---|---|---|---|---|---|
| K30 | Pruebas de recuperación que cumplen RTO y RPO | Semestral | ≥ 60% | ≥ 80% | ACT-041 | R34; R06; R08; R13 |
| K28 | Respaldos inmutables de sistemas críticos con restauración probada | Trimestral | ≥ 70% | ≥ 85% | ACT-041 | R17; R06; R08; R13 |
| K15 | Ejercicios de crisis con participación ejecutiva | Semestral | ≥ 50% | ≥ 75% | ACT-111 | R33; R12; R08; R13 |
| K32 | Escenarios críticos con playbook probado | Semestral | ≥ 50% | ≥ 75% | ACT-011 | R22; R06; R08; R13 |
| K31 | Proveedores críticos evaluados y con cláusulas de seguridad | Trimestral | ≥ 60% | ≥ 80% | ACT-022 | R07; R36; R06; R08; R13 |
| K21 | Procesos críticos con BIA vigente y dependencias mapeadas | Semestral | ≥ 60% | ≥ 80% | ACT-018 | R32; R06; R08; R13 |

### Q5 · ¿Gobernamos el riesgo con evidencia?

| ID | Indicador | Frecuencia | Meta año 1 (E3) | Meta año 2 (E4) | Primera actividad | Rituales |
|---|---|---|---|---|---|---|
| K09 | Procesos y activos críticos con dueño de riesgo designado | Trimestral | ≥ 60% | ≥ 80% | ACT-076 | R12; R23; R08; R13 |
| K14 | Supervisión activa del Directorio sobre el ciberriesgo | Trimestral | ≥ 50% | ≥ 75% | ACT-002 | R12; R13; R18; R43; R46; R08 |
| K58 | Calidad del reporte de ciberriesgo al Directorio | Trimestral | ≥ 50% | ≥ 70% | ACT-024 | R08; R13; R15; R43; R12 |
| K04 | Aceptaciones de riesgo con alternativas, pre-mortem y vencimiento | Trimestral | ≥ 50% | ≥ 80% | ACT-019 | R09; R54; R12; R08; R13 |
| K63 | Excepciones a políticas vigentes, justificadas y con vencimiento | Trimestral | ≥ 60% | ≥ 80% | ACT-015 | R09; R29; R54; R12; R08; R13 |
| K57 | Obligaciones aplicables mapeadas a controles con evidencia vigente | Trimestral | ≥ 70% | ≥ 85% | ACT-033 | R30; R53; R12; R08; R13 |
| K59 | Hallazgos de auditoría y de reguladores cerrados en plazo | Trimestral | ≥ 70% | ≥ 85% | ACT-015 | R06; R20; R31; R12; R08; R13 |
| K03 | Decisiones materiales con registro y revisión posterior | Trimestral | ≥ 50% | ≥ 75% | ACT-009 | R01; R42; R12; R08; R13 |
| K49 | Inventario de sistemas de IA y agentes | Mensual | ≥ 50% | ≥ 75% | ACT-043 | R37; R06; R08; R13 |
| K50 | Agentes con dueño humano y autoridad delegada acotada | Mensual | ≥ 50% | ≥ 75% | ACT-039 | R16; R37; R12; R08; R13 |
| K51 | Casos de uso de IA con evaluación de riesgo e impacto previa | Trimestral | ≥ 60% | ≥ 80% | ACT-043 | R37; R12; R08; R13 |

### Q6 · ¿Cumplimos lo que prometimos? (sistema de gestión y práctica del CISO)

| ID | Indicador | Frecuencia | Meta año 1 (E3) | Meta año 2 (E4) | Primera actividad | Rituales |
|---|---|---|---|---|---|---|
| KSG01 | Criterios de salida de los hitos cumplidos en fecha | Por hito · trimestral | ≥ 70% | ≥ 85% | ACT-072 | R14; R21; R43; R06; R08; R13 |
| KSG02 | Rituales del ciclo de gobierno realizados según el calendario | Trimestral | ≥ 70% | ≥ 85% | ACT-057 | R14; R45; R12; R08; R13 |
| KSG03 | Decisiones materiales tomadas por el rol con autoridad | Trimestral | ≥ 60% | ≥ 80% | ACT-057 | R12; R08; R13 |
| KSG04 | Indicadores del tablero con línea base, dueño y fuente | Trimestral | ≥ 60% | ≥ 80% | ACT-051 | R08; R12; R13 |
| KSG05 | Nivel de evidencia de las prácticas de gobierno y gestión | Anual · línea base en H100 | ≥ 2,0 | ≥ 3,0 | ACT-119 | R42; R45; R12; R08; R13 |
| KSG06 | Compromisos de rendición de cuentas cumplidos o renegociados a tiempo | Trimestral | ≥ 70% | ≥ 85% | ACT-002 | R13; R14; R43; R12; R08 |
| K02 | Tiempo del CISO en agenda de gobierno y negocio | Trimestral | ≥ 25% | ≥ 35% | ACT-012 | R19; R12; R08; R13 |
| K01 | Calibración del juicio de riesgo (puntaje de habilidad de Brier) | Trimestral | ≥ 0,1 | ≥ 0,2 | ACT-009 | R01; R19; R48; R12; R08; R13 |

## 6. OKR del año 1

*Regla de metas.* Meta del año 1 = umbral E3; si la línea base ya alcanza E3, la meta pasa a E4 (un estadio por encima de la línea base). Hitos: meta de cumplimiento del hito (80% por defecto).

*Cuándo se acuerdan.* A1-O1 con el mandato (H0); A1-O2 a A1-O6 en el informe de los 100 días (H100). Se revisan cada trimestre (R14) y se cierran en el informe anual (H365).

*Objetivos seleccionables.* Seleccionable: reemplazar por los OKR «Gestionar» y «Evolucionar» del sector (hoja OKR_Sectores del catálogo) con meta E3 en el año 1.

| Objetivo | Hito | Resultado clave | Indicador | Meta del año 1 | Actividades | Seguimiento | Responsable |
|---|---|---|---|---|---|---|---|
| A1-O1 · Conocer la verdad del área y acordar un mandato basado en evidencia. | H100 | A1-O1-KR1 · Cumplir el hito H30 «Acta de recepción»: estado conocido de al menos el 80% de los rubros, urgencias con dueño y equipo escuchado. | H30 · Cumplimiento del hito H30 · Acta de recepción | ≥ 80% de los criterios del hito (parámetro del tablero) | ACT-013; ACT-015; ACT-029 | Revisión del hito con el sponsor | CISO |
| A1-O1 · Conocer la verdad del área y acordar un mandato basado en evidencia. | H100 | A1-O1-KR2 · Llevar «Indicadores del tablero con línea base, dueño y fuente» a 60% o más (estadio E3) al presentar el informe de los 100 días. | KSG04 · Indicadores del tablero con línea base, dueño y fuente | ≥ 60% | ACT-051; ACT-061 | R08 · R14 | CISO |
| A1-O1 · Conocer la verdad del área y acordar un mandato basado en evidencia. | H100 | A1-O1-KR3 · Cumplir el hito H100 «Informe de los 100 días»: diagnóstico, riesgos estratégicos, resultados tempranos, hoja de ruta con OKR, apoyos y carta de la función. | H100 · Cumplimiento del hito H100 · Informe de los 100 días | ≥ 80% de los criterios del hito (parámetro del tablero) | ACT-055; ACT-059; ACT-058; ACT-069; ACT-071 | Revisión del hito con el sponsor | CISO |
| A1-O2 · Instalar el sistema de gobierno y gestión del ciberriesgo. | H180 | A1-O2-KR1 · Llevar «Rituales del ciclo de gobierno realizados según el calendario» a 70% o más (estadio E3). | KSG02 · Rituales del ciclo de gobierno realizados según el calendario | ≥ 70% | ACT-057; ACT-070; ACT-073; ACT-074 | R12 · R14 | CISO |
| A1-O2 · Instalar el sistema de gobierno y gestión del ciberriesgo. | H180 | A1-O2-KR2 · Llevar «Procesos y activos críticos con dueño de riesgo designado» a 60% o más (estadio E3). | K09 · Procesos y activos críticos con dueño de riesgo designado | ≥ 60% | ACT-076 | R12 · R23 | Dueños de riesgo y CISO |
| A1-O2 · Instalar el sistema de gobierno y gestión del ciberriesgo. | H180 | A1-O2-KR3 · Llevar «Decisiones materiales tomadas por el rol con autoridad» a 60% o más (estadio E3). | KSG03 · Decisiones materiales tomadas por el rol con autoridad | ≥ 60% | ACT-057; ACT-075; ACT-079 | R09 · R12 | Comité de ciberriesgo |
| A1-O3 · Probar que las capacidades críticas funcionan bajo presión. | H270 | A1-O3-KR1 · Llevar «Ejercicios de crisis con participación ejecutiva» a 50% o más (estadio E3). | K15 · Ejercicios de crisis con participación ejecutiva | ≥ 50% | ACT-111 | R33 | CISO y comité ejecutivo |
| A1-O3 · Probar que las capacidades críticas funcionan bajo presión. | H270 | A1-O3-KR2 · Llevar «Pruebas de recuperación que cumplen RTO y RPO» a 60% o más (estadio E3). | K30 · Pruebas de recuperación que cumplen RTO y RPO | ≥ 60% | ACT-109 | R17 · R34 | Continuidad y Tecnología |
| A1-O3 · Probar que las capacidades críticas funcionan bajo presión. | H270 | A1-O3-KR3 · Llevar «Controles clave con efectividad probada» a 60% o más (estadio E3). | K60 · Controles clave con efectividad probada | ≥ 60% | ACT-045; ACT-110 | R31 · R35 | CISO y auditoría interna |
| A1-O4 · Rendir cuentas con evidencia y renovar el mandato. | H365 | A1-O4-KR1 · Llevar «Criterios de salida de los hitos cumplidos en fecha» a 70% o más (estadio E3) en el acumulado del año. | KSG01 · Criterios de salida de los hitos cumplidos en fecha | ≥ 70% | ACT-072; ACT-102; ACT-116; ACT-126 | R14 · R43 | CISO |
| A1-O4 · Rendir cuentas con evidencia y renovar el mandato. | H365 | A1-O4-KR2 · Llevar «Compromisos de rendición de cuentas cumplidos o renegociados a tiempo» a 70% o más (estadio E3). | KSG06 · Compromisos de rendición de cuentas cumplidos o renegociados a tiempo | ≥ 70% | ACT-071; ACT-074; ACT-129 | R13 · R43 | CISO y sponsor |
| A1-O4 · Rendir cuentas con evidencia y renovar el mandato. | H365 | A1-O4-KR3 · Llevar el «Nivel de evidencia de las prácticas de gobierno y gestión» a 2,0 o más (estadio E3: implementado). | KSG05 · Nivel de evidencia de las prácticas de gobierno y gestión | ≥ 2,0 | ACT-119; ACT-127 | R42 · R45 | CISO |
| A1-O5 · Reducir la exposición en los escenarios de riesgo prioritarios. | H365 | A1-O5-KR1 · Reducir «Riesgos residuales fuera del apetito» a 10% o menos (estadio E3). | K25 · Riesgos residuales fuera del apetito | ≤ 10% | ACT-079; ACT-120 | R12 · R26 | Dueños de riesgo |
| A1-O5 · Reducir la exposición en los escenarios de riesgo prioritarios. | H365 | A1-O5-KR2 · Llevar «Vulnerabilidades explotadas y exposiciones críticas remediadas en plazo» a 70% o más (estadio E3). | K46 · Vulnerabilidades explotadas y exposiciones críticas remediadas en plazo | ≥ 70% | ACT-084 | R03 · R06 | Operaciones de seguridad y Tecnología |
| A1-O5 · Reducir la exposición en los escenarios de riesgo prioritarios. | H365 | A1-O5-KR3 · Llevar «Autenticación resistente al phishing» a 50% o más (estadio E3). | K33 · Autenticación resistente al phishing | ≥ 50% | ACT-055; ACT-087 | R06 · R08 | Identidad y acceso |
| A1-O6 · Gobernar la IA y los agentes antes de escalarlos. | H365 | A1-O6-KR1 · Llevar «Inventario de sistemas de IA y agentes» a 50% o más (estadio E3). | K49 · Inventario de sistemas de IA y agentes | ≥ 50% | ACT-043 | R08 · R37 | Responsable de IA y CISO |
| A1-O6 · Gobernar la IA y los agentes antes de escalarlos. | H365 | A1-O6-KR2 · Llevar «Agentes con dueño humano y autoridad delegada acotada» a 50% o más (estadio E3). | K50 · Agentes con dueño humano y autoridad delegada acotada | ≥ 50% | ACT-083; ACT-093 | R16 · R37 | Dueños de procesos con agentes |
| A1-O6 · Gobernar la IA y los agentes antes de escalarlos. | H365 | A1-O6-KR3 · Llevar «Casos de uso de IA con evaluación de riesgo e impacto previa» a 60% o más (estadio E3). | K51 · Casos de uso de IA con evaluación de riesgo e impacto previa | ≥ 60% | ACT-083 | R37 | Responsable de IA y CISO |

## 7. Reglas

**Metas por horizonte.** Año 1: umbral E3 del catálogo (mínimo aceptable), o E4 si la línea base ya alcanza E3. Año 2 en adelante: E4 (meta por defecto). Las metas son de referencia y se calibran con datos propios.

**Regla de revisión.** Cada indicador en uso se revisa al menos con la frecuencia con que se mide:

- R06 · Gestión: Comité operativo de seguridad (mensual): revisa los indicadores de gestión en uso.
- R12 · Gobierno: Comité de ciberriesgo (trimestral): revisa los indicadores de gobierno en uso.
- R08 · Tablero mensual: Tablero mensual de métricas: todos los indicadores del tablero con frecuencia mensual.
- R13 · Directorio: Reporte trimestral al directorio: indicadores de las preguntas Q1 a Q6.

**Cumplimiento de un hito.** Un criterio cumplido suma 1, uno parcial 0,5 (parámetro); el hito se considera cumplido con el 80% de sus criterios (parámetro), valor que también usan los OKR del año 1.

**Unidades.** En Excel los porcentajes se guardan como fracción con formato de porcentaje (75% = 0,75); en los JSON, de 0 a 100.

## 8. Uso en la evaluación y en las entrevistas

- KSG05 es el resultado de la evaluación de la gestión (nivel promedio de evidencia de las prácticas); su línea base se toma en H100 y se compara cada año en R42.
- Las prácticas EV24 (rendición de cuentas anual), EV23 (tablero), EV13 (comité), EV14, EV19 y EV01 (autoridad y dueños de riesgo) y EV06 (reevaluación anual) piden como evidencia los indicadores KSG correspondientes.
- En las entrevistas, la pregunta de fondo para el CISO y el sponsor es la de Q6: ¿qué se prometió, qué se cumplió y qué se renegoció a tiempo?
- Cada servicio sugerido declara los indicadores que mueve: el efecto de una asesoría se mide con los mismos indicadores del tablero.

## 9. Dónde está cada cosa

| Libro | Hoja | Contenido |
|---|---|---|
| AI_CISO_Atlas_CISO365_Plan_y_Ciclo_Anual_v1.0.xlsx | Indicadores del plan | 70 indicadores con actividades, primera medición, hito, rituales, coherencia, prácticas, metas y OKR |
| AI_CISO_Atlas_CISO365_Plan_y_Ciclo_Anual_v1.0.xlsx | OKR del año 1 | Definición de los 18 resultados clave, con actividades y rituales |
| AI_CISO_Atlas_CISO365_Tablero_Rendicion_de_Cuentas_v1.0.xlsx | Indicadores | Tablero del año 1 (39 indicadores) con línea base y valores por hito |
| AI_CISO_Atlas_CISO365_Tablero_Rendicion_de_Cuentas_v1.0.xlsx | OKR del año 1 | Seguimiento: meta sugerida, valor actual, avance y estado |
| AI_CISO_Atlas_CISO365_Tablero_Rendicion_de_Cuentas_v1.0.xlsx | Resumen | Síntesis por hito, por pregunta del directorio y por objetivo |
| AI_CISO_Atlas_CISO365_Evaluacion_y_Entrevistas_v1.0.xlsx | Resultados | KSG05 y resultados por línea y por hito |
| AI_CISO_Atlas_KPIs_OKRs_CISO_de_Frontera_v1.1_2026-11-10.xlsx | KPI_Sistema_Gestion · OKR_Anio1 · Plan365_Integracion · Cambios_v1.1 | Definiciones, OKR del año 1, integración y registro de cambios |


---
@SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre de 2026 · Propuesta sujeta a validación y a ajustes por organización.

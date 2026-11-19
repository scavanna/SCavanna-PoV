# Catálogo de indicadores

**Frontier CISO Atlas · Modelo Operativo CISO 365 · versión 2.0, revisión 2** · documento 05 de 16 · 15 de noviembre de 2026 · @SCavanna

> Propuesta de base, sujeta a validación y a calibración en cada organización. La ejecución se puede contratar; la rendición de cuentas, no.

## 1. Cómo leer el catálogo

El catálogo tiene 224 indicadores. **Es una lista para elegir, no un tablero**: nadie debería medirlos todos. El modelo propone un punto de partida de 42 indicadores principales, repartidos entre tres audiencias, y cada organización agrega los de las funciones donde tiene brecha.

| Campo | Qué indica |
|---|---|
| Fórmula | Cómo se calcula. Los porcentajes se expresan de 0 a 100. |
| Mejor si es | Mayor o Menor: en qué dirección mejora el indicador. |
| Umbrales E2 a E5 | Los cuatro valores que separan los estadios. El estadio alcanzado es el mayor umbral que el último valor cumple. |
| Si se externaliza | Cómo se mide cuando un proveedor opera la función (sección 4). |
| Base | Firme o Provisoria. Provisoria: se apoya en borradores o en guía de un proveedor. |
| Función | La función del modelo a la que pertenece. |

## 2. Familias y planos

| Familia | Indicadores | Origen |
|---|:--:|---|
| K01 a K64 | 64 | Catálogo 1.2, sin cambios |
| K65 a K196 | 132 | Nuevos en la versión 2.0 |
| KSG01 a KSG06 | 6 | Sistema de gestión del plan, desde la versión 1.1 |
| KX01 a KX22 | 22 | Gobierno de los servicios externalizados, nuevos |
| Total | 224 |  |

| Plano o servicio | Indicadores |
|---|:--:|
| Gobierno | 57 |
| Gestión | 55 |
| Operación · Identificar | 19 |
| Operación · Proteger | 36 |
| Operación · Detectar | 14 |
| Operación · Responder | 11 |
| Operación · Recuperar | 10 |
| Externalización | 22 |
| Total | 224 |

## 3. Estadios, metas y estados

- **Estadios.** E1 Inicial, E2 En desarrollo, E3 Definido, E4 Gestionado y E5 Optimizado.
- **Meta.** La meta propia, si se cargó; si no, el umbral del estadio objetivo, que por defecto es E4.
- **Avance.** (último valor − línea base) ÷ (meta − línea base), entre 0% y 100%; 100% si el último valor alcanza la meta.
- **Estado.** En meta; en camino con 70% o más; en riesgo entre 40% y 70%; fuera de curso por debajo.
- **Calibración.** Los umbrales de los 154 indicadores nuevos son propuestas del modelo. Se ajustan con la línea base del diagnóstico y se revisan al cierre de cada ciclo.

## 4. Cómo se mide un indicador cuando la función está externalizada

| Código | Cómo se mide | Qué significa | Indicadores |
|:--:|---|---|---|
| SLO | Nivel de servicio | Se pacta como nivel de servicio por resultado. Lo mide el proveedor y la organización lo verifica por muestreo o con una prueba independiente (KX05, KX06). | 80 |
| COM | Compartido | El proveedor ejecuta una parte o aporta el dato; la organización conserva la meta, decide y verifica. | 30 |
| INS | Insumo | El proveedor aporta insumos o evidencia; la medición y la decisión son internas. | 31 |
| INT | Interno | No se externaliza: mide una decisión o una responsabilidad que la organización no puede delegar. | 61 |
| EXT | Gobierno de la externalización | Indicador propio del gobierno de los servicios externalizados (KX): mide a la organización como contratante, no al proveedor. | 22 |
|  | Total |  | 224 |

## 5. Indicadores principales por audiencia

### Directorio y síndicos (12)

| ID | Indicador | Unidad | Mejor si es | Umbrales E2 · E3 · E4 · E5 | Función |
|---|---|---|---|---|---|
| K14 | Supervisión activa del Directorio sobre el ciberriesgo | % | Mayor | 25 · 50 · 75 · 95 | GOB-G6.1 |
| K24 | Pérdidas por incidentes frente a la tolerancia anual | % | Menor | 100 · 75 · 50 · 25 | GOB-G6.2 |
| K25 | Riesgos residuales fuera del apetito | % | Menor | 20 · 10 · 5 · 1 | GOB-G4.2 |
| K26 | Pérdida esperada de los escenarios prioritarios frente al apetito | % | Menor | 150 · 100 · 75 · 50 | GOB-G5.1 |
| K27 | Servicios críticos concentrados en un proveedor sin alternativa | % | Menor | 50 · 30 · 15 · 5 | GES-M6.2 |
| K30 | Pruebas de recuperación que cumplen RTO y RPO | % | Mayor | 40 · 60 · 80 · 95 | OPE-RC-02 |
| K58 | Calidad del reporte de ciberriesgo al Directorio | % | Mayor | 30 · 50 · 70 · 90 | GOB-G6.1 |
| K59 | Hallazgos de auditoría y de reguladores cerrados en plazo | % | Mayor | 50 · 70 · 85 · 95 | GOB-G3.2 |
| K60 | Controles clave con efectividad probada | % | Mayor | 40 · 60 · 80 · 95 | GES-M3.2 |
| K61 | Notificaciones obligatorias emitidas en plazo | % | Mayor | 60 · 80 · 95 · 100 | OPE-RS-04 |
| K98 | Decisiones automatizadas de alto impacto con supervisión humana verificada | % | Mayor | 40 · 60 · 80 · 95 | GOB-G6.2 |
| KX03 | Cumplimiento de los niveles de servicio | % | Mayor | 70 · 85 · 95 · 99 | — |

### CEO, CFO y comité ejecutivo (14)

| ID | Indicador | Unidad | Mejor si es | Umbrales E2 · E3 · E4 · E5 | Función |
|---|---|---|---|---|---|
| K09 | Procesos y activos críticos con dueño de riesgo designado | % | Mayor | 40 · 60 · 80 · 95 | GOB-G4.1 |
| K10 | Ejecutivos con objetivos de ciberseguridad en su evaluación | % | Mayor | 10 · 30 · 60 · 90 | GOB-G6.2 |
| K11 | Comportamiento seguro: tasa de reporte de phishing | % | Mayor | 10 · 25 · 45 · 65 | OPE-PR-10 |
| K12 | Cobertura de capacidades críticas del equipo de seguridad | % | Mayor | 50 · 70 · 85 · 95 | GES-M1.2 |
| K13 | Retención del talento crítico de seguridad | % | Mayor | 75 · 85 · 90 · 95 | GES-M1.2 |
| K17 | Inversión en seguridad trazada a riesgos y objetivos del negocio | % | Mayor | 40 · 60 · 80 · 95 | GOB-G1.2 |
| K18 | Avance del roadmap estratégico de seguridad | % | Mayor | 50 · 70 · 85 · 95 | GES-M1.1 |
| K19 | Reducción de riesgo por unidad de inversión | veces (x) | Mayor | 0,5 · 1 · 2 · 4 | GOB-G1.2 |
| K23 | Requisitos de seguridad de clientes y contratos cumplidos en plazo | % | Mayor | 60 · 80 · 90 · 98 | GOB-G3.1 |
| K103 | Desvío de la ejecución presupuestaria | % | Menor | 25 · 15 · 10 · 5 | GES-M1.2 |
| K104 | Gasto de seguridad con costo total conocido | % | Mayor | 40 · 60 · 80 · 95 | GES-M1.2 |
| K122 | Capacidades con herramientas solapadas sin justificación | % | Menor | 30 · 20 · 10 · 5 | GES-M3.2 |
| KX14 | Funciones críticas concentradas en un mismo proveedor | % | Menor | 60 · 45 · 30 · 20 | — |
| KX16 | Desvío del costo por unidad de resultado | % | Menor | 40 · 25 · 15 · 5 | — |

### CIO y CTO (16)

| ID | Indicador | Unidad | Mejor si es | Umbrales E2 · E3 · E4 · E5 | Función |
|---|---|---|---|---|---|
| K20 | Tiempo de habilitación segura de iniciativas | días | Menor | 20 · 10 · 5 · 2 | GES-M3.1 |
| K33 | Autenticación resistente al phishing | % | Mayor | 25 · 50 · 80 · 95 | OPE-PR-01 |
| K34 | Accesos privilegiados sin privilegios permanentes (JIT) | % | Mayor | 25 · 50 · 75 · 90 | OPE-PR-02 |
| K36 | Segmentación de activos críticos verificada | % | Mayor | 40 · 60 · 80 · 95 | OPE-PR-08 |
| K38 | Aplicaciones críticas con controles automatizados en el pipeline | % | Mayor | 30 · 50 · 75 · 90 | OPE-PR-07 |
| K41 | Cobertura de telemetría y protección de activos críticos | % | Mayor | 60 · 75 · 90 · 98 | OPE-DE-05 |
| K42 | Tiempo medio de detección (MTTD) | horas | Menor | 72 · 24 · 8 · 1 | OPE-DE-01 |
| K45 | Tiempo medio de contención (MTTC) | horas | Menor | 48 · 12 · 4 · 1 | OPE-RS-03 |
| K47 | Tiempo de restauración de servicios críticos frente al RTO | % del RTO | Menor | 200 · 150 · 100 · 75 | OPE-RC-02 |
| K116 | Iniciativas con revisión de arquitectura antes de producción | % | Mayor | 40 · 65 · 85 · 95 | GES-M3.1 |
| K118 | Accesos evaluados por política con señales de contexto | % | Mayor | 40 · 65 · 85 · 95 | GES-M3.1 |
| K120 | Desviaciones críticas de configuración abiertas | n.º | Menor | 20 · 10 · 3 · 0 | GES-M3.2 |
| K123 | Paridad de control entre entornos | % | Mayor | 40 · 60 · 80 · 95 | GES-M3.2 |
| K134 | Cuentas y suscripciones de nube bajo la línea base | % | Mayor | 50 · 75 · 90 · 98 | GES-M6.2 |
| K138 | Tiempo de corrección de vulnerabilidades críticas | días | Menor | 60 · 30 · 15 · 7 | OPE-ID-02 |
| K141 | Recursos conformes a la línea base en el entorno menos conforme | % | Mayor | 50 · 70 · 85 · 95 | OPE-ID-03 |

## 6. Catálogo completo

### Gobierno (57)

| ID | Indicador | Fórmula | Unidad | Frecuencia | Mejor si es | Umbrales E2 · E3 · E4 · E5 | Si se externaliza | Base | Función |
|---|---|---|---|---|---|---|---|---|---|
| K01 | Calibración del juicio de riesgo (puntaje de habilidad de Brier) | BSS = 1 − BS ÷ BS_ref, donde BS = (1/N) Σ (pᵢ − oᵢ)² sobre los pronósticos cerrados en el período (oᵢ = 1 si el evento ocurrió) y BS_ref usa la tasa histórica como pronóstico. | Índice | Trimestral | Mayor | 0 · 0,1 · 0,2 · 0,3 | INT | Firme | GOB-G5.1 |
| K02 | Tiempo del CISO en agenda de gobierno y negocio | Horas en agenda de gobierno y negocio ÷ horas laborales del CISO en el período × 100 (muestra de calendario o registro semanal). | % | Trimestral | Mayor | 15 · 25 · 35 · 45 | INT | Firme | GOB-G1.1 |
| K03 | Decisiones materiales con registro y revisión posterior | Decisiones materiales registradas y con revisión posterior realizada ÷ decisiones materiales del período × 100. | % | Trimestral | Mayor | 25 · 50 · 75 · 90 | INT | Firme | GOB-G6.2 |
| K04 | Aceptaciones de riesgo con alternativas, pre-mortem y vencimiento | Aceptaciones vigentes que cumplen los cinco criterios ÷ aceptaciones vigentes sobre el umbral × 100. | % | Trimestral | Mayor | 25 · 50 · 80 · 95 | INT | Firme | GOB-G5.2 |
| K08 | Escalamiento oportuno de riesgos materiales | Escalamientos realizados dentro del plazo ÷ eventos que requerían escalamiento × 100. | % | Trimestral | Mayor | 50 · 75 · 90 · 98 | INT | Firme | GOB-G4.2 |
| K09 | Procesos y activos críticos con dueño de riesgo designado | Procesos y activos críticos con dueño de riesgo formalizado ÷ procesos y activos críticos × 100. | % | Trimestral | Mayor | 40 · 60 · 80 · 95 | INT | Firme | GOB-G4.1 |
| K10 | Ejecutivos con objetivos de ciberseguridad en su evaluación | Ejecutivos con objetivos de seguridad ponderados ÷ ejecutivos del alcance × 100. | % | Anual | Mayor | 10 · 30 · 60 · 90 | INT | Firme | GOB-G6.2 |
| K14 | Supervisión activa del Directorio sobre el ciberriesgo | Sesiones con ciberriesgo en agenda y al menos una decisión o requerimiento registrado ÷ sesiones con ciberriesgo previstas en el calendario anual × 100. | % | Trimestral | Mayor | 25 · 50 · 75 · 95 | INT | Firme | GOB-G6.1 |
| K17 | Inversión en seguridad trazada a riesgos y objetivos del negocio | Presupuesto asignado a iniciativas con trazabilidad a un riesgo u objetivo ÷ presupuesto total de seguridad × 100. | % | Semestral | Mayor | 40 · 60 · 80 · 95 | INT | Firme | GOB-G1.2 |
| K19 | Reducción de riesgo por unidad de inversión | (Pérdida esperada antes − pérdida esperada después) ÷ costo anualizado de las iniciativas; cuantificación con un método explícito (p. ej., Open FAIR). | veces (x) | Anual | Mayor | 0,5 · 1 · 2 · 4 | INT | Firme | GOB-G1.2 |
| K22 | Resultados del perfil objetivo alcanzados (NIST CSF 2.0) | Subcategorías priorizadas en nivel objetivo ÷ subcategorías priorizadas del perfil objetivo × 100. | % | Anual | Mayor | 30 · 50 · 70 · 85 | INS | Firme | GOB-G2.1 |
| K23 | Requisitos de seguridad de clientes y contratos cumplidos en plazo | Requerimientos cumplidos en plazo ÷ requerimientos con vencimiento en el período × 100. | % | Trimestral | Mayor | 60 · 80 · 90 · 98 | INS | Firme | GOB-G3.1 |
| K24 | Pérdidas por incidentes frente a la tolerancia anual | Σ pérdidas por incidentes cibernéticos en 12 meses ÷ tolerancia anual de pérdida aprobada × 100. | % | Trimestral | Menor | 100 · 75 · 50 · 25 | INT | Firme | GOB-G6.2 |
| K25 | Riesgos residuales fuera del apetito | Riesgos residuales sobre la tolerancia sin plan ni aceptación vigente ÷ riesgos del registro × 100. | % | Trimestral | Menor | 20 · 10 · 5 · 1 | INT | Firme | GOB-G4.2 |
| K26 | Pérdida esperada de los escenarios prioritarios frente al apetito | Σ (frecuencia anual estimada × magnitud de pérdida) de los escenarios prioritarios ÷ apetito anual de pérdida aprobado × 100. | % | Semestral | Menor | 150 · 100 · 75 · 50 | INT | Firme | GOB-G5.1 |
| K51 | Casos de uso de IA con evaluación de riesgo e impacto previa | Casos de uso desplegados con evaluación previa aprobada ÷ casos de uso desplegados × 100. | % | Trimestral | Mayor | 40 · 60 · 80 · 95 | INT | Provisoria | GOB-G2.2 |
| K57 | Obligaciones aplicables mapeadas a controles con evidencia vigente | Obligaciones con controles asignados y evidencia vigente ÷ obligaciones aplicables identificadas × 100. | % | Trimestral | Mayor | 50 · 70 · 85 · 95 | INS | Firme | GOB-G3.2 |
| K58 | Calidad del reporte de ciberriesgo al Directorio | Criterios cumplidos ÷ 10 × 100, promedio de los reportes del período (evaluado por auditoría interna o por la secretaría del Directorio). | % | Trimestral | Mayor | 30 · 50 · 70 · 90 | INT | Firme | GOB-G6.1 |
| K59 | Hallazgos de auditoría y de reguladores cerrados en plazo | Hallazgos cerrados en plazo y validados ÷ hallazgos con vencimiento en el período × 100. | % | Trimestral | Mayor | 50 · 70 · 85 · 95 | INS | Firme | GOB-G3.2 |
| K63 | Excepciones a políticas vigentes, justificadas y con vencimiento | Excepciones vigentes con justificación, compensación, aprobación y sin vencer ÷ excepciones vigentes × 100. | % | Trimestral | Mayor | 40 · 60 · 80 · 95 | INT | Firme | GOB-G2.2 |
| K65 | Elementos del mandato del CISO aprobados y vigentes | Elementos del mandato aprobados y revisados en los últimos 12 meses (alcance, autoridad, línea de reporte, acceso al directorio, presupuesto y derechos de decisión) ÷ 6 × 100. | % | Anual | Mayor | 50 · 67 · 83 · 100 | INT | Firme | GOB-G1.1 |
| K66 | Partes interesadas clave con expectativas relevadas y vigentes | Partes interesadas del mapa con expectativas documentadas y revisadas en los últimos 12 meses ÷ partes interesadas del mapa × 100. | % | Semestral | Mayor | 40 · 60 · 80 · 95 | INT | Firme | GOB-G1.1 |
| K67 | Responsabilidades del CISO sin autoridad equivalente | Cantidad de responsabilidades asignadas a la función de seguridad para las que no tiene autoridad de decisión, presupuesto ni vía de escalamiento. | n.º | Semestral | Menor | 6 · 3 · 1 · 0 | INT | Firme | GOB-G1.1 |
| K68 | Objetivos del negocio con objetivo de seguridad asociado | Objetivos estratégicos del negocio con al menos un objetivo de seguridad trazado ÷ objetivos estratégicos × 100. | % | Anual | Mayor | 40 · 60 · 80 · 95 | INT | Firme | GOB-G1.2 |
| K69 | Iniciativas estratégicas con seguridad desde el diseño | Iniciativas estratégicas del negocio y de tecnología en las que seguridad participó antes de aprobarse el diseño ÷ iniciativas estratégicas × 100. | % | Trimestral | Mayor | 40 · 60 · 80 · 95 | INT | Firme | GOB-G1.2 |
| K70 | Deuda de seguridad con dueño, costo y fecha | Elementos de deuda de seguridad registrados con dueño, costo estimado y fecha de resolución ÷ elementos registrados × 100. | % | Trimestral | Mayor | 40 · 60 · 80 · 95 | INT | Firme | GOB-G1.2 |
| K71 | Cruces de la grilla de propiedad con dueño designado | Cruces aplicables entre función del marco y dominio Zero Trust con dueño nominado ÷ cruces aplicables × 100. | % | Trimestral | Mayor | 50 · 75 · 90 · 100 | INT | Firme | GOB-G2.1 |
| K72 | Antigüedad del perfil actual y objetivo | Meses transcurridos desde la última actualización aprobada del perfil actual y del perfil objetivo del marco de referencia. | meses | Semestral | Menor | 24 · 12 · 6 · 3 | INS | Firme | GOB-G2.1 |
| K73 | Requisitos del marco adoptado asignados a un control con dueño | Requisitos aplicables del marco de referencia cubiertos por al menos un control con dueño ÷ requisitos aplicables × 100. | % | Semestral | Mayor | 50 · 70 · 90 · 98 | INS | Firme | GOB-G2.1 |
| K74 | Políticas y estándares dentro de su ciclo de revisión | Documentos normativos revisados dentro del plazo definido ÷ documentos normativos vigentes × 100. | % | Semestral | Mayor | 50 · 70 · 90 · 98 | INS | Firme | GOB-G2.2 |
| K75 | Requisitos técnicos de política con verificación automática | Requisitos técnicos de las políticas comprobados por reglas automáticas ÷ requisitos técnicos × 100. | % | Trimestral | Mayor | 20 · 40 · 65 · 85 | COM | Firme | GOB-G2.2 |
| K76 | Desvíos de política detectados por verificación propia | Desvíos de política detectados por medición o verificación propia ÷ desvíos conocidos por cualquier vía (incluidos incidentes y auditorías) × 100. | % | Trimestral | Mayor | 40 · 60 · 80 · 90 | COM | Firme | GOB-G2.2 |
| K77 | Obligaciones aplicables con dueño y fecha de revisión | Obligaciones legales, regulatorias y contractuales con dueño y revisión vigente ÷ obligaciones del inventario × 100. | % | Semestral | Mayor | 50 · 70 · 90 · 98 | INS | Firme | GOB-G3.1 |
| K78 | Cambios regulatorios evaluados en plazo | Cambios regulatorios relevantes con evaluación de impacto dentro del plazo definido ÷ cambios relevantes identificados × 100. | % | Trimestral | Mayor | 50 · 70 · 90 · 98 | INS | Firme | GOB-G3.1 |
| K79 | Almacenes de datos críticos con localización verificada | Almacenes de datos críticos con ubicación geográfica y requisitos de residencia verificados ÷ almacenes de datos críticos × 100. | % | Semestral | Mayor | 40 · 60 · 80 · 95 | SLO | Firme | GOB-G3.1 |
| K80 | Controles clave con evidencia recolectada de forma automática | Controles clave cuya evidencia se obtiene sin intervención manual ÷ controles clave × 100. | % | Trimestral | Mayor | 20 · 40 · 65 · 85 | COM | Firme | GOB-G3.2 |
| K81 | Hallazgos repetidos en revisiones sucesivas | Hallazgos de auditoría o del regulador que repiten uno anterior ÷ hallazgos del período × 100. | % | Anual | Menor | 30 · 20 · 10 · 5 | INS | Firme | GOB-G3.2 |
| K82 | Cobertura del plan de aseguramiento | Revisiones independientes realizadas ÷ revisiones planificadas para el período × 100. | % | Semestral | Mayor | 50 · 70 · 90 · 98 | INS | Firme | GOB-G3.2 |
| K83 | Riesgos del registro con dueño, tratamiento y revisión vigentes | Riesgos con dueño, decisión de tratamiento y revisión dentro del plazo ÷ riesgos del registro × 100. | % | Trimestral | Mayor | 50 · 70 · 90 · 98 | INT | Firme | GOB-G4.1 |
| K84 | Riesgos de ciberseguridad integrados al registro de la empresa | Riesgos altos de ciberseguridad presentes en el registro de riesgos corporativo ÷ riesgos altos de ciberseguridad × 100. | % | Semestral | Mayor | 40 · 60 · 80 · 95 | INT | Firme | GOB-G4.1 |
| K85 | Riesgos altos con revisión independiente reciente | Riesgos altos cubiertos por auditoría interna o revisión independiente en los últimos 24 meses ÷ riesgos altos × 100. | % | Anual | Mayor | 30 · 50 · 70 · 90 | INS | Firme | GOB-G4.1 |
| K86 | Declaraciones de apetito con umbrales medibles | Escenarios prioritarios con umbral de apetito expresado en un indicador ÷ escenarios prioritarios × 100. | % | Semestral | Mayor | 40 · 60 · 80 · 95 | INT | Firme | GOB-G4.2 |
| K87 | Umbrales de apetito superados con decisión en plazo | Superaciones de umbral con decisión registrada dentro del plazo definido ÷ superaciones de umbral × 100. | % | Trimestral | Mayor | 50 · 70 · 90 · 98 | INT | Firme | GOB-G4.2 |
| K88 | Tipos de acción de agentes con nivel de autonomía aprobado | Tipos de acción de los agentes en producción con nivel de autonomía aprobado por el dueño del riesgo ÷ tipos de acción × 100. | % | Trimestral | Mayor | 40 · 60 · 80 · 95 | INT | Provisoria | GOB-G4.2 |
| K89 | Escenarios prioritarios cuantificados | Escenarios prioritarios con estimación de frecuencia y de rango de pérdida ÷ escenarios prioritarios × 100. | % | Semestral | Mayor | 25 · 50 · 80 · 95 | INS | Firme | GOB-G5.1 |
| K90 | Evaluaciones de riesgo actualizadas ante cambios materiales | Cambios materiales (iniciativas, adquisiciones, incidentes, proveedores nuevos) con evaluación de riesgo actualizada en plazo ÷ cambios materiales × 100. | % | Trimestral | Mayor | 40 · 60 · 80 · 95 | INS | Firme | GOB-G5.1 |
| K91 | Servicios críticos con evaluación de riesgo vigente | Servicios críticos del negocio con evaluación de riesgo de los últimos 12 meses ÷ servicios críticos × 100. | % | Semestral | Mayor | 40 · 60 · 80 · 95 | INS | Firme | GOB-G5.1 |
| K92 | Planes de tratamiento en plazo | Acciones de tratamiento cumplidas o en curso dentro de su fecha ÷ acciones de tratamiento comprometidas × 100. | % | Trimestral | Mayor | 50 · 70 · 85 · 95 | COM | Firme | GOB-G5.2 |
| K93 | Aceptaciones de riesgo vencidas sin renovar | Aceptaciones de riesgo con vencimiento superado y sin decisión de renovación o de tratamiento ÷ aceptaciones vigentes × 100. | % | Trimestral | Menor | 20 · 10 · 5 · 0 | INT | Firme | GOB-G5.2 |
| K94 | Tratamientos con reducción de riesgo verificada | Tratamientos cerrados cuya reducción de riesgo se verificó con medición o prueba ÷ tratamientos cerrados × 100. | % | Semestral | Mayor | 30 · 50 · 75 · 90 | INS | Firme | GOB-G5.2 |
| K95 | Decisiones solicitadas a la dirección resueltas en plazo | Decisiones pedidas al comité ejecutivo o al directorio resueltas dentro del plazo solicitado ÷ decisiones pedidas × 100. | % | Trimestral | Mayor | 40 · 60 · 80 · 95 | INT | Firme | GOB-G6.1 |
| K96 | Utilidad del reporte de ciberriesgo para sus destinatarios | Destinatarios que califican el reporte como útil para decidir (4 o 5 sobre 5) ÷ destinatarios consultados × 100. | % | Anual | Mayor | 40 · 60 · 80 · 90 | INT | Firme | GOB-G6.1 |
| K97 | Declaraciones de conflicto de interés vigentes | Integrantes del equipo de seguridad y proveedores críticos con declaración vigente ÷ obligados a declarar × 100. | % | Anual | Mayor | 50 · 75 · 90 · 100 | INS | Firme | GOB-G6.2 |
| K98 | Decisiones automatizadas de alto impacto con supervisión humana verificada | Tipos de decisión automatizada de alto impacto con supervisión humana comprobada por muestreo ÷ tipos de decisión automatizada de alto impacto × 100. | % | Semestral | Mayor | 40 · 60 · 80 · 95 | INT | Provisoria | GOB-G6.2 |
| KSG03 | Decisiones materiales tomadas por el rol con autoridad | Decisiones de la muestra tomadas por el rol con autoridad (A) y en plazo ÷ decisiones materiales de la muestra × 100. | % | Trimestral | Mayor | 40 · 60 · 80 · 95 | INT | Firme | GOB-G4.1 |
| KSG04 | Indicadores del tablero con línea base, dueño y fuente | Indicadores del tablero con línea base, dueño, fuente y fórmula documentados ÷ indicadores del tablero × 100. | % | Trimestral | Mayor | 40 · 60 · 80 · 95 | INT | Firme | GOB-G6.2 |
| KSG06 | Compromisos de rendición de cuentas cumplidos o renegociados a tiempo | (Compromisos cumplidos en fecha + compromisos renegociados antes del vencimiento) ÷ compromisos con vencimiento en el período × 100. | % | Trimestral | Mayor | 50 · 70 · 85 · 95 | INT | Firme | GOB-G6.1 |

### Gestión (55)

| ID | Indicador | Fórmula | Unidad | Frecuencia | Mejor si es | Umbrales E2 · E3 · E4 · E5 | Si se externaliza | Base | Función |
|---|---|---|---|---|---|---|---|---|---|
| K06 | Revisiones post-incidente que evalúan decisiones | Revisiones con análisis de decisiones y al menos un cambio de criterio aprobado ÷ incidentes mayores cerrados × 100. | % | Trimestral | Mayor | 25 · 50 · 75 · 95 | INT | Firme | GES-M5.2 |
| K07 | Competencias de liderazgo y juicio demostradas | Competencias demostradas con evidencia ÷ competencias requeridas en el plan del período × 100. | % | Semestral | Mayor | 25 · 50 · 75 · 90 | INT | Firme | GES-M1.2 |
| K12 | Cobertura de capacidades críticas del equipo de seguridad | Capacidades críticas cubiertas con competencia demostrada ÷ capacidades críticas del modelo × 100. | % | Semestral | Mayor | 50 · 70 · 85 · 95 | INT | Firme | GES-M1.2 |
| K13 | Retención del talento crítico de seguridad | (1 − bajas voluntarias en roles críticos ÷ dotación promedio en roles críticos) × 100, en 12 meses móviles. | % | Semestral | Mayor | 75 · 85 · 90 · 95 | INT | Firme | GES-M1.2 |
| K18 | Avance del roadmap estratégico de seguridad | Σ peso de riesgo de los hitos completados en plazo y presupuesto ÷ Σ peso de riesgo de los hitos comprometidos para el período × 100. | % | Trimestral | Mayor | 50 · 70 · 85 · 95 | INT | Firme | GES-M1.1 |
| K20 | Tiempo de habilitación segura de iniciativas | Mediana de días hábiles (solicitud → decisión de seguridad documentada) en el período. | días | Trimestral | Menor | 20 · 10 · 5 · 2 | INT | Firme | GES-M3.1 |
| K21 | Procesos críticos con BIA vigente y dependencias mapeadas | Procesos críticos con BIA de menos de 12 meses y mapa de dependencias ÷ procesos críticos × 100. | % | Semestral | Mayor | 40 · 60 · 80 · 95 | INT | Firme | GES-M5.1 |
| K27 | Servicios críticos concentrados en un proveedor sin alternativa | Servicios críticos con proveedor único sin plan de salida ni alternativa probada ÷ servicios críticos × 100. | % | Semestral | Menor | 50 · 30 · 15 · 5 | INS | Firme | GES-M6.2 |
| K32 | Escenarios críticos con playbook probado | Escenarios prioritarios con playbook aprobado y probado en 12 meses ÷ escenarios prioritarios × 100. | % | Semestral | Mayor | 30 · 50 · 75 · 90 | INS | Firme | GES-M5.1 |
| K48 | Acciones correctivas post-incidente cerradas en plazo | Acciones correctivas cerradas en plazo y verificadas ÷ acciones correctivas con vencimiento en el período × 100. | % | Trimestral | Mayor | 50 · 70 · 85 · 95 | COM | Firme | GES-M5.2 |
| K50 | Agentes con dueño humano y autoridad delegada acotada | Agentes en producción que cumplen los cinco requisitos ÷ agentes en producción × 100; se informa además la relación de agentes por dueño humano. | % | Mensual | Mayor | 30 · 50 · 75 · 95 | SLO | Provisoria | GES-M2.2 |
| K60 | Controles clave con efectividad probada | Controles clave con prueba de efectividad satisfactoria en el período ÷ controles clave × 100. | % | Trimestral | Mayor | 40 · 60 · 80 · 95 | INS | Firme | GES-M3.2 |
| K62 | Incidentes de terceros notificados en el plazo contractual | Incidentes de terceros notificados en el plazo contractual ÷ incidentes de terceros conocidos que afectaron a la organización × 100. | % | Trimestral | Mayor | 40 · 60 · 80 · 95 | SLO | Firme | GES-M6.2 |
| K64 | Tratamientos de datos personales de alto riesgo con evaluación de impacto | Tratamientos de alto riesgo con evaluación de impacto vigente y medidas implementadas ÷ tratamientos de alto riesgo inventariados × 100. | % | Semestral | Mayor | 30 · 50 · 75 · 95 | INT | Firme | GES-M2.1 |
| K99 | Productos-control con dueño, objetivo y evidencia | Controles del portafolio con dueño, objetivo medible, configuración de referencia y evidencia definidos ÷ controles del portafolio × 100. | % | Trimestral | Mayor | 30 · 60 · 80 · 95 | COM | Firme | GES-M1.1 |
| K100 | Cadencias operativas cumplidas | Tareas de cadencia (diarias, semanales, mensuales y trimestrales) realizadas ÷ tareas de cadencia programadas × 100. | % | Mensual | Mayor | 50 · 70 · 85 · 95 | SLO | Firme | GES-M1.1 |
| K101 | Trabajo no planificado del equipo | Horas dedicadas a trabajo no planificado ÷ horas disponibles × 100. | % | Mensual | Menor | 60 · 45 · 30 · 20 | INT | Firme | GES-M1.1 |
| K102 | Iniciativas con beneficio verificado al cierre | Iniciativas cerradas cuyo beneficio comprometido se midió y se alcanzó ÷ iniciativas cerradas × 100. | % | Semestral | Mayor | 30 · 50 · 70 · 85 | INT | Firme | GES-M1.1 |
| K103 | Desvío de la ejecución presupuestaria | Valor absoluto de (gasto real − gasto planificado) ÷ gasto planificado × 100, acumulado del año. | % | Trimestral | Menor | 25 · 15 · 10 · 5 | INT | Firme | GES-M1.2 |
| K104 | Gasto de seguridad con costo total conocido | Gasto de seguridad con costo total identificado (licencias, operación, personas y servicios) ÷ gasto de seguridad × 100. | % | Semestral | Mayor | 40 · 60 · 80 · 95 | INT | Firme | GES-M1.2 |
| K105 | Planes de desarrollo individual cumplidos | Integrantes del equipo con el plan de desarrollo cumplido en el período ÷ integrantes del equipo × 100. | % | Semestral | Mayor | 40 · 60 · 80 · 90 | INT | Firme | GES-M1.2 |
| K106 | Personal de funciones de alto riesgo con formación específica vigente | Personas con funciones de alto riesgo (administradores, finanzas, desarrollo y dirección) con formación específica de los últimos 12 meses ÷ personas con funciones de alto riesgo × 100. | % | Semestral | Mayor | 40 · 60 · 85 · 95 | SLO | Firme | GES-M1.2 |
| K107 | Tareas operativas con responsable definido por tipo | Tareas del catálogo operativo con responsable definido como persona, proveedor o agente ÷ tareas del catálogo × 100. | % | Trimestral | Mayor | 40 · 65 · 85 · 100 | COM | Firme | GES-M1.2 |
| K108 | Desvío del costo por tarea automatizada | Valor absoluto de (costo real por tarea − costo previsto) ÷ costo previsto × 100, para las tareas ejecutadas por agentes. | % | Trimestral | Menor | 40 · 25 · 10 · 5 | COM | Provisoria | GES-M1.2 |
| K109 | Activos críticos con dueño y clasificación | Activos críticos con dueño nominado y clasificación asignada ÷ activos críticos × 100. | % | Trimestral | Mayor | 50 · 70 · 90 · 98 | INS | Firme | GES-M2.1 |
| K111 | Repositorios con política de retención aplicada | Repositorios de datos con regla de retención y de eliminación aplicada ÷ repositorios del alcance × 100. | % | Semestral | Mayor | 25 · 50 · 75 · 90 | COM | Firme | GES-M2.1 |
| K114 | Accesos recertificados en plazo | Accesos a sistemas críticos recertificados por su responsable dentro del plazo ÷ accesos sujetos a recertificación × 100. | % | Trimestral | Mayor | 50 · 75 · 90 · 98 | COM | Firme | GES-M2.2 |
| K115 | Aplicaciones críticas integradas a la identidad central | Aplicaciones críticas que autentican contra el proveedor de identidad central ÷ aplicaciones críticas × 100. | % | Trimestral | Mayor | 50 · 70 · 90 · 98 | INS | Firme | GES-M2.2 |
| K116 | Iniciativas con revisión de arquitectura antes de producción | Iniciativas puestas en producción con revisión de arquitectura de seguridad aprobada ÷ iniciativas puestas en producción × 100. | % | Trimestral | Mayor | 40 · 65 · 85 · 95 | INT | Firme | GES-M3.1 |
| K117 | Despliegues sobre patrones de referencia aprobados | Despliegues nuevos que usan un patrón seguro aprobado ÷ despliegues nuevos × 100. | % | Trimestral | Mayor | 30 · 55 · 80 · 95 | COM | Firme | GES-M3.1 |
| K118 | Accesos evaluados por política con señales de contexto | Solicitudes de acceso a recursos críticos decididas por una política que evalúa identidad, dispositivo y contexto ÷ solicitudes de acceso a recursos críticos × 100. | % | Trimestral | Mayor | 40 · 65 · 85 · 95 | COM | Firme | GES-M3.1 |
| K119 | Excepciones de arquitectura con revisión vencida | Excepciones de arquitectura con fecha de revisión vencida ÷ excepciones de arquitectura vigentes × 100. | % | Semestral | Menor | 30 · 20 · 10 · 5 | INT | Firme | GES-M3.1 |
| K120 | Desviaciones críticas de configuración abiertas | Cantidad de desviaciones críticas respecto de la configuración de referencia abiertas al cierre del período. | n.º | Mensual | Menor | 20 · 10 · 3 · 0 | SLO | Firme | GES-M3.2 |
| K121 | Tiempo de corrección de la deriva crítica | Mediana de días entre la detección de una desviación crítica y su corrección. | días | Mensual | Menor | 30 · 14 · 7 · 2 | SLO | Firme | GES-M3.2 |
| K122 | Capacidades con herramientas solapadas sin justificación | Capacidades de seguridad cubiertas por dos o más herramientas sin justificación aprobada ÷ capacidades del inventario × 100. | % | Semestral | Menor | 30 · 20 · 10 · 5 | INT | Firme | GES-M3.2 |
| K123 | Paridad de control entre entornos | Cobertura de control del entorno menos cubierto ÷ cobertura del entorno más cubierto × 100. | % | Trimestral | Mayor | 40 · 60 · 80 · 95 | SLO | Firme | GES-M3.2 |
| K124 | Casos de uso de detección con dueño, prueba y revisión vigentes | Casos de uso con dueño, prueba y revisión de los últimos 12 meses ÷ casos de uso activos × 100. | % | Trimestral | Mayor | 40 · 60 · 80 · 95 | SLO | Firme | GES-M4.1 |
| K125 | Carga por analista | Mediana de alertas que requieren análisis humano por analista y por turno. | n.º | Mensual | Menor | 60 · 40 · 25 · 15 | SLO | Firme | GES-M4.1 |
| K126 | Servicios críticos con modelo de amenazas vigente | Servicios críticos con modelo de amenazas de los últimos 12 meses ÷ servicios críticos × 100. | % | Semestral | Mayor | 25 · 50 · 75 · 90 | INS | Firme | GES-M4.2 |
| K128 | Riesgos emergentes evaluados en plazo | Riesgos emergentes con evaluación dentro del plazo definido desde su identificación ÷ riesgos emergentes identificados × 100. | % | Trimestral | Mayor | 40 · 60 · 80 · 95 | INS | Firme | GES-M4.2 |
| K129 | Personas con rol en la respuesta entrenadas | Personas con rol en el plan de respuesta que participaron en una formación o un ejercicio en los últimos 12 meses ÷ personas con rol × 100. | % | Semestral | Mayor | 40 · 60 · 80 · 95 | COM | Firme | GES-M5.1 |
| K130 | Acuerdos y contactos de respuesta vigentes y verificados | Acuerdos y contactos de apoyo (respuesta, forense, legal, comunicación, seguro y autoridad) vigentes y verificados en el semestre ÷ acuerdos y contactos requeridos × 100. | % | Semestral | Mayor | 50 · 70 · 90 · 100 | INS | Firme | GES-M5.1 |
| K131 | Hallazgos de ejercicios corregidos en plazo | Hallazgos de ejercicios y simulacros corregidos dentro de su fecha ÷ hallazgos con fecha vencida × 100. | % | Trimestral | Mayor | 40 · 60 · 80 · 95 | COM | Firme | GES-M5.1 |
| K132 | Proveedores críticos con evidencia de control actualizada | Proveedores críticos con evidencia de control (informe independiente, prueba o auditoría) de los últimos 12 meses ÷ proveedores críticos × 100. | % | Semestral | Mayor | 40 · 60 · 85 · 95 | INS | Firme | GES-M6.2 |
| K133 | Aplicaciones críticas con inventario de componentes de terceros | Aplicaciones críticas con inventario de componentes actualizado en cada entrega ÷ aplicaciones críticas × 100. | % | Trimestral | Mayor | 25 · 50 · 75 · 90 | SLO | Firme | GES-M6.2 |
| K134 | Cuentas y suscripciones de nube bajo la línea base | Cuentas, suscripciones o proyectos de nube incorporados a la línea base y a la vigilancia ÷ cuentas, suscripciones o proyectos existentes × 100. | % | Mensual | Mayor | 50 · 75 · 90 · 98 | SLO | Firme | GES-M6.2 |
| K135 | Servicios críticos con telemetría, identidad y evidencia portables | Servicios críticos cuya telemetría, identidad y evidencia usan formatos y protocolos abiertos o exportables ÷ servicios críticos × 100. | % | Anual | Mayor | 25 · 50 · 75 · 90 | SLO | Firme | GES-M6.2 |
| K183 | Cobertura horaria efectiva de la vigilancia | Horas de la semana con vigilancia activa y capacidad de respuesta ÷ 168 × 100. | % | Trimestral | Mayor | 30 · 60 · 90 · 100 | SLO | Firme | GES-M4.1 |
| K184 | Incidentes significativos con revisión posterior en plazo | Incidentes significativos con revisión posterior realizada dentro del plazo definido ÷ incidentes significativos × 100. | % | Trimestral | Mayor | 50 · 70 · 90 · 100 | COM | Firme | GES-M5.2 |
| K185 | Servicios críticos con objetivos de recuperación aprobados por el negocio | Servicios críticos con objetivo de tiempo y de punto de recuperación aprobados por su dueño en los últimos 12 meses ÷ servicios críticos × 100. | % | Semestral | Mayor | 40 · 65 · 85 · 98 | INT | Firme | GES-M6.1 |
| K186 | Planes de continuidad y recuperación actualizados | Planes revisados en los últimos 12 meses o tras un cambio mayor ÷ planes × 100. | % | Semestral | Mayor | 40 · 65 · 85 · 95 | COM | Firme | GES-M6.1 |
| K188 | Vulnerabilidades críticas fuera de plazo con decisión de riesgo | Vulnerabilidades críticas fuera de plazo con aceptación de riesgo o plan aprobado ÷ vulnerabilidades críticas fuera de plazo × 100. | % | Mensual | Mayor | 40 · 60 · 80 · 95 | INT | Firme | GES-M4.2 |
| KSG01 | Criterios de salida de los hitos cumplidos en fecha | (Criterios cumplidos + valor parcial × criterios parciales) ÷ criterios exigibles a la fecha × 100. Valor parcial por defecto: 0,5. | % | Por hito · trimestral | Mayor | 50 · 70 · 85 · 95 | INT | Firme | GES-M1.1 |
| KSG02 | Rituales del ciclo de gobierno realizados según el calendario | Rituales realizados en ventana y con acta ÷ rituales programados para el período × 100. | % | Trimestral | Mayor | 50 · 70 · 85 · 95 | INT | Firme | GES-M1.1 |
| KSG05 | Nivel de evidencia de las prácticas de gobierno y gestión | Promedio del nivel actual (0 a 4) de las prácticas evaluadas; se informa junto con la cantidad de prácticas críticas en nivel 0. | nivel (0 a 4) | Anual · línea base en H100 | Mayor | 1 · 2 · 3 · 3,5 | INT | Firme | GES-M1.1 |

### Operación · Identificar (19)

| ID | Indicador | Fórmula | Unidad | Frecuencia | Mejor si es | Umbrales E2 · E3 · E4 · E5 | Si se externaliza | Base | Función |
|---|---|---|---|---|---|---|---|---|---|
| K31 | Proveedores críticos evaluados y con cláusulas de seguridad | Proveedores críticos con evaluación de menos de 12 meses, cláusulas vigentes y monitoreo ÷ proveedores críticos × 100. | % | Trimestral | Mayor | 40 · 60 · 80 · 95 | INS | Firme | OPE-ID-04 |
| K35 | Activos conformes a la línea base de configuración segura | Activos conformes a la línea base (con soporte vigente o compensación aprobada) ÷ activos del alcance × 100. | % | Mensual | Mayor | 50 · 70 · 85 · 95 | SLO | Firme | OPE-ID-03 |
| K39 | Cobertura del inventario de activos (TI, nube, OT e IoT) | Activos descubiertos que figuran en el inventario con dueño y criticidad ÷ activos descubiertos × 100. | % | Mensual | Mayor | 60 · 75 · 90 · 98 | SLO | Firme | OPE-ID-01 |
| K46 | Vulnerabilidades explotadas y exposiciones críticas remediadas en plazo | Vulnerabilidades explotadas o exposiciones críticas remediadas o mitigadas en plazo ÷ las que vencieron en el período × 100. | % | Mensual | Mayor | 50 · 70 · 85 · 95 | SLO | Firme | OPE-ID-02 |
| K49 | Inventario de sistemas de IA y agentes | Sistemas de IA y agentes registrados con dueño, propósito y riesgo ÷ sistemas de IA y agentes descubiertos × 100. | % | Mensual | Mayor | 30 · 50 · 75 · 95 | SLO | Provisoria | OPE-ID-07 |
| K54 | Hallazgos críticos de red teaming de IA corregidos | Hallazgos críticos o altos de red teaming de IA corregidos en plazo ÷ hallazgos críticos o altos con vencimiento × 100. | % | Trimestral | Mayor | 40 · 60 · 80 · 95 | COM | Provisoria | OPE-ID-05 |
| K110 | Cobertura del descubrimiento de datos sensibles | Repositorios analizados por el descubrimiento automático ÷ repositorios del alcance × 100. | % | Trimestral | Mayor | 30 · 55 · 80 · 95 | SLO | Firme | OPE-ID-06 |
| K136 | Activos no gestionados regularizados en plazo | Activos detectados fuera del inventario que se incorporaron o se retiraron dentro del plazo ÷ activos detectados fuera del inventario × 100. | % | Mensual | Mayor | 40 · 60 · 80 · 95 | SLO | Firme | OPE-ID-01 |
| K137 | Activos expuestos a internet sin inventariar | Cantidad de activos expuestos a internet detectados que no figuran en el inventario al cierre del período. | n.º | Mensual | Menor | 20 · 10 · 3 · 0 | SLO | Firme | OPE-ID-01 |
| K138 | Tiempo de corrección de vulnerabilidades críticas | Mediana de días entre la detección de una vulnerabilidad crítica y su corrección o mitigación verificada. | días | Mensual | Menor | 60 · 30 · 15 · 7 | SLO | Firme | OPE-ID-02 |
| K139 | Cobertura de la evaluación de vulnerabilidades | Activos del alcance evaluados en el ciclo ÷ activos del alcance × 100. | % | Mensual | Mayor | 50 · 75 · 90 · 98 | SLO | Firme | OPE-ID-02 |
| K140 | Rutas de ataque abiertas hacia activos críticos | Cantidad de rutas de ataque conocidas hacia activos críticos sin corregir al cierre del período. | n.º | Mensual | Menor | 20 · 10 · 3 · 0 | SLO | Firme | OPE-ID-02 |
| K141 | Recursos conformes a la línea base en el entorno menos conforme | Recursos conformes ÷ recursos evaluados × 100, en el entorno con menor cumplimiento. | % | Mensual | Mayor | 50 · 70 · 85 · 95 | SLO | Firme | OPE-ID-03 |
| K142 | Hallazgos críticos de postura fuera de plazo | Cantidad de hallazgos críticos de postura abiertos más allá del plazo de corrección. | n.º | Mensual | Menor | 20 · 10 · 3 · 0 | SLO | Firme | OPE-ID-03 |
| K143 | Hallazgos de terceros críticos corregidos en plazo | Hallazgos de evaluaciones de proveedores críticos corregidos dentro de su fecha ÷ hallazgos con fecha vencida × 100. | % | Trimestral | Mayor | 40 · 60 · 80 · 95 | INS | Firme | OPE-ID-04 |
| K144 | Hallazgos críticos de pruebas ofensivas corregidos y revalidados | Hallazgos críticos corregidos y revalidados dentro del plazo ÷ hallazgos críticos con plazo vencido × 100. | % | Trimestral | Mayor | 40 · 60 · 80 · 95 | COM | Firme | OPE-ID-05 |
| K145 | Escenarios prioritarios validados con simulación | Escenarios de riesgo prioritarios sometidos a una simulación o a un ejercicio de adversario en los últimos 12 meses ÷ escenarios prioritarios × 100. | % | Semestral | Mayor | 25 · 50 · 75 · 90 | COM | Firme | OPE-ID-05 |
| K187 | Sistemas de IA y agentes sin dueño o sin uso regularizados en plazo | Sistemas de IA y agentes detectados sin dueño o sin actividad que se regularizaron o se retiraron dentro del plazo ÷ detectados × 100. | % | Trimestral | Mayor | 40 · 60 · 80 · 95 | SLO | Provisoria | OPE-ID-07 |
| K194 | Repositorios con datos sensibles sin dueño | Repositorios con datos sensibles sin un dueño de datos nominado ÷ repositorios con datos sensibles × 100. | % | Trimestral | Menor | 40 · 25 · 10 · 5 | INS | Firme | OPE-ID-06 |

### Operación · Proteger (36)

| ID | Indicador | Fórmula | Unidad | Frecuencia | Mejor si es | Umbrales E2 · E3 · E4 · E5 | Si se externaliza | Base | Función |
|---|---|---|---|---|---|---|---|---|---|
| K11 | Comportamiento seguro: tasa de reporte de phishing | Usuarios que reportaron la simulación ÷ usuarios que la recibieron × 100 (promedio de las campañas del período). | % | Trimestral | Mayor | 10 · 25 · 45 · 65 | COM | Firme | OPE-PR-10 |
| K33 | Autenticación resistente al phishing | Cuentas con método resistente al phishing exigido por política ÷ cuentas del alcance × 100 (informar las privilegiadas por separado). | % | Mensual | Mayor | 25 · 50 · 80 · 95 | SLO | Firme | OPE-PR-01 |
| K34 | Accesos privilegiados sin privilegios permanentes (JIT) | Asignaciones privilegiadas elegibles o justo a tiempo ÷ total de asignaciones privilegiadas (permanentes + elegibles) × 100. | % | Mensual | Mayor | 25 · 50 · 75 · 90 | SLO | Firme | OPE-PR-02 |
| K36 | Segmentación de activos críticos verificada | Zonas o activos críticos con segmentación verificada en los últimos seis meses ÷ zonas o activos críticos del diseño × 100. | % | Trimestral | Mayor | 40 · 60 · 80 · 95 | SLO | Firme | OPE-PR-08 |
| K37 | Datos sensibles clasificados y protegidos | Repositorios sensibles clasificados y con los controles requeridos ÷ repositorios sensibles descubiertos × 100. | % | Trimestral | Mayor | 30 · 50 · 75 · 90 | SLO | Firme | OPE-PR-06 |
| K38 | Aplicaciones críticas con controles automatizados en el pipeline | Aplicaciones críticas con los cuatro controles activos y umbrales bloqueantes ÷ aplicaciones críticas × 100. | % | Trimestral | Mayor | 30 · 50 · 75 · 90 | SLO | Firme | OPE-PR-07 |
| K40 | Zonas OT e IIoT que alcanzan su nivel de seguridad objetivo | Zonas con SL-A ≥ SL-T verificado ÷ zonas con SL-T definido × 100. | % | Semestral | Mayor | 20 · 40 · 70 · 90 | SLO | Firme | OPE-PR-12 |
| K52 | Interacciones con IA protegidas contra la fuga de datos | Interacciones con IA bajo controles de DLP y de etiquetas ÷ interacciones con IA observadas × 100 (alternativa: usuarios activos de IA cubiertos ÷ usuarios activos de IA). | % | Mensual | Mayor | 30 · 50 · 75 · 95 | SLO | Provisoria | OPE-PR-06 |
| K112 | Identidades con ciclo de vida automatizado | Identidades de personas cuyas altas, cambios y bajas se disparan desde la fuente de personal ÷ identidades de personas × 100. | % | Trimestral | Mayor | 40 · 65 · 85 · 95 | SLO | Firme | OPE-PR-01 |
| K113 | Tiempo de revocación de accesos tras la baja | Mediana de horas entre la baja efectiva de la persona y la revocación de todos sus accesos. | horas | Mensual | Menor | 72 · 24 · 8 · 1 | SLO | Firme | OPE-PR-01 |
| K146 | Sesiones privilegiadas registradas y desde estación segura | Sesiones privilegiadas sobre sistemas críticos con registro y desde una estación dedicada ÷ sesiones privilegiadas sobre sistemas críticos × 100. | % | Mensual | Mayor | 40 · 65 · 85 · 98 | SLO | Firme | OPE-PR-02 |
| K147 | Cuentas de emergencia probadas y vigiladas | Cuentas de emergencia con prueba de acceso en el semestre y alerta de uso activa ÷ cuentas de emergencia × 100. | % | Semestral | Mayor | 50 · 75 · 90 · 100 | INT | Firme | OPE-PR-02 |
| K148 | Identidades no humanas con dueño, rotación y privilegio revisado | Identidades de servicios, cargas y agentes con dueño, credencial rotada en plazo y privilegio revisado ÷ identidades no humanas × 100. | % | Trimestral | Mayor | 30 · 55 · 80 · 95 | SLO | Firme | OPE-PR-03 |
| K149 | Accesos desde dispositivos gestionados y conformes | Accesos a recursos corporativos desde dispositivos gestionados y conformes ÷ accesos a recursos corporativos × 100. | % | Mensual | Mayor | 50 · 75 · 90 · 98 | SLO | Firme | OPE-PR-04 |
| K150 | Dispositivos con protección y respuesta activas | Dispositivos con agente de protección activo y telemetría reciente ÷ dispositivos del inventario × 100. | % | Mensual | Mayor | 60 · 80 · 95 · 99 | SLO | Firme | OPE-PR-04 |
| K151 | Tiempo de aplicación de parches críticos en dispositivos | Mediana de días entre la publicación de un parche crítico y su instalación en el 95% de los dispositivos. | días | Mensual | Menor | 45 · 21 · 10 · 5 | SLO | Firme | OPE-PR-04 |
| K152 | Tiempo de retiro de mensajes maliciosos entregados | Mediana de minutos entre la entrega de un mensaje malicioso y su retiro de todos los buzones. | minutos | Mensual | Menor | 480 · 120 · 30 · 10 | SLO | Firme | OPE-PR-05 |
| K153 | Dominios de correo con autenticación de remitente en modo de rechazo | Dominios de correo de la organización con política de autenticación de remitente en modo de rechazo ÷ dominios de correo × 100. | % | Trimestral | Mayor | 40 · 70 · 90 · 100 | SLO | Firme | OPE-PR-05 |
| K154 | Eventos de salida de datos sensibles resueltos en plazo | Eventos de salida de datos sensibles bloqueados, justificados o escalados dentro del plazo ÷ eventos de salida detectados × 100. | % | Mensual | Mayor | 50 · 70 · 85 · 95 | SLO | Firme | OPE-PR-06 |
| K155 | Datos sensibles sobreexpuestos corregidos | Elementos con datos sensibles accesibles a toda la organización o a externos que fueron corregidos ÷ elementos sobreexpuestos detectados × 100. | % | Trimestral | Mayor | 30 · 55 · 80 · 95 | COM | Firme | OPE-PR-06 |
| K156 | Claves y secretos en bóveda con rotación | Claves y secretos gestionados en una bóveda y rotados dentro del plazo ÷ claves y secretos inventariados × 100. | % | Trimestral | Mayor | 40 · 65 · 85 · 98 | SLO | Firme | OPE-PR-06 |
| K157 | Vulnerabilidades críticas en producción fuera de plazo | Cantidad de vulnerabilidades críticas en aplicaciones en producción abiertas más allá del plazo de corrección. | n.º | Mensual | Menor | 20 · 10 · 3 · 0 | SLO | Firme | OPE-PR-07 |
| K158 | Secretos expuestos en repositorios revocados en plazo | Secretos detectados en repositorios de código y revocados dentro del plazo ÷ secretos detectados × 100. | % | Mensual | Mayor | 50 · 75 · 90 · 100 | SLO | Firme | OPE-PR-07 |
| K159 | Acceso remoto por aplicación | Usuarios remotos que acceden por aplicación, sin acceso general a la red ÷ usuarios remotos × 100. | % | Trimestral | Mayor | 25 · 50 · 80 · 95 | SLO | Firme | OPE-PR-08 |
| K160 | Reglas de red revisadas y depuradas | Reglas de red revisadas en los últimos 12 meses, con las que no se usan o son demasiado amplias eliminadas ÷ reglas de red × 100. | % | Semestral | Mayor | 30 · 55 · 80 · 95 | SLO | Firme | OPE-PR-08 |
| K161 | Cargas con protección en tiempo de ejecución | Cargas en producción con protección activa en tiempo de ejecución ÷ cargas en producción × 100, en el entorno menos cubierto. | % | Mensual | Mayor | 40 · 65 · 85 · 95 | SLO | Firme | OPE-PR-09 |
| K162 | Despliegues analizados antes de llegar a producción | Imágenes y plantillas de infraestructura analizadas y aprobadas antes del despliegue ÷ despliegues × 100. | % | Mensual | Mayor | 30 · 60 · 85 · 98 | SLO | Firme | OPE-PR-09 |
| K163 | Tasa de falla en simulaciones de ingeniería social | Personas que ejecutan la acción insegura en las simulaciones ÷ personas alcanzadas por las simulaciones × 100. | % | Trimestral | Menor | 25 · 15 · 8 · 4 | SLO | Firme | OPE-PR-10 |
| K164 | Áreas con referente de seguridad activo | Áreas del negocio con un referente de seguridad designado y con actividad en el trimestre ÷ áreas del negocio × 100. | % | Semestral | Mayor | 25 · 50 · 75 · 90 | INT | Firme | OPE-PR-10 |
| K165 | Agentes con identidad propia y permisos por herramienta revisados | Agentes en producción con identidad propia y permisos por herramienta revisados en el trimestre ÷ agentes en producción × 100. | % | Trimestral | Mayor | 40 · 65 · 85 · 98 | SLO | Provisoria | OPE-PR-11 |
| K166 | Agentes con evaluación adversarial vigente | Agentes en producción con evaluación de calidad y prueba adversarial de los últimos 6 meses ÷ agentes en producción × 100. | % | Trimestral | Mayor | 30 · 55 · 80 · 95 | COM | Provisoria | OPE-PR-11 |
| K167 | Agentes con detención de emergencia probada | Agentes con autonomía de ejecución cuya detención se probó en el trimestre ÷ agentes con autonomía de ejecución × 100. | % | Trimestral | Mayor | 40 · 70 · 90 · 100 | COM | Provisoria | OPE-PR-11 |
| K192 | Usuarios sin privilegios de administrador local | Usuarios que trabajan sin privilegios de administrador local ÷ usuarios × 100. | % | Trimestral | Mayor | 60 · 80 · 95 · 99 | SLO | Firme | OPE-PR-04 |
| K193 | Tráfico entre segmentos críticos cifrado e inspeccionado | Flujos entre segmentos críticos cifrados e inspeccionados ÷ flujos entre segmentos críticos × 100. | % | Semestral | Mayor | 30 · 55 · 80 · 95 | SLO | Firme | OPE-PR-08 |
| K195 | Identidades no humanas sin uso retiradas | Identidades no humanas sin actividad en el plazo definido que fueron retiradas ÷ identidades no humanas sin actividad detectadas × 100. | % | Trimestral | Mayor | 40 · 60 · 80 · 95 | SLO | Firme | OPE-PR-03 |
| K196 | Accesos remotos de terceros a tecnología operacional aprobados y registrados | Sesiones remotas de fabricantes e integradores con aprobación previa y registro ÷ sesiones remotas de terceros × 100. | % | Trimestral | Mayor | 50 · 75 · 90 · 100 | SLO | Firme | OPE-PR-12 |

### Operación · Detectar (14)

| ID | Indicador | Fórmula | Unidad | Frecuencia | Mejor si es | Umbrales E2 · E3 · E4 · E5 | Si se externaliza | Base | Función |
|---|---|---|---|---|---|---|---|---|---|
| K41 | Cobertura de telemetría y protección de activos críticos | Activos críticos con la telemetría requerida y sensor activo ÷ activos críticos del inventario × 100. | % | Mensual | Mayor | 60 · 75 · 90 · 98 | SLO | Firme | OPE-DE-05 |
| K42 | Tiempo medio de detección (MTTD) | Mediana de horas (primer indicio → detección confirmada) en los incidentes confirmados del período. | horas | Mensual | Menor | 72 · 24 · 8 · 1 | SLO | Firme | OPE-DE-01 |
| K43 | Técnicas de ataque priorizadas con detección validada | Técnicas priorizadas con detección validada en 12 meses ÷ técnicas priorizadas × 100. | % | Semestral | Mayor | 30 · 50 · 70 · 85 | SLO | Firme | OPE-DE-02 |
| K44 | Campañas de hunting que mejoran la detección | Campañas con detección nueva o mejorada o con brecha corregida ÷ campañas de hunting realizadas × 100. | % | Trimestral | Mayor | 20 · 35 · 50 · 70 | SLO | Firme | OPE-DE-03 |
| K53 | Observabilidad de agentes integrada a la detección | Agentes en producción con registro completo y detecciones activas ÷ agentes en producción × 100. | % | Mensual | Mayor | 20 · 40 · 70 · 90 | SLO | Provisoria | OPE-DE-06 |
| K127 | Acciones derivadas de inteligencia de amenazas | Cantidad mensual de cambios en la detección, la protección o la configuración originados en inteligencia de amenazas. | n.º | Mensual | Mayor | 1 · 4 · 8 · 12 | SLO | Firme | OPE-DE-04 |
| K168 | Alertas de severidad alta clasificadas dentro del objetivo | Alertas de severidad alta clasificadas dentro del tiempo objetivo ÷ alertas de severidad alta × 100. | % | Mensual | Mayor | 60 · 80 · 95 · 99 | SLO | Firme | OPE-DE-01 |
| K169 | Consistencia de clasificación entre analistas | Casos de una muestra clasificados igual por dos analistas independientes ÷ casos de la muestra × 100. | % | Trimestral | Mayor | 60 · 75 · 85 · 95 | SLO | Firme | OPE-DE-01 |
| K170 | Falsos positivos de las detecciones prioritarias | Alertas cerradas como falso positivo ÷ alertas generadas por las detecciones prioritarias × 100. | % | Mensual | Menor | 60 · 40 · 20 · 10 | SLO | Firme | OPE-DE-02 |
| K171 | Detecciones sin revisión en los últimos 12 meses | Detecciones activas sin revisión ni prueba en 12 meses ÷ detecciones activas × 100. | % | Semestral | Menor | 50 · 30 · 15 · 5 | SLO | Firme | OPE-DE-02 |
| K172 | Exclusiones de detección sin vencimiento | Exclusiones y listas de permitidos sin fecha de vencimiento o con la fecha superada ÷ exclusiones vigentes × 100. | % | Mensual | Menor | 40 · 20 · 10 · 0 | SLO | Firme | OPE-DE-02 |
| K173 | Fuentes críticas con registro íntegro y retención conforme | Fuentes críticas con ingesta continua, integridad verificada y retención conforme ÷ fuentes críticas × 100. | % | Mensual | Mayor | 50 · 75 · 90 · 98 | SLO | Firme | OPE-DE-05 |
| K174 | Registros ingeridos sin uso en detección ni investigación | Volumen de registros de fuentes sin uso en detecciones ni en investigaciones durante 6 meses ÷ volumen total ingerido × 100. | % | Semestral | Menor | 40 · 25 · 15 · 5 | SLO | Firme | OPE-DE-05 |
| K175 | Acciones de agentes revertidas | Acciones ejecutadas por agentes que debieron revertirse ÷ acciones ejecutadas por agentes × 100. | % | Mensual | Menor | 10 · 5 · 2 · 1 | SLO | Provisoria | OPE-DE-06 |

### Operación · Responder (11)

| ID | Indicador | Fórmula | Unidad | Frecuencia | Mejor si es | Umbrales E2 · E3 · E4 · E5 | Si se externaliza | Base | Función |
|---|---|---|---|---|---|---|---|---|---|
| K05 | Tiempo hasta la decisión ejecutiva en crisis | Mediana de minutos (escalada → primera decisión ejecutiva) en incidentes severos y ejercicios del período. | minutos | Por evento · trimestral | Menor | 240 · 120 · 60 · 30 | INT | Firme | OPE-RS-05 |
| K15 | Ejercicios de crisis con participación ejecutiva | Ejercicios realizados con participación ejecutiva ÷ ejercicios planificados en el programa anual × 100. | % | Semestral | Mayor | 25 · 50 · 75 · 100 | INS | Firme | OPE-RS-05 |
| K45 | Tiempo medio de contención (MTTC) | Mediana de horas (detección confirmada → contención) en los incidentes del período. | horas | Mensual | Menor | 48 · 12 · 4 · 1 | SLO | Firme | OPE-RS-03 |
| K55 | Incidentes contenidos con respuesta automatizada o asistida por IA | Incidentes elegibles contenidos de forma automatizada o por agentes, sin reversión por error ÷ incidentes elegibles × 100. | % | Mensual | Mayor | 20 · 40 · 60 · 80 | SLO | Provisoria | OPE-RS-03 |
| K61 | Notificaciones obligatorias emitidas en plazo | Notificaciones (reales y simuladas) emitidas en plazo ÷ notificaciones requeridas en el período × 100. Toda notificación real tardía se informa además como evento de incumplimiento. | % | Por evento · trimestral | Mayor | 60 · 80 · 95 · 100 | INS | Firme | OPE-RS-04 |
| K176 | Incidentes gestionados con guía y registro completo | Incidentes cerrados con guía aplicada, cronología y decisiones registradas ÷ incidentes cerrados × 100. | % | Trimestral | Mayor | 50 · 70 · 90 · 98 | SLO | Firme | OPE-RS-01 |
| K177 | Tiempo medio de resolución (MTTR) | Mediana de horas entre la detección confirmada y el cierre del incidente, para los incidentes de severidad alta. | horas | Mensual | Menor | 168 · 72 · 24 · 8 | SLO | Firme | OPE-RS-01 |
| K178 | Incidentes significativos con causa raíz determinada | Incidentes significativos con causa raíz documentada ÷ incidentes significativos × 100. | % | Trimestral | Mayor | 50 · 70 · 90 · 100 | SLO | Firme | OPE-RS-02 |
| K179 | Automatizaciones de respuesta fallidas | Ejecuciones de automatización de respuesta que fallaron o debieron revertirse ÷ ejecuciones de automatización × 100. | % | Mensual | Menor | 15 · 8 · 3 · 1 | SLO | Firme | OPE-RS-03 |
| K190 | Evidencia de incidentes preservada con cadena de custodia | Incidentes significativos cuya evidencia se preservó con la cadena de custodia íntegra ÷ incidentes significativos × 100. | % | Trimestral | Mayor | 50 · 70 · 90 · 100 | SLO | Firme | OPE-RS-02 |
| K191 | Clientes y socios afectados informados en el plazo comprometido | Incidentes con afectación a clientes o socios en los que se informó dentro del plazo comprometido ÷ incidentes con afectación a clientes o socios × 100. | % | Trimestral | Mayor | 50 · 70 · 90 · 100 | INT | Firme | OPE-RS-04 |

### Operación · Recuperar (10)

| ID | Indicador | Fórmula | Unidad | Frecuencia | Mejor si es | Umbrales E2 · E3 · E4 · E5 | Si se externaliza | Base | Función |
|---|---|---|---|---|---|---|---|---|---|
| K16 | Roles críticos con suplente entrenado | Roles críticos con suplente entrenado y accesos habilitados ÷ roles críticos identificados × 100. | % | Semestral | Mayor | 40 · 60 · 80 · 95 | INT | Firme | OPE-RC-04 |
| K28 | Respaldos inmutables de sistemas críticos con restauración probada | Sistemas críticos con respaldo inmutable o aislado y restauración exitosa en seis meses ÷ sistemas críticos × 100. | % | Trimestral | Mayor | 50 · 70 · 85 · 95 | SLO | Firme | OPE-RC-01 |
| K29 | Operación degradada probada en procesos críticos | Procesos críticos con modo degradado probado en 12 meses ÷ procesos críticos × 100. | % | Semestral | Mayor | 25 · 50 · 75 · 90 | COM | Firme | OPE-RC-04 |
| K30 | Pruebas de recuperación que cumplen RTO y RPO | Pruebas que cumplieron RTO y RPO con validación de integridad ÷ pruebas de recuperación realizadas × 100. | % | Semestral | Mayor | 40 · 60 · 80 · 95 | COM | Firme | OPE-RC-02 |
| K47 | Tiempo de restauración de servicios críticos frente al RTO | Mediana de (horas de restauración real ÷ RTO aprobado) × 100 en los incidentes del período que afectaron servicios críticos. | % del RTO | Por evento · trimestral | Menor | 200 · 150 · 100 · 75 | COM | Firme | OPE-RC-02 |
| K56 | Procesos críticos con IA capaces de operar sin ella | Procesos críticos dependientes de IA con desactivación y operación sin IA probadas ÷ procesos críticos dependientes de IA × 100. | % | Semestral | Mayor | 25 · 50 · 75 · 95 | COM | Provisoria | OPE-RC-04 |
| K180 | Restauraciones de prueba exitosas | Restauraciones de prueba completadas dentro del tiempo objetivo ÷ restauraciones de prueba realizadas × 100. | % | Trimestral | Mayor | 50 · 75 · 90 · 98 | SLO | Firme | OPE-RC-01 |
| K181 | Componentes de la plataforma de control con recuperación probada | Componentes de la plataforma de control (identidad, gestión, respaldo y vigilancia) con recuperación probada en un entorno aislado en los últimos 12 meses ÷ componentes × 100. | % | Semestral | Mayor | 25 · 50 · 75 · 100 | COM | Firme | OPE-RC-03 |
| K182 | Lecciones aprendidas incorporadas | Lecciones de incidentes y ejercicios que produjeron un cambio verificable en las políticas, la arquitectura o las detecciones ÷ lecciones registradas × 100. | % | Semestral | Mayor | 30 · 55 · 80 · 95 | COM | Firme | OPE-RC-05 |
| K189 | Partes interesadas informadas del avance de la recuperación en plazo | Comunicaciones de avance de la recuperación emitidas a las partes interesadas dentro del plazo definido ÷ comunicaciones comprometidas × 100. | % | Trimestral | Mayor | 50 · 70 · 90 · 100 | COM | Firme | OPE-RC-05 |

### Externalización (22)

| ID | Indicador | Fórmula | Unidad | Frecuencia | Mejor si es | Umbrales E2 · E3 · E4 · E5 | Si se externaliza | Base | Función |
|---|---|---|---|---|---|---|---|---|---|
| KX01 | Servicios externalizados con dueño interno designado | Servicios externalizados con un dueño interno nominado y con autoridad sobre el contrato ÷ servicios externalizados × 100. | % | Trimestral | Mayor | 60 · 80 · 95 · 100 | EXT | Firme | — |
| KX02 | Servicios críticos con niveles de servicio medibles por resultado | Servicios críticos con niveles de servicio definidos como resultados medibles ÷ servicios críticos externalizados × 100. | % | Semestral | Mayor | 40 · 65 · 85 · 100 | EXT | Firme | — |
| KX03 | Cumplimiento de los niveles de servicio | Mediciones de nivel de servicio dentro del objetivo ÷ mediciones del período × 100. | % | Mensual | Mayor | 70 · 85 · 95 · 99 | EXT | Firme | — |
| KX04 | Evidencia del proveedor entregada en plazo y verificable | Entregas de evidencia en plazo y que permiten verificar ÷ entregas comprometidas × 100. | % | Mensual | Mayor | 60 · 80 · 95 · 100 | EXT | Firme | — |
| KX05 | Verificación independiente realizada según el plan | Verificaciones (muestreo, prueba o auditoría) realizadas ÷ verificaciones planificadas × 100. | % | Trimestral | Mayor | 40 · 65 · 85 · 100 | EXT | Firme | — |
| KX06 | Discrepancia entre lo informado y lo verificado | Mediciones verificadas que difieren de lo informado por el proveedor más allá de la tolerancia ÷ mediciones verificadas × 100. | % | Trimestral | Menor | 30 · 20 · 10 · 5 | EXT | Firme | — |
| KX07 | Incidentes del proveedor notificados en el plazo contractual | Incidentes notificados en plazo ÷ incidentes del proveedor conocidos × 100. Equivale a K62 aplicado a cada servicio. | % | Trimestral | Mayor | 60 · 80 · 95 · 100 | EXT | Firme | — |
| KX08 | Servicios críticos con plan de salida probado | Servicios críticos con plan de salida ensayado en los últimos 24 meses ÷ servicios críticos externalizados × 100. | % | Anual | Mayor | 15 · 40 · 70 · 90 | EXT | Firme | — |
| KX09 | Portabilidad comprobada de datos, configuraciones y reglas | Servicios críticos cuya exportación de datos, configuraciones y reglas se comprobó en un formato utilizable ÷ servicios críticos externalizados × 100. | % | Anual | Mayor | 25 · 50 · 75 · 95 | EXT | Firme | — |
| KX10 | Accesos del proveedor con privilegio mínimo, autenticación fuerte y registro | Cuentas del proveedor que cumplen las tres condiciones ÷ cuentas del proveedor × 100. | % | Trimestral | Mayor | 60 · 80 · 95 · 100 | EXT | Firme | — |
| KX11 | Subcontratistas identificados y aprobados | Servicios críticos cuyos subcontratistas están identificados y aprobados ÷ servicios críticos externalizados × 100. | % | Semestral | Mayor | 40 · 65 · 85 · 100 | EXT | Firme | — |
| KX12 | Tiempo de traspaso entre el proveedor y el equipo interno | Mediana de minutos entre el escalamiento del proveedor y la toma de control por el responsable interno. | minutos | Trimestral | Menor | 120 · 60 · 30 · 15 | EXT | Firme | — |
| KX13 | Decisiones reservadas ejecutadas sin aprobación | Cantidad de acciones reservadas a la organización que el proveedor ejecutó sin una aprobación registrada. | n.º | Trimestral | Menor | 5 · 2 · 1 · 0 | EXT | Firme | — |
| KX14 | Funciones críticas concentradas en un mismo proveedor | Mayor cantidad de funciones críticas que dependen de un solo proveedor ÷ funciones críticas × 100. | % | Semestral | Menor | 60 · 45 · 30 · 20 | EXT | Firme | — |
| KX15 | Funciones externalizadas con capacidad interna de supervisión | Funciones externalizadas para las que hay al menos una persona interna capacitada para supervisarlas ÷ funciones externalizadas × 100. | % | Semestral | Mayor | 50 · 75 · 90 · 100 | EXT | Firme | — |
| KX16 | Desvío del costo por unidad de resultado | Valor absoluto de (costo real por unidad de resultado − costo de referencia) ÷ costo de referencia × 100. | % | Semestral | Menor | 40 · 25 · 15 · 5 | EXT | Firme | — |
| KX17 | Servicios con uso de IA y agentes declarado y gobernado | Servicios cuyo proveedor declaró el uso de IA, los datos empleados y la supervisión humana ÷ servicios externalizados × 100. | % | Semestral | Mayor | 30 · 60 · 85 · 100 | EXT | Firme | — |
| KX18 | Hallazgos de la revisión del servicio corregidos en plazo | Hallazgos corregidos en fecha ÷ hallazgos con fecha vencida × 100. | % | Trimestral | Mayor | 50 · 70 · 85 · 95 | EXT | Firme | — |
| KX19 | Cobertura de entornos del servicio | Entornos del alcance cubiertos por el contrato ÷ entornos del alcance × 100, en el servicio crítico menos cubierto. | % | Semestral | Mayor | 60 · 80 · 95 · 100 | EXT | Firme | — |
| KX20 | Revisiones periódicas del servicio con decisiones registradas | Revisiones realizadas con acta y decisiones ÷ revisiones programadas × 100. | % | Trimestral | Mayor | 50 · 75 · 90 · 100 | EXT | Firme | — |
| KX21 | Cláusulas mínimas presentes en los contratos críticos | Cláusulas mínimas presentes ÷ (cláusulas mínimas × contratos críticos) × 100. | % | Semestral | Mayor | 50 · 70 · 90 · 100 | EXT | Firme | — |
| KX22 | Datos y registros en poder del proveedor con localización y devolución acordadas | Servicios con la localización, la retención y la devolución de datos y registros acordadas ÷ servicios que tratan datos o registros × 100. | % | Semestral | Mayor | 50 · 70 · 90 · 100 | EXT | Firme | — |

---

*Frontier CISO Atlas · Modelo Operativo CISO 365 · versión 2.0, revisión 2 · 15 de noviembre de 2026 · propuesta sujeta a validación · @SCavanna*

# AI CISO Atlas · KPIs y OKRs del CISO de empresa de frontera

**Guía de uso y referencia · v1.0 · 9 de noviembre de 2026**  
Acompaña al libro de Excel *AI_CISO_Atlas_KPIs_OKRs_CISO_de_Frontera_v1.0_2026-11-09.xlsx* y al catálogo en JSON *AI_CISO_Atlas_KPIs_OKRs_Catalogo_v1.0.json*.

> **Estado:** baseline editorial reutilizable. Los umbrales de los estadios son referencias para calibrar con datos propios, no benchmarks oficiales. Las correspondencias con marcos son editoriales, no equivalencias. El marco regulatorio se verificó con fuentes oficiales al 9-11-2026.

## Índice
1. Para qué sirve
2. Cómo está construido
3. Estrategia por territorio
4. Estrategia por función y subfunción
5. Los 64 KPIs
6. Estadios de madurez y de cumplimiento
7. Arreglos por sector
8. OKR
9. Cómo reutilizar el artefacto
10. Marco regulatorio por sector
11. Limitaciones y silencios
12. Fuentes

## 1. Para qué sirve

En la práctica, un CISO tiene que **gobernar** —definir propósito, apetito, prioridades, autoridad y supervisión— y **gestionar** —diseñar, implementar, operar, verificar, responder y mejorar—. Tiene que mostrar indicadores que prueben dos cosas a la vez: que hace bien su trabajo y que el riesgo efectivamente baja. Este artefacto ofrece un sistema de medición completo para lograrlo: estrategia por dimensión, 64 KPIs explicados, cinco estadios de madurez y de cumplimiento por KPI, arreglos por sector, OKR y un motor reutilizable para crear el arreglo de cualquier organización.

**Empresa de frontera.** El Microsoft Work Trend Index 2025 describe a la «Frontier Firm» como una organización que opera con inteligencia disponible a demanda y con equipos humano-agente, donde cada persona pasa a dirigir agentes («agent boss») y aparece una métrica nueva, la relación humano-agente. Para el CISO esto agrega un territorio completo de medición —la autoridad no humana— que este catálogo trata en T07 (ocho KPIs) y en los OKR de «Evolucionar».

**Gobernar y gestionar (TheNextCISO GM-24).** Cada KPI declara su *plano*: los de **Gobierno** informan decisiones de apetito, prioridad, autoridad y supervisión; los de **Gestión** informan la ejecución. Cada KPI se vincula, además, a la unidad de GM-24 donde se enseña.

## 2. Cómo está construido

- **64 KPIs = 8 territorios × 8 KPIs** del AI CISO Atlas 5.3 (coordenada X).
- Por función de NIST CSF 2.0 (coordenada Z): GV 21, ID 11, PR 12, DE 5, RS 7, RC 8. Govern concentra un tercio porque el CISO gobierna antes de gestionar.
- Las **32 subfunciones** editoriales del Atlas tienen al menos un KPI; las **24 unidades de GM-24** también.
- Plano: 25 de gobierno y 39 de gestión. Tipo: 22 KPI, 8 KRI y 34 KCI. Orientación: 45 adelantados y 19 rezagados.
- Tipo de medida según NIST SP 800-55v1 (2024): implementación 26, efectividad 25, eficiencia 6 e impacto 7.
- Cada KPI tiene: qué mide, por qué importa, fórmula, unidad, polaridad, fuente de datos, ejemplo de evidencia en plataforma Microsoft, frecuencia, audiencia, correspondencias (NIST CSF 2.0, CIS Controls v8.1, ISO/IEC 27001:2022 y otros) y cinco estadios con umbrales.

| Hoja del libro | Qué contiene |
|---|---|
| Inicio | Propósito, rutas de uso, leyenda y advertencias |
| Resumen | Distribución y cobertura del catálogo, con gráficos |
| Estrategia_Territorios | Estrategia por territorio |
| Estrategia_Funciones | Estrategia por función y por subfunción |
| Dominios | Qué debe demostrar el CISO en cada dominio |
| Catalogo_KPI | Los 64 KPIs |
| Estadios | E1–E5 y umbrales editables |
| Escalas | Escalas, tipologías, GM-24 y ejes de presión |
| Perfiles_Sector | Perfiles de presión, narrativa sectorial y parámetros |
| Afinidades | Impulsores, aptitud para Directorio y ajustes |
| Motor | Cálculo de puntajes y niveles |
| Arreglos_Sector | Nivel de cada KPI por sector |
| Paquetes_Sector | 10 KPIs de Directorio y 10 esenciales por sector |
| OKR_Territorios / OKR_Sectores | Objetivos y resultados clave con avance automático |
| Autoevaluacion / Tablero | Medición y tablero (caso ilustrativo precargado) |
| Marco_Regulatorio / Fuentes | Normas y fuentes verificadas |
| Control_Calidad | 19 controles automáticos |

## 3. Estrategia por territorio

### T01 · SELF & JUDGMENT
*Criterio individual, metacognición, sesgos y decisiones.*

- **Intención estratégica:** Que las decisiones de seguridad sean explícitas, calibradas y revisables, y que el CISO dedique su criterio a lo que solo él puede decidir.
- **Pregunta del Directorio:** ¿Podemos confiar en el juicio de quien nos dice cuánto riesgo tenemos?
- **Gobernar:** Define criterios de materialidad y escalamiento; exige que las decisiones registren alternativas; acepta riesgo con fecha de vencimiento.
- **Gestionar:** Mantiene el registro de decisiones y de pronósticos; mide la calibración; protege la agenda del CISO para el gobierno.
- **Riesgo que mitiga:** Sesgos (optimismo, disponibilidad, anclaje), decisiones tardías y aprendizaje que no ocurre.
- **Señal de éxito a 12 meses:** Registro de decisiones ≥ 75%, escalamiento en plazo ≥ 90% y calibración medida cada trimestre.
- **Trampa de medición:** Medir horas de capacitación como si fueran juicio; confundir rapidez con calidad de decisión.
- **Unidades GM-24:** G1.1 · G4.2 · G5.1 · G5.2 · G6.2 · M1.2 · M5.2
- **KPIs:** K01 Calibración del juicio de riesgo (puntaje de habilidad de Brier) (Gobierno); K02 Tiempo del CISO en agenda de gobierno y negocio (Gobierno); K03 Decisiones materiales con registro y revisión posterior (Gobierno); K04 Aceptaciones de riesgo con alternativas, pre-mortem y vencimiento (Gobierno); K05 Tiempo hasta la decisión ejecutiva en crisis (Gobierno); K06 Revisiones post-incidente que evalúan decisiones (Gestión); K07 Competencias de liderazgo y juicio demostradas (Gestión); K08 Escalamiento oportuno de riesgos materiales (Gobierno).

### T02 · LEADERSHIP & ORGANIZATION
*Personas, incentivos, roles, cultura, liderazgo y accountability.*

- **Intención estratégica:** Distribuir la responsabilidad del riesgo en el negocio y sostener un equipo capaz, estable y preparado para la crisis.
- **Pregunta del Directorio:** ¿Quién responde por el riesgo cibernético en cada parte del negocio y tenemos la gente para gestionarlo?
- **Gobernar:** Asigna dueños de riesgo, incorpora objetivos de seguridad en los incentivos ejecutivos y ejerce supervisión activa desde el Directorio.
- **Gestionar:** Desarrolla capacidades, retiene talento, organiza suplencias y ejercita la crisis con el nivel ejecutivo.
- **Riesgo que mitiga:** Rendición de cuentas difusa, dependencia de personas clave, cultura de cumplimiento formal y fatiga del equipo.
- **Señal de éxito a 12 meses:** ≥ 80% de procesos críticos con dueño, objetivos de seguridad en ≥ 60% de los ejecutivos y ejercicios ejecutivos según el programa anual.
- **Trampa de medición:** Contar personas capacitadas en lugar de comportamientos (reporte, escalamiento); celebrar una baja tasa de clics sin medir los reportes.
- **Unidades GM-24:** G4.1 · G6.1 · G6.2 · M1.2 · M5.1 · M6.1
- **KPIs:** K09 Procesos y activos críticos con dueño de riesgo designado (Gobierno); K10 Ejecutivos con objetivos de ciberseguridad en su evaluación (Gobierno); K11 Comportamiento seguro: tasa de reporte de phishing (Gestión); K12 Cobertura de capacidades críticas del equipo de seguridad (Gestión); K13 Retención del talento crítico de seguridad (Gestión); K14 Supervisión activa del Directorio sobre el ciberriesgo (Gobierno); K15 Ejercicios de crisis con participación ejecutiva (Gobierno); K16 Roles críticos con suplente entrenado (Gestión).

### T03 · STRATEGY & BUSINESS
*Outcomes, estrategia, inversión y priorización empresarial.*

- **Intención estratégica:** Que cada peso invertido en seguridad se explique por riesgo reducido u objetivo de negocio habilitado, y que la seguridad acelere iniciativas en lugar de frenarlas.
- **Pregunta del Directorio:** ¿Qué obtenemos por lo que invertimos en seguridad y cuánto nos costaron los incidentes?
- **Gobernar:** Aprueba el perfil objetivo, prioriza el portafolio por riesgo y fija la tolerancia anual de pérdidas.
- **Gestionar:** Ejecuta el roadmap, cuantifica el retorno en reducción de riesgo, habilita iniciativas con rapidez y cumple los compromisos con clientes.
- **Riesgo que mitiga:** Inversión inercial, seguridad percibida como freno y pérdida de negocios por falta de evidencia de confianza.
- **Señal de éxito a 12 meses:** ≥ 80% del presupuesto trazado a riesgos, brecha del perfil objetivo en cierre y habilitación de iniciativas en 5 días o menos.
- **Trampa de medición:** Tratar el presupuesto ejecutado como éxito; usar benchmarks de gasto como sustituto de la exposición propia.
- **Unidades GM-24:** G1.2 · G2.1 · G3.1 · G6.2 · M1.1 · M3.1 · M5.1
- **KPIs:** K17 Inversión en seguridad trazada a riesgos y objetivos del negocio (Gobierno); K18 Avance del roadmap estratégico de seguridad (Gestión); K19 Reducción de riesgo por unidad de inversión (Gobierno); K20 Tiempo de habilitación segura de iniciativas (Gestión); K21 Procesos críticos con BIA vigente y dependencias mapeadas (Gestión); K22 Resultados del perfil objetivo alcanzados (NIST CSF 2.0) (Gobierno); K23 Requisitos de seguridad de clientes y contratos cumplidos en plazo (Gobierno); K24 Pérdidas por incidentes frente a la tolerancia anual (Gobierno).

### T04 · RISK & RESILIENCE
*Exposición, escenarios, apetito, continuidad y riesgo de transición.*

- **Intención estratégica:** Mantener la exposición dentro del apetito y demostrar con pruebas que la organización resiste, opera degradada y se recupera.
- **Pregunta del Directorio:** ¿Estamos dentro del riesgo que aceptamos y cuánto tardaríamos en volver a operar?
- **Gobernar:** Fija apetito y tolerancias, decide sobre la concentración en terceros y exige pruebas de recuperación.
- **Gestionar:** Cuantifica escenarios, mantiene respaldos inmutables, prueba RTO y RPO, ensaya la operación degradada y gestiona a los proveedores críticos.
- **Riesgo que mitiga:** Ransomware, caída de un proveedor crítico, sabotaje con consecuencia física y riesgo de transición (IA, nube).
- **Señal de éxito a 12 meses:** Riesgos fuera de apetito ≤ 5%, ≥ 80% de las pruebas de recuperación dentro del RTO y respaldos inmutables en ≥ 85% de los sistemas críticos.
- **Trampa de medición:** Pruebas de recuperación «de escritorio»; matrices de calor sin cuantificación ni tolerancias.
- **Unidades GM-24:** G4.2 · G5.1 · M5.1 · M6.1 · M6.2
- **KPIs:** K25 Riesgos residuales fuera del apetito (Gobierno); K26 Pérdida esperada de los escenarios prioritarios frente al apetito (Gobierno); K27 Servicios críticos concentrados en un proveedor sin alternativa (Gobierno); K28 Respaldos inmutables de sistemas críticos con restauración probada (Gestión); K29 Operación degradada probada en procesos críticos (Gestión); K30 Pruebas de recuperación que cumplen RTO y RPO (Gestión); K31 Proveedores críticos evaluados y con cláusulas de seguridad (Gestión); K32 Escenarios críticos con playbook probado (Gestión).

### T05 · SECURITY ARCHITECTURE
*Diseño de controles, Zero Trust, ingeniería y fronteras técnicas.*

- **Intención estratégica:** Diseñar controles que eliminen clases enteras de ataque —identidad, configuración, segmentación, datos, software, OT— y que se mantengan por defecto.
- **Pregunta del Directorio:** ¿Nuestra arquitectura impide los ataques más probables o solo los detecta tarde?
- **Gobernar:** Aprueba estándares y patrones de referencia (Zero Trust, ISA/IEC 62443) y decide sobre las excepciones de diseño.
- **Gestionar:** Implementa autenticación resistente al phishing, privilegios justo a tiempo, líneas base, segmentación, protección de datos, pipeline seguro e inventario.
- **Riesgo que mitiga:** Robo de credenciales, movimiento lateral, configuraciones débiles, fuga de datos, compromiso de la cadena de software y sabotaje OT.
- **Señal de éxito a 12 meses:** ≥ 80% de autenticación resistente al phishing, ≥ 75% de privilegios justo a tiempo y zonas OT críticas en su nivel de seguridad objetivo.
- **Trampa de medición:** Medir herramientas compradas en lugar de cobertura efectiva; promedios que ocultan los activos críticos.
- **Unidades GM-24:** M2.1 · M2.2 · M3.1 · M3.2
- **KPIs:** K33 Autenticación resistente al phishing (Gestión); K34 Accesos privilegiados sin privilegios permanentes (JIT) (Gestión); K35 Activos conformes a la línea base de configuración segura (Gestión); K36 Segmentación de activos críticos verificada (Gestión); K37 Datos sensibles clasificados y protegidos (Gestión); K38 Aplicaciones críticas con controles automatizados en el pipeline (Gestión); K39 Cobertura del inventario de activos (TI, nube, OT e IoT) (Gestión); K40 Zonas OT e IIoT que alcanzan su nivel de seguridad objetivo (Gestión).

### T06 · SECURITY OPERATIONS
*SOC, monitoreo, investigación, respuesta y operación.*

- **Intención estratégica:** Ver todo lo crítico, detectar lo relevante, contener en horas y restaurar dentro del RTO, aprendiendo de cada incidente.
- **Pregunta del Directorio:** Si nos atacan hoy, ¿lo veríamos, lo frenaríamos y en cuánto tiempo volveríamos a la normalidad?
- **Gobernar:** Define niveles de servicio de detección y respuesta y la priorización por exposición.
- **Gestionar:** Opera la telemetría, la detección validada contra las amenazas del sector, el hunting, la contención, la remediación de vulnerabilidades explotadas y las acciones correctivas.
- **Riesgo que mitiga:** Permanencia prolongada del atacante, explotación de vulnerabilidades conocidas e incidentes recurrentes.
- **Señal de éxito a 12 meses:** MTTD ≤ 8 h, MTTC ≤ 4 h, ≥ 85% de vulnerabilidades explotadas remediadas en plazo y ≥ 70% de técnicas priorizadas validadas.
- **Trampa de medición:** Reportar volumen de alertas o de ataques bloqueados; promedios que esconden los incidentes graves.
- **Unidades GM-24:** M4.1 · M4.2 · M5.2 · M6.1
- **KPIs:** K41 Cobertura de telemetría y protección de activos críticos (Gestión); K42 Tiempo medio de detección (MTTD) (Gestión); K43 Técnicas de ataque priorizadas con detección validada (Gestión); K44 Campañas de hunting que mejoran la detección (Gestión); K45 Tiempo medio de contención (MTTC) (Gestión); K46 Vulnerabilidades explotadas y exposiciones críticas remediadas en plazo (Gestión); K47 Tiempo de restauración de servicios críticos frente al RTO (Gestión); K48 Acciones correctivas post-incidente cerradas en plazo (Gestión).

### T07 · AI & AUTONOMOUS SYSTEMS
*Modelos, agentes, autonomía, herramientas y autoridad no humana.*

- **Intención estratégica:** Gobernar la autoridad no humana: conocer cada modelo y agente, acotar lo que puede hacer, observarlo, probarlo y poder apagarlo sin detener el negocio; y usar la IA para defender.
- **Pregunta del Directorio:** ¿Cuántos agentes actúan en nuestro nombre, quién responde por ellos y qué pasa si fallan?
- **Gobernar:** Aprueba la política de IA, los casos de uso de alto riesgo y los límites de la autoridad delegada a los agentes.
- **Gestionar:** Mantiene el inventario, las identidades y permisos de los agentes, la DLP para IA, la observabilidad, el red teaming, la respuesta asistida y la operación sin IA.
- **Riesgo que mitiga:** IA en la sombra, inyección de prompts, abuso de herramientas, fuga de datos, decisiones autónomas no supervisadas y dependencia de un proveedor de IA.
- **Señal de éxito a 12 meses:** ≥ 75% de agentes con dueño y autoridad acotada, inventario ≥ 75% y operación sin IA probada en los procesos críticos.
- **Trampa de medición:** Contar licencias de IA como adopción segura; tratar a los agentes como usuarios o como software sin identidad.
- **Unidades GM-24:** G2.2 · M2.1 · M2.2 · M4.1 · M4.2 · M5.2 · M6.1 · M6.2
- **KPIs:** K49 Inventario de sistemas de IA y agentes (Gestión); K50 Agentes con dueño humano y autoridad delegada acotada (Gobierno); K51 Casos de uso de IA con evaluación de riesgo e impacto previa (Gobierno); K52 Interacciones con IA protegidas contra la fuga de datos (Gestión); K53 Observabilidad de agentes integrada a la detección (Gestión); K54 Hallazgos críticos de red teaming de IA corregidos (Gestión); K55 Incidentes contenidos con respuesta automatizada o asistida por IA (Gestión); K56 Procesos críticos con IA capaces de operar sin ella (Gestión).

### T08 · TRUST & ASSURANCE
*Evidencia, auditoría, legitimidad, confiabilidad y transparencia.*

- **Intención estratégica:** Demostrar con evidencia —ante el Directorio, reguladores, clientes y ciudadanos— que los controles funcionan, que se cumplen las obligaciones y que se informa a tiempo.
- **Pregunta del Directorio:** ¿Podemos probar lo que decimos sobre nuestra seguridad cuando nos lo piden?
- **Gobernar:** Supervisa obligaciones, hallazgos, excepciones y la calidad del reporte; asegura las notificaciones en plazo.
- **Gestionar:** Mantiene la evidencia, prueba la efectividad de los controles, gestiona los incidentes de terceros y las evaluaciones de impacto en privacidad.
- **Riesgo que mitiga:** Sanciones, pérdida de licencias o de clientes, notificaciones tardías y cumplimiento «de papel».
- **Señal de éxito a 12 meses:** ≥ 85% de obligaciones con evidencia, ≥ 85% de hallazgos cerrados en plazo y notificaciones en plazo ensayadas.
- **Trampa de medición:** Confundir certificación con seguridad; medir políticas publicadas en lugar de controles probados.
- **Unidades GM-24:** G2.2 · G3.1 · G3.2 · G6.1 · M2.1 · M3.2 · M6.2
- **KPIs:** K57 Obligaciones aplicables mapeadas a controles con evidencia vigente (Gobierno); K58 Calidad del reporte de ciberriesgo al Directorio (Gobierno); K59 Hallazgos de auditoría y de reguladores cerrados en plazo (Gobierno); K60 Controles clave con efectividad probada (Gestión); K61 Notificaciones obligatorias emitidas en plazo (Gobierno); K62 Incidentes de terceros notificados en el plazo contractual (Gestión); K63 Excepciones a políticas vigentes, justificadas y con vencimiento (Gobierno); K64 Tratamientos de datos personales de alto riesgo con evaluación de impacto (Gestión).

## 4. Estrategia por función y subfunción

**GV · Govern (Gobernar).** Decidir y supervisar: convertir apetito, obligaciones y estrategia en mandatos verificables, con autoridad y rendición de cuentas claras. — 21 KPIs.

**ID · Identify (Identificar).** Conocer y cuantificar: activos, dependencias, exposición y brechas expresados en términos que permitan priorizar. — 11 KPIs.

**PR · Protect (Proteger).** Prevenir por diseño: eliminar clases completas de ataque con controles que se mantienen por defecto. — 12 KPIs.

**DE · Detect (Detectar).** Ver lo crítico y detectar lo relevante rápido, con detecciones validadas contra las amenazas del sector. — 5 KPIs.

**RS · Respond (Responder).** Decidir, contener y comunicar en horas, coordinando negocio, terceros y autoridades. — 7 KPIs.

**RC · Recover (Recuperar).** Volver a operar —y operar degradado mientras tanto— con evidencia, y aprender de cada incidente. — 8 KPIs.

| Subfunción | Qué debe medirse | Pregunta que responde | KPIs | NIST CSF 2.0 |
|---|---|---|---|---|
| GV01 Contexto empresarial y estrategia | Alineación de la seguridad con los objetivos, riesgos y agenda del negocio. | ¿La seguridad trabaja en lo que importa al negocio? | K02, K17 | GV.OC |
| GV02 Estructura de gobierno y autoridad | Claridad de autoridad y de responsabilidad, humana y de agentes. | ¿Quién decide y quién responde, incluso por los agentes? | K09, K50 | GV.RR |
| GV03 Políticas y estándares | Aplicación efectiva de las políticas (incluida la de IA) y control de sus excepciones. | ¿Las políticas gobiernan la práctica o solo existen? | K51, K63 | GV.PO |
| GV04 Apetito, tolerancia y aceptación de riesgo | Posición frente al apetito, pérdidas reales y calidad de las aceptaciones de riesgo. | ¿Estamos dentro del riesgo que decidimos aceptar? | K04, K24, K25 | GV.RM |
| GV05 Gobierno de programas, recursos e inversión | Ejecución del programa y sostenibilidad de sus recursos. | ¿Cumplimos lo planificado con los recursos que tenemos? | K13, K18 | GV.RR |
| GV06 Obligaciones legales y contractuales | Cobertura de obligaciones con controles y evidencia; cumplimiento de compromisos con clientes. | ¿Sabemos qué debemos cumplir y podemos probarlo? | K23, K57 | GV.OC |
| GV07 Supervisión y reporting ejecutivo | Oportunidad del escalamiento y calidad de la supervisión del Directorio. | ¿El Directorio recibe a tiempo lo que necesita para decidir? | K08, K14, K58 | GV.OV |
| GV08 Assurance y revisión independiente | Efectividad probada de los controles y cierre de hallazgos. | ¿Quién verificó que los controles funcionan? | K59, K60 | GV.OV · ID.IM |
| GV09 Gobierno de terceros y ecosistemas | Evaluación, cláusulas y monitoreo de los proveedores críticos. | ¿Controlamos el riesgo que heredamos de terceros? | K31 | GV.SC |
| GV10 Ética, cultura y rendición de cuentas | Rendición de cuentas sobre las decisiones e incentivos alineados. | ¿Las decisiones se pueden reconstruir y los incentivos empujan en la dirección correcta? | K03, K10 | GV.RR |
| ID01 Inventario y clasificación de activos | Cobertura del inventario, incluidos OT, IoT, IA y agentes. | ¿Conocemos todo lo que debemos proteger? | K39, K49 | ID.AM |
| ID02 Dependencias y criticidad del negocio | Mapa de dependencias y concentración en proveedores. | ¿Qué se detiene si falla esto o este proveedor? | K21, K27 | ID.AM · GV.OC |
| ID03 Amenazas, vulnerabilidades y exposición | Reducción de la exposición explotable, incluida la de la IA. | ¿Cerramos primero lo que los atacantes ya saben explotar? | K46, K54 | ID.RA |
| ID04 Análisis de escenarios y cuantificación de riesgos | Exposición cuantificada, retorno de la inversión y calibración del juicio. | ¿Cuánto riesgo tenemos en moneda y qué tan bien lo estimamos? | K01, K19, K26 | ID.RA |
| ID05 Evaluación de capacidades y brechas | Brecha frente al perfil objetivo y capacidades del equipo. | ¿Cuánto nos falta para llegar al estado objetivo? | K12, K22 | ID.IM |
| PR01 Identidad y autorización | Fortaleza de la autenticación y eliminación de privilegios permanentes. | ¿Puede un atacante convertirse en nosotros? | K33, K34 | PR.AA |
| PR02 Protección de datos y privacidad por diseño | Datos sensibles protegidos, IA sin fuga y privacidad por diseño. | ¿Nuestros datos están protegidos dondequiera que viajen, incluida la IA? | K37, K52, K64 | PR.DS |
| PR03 Hardening y arquitectura segura | Conformidad de configuración, segmentación y nivel de seguridad OT. | ¿La arquitectura limita el radio de explosión? | K35, K36, K40 | PR.PS · PR.IR |
| PR04 Desarrollo seguro y gestión de cambios | Seguridad integrada al desarrollo y a la habilitación de iniciativas. | ¿La seguridad llega temprano y sin frenar? | K20, K38 | PR.PS |
| PR05 Preparación de personas y procedimientos | Comportamiento seguro y competencias demostradas. | ¿Las personas actúan como defensa? | K07, K11 | PR.AT |
| DE01 Telemetría y observabilidad | Cobertura de telemetría, incluida la de los agentes. | ¿Vemos lo que pasa en lo crítico? | K41, K53 | DE.CM |
| DE02 Ingeniería de detección y análisis | Velocidad de detección. | ¿Cuánto tarda en descubrirse un ataque? | K42 | DE.AE |
| DE03 Hunting, validación y mejora de detecciones | Conversión del hunting en detecciones. | ¿Aprende el SOC más rápido que el adversario? | K44 | DE.AE · ID.IM |
| DE04 Evaluación de cobertura y calidad de detección | Cobertura validada de las técnicas de ataque priorizadas. | ¿Detectamos las técnicas que usarían contra nosotros? | K43 | DE.CM · DE.AE |
| RS01 Preparación y coordinación de respuesta | Ejercicios ejecutivos y playbooks probados. | ¿Estamos ensayados para los escenarios que importan? | K15, K32 | ID.IM · RS.MA |
| RS02 Contención, erradicación y preservación de evidencia | Velocidad y automatización de la contención. | ¿Cuánto daño alcanza a hacer el atacante? | K45, K55 | RS.MI |
| RS03 Comunicación de crisis y decisiones ejecutivas | Velocidad de decisión y cumplimiento de las notificaciones. | ¿Decidimos y avisamos a tiempo? | K05, K61 | RS.CO |
| RS04 Gestión de incidentes con terceros | Transparencia y oportunidad de los terceros ante incidentes. | ¿Nos enteramos a tiempo de los incidentes de nuestros proveedores? | K62 | GV.SC · RS.CO |
| RC01 Restauración y recuperación técnica | Respaldos inmutables y tiempo real de restauración. | ¿Podemos volver desde una copia limpia y en cuánto tiempo? | K28, K47 | RC.RP · PR.DS |
| RC02 Continuidad y operación degradada | Operación sin TI, sin IA y sin personas clave. | ¿Seguimos operando mientras recuperamos? | K16, K29, K56 | RC.RP |
| RC03 Validación de recuperación y retorno seguro | Cumplimiento de RTO y RPO con integridad verificada. | ¿Lo que restauramos está limpio y llega a tiempo? | K30 | RC.RP |
| RC04 Aprendizaje, corrección y mejora continua | Cierre de acciones correctivas y aprendizaje de las decisiones. | ¿Cada incidente nos deja mejor preparados? | K06, K48 | ID.IM |

**Dominios (coordenada Y).** Todos los dominios quedan cubiertos como primarios o secundarios. Sin KPI primario: D09 (Endpoint & Workplace Security), D19 (IoT & Cyber-Physical Systems Security), D22 (AI for Security Assessment & Testing), D23 (AI for Security Engineering & Automation). Son candidatos a ampliar el catálogo.

## 5. Los 64 KPIs

Formato de cada ficha: coordenadas (territorio · subfunción · dominio · plano · unidad GM-24 · tipo · tipo de medida · orientación), qué mide, por qué importa, fórmula, unidad y polaridad, datos y evidencia, estadios y umbrales, y correspondencias.

### T01 · SELF & JUDGMENT

#### K01 · Calibración del juicio de riesgo (puntaje de habilidad de Brier)
- **Coordenadas:** T01 · ID04 Análisis de escenarios y cuantificación de riesgos · D02 Cyber Risk Management (secundarios: D12) · Gobierno · GM-24 G5.1 · KPI · Efectividad · Rezagado
- **Qué mide:** Qué tan bien coinciden las probabilidades que el CISO y su equipo asignan a eventos de riesgo (p. ej., «30% de probabilidad de un ransomware material en 12 meses») con lo que efectivamente ocurre. Mide la calidad del juicio, no la cantidad de análisis.
- **Por qué importa:** El Directorio decide sobre estimaciones. Un equipo sistemáticamente optimista o alarmista distorsiona apetito, inversión y prioridades; la calibración vuelve auditable el juicio experto.
- **Fórmula:** BSS = 1 − BS ÷ BS_ref, donde BS = (1/N) Σ (pᵢ − oᵢ)² sobre los pronósticos cerrados en el período (oᵢ = 1 si el evento ocurrió) y BS_ref usa la tasa histórica como pronóstico.
- **Unidad y polaridad:** Índice · Mayor es mejor · **Frecuencia:** Trimestral · **Audiencia:** Comité de riesgos · CISO
- **Fuente de datos:** Registro de pronósticos (fecha, horizonte, probabilidad, resultado) en el GRC o en una lista controlada. **Evidencia (ejemplo Microsoft):** Registro en Microsoft Lists o Dataverse con cierre automatizado y reporte en Power BI.
- **Estadios:** E1 Sin estimaciones probabilísticas o BSS < 0 (peor que usar la tasa histórica); el riesgo se expresa como alto, medio o bajo. | E2 BSS 0 a 0,09: pronósticos registrados de manera esporádica y poco discriminantes. | E3 BSS 0,10 a 0,19: registro trimestral de pronósticos y revisión de los que fallaron. | E4 BSS 0,20 a 0,29: calibración por persona y por tipo de escenario; ajustes al modelo cuantitativo. | E5 BSS ≥ 0,30: pronósticos agregados (equipo y modelos), retroalimentación continua y uso explícito en las decisiones de apetito.
- **Umbrales:** E2 ≥ 0,00 · E3 ≥ 0,10 · E4 ≥ 0,20 · E5 ≥ 0,30 (E3 = mínimo aceptable; E4 = meta por defecto)
- **Correspondencias:** NIST CSF 2.0 ID.RA · CIS v8.1 — · ISO/IEC 27001:2022 6.1.2 (evaluación de riesgos) · Otros: Open FAIR (O-RA 2.1); Brier (1950)

#### K02 · Tiempo del CISO en agenda de gobierno y negocio
- **Coordenadas:** T01 · GV01 Contexto empresarial y estrategia · D01 Cybersecurity Governance (secundarios: D04) · Gobierno · GM-24 G1.1 · KPI · Eficiencia · Adelantado
- **Qué mide:** Proporción del tiempo del CISO dedicada a gobierno (Directorio, comités, apetito, decisiones), a negocio (clientes, iniciativas, socios) y al desarrollo del equipo, frente a la operación reactiva.
- **Por qué importa:** Un CISO absorbido por la operación no gobierna: el riesgo se gestiona caso a caso y la estrategia queda sin dueño. El indicador hace visible el arquetipo real del rol.
- **Fórmula:** Horas en agenda de gobierno y negocio ÷ horas laborales del CISO en el período × 100 (muestra de calendario o registro semanal).
- **Unidad y polaridad:** % · Mayor es mejor · **Frecuencia:** Trimestral · **Audiencia:** CISO · Comité ejecutivo
- **Fuente de datos:** Calendario del CISO clasificado por categoría; registro semanal de tiempo. **Evidencia (ejemplo Microsoft):** Categorías de Outlook y análisis de tiempo con Microsoft Viva Insights; reporte en Power BI.
- **Estadios:** E1 Menos de 15%: el CISO opera como jefe de turno; la agenda la fijan los incidentes. | E2 15% a 24%: participación esporádica en comités; reportes a demanda. | E3 25% a 34%: agenda trimestral con Directorio y negocio; delegación operativa explícita. | E4 35% a 44%: agenda de gobierno planificada y protegida; un segundo nivel conduce la operación. | E5 45% o más: el CISO co-diseña la estrategia de negocio y de IA; la operación se gobierna por indicadores y agentes supervisados.
- **Umbrales:** E2 ≥ 15% · E3 ≥ 25% · E4 ≥ 35% · E5 ≥ 45% (E3 = mínimo aceptable; E4 = meta por defecto)
- **Correspondencias:** NIST CSF 2.0 GV.RR · CIS v8.1 — · ISO/IEC 27001:2022 5.1 (liderazgo y compromiso) · Otros: TheNextCISO GM-24, G1.1 (arquetipos CISO)

#### K03 · Decisiones materiales con registro y revisión posterior
- **Coordenadas:** T01 · GV10 Ética, cultura y rendición de cuentas · D01 Cybersecurity Governance (secundarios: D02) · Gobierno · GM-24 G6.2 · KCI · Implementación · Adelantado
- **Qué mide:** Porcentaje de decisiones materiales de seguridad (aceptaciones de riesgo, inversiones relevantes, decisiones de crisis, excepciones mayores) registradas con contexto, alternativas, autoridad que decide y criterio de éxito, y revisadas a los 6–12 meses.
- **Por qué importa:** La rendición de cuentas exige poder reconstruir por qué se decidió algo. Sin registro, el aprendizaje y la defensa ante auditores, reguladores o tribunales dependen de la memoria.
- **Fórmula:** Decisiones materiales registradas y con revisión posterior realizada ÷ decisiones materiales del período × 100.
- **Unidad y polaridad:** % · Mayor es mejor · **Frecuencia:** Trimestral · **Audiencia:** Comité de riesgos · CISO
- **Fuente de datos:** Registro de decisiones en el GRC; actas de comités. **Evidencia (ejemplo Microsoft):** Microsoft Lists o Dataverse con flujo de aprobación (Power Automate) y retención con Microsoft Purview.
- **Estadios:** E1 Menos de 25%: decisiones verbales o dispersas en correos; no hay criterio de materialidad. | E2 25% a 49%: registro parcial, sin alternativas ni criterio de éxito. | E3 50% a 74%: criterio de materialidad aprobado; registro estándar con autoridad y alternativas. | E4 75% a 89%: revisión posterior sistemática; las lecciones se incorporan a políticas y apetito. | E5 90% o más: registro trazable de decisiones humanas y de agentes; auditoría independiente del ciclo decisión-resultado.
- **Umbrales:** E2 ≥ 25% · E3 ≥ 50% · E4 ≥ 75% · E5 ≥ 90% (E3 = mínimo aceptable; E4 = meta por defecto)
- **Correspondencias:** NIST CSF 2.0 GV.OV · CIS v8.1 — · ISO/IEC 27001:2022 7.5 (información documentada) · Otros: ISO/IEC 27014:2020 (gobierno de la seguridad de la información)

#### K04 · Aceptaciones de riesgo con alternativas, pre-mortem y vencimiento
- **Coordenadas:** T01 · GV04 Apetito, tolerancia y aceptación de riesgo · D02 Cyber Risk Management (secundarios: D01) · Gobierno · GM-24 G5.2 · KCI · Efectividad · Adelantado
- **Qué mide:** Porcentaje de aceptaciones de riesgo por encima del umbral de materialidad que documentan al menos dos alternativas de tratamiento, un análisis pre-mortem (qué tendría que fallar), el costo de mitigar, el dueño de negocio y la fecha de vencimiento.
- **Por qué importa:** Aceptar riesgo es una decisión legítima de gobierno solo si es informada y temporal. Las aceptaciones sin alternativas ni vencimiento se convierten en exposición permanente e invisible.
- **Fórmula:** Aceptaciones vigentes que cumplen los cinco criterios ÷ aceptaciones vigentes sobre el umbral × 100.
- **Unidad y polaridad:** % · Mayor es mejor · **Frecuencia:** Trimestral · **Audiencia:** Comité de riesgos
- **Fuente de datos:** Registro de riesgos y de aceptaciones en el GRC. **Evidencia (ejemplo Microsoft):** Registro en Dataverse o Microsoft Lists con recordatorios de vencimiento automatizados (Power Automate).
- **Estadios:** E1 Menos de 25%: se acepta riesgo por omisión; no hay umbral de materialidad. | E2 25% a 49%: formulario de aceptación sin alternativas ni costo. | E3 50% a 79%: criterios mínimos y firma del dueño de negocio; vencimiento de 12 meses como máximo. | E4 80% a 94%: pre-mortem y cuantificación en las aceptaciones materiales; revisión en comité. | E5 95% o más: aceptaciones ligadas al apetito cuantificado; alertas de vencimiento y reevaluación ante cambios de contexto.
- **Umbrales:** E2 ≥ 25% · E3 ≥ 50% · E4 ≥ 80% · E5 ≥ 95% (E3 = mínimo aceptable; E4 = meta por defecto)
- **Correspondencias:** NIST CSF 2.0 GV.RM · CIS v8.1 — · ISO/IEC 27001:2022 6.1.3 (tratamiento de riesgos) · Otros: CRISC 2025 (R3); Open FAIR

#### K05 · Tiempo hasta la decisión ejecutiva en crisis
- **Coordenadas:** T01 · RS03 Comunicación de crisis y decisiones ejecutivas · D15 Incident Response & Crisis Management (secundarios: D01) · Gobierno · GM-24 M5.2 · KPI · Eficiencia · Rezagado
- **Qué mide:** Minutos entre la escalada formal de un incidente severo (real o de ejercicio) y la primera decisión ejecutiva registrada: aislar operaciones, activar continuidad, comunicar o notificar.
- **Por qué importa:** En una crisis, la demora en decidir suele causar más daño que una decisión imperfecta. El indicador revela si la autoridad está clara y si los decisores están preparados.
- **Fórmula:** Mediana de minutos (escalada → primera decisión ejecutiva) en incidentes severos y ejercicios del período.
- **Unidad y polaridad:** minutos · Menor es mejor · **Frecuencia:** Por evento · trimestral · **Audiencia:** Directorio · Comité de crisis
- **Fuente de datos:** Bitácora de crisis; informes de ejercicios; registro del incidente. **Evidencia (ejemplo Microsoft):** Línea de tiempo del incidente en Microsoft Defender XDR o Microsoft Sentinel y bitácora en un canal de crisis de Teams.
- **Estadios:** E1 Más de 240 min o sin registro: no está claro quién decide y se busca consenso durante la crisis. | E2 121 a 240 min: cadena de escalada definida pero no ensayada. | E3 61 a 120 min: autoridades y suplentes nominados; umbrales de decisión acordados de antemano. | E4 31 a 60 min: decisiones preautorizadas por escenario; ejercicios con el comité ejecutivo. | E5 30 min o menos: libretos de decisión con opciones precalculadas; síntesis de situación asistida por IA y validada por personas.
- **Umbrales:** E2 ≤ 240 min · E3 ≤ 120 min · E4 ≤ 60 min · E5 ≤ 30 min (E3 = mínimo aceptable; E4 = meta por defecto)
- **Correspondencias:** NIST CSF 2.0 RS.MA · CIS v8.1 17 · ISO/IEC 27001:2022 5.26 (respuesta a incidentes) · Otros: DORA art. 11; NIS2 art. 23

#### K06 · Revisiones post-incidente que evalúan decisiones
- **Coordenadas:** T01 · RC04 Aprendizaje, corrección y mejora continua · D15 Incident Response & Crisis Management (secundarios: D24) · Gestión · GM-24 M5.2 · KCI · Efectividad · Adelantado
- **Qué mide:** Porcentaje de revisiones post-incidente de incidentes mayores que analizan las decisiones (qué se sabía, cuándo y qué alternativas había), además de las fallas técnicas, y que producen cambios de criterio, umbrales o libretos.
- **Por qué importa:** Corregir solo la falla técnica deja intacto el error de juicio que la permitió. Este indicador conecta los incidentes con la mejora del criterio del equipo.
- **Fórmula:** Revisiones con análisis de decisiones y al menos un cambio de criterio aprobado ÷ incidentes mayores cerrados × 100.
- **Unidad y polaridad:** % · Mayor es mejor · **Frecuencia:** Trimestral · **Audiencia:** CISO · Comité de riesgos
- **Fuente de datos:** Informes de revisión post-incidente; registro de cambios de libretos. **Evidencia (ejemplo Microsoft):** Informe del incidente en Microsoft Sentinel o Defender XDR; revisión colaborativa en Loop o SharePoint.
- **Estadios:** E1 Menos de 25%: revisiones inexistentes o centradas en buscar culpables. | E2 25% a 49%: revisiones técnicas sin análisis de las decisiones. | E3 50% a 74%: formato sin culpa con línea de tiempo de decisiones. | E4 75% a 94%: cambios de criterio con dueño y plazo; seguimiento en comité. | E5 95% o más: patrones de decisión analizados entre incidentes y aprendizaje incorporado a simulaciones y agentes de respuesta.
- **Umbrales:** E2 ≥ 25% · E3 ≥ 50% · E4 ≥ 75% · E5 ≥ 95% (E3 = mínimo aceptable; E4 = meta por defecto)
- **Correspondencias:** NIST CSF 2.0 ID.IM · CIS v8.1 17 · ISO/IEC 27001:2022 5.27 (aprendizaje de los incidentes) · Otros: NIST SP 800-61r3

#### K07 · Competencias de liderazgo y juicio demostradas
- **Coordenadas:** T01 · PR05 Preparación de personas y procedimientos · D24 Security Workforce & Human Factors (secundarios: D01) · Gestión · GM-24 M1.2 · KPI · Implementación · Adelantado
- **Qué mide:** Porcentaje de las competencias críticas definidas para el CISO y su primera línea (gobierno, riesgo, comunicación ejecutiva, IA, crisis) demostradas con evidencia —ejercicios, dossiers, evaluaciones— y no solo con horas de curso.
- **Por qué importa:** La función evoluciona más rápido que los cargos. Medir competencia demostrada, no asistencia, evita la ilusión de preparación y alimenta el plan de sucesión.
- **Fórmula:** Competencias demostradas con evidencia ÷ competencias requeridas en el plan del período × 100.
- **Unidad y polaridad:** % · Mayor es mejor · **Frecuencia:** Semestral · **Audiencia:** CISO · Recursos humanos
- **Fuente de datos:** Planes de desarrollo individual; evaluaciones del programa TheNextCISO GM-24; registros de ejercicios. **Evidencia (ejemplo Microsoft):** Microsoft Viva Learning y credenciales de Microsoft Learn (p. ej., SC-100) como parte de la evidencia.
- **Estadios:** E1 Menos de 25%: desarrollo informal; sin mapa de competencias del rol. | E2 25% a 49%: plan anual centrado en cursos y certificaciones. | E3 50% a 74%: mapa de competencias por rol con evidencia de práctica (ejercicios, casos). | E4 75% a 89%: evaluación 360 y dossier anual; brechas vinculadas a la sucesión. | E5 90% o más: aprendizaje continuo con simulaciones de crisis y de IA; mentoría cruzada con el negocio.
- **Umbrales:** E2 ≥ 25% · E3 ≥ 50% · E4 ≥ 75% · E5 ≥ 90% (E3 = mínimo aceptable; E4 = meta por defecto)
- **Correspondencias:** NIST CSF 2.0 PR.AT · CIS v8.1 14 · ISO/IEC 27001:2022 7.2 (competencia) · Otros: TheNextCISO GM-24; CISM 2026; NIS2 art. 20.2 (formación del órgano de dirección)

#### K08 · Escalamiento oportuno de riesgos materiales
- **Coordenadas:** T01 · GV07 Supervisión y reporting ejecutivo · D02 Cyber Risk Management (secundarios: D01) · Gobierno · GM-24 G4.2 · KCI · Efectividad · Adelantado
- **Qué mide:** Porcentaje de riesgos que superaron su tolerancia (o de incidentes con impacto material potencial) que se escalaron al nivel de gobierno correspondiente dentro del plazo definido en la política.
- **Por qué importa:** Un Directorio que se entera tarde no puede supervisar. El escalamiento oportuno prueba que el apetito de riesgo funciona como mecanismo y no como documento.
- **Fórmula:** Escalamientos realizados dentro del plazo ÷ eventos que requerían escalamiento × 100.
- **Unidad y polaridad:** % · Mayor es mejor · **Frecuencia:** Trimestral · **Audiencia:** Directorio · Comité de riesgos
- **Fuente de datos:** Registro de riesgos (fechas de cruce de umbral) y actas de comités. **Evidencia (ejemplo Microsoft):** Alertas de umbral en Power BI sobre el registro de riesgos; actas en SharePoint con retención de Microsoft Purview.
- **Estadios:** E1 Menos de 50%: no hay umbrales de escalamiento; el Directorio se informa por terceros. | E2 50% a 74%: umbrales cualitativos; el escalamiento depende del criterio individual. | E3 75% a 89%: matriz de escalamiento aprobada con plazos por nivel. | E4 90% a 97%: escalamiento disparado por KRI cuantificados y verificado por auditoría interna. | E5 98% o más: alertas automáticas de cruce de tolerancia y evaluación de materialidad documentada en horas.
- **Umbrales:** E2 ≥ 50% · E3 ≥ 75% · E4 ≥ 90% · E5 ≥ 98% (E3 = mínimo aceptable; E4 = meta por defecto)
- **Correspondencias:** NIST CSF 2.0 GV.OV · CIS v8.1 — · ISO/IEC 27001:2022 9.3 (revisión por la dirección) · Otros: SEC Form 8-K Item 1.05 (materialidad); NIS2 art. 20

### T02 · LEADERSHIP & ORGANIZATION

#### K09 · Procesos y activos críticos con dueño de riesgo designado
- **Coordenadas:** T02 · GV02 Estructura de gobierno y autoridad · D01 Cybersecurity Governance (secundarios: D02) · Gobierno · GM-24 G4.1 · KCI · Implementación · Adelantado
- **Qué mide:** Porcentaje de procesos de negocio y activos críticos con un dueño de riesgo del negocio nominado, que aceptó formalmente su responsabilidad y participa en la decisión de tratamiento.
- **Por qué importa:** Si el riesgo cibernético «es del CISO», el negocio no decide ni financia su tratamiento. La rendición de cuentas distribuida es la base del gobierno.
- **Fórmula:** Procesos y activos críticos con dueño de riesgo formalizado ÷ procesos y activos críticos × 100.
- **Unidad y polaridad:** % · Mayor es mejor · **Frecuencia:** Trimestral · **Audiencia:** Directorio · Comité de riesgos
- **Fuente de datos:** Registro de procesos críticos (BIA), CMDB y registro de riesgos. **Evidencia (ejemplo Microsoft):** Clasificación de activos críticos en Microsoft Security Exposure Management y registro de dueños en Dataverse.
- **Estadios:** E1 Menos de 40%: el riesgo cibernético se asigna por defecto a TI o al CISO. | E2 40% a 59%: dueños nominados sin aceptación formal. | E3 60% a 79%: matriz RACI aprobada; los dueños firman tratamientos y aceptaciones. | E4 80% a 94%: dueños con objetivos asociados y revisión trimestral de su cartera de riesgos. | E5 95% o más: dueños también para agentes y procesos automatizados; cambios de dueño gestionados en el ciclo de vida.
- **Umbrales:** E2 ≥ 40% · E3 ≥ 60% · E4 ≥ 80% · E5 ≥ 95% (E3 = mínimo aceptable; E4 = meta por defecto)
- **Correspondencias:** NIST CSF 2.0 GV.RR · CIS v8.1 — · ISO/IEC 27001:2022 5.2 (roles y responsabilidades) · Otros: COBIT 2019 (APO01); DORA art. 5

#### K10 · Ejecutivos con objetivos de ciberseguridad en su evaluación
- **Coordenadas:** T02 · GV10 Ética, cultura y rendición de cuentas · D01 Cybersecurity Governance (secundarios: D24) · Gobierno · GM-24 G6.2 · KPI · Implementación · Adelantado
- **Qué mide:** Porcentaje de miembros del comité ejecutivo y líderes de unidades de negocio con objetivos de ciberseguridad o de riesgo digital ponderados en su evaluación de desempeño o en sus incentivos.
- **Por qué importa:** Lo que no está en los incentivos compite en desventaja con los objetivos comerciales. El indicador mide si la seguridad es una responsabilidad compartida en la práctica.
- **Fórmula:** Ejecutivos con objetivos de seguridad ponderados ÷ ejecutivos del alcance × 100.
- **Unidad y polaridad:** % · Mayor es mejor · **Frecuencia:** Anual · **Audiencia:** Directorio · Comité de compensaciones
- **Fuente de datos:** Sistema de gestión del desempeño; cuadros de mando ejecutivos. **Evidencia (ejemplo Microsoft):** Cuadro de mando en Power BI alimentado por el sistema de recursos humanos.
- **Estadios:** E1 Menos de 10%: la seguridad no aparece en los objetivos ejecutivos. | E2 10% a 29%: objetivos genéricos (p. ej., «cumplir las políticas») sin peso. | E3 30% a 59%: objetivos medibles en las unidades críticas, con ponderación explícita. | E4 60% a 89%: objetivos ligados a los KRI de cada unidad y revisados por el comité. | E5 90% o más: incentivos alineados al apetito de riesgo, incluidos los riesgos de IA de cada área.
- **Umbrales:** E2 ≥ 10% · E3 ≥ 30% · E4 ≥ 60% · E5 ≥ 90% (E3 = mínimo aceptable; E4 = meta por defecto)
- **Correspondencias:** NIST CSF 2.0 GV.RR · CIS v8.1 — · ISO/IEC 27001:2022 5.1 (liderazgo y compromiso) · Otros: NIS2 art. 20 (responsabilidad del órgano de dirección)

#### K11 · Comportamiento seguro: tasa de reporte de phishing
- **Coordenadas:** T02 · PR05 Preparación de personas y procedimientos · D24 Security Workforce & Human Factors (secundarios: D09) · Gestión · GM-24 M1.2 · KPI · Efectividad · Adelantado
- **Qué mide:** Porcentaje de usuarios que reportan por el canal oficial los mensajes de phishing simulados (y tendencia de reportes reales), idealmente antes de que alguien haga clic.
- **Por qué importa:** El clic mide vulnerabilidad; el reporte mide cultura y convierte a cada persona en un sensor. Es el mejor indicador adelantado del factor humano, incluido el fraude con voces y videos sintéticos.
- **Fórmula:** Usuarios que reportaron la simulación ÷ usuarios que la recibieron × 100 (promedio de las campañas del período).
- **Unidad y polaridad:** % · Mayor es mejor · **Frecuencia:** Trimestral · **Audiencia:** CISO · Comité ejecutivo
- **Fuente de datos:** Plataforma de simulación de phishing; buzón de reportes. **Evidencia (ejemplo Microsoft):** Attack simulation training de Microsoft Defender for Office 365 (tasa de reporte y de compromiso).
- **Estadios:** E1 Menos de 10%: no hay un canal de reporte simple; solo se mide el clic. | E2 10% a 24%: botón de reporte disponible; campañas anuales. | E3 25% a 44%: campañas trimestrales por riesgo del rol y retroalimentación inmediata. | E4 45% a 64%: reportes reales triados automáticamente; reconocimiento a quienes reportan. | E5 65% o más: cultura de sensor colectivo: simulaciones adaptativas (incluye deepfakes de voz y video) y triaje con agentes.
- **Umbrales:** E2 ≥ 10% · E3 ≥ 25% · E4 ≥ 45% · E5 ≥ 65% (E3 = mínimo aceptable; E4 = meta por defecto)
- **Correspondencias:** NIST CSF 2.0 PR.AT · CIS v8.1 14 · ISO/IEC 27001:2022 6.3 (concienciación, educación y formación) · Otros: PCI DSS v4.0.1 (req. 12.6)

#### K12 · Cobertura de capacidades críticas del equipo de seguridad
- **Coordenadas:** T02 · ID05 Evaluación de capacidades y brechas · D24 Security Workforce & Human Factors (secundarios: D04) · Gestión · GM-24 M1.2 · KRI · Implementación · Adelantado
- **Qué mide:** Porcentaje de las capacidades críticas del modelo operativo de seguridad (OT, nube, identidad, detección, seguridad de IA, respuesta, entre otras) cubiertas por personas con competencia demostrada, propias o de socios contratados.
- **Por qué importa:** La brecha de talento se traduce en controles sin dueño y en dependencia de pocas personas. Medir cobertura por capacidad orienta contratación, formación y tercerización.
- **Fórmula:** Capacidades críticas cubiertas con competencia demostrada ÷ capacidades críticas del modelo × 100.
- **Unidad y polaridad:** % · Mayor es mejor · **Frecuencia:** Semestral · **Audiencia:** CISO · Comité ejecutivo
- **Fuente de datos:** Modelo operativo de seguridad; matriz de competencias; contratos de servicios gestionados. **Evidencia (ejemplo Microsoft):** Credenciales de Microsoft Learn y matriz de competencias en Power BI.
- **Estadios:** E1 Menos de 50%: capacidades críticas sin titular; dependencia de personas «héroe». | E2 50% a 69%: inventario de capacidades; brechas cubiertas de forma reactiva. | E3 70% a 84%: plan de capacidades con presupuesto; socios con acuerdos de nivel de servicio. | E4 85% a 94%: rotación y entrenamiento cruzado; métricas de competencia por capacidad. | E5 95% o más: modelo humano-agente: tareas rutinarias delegadas a agentes supervisados y talento enfocado en el juicio.
- **Umbrales:** E2 ≥ 50% · E3 ≥ 70% · E4 ≥ 85% · E5 ≥ 95% (E3 = mínimo aceptable; E4 = meta por defecto)
- **Correspondencias:** NIST CSF 2.0 GV.RR · CIS v8.1 14 · ISO/IEC 27001:2022 7.2 (competencia) · Otros: NICE Framework (NIST SP 800-181r1); NIS2 art. 20.2

#### K13 · Retención del talento crítico de seguridad
- **Coordenadas:** T02 · GV05 Gobierno de programas, recursos e inversión · D24 Security Workforce & Human Factors (secundarios: D04) · Gestión · GM-24 M1.2 · KPI · Impacto · Rezagado
- **Qué mide:** Porcentaje de las personas en roles críticos de seguridad que permanecen en la organización en los últimos 12 meses (complemento de la rotación voluntaria).
- **Por qué importa:** Cada salida en un rol crítico se lleva contexto, accesos y relaciones. La retención es el resultado visible del liderazgo, de la carga de trabajo y de la propuesta de desarrollo.
- **Fórmula:** (1 − bajas voluntarias en roles críticos ÷ dotación promedio en roles críticos) × 100, en 12 meses móviles.
- **Unidad y polaridad:** % · Mayor es mejor · **Frecuencia:** Semestral · **Audiencia:** CISO · Recursos humanos
- **Fuente de datos:** Sistema de recursos humanos. **Evidencia (ejemplo Microsoft):** Reportes de recursos humanos en Power BI; encuestas de clima con Microsoft Viva Glint.
- **Estadios:** E1 Menos de 75%: rotación alta y no analizada; dependencia de contratistas sin transferencia de conocimiento. | E2 75% a 84%: entrevistas de salida y acciones aisladas. | E3 85% a 89%: plan de carrera y compensación de mercado para los roles críticos. | E4 90% a 94%: carga sostenible (guardias, alertas por analista) medida y gestionada. | E5 95% o más: propuesta de valor distintiva: trabajo de alto juicio, automatización de lo repetitivo y movilidad interna.
- **Umbrales:** E2 ≥ 75% · E3 ≥ 85% · E4 ≥ 90% · E5 ≥ 95% (E3 = mínimo aceptable; E4 = meta por defecto)
- **Correspondencias:** NIST CSF 2.0 GV.RR · CIS v8.1 — · ISO/IEC 27001:2022 7.2 (competencia) · Otros: ISC2 Cybersecurity Workforce Study

#### K14 · Supervisión activa del Directorio sobre el ciberriesgo
- **Coordenadas:** T02 · GV07 Supervisión y reporting ejecutivo · D01 Cybersecurity Governance (secundarios: D24) · Gobierno · GM-24 G6.1 · KCI · Implementación · Adelantado
- **Qué mide:** Porcentaje de las sesiones del Directorio (o de su comité de riesgos) con ciberriesgo en agenda que terminan con decisiones o requerimientos registrados, no solo con una «toma de conocimiento».
- **Por qué importa:** Varias regulaciones exigen que el órgano de dirección apruebe y supervise las medidas de ciberseguridad. Un Directorio que solo toma nota no gobierna.
- **Fórmula:** Sesiones con ciberriesgo en agenda y al menos una decisión o requerimiento registrado ÷ sesiones con ciberriesgo previstas en el calendario anual × 100.
- **Unidad y polaridad:** % · Mayor es mejor · **Frecuencia:** Trimestral · **Audiencia:** Directorio
- **Fuente de datos:** Calendario y actas del Directorio y de sus comités. **Evidencia (ejemplo Microsoft):** Actas y materiales en SharePoint protegidos con etiquetas de confidencialidad de Microsoft Purview.
- **Estadios:** E1 Menos de 25%: el ciberriesgo llega al Directorio solo después de un incidente. | E2 25% a 49%: presentaciones informativas sin decisiones; el Directorio no recibe formación. | E3 50% a 74%: agenda anual aprobada, formación anual del Directorio y decisiones registradas. | E4 75% a 94%: comité con mandato explícito sobre ciberriesgo y seguimiento de los pedidos al CISO. | E5 95% o más: el Directorio fija un apetito cuantificado, incluye los riesgos de IA y agentes y evalúa su propia eficacia de supervisión.
- **Umbrales:** E2 ≥ 25% · E3 ≥ 50% · E4 ≥ 75% · E5 ≥ 95% (E3 = mínimo aceptable; E4 = meta por defecto)
- **Correspondencias:** NIST CSF 2.0 GV.OV · CIS v8.1 — · ISO/IEC 27001:2022 9.3 (revisión por la dirección) · Otros: NIS2 art. 20; DORA art. 5; SEC Regulation S-K Item 106(c)

#### K15 · Ejercicios de crisis con participación ejecutiva
- **Coordenadas:** T02 · RS01 Preparación y coordinación de respuesta · D15 Incident Response & Crisis Management (secundarios: D16) · Gobierno · GM-24 M5.1 · KPI · Implementación · Adelantado
- **Qué mide:** Porcentaje de los ejercicios de crisis planificados (de mesa o funcionales) realizados en el año con participación efectiva del comité ejecutivo y de las áreas de negocio, legales y de comunicación.
- **Por qué importa:** Los planes que el nivel ejecutivo nunca ensayó fallan en la primera hora. El ejercicio construye memoria muscular y revela brechas de autoridad y de comunicación.
- **Fórmula:** Ejercicios realizados con participación ejecutiva ÷ ejercicios planificados en el programa anual × 100.
- **Unidad y polaridad:** % · Mayor es mejor · **Frecuencia:** Semestral · **Audiencia:** Directorio · Comité ejecutivo
- **Fuente de datos:** Programa anual de ejercicios; informes de ejercicio. **Evidencia (ejemplo Microsoft):** Escenarios basados en Microsoft Defender Threat Intelligence; bitácora y acciones en Teams y Planner.
- **Estadios:** E1 Menos de 25%: no hay programa de ejercicios o los ejecutivos delegan su participación. | E2 25% a 49%: un ejercicio técnico anual sin el nivel ejecutivo. | E3 50% a 74%: programa anual con al menos un ejercicio ejecutivo (ransomware o caída crítica). | E4 75% a 99%: escenarios propios del sector (OT, fraude, terceros, IA) con hallazgos gestionados. | E5 100%: ejercicios sorpresa e intersectoriales con proveedores y autoridades; se mide el tiempo de decisión (K05).
- **Umbrales:** E2 ≥ 25% · E3 ≥ 50% · E4 ≥ 75% · E5 ≥ 100% (E3 = mínimo aceptable; E4 = meta por defecto)
- **Correspondencias:** NIST CSF 2.0 ID.IM · CIS v8.1 17 · ISO/IEC 27001:2022 5.24 (planificación de la gestión de incidentes) · Otros: DORA art. 24–26 (pruebas; TLPT al menos cada 3 años); NIS2 art. 21; TSA SD Pipeline-2021-02 (prueba anual del plan de respuesta)

#### K16 · Roles críticos con suplente entrenado
- **Coordenadas:** T02 · RC02 Continuidad y operación degradada · D24 Security Workforce & Human Factors (secundarios: D16) · Gestión · GM-24 M6.1 · KRI · Implementación · Adelantado
- **Qué mide:** Porcentaje de roles críticos de seguridad y de operación tecnológica (incluidos los de OT y de respuesta) con al menos un suplente entrenado y habilitado para actuar.
- **Por qué importa:** La dependencia de personas clave es un punto único de falla tan real como un servidor sin redundancia, sobre todo en equipos pequeños y en crisis prolongadas.
- **Fórmula:** Roles críticos con suplente entrenado y accesos habilitados ÷ roles críticos identificados × 100.
- **Unidad y polaridad:** % · Mayor es mejor · **Frecuencia:** Semestral · **Audiencia:** CISO · Continuidad del negocio
- **Fuente de datos:** Mapa de roles críticos; registros de entrenamiento y de habilitación de accesos. **Evidencia (ejemplo Microsoft):** Paquetes de acceso de Microsoft Entra ID Governance para suplencias.
- **Estadios:** E1 Menos de 40%: conocimiento concentrado en pocas personas y sin documentar. | E2 40% a 59%: suplentes nominados sin práctica ni accesos. | E3 60% a 79%: suplentes entrenados con procedimientos documentados. | E4 80% a 94%: rotación planificada y prácticas de suplencia en los ejercicios. | E5 95% o más: suplencia humano-agente: libretos ejecutables por agentes supervisados y por suplentes.
- **Umbrales:** E2 ≥ 40% · E3 ≥ 60% · E4 ≥ 80% · E5 ≥ 95% (E3 = mínimo aceptable; E4 = meta por defecto)
- **Correspondencias:** NIST CSF 2.0 GV.RR · CIS v8.1 — · ISO/IEC 27001:2022 5.29 (seguridad de la información durante la disrupción) · Otros: ISO 22301

### T03 · STRATEGY & BUSINESS

#### K17 · Inversión en seguridad trazada a riesgos y objetivos del negocio
- **Coordenadas:** T03 · GV01 Contexto empresarial y estrategia · D04 Security Program & Investment Management (secundarios: D01, D02) · Gobierno · GM-24 G1.2 · KPI · Implementación · Adelantado
- **Qué mide:** Porcentaje del presupuesto de seguridad (inversión y gasto recurrente) asignado a iniciativas trazadas explícitamente a riesgos priorizados del registro o a objetivos estratégicos del negocio.
- **Por qué importa:** El gasto que no se explica en términos de riesgo o de negocio es el primero en recortarse y el más difícil de defender. La trazabilidad convierte el presupuesto en estrategia.
- **Fórmula:** Presupuesto asignado a iniciativas con trazabilidad a un riesgo u objetivo ÷ presupuesto total de seguridad × 100.
- **Unidad y polaridad:** % · Mayor es mejor · **Frecuencia:** Semestral · **Audiencia:** Comité ejecutivo · Directorio
- **Fuente de datos:** Presupuesto y portafolio de proyectos; registro de riesgos. **Evidencia (ejemplo Microsoft):** Portafolio en Microsoft Planner o Project y trazabilidad riesgo-iniciativa en Power BI.
- **Estadios:** E1 Menos de 40%: presupuesto inercial por herramientas, sin vínculo con riesgos. | E2 40% a 59%: justificación cualitativa de las principales iniciativas. | E3 60% a 79%: portafolio priorizado por riesgo, con dueños de negocio. | E4 80% a 94%: casos de negocio con reducción de riesgo estimada y revisión de beneficios. | E5 95% o más: asignación dinámica según exposición cuantificada y objetivos de negocio, incluida la adopción de IA.
- **Umbrales:** E2 ≥ 40% · E3 ≥ 60% · E4 ≥ 80% · E5 ≥ 95% (E3 = mínimo aceptable; E4 = meta por defecto)
- **Correspondencias:** NIST CSF 2.0 GV.OC · CIS v8.1 — · ISO/IEC 27001:2022 6.2 (objetivos de seguridad) · Otros: COBIT 2019 (EDM02, APO05); ISO/IEC 27014:2020

#### K18 · Avance del roadmap estratégico de seguridad
- **Coordenadas:** T03 · GV05 Gobierno de programas, recursos e inversión · D04 Security Program & Investment Management · Gestión · GM-24 M1.1 · KPI · Eficiencia · Rezagado
- **Qué mide:** Porcentaje de hitos del roadmap estratégico de seguridad completados en plazo y dentro del presupuesto aprobado, ponderado por la reducción de riesgo esperada de cada hito.
- **Por qué importa:** La estrategia se juzga por su ejecución. Ponderar por reducción de riesgo evita que se cumplan los hitos fáciles y se posterguen los que importan.
- **Fórmula:** Σ peso de riesgo de los hitos completados en plazo y presupuesto ÷ Σ peso de riesgo de los hitos comprometidos para el período × 100.
- **Unidad y polaridad:** % · Mayor es mejor · **Frecuencia:** Trimestral · **Audiencia:** Comité ejecutivo · Directorio
- **Fuente de datos:** Oficina de proyectos; herramienta de gestión de proyectos. **Evidencia (ejemplo Microsoft):** Microsoft Planner o Project y Power BI.
- **Estadios:** E1 Menos de 50%: roadmap inexistente o desactualizado; las prioridades cambian con cada incidente. | E2 50% a 69%: roadmap anual con hitos, sin ponderación ni control de presupuesto. | E3 70% a 84%: seguimiento trimestral con dueños; los desvíos se explican. | E4 85% a 94%: ponderación por riesgo y replanificación formal ante cambios de amenaza. | E5 95% o más: roadmap adaptativo con escenarios y opciones; ejecución apoyada por automatización y agentes.
- **Umbrales:** E2 ≥ 50% · E3 ≥ 70% · E4 ≥ 85% · E5 ≥ 95% (E3 = mínimo aceptable; E4 = meta por defecto)
- **Correspondencias:** NIST CSF 2.0 GV.OV · CIS v8.1 — · ISO/IEC 27001:2022 6.2 (objetivos de seguridad) · Otros: COBIT 2019 (BAI01)

#### K19 · Reducción de riesgo por unidad de inversión
- **Coordenadas:** T03 · ID04 Análisis de escenarios y cuantificación de riesgos · D04 Security Program & Investment Management (secundarios: D02) · Gobierno · GM-24 G1.2 · KPI · Impacto · Rezagado
- **Qué mide:** Reducción de la pérdida esperada anual (en moneda) atribuible a las iniciativas completadas, dividida por su costo total anualizado (inversión más operación).
- **Por qué importa:** Permite comparar iniciativas en el lenguaje del CFO y del Directorio y evita invertir en controles de bajo retorno en reducción de riesgo.
- **Fórmula:** (Pérdida esperada antes − pérdida esperada después) ÷ costo anualizado de las iniciativas; cuantificación con un método explícito (p. ej., Open FAIR).
- **Unidad y polaridad:** veces (x) · Mayor es mejor · **Frecuencia:** Anual · **Audiencia:** Directorio · CFO
- **Fuente de datos:** Modelos de cuantificación de riesgo; finanzas. **Evidencia (ejemplo Microsoft):** Modelos en Excel o Power BI alimentados con datos de exposición de Microsoft Security Exposure Management.
- **Estadios:** E1 Menos de 0,5x o sin cuantificación: la inversión se argumenta por miedo o por cumplimiento. | E2 0,5x a 0,99x: estimaciones cualitativas convertidas a moneda sin método. | E3 1x a 1,99x: método explícito y supuestos documentados en las iniciativas mayores. | E4 2x a 3,99x: cuantificación sistemática con rangos de incertidumbre y validación posterior. | E5 4x o más: optimización del portafolio por retorno de riesgo, con datos de exposición casi en tiempo real.
- **Umbrales:** E2 ≥ 0,5x · E3 ≥ 1x · E4 ≥ 2x · E5 ≥ 4x (E3 = mínimo aceptable; E4 = meta por defecto)
- **Correspondencias:** NIST CSF 2.0 ID.RA · CIS v8.1 — · ISO/IEC 27001:2022 6.1.3 (tratamiento de riesgos) · Otros: Open FAIR (O-RT 3.1, O-RA 2.1); métricas orientadas a resultados (Gartner, 2024)

#### K20 · Tiempo de habilitación segura de iniciativas
- **Coordenadas:** T03 · PR04 Desarrollo seguro y gestión de cambios · D04 Security Program & Investment Management (secundarios: D11, D20) · Gestión · GM-24 M3.1 · KPI · Eficiencia · Adelantado
- **Qué mide:** Mediana de días hábiles desde que una iniciativa de negocio (aplicación, servicio en la nube, caso de uso de IA, integración con socios) solicita la revisión de seguridad hasta que recibe una decisión con condiciones.
- **Por qué importa:** Una seguridad lenta empuja al negocio a evitarla (TI en la sombra, IA en la sombra). La velocidad con criterio convierte al CISO en habilitador.
- **Fórmula:** Mediana de días hábiles (solicitud → decisión de seguridad documentada) en el período.
- **Unidad y polaridad:** días · Menor es mejor · **Frecuencia:** Trimestral · **Audiencia:** Comité ejecutivo · CIO
- **Fuente de datos:** Gestión de la demanda o tickets de arquitectura. **Evidencia (ejemplo Microsoft):** Formularios y flujos en Power Apps y Power Automate; seguimiento en Azure DevOps.
- **Estadios:** E1 Más de 20 días o sin registro: la revisión de seguridad es un cuello de botella que el negocio evita. | E2 11 a 20 días: proceso definido, sin criterios de riesgo para acelerar. | E3 6 a 10 días: revisión proporcional al riesgo y patrones preaprobados. | E4 3 a 5 días: autoservicio con controles por defecto y revisión solo de las excepciones. | E5 2 días o menos: evaluación asistida por IA con validación humana; seguridad integrada desde la concepción.
- **Umbrales:** E2 ≤ 20 días · E3 ≤ 10 días · E4 ≤ 5 días · E5 ≤ 2 días (E3 = mínimo aceptable; E4 = meta por defecto)
- **Correspondencias:** NIST CSF 2.0 PR.PS · CIS v8.1 16 · ISO/IEC 27001:2022 5.8 (seguridad en la gestión de proyectos) · Otros: —

#### K21 · Procesos críticos con BIA vigente y dependencias mapeadas
- **Coordenadas:** T03 · ID02 Dependencias y criticidad del negocio · D16 Business Continuity & Cyber Recovery (secundarios: D17) · Gestión · GM-24 M5.1 · KCI · Implementación · Adelantado
- **Qué mide:** Porcentaje de procesos de negocio críticos con análisis de impacto (BIA) vigente —RTO, RPO, impacto económico y regulatorio— y con sus dependencias tecnológicas y de terceros mapeadas.
- **Por qué importa:** Sin saber qué depende de qué no se puede priorizar ni recuperar. El BIA traduce tecnología en consecuencias de negocio.
- **Fórmula:** Procesos críticos con BIA de menos de 12 meses y mapa de dependencias ÷ procesos críticos × 100.
- **Unidad y polaridad:** % · Mayor es mejor · **Frecuencia:** Semestral · **Audiencia:** Comité de riesgos · Continuidad
- **Fuente de datos:** Herramienta de continuidad (BIA); CMDB; registro de proveedores. **Evidencia (ejemplo Microsoft):** Mapa de dependencias con Azure Resource Graph y activos críticos en Microsoft Security Exposure Management.
- **Estadios:** E1 Menos de 40%: no hay BIA o es antiguo; la criticidad la define TI. | E2 40% a 59%: BIA anual en algunas áreas; dependencias incompletas. | E3 60% a 79%: BIA vigente para los procesos críticos con RTO/RPO aprobados por el negocio. | E4 80% a 94%: dependencias de terceros, nube y OT mapeadas y conectadas a la CMDB. | E5 95% o más: mapa vivo de dependencias actualizado automáticamente, incluidos agentes y modelos de IA.
- **Umbrales:** E2 ≥ 40% · E3 ≥ 60% · E4 ≥ 80% · E5 ≥ 95% (E3 = mínimo aceptable; E4 = meta por defecto)
- **Correspondencias:** NIST CSF 2.0 GV.OC · CIS v8.1 — · ISO/IEC 27001:2022 5.30 (preparación de las TIC para la continuidad) · Otros: ISO 22301; DORA art. 8

#### K22 · Resultados del perfil objetivo alcanzados (NIST CSF 2.0)
- **Coordenadas:** T03 · ID05 Evaluación de capacidades y brechas · D04 Security Program & Investment Management (secundarios: D01) · Gobierno · GM-24 G2.1 · KPI · Efectividad · Rezagado
- **Qué mide:** Porcentaje de los resultados (subcategorías) priorizados en el perfil objetivo de la organización que ya alcanzan el nivel objetivo en el perfil actual, según una evaluación con evidencia.
- **Por qué importa:** El perfil objetivo es la estrategia expresada en resultados. Medir la brecha muestra al Directorio cuánto falta, dónde y a qué ritmo se cierra.
- **Fórmula:** Subcategorías priorizadas en nivel objetivo ÷ subcategorías priorizadas del perfil objetivo × 100.
- **Unidad y polaridad:** % · Mayor es mejor · **Frecuencia:** Anual · **Audiencia:** Directorio · Comité de riesgos
- **Fuente de datos:** Evaluación de perfiles NIST CSF 2.0 (o C2M2 / IEC 62443-2-1 en OT). **Evidencia (ejemplo Microsoft):** Evaluaciones de Microsoft Purview Compliance Manager con plantilla NIST CSF y panel de cumplimiento normativo de Defender for Cloud.
- **Estadios:** E1 Menos de 30% o sin perfil objetivo: la estrategia no tiene un destino verificable. | E2 30% a 49%: autoevaluación sin evidencia; objetivo definido por TI. | E3 50% a 69%: perfil objetivo aprobado por la dirección; evaluación anual con evidencia. | E4 70% a 84%: evaluación independiente; brechas convertidas en roadmap (K18). | E5 85% o más: perfiles por unidad y por tecnología emergente (IA, OT), actualizados con evidencia continua.
- **Umbrales:** E2 ≥ 30% · E3 ≥ 50% · E4 ≥ 70% · E5 ≥ 85% (E3 = mínimo aceptable; E4 = meta por defecto)
- **Correspondencias:** NIST CSF 2.0 ID.IM · CIS v8.1 — · ISO/IEC 27001:2022 9.1 (seguimiento, medición, análisis y evaluación) · Otros: NIST CSF 2.0 (perfiles actual y objetivo); C2M2 v2.1; CISA CPG 2.0

#### K23 · Requisitos de seguridad de clientes y contratos cumplidos en plazo
- **Coordenadas:** T03 · GV06 Obligaciones legales y contractuales · D03 Compliance & Regulatory Security (secundarios: D07) · Gobierno · GM-24 G3.1 · KPI · Efectividad · Rezagado
- **Qué mide:** Porcentaje de requerimientos de seguridad de clientes y socios (cuestionarios de debida diligencia, cláusulas contractuales, auditorías de clientes, niveles de servicio de seguridad) respondidos o cumplidos dentro del plazo comprometido.
- **Por qué importa:** Para muchas empresas la seguridad es parte del producto: un cuestionario tardío demora ventas y una cláusula incumplida es un riesgo contractual y reputacional.
- **Fórmula:** Requerimientos cumplidos en plazo ÷ requerimientos con vencimiento en el período × 100.
- **Unidad y polaridad:** % · Mayor es mejor · **Frecuencia:** Trimestral · **Audiencia:** Comité ejecutivo · Comercial
- **Fuente de datos:** Registro de requerimientos de clientes; CRM; gestión de contratos. **Evidencia (ejemplo Microsoft):** Biblioteca de respuestas y evidencias en SharePoint; borradores con Microsoft 365 Copilot revisados por personas.
- **Estadios:** E1 Menos de 60%: respuestas artesanales y tardías; sin inventario de compromisos contractuales. | E2 60% a 79%: biblioteca de respuestas; compromisos dispersos en los contratos. | E3 80% a 89%: registro de compromisos con dueño y vencimiento. | E4 90% a 97%: portal de confianza con evidencias actualizadas. | E5 98% o más: evidencia continua compartible y respuestas asistidas por IA con revisión humana.
- **Umbrales:** E2 ≥ 60% · E3 ≥ 80% · E4 ≥ 90% · E5 ≥ 98% (E3 = mínimo aceptable; E4 = meta por defecto)
- **Correspondencias:** NIST CSF 2.0 GV.OC · CIS v8.1 — · ISO/IEC 27001:2022 5.31 (requisitos legales, regulatorios y contractuales) · Otros: ISO/IEC 27001:2022 cl. 4.2 (partes interesadas)

#### K24 · Pérdidas por incidentes frente a la tolerancia anual
- **Coordenadas:** T03 · GV04 Apetito, tolerancia y aceptación de riesgo · D02 Cyber Risk Management (secundarios: D04) · Gobierno · GM-24 G6.2 · KRI · Impacto · Rezagado
- **Qué mide:** Pérdidas económicas totales por incidentes de ciberseguridad en el año (respuesta, interrupción, fraude, multas, compensaciones) expresadas como porcentaje de la tolerancia anual de pérdida aprobada por el Directorio.
- **Por qué importa:** Es la medida final de efectividad del programa en el lenguaje del negocio. Compararla con la tolerancia vuelve accionable el apetito de riesgo.
- **Fórmula:** Σ pérdidas por incidentes cibernéticos en 12 meses ÷ tolerancia anual de pérdida aprobada × 100.
- **Unidad y polaridad:** % · Menor es mejor · **Frecuencia:** Trimestral · **Audiencia:** Directorio · CFO
- **Fuente de datos:** Registro de eventos de pérdida (riesgo operacional); finanzas; seguros. **Evidencia (ejemplo Microsoft):** Registro de pérdidas en Dataverse vinculado a los incidentes de Microsoft Sentinel.
- **Estadios:** E1 Más de 100% o sin registro de pérdidas: no se sabe cuánto cuestan los incidentes. | E2 76% a 100%: pérdidas estimadas después de incidentes mayores, sin tolerancia formal. | E3 51% a 75%: tolerancia aprobada; registro de pérdidas conciliado con finanzas. | E4 26% a 50%: pérdidas atribuidas por escenario y por control que falló. | E5 25% o menos: pérdidas previstas por modelo y contrastadas; transferencia (seguro) optimizada.
- **Umbrales:** E2 ≤ 100% · E3 ≤ 75% · E4 ≤ 50% · E5 ≤ 25% (E3 = mínimo aceptable; E4 = meta por defecto)
- **Correspondencias:** NIST CSF 2.0 GV.RM · CIS v8.1 — · ISO/IEC 27001:2022 9.1 (seguimiento, medición, análisis y evaluación) · Otros: Basilea (eventos de pérdida por riesgo operacional); SEC Form 8-K Item 1.05

### T04 · RISK & RESILIENCE

#### K25 · Riesgos residuales fuera del apetito
- **Coordenadas:** T04 · GV04 Apetito, tolerancia y aceptación de riesgo · D02 Cyber Risk Management (secundarios: D01) · Gobierno · GM-24 G4.2 · KRI · Impacto · Rezagado
- **Qué mide:** Porcentaje de riesgos cibernéticos del registro cuyo nivel residual supera la tolerancia aprobada sin aceptación vigente ni plan de tratamiento en curso.
- **Por qué importa:** Es la síntesis de la postura frente al apetito: cada riesgo fuera de tolerancia sin plan es una decisión pendiente del gobierno.
- **Fórmula:** Riesgos residuales sobre la tolerancia sin plan ni aceptación vigente ÷ riesgos del registro × 100.
- **Unidad y polaridad:** % · Menor es mejor · **Frecuencia:** Trimestral · **Audiencia:** Directorio · Comité de riesgos
- **Fuente de datos:** Registro de riesgos (GRC). **Evidencia (ejemplo Microsoft):** Registro de riesgos en Dataverse y Power BI; brechas de control asociadas en Microsoft Purview Compliance Manager.
- **Estadios:** E1 Más de 20% o sin tolerancias definidas: el apetito es una declaración sin umbrales. | E2 11% a 20%: tolerancias cualitativas y seguimiento anual. | E3 6% a 10%: tolerancias por categoría y seguimiento trimestral. | E4 2% a 5%: tolerancias cuantificadas; cada desvío tiene plan o aceptación firmada. | E5 1% o menos: monitoreo continuo con KRI automatizados; reacción en días ante cada cruce.
- **Umbrales:** E2 ≤ 20% · E3 ≤ 10% · E4 ≤ 5% · E5 ≤ 1% (E3 = mínimo aceptable; E4 = meta por defecto)
- **Correspondencias:** NIST CSF 2.0 GV.RM · CIS v8.1 — · ISO/IEC 27001:2022 6.1.3 (tratamiento de riesgos) · Otros: CRISC 2025 (R3); COSO ERM

#### K26 · Pérdida esperada de los escenarios prioritarios frente al apetito
- **Coordenadas:** T04 · ID04 Análisis de escenarios y cuantificación de riesgos · D02 Cyber Risk Management (secundarios: D12) · Gobierno · GM-24 G5.1 · KRI · Impacto · Adelantado
- **Qué mide:** Pérdida esperada anual (en moneda) de los diez escenarios cibernéticos prioritarios —ransomware, fraude, caída de proveedor crítico, sabotaje OT, fuga de datos, abuso de agentes, entre otros— comparada con el apetito anual de pérdida.
- **Por qué importa:** Cuantificar la exposición permite compararla con otros riesgos, decidir la transferencia y comprobar si el programa realmente reduce exposición.
- **Fórmula:** Σ (frecuencia anual estimada × magnitud de pérdida) de los escenarios prioritarios ÷ apetito anual de pérdida aprobado × 100.
- **Unidad y polaridad:** % · Menor es mejor · **Frecuencia:** Semestral · **Audiencia:** Directorio · CFO · Comité de riesgos
- **Fuente de datos:** Modelo de cuantificación (Open FAIR u otro); datos de incidentes y de exposición. **Evidencia (ejemplo Microsoft):** Datos de exposición y rutas de ataque de Microsoft Security Exposure Management como insumo del modelo.
- **Estadios:** E1 Más de 150% o sin cuantificación: la exposición no se puede comparar con el apetito. | E2 101% a 150%: cuantificación puntual de escenarios aislados. | E3 76% a 100%: los diez escenarios prioritarios cuantificados con rangos y supuestos aprobados. | E4 51% a 75%: cuantificación integrada a la planificación financiera y a la decisión de seguros. | E5 50% o menos: cuantificación continua con datos de exposición y simulación de escenarios de IA y de terceros.
- **Umbrales:** E2 ≤ 150% · E3 ≤ 100% · E4 ≤ 75% · E5 ≤ 50% (E3 = mínimo aceptable; E4 = meta por defecto)
- **Correspondencias:** NIST CSF 2.0 ID.RA · CIS v8.1 — · ISO/IEC 27001:2022 6.1.2 (evaluación de riesgos) · Otros: Open FAIR (O-RT 3.1, O-RA 2.1); ISO/IEC 27005:2022

#### K27 · Servicios críticos concentrados en un proveedor sin alternativa
- **Coordenadas:** T04 · ID02 Dependencias y criticidad del negocio · D17 Third-Party & Supply Chain Security (secundarios: D10, D16) · Gobierno · GM-24 M6.2 · KRI · Impacto · Adelantado
- **Qué mide:** Porcentaje de servicios de negocio críticos que dependen de un único proveedor tecnológico (nube, software crítico, telecomunicaciones, integrador OT, plataforma de IA) sin alternativa viable ni plan de salida probado.
- **Por qué importa:** La concentración convierte la falla de un tercero en una crisis propia. Los supervisores financieros y de infraestructura crítica la vigilan cada vez más.
- **Fórmula:** Servicios críticos con proveedor único sin plan de salida ni alternativa probada ÷ servicios críticos × 100.
- **Unidad y polaridad:** % · Menor es mejor · **Frecuencia:** Semestral · **Audiencia:** Directorio · Comité de riesgos
- **Fuente de datos:** Registro de terceros (TPRM); BIA; arquitectura. **Evidencia (ejemplo Microsoft):** Inventario de dependencias con Azure Resource Graph y de aplicaciones en la nube con Microsoft Defender for Cloud Apps.
- **Estadios:** E1 Más de 50% o desconocido: dependencias críticas sin identificar. | E2 31% a 50%: dependencias conocidas, sin estrategia de salida. | E3 16% a 30%: planes de salida documentados para los proveedores críticos. | E4 6% a 15%: alternativas contratadas o arquitectura multiproveedor en los servicios clave. | E5 5% o menos: planes de salida probados; portabilidad de modelos y agentes de IA evaluada.
- **Umbrales:** E2 ≤ 50% · E3 ≤ 30% · E4 ≤ 15% · E5 ≤ 5% (E3 = mínimo aceptable; E4 = meta por defecto)
- **Correspondencias:** NIST CSF 2.0 GV.SC · CIS v8.1 15 · ISO/IEC 27001:2022 5.21 (seguridad en la cadena de suministro de TIC) · Otros: DORA art. 28–29 (riesgo de concentración)

#### K28 · Respaldos inmutables de sistemas críticos con restauración probada
- **Coordenadas:** T04 · RC01 Restauración y recuperación técnica · D16 Business Continuity & Cyber Recovery (secundarios: D10) · Gestión · GM-24 M6.1 · KCI · Efectividad · Adelantado
- **Qué mide:** Porcentaje de sistemas críticos (incluidos los servicios de identidad, OT y la configuración de agentes) con respaldo inmutable o aislado y con una restauración completa exitosa en los últimos seis meses.
- **Por qué importa:** Ante ransomware o sabotaje, poder restaurar desde una copia limpia decide si el incidente dura días o meses.
- **Fórmula:** Sistemas críticos con respaldo inmutable o aislado y restauración exitosa en seis meses ÷ sistemas críticos × 100.
- **Unidad y polaridad:** % · Mayor es mejor · **Frecuencia:** Trimestral · **Audiencia:** Directorio · Comité de riesgos · CIO
- **Fuente de datos:** Plataforma de respaldo; registros de pruebas de restauración. **Evidencia (ejemplo Microsoft):** Azure Backup con bóvedas inmutables, Microsoft 365 Backup y Azure Site Recovery.
- **Estadios:** E1 Menos de 50%: copias sin aislamiento ni pruebas, con credenciales compartidas con producción. | E2 50% a 69%: copias diarias y pruebas de restauración parciales. | E3 70% a 84%: inmutabilidad o aislamiento en los sistemas críticos; pruebas semestrales. | E4 85% a 94%: restauración completa de identidad y servicios críticos probada en un entorno limpio. | E5 95% o más: recuperación orquestada y verificada automáticamente, incluidas las configuraciones de agentes y modelos.
- **Umbrales:** E2 ≥ 50% · E3 ≥ 70% · E4 ≥ 85% · E5 ≥ 95% (E3 = mínimo aceptable; E4 = meta por defecto)
- **Correspondencias:** NIST CSF 2.0 PR.DS · CIS v8.1 11 · ISO/IEC 27001:2022 8.13 (respaldo de la información) · Otros: DORA art. 12

#### K29 · Operación degradada probada en procesos críticos
- **Coordenadas:** T04 · RC02 Continuidad y operación degradada · D16 Business Continuity & Cyber Recovery (secundarios: D18) · Gestión · GM-24 M6.1 · KCI · Efectividad · Adelantado
- **Qué mide:** Porcentaje de procesos críticos con un modo de operación degradada o manual (sin TI, sin red corporativa o sin conectividad IT/OT) documentado y probado en los últimos 12 meses.
- **Por qué importa:** Seguir operando con capacidades mínimas mientras se recupera la tecnología protege ingresos, servicio y seguridad física. En OT y logística es la diferencia entre una pausa y un colapso.
- **Fórmula:** Procesos críticos con modo degradado probado en 12 meses ÷ procesos críticos × 100.
- **Unidad y polaridad:** % · Mayor es mejor · **Frecuencia:** Semestral · **Audiencia:** Directorio · Comité de riesgos · Operaciones
- **Fuente de datos:** Planes de continuidad; informes de prueba. **Evidencia (ejemplo Microsoft):** Planes y evidencias de prueba en SharePoint con retención de Microsoft Purview.
- **Estadios:** E1 Menos de 25%: no existe operación manual o nadie la recuerda. | E2 25% a 49%: modos degradados documentados pero no probados. | E3 50% a 74%: pruebas anuales en los procesos críticos con criterios de éxito. | E4 75% a 89%: pruebas con desconexión real IT/OT y medición de la capacidad residual. | E5 90% o más: diseño seguro ante fallas, con islas operativas y conmutación ensayada.
- **Umbrales:** E2 ≥ 25% · E3 ≥ 50% · E4 ≥ 75% · E5 ≥ 90% (E3 = mínimo aceptable; E4 = meta por defecto)
- **Correspondencias:** NIST CSF 2.0 RC.RP · CIS v8.1 — · ISO/IEC 27001:2022 5.29 (seguridad de la información durante la disrupción) · Otros: ISO 22301; ISA/IEC 62443-2-1:2024; TSA SD Pipeline-2021-02 (operación OT con la TI comprometida)

#### K30 · Pruebas de recuperación que cumplen RTO y RPO
- **Coordenadas:** T04 · RC03 Validación de recuperación y retorno seguro · D16 Business Continuity & Cyber Recovery (secundarios: D15) · Gestión · GM-24 M6.1 · KPI · Efectividad · Adelantado
- **Qué mide:** Porcentaje de pruebas de recuperación de servicios críticos en las que el servicio se restableció dentro del RTO, con pérdida de datos dentro del RPO aprobados por el negocio y con validación de integridad antes del retorno.
- **Por qué importa:** Un plan que no cumple sus tiempos en una prueba no los cumplirá en una crisis. Es la evidencia objetiva de resiliencia que piden reguladores y aseguradoras.
- **Fórmula:** Pruebas que cumplieron RTO y RPO con validación de integridad ÷ pruebas de recuperación realizadas × 100.
- **Unidad y polaridad:** % · Mayor es mejor · **Frecuencia:** Semestral · **Audiencia:** Directorio · Comité de riesgos
- **Fuente de datos:** Informes de pruebas de recuperación y continuidad. **Evidencia (ejemplo Microsoft):** Planes de recuperación de Azure Site Recovery con pruebas de conmutación; evidencias en SharePoint.
- **Estadios:** E1 Menos de 40% o sin pruebas: los RTO y RPO son aspiracionales. | E2 40% a 59%: pruebas técnicas parciales, sin el negocio. | E3 60% a 79%: pruebas anuales de punta a punta con el negocio y validación de integridad. | E4 80% a 94%: pruebas de recuperación ante ciberataque (no solo ante desastre) en un entorno limpio. | E5 95% o más: pruebas continuas y automatizadas; RTO verificado también en servicios que usan IA.
- **Umbrales:** E2 ≥ 40% · E3 ≥ 60% · E4 ≥ 80% · E5 ≥ 95% (E3 = mínimo aceptable; E4 = meta por defecto)
- **Correspondencias:** NIST CSF 2.0 RC.RP · CIS v8.1 11 · ISO/IEC 27001:2022 5.30 (preparación de las TIC para la continuidad) · Otros: DORA art. 11–12; ISO 22301

#### K31 · Proveedores críticos evaluados y con cláusulas de seguridad
- **Coordenadas:** T04 · GV09 Gobierno de terceros y ecosistemas · D17 Third-Party & Supply Chain Security (secundarios: D03) · Gestión · GM-24 M6.2 · KCI · Implementación · Adelantado
- **Qué mide:** Porcentaje de proveedores críticos (por acceso, datos o dependencia operativa) con evaluación de riesgo vigente, cláusulas de seguridad y de notificación en el contrato y monitoreo de su postura.
- **Por qué importa:** La superficie de ataque se extiende a través de los terceros; sin evaluación ni cláusulas, el riesgo se hereda sin control ni derecho a exigir.
- **Fórmula:** Proveedores críticos con evaluación de menos de 12 meses, cláusulas vigentes y monitoreo ÷ proveedores críticos × 100.
- **Unidad y polaridad:** % · Mayor es mejor · **Frecuencia:** Trimestral · **Audiencia:** Directorio · Comité de riesgos · Compras
- **Fuente de datos:** Plataforma de gestión de terceros; contratos; calificaciones externas. **Evidencia (ejemplo Microsoft):** Inventario de aplicaciones y proveedores con Microsoft Defender for Cloud Apps; revisiones de acceso de invitados con Microsoft Entra ID Governance.
- **Estadios:** E1 Menos de 40%: no hay criterio de criticidad de proveedores. | E2 40% a 59%: cuestionarios al alta, sin seguimiento ni cláusulas. | E3 60% a 79%: evaluación anual y cláusulas estándar para los críticos. | E4 80% a 94%: monitoreo continuo de la postura y derecho de auditoría ejercido. | E5 95% o más: gestión de cuarta parte y de proveedores de IA (modelos, agentes) con evidencias compartidas.
- **Umbrales:** E2 ≥ 40% · E3 ≥ 60% · E4 ≥ 80% · E5 ≥ 95% (E3 = mínimo aceptable; E4 = meta por defecto)
- **Correspondencias:** NIST CSF 2.0 GV.SC · CIS v8.1 15 · ISO/IEC 27001:2022 5.19–5.22 (relaciones con proveedores) · Otros: DORA art. 28–30; NIS2 art. 21.2(d); ISO 28000:2022; Marco SAFE de la OMA (OEA)

#### K32 · Escenarios críticos con playbook probado
- **Coordenadas:** T04 · RS01 Preparación y coordinación de respuesta · D15 Incident Response & Crisis Management (secundarios: D12) · Gestión · GM-24 M5.1 · KCI · Implementación · Adelantado
- **Qué mide:** Porcentaje de escenarios de incidente prioritarios (ransomware, compromiso de identidad, fraude, incidente en proveedor, sabotaje OT, abuso o falla de un agente de IA, fuga de datos) con playbook aprobado y probado en los últimos 12 meses.
- **Por qué importa:** La respuesta improvisada multiplica tiempos y errores. Un playbook probado por escenario es la unidad mínima de preparación.
- **Fórmula:** Escenarios prioritarios con playbook aprobado y probado en 12 meses ÷ escenarios prioritarios × 100.
- **Unidad y polaridad:** % · Mayor es mejor · **Frecuencia:** Semestral · **Audiencia:** CISO · Comité de crisis
- **Fuente de datos:** Biblioteca de playbooks; informes de ejercicios técnicos. **Evidencia (ejemplo Microsoft):** Playbooks y reglas de automatización en Microsoft Sentinel; respuesta automatizada en Microsoft Defender XDR.
- **Estadios:** E1 Menos de 30%: un plan genérico de incidentes, sin escenarios. | E2 30% a 49%: playbooks para algunos escenarios, no probados. | E3 50% a 74%: playbooks aprobados y probados para los escenarios principales. | E4 75% a 89%: playbooks con automatización parcial que incluyen los roles de terceros. | E5 90% o más: playbooks ejecutables por agentes, con puntos de aprobación humana y prueba continua.
- **Umbrales:** E2 ≥ 30% · E3 ≥ 50% · E4 ≥ 75% · E5 ≥ 90% (E3 = mínimo aceptable; E4 = meta por defecto)
- **Correspondencias:** NIST CSF 2.0 RS.MA · CIS v8.1 17 · ISO/IEC 27001:2022 5.24 (planificación de la gestión de incidentes) · Otros: NIST SP 800-61r3

### T05 · SECURITY ARCHITECTURE

#### K33 · Autenticación resistente al phishing
- **Coordenadas:** T05 · PR01 Identidad y autorización · D05 Identity & Access Security (secundarios: D09) · Gestión · GM-24 M2.2 · KCI · Implementación · Adelantado
- **Qué mide:** Porcentaje de cuentas humanas (primero las privilegiadas y las de acceso remoto) que usan exclusivamente métodos resistentes al phishing: llaves FIDO2, passkeys, Windows Hello for Business o certificados.
- **Por qué importa:** El robo de credenciales y la fatiga de MFA siguen entre las vías de entrada más frecuentes. La autenticación resistente al phishing elimina clases completas de ataque.
- **Fórmula:** Cuentas con método resistente al phishing exigido por política ÷ cuentas del alcance × 100 (informar las privilegiadas por separado).
- **Unidad y polaridad:** % · Mayor es mejor · **Frecuencia:** Mensual · **Audiencia:** Directorio · CISO
- **Fuente de datos:** Proveedor de identidad; reportes de métodos de autenticación. **Evidencia (ejemplo Microsoft):** Microsoft Entra ID: informe de métodos de autenticación y fortalezas de autenticación en Acceso condicional.
- **Estadios:** E1 Menos de 25%: predominan contraseñas o MFA por SMS; no hay inventario de métodos. | E2 25% a 49%: MFA por notificación u OTP generalizado; métodos resistentes solo en algunos administradores. | E3 50% a 79%: todas las cuentas privilegiadas con métodos resistentes; despliegue general en curso. | E4 80% a 94%: métodos resistentes exigidos por política en la mayoría; excepciones con vencimiento. | E5 95% o más: sin contraseñas en la práctica; acceso condicionado por riesgo y por cumplimiento del dispositivo.
- **Umbrales:** E2 ≥ 25% · E3 ≥ 50% · E4 ≥ 80% · E5 ≥ 95% (E3 = mínimo aceptable; E4 = meta por defecto)
- **Correspondencias:** NIST CSF 2.0 PR.AA · CIS v8.1 6 · ISO/IEC 27001:2022 8.5 (autenticación segura) · Otros: CISA CPG 2.0; PCI DSS v4.0.1 (req. 8.4)

#### K34 · Accesos privilegiados sin privilegios permanentes (JIT)
- **Coordenadas:** T05 · PR01 Identidad y autorización · D05 Identity & Access Security (secundarios: D17, D18) · Gestión · GM-24 M2.2 · KCI · Implementación · Adelantado
- **Qué mide:** Porcentaje de asignaciones privilegiadas —internas, de proveedores (incluidos los accesos remotos a OT) e identidades no humanas— otorgadas justo a tiempo, con aprobación, duración limitada y registro de sesión, en lugar de forma permanente.
- **Por qué importa:** Los privilegios permanentes son el atajo favorito del atacante para escalar y moverse. El acceso justo a tiempo reduce la ventana de abuso y deja evidencia de cada uso.
- **Fórmula:** Asignaciones privilegiadas elegibles o justo a tiempo ÷ total de asignaciones privilegiadas (permanentes + elegibles) × 100.
- **Unidad y polaridad:** % · Mayor es mejor · **Frecuencia:** Mensual · **Audiencia:** CISO · Comité de riesgos
- **Fuente de datos:** PAM/PIM; inventario de cuentas privilegiadas y de servicio; registro de accesos remotos de terceros. **Evidencia (ejemplo Microsoft):** Microsoft Entra Privileged Identity Management, Azure Bastion y Microsoft Defender for Identity para cuentas sensibles.
- **Estadios:** E1 Menos de 25%: administradores permanentes generalizados y cuentas compartidas. | E2 25% a 49%: inventario de privilegiados y bóveda de contraseñas. | E3 50% a 74%: acceso justo a tiempo en roles de nube e identidad; accesos remotos de terceros con aprobación. | E4 75% a 89%: acceso justo a tiempo también en OT y servidores; sesiones grabadas y revisadas por muestreo. | E5 90% o más: cero privilegios permanentes; credenciales efímeras para agentes y cargas de trabajo.
- **Umbrales:** E2 ≥ 25% · E3 ≥ 50% · E4 ≥ 75% · E5 ≥ 90% (E3 = mínimo aceptable; E4 = meta por defecto)
- **Correspondencias:** NIST CSF 2.0 PR.AA · CIS v8.1 5, 6 · ISO/IEC 27001:2022 8.2 (derechos de acceso privilegiado) · Otros: ISA/IEC 62443-3-3; NERC CIP-005 (acceso remoto interactivo); TSA SD Pipeline-2021-02 (control de acceso)

#### K35 · Activos conformes a la línea base de configuración segura
- **Coordenadas:** T05 · PR03 Hardening y arquitectura segura · D10 Cloud & Platform Security (secundarios: D08, D09) · Gestión · GM-24 M3.2 · KCI · Implementación · Adelantado
- **Qué mide:** Porcentaje de activos del alcance (servidores, endpoints, servicios en la nube, equipos de red) que cumplen la línea base de configuración segura vigente, incluida una versión con soporte del fabricante o un control compensatorio aprobado.
- **Por qué importa:** La mayoría de los ataques exitosos aprovecha configuraciones débiles o software sin soporte, no vulnerabilidades exóticas. La línea base es la higiene que sostiene todo lo demás.
- **Fórmula:** Activos conformes a la línea base (con soporte vigente o compensación aprobada) ÷ activos del alcance × 100.
- **Unidad y polaridad:** % · Mayor es mejor · **Frecuencia:** Mensual · **Audiencia:** CISO
- **Fuente de datos:** Gestión de configuración y de postura en la nube (CSPM); inventario. **Evidencia (ejemplo Microsoft):** Microsoft Secure Score, recomendaciones y puntuación segura de Defender for Cloud y líneas base de seguridad de Intune.
- **Estadios:** E1 Menos de 50%: configuraciones por defecto y sistemas sin soporte fuera de inventario. | E2 50% a 69%: líneas base documentadas y aplicadas manualmente. | E3 70% a 84%: aplicación automatizada en los nuevos despliegues; los desvíos se reportan. | E4 85% a 94%: corrección automática de desvíos (política como código); activos sin soporte solo con compensación aprobada. | E5 95% o más: postura verificada de forma continua; remediación propuesta por IA y aprobada por personas.
- **Umbrales:** E2 ≥ 50% · E3 ≥ 70% · E4 ≥ 85% · E5 ≥ 95% (E3 = mínimo aceptable; E4 = meta por defecto)
- **Correspondencias:** NIST CSF 2.0 PR.PS · CIS v8.1 4 · ISO/IEC 27001:2022 8.9 (gestión de la configuración) · Otros: CIS Benchmarks; DISA STIG

#### K36 · Segmentación de activos críticos verificada
- **Coordenadas:** T05 · PR03 Hardening y arquitectura segura · D08 Network & Infrastructure Security (secundarios: D18, D19) · Gestión · GM-24 M3.1 · KCI · Efectividad · Adelantado
- **Qué mide:** Porcentaje de activos o zonas críticas (incluidas las zonas OT y las redes de dispositivos IoT) aislados según el diseño aprobado de segmentación —zonas y conductos— y verificados con pruebas de flujo.
- **Por qué importa:** La segmentación limita el radio de explosión: convierte un compromiso local en un incidente acotado y protege los procesos físicos del tráfico corporativo.
- **Fórmula:** Zonas o activos críticos con segmentación verificada en los últimos seis meses ÷ zonas o activos críticos del diseño × 100.
- **Unidad y polaridad:** % · Mayor es mejor · **Frecuencia:** Trimestral · **Audiencia:** CISO · Operaciones
- **Fuente de datos:** Diseño de red; firewalls; herramientas de visibilidad de tráfico y de OT. **Evidencia (ejemplo Microsoft):** Azure Firewall y grupos de seguridad de red; mapa de conexiones OT en Microsoft Defender for IoT.
- **Estadios:** E1 Menos de 40%: red plana; OT accesible desde la red corporativa. | E2 40% a 59%: segmentación perimetral con reglas permisivas y sin revisión. | E3 60% a 79%: zonas y conductos definidos para los activos críticos; reglas revisadas. | E4 80% a 94%: microsegmentación en los sistemas críticos y DMZ industrial verificada. | E5 95% o más: segmentación adaptativa por identidad y riesgo, verificada de forma continua.
- **Umbrales:** E2 ≥ 40% · E3 ≥ 60% · E4 ≥ 80% · E5 ≥ 95% (E3 = mínimo aceptable; E4 = meta por defecto)
- **Correspondencias:** NIST CSF 2.0 PR.IR · CIS v8.1 12, 13 · ISO/IEC 27001:2022 8.22 (segregación de redes) · Otros: ISA/IEC 62443-3-2 (zonas y conductos); NERC CIP-005; TSA SD Pipeline-2021-02 (segmentación IT/OT)

#### K37 · Datos sensibles clasificados y protegidos
- **Coordenadas:** T05 · PR02 Protección de datos y privacidad por diseño · D06 Data Security & Information Protection (secundarios: D07) · Gestión · GM-24 M2.1 · KCI · Implementación · Adelantado
- **Qué mide:** Porcentaje de los repositorios de datos sensibles descubiertos (personales, financieros, propiedad intelectual, secretos operativos) con clasificación aplicada y controles acordes: cifrado, acceso mínimo y prevención de fuga.
- **Por qué importa:** No se puede proteger lo que no se conoce. La clasificación habilita controles proporcionales y es requisito para usar IA con datos corporativos sin exponerlos.
- **Fórmula:** Repositorios sensibles clasificados y con los controles requeridos ÷ repositorios sensibles descubiertos × 100.
- **Unidad y polaridad:** % · Mayor es mejor · **Frecuencia:** Trimestral · **Audiencia:** CISO · Privacidad
- **Fuente de datos:** Descubrimiento y clasificación de datos; DLP; gestión de la postura de datos (DSPM). **Evidencia (ejemplo Microsoft):** Microsoft Purview Information Protection, prevención de pérdida de datos y Data Security Posture Management.
- **Estadios:** E1 Menos de 30%: sin inventario de datos sensibles; la clasificación es voluntaria. | E2 30% a 49%: esquema de clasificación aprobado y etiquetado manual parcial. | E3 50% a 74%: etiquetado automático en los repositorios principales; DLP en correo y nube. | E4 75% a 89%: controles por etiqueta en todos los canales (incluida la IA) con monitoreo. | E5 90% o más: postura de datos continua; la protección acompaña al dato fuera de la organización.
- **Umbrales:** E2 ≥ 30% · E3 ≥ 50% · E4 ≥ 75% · E5 ≥ 90% (E3 = mínimo aceptable; E4 = meta por defecto)
- **Correspondencias:** NIST CSF 2.0 PR.DS · CIS v8.1 3 · ISO/IEC 27001:2022 5.12 (clasificación) y 8.24 (criptografía) · Otros: Leyes de protección de datos personales (ver Marco_Regulatorio)

#### K38 · Aplicaciones críticas con controles automatizados en el pipeline
- **Coordenadas:** T05 · PR04 Desarrollo seguro y gestión de cambios · D11 Application & Software Security (secundarios: D23) · Gestión · GM-24 M3.1 · KCI · Implementación · Adelantado
- **Qué mide:** Porcentaje de aplicaciones críticas (propias o personalizadas, incluidas las que integran modelos de IA) cuyo pipeline aplica de forma automática análisis de código, de dependencias, detección de secretos y lista de materiales de software (SBOM), con umbrales que bloquean.
- **Por qué importa:** Corregir en desarrollo cuesta una fracción de hacerlo en producción. Los controles en el pipeline escalan la seguridad sin frenar la entrega.
- **Fórmula:** Aplicaciones críticas con los cuatro controles activos y umbrales bloqueantes ÷ aplicaciones críticas × 100.
- **Unidad y polaridad:** % · Mayor es mejor · **Frecuencia:** Trimestral · **Audiencia:** CISO · CIO
- **Fuente de datos:** Plataforma CI/CD; herramientas SAST y SCA; inventario de aplicaciones. **Evidencia (ejemplo Microsoft):** GitHub Advanced Security (escaneo de código, secretos y dependencias) y seguridad de DevOps en Defender for Cloud.
- **Estadios:** E1 Menos de 30%: pruebas de seguridad manuales y tardías. | E2 30% a 49%: análisis en algunas aplicaciones, sin umbrales. | E3 50% a 74%: controles estándar en las aplicaciones críticas; los hallazgos críticos bloquean. | E4 75% a 89%: SBOM y firma de artefactos; métricas de deuda de seguridad por equipo. | E5 90% o más: corrección asistida por IA en la solicitud de cambios; controles específicos para modelos y prompts.
- **Umbrales:** E2 ≥ 30% · E3 ≥ 50% · E4 ≥ 75% · E5 ≥ 90% (E3 = mínimo aceptable; E4 = meta por defecto)
- **Correspondencias:** NIST CSF 2.0 PR.PS · CIS v8.1 16 · ISO/IEC 27001:2022 8.25–8.29 (desarrollo seguro) · Otros: NIST SSDF (SP 800-218); ISA/IEC 62443-4-1; Cyber Resilience Act (UE) 2024/2847

#### K39 · Cobertura del inventario de activos (TI, nube, OT e IoT)
- **Coordenadas:** T05 · ID01 Inventario y clasificación de activos · D13 Vulnerability & Exposure Management (secundarios: D18, D19) · Gestión · GM-24 M2.1 · KCI · Implementación · Adelantado
- **Qué mide:** Porcentaje de activos descubiertos por medios técnicos (red, nube, endpoints, OT, IoT) registrados en el inventario oficial con dueño, criticidad y estado de protección.
- **Por qué importa:** Los activos desconocidos no se parchean, no se monitorean y no se recuperan. La brecha entre lo descubierto y lo gestionado es exposición pura.
- **Fórmula:** Activos descubiertos que figuran en el inventario con dueño y criticidad ÷ activos descubiertos × 100.
- **Unidad y polaridad:** % · Mayor es mejor · **Frecuencia:** Mensual · **Audiencia:** CISO
- **Fuente de datos:** CMDB; descubrimiento de red, nube, EDR y monitoreo pasivo de OT. **Evidencia (ejemplo Microsoft):** Inventario de dispositivos de Defender for Endpoint, Microsoft Defender for IoT y Microsoft Security Exposure Management.
- **Estadios:** E1 Menos de 60%: inventarios dispersos y desactualizados. | E2 60% a 74%: CMDB central con conciliación manual. | E3 75% a 89%: descubrimiento automático en TI y nube con conciliación mensual. | E4 90% a 97%: inventario OT e IoT pasivo integrado; dueño y criticidad obligatorios. | E5 98% o más: inventario casi en tiempo real que incluye identidades, agentes y dependencias.
- **Umbrales:** E2 ≥ 60% · E3 ≥ 75% · E4 ≥ 90% · E5 ≥ 98% (E3 = mínimo aceptable; E4 = meta por defecto)
- **Correspondencias:** NIST CSF 2.0 ID.AM · CIS v8.1 1, 2 · ISO/IEC 27001:2022 5.9 (inventario de información y otros activos) · Otros: ISA/IEC 62443-2-1:2024; NERC CIP-002 (categorización); CIS Controls v8.1 (IG1)

#### K40 · Zonas OT e IIoT que alcanzan su nivel de seguridad objetivo
- **Coordenadas:** T05 · PR03 Hardening y arquitectura segura · D18 Operational Technology & Industrial Control Security (secundarios: D19, D08) · Gestión · GM-24 M3.1 · KCI · Efectividad · Rezagado
- **Qué mide:** Porcentaje de zonas OT e IIoT cuyo nivel de seguridad alcanzado (SL-A) iguala o supera el nivel objetivo (SL-T) definido en la evaluación de riesgos, según ISA/IEC 62443-3-2 y 3-3, incluidos los activos sin soporte con controles compensatorios.
- **Por qué importa:** En OT el objetivo no es «parchear todo» sino que cada zona tenga la protección que exige su consecuencia física. SL-T frente a SL-A es el lenguaje común entre ingeniería, seguridad y proveedores.
- **Fórmula:** Zonas con SL-A ≥ SL-T verificado ÷ zonas con SL-T definido × 100.
- **Unidad y polaridad:** % · Mayor es mejor · **Frecuencia:** Semestral · **Audiencia:** Directorio · Comité de riesgos · Operaciones
- **Fuente de datos:** Evaluaciones de riesgo OT (IEC 62443-3-2); inventario OT; auditorías a proveedores. **Evidencia (ejemplo Microsoft):** Microsoft Defender for IoT (inventario, vulnerabilidades y mapa de zonas OT).
- **Estadios:** E1 Menos de 20% o sin SL-T: OT sin evaluación de riesgos por zona. | E2 20% a 39%: zonas identificadas y SL-T definido en plantas piloto. | E3 40% a 69%: SL-T aprobado por ingeniería y seguridad en todas las plantas críticas. | E4 70% a 89%: brechas entre SL-T y SL-A con plan financiado; proveedores certificados (IEC 62443-4-1/4-2). | E5 90% o más: verificación continua de zonas; los cambios de ingeniería incluyen evaluación de seguridad.
- **Umbrales:** E2 ≥ 20% · E3 ≥ 40% · E4 ≥ 70% · E5 ≥ 90% (E3 = mínimo aceptable; E4 = meta por defecto)
- **Correspondencias:** NIST CSF 2.0 PR.PS · CIS v8.1 — · ISO/IEC 27001:2022 — · Otros: ISA/IEC 62443-3-2 y 3-3; ISA/IEC 62443-2-1:2024; C2M2 v2.1; API Std 1164

### T06 · SECURITY OPERATIONS

#### K41 · Cobertura de telemetría y protección de activos críticos
- **Coordenadas:** T06 · DE01 Telemetría y observabilidad · D14 Security Monitoring & Detection (secundarios: D09, D10, D18) · Gestión · GM-24 M4.1 · KCI · Implementación · Adelantado
- **Qué mide:** Porcentaje de activos críticos (identidades, endpoints, servidores, cargas en la nube, equipos de red y OT) que envían la telemetría requerida al SIEM/XDR y tienen un sensor de detección y respuesta activo.
- **Por qué importa:** Lo que no se observa no se detecta. Los atacantes eligen los puntos ciegos: activos sin sensor o con registros incompletos.
- **Fórmula:** Activos críticos con la telemetría requerida y sensor activo ÷ activos críticos del inventario × 100.
- **Unidad y polaridad:** % · Mayor es mejor · **Frecuencia:** Mensual · **Audiencia:** CISO
- **Fuente de datos:** SIEM/XDR; inventario; consola de EDR. **Evidencia (ejemplo Microsoft):** Dispositivos incorporados en Microsoft Defender XDR, conectores de datos de Microsoft Sentinel y Microsoft Defender for IoT.
- **Estadios:** E1 Menos de 60%: registros locales sin centralizar. | E2 60% a 74%: SIEM con las fuentes principales; brechas sin inventariar. | E3 75% a 89%: matriz de fuentes requeridas por tipo de activo; brechas gestionadas. | E4 90% a 97%: salud de las fuentes monitoreada y alertas por silencio de sensores. | E5 98% o más: telemetría unificada de TI, OT, nube e IA, con retención según el valor del dato.
- **Umbrales:** E2 ≥ 60% · E3 ≥ 75% · E4 ≥ 90% · E5 ≥ 98% (E3 = mínimo aceptable; E4 = meta por defecto)
- **Correspondencias:** NIST CSF 2.0 DE.CM · CIS v8.1 8, 13 · ISO/IEC 27001:2022 8.15 (registro) y 8.16 (actividades de monitoreo) · Otros: NERC CIP-007 (monitoreo de eventos); NERC CIP-015 (monitoreo interno de red, exigible desde oct-2028)

#### K42 · Tiempo medio de detección (MTTD)
- **Coordenadas:** T06 · DE02 Ingeniería de detección y análisis · D14 Security Monitoring & Detection (secundarios: D21) · Gestión · GM-24 M4.1 · KPI · Efectividad · Rezagado
- **Qué mide:** Tiempo entre el inicio de la actividad maliciosa —o su primer indicio en la telemetría— y la detección confirmada del incidente (se informa la mediana).
- **Por qué importa:** Cada hora sin detectar es tiempo del atacante para escalar privilegios, moverse y exfiltrar. Es el indicador clásico de eficacia del SOC.
- **Fórmula:** Mediana de horas (primer indicio → detección confirmada) en los incidentes confirmados del período.
- **Unidad y polaridad:** horas · Menor es mejor · **Frecuencia:** Mensual · **Audiencia:** Directorio · CISO · Comité de riesgos
- **Fuente de datos:** SIEM/XDR; informes de incidentes. **Evidencia (ejemplo Microsoft):** Tiempos de incidentes en Microsoft Sentinel y Microsoft Defender XDR; libro de eficiencia de operaciones de seguridad de Sentinel.
- **Estadios:** E1 Más de 72 h o sin medición: los incidentes los descubren terceros. | E2 25 a 72 h: detección por firmas y revisión en horario laboral. | E3 9 a 24 h: SOC con cobertura extendida y casos de uso priorizados. | E4 2 a 8 h: correlación XDR, analítica de comportamiento y operación 24×7. | E5 1 h o menos: detección y triaje asistidos por IA con validación humana; disrupción automática.
- **Umbrales:** E2 ≤ 72 h · E3 ≤ 24 h · E4 ≤ 8 h · E5 ≤ 1 h (E3 = mínimo aceptable; E4 = meta por defecto)
- **Correspondencias:** NIST CSF 2.0 DE.AE · CIS v8.1 13 · ISO/IEC 27001:2022 8.16 (actividades de monitoreo) · Otros: —

#### K43 · Técnicas de ataque priorizadas con detección validada
- **Coordenadas:** T06 · DE04 Evaluación de cobertura y calidad de detección · D12 Threat Intelligence & Threat Modeling (secundarios: D14) · Gestión · GM-24 M4.1 · KPI · Efectividad · Adelantado
- **Qué mide:** Porcentaje de las técnicas de ataque priorizadas por inteligencia de amenazas del sector (MITRE ATT&CK Enterprise e ICS) con al menos una detección validada mediante emulación o prueba en los últimos 12 meses.
- **Por qué importa:** Contar reglas no dice nada; probar que se detectan las técnicas que usarían los adversarios del sector sí. Orienta la ingeniería de detección hacia el riesgo real.
- **Fórmula:** Técnicas priorizadas con detección validada en 12 meses ÷ técnicas priorizadas × 100.
- **Unidad y polaridad:** % · Mayor es mejor · **Frecuencia:** Semestral · **Audiencia:** CISO
- **Fuente de datos:** Matriz de cobertura ATT&CK; resultados de emulación o de ejercicios purple team. **Evidencia (ejemplo Microsoft):** Cobertura MITRE ATT&CK en Microsoft Sentinel y simulaciones en Microsoft Defender XDR.
- **Estadios:** E1 Menos de 30% o sin priorización: la cobertura se mide por cantidad de reglas. | E2 30% a 49%: técnicas mapeadas en papel, sin validación. | E3 50% a 69%: perfil de amenazas del sector y validación anual por emulación. | E4 70% a 84%: purple team trimestral; las brechas se convierten en detecciones. | E5 85% o más: validación continua y automatizada, incluidas las técnicas contra IA y agentes.
- **Umbrales:** E2 ≥ 30% · E3 ≥ 50% · E4 ≥ 70% · E5 ≥ 85% (E3 = mínimo aceptable; E4 = meta por defecto)
- **Correspondencias:** NIST CSF 2.0 DE.AE · CIS v8.1 18 · ISO/IEC 27001:2022 8.16 (actividades de monitoreo) · Otros: MITRE ATT&CK v20 (Enterprise e ICS)

#### K44 · Campañas de hunting que mejoran la detección
- **Coordenadas:** T06 · DE03 Hunting, validación y mejora de detecciones · D14 Security Monitoring & Detection (secundarios: D12, D23) · Gestión · GM-24 M4.1 · KPI · Eficiencia · Adelantado
- **Qué mide:** Porcentaje de las campañas de hunting por hipótesis que terminan en una detección nueva o mejorada puesta en producción o en una brecha de visibilidad corregida.
- **Por qué importa:** El hunting que no se convierte en detección es un costo; el que sí, eleva la línea base del SOC. Mide el ciclo de aprendizaje de la operación.
- **Fórmula:** Campañas con detección nueva o mejorada o con brecha corregida ÷ campañas de hunting realizadas × 100.
- **Unidad y polaridad:** % · Mayor es mejor · **Frecuencia:** Trimestral · **Audiencia:** CISO · SOC
- **Fuente de datos:** Registro de campañas de hunting; repositorio de detecciones. **Evidencia (ejemplo Microsoft):** Búsqueda avanzada en Microsoft Defender XDR y Microsoft Sentinel; hipótesis asistidas por Microsoft Security Copilot con validación humana.
- **Estadios:** E1 Menos de 20% o sin hunting: el SOC solo reacciona a alertas. | E2 20% a 34%: hunting ocasional después de incidentes publicitados. | E3 35% a 49%: programa trimestral con hipótesis basadas en inteligencia. | E4 50% a 69%: detecciones como código con pruebas; métricas por analista. | E5 70% o más: hunting continuo asistido por IA y ciclo detección-validación automatizado.
- **Umbrales:** E2 ≥ 20% · E3 ≥ 35% · E4 ≥ 50% · E5 ≥ 70% (E3 = mínimo aceptable; E4 = meta por defecto)
- **Correspondencias:** NIST CSF 2.0 DE.AE · CIS v8.1 13 · ISO/IEC 27001:2022 8.16 (actividades de monitoreo) · Otros: —

#### K45 · Tiempo medio de contención (MTTC)
- **Coordenadas:** T06 · RS02 Contención, erradicación y preservación de evidencia · D15 Incident Response & Crisis Management (secundarios: D14, D21) · Gestión · GM-24 M5.2 · KPI · Efectividad · Rezagado
- **Qué mide:** Tiempo entre la detección confirmada de un incidente y su contención efectiva (aislamiento del activo, revocación de credenciales, bloqueo del vector); se informa la mediana.
- **Por qué importa:** Detectar rápido sirve si se contiene rápido. La contención define el alcance del daño, el costo y la obligación de notificar.
- **Fórmula:** Mediana de horas (detección confirmada → contención) en los incidentes del período.
- **Unidad y polaridad:** horas · Menor es mejor · **Frecuencia:** Mensual · **Audiencia:** Directorio · CISO · Comité de riesgos
- **Fuente de datos:** SIEM, SOAR y XDR; informes de incidentes. **Evidencia (ejemplo Microsoft):** Acciones de respuesta e interrupción automática de ataques de Microsoft Defender XDR; automatización de Microsoft Sentinel.
- **Estadios:** E1 Más de 48 h: contención manual y con aprobaciones lentas. | E2 13 a 48 h: procedimientos manuales documentados. | E3 5 a 12 h: acciones de contención preaprobadas por tipo de incidente. | E4 2 a 4 h: contención automatizada para los escenarios comunes. | E5 1 h o menos: disrupción automática de ataques y agentes de respuesta con supervisión humana.
- **Umbrales:** E2 ≤ 48 h · E3 ≤ 12 h · E4 ≤ 4 h · E5 ≤ 1 h (E3 = mínimo aceptable; E4 = meta por defecto)
- **Correspondencias:** NIST CSF 2.0 RS.MI · CIS v8.1 17 · ISO/IEC 27001:2022 5.26 (respuesta a incidentes) · Otros: —

#### K46 · Vulnerabilidades explotadas y exposiciones críticas remediadas en plazo
- **Coordenadas:** T06 · ID03 Amenazas, vulnerabilidades y exposición · D13 Vulnerability & Exposure Management (secundarios: D12) · Gestión · GM-24 M4.2 · KCI · Efectividad · Rezagado
- **Qué mide:** Porcentaje de vulnerabilidades con explotación conocida (catálogo KEV u otra fuente de inteligencia) y de exposiciones críticas en activos expuestos a internet que se remedian o mitigan dentro del plazo de la política.
- **Por qué importa:** Los atacantes priorizan lo que ya saben explotar. Cerrar primero lo explotado reduce más riesgo que perseguir el volumen total de vulnerabilidades.
- **Fórmula:** Vulnerabilidades explotadas o exposiciones críticas remediadas o mitigadas en plazo ÷ las que vencieron en el período × 100.
- **Unidad y polaridad:** % · Mayor es mejor · **Frecuencia:** Mensual · **Audiencia:** Directorio · CISO · Comité de riesgos
- **Fuente de datos:** Gestión de vulnerabilidades; catálogo KEV; superficie de ataque externa. **Evidencia (ejemplo Microsoft):** Microsoft Defender Vulnerability Management, Defender External Attack Surface Management y Microsoft Security Exposure Management.
- **Estadios:** E1 Menos de 50%: parches por calendario, sin priorizar por explotación. | E2 50% a 69%: KEV monitoreado, con plazos no diferenciados. | E3 70% a 84%: plazos por explotación y exposición (p. ej., 14 días o menos en activos expuestos). | E4 85% a 94%: mitigación compensatoria inmediata cuando no se puede parchear (OT, sistemas heredados). | E5 95% o más: priorización por rutas de ataque y activos críticos; remediación orquestada con IA.
- **Umbrales:** E2 ≥ 50% · E3 ≥ 70% · E4 ≥ 85% · E5 ≥ 95% (E3 = mínimo aceptable; E4 = meta por defecto)
- **Correspondencias:** NIST CSF 2.0 ID.RA · CIS v8.1 7 · ISO/IEC 27001:2022 8.8 (gestión de vulnerabilidades técnicas) · Otros: CISA BOD 26-04 (reemplazó a la BOD 22-01 en junio de 2026) y catálogo KEV; PCI DSS v4.0.1 (req. 6.3)

#### K47 · Tiempo de restauración de servicios críticos frente al RTO
- **Coordenadas:** T06 · RC01 Restauración y recuperación técnica · D16 Business Continuity & Cyber Recovery (secundarios: D15) · Gestión · GM-24 M6.1 · KPI · Impacto · Rezagado
- **Qué mide:** Tiempo real entre la contención de un incidente que afectó un servicio crítico y su restauración verificada, expresado como porcentaje del RTO aprobado.
- **Por qué importa:** Es lo que experimentan el cliente, el ciudadano o el operador del sistema. Mide la resiliencia en condiciones reales, no de laboratorio.
- **Fórmula:** Mediana de (horas de restauración real ÷ RTO aprobado) × 100 en los incidentes del período que afectaron servicios críticos.
- **Unidad y polaridad:** % del RTO · Menor es mejor · **Frecuencia:** Por evento · trimestral · **Audiencia:** Directorio · Comité de riesgos
- **Fuente de datos:** Informes de incidentes; registros de gestión de servicios. **Evidencia (ejemplo Microsoft):** Línea de tiempo de incidentes en Microsoft Sentinel y estado de recuperación en Azure Site Recovery.
- **Estadios:** E1 Más de 200% del RTO o sin medición. | E2 151% a 200%: restauración improvisada; las prioridades se discuten durante la crisis. | E3 101% a 150%: secuencia de restauración por criticidad documentada. | E4 76% a 100%: restauración dentro del RTO en entorno limpio y con validación de integridad. | E5 75% o menos: restauración orquestada y verificada automáticamente, con holgura frente al RTO.
- **Umbrales:** E2 ≤ 200% · E3 ≤ 150% · E4 ≤ 100% · E5 ≤ 75% (E3 = mínimo aceptable; E4 = meta por defecto)
- **Correspondencias:** NIST CSF 2.0 RC.RP · CIS v8.1 11 · ISO/IEC 27001:2022 5.30 (preparación de las TIC para la continuidad) · Otros: DORA art. 11

#### K48 · Acciones correctivas post-incidente cerradas en plazo
- **Coordenadas:** T06 · RC04 Aprendizaje, corrección y mejora continua · D15 Incident Response & Crisis Management (secundarios: D16) · Gestión · GM-24 M5.2 · KCI · Efectividad · Rezagado
- **Qué mide:** Porcentaje de acciones correctivas derivadas de incidentes y ejercicios cerradas en el plazo comprometido y con verificación de eficacia; se complementa con la tasa de incidentes recurrentes por la misma causa raíz.
- **Por qué importa:** Un incidente que se repite por la misma causa es una lección no aprendida. Cerrar acciones con verificación es la forma operativa de evolucionar en la mitigación del riesgo.
- **Fórmula:** Acciones correctivas cerradas en plazo y verificadas ÷ acciones correctivas con vencimiento en el período × 100.
- **Unidad y polaridad:** % · Mayor es mejor · **Frecuencia:** Trimestral · **Audiencia:** CISO · Comité de riesgos
- **Fuente de datos:** Registro de acciones correctivas; gestión de servicios; informes post-incidente. **Evidencia (ejemplo Microsoft):** Tareas en Planner o Azure DevOps vinculadas a los incidentes de Microsoft Sentinel.
- **Estadios:** E1 Menos de 50%: acciones sin dueño ni plazo; incidentes recurrentes frecuentes. | E2 50% a 69%: registro de acciones con seguimiento irregular. | E3 70% a 84%: acciones con dueño y plazo; seguimiento mensual. | E4 85% a 94%: verificación de eficacia y análisis de recurrencia por causa raíz. | E5 95% o más: correcciones sistémicas priorizadas con datos; recurrencia cercana a cero.
- **Umbrales:** E2 ≥ 50% · E3 ≥ 70% · E4 ≥ 85% · E5 ≥ 95% (E3 = mínimo aceptable; E4 = meta por defecto)
- **Correspondencias:** NIST CSF 2.0 ID.IM · CIS v8.1 17 · ISO/IEC 27001:2022 10.2 (no conformidad y acción correctiva) · Otros: NIST SP 800-61r3

### T07 · AI & AUTONOMOUS SYSTEMS

#### K49 · Inventario de sistemas de IA y agentes
- **Coordenadas:** T07 · ID01 Inventario y clasificación de activos · D20 AI & Agent Security (secundarios: D06) · Gestión · GM-24 M6.2 · KCI · Implementación · Adelantado
- **Qué mide:** Porcentaje de los sistemas de IA en uso —modelos, aplicaciones de IA generativa, copilotos y agentes, incluidos los creados por usuarios y los de terceros— descubiertos por medios técnicos que están registrados con dueño, propósito, datos que usan y nivel de riesgo.
- **Por qué importa:** En una empresa de frontera los agentes se multiplican más rápido que los procesos de aprobación. Sin inventario no hay gobierno, ni respuesta, ni rendición de cuentas.
- **Fórmula:** Sistemas de IA y agentes registrados con dueño, propósito y riesgo ÷ sistemas de IA y agentes descubiertos × 100.
- **Unidad y polaridad:** % · Mayor es mejor · **Frecuencia:** Mensual · **Audiencia:** Directorio · CISO · Comité de IA
- **Fuente de datos:** Registro de IA; descubrimiento de aplicaciones de IA; plataformas de agentes. **Evidencia (ejemplo Microsoft):** Registro de agentes en Microsoft Agent 365 y Microsoft Entra Agent ID; aplicaciones de IA generativa en Defender for Cloud Apps; DSPM para IA de Microsoft Purview.
- **Estadios:** E1 Menos de 30%: uso de IA sin registro; la IA en la sombra no se mide. | E2 30% a 49%: registro manual de los casos de uso aprobados. | E3 50% a 74%: descubrimiento técnico de aplicaciones de IA y conciliación mensual. | E4 75% a 94%: registro obligatorio de agentes con identidad, dueño y clasificación de riesgo. | E5 95% o más: inventario vivo de modelos, agentes, herramientas y conectores, con linaje de datos.
- **Umbrales:** E2 ≥ 30% · E3 ≥ 50% · E4 ≥ 75% · E5 ≥ 95% (E3 = mínimo aceptable; E4 = meta por defecto)
- **Correspondencias:** NIST CSF 2.0 ID.AM · CIS v8.1 1, 2 · ISO/IEC 27001:2022 5.9 (inventario de información y otros activos) · Otros: ISO/IEC 42001:2023; NIST AI RMF (MAP); Reglamento (UE) 2024/1689

#### K50 · Agentes con dueño humano y autoridad delegada acotada
- **Coordenadas:** T07 · GV02 Estructura de gobierno y autoridad · D20 AI & Agent Security (secundarios: D05) · Gobierno · GM-24 M2.2 · KCI · Implementación · Adelantado
- **Qué mide:** Porcentaje de agentes de IA en producción que cumplen el estándar de autoridad delegada: identidad propia, dueño humano responsable, permisos mínimos sobre herramientas y datos, límites de acción definidos y aprobación humana para acciones de alto impacto.
- **Por qué importa:** Un agente es autoridad no humana en ejecución. Si no está claro quién responde por él ni hasta dónde puede actuar, la organización delegó poder sin gobierno.
- **Fórmula:** Agentes en producción que cumplen los cinco requisitos ÷ agentes en producción × 100; se informa además la relación de agentes por dueño humano.
- **Unidad y polaridad:** % · Mayor es mejor · **Frecuencia:** Mensual · **Audiencia:** Directorio · Comité de IA
- **Fuente de datos:** Registro de agentes; proveedor de identidad; políticas de acceso a herramientas y datos. **Evidencia (ejemplo Microsoft):** Microsoft Entra Agent ID y Acceso condicional para agentes; Microsoft Agent 365; controles de administración de Copilot Studio.
- **Estadios:** E1 Menos de 30%: agentes con cuentas compartidas o con los permisos de quien los creó; sin dueño. | E2 30% a 49%: dueños nominados, con permisos amplios heredados. | E3 50% a 74%: identidad propia y permisos mínimos en los agentes críticos; aprobación humana definida. | E4 75% a 94%: límites de acción, presupuestos y revisiones periódicas; relación agentes por dueño controlada. | E5 95% o más: autoridad delegada como política verificable en ejecución y revocación inmediata.
- **Umbrales:** E2 ≥ 30% · E3 ≥ 50% · E4 ≥ 75% · E5 ≥ 95% (E3 = mínimo aceptable; E4 = meta por defecto)
- **Correspondencias:** NIST CSF 2.0 GV.RR · CIS v8.1 5, 6 · ISO/IEC 27001:2022 5.15–5.18 (control de acceso e identidades) · Otros: Reglamento (UE) 2024/1689 art. 14 (supervisión humana); ISO/IEC 42001:2023; NIST AI RMF (GOVERN)

#### K51 · Casos de uso de IA con evaluación de riesgo e impacto previa
- **Coordenadas:** T07 · GV03 Políticas y estándares · D20 AI & Agent Security (secundarios: D03, D07) · Gobierno · GM-24 G2.2 · KCI · Implementación · Adelantado
- **Qué mide:** Porcentaje de casos de uso de IA puestos en producción en el período que contaron, antes del despliegue, con una evaluación de riesgo e impacto (seguridad, privacidad, sesgo, regulación aplicable) aprobada conforme a la política de IA.
- **Por qué importa:** La política de IA vale lo que vale su aplicación antes del despliegue. Evaluar después convierte la gobernanza en arqueología.
- **Fórmula:** Casos de uso desplegados con evaluación previa aprobada ÷ casos de uso desplegados × 100.
- **Unidad y polaridad:** % · Mayor es mejor · **Frecuencia:** Trimestral · **Audiencia:** Directorio · Comité de IA · Comité de riesgos
- **Fuente de datos:** Registro de casos de uso de IA; actas del comité de IA; evaluaciones de impacto. **Evidencia (ejemplo Microsoft):** Evaluaciones con plantillas de regulación de IA en Microsoft Purview Compliance Manager; documentación del sistema en Microsoft Foundry.
- **Estadios:** E1 Menos de 40%: no hay política de IA o no se aplica antes del despliegue. | E2 40% a 59%: evaluaciones informales para los casos visibles. | E3 60% a 79%: evaluación estándar obligatoria con aprobación del comité de IA. | E4 80% a 94%: evaluación proporcional al riesgo, con pruebas adversariales en los casos de alto riesgo. | E5 95% o más: evaluación continua en producción (deriva, abuso, cambios de modelo) con reevaluación automática.
- **Umbrales:** E2 ≥ 40% · E3 ≥ 60% · E4 ≥ 80% · E5 ≥ 95% (E3 = mínimo aceptable; E4 = meta por defecto)
- **Correspondencias:** NIST CSF 2.0 GV.PO · CIS v8.1 — · ISO/IEC 27001:2022 5.8 (seguridad en la gestión de proyectos) · Otros: ISO/IEC 42001:2023; NIST AI 600-1; Reglamento (UE) 2024/1689, modificado por el Reglamento (UE) 2026/1744 (art. 9 y 27)

#### K52 · Interacciones con IA protegidas contra la fuga de datos
- **Coordenadas:** T07 · PR02 Protección de datos y privacidad por diseño · D20 AI & Agent Security (secundarios: D06) · Gestión · GM-24 M2.1 · KCI · Efectividad · Adelantado
- **Qué mide:** Porcentaje de las interacciones con aplicaciones de IA (sancionadas y descubiertas) cubiertas por controles de prevención de fuga de datos y de acceso por etiqueta que impiden enviar información sensible a servicios no autorizados.
- **Por qué importa:** La IA generativa es un nuevo canal de exfiltración involuntaria. Proteger el prompt y la respuesta es tan necesario como proteger el correo.
- **Fórmula:** Interacciones con IA bajo controles de DLP y de etiquetas ÷ interacciones con IA observadas × 100 (alternativa: usuarios activos de IA cubiertos ÷ usuarios activos de IA).
- **Unidad y polaridad:** % · Mayor es mejor · **Frecuencia:** Mensual · **Audiencia:** CISO · Privacidad
- **Fuente de datos:** DLP; CASB/SSE; telemetría de uso de IA. **Evidencia (ejemplo Microsoft):** DSPM para IA de Microsoft Purview, DLP para Microsoft 365 Copilot y para navegadores, y Microsoft Defender for Cloud Apps.
- **Estadios:** E1 Menos de 30%: uso de IA sin visibilidad; se bloquea o se permite todo. | E2 30% a 49%: bloqueo de algunas aplicaciones, sin control del contenido. | E3 50% a 74%: DLP en la IA sancionada y en los navegadores administrados. | E4 75% a 94%: controles por etiqueta en IA sancionada y de terceros; alertas de riesgo interno. | E5 95% o más: protección del dato que acompaña al agente (herencia de etiquetas y límites de contexto).
- **Umbrales:** E2 ≥ 30% · E3 ≥ 50% · E4 ≥ 75% · E5 ≥ 95% (E3 = mínimo aceptable; E4 = meta por defecto)
- **Correspondencias:** NIST CSF 2.0 PR.DS · CIS v8.1 3 · ISO/IEC 27001:2022 8.12 (prevención de fuga de datos) · Otros: OWASP Top 10 para aplicaciones LLM (2025); leyes de datos personales

#### K53 · Observabilidad de agentes integrada a la detección
- **Coordenadas:** T07 · DE01 Telemetría y observabilidad · D20 AI & Agent Security (secundarios: D14) · Gestión · GM-24 M4.1 · KCI · Implementación · Adelantado
- **Qué mide:** Porcentaje de agentes de IA en producción cuya actividad —invocaciones, herramientas usadas, datos accedidos y acciones ejecutadas— se registra y llega al SIEM/XDR con detecciones específicas (inyección de prompts, abuso de herramientas, exfiltración).
- **Por qué importa:** Un agente comprometido actúa con credenciales legítimas. Sin su rastro en el SOC, el incidente es invisible hasta que el daño es evidente.
- **Fórmula:** Agentes en producción con registro completo y detecciones activas ÷ agentes en producción × 100.
- **Unidad y polaridad:** % · Mayor es mejor · **Frecuencia:** Mensual · **Audiencia:** CISO · SOC
- **Fuente de datos:** Registros de las plataformas de agentes y de modelos; SIEM/XDR. **Evidencia (ejemplo Microsoft):** Protección contra amenazas para IA en Defender for Cloud, auditoría de Microsoft Purview para interacciones de Copilot y agentes, y Microsoft Sentinel.
- **Estadios:** E1 Menos de 20%: los agentes no generan registros utilizables. | E2 20% a 39%: registros locales de la plataforma, sin integración. | E3 40% a 69%: registros centralizados y detecciones básicas de abuso. | E4 70% a 89%: detecciones específicas de IA (MITRE ATLAS) correlacionadas con identidad y datos. | E5 90% o más: trazabilidad completa de cadenas de agentes y respuesta automatizada ante desvíos.
- **Umbrales:** E2 ≥ 20% · E3 ≥ 40% · E4 ≥ 70% · E5 ≥ 90% (E3 = mínimo aceptable; E4 = meta por defecto)
- **Correspondencias:** NIST CSF 2.0 DE.CM · CIS v8.1 8 · ISO/IEC 27001:2022 8.15 (registro) y 8.16 (actividades de monitoreo) · Otros: MITRE ATLAS; OWASP Top 10 para aplicaciones LLM (2025)

#### K54 · Hallazgos críticos de red teaming de IA corregidos
- **Coordenadas:** T07 · ID03 Amenazas, vulnerabilidades y exposición · D20 AI & Agent Security (secundarios: D22) · Gestión · GM-24 M4.2 · KCI · Efectividad · Adelantado
- **Qué mide:** Porcentaje de hallazgos críticos y altos de pruebas adversariales sobre sistemas de IA (inyección de prompts directa e indirecta, jailbreak, fuga de datos, abuso de herramientas) corregidos o mitigados en plazo, antes de la puesta en producción o de la versión siguiente.
- **Por qué importa:** Los modelos y agentes tienen una superficie de ataque propia que la prueba de penetración tradicional no cubre. Corregir lo encontrado convierte la prueba en reducción de riesgo.
- **Fórmula:** Hallazgos críticos o altos de red teaming de IA corregidos en plazo ÷ hallazgos críticos o altos con vencimiento × 100.
- **Unidad y polaridad:** % · Mayor es mejor · **Frecuencia:** Trimestral · **Audiencia:** CISO · Comité de IA
- **Fuente de datos:** Informes de red teaming de IA; backlog de corrección. **Evidencia (ejemplo Microsoft):** Agente de red teaming de IA de Microsoft Foundry (basado en PyRIT) y Prompt Shields de Azure AI Content Safety.
- **Estadios:** E1 Menos de 40% o sin pruebas: los sistemas de IA se lanzan sin pruebas adversariales. | E2 40% a 59%: pruebas puntuales en los casos visibles. | E3 60% a 79%: red teaming obligatorio en los casos de alto riesgo, con plazos de corrección. | E4 80% a 94%: pruebas automatizadas en el pipeline de IA y repetición tras cambios de modelo. | E5 95% o más: red teaming continuo (humano y automatizado) que incluye cadenas de agentes y herramientas.
- **Umbrales:** E2 ≥ 40% · E3 ≥ 60% · E4 ≥ 80% · E5 ≥ 95% (E3 = mínimo aceptable; E4 = meta por defecto)
- **Correspondencias:** NIST CSF 2.0 ID.RA · CIS v8.1 18 · ISO/IEC 27001:2022 8.29 (pruebas de seguridad en desarrollo y aceptación) · Otros: NIST AI 600-1; MITRE ATLAS; OWASP Top 10 para aplicaciones LLM (2025)

#### K55 · Incidentes contenidos con respuesta automatizada o asistida por IA
- **Coordenadas:** T07 · RS02 Contención, erradicación y preservación de evidencia · D21 AI for Cyber Defense & Security Operations (secundarios: D23) · Gestión · GM-24 M5.2 · KPI · Eficiencia · Rezagado
- **Qué mide:** Porcentaje de incidentes elegibles —de tipos con libreto aprobado— cuya contención se ejecutó de forma automatizada o por agentes de seguridad, con supervisión humana y sin reversiones por error.
- **Por qué importa:** La escala y la velocidad de los ataques asistidos por IA superan la capacidad humana. La automatización gobernada libera al analista para el juicio, no para el clic.
- **Fórmula:** Incidentes elegibles contenidos de forma automatizada o por agentes, sin reversión por error ÷ incidentes elegibles × 100.
- **Unidad y polaridad:** % · Mayor es mejor · **Frecuencia:** Mensual · **Audiencia:** CISO
- **Fuente de datos:** SOAR/XDR; registros de los agentes de seguridad. **Evidencia (ejemplo Microsoft):** Interrupción automática de ataques de Microsoft Defender XDR, agentes de Microsoft Security Copilot (p. ej., triaje de phishing) y automatización de Microsoft Sentinel.
- **Estadios:** E1 Menos de 20%: respuesta íntegramente manual. | E2 20% a 39%: automatizaciones aisladas (bloqueos, aislamiento). | E3 40% a 59%: libretos automatizados con aprobación humana para los escenarios comunes. | E4 60% a 79%: agentes de triaje y contención con supervisión y métricas de precisión. | E5 80% o más: respuesta autónoma gobernada, con límites de autoridad y revisión humana por muestreo.
- **Umbrales:** E2 ≥ 20% · E3 ≥ 40% · E4 ≥ 60% · E5 ≥ 80% (E3 = mínimo aceptable; E4 = meta por defecto)
- **Correspondencias:** NIST CSF 2.0 RS.MI · CIS v8.1 17 · ISO/IEC 27001:2022 5.26 (respuesta a incidentes) · Otros: NIST AI RMF (MANAGE)

#### K56 · Procesos críticos con IA capaces de operar sin ella
- **Coordenadas:** T07 · RC02 Continuidad y operación degradada · D20 AI & Agent Security (secundarios: D16) · Gestión · GM-24 M6.1 · KCI · Efectividad · Adelantado
- **Qué mide:** Porcentaje de procesos críticos que dependen de modelos o agentes de IA con mecanismo de desactivación probado y con un modo de operación sin IA documentado y ensayado en los últimos 12 meses.
- **Por qué importa:** Cuando un agente falla, es manipulado o el proveedor de IA cae, el proceso debe seguir. La resiliencia de frontera exige poder apagar la autonomía sin apagar el negocio.
- **Fórmula:** Procesos críticos dependientes de IA con desactivación y operación sin IA probadas ÷ procesos críticos dependientes de IA × 100.
- **Unidad y polaridad:** % · Mayor es mejor · **Frecuencia:** Semestral · **Audiencia:** Directorio · Comité de riesgos · Comité de IA
- **Fuente de datos:** BIA; registro de IA; informes de prueba. **Evidencia (ejemplo Microsoft):** Bloqueo y revocación de agentes con Microsoft Entra Agent ID y Microsoft Agent 365.
- **Estadios:** E1 Menos de 25%: dependencia de IA sin alternativa; nadie sabe apagar los agentes. | E2 25% a 49%: la desactivación es posible pero no se probó. | E3 50% a 74%: desactivación probada y procedimiento manual documentado. | E4 75% a 94%: ensayos anuales de operación sin IA con medición de la capacidad residual. | E5 95% o más: degradación controlada automática (de autónomo a asistido y a manual) ante señales de riesgo.
- **Umbrales:** E2 ≥ 25% · E3 ≥ 50% · E4 ≥ 75% · E5 ≥ 95% (E3 = mínimo aceptable; E4 = meta por defecto)
- **Correspondencias:** NIST CSF 2.0 RC.RP · CIS v8.1 — · ISO/IEC 27001:2022 5.29 (seguridad de la información durante la disrupción) · Otros: Reglamento (UE) 2024/1689 art. 14 (capacidad de interrumpir el sistema); NIST AI RMF (MANAGE)

### T08 · TRUST & ASSURANCE

#### K57 · Obligaciones aplicables mapeadas a controles con evidencia vigente
- **Coordenadas:** T08 · GV06 Obligaciones legales y contractuales · D03 Compliance & Regulatory Security (secundarios: D07) · Gobierno · GM-24 G3.2 · KCI · Implementación · Adelantado
- **Qué mide:** Porcentaje de las obligaciones legales, regulatorias y contractuales de ciberseguridad y datos identificadas que están mapeadas a controles con dueño y con evidencia de operación vigente.
- **Por qué importa:** Sin un inventario de obligaciones vinculado a controles y evidencias, cada auditoría o inspección se vuelve un proyecto de emergencia y el cumplimiento depende de la memoria.
- **Fórmula:** Obligaciones con controles asignados y evidencia vigente ÷ obligaciones aplicables identificadas × 100.
- **Unidad y polaridad:** % · Mayor es mejor · **Frecuencia:** Trimestral · **Audiencia:** Directorio · Comité de riesgos · Cumplimiento
- **Fuente de datos:** Registro de obligaciones (GRC); evidencias de control. **Evidencia (ejemplo Microsoft):** Microsoft Purview Compliance Manager (evaluaciones por regulación y puntuación de cumplimiento).
- **Estadios:** E1 Menos de 50%: obligaciones conocidas solo por áreas aisladas; sin registro. | E2 50% a 69%: inventario de obligaciones con mapeo parcial a controles. | E3 70% a 84%: obligaciones mapeadas con dueño; evidencia reunida para las auditorías. | E4 85% a 94%: evidencia periódica automatizada en controles clave y monitoreo de cambios regulatorios. | E5 95% o más: cumplimiento continuo: evidencia casi en tiempo real y análisis de impacto regulatorio asistido por IA.
- **Umbrales:** E2 ≥ 50% · E3 ≥ 70% · E4 ≥ 85% · E5 ≥ 95% (E3 = mínimo aceptable; E4 = meta por defecto)
- **Correspondencias:** NIST CSF 2.0 GV.OC · CIS v8.1 — · ISO/IEC 27001:2022 5.31 (requisitos legales, regulatorios y contractuales) · Otros: Regulación sectorial (ver Marco_Regulatorio)

#### K58 · Calidad del reporte de ciberriesgo al Directorio
- **Coordenadas:** T08 · GV07 Supervisión y reporting ejecutivo · D01 Cybersecurity Governance (secundarios: D02) · Gobierno · GM-24 G6.1 · KPI · Efectividad · Adelantado
- **Qué mide:** Cumplimiento de una lista de 10 criterios en los reportes al Directorio: tendencias, comparación con apetito y tolerancias, KRI adelantados, escenarios cuantificados, estado de terceros e IA, decisiones requeridas, incertidumbre declarada, evidencia trazable, lenguaje de negocio y seguimiento de pedidos previos.
- **Por qué importa:** El Directorio gobierna con lo que recibe. Un reporte de actividad («bloqueamos un millón de ataques») no permite decidir; uno orientado a riesgo y decisiones sí.
- **Fórmula:** Criterios cumplidos ÷ 10 × 100, promedio de los reportes del período (evaluado por auditoría interna o por la secretaría del Directorio).
- **Unidad y polaridad:** % · Mayor es mejor · **Frecuencia:** Trimestral · **Audiencia:** Directorio
- **Fuente de datos:** Reportes al Directorio; evaluación de auditoría interna. **Evidencia (ejemplo Microsoft):** Tablero ejecutivo en Power BI con datos de Microsoft Sentinel, Defender XDR, Microsoft Purview y Security Exposure Management.
- **Estadios:** E1 Menos de 30%: reportes de actividad técnica sin vínculo con el apetito. | E2 30% a 49%: semáforos cualitativos y métricas operativas. | E3 50% a 69%: KPI y KRI con tendencia y vínculo con el apetito; decisiones requeridas explícitas. | E4 70% a 89%: escenarios cuantificados, incertidumbre declarada y evidencia trazable. | E5 90% o más: tablero vivo con narrativa y simulaciones; el Directorio evalúa la utilidad del reporte.
- **Umbrales:** E2 ≥ 30% · E3 ≥ 50% · E4 ≥ 70% · E5 ≥ 90% (E3 = mínimo aceptable; E4 = meta por defecto)
- **Correspondencias:** NIST CSF 2.0 GV.OV · CIS v8.1 — · ISO/IEC 27001:2022 9.3 (revisión por la dirección) · Otros: SEC Regulation S-K Item 106; NIS2 art. 20; ISO/IEC 27004 (en revisión); métricas orientadas a resultados (Gartner, 2024)

#### K59 · Hallazgos de auditoría y de reguladores cerrados en plazo
- **Coordenadas:** T08 · GV08 Assurance y revisión independiente · D03 Compliance & Regulatory Security (secundarios: D01) · Gobierno · GM-24 G3.2 · KRI · Efectividad · Rezagado
- **Qué mide:** Porcentaje de hallazgos de ciberseguridad emitidos por auditoría interna, auditores externos y reguladores que se cerraron en el plazo comprometido, con validación del emisor.
- **Por qué importa:** Los hallazgos vencidos son riesgos reconocidos que siguen abiertos y erosionan la confianza del regulador y del Directorio en la función.
- **Fórmula:** Hallazgos cerrados en plazo y validados ÷ hallazgos con vencimiento en el período × 100.
- **Unidad y polaridad:** % · Mayor es mejor · **Frecuencia:** Trimestral · **Audiencia:** Directorio · Comité de auditoría
- **Fuente de datos:** Seguimiento de auditoría en el GRC. **Evidencia (ejemplo Microsoft):** Acciones de mejora en Microsoft Purview Compliance Manager y seguimiento en Planner.
- **Estadios:** E1 Menos de 50%: hallazgos recurrentes y vencidos sin explicación. | E2 50% a 69%: plan de acción por hallazgo, con vencimientos frecuentes. | E3 70% a 84%: seguimiento mensual con dueños y prórrogas formales. | E4 85% a 94%: atención de la causa raíz y validación independiente antes del cierre. | E5 95% o más: hallazgos anticipados por autoevaluación continua; recurrencia cero.
- **Umbrales:** E2 ≥ 50% · E3 ≥ 70% · E4 ≥ 85% · E5 ≥ 95% (E3 = mínimo aceptable; E4 = meta por defecto)
- **Correspondencias:** NIST CSF 2.0 GV.OV · CIS v8.1 — · ISO/IEC 27001:2022 10.2 (no conformidad y acción correctiva) · Otros: Normas Globales de Auditoría Interna del IIA (2024)

#### K60 · Controles clave con efectividad probada
- **Coordenadas:** T08 · GV08 Assurance y revisión independiente · D03 Compliance & Regulatory Security (secundarios: D01) · Gestión · GM-24 M3.2 · KCI · Efectividad · Adelantado
- **Qué mide:** Porcentaje de los controles clave de ciberseguridad cuya efectividad operativa (no solo su diseño) se probó en el período con resultado satisfactorio, preferentemente con evidencia reunida de forma automática.
- **Por qué importa:** Un control documentado pero no probado es una suposición. La prueba de efectividad es lo que permite afirmar que el riesgo está mitigado.
- **Fórmula:** Controles clave con prueba de efectividad satisfactoria en el período ÷ controles clave × 100.
- **Unidad y polaridad:** % · Mayor es mejor · **Frecuencia:** Trimestral · **Audiencia:** Directorio · Comité de auditoría · CISO
- **Fuente de datos:** Plan de pruebas de controles; GRC; evidencias automatizadas. **Evidencia (ejemplo Microsoft):** Pruebas y evidencias en Microsoft Purview Compliance Manager; cumplimiento normativo continuo en Defender for Cloud.
- **Estadios:** E1 Menos de 40%: los controles se evalúan solo en auditorías externas. | E2 40% a 59%: autoevaluaciones sin prueba de operación. | E3 60% a 79%: plan anual de pruebas de controles clave por la segunda línea. | E4 80% a 94%: pruebas basadas en evidencia automatizada y muestreo estadístico. | E5 95% o más: monitoreo continuo de controles con alertas de falla y validación por emulación.
- **Umbrales:** E2 ≥ 40% · E3 ≥ 60% · E4 ≥ 80% · E5 ≥ 95% (E3 = mínimo aceptable; E4 = meta por defecto)
- **Correspondencias:** NIST CSF 2.0 ID.IM · CIS v8.1 — · ISO/IEC 27001:2022 9.1 (seguimiento, medición, análisis y evaluación) · Otros: COSO; SOC 2; ISO/IEC 27004:2016

#### K61 · Notificaciones obligatorias emitidas en plazo
- **Coordenadas:** T08 · RS03 Comunicación de crisis y decisiones ejecutivas · D03 Compliance & Regulatory Security (secundarios: D07, D15) · Gobierno · GM-24 G3.1 · KCI · Efectividad · Rezagado
- **Qué mide:** Porcentaje de notificaciones obligatorias —a reguladores, autoridades de ciberseguridad o de datos personales, clientes y socios— emitidas dentro del plazo aplicable, considerando incidentes reales y simulados en ejercicios.
- **Por qué importa:** Notificar tarde convierte un incidente en un incumplimiento regulatorio y en una crisis de confianza. Los plazos se miden en horas: hay que ensayarlos.
- **Fórmula:** Notificaciones (reales y simuladas) emitidas en plazo ÷ notificaciones requeridas en el período × 100. Toda notificación real tardía se informa además como evento de incumplimiento.
- **Unidad y polaridad:** % · Mayor es mejor · **Frecuencia:** Por evento · trimestral · **Audiencia:** Directorio · Legal · Cumplimiento
- **Fuente de datos:** Registro de incidentes y de notificaciones; actas de ejercicios. **Evidencia (ejemplo Microsoft):** Línea de tiempo del incidente en Microsoft Sentinel o Defender XDR; plantillas y flujos en Teams y Power Automate.
- **Estadios:** E1 Menos de 60%: no hay inventario de plazos de notificación por jurisdicción. | E2 60% a 79%: Legal conoce los plazos, pero el procedimiento no se ensayó. | E3 80% a 94%: matriz de notificación por jurisdicción y plantillas aprobadas. | E4 95% a 99%: el reloj de notificación se activa automáticamente al clasificar el incidente. | E5 100%: notificaciones ensayadas con las autoridades en ejercicios; ninguna notificación real tardía.
- **Umbrales:** E2 ≥ 60% · E3 ≥ 80% · E4 ≥ 95% · E5 ≥ 100% (E3 = mínimo aceptable; E4 = meta por defecto)
- **Correspondencias:** NIST CSF 2.0 RS.CO · CIS v8.1 17 · ISO/IEC 27001:2022 5.5 (contacto con las autoridades) y 5.26 · Otros: DORA art. 19 (RTS 2025/301); NIS2 art. 23; Ley 21.663 art. 9 (Chile); CMF RAN 20-8; BCRA Com. «A» 8280; CRA art. 14; SEC Form 8-K Item 1.05

#### K62 · Incidentes de terceros notificados en el plazo contractual
- **Coordenadas:** T08 · RS04 Gestión de incidentes con terceros · D17 Third-Party & Supply Chain Security (secundarios: D15) · Gestión · GM-24 M6.2 · KRI · Efectividad · Rezagado
- **Qué mide:** Porcentaje de incidentes ocurridos en proveedores o socios que afectaron (o pudieron afectar) a la organización y que el tercero notificó dentro del plazo contractual con la información necesaria para responder.
- **Por qué importa:** Cuando el incidente ocurre en un tercero, la organización depende de su transparencia para cumplir sus propios plazos de notificación y contener el impacto.
- **Fórmula:** Incidentes de terceros notificados en el plazo contractual ÷ incidentes de terceros conocidos que afectaron a la organización × 100.
- **Unidad y polaridad:** % · Mayor es mejor · **Frecuencia:** Trimestral · **Audiencia:** Comité de riesgos · Compras
- **Fuente de datos:** Registro de incidentes; gestión de terceros; contratos. **Evidencia (ejemplo Microsoft):** Incidentes etiquetados por proveedor en Microsoft Sentinel; accesos de terceros en Microsoft Entra ID.
- **Estadios:** E1 Menos de 40% o desconocido: los incidentes de terceros se conocen por la prensa. | E2 40% a 59%: cláusulas de notificación genéricas y sin plazos. | E3 60% a 79%: plazos contractuales y contactos de crisis definidos con los proveedores críticos. | E4 80% a 94%: ejercicios conjuntos y canales de intercambio de inteligencia. | E5 95% o más: notificación automatizada e integración de telemetría con los proveedores críticos.
- **Umbrales:** E2 ≥ 40% · E3 ≥ 60% · E4 ≥ 80% · E5 ≥ 95% (E3 = mínimo aceptable; E4 = meta por defecto)
- **Correspondencias:** NIST CSF 2.0 GV.SC · CIS v8.1 15 · ISO/IEC 27001:2022 5.22 (seguimiento y gestión de cambios de los servicios de proveedores) · Otros: DORA art. 30; NIS2 art. 21.2(d); ISO 28000:2022

#### K63 · Excepciones a políticas vigentes, justificadas y con vencimiento
- **Coordenadas:** T08 · GV03 Políticas y estándares · D01 Cybersecurity Governance (secundarios: D02) · Gobierno · GM-24 G2.2 · KCI · Implementación · Adelantado
- **Qué mide:** Porcentaje de las excepciones vigentes a políticas y estándares de seguridad que tienen justificación de negocio, control compensatorio, aprobación de la autoridad correspondiente y fecha de vencimiento no superada.
- **Por qué importa:** Las excepciones son el punto donde la política se encuentra con la realidad. Sin control se acumulan como deuda invisible y vacían de contenido a la norma.
- **Fórmula:** Excepciones vigentes con justificación, compensación, aprobación y sin vencer ÷ excepciones vigentes × 100.
- **Unidad y polaridad:** % · Mayor es mejor · **Frecuencia:** Trimestral · **Audiencia:** Comité de riesgos · Auditoría
- **Fuente de datos:** Registro de excepciones en el GRC. **Evidencia (ejemplo Microsoft):** Exenciones con fecha de vencimiento en Microsoft Defender for Cloud y en Microsoft Secure Score.
- **Estadios:** E1 Menos de 40%: excepciones informales y permanentes. | E2 40% a 59%: registro de excepciones sin vencimiento ni compensación. | E3 60% a 79%: proceso formal con vencimiento máximo y aprobación según el nivel de riesgo. | E4 80% a 94%: controles compensatorios verificados y reporte de tendencia. | E5 95% o más: excepciones gestionadas como código, con expiración automática y reevaluación.
- **Umbrales:** E2 ≥ 40% · E3 ≥ 60% · E4 ≥ 80% · E5 ≥ 95% (E3 = mínimo aceptable; E4 = meta por defecto)
- **Correspondencias:** NIST CSF 2.0 GV.PO · CIS v8.1 — · ISO/IEC 27001:2022 5.1 (políticas) y 5.36 (cumplimiento de políticas) · Otros: COBIT 2019 (APO01)

#### K64 · Tratamientos de datos personales de alto riesgo con evaluación de impacto
- **Coordenadas:** T08 · PR02 Protección de datos y privacidad por diseño · D07 Privacy & Data Protection Engineering (secundarios: D06, D20) · Gestión · GM-24 M2.1 · KCI · Implementación · Adelantado
- **Qué mide:** Porcentaje de tratamientos de datos personales de alto riesgo (perfilamiento, datos sensibles, datos masivos de clientes o ciudadanos, uso en IA) con evaluación de impacto en la protección de datos vigente y medidas aplicadas.
- **Por qué importa:** La privacidad es la dimensión de la confianza que clientes y ciudadanos perciben de forma directa, y las leyes recientes de la región la refuerzan con derechos exigibles y sanciones.
- **Fórmula:** Tratamientos de alto riesgo con evaluación de impacto vigente y medidas implementadas ÷ tratamientos de alto riesgo inventariados × 100.
- **Unidad y polaridad:** % · Mayor es mejor · **Frecuencia:** Semestral · **Audiencia:** Delegado de protección de datos · Comité de riesgos
- **Fuente de datos:** Registro de actividades de tratamiento; evaluaciones de impacto. **Evidencia (ejemplo Microsoft):** Clasificadores de datos personales de Microsoft Purview y gestión de solicitudes de titulares con Microsoft Priva.
- **Estadios:** E1 Menos de 30%: sin registro de tratamientos; la privacidad se trata como trámite legal. | E2 30% a 49%: registro parcial de tratamientos y evaluaciones a demanda. | E3 50% a 74%: metodología de evaluación de impacto aprobada y aplicada a los nuevos tratamientos. | E4 75% a 94%: evaluaciones vinculadas a cambios de sistemas y a casos de uso de IA. | E5 95% o más: privacidad por diseño verificable; evaluaciones actualizadas por eventos y monitoreo de cumplimiento.
- **Umbrales:** E2 ≥ 30% · E3 ≥ 50% · E4 ≥ 75% · E5 ≥ 95% (E3 = mínimo aceptable; E4 = meta por defecto)
- **Correspondencias:** NIST CSF 2.0 PR.DS · CIS v8.1 3 · ISO/IEC 27001:2022 5.34 (privacidad y protección de datos personales) · Otros: ISO/IEC 27701; leyes de datos personales de la región (ver Marco_Regulatorio)

## 6. Estadios de madurez y de cumplimiento

| Estadio | Qué se observa | NIST CSF 2.0 (Tier) | C2M2 · ISA/IEC 62443 | Lectura |
|---|---|---|---|---|
| E1 Inicial | Práctica ad hoc o inexistente; sin medición cuantitativa. | Tier 1 Partial | MIL0–MIL1 · ML1 | No cumple |
| E2 En desarrollo | Práctica definida en parte; medición manual o esporádica. | Tier 2 Risk Informed | MIL1 · ML2 | No cumple (en camino) |
| E3 Definido | Práctica documentada, repetible y con dueño; alcanza el mínimo. | Tier 3 Repeatable | MIL2 · ML3 | Cumple el mínimo |
| E4 Gestionado | Medición automatizada, metas ligadas al apetito. | Tier 4 Adaptive (en parte) | MIL3 · ML4 | Meta alcanzada |
| E5 Adaptativo (frontera) | Mejora continua con automatización y agentes gobernados. | Tier 4 Adaptive | MIL3 · ML4 | Referente |

Estados de cumplimiento que calcula el libro: **No cumple** (peor que E3), **Cumple el mínimo** (E3 hasta la meta), **Meta alcanzada** (meta hasta E5), **Referente** (meta y E5), **Sin dato** y **No aplica**. Las correspondencias con Tiers, MIL y ML son editoriales. NIST SP 800-55v1 recuerda que las evaluaciones solo cualitativas no son mediciones: por eso cada estadio tiene un umbral cuantitativo.

## 7. Arreglos por sector

Cada sector tiene una relación distinta con el negocio, con los clientes y con la regulación. El libro la expresa como un **perfil de presión** de 1 a 5 en siete ejes y calcula el arreglo con un motor transparente:

> Puntaje = 100 × [α × base ÷ 3 + (1 − α) × Σ afinidad × (presión ÷ 5)^γ ÷ masa de referencia] + ajuste experto. Con α = 0,4, γ = 2 y masa de referencia 6. **Directorio:** 10 KPIs entre los aptos (el núcleo K24 y K25 entra siempre). **Esencial:** 10 más. **Complementario:** 20. **Opcional:** 24.

| Perfil | E1 Regulación y supervisión | E2 Clientes y confianza pública | E3 Continuidad operacional | E4 OT y consecuencia física | E5 Terceros y ecosistema | E6 Datos sensibles y PI | E7 IA y agentes (frontera) |
|---|---|---|---|---|---|---|---|
| Logística | 3 | 4 | 5 | 3 | 5 | 3 | 4 |
| Oil & Gas | 4 | 2 | 4 | 5 | 4 | 3 | 3 |
| Industrial | 3 | 3 | 4 | 5 | 4 | 4 | 4 |
| Financiero | 5 | 5 | 5 | 1 | 4 | 5 | 5 |
| Gobierno | 4 | 5 | 4 | 2 | 3 | 5 | 3 |
| Generación eléctrica | 5 | 3 | 5 | 5 | 4 | 2 | 3 |
| Mi organización | 3 | 3 | 3 | 3 | 3 | 3 | 3 |

### Logística
- **Negocio:** Vende tiempo, puntualidad y trazabilidad. La operación es una red de nodos (almacenes, flotas, puertos, aduanas) donde la indisponibilidad se mide en horas de flujo detenido.
- **Clientes:** B2B intensivo en integraciones (EDI/API) y acuerdos de nivel de servicio; en la última milla maneja datos de consumidores finales.
- **Regulación:** Moderada y fragmentada: aduanas (OEA, Marco SAFE de la OMA), marítima (OMI), seguridad de la cadena de suministro (ISO 28000) y, para operaciones en la UE, NIS2 (transporte).
- **Escenarios característicos:** Ransomware que detiene el WMS/TMS; compromiso de un socio integrado; fraude de pagos a proveedores; manipulación de telemetría de flota; caída de un proveedor de nube.
- **Qué quiere ver el Directorio:** Continuidad del flujo, dependencia de terceros, tiempo de restauración y compromisos con clientes.
- **Trampa de medición:** Medir solo la seguridad propia cuando el riesgo está en la red de socios.
- **Directorio (10):** K24 Pérdidas por incidentes frente a la tolerancia anual; K25 Riesgos residuales fuera del apetito; K31 Proveedores críticos evaluados y con cláusulas de seguridad; K27 Servicios críticos concentrados en un proveedor sin alternativa; K56 Procesos críticos con IA capaces de operar sin ella; K15 Ejercicios de crisis con participación ejecutiva; K28 Respaldos inmutables de sistemas críticos con restauración probada; K30 Pruebas de recuperación que cumplen RTO y RPO; K45 Tiempo medio de contención (MTTC); K61 Notificaciones obligatorias emitidas en plazo.
- **Esenciales del CISO (10):** K34 Accesos privilegiados sin privilegios permanentes (JIT); K21 Procesos críticos con BIA vigente y dependencias mapeadas; K37 Datos sensibles clasificados y protegidos; K47 Tiempo de restauración de servicios críticos frente al RTO; K62 Incidentes de terceros notificados en el plazo contractual; K29 Operación degradada probada en procesos críticos; K49 Inventario de sistemas de IA y agentes; K33 Autenticación resistente al phishing; K39 Cobertura del inventario de activos (TI, nube, OT e IoT); K05 Tiempo hasta la decisión ejecutiva en crisis.
- **Composición del tablero ejecutivo (20):** GV 3, ID 4, PR 3, DE 0, RS 5, RC 5; 6 de gobierno y 14 de gestión.
- **Ajustes expertos:** K31 +10 (La red de socios (transportistas, agentes de aduana, integraciones EDI/API) es la superficie de ataque principal.); K62 +10 (La operación depende de la transparencia de terceros para cumplir plazos con clientes y autoridades.)

### Oil & Gas
- **Negocio:** Procesos físicos continuos de alta consecuencia (personas, ambiente, integridad de activos); sitios remotos y tecnología OT de larga vida útil.
- **Clientes:** Mayormente B2B y mercados de commodities; el cliente final es indirecto, salvo en la venta minorista de combustibles.
- **Regulación:** Seguridad de procesos y ambiental, leyes de infraestructura crítica, directivas para ductos (TSA en EE. UU.) y estándares como API 1164 e ISA/IEC 62443.
- **Escenarios característicos:** Ransomware o sabotaje que alcanza OT; acceso remoto de contratistas; compromiso de un socio de joint venture; espionaje de datos de exploración.
- **Qué quiere ver el Directorio:** Seguridad de procesos, operación degradada, accesos de terceros a OT y nivel de seguridad por zona.
- **Trampa de medición:** Trasladar métricas de TI (parches al 100%) a OT, donde mandan la disponibilidad y la seguridad física.
- **Directorio (10):** K24 Pérdidas por incidentes frente a la tolerancia anual; K25 Riesgos residuales fuera del apetito; K15 Ejercicios de crisis con participación ejecutiva; K31 Proveedores críticos evaluados y con cláusulas de seguridad; K30 Pruebas de recuperación que cumplen RTO y RPO; K40 Zonas OT e IIoT que alcanzan su nivel de seguridad objetivo; K29 Operación degradada probada en procesos críticos; K27 Servicios críticos concentrados en un proveedor sin alternativa; K28 Respaldos inmutables de sistemas críticos con restauración probada; K45 Tiempo medio de contención (MTTC).
- **Esenciales del CISO (10):** K34 Accesos privilegiados sin privilegios permanentes (JIT); K39 Cobertura del inventario de activos (TI, nube, OT e IoT); K33 Autenticación resistente al phishing; K61 Notificaciones obligatorias emitidas en plazo; K32 Escenarios críticos con playbook probado; K36 Segmentación de activos críticos verificada; K47 Tiempo de restauración de servicios críticos frente al RTO; K21 Procesos críticos con BIA vigente y dependencias mapeadas; K26 Pérdida esperada de los escenarios prioritarios frente al apetito; K05 Tiempo hasta la decisión ejecutiva en crisis.
- **Composición del tablero ejecutivo (20):** GV 3, ID 4, PR 4, DE 0, RS 5, RC 4; 7 de gobierno y 13 de gestión.
- **Ajustes expertos:** K40 +20 (ISA/IEC 62443 y API 1164 orientan la protección por zonas; la consecuencia física exige un nivel objetivo por zona.)

### Industrial
- **Negocio:** La disponibilidad de planta (OEE) y la propiedad intelectual (diseños, fórmulas, recetas) son el valor; cadenas de suministro globales.
- **Clientes:** B2B y B2C, con responsabilidad creciente por la seguridad de los productos conectados que vende.
- **Regulación:** Moderada y en aumento: seguridad de productos con elementos digitales (Cyber Resilience Act para el mercado de la UE), requisitos de clientes (IEC 62443-4-1/4-2) y normas sectoriales.
- **Escenarios característicos:** Ransomware que detiene la planta; robo de propiedad intelectual; compromiso de un integrador de automatización; vulnerabilidad en un producto vendido.
- **Qué quiere ver el Directorio:** Disponibilidad de planta, protección de la propiedad intelectual, riesgo de proveedores y seguridad de producto.
- **Trampa de medición:** Separar TI y OT en tableros distintos sin una visión integrada del riesgo.
- **Directorio (10):** K24 Pérdidas por incidentes frente a la tolerancia anual; K25 Riesgos residuales fuera del apetito; K37 Datos sensibles clasificados y protegidos; K15 Ejercicios de crisis con participación ejecutiva; K28 Respaldos inmutables de sistemas críticos con restauración probada; K31 Proveedores críticos evaluados y con cláusulas de seguridad; K45 Tiempo medio de contención (MTTC); K29 Operación degradada probada en procesos críticos; K56 Procesos críticos con IA capaces de operar sin ella; K61 Notificaciones obligatorias emitidas en plazo.
- **Esenciales del CISO (10):** K34 Accesos privilegiados sin privilegios permanentes (JIT); K39 Cobertura del inventario de activos (TI, nube, OT e IoT); K30 Pruebas de recuperación que cumplen RTO y RPO; K33 Autenticación resistente al phishing; K40 Zonas OT e IIoT que alcanzan su nivel de seguridad objetivo; K47 Tiempo de restauración de servicios críticos frente al RTO; K27 Servicios críticos concentrados en un proveedor sin alternativa; K32 Escenarios críticos con playbook probado; K36 Segmentación de activos críticos verificada; K52 Interacciones con IA protegidas contra la fuga de datos.
- **Composición del tablero ejecutivo (20):** GV 3, ID 2, PR 6, DE 0, RS 4, RC 5; 5 de gobierno y 15 de gestión.
- **Ajustes expertos:** K40 +20 (Plantas con OT de larga vida útil; ISA/IEC 62443 es el lenguaje común con integradores y clientes.); K37 +10 (La propiedad intelectual (diseños, fórmulas, recetas) define la ventaja competitiva.)

### Financiero
- **Negocio:** La confianza es el producto: pagos, ahorro y crédito 24×7. El riesgo cibernético es riesgo operacional y, a escala, sistémico.
- **Clientes:** Exposición masiva y directa a clientes por canales digitales; fraude y protección del consumidor en primer plano.
- **Regulación:** La más intensa: supervisión prudencial (BCRA, SFC, CMF, SBS, CNBV), resiliencia operacional (Basilea; DORA en la UE), PCI DSS, SWIFT CSP y divulgación al mercado cuando cotiza (SEC).
- **Escenarios característicos:** Fraude con identidades sintéticas y deepfakes; ransomware; caída de un proveedor crítico o de la nube; fuga masiva de datos; abuso de agentes en procesos con clientes.
- **Qué quiere ver el Directorio:** Riesgo dentro del apetito, pérdidas frente a la tolerancia, notificaciones al supervisor, hallazgos regulatorios, concentración en terceros y gobierno de la IA.
- **Trampa de medición:** Responder la lista de verificación del supervisor y confundirla con resiliencia probada.
- **Directorio (10):** K24 Pérdidas por incidentes frente a la tolerancia anual; K25 Riesgos residuales fuera del apetito; K37 Datos sensibles clasificados y protegidos; K61 Notificaciones obligatorias emitidas en plazo; K64 Tratamientos de datos personales de alto riesgo con evaluación de impacto; K51 Casos de uso de IA con evaluación de riesgo e impacto previa; K27 Servicios críticos concentrados en un proveedor sin alternativa; K28 Respaldos inmutables de sistemas críticos con restauración probada; K30 Pruebas de recuperación que cumplen RTO y RPO; K45 Tiempo medio de contención (MTTC).
- **Esenciales del CISO (10):** K52 Interacciones con IA protegidas contra la fuga de datos; K50 Agentes con dueño humano y autoridad delegada acotada; K33 Autenticación resistente al phishing; K49 Inventario de sistemas de IA y agentes; K57 Obligaciones aplicables mapeadas a controles con evidencia vigente; K59 Hallazgos de auditoría y de reguladores cerrados en plazo; K15 Ejercicios de crisis con participación ejecutiva; K56 Procesos críticos con IA capaces de operar sin ella; K26 Pérdida esperada de los escenarios prioritarios frente al apetito; K34 Accesos privilegiados sin privilegios permanentes (JIT).
- **Composición del tablero ejecutivo (20):** GV 6, ID 3, PR 5, DE 0, RS 3, RC 3; 10 de gobierno y 10 de gestión.
- **Ajustes expertos:** K59 +25 (Los hallazgos del supervisor y de auditoría son materia del Directorio y del comité de auditoría.)

### Gobierno
- **Negocio:** Servicio público continuo y legitimidad institucional, con presupuestos rígidos, ciclos políticos y sistemas heredados.
- **Clientes:** Ciudadanos cautivos que no pueden cambiar de proveedor: la confianza pública y la protección de sus datos son el centro.
- **Regulación:** Marcos nacionales para el sector público, leyes de datos personales, transparencia, control de organismos de auditoría y leyes marco de ciberseguridad.
- **Escenarios característicos:** Ransomware en servicios al ciudadano; fuga de bases de identidad o tributarias; hacktivismo y desinformación; sistemas sin soporte.
- **Qué quiere ver el Directorio:** Continuidad de servicios críticos, cumplimiento con evidencia, protección de datos de ciudadanos y notificación oportuna.
- **Trampa de medición:** Medir el cumplimiento formal de la norma sin probar la recuperación.
- **Directorio (10):** K24 Pérdidas por incidentes frente a la tolerancia anual; K25 Riesgos residuales fuera del apetito; K37 Datos sensibles clasificados y protegidos; K61 Notificaciones obligatorias emitidas en plazo; K64 Tratamientos de datos personales de alto riesgo con evaluación de impacto; K57 Obligaciones aplicables mapeadas a controles con evidencia vigente; K30 Pruebas de recuperación que cumplen RTO y RPO; K33 Autenticación resistente al phishing; K28 Respaldos inmutables de sistemas críticos con restauración probada; K45 Tiempo medio de contención (MTTC).
- **Esenciales del CISO (10):** K52 Interacciones con IA protegidas contra la fuga de datos; K26 Pérdida esperada de los escenarios prioritarios frente al apetito; K51 Casos de uso de IA con evaluación de riesgo e impacto previa; K42 Tiempo medio de detección (MTTD); K35 Activos conformes a la línea base de configuración segura; K50 Agentes con dueño humano y autoridad delegada acotada; K38 Aplicaciones críticas con controles automatizados en el pipeline; K08 Escalamiento oportuno de riesgos materiales; K15 Ejercicios de crisis con participación ejecutiva; K47 Tiempo de restauración de servicios críticos frente al RTO.
- **Composición del tablero ejecutivo (20):** GV 6, ID 1, PR 6, DE 1, RS 3, RC 3; 9 de gobierno y 11 de gestión.
- **Ajustes expertos:** K57 +15 (Los órganos de control exigen cumplimiento con evidencia de los marcos nacionales.); K30 +10 (Evita la trampa del cumplimiento formal: la continuidad del servicio al ciudadano se debe probar.); K35 +15 (Alta proporción de sistemas heredados y sin soporte en el sector público.)

### Generación eléctrica
- **Negocio:** Disponibilidad y confiabilidad del sistema eléctrico (MW disponibles); procesos físicos de alta consecuencia con OT de larga vida útil.
- **Clientes:** El operador del sistema y el mercado mayorista; grandes clientes; la consecuencia social de un apagón es alta aunque el cliente final sea indirecto.
- **Regulación:** Intensa y técnica: códigos de red, estándares de ciberseguridad del coordinador o del regulador (p. ej., NERC CIP en Norteamérica) y leyes de infraestructura crítica.
- **Escenarios característicos:** Ransomware o sabotaje que alcanza DCS/SCADA; acceso remoto de fabricantes (OEM); compromiso de la cadena de suministro de equipos; falla en cascada.
- **Qué quiere ver el Directorio:** Disponibilidad, operación degradada y manual, nivel de seguridad de zonas OT, notificación al regulador y terceros con acceso.
- **Trampa de medición:** Informar cumplimiento de la norma técnica como si fuera resiliencia frente a un adversario capaz.
- **Directorio (10):** K24 Pérdidas por incidentes frente a la tolerancia anual; K25 Riesgos residuales fuera del apetito; K15 Ejercicios de crisis con participación ejecutiva; K30 Pruebas de recuperación que cumplen RTO y RPO; K29 Operación degradada probada en procesos críticos; K61 Notificaciones obligatorias emitidas en plazo; K27 Servicios críticos concentrados en un proveedor sin alternativa; K28 Respaldos inmutables de sistemas críticos con restauración probada; K45 Tiempo medio de contención (MTTC); K40 Zonas OT e IIoT que alcanzan su nivel de seguridad objetivo.
- **Esenciales del CISO (10):** K34 Accesos privilegiados sin privilegios permanentes (JIT); K39 Cobertura del inventario de activos (TI, nube, OT e IoT); K47 Tiempo de restauración de servicios críticos frente al RTO; K31 Proveedores críticos evaluados y con cláusulas de seguridad; K05 Tiempo hasta la decisión ejecutiva en crisis; K59 Hallazgos de auditoría y de reguladores cerrados en plazo; K21 Procesos críticos con BIA vigente y dependencias mapeadas; K32 Escenarios críticos con playbook probado; K26 Pérdida esperada de los escenarios prioritarios frente al apetito; K56 Procesos críticos con IA capaces de operar sin ella.
- **Composición del tablero ejecutivo (20):** GV 4, ID 4, PR 2, DE 0, RS 5, RC 5; 8 de gobierno y 12 de gestión.
- **Ajustes expertos:** K40 +25 (Estándares técnicos del sector (p. ej., NERC CIP, ISA/IEC 62443) y consecuencia física exigen nivel de seguridad por zona.); K29 +10 (La operación manual o en isla sostiene la disponibilidad del sistema eléctrico.); K61 +10 (Operadores de infraestructura crítica con plazos de notificación medidos en horas.); K59 +20 (Las auditorías del regulador o del coordinador del sistema son materia del Directorio.)

**Lectura transversal.** Banca y Gobierno ponen Govern al frente del tablero ejecutivo (6 de 20 KPIs); los sectores con OT y la logística priorizan Respond y Recover (9 a 10 de 20). Detect casi no llega al tablero ejecutivo: es un tablero del SOC, no del Directorio. Los KPIs de T01 (juicio) llegan poco al tablero ejecutivo (0 o 1 de 20, según el sector); se recomiendan como **tablero personal del CISO** y como eje de desarrollo en TheNextCISO.

**Mi organización.** En Perfiles_Sector, ajuste la fila «Mi organización» (presiones 1–5) y, si hace falta, la aptitud y los ajustes en Afinidades. El arreglo se recalcula solo y Paquetes_Sector lista el resultado.

## 8. OKR

Los OKR traducen la estrategia en compromisos con fecha. Cada resultado clave usa un KPI del catálogo con meta igual a su umbral E4 (editable). El avance se calcula como la fracción recorrida entre la línea base y la meta; «En camino» desde 70%.

### Por territorio
| Territorio | Objetivo | Resultados clave |
|---|---|---|
| T01 | Hacer explícito, calibrado y revisable el juicio de seguridad. | K03 Decisiones materiales con registro y revisión posterior: ≥ 75%<br>K08 Escalamiento oportuno de riesgos materiales: ≥ 90%<br>K01 Calibración del juicio de riesgo (puntaje de habilidad de Brier): ≥ 0,20 |
| T02 | Distribuir la responsabilidad del ciberriesgo y sostener un equipo preparado. | K09 Procesos y activos críticos con dueño de riesgo designado: ≥ 80%<br>K10 Ejecutivos con objetivos de ciberseguridad en su evaluación: ≥ 60%<br>K16 Roles críticos con suplente entrenado: ≥ 80% |
| T03 | Convertir la inversión en seguridad en reducción de riesgo y velocidad de negocio. | K17 Inversión en seguridad trazada a riesgos y objetivos del negocio: ≥ 80%<br>K19 Reducción de riesgo por unidad de inversión: ≥ 2x<br>K20 Tiempo de habilitación segura de iniciativas: ≤ 5 días |
| T04 | Mantener la exposición dentro del apetito y la recuperación probada. | K25 Riesgos residuales fuera del apetito: ≤ 5%<br>K30 Pruebas de recuperación que cumplen RTO y RPO: ≥ 80%<br>K28 Respaldos inmutables de sistemas críticos con restauración probada: ≥ 85% |
| T05 | Eliminar clases completas de ataque por diseño. | K33 Autenticación resistente al phishing: ≥ 80%<br>K34 Accesos privilegiados sin privilegios permanentes (JIT): ≥ 75%<br>K35 Activos conformes a la línea base de configuración segura: ≥ 85% |
| T06 | Detectar y contener en horas, aprendiendo de cada incidente. | K42 Tiempo medio de detección (MTTD): ≤ 8 h<br>K45 Tiempo medio de contención (MTTC): ≤ 4 h<br>K46 Vulnerabilidades explotadas y exposiciones críticas remediadas en plazo: ≥ 85% |
| T07 | Gobernar la autoridad no humana antes de escalarla. | K49 Inventario de sistemas de IA y agentes: ≥ 75%<br>K50 Agentes con dueño humano y autoridad delegada acotada: ≥ 75%<br>K56 Procesos críticos con IA capaces de operar sin ella: ≥ 75% |
| T08 | Probar con evidencia lo que afirmamos sobre nuestra seguridad. | K57 Obligaciones aplicables mapeadas a controles con evidencia vigente: ≥ 85%<br>K60 Controles clave con efectividad probada: ≥ 80%<br>K61 Notificaciones obligatorias emitidas en plazo: ≥ 95% |

### Por sector
| Sector | Tipo | Objetivo | Resultados clave |
|---|---|---|---|
| Financiero | Gobernar | Gobernar el ciberriesgo como riesgo operacional dentro del apetito aprobado. | K25 Riesgos residuales fuera del apetito: ≤ 5%<br>K61 Notificaciones obligatorias emitidas en plazo: ≥ 95%<br>K59 Hallazgos de auditoría y de reguladores cerrados en plazo: ≥ 85% |
| Financiero | Gestionar | Reducir la exposición a fuga de datos, ransomware y terceros críticos. | K37 Datos sensibles clasificados y protegidos: ≥ 75%<br>K30 Pruebas de recuperación que cumplen RTO y RPO: ≥ 80%<br>K27 Servicios críticos concentrados en un proveedor sin alternativa: ≤ 15% |
| Financiero | Evolucionar | Escalar la IA y los agentes con autoridad acotada y sin fuga de datos. | K50 Agentes con dueño humano y autoridad delegada acotada: ≥ 75%<br>K51 Casos de uso de IA con evaluación de riesgo e impacto previa: ≥ 80%<br>K52 Interacciones con IA protegidas contra la fuga de datos: ≥ 75% |
| Gobierno | Gobernar | Demostrar cumplimiento con evidencia y rendición de cuentas ante los órganos de control. | K57 Obligaciones aplicables mapeadas a controles con evidencia vigente: ≥ 85%<br>K61 Notificaciones obligatorias emitidas en plazo: ≥ 95%<br>K64 Tratamientos de datos personales de alto riesgo con evaluación de impacto: ≥ 75% |
| Gobierno | Gestionar | Asegurar la continuidad de los servicios críticos al ciudadano. | K30 Pruebas de recuperación que cumplen RTO y RPO: ≥ 80%<br>K33 Autenticación resistente al phishing: ≥ 80%<br>K35 Activos conformes a la línea base de configuración segura: ≥ 85% |
| Gobierno | Evolucionar | Proteger los datos de los ciudadanos en la adopción de IA. | K51 Casos de uso de IA con evaluación de riesgo e impacto previa: ≥ 80%<br>K49 Inventario de sistemas de IA y agentes: ≥ 75%<br>K52 Interacciones con IA protegidas contra la fuga de datos: ≥ 75% |
| Generación eléctrica | Gobernar | Gobernar el riesgo OT con el mismo rigor que la seguridad de los procesos. | K40 Zonas OT e IIoT que alcanzan su nivel de seguridad objetivo: ≥ 70%<br>K59 Hallazgos de auditoría y de reguladores cerrados en plazo: ≥ 85%<br>K14 Supervisión activa del Directorio sobre el ciberriesgo: ≥ 75% |
| Generación eléctrica | Gestionar | Mantener la disponibilidad frente a un adversario capaz. | K29 Operación degradada probada en procesos críticos: ≥ 75%<br>K34 Accesos privilegiados sin privilegios permanentes (JIT): ≥ 75%<br>K30 Pruebas de recuperación que cumplen RTO y RPO: ≥ 80% |
| Generación eléctrica | Evolucionar | Incorporar IA a la operación sin crear nuevas dependencias críticas. | K56 Procesos críticos con IA capaces de operar sin ella: ≥ 75%<br>K43 Técnicas de ataque priorizadas con detección validada: ≥ 70%<br>K12 Cobertura de capacidades críticas del equipo de seguridad: ≥ 85% |
| Oil & Gas | Gobernar | Integrar el ciberriesgo OT en el apetito y en la gestión de seguridad de procesos. | K26 Pérdida esperada de los escenarios prioritarios frente al apetito: ≤ 75%<br>K31 Proveedores críticos evaluados y con cláusulas de seguridad: ≥ 80%<br>K09 Procesos y activos críticos con dueño de riesgo designado: ≥ 80% |
| Oil & Gas | Gestionar | Cerrar las rutas de ataque hacia OT. | K36 Segmentación de activos críticos verificada: ≥ 80%<br>K34 Accesos privilegiados sin privilegios permanentes (JIT): ≥ 75%<br>K46 Vulnerabilidades explotadas y exposiciones críticas remediadas en plazo: ≥ 85% |
| Oil & Gas | Evolucionar | Operar sitios remotos con monitoreo y respuesta asistidos por IA. | K45 Tiempo medio de contención (MTTC): ≤ 4 h<br>K15 Ejercicios de crisis con participación ejecutiva: ≥ 75%<br>K53 Observabilidad de agentes integrada a la detección: ≥ 70% |
| Industrial | Gobernar | Proteger la propiedad intelectual y la disponibilidad de planta como decisiones de negocio. | K37 Datos sensibles clasificados y protegidos: ≥ 75%<br>K22 Resultados del perfil objetivo alcanzados (NIST CSF 2.0): ≥ 70%<br>K31 Proveedores críticos evaluados y con cláusulas de seguridad: ≥ 80% |
| Industrial | Gestionar | Reducir el radio de explosión entre TI, OT y proveedores. | K40 Zonas OT e IIoT que alcanzan su nivel de seguridad objetivo: ≥ 70%<br>K39 Cobertura del inventario de activos (TI, nube, OT e IoT): ≥ 90%<br>K28 Respaldos inmutables de sistemas críticos con restauración probada: ≥ 85% |
| Industrial | Evolucionar | Llevar la seguridad desde el diseño a productos conectados y a la IA de ingeniería. | K38 Aplicaciones críticas con controles automatizados en el pipeline: ≥ 75%<br>K51 Casos de uso de IA con evaluación de riesgo e impacto previa: ≥ 80%<br>K20 Tiempo de habilitación segura de iniciativas: ≤ 5 días |
| Logística | Gobernar | Gobernar el riesgo de la red de socios como riesgo propio. | K31 Proveedores críticos evaluados y con cláusulas de seguridad: ≥ 80%<br>K27 Servicios críticos concentrados en un proveedor sin alternativa: ≤ 15%<br>K23 Requisitos de seguridad de clientes y contratos cumplidos en plazo: ≥ 90% |
| Logística | Gestionar | Mantener el flujo operativo ante ransomware o caída de sistemas. | K29 Operación degradada probada en procesos críticos: ≥ 75%<br>K47 Tiempo de restauración de servicios críticos frente al RTO: ≤ 100%<br>K62 Incidentes de terceros notificados en el plazo contractual: ≥ 80% |
| Logística | Evolucionar | Escalar la optimización con IA y agentes sin perder el control. | K49 Inventario de sistemas de IA y agentes: ≥ 75%<br>K50 Agentes con dueño humano y autoridad delegada acotada: ≥ 75%<br>K56 Procesos críticos con IA capaces de operar sin ella: ≥ 75% |

## 9. Cómo reutilizar el artefacto

1. **Elegir el perfil.** En Autoevaluacion!E3, o ajustar «Mi organización» en Perfiles_Sector.
1. **Medir.** Reemplazar los valores del caso ilustrativo (columna J de Autoevaluacion). Porcentajes como 85%. Marcar «No» en Aplica lo que no corresponda.
1. **Calibrar.** Ajustar umbrales en Estadios con datos históricos propios; cargar metas propias en Autoevaluacion (columna O) o en los OKR.
1. **Comprometer.** Cargar líneas base en OKR_Sectores u OKR_Territorios; el valor actual y el avance se calculan solos.
1. **Controlar.** Verificar que Control_Calidad tenga los 19 controles en OK.
1. **Integrar al Atlas.** El JSON incluye KPIs, estadios, perfiles, arreglos y OKR, con una propuesta de extensión de la Core Ontology 1.0 (tipo SecurityIndicator; relaciones MEASURES, INFORMS y TRACKED_BY) para tramitar como ChangeSet gobernado (ADR-011).

## 10. Marco regulatorio por sector

| Sector | Jurisdicción | Norma | Plazos de notificación | KPIs |
|---|---|---|---|---|
| Financiero | Unión Europea | DORA, Reglamento (UE) 2022/2554, y Reglamento Delegado (UE) 2025/301 | Inicial: ≤ 4 h desde la clasificación (≤ 24 h desde el conocimiento). Intermedio: ≤ 72 h. Final: ≤ 1 mes. | K15 · K27 · K30 · K31 · K61 |
| Financiero | Internacional | Principles for operational resilience (BCBS d516) | — | K21 · K29 · K30 |
| Financiero | Argentina | Com. «A» 7724 (requisitos mínimos de gestión y control de riesgos de tecnología y seguridad de la información) y Com. «A» 8280 (notificación de ciberincidentes) | Inicial: ≤ 1 h desde la ocurrencia o detección. Cierre: ≤ 5 días corridos con causa raíz. | K14 · K51 · K57 · K61 |
| Financiero | Colombia | Circular Externa 007 de 2018, incorporada en la Circular Básica Jurídica (Parte I, Título IV, Cap. V) | Plazo en horas: no verificado. Métricas: ≤ 15 días calendario después de cada corte trimestral. | K57 · K58 · K61 |
| Financiero | Perú | Resolución SBS N.° 504-2021, Reglamento para la Gestión de la Seguridad de la Información y la Ciberseguridad | «En cuanto advierta» el incidente (sin plazo en horas). | K57 · K61 |
| Financiero | Chile | RAN Capítulo 20-10 (seguridad de la información y ciberseguridad) y Capítulo 20-8 (información de incidentes operacionales) | ≤ 30 minutos desde la ocurrencia, en días hábiles e inhábiles. | K05 · K61 |
| Financiero | México | Disposiciones de carácter general aplicables a las instituciones de crédito, arts. 168 Bis 11 a 168 Bis 17 y Anexos 64 y 64 Bis | Aviso «inmediato» (plazo no verificado en fuente oficial). | K57 · K61 |
| Financiero | Global | PCI DSS v4.0.1 | — | K11 · K33 · K46 |
| Financiero | Global | Swift Customer Security Controls Framework v2026 | Atestación anual hasta el 31 de diciembre. | K57 · K60 |
| Emisores cotizantes | Estados Unidos | Cybersecurity Risk Management, Strategy, Governance, and Incident Disclosure (regla final de 2023) | ≤ 4 días hábiles desde la determinación de materialidad. | K08 · K14 · K58 · K61 |
| Gobierno | Argentina | Decisión Administrativa 641/2021, Requisitos mínimos de seguridad de la información para los organismos del Sector Público Nacional | ≤ 48 h (verificación indirecta; revisar el destinatario tras el DNU 941/2025). | K09 · K57 · K61 |
| Gobierno | Colombia | CONPES 3995 (2020) y Modelo de Seguridad y Privacidad de la Información v5.0 (Res. MinTIC 500 de 2021 y 2277 de 2025) | — | K22 · K57 · K64 |
| Servicios esenciales (incluye energía, combustibles, transporte, banca y Estado) | Chile | Ley 21.663, Ley Marco de Ciberseguridad | Alerta temprana: ≤ 3 h. Segundo informe: ≤ 72 h (≤ 24 h para OIV afectados). Final: ≤ 15 días. Plan de acción de OIV: ≤ 7 días. | K05 · K15 · K61 |
| Datos personales (transversal) | Chile | Ley 21.719, que regula la protección y el tratamiento de los datos personales | Según la ley y su reglamentación. | K37 · K61 · K64 |
| Datos personales (transversal) | México | Ley Federal de Protección de Datos Personales en Posesión de los Particulares (2025) | — | K37 · K64 |
| Transversal | Unión Europea | Directiva NIS2, (UE) 2022/2555 | Alerta temprana: ≤ 24 h. Notificación: ≤ 72 h. Final: ≤ 1 mes. | K07 · K10 · K14 · K31 · K61 |
| IA (transversal) | Unión Europea | Reglamento de IA (UE) 2024/1689, modificado por el Reglamento (UE) 2026/1744 (Digital Omnibus sobre IA) | Incidentes graves de sistemas de alto riesgo, según el reglamento. | K49 · K50 · K51 · K56 |
| IA (transversal) | Internacional | ISO/IEC 42001:2023; NIST AI RMF 1.0 (AI 100-1); NIST AI 600-1 | — | K49 a K56 |
| Transversal | Estados Unidos (federal) | CISA BOD 26-04, Prioritizing Security Updates Based on Risk (reemplaza a la BOD 22-01) | Caso más grave: remediar o mitigar en 3 días. | K46 |
| Transversal | Estados Unidos | Cross-Sector Cybersecurity Performance Goals 2.0 | — | K22 · K33 |
| Generación eléctrica | Norteamérica (EE. UU., Canadá y norte de Baja California) | NERC CIP (CIP-002 a CIP-014; CIP-015 aprobado) | Según CIP-008 (respuesta y reporte de incidentes). | K34 · K36 · K39 · K40 · K41 |
| Generación eléctrica | Chile | Estándar de Ciberseguridad para el Sector Eléctrico (versión octubre de 2022) | Incidente reportable: ≤ 1 h. | K40 · K59 · K61 |
| Generación eléctrica | Colombia | Acuerdo CNO 1960 de 2025 (Guía de Ciberseguridad) y Acuerdo 2188 de 2026 (reporte de incidentes) | Procedimiento y formato del Acuerdo 2188 (plazos no verificados). | K31 · K39 · K57 · K61 |
| Generación eléctrica | México | Código de Red (RES/550/2021, capítulo REI) y Manual de Requerimientos TIC del SEN y del MEM (2017, Anexo 4) | — | K35 · K41 · K57 |
| Energía, oil & gas e industria (OT) | Internacional | Serie ISA/IEC 62443 (2-1:2024, 3-2:2020, 3-3:2013, 2-4:2023, 4-1:2018) | — | K29 · K34 · K36 · K40 |
| Energía y oil & gas | Internacional | ISO/IEC 27019:2024, controles de seguridad para la industria de servicios de energía | — | K35 · K40 |
| Energía y oil & gas | Estados Unidos | Cybersecurity Capability Maturity Model (C2M2) v2.1 | — | K22 |
| Oil & Gas | Estados Unidos | TSA Security Directives Pipeline-2021-01G y Pipeline-2021-02 (serie vigente 02G) | Reporte a CISA: ≤ 72 h. | K29 · K32 · K34 · K36 · K61 |
| Oil & Gas | Internacional | API Standard 1164, 3.ª edición (2021), Pipeline Control Systems Cybersecurity | — | K36 · K40 |
| Industrial | Unión Europea | Cyber Resilience Act, Reglamento (UE) 2024/2847 | Vulnerabilidades explotadas e incidentes graves: alerta ≤ 24 h; notificación ≤ 72 h; final ≤ 14 días (vulnerabilidades) o ≤ 1 mes (incidentes). | K38 · K46 · K61 |
| Logística | Internacional (marítimo) | OMI Res. MSC.428(98) y circular MSC-FAL.1/Circ.3/Rev.4 | — | K29 · K31 · K36 |
| Logística | Internacional | ISO 28000:2022, sistemas de gestión de la seguridad (cadena de suministro) | — | K21 · K27 · K31 |
| Logística | Internacional (aduanas) | Marco SAFE de la OMA, edición 2025 (programa de Operador Económico Autorizado) | — | K31 · K37 · K62 |

## 11. Limitaciones y silencios

- Los umbrales de los estadios son referencias editoriales; deben calibrarse con datos propios antes de usarlos para evaluar desempeño.
- El motor de arreglos combina juicio experto (afinidades, aptitud, ajustes) con perfiles de presión; es transparente y editable, no una verdad estadística.
- No verificados en fuente oficial: plazos de aviso de la CNBV (México) y de la SFC (Colombia) en horas; versión 02G de la directiva TSA para ductos (confirmación secundaria); el destinatario del reporte de 48 h de la DA 641/2021 tras el DNU 941/2025; los plazos del Acuerdo CNO 2188.
- Normas en movimiento: Ley 21.719 (Chile) con postergación en trámite; propuestas Digital Omnibus que tocan NIS2 y DORA; ISO/IEC 27004 en revisión; reafirmación de API 1164 en votación.
- Dominios sin KPI primario (D09, D19, D22, D23): cubiertos como secundarios.
- La evidencia Microsoft es un ejemplo de fuente de datos; el catálogo es neutral respecto de proveedores.
- Los estadios E1–E5 miden madurez del indicador; no son el horizonte H del Atlas (ADR-009).

## 12. Fuentes

- **F01** · NIST Cybersecurity Framework (CSF) 2.0, CSWP 29 · NIST · 26-2-2024. Funciones GV-ID-PR-DE-RS-RC, 22 categorías, Tiers (Partial, Risk Informed, Repeatable, Adaptive) y perfiles actual y objetivo (K22). <https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf>
- **F02** · NIST SP 800-55v1 y v2, Measurement Guide for Information Security · NIST · 4-12-2024. Cuatro tipos de medidas: implementación, efectividad, eficiencia e impacto (columna «Tipo de medida»); programa de medición iterativo. <https://csrc.nist.gov/pubs/sp/800/55/v1/final>
- **F03** · ISO/IEC 27004:2016 (seguimiento, medición, análisis y evaluación) · ISO/IEC JTC 1/SC 27 · 2016 (en revisión; 3.ª edición en DIS). Referencia de medición para ISO/IEC 27001, cláusula 9.1. <https://www.iso.org/standard/64120.html>
- **F04** · CIS Critical Security Controls v8.1 · Center for Internet Security · Junio de 2024. Columna CIS; IG1 = 56 salvaguardas (153 en total). <https://www.cisecurity.org/controls/v8-1>
- **F05** · ISO/IEC 27001:2022, Anexo A y cláusulas 4 a 10 · ISO/IEC JTC 1/SC 27 · 2022. Columna ISO/IEC 27001 (correspondencia editorial). <https://www.iso.org/standard/27001>
- **F06** · CISA Cross-Sector Cybersecurity Performance Goals 2.0 · CISA · 11-12-2025. Metas mínimas alineadas a CSF 2.0 (K22, K33). <https://www.cisa.gov/cybersecurity-performance-goals-2-0-cpg-2-0>
- **F07** · DOE C2M2 v2.1 · DOE CESER · Junio de 2022. Correspondencia de estadios con MIL0–MIL3. <https://www.energy.gov/ceser/cybersecurity-capability-maturity-model-c2m2>
- **F08** · Serie ISA/IEC 62443 (2-1:2024, 3-2:2020, 3-3:2013, 2-4:2023, 4-1:2018) · IEC TC 65 / ISA99 · 2013–2024. SL-T/SL-A (K40), zonas y conductos (K36), modelo de madurez ML1–ML4. <https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards>
- **F09** · NERC CIP Reliability Standards · NERC / FERC · Vigentes al 9-11-2026. Generación eléctrica (Norteamérica); CIP-015 exigible desde 2028. <https://www.nerc.com/standards/reliability-standards/cip>
- **F10** · TSA Security Directives Pipeline-2021-01G y 2021-02 (02G) · TSA · 2026. Oil & gas (ductos): reporte a CISA ≤ 72 h; segmentación IT/OT. <https://www.tsa.gov/sites/default/files/signed_security-directive-pipeline-2021-01g-and-transmittal-memo_508c.pdf>
- **F11** · API Standard 1164, 3.ª edición · American Petroleum Institute · Agosto de 2021. Ciberseguridad de sistemas de control de ductos. <https://www.apiwebstore.org/standards/1164>
- **F12** · Directiva NIS2 (UE) 2022/2555 · Unión Europea · DO L 333, 27-12-2022. Plazos 24 h / 72 h / 1 mes; art. 20 (órgano de dirección). <https://eur-lex.europa.eu/eli/dir/2022/2555/oj>
- **F13** · DORA (UE) 2022/2554 y Reglamento Delegado (UE) 2025/301 · Unión Europea · Aplica desde el 17-1-2025. Plazos 4 h / 72 h / 1 mes; TLPT cada 3 años; terceros TIC. <https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32022R2554>
- **F14** · Cyber Resilience Act (UE) 2024/2847 · Unión Europea · Art. 14 desde el 11-9-2026. Industrial: notificación de vulnerabilidades explotadas e incidentes graves. <https://eur-lex.europa.eu/eli/reg/2024/2847/oj>
- **F15** · Reglamento de IA (UE) 2024/1689 y Reglamento (UE) 2026/1744 · Unión Europea · En vigor desde el 27-7-2026 (modificación). Fechas de aplicación de alto riesgo postergadas; supervisión humana (art. 14). <https://eur-lex.europa.eu/eli/reg/2026/1744/oj/eng>
- **F16** · ISO/IEC 42001:2023; NIST AI 100-1 (AI RMF 1.0); NIST AI 600-1 · ISO/IEC; NIST · 2023–2024. KPIs de T07 (inventario, autoridad, evaluación, red teaming). <https://doi.org/10.6028/NIST.AI.600-1>
- **F17** · BCBS Principles for operational resilience (d516) · Banco de Pagos Internacionales · 31-3-2021. Resiliencia operacional en banca. <https://www.bis.org/bcbs/publ/d516.htm>
- **F18** · BCRA Com. «A» 7724 y «A» 8280 · BCRA · 2023 y 2025. Financiero Argentina: notificación ≤ 1 h; métricas y umbrales. <https://www.bcra.gob.ar/archivos/Pdfs/comytexord/A7724.pdf>
- **F19** · SFC Circular Externa 007 de 2018 (CBJ) · SFC Colombia · 2018; CBJ 2025. Financiero Colombia: TUIC y Formato 408. <https://www.superfinanciera.gov.co/>
- **F20** · SBS Resolución 504-2021 · SBS Perú · 19-2-2021. Financiero Perú. <https://busquedas.elperuano.pe/dispositivo/NL/1929393-1>
- **F21** · CMF RAN 20-10 y 20-8 (NCG 515) · CMF Chile · 2020 y 2024. Financiero Chile: reporte ≤ 30 minutos. <https://www.cmfchile.cl/portal/normativa/624/w4-article-105471.html>
- **F22** · CNBV, Disposiciones aplicables a las instituciones de crédito (arts. 168 Bis 11 a 17) · CNBV México · Vigente. Financiero México (plazos no verificados). <https://www.cnbv.gob.mx/Normatividad/Disposiciones%20de%20car%C3%A1cter%20general%20aplicables%20a%20las%20instituciones%20de%20cr%C3%A9dito.pdf>
- **F23** · PCI DSS v4.0.1 · PCI SSC · 11-6-2024. Requisitos con fecha futura obligatorios desde el 31-3-2025. <https://blog.pcisecuritystandards.org/just-published-pci-dss-v4-0-1>
- **F24** · Swift CSCF v2026 · Swift · Julio de 2025. Atestación anual. <https://www.swift.com/myswift/customer-security-programme/understand-controls>
- **F25** · SEC, Cybersecurity Risk Management, Strategy, Governance, and Incident Disclosure · SEC · 26-7-2023. 8-K Item 1.05 (4 días hábiles); Reg. S-K Item 106. <https://www.sec.gov/rules-regulations/2023/07/s7-09-22>
- **F26** · Ley 21.663 Marco de Ciberseguridad · Chile · DO 8-4-2024. Plazos 3 h / 72 h (24 h OIV) / 15 días. <https://www.bcn.cl/leychile/navegar?idNorma=1202434>
- **F27** · Ley 21.719 de Protección de Datos Personales · Chile · DO 13-12-2024; vigencia 1-12-2026. Privacidad (K64). <https://www.bcn.cl/leychile/navegar?idNorma=1209272>
- **F28** · Decisión Administrativa 641/2021 · Argentina, JGM · BO 28-6-2021. Gobierno Argentina. <https://www.boletinoficial.gob.ar/detalleAviso/primera/246104/20210628>
- **F29** · CONPES 3995 y MSPI v5.0 · Colombia · 2020 y 2025. Gobierno Colombia. <https://normograma.mintic.gov.co/mintic/compilacion/docs/resolucion_mintic_2277_2025.htm>
- **F30** · LFPDPPP (México, 2025) · México · DOF 20-3-2025. Privacidad (K64). <https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPDPPP.pdf>
- **F31** · CISA BOD 26-04 (reemplaza a la BOD 22-01) · CISA · 10-6-2026. K46: priorización por exposición y estado KEV. <https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk>
- **F32** · Estándar de Ciberseguridad para el Sector Eléctrico · Coordinador Eléctrico Nacional (Chile) · Octubre de 2022. Generación eléctrica Chile: incidente reportable ≤ 1 h. <https://www.coordinador.cl/wp-content/uploads/2024/08/Estandar-Ciberseguridad-SEN-Octubre-2022.pdf>
- **F33** · Acuerdos CNO 1960 de 2025 y 2188 de 2026 · CNO Colombia · 2025–2026. Generación eléctrica Colombia. <https://www.cno.org.co/calendar-ciberseguridad-acuerdos>
- **F34** · Código de Red (RES/550/2021) y Manual TIC SEN-MEM · CRE/CNE y SENER (México) · 2021 y 2017. Generación eléctrica México (sin norma específica). <https://dof.gob.mx/2021/CRE/CRE_311221.pdf>
- **F35** · ISO/IEC 27019:2024 · ISO/IEC JTC 1/SC 27 · Octubre de 2024. Controles para energía. <https://www.iso.org/standard/85056.html>
- **F36** · OMI MSC.428(98) y MSC-FAL.1/Circ.3/Rev.4 · OMI · 2017 y 2026. Logística marítima. <https://www.imo.org/en/OurWork/Security/Pages/Cyber-security.aspx>
- **F37** · ISO 28000:2022 · ISO/TC 292 · Marzo de 2022. Seguridad de la cadena de suministro. <https://www.iso.org/standard/79612.html>
- **F38** · Marco SAFE de la OMA, edición 2025 · Organización Mundial de Aduanas · Junio de 2025. Operador Económico Autorizado y seguridad de la información. <https://www.wcoomd.org/en/media/newsroom/2025/september/responding-to-emerging-challenges-and-paving-the-way-for-a-secure.aspx>
- **F39** · MITRE ATT&CK v20.1 (Enterprise e ICS) · MITRE · 13-10-2026. K43: técnicas priorizadas. <https://attack.mitre.org/resources/versions/>
- **F40** · Open FAIR: O-RT 3.1 y O-RA 2.1 · The Open Group · Mayo de 2025. Cuantificación de riesgo (K19, K26). <https://www.opengroup.org/open-fair>
- **F41** · Brier, G. W. (1950), Verification of forecasts expressed in terms of probability, Monthly Weather Review 78(1) · American Meteorological Society · Enero de 1950. K01 (calibración del juicio). <https://journals.ametsoc.org/view/journals/mwre/78/1/1520-0493_1950_078_0001_vofeit_2_0_co_2.xml>
- **F42** · Gartner, Top Cybersecurity Trends for 2024 (métricas orientadas a resultados) · Gartner · 22-2-2024. Enfoque de métricas orientadas a resultados y acuerdos de nivel de protección (K19, K58). <https://www.gartner.com/en/newsroom/press-releases/2024-02-22-gartner-identifies-top-cybersecurity-trends-for-2024>
- **F43** · Microsoft Work Trend Index 2025, The Year the Frontier Firm Is Born · Microsoft WorkLab · 23-4-2025. Concepto de empresa de frontera, equipos humano-agente, «agent boss» y relación humano-agente (K50). <https://www.microsoft.com/en-us/worklab/work-trend-index/2025-the-year-the-frontier-firm-is-born>
- **F44** · IBM Cost of a Data Breach Report 2025 · IBM / Ponemon · 30-7-2025. Contexto: USD 4,44 M; 241 días; 13% de brechas en IA y 97% sin controles de acceso. <https://newsroom.ibm.com/2025-07-30-ibm-report-13-of-organizations-reported-breaches-of-ai-models-or-applications,-97-of-which-reported-lacking-proper-ai-access-controls>
- **F45** · Verizon 2026 Data Breach Investigations Report · Verizon · 19-5-2026. Contexto: explotación 31% (LAC 44%); terceros 48% (LAC 74%); KEV 26% remediadas, mediana 43 días. <https://www.verizon.com/business/resources/reports/dbir/>
- **F46** · Microsoft Digital Defense Report 2025 · Microsoft · 16-10-2025. Contexto: la MFA bloquea más del 99% de los ataques de identidad (K33). <https://blogs.microsoft.com/on-the-issues/2025/10/16/mddr-2025/>
- **F47** · AI CISO Atlas, Taxonomía 5.3 y Core Ontology 1.0 · Proyecto AI CISO Atlas · 2026. Territorios, dominios, funciones, 32 subfunciones; entidades y relaciones.
- **F48** · TheNextCISO GM-24, Documento Maestro · Proyecto TheNextCISO · Noviembre de 2026. Plano Gobierno/Gestión y 24 unidades G1.1–M6.2.

---
@SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre de 2026

# TheNextCISO GM-24 — Pre-ensayos (archivos de inicialización), lote PA-02 (V7.1)

> **GM-24 V7.1 · The Next CISO + Sub-plan PO-GAC** · 2026-11-14. Catálogo: 379 conceptos (245 K · 52 AMP · 40 HC · 42 PA), todos con pre-ensayo íntegro y mapeados a 17 marcos (NIST/ISACA/MITRE/OWASP/CIS/CSA). V7.1 = ChangeSet editorial CS-GM24-V7.1-001 (4 títulos generalizados; sin cambio de IDs, cantidad ni mapeo). Plano A (corpus académico). Referencias DD/K4x/R/eo:OP/COE: marco interno.

**Estado:** ideas centrales para desarrollo editorial; IDs curriculares (asignar `ESS-######` desde el registro SQLite). Estructura de los lotes GM-24 + práctica, próximos pasos y relación con la unidad.

## Inventario

| N.º | ID | Tipo | Unidad | Concepto |
|---|---|---|---|---|
| 025 | M3.2-PA01 | PA | M3.2 | El control como producto: objetivo → configuración → evidencia |
| 026 | M3.2-PA02 | PA | M3.2 | Catálogo de controles de gobierno y gestión de agentes (AGC) |
| 027 | M3.2-PA03 | PA | M3.2 | Evaluación de calidad de agentes: datasets dorados, regresión y criterios de aceptación |
| 028 | M4.1-PA01 | PA | M4.1 | Modelo operativo del producto-control por cadencias (instancias: Defender for Office 365 · Defender XDR · Defender for Endpoint · Defender for Identity/Entra · Purview · Sentinel · Defender for Cloud) |
| 029 | M4.1-PA02 | PA | M4.1 | Gestión de incidentes y alertas en Defender XDR |
| 030 | M4.1-PA03 | PA | M4.1 | Gestión de la calidad de detección del dominio: FP/FN, tuning, listas, indicadores y supresiones (instancias: MDO · XDR · MDE · MDI/ID Protection · Purview DLP · Sentinel) |
| 031 | M4.1-PA04 | PA | M4.1 | Hunting y detecciones personalizadas |
| 032 | M4.1-PA05 | PA | M4.1 | Observabilidad de la flota de agentes: telemetría, trazas y tableros |
| 033 | M4.1-PA06 | PA | M4.1 | Gestión del desempeño de agentes: revisión periódica y drift |
| 034 | M4.2-PA01 | PA | M4.2 | Amenazas del dominio Zero Trust (instancias: correo y colaboración · cross-domain · endpoints · identidades · datos) |
| 035 | M4.2-PA02 | PA | M4.2 | Catálogos de amenazas a sistemas agénticos aplicados a la flota |
| 036 | M5.1-PA01 | PA | M5.1 | Playbooks de incidentes de correo con roles humano/agente |
| 037 | M5.2-PA01 | PA | M5.2 | Ejecución de respuesta en correo: AIR, acciones manuales y acciones de agentes con aprobación |
| 038 | M5.2-PA02 | PA | M5.2 | Mejora gobernada de agentes: del post-mortem al ChangeSet con regresión |
| 039 | M6.1-PA01 | PA | M6.1 | Operación degradada del SOC sin agentes ni modelos |
| 040 | M6.2-PA01 | PA | M6.2 | Plataformas y rutas de construcción de agentes y responsabilidad compartida en IA |
| 041 | M6.2-PA02 | PA | M6.2 | AgentOps / ALM de agentes |
| 042 | M6.2-PA03 | PA | M6.2 | Bases multiplataforma, multicloud y multimodelo |

---

### 025. M3.2-PA01 — El control como producto: objetivo → configuración → evidencia

**Unidad:** M3.2 Selección, Implementación y Evaluación de Controles · **Tipo:** PA · **Horas (sub-plan):** 4 · **Competencias:** C1.1, C2.4 · **Origen:** M3.2-PA01 (V5) · **Extensión:** 253 palabras · **Estado:** Idea central desarrollada (lote PA-01/02) — sub-plan PO-GAC; ID curricular, no ESS.

**Definición / idea central.** Cadena que une objetivo de control, configuración concreta y evidencia de operación efectiva, con owner continuo.

**Brecha frente a los 331.** K01/K09 y HC-018 sin ownership continuo ni cadena explícita.

**Tesis y sentido para el rol.** Un control es efectivo cuando su objetivo, su configuración y su evidencia forman una cadena verificable: el objetivo dice qué se quiere lograr, la configuración dice cómo se realiza y la evidencia demuestra que opera. M3.2-K01 y K09 tratan controles y pruebas; HC-018 la observabilidad; este concepto agrega el ownership continuo como condición: alguien es dueño de la cadena completa y la revisa. La tesis es que pensar el control como producto es exactamente eso: ser dueño de la cadena objetivo → configuración → evidencia y de su mejora.

**Tensión y límites.** La tensión es que las tres piezas viven en lugares distintos y con dueños distintos: el objetivo en la política, la configuración en la consola, la evidencia en informes que nadie conecta con el objetivo. El resultado es un control "implementado" cuya efectividad nadie puede afirmar. El ensayo debe mostrar un caso en el que la configuración cumple y el objetivo no.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: ISO 27001 y NIST RMF (Implement/Assess). Implementación: documentar la cadena para cinco controles de Defender for Office 365 (anti-phishing con impersonación, Safe Links, Safe Attachments, ZAP, autenticación DMARC) con objetivo, configuración concreta, evidencia de operación, KPI y owner.

**Evidencia y evaluación.** Evidencia: tabla objetivo → configuración → evidencia para cinco controles. Se evalúa que la evidencia pruebe el objetivo y no solo la configuración, y que cada fila tenga un owner y un KPI.

**Puentes.** Instancia M3.2-K01 (controles de seguridad); se relaciona con K09 (pruebas de efectividad); se apoya en HC-018. Es el núcleo de la competencia C1.1 y de la ficha de producto-control.

**Recomendaciones de práctica y ejercitación.**
1. Documentar la cadena objetivo → configuración → evidencia → KPI → owner para cinco controles de Defender for Office 365.
2. Buscar un caso en el que la configuración cumple y el objetivo no (p. ej., un override que permite lo que el objetivo prohíbe) y documentarlo.
3. Redactar la ficha de producto-control del dominio usando las cinco cadenas.

**Aplicación en el escenario de referencia.** Base agnóstica: ISO 27001; NIST RMF Implement/Assess. Implementación Microsoft: Presets Standard/Strict, Configuration Analyzer, informes como evidencia. Actividad: Documentar la cadena para 5 controles de MDO. Evidencia: Tabla objetivo→config→evidencia.

**Próximos pasos.**
- Incorporar las cadenas al tablero de KPIs del control (C1.4).
- Conectar con el control continuo de deriva (G3.2-PA01).
- Revisar la cadena cuando cambie una política o el baseline.

**Relación con los conceptos de la(s) unidad(es) M3.2.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M3.2-K01 | K | Controles de Seguridad | INSTANCIA_DE |
| M3.2-K02 | K | NIST SP 800-53 | misma unidad |
| M3.2-K03 | K | Selección y Adaptación | misma unidad |
| M3.2-K04 | K | Evaluación (Assess) | misma unidad |
| M3.2-K05 | K | Implementación | misma unidad |
| M3.2-K06 | K | Pentesting | misma unidad |
| M3.2-K07 | K | Controles Compensatorios | misma unidad |
| M3.2-K08 | K | Familias de Controles | misma unidad |
| M3.2-K09 | K | Pruebas de Efectividad | SE_RELACIONA |
| M3.2-K10 | K | POA&M | misma unidad |
| AMP-37 | AMP | Evaluación adversarial de agentes | misma unidad |
| AMP-38 | AMP | Pruebas de controles autónomos | misma unidad |
| HC-002 | HC | Apetito de riesgo convertido en arquitectura | misma unidad |
| HC-003 | HC | Riesgo residual y aceptación verificable | misma unidad |
| HC-004 | HC | Política como código gobernado | misma unidad |
| HC-005 | HC | Cumplimiento continuo orientado a resultados | misma unidad |
| HC-015 | HC | Gobierno y operación de Zero Trust | misma unidad |
| HC-018 | HC | Observabilidad y aseguramiento de controles | SE_APOYA_EN |
| HC-028 | HC | Gestión de excepciones y compensaciones | misma unidad |
| HC-031 | HC | Seguridad del software y confianza en componentes | misma unidad |
| HC-032 | HC | Evaluación adversarial de sistemas autónomos | misma unidad |
| HC-034 | HC | Decisiones reversibles y riesgo de transición | misma unidad |
| HC-036 | HC | Portafolio de controles y capacidades | misma unidad |
| HC-038 | HC | Aseguramiento de la arquitectura Zero Trust | misma unidad |
| AMP-52 | AMP | Content safety y riesgos de contenido generado | misma unidad |
| M3.2-PA02 | PA | Catálogo de controles de gobierno y gestión de agentes (AGC) | misma unidad |
| M3.2-PA03 | PA | Evaluación de calidad de agentes: datasets dorados, regresión y criterios de aceptación | misma unidad |

**Pregunta generadora:** Para cada control que su organización declara implementado, ¿qué evidencia demuestra que logra su objetivo, y no solo que está configurado?

---

### 026. M3.2-PA02 — Catálogo de controles de gobierno y gestión de agentes (AGC)

**Unidad:** M3.2 Selección, Implementación y Evaluación de Controles · **Tipo:** PA · **Horas (sub-plan):** 5 · **Competencias:** C5.1, C5.5 · **Origen:** M3.2-PA02 (V5) · **Referencias por ID (V7-C09):** CSA AI Controls Matrix v1.1 (AIS-11, IAM-19, MDS); NIST AI RMF 1.0 + AI 600-1; ISO/IEC 42001:2023 Anexo A · **Extensión:** 272 palabras · **Estado:** Idea central desarrollada (lote PA-01/02) — sub-plan PO-GAC; ID curricular, no ESS.

**Definición / idea central.** 24 controles mapeados a AI RMF, ISO 42001 y OWASP con implementación Microsoft y base agnóstica.

**Brecha frente a los 331.** No existe catálogo de controles para agentes.

**Tesis y sentido para el rol.** Los controles clásicos tienen catálogos (SP 800-53, ISO 27001 Anexo A); los agentes no los tenían. El catálogo AGC propone veinticuatro controles de gobierno y gestión de agentes organizados por capas —dirección y accountability, política y registro, identidad y acceso, datos y guardrails, operación y evidencia— cada uno con objetivo, mapeo a AI RMF e ISO/IEC 42001, amenaza OWASP que mitiga, implementación Microsoft, base agnóstica, evidencia y responsable. HC-010 distingue capacidad, permiso, delegación y ejecución; AMP-06 y AMP-38 fijan gobierno y pruebas; el catálogo los convierte en controles seleccionables. La tesis es que un owner debe poder evaluar su flota contra un catálogo, como evalúa su control contra el Anexo A.

**Tensión y límites.** La tensión es la madurez: el catálogo es una propuesta del sub-plan, no una norma, y debe presentarse así; su valor está en la trazabilidad a marcos públicos y en la implementación concreta. Otra tensión es la selección: aplicar los veinticuatro controles a un agente que solo genera informes es desproporcionado. El ensayo debe mostrar cómo seleccionar y adaptar (M3.2-K03) según nivel de autonomía y datos que toca.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: AI RMF, ISO/IEC 42001, OWASP, CSA AICM (AIS-11, IAM-19 como controles agénticos nombrados). Implementación: evaluar los quince agentes del catálogo contra los veinticuatro AGC, marcando implementado, parcial, no aplica o pendiente, con la evidencia disponible en el tenant y un plan de cierre.

**Evidencia y evaluación.** Evidencia: evaluación de la flota contra los AGC con plan de cierre. Se evalúa la proporcionalidad de la selección, la calidad de la evidencia citada y la consistencia con las fichas.

**Puentes.** Instancia M3.2-K03 (selección y adaptación); operacionaliza HC-010 y AMP-06; se relaciona con AMP-38. Documento 05 del sub-plan.

**Recomendaciones de práctica y ejercitación.**
1. Evaluar los 15 agentes contra los 24 AGC (implementado / parcial / no aplica / pendiente) con evidencia del tenant.
2. Aplicar un criterio de selección proporcional por nivel de autonomía y datos que toca; justificar los 'no aplica'.
3. Construir el plan de cierre y decidir qué agente debería pausarse hasta cumplir.

**Aplicación en el escenario de referencia.** Base agnóstica: AI RMF; ISO/IEC 42001; OWASP. Implementación Microsoft: 24 AGC del sub-plan. Actividad: Evaluar la flota contra los 24 AGC. Evidencia: Evaluación.

**Próximos pasos.**
- Mapear los AGC a AI RMF, ISO 42001 y CSA AICM (G2.1-PA02) y a la matriz de estándares del programa.
- Usar la evaluación como pieza del expediente ATO (AMP-22).
- Revisar el catálogo cuando cambien OWASP/AICM.

**Relación con los conceptos de la(s) unidad(es) M3.2.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M3.2-K01 | K | Controles de Seguridad | misma unidad |
| M3.2-K02 | K | NIST SP 800-53 | misma unidad |
| M3.2-K03 | K | Selección y Adaptación | INSTANCIA_DE |
| M3.2-K04 | K | Evaluación (Assess) | misma unidad |
| M3.2-K05 | K | Implementación | misma unidad |
| M3.2-K06 | K | Pentesting | misma unidad |
| M3.2-K07 | K | Controles Compensatorios | misma unidad |
| M3.2-K08 | K | Familias de Controles | misma unidad |
| M3.2-K09 | K | Pruebas de Efectividad | misma unidad |
| M3.2-K10 | K | POA&M | misma unidad |
| AMP-37 | AMP | Evaluación adversarial de agentes | misma unidad |
| AMP-38 | AMP | Pruebas de controles autónomos | SE_RELACIONA |
| HC-002 | HC | Apetito de riesgo convertido en arquitectura | misma unidad |
| HC-003 | HC | Riesgo residual y aceptación verificable | misma unidad |
| HC-004 | HC | Política como código gobernado | misma unidad |
| HC-005 | HC | Cumplimiento continuo orientado a resultados | misma unidad |
| HC-015 | HC | Gobierno y operación de Zero Trust | misma unidad |
| HC-018 | HC | Observabilidad y aseguramiento de controles | misma unidad |
| HC-028 | HC | Gestión de excepciones y compensaciones | misma unidad |
| HC-031 | HC | Seguridad del software y confianza en componentes | misma unidad |
| HC-032 | HC | Evaluación adversarial de sistemas autónomos | misma unidad |
| HC-034 | HC | Decisiones reversibles y riesgo de transición | misma unidad |
| HC-036 | HC | Portafolio de controles y capacidades | misma unidad |
| HC-038 | HC | Aseguramiento de la arquitectura Zero Trust | misma unidad |
| AMP-52 | AMP | Content safety y riesgos de contenido generado | misma unidad |
| M3.2-PA01 | PA | El control como producto: objetivo → configuración → evidencia | misma unidad |
| M3.2-PA03 | PA | Evaluación de calidad de agentes: datasets dorados, regresión y criterios de aceptación | misma unidad |
| HC-010 | HC | Autonomía delegada y límites de acción | OPERACIONALIZA (otra unidad) |
| AMP-06 | AMP | Gobierno de la IA | OPERACIONALIZA (otra unidad) |

**Pregunta generadora:** ¿Qué control del catálogo AGC su flota no cumple hoy, y qué agente debería pausar hasta cumplirlo?

---

### 027. M3.2-PA03 — Evaluación de calidad de agentes: datasets dorados, regresión y criterios de aceptación

**Unidad:** M3.2 Selección, Implementación y Evaluación de Controles · **Tipo:** PA · **Horas (sub-plan):** 4 · **Competencias:** C4.5 · **Origen:** M3.2-PA03 (V5) · **Extensión:** 265 palabras · **Estado:** Idea central desarrollada (lote PA-01/02) — sub-plan PO-GAC; ID curricular, no ESS.

**Definición / idea central.** Evaluación funcional con datasets dorados, regresión por versión y criterios de aceptación.

**Brecha frente a los 331.** AMP-37/38 cubren lo adversarial y las pruebas de controles autónomos; falta la calidad funcional.

**Tesis y sentido para el rol.** Antes de confiar en un agente hay que medir si hace bien su trabajo, no solo si resiste ataques. La evaluación de calidad usa un dataset dorado, métricas de precisión, utilidad y consistencia, pruebas de regresión que se repiten en cada versión y criterios de aceptación acordados antes de medir. AMP-37 cubre la evaluación adversarial y AMP-38 las pruebas de controles autónomos; este concepto completa el "Assess" del agente con la dimensión funcional. La tesis es que sin dataset dorado la revisión de desempeño (M4.1-PA06) no tiene línea base y la mejora gobernada (M5.2-PA02) no puede demostrar que un cambio mejoró algo.

**Tensión y límites.** La tensión es el costo de construir el dataset: requiere analistas senior que etiqueten incidentes reales, y esos incidentes cambian con las campañas. Otra tensión es la no determinación: el mismo prompt produce respuestas distintas; la evaluación debe medir distribuciones, no casos únicos. El ensayo debe discutir el tamaño mínimo razonable y cómo mantener el dataset vivo con los casos del propio runbook (MDO-D04).

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: testing de sistemas de IA y AI RMF MEASURE. Implementación: construir el dataset dorado de AG-01 (triaje) a partir de incidentes clasificados, definir métricas, ejecutar la evaluación con las herramientas de Foundry o las pruebas de Copilot Studio, fijar el criterio de aceptación (precisión ≥ 90 %) y repetirla en cada versión.

**Evidencia y evaluación.** Evidencia: dataset dorado documentado, informe de evaluación y criterio de aceptación. Se evalúa la representatividad del dataset, la repetibilidad y la conexión con KPI-11.

**Puentes.** Complementa AMP-37 y AMP-38; instancia M3.2-K04 (evaluación); se relaciona con M4.1-K08 (IA en SecOps). Sostiene AGC-12 y alimenta M4.1-PA06 y M5.2-PA02.

**Recomendaciones de práctica y ejercitación.**
1. Construir un dataset dorado de 50 incidentes clasificados para AG-01 (prioridad, clasificación, siguiente acción) con doble etiquetado.
2. Ejecutar la evaluación en Foundry o con pruebas de Copilot Studio midiendo distribuciones (varias corridas); fijar y defender el criterio de aceptación.
3. Diseñar el mecanismo para alimentar el dataset con los casos clasificados del runbook (MDO-D04).

**Aplicación en el escenario de referencia.** Base agnóstica: Testing de IA; AI RMF MEASURE. Implementación Microsoft: Evaluaciones de Foundry; pruebas en Copilot Studio. Actividad: Construir el dataset dorado y la evaluación de AG-01. Evidencia: Informe de evaluación.

**Próximos pasos.**
- Repetir la evaluación en cada versión (AGC-12/16) y registrar la línea base para M4.1-PA06.
- Combinar con la evaluación adversarial (AMP-37) en el expediente ATO.
- Extender el método a AG-03 y AG-10.

**Relación con los conceptos de la(s) unidad(es) M3.2.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M3.2-K01 | K | Controles de Seguridad | misma unidad |
| M3.2-K02 | K | NIST SP 800-53 | misma unidad |
| M3.2-K03 | K | Selección y Adaptación | misma unidad |
| M3.2-K04 | K | Evaluación (Assess) | INSTANCIA_DE |
| M3.2-K05 | K | Implementación | misma unidad |
| M3.2-K06 | K | Pentesting | misma unidad |
| M3.2-K07 | K | Controles Compensatorios | misma unidad |
| M3.2-K08 | K | Familias de Controles | misma unidad |
| M3.2-K09 | K | Pruebas de Efectividad | misma unidad |
| M3.2-K10 | K | POA&M | misma unidad |
| AMP-37 | AMP | Evaluación adversarial de agentes | COMPLEMENTA |
| AMP-38 | AMP | Pruebas de controles autónomos | COMPLEMENTA |
| HC-002 | HC | Apetito de riesgo convertido en arquitectura | misma unidad |
| HC-003 | HC | Riesgo residual y aceptación verificable | misma unidad |
| HC-004 | HC | Política como código gobernado | misma unidad |
| HC-005 | HC | Cumplimiento continuo orientado a resultados | misma unidad |
| HC-015 | HC | Gobierno y operación de Zero Trust | misma unidad |
| HC-018 | HC | Observabilidad y aseguramiento de controles | misma unidad |
| HC-028 | HC | Gestión de excepciones y compensaciones | misma unidad |
| HC-031 | HC | Seguridad del software y confianza en componentes | misma unidad |
| HC-032 | HC | Evaluación adversarial de sistemas autónomos | misma unidad |
| HC-034 | HC | Decisiones reversibles y riesgo de transición | misma unidad |
| HC-036 | HC | Portafolio de controles y capacidades | misma unidad |
| HC-038 | HC | Aseguramiento de la arquitectura Zero Trust | misma unidad |
| AMP-52 | AMP | Content safety y riesgos de contenido generado | misma unidad |
| M3.2-PA01 | PA | El control como producto: objetivo → configuración → evidencia | misma unidad |
| M3.2-PA02 | PA | Catálogo de controles de gobierno y gestión de agentes (AGC) | misma unidad |
| M4.1-K08 | K | IA en SecOps | SE_RELACIONA (otra unidad) |

**Pregunta generadora:** ¿Con cuántos casos etiquetados por sus mejores analistas evaluaría a un agente antes de dejarlo clasificar incidentes, y quién aceptaría el umbral?

---

### 028. M4.1-PA01 — Modelo operativo del producto-control por cadencias (instancias: Defender for Office 365 · Defender XDR · Defender for Endpoint · Defender for Identity/Entra · Purview · Sentinel · Defender for Cloud)

**Unidad:** M4.1 Operaciones de Seguridad, Monitorización e Inteligencia · **Tipo:** PA · **Horas (sub-plan):** 6 · **Competencias:** C3.1, C2.2 · **Origen:** M4.1-PA01 (V5) · **Título V7:** Modelo operativo de Defender for Office 365 en Defender XDR · **Extensión:** 333 palabras · **Estado:** Idea central desarrollada (lote PA-01/02) — PROMOVIDO al programa (V7-C04) — título generalizado (V7.1); ID curricular, no ESS.

**Definición / idea central.** Tareas diarias, semanales, mensuales, trimestrales y por evento con persona, evidencia y KPI; versión agnóstica (eo:OP).

**Brecha frente a los 331.** K01/K02 describen el SOC en general; no existe el modelo operativo de un control concreto.

**Tesis y sentido para el rol.** La guía de operaciones de seguridad de Defender for Office 365 y las tareas de mantenimiento del SOC de Defender XDR describen lo que un equipo debe hacer cada día, cada semana y ante eventos para que el control siga siendo efectivo: triar incidentes por prioridad, investigar y remediar, clasificar, enviar falsos positivos y negativos, gestionar listas y cuarentena, revisar campañas, tendencias, usuarios más atacados, Secure Score, anuncios de la plataforma, configuración y overrides. Este concepto convierte esa guía en el modelo operativo del producto-control: cada tarea con cadencia, persona responsable según el fabricante, función del CSF, práctica agnóstica que ejemplifica, nivel de autonomía recomendado y agente candidato. La tesis es que el modelo operativo es el objeto que el PO-GAC posee y mejora, y el mapa sobre el que decide qué delegar a agentes. En V7.1 el concepto se generaliza como modelo operativo del producto-control por cadencias; esta es su instancia de referencia (Defender for Office 365) y cada dominio tiene la suya.

**Tensión y límites.** La tensión es que la guía del fabricante describe tareas, no resultados: cumplir la lista no garantiza que el control proteja. Por eso cada tarea del modelo lleva un KPI y cada grupo de tareas se relee contra la cadena objetivo → configuración → evidencia (M3.2-PA01). Otra tensión es la propiedad de las tareas compartidas con la mesa de mensajería y el MDR: el modelo debe decir quién hace qué sin inventar una organización que no existe.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: MAEO e ITIL. Implementación: operar el runbook completo (31 tareas) durante dos semanas bajo supervisión, registrando evidencia por tarea y midiendo el cumplimiento de cadencias; identificar las tareas candidatas a los agentes AG-10, AG-03 y AG-05.

**Evidencia y evaluación.** Evidencia: bitácora de dos semanas con evidencia por tarea y un informe de cumplimiento de cadencias. Se evalúa la completitud, la calidad de la evidencia y la propuesta razonada de delegación.

**Puentes.** Instancia M4.1-K01 (SOC moderno) y K02 (monitorización continua); se relaciona con M1.1-K05 (ciclo de vida) y AMP-39 (SOC agéntico). Documento 04 del sub-plan.

**Recomendaciones de práctica y ejercitación.**
1. Operar el runbook de 31 tareas durante dos semanas en el entorno de prueba, registrando evidencia por tarea (capturas, decisiones, entradas con vencimiento, acciones del Action center).
2. Medir el cumplimiento de cadencias y el tiempo por tarea; identificar cuellos de botella.
3. Clasificar cada tarea por nivel de autonomía candidato (L0–L3) y asignar agente; justificar AG-10, AG-03 y AG-05 como primeros.

**Aplicación en el escenario de referencia.** Base agnóstica: MAEO; ITIL. Implementación Microsoft: Security Operations Guide de Defender for Office 365; tareas del SOC de Defender XDR. Actividad: Ejecutar dos semanas del runbook y documentar evidencia. Evidencia: Bitácora.

**Próximos pasos.**
- Formalizar el runbook como documento 04 con KPIs por tarea y persona responsable.
- Usar los tiempos medidos como línea base del KPI-18 (horas liberadas).
- Derivar las prácticas eo:OP (M1.1-PA03); instanciar en XDR, Endpoints, Identidades, Datos, SIEM y Nube.

**Relación con los conceptos de la(s) unidad(es) M4.1.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M4.1-K01 | K | SOC Moderno | INSTANCIA_DE |
| M4.1-K02 | K | Monitorización Continua | INSTANCIA_DE |
| M4.1-K03 | K | Threat Intelligence (CTI) | misma unidad |
| M4.1-K04 | K | SIEM | misma unidad |
| M4.1-K05 | K | SOAR | misma unidad |
| M4.1-K06 | K | XDR | misma unidad |
| M4.1-K07 | K | Threat Hunting | misma unidad |
| M4.1-K08 | K | IA en SecOps | misma unidad |
| M4.1-K09 | K | Ciclo Vida Inteligencia | misma unidad |
| M4.1-K10 | K | TTPs | misma unidad |
| AMP-39 | AMP | SOC agéntico | SE_RELACIONA |
| AMP-40 | AMP | Human-in-the-loop | misma unidad |
| HC-001 | HC | Gobierno de decisiones basadas en evidencia | misma unidad |
| HC-005 | HC | Cumplimiento continuo orientado a resultados | misma unidad |
| HC-010 | HC | Autonomía delegada y límites de acción | misma unidad |
| HC-012 | HC | Confianza verificable en decisiones de IA | misma unidad |
| HC-017 | HC | Inteligencia que modifica decisiones | misma unidad |
| HC-018 | HC | Observabilidad y aseguramiento de controles | misma unidad |
| HC-019 | HC | SOC agéntico con supervisión humana | misma unidad |
| HC-040 | HC | Homeostasis organizacional de seguridad | misma unidad |
| M4.1-K11 | K | Deception y señuelos como control detectivo | misma unidad |
| M4.1-PA02 | PA | Gestión de incidentes y alertas en Defender XDR | misma unidad |
| M4.1-PA03 | PA | Gestión de la calidad de detección del dominio: FP/FN, tuning, listas, indicadores y supresiones (instancias: MDO · XDR · MDE · MDI/ID Protection · Purview DLP · Sentinel) | misma unidad |
| M4.1-PA04 | PA | Hunting y detecciones personalizadas | misma unidad |
| M4.1-PA05 | PA | Observabilidad de la flota de agentes: telemetría, trazas y tableros | misma unidad |
| M4.1-PA06 | PA | Gestión del desempeño de agentes: revisión periódica y drift | misma unidad |
| M1.1-K05 | K | Ciclo de Vida | SE_RELACIONA (otra unidad) |

**Pregunta generadora:** De las tareas diarias de la guía de operaciones de su control, ¿cuáles se hicieron ayer, quién puede probarlo y cuáles podría hacer mañana un agente sin que usted pierda el control?

> **Instancias de dominio (V7.1).** Este pre-ensayo desarrolla la instancia de referencia (productividad: Defender for Office 365). Las instancias XDR, Endpoints, Identidades, Datos, SIEM, Nube y Apps están en los paquetes `Dominio_*` (plano B), que no modifican este concepto.


---

### 029. M4.1-PA02 — Gestión de incidentes y alertas en Defender XDR

**Unidad:** M4.1 Operaciones de Seguridad, Monitorización e Inteligencia · **Tipo:** PA · **Horas (sub-plan):** 5 · **Competencias:** C2.2, C3.2 · **Origen:** M4.1-PA02 (V5) · **Extensión:** 293 palabras · **Estado:** Idea central desarrollada (lote PA-01/02) — sub-plan PO-GAC; ID curricular, no ESS.

**Definición / idea central.** Cola de incidentes, prioridad, investigación, AIR, Action center, clasificación y resolución.

**Brecha frente a los 331.** K06 y M5.1-K07 son genéricos.

**Tesis y sentido para el rol.** La cola de incidentes de Defender XDR es el lugar donde el control de correo se encuentra con el resto de la superficie: un incidente correlaciona alertas de correo, identidad y endpoint, y el analista decide prioridad, investiga, ejecuta o aprueba acciones (manuales o de la investigación y respuesta automatizadas), clasifica el incidente como verdadero o falso positivo con su tipo de amenaza y lo resuelve. La guía del fabricante propone un orden de prioridad para alertas de correo que el owner debe conocer y que se convierte en la primera instrucción del agente de triaje. La tesis es que la operación concreta de la plataforma —no la teoría del XDR de M4.1-K06— es lo que hace confiable al analista y, después, al agente que lo asiste.

**Tensión y límites.** La tensión es la higiene: incidentes abiertos que envejecen, clasificaciones inconsistentes que arruinan el dataset dorado, alertas cerradas sin acción. Otra tensión es la correlación: un incidente de correo puede ser la primera señal de un compromiso de identidad, y cerrarlo como "spam" pierde el hilo. El ensayo debe discutir cómo la clasificación disciplinada (MDO-D04) alimenta la mejora del control y la evaluación del agente.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: NIST SP 800-61. Implementación: triar veinte incidentes de laboratorio en la cola de incidentes aplicando el orden de prioridad de la guía, usando la investigación automatizada y el Action center, clasificando con tipo de amenaza y escalando a ITSM los que corresponda; registrar el tiempo por incidente y las decisiones.

**Evidencia y evaluación.** Evidencia: bitácora de veinte incidentes con prioridad, acciones, clasificación y tiempo. Se evalúa la consistencia de las clasificaciones, el cumplimiento del SLA (KPI-01) y la calidad de la documentación.

**Puentes.** Instancia M4.1-K06 (XDR); se relaciona con M5.1-K07 (playbooks) y HC-019 (SOC agéntico). Tareas MDO-D01 a MDO-D04; base del agente AG-01.

**Recomendaciones de práctica y ejercitación.**
1. Triar 20 incidentes de laboratorio aplicando el orden de prioridad de la guía; registrar prioridad, acciones, clasificación, tipo de amenaza y tiempo.
2. Hacer que dos personas triajen los mismos 10 incidentes y medir el desacuerdo; derivar criterios de clasificación para la instrucción de AG-01.
3. Escalar dos incidentes a ITSM y verificar la trazabilidad (AG-15).

**Aplicación en el escenario de referencia.** Base agnóstica: NIST SP 800-61. Implementación Microsoft: Incidents queue, AIR, Action center. Actividad: Triar 20 incidentes de laboratorio. Evidencia: Bitácora.

**Próximos pasos.**
- Alimentar el dataset dorado de AG-01 (M3.2-PA03) con los incidentes clasificados.
- Medir KPI-01 y KPI-02 sobre la bitácora.
- Construir los playbooks híbridos (M5.1-PA01) sobre los casos reales.

**Relación con los conceptos de la(s) unidad(es) M4.1.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M4.1-K01 | K | SOC Moderno | misma unidad |
| M4.1-K02 | K | Monitorización Continua | misma unidad |
| M4.1-K03 | K | Threat Intelligence (CTI) | misma unidad |
| M4.1-K04 | K | SIEM | misma unidad |
| M4.1-K05 | K | SOAR | misma unidad |
| M4.1-K06 | K | XDR | INSTANCIA_DE |
| M4.1-K07 | K | Threat Hunting | misma unidad |
| M4.1-K08 | K | IA en SecOps | misma unidad |
| M4.1-K09 | K | Ciclo Vida Inteligencia | misma unidad |
| M4.1-K10 | K | TTPs | misma unidad |
| AMP-39 | AMP | SOC agéntico | misma unidad |
| AMP-40 | AMP | Human-in-the-loop | misma unidad |
| HC-001 | HC | Gobierno de decisiones basadas en evidencia | misma unidad |
| HC-005 | HC | Cumplimiento continuo orientado a resultados | misma unidad |
| HC-010 | HC | Autonomía delegada y límites de acción | misma unidad |
| HC-012 | HC | Confianza verificable en decisiones de IA | misma unidad |
| HC-017 | HC | Inteligencia que modifica decisiones | misma unidad |
| HC-018 | HC | Observabilidad y aseguramiento de controles | misma unidad |
| HC-019 | HC | SOC agéntico con supervisión humana | SE_RELACIONA |
| HC-040 | HC | Homeostasis organizacional de seguridad | misma unidad |
| M4.1-K11 | K | Deception y señuelos como control detectivo | misma unidad |
| M4.1-PA01 | PA | Modelo operativo del producto-control por cadencias (instancias: Defender for Office 365 · Defender XDR · Defender for Endpoint · Defender for Identity/Entra · Purview · Sentinel · Defender for Cloud) | misma unidad |
| M4.1-PA03 | PA | Gestión de la calidad de detección del dominio: FP/FN, tuning, listas, indicadores y supresiones (instancias: MDO · XDR · MDE · MDI/ID Protection · Purview DLP · Sentinel) | misma unidad |
| M4.1-PA04 | PA | Hunting y detecciones personalizadas | misma unidad |
| M4.1-PA05 | PA | Observabilidad de la flota de agentes: telemetría, trazas y tableros | misma unidad |
| M4.1-PA06 | PA | Gestión del desempeño de agentes: revisión periódica y drift | misma unidad |
| M5.1-K07 | K | Playbooks | SE_RELACIONA (otra unidad) |

**Pregunta generadora:** Si dos analistas triaran el mismo incidente de correo, ¿llegarían a la misma prioridad y clasificación, y qué pasaría con un agente entrenado con sus desacuerdos?

---

### 030. M4.1-PA03 — Gestión de la calidad de detección del dominio: FP/FN, tuning, listas, indicadores y supresiones (instancias: MDO · XDR · MDE · MDI/ID Protection · Purview DLP · Sentinel)

**Unidad:** M4.1 Operaciones de Seguridad, Monitorización e Inteligencia · **Tipo:** PA · **Horas (sub-plan):** 4 · **Competencias:** C2.3 · **Origen:** M4.1-PA03 (V5) · **Título V7:** Gestión de falsos positivos/negativos y listas · **Extensión:** 318 palabras · **Estado:** Idea central desarrollada (lote PA-01/02) — PROMOVIDO al programa (V7-C04) — título generalizado (V7.1); ID curricular, no ESS.

**Definición / idea central.** Submissions, Tenant Allow/Block List, cuarentena, mensajes reportados; causa raíz; precision/recall.

**Brecha frente a los 331.** No existe la gestión de calidad de detección de un control.

**Tesis y sentido para el rol.** La calidad de un control de detección se mide en dos errores: lo legítimo que bloquea (falsos positivos) y lo malicioso que deja pasar (falsos negativos). Gestionarlos es un ciclo: recibir mensajes reportados por usuarios y liberaciones de cuarentena, analizar la causa (veredicto del motor, configuración, override, lista), enviar la muestra al fabricante, agregar entradas de bloqueo con vencimiento, y ajustar la política cuando el patrón se repite. La tesis es que el owner debe tratar FP y FN como una métrica de producto (precision y recall) y no como tickets, y que HC-027 obliga a medirlos sin engañarse: una tasa de falsos positivos baja puede esconder un filtro permisivo. En V7.1 el concepto se generaliza como gestión de la calidad de detección del dominio; esta es su instancia de referencia.

**Tensión y límites.** La tensión es la presión por liberar: un ejecutivo que no recibe un correo pesa más que un phishing que nadie vio. La organización resuelve creando permisos amplios que luego nadie revisa (G2.2-PA03). Otra tensión es la atribución de causa: muchos falsos negativos no son fallas del motor sino overrides o configuración relajada; sin análisis de causa el envío al fabricante no mejora nada. El ensayo debe discutir el "allow" como la decisión más riesgosa del ciclo y por qué exige segunda aprobación.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: calidad de detección (precision/recall) y tuning. Implementación: analizar diez casos de falsos positivos y negativos con la página de envíos, la Tenant Allow/Block List y las políticas de cuarentena, documentando causa raíz, acción y vencimiento; proponer un cambio de política cuando el patrón se repita; definir el papel del agente AG-03 en L2.

**Evidencia y evaluación.** Evidencia: análisis de diez casos con causa raíz, acción y vencimiento, y propuesta de ajuste de política. Se evalúa la calidad del análisis de causa y la disciplina de vencimientos.

**Puentes.** Profundiza M4.1-K02 (monitorización continua); se apoya en HC-027 (métricas que no engañan). Tareas MDO-D05 a MDO-D08; KPI-04 y KPI-05.

**Recomendaciones de práctica y ejercitación.**
1. Analizar diez casos FP/FN (Submissions, TABL, cuarentena, reportes de usuarios) con causa raíz (motor / configuración / override / lista), acción y vencimiento.
2. Calcular precision y recall del período con los datos del entorno de prueba y discutir qué esconde cada cifra (HC-027).
3. Redactar la regla de 'allow con segunda aprobación' e incorporarla a la ficha de AG-03.

**Aplicación en el escenario de referencia.** Base agnóstica: Precision/recall; tuning. Implementación Microsoft: Submissions, TABL, Quarantine policies. Actividad: Analizar 10 casos FP/FN con causa raíz. Evidencia: Análisis.

**Próximos pasos.**
- Operar KPI-04 y KPI-05 semanalmente.
- Conectar los casos recurrentes con el procedimiento de excepciones (G2.2-PA03).
- Construir el dataset de casos FP/FN para evaluar a AG-03; instanciar en XDR, MDE, MDI y Purview.

**Relación con los conceptos de la(s) unidad(es) M4.1.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M4.1-K01 | K | SOC Moderno | misma unidad |
| M4.1-K02 | K | Monitorización Continua | PROFUNDIZA |
| M4.1-K03 | K | Threat Intelligence (CTI) | misma unidad |
| M4.1-K04 | K | SIEM | misma unidad |
| M4.1-K05 | K | SOAR | misma unidad |
| M4.1-K06 | K | XDR | misma unidad |
| M4.1-K07 | K | Threat Hunting | misma unidad |
| M4.1-K08 | K | IA en SecOps | misma unidad |
| M4.1-K09 | K | Ciclo Vida Inteligencia | misma unidad |
| M4.1-K10 | K | TTPs | misma unidad |
| AMP-39 | AMP | SOC agéntico | misma unidad |
| AMP-40 | AMP | Human-in-the-loop | misma unidad |
| HC-001 | HC | Gobierno de decisiones basadas en evidencia | misma unidad |
| HC-005 | HC | Cumplimiento continuo orientado a resultados | misma unidad |
| HC-010 | HC | Autonomía delegada y límites de acción | misma unidad |
| HC-012 | HC | Confianza verificable en decisiones de IA | misma unidad |
| HC-017 | HC | Inteligencia que modifica decisiones | misma unidad |
| HC-018 | HC | Observabilidad y aseguramiento de controles | misma unidad |
| HC-019 | HC | SOC agéntico con supervisión humana | misma unidad |
| HC-040 | HC | Homeostasis organizacional de seguridad | misma unidad |
| M4.1-K11 | K | Deception y señuelos como control detectivo | misma unidad |
| M4.1-PA01 | PA | Modelo operativo del producto-control por cadencias (instancias: Defender for Office 365 · Defender XDR · Defender for Endpoint · Defender for Identity/Entra · Purview · Sentinel · Defender for Cloud) | misma unidad |
| M4.1-PA02 | PA | Gestión de incidentes y alertas en Defender XDR | misma unidad |
| M4.1-PA04 | PA | Hunting y detecciones personalizadas | misma unidad |
| M4.1-PA05 | PA | Observabilidad de la flota de agentes: telemetría, trazas y tableros | misma unidad |
| M4.1-PA06 | PA | Gestión del desempeño de agentes: revisión periódica y drift | misma unidad |
| HC-027 | HC | Métricas que no engañan | SE_APOYA_EN (otra unidad) |

**Pregunta generadora:** ¿Cuántas de las entradas de permiso de su organización se crearon para resolver un falso positivo que hoy ya no existe, y cuántos falsos negativos han pasado por ellas?

> **Instancias de dominio (V7.1).** Este pre-ensayo desarrolla la instancia de referencia (productividad: Defender for Office 365). Las instancias XDR, Endpoints, Identidades, Datos, SIEM, Nube y Apps están en los paquetes `Dominio_*` (plano B), que no modifican este concepto.


---

### 031. M4.1-PA04 — Hunting y detecciones personalizadas

**Unidad:** M4.1 Operaciones de Seguridad, Monitorización e Inteligencia · **Tipo:** PA · **Horas (sub-plan):** 4 · **Competencias:** C2.2, C3.4 · **Origen:** M4.1-PA04 (V5) · **Extensión:** 248 palabras · **Estado:** Idea central desarrollada (lote PA-01/02) — sub-plan PO-GAC; ID curricular, no ESS.

**Definición / idea central.** Threat Explorer, Advanced Hunting (KQL), Threat analytics, consultas compartidas, Threat trackers y detecciones personalizadas.

**Brecha frente a los 331.** K07/K03 son conceptuales; falta la práctica con KQL y detection-as-code.

**Tesis y sentido para el rol.** Hunting es buscar lo que las detecciones no encontraron, con hipótesis y lenguaje de consulta; detection engineering es convertir lo encontrado en detecciones repetibles. En el control de correo, el hunting usa Threat Explorer, Advanced Hunting con KQL sobre tablas de correo y URL, Threat analytics como fuente de hipótesis, consultas compartidas y Threat trackers, y reglas de detección personalizadas para cerrar el ciclo. La tesis es que el owner debe dominar la práctica —no solo el concepto de M4.1-K07— porque las consultas y detecciones son el conocimiento operativo que luego alimenta a los agentes (AG-14) y porque una detección personalizada es un control con dueño.

**Tensión y límites.** La tensión es entre creatividad y disciplina: el hunting improvisado produce consultas que nadie documenta y detecciones ruidosas que nadie mantiene. La respuesta es tratar consultas y detecciones como código (versionadas, probadas, con dueño), lo que Sigma propone como referencia agnóstica. Otra tensión es el permiso: hunting sobre contenido de correo toca datos sensibles y requiere roles y propósito explícitos.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: detection engineering y detection-as-code (Sigma como referencia). Implementación: escribir cinco consultas KQL de hunting sobre correo y dos reglas de detección personalizadas, documentarlas y publicarlas como consultas compartidas en un repositorio versionado.

**Evidencia y evaluación.** Evidencia: repositorio con cinco consultas y dos detecciones documentadas, versionadas y con dueño. Se evalúa la utilidad de las hipótesis, la precisión de las detecciones y la calidad de la documentación.

**Puentes.** Instancia M4.1-K07 (threat hunting); se relaciona con M4.1-K03 (CTI). Tareas MDO-A02 a MDO-A04; base del agente AG-14.

**Recomendaciones de práctica y ejercitación.**
1. Escribir cinco consultas KQL de hunting sobre tablas de correo y URL (p. ej., clics en URL reescritas desde cuentas prioritarias, patrones de envío sospechosos) con hipótesis documentada.
2. Convertir dos hallazgos en reglas de detección personalizadas con dueño, prueba y versión.
3. Publicar las consultas como compartidas en un repositorio Git/SharePoint que sirva de knowledge source a AG-14.

**Aplicación en el escenario de referencia.** Base agnóstica: Detection engineering; Sigma. Implementación Microsoft: Advanced Hunting, custom detections, Threat trackers. Actividad: Escribir 5 consultas y 2 detecciones personalizadas. Evidencia: Repositorio.

**Próximos pasos.**
- Definir el proceso de curaduría y versionado de consultas (C3.4).
- Medir precisión de las detecciones creadas y retirarlas si son ruidosas.
- Explorar el servidor MCP de Sentinel como herramienta de AG-14 (ruta R3).

**Relación con los conceptos de la(s) unidad(es) M4.1.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M4.1-K01 | K | SOC Moderno | misma unidad |
| M4.1-K02 | K | Monitorización Continua | misma unidad |
| M4.1-K03 | K | Threat Intelligence (CTI) | SE_RELACIONA |
| M4.1-K04 | K | SIEM | misma unidad |
| M4.1-K05 | K | SOAR | misma unidad |
| M4.1-K06 | K | XDR | misma unidad |
| M4.1-K07 | K | Threat Hunting | INSTANCIA_DE |
| M4.1-K08 | K | IA en SecOps | misma unidad |
| M4.1-K09 | K | Ciclo Vida Inteligencia | misma unidad |
| M4.1-K10 | K | TTPs | misma unidad |
| AMP-39 | AMP | SOC agéntico | misma unidad |
| AMP-40 | AMP | Human-in-the-loop | misma unidad |
| HC-001 | HC | Gobierno de decisiones basadas en evidencia | misma unidad |
| HC-005 | HC | Cumplimiento continuo orientado a resultados | misma unidad |
| HC-010 | HC | Autonomía delegada y límites de acción | misma unidad |
| HC-012 | HC | Confianza verificable en decisiones de IA | misma unidad |
| HC-017 | HC | Inteligencia que modifica decisiones | misma unidad |
| HC-018 | HC | Observabilidad y aseguramiento de controles | misma unidad |
| HC-019 | HC | SOC agéntico con supervisión humana | misma unidad |
| HC-040 | HC | Homeostasis organizacional de seguridad | misma unidad |
| M4.1-K11 | K | Deception y señuelos como control detectivo | misma unidad |
| M4.1-PA01 | PA | Modelo operativo del producto-control por cadencias (instancias: Defender for Office 365 · Defender XDR · Defender for Endpoint · Defender for Identity/Entra · Purview · Sentinel · Defender for Cloud) | misma unidad |
| M4.1-PA02 | PA | Gestión de incidentes y alertas en Defender XDR | misma unidad |
| M4.1-PA03 | PA | Gestión de la calidad de detección del dominio: FP/FN, tuning, listas, indicadores y supresiones (instancias: MDO · XDR · MDE · MDI/ID Protection · Purview DLP · Sentinel) | misma unidad |
| M4.1-PA05 | PA | Observabilidad de la flota de agentes: telemetría, trazas y tableros | misma unidad |
| M4.1-PA06 | PA | Gestión del desempeño de agentes: revisión periódica y drift | misma unidad |

**Pregunta generadora:** ¿Qué hipótesis de hunting sobre su correo no ha probado nadie en seis meses, y qué detección personalizada nació de la última que sí se probó?

---

### 032. M4.1-PA05 — Observabilidad de la flota de agentes: telemetría, trazas y tableros

**Unidad:** M4.1 Operaciones de Seguridad, Monitorización e Inteligencia · **Tipo:** PA · **Horas (sub-plan):** 4 · **Competencias:** C6.3 · **Origen:** M4.1-PA06 (V5) · **Extensión:** 236 palabras · **Estado:** Idea central desarrollada (lote PA-01/02) — sub-plan PO-GAC; ID curricular, no ESS.

**Definición / idea central.** Telemetría, trazas, tableros y alertas de comportamiento de agentes integrados a la detección del SOC.

**Brecha frente a los 331.** HC-018 y AMP-45/46 no cubren la observabilidad operativa de agentes como flota.

**Tesis y sentido para el rol.** Un agente que no se observa no se gobierna. La observabilidad de la flota instrumenta tres cosas: telemetría, trazas y tableros con alertas de comportamiento. HC-018 trata la observabilidad de controles y AMP-45/46 la forense y la trazabilidad; este concepto los lleva a la operación: la flota como conjunto de servicios observables integrados a la detección del SOC. La tesis es que la observabilidad de agentes debe entrar en Sentinel como cualquier otra fuente, porque un agente comprometido es un incidente de seguridad.

**Tensión y límites.** La tensión es la fragmentación de señales: cada ruta de construcción emite telemetría distinta y Agent 365 la agrega parcialmente; normalizar exige esfuerzo y estándares (OpenTelemetry). Otra tensión es el volumen: registrar todo lo que un agente razona es caro; registrar poco impide la forense. El ensayo debe proponer qué se registra siempre, qué por muestreo y qué nunca.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: OpenTelemetry y LLM observability. Implementación: construir el tablero de la flota con tracing de Foundry o Application Insights, analíticas de Agent 365, logs de Copilot Studio y Sentinel, con tres alertas de comportamiento conectadas a la cola de incidentes; verificar que Defender para IA cubra los agentes del alcance.

**Evidencia y evaluación.** Evidencia: tablero operativo y tres alertas probadas. Se evalúa la cobertura (KPI-20), la integración con la detección y la decisión documentada sobre qué se registra.

**Puentes.** Profundiza HC-018; se apoya en AMP-46 (trazabilidad); se relaciona con AMP-45 (forense) y M4.1-K02. Sostiene AGC-11 y AGC-14.

**Recomendaciones de práctica y ejercitación.**
1. Definir el esquema de registro (siempre / por muestreo / nunca) para los 15 agentes y su ruta de construcción.
2. Construir el tablero de la flota (Foundry tracing o App Insights, Agent 365, logs de Copilot Studio, Sentinel) con tres alertas de comportamiento (herramienta fuera de allowlist, consumo por tarea > umbral, precisión < umbral).
3. Probar una alerta de punta a punta hasta la cola de incidentes y verificar quién la ve.

**Aplicación en el escenario de referencia.** Base agnóstica: OpenTelemetry; LLM observability. Implementación Microsoft: Foundry tracing, Sentinel, Agent 365 analytics, Defender para IA. Actividad: Construir el tablero de la flota con 3 alertas de comportamiento. Evidencia: Tablero.

**Próximos pasos.**
- Medir KPI-20 (cobertura de observabilidad) y cerrar brechas.
- Integrar los KRIs (G4.2-PA01) al tablero.
- Documentar los requisitos de telemetría forense (AMP-45) por agente.

**Relación con los conceptos de la(s) unidad(es) M4.1.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M4.1-K01 | K | SOC Moderno | misma unidad |
| M4.1-K02 | K | Monitorización Continua | SE_RELACIONA |
| M4.1-K03 | K | Threat Intelligence (CTI) | misma unidad |
| M4.1-K04 | K | SIEM | misma unidad |
| M4.1-K05 | K | SOAR | misma unidad |
| M4.1-K06 | K | XDR | misma unidad |
| M4.1-K07 | K | Threat Hunting | misma unidad |
| M4.1-K08 | K | IA en SecOps | misma unidad |
| M4.1-K09 | K | Ciclo Vida Inteligencia | misma unidad |
| M4.1-K10 | K | TTPs | misma unidad |
| AMP-39 | AMP | SOC agéntico | misma unidad |
| AMP-40 | AMP | Human-in-the-loop | misma unidad |
| HC-001 | HC | Gobierno de decisiones basadas en evidencia | misma unidad |
| HC-005 | HC | Cumplimiento continuo orientado a resultados | misma unidad |
| HC-010 | HC | Autonomía delegada y límites de acción | misma unidad |
| HC-012 | HC | Confianza verificable en decisiones de IA | misma unidad |
| HC-017 | HC | Inteligencia que modifica decisiones | misma unidad |
| HC-018 | HC | Observabilidad y aseguramiento de controles | PROFUNDIZA |
| HC-019 | HC | SOC agéntico con supervisión humana | misma unidad |
| HC-040 | HC | Homeostasis organizacional de seguridad | misma unidad |
| M4.1-K11 | K | Deception y señuelos como control detectivo | misma unidad |
| M4.1-PA01 | PA | Modelo operativo del producto-control por cadencias (instancias: Defender for Office 365 · Defender XDR · Defender for Endpoint · Defender for Identity/Entra · Purview · Sentinel · Defender for Cloud) | misma unidad |
| M4.1-PA02 | PA | Gestión de incidentes y alertas en Defender XDR | misma unidad |
| M4.1-PA03 | PA | Gestión de la calidad de detección del dominio: FP/FN, tuning, listas, indicadores y supresiones (instancias: MDO · XDR · MDE · MDI/ID Protection · Purview DLP · Sentinel) | misma unidad |
| M4.1-PA04 | PA | Hunting y detecciones personalizadas | misma unidad |
| M4.1-PA06 | PA | Gestión del desempeño de agentes: revisión periódica y drift | misma unidad |
| AMP-46 | AMP | Trazabilidad de decisiones autónomas | SE_APOYA_EN (otra unidad) |
| AMP-45 | AMP | Forense de agentes | SE_RELACIONA (otra unidad) |

**Pregunta generadora:** Si un agente de su flota empezara a actuar fuera de sus límites a las tres de la mañana, ¿qué alerta lo detectaría, en qué cola aparecería y quién la vería?

---

### 033. M4.1-PA06 — Gestión del desempeño de agentes: revisión periódica y drift

**Unidad:** M4.1 Operaciones de Seguridad, Monitorización e Inteligencia · **Tipo:** PA · **Horas (sub-plan):** 4 · **Competencias:** C6.2 · **Origen:** M4.1-PA07 (V5) · **Extensión:** 262 palabras · **Estado:** Idea central desarrollada (lote PA-01/02) — sub-plan PO-GAC; ID curricular, no ESS.

**Definición / idea central.** Revisión de calidad por muestreo, drift, retroalimentación y decisión de mantener/ajustar/pausar/retirar.

**Brecha frente a los 331.** AMP-39/26 no cubren la gestión de desempeño de trabajadores no humanos.

**Tesis y sentido para el rol.** Un agente tiene desempeño, y el desempeño se gestiona: se definen expectativas, se mide con regularidad, se revisa la calidad de decisiones por muestreo, se detecta deriva frente a la línea base del dataset dorado y se decide: mantener, ajustar, ampliar o reducir autonomía, pausar o retirar. AMP-39 propone medir el SOC agéntico y AMP-26 condiciona la supervisión efectiva a información, tiempo y autoridad. La tesis es que la revisión trimestral de desempeño de cada agente es el ritual que hace real la supervisión humana, y que su resultado puede cambiar el nivel de autonomía en cualquier dirección.

**Tensión y límites.** La tensión es antropomorfizar: un agente no mejora con feedback verbal, mejora con cambios versionados de instrucciones, conocimiento o herramientas (M5.2-PA02). Otra tensión es la deriva invisible: el agente mantiene sus métricas mientras cambian las amenazas, y su línea base queda obsoleta. El ensayo debe discutir cómo refrescar el dataset dorado y cómo evitar que la revisión se convierta en trámite.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: performance management y control estadístico de procesos. Implementación: conducir la revisión trimestral de un agente con la plantilla del sub-plan alimentada por muestreo de decisiones desde Sentinel, analíticas de Copilot Studio o Agent 365 y una evaluación en Foundry contra el dataset dorado; registrar la decisión y, si corresponde, el cambio de nivel de autonomía.

**Evidencia y evaluación.** Evidencia: informe de revisión trimestral con decisión firmada. Se evalúa la calidad del muestreo, la comparación con la línea base y la coherencia entre hallazgos y decisión.

**Puentes.** Profundiza AMP-39; se apoya en AMP-26 (supervisión humana efectiva) y se relaciona con AMP-40 (HITL). Tarea MDO-Q02; sostiene AGC-14.

**Recomendaciones de práctica y ejercitación.**
1. Conducir la revisión trimestral de AG-03 con la plantilla (resultados vs. metas, incidentes, costo, riesgo, cambios, decisión) sobre datos del entorno de prueba.
2. Muestrear 30 decisiones del agente y compararlas con la línea base del dataset dorado; estimar la deriva.
3. Redactar la decisión (mantener / ajustar / cambiar autonomía / pausar / retirar) y quién la firma.

**Aplicación en el escenario de referencia.** Base agnóstica: Performance management; SPC. Implementación Microsoft: Muestreo desde Sentinel; analíticas de Copilot Studio; evaluaciones periódicas en Foundry; Agent 365. Actividad: Conducir una revisión trimestral de desempeño de un agente. Evidencia: Informe.

**Próximos pasos.**
- Programar MDO-Q02 para toda la flota y conectar con AGC-14.
- Convertir los hallazgos en ChangeSets (M5.2-PA02).
- Refrescar el dataset dorado con los casos del trimestre (M3.2-PA03).

**Relación con los conceptos de la(s) unidad(es) M4.1.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M4.1-K01 | K | SOC Moderno | misma unidad |
| M4.1-K02 | K | Monitorización Continua | misma unidad |
| M4.1-K03 | K | Threat Intelligence (CTI) | misma unidad |
| M4.1-K04 | K | SIEM | misma unidad |
| M4.1-K05 | K | SOAR | misma unidad |
| M4.1-K06 | K | XDR | misma unidad |
| M4.1-K07 | K | Threat Hunting | misma unidad |
| M4.1-K08 | K | IA en SecOps | misma unidad |
| M4.1-K09 | K | Ciclo Vida Inteligencia | misma unidad |
| M4.1-K10 | K | TTPs | misma unidad |
| AMP-39 | AMP | SOC agéntico | PROFUNDIZA |
| AMP-40 | AMP | Human-in-the-loop | SE_RELACIONA |
| HC-001 | HC | Gobierno de decisiones basadas en evidencia | misma unidad |
| HC-005 | HC | Cumplimiento continuo orientado a resultados | misma unidad |
| HC-010 | HC | Autonomía delegada y límites de acción | misma unidad |
| HC-012 | HC | Confianza verificable en decisiones de IA | misma unidad |
| HC-017 | HC | Inteligencia que modifica decisiones | misma unidad |
| HC-018 | HC | Observabilidad y aseguramiento de controles | misma unidad |
| HC-019 | HC | SOC agéntico con supervisión humana | misma unidad |
| HC-040 | HC | Homeostasis organizacional de seguridad | misma unidad |
| M4.1-K11 | K | Deception y señuelos como control detectivo | misma unidad |
| M4.1-PA01 | PA | Modelo operativo del producto-control por cadencias (instancias: Defender for Office 365 · Defender XDR · Defender for Endpoint · Defender for Identity/Entra · Purview · Sentinel · Defender for Cloud) | misma unidad |
| M4.1-PA02 | PA | Gestión de incidentes y alertas en Defender XDR | misma unidad |
| M4.1-PA03 | PA | Gestión de la calidad de detección del dominio: FP/FN, tuning, listas, indicadores y supresiones (instancias: MDO · XDR · MDE · MDI/ID Protection · Purview DLP · Sentinel) | misma unidad |
| M4.1-PA04 | PA | Hunting y detecciones personalizadas | misma unidad |
| M4.1-PA05 | PA | Observabilidad de la flota de agentes: telemetría, trazas y tableros | misma unidad |
| AMP-26 | AMP | Supervisión humana efectiva | SE_APOYA_EN (otra unidad) |

**Pregunta generadora:** ¿Qué resultado de la revisión de desempeño de un agente lo llevaría a quitarle autonomía, y quién tendría que firmar esa decisión?

---

### 034. M4.2-PA01 — Amenazas del dominio Zero Trust (instancias: correo y colaboración · cross-domain · endpoints · identidades · datos)

**Unidad:** M4.2 Gestión de Amenazas, Vulnerabilidades y Riesgos Emergentes · **Tipo:** PA · **Horas (sub-plan):** 5 · **Competencias:** C2.2 · **Origen:** M4.2-PA01 (V5) · **Título V7:** Amenazas al correo y la colaboración · **Extensión:** 262 palabras · **Estado:** Idea central desarrollada (lote PA-01/02) — PROMOVIDO al programa (V7-C04) — título generalizado (V7.1); ID curricular, no ESS.

**Definición / idea central.** Phishing, BEC, malware, QR phishing, campañas, abuso de colaboración; Campaign Views, Threat analytics, simulaciones.

**Brecha frente a los 331.** Ningún concepto trata las amenazas del dominio productividad.

**Tesis y sentido para el rol.** El dominio productividad tiene su propio catálogo de amenazas: phishing de credenciales, compromiso de correo empresarial (BEC) sin enlaces ni adjuntos, malware en adjuntos y archivos compartidos, phishing por código QR, campañas coordinadas, abuso de la colaboración y ataques a las cuentas prioritarias. El owner debe reconocerlas en sus herramientas (Campaign Views, Threat analytics) y traducirlas a técnicas del adversario para hablar con el SOC. La tesis es que sin dominio de las amenazas del dominio el modelo operativo se ejecuta a ciegas y los agentes se instruyen con generalidades. En V7.1 el concepto se generaliza como amenazas del dominio Zero Trust; esta es su instancia de referencia.

**Tensión y límites.** La tensión es la velocidad: la guía semanal de campañas llega tarde para una campaña de dos horas; la respuesta es combinar la revisión semanal con alertas y con remediación posterior a la entrega. Otra tensión es el BEC: no tiene indicadores técnicos clásicos y las defensas son de impersonación y de proceso (verificación de pagos), fuera del alcance técnico del control.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: taxonomías de phishing y BEC; MITRE ATT&CK. Implementación: analizar tres campañas con Campaign Views y Threat analytics, describiendo técnica, infraestructura, qué capa detuvo cada mensaje y qué quedó entregado; diseñar una simulación en Attack Simulation Training alineada a la campaña más relevante.

**Evidencia y evaluación.** Evidencia: análisis de tres campañas y diseño de una simulación. Se evalúa la precisión técnica, la conexión con las capas de la arquitectura y la identificación de límites del control.

**Puentes.** Instancia M4.2-K06 (superficie de ataque); se relaciona con K10 (indicadores) y HC-016. Tareas MDO-D09, MDO-W02, MDO-W04 y MDO-M04.

**Recomendaciones de práctica y ejercitación.**
1. Analizar tres campañas (Campaign Views, Threat analytics): técnica ATT&CK, infraestructura, capa que detuvo cada mensaje, mensajes entregados.
2. Diseñar una simulación en Attack Simulation Training alineada a la campaña más relevante y definir su métrica.
3. Delimitar para el BEC qué es control técnico y qué es proceso de negocio; proponer la interfaz.

**Aplicación en el escenario de referencia.** Base agnóstica: Taxonomías de phishing/BEC; MITRE ATT&CK. Implementación Microsoft: Campaign Views, Threat analytics, Attack Simulation Training. Actividad: Analizar 3 campañas reales/sintéticas. Evidencia: Análisis.

**Próximos pasos.**
- Alimentar las instrucciones de AG-04 y AG-06 con los patrones observados.
- Conectar con la concientización (MDO-M04, AG-12).
- Revisar las campañas contra la matriz amenaza→agente (M4.2-PA02); instanciar en los demás dominios.

**Relación con los conceptos de la(s) unidad(es) M4.2.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M4.2-K01 | K | Gestión Vulnerabilidades | misma unidad |
| M4.2-K02 | K | Modelado de Amenazas | misma unidad |
| M4.2-K03 | K | Amenaza Interna | misma unidad |
| M4.2-K04 | K | RaaS (Ransomware) | misma unidad |
| M4.2-K05 | K | Priorización por Riesgo | misma unidad |
| M4.2-K06 | K | Superficie de Ataque | INSTANCIA_DE |
| M4.2-K07 | K | Riesgos Emergentes | misma unidad |
| M4.2-K08 | K | Economía del Cibercrimen | misma unidad |
| M4.2-K09 | K | STRIDE | misma unidad |
| M4.2-K10 | K | IoC (Indicadores) | SE_RELACIONA |
| AMP-41 | AMP | Prompt injection | misma unidad |
| AMP-42 | AMP | Envenenamiento de datos y modelos | misma unidad |
| HC-016 | HC | Superficie de ataque contextualizada | SE_RELACIONA |
| HC-026 | HC | Ética, cultura y controles internos | misma unidad |
| HC-031 | HC | Seguridad del software y confianza en componentes | misma unidad |
| HC-032 | HC | Evaluación adversarial de sistemas autónomos | misma unidad |
| M4.2-K11 | K | Escalamiento de privilegios en identidades humanas y no humanas como táctica adversaria | misma unidad |
| M4.2-PA02 | PA | Catálogos de amenazas a sistemas agénticos aplicados a la flota | misma unidad |

**Pregunta generadora:** De las campañas que su organización recibió el último mes, ¿cuál habría tenido éxito sin la remediación posterior a la entrega, y qué cambia eso en sus prioridades?

> **Instancias de dominio (V7.1).** Este pre-ensayo desarrolla la instancia de referencia (productividad: Defender for Office 365). Las instancias XDR, Endpoints, Identidades, Datos, SIEM, Nube y Apps están en los paquetes `Dominio_*` (plano B), que no modifican este concepto.


---

### 035. M4.2-PA02 — Catálogos de amenazas a sistemas agénticos aplicados a la flota

**Unidad:** M4.2 Gestión de Amenazas, Vulnerabilidades y Riesgos Emergentes · **Tipo:** PA · **Horas (sub-plan):** 5 · **Competencias:** C4.6, C5.1 · **Origen:** G2.1-PA03 + M4.2-PA02 (V5) · **Referencias por ID (V7-C09):** OWASP Top 10 for Agentic Applications 2026 v2.01 (ASI01–ASI10); OWASP Top 10 for LLM Applications 2025 (LLM01–LLM10); MITRE ATLAS; CSA MAESTRO · **Extensión:** 298 palabras · **Estado:** Idea central desarrollada (lote PA-01/02) — sub-plan PO-GAC; ID curricular, no ESS.

**Definición / idea central.** OWASP Agentic/LLM, MITRE ATLAS y CSA aplicados a los agentes del control: amenaza → agente → control.

**Brecha frente a los 331.** AMP-41/42 desarrollan dos amenazas; no hay uso sistemático de los catálogos.

**Tesis y sentido para el rol.** Los sistemas agénticos tienen catálogos de amenazas públicos: el OWASP Top 10 para aplicaciones agénticas (ASI01–ASI10) y para aplicaciones con LLM, MITRE ATLAS para tácticas contra sistemas de IA, y las guías de CSA (MAESTRO). AMP-41 y AMP-42 desarrollan dos amenazas y M6.2-K04 la seguridad de IA en general; este concepto aplica los catálogos de forma sistemática a la flota: para cada amenaza, qué agentes del control son vulnerables, por qué y qué control AGC o de plataforma la mitiga. La tesis es que el catálogo cobra sentido cuando se cruza con agentes concretos y sus permisos, no cuando se memoriza.

**Tensión y límites.** La tensión es que los catálogos cambian de versión y de códigos; el owner debe citar la versión vigente y aceptar que la matriz envejece. Otra tensión es la especificidad del SOC: un agente que lee correo malicioso para triarlo está expuesto por diseño a la inyección; no se puede eliminar la exposición, solo limitar lo que el agente puede hacer con ella (AMP-36). El ensayo debe discutir el principio de que el contenido procesado nunca es instrucción y cómo se verifica.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: OWASP GenAI Security Project (Agentic Top 10 v2.01, LLM Top 10 2025), MITRE ATLAS, CSA MAESTRO. Implementación: cruzar diez amenazas con los quince agentes del catálogo y los controles AGC, indicando la mitigación Microsoft (Prompt Shields, Defender para IA, DLP de Purview, políticas de conectores, acceso condicional) y la prueba que la verifica (red teaming de AMP-37).

**Evidencia y evaluación.** Evidencia: matriz amenaza → agente → control → prueba. Se evalúa la cobertura de los agentes de mayor autonomía, la cita de la versión del catálogo y la existencia de una prueba por mitigación crítica.

**Puentes.** Se apoya en AMP-41 y AMP-42; profundiza M6.2-K04; se relaciona con HC-032 (evaluación adversarial). Alimenta G4.1-PA02 (registro de riesgos) y AGC-08.

**Recomendaciones de práctica y ejercitación.**
1. Cruzar los 10 ASI (OWASP Agentic Top 10 v2.01) con los 15 agentes: exposición, causa (lee correo hostil, invoca remediación, consulta fuentes externas), control AGC y mitigación Microsoft.
2. Diseñar una prueba de inyección indirecta sobre AG-01/AG-02 con un correo que intente ordenar una remediación; ejecutarla en el entorno de prueba.
3. Mapear las mismas amenazas a MITRE ATLAS y a CSA MAESTRO para verificar que no quedan clases sin cubrir.

**Aplicación en el escenario de referencia.** Base agnóstica: OWASP GenAI Security Project; MITRE ATLAS; CSA MAESTRO. Implementación Microsoft: Defender para IA, Prompt Shields, DLP de Purview, políticas de conectores. Actividad: Cruzar 10 amenazas con los 15 agentes y los AGC. Evidencia: Matriz amenaza→agente→control.

**Próximos pasos.**
- Trasladar los hallazgos al registro de riesgos (G4.1-PA02) y a AGC-08.
- Incluir las pruebas en el expediente ATO (AMP-37).
- Actualizar la matriz en cada nueva versión de OWASP/ATLAS.

**Relación con los conceptos de la(s) unidad(es) M4.2.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M4.2-K01 | K | Gestión Vulnerabilidades | misma unidad |
| M4.2-K02 | K | Modelado de Amenazas | misma unidad |
| M4.2-K03 | K | Amenaza Interna | misma unidad |
| M4.2-K04 | K | RaaS (Ransomware) | misma unidad |
| M4.2-K05 | K | Priorización por Riesgo | misma unidad |
| M4.2-K06 | K | Superficie de Ataque | misma unidad |
| M4.2-K07 | K | Riesgos Emergentes | misma unidad |
| M4.2-K08 | K | Economía del Cibercrimen | misma unidad |
| M4.2-K09 | K | STRIDE | misma unidad |
| M4.2-K10 | K | IoC (Indicadores) | misma unidad |
| AMP-41 | AMP | Prompt injection | SE_APOYA_EN |
| AMP-42 | AMP | Envenenamiento de datos y modelos | SE_APOYA_EN |
| HC-016 | HC | Superficie de ataque contextualizada | misma unidad |
| HC-026 | HC | Ética, cultura y controles internos | misma unidad |
| HC-031 | HC | Seguridad del software y confianza en componentes | misma unidad |
| HC-032 | HC | Evaluación adversarial de sistemas autónomos | SE_RELACIONA |
| M4.2-K11 | K | Escalamiento de privilegios en identidades humanas y no humanas como táctica adversaria | misma unidad |
| M4.2-PA01 | PA | Amenazas del dominio Zero Trust (instancias: correo y colaboración · cross-domain · endpoints · identidades · datos) | misma unidad |
| M6.2-K04 | K | Seguridad IA | PROFUNDIZA (otra unidad) |

**Pregunta generadora:** ¿Qué haría el agente que remedia correo si el correo que investiga le ordenara remediar otra cosa, y qué control exacto se lo impide hoy?

---

### 036. M5.1-PA01 — Playbooks de incidentes de correo con roles humano/agente

**Unidad:** M5.1 Planificación y Preparación (Incl. BIA) · **Tipo:** PA · **Horas (sub-plan):** 4 · **Competencias:** C3.2, C3.5 · **Origen:** M5.1-PA01 (V5) · **Extensión:** 232 palabras · **Estado:** Idea central desarrollada (lote PA-01/02) — sub-plan PO-GAC; ID curricular, no ESS.

**Definición / idea central.** Phishing, BEC y malware entregado: pasos, ejecutor (humano, AIR, agente) y evidencia.

**Brecha frente a los 331.** K07 y HC-019 no distinguen ejecutores por paso en un dominio concreto.

**Tesis y sentido para el rol.** Un playbook híbrido describe la respuesta a un tipo de incidente de correo paso por paso, indicando para cada paso quién o qué lo ejecuta: un humano, la investigación y respuesta automatizadas de la plataforma, o un agente con su nivel de autonomía y su punto de aprobación; y qué evidencia queda. M5.1-K07 trata playbooks en general y HC-019 el SOC agéntico con supervisión; este concepto los une en el dominio concreto. La tesis es que el playbook es el lugar donde la decisión de autonomía (AMP-40) se vuelve operativa paso por paso.

**Tensión y límites.** La tensión es entre determinismo y juicio: la automatización clásica ejecuta pasos fijos, el agente interpreta; mezclar ambos sin marcar dónde termina uno y empieza el otro produce respuestas impredecibles. Otra tensión es el BEC, donde la respuesta técnica es menor que la de negocio y el playbook debe cruzar fronteras organizativas.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: NIST SP 800-61 y diseño de playbooks. Implementación: redactar dos playbooks híbridos (phishing de credenciales con clic; BEC sin enlace) con pasos, ejecutor (humano / AIR / agente AG-01, AG-02 o AG-03), nivel de autonomía, aprobación, herramienta y evidencia.

**Evidencia y evaluación.** Evidencia: dos playbooks híbridos revisados por el SOC Lead. Se evalúa la claridad de ejecutores por paso, la coherencia con las fichas de agentes y la trazabilidad de cada acción.

**Puentes.** Instancia M5.1-K07 (playbooks); se apoya en HC-019 y AMP-40. Prepara M5.2-PA01 y el tabletop de AMP-43.

**Recomendaciones de práctica y ejercitación.**
1. Redactar el playbook híbrido de phishing de credenciales con clic: pasos, ejecutor (humano / AIR / AG-01 / AG-02), nivel, aprobación, herramienta, evidencia.
2. Redactar el playbook de BEC sin enlace cruzando la frontera con el proceso de negocio (verificación de pagos).
3. Revisar ambos con el SOC Lead y marcar los pasos 'nunca delegar'.

**Aplicación en el escenario de referencia.** Base agnóstica: NIST SP 800-61; playbooks. Implementación Microsoft: AIR, Threat Explorer, agentes del catálogo. Actividad: Redactar 2 playbooks híbridos. Evidencia: Playbooks.

**Próximos pasos.**
- Ejecutar los playbooks en laboratorio (M5.2-PA01).
- Usarlos como guion del tabletop con agentes (AMP-43).
- Versionarlos junto con las fichas de los agentes implicados.

**Relación con los conceptos de la(s) unidad(es) M5.1.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M5.1-K01 | K | IRP (Plan Respuesta) | misma unidad |
| M5.1-K02 | K | BIA (Impacto Negocio) | misma unidad |
| M5.1-K03 | K | CSIRT | misma unidad |
| M5.1-K04 | K | Preparación (Readiness) | misma unidad |
| M5.1-K05 | K | Clasificación Incidentes | misma unidad |
| M5.1-K06 | K | Ejercicios Tabletop | misma unidad |
| M5.1-K07 | K | Playbooks | INSTANCIA_DE |
| M5.1-K08 | K | Cadena de Mando | misma unidad |
| M5.1-K09 | K | RTO/RPO | misma unidad |
| M5.1-K10 | K | Alineación BCDR | misma unidad |
| AMP-43 | AMP | Tabletop de incidentes con agentes | misma unidad |
| AMP-44 | AMP | Kill switch y escalamiento | misma unidad |
| HC-007 | HC | Resiliencia gobernada por impacto | misma unidad |
| HC-020 | HC | Respuesta y comunicación bajo incertidumbre | misma unidad |
| HC-022 | HC | Gobierno de crisis multidisciplinario | misma unidad |
| HC-025 | HC | Competencias y resiliencia organizacional | misma unidad |
| HC-030 | HC | Seguridad industrial y continuidad de negocio | misma unidad |
| HC-037 | HC | Alineación entre competencias y decisiones | misma unidad |
| HC-039 | HC | Riesgo cibernético como narrativa empresarial | misma unidad |
| HC-019 | HC | SOC agéntico con supervisión humana | SE_APOYA_EN (otra unidad) |
| AMP-40 | AMP | Human-in-the-loop | SE_APOYA_EN (otra unidad) |

**Pregunta generadora:** En su playbook de phishing, ¿qué paso ejecutaría un agente sin preguntar, cuál con aprobación y cuál jamás, y por qué exactamente en ese orden?

---

### 037. M5.2-PA01 — Ejecución de respuesta en correo: AIR, acciones manuales y acciones de agentes con aprobación

**Unidad:** M5.2 Ejecución, Post-Mortem y Comunicación · **Tipo:** PA · **Horas (sub-plan):** 4 · **Competencias:** C2.2, C3.5 · **Origen:** M5.2-PA01 (V5) · **Extensión:** 241 palabras · **Estado:** Idea central desarrollada (lote PA-01/02) — sub-plan PO-GAC; ID curricular, no ESS.

**Definición / idea central.** Contención y erradicación en correo; supervisión de acciones propuestas por agentes; límites de lote.

**Brecha frente a los 331.** K01/K07 genéricos; AMP-38 pide probar controles autónomos.

**Tesis y sentido para el rol.** Responder a un incidente de correo es contener y erradicar: remover mensajes de buzones (eliminación suave o definitiva), bloquear remitentes, dominios o URL, mover a cuarentena, revocar sesiones cuando hubo clic, y hacerlo con proporcionalidad y registro. La plataforma ofrece acciones manuales (Threat Explorer, Action center) y automatizadas (investigación y respuesta automatizadas); los agentes agregan acciones propuestas que un humano aprueba (L2) con límites de lote. La tesis es que la ejecución con agentes requiere tres cosas que la manual no: límite explícito de alcance por acción, aprobación registrada y reversibilidad probada.

**Tensión y límites.** La tensión es la escala: remover mil mensajes de una campaña es exactamente lo que un agente hace bien y exactamente donde un error se multiplica por mil; el límite de lote y la eliminación suave antes que la definitiva son el compromiso. Otra tensión es la autoridad sobre buzones de personas: la remediación es una intromisión legítima que debe quedar registrada.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: NIST SP 800-61. Implementación: ejecutar la respuesta a tres incidentes de laboratorio combinando investigación automatizada, acciones manuales en Threat Explorer y acciones propuestas por AG-02 aprobadas en L2 con límite de lote; registrar aprobador, alcance, resultado y reversión de prueba.

**Evidencia y evaluación.** Evidencia: bitácora de tres respuestas con acciones, aprobaciones y una reversión probada. Se evalúa la proporcionalidad, el cumplimiento de límites y la calidad del registro.

**Puentes.** Instancia M5.2-K01 (contención); se relaciona con K07 (triaje) y AMP-38 (pruebas de controles autónomos). Tareas MDO-D02, MDO-D09 y MDO-A01; KPI-12.

**Recomendaciones de práctica y ejercitación.**
1. Ejecutar la respuesta a tres incidentes de laboratorio: AIR, acciones manuales en Threat Explorer y acciones propuestas por AG-02 aprobadas en L2 con límite de lote.
2. Probar la reversión de una eliminación suave y documentar el tiempo y la evidencia.
3. Fijar el límite de lote por tipo de acción y justificarlo con el apetito de autonomía.

**Aplicación en el escenario de referencia.** Base agnóstica: NIST SP 800-61. Implementación Microsoft: AIR, Action center, Threat Explorer; aprobaciones L2. Actividad: Ejecutar la respuesta a 3 incidentes de laboratorio. Evidencia: Bitácora.

**Próximos pasos.**
- Medir KPI-12 (acciones revertidas) sobre la bitácora.
- Incorporar los límites a la ficha y a los permisos de AG-02 (M2.2-PA01).
- Alimentar el post-mortem (M5.2-PA02) con los errores observados.

**Relación con los conceptos de la(s) unidad(es) M5.2.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M5.2-K01 | K | Contención | INSTANCIA_DE |
| M5.2-K02 | K | Erradicación | misma unidad |
| M5.2-K03 | K | Recuperación | misma unidad |
| M5.2-K04 | K | Comunicación Crisis | misma unidad |
| M5.2-K05 | K | Post-Mortem | misma unidad |
| M5.2-K06 | K | Forense Digital | misma unidad |
| M5.2-K07 | K | Triaje | SE_RELACIONA |
| M5.2-K08 | K | Gestión Narrativa | misma unidad |
| M5.2-K09 | K | Notificación Brechas | misma unidad |
| M5.2-K10 | K | Resiliencia Adaptativa | misma unidad |
| AMP-45 | AMP | Forense de agentes | misma unidad |
| AMP-46 | AMP | Trazabilidad de decisiones autónomas | misma unidad |
| HC-019 | HC | SOC agéntico con supervisión humana | misma unidad |
| HC-020 | HC | Respuesta y comunicación bajo incertidumbre | misma unidad |
| HC-021 | HC | Recuperación como prueba de confianza | misma unidad |
| HC-035 | HC | Aprendizaje desde incidentes hasta políticas | misma unidad |
| M5.2-PA02 | PA | Mejora gobernada de agentes: del post-mortem al ChangeSet con regresión | misma unidad |
| AMP-38 | AMP | Pruebas de controles autónomos | SE_RELACIONA (otra unidad) |

**Pregunta generadora:** ¿Cuál es el máximo de buzones sobre los que permitiría que un agente actúe con una sola aprobación, y qué pasó la última vez que alguien removió mensajes por error?

---

### 038. M5.2-PA02 — Mejora gobernada de agentes: del post-mortem al ChangeSet con regresión

**Unidad:** M5.2 Ejecución, Post-Mortem y Comunicación · **Tipo:** PA · **Horas (sub-plan):** 4 · **Competencias:** C6.6, C6.5 · **Origen:** M5.2-PA02 (V5) · **Extensión:** 280 palabras · **Estado:** Idea central desarrollada (lote PA-01/02) — sub-plan PO-GAC; ID curricular, no ESS.

**Definición / idea central.** Causa raíz de errores de agentes convertida en cambios versionados con aprobación y regresión.

**Brecha frente a los 331.** K05 y HC-035 conectan post-mortem con políticas; falta el ciclo de cambio versionado del agente.

**Tesis y sentido para el rol.** Cuando un agente falla, el post-mortem debe reconstruir qué vio, qué decidió y por qué (AMP-45) y convertir la causa raíz en un cambio versionado: una instrucción más precisa, una fuente de conocimiento corregida, una herramienta acotada, un umbral distinto. HC-035 conecta el aprendizaje de incidentes con las políticas; este concepto lo lleva al agente como artefacto: el cambio se propone como ChangeSet, se prueba contra el dataset dorado (regresión), se aprueba y se despliega con versión. La tesis es que la mejora de un agente es gestión de cambios, no edición de prompts, y que sin regresión no hay evidencia de que el cambio mejoró algo.

**Tensión y límites.** La tensión es la velocidad: editar una instrucción toma un minuto y la tentación de hacerlo en producción es enorme; la disciplina de versionar y probar parece burocracia hasta el primer cambio que empeora al agente sin que nadie lo note. Otra tensión es el aprendizaje del propio modelo: el agente no "aprende" del post-mortem; aprende el equipo que lo mantiene.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: análisis de causa raíz, gestión de cambios y ALM. Implementación: realizar el post-mortem simulado de un fallo de AG-03, reconstruir la traza, proponer el ChangeSet con el cambio de instrucción y la prueba de regresión en Foundry o Copilot Studio, y registrar la aprobación y la nueva versión en el ALM de Power Platform.

**Evidencia y evaluación.** Evidencia: informe de post-mortem y ChangeSet con resultado de regresión. Se evalúa la calidad de la reconstrucción, la conexión causa → cambio y la prueba de que el cambio no degradó otros casos.

**Puentes.** Extiende M5.2-K05 (post-mortem); operacionaliza HC-035; se apoya en AMP-45 y se relaciona con HC-034 (decisiones reversibles). Sostiene AGC-16 y se conecta con M6.2-PA02.

**Recomendaciones de práctica y ejercitación.**
1. Simular un fallo de AG-03 (liberó de cuarentena un mensaje malicioso por instrucción ambigua) y reconstruir la traza completa (qué vio, qué decidió, con qué autoridad).
2. Proponer el ChangeSet (instrucción, conocimiento, herramienta o umbral) y ejecutar la regresión contra el dataset dorado.
3. Registrar aprobación y nueva versión en el ALM de Power Platform.

**Aplicación en el escenario de referencia.** Base agnóstica: RCA; gestión de cambios; ALM. Implementación Microsoft: ALM de Power Platform; evaluaciones de Foundry; ChangeSets. Actividad: Post-mortem simulado y ChangeSet propuesto. Evidencia: Informe + ChangeSet.

**Próximos pasos.**
- Formalizar el pipeline de cambios (M6.2-PA02) y el AGC-16.
- Alimentar la política y los procedimientos con la lección (HC-035).
- Repetir el ejercicio con un fallo de AG-02 (remediación).

**Relación con los conceptos de la(s) unidad(es) M5.2.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M5.2-K01 | K | Contención | misma unidad |
| M5.2-K02 | K | Erradicación | misma unidad |
| M5.2-K03 | K | Recuperación | misma unidad |
| M5.2-K04 | K | Comunicación Crisis | misma unidad |
| M5.2-K05 | K | Post-Mortem | EXTIENDE |
| M5.2-K06 | K | Forense Digital | misma unidad |
| M5.2-K07 | K | Triaje | misma unidad |
| M5.2-K08 | K | Gestión Narrativa | misma unidad |
| M5.2-K09 | K | Notificación Brechas | misma unidad |
| M5.2-K10 | K | Resiliencia Adaptativa | misma unidad |
| AMP-45 | AMP | Forense de agentes | SE_APOYA_EN |
| AMP-46 | AMP | Trazabilidad de decisiones autónomas | misma unidad |
| HC-019 | HC | SOC agéntico con supervisión humana | misma unidad |
| HC-020 | HC | Respuesta y comunicación bajo incertidumbre | misma unidad |
| HC-021 | HC | Recuperación como prueba de confianza | misma unidad |
| HC-035 | HC | Aprendizaje desde incidentes hasta políticas | OPERACIONALIZA |
| M5.2-PA01 | PA | Ejecución de respuesta en correo: AIR, acciones manuales y acciones de agentes con aprobación | misma unidad |
| HC-034 | HC | Decisiones reversibles y riesgo de transición | SE_RELACIONA (otra unidad) |

**Pregunta generadora:** Después del último error de un agente en su SOC, ¿qué cambió exactamente en el agente, quién lo aprobó y qué prueba demostró que no empeoró otra cosa?

---

### 039. M6.1-PA01 — Operación degradada del SOC sin agentes ni modelos

**Unidad:** M6.1 Continuidad, DRP y Resiliencia Operativa · **Tipo:** PA · **Horas (sub-plan):** 4 · **Competencias:** C6.5 · **Origen:** M6.1-PA01 (V5) · **Extensión:** 254 palabras · **Estado:** Idea central desarrollada (lote PA-01/02) — sub-plan PO-GAC; ID curricular, no ESS.

**Definición / idea central.** Modo manual, prioridades, dependencias de plataforma y pruebas de operación sin IA.

**Brecha frente a los 331.** AMP-47/48 cubren recuperación y dependencias; falta el runbook degradado.

**Tesis y sentido para el rol.** Un SOC que delegó tareas a agentes depende de plataformas de IA que pueden fallar, degradarse, cambiar de precio o quedar indisponibles; AMP-47 y AMP-48 tratan la recuperación de servicios de IA y las dependencias de modelos. Este concepto pregunta qué pasa el día en que no hay agentes: la operación degradada del SOC exige un runbook manual priorizado, la lista de dependencias de cada agente y una prueba periódica de operar sin IA. La tesis es que la continuidad del control no puede depender de la disponibilidad de los agentes, y que la degradación elegante es un control que se diseña y se ensaya.

**Tensión y límites.** La tensión es la atrofia: cuando los agentes triagen durante meses, las personas pierden práctica y el runbook manual se vuelve teórico. Otra tensión es la prioridad: sin agentes no se puede hacer todo; hay que decidir de antemano qué tareas son críticas y cuáles toleran demora.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: resiliencia operativa. Implementación: mapear las dependencias de los quince agentes y ejecutar un día del runbook en modo manual, midiendo tiempo por tarea y tareas no realizadas; documentar los disparadores de activación del modo degradado y el plan de recuperación de la flota.

**Evidencia y evaluación.** Evidencia: mapa de dependencias, informe del día en modo manual y plan de recuperación. Se evalúa la priorización explícita, la medición honesta de lo que no se pudo hacer y la claridad de los disparadores.

**Puentes.** Operacionaliza AMP-48 (dependencias de modelos); se apoya en AMP-47; se relaciona con M6.1-K10 (dependencias) y HC-023 (concentración). Parte de la etapa E5.

**Recomendaciones de práctica y ejercitación.**
1. Mapear las dependencias de los 15 agentes (plataforma, modelo, conectores/MCP, knowledge, identidad) a partir de los anexos.
2. Ejecutar un día del runbook en modo manual (sin agentes) midiendo tiempo por tarea y tareas no realizadas; priorizar explícitamente.
3. Redactar los disparadores del modo degradado y el plan de recuperación de la flota.

**Aplicación en el escenario de referencia.** Base agnóstica: Resiliencia operativa. Implementación Microsoft: Runbook manual; dependencias de Copilot Studio/Foundry/Agent 365. Actividad: Ejecutar un día del runbook en modo manual. Evidencia: Informe.

**Próximos pasos.**
- Programar el ejercicio en modo manual al menos semestralmente.
- Registrar la concentración tecnológica como riesgo estratégico (HC-023, AMP-15).
- Incluir la recuperación de agentes en el BCDR del programa.

**Relación con los conceptos de la(s) unidad(es) M6.1.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M6.1-K01 | K | Continuidad (BCP) | misma unidad |
| M6.1-K02 | K | Recuperación (DRP) | misma unidad |
| M6.1-K03 | K | Resiliencia Operativa | misma unidad |
| M6.1-K04 | K | ISO 22301 | misma unidad |
| M6.1-K05 | K | Pruebas Continuidad | misma unidad |
| M6.1-K06 | K | Backups Inmutables | misma unidad |
| M6.1-K07 | K | Alta Disponibilidad | misma unidad |
| M6.1-K08 | K | Sitio Alternativo | misma unidad |
| M6.1-K09 | K | Gestión Crisis (Negocio) | misma unidad |
| M6.1-K10 | K | Dependencias | SE_RELACIONA |
| AMP-47 | AMP | Recuperación de servicios de IA | SE_APOYA_EN |
| AMP-48 | AMP | Dependencias de modelos | OPERACIONALIZA |
| HC-007 | HC | Resiliencia gobernada por impacto | misma unidad |
| HC-008 | HC | Cadena de confianza en terceros | misma unidad |
| HC-021 | HC | Recuperación como prueba de confianza | misma unidad |
| HC-022 | HC | Gobierno de crisis multidisciplinario | misma unidad |
| HC-023 | HC | Riesgo de concentración tecnológica | SE_RELACIONA |
| HC-025 | HC | Competencias y resiliencia organizacional | misma unidad |
| HC-030 | HC | Seguridad industrial y continuidad de negocio | misma unidad |

**Pregunta generadora:** Si mañana su plataforma de agentes quedara indisponible una semana, ¿qué tareas del control dejarían de hacerse, quién lo decidiría y cuándo fue la última vez que su equipo operó sin ellos?

---

### 040. M6.2-PA01 — Plataformas y rutas de construcción de agentes y responsabilidad compartida en IA

**Unidad:** M6.2 Seguridad en Redes, Nube, Tecnologías Emergentes y SCRM · **Tipo:** PA · **Horas (sub-plan):** 5 · **Competencias:** C4.3, C4.4, C7.2 · **Origen:** M6.2-PA01 (V5) · **Extensión:** 294 palabras · **Estado:** Idea central desarrollada (lote PA-01/02) — sub-plan PO-GAC; ID curricular, no ESS.

**Definición / idea central.** Tres rutas (Security Copilot custom; Copilot Studio + MCP/Security Copilot; Foundry Agent Service + MCP); qué asegura la plataforma y qué el owner.

**Brecha frente a los 331.** K07 y AMP-51 no comparan plataformas ni dan criterios de ruta.

**Tesis y sentido para el rol.** En el escenario Microsoft existen tres rutas para construir agentes del SOC: agentes personalizados dentro de Security Copilot, que consumen SCU; agentes en Copilot Studio que consumen Security Copilot o servidores MCP de Microsoft (Sentinel, Microsoft MCP Server for Enterprise sobre Graph, Learn) y conectores con aprobaciones y canales en Teams; y agentes en Microsoft Foundry Agent Service con MCP, elección de modelo, evaluaciones y tracing. Cada ruta reparte de forma distinta la responsabilidad entre la plataforma y el owner (M6.2-K07) y tiene una unidad de costo distinta. La tesis es que elegir la ruta es una decisión de gobierno —no solo técnica— que debe hacerse por agente según autonomía, datos, costo y capacidad del equipo, y documentarse en la matriz de responsabilidad compartida.

**Tensión y límites.** La tensión es la comodidad: la ruta más integrada es la que menos control da sobre modelo y costo unitario; la más controlable es la que más responsabilidad operativa transfiere al owner. Otra tensión es la disponibilidad: capacidades en preview (Sentinel MCP, escenarios multi-tenant de identidad de agentes) no deben asumirse. El ensayo debe discutir criterios de ruta y por qué una flota puede combinar rutas sin perder gobierno si el control plane es común.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: responsabilidad compartida aplicada a IA; low-code frente a pro-code. Implementación: completar la matriz de responsabilidad compartida para las tres rutas y elegir la ruta para cinco agentes del catálogo, justificando por autonomía, datos, costo y capacidad; validar en el tenant qué capacidades están disponibles, en preview o pendientes.

**Evidencia y evaluación.** Evidencia: matriz de responsabilidad compartida y decisión de ruta para cinco agentes. Se evalúa la explicitud de los criterios y la honestidad sobre disponibilidad.

**Puentes.** Instancia M6.2-K07 (responsabilidad compartida); se relaciona con M6.2-K04, AMP-51 y AMP-50 (conectores). Depende de M3.1-PA01 y alimenta M1.2-PA01 (costo por ruta).

**Recomendaciones de práctica y ejercitación.**
1. Completar la matriz de responsabilidad compartida (plataforma / owner / segunda línea) para R1, R2 y R3 con los anexos de agentes como insumo.
2. Elegir y justificar la ruta para cinco agentes (AG-01, AG-02, AG-10, AG-14, AG-15) por autonomía, datos, costo y capacidad del equipo.
3. Verificar en el tenant la disponibilidad (GA/preview) de Sentinel MCP, Microsoft MCP Server for Enterprise y Agent ID para los agentes elegidos.

**Aplicación en el escenario de referencia.** Base agnóstica: Responsabilidad compartida aplicada a IA; low-code vs pro-code. Implementación Microsoft: Security Copilot, Copilot Studio, Foundry, Agent 365. Actividad: Completar la matriz de responsabilidad compartida y elegir la ruta para 5 agentes. Evidencia: Matriz + decisión.

**Próximos pasos.**
- Trasladar el costo por ruta al modelo FinOps (M1.2-PA01).
- Documentar la postura de IA en nube de los recursos de Foundry (AMP-51).
- Revisar la decisión de ruta en cada revisión de desempeño.

**Relación con los conceptos de la(s) unidad(es) M6.2.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M6.2-K01 | K | C-SCRM (Cadena Suministro) | misma unidad |
| M6.2-K02 | K | Seguridad Nube | misma unidad |
| M6.2-K03 | K | DevSecOps | misma unidad |
| M6.2-K04 | K | Seguridad IA | SE_RELACIONA |
| M6.2-K05 | K | IoT/OT Security | misma unidad |
| M6.2-K06 | K | Shadow AI | misma unidad |
| M6.2-K07 | K | Responsabilidad Compartida | INSTANCIA_DE |
| M6.2-K08 | K | Riesgo Terceros (TPRM) | misma unidad |
| M6.2-K09 | K | SDLC Seguro | misma unidad |
| M6.2-K10 | K | SBOM | misma unidad |
| AMP-49 | AMP | Supply chain de modelos | misma unidad |
| AMP-50 | AMP | Seguridad de herramientas y conectores | SE_RELACIONA |
| AMP-51 | AMP | Postura de IA en nube | SE_RELACIONA |
| HC-008 | HC | Cadena de confianza en terceros | misma unidad |
| HC-011 | HC | Seguridad de datos en la IA empresarial | misma unidad |
| HC-023 | HC | Riesgo de concentración tecnológica | misma unidad |
| HC-024 | HC | Cumplimiento y privacidad por diseño | misma unidad |
| HC-029 | HC | Aseguramiento de terceros y cadena de suministro | misma unidad |
| HC-030 | HC | Seguridad industrial y continuidad de negocio | misma unidad |
| HC-031 | HC | Seguridad del software y confianza en componentes | misma unidad |
| HC-032 | HC | Evaluación adversarial de sistemas autónomos | misma unidad |
| HC-033 | HC | Seguridad y soberanía de datos distribuidos | misma unidad |
| M6.2-PA02 | PA | AgentOps / ALM de agentes | misma unidad |
| M6.2-PA03 | PA | Bases multiplataforma, multicloud y multimodelo | misma unidad |

**Pregunta generadora:** Para el agente que más autonomía tendrá en su SOC, ¿qué ruta elegiría si el criterio fuera el control del costo, cuál si fuera la integración, y cuál elegiría realmente?

---

### 041. M6.2-PA02 — AgentOps / ALM de agentes

**Unidad:** M6.2 Seguridad en Redes, Nube, Tecnologías Emergentes y SCRM · **Tipo:** PA · **Horas (sub-plan):** 4 · **Competencias:** C6.6, C4.3 · **Origen:** M6.2-PA02 (V5) · **Extensión:** 221 palabras · **Estado:** Idea central desarrollada (lote PA-01/02) — sub-plan PO-GAC; ID curricular, no ESS.

**Definición / idea central.** Entornos, soluciones, versionado, pruebas, despliegue y ChangeSets gobernados para agentes.

**Brecha frente a los 331.** K03 y HC-034/AMP-21 no cubren el ciclo de vida de desarrollo de agentes.

**Tesis y sentido para el rol.** Un agente es software que cambia con frecuencia y debe gestionarse con un ciclo de vida de desarrollo: entornos separados, soluciones empaquetadas, versionado, pruebas automatizadas, despliegue controlado y posibilidad de volver atrás. M6.2-K03 trata DevSecOps para software clásico; HC-034 y AMP-21 la reversibilidad de decisiones. AgentOps aplica esas prácticas a instrucciones, conocimiento, herramientas y configuraciones de agentes, y las conecta con los ChangeSets gobernados. La tesis es que la mayoría de los incidentes de agentes serán causados por cambios no gobernados, y que el ALM es el control preventivo más barato.

**Tensión y límites.** La tensión es cultural: las plataformas low-code invitan a editar en producción y los equipos de SOC no vienen de la ingeniería de software. Otra tensión es la cobertura de pruebas: una regresión completa por cada cambio es cara; hay que graduar.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: LLMOps/AgentOps y ALM. Implementación: diseñar el pipeline de un agente con entornos y soluciones de Power Platform (o proyectos de Foundry), repositorio Git para instrucciones y conocimiento, evaluaciones automatizadas en Foundry, aprobación del owner y despliegue con versión; definir la política de reversión y su prueba.

**Evidencia y evaluación.** Evidencia: diseño del pipeline con gates y una ejecución de prueba. Se evalúa la proporcionalidad de las pruebas y la trazabilidad de versiones.

**Puentes.** Extiende M6.2-K03 (DevSecOps); operacionaliza HC-034 y se apoya en AMP-21. Sostiene AGC-16 y se conecta con M5.2-PA02.

**Recomendaciones de práctica y ejercitación.**
1. Diseñar el pipeline de AG-03: entornos dev/test/prod de Power Platform, solución, repositorio Git de instrucciones y conocimiento, evaluación automatizada, aprobación, despliegue con versión.
2. Ejecutar un ciclo completo cambio → regresión → aprobación → despliegue → reversión en el entorno de prueba.
3. Definir la graduación de pruebas por tipo de cambio (umbral / instrucción / herramienta).

**Aplicación en el escenario de referencia.** Base agnóstica: LLMOps/AgentOps; ALM. Implementación Microsoft: Entornos y soluciones de Power Platform, pipelines, Git, evaluaciones de Foundry. Actividad: Diseñar el pipeline de un agente. Evidencia: Diseño ALM.

**Próximos pasos.**
- Aplicar el pipeline a los agentes comunes (tools y knowledge compartidos) con control de impacto cruzado.
- Vincular con AGC-16 y el post-mortem (M5.2-PA02).
- Evaluar pipelines de Power Platform o GitHub Actions para automatizar.

**Relación con los conceptos de la(s) unidad(es) M6.2.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M6.2-K01 | K | C-SCRM (Cadena Suministro) | misma unidad |
| M6.2-K02 | K | Seguridad Nube | misma unidad |
| M6.2-K03 | K | DevSecOps | EXTIENDE |
| M6.2-K04 | K | Seguridad IA | misma unidad |
| M6.2-K05 | K | IoT/OT Security | misma unidad |
| M6.2-K06 | K | Shadow AI | misma unidad |
| M6.2-K07 | K | Responsabilidad Compartida | misma unidad |
| M6.2-K08 | K | Riesgo Terceros (TPRM) | misma unidad |
| M6.2-K09 | K | SDLC Seguro | misma unidad |
| M6.2-K10 | K | SBOM | misma unidad |
| AMP-49 | AMP | Supply chain de modelos | misma unidad |
| AMP-50 | AMP | Seguridad de herramientas y conectores | misma unidad |
| AMP-51 | AMP | Postura de IA en nube | misma unidad |
| HC-008 | HC | Cadena de confianza en terceros | misma unidad |
| HC-011 | HC | Seguridad de datos en la IA empresarial | misma unidad |
| HC-023 | HC | Riesgo de concentración tecnológica | misma unidad |
| HC-024 | HC | Cumplimiento y privacidad por diseño | misma unidad |
| HC-029 | HC | Aseguramiento de terceros y cadena de suministro | misma unidad |
| HC-030 | HC | Seguridad industrial y continuidad de negocio | misma unidad |
| HC-031 | HC | Seguridad del software y confianza en componentes | misma unidad |
| HC-032 | HC | Evaluación adversarial de sistemas autónomos | misma unidad |
| HC-033 | HC | Seguridad y soberanía de datos distribuidos | misma unidad |
| M6.2-PA01 | PA | Plataformas y rutas de construcción de agentes y responsabilidad compartida en IA | misma unidad |
| M6.2-PA03 | PA | Bases multiplataforma, multicloud y multimodelo | misma unidad |
| HC-034 | HC | Decisiones reversibles y riesgo de transición | OPERACIONALIZA (otra unidad) |
| AMP-21 | AMP | Decisiones reversibles | SE_APOYA_EN (otra unidad) |

**Pregunta generadora:** ¿Cuántos cambios recibieron los agentes de su SOC el último mes, cuántos pasaron por una prueba y cuántos podría revertir hoy en diez minutos?

---

### 042. M6.2-PA03 — Bases multiplataforma, multicloud y multimodelo

**Unidad:** M6.2 Seguridad en Redes, Nube, Tecnologías Emergentes y SCRM · **Tipo:** PA · **Horas (sub-plan):** 4 · **Competencias:** C4.1, C6.3 · **Origen:** M6.2-PA04 (V5) · **Extensión:** 241 palabras · **Estado:** Idea central desarrollada (lote PA-01/02) — sub-plan PO-GAC; ID curricular, no ESS.

**Definición / idea central.** Estándares abiertos que hacen portable el modelo: OpenTelemetry, OpenAPI/MCP, identidades de carga de trabajo, evidencia portable, prácticas eo:OP.

**Brecha frente a los 331.** HC-023/AMP-48 advierten sobre concentración; falta la base técnica de portabilidad.

**Tesis y sentido para el rol.** El escenario de este sub-plan es deliberadamente 100 % Microsoft para simplificar, pero el modelo debe sobrevivir a entornos multiplataforma, multicloud y multimodelo. Eso se logra separando en cada lección la base agnóstica de la implementación: estándares abiertos de telemetría (OpenTelemetry), de herramientas y protocolos (OpenAPI, MCP), de identidades de carga de trabajo (OAuth2/OIDC; SPIFFE como referencia), formatos de evidencia portables y prácticas operativas agnósticas (eo:OP) que las tareas de producto ejemplifican. La tesis es que la portabilidad es un atributo de diseño del programa de formación, no una promesa comercial, y que se verifica comprobando que cada capacidad tiene una base que no nombra al proveedor.

**Tensión y límites.** La tensión es que lo agnóstico suele ser menos preciso y menos útil para operar; lo específico, más útil y menos duradero. Otra tensión es que algunos estándares agénticos son jóvenes (MCP, A2A) y pueden cambiar. El ensayo debe discutir qué partes del modelo son realmente portables hoy y cuáles dependen de la plataforma.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: OTel, MCP, OAuth2/OIDC, SPIFFE, MAEO. Implementación: construir la tabla agnóstico ↔ Microsoft para quince capacidades indicando para cada una la relación de ejemplificación y el grado de portabilidad (alto, medio, bajo) con justificación.

**Evidencia y evaluación.** Evidencia: tabla de quince capacidades con grado de portabilidad justificado. Se evalúa la precisión de las bases agnósticas y la honestidad sobre lo que no es portable.

**Puentes.** Extiende G2.1-K07 (interoperabilidad); se relaciona con HC-023, AMP-48 y M6.2-K07. Cierra el sub-plan con la vista de portabilidad.

**Recomendaciones de práctica y ejercitación.**
1. Construir la tabla agnóstico ↔ Microsoft para 15 capacidades con grado de portabilidad (alto / medio / bajo) justificado.
2. Tomar los anexos de dos agentes y separar lo portable (ficha, controles AGC, prácticas eo:OP, MCP) de lo dependiente (conectores propietarios, identidad de plataforma).
3. Redactar la cláusula de portabilidad que debería tener cualquier contrato de plataforma de agentes (M1.2-PA02).

**Aplicación en el escenario de referencia.** Base agnóstica: OTel; MCP; OAuth2/OIDC; SPIFFE; MAEO. Implementación Microsoft: Cómo cada pieza Microsoft ejemplifica una base agnóstica. Actividad: Tabla agnóstico↔Microsoft para 15 capacidades. Evidencia: Tabla.

**Próximos pasos.**
- Mantener la tabla como anexo vivo del sub-plan.
- Preferir MCP y OpenAPI sobre conectores propietarios cuando la portabilidad sea un criterio.
- Reevaluar la madurez de MCP/A2A cada semestre.

**Relación con los conceptos de la(s) unidad(es) M6.2.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M6.2-K01 | K | C-SCRM (Cadena Suministro) | misma unidad |
| M6.2-K02 | K | Seguridad Nube | misma unidad |
| M6.2-K03 | K | DevSecOps | misma unidad |
| M6.2-K04 | K | Seguridad IA | misma unidad |
| M6.2-K05 | K | IoT/OT Security | misma unidad |
| M6.2-K06 | K | Shadow AI | misma unidad |
| M6.2-K07 | K | Responsabilidad Compartida | SE_RELACIONA |
| M6.2-K08 | K | Riesgo Terceros (TPRM) | misma unidad |
| M6.2-K09 | K | SDLC Seguro | misma unidad |
| M6.2-K10 | K | SBOM | misma unidad |
| AMP-49 | AMP | Supply chain de modelos | misma unidad |
| AMP-50 | AMP | Seguridad de herramientas y conectores | misma unidad |
| AMP-51 | AMP | Postura de IA en nube | misma unidad |
| HC-008 | HC | Cadena de confianza en terceros | misma unidad |
| HC-011 | HC | Seguridad de datos en la IA empresarial | misma unidad |
| HC-023 | HC | Riesgo de concentración tecnológica | SE_RELACIONA |
| HC-024 | HC | Cumplimiento y privacidad por diseño | misma unidad |
| HC-029 | HC | Aseguramiento de terceros y cadena de suministro | misma unidad |
| HC-030 | HC | Seguridad industrial y continuidad de negocio | misma unidad |
| HC-031 | HC | Seguridad del software y confianza en componentes | misma unidad |
| HC-032 | HC | Evaluación adversarial de sistemas autónomos | misma unidad |
| HC-033 | HC | Seguridad y soberanía de datos distribuidos | misma unidad |
| M6.2-PA01 | PA | Plataformas y rutas de construcción de agentes y responsabilidad compartida en IA | misma unidad |
| M6.2-PA02 | PA | AgentOps / ALM de agentes | misma unidad |
| G2.1-K07 | K | Interoperabilidad | EXTIENDE (otra unidad) |
| AMP-48 | AMP | Dependencias de modelos | SE_RELACIONA (otra unidad) |

**Pregunta generadora:** Si su organización cambiara de plataforma de correo y de agentes el año próximo, ¿qué parte de todo lo que construyó con este sub-plan seguiría sirviendo tal cual, y qué parte habría que rehacer?

---

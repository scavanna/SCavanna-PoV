# TheNextCISO GM-24 — Pre-ensayos (archivos de inicialización), lote PA-01 (V7.1)

> **GM-24 V7.1 · The Next CISO + Sub-plan PO-GAC** · 2026-11-14. Catálogo: 379 conceptos (245 K · 52 AMP · 40 HC · 42 PA), todos con pre-ensayo íntegro y mapeados a 17 marcos (NIST/ISACA/MITRE/OWASP/CIS/CSA). V7.1 = ChangeSet editorial CS-GM24-V7.1-001 (4 títulos generalizados; sin cambio de IDs, cantidad ni mapeo). Plano A (corpus académico). Referencias DD/K4x/R/eo:OP/COE: marco interno.

**Estado:** ideas centrales para desarrollo editorial; IDs curriculares (asignar `ESS-######` desde el registro SQLite). Estructura de los lotes GM-24 + práctica, próximos pasos y relación con la unidad.

## Inventario

| N.º | ID | Tipo | Unidad | Concepto |
|---|---|---|---|---|
| 001 | G1.1-PA01 | PA | G1.1 | Rol dual especialista/manager y Product Owner de control |
| 002 | G1.2-PA01 | PA | G1.2 | Economía unitaria de agentes: caso de negocio y TCO |
| 003 | G2.1-PA01 | PA | G2.1 | Grilla de ownership: NIST CSF 2.0 × dominios Zero Trust |
| 004 | G2.1-PA02 | PA | G2.1 | Marcos de gobierno de IA aplicados: NIST AI RMF e ISO/IEC 42001 |
| 005 | G2.2-PA01 | PA | G2.2 | Política de uso y gobierno de agentes |
| 006 | G2.2-PA02 | PA | G2.2 | Estándar de ficha de agente (charter) y runbooks de agentes |
| 007 | G2.2-PA03 | PA | G2.2 | Baseline, excepciones y overrides de un control técnico |
| 008 | G3.1-PA01 | PA | G3.1 | Panorama regulatorio de IA y agentes |
| 009 | G3.2-PA01 | PA | G3.2 | Aseguramiento continuo de la configuración del control (deriva) |
| 010 | G4.1-PA01 | PA | G4.1 | Tres líneas de defensa para la flota de agentes |
| 011 | G4.1-PA02 | PA | G4.1 | Taxonomía y registro de riesgos de agentes |
| 012 | G4.2-PA01 | PA | G4.2 | KRIs de la flota de agentes y umbrales de intervención |
| 013 | G6.1-PA01 | PA | G6.1 | Reporte ejecutivo del producto-control y de la fuerza de trabajo híbrida |
| 014 | G6.2-PA01 | PA | G6.2 | Métricas de efectividad del gobierno de la flota |
| 015 | M1.1-PA01 | PA | M1.1 | Diseño organizativo híbrido: roles, RACI y span of control |
| 016 | M1.1-PA02 | PA | M1.1 | Portafolio de productos-control con owners |
| 017 | M1.1-PA03 | PA | M1.1 | Modelo operativo por cadencias y excelencia operacional como requisito del programa |
| 018 | M1.2-PA01 | PA | M1.2 | FinOps de agentes: presupuesto, costo por tarea y alertas de consumo |
| 019 | M1.2-PA02 | PA | M1.2 | Requisitos de IA y agentes en contratos de servicios gestionados |
| 020 | M1.2-PA03 | PA | M1.2 | Itinerario de desarrollo: de analista a PO-GAC |
| 021 | M2.1-PA01 | PA | M2.1 | Registro de agentes como clase de activo |
| 022 | M2.2-PA01 | PA | M2.2 | Permisos de humanos y agentes en el control: RBAC unificado, roles y conectores |
| 023 | M3.1-PA01 | PA | M3.1 | Arquitectura de referencia del SOC agéntico con control plane |
| 024 | M3.1-PA02 | PA | M3.1 | Arquitectura de protección del dominio Zero Trust (instancias: correo y colaboración · detección y respuesta unificada · endpoints · identidades · datos) |

---

### 001. G1.1-PA01 — Rol dual especialista/manager y Product Owner de control

**Unidad:** G1.1 Principios de Gobierno, Contexto Organizacional y Arquetipos CISO · **Tipo:** PA · **Horas (sub-plan):** 4 · **Competencias:** C1.1, C6.1 · **Origen:** G1.1-PA02 (V5) · **Extensión:** 472 palabras · **Estado:** Idea central desarrollada (lote PA-01/02) — sub-plan PO-GAC; ID curricular, no ESS.

**Definición / idea central.** El analista evoluciona a owner de un producto-control (CSF 2.0 × dominio Zero Trust × tecnología × modelo operativo) y a manager de la fuerza de trabajo híbrida que lo opera.

**Brecha frente a los 331.** Ningún K/AMP/HC define el ownership de un control como producto ni el rol intermedio entre analista y CISO.

**Tesis y sentido para el rol.** El analista de ciberseguridad que hoy ejecuta tareas sobre una consola se convierte en owner de un producto-control cuando asume, de forma explícita, cuatro responsabilidades que antes estaban repartidas: definir qué resultado de seguridad debe producir el control (funciones y categorías de NIST CSF 2.0), delimitar qué protege (un dominio Zero Trust, en el escenario la productividad y colaboración), dominar con qué se realiza (Defender for Office 365 dentro de Defender XDR) y sostener cómo se opera (un modelo operativo con cadencias, evidencia y mejora). A esa primera identidad de especialista se suma una segunda: manager de una fuerza de trabajo híbrida compuesta por analistas, agentes cognitivos y servicios contratados. El rol dual no es un ascenso jerárquico sino un cambio de unidad de trabajo: de la tarea al producto, y de la tarea propia al trabajo de otros, humanos o no.

**Tensión y límites.** La tensión aparece porque la organización suele reconocer el ownership de forma implícita —"el que sabe de correo"— sin otorgar autoridad sobre configuración, presupuesto de consumo ni decisiones de autonomía de los agentes. El resultado es responsabilidad sin autoridad, la falla que AMP-03 describe para el CISO y que aquí se reproduce un nivel más abajo. También existe el riesgo inverso: un owner que configura y automatiza sin mandato del dueño del riesgo. El ensayo debe discutir qué decisiones puede tomar el PO-GAC por sí mismo (tuning, listas con vencimiento, aprobación de acciones L2), cuáles requieren al dueño del riesgo (nivel de autonomía, aceptación de residual) y cuáles son del CISO (política, presupuesto).

**Aplicación formativa (base agnóstica → implementación Microsoft).** La base agnóstica es la gestión de producto aplicada a controles: una ficha con objetivo, alcance, usuarios, métricas de éxito, backlog y criterios de retiro, más la descripción de puesto del manager híbrido. La implementación Microsoft consiste en escribir la ficha de rol del PO-GAC para el control de correo y colaboración, indicando permisos (Unified RBAC), tableros, cadencias de la Security Operations Guide y la relación owner–agente que Agent 365 y Entra Agent ID registran como sponsor. El ejercicio pide comparar la ficha con la del analista actual y con los arquetipos de CISO de G1.1-K03 para mostrar la continuidad de carrera.

**Evidencia y evaluación.** La evidencia es la ficha de rol aprobada por el CISO, con una matriz de derechos de decisión en tres niveles. Se evalúa que las decisiones estén asignadas sin huecos ni duplicaciones, que el alcance del control coincida con la grilla de G2.1-PA01 y que el span of control (agentes, contratos, personas) sea realista. Un criterio de calidad es que un tercero pueda leer la ficha y saber a quién preguntar por cualquier decisión del control.

**Puentes.** Se apoya en AMP-27 (CISO-OS) como sistema en el que el rol opera y en AMP-29 (competencias humanas y agentes) como rediseño del equipo; se relaciona con HC-037 (competencias y decisiones) y prepara M1.1-PA01 (diseño organizativo) y M1.2-PA03 (itinerario).

**Recomendaciones de práctica y ejercitación.**
1. Redactar la ficha de rol PO-GAC con matriz de derechos de decisión en tres niveles (PO-GAC / dueño del riesgo / CISO) para el control de correo y colaboración.
2. Comparar esa ficha con la descripción actual del puesto de analista y con los arquetipos de CISO (G1.1-K03): listar las cinco decisiones que hoy nadie tiene asignadas.
3. Simular con el manager una negociación de autoridad: qué se concede, qué se condiciona y qué evidencia se exige a cambio.

**Aplicación en el escenario de referencia.** Base agnóstica: Product ownership; accountability; diseño de puestos. Implementación Microsoft: Ficha de rol PO-GAC sobre Defender for Office 365 en Defender XDR; Agent 365 para la relación owner–agente. Actividad: Redactar la ficha de rol del PO-GAC para el control de correo y colaboración. Evidencia: Ficha de rol.

**Próximos pasos.**
- Llevar la ficha al CISO para aprobación; registrar la decisión y la fecha.
- Usar la ficha como insumo de M1.1-PA01 (organigrama híbrido y RACI) y de M1.2-PA03 (itinerario).
- Verificar en el tenant que los permisos de Unified RBAC coinciden con los derechos de decisión declarados.

**Relación con los conceptos de la(s) unidad(es) G1.1.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| G1.1-K01 | K | Principios de Gobierno | misma unidad |
| G1.1-K02 | K | Contexto Organizacional | misma unidad |
| G1.1-K03 | K | Arquetipos CISO | EXTIENDE |
| G1.1-K04 | K | Alineación Estratégica | misma unidad |
| G1.1-K05 | K | Cultura de Seguridad | misma unidad |
| G1.1-K06 | K | Visión Holística | misma unidad |
| G1.1-K07 | K | CISO como Socio de Negocio | misma unidad |
| G1.1-K08 | K | Gestión Estratégica del Riesgo | misma unidad |
| G1.1-K09 | K | Liderazgo de Influencia | misma unidad |
| G1.1-K10 | K | Mejora Continua (Gobierno) | misma unidad |
| AMP-01 | AMP | Metacognición del CISO | misma unidad |
| AMP-02 | AMP | Sesgos y límites cognitivos | misma unidad |
| AMP-03 | AMP | Autoridad frente a responsabilidad | misma unidad |
| HC-001 | HC | Gobierno de decisiones basadas en evidencia | misma unidad |
| HC-037 | HC | Alineación entre competencias y decisiones | SE_RELACIONA |
| HC-040 | HC | Homeostasis organizacional de seguridad | misma unidad |
| AMP-27 | AMP | CISO-OS | SE_APOYA_EN (otra unidad) |
| AMP-29 | AMP | Competencias humanas y agentes | SE_APOYA_EN (otra unidad) |

**Pregunta generadora:** ¿Qué decisiones sobre el control de correo y colaboración puede tomar hoy el analista sin pedir permiso, cuáles debería poder tomar como PO-GAC y qué autoridad formal falta para cerrar esa brecha?

---

### 002. G1.2-PA01 — Economía unitaria de agentes: caso de negocio y TCO

**Unidad:** G1.2 Desarrollo de Estrategia y Alineación con el Negocio · **Tipo:** PA · **Horas (sub-plan):** 4 · **Competencias:** C8.2, C6.4 · **Origen:** G1.2-PA01 (V5) · **Extensión:** 370 palabras · **Estado:** Idea central desarrollada (lote PA-01/02) — sub-plan PO-GAC; ID curricular, no ESS.

**Definición / idea central.** Caso de negocio con costos variables de consumo (SCU, créditos, tokens), costo por tarea, capacidad liberada medida, riesgo reducido e introducido.

**Brecha frente a los 331.** K05/K06 y HC-006 no consideran costos variables de IA ni costo por tarea.

**Tesis y sentido para el rol.** Un agente cognitivo no se paga una vez: se paga cada vez que trabaja. Esa diferencia obliga a construir el caso de negocio con economía unitaria y no solo con licencias. El costo de un agente del SOC combina una parte fija (plataforma, licencias de Agent 365 o Defender) y una parte variable que depende de la ruta de construcción: SCU si vive en Security Copilot, créditos o capacidad si se construye en Copilot Studio, tokens por modelo si corre en Foundry. El beneficio tampoco es abstracto: son horas del runbook ejecutadas por el agente, incidentes cerrados antes, mensajes maliciosos removidos más rápido y riesgo introducido por el propio agente, que debe restarse. La tesis es que el caso de negocio válido expresa costo por tarea, capacidad liberada medida y riesgo neto, con supuestos explícitos y análisis de sensibilidad.

**Tensión y límites.** La tensión está en la tentación de justificar agentes con horas "ahorradas" que nadie midió y con un consumo que nadie limitó. HC-006 recuerda que inversión, actividad, adopción y efectividad son cosas distintas; aquí se agrega que el consumo puede crecer sin que crezca el valor, por ejemplo si un agente re-investiga incidentes ya cerrados o resume informes que nadie lee. El ensayo debe tratar el costo descontrolado como riesgo (G4.1-PA02) y no solo como gasto.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: unit economics, TCO y ROSI con beneficios verificables. Implementación: modelar tres agentes del catálogo (AG-10, AG-03, AG-05) con su unidad de consumo, frecuencia, costo por ejecución y horas del runbook que asisten; comparar con la alternativa humana y con un servicio gestionado; definir el presupuesto trimestral y las alertas en Azure Cost Management. El ejercicio exige declarar qué pasa con el caso si el consumo se duplica o si la tasa de aceptación de propuestas cae al 70 %.

**Evidencia y evaluación.** La evidencia es un caso de negocio con tabla de supuestos, costo por tarea por agente, capacidad liberada expresada en horas medibles (KPI-18) y riesgo introducido con su mitigación. Se evalúa la trazabilidad de cada cifra a una fuente (tarifa, frecuencia del runbook, KPI histórico) y la honestidad del análisis de sensibilidad.

**Puentes.** Extiende G1.2-K05 (casos de negocio) y G1.2-K06 (ROI); profundiza HC-006 (medición causal); alimenta M1.2-PA01 (FinOps) y la decisión de ruta en M6.2-PA01.

**Recomendaciones de práctica y ejercitación.**
1. Construir el modelo de costo por tarea de AG-10, AG-03 y AG-05 (unidad de consumo × frecuencia + parte fija prorrateada) y compararlo con la alternativa humana y con un MDR.
2. Correr dos escenarios de sensibilidad: consumo ×2 y tasa de aceptación de propuestas al 70 %; documentar qué agente deja de justificarse.
3. Redactar el caso de negocio en una página con tabla de supuestos y fuente por cifra.

**Aplicación en el escenario de referencia.** Base agnóstica: Unit economics; ROSI; TCO. Implementación Microsoft: Costo de SCU, capacidad de Copilot Studio y consumo de Foundry; licencias Agent 365/Defender. Actividad: Construir el caso de negocio de 3 agentes con supuestos explícitos y sensibilidad. Evidencia: Caso de negocio.

**Próximos pasos.**
- Validar las tarifas de SCU, capacidad de Copilot Studio y modelos de Foundry en el tenant antes de presentar.
- Trasladar el modelo a M1.2-PA01 (presupuesto, alertas) y al KPI-18 (horas liberadas medidas).
- Registrar el 'costo descontrolado' como riesgo en G4.1-PA02.

**Relación con los conceptos de la(s) unidad(es) G1.2.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| G1.2-K01 | K | Estrategia de Ciberseguridad | misma unidad |
| G1.2-K02 | K | Alineación con Negocio | misma unidad |
| G1.2-K03 | K | Influencias y Tendencias | misma unidad |
| G1.2-K04 | K | Conexión de Valor | misma unidad |
| G1.2-K05 | K | Casos de Negocio | EXTIENDE |
| G1.2-K06 | K | ROI en Seguridad | EXTIENDE |
| G1.2-K07 | K | Visión de Negocio | misma unidad |
| G1.2-K08 | K | Planificación Estratégica | misma unidad |
| G1.2-K09 | K | Integración ERM | misma unidad |
| G1.2-K10 | K | Comunicación a la Junta | misma unidad |
| AMP-04 | AMP | Estrategia adaptativa | misma unidad |
| AMP-05 | AMP | Evolución contextual H | misma unidad |
| AMP-06 | AMP | Gobierno de la IA | misma unidad |
| HC-006 | HC | Valor de seguridad y medición causal | PROFUNDIZA |
| HC-013 | HC | Deuda de seguridad como riesgo de transformación | misma unidad |
| HC-014 | HC | Arquitectura de riesgo empresarial | misma unidad |
| HC-023 | HC | Riesgo de concentración tecnológica | misma unidad |
| HC-034 | HC | Decisiones reversibles y riesgo de transición | misma unidad |
| HC-035 | HC | Aprendizaje desde incidentes hasta políticas | misma unidad |
| HC-039 | HC | Riesgo cibernético como narrativa empresarial | misma unidad |
| AMP-29 | AMP | Competencias humanas y agentes | SE_RELACIONA (otra unidad) |

**Pregunta generadora:** ¿Cuánto cuesta que el agente triaje un incidente, cuánto cuesta que lo haga un analista y cuánto cuesta equivocarse en cada caso?

---

### 003. G2.1-PA01 — Grilla de ownership: NIST CSF 2.0 × dominios Zero Trust

**Unidad:** G2.1 Selección e Integración de Marcos y Estándares · **Tipo:** PA · **Horas (sub-plan):** 6 · **Competencias:** C1.2, C1.1 · **Origen:** G2.1-PA01 + G2.1-PA04 (V5) · **Extensión:** 340 palabras · **Estado:** Idea central desarrollada (lote PA-01/02) — sub-plan PO-GAC; ID curricular, no ESS.

**Definición / idea central.** Funciones/categorías del CSF 2.0 y pilares Zero Trust como coordenadas para asignar ownership de productos-control.

**Brecha frente a los 331.** El CSF se enseña como marco y Zero Trust como arquitectura; ninguno los usa como instrumento de asignación de ownership.

**Tesis y sentido para el rol.** NIST CSF 2.0 se enseña habitualmente como marco para conversar sobre resultados de seguridad; Zero Trust, como arquitectura. Este concepto propone usarlos juntos como un instrumento de asignación de ownership: las funciones y categorías del CSF indican qué resultado debe producir un control; los pilares de Zero Trust indican qué dominio protege; la tecnología dice con qué se realiza y el modelo operativo cómo se opera. El cruce de esas coordenadas define un producto-control y, por lo tanto, a quién pertenece. La tesis es que una organización puede dibujar su mapa de productos-control con esta grilla y descubrir controles sin dueño, dueños sin control y solapamientos que hoy se resuelven por costumbre.

**Tensión y límites.** La tensión es doble. Primero, los marcos no fueron diseñados para asignar personas: forzar una correspondencia uno a uno produce falsos ownerships, y AMP-08 advierte que los mapeos son referencias informativas. Segundo, Zero Trust tiene pilares que se solapan (identidades y aplicaciones, datos y productividad) y un control como Defender for Office 365 cruza varios. El ensayo debe mostrar cómo decidir el dominio principal y los secundarios sin pretender exclusividad.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: CSF 2.0 (incluida la función Govern) y SP 800-207. Implementación: construir la grilla para el control de correo y colaboración —GV.PO y PR.PS para políticas y presets, DE.AE y DE.CM para incidentes y monitoreo, RS.AN y RS.MI para investigación y remediación, ID.IM para la mejora— y luego extenderla a los siete pilares de una organización tipo, definiendo tres productos-control con owner, tecnología y modelo operativo. HC-015 aporta la vista de gobierno y operación de Zero Trust para verificar que la grilla no deje fuera políticas ni evidencia.

**Evidencia y evaluación.** Evidencia: la grilla completa y un catálogo de tres productos-control. Se evalúa que cada celda tenga un dueño único, que las categorías del CSF estén usadas con su intención original y que los solapamientos estén declarados con un criterio de arbitraje.

**Puentes.** Operacionaliza G2.1-K04 (NIST CSF) y se apoya en AMP-07 (CSF 2.0 Govern); complementa HC-015 y HC-038; es el insumo de M1.1-PA02 (portafolio) y de la ficha de producto-control.

**Recomendaciones de práctica y ejercitación.**
1. Completar la grilla función/categoría CSF 2.0 × pilar Zero Trust para el control de correo y colaboración, marcando dominio principal y secundarios.
2. Extender la grilla a los siete pilares de una organización tipo y detectar celdas sin dueño y celdas con dos dueños; proponer el criterio de arbitraje.
3. Definir tres productos-control (p. ej., correo y colaboración, identidades, endpoints) con owner, tecnología y modelo operativo.

**Aplicación en el escenario de referencia.** Base agnóstica: NIST CSF 2.0; NIST SP 800-207. Implementación Microsoft: Grilla del control MDO: GV.PO/PR.PS, DE.AE/DE.CM, RS.AN/RS.MI, ID.IM; dominio productividad. Actividad: Completar la grilla para los 7 pilares Zero Trust y definir 3 productos-control con owner. Evidencia: Grilla + catálogo de 3 productos-control.

**Próximos pasos.**
- Validar la grilla con el CISO y los owners actuales; registrar los solapamientos aceptados.
- Usar la grilla como insumo de M1.1-PA02 (portafolio) y de la ficha de producto-control (C1.1).
- Revisar la grilla cuando cambie la tecnología o el alcance del dominio.

**Relación con los conceptos de la(s) unidad(es) G2.1.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| G2.1-K01 | K | Marcos de Gobierno | misma unidad |
| G2.1-K02 | K | COBIT | misma unidad |
| G2.1-K03 | K | ISO 27001 (SGSI) | misma unidad |
| G2.1-K04 | K | NIST CSF | OPERACIONALIZA |
| G2.1-K05 | K | Estándares Relevantes | misma unidad |
| G2.1-K06 | K | Adaptación (Tailoring) | misma unidad |
| G2.1-K07 | K | Interoperabilidad | misma unidad |
| G2.1-K08 | K | Medición de Madurez | misma unidad |
| G2.1-K09 | K | Tendencias en Marcos | misma unidad |
| G2.1-K10 | K | Evolución Histórica | misma unidad |
| AMP-07 | AMP | NIST CSF 2.0 Govern | SE_APOYA_EN |
| AMP-08 | AMP | Referencias informativas y no equivalencia | misma unidad |
| G2.1-K11 | K | CSF 2.0 completo: funciones, categorías y perfiles organizacionales | misma unidad |
| G2.1-PA02 | PA | Marcos de gobierno de IA aplicados: NIST AI RMF e ISO/IEC 42001 | misma unidad |
| HC-015 | HC | Gobierno y operación de Zero Trust | COMPLEMENTA (otra unidad) |
| M2.2-K05 | K | Zero Trust | SE_RELACIONA (otra unidad) |

**Pregunta generadora:** Si tuviera que señalar con el dedo al dueño de cada celda de la grilla CSF × Zero Trust de su organización, ¿cuántas celdas quedarían vacías y cuántas tendrían dos dedos apuntando?

---

### 004. G2.1-PA02 — Marcos de gobierno de IA aplicados: NIST AI RMF e ISO/IEC 42001

**Unidad:** G2.1 Selección e Integración de Marcos y Estándares · **Tipo:** PA · **Horas (sub-plan):** 4 · **Competencias:** C5.1 · **Origen:** G2.1-PA02 (V5) · **Extensión:** 305 palabras · **Estado:** Idea central desarrollada (lote PA-01/02) — sub-plan PO-GAC; ID curricular, no ESS.

**Definición / idea central.** GOVERN/MAP/MEASURE/MANAGE y el sistema de gestión de IA de ISO/IEC 42001 aplicados a los agentes del SOC y conectados con el SGSI.

**Brecha frente a los 331.** AMP-06 y HC-012 no nombran ni aplican los marcos.

**Tesis y sentido para el rol.** Gobernar la IA, en los términos de AMP-06, es decidir quién la usa, con qué datos, con qué autonomía y con qué evidencia. Dos marcos públicos permiten convertir esa decisión en un sistema verificable: NIST AI RMF, con sus funciones GOVERN, MAP, MEASURE y MANAGE y su perfil para IA generativa, e ISO/IEC 42001, que define un sistema de gestión de IA con un Anexo A de controles. La tesis es que el owner de agentes no necesita un gobierno paralelo: necesita conectar sus controles de agentes (los AGC del sub-plan) con esos marcos y con el SGSI existente, de modo que una auditoría pueda leer una sola cadena de política, control y evidencia.

**Tensión y límites.** La tensión está en la falsa equivalencia. Mapear un control a una categoría del AI RMF o a un control del Anexo A no demuestra conformidad; solo indica dónde buscar evidencia. También existe el riesgo de duplicar el SGSI con un "SGIA" desconectado, con comités y registros propios que nadie mantiene. El ensayo debe discutir cómo integrar sin duplicar y cómo declarar el nivel de correspondencia de cada mapeo.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: AI RMF 1.0 y su perfil GenAI; ISO/IEC 42001; el perfil agéntico de CSA como extensión en borrador. Implementación: mapear los 24 AGC a funciones del AI RMF y a controles del Anexo A, usando Purview Compliance Manager como repositorio de evidencias cuando existan plantillas aplicables, y marcar cada correspondencia como fuerte, parcial o informativa.

**Evidencia y evaluación.** Evidencia: matriz AGC × AI RMF × ISO 42001 con nivel de correspondencia y evidencia esperada por control. Se evalúa la ausencia de equivalencias forzadas y la claridad sobre qué evidencia produciría cada control en el tenant.

**Puentes.** Operacionaliza AMP-06 (gobierno de la IA) y se apoya en HC-012 (confianza verificable); instancia G2.1-K05 (estándares relevantes); respeta AMP-08 (no equivalencia). Alimenta G2.2-PA01 (política) y M3.2-PA02 (catálogo AGC).

**Recomendaciones de práctica y ejercitación.**
1. Mapear los 24 AGC a las funciones y categorías del AI RMF y a los controles del Anexo A de ISO/IEC 42001, marcando cada correspondencia como fuerte, parcial o informativa.
2. Para AG-02 (remediación), listar la evidencia del tenant que respaldaría cada función del AI RMF y señalar la que hoy no existe.
3. Identificar qué registros del SGSI ya cubren controles de agentes para no duplicar comités ni repositorios.

**Aplicación en el escenario de referencia.** Base agnóstica: NIST AI RMF 1.0 + AI 600-1; ISO/IEC 42001. Implementación Microsoft: Purview Compliance Manager como repositorio de evidencias. Actividad: Mapear los 24 AGC a AI RMF e ISO 42001 con nivel de correspondencia. Evidencia: Matriz de mapeo.

**Próximos pasos.**
- Cargar la matriz en Purview Compliance Manager si existe plantilla aplicable; si no, en el GRC.
- Usar la matriz como base de G2.2-PA01 (política) y M3.2-PA02 (catálogo AGC).
- Revisar la matriz cuando cambien las versiones de AI RMF/ISO 42001 o el perfil agéntico de CSA.

**Relación con los conceptos de la(s) unidad(es) G2.1.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| G2.1-K01 | K | Marcos de Gobierno | misma unidad |
| G2.1-K02 | K | COBIT | misma unidad |
| G2.1-K03 | K | ISO 27001 (SGSI) | misma unidad |
| G2.1-K04 | K | NIST CSF | misma unidad |
| G2.1-K05 | K | Estándares Relevantes | INSTANCIA_DE |
| G2.1-K06 | K | Adaptación (Tailoring) | misma unidad |
| G2.1-K07 | K | Interoperabilidad | misma unidad |
| G2.1-K08 | K | Medición de Madurez | misma unidad |
| G2.1-K09 | K | Tendencias en Marcos | misma unidad |
| G2.1-K10 | K | Evolución Histórica | misma unidad |
| AMP-07 | AMP | NIST CSF 2.0 Govern | misma unidad |
| AMP-08 | AMP | Referencias informativas y no equivalencia | SE_RELACIONA |
| G2.1-K11 | K | CSF 2.0 completo: funciones, categorías y perfiles organizacionales | misma unidad |
| G2.1-PA01 | PA | Grilla de ownership: NIST CSF 2.0 × dominios Zero Trust | misma unidad |
| AMP-06 | AMP | Gobierno de la IA | OPERACIONALIZA (otra unidad) |
| HC-012 | HC | Confianza verificable en decisiones de IA | SE_APOYA_EN (otra unidad) |

**Pregunta generadora:** ¿Qué evidencia concreta del tenant respaldaría cada función del AI RMF para un agente que remueve correo de buzones, y cuál de esas evidencias hoy no existe?

---

### 005. G2.2-PA01 — Política de uso y gobierno de agentes

**Unidad:** G2.2 Ciclo de Vida de Políticas, Estándares y Procedimientos · **Tipo:** PA · **Horas (sub-plan):** 4 · **Competencias:** C5.1, C1.5 · **Origen:** G2.2-PA01 (V5) · **Extensión:** 309 palabras · **Estado:** Idea central desarrollada (lote PA-01/02) — sub-plan PO-GAC; ID curricular, no ESS.

**Definición / idea central.** Documento normativo con alcance, autorizaciones, prohibiciones, autonomía permitida, identidad, datos, evidencia y revisión para agentes.

**Brecha frente a los 331.** Falta el artefacto normativo concreto para agentes en la jerarquía documental.

**Tesis y sentido para el rol.** Una política de agentes es el documento que convierte los principios de gobierno de la IA en reglas exigibles: qué agentes se permiten, quién puede crearlos, qué identidades y datos usan, qué niveles de autonomía están autorizados por tipo de acción, qué evidencia deben producir y cuándo se revisan o retiran. Sin ese documento, los agentes se gobiernan por la configuración por defecto de la plataforma, que no conoce el apetito de riesgo de la organización. La tesis es que la política de agentes debe ocupar un lugar explícito en la jerarquía documental (política → estándar de ficha → procedimientos de operación) y tener una matriz de aplicación técnica que diga qué control de plataforma hace cumplir cada regla.

**Tensión y límites.** La tensión es entre generalidad y aplicabilidad. Una política demasiado abstracta no cambia nada en Copilot Studio; una demasiado técnica queda obsoleta con cada versión de la plataforma. AMP-09 sugiere la salida: expresar lo que se pueda como política aplicada por configuración (policy-as-code) y reservar el texto normativo para autoridad, prohibiciones y excepciones. El ensayo debe tratar también la tensión entre habilitar creadores y controlar la proliferación (Shadow AI, M6.2-K06).

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: ISO/IEC 42001 A.2 (políticas de IA) y AI RMF GOVERN. Implementación: redactar una política de tres páginas y su matriz de aplicación con políticas de datos y conectores de Power Platform, controles de compartición, plantillas de política de Agent 365 y Conditional Access para agentes. El ejercicio pide identificar al menos una regla que la plataforma no puede aplicar y que requiere control humano.

**Evidencia y evaluación.** Evidencia: política aprobada y matriz regla → control técnico → evidencia. Se evalúa la trazabilidad a AMP-06, la ausencia de reglas inaplicables y la definición de excepciones con dueño y caducidad.

**Puentes.** Operacionaliza AMP-06; instancia G2.2-K02 (desarrollo de políticas); se relaciona con AMP-09 (policy-as-code). Es prerrequisito de G2.2-PA02 (ficha) y de los AGC-01 a AGC-04.

**Recomendaciones de práctica y ejercitación.**
1. Redactar la política de agentes (3 páginas) con alcance, autoridades, prohibiciones, autonomía permitida por tipo de acción, identidad, datos, evidencia y revisión.
2. Construir la matriz regla → control técnico (DLP y conectores de Power Platform, compartición, plantillas de Agent 365, Conditional Access) → evidencia; marcar al menos una regla que solo un humano puede hacer cumplir.
3. Contrastar la política con la configuración por defecto del entorno de desarrollo de Copilot Studio y listar las reglas que hoy se violarían.

**Aplicación en el escenario de referencia.** Base agnóstica: ISO/IEC 42001 A.2; AI RMF GOVERN. Implementación Microsoft: Políticas de Power Platform (DLP, conectores, compartición); Copilot Control System; plantillas de Agent 365. Actividad: Redactar la política de agentes (3 páginas) y su matriz de aplicación técnica. Evidencia: Política aprobada.

**Próximos pasos.**
- Aprobar la política con el CISO y la segunda línea; publicar la versión y la fecha de revisión.
- Derivar el estándar de ficha (G2.2-PA02) y los controles AGC-01 a AGC-04.
- Revisar la matriz de aplicación tras cada cambio relevante de la plataforma (AG-09).

**Relación con los conceptos de la(s) unidad(es) G2.2.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| G2.2-K01 | K | Jerarquía Documental | misma unidad |
| G2.2-K02 | K | Desarrollo de Políticas | INSTANCIA_DE |
| G2.2-K03 | K | Estándares de Seguridad | misma unidad |
| G2.2-K04 | K | Procedimientos | misma unidad |
| G2.2-K05 | K | Comunicación | misma unidad |
| G2.2-K06 | K | Aplicación (Enforcement) | misma unidad |
| G2.2-K07 | K | Mantenimiento | misma unidad |
| G2.2-K08 | K | Control de Versiones | misma unidad |
| G2.2-K09 | K | Excepciones | misma unidad |
| G2.2-K10 | K | Rol de Auditoría | misma unidad |
| AMP-09 | AMP | Policy-as-code | SE_RELACIONA |
| AMP-10 | AMP | Gobierno de excepciones automatizadas | misma unidad |
| HC-004 | HC | Política como código gobernado | misma unidad |
| HC-013 | HC | Deuda de seguridad como riesgo de transformación | misma unidad |
| HC-015 | HC | Gobierno y operación de Zero Trust | misma unidad |
| HC-028 | HC | Gestión de excepciones y compensaciones | misma unidad |
| HC-035 | HC | Aprendizaje desde incidentes hasta políticas | misma unidad |
| HC-038 | HC | Aseguramiento de la arquitectura Zero Trust | misma unidad |
| G2.2-PA02 | PA | Estándar de ficha de agente (charter) y runbooks de agentes | misma unidad |
| G2.2-PA03 | PA | Baseline, excepciones y overrides de un control técnico | misma unidad |
| AMP-06 | AMP | Gobierno de la IA | OPERACIONALIZA (otra unidad) |

**Pregunta generadora:** ¿Qué regla de su política de agentes sería violada hoy por la configuración por defecto de la plataforma, y quién lo notaría?

---

### 006. G2.2-PA02 — Estándar de ficha de agente (charter) y runbooks de agentes

**Unidad:** G2.2 Ciclo de Vida de Políticas, Estándares y Procedimientos · **Tipo:** PA · **Horas (sub-plan):** 4 · **Competencias:** C4.2, C3.1 · **Origen:** G2.2-PA02 (V5) · **Extensión:** 333 palabras · **Estado:** Idea central desarrollada (lote PA-01/02) — sub-plan PO-GAC; ID curricular, no ESS.

**Definición / idea central.** Estándar que describe cada agente (propósito, tareas, herramientas, límites, autonomía, dueño, KPIs, escalamiento) y sus procedimientos de operación.

**Brecha frente a los 331.** AMP-28/36 piden roles y límites pero no definen el estándar documental.

**Tesis y sentido para el rol.** Un agente sin ficha es un empleado sin descripción de puesto: nadie sabe qué debe hacer, hasta dónde puede llegar ni cómo se evalúa. El estándar de ficha de agente (charter) establece los campos mínimos que todo agente debe declarar antes de operar: propósito, tareas del modelo operativo que asiste, entradas y salidas con su clasificación, herramientas y conectores permitidos, fuentes de conocimiento aprobadas, nivel de autonomía por tipo de acción, límites y cuotas, identidad y sponsor, KPIs y umbrales, costo esperado, riesgos y mitigaciones, escalamiento, versión y vigencia. Los runbooks de agentes completan el estándar con los procedimientos de operación: cómo se aprueba, se pausa, se revisa y se retira. La tesis es que la ficha es el objeto que une gobierno (autoriza), gestión (opera) y aseguramiento (verifica).

**Tensión y límites.** La tensión es que la plataforma ya pide "descripción" e "instrucciones" y resulta tentador creer que eso es la ficha. No lo es: la descripción en Copilot Studio habla al modelo; la ficha habla al dueño del riesgo y al auditor. Otra tensión es la deriva: la ficha se escribe una vez y las instrucciones cambian veinte veces. AMP-28 y AMP-36 recuerdan que los límites y traspasos deben ser explícitos y trazables; el estándar debe exigir versionado de la ficha junto con el agente.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: documentación de sistemas y diseño de puestos. Implementación: completar la ficha de tres agentes (AG-10, AG-03, AG-05) y mapear cada campo a dónde vive en la plataforma (descripción e instrucciones en Copilot Studio, permisos en Power Platform admin center, identidad en Entra Agent ID, perfil en Agent 365). El ejercicio pide escribir el runbook de pausa y retiro de uno de ellos.

**Evidencia y evaluación.** Evidencia: tres fichas aprobadas y un runbook. Se evalúa la completitud, la coherencia entre nivel de autonomía y permisos efectivos, y que cada KPI tenga una fuente de datos real.

**Puentes.** Instancia G2.2-K03 (estándares) y G2.2-K04 (procedimientos); se apoya en AMP-28 (orquestación) y AMP-36 (límites de herramientas). Es el AGC-03 y el insumo del expediente ATO (AMP-22).

**Recomendaciones de práctica y ejercitación.**
1. Completar la ficha de AG-10, AG-03 y AG-05 con los anexos de agente del sub-plan (tools, knowledge, skills propios y comunes).
2. Mapear cada campo de la ficha a su ubicación en la plataforma (Copilot Studio, Power Platform admin center, Entra Agent ID, Agent 365).
3. Escribir el runbook de pausa y retiro de AG-03 y ejecutarlo en el entorno de desarrollo.

**Aplicación en el escenario de referencia.** Base agnóstica: Documentación de sistemas; job descriptions. Implementación Microsoft: Plantilla de ficha; descripción e instrucciones en Copilot Studio; perfil en Agent 365. Actividad: Completar la ficha de 3 agentes (AG-10, AG-03, AG-05). Evidencia: Fichas aprobadas.

**Próximos pasos.**
- Versionar la ficha junto con el agente en el ALM (M6.2-PA02).
- Usar la ficha como pieza 1 del expediente ATO (AMP-22).
- Revisar la coherencia entre autonomía declarada y permisos efectivos en cada cambio (M2.2-PA01).

**Relación con los conceptos de la(s) unidad(es) G2.2.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| G2.2-K01 | K | Jerarquía Documental | misma unidad |
| G2.2-K02 | K | Desarrollo de Políticas | misma unidad |
| G2.2-K03 | K | Estándares de Seguridad | INSTANCIA_DE |
| G2.2-K04 | K | Procedimientos | INSTANCIA_DE |
| G2.2-K05 | K | Comunicación | misma unidad |
| G2.2-K06 | K | Aplicación (Enforcement) | misma unidad |
| G2.2-K07 | K | Mantenimiento | misma unidad |
| G2.2-K08 | K | Control de Versiones | misma unidad |
| G2.2-K09 | K | Excepciones | misma unidad |
| G2.2-K10 | K | Rol de Auditoría | misma unidad |
| AMP-09 | AMP | Policy-as-code | misma unidad |
| AMP-10 | AMP | Gobierno de excepciones automatizadas | misma unidad |
| HC-004 | HC | Política como código gobernado | misma unidad |
| HC-013 | HC | Deuda de seguridad como riesgo de transformación | misma unidad |
| HC-015 | HC | Gobierno y operación de Zero Trust | misma unidad |
| HC-028 | HC | Gestión de excepciones y compensaciones | misma unidad |
| HC-035 | HC | Aprendizaje desde incidentes hasta políticas | misma unidad |
| HC-038 | HC | Aseguramiento de la arquitectura Zero Trust | misma unidad |
| G2.2-PA01 | PA | Política de uso y gobierno de agentes | misma unidad |
| G2.2-PA03 | PA | Baseline, excepciones y overrides de un control técnico | misma unidad |
| AMP-28 | AMP | Orquestación de agentes | SE_APOYA_EN (otra unidad) |
| AMP-36 | AMP | Límites de herramientas y permisos | SE_APOYA_EN (otra unidad) |

**Pregunta generadora:** Si un auditor leyera solo la ficha de su agente, ¿podría predecir qué hará y qué no hará mañana, y verificarlo después contra los registros?

---

### 007. G2.2-PA03 — Baseline, excepciones y overrides de un control técnico

**Unidad:** G2.2 Ciclo de Vida de Políticas, Estándares y Procedimientos · **Tipo:** PA · **Horas (sub-plan):** 4 · **Competencias:** C1.5, C2.4 · **Origen:** G2.2-PA03 (V5) · **Extensión:** 310 palabras · **Estado:** Idea central desarrollada (lote PA-01/02) — sub-plan PO-GAC; ID curricular, no ESS.

**Definición / idea central.** Baseline (Standard/Strict), excepciones, overrides y revisiones periódicas como instancias de la jerarquía documental, con vencimiento y evidencia.

**Brecha frente a los 331.** HC-028 y AMP-10 son generales; falta el puente política → configuración de producto.

**Tesis y sentido para el rol.** Un control técnico tiene su propia jerarquía documental, aunque no se la llame así: el baseline (en Defender for Office 365, las políticas preestablecidas Standard y Strict) funciona como estándar; cada excepción, lista de permitidos y override es una desviación que requiere evaluación de riesgo, autoridad y vigencia; y la revisión periódica de configuración es el mantenimiento. La tesis es que el owner debe tratar la configuración del control con la misma disciplina que G2.2 exige a las políticas: versionada, con excepciones registradas, con caducidad y con evidencia de revisión. Lo que HC-028 plantea para excepciones y compensaciones y AMP-10 para las excepciones automatizadas encuentra aquí su instancia concreta: una entrada en Tenant Allow/Block List es una excepción, y debe vencer.

**Tensión y límites.** La tensión es operativa: las excepciones se crean bajo presión (un ejecutivo no recibe un correo) y nadie vuelve a revisarlas; los overrides acumulados debilitan la detección sin que ninguna métrica lo muestre. Otra tensión es la autoridad: ¿quién puede autorizar que un dominio sea permitido para toda la organización? El ensayo debe argumentar por qué la caducidad por defecto y el informe de overrides son controles de gobierno, no detalles administrativos.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: configuration baseline management y gestión de excepciones. Implementación: diseñar el procedimiento de excepciones del control de correo con solicitud, evaluación, aprobador según impacto, caducidad, registro y revisión mensual; usar Configuration Analyzer para detectar desviaciones del baseline y el informe de overrides para depurar excepciones no justificadas. El ejercicio pide clasificar diez excepciones reales o simuladas por riesgo y proponer cuáles vencen.

**Evidencia y evaluación.** Evidencia: procedimiento aprobado y registro de excepciones con vencimiento y dueño. Se evalúa que ninguna excepción carezca de justificación y fecha, y que el informe de overrides forme parte de la cadencia mensual (MDO-M02).

**Puentes.** Instancia G2.2-K09 (excepciones); profundiza HC-028; se apoya en AMP-10 y se relaciona con AMP-09. Alimenta G3.2-PA01 (deriva) y el KPI-07.

**Recomendaciones de práctica y ejercitación.**
1. Diseñar el procedimiento de excepciones del control de correo (solicitud, evaluación, aprobador por impacto, caducidad, registro, revisión mensual).
2. Clasificar diez excepciones (reales o simuladas) de Tenant Allow/Block List y overrides por riesgo; proponer cuáles vencen y cuándo.
3. Ejecutar Configuration Analyzer frente a Standard/Strict y documentar cada desviación como error o excepción con dueño.

**Aplicación en el escenario de referencia.** Base agnóstica: Configuration baseline management; gestión de excepciones. Implementación Microsoft: Preset security policies, Configuration Analyzer, informe de overrides, Tenant Allow/Block List con vencimientos. Actividad: Diseñar el procedimiento de excepciones del control de correo con caducidad y dueño. Evidencia: Procedimiento.

**Próximos pasos.**
- Incorporar la revisión de overrides a la cadencia mensual (MDO-M02) y definir el KPI-07.
- Conectar el procedimiento con el control continuo de deriva (G3.2-PA01) y con AG-10/AG-11.
- Proponer la caducidad por defecto como regla de la política de agentes y del control.

**Relación con los conceptos de la(s) unidad(es) G2.2.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| G2.2-K01 | K | Jerarquía Documental | misma unidad |
| G2.2-K02 | K | Desarrollo de Políticas | misma unidad |
| G2.2-K03 | K | Estándares de Seguridad | misma unidad |
| G2.2-K04 | K | Procedimientos | misma unidad |
| G2.2-K05 | K | Comunicación | misma unidad |
| G2.2-K06 | K | Aplicación (Enforcement) | misma unidad |
| G2.2-K07 | K | Mantenimiento | misma unidad |
| G2.2-K08 | K | Control de Versiones | misma unidad |
| G2.2-K09 | K | Excepciones | INSTANCIA_DE |
| G2.2-K10 | K | Rol de Auditoría | misma unidad |
| AMP-09 | AMP | Policy-as-code | SE_RELACIONA |
| AMP-10 | AMP | Gobierno de excepciones automatizadas | SE_APOYA_EN |
| HC-004 | HC | Política como código gobernado | misma unidad |
| HC-013 | HC | Deuda de seguridad como riesgo de transformación | misma unidad |
| HC-015 | HC | Gobierno y operación de Zero Trust | misma unidad |
| HC-028 | HC | Gestión de excepciones y compensaciones | PROFUNDIZA |
| HC-035 | HC | Aprendizaje desde incidentes hasta políticas | misma unidad |
| HC-038 | HC | Aseguramiento de la arquitectura Zero Trust | misma unidad |
| G2.2-PA01 | PA | Política de uso y gobierno de agentes | misma unidad |
| G2.2-PA02 | PA | Estándar de ficha de agente (charter) y runbooks de agentes | misma unidad |

**Pregunta generadora:** ¿Cuántas excepciones de su control de correo tienen fecha de vencimiento, y qué pasaría con la detección si todas las que no la tienen fueran legítimas hace un año pero no hoy?

---

### 008. G3.1-PA01 — Panorama regulatorio de IA y agentes

**Unidad:** G3.1 Requisitos Legales, Regulatorios y Contractuales · **Tipo:** PA · **Horas (sub-plan):** 3 · **Competencias:** C5.4, C5.1 · **Origen:** G3.1-PA01 (V5) · **Extensión:** 297 palabras · **Estado:** Idea central desarrollada (lote PA-01/02) — sub-plan PO-GAC; ID curricular, no ESS.

**Definición / idea central.** Obligaciones (EU AI Act, normas locales, privacidad) que afectan a agentes que procesan datos personales o toman decisiones.

**Brecha frente a los 331.** K01/K03 y AMP-11/12 no recorren la regulación específica de IA.

**Tesis y sentido para el rol.** Los agentes que leen correo, acceden a buzones y toman acciones sobre comunicaciones de personas operan dentro de un panorama regulatorio que ya no es solo el de la seguridad de la información: la regulación de IA (con el EU AI Act como referencia más desarrollada), las leyes de privacidad y las normas sectoriales imponen obligaciones de transparencia, supervisión humana, registro y gestión de riesgo según el nivel de riesgo del sistema. La tesis es que el owner debe clasificar sus agentes por exposición regulatoria antes de desplegarlos, porque esa clasificación determina qué evidencia, qué supervisión y qué comunicación a los usuarios son exigibles.

**Tensión y límites.** La tensión es que la mayoría de los agentes del SOC procesan datos personales de forma incidental (remitentes, destinatarios, contenido de mensajes) y la organización tiende a tratarlos como herramientas internas sin impacto regulatorio. El ensayo debe discutir cuándo un agente que decide sobre el correo de un empleado es un sistema que afecta derechos y cuándo es un filtro técnico, y qué cambia en cada caso. También debe reconocer la incertidumbre: la regulación evoluciona y los criterios locales difieren.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: EU AI Act (categorías de riesgo y obligaciones), GDPR y marcos locales; AMP-11 (soberanía) y AMP-12 (responsabilidad) como lentes. Implementación: clasificar los quince agentes del catálogo por nivel de riesgo regulatorio, identificar para cada uno las obligaciones aplicables y la evidencia que las satisface (Purview Audit, retención, disclosure), y marcar los que requieren consulta a Legal y Privacidad.

**Evidencia y evaluación.** Evidencia: clasificación con justificación y lista de obligaciones por agente. Se evalúa la prudencia (no sobreclasificar ni subestimar) y la conexión con los controles AGC-11 (trazabilidad) y AGC-21 (transparencia).

**Puentes.** Extiende G3.1-K01 (identificación de requisitos) y K03 (regulaciones sectoriales); se relaciona con AMP-11 y AMP-12. Alimenta el expediente ATO (AMP-22) con la dimensión regulatoria.

**Recomendaciones de práctica y ejercitación.**
1. Clasificar los 15 agentes del catálogo por exposición regulatoria (datos personales que tocan, decisiones sobre personas, jurisdicción) con justificación.
2. Para los tres de mayor exposición, listar obligaciones aplicables y la evidencia del tenant que las satisface (Purview Audit, retención, disclosure).
3. Preparar las preguntas para Legal y Privacidad sobre los casos dudosos.

**Aplicación en el escenario de referencia.** Base agnóstica: EU AI Act; GDPR; marcos locales. Implementación Microsoft: Purview (retención, auditoría); Compliance Manager. Actividad: Clasificar los agentes del catálogo por nivel de riesgo regulatorio. Evidencia: Clasificación.

**Próximos pasos.**
- Incorporar la clasificación regulatoria como pieza 9 del expediente ATO (AMP-22).
- Revisar la clasificación ante cambios regulatorios o de alcance de los agentes.
- Conectar con AGC-11 (trazabilidad) y AGC-21 (transparencia).

**Relación con los conceptos de la(s) unidad(es) G3.1.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| G3.1-K01 | K | Identificación de Requisitos | EXTIENDE |
| G3.1-K02 | K | Leyes de Privacidad | misma unidad |
| G3.1-K03 | K | Regulaciones Sectoriales | EXTIENDE |
| G3.1-K04 | K | Obligaciones Contractuales | misma unidad |
| G3.1-K05 | K | Implicaciones CISO | misma unidad |
| G3.1-K06 | K | Gestión de Privacidad | misma unidad |
| G3.1-K07 | K | Cumplimiento Integrado | misma unidad |
| G3.1-K08 | K | Riesgos Legales | misma unidad |
| G3.1-K09 | K | Auditorías de Cumplimiento | misma unidad |
| G3.1-K10 | K | Responsabilidad Legal | misma unidad |
| AMP-11 | AMP | Soberanía de datos | SE_RELACIONA |
| AMP-12 | AMP | Responsabilidad por agentes | SE_RELACIONA |
| HC-005 | HC | Cumplimiento continuo orientado a resultados | misma unidad |
| HC-008 | HC | Cadena de confianza en terceros | misma unidad |
| HC-011 | HC | Seguridad de datos en la IA empresarial | misma unidad |
| HC-024 | HC | Cumplimiento y privacidad por diseño | misma unidad |
| HC-029 | HC | Aseguramiento de terceros y cadena de suministro | misma unidad |
| HC-033 | HC | Seguridad y soberanía de datos distribuidos | misma unidad |

**Pregunta generadora:** ¿Cuál de sus agentes podría ser considerado un sistema que toma decisiones sobre personas, y qué obligación concreta eso le agrega mañana?

---

### 009. G3.2-PA01 — Aseguramiento continuo de la configuración del control (deriva)

**Unidad:** G3.2 Gestión del Cumplimiento y Aseguramiento Continuo · **Tipo:** PA · **Horas (sub-plan):** 4 · **Competencias:** C2.4, C1.4 · **Origen:** G3.2-PA02 (V5) · **Extensión:** 276 palabras · **Estado:** Idea central desarrollada (lote PA-01/02) — sub-plan PO-GAC; ID curricular, no ESS.

**Definición / idea central.** Verificación continua de que la configuración se mantiene en baseline; detección y corrección de deriva con KPI.

**Brecha frente a los 331.** K02 y AMP-13 enuncian aseguramiento y evidencia continua sin instrumentos.

**Tesis y sentido para el rol.** La configuración de un control se degrada aunque nadie la toque: cambian las recomendaciones del fabricante, se agregan excepciones, un administrador ajusta una política para resolver un ticket. El aseguramiento continuo de la configuración consiste en comparar de forma recurrente el estado real con el baseline declarado, explicar cada desviación y corregirla o registrarla como excepción. La tesis es que la deriva de configuración es el riesgo más silencioso de un control maduro y que su detección debe ser un control continuo con KPI propio, no una revisión anual.

**Tensión y límites.** La tensión está en la diferencia entre evidencia continua y ruido continuo: AMP-13 advierte que la evidencia generada por los propios controles vale según su alcance, integridad y responsable. Un informe de Configuration Analyzer que nadie lee no asegura nada. Otra tensión es el conflicto entre el baseline del fabricante y las decisiones locales legítimas: no toda desviación es un error, pero toda desviación necesita dueño.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: continuous controls monitoring y drift detection. Implementación: definir el control continuo de deriva para el control de correo con Configuration Analyzer y ORCA frente a Standard/Strict, Secure Score como tendencia, y una detección personalizada sobre cambios de política; asignar el agente AG-10 como centinela en L3 para detección y L2 para corrección; fijar el KPI-06 (desviaciones críticas abiertas = 0) y la evidencia mensual.

**Evidencia y evaluación.** Evidencia: diseño del control continuo con fuente, frecuencia, umbral, dueño, acción y evidencia; primer informe de deriva con remediación. Se evalúa que las desviaciones aceptadas estén registradas como excepciones (G2.2-PA03) y que el KPI sea verificable.

**Puentes.** Instancia G3.2-K02 (aseguramiento continuo); se apoya en AMP-13; se relaciona con HC-005 y HC-018. Tarea MDO-M01 del modelo operativo.

**Recomendaciones de práctica y ejercitación.**
1. Diseñar el control continuo de deriva: fuente (Configuration Analyzer/ORCA/Secure Score), frecuencia, umbral, dueño, acción y evidencia.
2. Escribir una detección personalizada (KQL) sobre cambios de política de correo y probarla con un cambio controlado en el entorno de prueba.
3. Producir el primer informe de deriva con remediación y excepciones registradas.

**Aplicación en el escenario de referencia.** Base agnóstica: Continuous controls monitoring; drift detection. Implementación Microsoft: Configuration Analyzer, ORCA, Secure Score, detecciones personalizadas sobre cambios de política. Actividad: Definir el control continuo de deriva, su KPI y su evidencia. Evidencia: Diseño de control continuo.

**Próximos pasos.**
- Asignar AG-10 como centinela (L3 detección / L2 corrección) y definir el KPI-06.
- Enlazar cada desviación aceptada con el registro de excepciones (G2.2-PA03).
- Mapear el control continuo a ISO 27001/42001 (HC-005) y a la evidencia continua (AMP-13).

**Relación con los conceptos de la(s) unidad(es) G3.2.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| G3.2-K01 | K | Procesos de Gestión | misma unidad |
| G3.2-K02 | K | Aseguramiento Continuo | INSTANCIA_DE |
| G3.2-K03 | K | Supervisión de Auditorías | misma unidad |
| G3.2-K04 | K | Reporte de Incumplimiento | misma unidad |
| G3.2-K05 | K | Estrategias Proactivas | misma unidad |
| G3.2-K06 | K | Gestión de Evidencia | misma unidad |
| G3.2-K07 | K | Automatización | misma unidad |
| G3.2-K08 | K | KPIs de Cumplimiento | misma unidad |
| G3.2-K09 | K | Formación en Cumplimiento | misma unidad |
| G3.2-K10 | K | Relación con Reguladores | misma unidad |
| AMP-13 | AMP | Evidencia continua | SE_APOYA_EN |
| AMP-14 | AMP | Aseguramiento de decisiones de IA | misma unidad |
| HC-003 | HC | Riesgo residual y aceptación verificable | misma unidad |
| HC-004 | HC | Política como código gobernado | misma unidad |
| HC-005 | HC | Cumplimiento continuo orientado a resultados | SE_RELACIONA |
| HC-012 | HC | Confianza verificable en decisiones de IA | misma unidad |
| HC-018 | HC | Observabilidad y aseguramiento de controles | SE_RELACIONA |
| HC-024 | HC | Cumplimiento y privacidad por diseño | misma unidad |
| HC-029 | HC | Aseguramiento de terceros y cadena de suministro | misma unidad |

**Pregunta generadora:** Si mañana alguien relajara una política anti-phishing para resolver un ticket, ¿cuánto tardaría su organización en enterarse y quién decidiría si es deriva o excepción?

---

### 010. G4.1-PA01 — Tres líneas de defensa para la flota de agentes

**Unidad:** G4.1 Gobernanza del Riesgo: Marcos y Estructuras · **Tipo:** PA · **Horas (sub-plan):** 4 · **Competencias:** C5.5, C8.1 · **Origen:** G4.1-PA01 (V5) · **Extensión:** 300 palabras · **Estado:** Idea central desarrollada (lote PA-01/02) — sub-plan PO-GAC; ID curricular, no ESS.

**Definición / idea central.** Owner (1ª), gobierno de IA/riesgo (2ª), auditoría (3ª); derechos de decisión y escalamiento.

**Brecha frente a los 331.** K03/K08 se enseñan para personas; HC-009 no asigna líneas.

**Tesis y sentido para el rol.** El modelo de tres líneas separa a quien gestiona el riesgo de quien lo supervisa y de quien lo asegura de forma independiente. Aplicado a una flota de agentes, la primera línea es el owner del control y de los agentes (PO-GAC), que diseña, opera y mide; la segunda es la función de gobierno de IA y riesgo (COE-IA en la referencia interna), que fija política, revisa clasificaciones de autonomía y mantiene el registro; la tercera es auditoría interna, que verifica la flota y el gobierno al menos una vez al año. La tesis es que sin esa separación el owner se convierte en juez de su propio agente, y HC-009 lo muestra para identidades no humanas: la accountability no puede recaer en quien también construye.

**Tensión y límites.** La tensión es de escala y de competencia: la segunda línea rara vez tiene capacidad técnica para revisar instrucciones de agentes, y la tercera no suele auditar sistemas de IA. El riesgo es una supervisión ceremonial. El ensayo debe proponer qué revisa cada línea con qué evidencia (la segunda, fichas, clasificaciones y KRIs; la tercera, muestras de trazas y expedientes ATO) y cómo se escala un desacuerdo.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: IIA Three Lines Model y AI RMF GOVERN. Implementación: asignar las tres líneas para la flota del control usando Agent 365 como instrumento de segunda línea (registro, reglas, políticas), el comité de ciberriesgo (referencia interna) para casos de alto riesgo y el plan anual de auditoría (AGC-22); construir el RACI de la flota.

**Evidencia y evaluación.** Evidencia: RACI por líneas con derechos de decisión y escalamiento. Se evalúa que cada actividad tenga una sola A, que la segunda línea no ejecute y que la tercera tenga acceso a evidencia sin depender del owner.

**Puentes.** Instancia G4.1-K03 (tres líneas) y K08 (roles); profundiza HC-009. Sostiene los AGC-02, AGC-13 y AGC-22.

**Recomendaciones de práctica y ejercitación.**
1. Asignar las tres líneas para la flota del control: qué revisa cada una, con qué evidencia y con qué frecuencia.
2. Construir el RACI de las 16 actividades de gobierno y gestión de agentes; verificar una sola A por actividad.
3. Simular un desacuerdo entre owner y segunda línea sobre el nivel de autonomía de AG-02 y documentar la ruta de escalamiento.

**Aplicación en el escenario de referencia.** Base agnóstica: IIA Three Lines Model; AI RMF GOVERN. Implementación Microsoft: COE-IA y comité de ciberriesgo (referencia interna); Agent 365 como instrumento de 2ª línea. Actividad: Asignar las tres líneas y el RACI para la flota. Evidencia: RACI por líneas.

**Próximos pasos.**
- Acordar con auditoría interna el acceso a trazas y expedientes sin depender del owner (AGC-22).
- Configurar en Agent 365 las reglas de segunda línea (agentes sin dueño, inactivos).
- Revisar el RACI al incorporar agentes de proveedores (M1.2-PA02).

**Relación con los conceptos de la(s) unidad(es) G4.1.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| G4.1-K01 | K | Enfoque Organizacional | misma unidad |
| G4.1-K02 | K | Integración ERM | misma unidad |
| G4.1-K03 | K | Tres Líneas de Defensa | INSTANCIA_DE |
| G4.1-K04 | K | Gestión Avanzada | misma unidad |
| G4.1-K05 | K | Marcos de Riesgo | misma unidad |
| G4.1-K06 | K | Evaluación Organizacional | misma unidad |
| G4.1-K07 | K | Enfoque en Negocio | misma unidad |
| G4.1-K08 | K | Roles y Responsabilidades | INSTANCIA_DE |
| G4.1-K09 | K | Supervisión | misma unidad |
| G4.1-K10 | K | Reporte a Dirección | misma unidad |
| AMP-15 | AMP | Riesgo sistémico | misma unidad |
| AMP-16 | AMP | Homeostasis y fuerzas de cambio | misma unidad |
| HC-009 | HC | Gobierno de identidades no humanas | PROFUNDIZA |
| HC-014 | HC | Arquitectura de riesgo empresarial | misma unidad |
| HC-022 | HC | Gobierno de crisis multidisciplinario | misma unidad |
| G4.1-PA02 | PA | Taxonomía y registro de riesgos de agentes | misma unidad |

**Pregunta generadora:** ¿Quién, fuera del owner, podría hoy decir con evidencia que un agente del SOC actúa dentro de sus límites, y con qué frecuencia lo hace?

---

### 011. G4.1-PA02 — Taxonomía y registro de riesgos de agentes

**Unidad:** G4.1 Gobernanza del Riesgo: Marcos y Estructuras · **Tipo:** PA · **Horas (sub-plan):** 4 · **Competencias:** C8.1, C4.6 · **Origen:** G4.1-PA02 (V5) · **Extensión:** 299 palabras · **Estado:** Idea central desarrollada (lote PA-01/02) — sub-plan PO-GAC; ID curricular, no ESS.

**Definición / idea central.** Taxonomía operativa (agencia excesiva, inyección, fuga, drift, costo, dependencia, cascada) y registro con dueño y tratamiento.

**Brecha frente a los 331.** AMP-20/15 cubren modelos y riesgo sistémico; falta la taxonomía operativa de agentes.

**Tesis y sentido para el rol.** Los agentes introducen riesgos que no están en los registros tradicionales: agencia excesiva (hacen más de lo pedido), inyección de instrucciones a través del contenido que procesan, fuga de datos por herramientas o conocimiento mal acotado, deriva de comportamiento, costo descontrolado, dependencia de un modelo o proveedor y fallos en cascada entre agentes. AMP-20 trata el riesgo de los modelos y AMP-15 el riesgo sistémico; este concepto propone una taxonomía operativa de riesgos de agentes y su registro con dueño, KRI y tratamiento, para que el riesgo de la flota se gobierne con el mismo rigor que el del control.

**Tensión y límites.** La tensión está en la novedad: las taxonomías públicas (OWASP Agentic Top 10) cambian de versión y usan vocabulario técnico que el registro de riesgos corporativo no reconoce. Traducir sin perder precisión es el trabajo del owner. Otra tensión es el doble conteo: el riesgo del agente que remedia correo se solapa con el riesgo del control de correo. El ensayo debe mostrar cómo registrar el riesgo introducido por el agente sin duplicar el riesgo que el agente mitiga.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: OWASP Agentic Top 10 (ASI01–ASI10, v2.01), AI RMF MAP, ISO 31000. Implementación: poblar el registro con diez riesgos de la flota, cada uno con escenario, agente afectado, control AGC que lo trata, KRI (G4.2-PA01) y dueño; conectar las señales con Defender (amenazas a IA), Purview (fuga) y Agent 365 (agentes sin dueño, inactivos).

**Evidencia y evaluación.** Evidencia: registro de riesgos de la flota con diez entradas tratadas. Se evalúa la traducción correcta de la taxonomía al lenguaje del ERM, la ausencia de doble conteo y la vinculación de cada riesgo a un control y un indicador.

**Puentes.** Extiende AMP-20 (riesgo de modelos); se relaciona con AMP-15 (riesgo sistémico) y HC-016 (superficie de ataque); instancia G4.1-K05 (marcos de riesgo). Alimenta G4.2-PA01 y M4.2-PA02.

**Recomendaciones de práctica y ejercitación.**
1. Traducir los diez ASI del OWASP Agentic Top 10 al lenguaje del registro de riesgos corporativo (escenario, causa, consecuencia) para la flota.
2. Poblar el registro con diez riesgos: agente afectado, control AGC, KRI, dueño y tratamiento; evitar el doble conteo con el riesgo del control.
3. Conectar tres de esos riesgos a señales reales (Defender para IA, Purview, Agent 365).

**Aplicación en el escenario de referencia.** Base agnóstica: OWASP Agentic Top 10; AI RMF MAP; ISO 31000. Implementación Microsoft: Registro en GRC; señales desde Defender, Purview y Agent 365. Actividad: Poblar el registro con 10 riesgos de la flota. Evidencia: Registro de riesgos.

**Próximos pasos.**
- Definir los KRIs de la flota (G4.2-PA01) a partir de los riesgos registrados.
- Cruzar el registro con la matriz amenaza→agente→control (M4.2-PA02).
- Revisar la taxonomía cuando OWASP publique una nueva versión.

**Relación con los conceptos de la(s) unidad(es) G4.1.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| G4.1-K01 | K | Enfoque Organizacional | misma unidad |
| G4.1-K02 | K | Integración ERM | misma unidad |
| G4.1-K03 | K | Tres Líneas de Defensa | misma unidad |
| G4.1-K04 | K | Gestión Avanzada | misma unidad |
| G4.1-K05 | K | Marcos de Riesgo | INSTANCIA_DE |
| G4.1-K06 | K | Evaluación Organizacional | misma unidad |
| G4.1-K07 | K | Enfoque en Negocio | misma unidad |
| G4.1-K08 | K | Roles y Responsabilidades | misma unidad |
| G4.1-K09 | K | Supervisión | misma unidad |
| G4.1-K10 | K | Reporte a Dirección | misma unidad |
| AMP-15 | AMP | Riesgo sistémico | SE_RELACIONA |
| AMP-16 | AMP | Homeostasis y fuerzas de cambio | misma unidad |
| HC-009 | HC | Gobierno de identidades no humanas | misma unidad |
| HC-014 | HC | Arquitectura de riesgo empresarial | misma unidad |
| HC-022 | HC | Gobierno de crisis multidisciplinario | misma unidad |
| G4.1-PA01 | PA | Tres líneas de defensa para la flota de agentes | misma unidad |
| AMP-20 | AMP | Riesgo de modelos de IA | EXTIENDE (otra unidad) |
| HC-016 | HC | Superficie de ataque contextualizada | SE_RELACIONA (otra unidad) |

**Pregunta generadora:** ¿Qué riesgo introduce el agente que usted propone para reducir un riesgo, y en qué registro quedaría escrito?

---

### 012. G4.2-PA01 — KRIs de la flota de agentes y umbrales de intervención

**Unidad:** G4.2 Definición y Comunicación del Apetito de Riesgo · **Tipo:** PA · **Horas (sub-plan):** 4 · **Competencias:** C8.1, C6.2 · **Origen:** G4.2-PA02 (V5) · **Extensión:** 281 palabras · **Estado:** Idea central desarrollada (lote PA-01/02) — sub-plan PO-GAC; ID curricular, no ESS.

**Definición / idea central.** Indicadores de riesgo de la flota con umbrales que disparan revisión o pausa.

**Brecha frente a los 331.** K09 es general; AMP-17/18 fijan límites sin indicadores.

**Tesis y sentido para el rol.** Un KRI de la flota de agentes es un indicador que anticipa la transgresión de un límite de autonomía o de un umbral de riesgo antes de que se convierta en incidente: tasa de acciones revertidas, tasa de escalamiento fuera de rango, precisión de clasificación en caída, consumo por tarea en ascenso, invocaciones de herramientas fuera de la allowlist, inicios de sesión de identidades de agentes desde contextos no previstos. La tesis es que los límites de autonomía de AMP-18 solo son operables si tienen indicadores con umbrales que disparen una acción predefinida: revisar, reducir autonomía, pausar.

**Tensión y límites.** La tensión es la que HC-027 llama métricas que no engañan: un agente puede mostrar precisión alta porque solo trata casos fáciles, o consumo estable porque dejó de trabajar. Los KRIs deben leerse en conjunto y con calidad de datos conocida. Otra tensión es el umbral: demasiado sensible y el agente vive pausado; demasiado laxo y la intervención llega tarde. El ensayo debe argumentar los umbrales con historia y con el apetito declarado (AMP-17).

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: KRIs y control estadístico de procesos. Implementación: definir ocho KRIs de la flota con definición, fuente (Agent 365 analytics, Sentinel, Cost Management, sign-in logs de Entra), umbral, acción automática o humana y dueño; conectar con los KPI-11 a KPI-15 y KPI-19 del sub-plan.

**Evidencia y evaluación.** Evidencia: ficha de ocho KRIs con umbrales y acciones. Se evalúa que cada KRI tenga fuente real, que los umbrales deriven del apetito y que exista al menos un KRI de costo, uno de calidad, uno de identidad y uno de comportamiento.

**Puentes.** Instancia G4.2-K09 (métricas de apetito); operacionaliza AMP-18 (límites de autonomía); se apoya en HC-027. Sostiene el AGC-14 y la revisión de desempeño (M4.1-PA06).

**Recomendaciones de práctica y ejercitación.**
1. Definir ocho KRIs de la flota (al menos uno de costo, calidad, identidad y comportamiento) con fuente, umbral, acción y dueño.
2. Derivar cada umbral del apetito de autonomía declarado (AMP-17) y de datos históricos del entorno de prueba.
3. Construir una consulta en Sentinel o Agent 365 que materialice dos de los KRIs.

**Aplicación en el escenario de referencia.** Base agnóstica: KRIs; control estadístico de procesos. Implementación Microsoft: Agent 365 analytics, Sentinel, Cost Management. Actividad: Definir 8 KRIs con umbrales y acción. Evidencia: Ficha de KRIs.

**Próximos pasos.**
- Integrar los KRIs al tablero de la flota (M4.1-PA05) y al monitoreo AGC-14.
- Revisar umbrales tras la primera revisión de desempeño (M4.1-PA06).
- Contrastar los KRIs con los 20 KPIs del sub-plan usando HC-027.

**Relación con los conceptos de la(s) unidad(es) G4.2.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| G4.2-K01 | K | Apetito de Riesgo | misma unidad |
| G4.2-K02 | K | Tolerancia al Riesgo | misma unidad |
| G4.2-K03 | K | Documentación | misma unidad |
| G4.2-K04 | K | Comunicación | misma unidad |
| G4.2-K05 | K | Rol Ejecutivo | misma unidad |
| G4.2-K06 | K | Impacto en Estrategia | misma unidad |
| G4.2-K07 | K | Talleres de Definición | misma unidad |
| G4.2-K08 | K | Relación Apetito-Residual | misma unidad |
| G4.2-K09 | K | Métricas de Apetito | INSTANCIA_DE |
| G4.2-K10 | K | Aceptación Formal | misma unidad |
| AMP-17 | AMP | Autoridad delegada | misma unidad |
| AMP-18 | AMP | Límites de autonomía | OPERACIONALIZA |
| HC-002 | HC | Apetito de riesgo convertido en arquitectura | misma unidad |
| HC-003 | HC | Riesgo residual y aceptación verificable | misma unidad |
| HC-007 | HC | Resiliencia gobernada por impacto | misma unidad |
| HC-010 | HC | Autonomía delegada y límites de acción | misma unidad |
| HC-027 | HC | Métricas que no engañan | SE_APOYA_EN |
| HC-040 | HC | Homeostasis organizacional de seguridad | misma unidad |

**Pregunta generadora:** ¿Qué indicador le avisaría una semana antes de que un agente empiece a hacer daño, y qué ocurriría automáticamente cuando lo cruce?

---

### 013. G6.1-PA01 — Reporte ejecutivo del producto-control y de la fuerza de trabajo híbrida

**Unidad:** G6.1 Comunicación Estratégica · **Tipo:** PA · **Horas (sub-plan):** 3 · **Competencias:** C8.3 · **Origen:** G6.1-PA01 (V5) · **Extensión:** 266 palabras · **Estado:** Idea central desarrollada (lote PA-01/02) — sub-plan PO-GAC; ID curricular, no ESS.

**Definición / idea central.** Valor, costo, riesgo, incidentes, desempeño de humanos, agentes y proveedores, decisiones requeridas.

**Brecha frente a los 331.** Ningún concepto reporta agentes como fuerza de trabajo.

**Tesis y sentido para el rol.** El reporte ejecutivo de un producto-control debe responder lo que un director necesita decidir: qué valor entregó el control, qué costó, qué riesgo quedó, qué incidentes hubo y qué decisiones se requieren. Cuando el control se opera con una fuerza de trabajo híbrida, el reporte agrega una sección que antes no existía: el desempeño, costo y riesgo de los agentes y de los proveedores, con el mismo nivel de hechos que el de las personas. La tesis es que reportar la flota como fuerza de trabajo —y no como herramienta— es lo que permite a la dirección ejercer supervisión real sobre la autonomía delegada.

**Tensión y límites.** La tensión es la narrativa: AMP-23 pide hechos verificables, incertidumbre y decisiones pendientes, y AMP-24 comunicar incertidumbre con rangos; el reporte de agentes tiende al entusiasmo (horas "ahorradas") o al alarmismo (incidentes de IA). HC-027 recuerda que actividad, uso y efectividad son distintos. El ensayo debe mostrar cómo reportar un trimestre en el que los agentes hicieron más tareas pero cometieron un error relevante.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: reporting ejecutivo basado en hechos. Implementación: preparar el reporte trimestral del control con la plantilla del sub-plan (valor, costo, riesgo, incidentes, flota, decisiones) alimentado por Power BI y Sentinel, con los KPIs del control y de la flota y con el estado de los expedientes ATO.

**Evidencia y evaluación.** Evidencia: reporte trimestral de dos páginas y su anexo de datos. Se evalúa la separación de hechos e inferencias (G6.1-K05), la presencia de decisiones requeridas y la honestidad sobre incertidumbre.

**Puentes.** Instancia G6.1-K05 (reportes factuales) y K06 (métricas clave); se apoya en AMP-23 y HC-027. Es el entregable del capstone (E5).

**Recomendaciones de práctica y ejercitación.**
1. Preparar el reporte trimestral de dos páginas con la plantilla (valor, costo, riesgo, incidentes, flota, decisiones) a partir de datos del entorno de prueba.
2. Redactar el caso difícil: un trimestre con más tareas ejecutadas por agentes y un error relevante; separar hechos, inferencias y rangos.
3. Presentarlo a un par que haga de CISO y registrar qué decisión tomaría y con qué dato.

**Aplicación en el escenario de referencia.** Base agnóstica: Reporting ejecutivo basado en hechos. Implementación Microsoft: Plantilla del sub-plan; Power BI. Actividad: Preparar el reporte trimestral del control. Evidencia: Reporte.

**Próximos pasos.**
- Automatizar el anexo de datos desde Power BI/Sentinel.
- Usar el reporte como entregable del capstone (E5).
- Incorporar el protocolo de comunicación de incidentes de agentes (HC-020).

**Relación con los conceptos de la(s) unidad(es) G6.1.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| G6.1-K01 | K | Estrategia Comunicación | misma unidad |
| G6.1-K02 | K | Comunicación Junta | misma unidad |
| G6.1-K03 | K | Comunicación Ejecutiva | misma unidad |
| G6.1-K04 | K | Lenguaje de Negocio | misma unidad |
| G6.1-K05 | K | Reportes Factuales | INSTANCIA_DE |
| G6.1-K06 | K | Métricas Clave | INSTANCIA_DE |
| G6.1-K07 | K | Gestión Expectativas | misma unidad |
| G6.1-K08 | K | Comunicación Crisis | misma unidad |
| G6.1-K09 | K | Responsabilidad Legal | misma unidad |
| G6.1-K10 | K | Cultura Abierta | misma unidad |
| AMP-23 | AMP | Narrativa de riesgo basada en evidencia | SE_APOYA_EN |
| AMP-24 | AMP | Comunicación de incertidumbre | misma unidad |
| HC-001 | HC | Gobierno de decisiones basadas en evidencia | misma unidad |
| HC-017 | HC | Inteligencia que modifica decisiones | misma unidad |
| HC-018 | HC | Observabilidad y aseguramiento de controles | misma unidad |
| HC-020 | HC | Respuesta y comunicación bajo incertidumbre | misma unidad |
| HC-022 | HC | Gobierno de crisis multidisciplinario | misma unidad |
| HC-026 | HC | Ética, cultura y controles internos | misma unidad |
| HC-027 | HC | Métricas que no engañan | SE_APOYA_EN |
| HC-039 | HC | Riesgo cibernético como narrativa empresarial | misma unidad |

**Pregunta generadora:** ¿Qué decisión debería tomar el CISO después de leer su reporte, y qué dato del reporte la sostiene?

---

### 014. G6.2-PA01 — Métricas de efectividad del gobierno de la flota

**Unidad:** G6.2 Liderazgo Ético y Medición de Efectividad · **Tipo:** PA · **Horas (sub-plan):** 3 · **Competencias:** C6.2, C5.1 · **Origen:** G6.2-PA03 (V5) · **Extensión:** 260 palabras · **Estado:** Idea central desarrollada (lote PA-01/02) — sub-plan PO-GAC; ID curricular, no ESS.

**Definición / idea central.** Cobertura del registro, agentes con dueño, revisiones a tiempo, incidentes evitados, hallazgos de auditoría.

**Brecha frente a los 331.** K05/K06 miden gobierno sin agentes; AMP-26 sin métricas.

**Tesis y sentido para el rol.** El gobierno de una flota de agentes se mide con indicadores propios, distintos de los del control y de los de cada agente: cobertura del registro (qué proporción de agentes observados están registrados con dueño), agentes sin dueño o inactivos, revisiones de desempeño y recertificaciones a tiempo, cambios desplegados con evaluación previa, incidentes evitados por controles de autonomía y hallazgos de auditoría abiertos. La tesis es que estas métricas de efectividad del gobierno son la forma de demostrar que la supervisión humana de AMP-26 es real y no ceremonial, y de dar a la segunda línea una base para intervenir.

**Tensión y límites.** La tensión es la de toda métrica de gobierno: mide proceso, no resultado, y puede cumplirse sin que el riesgo baje. HC-027 obliga a acompañarlas con indicadores de efectividad. Otra tensión es el perímetro: contar agentes supone saber cuántos hay, y Shadow AI (M6.2-K06) hace que el denominador sea incierto. El ensayo debe discutir cómo estimar el denominador y cómo evitar que la métrica premie no registrar.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: governance metrics y AI RMF MEASURE. Implementación: definir seis métricas de gobierno de la flota con fuente (Agent 365 para agentes sin dueño e inactivos, Compliance Manager para evidencias, registro de cambios para evaluaciones previas) y conectarlas con el KPI-10, KPI-16 y KPI-17.

**Evidencia y evaluación.** Evidencia: ficha de seis métricas con metas y un primer corte. Se evalúa que al menos una métrica sea de resultado (incidentes evitados o detectados) y que el denominador esté declarado.

**Puentes.** Instancia G6.2-K05 (métricas de gobierno) y K06 (efectividad); se relaciona con AMP-26 y HC-027. Es el AGC-24.

**Recomendaciones de práctica y ejercitación.**
1. Definir seis métricas de gobierno de la flota con fuente, meta y denominador declarado; al menos una de resultado.
2. Estimar el denominador real de agentes en el tenant (Power Platform admin center, Agent 365, inventario de app registrations) y compararlo con el registro.
3. Producir el primer corte y comentar qué métrica podría 'premiar no registrar'.

**Aplicación en el escenario de referencia.** Base agnóstica: Governance metrics; AI RMF MEASURE. Implementación Microsoft: Agent 365 (ownerless/inactive), Compliance Manager. Actividad: Definir 6 métricas de gobierno de la flota. Evidencia: Ficha de métricas.

**Próximos pasos.**
- Publicar las métricas en el tablero de gobierno (AGC-24) y en el reporte trimestral (G6.1-PA01).
- Definir la regla de detección de agentes no registrados (M6.2-K06).
- Revisar las métricas con la segunda línea tras el primer trimestre.

**Relación con los conceptos de la(s) unidad(es) G6.2.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| G6.2-K01 | K | Liderazgo Ético | misma unidad |
| G6.2-K02 | K | Conducta Profesional | misma unidad |
| G6.2-K03 | K | Conflictos Interés | misma unidad |
| G6.2-K04 | K | Debida Diligencia | misma unidad |
| G6.2-K05 | K | Métricas Gobierno | INSTANCIA_DE |
| G6.2-K06 | K | Efectividad Programa | INSTANCIA_DE |
| G6.2-K07 | K | Mejora Continua | misma unidad |
| G6.2-K08 | K | Aseguramiento | misma unidad |
| G6.2-K09 | K | Balance Riesgo-Valor | misma unidad |
| G6.2-K10 | K | Rendición Cuentas | misma unidad |
| AMP-25 | AMP | Ética de autonomía | misma unidad |
| AMP-26 | AMP | Supervisión humana efectiva | SE_RELACIONA |
| HC-006 | HC | Valor de seguridad y medición causal | misma unidad |
| HC-012 | HC | Confianza verificable en decisiones de IA | misma unidad |
| HC-021 | HC | Recuperación como prueba de confianza | misma unidad |
| HC-026 | HC | Ética, cultura y controles internos | misma unidad |
| HC-027 | HC | Métricas que no engañan | SE_APOYA_EN |
| AMP-52 | AMP | Content safety y riesgos de contenido generado | misma unidad |

**Pregunta generadora:** Si el 100 % de sus agentes registrados tiene dueño, ¿qué porcentaje de los agentes que realmente operan en su tenant está registrado?

---

### 015. M1.1-PA01 — Diseño organizativo híbrido: roles, RACI y span of control

**Unidad:** M1.1 Desarrollo, Gestión y Operaciones del Programa de Seguridad · **Tipo:** PA · **Horas (sub-plan):** 6 · **Competencias:** C6.1, C7.3 · **Origen:** G1.1-PA01 + M1.1-PA01 (V5) · **Extensión:** 336 palabras · **Estado:** Idea central desarrollada (lote PA-01/02) — sub-plan PO-GAC; ID curricular, no ESS.

**Definición / idea central.** Roles, funciones y supervisión entre humanos, agentes y proveedores; organigrama híbrido; RACI; span of control.

**Brecha frente a los 331.** K03 describe la oficina humana; AMP-27/29 no diseñan la estructura.

**Tesis y sentido para el rol.** Diseñar la organización de un programa de seguridad híbrido es decidir qué hace cada tipo de trabajador —persona, agente, proveedor—, quién supervisa a quién y cuánto puede supervisar razonablemente un owner. La oficina del CISO que describe M1.1-K03 se compone de personas; AMP-27 la imagina como un sistema operativo que integra datos, decisiones, agentes y evidencia, y AMP-29 anticipa el rediseño de roles. Falta el plano: el organigrama híbrido con sus relaciones de reporte, el RACI que asigna decisiones y el span of control medido en agentes y contratos además de personas. La tesis es que ese plano es un entregable de gestión, no una metáfora, y que su ausencia es la causa más frecuente de agentes sin dueño.

**Tensión y límites.** La tensión es que los agentes no son personas y el organigrama puede sugerir una equivalencia falsa: un agente no tiene carrera, no negocia y puede replicarse sin costo. Pero sí tiene ficha, identidad, presupuesto, revisión de desempeño y retiro, y Agent 365 lo coloca en el directorio con una relación con su dueño. El ensayo debe discutir cuántos agentes puede supervisar con sentido un owner (el límite lo ponen la revisión de muestras y las aprobaciones L2, no la tecnología) y qué pasa con los agentes del proveedor MDR dentro del mismo plano.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: diseño organizacional y teoría de agencia. Implementación: diseñar la estructura del equipo del control para seis personas, quince agentes y un MDR, con organigrama híbrido, RACI de las dieciséis actividades de gobierno y gestión de agentes y cálculo del span of control por owner; registrar sponsors en Entra Agent ID y la relación en Agent 365.

**Evidencia y evaluación.** Evidencia: organigrama híbrido comentado y RACI. Se evalúa que cada agente tenga un dueño con capacidad real de supervisión, que las decisiones de autonomía y aceptación de riesgo no recaigan en quien construye y que el MDR tenga una interfaz definida.

**Puentes.** Extiende M1.1-K03 (oficina del CISO); se apoya en AMP-27 y AMP-29; se relaciona con AMP-28 (orquestación). Prepara M1.2-PA03 y sostiene los AGC-02 y AGC-23.

**Recomendaciones de práctica y ejercitación.**
1. Dibujar el organigrama híbrido del control (6 personas, 15 agentes, 1 MDR) con relaciones de reporte y sponsors.
2. Calcular el span of control de cada owner a partir del tiempo de revisión de muestras y aprobaciones L2 por agente; marcar el límite.
3. Completar el RACI de las 16 actividades de gobierno y gestión de agentes e incluir la interfaz con el MDR.

**Aplicación en el escenario de referencia.** Base agnóstica: Diseño organizacional; teoría de agencia. Implementación Microsoft: Agent 365 (agentes con cuenta y perfil), Entra (sponsors). Actividad: Diseñar la estructura para 6 personas, 15 agentes y un MDR, con RACI. Evidencia: Organigrama híbrido + RACI.

**Próximos pasos.**
- Registrar sponsors en Entra Agent ID y la relación owner–agente en Agent 365.
- Usar el organigrama en M1.2-PA03 (itinerario) y como evidencia de AGC-02/AGC-23.
- Revisar el span of control si se duplica la flota o cambia la ruta de construcción.

**Relación con los conceptos de la(s) unidad(es) M1.1.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M1.1-K01 | K | Programa de Seguridad | misma unidad |
| M1.1-K02 | K | Alcance y Objetivos | misma unidad |
| M1.1-K03 | K | Oficina del CISO | EXTIENDE |
| M1.1-K04 | K | Alineación Operativa | misma unidad |
| M1.1-K05 | K | Ciclo de Vida | misma unidad |
| M1.1-K06 | K | Recursos | misma unidad |
| M1.1-K07 | K | Medición Rendimiento | misma unidad |
| M1.1-K08 | K | Interesados (Stakeholders) | misma unidad |
| M1.1-K09 | K | Integración Gobierno | misma unidad |
| M1.1-K10 | K | Mejora Continua | misma unidad |
| AMP-27 | AMP | CISO-OS | SE_APOYA_EN |
| AMP-28 | AMP | Orquestación de agentes | SE_RELACIONA |
| HC-006 | HC | Valor de seguridad y medición causal | misma unidad |
| HC-027 | HC | Métricas que no engañan | misma unidad |
| HC-035 | HC | Aprendizaje desde incidentes hasta políticas | misma unidad |
| HC-036 | HC | Portafolio de controles y capacidades | misma unidad |
| M1.1-PA02 | PA | Portafolio de productos-control con owners | misma unidad |
| M1.1-PA03 | PA | Modelo operativo por cadencias y excelencia operacional como requisito del programa | misma unidad |
| AMP-29 | AMP | Competencias humanas y agentes | SE_APOYA_EN (otra unidad) |

**Pregunta generadora:** ¿Cuántos agentes puede supervisar hoy, con revisión real de sus decisiones, cada persona de su equipo, y qué cambia en ese número si duplica la flota?

---

### 016. M1.1-PA02 — Portafolio de productos-control con owners

**Unidad:** M1.1 Desarrollo, Gestión y Operaciones del Programa de Seguridad · **Tipo:** PA · **Horas (sub-plan):** 4 · **Competencias:** C1.1, C1.3 · **Origen:** M1.1-PA02 (V5) · **Extensión:** 280 palabras · **Estado:** Idea central desarrollada (lote PA-01/02) — sub-plan PO-GAC; ID curricular, no ESS.

**Definición / idea central.** Conjunto de controles como productos con owner, métricas, backlog y presupuesto.

**Brecha frente a los 331.** HC-036 integra el portafolio sin owner por producto.

**Tesis y sentido para el rol.** Un programa de seguridad maduro gestiona sus controles como un portafolio de productos: cada producto-control tiene owner, propósito, métricas, backlog, presupuesto y ciclo de vida, y el portafolio se revisa como un todo para decidir dónde invertir, qué consolidar y qué retirar. HC-036 integra inversión, selección, adopción y pruebas de un portafolio de controles; este concepto agrega el ownership por producto como principio organizador y la grilla CSF × Zero Trust (G2.1-PA01) como mapa del portafolio. La tesis es que el portafolio con owners es la unidad natural de gestión en una oficina del CISO híbrida, porque permite asignar agentes y presupuesto por producto y comparar productos entre sí.

**Tensión y límites.** La tensión es la fragmentación: un portafolio de treinta productos-control con treinta owners parciales reproduce los silos que se quería evitar. La respuesta es agrupar por dominio Zero Trust y aceptar que un owner tenga varios productos pequeños. Otra tensión es la medición comparada: comparar el "valor" del control de correo con el de identidades induce a métricas ficticias; el portafolio debe comparar cobertura, deuda y riesgo residual, no un número único.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: portfolio management. Implementación: definir el portafolio de cinco productos-control de una organización tipo (correo y colaboración, identidades, endpoints, datos, SecOps) con owner, tecnología, modelo operativo, métricas, backlog y presupuesto de agentes; usar el catálogo de productos-control por pilar como vista ejecutiva.

**Evidencia y evaluación.** Evidencia: portafolio de cinco productos-control con fichas resumidas y una revisión de portafolio simulada. Se evalúa la coherencia con la grilla de ownership, la comparabilidad honesta y la asignación de agentes por producto.

**Puentes.** Profundiza HC-036; se relaciona con M1.1-K02 (alcance y objetivos) y K05 (ciclo de vida). Depende de G2.1-PA01 y alimenta M1.2-PA01 (presupuesto por producto).

**Recomendaciones de práctica y ejercitación.**
1. Definir cinco productos-control con owner, tecnología, modelo operativo, métricas, backlog y presupuesto de agentes.
2. Simular una revisión de portafolio: comparar cobertura, deuda y riesgo residual (no un número único) y decidir dónde reasignar agentes.
3. Agrupar los productos por pilar Zero Trust y justificar los owners con varios productos.

**Aplicación en el escenario de referencia.** Base agnóstica: Portfolio management. Implementación Microsoft: Catálogo de productos-control por pilar Zero Trust. Actividad: Definir el portafolio de 5 productos-control. Evidencia: Portafolio.

**Próximos pasos.**
- Alinear el portafolio con la grilla de ownership (G2.1-PA01).
- Derivar el presupuesto por producto (M1.2-PA01).
- Revisar el portafolio trimestralmente junto con el reporte ejecutivo (G6.1-PA01).

**Relación con los conceptos de la(s) unidad(es) M1.1.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M1.1-K01 | K | Programa de Seguridad | misma unidad |
| M1.1-K02 | K | Alcance y Objetivos | SE_RELACIONA |
| M1.1-K03 | K | Oficina del CISO | misma unidad |
| M1.1-K04 | K | Alineación Operativa | misma unidad |
| M1.1-K05 | K | Ciclo de Vida | SE_RELACIONA |
| M1.1-K06 | K | Recursos | misma unidad |
| M1.1-K07 | K | Medición Rendimiento | misma unidad |
| M1.1-K08 | K | Interesados (Stakeholders) | misma unidad |
| M1.1-K09 | K | Integración Gobierno | misma unidad |
| M1.1-K10 | K | Mejora Continua | misma unidad |
| AMP-27 | AMP | CISO-OS | misma unidad |
| AMP-28 | AMP | Orquestación de agentes | misma unidad |
| HC-006 | HC | Valor de seguridad y medición causal | misma unidad |
| HC-027 | HC | Métricas que no engañan | misma unidad |
| HC-035 | HC | Aprendizaje desde incidentes hasta políticas | misma unidad |
| HC-036 | HC | Portafolio de controles y capacidades | PROFUNDIZA |
| M1.1-PA01 | PA | Diseño organizativo híbrido: roles, RACI y span of control | misma unidad |
| M1.1-PA03 | PA | Modelo operativo por cadencias y excelencia operacional como requisito del programa | misma unidad |

**Pregunta generadora:** Si tuviera que retirar un producto-control de su portafolio para financiar agentes en otro, ¿con qué criterio lo elegiría y quién debería aprobarlo?

---

### 017. M1.1-PA03 — Modelo operativo por cadencias y excelencia operacional como requisito del programa

**Unidad:** M1.1 Desarrollo, Gestión y Operaciones del Programa de Seguridad · **Tipo:** PA · **Horas (sub-plan):** 5 · **Competencias:** C3.1 · **Origen:** M1.1-PA03 (V5) · **Extensión:** 315 palabras · **Estado:** Idea central desarrollada (lote PA-01/02) — sub-plan PO-GAC; ID curricular, no ESS.

**Definición / idea central.** Cadencias, runbooks, SLAs, evidencia y rituales por control; prácticas agnósticas (eo:OP).

**Brecha frente a los 331.** K05 advierte el abandono del mantenimiento; nadie formaliza el modelo operativo por control.

**Tesis y sentido para el rol.** M1.1-K05 describe el patrón más dañino de la gestión de controles: se celebra el despliegue y se abandona el mantenimiento. El antídoto es el modelo operativo por cadencias: la lista de tareas diarias, semanales, mensuales, trimestrales y por evento que mantienen el control efectivo, con responsable, evidencia y SLA. Los fabricantes publican guías de operación por tecnología (Microsoft, la Security Operations Guide de Defender for Office 365); el programa debe exigir que cada producto-control tenga su modelo operativo y que se mida la excelencia operacional sobre él. La tesis es que el modelo operativo es el contrato entre el owner y el programa, y que las prácticas agnósticas (eo:OP en la convención MAEO) permiten reutilizarlo cuando cambia la tecnología.

**Tensión y límites.** La tensión está en la relación entre lo específico y lo portable: la guía de Microsoft dice "revisar Threat analytics semanalmente"; la práctica agnóstica dice "revisar inteligencia de amenazas y derivar acciones". Si el programa solo documenta lo específico, cambiar de plataforma destruye el modelo; si solo documenta lo agnóstico, nadie sabe qué botón tocar. El ensayo debe argumentar por qué se necesitan los dos niveles y cómo se relacionan (la tarea de producto ejemplifica la práctica).

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: MAEO, ITIL, O-ISM3. Implementación: tomar las tareas de la Security Operations Guide y las de mantenimiento del SOC de Defender XDR y derivar diez prácticas agnósticas con verbo, objeto, cadencia, rol y evidencia; definir cómo el programa mide la excelencia operacional por control (cumplimiento de cadencias, evidencia completa, SLA).

**Evidencia y evaluación.** Evidencia: diez fichas eo:OP y la política de modelo operativo del programa. Se evalúa que cada práctica sea independiente del producto, que cada tarea de producto quede mapeada y que la medición de excelencia no premie la actividad sin resultado.

**Puentes.** Profundiza M1.1-K05 (ciclo de vida); se relaciona con M1.1-K07 (medición de rendimiento) y se apoya en AMP-27 (CISO-OS). Es la base conceptual de M4.1-PA01 y del documento 04.

**Recomendaciones de práctica y ejercitación.**
1. Derivar diez prácticas eo:OP (verbo + objeto + cadencia + rol + evidencia) de las 31 tareas del modelo operativo MDO/XDR.
2. Redactar la política de modelo operativo del programa: qué debe tener todo producto-control y cómo se mide la excelencia operacional.
3. Auditar seis meses hacia atrás: qué tareas de mantenimiento del control no se hicieron y qué métrica debería haberlo mostrado.

**Aplicación en el escenario de referencia.** Base agnóstica: MAEO; ITIL; O-ISM3. Implementación Microsoft: Security Operations Guide de Defender for Office 365; tareas del SOC de Defender XDR. Actividad: Derivar 10 prácticas agnósticas (eo:OP) de las tareas de MDO. Evidencia: Fichas eo:OP.

**Próximos pasos.**
- Proponer las eo:OP nuevas al MAEO mediante ChangeSet.
- Aplicar la política de modelo operativo al portafolio (M1.1-PA02).
- Vincular con M4.1-PA01 (modelo operativo concreto).

**Relación con los conceptos de la(s) unidad(es) M1.1.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M1.1-K01 | K | Programa de Seguridad | misma unidad |
| M1.1-K02 | K | Alcance y Objetivos | misma unidad |
| M1.1-K03 | K | Oficina del CISO | misma unidad |
| M1.1-K04 | K | Alineación Operativa | misma unidad |
| M1.1-K05 | K | Ciclo de Vida | PROFUNDIZA |
| M1.1-K06 | K | Recursos | misma unidad |
| M1.1-K07 | K | Medición Rendimiento | SE_RELACIONA |
| M1.1-K08 | K | Interesados (Stakeholders) | misma unidad |
| M1.1-K09 | K | Integración Gobierno | misma unidad |
| M1.1-K10 | K | Mejora Continua | misma unidad |
| AMP-27 | AMP | CISO-OS | SE_APOYA_EN |
| AMP-28 | AMP | Orquestación de agentes | misma unidad |
| HC-006 | HC | Valor de seguridad y medición causal | misma unidad |
| HC-027 | HC | Métricas que no engañan | misma unidad |
| HC-035 | HC | Aprendizaje desde incidentes hasta políticas | misma unidad |
| HC-036 | HC | Portafolio de controles y capacidades | misma unidad |
| M1.1-PA01 | PA | Diseño organizativo híbrido: roles, RACI y span of control | misma unidad |
| M1.1-PA02 | PA | Portafolio de productos-control con owners | misma unidad |

**Pregunta generadora:** ¿Qué tareas de mantenimiento de su control se dejaron de hacer en los últimos seis meses sin que ninguna métrica lo mostrara?

---

### 018. M1.2-PA01 — FinOps de agentes: presupuesto, costo por tarea y alertas de consumo

**Unidad:** M1.2 Gestión Financiera, Liderazgo de Equipo y Capacitación · **Tipo:** PA · **Horas (sub-plan):** 5 · **Competencias:** C6.4, C8.2 · **Origen:** M1.2-PA01 (V5) · **Extensión:** 273 palabras · **Estado:** Idea central desarrollada (lote PA-01/02) — sub-plan PO-GAC; ID curricular, no ESS.

**Definición / idea central.** Presupuesto de consumo (SCU, créditos, tokens), costo por tarea, forecasting, alertas, optimización y chargeback.

**Brecha frente a los 331.** K01/K02 no incluyen costos variables de IA; ningún AMP/HC trata FinOps.

**Tesis y sentido para el rol.** FinOps aplicado a agentes es la disciplina de presupuestar, medir, asignar y optimizar el consumo variable de la flota: SCU en Security Copilot, créditos o capacidad en Copilot Studio, tokens por modelo en Foundry, más las licencias que habilitan identidad y gobierno. La unidad de gestión es el costo por tarea del agente (consumo dividido por tareas completadas), que permite comparar agentes, detectar desperdicio y pronosticar. La tesis es que el owner de agentes es también el owner de su presupuesto de consumo, con alertas, límites y chargeback, y que sin FinOps la autonomía se vuelve un gasto no gobernado.

**Tensión y límites.** La tensión es entre control y utilidad: límites de consumo muy estrictos apagan al agente justo durante una campaña de phishing, cuando más se lo necesita. Otra tensión es la atribución: en flujos multi-agente (AG-01 → AG-02) el consumo se reparte y el costo por tarea se vuelve ambiguo. El ensayo debe proponer cómo presupuestar con elasticidad (reserva para picos aprobada por anticipado) y cómo atribuir costos en cadenas de agentes.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: FinOps Foundation framework y unit economics. Implementación: construir el modelo de costos de la flota con Azure Cost Management, consumo de SCU, capacidad de Copilot Studio y cuotas de Foundry; definir alertas de presupuesto, costo por tarea por agente (KPI-14), desvío trimestral (KPI-15) y el ritual mensual de revisión; proponer optimizaciones.

**Evidencia y evaluación.** Evidencia: modelo de costos, presupuesto trimestral y alertas configuradas. Se evalúa la trazabilidad del costo por tarea, la existencia de una reserva para picos y la decisión documentada sobre chargeback.

**Puentes.** Extiende M1.2-K01 (presupuesto) y K02 (optimización); se relaciona con HC-036. Depende de G1.2-PA01 (economía unitaria) y sostiene el AGC-15.

**Recomendaciones de práctica y ejercitación.**
1. Construir el modelo de costos de la flota (SCU, capacidad de Copilot Studio, tokens de Foundry, licencias) con costo por tarea por agente.
2. Definir presupuesto trimestral con reserva para picos, alertas en Azure Cost Management y regla de atribución en cadenas AG-01→AG-02.
3. Proponer tres optimizaciones (modelo, prompt, frecuencia) y estimar su efecto.

**Aplicación en el escenario de referencia.** Base agnóstica: FinOps Foundation; unit economics. Implementación Microsoft: Azure Cost Management, SCU, capacidad de Copilot Studio, cuotas de Foundry. Actividad: Construir el modelo de costos de la flota y sus alertas. Evidencia: Modelo de costos.

**Próximos pasos.**
- Operar el ritual mensual de revisión de consumo (KPI-14/15) y el AGC-15.
- Alimentar el reporte ejecutivo (G6.1-PA01) con costo por tarea.
- Revisar la decisión de ruta de construcción (M6.2-PA01) con los datos de consumo reales.

**Relación con los conceptos de la(s) unidad(es) M1.2.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M1.2-K01 | K | Presupuesto | EXTIENDE |
| M1.2-K02 | K | Optimización Recursos | EXTIENDE |
| M1.2-K03 | K | RFI/RFP | misma unidad |
| M1.2-K04 | K | Liderazgo de Equipo | misma unidad |
| M1.2-K05 | K | Habilidades Técnicas | misma unidad |
| M1.2-K06 | K | Concienciación | misma unidad |
| M1.2-K07 | K | Capacitación | misma unidad |
| M1.2-K08 | K | Gestión Talento | misma unidad |
| M1.2-K09 | K | Efectividad Capacitación | misma unidad |
| M1.2-K10 | K | Ética en Equipo | misma unidad |
| AMP-29 | AMP | Competencias humanas y agentes | misma unidad |
| AMP-30 | AMP | Adopción responsable de IA | misma unidad |
| HC-013 | HC | Deuda de seguridad como riesgo de transformación | misma unidad |
| HC-025 | HC | Competencias y resiliencia organizacional | misma unidad |
| HC-026 | HC | Ética, cultura y controles internos | misma unidad |
| HC-036 | HC | Portafolio de controles y capacidades | SE_RELACIONA |
| HC-037 | HC | Alineación entre competencias y decisiones | misma unidad |
| M1.2-PA02 | PA | Requisitos de IA y agentes en contratos de servicios gestionados | misma unidad |
| M1.2-PA03 | PA | Itinerario de desarrollo: de analista a PO-GAC | misma unidad |

**Pregunta generadora:** ¿Qué agente de su flota tiene el costo por tarea más alto, y sabe si es porque trabaja en casos difíciles o porque está mal diseñado?

---

### 019. M1.2-PA02 — Requisitos de IA y agentes en contratos de servicios gestionados

**Unidad:** M1.2 Gestión Financiera, Liderazgo de Equipo y Capacitación · **Tipo:** PA · **Horas (sub-plan):** 3 · **Competencias:** C7.2 · **Origen:** M1.2-PA03 (V5) · **Extensión:** 310 palabras · **Estado:** Idea central desarrollada (lote PA-01/02) — sub-plan PO-GAC; ID curricular, no ESS.

**Definición / idea central.** Requisitos, SLAs, KPIs, evidencia, interoperabilidad con agentes propios y salida para MSSP/MDR y plataformas de IA.

**Brecha frente a los 331.** K03 es genérico; HC-008 y AMP-12 no bajan al anexo contractual.

**Tesis y sentido para el rol.** Cuando un servicio gestionado (MDR, MSSP) opera con sus propios agentes sobre el entorno del cliente, o cuando se contrata una plataforma de IA, el contrato debe decir lo que la política de agentes dice para los agentes propios: qué pueden hacer, con qué identidad, con qué datos, qué evidencia entregan, cómo se integran con los agentes del cliente, qué pasa cuando fallan y cómo se sale. La tesis es que los RFI/RFP de servicios de seguridad necesitan un anexo de requisitos de IA y agentes, y que la responsabilidad por lo que hace el agente del proveedor (AMP-12) debe quedar escrita y no supuesta.

**Tensión y límites.** La tensión es de asimetría: el proveedor conoce su tecnología y el cliente no; los requisitos genéricos ("usar IA responsable") no obligan a nada. HC-008 plantea la cadena de confianza en terceros; aquí el eslabón es un agente que actúa en el tenant del cliente. Otra tensión es la interoperabilidad: el agente del MDR y el agente propio pueden actuar sobre el mismo incidente sin coordinación. El ensayo debe discutir cláusulas de identidad propia del agente del proveedor, límites de acción, evidencia compartida y derecho a desactivar.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: TPRM y C-SCRM (SP 800-161). Implementación: redactar el anexo de requisitos de IA para un RFP de MDR con secciones de identidad (Entra Agent ID para agentes del proveedor), permisos, datos y residencia, evidencia (trazas entregadas al Sentinel del cliente), niveles de autonomía permitidos, kill switch, incidentes causados por el agente, métricas y salida; apoyarse en el Trust Center y en la responsabilidad compartida de la plataforma.

**Evidencia y evaluación.** Evidencia: anexo RFP de dos páginas y matriz de evaluación de propuestas. Se evalúa que cada requisito sea verificable y que la responsabilidad por acciones del agente del proveedor quede asignada.

**Puentes.** Extiende M1.2-K03 (RFI/RFP); se apoya en HC-008; se relaciona con AMP-12 y M6.2-K08 (TPRM). Sostiene la competencia C7.2.

**Recomendaciones de práctica y ejercitación.**
1. Redactar el anexo de requisitos de IA y agentes para un RFP de MDR (identidad, permisos, datos, evidencia, autonomía, kill switch, incidentes, métricas, salida).
2. Construir la matriz de evaluación de propuestas con criterio verificable por requisito.
3. Revisar un contrato vigente (o plantilla) y marcar qué cláusula se aplicaría ante un error del agente del proveedor.

**Aplicación en el escenario de referencia.** Base agnóstica: TPRM; C-SCRM (SP 800-161). Implementación Microsoft: Cláusulas de IA; responsabilidad compartida; Trust Center. Actividad: Redactar el anexo de requisitos de IA para un RFP de MDR. Evidencia: Anexo RFP.

**Próximos pasos.**
- Alinear el anexo con la política de agentes (G2.2-PA01) y el RACI (G4.1-PA01).
- Incorporar los agentes del proveedor al registro (M2.1-PA01) y al organigrama híbrido (M1.1-PA01).
- Revisar el anexo con Legal y Compras.

**Relación con los conceptos de la(s) unidad(es) M1.2.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M1.2-K01 | K | Presupuesto | misma unidad |
| M1.2-K02 | K | Optimización Recursos | misma unidad |
| M1.2-K03 | K | RFI/RFP | EXTIENDE |
| M1.2-K04 | K | Liderazgo de Equipo | misma unidad |
| M1.2-K05 | K | Habilidades Técnicas | misma unidad |
| M1.2-K06 | K | Concienciación | misma unidad |
| M1.2-K07 | K | Capacitación | misma unidad |
| M1.2-K08 | K | Gestión Talento | misma unidad |
| M1.2-K09 | K | Efectividad Capacitación | misma unidad |
| M1.2-K10 | K | Ética en Equipo | misma unidad |
| AMP-29 | AMP | Competencias humanas y agentes | misma unidad |
| AMP-30 | AMP | Adopción responsable de IA | misma unidad |
| HC-013 | HC | Deuda de seguridad como riesgo de transformación | misma unidad |
| HC-025 | HC | Competencias y resiliencia organizacional | misma unidad |
| HC-026 | HC | Ética, cultura y controles internos | misma unidad |
| HC-036 | HC | Portafolio de controles y capacidades | misma unidad |
| HC-037 | HC | Alineación entre competencias y decisiones | misma unidad |
| M1.2-PA01 | PA | FinOps de agentes: presupuesto, costo por tarea y alertas de consumo | misma unidad |
| M1.2-PA03 | PA | Itinerario de desarrollo: de analista a PO-GAC | misma unidad |
| HC-008 | HC | Cadena de confianza en terceros | SE_APOYA_EN (otra unidad) |
| AMP-12 | AMP | Responsabilidad por agentes | SE_RELACIONA (otra unidad) |
| M6.2-K08 | K | Riesgo Terceros (TPRM) | SE_RELACIONA (otra unidad) |

**Pregunta generadora:** Si el agente de su proveedor MDR removiera por error el correo de su director financiero, ¿qué cláusula de su contrato actual se aplicaría?

---

### 020. M1.2-PA03 — Itinerario de desarrollo: de analista a PO-GAC

**Unidad:** M1.2 Gestión Financiera, Liderazgo de Equipo y Capacitación · **Tipo:** PA · **Horas (sub-plan):** 3 · **Competencias:** C7.1 · **Origen:** M1.2-PA04 (V5) · **Extensión:** 265 palabras · **Estado:** Idea central desarrollada (lote PA-01/02) — sub-plan PO-GAC; ID curricular, no ESS.

**Definición / idea central.** Itinerario de competencias, evidencias y evaluación del rol; autoevaluación y plan individual.

**Brecha frente a los 331.** HC-037 y AMP-29 no definen el itinerario de carrera hacia la gestión de agentes.

**Tesis y sentido para el rol.** Convertir a un analista en PO-GAC es un itinerario de competencias, no un curso: parte de una autoevaluación contra el marco (ocho dominios, cuarenta y una competencias, niveles N1 a N4), identifica brechas, asigna lecciones del GM-24 y del sub-plan, exige evidencias por etapa y culmina en un capstone donde el participante opera el control con su flota durante un trimestre. HC-037 plantea alinear competencias y decisiones; AMP-29 rediseñar roles del equipo híbrido. La tesis es que el itinerario es a la vez instrumento de desarrollo individual y control de gobierno (AGC-23): nadie opera agentes L2 o superiores sin acreditar las competencias.

**Tensión y límites.** La tensión es el tiempo: el itinerario suma cientos de horas sobre un analista que ya opera un SOC; sin protección de agenda y sin práctica integrada en el trabajo real, el plan se vuelve aspiracional. Otra tensión es la evaluación: medir competencias de gobierno con exámenes es inútil; se necesitan evidencias de decisiones reales y una defensa ante quienes dependen de esas decisiones.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: competency-based development. Implementación: completar la autoevaluación, construir el plan individual con las etapas E0–E5, seleccionar módulos del Ninja Training interno y de Microsoft Learn como apoyo, y acordar con el manager las evidencias y el calendario; validar la vigencia de certificaciones de apoyo (SC-200, SC-401, AI-900, AAISM) antes de incluirlas.

**Evidencia y evaluación.** Evidencia: autoevaluación firmada y plan individual con hitos y evidencias. Se evalúa el realismo del calendario, la cobertura de los ocho dominios y la definición del capstone.

**Puentes.** Instancia HC-037; operacionaliza AMP-29; se relaciona con M1.2-K07 (capacitación) y K08 (gestión del talento). Es el documento 06 del sub-plan.

**Recomendaciones de práctica y ejercitación.**
1. Completar la autoevaluación de las 41 competencias (N1–N4) con una evidencia real por competencia acreditada.
2. Construir el plan individual E0–E5 con hitos, evidencias y horas protegidas; acordarlo con el manager.
3. Seleccionar módulos de apoyo (Ninja Training, Microsoft Learn) y validar vigencia de certificaciones (SC-200, SC-401, AI-900, AAISM).

**Aplicación en el escenario de referencia.** Base agnóstica: Competency-based development. Implementación Microsoft: Este sub-plan; Ninja Training; SC-200/SC-401/AI-900 (validar vigencia). Actividad: Autoevaluación inicial y plan individual. Evidencia: Plan individual.

**Próximos pasos.**
- Registrar la autoevaluación como línea base y repetirla al cierre de E3 y E5.
- Usar el itinerario como evidencia del AGC-23 antes de operar agentes L2+.
- Revisar el itinerario con los resultados de la revisión de desempeño de la flota.

**Relación con los conceptos de la(s) unidad(es) M1.2.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M1.2-K01 | K | Presupuesto | misma unidad |
| M1.2-K02 | K | Optimización Recursos | misma unidad |
| M1.2-K03 | K | RFI/RFP | misma unidad |
| M1.2-K04 | K | Liderazgo de Equipo | misma unidad |
| M1.2-K05 | K | Habilidades Técnicas | misma unidad |
| M1.2-K06 | K | Concienciación | misma unidad |
| M1.2-K07 | K | Capacitación | SE_RELACIONA |
| M1.2-K08 | K | Gestión Talento | SE_RELACIONA |
| M1.2-K09 | K | Efectividad Capacitación | misma unidad |
| M1.2-K10 | K | Ética en Equipo | misma unidad |
| AMP-29 | AMP | Competencias humanas y agentes | OPERACIONALIZA |
| AMP-30 | AMP | Adopción responsable de IA | misma unidad |
| HC-013 | HC | Deuda de seguridad como riesgo de transformación | misma unidad |
| HC-025 | HC | Competencias y resiliencia organizacional | misma unidad |
| HC-026 | HC | Ética, cultura y controles internos | misma unidad |
| HC-036 | HC | Portafolio de controles y capacidades | misma unidad |
| HC-037 | HC | Alineación entre competencias y decisiones | INSTANCIA_DE |
| M1.2-PA01 | PA | FinOps de agentes: presupuesto, costo por tarea y alertas de consumo | misma unidad |
| M1.2-PA02 | PA | Requisitos de IA y agentes en contratos de servicios gestionados | misma unidad |

**Pregunta generadora:** ¿Qué competencia del marco podría acreditar hoy con una evidencia real de su trabajo, y cuál no podría acreditar ni con un año más de hacer lo mismo?

---

### 021. M2.1-PA01 — Registro de agentes como clase de activo

**Unidad:** M2.1 Gestión de Activos y Seguridad del Ciclo de Vida de los Datos · **Tipo:** PA · **Horas (sub-plan):** 4 · **Competencias:** C5.3 · **Origen:** M2.1-PA01 (V5) · **Extensión:** 268 palabras · **Estado:** Idea central desarrollada (lote PA-01/02) — sub-plan PO-GAC; ID curricular, no ESS.

**Definición / idea central.** Registro de agentes propios y de terceros con dueño, criticidad, datos, dependencias y estado de ciclo de vida.

**Brecha frente a los 331.** K03 inventaría activos clásicos; AMP-33 solo la credencial.

**Tesis y sentido para el rol.** Un agente es un activo de información con características propias: tiene dueño, criticidad, dependencias (modelo, conectores, fuentes de conocimiento, identidad), datos que toca y un estado de ciclo de vida que cambia rápido. El inventario de activos clásico (M2.1-K03) no lo contempla y el inventario de identidades no humanas (AMP-33) solo captura su credencial. La tesis es que la flota debe registrarse como una clase de activo propia, con un registro que la segunda línea pueda consultar y que alimente el riesgo, la continuidad y el presupuesto.

**Tensión y límites.** La tensión es la proliferación: crear un agente cuesta minutos y el registro puede quedar atrás desde el primer día; Shadow AI (M6.2-K06) es la versión agéntica del activo no inventariado. Otra tensión es el perímetro: ¿se registran los agentes del proveedor MDR, los agentes nativos de Security Copilot, los que un analista creó para sí? El ensayo debe argumentar un criterio de inclusión basado en lo que el agente puede tocar, no en quién lo creó.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: gestión de activos e inventario de sistemas de IA (ISO/IEC 42001 A.6). Implementación: inventariar la flota del control en Agent 365 y Power Platform admin center con dueño, sponsor, criticidad, datos, dependencias, nivel de autonomía, estado y fecha de revisión; definir reglas de descubrimiento de agentes no registrados.

**Evidencia y evaluación.** Evidencia: inventario de la flota con todos los campos y la regla de descubrimiento. Se evalúa la cobertura frente a los agentes observados en el tenant y la calidad de las dependencias declaradas.

**Puentes.** Extiende M2.1-K03 (inventario); se relaciona con AMP-33 (identidades no humanas) y AMP-28 (orquestación). Sostiene AGC-01 y AGC-19 y alimenta M6.1-PA01 (dependencias).

**Recomendaciones de práctica y ejercitación.**
1. Inventariar los 15 agentes del catálogo con dueño, sponsor, criticidad, datos, dependencias (modelo, conectores, knowledge, identidad), autonomía, estado y fecha de revisión.
2. Definir el criterio de inclusión (por lo que el agente puede tocar) y aplicarlo a agentes del MDR, nativos y personales.
3. Diseñar la regla de descubrimiento de agentes no registrados (Power Platform admin center, Agent 365, app registrations).

**Aplicación en el escenario de referencia.** Base agnóstica: Gestión de activos; ISO/IEC 42001 A.6; CMDB. Implementación Microsoft: Agent 365 registry; Power Platform admin center. Actividad: Inventariar la flota con criticidad y dependencias. Evidencia: Inventario.

**Próximos pasos.**
- Cargar el inventario en Agent 365 y conectarlo con AGC-01/AGC-19.
- Alimentar el mapa de dependencias de M6.1-PA01.
- Reconciliar el inventario mensualmente contra lo observado en el tenant.

**Relación con los conceptos de la(s) unidad(es) M2.1.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M2.1-K01 | K | Identificación Activos | misma unidad |
| M2.1-K02 | K | Clasificación | misma unidad |
| M2.1-K03 | K | Inventario | EXTIENDE |
| M2.1-K04 | K | Ciclo de Vida Datos | misma unidad |
| M2.1-K05 | K | Seguridad Reposo/Tránsito | misma unidad |
| M2.1-K06 | K | Retención/Destrucción | misma unidad |
| M2.1-K07 | K | Gobernanza Datos | misma unidad |
| M2.1-K08 | K | Activos Críticos | misma unidad |
| M2.1-K09 | K | Auditoría Activos | misma unidad |
| M2.1-K10 | K | Riesgos de Datos | misma unidad |
| AMP-31 | AMP | DSPM | misma unidad |
| AMP-32 | AMP | Gobierno de datos para RAG | misma unidad |
| HC-011 | HC | Seguridad de datos en la IA empresarial | misma unidad |
| HC-014 | HC | Arquitectura de riesgo empresarial | misma unidad |
| HC-016 | HC | Superficie de ataque contextualizada | misma unidad |
| HC-024 | HC | Cumplimiento y privacidad por diseño | misma unidad |
| HC-033 | HC | Seguridad y soberanía de datos distribuidos | misma unidad |
| AMP-33 | AMP | Identidades no humanas | SE_RELACIONA (otra unidad) |
| AMP-28 | AMP | Orquestación de agentes | SE_RELACIONA (otra unidad) |

**Pregunta generadora:** ¿Cuántos agentes operan en su tenant, cuántos están en su inventario, y cómo sabe la diferencia?

---

### 022. M2.2-PA01 — Permisos de humanos y agentes en el control: RBAC unificado, roles y conectores

**Unidad:** M2.2 Gestión de Identidad y Acceso (IAM) y Principios de Confianza Cero · **Tipo:** PA · **Horas (sub-plan):** 4 · **Competencias:** C2.6, C5.2 · **Origen:** Nuevo V6 · **Extensión:** 311 palabras · **Estado:** Idea central desarrollada (lote PA-01/02) — sub-plan PO-GAC; ID curricular, no ESS.

**Definición / idea central.** Permisos mínimos por tarea para personas (Unified RBAC, roles de Exchange/Defender) y agentes (conectores, API permissions).

**Brecha frente a los 331.** K03 y AMP-34/36 fijan principios; falta la práctica tarea→rol→permiso.

**Tesis y sentido para el rol.** La autorización es la competencia que decide qué puede hacer una identidad; M2.2-K03 la enseña para personas y AMP-34 y AMP-36 fijan los principios para agentes. Lo que falta es la práctica: la matriz que asigna, para cada tarea del modelo operativo, el rol mínimo de la persona (Unified RBAC de Defender XDR, roles de Exchange Online y de Defender for Office 365) y los permisos mínimos del agente (permisos de conectores en Power Platform, API permissions de la identidad de agente, acceso condicional). La tesis es que humanos y agentes deben aparecer en la misma matriz tarea→rol→permiso, porque comparten tareas y porque la separación de funciones entre ellos (el humano aprueba lo que el agente ejecuta) solo es real si los permisos lo hacen cumplir.

**Tensión y límites.** La tensión es la deriva por comodidad: los agentes se crean con la identidad del constructor o con permisos amplios "para probar" y así quedan; los agentes que actúan en nombre de un usuario arrancan sin permisos y su techo es el del usuario, pero el riesgo del agente se evalúa aparte. Otra tensión es la granularidad: la plataforma no siempre ofrece el permiso exacto que la ficha pide. El ensayo debe mostrar cómo compensar un permiso excesivo con límites de herramientas y aprobación humana.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: least privilege, RBAC/ABAC, separación de funciones. Implementación: construir la matriz para las 31 tareas del modelo operativo con rol humano y permisos del agente, revisar los permisos de conectores de tres agentes contra su ficha y configurar acceso condicional para identidades de agentes.

**Evidencia y evaluación.** Evidencia: matriz tarea→rol→permiso para humanos y agentes y el informe de revisión de permisos. Se evalúa que ningún agente supere los permisos de su ficha y que la separación aprobador/ejecutor esté garantizada por permisos y no por costumbre.

**Puentes.** Instancia M2.2-K03 (autorización); operacionaliza AMP-34 y AMP-36; se relaciona con M2.2-K04 (PAM). Sostiene AGC-05, AGC-06 y AGC-18.

**Recomendaciones de práctica y ejercitación.**
1. Construir la matriz tarea→rol humano→permisos del agente para las 31 tareas (Unified RBAC, roles de Exchange/MDO, conectores, API permissions).
2. Revisar los permisos de conectores de AG-02, AG-03 y AG-10 contra sus fichas y anexos; documentar excesos y compensaciones.
3. Configurar acceso condicional para una identidad de agente en el entorno de prueba y verificar el efecto.

**Aplicación en el escenario de referencia.** Base agnóstica: Least privilege; RBAC/ABAC; separación de funciones. Implementación Microsoft: Defender XDR Unified RBAC, roles de Exchange/MDO, políticas de conectores (PPAC), API permissions de Agent ID. Actividad: Construir la matriz tarea→rol→permiso para humanos y agentes. Evidencia: Matriz de permisos.

**Próximos pasos.**
- Usar la matriz como evidencia de AGC-05/06 y como insumo de la recertificación trimestral (AGC-18, MDO-Q03).
- Actualizar la matriz en cada cambio de ficha o de conector (M6.2-PA02).
- Reportar permisos excesivos no compensables como riesgo (G4.1-PA02).

**Relación con los conceptos de la(s) unidad(es) M2.2.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M2.2-K01 | K | Estrategias IAM | misma unidad |
| M2.2-K02 | K | Autenticación | misma unidad |
| M2.2-K03 | K | Autorización | INSTANCIA_DE |
| M2.2-K04 | K | PAM (Privilegiados) | SE_RELACIONA |
| M2.2-K05 | K | Zero Trust | misma unidad |
| M2.2-K06 | K | ZTNA | misma unidad |
| M2.2-K07 | K | Ciclo Vida Identidad | misma unidad |
| M2.2-K08 | K | Auditoría IAM | misma unidad |
| M2.2-K09 | K | Federación | misma unidad |
| M2.2-K10 | K | Contexto de Acceso | misma unidad |
| AMP-33 | AMP | Identidades no humanas | misma unidad |
| AMP-34 | AMP | Identidad y autorización de agentes | OPERACIONALIZA |
| HC-009 | HC | Gobierno de identidades no humanas | misma unidad |
| HC-010 | HC | Autonomía delegada y límites de acción | misma unidad |
| HC-015 | HC | Gobierno y operación de Zero Trust | misma unidad |
| HC-032 | HC | Evaluación adversarial de sistemas autónomos | misma unidad |
| HC-038 | HC | Aseguramiento de la arquitectura Zero Trust | misma unidad |
| AMP-36 | AMP | Límites de herramientas y permisos | OPERACIONALIZA (otra unidad) |

**Pregunta generadora:** ¿Qué podría hacer hoy el agente más privilegiado de su flota si su instrucción fuera manipulada, y qué permiso concreto lo impediría?

---

### 023. M3.1-PA01 — Arquitectura de referencia del SOC agéntico con control plane

**Unidad:** M3.1 Arquitectura de Seguridad, Ingeniería y Diseño (Incl. Zero Trust) · **Tipo:** PA · **Horas (sub-plan):** 5 · **Competencias:** C3.1, C4.2 · **Origen:** M3.1-PA01 (V5) · **Extensión:** 305 palabras · **Estado:** Idea central desarrollada (lote PA-01/02) — sub-plan PO-GAC; ID curricular, no ESS.

**Definición / idea central.** Capas: señales, XDR/SIEM, orquestación, agentes, control plane de gobierno, humanos; límites de confianza.

**Brecha frente a los 331.** AMP-35/39 y HC-019 no dibujan el control plane como capa explícita.

**Tesis y sentido para el rol.** La arquitectura de referencia del SOC agéntico organiza en capas lo que hoy aparece disperso: señales y datos (telemetría, correo, identidades), plataforma de detección y respuesta (XDR, SIEM), orquestación (playbooks deterministas), agentes (nativos y propios), control plane de gobierno (registro, identidad, datos, observabilidad, políticas) y personas (owners, aprobadores, auditores), con límites de confianza explícitos entre capas. AMP-35 pide separar planificación, herramientas, datos y permisos; AMP-39 y HC-019 describen el SOC agéntico y su supervisión. La tesis es que el control plane debe dibujarse como capa propia, porque es donde el gobierno se vuelve arquitectura y donde se deciden los límites que los agentes no pueden cruzar.

**Tensión y límites.** La tensión es que el control plane no es un producto único (en el escenario lo forman Agent 365, Entra Agent ID, Purview y Power Platform admin center) y su integración con la plataforma de detección es parcial; el riesgo es dibujar una arquitectura más integrada de lo que el tenant permite. Otra tensión es el límite de confianza entre el contenido que el agente procesa (correo hostil) y las acciones que puede ejecutar: la arquitectura debe hacer visible ese límite.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: arquitectura de referencia y Zero Trust. Implementación: dibujar la arquitectura objetivo del SOC agéntico de la organización con Defender XDR, Sentinel, Security Copilot y agentes propios (Copilot Studio o Foundry), Agent 365, Entra Agent ID, Purview y Defender para IA; marcar límites de confianza, flujos de aprobación y puntos de observabilidad; declarar qué integraciones están disponibles, en preview o pendientes.

**Evidencia y evaluación.** Evidencia: diagrama comentado con capas, límites de confianza y estado de disponibilidad. Se evalúa la honestidad sobre lo que el tenant permite y la coherencia con las fichas de agentes.

**Puentes.** Profundiza AMP-35; se apoya en AMP-39 y HC-019; se relaciona con M3.1-K03 (Zero Trust). Es el diagrama 2 del documento 07 y la base de M6.2-PA01.

**Recomendaciones de práctica y ejercitación.**
1. Dibujar la arquitectura objetivo del SOC agéntico con las seis capas y los límites de confianza; marcar disponibilidad (GA/preview/pendiente) de cada integración.
2. Trazar el camino de un correo hostil desde la señal hasta una acción de agente y señalar la capa que impide que se convierta en instrucción.
3. Verificar la coherencia del diagrama con los anexos de los 15 agentes (tools, knowledge, identidad).

**Aplicación en el escenario de referencia.** Base agnóstica: Arquitectura de referencia; Zero Trust. Implementación Microsoft: Defender XDR + Sentinel + Security Copilot/agentes propios + Agent 365 + Entra Agent ID + Purview. Actividad: Dibujar la arquitectura objetivo del SOC agéntico. Evidencia: Diagrama comentado.

**Próximos pasos.**
- Usar el diagrama como base de M6.2-PA01 (rutas) y del documento 07.
- Actualizarlo tras cambios de plataforma detectados por AG-09.
- Someterlo a revisión de arquitectura y de la segunda línea.

**Relación con los conceptos de la(s) unidad(es) M3.1.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M3.1-K01 | K | Arquitectura de Seguridad | misma unidad |
| M3.1-K02 | K | Ingeniería de Seguridad | misma unidad |
| M3.1-K03 | K | Zero Trust (Arquitectura) | SE_RELACIONA |
| M3.1-K04 | K | Diseño Seguro (SbD) | misma unidad |
| M3.1-K05 | K | TOGAF y Seguridad | misma unidad |
| M3.1-K06 | K | ZTNA (Acceso) | misma unidad |
| M3.1-K07 | K | Microsegmentación | misma unidad |
| M3.1-K08 | K | Defensa en Profundidad | misma unidad |
| M3.1-K09 | K | Mínimo Privilegio (Arquitectura) | misma unidad |
| M3.1-K10 | K | Resiliencia (Diseño) | misma unidad |
| AMP-35 | AMP | Arquitectura de sistemas agénticos | PROFUNDIZA |
| AMP-36 | AMP | Límites de herramientas y permisos | misma unidad |
| HC-002 | HC | Apetito de riesgo convertido en arquitectura | misma unidad |
| HC-010 | HC | Autonomía delegada y límites de acción | misma unidad |
| HC-013 | HC | Deuda de seguridad como riesgo de transformación | misma unidad |
| HC-014 | HC | Arquitectura de riesgo empresarial | misma unidad |
| HC-015 | HC | Gobierno y operación de Zero Trust | misma unidad |
| HC-023 | HC | Riesgo de concentración tecnológica | misma unidad |
| HC-030 | HC | Seguridad industrial y continuidad de negocio | misma unidad |
| HC-034 | HC | Decisiones reversibles y riesgo de transición | misma unidad |
| HC-038 | HC | Aseguramiento de la arquitectura Zero Trust | misma unidad |
| HC-040 | HC | Homeostasis organizacional de seguridad | misma unidad |
| M3.1-K11 | K | Arquitectura empresarial y arquitectura de seguridad de la información | misma unidad |
| M3.1-K12 | K | Seguridad física, ambiental y mantenimiento como dependencias del control | misma unidad |
| M3.1-PA02 | PA | Arquitectura de protección del dominio Zero Trust (instancias: correo y colaboración · detección y respuesta unificada · endpoints · identidades · datos) | misma unidad |
| AMP-39 | AMP | SOC agéntico | SE_APOYA_EN (otra unidad) |
| HC-019 | HC | SOC agéntico con supervisión humana | SE_APOYA_EN (otra unidad) |

**Pregunta generadora:** ¿Dónde, en su arquitectura, un correo malicioso deja de ser dato y podría convertirse en instrucción para un agente, y qué capa lo impide?

---

### 024. M3.1-PA02 — Arquitectura de protección del dominio Zero Trust (instancias: correo y colaboración · detección y respuesta unificada · endpoints · identidades · datos)

**Unidad:** M3.1 Arquitectura de Seguridad, Ingeniería y Diseño (Incl. Zero Trust) · **Tipo:** PA · **Horas (sub-plan):** 5 · **Competencias:** C2.1 · **Origen:** M3.1-PA03 (V5) · **Título V7:** Arquitectura de protección de correo y colaboración · **Extensión:** 314 palabras · **Estado:** Idea central desarrollada (lote PA-01/02) — PROMOVIDO al programa (V7-C04) — título generalizado (V7.1); ID curricular, no ESS.

**Definición / idea central.** Capas de protección y flujo de correo; autenticación (SPF/DKIM/DMARC/ARC); cobertura de Teams/SharePoint/OneDrive; remediación post-entrega.

**Brecha frente a los 331.** Ningún concepto de los 331 trata la arquitectura del dominio productividad.

**Tesis y sentido para el rol.** La protección del correo y la colaboración es una arquitectura de capas que el owner debe poder explicar de memoria: reputación y autenticación del remitente (SPF, DKIM, DMARC, ARC), filtrado anti-malware y anti-spam, protección contra phishing y suplantación, detonación de adjuntos y reescritura de URL en el momento del clic, remediación posterior a la entrega cuando el veredicto cambia, y extensión de las mismas protecciones a archivos en SharePoint, OneDrive y Teams. La tesis es que ningún concepto de los 331 trata esta arquitectura, y que sin ella el owner no puede diagnosticar por qué un mensaje fue entregado o bloqueado ni asignar con sentido las tareas del modelo operativo. En V7.1 el concepto se generaliza como arquitectura de protección del dominio: esta es su instancia de referencia (correo y colaboración); XDR, endpoints, identidades y datos tienen la suya.

**Tensión y límites.** La tensión es entre seguridad y flujo de correo: cada capa agrega latencia, falsos positivos y excepciones; el owner negocia permanentemente con la mesa de mensajería. Otra tensión es la cobertura: la colaboración (Teams, archivos compartidos) tiene protecciones distintas del correo y el adversario lo sabe. El ensayo debe mostrar cinco casos de entrega y qué capa decidió en cada uno.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: arquitectura SEG/ICES y los RFC de autenticación de correo. Implementación: Exchange Online Protection más Defender for Office 365 Plan 2 (Safe Links, Safe Attachments, anti-phishing con protección de impersonación, Zero-hour auto purge, políticas preestablecidas Standard/Strict, Safe Attachments para SharePoint, OneDrive y Teams); dibujar el flujo y ubicar en él las tareas MDO-D05 a MDO-D09 y MDO-M01 a MDO-M03.

**Evidencia y evaluación.** Evidencia: diagrama de arquitectura y análisis de cinco casos. Se evalúa la precisión técnica, la correcta ubicación de cada tarea del modelo operativo y la identificación de la capa que decidió en cada caso.

**Puentes.** Instancia M3.1-K08 (defensa en profundidad); se relaciona con M3.1-K04 (diseño seguro). Base técnica de M4.1-PA01 a PA04 y de M4.2-PA01.

**Recomendaciones de práctica y ejercitación.**
1. Dibujar el flujo de protección del correo (autenticación, filtrado, anti-phishing, detonación, URL, remediación post-entrega) y ubicar en él las tareas MDO-D05–D09 y M01–M03.
2. Analizar cinco casos de entrega (bloqueado en autenticación, detonado, reescrito, entregado y removido por ZAP, entregado por override) y señalar la capa que decidió.
3. Explicar en cinco minutos a un no especialista por qué un phishing reciente llegó a un buzón.

**Aplicación en el escenario de referencia.** Base agnóstica: Email security architecture (SEG/ICES); RFC SPF/DKIM/DMARC. Implementación Microsoft: EOP + Defender for Office 365 (Safe Links, Safe Attachments, anti-phishing, ZAP, presets). Actividad: Explicar la arquitectura con 5 casos de entrega. Evidencia: Diagrama + análisis.

**Próximos pasos.**
- Usar el diagrama como base técnica de M4.1-PA01–PA04 y M4.2-PA01.
- Verificar en el tenant la configuración de cada capa frente a Standard/Strict (G2.2-PA03).
- Extender el análisis a Teams, SharePoint y OneDrive; instanciar en los demás dominios (paquetes Dominio_*).

**Relación con los conceptos de la(s) unidad(es) M3.1.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M3.1-K01 | K | Arquitectura de Seguridad | misma unidad |
| M3.1-K02 | K | Ingeniería de Seguridad | misma unidad |
| M3.1-K03 | K | Zero Trust (Arquitectura) | misma unidad |
| M3.1-K04 | K | Diseño Seguro (SbD) | SE_RELACIONA |
| M3.1-K05 | K | TOGAF y Seguridad | misma unidad |
| M3.1-K06 | K | ZTNA (Acceso) | misma unidad |
| M3.1-K07 | K | Microsegmentación | misma unidad |
| M3.1-K08 | K | Defensa en Profundidad | INSTANCIA_DE |
| M3.1-K09 | K | Mínimo Privilegio (Arquitectura) | misma unidad |
| M3.1-K10 | K | Resiliencia (Diseño) | misma unidad |
| AMP-35 | AMP | Arquitectura de sistemas agénticos | misma unidad |
| AMP-36 | AMP | Límites de herramientas y permisos | misma unidad |
| HC-002 | HC | Apetito de riesgo convertido en arquitectura | misma unidad |
| HC-010 | HC | Autonomía delegada y límites de acción | misma unidad |
| HC-013 | HC | Deuda de seguridad como riesgo de transformación | misma unidad |
| HC-014 | HC | Arquitectura de riesgo empresarial | misma unidad |
| HC-015 | HC | Gobierno y operación de Zero Trust | misma unidad |
| HC-023 | HC | Riesgo de concentración tecnológica | misma unidad |
| HC-030 | HC | Seguridad industrial y continuidad de negocio | misma unidad |
| HC-034 | HC | Decisiones reversibles y riesgo de transición | misma unidad |
| HC-038 | HC | Aseguramiento de la arquitectura Zero Trust | misma unidad |
| HC-040 | HC | Homeostasis organizacional de seguridad | misma unidad |
| M3.1-K11 | K | Arquitectura empresarial y arquitectura de seguridad de la información | misma unidad |
| M3.1-K12 | K | Seguridad física, ambiental y mantenimiento como dependencias del control | misma unidad |
| M3.1-PA01 | PA | Arquitectura de referencia del SOC agéntico con control plane | misma unidad |

**Pregunta generadora:** Para el último mensaje de phishing que llegó a un buzón de su organización, ¿qué capa debería haberlo detenido y por qué no lo hizo?

> **Instancias de dominio (V7.1).** Este pre-ensayo desarrolla la instancia de referencia (productividad: Defender for Office 365). Las instancias XDR, Endpoints, Identidades, Datos, SIEM, Nube y Apps están en los paquetes `Dominio_*` (plano B), que no modifican este concepto.


---

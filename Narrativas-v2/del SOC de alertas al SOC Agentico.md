# Del SOC de alertas al SOC agéntico: compilación de la sesión del 24 de noviembre de 2026

## Síntesis integrada

Esta parte combina los tres entregables de la sesión (plan de investigación, informe para el CISO y análisis del caso Zava) con las siete respuestas de la Parte A. Cuando un turno posterior corrigió a uno anterior, aquí figura la versión corregida; la sección B.13 lista esos cambios.

**Cómo leer esta parte.**

- **Estado epistémico:** **[E]** evidencia de una fuente citada, **[I]** inferencia propia, **[R]** recomendación, **[D]** decisión o dato pendiente.
- **Disponibilidad de producto:** **GA**, **Preview** u **Hoja de ruta**, según los anuncios del 17 al 19 de noviembre de 2026. No se verificó fila por fila en Microsoft Learn.
- **Claves de fuente:** los códigos entre corchetes (MS-05, INT-10, LAB-09) remiten a la Parte C. Las claves INT son material interno de Microsoft.

### B.1 Alcance y método

**Destinatario del análisis.** CISO de un holding de 50.000 empleados con tres unidades de negocio independientes (industria, retail, servicios financieros), un SOC propio de servicios compartidos y la obligación de reportar incidentes de cualquiera de las tres para información de los accionistas.

**Preguntas que guiaron la sesión.**

| ID | Pregunta | Dónde se responde |
|---|---|---|
| RQ1 | ¿Qué procesos se pueden individualizar en un SOC? | B.4 |
| RQ2 y RQ3 | ¿Cuáles fueron impactados o transformados por la IA, cómo y en qué grado? | B.4 |
| RQ4 | ¿Qué procesos son nuevos, por la IA ofensiva y por la IA defensiva? | B.5 |
| RQ5 | ¿Cómo opera un SOC agéntico y qué casos de uso ya están agentificados? | B.6 |
| RQ6 | ¿Qué se puede agentificar con tecnología Microsoft, con cuál y cómo? | B.10 |
| RQ7 y RQ8 | ¿Cuál es la postura de Microsoft y cómo se compara con NIST, CSA, CIS y The Open Group? | B.11 |
| RQ9 | ¿Qué implica para el holding? | B.12 |
| RQ10 (turno 3) | ¿Está reflejado en los workshops SAF SecOps y AI SAF? | B.11.5 |
| RQ11 (turnos 6 y 7) | ¿Cómo debe ser el flujo de respuesta y cómo se analiza el ataque de 75 minutos? | B.6.3 y B.9 |
| RQ12 (turnos 8 y 9) | ¿Cuáles son las narrativas de ataque nuevas y cuáles las previas enriquecidas con IA? | B.7 |
| RQ13 (turno 10) | ¿Qué fuentes de telemetría hay que incorporar? | B.8 |

**Hipótesis de trabajo y resultado.**

| Hipótesis | Resultado |
|---|---|
| H1. La IA no agregó procesos de forma uniforme: aceleró unos, cambió el diseño de otros y creó un grupo de gobierno de agentes | Respaldada [I] |
| H2. Microsoft pasó de "copiloto que asiste" a "sistema de agentes que ejecuta con personas que aprueban", e Ignite 2026 es el punto donde eso se vuelve producto | Respaldada [E: MS-01, MS-02, MS-05] |
| H3. Los marcos coinciden con Microsoft en principios, pero ninguno tiene una norma final para operar un SOC agéntico | Respaldada [E/I] |
| H4. En un holding con reporte a accionistas, el límite de la autonomía es de responsabilidad: la materialidad no se delega | Posición razonada, no un hallazgo; depende del régimen regulatorio, que no se investigó [R] |

**Jerarquía de fuentes usada.** (1) Publicación oficial del emisor; (2) documento oficial en borrador, citado con su madurez; (3) análisis de terceros, marcado como fuente secundaria; (4) material interno de Microsoft, usado para orientar y validar coherencia, no para citar al cliente.

**Fases.** Se ejecutaron el relevamiento de Microsoft, el de marcos, el catálogo de procesos y la comparación. Siguen pendientes la lectura completa de los documentos fuente con verificación del estado GA/Preview en Learn, y la validación con el cliente (régimen regulatorio, topología de tenants, cobertura OT, licenciamiento).

### B.2 Conclusiones integradas

1. **El SOC dejó de ser una cola de alertas atendida por niveles.** En cinco años pasó de analistas que ejecutan con ayuda de automatización, a analistas asistidos por IA generativa, a agentes que ejecutan mientras las personas fijan límites y aprueban. [I, sobre MS-05, MS-06, MS-01]
2. **El motivo es la velocidad y la escala del atacante, no una técnica nueva.** Una campaña de phishing como servicio que tardaba unos catorce días hoy se completa en 85 minutos y pasa de 10 a 3.000 usuarios objetivo [E: MS-02]. El Microsoft Digital Defense Report 2026 lo resume así: los métodos y los blancos no cambiaron; cambiaron la escala y la eficacia [E: MS-46].
3. **Ignite 2026 convirtió la visión en producto.** Microsoft Perception pasó a disponibilidad general con agentes rojos, azules y verdes coordinados por playbooks, y las capacidades centrales de ISOC en Defender también son GA [E: MS-01, MS-02, MS-03].
4. **De 16 procesos clásicos, diez se transforman y seis se aceleran.** Aparecen nueve procesos nuevos y el caso Zava obliga a agregar un décimo: la respuesta sobre agentes del negocio y sus fuentes de conocimiento [I].
5. **De las narrativas de ataque, solo tres no tienen antecedente:** secuestro del agente, envenenamiento de memoria y cascadas entre agentes. Las otras son trece narrativas previas, diez de ellas enriquecidas con IA en grado medio o alto [I].
6. **La telemetría nueva es la del propio agente.** Las narrativas previas se detectan con las fuentes de siempre, más correlación y velocidad. Hay seis fuentes nuevas a incorporar y dos señales para las que no se encontró un registro de seguridad nativo [E/I].
7. **La falla típica es de contexto, no de sensores.** En el caso Zava hubo señal en las cinco etapas y nada las unió [E: LAB-09]. Dos de los cuatro saltos dependen de saber qué almacenamiento alimenta al agente y qué identidad usa, y eso no está en ningún registro [I].
8. **Los marcos independientes coinciden en los principios y llegan tarde en lo operativo.** NIST, CSA, CIS y The Open Group respaldan supervisión humana, identidad y mínimo privilegio para agentes y fundamentos primero. Ninguno tiene una norma final para operar un SOC agéntico [E/I].
9. **El material de Microsoft para clientes está desparejo.** El SAF Modern SecOps y el AI SAF no mencionan Perception ni ISOC; el workshop AI-Powered SOC sí [E: INT-04, INT-06, INT-10].
10. **El vacío más importante para el holding no lo cubre ningún proveedor ni marco:** cómo se gobierna la autonomía de agentes en un SOC compartido entre tres negocios con perfiles de riesgo distintos, y cómo se preserva la decisión humana sobre materialidad y divulgación [I].
11. **Hay una fecha que no depende de la estrategia:** el soporte de Microsoft Sentinel en el portal de Azure termina el 31 de marzo de 2027 [E: EXT-02, INT-03].

**Recomendación central [R].** Adoptar el SOC agéntico por etapas durante 2027, con un modelo de autonomía por niveles que use la reversibilidad de la acción y la criticidad del negocio como criterios, y con una regla explícita: los agentes preparan la evidencia de un incidente; la determinación de materialidad y la divulgación siguen siendo decisiones humanas con responsable nombrado.

### B.3 Por qué cambia el SOC

| Fuerza | Evidencia | Fuente |
|---|---|---|
| El atacante opera a velocidad de máquina | Campaña comparable a EvilTokens: de unos 14 días a 85 minutos; de 10 a 3.000 usuarios objetivo | MS-02 |
| Descubrir y explotar vulnerabilidades se abarató | Exploit funcional en alrededor de un día tras la divulgación de fallas críticas de PHP; unos 29 millones de servicios seguían vulnerables casi dos semanas después | MS-01 |
| El volumen de vulnerabilidades crece | Casi 40.000 CVE publicados en el primer semestre de 2026 | MS-44 |
| La exposición se ataca en horas | Las cargas de nube expuestas son atacadas en 5,3 horas en promedio | MS-46 |
| El modelo manual no escala | 42 % de las alertas quedan sin investigar; los analistas dedican más del 20 % de su tiempo a reunir datos; 91 % de los líderes atribuye a estas brechas un incidente serio (encuesta de Microsoft) | MS-06 |
| Los agentes son un nuevo tipo de actor interno | Microsoft los describe como "los nuevos insiders": operan sin pausa, con acceso amplio, y pueden equivocarse, ser manipulados o comprometidos | MS-01 |
| De asistir a ejecutar | En seis meses el panorama pasó de IA que asiste a operadores humanos, a IA que dirige la actividad de ataque, hacia la ejecución autónoma | MS-44 |
| Presión regulatoria | Directorios y reguladores piden gobierno más fuerte, supervisión humana documentada y reporte rápido y preciso | MS-06 |

**Calibración.** En abril de 2026 Microsoft decía que normalmente sigue habiendo una persona dirigiendo el ataque [E: MS-43]. Las dos campañas asistidas por IA que ATT&CK incorporó fueron dirigidas por personas; la de México se describe como híbrida, con cerca del 75 % de la ejecución remota de comandos a cargo del agente [E: EXT-12].

### B.4 Procesos del SOC y cómo cambiaron

#### B.4.1 Catálogo de 16 procesos

No existe una taxonomía única. Este catálogo combina las funciones de operaciones de seguridad del Security Adoption Framework de Microsoft con las seis funciones de NIST CSF 2.0. Es una síntesis propia [I]. El borrador S252 de The Open Group, que define roles de SecOps, puede servir de respaldo adicional [E: INT-06].

| Grupo | ID | Proceso | Qué hace |
|---|---|---|---|
| Dirigir | P1 | Gobierno, métricas y reporte del SOC | Define misión, mide MTTA y MTTR, informa al negocio |
| Dirigir | P2 | Gestión de incidentes mayores y notificación | Coordina crisis, evalúa impacto, notifica a reguladores y accionistas |
| Anticipar | P3 | Inteligencia de amenazas | Convierte información externa en contexto y prioridades |
| Anticipar | P4 | Gestión de exposición y vulnerabilidades | Prioriza y reduce la superficie de ataque |
| Anticipar | P5 | Validación ofensiva | Red team, pruebas de penetración, simulación de ataques |
| Detectar | P6 | Gestión de datos y telemetría | Ingesta, normalización, retención y salud de conectores |
| Detectar | P7 | Ingeniería de detección | Crea, prueba y ajusta reglas; mide cobertura |
| Detectar | P8 | Monitoreo y triage de alertas | Clasifica alertas en verdaderas o falsas (nivel 1) |
| Responder | P9 | Investigación de incidentes | Reconstruye el ataque, su alcance y sus entidades (nivel 2) |
| Responder | P10 | Threat hunting | Busca amenazas que evadieron la detección (nivel 3) |
| Responder | P11 | Contención, erradicación y remediación | Aísla, bloquea, revoca, limpia |
| Responder | P12 | Forense y análisis de malware | Preserva evidencia y analiza artefactos |
| Responder | P13 | Automatización y orquestación | Mantiene playbooks e integraciones |
| Mejorar | P14 | Recuperación y coordinación con TI y negocio | Restaura servicios y cierra causas |
| Mejorar | P15 | Lecciones aprendidas | Análisis de causa raíz y mejora de controles |
| Mejorar | P16 | Talento, conocimiento y turnos | Formación, documentación, relevo |

#### B.4.2 Evolución en tres momentos

**Los tres momentos.** *2021–2022:* SIEM, SOAR y XDR con aprendizaje automático clásico; la persona ejecuta. *Noviembre de 2026:* IA generativa asistiva madura y primeros sistemas multiagente en GA. *2027:* proyección; el agente ejecuta flujos completos dentro de límites aprobados. Entre 2023 y 2025 hubo una etapa intermedia: Security Copilot como asistente y, desde marzo de 2025, los primeros agentes de Security Copilot [E: MS-14, MS-13].

Las columnas 2021–2022 y "grado" son juicio analítico [I]. La columna 2027 es proyección [I], no un compromiso de producto.

| ID | Proceso | 2021–2022 | Noviembre de 2026 | Proyección 2027 | Tipo de cambio | Grado |
|---|---|---|---|---|---|---|
| P8 | Triage de alertas | Analista de nivel 1 revisa una por una | Agentes clasifican y explican el veredicto; Microsoft afirma cerca del 80 % de una cola típica de Defender [MS-02] | El nivel 1 humano pasa a ser revisión por excepción | Transformado | Muy alto |
| P9 | Investigación | Correlación manual entre consolas | Agente reconstruye la historia del ataque, cronología, técnicas y entidades [MS-10] | Investigación preparada antes de que la persona abra el caso | Transformado | Alto |
| P7 | Ingeniería de detección | Reglas escritas a mano; ciclos de semanas | Agente identifica brechas de cobertura y propone reglas [MS-02, MS-10] | Detección como código generada por agentes, con aprobación humana | Transformado | Alto |
| P3 | Inteligencia de amenazas | Lectura manual de reportes | Agente extrae patrones e indicadores y los relaciona con el entorno [MS-10, MS-13] | Inteligencia que dispara protección sin pasar por una cola | Acelerado y transformado | Alto |
| P4 | Gestión de exposición | Ciclo mensual, fuera del SOC | Agente prioriza por riesgo real; protección previa al parche en Preview [MS-03, MS-10] | Hallazgo, protección y parche en un mismo flujo | Transformado y fusionado | Muy alto |
| P5 | Validación ofensiva | Ejercicios anuales o trimestrales | Agente de reconocimiento GA; pruebas de penetración web en Preview [MS-02, MS-10] | Validación continua que alimenta detección y remediación | Transformado | Alto |
| P6 | Datos y telemetría | Conectores a medida; el costo limita la visibilidad | Más de 500 conectores, lago de datos, retención de 90 días para datos de Defender elegibles [MS-04] | Normalización en la ingesta; datos preparados para agentes | Transformado | Alto |
| P11 | Contención y remediación | Playbooks SOAR con aprobación manual | Defensa autónoma integrada para amenazas de alta confianza; agentes recomiendan y piden aprobación [MS-05, MS-09] | Más acciones reversibles sin intervención; las irreversibles con aprobación | Acelerado | Medio a alto |
| P10 | Threat hunting | Hipótesis y consultas de expertos | Lenguaje natural a consultas; agentes que generan hipótesis en Preview [MS-24] | Hunting continuo por agentes | Acelerado | Medio a alto |
| P13 | Automatización | Playbooks estáticos | Playbooks que coordinan equipos de agentes hacia un resultado [MS-09] | La orquestación de agentes reemplaza gran parte del SOAR estático | Transformado | Alto |
| P1 | Gobierno y métricas | MTTA, MTTR, volumen | Se agregan métricas de agentes y de costo por consumo [MS-11] | Métricas de resultado: exposición cerrada, veredictos revertidos, costo por caso | Transformado | Medio a alto |
| P2 | Incidentes mayores y notificación | Informe armado a mano | Resúmenes y cronologías generados por IA; la decisión sigue siendo humana | Evidencia lista en horas; presión por decidir más rápido | Acelerado | Medio |
| P12 | Forense y malware | Especialistas | Asistencia para analizar scripts | Agentes de ingeniería inversa (Hoja de ruta, a validar) | Acelerado | Medio |
| P14 | Recuperación | Coordinación manual con TI | Planes de remediación que llegan a TI con contexto [MS-16] | Seguridad prioriza, TI aprueba y despliega en un mismo flujo | Acelerado | Medio |
| P15 | Lecciones aprendidas | Informe posterior | Los agentes aprenden de la retroalimentación del analista [MS-10] | Aprendizaje compartido entre agentes (Hoja de ruta, a validar) | Acelerado | Medio |
| P16 | Talento y turnos | Carrera por niveles | El nivel 1 se reduce como puerta de entrada | Supervisor de agentes, ingeniero de contexto, ingeniero de detección | Transformado | Alto |

**Lectura.**

- **Acelerados (mismo diseño):** P2, P10, P11, P12, P14, P15.
- **Transformados (cambia quién ejecuta o el diseño):** P1, P3, P4, P5, P6, P7, P8, P9, P13, P16.
- **Fusionados:** la gestión de exposición (P4) y la validación ofensiva (P5) entran al mismo ciclo que la detección y la respuesta [I, sobre MS-09].

### B.5 Procesos nuevos

| ID | Proceso nuevo | Origen | Por qué aparece | Respaldo |
|---|---|---|---|---|
| N1 | Detección y respuesta sobre sistemas de IA y agentes | IA en el ataque | Los agentes del negocio son insiders que pueden ser manipulados | MS-01, MS-03 |
| N2 | Inventario y postura de agentes | IA en el ataque | No se defiende lo que no se conoce | MS-01, CIS-01, NIST-05 |
| N3 | Protección previa al parche a velocidad de máquina | IA en el ataque | La ventana entre divulgación y explotación se redujo a alrededor de un día | MS-01, MS-03 |
| N4 | Defensa del propio SOC agéntico | IA en el ataque | Un agente del SOC puede ser atacado con inyección, alertas falsas o envenenamiento de memoria | CSA-01 |
| N5 | Gobierno y supervisión de agentes defensivos | IA en la defensa | Define qué agente puede hacer qué, aprueba, detiene y revisa | MS-09, MS-11 |
| N6 | Evaluación y aseguramiento de agentes | IA en la defensa | Mide precisión, tasa de reversión y deriva antes de ampliar autonomía | CSA-01, NIST-02 [I] |
| N7 | Ingeniería de contexto | IA en la defensa | Mantiene el conocimiento que usan los agentes: criticidad, excepciones, dependencias | MS-10, MS-11 |
| N8 | Gestión económica del SOC agéntico | IA en la defensa | Presupuesta y controla el consumo de IA frente a resultados | MS-11 |
| N9 | Seguridad de código asistida por agentes | IA en la defensa | Descubre y valida vulnerabilidades en repositorios | MS-17, MS-18 |
| N10 | Respuesta a incidentes sobre agentes del negocio y sus fuentes de conocimiento | Agregado tras el caso Zava [R] | Suspender, preservar, restaurar a una versión conocida, revisar respuestas emitidas y revalidar antes de reactivar | LAB-14, EXT-09 |

N4 y N6 son los que menos aparecen en el mensaje de producto y los que más importan para un regulador financiero [I].

### B.6 Cómo opera un SOC agéntico

#### B.6.1 El modelo según Microsoft

- **Definición.** Un modelo operativo que pasa de reaccionar a incidentes a anticipar cómo se mueve el atacante y modificar el entorno para cortarle el camino [E: MS-05].
- **Tres etapas de madurez.** Unificar la plataforma, acelerar con IA generativa y agentes de tarea, y desplegar automatización agéntica [E: MS-05, MS-06].
- **Tres equipos de agentes en ciclo cerrado.** Rojos encuentran y validan caminos de compromiso; azules clasifican, investigan y convierten inteligencia en detecciones; verdes priorizan exposición y coordinan la remediación [E: MS-02, MS-09].
- **Playbooks orientados a resultados.** Asignan objetivos a un equipo de agentes; pueden iniciarse a mano, por chat o por reglas [E: MS-09].
- **Personas en control.** Mínimo privilegio, aprobación antes de acciones críticas y registro auditable de cada acción [E: MS-09, MS-11].
- **Razonar y actuar son funciones distintas.** Los agentes razonan y las capacidades de la plataforma actúan [E: INT-11]. El análisis en tiempo de máquina es trabajo de agentes; la respuesta en tiempo de máquina es sobre todo interrupción automática [I].

#### B.6.2 Cómo cambia el trabajo diario [I]

| Antes | En el SOC agéntico |
|---|---|
| El analista abre una alerta y empieza a reunir datos | El analista abre un caso con veredicto, cronología y acciones sugeridas |
| Tres niveles que se pasan el caso | Agentes que comparten contexto; personas que deciden en puntos definidos |
| Se mide volumen atendido | Se mide resultado: exposición cerrada, tiempo de permanencia del atacante |
| El rojo entrega un informe; el azul lo lee semanas después | El hallazgo del rojo genera una detección y una remediación en el mismo flujo |
| El conocimiento está en las personas | El conocimiento también está en el contexto que usan los agentes y hay que mantenerlo |

#### B.6.3 Flujo de ocho etapas [R]

El tablero evaluado en el turno 6 (Intake, Triage, Escalation, Resolution, Closure) es un flujo de mesa de ayuda: lineal, sin etapa de contención y con la investigación después del escalamiento. El módulo 5 del workshop AI-Powered SOC llama a ese modelo "el SOC de ayer" [E: INT-12]. NIST SP 800-61 Rev. 3 organiza la respuesta en detectar, responder y recuperar, con mejora continua [E: NIST-07].

| Etapa | Qué incluye | Procesos | Qué corrige del tablero |
|---|---|---|---|
| 1. Preparar (continuo) | Inventario y criticidad de activos y agentes, telemetría, playbooks, política de autonomía | N2, N7, P6 | El tablero no tenía preparación; la IA no compensa telemetría faltante [INT-10] |
| 2. Detectar y correlacionar | Señales convertidas en un caso unificado; severidad ajustada por activo | P6, P7 | Reemplaza "Intake": los casos nacen de señales, no de un reporte |
| 3. Interrumpir y contener | Acciones reversibles a velocidad de máquina, en paralelo a la investigación | P11 | Etapa ausente en el tablero. Para AiTM, la interrupción automática deshabilita la cuenta y revoca la cookie de sesión [MS-27] |
| 4. Triage en dos modos | Resuelto por agentes con revisión, o asistido para una persona | P8 | Separa lo que el modelo de siete fases del workshop también separa [INT-10] |
| 5. Investigar y hacer hunting | Alcance, otras entidades afectadas, persistencia | P9, P10 | En el tablero, la investigación venía después del escalamiento |
| 6. Expulsar y remediar | Rotar credenciales, retirar persistencia, restaurar fuentes | P11, N10 | Precisa la nota de "limpieza de datos": lo envenenado es la base de conocimiento, no el entrenamiento [EXT-08] |
| 7. Recuperar y validar | Restaurar la confianza en identidad, dispositivo y agente; poder deshacer acciones automáticas | P14 | Etapa ausente en el tablero [INT-13] |
| 8. Mejorar y gobernar | Detecciones nuevas, revisión de eficacia de agentes, ajuste de la política | P7, P15, N5, N6 | Amplía "Closure" |
| Transversal | Escalamiento, evidencia (incluida la traza del agente) y comunicación al negocio | P2, P12 | El escalamiento pasa de etapa a decisión; lo dispara la correlación entre capas, no la severidad de cada alerta |

#### B.6.4 Casos de uso: qué ya está agentificado y qué sigue

| Estado | Casos de uso |
|---|---|
| **Ya agentificados (GA o uso extendido)** | Triage de phishing reportado por usuarios; triage de alertas de Defender; investigación y reconstrucción de ataques; extracción de inteligencia e informes adaptados; creación de detecciones a partir de inteligencia; reconocimiento de caminos de ataque; priorización de postura |
| **En agentificación (Preview)** | Triage de alertas de identidad y nube; pruebas de penetración de aplicaciones web; reducción de riesgo con protección previa al parche; hunting con generación de hipótesis; detección dinámica de amenazas; triage de alertas de DLP y riesgo interno; remediación de vulnerabilidades desde Intune; señales de terceros |
| **Próximos (Hoja de ruta o proyección)** | Agentes de hunting e ingeniería inversa; aprendizaje compartido entre agentes; gestión de exposición integrada; correcciones propuestas como cambios de código; normalización de datos en la ingesta |
| **Sin agentificar, y conviene que siga así [R]** | Determinación de materialidad; decisión de divulgar; declaración de crisis; acciones irreversibles sobre sistemas críticos u OT; aceptación de riesgo |

Las dos primeras filas se apoyan en MS-02, MS-03, MS-10, MS-12, MS-16, MS-23 y MS-24. La fila "próximos" incluye elementos de hoja de ruta tomados de recaps internos [INT-02, INT-03] que no se confirmaron en una fuente pública escrita. Como referencia externa, la guía de CSA organiza los agentes de seguridad en cuatro patrones: automatización del SOC, gestión de vulnerabilidades, hunting y respuesta a incidentes [E: CSA-01].

### B.7 Narrativas de ataque

#### B.7.1 Qué dicen hoy los marcos de MITRE

- **ATT&CK ya cubre IA.** La versión 20 (13-oct-2026) agregó técnicas de IA y dos campañas asistidas por IA [E: MITRE-03]: inyección directa e indirecta de instrucciones, exfiltración mediante agentes, envenenamiento de resultados de IA y sabotaje de defensas autónomas [E: EXT-14, fuente secundaria].
- **"Fuentes de datos" ya no existe en ATT&CK.** Desde la versión 18 se reemplazó por estrategias de detección, analíticas y componentes de datos [E: MITRE-04].
- **ATLAS ya modela al atacante autónomo.** En agosto de 2026 sumó reconocimiento autónomo, orquestación autónoma del ataque y comunicación entre agentes [E: MITRE-02].
- **El módulo 3 del workshop quedó atrás.** Todavía dice que ATT&CK tiene 14 tácticas y no cubre inyección de instrucciones, y sus cifras de ATLAS (167 técnicas, 57 casos) son anteriores a las que muestra hoy el sitio (221 y 77) [E: INT-11, MITRE-01].

#### B.7.2 Las trece narrativas previas y qué les agregó la IA

El catálogo es una síntesis propia sobre los capítulos del Microsoft Digital Defense Report 2026 [E: MS-47]. El grado es juicio propio [I].

| # | Narrativa previa | Qué le agregó la IA | Grado |
|---|---|---|---|
| 1 | Phishing y robo de credenciales o de sesión | Señuelos personalizados a escala. El 44,6 % de las técnicas de phishing ya son AiTM [INT-16]; los kits usan IA para personalizar [INT-11] | Alto |
| 2 | Fraude por correo y de pagos (BEC) | Análisis del buzón robado para elegir a quién suplantar [MS-41]. Más de 46 millones de ataques de suplantación detectados [MS-46] | Alto |
| 3 | Ingeniería social por voz y mesa de ayuda | Servicios criminales con agentes de voz que hacen vishing y roban códigos de un solo uso [EXT-19]. Segundo vector inicial en 2025 según Mandiant, citado por un tercero [EXT-22] | Alto |
| 4 | Ransomware y extorsión de datos | Acelerador, no reemplazo; 275 % más de datos robados [EXT-20]. Primer caso de extorsión automatizada, JADEPUFFER [INT-16] | Medio a alto |
| 5 | Explotación de servicios expuestos y dispositivos de borde | Casi 40.000 CVE en el primer semestre [MS-44]; cargas expuestas atacadas en 5,3 horas [MS-46] | Alto |
| 6 | Malware común, infostealers y ejecución por el usuario | Malware a medida generado con IA [INT-14]. Marco ofensivo de 88.000 líneas en menos de una semana [EXT-19]. No se encontró IA en ClickFix | Medio |
| 7 | Espionaje de actores estatales | Agentes que ejecutan la intrusión. El resto sigue sin IA: abuso de OAuth y repetición de tokens [INT-15] | Alto |
| 8 | Cadena de suministro de software y SaaS | Herramientas de IA para desarrolladores secuestradas: unos 2.000 secretos de 225 víctimas [INT-16]. El 19,7 % de los paquetes recomendados por modelos no existía [EXT-23] | Medio |
| 9 | Amenaza interna | Identidades fabricadas para ser contratado y sostener el acceso [EXT-18, INT-11] | Alto, solo en contratación fraudulenta |
| 10 | Compromiso de nube e identidades de carga de trabajo | El recurso robado ahora es capacidad de IA [MS-45] | Medio |
| 11 | OT e infraestructura crítica | Un caso asistido por IA que llegó a una empresa de agua [EXT-13]. El ataque destructivo al sector eléctrico polaco entró por dispositivos de borde, sin IA mencionada [INT-15] | Bajo |
| 12 | Abuso automatizado de aplicaciones web | Resolución de CAPTCHA con IA, técnica nueva de ATT&CK v20 [MITRE-07]. Sin campaña documentada leída | Bajo a medio |
| 13 | Denegación de servicio | Solo lo afirma un blog universitario [EXT-24] | Sin evidencia sólida |

**Lo que no cambió.** Los objetivos (acceso, persistencia, robo de datos, fraude, espionaje, interrupción) [E: MS-44]; la puerta de entrada, con ejecución por el usuario (30 %) y cuentas válidas (20 %) a la cabeza [E: INT-16]; y quién dirige: en ransomware la IA es un multiplicador de los operadores, no un sustituto [E: EXT-21].

#### B.7.3 Las once narrativas del turno 8, con la clasificación corregida

En el turno 8 se presentaron como "nuevas". El turno 9 corrigió: cinco son previas enriquecidas, tres son previas con un blanco nuevo y solo tres no tienen antecedente. Las señales tempranas son inferencia propia salvo donde hay cita.

| # | Narrativa | Evidencia | Clasificación corregida | Señal temprana y fuente | Tiempo de máquina |
|---|---|---|---|---|---|
| 1 | Intrusión orquestada por agentes | GTG-1002: unas 30 entidades [MITRE-05], 80 a 90 % de la operación táctica por IA [EXT-11]. México: cruzó de TI a OT [EXT-13] | Previa enriquecida | Ritmo y paralelismo imposibles para una persona; correlación de red, identidad, endpoint y nube | Sí |
| 2 | Robo de sesión y fraude por correo industrializados | EvilTokens: más de 12.000 buzones en más de 10.000 organizaciones [MS-41] | Previa enriquecida | Token desde infraestructura nueva, reglas de bandeja, registro de dispositivo, reconocimiento por Graph [MS-41] | Sí |
| 3 | Explotación en menos de un día | Mediana entre descubrimiento y uso como arma muy por debajo de 24 horas [MS-44] | Previa enriquecida | Activo expuesto con vulnerabilidad recién divulgada | Sí, como protección previa al parche |
| 4 | Malware que consulta un modelo | PROMPTSTEAL y PROMPTFLUX según el módulo 3; fuente original sin verificar [INT-11] | Previa enriquecida | Proceso no esperado que llama a un servicio de modelos | En parte |
| 5 | Suplantación sintética | Trabajadores remotos con identidades fabricadas [MS-42]; fraude por videollamada de USD 25 millones [EXT-17, secundaria] | Previa enriquecida | Fuera del SOC: flujo de pagos, mesa de ayuda, verificación de identidad | No: verificación fuera de banda y doble control |
| 6 | Secuestro del agente por inyección indirecta | Caso de ATLAS en Copilot Studio [MITRE-02]; escenario del agente de tesorería [INT-11] | **Sin antecedente** | Instrucciones y respuestas, secuencias de herramientas, eventos de límite de permisos [INT-11] | Sí |
| 7 | Envenenamiento de memoria, contexto o base de conocimiento | OWASP ASI06 [EXT-10]; módulo 3 [INT-11] | **Sin antecedente** | Lecturas y escrituras de memoria [INT-11]; auditoría del almacenamiento de la fuente | No para detectar; sí para contener |
| 8 | Cadena de suministro agéntica | OWASP ASI04 [EXT-10]; extensiones que extraen conversaciones [INT-11] | Previa con blanco nuevo | Inventario de agentes y componentes; cambios en herramientas | En parte |
| 9 | Abuso de identidad del agente y fallas en cascada | OWASP ASI03, ASI07 y ASI08 [EXT-10]. Sin campaña pública; es un escenario [INT-11] | **Sin antecedente** | Comunicación entre agentes y cadena de planificación [INT-11] | Sí |
| 10 | Secuestro de capacidad de IA | LLMJacking en ATT&CK [MITRE-06]; caso de estudio de ATLAS [EXT-16] | Previa con blanco nuevo | Pico de consumo y acceso desde IP anónimas [INT-11] | En parte |
| 11 | Cegar o desviar la defensa autónoma | Subtécnica nueva de ATT&CK v20 dentro de "deshabilitar o modificar herramientas" [EXT-14, EXT-15]. Sin campaña documentada | Previa con blanco nuevo | Traza del agente del SOC comparada con muestreo humano | No: evaluación continua |

#### B.7.4 Cuándo hace falta un SOC agéntico [I]

Tres condiciones que deben darse juntas: el ciclo de decisión del atacante está automatizado, el daño ocurre en minutos y la contención es reversible. Las narrativas 1, 2, 3, 6 y 9 de la tabla anterior las cumplen. La 5 pide control de proceso, la 7 vigilancia de integridad y la 11 aseguramiento de los propios agentes del SOC.

El caso Zava encadena las narrativas 2, 7, 6 y 10. El informe v1.0 cubría bien la 1, la 2 y la 3; trataba la 6, la 7, la 9 y la 11 solo como procesos nuevos, y no contemplaba la 4, la 5, la 8 ni la 10.

### B.8 Fuentes de telemetría

**Regla general [I].** Las trece narrativas previas se detectan con la telemetría de siempre; lo que exigen ahora es correlación y velocidad. Las tres sin antecedente son las únicas que piden telemetría nueva, la del propio agente. El módulo 3 del workshop lista lo que hay que ver: instrucciones y respuestas, secuencias de herramientas, memoria, cadena de planificación, comunicación entre agentes y eventos de límite de permisos [E: INT-11].

#### B.8.1 Seis fuentes nuevas

Ninguna llega sola al SIEM: todas requieren habilitar un conector, un plan o una configuración.

| Fuente | Qué registra | Narrativas que cubre | Dónde se obtiene y qué hay que habilitar |
|---|---|---|---|
| Ejecución del agente | Instrucciones, sesiones, invocaciones de herramientas y MCP con argumentos y respuestas, errores | Secuestro del agente, abuso de herramientas, cascadas | Conector de Agent 365 hacia la tabla `UnifiedAgentObservability` de Sentinel [MS-53]. Los agentes de otras plataformas deben emitir telemetría con el SDK [MS-37] |
| Inventario y configuración de agentes | Agentes, herramientas, identidades, indicadores de riesgo | Cadena de suministro agéntica, agentes no autorizados | Tabla `AIAgentsInfo` en búsqueda avanzada [INT-11] y conector Microsoft Agent Identities [MS-57]. Requiere habilitar la seguridad para agentes en Defender [MS-51] |
| Alertas de protección de IA | Jailbreak, inyección, credenciales en respuestas, acceso desde IP anónimas, abuso de consumo | Secuestro del agente, secuestro de capacidad de IA | Defender for Cloud hacia `SecurityAlert` [INT-11]. Hay que activar el plan y validar que las alertas lleguen a Sentinel [MS-54] |
| Diagnóstico del servicio de modelos | Auditoría, solicitudes y respuestas, uso | Secuestro de capacidad de IA | Configuración de diagnóstico de Foundry hacia Log Analytics; hay que crearla [MS-59] |
| Auditoría de Copilot y apps de IA | Quién interactuó, cuándo, en qué app y qué recursos leyó Copilot | Inyección indirecta sobre Copilot, exfiltración | Auditoría de Purview, activa por defecto en organizaciones empresariales [MS-50]. Las apps de IA de terceros se facturan por consumo [MS-48]. A Sentinel llega con el conector de Copilot, tabla `CopilotActivity` [MS-53] |
| Agentes locales en equipos | Agentes de IA descubiertos en endpoints y su comportamiento | Cadena de suministro agéntica, inyección sobre agentes locales | Defender for Endpoint en modo activo; se incorporan aparte de los agentes de nube [MS-37] |

#### B.8.2 Fuentes tradicionales que hay que ampliar

- **Entra:** inicios de sesión y auditoría de identidades de agente, que se distinguen por la propiedad `agentType` [E: MS-58]. Sin estos conectores, las amenazas de identidad sobre agentes no generan señal en Sentinel [E: MS-54].
- **Almacenamiento y SharePoint:** escrituras en las fuentes de conocimiento, asociadas al agente que las consume [I, del caso Zava].
- **Endpoint y salida de red:** procesos no esperados que llaman a servicios de modelos [I].
- **Fuera del SOC:** flujo de pagos, mesa de ayuda y contratación, para la suplantación sintética [I].

#### B.8.3 Señales sin fuente identificada

- **Memoria del agente.** Los almacenes de estado quedan fuera del alcance del SIEM [E: INT-11]. En Microsoft 365 Copilot las memorias se guardan como contactos en una carpeta oculta del buzón y no las preserva una retención legal [E: MS-49].
- **Planificación y comunicación entre agentes.** Agent 365 modela cada ejecución como un árbol de pasos: invocación, llamada al modelo, llamada a herramienta, respuesta [E: MS-56]. No se verificó si incluye el razonamiento intermedio ni los mensajes entre agentes [D].
- **Agentes del propio SOC.** Security Copilot está incluido en la auditoría estándar de Purview [E: MS-48]. No se verificó dónde queda la traza de Perception [D].

#### B.8.4 Tres advertencias

- **Texto de las instrucciones.** El registro de auditoría de Copilot no lo contiene; se recupera con eDiscovery, según una fuente de terceros [E: EXT-25]. En las alertas de Defender, la evidencia de instrucciones es una configuración opcional [E: MS-37].
- **Retención.** Log Analytics conserva 30 días por defecto [E: MS-52]. Para un envenenamiento lento es poco.
- **Estado y licencias.** El conector de Agent 365 se anunció en Preview en mayo de 2026 [E: MS-55] y la detección de amenazas sobre agentes figura en Preview [E: MS-37]. El módulo 3 lista licencias de Agent 365 como requisito [E: INT-11]. No se verificó el estado actual de cada una [D].

### B.9 Caso Zava: el ataque de 75 minutos

Caso del laboratorio del módulo 3 del TechWorkshop L400 "Using AI to Secure the Modern SOC". El repositorio se declara como primer borrador, con navegación, consultas y entidades ilustrativas [E: LAB-01]. Los nombres de entidades son del laboratorio, no de un incidente real.

#### B.9.1 La cadena

| Etapa | Momento | Capa | Qué ocurrió | Entidad principal |
|---|---|---|---|---|
| 1 | T+0 | Identidad | Phishing con intermediario (AiTM) roba el token de sesión; inicio de sesión desde una IP anónima | Mariya Petrova; 102.89.42.17 |
| 2 | T+16 min | Datos y grounding | Documento envenenado de "actualización de política" en la fuente de conocimiento del Refund Agent | trusted-report.docx |
| 3 | T+34 min | IA | Intentos de inyección de instrucciones y jailbreak, bloqueados por Prompt Shields | Refund Agent (oai-soclab-v02) |
| 4 | T+52 min | Infraestructura | La entidad de servicio del agente hace solicitudes anómalas hacia la inferencia con GPU | sp-refund-agent-inference |
| 5 | T+69 min | Endpoint | PowerShell codificado que actúa como baliza | update_check.ps1 en OPS-LT-0427 |

Fuente: LAB-04, LAB-07, LAB-15.

#### B.9.2 ¿Estaba contemplado en el informe v1.0?

Parcialmente. Los procesos que el ataque pone a prueba estaban; el escenario de un agente del negocio usado como paso intermedio, no.

| Etapa | En el informe v1.0 | Estado |
|---|---|---|
| 1. Identidad | P8, P9, P11; fila "deshabilitar cuenta de usuario" de la matriz de autonomía | Cubierto |
| 2. Envenenamiento de la base de conocimiento | N4 trataba el envenenamiento de memoria, pero de los agentes del propio SOC | Parcial |
| 3. Inyección y jailbreak contra el agente | N1; el mapa de tecnologías no incluía la protección de IA de Defender for Cloud | Parcial |
| 4. Infraestructura de inferencia | No aparecía | No cubierto |
| 5. Endpoint | P9, P11, P12 | Cubierto |
| Correlación, falla de detección, autonomía, impacto de negocio | Cubiertos como principio o proceso; la matriz de autonomía no tenía filas para acciones sobre agentes | Cubierto con vacíos |

#### B.9.3 Qué queda probado y qué no

| Queda probado | No queda probado con los datos del laboratorio |
|---|---|
| Que cada uno de los cinco eventos existe en la telemetría | **Los intervalos.** Los eventos sembrados comparten una sola marca de tiempo; el orden sale de un campo de etapa [LAB-07]. Los valores T+ son parte del guion [LAB-15] |
| El orden lógico de las etapas | **Que sea un mismo actor.** El vínculo se infiere por entidades y secuencia [I] |
| Que la capa de IA generó una alerta real de Defender for Cloud, consultable en `SecurityAlert`, y que quedó sin correlacionar [LAB-07, LAB-09] | **Que el documento haya influido en alguna respuesta del agente.** Es riesgo residual abierto [LAB-14] |
| Que la identidad comprometida y la entidad de servicio muestran actividad anómala desde una segunda vista [LAB-08] | **Cómo llegó el script al equipo** y **que el ataque haya sido conducido por IA** |

En un incidente real, la primera tarea de prueba sería reemplazar el orden lógico por marcas de tiempo de origen. Sin eso, la cifra de 75 minutos no se puede defender ante un auditor [I].

**Consultas de partida.** Usan solo nombres confirmados por las fuentes: la tabla y el campo de etapa del laboratorio, y el esquema estándar de `SecurityAlert`. No se ejecutaron. El tipo de alerta de jailbreak bloqueado por Prompt Shields es `AI.Azure_Jailbreak.ContentFiltering.BlockedAttempt` [E: MS-30].

```kusto
// Etapas 1, 2, 4 y 5: eventos sembrados, ordenados por etapa y no por reloj
SocLabEvents_CL
| where isnotempty(Stage_s)
| sort by Stage_s asc
```

```kusto
// Etapa 3: alerta nativa de Defender for Cloud para servicios de IA
SecurityAlert
| where AlertType startswith "AI.Azure_"
| project TimeGenerated, AlertName, AlertSeverity, AlertType,
          CompromisedEntity, Entities, ExtendedProperties
```

#### B.9.4 Por qué falló la detección

**Lo que establece el laboratorio [E].**

| Causa | Detalle | Fuente |
|---|---|---|
| Fragmentación | En producción, las cinco señales llegan como alertas separadas de cinco productos, cada una en su consola | LAB-06 |
| Severidad individual baja | Cada etapa, vista sola, es baja o informativa; la cadena es un único incidente de severidad media entre señuelos | LAB-06, LAB-16, LAB-17 |
| Ruido | Unos 25 incidentes señuelo: inicios de sesión de riesgo rutinarios, coincidencias benignas de DLP, malware común | LAB-04 |
| Sin correlación entre capas | En todas las etapas hubo señal y nada la unió; la alerta de IA nunca se asoció a las demás | LAB-09 |
| Respuesta manual | Lo que se llegó a ver se atendió herramienta por herramienta, más lento que el atacante | LAB-16, LAB-17 |
| Diseño preventivo | La base de conocimiento confiaba en cualquier carga autenticada; el agente trataba su fuente como autoridad; la entidad de servicio tenía más alcance del necesario | LAB-10 |

**Causas de fondo [I].**

1. **La correlación trabaja sobre alertas, y varias señales eran solo eventos.** El portal de Defender agrupa en incidentes las alertas que recibe; cuando hay varios espacios de trabajo de Sentinel, solo las alertas del principal se correlacionan con las de Defender [E: MS-35].
2. **Las cinco señales no comparten una entidad.** La correlación se apoya, entre otras cosas, en entidades comunes, tiempo y comportamiento de ataque [E: MS-36]. El salto del usuario al documento está en la telemetría; el del documento al agente y el del agente a su identidad de inferencia dependen de un mapa de dependencias que no existe en ningún registro.
3. **La severidad no tiene en cuenta el activo.** Un inicio de sesión desde una IP anónima es rutina; en una cuenta que puede escribir en la fuente de un agente que decide reembolsos, no.
4. **"Bloqueado" se lee como "resuelto".** El bloqueo de la inyección directa no dice nada del documento ya cargado. En Foundry, la detección de ataques en documentos está desactivada por defecto [E: MS-31]. El caso no indica cómo estaba configurada [D].
5. **La señal de la etapa 1 estaba disponible en tiempo real.** La detección de IP anónima se evalúa durante el inicio de sesión [E: MS-33] y las políticas basadas en riesgo pueden exigir controles en ese momento [E: MS-34].

La guía del Zero Trust Workshop de Microsoft describe el mismo patrón: cuando Sentinel y Defender XDR operan por separado, el SOC ve incidentes distintos en dos consolas [E: MS-40].

#### B.9.5 La respuesta que debió dispararse

| Momento | Disparador | Acción | Modo | Reversible |
|---|---|---|---|---|
| T+0 | Riesgo del inicio de sesión evaluado en tiempo real | Bloquear o forzar reautenticación con Acceso Condicional basado en riesgo | Política automática [R] | Sí |
| T+0 en adelante | Usuario marcado en riesgo | Revocar las sesiones y aplicar la política de reautenticación | Autónomo [E: LAB-13] | Sí |
| T+16 | Escritura en la fuente de conocimiento desde una identidad en riesgo | Poner el documento en cuarentena y congelar nuevas escrituras | Autónomo [E: LAB-13] | Sí |
| T+16 | Mismo disparador | Purgar el correo de origen en otros buzones y bloquear al remitente | [R]; no figura en los pasos del laboratorio | Sí |
| T+34 | Alerta de IA sobre el mismo agente | Unir la alerta al caso, subir la severidad y abrir la revisión de respuestas del agente desde T+16 | Automático [R] | No aplica |
| T+52 | Actividad anómala de la entidad de servicio | Deshabilitar la entidad de servicio y rotar sus credenciales | En el laboratorio es contención de identidad [E: LAB-11]; en la matriz propia requiere aprobación [D] | Parcial: detiene al agente |
| T+52 | Mismo disparador | Restringir el recurso de Azure OpenAI | Con aprobación humana [E: LAB-13] | Interrumpe un servicio en producción |
| T+69 | Ejecución del script | Aislar el equipo y preservar el script | [R]; no figura entre los pasos del laboratorio | Sí |

El laboratorio lo operacionaliza con un playbook de Logic Apps asociado a una regla de automatización de Sentinel, con una compuerta de aprobación para la acción de mayor impacto [E: LAB-12]. Clasifica cada acción por reversibilidad e impacto de negocio [E: LAB-13], los mismos dos primeros criterios del modelo de autonomía de B.12.

**Contrafactual [I].**

- Con el control de la etapa 1, la cadena se corta en T+0.
- Sin ese control pero con correlación, el primer momento en que dos señales comparten una entidad es T+16. Dos acciones reversibles cortan ahí el acceso y retiran el documento: la ventana del atacante baja de unos 75 minutos a 16 como máximo, más la latencia de ejecución.
- La evaluación continua de acceso admite hasta 15 minutos de latencia y se centra en Exchange, Teams y SharePoint [E: MS-32].
- Para AiTM, la interrupción automática deshabilita la cuenta y revoca la cookie de sesión robada [E: MS-27]; actúa sobre señales correlacionadas con alta confianza [E: MS-28]. El caso no explica por qué no actuó.

#### B.9.6 Riesgo residual

| Riesgo | Por qué sigue abierto | Siguiente paso [R] |
|---|---|---|
| Efecto del documento sobre respuestas ya emitidas | La cuarentena evita respuestas futuras; lo producido en la ventana no está acotado [LAB-14] | Revisar las interacciones del agente desde T+16; el dueño del negocio decide si se revierten |
| Persistencia de acceso | No está probado que el atacante no haya dejado otro método de MFA, un consentimiento o un token [LAB-14] | Hunting sobre cambios de autenticación y consentimientos |
| Exposición de datos | No está confirmado si hubo exfiltración [LAB-14] | Revisar accesos al contenedor y respuestas del agente |
| Origen de la etapa 5 | No se pudo establecer el vector | Analizar el script y el árbol de procesos |

Para restaurar la fuente, una guía de controles sobre la entrada ASI06 de OWASP pide instantáneas, control de versiones y vencimiento de la memoria no verificada [E: EXT-09, fuente secundaria].

### B.10 Tecnología Microsoft

#### B.10.1 Las piezas

| Capa | Tecnología | Papel |
|---|---|---|
| Señales, sensores y actuadores | Microsoft Defender (endpoint, identidad, correo, nube, aplicaciones), Entra, Intune, Purview | Ven y actúan |
| Contexto | Microsoft Sentinel (lago de datos, grafo, más de 500 conectores) dentro de ISOC en el portal de Defender | Convierte señales en comprensión compartida para personas y agentes |
| Agentes, orquestación y modelos | Microsoft Perception (agentes rojos, azules y verdes; playbooks; modelos MAI-Cyber) y agentes de Security Copilot | Razonan y ejecutan |
| Extensión | API y MCP de Perception (Preview), servidor MCP de Sentinel (Preview), creador de agentes de Security Copilot, Copilot Studio, Logic Apps | Agentes propios e integración con SIEM, SOAR e ITSM existentes |
| Gobierno de agentes del negocio | Agent 365, Entra Agent ID, Acceso Condicional para agentes | Inventario, identidad y control de los agentes que el SOC debe vigilar |

Fuentes: MS-01, MS-02, MS-03, MS-04, MS-07, MS-19. Las tres capas del "cyber stack" son la formulación de Microsoft [E: MS-01, MS-07].

#### B.10.2 Mapa por proceso

| Proceso | Agente o capacidad Microsoft | Estado | Cómo se agentifica | Control humano |
|---|---|---|---|---|
| P8 Triage | Triage Agent (Perception) | GA | Clasifica alertas y explica el razonamiento; aprende de la retroalimentación | Revisión de veredictos |
| P8 Triage | Security Alert Triage Agent (Security Copilot) | GA para phishing; identidad y nube en Preview según la última información disponible | Triage de correos reportados y de un subconjunto de alertas | Ídem |
| P9 Investigación | Attack Investigation Agent (Perception) | GA | Correlaciona alertas, incidentes y señales; entrega veredicto, cronología, técnicas, indicadores y entidades | La persona valida y decide la respuesta |
| P3 Inteligencia | Threat Intelligence Agent (Perception) | GA | Extrae patrones e indicadores de un reporte | Selección de fuentes |
| P3 Inteligencia | Threat Intelligence Briefing Agent (Security Copilot) | GA | Informe periódico adaptado al entorno | Lectura y priorización |
| P7 Detección | Detection Authoring Agent y playbook de amenazas emergentes (Perception) | GA | Identifica brechas de cobertura y redacta reglas | Aprobación antes de desplegar |
| P7 Detección | Dynamic Threat Detection Agent (Security Copilot) | Preview según la última información disponible | Correlaciona telemetría y emite alertas con explicación | Revisión de alertas |
| P10 Hunting | Threat Hunting Agent (Security Copilot) | Preview según la última información disponible | Lenguaje natural a consultas, hunting guiado | La persona formula la hipótesis |
| P5 Validación ofensiva | Recon Agent (Perception) | GA | Mapea caminos de ataque, activos valiosos, configuraciones débiles | Definición de alcance |
| P5 Validación ofensiva | Web App Pen Test Agent (Perception) | Preview | Prueba aplicaciones web autorizadas y demuestra qué es explotable | Autorización explícita del objetivo |
| P4 Exposición | Posture Prioritization Agent (Perception) | GA | Ordena problemas de postura por riesgo real | Decisión de qué remediar |
| P4 Exposición | Risk Reduction Agent y protección previa al parche (Defender) | Preview | Despliega el parche con Intune si existe o aplica una protección temporal | Aprobación del plan |
| P4 Exposición | Identity Risk Reduction Agent (Perception); Conditional Access Optimization Agent (Entra) | Verificar estado en Learn | Propone cambios de Acceso Condicional | El administrador aprueba |
| P14 Recuperación | Vulnerability Remediation Agent (Intune) | Verificar estado en Learn | Planes de reducción listos para aprobar | TI aprueba el cambio |
| P6 Datos | Connector Builder Agent en VS Code (Sentinel) | GA prevista para fin de noviembre de 2026 | Asiste en la construcción de conectores | Revisión del conector |
| P6 Datos | Normalización en la ingesta (Sentinel) | Preview desde diciembre de 2026 | Estandariza los datos al ingresarlos | Gestión de analizadores |
| P11 Contención | Interrupción automática de ataques (Defender); playbooks de Perception | GA la defensa integrada; acciones de agentes con aprobación | Aísla dispositivos y bloquea cuentas ante señales de alta confianza | Aprobación de acciones de alto impacto |
| N1 Agentes como insiders | Protección en ejecución de agentes locales en Windows (Defender); Dynamic Agent Risk (Agent 365) | Verificar en Learn; Dynamic Agent Risk en Preview | Vigila el comportamiento de agentes y calcula un riesgo por agente | Política de contención |
| N2 Inventario | Agent 365 con Entra Agent ID; inventario de agentes en Defender | Verificar por capacidad | Descubre agentes y les asigna identidad gobernable | Asignación de dueño |
| N9 Código | Codename MDASH con modelos MAI-Cyber | Preview | Busca y valida vulnerabilidades en repositorios | Revisión de hallazgos |
| Datos sensibles | Data Security Triage Agent y Data Security Posture Agent (Purview) | Preview según la última información disponible | Triage de alertas de DLP y riesgo interno | Revisión del analista de datos |
| Casos propios | Creador de agentes de Security Copilot, Copilot Studio o Logic Apps con el servidor MCP de Sentinel; API y MCP de Perception | Preview en los componentes MCP | Agentes a medida que consultan datos de Sentinel o inician playbooks | Diseño, pruebas y dueño a cargo del cliente |

Fuentes principales: MS-02, MS-03, MS-04, MS-10, MS-12, MS-15, MS-16, MS-18, MS-19, MS-23, MS-24.

**Filas agregadas tras el caso Zava y el turno 10.**

| Proceso | Capacidad Microsoft | Estado | Aporte | Fuente |
|---|---|---|---|---|
| N1 | Protección contra amenazas para servicios de IA (Defender for Cloud) | GA | Alertas de jailbreak, fuga de datos y robo de credenciales, correlacionadas en Defender XDR | MS-29 |
| N1 | Detección de amenazas sobre agentes en Defender | Preview; agentes administrados con Agent 365 | Detecta comportamiento malicioso de agentes y permite investigar causa y alcance | MS-37 |
| N1 e identidad | Riesgo de identidades de carga de trabajo (Entra ID Protection) | No cubre identidades administradas; el acceso basado en riesgo requiere Workload Identities Premium | Señal sobre la identidad con la que actúa el agente | MS-38 |
| P6 | Conector de Agent 365 y conector Microsoft Agent Identities para Sentinel | Preview (anunciado en mayo de 2026) | Telemetría de ejecución e inventario de agentes en el lago de datos | MS-55, MS-57 |

#### B.10.3 Lo que este mapa no garantiza

- **Las cifras de eficacia son de Microsoft.** El 80 % de la cola es una cifra agregada propia, no una tasa garantizada por cliente [E: MS-02, EXT-01].
- **El costo es por consumo.** No hay en las fuentes revisadas un precio de referencia por caso [E: MS-11].
- **La elegibilidad de ISOC depende de la licencia.** Desde el 17-nov-2026 pueden optar los clientes de Sentinel con Microsoft 365 E5, E7 o Defender Suite [E: MS-04].
- **La cobertura fuera de Microsoft está empezando.** Las señales de AWS, Okta y Salesforce para los agentes son recientes [E: MS-02].
- **No se encontró evidencia sobre cobertura de agentes en entornos OT** [D].
- **Activar una capacidad no equivale a operarla con madurez ni a cumplir una norma** [I].

### B.11 Postura de Microsoft y comparación con los marcos

#### B.11.1 Postura y mensaje de Microsoft

| # | Mensaje | Fuente |
|---|---|---|
| 1 | "La física de la ciberseguridad está cambiando": la IA amplifica el riesgo, los ataques se automatizan y los agentes son los nuevos insiders | MS-01 |
| 2 | Hace falta un nuevo "cyber stack" para combatir IA con IA, en tres capas | MS-01, MS-07 |
| 3 | Tres resultados: asegurar los fundamentos, defender con agentes, asegurar a los agentes como insiders | MS-01 |
| 4 | El SOC agéntico es un modelo operativo, no una herramienta | MS-05 |
| 5 | La base es la unificación de SIEM y protección contra amenazas (ISOC en Defender) | MS-07, MS-03 |
| 6 | Agentes rojos, azules y verdes en ciclo cerrado, coordinados por playbooks | MS-02, MS-09 |
| 7 | Las personas mantienen el control: fijan límites y aprueban acciones de alto impacto | MS-09, MS-11 |
| 8 | Apertura: señales de terceros y acceso por API y MCP | MS-02 |
| 9 | Modelos propios especializados en seguridad para bajar el costo de operar agentes | MS-17 |

**Evolución del mensaje [I].** 2023–2024: un copiloto que asiste al analista. 2025: agentes de tarea dentro de cada producto. Abril de 2026: el SOC agéntico como modelo operativo. Julio a noviembre de 2026: un sistema de agentes coordinados sobre una plataforma unificada, ya disponible. La palabra que cambia es "asistir" por "actuar".

#### B.11.2 Qué dice cada marco

| Organismo | Publicaciones relevantes | Madurez | Qué aporta al SOC agéntico |
|---|---|---|---|
| **NIST** | SP 800-61 Rev. 3 (abr-2025) [NIST-01] | Final | Integra la respuesta a incidentes en toda la gestión de riesgo. No trata agentes |
| **NIST** | IR 8596, Cyber AI Profile (dic-2025) [NIST-02] | Borrador preliminar | Tres áreas: asegurar los sistemas de IA, defender con IA, frustrar ataques con IA |
| **NIST** | Overlays de SP 800-53 para sistemas de IA [NIST-04]; AI Agent Standards Initiative [NIST-05] | En desarrollo | Controles e identidad y autorización de agentes |
| **CSA** | Agentic Cybersecurity Implementation Guide (mar-2026) [CSA-01] | Borrador | Cuatro patrones con límites de confianza, alcance de permisos, prevención de manipulación, supervisión humana y manejo de fallas |
| **CSA** | MAESTRO, IAM para agentes, diseño seguro por rasgos, programa "Securing the Agentic Control Plane" [CSA-02, CSA-03, CSA-04] | Publicados y en expansión | Modelado de amenazas y controles para agentes |
| **CIS** | AI Agents Companion Guide para CIS Controls v8.1 (abr-2026) [CIS-01]; AI Security Guidance Workbook v8.1.2 [CIS-02] | Publicados | Aplica los controles a la capa de agentes. No propone un modelo operativo de SOC |
| **The Open Group** | Zero Trust Commandments, Zero Trust Reference Model (snapshot), Open FAIR, O-ISM3 [TOG-01, TOG-02, TOG-03, EXT-07]; borrador S252 de roles y glosario [INT-06] | Estándares publicados; modelos en borrador | Principios, roles y cuantificación de riesgo. No se encontró una publicación oficial sobre IA o agentes en operaciones |
| **MITRE** | ATT&CK v20 [MITRE-03]; ATLAS [MITRE-01, MITRE-02] | Publicados, en actualización continua | Técnicas y campañas de IA; atacante autónomo modelado |
| **OWASP** | Top 10 for Agentic Applications 2026 [OWASP-01] | Publicado | Lista de riesgos de agentes (ASI01 a ASI10) |

#### B.11.3 Puntos en común

| # | Coincidencia | Microsoft | NIST | CSA | CIS | Open Group |
|---|---|---|---|---|---|---|
| 1 | Supervisión humana sobre acciones de alto impacto | Aprobaciones y límites | Requisito constante del perfil | Requisitos por patrón | Capa de aplicación de políticas e interruptor de parada | Responsabilidad alineada al negocio |
| 2 | El agente es una identidad con mínimo privilegio | Entra Agent ID | Documento de identidad y autorización | IAM para agentes | Control de acceso aplicado a agentes | Principios Zero Trust |
| 3 | Fundamentos primero | "Asegurar los fundamentos" | Prácticas conocidas extendidas a IA | Controles base | Esencia de los CIS Controls | Principios de arquitectura |
| 4 | Doble mirada: asegurar la IA y defender con IA | Asegurar agentes y defender con agentes | Asegurar, defender, frustrar | Riesgo bidireccional | Asegurar la capa de agentes | Sin tratamiento específico |
| 5 | Registro y auditabilidad de lo que hace el agente | Acciones registradas | Registro extendido a activos de IA | Auditabilidad como condición | Traza de acciones del agente | Sin tratamiento específico |
| 6 | Inventario de sistemas de IA y agentes | Descubrimiento de agentes | Función Identificar | Registro de agentes | Inventario como primer control | Sin tratamiento específico |
| 7 | Respuesta a incidentes integrada con la gestión de riesgo | Ciclo rojo, azul y verde | SP 800-61 Rev. 3 | Patrones conectados | Control de respuesta a incidentes | Open FAIR para cuantificar |

La correspondencia entre los tres resultados de Microsoft y las tres áreas de NIST es una lectura propia [I].

#### B.11.4 Espacios vacíos

**En el mensaje de Microsoft, mirado desde los marcos [I].**

| # | Vacío | Quién sí lo trata |
|---|---|---|
| 1 | Modelo de amenazas del propio SOC agéntico: alertas falsas inyectadas, envenenamiento de memoria, secuestro de objetivos | CSA [CSA-01]; ATT&CK v20 ya incluye la técnica [EXT-14] |
| 2 | Verificación independiente de la eficacia de los agentes | CSA con STAR for AI, como camino posible |
| 3 | Criterios para decidir cuánta autonomía dar a cada acción | Ninguno de forma completa |
| 4 | Modos de falla y operación degradada | CSA [CSA-01] |
| 5 | Gobierno en organizaciones con varias entidades | Ninguno |
| 6 | Cuantificación del riesgo y materialidad | The Open Group con Open FAIR |
| 7 | Entornos OT | Ninguno de los revisados |

**En los marcos, mirados desde lo que ya se puede operar [I].**

1. No hay una norma final para el SOC agéntico.
2. SP 800-61 Rev. 3 no contempla agentes que ejecutan pasos de la respuesta.
3. No hay una taxonomía estándar de niveles de autonomía para acciones de seguridad.
4. No hay métricas estándar para evaluar agentes de seguridad.
5. La convergencia de exposición, validación ofensiva y respuesta no está reflejada en la estructura de los marcos.
6. El valor probatorio de la evidencia generada por agentes no está tratado.
7. El modelo económico por consumo y su gobierno no están tratados.

**Consecuencia para el CISO [I].** Durante 2027 no habrá una norma que diga cómo operar un SOC agéntico. El holding tendrá que fijar su propio criterio, documentarlo y poder defenderlo usando lo que sí existe: CSF 2.0 y SP 800-61 Rev. 3 como estructura, el borrador de CSA para los controles sobre agentes, CIS para la higiene de la capa de agentes y Open FAIR para cuantificar.

#### B.11.5 ¿Está reflejado en los workshops SAF?

No en los dos decks SAF. Se buscó por términos clave y se leyeron los pasajes devueltos, no los decks completos; del AI-Powered SOC se revisó el módulo 1 y fragmentos de los módulos 3, 5 y 7.

| Tema | SAF Modern SecOps (ADS 3) [INT-04] | AI SAF Strategy and Governance [INT-06] | Workshop AI-Powered SOC [INT-10] |
|---|---|---|---|
| Procesos y roles clásicos | Sí | Sí, como roles del borrador S252 de The Open Group | Sí, como modelo operativo de 7 fases |
| IA asistiva (Security Copilot) | Parcial: diapositivas ocultas | Sí | Sí |
| Agentes de tarea | No se encontró | Sí: cinco agentes como ejemplo | Sí |
| Perception, agentes rojo, azul y verde, playbooks | No | No | Sí |
| ISOC | No: arquitectura XDR + SIEM fechada en diciembre de 2023 | No | Sí |
| Supervisión humana y gobierno de agentes | Solo aprobación de la remediación automática | Sí, como principio | Sí: aprobaciones, controles de identidad, auditabilidad [INT-09] |
| Niveles de autonomía, SOC compartido, materialidad | No | No | No se vio en el módulo 1 |

- **AI SAF:** la versión publicada es del 30 de junio [INT-08]; la copia de trabajo del 16 de octubre ya nombra el AI-Powered SOC como workshop complementario [INT-07].
- **AI-Powered SOC:** las notas del orador del módulo 1 todavía describen a Security Copilot como capa de coordinación, mientras las diapositivas ya muestran los playbooks de Perception. El módulo 3 tiene cifras de ATT&CK y ATLAS desactualizadas (B.7.1).
- **Guía pública de SAF en Learn:** recoge el principio (automatización a velocidad de máquina con juicio y supervisión humana), no los productos [MS-25, MS-26].

### B.12 Qué significa para el holding

#### B.12.1 Un SOC compartido para tres negocios independientes

El modelo agéntico se apoya en contexto compartido, y eso choca con la independencia de las unidades. Tres preguntas que el diseño debe responder [D]:

1. **¿Qué puede ver un agente entre unidades?** Conviene que vea para detectar movimiento lateral; hay que decidir bajo qué reglas.
2. **¿Con qué identidad actúa?** Cada acción debe ser atribuible a una identidad con permisos acotados a la unidad y a un responsable humano.
3. **¿Quién aprueba?** El SOC es compartido, pero el dueño del riesgo es cada unidad.

No se investigó cómo se comportan Perception e ISOC con varios tenants o workspaces [D].

| Unidad | Qué prima | Dónde empezar a agentificar [R] | Dónde limitar la autonomía [R] |
|---|---|---|---|
| **Industria** | Disponibilidad y seguridad física; OT | Triage e investigación en TI corporativa; inteligencia del sector; priorización de exposición | Cualquier acción sobre OT: solo recomendación |
| **Retail** | Continuidad del canal digital; datos de pago | Triage de phishing e identidad; protección previa al parche en activos expuestos | Acciones sobre plataformas de venta en picos de demanda: aprobación con ventana |
| **Financiera** | Cumplimiento, evidencia y plazos | Investigación con cronología y evidencia; ingeniería de detección; triage con muestreo ampliado | Sistemas centrales y cuentas privilegiadas: aprobación explícita; conservación completa de trazas del agente |

Agregado tras el caso Zava [R]: en retail y en la unidad financiera, tratar como activos críticos a los agentes que intervienen en decisiones con efecto económico.

#### B.12.2 La obligación de reportar incidentes a los accionistas

- **Qué aporta el SOC agéntico [I].** Reduce el tiempo hasta tener un cuadro confiable de alcance, cronología y entidades afectadas.
- **Qué no cambia [R].** La determinación de materialidad y la decisión de divulgar no se delegan a un agente.
- **Qué se vuelve más exigente [I].** El reloj corre antes; los incidentes se cruzan entre unidades; la traza del agente es parte del expediente; un error del agente también puede ser un incidente.
- **Lección del caso Zava [I].** Un agente que decide o aconseja sobre reembolsos es un activo financiero: las respuestas emitidas en la ventana pueden traducirse en pagos, aunque no haya exfiltración.

| Paso | Quién | Apoyo de agentes |
|---|---|---|
| 1. Detección y triage con severidad única del holding | SOC | Sí |
| 2. Investigación y paquete de evidencia | SOC | Sí, con revisión humana |
| 3. Estimación de impacto por unidad | Unidad de negocio con el SOC | Parcial |
| 4. Determinación de materialidad | Comité: CISO, legal, finanzas y la unidad afectada | No |
| 5. Divulgación y notificaciones | Legal y relación con inversores | No |
| 6. Conservación del expediente, incluida la traza de agentes | SOC y legal | Parcial |

No se investigó el régimen de divulgación aplicable al holding [D].

#### B.12.3 Modelo de autonomía gobernada [R]

Ninguna de las fuentes revisadas ofrece una escala estándar. Esta es una propuesta.

| Nivel | Nombre | El agente | La persona |
|---|---|---|---|
| A0 | Informar | Resume y recomienda | Decide y ejecuta |
| A1 | Proponer | Prepara la acción | Ejecuta |
| A2 | Ejecutar con aprobación | Ejecuta después de una aprobación explícita | Aprueba cada acción |
| A3 | Ejecutar e informar | Ejecuta acciones reversibles dentro de límites | Revisa después; puede revertir |
| A4 | Ciclo cerrado | Ejecuta el flujo completo | Audita por muestreo |

**Criterios para asignar un nivel.** Reversibilidad (lo que no se puede deshacer no pasa de A2); radio de impacto; criticidad del activo; desempeño medido del agente dentro del holding; exigencia regulatoria.

| Acción | Corporativo y retail | Financiera | Industria, TI | Industria, OT |
|---|---|---|---|---|
| Enriquecer e investigar | A4 | A4 | A4 | A4 sobre datos; sin interacción activa |
| Cerrar una alerta como falso positivo | A3 | A3 con muestreo ampliado | A3 | A2 |
| Aislar un equipo de usuario | A3 | A2, con paso a A3 según evidencia | A3 | A1 |
| Deshabilitar una cuenta de usuario | A3 | A2 | A2 | A1 |
| Deshabilitar una cuenta privilegiada o de servicio | A2 | A2 | A2 | A1 |
| Desplegar una regla de detección | A2 | A2 | A2 | A2 |
| Aplicar una protección temporal previa al parche | A2, con paso a A3 según evidencia | A2 | A2 | A1 |
| Desplegar un parche | A2 | A2 | A2 | A1 |
| Prueba de penetración sobre una aplicación web | A2 con alcance autorizado | A2 con ventana acordada | A2 | No aplica |
| Determinar materialidad y divulgar | Solo personas | Solo personas | Solo personas | Solo personas |

**Filas propuestas tras el caso Zava, pendientes de aprobación [D].** No se propuso un nivel por unidad de negocio.

| Acción sobre agentes del negocio | Nivel propuesto |
|---|---|
| Poner en cuarentena un documento de una fuente de conocimiento | A3 |
| Congelar escrituras en la fuente de conocimiento | A3 |
| Suspender un agente del negocio | A2 |
| Restringir un despliegue de IA | A2 |

Subir de nivel exige evidencia: un período de comparación entre el veredicto del agente y el del analista, con tasa de reversión por debajo de un umbral que el CISO define [R].

#### B.12.4 Hoja de ruta 2027 [R]

| Ciclo | Período | Objetivo | Acciones principales | Resultado verificable |
|---|---|---|---|---|
| 0 | Dic-2026 | Decidir y medir | Tomar las siete decisiones; línea base de MTTA, MTTR, alertas sin investigar y tiempo hasta la determinación de materialidad; confirmar licencias | Decisiones registradas; línea base publicada |
| 1 | Ene a mar | Unificar la plataforma | Operar Sentinel desde el portal de Defender antes del 31-mar-2027; evaluar la adhesión a ISOC; inventario de agentes del negocio con dueño, fuentes de conocimiento e identidad; política de autonomía v1; mapa contra CSF 2.0 | SOC en una sola consola; inventario y política aprobados |
| 2 | Abr a jun | Agentificar lo de bajo riesgo | Triage con agentes en categorías de pocos falsos positivos, comparando contra el analista; investigación asistida; informes de inteligencia; formar supervisores de agentes; incorporar las fuentes de telemetría de B.8 (agregado en esta síntesis) | Tasa de reversión medida; primer tablero de desempeño de agentes |
| 3 | Jul a sep | Cerrar el ciclo | Detecciones propuestas por agentes con aprobación; priorización de postura; reconocimiento en alcance acotado; integración con la mesa de servicios; simulacro de materialidad con evidencia generada por agentes | Primer flujo rojo, azul y verde completo; simulacro realizado |
| 4 | Oct a dic | Autonomía gobernada | Subir niveles donde la evidencia lo permita; incorporar capacidades que hayan pasado a GA; revisión independiente contra el borrador de CSA y el perfil de NIST; informe al directorio | Matriz de autonomía v2; informe de aseguramiento |

**Hitos externos.** Normalización en la ingesta de Sentinel en Preview (dic-2026) [EXT-02]; novedades de Purview (ene-2027, a validar en fuente pública) [INT-03]; fin del soporte de Sentinel en el portal de Azure (31-mar-2027) [EXT-02]; pilotos del anexo de STAR for AI de CSA (ene a jun-2027) [EXT-04]; próximas versiones del Cyber AI Profile y de los overlays de NIST (sin fecha).

**Indicadores propuestos.** MTTA y MTTR; porcentaje de alertas triadas por agentes; tasa de reversión de veredictos; porcentaje de alertas sin investigar; tiempo de exposición a remediación; tiempo hasta el paquete de evidencia y hasta la determinación de materialidad; porcentaje de acciones de alto impacto con aprobación registrada; costo de IA por incidente investigado. Agregados tras el caso Zava: tiempo hasta correlacionar señales de capas distintas, y porcentaje de agentes con dueño y dependencias mapeadas.

#### B.12.5 Decisiones que se le piden al CISO

| # | Decisión [D] | Opciones | Recomendación [R] |
|---|---|---|---|
| 1 | Plataforma | Adherir a ISOC ahora, o migrar solo al portal de Defender y evaluar ISOC después | Migrar antes del 31-mar-2027 en cualquier caso; decidir ISOC tras confirmar licencias y topología |
| 2 | Política de autonomía | Aprobar el modelo de niveles y la matriz, o ajustarlo | Aprobar como v1 con revisión trimestral, incluidas las filas sobre agentes |
| 3 | Materialidad | Formalizar que la determinación y la divulgación son humanas | Formalizar antes de activar agentes de investigación |
| 4 | Segregación entre unidades | Contexto compartido, o separación para la unidad financiera | Compartir para detección; acotar las acciones por unidad; validar viabilidad técnica |
| 5 | OT | Incluir OT en acciones de agentes, o limitarlo a recomendación | Limitar a recomendación durante 2027 |
| 6 | Aseguramiento | Marco de referencia y frecuencia de evaluación de agentes | CSF 2.0 y SP 800-61 Rev. 3 como estructura; borrador de CSA para controles de agentes; evaluación trimestral |
| 7 | Presupuesto y talento | Tope de consumo de IA; rediseño del nivel 1 | Tope por ciclo ligado a indicadores; reconversión hacia supervisión de agentes e ingeniería de detección |

### B.13 Correcciones y cambios hechos durante la sesión

| Turno | Qué cambió | Efecto |
|---|---|---|
| 3 | El borrador S252 de The Open Group define roles de SecOps y debe figurar en la comparación | Agregado en B.4.1 y B.11.2 |
| 6 | El flujo de cinco etapas del tablero se reemplaza por uno de ocho, con contención en paralelo a la investigación | B.6.3 |
| 7 | El informe v1.0 tenía tres vacíos: respuesta sobre agentes del negocio, infraestructura de IA como capa y acciones sobre agentes en la matriz de autonomía | Proceso N10 (B.5), filas nuevas del mapa (B.10.2) y de la matriz (B.12.3), dos indicadores nuevos (B.12.4) |
| 8 | ATT&CK v20 y ATLAS ya cubren técnicas de IA; el módulo 3 del workshop tiene cifras anteriores | B.7.1 |
| 9 | De las once narrativas presentadas como nuevas en el turno 8, solo tres no tienen antecedente | B.7.3 |
| 10 | Seis fuentes de telemetría nuevas y dos señales sin registro identificado | B.8 |

Los siete cambios que el caso Zava pedía al informe v1.0 quedaron incorporados en esta síntesis. Los archivos originales no se modificaron (Parte D).

### B.14 Límites y pendientes

| Tema | Detalle |
|---|---|
| Lectura parcial de fuentes | Varias páginas se recuperaron truncadas. La guía de CSA, el perfil de NIST, la guía de CIS, el Microsoft Digital Defense Report y las páginas del laboratorio se trabajaron por fragmentos o resúmenes, no por el texto completo |
| Estado de disponibilidad | GA y Preview se tomaron de los anuncios del 17 al 19 de noviembre de 2026 y no se verificaron uno por uno en Learn |
| Hoja de ruta sin fuente pública | Los agentes futuros de hunting e ingeniería inversa, el aprendizaje compartido y las novedades de Purview de enero de 2027 salen de recaps internos |
| Cifras del fabricante | El 80 % de la cola triado por el agente y otras cifras de eficacia son de Microsoft, sin verificación independiente. Varias cifras de amenazas vienen de informes de fabricantes de seguridad |
| Marcos en borrador | El perfil de NIST y la guía de CSA pueden cambiar |
| The Open Group | No se halló publicación específica sobre IA en operaciones; la ausencia puede deberse al alcance de la búsqueda |
| Identificadores sin verificar | Los nombres de las técnicas nuevas de ATT&CK v20 y la lista de OWASP vienen de fuentes secundarias |
| Caso de laboratorio | Entidades y tiempos del guion; discrepancias internas entre páginas del laboratorio sobre la etapa 2 y sobre la severidad |
| Régimen regulatorio | No investigado |
| Datos del holding | Licencias, tenants, cobertura OT y herramientas no Microsoft no relevados |
| Dependencia del proveedor | Concentrar plataforma, agentes y modelos en un proveedor reduce fricción y aumenta dependencia; conviene evaluarlo de forma explícita |
| Sin investigar | Operaciones de influencia, ataques destructivos con borrado de datos, comparación con otros fabricantes, dimensionamiento económico |

## Parte C. Referencias y fuentes

Los enlaces son los que se registraron durante la sesión; no se volvieron a abrir al compilar. La columna "Turnos" indica en qué turno se consultó cada fuente. Las fuentes marcadas como secundarias, de fabricante o de comunidad no sustituyen a la publicación oficial.

### C.1 Enlaces internos de Microsoft

Requieren acceso corporativo. Se usaron para orientar la investigación y validar coherencia; el informe para el cliente debe citar solo fuentes públicas. >> **Se reumueve del documento.** 



### C.2 Enlaces públicos

#### C.2.1 Microsoft: postura, Ignite 2026 y producto

| Clave | Fuente | Tipo | Turnos | Enlace |
|---|---|---|---|---|
| MS-01 | Security for the agentic era, powered by Microsoft Perception (17-nov-2026) | Oficial | T1 | <https://www.microsoft.com/en-us/security/blog/2026/11/17/security-for-the-agentic-era-powered-by-microsoft-perception/> |
| MS-02 | What's new with Microsoft Perception at Ignite 2026 (17-nov-2026) | Oficial | T1 | <https://techcommunity.microsoft.com/blog/perception-blog/whats-new-with-microsoft-perception-at-ignite-2026/4571834> |
| MS-03 | Ignite 2026: What's new in Microsoft Defender & Sentinel (17-nov-2026) | Oficial | T1 | <https://techcommunity.microsoft.com/blog/microsoftthreatprotectionblog/ignite-2026-whats-new-in-microsoft-defender--sentinel/4569975> |
| MS-04 | Ignite 2026: What's new in Microsoft Sentinel (17-nov-2026) | Oficial | T1 | <https://techcommunity.microsoft.com/blog/microsoftsentinelblog/ignite-2026-whats-new-in-microsoft-sentinel/4571174> |
| MS-05 | The agentic SOC: Rethinking SecOps for the next decade (9-abr-2026) | Oficial | T1 | <https://www.microsoft.com/en-us/security/blog/2026/04/09/the-agentic-soc-rethinking-secops-for-the-next-decade/> |
| MS-06 | Whitepaper: Agentic SecOps, A New SOC Operating Model | Oficial | T1 | <https://marketingassets.microsoft.com/gdc/gdc46cegG/original> |
| MS-07 | Reimagining the SOC for the agentic era in Microsoft Defender (23-sep-2026) | Oficial | T1 | <https://www.microsoft.com/en-us/security/blog/2026/09/23/reimagining-the-soc-for-the-agentic-era-in-microsoft-defender/> |
| MS-08 | Rethinking security for the age of AI (27-jul-2026) | Oficial | T1 | <https://blogs.microsoft.com/blog/2026/07/27/rethinking-security-for-the-age-of-ai/> |
| MS-09 | What is Perception? (Microsoft Learn) | Oficial | T1 | <https://learn.microsoft.com/en-us/security/agentic-security/agentic-security-overview> |
| MS-10 | Agent categories in Perception (Microsoft Learn) | Oficial | T1 | <https://learn.microsoft.com/en-us/security/agentic-security/agentic-security-agent-categories> |
| MS-11 | Microsoft Perception, página de producto | Oficial | T1 | <https://www.microsoft.com/en-us/security/business/microsoft-perception-agentic-system> |
| MS-12 | Security Copilot in Defender: assistive and autonomous AI (20-mar-2026) | Oficial | T1 | <https://techcommunity.microsoft.com/blog/microsoftthreatprotectionblog/security-copilot-in-defender-empowering-the-soc-with-assistive-and-autonomous-ai/4503047> |
| MS-13 | Security Copilot for SOC: bringing agentic AI to every defender (18-nov-2025) | Oficial | T1 | <https://techcommunity.microsoft.com/blog/microsoftthreatprotectionblog/security-copilot-for-soc-bringing-agentic-ai-to-every-defender/4470187> |
| MS-14 | Microsoft unveils Security Copilot agents (24-mar-2025) | Oficial | T1 | <https://www.microsoft.com/en-us/security/blog/2025/03/24/microsoft-unveils-microsoft-security-copilot-agents-and-new-protections-for-ai/> |
| MS-15 | Deploy AI agents in Microsoft Defender (Microsoft Learn) | Oficial | T1 | <https://learn.microsoft.com/en-us/defender-xdr/security-copilot-agents-defender> |
| MS-16 | Microsoft Perception helps IT drive outcomes and scale (17-nov-2026) | Oficial | T1 | <https://techcommunity.microsoft.com/blog/IntuneCustomerSuccess/microsoft-perception-helps-it-drive-outcomes-and-scale/4573285> |
| MS-17 | MAI Cyber 2 Flash (17-nov-2026) | Oficial | T1 | <https://microsoft.ai/news/introducing-mai-cyber-2-flash/> |
| MS-18 | Getting started with Codename MDASH (Microsoft Learn) | Oficial | T1 | <https://learn.microsoft.com/en-us/security-exposure-management/ai-code-security-onboarding> |
| MS-19 | Microsoft Sentinel MCP, conector (Microsoft Learn) | Oficial | T1 | <https://learn.microsoft.com/en-us/connectors/sentinelmcp/> |
| MS-20 | Announcing Zero Trust for AI (19-mar-2026) | Oficial | T1 | <https://www.microsoft.com/en-us/security/blog/2026/03/19/new-tools-and-guidance-announcing-zero-trust-for-ai/> |
| MS-21 | Microsoft Ignite 2026 Book of News | Oficial | T1 | <https://news.microsoft.com/events/ignite/2026/book-of-news/> |
| MS-22 | Documentación de Perception (Microsoft Learn) | Oficial | T1 | <https://learn.microsoft.com/en-us/security/agentic-security/> |
| MS-23 | Microsoft Security Copilot, sitio de adopción | Oficial | T1 | <https://adoption.microsoft.com/en-us/security-copilot/> |
| MS-24 | Security Copilot agents in Defender XDR: where things actually stand (abr-2026) | Comunidad, no oficial | T1 | <https://techcommunity.microsoft.com/discussions/microsoft-security/security-copilot-agents-in-defender-xdr-where-things-actually-stand/4514689> |
| MS-25 | Establish a Security Operations discipline (SAF, Microsoft Learn) | Oficial | T3 | <https://learn.microsoft.com/en-us/security/zero-trust/security-adoption-discipline-security-operations> |
| MS-26 | AI security in the Security Adoption Framework (Microsoft Learn) | Oficial | T3 | <https://learn.microsoft.com/en-us/security/saf/foundations/ai-security-governance> |

#### C.2.2 Microsoft: detección, respuesta e identidad (caso Zava)

| Clave | Fuente | Tipo | Turnos | Enlace |
|---|---|---|---|---|
| MS-27 | Automatically disrupt adversary-in-the-middle (AiTM) attacks with XDR | Oficial | T6, T7 | <https://techcommunity.microsoft.com/blog/microsoftthreatprotectionblog/automatically-disrupt-adversary-in-the-middle-aitm-attacks-with-xdr/3821751> |
| MS-28 | Automatic attack disruption in Microsoft Defender (Microsoft Learn) | Oficial | T7 | <https://learn.microsoft.com/en-us/defender-xdr/automatic-attack-disruption> |
| MS-29 | AI threat protection in Microsoft Defender for Cloud (Microsoft Learn) | Oficial | T6, T7 | <https://learn.microsoft.com/en-us/azure/defender-for-cloud/ai-threat-protection> |
| MS-30 | Alerts for AI services (Defender for Cloud, Microsoft Learn) | Oficial | T7 | <https://learn.microsoft.com/en-us/azure/defender-for-cloud/alerts-ai-workloads> |
| MS-31 | Prompt Shields in Azure AI Content Safety (Microsoft Learn) | Oficial | T7 | <https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection> |
| MS-32 | Continuous access evaluation in Microsoft Entra (Microsoft Learn) | Oficial | T7 | <https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-continuous-access-evaluation> |
| MS-33 | What are risk detections? (Entra ID Protection, Microsoft Learn) | Oficial | T7 | <https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-risks> |
| MS-34 | What is Microsoft Entra ID Protection? (Microsoft Learn) | Oficial | T7 | <https://learn.microsoft.com/en-us/entra/id-protection/overview-identity-protection> |
| MS-35 | Alert correlation and incident merging in the Defender portal (Microsoft Learn) | Oficial | T7 | <https://learn.microsoft.com/en-us/defender-xdr/alerts-incidents-correlation> |
| MS-36 | Merge and split incident cases in the Defender portal (Microsoft Learn) | Oficial | T7 | <https://learn.microsoft.com/en-us/defender-xdr/manage-incident-case-merging> |
| MS-37 | Detect and investigate threats to AI agents using Microsoft Defender (Preview) (Microsoft Learn) | Oficial | T7, T10 | <https://learn.microsoft.com/en-us/defender-xdr/security-for-ai/ai-agent-detection-protection> |
| MS-38 | Securing workload identities with Microsoft Entra ID Protection (Microsoft Learn) | Oficial | T7 | <https://learn.microsoft.com/en-us/entra/id-protection/concept-workload-identity-risk> |
| MS-39 | Protecting tokens in Microsoft Entra (Microsoft Learn) | Oficial | T7 | <https://learn.microsoft.com/en-us/entra/identity/devices/protecting-tokens-microsoft-entra-id> |
| MS-40 | Zero Trust Workshop: Integrate AI Threat Response with Defender XDR | Oficial | T7 | <https://microsoft.github.io/zerotrustassessment/docs/workshop-guidance/AI/AI_095> |

#### C.2.3 Microsoft: inteligencia de amenazas

| Clave | Fuente | Tipo | Turnos | Enlace |
|---|---|---|---|---|
| MS-41 | Unmasking EvilTokens: Getting to the root of device code phishing (22-sep-2026) | Oficial | T8, T9 | <https://www.microsoft.com/en-us/security/blog/2026/09/22/unmasking-eviltokens-getting-to-the-root-of-device-code-phishing/> |
| MS-42 | AI as tradecraft: How threat actors operationalize AI (6-mar-2026) | Oficial | T8 | <https://www.microsoft.com/en-us/security/blog/2026/03/06/ai-as-tradecraft-how-threat-actors-operationalize-ai/> |
| MS-43 | Threat actor abuse of AI accelerates from tool to cyberattack surface (2-abr-2026) | Oficial | T8 | <https://www.microsoft.com/en-us/security/blog/2026/04/02/threat-actor-abuse-of-ai-accelerates-from-tool-to-cyberattack-surface/> |
| MS-44 | 2026 Digital Defense Report, Security Insider (1-oct-2026) | Oficial | T8, T9 | <https://www.microsoft.com/en-us/security/security-insider/threat-landscape/2026-digital-defense-report> |
| MS-45 | Microsoft Digital Defense Report 2026, página del informe | Oficial | T9 | <https://www.microsoft.com/en-us/corporate-responsibility/topics/cybersecurity/reports/microsoft-digital-defense-report/> |
| MS-46 | Microsoft Digital Defense Report 2026, resumen ejecutivo (PDF) | Oficial | T9 | <https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/msc/documents/presentations/CSR/2026-Microsoft-DDR-Exec-Summary.pdf> |
| MS-47 | Microsoft Digital Defense Report 2026, informe completo v1.1 (PDF) | Oficial | T9 | <https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/msc/documents/presentations/CSR/Microsoft-Digital-Defense-Report-2026-v1.1.pdf> |

#### C.2.4 Microsoft: telemetría de IA y agentes

| Clave | Fuente | Tipo | Turnos | Enlace |
|---|---|---|---|---|
| MS-48 | Audit logs for Copilot and AI applications (Microsoft Learn) | Oficial | T10 | <https://learn.microsoft.com/en-us/purview/audit-copilot> |
| MS-49 | Collecting Microsoft 365 Copilot Data with Microsoft Purview eDiscovery (4-may-2026) | Oficial | T10 | <https://techcommunity.microsoft.com/blog/microsoft-security-blog/collecting-microsoft-365-copilot-data-with-microsoft-purview-ediscovery/4516489> |
| MS-50 | Zero Trust Workshop: Enable Microsoft Purview Audit for AI interactions | Oficial | T10 | <https://microsoft.github.io/zerotrustassessment/docs/workshop-guidance/AI/AI_045> |
| MS-51 | Discover AI agents and assess security posture using Microsoft Defender (Microsoft Learn) | Oficial | T10 | <https://learn.microsoft.com/en-us/defender-xdr/security-for-ai/ai-agent-inventory> |
| MS-52 | Zero Trust Workshop: Enable Diagnostic Logging for AI Services and Agents | Oficial | T10 | <https://microsoft.github.io/zerotrustassessment/docs/workshop-guidance/AI/AI_085> |
| MS-53 | Securing Enterprise AI Agents with Microsoft Sentinel (30-jul-2026) | Oficial | T10 | <https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/securing-enterprise-ai-agents-with-microsoft-sentinel/4542583> |
| MS-54 | Zero Trust Workshop: AI related data connectors enabled on Microsoft Sentinel/SIEM workspace | Oficial | T10 | <https://microsoft.github.io/zerotrustassessment/docs/workshop-guidance/AI/AI_089> |
| MS-55 | Agent 365 connector: Monitor, hunt, and investigate AI agent activity in Microsoft Sentinel (18-may-2026) | Oficial | T10 | <https://techcommunity.microsoft.com/blog/microsoftsentinelblog/agent-365-connector-monitor-hunt-and-investigate-ai-agent-activity-in-microsoft-/4520836> |
| MS-56 | Agent 365 observability concepts (Microsoft Learn) | Oficial | T10 | <https://learn.microsoft.com/en-us/microsoft-agent-365/developer/observability-concepts> |
| MS-57 | Agent 365 solution for Sentinel (Preview), Microsoft Marketplace | Oficial | T10 | <https://marketplace.microsoft.com/en-us/product/azuresentinel.azure-sentinel-solution-a365observability> |
| MS-58 | Microsoft Entra Agent ID logs (Microsoft Learn) | Oficial | T10 | <https://learn.microsoft.com/en-us/entra/agent-id/sign-in-audit-logs-agents> |
| MS-59 | Enable diagnostic logging for Microsoft Foundry (Microsoft Learn) | Oficial | T10 | <https://learn.microsoft.com/en-us/azure/foundry/how-to/diagnostic-logging> |

#### C.2.5 Laboratorio TechWorkshop L400 "Using AI to Secure the Modern SOC" (primer borrador)

| Clave | Fuente | Tipo | Turnos | Enlace |
|---|---|---|---|---|
| LAB-01 | Repositorio del laboratorio (declara estado de borrador) | Oficial, borrador | T7 | <https://github.com/microsoft/TWL400-Using-AI-to-Secure-the-Modern-SOC> |
| LAB-02 | Introducción del laboratorio | Oficial, borrador | T7 | <https://microsoft.github.io/TWL400-Using-AI-to-Secure-the-Modern-SOC/> |
| LAB-03 | Ejercicio 01: triage y alcance | Oficial, borrador | T7 | <https://microsoft.github.io/TWL400-Using-AI-to-Secure-the-Modern-SOC/docs/01_triage_and_scope/01_triage_and_scope.html> |
| LAB-04 | Ejercicio 00, tarea 02: escenario y cola de alertas | Oficial, borrador | T7 | <https://microsoft.github.io/TWL400-Using-AI-to-Secure-the-Modern-SOC/docs/00_lab_environment/00_02.html> |
| LAB-05 | Ejercicio 01, tarea 03: entidades y cronología | Oficial, borrador | T7 | <https://microsoft.github.io/TWL400-Using-AI-to-Secure-the-Modern-SOC/docs/01_triage_and_scope/01_03.html> |
| LAB-06 | Ejercicio 01, tarea 04: por qué la sobrecarga de señales oculta la cadena | Oficial, borrador | T7 | <https://microsoft.github.io/TWL400-Using-AI-to-Secure-the-Modern-SOC/docs/01_triage_and_scope/01_04.html> |
| LAB-07 | Ejercicio 02, tarea 01: hunting con KQL y ubicación de cada etapa | Oficial, borrador | T7 | <https://microsoft.github.io/TWL400-Using-AI-to-Secure-the-Modern-SOC/docs/02_reconstruct_the_lifecycle/02_01.html> |
| LAB-08 | Ejercicio 02, tarea 02: corroboración con Defender for Identity | Oficial, borrador | T7 | <https://microsoft.github.io/TWL400-Using-AI-to-Secure-the-Modern-SOC/docs/02_reconstruct_the_lifecycle/02_02.html> |
| LAB-09 | Ejercicio 02, tarea 03: puntos de falla de detección | Oficial, borrador | T7 | <https://microsoft.github.io/TWL400-Using-AI-to-Secure-the-Modern-SOC/docs/02_reconstruct_the_lifecycle/02_03.html> |
| LAB-10 | Ejercicio 02, tarea 04: dependencias sistémicas y señales en conflicto | Oficial, borrador | T7 | <https://microsoft.github.io/TWL400-Using-AI-to-Secure-the-Modern-SOC/docs/02_reconstruct_the_lifecycle/02_04.html> |
| LAB-11 | Ejercicio 03, tarea 01: contención coordinada | Oficial, borrador | T7 | <https://microsoft.github.io/TWL400-Using-AI-to-Secure-the-Modern-SOC/docs/03_coordinated_response/03_01.html> |
| LAB-12 | Ejercicio 03, tarea 02: automatización con Sentinel | Oficial, borrador | T7 | <https://microsoft.github.io/TWL400-Using-AI-to-Secure-the-Modern-SOC/docs/03_coordinated_response/03_02.html> |
| LAB-13 | Ejercicio 03, tarea 03: frontera entre acciones autónomas y aprobadas | Oficial, borrador | T7 | <https://github.com/microsoft/TWL400-Using-AI-to-Secure-the-Modern-SOC/blob/main/docs/03_coordinated_response/03_03.md> |
| LAB-14 | Ejercicio 03, tarea 04: riesgo residual | Oficial, borrador | T7 | <https://microsoft.github.io/TWL400-Using-AI-to-Secure-the-Modern-SOC/docs/03_coordinated_response/03_04.html> |
| LAB-15 | Ejercicio 04, tarea 01: visualización de extremo a extremo | Oficial, borrador | T7 | <https://microsoft.github.io/TWL400-Using-AI-to-Secure-the-Modern-SOC/docs/04_proof_through_scenario/04_01.html> |
| LAB-16 | Ejercicio 04, tarea 02: fallas de detección | Oficial, borrador | T7 | <https://microsoft.github.io/TWL400-Using-AI-to-Secure-the-Modern-SOC/docs/04_proof_through_scenario/04_02.html> |
| LAB-17 | Ejercicio 04, tarea 03: impacto de negocio | Oficial, borrador | T7 | <https://microsoft.github.io/TWL400-Using-AI-to-Secure-the-Modern-SOC/docs/04_proof_through_scenario/04_03.html> |

#### C.2.6 MITRE

| Clave | Fuente | Tipo | Turnos | Enlace |
|---|---|---|---|---|
| MITRE-01 | MITRE ATLAS, matriz y cifras actuales | Oficial | T8 | <https://atlas.mitre.org/> |
| MITRE-02 | ATLAS data, registro de cambios (versiones 2026.08 y 2026.09) | Oficial | T8 | <https://github.com/mitre-atlas/atlas-data/blob/main/CHANGELOG.md> |
| MITRE-03 | ATT&CK, actualizaciones de octubre de 2026 (v20) | Oficial | T8 | <https://attack.mitre.org/resources/updates/> |
| MITRE-04 | ATT&CK, actualizaciones de octubre de 2025 (v18) | Oficial | T8 | <https://attack.mitre.org/resources/updates/updates-october-2025/> |
| MITRE-05 | ATT&CK, campaña C0062: Anthropic AI-orchestrated Campaign | Oficial | T8 | <https://attack.mitre.org/campaigns/C0062/> |
| MITRE-06 | ATT&CK T1496.004, Resource Hijacking: Cloud Service Hijacking | Oficial | T8 | <https://attack.mitre.org/techniques/T1496/004/> |
| MITRE-07 | ATT&CK T1696, Anti-Automation Evasion | Oficial | T9 | <https://attack.mitre.org/techniques/T1696/> |

#### C.2.7 NIST

| Clave | Fuente | Tipo | Turnos | Enlace |
|---|---|---|---|---|
| NIST-01 | SP 800-61 Rev. 3, Incident Response Recommendations and Considerations (abr-2025) | Oficial, final | T1 | <https://csrc.nist.gov/pubs/sp/800/61/r3/final> |
| NIST-02 | IR 8596, Cyber AI Profile (dic-2025) | Oficial, borrador preliminar | T1 | <https://csrc.nist.gov/pubs/ir/8596/iprd> |
| NIST-03 | IR 8607, resumen del taller del Cyber AI Profile (ago-2026) | Oficial | T1 | <https://www.nist.gov/publications/workshop-summary-report-cyber-ai-profile-hybrid-workshop> |
| NIST-04 | Proyecto de overlays de SP 800-53 para sistemas de IA | Oficial, en desarrollo | T1 | <https://csrc.nist.gov/projects/cosis> |
| NIST-05 | AI Agent Standards Initiative | Oficial, en curso | T1 | <https://www.nist.gov/artificial-intelligence/ai-agent-standards-initiative> |
| NIST-06 | Draft NIST Guidelines Rethink Cybersecurity for the AI Era (16-dic-2025) | Oficial | T1 | <https://www.nist.gov/news-events/news/2025/12/draft-nist-guidelines-rethink-cybersecurity-ai-era> |
| NIST-07 | Proyecto Incident Response, CSRC (modelo de ciclo de vida de SP 800-61 Rev. 3) | Oficial | T6 | <https://csrc.nist.gov/projects/incident-response> |

#### C.2.8 Cloud Security Alliance

| Clave | Fuente | Tipo | Turnos | Enlace |
|---|---|---|---|---|
| CSA-01 | Agentic Cybersecurity Implementation Guide (27-mar-2026) | Oficial, borrador | T1 | <https://labs.cloudsecurityalliance.org/agentic/agentic-cybersecurity-implementation-guide-v1/> |
| CSA-02 | Securing the Agentic Control Plane, programa 2026 | Oficial | T1 | <https://labs.cloudsecurityalliance.org/agentic/> |
| CSA-03 | Secure Agentic System Design: A Trait-Based Approach | Oficial | T1 | <https://cloudsecurityalliance.org/artifacts/secure-agentic-system-design> |
| CSA-04 | Agentic AI Identity and Access Management: A New Approach | Oficial | T1 | <https://cloudsecurityalliance.org/artifacts/agentic-ai-identity-and-access-management-a-new-approach> |
| CSA-05 | Nota de investigación de CSA sobre la iniciativa de NIST (30-mar-2026) | Oficial | T1 | <https://labs.cloudsecurityalliance.org/research/csa-research-note-nist-ai-agent-standards-federal-framework/> |
| CSA-06 | Slopsquatting: AI Code Hallucinations Fuel Supply Chain Attacks (19-abr-2026) | Investigación no oficial asistida por IA | T9 | <https://labs.cloudsecurityalliance.org/research/csa-research-note-slopsquatting-ai-supply-chain-20260419-csa/> |
| CSA-07 | Slopsquatting, versión PDF de la nota | Investigación no oficial asistida por IA | T9 | <https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/04/CSA_research_note_slopsquatting-ai-supply-chain_20260419-csa-styled-1.pdf> |

#### C.2.9 Center for Internet Security

| Clave | Fuente | Tipo | Turnos | Enlace |
|---|---|---|---|---|
| CIS-01 | AI Agents Companion Guide, CIS Controls v8.1 (20-abr-2026) | Oficial | T1 | <https://www.cisecurity.org/insights/white-papers/controls-v8-1-ai-agents-companion-guide> |
| CIS-02 | CIS Controls v8.1 AI Security Guidance Workbook (27-jul-2026) | Oficial | T1 | <https://www.cisecurity.org/insights/white-papers/controls-v8-1-2-ai-security-guidance-workbook> |

#### C.2.10 The Open Group

| Clave | Fuente | Tipo | Turnos | Enlace |
|---|---|---|---|---|
| TOG-01 | Zero Trust, Security Forum | Oficial | T1 | <https://www.opengroup.org/forum/security/Zerotrust> |
| TOG-02 | Zero Trust Architecture Working Group | Oficial | T1 | <https://www.opengroup.org/forum/security-forum-0/zerotrustsecurityarchitecture> |
| TOG-03 | Security Forum Members' Meeting, Houston 2024 | Oficial | T1 | <https://www.opengroup.org/Houston-2024-10/Security> |

#### C.2.11 OWASP

| Clave | Fuente | Tipo | Turnos | Enlace |
|---|---|---|---|---|
| OWASP-01 | OWASP Top 10 for Agentic Applications 2026 | Oficial | T7 | <https://genai.owasp.org/top-10-for-agentic-applications-2026/> |

#### C.2.12 Terceros y fuentes secundarias

| Clave | Fuente | Tipo | Turnos | Enlace |
|---|---|---|---|---|
| EXT-01 | Recap independiente: What's new with Microsoft Perception at Ignite 2026 | Secundaria | T1 | <https://ignite2026.recapped.fi/a/whats-new-with-microsoft-perception-at-ignite-2026/> |
| EXT-02 | Recap independiente: Ignite 2026: What's new in Microsoft Sentinel | Secundaria | T1 | <https://ignite2026.recapped.fi/a/ignite-2026-whats-new-in-microsoft-sentinel/> |
| EXT-03 | Skylight Cyber: análisis de NIST IR 8596 (mar-2026) | Secundaria | T1 | <https://skylightcyber.com/2026/03/16/nist-ai-security/> |
| EXT-04 | THE Journal: Cloud Security Alliance Expands Agentic AI Governance Work (6-may-2026) | Secundaria | T1 | <https://thejournal.com/articles/2026/05/06/cloud-security-alliance-expands-agentic-ai-governance-work.aspx> |
| EXT-05 | Cequence: análisis de la guía MCP de CIS (abr-2026) | Secundaria | T1 | <https://www.cequence.ai/blog/cis-mcp-companion-guide-enterprise-ai-agent-governance> |
| EXT-06 | Reseña de la AI Agents Companion Guide de CIS (LinkedIn, jul-2026) | Secundaria | T1 | <https://www.linkedin.com/pulse/new-cis-ai-agents-companion-guide-april-2026-chandra-mouli-y9xtc> |
| EXT-07 | Mark Simos: Security and Zero Trust at The Open Group (LinkedIn, ago-2025) | Secundaria | T1 | <https://www.linkedin.com/pulse/security-zero-trust-open-group-mark-simos-vc7fe/> |
| EXT-08 | Vectorize: OWASP ASI06, Memory and Context Poisoning Explained (12-jun-2026) | Secundaria | T6, T7 | <https://vectorize.io/articles/owasp-asi06> |
| EXT-09 | NHI Mgmt Group: OWASP ASI06 Memory and Context Poisoning, Controls Guide (26-oct-2026) | Secundaria | T6, T7 | <https://nhimg.org/owasp-agentic-top-10-asi06-guide> |
| EXT-10 | Blck Alpaca: OWASP Agentic Security Top 10 (2026) | Secundaria | T8 | <https://blckalpaca.at/en/knowledge-base/ai-agents/ai-agent-security-owasp/owasp-agentic-asi-top-10-2026> |
| EXT-11 | Anthropic: Disrupting the first reported AI-orchestrated cyber espionage campaign (nov-2025) | Informe del proveedor afectado | T8 | <https://www-cdn.anthropic.com/d7dd50dd1185f59be051b307150d877f2b82bd2c.pdf> |
| EXT-12 | Gambit Security: The AI-Assisted Breach of Mexico's Government Infrastructure | Informe de fabricante | T8 | <https://gambit.security/ai-assisted-breach-of-mexicos-government-infrastructure> |
| EXT-13 | Industrial Cyber: MITRE ATT&CK v20 expands critical infrastructure threat coverage (16-oct-2026) | Secundaria | T8, T9 | <https://industrialcyber.co/industrial-cyber-attacks/mitre-attck-v20-expands-critical-infrastructure-threat-coverage-with-new-it-and-ot-attack-techniques/> |
| EXT-14 | Cyberpress: MITRE ATT&CK Adds New AI Attack Techniques (16-oct-2026) | Secundaria | T8 | <https://cyberpress.org/mitre-attck-adds-new-ai-attack-techniques/> |
| EXT-15 | CortexFlow: MITRE ATT&CK v20 Maps the AI Attacks (16-oct-2026) | Secundaria | T9 | <https://cortexflow.tech/blog/mitre-attck-v20-ai-techniques-agent-defense/> |
| EXT-16 | ShieldPi: ficha del caso de ATLAS AML.CS0030, LLMjacking | Secundaria | T8 | <https://www.shieldpi.io/map/incident/AML.CS0030> |
| EXT-17 | Security Today: Deepfake Voices Stealing Millions from Executive Suites (4-abr-2026) | Secundaria | T8 | <https://www.securitytoday.de/en/2026/04/04/deepfake-attacks-c-suite-ai-voices-ceo-fraud/> |
| EXT-18 | CrowdStrike: 2026 Global Threat Report, comunicado (24-feb-2026) | Informe de fabricante | T9 | <https://www.crowdstrike.com/en-us/press-releases/2026-crowdstrike-global-threat-report/> |
| EXT-19 | Check Point Research: AI Security Report 2026 (14-jul-2026) | Informe de fabricante | T9 | <https://research.checkpoint.com/2026/ai-security-report-2026/> |
| EXT-20 | Digital Watch Observatory: Zscaler ThreatLabz 2026 Ransomware Report (30-sep-2026) | Secundaria sobre informe de fabricante | T9 | <https://dig.watch/updates/zscaler-threatlabz-2026-ransomware-report-275> |
| EXT-21 | Black Kite: AI and Ransomware, 2026 Ransomware Report | Informe de fabricante | T9 | <https://blackkite.com/report/ransomware-report-2026/ai-and-ransomware> |
| EXT-22 | imper.ai: Case Files from the Help Desk, A Month of Vishing (16-jul-2026) | Informe de fabricante | T9 | <https://imper.ai/case-files-from-the-help-desk-a-month-of-vishing-q2-2026/> |
| EXT-23 | Wikipedia: Slopsquatting | Secundaria | T9 | <https://en.wikipedia.org/wiki/Slopsquatting> |
| EXT-24 | EC-Council University: How AI Is Rewriting the Rules of DDoS Attacks (10-abr-2026) | Blog universitario | T9 | <https://www.eccu.edu/blog/ai-powered-ddos-attacks-2026/> |
| EXT-25 | Frontrow: Copilot audit logs and eDiscovery, the investigation runbook (28-ago-2026) | Secundaria | T10 | <https://frontrowtech.com.au/insights/copilot-audit-logs-ediscovery-kql> |

### 

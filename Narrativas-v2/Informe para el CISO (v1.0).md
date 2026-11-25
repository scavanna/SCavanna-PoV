# Del SOC de alertas al SOC agéntico: qué cambió, qué viene en 2027 y qué decidir

**Informe para el CISO del holding**

| Campo | Valor |
|---|---|
| Destinatario | CISO de un holding |
| Propósito | Explicar cómo cambiaron los procesos del SOC, qué propone Microsoft tras Ignite 2026, cómo se compara con NIST, CSA, CIS y The Open Group, y qué decisiones requiere |
| Fecha | 24-nov-2026 |
| Versión | 1.0, borrador para revisión antes de entregar |
| Base | Fuentes públicas listadas en la sección 14 |

**Cómo leer este informe.** Cada afirmación relevante lleva una etiqueta: **[E]** evidencia de una fuente citada, **[I]** inferencia propia, **[R]** recomendación, **[D]** decisión pendiente. Las capacidades de producto llevan su estado: **GA**, **Preview** u **Hoja de ruta**. Los estados corresponden a los anuncios del 17 al 19 de noviembre de 2026 y deben verificarse en Microsoft Learn antes de comprometer fechas.

---

## 1. Resumen ejecutivo

1. **El SOC dejó de ser una cola de alertas atendida por niveles.** En cinco años pasó de analistas que ejecutan con ayuda de automatización, a analistas asistidos por IA generativa, a agentes que ejecutan mientras las personas fijan límites y aprueban. [I, sobre M5, M6, M1]
2. **El motivo es la velocidad del atacante.** Microsoft documenta una campaña de phishing como servicio que tardaba unos catorce días y hoy se completa en 85 minutos, pasando de 10 a 3.000 usuarios objetivo, y exploits funcionales en alrededor de un día tras la divulgación de una vulnerabilidad crítica. [E: M2, M1]
3. **Ignite 2026 convirtió la visión en producto.** Microsoft Perception pasó a disponibilidad general con agentes rojos, azules y verdes coordinados por playbooks, y las capacidades centrales de ISOC (SIEM y XDR unificados en el portal de Defender) también son GA. [E: M1, M2, M3]
4. **De 16 procesos clásicos del SOC, diez cambian quién ejecuta o cómo están diseñados y seis se aceleran sin cambiar de diseño.** Aparecen además nueve procesos nuevos, la mayoría de gobierno y supervisión de agentes. [I, secciones 4 y 5]
5. **Los marcos independientes coinciden en los principios y llegan tarde en lo operativo.** NIST, CSA, CIS y The Open Group respaldan supervisión humana, identidad y mínimo privilegio para agentes y fundamentos primero. Ninguno tiene todavía una norma final para operar un SOC agéntico. [E/I, sección 8]
6. **El vacío más importante para este holding no lo cubre ningún proveedor ni marco:** cómo se gobierna la autonomía de agentes en un SOC compartido entre tres negocios con perfiles de riesgo distintos, y cómo se preserva la decisión humana sobre materialidad y divulgación a accionistas. [I]
7. **Hay una fecha que no depende de la estrategia:** el soporte de Microsoft Sentinel en el portal de Azure termina el 31 de marzo de 2027. [E: M25]

**Recomendación central [R].** Adoptar el SOC agéntico por etapas durante 2027, con un modelo de autonomía por niveles que use la reversibilidad de la acción y la criticidad del negocio como criterios, y con una regla explícita: los agentes preparan la evidencia de un incidente; la determinación de materialidad y la divulgación siguen siendo decisiones humanas con responsable nombrado.

**Las siete decisiones que se le piden al CISO** están en la sección 12.

---

## 2. Por qué cambia el SOC

| Fuerza | Evidencia | Fuente |
|---|---|---|
| El atacante opera a velocidad de máquina | Campaña comparable a EvilTokens: de ~14 días a 85 minutos; de 10 a 3.000 usuarios objetivo | M2 |
| Descubrir y explotar vulnerabilidades se abarató | Exploit funcional en alrededor de un día tras la divulgación de fallas críticas de PHP; unos 29 millones de servicios seguían vulnerables casi dos semanas después | M1 |
| El volumen de vulnerabilidades crece | Cerca de 40.000 CVE publicados en el primer semestre de 2026, según el Microsoft Digital Defense Report 2026 citado por Microsoft | M16 |
| El modelo manual no escala | 42 % de las alertas quedan sin investigar; los analistas dedican más del 20 % de su tiempo a reunir datos; 91 % de los líderes atribuye a estas brechas un incidente serio (encuesta de Microsoft) | M6 |
| Los agentes son un nuevo tipo de actor interno | Microsoft los describe como "los nuevos insiders": operan sin pausa, con acceso amplio, y pueden equivocarse, ser manipulados o comprometidos | M1 |
| Presión regulatoria | Directorios y reguladores piden gobierno más fuerte, supervisión humana documentada y reporte rápido y preciso de incidentes | M6 |

**Lectura para el holding [I].** Las tres primeras filas afectan a las tres unidades. La última es la que más pesa en este caso: un SOC que reporta incidentes para información de accionistas necesita velocidad de investigación y, a la vez, trazabilidad de quién decidió qué.

---

## 3. Los procesos que se pueden individualizar en un SOC

No existe una taxonomía única. Este catálogo combina las funciones de operaciones de seguridad que Microsoft describe en su Security Adoption Framework (triage, investigación, hunting, ingeniería de detección, inteligencia de amenazas, gestión de incidentes, con MTTA y MTTR como métricas) con las seis funciones de NIST CSF 2.0. Es una síntesis propia. [I]

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

---

## 4. Cómo cambió cada proceso en tres momentos

**Los tres momentos.** *2021–2022:* SIEM, SOAR y XDR con aprendizaje automático clásico; la persona ejecuta. *Noviembre de 2026:* IA generativa asistiva madura y primeros sistemas multiagente en GA; el agente ejecuta tareas acotadas. *2027:* proyección; el agente ejecuta flujos completos dentro de límites aprobados.

Entre 2023 y 2025 hubo una etapa intermedia que explica el salto: Security Copilot como asistente (resumen de incidentes, consultas en lenguaje natural, respuesta guiada) y, desde marzo de 2025, los primeros agentes de Security Copilot para phishing, datos e identidad. [E: M14, M13]

Las columnas 2021–2022 y "grado" son juicio analítico [I]. La columna noviembre de 2026 se apoya en las fuentes indicadas. La columna 2027 es proyección [I] y no un compromiso de producto.

| ID | Proceso | 2021–2022 | Noviembre de 2026 | Proyección 2027 | Tipo de cambio | Grado |
|---|---|---|---|---|---|---|
| P8 | Triage de alertas | Analista de nivel 1 revisa una por una; reglas de supresión | Agentes clasifican y explican el veredicto; Microsoft afirma ~80 % de una cola típica de Defender (M2) | El nivel 1 humano pasa a ser revisión por excepción y ajuste del agente | Transformado | Muy alto |
| P9 | Investigación | Correlación manual entre consolas; horas por incidente | Agente reconstruye la historia del ataque, cronología, técnicas y entidades (M10) | Investigación preparada antes de que la persona abra el caso; señales de terceros incorporadas | Transformado | Alto |
| P7 | Ingeniería de detección | Reglas escritas a mano; ciclos de semanas | Agente identifica brechas de cobertura y propone reglas; playbook que va de inteligencia a detección (M2, M10) | Detección como código generada y probada por agentes, con aprobación humana | Transformado | Alto |
| P3 | Inteligencia de amenazas | Lectura manual de reportes; listas de indicadores | Agente extrae patrones e indicadores de reportes y los relaciona con el entorno (M10); informes diarios adaptados (M13) | Inteligencia que dispara protección sin pasar por una cola | Acelerado y transformado | Alto |
| P4 | Gestión de exposición | Ciclo mensual de escaneo y parcheo, fuera del SOC | Agente prioriza por riesgo real; protección temporal previa al parche en Preview (M3, M10) | Se integra al ciclo del SOC: hallazgo, protección y parche en un mismo flujo | Transformado y fusionado | Muy alto |
| P5 | Validación ofensiva | Ejercicios anuales o trimestrales, tercerizados | Agente de reconocimiento GA; agente de pruebas de penetración web en Preview (M2, M10) | Validación continua; el resultado alimenta detección y remediación | Transformado | Alto |
| P6 | Datos y telemetría | Conectores a medida; costo de ingesta limita la visibilidad | Más de 500 conectores, lago de datos integrado, retención de 90 días para datos de Defender elegibles; agente constructor de conectores (M4) | Normalización en la ingesta; los datos se preparan para agentes, no solo para consultas | Transformado | Alto |
| P11 | Contención y remediación | Playbooks SOAR con aprobación manual; pocas acciones automáticas | Defensa autónoma integrada para amenazas de alta confianza; agentes recomiendan y piden aprobación para acciones críticas (M5, M9) | Más acciones reversibles ejecutadas sin intervención; las irreversibles siguen con aprobación | Acelerado | Medio a alto |
| P10 | Threat hunting | Hipótesis y consultas escritas por expertos | Lenguaje natural a consultas; agentes que generan hipótesis (Preview en Security Copilot, M24) | Hunting continuo por agentes; la persona define hipótesis estratégicas | Acelerado | Medio a alto |
| P13 | Automatización | Playbooks estáticos | Playbooks que coordinan equipos de agentes hacia un resultado (M9) | La orquestación de agentes reemplaza gran parte del SOAR estático | Transformado | Alto |
| P1 | Gobierno y métricas | MTTA, MTTR, volumen de alertas | Se agregan métricas de agentes y de costo por consumo (M11) | Métricas de resultado: exposición cerrada, veredictos revertidos, costo por caso | Transformado | Medio a alto |
| P2 | Incidentes mayores y notificación | Informe armado a mano bajo presión | Resúmenes y cronologías generados por IA; la decisión sigue siendo humana | Evidencia lista en horas; presión por decidir más rápido | Acelerado | Medio |
| P12 | Forense y malware | Especialistas; herramientas dedicadas | Asistencia para analizar scripts | Agentes de ingeniería inversa (Hoja de ruta, a validar) | Acelerado | Medio |
| P14 | Recuperación | Coordinación manual con TI | Planes de remediación que llegan a TI con contexto (M16) | Seguridad prioriza, TI aprueba y despliega en un mismo flujo | Acelerado | Medio |
| P15 | Lecciones aprendidas | Informe posterior al incidente | Los agentes aprenden de la retroalimentación del analista (M10) | El aprendizaje se comparte entre agentes (Hoja de ruta, a validar) | Acelerado | Medio |
| P16 | Talento y turnos | Carrera por niveles 1, 2 y 3 | El nivel 1 se reduce como puerta de entrada | Nuevos roles: supervisor de agentes, ingeniero de contexto, ingeniero de detección | Transformado | Alto |

**Respuesta directa a las tres primeras preguntas.**

- **Impactados (acelerados, mismo diseño):** P2, P10, P11, P12, P14, P15. La IA reduce el tiempo; la persona sigue siendo quien decide y, en buena parte, quien ejecuta.
- **Transformados (cambia quién ejecuta o el diseño):** P1, P3, P4, P5, P6, P7, P8, P9, P13, P16. El caso extremo es el triage: deja de ser un puesto y pasa a ser una función supervisada.
- **Fusionados:** la gestión de exposición (P4) y la validación ofensiva (P5) eran procesos vecinos al SOC. El modelo rojo, azul y verde los mete en el mismo ciclo que la detección y la respuesta. [I, sobre M9]

---

## 5. Procesos nuevos

### 5.1 Nuevos por la IA en el ataque

| ID | Proceso nuevo | Por qué aparece | Respaldo |
|---|---|---|---|
| N1 | Detección y respuesta sobre sistemas de IA y agentes | Los agentes del negocio son insiders que pueden ser manipulados o comprometidos; hay que vigilar su comportamiento en ejecución | M1, M3 |
| N2 | Inventario y postura de agentes | No se defiende lo que no se conoce: agentes locales, en la nube y no autorizados | M1, I1, N5 |
| N3 | Protección previa al parche a velocidad de máquina | La ventana entre divulgación y explotación se redujo a alrededor de un día | M1, M3 |
| N4 | Defensa del propio SOC agéntico | Un agente del SOC puede ser atacado con inyección de instrucciones, alertas falsas o envenenamiento de memoria | C1 |

### 5.2 Nuevos por la IA en la defensa

| ID | Proceso nuevo | Qué hace | Respaldo |
|---|---|---|---|
| N5 | Gobierno y supervisión de agentes defensivos | Define qué agente puede hacer qué, aprueba acciones, detiene sesiones, revisa resultados | M9, M11 |
| N6 | Evaluación y aseguramiento de agentes | Mide precisión de veredictos, tasa de reversión y deriva; prueba antes de ampliar autonomía | C1, N2 [I] |
| N7 | Ingeniería de contexto | Mantiene el conocimiento de la organización que los agentes usan: criticidad de activos, excepciones, retroalimentación | M10, M11 |
| N8 | Gestión económica del SOC agéntico | Presupuesta y controla el consumo de IA frente a resultados | M11 |
| N9 | Seguridad de código asistida por agentes | Descubre y valida vulnerabilidades en repositorios; frontera entre SOC y desarrollo | M17, M18 |

**Nota [I].** N4 y N6 son los que menos aparecen en el mensaje de producto y los que más importan para un regulador financiero. Están en la guía de CSA y en el perfil de NIST, no en los anuncios.

---

## 6. Cómo opera un SOC agéntico

### 6.1 El modelo según Microsoft

- **Definición.** Un modelo operativo que pasa de reaccionar a incidentes a anticipar cómo se mueve el atacante y modificar el entorno para cortarle el camino. Combina una plataforma que se defiende sola ante amenazas conocidas de alta confianza con agentes que trabajan junto a las personas. [E: M5]
- **Tres etapas de madurez.** (1) Unificar la plataforma. (2) Acelerar con IA generativa y agentes de tarea. (3) Desplegar automatización agéntica. [E: M5, M6]
- **Tres equipos de agentes en ciclo cerrado.** Rojos encuentran y validan caminos de compromiso. Azules clasifican alertas, investigan y convierten inteligencia en detecciones. Verdes priorizan exposición y coordinan la remediación. [E: M2, M9]
- **Playbooks orientados a resultados.** Un playbook asigna objetivos a un equipo de agentes y coordina su trabajo; puede iniciarse a mano, por chat o por reglas de automatización. [E: M9]
- **Personas en control.** Los agentes operan con mínimo privilegio, piden aprobación antes de acciones críticas, y cada acción queda registrada y auditable. La persona puede aprobar, rechazar, detener o redirigir una sesión. [E: M9, M11]

### 6.2 Cómo cambia el trabajo diario [I]

| Antes | En el SOC agéntico |
|---|---|
| El analista abre una alerta y empieza a reunir datos | El analista abre un caso con veredicto, cronología y acciones sugeridas |
| Tres niveles que se pasan el caso | Agentes que comparten contexto; personas que deciden en puntos definidos |
| Se mide volumen atendido | Se mide resultado: exposición cerrada, tiempo de permanencia del atacante |
| El rojo entrega un informe; el azul lo lee semanas después | El hallazgo del rojo genera una detección y una remediación en el mismo flujo |
| El conocimiento está en las personas | El conocimiento también está en el contexto que usan los agentes y hay que mantenerlo |

### 6.3 Casos de uso: qué ya está agentificado y qué sigue

| Estado | Casos de uso |
|---|---|
| **Ya agentificados (GA o uso extendido)** | Triage de phishing reportado por usuarios; triage de alertas de Defender; investigación y reconstrucción de ataques; extracción de inteligencia de amenazas e informes adaptados; creación de detecciones a partir de inteligencia; reconocimiento de caminos de ataque; priorización de postura |
| **En agentificación (Preview)** | Triage de alertas de identidad y nube; pruebas de penetración de aplicaciones web; reducción de riesgo con protección previa al parche; hunting con generación de hipótesis; detección dinámica de amenazas; triage de alertas de DLP y riesgo interno; remediación de vulnerabilidades desde Intune; incorporación de señales de terceros |
| **Próximos (Hoja de ruta o proyección)** | Agentes especializados de hunting e ingeniería inversa; aprendizaje compartido entre agentes; gestión de exposición integrada; correcciones propuestas como cambios de código; normalización de datos en la ingesta |
| **Sin agentificar, y conviene que siga así [R]** | Determinación de materialidad; decisión de divulgar; declaración de crisis; acciones irreversibles sobre sistemas críticos del negocio u OT; aceptación de riesgo |

Las filas "ya agentificados" y "en agentificación" se apoyan en M2, M3, M10, M12, M16, M23 y M24. La fila "próximos" incluye elementos de hoja de ruta mencionados en Ignite 2026 que no pude confirmar en una fuente pública escrita; deben validarse antes de usarlos en una planificación.

Como referencia externa, la guía de CSA organiza los agentes de seguridad en cuatro patrones: automatización del SOC, gestión de vulnerabilidades, hunting y respuesta a incidentes. [E: C1]

---

## 7. Qué se puede agentificar con tecnología Microsoft, con cuál y cómo

### 7.1 Las piezas

| Capa | Tecnología | Papel |
|---|---|---|
| Señales, sensores y actuadores | Microsoft Defender (endpoint, identidad, correo, nube, aplicaciones), Entra, Intune, Purview | Ven y actúan |
| Contexto | Microsoft Sentinel (lago de datos, grafo, más de 500 conectores) dentro de ISOC en el portal de Defender | Convierte señales en comprensión compartida para personas y agentes |
| Agentes, orquestación y modelos | Microsoft Perception (agentes rojos, azules y verdes; playbooks; modelos MAI-Cyber) y agentes de Security Copilot | Razonan y ejecutan |
| Extensión | API y MCP de Perception (Preview), servidor MCP de Sentinel (Preview), creador de agentes de Security Copilot, Copilot Studio, Logic Apps, Security Store | Agentes propios e integración con SIEM, SOAR e ITSM existentes |
| Gobierno de agentes del negocio | Agent 365, Entra Agent ID, Acceso Condicional para agentes | Inventario, identidad y control de los agentes que el SOC debe vigilar |

Fuentes: M1, M2, M3, M4, M7, M19. Las tres capas del "cyber stack" son la formulación de Microsoft. [E: M1, M7]

### 7.2 Mapa por proceso

| Proceso | Agente o capacidad Microsoft | Estado | Cómo se agentifica | Control humano |
|---|---|---|---|---|
| P8 Triage | Triage Agent (Perception) | GA | Clasifica alertas como verdaderas o falsas y explica el razonamiento; aprende de la retroalimentación | Revisión de veredictos; ajuste por retroalimentación |
| P8 Triage | Security Alert Triage Agent (Security Copilot) | GA para phishing; identidad y nube en Preview según la última información disponible | Triage de correos reportados y de un subconjunto de alertas de identidad y nube | Ídem |
| P9 Investigación | Attack Investigation Agent (Perception) | GA | Correlaciona alertas, incidentes y señales; entrega veredicto, cronología, técnicas, indicadores y entidades | La persona valida y decide la respuesta |
| P3 Inteligencia | Threat Intelligence Agent (Perception) | GA | Extrae patrones e indicadores de un reporte y analiza cómo defenderse | Selección de fuentes; revisión del análisis |
| P3 Inteligencia | Threat Intelligence Briefing Agent (Security Copilot) | GA | Informe periódico adaptado al entorno | Lectura y priorización |
| P7 Detección | Detection Authoring Agent y playbook de amenazas emergentes (Perception) | GA | Identifica brechas de cobertura y redacta reglas | Aprobación antes de desplegar la regla |
| P7 Detección | Dynamic Threat Detection Agent (Security Copilot) | Preview según la última información disponible | Correlaciona telemetría de forma continua y emite alertas con explicación | Revisión de alertas generadas |
| P10 Hunting | Threat Hunting Agent (Security Copilot) | Preview según la última información disponible | Lenguaje natural a consultas, hunting guiado | La persona formula la hipótesis |
| P5 Validación ofensiva | Recon Agent (Perception) | GA | Mapea el entorno, caminos de ataque, activos valiosos, configuraciones débiles y permisos excesivos | Definición de alcance; el agente pregunta antes de ampliar |
| P5 Validación ofensiva | Web App Pen Test Agent (Perception) | Preview | Prueba aplicaciones web autorizadas y demuestra qué debilidades son explotables | Autorización explícita del objetivo |
| P4 Exposición | Posture Prioritization Agent (Perception) | GA | Ordena problemas de postura por riesgo real, explotabilidad y criticidad | Decisión de qué remediar |
| P4 Exposición | Risk Reduction Agent y protección previa al parche (Defender) | Preview | Investiga la vulnerabilidad, despliega el parche con Intune si existe o aplica una protección temporal | Aprobación del plan |
| P4 Exposición | Identity Risk Reduction Agent (Perception); Conditional Access Optimization Agent (Entra) | Verificar estado en Learn | Detecta brechas en protección de identidad y propone cambios de Acceso Condicional | El administrador revisa y aprueba |
| P14 Recuperación | Vulnerability Remediation Agent (Intune) | Verificar estado en Learn | Convierte riesgo priorizado en planes de reducción listos para aprobar | TI aprueba el cambio |
| P6 Datos | Connector Builder Agent en VS Code (Sentinel) | GA prevista para fin de noviembre de 2026 | Asiste en la construcción de conectores | Revisión del conector |
| P6 Datos | Normalización en la ingesta (Sentinel) | Preview desde diciembre de 2026 | Estandariza los datos al ingresarlos | Gestión de analizadores |
| P11 Contención | Interrupción automática de ataques y acciones de respuesta (Defender); playbooks de Perception | GA la defensa integrada; acciones de agentes con aprobación | Aísla dispositivos y bloquea cuentas ante señales de alta confianza; los agentes recomiendan el resto | Aprobación de acciones de alto impacto |
| N1 Agentes como insiders | Protección en ejecución de agentes locales en Windows (Defender); Dynamic Agent Risk (Agent 365) | Verificar estado en Learn; Dynamic Agent Risk en Preview | Vigila el comportamiento de agentes y calcula un riesgo por agente | Política de contención |
| N2 Inventario de agentes | Agent 365 con Entra Agent ID | Verificar por capacidad | Descubre agentes locales y en la nube y les asigna identidad gobernable | Asignación de dueño |
| N9 Código | Codename MDASH con modelos MAI-Cyber | Preview | Sistema de agentes que busca y valida vulnerabilidades en repositorios | Revisión de hallazgos y correcciones |
| Datos sensibles | Data Security Triage Agent y Data Security Posture Agent (Purview) | Preview según la última información disponible | Triage de alertas de DLP y riesgo interno | Revisión del analista de datos |
| Casos propios | Creador de agentes de Security Copilot, Copilot Studio o Logic Apps con el servidor MCP de Sentinel; API y MCP de Perception | Preview en los componentes MCP | Agentes a medida que consultan datos de Sentinel o inician playbooks desde ITSM, SIEM o SOAR | Diseño, pruebas y dueño a cargo del cliente |

Fuentes principales: M2, M3, M4, M10, M12, M15, M16, M18, M19, M23, M24.

### 7.3 Lo que este mapa no garantiza

- **Las cifras de eficacia son de Microsoft.** El ~80 % de la cola es una cifra agregada propia, no una tasa garantizada por cliente. [E: M2, M25]
- **El costo es por consumo.** Perception se paga por uso o con compromiso previo, y Microsoft ofrece tableros y un estimador; no hay en las fuentes revisadas un precio de referencia por caso. [E: M11]
- **La elegibilidad de ISOC depende de la licencia.** Desde el 17-nov-2026 pueden optar los clientes de Sentinel con Microsoft 365 E5, E7 o Defender Suite; la adhesión es opcional. [E: M4]
- **La cobertura fuera de Microsoft está empezando.** Las señales de AWS, Okta y Salesforce para los agentes son recientes. [E: M2]
- **No encontré evidencia sobre cobertura de agentes en entornos OT.** Para la unidad industrial es una pregunta abierta. [D]
- **Activar una capacidad no equivale a operarla con madurez ni a cumplir una norma.** El cumplimiento sigue siendo responsabilidad de la organización. [I]

---

## 8. Postura de Microsoft y comparación con NIST, CSA, CIS y The Open Group

### 8.1 Postura y mensaje de Microsoft (incluye Ignite 2026)

| # | Mensaje | Fuente |
|---|---|---|
| 1 | "La física de la ciberseguridad está cambiando": la IA amplifica el riesgo, los ataques se automatizan por completo y los agentes son los nuevos insiders | M1 |
| 2 | Hace falta un nuevo "cyber stack" para combatir IA con IA, en tres capas: señales, sensores y actuadores; contexto; agentes, orquestación y modelos | M1, M7 |
| 3 | Tres resultados para el cliente: asegurar los fundamentos, defender con agentes, asegurar a los agentes como insiders | M1 |
| 4 | El SOC agéntico es un modelo operativo, no una herramienta: plataforma que se autodefiende más agentes que trabajan con personas | M5 |
| 5 | La base es la unificación: SIEM y protección contra amenazas como un solo sistema (ISOC en Defender) | M7, M3 |
| 6 | Agentes rojos, azules y verdes en ciclo cerrado, coordinados por playbooks orientados a resultados | M2, M9 |
| 7 | Las personas mantienen el control: fijan límites y aprueban acciones de alto impacto; todo queda registrado | M9, M11 |
| 8 | Apertura: señales de terceros y acceso por API y MCP desde las herramientas existentes | M2 |
| 9 | Modelos propios especializados en seguridad para bajar el costo de operar agentes a escala | M17 |

**Evolución del mensaje [I].** 2023–2024: un copiloto que asiste al analista. 2025: agentes de tarea dentro de cada producto. Abril de 2026: el SOC agéntico como modelo operativo. Julio a noviembre de 2026: un sistema de agentes coordinados sobre una plataforma unificada, ya disponible. La palabra que cambia es "asistir" por "actuar".

### 8.2 Qué dice cada marco

| Organismo | Publicaciones relevantes | Madurez | Qué aporta al SOC agéntico |
|---|---|---|---|
| **NIST** | SP 800-61 Rev. 3 (abr-2025): respuesta a incidentes como perfil de CSF 2.0 | Final | Integra la respuesta a incidentes en toda la gestión de riesgo, no como un proceso aislado. No trata agentes |
| **NIST** | IR 8596, Cyber AI Profile (dic-2025) | Borrador preliminar; talleres durante 2026 | Tres áreas: asegurar los sistemas de IA, defender con IA, frustrar ataques con IA. Supervisión humana como requisito constante |
| **NIST** | Overlays de SP 800-53 para sistemas de IA, con casos de agente único y multiagente (proyecto renombrado en oct-2026) | En desarrollo | Controles concretos para agentes cuando se publiquen |
| **NIST** | AI Agent Standards Initiative (feb-2026) y documento conceptual de identidad y autorización de agentes | Iniciativa en curso | Identidad y autorización de agentes como problema central |
| **CSA** | Agentic Cybersecurity Implementation Guide (mar-2026) | Borrador | El más cercano al tema: cuatro patrones (automatización del SOC, vulnerabilidades, hunting, respuesta) con límites de confianza, alcance de permisos, prevención de manipulación, supervisión humana y manejo de fallas |
| **CSA** | MAESTRO, guía de red teaming agéntico, IAM para agentes, diseño seguro por rasgos, AI Controls Matrix, programa "Securing the Agentic Control Plane" | Publicados y en expansión | Modelado de amenazas y controles para agentes; camino de aseguramiento con STAR for AI |
| **CIS** | AI Agents Companion Guide para CIS Controls v8.1 (abr-2026); guías para LLM y MCP; AI Security Guidance Workbook v8.1.2 (jul-2026) | Publicados | Aplica los 18 controles a la capa de agentes: inventario, mínimo privilegio, registro, respuesta a incidentes, pruebas. No propone un modelo operativo de SOC |
| **The Open Group** | Zero Trust Commandments (estándar), Zero Trust Reference Model (snapshot), Security Principles for Architecture, Open FAIR, O-ISM3 | Estándares publicados; modelo de referencia en borrador | Principios, roles y cuantificación de riesgo. No encontré una publicación oficial sobre IA o agentes en operaciones de seguridad |

Fuentes: N1 a N7, C1 a C6, I1 a I4, O1 a O4.

### 8.3 Puntos en común

| # | Coincidencia | Microsoft | NIST | CSA | CIS | Open Group |
|---|---|---|---|---|---|---|
| 1 | Supervisión humana sobre acciones de alto impacto | Aprobaciones y límites | Requisito constante del perfil | Requisitos por patrón | Capa de aplicación de políticas e interruptor de parada | Responsabilidad alineada al negocio |
| 2 | El agente es una identidad con mínimo privilegio | Entra Agent ID, permisos acotados | Documento de identidad y autorización | IAM para agentes | Control de acceso aplicado a agentes | Principios Zero Trust |
| 3 | Fundamentos primero | "Asegurar los fundamentos" | La mayoría de las prioridades altas son prácticas conocidas extendidas a IA | Controles base | Es la esencia de los CIS Controls | Principios de arquitectura |
| 4 | Doble mirada: asegurar la IA y defender con IA | Asegurar agentes y defender con agentes | Asegurar, defender, frustrar | Riesgo bidireccional | Asegurar la capa de agentes | Sin tratamiento específico |
| 5 | Registro y auditabilidad de lo que hace el agente | Acciones registradas y auditables | Registro extendido a activos de IA | Auditabilidad como condición | Traza de acciones del agente | Sin tratamiento específico |
| 6 | Inventario de sistemas de IA y agentes | Descubrimiento de agentes | Función Identificar | Registro de agentes | Inventario como primer control | Sin tratamiento específico |
| 7 | La respuesta a incidentes integrada con la gestión de riesgo | Ciclo rojo, azul y verde | SP 800-61 Rev. 3 | Patrones conectados | Control de respuesta a incidentes | Open FAIR para cuantificar |

La correspondencia entre los tres resultados de Microsoft y las tres áreas de NIST es una lectura propia; ninguna de las dos fuentes la declara. [I]

### 8.4 Espacios vacíos

**En el mensaje de Microsoft, mirado desde los marcos [I].**

| # | Vacío | Quién sí lo trata |
|---|---|---|
| 1 | Modelo de amenazas del propio SOC agéntico: alertas falsas inyectadas, envenenamiento de memoria, secuestro de objetivos. El mensaje público enfatiza límites y aprobaciones más que el ataque al agente defensor | CSA (C1) |
| 2 | Verificación independiente de la eficacia de los agentes. Las cifras publicadas son del fabricante | CSA con STAR for AI, como camino posible |
| 3 | Criterios para decidir cuánta autonomía dar a cada acción. Se afirma que la persona aprueba lo crítico; no se define qué es crítico | Ninguno de forma completa; CSA lo esboza |
| 4 | Modos de falla y operación degradada: qué pasa cuando el agente se equivoca o no está disponible | CSA (C1) |
| 5 | Gobierno en organizaciones con varias entidades: segregación entre negocios, responsabilidades cruzadas | Ninguno |
| 6 | Cuantificación del riesgo y materialidad | The Open Group con Open FAIR |
| 7 | Entornos OT | Ninguno de los revisados |

**En los marcos, mirados desde lo que ya se puede operar [I].**

| # | Vacío |
|---|---|
| 1 | No hay una norma final para el SOC agéntico. NIST está en borrador, CSA en borrador, CIS no lo aborda como modelo operativo, The Open Group no lo trata |
| 2 | SP 800-61 Rev. 3 no contempla agentes que ejecutan pasos de la respuesta |
| 3 | No hay una taxonomía estándar de niveles de autonomía para acciones de seguridad |
| 4 | No hay métricas estándar para evaluar agentes de seguridad: precisión de veredictos, tasa de reversión, deriva |
| 5 | La convergencia de exposición, validación ofensiva y respuesta en un solo ciclo no está reflejada en la estructura de los marcos |
| 6 | Valor probatorio de la evidencia generada por agentes ante reguladores y auditores: sin tratamiento |
| 7 | Modelo económico por consumo y su gobierno: sin tratamiento |

**Consecuencia para el CISO [I].** Durante 2027 no habrá una norma que diga cómo operar un SOC agéntico. El holding tendrá que fijar su propio criterio, documentarlo y poder defenderlo ante auditores usando lo que sí existe: CSF 2.0 y SP 800-61 Rev. 3 como estructura, el borrador de CSA para los controles sobre agentes, CIS para la higiene de la capa de agentes y Open FAIR para cuantificar.

---

## 9. Qué significa para el holding

### 9.1 Un SOC compartido para tres negocios independientes

El modelo agéntico se apoya en contexto compartido: cuanto más ve el agente, mejor razona. Eso choca con la independencia de las unidades. Tres preguntas que el diseño debe responder [D]:

1. **¿Qué puede ver un agente entre unidades?** Un agente que investiga un incidente en retail, ¿puede consultar datos de la unidad financiera para buscar movimiento lateral? Conviene que sí para detectar, y hay que decidir bajo qué reglas.
2. **¿Con qué identidad actúa?** Si un agente contiene una cuenta en la unidad industrial, la acción debe ser atribuible a una identidad con permisos acotados a esa unidad y a un responsable humano.
3. **¿Quién aprueba?** El SOC es compartido, pero el dueño del riesgo es cada unidad. Las aprobaciones de alto impacto necesitan una ruta definida hacia la unidad afectada.

No investigué cómo se comportan Perception e ISOC en topologías con varios tenants o varios workspaces. Es un punto a validar con Microsoft antes de diseñar. [D]

### 9.2 Las tres unidades no admiten la misma autonomía

| Unidad | Qué prima | Dónde conviene empezar a agentificar [R] | Dónde limitar la autonomía [R] |
|---|---|---|---|
| **Industria** | Disponibilidad y seguridad física; entornos OT | Triage e investigación en TI corporativa; inteligencia de amenazas del sector; priorización de exposición | Cualquier acción sobre OT: solo recomendación hasta tener evidencia de cobertura y de efectos |
| **Retail** | Continuidad del canal digital; datos de pago; estacionalidad | Triage de phishing y de alertas de identidad; pruebas de penetración web cuando estén en GA; protección previa al parche en activos expuestos a internet | Acciones sobre plataformas de venta en picos de demanda: aprobación con ventana |
| **Financiera** | Cumplimiento, evidencia y plazos de notificación | Investigación con cronología y evidencia; ingeniería de detección; triage con muestreo de control ampliado | Acciones sobre sistemas centrales y cuentas privilegiadas: aprobación explícita; conservación completa de trazas del agente |

### 9.3 La obligación de reportar incidentes a los accionistas

**Qué aporta el SOC agéntico [I].** Reduce el tiempo entre la detección y el momento en que se tiene un cuadro confiable de alcance, cronología y entidades afectadas. Ese es el insumo de una evaluación de materialidad.

**Qué no cambia [R].** La determinación de si un incidente es material y la decisión de divulgarlo no se delegan a un agente. Requieren juicio sobre impacto financiero, reputacional y legal, y un responsable que responda por ellas.

**Qué se vuelve más exigente [I].**

- **El reloj corre antes.** Si la evidencia está lista en horas, será difícil justificar una determinación que tarde días.
- **Los incidentes se cruzan.** Un atacante que entra por retail y llega a la unidad financiera es un solo incidente para el accionista. El registro y la severidad deben ser únicos para el holding.
- **La traza del agente es parte del expediente.** Lo que el agente vio, concluyó y ejecutó, y quién lo aprobó, debe conservarse con el mismo cuidado que la evidencia forense.
- **Un error del agente también puede ser un incidente.** Una contención equivocada que detiene una operación es un evento a registrar y, según el impacto, a informar.

**Propuesta de proceso [R].**

| Paso | Quién | Apoyo de agentes |
|---|---|---|
| 1. Detección y triage con severidad única del holding | SOC | Sí |
| 2. Investigación y paquete de evidencia: alcance, cronología, unidades afectadas | SOC | Sí, con revisión humana |
| 3. Estimación de impacto por unidad | Unidad de negocio con el SOC | Parcial |
| 4. Determinación de materialidad | Comité: CISO, legal, finanzas y la unidad afectada | No |
| 5. Divulgación y notificaciones | Legal y relación con inversores | No |
| 6. Conservación del expediente, incluida la traza de agentes | SOC y legal | Parcial |

No investigué el régimen de divulgación aplicable al holding (mercado de valores, supervisor financiero, protección de datos). Los plazos y umbrales dependen de la jurisdicción y deben confirmarse con el área legal. [D]

---

## 10. Modelo de autonomía gobernada

Ninguna de las fuentes revisadas ofrece una escala estándar. Esta es una propuesta. [R]

### 10.1 Niveles

| Nivel | Nombre | El agente | La persona |
|---|---|---|---|
| A0 | Informar | Resume y recomienda | Decide y ejecuta |
| A1 | Proponer | Prepara la acción | Ejecuta |
| A2 | Ejecutar con aprobación | Ejecuta después de una aprobación explícita | Aprueba cada acción |
| A3 | Ejecutar e informar | Ejecuta acciones reversibles dentro de límites | Revisa después; puede revertir |
| A4 | Ciclo cerrado | Ejecuta el flujo completo | Audita por muestreo |

### 10.2 Criterios para asignar un nivel

1. **Reversibilidad.** Lo que no se puede deshacer no pasa de A2.
2. **Radio de impacto.** Cuántos usuarios, sistemas o ingresos afecta.
3. **Criticidad del activo** para la unidad de negocio.
4. **Desempeño medido del agente** en ese tipo de acción dentro del holding, no en promedios del fabricante.
5. **Exigencia regulatoria** sobre esa acción o ese sistema.

### 10.3 Matriz inicial

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

Subir de nivel exige evidencia: un período de comparación entre el veredicto del agente y el del analista, con tasa de reversión por debajo de un umbral que el CISO define. [R]

---

## 11. Hoja de ruta 2027

Cuatro ciclos de 90 días, compatibles con objetivos trimestrales, precedidos por un ciclo de preparación. [R]

| Ciclo | Período | Objetivo | Acciones principales | Resultado verificable |
|---|---|---|---|---|
| 0 | Dic-2026 | Decidir y medir | Tomar las decisiones de la sección 12; línea base de MTTA, MTTR, alertas sin investigar y tiempo hasta la determinación de materialidad; confirmar licencias y elegibilidad | Decisiones registradas; línea base publicada |
| 1 | Ene a mar | Unificar la plataforma | Operar Sentinel desde el portal de Defender antes del 31-mar-2027; evaluar la adhesión a ISOC; inventario de agentes del negocio; política de autonomía v1; mapa contra CSF 2.0 | SOC operando en una sola consola; inventario y política aprobados |
| 2 | Abr a jun | Agentificar lo de bajo riesgo | Triage con agentes en categorías de pocos falsos positivos, comparando contra el analista; investigación asistida; informes de inteligencia; formar supervisores de agentes | Tasa de reversión medida; primer tablero de desempeño de agentes |
| 3 | Jul a sep | Cerrar el ciclo | Detecciones propuestas por agentes con aprobación; priorización de postura; reconocimiento en alcance acotado; integración con la mesa de servicios; simulacro de materialidad con evidencia generada por agentes | Primer flujo rojo, azul y verde completo; simulacro realizado |
| 4 | Oct a dic | Autonomía gobernada | Subir niveles donde la evidencia lo permita; incorporar capacidades que hayan pasado a GA; revisión independiente contra el borrador de CSA y el perfil de NIST; informe al directorio | Matriz de autonomía v2; informe de aseguramiento |

**Hitos externos de 2027 que condicionan el plan.**

| Fecha | Hito | Fuente |
|---|---|---|
| Dic-2026 | Normalización en la ingesta de Sentinel en Preview | M25 |
| Ene-2027 | Novedades de Purview para clasificación y protección de datos frente a Copilot y agentes, según lo anunciado en Ignite | A validar en fuente pública |
| 31-mar-2027 | Fin del soporte de Sentinel en el portal de Azure | M25 |
| Ene a jun-2027 | Fase de pilotos del anexo de riesgo catastrófico de STAR for AI de CSA | C5 |
| Sin fecha | Versión siguiente del Cyber AI Profile de NIST y overlays para agentes | N2, N4 |

**Indicadores propuestos [R].**

| Indicador | Qué muestra |
|---|---|
| MTTA y MTTR | Capacidad de respuesta y tiempo de permanencia del atacante |
| Porcentaje de alertas triadas por agentes | Alcance de la agentificación |
| Tasa de reversión de veredictos de agentes | Confiabilidad; condición para subir autonomía |
| Porcentaje de alertas sin investigar | Deuda operativa |
| Tiempo de exposición a remediación | Efecto del ciclo rojo, azul y verde |
| Tiempo hasta el paquete de evidencia y hasta la determinación de materialidad | Preparación para el reporte a accionistas |
| Porcentaje de acciones de alto impacto con aprobación registrada | Cumplimiento de la política de autonomía |
| Costo de IA por incidente investigado | Sostenibilidad económica |

---

## 12. Decisiones que se le piden al CISO

| # | Decisión [D] | Opciones | Recomendación [R] |
|---|---|---|---|
| 1 | Plataforma | Adherir a ISOC ahora, o migrar solo al portal de Defender y evaluar ISOC después | Migrar antes del 31-mar-2027 en cualquier caso; decidir ISOC tras confirmar licencias y topología |
| 2 | Política de autonomía | Aprobar el modelo de niveles y la matriz inicial, o ajustarlo | Aprobar como v1 con revisión trimestral |
| 3 | Materialidad | Formalizar que la determinación y la divulgación son humanas, con comité y reloj definidos | Formalizar antes de activar agentes de investigación |
| 4 | Segregación entre unidades | Contexto compartido para los agentes, o separación para la unidad financiera | Compartir para detección; acotar las acciones por unidad; validar viabilidad técnica |
| 5 | OT | Incluir OT en acciones de agentes, o limitarlo a recomendación | Limitar a recomendación durante 2027 |
| 6 | Aseguramiento | Marco de referencia y frecuencia de evaluación de agentes | CSF 2.0 y SP 800-61 Rev. 3 como estructura; borrador de CSA para controles de agentes; evaluación trimestral |
| 7 | Presupuesto y talento | Tope de consumo de IA; rediseño del nivel 1 | Tope por ciclo ligado a indicadores; plan de reconversión hacia supervisión de agentes e ingeniería de detección |

---

## 13. Riesgos, límites y dependencias

| Tema | Detalle |
|---|---|
| Disponibilidad de producto | Varias capacidades clave están en Preview. El plan no debe depender de ellas hasta que sean GA |
| Cifras del fabricante | Los porcentajes de eficacia son agregados de Microsoft, sin verificación independiente |
| Hoja de ruta sin fuente escrita | Los agentes futuros de hunting e ingeniería inversa, el aprendizaje compartido y las novedades de Purview de enero de 2027 deben confirmarse en fuentes públicas |
| Marcos en borrador | El perfil de NIST y la guía de CSA pueden cambiar; la guía de CSA figura como borrador en su espacio de laboratorio |
| The Open Group | No se halló publicación específica; la ausencia puede deberse al alcance de la búsqueda |
| Lectura parcial de fuentes | Parte del análisis se apoya en resúmenes ejecutivos y fichas, no en el texto completo |
| Régimen regulatorio | No investigado; condiciona la sección 9.3 |
| Datos del holding | Licencias, tenants, cobertura OT y herramientas no Microsoft no relevados |
| Dependencia del proveedor | Concentrar plataforma, agentes y modelos en un proveedor reduce fricción y aumenta dependencia; conviene evaluarlo de forma explícita |
| Costo por consumo | Sin referencia de precio por caso en las fuentes revisadas |

---

## 14. Fuentes

### Microsoft

| ID | Fuente | URL |
|---|---|---|
| M1 | Security for the agentic era, powered by Microsoft Perception (17-nov-2026) | https://www.microsoft.com/en-us/security/blog/2026/11/17/security-for-the-agentic-era-powered-by-microsoft-perception/ |
| M2 | What's new with Microsoft Perception at Ignite 2026 (17-nov-2026) | https://techcommunity.microsoft.com/blog/perception-blog/whats-new-with-microsoft-perception-at-ignite-2026/4571834 |
| M3 | Ignite 2026: What's new in Microsoft Defender & Sentinel (17-nov-2026) | https://techcommunity.microsoft.com/blog/microsoftthreatprotectionblog/ignite-2026-whats-new-in-microsoft-defender--sentinel/4569975 |
| M4 | Ignite 2026: What's new in Microsoft Sentinel (17-nov-2026) | https://techcommunity.microsoft.com/blog/microsoftsentinelblog/ignite-2026-whats-new-in-microsoft-sentinel/4571174 |
| M5 | The agentic SOC: Rethinking SecOps for the next decade (9-abr-2026) | https://www.microsoft.com/en-us/security/blog/2026/04/09/the-agentic-soc-rethinking-secops-for-the-next-decade/ |
| M6 | Whitepaper: Agentic SecOps, A New SOC Operating Model | https://marketingassets.microsoft.com/gdc/gdc46cegG/original |
| M7 | Reimagining the SOC for the agentic era in Microsoft Defender (23-sep-2026) | https://www.microsoft.com/en-us/security/blog/2026/09/23/reimagining-the-soc-for-the-agentic-era-in-microsoft-defender/ |
| M8 | Rethinking security for the age of AI (27-jul-2026) | https://blogs.microsoft.com/blog/2026/07/27/rethinking-security-for-the-age-of-ai/ |
| M9 | What is Perception? (Microsoft Learn) | https://learn.microsoft.com/en-us/security/agentic-security/agentic-security-overview |
| M10 | Agent categories in Perception (Microsoft Learn) | https://learn.microsoft.com/en-us/security/agentic-security/agentic-security-agent-categories |
| M11 | Microsoft Perception, página de producto | https://www.microsoft.com/en-us/security/business/microsoft-perception-agentic-system |
| M12 | Security Copilot in Defender: assistive and autonomous AI (20-mar-2026) | https://techcommunity.microsoft.com/blog/microsoftthreatprotectionblog/security-copilot-in-defender-empowering-the-soc-with-assistive-and-autonomous-ai/4503047 |
| M13 | Security Copilot for SOC: bringing agentic AI to every defender (18-nov-2025) | https://techcommunity.microsoft.com/blog/microsoftthreatprotectionblog/security-copilot-for-soc-bringing-agentic-ai-to-every-defender/4470187 |
| M14 | Microsoft unveils Security Copilot agents (24-mar-2025) | https://www.microsoft.com/en-us/security/blog/2025/03/24/microsoft-unveils-microsoft-security-copilot-agents-and-new-protections-for-ai/ |
| M15 | Deploy AI agents in Microsoft Defender (Microsoft Learn) | https://learn.microsoft.com/en-us/defender-xdr/security-copilot-agents-defender |
| M16 | Microsoft Perception helps IT drive outcomes and scale (17-nov-2026) | https://techcommunity.microsoft.com/blog/IntuneCustomerSuccess/microsoft-perception-helps-it-drive-outcomes-and-scale/4573285 |
| M17 | MAI Cyber 2 Flash (17-nov-2026) | https://microsoft.ai/news/introducing-mai-cyber-2-flash/ |
| M18 | Getting started with Codename MDASH (Microsoft Learn) | https://learn.microsoft.com/en-us/security-exposure-management/ai-code-security-onboarding |
| M19 | Microsoft Sentinel MCP, conector (Microsoft Learn) | https://learn.microsoft.com/en-us/connectors/sentinelmcp/ |
| M20 | Announcing Zero Trust for AI (19-mar-2026) | https://www.microsoft.com/en-us/security/blog/2026/03/19/new-tools-and-guidance-announcing-zero-trust-for-ai/ |
| M21 | Microsoft Ignite 2026 Book of News | https://news.microsoft.com/events/ignite/2026/book-of-news/ |
| M22 | Documentación de Perception (Microsoft Learn) | https://learn.microsoft.com/en-us/security/agentic-security/ |
| M23 | Microsoft Security Copilot, sitio de adopción | https://adoption.microsoft.com/en-us/security-copilot/ |
| M24 | Security Copilot agents in Defender XDR: where things actually stand (abr-2026). Discusión de la comunidad, no oficial | https://techcommunity.microsoft.com/discussions/microsoft-security/security-copilot-agents-in-defender-xdr-where-things-actually-stand/4514689 |
| M25 | Recaps independientes de Ignite 2026 (Perception y Sentinel). Fuente secundaria | https://ignite2026.recapped.fi/a/whats-new-with-microsoft-perception-at-ignite-2026/ y https://ignite2026.recapped.fi/a/ignite-2026-whats-new-in-microsoft-sentinel/ |

### NIST

| ID | Fuente | URL |
|---|---|---|
| N1 | SP 800-61 Rev. 3, Incident Response Recommendations and Considerations (abr-2025) | https://csrc.nist.gov/pubs/sp/800/61/r3/final |
| N2 | IR 8596, Cyber AI Profile, borrador preliminar (dic-2025) | https://csrc.nist.gov/pubs/ir/8596/iprd |
| N3 | IR 8607, resumen del taller del Cyber AI Profile (ago-2026) | https://www.nist.gov/publications/workshop-summary-report-cyber-ai-profile-hybrid-workshop |
| N4 | Proyecto de overlays de SP 800-53 para sistemas de IA | https://csrc.nist.gov/projects/cosis |
| N5 | AI Agent Standards Initiative | https://www.nist.gov/artificial-intelligence/ai-agent-standards-initiative |
| N6 | Draft NIST Guidelines Rethink Cybersecurity for the AI Era (16-dic-2025) | https://www.nist.gov/news-events/news/2025/12/draft-nist-guidelines-rethink-cybersecurity-ai-era |
| N7 | Análisis de IR 8596 por Skylight Cyber (mar-2026). Fuente secundaria | https://skylightcyber.com/2026/03/16/nist-ai-security/ |

### Cloud Security Alliance

| ID | Fuente | URL |
|---|---|---|
| C1 | Agentic Cybersecurity Implementation Guide, borrador (27-mar-2026) | https://labs.cloudsecurityalliance.org/agentic/agentic-cybersecurity-implementation-guide-v1/ |
| C2 | Securing the Agentic Control Plane, programa 2026 | https://labs.cloudsecurityalliance.org/agentic/ |
| C3 | Secure Agentic System Design: A Trait-Based Approach | https://cloudsecurityalliance.org/artifacts/secure-agentic-system-design |
| C4 | Agentic AI Identity and Access Management: A New Approach | https://cloudsecurityalliance.org/artifacts/agentic-ai-identity-and-access-management-a-new-approach |
| C5 | Cloud Security Alliance Expands Agentic AI Governance Work (6-may-2026). Fuente secundaria | https://thejournal.com/articles/2026/05/06/cloud-security-alliance-expands-agentic-ai-governance-work.aspx |
| C6 | Nota de investigación de CSA sobre la iniciativa de NIST (30-mar-2026) | https://labs.cloudsecurityalliance.org/research/csa-research-note-nist-ai-agent-standards-federal-framework/ |

### Center for Internet Security

| ID | Fuente | URL |
|---|---|---|
| I1 | AI Agents Companion Guide, CIS Controls v8.1 (20-abr-2026) | https://www.cisecurity.org/insights/white-papers/controls-v8-1-ai-agents-companion-guide |
| I2 | CIS Controls v8.1 AI Security Guidance Workbook (27-jul-2026) | https://www.cisecurity.org/insights/white-papers/controls-v8-1-2-ai-security-guidance-workbook |
| I3 | Análisis de la guía MCP de CIS por Cequence (abr-2026). Fuente secundaria | https://www.cequence.ai/blog/cis-mcp-companion-guide-enterprise-ai-agent-governance |
| I4 | Reseña de la AI Agents Companion Guide de CIS (jul-2026). Fuente secundaria, usada para los conceptos de capa de aplicación de políticas e interruptor de parada | https://www.linkedin.com/pulse/new-cis-ai-agents-companion-guide-april-2026-chandra-mouli-y9xtc |

### The Open Group

| ID | Fuente | URL |
|---|---|---|
| O1 | Zero Trust, Security Forum | https://www.opengroup.org/forum/security/Zerotrust |
| O2 | Zero Trust Architecture Working Group | https://www.opengroup.org/forum/security-forum-0/zerotrustsecurityarchitecture |
| O3 | Security and Zero Trust at The Open Group, artículo de Mark Simos (ago-2025). Fuente secundaria | https://www.linkedin.com/pulse/security-zero-trust-open-group-mark-simos-vc7fe/ |
| O4 | Security Forum Members' Meeting, Houston 2024 | https://www.opengroup.org/Houston-2024-10/Security |

**Referencias estándar no recuperadas en esta sesión:** NIST Cybersecurity Framework 2.0 y Microsoft Security Adoption Framework. Se usaron como marco general; conviene agregar sus URL oficiales al cerrar la versión 1.1.

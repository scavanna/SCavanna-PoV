# Nivel 4 · SOC agéntico · Del SOC tradicional al SOC agéntico

*Microsoft Security Copilot Ninja Training: hacia el SOC agéntico · Edición 2026*

[← Nivel 3 · Avanzado](03_Nivel_3_Avanzado.md) · [Índice del programa](README.md) · [Comunidad →](05_Comunidad.md)

<a id="agentes"></a>

Modelo operativo del SOC agéntico, casos de uso y retorno, seguridad de la IA y de los agentes, y operación de un parque de agentes. Terminas con un proyecto integrador y una hoja de ruta defendible ante el comité.

*L300–L400 · 5 módulos · ~31 horas · 63 recursos*

**Módulos de este nivel:** [X1 Hacia el SOC agéntico](#x1) · [X2 Casos de uso, métricas y ROI](#x2) · [X3 Seguridad de IA y agentes](#x3) · [X4 Operar un parque de agentes](#x4) · [X5 Proyecto integrador](#x5)

<a id="x1"></a>

## X1 · Del SOC tradicional al SOC agéntico

*L300–L400 · ~4 h · Origen: Nuevo en esta edición*

El cuello de botella del SOC ya no es detectar, sino la capacidad de atender: el libro blanco de Microsoft sobre SecOps agéntico estima que el 42 % de las alertas queda sin investigar y que los analistas dedican más del 20 % de su tiempo a juntar datos. Microsoft describe el **SOC agéntico** en dos capas —una disrupción determinista que contiene ataques en minutos y agentes supervisados que absorben el trabajo repetitivo— y en tres etapas: **SOC 1**, unificar la plataforma; **SOC 2**, IA generativa y agentes de tarea; **SOC 3**, automatización agéntica de punta a punta.

Las piezas ya existen: el portal de Defender con Sentinel y el **Integrated SOC (ISOC)** como base de señales, contexto y actuadores; Security Copilot como la IA que asiste; los agentes de Microsoft, de partners y propios para tareas concretas; y **Project Perception** como la IA que actúa, con playbooks predefinidos, aprobaciones humanas (aprobar, rechazar, sugerir una alternativa o detener) y sesiones que quedan como registro inmutable de auditoría. Lo que no viene en la caja es el **modelo operativo**: qué decide un agente, qué aprueba una persona, cómo se gana la confianza y cómo cambian los roles.

Este módulo te ayuda a ubicar tu SOC en el [modelo de madurez](00_Programa.md#madurez-soc-agentico) y a diseñar la matriz de autonomía. Las prácticas de excelencia del SOC —procesos, métricas y gobierno— se profundizan en el track de excelencia del programa de Defender XDR (módulos S1 a S7).

**Por qué importa**

Sumar analistas no escala al ritmo de las alertas. Un modelo operativo explícito —qué hacen los agentes, qué aprueban las personas y con qué evidencia se amplía la autonomía— es lo que permite capturar el valor sin perder el control, y es lo que preguntarán el directorio, el auditor y el regulador.

**Qué vas a lograr**

- Explicar el modelo de Microsoft: dos capas y tres etapas (SOC 1, SOC 2 y SOC 3).
- Ubicar tu SOC en el modelo de madurez de esta guía con evidencia por dimensión.
- Diseñar una matriz de autonomía por tipo de acción con humano en el circuito.
- Describir cómo Project Perception organiza el trabajo agéntico: playbooks, aprobaciones y sesiones auditables.
- Redefinir los roles del SOC alrededor de la supervisión y la ingeniería de agentes.

> **Novedad.** El 9 de abril de 2026 Microsoft publicó su visión del SOC agéntico: dos capas —disrupción determinista y agentes supervisados— y tres etapas (SOC 1, SOC 2 y SOC 3). Según Microsoft, sus agentes internos automatizan el 75 % de las investigaciones de phishing y malware, y la disrupción de ataques detiene un ransomware en unos 3 minutos con un 99,99 % de confianza ([el SOC agéntico](https://www.microsoft.com/en-us/security/blog/2026/04/09/the-agentic-soc-rethinking-secops-for-the-next-decade/)).

> **Novedad.** El 23 de septiembre de 2026 Microsoft anunció el Integrated SOC (ISOC) en Defender como base de señales, contexto y actuadores para personas y agentes ([ISOC](https://www.microsoft.com/en-us/security/blog/2026/09/23/reimagining-the-soc-for-the-agentic-era-in-microsoft-defender/)). La documentación de Perception, actualizada el 30 de octubre de 2026, aclara que los playbooks los define Microsoft (de solo lectura en esta versión) y que cada agente requiere una identidad de Entra Agent ID y un rol ([conceptos de Perception](https://learn.microsoft.com/en-us/security/agentic-security/agentic-security-concepts)).

> **Atención.** Las cifras del SOC interno de Microsoft y las del libro blanco (42 % de alertas sin investigar y más del 20 % del tiempo de los analistas dedicado a juntar datos) son referencias, no promesas: tu modelo operativo debe apoyarse en tu propia línea base ([Agentic SecOps](https://marketingassets.microsoft.com/gdc/gdc46cegG/original)).

> **Consejo Ninja.** En Perception, el humano en el circuito tiene forma concreta: el estado Waiting for input, las opciones de aprobar, rechazar o sugerir una alternativa y la detención de la sesión, que es irreversible; las sesiones quedan como registro inmutable de auditoría ([supervisar el trabajo agéntico](https://learn.microsoft.com/en-us/security/agentic-security/agentic-security-supervise-work), [Application card de Perception](https://learn.microsoft.com/en-us/security/agentic-security/agentic-security-application-card)). Las prácticas de excelencia del SOC se profundizan en el programa de Defender XDR (módulos S1 a S7).

**¿Tienes poco tiempo?**

- [The agentic SOC—Rethinking SecOps for the next decade](https://www.microsoft.com/en-us/security/blog/2026/04/09/the-agentic-soc-rethinking-secops-for-the-next-decade/) · Blog oficial
- [Agentic SecOps: A New SOC Operating Model (whitepaper)](https://marketingassets.microsoft.com/gdc/gdc46cegG/original) · Libro
- [What is Perception?](https://learn.microsoft.com/en-us/security/agentic-security/agentic-security-overview) · Documentación

**Matriz de autonomía de referencia para agentes del SOC**

| Acción del agente | Riesgo si se equivoca | Reversibilidad | Autonomía sugerida para empezar | Control y evidencia |
|---|---|---|---|---|
| Resumir un incidente o una alerta | Bajo: una lectura equivocada | Total | Ejecuta y reporta | Muestreo semanal de calidad |
| Enriquecer un incidente con inteligencia | Bajo | Total | Ejecuta y reporta | Fuentes citadas en el comentario |
| Clasificar una alerta como verdadero o falso positivo | Medio: un ataque clasificado como benigno | Alta si se revisa a tiempo | Propone; el analista confirma hasta medir la precisión | Precisión y falsos negativos por semana |
| Cerrar una alerta benigna | Medio a alto: se pierde un ataque real | Media: se puede reabrir | Ejecuta con aprobación; luego ejecuta y reporta solo en categorías con precisión probada | Revisión por muestreo y feedback registrado |
| Generar KQL o proponer una detección | Medio: ruido o puntos ciegos | Total mientras no se guarde | Propone; una persona guarda la detección | Revisión de pares antes de activar |
| Bloquear un indicador (IP, URL o hash) | Alto: impacto en el negocio | Alta, con impacto mientras dura | Ejecuta con aprobación | Aprobación registrada y caducidad del bloqueo |
| Aislar un dispositivo o deshabilitar un usuario | Alto: interrupción de la operación | Media | Ejecuta con aprobación y nunca sobre activos o cuentas críticas | Lista de exclusiones y reversión probada |
| Cambiar políticas (acceso condicional o DLP) | Muy alto: bloqueos masivos o brechas de cobertura | Media | Solo propone, en modo solo informe | Control de cambios y análisis de impacto |

Propuesta de esta guía basada en [supervisar el trabajo agéntico](https://learn.microsoft.com/en-us/security/agentic-security/agentic-security-supervise-work), la [Application card de los agentes](https://learn.microsoft.com/en-us/copilot/security/security-copilot-application-card-agents) y [el SOC agéntico](https://www.microsoft.com/en-us/security/blog/2026/04/09/the-agentic-soc-rethinking-secops-for-the-next-decade/). Ajusta cada fila a tu apetito de riesgo.

### Documentación, cursos y credenciales

- [What is Perception?](https://learn.microsoft.com/en-us/security/agentic-security/agentic-security-overview) · Documentación · Oficial · Vista previa · Nuevo · Microsoft Learn · 30 oct 2026. Visión general de Perception: configurar agentes, delegar trabajo con playbooks o chat y supervisar sesiones aprobando, rechazando o deteniendo acciones. *Nota:* Navegación en Defender: New Chat, Sessions, Agents, Playbooks, Insights
- [Project Perception | Microsoft Security](https://www.microsoft.com/en-us/security/business/ai-powered-cybersecurity/project-perception-agentic-system) · Documentación · Oficial · Vista previa · Nuevo · Microsoft Security · jul 2026. Página de producto que distingue Project Perception (sistema agéntico: 'IA que actúa') de Security Copilot (interfaz de chat asistida: 'IA que asiste'), indica que arranca en Microsoft Defender y se factura por consumo en SCU. *Nota:* Precio por consumo (pago por uso) con tasas distintas por agente; se lanza dentro de Microsoft Defender
- [Key concepts in Perception](https://learn.microsoft.com/en-us/security/agentic-security/agentic-security-concepts) · Documentación · Oficial · Vista previa · Microsoft Learn. Conceptos de Project Perception: sesiones, agentes (Recon, Triage, Threat Intelligence, Attack Investigation, Detection Authoring, Posture Prioritization) y playbooks multiagente. *Nota:* Perception está en Limited Public Preview por invitación; playbooks predefinidos por Microsoft y de solo lectura
- [Approve, reject, or stop agentic work (Project Perception)](https://learn.microsoft.com/en-us/security/agentic-security/agentic-security-supervise-work) · Documentación · Oficial · Vista previa · Microsoft Learn. Cómo supervisar sesiones agénticas: estado 'Waiting for input', aprobar, rechazar o sugerir alternativas y detener sesiones de forma irreversible. *Nota:* Base del modelo humano-en-el-circuito para acciones de alto impacto (p. ej., deshabilitar cuentas o aislar dispositivos)

### Anuncios y blogs oficiales

- [Reimagining the SOC for the agentic era in Microsoft Defender](https://www.microsoft.com/en-us/security/blog/2026/09/23/reimagining-the-soc-for-the-agentic-era-in-microsoft-defender/) · Blog oficial · Empleado de Microsoft · Nuevo · Rob Lefferts · Microsoft Security Blog · 23 sep 2026. Anuncia el ISOC (integrated SOC) en Microsoft Defender, que une SIEM y protección como base para que agentes y personas operen con el mismo contexto.
- [The agentic SOC—Rethinking SecOps for the next decade](https://www.microsoft.com/en-us/security/blog/2026/04/09/the-agentic-soc-rethinking-secops-for-the-next-decade/) · Blog oficial · Empleado de Microsoft · Rob Lefferts; David Weston · Microsoft Security Blog · 9 abr 2026. Define el SOC agéntico en dos capas (disrupción determinista + agentes que razonan) y enlaza al whitepaper 'The agentic SOC: Your teammate for tomorrow, today'.
- [The Agentic SOC Era: How Sentinel MCP Enables Autonomous Security Reasoning](https://techcommunity.microsoft.com/blog/microsoftsentinelblog/the-agentic-soc-era-how-sentinel-mcp-enables-autonomous-security-reasoning/4491003) · Blog oficial · Empleado de Microsoft · Iftekhar Hussain · Microsoft Sentinel Blog · 3 feb 2026. Ejemplos prácticos de razonamiento agéntico con el MCP de Sentinel en VS Code (p. ej. service principals inactivos reactivados) sobre datos de larga retención.
- [Microsoft named an overall leader in KuppingerCole Analyst's 2026 Emerging AI SOC report](https://www.microsoft.com/en-us/security/blog/2026/05/06/microsoft-named-an-overall-leader-in-kuppingercole-analysts-2026-emerging-ai-security-operations-center-soc-report/) · Blog oficial · Empleado de Microsoft · Nuevo · Rob Lefferts · Microsoft Security Blog · 6 may 2026. Resume la transición de SOAR basado en playbooks a automatización guiada por inteligencia (disrupción, agente de phishing, priorización ML, generador de playbooks) hacia el SOC agéntico.

### Comunidad: blogs, libros, newsletters y eventos

- [Agentic SecOps: A New SOC Operating Model (whitepaper)](https://marketingassets.microsoft.com/gdc/gdc46cegG/original) · Libro · Oficial · Microsoft Security · feb 2026. Libro blanco con el imperativo agéntico, las tres etapas de madurez del SOC agéntico, el modelo operativo humano-agente y cómo elegir la ruta de adopción.
- [Agentic SOC: The new operating model for continuous defense (whitepaper)](https://marketingassets.microsoft.com/adobe/assets/urn:aaid:aem:cabe0317-d0d3-4816-b046-c981c4b58132/original/as/Whitepaper-Agentic-SOC-The-new-operating-model.pdf) · Libro · Empleado de Microsoft · David Weston (prólogo) · Microsoft Security. Segundo libro blanco que propone medir el SOC por riesgo eliminado y no por alertas procesadas, y rediseñar roles (p. ej. Frontier Security Engineer) alrededor de agentes.

**Manos a la obra**

1. `Laboratorio` Ubica tu SOC en el [modelo de madurez del SOC agéntico](00_Programa.md#madurez-soc-agentico): nivel actual, estado de cada dimensión con su evidencia y siguiente paso con dueño y fecha. Evidencia: evaluación de madurez firmada por el líder del SOC.
2. `Laboratorio` Completa la matriz de autonomía de este módulo para quince acciones de tu SOC (clasificar una alerta, cerrar un falso positivo, aislar un dispositivo, deshabilitar un usuario, bloquear un indicador o crear una detección, entre otras) y justifica cada nivel con su riesgo y su reversibilidad ([supervisar el trabajo agéntico](https://learn.microsoft.com/en-us/security/agentic-security/agentic-security-supervise-work)). Evidencia: matriz de autonomía aprobada.
3. `Laboratorio` Lee [el SOC agéntico](https://www.microsoft.com/en-us/security/blog/2026/04/09/the-agentic-soc-rethinking-secops-for-the-next-decade/) y el libro blanco [Agentic SOC: the new operating model](https://marketingassets.microsoft.com/adobe/assets/urn:aaid:aem:cabe0317-d0d3-4816-b046-c981c4b58132/original/as/Whitepaper-Agentic-SOC-The-new-operating-model.pdf); extrae cinco afirmaciones y clasifícalas en «dato interno de Microsoft», «proyección» o «a medir en mi SOC». Evidencia: tabla de afirmaciones clasificadas.
4. `Laboratorio` Rediseña los roles del SOC: asigna a cada rol actual sus responsabilidades nuevas (supervisión de agentes, ingeniería de agentes, dueño de caso de uso) y la ruta de formación de esta guía que le corresponde ([rutas por rol](00_Programa.md#rutas)). Evidencia: matriz RACI del SOC agéntico.
5. `Solo producción` Supervisa una sesión de Project Perception si tu tenant participa en la vista previa ([qué es Perception](https://learn.microsoft.com/en-us/security/agentic-security/agentic-security-overview)). Cómo hacerlo seguro: incidentes de prueba o ya cerrados, roles de ejecución restringidos, rechazo de toda acción de contención sobre activos productivos y detención de cualquier sesión dudosa. Evidencia: sesión revisada con cada decisión y su justificación.

**¿Quieres profundizar?**

- [Agentic SOC: The new operating model for continuous defense (whitepaper)](https://marketingassets.microsoft.com/adobe/assets/urn:aaid:aem:cabe0317-d0d3-4816-b046-c981c4b58132/original/as/Whitepaper-Agentic-SOC-The-new-operating-model.pdf) · Libro

<a id="x2"></a>

## X2 · Casos de uso, métricas de valor y ROI

*L300–L400 · ~4 h · Origen: Nuevo en esta edición*

El valor de la IA en el SOC se mide, no se declara. La evidencia pública es prometedora y de distinta calidad: un **ensayo controlado aleatorizado** con 167 analistas midió hasta 6,5 veces más verdaderos positivos por minuto con el agente de triage de phishing, y atribuyó el 83 % de la ganancia a la priorización de la cola; un **estudio observacional** de más de 150 organizaciones asoció la adopción de Security Copilot con un MTTR 30,13 % menor a los tres meses; y los estudios **Total Economic Impact** de Forrester son proyecciones basadas en entrevistas y modelos.

Ninguna de esas cifras reemplaza tu propia **línea base**. Este módulo te enseña a medir antes y después con el mismo tipo de casos —MTTA, MTTR, tiempo de triage, tasa de falsos positivos y horas de analista—, a poner el costo en SCU de cada caso de uso en la misma tabla (pool de E5/E7, capacidad aprovisionada o excedente) y a convertir todo en un caso de negocio que un comité pueda aprobar o rechazar con datos. La [tabla de casos de uso](00_Programa.md#casos-de-uso) es tu punto de partida.

**Por qué importa**

Sin línea base, cualquier piloto de IA termina en opiniones. Un caso de negocio con MTTA, MTTR, tiempo de triage, falsos positivos y SCU por caso medidos es lo que sostiene el presupuesto, justifica ampliar un agente que funciona y, con la misma honestidad, apagar uno que no aporta.

**Qué vas a lograr**

- Distinguir tipos de evidencia (ensayo controlado, estudio observacional y estudio proyectado) y sus límites.
- Definir la línea base y la medición posterior de MTTA, MTTR, tiempo de triage, falsos positivos y horas de analista.
- Calcular el costo por caso de uso en SCU con el pool de E5/E7 o con capacidad aprovisionada.
- Construir un caso de negocio defendible ante el comité.

> **Novedad.** El ensayo controlado aleatorizado del agente de triage de phishing (167 analistas) midió hasta 6,5 veces más verdaderos positivos por minuto de analista, un 77 % más de exactitud (F1) y un 53 % más de tiempo dedicado a correos maliciosos; el 83 % de la ganancia vino de priorizar la cola, sobre una base de 11,88 % de correos maliciosos ([ensayo controlado](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/security/randomized-controlled-trial-for-phishing-triage-agent-accessible.pdf), [versión en arXiv](https://arxiv.org/html/2511.13860)).

> **Atención.** No todas las cifras valen lo mismo. El −30,13 % de MTTR a los tres meses viene de un estudio observacional de más de 150 organizaciones: asociación, no causalidad ([operaciones reales](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/final/en-us/microsoft-brand/documents/Generative-AI-and-Security-Operations-Center-Productivity-Evidence-from-Live-Operations_v2.5-FINAL.pdf)). El estudio de Forrester de noviembre de 2024 es una proyección —ROI de 99 % a 348 % y VPN de 0,5 a 1,8 millones de USD para un SOC de 20 personas— ([TEI de Security Copilot](https://tei.forrester.com/go/Microsoft/SecurityCopilot/)). Y las métricas de RSAC 2026, como un triage hasta 78 % más rápido o las más de 200 horas al mes que ahorra St. Luke's, las informa el equipo de producto ([blog de Security Copilot](https://techcommunity.microsoft.com/t5/s/gxcuf89792/rss/board?board.id=SecurityCopilotBlog)).

> **Consejo Ninja.** Para el costo usa precios de lista y tu pool: 4 USD por SCU aprovisionada y hora, 6 USD por SCU de excedente y, con E5/E7, 400 SCU al mes por cada 1.000 licencias pagas, hasta 10.000 ([precios](https://www.microsoft.com/en-us/security/pricing/microsoft-security-copilot/)). El estudio de Forrester de abril de 2026 (ROI de 124 %) mide la plataforma de seguridad de Microsoft completa, no solo Security Copilot ([TEI de Microsoft Security](https://tei.forrester.com/go/Microsoft/SecuritySolutions/?lang=en-us)).

**¿Tienes poco tiempo?**

- [Randomized Controlled Trial for Phishing Triage Agent](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/security/randomized-controlled-trial-for-phishing-triage-agent-accessible.pdf) · Libro
- [Generative AI and Security Operations Center Productivity: Evidence from Live Operations](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/final/en-us/microsoft-brand/documents/Generative-AI-and-Security-Operations-Center-Productivity-Evidence-from-Live-Operations_v2.5-FINAL.pdf) · Libro
- [New Technology: The Projected Total Economic Impact™ Of Microsoft Security Copilot (Forrester)](https://tei.forrester.com/go/Microsoft/SecurityCopilot/) · Libro

### Documentación, cursos y credenciales

- [Microsoft Security Copilot – Pricing](https://www.microsoft.com/en-us/security/pricing/microsoft-security-copilot/) · Documentación · Oficial · Microsoft Security. Página oficial de precios: SCU aprovisionada a 4 USD/hora y SCU de overage a 6 USD/hora (precios de lista estimados), con FAQ sobre la inclusión en E5/E7 y la calculadora de capacidad.

### Anuncios y blogs oficiales

- [Learn what generative AI can do for your security operations center (SOC)](https://www.microsoft.com/en-us/security/blog/2025/11/04/learn-what-generative-ai-can-do-for-your-security-operations-center-soc/) · Blog oficial · Empleado de Microsoft · Rob Lefferts · Microsoft Security Blog · 4 nov 2025. Presenta el e-book 'From Alert Fatigue to Proactive Defense' con escenarios de investigación, análisis, caza e informes y cita la reducción del 30% del MTTR.

### Webinars, videos y podcasts

- [From Alert to Resolution: Using Security Agents to Power Real-World SOC Workflows](https://www.youtube.com/watch?v=7exfnonnk5o) · Webinar · Empleado de Microsoft · Pablo Chacon; Ankur Arora; Ugur Koc; Konrad Sagala · YouTube - Microsoft Security Community · 25 feb 2026. Demostraciones de agentes del Security Store en tres casos de uso SOC típicos (phishing, toma de cuenta y BEC) de la alerta a la remediación.

### Comunidad: blogs, libros, newsletters y eventos

- [Randomized Controlled Trial for Phishing Triage Agent](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/security/randomized-controlled-trial-for-phishing-triage-agent-accessible.pdf) · Libro · Empleado de Microsoft · James Bono · Microsoft · oct 2025. Ensayo controlado con 167 analistas: con el agente de triage de phishing se detectan hasta 6,5 veces más verdaderos positivos por minuto y la exactitud (F1) mejora hasta 77%.
- [Generative AI and Security Operations Center Productivity: Evidence from Live Operations](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/final/en-us/microsoft-brand/documents/Generative-AI-and-Security-Operations-Center-Productivity-Evidence-from-Live-Operations_v2.5-FINAL.pdf) · Libro · Empleado de Microsoft · Legado aún útil · James Bono; Justin Grana; Alec Xu · Microsoft · nov 2024. Estudio observacional en más de 150 organizaciones que asocia la adopción de Security Copilot con una reducción del 30,13% del MTTR de incidentes a los tres meses. *Nota:* Correlacional (no causal); sigue siendo la principal evidencia en operaciones reales; publicado como 'Copilot' antes de los agentes
- [New Technology: The Projected Total Economic Impact™ Of Microsoft Security Copilot (Forrester)](https://tei.forrester.com/go/Microsoft/SecurityCopilot/) · Libro · Comunidad · Legado aún útil · Kris Peterson (Forrester) · Forrester Consulting · nov 2024. Estudio TEI encargado por Microsoft que proyecta un ROI de 99% a 348%, VPN de 0,5 a 1,8 M USD y ganancias de productividad de 23% a 46,7% para un SOC de 20 personas. *Nota:* Proyección (New Technology TEI) basada en 4 entrevistas y encuesta a 307 decisores; anterior a agentes e inclusión en E5
- [The Total Economic Impact™ Of Microsoft Security (Forrester, abril 2026)](https://tei.forrester.com/go/Microsoft/SecuritySolutions/?lang=en-us) · Libro · Comunidad · Forrester · Forrester Consulting · abr 2026. TEI de la plataforma de seguridad de Microsoft (no solo Copilot) con ROI de 124% y VPN de 16,6 M USD, útil para enmarcar el caso de negocio del SOC agéntico.
- [Randomized Controlled Trials for Phishing Triage Agent (arXiv 2511.13860)](https://arxiv.org/html/2511.13860) · Libro · Empleado de Microsoft · James Bono (Microsoft) · arXiv · 17 nov 2025. Versión académica abierta del ensayo controlado del agente de triage de phishing con metodología y resultados detallados.

**Manos a la obra**

1. `Laboratorio` Lee el [ensayo controlado](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/security/randomized-controlled-trial-for-phishing-triage-agent-accessible.pdf) y el [estudio de operaciones reales](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/final/en-us/microsoft-brand/documents/Generative-AI-and-Security-Operations-Center-Productivity-Evidence-from-Live-Operations_v2.5-FINAL.pdf) y arma una tabla con diseño, muestra, métrica, resultado y limitaciones de cada uno; explica por qué el 83 % de la ganancia del ensayo vino de priorizar la cola. Evidencia: tabla comparativa de evidencia.
2. `Laboratorio parcial` Replica el diseño del ensayo a pequeña escala: dos grupos de analistas, con y sin agente, sobre el mismo lote de correos de prueba; mide verdaderos positivos por minuto, exactitud y SCU por correo. Limitación: sin volumen real la significancia es baja; en producción usa un grupo piloto y el panel de uso. Evidencia: resultados por grupo con sus limitaciones explícitas.
3. `Laboratorio` Construye el modelo de costos por caso de uso con cinco filas de la [tabla de casos de uso](00_Programa.md#casos-de-uso): volumen mensual, SCU por ejecución medidas en tus laboratorios, costo con el pool de E5/E7 o con capacidad aprovisionada ([precios](https://www.microsoft.com/en-us/security/pricing/microsoft-security-copilot/)) y horas de analista liberadas por su costo hora. Evidencia: modelo de costos por caso de uso.
4. `Solo producción` Toma cuatro semanas de línea base en producción: MTTA, MTTR, tiempo de triage, tasa de falsos positivos y horas de analista por tipo de caso, más la exportación del [panel de uso](https://learn.microsoft.com/en-us/copilot/security/manage-usage). Cómo hacerlo seguro: extracción con roles de solo lectura, sin cambiar el proceso durante la medición y con métricas agregadas por equipo, no por persona, acordadas con RR. HH. Evidencia: informe de línea base.
5. `Laboratorio` Escribe el caso de negocio en una página: hipótesis de valor, métricas y cómo se medirán, costo, riesgos, controles y la decisión que pides al comité; pide a un par que haga de abogado del diablo ([TEI de Security Copilot](https://tei.forrester.com/go/Microsoft/SecurityCopilot/)). Evidencia: caso de negocio revisado.

**¿Quieres profundizar?**

- [From Alert to Resolution: Using Security Agents to Power Real-World SOC Workflows](https://www.youtube.com/watch?v=7exfnonnk5o) · Webinar
- [The Total Economic Impact™ Of Microsoft Security (Forrester, abril 2026)](https://tei.forrester.com/go/Microsoft/SecuritySolutions/?lang=en-us) · Libro

<a id="x3"></a>

## X3 · Seguridad de la IA y de los agentes

*L300–L400 · ~6 h · Origen: Nuevo en esta edición*

Los agentes del SOC tienen acceso privilegiado a lo más sensible —incidentes, identidades, correos y vulnerabilidades—, por eso son un blanco atractivo. La **taxonomía de modos de fallo de sistemas agénticos** del AI Red Team de Microsoft (versión 2, abril de 2026) suma riesgos como el abuso de MCP y plugins y la escalada de confianza entre agentes; en 2025 se registraron 99 CVE relacionadas con MCP. Un caso documentado de envenenamiento de descripciones de herramientas MCP en Copilot Studio muestra que la **inyección indirecta de prompts (XPIA)** ya no es teórica: un correo que tu agente de triage lee puede traer instrucciones escondidas.

Las defensas se apilan en capas. **Identidad**: Microsoft Entra Agent ID —sin credenciales propias, de un solo tenant y con un sponsor humano— y **Agent 365** para extender acceso condicional e ID Protection a los agentes. **Datos**: Purview, con DSPM for AI para ver la postura de los datos que usan las aplicaciones y los agentes de IA (su versión clásica se está reemplazando por la nueva experiencia DSPM); para agentes de Security Copilot aplica clasificación y para los de Copilot Studio y Foundry, además, etiquetas, DLP y riesgo interno. **Ejecución**: la protección en tiempo real de Defender, la detección de amenazas para agentes y Defender for Endpoint para agentes locales, en vista previa. **Postura**: el Security Dashboard for AI. El programa de Entra (módulos X2 a X4) y el de Purview DSPM profundizan cada capa.

**Por qué importa**

Un agente secuestrado por una inyección indirecta actúa con sus permisos y su reputación de confianza: es un insider nuevo. Modelar las amenazas de cada agente y mapear controles por capa es lo que permite ampliar la autonomía sin abrir una puerta trasera en el propio SOC.

**Qué vas a lograr**

- Describir los modos de fallo de los sistemas agénticos y los riesgos propios de MCP y de los plugins.
- Modelar las amenazas de un agente del SOC: entradas, herramientas, identidad, datos y salidas.
- Aplicar Entra Agent ID, Agent 365, Purview (incluido DSPM for AI) y Defender como capas de control.
- Detectar y responder a ataques contra agentes con las alertas y tablas de Defender.

> **Novedad.** La versión 2 de la taxonomía de modos de fallo de sistemas agénticos (abril de 2026) suma riesgos como el abuso de MCP y de plugins y la escalada de confianza entre agentes, y registra 99 CVE relacionadas con MCP en 2025 ([taxonomía v2](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/security/Taxonomy-of-Failure-Modes-in-Agentic-AI-Systems-v2-0.pdf), [lo que enseñó un año de red teaming](https://www.microsoft.com/en-us/security/blog/2026/06/04/updating-taxonomy-failure-modes-agentic-ai-systems-year-red-teaming-taught-us/)). Un caso real de envenenamiento de descripciones de herramientas MCP en Copilot Studio ilustra los riesgos ASI02 y ASI04 de OWASP para agentes ([de leer a actuar](https://www.microsoft.com/en-us/security/blog/2026/06/30/securing-ai-agents-ai-tools-move-from-reading-acting/)).

> **Atención.** Microsoft Entra Agent ID está disponible para todos los clientes de Entra, pero extender el acceso condicional e ID Protection a los agentes requiere Microsoft Agent 365, incluido en E7 y disponible como complemento para E5, A5 y Business Premium ([qué es Entra Agent ID](https://learn.microsoft.com/en-us/entra/agent-id/what-is-microsoft-entra-agent-id)). Las identidades de agente no tienen credenciales propias —las aporta el blueprint—, son de un solo tenant y pueden tener un sponsor humano ([identidades de agente](https://learn.microsoft.com/en-us/entra/agent-id/agent-identities)). Las fuentes difieren sobre la licencia de ID Protection para agentes: revísalo en [Metodología y fuentes](08_Cierre_glosario_y_fuentes.md#metodologia).

> **Novedad.** Defender protege agentes en tres frentes: la protección en tiempo real (regla por defecto en auditoría y reglas de bloqueo; Copilot Studio y Foundry en vista previa; registros en la tabla BehaviorInfo), la detección de amenazas para agentes de Foundry publicados (jailbreak, XPIA, fuga de secretos y reconocimiento de LLM, en vista previa) y la protección en tiempo de ejecución de agentes locales como Claude Code, Codex CLI o GitHub Copilot CLI con Defender for Endpoint en modo activo, también en vista previa ([tiempo real](https://learn.microsoft.com/en-us/defender-xdr/security-for-ai/ai-agent-real-time-protection), [detección](https://learn.microsoft.com/en-us/defender-xdr/security-for-ai/ai-agent-detection-protection), [agentes locales](https://learn.microsoft.com/en-us/defender-endpoint/ai-agent-runtime-protection-overview)).

> **Consejo Ninja.** En Purview, para los agentes de Security Copilot solo aplica la clasificación de datos; para los de Copilot Studio y Foundry, además, etiquetas, DLP y riesgo interno ([Purview para agentes](https://learn.microsoft.com/en-us/purview/ai-agents)). La identidad de los agentes se profundiza en el programa de Entra (módulos X2 a X4) y la seguridad de datos para IA, en el programa de Purview DSPM.

**¿Tienes poco tiempo?**

- [What is Microsoft Entra Agent ID?](https://learn.microsoft.com/en-us/entra/agent-id/what-is-microsoft-entra-agent-id) · Documentación
- [Protect AI agents in real time using Microsoft Defender](https://learn.microsoft.com/en-us/defender-xdr/security-for-ai/ai-agent-real-time-protection) · Documentación
- [Taxonomy of Failure Modes in Agentic AI Systems v2.0](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/security/Taxonomy-of-Failure-Modes-in-Agentic-AI-Systems-v2-0.pdf) · Libro
- [Securing AI agents: When AI tools move from reading to acting](https://www.microsoft.com/en-us/security/blog/2026/06/30/securing-ai-agents-ai-tools-move-from-reading-acting/) · Blog oficial

### Documentación, cursos y credenciales

- [Enable security for AI agents using Microsoft Defender](https://learn.microsoft.com/en-us/defender-xdr/security-for-ai/get-started-defender-security-for-ai) · Documentación · Oficial · Nuevo · Microsoft Learn · 30 oct 2026. Pasos de incorporación de seguridad para agentes en Defender: Agent 365, conector de Microsoft 365 y conexión de Copilot Studio para protección en tiempo real con un administrador de Power Platform.
- [What is Microsoft Entra Agent ID?](https://learn.microsoft.com/en-us/entra/agent-id/what-is-microsoft-entra-agent-id) · Documentación · Oficial · Nuevo · Microsoft Learn · 24 jun 2026. Explica Entra Agent ID como marco de identidad para agentes (blueprints, Conditional Access, Identity Protection, gobierno y registros) y su licenciamiento vía Agent 365.
- [Application card: Microsoft Security Copilot](https://learn.microsoft.com/en-us/copilot/security/security-copilot-application-card) · Documentación · Oficial · Nuevo · Microsoft Learn · 22 jun 2026. Ficha de IA responsable que reemplaza a la antigua FAQ de RAI: glosario, usos previstos, modelos (Azure OpenAI vía Foundry, sin entrenamiento con datos del cliente), limitaciones, evaluaciones, mitigaciones y buenas prácticas para desplegadores y usuarios.
- [Application card for Microsoft Security Copilot agents](https://learn.microsoft.com/en-us/copilot/security/security-copilot-application-card-agents) · Documentación · Oficial · Microsoft Learn. Tarjeta de IA responsable de los agentes: usos previstos, autonomía, limitaciones, evaluaciones y buenas prácticas de despliegue con control humano.
- [Protect AI agents in real time using Microsoft Defender](https://learn.microsoft.com/en-us/defender-xdr/security-for-ai/ai-agent-real-time-protection) · Documentación · Oficial · Microsoft Learn. Explica la protección en tiempo real de agentes (Agent 365, Copilot Studio y Foundry en preview, agentes locales vía MDE) con regla por defecto en auditoría, reglas de bloqueo y registro en BehaviorInfo.
- [Microsoft Purview data security and compliance protections for generative AI apps](https://learn.microsoft.com/en-us/purview/ai-microsoft-purview) · Documentación · Oficial · Microsoft Learn. Visión general de DSPM y DSPM for AI (clásico) y de las protecciones de Purview para Copilots, Security Copilot, Copilot Studio, Foundry y apps de IA de terceros.
- [Use Microsoft Purview to manage data security & compliance for AI agents](https://learn.microsoft.com/en-us/purview/ai-agents) · Documentación · Oficial · Nuevo · Microsoft Learn · 27 may 2026. Matriz de protección de Purview por tipo de agente (Security Copilot, Copilot Studio, Foundry, Entra-registrados, ChatGPT/Claude Enterprise).
- [Agent identities in Microsoft Entra Agent ID](https://learn.microsoft.com/en-us/entra/agent-id/agent-identities) · Documentación · Oficial · Microsoft Learn. Anatomía de una identidad de agente: sin credenciales propias, tokens vía blueprint, sponsor responsable y cuenta de usuario de agente opcional.
- [Governing Agent Identities (Microsoft Entra ID Governance)](https://learn.microsoft.com/en-us/entra/id-governance/agent-id-governance-overview) · Documentación · Oficial · Microsoft Learn. Cómo gobernar el ciclo de vida y el acceso de identidades de agentes (sponsors, paquetes de acceso, Conditional Access) y cómo Foundry y Copilot Studio las aprovisionan.
- [Copilot controls security and governance](https://learn.microsoft.com/en-us/copilot/implement/copilot-controls-security-governance) · Documentación · Oficial · Microsoft Learn. Marco de controles para Copilot y agentes de Copilot Studio que distingue controles 'foundational' (A3/E3/G3, SAM, Purview básico) y 'optimized' (A5/E5/G5, DSPM for AI, IRM, Defender for Cloud Apps).
- [Detect and investigate threats to AI agents using Microsoft Defender (Preview)](https://learn.microsoft.com/en-us/defender-xdr/security-for-ai/ai-agent-detection-protection) · Documentación · Oficial · Vista previa · Microsoft Learn. Detecciones casi en tiempo real para agentes gestionados por Agent 365 (jailbreak, XPIA, fuga de secretos, reconocimiento de LLM) e investigación con Advanced hunting. *Nota:* Solo agentes de Foundry publicados; agentes de otras plataformas requieren el SDK de Agent 365
- [AI agent runtime protection with Microsoft Defender for Endpoint (Preview)](https://learn.microsoft.com/en-us/defender-endpoint/ai-agent-runtime-protection-overview) · Documentación · Oficial · Vista previa · Microsoft Learn. Protección de agentes locales (Claude Code, Codex CLI, GitHub Copilot CLI y otros) contra inyección de prompts mediante inspección nativa de eventos e inspección de red. *Nota:* Relevante para clientes MCP locales usados en el track A5 (VS Code, CLI)
- [Application card for Perception](https://learn.microsoft.com/en-us/security/agentic-security/agentic-security-application-card) · Documentación · Oficial · Vista previa · Microsoft Learn. Ficha de IA responsable de Perception: usos previstos, limitaciones, evaluaciones, mitigaciones, supervisión humana, privacidad y uso de Entra Agent ID por agente.

### Anuncios y blogs oficiales

- [Securing AI agents: When AI tools move from reading to acting](https://www.microsoft.com/en-us/security/blog/2026/06/30/securing-ai-agents-ai-tools-move-from-reading-acting/) · Blog oficial · Oficial · Nuevo · Microsoft Defender Experts / Incident Response · Microsoft Security Blog · 30 jun 2026. Caso de envenenamiento de descripciones de herramientas MCP en un agente de Copilot Studio y guía de detección, contención y prevención con controles de Microsoft.
- [Updating the taxonomy of failure modes in agentic AI systems: What a year of red teaming taught us](https://www.microsoft.com/en-us/security/blog/2026/06/04/updating-taxonomy-failure-modes-agentic-ai-systems-year-red-teaming-taught-us/) · Blog oficial · Oficial · Nuevo · Microsoft AI Red Team · Microsoft Security Blog · 4 jun 2026. Resume los siete nuevos modos de fallo (cadena de suministro agéntica, secuestro de objetivos, abuso de MCP, etc.) y las nuevas mitigaciones de la taxonomía v2.

### Comunidad: blogs, libros, newsletters y eventos

- [Taxonomy of Failure Modes in Agentic AI Systems v2.0](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/security/Taxonomy-of-Failure-Modes-in-Agentic-AI-Systems-v2-0.pdf) · Libro · Oficial · Microsoft AI Red Team · abr 2026. Taxonomía v2 de fallos de seguridad y seguridad funcional en sistemas agénticos (XPIA, envenenamiento de memoria, abuso de MCP/plugins, escalada de confianza entre agentes) con familias de mitigación.

**Manos a la obra**

1. `Laboratorio` Modela las amenazas de un agente del SOC —el agente de triage o el que creaste en [A4](03_Nivel_3_Avanzado.md#a4)—: entradas (correos o documentos con instrucciones ocultas), herramientas, identidad y permisos, datos que lee, salidas y acciones; mapea cada amenaza a un modo de fallo de la [taxonomía v2](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/security/Taxonomy-of-Failure-Modes-in-Agentic-AI-Systems-v2-0.pdf) y a un control. Evidencia: modelo de amenazas con controles mapeados.
2. `Laboratorio parcial` Prueba de inyección indirecta controlada: incluye una instrucción oculta en un documento o correo de prueba que procese tu agente propio y documenta su comportamiento, la detección (si la hubo) y la mitigación que agregarías a sus instrucciones o herramientas ([de leer a actuar](https://www.microsoft.com/en-us/security/blog/2026/06/30/securing-ai-agents-ai-tools-move-from-reading-acting/)). Limitación: consumo de SCU y solo con datos de prueba. Evidencia: informe de la prueba.
3. `Laboratorio parcial` Inventaría las identidades de agente en Entra (Agents > Agent identities) con su sponsor ([administrar identidades de agente](https://learn.microsoft.com/en-us/entra/agent-id/manage-agent-identities-admin)) y consulta la tabla AgentsInfo en la búsqueda avanzada ([inventario de agentes](https://learn.microsoft.com/en-us/defender-xdr/security-for-ai/ai-agent-inventory)). Limitación: el inventario completo requiere habilitar la seguridad para agentes y, para Foundry y terceros, Agent 365. Evidencia: inventario con dueño y sponsor por agente.
4. `Laboratorio parcial` En una VM de laboratorio con Defender for Endpoint en modo activo, habilita la [protección en tiempo de ejecución para agentes locales](https://learn.microsoft.com/en-us/defender-endpoint/ai-agent-runtime-protection-overview) y revisa qué eventos genera un agente de línea de comandos ([guía de un MVP](https://jeffreyappel.nl/configure-ai-agent-runtime-protection-preview-with-microsoft-defender-for-endpoint/)). Limitación: vista previa y licencia de la herramienta de IA. Evidencia: eventos capturados y configuración aplicada.
5. `Laboratorio parcial` Revisa el [Security Dashboard for AI](https://learn.microsoft.com/en-us/security/security-for-ai/security-dashboard-for-ai) con el rol Security Reader y registra la línea base de inventario y riesgos de IA de tu tenant. Limitación: en un tenant de prueba habrá pocos activos de IA. Evidencia: captura de la línea base y tres recomendaciones priorizadas.
6. `Laboratorio parcial` En [DSPM for AI](https://learn.microsoft.com/en-us/purview/dspm-for-ai) de Purview, revisa las interacciones de Security Copilot y de tus agentes de prueba (pares prompt-respuesta y datos sensibles detectados) y define qué alertas o directivas aplicarías según las [protecciones de Purview para IA generativa](https://learn.microsoft.com/en-us/purview/ai-microsoft-purview). Limitación: pocas interacciones en el laboratorio y la versión clásica de DSPM for AI se está reemplazando por la nueva experiencia DSPM. Evidencia: informe de interacciones con tres decisiones de protección.
7. `Solo producción` Activa la [protección en tiempo real de Defender](https://learn.microsoft.com/en-us/defender-xdr/security-for-ai/ai-agent-real-time-protection) para los agentes de producción, que requiere Agent 365. Cómo hacerlo seguro: empezar con la regla por defecto en auditoría, revisar BehaviorInfo durante dos semanas, crear reglas de bloqueo solo para patrones confirmados y avisar a los dueños de los agentes. Evidencia: informe de dos semanas de auditoría y reglas aprobadas.

<a id="x4"></a>

## X4 · Operación y gobierno de un parque de agentes

*L300–L400 · ~5 h · Origen: Nuevo en esta edición*

Con un agente alcanza una buena configuración; con veinte hace falta **gobierno de parque**. Cada agente necesita un dueño, un sponsor, una identidad con permisos revisados, un presupuesto de SCU, una métrica de calidad y un procedimiento de parada probado. Las herramientas existen: el **panel de uso** con 90 días de consumo por agente, tipo y experiencia (el agente de triage incluso muestra el costo por correo procesado), los controles de cada agente (ejecutar, pausar, feedback, memoria, editar y quitar), las **identidades de agente** en Entra, el inventario de Defender con la tabla **AgentsInfo** (que reemplaza a AIAgentsInfo), el **Security Dashboard for AI** y, en Perception, métricas por agente como la tasa de éxito y las aprobaciones otorgadas.

**Agent 365**, en disponibilidad general desde el 1 de mayo de 2026 e incluido en Microsoft 365 E7, es el plano de control para registrar, gobernar y proteger agentes; desde el 1 de julio de 2026 también es requisito para descubrir agentes de Foundry y de terceros en Defender for Cloud. En noviembre de 2026 Microsoft anunció permisos y acceso condicional dinámicos para limitar la autoridad de un agente a cada tarea. Este módulo convierte todo eso en una rutina operativa con evidencia para auditoría; el ciclo de vida de las identidades de agente se profundiza en el programa de Entra (módulo X4).

**Por qué importa**

Sin gobierno de parque, los agentes se acumulan como cuentas de servicio olvidadas: nadie sabe quién los aprobó, cuánto cuestan ni qué pueden tocar. Una ficha por agente y un simulacro de parada probado son lo mínimo que esperará un auditor, y lo que permite escalar sin sorpresas de costo ni de riesgo.

**Qué vas a lograr**

- Mantener un inventario de agentes con dueño, sponsor, identidad, permisos, costo y métricas.
- Operar agentes: ejecutar, pausar, dar feedback, gestionar memoria, editar y retirar.
- Monitorear costo y calidad por agente con el panel de uso y las métricas de cada producto.
- Auditar cambios de configuración de agentes con Purview y la búsqueda avanzada.
- Probar un procedimiento de parada de emergencia y de rotación de identidad.

> **Novedad.** Microsoft Agent 365 está en disponibilidad general desde el 1 de mayo de 2026 e incluido en Microsoft 365 E7 ([Agent 365 en GA](https://www.microsoft.com/en-us/security/blog/2026/05/01/microsoft-agent-365-now-generally-available-expands-capabilities-and-integrations/)); desde el 1 de julio de 2026 también es requisito para descubrir y evaluar la postura de agentes de Foundry y de terceros en Defender for Cloud ([postura de seguridad de IA](https://learn.microsoft.com/en-us/azure/defender-for-cloud/ai-security-posture)).

> **Qué cambió.** La tabla AgentsInfo reemplaza a AIAgentsInfo con la transición a Agent 365: actualiza tus consultas y detecciones ([inventario de agentes](https://learn.microsoft.com/en-us/defender-xdr/security-for-ai/ai-agent-inventory)). Las identidades de agente se administran en Entra con Agent ID Administrator o Cloud Application Administrator ([administrar identidades de agente](https://learn.microsoft.com/en-us/entra/agent-id/manage-agent-identities-admin)).

> **Consejo Ninja.** Para auditar la gestión de agentes, la comunidad propone consultar CloudAppEvents filtrando las acciones que contienen «CopilotAgent»; valida el resultado en tu tenant antes de convertirlo en detección ([notas operativas](https://techcommunity.microsoft.com/discussions/microsoftthreatprotection/operational-notes-on-microsoft-security-copilot-agents-in-defender-xdr-and-micro/4525826)). También hay consultas comunitarias de deriva de configuración sobre AgentsInfo ([deriva de configuración](https://techcommunity.microsoft.com/discussions/microsoftsentinel/hunting-ai-agent-configuration-drift-with-microsoft-sentinel/4538962)).

> **Novedad.** El 5 de noviembre de 2026 Microsoft anunció Dynamic Permissions, Dynamic Agent Risk y Dynamic Conditional Access para limitar la autoridad de un agente a cada tarea; verifica su estado después de Ignite ([novedades de noviembre de 2026](https://www.microsoft.com/en-us/security/blog/2026/11/05/whats-new-in-microsoft-security-november-2026/)).

**¿Tienes poco tiempo?**

- [Setup and manage Security Copilot agents](https://learn.microsoft.com/en-us/copilot/security/agents-manage) · Documentación
- [Manage agent identities in your organization - Microsoft Entra Agent ID](https://learn.microsoft.com/en-us/entra/agent-id/manage-agent-identities-admin) · Documentación
- [Discover AI agents and assess security posture using Microsoft Defender](https://learn.microsoft.com/en-us/defender-xdr/security-for-ai/ai-agent-inventory) · Documentación
- [Approve, reject, or stop agentic work (Project Perception)](https://learn.microsoft.com/en-us/security/agentic-security/agentic-security-supervise-work) · Documentación

### Documentación, cursos y credenciales

- [Manage security compute unit usage in Security Copilot](https://learn.microsoft.com/en-us/copilot/security/manage-usage) · Documentación · Oficial · Nuevo · Microsoft Learn · 4 jun 2026. Describe el panel de uso (90 días, por capacidad, sesión, usuario, plugin, experiencia y categoría), exportación a Excel, avisos al acercarse al límite, cambio de SCU aprovisionadas/overage y borrado de capacidad.
- [Application card for Microsoft Security Copilot agents](https://learn.microsoft.com/en-us/copilot/security/security-copilot-application-card-agents) · Documentación · Oficial · Microsoft Learn. Tarjeta de IA responsable de los agentes: usos previstos, autonomía, limitaciones, evaluaciones y buenas prácticas de despliegue con control humano.
- [Setup and manage Security Copilot agents](https://learn.microsoft.com/en-us/copilot/security/agents-manage) · Documentación · Oficial · Microsoft Learn. Cómo configurar agentes de Microsoft y de partners, elegir identidad, dar feedback, gestionar la memoria, ejecutar/pausar y editar agentes.
- [Manage agent identities in your organization - Microsoft Entra Agent ID](https://learn.microsoft.com/en-us/entra/agent-id/manage-agent-identities-admin) · Documentación · Oficial · Microsoft Learn. Tareas de administración de identidades de agente: ver, blueprints, permisos heredables, Acceso Condicional, riesgo, sponsors y deshabilitación.
- [What are agent identities? - Microsoft Entra Agent ID](https://learn.microsoft.com/en-us/entra/agent-id/what-are-agent-identities) · Documentación · Oficial · Microsoft Learn. Explica por qué los agentes necesitan un tipo de identidad propio, distinto de usuarios y service principals, para atribución, mínimo privilegio y escala.
- [What is Perception?](https://learn.microsoft.com/en-us/security/agentic-security/agentic-security-overview) · Documentación · Oficial · Vista previa · Nuevo · Microsoft Learn · 30 oct 2026. Visión general de Perception: configurar agentes, delegar trabajo con playbooks o chat y supervisar sesiones aprobando, rechazando o deteniendo acciones. *Nota:* Navegación en Defender: New Chat, Sessions, Agents, Playbooks, Insights
- [Work with agents in Project Perception](https://learn.microsoft.com/en-us/security/agentic-security/agentic-security-agents) · Documentación · Oficial · Vista previa · Microsoft Learn. Administración de agentes de Perception: configuración, identidad Entra Agent ID, roles (Security Admin instala, Security Reader usa), métricas de desempeño y retiro de agentes. *Nota:* La pestaña Performance muestra Success Rate, Approvals Granted y Automatic Initiation por agente
- [Approve, reject, or stop agentic work (Project Perception)](https://learn.microsoft.com/en-us/security/agentic-security/agentic-security-supervise-work) · Documentación · Oficial · Vista previa · Microsoft Learn. Cómo supervisar sesiones agénticas: estado 'Waiting for input', aprobar, rechazar o sugerir alternativas y detener sesiones de forma irreversible. *Nota:* Base del modelo humano-en-el-circuito para acciones de alto impacto (p. ej., deshabilitar cuentas o aislar dispositivos)
- [Discover AI agents and assess security posture using Microsoft Defender](https://learn.microsoft.com/en-us/defender-xdr/security-for-ai/ai-agent-inventory) · Documentación · Oficial · Microsoft Learn. Inventario centralizado de agentes de IA (Copilot Studio, Foundry, Microsoft 365, terceros y locales) con nivel de riesgo, recomendaciones y tabla AgentsInfo en Advanced Hunting.
- [Overview - AI security posture management](https://learn.microsoft.com/en-us/azure/defender-for-cloud/ai-security-posture) · Documentación · Oficial · Microsoft Learn. Gestión de postura de IA en Defender CSPM y aviso de que desde el 1-jul-2026 el descubrimiento y postura de agentes de Foundry y de terceros requiere licencia de Microsoft Agent 365.
- [Secure agents: Identity, access, and data protection](https://learn.microsoft.com/en-us/agents/center-of-excellence/secure-agents) · Documentación · Oficial · Microsoft Learn. Guía de centro de excelencia para dar identidad (Entra Agent ID), mínimo privilegio, registro, protección de datos y monitoreo a todo agente.
- [Agent identities in Microsoft Entra Agent ID](https://learn.microsoft.com/en-us/entra/agent-id/agent-identities) · Documentación · Oficial · Microsoft Learn. Anatomía de una identidad de agente: sin credenciales propias, tokens vía blueprint, sponsor responsable y cuenta de usuario de agente opcional.
- [Assess your organization's AI risk with Microsoft Security Dashboard for AI](https://learn.microsoft.com/en-us/security/security-for-ai/security-dashboard-for-ai) · Documentación · Oficial · Microsoft Learn. Panel unificado de riesgo de IA (Entra, Defender, Purview) con inventario de agentes, recomendaciones asignables y prompts de Security Copilot.
- [View and manage sessions (Project Perception)](https://learn.microsoft.com/en-us/security/agentic-security/agentic-security-sessions) · Documentación · Oficial · Vista previa · Nuevo · Microsoft Learn · 29 oct 2026. Página de sesiones de Perception con vista lista o Kanban, estados (In progress, Waiting for input, Completed, Ended with failures, Stopped) y formas de iniciar sesiones. *Nota:* Ver sesiones requiere al menos Security Reader
- [Agent Management Essentials for Microsoft 365](https://learn.microsoft.com/en-us/microsoft-365/copilot/agent-essentials/agent-essentials-overview) · Documentación · Oficial · Microsoft Learn. Guía de gobierno de agentes en Microsoft 365 (prerrequisitos, blueprint, checklist) que remite a Agent 365 como plano de control.

### Anuncios y blogs oficiales

- [Secure agentic AI for your Frontier Transformation](https://www.microsoft.com/en-us/security/blog/2026/03/09/secure-agentic-ai-for-your-frontier-transformation/) · Blog oficial · Empleado de Microsoft · Vasu Jakkal · Microsoft Security Blog · 9 mar 2026. Anuncia Agent 365 y Microsoft 365 E7 (GA 1-may-2026) con registro de agentes, observabilidad, señales de riesgo y Agent ID para gobernar el parque de agentes.
- [What's new in Microsoft Security: November 2026](https://www.microsoft.com/en-us/security/blog/2026/11/05/whats-new-in-microsoft-security-november-2026/) · Blog oficial · Empleado de Microsoft · Nuevo · Alym Rayani · Microsoft Security Blog · 5 nov 2026. Novedades de noviembre 2026: Dynamic Permissions, Dynamic Agent Risk y Dynamic Conditional Access para limitar la autoridad de agentes, y Microsoft Execution Containers en GA.
- [Microsoft Agent 365, now generally available, expands capabilities and integrations](https://www.microsoft.com/en-us/security/blog/2026/05/01/microsoft-agent-365-now-generally-available-expands-capabilities-and-integrations/) · Blog oficial · Empleado de Microsoft · Nuevo · Nirav Shah; Rob Lefferts; Jason Roszak · Microsoft Security Blog · 1 may 2026. Anuncio de GA de Agent 365 con descubrimiento de agentes y shadow AI vía Defender e Intune, y gobierno de agentes con credenciales propias o delegadas.
- [Detecting and mitigating common agent misconfigurations](https://www.microsoft.com/en-us/security/blog/2026/02/12/detecting-and-mitigating-common-agent-misconfigurations/) · Blog oficial · Oficial · Microsoft Security Blog · 12 feb 2026. Diez configuraciones erróneas comunes de agentes y cómo detectarlas con consultas comunitarias de Advanced Hunting y mitigarlas en Copilot Studio.
- [Ambient and autonomous security for the agentic era](https://www.microsoft.com/en-us/security/blog/2025/11/18/ambient-and-autonomous-security-for-the-agentic-era/) · Blog oficial · Empleado de Microsoft · Vasu Jakkal · Microsoft Security Blog · 18 nov 2025. Visión de Ignite 2025 sobre seguridad 'ambiente y autónoma': Agent 365, protección de agentes y uso de agentes de Security Copilot para equipos de seguridad e IT.
- [Security Dashboard for AI - Now Generally Available](https://techcommunity.microsoft.com/blog/microsoft-security-blog/security-dashboard-for-ai---now-generally-available/4494637) · Blog oficial · Empleado de Microsoft · Amanda Lowe · Microsoft Tech Community (Microsoft Security Blog) · 13 feb 2026. Anuncio de GA del Security Dashboard for AI para CISOs con scorecard de riesgo, inventario de IA y priorización asistida por Security Copilot.

### Webinars, videos y podcasts

- [Agents That Actually Work: From an MVP (Skilling Series)](https://www.youtube.com/watch?v=1KsM2k2dP7U) · Webinar · MVP · Ugur Koc · Microsoft Security Community (YouTube) · 19 feb 2026. Webinar de un MVP sobre cómo pasar de una idea a un agente fiable: iterar objetivos e instrucciones, elegir herramientas y validar decisiones con evidencia (lenguaje natural, Agent Builder y YAML).
- [Security Copilot: Your agentic workforce for smarter faster defense | BRK238 (Ignite 2025, resumen)](https://tech.hub.ms/ai/videos/security-copilot-automating-and-accelerating-defense-with-agentic-workflows) · Video · Empleado de Microsoft · Lizzie Heinze; Sarat Subramaniam · Tech Hub (resumen de Microsoft Events) · 21 nov 2025. Resumen de la sesión avanzada BRK238 sobre métricas de impacto de agentes, transparencia de decisiones y orquestación de agentes de Microsoft, partners y personalizados.

### Comunidad: blogs, libros, newsletters y eventos

- [Operational Notes on Microsoft Security Copilot Agents in Defender XDR and Microsoft Entra ID](https://techcommunity.microsoft.com/discussions/microsoftthreatprotection/operational-notes-on-microsoft-security-copilot-agents-in-defender-xdr-and-micro/4525826) · Blog · Comunidad · Nuevo · klianos · Microsoft Tech Community (foro) · 5 jun 2026. Notas operativas de la comunidad: cuentas de usuario agénticas, roles URBAC creados por los agentes, monitoreo de uso y consultas KQL sobre CloudAppEvents para auditar la gestión de agentes.
- [Security Copilot Agents in Defender XDR: where things actually stand](https://techcommunity.microsoft.com/discussions/microsoft-security/security-copilot-agents-in-defender-xdr-where-things-actually-stand/4514689) · Blog · Comunidad · Marcel_Graewer · Microsoft Tech Community (foro) · 25 abr 2026. Análisis práctico de un miembro de la comunidad sobre qué agentes de Defender están GA o en preview, trampas de configuración y cómo controlar el consumo de SCU.

**Manos a la obra**

1. `Laboratorio` Completa una ficha de gobierno para cada agente de tu parque (de Microsoft, de partners y propios): dueño, sponsor, identidad, permisos, disparador, datos, presupuesto de SCU, métrica de calidad, fecha de revisión y procedimiento de parada ([configurar y gestionar agentes](https://learn.microsoft.com/en-us/copilot/security/agents-manage)). Evidencia: fichas de gobierno por agente.
2. `Laboratorio parcial` Haz un simulacro de parada: pausa un agente, rechaza su último feedback, cambia su identidad y quítalo; mide cuánto tardaste en cada paso y quién tuvo que intervenir. Limitación: requiere capacidad, un agente configurado y Security Administrator. Evidencia: simulacro de parada documentado con tiempos.
3. `Laboratorio parcial` Despliega las [consultas comunitarias de deriva de configuración](https://techcommunity.microsoft.com/discussions/microsoftsentinel/hunting-ai-agent-configuration-drift-with-microsoft-sentinel/4538962) sobre AgentsInfo y la consulta de CloudAppEvents de las [notas operativas](https://techcommunity.microsoft.com/discussions/microsoftthreatprotection/operational-notes-on-microsoft-security-copilot-agents-in-defender-xdr-and-micro/4525826), y valida qué devuelven en tu tenant. Limitación: contenido comunitario y poco volumen en el laboratorio. Evidencia: consultas guardadas con su resultado.
4. `Laboratorio parcial` Exporta el [panel de uso](https://learn.microsoft.com/en-us/copilot/security/manage-usage) y arma un tablero por agente: SCU por ejecución, ejecuciones por día y costo mensual proyectado, con un umbral de alerta. Limitación: volumen de laboratorio. Evidencia: tablero de costo por agente.
5. `Solo producción` Haz la revisión mensual del parque en producción: consumo por agente, costo por correo procesado del agente de triage, métricas de Perception (tasa de éxito, aprobaciones otorgadas e inicio automático) y la decisión de ampliar, mantener o pausar cada agente ([agentes en Perception](https://learn.microsoft.com/en-us/security/agentic-security/agentic-security-agents)). Cómo hacerlo seguro: revisores con roles de solo lectura, decisiones registradas en comité y cambios por ventana. Evidencia: acta de la revisión mensual.
6. `Solo producción` Si tienes Agent 365 (en E7 o como complemento), registra tus agentes y evalúa el acceso condicional y la protección de identidad para agentes en modo solo informe ([Agent 365 en GA](https://www.microsoft.com/en-us/security/blog/2026/05/01/microsoft-agent-365-now-generally-available-expands-capabilities-and-integrations/)). Cómo hacerlo seguro: grupo piloto de agentes, políticas en solo informe, aprobación del sponsor de cada agente y reversión documentada. Evidencia: informe del impacto que tendrían las políticas.

**¿Quieres profundizar?**

- [Agents That Actually Work: From an MVP (Skilling Series)](https://www.youtube.com/watch?v=1KsM2k2dP7U) · Webinar
- [Operational Notes on Microsoft Security Copilot Agents in Defender XDR and Microsoft Entra ID](https://techcommunity.microsoft.com/discussions/microsoftthreatprotection/operational-notes-on-microsoft-security-copilot-agents-in-defender-xdr-and-micro/4525826) · Blog
- [Security Copilot Agents in Defender XDR: where things actually stand](https://techcommunity.microsoft.com/discussions/microsoft-security/security-copilot-agents-in-defender-xdr-where-things-actually-stand/4514689) · Blog

<a id="x5"></a>

## X5 · Proyecto integrador: un SOC agéntico de punta a punta

*L300–L400 · ~12 h · Origen: Nuevo en esta edición (equivale a la evaluación práctica final)*

El cierre del programa es construir, en tu laboratorio y con un piloto en producción, un SOC agéntico pequeño pero completo. No se trata de usar todas las funciones, sino de demostrar criterio: qué delegar a un agente, dónde poner a una persona, cuánto cuesta, cómo se protege y cómo se mide. El proyecto se apoya en la serie oficial **IdentityDrift** —datos sintéticos en el data lake de Sentinel, un prototipo en Foundry y un agente en Security Copilot— y en los laboratorios oficiales de **Agent 365**.

Está organizado en ocho fases con entregables verificables: plataforma, datos, prototipo, agente propio, automatización, agente de Microsoft supervisado, gobierno y piloto con métricas. Al terminar tendrás un portafolio reutilizable —manifiestos, plugins, flujos, fichas de gobierno, modelo de amenazas y caso de negocio— y una hoja de ruta para defender ante el comité. Los proyectos integradores de los programas de Sentinel (X7) y Defender XDR (A8) son buenos complementos.

**Por qué importa**

Un comité no aprueba tecnología: aprueba un plan con evidencia. Este proyecto produce exactamente eso —un prototipo funcionando, costos medidos, controles probados y un piloto con métricas— y deja al equipo con la experiencia de haber recorrido el camino completo antes de escalarlo.

**Qué vas a lograr**

- Integrar plataforma, datos, agentes, automatización y gobierno en un flujo coherente.
- Construir y publicar un agente propio a partir de un prototipo en Foundry.
- Supervisar un agente de Microsoft con una matriz de autonomía y métricas.
- Defender ante un comité una hoja de ruta con costos, riesgos y valor medido.

> **Consejo Ninja.** La serie oficial IdentityDrift es el esqueleto del proyecto: [ingesta de datos de muestra en el data lake](https://learn.microsoft.com/en-us/azure/sentinel/isv/ingest-sample-data), [prototipo en Foundry](https://learn.microsoft.com/en-us/azure/sentinel/isv/build-agent-azure-ai-foundry) y [agente en Security Copilot](https://learn.microsoft.com/en-us/azure/sentinel/isv/build-agent-security-copilot), este último también [en español](https://learn.microsoft.com/es-es/azure/sentinel/isv/build-agent-security-copilot). El propio laboratorio pide eliminar la capacidad de SCU al terminar.

> **Atención.** El laboratorio IdentityDrift todavía usa el nombre Azure AI Foundry (nombre anterior), y en tenants incorporados al data lake después del 23 de septiembre de 2026 la colección de exploración del servidor MCP podría no responder: prueba la fase de datos antes de comprometer fechas ([reporte comunitario](https://tokesi.cloud/blogs/26_09_28_integrated_data_lake/)).

> **Consejo Ninja.** Para extender el proyecto a agentes de Copilot Studio, los laboratorios oficiales de Agent 365 muestran un agente con MCP y la caza de su telemetría en Defender ([agent365-labs](https://github.com/microsoft/agent365-labs)). Los proyectos integradores de los programas de Sentinel (X7) y Defender XDR (A8) aportan datos, detecciones y playbooks reutilizables.

**¿Tienes poco tiempo?**

- [Ingest Data to Microsoft Sentinel Data Lake (serie IdentityDrift)](https://learn.microsoft.com/en-us/azure/sentinel/isv/ingest-sample-data) · Laboratorio
- [Build a security investigation agent in Azure AI Foundry (serie IdentityDrift)](https://learn.microsoft.com/en-us/azure/sentinel/isv/build-agent-azure-ai-foundry) · Laboratorio
- [Develop a Security Copilot agent platform solution (serie IdentityDrift)](https://learn.microsoft.com/en-us/azure/sentinel/isv/build-agent-security-copilot) · Laboratorio
- [microsoft/agent365-labs](https://github.com/microsoft/agent365-labs) · Laboratorio

**Fases del proyecto integrador**

| Fase | Qué construyes | Entregable verificable | Módulos de apoyo |
|---|---|---|---|
| 1 · Plataforma | Workspace, roles, auditoría, política de gobierno y capacidad | Checklist de plataforma completo | I2, M7 |
| 2 · Datos | Datos sintéticos de IdentityDrift en el data lake y una herramienta MCP propia | Tablas pobladas y herramienta MCP funcionando | A5 |
| 3 · Prototipo | Instrucciones del agente investigador probadas en Foundry | Instrucciones versionadas con tres pruebas | A7 |
| 4 · Agente propio | Agente en el agent builder con su tabla de pruebas | Agente publicado en ámbito de usuario | A2, A4 |
| 5 · Automatización | Playbook que dispara el agente y Logic App de contención con aprobación | Ejecución de punta a punta registrada | A3 |
| 6 · Agente supervisado | Agente de Microsoft con identidad de agente y matriz de autonomía | Veredictos revisados y decisiones de autonomía | M1, M6, X1 |
| 7 · Gobierno | Fichas, modelo de amenazas, costos, simulacro de parada y planes de salida | Carpeta lista para auditoría | X3, X4 |
| 8 · Piloto con métricas | Piloto de dos a cuatro semanas con línea base y caso de negocio | Informe del piloto y decisión del comité | X2 |

Basado en la serie oficial IdentityDrift ([datos](https://learn.microsoft.com/en-us/azure/sentinel/isv/ingest-sample-data), [Foundry](https://learn.microsoft.com/en-us/azure/sentinel/isv/build-agent-azure-ai-foundry) y [Security Copilot](https://learn.microsoft.com/en-us/azure/sentinel/isv/build-agent-security-copilot)) y en los [laboratorios de Agent 365](https://github.com/microsoft/agent365-labs).

### Laboratorios, GitHub y herramientas

- [Ingest Data to Microsoft Sentinel Data Lake (serie IdentityDrift)](https://learn.microsoft.com/en-us/azure/sentinel/isv/ingest-sample-data) · Laboratorio · Oficial · Microsoft Learn. Primer paso del laboratorio de punta a punta: poblar el data lake con datos de ejemplo mediante KQL jobs (SigninLogs, AADRiskyUsers, DeviceProcessEvents, SecurityAlerts y telemetría del ISV).
- [Build a security investigation agent in Azure AI Foundry (serie IdentityDrift)](https://learn.microsoft.com/en-us/azure/sentinel/isv/build-agent-azure-ai-foundry) · Laboratorio · Oficial · Microsoft Learn. Usa Foundry como banco de pruebas para afinar las instrucciones del agente con la herramienta de exploración de datos de Sentinel antes de llevarlo a Security Copilot.
- [Develop a Security Copilot agent platform solution (serie IdentityDrift)](https://learn.microsoft.com/en-us/azure/sentinel/isv/build-agent-security-copilot) · Laboratorio · Oficial · Microsoft Learn. Paso a paso para crear capacidad SCU y workspace, construir el agente IdentityDrift con el agent builder, configurarlo y probarlo en Security Copilot.
- [microsoft/agent365-labs](https://github.com/microsoft/agent365-labs) · Laboratorio · Empleado de Microsoft · Nuevo · Microsoft (Matteo Pagani y otros) · GitHub (Microsoft) · oct 2026. Laboratorios oficiales para incorporar agentes a Agent 365: agente de Copilot Studio con MCP de Microsoft Learn, observabilidad y caza de sus trazas en Microsoft Defender.

**Manos a la obra**

1. `Laboratorio parcial` Fase 1 · Plataforma: workspace documentado ([I2](01_Nivel_1_Inicial.md#i2)), roles y grupos, auditoría activa, política de gobierno ([M7](02_Nivel_2_Intermedio.md#m7)) y capacidad del proyecto (pool de E5/E7 o 1 SCU con excedente en cero que eliminas al final de cada sesión). Limitación: capacidad por horas en el laboratorio. Evidencia: checklist de plataforma completo.
2. `Laboratorio parcial` Fase 2 · Datos: carga los datos sintéticos de IdentityDrift en el data lake con trabajos de KQL ([ingesta de datos de muestra](https://learn.microsoft.com/en-us/azure/sentinel/isv/ingest-sample-data)) y crea una herramienta MCP personalizada sobre ellos. Limitación: costo del data lake. Evidencia: tablas pobladas y herramienta MCP funcionando.
3. `Laboratorio parcial` Fase 3 · Prototipo: diseña y prueba las instrucciones del agente investigador en Foundry con la herramienta de exploración de Sentinel ([prototipo en Foundry](https://learn.microsoft.com/en-us/azure/sentinel/isv/build-agent-azure-ai-foundry)). Limitación: costo de Foundry y del data lake. Evidencia: instrucciones versionadas con tres pruebas.
4. `Laboratorio parcial` Fase 4 · Agente propio: construye el agente en el agent builder ([agente en Security Copilot](https://learn.microsoft.com/en-us/azure/sentinel/isv/build-agent-security-copilot)), ejecuta tu tabla de pruebas, incluidas las adversas, y publícalo en ámbito de usuario. Limitación: consumo de SCU en las pruebas. Evidencia: agente propio funcionando y tabla de pruebas.
5. `Laboratorio parcial` Fase 5 · Automatización: un playbook dispara el agente ante incidentes de severidad alta y escribe su resultado en el incidente, y una Logic App expuesta como skill ejecuta la contención solo con aprobación humana ([disparar agentes desde Logic Apps](https://learn.microsoft.com/en-us/copilot/security/connector-logicapp-agent-trigger)). Limitación: SCU y costo de Logic Apps. Evidencia: ejecución de punta a punta registrada.
6. `Laboratorio parcial` Fase 6 · Agente de Microsoft supervisado: configura el [Security Alert Triage Agent](https://learn.microsoft.com/en-us/defender-xdr/security-alert-triage-agent) con identidad de agente y aplica tu matriz de autonomía; si tu tenant participa en la vista previa de Perception, compáralo con su Triage Agent sobre incidentes cerrados. Limitación: bajo volumen de correo reportado en el laboratorio. Evidencia: veredictos revisados y decisiones de autonomía.
7. `Laboratorio` Fase 7 · Gobierno: fichas de gobierno de cada agente, modelo de amenazas, acceso condicional para Security Copilot, umbrales de costo, simulacro de parada y plan de salida para cada función en vista previa ([X3](#x3), [X4](#x4)). Evidencia: carpeta de gobierno lista para auditoría.
8. `Solo producción` Fase 8 · Piloto con métricas: dos a cuatro semanas en producción con un caso de uso, línea base frente a resultado (MTTA, MTTR, tiempo de triage, falsos positivos y SCU por caso) y defensa de la hoja de ruta ante el comité ([casos de uso y métricas](00_Programa.md#casos-de-uso)). Cómo hacerlo seguro: grupo piloto, autonomía mínima al inicio, revisión diaria de las salidas, umbral de costo que obliga a pausar el agente y criterio de éxito acordado antes de empezar. Evidencia: informe del piloto y decisión del comité.

<a id="reto-agentes"></a>

## Reto del nivel

**Defensa de la hoja de ruta ante el comité.** Con el proyecto integrador ([X5](#x5)) como evidencia, presenta en 20 minutos la evaluación de madurez y el objetivo a 12 meses, la matriz de autonomía, el caso de negocio con línea base y costo por caso de uso, el modelo de amenazas y los controles por agente, las fichas de gobierno y el resultado del simulacro de parada. Un comité formado por tu líder, una persona de riesgo y una de privacidad decide ampliar, ajustar o detener; documenta la decisión y sus condiciones.

<a id="quiz-agentes"></a>

## Evaluación del nivel

Responde y compara con [Evaluaciones y respuestas](06_Evaluaciones_y_respuestas.md#eval-agentes). Con 80 % o más, ¡nivel aprobado! (En la versión web puedes corregir en línea y generar tu certificado).

1. Según Microsoft, ¿qué caracteriza la etapa SOC 2 del camino hacia el SOC agéntico?
   - a) Unificar la plataforma
   - b) IA generativa y agentes de tarea
   - c) Automatización agéntica de punta a punta
   - d) Tercerizar el SOC

2. En Project Perception, ¿qué ocurre al detener una sesión de trabajo agéntico?
   - a) Se puede reanudar en las siguientes 24 horas
   - b) Se convierte en un playbook propio
   - c) Es irreversible y la sesión queda como registro de auditoría
   - d) Se eliminan sus registros

3. ¿Qué estima el libro blanco de Microsoft sobre SecOps agéntico acerca de las alertas?
   - a) Que el 42 % queda sin investigar
   - b) Que el 99,99 % son falsos positivos
   - c) Que el 75 % son de phishing
   - d) Que el 20 % son críticas

4. En el ensayo controlado del agente de triage de phishing, ¿qué parte de la ganancia de productividad vino de priorizar la cola?
   - a) 17 %
   - b) 53 %
   - c) 77 %
   - d) 83 %

5. El estudio que asocia la adopción de Security Copilot con un MTTR 30,13 % menor a los tres meses es:
   - a) Un ensayo controlado aleatorizado
   - b) Un estudio observacional de operaciones reales
   - c) Una proyección de Forrester
   - d) Una encuesta de satisfacción

6. ¿Qué describe mejor el estudio Total Economic Impact de Forrester de noviembre de 2024 sobre Security Copilot?
   - a) Una medición en más de 150 organizaciones
   - b) Un ensayo controlado con 167 analistas
   - c) Un estudio proyectado, con un ROI estimado de 99 % a 348 % para un SOC de 20 personas
   - d) Una auditoría independiente de costos reales

7. Para extender el acceso condicional e ID Protection a identidades de agente, ¿qué se necesita?
   - a) Solo Entra ID Free
   - b) SCU de Security Copilot
   - c) Defender for Cloud
   - d) Microsoft Agent 365 (incluido en E7 y como complemento para E5)

8. ¿Qué afirmación sobre las identidades de agente de Entra es correcta?
   - a) No tienen credenciales propias, son de un solo tenant y pueden tener un sponsor humano
   - b) Usan contraseñas que rota el propio agente
   - c) Funcionan en varios tenants a la vez
   - d) Reemplazan a las cuentas de servicio y no se auditan

9. ¿Dónde se registran los eventos de la protección en tiempo real de Defender para agentes?
   - a) En AIAgentsInfo
   - b) En BehaviorInfo
   - c) En SigninLogs
   - d) Solo en CloudAppEvents

10. En Purview, ¿qué protección aplica a los agentes de Security Copilot?
   - a) Clasificación, etiquetas, DLP y riesgo interno
   - b) Solo DLP
   - c) Solo la clasificación de datos
   - d) Ninguna

11. ¿Qué tabla de la búsqueda avanzada reemplaza a AIAgentsInfo con la transición a Agent 365?
   - a) AgentsInfo
   - b) AIAgentEvents
   - c) AgentIdentityInfo
   - d) CopilotAgents

12. Desde el 1 de julio de 2026, ¿qué se necesita para descubrir agentes de Foundry y de terceros en Defender for Cloud?
   - a) Defender CSPM únicamente
   - b) Microsoft Agent 365
   - c) Un workspace de Sentinel
   - d) Capacidad aprovisionada de Security Copilot

13. En Project Perception, ¿qué roles configuran los agentes y cuáles los usan?
   - a) Global Administrator configura y Global Reader usa
   - b) Copilot owner configura y Copilot contributor usa
   - c) Agent ID Administrator configura y Cloud Application Administrator usa
   - d) Security Admin instala y configura; Security Reader usa y ve las sesiones

14. ¿Qué controles de operación comunes ofrece Security Copilot para sus agentes?
   - a) Feedback, memoria, ejecutar o pausar, editar y quitar
   - b) Solo activar y desactivar
   - c) Solo cambiar la identidad
   - d) Ninguno: se gestionan desde Azure

15. En la serie oficial IdentityDrift, ¿cuál es el orden de trabajo?
   - a) Agente en Security Copilot, datos y prototipo
   - b) Prototipo en Foundry, publicación en el Store y datos
   - c) Datos sintéticos en el data lake, prototipo en Foundry y agente en Security Copilot
   - d) Logic Apps, Copilot Studio y Foundry

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

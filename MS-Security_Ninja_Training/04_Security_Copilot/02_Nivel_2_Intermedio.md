# Nivel 2 · Intermedio · Security Copilot en cada rol

*Microsoft Security Copilot Ninja Training: hacia el SOC agéntico · Edición 2026*

[← Nivel 1 · Inicial](01_Nivel_1_Inicial.md) · [Índice del programa](README.md) · [Nivel 3 · Avanzado →](03_Nivel_3_Avanzado.md)

<a id="intermedio"></a>

Security Copilot y sus agentes para el SOC, la inteligencia de amenazas, la identidad, los endpoints y la protección de datos, con el marco común de agentes y el gobierno base. Terminas con un agente de Microsoft configurado con mínimo privilegio y una política de gobierno aprobada.

*L300 · 7 módulos · ~35 horas · 93 recursos*

**Módulos de este nivel:** [M1 SOC: triage e investigación](#m1) · [M2 Inteligencia de amenazas](#m2) · [M3 Identidad y acceso](#m3) · [M4 Endpoints y vulnerabilidades](#m4) · [M5 Datos y cumplimiento](#m5) · [M6 Agentes de Microsoft](#m6) · [M7 Gobierno, costos y auditoría](#m7)

<a id="m1"></a>

## M1 · Security Copilot en el SOC: triage, investigación e informes

*L300 · ~7 h · Origen: Ninja oficial de 2024, parte 2, módulo 1 (plugins de Defender XDR y Sentinel), ampliado con los agentes del SOC*

En el portal de Defender, Security Copilot acompaña todo el ciclo del incidente: el **resumen** (hasta 100 alertas, con caché de una semana sin costo si el incidente no cambia), las **respuestas guiadas** en cuatro categorías —triage, contención, investigación y remediación— limitadas por tus permisos de URBAC, el **análisis de scripts** con técnicas de MITRE ATT&CK, el **asistente de consultas** que traduce lenguaje natural a KQL y el **informe de incidente**, que consolida acciones manuales y automáticas, analistas, clasificación y playbooks de Sentinel. Con Sentinel incorporado al portal, todo esto aplica a los incidentes unificados.

Sobre esa base trabajan los **agentes del SOC**. El **Security Alert Triage Agent** —el antiguo agente de triage de phishing ampliado— clasifica de forma autónoma los correos reportados por usuarios (en disponibilidad general) y, en vista previa, alertas de nube, contenedores e identidad, con un veredicto explicado y aprendizaje por retroalimentación en correo. El **Threat Hunting Assistant** conversa en la búsqueda avanzada (modos *Rich insights* y *Query only*), el **Security Analyst Agent** hace análisis profundos con Python sobre Defender XDR, Sentinel o el data lake, y el **Dynamic Threat Detection Agent** busca falsos negativos en segundo plano, gratis mientras esté en vista previa.

El foco de este módulo es combinar experiencias y agentes con medición. El detalle de cada agente en Defender se profundiza en el programa de Defender XDR (módulo A6) y el uso con datos de Sentinel, en el programa de Sentinel (módulo X2).

**Por qué importa**

El triage de correos reportados y de la cola de alertas consume la mayor parte del tiempo del nivel 1. Un agente que clasifica con veredicto explicado puede liberar horas cada día —el ensayo controlado de Microsoft midió hasta 6,5 veces más verdaderos positivos por minuto de analista—, pero solo si los prerrequisitos están bien configurados y se mide la precisión antes de confiar en él.

**Qué vas a lograr**

- Usar el resumen, las respuestas guiadas, el análisis de scripts y el informe de incidente en el portal de Defender.
- Configurar el Security Alert Triage Agent con sus prerrequisitos, una identidad de agente y permisos mínimos.
- Comparar el Threat Hunting Assistant (Rich insights y Query only) con el Security Analyst Agent.
- Explicar cómo funciona y cuánto cuesta el Dynamic Threat Detection Agent.
- Medir tiempo de triage, precisión y SCU por alerta en un piloto.

> **Novedad.** El Security Alert Triage Agent es el antiguo agente de triage de phishing ampliado: el triage de correo y colaboración está en disponibilidad general (anunciado el 18 de noviembre de 2025) y el de alertas de nube, contenedores e identidad —por ejemplo, password spray o reglas de buzón típicas de BEC—, en vista previa (documentación del 2 de julio de 2026). El aprendizaje por feedback solo aplica a correo ([Security Alert Triage Agent](https://learn.microsoft.com/en-us/defender-xdr/security-alert-triage-agent)). En Ignite 2025 Microsoft informó, en pruebas, 6,5 veces más alertas maliciosas identificadas y un 77 % más de precisión del veredicto ([anuncio](https://techcommunity.microsoft.com/blog/MicrosoftDefenderforOffice365Blog/microsoft-ignite-2025-transforming-phishing-response-with-agentic-innovation/4470791)).

> **Atención.** Si el agente de triage «no hace nada», revisa la regla de ajuste Auto-Resolve – Email reported by user as malware or phish: el agente no tría alertas ya resueltas. También necesita URBAC activo para Defender for Office 365, la opción Monitor reported messages in Outlook y la política de alerta de correo reportado. Configurarlo, pausarlo, cambiar su identidad o rechazar feedback exige Security Administrator de Entra, y una cuenta de usuario como identidad no es compatible con PIM ni con TAP ([Security Alert Triage Agent](https://learn.microsoft.com/en-us/defender-xdr/security-alert-triage-agent)).

> **Qué cambió.** El Threat Hunting Agent pasó a llamarse Threat Hunting Assistant (página actualizada el 10 de septiembre de 2026): solo ejecuta consultas de lectura con tus permisos y descubre también las tablas personalizadas de Sentinel ([Copilot en la búsqueda avanzada](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-security-copilot)). El Security Analyst Agent está en vista previa pública desde abril de 2026 y el Dynamic Threat Detection Agent genera alertas con fuente «Security Copilot», gratis durante su vista previa ([Security Analyst Agent](https://learn.microsoft.com/en-us/defender-xdr/security-analyst-agent), [Dynamic Threat Detection Agent](https://learn.microsoft.com/en-us/defender-xdr/dynamic-threat-detection-agent)).

> **Atención.** Si configuras el Triage Agent de Project Perception, este reemplaza al agente de triage de Security Copilot y conserva su historial: solo puede haber un agente de triage activo ([Triage Agent de Perception](https://learn.microsoft.com/en-us/security/agentic-security/triage-agent)). Los agentes de Defender se profundizan en el programa de Defender XDR (módulo A6).

**¿Tienes poco tiempo?**

- [Microsoft Security Copilot Security Alert Triage Agent in Microsoft Defender (Preview)](https://learn.microsoft.com/en-us/defender-xdr/security-alert-triage-agent) · Documentación
- [Microsoft Security Copilot in advanced hunting](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-security-copilot) · Documentación
- [Summarize an incident with Microsoft Copilot in Microsoft Defender](https://learn.microsoft.com/en-us/defender-xdr/security-copilot-m365d-incident-summary) · Documentación
- [Empowering the SOC: Security Copilot and the Rise of Agentic Defense | BRK1731 (Ignite 2025)](https://www.youtube.com/watch?v=SiF5YDHaw6Y) · Video

### Documentación, cursos y credenciales

- [Microsoft Security Copilot in advanced hunting](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-security-copilot) · Documentación · Oficial · Nuevo · Microsoft Learn · 10 sep 2026. Explica los dos modos de Copilot en Advanced hunting (Rich insights/Threat Hunting Assistant y Query only) y cómo cambiar al Security Analyst Agent.
- [Security Copilot with Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/sentinel-security-copilot) · Documentación · Oficial · Microsoft Learn (Sentinel). Explica los plugins Microsoft Sentinel y NL to KQL (preview), cómo fijar un workspace por defecto y cómo aprovechar incidentes unificados en el portal de Defender.
- [Microsoft Security Copilot Phishing Triage Agent in Microsoft Defender](https://learn.microsoft.com/en-us/defender-xdr/phishing-triage-agent) · Documentación · Oficial · Microsoft Learn. Guía de prerrequisitos (MDO P2, URBAC, alertas de correo reportado), configuración, feedback y monitoreo del agente de triage de phishing reportado por usuarios.
- [Microsoft Security Copilot Threat Hunting Assistant in advanced hunting](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-security-copilot-threat-hunting-assistant) · Documentación · Oficial · Microsoft Learn. Experiencia conversacional de caza que descubre esquemas (incluidas tablas personalizadas de Sentinel), genera y ejecuta KQL de solo lectura e interpreta resultados.
- [Summarize an incident with Microsoft Copilot in Microsoft Defender](https://learn.microsoft.com/en-us/defender-xdr/security-copilot-m365d-incident-summary) · Documentación · Oficial · Microsoft Learn. Resumen de incidentes (hasta 100 alertas) con cronología, activos, IOC y actores, y configuración de generación automática por severidad o bajo demanda con estimación de SCU.
- [Create an incident report with Microsoft Copilot in Microsoft Defender](https://learn.microsoft.com/en-us/defender-xdr/security-copilot-m365d-create-incident-report) · Documentación · Oficial · Microsoft Learn. Generación de informes de incidente que consolidan acciones manuales y automáticas, analistas, clasificación y playbooks de Sentinel, exportables a PDF o al registro de actividad.
- [Triage and investigate incidents with guided responses from Microsoft Copilot in Microsoft Defender](https://learn.microsoft.com/en-us/defender-xdr/security-copilot-m365d-guided-response) · Documentación · Oficial · Microsoft Learn. Respuestas guiadas por categoría (triage, contención, investigación, remediación) con acciones aplicables por entidad y posibilidad de cargar guías propias de la organización.
- [Microsoft Security Copilot Security Analyst Agent overview](https://learn.microsoft.com/en-us/defender-xdr/security-analyst-agent) · Documentación · Oficial · Vista previa · Nuevo · Microsoft Learn · 14 ago 2026. Agente conversacional que realiza análisis avanzados con Python sobre Defender XDR, Sentinel Log Analytics o data lake (tendencias, anomalías, scoring) sin escribir código. *Nota:* Se ejecuta con la identidad del usuario; se activa desde Advanced hunting con 'Switch to Security Analyst Agent'
- [Microsoft Security Copilot Security Alert Triage Agent in Microsoft Defender (Preview)](https://learn.microsoft.com/en-us/defender-xdr/security-alert-triage-agent) · Documentación · Oficial · Vista previa · Nuevo · Microsoft Learn · 2 jul 2026. Documentación del agente autónomo que clasifica alertas de Defender (correo GA; nube/contenedores e identidad en preview) con razonamiento transparente y aprendizaje por feedback. *Nota:* Mismo agente que el Phishing Triage Agent; correo/colaboración GA, nube/contenedores e identidad (password spray, reglas de buzón BEC) en preview; identidad recomendada: nueva Entra Agent ID (la cuenta de usuario no es compatible con PIM/TAP)…
- [Microsoft Security Copilot Dynamic Threat Detection Agent](https://learn.microsoft.com/en-us/defender-xdr/dynamic-threat-detection-agent) · Documentación · Oficial · Vista previa · Microsoft Learn · 23 feb 2026. Agente siempre activo en el backend de Defender que busca falsos negativos correlacionando señales de Defender y Sentinel y genera alertas con fuente 'Security Copilot'. *Nota:* Gratis durante la preview pública; consumirá SCU al llegar a GA; no requiere configuración
- [Microsoft Security Copilot advanced hunting query assistant](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-security-copilot-query-assistant) · Documentación · Oficial · Nuevo · Microsoft Learn · 5 ago 2026. Uso del asistente NL-a-KQL para generar, revisar, ejecutar o editar consultas de caza y dar feedback.
- [Use case: Investigate an incident and associated suspicious entities](https://learn.microsoft.com/en-us/copilot/security/investigate-incident-malicious-script) · Documentación · Oficial · Nuevo · Microsoft Learn · 29 may 2026. Caso de uso paso a paso que combina resumen de incidente, análisis de script y prompts en el portal independiente para producir una evaluación con recomendaciones.
- [Script analysis with Microsoft Copilot in Microsoft Defender](https://learn.microsoft.com/en-us/defender-xdr/security-copilot-m365d-script-analysis) · Documentación · Oficial · Microsoft Learn. Análisis de scripts y líneas de comando sospechosas desde la historia del ataque o la línea de tiempo del dispositivo, con técnicas MITRE asociadas.

### Anuncios y blogs oficiales

- [Monthly news - January 2026 (Microsoft Defender)](https://techcommunity.microsoft.com/blog/microsoftthreatprotectionblog/monthly-news---january-2026/4484885) · Blog oficial · Empleado de Microsoft · HeikeRitter · Microsoft Tech Community (Defender XDR Blog) · 13 ene 2026. Resumen mensual que confirma GA del agente de triage de phishing y del TI Briefing Agent y la preview pública de Dynamic Threat Detection y Threat Hunting Agent.
- [Microsoft Ignite 2025: Transforming Phishing Response with Agentic Innovation](https://techcommunity.microsoft.com/blog/MicrosoftDefenderforOffice365Blog/microsoft-ignite-2025-transforming-phishing-response-with-agentic-innovation/4470791) · Blog oficial · Empleado de Microsoft · JeffreyPinkston · Microsoft Tech Community (Defender for Office 365 Blog) · 18 nov 2025. Anuncia la disponibilidad general del agente de triage (antes Phishing Triage Agent, hoy Security Alert Triage Agent), métricas de impacto y el sistema agéntico de calificación de envíos.
- [What's new in Microsoft Security: September 2026](https://www.microsoft.com/en-us/security/blog/2026/09/24/whats-new-in-microsoft-security-september-2026/) · Blog oficial · Empleado de Microsoft · Nuevo · Alym Rayani · Microsoft Security Blog · 24 sep 2026. Incluye el nuevo resumen de detonación de correo generado por Security Copilot para explicar resultados de sandboxing de URL y archivos en investigaciones.

### Webinars, videos y podcasts

- [Empowering the SOC: Security Copilot and the Rise of Agentic Defense | BRK1731 (Ignite 2025)](https://www.youtube.com/watch?v=SiF5YDHaw6Y) · Video · Empleado de Microsoft · Cristina Da Gama; Corina Feuerstein · Microsoft Events (YouTube) · nov 2025. Sesión de Ignite 2025 con demos del SOC agéntico en Defender: memoria de sesión, GA del agente de triage de phishing, TI Briefing Agent y cambio a asignación mensual de SCU.

**Manos a la obra**

1. `Laboratorio parcial` Despliega el [Security Alert Triage Agent](https://learn.microsoft.com/en-us/defender-xdr/security-alert-triage-agent) para correo reportado: verifica Defender for Office 365 P2 (incluido en la prueba de E5), activa URBAC para Defender for Office 365, configura Monitor reported messages in Outlook y la política de alerta, desactiva la regla de ajuste de autorresolución, crea una identidad de agente con permisos mínimos, reporta correos de prueba y revisa el veredicto y View agent activity. Limitación: bajo volumen, correos sintéticos y consumo de SCU. Evidencia: agente configurado con identidad de agente y tres veredictos revisados.
2. `Laboratorio parcial` Plantea cinco preguntas de caza al [Threat Hunting Assistant](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-security-copilot-threat-hunting-assistant) en modo Rich insights y en modo Query only, compara el KQL generado y documenta los errores; luego lleva una pregunta de tendencia al [Security Analyst Agent](https://learn.microsoft.com/en-us/defender-xdr/security-analyst-agent). Limitación: poca telemetría en el laboratorio y consumo de SCU. Evidencia: tabla de KQL generado y corregido.
3. `Laboratorio parcial` Sobre un incidente de prueba, usa el resumen, las [respuestas guiadas](https://learn.microsoft.com/en-us/defender-xdr/security-copilot-m365d-guided-response) (anota qué acciones bloquea tu rol de URBAC), el [análisis de scripts](https://learn.microsoft.com/en-us/defender-xdr/security-copilot-m365d-script-analysis) desde la línea de tiempo del dispositivo y, tras resolverlo, el [informe de incidente](https://learn.microsoft.com/en-us/defender-xdr/security-copilot-m365d-create-incident-report). Limitación: telemetría de prueba. Evidencia: informe exportado con tus correcciones.
4. `Laboratorio parcial` Busca en la cola las alertas generadas por el [Dynamic Threat Detection Agent](https://learn.microsoft.com/en-us/defender-xdr/dynamic-threat-detection-agent) (fuente «Security Copilot») y, si aparece alguna, documenta qué falso negativo intentaba cubrir y si la consideras válida. Limitación: con poca telemetría puede no generar alertas; es gratuito mientras siga en vista previa. Evidencia: registro de la búsqueda y de su resultado.
5. `Solo producción` Piloto del agente de triage en producción con un grupo de usuarios que reportan correos. Cómo hacerlo seguro: revisión diaria de los incidentes con la etiqueta Agent, feedback solo después de una revisión por pares, identidad de agente con permisos mínimos, pausa inmediata ante un veredicto benigno equivocado y lectura semanal de la pestaña Performance (tiempo medio de triage y SCU). Evidencia: informe semanal del piloto.
6. `Solo producción` Mide antes y después: cuatro semanas de línea base de MTTA y MTTR para un tipo de incidente y cuatro semanas de comparación con el resumen por severidad activado ([casos de uso y métricas](00_Programa.md#casos-de-uso)). Cómo hacerlo seguro: extracción de datos con roles de solo lectura, sin cambiar el proceso durante la línea base y con métricas agregadas, no por analista. Evidencia: tabla de antes y después con SCU por incidente.

<a id="m2"></a>

## M2 · Inteligencia de amenazas con Security Copilot

*L300 · ~4 h · Origen: Ninja oficial de 2024, parte 2, módulo 1 (plugins de Threat Intelligence y Defender EASM)*

Todo usuario autenticado de Security Copilot accede a **Microsoft Threat Intelligence**: perfiles de actores, campañas, indicadores y vulnerabilidades, con promptbooks como *Check impact of an external threat article*, el perfil de actor y el informe TI 360. En 2026 la inteligencia de Defender Threat Intelligence convergió en el portal de Defender, con una vista general cuyo resumen ejecutivo genera el **Threat Intelligence Briefing Agent**, el explorador de inteligencia y Threat analytics.

El **Threat Intelligence Briefing Agent** prepara informes personalizados con tu exposición y las CVE de interés. Funciona en Defender y en la experiencia independiente (cada 7 días o bajo demanda) y se recomienda configurarlo con una identidad de agente de solo lectura: si esa identidad no tiene permisos sobre la búsqueda avanzada, la gestión de vulnerabilidades y los grupos de dispositivos, el informe de exposición aparece como no disponible. En **Project Perception**, el **Threat Intelligence Agent** va más lejos: extrae indicadores, TTP, CVE y actores de un artículo, los mapea a MITRE, evalúa su relevancia para tu entorno y genera KQL, pidiéndote aprobar su plan de tareas.

**Por qué importa**

Los equipos de inteligencia pierden horas leyendo informes que no aplican a su entorno. Conectar la inteligencia con tu exposición real —dispositivos, CVE y activos— acorta el tiempo entre la publicación de una amenaza relevante y la primera búsqueda en tu entorno, que es la métrica que importa al negocio.

**Qué vas a lograr**

- Usar el plugin y los promptbooks de inteligencia para evaluar el impacto de un artículo externo.
- Configurar el Threat Intelligence Briefing Agent con identidad de agente y mínimo privilegio.
- Diagnosticar por qué un informe de exposición aparece como no disponible.
- Describir el flujo del Threat Intelligence Agent de Perception, del artículo al KQL, con aprobación humana.

> **Atención.** Si el informe de exposición del Threat Intelligence Briefing Agent aparece como «not available», revisa la identidad del agente: necesita lectura sobre búsqueda avanzada, gestión de vulnerabilidades, configuración e inventario de dispositivos, y acceso de lectura a cada grupo de dispositivos ([agentes en Defender](https://learn.microsoft.com/en-us/defender-xdr/security-copilot-agents-defender)). Además requiere los plugins Microsoft Threat Intelligence y Microsoft Threat Intelligence agents (EASM es opcional) y URBAC activo ([TI Briefing Agent en Defender](https://learn.microsoft.com/en-us/defender-xdr/threat-intel-briefing-agent-defender)).

> **Qué cambió.** En 2026 Defender Threat Intelligence convergió en el portal de Defender: la nueva vista general muestra un resumen ejecutivo generado por el Threat Intelligence Briefing Agent, junto al explorador de inteligencia y Threat analytics, y algunas capacidades en vista previa exigen un workspace de ISOC ([inteligencia en Defender](https://learn.microsoft.com/en-us/defender-xdr/defender-threat-intelligence), [novedades de julio de 2026](https://www.microsoft.com/en-us/security/blog/2026/07/30/whats-new-in-microsoft-security-july-2026/)).

> **Atención.** El estado y la licencia del Threat Intelligence Briefing Agent varían según la fuente: disponibilidad general desde diciembre de 2025 según las noticias mensuales de Defender, vista previa en «What's new»; «Not Applicable» en Defender y Defender EASM Standard en la tabla de la experiencia independiente ([noticias de enero de 2026](https://techcommunity.microsoft.com/blog/microsoftthreatprotectionblog/monthly-news---january-2026/4484885), [agentes independientes](https://learn.microsoft.com/en-us/copilot/security/agents-security-copilot)).

> **Novedad.** El Threat Intelligence Agent de Perception (documentación del 24 de septiembre de 2026) extrae indicadores, TTP, CVE y actores de un artículo, los mapea a MITRE, evalúa su relevancia para tu entorno y genera KQL; requiere Defender XDR y Defender Threat Intelligence y pide aprobar su plan de tareas ([Threat Intelligence Agent](https://learn.microsoft.com/en-us/security/agentic-security/threat-intelligence-agent)).

**¿Tienes poco tiempo?**

- [Security Copilot Threat Intelligence Briefing Agent in Microsoft Defender](https://learn.microsoft.com/en-us/defender-xdr/threat-intel-briefing-agent-defender) · Documentación
- [Use Microsoft Security Copilot for threat intelligence](https://learn.microsoft.com/en-us/defender-xdr/security-copilot-and-defender-threat-intelligence) · Documentación
- [Threat Intelligence Agent (Project Perception)](https://learn.microsoft.com/en-us/security/agentic-security/threat-intelligence-agent) · Documentación

### Documentación, cursos y credenciales

- [Security Copilot Threat Intelligence Briefing Agent in Microsoft Defender](https://learn.microsoft.com/en-us/defender-xdr/threat-intel-briefing-agent-defender) · Documentación · Oficial · Microsoft Learn. Configuración del agente que genera informes de inteligencia de amenazas personalizados desde Threat analytics en Defender, con identidad de agente recomendada.
- [Use Microsoft Security Copilot for threat intelligence](https://learn.microsoft.com/en-us/defender-xdr/security-copilot-and-defender-threat-intelligence) · Documentación · Oficial · Microsoft Learn. Cómo usar el plugin Microsoft Threat Intelligence y los promptbooks de TI (por ejemplo, impacto de un artículo externo) en el portal independiente y en Defender.
- [Threat intelligence in Microsoft Defender](https://learn.microsoft.com/en-us/defender-xdr/defender-threat-intelligence) · Documentación · Oficial · Microsoft Learn. Nueva experiencia de inteligencia en Defender (Overview con resumen ejecutivo del TI Briefing Agent, Intel explorer, threat analytics) y uso de Copilot y del Threat Intelligence Agent de Perception.
- [Threat Intelligence Agent (Project Perception)](https://learn.microsoft.com/en-us/security/agentic-security/threat-intelligence-agent) · Documentación · Oficial · Vista previa · Nuevo · Microsoft Learn · 24 sep 2026. Agente que convierte artículos de TI en inteligencia estructurada (IOC, TTP, CVE, MITRE), evalúa relevancia para el entorno y genera consultas KQL, con aprobación del plan de tareas. *Nota:* Requiere Defender XDR y MDTI; permisos ThreatIntelligence.Read.All, ThreatHunting.Read.All, AdvancedHunting.Read.All y SecurityEvents.Read.All; punto de entrada del playbook 'Protect against a threat'
- [Microsoft Security Copilot Threat Intelligence Briefing Agent (standalone)](https://learn.microsoft.com/en-us/copilot/security/threat-intel-briefing-agent) · Documentación · Oficial · Microsoft Learn. Documentación del agente de briefings de inteligencia de amenazas: plugins requeridos, identidad del agente (recomendada) y permisos mínimos con rol personalizado de Defender XDR.
- [Using Microsoft Security Copilot for threat intelligence (Defender TI embedded)](https://learn.microsoft.com/en-ca/defender/threat-intelligence/using-copilot-threat-intelligence-defender-xdr) · Documentación · Oficial · Legado aún útil · Microsoft Learn · 12 sep 2025. Prompts integrados Summarize, Prioritize y Ask en Threat analytics, Intel profiles, Intel explorer e Intel projects del portal Defender. *Nota:* Escrita antes de la convergencia de MDTI en Defender (ago-2026); las páginas Intel profiles/projects cambiaron de ubicación

**Manos a la obra**

1. `Laboratorio parcial` Configura el [Threat Intelligence Briefing Agent en Defender](https://learn.microsoft.com/en-us/defender-xdr/threat-intel-briefing-agent-defender) con una identidad de agente: crea un rol personalizado de solo lectura (búsqueda avanzada, gestión de vulnerabilidades, configuración e inventario de dispositivos), da acceso de lectura a los grupos de dispositivos y compara el briefing con y sin esos permisos. Limitación: con pocos dispositivos el informe de exposición será pobre y cada ejecución consume SCU. Evidencia: briefing de inteligencia generado con mínimo privilegio.
2. `Laboratorio parcial` Ejecuta el promptbook Check impact of an external threat article ([Copilot para inteligencia de amenazas](https://learn.microsoft.com/en-us/defender-xdr/security-copilot-and-defender-threat-intelligence)) con un artículo reciente y compara su resultado con una búsqueda manual de los mismos indicadores en tu entorno. Limitación: poca telemetría y consumo de SCU. Evidencia: comparación de hallazgos.
3. `Laboratorio parcial` Ejecuta los promptbooks de perfil de actor e informe TI 360 sobre un actor que afecte a tu industria y redacta un briefing ejecutivo de una página, verificando cada afirmación en Threat analytics. Limitación: consumo de SCU. Evidencia: briefing con las fuentes verificadas.
4. `Laboratorio` Diseña la métrica «tiempo desde la publicación de una amenaza relevante hasta la primera búsqueda en tu entorno»: campos del registro, quién lo completa y cómo obtener la línea base sin Copilot ([casos de uso y métricas](00_Programa.md#casos-de-uso)). Evidencia: planilla de registro con los datos del último mes.
5. `Solo producción` Prueba el [Threat Intelligence Agent de Perception](https://learn.microsoft.com/en-us/security/agentic-security/threat-intelligence-agent) si tu tenant fue invitado a la vista previa. Cómo hacerlo seguro: aprobar su plan de tareas paso a paso, rechazar cualquier paso que no sea de lectura, dar Security Reader al equipo que aprende y revisar el KQL generado antes de guardarlo como detección. Evidencia: sesión revisada con las decisiones tomadas.

<a id="m3"></a>

## M3 · Identidad y acceso con Security Copilot

*L300 · ~5 h · Origen: Ninja oficial de 2024, parte 2, módulo 1 (plugin de Entra), ampliado con los agentes de Entra*

En el centro de administración de **Microsoft Entra**, Copilot responde con el rol mínimo de Security Reader y la autenticación on-behalf-of: resume **usuarios en riesgo** (con Entra ID P2), investiga inicios de sesión, explica políticas de acceso condicional y, en gobierno de identidades, ayuda en revisiones de acceso y paquetes de acceso, incluso detectando decisiones que contradicen la recomendación de la IA. Para organizaciones sin E5, la guía de prueba de concepto de Entra sugiere entre 15 y 20 SCU.

El **Conditional Access Optimization Agent** está en disponibilidad general desde julio de 2025: cada 24 horas (o bajo demanda) busca usuarios y aplicaciones sin cobertura, propone consolidar políticas y crea las nuevas en **modo solo informe**, con menos de 1 SCU por ejecución en promedio y una identidad de agente con permisos de Graph fijos. El **Identity Risk Management Agent**, en vista previa, investiga hasta 100 usuarios en riesgo por ejecución y recomienda remediaciones que una persona aprueba. El estado del **Access Review Agent** y del **App Lifecycle Management Agent** es incierto: verifícalo en tu tenant. La identidad de los agentes y el acceso condicional para agentes se profundizan en el programa de Entra (módulos X2, X3 y X5).

**Por qué importa**

Las brechas de cobertura de acceso condicional —usuarios o aplicaciones sin política— están entre las debilidades más explotadas. Un agente que las encuentra a diario por menos de 1 SCU y propone políticas en solo informe acorta el tiempo para cerrarlas sin saltarse el control de cambios.

**Qué vas a lograr**

- Usar Copilot en Entra para investigar usuarios en riesgo, inicios de sesión y políticas.
- Configurar el Conditional Access Optimization Agent y revisar sus sugerencias en modo solo informe.
- Explicar el alcance, los límites y los roles del Identity Risk Management Agent.
- Reconocer el estado incierto del Access Review Agent y del App Lifecycle Management Agent.

> **Novedad.** El Conditional Access Optimization Agent está en disponibilidad general desde julio de 2025 (se anunció en marzo de 2025); la integración con ServiceNow y las ejecuciones disparadas por actividad siguen en vista previa. En RSAC 2026, el equipo de producto lo presentó como un 43 % más rápido y un 48 % más preciso ([CA Optimization Agent](https://learn.microsoft.com/en-us/entra/security-copilot/conditional-access-agent-optimization), [blog de Security Copilot](https://techcommunity.microsoft.com/t5/s/gxcuf89792/rss/board?board.id=SecurityCopilotBlog)).

> **Atención.** El agente de acceso condicional requiere Entra ID P1, consume menos de 1 SCU por ejecución en promedio (el escaneo inicial no consume), crea políticas en modo solo informe y analiza hasta 300 usuarios y 150 aplicaciones por ejecución y 40 pares de políticas para consolidar. Su identidad de agente tiene permisos de Graph fijos, que no se pueden cambiar ni quitar, y se ejecuta cada 24 horas o bajo demanda ([CA Optimization Agent](https://learn.microsoft.com/en-us/entra/security-copilot/conditional-access-agent-optimization), [agentes de Entra](https://learn.microsoft.com/en-us/entra/security-copilot/entra-agents)).

> **Atención.** El Identity Risk Management Agent (vista previa, documentación del 1 de mayo de 2026) analiza hasta 100 usuarios en riesgo por ejecución, en unos 10 a 15 minutos y sin remediación automática; la guía exige Entra ID P2, pero el catálogo de agentes de Entra menciona la licencia de Agent ID. Las páginas de Learn del Access Review Agent se eliminaron el 2 de abril de 2026 y el App Lifecycle Management Agent solo figura en la hoja de ruta ([Identity Risk Management Agent](https://learn.microsoft.com/en-us/entra/id-protection/identity-risk-management-agent-get-started), [Entra.News](https://daily.entra.news/day/2026-04-02/), [RM536578](https://mc.merill.net/message/RM536578)).

> **Consejo Ninja.** Las identidades de agente, el acceso condicional para agentes y los agentes de Security Copilot en Entra se profundizan en el programa de Entra (módulos X2, X3 y X5). Para organizaciones sin E5, la [guía de prueba de concepto](https://learn.microsoft.com/en-us/entra/architecture/security-copilot-entra-proof-of-concept) sugiere de 15 a 20 SCU.

**¿Tienes poco tiempo?**

- [Microsoft Entra Conditional Access Optimization Agent](https://learn.microsoft.com/en-us/entra/security-copilot/conditional-access-agent-optimization) · Documentación
- [Microsoft Entra agents](https://learn.microsoft.com/en-us/entra/security-copilot/entra-agents) · Documentación
- [Identity Risk Management Agent (Preview)](https://learn.microsoft.com/en-us/entra/id-protection/identity-risk-management-agent-get-started) · Documentación

### Documentación, cursos y credenciales

- [Microsoft Entra Conditional Access Optimization Agent](https://learn.microsoft.com/en-us/entra/security-copilot/conditional-access-agent-optimization) · Documentación · Oficial · Nuevo · Microsoft Learn · 23 jun 2026. Agente que detecta usuarios, apps e identidades de agente sin cobertura de Acceso Condicional, propone políticas en modo solo informe y consolida políticas similares.
- [Microsoft Security Copilot in Microsoft Entra proof-of-concept guide](https://learn.microsoft.com/en-us/entra/architecture/security-copilot-entra-proof-of-concept) · Documentación · Oficial · Microsoft Learn. Guía de prueba de concepto con escenarios por persona (helpdesk, identidad, seguridad) para Copilot embebido en Entra y sus agentes, con prompts sugeridos.
- [Microsoft Entra agents](https://learn.microsoft.com/en-us/entra/security-copilot/entra-agents) · Documentación · Oficial · Microsoft Learn · 1 abr 2026. Catálogo de agentes de Entra con identidad, licencias, permisos Graph, roles y triggers de cada agente (CA Optimization, Identity Risk Management y otros).
- [Respond to identity threats using risky user summarization](https://learn.microsoft.com/en-us/entra/security-copilot/entra-risky-user-summarization) · Documentación · Oficial · Microsoft Learn · 3 oct 2025. Resumen de riesgo de usuario en ID Protection con explicación, pasos recomendados y prompts para listar usuarios en riesgo e historial.
- [Identity Risk Management Agent (Preview)](https://learn.microsoft.com/en-us/entra/id-protection/identity-risk-management-agent-get-started) · Documentación · Oficial · Vista previa · Nuevo · Microsoft Learn · 1 may 2026. Agente de Entra ID Protection que investiga usuarios en riesgo, resume hallazgos, recomienda remediación (aprobación manual) y guarda instrucciones en memoria. *Nota:* Requiere Entra ID P2 y Security Administrator para activarlo; hasta 100 usuarios en riesgo por ejecución; no remedia automáticamente
- [Review and apply suggestions from the Conditional Access Optimization Agent](https://learn.microsoft.com/en-us/entra/security-copilot/conditional-access-agent-optimization-review-suggestions) · Documentación · Oficial · Microsoft Learn. Cómo revisar la lógica, el impacto y el JSON de cada sugerencia, activar políticas, posponer 14 días o marcar como revisada.
- [Identity Governance and optimization with Microsoft Security Copilot](https://learn.microsoft.com/en-us/entra/security-copilot/entra-governance-optimization) · Documentación · Oficial · Microsoft Learn. Prompts y roles para analizar revisiones de acceso, entitlement management y PIM con Security Copilot embebido en Entra, incluida la detección de decisiones que contradicen recomendaciones de IA.
- [Microsoft Entra Ignite 2025: Key Announcements and Updates](https://learn.microsoft.com/en-us/entra/fundamentals/whats-new-ignite-2025) · Documentación · Oficial · Microsoft Learn · nov 2025. Resumen oficial de novedades de Entra en Ignite 2025: Microsoft Entra Agent ID, plataforma de identidad de agentes y escenarios actualizados de Security Copilot en Entra.
- [Microsoft Security Copilot scenarios in Microsoft Entra ID Governance](https://learn.microsoft.com/en-us/entra/security-copilot/entra-id-governance-scenarios) · Documentación · Oficial · Microsoft Learn. Tabla de escenarios embebidos de ID Governance (access reviews, entitlement, PIM y acciones de escritura, lifecycle workflows) con rol y licencia requeridos.
- [Respuesta a amenazas de identidad mediante el resumen de usuarios de riesgo](https://learn.microsoft.com/es-es/entra/security-copilot/entra-risky-user-summarization) · Documentación · Oficial · ES · Microsoft Learn · 20 mar 2026. Versión en español de la guía de resumen de usuarios en riesgo con Copilot en Entra ID Protection.

### Anuncios y blogs oficiales

- [The Microsoft Entra agent for smarter access governance: Access Review Agent](https://techcommunity.microsoft.com/blog/microsoft-entra-blog/the-microsoft-entra-agent-for-smarter-access-governance-access-review-agent/4279689) · Blog oficial · Empleado de Microsoft · Vista previa · ManmeetBawa · Microsoft Tech Community (Microsoft Entra Blog) · 30 sep 2025. Presenta el Access Review Agent en preview pública, que analiza actividad de inicio de sesión y pares para recomendar decisiones de revisión de acceso dentro de Microsoft Teams. *Nota:* Autor ManmeetBawa (Microsoft); el revisor conversa con el agente en Teams y el administrador ve un mapa de actividad

### Laboratorios, GitHub y herramientas

- [RM536578 - Microsoft Security Copilot App Lifecycle Management Agent in Microsoft Entra](https://mc.merill.net/message/RM536578) · Herramienta · Comunidad · Vista previa · Microsoft 365 Roadmap (archivo merill.net) · 12 feb 2026. Elemento de roadmap del agente de ciclo de vida de aplicaciones de Entra que descubre apps privadas vía Global Secure Access, las incorpora con mínimo privilegio y propone deshabilitar las no usadas. *Nota:* Roadmap: preview dic-2025, GA prevista jul-2026 'In development'; no se encontró página Learn vigente — verificar en el tenant

### Comunidad: blogs, libros, newsletters y eventos

- [2 April 2026 — Entra.News Daily](https://daily.entra.news/day/2026-04-02/) · Newsletter · Comunidad · Entra.News Daily · 2 abr 2026. Rastreador de cambios de documentación de Entra que registra la eliminación de las páginas Learn del Access Review Agent el 2-abr-2026, sin confirmar su retiro.

**Manos a la obra**

1. `Laboratorio parcial` Crea usuarios y una aplicación de prueba sin cobertura de acceso condicional, ejecuta el [Conditional Access Optimization Agent](https://learn.microsoft.com/en-us/entra/security-copilot/conditional-access-agent-optimization), revisa en cada sugerencia el impacto de la política, el JSON y la lógica ([revisar sugerencias](https://learn.microsoft.com/en-us/entra/security-copilot/conditional-access-agent-optimization-review-suggestions)) y deja las políticas en solo informe. Limitación: consumo de SCU (el escaneo inicial no consume) y poco volumen. Evidencia: sugerencias en solo informe con la decisión documentada para cada una.
2. `Laboratorio parcial` Genera el [resumen de un usuario en riesgo](https://learn.microsoft.com/en-us/entra/security-copilot/entra-risky-user-summarization) para una cuenta de prueba con detecciones de riesgo y compáralo con la revisión manual en ID Protection. Limitación: requiere Entra ID P2 (incluido en la prueba de E5) y las señales de riesgo de un laboratorio son pocas. Evidencia: resumen y comparación.
3. `Laboratorio parcial` Desde el centro de administración de Entra, pregunta a Copilot por inicios de sesión fallidos, cambios recientes de políticas y aplicaciones con permisos altos; repite con una cuenta que solo tenga Security Reader y verifica que ve datos pero no puede actuar ([Copilot en Entra](https://learn.microsoft.com/en-us/entra/security-copilot/security-copilot-in-entra)). Limitación: pocos datos en el laboratorio. Evidencia: capturas con ambos roles.
4. `Laboratorio` Compara el [catálogo de agentes de Entra](https://learn.microsoft.com/en-us/entra/security-copilot/entra-agents) con el [inventario de agentes](00_Programa.md#inventario-agentes) de esta guía y registra las diferencias de nombre, estado o licencia (por ejemplo, Access Review Agent y App Lifecycle Management Agent). Evidencia: lista de diferencias con fecha de verificación.
5. `Solo producción` Activa el [Identity Risk Management Agent](https://learn.microsoft.com/en-us/entra/id-protection/identity-risk-management-agent-get-started), que necesita usuarios realmente en riesgo y señales de ID Protection. Cómo hacerlo seguro: limitar el alcance del agente a un grupo piloto, dar a la mayoría del equipo solo Security Reader y aprobar manualmente cada recomendación, ya que no hay remediación automática. Evidencia: registro de recomendaciones aprobadas y rechazadas.
6. `Solo producción` Lleva las sugerencias del agente de acceso condicional al control de cambios de producción. Cómo hacerlo seguro: nunca activar una política sin ventana de cambio, excluir las cuentas de emergencia, posponer 14 días las sugerencias que no correspondan y adjuntar las notas del agente a la solicitud para el comité de cambios. Evidencia: dos solicitudes de cambio con su análisis de impacto.

**¿Quieres profundizar?**

- [RM536578 - Microsoft Security Copilot App Lifecycle Management Agent in Microsoft Entra](https://mc.merill.net/message/RM536578) · Herramienta

<a id="m4"></a>

## M4 · Endpoints, dispositivos y vulnerabilidades con Security Copilot

*L300 · ~4 h · Origen: Ninja oficial de 2024, parte 2, módulo 1 (plugin de Intune), ampliado con agentes y Defender for Cloud*

En **Intune**, Copilot ayuda a entender políticas, comparar configuraciones, investigar dispositivos y explicar scripts, sin licencias adicionales de Intune y respetando RBAC y scope tags: el Intune Administrator hereda el rol de owner de Security Copilot y los demás roles de Intune, el de contributor. El agente vigente es el **Vulnerability Remediation Agent** (vista previa pública), que prioriza las CVE de Defender Vulnerability Management y guía su remediación con un usuario agéntico de solo lectura; requiere Intune Plan 1, Defender for Endpoint P2 o Defender Vulnerability Management y SCU.

2026 dejó una lección: tres de los cuatro agentes de Intune se retiraron (**Device Offboarding** el 1 de junio; **Policy Configuration** y **Change Review** el 31 de agosto). Quien construyó procesos sobre ellos tuvo que volver a lo manual. En la nube, **Defender for Cloud** no tiene un agente propio, pero Copilot resume, remedia y delega recomendaciones —con todo su potencial si tienes Defender CSPM— y el **Posture Prioritization Agent** de Perception propone, en vista previa, un plan de remediación priorizado y explicado para nube y dispositivos.

**Por qué importa**

El tiempo medio de remediación de vulnerabilidades críticas es una métrica que mira el directorio. Un agente que prioriza por explotabilidad y exposición ayuda a enfocar el esfuerzo, y la experiencia de los agentes retirados enseña a no depender de una vista previa sin un plan de salida.

**Qué vas a lograr**

- Usar Copilot en Intune respetando RBAC y scope tags.
- Configurar el Vulnerability Remediation Agent y validar su priorización de CVE.
- Explicar qué agentes de Intune se retiraron en 2026 y cómo planificar la salida de una vista previa.
- Usar Copilot en Defender for Cloud para resumir, remediar y delegar recomendaciones.

> **Qué cambió.** Tres de los cuatro agentes de Intune se retiraron en 2026: el Device Offboarding Agent no admite configuraciones nuevas desde el 30 de abril y se eliminó el 1 de junio; el Policy Configuration Agent y el Change Review Agent dejaron de estar disponibles el 31 de agosto. La página general de agentes de Intune, del 1 de abril de 2026, todavía lista los cuatro ([Device Offboarding Agent](https://learn.microsoft.com/en-us/intune/copilot/agents/device-offboarding-agent), [Change Review Agent](https://learn.microsoft.com/en-us/intune/copilot/agents/change-review-agent), [agentes de Intune](https://learn.microsoft.com/en-us/intune/copilot/agents/)).

> **Novedad.** El Vulnerability Remediation Agent (vista previa pública, solo en la nube pública) requiere Intune Plan 1, Defender for Endpoint P2 o Defender Vulnerability Management Standalone y SCU. Lo configura un owner de Security Copilot con Intune Read Only Operator, lo usa un contributor y trabaja con un usuario agéntico con lectura delegada en Intune y Defender ([Vulnerability Remediation Agent](https://learn.microsoft.com/en-us/intune/copilot/agents/vulnerability-remediation-agent)).

> **Consejo Ninja.** Copilot en Intune no exige licencias adicionales de Intune: el Intune Administrator hereda el rol de owner de Security Copilot, los demás roles de Intune heredan el de contributor y las respuestas respetan las scope tags ([Copilot en Intune](https://learn.microsoft.com/en-us/intune/copilot/)).

> **Atención.** Defender for Cloud no tiene agente propio: Copilot resume, remedia y delega recomendaciones, con más provecho si tienes Defender CSPM ([remediar con Copilot](https://learn.microsoft.com/en-us/azure/defender-for-cloud/remediate-with-copilot)). El Posture Prioritization Agent de Perception, de solo lectura y en vista previa limitada, propone un plan de remediación priorizado para nube y dispositivos ([Posture Prioritization Agent](https://learn.microsoft.com/en-us/security/agentic-security/posture-prioritization-agent)).

**¿Tienes poco tiempo?**

- [Vulnerability Remediation Agent in Microsoft Intune](https://learn.microsoft.com/en-us/intune/copilot/agents/vulnerability-remediation-agent) · Documentación
- [Security Copilot in Microsoft Intune features overview](https://learn.microsoft.com/en-us/intune/copilot/) · Documentación
- [Microsoft Security Copilot in Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/copilot-security-in-defender-for-cloud) · Documentación

### Documentación, cursos y credenciales

- [Microsoft Security Copilot in Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/copilot-security-in-defender-for-cloud) · Documentación · Oficial · Nuevo · Microsoft Learn (Defender for Cloud) · 15 jul 2026. Integración vía Copilot en Azure para analizar, resumir, remediar y delegar recomendaciones; funciona sin planes pagos pero con capacidad completa solo con Defender CSPM.
- [Security Copilot in Microsoft Intune features overview](https://learn.microsoft.com/en-us/intune/copilot/) · Documentación · Oficial · Microsoft Learn (Intune). Copilot embebido en el centro de administración de Intune (exploración de datos, políticas, troubleshooting y agentes) sin licencias adicionales de Intune, respetando RBAC y scope tags.
- [Security Copilot agents in Intune overview](https://learn.microsoft.com/en-us/intune/copilot/agents/) · Documentación · Oficial · Microsoft Learn · 1 abr 2026. Resume los agentes de Intune (Change Review, Device Offboarding, Policy Configuration, Vulnerability Remediation), prerrequisitos de SCU y pasos de activación.
- [Posture Prioritization Agent (Project Perception)](https://learn.microsoft.com/en-us/security/agentic-security/posture-prioritization-agent) · Documentación · Oficial · Vista previa · Nuevo · Microsoft Learn · 3 ago 2026. Agente de equipo verde que convierte hallazgos de postura de nube y dispositivos en un plan de remediación priorizado y explicado, general o enfocado en una amenaza. *Nota:* En preview es de solo lectura; playbooks 'Plan for posture remediation' y 'Protect against a threat'
- [Vulnerability Remediation Agent in Microsoft Intune](https://learn.microsoft.com/en-us/intune/copilot/agents/vulnerability-remediation-agent) · Documentación · Oficial · Vista previa · Microsoft Learn. Agente de Intune que usa datos de Defender Vulnerability Management para priorizar CVE en dispositivos gestionados y dar pasos guiados de remediación con Intune. *Nota:* Requiere Intune P1, SCU y MDE P2 o DVM Standalone; solo nube pública; usa un 'agentic user' con permisos delegados de lectura
- [Security Copilot in Microsoft Intune](https://learn.microsoft.com/en-us/intune/copilot/security-copilot) · Documentación · Oficial · Microsoft Learn (Intune). Uso del plugin de Intune desde la experiencia independiente con enfoque SOC (dispositivos, cumplimiento, comparación de equipos y Cloud PC) y prompts de ejemplo.
- [Remediate recommendations with Microsoft Security Copilot](https://learn.microsoft.com/en-us/azure/defender-for-cloud/remediate-with-copilot) · Documentación · Oficial · Nuevo · Microsoft Learn · 18 sep 2026. Paso a paso para resumir y corregir recomendaciones de Defender for Cloud con 'Fix with Copilot', incluyendo ejecución opcional de scripts.

**Manos a la obra**

1. `Laboratorio parcial` Incorpora dos o tres VM Windows de laboratorio a Intune y Defender for Endpoint con aplicaciones desactualizadas, configura el [Vulnerability Remediation Agent](https://learn.microsoft.com/en-us/intune/copilot/agents/vulnerability-remediation-agent), revisa la lista priorizada de CVE y valida cada una en Defender Vulnerability Management. Limitación: vista previa, requiere Defender for Endpoint P2 (incluido en la prueba de E5) o Defender Vulnerability Management Standalone, y consume SCU. Evidencia: CVE priorizadas y validadas, con las discrepancias anotadas.
2. `Laboratorio parcial` Con [Copilot en Intune](https://learn.microsoft.com/en-us/intune/copilot/), compara dos perfiles de configuración y pregunta por un dispositivo y por un script; después inicia sesión con un rol de Intune limitado por scope tag y verifica que Copilot no muestra dispositivos fuera de su alcance. Limitación: hay que completar la primera ejecución y consume SCU. Evidencia: capturas con ambos roles.
3. `Laboratorio parcial` En [Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/copilot-security-in-defender-for-cloud), resume una recomendación, remédiala con Copilot y delega otra a su responsable; anota qué funciones necesitaron Defender CSPM. Limitación: costo de los planes de Defender for Cloud y de los recursos de Azure. Evidencia: registro de las tres acciones.
4. `Laboratorio` Con las páginas de los agentes retirados de Intune, redacta un plan de salida para cualquier proceso que dependa de una función en vista previa: inventario de dependencias, alternativa manual, responsable, disparador de activación y fecha de revisión. Evidencia: plan de salida aplicado a un proceso real de tu equipo.
5. `Solo producción` Piloto del Vulnerability Remediation Agent sobre un grupo de dispositivos de producción. Cómo hacerlo seguro: roles separados (el owner configura y el contributor usa), validación de cada recomendación antes de crear la tarea de remediación, cambios por la ventana habitual de parches y medición del tiempo de remediación por criticidad antes y después ([casos de uso y métricas](00_Programa.md#casos-de-uso)). Evidencia: informe de tiempos de remediación.

<a id="m5"></a>

## M5 · Protección de datos y cumplimiento con Security Copilot

*L300 · ~4 h · Origen: Ninja oficial de 2024, parte 2, módulo 1 (plugin de Purview), ampliado con los agentes de Purview*

Embebido en **Microsoft Purview**, Copilot resume alertas de DLP y de riesgo interno, ayuda en Communication Compliance, en eDiscovery y en el explorador de actividad, y responde preguntas de postura en DSPM. El acceso a datos de Microsoft 365 se limita hoy a lo que Purview ya procesó: alertas de DLP e IRM, conjuntos de revisión de eDiscovery, coincidencias de Communication Compliance y DSPM.

Los agentes de Purview forman dos familias. Los de **triage** (Data Security Triage) priorizan alertas de **DLP** por contenido, exfiltración y política, y de **riesgo interno** por la actividad y el usuario; el de DLP solo tría alertas de políticas en modo activo —no en simulación—, archivos de hasta 2 MB y alertas de hasta 30 días antes de habilitarlo. Los de **postura** incluyen el **Data Security Posture Agent** de DSPM (vista previa, una instancia por tenant y dos prompts concurrentes) y el de **Data Security Investigations**, que busca credenciales expuestas. Todos leen contenido sensible, así que la identidad del agente, el alcance y el acuerdo con privacidad, Legal y RR. HH. van antes que la configuración. Los programas de Purview (DLP, riesgo interno y DSPM) profundizan cada producto.

**Por qué importa**

Los equipos de DLP y riesgo interno se ahogan en alertas: priorizar por contenido y riesgo permite atender primero lo que necesita atención —Microsoft reporta más de 40.000 alertas DLP procesadas por su agente en 90 días—. Pero estos agentes leen información sensible, por eso la identidad, el alcance y las reglas de privacidad se definen antes de encenderlos.

**Qué vas a lograr**

- Usar Copilot en Purview para resumir alertas de DLP e IRM y apoyar Communication Compliance y eDiscovery.
- Configurar el agente de triage de DLP con identidad de agente y saber qué alertas puede triar.
- Explicar las particularidades del triage de IRM y del Data Security Posture Agent.
- Acordar con privacidad, Legal y RR. HH. las reglas de uso de agentes sobre datos sensibles.

> **Atención.** El agente de triage de DLP solo procesa alertas de políticas en modo activo (no en simulación), archivos de hasta 2 MB y alertas generadas hasta 30 días antes de habilitarlo, y las clasifica en Needs attention, Less urgent o Not categorized. Los agentes de Purview no reconocen unidades administrativas ([agentes de Purview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-agents-overview)).

> **Atención.** El triage de riesgo interno corre en el contexto del último usuario que guardó la configuración y esa autenticación vence a los 90 días, mientras que la guía de DLP recomienda la identidad de agente. Usa Create and use agent identity siempre que puedas ([triage de IRM](https://learn.microsoft.com/en-us/purview/copilot-in-purview-triage-irm-agent-get-started), [triage de DLP](https://learn.microsoft.com/en-us/purview/copilot-in-purview-triage-dlp-agent-get-started)).

> **Novedad.** Licencias: los agentes de triage requieren la licencia del producto (DLP o riesgo interno; la ficha de Purview menciona Microsoft 365 E3, E5, A5, F5 o G5) más SCU, y el Data Security Posture Agent requiere Microsoft 365 E5 y SCU, con una instancia por tenant y dos prompts concurrentes como máximo ([agentes en Purview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-agents), [Posture Agent](https://learn.microsoft.com/en-us/purview/copilot-in-purview-posture-agent-get-started)). La experiencia no agéntica de Data Security Investigations se paga aparte.

> **Consejo Ninja.** Para conversar con privacidad: el acceso de Security Copilot a datos de Microsoft 365 se limita hoy a lo que Purview ya procesó —alertas de DLP e IRM, conjuntos de revisión de eDiscovery, coincidencias de Communication Compliance y DSPM— ([privacidad](https://learn.microsoft.com/en-us/copilot/security/privacy-data-security)). Los programas de Purview DLP, riesgo interno y DSPM profundizan cada producto; esta guía no reemplaza la asesoría legal.

**¿Tienes poco tiempo?**

- [Security Copilot Agents in Microsoft Purview overview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-agents-overview) · Documentación
- [Security Copilot in Microsoft Purview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-overview) · Documentación
- [Get started with the Microsoft Purview Triage Agent in Data Loss Prevention](https://learn.microsoft.com/en-us/purview/copilot-in-purview-triage-dlp-agent-get-started) · Documentación

### Documentación, cursos y credenciales

- [Security Copilot in Microsoft Purview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-overview) · Documentación · Oficial · Microsoft Learn (Purview). Capacidades embebidas e independientes en DSPM, DLP, Insider Risk, Communication Compliance y eDiscovery, incluidos resúmenes de alertas y promptbooks de DLP/IRM.
- [Get started with the Microsoft Purview Triage Agent in Data Loss Prevention](https://learn.microsoft.com/en-us/purview/copilot-in-purview-triage-dlp-agent-get-started) · Documentación · Oficial · Microsoft Learn. Despliegue del agente de triage DLP en Purview y Defender XDR: licencias, roles por grupo (admin/analista), identidad de agente recomendada y triggers.
- [Get started with the Microsoft Purview Triage Agent in Insider Risk Management](https://learn.microsoft.com/en-us/purview/copilot-in-purview-triage-irm-agent-get-started) · Documentación · Oficial · Microsoft Learn. Guía de despliegue del agente de triage de IRM con roles por grupo para administradores y analistas y requisitos de licencia y SCU.
- [Security Copilot Agents in Microsoft Purview overview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-agents-overview) · Documentación · Oficial · Microsoft Learn (Purview) · 23 mar 2026. Resume los agentes de Purview (triage de DLP e IRM, posture agent de DSPM y de Data Security Investigations en preview) y sus disparadores.
- [Get started with the Data Security Posture Agent (Microsoft Purview)](https://learn.microsoft.com/en-us/purview/copilot-in-purview-posture-agent-get-started) · Documentación · Oficial · Vista previa · Microsoft Learn. Despliegue del Posture Agent (preview) en DSPM y Data Security Investigations para descubrir datos sensibles con lenguaje natural, con identidad de agente recomendada. *Nota:* Requiere Microsoft 365 E5 y SCU; solo una instancia por tenant; máximo dos prompts concurrentes
- [Microsoft Security Copilot agents in Purview (preview)](https://learn.microsoft.com/en-us/purview/copilot-in-purview-agents) · Documentación · Oficial · Vista previa · Microsoft Learn · 24 feb 2026. Ficha de identidad, licencias, permisos, roles y trigger de los agentes de triage de Insider Risk Management y DLP. *Nota:* Ficha que indica que el agente corre como el administrador que lo activó y que la autenticación expira a los 90 días; la guía DLP más reciente ya ofrece identidad de agente

**Manos a la obra**

1. `Laboratorio parcial` Crea una política DLP en modo activo, acotada a usuarios de prueba y con acción de auditoría o notificación, genera dos alertas con archivos de prueba y resúmelas con [Copilot en Purview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-overview); compara cada resumen con tu lectura de la alerta. Limitación: alertas sintéticas y consumo de SCU. Evidencia: resúmenes y comparación.
2. `Laboratorio parcial` Haz cinco preguntas en lenguaje natural al [Data Security Posture Agent](https://learn.microsoft.com/en-us/purview/copilot-in-purview-posture-agent-get-started) sobre los datos sensibles de tu tenant de prueba y verifica dos respuestas en DSPM. Limitación: vista previa, datos de prueba, una instancia por tenant y dos prompts concurrentes como máximo. Evidencia: preguntas, respuestas y verificación.
3. `Laboratorio` Redacta la política de uso de agentes de Purview: qué agentes se activan, con qué identidad, sobre qué alcance, quién revisa sus clasificaciones, cuánto tiempo se conservan los resultados y quién aprueba los cambios; revísala con privacidad, Legal y RR. HH. Evidencia: política acordada con privacidad.
4. `Solo producción` Activa el [agente de triage de DLP](https://learn.microsoft.com/en-us/purview/copilot-in-purview-triage-dlp-agent-get-started), que necesita alertas reales de políticas en modo activo. Cómo hacerlo seguro: política acotada a un grupo piloto con acciones de auditoría o notificación (sin bloqueo), ejecución manual de una alerta a la vez al inicio, identidad de agente con roles de analista y revisión por muestreo de sus clasificaciones. Evidencia: muestra de veinte alertas con la clasificación del agente y la del analista.
5. `Solo producción` Evalúa el [agente de triage de riesgo interno](https://learn.microsoft.com/en-us/purview/copilot-in-purview-triage-irm-agent-get-started). Cómo hacerlo seguro: acuerdo previo con privacidad, Legal y RR. HH., seudonimización activa, identidad de agente en lugar de la de un administrador, alcance a un grupo piloto y revisión de cada priorización por un investigador autorizado. Evidencia: acta de aprobación y registro del piloto.

<a id="m6"></a>

## M6 · Agentes de Microsoft para operaciones de seguridad

*L300 · ~6 h · Origen: Ninja oficial de 2024, parte 2, módulo 5 (integraciones de terceros), reemplazado por el ecosistema de agentes*

Todos los agentes de Security Copilot comparten un **marco común**: un **disparador** (programado, por evento o manual), **permisos**, una **identidad** —una Microsoft Entra Agent ID dedicada, opción disponible para los agentes de Microsoft, o una cuenta de usuario cuyos permisos hereda—, los **plugins** y **productos** que necesita y el **acceso basado en roles** que define quién lo configura y quién ve sus resultados. Todos consumen SCU, ninguno se activa solo y se operan igual: ejecutar, pausar, dar feedback, gestionar su memoria, editar y quitar.

El ecosistema tiene cuatro capas. Los **agentes de Microsoft** por producto (el [inventario](00_Programa.md#inventario-agentes) registra 23, tres ya retirados); los **agentes de partners** del **Security Store**, una vitrina sobre Microsoft Marketplace con licencia del partner aparte y aprobación de un Global Administrator si acceden a datos de Microsoft; los **agentes propios** (módulo [A4](03_Nivel_3_Avanzado.md#a4)); y **Project Perception**, un sistema multiagente con agentes rojo, azul y verde coordinados por playbooks predefinidos por Microsoft y supervisados por personas.

Este módulo te da el método para evaluar, aprobar, configurar y priorizar agentes con el pool de SCU disponible.

**Por qué importa**

Los agentes no se encienden solos: cada uno es una decisión sobre datos, identidad, costo y riesgo. Una ficha de evaluación común evita aprobar agentes por entusiasmo y permite al CISO dirigir el pool de SCU hacia los agentes con más valor medible.

**Qué vas a lograr**

- Explicar los componentes comunes de un agente: disparador, permisos, identidad, plugins, productos y roles.
- Elegir entre identidad de agente y cuenta de usuario y justificar el mínimo privilegio.
- Evaluar y aprobar un agente de partner del Security Store.
- Distinguir los agentes de Security Copilot de los de Project Perception y sus playbooks.
- Priorizar qué agentes encender con el pool de SCU disponible.

> **Atención.** La opción de crear una identidad de agente (Microsoft Entra Agent ID) solo existe para los agentes creados por Microsoft; la alternativa es una cuenta de usuario, cuyos permisos hereda el agente ([agentes de Security Copilot](https://learn.microsoft.com/en-us/copilot/security/agents-overview)). Los agentes de partners que acceden a datos de productos Microsoft requieren la aprobación de un Global Administrator antes de que owners o contributors terminen la configuración ([configurar y gestionar agentes](https://learn.microsoft.com/en-us/copilot/security/agents-manage)).

> **Novedad.** El Security Store (vista previa desde septiembre de 2025) funciona sobre Microsoft Marketplace, con facturación de Microsoft, MACC y ofertas públicas o privadas. Para desplegar un agente de partner necesitas Contributor u Owner en la suscripción de facturación y Owner o Contributor de Security Copilot; el despliegue crea recursos de facturación, la instancia del agente y, si aplica, trabajos de notebooks del data lake de Sentinel ([qué es Security Store](https://learn.microsoft.com/en-us/security/store/what-is-security-store), [obtener agentes](https://learn.microsoft.com/en-us/security/store/customers/get-agents-in-security-store)).

> **Novedad.** Project Perception reúne agentes rojos (Recon), azules (Triage, Threat Intelligence, Attack Investigation y Detection Authoring) y verdes (Posture Prioritization) coordinados por playbooks que define Microsoft: en esta versión no se pueden crear playbooks propios ([conceptos de Perception](https://learn.microsoft.com/en-us/security/agentic-security/agentic-security-concepts)).

> **Consejo Ninja.** La certificación del Security Store rechaza agentes que solo envuelven un LLM y exige un plan multipaso y una estimación de consumo de SCU ([certificación del Store](https://learn.microsoft.com/en-us/security/store/partners/security-store-certification)). Usa esos mismos criterios para evaluar cualquier agente antes de aprobarlo.

**¿Tienes poco tiempo?**

- [Microsoft Security Copilot agents overview](https://learn.microsoft.com/en-us/copilot/security/agents-overview) · Documentación
- [Deploy AI agents in Microsoft Defender](https://learn.microsoft.com/en-us/defender-xdr/security-copilot-agents-defender) · Documentación
- [What is Microsoft Security Store?](https://learn.microsoft.com/en-us/security/store/what-is-security-store) · Documentación
- [Key concepts in Perception](https://learn.microsoft.com/en-us/security/agentic-security/agentic-security-concepts) · Documentación

**Ficha de evaluación de un agente antes de activarlo**

| Elemento | Qué revisar | Pregunta de gobierno | Evidencia esperada |
|---|---|---|---|
| Propósito y caso de uso | Tarea concreta, volumen y quién usa el resultado | ¿Qué decisión humana mejora o reemplaza? | Caso de uso con métrica de valor y línea base |
| Disparador | Programado, por evento o manual, y frecuencia | ¿Cuántas ejecuciones al mes y cuánto cuesta cada una? | Estimación mensual de SCU |
| Identidad | Entra Agent ID dedicada (agentes de Microsoft) o cuenta de usuario | ¿Quién es el sponsor? ¿La cuenta es compatible con PIM y TAP? | Identidad registrada con dueño y sponsor |
| Permisos | Roles y alcance que necesita la identidad | ¿Es el mínimo necesario? ¿Puede escribir o solo leer? | Lista de roles revisada |
| Plugins y productos | Plugins que habilita y licencias de los productos que lee | ¿Qué datos lee y desde qué productos? | Prerrequisitos verificados |
| Acciones y autonomía | Qué ejecuta solo y qué requiere aprobación | ¿Qué pasa si se equivoca? ¿La acción es reversible? | Fila en la matriz de autonomía (X1) |
| Licencia y costo | Licencia del producto o del partner y SCU por ejecución | ¿Sale del pool de E5/E7 o de capacidad aprovisionada? | Presupuesto y umbral de consumo |
| Datos y privacidad | Contenido sensible, residencia y retención | ¿Lo aprobó privacidad? ¿Sus mensajes cruzan fronteras? | Aprobación de privacidad |
| Calidad | Precisión, errores y uso del feedback | ¿Cómo se mide y quién revisa las salidas? | Plan de muestreo y métrica de calidad |
| Estado y salida | Disponibilidad general o vista previa y fecha de revisión | ¿Qué hacemos si se retira o cambia su precio? | Plan de salida documentado |

Propuesta de esta guía basada en [configurar y gestionar agentes](https://learn.microsoft.com/en-us/copilot/security/agents-manage), [agentes de Security Copilot](https://learn.microsoft.com/en-us/copilot/security/agents-overview) y la [Application card de los agentes](https://learn.microsoft.com/en-us/copilot/security/security-copilot-application-card-agents).

### Documentación, cursos y credenciales

- [Deploy AI agents in Microsoft Defender](https://learn.microsoft.com/en-us/defender-xdr/security-copilot-agents-defender) · Documentación · Oficial · Nuevo · Microsoft Learn · 5 ago 2026. Catálogo de agentes de Security Copilot en Defender (Alert Triage, TI Briefing, Threat Hunting Assistant, Security Analyst, Dynamic Threat Detection) con licencias, permisos y despliegue desde Security Store.
- [Learn about Security Copilot for Microsoft 365 E5 and E7 customers](https://learn.microsoft.com/en-us/copilot/security/security-copilot-inclusion) · Documentación · Oficial · Nuevo · Microsoft Learn · 19 jun 2026. FAQ oficial de la inclusión de Security Copilot en Microsoft 365 E5/E7: 400 SCU al mes por cada 1.000 licencias de usuario de pago (tope 10.000), despliegue desde el 18-nov-2025, qué incluye y qué no.
- [Get agents in Microsoft Security Store](https://learn.microsoft.com/en-us/security/store/customers/get-agents-in-security-store) · Documentación · Oficial · Nuevo · Microsoft Learn · 28 may 2026. Pasos para comprar y desplegar un agente: suscripción de facturación Azure, recursos (incluidos jobs de notebooks del data lake de Sentinel) y configuración en Security Copilot.
- [What is Microsoft Security Store?](https://learn.microsoft.com/en-us/security/store/what-is-security-store) · Documentación · Oficial · Microsoft Learn. Define Security Store como vitrina de seguridad sobre la infraestructura de Microsoft Marketplace para encontrar, comprar (incluido MACC, ofertas públicas o privadas) y desplegar agentes y soluciones.
- [Microsoft Security Copilot Security Compute Units and capacity](https://learn.microsoft.com/en-us/copilot/security/security-compute-units-capacity) · Documentación · Oficial · Microsoft Learn · 29 abr 2026. Define las SCU y compara capacidad aprovisionada (mínimo 1 SCU, bloques de hora de reloj, sin acumulación), overage (facturación por consumo con décimas) y capacidad de inclusión E5/E7, con ejemplos de facturación.
- [What's new in Microsoft Security Copilot?](https://learn.microsoft.com/en-us/copilot/security/whats-new-copilot-security) · Documentación · Oficial · Microsoft Learn · 17 abr 2026. Registro mensual oficial de novedades (agentes, inclusión E5, workspaces, overage, auditoría de agentes en Purview, GPT-4.1, idiomas, residencia de datos) indicando si cada cambio aplica a la experiencia independiente o embebida.
- [Microsoft Security Copilot agents overview](https://learn.microsoft.com/en-us/copilot/security/agents-overview) · Documentación · Oficial · Microsoft Learn · 18 mar 2026. Página base que define qué es un agente de Security Copilot, su terminología (trigger, permisos, identidad Agent ID o cuenta de usuario, plugins) y el recorrido descubrir-configurar-extender.
- [Microsoft Security Copilot agents](https://learn.microsoft.com/en-us/copilot/security/agents-security-copilot) · Documentación · Oficial · Microsoft Learn · 18 mar 2026. Índice oficial de agentes en experiencia independiente (Threat Intelligence Briefing) y enlaces a los catálogos embebidos de Entra, Defender, Intune, Purview y Sentinel.
- [Agent categories in Project Perception](https://learn.microsoft.com/en-us/security/agentic-security/agentic-security-agent-categories) · Documentación · Oficial · Vista previa · Nuevo · Microsoft Learn · 29 oct 2026. Describe los equipos rojo, azul y verde de agentes de Perception y cómo colaboran en el playbook 'Protect against a threat' con aprobación humana.
- [Perception documentation](https://learn.microsoft.com/en-us/security/agentic-security/) · Documentación · Oficial · Vista previa · Microsoft Learn. Hub de documentación de Perception con conceptos, agentes red/blue/green (Recon, Attack Investigation, Detection Authoring, Triage, Threat Intelligence, Posture Prioritization), playbooks, sesiones y ficha de IA responsable.
- [Key concepts in Perception](https://learn.microsoft.com/en-us/security/agentic-security/agentic-security-concepts) · Documentación · Oficial · Vista previa · Microsoft Learn. Conceptos de Project Perception: sesiones, agentes (Recon, Triage, Threat Intelligence, Attack Investigation, Detection Authoring, Posture Prioritization) y playbooks multiagente. *Nota:* Perception está en Limited Public Preview por invitación; playbooks predefinidos por Microsoft y de solo lectura
- [Project Perception | Microsoft Security](https://www.microsoft.com/en-in/security/business/ai-powered-cybersecurity/project-perception-agentic-system) · Documentación · Oficial · Vista previa · Microsoft Security. Página de producto y FAQ de Perception: diferencia con Security Copilot ('AI that acts' vs 'AI that assists'), acceso en Defender y precio por consumo en SCU. *Nota:* Indica pago por uso medido en SCU, con consumo distinto por agente
- [Attack Investigation Agent (Project Perception)](https://learn.microsoft.com/en-us/security/agentic-security/attack-investigation-agent) · Documentación · Oficial · Vista previa · Microsoft Learn. Investigador autónomo de nivel 2 que reconstruye la historia completa del ataque desde una alerta o incidente de Defender, con veredicto, cronología, IOC y acciones de remediación. *Nota:* Requiere Microsoft 365 E5, Defender XDR y onboarding al data lake; la identidad del agente debe agregarse a los grupos de dispositivos de MDE
- [Detection Authoring Agent in Microsoft Defender (Project Perception)](https://learn.microsoft.com/en-us/security/agentic-security/detection-authoring-agent) · Documentación · Oficial · Vista previa · Microsoft Learn. Agente que, a partir de TTP extraídas por el TI Agent, propone detecciones KQL con enriquecimiento MITRE, estimación de volumen y reglas existentes que ya cubren el comportamiento. *Nota:* La detección solo se activa cuando el analista la guarda en el asistente de detección personalizada (humano en el circuito)
- [Use Microsoft Security Store to find, buy, and deploy security solutions and agents](https://learn.microsoft.com/en-us/security/store/customers/find-security-agents-solutions-and-more-for-purchase-in-security-store) · Documentación · Oficial · Nuevo · Microsoft Learn · 28 may 2026. Guía del cliente de Security Store: Advisor en lenguaje natural, agentes por portal (Entra, Defender, Security Copilot), soluciones por NIST CSF 2.0 y soporte.
- [Microsoft Security Copilot in your workflows](https://learn.microsoft.com/en-us/copilot/security/workflows-overview) · Documentación · Oficial · Nuevo · Microsoft Learn · 1 may 2026. Explica cómo combinar agentes, plugins, conectores y promptbooks por persona (administrador, analista, desarrollador) y cuándo usar cada enfoque.
- [Security Copilot agents in Microsoft 365 E5](https://www.microsoft.com/en-us/security/security-copilot-in-microsoft-365-e5) · Documentación · Oficial · Microsoft Security. Página de producto de los agentes incluidos en Microsoft 365 E5 con FAQ del beneficio de SCU y enlaces a adopción, blog y talleres.
- [Microsoft Security Copilot – Pricing](https://www.microsoft.com/en-ie/security/pricing/microsoft-security-copilot) · Documentación · Oficial · Microsoft Security. Precios y FAQ de SCU aprovisionadas y overage, con ejemplo de facturación y confirmación de la inclusión para Microsoft 365 E5 y E7.
- [Discover agents in Microsoft Security Copilot](https://learn.microsoft.com/en-us/copilot/security/discover-agents) · Documentación · Oficial · Microsoft Learn · 18 mar 2026. Cómo encontrar agentes de Microsoft y de partners en la biblioteca del portal independiente, en los portales embebidos y en Security Store.
- [Partner-built agents](https://learn.microsoft.com/en-us/copilot/security/agents-other) · Documentación · Oficial · Microsoft Learn · 18 mar 2026. Explica el ecosistema de agentes de partners (respuesta a brechas de privacidad, supervisión de red, triage) y remite a Security Store para el catálogo vigente.
- [Triage Agent (Project Perception)](https://learn.microsoft.com/en-us/security/agentic-security/triage-agent) · Documentación · Oficial · Vista previa · Nuevo · Microsoft Learn · 30 jul 2026. Agente de triage de Perception que clasifica alertas de Defender (correo, nube/contenedores, identidad) y puede dispararse automáticamente con reglas. *Nota:* Comparte capacidades con el Security Alert Triage Agent; ms.date 07/30/2026 según el repo público
- [Use the Recon Agent in Project Perception](https://learn.microsoft.com/en-us/security/agentic-security/recon-agent) · Documentación · Oficial · Vista previa · Microsoft Learn. Agente de equipo rojo que hace reconocimiento de solo lectura en Azure para revelar rutas de ataque desde cualquier activo o identidad y priorizar puntos de estrangulamiento. *Nota:* Complementa Exposure Management con análisis de 'assumed breach'

### Anuncios y blogs oficiales

- [Reimagining the SOC for the agentic era in Microsoft Defender](https://www.microsoft.com/en-us/security/blog/2026/09/23/reimagining-the-soc-for-the-agentic-era-in-microsoft-defender/) · Blog oficial · Empleado de Microsoft · Nuevo · Rob Lefferts · Microsoft Security Blog · 23 sep 2026. Anuncia el ISOC (integrated SOC) en Microsoft Defender, que une SIEM y protección como base para que agentes y personas operen con el mismo contexto.
- [The agentic SOC—Rethinking SecOps for the next decade](https://www.microsoft.com/en-us/security/blog/2026/04/09/the-agentic-soc-rethinking-secops-for-the-next-decade/) · Blog oficial · Empleado de Microsoft · Rob Lefferts; David Weston · Microsoft Security Blog · 9 abr 2026. Define el SOC agéntico en dos capas (disrupción determinista + agentes que razonan) y enlaza al whitepaper 'The agentic SOC: Your teammate for tomorrow, today'.
- [Agents built into your workflow: Get Security Copilot with Microsoft 365 E5](https://www.microsoft.com/en-us/security/blog/2025/11/18/agents-built-into-your-workflow-get-security-copilot-with-microsoft-365-e5/) · Blog oficial · Empleado de Microsoft · Dorothy Li · Microsoft Security Blog · 18 nov 2025. Anuncio oficial de la inclusión de Security Copilot en Microsoft 365 E5 con 12 nuevos agentes de Microsoft y más de 30 de partners, y aviso de 30 días antes de la activación.
- [Rethinking security for the age of AI](https://blogs.microsoft.com/blog/2026/07/27/rethinking-security-for-the-age-of-ai/) · Blog oficial · Empleado de Microsoft · Vista previa · Nuevo · Hayete Gallot · The Official Microsoft Blog · 27 jul 2026. Anuncio de Project Perception, un sistema agéntico con agentes red, blue y green, arquitectura multimodelo (incluido MAI-Cyber-1-Flash) y preview pública a partir del 3 de agosto. *Nota:* El blog habla de 'public preview' el 3-ago-2026, mientras que Learn la describe como 'Limited Public Preview' por invitación
- [What's new in Microsoft Security: July 2026](https://www.microsoft.com/en-us/security/blog/2026/07/30/whats-new-in-microsoft-security-july-2026/) · Blog oficial · Empleado de Microsoft · Nuevo · Alym Rayani · Microsoft Security Blog · 30 jul 2026. Novedades de julio 2026: Project Perception, protección contra prompt injection en correo, Threat Intelligence Agent mejorado y convergencia de Defender Threat Intelligence.
- [Secure agentic AI end-to-end (RSAC 2026)](https://www.microsoft.com/en-us/security/blog/2026/03/20/secure-agentic-ai-end-to-end/) · Blog oficial · Empleado de Microsoft · Vasu Jakkal · Microsoft Security Blog · 20 mar 2026. Anuncios de Microsoft para RSAC 2026: asegurar agentes, cimientos y defender con agentes y expertos; confirma que E7 incluye Agent 365, Microsoft 365 Copilot, Entra Suite y E5.
- [Microsoft unveils Microsoft Security Copilot agents and new protections for AI](https://www.microsoft.com/en-us/security/blog/2025/03/24/microsoft-unveils-microsoft-security-copilot-agents-and-new-protections-for-ai/) · Blog oficial · Empleado de Microsoft · Legado aún útil · Vasu Jakkal · Microsoft Security Blog · 24 mar 2025. Anuncio original (marzo 2025) de los seis primeros agentes de Microsoft: Phishing Triage, Alert Triage de Purview, CA Optimization, Vulnerability Remediation y TI Briefing. *Nota:* Contexto histórico; varios agentes cambiaron de nombre o estado desde entonces

### Webinars, videos y podcasts

- [Microsoft Security Copilot video hub](https://adoption.microsoft.com/en-us/security-copilot/video-hub/) · Video · Oficial · Microsoft Adoption. Colección oficial de vídeos cortos y deep dives (agentes, funciones, partners y casos de clientes), incluida la guía rápida y el vídeo de configuración inicial y asignación de usuarios.
- [Microsoft Security Copilot agents (Microsoft Mechanics)](https://www.youtube.com/watch?v=al9OSFGqd8I) · Video · Empleado de Microsoft · Dilip Radhakrishnan · Microsoft Mechanics · 3 oct 2025. Demo de 8 minutos de agentes (triage de phishing y alertas, revisiones de acceso, optimización de Acceso Condicional, remediación de vulnerabilidades) y creación de agentes propios.

### Laboratorios, GitHub y herramientas

- [Microsoft Security Store (portal)](https://securitystore.microsoft.com/) · Herramienta · Oficial · Microsoft. Portal público de Security Store para explorar agentes de Microsoft y partners, soluciones e integraciones, con asesor conversacional y compra con facturación Microsoft/MACC.
- [MC1261596 - Notice: Security Copilot will be included as part of your Microsoft 365 E5 plan soon](https://mc.merill.net/message/MC1261596) · Herramienta · Comunidad · Microsoft 365 Message Center Archive (merill.net) · 25 mar 2026. Aviso del Message Center sobre el despliegue escalonado de Security Copilot en E5 (20-abr a 30-jun-2026) y lo que no está incluido (data lake de Sentinel, Logic Apps, agentes de terceros).

### Comunidad: blogs, libros, newsletters y eventos

- [Your complete guide to Microsoft experiences at RSAC 2026 Conference](https://www.microsoft.com/en-us/security/blog/2026/02/12/your-complete-guide-to-microsoft-experiences-at-rsac-2026-conference/) · Evento · Oficial · Microsoft Security Blog · 12 feb 2026. Agenda de Microsoft en RSAC 2026 (22-26 marzo, San Francisco): Pre-Day, sesiones ejecutivas sobre agentes y foros posteriores.

**Manos a la obra**

1. `Laboratorio` Con el [inventario de agentes](00_Programa.md#inventario-agentes) y la ficha de evaluación de este módulo, evalúa tres agentes candidatos para tu organización: propósito, licencia, roles, identidad, disparador, datos que lee, costo estimado, riesgo y métrica de éxito. Evidencia: tres fichas de evaluación con una recomendación.
2. `Laboratorio` Recorre el [Security Store](https://securitystore.microsoft.com/) sin comprar y compara tres agentes de partners: editor, permisos, productos requeridos, modelo de facturación y si necesitan el consentimiento de un Global Administrator; redacta una checklist de aprobación. Evidencia: checklist de aprobación de agentes de partners.
3. `Laboratorio parcial` En Security Copilot y en Defender (Security Copilot > Agents), recorre [Discover agents](https://learn.microsoft.com/en-us/copilot/security/discover-agents) y la vista Ready for setup, configura un agente de Microsoft de bajo riesgo con identidad de agente y practica ejecutarlo, pausarlo, darle feedback y quitarlo ([configurar y gestionar agentes](https://learn.microsoft.com/en-us/copilot/security/agents-manage)). Limitación: consumo de SCU por ejecución. Evidencia: registro de cada operación con hora y resultado.
4. `Laboratorio` Ejercicio de gobierno de mesa: con la [Application card de los agentes](https://learn.microsoft.com/en-us/copilot/security/security-copilot-application-card-agents), define dueño y sponsor por agente, rol mínimo, umbral de costo mensual y el procedimiento para pausar un agente, rechazar su feedback y rotar su identidad. Evidencia: procedimiento revisado por el líder del SOC.
5. `Solo producción` Ejecuta un playbook de Project Perception (por ejemplo, Investigate attack) si tu tenant fue invitado a la vista previa limitada, que exige Microsoft 365 E5, Defender XDR y data lake ([Attack Investigation Agent](https://learn.microsoft.com/en-us/security/agentic-security/attack-investigation-agent)). Cómo hacerlo seguro: correrlo sobre un incidente ya cerrado, practicar aprobar, rechazar y sugerir una alternativa, detener la sesión al terminar y dar Security Reader al equipo que aprende. Evidencia: sesión revisada con cada decisión anotada.
6. `Solo producción` Reparte el pool de SCU de E5/E7 entre agentes y casos de uso para el próximo mes con datos reales del [panel de uso](https://learn.microsoft.com/en-us/copilot/security/manage-usage). Cómo hacerlo seguro: decisión en comité, umbral de consumo por agente, revisión semanal y pausa del agente que supere su umbral hasta revisar su valor. Evidencia: asignación mensual aprobada.

**¿Quieres profundizar?**

- [Microsoft Security Copilot agents (Microsoft Mechanics)](https://www.youtube.com/watch?v=al9OSFGqd8I) · Video
- [Microsoft Security Copilot video hub](https://adoption.microsoft.com/en-us/security-copilot/video-hub/) · Video
- [Microsoft Security Store (portal)](https://securitystore.microsoft.com/) · Herramienta
- [MC1261596 - Notice: Security Copilot will be included as part of your Microsoft 365 E5 plan soon](https://mc.merill.net/message/MC1261596) · Herramienta

<a id="m7"></a>

## M7 · Gobierno: roles, privacidad, uso, costos y auditoría

*L300 · ~5 h · Origen: Ninja oficial de 2024, parte 1, módulo 2, y parte 2, módulo 4 (autenticación, roles y gestión de plugins)*

Security Copilot tiene roles propios —**owner** y **contributor**, que no son roles de Entra— y nunca supera los permisos del usuario en cada plugin: un contributor sin rol en Sentinel no ve incidentes de Sentinel. Siempre debe haber dos owners, las asignaciones admiten solo grupos asignables a roles y el grupo Everyone se puede quitar pero no volver a asignar. Para proveedores de servicios existen el cambio de tenant (B2B), GDAP y Azure Lighthouse.

La **privacidad** se documenta: los datos no se comparten con OpenAI ni entrenan los modelos base, se cifran en reposo y la compartición de datos con Microsoft se decide por workspace; los mensajes de agentes por correo o Teams pueden cruzar fronteras en tránsito. La **auditoría** combina el registro unificado de Purview (eventos de administración y de agentes), **DSPM for AI** (pares prompt-respuesta) y la **Export API**. El **acceso condicional** puede dirigirse a los service principals de Security Copilot —las políticas de *Protect AI* cubren la experiencia independiente, no la embebida—, y el **panel de uso** muestra 90 días de consumo por experiencia, usuario, plugin y categoría.

**Por qué importa**

Un auditor o un regulador preguntará quién puede usarlo, qué datos ve, dónde se procesan y cuánto cuesta. Responder con evidencia —roles, registros, ubicación y consumo— es lo que permite a una organización regulada de MCSA encender agentes sin frenar meses en comités.

**Qué vas a lograr**

- Asignar los roles owner y contributor con grupos asignables a roles y mantener dos owners.
- Explicar la autenticación on-behalf-of y su efecto en el acceso a datos.
- Configurar privacidad, residencia y auditoría (registro unificado, DSPM for AI y Export API).
- Proteger el acceso a Security Copilot con acceso condicional.
- Monitorear y exportar el consumo de SCU por experiencia, usuario, plugin y categoría.

> **Atención.** Los roles owner y contributor de Security Copilot no son roles de Entra: siempre deben quedar dos owners, las asignaciones admiten solo grupos asignables a roles y el grupo Everyone puede quitarse, pero no volver a asignarse. Copilot nunca supera los permisos del usuario en cada plugin: para ver incidentes de Sentinel hace falta, por ejemplo, Microsoft Sentinel Reader ([autenticación](https://learn.microsoft.com/en-us/copilot/security/authentication)).

> **Novedad.** Auditoría en dos capas: el registro unificado de Purview guarda eventos de administración y metadatos —la auditoría de la gestión de agentes está en disponibilidad general desde julio de 2025— y DSPM for AI guarda los pares prompt-respuesta. La retención por defecto es de 180 días, el registro se activa en Owner settings y los eventos pueden tardar hasta 24 horas; la Export API permite a los owners exportar prompts, respuestas y evaluaciones ([registro de auditoría](https://learn.microsoft.com/en-us/copilot/security/audit-log), [Export API](https://learn.microsoft.com/en-us/copilot/security/activity-export-api)).

> **Atención.** Las políticas de acceso condicional de Protect AI aplican a la experiencia independiente, no a la embebida, y se crean en modo solo informe. Microsoft recomienda cubrir «todos los recursos» y, para dirigirte a Security Copilot, usar sus service principals con atributos de seguridad personalizados ([solución de problemas de acceso condicional](https://learn.microsoft.com/en-us/entra/identity/conditional-access/troubleshoot-security-copilot-policies), [política Protect AI](https://raw.githubusercontent.com/MicrosoftDocs/entra-docs/main/docs/identity/conditional-access/policy-all-users-copilot-ai-security.md)).

> **Consejo Ninja.** Para privacidad: los datos no se comparten con OpenAI ni se usan para entrenar los modelos base, se cifran con AES-256 en reposo, la recolección de feedback solo se desactiva por ticket de soporte y los mensajes de agentes por correo o Teams pueden cruzar fronteras geográficas en tránsito ([privacidad](https://learn.microsoft.com/en-us/copilot/security/privacy-data-security)). Las contradicciones sobre compartición y retención de datos están en [Metodología y fuentes](08_Cierre_glosario_y_fuentes.md#metodologia).

**¿Tienes poco tiempo?**

- [Understand authentication in Microsoft Security Copilot](https://learn.microsoft.com/en-us/copilot/security/authentication) · Documentación
- [Privacy and data security in Microsoft Security Copilot](https://learn.microsoft.com/en-us/copilot/security/privacy-data-security) · Documentación
- [Access the Security Copilot audit log](https://learn.microsoft.com/en-us/copilot/security/audit-log) · Documentación
- [Manage security compute unit usage in Security Copilot](https://learn.microsoft.com/en-us/copilot/security/manage-usage) · Documentación

### Documentación, cursos y credenciales

- [Application card: Microsoft Security Copilot](https://learn.microsoft.com/en-us/copilot/security/security-copilot-application-card) · Documentación · Oficial · Nuevo · Microsoft Learn · 22 jun 2026. Ficha de IA responsable que reemplaza a la antigua FAQ de RAI: glosario, usos previstos, modelos (Azure OpenAI vía Foundry, sin entrenamiento con datos del cliente), limitaciones, evaluaciones, mitigaciones y buenas prácticas para desplegadores y usuarios.
- [Manage security compute unit usage in Security Copilot](https://learn.microsoft.com/en-us/copilot/security/manage-usage) · Documentación · Oficial · Nuevo · Microsoft Learn · 4 jun 2026. Describe el panel de uso (90 días, por capacidad, sesión, usuario, plugin, experiencia y categoría), exportación a Excel, avisos al acercarse al límite, cambio de SCU aprovisionadas/overage y borrado de capacidad.
- [Understand authentication in Microsoft Security Copilot](https://learn.microsoft.com/en-us/copilot/security/authentication) · Documentación · Oficial · Nuevo · Microsoft Learn · 4 jun 2026. Explica la autenticación on-behalf-of, los roles Copilot owner/contributor (no son roles de Entra), roles que heredan owner, grupo de roles recomendados, sesiones compartidas y escenarios multitenant (B2B, GDAP, Lighthouse).
- [Access the Security Copilot audit log](https://learn.microsoft.com/en-us/copilot/security/audit-log) · Documentación · Oficial · Microsoft Learn. Explica cómo habilitar el registro en Microsoft Purview (UAL para eventos de administración y metadatos de actividad; DSPM for AI para pares prompt-respuesta) y cómo consultarlo, con retención por defecto de 180 días.
- [Privacy and data security in Microsoft Security Copilot](https://learn.microsoft.com/en-us/copilot/security/privacy-data-security) · Documentación · Oficial · Microsoft Learn · 8 abr 2026. Detalla datos de cliente vs. logs del sistema, opciones de compartición de datos, acceso a datos de M365 vía Purview, ubicación de almacenamiento por workspace, retención/borrado (180 días) y ubicación de evaluación de prompts.
- [Manage plugins and agents in Microsoft Security Copilot (módulo)](https://learn.microsoft.com/en-us/training/modules/manage-plugins-agents-security-copilot/) · Curso · Oficial · Microsoft Learn. Módulo de 24 minutos sobre gobierno de plugins (alcance usuario/organización), restricción de preinstalados y ciclo de vida de agentes de Microsoft y de partners del Security Store, incluida la aprobación del Global Administrator.
- [Export Activity in Security Copilot (Admin Export API)](https://learn.microsoft.com/en-us/copilot/security/activity-export-api) · Documentación · Oficial · Microsoft Learn. API para que los owners del workspace exporten de forma paginada prompts, respuestas y evaluaciones, autenticando con usuario owner o service principal dentro de un grupo asignable a roles.
- [Troubleshoot Conditional Access policies for Microsoft Security Copilot](https://learn.microsoft.com/en-us/entra/identity/conditional-access/troubleshoot-security-copilot-policies) · Documentación · Oficial · Microsoft Learn (Microsoft Entra) · 8 abr 2026. Recomienda aplicar Acceso Condicional dirigido a todos los recursos y, si se quiere apuntar a Security Copilot, usar atributos de seguridad personalizados sobre sus service principals (Portal, API, Agent Management y conector de Logic Apps).
- [Protect AI with Conditional Access policy (fuente Markdown en GitHub MicrosoftDocs/entra-docs)](https://raw.githubusercontent.com/MicrosoftDocs/entra-docs/main/docs/identity/conditional-access/policy-all-users-copilot-ai-security.md) · Documentación · Oficial · Microsoft (repositorio público MicrosoftDocs) · 1 abr 2025. Guía oficial para crear el service principal de Security Copilot y políticas de Acceso Condicional (MFA resistente a phishing, dispositivo conforme o bloqueo según riesgo interno) en modo solo informe para la experiencia independiente.

### Comunidad: blogs, libros, newsletters y eventos

- [Security Copilot in Microsoft 365 E5: What Should You Govern First?](https://i3solutions.com/answers/security-copilot-e5-governance/) · Blog · Comunidad · Nuevo · Michael Branson · i3solutions · sep 2026. Lista de decisiones de gobierno antes de activar agentes con la inclusión E5: grupos asignables a roles, restricción de plugins, acceso a datos de M365, ubicación del workspace, auditoría y DSPM for AI e identidad por agente.

**Manos a la obra**

1. `Laboratorio parcial` Configura los roles de Security Copilot: quita el grupo Everyone (no podrás volver a asignarlo), asigna contributors mediante un grupo asignable a roles y verifica la regla de dos owners ([autenticación](https://learn.microsoft.com/en-us/copilot/security/authentication)). Limitación: requiere capacidad activa. Evidencia: capturas de la configuración de roles.
2. `Laboratorio parcial` Crea el service principal de Security Copilot y una política de acceso condicional en solo informe que exija MFA resistente al phishing ([política Protect AI](https://raw.githubusercontent.com/MicrosoftDocs/entra-docs/main/docs/identity/conditional-access/policy-all-users-copilot-ai-security.md)); revisa su efecto en los registros de inicio de sesión. Limitación: solo cubre la experiencia independiente y requiere Entra ID P1 (incluido en la prueba de E5). Evidencia: política en solo informe y resultado en los registros.
3. `Laboratorio parcial` Activa el registro en Purview desde Owner settings, busca eventos de Security Copilot en el registro unificado de auditoría y prueba la consulta comunitaria sobre CloudAppEvents para la gestión de agentes ([registro de auditoría](https://learn.microsoft.com/en-us/copilot/security/audit-log), [notas operativas](https://techcommunity.microsoft.com/discussions/microsoftthreatprotection/operational-notes-on-microsoft-security-copilot-agents-in-defender-xdr-and-micro/4525826)). Limitación: los eventos pueden tardar hasta 24 horas y el contenido de los prompts solo aparece vía DSPM for AI. Evidencia: eventos encontrados y consulta guardada.
4. `Laboratorio parcial` En el [panel de uso](https://learn.microsoft.com/en-us/copilot/security/manage-usage), filtra por experiencia, usuario, plugin y categoría (Prompt, Promptbook, Agent y Primitive), exporta a Excel y arma un tablero mensual de costo por caso de uso. Limitación: poco volumen en el laboratorio. Evidencia: tablero alimentado con la exportación de tu sesión de laboratorio.
5. `Laboratorio` Escribe la política de gobierno de una página —roles y grupos, plugins permitidos, datos que no se suben, compartición de sesiones, ubicación de datos, auditoría y retención, presupuesto y excedente, identidad por agente y revisión trimestral—, apoyándote en el módulo [Manage plugins and agents](https://learn.microsoft.com/en-us/training/modules/manage-plugins-agents-security-copilot/). Evidencia: política aprobada por el CISO.
6. `Solo producción` Haz una revisión de gobierno previa a activar agentes en el tenant real: roles, plugins, acceso a datos de Microsoft 365, ubicación, auditoría e identidad por agente ([qué gobernar primero](https://i3solutions.com/answers/security-copilot-e5-governance/)). Cómo hacerlo seguro: auditoría en modo lectura y cambios por ventana de mantenimiento con plan de reversión. Evidencia: informe de brechas con dueños y fechas.

<a id="reto-intermedio"></a>

## Reto del nivel

**Encender un agente con criterio.** Elige un agente de Microsoft del [inventario](00_Programa.md#inventario-agentes) que resuelva un problema real de tu SOC. Entrega: la ficha de evaluación de [M6](#m6), la configuración con identidad de agente y permisos mínimos en el laboratorio (o el plan de producción si el agente lo exige), la política de gobierno de una página aprobada ([M7](#m7)) y un plan de piloto de dos semanas con línea base, métricas de calidad y costo, umbral de pausa y criterio para ampliar o apagar el agente.

<a id="quiz-intermedio"></a>

## Evaluación del nivel

Responde y compara con [Evaluaciones y respuestas](06_Evaluaciones_y_respuestas.md#eval-intermedio). Con 80 % o más, ¡nivel aprobado! (En la versión web puedes corregir en línea y generar tu certificado).

1. ¿Qué tipo de alerta tría el Security Alert Triage Agent en disponibilidad general?
   - a) Identidad
   - b) Nube y contenedores
   - c) Correo y colaboración
   - d) Todas las anteriores

2. Configuraste el agente de triage de correo reportado, pero no clasifica nada. ¿Cuál es la causa más probable?
   - a) Falta un workspace de Sentinel
   - b) La regla de ajuste Auto-Resolve resuelve las alertas de correo reportado antes de que el agente las vea
   - c) Falta la licencia de Defender EASM
   - d) El tenant no tiene Intune

3. ¿Cómo se cobra hoy el Dynamic Threat Detection Agent?
   - a) Es gratuito durante la vista previa y consumirá SCU al llegar a disponibilidad general
   - b) 1 SCU por alerta generada
   - c) Con una licencia aparte en el Security Store
   - d) Solo está incluido en E7

4. Al configurar un agente de Microsoft en Defender, ¿qué identidad se recomienda?
   - a) Una cuenta de Global Administrator para evitar errores de permisos
   - b) Una cuenta de usuario protegida con PIM
   - c) Una cuenta compartida del SOC
   - d) Una nueva Microsoft Entra Agent ID con permisos mínimos

5. El informe de exposición del Threat Intelligence Briefing Agent aparece como «not available». ¿Qué revisas primero?
   - a) La licencia de E7
   - b) El plugin de Purview
   - c) Los permisos de lectura de la identidad del agente sobre Defender for Endpoint y los grupos de dispositivos
   - d) El rol de Global Administrator del usuario

6. ¿En qué estado crea las políticas nuevas el Conditional Access Optimization Agent y qué licencia mínima exige?
   - a) Activas; Entra ID P2
   - b) En modo solo informe; Entra ID P1
   - c) Deshabilitadas; Entra Suite
   - d) Activas; Entra ID P1

7. ¿Qué afirmación sobre el Identity Risk Management Agent es correcta?
   - a) Remedia automáticamente a los usuarios en riesgo
   - b) Analiza identidades de carga de trabajo
   - c) No consume SCU
   - d) Analiza hasta 100 usuarios en riesgo por ejecución y una persona aprueba cada recomendación

8. Al 6 de noviembre de 2026, ¿qué agente de Intune sigue disponible?
   - a) Policy Configuration Agent
   - b) Change Review Agent
   - c) Device Offboarding Agent
   - d) Vulnerability Remediation Agent

9. ¿Qué alertas DLP NO tría el agente de triage de Purview?
   - a) Las de Exchange Online
   - b) Las de Teams
   - c) Las de políticas en modo simulación
   - d) Las de dispositivos

10. ¿Para qué agentes existe en Security Copilot la opción de crear una identidad de agente (Entra Agent ID)?
   - a) Solo para los agentes creados por Microsoft
   - b) Para todos los agentes, incluidos los de partners
   - c) Solo para los agentes personalizados
   - d) Para ninguno: siempre se usa una cuenta de usuario

11. Quieres desplegar un agente de partner que accede a datos de productos Microsoft. ¿Qué aprobación adicional necesitas?
   - a) La de un Global Administrator antes de que owners o contributors terminen la configuración
   - b) La de un Security Reader
   - c) Ninguna, basta con ser contributor
   - d) La del soporte de Microsoft

12. ¿Qué caracteriza a los playbooks de Project Perception en su versión actual?
   - a) Cada SOC escribe los suyos en YAML
   - b) Los define Microsoft y no se pueden crear playbooks propios
   - c) Son flujos de Logic Apps
   - d) Se compran en el Security Store

13. ¿Qué afirmación sobre los roles de Security Copilot es correcta?
   - a) Son roles de Entra ID
   - b) Dan acceso a los datos de seguridad de cada producto
   - c) Admiten asignación a cualquier tipo de grupo
   - d) Controlan la plataforma, exigen mantener dos owners y Copilot no supera los permisos del usuario en cada plugin

14. ¿Dónde se auditan los pares prompt-respuesta de Security Copilot?
   - a) Solo en el panel de uso
   - b) En Sentinel, por defecto
   - c) En Purview DSPM for AI
   - d) No se auditan

15. Creas una política de acceso condicional de Protect AI dirigida a Security Copilot. ¿Qué cubre?
   - a) La experiencia independiente, no las experiencias embebidas
   - b) Todas las experiencias embebidas
   - c) Solo los agentes de partners
   - d) Solo las Logic Apps que usan el conector

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

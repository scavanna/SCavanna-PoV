# Nivel 3 · Avanzado · Agentes de IA, postura de IA, regulación y SOC

*Microsoft Purview DSPM y seguridad de datos para IA Ninja Training · Edición 2026*

[← Nivel 2 · Intermedio](02_Nivel_2_Intermedio.md) · [Índice del programa](README.md) · [Nivel 4 · Operación →](04_Nivel_4_Operacion.md)

<a id="avanzado"></a>

Agentes de Security Copilot y Data Security Investigations, postura de IA con Defender for Cloud, marcos de gobierno de IA en Compliance Manager e integración con Defender XDR, Sentinel y apps propias. Terminas con un piloto de agente con presupuesto de SCU, un mapa de evidencias regulatorias y un runbook del SOC.

*L400 · 4 módulos · ~21 horas · 27 recursos*

**Módulos de este nivel:** [A1 Agentes de Security Copilot](#a1) · [A2 Defender for Cloud y AI-SPM](#a2) · [A3 Gobierno de IA y regulación](#a3) · [A4 Automatización y SOC](#a4)

<a id="a1"></a>

## A1 · Agentes de Security Copilot y Data Security Investigations en Purview

*L400 · ~6 h · Origen: Ruta Ninja de Purview, módulo 3 (Security Copilot en Purview), y ruta de DSPM, módulo 4 (investigar con Security Copilot)*

Security Copilot llega a Purview de dos formas. Las **experiencias integradas** resumen alertas de DLP e Insider Risk, responden prompts en DSPM, consultan el explorador de actividad en lenguaje natural y ejecutan promptbooks. Los **agentes** trabajan en segundo plano. Microsoft 365 E5 incluye 400 unidades de cómputo de seguridad (SCU) al mes por cada 1.000 licencias, con un tope de 10.000 SCU mensuales. Quienes ya usaban Security Copilot el 18 de noviembre de 2025 tuvieron acceso inmediato; el resto se activa por fases.

El **Data Security Posture Agent** descubre datos sensibles con lenguaje natural, etiqueta hasta 10 archivos a la vez y permite programar ejecuciones. Requiere E5 con SCU aprovisionadas, admite dos prompts concurrentes y una sola instancia por inquilino, y escanea hasta 5 GB o 10.000 elementos (devuelve los 1.000 primeros). Su estado es contradictorio: un aviso del Message Center anunció la GA para junio y julio de 2026, pero Learn sigue diciendo preview. El **Data Security Triage Agent** clasifica alertas de DLP e Insider Risk para reducir el ruido; en DLP solo cubre Exchange, Teams, OneDrive, SharePoint y Endpoint.

**Data Security Investigations** (DSI) llegó a disponibilidad general en enero de 2026. Se factura solo por consumo (almacenamiento y cómputo de IA) y no requiere una licencia específica de Microsoft 365. Sus investigaciones parten de incidentes de Defender XDR, casos de Insider Risk o insights de DSPM. Los insights proactivos dentro de DSPM llegaron a GA en junio de 2026, y en mayo se sumaron OCR y exámenes personalizados. Los fundamentos de Security Copilot están en su propio programa (módulos I2, M5 y M6); los agentes de triaje se profundizan en los programas de DLP (A4) e Insider Risk (A3).

**Por qué importa**

El volumen de hallazgos de postura supera a cualquier equipo. Los agentes reducen el tiempo de descubrimiento y de triaje si se gobiernan con presupuesto de SCU, identidades de solo lectura y aprobación humana. DSI convierte un incidente de datos en una investigación asistida por IA con un costo que se puede estimar. Este módulo te ayuda a decidir qué agente pilotar primero, con qué presupuesto y cómo medir su valor.

**Qué vas a lograr**

- Explicar qué hacen el Data Security Posture Agent, el Data Security Triage Agent y DSI, y qué requiere cada uno.
- Calcular la capacidad de SCU incluida en E5 y presupuestar el consumo de los agentes.
- Desplegar un agente con identidad de agente, roles por nivel de visibilidad y fuentes acotadas.
- Estimar el costo de una investigación de DSI y activar los insights proactivos con aprobación.
- Reconocer contradicciones de estado (preview frente a GA) y verificarlas antes de comprometer un diseño.

> **Atención.** Estado del Data Security Posture Agent: MC1318248 (Roadmap 542790) anunció la GA en DSPM entre mediados de junio y fines de julio de 2026, pero la página de Learn actualizada el 23 de junio de 2026 y la vista general de agentes siguen diciendo preview ([MC1318248](https://mc.merill.net/message/MC1318248), [Posture Agent](https://learn.microsoft.com/en-us/purview/copilot-in-purview-posture-agent-get-started)). Trátalo como preview en compromisos de servicio hasta que Learn cambie.

> **Novedad.** Microsoft 365 E5 incluye Security Copilot: 400 SCU al mes por cada 1.000 licencias, hasta 10.000 SCU al mes (4.000 licencias equivalen a 1.600 SCU). Quienes ya lo usaban el 18 de noviembre de 2025 tuvieron acceso inmediato y el resto se activa por fases ([Security Copilot en E5](https://www.microsoft.com/en-us/security/security-copilot-in-microsoft-365-e5)). Las SCU se calculan sobre licencias pagas: una prueba no te da capacidad útil ([inclusión en E5 y E7](https://learn.microsoft.com/en-us/copilot/security/security-copilot-inclusion)).

> **Consejo Ninja.** Límites del Posture Agent: dos prompts concurrentes, una instancia por inquilino, escaneo de hasta 5 GB o 10.000 elementos (devuelve los 1.000 primeros) y etiquetado de hasta 10 archivos a la vez; se recomienda desplegarlo con una identidad de agente. El agente de triaje de DLP solo clasifica alertas de Exchange, Teams, OneDrive, SharePoint y Endpoint, y combina licencia por usuario con consumo de SCU ([Triage Agent](https://learn.microsoft.com/en-us/purview/copilot-in-purview-triage-dlp-agent-get-started)).

> **Atención.** DSI se factura solo por consumo (almacenamiento por GB al mes y cómputo de IA), incluidas las investigaciones proactivas creadas desde DSPM ([facturación de DSI](https://learn.microsoft.com/en-us/purview/data-security-investigations-billing)). Los insights proactivos del objetivo de exfiltración llegaron a GA de inicios a mediados de junio de 2026 y requieren DSI y DSPM configurados ([MC1317196](https://mc.merill.net/message/MC1317196)). Una fuente de terceros afirma que unidades de cómputo propias de DSI reemplazaron a las SCU: confírmalo antes de presupuestar ([4sysops](https://4sysops.com/archives/microsoft-purview-data-security-investigations-ai-powered-threat-detection-for-microsoft-365/)).

**¿Tienes poco tiempo?**

- [Security Copilot agents in Microsoft Purview overview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-agents-overview) · Documentación
- [Get started with the Microsoft Purview Data Security Posture Agent](https://learn.microsoft.com/en-us/purview/copilot-in-purview-posture-agent-get-started) · Documentación
- [Security Copilot agents in Microsoft 365 E5](https://www.microsoft.com/en-us/security/security-copilot-in-microsoft-365-e5) · Documentación
- [Security Copilot Agents, DSPM AI Observability, and IRM for Agents (webinar)](https://www.youtube.com/watch?v=_JSHcsm9rYI) · Webinar

**Agentes de Security Copilot y Data Security Investigations en Purview**

| Herramienta | Qué hace | Requisitos | Costo | Estado al 6 de noviembre de 2026 | Fuente |
|---|---|---|---|---|---|
| Security Copilot integrado en Purview | Resume alertas de DLP e Insider Risk, responde prompts en DSPM, consulta el explorador de actividad en lenguaje natural y ejecuta promptbooks | Security Copilot en el mismo inquilino; Data Security Viewer para DSPM | SCU (incluidas en E5 según licencias pagas) | Vigente | [Security Copilot en Purview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-overview) |
| Data Security Posture Agent (DSPM) | Descubre datos sensibles con lenguaje natural, etiqueta hasta 10 archivos a la vez y programa ejecuciones | E5 con SCU aprovisionadas, incorporación a Security Copilot, plugin de Purview e identidad de agente recomendada; una instancia por inquilino y dos prompts concurrentes | SCU | GA anunciada para junio y julio de 2026 (MC1318248); Learn todavía dice preview | [Posture Agent](https://learn.microsoft.com/en-us/purview/copilot-in-purview-posture-agent-get-started) |
| Posture Agent en Data Security Investigations | Busca credenciales expuestas en SharePoint, OneDrive, Exchange y Teams, con tablero Kanban, puntuaciones de riesgo y consultas KQL | SCU; no requiere configurar la facturación de DSI | SCU | Preview | [Posture Agent en DSI](https://learn.microsoft.com/en-us/purview/data-security-investigations-posture-agent) |
| Data Security Triage Agent | Clasifica alertas de DLP e Insider Risk y reduce el ruido | Licencia por usuario; en DLP solo Exchange, Teams, OneDrive, SharePoint y Endpoint; identidad de agente recomendada | SCU | Vigente (fecha no verificada) | [Triage Agent](https://learn.microsoft.com/en-us/purview/copilot-in-purview-triage-dlp-agent-get-started) |
| Data Security Investigations | Investiga con IA desde incidentes de Defender XDR, casos de Insider Risk o insights de DSPM; OCR, exámenes personalizados y purga | Configurar la facturación y los permisos antes de activar los insights proactivos | Consumo: almacenamiento por GB al mes y cómputo de IA | GA en enero de 2026; insights proactivos en GA en junio de 2026 | [Facturación de DSI](https://learn.microsoft.com/en-us/purview/data-security-investigations-billing) · [Primeros pasos](https://learn.microsoft.com/en-us/purview/data-security-investigations-get-started) |

Capacidad incluida en Microsoft 365 E5: 400 SCU al mes por cada 1.000 licencias pagas, hasta 10.000 ([Security Copilot en E5](https://www.microsoft.com/en-us/security/security-copilot-in-microsoft-365-e5)). Vista general de los agentes: [agentes de Security Copilot en Purview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-agents-overview).

### Documentación, cursos y credenciales

- [Security Copilot agents in Microsoft Purview overview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-agents-overview) · Documentación · Oficial · Microsoft Learn. Describe los agentes de Security Copilot en Purview: Data Security Triage Agent (DLP e IRM), Data Security Posture Agent de DSPM y el Posture Agent de Data Security Investigations, que consumen SCU.
- [Get started with the Microsoft Purview Triage Agent in Data Loss Prevention](https://learn.microsoft.com/en-us/purview/copilot-in-purview-triage-dlp-agent-get-started) · Documentación · Oficial · Microsoft Learn. Guía de despliegue del agente de triaje de DLP en los portales de Purview y Defender XDR, con licenciamiento por usuario más consumo de SCU, roles requeridos e identidad de agente de Entra recomendada.
- [Billing in Data Security Investigations](https://learn.microsoft.com/en-us/purview/data-security-investigations-billing) · Documentación · Oficial · Microsoft Learn. Explica que Data Security Investigations se factura solo por consumo (almacenamiento por GB/mes y unidades de cómputo de IA), incluidas las investigaciones proactivas creadas desde DSPM.
- [Microsoft Security Copilot Security Compute Units and capacity](https://learn.microsoft.com/en-us/copilot/security/security-compute-units-capacity) · Documentación · Oficial · Microsoft Learn. Explica las SCU, la capacidad aprovisionada y de excedente y la capacidad predeterminada autoaprovisionada para clientes Microsoft 365 E5 y E7.
- [Security Copilot agents in Microsoft 365 E5](https://www.microsoft.com/en-us/security/security-copilot-in-microsoft-365-e5) · Documentación · Oficial · Microsoft Security · 18 nov 2025. Página oficial del beneficio: 400 SCU al mes por cada 1.000 licencias E5, hasta 10.000 SCU/mes, con activación por fases desde el 18-nov-2025 e incluye agentes de Purview.
- [Get started with the Microsoft Purview Data Security Posture Agent](https://learn.microsoft.com/en-us/purview/copilot-in-purview-posture-agent-get-started) · Documentación · Oficial · Vista previa · Nuevo · Microsoft Learn · 23 jun 2026. Guía para habilitar el Posture Agent en DSPM y DSI: requiere Microsoft 365 E5 con SCU, incorporación a Security Copilot, plugin de Purview, identidad de agente recomendada y roles por nivel de visibilidad de contenido. *Nota:* Página actualizada el 23-jun-2026 y aún marcada como preview pese a MC1318248 (GA jun-jul 2026). Requiere E5 con SCU aprovisionadas; dos prompts concurrentes; una instancia por inquilino; escanea máx. 5 GB o 10.000 elementos y devuelve los 1.000 primeros…
- [Security Copilot in Microsoft Purview overview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-overview) · Documentación · Oficial · Microsoft Learn. Resume las experiencias integradas y autónomas de Security Copilot en Purview: resúmenes de alertas DLP/IRM, prompts en DSPM, explorador de actividad con lenguaje natural y promptbooks.
- [Get started with Data Security Investigations](https://learn.microsoft.com/en-us/purview/data-security-investigations-get-started) · Documentación · Oficial · Microsoft Learn. Flujo de ocho pasos para configurar permisos, facturación, crear investigaciones desde incidentes de Defender XDR, casos de IRM o insights de DSPM, y aplicar mitigaciones.
- [Get started with the Data Security Posture agent (preview) in Data Security Investigations](https://learn.microsoft.com/en-us/purview/data-security-investigations-posture-agent) · Documentación · Oficial · Vista previa · Microsoft Learn. Describe el uso del Posture Agent en DSI para escanear credenciales expuestas en SharePoint, OneDrive, Exchange y Teams con tablero Kanban, puntajes de riesgo y consultas KQL. *Nota:* No requiere configurar la facturación de DSI, solo SCU

### Webinars, videos y podcasts

- [Security Copilot Agents, DSPM AI Observability, and IRM for Agents (webinar)](https://www.youtube.com/watch?v=_JSHcsm9rYI) · Webinar · Oficial · Nuevo · Microsoft Security Community · Microsoft Security Community (YouTube) · may 2026. Webinar sobre observabilidad de IA en DSPM, IRM para agentes de Copilot Studio y Foundry, y despliegue del IRM Triage Agent y del DSPM Posture Agent.

### Laboratorios, GitHub y herramientas

- [MC1318248 – Data Security Posture Management: New data security agent in DSPM (archivo Message Center)](https://mc.merill.net/message/MC1318248) · Herramienta · Comunidad · Nuevo · Microsoft (archivado por Merill Fernando) · Microsoft 365 Message Center Archive (merill.net) · 21 may 2026. Mensaje del Centro de mensajes que confirma la GA mundial de DSPM y del Data Security Posture Agent entre mediados de junio y finales de julio de 2026 (Roadmap 542790).

**Manos a la obra**

1. `Laboratorio parcial` Posture Agent en una sesión corta: en una suscripción separada crea una capacidad de 1 SCU con excedente 0, incorpora Security Copilot ([incorporación manual](https://learn.microsoft.com/en-us/copilot/security/manual-onboarding)), habilita el agente con una identidad de agente y pídele que descubra datos sensibles en un sitio de prueba; borra la capacidad al terminar ([Posture Agent](https://learn.microsoft.com/en-us/purview/copilot-in-purview-posture-agent-get-started)). Limitación: la inclusión de E5 no aplica a una prueba y cada SCU se cobra por hora. Evidencia: resultado del agente y consumo de SCU.
2. `Laboratorio parcial` Security Copilot en DSPM: con el rol Data Security Viewer, usa los prompts de DSPM para resumir el objetivo de sobreexposición y compara la respuesta con tu lectura manual ([Security Copilot en Purview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-overview)). Limitación: consume SCU y los datos del laboratorio son pocos. Evidencia: comparación en una página.
3. `Laboratorio` Presupuesto de SCU: calcula la capacidad incluida para tu organización (400 SCU por cada 1.000 licencias E5 pagas, con tope de 10.000) y repártela entre el Posture Agent, el Triage Agent y el uso integrado, con umbrales de alerta ([capacidad y SCU](https://learn.microsoft.com/en-us/copilot/security/security-compute-units-capacity)). Evidencia: hoja de presupuesto aprobada.
4. `Laboratorio` Costo de una investigación de DSI: con la página de facturación estima el costo de una investigación acotada (GB de almacenamiento y cómputo de IA) y redacta los criterios para activar los insights proactivos ([facturación de DSI](https://learn.microsoft.com/en-us/purview/data-security-investigations-billing)). Evidencia: estimación y criterios aprobados por el dueño del presupuesto.
5. `Solo producción` Data Security Triage Agent: despliégalo con identidad de agente y roles de solo lectura que no vean contenido, acotado a las alertas de una política DLP piloto; vigila las SCU en la pestaña de rendimiento y desactívalo si el consumo se dispara ([Triage Agent](https://learn.microsoft.com/en-us/purview/copilot-in-purview-triage-dlp-agent-get-started)). Cómo hacerlo seguro: alcance piloto, aprobación manual de cada recomendación y revisión semanal. Evidencia: alertas triadas y consumo.
6. `Solo producción` Investigación proactiva con DSI: estima el costo, limita el alcance a un incidente, asigna los roles de revisión y deja la purga como segundo paso con aprobación ([primeros pasos con DSI](https://learn.microsoft.com/en-us/purview/data-security-investigations-get-started)). Cómo hacerlo seguro: presupuesto con alertas y revisión a los 7 días; recuerda que detener la facturación elimina todas las investigaciones. Evidencia: informe de la investigación y costo real.

**¿Quieres profundizar?**

- [MC1318248 – Data Security Posture Management: New data security agent in DSPM (archivo Message Center)](https://mc.merill.net/message/MC1318248) · Herramienta

<a id="a2"></a>

## A2 · Integración con Defender for Cloud y la postura de seguridad de la IA

*L400 · ~5 h · Origen: Nuevo en esta edición*

Purview protege los **datos** de las interacciones; Defender for Cloud protege las **cargas de trabajo** de IA. La gestión de la postura de seguridad de la IA (AI-SPM), incluida en el plan Defender CSPM, genera la lista de materiales de IA (AI BOM), recomendaciones y rutas de ataque, y señala los endpoints expuestos. Cubre Azure OpenAI, Microsoft Foundry, Azure Machine Learning, Amazon Bedrock y Google Vertex AI. Desde el 1 de julio de 2026, el descubrimiento y la postura de agentes de Foundry y de nubes de terceros requieren licencia de **Agent 365**; Defender CSPM sigue descubriendo cuentas y proyectos de Foundry.

La **protección contra amenazas de IA** (Defender for AI Services) usa Prompt Shields para alertar sobre fuga de datos, jailbreak o robo de credenciales, y envía las alertas a Defender XDR. En la capa de red, el AI Gateway de Entra Internet Access agrega protección contra inyección de prompts. Para la dirección, el **Security Dashboard for AI** reúne señales de Entra, Defender y Purview: inventario de IA (Copilot, agentes, Foundry, Gemini, ChatGPT y servidores MCP), riesgos y recomendaciones asignables.

La postura de IA completa combina cuatro piezas: DSPM para los datos, AI-SPM para las cargas, Entra para las identidades de usuarios y agentes, y Defender XDR para las amenazas. Este módulo las conecta; la identidad de los agentes se profundiza en el programa de Entra y la seguridad de la IA en el de Security Copilot (módulo X3).

**Por qué importa**

El riesgo de la IA no se agota en los datos: un endpoint expuesto, un modelo sin filtro de contenido o un agente con permisos excesivos también exponen información. El CISO necesita una sola foto con responsables claros, sin herramientas duplicadas. También necesita entender el cambio de licencias de julio de 2026, que mueve a Agent 365 la postura de agentes.

**Qué vas a lograr**

- Explicar AI-SPM: AI BOM, recomendaciones, rutas de ataque y endpoints expuestos.
- Identificar qué requiere Defender CSPM y qué requiere Agent 365 desde el 1 de julio de 2026.
- Habilitar Defender for AI Services y revisar alertas de Prompt Shields en Defender XDR.
- Usar el Security Dashboard for AI para el reporte ejecutivo del riesgo de IA.
- Conectar los hallazgos de AI-SPM con DSPM a través de la integración de Purview con Foundry.

> **Qué cambió.** Desde el 1 de julio de 2026, el descubrimiento y la postura de agentes de Microsoft Foundry y de agentes en nubes de terceros requieren licencia de Agent 365; Defender CSPM sigue descubriendo cuentas y proyectos de Foundry ([AI-SPM](https://learn.microsoft.com/en-us/azure/defender-for-cloud/ai-security-posture)). La versión en español es traducción automática: valídala contra la versión en inglés ([AI-SPM en español](https://learn.microsoft.com/es-es/azure/defender-for-cloud/ai-security-posture)).

> **Novedad.** Defender for AI Services usa Prompt Shields para alertar sobre fuga de datos, jailbreak o robo de credenciales y envía las alertas a Defender XDR. La prueba de 30 días está limitada a 75.000 millones de tokens y solo analiza texto ([protección contra amenazas de IA](https://learn.microsoft.com/en-us/azure/defender-for-cloud/ai-threat-protection)).

> **Consejo Ninja.** Para el comité ejecutivo, el [Security Dashboard for AI](https://learn.microsoft.com/en-us/security/security-for-ai/security-dashboard-for-ai) reúne señales de Entra, Defender y Purview sobre el inventario de IA (Copilot, agentes, Foundry, Gemini, ChatGPT y servidores MCP), sus riesgos y recomendaciones asignables; el rol mínimo es Security Reader.

> **Atención.** La protección contra inyección de prompts del AI Gateway de Entra Internet Access requiere esa licencia y admite solo texto, hasta 64.000 caracteres por prompt (página del 1 de septiembre de 2026) ([AI Gateway](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-ai-prompt-injection-protection)).

**¿Tienes poco tiempo?**

- [Overview - AI security posture management (Microsoft Defender for Cloud)](https://learn.microsoft.com/en-us/azure/defender-for-cloud/ai-security-posture) · Documentación
- [AI threat protection in Microsoft Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/ai-threat-protection) · Documentación
- [Assess your organization's AI risk with Microsoft Security Dashboard for AI](https://learn.microsoft.com/en-us/security/security-for-ai/security-dashboard-for-ai) · Documentación

### Documentación, cursos y credenciales

- [Overview - AI security posture management (Microsoft Defender for Cloud)](https://learn.microsoft.com/en-us/azure/defender-for-cloud/ai-security-posture) · Documentación · Oficial · Nuevo · Microsoft Learn · 17 jun 2026. Explica AI-SPM en el plan Defender CSPM: AI BOM, recomendaciones, rutas de ataque y endpoints expuestos para Azure OpenAI, Foundry, Azure ML, Bedrock y Vertex AI.
- [Protect enterprise generative AI apps with prompt injection protection (Global Secure Access)](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-ai-prompt-injection-protection) · Documentación · Oficial · Nuevo · Microsoft Learn · 1 sep 2026. Configura la protección contra inyección de prompts del AI Gateway de Entra Internet Access con políticas de prompts, perfiles de seguridad y acceso condicional para apps de IA basadas en JSON.
- [AI threat protection in Microsoft Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/ai-threat-protection) · Documentación · Oficial · Nuevo · Microsoft Learn · 17 jun 2026. Describe la protección contra amenazas de IA (Defender for AI Services) que usa Prompt Shields para alertar sobre fuga de datos, jailbreak o robo de credenciales e integra las alertas en Defender XDR.

**Manos a la obra**

1. `Laboratorio parcial` AI-SPM: habilita Defender CSPM en la suscripción del laboratorio con un proyecto de Foundry y revisa el AI BOM, las recomendaciones y, si aparecen, las rutas de ataque ([AI-SPM](https://learn.microsoft.com/en-us/azure/defender-for-cloud/ai-security-posture)). Limitación: Defender CSPM tiene costo y la postura de agentes requiere Agent 365; desactiva el plan al terminar. Evidencia: AI BOM exportado y una recomendación analizada.
2. `Laboratorio parcial` Defender for AI Services: habilita la protección en el recurso de Foundry (prueba de 30 días), envía un prompt de jailbreak de prueba documentado y verifica la alerta en Defender XDR ([protección contra amenazas de IA](https://learn.microsoft.com/en-us/azure/defender-for-cloud/ai-threat-protection)). Limitación: la prueba se limita a 75.000 millones de tokens y solo analiza texto. Evidencia: alerta con su evidencia.
3. `Laboratorio parcial` Security Dashboard for AI: con el rol Security Reader revisa el inventario y asigna una recomendación a un responsable ([Security Dashboard for AI](https://learn.microsoft.com/en-us/security/security-for-ai/security-dashboard-for-ai)). Limitación: en un inquilino de prueba el inventario es pequeño. Evidencia: recomendación asignada.
4. `Laboratorio` Mapa de responsabilidades de la postura de IA: arma una tabla que asigne datos (Purview DSPM), cargas de trabajo (Defender for Cloud), identidades de usuarios y agentes (Entra) y amenazas (Defender XDR) a equipos, con la licencia que requiere cada capacidad. Evidencia: mapa validado por el CISO.
5. `Solo producción` Postura de agentes de Foundry con Agent 365: revisa en producción los agentes descubiertos y su postura y, para el de mayor riesgo, define acciones con su dueño. Cómo hacerlo seguro: solo lectura, cambios en una ventana aprobada y registro del riesgo aceptado. Evidencia: plan de acción.

<a id="a3"></a>

## A3 · Marcos de gobierno de IA y regulación

*L400 · ~4 h · Origen: Nuevo en esta edición (se apoya en el pilar de IA del taller Zero Trust de Microsoft)*

Los marcos de gobierno de IA, como la **Ley de IA de la UE (EU AI Act)**, **ISO/IEC 42001**, **ISO/IEC 23894** y el **NIST AI RMF**, se traducen en controles verificables. Compliance Manager ofrece plantillas premium para todos ellos, y Microsoft 365 E5 permite usar tres plantillas premium sin costo. También hay evaluaciones automáticas para apps y agentes de IA y una evaluación base para Microsoft 365 Copilot. Desde DSPM, la recomendación «Get guided assistance to AI regulations» crea evaluaciones con esas plantillas para todas las apps de IA.

El pilar de IA del **taller Zero Trust** de Microsoft propone dos tareas concretas. La primera crea evaluaciones de EU AI Act, NIST AI RMF e ISO/IEC 42001 y suma informes de despliegue de Foundry como evidencia. La segunda despliega las políticas Risky AI usage y Risky Agents con bajo esfuerzo. La idea central es una **cadena de evidencia**. AI observability aporta el inventario, Audit los registros y la aprobación de acciones de agentes la supervisión humana. Las evaluaciones de riesgo de datos y la DLP para Copilot aportan los controles preventivos.

En MCSA ya hay normas específicas, como el reglamento peruano de la Ley 31814 y la circular de la SIC de Colombia sobre datos personales en IA. Se tratan en [O3](04_Nivel_4_Operacion.md#o3). Este módulo no interpreta normas: construye la evidencia técnica que Legal y privacidad evalúan. El detalle de Compliance Manager está en su propio programa (módulo M3).

**Por qué importa**

Reguladores, auditores y directorios ya preguntan cómo se gobierna la IA. Una respuesta defendible necesita un marco de referencia, controles mapeados a ese marco y evidencia producida por las herramientas, no por planillas. Este módulo arma esa cadena de evidencia y evita reinventar plantillas que Microsoft ya mantiene.

**Qué vas a lograr**

- Elegir un marco de referencia de IA (EU AI Act, ISO/IEC 42001 o NIST AI RMF) según el contexto de tu organización.
- Crear una evaluación de IA en Compliance Manager y asignar acciones de mejora.
- Vincular evidencias de DSPM, Audit e Insider Risk a los controles del marco.
- Usar la evaluación base de Microsoft 365 Copilot y las evaluaciones automáticas de apps y agentes.
- Identificar qué decisiones corresponden a Legal y privacidad.

> **Novedad.** Compliance Manager ofrece plantillas premium de IA (EU AI Act, ISO/IEC 42001, ISO/IEC 23894 y NIST AI RMF), y Microsoft 365 E5 permite usar tres plantillas premium sin costo ([lista de regulaciones](https://learn.microsoft.com/en-us/purview/compliance-manager-regulations-list)). Hay evaluaciones automáticas para apps y agentes de IA y una evaluación base para Microsoft 365 Copilot ([evaluaciones](https://learn.microsoft.com/en-us/purview/compliance-manager-assessments)).

> **Consejo Ninja.** La recomendación de DSPM «Get guided assistance to AI regulations» crea evaluaciones con plantillas de Compliance Manager para todas las apps de IA ([otras apps de IA](https://learn.microsoft.com/en-us/purview/ai-other-apps)). El taller Zero Trust propone complementarlas con informes de despliegue de Foundry como evidencia ([documentación de cumplimiento de IA](https://microsoft.github.io/zerotrustassessment/docs/workshop-guidance/AI/AI_107)).

> **Atención.** Una evaluación con buena puntuación no equivale a cumplimiento legal: es evidencia técnica que Legal y privacidad deben valorar. Un blog de un ISV (24 de agosto de 2026) muestra cómo configurar una evaluación de EU AI Act y también los límites de la herramienta ([guía práctica](https://rencore.com/en/blog/managing-monitoring-eu-ai-act-compliance-manager/)).

**¿Tienes poco tiempo?**

- [Microsoft Purview Compliance Manager regulations list](https://learn.microsoft.com/en-us/purview/compliance-manager-regulations-list) · Documentación
- [Build and manage assessments in Microsoft Purview Compliance Manager (AI assessments)](https://learn.microsoft.com/en-us/purview/compliance-manager-assessments) · Documentación
- [Establish AI Compliance Documentation (Zero Trust Workshop – AI)](https://microsoft.github.io/zerotrustassessment/docs/workshop-guidance/AI/AI_107) · Laboratorio

### Documentación, cursos y credenciales

- [Build and manage assessments in Microsoft Purview Compliance Manager (AI assessments)](https://learn.microsoft.com/en-us/purview/compliance-manager-assessments) · Documentación · Oficial · Microsoft Learn. Describe las evaluaciones para regulaciones de IA, las evaluaciones automáticas para apps y agentes de IA y la evaluación base para Microsoft 365 Copilot y Copilot Chat.

### Laboratorios, GitHub y herramientas

- [Establish AI Compliance Documentation (Zero Trust Workshop – AI)](https://microsoft.github.io/zerotrustassessment/docs/workshop-guidance/AI/AI_107) · Laboratorio · Oficial · Microsoft Zero Trust Workshop (GitHub Pages). Tarea del taller Zero Trust para crear evaluaciones de EU AI Act, NIST AI RMF e ISO/IEC 42001 en Compliance Manager y complementarlas con informes de despliegue de Foundry como evidencia.

### Comunidad: blogs, libros, newsletters y eventos

- [Managing and monitoring your EU AI Act compliance with Compliance Manager](https://rencore.com/en/blog/managing-monitoring-eu-ai-act-compliance-manager/) · Blog · Comunidad · Nuevo · Jasper Oosterveld · Rencore · 24 ago 2026. Guía práctica para configurar una evaluación de EU AI Act en Compliance Manager, con agrupación, acciones de mejora, roles y límites de la herramienta.

**Manos a la obra**

1. `Laboratorio parcial` Evaluación regulatoria de IA: crea en Compliance Manager una evaluación de EU AI Act o de ISO/IEC 42001, asigna acciones de mejora y enlaza informes de DSPM como evidencia ([evaluaciones](https://learn.microsoft.com/en-us/purview/compliance-manager-assessments), [taller Zero Trust](https://microsoft.github.io/zerotrustassessment/docs/workshop-guidance/AI/AI_107)). Limitación: consume uno de los tres cupos premium de E5 y en la prueba no hay evidencia real. Evidencia: evaluación con acciones asignadas.
2. `Laboratorio` Mapa de evidencias: elige 10 controles del marco y asigna a cada uno una evidencia de Purview: inventario (AI observability), registros (Audit), supervisión humana (aprobación de acciones de agentes), evaluaciones de riesgo de datos y DLP para Copilot. Evidencia: tabla control–evidencia–responsable.
3. `Laboratorio parcial` Recomendación de DSPM para regulaciones de IA: activa «Get guided assistance to AI regulations» y revisa las evaluaciones que crea ([otras apps de IA](https://learn.microsoft.com/en-us/purview/ai-other-apps)). Limitación: sin uso real de IA muchas acciones quedan sin evidencia. Evidencia: evaluaciones creadas.
4. `Solo producción` Taller con Legal y privacidad: presenta el mapa de evidencias y la clasificación de riesgo de los usos de IA según la norma aplicable (por ejemplo, el reglamento peruano) y acuerda responsables. Cómo hacerlo seguro: Legal decide la interpretación, no se comparten datos personales y se levanta un acta. Evidencia: acta con decisiones.

<a id="a4"></a>

## A4 · Automatización, reportes e integración con el SOC

*L400 · ~6 h · Origen: Ruta SC-200 «Mitigate threats using Microsoft Purview» y guías para desarrolladores de Purview*

Las alertas de DLP se investigan en la **cola unificada de incidentes de Defender XDR**, con resumen de Security Copilot y búsqueda avanzada. Desde inicios de octubre de 2026, una regla de ajuste integrada convierte señales de DLP en comportamientos (BehaviorInfo): si el SOC deja de ver alertas, ese es el primer lugar que hay que revisar. En **Microsoft Sentinel**, el conector de Defender XDR y la tabla CloudAppEvents permiten correlacionar incidentes de DLP con la actividad del usuario mediante KQL. Las alertas de **Insider Risk** se exportan a un SIEM o SOAR por la Office 365 Management Activity API o por el conector de Sentinel, pero la exportación por API no conserva la seudonimización.

Para las apps propias, las **APIs de Purview en Microsoft Graph** (protectionScopes, processContent, contentActivities y sensitivityLabels) permiten aplicar DLP, Insider Risk, etiquetas y auditoría. Las políticas DLP para apps registradas en Entra se crean con PowerShell (New-DlpComplianceRule), y configurar el inquilino requiere E5 y la auditoría activa. El middleware de Purview para **Microsoft Agent Framework** bloquea contenido sensible en línea y registra las interacciones. La integración nativa de Foundry no cubre DLP ni sobreexposición; las APIs sí.

El repositorio «Data and Agent Governance and Security Accelerator» se archivó el 28 de septiembre de 2026: sirve como referencia, pero ya no recibe mantenimiento. La integración con el SOC se profundiza en los programas de DLP (A2), Insider Risk (A2), Defender XDR y Sentinel.

**Por qué importa**

Seguridad de datos sin integración con el SOC produce alertas que nadie atiende. Este módulo lleva las señales de DLP, Insider Risk e IA a Defender XDR y Sentinel, y extiende las políticas a tus propias apps de IA. Así se cierra la brecha entre postura y respuesta, con métricas como el tiempo de triaje de incidentes de datos y la cobertura de las apps de IA propias.

**Qué vas a lograr**

- Investigar alertas de DLP en Defender XDR y explicar la regla de ajuste de octubre de 2026.
- Llevar incidentes de DLP e Insider Risk a Sentinel y correlacionarlos con KQL.
- Integrar una app propia con protectionScopes y processContent.
- Crear políticas DLP para apps registradas en Entra con PowerShell.
- Elegir entre la integración nativa de Foundry, Agent Framework y las APIs de Purview según el escenario.

> **Atención.** Desde inicios de octubre de 2026, una regla de ajuste integrada de Defender XDR convierte señales de DLP en comportamientos (BehaviorInfo) en lugar de alertas. Si el SOC deja de ver alertas de DLP, revisa esa regla ([alertas de DLP en Defender XDR](https://learn.microsoft.com/en-us/defender-xdr/dlp-investigate-alerts-defender)).

> **Consejo Ninja.** Elige la integración por escenario: la integración nativa de Foundry no cubre DLP ni sobreexposición, Agent Framework agrega middleware de Purview y las APIs de Graph (protectionScopes y processContent) cubren la DLP en línea ([apps de IA seguras con Purview](https://learn.microsoft.com/en-us/purview/developer/secure-ai-with-purview)). Configurar el inquilino para las APIs requiere licencias E5 y la auditoría activa, según la página actualizada el 5 de mayo de 2026 ([configurar el inquilino](https://learn.microsoft.com/en-us/purview/developer/configuretenant)).

> **Qué cambió.** El repositorio «Data and Agent Governance and Security Accelerator» (PowerShell y azd para incorporar DSPM para IA, DLP, etiquetas, auditoría y Defender for AI) se archivó el 28 de septiembre de 2026: úsalo solo como referencia ([GitHub](https://github.com/microsoft/Data-and-Agent-Governance-and-Security-Accelerator)).

> **Atención.** Al exportar alertas de Insider Risk por la Office 365 Management Activity API se pierde la seudonimización ([compartir datos de Insider Risk](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-share-data)). Acuerda con privacidad quién puede ver esos datos en el SIEM.

**¿Tienes poco tiempo?**

- [Investigate data loss prevention alerts with Microsoft Defender XDR](https://learn.microsoft.com/en-us/defender-xdr/dlp-investigate-alerts-defender) · Documentación
- [Use Microsoft Purview APIs to leverage your policies in your apps (tutorial)](https://learn.microsoft.com/en-us/purview/developer/use-the-api) · Laboratorio
- [Mitigate threats using Microsoft Purview (SC-200 learning path)](https://learn.microsoft.com/en-us/training/paths/sc-200-mitigate-threats-using-microsoft-purview/) · Curso

### Documentación, cursos y credenciales

- [Develop and deploy secure and compliant Microsoft Foundry or custom AI apps (Purview SDK)](https://learn.microsoft.com/en-us/purview/developer/secure-ai-with-purview) · Documentación · Oficial · Microsoft Learn. Compara las opciones de integración (nativa en Foundry, Agent Framework y APIs de Purview en Graph: protection scopes y processContent) según escenario de gobierno, DLP o sobreexposición.
- [Overview of Microsoft Purview APIs (Microsoft Graph)](https://learn.microsoft.com/en-us/purview/developer/microsoft-purview-sdk-documentation-overview) · Documentación · Oficial · Microsoft Learn. Resume las APIs de Purview en Graph (protectionScopes, processContent, contentActivities y sensitivityLabels) para que apps de IA y de negocio apliquen DLP, IRM, etiquetas y auditoría.
- [Investigate data loss prevention alerts with Microsoft Defender XDR](https://learn.microsoft.com/en-us/defender-xdr/dlp-investigate-alerts-defender) · Documentación · Oficial · Microsoft Learn. Explica la investigación de alertas DLP en la cola unificada de incidentes de Defender XDR, con licencias, roles mínimos, resumen con Security Copilot y búsqueda avanzada.
- [Mitigate threats using Microsoft Purview (SC-200 learning path)](https://learn.microsoft.com/en-us/training/paths/sc-200-mitigate-threats-using-microsoft-purview/) · Curso · Oficial · Microsoft Learn. Ruta SC-200 de 4 módulos para el SOC: investigar alertas DLP e IRM (incluidos agentes de IA), auditar actividades de Copilot y apps de IA y buscar con eDiscovery.
- [Investigate data loss prevention alerts with Microsoft Sentinel](https://learn.microsoft.com/en-us/defender-xdr/dlp-investigate-alerts-sentinel) · Documentación · Oficial · Nuevo · Microsoft Learn · 11 ago 2026. Muestra cómo importar incidentes DLP a Sentinel con el conector de Defender XDR y CloudAppEvents y correlacionar alertas con actividad de usuarios mediante KQL.
- [Configure Data Security Posture Management (DSPM) for AI for custom AI apps (Purview SDK)](https://learn.microsoft.com/en-us/purview/developer/configurepurview) · Documentación · Oficial · Microsoft Learn. Guía para desarrolladores que habilita auditoría, la política KYD Secure interactions from enterprise apps, Communication Compliance e IRM para que las apps de IA personalizadas reporten prompts y respuestas a Purview.
- [Microsoft Purview middleware – Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/integrations/by-component/middleware/purview) · Documentación · Oficial · Microsoft Learn. Muestra cómo añadir el middleware de directivas de Purview a agentes de Agent Framework (C#, Python) para bloquear contenido sensible en línea con DLP y registrar interacciones para auditoría y cumplimiento.
- [Get started with data loss prevention alerts](https://learn.microsoft.com/en-us/purview/dlp-alerts-get-started) · Documentación · Oficial · Microsoft Learn. Tipos de alertas DLP (evento único y agregadas), licencias por SKU, roles y recomendación de investigar en Defender XDR y crear políticas en Purview.
- [Share Insider Risk Management data with other solutions](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-share-data) · Documentación · Oficial · Microsoft Learn. Explica cómo exportar alertas de IRM a SIEM/SOAR vía Office 365 Management Activity API, el conector de Sentinel y compartir niveles de severidad con Defender XDR y DLP.

### Laboratorios, GitHub y herramientas

- [Use Microsoft Purview APIs to leverage your policies in your apps (tutorial)](https://learn.microsoft.com/en-us/purview/developer/use-the-api) · Laboratorio · Oficial · Microsoft Learn. Tutorial paso a paso para calcular protection scopes y enviar contenido a processContent desde una app de IA, con permisos de Graph y pruebas de bloqueo.

**Manos a la obra**

1. `Laboratorio` Alertas de DLP en Defender XDR: genera una alerta DLP con una cuenta de prueba, investígala en la cola unificada y revisa la regla de ajuste integrada de octubre de 2026 ([alertas de DLP en Defender XDR](https://learn.microsoft.com/en-us/defender-xdr/dlp-investigate-alerts-defender)). Evidencia: incidente investigado y estado de la regla.
2. `Laboratorio` Sentinel: con el conector de Defender XDR importa los incidentes de DLP y escribe una consulta KQL que correlacione la alerta con CloudAppEvents del mismo usuario ([DLP con Sentinel](https://learn.microsoft.com/en-us/defender-xdr/dlp-investigate-alerts-sentinel)). Evidencia: consulta guardada y su resultado.
3. `Laboratorio parcial` APIs de Purview: sigue el tutorial de protectionScopes y processContent con una app registrada en Entra y crea la política DLP con New-DlpComplianceRule ([tutorial](https://learn.microsoft.com/en-us/purview/developer/use-the-api), [configurar el inquilino](https://learn.microsoft.com/en-us/purview/developer/configuretenant)). Limitación: requiere E5 y pago por uso; usa un inquilino del Microsoft 365 Developer Program o una app piloto. Evidencia: respuesta de la API con la acción de bloqueo.
4. `Laboratorio parcial` Agent Framework: agrega el middleware de Purview a un agente de ejemplo en Python o C# y verifica que bloquea un prompt con un SIT de prueba ([middleware de Purview](https://learn.microsoft.com/en-us/agent-framework/integrations/by-component/middleware/purview)). Limitación: requiere E5 y pago por uso. Evidencia: registro del bloqueo y de la interacción auditada.
5. `Laboratorio` Insider Risk hacia el SIEM: diseña el flujo de exportación de alertas de Insider Risk a Sentinel e indica qué campos pierden la seudonimización y quién puede verlos ([compartir datos de Insider Risk](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-share-data)). Evidencia: diagrama aprobado por privacidad.
6. `Solo producción` Runbook de incidente de datos con IA: define con el SOC el flujo para prompts con datos sensibles bloqueados de forma repetida (DLP, Insider Risk y, si corresponde, DSI) y pruébalo con cuentas de prueba en producción ([ruta SC-200 de Purview](https://learn.microsoft.com/en-us/training/paths/sc-200-mitigate-threats-using-microsoft-purview/)). Cómo hacerlo seguro: cuentas de prueba, sin datos reales y con aprobación de privacidad. Evidencia: runbook versionado y ejercicio documentado.

<a id="reto-avanzado"></a>

## Reto del nivel

**Del hallazgo al incidente, con IA y costo controlado.** En una sesión corta con 1 SCU usa el Posture Agent para encontrar datos sensibles en un sitio de prueba; genera una alerta DLP, investígala en Defender XDR y correlaciónala en Sentinel con KQL; protege una app de prueba con processContent; y mapea las evidencias a EU AI Act o ISO/IEC 42001 en Compliance Manager. Entrega el runbook del SOC y una estimación trimestral de costos de SCU, pago por uso y DSI.

<a id="quiz-avanzado"></a>

## Evaluación del nivel

Responde y compara con [Evaluaciones y respuestas](06_Evaluaciones_y_respuestas.md#eval-avanzado). Con 80 % o más, ¡nivel aprobado! (En la versión web puedes corregir en línea y generar tu certificado).

1. ¿Cuánta capacidad de Security Copilot incluye Microsoft 365 E5?
   - a) 100 SCU fijas al mes
   - b) 400 SCU al mes por cada 1.000 licencias, hasta 10.000
   - c) Capacidad ilimitada
   - d) 1 SCU por usuario

2. ¿Qué límites tiene el Data Security Posture Agent?
   - a) Una instancia por inquilino y dos prompts concurrentes
   - b) Diez instancias por inquilino
   - c) Una instancia por usuario y prompts ilimitados
   - d) No tiene límites documentados

3. ¿Cómo se factura Data Security Investigations?
   - a) Incluida en Microsoft 365 E5
   - b) Con licencias de Agent 365
   - c) Por consumo (almacenamiento y cómputo de IA), sin licencia específica de Microsoft 365
   - d) Con las SCU incluidas en E5

4. ¿Qué alertas de DLP clasifica el Data Security Triage Agent?
   - a) Todas, incluidas las de red
   - b) Solo las de Endpoint
   - c) Solo las de apps de IA de terceros
   - d) Las de Exchange, Teams, OneDrive, SharePoint y Endpoint

5. Al 6 de noviembre de 2026, ¿qué describe mejor el estado del Data Security Posture Agent?
   - a) Learn y el Message Center coinciden en que está en GA
   - b) MC1318248 anunció la GA para junio y julio de 2026, pero Learn todavía dice preview
   - c) Learn dice GA y el Message Center dice preview
   - d) Fue retirado en octubre de 2026

6. Desde el 1 de julio de 2026, ¿qué requiere el descubrimiento de agentes de Foundry en Defender for Cloud?
   - a) Defender CSPM
   - b) Defender for AI Services
   - c) Microsoft Purview Suite
   - d) Microsoft Agent 365

7. ¿Qué tecnología usa Defender for AI Services para alertar sobre jailbreak, fuga de datos o robo de credenciales?
   - a) Prompt Shields
   - b) Customer Key
   - c) Restricted Content Discovery
   - d) Directivas de colección

8. ¿Qué admite la protección contra inyección de prompts del AI Gateway de Entra Internet Access?
   - a) Texto, imágenes y audio
   - b) Solo texto, hasta 64.000 caracteres por prompt
   - c) Cualquier formato y sin límite
   - d) Solo archivos PDF

9. ¿Cuántas plantillas premium de Compliance Manager puede usar sin costo una organización con Microsoft 365 E5?
   - a) Una
   - b) Cinco
   - c) Tres
   - d) Ilimitadas

10. ¿Qué cambió en Defender XDR a inicios de octubre de 2026 con las señales de DLP?
   - a) Las alertas de DLP dejaron de llegar a Defender XDR por diseño
   - b) Las alertas de DLP pasaron a llegar solo a Sentinel
   - c) Se retiró la cola unificada de incidentes
   - d) Una regla de ajuste integrada convierte señales de DLP en comportamientos (BehaviorInfo)

11. ¿Cómo se crean las políticas DLP para apps registradas en Entra que usan las APIs de Purview?
   - a) Desde la ubicación Microsoft Copilot del portal
   - b) Con PowerShell (New-DlpComplianceRule)
   - c) Con la API processContent
   - d) Desde Defender XDR

12. ¿Qué pasa con la seudonimización al exportar alertas de Insider Risk por la Office 365 Management Activity API?
   - a) Se conserva siempre
   - b) Solo se conserva en Sentinel
   - c) No se conserva
   - d) La exportación por API no está disponible

13. ¿Qué cubre la integración nativa de Foundry con Purview frente a las APIs de Purview?
   - a) La integración nativa no cubre DLP ni sobreexposición; las APIs sí
   - b) La integración nativa cubre DLP y sobreexposición; las APIs no
   - c) Ninguna cubre la auditoría
   - d) Ambas requieren Agent 365 para cualquier función

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. No constituye asesoría legal ni laboral: las decisiones sobre privacidad, captura de contenido, monitoreo y normativa corresponden a tus áreas de Legal, RR. HH. y privacidad. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

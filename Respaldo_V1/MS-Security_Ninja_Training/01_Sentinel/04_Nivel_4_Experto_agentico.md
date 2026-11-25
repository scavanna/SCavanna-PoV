# Nivel 4 · Experto agéntico · SOAR avanzado, Security Copilot, agentes y MCP

*Microsoft Sentinel Ninja Training · Edición 2026*

[← Nivel 3 · Avanzado](03_Nivel_3_Avanzado.md) · [Índice del programa](README.md) · [Comunidad →](05_Comunidad.md)

<a id="experto"></a>

La ampliación de esta edición: automatización avanzada con Logic Apps, Security Copilot en el SOC, plugins y promptbooks, agentes, el servidor MCP de Sentinel y un proyecto integrador.

*L400+ · 7 módulos · ~59 horas · 175 recursos*

**Módulos de este nivel:** [X1 SOAR con Logic Apps](#x1) · [X2 Security Copilot](#x2) · [X3 Copilot + Logic Apps](#x3) · [X4 Plugins y promptbooks](#x4) · [X5 Agentes](#x5) · [X6 Servidor MCP](#x6) · [X7 Proyecto integrador](#x7)

<a id="x1"></a>

## X1 · SOAR avanzado con Azure Logic Apps

*L400+ · ~10 h · Origen: Módulo 12 · Implementing SOAR (profundización)*

Los playbooks de Sentinel son flujos de **Azure Logic Apps**, y dominarlos es dominar la respuesta. En este nivel diseñarás playbooks robustos y seguros: identidades administradas con mínimo privilegio, aprobaciones humanas con tarjetas adaptables en Teams, enriquecimiento con inteligencia de amenazas, contención en Defender y Microsoft Entra ID, integración bidireccional con ITSM, manejo de errores y reintentos, y despliegue como código.

También aprenderás a elegir entre **Logic Apps Consumption y Standard** —incluida la integración con redes privadas— y verás cómo las nuevas capacidades **agénticas** de Logic Apps, que permiten incorporar modelos de IA y herramientas dentro de un flujo, cambian el diseño de la automatización de seguridad.

**Qué vas a lograr**

- Diseñar playbooks con identidad administrada, aprobación humana y manejo de errores.
- Elegir entre Logic Apps Consumption y Standard según red, escala y costo.
- Integrar Sentinel con ITSM y con acciones de contención de Defender y Entra ID.
- Desplegar y monitorear playbooks como código.

> **Atención.** El error de campo más común: para que una regla de automatización ejecute un playbook, la cuenta de servicio de Sentinel (app «Azure Security Insights») necesita el rol Microsoft Sentinel Automation Contributor sobre el grupo de recursos del playbook, y otorgarlo requiere ser Owner de ese grupo. Sin ese permiso, el playbook aparece en gris. En escenarios MSSP hace falta además una delegación de Lighthouse para esa app ([reglas de automatización](https://learn.microsoft.com/en-us/azure/sentinel/automate-incident-handling-with-automation-rules)).

> **Consejo Ninja.** Identidad administrada del playbook: Microsoft Sentinel Responder si escribe en incidentes, Reader si solo lee ([autenticar playbooks](https://learn.microsoft.com/en-us/azure/sentinel/automation/authenticate-playbooks-to-sentinel)). Consumption admite la identidad del sistema o una asignada por el usuario; Standard admite la del sistema y varias asignadas por el usuario ([identidades administradas en Logic Apps](https://learn.microsoft.com/en-us/azure/logic-apps/authenticate-with-managed-identity)).

> **Qué cambió.** Invocar playbooks directamente desde reglas de analítica quedó en desuso en marzo de 2026: migra esas llamadas a reglas de automatización con disparador de alerta ([migración](https://learn.microsoft.com/en-us/azure/sentinel/automation/migrate-playbooks-to-automation-rules)).

> **Novedad.** Desde el portal de Defender se crean playbooks con disparador de alerta o de caso, y los disparadores clásicos de incidente, alerta y entidad aparecen como heredados ([crear playbooks](https://learn.microsoft.com/en-us/azure/sentinel/automation/create-playbooks)). En vista previa llegaron los Simple Flows, con acciones prediseñadas sin playbook ([Simple Flows](https://learn.microsoft.com/en-us/azure/sentinel/automation/create-basic-automation-rules-simple-flows)).

> **Atención.** Con Sentinel en Defender, si un incidente cambia varias veces en 5 a 10 minutos la automatización recibe una sola actualización con el último cambio; además, evita condiciones por título del incidente, porque la correlación puede cambiarlo ([reglas de automatización](https://learn.microsoft.com/en-us/azure/sentinel/automate-incident-handling-with-automation-rules)).

> **Novedad.** **Agent Loop** llegó a disponibilidad general en Logic Apps Standard el 18 de noviembre de 2025: flujos de agente autónomos y conversacionales que usan acciones y conectores como herramientas de un modelo ([anuncio](https://techcommunity.microsoft.com/blog/integrationsonazureblog/%F0%9F%8E%89announcing-general-availability-of-agent-loop-in-azure-logic-apps/4470739), [agentes autónomos](https://learn.microsoft.com/en-us/azure/logic-apps/create-autonomous-agent-workflows)). Logic Apps Standard también puede exponerse como servidor MCP remoto, en vista previa ([servidor MCP](https://learn.microsoft.com/en-us/azure/logic-apps/create-model-context-protocol-server-standard)).

> **Consejo Ninja.** Un registro «Automation rule run» con estado Success en `SentinelHealth` solo indica que la regla disparó su acción: el resultado del playbook se verifica en el historial de ejecuciones o en los diagnósticos de Logic Apps ([salud de la automatización](https://learn.microsoft.com/en-us/azure/sentinel/monitor-automation-health)).

> **Novedad.** El generador de playbooks con IA, que crea playbooks en Python de forma conversacional, figura en disponibilidad general desde mayo de 2026 en la página de novedades ([novedades de Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/whats-new)).

> **Atención.** Un cambio en la entidad Account de UEBA (prefijo UPN) obligó a revisar reglas de automatización y Logic Apps que dependan de ese campo ([novedades de Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/whats-new)).

**¿Tienes poco tiempo?**

- [Azure Logic Apps for Microsoft Sentinel playbooks](https://learn.microsoft.com/en-us/azure/sentinel/automation/logic-apps-playbooks) · Documentación
- [The Microsoft Sentinel Logic Apps connector](https://learn.microsoft.com/en-us/connectors/azuresentinel/) · Documentación
- [Create autonomous agentic workflows without human interactions in Azure Logic Apps](https://learn.microsoft.com/en-us/azure/logic-apps/create-autonomous-agent-workflows) · Documentación

**Logic Apps Consumption frente a Standard para playbooks**

| Aspecto | Consumption | Standard |
|---|---|---|
| Hospedaje | Multiinquilino, un flujo por recurso | Inquilino único, varios flujos por recurso |
| Facturación | Por ejecución de acciones y conectores | Plan reservado más conectores administrados |
| Plantillas del Content hub | Sí | No: se crean desde cero o como código |
| Tipo de flujo con Sentinel | Con estado | Solo con estado (stateful) |
| Red | Sin aislamiento propio | Integración con VNet y private endpoints |
| Identidad administrada | Del sistema o una asignada por el usuario | Del sistema y varias asignadas por el usuario |
| Agentes (Agent Loop) | Vista previa | Disponibilidad general desde noviembre de 2025 |

Fuentes: [comparación de Logic Apps](https://learn.microsoft.com/en-us/azure/logic-apps/single-tenant-overview-compare), [playbooks en Logic Apps](https://learn.microsoft.com/en-us/azure/sentinel/automation/logic-apps-playbooks) y [anuncio de Agent Loop](https://techcommunity.microsoft.com/blog/integrationsonazureblog/%F0%9F%8E%89announcing-general-availability-of-agent-loop-in-azure-logic-apps/4470739).

### Documentación, cursos y credenciales

- [Azure Logic Apps for Microsoft Sentinel playbooks](https://learn.microsoft.com/en-us/azure/sentinel/automation/logic-apps-playbooks) · Documentación · Oficial · Nuevo · Microsoft Learn · 14 may 2026. Describe los componentes del conector de Sentinel (disparadores, acciones, campos dinámicos) y las diferencias funcionales entre logic apps Consumption y Standard cuando se usan como playbooks.
- [Supported triggers and actions in Microsoft Sentinel playbooks](https://learn.microsoft.com/en-us/azure/sentinel/automation/playbook-triggers-actions) · Documentación · Oficial · Microsoft Learn. Detalla los disparadores incidente (recomendado), alerta (preview) y entidad, los campos dinámicos, las acciones principales (Get/Update incident, Add comment, Entities - Get) y los esquemas de entidades soportadas.
- [Differences between Standard single-tenant logic apps versus Consumption multitenant logic apps](https://learn.microsoft.com/en-us/azure/logic-apps/single-tenant-overview-compare) · Documentación · Oficial · Microsoft Learn. Compara Consumption (multitenant, pago por ejecución, un workflow por recurso) con Standard (single-tenant, plan de hospedaje, varios workflows stateful/stateless, VNet y endpoints privados, ASEv3).
- [Secure traffic between Standard logic apps and Azure virtual networks using private endpoints](https://learn.microsoft.com/en-us/azure/logic-apps/secure-single-tenant-workflow-virtual-network-private-endpoint) · Documentación · Oficial · Microsoft Learn. Guía para configurar endpoints privados (entrada) e integración con VNet (salida) en Logic Apps Standard, con consideraciones sobre disparadores webhook administrados y despliegue.
- [Create autonomous agentic workflows without human interactions in Azure Logic Apps](https://learn.microsoft.com/en-us/azure/logic-apps/create-autonomous-agent-workflows) · Documentación · Oficial · Microsoft Learn. Tutorial para crear workflows de tipo 'Autonomous Agents' con un bucle de agente, modelo de Azure OpenAI/Foundry/APIM y herramientas basadas en acciones de conectores, incluyendo facturación y buenas prácticas.
- [Microsoft Defender ATP - Connectors (connector reference)](https://learn.microsoft.com/en-us/connectors/wdatp/) · Documentación · Oficial · Microsoft Learn (Connector reference). Referencia del conector de Defender for Endpoint para Logic Apps con acciones de respuesta (aislar/desaislar, restringir ejecución, antivirus, paquete de investigación, live response, etiquetar equipo) y límite de 100 llamadas/60 s.
- [Authenticate workflow connections to protected Azure resources by using managed identities in Azure Logic Apps](https://learn.microsoft.com/en-us/azure/logic-apps/authenticate-with-managed-identity) · Documentación · Oficial · Microsoft Learn. Guía para habilitar identidades administradas (sistema/usuario) en Logic Apps Consumption y Standard, asignarles roles y usarlas en acciones HTTP y conectores administrados, incluyendo plantillas ARM para conexiones.
- [Microsoft Teams - Connectors (connector reference)](https://learn.microsoft.com/en-us/connectors/teams/) · Documentación · Oficial · Microsoft Learn (Connector reference). Referencia del conector de Teams con las acciones de tarjetas adaptables ('Post adaptive card and wait for a response', publicar/actualizar tarjetas), límites y problemas conocidos.
- [Create remote Model Context Protocol (MCP) servers from Standard workflows (preview)](https://learn.microsoft.com/en-us/azure/logic-apps/create-model-context-protocol-server-standard) · Documentación · Oficial · Vista previa · Microsoft Learn. Cómo exponer workflows Standard (Request trigger + Response) como herramientas de un servidor MCP remoto, protegido con OAuth (Easy Auth) o clave API, y probarlo desde VS Code. *Nota:* Permite que agentes (incluidos los de seguridad) invoquen playbooks/herramientas de Logic Apps vía MCP; soporta Streamable HTTP y SSE
- [Get started with Microsoft Azure Sentinel integration (ServiceNow Security Incident Response)](https://www.servicenow.com/docs/r/security-management/security-incident-response/get-started-with-microsoft-azure-sentinel-integration.html) · Documentación · Comunidad · Nuevo · ServiceNow · ServiceNow Docs · 10 sep 2026. Documentación del partner para la integración nativa de ingesta de incidentes de Sentinel en ServiceNow SIR, con roles, plugins y registro de aplicación en Entra ID.
- [Create and publish playbooks for Microsoft Sentinel solutions](https://learn.microsoft.com/en-us/azure/sentinel/isv/sentinel-playbook-creation) · Documentación · Oficial · Microsoft Learn. Guía para ISV/partners sobre cómo exportar un playbook como plantilla ARM saneada (script playbook_ARM_Template_Generator.ps1), usar identidad administrada y empaquetarlo en una solución de Content hub.
- [Create conversational agentic workflows with chat interactions in Azure Logic Apps](https://learn.microsoft.com/en-us/azure/logic-apps/create-conversational-agent-workflows) · Documentación · Oficial · Microsoft Learn. Tutorial para crear workflows de agentes conversacionales (chat con humanos) en Logic Apps, con herramientas, base de conocimiento, autenticación de chat externo y migración a autenticación de producción.
- [Automate build and deployment for Standard logic app workflows with Azure DevOps and Visual Studio Code](https://learn.microsoft.com/en-us/azure/logic-apps/automate-build-deployment-standard) · Documentación · Oficial · Microsoft Learn. Muestra cómo la extensión de Logic Apps (Standard) para VS Code parametriza conexiones y genera scripts y pipelines de infraestructura, CI y CD en Azure DevOps.
- [Automate DevOps deployment for Standard logic app projects from Visual Studio Code to Azure Logic Apps](https://learn.microsoft.com/en-us/azure/logic-apps/set-up-devops-deployment-single-tenant-azure-logic-apps) · Documentación · Oficial · Microsoft Learn. Explica el despliegue DevOps de Logic Apps Standard (zip deploy) con GitHub Actions o Azure Pipelines, incluyendo conexiones API, políticas de acceso y proyectos de ejemplo.
- [Isolate machine API - Microsoft Defender for Endpoint](https://learn.microsoft.com/en-us/defender-endpoint/api/isolate-machine) · Documentación · Oficial · Microsoft Learn · 23 nov 2025. Documenta la API de aislamiento (Full, Selective, UnManagedDevice), los permisos Machine.Isolate y los límites de 100 llamadas/minuto y 1.500/hora, útil para llamadas HTTP con identidad administrada.
- [Automatización de la compilación e implementación de flujos de trabajo de aplicaciones lógicas estándar con Azure DevOps y Visual Studio Code](https://learn.microsoft.com/es-es/azure/logic-apps/automate-build-deployment-standard) · Documentación · Oficial · ES · Microsoft Learn. Versión en español de la guía de CI/CD para Logic Apps Standard con VS Code y Azure DevOps.
- [Create MCP servers in API Center driven by Azure Logic Apps (preview)](https://learn.microsoft.com/en-us/azure/logic-apps/create-mcp-server-api-center) · Documentación · Oficial · Vista previa · Microsoft Learn. Muestra cómo crear y registrar en Azure API Center un servidor MCP respaldado por una logic app Standard, construyendo herramientas a partir de acciones de conectores. *Nota:* Alternativa gobernada (catálogo en API Center) para publicar herramientas MCP basadas en conectores

### Anuncios y blogs oficiales

- [Announcing General Availability of Agent Loop in Azure Logic Apps](https://techcommunity.microsoft.com/blog/integrationsonazureblog/%F0%9F%8E%89announcing-general-availability-of-agent-loop-in-azure-logic-apps/4470739) · Blog oficial · Empleado de Microsoft · DivSwa (Microsoft) · Microsoft Tech Community - Azure Integration Services Blog · 18 nov 2025. Anuncia la disponibilidad general de Agent Loop en Logic Apps Standard (Ignite 2025), que convierte Logic Apps en plataforma multiagente con agentes autónomos y conversacionales, identidad empresarial y CI/CD, e incluye el caso de SOC de Cyderes.
- [MDTI is Converging into Microsoft Sentinel and Defender XDR](https://techcommunity.microsoft.com/blog/microsoftthreatprotectionblog/mdti-is-converging-into-microsoft-sentinel-and-defender-xdr/4427991) · Blog oficial · Empleado de Microsoft · Mike_Browning · Microsoft Tech Community - Microsoft Defender XDR Blog · 22 jul 2025. Anuncia que las capacidades de Microsoft Defender Threat Intelligence (incluido premium) se integran en Defender XDR y Sentinel sin costo adicional: informes, intel profiles, IoC y TTP en Threat analytics e IoC en case management.
- [Deploy Microsoft Sentinel using Bicep](https://techcommunity.microsoft.com/blog/microsoftsentinelblog/deploy-microsoft-sentinel-using-bicep/4270970) · Blog oficial · Empleado de Microsoft · Legado aún útil · Gary Bushey · Microsoft Tech Community - Microsoft Sentinel Blog · 24 oct 2024. Explica cómo desplegar un workspace con Sentinel y soluciones de Content hub mediante Bicep (con apoyo de PowerShell), base para llevar playbooks y reglas a infraestructura como código. *Nota:* Útil como punto de partida de IaC; combinar con plantillas azuredeploy.json de playbooks y recursos Microsoft.Logic/workflows
- [Playbooks & Watchlists Part 2: Automate incident response for Deny-list/Allow-list](https://techcommunity.microsoft.com/blog/microsoftsentinelblog/playbooks--watchlists-part-2-automate-incident-response-for-deny-listallow-list/1771676) · Blog oficial · Empleado de Microsoft · Legado aún útil · Lior Tamir · Microsoft Tech Community - Microsoft Sentinel Blog · 19 oct 2020. Patrón clásico de playbook que consulta una watchlist de IP aprobadas, comenta el incidente con IP seguras/no seguras y lo cierra como Benign Positive si todas son conocidas. *Nota:* Lior Tamir (ex-PM de automatización de Sentinel, hoy 'Former Employee'); usa disparador de alerta y 'Azure Sentinel': adaptar a disparador de incidente, regla de automatización e identidad administrada

### Webinars, videos y podcasts

- [Azure Sentinel webinar: Unleash the automation Jedi tricks & build Logic Apps playbooks like a boss](https://www.youtube.com/watch?v=PaKyexE8tQ0) · Webinar · Oficial · Legado aún útil · YouTube - Microsoft Security. Webinar clásico con casos de uso y trucos profesionales para construir playbooks de Logic Apps integrados con Sentinel. *Nota:* De hace ~4 años (aún 'Azure Sentinel', portal de Azure y playbooks de alerta en reglas de análisis); los patrones de diseño siguen siendo útiles

### Laboratorios, GitHub y herramientas

- [Send-Teams-adaptive-card-on-incident-creation (SentinelSOARessentials)](https://github.com/Azure/Azure-Sentinel/blob/master/Solutions/SentinelSOARessentials/Playbooks/Send-Teams-adaptive-card-on-incident-creation/readme.md) · GitHub · Empleado de Microsoft · Benjamin Kovacevic · GitHub - Azure/Azure-Sentinel. Plantilla de playbook (disparador de incidente) que publica una tarjeta adaptable en un canal de Teams y permite al analista cambiar severidad y/o estado del incidente desde la tarjeta.
- [Isolate-MDEMachine (solución Microsoft Defender for Endpoint)](https://github.com/Azure/Azure-Sentinel/blob/master/Solutions/MicrosoftDefenderForEndpoint/Playbooks/Isolate-MDEMachine/readme.md) · GitHub · Empleado de Microsoft · Nicholas DiCola · GitHub - Azure/Azure-Sentinel. Plantilla oficial (variantes de disparador de entidad, incidente y alerta) que aísla por completo un equipo en Defender for Endpoint usando la identidad administrada del playbook.
- [Revoke-AADSignInSessions (solución Microsoft Entra ID)](https://github.com/Azure/Azure-Sentinel/blob/master/Solutions/Microsoft%20Entra%20ID/Playbooks/Revoke-AADSignInSessions/readme.md) · GitHub · Oficial · Microsoft Sentinel community · GitHub - Azure/Azure-Sentinel. Plantilla oficial (entidad, incidente o alerta) que revoca todas las sesiones de inicio de sesión de un usuario vía Microsoft Graph con identidad administrada y notifica a su jefe por correo.
- [Pricing - Logic Apps](https://azure.microsoft.com/en-us/pricing/details/logic-apps/) · Herramienta · Oficial · Microsoft Azure. Página de precios de Logic Apps: Consumption (pago por ejecución) frente a Standard (Workflow Service Plan por vCPU/memoria, ASEv3, modelo híbrido) y tarifas por llamada de conectores estándar y enterprise.
- [Tutorial: Automatically check and record IP address reputation information in incidents](https://learn.microsoft.com/en-us/azure/sentinel/tutorial-enrich-ip-information) · Laboratorio · Oficial · Microsoft Learn. Tutorial oficial que crea un playbook de enriquecimiento desde la plantilla 'IP Enrichment - Virus Total report', autoriza sus conexiones (Sentinel con identidad administrada) y lo invoca con una regla de automatización.
- [Azure-Sentinel/Solutions/SentinelSOARessentials/Playbooks](https://github.com/Azure/Azure-Sentinel/tree/master/Solutions/SentinelSOARessentials/Playbooks) · GitHub · Oficial · GitHub - Azure/Azure-Sentinel. Carpeta de la solución 'Sentinel SOAR Essentials' con los playbooks base de Microsoft (notificaciones y tarjetas en Teams, Post-Message-Teams, cierre de incidentes, plantillas de entity analyzer) que se instalan desde Content hub.
- [Azure-Sentinel/.github/instructions/playbooks.instructions.md](https://github.com/Azure/Azure-Sentinel/blob/master/.github/instructions/playbooks.instructions.md) · GitHub · Oficial · GitHub - Azure/Azure-Sentinel. Guía de contribución (también usada como instrucciones para asistentes de IA) que define la estructura obligatoria de un playbook: azuredeploy.json, README, metadatos, parámetro PlaybookName y convenciones para conectores personalizados y Function Apps.
- [Notify-IncidentClosed (SentinelSOARessentials)](https://github.com/Azure/Azure-Sentinel/blob/master/Solutions/SentinelSOARessentials/Playbooks/Notify-IncidentClosed/readme.md) · GitHub · Empleado de Microsoft · Benjamin Kovacevic · GitHub - Azure/Azure-Sentinel. Playbook que usa el disparador de actualización de incidentes para notificar por Teams/Outlook cuando un incidente se cierra (regla: When incident is updated + Status changed to Closed).
- [Azure-Sentinel/Solutions/VirusTotal/Playbooks](https://github.com/Azure/Azure-Sentinel/tree/master/Solutions/VirusTotal/Playbooks) · GitHub · Oficial · Microsoft y comunidad · GitHub - Azure/Azure-Sentinel. Plantillas de enriquecimiento con VirusTotal (reportes de IP, dominio, URL y archivo) en variantes de disparador de incidente y alerta, empaquetadas en la solución de Content hub.
- [Azure-Sentinel Playbooks ReadMe (deploy and templatize playbooks, ARM Template Generator)](https://raw.githubusercontent.com/Azure/Azure-Sentinel/master/Playbooks/ReadMe.md) · GitHub · Oficial · GitHub - Azure/Azure-Sentinel. Instrucciones para desplegar playbooks del repositorio como plantilla ARM personalizada, autorizar conexiones y convertir un playbook propio en plantilla ARM reutilizable con el 'Playbook ARM Template Generator' o manualmente.
- [Block-AADUser (Microsoft Entra ID solution playbook)](https://github.com/Azure/Azure-Sentinel/blob/master/Solutions/Microsoft%20Entra%20ID/Playbooks/Block-AADUser/readme.md) · GitHub · Oficial · GitHub - Azure/Azure-Sentinel. Plantilla de contención que deshabilita en Entra ID las cuentas del incidente, deja un comentario en el incidente y notifica al manager, sin deshabilitar cuentas administrativas.
- [KQL-Collectors: IOC Collection into MISP](https://github.com/Sergio-Albea-Git/Threat-Hunting-KQL-Queries/blob/main/KQL-Collectors/Readme.md) · GitHub · MVP · Sergio Albea · GitHub. Guía paso a paso para recolectar IOCs observados en Defender XDR con consultas KQL vía Microsoft Graph y enviarlos a MISP con una Logic App que lee secretos de Key Vault con identidad administrada.
- [Post-Message-Teams (Sentinel SOAR Essentials)](https://github.com/Azure/Azure-Sentinel/tree/master/Solutions/SentinelSOARessentials/Playbooks/Post-Message-Teams) · GitHub · Oficial · GitHub - Azure/Azure-Sentinel. Plantilla sencilla de playbook que publica un mensaje en un canal de Teams a partir de un incidente, punto de partida antes de usar tarjetas adaptables con respuesta.
- [Group-IB playbooks - User guide (Logic Apps Standard)](https://github.com/Azure/Azure-Sentinel/blob/master/Solutions/Group-IB/Playbooks/USER_GUIDE_STANDARD.md) · GitHub · Comunidad · Group-IB · GitHub - Azure/Azure-Sentinel. Guía de un partner para desplegar y operar sus playbooks de Sentinel sobre Logic Apps Standard, útil como ejemplo real de empaquetado Standard fuera de las plantillas de Content hub.
- [joetanx/autosoc](https://github.com/joetanx/autosoc/tree/main) · GitHub · Comunidad · joetanx · GitHub. Proyecto comunitario de triaje agéntico en el que una Logic App de Sentinel envía el incidente a un agente (LangGraph en Azure Container Apps) que investiga y devuelve el resultado.
- [Defender_XDR_Phishing_Playbook_for_SecOps-Tasks (readme)](https://raw.githubusercontent.com/Azure/Azure-Sentinel/refs/heads/master/Solutions/SentinelSOARessentials/Playbooks/Defender_XDR_Phishing_Playbook_for_SecOps-Tasks/readme.md) · GitHub · Oficial · Microsoft y contribuidores · GitHub - Azure/Azure-Sentinel. Playbook de la solución SentinelSOARessentials que añade tareas guiadas de SecOps a incidentes de phishing de Defender XDR.
- [MDE-IsolateMachine-Nested (MasterPlaybooks Remediation-Host)](https://github.com/Azure/Azure-Sentinel/blob/master/MasterPlaybooks/Remediation-Host/MDE-IsolateMachine-Nested/readme.md) · GitHub · Empleado de Microsoft · Legado aún útil · Nicholas DiCola · GitHub - Azure/Azure-Sentinel. Ejemplo del patrón 'master playbook' en el que un playbook orquestador invoca sub-playbooks anidados de remediación por proveedor (MDE, CrowdStrike, Carbon Black, Meraki) con un esquema común. *Nota:* Patrón de diseño útil para SOAR avanzado (modularidad y reutilización); revisar permisos (Machine.Isolate) y modernizar conexiones
- [AzureMonitor-ManagedId (playbook)](https://github.com/Azure/Azure-Sentinel/tree/master/Playbooks/AzureMonitor-ManagedId) · GitHub · Comunidad · Legado aún útil · Comunidad (créditos a Koos Goossens) · GitHub - Azure/Azure-Sentinel. Playbook que replica el bloque de consulta KQL de Azure Monitor usando una acción HTTP con identidad administrada (rol Log Analytics Reader) y una transformación Liquid. *Nota:* Requiere Integration Account para el mapa Liquid; patrón útil cuando un conector no soporta identidad administrada
- [EnrichIP-VirusTotal-Nested (Master Playbooks - IP Enrichment)](https://github.com/Azure/Azure-Sentinel/blob/master/MasterPlaybooks/IP-Enrichment/EnrichIP-VirusTotal-Nested/readme.md) · GitHub · Comunidad · Legado aún útil · Microsoft / comunidad · GitHub - Azure/Azure-Sentinel. Ejemplo del patrón de playbooks maestro/anidados: un playbook hijo reutilizable enriquece IP con VirusTotal y devuelve el resultado al playbook orquestador. *Nota:* Patrón útil para modularizar; revisar conectores y autenticación (usar identidad administrada donde sea posible)

### Comunidad: blogs, libros, newsletters y eventos

- [Microsoft Defender for Endpoint series – Automation via Logic Apps and Sentinel – Part9](https://jeffreyappel.nl/microsoft-defender-for-endpoint-series-automation-via-logic-apps-and-sentinel-part9/) · Blog · MVP · Legado aún útil · Jeffrey Appel · Jeffrey Appel - Microsoft Security blog · 9 feb 2023. Muestra automatizaciones de Defender for Endpoint con Logic Apps e identidad administrada: etiquetado de equipos vía consultas de hunting y acciones de respuesta MDE desde playbooks de Sentinel. *Nota:* Anterior a la plataforma unificada; la acción de Advanced Hunting del conector MDE se retira el 1-feb-2027 (usar Graph Security API)
- [Automate Security Alert Response with Bicep and Sentinel](https://kloudschool.com/stop-reacting-manually-automating-security-alert-response-with-bicep) · Blog · Comunidad · Induranga Lokuliyanage · KloudSchool · 1 nov 2025. Ejemplo comunitario que despliega con Bicep la conexión API de Sentinel, un playbook con disparador de incidente y la regla de automatización, incluyendo la asignación de roles necesaria.
- [Logic Apps MS Teams Connector - MessageId Not Available for TimedOut Actions with Adaptive Cards](https://learn.microsoft.com/en-gb/answers/questions/2279002/logic-apps-ms-teams-connector-messageid-not-availa) · Blog · Comunidad · Comunidad Microsoft Q&A · Microsoft Q&A · 27 may 2025. Hilo que documenta una limitación real del patrón de aprobación por Teams: si 'Post adaptive card and wait for a response' expira, no devuelve el MessageId para actualizar la tarjeta.

**Manos a la obra**

1. `Laboratorio` Orden de reglas: crea dos reglas de automatización (la primera baja la severidad y la segunda solo aplica a severidad media o mayor) y observa que la segunda evalúa el incidente ya modificado.
2. `Laboratorio` Aprobación humana: despliega la plantilla de tarjeta adaptable de Teams en la creación de incidentes y espera la respuesta del analista ([conector de Teams](https://learn.microsoft.com/en-us/connectors/teams/)).
3. `Laboratorio` Enriquecimiento con identidad administrada: sigue el [tutorial de enriquecimiento de IP](https://learn.microsoft.com/en-us/azure/sentinel/tutorial-enrich-ip-information) y asigna a la identidad solo el rol Responder.
4. `Laboratorio` Contención aprobada: combina la aprobación con [Isolate-MDEMachine](https://github.com/Azure/Azure-Sentinel/blob/master/Solutions/MicrosoftDefenderForEndpoint/Playbooks/Isolate-MDEMachine/readme.md) y [Revoke-AADSignInSessions](https://github.com/Azure/Azure-Sentinel/blob/master/Solutions/Microsoft%20Entra%20ID/Playbooks/Revoke-AADSignInSessions/readme.md).
5. `Laboratorio parcial` Red privada: despliega un playbook en Logic Apps Standard con private endpoint y la política de restricción de acceso que permite a Sentinel invocarlo ([playbooks en Logic Apps](https://learn.microsoft.com/en-us/azure/sentinel/automation/logic-apps-playbooks)).
6. `Laboratorio` Como código y observable: exporta el playbook a ARM o Bicep, publícalo con un pipeline y correlaciona `SentinelHealth` con los diagnósticos de Logic Apps.
7. `Laboratorio parcial` Agéntico: crea un flujo de agente autónomo en Logic Apps Standard que reciba un incidente, consulte herramientas y proponga una acción para aprobación humana ([agentes autónomos](https://learn.microsoft.com/en-us/azure/logic-apps/create-autonomous-agent-workflows)).

**¿Quieres profundizar?**

- [Send-Teams-adaptive-card-on-incident-creation (SentinelSOARessentials)](https://github.com/Azure/Azure-Sentinel/blob/master/Solutions/SentinelSOARessentials/Playbooks/Send-Teams-adaptive-card-on-incident-creation/readme.md) · GitHub
- [Isolate-MDEMachine (solución Microsoft Defender for Endpoint)](https://github.com/Azure/Azure-Sentinel/blob/master/Solutions/MicrosoftDefenderForEndpoint/Playbooks/Isolate-MDEMachine/readme.md) · GitHub
- [Notify-IncidentClosed (SentinelSOARessentials)](https://github.com/Azure/Azure-Sentinel/blob/master/Solutions/SentinelSOARessentials/Playbooks/Notify-IncidentClosed/readme.md) · GitHub
- [KQL-Collectors: IOC Collection into MISP](https://github.com/Sergio-Albea-Git/Threat-Hunting-KQL-Queries/blob/main/KQL-Collectors/Readme.md) · GitHub

<a id="x2"></a>

## X2 · Security Copilot para operaciones de seguridad

*L400+ · ~8 h · Origen: Nuevo (sucede a "Copilot for Security" y al Security Copilot Ninja Training)*

**Microsoft Security Copilot** lleva la IA generativa a la operación diaria del SOC: resume incidentes, sugiere respuestas guiadas, analiza scripts y archivos sospechosos, traduce lenguaje natural a KQL, redacta informes para distintas audiencias y consulta en un mismo diálogo datos de Sentinel, Defender, Entra, Intune, Purview e inteligencia de amenazas. Se usa **embebido** en el portal de Defender o desde su **experiencia independiente**, se dimensiona en unidades de cómputo de seguridad (SCU) y respeta los permisos de cada usuario.

Este módulo cubre cuándo y cómo usarlo en el ciclo del incidente, cómo escribir buenos prompts, qué plugins habilitar para el contexto del SOC, cómo funcionan los promptbooks integrados y cómo gobernar el acceso, la privacidad y el consumo.

**Qué vas a lograr**

- Usar Security Copilot embebido en incidentes, búsqueda avanzada y análisis de scripts.
- Escribir prompts efectivos y ejecutar promptbooks para triage e investigación.
- Configurar plugins y permisos y monitorear el consumo de SCU.

> **Novedad.** Microsoft 365 E5 y E7 incluyen Security Copilot: **400 SCU al mes por cada 1.000 licencias de usuario pagas, hasta 10.000 SCU mensuales**. El despliegue empezó el 18 de noviembre de 2025 y continúa por fases con aviso previo de 30 días; el aprovisionamiento es automático y crea una capacidad y un workspace por defecto ([inclusión en E5](https://learn.microsoft.com/en-us/copilot/security/security-copilot-inclusion), [aprovisionamiento automático](https://learn.microsoft.com/en-us/copilot/security/auto-provisioning-security-copilot)).

> **Atención.** Para clientes regulados de MCSA: con el aprovisionamiento automático, la ubicación de datos sigue la geografía de Entra y la evaluación de prompts es global salvo que los datos estén en la UE ([aprovisionamiento automático](https://learn.microsoft.com/en-us/copilot/security/auto-provisioning-security-copilot)). Revísalo con el área legal antes de habilitarlo.

> **Consejo Ninja.** Facturación: la capacidad aprovisionada se cobra por bloques de hora completos y lo no usado no se acumula; el excedente (overage) se cobra por uso y puede limitarse ([capacidad y SCU](https://learn.microsoft.com/en-us/copilot/security/security-compute-units-capacity)). El panel de uso muestra 90 días por experiencia, usuario, plugin y categoría ([monitorear uso](https://learn.microsoft.com/en-us/copilot/security/manage-usage)).

> **Novedad.** En incidentes de Sentinel dentro del portal de Defender, Security Copilot genera resúmenes, respuestas guiadas, análisis de scripts e informes de incidente ([resumen de incidentes](https://learn.microsoft.com/en-us/defender-xdr/security-copilot-m365d-incident-summary)). En la búsqueda avanzada, el **Threat Hunting Assistant** (antes Threat Hunting Agent) traduce lenguaje natural a KQL y descubre tablas de Sentinel según tus permisos ([búsqueda con Security Copilot](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-security-copilot)).

> **Consejo Ninja.** Security Copilot nunca excede los permisos del usuario en cada plugin, y sus roles propios (owner y contributor) no son roles de Entra ([autenticación y roles](https://learn.microsoft.com/en-us/copilot/security/authentication)).

**¿Tienes poco tiempo?**

- [Learn about Security Copilot for Microsoft 365 E5 and E7 customers](https://learn.microsoft.com/en-us/copilot/security/security-copilot-inclusion) · Documentación
- [Getting Started with Security Copilot (Security Copilot Skilling Series)](https://www.youtube.com/watch?v=g2I1rozWGVI) · Webinar

### Documentación, cursos y credenciales

- [Microsoft Security Copilot in advanced hunting](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-security-copilot) · Documentación · Oficial · Nuevo · Microsoft Learn · 10 sep 2026. Describe los dos modos del Threat Hunting Assistant en Advanced hunting (Rich insights conversacional y Query only o query assistant) y cómo cambiar al Security Analyst Agent; descubre tablas según permisos, incluidas tablas personalizadas de Sentinel.
- [Microsoft Security Copilot advanced hunting query assistant](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-security-copilot-query-assistant) · Documentación · Oficial · Nuevo · Microsoft Learn · 5 ago 2026. Lenguaje natural a KQL en Advanced hunting: genera la consulta, explica su lógica (See the logic behind the query) y permite ejecutarla o añadirla al editor.
- [Enhance security operations by using Microsoft Security Copilot (SC-5006)](https://learn.microsoft.com/en-us/training/paths/security-copilot-and-ai/) · Curso · Oficial · Microsoft Learn. Ruta de Learn (6 módulos, ~6 h) sobre Security Copilot que incluye un módulo dedicado a agentes (identidades, permisos, agentes de Entra/Defender/Purview/Intune y creación de agentes propios).
- [Deploy and operate Microsoft Security Copilot (learning path)](https://learn.microsoft.com/en-us/training/paths/deploy-operate-security-copilot/) · Curso · Oficial · Microsoft Learn. Ruta de Learn (3 módulos, ~1 h 41 min) para desplegar Security Copilot: prompts, workspaces con SCU y residencia de datos, roles, gobierno de plugins y ciclo de vida de agentes Microsoft y de partners (Security Store).
- [Learn about Security Copilot for Microsoft 365 E5 and E7 customers](https://learn.microsoft.com/en-us/copilot/security/security-copilot-inclusion) · Documentación · Oficial · Microsoft Learn. Explica la inclusión de Security Copilot en Microsoft 365 E5/E7 (anunciada en Ignite 2025): aprovisionamiento automático y 400 SCU/mes por cada 1.000 licencias pagadas, hasta 10.000 SCU/mes.
- [Microsoft Security Copilot Security Compute Units and capacity](https://learn.microsoft.com/en-us/copilot/security/security-compute-units-capacity) · Documentación · Oficial · Microsoft Learn. Describe las SCU, la capacidad aprovisionada (facturada por hora, mínimo 1 SCU, sin acumulación), la capacidad de excedente (overage, facturada por uso) y la capacidad por defecto creada para clientes E5/E7.
- [Security Copilot with Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/sentinel-security-copilot) · Documentación · Oficial · Microsoft Learn. Explica cómo se usan los datos de Sentinel con Security Copilot: plugins standalone Microsoft Sentinel (Preview) y Natural language to KQL for Microsoft Sentinel (Preview), workspace por defecto y experiencias embebidas sobre incidentes unificados en Defender.
- [Summarize an incident with Microsoft Copilot in Microsoft Defender](https://learn.microsoft.com/en-us/defender-xdr/security-copilot-m365d-incident-summary) · Documentación · Oficial · Microsoft Learn. Resumen automático de incidentes en el portal de Defender (aplica a Sentinel) con línea de tiempo, activos, IoC y actores, más la configuración para generarlo siempre, por severidad o bajo demanda con estimación de SCU.
- [Triage and investigate incidents with guided responses from Microsoft Copilot in Microsoft Defender](https://learn.microsoft.com/en-us/defender-xdr/security-copilot-m365d-guided-response) · Documentación · Oficial · Microsoft Learn. Respuestas guiadas con tarjetas de triage, contención, investigación y remediación aplicables con un clic, respetando los permisos URBAC del analista.
- [Microsoft Security Copilot Threat Hunting Assistant in advanced hunting](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-security-copilot-threat-hunting-assistant) · Documentación · Oficial · Microsoft Learn. Experiencia conversacional de caza que genera y ejecuta KQL, interpreta resultados con gráficos, sugiere preguntas de seguimiento y descubre el esquema real del entorno.
- [Prompting in Microsoft Security Copilot](https://learn.microsoft.com/en-us/copilot/security/prompting-security-copilot) · Documentación · Oficial · Microsoft Learn. Cómo iniciar sesiones de prompts, usar la biblioteca de prompts y promptbooks filtrando por rol y plugin, revisar el registro de proceso y cuándo preferir agentes o prompts.
- [Use promptbooks in Microsoft Security Copilot](https://learn.microsoft.com/en-us/copilot/security/using-promptbooks) · Documentación · Oficial · Microsoft Learn. Catálogo de promptbooks integrados (investigación de incidentes de Sentinel y Defender XDR, análisis de usuario, script sospechoso, perfil de actor, impacto de vulnerabilidad, TI 360) y cómo ejecutarlos.
- [Understand authentication in Microsoft Security Copilot](https://learn.microsoft.com/en-us/copilot/security/authentication) · Documentación · Oficial · Microsoft Learn. Modelo de acceso: autenticación on-behalf-of, roles propios Security Copilot owner y contributor (no son roles de Entra), roles de Entra/Intune/Purview que heredan owner y roles necesarios para aprovisionar capacidad.
- [Privacy and data security in Microsoft Security Copilot](https://learn.microsoft.com/en-us/copilot/security/privacy-data-security) · Documentación · Oficial · Microsoft Learn. Diferencia datos de cliente y logs de sistema, opciones de compartición de datos, ubicación de almacenamiento y de evaluación de prompts, retención, DSR del RGPD y protección de datos.
- [Manage security compute unit usage in Security Copilot](https://learn.microsoft.com/en-us/copilot/security/manage-usage) · Documentación · Oficial · Microsoft Learn. Panel de monitorización de uso con 90 días de datos por capacidad, sesión, usuario, plugin, experiencia (standalone, embebida, Logic Apps) y categoría (prompt, promptbook, agente, primitive), con filtros y exportación.
- [Understand how Security Copilot is auto provisioned for eligible Microsoft 365 E5 and E7 customers](https://learn.microsoft.com/en-us/copilot/security/auto-provisioning-security-copilot) · Documentación · Oficial · Microsoft Learn. Qué se crea automáticamente para E5/E7: capacidad virtual y workspace por defecto, ubicación de datos según la geografía de Entra, compartición de datos desactivada, evaluación de prompts (UE o global), acceso a datos de M365 activado y roles por defecto.
- [Microsoft Security Copilot - Microsoft Adoption](https://adoption.microsoft.com/en-us/security-copilot/) · Curso · Oficial · Microsoft Adoption. Hub de adopción con talleres técnicos globales, entornos, catálogo de agentes por dominio, estudios de impacto, casos de clientes, partners y FAQ de la inclusión en E5/E7.
- [What's new in Microsoft Security Copilot?](https://learn.microsoft.com/en-us/copilot/security/whats-new-copilot-security) · Documentación · Oficial · Microsoft Learn · 17 abr 2026. Registro mensual de novedades de Security Copilot: Security Analyst Agent (preview, abr-2026), inclusión E5 (nov-2025), agent builder y Security Store (preview, sep-2025), GA de agentes de Entra e Intune (jul-2025), overage GA (abr-2025).
- [Microsoft Security Copilot in your workflows](https://learn.microsoft.com/en-us/copilot/security/workflows-overview) · Documentación · Oficial · Nuevo · Microsoft Learn · 1 may 2026. Explica cómo combinar agentes, prompts, promptbooks, plugins y conectores según el escenario (análisis ad hoc, flujos repetibles, automatización) y los tres perfiles: administradores, usuarios finales y desarrolladores.
- [Mitigate threats using Microsoft Security Copilot (SC-200 learning path)](https://learn.microsoft.com/en-us/training/paths/sc-200-mitigate-threats-using-microsoft-copilot-for-security/) · Curso · Oficial · Microsoft Learn. Ruta de Learn alineada con SC-200 (5 módulos, ~4 h 54 min) que introduce IA generativa y agentes, Security Copilot, sus funciones, experiencias embebidas y simulaciones guiadas.
- [Script analysis with Microsoft Copilot in Microsoft Defender](https://learn.microsoft.com/en-us/defender-xdr/security-copilot-m365d-script-analysis) · Documentación · Oficial · Microsoft Learn. Análisis de scripts y líneas de comando sospechosas desde la historia del ataque o la línea de tiempo del dispositivo, con explicación y técnicas MITRE ATT&CK asociadas.
- [Create an incident report with Microsoft Copilot in Microsoft Defender](https://learn.microsoft.com/en-us/defender-xdr/security-copilot-m365d-create-incident-report) · Documentación · Oficial · Microsoft Learn. Genera un informe de incidente que consolida datos de Sentinel y Defender: hitos, analistas, clasificación, acciones manuales y automáticas (incluidos playbooks de Sentinel ejecutados) y próximos pasos; exportable a PDF.
- [Summarize Microsoft Sentinel incidents with Security Copilot](https://learn.microsoft.com/en-us/azure/sentinel/sentinel-security-copilot-incident-summary) · Documentación · Oficial · Vista previa · Nuevo · Microsoft Learn · 2 jul 2026. Resumen de incidentes de Sentinel con Copilot (hasta 100 alertas) que añade enriquecimientos como riesgo y criticidad de usuario y dispositivo y coincidencias con watchlists. *Nota:* Experiencia del portal de Azure en preview; la dirección estratégica es el portal de Defender, donde se usan resumen, respuestas guiadas e informes
- [Use case: Investigate an incident and associated suspicious entities](https://learn.microsoft.com/en-us/copilot/security/investigate-incident-malicious-script) · Documentación · Oficial · Nuevo · Microsoft Learn · 29 may 2026. Caso de uso guiado que combina resumen de incidente y análisis de script en Defender con continuación en el portal standalone para reputación de indicadores y recomendaciones.

### Anuncios y blogs oficiales

- [Agents built into your workflow: Get Security Copilot with Microsoft 365 E5](https://www.microsoft.com/en-us/security/blog/2025/11/18/agents-built-into-your-workflow-get-security-copilot-with-microsoft-365-e5/) · Blog oficial · Empleado de Microsoft · Dorothy Li · Microsoft Security Blog · 18 nov 2025. Anuncio de Ignite 2025 de la inclusión de Security Copilot en Microsoft 365 E5, 12 nuevos agentes de Microsoft en preview y más de 30 agentes de partners en el Security Store.
- [Security Copilot agents in Microsoft 365 E5](https://www.microsoft.com/en-us/security/security-copilot-in-microsoft-365-e5) · Blog oficial · Oficial · Microsoft Security · nov 2025. Página oficial con las preguntas frecuentes del beneficio de Security Copilot en Microsoft 365 E5 (capacidad de SCU incluida, calendario de activación y agentes disponibles).

### Webinars, videos y podcasts

- [Microsoft Security Copilot video hub - Microsoft Adoption](https://adoption.microsoft.com/en-us/security-copilot/video-hub/) · Video · Oficial · Varios (equipos de Microsoft Security) · Microsoft Adoption. Videoteca con demos breves de agentes (Security Alert Triage, Security Analyst, TI Briefing), agentes de partners y escenarios de Logic Apps con Sentinel (enriquecimiento de incidentes, inicios de sesión fallidos, análisis de scripts).
- [Security Copilot Skilling Series (playlist)](https://www.youtube.com/playlist?list=PLmAptfqzxVEWGjqfUaMx9R2DjPjrXrfjK) · Webinar · Oficial · Equipos de producto de Microsoft Security · YouTube – Microsoft Security Community. Serie de webinars (≈18 vídeos) de Security Copilot con Defender, Entra, Intune y Purview, agentes personalizados, 'Logic Apps vs. agentes de Security Copilot' y una sesión de un MVP sobre agentes.
- [What's New in Security Copilot for Defender](https://www.youtube.com/watch?v=mek5psEpmB4) · Webinar · Empleado de Microsoft · Doug Helton · Microsoft Security Community (YouTube) · 18 dic 2025. Repaso de novedades de Security Copilot embebido en Defender tras Ignite 2025, agentes de Defender, demo y despliegue de agentes de Microsoft y de terceros.

### Comunidad: blogs, libros, newsletters y eventos

- [Rod's Blog (Substack) - Security Copilot tag](https://rodtrent.substack.com/t/security-copilot) · Newsletter · Comunidad · Rod Trent · Substack. Colección de artículos de Rod Trent sobre Security Copilot: inclusión E5, workspaces, calculadora de capacidad, SCU de excedente y prompts del día, además del boletín THE PROMPT for Microsoft Security.

**Manos a la obra**

1. `Solo producción` Verifica si tu tenant tiene la inclusión de E5, revisa la capacidad y el workspace creados y explora el [panel de uso](https://learn.microsoft.com/en-us/copilot/security/manage-usage).
2. `Laboratorio parcial` En un incidente de Sentinel, genera el resumen y las respuestas guiadas y compáralos con tu propio triage.
3. `Laboratorio parcial` En la búsqueda avanzada, genera tres consultas con el Threat Hunting Assistant en modo de solo consulta; revisa y corrige el KQL antes de ejecutarlo.
4. `Laboratorio parcial` Ejecuta un promptbook integrado de investigación sobre un incidente con el plugin de Sentinel ([Security Copilot en Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/sentinel-security-copilot)) y exporta el informe.
5. `Laboratorio` Redacta una guía de prompts para tu SOC: contexto, objetivo, fuentes y formato de salida esperados.

**¿Quieres profundizar?**

- [What's New in Security Copilot for Defender](https://www.youtube.com/watch?v=mek5psEpmB4) · Webinar
- [Microsoft Security Copilot video hub - Microsoft Adoption](https://adoption.microsoft.com/en-us/security-copilot/video-hub/) · Video
- [Security Copilot Skilling Series (playlist)](https://www.youtube.com/playlist?list=PLmAptfqzxVEWGjqfUaMx9R2DjPjrXrfjK) · Webinar
- [Rod's Blog (Substack) - Security Copilot tag](https://rodtrent.substack.com/t/security-copilot) · Newsletter

<a id="x3"></a>

## X3 · Security Copilot y Logic Apps: automatización con IA

*L400+ · ~5 h · Origen: Nuevo*

La IA rinde más cuando no espera a que alguien le pregunte. Con el **conector de Security Copilot para Logic Apps**, un playbook puede enviar un prompt o ejecutar un promptbook en cuanto se crea un incidente y escribir el resultado —un resumen, una evaluación de riesgo, un análisis de entidades o de un script— como comentario del incidente, como tarea o como mensaje al equipo.

Este módulo combina lo aprendido en SOAR con Security Copilot para construir triage asistido por IA, con atención especial a tres preguntas de diseño: qué incidentes merecen gastar SCU, cómo mantener a una persona en el circuito de decisión y cómo medir si la IA realmente ahorra tiempo al SOC.

**Qué vas a lograr**

- Invocar Security Copilot desde un playbook y registrar el resultado en el incidente.
- Ejecutar promptbooks desde Logic Apps con parámetros del incidente.
- Aplicar controles de costo y revisión humana a la automatización con IA.

> **Novedad.** El conector de Security Copilot para Logic Apps ofrece **Submit a Security Copilot prompt** (con sesión, plugins y Direct Skill para saltear el planificador) y **Submit a Security Copilot promptbook** ([conector](https://learn.microsoft.com/en-us/copilot/security/connector-logicapp)); una acción más reciente ejecuta agentes configurados en el workspace predeterminado ([disparar agentes](https://learn.microsoft.com/en-us/copilot/security/connector-logicapp-agent-trigger)).

> **Atención.** Autenticación: la documentación del conector indica OAuth delegado (Authorization Code); la referencia del conector y los ejemplos oficiales mencionan otras opciones. Valídalo en laboratorio antes de diseñar producción ([referencia del conector](https://learn.microsoft.com/en-us/connectors/securitycopilot/)).

> **Consejo Ninja.** Los ejemplos oficiales advierten que combinar Logic Apps con Security Copilot puede elevar el consumo de SCU. Usa Direct Skills, limita las llamadas y adjunta el playbook solo a incidentes que lo justifiquen mediante condiciones en la regla de automatización ([ejemplos oficiales](https://github.com/Azure/Security-Copilot/blob/main/Logic%20Apps/Readme.md)).

> **Novedad.** En sentido inverso, una Logic App con disparador HTTP puede registrarse como habilidad de Security Copilot y ser invocada por prompts, promptbooks o agentes ([Logic Apps como plugin](https://learn.microsoft.com/en-us/copilot/security/developer/plugin-logic-apps)). Y el conector «Microsoft Sentinel MCP tools» permite usar el entity analyzer desde un playbook ([MCP en Logic Apps](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-mcp-logic-apps)).

**¿Tienes poco tiempo?**

- [Microsoft Security Copilot Logic Apps connector](https://learn.microsoft.com/en-us/copilot/security/connector-logicapp) · Documentación
- [When to Use Logic Apps vs. Security Copilot Agents](https://www.youtube.com/watch?v=GMST8t6hF8Y) · Webinar
- [SecurityCopilot-Sentinel-Incident-Investigation (Logic App)](https://github.com/Azure/Security-Copilot/tree/main/Logic%20Apps/SecurityCopilot-Sentinel-Incident-Investigation) · GitHub

### Documentación, cursos y credenciales

- [What is Microsoft Sentinel's support for Model Context Protocol (MCP)?](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-mcp-overview) · Documentación · Oficial · Microsoft Learn. Introduce el servidor MCP alojado de Sentinel y sus colecciones de herramientas para explorar el data lake, analizar entidades, triage y crear agentes en lenguaje natural.
- [Azure Logic Apps plugin in Microsoft Security Copilot](https://learn.microsoft.com/en-us/copilot/security/developer/plugin-logic-apps) · Documentación · Oficial · Microsoft Learn. Explica el sentido inverso: exponer un workflow de Logic Apps (disparador HTTP Request) como skill de Security Copilot mediante un manifiesto YAML para invocarlo desde prompts, promptbooks o agentes.
- [Learn about Security Copilot for Microsoft 365 E5 and E7 customers](https://learn.microsoft.com/en-us/copilot/security/security-copilot-inclusion) · Documentación · Oficial · Microsoft Learn. Explica la inclusión de Security Copilot en Microsoft 365 E5/E7 (anunciada en Ignite 2025): aprovisionamiento automático y 400 SCU/mes por cada 1.000 licencias pagadas, hasta 10.000 SCU/mes.
- [Trigger Security Copilot agents from Azure Logic Apps](https://learn.microsoft.com/en-us/copilot/security/connector-logicapp-agent-trigger) · Documentación · Oficial · Microsoft Learn. Documenta la acción 'Execute a Security Copilot Agent' del conector de Security Copilot para invocar agentes ya configurados desde un workflow de Logic Apps, encadenarlos con otras acciones y pasarles entradas dinámicas.
- [Microsoft Security Copilot Logic Apps connector](https://learn.microsoft.com/en-us/copilot/security/connector-logicapp) · Documentación · Oficial · Microsoft Learn · 15 ene 2026. Describe las dos acciones del conector de Security Copilot para Logic Apps (enviar prompt y enviar promptbook), sus parámetros (sesión, plugins, skill directa) y los requisitos de autenticación.
- [Build logic apps with Microsoft Sentinel MCP tools (preview)](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-mcp-logic-apps) · Documentación · Oficial · Vista previa · Microsoft Learn. Explica cómo usar en Logic Apps el conector 'Microsoft Sentinel MCP tools', empezando por la herramienta entity analyzer (usuarios y URL sobre el data lake), vía plantillas de SOAR Essentials o como acción en playbooks existentes. *Nota:* Plantillas: Incident Trigger / Url Trigger / HTTP Trigger Entity Analyzer; la identidad de la Logic App necesita el rol Security reader; admite Entra ID, service principal e identidad administrada. Alternativa a Security Copilot para enriquecer con IA dentro de playbooks
- [Microsoft Security Copilot (Preview) - Connectors](https://learn.microsoft.com/en-us/connectors/securitycopilot/) · Documentación · Oficial · Vista previa · Microsoft Learn - Connector reference. Referencia técnica del conector para Logic Apps, Power Automate, Power Apps y Copilot Studio: acciones (incluida Execute a Security Copilot Agent), autenticación OAuth o service principal y límite de 600 llamadas por minuto por conexión. *Nota:* No disponible en Azure Government, China ni DoD; la acción para ejecutar agentes configurados habilita orquestar agentes desde SOAR

### Anuncios y blogs oficiales

- [Security Copilot agents in Microsoft 365 E5](https://www.microsoft.com/en-us/security/security-copilot-in-microsoft-365-e5) · Blog oficial · Oficial · Microsoft Security · nov 2025. Página oficial con las preguntas frecuentes del beneficio de Security Copilot en Microsoft 365 E5 (capacidad de SCU incluida, calendario de activación y agentes disponibles).
- [Supercharging Security Copilot with Logic Apps: Best practices and pro tips (republicación)](https://serviceautomation.online/supercharging-security-copilot-with-logic-apps-best-practices-and-pro-tips/) · Blog oficial · Empleado de Microsoft · Innocent Wafula · Republicado de Microsoft Security Copilot Blog (Tech Community) · 24 sep 2025. Buenas prácticas para combinar Logic Apps y Security Copilot: elegir casos de uso, invocar skills directas para reducir costo y latencia, limitar llamadas a Copilot y prototipar con payloads simulados antes de producción.
- [Automating Phishing Email Triage with Microsoft Security Copilot](https://techcommunity.microsoft.com/blog/securitycopilotblog/automating-phishing-email-triage-with-microsoft-security-copilot/4416559) · Blog oficial · Empleado de Microsoft · Craig Freyman · Microsoft Tech Community - Microsoft Security Copilot Blog · 22 may 2025. Solución desplegable desde GitHub que combina Logic Apps, Azure Functions y Security Copilot para analizar la intención de correos reportados por usuarios y, opcionalmente, reflejar el análisis en incidentes de Sentinel.
- [Exploring Copilot for Security to Automate Incident Triage](https://techcommunity.microsoft.com/blog/securitycopilotblog/exploring-copilot-for-security-to-automate-incident-triage/4154887) · Blog oficial · Empleado de Microsoft · Legado aún útil · Brandon Dixon · Microsoft Tech Community - Microsoft Security Copilot Blog · 30 may 2024. Muestra cómo replicar el promptbook de triaje de incidentes de Sentinel en un playbook de Logic Apps con el conector de Security Copilot, que clasifica severidad, explica el razonamiento, sugiere etiquetas y comenta el incidente. *Nota:* Escrito cuando se llamaba 'Copilot for Security' (el autor figura hoy como ex-empleado); el patrón (switch sobre la etiqueta del LLM + Update incident) sigue vigente

### Webinars, videos y podcasts

- [Microsoft Security Copilot video hub - Microsoft Adoption](https://adoption.microsoft.com/en-us/security-copilot/video-hub/) · Video · Oficial · Varios (equipos de Microsoft Security) · Microsoft Adoption. Videoteca con demos breves de agentes (Security Alert Triage, Security Analyst, TI Briefing), agentes de partners y escenarios de Logic Apps con Sentinel (enriquecimiento de incidentes, inicios de sesión fallidos, análisis de scripts).
- [When to Use Logic Apps vs. Security Copilot Agents](https://www.youtube.com/watch?v=GMST8t6hF8Y) · Webinar · Empleado de Microsoft · Shiv Patel e Innocent Wafula · Microsoft Security Community (YouTube) · 9 oct 2025. Compara cuándo usar Logic Apps (flujos orquestados deterministas) y cuándo agentes de Security Copilot (respuestas adaptativas con IA), con demos del conector y del agent builder.
- [Logic Apps (Part 10 of 11) - Microsoft Security Copilot Flight School](https://learn.microsoft.com/en-us/shows/microsoft-security-copilot-flight-school/logic-apps) · Video · Empleado de Microsoft · Legado aún útil · Ryan Munsch · Microsoft Learn Shows · 24 oct 2024. Episodio de la serie Flight School que muestra cómo invocar Security Copilot desde Logic Apps con el conector y desplegar muestras del repositorio de GitHub. *Nota:* Serie de 2024 con 11 episodios; los conceptos siguen vigentes pero no cubre agentes ni MCP

### Laboratorios, GitHub y herramientas

- [SecurityCopilot-Sentinel-Incident-Investigation (Logic App)](https://github.com/Azure/Security-Copilot/tree/main/Logic%20Apps/SecurityCopilot-Sentinel-Incident-Investigation) · GitHub · Empleado de Microsoft · Pratik Lal, Innocent Wafula, Stefano Pescosolido · GitHub - Azure/Security-Copilot. Plantilla ARM oficial de playbook que lee las entidades de un incidente de Sentinel, invoca skills de Security Copilot por tipo de entidad, resume el resultado y lo escribe como comentario del incidente (y opcionalmente por correo).
- [Microsoft Security Copilot – Pricing](https://www.microsoft.com/en-us/security/pricing/microsoft-security-copilot/) · Herramienta · Oficial · Microsoft Security. Página oficial de precios de Security Copilot: SCU aprovisionadas (4 USD/SCU-hora, mínimo 1) y SCU de excedente (6 USD/SCU-hora) con límite configurable, más calculadora de capacidad y panel de uso.
- [Security-Copilot/Logic Apps/Readme.md](https://github.com/Azure/Security-Copilot/blob/main/Logic%20Apps/Readme.md) · GitHub · Oficial · Legado aún útil · GitHub - Azure/Security-Copilot. Índice oficial de playbooks de ejemplo con Security Copilot (incidentes de Sentinel, phishing, reportes) y descripción de las acciones del conector, con advertencia explícita sobre el aumento de consumo de SCU. *Nota:* Describe acciones de la primera versión ('Evaluate Prompt'/'Evaluate Direct Skill'); hoy el conector expone 'Submit a Security Copilot prompt/promptbook' y 'Execute a Security Copilot Agent'
- [Security-Copilot/Logic Apps (Azure/Security-Copilot)](https://github.com/Azure/Security-Copilot/tree/main/Logic%20Apps) · GitHub · Oficial · Legado aún útil · Microsoft (equipo Security Copilot) · GitHub - Azure. Colección de Logic Apps de ejemplo con Security Copilot: investigación de incidentes de Sentinel, severidad dinámica, phishing reportado, informes CISO, boletines de amenazas, migrador KQL y traspaso de turno SOC. *Nota:* La mayoría de muestras son de 2024-2025 y usan acciones antiguas (Evaluate Prompt); advierte que las Logic Apps pueden aumentar el consumo de SCU
- [Copilot-Sentinel_investigation-DynamicSev (Logic App)](https://github.com/Azure/Security-Copilot/tree/main/Logic%20Apps/Copilot-Sentinel_investigation-DynamicSev) · GitHub · Empleado de Microsoft · Legado aún útil · Yaniv Shasha · GitHub - Azure/Security-Copilot. Playbook de ejemplo que, con disparador de incidente, pone el incidente en activo, genera etiquetas dinámicas, ajusta la severidad con enriquecimiento de MDTI y documenta el razonamiento como comentario. *Nota:* Último cambio hace ~2 años y usa terminología 'Copilot for Security'; el patrón sigue siendo válido (hoy 'Security Copilot', ejecución desde reglas de automatización)
- [Automation Workshop - Module 1: Leveraging the Microsoft Security Copilot Logic App Connector](https://github.com/Azure/Security-Copilot/blob/main/Technical%20Workshops/Automation%20Workshop/Module%201%20-Leveraging%20the%20Microsoft%20Copilot%20For%20Security%20logic%20app%20Connector/readme.md) · Laboratorio · Oficial · Legado aún útil · GitHub - Azure/Security-Copilot. Laboratorio de 15 minutos (nivel 100) para desplegar una Logic App Consumption con disparador de recurrencia que envía prompts a Security Copilot y revisar el resultado en el portal. *Nota:* Parte de un workshop de automatización con varios módulos; capturas con la nomenclatura antigua 'Copilot for Security'
- [Automation Workshop - Module 2: Using Logic app samples with the Microsoft Security Logic App Connector](https://github.com/Azure/Security-Copilot/tree/main/Technical%20Workshops/Automation%20Workshop/Module%202-%20Using%20Logic%20app%20samples%20with%20the%20Microsoft%20Security%20Logic%20App%20Connector) · Laboratorio · Oficial · Legado aún útil · Microsoft (equipo Security Copilot) · GitHub - Azure. Laboratorio de unos 30 minutos que despliega un boletín de amenazas MDTI por correo y una Logic App de investigación de incidentes de Sentinel con etiquetas, severidad dinámica y comentarios generados por Copilot. *Nota:* Material de 2024; sigue siendo válido como ejercicio, revisar nombres de acciones del conector actual
- [Tutorial: Generate Security Copilot Risky Incident Reports (Get-CfS-Risky-Incidents-Report)](https://github.com/Azure/Security-Copilot/blob/main/Logic%20Apps/Get-CfS-Risky-Incidents-Report/Readme.md) · GitHub · Empleado de Microsoft · Legado aún útil · Microsoft (comunidad Security Copilot) · GitHub - Azure/Security-Copilot. Logic App programada que consulta los incidentes más riesgosos (puntuación de STAT), genera informes con la skill de Incident Report de Security Copilot y los publica en Teams y como comentario/etiqueta del incidente. *Nota:* Usa el nombre antiguo 'Copilot for Security' y menciona 'Unified SOC Preview'; útil como patrón de reporte programado y de consumo controlado de SCU

### Comunidad: blogs, libros, newsletters y eventos

- [Automated incident triage with Security Copilot and Microsoft Sentinel/ Defender XDR](https://jeffreyappel.nl/automated-incident-triage-with-security-copilot-and-microsoft-sentinel-defender-xdr/) · Blog · MVP · Jeffrey Appel · Jeffrey Appel - Microsoft Security blog · 26 mar 2025. Recorrido detallado del despliegue y funcionamiento del playbook oficial que usa Security Copilot para triar incidentes de Sentinel/Defender XDR, con prerrequisitos, skills y resultados en comentarios.
- [Security Copilot Integration with Microsoft Sentinel - Why Automation matters now](https://techcommunity.microsoft.com/discussions/microsoftsentinel/security-copilot-integration-with-microsoft-sentinel---why-automation-matters-no/4507293) · Blog · Comunidad · Marcel Graewer · Microsoft Tech Community - Microsoft Sentinel (discusiones) · 31 mar 2026. Artículo comunitario que propone una arquitectura en capas (detección, enriquecimiento con Logic Apps + Security Copilot, triaje y enrutamiento) con consultas KQL para elegir candidatos de alto volumen.

**Manos a la obra**

1. `Laboratorio parcial` Despliega el ejemplo oficial [SecurityCopilot-Sentinel-Incident-Investigation](https://github.com/Azure/Security-Copilot/blob/main/Logic%20Apps/SecurityCopilot-Sentinel-Incident-Investigation/readme.md) y adjúntalo con una regla de automatización solo a incidentes de severidad alta.
2. `Laboratorio parcial` Modifícalo para usar una Direct Skill y compara el consumo de SCU en el panel de uso.
3. `Laboratorio parcial` Construye un playbook que ejecute un promptbook con parámetros del incidente y publique el resultado en Teams.
4. `Laboratorio parcial` Dispara un agente desde Logic Apps con la acción de ejecución de agentes ([guía](https://learn.microsoft.com/en-us/copilot/security/connector-logicapp-agent-trigger)).

**¿Quieres profundizar?**

- [Automated incident triage with Security Copilot and Microsoft Sentinel/ Defender XDR](https://jeffreyappel.nl/automated-incident-triage-with-security-copilot-and-microsoft-sentinel-defender-xdr/) · Blog
- [Copilot-Sentinel_investigation-DynamicSev (Logic App)](https://github.com/Azure/Security-Copilot/tree/main/Logic%20Apps/Copilot-Sentinel_investigation-DynamicSev) · GitHub
- [Microsoft Security Copilot – Pricing](https://www.microsoft.com/en-us/security/pricing/microsoft-security-copilot/) · Herramienta
- [Microsoft Security Copilot video hub - Microsoft Adoption](https://adoption.microsoft.com/en-us/security-copilot/video-hub/) · Video

<a id="x4"></a>

## X4 · Plugins y promptbooks personalizados

*L400+ · ~6 h · Origen: Nuevo*

Security Copilot es extensible. Los **promptbooks** encadenan prompts en un procedimiento repetible —por ejemplo, el triage de un tipo de incidente o el informe ejecutivo semanal— y se comparten con el equipo. Los **plugins** le dan nuevas habilidades: plugins **KQL** que consultan tus tablas de Sentinel o Defender, plugins de **API** que llaman a servicios internos o de terceros a partir de una especificación OpenAPI, y plugins basados en **instrucciones**.

Aquí aprenderás el formato del manifiesto, buenas prácticas para describir habilidades de modo que el orquestador las elija bien, cómo probar y versionar, y cómo publicar para tu organización, con ejemplos del repositorio oficial de Security Copilot en GitHub.

**Qué vas a lograr**

- Crear un promptbook reutilizable para un procedimiento del SOC.
- Construir un plugin KQL sobre tablas de Sentinel.
- Construir un plugin de API con OpenAPI y gestionar su autenticación.

> **Novedad.** Los plugins KQL admiten como destino Sentinel, el data lake de Sentinel, Log Analytics, Defender y Kusto ([plugins KQL](https://learn.microsoft.com/en-us/copilot/security/plugin-kql)).

> **Novedad.** Security Copilot admite servidores MCP externos como plugins (vista previa): solo herramientas, con lista AllowedTools obligatoria y transporte StreamableHttp recomendado ([plugins MCP](https://learn.microsoft.com/en-us/copilot/security/plugin-mcp)).

> **Consejo Ninja.** La calidad de un plugin depende de sus descripciones: el orquestador elige habilidades leyendo nombre, descripción y parámetros. Escríbelas como si se las explicaras a un analista nuevo y prueba con prompts ambiguos.

**¿Tienes poco tiempo?**

- [Build your own promptbooks](https://learn.microsoft.com/en-us/copilot/security/build-promptbooks) · Documentación
- [KQL plugins in Microsoft Security Copilot](https://learn.microsoft.com/en-us/copilot/security/plugin-kql) · Documentación
- [Model Context Protocol (MCP) plugins in Microsoft Security Copilot (Preview)](https://learn.microsoft.com/en-us/copilot/security/plugin-mcp) · Documentación

### Documentación, cursos y credenciales

- [Build your own promptbooks](https://learn.microsoft.com/en-us/copilot/security/build-promptbooks) · Documentación · Oficial · Microsoft Learn. Crear promptbooks desde una sesión existente, parametrizar entradas con <Parametro>, activar continuar en caso de fallo, invocar capacidades del sistema directamente (preview), compartir, duplicar y ejecutar.
- [Create your own custom plugins](https://learn.microsoft.com/en-us/copilot/security/custom-plugins) · Documentación · Oficial · Microsoft Learn. Requisitos del manifiesto YAML/JSON (Descriptor y SkillGroups), mapeo entre manifiestos OpenAI y Security Copilot (solo OpenAPI 3.0/3.0.1) y buenas prácticas para evitar colisiones de skills.
- [KQL plugins in Microsoft Security Copilot](https://learn.microsoft.com/en-us/copilot/security/plugin-kql) · Documentación · Oficial · Microsoft Learn · 30 sep 2025. Referencia de skills KQL con targets Defender, Sentinel, SentinelDataLake, LogAnalytics y Kusto, plantillas de hasta 80.000 caracteres y ejemplos de manifiesto para Sentinel y el data lake.
- [Model Context Protocol (MCP) plugins in Microsoft Security Copilot (Preview)](https://learn.microsoft.com/en-us/copilot/security/plugin-mcp) · Documentación · Oficial · Vista previa · Microsoft Learn. Cómo conectar un servidor MCP existente como plugin (Format: MCP) con Endpoint, StreamableHttp, autenticación OAuth o AADDelegated y lista AllowedTools, para usar sus herramientas en prompts, promptbooks, Logic Apps y agentes. *Nota:* Solo soporta herramientas MCP (no recursos ni prompts) y no redescubre cambios automáticamente; SSE será deprecado frente a StreamableHttp

### Anuncios y blogs oficiales

- [Using parameterized functions with KQL-based custom plugins in Microsoft Security Copilot](https://techcommunity.microsoft.com/blog/securitycopilotblog/using-parameterized-functions-with-kql-based-custom-plugins-in-microsoft-securit/4419286) · Blog oficial · Empleado de Microsoft · Innocent Wafula · Microsoft Tech Community - Security Copilot Blog · 2 jun 2025. Cómo encapsular consultas KQL largas en funciones parametrizadas de Log Analytics para que el plugin KQL de Security Copilot quede en una línea, sea reutilizable y más fácil de mantener.

### Laboratorios, GitHub y herramientas

- [Experience Security Copilot through guided simulations](https://learn.microsoft.com/en-us/training/modules/security-copilot-interactive-guides/) · Laboratorio · Oficial · Microsoft Learn Training. Módulo con simulaciones interactivas: configuración de owner, prompts y promptbooks, creación de un promptbook personalizado, investigación en Defender XDR y Purview, creación de un agente y el agente de optimización de acceso condicional.
- [Azure/Security-Copilot (Microsoft Security Copilot Community repository)](https://github.com/Azure/Security-Copilot) · GitHub · Oficial · Legado aún útil · Microsoft (equipo Security Copilot) y comunidad · GitHub - Azure. Repositorio oficial con plugins de ejemplo (API, GPT, KQL), muestras de promptbooks, prompts, Logic Apps, monitorización y talleres técnicos. *Nota:* Última actividad hace meses y referencias al antiguo nombre Copilot for Security; para agentes y MCP usar la documentación de Learn más reciente
- [Security-Copilot/Technical Workshops/Custom Plugin Workshop](https://github.com/Azure/Security-Copilot/tree/main/Technical%20Workshops/Custom%20Plugin%20Workshop) · Laboratorio · Oficial · Legado aún útil · Microsoft (equipo Security Copilot) · GitHub - Azure. Taller práctico de plugins personalizados en cinco módulos: plugin de Logic App, plugins GPT, plugin API (GeoIP) y plugin KQL. *Nota:* Escrito con el nombre Copilot for Security; los formatos de manifiesto siguen vigentes
- [Security-Copilot-mssp](https://github.com/hesaad/Security-Copilot-mssp) · GitHub · Empleado de Microsoft · Legado aún útil · Hesham Saad · GitHub. Repositorio con plugins personalizados de Security Copilot pensados para escenarios de MSSP. *Nota:* Última actividad visible del autor ~2024; sirve también a A9

### Comunidad: blogs, libros, newsletters y eventos

- [The KQL Grimoire - PART 1](https://pe.linkedin.com/pulse/slims-elite-kql-detection-cyber-defense-tips-steven-lim-wujbc/) · Blog · MVP · Legado aún útil · Steven Lim · LinkedIn · 24 mar 2024. Compilación de consultas KQL de hunting para Sentinel y Defender XDR que incluye casos como caza de plugins maliciosos de Copilot, restricción de plugins y análisis KQL con Copilot. *Nota:* Actualizado en feb-2025; útil como banco de consultas para convertir en plugins KQL o herramientas MCP personalizadas

**Manos a la obra**

1. `Laboratorio parcial` Crea un plugin KQL con tres habilidades sobre tablas de Sentinel (por ejemplo, fallos de inicio de sesión de un usuario, dispositivos con un indicador y cambios recientes en reglas) ([plugins KQL](https://learn.microsoft.com/en-us/copilot/security/plugin-kql)).
2. `Laboratorio parcial` Diseña un promptbook de triage de phishing con cinco prompts y parámetros de entrada, y compártelo con el equipo.
3. `Laboratorio parcial` Construye un plugin de API sobre un servicio de inteligencia con su especificación OpenAPI y versiona los manifiestos en Git.

**¿Quieres profundizar?**

- [Experience Security Copilot through guided simulations](https://learn.microsoft.com/en-us/training/modules/security-copilot-interactive-guides/) · Laboratorio
- [Azure/Security-Copilot (Microsoft Security Copilot Community repository)](https://github.com/Azure/Security-Copilot) · GitHub
- [Security-Copilot/Technical Workshops/Custom Plugin Workshop](https://github.com/Azure/Security-Copilot/tree/main/Technical%20Workshops/Custom%20Plugin%20Workshop) · Laboratorio

<a id="x5"></a>

## X5 · Agentes de Security Copilot

*L400+ · ~8 h · Origen: Nuevo*

Los **agentes** llevan la IA de la asistencia a la autonomía supervisada: trabajan en segundo plano sobre tareas repetitivas y de alto volumen —clasificar reportes de phishing, priorizar alertas, optimizar políticas de acceso condicional, preparar informes de inteligencia, priorizar vulnerabilidades—, aprenden de la retroalimentación del analista y muestran su razonamiento para que puedas auditarlo.

Microsoft y sus partners publican agentes listos para usar, y puedes construir los tuyos con el **creador de agentes** sin código o con un manifiesto para desarrolladores que combina instrucciones, habilidades y herramientas. Este módulo cubre los agentes disponibles, su configuración, identidad y permisos, la supervisión de su trabajo, sus costos y el gobierno de un parque creciente de agentes.

**Qué vas a lograr**

- Habilitar, configurar y supervisar un agente de Microsoft en el SOC.
- Construir un agente personalizado y definir sus herramientas y permisos.
- Gobernar identidad, acceso, costos y calidad de los agentes.

> **Novedad.** Estado a noviembre de 2026 en SecOps: el **Security Alert Triage Agent** (antes Phishing Triage Agent) es GA para alertas de correo y está en vista previa para nube e identidad ([Alert Triage Agent](https://learn.microsoft.com/en-us/defender-xdr/security-alert-triage-agent)); el **Security Analyst Agent** (vista previa desde abril de 2026) analiza datos de Defender XDR, Log Analytics de Sentinel o el data lake ([Security Analyst Agent](https://learn.microsoft.com/en-us/defender-xdr/security-analyst-agent)); el **Dynamic Threat Detection Agent** es gratuito durante su vista previa ([Dynamic Threat Detection](https://learn.microsoft.com/en-us/defender-xdr/dynamic-threat-detection-agent)). Panorama completo en [agentes de Defender](https://learn.microsoft.com/en-us/defender-xdr/security-copilot-agents-defender).

> **Novedad.** Project Perception, anunciado el 27 de julio de 2026, organiza equipos de agentes (reconocimiento, triage, inteligencia, investigación, creación de detecciones y priorización de postura) con aprobaciones humanas; Microsoft lo presenta como el sistema que actúa, mientras Security Copilot es la interfaz que asiste ([anuncio](https://blogs.microsoft.com/blog/2026/07/27/rethinking-security-for-the-age-of-ai/)). Su disponibilidad varía según la fuente: confirma el estado antes de recomendarlo.

> **Consejo Ninja.** Agentes personalizados: creador sin código, NL2Agent, YAML o creación vía MCP; todo converge en un manifiesto YAML. Crear y publicar no consume SCU, probar sí ([costos de desarrollo](https://learn.microsoft.com/en-us/copilot/security/developer/cost-considerations), [agentes personalizados](https://learn.microsoft.com/en-us/copilot/security/developer/custom-agent-overview)).

> **Consejo Ninja.** Gobierno: Microsoft Entra Agent ID está disponible en general y los agentes de Security Copilot reciben identidad de agente; define sponsor de negocio y owner técnico para cada uno ([Agent ID](https://techcommunity.microsoft.com/blog/microsoft-entra-blog/build-ai-agents-for-production-with-secure-identities-from-day-one/4524606)). En Defender, la tabla AgentsInfo inventaría agentes ([inventario de agentes](https://learn.microsoft.com/en-us/defender-xdr/security-for-ai/ai-agent-inventory)).

> **Atención.** Microsoft Ignite se realiza del 17 al 20 de noviembre de 2026: varios estados de vista previa pueden cambiar en días. Revisa las [novedades de Security Copilot](https://learn.microsoft.com/en-us/copilot/security/whats-new-copilot-security) antes de cada recomendación.

**¿Tienes poco tiempo?**

- [Deploy AI agents in Microsoft Defender](https://learn.microsoft.com/en-us/defender-xdr/security-copilot-agents-defender) · Documentación
- [Microsoft Security Copilot agents overview](https://learn.microsoft.com/en-us/copilot/security/agents-overview) · Documentación
- [Agents That Actually Work: From an MVP](https://www.youtube.com/watch?v=1KsM2k2dP7U) · Webinar

### Documentación, cursos y credenciales

- [Deploy AI agents in Microsoft Defender](https://learn.microsoft.com/en-us/defender-xdr/security-copilot-agents-defender) · Documentación · Oficial · Microsoft Learn. Cómo descubrir, comprar y desplegar agentes desde el Security Store en el portal de Defender y ficha de los agentes de Microsoft disponibles: Security Alert Triage, Threat Intelligence Briefing, Threat Hunting, Security Analyst y Dynamic Threat Detection.
- [Microsoft Security Copilot Phishing Triage Agent in Microsoft Defender](https://learn.microsoft.com/en-us/defender-xdr/phishing-triage-agent) · Documentación · Oficial · Microsoft Learn. Documentación del agente que clasifica correos reportados por usuarios como phishing o falso positivo, con razonamiento transparente, aprendizaje por feedback y prerrequisitos (MDO P2, URBAC, política de alerta de correo reportado).
- [Microsoft Security Copilot - Developer content](https://learn.microsoft.com/en-us/copilot/security/developer/) · Documentación · Oficial · Microsoft Learn. Índice del contenido para desarrolladores: planificación, componentes, consideraciones de coste, manifiesto YAML y changelog, construcción de agentes (NL, formulario, YAML, MCP, interactivos), plugins (API, GPT, KQL, MCP, Logic Apps), pruebas y publicación.
- [Microsoft Security Copilot agents overview](https://learn.microsoft.com/en-us/copilot/security/agents-overview) · Documentación · Oficial · Microsoft Learn · 18 mar 2026. Define la terminología de agentes (disparador, permisos, identidad con Entra Agent ID o cuenta de usuario, plugins) y aclara que los agentes consumen SCU como el resto del producto.
- [What is Perception?](https://learn.microsoft.com/en-us/security/agentic-security/agentic-security-overview) · Documentación · Oficial · Vista previa · Nuevo · Microsoft Learn · 30 oct 2026. Visión general de Perception: playbooks que coordinan agentes especializados, chat para iniciar sesiones, aprobaciones humanas y navegación en el portal de Defender (New Chat, Sessions, Agents, Playbooks, Insights). *Nota:* La documentación indica Limited Public Preview por invitación
- [Triage Agent (Project Perception)](https://learn.microsoft.com/en-us/security/agentic-security/triage-agent) · Documentación · Oficial · Vista previa · Nuevo · Microsoft Learn · 18 ago 2026. Agente de triage de Perception para alertas de correo, nube/contenedores, identidad, endpoint y cloud apps, con identidad Entra Agent ID, permisos mínimos por tipo de alerta, aprendizaje por feedback y métricas de rendimiento. *Nota:* Al configurarlo reemplaza al Phishing Triage Agent conservando historial; solo puede haber un agente de triage activo
- [Microsoft Security Copilot agent development overview](https://learn.microsoft.com/en-us/copilot/security/developer/custom-agent-overview) · Documentación · Oficial · Vista previa · Microsoft Learn. Visión general del desarrollo de agentes personalizados: herramientas (skills), disparadores, orquestadores, instrucciones y memoria; tres vías en standalone (NL2Agent, agent builder, subir YAML) y creación vía herramientas MCP. *Nota:* Todas las vías convergen en un manifiesto YAML publicable en Security Copilot o en el Security Store para partners
- [Microsoft Security Copilot Security Alert Triage Agent in Microsoft Defender (Preview)](https://learn.microsoft.com/en-us/defender-xdr/security-alert-triage-agent) · Documentación · Oficial · Vista previa · Microsoft Learn. Describe la evolución del agente de triage de phishing hacia alertas de correo (GA), nube/contenedores e identidad (preview), con licencias y permisos por tipo de alerta. *Nota:* Requiere URBAC activado; el aprendizaje por feedback solo aplica a alertas de correo y colaboración
- [Microsoft Security Copilot Security Analyst Agent overview](https://learn.microsoft.com/en-us/defender-xdr/security-analyst-agent) · Documentación · Oficial · Vista previa · Microsoft Learn. Agente que realiza análisis multi-paso con Python sobre datos de Defender XDR, Sentinel Log Analytics o el data lake de Sentinel, y entrega hallazgos priorizados con evidencias, visualizaciones y artefactos (incluye las consultas KQL usadas). *Nota:* Se activa en Advanced hunting cambiando del Threat Hunting Assistant al Security Analyst Agent; para el data lake hay que configurar el origen de datos
- [Build an agent from scratch using the agent builder](https://learn.microsoft.com/en-us/copilot/security/developer/create-agent-dev) · Documentación · Oficial · Vista previa · Microsoft Learn. Uso del formulario del agent builder (pestañas Build y Test) para definir detalles, instrucciones, entradas, herramientas (AGENT, GPT, KQL, API, MCP y del catálogo, p. ej. MCP.Sentinel) y automatización con disparadores y permisos. *Nota:* Incluye un chat de Copilot que ayuda a rellenar la definición del agente
- [Key concepts in Perception](https://learn.microsoft.com/en-us/security/agentic-security/agentic-security-concepts) · Documentación · Oficial · Vista previa · Microsoft Learn. Define sesiones, agentes y playbooks y lista los agentes de Perception (Recon, Triage, Threat Intelligence, Attack Investigation, Detection Authoring, Posture Prioritization) y playbooks como Protect against a threat o Investigate attack. *Nota:* Los playbooks son predefinidos por Microsoft y no se pueden crear personalizados en esta versión
- [Microsoft Security Copilot Dynamic Threat Detection Agent](https://learn.microsoft.com/en-us/defender-xdr/dynamic-threat-detection-agent) · Documentación · Oficial · Vista previa · Microsoft Learn · 23 feb 2026. Agente siempre activo en el backend de Defender que busca falsos negativos correlacionando alertas, eventos, anomalías y TI de Defender y Sentinel, y genera alertas dinámicas con explicación y mapeo MITRE ATT&CK. *Nota:* Gratuito durante la preview pública; empezará a consumir SCU cuando sea GA. Aplica a Sentinel en el portal de Defender
- [Cost considerations for Security Copilot](https://learn.microsoft.com/en-us/copilot/security/developer/cost-considerations) · Documentación · Oficial · Vista previa · Microsoft Learn · 30 sep 2025. Aclara cuándo se consumen SCU al construir agentes: crear con NL2Agent, agent builder o vía MCP y publicar no consume; probar agentes siempre consume. *Nota:* La versión en español figura actualizada el 14-abr-2026
- [Application card for Microsoft Security Copilot agents](https://learn.microsoft.com/en-us/copilot/security/security-copilot-application-card-agents) · Documentación · Oficial · Microsoft Learn. Ficha de IA responsable de los agentes: usos previstos, limitaciones, mitigaciones, manifiesto YAML, autonomía acotada y certificación ISO 42001 de Security Copilot.
- [What is Microsoft Security Store?](https://learn.microsoft.com/en-us/security/store/what-is-security-store) · Documentación · Oficial · Microsoft Learn. Explica el Security Store como tienda optimizada para seguridad donde descubrir, comprar (incluso con MACC) y desplegar agentes, SaaS y servicios de Microsoft y partners integrados con Defender, Sentinel, Entra, Purview, Intune y Security Copilot.
- [Certification in Microsoft Security Store](https://learn.microsoft.com/en-us/security/store/partners/security-store-certification) · Documentación · Oficial · Microsoft Learn. Requisitos de certificación: los agentes deben generar planes multi-paso (se rechazan los simples envoltorios de LLM), cumplir IA responsable, describir entradas, tareas y salidas e indicar el consumo estimado de SCU.
- [Microsoft Security Copilot agents](https://learn.microsoft.com/en-us/copilot/security/agents-security-copilot) · Documentación · Oficial · Microsoft Learn · 18 mar 2026. Catálogo de agentes en la experiencia standalone (p. ej. Threat Intelligence Briefing Agent, requiere Defender EASM) y enlaces a los agentes embebidos en Entra, Defender, Intune, Purview y Sentinel.
- [Agent categories in Project Perception](https://learn.microsoft.com/en-us/security/agentic-security/agentic-security-agent-categories) · Documentación · Oficial · Vista previa · Nuevo · Microsoft Learn · 29 oct 2026. Explica los equipos de agentes red (exponer brechas), blue (detectar, triar, investigar, crear detecciones) y green (priorizar y endurecer postura) y cómo colaboran con aprobación humana en acciones de alto impacto.
- [Project Perception | Microsoft Security](https://www.microsoft.com/en-us/security/business/ai-powered-cybersecurity/project-perception-agentic-system) · Documentación · Oficial · Vista previa · Nuevo · Microsoft Security · jul 2026. Página de producto con FAQ: Perception llega primero al portal de Defender, se factura por consumo en SCU según la intensidad de cada agente y trabaja junto a Security Copilot.
- [Attack Investigation Agent](https://learn.microsoft.com/en-us/security/agentic-security/attack-investigation-agent) · Documentación · Oficial · Vista previa · Microsoft Learn. Investigador autónomo de nivel 2 que reconstruye la historia completa de un ataque desde una alerta o incidente de Defender, con veredicto, línea de tiempo, técnicas, IoC y chat interactivo. *Nota:* Requiere Microsoft 365 E5, Defender XDR y onboarding al data lake y a la experiencia unificada
- [Application card for Perception](https://learn.microsoft.com/en-us/security/agentic-security/agentic-security-application-card) · Documentación · Oficial · Vista previa · Microsoft Learn. Ficha de IA responsable de Perception: usos previstos, identidad de agente con Entra Agent ID, sesiones inmutables como pista de auditoría, supervisión humana, privacidad y limitaciones. *Nota:* Clave para la sección de gobierno de agentes autónomos
- [Build Security Copilot agents in standalone](https://learn.microsoft.com/en-us/copilot/security/developer/agent-standalone-overview) · Documentación · Oficial · Vista previa · Microsoft Learn · 12 ene 2026. Resume las tres vías para crear agentes en el portal standalone (NL2Agent, agent builder y subir manifiesto YAML) y remite a la guía de planificación y al esquema del manifiesto.
- [Microsoft Security Store in Microsoft Security Copilot](https://learn.microsoft.com/en-us/copilot/security/security-store-integration) · Documentación · Oficial · Vista previa · Microsoft Learn · 30 sep 2025. Cómo descubrir y obtener agentes desde el Security Store integrado en el portal standalone y configurarlos después en Active agents. *Nota:* Las suscripciones del Store se facturan aparte y el uso del agente consume SCU de forma independiente; eliminar el agente no cancela la suscripción
- [Plan your publication for Security Store](https://learn.microsoft.com/en-us/security/store/partners/plan-your-publication-for-security-store) · Documentación · Oficial · Microsoft Learn. Guía para ISV y MSSP sobre cómo publicar agentes de Security Copilot, SaaS integradas y notebook jobs del data lake de Sentinel en el Security Store vía Partner Center, con estructura de oferta, plan y paquete (manifiesto YAML).
- [Discover agents in Microsoft Security Copilot](https://learn.microsoft.com/en-us/copilot/security/discover-agents) · Documentación · Oficial · Microsoft Learn · 18 mar 2026. Cómo descubrir agentes de Microsoft y de partners desde la biblioteca de agentes standalone, las experiencias embebidas y el Security Store integrado.

### Anuncios y blogs oficiales

- [Build AI agents for production with secure identities from day one](https://techcommunity.microsoft.com/blog/microsoft-entra-blog/build-ai-agents-for-production-with-secure-identities-from-day-one/4524606) · Blog oficial · Empleado de Microsoft · Nuevo · ArLucaID · Microsoft Tech Community - Microsoft Entra Blog · 2 jun 2026. Explica Microsoft Entra Agent ID (ya GA): blueprints, identidad por instancia con logs de inicio de sesión y Acceso Condicional, sponsors y owners, y cómo los agentes de Security Copilot reciben Agent ID automáticamente.
- [Rethinking security for the age of AI](https://blogs.microsoft.com/blog/2026/07/27/rethinking-security-for-the-age-of-ai/) · Blog oficial · Empleado de Microsoft · Vista previa · Nuevo · Hayete Gallot · The Official Microsoft Blog · 27 jul 2026. Presenta Project Perception, un sistema de seguridad agéntico con agentes red, blue y green, arquitectura multimodelo y el modelo propio MAI-Cyber-1-Flash, con preview pública a partir del 3 de agosto de 2026. *Nota:* Hito mayor de 2026: Microsoft distingue Perception (IA que actúa) de Security Copilot (IA que asiste, interfaz de chat)
- [Agents are your newest insiders. Security must move at their speed.](https://www.microsoft.com/en-us/security/blog/2026/10/19/agents-are-your-newest-insiders-security-must-move-at-their-speed/) · Blog oficial · Empleado de Microsoft · Nuevo · Nadim Abdo · Microsoft Security Blog · 19 oct 2026. Extiende Perception a la protección de agentes como insiders con Guardian Agents, registro unificado compartido con Agent 365, identidad responsable con Entra Agent ID y contención continua de permisos.
- [What's new in Microsoft Security: July 2026](https://www.microsoft.com/en-us/security/blog/2026/07/30/whats-new-in-microsoft-security-july-2026/) · Blog oficial · Empleado de Microsoft · Nuevo · Alym Rayani · Microsoft Security Blog · 30 jul 2026. Resumen mensual con el anuncio de Project Perception, protección contra prompt injection en correo, protección de agentes cloud en Agent 365 y un Threat Intelligence Agent mejorado.
- [Secure agentic AI end-to-end](https://www.microsoft.com/en-us/security/blog/2026/03/20/secure-agentic-ai-end-to-end/) · Blog oficial · Empleado de Microsoft · Vasu Jakkal · Microsoft Security Blog · 20 mar 2026. Anuncios de RSAC 2026: Agent 365 GA el 1 de mayo de 2026 (incluido en Microsoft 365 E7), Security Dashboard for AI GA y nuevas capacidades para proteger agentes y defender con agentes.
- [Microsoft Ignite: Ambient and autonomous security for the agentic era](https://www.microsoft.com/en-us/security/blog/2025/11/18/ambient-and-autonomous-security-for-the-agentic-era/) · Blog oficial · Empleado de Microsoft · Vasu Jakkal · Microsoft Security Blog · 18 nov 2025. Visión de Microsoft Security en Ignite 2025: Agent 365 como plano de control de agentes, Entra Agent ID, agentes de Security Copilot y Sentinel como plataforma agéntica.
- [Microsoft Ignite 2025: Transforming Phishing Response with Agentic Innovation](https://techcommunity.microsoft.com/blog/MicrosoftDefenderforOffice365Blog/microsoft-ignite-2025-transforming-phishing-response-with-agentic-innovation/4470791) · Blog oficial · Empleado de Microsoft · Jeffrey Pinkston · Microsoft Tech Community - Defender for Office 365 Blog · 18 nov 2025. Anuncia la disponibilidad general del Security Alert Triage Agent (antes Phishing Triage Agent) y su extensión prevista a alertas de identidad y nube, con métricas de mejora de precisión.
- [Microsoft unveils Microsoft Security Copilot agents and new protections for AI](https://www.microsoft.com/en-us/security/blog/2025/03/24/microsoft-unveils-microsoft-security-copilot-agents-and-new-protections-for-ai/) · Blog oficial · Empleado de Microsoft · Legado aún útil · Vasu Jakkal · Microsoft Security Blog · 24 mar 2025. Anuncio original de los seis primeros agentes de Microsoft (Phishing Triage, Purview Alert Triage, Conditional Access Optimization, Vulnerability Remediation, Threat Intelligence Briefing) y cinco de partners. *Nota:* Histórico: el Phishing Triage Agent pasó a llamarse Security Alert Triage Agent (GA para correo en nov-2025) y el portafolio creció con Ignite 2025 y RSAC 2026

### Webinars, videos y podcasts

- [Agents That Actually Work: From an MVP](https://www.youtube.com/watch?v=1KsM2k2dP7U) · Webinar · MVP · Ugur Koc · Microsoft Security Community (YouTube) · 19 feb 2026. Flujo real para construir agentes fiables en Security Copilot comparando tres métodos (lenguaje natural, agent builder y manifiesto YAML), con técnicas de prueba, validación y diagnóstico de deriva.
- [Building Custom Agents: Unlocking Context, Automation, and Scale](https://www.youtube.com/watch?v=vPcLa1xy_74) · Webinar · Empleado de Microsoft · Innocent Wafula y Sean Wesonga · Microsoft Security Community (YouTube) · 22 ene 2026. Sesión práctica sobre el agent builder de Security Copilot y los servidores MCP para crear agentes personalizados con contexto propio de la organización.
- [Brewing KQL: AI Agents, Security Copilot & MCP with Mona Ghadiri](https://www.youtube.com/watch?v=53nwOQ9qid8) · Video · MVP · Gianni Castaldi y Alex Verboon con Mona Ghadiri · YouTube - KQL Cafe · 15 dic 2025. Sesión de KQL Cafe sobre agentes de IA en el SOC, detection-as-code, parametrización con KQL, costes de Security Copilot (SCU y beneficio E5) y una arquitectura de referencia de riesgos de IA generativa.
- [Microsoft Security Copilot agents (Microsoft Mechanics)](https://www.youtube.com/watch?v=al9OSFGqd8I) · Video · Empleado de Microsoft · Legado aún útil · Dilip Radhakrishnan · Microsoft Mechanics (YouTube). Vídeo de unos 8 minutos con demos del Phishing Triage Agent, agentes de triage de Purview, revisión de accesos, optimización de acceso condicional, remediación de vulnerabilidades y creación de agentes propios. *Nota:* Usa nombres de 2025 (Phishing Triage Agent hoy forma parte del Security Alert Triage Agent y de Perception)
- [Own your security posture I Build custom agents with Security Copilot](https://www.youtube.com/watch?v=8YFhbQb_a00) · Video · Empleado de Microsoft · Dilip Radhakrishnan · Microsoft Security (YouTube). Demo de creación y despliegue de agentes personalizados sin código, optimización con AutoTune y despliegue desde el Security Store.
- [Microsoft Entra AI: Unlocking Identity Intelligence with Security Copilot and Agents](https://www.youtube.com/watch?v=05U4QdMQykk) · Webinar · Empleado de Microsoft · Mamta Kumar y Margaret Garcia Fani · Microsoft Security Community (YouTube) · 13 nov 2025. Security Copilot en Entra: acciones de escritura, promptbooks, calculadora de SCU y agentes de identidad como el de optimización de acceso condicional y revisiones de acceso.
- [What's new in Copilot in Microsoft Purview](https://www.youtube.com/watch?v=Rfx_4nMko1o) · Webinar · Empleado de Microsoft · Patrick David y Sarahzin Shane · Microsoft Security Community (YouTube) · 16 oct 2025. Novedades de Copilot en Purview, DSPM y los agentes de triage de alertas de DLP e Insider Risk Management.

### Laboratorios, GitHub y herramientas

- [AI Agents Monitoring Workbook V2](https://github.com/davidalonsod/Dalonso-Security-Repo/tree/main/Workbooks/AI-Agents-Monitoring/V2) · GitHub · Comunidad · Nuevo · David Alonso Domínguez · GitHub · oct 2026. Workbook de Sentinel (20 pestañas, 254 consultas) que unifica la telemetría de agentes de IA: M365 Copilot, Copilot Studio, Foundry, OpenAI, APIM AI Gateway, inventario de Defender y agentes locales con MCP.
- [Agent Identities (AzureAD-Attack-Defense playbook)](https://github.com/Cloud-Architekt/AzureAD-Attack-Defense/blob/main/AgentIdentities.md) · GitHub · MVP · Nuevo · Thomas Naunheim, Sami Lamppu y Robbe Van Den Daele · GitHub - Cloud-Architekt · sep 2026. Playbook de ataque y defensa sobre Microsoft Entra Agent ID: modelo de blueprints e identidades de agente, escenarios de abuso (propiedad, permisos, consentimientos), detecciones con Defender XDR y Sentinel (incluido el conector de Agent 365) y mitigaciones.
- [Develop a Security Copilot agent platform solution](https://learn.microsoft.com/en-us/azure/sentinel/isv/build-agent-security-copilot) · Laboratorio · Oficial · Microsoft Learn. Tutorial de la serie ISV que construye el agente ficticio IdentityDrift Investigation Agent sobre tablas del data lake de Sentinel: crear capacidad SCU y workspace, definir instrucciones con consultas KQL y probar el agente.

### Comunidad: blogs, libros, newsletters y eventos

- [Hunting AI Agent Configuration Drift with Microsoft Sentinel](https://techcommunity.microsoft.com/discussions/microsoftsentinel/hunting-ai-agent-configuration-drift-with-microsoft-sentinel/4538962) · Blog · Comunidad · Nuevo · Marcel Graewer · Microsoft Tech Community - Microsoft Sentinel · 20 jul 2026. Cuatro consultas de hunting aportadas al repositorio Azure-Sentinel que usan la tabla AgentsInfo para detectar cambios de instrucciones, nuevos servidores MCP, nuevos propietarios y compartición a toda la organización en agentes de IA.
- [Sami Lamppu (blog)](https://samilamppu.com/) · Blog · MVP · Sami Lamppu · samilamppu.com · sep 2025. Blog con análisis profundos de Defender XDR, Sentinel y agentes de Security Copilot (p. ej., Threat Intelligence Briefing Agent).
- [Microsoft Sentinel in September 2026: Data Lake, Fabric, and Incident Cases](https://learn.cloudpartner.fi/posts/microsoft-sentinel-september-2026-data-lake-soc-project-perception) · Blog · Comunidad · Nuevo · Harri Jaakkonen · Cloudpartner · 25 sep 2026. Análisis de cómo el data lake integrado, Fabric e Incident Cases cambian el modelo operativo del SOC y qué implican para la adopción de Project Perception.
- [Introducing Project Perception (Microsoft News - July 2026 security news)](https://news.microsoft.com/july-2026-security-news/) · Evento · Oficial · Nuevo · Microsoft News · 27 jul 2026. Kit de prensa del evento de lanzamiento de Project Perception en San Francisco con vídeos (incluido el caso de Nationwide) y el anuncio del modelo MAI-Cyber-1-Flash.
- [Configure AI agent runtime protection (preview) with Microsoft Defender for Endpoint](https://jeffreyappel.nl/configure-ai-agent-runtime-protection-preview-with-microsoft-defender-for-endpoint/) · Blog · MVP · Vista previa · Nuevo · Jeffrey Appel · jeffreyappel.nl · 22 jun 2026. Configuración de la protección en tiempo de ejecución de agentes de IA locales en MDE mediante hooks (prompt, antes y después de la herramienta) e inspección de red contra prompt injection. *Nota:* Complementa el gobierno de agentes: proteger agentes además de usarlos

**Manos a la obra**

1. `Solo producción` Habilita el Security Alert Triage Agent para alertas de correo en el laboratorio, revisa sus decisiones y dale retroalimentación en lenguaje natural.
2. `Laboratorio parcial` Ejecuta el Threat Intelligence Briefing Agent y compara su informe con tu proceso actual de inteligencia.
3. `Laboratorio parcial` Construye un agente propio para triage de inicios de sesión sospechosos con herramientas MCP de Sentinel y tu plugin KQL; define instrucciones, herramientas y permisos, y pruébalo (consume SCU).
4. `Laboratorio` Escribe la ficha de gobierno del agente: identidad, sponsor, owner, permisos, tope de costo y frecuencia de revisión.

**¿Quieres profundizar?**

- [Agent Identities (AzureAD-Attack-Defense playbook)](https://github.com/Cloud-Architekt/AzureAD-Attack-Defense/blob/main/AgentIdentities.md) · GitHub
- [Building Custom Agents: Unlocking Context, Automation, and Scale](https://www.youtube.com/watch?v=vPcLa1xy_74) · Webinar
- [Brewing KQL: AI Agents, Security Copilot & MCP with Mona Ghadiri](https://www.youtube.com/watch?v=53nwOQ9qid8) · Video
- [Sami Lamppu (blog)](https://samilamppu.com/) · Blog

<a id="x6"></a>

## X6 · Servidor MCP de Sentinel y la plataforma agéntica

*L400+ · ~6 h · Origen: Nuevo*

El **Model Context Protocol (MCP)** es el estándar abierto con el que los agentes de IA descubren y usan herramientas. El **servidor MCP de Microsoft Sentinel** expone colecciones de herramientas —exploración de datos del data lake, triage de incidentes, creación de agentes y otras— para que clientes como Visual Studio Code con GitHub Copilot, Copilot Studio o Microsoft Foundry trabajen con tus datos de seguridad en lenguaje natural, respetando los permisos del usuario.

Junto con el data lake y el graph, el servidor MCP convierte a Sentinel en una **plataforma para construir y ejecutar agentes de seguridad**. Este módulo cubre la conexión desde distintos clientes, las herramientas disponibles, la creación de herramientas personalizadas a partir de consultas KQL y las consideraciones de seguridad propias de exponer datos sensibles a agentes.

**Qué vas a lograr**

- Conectar Visual Studio Code y otros clientes al servidor MCP de Sentinel.
- Explorar el data lake y gestionar incidentes en lenguaje natural mediante herramientas MCP.
- Crear una herramienta MCP personalizada a partir de una consulta KQL.
- Aplicar controles de seguridad al uso de agentes con datos del SOC.

> **Novedad.** El servidor MCP de Sentinel llegó a disponibilidad general el 18 de noviembre de 2025, tras su vista previa del 30 de septiembre ([anuncio de GA](https://techcommunity.microsoft.com/blog/microsoft-security-blog/microsoft-sentinel-mcp-server---generally-available-with-exciting-new-capabiliti/4470125)). Sus colecciones son exploración de datos, triage y creación de agentes de Security Copilot, además de herramientas personalizadas a partir de consultas KQL ([herramientas MCP](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-mcp-tools-overview)).

> **Consejo Ninja.** Triage expone listar y obtener incidentes y alertas, consultar el esquema y ejecutar consultas de búsqueda avanzada, siempre con los permisos del usuario ([triage](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-mcp-triage-tool)). Para crear una herramienta personalizada con «Save as tool» necesitas Security Operator o superior; para usarla, Security Reader ([herramientas personalizadas](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-mcp-create-custom-tool)).

> **Novedad.** Clientes compatibles: Security Copilot, Visual Studio Code con GitHub Copilot, Copilot Studio y Microsoft Foundry de forma nativa; en RSAC 2026 se sumaron un conector para Claude y una colección de grafo en vista previa, y el entity analyzer pasó a GA con facturación en SCU ([novedades RSAC 2026](https://techcommunity.microsoft.com/blog/microsoftsentinelblog/what%E2%80%99s-new-in-microsoft-sentinel-rsac-2026/4503971)).

> **Atención.** Tras el onboarding integrado del 23 de septiembre de 2026, Microsoft orienta a usar la colección de triage para consultar datos, y un experto de la comunidad reportó que la exploración de datos no respondía en tenants nuevos: pruébalo en tu tenant antes de comprometer un diseño ([novedades](https://learn.microsoft.com/en-us/azure/sentinel/whats-new)).

> **Consejo Ninja.** Exponer datos del SOC a agentes exige un modelo de amenazas propio: mínimo privilegio, registro de cada llamada, revisión humana de acciones y defensas contra inyección de instrucciones en los datos que el agente lee.

**¿Tienes poco tiempo?**

- [Tool collection in Microsoft Sentinel MCP server](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-mcp-tools-overview) · Documentación
- [Microsoft Sentinel | AI-Powered Entity Analysis in Sentinel's MCP Server](https://www.youtube.com/watch?v=adQ3Q38pPZ8) · Webinar

### Documentación, cursos y credenciales

- [Tool collection in Microsoft Sentinel MCP server](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-mcp-tools-overview) · Documentación · Oficial · Nuevo · Microsoft Learn · 14 may 2026. Lista las colecciones de herramientas MCP de Sentinel con sus URL de servidor: exploración de datos (data-exploration), creación de agentes de Security Copilot (security-copilot-agent-creation) y triage, más la creación de herramientas personalizadas desde KQL.
- [Get started with Microsoft Sentinel MCP server](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-mcp-get-started) · Documentación · Oficial · Nuevo · Microsoft Learn · 7 may 2026. Prerrequisitos (onboarding al data lake de Sentinel, rol Security Reader) y enlaces para añadir las colecciones a Security Copilot, Copilot Studio, Microsoft Foundry y VS Code, con prompts de prueba.
- [What is Microsoft Sentinel's support for Model Context Protocol (MCP)?](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-mcp-overview) · Documentación · Oficial · Microsoft Learn. Introduce el servidor MCP alojado de Sentinel y sus colecciones de herramientas para explorar el data lake, analizar entidades, triage y crear agentes en lenguaje natural.
- [Prioritize incidents and hunt for threats with triage collection](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-mcp-triage-tool) · Documentación · Oficial · Microsoft Learn. Describe la colección de triage (endpoint /mcp/triage) con herramientas como ListIncidents, GetIncidentById, ListAlerts, FetchAdvancedHuntingTablesOverview y RunAdvancedHuntingQuery, con parámetros y prompts de ejemplo.
- [Explore Microsoft Sentinel data lake with data exploration collection (MCP)](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-mcp-data-exploration-tool) · Documentación · Oficial · Vista previa · Nuevo · Microsoft Learn · 1 jul 2026. Herramientas MCP search_tables, ejecución de KQL sobre el lake, listado de workspaces, entity analyzer y herramientas de grafo (preview) sobre grafos de exposición, hunting y riesgo de datos. *Nota:* Endpoint roles mínimos Security Reader/Operator/Administrator; el entity analyzer consume SCU (Security Copilot Contributor) y las herramientas de grafo usan el medidor de graph
- [Create and use custom Microsoft Sentinel MCP tools (preview)](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-mcp-create-custom-tool) · Documentación · Oficial · Vista previa · Nuevo · Microsoft Learn · 14 may 2026. Cómo convertir consultas KQL guardadas de Advanced hunting o del data lake en herramientas MCP personalizadas con nombre, descripción, colección, workspace por defecto y parámetros, más buenas prácticas para describir herramientas. *Nota:* Crear/editar requiere Security Operator, Security Admin o Global Admin; invocar requiere Security Reader o Global Reader
- [Getting started with Microsoft Sentinel MCP server (agent creation tools)](https://learn.microsoft.com/en-us/copilot/security/developer/mcp-get-started) · Documentación · Oficial · Vista previa · Microsoft Learn. Guía paso a paso para conectar VS Code con GitHub Copilot en modo agente al endpoint security-copilot-agent-creation y usar sus cinco herramientas (start_agent_creation, compose_agent, etc.) para generar agentes de Security Copilot en YAML. *Nota:* Incluye un archivo de contexto scp-mcp-context.md recomendado como instrucciones personalizadas (.github/copilot-instructions.md)
- [Add Microsoft Sentinel MCP tools to AI agents in Microsoft Copilot Studio (preview)](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-mcp-use-tool-copilot-studio) · Documentación · Oficial · Vista previa · Microsoft Learn. Pasos para añadir colecciones de Sentinel a un agente de Copilot Studio con autenticación integrada de Entra y para registrar una app con el permiso SentinelPlatform.DelegatedAccess para colecciones personalizadas vía OAuth. *Nota:* Recomienda GPT-5 o posterior para mejor rendimiento con herramientas MCP
- [Use Microsoft Sentinel MCP tools in Microsoft Foundry (preview)](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-mcp-use-tool-azure-ai-foundry) · Documentación · Oficial · Vista previa · Microsoft Learn. Cómo conectar colecciones de Sentinel (p. ej. Data exploration) a agentes de Microsoft Foundry y añadir colecciones personalizadas como servidor MCP remoto con OAuth Identity Passthrough. *Nota:* Microsoft Foundry es el nuevo nombre de Azure AI Foundry; la URL conserva azure-ai-foundry

### Anuncios y blogs oficiales

- [What's new in Microsoft Sentinel: RSAC 2026](https://techcommunity.microsoft.com/blog/microsoftsentinelblog/what%E2%80%99s-new-in-microsoft-sentinel-rsac-2026/4503971) · Blog oficial · Empleado de Microsoft · spalani · Microsoft Tech Community - Microsoft Sentinel Blog · 20 mar 2026. Novedades de RSAC 2026: experiencia de migración SIEM en GA (Splunk/QRadar), generador de playbooks, GDAP, URBAC y RBAC a nivel de fila para Sentinel, y federación de datos con Fabric/ADLS/Databricks.
- [Microsoft Sentinel MCP server - Generally Available With Exciting New Capabilities](https://techcommunity.microsoft.com/blog/microsoft-security-blog/microsoft-sentinel-mcp-server---generally-available-with-exciting-new-capabiliti/4470125) · Blog oficial · Empleado de Microsoft · Omri Amdursky · Microsoft Tech Community - Microsoft Security Community Blog · 18 nov 2025. Anuncia la GA del servidor MCP de Sentinel (preview desde el 30-sep-2025) e introduce integración nativa con Copilot Studio y Microsoft Foundry, conexión con ChatGPT vía OAuth, herramientas KQL personalizadas, entity analyzer y herramientas de grafo.
- [Empowering defenders in the era of agentic AI with Microsoft Sentinel](https://www.microsoft.com/en-us/security/blog/2025/09/30/empowering-defenders-in-the-era-of-agentic-ai-with-microsoft-sentinel/) · Blog oficial · Empleado de Microsoft · Vasu Jakkal · Microsoft Security Blog · 30 sep 2025. Anuncio ejecutivo de Sentinel como plataforma agéntica: GA del data lake y vista previa pública de Sentinel graph y del servidor MCP, más el constructor de agentes sin código de Security Copilot.
- [The Agentic SOC Era: How Sentinel MCP Enables Autonomous Security Reasoning](https://techcommunity.microsoft.com/blog/microsoftsentinelblog/the-agentic-soc-era-how-sentinel-mcp-enables-autonomous-security-reasoning/4491003) · Blog oficial · Empleado de Microsoft · Iftekhar Hussain · Microsoft Tech Community - Microsoft Sentinel Blog · 3 feb 2026. Ejemplos prácticos de exploración en lenguaje natural del data lake con VS Code, GitHub Copilot y las herramientas de exploración de datos del MCP (p. ej. service principals inactivos reactivados).

### Webinars, videos y podcasts

- [MCP Server demo | Accelerate threat hunting with Microsoft Sentinel](https://www.youtube.com/watch?v=G3eQ5ap_Ys0) · Video · Empleado de Microsoft · Krishna Kumar Parthasarathy · Microsoft Security (YouTube). Demo del CVP de la plataforma Sentinel sobre herramientas MCP: búsqueda semántica, automatización KQL, entity analyzer y generación de notebooks Python para cazar un password spray.

### Laboratorios, GitHub y herramientas

- [Local_Agents (detecciones de agentes locales y MCP en VS Code)](https://github.com/davidalonsod/Dalonso-Security-Repo/blob/main/Use%20Cases%20Threat%20Hunting/Monitoring%20AI%20Agents/Local_Agents/README.MD) · GitHub · Comunidad · Vista previa · David Alonso Domínguez · GitHub. Candidatos de detección personalizada para agentes de IA locales y servidores MCP descubiertos por Defender for Endpoint (auto-aprobación, procesos no confiables, MCP externos). *Nota:* Depende de funciones en preview de Defender for Endpoint (AgentsInfo, LocalAgents)

### Comunidad: blogs, libros, newsletters y eventos

- [Sentinel Data Lake 2.0](https://tokesi.cloud/blogs/26_09_28_integrated_data_lake/) · Blog · Comunidad · Nuevo · Sandor Tokesi · tokesi.cloud · 28 sep 2026. Análisis práctico del cambio del 23-sep-2026: para tenants nuevos el data lake pasa a ser un nivel de tabla, con consultas en Advanced hunting y analítica avanzada en Fabric, y el autor observó que la API del lake y el servidor MCP no respondían en esos tenants.
- [From Hours to Minutes: Building Sentinel Detections with AI and the Sentinel MCP Server](https://moderncloud.ca/posts/2026/sentinel-data-lake-mcp-kql-detection/) · Blog · Comunidad · Anton Willoughby · Modern Cloud Solutions · 11 mar 2026. Caso práctico que usa VS Code, GitHub Copilot y la colección de exploración de datos (query_lake) para construir en minutos una detección sobre cambios de perfiles de configuración de Intune, generando además la KQL y acciones recomendadas.
- [How to integrate Microsoft Defender/ Sentinel with Microsoft Fabric](https://jeffreyappel.nl/how-to-integrate-microsoft-defender-sentinel-with-microsoft-fabric/) · Blog · MVP · Nuevo · Jeffrey Appel · jeffreyappel.nl · 6 oct 2026. Resume qué queda en Defender (Advanced hunting, workbooks, summary rules) y qué pasa a Fabric (jobs KQL, federación, notebooks, grafos personalizados) tras la integración del data lake del 23-sep-2026.
- [Microsoft Expands Sentinel Into Agentic Security Platform With Unified Data Lake](https://thehackernews.com/2025/09/microsoft-expands-sentinel-into-agentic.html) · Blog · Comunidad · Ravie Lakshmanan · The Hacker News · 30 sep 2025. Cobertura periodística del anuncio de Sentinel como plataforma agéntica con detalles de seguridad del data lake (RBAC de Azure y Entra, residencia regional, cifrado con claves gestionadas o CMK, aislamiento por tenant) y mitigaciones de prompt injection.

**Manos a la obra**

1. `Laboratorio` Conecta Visual Studio Code con GitHub Copilot al servidor MCP de Sentinel ([visión general](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-mcp-overview)) con las colecciones de exploración y triage.
2. `Laboratorio` Pide en lenguaje natural las tablas con datos de inicio de sesión y luego los fallos de los últimos siete días; revisa el KQL generado.
3. `Laboratorio` Lista los incidentes abiertos de severidad alta y pide un resumen con las herramientas de triage.
4. `Laboratorio` Crea una herramienta personalizada desde una consulta guardada de búsqueda avanzada y úsala desde Visual Studio Code.
5. `Laboratorio parcial` Conecta Copilot Studio o Microsoft Foundry con una app de Entra de acceso delegado y construye un agente simple ([Copilot Studio](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-mcp-use-tool-copilot-studio)).

**¿Quieres profundizar?**

- [MCP Server demo | Accelerate threat hunting with Microsoft Sentinel](https://www.youtube.com/watch?v=G3eQ5ap_Ys0) · Video
- [Sentinel Data Lake 2.0](https://tokesi.cloud/blogs/26_09_28_integrated_data_lake/) · Blog
- [From Hours to Minutes: Building Sentinel Detections with AI and the Sentinel MCP Server](https://moderncloud.ca/posts/2026/sentinel-data-lake-mcp-kql-detection/) · Blog
- [Local_Agents (detecciones de agentes locales y MCP en VS Code)](https://github.com/davidalonsod/Dalonso-Security-Repo/blob/main/Use%20Cases%20Threat%20Hunting/Monitoring%20AI%20Agents/Local_Agents/README.MD) · GitHub

<a id="x7"></a>

## X7 · Proyecto integrador: un SOC agéntico de punta a punta

*L400+ · ~16 h · Origen: Nuevo (equivale a la evaluación final práctica)*

El cierre del recorrido es construir, en tu laboratorio, un SOC completo que una todo lo aprendido: datos bien gobernados, detecciones probadas, automatización segura, IA en el circuito y agentes trabajando con supervisión. No se trata de usar todas las funciones, sino de demostrar criterio: qué automatizar, dónde poner a una persona, cuánto cuesta y cómo se mide.

El proyecto está organizado en fases con entregables verificables. Al completarlo tendrás un portafolio técnico reutilizable —repositorio, playbooks, plugins, agente y documentación— y la mejor preparación posible para conversaciones de arquitectura con clientes o con tu equipo.

**Qué vas a lograr**

- Integrar recolección, detección, automatización, IA y agentes en un flujo coherente.
- Justificar decisiones de diseño con criterios de riesgo, costo y operación.
- Documentar y presentar la solución como un caso de arquitectura.

> **Consejo Ninja.** Haz el proyecto en un tenant y una suscripción de laboratorio, con presupuesto y alertas configurados desde el primer día. Lo que se evalúa no es la cantidad de funciones, sino el criterio: qué automatizar, dónde poner a una persona, cuánto cuesta y cómo se mide.

**Manos a la obra**

1. `Laboratorio` **Fase 1 · Plataforma:** workspace principal incorporado a Defender con data lake, RBAC unificado y presupuesto. Entregable: diagrama y registro de decisiones (M1, M3).
2. `Laboratorio` **Fase 2 · Datos:** Entra ID, Defender XDR, actividad de Azure y una fuente Syslog/CEF vía AMA o un conector CCF; una tabla dividida entre analítica y lago. Entregable: inventario de tablas por nivel con costo estimado (M2, M3, M5, A5).
3. `Laboratorio` **Fase 3 · Detección:** tres reglas (una NRT, una con ASIM y una con watchlist) y una detección personalizada con acción de respuesta, todas en un repositorio. Entregable: contenido como código con mapeo MITRE (M7, A1, A4).
4. `Laboratorio` **Fase 4 · Validación:** simulación controlada con el Training Lab o una prueba en una VM de laboratorio; incidentes generados y métricas de detección (I5, M9).
5. `Laboratorio` **Fase 5 · Automatización:** regla de automatización, playbook de enriquecimiento con identidad administrada, aprobación en Teams y contención (M13, X1).
6. `Laboratorio parcial` **Fase 6 · IA:** playbook que invoca Security Copilot y comenta el incidente, un promptbook de triage y un plugin KQL propio (X2, X3, X4).
7. `Laboratorio parcial` **Fase 7 · Agentes y MCP:** un agente de Microsoft habilitado y supervisado, un agente propio que usa herramientas MCP de Sentinel y consultas en lenguaje natural sobre el lago desde Visual Studio Code (X5, X6).
8. `Laboratorio` **Fase 8 · Operación y gobierno:** salud y auditoría, tablero de consumo (ingesta, lago y SCU), identidades de agentes y un informe ejecutivo de una página (M12, X5).

<a id="reto-experto"></a>

## Reto del nivel

**Defensa ante el comité.** Presenta el proyecto integrador (X7) como si fuera ante el comité de riesgos: arquitectura, costos (ingesta, lago y unidades de cómputo de seguridad), métricas antes y después, riesgos y gobierno de los agentes, y la hoja de ruta de seis meses. Formato: diez minutos de exposición y una página de resumen ejecutivo.

<a id="quiz-experto"></a>

## Evaluación del nivel

Responde y compara con [Evaluaciones y respuestas](06_Evaluaciones_y_respuestas.md#eval-experto). Con 80 % o más, ¡nivel aprobado! (En la versión web puedes corregir en línea y generar tu certificado).

1. ¿Qué rol necesita la cuenta de servicio de Sentinel sobre el grupo de recursos del playbook para que una regla de automatización lo ejecute?
   - a) Logic App Contributor
   - b) Microsoft Sentinel Automation Contributor
   - c) Microsoft Sentinel Responder
   - d) Reader

2. La regla 1 (incidente creado) baja la severidad de media a baja; la regla 2, posterior, solo aplica a severidad media o mayor. ¿Qué ocurre?
   - a) La regla 2 se ejecuta porque evalúa el estado original
   - b) La regla 2 no se ejecuta porque evalúa el estado ya modificado
   - c) Ambas corren en paralelo
   - d) Se produce un error de conflicto

3. ¿Qué disparador de playbook NO puede invocarse desde una regla de automatización?
   - a) Incidente
   - b) Alerta
   - c) Entidad
   - d) Todos pueden invocarse

4. Un playbook en Logic Apps Standard con private endpoint falla cada vez que Sentinel intenta ejecutarlo. ¿Qué falta con mayor probabilidad?
   - a) Application Insights
   - b) Una política de restricción de acceso que permita a Sentinel invocar el flujo
   - c) Convertir el flujo a stateless
   - d) Instalarlo desde el Content hub

5. La identidad administrada de un playbook debe agregar comentarios y cambiar el estado de incidentes. ¿Qué rol mínimo necesita?
   - a) Microsoft Sentinel Reader
   - b) Microsoft Sentinel Responder
   - c) Owner
   - d) Logic App Operator

6. Con Sentinel en el portal de Defender, un incidente recibe cuatro cambios en seis minutos. ¿Qué recibe la automatización?
   - a) Cuatro actualizaciones
   - b) Una sola actualización con el cambio más reciente
   - c) Ninguna
   - d) Dos actualizaciones agrupadas

7. ¿Qué método de autenticación documenta oficialmente el conector de Security Copilot para Logic Apps?
   - a) Identidad administrada
   - b) OAuth delegado (Authorization Code) de un usuario con acceso a Security Copilot
   - c) Clave de API
   - d) Ninguno

8. En la acción Submit a Security Copilot prompt, ¿qué parámetro permite saltear el planificador e invocar una habilidad concreta?
   - a) Session ID
   - b) Plugins
   - c) Direct Skill Name
   - d) Prompt Content

9. Una organización con 2.500 licencias elegibles de Microsoft 365 E5, ¿cuántas SCU mensuales recibe por la inclusión?
   - a) 400
   - b) 1.000
   - c) 2.500
   - d) 10.000

10. ¿Qué colección del servidor MCP de Sentinel permite listar incidentes y ejecutar consultas de búsqueda avanzada?
   - a) Exploración de datos
   - b) Triage
   - c) Creación de agentes de Security Copilot
   - d) Grafo

11. ¿Qué rol mínimo permite crear herramientas MCP personalizadas a partir de consultas guardadas?
   - a) Security Reader
   - b) Global Reader
   - c) Security Operator
   - d) Microsoft Sentinel Reader

12. El Security Alert Triage Agent es…
   - a) Un agente de partner del Security Store
   - b) El Phishing Triage Agent ampliado a más tipos de alerta
   - c) Un plugin de Logic Apps
   - d) Un agente de Purview

13. ¿Cuál de estos NO es un destino válido para un plugin KQL de Security Copilot?
   - a) Sentinel
   - b) SentinelDataLake
   - c) Kusto
   - d) Purview

14. Al desarrollar un agente personalizado, ¿qué actividad consume SCU?
   - a) Crearlo con el agent builder
   - b) Crearlo con NL2Agent vía MCP
   - c) Probarlo
   - d) Publicarlo

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza al Ninja Training oficial, a la documentación de Microsoft Learn o a las certificaciones oficiales. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

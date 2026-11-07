# Nivel 3 · Avanzado · Extender y automatizar

*Microsoft Security Copilot Ninja Training: hacia el SOC agéntico · Edición 2026*

[← Nivel 2 · Intermedio](02_Nivel_2_Intermedio.md) · [Índice del programa](README.md) · [Nivel 4 · SOC agéntico →](04_Nivel_4_SOC_agentico.md)

<a id="avanzado"></a>

Promptbooks y plugins propios, Logic Apps, agentes personalizados, el servidor MCP de Sentinel, Power Platform, Copilot Studio y Microsoft Foundry. Terminas con una automatización de punta a punta y un agente propio probado y publicado.

*L400 · 7 módulos · ~46 horas · 62 recursos*

**Módulos de este nivel:** [A1 Promptbooks personalizados](#a1) · [A2 Plugins: KQL, API, GPT, MCP](#a2) · [A3 Logic Apps](#a3) · [A4 Agentes personalizados](#a4) · [A5 MCP de Sentinel](#a5) · [A6 Power Platform/Copilot Studio](#a6) · [A7 Foundry y pro-code](#a7)

<a id="a1"></a>

## A1 · Promptbooks personalizados

*L400 · ~4 h · Origen: Ninja oficial de 2024, parte 3, módulo 1 (promptbooks personalizados)*

Un **promptbook** es una secuencia reutilizable de prompts con entradas parametrizadas: convierte la mejor investigación de tu analista más experimentado en un procedimiento que cualquiera del turno puede repetir. Se crea seleccionando prompts de una sesión que funcionó; las entradas se escriben como `<NombreDelParametro>` sin espacios, cada prompt puede seguir aunque falle (*Continue on failure*, en disponibilidad general desde marzo de 2025) y se comparte solo contigo o con toda la organización.

El diseño importa: el **orden** de los prompts cambia el resultado y el consumo de SCU, y la **llamada directa a capacidades del sistema** (en vista previa) puede reducir el costo al evitar el planificador. Un promptbook también se ejecuta desde **Logic Apps** con la acción *Submit a Security Copilot promptbook*, y si falta una entrada obligatoria —por ejemplo `<SENTINEL_INCIDENT_ID>`— el flujo falla. Este módulo cubre diseño, pruebas, versionado y gobierno de promptbooks, con las muestras del repositorio oficial como punto de partida.

**Por qué importa**

El promptbook es el paso más barato para estandarizar un procedimiento del SOC: no requiere código, se comparte en minutos y deja el mismo rastro auditable en cada ejecución. Bien ordenado y con llamadas directas, reduce las SCU por ejecución y el tiempo de triage de los analistas nuevos.

**Qué vas a lograr**

- Convertir una sesión en un promptbook con entradas parametrizadas.
- Diseñar el orden de los prompts, el uso de Continue on failure y las llamadas directas a capacidades.
- Compartir, versionar y retirar promptbooks con criterios de gobierno.
- Ejecutar un promptbook desde Logic Apps con las entradas del incidente.

> **Novedad.** La guía para crear promptbooks (actualizada el 4 de junio de 2026) indica que las entradas se escriben como `<NombreDelParametro>` sin espacios, que *Continue on failure* se activa por prompt, que se comparte con Just me o con Anyone in my organization y que reordenar los prompts cambia el resultado y el consumo de SCU ([crear promptbooks](https://learn.microsoft.com/en-us/copilot/security/build-promptbooks)).

> **Novedad.** *Continue on failure* está en disponibilidad general desde marzo de 2025; la llamada directa a capacidades del sistema dentro de un prompt sigue en vista previa y puede reducir el consumo de SCU ([What's new](https://learn.microsoft.com/en-us/copilot/security/whats-new-copilot-security)).

> **Atención.** Si lanzas un promptbook desde Logic Apps con *Submit a Security Copilot promptbook* y falta una entrada obligatoria —por ejemplo `<SENTINEL_INCIDENT_ID>` en el promptbook de investigación de incidentes—, el flujo falla ([conector de Logic Apps](https://learn.microsoft.com/en-us/copilot/security/connector-logicapp), [usar promptbooks](https://learn.microsoft.com/en-us/copilot/security/using-promptbooks)).

> **Consejo Ninja.** El repositorio oficial incluye muestras de promptbooks —alto radio de impacto, inicios de sesión anómalos y priorización de incidentes— y scripts de PowerShell para gestionarlos ([muestras de promptbooks](https://github.com/Azure/Security-Copilot/tree/main/Promptbook%20samples)); el libro de Packt dedica un capítulo al diseño de promptbooks ([Microsoft Security Copilot, Packt](https://www.packtpub.com/en-us/product/microsoft-security-copilot-9781835884522/chapter/the-power-of-promptbooks-in-security-copilot-6/section/the-power-of-promptbooks-in-security-copilot-6)).

**¿Tienes poco tiempo?**

- [Build your own promptbooks](https://learn.microsoft.com/en-us/copilot/security/build-promptbooks) · Documentación
- [Use promptbooks in Microsoft Security Copilot](https://learn.microsoft.com/en-us/copilot/security/using-promptbooks) · Documentación
- [Microsoft Security Copilot Sample Promptbooks Library (Azure/Security-Copilot)](https://github.com/Azure/Security-Copilot/tree/main/Promptbook%20samples) · GitHub

### Documentación, cursos y credenciales

- [Build your own promptbooks](https://learn.microsoft.com/en-us/copilot/security/build-promptbooks) · Documentación · Oficial · Nuevo · Microsoft Learn · 4 jun 2026. Explica cómo convertir una sesión en promptbook con entradas <parametrizadas>, continuar ante fallos, invocar capacidades del sistema (preview), compartirlo con la organización y gestionarlo desde la biblioteca.
- [Use promptbooks in Microsoft Security Copilot](https://learn.microsoft.com/en-us/copilot/security/using-promptbooks) · Documentación · Oficial · Nuevo · Microsoft Learn · 1 jun 2026. Lista y explica los promptbooks prediseñados (impacto de artículo de amenaza externo, investigación de incidentes de Sentinel/Defender XDR, análisis de usuario, script sospechoso, perfil de actor, TI 360 y evaluación de vulnerabilidad) con sus entradas.

### Laboratorios, GitHub y herramientas

- [Microsoft Security Copilot Sample Promptbooks Library (Azure/Security-Copilot)](https://github.com/Azure/Security-Copilot/tree/main/Promptbook%20samples) · GitHub · Oficial · Legado aún útil · Microsoft y comunidad · GitHub (Azure). Muestras de promptbooks personalizados (usuarios de alto radio de impacto, inicios de sesión anómalos, priorización de incidentes, análisis de cabeceras de correo) y scripts PowerShell para gestionarlos. *Nota:* Contenido de 2024-2025; revisar nombres de plugins y SCU antes de reutilizar

**Manos a la obra**

1. `Laboratorio parcial` Ejecuta el promptbook integrado de investigación de incidentes y crea uno propio desde la sesión con la entrada `<INCIDENT_ID>`; activa Continue on failure en los prompts no críticos y compártelo con tu organización ([crear promptbooks](https://learn.microsoft.com/en-us/copilot/security/build-promptbooks)). Limitación: requiere 1 SCU temporal y alertas de prueba en Defender XDR. Evidencia: promptbook parametrizado publicado.
2. `Laboratorio parcial` Cambia el orden de los prompts de tu promptbook, prueba la llamada directa a una capacidad del sistema (vista previa) en uno de ellos y compara resultados y SCU de las dos versiones en el panel de uso. Limitación: consumo de SCU. Evidencia: tabla de resultados y consumo por versión.
3. `Laboratorio` Revisa tres [muestras de promptbooks](https://github.com/Azure/Security-Copilot/tree/main/Promptbook%20samples) del repositorio oficial (alto radio de impacto, inicios de sesión anómalos y priorización de incidentes) y adapta una a tu SOC: entradas, plugins requeridos, orden de los prompts y criterio de verificación de cada salida. Evidencia: diseño del promptbook adaptado.
4. `Laboratorio parcial` Lanza tu promptbook desde Logic Apps con la acción Submit a Security Copilot promptbook ([conector de Logic Apps](https://learn.microsoft.com/en-us/copilot/security/connector-logicapp)) y provoca a propósito el error de entrada faltante para documentar cómo falla y cómo lo detectas en el historial de ejecuciones. Limitación: SCU y costo de Logic Apps. Evidencia: ejecución fallida y ejecución corregida.
5. `Laboratorio` Define el ciclo de vida de los promptbooks del equipo: convención de nombres con versión, dueño, revisión de contenido sensible antes de compartir con toda la organización, pruebas mínimas y criterio de retiro ([usar promptbooks](https://learn.microsoft.com/en-us/copilot/security/using-promptbooks)). Evidencia: procedimiento publicado.
6. `Solo producción` Valida tus promptbooks sobre incidentes reales ya cerrados con un grupo piloto antes de compartirlos con toda la organización. Cómo hacerlo seguro: compartir solo con el equipo autorizado, revisar que las salidas no expongan datos sensibles en sesiones compartidas y comparar el resultado con la investigación original. Evidencia: informe de validación de cinco incidentes.

<a id="a2"></a>

## A2 · Plugins personalizados: KQL, API, GPT y MCP

*L400 · ~8 h · Origen: Ninja oficial de 2024, parte 2, módulo 2 (plugins de OpenAI), y parte 3, módulos 2 y 4 (plugins personalizados y bases de conocimiento)*

Los plugins son la forma en que Security Copilot —y sus agentes— llegan a tus datos y herramientas. Todo plugin parte de un **manifiesto** YAML o JSON con un `Descriptor` y uno o más `SkillGroups`, y cada skill tiene un formato: **KQL** (consultas sobre Defender, Sentinel, el data lake de Sentinel, Log Analytics o Kusto, con plantillas de hasta 80.000 caracteres), **API** (una especificación OpenAPI 3.0 o 3.0.1 con uno de los esquemas de autenticación admitidos), **GPT** (skills basadas en instrucciones al modelo) y **MCP**, en vista previa, que conecta un servidor Model Context Protocol. Los temas del Ninja de 2024 que este módulo actualiza —plugins de OpenAI, plugins personalizados y bases de conocimiento— se resuelven hoy, en esta guía, con estos formatos: por ejemplo, una base de conocimiento interna se conecta con un plugin API o MCP.

Escribir la skill es la mitad del trabajo; la otra mitad es que el orquestador la elija bien. Los nombres y descripciones tienen límites (40 caracteres para el nombre visible, 16.000 para la descripción que lee el modelo) y las skills multipropósito provocan **colisiones** con otras. Los plugins MCP tienen reglas propias: lista `AllowedTools` obligatoria, transporte StreamableHttp recomendado (SSE se deprecará), solo herramientas —ni recursos ni prompts—, sin redescubrimiento automático y sin importar herramientas marcadas como destructivas. Para integraciones programáticas, Microsoft Graph expone en beta sesiones, prompts y evaluaciones de Security Copilot.

**Por qué importa**

El conocimiento más valioso del SOC vive en tus propias tablas, APIs y herramientas. Un plugin bien descrito permite que Copilot y los agentes lo usen con los permisos de cada persona, en lugar de copiar y pegar datos; uno mal descrito colisiona con otros, devuelve respuestas equivocadas y gasta SCU.

**Qué vas a lograr**

- Escribir un manifiesto con Descriptor y SkillGroups dentro de los límites documentados.
- Construir un plugin KQL con targets de Defender y Sentinel y funciones parametrizadas.
- Construir un plugin API con OpenAPI 3.0 y el esquema de autenticación adecuado.
- Conectar un servidor MCP como plugin respetando sus limitaciones de vista previa.
- Usar la API de Microsoft Graph (beta) para crear sesiones, prompts y evaluaciones.

> **Atención.** Límites del manifiesto: solo OpenAPI 3.0 o 3.0.1, nombre interno de hasta 100 caracteres, nombre visible de hasta 40 y descripción para el modelo de hasta 16.000; evita las colisiones que provocan las skills multipropósito ([plugins personalizados](https://learn.microsoft.com/en-us/copilot/security/custom-plugins)). Las skills KQL admiten los targets Defender, Sentinel, SentinelDataLake, LogAnalytics y Kusto, con plantillas en línea, TemplateUrl o PackageUrl de hasta 80.000 caracteres ([plugins KQL](https://learn.microsoft.com/en-us/copilot/security/plugin-kql)).

> **Novedad.** Los plugins MCP están en vista previa (documentación del 13 de noviembre de 2025): `Format: MCP`, lista `AllowedTools` obligatoria, StreamableHttp recomendado (SSE se deprecará), solo herramientas —no recursos ni prompts—, sin redescubrimiento automático (hay que volver a subir el YAML), entradas solo de tipo primitivo, y las herramientas con destructiveHint=true no se importan. Microsoft recomienda servidores alojados por el propio proveedor, no proxies ([plugins MCP](https://learn.microsoft.com/en-us/copilot/security/plugin-mcp)).

> **Atención.** Un plugin API admite un solo tipo de autenticación preconfigurado entre None, Basic, ApiKey, ServiceHttp, OAuthAuthorizationCodeFlow, OAuthClientCredentialsFlow, AAD y AADDelegated ([plugins API](https://learn.microsoft.com/en-us/copilot/security/plugin-api)). Para subir plugins o agentes para toda la organización, un owner debe permitir que owners y contributors gestionen los plugins personalizados ([manifiesto YAML de agentes](https://learn.microsoft.com/en-us/copilot/security/developer/build-agent-manifest)).

> **Consejo Ninja.** Para acelerar: las funciones KQL parametrizadas simplifican los plugins ([funciones parametrizadas](https://techcommunity.microsoft.com/blog/securitycopilotblog/using-parameterized-functions-with-kql-based-custom-plugins-in-microsoft-securit/4419286)), el taller oficial tiene tareas paso a paso ([Custom Plugin Workshop](https://github.com/Azure/Security-Copilot/tree/main/Technical%20Workshops/Custom%20Plugin%20Workshop)) y un arquitecto de Microsoft publicó una skill de GitHub Copilot que genera manifiestos ([builder de plugins y agentes](https://github.com/mariocuomo/Experimenting-With-Security-Copilot/blob/main/Security%20Copilot%20custom%20plugins%20builder/README.md)).

**¿Tienes poco tiempo?**

- [Create your own custom plugins in Microsoft Security Copilot](https://learn.microsoft.com/en-us/copilot/security/custom-plugins) · Documentación
- [Kusto Query Language (KQL) plugins in Microsoft Security Copilot](https://learn.microsoft.com/en-us/copilot/security/plugin-kql) · Documentación
- [Model Context Protocol (MCP) plugins in Microsoft Security Copilot (Preview)](https://learn.microsoft.com/en-us/copilot/security/plugin-mcp) · Documentación
- [API plugins in Microsoft Security Copilot](https://learn.microsoft.com/en-us/copilot/security/plugin-api) · Documentación

**Formatos de skill en Security Copilot y cuándo usarlos**

| Formato | Para qué sirve | Requisitos y límites | Notas de estado | Fuente |
|---|---|---|---|---|
| KQL | Consultar tus tablas con plantillas parametrizadas | Targets Defender, Sentinel, SentinelDataLake, LogAnalytics o Kusto; plantilla en línea, TemplateUrl o PackageUrl de hasta 80.000 caracteres | Documentación de septiembre de 2025 | [Plugins KQL](https://learn.microsoft.com/en-us/copilot/security/plugin-kql) |
| API | Llamar a servicios propios o de terceros | OpenAPI 3.0 o 3.0.1; un solo tipo de autenticación preconfigurado | Documentado | [Plugins API](https://learn.microsoft.com/en-us/copilot/security/plugin-api) |
| GPT | Encapsular instrucciones al modelo para resumir, clasificar o dar formato | Descripción clara para que el orquestador no la confunda con otras skills | Documentado | [Plugins personalizados](https://learn.microsoft.com/en-us/copilot/security/custom-plugins) |
| MCP | Conectar las herramientas de un servidor Model Context Protocol | AllowedTools obligatorio; StreamableHttp recomendado; solo herramientas; sin redescubrimiento; no importa herramientas destructivas | Vista previa (documentación del 13 de noviembre de 2025) | [Plugins MCP](https://learn.microsoft.com/en-us/copilot/security/plugin-mcp) |
| LogicApp | Ejecutar un flujo de Logic Apps como acción desde prompts, promptbooks o agentes | Disparador HTTP Request; mismo tenant; SCU aprovisionadas | Documentación de febrero de 2026; Microsoft anuncia un disparador nativo | [Logic Apps como plugin](https://learn.microsoft.com/en-us/copilot/security/developer/plugin-logic-apps) |
| AGENT | Definir un agente con instrucciones y ChildSkills dentro de AgentDefinitions | Un AgentDefinition por YAML; FetchSkill y ProcessSkill con el espacio de nombres Skillset.Skill | Agentes personalizados en vista previa desde septiembre de 2025 | [Manifiesto de agentes](https://learn.microsoft.com/en-us/copilot/security/developer/agent-manifest) |

Fuentes: columna Fuente y [plugins personalizados](https://learn.microsoft.com/en-us/copilot/security/custom-plugins).

### Documentación, cursos y credenciales

- [Create your own custom plugins in Microsoft Security Copilot](https://learn.microsoft.com/en-us/copilot/security/custom-plugins) · Documentación · Oficial · Nuevo · Microsoft Learn · 29 may 2026. Describe el manifiesto YAML/JSON de un plugin (Descriptor y SkillGroups), el mapeo con manifiestos OpenAI (solo OpenAPI 3.0/3.0.1) y buenas prácticas para evitar colisiones de skills.
- [API plugins in Microsoft Security Copilot](https://learn.microsoft.com/en-us/copilot/security/plugin-api) · Documentación · Oficial · Microsoft Learn. Tutoriales para crear plugins API desde una especificación OpenAPI u OpenAI existente y configurar los esquemas de autenticación soportados (Basic, ApiKey, OAuth, Entra ID/AADDelegated, etc.).
- [Kusto Query Language (KQL) plugins in Microsoft Security Copilot](https://learn.microsoft.com/en-us/copilot/security/plugin-kql) · Documentación · Oficial · Microsoft Learn · 30 sep 2025. Referencia de skills KQL con los targets Defender, Sentinel, SentinelDataLake, LogAnalytics y Kusto, plantillas de hasta 80.000 caracteres y ejemplos YAML.
- [Model Context Protocol (MCP) plugins in Microsoft Security Copilot (Preview)](https://learn.microsoft.com/en-us/copilot/security/plugin-mcp) · Documentación · Oficial · Vista previa · Microsoft Learn · 13 nov 2025. Muestra cómo conectar un servidor MCP externo como plugin (Format: MCP) con OAuth, AllowedTools obligatorio y StreamableHttp, y enumera sus limitaciones. *Nota:* Solo herramientas MCP (no resources/prompts); no redescubre herramientas; ignora tools con destructiveHint=true; SSE se deprecará
- [Microsoft Graph Security Copilot API (beta): Create session](https://learn.microsoft.com/en-us/graph/api/security-securitycopilot-workspace-post-sessions?view=graph-rest-beta) · Documentación · Oficial · Vista previa · Microsoft Learn. Referencia de la API beta de Microsoft Graph para Security Copilot (workspaces, sesiones, prompts y evaluaciones) que permite invocarlo programáticamente. *Nota:* Beta no soportada en producción; permiso SecurityCopilotWorkspaces.ReadWrite.All; rol mínimo Security Copilot Contributor; solo nube global
- [Microsoft Graph Security Copilot API (beta): Create evaluation](https://learn.microsoft.com/en-us/graph/api/security-securitycopilot-prompt-post-evaluations?view=graph-rest-beta) · Documentación · Oficial · Vista previa · Microsoft Learn. Muestra cómo lanzar la evaluación de un prompt y luego consultarla (patrón asíncrono sesión → prompt → evaluación). *Nota:* Mismo patrón asíncrono que get_evaluation en el MCP de creación de agentes

### Laboratorios, GitHub y herramientas

- [Azure/Security-Copilot (repositorio oficial de la comunidad)](https://github.com/Azure/Security-Copilot) · GitHub · Empleado de Microsoft · Legado aún útil · Sean Wasonga y colaboradores · GitHub – Azure. Repositorio oficial con plugins de ejemplo, muestras de promptbooks, prompts, escenarios de Logic Apps, monitoreo y talleres técnicos usados por el Ninja. *Nota:* Último commit hace ~9 meses (≈ febrero 2026); varios enlaces del README apuntan a rutas antiguas de Learn y al nombre Copilot-For-Security

**Manos a la obra**

1. `Laboratorio parcial` Crea un [plugin KQL](https://learn.microsoft.com/en-us/copilot/security/plugin-kql) con dos skills parametrizadas, una con `Target: Defender` sobre EmailEvents y otra con `Target: Sentinel` sobre SigninLogs; súbelo como privado, pruébalo y publícalo para la organización con permiso del owner. Limitación: consumo de SCU y un workspace de Sentinel con datos. Evidencia: plugin publicado y su YAML versionado en Git.
2. `Laboratorio parcial` Sigue la tarea de KQL del [Custom Plugin Workshop](https://github.com/Azure/Security-Copilot/tree/main/Technical%20Workshops/Custom%20Plugin%20Workshop/Task05_KQL) con una función parametrizada en Log Analytics y compara el resultado con tu propio YAML. Limitación: consumo de SCU al probar. Evidencia: diferencias documentadas entre ambos manifiestos.
3. `Laboratorio parcial` Crea un [plugin API](https://learn.microsoft.com/en-us/copilot/security/plugin-api) con una especificación OpenAPI 3.0 sobre una API de prueba propia (por ejemplo, una función de Azure detrás de API Management) con autenticación ApiKey u OAuth, y pruébalo con tres prompts. Limitación: costo de Azure y de SCU. Evidencia: plugin API probado con las tres respuestas.
4. `Laboratorio parcial` Despliega un servidor MCP de prueba en Azure con StreamableHttp y OAuth, conéctalo como [plugin MCP](https://learn.microsoft.com/en-us/copilot/security/plugin-mcp) con `AllowedTools`, comprueba que una herramienta con destructiveHint=true no se importa y que una herramienta nueva solo aparece después de volver a subir el YAML. Limitación: vista previa, costo de Azure y de SCU. Evidencia: plugin MCP probado y registro de ambas comprobaciones.
5. `Laboratorio` Escribe la guía de estilo de descripciones de skills del equipo —nombres visibles de hasta 40 caracteres, qué debe decir la descripción para el modelo, ejemplos de entradas y cómo evitar colisiones con skills existentes— y aplícala a tres skills propias ([plugins personalizados](https://learn.microsoft.com/en-us/copilot/security/custom-plugins)). Evidencia: guía de estilo y las tres skills corregidas.
6. `Laboratorio parcial` Registra una aplicación con el permiso SecurityCopilotWorkspaces.ReadWrite.All y, con la [API de Microsoft Graph en beta](https://learn.microsoft.com/en-us/graph/api/security-securitycopilot-workspace-post-sessions?view=graph-rest-beta), crea una sesión, un prompt y una [evaluación](https://learn.microsoft.com/en-us/graph/api/security-securitycopilot-prompt-post-evaluations?view=graph-rest-beta), y consulta su estado. Limitación: beta no soportada en producción, solo nube global y consumo de SCU. Evidencia: script y respuestas de la API.
7. `Solo producción` Publica un plugin para toda la organización en producción. Cómo hacerlo seguro: revisión previa del owner, carga de plugins restringida, funciones parametrizadas en lugar de consultas abiertas, pruebas previas en el workspace de laboratorio y retiro inmediato si expone datos que el rol del usuario no debería ver. Evidencia: aprobación del owner y resultado de las pruebas.

**¿Quieres profundizar?**

- [Azure/Security-Copilot (repositorio oficial de la comunidad)](https://github.com/Azure/Security-Copilot) · GitHub

<a id="a3"></a>

## A3 · Automatización con Azure Logic Apps

*L400 · ~6 h · Origen: Ninja oficial de 2024, parte 3, módulo 3 (automatización con Logic Apps)*

Logic Apps y Security Copilot se conectan en dos direcciones. **De Logic Apps hacia Copilot**, el conector ofrece *Submit a Security Copilot prompt* —con sesión, lista de plugins para evitar colisiones y *Direct Skill* para saltarse el planificador—, *Submit a Security Copilot promptbook* y, según la referencia del conector, *Execute a Security Copilot Agent*, con un límite de 600 llamadas por conexión cada 60 segundos. **De Copilot hacia Logic Apps**, un flujo con disparador HTTP se registra como skill (`Format: LogicApp`) y puede invocarse desde prompts, promptbooks o agentes, por ejemplo para crear un ticket o agregar un usuario a una watchlist con aprobación humana.

El diseño decide el costo: filtrar por severidad, usar direct skills, acotar plugins y reutilizar sesiones puede reducir mucho las SCU por incidente, y las muestras oficiales advierten que las Logic Apps con Copilot elevan el consumo. También importan las identidades: la conexión usa una cuenta con acceso a Security Copilot y a los datos consultados, y un agente disparado desde Logic Apps corre con su propia identidad de ejecución, distinta de la de la conexión. Los cargos de Logic Apps no están incluidos en E5/E7.

El SOAR con Logic Apps se profundiza en el programa de Sentinel (módulos X1 y X3); aquí te concentras en la integración con Security Copilot y en decidir cuándo conviene un playbook, un agente o un workflow agéntico de Logic Apps.

**Por qué importa**

La automatización define si la IA se usa donde más valor aporta o si vacía el pool: enriquecer solo los incidentes de severidad alta con una direct skill cuesta una fracción de un prompt genérico para cada incidente, y el analista encuentra el resumen ya escrito en el incidente cuando lo abre, lo que reduce el MTTA.

**Qué vas a lograr**

- Invocar Security Copilot desde un playbook con prompt, promptbook o agente y escribir el resultado en el incidente.
- Reducir el consumo con listas de plugins, direct skills, sesiones y filtros por severidad.
- Exponer una Logic App como skill invocable desde prompts, promptbooks y agentes.
- Elegir la autenticación del conector y entender la identidad de ejecución de los agentes.
- Decidir entre playbooks de Logic Apps, agentes de Security Copilot y workflows agénticos de Logic Apps.

> **Novedad.** La referencia del conector de Security Copilot suma Execute a Security Copilot Agent, Run a Security Copilot promptbook, Fetch prompt status y Submit a Security Copilot prompt (V2), esta en vista previa; el límite es de 600 llamadas por conexión cada 60 segundos y el conector no está disponible en GCC, GCC High, DoD ni China ([referencia del conector](https://learn.microsoft.com/en-us/connectors/securitycopilot/)).

> **Atención.** Para disparar agentes desde Logic Apps (documentación del 10 de abril de 2026), el agente debe estar en el workspace por defecto y, si es personalizado, compartido con Anyone in this workspace; el agente corre con su propia identidad de ejecución, distinta de la identidad de la conexión ([disparar agentes desde Logic Apps](https://learn.microsoft.com/en-us/copilot/security/connector-logicapp-agent-trigger)).

> **Atención.** La autenticación del conector tiene versiones distintas: la documentación de Logic Apps indica solo OAuth delegado, la referencia del conector ofrece también service principal y el ejemplo oficial de GitHub menciona certificado de cliente; además, la autenticación Default figura como deprecada y la referencia todavía menciona el antiguo Early Access Program. Pruébalo en tu laboratorio antes de diseñar producción ([conector](https://learn.microsoft.com/en-us/copilot/security/connector-logicapp), [ejemplo oficial](https://github.com/Azure/Security-Copilot/blob/main/Logic%20Apps/SecurityCopilot-Sentinel-Incident-Investigation/readme.md)).

> **Qué cambió.** Las muestras antiguas usan las acciones Evaluate Prompt y Evaluate Direct Skill; hoy se usan Submit a Security Copilot prompt y promptbook. Las muestras advierten que las Logic Apps con Copilot elevan el consumo de SCU, y una Logic App expuesta como skill (`Format: LogicApp`) necesita disparador HTTP, el mismo tenant y SCU aprovisionadas ([muestras de Logic Apps](https://github.com/Azure/Security-Copilot/blob/main/Logic%20Apps/Readme.md), [Logic Apps como plugin](https://learn.microsoft.com/en-us/copilot/security/developer/plugin-logic-apps)). El SOAR se profundiza en el programa de Sentinel (módulos X1 y X3).

**¿Tienes poco tiempo?**

- [Logic Apps connectors in Microsoft Security Copilot](https://learn.microsoft.com/en-us/copilot/security/connector-logicapp) · Documentación
- [Trigger Security Copilot agents from Azure Logic Apps](https://learn.microsoft.com/en-us/copilot/security/connector-logicapp-agent-trigger) · Documentación
- [Azure Logic Apps plugin in Microsoft Security Copilot](https://learn.microsoft.com/en-us/copilot/security/developer/plugin-logic-apps) · Documentación
- [When to Use Logic Apps vs. Security Copilot Agents](https://www.youtube.com/watch?v=GMST8t6hF8Y) · Webinar

### Documentación, cursos y credenciales

- [Trigger Security Copilot agents from Azure Logic Apps](https://learn.microsoft.com/en-us/copilot/security/connector-logicapp-agent-trigger) · Documentación · Oficial · Microsoft Learn · 10 abr 2026. Guía paso a paso de la acción Execute a Security Copilot Agent para disparar agentes ya configurados desde un flujo, con identidad de ejecución del agente separada de la conexión.
- [Azure Logic Apps plugin in Microsoft Security Copilot](https://learn.microsoft.com/en-us/copilot/security/developer/plugin-logic-apps) · Documentación · Oficial · Microsoft Learn · 25 feb 2026. Enseña a exponer una Logic App con disparador HTTP como skill (Format: LogicApp) invocable desde prompts, promptbooks o agentes, con ejemplo para crear incidentes en Sentinel.
- [Logic Apps connectors in Microsoft Security Copilot](https://learn.microsoft.com/en-us/copilot/security/connector-logicapp) · Documentación · Oficial · Microsoft Learn · 15 ene 2026. Explica las acciones Submit a Security Copilot prompt y Submit a Security Copilot promptbook (sesión, lista de plugins, Direct Skill) en planes Standard y Consumption con autenticación OAuth delegada.
- [Build logic apps with Microsoft Sentinel MCP tools (preview)](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-mcp-logic-apps) · Documentación · Oficial · Vista previa · Nuevo · Microsoft Learn · 1 jul 2026. Explica cómo usar el entity analyzer (usuarios y URL) en Logic Apps mediante las plantillas Incident/Url/HTTP Trigger Entity Analyzer o el conector Microsoft Sentinel MCP tools. *Nota:* Requiere Sentinel SOAR Essentials actualizado y rol Security Reader para la identidad de la Logic App; limitar paralelismo a ~5

### Webinars, videos y podcasts

- [When to Use Logic Apps vs. Security Copilot Agents](https://www.youtube.com/watch?v=GMST8t6hF8Y) · Webinar · Empleado de Microsoft · Shiv Patel; Innocent Wafula · YouTube - Microsoft Security Community · 9 oct 2025. Sesión de la Skilling Series que compara flujos orquestados con Logic Apps frente a agentes de Security Copilot, con demos de ambos y criterios de cuándo usar cada uno.

### Comunidad: blogs, libros, newsletters y eventos

- [Supercharging Security Copilot with Logic Apps: Best practices and pro tips (republicación)](https://serviceautomation.online/supercharging-security-copilot-with-logic-apps-best-practices-and-pro-tips/) · Blog · Empleado de Microsoft · Innocent Wafula y otros (Microsoft) · Service Automation (republica Tech Community) · 24 sep 2025. Buenas prácticas para elegir casos de uso, usar invocación directa de skills para ahorrar SCU, prototipar con variables, gestionar sesiones, identidades administradas y monitorización.

**Manos a la obra**

1. `Laboratorio parcial` Construye un playbook con disparador de incidente de Sentinel que llame a Submit a Security Copilot prompt con una lista de plugins acotada y escriba el resultado con Add comment to incident; adjúntalo a una regla de automatización que solo lo ejecute para severidad alta ([conector de Logic Apps](https://learn.microsoft.com/en-us/copilot/security/connector-logicapp)). Limitación: consumo de SCU y de Logic Apps, que E5/E7 no incluye. Evidencia: playbook con Security Copilot activo solo para severidad alta.
2. `Laboratorio parcial` Repite el playbook usando Direct Skill Name y Direct Skill Inputs en lugar del planificador y compara SCU y duración con la versión anterior en el panel de uso (tipo automatizado). Limitación: consumo de SCU. Evidencia: comparación de consumo con direct skills.
3. `Laboratorio parcial` Desde Logic Apps, usa Execute a Security Copilot Agent con un agente del workspace por defecto compartido con Anyone in this workspace ([disparar agentes](https://learn.microsoft.com/en-us/copilot/security/connector-logicapp-agent-trigger)) y compara el resultado con la plantilla Incident Trigger Entity Analyzer del [servidor MCP de Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-mcp-logic-apps), con paralelismo 5. Limitación: SCU y data lake para el entity analyzer. Evidencia: los dos comentarios en el mismo incidente y tu evaluación.
4. `Laboratorio parcial` Expón una Logic App con disparador HTTP como skill ([Logic Apps como plugin](https://learn.microsoft.com/en-us/copilot/security/developer/plugin-logic-apps)) que agregue un usuario a una watchlist solo después de una confirmación por correo, e invócala desde un promptbook. Limitación: requiere el mismo tenant y SCU aprovisionadas. Evidencia: flujo con aprobación humana y ejecución registrada.
5. `Laboratorio` Mira el webinar [When to Use Logic Apps vs. Security Copilot Agents](https://www.youtube.com/watch?v=GMST8t6hF8Y) y completa una tabla de decisión para cinco procesos de tu SOC —playbook de Logic Apps, agente de Security Copilot o workflow agéntico de Logic Apps— con el criterio usado (determinismo, juicio, costo y riesgo). Evidencia: tabla de decisión.
6. `Solo producción` Lleva el playbook a producción. Cómo hacerlo seguro: cuenta de conexión dedicada con acceso mínimo, filtro por severidad, lista de plugins acotada, regla creada deshabilitada y probada sobre incidentes de prueba, alerta de consumo en el panel de uso y reversión inmediata deshabilitando la regla ([buenas prácticas](https://serviceautomation.online/supercharging-security-copilot-with-logic-apps-best-practices-and-pro-tips/)). Evidencia: plan de despliegue y primera semana de consumo revisada.

**¿Quieres profundizar?**

- [Supercharging Security Copilot with Logic Apps: Best practices and pro tips (republicación)](https://serviceautomation.online/supercharging-security-copilot-with-logic-apps-best-practices-and-pro-tips/) · Blog

<a id="a4"></a>

## A4 · Agentes personalizados: creación, pruebas y publicación

*L400 · ~10 h · Origen: Nuevo en esta edición*

Cuando ningún agente de Microsoft o de partners cubre tu proceso, construyes el tuyo. Un agente de Security Copilot combina **herramientas** (skills), **disparadores**, un **orquestador**, **instrucciones** y **feedback y memoria**. Hay cuatro vías de creación —**NL2Agent** (describirlo en lenguaje natural; figura como «Private Preview, but globally available»), el **agent builder** sin código, subir un **manifiesto YAML** y las **herramientas MCP** de creación de agentes desde Visual Studio Code— y todas terminan en el mismo manifiesto, con las claves `Descriptor`, `AgentDefinitions` y `SkillGroups`.

Crear y publicar no consumen SCU; **probar y ejecutar, siempre**. Las pruebas usan el mapa de actividad y la optimización automática de instrucciones (*autotune*, solo en regiones de EE. UU. y la UE), y publicar con el mismo nombre sobrescribe la versión anterior. Un contributor publica en su propio ámbito; un owner, para todo el workspace; los partners pueden llevar su agente al Security Store con un paquete y una certificación. Un punto de diseño que conviene conocer: según la documentación de Security Copilot, la opción de crear una identidad de agente solo existe para los agentes de Microsoft, así que un agente propio corre con una cuenta de usuario y sus permisos.

**Por qué importa**

Un agente que codifica un procedimiento propio —un informe post-incidente, la investigación de una detección específica— escala el criterio de tus mejores analistas. La disciplina de pruebas y la publicación por ámbitos evitan el riesgo más común: agentes con herramientas o permisos de más publicados para todos sin revisión.

**Qué vas a lograr**

- Describir los componentes de un agente y las cuatro vías de creación que convergen en el manifiesto.
- Construir un agente con el agent builder: instrucciones, entradas, herramientas y disparadores.
- Escribir y validar un manifiesto con AgentDefinitions, skills de tipo AGENT y disparadores.
- Probar un agente con casos de prueba, mapa de actividad y autotune, controlando el costo.
- Publicar en ámbito de usuario o de workspace según el rol y conocer el camino al Security Store.

> **Novedad.** Hay cuatro vías para crear un agente —NL2Agent, agent builder, subir un YAML y las herramientas MCP de creación— y todas convergen en un manifiesto ([desarrollo de agentes](https://learn.microsoft.com/en-us/copilot/security/developer/custom-agent-overview)). NL2Agent figura como «Private Preview, but globally available» en la documentación del 4 de junio de 2026: planifica como si fuera una vista previa ([NL2Agent](https://learn.microsoft.com/en-us/copilot/security/developer/build-agent-natural-language)).

> **Atención.** Crear (con NL2Agent, el builder o MCP) y publicar no consumen SCU; probar siempre consume ([costos del desarrollo de agentes](https://learn.microsoft.com/en-us/copilot/security/developer/cost-considerations)). La optimización automática de instrucciones (autotune) solo funciona en regiones de EE. UU. y la UE, y publicar con el mismo nombre sobrescribe la versión anterior ([probar agentes](https://learn.microsoft.com/en-us/copilot/security/developer/test-agent-dev)).

> **Atención.** Según la documentación de Security Copilot, la opción de identidad de agente solo existe para los agentes de Microsoft, así que un agente propio corre con una cuenta de usuario y sus permisos; un blog de Entra afirma, en cambio, que los agentes de Security Copilot reciben Agent ID automáticamente. Diseña con mínimo privilegio y verifica en tu tenant ([agentes de Security Copilot](https://learn.microsoft.com/en-us/copilot/security/agents-overview), [blog de Entra](https://techcommunity.microsoft.com/blog/microsoft-entra-blog/build-ai-agents-for-production-with-secure-identities-from-day-one/4524606)).

> **Consejo Ninja.** Reglas del manifiesto: un solo AgentDefinition por YAML, FetchSkill y ProcessSkill con el espacio de nombres Skillset.Skill y un único esquema de autenticación por agente ([buenas prácticas del manifiesto](https://learn.microsoft.com/en-us/copilot/security/developer/manifest-best-practices)). Dos webinars de la Skilling Series muestran casos reales: uno del equipo de producto ([Building Custom Agents](https://www.youtube.com/watch?v=vPcLa1xy_74)) y otro de un MVP ([Agents That Actually Work](https://www.youtube.com/watch?v=1KsM2k2dP7U)).

**¿Tienes poco tiempo?**

- [Microsoft Security Copilot agent development overview](https://learn.microsoft.com/en-us/copilot/security/developer/custom-agent-overview) · Documentación
- [Build an agent from scratch using the agent builder](https://learn.microsoft.com/en-us/copilot/security/developer/create-agent-dev) · Documentación
- [Test an agent in Microsoft Security Copilot](https://learn.microsoft.com/en-us/copilot/security/developer/test-agent-dev) · Documentación
- [Building Custom Agents: Unlocking Context, Automation, and Scale (Security Copilot Skilling Series)](https://www.youtube.com/watch?v=vPcLa1xy_74) · Webinar

### Documentación, cursos y credenciales

- [Microsoft Security Copilot - Developer content](https://learn.microsoft.com/en-us/copilot/security/developer/) · Documentación · Oficial · Microsoft Learn. Índice oficial de la documentación para desarrolladores: planificación, manifiesto, changelog, creación de agentes, plugins, muestras, pruebas y publicación.
- [Set up and authenticate the Microsoft Sentinel MCP server (agent creation tools)](https://learn.microsoft.com/en-us/copilot/security/developer/mcp-get-started) · Documentación · Oficial · Vista previa · Nuevo · Microsoft Learn · 4 jun 2026. Configura la colección de creación de agentes del MCP de Sentinel en VS Code con GitHub Copilot en modo agente y aporta el archivo de contexto con las cinco herramientas (start_agent_creation, compose_agent, search_for_tools, get_evaluation, deploy_agent). *Nota:* Endpoint de servicio: sentinel.microsoft.com/mcp/security-copilot-agent-creation (sensible a mayúsculas)
- [Build Security Copilot agents using natural language prompts (Preview)](https://learn.microsoft.com/en-us/copilot/security/developer/build-agent-natural-language) · Documentación · Oficial · Vista previa · Nuevo · Microsoft Learn · 4 jun 2026. Muestra NL2Agent: describir el agente en lenguaje natural para que Security Copilot proponga herramientas e instrucciones y genere el YAML, que luego se termina en el agent builder. *Nota:* La página indica 'Private Preview, but globally available'
- [Microsoft Security Copilot agent development overview](https://learn.microsoft.com/en-us/copilot/security/developer/custom-agent-overview) · Documentación · Oficial · Vista previa · Nuevo · Microsoft Learn · 26 may 2026. Presenta los componentes de un agente (herramientas, disparadores, orquestadores, instrucciones, feedback), las vías de creación (NL2Agent, agent builder, YAML, MCP) y los permisos de publicación por rol. *Nota:* Contributor publica en ámbito de usuario; Owner publica en ámbito de workspace
- [Agent manifest](https://learn.microsoft.com/en-us/copilot/security/developer/agent-manifest) · Documentación · Oficial · Vista previa · Microsoft Learn. Referencia del manifiesto de agente con sus tres claves (Descriptor, AgentDefinitions, SkillGroups), formatos de skill, disparadores FetchSkill/ProcessSkill y autenticación. *Nota:* Ejemplo oficial con modelo gpt-4.1 y skills GPT, KQL y API combinadas
- [Publish a custom agent](https://learn.microsoft.com/en-us/copilot/security/developer/publish-agent-dev) · Documentación · Oficial · Vista previa · Microsoft Learn. Explica la publicación de un agente en ámbito de usuario o workspace con validaciones automáticas y la opción de publicarlo en Security Store para partners.
- [Test an agent in Microsoft Security Copilot](https://learn.microsoft.com/en-us/copilot/security/developer/test-agent-dev) · Documentación · Oficial · Vista previa · Microsoft Learn. Describe el ciclo de prueba con entradas de ejemplo, el mapa de actividad, la optimización automática de instrucciones (autotune), el versionado por nombre y la edición o borrado. *Nota:* Autotune solo en regiones de EE. UU. y UE; probar consume SCU
- [Build an agent from scratch using the agent builder](https://learn.microsoft.com/en-us/copilot/security/developer/create-agent-dev) · Documentación · Oficial · Vista previa · Microsoft Learn. Guía del formulario del agent builder (detalles, instrucciones, entradas, herramientas del catálogo incluido MCP.Sentinel, automatización y permisos) con chat asistido.
- [Quickstart: Build agents using MCP tools](https://learn.microsoft.com/en-us/copilot/security/developer/mcp-quickstart) · Documentación · Oficial · Vista previa · Microsoft Learn · 28 ene 2026. Inicio rápido para generar con GitHub Copilot el YAML de un agente de informe post-incidente (Defender, Purview, Sentinel), desplegarlo en ámbito de usuario o workspace y probarlo. *Nota:* Versión en español:
- [Cost considerations for Security Copilot (agent development)](https://learn.microsoft.com/en-us/copilot/security/developer/cost-considerations) · Documentación · Oficial · Vista previa · Microsoft Learn · 30 sep 2025. Tabla que aclara que crear (NL2Agent, builder, MCP) y publicar agentes no consume SCU, mientras que probarlos siempre consume.
- [Publish your Microsoft Security Copilot agent to the Microsoft Security Store](https://learn.microsoft.com/en-us/azure/sentinel/isv/publish-agent-to-security-store) · Documentación · Oficial · Microsoft Learn. Explica cómo empaquetar (PackageManifest.yaml + AgentManifest.yaml), crear la oferta SaaS en Partner Center y certificar un agente para el Security Store usando el ejemplo IdentityDrift.
- [Create an agent tool using Security Copilot tool types](https://learn.microsoft.com/en-us/copilot/security/developer/create-agent-tool) · Documentación · Oficial · Vista previa · Nuevo · Microsoft Learn · 4 jun 2026. Explica cómo crear herramientas GPT y KQL (Defender, Sentinel, Kusto) desde el agent builder con entradas parametrizadas {{Input}} y plantillas inline, URL o paquete. *Nota:* API y MCP se crean como plugins aparte
- [Security Copilot Agent Manifest Best Practices](https://learn.microsoft.com/en-us/copilot/security/developer/manifest-best-practices) · Documentación · Oficial · Vista previa · Nuevo · Microsoft Learn · 1 jun 2026. Reglas prácticas del manifiesto: un único AgentDefinition, FetchSkill/ProcessSkill con espacio de nombres, ChildSkills y RequiredSkillsets coherentes y un solo esquema de autenticación por agente.
- [Build Security Copilot agents in the standalone experience](https://learn.microsoft.com/en-us/copilot/security/developer/agent-standalone-overview) · Documentación · Oficial · Vista previa · Microsoft Learn. Punto de entrada a la sección Build del portal independiente con las tres vías de creación de agentes y el enlace a la guía de planificación.
- [Build a Security Copilot agent using the YAML manifest](https://learn.microsoft.com/en-us/copilot/security/developer/build-agent-manifest) · Documentación · Oficial · Vista previa · Microsoft Learn. Pasos para crear el YAML, subirlo como plugin personalizado, revisar permisos, descubrir y configurar el agente y probarlo. *Nota:* Solo se publica como agente si el YAML incluye AgentDefinitions; el Owner debe permitir plugins personalizados
- [Build Security Copilot agents with an interactive chat experience](https://learn.microsoft.com/en-us/copilot/security/developer/build-interactive-agents) · Documentación · Oficial · Vista previa · Microsoft Learn. Tutorial para crear un agente interactivo (Chat with agent) con PromptSkill, interfaz InteractiveAgent, prompts sugeridos y el MCP de Microsoft Docs como herramienta.
- [Model Context Protocol overview (Security Copilot agent creation)](https://learn.microsoft.com/en-us/copilot/security/developer/mcp-overview) · Documentación · Oficial · Vista previa · Microsoft Learn · 4 nov 2025. Presenta las herramientas MCP de creación de agentes (descubrir skills, autogenerar YAML, desplegar en ámbito usuario/workspace) dentro del servidor MCP de Sentinel.

### Webinars, videos y podcasts

- [Agents That Actually Work: From an MVP (Skilling Series)](https://www.youtube.com/watch?v=1KsM2k2dP7U) · Webinar · MVP · Ugur Koc · Microsoft Security Community (YouTube) · 19 feb 2026. Webinar de un MVP sobre cómo pasar de una idea a un agente fiable: iterar objetivos e instrucciones, elegir herramientas y validar decisiones con evidencia (lenguaje natural, Agent Builder y YAML).
- [Building Custom Agents: Unlocking Context, Automation, and Scale (Security Copilot Skilling Series)](https://www.youtube.com/watch?v=vPcLa1xy_74) · Webinar · Empleado de Microsoft · Innocent Wafula; Sean Wesonga · YouTube - Microsoft Security Community · 22 ene 2026. Webinar de 50 min que muestra cómo el agent builder y los servidores MCP permiten crear agentes personalizados con contexto propio, con demostración práctica.

### Laboratorios, GitHub y herramientas

- [Security Copilot Custom Plugins & Agents Builder (skill para GitHub Copilot)](https://github.com/mariocuomo/Experimenting-With-Security-Copilot/blob/main/Security%20Copilot%20custom%20plugins%20builder/README.md) · GitHub · Empleado de Microsoft · Mario Cuomo · GitHub (mariocuomo). Skill comunitaria para GitHub Copilot que guía la generación y validación de manifiestos YAML de plugins y agentes (KQL, API, GPT, LogicApp, MCP, Agent) usando herramientas MCP de Sentinel.

**Manos a la obra**

1. `Laboratorio parcial` Con el [agent builder](https://learn.microsoft.com/en-us/copilot/security/developer/create-agent-dev), crea un agente de triage para un tipo de alerta de tu SOC: instrucciones, una entrada {{IncidentId}}, herramientas mínimas (del catálogo filtrado por Publisher: MCP.Sentinel y la skill KQL de [A2](#a2)) y disparador manual; exporta el manifiesto. Limitación: probar consume SCU. Evidencia: agente creado y manifiesto exportado en Git.
2. `Laboratorio parcial` Describe el mismo agente con [NL2Agent](https://learn.microsoft.com/en-us/copilot/security/developer/build-agent-natural-language), termínalo en el builder y compara ambos manifiestos ([estructura del manifiesto](https://learn.microsoft.com/en-us/copilot/security/developer/agent-manifest)): instrucciones, ChildSkills y disparadores. Limitación: estado ambiguo de vista previa y SCU al probar. Evidencia: comparación de manifiestos.
3. `Laboratorio parcial` Sigue el [quickstart de creación con MCP](https://learn.microsoft.com/en-us/copilot/security/developer/mcp-quickstart) desde Visual Studio Code (agente de informe post-incidente) con start_agent_creation, compose_agent y deploy_agent en ámbito User, y verifica que agentSkillsetName coincida exactamente con Descriptor: Name ([configurar el servidor MCP](https://learn.microsoft.com/en-us/copilot/security/developer/mcp-get-started)). Limitación: licencia de GitHub Copilot y SCU al probar. Evidencia: agente desplegado en ámbito de usuario.
4. `Laboratorio parcial` Prueba tu agente con diez casos con resultado esperado, incluidos casos adversos (entrada vacía, incidente inexistente y un texto con instrucciones ocultas); usa el mapa de actividad y, si tu región lo permite, la optimización automática de instrucciones, y registra las SCU de cada prueba ([probar agentes](https://learn.microsoft.com/en-us/copilot/security/developer/test-agent-dev)). Limitación: cada prueba consume SCU. Evidencia: tabla de pruebas del agente.
5. `Laboratorio parcial` [Publica](https://learn.microsoft.com/en-us/copilot/security/developer/publish-agent-dev) el agente en ámbito de usuario y comprueba que una nueva publicación con el mismo nombre sobrescribe la anterior; pide a un owner que lo publique para el workspace solo después de revisar herramientas, permisos y resultados de las pruebas. Limitación: consumo de SCU al ejecutar. Evidencia: agente publicado en ámbito de usuario y acta de revisión del owner.
6. `Solo producción` Publica un agente propio en el workspace productivo. Cómo hacerlo seguro: herramientas mínimas, cuenta de ejecución con permisos de solo lectura salvo justificación, piloto con un grupo de analistas, revisión de cada ejecución durante la primera semana, umbral de costo y procedimiento para eliminarlo desde Manage sources. Evidencia: ficha de gobierno del agente aprobada.

**¿Quieres profundizar?**

- [Agents That Actually Work: From an MVP (Skilling Series)](https://www.youtube.com/watch?v=1KsM2k2dP7U) · Webinar
- [Security Copilot Custom Plugins & Agents Builder (skill para GitHub Copilot)](https://github.com/mariocuomo/Experimenting-With-Security-Copilot/blob/main/Security%20Copilot%20custom%20plugins%20builder/README.md) · GitHub

<a id="a5"></a>

## A5 · Servidor MCP de Sentinel y herramientas agénticas

*L400 · ~6 h · Origen: Nuevo en esta edición*

El **Model Context Protocol (MCP)** es el estándar abierto con el que los agentes descubren y usan herramientas. El **servidor MCP de Microsoft Sentinel** —en disponibilidad general desde el 18 de noviembre de 2025— es un servicio alojado, sin infraestructura propia y con identidad de Entra, que expone **colecciones** de herramientas: **exploración de datos** del data lake (buscar tablas, ejecutar KQL, el *entity analyzer* y herramientas de grafo en vista previa), **triage** de incidentes, alertas y búsqueda avanzada, y **creación de agentes** de Security Copilot. Se usa desde Security Copilot, Visual Studio Code con GitHub Copilot, Copilot Studio, Microsoft Foundry y, con conectores en vista previa, ChatGPT y Claude.

Las **herramientas personalizadas** (vista previa) convierten una consulta de la búsqueda avanzada en una herramienta MCP con un clic, y las **colecciones personalizadas** se publican en su propio endpoint para que tus agentes usen KQL revisado en lugar de generarlo. Cada colección tiene requisitos y límites: la mayoría de las herramientas exigen el data lake, la colección de triage solo funciona en tu propio tenant y no consulta el lake, y para listar e invocar herramientas basta Security Reader. El data lake y el detalle de cada colección se profundizan en el programa de Sentinel (módulos A8 y X6).

**Por qué importa**

MCP convierte tus datos de seguridad en herramientas que cualquier agente aprobado puede usar con los permisos de la persona, en lugar de construir una integración por cliente. Las herramientas personalizadas encapsulan tus mejores consultas de caza, de modo que los agentes trabajen con KQL validado y el costo de las consultas sea predecible.

**Qué vas a lograr**

- Explicar el servidor MCP de Sentinel, sus colecciones y sus requisitos de data lake y roles.
- Conectar Visual Studio Code con GitHub Copilot a las colecciones de triage y exploración de datos.
- Crear herramientas MCP personalizadas desde la búsqueda avanzada y publicar colecciones propias.
- Usar herramientas MCP de Sentinel desde agentes de Security Copilot y otros clientes.
- Aplicar controles de seguridad y costo al exponer datos del SOC a agentes.

> **Novedad.** El servidor MCP de Sentinel entró en vista previa pública el 30 de septiembre de 2025 y en disponibilidad general el 18 de noviembre de 2025, con integración nativa en Security Copilot, Visual Studio Code con GitHub Copilot, Copilot Studio y Foundry ([blog de GA](https://techcommunity.microsoft.com/blog/microsoft-security-blog/microsoft-sentinel-mcp-server---generally-available-with-exciting-new-capabiliti/4470125)). Sus colecciones (documentación del 14 de mayo de 2026) son exploración de datos, creación de agentes de Security Copilot y triage ([colecciones](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-mcp-tools-overview)).

> **Atención.** La mayoría de las herramientas exigen el data lake; para listar e invocar herramientas basta Security Reader, y desactivar el acceso requiere contactar a soporte ([primeros pasos](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-mcp-get-started)). La colección de triage solo funciona en tu propio tenant —no como invitado ni con acceso delegado—, no permite elegir el workspace de Sentinel y no consulta el data lake ([triage](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-mcp-triage-tool)).

> **Novedad.** Las herramientas personalizadas (vista previa) se crean con Save as tool desde la búsqueda avanzada, con Security Operator, Security Admin o Global Admin, y se usan con Security Reader o Global Reader ([herramientas personalizadas](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-mcp-create-custom-tool)). Una colección personalizada se sube a Security Copilot como plugin `Format: MCP` con el TokenScope de Sentinel y UsePluginAuth en false (documentación del 8 de agosto de 2026) ([MCP en Security Copilot](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-mcp-use-tool-security-copilot)).

> **Atención.** Dos puntos a verificar: el entity analyzer se anunció sin cargo adicional, pero las novedades de RSAC 2026 indican facturación en SCU desde el 1 de abril de 2026; y, tras el onboarding integrado del 23 de septiembre de 2026, un experto de la comunidad reportó que la colección de exploración no respondía en tenants nuevos ([novedades de RSAC 2026](https://techcommunity.microsoft.com/blog/microsoftsentinelblog/what%E2%80%99s-new-in-microsoft-sentinel-rsac-2026/4503971), [reporte comunitario](https://tokesi.cloud/blogs/26_09_28_integrated_data_lake/)). El data lake se profundiza en el programa de Sentinel (módulos A8 y X6).

**¿Tienes poco tiempo?**

- [What is Microsoft Sentinel's support for Model Context Protocol (MCP)?](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-mcp-overview) · Documentación
- [Tool collection in Microsoft Sentinel MCP server](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-mcp-tools-overview) · Documentación
- [Create and use custom Microsoft Sentinel MCP tools (preview)](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-mcp-create-custom-tool) · Documentación
- [Use Microsoft Sentinel MCP tools in Microsoft Security Copilot](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-mcp-use-tool-security-copilot) · Documentación

### Documentación, cursos y credenciales

- [Use Microsoft Sentinel MCP tools in Microsoft Security Copilot](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-mcp-use-tool-security-copilot) · Documentación · Oficial · Nuevo · Microsoft Learn · 8 ago 2026. Muestra cómo añadir herramientas MCP de Sentinel a un agente personalizado y cómo empaquetar una colección propia como plugin YAML Format: MCP con TokenScope de Sentinel.
- [Use an MCP tool in Visual Studio Code](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-mcp-use-tool-visual-studio-code) · Documentación · Oficial · Nuevo · Microsoft Learn · 1 jul 2026. Guía corta para añadir una colección de Sentinel o una colección personalizada como servidor MCP HTTP en VS Code y usarla en el modo agente de GitHub Copilot.
- [Prioritize incidents and hunt for threats with triage collection](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-mcp-triage-tool) · Documentación · Oficial · Nuevo · Microsoft Learn · 18 jun 2026. Referencia de las herramientas de la colección de triage (incidentes, alertas, Advanced hunting, archivos, IP, dispositivos, vulnerabilidades e indicadores) con parámetros y limitaciones.
- [Tool collection in Microsoft Sentinel MCP server](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-mcp-tools-overview) · Documentación · Oficial · Nuevo · Microsoft Learn · 14 may 2026. Lista las colecciones oficiales y sus endpoints (data-exploration, security-copilot-agent-creation, triage) y presenta las herramientas personalizadas basadas en KQL guardado.
- [Get started with Microsoft Sentinel MCP server](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-mcp-get-started) · Documentación · Oficial · Nuevo · Microsoft Learn · 7 may 2026. Requisitos (data lake, Defender, rol Security Reader), clientes compatibles y prompts de prueba para empezar a usar las herramientas MCP de Sentinel.
- [What is Microsoft Sentinel's support for Model Context Protocol (MCP)?](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-mcp-overview) · Documentación · Oficial · Microsoft Learn. Visión general del servidor MCP alojado de Sentinel con identidad de Entra, sus colecciones por escenario y casos de uso (exploración de datos, análisis de entidades, creación de agentes, triage y hunting).
- [Explore Microsoft Sentinel data lake with data exploration collection](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-mcp-data-exploration-tool) · Documentación · Oficial · Microsoft Learn. Detalla search_tables, ejecución de KQL en el lake, listado de workspaces, entity analyzer y herramientas de grafo (exposición, hunting y riesgo de datos) con sus requisitos.
- [Create and use custom Microsoft Sentinel MCP tools (preview)](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-mcp-create-custom-tool) · Documentación · Oficial · Vista previa · Nuevo · Microsoft Learn · 14 may 2026. Explica cómo guardar consultas KQL de Advanced hunting o del data lake como herramientas MCP con parámetros {Param}, colecciones propias y buenas prácticas de descripción. *Nota:* Crear: Security Operator/Security Admin/Global Admin; usar: Security Reader/Global Reader
- [Use the Microsoft Sentinel MCP connector in ChatGPT or Claude (preview)](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-mcp-chatgpt-claude-connector) · Documentación · Oficial · Vista previa · Microsoft Learn. Pasos para registrar una app de Entra con SentinelPlatform.DelegatedAccess y crear un conector MCP personalizado de Sentinel en ChatGPT o Claude. *Nota:* Requiere planes ChatGPT Pro o Claude Pro/Max/Team/Enterprise y privilegios de administración del tenant
- [Overview of Microsoft MCP Server for Enterprise (preview)](https://learn.microsoft.com/en-us/graph/mcp-server/overview) · Documentación · Oficial · Vista previa · Microsoft Learn. Describe el servidor MCP de Microsoft Graph para consultas de solo lectura sobre Entra (usuarios, grupos, apps, dispositivos) desde agentes, útil como complemento al MCP de Sentinel. *Nota:* Sin coste adicional; respeta permisos de Graph; solo nube global

### Anuncios y blogs oficiales

- [Microsoft Sentinel MCP server - Generally Available With Exciting New Capabilities](https://techcommunity.microsoft.com/blog/microsoft-security-blog/microsoft-sentinel-mcp-server---generally-available-with-exciting-new-capabiliti/4470125) · Blog oficial · Empleado de Microsoft · Omri Amdursky · Microsoft Security Community Blog · 18 nov 2025. Anuncio de GA del servidor MCP de Sentinel con integración nativa en Copilot Studio y Foundry, conexión con ChatGPT, herramientas KQL personalizadas, entity analyzer, grafo y triage.

### Webinars, videos y podcasts

- [Microsoft Sentinel | AI-Powered Entity Analysis in Sentinel's MCP Server](https://www.youtube.com/watch?v=adQ3Q38pPZ8) · Webinar · Empleado de Microsoft · Alexander Kolmann; Matt Lichtinger · YouTube - Microsoft Security Community · 27 ene 2026. Sesión técnica sobre el servidor MCP de Sentinel y el entity analyzer, incluida su integración con Logic Apps para enriquecer entidades.

**Manos a la obra**

1. `Laboratorio parcial` Conecta Visual Studio Code con GitHub Copilot a la colección de triage ([usar MCP en Visual Studio Code](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-mcp-use-tool-visual-studio-code)), lista incidentes, ejecuta una consulta de búsqueda avanzada y verifica con una cuenta de menos permisos que el servidor respeta los permisos del usuario. Limitación: requiere licencia de GitHub Copilot y la colección de triage solo funciona en tu propio tenant. Evidencia: transcripción de la sesión con ambas cuentas.
2. `Laboratorio parcial` Guarda una consulta de la búsqueda avanzada como [herramienta MCP personalizada](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-mcp-create-custom-tool) con el rol Security Operator y úsala desde Visual Studio Code y desde el agente que creaste en [A4](#a4). Limitación: vista previa y consumo de SCU en el agente. Evidencia: herramienta MCP personalizada usada desde ambos clientes.
3. `Laboratorio parcial` Con el data lake incorporado, usa la [colección de exploración](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-mcp-data-exploration-tool): busca tablas, ejecuta KQL en el lake y analiza una entidad con el entity analyzer; anota el costo de cada paso (consultas del lake y SCU). Limitación: requiere el data lake y, en tenants incorporados después del 23 de septiembre de 2026, la colección podría no responder. Evidencia: registro de pasos con su costo estimado.
4. `Laboratorio parcial` Publica una colección personalizada y súbela a Security Copilot como plugin `Format: MCP` siguiendo [MCP de Sentinel en Security Copilot](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-mcp-use-tool-security-copilot); pruébala con un prompt. Limitación: vista previa y consumo de SCU. Evidencia: plugin cargado y una respuesta que usa la herramienta.
5. `Laboratorio` Escribe el modelo de amenazas del servidor MCP en tu organización: quién puede invocar qué herramientas, qué datos devuelve cada una, riesgos de envenenamiento de descripciones y de inyección en los datos, y cómo se desactiva (requiere soporte) ([qué es el MCP de Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-mcp-overview)). Evidencia: tabla de riesgos y controles.
6. `Solo producción` Evalúa el [conector para ChatGPT o Claude](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-mcp-chatgpt-claude-connector), en vista previa, que requiere planes pagos de esos servicios y una aplicación de Entra registrada. Cómo hacerlo seguro: decisión previa de privacidad sobre el envío de datos de seguridad a un tercero, usuarios piloto con Security Reader, consentimiento de la aplicación revisado y revocación probada. Evidencia: análisis de riesgo aprobado o rechazado con fundamentos.

**¿Quieres profundizar?**

- [Microsoft Sentinel | AI-Powered Entity Analysis in Sentinel's MCP Server](https://www.youtube.com/watch?v=adQ3Q38pPZ8) · Webinar

<a id="a6"></a>

## A6 · Power Platform y Copilot Studio

*L400 · ~6 h · Origen: Nuevo en esta edición*

Power Platform conecta a Security Copilot con el resto del negocio. El **conector de Security Copilot** —en disponibilidad general en Copilot Studio desde mayo de 2025 y disponible también en Power Automate y Power Apps, salvo nubes de gobierno— permite que un flujo, un flujo de agente o un agente de **Copilot Studio** envíe prompts, ejecute promptbooks o dispare agentes de Security Copilot: por ejemplo, un agente en Teams que responde «¿este correo es phishing?» con el análisis de Copilot detrás, o una aprobación que llega al responsable con el resumen del incidente. En sentido inverso, un agente de Copilot Studio puede usar las **herramientas MCP de Sentinel** (vista previa) con autenticación integrada de Entra.

Cada agente de Copilot Studio es también una superficie de ataque que el SOC debe gobernar. Las **directivas de datos** de Power Platform son obligatorias para todos los tenants desde principios de 2025 y permiten exigir autenticación y bloquear HTTP, conectores, canales, fuentes de conocimiento y disparadores; la **protección en tiempo real** de Defender (que requiere Agent 365) y los controles de **Purview** —DSPM, auditoría, etiquetas, DLP, riesgo interno y eDiscovery— completan la defensa. Las identidades de estos agentes se profundizan en el programa de Entra (módulo X6).

**Por qué importa**

Muchas consultas que llegan al SOC vienen del negocio. Un agente de Copilot Studio con Security Copilot detrás, gobernado por directivas de datos, reduce tickets y tiempos de respuesta; sin gobierno, cada agente creado por un desarrollador ciudadano es un canal nuevo de fuga de datos o de inyección de prompts.

**Qué vas a lograr**

- Usar el conector de Security Copilot en Power Automate, Power Apps y Copilot Studio.
- Agregar herramientas MCP de Sentinel a un agente de Copilot Studio con la autenticación correcta.
- Aplicar directivas de datos de Power Platform a agentes: autenticación, HTTP, canales y conectores.
- Habilitar la protección en tiempo real de Defender y los controles de Purview para agentes de Copilot Studio.
- Explicar cómo interoperan los agentes de Security Copilot y los de Copilot Studio.

> **Novedad.** El conector de Security Copilot para Copilot Studio está en disponibilidad general desde mayo de 2025 ([What's new](https://learn.microsoft.com/en-us/copilot/security/whats-new-copilot-security)) y la referencia lo ofrece en Copilot Studio, Power Automate y Power Apps, salvo en nubes de gobierno ([referencia del conector](https://learn.microsoft.com/en-us/connectors/securitycopilot/)). Las herramientas MCP de Sentinel en Copilot Studio están en vista previa, usan autenticación Microsoft Entra ID Integrated para las colecciones oficiales y se recomienda GPT-5 o superior ([MCP de Sentinel en Copilot Studio](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-mcp-use-tool-copilot-studio)).

> **Atención.** Las directivas de datos de Power Platform son obligatorias para todos los tenants desde principios de 2025 (MC973179), sin exenciones para agentes; permiten exigir autenticación —bloqueando el chat sin autenticación de Entra— y bloquear fuentes de conocimiento, conectores, HTTP, canales y disparadores ([directivas de datos para agentes](https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-data-loss-prevention)).

> **Atención.** La detección externa en tiempo de ejecución de Copilot Studio solo aplica a agentes con orquestación generativa y la documentación la marca como vista previa, aunque el plan de lanzamiento preveía la GA en junio de 2026 ([protección externa](https://learn.microsoft.com/en-us/microsoft-copilot-studio/external-security-provider)). La protección de Defender requiere Agent 365, Security Administrator y un administrador de Power Platform que use el mismo App ID; sin el conector de Microsoft 365, bloquea pero no genera alertas ([Defender para agentes](https://learn.microsoft.com/en-us/defender-xdr/security-for-ai/get-started-defender-security-for-ai)).

> **Consejo Ninja.** Licencias de gobierno: los controles básicos vienen con A3, E3 o G3 y los optimizados (DSPM for AI, riesgo interno y Defender for Cloud Apps), con A5, E5 o G5 ([controles de seguridad y gobierno](https://learn.microsoft.com/en-us/copilot/implement/copilot-controls-security-governance)). En Purview, los agentes publicados en canales que no son de Microsoft requieren facturación pay-as-you-go ([Purview para Copilot Studio](https://learn.microsoft.com/en-us/purview/ai-copilot-studio)). Las identidades de estos agentes se profundizan en el programa de Entra (módulo X6).

**¿Tienes poco tiempo?**

- [Microsoft Security Copilot (Preview) - Connectors reference](https://learn.microsoft.com/en-us/connectors/securitycopilot/) · Documentación
- [Add Microsoft Sentinel MCP tools to AI agents in Microsoft Copilot Studio (preview)](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-mcp-use-tool-copilot-studio) · Documentación
- [Configure data policies for agents (Copilot Studio)](https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-data-loss-prevention) · Documentación
- [Key concepts - Copilot Studio security and governance](https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance) · Documentación

### Documentación, cursos y credenciales

- [Key concepts - Copilot Studio security and governance](https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance) · Documentación · Oficial · Microsoft Learn. Catálogo de controles de seguridad y gobierno de Copilot Studio: directivas de datos, enrutamiento de entornos, auditoría en Purview y Sentinel, escaneo de seguridad previo a publicar, protección en tiempo de ejecución y Agent 365 como plano de control.
- [Configure data policies for agents (Copilot Studio)](https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-data-loss-prevention) · Documentación · Oficial · Microsoft Learn. Explica cómo usar directivas de datos (DLP) del Power Platform admin center para exigir autenticación, bloquear fuentes de conocimiento, conectores, HTTP, canales y disparadores en agentes de Copilot Studio.
- [Microsoft Security Copilot (Preview) - Connectors reference](https://learn.microsoft.com/en-us/connectors/securitycopilot/) · Documentación · Oficial · Vista previa · Microsoft Learn. Referencia del conector para Logic Apps, Power Automate, Power Apps y Copilot Studio con acciones de prompt (incluida V2 en preview), promptbook, estado de evaluación y Execute a Security Copilot Agent. *Nota:* No disponible en GCC/GCC High/DoD/China; límite 600 llamadas por minuto por conexión; auth Default marcada como DEPRECATED; menciona aún el antiguo Early Access Program
- [Add Microsoft Sentinel MCP tools to AI agents in Microsoft Copilot Studio (preview)](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-mcp-use-tool-copilot-studio) · Documentación · Oficial · Vista previa · Microsoft Learn. Paso a paso para añadir colecciones de Sentinel (auth Entra ID integrada) o colecciones personalizadas (app de Entra con OAuth manual) a agentes de Copilot Studio. *Nota:* Recomienda GPT-5 o superior para mejor rendimiento con herramientas MCP
- [Enable external threat detection and protection for Copilot Studio custom agents (preview)](https://learn.microsoft.com/en-us/microsoft-copilot-studio/external-security-provider) · Documentación · Oficial · Vista previa · Microsoft Learn. Describe el modelo 'trae tu propia protección' que envía cada invocación de herramienta a un sistema externo (Defender u otro) para aprobarla o bloquearla en tiempo real, y qué datos se comparten. *Nota:* Solo agentes con orquestación generativa; los agentes ya traen protección integrada contra UPIA y XPIA
- [Govern data policies in Power Platform (training module)](https://learn.microsoft.com/en-us/training/modules/govern-data-policies/) · Curso · Oficial · Microsoft Learn. Módulo de 1 h 22 min con ejercicio para diseñar una estrategia de directivas de datos por capas que incluya agentes de Copilot Studio.
- [Use Microsoft Purview to manage data security & compliance for Microsoft Copilot Studio](https://learn.microsoft.com/en-us/purview/ai-copilot-studio) · Documentación · Oficial · Microsoft Learn. Tabla de capacidades de Purview (DSPM, auditoría, etiquetas, DLP, IRM, eDiscovery) soportadas para interacciones con agentes de Copilot Studio y pasos recomendados.
- [Strengthen security of Copilot Studio agents with additional threat protection (release plan)](https://learn.microsoft.com/en-ca/power-platform/release-plan/2025wave1/microsoft-copilot-studio/strengthen-security-copilot-studio-agents-additional-threat-protection) · Documentación · Oficial · Microsoft Learn · 17 mar 2026. Entrada del plan de lanzamiento que fecha la preview pública de la protección externa en tiempo de ejecución (4-sep-2025) y su GA prevista para junio de 2026.
- [Build a runtime threat detection system for Copilot Studio agents](https://learn.microsoft.com/en-us/microsoft-copilot-studio/external-security-webhooks-interface-developers) · Documentación · Oficial · Microsoft Learn. Especificación para desarrolladores de los endpoints /validate y /analyze-tool-execution que un proveedor de seguridad debe exponer para aprobar o bloquear herramientas de agentes.

**Manos a la obra**

1. `Laboratorio parcial` Crea un flujo de Power Automate que reciba una consulta desde Teams, la envíe con el [conector de Security Copilot](https://learn.microsoft.com/en-us/connectors/securitycopilot/) (Submit a Security Copilot prompt) y publique la respuesta en el canal, con una aprobación antes de responder fuera del equipo de seguridad. Limitación: SCU por llamada y licencias de Power Platform. Evidencia: flujo con el conector de Security Copilot y una ejecución completa.
2. `Laboratorio parcial` Agrega las [herramientas MCP de Sentinel a un agente de Copilot Studio](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-mcp-use-tool-copilot-studio) con autenticación Microsoft Entra ID Integrated, haz tres preguntas sobre incidentes y verifica que respeta los permisos del usuario. Limitación: vista previa y licencia o prueba de Copilot Studio. Evidencia: conversación con el agente y su configuración.
3. `Laboratorio parcial` En un entorno piloto, crea una [directiva de datos](https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-data-loss-prevention) que bloquee el chat sin autenticación de Entra y el conector HTTP, y verifica qué le pasa a un agente que los usaba. Limitación: requiere un administrador de Power Platform y un entorno dedicado. Evidencia: directiva de datos aplicada a un agente y el error que muestra.
4. `Laboratorio parcial` Revisa en Purview la auditoría y DSPM for AI de las interacciones con tu agente de Copilot Studio ([Purview para Copilot Studio](https://learn.microsoft.com/en-us/purview/ai-copilot-studio)). Limitación: algunas directivas usan facturación pay-as-you-go. Evidencia: eventos de auditoría de tres interacciones.
5. `Laboratorio` Dibuja el mapa de interoperabilidad: cómo un agente de Copilot Studio o un flujo llama a Security Copilot (prompt, promptbook o agente) y cómo un agente de Security Copilot usa herramientas (MCP, plugins y Logic Apps), con la identidad de cada salto y dónde aplican las directivas de datos ([seguridad y gobierno de Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance)). Evidencia: diagrama revisado por el equipo de arquitectura.
6. `Solo producción` Habilita la [protección en tiempo real de Defender](https://learn.microsoft.com/en-us/defender-xdr/security-for-ai/ai-agent-real-time-protection) para agentes de Copilot Studio, que requiere Agent 365 y coordinación con el administrador de Power Platform. Cómo hacerlo seguro: entorno de pruebas aislado, regla por defecto en modo auditoría antes de las reglas de bloqueo, agentes de prueba, un intento controlado de XPIA y reversión documentada. Evidencia: registro del intento en Defender.

<a id="a7"></a>

## A7 · Microsoft Foundry y agentes pro-code

*L400 · ~6 h · Origen: Nuevo en esta edición*

Algunos escenarios del SOC necesitan código: orquestación multiagente, modelos específicos, integración con sistemas internos o publicación en Teams. **Microsoft Foundry** —Azure AI Foundry (nombre anterior)— ofrece con **Foundry Agent Service** agentes de prompt, de voz y alojados, con *toolboxes* expuestos como un endpoint MCP administrado, identidad de Entra, RBAC, filtros de contenido y publicación en Teams, Microsoft Copilot y el registro de agentes de Entra. Foundry crea automáticamente identidades de agente y las usa para herramientas MCP y A2A. Los agentes clásicos están deprecados y se retiran el 31 de marzo de 2027.

El patrón oficial para el SOC es **prototipar en Foundry y llevar a Security Copilot**: diseñar las instrucciones de un agente con la herramienta de exploración del servidor MCP de Sentinel y luego construirlo en el agent builder, como en la serie IdentityDrift. La seguridad se diseña desde el día uno: **Defender for AI Services** (Prompt Shields e inteligencia de amenazas, con prueba de 30 días), recomendaciones de postura que exigen humano en el circuito para acciones de herramientas MCP con riesgo de XPIA, detección de amenazas para agentes publicados y **Purview** para sus datos. Desde el 1 de julio de 2026, descubrir agentes de Foundry en Defender for Cloud requiere Agent 365.

**Por qué importa**

Foundry da control total sobre modelos, herramientas y despliegue, pero cada agente pro-code es una identidad con herramientas y acceso a datos. Construirlo con Defender y Purview desde el primer día evita que el propio SOC genere la IA en la sombra que después tendría que investigar.

**Qué vas a lograr**

- Describir los tipos de agentes de Foundry Agent Service, sus toolboxes MCP y sus canales de publicación.
- Conectar herramientas MCP de Sentinel a un agente de Foundry con OAuth Identity Passthrough.
- Prototipar instrucciones de un agente de seguridad en Foundry y llevarlas a Security Copilot.
- Proteger agentes de Foundry con Defender for AI Services, recomendaciones de postura y Purview.
- Planificar la migración de agentes clásicos antes del 31 de marzo de 2027.

> **Qué cambió.** Azure AI Foundry (nombre anterior) hoy es Microsoft Foundry; la serie IdentityDrift todavía usa el nombre anterior. Los agentes clásicos de Foundry están deprecados y se retiran el 31 de marzo de 2027 ([herramientas de agentes clásicos](https://learn.microsoft.com/en-us/azure/foundry-classic/agents/how-to/tools-classic/overview)).

> **Novedad.** Foundry Agent Service ofrece agentes de prompt, de voz y alojados, con toolboxes expuestos como un endpoint MCP administrado, identidad de Entra, RBAC, filtros de contenido y publicación en Teams, Microsoft Copilot y el registro de agentes de Entra ([Foundry Agent Service](https://learn.microsoft.com/en-us/azure/foundry/agents/overview)). Foundry crea identidades de agente —un blueprint por proyecto y por agente publicado— y las usa para herramientas MCP y A2A ([gobierno de identidades de agente](https://learn.microsoft.com/en-us/entra/id-governance/agent-id-governance-overview)).

> **Atención.** Defender for AI Services está en disponibilidad general con Prompt Shields e inteligencia de amenazas: es un plan pago con prueba de 30 días (hasta 75.000 millones de tokens), solo analiza tokens de texto y no está disponible en Azure Government ([protección de IA](https://learn.microsoft.com/en-us/azure/defender-for-cloud/ai-threat-protection)). Desde el 1 de julio de 2026, descubrir agentes de Foundry y de terceros en Defender for Cloud requiere Agent 365 ([postura de seguridad de IA](https://learn.microsoft.com/en-us/azure/defender-for-cloud/ai-security-posture)).

> **Consejo Ninja.** Una recomendación de postura pide que los agentes de Foundry con riesgo de XPIA exijan humano en el circuito para las acciones de herramientas MCP ([recomendaciones de IA](https://learn.microsoft.com/en-us/azure/defender-for-cloud/recommendations-reference-ai)). Para Purview, activa Data Security desde Foundry Control Plane o Defender for Cloud; las directivas usan pay-as-you-go y la auditoría está incluida ([Purview para Foundry](https://learn.microsoft.com/en-us/purview/ai-azure-foundry)).

**¿Tienes poco tiempo?**

- [What is Microsoft Foundry Agent Service?](https://learn.microsoft.com/en-us/azure/foundry/agents/overview) · Documentación
- [Use Microsoft Sentinel MCP tools in Microsoft Foundry (preview)](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-mcp-use-tool-azure-ai-foundry) · Documentación
- [AI threat protection in Microsoft Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/ai-threat-protection) · Documentación

### Documentación, cursos y credenciales

- [AI threat protection in Microsoft Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/ai-threat-protection) · Documentación · Oficial · Nuevo · Microsoft Learn · 17 jun 2026. Protección GA para cargas de IA generativa en Azure (Prompt Shields + inteligencia de amenazas) con alertas de jailbreak, fuga de datos o robo de credenciales integradas en Defender XDR.
- [What is Microsoft Foundry Agent Service?](https://learn.microsoft.com/en-us/azure/foundry/agents/overview) · Documentación · Oficial · Microsoft Learn. Visión general de Foundry Agent Service (prompt agents, hosted agents, toolboxes con endpoint MCP gestionado, observabilidad, Entra Agent ID y publicación) para agentes pro-code.
- [Use Microsoft Sentinel MCP tools in Microsoft Foundry (preview)](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-mcp-use-tool-azure-ai-foundry) · Documentación · Oficial · Vista previa · Microsoft Learn. Muestra cómo conectar colecciones de Sentinel o personalizadas a un agente de Microsoft Foundry con OAuth Identity Passthrough. *Nota:* Antes Azure AI Foundry; el endpoint personalizado sigue el formato sentinel.microsoft.com/mcp/custom/<colección>
- [Use Microsoft Purview to manage data security & compliance for Microsoft Foundry](https://learn.microsoft.com/en-us/purview/ai-azure-foundry) · Documentación · Oficial · Microsoft Learn. Explica cómo habilitar Purview Data Security para Foundry (Foundry Control Plane o Defender for Cloud) y qué capacidades aplican a sus interacciones de IA.
- [Reference table for all AI security recommendations in Microsoft Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/recommendations-reference-ai) · Documentación · Oficial · Microsoft Learn. Lista de recomendaciones de postura para IA, incluidas las de agentes de Foundry con riesgo de inyección indirecta que deben exigir humano en el bucle para herramientas MCP.

**Manos a la obra**

1. `Laboratorio parcial` Crea un proyecto de Foundry con un modelo vendido directamente por Azure (recurso opcional del anexo de entorno) y un agente conectado a una colección personalizada del servidor MCP de Sentinel mediante una aplicación de Entra con SentinelPlatform.DelegatedAccess y OAuth Identity Passthrough ([MCP de Sentinel en Foundry](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-mcp-use-tool-azure-ai-foundry)). Limitación: costo de Azure y del data lake. Evidencia: agente que responde con datos de la colección.
2. `Laboratorio parcial` Sigue el laboratorio [Build a security investigation agent](https://learn.microsoft.com/en-us/azure/sentinel/isv/build-agent-azure-ai-foundry) de la serie IdentityDrift: prototipa las instrucciones en Foundry con la herramienta de exploración de Sentinel y llévalas al agent builder de Security Copilot. Limitación: data lake, Foundry y SCU con créditos de Azure. Evidencia: instrucciones prototipadas en Foundry y su versión en Security Copilot.
3. `Laboratorio` Activa la prueba de 30 días de [Defender for AI Services](https://learn.microsoft.com/en-us/azure/defender-for-cloud/ai-threat-protection) en el proyecto de Foundry, habilita la evidencia de prompts ([incorporación](https://learn.microsoft.com/en-us/azure/defender-for-cloud/ai-onboarding)), lanza un jailbreak de prueba contra tu agente y revisa la alerta en Defender XDR y la recomendación de humano en el circuito para MCP; desactiva el plan al terminar. Evidencia: alerta de Defender for AI Services y recomendación revisada.
4. `Laboratorio parcial` Activa Data Security para Foundry y revisa en Purview la auditoría de las interacciones de tu agente ([Purview para Foundry](https://learn.microsoft.com/en-us/purview/ai-azure-foundry)). Limitación: las directivas usan pay-as-you-go. Evidencia: eventos de auditoría del agente.
5. `Laboratorio` Inventaría los agentes clásicos de Foundry de tu organización (o declara que no hay) y escribe el plan de migración al modelo actual de [Foundry Agent Service](https://learn.microsoft.com/en-us/azure/foundry/agents/overview) antes del 31 de marzo de 2027, con dueño, fecha y pruebas. Evidencia: inventario y plan de migración.
6. `Solo producción` Descubre y evalúa la postura de los agentes de Foundry de producción en Defender for Cloud, lo que desde el 1 de julio de 2026 requiere Agent 365 ([postura de seguridad de IA](https://learn.microsoft.com/en-us/azure/defender-for-cloud/ai-security-posture)). Cómo hacerlo seguro: revisión en modo lectura, suscripción piloto, sin directivas de bloqueo al inicio y plan de corrección acordado con el dueño de cada agente. Evidencia: informe de postura con prioridades.

<a id="reto-avanzado"></a>

## Reto del nivel

**Automatización de punta a punta con un agente propio.** Construye un agente personalizado que investigue un tipo de incidente con una skill KQL propia y una herramienta MCP de Sentinel; dispáralo desde un playbook de Logic Apps solo para severidad alta, escribe su resultado en el incidente y agrega una Logic App como skill para la contención con aprobación humana. Entrega: manifiestos en Git, tabla de pruebas con casos adversos, comparación de SCU entre prompt genérico, direct skill y agente, la directiva de datos si lo expones en Copilot Studio y el agente publicado en ámbito de usuario con la revisión del owner.

<a id="quiz-avanzado"></a>

## Evaluación del nivel

Responde y compara con [Evaluaciones y respuestas](06_Evaluaciones_y_respuestas.md#eval-avanzado). Con 80 % o más, ¡nivel aprobado! (En la versión web puedes corregir en línea y generar tu certificado).

1. ¿Cómo se escribe una entrada reutilizable en un promptbook personalizado?
   - a) {NombreDelParametro}
   - b) $NombreDelParametro
   - c) <NombreDelParametro>, sin espacios
   - d) [[NombreDelParametro]]

2. Un flujo de Logic Apps que ejecuta un promptbook falla siempre. ¿Cuál es la causa más probable?
   - a) Falta una entrada obligatoria, como <SENTINEL_INCIDENT_ID>
   - b) El promptbook tiene Continue on failure activado
   - c) El promptbook está compartido con toda la organización
   - d) El plan de Logic Apps es Consumption

3. ¿Qué alcance tienen las directivas de datos de Power Platform para agentes de Copilot Studio?
   - a) Solo aplican a tenants con E5
   - b) Son obligatorias para todos los tenants desde principios de 2025, sin exenciones
   - c) Solo aplican a agentes publicados en Teams
   - d) Son opcionales y solo se recomiendan

4. Sobre los plugins MCP de Security Copilot, ¿qué afirmación es correcta?
   - a) Importan recursos y prompts del servidor
   - b) Redescubren herramientas nuevas automáticamente
   - c) SSE es el transporte recomendado
   - d) Las herramientas con destructiveHint=true no se importan aunque figuren en AllowedTools

5. ¿Cuál de estos NO es un valor válido de Target en una skill KQL de Security Copilot?
   - a) Purview
   - b) Sentinel
   - c) SentinelDataLake
   - d) Kusto

6. En la acción Submit a Security Copilot prompt, ¿qué parámetro permite saltarse el planificador e invocar una skill concreta?
   - a) Session ID
   - b) Plugins
   - c) Prompt Content
   - d) Direct Skill Name

7. Un agente personalizado no aparece en la acción Execute a Security Copilot Agent. ¿Cuál es la causa más probable?
   - a) Falta Application Insights
   - b) El agente no está en el workspace por defecto o no está compartido con Anyone in this workspace
   - c) Logic Apps Consumption no es compatible
   - d) Falta el rol Microsoft Sentinel Contributor

8. ¿Cuál es el límite documentado del conector de Security Copilot?
   - a) 600 llamadas por conexión cada 60 segundos
   - b) 60 llamadas por minuto por tenant
   - c) 6.000 llamadas por hora
   - d) No tiene límite

9. Al desarrollar un agente personalizado, ¿qué actividad consume SCU?
   - a) Crearlo con el agent builder
   - b) Crearlo con NL2Agent
   - c) Probarlo
   - d) Publicarlo

10. ¿Qué rol puede publicar un agente personalizado para todo el workspace?
   - a) Copilot contributor
   - b) Copilot owner
   - c) Security Reader
   - d) Global Reader

11. ¿Qué regla aplica al manifiesto YAML de un agente de Security Copilot?
   - a) Puede contener varios AgentDefinitions
   - b) Cada agente admite varios esquemas de autenticación
   - c) Un solo AgentDefinition por YAML, con FetchSkill y ProcessSkill en el espacio de nombres Skillset.Skill
   - d) No necesita la clave Descriptor

12. ¿Cuál es una limitación de la colección de triage del servidor MCP de Sentinel?
   - a) Solo consulta el data lake
   - b) Funciona como invitado en otros tenants
   - c) Requiere Copilot Studio
   - d) Solo funciona en tu propio tenant y no consulta el data lake

13. ¿Qué rol mínimo permite crear herramientas MCP personalizadas desde la búsqueda avanzada?
   - a) Security Operator
   - b) Security Reader
   - c) Global Reader
   - d) Microsoft Sentinel Reader

14. ¿A qué agentes aplica la detección externa de amenazas en tiempo de ejecución de Copilot Studio?
   - a) A los agentes clásicos
   - b) A los agentes con orquestación generativa
   - c) A todos los flujos de Power Automate
   - d) Solo a los agentes publicados en Teams

15. ¿Cuándo se retiran los agentes clásicos de Microsoft Foundry?
   - a) El 1 de julio de 2026
   - b) El 18 de noviembre de 2026
   - c) El 31 de marzo de 2027
   - d) No tienen fecha de retiro

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

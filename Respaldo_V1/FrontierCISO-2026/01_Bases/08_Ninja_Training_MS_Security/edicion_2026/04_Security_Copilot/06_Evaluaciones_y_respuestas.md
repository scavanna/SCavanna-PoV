# Evaluaciones y respuestas

*Microsoft Security Copilot Ninja Training: hacia el SOC agéntico · Edición 2026*

[← Comunidad](05_Comunidad.md) · [Índice del programa](README.md) · [Laboratorio y práctica en producción →](07_Laboratorio_y_practica_en_produccion.md)

<a id="respuestas"></a>

Cada evaluación tiene preguntas de opción múltiple. Con 80 % o más el nivel se considera aprobado. Es una autoevaluación de esta guía, no una certificación de Microsoft.

<a id="eval-inicial"></a>

## Nivel 1 · Inicial · Fundamentos

**1. ¿Cuántas SCU mensuales recibe por la inclusión una organización con 4.000 licencias pagas de Microsoft 365 E5?**

- a) 400
- b) 1.600  ✅
- c) 4.000
- d) 10.000

*Respuesta: b).* La inclusión otorga 400 SCU al mes por cada 1.000 licencias de usuario pagas, con escalado lineal y un tope de 10.000. [Fuente](https://learn.microsoft.com/en-us/copilot/security/security-copilot-inclusion) · Repasa [I2](01_Nivel_1_Inicial.md#i2)

**2. ¿Qué pasa con las SCU incluidas en E5/E7 que no se usan durante el mes?**

- a) Se acumulan hasta tres meses
- b) Se convierten en SCU de excedente
- c) Se reembolsan como crédito de Azure
- d) Se pierden: el pool se reinicia cada mes sin acumularse  ✅

*Respuesta: d).* La asignación se reinicia cada mes y no se acumula; por eso conviene priorizar casos de uso y agentes con el pool disponible. [Fuente](https://learn.microsoft.com/en-us/copilot/security/security-copilot-inclusion) · Repasa [I2](01_Nivel_1_Inicial.md#i2)

**3. ¿Cómo se factura la capacidad aprovisionada de Security Copilot?**

- a) Por bloques de hora de reloj, con un mínimo de 1 SCU; lo no usado expira al final de cada hora  ✅
- b) Por minuto de uso real
- c) Por prompt ejecutado
- d) Con una tarifa mensual fija por usuario

*Respuesta: a).* La capacidad aprovisionada se cobra por hora de reloj iniciada; el excedente, en cambio, se mide por uso real con un decimal. [Fuente](https://learn.microsoft.com/en-us/copilot/security/security-compute-units-capacity) · Repasa [I2](01_Nivel_1_Inicial.md#i2)

**4. En un tenant de MCSA auto-aprovisionado con E5, cuyos datos no residen en la UE, ¿dónde se evalúan los prompts por defecto?**

- a) Solo en EE. UU.
- b) En la región del workspace de Sentinel
- c) De forma global (EE. UU., Reino Unido, UE y Australia-Nueva Zelanda)  ✅
- d) Solo en la UE

*Respuesta: c).* La evaluación queda en la UE solo si los datos residen en la UE; en otro caso es global, el escenario típico en MCSA. [Fuente](https://learn.microsoft.com/en-us/copilot/security/auto-provisioning-security-copilot) · Repasa [I2](01_Nivel_1_Inicial.md#i2)

**5. Según Microsoft, ¿cómo se relacionan Project Perception y Security Copilot?**

- a) Perception reemplaza y retira a Security Copilot
- b) Perception es un plugin de la experiencia independiente
- c) Son productos sin relación
- d) Perception es el sistema agéntico que actúa y Security Copilot la IA que asiste; trabajan juntos  ✅

*Respuesta: d).* Microsoft presenta a Perception como la «IA que actúa» y a Security Copilot como la «IA que asiste», y aclara que funcionan juntos. [Fuente](https://www.microsoft.com/en-us/security/business/ai-powered-cybersecurity/project-perception-agentic-system) · Repasa [I1](01_Nivel_1_Inicial.md#i1)

**6. ¿En qué estado está Project Perception según la documentación de Learn al 6 de noviembre de 2026?**

- a) Vista previa pública limitada, solo por invitación, dentro del portal de Defender  ✅
- b) Disponibilidad general incluida en E5
- c) Vista previa privada sin costo
- d) Retirado

*Respuesta: a).* Learn lo describe como Limited Public Preview por invitación; el blog del anuncio habla de vista previa pública desde el 3 de agosto, una contradicción registrada en las limitaciones de esta guía. [Fuente](https://learn.microsoft.com/en-us/security/agentic-security/agentic-security-get-started) · Repasa [I1](01_Nivel_1_Inicial.md#i1)

**7. Un analista comparte una sesión con un compañero que no tiene permisos sobre los datos de Sentinel usados en ella. ¿Qué ocurre?**

- a) El compañero no puede abrir la sesión
- b) El compañero la ve en solo lectura, aunque no tenga acceso a los datos del plugin  ✅
- c) El compañero puede continuar la sesión con sus propios prompts
- d) La sesión se comparte también fuera del tenant

*Respuesta: b).* Las sesiones compartidas son de solo lectura, solo dentro del tenant, y quien las ve no necesita acceso a los datos del plugin: por eso compartir es una decisión de gobierno. [Fuente](https://learn.microsoft.com/en-us/copilot/security/authentication) · Repasa [I3](01_Nivel_1_Inicial.md#i3)

**8. Un owner restringe un plugin preinstalado de Microsoft en la configuración de plugins. ¿Qué efecto tiene?**

- a) Ninguno sobre las experiencias embebidas
- b) Solo afecta a los agentes de partners
- c) También afecta a las experiencias embebidas que usan ese plugin  ✅
- d) Elimina el plugin del tenant de forma irreversible

*Respuesta: c).* Restringir un plugin preinstalado también lo quita de las experiencias embebidas, así que hay que evaluar el impacto antes de hacerlo. [Fuente](https://learn.microsoft.com/en-us/copilot/security/manage-plugins) · Repasa [I3](01_Nivel_1_Inicial.md#i3)

**9. Un analista oculta el panel lateral de Copilot en el portal de Defender para ahorrar SCU. ¿Funciona?**

- a) Sí, el resumen deja de generarse
- b) No: el resumen de incidentes se sigue generando; el costo se controla con el modo de generación  ✅
- c) Sí, pero solo en incidentes de severidad baja
- d) No, porque el resumen de incidentes no consume SCU

*Respuesta: b).* Ocultar el panel no cambia el consumo. El control real es el modo de generación (siempre, por severidad o bajo demanda) y la caché de una semana. [Fuente](https://learn.microsoft.com/en-us/copilot/security/experiences-security-copilot) · Repasa [I4](01_Nivel_1_Inicial.md#i4)

**10. ¿Qué integración de Azure funciona solo desde la experiencia independiente de Security Copilot?**

- a) Azure WAF  ✅
- b) Defender for Cloud
- c) Azure Firewall
- d) Intune

*Respuesta: a).* Azure WAF (Application Gateway y Front Door) solo se usa desde la experiencia independiente; Defender for Cloud y Azure Firewall también llegan vía Copilot en Azure. [Fuente](https://learn.microsoft.com/en-us/azure/web-application-firewall/waf-copilot) · Repasa [I4](01_Nivel_1_Inicial.md#i4)

**11. ¿Cuál NO es uno de los cuatro elementos de un prompt efectivo según Microsoft?**

- a) Objetivo
- b) Contexto
- c) Fuente
- d) Temperatura del modelo  ✅

*Respuesta: d).* Los cuatro elementos son objetivo, contexto, expectativas y fuente; la temperatura no se configura en Security Copilot. [Fuente](https://learn.microsoft.com/en-us/copilot/security/prompting-tips) · Repasa [I5](01_Nivel_1_Inicial.md#i5)

**12. ¿Qué funciones de Security Copilot consumen SCU?**

- a) Solo las de disponibilidad general
- b) Solo las de vista previa privada
- c) Las de disponibilidad general y las de vista previa pública  ✅
- d) Ninguna en vista previa

*Respuesta: c).* GA y vista previa pública consumen SCU; la vista previa privada no. Hay excepciones puntuales, como el Dynamic Threat Detection Agent, gratuito durante su vista previa. [Fuente](https://learn.microsoft.com/en-us/copilot/security/manage-usage) · Repasa [I6](01_Nivel_1_Inicial.md#i6)

**13. Quieres practicar prompts, promptbooks y la creación de agentes sin tenant ni SCU. ¿Qué recurso usas?**

- a) El Customer Connection Program
- b) El onboarding manual con 3 SCU y excedente ilimitado
- c) La calculadora de capacidad
- d) Las simulaciones guiadas de la ruta SC-5006  ✅

*Respuesta: d).* Las simulaciones guiadas (casi dos horas) cubren owner settings, prompts, promptbooks, Purview, Defender XDR, agentes y el agente de acceso condicional sin tenant ni SCU. [Fuente](https://learn.microsoft.com/en-us/training/modules/security-copilot-interactive-guides/) · Repasa [I6](01_Nivel_1_Inicial.md#i6)

**14. En el OWASP Top 10 para aplicaciones LLM 2025, ¿qué riesgo se relaciona más directamente con el costo de un playbook que llama a Copilot en cada incidente?**

- a) LLM01 · Inyección de prompts
- b) LLM06 · Agencia excesiva
- c) LLM10 · Consumo no acotado  ✅
- d) Ninguno: el costo no es un riesgo de seguridad

*Respuesta: c).* LLM10 trata el consumo no acotado de recursos; en Security Copilot se traduce en SCU y se mitiga con filtros, topes de excedente y el panel de uso. [Fuente](https://genai.owasp.org/llm-top-10/) · Repasa [P0](01_Nivel_1_Inicial.md#p0)

**15. ¿Qué puntaje del knowledge check del Ninja oficial permite pedir el certificado de participación?**

- a) 100 %
- b) 80 %  ✅
- c) 75 %
- d) 70 %

*Respuesta: b).* Con 80 % o más se solicita un certificado de participación, que no es una certificación oficial de Microsoft. [Fuente](https://techcommunity.microsoft.com/blog/securitycopilotblog/how-to-become-a-microsoft-security-copilot-ninja-the-complete-level-400-training/4106928) · Repasa [I0](01_Nivel_1_Inicial.md#i0)

<a id="eval-intermedio"></a>

## Nivel 2 · Intermedio · Security Copilot en cada rol

**1. ¿Qué tipo de alerta tría el Security Alert Triage Agent en disponibilidad general?**

- a) Identidad
- b) Nube y contenedores
- c) Correo y colaboración  ✅
- d) Todas las anteriores

*Respuesta: c).* El triage de correo y colaboración es GA; nube, contenedores e identidad siguen en vista previa. [Fuente](https://learn.microsoft.com/en-us/defender-xdr/security-alert-triage-agent) · Repasa [M1](02_Nivel_2_Intermedio.md#m1)

**2. Configuraste el agente de triage de correo reportado, pero no clasifica nada. ¿Cuál es la causa más probable?**

- a) Falta un workspace de Sentinel
- b) La regla de ajuste Auto-Resolve resuelve las alertas de correo reportado antes de que el agente las vea  ✅
- c) Falta la licencia de Defender EASM
- d) El tenant no tiene Intune

*Respuesta: b).* El agente no tría alertas ya resueltas: hay que desactivar la regla de ajuste de autorresolución del correo reportado. [Fuente](https://learn.microsoft.com/en-us/defender-xdr/security-alert-triage-agent) · Repasa [M1](02_Nivel_2_Intermedio.md#m1)

**3. ¿Cómo se cobra hoy el Dynamic Threat Detection Agent?**

- a) Es gratuito durante la vista previa y consumirá SCU al llegar a disponibilidad general  ✅
- b) 1 SCU por alerta generada
- c) Con una licencia aparte en el Security Store
- d) Solo está incluido en E7

*Respuesta: a).* Es un servicio de backend sin configuración, gratuito mientras siga en vista previa pública. [Fuente](https://learn.microsoft.com/en-us/defender-xdr/dynamic-threat-detection-agent) · Repasa [M1](02_Nivel_2_Intermedio.md#m1)

**4. Al configurar un agente de Microsoft en Defender, ¿qué identidad se recomienda?**

- a) Una cuenta de Global Administrator para evitar errores de permisos
- b) Una cuenta de usuario protegida con PIM
- c) Una cuenta compartida del SOC
- d) Una nueva Microsoft Entra Agent ID con permisos mínimos  ✅

*Respuesta: d).* La identidad de agente dedicada es la recomendación; una cuenta de usuario no es compatible con PIM ni TAP y hereda todos sus accesos. [Fuente](https://learn.microsoft.com/en-us/defender-xdr/security-alert-triage-agent) · Repasa [M1](02_Nivel_2_Intermedio.md#m1)

**5. El informe de exposición del Threat Intelligence Briefing Agent aparece como «not available». ¿Qué revisas primero?**

- a) La licencia de E7
- b) El plugin de Purview
- c) Los permisos de lectura de la identidad del agente sobre Defender for Endpoint y los grupos de dispositivos  ✅
- d) El rol de Global Administrator del usuario

*Respuesta: c).* Con identidad de agente hay que darle lectura de búsqueda avanzada, gestión de vulnerabilidades, configuración e inventario de dispositivos y acceso a cada grupo de dispositivos. [Fuente](https://learn.microsoft.com/en-us/defender-xdr/security-copilot-agents-defender) · Repasa [M2](02_Nivel_2_Intermedio.md#m2)

**6. ¿En qué estado crea las políticas nuevas el Conditional Access Optimization Agent y qué licencia mínima exige?**

- a) Activas; Entra ID P2
- b) En modo solo informe; Entra ID P1  ✅
- c) Deshabilitadas; Entra Suite
- d) Activas; Entra ID P1

*Respuesta: b).* El agente requiere Entra ID P1 y crea las políticas en solo informe, para que pasen por el control de cambios. [Fuente](https://learn.microsoft.com/en-us/entra/security-copilot/conditional-access-agent-optimization) · Repasa [M3](02_Nivel_2_Intermedio.md#m3)

**7. ¿Qué afirmación sobre el Identity Risk Management Agent es correcta?**

- a) Remedia automáticamente a los usuarios en riesgo
- b) Analiza identidades de carga de trabajo
- c) No consume SCU
- d) Analiza hasta 100 usuarios en riesgo por ejecución y una persona aprueba cada recomendación  ✅

*Respuesta: d).* Está en vista previa, no remedia de forma automática y analiza hasta 100 usuarios por ejecución, con menos de 1 SCU en promedio. [Fuente](https://learn.microsoft.com/en-us/entra/id-protection/identity-risk-management-agent-get-started) · Repasa [M3](02_Nivel_2_Intermedio.md#m3)

**8. Al 6 de noviembre de 2026, ¿qué agente de Intune sigue disponible?**

- a) Policy Configuration Agent
- b) Change Review Agent
- c) Device Offboarding Agent
- d) Vulnerability Remediation Agent  ✅

*Respuesta: d).* Device Offboarding se retiró el 1 de junio de 2026 y Policy Configuration y Change Review, el 31 de agosto de 2026. [Fuente](https://learn.microsoft.com/en-us/intune/copilot/agents/change-review-agent) · Repasa [M4](02_Nivel_2_Intermedio.md#m4)

**9. ¿Qué alertas DLP NO tría el agente de triage de Purview?**

- a) Las de Exchange Online
- b) Las de Teams
- c) Las de políticas en modo simulación  ✅
- d) Las de dispositivos

*Respuesta: c).* El agente solo procesa alertas de políticas en modo activo, con archivos de hasta 2 MB y alertas de hasta 30 días antes de habilitarlo. [Fuente](https://learn.microsoft.com/en-us/purview/copilot-in-purview-agents-overview) · Repasa [M5](02_Nivel_2_Intermedio.md#m5)

**10. ¿Para qué agentes existe en Security Copilot la opción de crear una identidad de agente (Entra Agent ID)?**

- a) Solo para los agentes creados por Microsoft  ✅
- b) Para todos los agentes, incluidos los de partners
- c) Solo para los agentes personalizados
- d) Para ninguno: siempre se usa una cuenta de usuario

*Respuesta: a).* La documentación de Security Copilot indica que la opción solo existe para agentes de Microsoft; los demás usan una cuenta de usuario cuyos permisos heredan. [Fuente](https://learn.microsoft.com/en-us/copilot/security/agents-overview) · Repasa [M6](02_Nivel_2_Intermedio.md#m6)

**11. Quieres desplegar un agente de partner que accede a datos de productos Microsoft. ¿Qué aprobación adicional necesitas?**

- a) La de un Global Administrator antes de que owners o contributors terminen la configuración  ✅
- b) La de un Security Reader
- c) Ninguna, basta con ser contributor
- d) La del soporte de Microsoft

*Respuesta: a).* Los agentes de partners que acceden a datos de Microsoft requieren el consentimiento de un Global Administrator. [Fuente](https://learn.microsoft.com/en-us/copilot/security/agents-manage) · Repasa [M6](02_Nivel_2_Intermedio.md#m6)

**12. ¿Qué caracteriza a los playbooks de Project Perception en su versión actual?**

- a) Cada SOC escribe los suyos en YAML
- b) Los define Microsoft y no se pueden crear playbooks propios  ✅
- c) Son flujos de Logic Apps
- d) Se compran en el Security Store

*Respuesta: b).* Perception coordina sus agentes con playbooks predefinidos por Microsoft, de solo lectura en esta versión. [Fuente](https://learn.microsoft.com/en-us/security/agentic-security/agentic-security-concepts) · Repasa [M6](02_Nivel_2_Intermedio.md#m6)

**13. ¿Qué afirmación sobre los roles de Security Copilot es correcta?**

- a) Son roles de Entra ID
- b) Dan acceso a los datos de seguridad de cada producto
- c) Admiten asignación a cualquier tipo de grupo
- d) Controlan la plataforma, exigen mantener dos owners y Copilot no supera los permisos del usuario en cada plugin  ✅

*Respuesta: d).* Owner y contributor son roles propios de Security Copilot; el acceso a los datos depende de los permisos de cada usuario (on-behalf-of). [Fuente](https://learn.microsoft.com/en-us/copilot/security/authentication) · Repasa [M7](02_Nivel_2_Intermedio.md#m7)

**14. ¿Dónde se auditan los pares prompt-respuesta de Security Copilot?**

- a) Solo en el panel de uso
- b) En Sentinel, por defecto
- c) En Purview DSPM for AI  ✅
- d) No se auditan

*Respuesta: c).* El registro unificado de Purview guarda eventos de administración y metadatos; los pares prompt-respuesta se ven en DSPM for AI. [Fuente](https://learn.microsoft.com/en-us/copilot/security/audit-log) · Repasa [M7](02_Nivel_2_Intermedio.md#m7)

**15. Creas una política de acceso condicional de Protect AI dirigida a Security Copilot. ¿Qué cubre?**

- a) La experiencia independiente, no las experiencias embebidas  ✅
- b) Todas las experiencias embebidas
- c) Solo los agentes de partners
- d) Solo las Logic Apps que usan el conector

*Respuesta: a).* Estas políticas aplican a la experiencia independiente y se crean en modo solo informe; Microsoft recomienda además cubrir todos los recursos. [Fuente](https://raw.githubusercontent.com/MicrosoftDocs/entra-docs/main/docs/identity/conditional-access/policy-all-users-copilot-ai-security.md) · Repasa [M7](02_Nivel_2_Intermedio.md#m7)

<a id="eval-avanzado"></a>

## Nivel 3 · Avanzado · Extender y automatizar

**1. ¿Cómo se escribe una entrada reutilizable en un promptbook personalizado?**

- a) {NombreDelParametro}
- b) $NombreDelParametro
- c) <NombreDelParametro>, sin espacios  ✅
- d) [[NombreDelParametro]]

*Respuesta: c).* Las entradas se escriben entre signos de menor y mayor y sin espacios; luego se completan al ejecutar el promptbook. [Fuente](https://learn.microsoft.com/en-us/copilot/security/build-promptbooks) · Repasa [A1](03_Nivel_3_Avanzado.md#a1)

**2. Un flujo de Logic Apps que ejecuta un promptbook falla siempre. ¿Cuál es la causa más probable?**

- a) Falta una entrada obligatoria, como <SENTINEL_INCIDENT_ID>  ✅
- b) El promptbook tiene Continue on failure activado
- c) El promptbook está compartido con toda la organización
- d) El plan de Logic Apps es Consumption

*Respuesta: a).* Si falta una entrada obligatoria del promptbook, la acción Submit a Security Copilot promptbook falla. [Fuente](https://learn.microsoft.com/en-us/copilot/security/connector-logicapp) · Repasa [A1](03_Nivel_3_Avanzado.md#a1)

**3. ¿Qué alcance tienen las directivas de datos de Power Platform para agentes de Copilot Studio?**

- a) Solo aplican a tenants con E5
- b) Son obligatorias para todos los tenants desde principios de 2025, sin exenciones  ✅
- c) Solo aplican a agentes publicados en Teams
- d) Son opcionales y solo se recomiendan

*Respuesta: b).* Desde principios de 2025 (MC973179) las directivas de datos se aplican a todos los tenants y ya no hay exenciones para agentes. [Fuente](https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-data-loss-prevention) · Repasa [A6](03_Nivel_3_Avanzado.md#a6)

**4. Sobre los plugins MCP de Security Copilot, ¿qué afirmación es correcta?**

- a) Importan recursos y prompts del servidor
- b) Redescubren herramientas nuevas automáticamente
- c) SSE es el transporte recomendado
- d) Las herramientas con destructiveHint=true no se importan aunque figuren en AllowedTools  ✅

*Respuesta: d).* Los plugins MCP (vista previa) solo importan herramientas no destructivas, no redescubren solos y recomiendan StreamableHttp. [Fuente](https://learn.microsoft.com/en-us/copilot/security/plugin-mcp) · Repasa [A2](03_Nivel_3_Avanzado.md#a2)

**5. ¿Cuál de estos NO es un valor válido de Target en una skill KQL de Security Copilot?**

- a) Purview  ✅
- b) Sentinel
- c) SentinelDataLake
- d) Kusto

*Respuesta: a).* Los targets válidos son Defender, Sentinel, SentinelDataLake, LogAnalytics y Kusto. [Fuente](https://learn.microsoft.com/en-us/copilot/security/plugin-kql) · Repasa [A2](03_Nivel_3_Avanzado.md#a2)

**6. En la acción Submit a Security Copilot prompt, ¿qué parámetro permite saltarse el planificador e invocar una skill concreta?**

- a) Session ID
- b) Plugins
- c) Prompt Content
- d) Direct Skill Name  ✅

*Respuesta: d).* Direct Skill Name y Direct Skill Inputs evitan el planificador, lo que suele reducir tiempo y consumo de SCU. [Fuente](https://learn.microsoft.com/en-us/copilot/security/connector-logicapp) · Repasa [A3](03_Nivel_3_Avanzado.md#a3)

**7. Un agente personalizado no aparece en la acción Execute a Security Copilot Agent. ¿Cuál es la causa más probable?**

- a) Falta Application Insights
- b) El agente no está en el workspace por defecto o no está compartido con Anyone in this workspace  ✅
- c) Logic Apps Consumption no es compatible
- d) Falta el rol Microsoft Sentinel Contributor

*Respuesta: b).* Solo se pueden disparar agentes del workspace por defecto y, si son personalizados, compartidos con todo el workspace. [Fuente](https://learn.microsoft.com/en-us/copilot/security/connector-logicapp-agent-trigger) · Repasa [A3](03_Nivel_3_Avanzado.md#a3)

**8. ¿Cuál es el límite documentado del conector de Security Copilot?**

- a) 600 llamadas por conexión cada 60 segundos  ✅
- b) 60 llamadas por minuto por tenant
- c) 6.000 llamadas por hora
- d) No tiene límite

*Respuesta: a).* La referencia del conector fija 600 llamadas por conexión cada 60 segundos. [Fuente](https://learn.microsoft.com/en-us/connectors/securitycopilot/) · Repasa [A3](03_Nivel_3_Avanzado.md#a3)

**9. Al desarrollar un agente personalizado, ¿qué actividad consume SCU?**

- a) Crearlo con el agent builder
- b) Crearlo con NL2Agent
- c) Probarlo  ✅
- d) Publicarlo

*Respuesta: c).* Crear y publicar no consumen SCU; probar y ejecutar siempre consumen. [Fuente](https://learn.microsoft.com/en-us/copilot/security/developer/cost-considerations) · Repasa [A4](03_Nivel_3_Avanzado.md#a4)

**10. ¿Qué rol puede publicar un agente personalizado para todo el workspace?**

- a) Copilot contributor
- b) Copilot owner  ✅
- c) Security Reader
- d) Global Reader

*Respuesta: b).* El contributor crea, prueba y publica en su propio ámbito; el owner publica para el workspace. [Fuente](https://learn.microsoft.com/en-us/copilot/security/developer/custom-agent-overview) · Repasa [A4](03_Nivel_3_Avanzado.md#a4)

**11. ¿Qué regla aplica al manifiesto YAML de un agente de Security Copilot?**

- a) Puede contener varios AgentDefinitions
- b) Cada agente admite varios esquemas de autenticación
- c) Un solo AgentDefinition por YAML, con FetchSkill y ProcessSkill en el espacio de nombres Skillset.Skill  ✅
- d) No necesita la clave Descriptor

*Respuesta: c).* Las buenas prácticas piden un AgentDefinition por archivo, nombres Skillset.Skill y un único esquema de autenticación por agente. [Fuente](https://learn.microsoft.com/en-us/copilot/security/developer/manifest-best-practices) · Repasa [A4](03_Nivel_3_Avanzado.md#a4)

**12. ¿Cuál es una limitación de la colección de triage del servidor MCP de Sentinel?**

- a) Solo consulta el data lake
- b) Funciona como invitado en otros tenants
- c) Requiere Copilot Studio
- d) Solo funciona en tu propio tenant y no consulta el data lake  ✅

*Respuesta: d).* La colección de triage no admite acceso como invitado ni delegado, no permite elegir workspace y no consulta el lake. [Fuente](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-mcp-triage-tool) · Repasa [A5](03_Nivel_3_Avanzado.md#a5)

**13. ¿Qué rol mínimo permite crear herramientas MCP personalizadas desde la búsqueda avanzada?**

- a) Security Operator  ✅
- b) Security Reader
- c) Global Reader
- d) Microsoft Sentinel Reader

*Respuesta: a).* Crear requiere Security Operator, Security Admin o Global Admin; usarlas, Security Reader o Global Reader. [Fuente](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-mcp-create-custom-tool) · Repasa [A5](03_Nivel_3_Avanzado.md#a5)

**14. ¿A qué agentes aplica la detección externa de amenazas en tiempo de ejecución de Copilot Studio?**

- a) A los agentes clásicos
- b) A los agentes con orquestación generativa  ✅
- c) A todos los flujos de Power Automate
- d) Solo a los agentes publicados en Teams

*Respuesta: b).* La protección externa (Defender u otro proveedor) solo aplica a agentes con orquestación generativa y está en vista previa. [Fuente](https://learn.microsoft.com/en-us/microsoft-copilot-studio/external-security-provider) · Repasa [A6](03_Nivel_3_Avanzado.md#a6)

**15. ¿Cuándo se retiran los agentes clásicos de Microsoft Foundry?**

- a) El 1 de julio de 2026
- b) El 18 de noviembre de 2026
- c) El 31 de marzo de 2027  ✅
- d) No tienen fecha de retiro

*Respuesta: c).* Los agentes clásicos están deprecados y se retiran el 31 de marzo de 2027: hay que planificar la migración. [Fuente](https://learn.microsoft.com/en-us/azure/foundry-classic/agents/how-to/tools-classic/overview) · Repasa [A7](03_Nivel_3_Avanzado.md#a7)

<a id="eval-agentes"></a>

## Nivel 4 · SOC agéntico · Del SOC tradicional al SOC agéntico

**1. Según Microsoft, ¿qué caracteriza la etapa SOC 2 del camino hacia el SOC agéntico?**

- a) Unificar la plataforma
- b) IA generativa y agentes de tarea  ✅
- c) Automatización agéntica de punta a punta
- d) Tercerizar el SOC

*Respuesta: b).* SOC 1 unifica la plataforma, SOC 2 incorpora IA generativa y agentes de tarea, y SOC 3 llega a la automatización agéntica. [Fuente](https://www.microsoft.com/en-us/security/blog/2026/04/09/the-agentic-soc-rethinking-secops-for-the-next-decade/) · Repasa [X1](04_Nivel_4_SOC_agentico.md#x1)

**2. En Project Perception, ¿qué ocurre al detener una sesión de trabajo agéntico?**

- a) Se puede reanudar en las siguientes 24 horas
- b) Se convierte en un playbook propio
- c) Es irreversible y la sesión queda como registro de auditoría  ✅
- d) Se eliminan sus registros

*Respuesta: c).* Detener es irreversible; las sesiones son registros inmutables de auditoría, junto con las aprobaciones y rechazos. [Fuente](https://learn.microsoft.com/en-us/security/agentic-security/agentic-security-supervise-work) · Repasa [X1](04_Nivel_4_SOC_agentico.md#x1)

**3. ¿Qué estima el libro blanco de Microsoft sobre SecOps agéntico acerca de las alertas?**

- a) Que el 42 % queda sin investigar  ✅
- b) Que el 99,99 % son falsos positivos
- c) Que el 75 % son de phishing
- d) Que el 20 % son críticas

*Respuesta: a).* El libro blanco estima que el 42 % de las alertas queda sin investigar y que los analistas dedican más del 20 % de su tiempo a juntar datos. [Fuente](https://marketingassets.microsoft.com/gdc/gdc46cegG/original) · Repasa [X1](04_Nivel_4_SOC_agentico.md#x1)

**4. En el ensayo controlado del agente de triage de phishing, ¿qué parte de la ganancia de productividad vino de priorizar la cola?**

- a) 17 %
- b) 53 %
- c) 77 %
- d) 83 %  ✅

*Respuesta: d).* El 83 % de la ganancia vino de la priorización; 77 % fue la mejora de exactitud y 53 % el aumento del tiempo dedicado a correos maliciosos. [Fuente](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/security/randomized-controlled-trial-for-phishing-triage-agent-accessible.pdf) · Repasa [X2](04_Nivel_4_SOC_agentico.md#x2)

**5. El estudio que asocia la adopción de Security Copilot con un MTTR 30,13 % menor a los tres meses es:**

- a) Un ensayo controlado aleatorizado
- b) Un estudio observacional de operaciones reales  ✅
- c) Una proyección de Forrester
- d) Una encuesta de satisfacción

*Respuesta: b).* Es un estudio observacional de más de 150 organizaciones: muestra una asociación, no una relación causal. [Fuente](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/final/en-us/microsoft-brand/documents/Generative-AI-and-Security-Operations-Center-Productivity-Evidence-from-Live-Operations_v2.5-FINAL.pdf) · Repasa [X2](04_Nivel_4_SOC_agentico.md#x2)

**6. ¿Qué describe mejor el estudio Total Economic Impact de Forrester de noviembre de 2024 sobre Security Copilot?**

- a) Una medición en más de 150 organizaciones
- b) Un ensayo controlado con 167 analistas
- c) Un estudio proyectado, con un ROI estimado de 99 % a 348 % para un SOC de 20 personas  ✅
- d) Una auditoría independiente de costos reales

*Respuesta: c).* Es un estudio proyectado basado en entrevistas y modelos; sirve de referencia, no reemplaza tu línea base. [Fuente](https://tei.forrester.com/go/Microsoft/SecurityCopilot/) · Repasa [X2](04_Nivel_4_SOC_agentico.md#x2)

**7. Para extender el acceso condicional e ID Protection a identidades de agente, ¿qué se necesita?**

- a) Solo Entra ID Free
- b) SCU de Security Copilot
- c) Defender for Cloud
- d) Microsoft Agent 365 (incluido en E7 y como complemento para E5)  ✅

*Respuesta: d).* Entra Agent ID está disponible para todos los clientes de Entra, pero los controles avanzados para agentes requieren Agent 365. [Fuente](https://learn.microsoft.com/en-us/entra/agent-id/what-is-microsoft-entra-agent-id) · Repasa [X3](04_Nivel_4_SOC_agentico.md#x3)

**8. ¿Qué afirmación sobre las identidades de agente de Entra es correcta?**

- a) No tienen credenciales propias, son de un solo tenant y pueden tener un sponsor humano  ✅
- b) Usan contraseñas que rota el propio agente
- c) Funcionan en varios tenants a la vez
- d) Reemplazan a las cuentas de servicio y no se auditan

*Respuesta: a).* Las credenciales las aporta el blueprint; cada identidad pertenece a un tenant y puede tener un sponsor responsable. [Fuente](https://learn.microsoft.com/en-us/entra/agent-id/agent-identities) · Repasa [X3](04_Nivel_4_SOC_agentico.md#x3)

**9. ¿Dónde se registran los eventos de la protección en tiempo real de Defender para agentes?**

- a) En AIAgentsInfo
- b) En BehaviorInfo  ✅
- c) En SigninLogs
- d) Solo en CloudAppEvents

*Respuesta: b).* La protección en tiempo real, con una regla por defecto en auditoría y reglas de bloqueo, registra su actividad en BehaviorInfo. [Fuente](https://learn.microsoft.com/en-us/defender-xdr/security-for-ai/ai-agent-real-time-protection) · Repasa [X3](04_Nivel_4_SOC_agentico.md#x3)

**10. En Purview, ¿qué protección aplica a los agentes de Security Copilot?**

- a) Clasificación, etiquetas, DLP y riesgo interno
- b) Solo DLP
- c) Solo la clasificación de datos  ✅
- d) Ninguna

*Respuesta: c).* Para agentes de Security Copilot solo aplica la clasificación; los de Copilot Studio y Foundry suman etiquetas, DLP y riesgo interno. [Fuente](https://learn.microsoft.com/en-us/purview/ai-agents) · Repasa [X3](04_Nivel_4_SOC_agentico.md#x3)

**11. ¿Qué tabla de la búsqueda avanzada reemplaza a AIAgentsInfo con la transición a Agent 365?**

- a) AgentsInfo  ✅
- b) AIAgentEvents
- c) AgentIdentityInfo
- d) CopilotAgents

*Respuesta: a).* AgentsInfo reemplaza a AIAgentsInfo: actualiza consultas y detecciones que usaban la tabla anterior. [Fuente](https://learn.microsoft.com/en-us/defender-xdr/security-for-ai/ai-agent-inventory) · Repasa [X4](04_Nivel_4_SOC_agentico.md#x4)

**12. Desde el 1 de julio de 2026, ¿qué se necesita para descubrir agentes de Foundry y de terceros en Defender for Cloud?**

- a) Defender CSPM únicamente
- b) Microsoft Agent 365  ✅
- c) Un workspace de Sentinel
- d) Capacidad aprovisionada de Security Copilot

*Respuesta: b).* El descubrimiento y la postura de agentes de Foundry y de terceros pasaron a requerir Agent 365. [Fuente](https://learn.microsoft.com/en-us/azure/defender-for-cloud/ai-security-posture) · Repasa [X4](04_Nivel_4_SOC_agentico.md#x4)

**13. En Project Perception, ¿qué roles configuran los agentes y cuáles los usan?**

- a) Global Administrator configura y Global Reader usa
- b) Copilot owner configura y Copilot contributor usa
- c) Agent ID Administrator configura y Cloud Application Administrator usa
- d) Security Admin instala y configura; Security Reader usa y ve las sesiones  ✅

*Respuesta: d).* Perception usa roles de Entra: Security Admin configura y Security Reader usa; además muestra métricas por agente. [Fuente](https://learn.microsoft.com/en-us/security/agentic-security/agentic-security-agents) · Repasa [X4](04_Nivel_4_SOC_agentico.md#x4)

**14. ¿Qué controles de operación comunes ofrece Security Copilot para sus agentes?**

- a) Feedback, memoria, ejecutar o pausar, editar y quitar  ✅
- b) Solo activar y desactivar
- c) Solo cambiar la identidad
- d) Ninguno: se gestionan desde Azure

*Respuesta: a).* Estos controles son la base del procedimiento de parada y de la mejora continua de cada agente. [Fuente](https://learn.microsoft.com/en-us/copilot/security/agents-manage) · Repasa [X4](04_Nivel_4_SOC_agentico.md#x4)

**15. En la serie oficial IdentityDrift, ¿cuál es el orden de trabajo?**

- a) Agente en Security Copilot, datos y prototipo
- b) Prototipo en Foundry, publicación en el Store y datos
- c) Datos sintéticos en el data lake, prototipo en Foundry y agente en Security Copilot  ✅
- d) Logic Apps, Copilot Studio y Foundry

*Respuesta: c).* La serie empieza por los datos en el data lake, prototipa en Foundry con la herramienta de exploración de Sentinel y termina en el agent builder. [Fuente](https://learn.microsoft.com/en-us/azure/sentinel/isv/build-agent-security-copilot) · Repasa [X5](04_Nivel_4_SOC_agentico.md#x5)

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

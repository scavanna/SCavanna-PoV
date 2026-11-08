# Evaluaciones y respuestas

*Seguridad de agentes de IA en Microsoft Foundry Ninja Training · Edición 2026*

[← Comunidad](05_Comunidad.md) · [Índice del programa](README.md) · [Laboratorio y práctica en producción →](07_Laboratorio_y_practica_en_produccion.md)

<a id="respuestas"></a>

Cada evaluación tiene preguntas de opción múltiple. Con 80 % o más el nivel se considera aprobado. Es una autoevaluación de esta guía, no una certificación de Microsoft.

<a id="eval-inicial"></a>

## Nivel 1 · Inicial · Fundamentos de la arquitectura segura

**1. ¿Qué describe correctamente a la nueva generación de Foundry Agent Service?**

- a) Un SDK de código abierto que solo se ejecuta en tu equipo
- b) El runtime administrado de agentes de Foundry, basado en la Responses API  ✅
- c) El nombre nuevo de Copilot Studio para desarrolladores profesionales de agentes
- d) Una API de Azure OpenAI limitada a Assistants y threads

*Respuesta: b).* Foundry Agent Service es el runtime administrado de agentes de Foundry y se basa en la Responses API; ofrece prompt agents (declarativos) y hosted agents (tu código en contenedores administrados). Los Assistants son la generación clásica, que se retira el 31 de marzo de 2027. [Fuente](https://devblogs.microsoft.com/foundry/foundry-agent-service-ga/) · Repasa [P0](01_Nivel_1_Inicial.md#p0)

**2. En un proyecto de Foundry con red aislada, ¿qué herramienta del agente sigue saliendo por un endpoint público?**

- a) Azure AI Search
- b) Un servidor MCP privado en tu subred
- c) Code Interpreter
- d) Grounding with Bing Search  ✅

*Respuesta: d).* Bing Grounding, Web Search y SharePoint Grounding funcionan con red aislada, pero salen por endpoint público. AI Search usa private endpoint, el MCP privado sale por tu subred y Code Interpreter usa la red troncal de Microsoft. [Fuente](https://learn.microsoft.com/en-us/azure/foundry/how-to/configure-private-link) · Repasa [P0](01_Nivel_1_Inicial.md#p0)

**3. ¿Qué examen reemplazó a AZ-500, retirado el 31 de agosto de 2026?**

- a) SC-500 (Cloud and AI Security Engineer Associate)  ✅
- b) SC-100 (Cybersecurity Architect Expert)
- c) AI-103 (Developing AI Apps and Agents on Azure)
- d) SC-401 (Information Security Administrator Associate)

*Respuesta: a).* SC-500 reemplaza a AZ-500. Su bloque «Implement security for AI» pide, entre otras habilidades, desplegar el AI gateway de API Management para Foundry, habilitar Defender for AI Services y configurar guardrails de agentes; todavía no tiene Practice Assessment. [Fuente](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-500) · Repasa [F0](01_Nivel_1_Inicial.md#f0)

**4. Al 7 de noviembre de 2026, ¿existe un Ninja oficial de Microsoft dedicado a la seguridad de Foundry o de la IA?**

- a) Sí: el «Foundry Security Ninja», publicado en 2026
- b) Sí: un módulo de IA dentro del último Ninja de Defender
- c) No: lo más cercano son rutas de Learn y la certificación SC-500  ✅
- d) Sí: el «AI Ninja», con certificado oficial dentro de AI Skills Navigator

*Respuesta: c).* La etiqueta «ninja training» de Tech Community no tiene ningún Ninja de IA; el más reciente es «Become a Microsoft Defender Ninja», del 19 de octubre de 2026. Este programa es complementario y no oficial. [Fuente](https://techcommunity.microsoft.com/tag/ninja%20training) · Repasa [F0](01_Nivel_1_Inicial.md#f0)

**5. Un banco de México exige que la inferencia no salga de una zona definida. ¿Qué es correcto?**

- a) Existe una Data Zone de América Latina
- b) Global Standard garantiza el procesamiento en la región del recurso
- c) Data Zone solo existe para EE. UU., la UE y APAC  ✅
- d) El tipo Developer garantiza la residencia de los datos

*Respuesta: c).* Los despliegues Data Zone procesan dentro de EE. UU., la UE o APAC; Global procesa en cualquier región y Developer no ofrece SLA ni residencia. No hay Data Zone de América Latina: hay que evaluar Standard o Regional Provisioned en una región aceptada. [Fuente](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/deployment-types) · Repasa [F1](01_Nivel_1_Inicial.md#f1)

**6. ¿Qué ocurre el 1 de diciembre de 2026 en Microsoft Foundry?**

- a) Se retiran los workflows de Foundry  ✅
- b) Los hosted agents pasan a disponibilidad general
- c) Se retiran los agentes clásicos (Assistants)
- d) Cambian de nombre los roles Azure AI User

*Respuesta: a).* Los workflows de Foundry, en preview, se retiran el 1 de diciembre de 2026. Los hosted agents están en GA desde el 9 de julio de 2026 y los agentes clásicos se retiran el 31 de marzo de 2027. [Fuente](https://learn.microsoft.com/en-us/azure/foundry/concepts/general-availability) · Repasa [F1](01_Nivel_1_Inicial.md#f1)

**7. En el modelo de responsabilidad compartida para agentes PaaS como Foundry Agent Service, ¿qué conserva siempre el cliente?**

- a) El hosting del modelo base y sus pesos
- b) La aprobación humana de las acciones de alto impacto  ✅
- c) La seguridad de la infraestructura física de los centros de datos
- d) El runtime del agente y el hosting de sus contenedores

*Respuesta: b).* En PaaS, el cliente posee instrucciones, selección y permisos de herramientas, lógica de orquestación, diseño de memoria e identidad del agente, y siempre la aprobación humana de acciones de alto impacto; Microsoft aporta runtime, hosting de modelos e infraestructura. La autonomía no reduce la responsabilidad. [Fuente](https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility-ai-agent) · Repasa [F1](01_Nivel_1_Inicial.md#f1)

**8. La infografía atribuye a «Defender for AI» la detección de «data poisoning» y «model misuse». ¿Qué es correcto?**

- a) Ambas alertas existen desde 2025 en Defender for AI Services
- b) Solo existe la alerta de data poisoning, en preview
- c) Ninguna de las dos existe como alerta de Defender for AI Services  ✅
- d) Ambas existen, pero solo se activan con una licencia de Agent 365 por usuario

*Respuesta: c).* La lista de alertas de Defender for AI Services no incluye «data poisoning» ni «model misuse». El envenenamiento se mitiga con integridad y permisos en el grounding y con evaluaciones. [Fuente](https://learn.microsoft.com/en-us/azure/defender-for-cloud/alerts-ai-workloads) · Repasa [F2](01_Nivel_1_Inicial.md#f2)

**9. Desde el 1 de julio de 2026, ¿qué capacidad de seguridad para Foundry requiere Microsoft Agent 365?**

- a) Defender for AI Services para modelos como Azure OpenAI
- b) El descubrimiento de cuentas y proyectos de Foundry en Defender CSPM con AI-SPM
- c) Los guardrails de Foundry
- d) El descubrimiento, la postura y la detección de amenazas a nivel de agente  ✅

*Respuesta: d).* La seguridad a nivel de agente pasó a Agent 365. Defender CSPM sigue descubriendo cuentas y proyectos y Defender for AI Services sigue cubriendo los modelos; los guardrails son de Foundry y no dependen de Agent 365. [Fuente](https://learn.microsoft.com/en-us/defender-xdr/security-for-ai/transition-agent-security-to-agent-365) · Repasa [F2](01_Nivel_1_Inicial.md#f2)

**10. En el OWASP Top 10 for Agentic Applications, publicado el 9 de diciembre de 2025, ¿qué riesgo es ASI04?**

- a) Agent Goal Hijack
- b) Agentic Supply Chain Vulnerabilities  ✅
- c) Rogue Agents
- d) Cascading Failures

*Respuesta: b).* ASI04 es Agentic Supply Chain Vulnerabilities. ASI01 es Agent Goal Hijack, ASI08 Cascading Failures y ASI10 Rogue Agents. [Fuente](https://genai.owasp.org/2025/12/09/owasp-top-10-for-agentic-applications-the-benchmark-for-agentic-security-in-the-age-of-autonomous-ai/) · Repasa [F3](01_Nivel_1_Inicial.md#f3)

**11. Según la v2.0 de la taxonomía de modos de fallo agénticos de Microsoft, ¿cuál fue el fallo más explotado en 12 meses de red teaming?**

- a) La fuga del prompt de sistema
- b) El bypass del humano en el circuito  ✅
- c) El agotamiento de la cuota de tokens
- d) El ataque visual a agentes de uso de computadora

*Respuesta: b).* La actualización del 4 de junio de 2026 indica que el bypass del humano en el circuito (HitL) fue el fallo más explotado; por eso la aprobación humana debe ligarse a la acción y a sus argumentos. [Fuente](https://www.microsoft.com/en-us/security/blog/2026/06/04/updating-taxonomy-failure-modes-agentic-ai-systems-year-red-teaming-taught-us/) · Repasa [F3](01_Nivel_1_Inicial.md#f3)

**12. ¿Qué rol permite solo interactuar con el endpoint de un agente concreto?**

- a) Foundry User
- b) Azure AI Developer
- c) Cognitive Services OpenAI User asignado en el proyecto
- d) Foundry Agent Consumer en el ámbito del agente  ✅

*Respuesta: d).* Foundry Agent Consumer solo permite invocar agentes y se puede asignar a un proyecto o a un agente concreto con la CLI. Foundry User permite construir; Azure AI Developer aplica a hubs y no a proyectos de Foundry. [Fuente](https://learn.microsoft.com/en-us/azure/foundry/concepts/rbac-foundry) · Repasa [F4](01_Nivel_1_Inicial.md#f4)

**13. Deshabilitaste la autenticación local de un recurso de Foundry durante un incidente. ¿Qué haces antes de darlo por contenido?**

- a) Nada: el corte de las claves es inmediato y definitivo
- b) Reiniciar el recurso para forzar el cambio
- c) Verificar que la clave antigua devuelva 401  ✅
- d) Eliminar el proyecto y crear uno nuevo

*Respuesta: c).* La desactivación de las claves no es inmediata: la puerta de enlace puede aceptar claves válidas durante minutos u horas. Verifica con una llamada que devuelva 401 y documéntalo en el runbook. [Fuente](https://learn.microsoft.com/en-us/azure/ai-services/disable-local-auth) · Repasa [F4](01_Nivel_1_Inicial.md#f4)

**14. ¿Qué licencia exige el acceso condicional dirigido a identidades de agente?**

- a) Entra ID P1 sin otros complementos
- b) Microsoft 365 E5 con Entra ID P2 y Defender for Identity
- c) Workload ID Premium para cada agente
- d) Microsoft 365 E7, o Agent 365 con Entra ID P1 o E3  ✅

*Respuesta: d).* El acceso condicional para agentes requiere E7, o Agent 365 con Entra ID P1 o E3; además, las API keys lo evitan por completo. Este programa enseña la alternativa: sin claves, RBAC mínimo, red privada y deshabilitar el blueprint. [Fuente](https://learn.microsoft.com/en-us/entra/identity/conditional-access/agent-id) · Repasa [F4](01_Nivel_1_Inicial.md#f4)

**15. ¿Por qué el laboratorio envía las trazas a OpenTelemetry local o a una suscripción de pago por uso?**

- a) Porque Application Insights está excluido del crédito de Visual Studio  ✅
- b) Porque Foundry no admite Application Insights como destino
- c) Porque las trazas de agentes solo funcionan en la región Brazil South de Azure
- d) Porque OpenTelemetry está prohibido en suscripciones de pago

*Respuesta: a).* Application Insights está excluido del crédito; con el límite de gasto activo, un servicio excluido suspende la suscripción. La alternativa es exportar las trazas a la consola o por OTLP, o usar una segunda suscripción de pago por uso. [Fuente](https://azure.microsoft.com/en-us/pricing/member-offers/credit-for-visual-studio-subscribers/) · Repasa [F5](01_Nivel_1_Inicial.md#f5)

<a id="eval-intermedio"></a>

## Nivel 2 · Intermedio · Construir y desplegar con seguridad

**1. En Microsoft Agent Framework, ¿qué ocurre por defecto con las herramientas de función?**

- a) Siempre piden aprobación humana
- b) Se ejecutan sin aprobación salvo que las marques  ✅
- c) Piden aprobación solo cuando la herramienta escribe datos externos
- d) Quedan deshabilitadas hasta firmarlas

*Respuesta: b).* Por defecto todas las herramientas se ejecutan sin aprobación. Las de efectos laterales se marcan con approval_mode="always_require" en Python o con ApprovalRequiredAIFunction en .NET. [Fuente](https://learn.microsoft.com/en-us/agent-framework/concepts/agents/safety) · Repasa [M1](02_Nivel_2_Intermedio.md#m1)

**2. ¿Qué requiere el middleware de Purview de Agent Framework?**

- a) No requiere ninguna licencia adicional
- b) Microsoft 365 E3 con Entra ID P1 y Defender for Cloud Apps
- c) Una licencia de Agent 365 por usuario
- d) Microsoft 365 E5 y pago por uso de Purview  ✅

*Respuesta: d).* PurviewPolicyMiddleware (Python) y WithPurview (.NET) bloquean en línea con DLP y registran para Audit, pero requieren Microsoft 365 E5 y pago por uso; además están en preview. [Fuente](https://learn.microsoft.com/en-us/agent-framework/integrations/by-component/middleware/purview) · Repasa [M1](02_Nivel_2_Intermedio.md#m1)

**3. ¿Qué configuración de Foundry Agent Service permite el aislamiento de red saliente del agente con tu propia VNet?**

- a) La estándar, con tu VNet definida al crear el recurso  ✅
- b) La básica, protegida con un private endpoint
- c) Cualquier configuración asociada a un Network Security Perimeter
- d) La básica, porque el estado lo administra Microsoft

*Respuesta: a).* El aislamiento saliente con tu VNet solo existe en la configuración estándar y se define al crear el recurso; el private endpoint solo protege la entrada. [Fuente](https://learn.microsoft.com/en-us/azure/foundry/agents/environment-setup) · Repasa [M2](02_Nivel_2_Intermedio.md#m2)

**4. En la herramienta MCP de Foundry, ¿qué efecto tiene allowed_tools=[]?**

- a) Bloquea todas las herramientas
- b) Permite todas las herramientas del servidor  ✅
- c) Habilita solo las herramientas marcadas como de lectura
- d) Provoca un error de validación

*Respuesta: b).* Una lista vacía permite todas las herramientas del servidor. Declara siempre una lista no vacía y require_approval de forma explícita. [Fuente](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/model-context-protocol) · Repasa [M2](02_Nivel_2_Intermedio.md#m2)

**5. Usas Grounding with Bing Search en un proyecto con red aislada. ¿Qué es correcto?**

- a) El tráfico queda dentro de tu VNet
- b) Requiere un private endpoint de Bing
- c) Los datos salen del límite de cumplimiento y el DPA no aplica  ✅
- d) Solo se admite con modelos que no son de OpenAI y en regiones europeas

*Respuesta: c).* Web Search y Grounding with Bing son First Party Consumption Services: el DPA no aplica, los datos salen del límite de cumplimiento y de la geografía de Azure, y se comportan como endpoint público. [Fuente](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/bing-tools) · Repasa [M2](02_Nivel_2_Intermedio.md#m2)

**6. ¿Qué detección viene apagada en el guardrail Microsoft.DefaultV2?**

- a) Ataques del usuario para saltarse las reglas (jailbreak)
- b) Material protegido de texto
- c) Autolesión
- d) Ataques en documentos (inyección indirecta)  ✅

*Respuesta: d).* La detección de ataques en documentos está apagada por defecto y hay que activarla. Los ataques del usuario, el material protegido y las categorías de daño vienen activos. [Fuente](https://learn.microsoft.com/en-us/azure/foundry/guardrails/default-safety-policies) · Repasa [M3](02_Nivel_2_Intermedio.md#m3)

**7. Un agente usa un despliegue con un guardrail estricto, pero tiene asignado otro guardrail más laxo. ¿Qué se aplica?**

- a) Solo el del agente, que reemplaza al del modelo  ✅
- b) El más restrictivo de los dos
- c) La combinación de ambos guardrails
- d) Solo el del modelo, porque el de agente es preview

*Respuesta: a).* El guardrail asignado al agente reemplaza por completo al del despliegue; si no se asigna ninguno, el agente hereda el del modelo. [Fuente](https://learn.microsoft.com/en-us/azure/foundry/guardrails/guardrails-overview) · Repasa [M3](02_Nivel_2_Intermedio.md#m3)

**8. Tu agente usa una herramienta MCP y configuraste el control de ataques indirectos en la respuesta de herramienta. ¿Qué esperas?**

- a) Un bloqueo garantizado en la respuesta
- b) Ningún efecto: MCP no está entre las herramientas moderadas  ✅
- c) La conversión automática de la herramienta MCP a una herramienta OpenAPI
- d) La aplicación del control solo a la salida final

*Respuesta: b).* Los puntos de intervención en herramientas solo moderan las herramientas listadas (AI Search, Functions, OpenAPI, SharePoint, Fabric, Bing, Bing Custom Search y Browser Automation). Para MCP y A2A, la alternativa documentada es llm-content-safety en API Management. [Fuente](https://learn.microsoft.com/en-us/azure/foundry/guardrails/intervention-points) · Repasa [M3](02_Nivel_2_Intermedio.md#m3)

**9. ¿Qué código devuelve llm-token-limit cuando se agota la cuota de tokens del periodo?**

- a) 429
- b) 503
- c) 403  ✅
- d) 401

*Respuesta: c).* El 429 corresponde a superar el límite de tokens por minuto; el 403, a agotar la cuota del periodo. [Fuente](https://learn.microsoft.com/en-us/azure/api-management/llm-token-limit-policy) · Repasa [M4](02_Nivel_2_Intermedio.md#m4)

**10. ¿Cuál es el valor por defecto del atributo shield-prompt de llm-content-safety?**

- a) false: hay que activarlo explícitamente  ✅
- b) true en todos los tiers, incluido Consumption
- c) Depende del tier de APIM
- d) El atributo no existe

*Respuesta: a).* shield-prompt viene en false; hay que activarlo para usar Prompt Shields en el gateway. Con streaming, la política corta el flujo sin devolver 403. [Fuente](https://learn.microsoft.com/en-us/azure/api-management/llm-content-safety-policy) · Repasa [M4](02_Nivel_2_Intermedio.md#m4)

**11. ¿Qué es correcto sobre el tier AI Gateway de API Management al 7 de noviembre de 2026?**

- a) GA con SLA en todas las regiones
- b) Preview, sin SLA ni precio, en dos regiones  ✅
- c) El nombre nuevo del tier Consumption
- d) Obligatorio para usar las políticas llm-* en cualquier tier

*Respuesta: b).* El tier AI Gateway está en preview pública desde el 27 de julio de 2026, sin SLA ni precio y solo en dos regiones fuera de MCSA. Las políticas llm-* funcionan en los tiers regulares. [Fuente](https://learn.microsoft.com/en-us/azure/api-management/ai-gateway-overview) · Repasa [M4](02_Nivel_2_Intermedio.md#m4)

**12. En la arquitectura baseline de Foundry, ¿por qué no se aplica inspección TLS del firewall al egreso de los agentes?**

- a) La inspección TLS saliente no existe en Azure Firewall Premium
- b) Su costo por GB es demasiado alto
- c) La bloquea el Network Security Perimeter
- d) El certificado de inspección puede romper las conexiones  ✅

*Respuesta: d).* La baseline advierte que la inspección TLS con certificados propios puede romper las conexiones de los agentes. La inspección TLS saliente existe en Azure Firewall Premium. [Fuente](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/architecture/baseline-microsoft-foundry-chat) · Repasa [M5](02_Nivel_2_Intermedio.md#m5)

**13. ¿Qué requisito tiene la subred de agentes cuando usas tu propia VNet?**

- a) Delegada a Microsoft.App/environments y dedicada a un recurso  ✅
- b) Compartida entre varios recursos de Foundry de la misma suscripción
- c) Ubicada en cualquier región de la geografía
- d) Modificable después del despliegue

*Respuesta: a).* La subred debe estar delegada a Microsoft.App/environments, tener al menos /27 (se recomienda /24), ser exclusiva de un recurso de Foundry y estar en su misma región; no se puede cambiar después: hay que redesplegar. [Fuente](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/virtual-networks) · Repasa [M5](02_Nivel_2_Intermedio.md#m5)

**14. En los permisos por documento de Azure AI Search, ¿qué está en GA al 7 de noviembre de 2026?**

- a) Las etiquetas de Purview
- b) Las ACL de SharePoint
- c) Los filtros de seguridad del backend  ✅
- d) Las ACL de ADLS Gen2 y de los blobs del índice

*Respuesta: c).* Los filtros de seguridad están en GA; las ACL y el RBAC de ADLS Gen2 y blobs, las ACL de SharePoint y las etiquetas de Purview están en preview con la API 2026-08-01-preview. [Fuente](https://learn.microsoft.com/en-us/azure/search/search-document-level-access-overview) · Repasa [M6](02_Nivel_2_Intermedio.md#m6)

**15. Tu política de modelos aprobados usa un asset ID terminado en «/models/gpt-5», sin barra final. ¿Qué pasa?**

- a) Solo permite exactamente el modelo GPT-5 indicado
- b) La asignación falla
- c) Permite también otras versiones por prefijo  ✅
- d) Bloquea todos los modelos

*Respuesta: c).* Los asset IDs se comparan como prefijo: sin la barra final, la política también admite versiones cuyo identificador empieza igual. Termina el ID con «/» para fijar un modelo. [Fuente](https://learn.microsoft.com/en-us/azure/foundry/how-to/model-deployment-policy) · Repasa [M7](02_Nivel_2_Intermedio.md#m7)

<a id="eval-avanzado"></a>

## Nivel 3 · Avanzado · Probar, detectar y responder

**1. ¿Qué métrica clave entrega el AI Red Teaming Agent para comparar la postura de un agente antes y después de una mitigación?**

- a) La puntuación F1 sobre un conjunto de datos etiquetado
- b) El tiempo medio de detección (MTTD) de las alertas
- c) La tasa de éxito de ataques (Attack Success Rate, ASR) en un scorecard por categoría de riesgo  ✅
- d) La densidad de defectos por cada mil líneas de código

*Respuesta: c).* El agente combina PyRIT con los evaluadores de riesgo y seguridad, calcula el ASR y genera un scorecard. Ese ASR por categoría y estrategia es tu línea base: endureces guardrails o instrucciones y repites el escaneo para medir la mejora. [Fuente](https://learn.microsoft.com/en-us/azure/foundry/concepts/ai-red-teaming-agent) · Repasa [A1](03_Nivel_3_Avanzado.md#a1)

**2. Quieres probar acciones prohibidas y fuga de datos sensibles de un agente con el AI Red Teaming Agent, y tu proyecto está en Brazil South. ¿Qué limitación aplica?**

- a) Solo funciona con el SDK en local y no admite agentes
- b) Las categorías agénticas corren solo en la nube, en East US 2, France Central, Sweden Central, Switzerland West y North Central US, en un solo turno y en inglés  ✅
- c) Requiere una licencia de Microsoft Agent 365 por agente evaluado
- d) Solo evalúa workflow agents, no prompt agents

*Respuesta: b).* Las categorías agénticas (acciones prohibidas, fuga de datos sensibles, task adherence) se ejecutan en la nube en cinco regiones fuera de MCSA, en un turno y en inglés. Para equipos de la región, usa un proyecto de laboratorio en una de esas regiones con datos sintéticos y complementa en español con PyRIT. [Fuente](https://learn.microsoft.com/en-us/azure/foundry/concepts/ai-red-teaming-agent) · Repasa [A1](03_Nivel_3_Avanzado.md#a1)

**3. ¿Cómo se facturan una evaluación de seguridad y una evaluación de calidad ejecutadas en la nube de Foundry?**

- a) Ambas son gratuitas mientras el evaluador esté en preview
- b) Ambas con el medidor AI evaluations, por evaluación ejecutada
- c) Por agente evaluado al mes, con un mínimo de mil ejecuciones
- d) La de seguridad con el medidor AI evaluations (USD 20 y 60 por millón de tokens de entrada y de salida); la de calidad, como tokens del modelo juez, sin recargo  ✅

*Respuesta: d).* Los evaluadores de riesgo y seguridad usan el medidor AI evaluations; los de calidad consumen tokens del modelo juez que despliegas. Presupuesta las corridas de CI/CD con esa diferencia y limita el tamaño de los conjuntos de prueba. [Fuente](https://azure.microsoft.com/en-us/pricing/details/foundryobservability/) · Repasa [A1](03_Nivel_3_Avanzado.md#a1)

**4. Desde el 30-sep-2026, ¿cómo restringes quién ve los prompts y los argumentos de herramientas en las trazas de tus agentes?**

- a) Marcando la tabla AppGenAIContent como protegida y asignando Privileged Monitoring Data Reader solo a las identidades autorizadas  ✅
- b) Aplicando una etiqueta de confidencialidad de Purview al recurso de Application Insights
- c) Quitando el rol Log Analytics Reader a todos los usuarios del workspace
- d) Apagando el tracing del proyecto en producción

*Respuesta: a).* El contenido sensible (mensajes, instrucciones de sistema, definiciones, argumentos y resultados de herramientas) va a AppGenAIContent. Marca la tabla como protegida y da lectura con Privileged Monitoring Data Reader, idealmente con acceso JIT; el opt-out solo existe hasta el 30-sep-2027. [Fuente](https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/traces-sensitive-content) · Repasa [A2](03_Nivel_3_Avanzado.md#a2)

**5. Conectaste Application Insights a tu proyecto de Foundry y no activaste ninguna opción de grabación de contenido en el código. ¿Qué pasa con los prompts de tus prompt agents?**

- a) No se registran, porque la grabación de contenido es opt-in y está apagada
- b) Solo se registran si defines la variable de entorno de grabación en el cliente
- c) Las trazas del lado del servidor los capturan sin cambios de código; el opt-in de grabación aplica a la instrumentación del cliente  ✅
- d) Se registran, pero se borran a los siete días

*Respuesta: c).* Las trazas del servidor se activan al conectar Application Insights y capturan entradas, salidas y llamadas a herramientas. La protección real es la tabla AppGenAIContent protegida y no poner secretos en prompts ni en argumentos. [Fuente](https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/trace-agent-setup) · Repasa [A2](03_Nivel_3_Avanzado.md#a2)

**6. Agregaste el contexto de seguridad del usuario final (UserSecurityContext) a tus llamadas, pero las alertas de Defender for AI Services siguen sin mostrar al usuario. ¿Qué explicación es consistente con la documentación?**

- a) El contexto solo aparece en las alertas de severidad alta
- b) Debes activar primero la auditoría de Purview en el proyecto
- c) El plan necesita Microsoft Agent 365 para leer el contexto
- d) Llamas a los modelos con la Azure AI Model Inference API, que no lo admite, o escribiste mal un campo, lo que no hace fallar la llamada  ✅

*Respuesta: d).* UserSecurityContext (EndUserId, SourceIP y applicationName) se admite en la API de Azure OpenAI y en sus SDK recientes, no en la Azure AI Model Inference API. Los campos son opcionales y un error de escritura pasa sin aviso: valida siempre con una alerta de prueba. [Fuente](https://learn.microsoft.com/en-us/azure/defender-for-cloud/gain-end-user-context-ai) · Repasa [A3](03_Nivel_3_Avanzado.md#a3)

**7. En el plan AI services de Defender for Cloud desactivas el componente Suspicious prompt evidence. ¿Qué ocurre?**

- a) El plan deja de generar alertas de jailbreak
- b) Las alertas siguen llegando, pero el contenido de los prompts aparece enmascarado  ✅
- c) Las alertas se envían solo a Purview
- d) También se desactiva AI model security

*Respuesta: b).* Ese componente decide si el texto sospechoso se muestra en la alerta; sin él, el contenido se enmascara y la investigación pierde contexto. Data security for AI interactions (de Purview, de pago y no incluido en el plan) y AI model security son componentes distintos. [Fuente](https://learn.microsoft.com/en-us/azure/defender-for-cloud/ai-onboarding) · Repasa [A3](03_Nivel_3_Avanzado.md#a3)

**8. Sin pago por uso de Purview ni suscripción de Agent 365, ¿qué capacidad de Purview funciona para las interacciones de Foundry activadas desde el Control Plane?**

- a) Solo Purview Audit  ✅
- b) DLP que bloquea prompts con tipos de información confidencial
- c) Insider Risk Management con indicadores de IA
- d) Communication Compliance sobre las respuestas

*Respuesta: a).* Las capacidades de seguridad de datos de Purview para Foundry se facturan por pago por uso o con Agent 365; sin ellos solo queda la auditoría. Acuerda el modelo de facturación antes de prometer DLP al comité. [Fuente](https://learn.microsoft.com/en-us/azure/foundry/control-plane/how-to-manage-compliance-security) · Repasa [A4](03_Nivel_3_Avanzado.md#a4)

**9. Un agente llama al modelo con su identidad administrada desde un proyecto con red aislada. ¿Qué esperas de las políticas de seguridad de datos de Purview?**

- a) Se aplican igual, porque Purview inspecciona todo el tráfico del recurso
- b) Se aplican solo a las respuestas, no a los prompts
- c) No se aplican: requieren tokens de Entra con el contexto del usuario en /chat/completions y la integración no admite aislamiento de red  ✅
- d) Se aplican si instalas DLP de endpoint en el servidor del agente

*Respuesta: c).* El enforcement de Purview desde Foundry exige tokens de Entra del usuario en `/chat/completions` y no soporta aislamiento de red. Con identidades de aplicación, evalúa el middleware de Purview de Agent Framework, que permite indicar el usuario, y documenta el riesgo de una falsa sensación de DLP. [Fuente](https://learn.microsoft.com/en-us/azure/foundry/control-plane/how-to-manage-compliance-security) · Repasa [A4](03_Nivel_3_Avanzado.md#a4)

**10. En el playbook «See What Happened» de Microsoft AeGIS, ¿con qué se correlaciona una alerta CredentialTheftAttempt para detectar la explotación de la credencial?**

- a) Con SigninLogs de los usuarios de las 24 horas previas
- b) Con operaciones listKeys o accounts/write en AzureActivity dentro de una ventana de una hora  ✅
- c) Con DeviceNetworkEvents del equipo del desarrollador
- d) Con OfficeActivity del buzón del administrador

*Respuesta: b).* La regla busca `Microsoft.CognitiveServices/accounts/listKeys/action` o `accounts/write` en AzureActivity dentro de una hora de la alerta; las reglas corren cada 5 minutos con ventana de 30. Adapta las consultas que usan tablas de agentes cambiadas tras el 1-jul-2026. [Fuente](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/security/See-What-Happened-AI-Investigation-Playbook.pdf) · Repasa [A5](03_Nivel_3_Avanzado.md#a5)

**11. Durante un incidente necesitas impedir de inmediato que se autentiquen todas las identidades de agente creadas a partir de un mismo blueprint de Entra. ¿Qué haces?**

- a) Quitas el rol Foundry User a los desarrolladores del proyecto
- b) Borras el proyecto de Foundry
- c) Deshabilitas el blueprint, que funciona como interruptor de emergencia para todas sus identidades  ✅
- d) Rotas las API keys del recurso de Foundry

*Respuesta: c).* Deshabilitar el blueprint impide autenticarse a todas sus identidades. Rotar claves no afecta a los tokens de Entra y borrar el proyecto destruye evidencia; con licencia, ID Protection permite además confirmar el compromiso de un agente concreto. [Fuente](https://learn.microsoft.com/en-us/entra/agent-id/agent-blueprint) · Repasa [A5](03_Nivel_3_Avanzado.md#a5)

**12. Activaste el gobierno de herramientas MCP mediante el AI gateway de Foundry (preview). ¿Qué herramientas MCP pasan por API Management?**

- a) Todas las del proyecto, incluidas las que ya existían
- b) Solo las herramientas MCP nuevas creadas en el portal que no usan OAuth administrado  ✅
- c) Solo los servidores MCP del catálogo de Foundry
- d) Solo las herramientas MCP de los hosted agents

*Respuesta: b).* El gobierno vía AI gateway cubre herramientas MCP nuevas creadas en el portal sin OAuth administrado; las políticas (rate-limit-by-key, ip-filter, limpieza de encabezados) se editan en API Management. Para el resto, mantén `allowed_tools` explícito, aprobación y revisión de cambios. [Fuente](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/governance) · Repasa [A6](03_Nivel_3_Avanzado.md#a6)

**13. ¿Cuál es un límite de AI model security de Defender for Cloud que debes considerar en tu cadena de suministro de modelos?**

- a) Solo analiza modelos en formato ONNX
- b) Solo analiza modelos del catálogo de Foundry
- c) Requiere Microsoft Agent 365
- d) Analiza archivos de hasta 10 GB, con escaneo semanal y sin soporte para private link  ✅

*Respuesta: d).* El escaneo tiene límites de tamaño, frecuencia y conectividad. Compleméntalo con modelos aprobados (MCSB AI-1), registros privados y el AI BOM de AI-SPM. [Fuente](https://learn.microsoft.com/en-us/azure/defender-for-cloud/ai-model-security) · Repasa [A6](03_Nivel_3_Avanzado.md#a6)

**14. Migras una solución que usaba Connected Agents de la API clásica al nuevo Foundry Agent Service. ¿Qué la reemplaza?**

- a) La herramienta A2A o la orquestación con workflows  ✅
- b) La herramienta Toolbox, que agrupa a los agentes como funciones
- c) Function calling hacia el endpoint del otro agente con una API key
- d) La memoria compartida entre los agentes del mismo proyecto

*Respuesta: a).* Connected Agents no existe en el nuevo servicio: usa la herramienta A2A o workflows. Como los workflows de Foundry se retiran el 1-dic-2026, Microsoft recomienda Microsoft Agent Framework para orquestar en código; en ambos casos, cada salto necesita identidad y rol mínimo. [Fuente](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/agent-to-agent) · Repasa [A7](03_Nivel_3_Avanzado.md#a7)

**15. Según la versión 2.0 de la taxonomía de modos de fallo de sistemas agénticos de Microsoft, ¿qué es el escalamiento de confianza entre agentes?**

- a) La fuga de memoria entre sesiones de usuarios distintos
- b) Un ataque visual contra un agente de computer use
- c) El agotamiento de recursos por llamadas recursivas entre agentes
- d) Un agente comprometido que afirma una identidad o permisos falsos ante un orquestador que no los verifica  ✅

*Respuesta: d).* Por eso cada salto entre agentes necesita identidad verificable (Entra Agent ID), el rol mínimo (Foundry Agent Consumer) y límites de autoridad explícitos: el orquestador no debe confiar en lo que otro agente dice de sí mismo. [Fuente](https://www.microsoft.com/en-us/security/blog/2026/06/04/updating-taxonomy-failure-modes-agentic-ai-systems-year-red-teaming-taught-us/) · Repasa [A7](03_Nivel_3_Avanzado.md#a7)

<a id="eval-operacion"></a>

## Nivel 4 · Gobierno y operación · Gobernar y operar la IA en Azure

**1. Según el Digital Omnibus on AI (Reglamento (UE) 2026/1744), ¿desde cuándo aplican las obligaciones para los sistemas de alto riesgo autónomos, no integrados en productos?**

- a) 2-ago-2026
- b) 2-dic-2026
- c) 2-ago-2028
- d) 2-dic-2027  ✅

*Respuesta: d).* El Omnibus llevó el alto riesgo autónomo al 2-dic-2027 y el integrado en productos al 2-ago-2028; el 2-dic-2026 aplica el marcado de contenido generado por IA para sistemas comercializados antes del 2-ago-2026. Si tu organización ofrece sistemas en la UE desde MCSA, estas fechas te alcanzan. [Fuente](https://www.europarl.europa.eu/legislative-train/package-digital-omnibus/file-digital-omnibus-on-ai) · Repasa [O1](04_Nivel_4_Gobierno_y_operacion.md#o1)

**2. ¿Qué control del dominio de IA del MCSB v2 apunta a los ataques a la cadena de suministro con un registro central de modelos, validación automática y aprobación en varias etapas?**

- a) AI-1 · Usar solo modelos aprobados  ✅
- b) AI-4 · Mínimo privilegio para las funciones de los agentes
- c) AI-6 · Monitoreo y detección
- d) AI-7 · Red teaming continuo

*Respuesta: a).* AI-1 se respalda con una política en preview que limita los despliegues a modelos de registros aprobados, en Audit o Deny. El MCSB es una guía con políticas asociadas, no una certificación. [Fuente](https://learn.microsoft.com/en-us/security/benchmark/azure/mcsb-v2-artificial-intelligence-security) · Repasa [O1](04_Nivel_4_Gobierno_y_operacion.md#o1)

**3. A fines de octubre de 2026, ¿qué pasó con el proyecto de ley de IA de Chile basado en riesgos (boletines 15869-19 y 16821-19)?**

- a) Se promulgó y entró en vigor con multas de hasta 20.000 UTM
- b) La Comisión de Desafíos del Futuro del Senado aprobó por unanimidad legislarlo (26-oct-2026), sin la indicación sustitutiva del Gobierno; sigue en trámite  ✅
- c) Se archivó y lo reemplazó la moción sobre agentes del Boletín 18.820-19
- d) El Tribunal Constitucional lo declaró inadmisible

*Respuesta: b).* Sigue en trámite, con un plazo de indicaciones propuesto hasta el 4-dic-2026. El Boletín 18.820-19 (28-oct-2026) es una moción aparte sobre identidad y trazabilidad de agentes. Prepara inventario y evaluaciones de riesgo sin tratarlo como ley vigente. [Fuente](https://www.latribuna.cl/politica/2026/11/04/chile-avanza-hacia-una-ley-que-podria-prohibir-usos-de-la-inteligencia-artificial-y-aplicar-multas-millonarias.html) · Repasa [O1](04_Nivel_4_Gobierno_y_operacion.md#o1)

**4. Tu auditor pide evidencia de un sistema de gestión de IA. ¿Qué valor tiene la certificación ISO/IEC 42001 de Microsoft, que incluye a Foundry en su alcance?**

- a) Certifica automáticamente tu propio sistema de gestión de IA
- b) Reemplaza las evaluaciones que exige la Ley de IA de la UE
- c) Es evidencia del proveedor, útil en tu gestión de terceros, pero no sustituye tu propio sistema de gestión de IA  ✅
- d) Solo aplica a Microsoft 365 Copilot, no a Foundry

*Respuesta: c).* Foundry está en el alcance certificado de Microsoft, lo que sirve como evidencia de proveedor. Si buscas alinearte o certificarte, tu organización debe operar su propio sistema: políticas, roles, riesgos y mejora continua. [Fuente](https://learn.microsoft.com/en-us/compliance/regulatory/offering-iso-42001) · Repasa [O1](04_Nivel_4_Gobierno_y_operacion.md#o1)

**5. ¿Qué rol mínimo permite detener o bloquear un agente desde el Foundry Control Plane?**

- a) Reader
- b) Foundry User
- c) Contributor  ✅
- d) Cost Management Reader

*Respuesta: c).* Detener o bloquear exige Contributor. Asígnalo de forma acotada a quien opera la contención y ensaya el procedimiento en el simulacro, porque es una de las palancas más rápidas en un incidente. [Fuente](https://learn.microsoft.com/en-us/azure/foundry/control-plane/how-to-manage-agents) · Repasa [O2](04_Nivel_4_Gobierno_y_operacion.md#o2)

**6. Al crear un blueprint de agente en Entra, ¿qué responsable exige la plataforma?**

- a) Un sponsor, persona o grupo responsable del agente; el owner es recomendado  ✅
- b) Un owner técnico; el sponsor es opcional
- c) Un Global Administrator como aprobador de cada identidad
- d) Ninguno, porque Foundry gobierna la identidad

*Respuesta: a).* Los blueprints exigen sponsor (responsabilidad de negocio sobre el ciclo de vida y el acceso) y recomiendan owner (configuración técnica). En el RACI, el sponsor es quien rinde cuentas de la existencia del agente y de su recertificación. [Fuente](https://learn.microsoft.com/en-us/entra/agent-id/create-blueprint) · Repasa [O2](04_Nivel_4_Gobierno_y_operacion.md#o2)

**7. ¿Qué combinan las políticas de ciclo de vida (preview) de Entra ID Governance para identidades de agente?**

- a) Solo la caducidad de los secretos del blueprint a los 90 días
- b) El borrado automático de los agentes sin trazas durante 30 días
- c) Una revisión de acceso trimestral fija que aprueba el Global Administrator
- d) Reconfirmación periódica (de 30 a 730 días), un mínimo de sponsors e inactividad sin tokens emitidos, con acciones, periodo de gracia y destinatarios de respaldo  ✅

*Respuesta: d).* Requieren Microsoft 365 E7, o Agent 365 con Entra ID P1 o Microsoft 365 E3, y el rol Lifecycle Workflows Administrator o AI Administrator. Sin esa licencia, sustitúyelas por una revisión manual periódica del inventario con sponsors obligatorios. [Fuente](https://learn.microsoft.com/en-us/entra/id-governance/agent-lifecycle-policies) · Repasa [O2](04_Nivel_4_Gobierno_y_operacion.md#o2)

**8. En el mapeo de roles por persona de Foundry, ¿qué rol mínimo necesita el líder técnico para publicar agentes?**

- a) Foundry User en el proyecto
- b) Foundry Project Manager sobre el recurso  ✅
- c) Azure AI Developer en el hub
- d) Cognitive Services Contributor en la suscripción

*Respuesta: b).* Publicar requiere al menos Foundry Project Manager sobre el recurso, que además solo puede asignar Foundry User. Azure AI Developer aplica a hubs y Azure Machine Learning, no a proyectos de Foundry. [Fuente](https://learn.microsoft.com/en-us/azure/foundry/concepts/rbac-foundry) · Repasa [O2](04_Nivel_4_Gobierno_y_operacion.md#o2)

**9. Despliegas API Management con gateways en dos regiones y la misma política llm-token-limit de 10.000 tokens por minuto por suscripción. ¿Qué es correcto?**

- a) El contador es por gateway y no se suma entre regiones, y con streaming o solicitudes concurrentes el límite puede superarse temporalmente  ✅
- b) El contador se comparte entre regiones mediante una caché global
- c) La política solo funciona en el tier Premium clásico
- d) Al superar el límite, API Management encola las solicitudes hasta el minuto siguiente

*Respuesta: a).* Diseña la cuota con margen: los contadores no se agregan entre gateways regionales ni de workspace, los tiers v2 usan token bucket y con `stream: true` los tokens se estiman. Al exceder el TPM el cliente recibe 429; al agotar la cuota del periodo, 403. [Fuente](https://learn.microsoft.com/en-us/azure/api-management/llm-token-limit-policy) · Repasa [O3](04_Nivel_4_Gobierno_y_operacion.md#o3)

**10. ¿Qué alerta de Defender for AI Services indica un posible denial of wallet por un volumen anómalo de solicitudes?**

- a) AI.Azure_AccessAnomaly
- b) AI.Azure_LLMReconnaissance
- c) AI.Azure_DOWVolumeAnomaly  ✅
- d) AI.Azure_AnomalousToolInvocation

*Respuesta: c).* Las alertas de wallet attack son DOWVolumeAnomaly y DOWDuplicateRequests, de severidad media y táctica Impact. Correlaciónalas con ApiManagementGatewayLlmLog y con las alertas de presupuesto para identificar al consumidor. [Fuente](https://learn.microsoft.com/en-us/azure/defender-for-cloud/alerts-ai-workloads) · Repasa [O3](04_Nivel_4_Gobierno_y_operacion.md#o3)

**11. ¿Cómo entró Storm-2139 en los servicios de IA generativa cuyo acceso revendió después de alterar sus capacidades?**

- a) Explotó una vulnerabilidad de día cero en el plano de control de Azure
- b) Usó credenciales de clientes expuestas en fuentes públicas  ✅
- c) Compró suscripciones legítimas con tarjetas robadas
- d) Engañó con phishing a empleados de Microsoft

*Respuesta: b).* La Unidad de Crímenes Digitales demandó a la red el 19-dic-2024 y el 27-feb-2025 nombró a cuatro desarrolladores; el expediente figura como terminado el 9-jul-2026. La lección: sin claves en código ni repositorios, `disableLocalAuth` y alertas de acceso anómalo. [Fuente](https://blogs.microsoft.com/on-the-issues/2025/02/27/disrupting-cybercrime-abusing-gen-ai/) · Repasa [O3](04_Nivel_4_Gobierno_y_operacion.md#o3)

**12. ¿Qué riesgo del OWASP Top 10 para aplicaciones de LLM 2025 cubre el denial of wallet y el consumo descontrolado de recursos?**

- a) LLM01 Prompt Injection
- b) LLM06 Excessive Agency
- c) LLM03 Supply Chain
- d) LLM10 Unbounded Consumption  ✅

*Respuesta: d).* LLM10 reemplazó al antiguo «Model Denial of Service» e incluye DoS, denial of wallet y extracción de modelos. Mitígalo con validación de entradas, límites y cuotas por usuario, timeouts y monitoreo de anomalías. [Fuente](https://genai.owasp.org/llmrisk/llm102025-unbounded-consumption/) · Repasa [O3](04_Nivel_4_Gobierno_y_operacion.md#o3)

**13. Quieres aislar la salida del Agent Service con tu propia VNet en un recurso de Foundry que ya está en uso. ¿Qué dice la documentación?**

- a) No puedes agregar la inyección de VNet a un recurso existente ni cambiar después la subred: hay que redesplegar  ✅
- b) Basta con agregar un private endpoint al recurso
- c) La activas desde el portal en cualquier momento, sin interrupción
- d) Se configura por proyecto, no por recurso, y se cambia cuando quieras

*Respuesta: a).* La red del Agent Service se decide al crear el recurso; en hosted agents, al crear la cuenta. El private endpoint solo protege el tráfico entrante. Por eso el proyecto integrador parte de una plantilla con red privada. [Fuente](https://learn.microsoft.com/en-us/azure/foundry/how-to/configure-private-link) · Repasa [O4](04_Nivel_4_Gobierno_y_operacion.md#o4)

**14. En la arquitectura baseline de Foundry, el WAF de Application Gateway empieza a devolver 403 en conversaciones largas que incluyen código o SQL. ¿Qué recomienda la arquitectura?**

- a) Pasar el WAF a modo de detección de forma permanente
- b) Deshabilitar el conjunto de reglas DRS para la ruta del chat
- c) Publicar el chat en un endpoint sin WAF
- d) Crear exclusiones acotadas al campo del cuerpo que contiene los mensajes, porque la puntuación de anomalías se acumula en conversaciones largas  ✅

*Respuesta: d).* El contenido del chat genera falsos positivos y la puntuación de anomalías se acumula hasta el 403. Las exclusiones acotadas al campo de mensajes mantienen la protección del resto de la solicitud; apagar reglas o el WAF abre la puerta que querías cerrar. [Fuente](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/architecture/baseline-microsoft-foundry-chat) · Repasa [O4](04_Nivel_4_Gobierno_y_operacion.md#o4)

**15. En tu diseño, API Management Standard v2 es el AI gateway y recibe tráfico de Internet. ¿Cómo obtienes protección DDoS para ese punto de entrada?**

- a) Habilitando Azure DDoS Protection directamente en la instancia v2
- b) Poniendo Application Gateway con WAF o Front Door delante, porque los tiers v2 no permiten habilitar DDoS Protection  ✅
- c) Con Defender for APIs, que incluye mitigación volumétrica
- d) No hace falta, porque Standard v2 incluye DDoS Network Protection

*Respuesta: b).* Los tiers v2 no permiten habilitar DDoS Protection, así que la protección volumétrica llega por el componente de entrada (Application Gateway WAF v2 con DDoS Network o IP Protection en su IP pública, o Front Door). Defender for APIs detecta amenazas de API, no mitiga volumen. [Fuente](https://learn.microsoft.com/en-us/azure/api-management/v2-service-tiers-overview) · Repasa [O4](04_Nivel_4_Gobierno_y_operacion.md#o4)

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. Los precios son de lista, en USD y sin impuestos, y cambian: confírmalos en la calculadora de precios de Azure antes de presupuestar. La infografía analizada pertenece a su autor y se usa solo como material de estudio. El contenido regulatorio y de privacidad es una referencia y no constituye asesoría legal: las decisiones corresponden a tus áreas de Legal, privacidad y cumplimiento. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 7 de noviembre de 2026

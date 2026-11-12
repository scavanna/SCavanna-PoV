# Cierre, glosario y fuentes

*Microsoft Security Copilot Ninja Training: hacia el SOC agéntico · Edición 2026*

[← Laboratorio y práctica en producción](07_Laboratorio_y_practica_en_produccion.md) · [Índice del programa](README.md)

<a id="cierre"></a>

## ¿Y ahora?

Ser Ninja de Security Copilot no es conocer todas las funciones, sino tener criterio: qué delegar a la IA, dónde poner a una persona, cuánto cuesta y cómo se demuestra el valor. Ese criterio se mantiene con práctica y con una rutina de actualización, sobre todo después de Microsoft Ignite (17 al 20 de noviembre de 2026), que puede cambiar estados de vista previa, nombres y precios.

Próximos pasos: completa la ruta SC-5006 y el knowledge check del Ninja oficial (certificado de participación al 80 %); para una certificación, el examen SC-200 incluye la investigación con Security Copilot. Continúa con los programas de la serie: Sentinel (Logic Apps, MCP y data lake), Defender XDR (agentes en Defender y el track de excelencia del SOC), Entra (Agent ID y agentes en Entra) y los programas de Purview (DSPM para IA, DLP y riesgo interno).

Si encuentras un enlace roto, un estado desactualizado o un agente nuevo, actualiza el inventario de tu organización y compártelo con tu equipo: esta guía está pensada para revisarse cada trimestre, como el Ninja original.

<a id="glosario"></a>

## Glosario

| Término | Definición |
|---|---|
| Agente | Componente de IA que trabaja con autonomía acotada sobre una tarea: usa herramientas, disparadores, instrucciones y memoria, con una identidad y permisos propios. |
| Agent 365 | Plano de control de Microsoft para registrar, gobernar y proteger agentes; disponible en general desde el 1 de mayo de 2026 e incluido en Microsoft 365 E7. |
| Agent builder | Editor sin código de Security Copilot para crear agentes con instrucciones, entradas, herramientas y disparadores. |
| Application card | Ficha de transparencia de Microsoft (antes Responsible AI FAQ) con usos previstos, límites, evaluaciones y mitigaciones de Security Copilot y de sus agentes. |
| Blueprint de agente | Plantilla y contenedor de credenciales de Entra Agent ID del que heredan permisos sus identidades de agente. |
| Capacidad aprovisionada | SCU compradas por hora en Azure (mínimo 1), facturadas por bloques de hora de reloj; lo no usado expira al final de cada hora. |
| Default Security Copilot Capacity | Capacidad virtual creada por la inclusión en E5/E7: no se factura por hora, no se puede modificar y la comparte todo el tenant. |
| Direct skill | Invocación directa de una skill concreta que evita el planificador; suele ser más rápida y consumir menos SCU. |
| DSPM for AI | Capacidad de Purview para la postura de seguridad de datos de la IA; registra los pares prompt-respuesta de Security Copilot. La versión clásica se está reemplazando por la nueva experiencia DSPM. |
| Entra Agent ID | Tipo de identidad de Microsoft Entra para agentes: sin credenciales propias, de un solo tenant y con un sponsor humano responsable. |
| Excedente (overage) | SCU adicionales que se cobran por uso real (6 USD por SCU, precio de lista) cuando se agota la capacidad; pueden tener tope. |
| Experiencia embebida | Security Copilot dentro de un portal (Defender, Entra, Intune, Purview o Azure) con el contexto de esa consola. |
| Experiencia independiente | Portal propio de Security Copilot, donde se combinan plugins de varios productos en sesiones. |
| Grounding | Enriquecimiento del prompt con datos de contexto obtenidos por plugins antes de enviarlo al modelo. |
| Humano en el circuito | Diseño en el que una persona aprueba, rechaza o corrige las acciones de un agente antes de que se ejecuten. |
| ISOC | Integrated SOC en Microsoft Defender (anunciado el 23 de septiembre de 2026): SIEM y protección como un solo sistema para personas y agentes. |
| MCP | Model Context Protocol: estándar abierto para que los agentes descubran y usen herramientas. |
| NL2Agent | Creación de agentes de Security Copilot a partir de una descripción en lenguaje natural, que se termina en el agent builder. |
| On-behalf-of | Modelo de autenticación por el que Security Copilot accede a los datos con los permisos del usuario, nunca por encima de ellos. |
| Orquestador | Componente que interpreta el prompt, elige plugins y skills, llama al modelo y compone la respuesta. |
| Plugin | Colección de herramientas (skills) que amplía lo que Security Copilot puede hacer: KQL, API, GPT, MCP o Logic Apps. |
| Project Perception | Sistema multiagente de Microsoft en el portal de Defender (vista previa limitada desde 2026) con agentes rojo, azul y verde coordinados por playbooks predefinidos. |
| Promptbook | Secuencia reutilizable de prompts con entradas parametrizadas. |
| SCU | Security Compute Unit: unidad de capacidad de Security Copilot. |
| Security Store | Vitrina de Microsoft, sobre la infraestructura de Microsoft Marketplace, para encontrar, comprar y desplegar agentes y soluciones de seguridad. |
| Sesión | Hilo de prompts y respuestas en la experiencia independiente; se puede fijar, compartir en solo lectura y convertir en promptbook. |
| Sponsor | Persona responsable de negocio de una identidad de agente en Entra. |
| Trigger | Disparador de un agente: programado, por evento o manual. |
| Workspace | Contenedor de capacidad, configuración de plugins, miembros y ubicación de datos de Security Copilot; la ubicación no se puede cambiar después de crearlo. |
| XPIA y UPIA | Inyección indirecta de prompts (instrucciones ocultas en datos que lee el agente) e inyección directa por parte del usuario. |

<a id="metodologia"></a>

## Metodología y fuentes

Esta guía se construyó con líneas de investigación en paralelo sobre fuentes públicas: la forma y la historia del Ninja oficial, cada nivel técnico, la operación y la comunidad. Cada enlace se registró solo si apareció literalmente en un resultado de búsqueda o en una página leída, y luego se consolidó, se depuró y se verificó. Se descartaron recursos retirados, alojados en espacios no públicos o duplicados. Fecha de corte: 6 de noviembre de 2026.

Puntos a confirmar en fuentes oficiales antes de recomendarlos:

- **Inclusión en tenants de prueba.** La inclusión se calcula sobre licencias de usuario pagas; que un tenant de prueba de E5 no reciba SCU es una inferencia, no una afirmación explícita de Microsoft. Tampoco está confirmado que los créditos de Visual Studio cubran el medidor de Security Copilot ([FAQ de inclusión](https://learn.microsoft.com/en-us/copilot/security/security-copilot-inclusion)).
- **Elegibilidad de otras SKU.** La FAQ define la inclusión para Microsoft 365 E5 y E7; la investigación no encontró si Microsoft Defender Suite (antes Microsoft 365 E5 Security) o E5 Compliance dan derecho a ella. Confírmalo con Microsoft ([FAQ de inclusión](https://learn.microsoft.com/en-us/copilot/security/security-copilot-inclusion)).
- **Uso por encima del pool de E5/E7.** La FAQ oficial habla de una limitación futura con opción de pago a 6 USD por SCU y aviso de 30 días; la calculadora comunitaria lo trata como excedente facturable hoy ([FAQ](https://learn.microsoft.com/en-us/copilot/security/security-copilot-inclusion), [calculadora comunitaria](https://www.scucalculator.com/)).
- **Fechas del despliegue de la inclusión.** El blog de Ignite habla de fases desde el 18-nov-2025 con 30 días de aviso; el aviso MC1261596 (25-mar-2026) fijó del 20 de abril al 30 de junio de 2026 con 7 días de aviso; el MC1478465 (24-sep-2026) se marcó el 19-oct-2026 como enviado a la audiencia equivocada ([anuncio](https://www.microsoft.com/en-us/security/blog/2025/11/18/agents-built-into-your-workflow-get-security-copilot-with-microsoft-365-e5/), [MC1261596](https://mc.merill.net/message/MC1261596), [MC1478465](https://mc.merill.net/message/MC1478465)).
- **Project Perception.** El blog oficial habla de vista previa pública desde el 3-ago-2026; Learn la describe como Limited Public Preview solo por invitación ([blog](https://blogs.microsoft.com/blog/2026/07/27/rethinking-security-for-the-age-of-ai/), [Learn](https://learn.microsoft.com/en-us/security/agentic-security/agentic-security-get-started)).
- **Security Alert Triage Agent.** El anuncio de Ignite habla de disponibilidad general del agente, pero Learn titula la página como vista previa: solo el triage de correo es GA. Las fechas del cambio de nombre desde Phishing Triage Agent (nombre anterior) también varían entre fuentes ([anuncio](https://techcommunity.microsoft.com/blog/MicrosoftDefenderforOffice365Blog/microsoft-ignite-2025-transforming-phishing-response-with-agentic-innovation/4470791), [Learn](https://learn.microsoft.com/en-us/defender-xdr/security-alert-triage-agent)).
- **Threat Intelligence Briefing Agent.** La licencia figura como «Defender EASM Standard» en la tabla independiente y como «Not Applicable» en Defender; su estado aparece como vista previa (julio de 2025) en «What's new» y como GA desde diciembre de 2025 en las noticias mensuales de Defender ([agentes independientes](https://learn.microsoft.com/en-us/copilot/security/agents-security-copilot), [agentes en Defender](https://learn.microsoft.com/en-us/defender-xdr/security-copilot-agents-defender), [noticias de enero de 2026](https://techcommunity.microsoft.com/blog/microsoftthreatprotectionblog/monthly-news---january-2026/4484885)).
- **Identity Risk Management Agent.** El catálogo de Entra lista como licencia «Microsoft Entra Agent ID», mientras que la guía exige Entra ID P2 ([catálogo](https://learn.microsoft.com/en-us/entra/security-copilot/entra-agents), [guía](https://learn.microsoft.com/en-us/entra/id-protection/identity-risk-management-agent-get-started)).
- **Access Review Agent y App Lifecycle Management Agent.** El primero se anunció en vista previa (30-sep-2025) y figura en «What's new», pero sus páginas de Learn se eliminaron el 2-abr-2026; el segundo solo aparece en la hoja de ruta como «In development» ([Entra.News](https://daily.entra.news/day/2026-04-02/), [RM536578](https://mc.merill.net/message/RM536578)).
- **Identidad de los agentes de Purview.** La ficha antigua dice que el agente corre como el administrador que lo activó (90 días); la guía de DLP recomienda identidad de agente ([ficha](https://learn.microsoft.com/en-us/purview/copilot-in-purview-agents), [guía de DLP](https://learn.microsoft.com/en-us/purview/copilot-in-purview-triage-dlp-agent-get-started)).
- **Identidad de agentes propios y de partners.** La documentación de Security Copilot dice que la opción de crear una identidad de agente solo existe para agentes de Microsoft, mientras que un blog de Entra afirma que los agentes de Security Copilot, Foundry y Copilot Studio reciben Agent ID automáticamente ([agentes](https://learn.microsoft.com/en-us/copilot/security/agents-overview), [blog de Entra](https://techcommunity.microsoft.com/blog/microsoft-entra-blog/build-ai-agents-for-production-with-secure-identities-from-day-one/4524606)).
- **Intune.** La página general de agentes (1-abr-2026) todavía lista cuatro agentes, tres de ellos retirados después (1-jun y 31-ago-2026) ([agentes de Intune](https://learn.microsoft.com/en-us/intune/copilot/agents/)).
- **Security Analyst Agent.** Learn indica vista previa en abril de 2026; un post comunitario la ubica desde el 26-mar-2026 ([What's new](https://learn.microsoft.com/en-us/copilot/security/whats-new-copilot-security), [post comunitario](https://techcommunity.microsoft.com/discussions/microsoft-security/security-copilot-agents-in-defender-xdr-where-things-actually-stand/4514689)).
- **Dynamic Threat Detection Agent.** Learn lo describe como vista previa gratuita; fuentes comunitarias del programa de Defender XDR afirman su inclusión en E5 y una GA a fines de 2026. Prevalece Learn ([Learn](https://learn.microsoft.com/en-us/defender-xdr/dynamic-threat-detection-agent)).
- **Compartición y retención de datos.** La compartición de datos está activada por defecto en el onboarding manual y desactivada en el aprovisionamiento automático de E5/E7; la misma página de privacidad indica «90 días» de retención para datos compartidos y «no más de 180 días» tras el opt-out ([privacidad](https://learn.microsoft.com/en-us/copilot/security/privacy-data-security), [aprovisionamiento automático](https://learn.microsoft.com/en-us/copilot/security/auto-provisioning-security-copilot)).
- **Excedente ilimitado en el onboarding manual.** Microsoft sugiere 3 SCU con excedente ilimitado para explorar; para laboratorios esta guía recomienda excedente en cero por el riesgo de costo ([onboarding manual](https://learn.microsoft.com/en-us/copilot/security/manual-onboarding)).
- **Estado de los workspaces.** «What's new» de junio de 2025 cita los workspaces en vista previa y la gestión de plugins por workspace en GA; otras notas de la investigación los dan por GA. Verifica en tu tenant ([What's new](https://learn.microsoft.com/en-us/copilot/security/whats-new-copilot-security)).
- **Lista de experiencias embebidas.** La página de experiencias no incluye Azure WAF ni Defender EASM, que el hub de adopción cita como integraciones (WAF es solo independiente y EASM funciona como plugin) ([experiencias](https://learn.microsoft.com/en-us/copilot/security/experiences-security-copilot), [hub de adopción](https://adoption.microsoft.com/en-us/security-copilot/)).
- **Ninja oficial.** El Ninja afirma que no hay configuración de plugins a nivel de tenant, superado por la gestión por workspace (GA en junio de 2025); además, la página muestra la versión 4.0 del 19-nov-2024 mientras el listado de etiquetas registra actividad del 8-may-2026 ([Ninja oficial](https://techcommunity.microsoft.com/blog/securitycopilotblog/how-to-become-a-microsoft-security-copilot-ninja-the-complete-level-400-training/4106928)).
- **«What's new» de Learn.** Dice actualizarse cada mes, pero su última entrada visible es de abril de 2026 ([What's new](https://learn.microsoft.com/en-us/copilot/security/whats-new-copilot-security)).
- **Autenticación del conector de Security Copilot.** La documentación de Logic Apps indica solo OAuth delegado; la referencia del conector ofrece también service principal y el ejemplo oficial de GitHub menciona certificado de cliente. La referencia todavía exige el antiguo Early Access Program ([conector](https://learn.microsoft.com/en-us/copilot/security/connector-logicapp), [referencia](https://learn.microsoft.com/en-us/connectors/securitycopilot/), [ejemplo](https://github.com/Azure/Security-Copilot/blob/main/Logic%20Apps/SecurityCopilot-Sentinel-Incident-Investigation/readme.md)).
- **Precio del entity analyzer del MCP de Sentinel.** El blog de GA lo anunció sin cargo adicional y con precios futuros por definir; las novedades de Sentinel de RSAC 2026 indican facturación en SCU desde el 1-abr-2026 ([blog de GA](https://techcommunity.microsoft.com/blog/microsoft-security-blog/microsoft-sentinel-mcp-server---generally-available-with-exciting-new-capabiliti/4470125), [RSAC 2026](https://techcommunity.microsoft.com/blog/microsoftsentinelblog/what%E2%80%99s-new-in-microsoft-sentinel-rsac-2026/4503971)).
- **Exploración de datos del MCP en tenants nuevos.** Tras el onboarding integrado del 23-sep-2026, un experto de la comunidad reportó que la API del data lake y la colección de exploración no respondían; pruébalo en cada tenant ([reporte comunitario](https://tokesi.cloud/blogs/26_09_28_integrated_data_lake/)).
- **NL2Agent.** Figura como «Private Preview, but globally available», una formulación ambigua para planificar ([NL2Agent](https://learn.microsoft.com/en-us/copilot/security/developer/build-agent-natural-language)).
- **Protección externa de Copilot Studio.** La documentación la marca como vista previa, mientras el plan de lanzamiento preveía GA en junio de 2026 ([documentación](https://learn.microsoft.com/en-us/microsoft-copilot-studio/external-security-provider), [plan de lanzamiento](https://learn.microsoft.com/en-ca/power-platform/release-plan/2025wave1/microsoft-copilot-studio/strengthen-security-copilot-studio-agents-additional-threat-protection)).
- **Purview y agentes de Foundry.** Defender for Cloud indica que su integración con Purview no incluye datos de agentes de Foundry, mientras Purview los lista como compatibles, probablemente vía Foundry Control Plane ([Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/ai-onboarding), [Purview](https://learn.microsoft.com/en-us/purview/ai-agents)).
- **Licencia de ID Protection para agentes.** Una página dice que «pronto» requerirá Agent 365, otra pide Entra ID P2 durante la vista previa y la descripción de servicio la ubica en E7 o Agent 365 ([agentes en riesgo](https://learn.microsoft.com/en-us/entra/id-protection/concept-risky-agents), [administrar identidades de agente](https://learn.microsoft.com/en-us/entra/agent-id/manage-agent-identities-admin)).
- **Microsoft Ignite 2026 (17 al 20 de noviembre).** Puede cambiar el estado de Perception, NL2Agent, plugins MCP, Security Analyst Agent, Dynamic Threat Detection Agent, la protección en tiempo de ejecución de agentes y los precios. Revisa las fuentes oficiales después del evento.

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

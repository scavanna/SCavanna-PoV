> **Anexo del Frontier CISO Atlas 1.0.** Informe de verificación de Microsoft y el concepto de empresa de frontera, hecho el 15 de noviembre de 2026 contra las páginas de los organismos emisores. Es el informe tal como lo entregó el agente de verificación; la base consolidada está en `data/base_de_referencia.json` y el resumen en `docs/04_Base_de_Referencia.md`.

Los 12 elementos quedaron verificados hoy (15-nov-2026) contra páginas oficiales de Microsoft. Tres puntos quedan parciales: el texto público del Responsible AI Standard rediseñado, la disponibilidad general del nuevo Purview DSPM y el estado individual de cada agente de Security Copilot.

Las entradas usan las claves del esquema para serializarlas tal cual; `organismo` es "Microsoft" en todas.

Lo que más cambia respecto de una base de 2025:
- El SAF fue rediseñado: cuatro componentes e IA como séptima tecnología.
- La MCRA vigente es de junio de 2026.
- El MCSB v2 sigue en versión preliminar e incluye un dominio de IA.
- Zero Trust ahora dice «assume compromise».
- Existe un catálogo público de capacidades de defensa de IA.
- Hay ediciones 2026 del Work Trend Index, del informe de la SFI, del MDDR y de la taxonomía del AI Red Team.
- Ignite 2026 es del 17 al 20 de noviembre, así que todavía no hay anuncios de esa edición.

## Base de referencia (23 entradas)

**1. Frontier Firm (concepto)**
- version_o_fecha: Work Trend Index 2025, del 23-abr-2025; actualizado por el Work Trend Index 2026 (5-may-2026) y por blogs oficiales hasta el 12-nov-2026.
- estado: concepto vigente; marco estratégico y comercial, no un estándar.
- estructura_cantidad: 3 fases (2025); 3 rasgos de la «Frontier Transformation» (2026).
- estructura_nombres: fases "Human with assistant", "Human-agent teams", "Human-led, agent-operated"; rasgos: human ambition, intelligence, trust.
- definicion: empresa basada en inteligencia disponible a demanda, equipos de personas y agentes, y el rol de «agent boss» para todos. Las fases van de la IA como asistente, a agentes que se suman a los equipos bajo dirección humana, a agentes que ejecutan procesos completos mientras las personas fijan el rumbo; no son lineales.
- url_oficial: https://www.microsoft.com/en-us/worklab/work-trend-index/2025-the-year-the-frontier-firm-is-born ; https://www.microsoft.com/en-us/worklab/work-trend-index/agents-human-agency-and-the-opportunity-for-every-organization
- novedades_2025_2026:
  - 11-nov-2025: estudio de IDC encargado por Microsoft; las Frontier Firms declaran retornos tres veces mayores que los rezagados y usan IA en siete funciones en promedio. https://blogs.microsoft.com/blog/2025/11/11/bridging-the-ai-divide-how-frontier-firms-are-transforming-business/
  - 18-nov-2025 (Ignite 2025): la Frontier Firm se describe como «human-led and agent-operated»; se anuncian Work IQ, Agent 365 y la Frontier Firm AI Initiative con Harvard D^3. https://www.microsoft.com/en-us/copilot/blog/2025/11/18/microsoft-ignite-2025-copilot-and-agents-built-to-power-the-frontier-firm/
  - 27-ene-2026: «Frontier Transformation» (presentada en Ignite 2025) sobre Intelligence + Trust, con tres rasgos: IA en el flujo de la ambición humana, innovación ubicua y observabilidad en cada capa. https://blogs.microsoft.com/blog/2026/01/27/how-microsoft-is-empowering-frontier-transformation-with-intelligence-trust/
  - 9-mar-2026: Microsoft 365 E7: The Frontier Suite (entrada 10c).
  - 5-may-2026: Work Trend Index 2026. Las Frontier Firms rediseñan el modelo operativo en tres niveles (empleados, líderes, organización). Introduce «Frontier Professionals» (16 % de los usuarios de IA encuestados), la «Transformation Paradox», la organización como «Learning System» y la «Owned Intelligence»; solo 19 % de los usuarios de IA está en la zona «Frontier». Patrones de colaboración: Author, Editor, Director, Orchestrator. https://blogs.microsoft.com/blog/2026/05/05/how-frontier-firms-are-rebuilding-the-operating-model-for-the-age-of-ai/
  - 2-jul-2026: Microsoft Frontier Company, unidad de ingeniería de IA para clientes (USD 2.500 millones, 6.000 especialistas). https://blogs.microsoft.com/blog/2026/07/02/microsoft-frontier-company-ai-engineering-that-amplifies-and-protects-your-intelligence/
  - 27-oct-2026: enfoque de plataforma: Copilot para la ambición humana, Microsoft IQ para la inteligencia, Agent 365 para la confianza y la observabilidad. https://blogs.microsoft.com/blog/2026/10/27/the-platform-approach-to-becoming-frontier/
  - 12-nov-2026: IDC 2026. Frontier Firms = 10 % superior de la escala de madurez de IA de IDC; retorno 4x frente a 2,7x; 87 % con proceso para gobernar agentes frente a 51 % de los rezagados. https://blogs.microsoft.com/blog/2026/11/12/scaling-ai-value-without-losing-control-lessons-from-frontier-firms/
  - Programa Frontier: acceso anticipado a funciones de IA en versión preliminar de Microsoft 365 Copilot; esas funciones no cumplen ISO 27001/27002/27018 ni incluyen BAA de HIPAA. https://www.microsoft.com/en-us/copilot/resources/frontier-program
  - Ignite 2026: 17 al 20-nov-2026 en San Francisco, con una keynote de socios titulada «Frontier Transformation»; aún sin anuncios. https://partner.microsoft.com/blog/article/ignite-2026-overview
- verificado: si
- nota: Agent boss: «A human manager of one or more agents». Human-agent ratio: métrica de negocio que equilibra la supervisión humana con la eficiencia de los agentes; no hay valor numérico publicado, porque la proporción correcta depende de cada tarea. Otros términos del glosario: intelligence resources, Work Chart, capacity gap y digital labor. El 71 % de quienes trabajan en estas empresas dice que su compañía prospera, frente a 37 % global.

**2. Microsoft Security Adoption Framework (SAF)**
- version_o_fecha: sin número de versión; página principal actualizada el 6-nov-2026.
- estado: vigente; rediseñado en 2026 como modelo operativo dentro de la documentación de Zero Trust.
- estructura_cantidad: 4 componentes; 5 escenarios de negocio; 9 disciplinas en 3 categorías; 7 tecnologías; 3 temas de transformación de seguridad con IA.
- estructura_nombres:
  - Componentes: Business scenarios, Security disciplines, Technologies, Technical solutions.
  - Escenarios: Rapidly and securely adopt AI; Enable people to work securely from anywhere; Minimize business damage from security incidents; Identify and protect critical business assets; Continuously improve security posture and compliance.
  - Disciplinas: Planning and oversight: Security Strategy, Integration, and Governance; Security Architecture. Technical strategy: Access and Identity; Infrastructure Security; Development Security; Data Security; OT/IoT Security. Operational: Security Posture Management; SecOps.
  - Tecnologías: Identity, Endpoints, Applications, Data, Infrastructure, Network, AI.
  - Temas de IA: secure your foundations, defend with agents, secure your agentic insider.
- definicion: modelo operativo que convierte prioridades de negocio, riesgo y principios de Zero Trust en acción coordinada entre roles de negocio, tecnología y seguridad; se apoya en la guía existente de Microsoft en lugar de reemplazarla.
- url_oficial: https://learn.microsoft.com/en-us/security/zero-trust/security-adoption-model ; talleres: https://learn.microsoft.com/en-us/security/zero-trust/workshop-business-overview ; CISO Workshop: https://learn.microsoft.com/en-us/security/zero-trust/workshop-business-security-leaders ; temas de IA: https://learn.microsoft.com/en-us/security/saf/scenarios/ai-security/overview
- novedades_2025_2026: versiones localizadas sin actualizar aún describen tres componentes; ahora son cuatro, con las soluciones técnicas. La IA figura como tecnología. Hay un nuevo punto de partida por prioridades de seguridad de IA. Al abrir la URL anterior (/security/adoption/adoption) se devolvió la página nueva.
- verificado: si
- nota:
  - Talleres: dos tipos con entrega experta vía Microsoft Unified: Security Architecture and Strategy y Technology Adoption.
  - Los de arquitectura y estrategia: Security Overview and Planning; Enterprise Security Assessment; Security Capability Adoption Planning; CISO Workshop; MCRA / Security ADS Module 1; Secure Identities (nombre truncado en la página); Modern Security Operations / Security ADS Module 3; Infrastructure & Development Security; Data Security & Governance.
  - Recursos públicos: CISO Workshop, Zero Trust Workshop, SecOps Workshop y MCRA.
  - CISO Workshop: tres partes (A contexto y fundamentos, B alineación con el negocio, C disciplinas de seguridad), con videos y PDF públicos.
  - Fechas: disciplinas y escenarios, 31-may-2026; talleres, 4-nov-2026; la página de temas de IA muestra 15-nov-2026, igual a la fecha de consulta.

**3. Microsoft Cybersecurity Reference Architectures (MCRA)**
- version_o_fecha: versión de junio de 2026, que reemplaza a la de abril de 2025; página actualizada el 6-nov-2026.
- estado: vigente.
- estructura_cantidad: 8 grupos de diagramas de arquitectura; 5 bloques de contenido.
- estructura_nombres: diagramas: Microsoft cybersecurity capabilities; Zero Trust user access; Security operations (SecOps/SOC); Operational technology (OT); Multicloud and cross-platform capabilities; Attack chain coverage; Infrastructure and development security; Security organizational functions. Contenido: antipatrones y buenas prácticas; tendencias de amenazas y patrones de ataque; priorización de extremo a extremo; guía de adopción Zero Trust; mapeo de capacidades a estándares y roles de Zero Trust.
- definicion: conjunto de arquitecturas técnicas para adoptar y modernizar la seguridad con Zero Trust, que abarca TI heredada, multinube, OT/IoT e IA; es un componente del SAF.
- url_oficial: https://learn.microsoft.com/en-us/security/zero-trust/microsoft-reference-architecture
- novedades_2025_2026: la versión de junio de 2026 incorpora Microsoft Agent 365 en la cadena de ataque, los mapeos y varias arquitecturas de referencia, suma Microsoft Foundry, actualiza casi toda la sección de IA, agrega un diagrama de seguridad de datos y actualiza el mapeo a los borradores del Zero Trust Reference Model de The Open Group.
- verificado: si
- nota: la URL anterior (/security/adoption/mcra) devolvió esta página.

**4. Microsoft cloud security benchmark (MCSB)**
- version_o_fecha: v2 (preview), página del 15-ene-2026; v1 sigue publicada como versión heredada (página del 11-nov-2025).
- estado: v2 en versión preliminar y declarada sucesora de v1; no encontré anuncio de disponibilidad general.
- estructura_cantidad: v2: 12 dominios; v1: 12 dominios.
- estructura_nombres: v2: Network security (NS), Identity Management (IM), Privileged Access (PA), Data Protection (DP), Asset Management (AM), Logging and Threat Detection (LT), Incident Response (IR), Posture and Vulnerability Management (PV), Endpoint Security (ES), Backup and Recovery (BR), DevOps Security (DS), Artificial Intelligence Security (AI). v1: los once primeros más Governance and Strategy (GS), sin AI.
- definicion: conjunto de controles de seguridad en la nube; la v2 se centra en Azure, con más de 420 definiciones de Azure Policy y guía basada en riesgos y amenazas.
- url_oficial: https://learn.microsoft.com/en-us/security/benchmark/azure/overview ; dominio AI: https://learn.microsoft.com/en-us/security/benchmark/azure/mcsb-v2-artificial-intelligence-security ; v1: https://learn.microsoft.com/en-us/security/benchmark/azure/overview-mcsb-v1
- novedades_2025_2026: la v2 agrega el dominio AI, niveles de criticidad (Must have, Should have, Nice to have) y mapeos a NIST SP 800-53 Rev.5, PCI-DSS v4, CIS Controls v8.1, NIST CSF v2.0, ISO 27001:2022 y SOC 2. El dominio GS de v1 no figura en la tabla de v2.
- verificado: si
- nota: dominio de IA: sí. Tiene siete recomendaciones: AI-1 Ensure use of approved models; AI-2 Implement multi-layered content filtering; AI-3 Adopt safety meta-prompts; AI-4 Apply least privilege for agent functions; AI-5 Ensure human-in-the-loop; AI-6 Establish monitoring and detection; AI-7 Perform continuous AI Red Teaming. Se organizan en tres pilares: AI Platform Security, AI Application Security, Monitor and Respond. Ese contenido se revisó por última vez el 1-dic-2025. El mapeo a NIST CSF 2.0 sirve directo para las 6 funciones del Atlas.

**5a. Zero Trust: principios, tecnologías y Zero Trust for AI**
- version_o_fecha: página de principios con fecha 15-nov-2026 (coincide con la consulta); Zero Trust for AI anunciado el 19-mar-2026 y ampliado el 4-ago-2026.
- estado: vigente.
- estructura_cantidad: 3 principios; 7 tecnologías; 7 áreas de control para IA.
- estructura_nombres: principios: Assume compromise (antes «assume breach»), Verify explicitly, Use least privilege access. Tecnologías: identity, endpoints, applications, data, infrastructure, networks, AI. Áreas de control para IA: Map and assess AI risk; Register agents and enforce lifecycle governance; Secure AI authentication and access; Secure AI network and service access; Secure AI data access and usage; Build and deploy agents securely; Detect and respond for AI.
- definicion: decidir la confianza de forma explícita, con contexto y riesgo, limitando privilegios y diseñando para un posible compromiso. Zero Trust for AI extiende esos principios a todo el ciclo de vida de la IA, desde la ingesta de datos y el entrenamiento hasta el despliegue y el comportamiento de los agentes.
- url_oficial: https://learn.microsoft.com/en-us/security/zero-trust/zero-trust-overview ; https://www.microsoft.com/en-us/security/blog/2026/03/19/new-tools-and-guidance-announcing-zero-trust-for-ai/ ; https://www.microsoft.com/en-us/security/blog/2026/08/04/advance-zero-trust-for-ai-new-tools-and-guidance-to-secure-ai-agents-and-devsecops/ ; https://learn.microsoft.com/en-us/security/saf/technologies/ai/overview
- novedades_2025_2026: en marzo de 2026 llegaron el pilar de IA en el Workshop, pilares de Data y Networking en el Assessment, una arquitectura de referencia Zero Trust para IA y patrones y prácticas. En agosto de 2026 se sumaron comprobaciones de IA, SecOps e Infrastructure en el Assessment, el pilar DevSecOps y guía de memoria de IA en el Workshop, y un e-book.
- verificado: si
- nota: Learn usa «assume compromise», pero los blogs de 2026 siguen diciendo «assume breach». La portada del Zero Trust Guidance Center todavía lista el conjunto clásico de pilares, con «Visibility, automation, and orchestration». La página de principios aún describe tres componentes del SAF, no cuatro.

**5b. Zero Trust Workshop**
- version_o_fecha: sin versión; página general con fecha 15-nov-2026 (coincide con la consulta); pilar de IA, 6-nov-2026.
- estado: vigente; recurso de tipo comunitario mantenido por Microsoft en GitHub, sin soporte formal.
- estructura_cantidad: 8 pilares; 3 componentes; 4 fases; 7 áreas en el pilar de IA.
- estructura_nombres: pilares: Identity, Devices, Data, Networking, Infrastructure, SecOps, DevSecOps, AI. Componentes: Assessment tool, Workshop tool, Workshop guidance. Fases: Kickoff/Orientation, Assessment (optional), Roadmap, Closeout. Pilar de IA: Map and assess AI risk; Register agents; Secure AI authentication and access; Secure AI network access; Secure AI data access; Build agents securely; Detect and respond for AI.
- definicion: guía y herramienta para armar una estrategia y una hoja de ruta de implementación Zero Trust a partir de datos reales de evaluación; los resultados se ordenan en el esquema First, Then, Next.
- url_oficial: https://learn.microsoft.com/en-us/security/zero-trust/workshop-zero-trust-overview ; https://learn.microsoft.com/en-us/security/zero-trust/workshop-zero-trust-ai-security ; https://zerotrust.microsoft.com/
- novedades_2025_2026: con el pilar de IA (mar-2026) el Workshop pasó a cubrir 700 controles en 116 grupos lógicos y 33 carriles funcionales; el pilar DevSecOps (ago-2026) tiene 15 grupos de control y 91 tareas; el pilar de IA incorpora guía basada en el Microsoft AI Memory framework.
- verificado: si
- nota: el pilar de IA corresponde a la tecnología AI del SAF; SecOps y DevSecOps corresponden a disciplinas del SAF. La copia indexada por el buscador muestra una lista más larga de áreas del pilar de IA (gobierno y responsabilidad, registro y ciclo de vida de agentes, acceso de agentes a herramientas, pasarelas de IA, memoria de agentes) que la versión que abrí. Conviene revisarla después de Ignite 2026.

**5c. Zero Trust Assessment**
- version_o_fecha: la release 2.6.0 introdujo el informe rediseñado y los siete pilares por defecto; página con fecha 15-nov-2026.
- estado: vigente; proyecto comunitario mantenido por empleados de Microsoft, no es un producto oficial y se entrega sin soporte.
- estructura_cantidad: 7 pilares.
- estructura_nombres: Identity, Devices, Network, Data, Infrastructure, Security operations (SecOps), AI.
- definicion: módulo de PowerShell que compara la configuración del tenant de Microsoft 365 y de Azure con recomendaciones de seguridad; no remedia, genera informes locales; su JSON puede importarse al Workshop.
- url_oficial: https://learn.microsoft.com/en-us/security/zero-trust/assessment/overview
- novedades_2025_2026: Data y Network se sumaron en marzo de 2026; AI, Security Operations e Infrastructure en agosto de 2026.
- verificado: si
- nota: las comprobaciones se apoyan en aprendizajes de la SFI.

**6a. Cloud Adoption Framework (CAF): fases y Secure**
- version_o_fecha: página general del 4-sep-2026; Secure del 15-sep-2025.
- estado: vigente.
- estructura_cantidad: 7 fases de adopción de Azure; 6 escenarios; Secure: 4 bloques.
- estructura_nombres: fases: Strategy, Plan, Ready, Adopt, Govern, Secure, Manage. Escenarios: Azure adoption, Unified data platform, AI adoption, AI agents, Sovereignty, Azure VMware Solution. Secure: Modernize security posture; Prepare for and respond to incidents; Adopt CIA Triad principles (confidentiality, integrity, availability); Sustain security posture.
- definicion: guía para que quienes deciden adopten Azure con menos riesgo y dejen una base (zona de aterrizaje y estándares operativos) para las cargas de trabajo. Secure aplica seguridad en todas las fases, alineada con la adopción de Zero Trust.
- url_oficial: https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/overview ; https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/secure/overview
- novedades_2025_2026: la página general habla de «fases de adopción de Azure» y «escenarios»; la de Secure conserva el término «methodology». AI agents y Sovereignty figuran como escenarios propios.
- verificado: si
- nota: Secure incluye una lista de verificación de seguridad en la nube por fase.

**6b. CAF: adopción de IA (AI CoE, Govern AI, Secure AI)**
- version_o_fecha: AI adoption, 15-oct-2026; Govern AI y AI CoE, 10-abr-2026; Secure AI, 25-jun-2026.
- estado: vigente.
- estructura_cantidad: 6 pasos; Govern AI: 4 pasos; Secure AI: 3 bloques; AI CoE: 3 bloques.
- estructura_nombres: pasos: AI Strategy, AI Plan, AI Ready, Govern AI, Secure AI, Manage AI. Govern AI: Assess AI organizational risks; Document AI governance policies; Enforce AI governance policies; Monitor AI organizational risks. Secure AI: Discover AI security risks; Protect AI resources and data; Detect AI security threats. AI CoE: Build the AI CoE team; Define the responsibilities of the AI CoE; Evolve AI CoE operations.
- definicion: ruta para decidir qué IA adoptar y cómo gobernarla, protegerla y operarla. El AI CoE es un equipo interno de expertos que evita la adopción fragmentada y pasa de un modelo centralizado a uno asesor al madurar.
- url_oficial: https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai/strategy ; https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai/center-of-excellence ; https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai/govern ; https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai/secure
- novedades_2025_2026: rutas nuevas /ai/… (las anteriores /scenarios/ai/… redirigen). El árbol de decisión de IA muestra Agent 365, Defender, Entra y Purview como capa unificada de identidad, seguridad y gobierno. Govern AI sigue el NIST AI RMF; Secure AI remite a STRIDE, MITRE ATLAS y OWASP para IA generativa.
- verificado: si
- nota: Govern, Secure y Manage se describen como procesos continuos.

**6c. CAF: agentes de IA (gobierno y seguridad)**
- version_o_fecha: AI agent adoption, 3-dic-2025; la página de gobierno y seguridad no mostró fecha.
- estado: vigente.
- estructura_cantidad: 4 áreas; gobierno y seguridad: 3 pasos y 4 dominios de política.
- estructura_nombres: áreas: plan for agents; govern and secure agents; build agents; manage agents. Pasos: Responsible AI policies; Agent governance and security; Prepare environment. Dominios: Control plane governance; Data governance and compliance; Security; Development standards.
- definicion: guía para adoptar agentes con una línea base centralizada y exigible: registro de agentes, identidad única por agente, dueño responsable, observabilidad, cumplimiento de datos, pruebas adversarias y estándares de desarrollo (MCP, A2A).
- url_oficial: https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/ ; https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/governance-security-across-organization
- novedades_2025_2026: recomienda Agent 365 como registro y plano de control, y Entra Agent ID como fuente de identidad cuando Agent 365 no está disponible. Clasifica agentes en productivity, action y automation.
- verificado: si
- nota: componentes de un agente según la guía: modelo, instrucciones, recuperación, acciones y memoria.

**7. Secure Future Initiative (SFI)**
- version_o_fecha: informe de progreso de julio de 2026 (cuarto informe); el anterior es de noviembre de 2025.
- estado: vigente; iniciativa lanzada en noviembre de 2023.
- estructura_cantidad: 3 principios; 4 fundamentos; 6 pilares.
- estructura_nombres: principios: Secure by design, Secure by default, Secure operations. Fundamentos: Security-first culture; Security governance; Continuous security improvement; Paved paths and standards. Pilares: Protect identities and secrets; Protect tenants and isolate production systems; Protect networks; Protect engineering systems; Monitor and detect threats; Accelerate response and remediation.
- definicion: programa plurianual con el que Microsoft cambia cómo diseña, construye, prueba y opera su tecnología, con cultura, gobierno e ingeniería medidos por objetivos.
- url_oficial: https://www.microsoft.com/en-us/trust-center/security/secure-future-initiative ; https://www.microsoft.com/en-us/trust-center/security/secure-future-initiative/sfi-progress-report-july-2026
- novedades_2025_2026: el informe de julio de 2026 ordena el progreso en tres temas: Secure foundations, Proactive defense, Future-ready security. Tres objetivos alcanzaron su estado objetivo, tres están cerca y doce avanzaron de forma significativa. MFA resistente a phishing con 99,97 % de cobertura; 1,4 millones de aplicaciones Entra sin uso dadas de baja. La biblioteca de patrones y prácticas incluye guía para sistemas agénticos.
- verificado: si
- nota: la portada nombra dos pilares con variantes («Protect tenants and isolate systems», «Monitor and detect cyberthreats»).

**8. Microsoft Security Development Lifecycle (SDL)**
- version_o_fecha: página de prácticas sin fecha visible; ampliación «SDL for AI» del 3-feb-2026.
- estado: vigente.
- estructura_cantidad: 10 prácticas; SDL for AI: 6 pilares y 6 áreas nuevas.
- estructura_nombres:
  - Prácticas: 1 Establish security standards, metrics, and governance; 2 Require use of proven security features, languages, and frameworks; 3 Perform security design review and threat modeling; 4 Define and use cryptography standards; 5 Secure the software supply chain; 6 Secure the engineering environment; 7 Perform security testing; 8 Ensure operational platform security; 9 Implement security monitoring and response; 10 Provide security training.
  - SDL for AI, pilares: research, policy, standards, enablement, cross-functional collaboration, continuous improvement.
  - SDL for AI, áreas: Threat modeling for AI; AI system observability; AI memory protections; Agent identity and RBAC enforcement; AI model publishing; AI shutdown mechanisms.
- definicion: prácticas para integrar la seguridad en cada etapa del desarrollo (diseño, código, compilación y despliegue, ejecución) bajo principios de Zero Trust.
- url_oficial: https://www.microsoft.com/en-us/securityengineering/sdl/practices ; https://www.microsoft.com/en-us/security/blog/2026/02/03/microsoft-sdl-evolving-security-practices-for-an-ai-powered-world/
- novedades_2025_2026: SDL for AI (feb-2026). En abril de 2026 Microsoft anunció que incorporará modelos avanzados de IA al SDL para descubrir vulnerabilidades: https://www.microsoft.com/en-us/security/blog/2026/04/22/ai-powered-defense-for-an-ai-accelerated-threat-landscape/
- verificado: si
- nota: las seis áreas de IA se anunciaron como temas de guía; la página de prácticas sigue listando diez, sin prácticas numeradas de IA.

**9a. Principios de IA responsable y Responsible AI Standard**
- version_o_fecha: documento público: Responsible AI Standard v2, General Requirements (junio de 2022). Estándar rediseñado en 2026, anunciado el 1-sep-2026 con el Responsible AI Transparency Report 2026.
- estado: principios vigentes; estándar rediseñado en uso interno; texto público del rediseño no verificado.
- estructura_cantidad: 6 principios.
- estructura_nombres: Fairness; Reliability and safety; Privacy and security; Inclusiveness; Transparency; Accountability.
- definicion: principios que guían el desarrollo y uso de IA, y estándar que los convierte en requisitos de producto. El rediseño de 2026 se organiza por capa de la pila (modelos, servicios de plataforma, aplicaciones) y por el rol de Microsoft como desarrollador o desplegador, con requisitos básicos más requisitos por escenario.
- url_oficial: https://www.microsoft.com/en-us/ai/principles-and-approach ; https://blogs.microsoft.com/on-the-issues/2026/09/01/responsible-ai-in-2026-how-we-are-adapting-for-whats-ahead/ ; https://www.microsoft.com/en-us/corporate-responsibility/topics/responsible-ai/reports/transparency-report/
- novedades_2025_2026: tercer informe anual de transparencia (2026). Gestión de riesgos alineada con Govern, Map, Measure y Manage del NIST AI RMF. Nuevas prácticas de modelado de amenazas para IA agéntica y controles centrados en identidades de agentes, permisos de herramientas y monitoreo de acciones.
- verificado: parcial
- nota: no hallé en dominio oficial el texto completo ni el número de versión del estándar rediseñado. El PDF público sigue siendo el v2 de 2022, que agrupa sus objetivos bajo los seis principios: https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/final/en-us/microsoft-brand/documents/Microsoft-Responsible-AI-Standard-v2-General-Requirements-0.pdf?culture=en-us&country=us

**9b. Taxonomy of Failure Modes in Agentic AI Systems (AI Red Team)**
- version_o_fecha: v2.0, abril de 2026 (blog del 4-jun-2026); v1.0 del 24-abr-2025.
- estado: vigente.
- estructura_cantidad: matriz de 2 ejes × 2 pilares; 34 modos de falla en la tabla resumen de la v2.0 (conteo propio); 7 nuevos en v2.0; 5 familias de mitigación.
- estructura_nombres: pilares: Safety, Security. Ejes: Novel, Existing. Nuevos en v2.0: Agentic supply chain compromise; Goal hijacking; Inter-agent trust escalation; Computer Use Agent (CUA) visual attack; Session context contamination; MCP/plugin abuse; Capability/architecture disclosure.
- definicion: vocabulario común de fallas de safety y de security en sistemas agénticos, para modelado de amenazas, pruebas y diseño de mitigaciones.
- url_oficial: https://www.microsoft.com/en-us/security/blog/2026/06/04/updating-taxonomy-failure-modes-agentic-ai-systems-year-red-teaming-taught-us/ ; https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/security/Taxonomy-of-Failure-Modes-in-Agentic-AI-Systems-v2-0.pdf
- novedades_2025_2026: la v2.0 se apoya en doce meses de ejercicios de red team sobre sistemas desplegados y cubre superficies nuevas: MCP y plugins, agentes de uso de computadora y cadena de suministro en lenguaje natural.
- verificado: si
- nota: desglose de la tabla resumen: Novel/Security 13, Novel/Safety 4, Existing/Security 10, Existing/Safety 7. No verifiqué los nombres de las cinco familias de mitigación.

**10a. Microsoft Agent 365**
- version_o_fecha: disponibilidad general desde el 1-may-2026; página de Learn del 12-nov-2026.
- estado: GA para el segmento comercial, licencia por usuario (USD 15); incluido en Microsoft 365 E7. En versión preliminar: agentes con acceso propio que participan en flujos de equipo, descubrimiento de Shadow AI y parte de las señales de riesgo de Defender y Purview.
- estructura_cantidad: 4 pilares.
- estructura_nombres: Management, Governance, Security, Business value.
- definicion: plano de control para observar, gobernar y proteger agentes propios y de terceros, con registro, mapa de agentes, políticas y señales de riesgo de Defender, Entra y Purview. Learn lo llama «the observability platform for AI».
- url_oficial: https://learn.microsoft.com/en-us/microsoft-agent-365/overview ; https://www.microsoft.com/en-us/security/blog/2026/05/01/microsoft-agent-365-now-generally-available-expands-capabilities-and-integrations/ ; https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-agent-365/microsoft-agent-365
- novedades_2025_2026: presentado en Ignite 2025 con cinco capacidades (Registry, Access Control, Visualization, Interoperability, Security). El registro de agentes de Entra converge en Agent 365. Al 1-oct-2026 cumple los controles FedRAMP High, con autorización final pendiente.
- verificado: si
- nota: funciona mejor con Microsoft 365 E5 como requisito previo.

**10b. Microsoft Entra Agent ID**
- version_o_fecha: GA en 2026; página «What is» del 24-jun-2026.
- estado: GA. La cuenta de usuario del agente solo está disponible para tenants del programa Frontier; el Conditional Access ampliado para esas cuentas está en versión preliminar pública (jun-2026).
- estructura_cantidad: 3 construcciones de identidad.
- estructura_nombres: Agent identity blueprint; Agent identity; Agent's user account.
- definicion: plataforma de identidad y autorización específica para agentes de IA (OAuth 2.0, MCP, A2A), con dueño y patrocinador, ciclo de vida, Conditional Access e ID Protection; admite agentes de plataformas ajenas a Microsoft.
- url_oficial: https://learn.microsoft.com/en-us/entra/agent-id/what-is-microsoft-entra-agent-id ; https://learn.microsoft.com/en-us/entra/agent-id/whats-new-agent-id
- novedades_2025_2026: disponible para todos los clientes de Entra; extender las funciones de seguridad de Entra a los agentes requiere Agent 365. Plantillas de Conditional Access para agentes y flujos de ciclo de vida para patrocinadores.
- verificado: si
- nota: la fecha exacta de GA no figura en una página oficial fechada. Réplicas no oficiales de las notas de versión de Entra la sitúan en abril de 2026; el repositorio público de la documentación fecha la página de novedades el 1-may-2026.

**10c. Microsoft 365 E7: The Frontier Suite**
- version_o_fecha: anunciado el 9-mar-2026; GA el 1-may-2026.
- estado: GA; USD 99 por usuario al mes; con y sin Teams.
- estructura_cantidad: 4 componentes.
- estructura_nombres: Microsoft 365 E5; Microsoft 365 Copilot; Microsoft Agent 365; Microsoft Entra Suite.
- definicion: suite que une productividad, IA, identidad y seguridad para personas y agentes, con Work IQ como capa de inteligencia y capacidades avanzadas de Defender, Intune y Purview.
- url_oficial: https://blogs.microsoft.com/blog/2026/03/09/introducing-the-first-frontier-suite-built-on-intelligence-trust/ ; https://www.microsoft.com/en-za/microsoft-365/enterprise/e7
- novedades_2025_2026: Security Copilot incluido para clientes E5 y E7 (400 SCU al mes por cada 1.000 licencias, hasta 10.000).
- verificado: si
- nota: la página de producto que abrí es una variante regional con precio en USD.

**10d. Agentes de Security Copilot**
- version_o_fecha: páginas de Learn del 18-mar-2026 (general) y del 1-abr-2026 (Entra e Intune).
- estado: mixto por agente; la página general advierte que parte de la información corresponde a producto en versión preliminar.
- estructura_cantidad: 15 agentes de Microsoft identificados en Learn (conteo propio).
- estructura_nombres:
  - Standalone y Defender: Threat Intelligence Briefing Agent; Security Alert Triage Agent (Preview; es el Phishing Triage Agent ampliado, con alertas de correo en GA y de nube e identidad en preview); Threat Hunting Agent; Security Analyst Agent; Dynamic Threat Detection Agent.
  - Entra: Conditional Access Optimization Agent; Identity Risk Management Agent (Preview).
  - Intune: Change Review Agent; Device Offboarding Agent; Policy Configuration Agent; Vulnerability Remediation Agent.
  - Purview: triage agent de DLP; triage agent de Insider Risk Management; posture agent de DSPM (preview según Learn); posture agent de Data Security Investigations (preview).
- definicion: agentes que automatizan tareas repetitivas de seguridad y TI dentro de Defender, Entra, Intune y Purview; consumen SCU y pueden usar una identidad de agente de Entra.
- url_oficial: https://learn.microsoft.com/en-us/copilot/security/agents-overview ; https://learn.microsoft.com/en-us/defender-xdr/security-copilot-agents-defender ; https://learn.microsoft.com/en-us/entra/security-copilot/entra-agents ; https://learn.microsoft.com/en-us/intune/copilot/agents/ ; https://learn.microsoft.com/en-us/purview/copilot-in-purview-agents-overview ; https://learn.microsoft.com/en-us/copilot/security/security-copilot-inclusion
- novedades_2025_2026: inclusión en Microsoft 365 E5 y E7 con despliegue por fases desde el 18-nov-2025. Agentes de socios en Security Store. «Project Perception» (sistema multiagente) anunciado en julio de 2026, con disponibilidad no verificada: https://www.microsoft.com/en-us/security/blog/2026/07/30/whats-new-in-microsoft-security-july-2026/
- verificado: parcial
- nota: Learn no etiqueta GA o preview de forma uniforme por agente. El posture agent de DSPM figura como preview en Learn, mientras que una réplica no oficial del Message Center indica GA entre junio y julio de 2026.

**10e. Microsoft Purview DSPM (antes «DSPM for AI»)**
- version_o_fecha: DSPM for AI (classic), página del 15-dic-2025; reemplazado por la versión actual unificada de Data Security Posture Management, anunciada el 18-nov-2025.
- estado: versión actual sin etiqueta de versión preliminar en Learn. La GA de mayo de 2026 consta solo en réplicas no oficiales del Message Center (MC1191257). La versión clásica sigue accesible.
- estructura_cantidad: clásica: 4 capacidades; actual: 6 páginas principales.
- estructura_nombres: clásica: insights and analytics; ready-to-use policies; data risk assessments; compliance controls. Actual: Posture; Objectives; AI observability; Asset explorer; Reports; Setup tasks.
- definicion: punto central de Purview para descubrir, proteger e investigar riesgos de datos sensibles en aplicaciones tradicionales y en aplicaciones y agentes de IA, con inventario de agentes con actividad reciente.
- url_oficial: https://learn.microsoft.com/en-us/purview/data-security-posture-management-learn-about ; https://learn.microsoft.com/en-us/purview/dspm-for-ai ; https://techcommunity.microsoft.com/blog/microsoft-security-blog/beyond-visibility-the-new-microsoft-purview-data-security-posture-management-dsp/4470984
- novedades_2025_2026: objetivos de seguridad de datos guiados; AI observability con inventario de agentes, incluido Agent 365; señales de terceros (Varonis, Cyera, BigID, OneTrust); agentes de Security Copilot para triage y postura.
- verificado: parcial
- nota: «DSPM for AI» ya no es el nombre vigente. La integración de fuentes externas vía Sentinel data lake figura en preview.

**10f. Defender for AI Services (Defender for Cloud)**
- version_o_fecha: página del 17-jun-2026.
- estado: GA para la protección contra amenazas de servicios de IA. En preview: protección de agentes creados con Foundry (desde el 2-feb-2026) y de agentes de Copilot Studio.
- estructura_cantidad: 2 funciones en GA.
- estructura_nombres: Activity monitoring (security alerts); Prompt evidence (security alerts).
- definicion: plan de Defender for Cloud que detecta en tiempo real amenazas contra aplicaciones de IA generativa (fuga de datos, envenenamiento, jailbreak, robo de credenciales), integrado con Prompt Shields y Defender XDR.
- url_oficial: https://learn.microsoft.com/en-us/azure/defender-for-cloud/ai-threat-protection ; https://learn.microsoft.com/en-us/security/security-for-ai/whats-new ; https://learn.microsoft.com/en-nz/azure/defender-for-cloud/release-notes
- novedades_2025_2026: Security Dashboard for AI en GA (abril de 2026 según Learn). Postura y protección en tiempo de ejecución unificadas para agentes en la nube dentro de Agent 365 (julio de 2026, estado no indicado).
- verificado: si
- nota: cubre modelos de Azure OpenAI y Azure AI Model Inference, solo tokens de texto y solo nubes comerciales.

**10g. Microsoft Sentinel (data lake, graph, MCP server)**
- version_o_fecha: data lake GA el 30-sep-2025; graph GA desde el 1-dic-2025; MCP server GA el 18-nov-2025.
- estado: data lake GA. Graph GA en las experiencias integradas de Defender y Purview, con custom graphs en preview. MCP server GA, con herramientas MCP de grafo en preview (dato de nov-2025).
- estructura_cantidad: 3 componentes de plataforma; 3 colecciones de herramientas MCP; 2 niveles de almacenamiento.
- estructura_nombres: Microsoft Sentinel data lake; Microsoft Sentinel graph; Microsoft Sentinel MCP server. Colecciones MCP: Data exploration; Security Copilot agent creation; Triage. Niveles: Analytics tier; Data lake tier.
- definicion: Sentinel como SIEM y plataforma para defensa con agentes: lago de datos de seguridad administrado (hasta 12 años de retención), análisis de grafos de relaciones y acceso de agentes a los datos por MCP.
- url_oficial: https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-lake-overview ; https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-graph-overview ; https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-mcp-overview
- novedades_2025_2026: herramientas MCP personalizadas a partir de consultas KQL guardadas; conexión desde Security Copilot, VS Code, Copilot Studio, Foundry y clientes de terceros compatibles; retiro de Sentinel en el portal de Azure previsto para el 31-mar-2027.
- verificado: si
- nota: fechas de GA tomadas de techcommunity.microsoft.com: https://techcommunity.microsoft.com/blog/microsoft-security-blog/microsoft-sentinel-data-lake-is-now-generally-available/4456342 ; https://techcommunity.microsoft.com/blog/microsoft-security-blog/uncover-hidden-security-risks-with-microsoft-sentinel-graph/4469437 ; https://techcommunity.microsoft.com/blog/microsoft-security-blog/microsoft-sentinel-mcp-server---generally-available-with-exciting-new-capabiliti/4470125

**11. Microsoft Digital Defense Report (MDDR)**
- version_o_fecha: edición 2026, publicada el 1-oct-2026; cubre de julio de 2025 a junio de 2026.
- estado: edición vigente.
- estructura_cantidad: 4 secciones temáticas; 10 conclusiones principales; 10 prioridades de seguridad.
- estructura_nombres: AI; The threat landscape; Cybercrime; Resilience.
- definicion: informe anual de inteligencia de amenazas de Microsoft. La edición 2026 sostiene que la IA cambia la velocidad, la escala y la economía del ataque y de la defensa, en un ecosistema de riesgos interconectados.
- url_oficial: https://www.microsoft.com/en-us/corporate-responsibility/topics/cybersecurity/reports/microsoft-digital-defense-report/ ; https://www.microsoft.com/en-us/security/security-insider/threat-landscape/2026-digital-defense-report
- novedades_2025_2026: las diez conclusiones, en mis palabras:
  1. La IA comprime los tiempos de ataque y de defensa.
  2. La IA ya es superficie de ataque.
  3. Las personas siguen siendo vía de acceso inicial.
  4. La identidad, humana y no humana (agentes incluidos), es el plano de control primario.
  5. La correlación de señales es la variable estratégica.
  6. Amenazas emergentes: cadena de suministro de código abierto, dispositivos de borde e IA como multiplicador.
  7. Proteger los datos pesa más con IA.
  8. Hay que pasar de la respuesta reactiva a la gestión continua de exposición.
  9. La política pública define el terreno.
  10. La resiliencia es un resultado central.
- verificado: si
- nota: cifras: más de 165 billones (165 trillion) de señales diarias; 63 % de las intrusiones con robo de datos; 5,3 horas en promedio hasta el ataque a cargas en la nube expuestas; casi 40.000 CVE en el primer semestre de 2026. Define cinco clases de riesgo de la superficie agéntica: Prompt and intent manipulation; Sensitive data exposure; Identity and privilege compromise; Excessive agency; Operational integrity. La edición 2025 se tituló «Lighting the path to a secure future».

**12. Catálogo de capacidades de defensa de IA**
- version_o_fecha: páginas con fecha 1-ago-2026.
- estado: publicado en Learn; es guía, no un producto.
- estructura_cantidad: 9 familias de capacidades; 3 objetivos de control. El catálogo compañero de ataques tiene 14 técnicas en 5 macrofamilias.
- estructura_nombres:
  - Familias: 1 Govern, Assure, and Respond; 2 Supply-chain and Provenance; 3 Identity, Access, and Least Privilege; 4 Input, Context, and Retrieval Hygiene; 5 Model Hardening and Alignment; 6 Runtime Isolation and Sandboxing; 7 Output Safety and Downstream Handling; 8 Monitoring, Detection, and Forensics; 9 Resource Governance and Abuse Prevention.
  - Objetivos: trust boundary on input; integrity on data and models; containment on execution.
  - Macrofamilias de ataque (CAAT): Instruction Manipulation; State and Memory Manipulation; Trust and Supply Chain Abuse; Execution and Autonomy Abuse; Resource and Extraction Abuse.
- definicion: vista única de las capacidades defensivas que una empresa necesita para adoptar IA con seguridad, derivada del catálogo de técnicas de ataque y normalizada con MITRE ATLAS, OWASP Top 10 para aplicaciones LLM (2025) y NIST AI RMF con su perfil de IA generativa.
- url_oficial: https://learn.microsoft.com/en-us/security/zero-trust/catalog-ai-defense-capabilities/catalog-ai-defense-capabilities ; https://learn.microsoft.com/en-us/security/zero-trust/catalog-ai-attack-techniques/catalog-ai-attack-techniques
- novedades_2025_2026: publicado en 2026 dentro de la documentación de Zero Trust. Está dirigido a CISOs, arquitectos y responsables de riesgo, y reparte responsabilidades entre arquitectura, ingeniería de producto, operaciones de seguridad y gobierno.
- verificado: si
- nota: el título oficial es «AI Defense Capabilities for Enterprise AI Security»; «catalog» aparece en la ruta de la URL y en el nombre del compañero, «Catalog of AI Attack Techniques (CAAT)».

## Ocho hallazgos para caracterizar a la empresa y al CISO de frontera

1. **La empresa de frontera se define por cómo reparte el trabajo entre personas y agentes.** Combina inteligencia a demanda, equipos de personas y agentes, y el rol de agent boss para todos; desde Ignite 2025 Microsoft la resume como dirigida por personas y operada por agentes. Su métrica propia es la proporción humanos–agentes, sin valor fijo. Fuente: https://www.microsoft.com/en-us/worklab/work-trend-index/2025-the-year-the-frontier-firm-is-born

2. **En 2026 la confianza queda al mismo nivel que la inteligencia.** Los tres rasgos duraderos son ambición humana, inteligencia y confianza; la confianza se concreta como observabilidad, gobierno y seguridad en cada capa, con Agent 365 como plataforma. Fuente: https://blogs.microsoft.com/blog/2026/10/27/the-platform-approach-to-becoming-frontier/

3. **El cuello de botella es organizacional, no individual.** En el Work Trend Index 2026 los factores organizacionales pesan más del doble que los individuales en el impacto de la IA (67 % frente a 32 %), y solo 19 % de los usuarios de IA está en la zona Frontier. Fuente: https://www.microsoft.com/en-us/worklab/work-trend-index/agents-human-agency-and-the-opportunity-for-every-organization

4. **Seguridad es uno de los cuatro roles que se reinventan a la vez** (empleados, líderes, TI, seguridad). Según el mismo informe, los agentes traen riesgos de exfiltración de datos, acciones no previstas y acceso no autorizado; la respuesta es integrar monitoreo, aplicación de políticas y auditabilidad en la plataforma, para que la confianza sea una propiedad estructural. Fuente: la misma URL del hallazgo 3.

5. **Gobernar agentes es lo que permite escalar.** En el estudio de IDC de 2026, 87 % de las Frontier Firms tiene un proceso para gobernar agentes, frente a 51 % de los rezagados, y declara retornos de 4x frente a 2,7x. Solo 60 % de las organizaciones confía en manejar los riesgos de seguridad y gobierno de IA. Fuente: https://blogs.microsoft.com/blog/2026/11/12/scaling-ai-value-without-losing-control-lessons-from-frontier-firms/

6. **El agente pasa a ser una identidad gestionada, con dueño.** Registro, identidad única, patrocinador, mínimo privilegio y ciclo de vida aparecen en Agent 365, Entra Agent ID y la guía de agentes del CAF. El MDDR 2026 coloca la identidad, incluida la no humana, como plano de control primario. Fuentes: https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/governance-security-across-organization ; https://www.microsoft.com/en-us/corporate-responsibility/topics/cybersecurity/reports/microsoft-digital-defense-report/

7. **Los marcos tratan la IA como parte del programa de seguridad, no como programa aparte.**
   - El SAF pide abordar los cambios de la IA dentro del programa existente y la suma como tecnología a proteger.
   - Zero Trust parte de «assume compromise».
   - El MCSB v2 trae un dominio de IA con siete recomendaciones.
   - Se agregan el catálogo de nueve familias de defensa y la taxonomía v2.0 del AI Red Team.

   Fuentes: https://learn.microsoft.com/en-us/security/zero-trust/security-adoption-model ; https://learn.microsoft.com/en-us/security/zero-trust/catalog-ai-defense-capabilities/catalog-ai-defense-capabilities

8. **El CISO de frontera equilibra tres frentes y gestiona ecosistemas.**
   - Los frentes son: asegurar los cimientos, defender con agentes y controlar al «agentic insider», equilibrando automatización a velocidad de máquina con juicio humano, e innovación con control.
   - El MDDR 2026 afirma que «CISOs today are managing ecosystems, not just environments» y pide medir exposición reducida y tiempo de mitigación en lugar de parches desplegados.
   - El CISO Workshop plantea la seguridad como habilitador del negocio, no solo como función técnica.

   Fuentes: https://learn.microsoft.com/en-us/security/saf/scenarios/ai-security/overview ; https://www.microsoft.com/en-us/security/security-insider/threat-landscape/2026-digital-defense-report

## Vacíos e incertidumbres

- **Ignite 2026 (17 al 20-nov-2026):** aún no ocurrió. Conviene revisar después el estado del MCSB v2, Agent 365, el SAF y el pilar de IA del Workshop.
- **Fechas iguales al día de consulta:** varias páginas de Learn muestran 15-nov-2026 (principios de Zero Trust, Assessment, Workshop, CISO Workshop y las páginas /security/saf/). Puede ser una actualización del mismo día o un artefacto de publicación.
- **MCSB v2:** busqué un anuncio de disponibilidad general y revisé las notas de versión de Defender for Cloud; no apareció. La página oficial sigue diciendo preview.
- **Responsible AI Standard rediseñado:** el blog oficial describe su estructura, pero no hallé el texto ni su número de versión.
- **Solo en fuentes no oficiales:** la GA del nuevo Purview DSPM (mayo de 2026) y el mes exacto de GA de Entra Agent ID (abril de 2026) constan en réplicas del Message Center y de las notas de versión.
- **Conteos propios:** los 34 modos de falla de la taxonomía v2.0 y los 15 agentes de Security Copilot salen de las tablas y páginas abiertas, no de una cifra declarada por Microsoft.
- **No abierto en detalle:** las soluciones técnicas del SAF, las diez prioridades de seguridad del MDDR 2026, las cinco familias de mitigación de la taxonomía y los criterios con que el Work Trend Index 2025 clasificó a las Frontier Firms.
- **Vistas previas privadas:** excluidas. Las funciones del programa Frontier se citan solo como contexto de estado.

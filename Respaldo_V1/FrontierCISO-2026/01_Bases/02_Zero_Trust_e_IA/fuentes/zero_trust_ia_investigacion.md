# Zero Trust y su aplicación a la IA según NIST, The Open Group y Microsoft

Fecha de corte y de consulta: 15 de noviembre de 2026. Ámbito: fuentes oficiales de NIST (incluidos NCCoE y CAISI), The Open Group y Microsoft. CISA y DoD aparecen solo como derivados. Las cifras entre corchetes remiten a la sección 7. «Abierta» significa que la página se cargó completa; «extracto» significa que solo se leyó el extracto del buscador sobre el dominio oficial.

## 1. Resumen

1. Ninguna de las tres organizaciones ha publicado una norma formal dedicada a «Zero Trust para IA». Solo Microsoft usa esa etiqueta («Zero Trust for AI», ZT4AI, marzo de 2026) [20], y la aplica a guías, a un pilar de IA del Workshop y a comprobaciones del Assessment ligadas a sus productos [21][22][23].
2. NIST mantiene SP 800-207 (2020) como base, sin revisión que incorpore IA [1]. Su aporte sobre agentes es reciente y no definitivo: documento conceptual del NCCoE (febrero de 2026) [5], un centro de recursos del proyecto [6] y diez «design tenets» propuestos en un blog del 27-10-2026 [7].
3. Las superposiciones de control para IA (antes COSAiS, ahora COSIS) siguen sin borrador público inicial. El Cyber AI Profile (IR 8596) sigue como borrador preliminar [9][10].
4. En la terminología federal, un decreto del 29-09-2026 cambió «AI» por «Super Intelligence (SI)». NIST renombró proyectos, pero no modificó documentos ya publicados [9].
5. The Open Group tiene un estándar vigente, Zero Trust Commandments, y un Zero Trust Reference Model que sigue como Snapshot 1.0, con la versión 2.0 en desarrollo. No publicó nada sobre IA; el tema solo aparece en actas como posible colaboración [12][13][14].
6. Las tres fuentes coinciden en identidad propia para cada agente, mínimo privilegio por tarea, política aplicada fuera del modelo, telemetría independiente y aprobación humana para acciones de alto impacto.
7. Para medir hay modelos de madurez en los derivados (CISA, DoD) y criterios comprobables en NIST (tenets) y Microsoft (Assessment). Ninguna de las tres organizaciones propone un modelo de madurez de Zero Trust específico para IA.

## 2. Inventario por organización

### 2.1 NIST, NCCoE y CAISI

| Identificador | Título exacto | Estado | Fecha | URL | Síntesis |
|---|---|---|---|---|---|
| SP 800-207 | Zero Trust Architecture | Final | 11-08-2020 | https://csrc.nist.gov/pubs/sp/800/207/final | Define ZT/ZTA, siete principios (tenets), componentes lógicos PE/PA/PEP y fuentes de datos, modelos de despliegue y una ruta de migración. Su objeto son los recursos, no los segmentos de red [1][2]. |
| SP 800-207A | A Zero Trust Architecture Model for Access Control in Cloud-Native Applications in Multi-Cloud Environments | Final | 13-09-2023 | https://csrc.nist.gov/pubs/sp/800/207/a/final | Lleva las políticas de acceso a identidades de aplicación y servicio (gateways, sidecars, SPIFFE) en entornos multinube e híbridos [3]. |
| SP 1800-35 | Implementing a Zero Trust Architecture: High-Level Document | Final | 10-06-2025 | https://csrc.nist.gov/pubs/sp/1800/35/final | Guía práctica del NCCoE: 24 colaboradores, 19 implementaciones de ejemplo y correspondencias con otros marcos [4]. |
| CSWP 20 | Planning for a Zero Trust Architecture: A Planning Guide for Federal Administrators | Final | 06-05-2022 | https://csrc.nist.gov/pubs/cswp/20/planning-for-a-zero-trust-architecture/final | Explica cómo aplicar el NIST RMF a la planificación y migración a ZTA (extracto; la ficha no cargó) [11]. |
| Concept paper NCCoE | Accelerating the Adoption of Software and Artificial Intelligence Agent Identity and Authorization | Borrador (comentarios cerrados el 02-04-2026) | 05-02-2026 | https://csrc.nist.gov/pubs/other/2026/02/05/accelerating-the-adoption-of-software-and-ai-agent/ipd | Propone un proyecto para aplicar normas de identidad y autorización a agentes. Pide opinión sobre identificación, autorización, auditoría, no repudio e inyección de instrucciones [5]. |
| Proyecto NCCoE (hub) | NCCoE Agentic AI (SI) Identity and Authorization Project Resource Hub | En curso | Consulta 15-11-2026 | https://pages.nist.gov/nccoe-ai-identity/index.html | Anuncia como entregable final una guía de la serie SP 1800 e indica que se recibieron más de 600 respuestas [6]. |
| Blog NIST n.º 2 | Design Tenets for Agent Identity Management Systems | Propuesta (no normativa) | 27-10-2026 | https://www.nist.gov/blogs/cybersecurity-insights/design-tenets-agent-identity-management-systems | Diez principios de diseño para identificar, autenticar y autorizar agentes. Guiarán las demostraciones del NCCoE [7]. |
| Blog NIST n.º 1 | Back to the Future: Why Agentic AI Needs a Strong Identity Foundation | Publicado | 27-08-2026 | https://www.nist.gov/blogs/cybersecurity-insights/back-future-why-agentic-ai-needs-strong-identity-foundation | Desaconseja compartir credenciales y usar secretos estáticos. Propone tratar a los agentes como entidades propias (extracto) [8]. |
| COSIS (antes COSAiS) | SP 800-53 Control Overlays for Super Intelligence Systems | En desarrollo; concept paper (14-08-2025) y esquema anotado (08-01-2026) | Página actualizada el 20-10-2026 | https://csrc.nist.gov/projects/cosis | Serie de superposiciones SP 800-53 para cinco casos de uso, entre ellos agente único y multiagente. No hay borrador público inicial visible [9]. |
| IR 8596 iprd | Cybersecurity Framework Profile for Artificial Intelligence (Cyber AI Profile): NIST Community Profile | Borrador preliminar | 16-12-2025 | https://csrc.nist.gov/pubs/ir/8596/iprd | Perfil CSF 2.0 con tres áreas de foco: Secure, Defend y Thwart (extracto) [10]. |
| AI 100-1 | AI Risk Management Framework (AI RMF 1.0) | Final, en revisión | 26-01-2023 | https://www.nist.gov/itl/ai-risk-management-framework | Marco voluntario de riesgo de IA. NIST informa que se está revisando (extracto) [15]. |
| AI 600-1 | Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile | Final | 26-07-2024 | https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence | Perfil del AI RMF para IA generativa (extracto) [16]. |
| AI 800-5 (según la ficha) | Summary Analysis of Responses to the Request for Information Regarding Security Considerations for AI Agents | Publicado | 18-05-2026 | https://www.nist.gov/publications/summary-analysis-responses-request-information-regarding-security-considerations-ai | Resume la consulta de CAISI: los principios clásicos siguen siendo válidos, pero deben adaptarse a los agentes (extracto) [17]. |
| Iniciativa CAISI | AI Agent Standards Initiative | En curso | Creada el 17-02-2026; actualizada el 14-08-2026 | https://www.nist.gov/artificial-intelligence/ai-agent-standards-initiative | Programa de normas, protocolos e investigación sobre identidad y seguridad de agentes (extracto) [18]. |

**¿Tiene NIST una publicación titulada o dedicada a «Zero Trust para IA»?** No. Encontré documentos que aplican principios de Zero Trust a la identidad y la autorización de agentes, pero ninguno con ese título ni con ese alcance declarado. Los tenets de octubre de 2026 están en un blog y se presentan como propuesta [7].

**Principios (tenets) de SP 800-207, en síntesis propia** [2]:
1. Todo dato y todo servicio de cómputo es un recurso.
2. Toda comunicación se protege, con independencia de la red.
3. El acceso se concede sesión por sesión y con el mínimo privilegio.
4. El acceso lo decide una política dinámica que considera identidad, estado del activo y atributos de comportamiento y entorno.
5. La organización vigila la integridad y la postura de todos sus activos.
6. Autenticación y autorización son dinámicas y se aplican antes de dar acceso.
7. Se recoge información del estado del entorno para mejorar la postura.

**Componentes lógicos** [2]: Policy Engine (decide), Policy Administrator (abre o cierra la ruta) y Policy Enforcement Point (hace cumplir). Las fuentes que alimentan la decisión son CDM, cumplimiento sectorial, inteligencia de amenazas, registros de actividad, políticas de acceso a datos, PKI, gestión de identidades y SIEM.

### 2.2 The Open Group

| Identificador | Título | Estado | Fecha | URL | Síntesis |
|---|---|---|---|---|---|
| No verificado | Zero Trust Commandments (Standard) | Estándar vigente | No verificada | https://www.opengroup.org/forum/security/Zerotrust | Reglas prescriptivas de Zero Trust. Reemplaza al Snapshot y a la Guide previos y al white paper de Core Principles [12]. El texto no se pudo abrir: pubs.opengroup.org bloqueó la carga. |
| No verificado | Zero Trust Core Principles (White Paper) | Reemplazado por el estándar Commandments | No verificada | https://www.opengroup.org/forum/security/Zerotrust | Primer conjunto de principios orientado a ejecutivos [12][19]. |
| No verificado | Zero Trust Reference Model, Snapshot Version 1.0 | Snapshot (borrador público, no estándar); v2.0 en desarrollo | No verificada | https://www.opengroup.org/forum/security-forum-0/zerotrustsecurityarchitecture | Define capacidades y bloques de arquitectura (ABB). Es el primer paso hacia una arquitectura de referencia [13][14]. |
| Proyectos | Zero Trust Implementation Guide; Reference Architecture; Glossary & Roles (S222) | En desarrollo | — | https://www.opengroup.org/forum/security-forum-0/zerotrustsecurityarchitecture | La guía de implementación remite al «3-Pillar Model» del Reference Model y declara neutralidad de herramientas [13]. |

**¿Tiene The Open Group una publicación sobre Zero Trust aplicado a IA o agentes?** No. Las actas oficiales solo registran que la IA se discutió como posible proyecto (octubre de 2024), como área de colaboración con el Architecture Forum (noviembre de 2025) y como tema de un posible grupo de trabajo (abril de 2026) [14][24][25].

### 2.3 Microsoft

| Identificador | Título | Estado | Fecha | URL | Síntesis |
|---|---|---|---|---|---|
| Learn | Zero Trust as a security foundation | Publicado | Actualizado el 15-11-2026 | https://learn.microsoft.com/en-us/security/zero-trust/zero-trust-overview | Tres principios: verificar explícitamente, mínimo privilegio y asumir compromiso. Los aplica a varias áreas técnicas, IA incluida, y los integra en el Security Adoption Framework (SAF) [26]. |
| Learn | Zero Trust adoption framework overview | Publicado | Actualizado el 05-05-2025 | https://learn.microsoft.com/en-us/security/zero-trust/adopt/zero-trust-adoption-overview | Cinco escenarios de negocio, fases de ciclo de vida, cuatro etapas de implementación y herramientas de seguimiento [27]. |
| Learn (SAF) | Secure AI with Zero Trust | Publicado | No visible | https://learn.microsoft.com/en-us/security/saf/technologies/ai/overview | Pilar de IA del SAF con siete áreas de control, del inventario a la detección y respuesta (extracto) [22]. |
| Learn | Microsoft Zero Trust Workshop - AI security | Publicado | No visible | https://learn.microsoft.com/en-us/security/zero-trust/workshop-zero-trust-ai-security | Áreas de implementación de seguridad de IA y una cartera priorizada en «First, Then, Next» (extracto) [21]. |
| Learn | Zero Trust Assessment (pilar de IA) | Publicado; algunas capacidades enlazadas están en vista previa | No visible | https://learn.microsoft.com/en-us/security/zero-trust/assessment/ai-pillar | Comprobaciones automáticas sobre identidades de agentes, Conditional Access y gobierno del ciclo de vida. El Assessment cubre siete pilares (extracto) [23][28]. |
| Learn | AI Defense Capabilities for Enterprise AI Security | Publicado | Actualizado el 01-08-2026 | https://learn.microsoft.com/en-us/security/zero-trust/catalog-ai-defense-capabilities/catalog-ai-defense-capabilities | Nueve familias de capacidades defensivas alineadas con MITRE ATLAS, OWASP LLM 2025 y NIST AI RMF/600-1 (extracto) [29][30]. |
| Learn (SFI) | Secure autonomous agentic AI systems; Reduce autonomous agentic AI risk; Least privilege for AI agents | Publicados | No visibles | https://learn.microsoft.com/en-us/security/zero-trust/sfi/secure-agentic-systems | Patrones SFI con controles por capa (modelo, sistema de seguridad, aplicación y posicionamiento) y diseño de mínimo privilegio para agentes (extracto) [31][32][33]. |
| Learn (SFI) | Microsoft Secure Future Initiative (SFI) overview | Publicado | Cita el informe de julio de 2026 | https://learn.microsoft.com/en-us/security/zero-trust/sfi/secure-future-initiative-overview | Seis pilares de ingeniería alineados con los principios de Zero Trust y las funciones del CSF (extracto) [34]. |
| Blog | New tools and guidance: Announcing Zero Trust for AI | Publicado | 19-03-2026 | https://www.microsoft.com/en-us/security/blog/2026/03/19/new-tools-and-guidance-announcing-zero-trust-for-ai/ | Presenta ZT4AI, el pilar de IA del Workshop y una arquitectura de referencia para IA (extracto) [20]. |
| Blog | Advance Zero Trust for AI: New tools and guidance to secure AI agents and DevSecOps | Publicado | 04-08-2026 | https://www.microsoft.com/en-us/security/blog/2026/08/04/advance-zero-trust-for-ai-new-tools-and-guidance-to-secure-ai-agents-and-devsecops/ | Añade pilares de IA, SecOps e Infraestructura al Assessment, un pilar DevSecOps al Workshop y un libro electrónico (extracto) [35]. |
| Learn (SAF) | Map The Open Group Zero Trust model to SAF | Publicado | Actualizado el 15-11-2026 | https://learn.microsoft.com/en-us/security/saf/framework-mappings/open-group-zero-trust | Correspondencia escrita por Microsoft. Aclara que The Open Group es la fuente autorizada y que el Reference Model sigue siendo Snapshot [36]. |

### 2.4 Derivados (no son de las tres organizaciones)

| Organización | Publicación | Estado y fecha | URL | Relación |
|---|---|---|---|---|
| CISA (derivado) | Zero Trust Maturity Model, Version 2.0 | Final; 11-04-2023 | https://www.cisa.gov/resources-tools/resources/zero-trust-maturity-model | Cinco pilares, tres capacidades transversales y cuatro etapas: tradicional, inicial, avanzada y óptima. Se apoya en la definición de NIST (extracto) [37]. |
| DoD (derivado) | DoD Zero Trust Reference Architecture, Version 2.0 | Final; julio de 2022 | https://dodcio.defense.gov/Portals/0/Documents/Library/(U)ZT_RA_v2.0(U)_Sep22.pdf | Pilares, principios, taxonomía de capacidades y un caso de uso de analítica e IA (extracto) [38]. |
| DoD (derivado) | DoD Zero Trust Strategy (placemats) | Fecha no verificada | https://dodcio.defense.gov/Portals/0/Documents/Library/ZT-StrategyPlacemats.pdf | Siete pilares con niveles Target y Advanced (extracto) [39]. |

## 3. Correspondencia de principios y pilares

### 3.1 Principios por tema (síntesis propia)

| Tema | NIST SP 800-207 | The Open Group | Microsoft |
|---|---|---|---|
| Verificación explícita y continua | Tenets 3 y 6: acceso por sesión y autenticación/autorización dinámicas antes de cada acceso [2] | Mandamiento de validar la confianza de forma explícita (*nombre no verificado en fuente oficial*) | Verify explicitly, con señales de identidad, dispositivo, recurso, entorno y comportamiento [26] |
| Mínimo privilegio | Tenet 3: privilegio mínimo para cada tarea [2] | Mandamiento de mínimo privilegio (*no verificado*); capacidad de acceso privilegiado y activos de alto valor [36] | Least privilege con JIT/JEA y políticas adaptativas [26][27] |
| Asumir brecha | Red considerada comprometida; atacante presente [2] | Supuesto de fallo o compromiso (*no verificado*) | Assume compromise; antes se llamaba «assume breach» [26] |
| Centrado en datos y activos | Tenet 1: todo dato o servicio es un recurso [2] | Seguridad centrada en activos y gestión segura de activos [36] | La protección sigue al activo y a sus relaciones [26] |
| Política dinámica | Tenet 4 y algoritmo de confianza [2] | Gestión de identidad y acceso adaptativo (PDP, PEP y PIP como ABB) [36] | Los privilegios cambian cuando cambia el riesgo [26] |
| Telemetría y automatización | Tenets 5 y 7; CDM y SIEM como fuentes [2] | Operaciones de seguridad centradas en activos; gestión de postura [36] | Detección, respuesta y recuperación incluidas en el diseño [26] |
| Gobierno y negocio | Migración por procesos de negocio; RMF (CSWP 20) [2][11] | Gobierno Zero Trust y estrategia, integración y gobierno de seguridad [36] | Implicación de la alta dirección; escenarios de negocio del SAF [27][26] |

### 3.2 Pilares o dominios

| Dominio | NIST | The Open Group | Microsoft | CISA (derivado) | DoD (derivado) |
|---|---|---|---|---|---|
| Identidades | Sujetos y gestión de identidades [2] | IAAMP [36] | Sí [26][28] | Sí | Sí |
| Dispositivos | Activos y postura [2] | Dentro de capacidades | Endpoints / dispositivos | Sí | Sí |
| Aplicaciones y cargas | Recursos; 800-207A [3] | Software y DevSecOps [36] | Sí; DevSecOps en el Workshop [35] | Sí | Sí |
| Datos | Recursos y políticas de datos [2] | Seguridad de datos [36] | Sí | Sí | Sí |
| Infraestructura | Entorno y red [2] | Zonas de seguridad [36] | Sí | No como pilar | No verificado |
| Red | Red y entorno [2] | Zonas de seguridad | Sí | Sí | Sí |
| Visibilidad, automatización y gobierno | Fuentes de datos del PE [2] | Postura, SecOps y gobierno [36] | SecOps (Assessment) [28] | Tres capacidades transversales [37] | Sí |
| **IA** | No como pilar; proyecto aparte [6][7] | **No** | **Sí**: pilar de SAF, Workshop y Assessment [21][22][28] | No | No; solo un caso de uso de IA [38] |

## 4. Zero Trust aplicado a IA y agentes, por organización

### 4.1 NIST

**Lo que afirma la fuente.**
- *Identidad propia del agente.* Cada agente necesita una identificación criptográficamente verificable, distinta de la de personas y cuentas de servicio, ligada a su carga y su configuración y con un ciclo de vida separado (tenet 01). El agente queda vinculado a quien le encarga la tarea, y la autoridad se reduce en cada delegación (tenet 02) [7].
- *Autorización por tarea.* Sin privilegio permanente y con el mínimo alcance por tarea (tenet 03). Los permisos son JIT, de corta duración, con destinatario específico y revocables, y cada llamada a herramienta se verifica en tiempo de ejecución (tenet 04) [7]. El blog n.º 1 desaconseja compartir credenciales y usar claves estáticas [8].
- *Contenido no confiable.* La lógica que decide qué intenta hacer el agente se separa de la que decide qué se le permite (tenet 07). Las decisiones de acceso son deterministas (tenet 08). Sobre los guardarraíles, el blog dice: «Guardrails alone are insufficient» [7].
- *Supervisión.* Monitoreo continuo con métricas específicas de agentes (tenet 09) y evidencia inmutable, de solo anexado, guardada fuera del alcance del agente (tenet 10) [7].
- *Control humano.* Umbrales de riesgo que llevan a revisión humana, con atención a la fatiga de aprobación (tenet 05). Mandatos firmados que fijan el resultado esperado y sus límites (tenet 06) [7].
- *Datos y etiquetado.* COSIS prevé superposiciones SP 800-53 que cubren datos de entrenamiento, pesos y configuración [9]. No encontré criterios publicados de etiquetado para agentes.
- NIST advierte que la tecnología actual no cumple todavía todos los tenets [7].

**Interpretación propia.** Los diez tenets llevan los principios de SP 800-207 al caso de los agentes. La política dinámica (tenet 4 de 800-207) se convierte en verificación de cada llamada, y el monitoreo de activos (tenet 5) en evidencia independiente del agente. Como son una propuesta publicada en un blog, conviene usarlos como referencia para medir brechas, no como requisito de cumplimiento.

### 4.2 The Open Group

**Lo que afirma la fuente.** No tiene guía oficial sobre IA. Las actas documentan que la IA se trata como tema exploratorio [24][25].

**Interpretación propia.** Las capacidades del Reference Model, según la correspondencia que publica Microsoft, pueden alojar a los agentes sin cambiar el modelo. Por ejemplo, el ABB IAAMP-1.3.7, que corresponde a los mecanismos de autorización de cargas y agentes [36]. Esa correspondencia es de Microsoft y no amplía las publicaciones de The Open Group [36].

### 4.3 Microsoft

**Lo que afirma la fuente.**
- *Identidad.* Pide identidades de agente dedicadas y no credenciales compartidas, con Conditional Access, gobierno de identidades y PIM [21]. Pide además un responsable nombrado y aprobador para cada agente, y probar la revocación [33].
- *Autorización por tarea.* Limitar los permisos al propósito y al riesgo, y pedir aprobación para capacidades de alto impacto [21]. Empezar sin acciones permitidas y habilitarlas de forma gradual [31]. Revisar los permisos agregados y efectivos, y denegar por defecto las herramientas no revisadas [33].
- *Datos.* Clasificar y proteger los datos de instrucciones, contexto, grounding y salidas, y aplicar DLP [22]. Reducir la sobreexposición, gobernar la herencia de etiquetas y definir requisitos para la memoria del agente [21].
- *Contenido no confiable.* El catálogo parte de un objetivo: no se confía por defecto en nada de lo que lee el modelo [29]. Recomienda filtrar entradas y salidas, incluida la inyección indirecta [31].
- *Supervisión.* Registrar planes, llamadas a herramientas y resultados [31], y conservar identificadores de correlación en almacenes resistentes a manipulación [30].
- *Reversibilidad y control humano.* Clasificar las acciones por impacto y reversibilidad, prever una parada de emergencia y la reversión [30]. Exigir intervención humana determinista para acciones irreversibles [31].

**Interpretación propia.** Es la guía más operativa de las tres, pero sus recomendaciones dependen de productos concretos, como Entra Agent ID, Purview o Agent 365 Registry. Para un plan neutral, conviene tomar las áreas de control y dejar de lado las herramientas que nombra.

## 5. Criterios e indicadores medibles

| Fuente | Qué ofrece para medir |
|---|---|
| NIST SP 800-207 | Siete tenets que pueden evaluarse uno por uno [2]. No incluye modelo de madurez. |
| NIST tenets de agentes | Diez criterios formulados como capacidades, útiles como lista de brechas [7]. |
| NIST IR 8596 | Resultados organizados según CSF 2.0, que admite perfiles actual y objetivo [10]. Es un borrador. |
| The Open Group | Capacidades en niveles L1 a L4 (*no verificado en fuente oficial*). No ofrece métricas oficiales. |
| Microsoft | Etapas de implementación y herramientas de seguimiento por escenario [27]. Assessment con comprobaciones por pilar; por ejemplo, revisa 30 días de inicios de sesión de cada identidad de agente [23]. Workshop con priorización «First, Then, Next» [21]. |
| CISA (derivado) | Cuatro etapas de madurez por pilar [37]. |
| DoD (derivado) | Niveles Target y Advanced por capacidad [39]. |

**Propuesta de KPI independientes de proveedor (interpretación propia).** Cada indicador se apoya en la fuente indicada; también valen para servicios externalizados si el proveedor entrega evidencias.
1. Porcentaje de agentes inventariados con identidad propia, responsable y propósito documentado [7][21].
2. Porcentaje de agentes sin privilegio permanente y vida media de las credenciales emitidas [7].
3. Porcentaje de herramientas y conectores con autorización por llamada y denegación por defecto [7][33].
4. Porcentaje de acciones de alto impacto o irreversibles con aprobación humana registrada, junto con la tasa de aprobaciones automáticas como señal de fatiga [7][30].
5. Tiempo medido para revocar un agente en pruebas periódicas [33].
6. Porcentaje de acciones de agentes con evidencia en un almacén independiente y a prueba de manipulación [7][30].
7. Porcentaje de fuentes de grounding y memoria con etiqueta de sensibilidad [21][22].
8. Etapa CISA por pilar para el Zero Trust general [37].

## 6. Silencios y límites

**NIST**
- No hay publicación titulada ni dedicada a «Zero Trust para IA».
- No encontré una revisión de SP 800-207.
- COSIS no tiene borrador público inicial; solo hay concept paper y esquema anotado [9].
- El Cyber AI Profile no pasó a borrador público inicial, según el historial visible [10].
- El proyecto de agentes no tiene todavía descripción de proyecto ni borrador SP 1800 [6].
- Los tenets están en un blog, sin período formal de comentarios [7].
- NIST no propone un modelo de madurez de Zero Trust.

**The Open Group**
- No hay ninguna publicación sobre IA o agentes.
- No pude abrir pubs.opengroup.org ni publications.opengroup.org. Por eso quedan sin verificar los identificadores, las fechas y el texto de Commandments, Core Principles y Reference Model.
- No hay constancia de que el Snapshot 2.0 se haya publicado a la fecha de corte [24][36].

**Microsoft**
- No abrí la «Zero Trust reference architecture for AI» ni el libro electrónico «Zero Trust for AI»; solo conozco su anuncio [20][35].
- Las fechas de varias páginas de Learn no aparecían en los extractos.
- La guía de adopción de 2025 no incluye IA [27]. Su relación formal con el SAF no está declarada en lo que consulté.
- Las cifras del Workshop (700 controles, 116 grupos, 33 carriles) son afirmaciones del propio fabricante [20].

**Derivados**
- No verifiqué si existe una versión de CISA ZTMM posterior a la 2.0 ni una actualización del DoD que incluya IA.

**Contexto normativo**
- El decreto del 29-09-2026 se conoce solo por cómo lo citan las páginas de NIST. No abrí el texto original [9][10].

**Afirmaciones no verificadas** (marcadas en el texto):
- Nombres y agrupación de los Zero Trust Commandments.
- Niveles L1 a L4 del Reference Model.
- Identificadores y fechas de las publicaciones de The Open Group.
- Nombres de las capacidades transversales de CISA.
- Lista de pilares y fecha de la estrategia del DoD.
- Número exacto de respuestas al concept paper del NCCoE.
- Contenido de la arquitectura de referencia para IA de Microsoft.

## 7. Fuentes

Fecha de consulta de todas las fuentes: 2026-11-15.

1. SP 800-207 (ficha), NIST, 08-2020, https://csrc.nist.gov/pubs/sp/800/207/final. Abierta.
2. SP 800-207 (PDF), NIST, 08-2020, https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207.pdf. Abierta (secciones 1 a 3).
3. SP 800-207A, NIST, 09-2023, https://csrc.nist.gov/pubs/sp/800/207/a/final. Abierta.
4. SP 1800-35, NIST/NCCoE, 06-2025, https://csrc.nist.gov/pubs/sp/1800/35/final. Abierta.
5. Concept paper sobre identidad y autorización de agentes, NCCoE, 05-02-2026, https://csrc.nist.gov/pubs/other/2026/02/05/accelerating-the-adoption-of-software-and-ai-agent/ipd. Extracto, más el PDF en nccoe.nist.gov (extracto).
6. NCCoE Agentic AI Identity and Authorization Project Resource Hub, NIST, sin fecha, https://pages.nist.gov/nccoe-ai-identity/index.html. Abierta.
7. Design Tenets for Agent Identity Management Systems, NIST, 27-10-2026, https://www.nist.gov/blogs/cybersecurity-insights/design-tenets-agent-identity-management-systems. Abierta.
8. Back to the Future: Why Agentic AI Needs a Strong Identity Foundation, NIST, 27-08-2026, https://www.nist.gov/blogs/cybersecurity-insights/back-future-why-agentic-ai-needs-strong-identity-foundation. Extracto.
9. SP 800-53 Control Overlays for Super Intelligence Systems (COSIS), NIST, actualizada el 20-10-2026, https://csrc.nist.gov/projects/cosis. Abierta.
10. IR 8596 iprd (Cyber AI Profile), NIST, 16-12-2025, https://csrc.nist.gov/pubs/ir/8596/iprd. Extracto.
11. CSWP 20, NIST, 06-05-2022, https://csrc.nist.gov/pubs/cswp/20/planning-for-a-zero-trust-architecture/final. Extracto; la ficha /final no cargó.
12. Zero Trust (página del Security Forum), The Open Group, sin fecha, https://www.opengroup.org/forum/security/Zerotrust. Abierta.
13. Zero Trust Architecture Working Group, The Open Group, sin fecha, https://www.opengroup.org/forum/security-forum-0/zerotrustsecurityarchitecture. Extracto.
14. Security Forum Members' Meeting, Houston 2024, The Open Group, 10-2024, https://www.opengroup.org/Houston-2024-10/Security. Extracto.
15. AI Risk Management Framework, NIST, página vigente, https://www.nist.gov/itl/ai-risk-management-framework. Extracto.
16. NIST AI 600-1, NIST, 26-07-2024, https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence. Extracto.
17. Summary Analysis of Responses to the RFI on AI Agents, NIST/CAISI, 18-05-2026, https://www.nist.gov/publications/summary-analysis-responses-request-information-regarding-security-considerations-ai. Extracto.
18. AI Agent Standards Initiative, NIST, actualizada el 14-08-2026, https://www.nist.gov/artificial-intelligence/ai-agent-standards-initiative. Extracto.
19. Zero Trust Core Principles Project Charter V2.0, The Open Group, 29-09-2022, https://www.opengroup.org/sites/default/files/pdf/%5BZTA%5D%20Zero%20Trust%20Core%20Principles%20Project%20Charter%20-%20V2.0.pdf. Extracto.
20. New tools and guidance: Announcing Zero Trust for AI, Microsoft, 19-03-2026, https://www.microsoft.com/en-us/security/blog/2026/03/19/new-tools-and-guidance-announcing-zero-trust-for-ai/. Extracto.
21. Microsoft Zero Trust Workshop - AI security, Microsoft, sin fecha visible, https://learn.microsoft.com/en-us/security/zero-trust/workshop-zero-trust-ai-security. Extracto.
22. Secure AI with Zero Trust (SAF), Microsoft, sin fecha visible, https://learn.microsoft.com/en-us/security/saf/technologies/ai/overview. Extracto.
23. Zero Trust Assessment, pilar de IA, Microsoft, sin fecha visible, https://learn.microsoft.com/en-us/security/zero-trust/assessment/ai-pillar. Extracto.
24. Security Forum, Houston Summit 2025, The Open Group, 11-2025, https://www.opengroup.org/events/Houston-2025-11/Security. Extracto.
25. Oslo Summit 2026: Security Portfolio, The Open Group, 04-2026, https://www.opengroup.org/events/Oslo-2026-04/Forums/Security. Extracto.
26. Zero Trust as a security foundation, Microsoft, 15-11-2026, https://learn.microsoft.com/en-us/security/zero-trust/zero-trust-overview. Abierta.
27. Zero Trust adoption framework overview, Microsoft, 05-05-2025, https://learn.microsoft.com/en-us/security/zero-trust/adopt/zero-trust-adoption-overview. Abierta.
28. Zero Trust Assessment documentation, Microsoft, sin fecha visible, https://learn.microsoft.com/en-us/security/zero-trust/assessment/. Extracto.
29. AI Defense Capabilities for Enterprise AI Security, Microsoft, 01-08-2026, https://learn.microsoft.com/en-us/security/zero-trust/catalog-ai-defense-capabilities/catalog-ai-defense-capabilities. Extracto; la URL raíz del catálogo no cargó.
30. Govern, Assure, and Respond (catálogo), Microsoft, sin fecha visible, https://learn.microsoft.com/en-us/security/zero-trust/catalog-ai-defense-capabilities/govern-assure-respond. Extracto.
31. Secure autonomous agentic AI systems, Microsoft, sin fecha visible, https://learn.microsoft.com/en-us/security/zero-trust/sfi/secure-agentic-systems. Extracto.
32. Reduce autonomous agentic AI risk, Microsoft, sin fecha visible, https://learn.microsoft.com/en-us/security/zero-trust/sfi/manage-agentic-risk. Extracto.
33. Least privilege for AI agents, Microsoft, sin fecha visible, https://learn.microsoft.com/en-us/security/zero-trust/sfi/least-privilege-for-ai-agents. Extracto.
34. Microsoft Secure Future Initiative (SFI) overview, Microsoft, sin fecha visible, https://learn.microsoft.com/en-us/security/zero-trust/sfi/secure-future-initiative-overview. Extracto.
35. Advance Zero Trust for AI, Microsoft, 04-08-2026, https://www.microsoft.com/en-us/security/blog/2026/08/04/advance-zero-trust-for-ai-new-tools-and-guidance-to-secure-ai-agents-and-devsecops/. Extracto.
36. Map The Open Group Zero Trust model to SAF, Microsoft, 15-11-2026, https://learn.microsoft.com/en-us/security/saf/framework-mappings/open-group-zero-trust. Abierta.
37. Zero Trust Maturity Model (v2.0), CISA (derivado), 11-04-2023, https://www.cisa.gov/resources-tools/resources/zero-trust-maturity-model. Extracto.
38. DoD Zero Trust Reference Architecture v2.0, DoD (derivado), 07-2022, https://dodcio.defense.gov/Portals/0/Documents/Library/%28U%29ZT_RA_v2.0%28U%29_Sep22.pdf. Extracto.
39. ZT Strategy Placemats, DoD (derivado), sin fecha, https://dodcio.defense.gov/Portals/0/Documents/Library/ZT-StrategyPlacemats.pdf. Extracto.

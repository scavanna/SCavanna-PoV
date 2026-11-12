# Nivel 4 · Gobierno y operación · Gobernar y operar la IA en Azure

*Seguridad de agentes de IA en Microsoft Foundry Ninja Training · Edición 2026*

[← Nivel 3 · Avanzado](03_Nivel_3_Avanzado.md) · [Índice del programa](README.md) · [Comunidad →](05_Comunidad.md)

<a id="operacion"></a>

Marcos y regulación (CAF, Well-Architected, Zero Trust para IA, NIST AI RMF, ISO/IEC 42001 y normativa de MCSA), modelo operativo y ciclo de vida de los agentes, FinOps de IA, denial of wallet y LLMjacking. Terminas con el proyecto integrador: la arquitectura de la infografía, corregida y desplegada en el laboratorio, con evidencia por capa para un comité de gobierno.

*L300–L400 · 4 módulos · ~20 horas · 40 recursos*

**Módulos de este nivel:** [O1 Marcos y gobierno de la IA](#o1) · [O2 Modelo operativo y RACI](#o2) · [O3 FinOps y abuso de recursos](#o3) · [O4 Proyecto integrador](#o4)

<a id="o1"></a>

## O1 · Marcos y gobierno de la IA en Azure: CAF, Well-Architected, Zero Trust para IA, NIST AI RMF, ISO/IEC 42001 y regulación en MCSA

*L300–L400 · ~5 h · Origen: Nuevo en esta edición (base: CAF y Well-Architected para IA, Zero Trust para IA, MCSB v2 y marcos externos; referencia regulatoria al 7 de noviembre de 2026, no asesoría legal)*

La infografía declara principios —mínimo privilegio, autenticación en cada salto, monitoreo en cada capa— y una capa de cumplimiento, pero no dice frente a qué marco se miden. Este módulo asegura la gestión del cumplimiento de la **Capa 8 · Datos y cumplimiento** y los principios transversales. Los marcos de Microsoft se complementan: el **Cloud Adoption Framework** (Govern, Manage y Secure AI, más el gobierno de PaaS), el **Well-Architected** para IA, **Zero Trust para IA** (marzo de 2026, con un pilar de IA en el Workshop y comprobaciones en el Assessment) y el **MCSB v2**, cuyos controles van de AI-1 (modelos aprobados) a AI-7 (red teaming continuo). Para las amenazas usas OWASP y MITRE ATLAS.

Para gestionar riesgos sirven el **NIST AI RMF** (en revisión), con su perfil de IA generativa AI 600-1, e **ISO/IEC 42001**: la certificación de Microsoft, con Foundry en su alcance, es evidencia del proveedor y no reemplaza tu sistema de gestión. En la UE, el *Digital Omnibus on AI* (julio de 2026) aplazó el alto riesgo a diciembre de 2027 y agosto de 2028. En **MCSA**, Perú tiene ley y reglamento vigentes, Ecuador una norma vinculante sobre datos personales en IA y en Chile una comisión del Senado aprobó en general, el 26 de octubre de 2026, el proyecto por niveles de riesgo. Es referencia, no asesoría legal: decide con Legal, privacidad y RR. HH.

**Por qué importa**

Comités, auditores y reguladores preguntan «¿frente a qué marco?». Mapear cada control de la arquitectura a CAF, Well-Architected, Zero Trust para IA, MCSB v2, NIST e ISO/IEC 42001 convierte la evidencia técnica en evidencia de gobierno, ordena prioridades con un lenguaje común y te prepara para los proyectos de ley de MCSA antes de que se aprueben, en lugar de rediseñar después.

**Qué vas a lograr**

- Mapear los controles de la arquitectura segura a CAF, Well-Architected, Zero Trust para IA y MCSB v2.
- Estructurar la gestión de riesgos de IA con NIST AI RMF, AI 600-1 e ISO/IEC 42001, y usar la evidencia del proveedor.
- Ubicar el estado de la regulación de IA de cada país de MCSA al 7 de noviembre de 2026, con la UE como referencia.
- Priorizar brechas con las áreas del pilar de IA del Zero Trust Workshop.
- Preparar evidencias técnicas para que Legal decida, sin interpretar la ley.

> **Novedad.** Chile, después de la tabla del programa de Copilot: el 26 de octubre de 2026 la Comisión de Desafíos del Futuro del Senado aprobó en general, por unanimidad, el proyecto de IA por niveles de riesgo (multas de hasta 20.000 UTM), sin la indicación sustitutiva del Gobierno y con plazo de indicaciones propuesto al 4 de diciembre de 2026. El 28 de octubre se presentó la moción Boletín 18.820-19, que propone identidad verificable por agente, registro de autorizaciones, trazabilidad, control de delegaciones y registro de «cuasi incidentes de pérdida de control». Son fuentes de prensa: confírmalas con Legal ([La Tribuna](https://www.latribuna.cl/politica/2026/11/04/chile-avanza-hacia-una-ley-que-podria-prohibir-usos-de-la-inteligencia-artificial-y-aplicar-multas-millonarias.html), [Prensa Mercosur](https://prensamercosur.org/2026/11/05/chile-chile-regula-agentes-de-ia-identidad-y-trazabilidad/)).

> **Atención.** Fechas que debes revalidar: el Reglamento (UE) 2026/1744 se firmó el 8 de julio y se publicó el 24 de julio de 2026, pero verifica en el texto la fecha exacta de entrada en vigor; el AI RMF de NIST está en revisión sin fecha publicada y el Cyber AI Profile (NIST IR 8596) sigue como borrador preliminar ([Digital Omnibus on AI](https://www.europarl.europa.eu/legislative-train/package-digital-omnibus/file-digital-omnibus-on-ai), [NIST IR 8596](https://csrc.nist.gov/pubs/ir/8596/iprd)).

> **Atención.** Choque de siglas: OWASP publica un «Agent Control Standard» y Microsoft una «Agent Control Specification» dentro del Agent Governance Toolkit (vista previa pública). No los trates como equivalentes en tu marco de control ni en tus informes al comité ([iniciativa agéntica de OWASP](https://genai.owasp.org/initiatives/agentic-security-initiative/), [ASSERT y ACS](https://devblogs.microsoft.com/foundry/build-2026-open-trust-stack-ai-agents/)).

> **Consejo Ninja.** Compliance Manager tiene plantillas premium de IA —EU AI Act, ISO/IEC 23894, ISO/IEC 42001 y NIST AI RMF— y con E5 puedes elegir hasta tres; úsalas para registrar las evidencias de la arquitectura. La certificación ISO/IEC 42001 de Microsoft, con Foundry y Security Copilot en su alcance, es evidencia del proveedor y no sustituye tu propio sistema de gestión de IA. Se profundiza en el programa de Purview Compliance Manager, módulo M3 ([evaluaciones](https://learn.microsoft.com/en-us/purview/compliance-manager-assessments), [ISO/IEC 42001](https://learn.microsoft.com/en-us/compliance/regulatory/offering-iso-42001)).

**¿Tienes poco tiempo?**

- [Secure AI – guidance to set up your organization's AI security process (Cloud Adoption Framework)](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai/secure) · Documentación
- [Microsoft Zero Trust Workshop - AI security](https://learn.microsoft.com/en-us/security/zero-trust/workshop-zero-trust-ai-security) · Documentación
- [Microsoft cloud security benchmark v2 - Artificial Intelligence Security](https://learn.microsoft.com/en-us/security/benchmark/azure/mcsb-v2-artificial-intelligence-security) · Documentación
- [AI Risk Management Framework (NIST)](https://www.nist.gov/itl/ai-risk-management-framework) · Documentación

**Marcos y regulación de la IA (incluida MCSA)**

| Ámbito | Marco o norma | Versión, estado y fecha | Qué aporta o exige | Cómo se usa con agentes de Foundry | Fuente |
|---|---|---|---|---|---|
| Microsoft | Cloud Adoption Framework: Govern AI, Manage AI, Secure AI y gobierno de PaaS para IA | Vigente | Procesos continuos; inventario con Azure Resource Graph, Defender for Cloud y Entra Agent ID; modelos aprobados, guardrails mínimos, cuotas y gateway; API Management para proteger endpoints MCP | Gobierno de la plataforma (M7) y modelo operativo (O2) | [Secure AI](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai/secure) · [Gobierno de PaaS](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai/platform/governance) |
| Microsoft | Well-Architected para cargas de IA | Vigente | Seguridad de contenido en todo el ciclo, detección avanzada, cuotas ligadas a identidad, gateway de IA, bloqueo del acceso directo a datos y personas del equipo | Revisión de la arquitectura (O4) y RACI (O2) | [Principios de diseño](https://learn.microsoft.com/en-us/azure/well-architected/ai/design-principles) · [Diseño de aplicaciones](https://learn.microsoft.com/en-us/azure/well-architected/ai/application-design) |
| Microsoft | Zero Trust para IA: pilar de IA del Workshop y Zero Trust Assessment | Anunciado el 19-mar-2026; ampliado el 4-ago-2026 (DevSecOps y memoria); Workshop actualizado el 6-nov-2026 | Áreas: mapear riesgos, registrar agentes, autenticación y acceso, red, datos, construir agentes seguros, y detectar y responder | Hoja de ruta por áreas; Assessment con cuentas de solo lectura | [Workshop de IA](https://learn.microsoft.com/en-us/security/zero-trust/workshop-zero-trust-ai-security) · [Anuncio](https://www.microsoft.com/en-us/security/blog/2026/03/19/new-tools-and-guidance-announcing-zero-trust-for-ai/) |
| Microsoft | MCSB v2 · inteligencia artificial | Revisado el 1-dic-2025 | AI-1 modelos aprobados, AI-2 filtrado multicapa, AI-3 meta-prompts de seguridad, AI-4 mínimo privilegio de funciones, AI-5 humano en el circuito, AI-6 monitoreo y AI-7 red teaming continuo; es guía, no certificación | Línea base técnica con mapeo a Azure Policy | [MCSB v2 para IA](https://learn.microsoft.com/en-us/security/benchmark/azure/mcsb-v2-artificial-intelligence-security) |
| Microsoft | CAAT y AI Defense Capabilities | 1-ago-2026 | 14 técnicas de ataque en 5 familias y 9 familias de defensa con dueños: arquitectura, ingeniería, SecOps y riesgo | Puente entre amenaza, control y dueño | [CAAT](https://learn.microsoft.com/en-us/security/zero-trust/catalog-ai-attack-techniques/catalog-ai-attack-techniques) · [Capacidades de defensa](https://learn.microsoft.com/en-us/security/zero-trust/catalog-ai-defense-capabilities/catalog-ai-defense-capabilities) |
| Microsoft | Taxonomía de modos de fallo en sistemas agénticos | v2.0 del 4-jun-2026 (v1.0 de abril de 2025) | Siete modos nuevos, como la cadena de suministro agéntica, la escalada de confianza entre agentes y el abuso de MCP; la evasión del humano en el circuito fue el fallo más explotado | Cobertura del red teaming (A1) y del diseño multiagente (A7) | [Taxonomía v2.0](https://www.microsoft.com/en-us/security/blog/2026/06/04/updating-taxonomy-failure-modes-agentic-ai-systems-year-red-teaming-taught-us/) |
| Microsoft | Clasificación de severidad del MSRC para sistemas de IA | Vigente | Severidad por impacto de la inyección de prompts, la perturbación de entradas, la divulgación inferencial y la manipulación de modelos | Clasificar incidentes (A5) | [Severidad para IA](https://www.microsoft.com/en-us/msrc/aibugbar) |
| Microsoft | Responsible AI Standard v2 | Junio de 2022 | Rendición de cuentas, transparencia, equidad, confiabilidad y seguridad, privacidad e inclusión | Principios de la política interna de IA | [Responsible AI Standard](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/final/en-us/microsoft-brand/documents/Microsoft-Responsible-AI-Standard-General-Requirements.pdf) |
| Amenazas | OWASP Top 10 for LLM Applications | 2025 (publicado el 18-nov-2024; versión en español del 12-mar-2025) | LLM01 a LLM10, incluido LLM10 Unbounded Consumption | Vocabulario común del modelado de amenazas (F3) | [OWASP LLM Top 10](https://genai.owasp.org/llm-top-10/) |
| Amenazas | OWASP Top 10 for Agentic Applications | «for 2026», publicado el 9-dic-2025 | ASI01 a ASI10, como secuestro del objetivo, mal uso de herramientas, cadena de suministro agéntica y comunicación insegura entre agentes | Amenazas agénticas del modelado (F3) | [OWASP agéntico](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) |
| Amenazas | MITRE ATLAS | Datos v2026.10 (v6.1.0), con cadencia mensual | Tácticas, técnicas, mitigaciones y casos; AML.T0010 Supply Chain Compromise y AML.M0023 Maintain an AI Bill of Materials | Identificadores en reglas y playbooks | [Versiones de ATLAS](https://github.com/mitre-atlas/atlas-data/releases) |
| Gestión de riesgos | NIST AI RMF 1.0 y perfil de IA generativa NIST AI 600-1 | 26-ene-2023 (en revisión) y 26-jul-2024 | Funciones Govern, Map, Measure y Manage; riesgos de la IA generativa | Registro de riesgos; el red teaming alimenta Measure | [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) |
| Gestión de riesgos | NIST IR 8596 · Cyber AI Profile | Borrador preliminar del 16-dic-2025 | CSF 2.0 aplicado a la IA: Secure, Defend y Thwart | Referencia para equipos que ya usan CSF | [NIST IR 8596](https://csrc.nist.gov/pubs/ir/8596/iprd) |
| Gestión de riesgos | ISO/IEC 42001 · sistema de gestión de IA | 2023; Foundry y Security Copilot en el alcance certificado de Microsoft | Requisitos de un sistema de gestión de la IA | Evidencia del proveedor; no reemplaza tu propio sistema | [ISO/IEC 42001 en Microsoft](https://learn.microsoft.com/en-us/compliance/regulatory/offering-iso-42001) |
| Gestión de riesgos | Compliance Manager · plantillas de IA | Vigente | Plantillas premium de EU AI Act, ISO/IEC 23894, ISO/IEC 42001 y NIST AI RMF; con E5, hasta tres premium | Evaluación con acciones de mejora vinculadas a evidencias | [Evaluaciones](https://learn.microsoft.com/en-us/purview/compliance-manager-assessments) |
| Unión Europea (referencia) | Ley de IA y Reglamento (UE) 2026/1744 (Digital Omnibus on AI) | Firmado el 8-jul-2026 y publicado el 24-jul-2026; alto riesgo autónomo: 2-dic-2027; integrado en productos: 2-ago-2028; marcado de contenido generado por IA: 2-dic-2026 para sistemas comercializados antes del 2-ago-2026 | Calendario de obligaciones y nuevas prohibiciones | Referencia para multinacionales; verifica la fecha de entrada en vigor | [Digital Omnibus on AI](https://www.europarl.europa.eu/legislative-train/package-digital-omnibus/file-digital-omnibus-on-ai) |
| MCSA · México | Sin ley federal de IA; iniciativas de una Ley General para la Regulación y Uso Ético de la IA (junio de 2026) y de reforma del artículo 73 constitucional (5-ago-2026); reforma de mayo de 2026 a la Ley Federal del Derecho de Autor sobre clonación de voz | Iniciativas en comisión, no vigentes | Anticipan registros de sistemas de alto riesgo y evaluaciones de impacto (Congreso de la Unión) | Inventario de agentes en el Control Plane, casos de uso documentados y evidencias de auditoría y red teaming | [Cámara de Diputados](https://comunicacionsocial.diputados.gob.mx/index.php/boletines/-propone-iniciativa-crear-ley-para-la-regulacion-y-uso-etico-de-la-inteligencia-artificial-en-el-pais) · [Senado](https://infosen.senado.gob.mx/sgsp/gaceta/66/2/2026-08-05-1/assets/documentos/Inic_Morena_Dip_Georgina_art_73_CPEUM.pdf) |
| MCSA · Guatemala | No se identificó ley, estrategia ni proyecto específico de IA | — | Rigen las normas de datos, imagen y derechos de autor | Transparencia y supervisión humana como buenas prácticas | [Panorama regional](https://consortiumlegal.com/2026/02/23/panorama-regulatorio-de-la-inteligencia-artificial-en-centroamericana/) |
| MCSA · El Salvador | Ley de Fomento a la Inteligencia Artificial y Tecnologías (Decreto 234) | Vigente: emitida el 26-feb-2025 y publicada el 3-mar-2025 | Única ley específica de IA de Centroamérica; transparencia, rendición de cuentas y capacitación (Asamblea Legislativa) | Documenta los casos de uso de cada agente y la capacitación de quienes lo operan | [Asamblea Legislativa](https://www.asamblea.gob.sv/leyes-y-decretos/view/6137) |
| MCSA · Honduras | Sin ley de IA; proyecto sobre el consumo de agua de los centros de datos y la IA | Proyecto (septiembre de 2026) | No regula el uso de la IA en las organizaciones (Congreso Nacional) | Aplica las buenas prácticas del programa | [Tiempo](https://tiempo.hn/honduras/2026/09/28/inteligencia-artificial-regularizacion-congreso-nacional/) |
| MCSA · Nicaragua | Decreto A.N. 8933: acuerdo de la Organización Mundial para la Cooperación en IA (La Gaceta 179) | Publicado el 1-oct-2026; cooperación internacional, no regulación interna | Sin obligaciones específicas para agentes (Asamblea Nacional) | Rige la ley de datos personales | [La Gaceta](https://digesto.asamblea.gob.ni/consultas/util/pdf.php?type=rdd&rdd=wmuyoFojZnQ%3D) |
| MCSA · Costa Rica | Estrategia Nacional de IA 2024–2027 y proyecto de ley 23.771 | Estrategia no vinculante (octubre de 2024); proyecto en la Asamblea Legislativa | Principios orientadores (MICITT y Asamblea Legislativa) | Guía de principios; vigila el proyecto | [AI Policy Tracker](https://aipolicytracker.org/jurisdictions/costa-rica) |
| MCSA · Panamá | Estrategia Nacional de IA (Resolución de Gabinete 75) y proyecto 588 de gobernanza adaptativa por niveles de impacto (bajo, moderado, alto y crítico) | Estrategia aprobada el 11-ago-2026 (Gaceta 30592-A); proyecto aprobado en tercer debate el 19-ago-2026, pendiente de sanción | Clasificación por impacto, supervisión humana y trazabilidad (Consejo de Gabinete y Asamblea Nacional) | Clasifica los agentes por impacto y conserva trazas, auditoría y aprobaciones | [Gaceta Oficial](https://www.gacetaoficial.gob.pa/storage/gacetas/2026/08/30592_A/104761.pdf) · [Asamblea Nacional](https://www.asamblea.gob.pa/Noticias/Actualidad/REGLAS-DE-GOBERNANZA-EN-APLICACION-DE-LA-IA-) |
| MCSA · Colombia | CONPES 4144 (Política Nacional de IA); Ley 2502 de 2025 (agravante por suplantación con IA); Circular Externa 002 de 2024 de la SIC sobre datos personales en IA; proyectos 025/2026C, 065/26 y 138/26 | Política vigente desde el 14-feb-2025; proyectos en trámite (el 043/2025S fue archivado) | Sin ley integral; la SIC aplica la protección de datos a la IA (CONPES, MinCiencias, SIC y Congreso) | Clasificación y DLP de los datos personales que procesa el agente y evaluación de impacto | [CONPES 4144](https://inteligenciaartificial.minciencias.gov.co/wp-content/uploads/2025/09/CONPES-4144) · [Normatividad](https://www.iaencolombia.org/normatividad) · [Proyecto 025/2026C](https://congresovisible.uniandes.edu.co/proyectos-de-ley/ppor-medio-de-la-cual-se-regula-la-inteligencia-artificial-en-colombia-para-garantizar-su-desarrollo-etico-y-responsable-y-se-dictan-otras-disposiciones-regula-la-inteligencia-artificial/15422/) |
| MCSA · Venezuela | Código de Ética para el Desarrollo y Aplicación Responsable de la IA; proyecto de ley aprobado en primera discusión el 19-nov-2024 | Código voluntario (19-feb-2026); proyecto pendiente | Principios de transparencia, privacidad y rendición de cuentas (MINCYT y Asamblea Nacional) | Guía interna para la política de IA | [Código de Ética](https://mincyt.gob.ve/wp-content/uploads/2026/02/Codigo_de_Etica_de_Inteligencia_Artificial_de_la_Republica_Bolivariana-1.pdf) |
| MCSA · Ecuador | Norma SPDP-SPD-2026-0009-R sobre datos personales en sistemas de IA; estrategia EFIA-EC; NTE INEN-ISO/IEC 42001 voluntaria | Vinculante desde el 10-mar-2026 (reformada en septiembre de 2026); proyecto de ley archivado el 15-sep-2026 y nuevo proyecto en comisión | Obligaciones vigentes para los datos personales que trata la IA (Superintendencia de Protección de Datos Personales) | Purview para Foundry, DLP en tiempo de ejecución, auditoría y evaluaciones de impacto | [Regulación en Ecuador](https://oscarobando.ai/es/regulacion-ia-ecuador/) · [Asamblea Nacional](https://www.asambleanacional.gob.ec/es/noticia/119354-pleno-archiva-proyecto-de-ley-de-inteligencia) |
| MCSA · Perú | Ley 31814 y su reglamento (DS 115-2025-PCM) | Publicado el 9-sep-2025; vigente desde el 22-ene-2026, con cronograma para el sector privado | Clasifica los usos por riesgo; para el riesgo alto, transparencia, registros y supervisión humana (PCM, Secretaría de Gobierno y Transformación Digital) | Inventario y clasificación de agentes, trazas protegidas, auditoría de Purview y aprobación humana de herramientas | [DS 115-2025-PCM](https://www.gob.pe/institucion/pcm/normas-legales/7133522-115-2025-pcm) · [Resumen de Cuatrecasas](https://www.cuatrecasas.com/resources/que-establece-el-reglamento-de-la-ley-de-inteligencia-artificial-68c19ecd38db6505769013.pdf) |
| MCSA · Bolivia | P.L. 165/2025-2026 C.S. (IA en el sistema educativo) | En comisión desde junio de 2026 | Sin obligaciones para el uso de la IA en las organizaciones (Cámara de Senadores) | Aplica las buenas prácticas del programa | [Senado](https://www.senado.gob.bo/area-legislativa/proyectos-de-ley-en-tratamiento/831) |
| MCSA · Chile | Proyecto de ley de IA por niveles de riesgo (boletines 15869-19 y 16821-19); moción Boletín 18.820-19 sobre agentes; Ley 21.719 de datos personales | Aprobado por la Cámara el 13-oct-2025; el 26-oct-2026 la Comisión de Desafíos del Futuro del Senado lo aprobó en general, por unanimidad y sin la indicación sustitutiva del Gobierno (plazo de indicaciones propuesto: 4-dic-2026); moción presentada el 28-oct-2026; la Ley 21.719 rige desde el 1-dic-2026 salvo prórroga | Enfoque por riesgo con multas de hasta 20.000 UTM; la moción propone identidad verificable por agente, registro de autorizaciones, trazabilidad, control de delegaciones y registro de cuasi incidentes de pérdida de control (Congreso Nacional) | Evaluación de riesgos y transparencia; Entra Agent ID, auditoría, trazas y los playbooks de A5 anticipan la moción | [La Tribuna](https://www.latribuna.cl/politica/2026/11/04/chile-avanza-hacia-una-ley-que-podria-prohibir-usos-de-la-inteligencia-artificial-y-aplicar-multas-millonarias.html) · [Prensa Mercosur](https://prensamercosur.org/2026/11/05/chile-chile-regula-agentes-de-ia-identidad-y-trazabilidad/) · [Ley de IA en Chile](https://www.codigoia.cl/ley-ia-chile/) |
| MCSA · Argentina | Sin ley; proyectos con clasificación por riesgo, evaluaciones de impacto y rotulado de contenido (con el INTI como autoridad propuesta), además del 0253-D-2026 y el expediente 1004/26 del Senado | Proyectos sin dictamen (2026) | Congreso de la Nación | Evaluaciones de impacto y rotulado de contenido generado por IA de forma voluntaria | [Quorum](https://quorum.politeia.ar/proyectos/proyecto-de-regimen-legal-aplicable-para-el-uso-responsable-de-la-ia) · [Senado](https://www.senado.gob.ar/parlamentario/comisiones/verExp/1004.26/S/PL) |
| MCSA · Uruguay | Estrategia Nacional de IA 2024–2030 (artículo 74 de la Ley 20.212) | Aprobada el 21-nov-2024; no crea obligaciones nuevas | Orienta a los sectores público y privado (AGESIC) | Compleméntala con la ley de datos personales | [AGESIC](https://www.gub.uy/agencia-gobierno-electronico-sociedad-informacion-conocimiento/comunicacion/publicaciones/estrategia-nacional-inteligencia-artificial-2024-2030) |
| MCSA · Paraguay | Sin ley de IA; Hoja de Ruta Nacional de IA, evaluación RAM de la UNESCO, proyecto en el Senado y directrices de la Corte Suprema para el Poder Judicial | Proyecto en trámite (2026) | MITIC y Congreso; la Ley 7593/2025 es de datos personales, no de IA | Guía de principios; vigila el proyecto | [MITIC](https://www.ip.gov.py/ip/2026/06/26/mitic-presenta-avances-del-pais-en-inteligencia-artificial-en-cumbre-regional-sobre-etica-de-la-ia/) |
| MCSA · Regional | III Cumbre Ministerial sobre Ética de la IA de América Latina y el Caribe (Santo Domingo) | 25 y 26 de junio de 2026 | Tendencia hacia evaluaciones éticas y hojas de ruta nacionales | Anticipa evaluaciones de impacto ético | [MITIC](https://www.ip.gov.py/ip/2026/06/26/mitic-presenta-avances-del-pais-en-inteligencia-artificial-en-cumbre-regional-sobre-etica-de-la-ia/) |

Referencia, no asesoría legal: situación al 7 de noviembre de 2026 según fuentes públicas, sin interpretación jurídica. MCSA = México, Centroamérica y Sudamérica, sin Brasil. Las filas de MCSA actualizan la tabla del programa de Seguridad de Microsoft 365 Copilot, agentes y Copilot Studio (módulo O6); la de Chile incorpora la aprobación en general del 26 de octubre de 2026 y la moción del 28 de octubre, ambas de fuentes de prensa. Las obligaciones, los plazos y su aplicación a tu organización los define Legal con el texto oficial vigente, junto con privacidad y RR. HH. Las leyes de datos personales, ciberseguridad y sector financiero están en la hoja «Normativa MCSA».

### Documentación, cursos y credenciales

- [Microsoft Zero Trust Workshop - AI security](https://learn.microsoft.com/en-us/security/zero-trust/workshop-zero-trust-ai-security) · Documentación · Oficial · Nuevo · Microsoft Learn · 6 nov 2026. Pilar de IA del Zero Trust Workshop: inventario y registro de agentes, acceso y autenticación, red, datos, construcción segura de agentes con red teaming y detección y respuesta.
- [Digital Omnibus on AI - Legislative Train Schedule](https://www.europarl.europa.eu/legislative-train/package-digital-omnibus/file-digital-omnibus-on-ai) · Documentación · Comunidad · Nuevo · European Parliamentary Research Service · Parlamento Europeo · 25 oct 2026. Cronología del Omnibus: alto riesgo autónomo al 2-dic-2027, alto riesgo integrado en productos al 2-ago-2028, marcado de contenido generado por IA al 2-dic-2026 y prohibición de prácticas que generen NCII o CSAM.
- [Secure AI – guidance to set up your organization's AI security process (Cloud Adoption Framework)](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai/secure) · Documentación · Oficial · Microsoft Learn · Cloud Adoption Framework. Tres fases: descubrir riesgos (STRIDE + MITRE ATLAS/OWASP, red teaming), proteger recursos y datos (inventario con Resource Graph y Defender for Cloud, identidades administradas, red privada del Agent Service) y detectar amenazas.
- [AI Risk Management Framework (NIST)](https://www.nist.gov/itl/ai-risk-management-framework) · Documentación · Comunidad · NIST ITL · NIST · 7 abr 2026. Portal del AI RMF 1.0 (ene-2023) y del perfil de IA generativa NIST AI 600-1 (jul-2024); indica que el AI RMF se está revisando y que en abr-2026 se publicó una nota conceptual de perfil para infraestructura crítica.
- [Regulation (EU) 2026/1744 (Digital Omnibus on AI) - Official Journal](https://publications.europa.eu/resource/cellar/b459c07f-86fb-11f1-bf5e-01aa75ed71a1.0006.01/DOC_1) · Documentación · Comunidad · Nuevo · Parlamento Europeo y Consejo · Publications Office of the EU · 24 jul 2026. Texto oficial del reglamento que modifica la Ley de IA de la UE: simplificación, aplazamiento de obligaciones de alto riesgo y nuevas prohibiciones.
- [Design principles for AI workloads on Azure (Well-Architected Framework)](https://learn.microsoft.com/en-us/azure/well-architected/ai/design-principles) · Documentación · Oficial · Microsoft Learn · Azure Well-Architected Framework. Principios por pilar para cargas de IA; en seguridad pide ganar la confianza del usuario con seguridad de contenido en todo el ciclo, eliminar datos personales innecesarios de índices y cachés, cifrar en reposo y en tránsito y detectar amenazas.
- [Application design for AI workloads on Azure (Well-Architected)](https://learn.microsoft.com/en-us/azure/well-architected/ai/application-design) · Documentación · Oficial · Microsoft Learn. Recomendaciones de diseño: priorizar controles de seguridad e IA responsable, cuotas y límites ligados a identidad, gateway de IA para políticas y bloquear el acceso directo a almacenes de datos.
- [NIST IR 8596 (iprd) Cybersecurity Framework Profile for Artificial Intelligence (Cyber AI Profile)](https://csrc.nist.gov/pubs/ir/8596/iprd) · Documentación · Comunidad · Vista previa · Katerina Megas, Barbara Cuthill et al. (NIST/MITRE) · NIST CSRC · 16 dic 2025. Borrador preliminar del perfil CSF 2.0 para IA con tres áreas (Secure, Defend, Thwart) y prioridades por subcategoría; comentarios cerrados el 30-ene-2026. *Nota:* Sigue en borrador preliminar a nov-2026 (pendiente de borrador público inicial)

### Anuncios y blogs oficiales

- [Advance Zero Trust for AI: New tools and guidance to secure AI agents and DevSecOps](https://www.microsoft.com/en-us/security/blog/2026/08/04/advance-zero-trust-for-ai-new-tools-and-guidance-to-secure-ai-agents-and-devsecops/) · Blog oficial · Empleado de Microsoft · Nuevo · Ron Pessner · Microsoft Security Blog · 4 ago 2026. Amplía Zero Trust for AI con chequeos de IA, SecOps e infraestructura en el Zero Trust Assessment, un pilar DevSecOps en el Workshop y guía sobre memoria de IA como frontera de seguridad.
- [New tools and guidance: Announcing Zero Trust for AI](https://www.microsoft.com/en-us/security/blog/2026/03/19/new-tools-and-guidance-announcing-zero-trust-for-ai/) · Blog oficial · Empleado de Microsoft · Mike Adams · Microsoft Security Blog · 19 mar 2026. Lanza Zero Trust for AI: pilar de IA en el Zero Trust Workshop (700 controles), pilares de Datos y Red en el Zero Trust Assessment y una arquitectura de referencia para IA basada en verificar explícitamente, mínimo privilegio y asumir brecha.

### Comunidad: blogs, libros, newsletters y eventos

- [Chile: comisión del Senado aprueba en general la ley de IA (La Tribuna)](https://www.latribuna.cl/politica/2026/11/04/chile-avanza-hacia-una-ley-que-podria-prohibir-usos-de-la-inteligencia-artificial-y-aplicar-multas-millonarias.html) · Blog · Comunidad · Nuevo · Jorge Monares Olivares · La Tribuna (Chile) · 4 nov 2026. La Comisión de Desafíos del Futuro del Senado aprobó por unanimidad legislar el proyecto de IA basado en riesgos (multas de hasta 20.000 UTM) sin la indicación sustitutiva del Gobierno; plazo de indicaciones propuesto: 4-dic-2026.
- [Chile regula agentes de IA: identidad y trazabilidad (Boletín 18.820-19)](https://prensamercosur.org/2026/11/05/chile-chile-regula-agentes-de-ia-identidad-y-trazabilidad/) · Blog · Comunidad · Vista previa · Nuevo · Redacción Central · Prensa Mercosur · 5 nov 2026. Moción ingresada el 28-oct-2026 para modificar la Ley Marco de Ciberseguridad 21.663: identidad digital verificable por agente, registro de autorizaciones, trazabilidad reconstruible, control de delegaciones y registro de «cuasi incidentes de pérdida de control». *Nota:* Proyecto en etapa inicial; verificar en el sitio del Senado antes de enseñarlo como obligación

**Manos a la obra**

1. `Laboratorio` Mapea dos controles de cada capa de la arquitectura corregida a CAF, Well-Architected, el área del Zero Trust Workshop, el control del MCSB v2 (AI-1 a AI-7), la función del NIST AI RMF y la amenaza OWASP o ATLAS que mitigan ([MCSB v2 para IA](https://learn.microsoft.com/en-us/security/benchmark/azure/mcsb-v2-artificial-intelligence-security), [Zero Trust Workshop de IA](https://learn.microsoft.com/en-us/security/zero-trust/workshop-zero-trust-ai-security)). Evidencia: matriz de control en una hoja de cálculo.
2. `Laboratorio` Recorre los siete controles del MCSB v2 para IA sobre tu laboratorio y anota la evidencia de cada uno: política de modelos aprobados, guardrails, meta-prompt de seguridad, mínimo privilegio de herramientas, aprobación humana, monitoreo y red teaming ([MCSB v2 para IA](https://learn.microsoft.com/en-us/security/benchmark/azure/mcsb-v2-artificial-intelligence-security), [mapeo a Azure Policy](https://learn.microsoft.com/en-us/security/benchmark/azure/mcsb-v2-controls-policy-mapping)). Evidencia: lista de verificación con estado y brechas.
3. `Laboratorio` Arma el registro de riesgos del agente de laboratorio con las funciones Govern, Map, Measure y Manage del NIST AI RMF y los riesgos de la IA generativa del perfil AI 600-1; conecta Measure con la tasa de éxito de ataque de [A1](03_Nivel_3_Avanzado.md#a1) ([NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework)). Evidencia: registro de riesgos con dueño, tratamiento y fecha de revisión.
4. `Laboratorio parcial` Crea en Compliance Manager una evaluación con la plantilla de ISO/IEC 42001 o de NIST AI RMF y vincula tres acciones de mejora a evidencias del laboratorio ([evaluaciones de Compliance Manager](https://learn.microsoft.com/en-us/purview/compliance-manager-assessments)). Limitación: las plantillas premium tienen un cupo según la licencia y el inquilino de prueba dura un mes. Evidencia: evaluación con las acciones vinculadas.
5. `Laboratorio` Completa el mapa regulatorio de los países de MCSA donde operas con la tabla de este módulo: estado, autoridad e implicancias para tus agentes (inventario, clasificación por riesgo, registros, supervisión humana y residencia), y pide a Legal que lo revise ([ley de IA de Chile](https://www.codigoia.cl/ley-ia-chile/), [reglamento de Perú](https://www.gob.pe/institucion/pcm/normas-legales/7133522-115-2025-pcm)). Evidencia: mapa revisado por Legal, sin interpretación jurídica propia.
6. `Laboratorio` Redacta el registro de decisión de residencia: no hay data zone de Latinoamérica; compara despliegues Global, Data Zone y Standard, y anota que la red administrada incluye Brazil South pero no México, que el tier AI Gateway no está en MCSA y que el red teaming en la nube corre fuera de la región ([tipos de despliegue](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/deployment-types), [red administrada](https://learn.microsoft.com/en-us/azure/foundry/how-to/managed-virtual-network)). Evidencia: decisión aprobada por privacidad con el recorrido completo de los datos.
7. `Solo producción` Ejecuta el Zero Trust Assessment con las comprobaciones de IA. Solo aporta valor sobre la configuración real del inquilino. Cómo hacerlo seguro: cuentas de solo lectura, informe compartido únicamente con el comité de riesgo y brechas mapeadas a las áreas del Workshop ([Zero Trust para IA, agosto de 2026](https://www.microsoft.com/en-us/security/blog/2026/08/04/advance-zero-trust-for-ai-new-tools-and-guidance-to-secure-ai-agents-and-devsecops/)). Evidencia: informe y backlog priorizado.

**¿Quieres profundizar?**

- [Chile: comisión del Senado aprueba en general la ley de IA (La Tribuna)](https://www.latribuna.cl/politica/2026/11/04/chile-avanza-hacia-una-ley-que-podria-prohibir-usos-de-la-inteligencia-artificial-y-aplicar-multas-millonarias.html) · Blog
- [Chile regula agentes de IA: identidad y trazabilidad (Boletín 18.820-19)](https://prensamercosur.org/2026/11/05/chile-chile-regula-agentes-de-ia-identidad-y-trazabilidad/) · Blog

<a id="o2"></a>

## O2 · Modelo operativo y ciclo de vida de los agentes: RACI entre plataforma, desarrollo, datos y seguridad

*L300–L400 · ~5 h · Origen: Nuevo en esta edición (base: personas del Well-Architected para IA, AI Defense Capabilities, Foundry Control Plane y gobernanza de Entra Agent ID)*

La infografía muestra «Lifecycle & version management» en la **Capa 2 · Despliegue y gobierno**, pero no dice quién lo ejecuta. Este módulo asegura esa capa con un modelo operativo. No existe un RACI oficial de Microsoft para agentes de Foundry: el de este módulo se deriva de las **personas del Well-Architected** (de 5 a 10 personas humanas y agénticas mapeadas a componentes, procesos y RBAC), del reparto de dueños de **AI Defense Capabilities** (arquitectura, ingeniería, SecOps y riesgo) y de la responsabilidad compartida: en PaaS, las instrucciones, las herramientas, la orquestación, la memoria y la identidad del agente son del cliente, y la autonomía nunca reduce esa responsabilidad.

El ciclo de vida se opera en el **Foundry Control Plane** (vista previa): inventario con estado, versión, publicación, costo estimado e ID de Entra; Reader observa y Contributor detiene o bloquea. En Entra, cada blueprint exige un **sponsor** y conviene un owner técnico; publicar requiere al menos Foundry Project Manager. La recertificación automática con políticas de ciclo de vida de ID Governance exige Microsoft 365 E7 o Agent 365, así que dentro del alcance la sustituyen el sponsor obligatorio, la revisión periódica del inventario y el bloqueo de blueprints. Los retiros de la plataforma también son parte del ciclo. Se profundiza en el programa de Entra, módulo X4, y en el de Defender for Cloud, módulo O1.

**Por qué importa**

La mayoría de las fallas de gobierno son de dueño: agentes sin sponsor, permisos que nadie revoca, modelos que se retiran sin aviso y costos sin responsable. Un RACI explícito, compuertas de ciclo de vida y roles mínimos para detener un agente deciden quién aprueba, quién puede apagarlo a las tres de la mañana y quién responde ante el comité.

**Qué vas a lograr**

- Adaptar el RACI de referencia a tu organización con una sola «A» por actividad.
- Definir las compuertas del ciclo de vida: registro, construcción, prueba, publicación, operación, recertificación y retiro.
- Operar el inventario y los controles de inicio, detención y bloqueo del Foundry Control Plane con roles mínimos.
- Exigir sponsor y owner en los blueprints y planificar la recertificación sin Agent 365.
- Mapear las personas del Well-Architected a componentes, procesos y RBAC por entorno.

> **Atención.** No existe un RACI oficial de Microsoft para agentes de Foundry: la tabla de este módulo se deriva de las personas del Well-Architected, del reparto de dueños de AI Defense Capabilities y de los roles del Foundry Control Plane y de Entra Agent ID. Adáptala a tu organización con una sola «A» por actividad ([personas](https://learn.microsoft.com/en-us/azure/well-architected/ai/personas), [AI Defense Capabilities](https://learn.microsoft.com/en-us/security/zero-trust/catalog-ai-defense-capabilities/catalog-ai-defense-capabilities)).

> **Atención.** Frontera de licencias en el ciclo de vida: las políticas de ciclo de vida de identidades de agente (vista previa), los paquetes de acceso para agentes y los flujos que transfieren el sponsorship cuando alguien cambia de rol requieren Microsoft 365 E7 o Agent 365 con Entra ID P1 o Microsoft 365 E3. Dentro del alcance quedan los sponsors y owners obligatorios, la revisión manual del inventario y la deshabilitación de blueprints ([políticas de ciclo de vida](https://learn.microsoft.com/en-us/entra/id-governance/agent-lifecycle-policies), [gobernanza de identidades de agente](https://learn.microsoft.com/en-us/entra/id-governance/agent-id-governance-overview)).

> **Qué cambió.** Retiros que afectan el ciclo de vida: la herramienta Fabric data agent se deprecó el 6 de noviembre de 2026 (la reemplaza Fabric IQ), los workflows de Foundry se retiran el 1 de diciembre de 2026, los agentes clásicos y la Assistants API el 31 de marzo de 2027 y la migración de Prompt Flow vence el 20 de abril de 2027. Agéndalos en tu calendario de recertificación ([Fabric](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/fabric), [disponibilidad general](https://learn.microsoft.com/en-us/azure/foundry/concepts/general-availability), [migración de agentes clásicos](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/migrate), [novedades de marzo](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-mar-2026/)).

> **Consejo Ninja.** El inventario del Control Plane (vista previa) cubre agentes de Foundry, Azure SRE Agent, agent loops de Logic Apps y agentes personalizados registrados, pero no los de Foundry classic ni los Assistants: inventaríalos aparte. Asigna Reader para observar y reserva Contributor, que puede detener y bloquear, a un grupo pequeño con asignación elegible en PIM; recuerda que PIM no puede hacer elegibles a las identidades administradas ([gestionar agentes](https://learn.microsoft.com/en-us/azure/foundry/control-plane/how-to-manage-agents), [PIM para roles de Azure](https://learn.microsoft.com/en-us/azure/role-based-access-control/pim-integration)).

**¿Tienes poco tiempo?**

- [Manage agents at scale in Microsoft Foundry Control Plane](https://learn.microsoft.com/en-us/azure/foundry/control-plane/how-to-manage-agents) · Documentación
- [Workload team personas for AI workloads](https://learn.microsoft.com/en-us/azure/well-architected/ai/personas) · Documentación
- [Best practices for Microsoft Entra Agent ID](https://learn.microsoft.com/en-us/entra/agent-id/best-practices-agent-id) · Documentación
- [Why Enterprises Need a Control Plane for AI Agents](https://www.microsoft.com/en-us/security/security-insider/emerging-trends/agent-control-plane) · Video

**RACI de agentes de IA en Azure**

| Actividad | Plataforma de IA | Desarrollo | Datos | Seguridad y SOC | Identidad | Riesgo y cumplimiento | FinOps | Sponsor del agente | Fuente |
|---|---|---|---|---|---|---|---|---|---|
| Registro y aprobación del agente (propósito, datos, herramientas, sponsor, owner y clasificación de riesgo) | C | R | C | C | C | A | I | R | [Zero Trust Workshop de IA](https://learn.microsoft.com/en-us/security/zero-trust/workshop-zero-trust-ai-security) |
| Modelos aprobados y guardrails mínimos con Azure Policy | A/R | C | I | C | I | C | I | I | [Gobierno de PaaS para IA](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai/platform/governance) |
| Red privada, perímetro y egreso (private endpoints, WAF, DDoS y firewall) | A/R | C | I | C | I | I | C | I | [Baseline de Foundry](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/architecture/baseline-microsoft-foundry-chat) |
| AI gateway: autenticación, límites de tokens, seguridad de contenido y registro | A/R | C | I | C | C | I | C | I | [AI gateway en Foundry](https://learn.microsoft.com/en-us/azure/foundry/configuration/enable-ai-api-management-gateway-portal) |
| Identidad del agente, RBAC mínimo y delegación OBO | C | R | C | C | A | I | I | I | [Buenas prácticas de Agent ID](https://learn.microsoft.com/en-us/entra/agent-id/best-practices-agent-id) |
| Herramientas y servidores MCP: registro privado, allowed_tools y aprobación humana | A | R | C | C | C | I | I | I | [Herramienta MCP](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/model-context-protocol) |
| Evaluaciones y red teaming antes de publicar | C | R | C | A | I | C | I | I | [AI Red Teaming Agent](https://learn.microsoft.com/en-us/azure/foundry/concepts/ai-red-teaming-agent) |
| Publicación en Microsoft 365 o Teams | C | R | C | C | I | C | I | A | [Publicar agentes](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/publish-copilot) |
| Observabilidad y protección del contenido de las trazas | R | R | A | C | I | C | I | I | [Contenido sensible en trazas](https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/traces-sensitive-content) |
| Purview para Foundry (auditoría, DSPM y políticas) | R | C | A | C | I | C | C | I | [Cumplimiento y seguridad en Foundry](https://learn.microsoft.com/en-us/azure/foundry/control-plane/how-to-manage-compliance-security) |
| Defender for AI Services y AI-SPM | R | I | I | A | I | I | C | I | [Activar AI services](https://learn.microsoft.com/en-us/azure/defender-for-cloud/ai-onboarding) |
| Detección y respuesta (reglas, playbooks y contención) | C | C | C | A/R | R | I | I | I | [Respuesta a incidentes en sistemas de IA](https://learn.microsoft.com/en-us/security/zero-trust/sfi/incident-response-ai-systems) |
| Ciclo de vida: versionar, detener, bloquear y retirar | A/R | R | I | C | C | I | I | C | [Gestionar agentes](https://learn.microsoft.com/en-us/azure/foundry/control-plane/how-to-manage-agents) |
| Recertificación (sponsor, uso, permisos e inactividad) | C | R | I | C | A | C | I | R | [Políticas de ciclo de vida](https://learn.microsoft.com/en-us/entra/id-governance/agent-lifecycle-policies) |
| Cuotas, límites de tokens, presupuestos y chargeback | R | C | I | C | I | I | A | C | [Costos de Foundry](https://learn.microsoft.com/en-us/azure/foundry/concepts/manage-costs) |
| Cadena de suministro: AI BOM, escaneo de modelos y dependencias | R | R | I | A | I | C | I | I | [MCSB v2 para IA](https://learn.microsoft.com/en-us/security/benchmark/azure/mcsb-v2-artificial-intelligence-security) |
| Evaluación regulatoria y de marcos (MCSA, UE e ISO/IEC 42001) | C | C | C | C | I | A/R | I | C | [ISO/IEC 42001](https://learn.microsoft.com/en-us/compliance/regulatory/offering-iso-42001) |
| Excepciones a las políticas y aceptación del riesgo residual | C | C | C | C | C | A | I | R | [Gobierno de la IA (CAF)](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai/govern) |

R: ejecuta · A: rinde cuentas (una sola por actividad) · C: consultado · I: informado. RACI ilustrativo: no existe un RACI oficial de Microsoft para agentes de Foundry; se deriva de las [personas del Well-Architected](https://learn.microsoft.com/en-us/azure/well-architected/ai/personas), del reparto de dueños de [AI Defense Capabilities](https://learn.microsoft.com/en-us/security/zero-trust/catalog-ai-defense-capabilities/catalog-ai-defense-capabilities) y de los roles del Foundry Control Plane y de Entra Agent ID. Adáptalo a tu organización.

**Compuertas del ciclo de vida de un agente de Foundry**

| Etapa | Control | Herramienta | Evidencia | Responsable |
|---|---|---|---|---|
| Registro | Solicitud con propósito, datos, herramientas, sponsor y owner; clasificación de riesgo | Área «Register agents» del Zero Trust Workshop y formulario interno | Solicitud aprobada | Sponsor y riesgo |
| Construcción | Agente como código: instrucciones, herramientas, guardrail y versión del modelo en un repositorio | Agent Framework, Bicep y Azure Policy | Pull request revisado | Desarrollo |
| Identidad | Blueprint con sponsor y owner; identidad sin permisos iniciales; RBAC mínimo por recurso | Entra Agent ID y Azure RBAC por GUID | Asignaciones revisadas | Identidad |
| Prueba | Evaluadores de riesgo y red teaming con un umbral para publicar | ai-agent-evals y AI Red Teaming Agent | Scorecard con la tasa de éxito de ataque | Seguridad y desarrollo |
| Publicación | Rol mínimo Foundry Project Manager; audiencia acotada en Microsoft 365 o Teams | Portal de Foundry | Agente publicado para el grupo piloto | Sponsor |
| Operación | Trazas sin contenido, alertas, límites de tokens y costos | Agent Monitoring Dashboard, API Management, Sentinel y Cost Management | Tablero mensual | Plataforma y SOC |
| Recertificación | Revisión periódica de sponsor, uso, permisos e inactividad | Inventario exportado del Control Plane (las políticas automáticas exigen Agent 365) | Acta de recertificación | Identidad y sponsor |
| Retiro | Bloqueo, exportación de evidencias, deshabilitación del blueprint y eliminación; retiros de plataforma agendados | Foundry Control Plane (Contributor) y Entra | Registro de retiro firmado | Plataforma |

Fuentes: [gestionar agentes](https://learn.microsoft.com/en-us/azure/foundry/control-plane/how-to-manage-agents), [roles de Foundry](https://learn.microsoft.com/en-us/azure/foundry/concepts/rbac-foundry), [crear un blueprint](https://learn.microsoft.com/en-us/entra/agent-id/create-blueprint) y [Zero Trust Workshop de IA](https://learn.microsoft.com/en-us/security/zero-trust/workshop-zero-trust-ai-security).

### Documentación, cursos y credenciales

- [Agent identity concepts in Microsoft Foundry](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/agent-identity) · Documentación · Oficial · Nuevo · Microsoft Learn · 28 oct 2026. Explica blueprints e identidades de agente de Entra en Foundry: credencial federada sin secretos, intercambio de tokens en cuatro pasos, acceso solo-aplicación vs delegado (OBO), herramientas soportadas y auditoría en los registros de Entra.
- [What is Microsoft Entra Agent ID?](https://learn.microsoft.com/en-us/entra/agent-id/what-is-microsoft-entra-agent-id) · Documentación · Oficial · Nuevo · Microsoft Learn · 24 jun 2026. Presenta Agent ID como plataforma de identidad para agentes (blueprints, OAuth 2.0, MCP y A2A) disponible para todos los clientes de Entra, y aclara que extender las funciones de seguridad de Entra a los agentes requiere Agent 365.
- [Govern Azure platform services (PaaS) for AI (Cloud Adoption Framework)](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai/platform/governance) · Documentación · Oficial · Microsoft Learn · Cloud Adoption Framework. Prácticas concretas de gobierno de plataforma: Azure Policy integradas para Foundry, Foundry Tools y AI Search, inventario de agentes con Entra Agent ID, restricción de modelos, políticas de guardrails, cuotas, costos y gateway de IA.
- [Manage agents at scale in Microsoft Foundry Control Plane](https://learn.microsoft.com/en-us/azure/foundry/control-plane/how-to-manage-agents) · Documentación · Oficial · Microsoft Learn. Inventario de agentes por suscripción (Operate > Assets > Agents) con estado, versión, publicación, costo estimado y Agent ID, y operaciones de ciclo de vida iniciar, detener y bloquear según rol.
- [Workload team personas for AI workloads](https://learn.microsoft.com/en-us/azure/well-architected/ai/personas) · Documentación · Oficial · Microsoft Learn. Guía del Well-Architected para definir personas humanas y agénticas (científico de datos GenAI, desarrollador, MLOps, monitoreo) con acceso a componentes y responsabilidades: base para un RACI.
- [Governing Agent Identities - Microsoft Entra ID Governance](https://learn.microsoft.com/en-us/entra/id-governance/agent-id-governance-overview) · Documentación · Oficial · Microsoft Learn. Cómo gobernar identidades de agente con ID Governance (asignación de acceso, sponsors, delegación); en Foundry, el primer agente de un proyecto usa un blueprint y una identidad por defecto compartidos por el proyecto, y publicar un agente crea un blueprint y una identidad dedicados.
- [Entra Agent ID lifecycle policies (preview)](https://learn.microsoft.com/en-us/entra/id-governance/agent-lifecycle-policies) · Documentación · Oficial · Vista previa · Microsoft Learn. Políticas de ciclo de vida para identidades de agente: reconfirmación periódica (30 a 730 días), mínimo de sponsors e inactividad (sin tokens emitidos), con acciones, periodo de gracia y destinatarios de respaldo. *Nota:* Licencia E7, o Agent 365 + Entra ID P1/M365 E3; roles Lifecycle Workflows Administrator o AI Administrator. Base para la recertificación del módulo O2
- [Agent identity blueprints in Microsoft Entra Agent ID](https://learn.microsoft.com/en-us/entra/agent-id/agent-blueprint) · Documentación · Oficial · Microsoft Learn. Explica el blueprint como plantilla y contenedor de credenciales de las identidades de agente; deshabilitarlo impide autenticarse a todas sus identidades y permite aplicar acceso condicional por clase de agente.
- [Best practices for Microsoft Entra Agent ID](https://learn.microsoft.com/en-us/entra/agent-id/best-practices-agent-id) · Documentación · Oficial · Microsoft Learn. Prácticas operativas: una identidad por instancia, sponsor y owner obligatorios, metadatos descriptivos, políticas a nivel de blueprint, credenciales federadas en producción y guardrails para asistentes de código que crean apps.
- [Create an agent identity blueprint](https://learn.microsoft.com/en-us/entra/agent-id/create-blueprint) · Documentación · Oficial · Microsoft Learn. Creación de blueprints de identidad de agente desde el centro de administración de Entra o Graph/PowerShell, con sponsor obligatorio y owner recomendado, roles Agent ID Developer y Agent ID Administrator.
- [Agent 365 identity](https://learn.microsoft.com/en-us/microsoft-agent-365/developer/identity) · Documentación · Oficial · Microsoft Learn. Modelo de identidad de Agent ID: blueprint (credenciales y permisos heredables), identidad de agente (single-tenant) y cuenta de usuario opcional; modos S2S, OBO y agente-usuario; las identidades no usan MFA y se gobiernan con acceso condicional.
- [What's new in Microsoft Entra Agent ID](https://learn.microsoft.com/en-us/entra/agent-id/whats-new-agent-id) · Documentación · Oficial · Microsoft Learn. Novedades de Agent ID (GA): paquetes de acceso para agentes (OBO y autónomos), flujos de ciclo de vida de sponsors, transferencia de sponsorship y plantillas de acceso condicional (bloquear agentes de alto riesgo, agentes autónomos, OBO).

### Webinars, videos y podcasts

- [Why Enterprises Need a Control Plane for AI Agents](https://www.microsoft.com/en-us/security/security-insider/emerging-trends/agent-control-plane) · Video · Empleado de Microsoft · Irina Mechaeva · Microsoft Security Insider · 4 mar 2026. Conversación sobre la proliferación de agentes: inventario, identidad propia por agente, patrocinador humano responsable, observabilidad de relaciones y Zero Trust para agentes.

### Comunidad: blogs, libros, newsletters y eventos

- [Forbidden by the Spec, Documented by Microsoft: Agent Identity for a Custom MCP Tool in Foundry](https://m365xazure.de/) · Blog · MVP · Nuevo · Andreas Rogge · M365 x Azure · 9 ago 2026. Caso práctico que muestra qué identidad (proyecto o agente) realiza realmente la llamada a una herramienta MCP personalizada en Foundry y cómo depurar un 403.

**Manos a la obra**

1. `Laboratorio` Adapta el RACI de este módulo a tu organización: reemplaza los roles genéricos por equipos reales, deja una sola «A» por actividad y valídalo en un taller con plataforma, desarrollo, datos, seguridad, identidad, riesgo y FinOps ([personas del Well-Architected](https://learn.microsoft.com/en-us/azure/well-architected/ai/personas)). Evidencia: RACI aprobado y acta del taller.
2. `Laboratorio` Exporta el inventario de agentes del Foundry Control Plane, completa sponsor y owner de cada agente, define los estados (registrado, aprobado, publicado, recertificado y retirado) y asigna cada persona del Well-Architected a componentes, procesos y RBAC por entorno ([gestionar agentes](https://learn.microsoft.com/en-us/azure/foundry/control-plane/how-to-manage-agents), [personas](https://learn.microsoft.com/en-us/azure/well-architected/ai/personas)). Evidencia: inventario con dueños y estados.
3. `Laboratorio` Asigna Reader al equipo de gobierno y Contributor, como rol elegible en PIM, a dos operadores; verifica que Reader no puede detener ni bloquear un agente y que Contributor sí, tras activar el rol ([gestionar agentes](https://learn.microsoft.com/en-us/azure/foundry/control-plane/how-to-manage-agents), [PIM para roles de Azure](https://learn.microsoft.com/en-us/azure/role-based-access-control/pim-integration)). Evidencia: asignaciones y el intento fallido registrado.
4. `Laboratorio` Configura sponsor (un grupo) y owner en el blueprint del agente de laboratorio y revisa qué roles de Agent ID permiten crear o administrar identidades ([crear un blueprint](https://learn.microsoft.com/en-us/entra/agent-id/create-blueprint), [buenas prácticas](https://learn.microsoft.com/en-us/entra/agent-id/best-practices-agent-id)). Evidencia: propiedades del blueprint y lista de titulares de los roles.
5. `Laboratorio` Convierte las compuertas en código: definición del agente (instrucciones, herramientas, guardrail y versión de modelo) en un repositorio, pull request con revisión obligatoria y la compuerta de evaluación de [A1](03_Nivel_3_Avanzado.md#a1); la publicación queda en manos de quien tiene Foundry Project Manager ([roles de Foundry](https://learn.microsoft.com/en-us/azure/foundry/concepts/rbac-foundry)). Evidencia: pull request con las comprobaciones y la publicación registrada.
6. `Laboratorio parcial` Diseña la recertificación: si el inquilino es elegible, crea una política de ciclo de vida con reconfirmación periódica, mínimo de un sponsor e inactividad, con un destinatario de respaldo; si no, arma la revisión trimestral manual con el inventario y los inicios de sesión de las identidades de agente ([políticas de ciclo de vida](https://learn.microsoft.com/en-us/entra/id-governance/agent-lifecycle-policies)). Limitación: la política requiere Microsoft 365 E7 o Agent 365 con Entra ID P1. Evidencia: política en modo de notificación o informe manual de recertificación.
7. `Solo producción` Retira un agente real de bajo riesgo de punta a punta. Requiere un agente en uso y su sponsor. Cómo hacerlo seguro: anuncio previo, bloqueo en el Control Plane, exportación de evidencias, deshabilitación del blueprint, observación de una semana y recién entonces eliminación, con la firma del sponsor ([gestionar agentes](https://learn.microsoft.com/en-us/azure/foundry/control-plane/how-to-manage-agents)). Evidencia: registro de retiro firmado.

<a id="o3"></a>

## O3 · Costos y abuso de recursos: FinOps de IA, denial of wallet y LLMjacking

*L300–L400 · ~4 h · Origen: Nuevo en esta edición (base: OWASP LLM10:2025, el caso Storm-2139 de la Digital Crimes Unit, políticas de tokens de API Management y laboratorios FinOps de AI-Gateway)*

La amenaza «uso excesivo de recursos» de la infografía apunta a la **Capa 5 · Control de tráfico** y a la detección de la **Capa 6.5 · Defender for AI**: este módulo asegura ambas. OWASP la llama **LLM10 Unbounded Consumption** (denegación de servicio, *denial of wallet* y extracción de modelos) y MITRE ATLAS sumó en marzo de 2026 subtécnicas de *Cost Harvesting*. El **LLMjacking** es real: en el caso Storm-2139, Microsoft demandó en diciembre de 2024 a una red que usaba credenciales de clientes expuestas para revender el acceso a servicios como Azure OpenAI, y en febrero de 2025 nombró a cuatro desarrolladores. La prevención es de diseño: autenticación sin claves, porque una API key evita el acceso condicional.

Foundry Agent Service no impone límites de tasa propios: viven en la cuota del despliegue y en API Management, donde `llm-token-limit` fija tokens por minuto (429) y cuotas por periodo (403) por suscripción, IP o identidad, y `llm-emit-token-metric` alimenta el *chargeback*. Defender for AI Services detecta el denial of wallet con `DOWVolumeAnomaly` y `DOWDuplicateRequests`. Cost Management aporta presupuestos y exportaciones, pero sus alertas avisan sin detener nada: el laboratorio FinOps de AI-Gateway suspende la suscripción que supera su cuota de costo. Los hosted agents aún no tienen tarifa publicada. Se profundiza en [M4](02_Nivel_2_Intermedio.md#m4) y [M7](02_Nivel_2_Intermedio.md#m7).

**Por qué importa**

Una clave expuesta o un agente en bucle pueden consumir el presupuesto del mes en horas y convertirse en un incidente con daño económico y reputacional. Límites por consumidor, presupuestos con alertas, detecciones de denial of wallet y autenticación sin claves hacen del costo una señal de seguridad, y el chargeback entrega a cada equipo la factura que genera.

**Qué vas a lograr**

- Explicar el denial of wallet y el LLMjacking con OWASP LLM10, MITRE ATLAS y el caso Storm-2139.
- Aplicar límites de tokens y cuotas por consumidor con llm-token-limit y medir el consumo para el chargeback.
- Configurar presupuestos, alertas y exportaciones de costos de Foundry.
- Detectar el abuso con las alertas de denial of wallet de Defender y los registros del gateway.
- Automatizar la contención financiera: suspender una suscripción de API Management que supera su cuota de costo.

> **Novedad.** Cronología de Storm-2139: demanda civil presentada el 19 de diciembre de 2024 en el Distrito Este de Virginia, desellada el 10 de enero de 2025 y enmendada el 27 de febrero de 2025 para nombrar a cuatro desarrolladores; el expediente figura como terminado el 9 de julio de 2026, con liberación de la fianza ordenada el 8 de octubre de 2026. Las fuentes oficiales no detallan el resultado y las referencias penales o condenas que mencionan sitios secundarios no están verificadas ([Digital Crimes Unit](https://www.microsoft.com/en-us/corporate-responsibility/customer-security-trust/digital-crimes-unit/notice-of-pleadings/storm-2139/), [expediente](https://www.pacermonitor.com/public/case/56471380/Microsoft_Corporation_v_Does_410_Operating_an_Azure_Abuse_Network)).

> **Atención.** Los hosted agents están en disponibilidad general desde el 9 de julio de 2026, pero la página de precios aún muestra N/A para vCPU-hora y GiB-hora: no los presupuestes con tarifas de blogs de socios ni los dejes encendidos sin control. Tampoco hay un dato publicado sobre si los guardrails predeterminados generan cargos de Content Safety ([precios de Agent Service](https://azure.microsoft.com/en-us/pricing/details/foundry-agent-service/), [precios de Content Safety](https://azure.microsoft.com/en-us/pricing/details/content-safety/)).

> **Consejo Ninja.** Diseña bien los contadores: en `llm-token-limit` son por gateway (no se suman entre gateways regionales ni de workspace), con streaming los tokens se estiman y las solicitudes concurrentes pueden superar el límite por un momento. `llm-emit-token-metric` admite hasta 5 dimensiones y descarta en silencio los datos si superas 100 valores por dimensión o 1.000 series ([llm-token-limit](https://learn.microsoft.com/en-us/azure/api-management/llm-token-limit-policy), [llm-emit-token-metric](https://learn.microsoft.com/en-us/azure/api-management/llm-emit-token-metric-policy)).

> **Atención.** Los datos de costo de Foundry llegan con retraso, la atribución de costos por proyecto está en vista previa y las alertas de presupuesto avisan, pero no detienen recursos. Para contener el gasto necesitas automatización, como la suspensión de suscripciones de API Management del laboratorio FinOps de AI-Gateway ([costos de Foundry](https://learn.microsoft.com/en-us/azure/foundry/concepts/manage-costs), [laboratorio FinOps](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/finops-framework)).

**¿Tienes poco tiempo?**

- [Disrupting a global cybercrime network abusing generative AI](https://blogs.microsoft.com/on-the-issues/2025/02/27/disrupting-cybercrime-abusing-gen-ai/) · Blog oficial
- [OWASP LLM10:2025 Unbounded Consumption](https://genai.owasp.org/llmrisk/llm102025-unbounded-consumption/) · Documentación
- [Azure API Management policy reference - llm-token-limit](https://learn.microsoft.com/en-us/azure/api-management/llm-token-limit-policy) · Documentación
- [AI-Gateway lab: FinOps Framework](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/finops-framework) · Laboratorio

**Abuso de recursos: señales y palancas**

| Riesgo | Prevenir | Detectar | Contener | Referencia de costo | Fuente |
|---|---|---|---|---|---|
| LLMjacking con una clave filtrada | Autenticación sin claves (`disableLocalAuth`), Key Vault y ninguna clave en repositorios | AnonymizedIP, SuspiciousIP y AccessAnomaly; `listKeys` en `AzureActivity` | Deshabilitar la autenticación local, verificar el 401 y regenerar claves | Tokens del modelo a precio de lista | [Deshabilitar la autenticación local](https://learn.microsoft.com/en-us/azure/ai-services/disable-local-auth) |
| Denial of wallet por volumen | `llm-token-limit` por consumidor (429 y 403) | `AI.Azure_DOWVolumeAnomaly`; tokens por suscripción en `ApiManagementGatewayLlmLog` | Bajar los TPM o suspender la suscripción de API Management | Defender for AI Services: USD 0,0008 por 1.000 tokens | [llm-token-limit](https://learn.microsoft.com/en-us/azure/api-management/llm-token-limit-policy) |
| Solicitudes duplicadas | Caché semántica particionada con `vary-by` y timeouts | `AI.Azure_DOWDuplicateRequests` | Bloquear o limitar al consumidor | — | [Caché semántica](https://learn.microsoft.com/en-us/azure/api-management/llm-semantic-cache-lookup-policy) |
| Agente en bucle | Presupuesto de pasos y de herramientas por sesión; interruptor de apagado | Spans `execute_tool` repetidos en las trazas | Detener el agente en el Foundry Control Plane | Code Interpreter: USD 0,033 por sesión | [Precios de Agent Service](https://azure.microsoft.com/en-us/pricing/details/foundry-agent-service/) |
| Consumo agéntico de recursos (Cost Harvesting) | Límites de tokens por proyecto en el AI gateway de Foundry | Métricas de tokens por proyecto | Cuota por proyecto (403) | Basic v2 gratis hasta 100.000 solicitudes como AI gateway | [Límites por proyecto](https://learn.microsoft.com/en-us/azure/foundry/control-plane/how-to-enforce-limits-models) |
| Evaluaciones y escaneos sin control | Muestras pequeñas y presupuestos por grupo de recursos | Cost Management por medidor | Pausar evaluaciones recurrentes y escaneos programados | USD 20 y 60 por 1M de tokens de entrada y salida | [Precios de observabilidad](https://azure.microsoft.com/en-us/pricing/details/foundryobservability/) |
| Recursos de red olvidados | Etiqueta de expiración y sesiones de tiempo acotado | Consulta de recursos por etiqueta al cierre | Borrar el grupo de recursos | WAF v2: USD 0,443 por hora; Firewall Basic: USD 0,395 por hora | [Precios de Application Gateway](https://azure.microsoft.com/en-us/pricing/details/application-gateway/) |
| Costo sin dueño | Etiquetas, atribución por proyecto (vista previa) y chargeback con `llm-emit-token-metric` | Exportaciones de Cost Management | Presupuesto con alertas al 50, 75 y 90 % | — | [Costos de Foundry](https://learn.microsoft.com/en-us/azure/foundry/concepts/manage-costs) |
| Gateway de IA comprometido | Parches y control de acceso del gateway; claves de proveedores fuera de su alcance | Robo de claves de proveedores de modelos y minado de criptomonedas | Rotar las claves de los proveedores y aislar el gateway | — | [Ataques a gateways de IA](https://www.microsoft.com/en-us/security/blog/2026/08/26/when-ai-infrastructure-becomes-target-securing-gateways-control-points/) |
| Seguridad de contenido a escala | Elegir qué controles aplicar en el gateway y en Foundry | Registros de texto procesados | Ajustar los controles por API o producto | USD 0,38 por 1.000 registros de texto (5.000 gratis al mes) | [Precios de Content Safety](https://azure.microsoft.com/en-us/pricing/details/content-safety/) |

Precios de lista en USD al 7 de noviembre de 2026; cambian y no incluyen impuestos. La tabla de costos completa de la arquitectura está en el bloque de costos de referencia del programa. Taxonomía del riesgo: [OWASP LLM10](https://genai.owasp.org/llmrisk/llm102025-unbounded-consumption/) y [Cost Harvesting en MITRE ATLAS](https://github.com/mitre-atlas/atlas-website/blob/main/public/content/update-files/2026-03.md).

### Documentación, cursos y credenciales

- [Disable local authentication in Foundry Tools](https://learn.microsoft.com/en-us/azure/ai-services/disable-local-auth) · Documentación · Oficial · Nuevo · Microsoft Learn · 2 jun 2026. Cómo forzar Entra ID deshabilitando las claves (política integrada, propiedad disableLocalAuth en Bicep/ARM o PowerShell) y cómo verificar que una clave antigua ya devuelve 401.
- [Azure API Management policy reference - llm-token-limit](https://learn.microsoft.com/en-us/azure/api-management/llm-token-limit-policy) · Documentación · Oficial · Nuevo · Microsoft Learn · 5 may 2026. Referencia de la política que limita tokens por minuto y/o cuotas por hora, día, semana, mes o año con una clave de conteo (suscripción, IP o expresión), devolviendo 429 o 403 al excederse.
- [Plan and manage costs for Microsoft Foundry](https://learn.microsoft.com/en-us/azure/foundry/concepts/manage-costs) · Documentación · Oficial · Microsoft Learn. Cómo estimar con la calculadora (Foundry no tiene página propia), validar el plan con tráfico de prueba agrupando por recurso y medidor, crear presupuestos y alertas, exportar costos y atribuir costos por proyecto.
- [Microsoft Defender for Cloud pricing](https://azure.microsoft.com/en-us/pricing/details/defender-for-cloud/) · Documentación · Oficial · Microsoft Azure. Precios de lista de Defender for Cloud: Defender for APIs en cinco planes por suscripción (de USD 200,02/mes hasta 1 M de llamadas a USD 50.000,04/mes hasta 1.000 M) con sobrecargo por llamada, y Defender for AI Services a USD 0,0008 por 1.000 tokens.
- [OWASP LLM10:2025 Unbounded Consumption](https://genai.owasp.org/llmrisk/llm102025-unbounded-consumption/) · Documentación · Comunidad · OWASP Top 10 for LLM team · OWASP Gen AI Security Project · 18 nov 2024. Define el consumo no acotado (DoS, denial of wallet, extracción de modelos) y mitigaciones: validación de entradas, rate limiting y cuotas por usuario, timeouts, monitoreo de anomalías y controles de acceso.
- [Storm-2139 (FizzDogg) - Microsoft Digital Crimes Unit notice of pleadings](https://www.microsoft.com/en-us/corporate-responsibility/customer-security-trust/digital-crimes-unit/notice-of-pleadings/storm-2139/) · Documentación · Oficial · Microsoft Digital Crimes Unit · 25 feb 2025. Página oficial de notificación del caso civil 1:24-cv-2323 (EDVA) contra los demandados de la «Azure Abuse Network», con la demanda, la enmienda y las órdenes de restricción.
- [Microsoft Corporation v. Does 4-10 Operating an Azure Abuse Network (1:24-cv-02323)](https://www.pacermonitor.com/public/case/56471380/Microsoft_Corporation_v_Does_410_Operating_an_Azure_Abuse_Network) · Documentación · Comunidad · Nuevo · PacerMonitor · 8 oct 2026. Ficha del expediente del caso Storm-2139: presentado el 19-dic-2024, terminado el 9-jul-2026 y con liberación de la fianza de Microsoft ordenada el 8-oct-2026.

### Anuncios y blogs oficiales

- [When AI infrastructure becomes the target: Securing gateways and control points](https://www.microsoft.com/en-us/security/blog/2026/08/26/when-ai-infrastructure-becomes-target-securing-gateways-control-points/) · Blog oficial · Empleado de Microsoft · Nuevo · Microsoft Security Research (Yash Gund, Sumith Maniath) · Microsoft Security Blog · 26 ago 2026. Investigación de intrusiones reales contra un gateway LiteLLM, RAGFlow y Kestra para robar llaves de proveedores de modelos, persistir y minar criptomonedas, con guía de mitigación.
- [Disrupting a global cybercrime network abusing generative AI](https://blogs.microsoft.com/on-the-issues/2025/02/27/disrupting-cybercrime-abusing-gen-ai/) · Blog oficial · Empleado de Microsoft · Steven Masada · Microsoft On the Issues · 27 feb 2025. La Digital Crimes Unit nombra en una demanda enmendada a cuatro desarrolladores de Storm-2139 que usaron credenciales de clientes expuestas para acceder a servicios de IA generativa, alterar sus capacidades y revender el acceso.
- [Taking legal action to protect the public from abusive AI-generated content](https://blogs.microsoft.com/on-the-issues/2025/01/10/taking-legal-action-to-protect-the-public-from-abusive-ai-generated-content/) · Blog oficial · Empleado de Microsoft · Steven Masada · Microsoft On the Issues · 10 ene 2025. Anuncio del desellado de la demanda de la DCU: un grupo extranjero usó credenciales de clientes extraídas de sitios públicos para abusar de servicios de IA; Microsoft revocó el acceso y reforzó salvaguardas.

### Laboratorios, GitHub y herramientas

- [AI-Gateway lab: FinOps Framework](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/finops-framework) · Laboratorio · Empleado de Microsoft · Nuevo · vieiraae (Alex Vieira) y colaboradores · GitHub Azure-Samples/AI-Gateway · sep 2026. Laboratorio de FinOps para IA: límites de tokens por producto de APIM, alertas de Azure Monitor y Logic Apps que suspenden automáticamente suscripciones que superan su cuota de costo.
- [AI-Gateway lab: Token Rate Limiting](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/token-rate-limiting) · Laboratorio · Empleado de Microsoft · Nuevo · vieiraae (Alex Vieira) y colaboradores · GitHub Azure-Samples/AI-Gateway · jun 2026. Laboratorio con Bicep y notebook para aplicar límites de tokens por minuto en APIM frente a endpoints de Foundry y observar respuestas 429.
- [Azure AI Governance - Cost Governance / FinOps for AI Lab 01: Token Rate Limiting (Managed Identity)](https://github.com/Azure/AzureAIGovernance/blob/main/Cost%20GovernanceFinOpsforAI/Labs/Lab-01-Token-Rate-Limiting-managed-identity.md) · Laboratorio · Empleado de Microsoft · Nuevo · sujithre y colaboradores · GitHub Azure/AzureAIGovernance · jul 2026. Laboratorio de 45-60 minutos que aplica límites de tokens por equipo en APIM autenticando a Azure OpenAI con identidad administrada (sin API keys).
- [MITRE ATLAS website update March 2026 (Cost Harvesting sub-techniques)](https://github.com/mitre-atlas/atlas-website/blob/main/public/content/update-files/2026-03.md) · GitHub · Comunidad · MITRE ATLAS team · MITRE (GitHub mitre-atlas/atlas-website) · mar 2026. Notas de la versión de datos 5.5.0: nuevas subtécnicas de Cost Harvesting (consultas excesivas, consultas intensivas en recursos y consumo agéntico de recursos) y técnicas de cadena de suministro de herramientas de agentes.

**Manos a la obra**

1. `Laboratorio` Despliega el laboratorio Token Rate Limiting de AI-Gateway (o usa el gateway Basic v2 creado desde Foundry) con dos suscripciones, 500 tokens por minuto y una cuota pequeña, y ejecuta el script de abuso de tokens del anexo de laboratorio: espera 200, luego 429 y, al agotar la cuota, 403 ([laboratorio de límites de tokens](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/token-rate-limiting), [llm-token-limit](https://learn.microsoft.com/en-us/azure/api-management/llm-token-limit-policy)). Evidencia: registro de códigos HTTP y XML de la política.
2. `Laboratorio` Calcula el chargeback del mes con una consulta sobre `ApiManagementGatewayLlmLog` unida por `CorrelationId` a `ApiManagementGatewayLogs`: tokens de entrada y salida por suscripción y su costo con el precio de lista de tu modelo ([ApiManagementGatewayLlmLog](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/apimanagementgatewayllmlog), [registros LLM de API Management](https://learn.microsoft.com/en-ie/azure/api-management/api-management-howto-llm-logs)). Evidencia: consulta guardada y tabla de costo por consumidor.
3. `Laboratorio` Crea en Cost Management un presupuesto para el grupo de recursos de Foundry con alertas al 50, 75 y 90 % y una pronosticada al 100 %, etiquetas por proyecto y una exportación programada de costos ([costos de Foundry](https://learn.microsoft.com/en-us/azure/foundry/concepts/manage-costs)). Evidencia: presupuesto, regla de alertas y primer archivo exportado.
4. `Laboratorio` Ejecuta el laboratorio FinOps de AI-Gateway: supera la cuota de costo de una suscripción de API Management y observa cómo Azure Monitor y Logic Apps la suspenden; borra los recursos al terminar ([laboratorio FinOps](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/finops-framework), [límites con identidad administrada](https://github.com/Azure/AzureAIGovernance/blob/main/Cost%20GovernanceFinOpsforAI/Labs/Lab-01-Token-Rate-Limiting-managed-identity.md)). Evidencia: suscripción en estado suspendido y aviso generado.
5. `Laboratorio parcial` Escribe en Sentinel una regla para las alertas `AI.Azure_DOWVolumeAnomaly` y `AI.Azure_DOWDuplicateRequests` y otra para el consumo anómalo de tokens por suscripción, y prueba la segunda con una ráfaga sintética ([alertas de IA](https://learn.microsoft.com/en-us/azure/defender-for-cloud/alerts-ai-workloads)). Limitación: no puedes garantizar que Defender dispare las alertas de denial of wallet con tráfico de laboratorio. Evidencia: reglas como código y resultado de la ráfaga.
6. `Laboratorio` Audita la exposición al LLMjacking: asigna en modo Audit la política que exige deshabilitar las claves de los recursos de Foundry, lista los recursos que aún aceptan claves y consulta en `AzureActivity` quién ejecutó `listKeys` en los últimos 30 días ([deshabilitar la autenticación local](https://learn.microsoft.com/en-us/azure/ai-services/disable-local-auth), [ataques a gateways de IA](https://www.microsoft.com/en-us/security/blog/2026/08/26/when-ai-infrastructure-becomes-target-securing-gateways-control-points/)). Evidencia: lista de recursos no conformes con su plan de remediación.
7. `Solo producción` Implanta cuotas y chargeback para equipos reales. Requiere consumo real durante al menos un ciclo de facturación. Cómo hacerlo seguro: cuotas generosas al inicio, alerta al 80 %, un mes solo de informe y después aplicación gradual por producto o proyecto ([llm-token-limit](https://learn.microsoft.com/en-us/azure/api-management/llm-token-limit-policy), [límites por proyecto](https://learn.microsoft.com/en-us/azure/foundry/control-plane/how-to-enforce-limits-models)). Evidencia: primer informe mensual de chargeback aprobado por FinOps.

**¿Quieres profundizar?**

- [AI-Gateway lab: Token Rate Limiting](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/token-rate-limiting) · Laboratorio
- [Azure AI Governance - Cost Governance / FinOps for AI Lab 01: Token Rate Limiting (Managed Identity)](https://github.com/Azure/AzureAIGovernance/blob/main/Cost%20GovernanceFinOpsforAI/Labs/Lab-01-Token-Rate-Limiting-managed-identity.md) · Laboratorio
- [MITRE ATLAS website update March 2026 (Cost Harvesting sub-techniques)](https://github.com/mitre-atlas/atlas-website/blob/main/public/content/update-files/2026-03.md) · GitHub

<a id="o4"></a>

## O4 · Proyecto integrador: arquitectura segura para agentes de IA de punta a punta

*L300–L400 · ~6 h · Origen: Nuevo en esta edición (proyecto integrador sobre la infografía corregida, la arquitectura baseline de Foundry y el anexo de laboratorio de Foundry)*

El proyecto integrador cierra el programa y asegura **todas las capas** de la infografía, de la 1 a la 8, con la banda de red y los principios. Eliges un caso de uso real —por ejemplo, un agente de atención a clientes que responde con políticas internas desde Azure AI Search y abre tickets con una herramienta MCP propia— y entregas la arquitectura corregida, con nombres vigentes, desplegada en el laboratorio: Foundry sin claves, Agent Service con red privada, guardrails con ataques indirectos, límites de tokens en API Management, WAF, egreso controlado, Defender for AI Services, auditoría de Purview, informe de red teaming, una regla analítica de Sentinel y un playbook de incidentes, con evidencia por capa.

La red privada del agente se decide al crear el recurso, así que el diseño va primero. Trabajas con las sesiones de tiempo acotado del anexo de laboratorio de Foundry —unos USD 48 del crédito mensual en el perfil completo, según su estimación— y documentas cada decisión: qué está en vista previa, qué exige Agent 365 o Microsoft 365 E7 y cuál es la alternativa, dónde vive cada dato (no hay data zone de Latinoamérica) y qué riesgo residual aceptas. Cierras con un paquete para el comité y una presentación de diez minutos. Microsoft Ignite (17 al 20 de noviembre de 2026) puede cambiar estados de vista previa: revalida antes de presentar.

**Por qué importa**

Saber qué control existe no es lo mismo que demostrarlo. El proyecto integra las 151 horas del programa en un artefacto defendible: una arquitectura que funciona, con evidencia verificable por capa y con sus límites declarados —vista previa, licencias y región—. Es lo que un comité, un auditor o un regulador de MCSA te van a pedir antes de aprobar un agente en producción.

**Qué vas a lograr**

- Diseñar la versión corregida de la arquitectura de la infografía para un caso de uso real de tu organización.
- Desplegarla por capas en el laboratorio, con sesiones de tiempo acotado y costo controlado.
- Reunir evidencia verificable por capa y declarar los riesgos residuales y las fronteras de licencia.
- Ensayar de punta a punta la detección y la respuesta a un incidente de agente.
- Presentar y defender la arquitectura ante un comité con métricas de resultado.

> **Atención.** La red privada del agente se decide al crear el recurso: la salida privada requiere la configuración estándar con tu VNet desde el inicio, no puedes agregar la inyección a un recurso existente ni cambiar la subred, y en hosted agents se define al crear la cuenta. La plantilla 15 admite brazilsouth pero no mexicocentral, y AI Landing Zones no incluye regiones de MCSA para el despliegue completo ([red privada de Foundry](https://learn.microsoft.com/en-us/azure/foundry/how-to/configure-private-link), [VNet del Agent Service](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/virtual-networks), [AI Landing Zones](https://github.com/Azure/AI-Landing-Zones)).

> **Atención.** Varias piezas del proyecto siguen en vista previa al 7 de noviembre de 2026: guardrails de agentes y puntos de intervención en herramientas, Operate del Control Plane, AI gateway desde Foundry, memoria y escaneos de red team programados; la red administrada se crea solo con CLI en vista previa y no se puede desactivar. Márcalas así en tus entregables y revalídalas después de Microsoft Ignite (17 al 20 de noviembre) ([tabla de disponibilidad](https://learn.microsoft.com/en-us/azure/foundry/concepts/general-availability), [red administrada](https://learn.microsoft.com/en-us/azure/foundry/how-to/managed-virtual-network)).

> **Consejo Ninja.** Cinco advertencias de la baseline que debes probar: el contenido del chat genera falsos positivos del WAF (crea exclusiones acotadas al campo de mensajes), la inspección TLS del firewall rompe las conexiones de los agentes, web search no pasa por la subred de egreso, ninguna regla del WAF detecta inyección de prompts y DDoS Protection no cubre los tiers v2 de API Management ([baseline](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/architecture/baseline-microsoft-foundry-chat), [tiers v2](https://learn.microsoft.com/en-us/azure/api-management/v2-service-tiers-overview)).

> **Consejo Ninja.** Limpieza en orden, como indica el anexo de laboratorio de Foundry: elimina y purga la cuenta de Foundry con red privada antes de borrar la VNet (la subred delegada tarda unos 20 minutos en liberarse), recuerda que Application Gateway, Azure Firewall y Private Link cobran la hora parcial como completa y verifica al cierre que no quede ningún recurso con la etiqueta del programa ([precios de Application Gateway](https://azure.microsoft.com/en-us/pricing/details/application-gateway/), [precios de Azure Firewall](https://azure.microsoft.com/en-us/pricing/details/azure-firewall/)).

**¿Tienes poco tiempo?**

- [Baseline Microsoft Foundry chat reference architecture](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/architecture/baseline-microsoft-foundry-chat) · Documentación
- [Azure-Samples/microsoft-foundry-baseline](https://github.com/Azure-Samples/microsoft-foundry-baseline) · GitHub
- [microsoft-foundry/foundry-samples · 15-private-network-standard-agent-setup](https://github.com/microsoft-foundry/foundry-samples/tree/main/infrastructure/infrastructure-setup-bicep/15-private-network-standard-agent-setup) · GitHub
- [Azure/AI-Landing-Zones](https://github.com/Azure/AI-Landing-Zones) · GitHub

**Plan del proyecto integrador por fases y sesiones**

| Fase | Capas | Sesión del anexo de laboratorio | Costo estimado (USD) | Evidencia mínima | Módulos |
|---|---|---|---|---|---|
| 1 · Diseño y amenazas | 1 a 8 | Ninguna | 0 | Diagrama corregido con nombres vigentes y matriz de amenazas | F2, F3 |
| 2 · Base sin claves y gobernada | 3, 4 y 7 | Ninguna (recursos permanentes) | ≈3 al mes en tokens | Respuesta 401 con la clave antigua; guardrail con ataques en documentos; política de modelos en Audit | F4, M3, M7 |
| 3 · Agente con red privada y herramientas | 1, 2 y banda de red | S1 y S2 (4 h cada una) | ≈1,5 por sesión | IP privada en `nslookup`; contenedores en Cosmos DB; aprobaciones de MCP registradas | M1, M2, M5, M6 |
| 4 · Tráfico, perímetro y egreso | 5, 6 y banda de red | S3 (API Management Standard v2), S4 (WAF y DDoS IP Protection) y S5 (Firewall Basic) | ≈4, ≈3,5 y ≈1,5 | 429 y 403 del gateway; registros del WAF en Detección y Prevención; denegaciones del firewall | M4, M5 |
| 5 · Protección y datos | 6.5, 7 y 8 | Pruebas de 30 días de Defender y prueba de Microsoft 365 E5 | 0 durante las pruebas | Alerta con el usuario identificado; recomendaciones de AI-SPM; auditoría de Purview | A3, A4, A2 |
| 6 · Evaluación, detección y respuesta | 4, 6.5 y SOC | S7 (red teaming) y S8 opcional (Security Copilot) | ≈5–10 y ≈12 | ASR antes y después; reglas como código; acta del simulacro con tiempos | A1, A5, A6, A7 |
| 7 · Gobierno y cierre | Transversal | Ninguna | 0 | RACI, compuertas, presupuesto, mapa de marcos y regulación y limpieza verificada | O1, O2, O3 |

Costos estimados por el anexo de laboratorio de Foundry con precios de lista en USD, sin impuestos, al 7 de noviembre de 2026: perfil completo ≈48 USD al mes sin DDoS Network Protection y ≈64 con ella; las horas parciales se cobran completas. Precios de referencia: [API Management](https://azure.microsoft.com/en-us/pricing/details/api-management/), [Application Gateway](https://azure.microsoft.com/en-us/pricing/details/application-gateway/), [Azure Firewall](https://azure.microsoft.com/en-us/pricing/details/azure-firewall/) y [DDoS Protection](https://azure.microsoft.com/en-us/pricing/details/ddos-protection/).

**Manos a la obra**

1. `Laboratorio` Elige el caso de uso y entrega el diagrama corregido con nombres vigentes (Foundry Agent Service, guardrails de Microsoft Foundry, Defender for AI Services, DevOps security de Defender for Cloud, DDoS Network o IP Protection) y su modelo de amenazas con OWASP, ATLAS y la taxonomía de Microsoft ([baseline de Foundry](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/architecture/baseline-microsoft-foundry-chat), [CAAT](https://learn.microsoft.com/en-us/security/zero-trust/catalog-ai-attack-techniques/catalog-ai-attack-techniques)). Evidencia: diagrama y matriz de amenazas revisados por un par.
2. `Laboratorio` Construye la base sin claves y gobernada: Foundry con `disableLocalAuth` (verifica el 401), RBAC por GUID, política de modelos aprobados en Audit y un guardrail con ataques en documentos probado con la batería en español de [A1](03_Nivel_3_Avanzado.md#a1) ([deshabilitar la autenticación local](https://learn.microsoft.com/en-us/azure/ai-services/disable-local-auth), [políticas de modelos](https://learn.microsoft.com/en-us/azure/foundry/how-to/model-deployment-policy)). Evidencia: una prueba por capa (3, 4 y 7) en la tabla de evidencias.
3. `Laboratorio parcial` Despliega el agente con red privada usando la plantilla 15 en East US 2 (sesiones S1 y S2), con una herramienta MCP propia con `allowed_tools` y `require_approval` y la identidad del agente con RBAC mínimo ([plantilla 15](https://github.com/microsoft-foundry/foundry-samples/tree/main/infrastructure/infrastructure-setup-bicep/15-private-network-standard-agent-setup), [VNet del Agent Service](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/virtual-networks)). Limitación: costo por hora, Application Insights fuera del crédito y la plantilla no admite mexicocentral. Evidencia: `nslookup` con IP privada, contenedores en Cosmos DB y registro de aprobaciones.
4. `Laboratorio parcial` Agrega tráfico, perímetro y egreso en sesiones acotadas: API Management con `llm-token-limit` y `llm-content-safety` con `shield-prompt` activado; Application Gateway WAF v2 en Detección y luego en Prevención, con exclusiones para el campo de mensajes y DDoS IP Protection; Azure Firewall Basic con lista de FQDN, comprobando que web search no pasa por él ([AI gateway en Foundry](https://learn.microsoft.com/en-us/azure/foundry/configuration/enable-ai-api-management-gateway-portal), [WAF](https://learn.microsoft.com/en-us/azure/web-application-firewall/ag/ag-overview), [Azure Firewall](https://learn.microsoft.com/en-us/azure/firewall/features-by-sku)). Limitación: recursos caros solo por horas y sin simulaciones de DDoS. Evidencia: 429 y 403, registros del WAF y denegaciones del firewall.
5. `Laboratorio` Activa la protección y los datos: Defender for AI Services con `user_security_context`, la prueba de Defender CSPM, la auditoría de Purview con tokens de usuario (espera un día) y trazas sin contenido ([contexto del usuario final](https://learn.microsoft.com/en-us/azure/defender-for-cloud/gain-end-user-context-ai), [Purview para Foundry](https://learn.microsoft.com/en-us/purview/ai-azure-foundry)). Evidencia: alerta con el usuario identificado, recomendaciones de AI-SPM y registros de auditoría.
6. `Laboratorio parcial` Cierra el ciclo de seguridad: escaneo de red teaming antes y después (sesión S7), reglas de Sentinel para jailbreak, robo de credenciales y abuso de tokens, y un simulacro de LLMjacking o de envenenamiento de herramientas con tiempos medidos ([AI Red Teaming Agent](https://learn.microsoft.com/en-us/azure/foundry/concepts/ai-red-teaming-agent), [respuesta a incidentes en sistemas de IA](https://learn.microsoft.com/en-us/security/zero-trust/sfi/incident-response-ai-systems)). Limitación: categorías agénticas solo en inglés y fuera de MCSA, y Security Copilot opcional con costo por hora. Evidencia: informe de ASR, reglas como código y acta del simulacro.
7. `Laboratorio` Arma el paquete para el comité: tabla de evidencias por capa, fronteras de licencia con su alternativa, riesgos residuales y decisiones de residencia, costos reales de Cost Management, RACI y compuertas de [O2](#o2); termina la limpieza y comprueba que la consulta de recursos con la etiqueta del programa no devuelve nada ([costos de Foundry](https://learn.microsoft.com/en-us/azure/foundry/concepts/manage-costs)). Evidencia: paquete, presentación de diez minutos y captura de la consulta vacía.
8. `Solo producción` Lleva la arquitectura a un agente piloto con usuarios internos. Requiere usuarios, datos y tráfico reales. Cómo hacerlo seguro: políticas primero en Audit, WAF en Detección durante una o dos semanas, firewall con reglas que permiten y registran antes de denegar, Purview solo con auditoría, reglas de Sentinel con severidad informativa y un plan de reversión por capa ([baseline de Foundry](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/architecture/baseline-microsoft-foundry-chat), [implementación de referencia](https://github.com/Azure-Samples/microsoft-foundry-baseline)). Evidencia: aprobación del piloto con criterios de continuidad o reversión.

<a id="reto-operacion"></a>

## Reto del nivel

**Proyecto integrador: la arquitectura segura de la infografía, corregida y desplegada.** Elige un caso de uso real de tu organización (por ejemplo, un agente interno que consulta políticas y abre tickets) y entrégalo en el laboratorio con la arquitectura corregida, capa por capa, según el plan de [O4](#o4). Cada fase deja evidencia verificable en una tabla de evidencias por capa. Trabaja con datos sintéticos, sesiones acotadas y la etiqueta del programa en todos los recursos. El proyecto no depende de Agent 365 ni de E7: donde una capacidad los requiera, documenta la frontera y la alternativa.

**Fase 1 · Diseño y amenazas (capas 1 a 8).** Diagrama de la infografía corregido con los nombres vigentes, el estado (GA o preview) y la licencia de cada control, y la matriz de amenazas del caso con OWASP, MITRE ATLAS y la taxonomía de Microsoft, con un dueño por amenaza ([F2](01_Nivel_1_Inicial.md#f2), [F3](01_Nivel_1_Inicial.md#f3)). Evidencia: diagrama y matriz revisados por un par.

**Fase 2 · Base sin claves y gobernada (capas 3, 4 y 7).** Foundry con `disableLocalAuth` y la prueba del 401 con la clave antigua, RBAC por persona asignado por GUID, política de modelos aprobados en Audit y un guardrail con detección de ataques del usuario y de ataques en documentos ([F4](01_Nivel_1_Inicial.md#f4), [M3](02_Nivel_2_Intermedio.md#m3), [M7](02_Nivel_2_Intermedio.md#m7)). Evidencia: la respuesta 401, las asignaciones de roles exportadas y el bloqueo de una inyección indirecta de prueba.

**Fase 3 · Agente con red privada y herramientas (capas 1 y 2 y banda de red).** Agent Service en configuración estándar con red privada definida desde la creación, recursos propios (Cosmos DB, AI Search y Storage), identidad del agente con RBAC mínimo y una herramienta MCP con `allowed_tools` explícito y aprobación obligatoria ([M1](02_Nivel_2_Intermedio.md#m1), [M2](02_Nivel_2_Intermedio.md#m2), [M5](02_Nivel_2_Intermedio.md#m5), [M6](02_Nivel_2_Intermedio.md#m6)). Evidencia: `nslookup` con IP privada, acceso público deshabilitado y el registro de una aprobación de herramienta.

**Fase 4 · Tráfico, perímetro y egreso (capas 5 y 6 y banda de red).** API Management como AI gateway con `llm-token-limit` por consumidor y `llm-content-safety` con `shield-prompt` activado; Application Gateway WAF v2 en Detección y luego en Prevención, con exclusiones acotadas al campo de mensajes y DDoS IP Protection en su IP pública, y Azure Firewall Basic con lista de FQDN para el egreso de los agentes ([M4](02_Nivel_2_Intermedio.md#m4), [M5](02_Nivel_2_Intermedio.md#m5)). Evidencia: un 429 y un 403 del gateway, los registros del WAF en ambos modos, las denegaciones del firewall y la nota de riesgo sobre web search, que no pasa por él.

**Fase 5 · Protección, datos y evidencia (capas 6.5, 7 y 8).** Defender for AI Services con el contexto del usuario final en las llamadas, recomendaciones de AI-SPM en Defender CSPM, auditoría de Purview de las interacciones con tokens de usuario y trazas del servidor con la tabla AppGenAIContent protegida ([A2](03_Nivel_3_Avanzado.md#a2), [A3](03_Nivel_3_Avanzado.md#a3), [A4](03_Nivel_3_Avanzado.md#a4)). Evidencia: una alerta de jailbreak con el usuario identificado, las recomendaciones atendidas y los registros de auditoría.

**Fase 6 · Red teaming, detección y respuesta (capas 4 y 6.5 y SOC).** Informe del AI Red Teaming Agent antes y después de endurecer, con el ASR por categoría; al menos una regla analítica de Sentinel sobre las alertas de IA y `AzureActivity` (por ejemplo, robo de credenciales correlacionado con `listKeys`), y un playbook de incidente de IA ensayado con un simulacro de LLMjacking o de envenenamiento de herramientas ([A1](03_Nivel_3_Avanzado.md#a1), [A5](03_Nivel_3_Avanzado.md#a5), [A6](03_Nivel_3_Avanzado.md#a6), [A7](03_Nivel_3_Avanzado.md#a7)). Evidencia: informe de red teaming, regla como código y acta del simulacro con los tiempos de detección y contención.

**Fase 7 · Gobierno y cierre (transversal).** RACI aprobado con el sponsor del agente, compuertas del ciclo de vida, presupuesto con alertas y costos reales, y el mapa de marcos y regulación de los países donde operas, revisado por Legal ([O1](#o1), [O2](#o2), [O3](#o3)). Evidencia: paquete para el comité con la tabla de evidencias por capa y los riesgos residuales, una presentación de diez minutos y la consulta de recursos con la etiqueta del programa vacía tras la limpieza.

<a id="quiz-operacion"></a>

## Evaluación del nivel

Responde y compara con [Evaluaciones y respuestas](06_Evaluaciones_y_respuestas.md#eval-operacion). Con 80 % o más, ¡nivel aprobado! (En la versión web puedes corregir en línea y generar tu certificado).

1. Según el Digital Omnibus on AI (Reglamento (UE) 2026/1744), ¿desde cuándo aplican las obligaciones para los sistemas de alto riesgo autónomos, no integrados en productos?
   - a) 2-ago-2026
   - b) 2-dic-2026
   - c) 2-ago-2028
   - d) 2-dic-2027

2. ¿Qué control del dominio de IA del MCSB v2 apunta a los ataques a la cadena de suministro con un registro central de modelos, validación automática y aprobación en varias etapas?
   - a) AI-1 · Usar solo modelos aprobados
   - b) AI-4 · Mínimo privilegio para las funciones de los agentes
   - c) AI-6 · Monitoreo y detección
   - d) AI-7 · Red teaming continuo

3. A fines de octubre de 2026, ¿qué pasó con el proyecto de ley de IA de Chile basado en riesgos (boletines 15869-19 y 16821-19)?
   - a) Se promulgó y entró en vigor con multas de hasta 20.000 UTM
   - b) La Comisión de Desafíos del Futuro del Senado aprobó por unanimidad legislarlo (26-oct-2026), sin la indicación sustitutiva del Gobierno; sigue en trámite
   - c) Se archivó y lo reemplazó la moción sobre agentes del Boletín 18.820-19
   - d) El Tribunal Constitucional lo declaró inadmisible

4. Tu auditor pide evidencia de un sistema de gestión de IA. ¿Qué valor tiene la certificación ISO/IEC 42001 de Microsoft, que incluye a Foundry en su alcance?
   - a) Certifica automáticamente tu propio sistema de gestión de IA
   - b) Reemplaza las evaluaciones que exige la Ley de IA de la UE
   - c) Es evidencia del proveedor, útil en tu gestión de terceros, pero no sustituye tu propio sistema de gestión de IA
   - d) Solo aplica a Microsoft 365 Copilot, no a Foundry

5. ¿Qué rol mínimo permite detener o bloquear un agente desde el Foundry Control Plane?
   - a) Reader
   - b) Foundry User
   - c) Contributor
   - d) Cost Management Reader

6. Al crear un blueprint de agente en Entra, ¿qué responsable exige la plataforma?
   - a) Un sponsor, persona o grupo responsable del agente; el owner es recomendado
   - b) Un owner técnico; el sponsor es opcional
   - c) Un Global Administrator como aprobador de cada identidad
   - d) Ninguno, porque Foundry gobierna la identidad

7. ¿Qué combinan las políticas de ciclo de vida (preview) de Entra ID Governance para identidades de agente?
   - a) Solo la caducidad de los secretos del blueprint a los 90 días
   - b) El borrado automático de los agentes sin trazas durante 30 días
   - c) Una revisión de acceso trimestral fija que aprueba el Global Administrator
   - d) Reconfirmación periódica (de 30 a 730 días), un mínimo de sponsors e inactividad sin tokens emitidos, con acciones, periodo de gracia y destinatarios de respaldo

8. En el mapeo de roles por persona de Foundry, ¿qué rol mínimo necesita el líder técnico para publicar agentes?
   - a) Foundry User en el proyecto
   - b) Foundry Project Manager sobre el recurso
   - c) Azure AI Developer en el hub
   - d) Cognitive Services Contributor en la suscripción

9. Despliegas API Management con gateways en dos regiones y la misma política llm-token-limit de 10.000 tokens por minuto por suscripción. ¿Qué es correcto?
   - a) El contador es por gateway y no se suma entre regiones, y con streaming o solicitudes concurrentes el límite puede superarse temporalmente
   - b) El contador se comparte entre regiones mediante una caché global
   - c) La política solo funciona en el tier Premium clásico
   - d) Al superar el límite, API Management encola las solicitudes hasta el minuto siguiente

10. ¿Qué alerta de Defender for AI Services indica un posible denial of wallet por un volumen anómalo de solicitudes?
   - a) AI.Azure_AccessAnomaly
   - b) AI.Azure_LLMReconnaissance
   - c) AI.Azure_DOWVolumeAnomaly
   - d) AI.Azure_AnomalousToolInvocation

11. ¿Cómo entró Storm-2139 en los servicios de IA generativa cuyo acceso revendió después de alterar sus capacidades?
   - a) Explotó una vulnerabilidad de día cero en el plano de control de Azure
   - b) Usó credenciales de clientes expuestas en fuentes públicas
   - c) Compró suscripciones legítimas con tarjetas robadas
   - d) Engañó con phishing a empleados de Microsoft

12. ¿Qué riesgo del OWASP Top 10 para aplicaciones de LLM 2025 cubre el denial of wallet y el consumo descontrolado de recursos?
   - a) LLM01 Prompt Injection
   - b) LLM06 Excessive Agency
   - c) LLM03 Supply Chain
   - d) LLM10 Unbounded Consumption

13. Quieres aislar la salida del Agent Service con tu propia VNet en un recurso de Foundry que ya está en uso. ¿Qué dice la documentación?
   - a) No puedes agregar la inyección de VNet a un recurso existente ni cambiar después la subred: hay que redesplegar
   - b) Basta con agregar un private endpoint al recurso
   - c) La activas desde el portal en cualquier momento, sin interrupción
   - d) Se configura por proyecto, no por recurso, y se cambia cuando quieras

14. En la arquitectura baseline de Foundry, el WAF de Application Gateway empieza a devolver 403 en conversaciones largas que incluyen código o SQL. ¿Qué recomienda la arquitectura?
   - a) Pasar el WAF a modo de detección de forma permanente
   - b) Deshabilitar el conjunto de reglas DRS para la ruta del chat
   - c) Publicar el chat en un endpoint sin WAF
   - d) Crear exclusiones acotadas al campo del cuerpo que contiene los mensajes, porque la puntuación de anomalías se acumula en conversaciones largas

15. En tu diseño, API Management Standard v2 es el AI gateway y recibe tráfico de Internet. ¿Cómo obtienes protección DDoS para ese punto de entrada?
   - a) Habilitando Azure DDoS Protection directamente en la instancia v2
   - b) Poniendo Application Gateway con WAF o Front Door delante, porque los tiers v2 no permiten habilitar DDoS Protection
   - c) Con Defender for APIs, que incluye mitigación volumétrica
   - d) No hace falta, porque Standard v2 incluye DDoS Network Protection

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. Los precios son de lista, en USD y sin impuestos, y cambian: confírmalos en la calculadora de precios de Azure antes de presupuestar. La infografía analizada pertenece a su autor y se usa solo como material de estudio. El contenido regulatorio y de privacidad es una referencia y no constituye asesoría legal: las decisiones corresponden a tus áreas de Legal, privacidad y cumplimiento. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 7 de noviembre de 2026

> **Anexo del Frontier CISO Atlas 1.0.** Informe de verificación de ISO/IEC, ISA/IEC, ETSI, ISACA, ISC2, The Open Group, SABSA, FAIR, SFIA, ENISA, NACD–ISA, CyBOK y marcos sectoriales, hecho el 15 de noviembre de 2026 contra las páginas de los organismos emisores. Es el informe tal como lo entregó el agente de verificación; la base consolidada está en `data/base_de_referencia.json` y el resumen en `docs/04_Base_de_Referencia.md`.

# Base de referencia verificada: organismos y artefactos (al 15-nov-2026)

## Resumen

Verifiqué los 26 ítems (unos 45 artefactos) contra las páginas del organismo emisor. La mayoría quedó verificada en datos de catálogo; varias estructuras internas quedaron como «parcial» porque el texto normativo es de pago o la página oficial no fue accesible.

Las entradas de abajo llevan todos los campos pedidos, en el mismo orden, para serializarlas.

Lo que cambia respecto de una foto de 2024:

- **ISO/IEC 27090:2026** (seguridad de sistemas de IA) se publicó en octubre de 2026.
- ISO/IEC 27701:2025 es la edición 2, publicada en 2025-10, y ahora es una norma de sistema de gestión independiente.
- **COBIT 7** se lanza el 19-nov-2026 según ISACA; hoy sigue vigente COBIT 2019.
- **CISM** tiene un esquema nuevo desde el 3-nov-2026, y **CISSP** tendrá uno nuevo desde el 15-abr-2027.
- **NCSC CAF v4.0** (ago-2025) sumó un Core Profile el 30-oct-2026.
- **NACD–ISA** publicó la 5.ª edición del manual en 2026 y **CyBOK** la versión 1.2 en septiembre de 2026.
- Tres normas ISO de base están en revisión: 27014, 31000 y 22301.

## Entradas por artefacto

Claves: `org` = organismo · `ver` = version_vigente · `cant` = estructura_cantidad · `nombres` = estructura_nombres · `url` = url_oficial · `nov` = novedades_2025_2026 · `verif` = verificado · `nota`.

### ISO / IEC

**1. ISO/IEC 27001:2022**
- org: ISO/IEC JTC 1/SC 27
- ver: Edición 3, con 1 enmienda (Amd 1:2024, «Climate action changes»)
- fecha: 2022-10; enmienda 2024-02
- estado: vigente, etapa 60.60; la ficha no anuncia reemplazo
- cant: 7 cláusulas de requisitos (4–10) + Anexo A con 93 controles en 4 temas
- nombres: [4 Context of the organization; 5 Leadership; 6 Planning; 7 Support; 8 Operation; 9 Performance evaluation; 10 Improvement; Annex A (normative) Information security controls reference: Organizational (37), People (8), Physical (14), Technological (34)]
- url: https://www.iso.org/standard/27001 · enmienda: https://www.iso.org/standard/88435.html
- nov: sin edición nueva en 2025–2026. La enmienda de 2024 agrega en 4.1 que la organización debe determinar si el cambio climático es una cuestión relevante.
- verif: parcial
- nota: cláusulas 4–8 vistas en el índice de la OBP de ISO; 9–10 y el título del Anexo A en una copia del índice. El conteo por tema viene de fuente secundaria: 37, 8, 14 y 34.

**2. ISO/IEC 27002:2022**
- org: ISO/IEC JTC 1/SC 27
- ver: Edición 3
- fecha: 2022-02, versión corregida 2022-03
- estado: vigente (60.60)
- cant: 93 controles en cuatro temas; 5 atributos
- nombres (temas): [Organizational controls (cl. 5; 37); People controls (cl. 6; 8); Physical controls (cl. 7; 14); Technological controls (cl. 8; 34)]
- nombres (atributos):
  - Control type: Preventive, Detective, Corrective
  - Information security properties: Confidentiality, Integrity, Availability
  - Cybersecurity concepts: Identify, Protect, Detect, Respond, Recover
  - Operational capabilities (15): Governance; Asset management; Information protection; Human resource security; Physical security; System and network security; Application security; Secure configuration; Identity and access management; Threat and vulnerability management; Continuity; Supplier relationships security; Legal and compliance; Information security event management; Information security assurance
  - Security domains (4): Governance and Ecosystem; Protection; Defence; Resilience
- url: https://www.iso.org/standard/75652.html
- nov: ninguna; la ficha no lista enmiendas
- verif: parcial
- nota: los valores de los atributos salen de fuentes secundarias coincidentes (itsmf.ch, iso-library.com); no pude abrir la cláusula 4.2 en la OBP. El prólogo oficial sí confirma que «#information_security_assurance» pasó a la columna «Operational capabilities». La norma escribe los valores como etiquetas (`#Asset_management`).

**3a. ISO/IEC 27005:2022**
- org: ISO/IEC JTC 1/SC 27
- ver: Edición 4, 2022-10
- estado: vigente (60.60)
- cant: no verificado completo
- nombres: [5 Information security risk management; 6 Context establishment; resto no visto]
- url: https://www.iso.org/standard/80585.html
- nov: ninguna
- verif: parcial
- nota: adapta los principios generales de ISO 31000 al contexto de la seguridad de la información.

**3b. ISO 31000:2018**
- org: ISO/TC 262
- ver: Edición 2 (2018-02), revisada y confirmada en 2023
- estado: vigente, en revisión. ISO/DIS 31000 (edición 3) está en fase de consulta, etapa 40.00.
- cant: 3 componentes
- nombres: [principles; framework; process] (la norma provee principios, un marco y un proceso)
- url: https://www.iso.org/standard/31000 · borrador: https://www.iso.org/standard/88574.html
- nov: edición 3 en trámite
- verif: si (catálogo); títulos exactos de cláusulas no vistos

**4. ISO/IEC 27701:2025**
- org: ISO/IEC JTC 1/SC 27
- ver: Edición 2, 2025-10
- estado: vigente; la edición 2019 está retirada
- cant / nombres: no verificado (índice no abierto; 64 páginas)
- url: https://www.iso.org/standard/27701
- nov: es la novedad. Puede usarse sola, porque es una norma de sistema de gestión independiente; la ficha agrega que se alinea con sistemas ISO/IEC 27001 existentes.
- verif: parcial
- nota: publicada el 2025-10-14.

**5. ISO/IEC 27014:2020**
- org: ISO/IEC JTC 1/SC 27
- ver: Edición 2 (2020-12, corregida 2022-04)
- estado: vigente, con reemplazo inminente. Etapa 90.92; será reemplazada por ISO/IEC FDIS 27014, cuya edición 3 está en etapa 50.60 (cierre de votación).
- cant: 4 procesos de gobierno; 3 cláusulas sustantivas
- nombres: procesos [evaluate; direct; monitor; communicate]; cláusulas [6 Governance and management standards; 7 Entity governance and information security governance; 8 The governing body's requirements on the ISMS]
- url: https://www.iso.org/standard/74046.html · FDIS: https://www.iso.org/standard/94270.html
- nov: edición 3 por publicarse; un espejo nacional fecha el cierre de votación el 12-ago-2026
- verif: si
- nota: el resumen del FDIS repite el alcance de la edición 2020.

**6. ISO/IEC 27035 (serie)**
- org: ISO/IEC JTC 1/SC 27
- ver / fecha por parte:
  - 27035-1:2023, Ed. 2, 2023-02: Principles and process
  - 27035-2:2023, Ed. 2, 2023-02: Guidelines to plan and prepare for incident response
  - 27035-3:2020, Ed. 1, 2020-09: Guidelines for ICT incident response operations
  - 27035-4:2024, Ed. 1, 2024-12: Coordination
- estado: las cuatro vigentes; la parte 3 está en etapa 90.60 (cierre de revisión)
- cant: 4 partes; 5 fases de proceso
- nombres (fases, parte 1 cl. 5): [Plan and prepare; Detect and report; Assess and decide; Respond; Learn lessons]
- url: https://www.iso.org/standard/78973.html · https://www.iso.org/standard/78974.html · https://www.iso.org/standard/74033.html · https://www.iso.org/standard/80973.html
- nov: la parte 4 es de dic-2024
- verif: si

**7. ISO 22301:2019**
- org: ISO/TC 292
- ver: Edición 2 (2019) + Amd 1:2024 (2024-02)
- estado: vigente, en revisión. ISO/CD 22301 (edición 3) está en desarrollo, etapa 30.60.
- cant / nombres: no verificado en esta sesión
- url: https://www.iso.org/standard/88412.html · borrador: https://www.iso.org/standard/93606.html
- nov: proyecto de edición 3 aprobado en 2025-12; comentarios al borrador cerrados el 2026-05-10
- verif: parcial
- nota: no abrí la ficha base de la edición 2019.

**8. ISO/IEC 42001:2023**
- org: ISO/IEC JTC 1/SC 42
- ver: Edición 1, 2023-12
- estado: vigente, etapa 60.60
- cant: 7 cláusulas (4–10) + Anexo A con 38 controles, diez objetivos de control y nueve áreas (A.2 a A.10)
- nombres (cláusulas): [Context of the organization; Leadership; Planning; Support; Operation; Performance evaluation; Improvement]
- nombres (Anexo A): [A.2 Policies related to AI (3); A.3 Internal organization (2); A.4 Resources for AI systems (5); A.5 Assessing impacts of AI systems (4); A.6 AI system life cycle (9); A.7 Data for AI systems (5); A.8 Information for interested parties of AI systems (4); A.9 Use of AI systems (3); A.10 Third-party and customer relationships (3)]
- url: https://www.iso.org/standard/42001
- nov: sin enmiendas; se sumaron las normas complementarias 42005 y 42006
- verif: parcial
- nota: catálogo oficial; cláusulas y Anexo A por fuentes secundarias coincidentes. Una fuente aislada (aiactindex.eu) dice 39 controles.

**9. Otras normas de IA**
- org: ISO/IEC JTC 1/SC 42 (y SC 27 para 27090)
- ver / fecha / estado:
  - ISO/IEC 42005:2025, Ed. 1, 2025-05, vigente: AI system impact assessment
  - ISO/IEC 42006:2025, Ed. 1, 2025-07, vigente: Requirements for bodies providing audit and certification of AI management systems
  - ISO/IEC 23894:2023, Ed. 1, 2023-02, vigente: Guidance on risk management
  - ISO/IEC 38507:2022, Ed. 1, 2022-04, vigente: Governance implications of the use of AI by organizations
  - ISO/IEC 27090:2026, Ed. 1, 2026-10, vigente: Cybersecurity — Artificial intelligence (AI) — Addressing security threats and compromises to AI systems
- cant: 5 normas; el SC 42 declara 44 normas publicadas y 54 en desarrollo
- nombres: los títulos de arriba
- url: https://www.iso.org/standard/42005 · https://www.iso.org/standard/42006 · https://www.iso.org/standard/77304.html · https://www.iso.org/standard/56641.html · https://www.iso.org/standard/27090 · comité: https://www.iso.org/committee/6794475.html
- nov: 42005, 42006 y 27090 son de 2025–2026
- verif: si
- nota: no busqué ISO/IEC 27091 ni otros proyectos de SC 27 sobre IA.

### IEC / ISA y ETSI

**10. ISA/IEC 62443 (serie)**
- org: ISA99 / IEC TC 65 WG 10
- ver / fecha (ediciones ISA): 1-1 (2007); 2-1 (2024); TR 2-2 (2025); TR 2-3 (2015); 2-4 (2018, idéntica a IEC 62443-2-4:2015+AMD1:2017); 3-2 (2020); 3-3 (2013); 4-1 (2018); 4-2 (2018)
- estado: serie vigente
- cant: 4 grupos; 7 requisitos fundamentales; ISAGCA habla de 14 documentos
- nombres (grupos): [General (1-x); Policies and procedures (2-x); System (3-x); Component (4-x)]
- nombres (FR): [FR1 Identification and authentication control; FR2 Use control; FR3 System integrity; FR4 Data confidentiality; FR5 Restricted data flow; FR6 Timely response to events; FR7 Resource availability]
- url: https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards · https://www.isa.org/products/isa-62443-3-3-2013-security-for-industrial-au
- nov: ISA-TR62443-2-2-2025 (IACS security protection scheme)
- verif: parcial
- nota: no consulté el webstore de IEC. Una fuente secundaria da IEC 62443-2-1:2024 (Ed. 2.0) e IEC 62443-2-4:2023 (Ed. 2.0). La ficha ISA de la parte 3-3 nombra las siete áreas; la numeración FR1–FR7 viene de fuentes secundarias.

**11a. ETSI EN 303 645**
- org: ETSI TC CYBER
- ver: V3.1.3
- fecha: 2024-09
- estado: vigente (el portal de ETSI la lista como publicación)
- cant: 13 grupos de disposiciones (5.1–5.13) + 5.0 + cláusula 6
- nombres: [5.0 Reporting implementation; 5.1 No universal default passwords; 5.2 Implement a means to manage reports of vulnerabilities; 5.3 Keep software updated; 5.4 Securely store sensitive security parameters; 5.5 Communicate securely; 5.6 Minimize exposed attack surfaces; 5.7 Ensure software integrity; 5.8 Ensure that personal data is secure; 5.9 Make systems resilient to outages; 5.10 Examine system telemetry data; 5.11 Make it easy for users to delete user data; 5.12 Make installation and maintenance of devices easy; 5.13 Validate input data; 6 Data protection provisions for consumer IoT]
- url: https://www.etsi.org/deliver/etsi_en/303600_303699/303645/03.01.03_60/en_303645v030103p.pdf
- nov: sin versión nueva en 2025–2026
- verif: si

**11b. ETSI EN 304 223**
- org: ETSI TC SAI
- ver: V2.1.1
- fecha: 2025-12
- estado: vigente (norma europea)
- cant: 13 principios en 5 fases
- nombres:
  - Secure Design: P1 Raise awareness of AI security threats and risks; P2 Design the AI system for security as well as functionality and performance; P3 Evaluate the threats and manage the risks to the AI system; P4 Enable human responsibility for AI systems
  - Secure Development: P5 Identify, track and protect the assets; P6 Secure the infrastructure; P7 Secure the supply chain; P8 Document data, models and prompts; P9 Conduct appropriate testing and evaluation
  - Secure Deployment: P10 Communication and processes associated with End-users and Affected Entities
  - Secure Maintenance: P11 Maintain regular security updates, patches and mitigations; P12 Monitor the system's behaviour
  - Secure End of Life: P13 Ensure proper data and model disposal
- url: https://www.etsi.org/deliver/etsi_en/304200_304299/304223/02.01.01_60/en_304223v020101p.pdf
- nov: es la novedad (dic-2025)
- verif: si
- nota: no abrí ETSI TS 104 223; su relación con la EN queda «no verificado».

### ISACA e ISC2

**12. COBIT**
- org: ISACA
- ver: COBIT 2019 (vigente hoy); COBIT 7 anunciado
- fecha: COBIT 2019 se presentó en 2018–2019; COBIT 7 se lanza el 19-nov-2026 según el artículo de soporte de ISACA del 13-nov-2026
- estado: COBIT 2019 vigente hasta su retiro el 31-dic-2027; COBIT 5 retirado el 26-oct-2026
- cant: 5 dominios; 40 objetivos de gobierno y gestión
- nombres: [EDM Evaluate, Direct and Monitor (5); APO Align, Plan and Organize (14); BAI Build, Acquire and Implement (11); DSS Deliver, Service and Support (6); MEA Monitor, Evaluate and Assess (4)]
- url: https://www.isaca.org/resources/cobit · https://support.isaca.org/s/article/COBIT-Certificate-and-Exam-Updates
- nov: COBIT 7 llega como plataforma digital con acceso básico gratuito y acceso premium (Design Guide y tres evaluaciones: Board-Level, High-Level, Detailed)
- verif: parcial
- nota: los 40 objetivos están en isaca.org; el reparto por dominio viene de fuentes secundarias coincidentes. La estructura de COBIT 7 es «no verificado»: no hay contenido público. Terceros daban el 27-oct-2026 como fecha de lanzamiento; ISACA ahora dice 19-nov-2026.

**13a. CISM**
- org: ISACA
- ver: esquema de examen 2026
- fecha: vigente desde el 3-nov-2026 (anuncio del 10-sep-2026)
- estado: vigente
- cant: 4 dominios; 150 preguntas
- nombres: [D1 Information Security Governance 18%; D2 Information Security Risk Management 20%; D3 Information Security Program 33%; D4 Incident Management 29%]
- url: https://www.isaca.org/credentialing/cism/cism-exam-content-outline · https://support.isaca.org/s/article/Certification-CISM-Job-Practice-Update-2026
- nov: agrega dos áreas de contenido (enterprise architecture e information security architecture). El esquema 2022 era 17/20/33/30.
- verif: si

**13b. CRISC**
- org: ISACA
- ver: esquema de examen 2025
- fecha: vigente desde el 3-nov-2025
- estado: vigente
- cant: 4 dominios; 150 preguntas
- nombres: [D1 Governance 26%; D2 Risk Assessment 22%; D3 Risk Response and Reporting 32%; D4 Technology and Security 20%]
- url: https://www.isaca.org/credentialing/crisc/crisc-exam-content-outline · https://support.isaca.org/s/article/Certification-CRISC-Job-Practice-Update-2025
- nov: el esquema 2021 era 26/20/32/22. El mismo anuncio llevó CDPSE a 4 dominios (Privacy Governance 20%; Privacy Risk Management and Compliance 18%; Data Life Cycle Management 23%; Privacy Engineering 39%).
- verif: si

**13c. AAISM (Advanced in AI Security Management)**
- org: ISACA
- ver: esquema vigente; fecha de lanzamiento no verificada
- estado: vigente; requiere CISM o CISSP activo
- cant: 3 dominios; 90 preguntas
- nombres: [D1 AI Governance and Program Management 31%; D2 AI Risk Management 31%; D3 AI Technologies and Controls 38%]
- url: https://www.isaca.org/credentialing/aaism/aaism-exam-content-outline
- nov: credencial nueva
- verif: si

**13d. Otras credenciales de IA de ISACA**
- org: ISACA
- ver / estado:
  - AAIA (Advanced in AI Audit): vigente; 90 preguntas
  - AAIR (Advanced in AI Risk): vigente; 90 preguntas
  - AAIG (Advanced in AI Governance): en beta, con el período de postulación cerrado
- cant: 3 dominios o áreas cada una
- nombres:
  - AAIA: [AI Governance and Risk 33%; AI Operations 46%; AI Auditing Tools and Techniques 21%]
  - AAIR: [AI Risk Governance and Framework Integration 37%; AI Life Cycle Risk Management 21%; AI Risk Program Management 42%]
  - AAIG (áreas, sin pesos): [AI Enterprise Governance; Data and AI Architecture Principles; AI Enterprise Integration and Performance Monitoring]
- url: https://www.isaca.org/credentialing/aaia/aaia-exam-content-outline · https://www.isaca.org/credentialing/aair/aair-exam-content-outline · https://www.isaca.org/credentialing/aaig
- nov: AAIR y AAIG son de 2026. El comunicado de CISM menciona además la nueva Certified Cybersecurity Specialist (CCS).
- verif: parcial
- nota: la fecha de lanzamiento de AAIR (15-abr-2026) viene de fuentes secundarias.

**14. Digital Trust Ecosystem Framework (DTEF)**
- org: ISACA
- ver: edición 2024 (anuncio del 6-mar-2024)
- estado: vigente
- cant: 6 dominios; 4 nodos; 34 factores de confianza
- nombres (dominios): [Culture (3 factores); Emergence (4); Enabling and Support (7); Human Factors (4); Direct and Monitor (12); Architecture (4)]
- nombres (nodos): [People; Process; Technology; Organization]
- nombres (jerarquía): Domain → Trust Factor → Practice → Activity → Outcome
- url: https://www.isaca.org/resources/news-and-trends/newsletters/atisaca/2024/volume-5/digital-trust-ecosystem-framework-to-steer-organizations-toward-sturdier-relationships
- nov: sin versión nueva verificada
- verif: parcial
- nota: los factores de confianza por dominio salen de una lámina del capítulo ISACA San Diego (https://isaca-sd.squarespace.com/s/DTEF-0224_laminate_digital.pdf); el total de 34 es mi suma.

**15. CISSP**
- org: ISC2
- ver: esquema vigente desde el 15-abr-2024
- estado: vigente; ISC2 avisa que desde el 15-abr-2027 regirá un esquema nuevo
- cant: 8 dominios
- nombres (2024): [1 Security and Risk Management 16%; 2 Asset Security 10%; 3 Security Architecture and Engineering 13%; 4 Communication and Network Security 13%; 5 Identity and Access Management (IAM) 13%; 6 Security Assessment and Testing 12%; 7 Security Operations 13%; 8 Software Development Security 10%]
- nombres (2027): [1 Security Governance and Risk Management 13,6%; 2 Asset Security 12%; 3 Security Architecture and Engineering 12,8%; 4 Communication and Network Security 12,8%; 5 IAM 13,6%; 6 Security Assessment and Testing 11,2%; 7 Security Operations 12,8%; 8 Software Development Security 11,2%]
- url: https://www.isc2.org/certifications/cissp/cissp-certification-exam-outline
- nov: el dominio 1 cambia de nombre; ISC2 integra la seguridad de IA en los 8 dominios en lugar de crear un dominio propio
- verif: si para 2024; parcial para 2027
- nota: los pesos de 2027 vienen de cuatro fuentes secundarias coincidentes que citan el PDF de ISC2.

### The Open Group, SABSA y FAIR Institute

**16a. TOGAF Standard**
- org: The Open Group
- ver: 10th Edition
- fecha: no verificado (la página no la muestra)
- estado: vigente
- cant: 2 bloques
- nombres: [TOGAF Fundamental Content; TOGAF Series Guides]
- url: https://www.opengroup.org/togaf
- nov: no verificado
- verif: parcial

**16b. Open FAIR Body of Knowledge**
- org: The Open Group Security Forum
- ver: Risk Analysis (O-RA) Version 2.0.1; Risk Taxonomy (O-RT) Version 3.0.1
- fecha: noviembre de 2021 según fuente secundaria
- estado: vigente
- cant: 2 normas
- nombres (factores superiores de O-RT): [Loss Event Frequency; Loss Magnitude (Primary Loss Magnitude; Secondary Loss)]
- url: https://www.opengroup.org/open-fair
- nov: ninguna versión nueva verificada
- verif: si (versiones); parcial (fecha)

**16c. Zero Trust y arquitectura de seguridad**
- org: The Open Group (Security Forum / ZTA Working Group)
- ver / estado:
  - Zero Trust Commandments: norma publicada
  - Security Principles for Architecture: norma publicada
  - Zero Trust Reference Model: Snapshot, Version 1.0 (borrador)
  - Security Roles and Glossary: borrador en revisión
  - O-ISM3: figura como publicado; versión no verificada
  - O-ESA: no verificado
- fecha: no verificado
- cant / nombres: no verificado
- url: https://www.opengroup.org/forum/security-forum-0/zerotrustsecurityarchitecture · https://www.opengroup.org/events/Amsterdam-2025-05/Security
- nov: está en formación un «Security and Zero Trust Body of Knowledge» que integra estos documentos
- verif: parcial
- nota: no pude confirmar si el Reference Model pasó de borrador a norma en 2026.

**17. SABSA Matrix**
- org: The SABSA Institute
- ver / fecha: no verificado
- estado: vigente
- cant: 6 capas × 6 columnas = 36 celdas
- nombres (capas): [Contextual; Conceptual; Logical; Physical; Component; Service Management (llamada «Operational» en algunas fuentes)]
- nombres (columnas): [Assets (What); Motivation (Why); Process (How); People (Who); Location (Where); Time (When)]
- url: https://sabsa.org/sabsa-executive-summary/
- nov: no verificado
- verif: parcial
- nota: sabsa.org bloqueó la lectura; la estructura viene de fuentes secundarias coincidentes (por ejemplo https://alvor.io/frameworks/sabsa, que cita el resumen ejecutivo del instituto).

**18a. FAIR-CAM**
- org: FAIR Institute
- ver: Standard Artifact Version 1.0
- fecha: 15-ene-2025
- estado: vigente
- cant: 3 dominios funcionales
- nombres:
  - Loss Event Control: Prevention (Avoidance, Deterrence, Resistance); Detection (Visibility, Monitoring, Recognition); Response (Event Termination, Resilience, Loss Reduction)
  - Variance Management Control: Variance Prevention; Variance Identification; Variance Correction
  - Decision Support Control
- url: https://www.fairinstitute.org/fair-controls-analytics-model · https://www.fairinstitute.org/hubfs/Standards%20Artifacts/FAIR%20Controls%20Analytics%20Model%20%28FAIR-CAM%29%20Standard%20V1.0%20%28January%202025%29.pdf
- nov: pasó a norma v1.0 en 2025; el instituto también mantiene FAIR Model v3.0 y FAIR-MAM v1.0
- verif: si

**18b. FAIR-AIR**
- org: FAIR Institute
- ver: «FAIR-AIR Approach Playbook»; versión y fecha no verificadas
- estado: vigente
- cant: 5 pasos; 5 vectores de riesgo de IA generativa
- nombres (pasos): [Contextualize; Scope; Quantify; Prioritize/Treat; Decision Making]
- nombres (vectores): [Shadow GenAI; Foundational LLM; Hosting on LLMs; Managed LLMs; Active Cyber Attack]
- url: https://www.fairinstitute.org/hubfs/FAIR-AIR%20Approach%20Playbook.pdf
- nov: no verificado
- verif: parcial

### Competencias, gobierno corporativo y cuerpos de conocimiento

**19. SFIA**
- org: SFIA Foundation
- ver: SFIA 9
- fecha: octubre de 2024
- estado: vigente
- cant: 6 categorías; 147 habilidades; 7 niveles
- nombres:
  - Strategy and architecture: Strategy and planning; Financial and value management; Security and privacy; Governance, risk and compliance; Advice and guidance
  - Change and transformation: Change implementation; Change analysis; Change planning
  - Development and implementation: Systems development; Data and analytics; User centred design; Content management; Computational science
  - People and skills: People management; Skills management
  - Delivery and operation: Technology management; Service management; Security services; Data and records operations
  - Relationships and engagement: Stakeholder management; Sales and bid management; Marketing
- url: https://sfia-online.org/en/sfia-9 · https://sfia-online.org/en/sfia-9/sfia-views/sfia-9-multi-view/sfia-9-en-summary-chart-with-roles
- nov: la portada anuncia una consulta para SFIA 10 (no la abrí)
- verif: si
- nota: la seguridad está repartida en dos subcategorías. «Security and privacy» incluye Information security, Information assurance, Information and data compliance, Vulnerability research y Threat intelligence. «Security services» incluye Security operations, Identity and access management, Vulnerability assessment, Digital forensics, Cybercrime investigation, Offensive cyber operations y Penetration testing.

**20. European Cybersecurity Skills Framework (ECSF)**
- org: ENISA
- ver: edición de septiembre de 2022 (publicada el 19-sep-2022)
- estado: vigente, en revisión
- cant: 12 perfiles
- nombres: [Chief Information Security Officer (CISO); Cyber Incident Responder; Cyber Legal, Policy & Compliance Officer; Cyber Threat Intelligence Specialist; Cybersecurity Architect; Cybersecurity Auditor; Cybersecurity Educator; Cybersecurity Implementer; Cybersecurity Researcher; Cybersecurity Risk Manager; Digital Forensics Investigator; Penetration Tester]
- url: https://www.enisa.europa.eu/topics/skills-and-competences/skills-development/european-cybersecurity-skills-framework-ecsf · https://www.enisa.europa.eu/sites/default/files/publications/European%20Cybersecurity%20Skills%20Framework%20Role%20Profiles.pdf
- nov: ENISA prevé una consulta pública del ECSF revisado para fines de 2026; sumará niveles de competencia y alineación con el ciclo de vida de productos digitales seguros
- verif: si

**21. Director's Handbook on Cyber-Risk Oversight**
- org: NACD e Internet Security Alliance
- ver: Fifth Edition
- fecha: 2026 (mes no verificado)
- estado: vigente
- cant: 6 principios; 15 herramientas (A–O)
- nombres: [1 Treat Cybersecurity as a Strategic Risk; 2 Monitor Legal and Disclosure Implications; 3 Establish Board Oversight Structures and Access to Expertise; 4 Adopt an Enterprise Framework for Managing Cyber Risk; 5 Guide Cybersecurity Risk Measurement and Reporting; 6 Encourage Systemic Resilience and Collaboration]
- url: https://www.nacdonline.org/globalassets/public-pdfs/2026_directors-handbook-cyber-risk_accessible.pdf
- nov: edición nueva; reemplaza la de 2023. Trae prólogo de CISA y herramientas sobre IA, computación cuántica, ransomware, terceros y relación directorio–CISO.
- verif: si

**22. CyBOK**
- org: proyecto CyBOK (Reino Unido)
- ver: 1.2
- fecha: septiembre de 2026
- estado: vigente
- cant: 5 categorías; 21 áreas de conocimiento (más una introducción)
- nombres:
  - Human, Organisational & Regulatory Aspects: Risk Management & Governance; Law & Regulation; Human Factors; Privacy & Online Rights
  - Attacks & Defences: Forensics; Security Operations & Incident Management; Adversarial Behaviours; Malware & Attack Technologies
  - Systems Security: Authentication, Authorisation & Accountability; Formal Methods for Security; Distributed Systems Security; Operating Systems & Virtualisation Security; Cryptography
  - Software and Platform Security: Secure Software Lifecycle; Web & Mobile Security; Software Security
  - Infrastructure Security: Physical Layer and Telecommunications Security; Cyber Physical Systems; Hardware Security; Network Security; Applied Cryptography
- url: https://www.cybok.org/knowledgebase1_2/
- nov: la v1.2 revisa dos áreas (Software Security y Secure Software Lifecycle)
- verif: si
- nota: la v1.1 es de julio de 2021 y la v1.0 (19 áreas) de octubre de 2019.

### Marcos sectoriales y gubernamentales

**23. C2M2**
- org: Departamento de Energía de EE. UU. (CESER)
- ver: Version 2.1
- fecha: junio de 2022
- estado: vigente (página actualizada el 8-oct-2026)
- cant: 10 dominios; 356 prácticas; niveles MIL0–MIL3
- nombres: [Asset, Change, and Configuration Management (ASSET); Threat and Vulnerability Management (THREAT); Risk Management (RISK); Identity and Access Management (ACCESS); Situational Awareness (SITUATION); Event and Incident Response, Continuity of Operations (RESPONSE); Third-Party Risk Management (THIRD-PARTIES); Workforce Management (WORKFORCE); Cybersecurity Architecture (ARCHITECTURE); Cybersecurity Program Management (PROGRAM)]
- url: https://www.energy.gov/ceser/cybersecurity-capability-maturity-model-c2m2 · https://www.energy.gov/sites/default/files/2022-06/C2M2%20Version%202.1%20June%202022.pdf
- nov: sin versión nueva. Se agregó la «Cybersecurity Threat Profile Development Guide» (jul-2026); el mapeo a CSF 2.0 figura como «coming soon».
- verif: si

**24. PCI DSS**
- org: PCI Security Standards Council
- ver: v4.0.1
- fecha: junio de 2024
- estado: única versión activa (v4.0 retirada el 31-dic-2024)
- cant: 6 objetivos; 12 requisitos
- nombres (requisitos): [1 Install and maintain network security controls; 2 Apply secure configurations to all system components; 3 Protect stored account data; 4 Protect cardholder data with strong cryptography during transmission over open, public networks; 5 Protect all systems and networks from malicious software; 6 Develop and maintain secure systems and software; 7 Restrict access to system components and cardholder data by business need to know; 8 Identify users and authenticate access to system components; 9 Restrict physical access to cardholder data; 10 Log and monitor all access to system components and cardholder data; 11 Test security of systems and networks regularly; 12 Support information security with organizational policies and programs]
- nombres (objetivos): [Build and Maintain a Secure Network and Systems; Protect Account Data; los otros cuatro cubren gestión de vulnerabilidades, control de acceso, monitoreo y pruebas, y política de seguridad de la información]
- url: https://www.pcisecuritystandards.org/standards/pci-dss/
- nov: los 51 requisitos de fecha futura son obligatorios desde el 31-mar-2025. Entre el 3-jun y el 20-jul-2026 hubo una consulta sobre v4.0.1 para planificar la próxima versión; no hay v4.1 ni v5 anunciada.
- verif: parcial
- nota: versión, fechas y títulos de requisitos vienen de fuentes secundarias que citan el blog del consejo; la página oficial abierta no los lista. La redacción exacta de los objetivos 3 a 6 es «no verificado».

**25. Swift Customer Security Controls Framework (CSCF)**
- org: Swift
- ver: CSCF v2026 (rige para la atestación de 2026); CSCF v2027 ya publicado para 2027
- fecha: v2026 fechado 1-jul-2025
- estado: vigente
- cant: 3 objetivos; 7 principios; 32 controles (26 obligatorios y 6 recomendados)
- nombres (objetivos): [Secure your Environment; Know and Limit Access; Detect and Respond]
- nombres (principios): [1 Restrict Internet Access and Protect Critical Systems from General IT Environment; 2 Reduce Attack Surface and Vulnerabilities; 3 Physically Secure the Environment; 4 Prevent Compromise of Credentials; 5 Manage Identities and Separate Privileges; 6 Detect Anomalous Activity to Systems or Transaction Records; 7 Plan for Incident Response and Information Sharing]
- url: https://www.swift.com/myswift/services/training/swift-training-catalogue/swift-customer-security-programme-v2026
- nov: v2026 vuelve obligatorio el control 2.4 (Back Office Data Flow Security). v2027 mantiene 32 controles e incorpora al alcance las bóvedas de secretos y claves, además de guía sobre agentes de IA.
- verif: parcial
- nota: los principios están en swift.com; objetivos, conteo de controles y cambios de v2027 vienen de fuentes secundarias (por ejemplo https://www.usd.de/en/swift-cscfv2027-the-most-important-changes/).

**26a. Essential Eight Maturity Model**
- org: Australian Signals Directorate (ASD)
- ver: edición de noviembre de 2023 (última revisión 27-nov-2023)
- estado: vigente
- cant: 8 estrategias; 4 niveles de madurez (Zero a Three)
- nombres: [Patch applications; Patch operating systems; Multi-factor authentication; Restrict administrative privileges; Application control; Restrict Microsoft Office macros; User application hardening; Regular backups]
- url: https://www.cyber.gov.au/publication/essential-eight-maturity-model
- nov: ninguna
- verif: si

**26b. Cyber Assessment Framework (CAF)**
- org: NCSC (Reino Unido)
- ver: 4.0
- fecha: 6-ago-2025
- estado: vigente
- cant: 4 objetivos; 14 principios; 41 resultados contribuyentes
- nombres:
  - A Managing security risk: A1 Governance; A2 Risk Management; A3 Asset Management; A4 Supply Chain
  - B Protecting against cyber attack: B1 Service Protection Policies, Processes and Procedures; B2 Identity and Access Control; B3 Data Security; B4 System Security; B5 Resilient Networks and Systems; B6 Staff Awareness and Training
  - C Detecting cyber security events: C1 Security Monitoring; C2 Threat Hunting
  - D Minimising the impact of cyber security incidents: D1 Response and Recovery Planning; D2 Lessons Learned
- url: https://www.ncsc.gov.uk/collection/cyber-assessment-framework · https://www.ncsc.gov.uk/files/NCSC-Cyber-Assessment-Framework-4.0.pdf
- nov: v4.0 renombra C2 a «Threat Hunting» y agrega A2.b Understanding Threat y A4.b Secure Software Development and Support. El 30-oct-2026 se publicó el «CAF Core Profile», un piso mínimo común.
- verif: si
- nota: los 41 resultados son mi conteo sobre la tabla del Core Profile; una guía del gobierno todavía cita 39, de la versión anterior.

## Los 8 artefactos nuevos de 2025–2026 que un CISO debería conocer

1. **ISO/IEC 27090:2026** (oct-2026): primera norma de SC 27 sobre amenazas de seguridad específicas de sistemas de IA. https://www.iso.org/standard/27090
2. **ISO/IEC 27701:2025** (oct-2025): privacidad como sistema de gestión independiente de 27001. https://www.iso.org/standard/27701
3. **ISO/IEC 42005:2025 y 42006:2025**: evaluación de impacto de sistemas de IA y requisitos para organismos que certifican 42001.
4. **ETSI EN 304 223 V2.1.1** (dic-2025): línea base europea de ciberseguridad para modelos y sistemas de IA, con 13 principios.
5. **COBIT 7** (lanzamiento 19-nov-2026): primera versión mayor desde COBIT 2019; estructura aún no pública.
6. **Credenciales de IA de ISACA** (AAISM, AAIA, AAIR, AAIG en beta), más el esquema CISM 2026 y el CISSP 2027.
7. **NCSC CAF v4.0** (ago-2025) y su **Core Profile** (oct-2026).
8. **NACD–ISA Director's Handbook, 5.ª edición** (2026).

## Los 8 hallazgos más importantes para la taxonomía de dominios

1. **La IA ya es una capa propia, con cuatro ejes repetidos.** ISACA la divide en gobierno y programa, riesgo, tecnologías y controles, y auditoría. ISO/IEC 42001 dedica áreas enteras a impacto, ciclo de vida, datos y terceros; ETSI ordena 13 principios por fase de ciclo de vida. ISC2 hace lo contrario: reparte la IA en sus 8 dominios. La decisión de fondo es si la IA es un territorio o un eje transversal.

2. **Gobierno está separado de gestión, y la supervisión del directorio tiene marco propio.** COBIT aísla el dominio EDM; ISO/IEC 27014 define cuatro procesos de gobierno; NACD fija seis principios para el directorio; CISSP renombra su dominio 1 a «Security Governance and Risk Management». Conviene distinguir gobierno, gestión del programa y gestión de riesgo.

3. **La seguridad física es categoría de primer nivel en los marcos de control.** Es uno de los cuatro temas de ISO/IEC 27002 (14 controles) y una capacidad operativa propia; es el principio 3 de Swift y el requisito 9 de PCI DSS. Si los 24 dominios no tienen uno físico y ambiental explícito, es un hueco.

4. **La privacidad se trata por separado de la seguridad.** ISO/IEC 27701:2025 se independizó de 27001; CyBOK tiene «Privacy & Online Rights»; ISACA mantiene CDPSE con cuatro dominios; ETSI EN 303 645 separa la protección de datos en su cláusula 6.

5. **Aseguramiento, auditoría y pruebas forman una categoría propia.** Aparece como dominio 6 de CISSP, dominio MEA de COBIT, capacidad «Information security assurance» de 27002, resultado A2.c del CAF y perfiles Auditor y Penetration Tester del ECSF. ISO/IEC 42006 y AAIA la extienden a la IA.

6. **La criptografía es dominio de conocimiento, no de control.** CyBOK le da dos áreas (Cryptography y Applied Cryptography) y CISSP la trata como objetivos dentro de arquitectura. En cambio no figura entre las 15 capacidades operativas de 27002, ni como dominio de C2M2, ni como principio del CAF. NACD la trae al directorio por el lado cuántico. La pregunta es si va como dominio o como capacidad transversal.

7. **Personas, cultura y fuerza laboral son de primer nivel.** Lo muestran el tema «People controls» de 27002, el principio B6 del CAF, el dominio WORKFORCE de C2M2, el área «Human Factors» de CyBOK, los dominios Culture y Human Factors del DTEF, y marcos enteros dedicados a competencias (SFIA, ECSF).

8. **Terceros, arquitectura y entornos ciberfísicos tienen identidad propia.** Terceros y cadena de suministro: dominio THIRD-PARTIES de C2M2, principio A4 del CAF (que ahora incluye desarrollo seguro de software), área A.10 de 42001. Arquitectura: dominio ARCHITECTURE de C2M2, SABSA, y contenido nuevo en CISM 2026. OT, sistemas industriales e IoT: IEC 62443 con sus siete requisitos fundamentales, EN 303 645 y «Cyber Physical Systems» en CyBOK.

## Vacíos e incertidumbres

- **OBP de ISO no accesible por lectura directa.** Los títulos de cláusulas de 27001 y los índices de 27005, 27014 y 27035 salieron de resultados de búsqueda sobre la OBP. Los de 42001 son de fuente secundaria; los de 22301 y 27701 no se verificaron.
- **Estructuras de pago por fuentes secundarias.** Valores de atributos de 27002, conteos del Anexo A de 27001 y 42001.
- **Sitios no consultados o bloqueados.** sabsa.org bloqueó la lectura; no consulté el webstore de IEC ni abrí ETSI TS 104 223.
- **COBIT 7.** Dominios y cantidad de objetivos sin publicar; la fecha de lanzamiento cambió del 27-oct al 19-nov-2026.
- **The Open Group.** Sin verificar: fecha de TOGAF 10th Edition, versiones de O-ISM3 y O-ESA, y si el Zero Trust Reference Model ya es norma.
- **Otros datos de fuente secundaria.** Pesos de CISSP 2027, fecha de lanzamiento de AAIR, conteo de controles de Swift y cambios de v2027, versión y fechas de PCI DSS.
- **No busqué** ISO/IEC 27091 ni la página de la consulta de SFIA 10.

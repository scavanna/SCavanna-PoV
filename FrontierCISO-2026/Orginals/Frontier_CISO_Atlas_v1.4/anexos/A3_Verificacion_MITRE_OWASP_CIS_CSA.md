> **Anexo del Frontier CISO Atlas 1.0.** Informe de verificación de MITRE, OWASP, CIS, CSA, FIRST, cadena de suministro y protocolos de agentes, hecho el 15 de noviembre de 2026 contra las páginas de los organismos emisores. Es el informe tal como lo entregó el agente de verificación; la base consolidada está en `data/base_de_referencia.json` y el resumen en `docs/04_Base_de_Referencia.md`.

Las entradas van con los mismos campos para que las persistas. Los cambios de mayor impacto son:

- **ATT&CK:** está en v20 y Enterprise tiene 15 tácticas, con Defense Evasion dividida en Stealth y Defense Impairment.
- **ATLAS:** tiene 16 tácticas y etiqueta de plataforma "Agentic AI".
- **Catálogos y protocolos nuevos:** CCM v4.1, AICM v1.1, OWASP Top 10:2025, OWASP Agentic Top 10, MCP 2026-07-28 y A2A v1.0.

## Entradas por artefacto

### MITRE

**ATT&CK (Enterprise)**
- version_vigente / fecha / estado: v20 (el sitio marca v20.1 como versión actual), 13-oct-2026, vigente.
- estructura_cantidad: 15 tácticas Enterprise, 227 técnicas, 479 subtécnicas; Mobile e ICS tienen 12 tácticas cada una.
- estructura_nombres: Reconnaissance (TA0043), Resource Development (TA0042), Initial Access (TA0001), Execution (TA0002), Persistence (TA0003), Privilege Escalation (TA0004), Stealth (TA0005), Defense Impairment (TA0112), Credential Access (TA0006), Discovery (TA0007), Lateral Movement (TA0008), Collection (TA0009), Command and Control (TA0011), Exfiltration (TA0010), Impact (TA0040).
- url_oficial: https://attack.mitre.org/resources/updates/ ; https://attack.mitre.org/tactics/enterprise/ ; https://attack.mitre.org/resources/versions/
- novedades_2025_2026:
  - v19 (28-abr-2026) dividió Defense Evasion en Stealth y Defense Impairment, agregó subtécnicas a ICS e inició Detection Strategies en Mobile.
  - v20 agrega AI-Enabled Exfiltration, Direct Prompt Injection, Indirect Prompt Injection, Disable or Modify Tools: Impair Autonomous Defenses y Stage Capabilities: AI Result Poisoning.
  - v18.1 rigió desde el 28-oct-2025 y v17.1 desde el 22-abr-2025.
- verificado: si. nota: TA0005 se conserva renombrado como Stealth; TA0112 es un ID nuevo.

**ATLAS**
- version_vigente / fecha / estado: v2026.10, marcada "Latest", publicada unas dos semanas antes de la consulta; fecha exacta no mostrada. La v2026.09 es del 15-sep-2026 y usa formato 6.0.0.
- estructura_cantidad: 1 matriz, 16 tácticas, 129 técnicas, 92 subtécnicas, 44 mitigaciones, 77 casos de estudio, 44 entidades y 37 registros de software.
- estructura_nombres: AI Model Access (AML.TA0000), AI Attack Adaptation (AML.TA0001), Reconnaissance (AML.TA0002), Resource Development (AML.TA0003), Initial Access (AML.TA0004), Execution (AML.TA0005), Persistence (AML.TA0006), Defense Evasion (AML.TA0007), Discovery (AML.TA0008), Collection (AML.TA0009), Exfiltration (AML.TA0010), Impact (AML.TA0011), Privilege Escalation (AML.TA0012), Credential Access (AML.TA0013), Command and Control (AML.TA0014), Lateral Movement (AML.TA0015).
- url_oficial: https://github.com/mitre-atlas/atlas-data/releases ; https://github.com/mitre-atlas/atlas-data/blob/main/dist/v6/ATLAS-2026.09.yaml ; https://atlas.mitre.org (bloqueado para la herramienta).
- novedades_2025_2026:
  - Desde v2026.05 el contenido se versiona como YYYY.MM, separado del formato de datos.
  - Cada técnica lleva una o más plataformas: Predictive AI, Generative AI, Agentic AI, Enterprise.
  - v2026.08 renombró "AI Attack Staging" como "AI Attack Adaptation" y agregó Autonomous Reconnaissance, Autonomous Attack Orchestration y Autonomous AI Agent Communication.
  - El alcance ahora incluye comportamiento autónomo dañino habilitado por IA.
  - Lateral Movement (AML.TA0015) fue creada el 27-oct-2025 según el YAML.
- verificado: si. nota: los 16 nombres salen del YAML v2026.09; las notas de v2026.10 informan 16 tácticas y no listan cambios de tácticas. ATLAS conserva "Defense Evasion".

**D3FEND**
- version_vigente / fecha / estado: ontología 1.6.0 (31-ago-2026); interfaz web 0.26.1 (23-sep-2026); vigente.
- estructura_cantidad: 7 tácticas defensivas.
- estructura_nombres: Model, Harden, Detect, Isolate, Deceive, Evict, Restore.
- url_oficial: https://d3fend.mitre.org/changelog/ ; https://d3fend.mitre.org/tactic/d3f:Model/
- novedades_2025_2026: D3FEND for OT (ontología 1.3.0, 16-dic-2025); página D3FEND for Space (31-ago-2026); ontología 1.5.0 (31-jul-2026) actualizada a ATT&CK v19.0 y ATLAS v2026.06; matrices y búsqueda sobre ATT&CK Enterprise, Mobile e ICS, ATLAS y SPARTA.
- verificado: parcial. nota: la portada fue bloqueada por la herramienta. La lista de 7 proviene de documentación de ServiceNow; en el sitio oficial confirmé la página de la táctica Model (27 técnicas) y las menciones de Restore y Evict en el changelog.

**Engage**
- version_vigente / fecha / estado: 1.0, última actualización 28-feb-2022, vigente sin revisiones posteriores encontradas.
- estructura_cantidad: 5 objetivos (2 estratégicos, 3 de engagement) y 9 enfoques.
- estructura_nombres: objetivos Prepare, Expose, Affect, Elicit, Understand; enfoques Plan, Collect, Detect, Prevent, Direct, Disrupt, Reassure, Motivate, Analyze.
- url_oficial: https://engage.mitre.org/matrix/ ; https://engage.mitre.org/learn-more-matrix/
- novedades_2025_2026: ninguna encontrada. Sus mapeos siguen citando la táctica Defense Evasion de ATT&CK.
- verificado: si. nota: no conté las actividades.

**EMB3D**
- version_vigente / fecha / estado: 2.0.2, 1-jun-2026; vigente. La 2.0 es del 22-abr-2025.
- estructura_cantidad: 4 categorías de amenazas y 3 niveles de mitigación, mapeadas desde propiedades de dispositivo.
- estructura_nombres: amenazas Hardware, System Software, Application Software, Networking; mitigaciones Foundational, Intermediate, Leading.
- url_oficial: https://emb3d.mitre.org/
- novedades_2025_2026: v2.0 sumó representación STIX en JSON y nuevas propiedades, amenazas y mitigaciones.
- verificado: si.

**CWE Top 25**
- version_vigente / fecha / estado: edición 2025, publicada el 11-dic-2025, vigente. No hay edición 2026: la página de noticias 2026 de CWE no la anuncia (última entrada, 28-oct-2026).
- estructura_cantidad: 25 debilidades, sobre 39.080 registros CVE.
- estructura_nombres (primeras 10): CWE-79, CWE-89, CWE-352, CWE-862, CWE-787, CWE-22, CWE-416, CWE-125, CWE-78, CWE-94.
- url_oficial: https://cwe.mitre.org/top25/ ; https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25.html
- novedades_2025_2026:
  - Listas derivadas 2025 CWE Top 10 KEV Weaknesses y "On the Cusp" (29-ene-2026).
  - CWE 4.20 (30-abr-2026) agregó la vista "Weaknesses Related to AI/ML Products".
  - CWE 5.0 con Schema 8.0 (28-oct-2026) reemplaza "Category" por "Grouping" y agrega fases de ciclo de vida para IA y hardware; tiene 956 debilidades y 1.477 entradas.
- verificado: si. nota: varios medios titulan la lista como "2026"; el sitio oficial la llama 2025.

### OWASP

**Top 10 (aplicaciones web)**
- version_vigente / fecha / estado: Top 10:2025, publicada ("most current released version"). Release candidate el 6-nov-2025; versión final en enero de 2026 según fuentes secundarias (la página oficial no da fecha).
- estructura_cantidad: 10.
- estructura_nombres: A01:2025 Broken Access Control; A02:2025 Security Misconfiguration; A03:2025 Software Supply Chain Failures; A04:2025 Cryptographic Failures; A05:2025 Injection; A06:2025 Insecure Design; A07:2025 Authentication Failures; A08:2025 Software or Data Integrity Failures; A09:2025 Security Logging and Alerting Failures; A10:2025 Mishandling of Exceptional Conditions.
- url_oficial: https://top10.owasp.org/2025/ ; https://owasp.org/projects/top-ten
- novedades_2025_2026: dos categorías nuevas (A03 y A10); SSRF absorbida en A01; Security Misconfiguration sube de #5 a #2.
- verificado: si (fecha final: parcial). nota: la introducción escribe A09 como "Security Logging & Alerting Failures".

**API Security Top 10**
- version_vigente / fecha / estado: 2023 ("Latest Version 2023"), vigente; día no verificado; sin edición posterior en la página oficial.
- estructura_cantidad: 10.
- estructura_nombres: API1:2023 Broken Object Level Authorization; API2:2023 Broken Authentication; API3:2023 Broken Object Property Level Authorization; API4:2023 Unrestricted Resource Consumption; API5:2023 Broken Function Level Authorization; API6:2023 Unrestricted Access to Sensitive Business Flows; API7:2023 Server Side Request Forgery; API8:2023 Security Misconfiguration; API9:2023 Improper Inventory Management; API10:2023 Unsafe Consumption of APIs.
- url_oficial: https://owasp.org/projects/api-security-project ; https://api-security.owasp.org/
- novedades_2025_2026: ninguna encontrada.
- verificado: si.

**Top 10 for LLM Applications**
- version_vigente / fecha / estado: 2025, vigente; fecha de publicación no verificada (la página solo fecha traducciones: 12-mar-2025 y 22-jul-2025).
- estructura_cantidad: 10.
- estructura_nombres: LLM01:2025 Prompt Injection; LLM02:2025 Sensitive Information Disclosure; LLM03:2025 Supply Chain; LLM04:2025 Data and Model Poisoning; LLM05:2025 Improper Output Handling; LLM06:2025 Excessive Agency; LLM07:2025 System Prompt Leakage; LLM08:2025 Vector and Embedding Weaknesses; LLM09:2025 Misinformation; LLM10:2025 Unbounded Consumption.
- url_oficial: https://genai.owasp.org/llm-top-10/
- novedades_2025_2026: sin edición posterior en la página oficial.
- verificado: si (fecha: no).

**Top 10 for Agentic Applications**
- version_vigente / fecha / estado: "for 2026" (Version 2026), 9-dic-2025, publicada.
- estructura_cantidad: 10.
- estructura_nombres: ASI01 Agent Goal Hijack; ASI02 Tool Misuse and Exploitation; ASI03 Identity and Privilege Abuse; ASI04 Agentic Supply Chain Vulnerabilities; ASI05 Unexpected Code Execution (RCE); ASI06 Memory & Context Poisoning; ASI07 Insecure Inter-Agent Communication; ASI08 Cascading Failures; ASI09 Human-Agent Trust Exploitation; ASI10 Rogue Agents.
- url_oficial: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
- novedades_2025_2026: artefacto nuevo; trae apéndices de mapeo con el LLM Top 10 2025 y con CycloneDX/AIBOM.
- verificado: si. nota: la fecha está en la página oficial; los nombres salen del índice del PDF oficial, leído en copias alojadas por terceros.

**Non-Human Identities Top 10**
- version_vigente / fecha / estado: 2025, vigente; día no verificado.
- estructura_cantidad: 10.
- estructura_nombres: NHI1:2025 Improper Offboarding; NHI2:2025 Secret Leakage; NHI3:2025 Vulnerable Third-Party NHI; NHI4:2025 Insecure Authentication; NHI5:2025 Overprivileged NHI; NHI6:2025 Insecure Cloud Deployment Configurations; NHI7:2025 Long-Lived Secrets; NHI8:2025 Environment Isolation; NHI9:2025 NHI Reuse; NHI10:2025 Human Use of NHI.
- url_oficial: https://owasp.github.io/www-project-non-human-identities-top-10/2025/top-10-2025/
- novedades_2025_2026: es la primera edición.
- verificado: si.

**SAMM**
- version_vigente / fecha / estado: modelo v2; la última release del repositorio core es v2.2.0 (fecha no verificada); la anterior es v2.1.0.
- estructura_cantidad: 5 funciones de negocio y 15 prácticas.
- estructura_nombres:
  - Governance: Strategy & Metrics; Policy & Compliance; Education & Guidance.
  - Design: Threat Assessment; Security Requirements; Secure Architecture.
  - Implementation: Secure Build; Secure Deployment; Defect Management.
  - Verification: Architecture Assessment; Requirements-driven Testing; Security Testing.
  - Operations: Incident Management; Environment Management; Operational Management.
- url_oficial: https://owaspsamm.org/model/ ; https://github.com/owaspsamm/core/releases
- novedades_2025_2026: no verificadas.
- verificado: parcial. nota: la página del modelo sigue hablando de "Version 2.0".

**ASVS**
- version_vigente / fecha / estado: 5.0.0, 30-may-2025, "Stable release".
- estructura_cantidad: 17 capítulos.
- estructura_nombres: V1 Encoding and Sanitization; V2 Validation and Business Logic; V3 Web Frontend Security; V4 API and Web Service; V5 File Handling; V6 Authentication; V7 Session Management; V8 Authorization; V9 Self-contained Tokens; V10 OAuth and OIDC; V11 Cryptography; V12 Secure Communication; V13 Configuration; V14 Data Protection; V15 Secure Coding and Architecture; V16 Security Logging and Error Handling; V17 WebRTC.
- url_oficial: https://asvs.owasp.org/ ; https://github.com/OWASP/ASVS/tree/master/5.0/en
- novedades_2025_2026: la 5.0.0 reorganizó el estándar en 17 capítulos.
- verificado: si.

**Otros proyectos de IA de OWASP**
- AI Exchange:
  - Estado: proyecto flagship y documento vivo (383 páginas). Declara haber dado forma a ISO/IEC 27090 y al borrador de estándar de seguridad del EU AI Act.
  - Secciones: AI Security Overview; General controls; Input threats and controls; Development-time threats and controls; Runtime conventional security threats; AI Security Testing; AI Privacy; References.
  - URL: https://owaspai.org/
- AIVSS: última publicación v0.8 (fecha no verificada), con una calculadora "AIVSS 1.0" en línea; puntúa los riesgos núcleo de IA agéntica. https://aivss.owasp.org/
- AI Testing Guide: v1, 26-nov-2025, proyecto incubator. https://owasp.org/projects/ai-testing-guide
- MCP Top 10:
  - Estado: beta (fase 3 de 5).
  - Riesgos: MCP01:2025 Token Mismanagement & Secret Exposure; MCP02:2025 Privilege Escalation via Scope Creep; MCP03:2025 Tool Poisoning; MCP04:2025 Software Supply Chain Attacks & Dependency Tampering; MCP05:2025 Command Injection & Execution; MCP06:2025 Prompt Injection via Contextual Payloads; MCP07:2025 Insufficient Authentication & Authorization; MCP08:2025 Lack of Audit and Telemetry; MCP09:2025 Shadow MCP Servers; MCP10:2025 Context Injection & Over-Sharing.
  - URL: https://owasp.org/projects/mcp-top-10
- verificado: si (AIVSS: parcial).

### CIS

**Critical Security Controls**
- version_vigente / fecha / estado: v8.1, 25-jun-2024 (nota de prensa), vigente. No encontré v9.
- estructura_cantidad: 18 controles, 153 salvaguardas, 3 grupos de implementación.
- estructura_nombres:
  1. Inventory and Control of Enterprise Assets
  2. Inventory and Control of Software Assets
  3. Data Protection
  4. Secure Configuration of Enterprise Assets and Software
  5. Account Management
  6. Access Control Management
  7. Continuous Vulnerability Management
  8. Audit Log Management
  9. Email and Web Browser Protections
  10. Malware Defenses
  11. Data Recovery
  12. Network Infrastructure Management
  13. Network Monitoring and Defense
  14. Security Awareness and Skills Training
  15. Service Provider Management
  16. Application Software Security
  17. Incident Response Management
  18. Penetration Testing
- Grupos de implementación: IG1 ("essential cyber hygiene"), IG2 e IG3 (todas las salvaguardas). El reparto 56/130/153 es de fuente secundaria.
- url_oficial: https://www.cisecurity.org/controls/cis-controls-list ; https://www.cisecurity.org/controls/v8-1 ; https://www.cisecurity.org/about-us/media/press-release/center-for-internet-security-releases-cis-controls-v8-1-with-new-governance-recommendations
- novedades_2025_2026: sin cambio de versión. Nuevos mapeos a CISA Cross-Sector CPGs v2 (9-nov-2026) y a CSA CCM v4.1 (6-nov-2026). La v8.1 ya había agregado la función "Govern" de CSF 2.0.
- verificado: si.

### CSA

**Cloud Controls Matrix (CCM)**
- version_vigente / fecha / estado: v4.1, 27-ene-2026, vigente. Transición de dos años: obligatoria para nuevos postulantes STAR desde julio de 2027 y para todos en enero de 2028 (artículo de Schellman publicado por CSA).
- estructura_cantidad: 17 dominios y 207 objetivos de control; CAIQ v4.1 tiene 283 preguntas.
- estructura_nombres: A&A Audit & Assurance; AIS Application & Interface Security; BCR Business Continuity Mgmt & Op Resilience; CCC Change Control & Configuration Management; CEK Cryptography, Encryption, & Key Management; DCS Datacenter Security; DSP Data Security & Privacy; GRC Governance, Risk Management, & Compliance; HRS Human Resources Security; IAM Identity & Access Management; IPY Interoperability & Portability; I&S Infrastructure Security (antes IVS Infrastructure & Virtualization Security); LOG Logging & Monitoring; SEF Sec. Incident Mgmt, E-Disc & Cloud Forensics; STA Supply Chain Mgmt, Transparency, & Accountability; TVM Threat & Vulnerability Management; UEM Universal Endpoint Management.
- url_oficial: https://cloudsecurityalliance.org/artifacts/cloud-controls-matrix-v4-1 ; https://cloudsecurityalliance.org/research/cloud-controls-matrix
- novedades_2025_2026: 11 controles nuevos, entre ellos AIS-08 API Security, LOG-08 Audit Logs Sanitization, STA-09 Service Bill of Material, TVM-04 Threat Analysis and Modelling y TVM-10 Threat Response. Mapea a NIST 800-171 r2, ATT&CK v17.1 y DORA.
- verificado: si. nota: la página de investigación aún dice "197 control objectives" y lista IVS; la ficha v4.1 dice 207.

**AI Controls Matrix (AICM)**
- version_vigente / fecha / estado: v1.1, 22-jun-2026, vigente. La v1.0 es del 9-jul-2025 (243 objetivos).
- estructura_cantidad: 18 dominios y 247 objetivos de control; AI-CAIQ v1.1 tiene 320 preguntas.
- estructura_nombres: los 17 dominios de CCM v4.1 más MDS Model Security (13 controles).
- Relación con CCM: construida sobre CCM; la v1.1 está sincronizada con CCM v4.1. Asigna controles a cinco roles (Model Provider, Orchestrated Service Provider, Application Provider, AI Customer, Cloud Service Provider).
- STAR for AI:
  - Level 1: autoevaluación con AI-CAIQ, con variante Valid-AI-ted.
  - Level 2: disponible desde el 27-oct-2026. Rutas de certificación: ISO/IEC 27001 + AICM, 27001 + 42001 + AICM, y 42001 + AICM. Hay además una atestación SOC 2 + AICM.
- url_oficial: https://cloudsecurityalliance.org/artifacts/ai-controls-matrix-v1-1 ; https://cloudsecurityalliance.org/star/ai/
- novedades_2025_2026: nuevo mapeo a AIUC-1, además de BSI AIC4, ISO/IEC 42001, EU AI Act y NIST AI RMF / AI 600-1.
- verificado: si (lista nominal de los 18 dominios: parcial, por fuente secundaria). nota: un dataset de CSA advierte que v1.1.0 renumeró controles; 54 de los 242 IDs compartidos con v1.0.3 designan otro control.

**MAESTRO y guías de IA agéntica / Zero Trust**
- version_vigente / fecha / estado: MAESTRO no tiene número de versión; publicado en febrero de 2025 según un blog de CSA del 15-oct-2026.
- estructura_cantidad: 7 capas.
- estructura_nombres: Foundation Models; Data Operations; Agent Frameworks; Deployment & Infrastructure; Evaluation & Observability; Security & Compliance (vertical); Agent Ecosystem.
- url_oficial: https://cloudsecurityalliance.org/blog/2026/10/15/i-love-google-s-agentic-ai-security-roadmap-adding-maestro-will-make-it-more-powerful-an-open-letter-to-google ; https://github.com/CloudSecurityAlliance/MAESTRO
- novedades_2025_2026:
  - Agentic AI Red Teaming Guide (28-may-2025): https://cloudsecurityalliance.org/artifacts/agentic-ai-red-teaming-guide
  - Agentic AI Identity and Access Management: A New Approach (18-ago-2025): https://cloudsecurityalliance.org/artifacts/agentic-ai-identity-and-access-management-a-new-approach
  - The Agentic Trust Framework: Zero Trust Governance for AI Agents (blog, 2-feb-2026), con cinco elementos: Identity, Behavior, Data Governance, Segmentation, Incident Response. https://cloudsecurityalliance.org/blog/2026/02/02/the-agentic-trust-framework-zero-trust-governance-for-ai-agents
  - CSAI Foundation, "Securing the Agentic Control Plane": 30 publicaciones de laboratorio al 2-abr-2026. https://labs.cloudsecurityalliance.org/agentic/
  - Zero Trust: "Integrating DNS and SDP: Enhanced Zero Trust Policy Enforcement 2.0" (8-oct-2026) y "Why You Need a Zero Trust Program Management Office" (15-oct-2026). https://cloudsecurityalliance.org/zt
- verificado: parcial. nota: no abrí la publicación original de MAESTRO.

### FIRST

**CVSS**
- version_vigente / fecha / estado: v4.0, publicación inicial en noviembre de 2023, vigente.
- estructura: no verificada (la página del SIG no lista los grupos de métricas).
- url_oficial: https://www.first.org/cvss/
- novedades_2025_2026: documento suplementario CVSS Consumer Implementation Guide (fecha no verificada).
- verificado: parcial.

**EPSS**
- version_vigente / fecha / estado: v5 (v2026.06.15), publicando desde el 15-jun-2026, vigente. La v4 (v2025.03.14) publicó desde el 17-mar-2025.
- estructura: probabilidad de 0 a 1 de explotación en 30 días, más percentil, por cada CVE.
- url_oficial: https://www.first.org/epss/ ; https://research.empiricalsecurity.com/research/epss-v5-is-here
- novedades_2025_2026: la v5 reentrena el modelo y mejora la calibración.
- verificado: parcial. nota: first.org habla de "Version 5 today"; la fecha viene de Empirical Security (genera los scores) y de fuentes secundarias, porque la página de datos de FIRST no abrió.

**TLP**
- version_vigente / fecha / estado: 2.0, autoritativa desde agosto de 2022, vigente.
- estructura_cantidad: 4 etiquetas.
- estructura_nombres: TLP:RED, TLP:AMBER (con la variante TLP:AMBER+STRICT), TLP:GREEN, TLP:CLEAR.
- url_oficial: https://www.first.org/tlp/
- novedades_2025_2026: ninguna encontrada.
- verificado: si.

**CSIRT Services Framework**
- version_vigente / fecha / estado: v2.1; fecha no verificada (la página no la muestra).
- estructura_cantidad: 5 áreas de servicio y 19 servicios.
- estructura_nombres: Information Security Event Management; Information Security Incident Management; Vulnerability Management; Situational Awareness; Knowledge Transfer.
- url_oficial: https://www.first.org/standards/frameworks/csirts/csirt_services_framework_v2.1
- novedades_2025_2026: ninguna encontrada.
- verificado: si (fecha: no). nota: el encabezado HTML dice "Version 2.1 (for review purposes)".

### Cadena de suministro de software

**SLSA**
- version_vigente / fecha / estado: v1.2, "Status: Approved"; fecha no verificada.
- estructura_cantidad: 2 pistas; 4 niveles Build (L0 a L3) y 4 niveles Source (L1 a L4).
- estructura_nombres:
  - Build: L0 No guarantees; L1 Provenance exists; L2 Hosted build platform; L3 Hardened builds.
  - Source: L1 Version controlled; L2 History & Provenance; L3 Continuous technical controls; L4 Two-party review.
- url_oficial: https://slsa.dev/spec/ ; https://slsa.dev/spec/v1.2/whats-new
- novedades_2025_2026: la v1.2 agrega la Source Track respecto de la v1.1.
- verificado: si (fecha: no).

**CISA: elementos mínimos de SBOM**
- version_vigente / fecha / estado: "2026 Minimum Elements for a Software Bill of Materials (SBOM)", v2.1, 29-jul-2026, final. La v2.0 fue el borrador del 22-ago-2025 y la v1.0 la de NTIA (12-jul-2021).
- estructura: Data Fields (SBOM Metadata y Component Data) y Practices and Processes.
- url_oficial: https://content.govdelivery.com/accounts/USDHSCISA/bulletins/422a7eb ; https://media.defense.gov/2026/Jul/29/2003971159/-1/-1/0/CSI_2026_cisa_sbom_minimum_elements_508c.PDF
- novedades_2025_2026: campos nuevos Component Hash, License, SBOM Tool Name y SBOM Generation Context; secciones para SaaS y para sistemas de IA; coautoría de CISA, NSA, FBI y socios internacionales.
- verificado: si. nota: no extraje la lista completa de campos ni recuperé la página en cisa.gov.

### IA segura y protocolos de agentes

**Coalition for Secure AI (CoSAI)**
- version_vigente / fecha / estado: sin versión; opera bajo OASIS Open; activa.
- estructura_cantidad: 4 líneas de trabajo.
- estructura_nombres: Software Supply Chain Security for AI Systems; Preparing Defenders for a Changing Security Landscape; AI Security Risk Governance; Secure Design Patterns for Agentic Systems.
- url_oficial: https://www.coalitionforsecureai.org/ ; https://www.coalitionforsecureai.org/resources/
- novedades_2025_2026 (fechas de los resúmenes en su blog):
  - Signing ML Artifacts (29-sep-2025)
  - AI Incident Response Framework (30-oct-2025)
  - Model Context Protocol (MCP) Security (20-ene-2026)
  - The Future of Agentic Security (31-mar-2026)
  - Agentic Identity and Access Management (17-abr-2026)
  - AI Shared Responsibility Framework (28-may-2026)
  - Zero Trust for AI Systems (16-sep-2026)
  - MCP Security V2.0 (25-sep-2026)
  - AIMM: Artifact Integrity Maturity Model (5-oct-2026)
- verificado: si.

**Google Secure AI Framework (SAIF)**
- version_vigente / fecha / estado: sin número de versión ni fecha en el sitio; vigente.
- estructura_cantidad: 6 elementos centrales; el SAIF Map tiene 4 áreas de componentes y 15 riesgos.
- estructura_nombres:
  1. Expand strong security foundations to the AI ecosystem
  2. Extend detection and response to bring AI into an organization's threat universe
  3. Automate defenses to keep pace with existing and new threats
  4. Harmonize platform level controls to ensure consistent security across the organization
  5. Adapt controls to adjust mitigations and create faster feedback loops for AI deployment
  6. Contextualize AI system risks in surrounding business processes
- Áreas del mapa: Data, Infrastructure, Model, Application.
- url_oficial: https://saif.google/ ; https://www.saif.google/secure-ai-framework ; https://safety.google/intl/en_uk/safety/saif/
- novedades_2025_2026: sección "Focus on Agents" y Agent Risk Self Assessment; el mapa, los riesgos y los controles fueron aportados a CoSAI.
- verificado: si (fechas: no).

**Model Context Protocol (MCP)**
- version_vigente / fecha / estado: 2026-07-28, publicada el 28-jul-2026, "current". La anterior es 2025-11-25.
- gobierno:
  - Constituido como "Model Context Protocol a Series of LF Projects, LLC" (Linux Foundation) y alojado en la Agentic AI Foundation (AAIF).
  - Los Lead Maintainers son David Soria Parra y Den Delimarsky; debajo están los Core Maintainers y Maintainers. Los puestos son personales, no de empresas.
  - Los cambios se proponen como Specification Enhancement Proposals (SEP).
- url_oficial: https://modelcontextprotocol.io/specification/2026-07-28 ; https://modelcontextprotocol.io/community/governance ; https://blog.modelcontextprotocol.io/posts/2026-07-28/
- novedades_2025_2026:
  - Núcleo sin estado: desaparecen el handshake initialize y la cabecera Mcp-Session-Id.
  - Marco formal de extensiones: Tasks, MCP Apps, Skills over MCP y Enterprise Managed Authorization.
  - Autorización endurecida (RFC 9207 y documentos de metadatos de cliente en lugar de registro dinámico).
  - Política de deprecación con ventana mínima de 12 meses.
- verificado: si. nota: la donación a AAIF el 9-dic-2025 consta en fuentes secundarias. La página versionada muestra un aviso de "older version", pero la página de versionado afirma "The current protocol version is 2026-07-28".

**Agent2Agent (A2A)**
- version_vigente / fecha / estado: v1.0.1 (26-may-2026); la v1.0.0 (12-mar-2026) fue la primera estable y apta para producción.
- gobierno:
  - Proyecto open source bajo la Linux Foundation, aportado por Google.
  - Aceptado en AAIF como proyecto "Growth Stage" (anuncio de A2A del 27-ago-2026; de AAIF del 17-ago-2026).
  - Comité técnico con AWS, Cisco, Google, IBM Research, Microsoft, Salesforce, SAP y ServiceNow.
- url_oficial: https://a2a-protocol.org/latest/ ; https://github.com/a2aproject/A2A/releases ; https://aaif.io/
- novedades_2025_2026: la v1.0 trae Agent Cards firmadas, multi-tenancy, bindings JSON-RPC, gRPC y HTTP+JSON, y flujos OAuth modernizados. AAIF aloja también AGENTS.md, Goose, agentgateway, Agent Skills, Agent Router, Open Responses, OpenEnv y OpenSandbox.
- verificado: si.

## Artefactos nuevos de 2025–2026 que un CISO debería conocer

1. OWASP Top 10 for Agentic Applications for 2026 (9-dic-2025).
2. CSA AICM v1.1 (22-jun-2026) y STAR for AI Level 2 (27-oct-2026).
3. MCP 2026-07-28 y A2A v1.0, ambos bajo la Agentic AI Foundation de la Linux Foundation.
4. CWE 5.0 con Schema 8.0 (28-oct-2026) y la vista de debilidades de IA/ML de CWE 4.20.
5. "2026 Minimum Elements for an SBOM" de CISA y socios (29-jul-2026).
6. Publicaciones de CoSAI: MCP Security V2.0, Agentic Identity and Access Management, Zero Trust for AI Systems y AI Incident Response Framework.
7. OWASP MCP Top 10 (beta), AI Testing Guide v1 (26-nov-2025) y AIVSS v0.8.
8. SLSA v1.2 con Source Track y EPSS v5 (15-jun-2026).

## Ocho hallazgos para la taxonomía

1. **ATT&CK Enterprise pasó a 15 tácticas.** Defense Evasion ya no existe: se dividió en Stealth y Defense Impairment. Todo mapeo que use "Defense Evasion" quedó desactualizado; ATLAS y Engage todavía lo usan.
2. **La IA entró al ATT&CK general.** La v20 incluye inyección de prompts, exfiltración habilitada por IA y degradación de defensas autónomas. La IA ya no es solo un dominio aparte.
3. **ATLAS aporta dos tácticas propias de IA y una dimensión de plataforma.** Las tácticas son AI Model Access y AI Attack Adaptation; la plataforma distingue Predictive AI, Generative AI, Agentic AI y Enterprise. Sirve como eje para separar seguridad de modelos de seguridad de agentes.
4. **La seguridad de agentes ya tiene taxonomías de primer nivel propias.** Están ASI01–ASI10, las 7 capas de MAESTRO, el MCP Top 10 y las guías de CoSAI. Los temas recurrentes son secuestro de objetivos, abuso de herramientas, envenenamiento de memoria y contexto, comunicación entre agentes, fallas en cascada y agentes rebeldes.
5. **Los protocolos de agentes son ahora infraestructura gobernada.** MCP y A2A están bajo una misma fundación, con grupos de trabajo de identidad, observabilidad y seguridad. Conviene un dominio o subdominio explícito para protocolos y gateways de agentes.
6. **La identidad no humana y de agentes es transversal.** Aparece en el NHI Top 10, ASI03, las guías de IAM agéntico de CSA y CoSAI, y en las nuevas debilidades de sesión y credenciales de CWE 5.0.
7. **Los controles de IA agregan un solo dominio nuevo.** AICM reutiliza los 17 dominios de CCM y suma Model Security. Es un argumento para ampliar dominios existentes y crear uno específico de modelo, no duplicar toda la taxonomía. CIS v8.1 y CCM v4.1 refuerzan gobierno, modelado de amenazas y seguridad de API.
8. **La cadena de suministro subió a categoría de primer nivel.** Lo muestran A03:2025 de OWASP, la Source Track de SLSA, el SBOM 2026 con IA y SaaS, STA-09 de CCM, LLM03, ASI04 y MCP04. En paralelo, D3FEND y ATT&CK ampliaron cobertura a OT y espacio.

## Brechas e incertidumbres

- **Sitios bloqueados:** la herramienta no pudo abrir las portadas de atlas.mitre.org y d3fend.mitre.org; usé el repositorio oficial de datos de ATLAS y las páginas internas de D3FEND.
- **Fechas no verificadas:** SLSA v1.2, CSIRT Services Framework v2.1, SAMM v2.2.0, AIVSS v0.8, LLM Top 10 2025, día exacto de ATLAS v2026.10 y fecha final de OWASP Top 10:2025.
- **Estructuras no verificadas:** grupos de métricas de CVSS v4.0, lista completa de campos del SBOM 2026, cantidad de actividades de Engage y lista nominal oficial de los 18 dominios de AICM.
- **Solo fuente secundaria:** reparto 56/130/153 de los grupos de CIS, fecha de donación de MCP a AAIF y fecha de inicio de EPSS v5.
- **No busqué en profundidad** ediciones 2026 de API Security, LLM o NHI más allá de lo que muestran sus páginas oficiales.

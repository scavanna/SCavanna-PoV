> **Anexo del Frontier CISO Atlas 1.0.** Informe de verificación de NIST, CISA, DoD y SEC, hecho el 15 de noviembre de 2026 contra las páginas de los organismos emisores. Es el informe tal como lo entregó el agente de verificación; la base consolidada está en `data/base_de_referencia.json` y el resumen en `docs/04_Base_de_Referencia.md`.

# Referencia verificada NIST / CISA / DoD / SEC al 15-nov-2026

**Resumen.** Los 22 ítems quedaron verificados contra páginas oficiales; cuatro son parciales (5, 15, 20 y 21) y el detalle está en cada nota. Cinco cambios pesan sobre el Atlas:
- **BOD 22-01 revocada:** la reemplaza BOD 26-04 (10-jun-2026); KEV sigue vigente.
- **NIST IR 8547 final** (27-oct-2026), con fechas de transición poscuántica firmes.
- **CMMC Fase II suspendida** (13-jul-2026); el programa queda en Fase 1.
- **Renombre «AI» → «Super Intelligence (SI)»** en proyectos NIST: COSAiS pasó a llamarse COSIS el 20-oct-2026 por una orden ejecutiva del 29-sep-2026.
- **CSF 2.0 sin cambios** en su Core.

Abajo va el mismo contenido con los mismos campos, listo para serializar.

**Método:** abrí yo las páginas de 1–5, 8, 11–16, 18 y 19. Los nombres de estructura de 6, 7, 9, 10, 17, 20, 21 y el estado de 22 salieron de sub-búsquedas delegadas que abrieron las fuentes oficiales; esos PDF no los releí.

## Entradas (una por artefacto)

**1. NIST — Cybersecurity Framework (CSF) 2.0 (CSWP 29)**
- version_vigente: 2.0 · fecha: 2024-02-26 · estado: final; el historial solo registra borrador (08/08/23) y final (02/26/24)
- estructura_cantidad: 6 funciones, 22 categorías, 106 subcategorías (GV 31, ID 21, PR 22, DE 11, RS 13, RC 8)
- estructura_nombres: Govern: GV.OC Organizational Context; GV.RM Risk Management Strategy; GV.RR Roles, Responsibilities, and Authorities; GV.PO Policy; GV.OV Oversight; GV.SC Cybersecurity Supply Chain Risk Management. Identify: ID.AM Asset Management; ID.RA Risk Assessment; ID.IM Improvement. Protect: PR.AA Identity Management, Authentication, and Access Control; PR.AT Awareness and Training; PR.DS Data Security; PR.PS Platform Security; PR.IR Technology Infrastructure Resilience. Detect: DE.CM Continuous Monitoring; DE.AE Adverse Event Analysis. Respond: RS.MA Incident Management; RS.AN Incident Analysis; RS.CO Incident Response Reporting and Communication; RS.MI Incident Mitigation. Recover: RC.RP Incident Recovery Plan Execution; RC.CO Incident Recovery Communication
- url_oficial: https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final
- novedades_2025_2026: segundo aniversario el 24-feb-2026; SP 800-221r1 ipd en comentarios hasta el 7-dic-2026; borrador de Community Profile para O-RAN de agencias federales; versión final del Informative References Quick-Start Guide
- verificado: si · nota: las 106 subcategorías son conteo propio de identificadores únicos en el texto del PDF.

**2. NIST — IR 8596 «Cyber AI Profile»**
- version_vigente: Initial Preliminary Draft · fecha: 2025-12-16; comentarios cerrados el 30-ene-2026 · estado: borrador preliminar; «Reviewing Comments»
- estructura_cantidad: 3 áreas de enfoque, organizadas sobre Funciones, Categorías y Subcategorías del CSF 2.0
- estructura_nombres: Securing AI System Components (Secure); Conducting AI-Enabled Cyber Defense (Defend); Thwarting AI-enabled Cyber Attacks (Thwart)
- url_oficial: https://csrc.nist.gov/pubs/ir/8596/iprd
- novedades_2025_2026: sesiones de trabajo virtuales el 28-abr, 5-may y 12-may-2026; los comentarios alimentarán el initial public draft; el proyecto NCCoE ahora figura como «Cyber SI Profile» (https://www.nccoe.nist.gov/projects/cyber-si-profile)
- verificado: si · nota: no hallé un initial public draft; la URL `/pubs/ir/8596/ipd` no devolvió documento.

**3. NIST — SP 800-53 Rev. 5**
- version_vigente: Rev. 5, Release 5.2.0 · fecha: 2025-08-27 (base: sep-2020, con actualizaciones al 10-dic-2020) · estado: final
- estructura_cantidad: 20 familias
- estructura_nombres: AC Access Control; AT Awareness and Training; AU Audit and Accountability; CA Assessment, Authorization, and Monitoring; CM Configuration Management; CP Contingency Planning; IA Identification and Authentication; IR Incident Response; MA Maintenance; MP Media Protection; PE Physical and Environmental Protection; PL Planning; PM Program Management; PS Personnel Security; PT PII Processing and Transparency; RA Risk Assessment; SA System and Services Acquisition; SC System and Communications Protection; SI System and Information Integrity; SR Supply Chain Risk Management
- url_oficial: https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final
- novedades_2025_2026: 5.2.0 agrega SA-15(13), SA-24 y SI-02(07) y revisa SI-07(12). No hay release posterior ni plan anunciado de Rev. 6.
- verificado: si · nota: la página Downloads todavía dice «CURRENT VERSION 5.1» y CPRT fecha 5.2.0 el 26-ago-2025.

**3b. NIST — Control Overlays for Securing AI Systems (COSAiS → COSIS)**
- version_vigente: sin overlay publicado · fecha: concept paper 2025-08-14 · estado: en desarrollo
- estructura_cantidad: 5 casos de uso propuestos
- estructura_nombres: Adapting and Using Generative SI – Assistant/LLM; Using and Fine-Tuning Predictive SI; Using SI Agent Systems – Single Agent; Using SI Agent Systems – Multi-Agent; Security Controls for SI Developers
- url_oficial: https://csrc.nist.gov/projects/cosis
- novedades_2025_2026: esquema anotado (discussion draft) del overlay de IA predictiva, 8-ene-2026; renombre a COSIS el 20-oct-2026; los documentos ya emitidos no se alteraron
- verificado: si · nota: la página de publicaciones del proyecto solo lista AI 100-2 E2025 (final, 24-mar-2025).

**4. NIST — SP 800-37 Rev. 2 (RMF)**
- version_vigente: Rev. 2 · fecha: dic-2018 · estado: final
- estructura_cantidad: 7 pasos
- estructura_nombres: Prepare; Categorize; Select; Implement; Assess; Authorize; Monitor
- url_oficial: https://csrc.nist.gov/pubs/sp/800/37/r2/final
- novedades_2025_2026: ninguna revisión; la página del RMF se actualizó el 23-sep-2026.
- verificado: si · nota: los pasos salen de https://csrc.nist.gov/Projects/risk-management/about-rmf.

**5. NIST — AI RMF 1.0 (AI 100-1)**
- version_vigente: 1.0 · fecha: 2023-01-26 · estado: final, en revisión como parte del White House AI Action Plan
- estructura_cantidad: 4 funciones, 19 categorías (GOVERN 6, MAP 5, MEASURE 4, MANAGE 4)
- estructura_nombres: GOVERN, MAP, MEASURE, MANAGE
- url_oficial: https://www.nist.gov/itl/ai-risk-management-framework
- novedades_2025_2026: concept note del 7-abr-2026 para un perfil «Trustworthy AI in Critical Infrastructure». No hay borrador de versión nueva; las diapositivas de NIST del 27-mar-2026 lo listan como «Revised NIST AI RMF» en «Looking Ahead».
- verificado: parcial · nota: conté 71 subcategorías en el texto extraído y MEASURE 3.3 no apareció, así que el total exacto queda sin verificar.

**5b. NIST — AI 600-1 (Generative AI Profile)**
- version_vigente: única · fecha: 2024-07-26 · estado: final
- estructura_cantidad: 12 riesgos
- estructura_nombres: CBRN Information or Capabilities; Confabulation; Dangerous, Violent, or Hateful Content; Data Privacy; Environmental Impacts; Harmful Bias or Homogenization; Human-AI Configuration; Information Integrity; Information Security; Intellectual Property; Obscene, Degrading, and/or Abusive Content; Value Chain and Component Integration
- url_oficial: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
- novedades_2025_2026: ninguna hallada.
- verificado: si · nota: el encabezado 2.6 del documento dice «Harmful Bias and Homogenization».

**5c. NIST/CAISI — AI Agent Standards Initiative**
- version_vigente: iniciativa, sin perfil ni guía final sobre agentes · fecha: 2026-02-17 · estado: en curso
- estructura_cantidad: 3 pilares
- estructura_nombres: desarrollo de estándares de agentes liderado por la industria; protocolos abiertos liderados por la comunidad; investigación en seguridad e identidad de agentes
- url_oficial: https://www.nist.gov/super-intelligence/si-agent-standards-initiative
- novedades_2025_2026:
  - RFI sobre seguridad de agentes, 12-ene-2026.
  - NIST AI 800-5 (final, 18-may-2026), resumen de respuestas a ese RFI.
  - NIST AI 800-2 (initial public draft), sobre evaluaciones de modelos y agentes.
  - Concept paper del NCCoE sobre identidad y autorización de agentes (feb-2026).
- verificado: si · nota: CAISI figura ahora como «Center for Advancing Innovation and Standards for Super Intelligence (CAISSI)»; las «Agent Security guidelines» están anunciadas como próximas.

**6. NIST — Privacy Framework**
- version_vigente: 1.0 · fecha: 2020-01-16 · estado: final; 1.1 sigue en Initial Public Draft (CSWP 40, 2025-04-14, comentarios cerrados el 13-jun-2025)
- estructura_cantidad: 5 funciones
- estructura_nombres: Identify-P; Govern-P; Control-P; Communicate-P; Protect-P (iguales en 1.0 y en el borrador 1.1)
- url_oficial: https://www.nist.gov/privacy-framework
- novedades_2025_2026: el borrador 1.1 se realinea con CSF 2.0; la página del proyecto (actualizada el 1-abr-2026) dice «Privacy Framework 1.1 Coming soon».
- verificado: si · nota: borrador en https://csrc.nist.gov/pubs/cswp/40/nist-privacy-framework-11/ipd.

**7. NIST — NICE Framework (SP 800-181 Rev. 1 + Components)**
- version_vigente: SP 800-181 Rev. 1 (nov-2020); Components v2.2.0 · fecha: 2026-04-28 · estado: final
- estructura_cantidad: 5 categorías de roles, 42 roles (OG 17, DD 9, IO 7, PD 7, IN 2), 11 áreas de competencia
- estructura_nombres:
  - Categorías: Oversight and Governance; Design and Development; Implementation and Operation; Protection and Defense; Investigation.
  - Áreas de competencia: Access Controls; Artificial Intelligence (AI) Security; Asset Management; Cloud Security; Communications Security; Cryptography; Cyber Resiliency; DevSecOps; Operating Systems (OS) Security; Operational Technology (OT) Security; Supply Chain Security.
- url_oficial: https://www.nist.gov/itl/applied-cybersecurity/nice/nice-framework-resource-center/current-version/change-logs
- novedades_2025_2026:
  - v2.0.0 (5-mar-2025): elimina Cyberspace Effects y Cyberspace Intelligence y agrega el rol OT Cybersecurity Engineering.
  - v2.1.0 (3-dic-2025): actualiza AI Security (NF-COM-002).
  - v2.2.0: nuevo rol Cybersecurity Supply Chain Risk Management (OG-WRL-017) y actualiza Cryptography y DevSecOps.
- verificado: si · nota: IA aparece como área de competencia, no como rol. La página Current Versions imprime «2.2.0 (April 28, 2025)»; el change log y la nota de prensa dicen 2026.

**8. NIST — SP 800-207 Zero Trust Architecture (y 800-207A)**
- version_vigente: SP 800-207 · fecha: ago-2020 · estado: final; 800-207A final (sep-2023)
- estructura_cantidad: 7 tenets
- estructura_nombres:
  1. All data sources and computing services are considered resources.
  2. All communication is secured regardless of network location.
  3. Access to individual enterprise resources is granted on a per-session basis.
  4. Access to resources is determined by dynamic policy—including the observable state of client identity, application/service, and the requesting asset—and may include other behavioral and environmental attributes.
  5. The enterprise monitors and measures the integrity and security posture of all owned and associated assets.
  6. All resource authentication and authorization are dynamic and strictly enforced before access is allowed.
  7. The enterprise collects as much information as possible about the current state of assets, network infrastructure and communications and uses it to improve its security posture.
- url_oficial: https://csrc.nist.gov/pubs/sp/800/207/final
- novedades_2025_2026: ninguna revisión.
- verificado: si · nota: 800-207A es «A Zero Trust Architecture Model for Access Control in Cloud-Native Applications in Multi-Cloud Environments» (https://csrc.nist.gov/pubs/sp/800/207/a/final).

**9. NIST — SP 800-61 Rev. 3**
- version_vigente: Rev. 3 · fecha: abr-2025 (reemplaza a Rev. 2 de 2012) · estado: final
- estructura_cantidad: 3 secciones; perfil comunitario del CSF 2.0 en 2 tablas
- estructura_nombres:
  - Tabla 2, «Preparation and Lessons Learned»: Govern, Identify, Protect.
  - Tabla 3, «Incident Response»: Detect, Respond, Recover.
  - Mejora continua: categoría ID.IM.
  - Columnas: CSF Element | Description | Priority (High/Medium/Low) | Recommendations (R), Considerations (C), Notes (N).
- url_oficial: https://csrc.nist.gov/pubs/sp/800/61/r3/final
- novedades_2025_2026: abandona el ciclo de 4 fases de Rev. 2 y lo mapea a las 6 funciones.
- verificado: si · nota: prioridades por función: GV Low; ID y PR Medium; DE, RS y RC High.

**10. NIST — SP 800-160 Vol. 2 Rev. 1**
- version_vigente: Vol. 2 Rev. 1 · fecha: dic-2021 · estado: final
- estructura_cantidad: 4 metas, 8 objetivos, 14 técnicas
- estructura_nombres:
  - Metas: Anticipate; Withstand; Recover; Adapt.
  - Objetivos: Prevent or Avoid; Prepare; Continue; Constrain; Reconstitute; Understand; Transform; Re-Architect.
  - Técnicas: Adaptive Response; Analytic Monitoring; Contextual Awareness; Coordinated Protection; Deception; Diversity; Dynamic Positioning; Non-Persistence; Privilege Restriction; Realignment; Redundancy; Segmentation; Substantiated Integrity; Unpredictability.
- url_oficial: https://csrc.nist.gov/pubs/sp/800/160/v2/r1/final
- novedades_2025_2026: ninguna.
- verificado: si · nota: la cantidad de principios de diseño quedó sin verificar.

**11. NIST — SP 800-218 SSDF (y 800-218A)**
- version_vigente: SSDF v1.1 · fecha: feb-2022 · estado: final
- estructura_cantidad: 4 grupos, 19 prácticas activas (PO 5, PS 3, PW 8, RV 3)
- estructura_nombres: Prepare the Organization (PO); Protect the Software (PS); Produce Well-Secured Software (PW); Respond to Vulnerabilities (RV)
- url_oficial: https://csrc.nist.gov/pubs/sp/800/218/final
- novedades_2025_2026: SP 800-218 Rev. 1 (SSDF v1.2), initial public draft del 17-dic-2025, comentarios cerrados el 30-ene-2026 (https://csrc.nist.gov/pubs/sp/800/218/r1/ipd).
- verificado: si · nota: PW.3 figura como «Moved to PW.4». 800-218A (perfil para IA generativa y modelos fundacionales de uso dual) es final desde jul-2024.

**12. NIST — SP 800-161 Rev. 1 (C-SCRM)**
- version_vigente: Rev. 1 Update 1 · fecha: may-2022, con actualizaciones al 2024-11-01 · estado: final
- estructura_cantidad: no relevada · estructura_nombres: []
- url_oficial: https://csrc.nist.gov/pubs/sp/800/161/r1/upd1/final
- novedades_2025_2026: versión rellenable del SCRM Assessment Scoping Questionnaire (2-dic-2025).
- verificado: si · nota: solo se pidió el estado.

**13. NIST — SP 800-55 Vol. 1 y Vol. 2**
- version_vigente: Vol. 1 y Vol. 2 · fecha: 2024-12-04 · estado: final (reemplazan a SP 800-55 Rev. 1 de 2008)
- estructura_cantidad: 2 volúmenes
- estructura_nombres: Volume 1 — Identifying and Selecting Measures; Volume 2 — Developing an Information Security Measurement Program
- url_oficial: https://csrc.nist.gov/pubs/sp/800/55/v1/final
- novedades_2025_2026: ninguna.
- verificado: si · nota: Vol. 2 en https://csrc.nist.gov/pubs/sp/800/55/v2/final.

**14. NIST — SP 800-82 Rev. 3 (OT)**
- version_vigente: Rev. 3 · fecha: sep-2023 · estado: final, con Rev. 4 en borrador
- estructura_cantidad: no relevada · estructura_nombres: []
- url_oficial: https://csrc.nist.gov/pubs/sp/800/82/r3/final
- novedades_2025_2026: Rev. 4 initial public draft del 21-sep-2026, comentarios hasta el 30-nov-2026 (https://csrc.nist.gov/pubs/sp/800/82/r4/ipd). Se reestructura sobre CSF 2.0, suma sectores (edificios, agua, alimentos, ferrocarril de carga, marítimo, IIoT y nube) y aplica principios de zero trust.
- verificado: si · nota: el historial de Rev. 4 lista también una entrada de borrador del 22-ene-2026.

**15. NIST — FIPS 203, 204, 205 (y en curso)**
- version_vigente: FIPS 203 ML-KEM; FIPS 204 ML-DSA; FIPS 205 SLH-DSA · fecha: 2024-08-13 · estado: finales
- estructura_cantidad: 3 estándares publicados; 2 en desarrollo
- estructura_nombres: en desarrollo: FIPS 206 FN-DSA (derivado de FALCON) y un FIPS para HQC (seleccionado el 11-mar-2025)
- url_oficial: https://csrc.nist.gov/projects/post-quantum-cryptography
- novedades_2025_2026:
  - SP 800-227 final (18-sep-2025).
  - SP 800-230 en borrador (13-abr-2026), parámetros adicionales de SLH-DSA.
  - IR 8610 (14-may-2026): 9 candidatos pasan a la tercera ronda de firmas adicionales.
  - Erratas pendientes en FIPS 203 (17-nov-2025) y FIPS 204 (31-jul-2026).
- verificado: parcial · nota: no hay borrador publicado de FIPS 206 ni del FIPS de HQC; la página dice «in development».

**15b. NIST — IR 8547 (transición poscuántica)**
- version_vigente: final · fecha: 2026-10-27 · estado: final (reemplaza al borrador del 12-nov-2024)
- estructura_cantidad: 2 hitos generales y 3 plazos federales anticipados
- estructura_nombres:
  - «Deprecated after 2030» y «Disallowed after 2035» para ECDSA, EdDSA y RSA (firmas, FIPS 186).
  - Los mismos hitos para Finite Field DH/MQV, Elliptic Curve DH/MQV (SP 800-56A) y RSA (SP 800-56B) en establecimiento de claves.
  - Sistemas federales de alto valor o alto impacto: establecimiento de claves poscuántico al 31-dic-2030 y firmas al 31-dic-2031 (EO 14412 y OMB M-26-15).
  - TLS 1.3 al 2-ene-2030.
- url_oficial: https://csrc.nist.gov/pubs/ir/8547/final
- novedades_2025_2026: recomienda ML-KEM-768 como conjunto de parámetros por defecto.
- verificado: si · nota: que el borrador de 2024 solo deprecaba el nivel de 112 bits lo dicen análisis de terceros; no lo contrasté con el borrador.

**16. NIST — SP 800-63-4 (identidad digital)**
- version_vigente: Revision 4 · fecha: 2025-07-31 · estado: final (reemplaza a SP 800-63-3)
- estructura_cantidad: 4 volúmenes
- estructura_nombres: SP 800-63-4; SP 800-63A-4; SP 800-63B-4; SP 800-63C-4
- url_oficial: https://csrc.nist.gov/pubs/sp/800/63/4/final
- novedades_2025_2026: Implementation Resource Hub disponible (6-oct-2026).
- verificado: si · nota: —

**17. CISA — Zero Trust Maturity Model**
- version_vigente: 2.0 · fecha: abr-2023 (la página de recurso dice 11-abr-2023) · estado: final, sin versión posterior
- estructura_cantidad: 5 pilares, 3 capacidades transversales, 4 etapas
- estructura_nombres:
  - Pilares: Identity; Devices; Networks; Applications and Workloads; Data.
  - Transversales: Visibility and Analytics; Automation and Orchestration; Governance.
  - Etapas: Traditional; Initial; Advanced; Optimal.
- url_oficial: https://www.cisa.gov/zero-trust-maturity-model
- novedades_2025_2026: ninguna versión nueva.
- verificado: si · nota: la página está marcada «Archived Content».

**18. CISA — Cross-Sector Cybersecurity Performance Goals**
- version_vigente: 2.0 · fecha: 2025-12-11 · estado: final (reemplaza a 1.0.1)
- estructura_cantidad: 6 funciones y 34 metas (Govern 5, Identify 5, Protect 19, Detect 2, Respond 2, Recover 1)
- estructura_nombres: Govern (1); Identify (2); Protect (3); Detect (4); Respond (5); Recover (6)
- url_oficial: https://www.cisa.gov/cross-sector-cybersecurity-performance-goals
- novedades_2025_2026: agrega Govern, unifica metas de IT y OT, suma metas sobre proveedores de servicios gestionados, mínimo privilegio y comunicación de incidentes. Publica los primeros Sector-Specific Goals: químico, energía, servicios financieros, salud y TI.
- verificado: si · nota: las 34 metas son conteo propio sobre https://www.cisa.gov/cybersecurity-performance-goals-2-0-cpg-2-0; no abrí el PDF del informe.

**19. CISA — Directiva sobre vulnerabilidades explotadas y catálogo KEV**
- version_vigente: BOD 26-04 «Prioritizing Security Updates Based on Risk» · fecha: 2026-06-10 · estado: vigente; revoca BOD 19-02 y BOD 22-01
- estructura_cantidad: 4 variables de priorización y 3 fases
- estructura_nombres:
  - Variables: Asset Exposure; KEV Status; Exploit Automation; Technical Impact.
  - Fases: I (inmediata); II (60 días); III (180 días).
- url_oficial: https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk
- novedades_2025_2026: KEV sigue vigente con 1.781 entradas (última alta el 13-nov-2026). Cada entrada indica si exige «forensic triage» según BOD 26-04, con plazo de 3 días.
- verificado: si · nota: catálogo en https://www.cisa.gov/known-exploited-vulnerabilities-catalog.

**20. DoD — Zero Trust**
- version_vigente: DoD Zero Trust Strategy v1.0 · fecha: 2022-10-21 · estado: vigente
- estructura_cantidad: 7 pilares
- estructura_nombres: User; Device; Application & Workload; Data; Network & Environment; Automation & Orchestration; Visibility & Analytics
- url_oficial: https://dodcio.defense.gov/Portals/0/Documents/Library/DoD-ZTStrategy.pdf
- novedades_2025_2026:
  - DTM 25-003 «Implementing the DoD Zero Trust Strategy» (17-jul-2025, con vencimiento declarado el 17-jul-2026).
  - «Zero Trust for Operational Technology Activities and Outcomes» (versión OT.1.3, 25-sep-2025).
  - Guía conjunta «Adapting Zero Trust Principles to Operational Technology» (30-abr-2026).
- verificado: parcial · nota: no pude verificar una «Strategy 2.0» ni el sucesor de la DTM. Las páginas oficiales ya usan «Department of War».

**21. DoD — CMMC**
- version_vigente: «CMMC Program»; Model Overview v2.13 · fecha: sep-2024 (modelo); Fase 1 desde 2025-11-10 · estado: pausado en Fase 1; Fase II suspendida el 2026-07-13
- estructura_cantidad: 3 niveles (hoy solo se exigen 2, por autoevaluación) y 14 dominios
- estructura_nombres:
  - Niveles: Level 1: Basic Safeguarding of FCI (15 requisitos, FAR 52.204-21); Level 2: Broad Protection of CUI (110 requisitos, NIST SP 800-171 Rev. 2); Level 3 (24 requisitos de NIST SP 800-172).
  - Dominios: Access Control (AC); Awareness & Training (AT); Audit & Accountability (AU); Configuration Management (CM); Identification & Authentication (IA); Incident Response (IR); Maintenance (MA); Media Protection (MP); Personnel Security (PS); Physical Protection (PE); Risk Assessment (RA); Security Assessment (CA); System and Communications Protection (SC); System and Information Integrity (SI).
- url_oficial: https://dodcio.defense.gov/CMMC/About/
- novedades_2025_2026: la suspensión crea un grupo de reforma de CMMC. Durante la pausa se exige NIST SP 800-171 Rev. 2 por autoevaluación y evaluaciones gubernamentales selectas; las evaluaciones por terceros de Level 2 y las de Level 3 no pueden designarse.
- verificado: parcial · nota: el nombre descriptivo de Level 3 no figura en la página actual.

**22. SEC — Reglas de divulgación de ciberseguridad (2023)**
- version_vigente: Release 33-11216 · fecha: adoptada 2023-07-26; efectiva 2023-09-05 · estado: vigente, sin enmienda ni rescisión propuesta o adoptada
- estructura_cantidad: 2 componentes
- estructura_nombres: Form 8-K Item 1.05 (Material Cybersecurity Incidents); Regulation S-K Item 106 (gestión de riesgos, estrategia y gobierno)
- url_oficial: https://www.sec.gov/rules-regulations/2023/07/s7-09-22
- novedades_2025_2026:
  - Petición 4-856 (22-may-2025) de asociaciones bancarias para rescindir Item 1.05.
  - Revisión integral de Regulation S-K anunciada el 13-ene-2026 (expediente CLL-15), sin mención expresa de ciberseguridad.
  - Siguen presentándose 8-K bajo Item 1.05 en 2026.
- verificado: si · nota: Item 106 figura en eCFR al 12-nov-2026. No se revisó la agenda regulatoria ni la respuesta de la SEC a la petición.

## Artefactos nuevos 2025–2026 fuera de la lista

1. **CISA BOD 26-02**, «Mitigating Risk From End-of-Support Edge Devices» (fecha no verificada): https://www.cisa.gov/news-events/directives
2. **NIST AI 800-5** (final, 18-may-2026), consideraciones de seguridad para agentes de IA: https://www.nist.gov/publications/summary-analysis-responses-request-information-regarding-security-considerations-ai
3. **NIST AI 800-2** (initial public draft, ene-2026), evaluaciones automatizadas de modelos y agentes: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.800-2.ipd.pdf
4. **Concept paper del NCCoE** sobre identidad y autorización de software y agentes de IA (feb-2026): https://www.nccoe.nist.gov/sites/default/files/2026-02/accelerating-the-adoption-of-software-and-ai-agent-identity-and-authorization-concept-paper.pdf
5. **Concept Note: AI RMF Profile on Trustworthy AI in Critical Infrastructure** (7-abr-2026): https://www.nist.gov/programs-projects/concept-note-ai-rmf-profile-trustworthy-ai-critical-infrastructure
6. **NIST AI 100-2 E2025**, taxonomía de ataques y mitigaciones de aprendizaje automático adversario (final, 24-mar-2025): https://csrc.nist.gov/Projects/cosis/publications
7. **SP 800-221r1** (borrador, comentarios hasta el 7-dic-2026), riesgo de tecnologías de la información y comunicación dentro del portafolio de riesgo empresarial: https://www.nist.gov/cyberframework
8. **Guía conjunta «Adapting Zero Trust Principles to Operational Technology»** (30-abr-2026): https://dodcio.defense.gov/In-the-News/Article/4473613/cisa-and-us-government-partners-unveil-guide-to-accelerate-zero-trust-adoption/

## 8 hallazgos para la taxonomía

1. **Las 6 funciones siguen firmes.** CSF 2.0 no cambió y los artefactos nuevos se alinean a él: SP 800-61 Rev. 3, el borrador de SP 800-82 Rev. 4, CPG 2.0 y el Cyber AI Profile. No hace falta una séptima función.
2. **Hay que mapear alias AI/SI.** NIST está actualizando sus comunicaciones para incorporar «super intelligence», y COSIS, «Cyber SI Profile», CAISSI y «SI Agent Standards Initiative» ya usan el término. Los documentos previos conservan «AI».
3. **La seguridad de IA ya tiene estructura propia.** Las tres áreas Secure/Defend/Thwart y los cinco casos de uso de COSIS, incluidos agente único y multiagente, son la base para un dominio o subdominios de IA y de agentes.
4. **La gestión de vulnerabilidades cambió de modelo.** BOD 26-04 prioriza por exposición, estado en KEV, automatización del exploit e impacto técnico, y agrega triage forense. El dominio debería cubrir exposición y triage, no solo parcheo.
5. **La migración poscuántica tiene fechas firmes.** Deprecación después de 2030, prohibición después de 2035 y plazos federales de 2030 y 2031 justifican un subdominio de agilidad criptográfica e inventario.
6. **OT pasa a ser transversal.** CPG 2.0 unifica metas de IT y OT, el borrador de SP 800-82 Rev. 4 se reorganiza sobre CSF 2.0 y aparecen guías de zero trust para OT. Conviene tratar OT como dimensión que cruza dominios.
7. **NICE ofrece una lista de control de dominios.** Sus 11 áreas de competencia (IA, nube, criptografía, ciberresiliencia, DevSecOps, OT, cadena de suministro, entre otras) y el nuevo rol de C-SCRM sirven para contrastar los 24 dominios.
8. **El frente regulatorio es inestable.** CMMC quedó pausado en Fase 1 y la regla de la SEC sigue vigente pero con pedidos de rescisión de Item 1.05. Los modelos de zero trust no cambiaron (5 y 7 pilares). El dominio de cumplimiento necesita estado y fecha por artefacto.

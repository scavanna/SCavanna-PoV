# Mapeo GM-24 V7.1 (379 conceptos) → NIST · ISACA · MITRE · OWASP · CIS · CSA

> **GM-24 V7.1 · The Next CISO + Sub-plan PO-GAC** · 2026-11-14. Catálogo: 379 conceptos (245 K · 52 AMP · 40 HC · 42 PA), todos con pre-ensayo íntegro y mapeados a 17 marcos (NIST/ISACA/MITRE/OWASP/CIS/CSA). V7.1 = ChangeSet editorial CS-GM24-V7.1-001 (4 títulos generalizados; sin cambio de IDs, cantidad ni mapeo). Plano A (corpus académico). Referencias DD/K4x/R/eo:OP/COE: marco interno.

## 1. Método

Herencia de unidad (◐ Parcial) → reglas por palabra clave sobre K (53 reglas; 245/245) → explícitos AMP (52), HC (40), PA (42). Vínculo: cubre | instancia | referencia. No afirma conformidad (AMP-08). IDs validados contra `estandares.py` (0 desconocidos). **V7.1 no cambia el mapeo.**

## 2. Marcos y fuentes

| Clave | Marco / versión | Fuente |
|---|---|---|
| NIST-CSF | NIST Cybersecurity Framework 2.0 (feb-2024): 6 funciones, 22 categorías | https://www.nist.gov/cyberframework |
| NIST-RMF | NIST SP 800-37 Rev. 2 RMF: 7 pasos | https://csrc.nist.gov/pubs/sp/800/37/r2/final |
| NIST-53 | NIST SP 800-53 Rev. 5: 20 familias | https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final |
| NIST-AIRMF | NIST AI RMF 1.0 (ene-2023) GOVERN/MAP/MEASURE/MANAGE; NIST AI 600-1 perfil GenAI (jul-2024): 12 riesgos | https://www.nist.gov/itl/ai-risk-management-framework |
| NIST-OTROS | SP 800-61 Rev. 3, SP 800-207, SP 800-161 Rev. 1, SP 800-30, SP 800-84, Privacy Framework 1.0 | https://csrc.nist.gov |
| ISACA-CISM | CISM ECO 2026 (vigente 3-nov-2026; 18/20/33/29 %; + arquitectura empresarial y de seguridad) | https://www.isaca.org/credentialing/cism |
| ISACA-CRISC | CRISC ECO 2025 (vigente 3-nov-2025; 26/22/32/20 %; 9 subdominios) | https://www.isaca.org/credentialing/crisc |
| ISACA-AAISM | ISACA AAISM (ago-2025): 3 dominios (31/31/38 %), 13 subdominios | https://www.isaca.org/credentialing/aaism |
| MITRE | ATT&CK Enterprise (14 tácticas); ATLAS (tácticas IA); D3FEND (7 tácticas defensivas); Engage | https://attack.mitre.org · https://atlas.mitre.org · https://d3fend.mitre.org |
| OWASP | Top 10 for LLM Applications 2025 (LLM01–10); Top 10 for Agentic Applications 2026 v2.01 (ASI01–10); SAMM v2; ASVS; Top 10 for NHI | https://genai.owasp.org · https://owaspsamm.org |
| CIS | CIS Critical Security Controls v8.1 (18); CIS Benchmarks (incl. Microsoft 365 Foundations); CIS RAM | https://www.cisecurity.org/controls |
| CSA | CCM v4.x (17 dominios); AI Controls Matrix v1.1 (18 dominios, 247 objetivos; AIS-11, IAM-19, MDS); MAESTRO; STAR / STAR for AI; Zero Trust Advancement Center; NIST AI RMF Agentic Profile (borrador) | https://cloudsecurityalliance.org |

## 3. Resumen de cobertura

| Marco | Elementos | Con fuerte | Solo parcial/informativa | Sin cobertura |
|---|---|---|---|---|
| NIST CSF 2.0 | 22 | 22 | 0 | 0 |
| NIST RMF | 7 | 7 | 0 | 0 |
| NIST SP 800-53 | 20 | 20 | 0 | 0 |
| NIST AI RMF | 19 | 19 | 0 | 0 |
| NIST AI 600-1 | 12 | 10 | 0 | 2 |
| ISACA CISM 2026 | 8 | 8 | 0 | 0 |
| ISACA CRISC 2025 | 9 | 9 | 0 | 0 |
| ISACA AAISM | 13 | 13 | 0 | 0 |
| MITRE ATT&CK | 14 | 14 | 0 | 0 |
| MITRE ATLAS | 14 | 14 | 0 | 0 |
| MITRE D3FEND | 7 | 7 | 0 | 0 |
| OWASP LLM Top 10 2025 | 10 | 10 | 0 | 0 |
| OWASP Agentic Top 10 2026 | 10 | 10 | 0 | 0 |
| OWASP SAMM | 5 | 5 | 0 | 0 |
| CIS Controls v8.1 | 18 | 18 | 0 | 0 |
| CSA CCM v4 | 17 | 17 | 0 | 0 |
| CSA AICM | 4 | 4 | 0 | 0 |

Residual sin cobertura fuerte: GAI-CBRN y GAI-Env (AI 600-1), declarados fuera del alcance del rol en AMP-52.

## 4. Cobertura por elemento

### NIST CSF 2.0

| Elemento | Nombre | Fuerte (n) | Fuerte (IDs) | Parcial (n) |
|---|---|---|---|---|
| GV.OC | Organizational Context | 119 | G1.1-K01, G1.1-K02, G1.1-K03, G1.1-K04, G1.1-K05, G1.1-K06, G1.1-K07, G1.1-K08, G1.2-K01, G1.2-K02, G1.2-K03, G1.2-K04, G1.2-K05, G1.2-K06, G1.2-K07, G1.2-K08, G1.2-K09, G1.2-K10, G2.1-K09, G2.2-K05, G3.1-K01, G3.1-K02, G3.1-K03, G3.1-K04, G3.1-K05 … | 32 |
| GV.RM | Risk Management Strategy | 86 | G1.1-K04, G1.1-K06, G1.1-K07, G1.1-K08, G1.2-K01, G1.2-K02, G1.2-K03, G1.2-K04, G1.2-K05, G1.2-K06, G1.2-K07, G1.2-K08, G1.2-K09, G2.1-K09, G2.2-K09, G3.2-K03, G3.2-K05, G4.1-K01, G4.1-K02, G4.1-K04, G4.1-K05, G4.1-K06, G4.1-K07, G4.1-K09, G4.2-K01 … | 17 |
| GV.RR | Roles, Responsibilities, and Authorities | 58 | G1.1-K01, G1.1-K02, G1.1-K03, G1.1-K05, G1.1-K09, G3.2-K01, G3.2-K03, G4.1-K03, G4.1-K08, G4.1-K09, G5.1-K01, G5.2-K01, G6.1-K10, G6.2-K01, G6.2-K02, G6.2-K03, G6.2-K04, G6.2-K06, G6.2-K10, M1.1-K01, M1.1-K02, M1.1-K03, M1.1-K05, M1.1-K06, M1.2-K02 … | 44 |
| GV.PO | Policy | 37 | G2.1-K01, G2.1-K02, G2.1-K03, G2.1-K04, G2.1-K05, G2.1-K06, G2.1-K07, G2.2-K01, G2.2-K02, G2.2-K03, G2.2-K04, G2.2-K06, G2.2-K07, G2.2-K08, G2.2-K09, M3.2-K08, M6.2-K06, AMP-06, AMP-07, AMP-08, AMP-09, AMP-10, HC-004, HC-012, HC-013 … | 25 |
| GV.OV | Oversight | 85 | G1.2-K10, G2.1-K01, G2.1-K02, G2.1-K03, G2.1-K04, G2.1-K05, G2.1-K06, G2.1-K07, G2.1-K08, G2.2-K03, G2.2-K05, G2.2-K10, G3.1-K09, G3.2-K02, G3.2-K03, G3.2-K06, G3.2-K07, G3.2-K08, G4.1-K03, G4.1-K08, G4.1-K09, G4.1-K10, G4.2-K04, G4.2-K05, G4.2-K07 … | 33 |
| GV.SC | Cybersecurity Supply Chain Risk Management | 44 | G1.1-K09, G1.2-K01, G2.2-K02, G3.2-K06, G4.2-K02, G4.2-K06, G5.2-K05, G6.1-K01, G6.2-K04, M1.2-K03, M3.1-K10, M4.1-K08, M4.1-K09, M5.1-K02, M5.2-K10, M6.1-K03, M6.2-K01, M6.2-K02, M6.2-K03, M6.2-K04, M6.2-K07, M6.2-K08, M6.2-K09, M6.2-K10, AMP-07 … | 26 |
| ID.AM | Asset Management | 20 | M2.1-K01, M2.1-K02, M2.1-K03, M2.1-K08, M2.1-K09, M5.1-K05, M6.2-K05, M6.2-K06, AMP-31, AMP-33, AMP-49, AMP-51, HC-011, HC-014, HC-016, HC-030, G2.1-K11, G2.1-PA01, G2.2-PA02, M2.1-PA01 | 8 |
| ID.RA | Risk Assessment | 68 | G1.1-K09, G1.2-K01, G3.2-K06, G4.1-K05, G4.1-K06, G4.2-K02, G4.2-K06, G5.1-K02, G5.1-K04, G5.1-K05, G5.1-K06, G5.1-K07, G5.1-K08, G5.1-K09, G5.2-K04, G5.2-K05, G5.2-K09, G5.2-K10, G6.1-K01, G6.2-K04, M3.1-K10, M3.2-K04, M3.2-K06, M3.2-K07, M3.2-K09 … | 13 |
| ID.IM | Improvement | 71 | G1.1-K10, G2.1-K08, G2.2-K10, G3.1-K09, G3.2-K02, G3.2-K03, G3.2-K07, G3.2-K08, G4.2-K03, G4.2-K09, G5.1-K10, G5.2-K09, G5.2-K10, G6.1-K06, G6.1-K08, G6.2-K05, G6.2-K06, G6.2-K07, G6.2-K08, M1.1-K07, M1.1-K09, M1.1-K10, M2.1-K09, M2.2-K08, M3.2-K01 … | 31 |
| PR.AA | Identity Management, Authentication, and Access Control | 30 | G5.2-K03, M2.2-K01, M2.2-K02, M2.2-K03, M2.2-K04, M2.2-K05, M2.2-K06, M2.2-K07, M2.2-K08, M2.2-K09, M2.2-K10, M3.1-K03, M3.1-K06, M3.1-K09, AMP-18, AMP-28, AMP-32, AMP-33, AMP-34, AMP-36, AMP-50, HC-009, HC-010, HC-015, HC-038 … | 1 |
| PR.AT | Awareness and Training | 17 | G1.1-K05, G1.1-K09, G6.2-K01, M1.2-K04, M1.2-K05, M1.2-K06, M1.2-K07, M1.2-K08, M1.2-K09, AMP-29, AMP-30, HC-025, HC-037, G2.1-K11, G2.1-PA01, M1.2-PA03, M4.2-PA01 | 9 |
| PR.DS | Data Security | 15 | G3.1-K02, G3.1-K06, M2.1-K05, M2.1-K06, M2.1-K07, M2.1-K10, AMP-11, AMP-31, AMP-32, AMP-42, HC-011, HC-024, HC-033, G2.1-K11, G2.1-PA01 | 31 |
| PR.PS | Platform Security | 61 | G2.2-K02, G4.2-K03, M2.2-K05, M2.2-K06, M3.1-K01, M3.1-K02, M3.1-K03, M3.1-K04, M3.1-K05, M3.1-K06, M3.1-K07, M3.1-K08, M3.1-K09, M3.1-K10, M3.2-K01, M3.2-K02, M3.2-K03, M3.2-K05, M3.2-K10, M6.2-K02, M6.2-K03, M6.2-K05, M6.2-K09, AMP-09, AMP-28 … | 25 |
| PR.IR | Technology Infrastructure Resilience | 32 | M3.1-K01, M3.1-K02, M3.1-K03, M3.1-K04, M3.1-K05, M3.1-K07, M3.1-K08, M3.1-K09, M3.1-K10, M5.1-K09, M5.1-K10, M6.1-K01, M6.1-K02, M6.1-K03, M6.1-K04, M6.1-K05, M6.1-K06, M6.1-K07, M6.1-K08, M6.1-K10, AMP-47, AMP-48, HC-007, HC-023, HC-025 … | 16 |
| DE.CM | Continuous Monitoring | 25 | G5.1-K05, M3.1-K07, M4.1-K01, M4.1-K02, M4.1-K03, M4.1-K04, M4.1-K06, M4.1-K07, M4.1-K09, M4.1-K10, M4.2-K10, AMP-46, AMP-51, HC-017, HC-018, HC-040, G2.1-K11, M4.1-K11, M4.2-K11, G2.1-PA01, G4.2-PA01, M3.1-PA02, M4.1-PA01, M4.1-PA04, M4.1-PA05 | 12 |
| DE.AE | Adverse Event Analysis | 19 | G5.1-K05, M4.1-K01, M4.1-K02, M4.1-K04, M4.1-K05, M4.1-K06, M4.1-K08, AMP-39, AMP-41, HC-019, G2.1-K11, M4.1-K11, G2.1-PA01, M4.1-PA01, M4.1-PA02, M4.1-PA03, M4.1-PA04, M4.1-PA05, M4.2-PA01 | 30 |
| RS.MA | Incident Management | 18 | M5.1-K01, M5.1-K02, M5.1-K03, M5.1-K04, M5.1-K05, M5.1-K06, M5.1-K07, M5.1-K08, AMP-43, AMP-44, HC-017, HC-020, HC-022, G2.1-K11, G2.1-PA01, M4.1-PA01, M4.1-PA02, M5.1-PA01 | 7 |
| RS.AN | Incident Analysis | 21 | G6.1-K08, M4.1-K08, M5.2-K01, M5.2-K02, M5.2-K03, M5.2-K04, M5.2-K05, M5.2-K06, M5.2-K07, M6.1-K02, M6.1-K09, AMP-39, AMP-45, AMP-46, HC-019, HC-035, G2.1-K11, G2.1-PA01, M4.1-PA02, M5.2-PA01, M5.2-PA02 | 28 |
| RS.CO | Incident Response Reporting and Communication | 48 | G1.2-K10, G2.2-K05, G3.1-K01, G3.1-K02, G3.1-K03, G3.1-K04, G3.1-K05, G3.1-K07, G3.1-K08, G3.1-K09, G3.1-K10, G3.2-K04, G3.2-K08, G3.2-K09, G3.2-K10, G4.1-K10, G4.2-K04, G4.2-K05, G4.2-K07, G5.2-K08, G6.1-K01, G6.1-K02, G6.1-K03, G6.1-K04, G6.1-K05 … | 15 |
| RS.MI | Incident Mitigation | 19 | G6.1-K08, M4.1-K05, M5.2-K01, M5.2-K02, M5.2-K03, M5.2-K04, M5.2-K05, M5.2-K06, M5.2-K07, M6.1-K02, M6.1-K09, AMP-39, AMP-40, AMP-44, HC-019, G2.1-K11, G2.1-PA01, M5.1-PA01, M5.2-PA01 | 9 |
| RC.RP | Incident Recovery Plan Execution | 21 | M4.2-K04, M4.2-K08, M5.1-K09, M5.1-K10, M6.1-K01, M6.1-K02, M6.1-K03, M6.1-K04, M6.1-K05, M6.1-K06, M6.1-K07, M6.1-K08, M6.1-K10, AMP-47, HC-007, HC-021, HC-030, G2.1-K11, M3.1-K12, G2.1-PA01, M6.1-PA01 | 6 |
| RC.CO | Incident Recovery Communication | 15 | G6.1-K08, M5.2-K01, M5.2-K02, M5.2-K03, M5.2-K04, M5.2-K05, M5.2-K06, M5.2-K07, M6.1-K02, M6.1-K09, HC-020, HC-021, HC-022, G2.1-K11, G2.1-PA01 | 9 |

### NIST RMF

| Elemento | Nombre | Fuerte (n) | Fuerte (IDs) | Parcial (n) |
|---|---|---|---|---|
| Prepare | Prepare | 47 | G1.1-K04, G1.1-K06, G1.1-K08, G1.2-K01, G1.2-K02, G1.2-K03, G1.2-K07, G1.2-K08, G1.2-K09, G2.1-K01, G2.1-K02, G2.1-K03, G2.1-K04, G2.1-K05, G2.1-K06, G2.1-K07, G2.1-K09, G2.2-K03, G3.2-K03, G3.2-K05, G4.1-K01, G4.1-K02, G4.1-K04, G4.1-K05, G4.1-K06 … | 98 |
| Categorize | Categorize | 8 | M2.1-K01, M2.1-K02, M2.1-K03, M2.1-K08, M2.1-K09, M5.1-K05, HC-014, M2.1-PA01 | 11 |
| Select | Select | 30 | G2.1-K01, G2.1-K02, G2.1-K03, G2.1-K04, G2.1-K05, G2.1-K06, G2.1-K07, G2.2-K03, G4.2-K03, M3.1-K01, M3.1-K02, M3.1-K03, M3.1-K04, M3.1-K05, M3.1-K08, M3.1-K09, M3.1-K10, M3.2-K01, M3.2-K02, M3.2-K03, M3.2-K05, M3.2-K08, M3.2-K10, HC-002, HC-036 … | 38 |
| Implement | Implement | 19 | G4.2-K03, M3.1-K01, M3.1-K02, M3.1-K03, M3.1-K04, M3.1-K05, M3.1-K08, M3.1-K09, M3.1-K10, M3.2-K01, M3.2-K02, M3.2-K03, M3.2-K05, M3.2-K10, HC-002, HC-036, M3.1-K11, M3.1-PA01, M3.2-PA01 | 32 |
| Assess | Assess | 36 | G2.2-K10, G3.1-K09, G3.2-K02, G3.2-K03, G3.2-K07, G4.1-K05, G4.1-K06, G5.1-K02, G5.1-K04, G5.1-K05, G5.1-K06, G5.1-K07, G5.1-K08, G5.1-K09, G5.1-K10, G5.2-K10, G6.2-K08, M1.1-K09, M2.1-K09, M2.2-K08, M3.2-K04, M3.2-K06, M3.2-K09, M4.1-K02, M4.2-K01 … | 35 |
| Authorize | Authorize | 13 | G4.2-K01, G4.2-K02, G4.2-K08, G4.2-K09, G4.2-K10, G5.2-K02, G5.2-K03, G5.2-K06, G5.2-K07, AMP-22, HC-003, HC-012, HC-028 | 8 |
| Monitor | Monitor | 26 | G1.1-K10, G2.1-K08, G2.2-K10, G3.1-K09, G3.2-K02, G3.2-K03, G3.2-K07, G5.1-K05, G5.1-K10, G5.2-K10, G6.2-K07, G6.2-K08, M1.1-K09, M1.1-K10, M2.1-K09, M2.2-K08, M4.1-K01, M4.1-K02, M4.1-K04, M4.1-K06, AMP-13, HC-005, HC-018, G3.2-PA01, M1.1-PA03 … | 32 |

### NIST SP 800-53

| Elemento | Nombre | Fuerte (n) | Fuerte (IDs) | Parcial (n) |
|---|---|---|---|---|
| AC | Access Control | 21 | G5.2-K03, M2.2-K01, M2.2-K02, M2.2-K03, M2.2-K04, M2.2-K07, M2.2-K08, M2.2-K09, M2.2-K10, M3.1-K07, M3.1-K09, AMP-32, AMP-33, AMP-34, AMP-36, AMP-50, HC-009, HC-011, HC-026, M4.2-K11, M2.2-PA01 | 6 |
| AT | Awareness and Training | 14 | G1.1-K05, G1.1-K09, G6.2-K01, M1.2-K04, M1.2-K05, M1.2-K06, M1.2-K07, M1.2-K08, M1.2-K09, AMP-29, HC-025, HC-037, M1.2-PA03, M4.2-PA01 | 10 |
| AU | Audit and Accountability | 37 | G2.2-K10, G3.1-K09, G3.2-K02, G3.2-K03, G3.2-K06, G3.2-K07, G5.1-K05, G5.1-K10, G5.2-K10, G6.1-K08, G6.2-K08, M1.1-K09, M2.1-K09, M2.2-K08, M4.1-K01, M4.1-K02, M4.1-K04, M4.1-K06, M5.2-K01, M5.2-K02, M5.2-K03, M5.2-K04, M5.2-K05, M5.2-K06, M5.2-K07 … | 36 |
| CA | Assessment, Authorization, and Monitoring | 56 | G2.2-K10, G3.1-K09, G3.2-K02, G3.2-K03, G3.2-K06, G3.2-K07, G4.2-K01, G4.2-K02, G4.2-K03, G4.2-K08, G4.2-K09, G4.2-K10, G5.1-K10, G5.2-K02, G5.2-K03, G5.2-K04, G5.2-K06, G5.2-K07, G5.2-K09, G5.2-K10, G6.2-K08, M1.1-K09, M2.1-K09, M2.2-K08, M3.2-K01 … | 33 |
| CM | Configuration Management | 31 | G4.2-K03, M2.1-K01, M2.1-K02, M2.1-K03, M2.1-K08, M2.1-K09, M3.2-K01, M3.2-K02, M3.2-K03, M3.2-K05, M3.2-K10, M5.1-K05, M6.2-K05, AMP-09, AMP-10, AMP-36, AMP-51, HC-004, HC-016, HC-030, HC-034, HC-040, G2.2-PA02, G2.2-PA03, G3.2-PA01 … | 31 |
| CP | Contingency Planning | 32 | M4.2-K04, M4.2-K08, M5.1-K01, M5.1-K02, M5.1-K03, M5.1-K04, M5.1-K05, M5.1-K06, M5.1-K07, M5.1-K08, M5.1-K09, M5.1-K10, M6.1-K01, M6.1-K02, M6.1-K03, M6.1-K04, M6.1-K05, M6.1-K06, M6.1-K07, M6.1-K08, M6.1-K10, AMP-43, AMP-47, AMP-48, HC-007 … | 7 |
| IA | Identification and Authentication | 15 | G5.2-K03, M2.2-K01, M2.2-K02, M2.2-K03, M2.2-K04, M2.2-K07, M2.2-K08, M2.2-K09, M2.2-K10, M3.1-K09, AMP-33, AMP-34, HC-009, M4.2-K11, M2.2-PA01 | 6 |
| IR | Incident Response | 38 | G5.1-K05, G6.1-K08, M4.1-K01, M4.1-K02, M4.1-K04, M4.1-K05, M4.1-K06, M5.1-K01, M5.1-K02, M5.1-K03, M5.1-K04, M5.1-K05, M5.1-K06, M5.1-K07, M5.1-K08, M5.2-K01, M5.2-K02, M5.2-K03, M5.2-K04, M5.2-K05, M5.2-K06, M5.2-K07, M6.1-K02, M6.1-K09, AMP-39 … | 29 |
| MA | Maintenance | 1 | M3.1-K12 | 0 |
| MP | Media Protection | 4 | M2.1-K05, M2.1-K06, M2.1-K07, M2.1-K10 | 14 |
| PE | Physical and Environmental Protection | 1 | M3.1-K12 | 0 |
| PL | Planning | 43 | G2.1-K01, G2.1-K02, G2.1-K03, G2.1-K04, G2.1-K05, G2.1-K06, G2.1-K07, G2.2-K01, G2.2-K02, G2.2-K03, G2.2-K04, G2.2-K06, G2.2-K07, G2.2-K08, G4.2-K03, M3.1-K01, M3.1-K02, M3.1-K03, M3.1-K04, M3.1-K05, M3.1-K08, M3.1-K09, M3.1-K10, M3.2-K01, M3.2-K02 … | 40 |
| PM | Program Management | 92 | G1.1-K04, G1.1-K06, G1.1-K07, G1.1-K08, G1.2-K01, G1.2-K02, G1.2-K03, G1.2-K04, G1.2-K05, G1.2-K06, G1.2-K07, G1.2-K08, G1.2-K09, G1.2-K10, G2.1-K01, G2.1-K02, G2.1-K03, G2.1-K04, G2.1-K05, G2.1-K06, G2.1-K07, G2.1-K08, G2.1-K09, G2.2-K03, G2.2-K05 … | 115 |
| PS | Personnel Security | 15 | G1.1-K05, G1.1-K09, G6.2-K01, M1.2-K04, M1.2-K05, M1.2-K06, M1.2-K07, M1.2-K08, M1.2-K09, AMP-29, HC-025, HC-026, HC-037, M1.1-PA01, M1.2-PA03 | 0 |
| PT | PII Processing and Transparency | 13 | G3.1-K02, G3.1-K06, M2.1-K05, M2.1-K06, M2.1-K07, M2.1-K10, AMP-11, AMP-31, AMP-32, HC-011, HC-024, HC-033, G3.1-PA01 | 21 |
| RA | Risk Assessment | 64 | G4.1-K05, G4.1-K06, G4.2-K01, G4.2-K02, G4.2-K08, G4.2-K09, G4.2-K10, G5.1-K02, G5.1-K04, G5.1-K05, G5.1-K06, G5.1-K07, G5.1-K08, G5.1-K09, G5.2-K02, G5.2-K03, G5.2-K04, G5.2-K06, G5.2-K07, G5.2-K09, G5.2-K10, M2.1-K01, M2.1-K02, M2.1-K03, M2.1-K08 … | 38 |
| SA | System and Services Acquisition | 39 | G2.2-K02, M1.2-K03, M3.1-K01, M3.1-K02, M3.1-K03, M3.1-K04, M3.1-K05, M3.1-K08, M3.1-K09, M3.1-K10, M4.2-K02, M4.2-K03, M4.2-K05, M4.2-K06, M4.2-K07, M4.2-K09, M6.2-K01, M6.2-K02, M6.2-K03, M6.2-K07, M6.2-K08, M6.2-K09, M6.2-K10, AMP-35, AMP-49 … | 36 |
| SC | System and Communications Protection | 24 | M2.1-K05, M2.1-K06, M2.1-K07, M2.1-K10, M3.1-K01, M3.1-K02, M3.1-K03, M3.1-K04, M3.1-K05, M3.1-K07, M3.1-K08, M3.1-K09, M3.1-K10, M6.2-K02, M6.2-K05, AMP-11, AMP-35, HC-011, HC-030, HC-033, M3.1-K11, M4.1-K11, M3.1-PA01, M3.1-PA02 | 31 |
| SI | System and Information Integrity | 37 | G2.2-K02, G5.1-K05, M3.2-K04, M3.2-K06, M3.2-K09, M4.1-K01, M4.1-K02, M4.1-K03, M4.1-K04, M4.1-K05, M4.1-K06, M4.1-K07, M4.1-K09, M4.1-K10, M4.2-K01, M4.2-K10, M6.2-K03, M6.2-K09, AMP-38, AMP-39, AMP-41, AMP-42, HC-017, HC-018, HC-019 … | 20 |
| SR | Supply Chain Risk Management | 18 | M1.2-K03, M6.2-K01, M6.2-K07, M6.2-K08, M6.2-K10, AMP-15, AMP-20, AMP-42, AMP-48, AMP-49, AMP-50, HC-008, HC-023, HC-029, HC-031, M1.2-PA02, M6.1-PA01, M6.2-PA01 | 14 |

### NIST AI RMF

| Elemento | Nombre | Fuerte (n) | Fuerte (IDs) | Parcial (n) |
|---|---|---|---|---|
| GOVERN-1 | Policies, processes, procedures and practices | 15 | M6.2-K06, AMP-06, AMP-17, AMP-25, AMP-27, AMP-30, AMP-33, AMP-46, HC-012, G2.1-PA02, G2.2-PA01, G2.2-PA02, G3.1-PA01, G6.2-PA01, M3.2-PA02 | 1 |
| GOVERN-2 | Accountability structures | 14 | AMP-03, AMP-06, AMP-12, AMP-17, AMP-22, AMP-26, AMP-29, AMP-40, HC-009, HC-010, G1.1-PA01, G2.1-PA02, G4.1-PA01, M1.1-PA01 | 7 |
| GOVERN-3 | Workforce diversity, equity, inclusion, accessibility | 4 | AMP-29, G2.1-PA02, M1.1-PA01, M1.2-PA03 | 0 |
| GOVERN-4 | Culture of risk | 3 | AMP-02, AMP-25, G2.1-PA02 | 6 |
| GOVERN-5 | Engagement with AI actors | 3 | AMP-23, G2.1-PA02, G6.1-PA01 | 0 |
| GOVERN-6 | Third-party and supply chain risks | 9 | AMP-12, AMP-48, AMP-49, AMP-50, HC-023, G2.1-PA02, M1.2-PA02, M6.2-PA01, M6.2-PA03 | 7 |
| MAP-1 | Context established | 24 | G1.1-K09, G1.2-K01, G3.2-K06, G4.2-K02, G4.2-K06, G5.2-K05, G6.1-K01, G6.2-K04, M3.1-K10, M4.1-K08, M4.1-K09, M5.1-K02, M5.2-K10, M6.1-K03, M6.2-K04, M6.2-K06, AMP-04, AMP-06, AMP-31, AMP-51, M4.2-K11, G2.1-PA02, G3.1-PA01, M2.1-PA01 | 1 |
| MAP-2 | Categorization of the AI system | 6 | AMP-28, AMP-35, G2.1-PA02, G2.2-PA02, M2.1-PA01, M3.1-PA01 | 0 |
| MAP-3 | Capabilities, usage, goals, benefits/costs | 8 | M4.1-K08, AMP-35, AMP-39, G1.2-PA01, G2.1-PA02, G2.2-PA02, M1.2-PA01, M3.1-PA01 | 0 |
| MAP-4 | Risks and benefits of components incl. third-party | 29 | G1.1-K09, G1.2-K01, G3.2-K06, G4.2-K02, G4.2-K06, G5.2-K05, G6.1-K01, G6.2-K04, M3.1-K10, M4.1-K08, M4.1-K09, M5.1-K02, M5.2-K10, M6.1-K03, M6.2-K04, AMP-15, AMP-20, AMP-32, AMP-41, AMP-42, AMP-48, AMP-49, HC-011, HC-032, M4.2-K11 … | 0 |
| MAP-5 | Impacts to individuals, groups, organizations, society | 6 | AMP-02, AMP-15, AMP-25, AMP-52, G2.1-PA02, G4.1-PA02 | 0 |
| MEASURE-1 | Appropriate methods and metrics | 9 | AMP-19, AMP-24, AMP-37, HC-027, G2.1-PA02, G4.2-PA01, G6.1-PA01, G6.2-PA01, M3.2-PA03 | 1 |
| MEASURE-2 | Trustworthy characteristics evaluated | 13 | AMP-14, AMP-19, AMP-20, AMP-26, AMP-37, AMP-38, AMP-41, HC-012, HC-032, AMP-52, G2.1-PA02, M3.2-PA03, M4.1-PA06 | 0 |
| MEASURE-3 | Mechanisms for tracking risks over time | 8 | AMP-13, AMP-45, AMP-46, AMP-51, G2.1-PA02, G4.2-PA01, M4.1-PA05, M4.1-PA06 | 2 |
| MEASURE-4 | Feedback on measurement efficacy | 7 | AMP-14, HC-027, G2.1-PA02, G6.2-PA01, M3.2-PA03, M4.1-PA06, M5.2-PA02 | 0 |
| MANAGE-1 | Risks prioritized, responded to and managed | 37 | G1.1-K09, G1.2-K01, G3.2-K06, G4.2-K02, G4.2-K06, G5.2-K05, G6.1-K01, G6.2-K04, M3.1-K10, M4.1-K08, M4.1-K09, M5.1-K02, M5.2-K10, M6.1-K03, M6.2-K04, AMP-17, AMP-18, AMP-22, AMP-26, AMP-28, AMP-32, AMP-34, AMP-36, AMP-39, AMP-40 … | 0 |
| MANAGE-2 | Strategies to maximize benefits and minimize negative impacts | 7 | AMP-04, AMP-21, AMP-30, AMP-47, HC-034, G2.1-PA02, M6.1-PA01 | 0 |
| MANAGE-3 | Third-party risks managed | 7 | AMP-20, AMP-42, AMP-49, AMP-50, G2.1-PA02, M1.2-PA02, M6.2-PA01 | 5 |
| MANAGE-4 | Risk treatments documented and monitored | 11 | AMP-18, AMP-38, AMP-43, AMP-44, HC-034, G2.1-PA02, G4.2-PA01, M1.2-PA01, M4.1-PA06, M5.2-PA02, M6.2-PA02 | 1 |

### NIST AI 600-1

| Elemento | Nombre | Fuerte (n) | Fuerte (IDs) | Parcial (n) |
|---|---|---|---|---|
| GAI-CBRN | CBRN information or capabilities | 0 |  | 0 |
| GAI-Confab | Confabulation | 7 | AMP-02, AMP-14, AMP-19, AMP-20, AMP-52, M3.2-PA03, M4.1-PA06 | 0 |
| GAI-Dangerous | Dangerous, violent or hateful content | 1 | AMP-52 | 0 |
| GAI-Privacy | Data privacy | 5 | AMP-11, AMP-31, AMP-32, HC-011, G3.1-PA01 | 0 |
| GAI-Env | Environmental impacts | 0 |  | 0 |
| GAI-Bias | Harmful bias and homogenization | 3 | AMP-20, AMP-25, AMP-52 | 0 |
| GAI-HAI | Human-AI configuration | 7 | AMP-02, AMP-14, AMP-18, AMP-25, AMP-26, AMP-40, G3.1-PA01 | 1 |
| GAI-InfoInt | Information integrity | 4 | AMP-19, AMP-32, AMP-42, AMP-52 | 0 |
| GAI-InfoSec | Information security | 2 | AMP-41, M4.2-PA02 | 16 |
| GAI-IP | Intellectual property | 1 | AMP-49 | 0 |
| GAI-Obscene | Obscene, degrading or abusive content | 1 | AMP-52 | 0 |
| GAI-ValueChain | Value chain and component integration | 5 | AMP-20, AMP-42, AMP-48, AMP-49, M6.2-PA01 | 16 |

### ISACA CISM 2026

| Elemento | Nombre | Fuerte (n) | Fuerte (IDs) | Parcial (n) |
|---|---|---|---|---|
| CISM-1A | D1 Governance · A Enterprise Governance | 74 | G1.1-K01, G1.1-K02, G1.1-K03, G1.1-K05, G1.2-K10, G2.2-K05, G3.1-K01, G3.1-K02, G3.1-K03, G3.1-K04, G3.1-K05, G3.1-K07, G3.1-K08, G3.1-K09, G3.1-K10, G3.2-K03, G3.2-K04, G3.2-K08, G3.2-K09, G3.2-K10, G4.1-K03, G4.1-K08, G4.1-K09, G4.1-K10, G4.2-K04 … | 26 |
| CISM-1B | D1 · B Information Security Strategy (2026: + enterprise architecture, information governance) | 66 | G1.1-K04, G1.1-K06, G1.1-K07, G1.1-K08, G1.2-K01, G1.2-K02, G1.2-K03, G1.2-K04, G1.2-K05, G1.2-K06, G1.2-K07, G1.2-K08, G1.2-K09, G2.1-K01, G2.1-K02, G2.1-K03, G2.1-K04, G2.1-K05, G2.1-K06, G2.1-K07, G2.1-K09, G2.2-K03, G3.2-K03, G3.2-K05, G4.1-K01 … | 8 |
| CISM-2A | D2 Risk Management · A Risk Identification and Assessment | 35 | G4.1-K05, G4.1-K06, G5.1-K02, G5.1-K04, G5.1-K05, G5.1-K06, G5.1-K07, G5.1-K08, G5.1-K09, M4.1-K02, M4.1-K03, M4.1-K07, M4.1-K09, M4.1-K10, M4.2-K02, M4.2-K03, M4.2-K04, M4.2-K05, M4.2-K06, M4.2-K07, M4.2-K08, M4.2-K09, M4.2-K10, AMP-15, AMP-20 … | 21 |
| CISM-2B | D2 · B Risk Response | 23 | G4.2-K01, G4.2-K02, G4.2-K08, G4.2-K09, G4.2-K10, G5.2-K02, G5.2-K03, G5.2-K04, G5.2-K06, G5.2-K07, G5.2-K09, G5.2-K10, M3.2-K07, AMP-17, AMP-22, HC-002, HC-003, HC-007, HC-010, HC-027, HC-028, HC-040, G4.2-PA01 | 11 |
| CISM-3A | D3 Program · A Program Development (2026: + information security architecture) | 82 | G2.2-K01, G2.2-K02, G2.2-K04, G2.2-K06, G2.2-K07, G2.2-K08, G3.2-K01, G4.2-K03, G5.2-K03, G6.2-K06, M1.1-K01, M1.1-K02, M1.1-K03, M1.1-K05, M1.1-K06, M1.2-K02, M2.1-K01, M2.1-K02, M2.1-K03, M2.1-K04, M2.1-K08, M2.1-K09, M2.2-K01, M2.2-K02, M2.2-K03 … | 57 |
| CISM-3B | D3 · B Program Management | 82 | G1.1-K05, G1.1-K07, G1.1-K09, G1.1-K10, G1.2-K04, G1.2-K05, G1.2-K06, G2.1-K08, G3.2-K01, G3.2-K08, G4.1-K07, G4.2-K09, G5.2-K09, G6.1-K06, G6.2-K01, G6.2-K05, G6.2-K06, G6.2-K07, G6.2-K09, M1.1-K01, M1.1-K02, M1.1-K03, M1.1-K05, M1.1-K06, M1.1-K07 … | 49 |
| CISM-4A | D4 Incident Management · A Readiness | 30 | M5.1-K01, M5.1-K02, M5.1-K03, M5.1-K04, M5.1-K05, M5.1-K06, M5.1-K07, M5.1-K08, M5.1-K09, M5.1-K10, M6.1-K01, M6.1-K02, M6.1-K03, M6.1-K04, M6.1-K05, M6.1-K06, M6.1-K07, M6.1-K08, M6.1-K10, AMP-43, AMP-44, AMP-47, HC-007, HC-020, HC-022 … | 7 |
| CISM-4B | D4 · B Operations | 42 | G5.1-K05, G6.1-K08, M4.1-K01, M4.1-K02, M4.1-K03, M4.1-K04, M4.1-K05, M4.1-K06, M4.1-K07, M4.1-K08, M4.1-K09, M4.1-K10, M4.2-K10, M5.2-K01, M5.2-K02, M5.2-K03, M5.2-K04, M5.2-K05, M5.2-K06, M5.2-K07, M6.1-K02, M6.1-K09, AMP-39, AMP-40, AMP-44 … | 8 |

### ISACA CRISC 2025

| Elemento | Nombre | Fuerte (n) | Fuerte (IDs) | Parcial (n) |
|---|---|---|---|---|
| CRISC-1A | D1 Governance · A Organizational Governance | 114 | G1.1-K01, G1.1-K02, G1.1-K03, G1.1-K04, G1.1-K05, G1.1-K06, G1.1-K07, G1.1-K08, G1.2-K01, G1.2-K02, G1.2-K03, G1.2-K04, G1.2-K05, G1.2-K06, G1.2-K07, G1.2-K08, G1.2-K09, G2.1-K09, G2.2-K01, G2.2-K02, G2.2-K04, G2.2-K06, G2.2-K07, G2.2-K08, G3.2-K01 … | 67 |
| CRISC-1B | D1 · B Risk Governance | 83 | G1.1-K04, G1.1-K06, G1.1-K08, G1.2-K01, G1.2-K02, G1.2-K03, G1.2-K07, G1.2-K08, G1.2-K09, G2.1-K01, G2.1-K02, G2.1-K03, G2.1-K04, G2.1-K05, G2.1-K06, G2.1-K07, G2.1-K09, G2.2-K03, G3.1-K01, G3.1-K02, G3.1-K03, G3.1-K04, G3.1-K05, G3.1-K07, G3.1-K08 … | 34 |
| CRISC-2A | D2 Risk Assessment · A Risk Identification | 36 | G4.1-K05, G4.1-K06, G5.1-K02, G5.1-K04, G5.1-K05, G5.1-K06, G5.1-K07, G5.1-K08, G5.1-K09, M4.1-K02, M4.1-K03, M4.1-K07, M4.1-K09, M4.1-K10, M4.2-K01, M4.2-K02, M4.2-K03, M4.2-K04, M4.2-K05, M4.2-K06, M4.2-K07, M4.2-K08, M4.2-K09, M4.2-K10, AMP-15 … | 9 |
| CRISC-2B | D2 · B Risk Analysis | 13 | G4.1-K05, G4.1-K06, G5.1-K02, G5.1-K04, G5.1-K05, G5.1-K06, G5.1-K07, G5.1-K08, G5.1-K09, M4.1-K02, AMP-19, AMP-20, G4.1-PA02 | 7 |
| CRISC-3A | D3 Risk Response and Reporting · A Risk Response | 33 | G2.2-K09, G4.2-K01, G4.2-K02, G4.2-K08, G4.2-K09, G4.2-K10, G5.2-K02, G5.2-K03, G5.2-K04, G5.2-K06, G5.2-K07, G5.2-K09, G5.2-K10, G6.1-K08, M3.2-K07, M5.2-K01, M5.2-K02, M5.2-K03, M5.2-K04, M5.2-K05, M5.2-K06, M5.2-K07, M6.1-K02, M6.1-K09, AMP-10 … | 13 |
| CRISC-3B | D3 · B Control Design and Implementation | 32 | G4.2-K03, G5.2-K04, G5.2-K09, G5.2-K10, M3.2-K01, M3.2-K02, M3.2-K03, M3.2-K04, M3.2-K05, M3.2-K06, M3.2-K07, M3.2-K09, M3.2-K10, M4.2-K01, AMP-09, AMP-18, AMP-37, AMP-38, HC-002, HC-004, HC-024, HC-028, HC-031, HC-032, HC-034 … | 7 |
| CRISC-3C | D3 · C Risk Monitoring and Reporting | 72 | G1.1-K10, G1.2-K10, G2.1-K08, G2.2-K05, G3.2-K08, G4.1-K05, G4.1-K06, G4.1-K10, G4.2-K04, G4.2-K05, G4.2-K07, G4.2-K09, G5.1-K02, G5.1-K04, G5.1-K05, G5.1-K06, G5.1-K07, G5.1-K08, G5.1-K09, G5.2-K08, G5.2-K09, G6.1-K01, G6.1-K02, G6.1-K03, G6.1-K04 … | 43 |
| CRISC-4A | D4 Technology and Security · A Technology Principles | 26 | G2.2-K02, M3.1-K01, M3.1-K02, M3.1-K03, M3.1-K04, M3.1-K05, M3.1-K07, M3.1-K08, M3.1-K09, M3.1-K10, M6.2-K02, M6.2-K03, M6.2-K05, M6.2-K09, AMP-35, AMP-51, HC-002, HC-014, HC-030, HC-031, M3.1-K11, M3.1-K12, M3.1-PA01, M3.1-PA02, M6.2-PA01 … | 24 |
| CRISC-4B | D4 · B Information Security Principles | 27 | G5.1-K05, G5.2-K03, M2.2-K01, M2.2-K02, M2.2-K03, M2.2-K04, M2.2-K07, M2.2-K08, M2.2-K09, M2.2-K10, M3.1-K09, M4.1-K01, M4.1-K02, M4.1-K04, M4.1-K06, AMP-33, AMP-34, AMP-39, HC-009, HC-015, HC-019, M4.1-K11, M4.2-K11, M2.2-PA01, M4.1-PA01 … | 39 |

### ISACA AAISM

| Elemento | Nombre | Fuerte (n) | Fuerte (IDs) | Parcial (n) |
|---|---|---|---|---|
| AAISM-1A | D1 AI Governance and Program Management · A Stakeholders, frameworks, regulatory | 8 | AMP-03, AMP-06, AMP-11, AMP-12, HC-012, G2.1-PA02, G3.1-PA01, G4.1-PA01 | 46 |
| AAISM-1B | D1 · B AI strategies, policies, procedures | 9 | AMP-03, AMP-04, AMP-06, AMP-17, AMP-30, HC-010, G2.2-PA01, G2.2-PA02, M3.2-PA02 | 36 |
| AAISM-1C | D1 · C AI asset and data life cycle management | 7 | M6.2-K06, AMP-31, AMP-33, AMP-51, HC-009, G2.2-PA02, M2.1-PA01 | 16 |
| AAISM-1D | D1 · D AI security program development and management | 15 | AMP-06, AMP-21, AMP-22, AMP-27, AMP-29, AMP-30, G1.1-PA01, G1.2-PA01, G4.1-PA01, G6.1-PA01, G6.2-PA01, M1.1-PA01, M1.2-PA01, M1.2-PA03, M4.1-PA06 | 69 |
| AAISM-1E | D1 · E Business continuity and incident response | 10 | AMP-39, AMP-43, AMP-44, AMP-45, AMP-47, AMP-48, M5.1-PA01, M5.2-PA01, M5.2-PA02, M6.1-PA01 | 68 |
| AAISM-2A | D2 AI Risk Management · A Risk assessment, thresholds, treatment | 7 | AMP-15, AMP-17, AMP-18, AMP-20, AMP-22, G4.1-PA02, G4.2-PA01 | 59 |
| AAISM-2B | D2 · B AI threat and vulnerability management | 23 | G1.1-K09, G1.2-K01, G3.2-K06, G4.2-K02, G4.2-K06, G5.2-K05, G6.1-K01, G6.2-K04, M3.1-K10, M4.1-K08, M4.1-K09, M5.1-K02, M5.2-K10, M6.1-K03, M6.2-K04, AMP-20, AMP-37, AMP-41, AMP-42, HC-032, M4.2-K11, G4.1-PA02, M4.2-PA02 | 28 |
| AAISM-2C | D2 · C AI vendor and supply chain management | 8 | AMP-12, AMP-48, AMP-49, AMP-50, HC-023, M1.2-PA02, M6.1-PA01, M6.2-PA01 | 54 |
| AAISM-3A | D3 AI Technologies and Controls · A Security architecture and design | 26 | G1.1-K09, G1.2-K01, G3.2-K06, G4.2-K02, G4.2-K06, G5.2-K05, G6.1-K01, G6.2-K04, M3.1-K10, M4.1-K08, M4.1-K09, M5.1-K02, M5.2-K10, M6.1-K03, M6.2-K04, AMP-28, AMP-34, AMP-35, AMP-36, AMP-50, M3.1-K11, M4.2-K11, M2.2-PA01, M3.1-PA01, M6.2-PA01 … | 52 |
| AAISM-3B | D3 · B AI life cycle | 7 | AMP-20, AMP-37, AMP-42, AMP-49, M3.2-PA03, M5.2-PA02, M6.2-PA02 | 47 |
| AAISM-3C | D3 · C Data management controls | 5 | AMP-11, AMP-31, AMP-32, AMP-42, HC-011 | 15 |
| AAISM-3D | D3 · D Privacy, ethical, trust and safety controls | 8 | AMP-02, AMP-14, AMP-19, AMP-25, AMP-26, AMP-40, AMP-52, G3.1-PA01 | 34 |
| AAISM-3E | D3 · E Security controls and monitoring | 43 | G1.1-K09, G1.2-K01, G3.2-K06, G4.2-K02, G4.2-K06, G5.2-K05, G6.1-K01, G6.2-K04, M3.1-K10, M4.1-K08, M4.1-K09, M5.1-K02, M5.2-K10, M6.1-K03, M6.2-K04, AMP-13, AMP-14, AMP-18, AMP-26, AMP-33, AMP-34, AMP-36, AMP-38, AMP-39, AMP-40 … | 62 |

### MITRE ATT&CK

| Elemento | Nombre | Fuerte (n) | Fuerte (IDs) | Parcial (n) |
|---|---|---|---|---|
| TA0043 Reconnaissance | TA0043 Reconnaissance | 14 | M4.1-K03, M4.1-K07, M4.1-K09, M4.1-K10, M4.2-K02, M4.2-K03, M4.2-K05, M4.2-K06, M4.2-K07, M4.2-K09, M4.2-K10, HC-016, HC-017, M4.2-PA01 | 10 |
| TA0042 Resource Development | TA0042 Resource Development | 8 | M4.2-K02, M4.2-K03, M4.2-K05, M4.2-K06, M4.2-K07, M4.2-K09, HC-017, M4.2-PA01 | 0 |
| TA0001 Initial Access | TA0001 Initial Access | 15 | M4.1-K03, M4.1-K07, M4.1-K09, M4.1-K10, M4.2-K02, M4.2-K03, M4.2-K05, M4.2-K06, M4.2-K07, M4.2-K09, M4.2-K10, HC-016, M3.1-PA02, M4.1-PA04, M4.2-PA01 | 10 |
| TA0002 Execution | TA0002 Execution | 8 | M4.1-K03, M4.1-K07, M4.1-K09, M4.1-K10, M4.2-K10, M3.1-PA02, M4.1-PA04, M4.2-PA01 | 0 |
| TA0003 Persistence | TA0003 Persistence | 6 | M4.1-K03, M4.1-K07, M4.1-K09, M4.1-K10, M4.2-K10, M4.2-K11 | 0 |
| TA0004 Privilege Escalation | TA0004 Privilege Escalation | 1 | M4.2-K11 | 10 |
| TA0005 Defense Evasion | TA0005 Defense Evasion | 5 | M4.1-K03, M4.1-K07, M4.1-K09, M4.1-K10, M4.2-K10 | 0 |
| TA0006 Credential Access | TA0006 Credential Access | 5 | M4.1-K11, M4.2-K11, M3.1-PA02, M4.1-PA04, M4.2-PA01 | 10 |
| TA0007 Discovery | TA0007 Discovery | 8 | M4.1-K03, M4.1-K07, M4.1-K09, M4.1-K10, M4.2-K04, M4.2-K08, M4.2-K10, M4.1-K11 | 0 |
| TA0008 Lateral Movement | TA0008 Lateral Movement | 3 | M3.1-K07, M4.2-K04, M4.2-K08 | 0 |
| TA0009 Collection | TA0009 Collection | 3 | HC-026, M4.1-K11, M4.2-PA01 | 4 |
| TA0011 Command and Control | TA0011 Command and Control | 7 | M3.1-K07, M4.1-K03, M4.1-K07, M4.1-K09, M4.1-K10, M4.2-K10, M4.1-PA04 | 0 |
| TA0010 Exfiltration | TA0010 Exfiltration | 8 | M4.1-K03, M4.1-K07, M4.1-K09, M4.1-K10, M4.2-K04, M4.2-K08, M4.2-K10, HC-026 | 4 |
| TA0040 Impact | TA0040 Impact | 2 | M4.2-K04, M4.2-K08 | 0 |

### MITRE ATLAS

| Elemento | Nombre | Fuerte (n) | Fuerte (IDs) | Parcial (n) |
|---|---|---|---|---|
| ATLAS Reconnaissance | ATLAS Reconnaissance | 2 | HC-032, M4.2-PA02 | 0 |
| ATLAS Resource Development | ATLAS Resource Development | 3 | AMP-42, AMP-49, M4.2-PA02 | 0 |
| ATLAS Initial Access | ATLAS Initial Access | 3 | AMP-41, G4.1-PA02, M4.2-PA02 | 0 |
| ATLAS AI Model Access | ATLAS AI Model Access | 18 | G1.1-K09, G1.2-K01, G3.2-K06, G4.2-K02, G4.2-K06, G5.2-K05, G6.1-K01, G6.2-K04, M3.1-K10, M4.1-K08, M4.1-K09, M5.1-K02, M5.2-K10, M6.1-K03, M6.2-K04, AMP-20, M4.2-K11, M4.2-PA02 | 0 |
| ATLAS Execution | ATLAS Execution | 3 | AMP-37, AMP-41, M4.2-PA02 | 0 |
| ATLAS Persistence | ATLAS Persistence | 2 | AMP-42, M4.2-PA02 | 0 |
| ATLAS Privilege Escalation | ATLAS Privilege Escalation | 2 | M4.2-K11, M4.2-PA02 | 0 |
| ATLAS Defense Evasion | ATLAS Defense Evasion | 2 | AMP-41, M4.2-PA02 | 0 |
| ATLAS Credential Access | ATLAS Credential Access | 2 | M4.2-K11, M4.2-PA02 | 0 |
| ATLAS Discovery | ATLAS Discovery | 1 | M4.2-PA02 | 0 |
| ATLAS Collection | ATLAS Collection | 1 | M4.2-PA02 | 0 |
| ATLAS AI Attack Staging | ATLAS AI Attack Staging | 22 | G1.1-K09, G1.2-K01, G3.2-K06, G4.2-K02, G4.2-K06, G5.2-K05, G6.1-K01, G6.2-K04, M3.1-K10, M4.1-K08, M4.1-K09, M5.1-K02, M5.2-K10, M6.1-K03, M6.2-K04, AMP-20, AMP-37, AMP-42, HC-032, M4.2-K11, G4.1-PA02, M4.2-PA02 | 0 |
| ATLAS Exfiltration | ATLAS Exfiltration | 1 | M4.2-PA02 | 0 |
| ATLAS Impact | ATLAS Impact | 2 | G4.1-PA02, M4.2-PA02 | 0 |

### MITRE D3FEND

| Elemento | Nombre | Fuerte (n) | Fuerte (IDs) | Parcial (n) |
|---|---|---|---|---|
| D3FEND Model | D3FEND Model | 16 | M4.1-K03, M4.1-K07, M4.1-K09, M4.1-K10, M4.2-K02, M4.2-K03, M4.2-K05, M4.2-K06, M4.2-K07, M4.2-K09, M4.2-K10, HC-016, HC-017, M4.1-PA04, M4.2-PA01, M4.2-PA02 | 9 |
| D3FEND Harden | D3FEND Harden | 3 | HC-015, M4.2-K11, M3.1-PA02 | 14 |
| D3FEND Detect | D3FEND Detect | 21 | G5.1-K05, M4.1-K01, M4.1-K02, M4.1-K03, M4.1-K04, M4.1-K06, M4.1-K07, M4.1-K09, M4.1-K10, M4.2-K10, AMP-39, HC-017, HC-018, HC-019, M4.1-K11, M4.2-K11, M3.1-PA02, M4.1-PA02, M4.1-PA04, M4.1-PA05, M4.2-PA01 | 11 |
| D3FEND Isolate | D3FEND Isolate | 14 | G6.1-K08, M5.2-K01, M5.2-K02, M5.2-K03, M5.2-K04, M5.2-K05, M5.2-K06, M5.2-K07, M6.1-K02, M6.1-K09, AMP-39, AMP-44, HC-019, M5.2-PA01 | 9 |
| D3FEND Deceive | D3FEND Deceive | 1 | M4.1-K11 | 0 |
| D3FEND Evict | D3FEND Evict | 12 | G6.1-K08, M5.2-K01, M5.2-K02, M5.2-K03, M5.2-K04, M5.2-K05, M5.2-K06, M5.2-K07, M6.1-K02, M6.1-K09, AMP-44, M5.2-PA01 | 10 |
| D3FEND Restore | D3FEND Restore | 27 | G6.1-K08, M4.2-K04, M4.2-K08, M5.1-K09, M5.1-K10, M5.2-K01, M5.2-K02, M5.2-K03, M5.2-K04, M5.2-K05, M5.2-K06, M5.2-K07, M6.1-K01, M6.1-K02, M6.1-K03, M6.1-K04, M6.1-K05, M6.1-K06, M6.1-K07, M6.1-K08, M6.1-K09, M6.1-K10, AMP-47, HC-007, HC-021 … | 6 |

### OWASP LLM Top 10 2025

| Elemento | Nombre | Fuerte (n) | Fuerte (IDs) | Parcial (n) |
|---|---|---|---|---|
| LLM01 | Prompt Injection | 22 | G1.1-K09, G1.2-K01, G3.2-K06, G4.2-K02, G4.2-K06, G5.2-K05, G6.1-K01, G6.2-K04, M3.1-K10, M4.1-K08, M4.1-K09, M5.1-K02, M5.2-K10, M6.1-K03, M6.2-K04, AMP-37, AMP-41, HC-032, M4.2-K11, G4.1-PA02, M3.2-PA02, M4.2-PA02 | 0 |
| LLM02 | Sensitive Information Disclosure | 23 | G1.1-K09, G1.2-K01, G3.2-K06, G4.2-K02, G4.2-K06, G5.2-K05, G6.1-K01, G6.2-K04, M3.1-K10, M4.1-K08, M4.1-K09, M5.1-K02, M5.2-K10, M6.1-K03, M6.2-K04, AMP-31, AMP-32, AMP-37, HC-011, M4.2-K11, G4.1-PA02, M3.2-PA02, M4.2-PA02 | 0 |
| LLM03 | Supply Chain | 23 | G1.1-K09, G1.2-K01, G3.2-K06, G4.2-K02, G4.2-K06, G5.2-K05, G6.1-K01, G6.2-K04, M3.1-K10, M4.1-K08, M4.1-K09, M5.1-K02, M5.2-K10, M6.1-K03, M6.2-K04, AMP-20, AMP-42, AMP-48, AMP-49, AMP-50, M4.2-K11, M4.2-PA02, M6.2-PA01 | 1 |
| LLM04 | Data and Model Poisoning | 5 | AMP-20, AMP-32, AMP-42, AMP-49, M4.2-PA02 | 0 |
| LLM05 | Improper Output Handling | 5 | AMP-35, AMP-36, AMP-41, AMP-52, M4.2-PA02 | 0 |
| LLM06 | Excessive Agency | 38 | G1.1-K09, G1.2-K01, G3.2-K06, G4.2-K02, G4.2-K06, G5.2-K05, G6.1-K01, G6.2-K04, M3.1-K10, M4.1-K08, M4.1-K09, M5.1-K02, M5.2-K10, M6.1-K03, M6.2-K04, AMP-17, AMP-18, AMP-26, AMP-28, AMP-34, AMP-35, AMP-36, AMP-37, AMP-39, AMP-40 … | 0 |
| LLM07 | System Prompt Leakage | 2 | AMP-41, M4.2-PA02 | 0 |
| LLM08 | Vector and Embedding Weaknesses | 3 | AMP-32, AMP-42, M4.2-PA02 | 0 |
| LLM09 | Misinformation | 3 | AMP-20, AMP-52, M4.2-PA02 | 0 |
| LLM10 | Unbounded Consumption | 6 | G1.2-PA01, G4.1-PA02, G4.2-PA01, M1.2-PA01, M3.2-PA02, M4.2-PA02 | 0 |

### OWASP Agentic Top 10 2026

| Elemento | Nombre | Fuerte (n) | Fuerte (IDs) | Parcial (n) |
|---|---|---|---|---|
| ASI01 | Agent Goal Hijack | 10 | AMP-26, AMP-37, AMP-39, AMP-41, AMP-45, HC-032, G2.2-PA02, G4.1-PA02, M3.2-PA02, M4.2-PA02 | 16 |
| ASI02 | Tool Misuse and Exploitation | 17 | AMP-18, AMP-36, AMP-37, AMP-39, AMP-40, AMP-45, AMP-50, HC-010, HC-019, HC-032, M4.2-K11, G4.1-PA02, M2.2-PA01, M3.2-PA02, M4.2-PA02, M5.1-PA01, M5.2-PA01 | 15 |
| ASI03 | Agent Identity and Privilege Abuse | 17 | AMP-12, AMP-17, AMP-18, AMP-33, AMP-34, AMP-36, HC-009, HC-010, HC-032, M4.1-K11, M4.2-K11, G2.2-PA01, G2.2-PA02, G4.1-PA02, M2.2-PA01, M3.2-PA02, M4.2-PA02 | 15 |
| ASI04 | Agentic Supply Chain Vulnerabilities | 10 | AMP-42, AMP-48, AMP-49, AMP-50, G4.1-PA02, M1.2-PA02, M3.2-PA02, M4.2-PA02, M6.2-PA01, M6.2-PA02 | 0 |
| ASI05 | Unexpected Code Execution | 4 | AMP-35, AMP-36, G4.1-PA02, M4.2-PA02 | 0 |
| ASI06 | Memory and Context Poisoning | 9 | AMP-32, AMP-37, AMP-41, AMP-42, G4.1-PA02, M3.2-PA02, M4.2-PA02, M5.2-PA02, M6.2-PA02 | 0 |
| ASI07 | Insecure Inter-Agent Communication | 9 | AMP-28, AMP-35, AMP-46, AMP-50, G4.1-PA02, M3.1-PA01, M4.1-PA05, M4.2-PA02, M6.2-PA03 | 0 |
| ASI08 | Cascading Failures | 15 | AMP-15, AMP-18, AMP-28, AMP-35, AMP-38, AMP-39, AMP-43, AMP-44, G4.1-PA02, M3.1-PA01, M3.2-PA02, M4.1-PA06, M4.2-PA02, M5.2-PA01, M6.1-PA01 | 1 |
| ASI09 | Human-Agent Trust Exploitation | 8 | AMP-02, AMP-25, AMP-26, AMP-40, HC-019, AMP-52, G4.1-PA02, M4.2-PA02 | 1 |
| ASI10 | Rogue Agents | 18 | M6.2-K06, AMP-12, AMP-17, AMP-22, AMP-28, AMP-33, AMP-43, AMP-44, HC-009, M4.1-K11, G2.2-PA01, G4.1-PA02, G6.2-PA01, M1.2-PA02, M2.1-PA01, M3.2-PA02, M4.1-PA05, M4.2-PA02 | 1 |

### OWASP SAMM

| Elemento | Nombre | Fuerte (n) | Fuerte (IDs) | Parcial (n) |
|---|---|---|---|---|
| SAMM Governance | SAMM Governance | 4 | G2.2-K02, M6.2-K03, M6.2-K09, HC-024 | 0 |
| SAMM Design | SAMM Design | 6 | G2.2-K02, M6.2-K03, M6.2-K09, AMP-35, M3.1-K11, M3.1-PA01 | 14 |
| SAMM Implementation | SAMM Implementation | 6 | G2.2-K02, M6.2-K03, M6.2-K09, AMP-49, HC-031, M6.2-PA02 | 21 |
| SAMM Verification | SAMM Verification | 8 | G2.2-K02, M6.2-K03, M6.2-K09, AMP-37, HC-024, HC-031, HC-032, M3.2-PA03 | 4 |
| SAMM Operations | SAMM Operations | 4 | G2.2-K02, M6.2-K03, M6.2-K09, M6.2-PA02 | 0 |

### CIS Controls v8.1

| Elemento | Nombre | Fuerte (n) | Fuerte (IDs) | Parcial (n) |
|---|---|---|---|---|
| CIS 1 | Inventory and Control of Enterprise Assets | 10 | M2.1-K01, M2.1-K02, M2.1-K03, M2.1-K08, M2.1-K09, M5.1-K05, M6.2-K05, HC-016, HC-030, M2.1-PA01 | 11 |
| CIS 2 | Inventory and Control of Software Assets | 8 | M2.1-K01, M2.1-K02, M2.1-K03, M2.1-K08, M2.1-K09, M5.1-K05, M6.2-K06, M2.1-PA01 | 12 |
| CIS 3 | Data Protection | 11 | G3.1-K02, G3.1-K06, M2.1-K05, M2.1-K06, M2.1-K07, M2.1-K10, AMP-31, AMP-32, HC-011, HC-024, HC-033 | 9 |
| CIS 4 | Secure Configuration of Enterprise Assets and Software | 14 | G4.2-K03, M3.2-K01, M3.2-K02, M3.2-K03, M3.2-K05, M3.2-K10, M6.2-K05, AMP-09, AMP-51, HC-004, HC-030, G2.2-PA03, G3.2-PA01, M3.2-PA01 | 42 |
| CIS 5 | Account Management | 15 | G5.2-K03, M2.2-K01, M2.2-K02, M2.2-K03, M2.2-K04, M2.2-K07, M2.2-K08, M2.2-K09, M2.2-K10, M3.1-K09, AMP-33, AMP-34, HC-009, M4.2-K11, M2.2-PA01 | 6 |
| CIS 6 | Access Control Management | 16 | G5.2-K03, M2.2-K01, M2.2-K02, M2.2-K03, M2.2-K04, M2.2-K07, M2.2-K08, M2.2-K09, M2.2-K10, M3.1-K09, AMP-33, AMP-34, AMP-36, HC-009, M4.2-K11, M2.2-PA01 | 6 |
| CIS 7 | Continuous Vulnerability Management | 12 | M3.2-K04, M3.2-K06, M3.2-K09, M4.2-K01, M4.2-K02, M4.2-K03, M4.2-K05, M4.2-K06, M4.2-K07, M4.2-K09, AMP-51, HC-016 | 11 |
| CIS 8 | Audit Log Management | 24 | G2.2-K10, G3.1-K09, G3.2-K02, G3.2-K03, G3.2-K07, G5.1-K05, G5.1-K10, G5.2-K10, G6.2-K08, M1.1-K09, M2.1-K09, M2.2-K08, M4.1-K01, M4.1-K02, M4.1-K04, M4.1-K06, AMP-13, AMP-45, AMP-46, HC-005, HC-018, M4.1-K11, M4.1-PA04, M4.1-PA05 | 18 |
| CIS 9 | Email and Web Browser Protections | 7 | G2.2-PA03, G3.2-PA01, M3.1-PA02, M3.2-PA01, M4.1-PA01, M4.1-PA03, M4.2-PA01 | 0 |
| CIS 10 | Malware Defenses | 3 | M4.2-K04, M4.2-K08, M3.1-PA02 | 0 |
| CIS 11 | Data Recovery | 19 | M4.2-K04, M4.2-K08, M5.1-K09, M5.1-K10, M6.1-K01, M6.1-K02, M6.1-K03, M6.1-K04, M6.1-K05, M6.1-K06, M6.1-K07, M6.1-K08, M6.1-K10, AMP-47, HC-007, HC-021, HC-030, M3.1-K12, M6.1-PA01 | 6 |
| CIS 12 | Network Infrastructure Management | 2 | M3.1-K07, HC-030 | 47 |
| CIS 13 | Network Monitoring and Defense | 18 | G5.1-K05, M3.1-K07, M4.1-K01, M4.1-K02, M4.1-K03, M4.1-K04, M4.1-K06, M4.1-K07, M4.1-K09, M4.1-K10, M4.2-K10, AMP-39, HC-017, HC-019, M4.1-K11, M4.1-PA01, M4.1-PA04, M4.1-PA05 | 12 |
| CIS 14 | Security Awareness and Skills Training | 16 | G1.1-K05, G1.1-K09, G6.2-K01, M1.2-K04, M1.2-K05, M1.2-K06, M1.2-K07, M1.2-K08, M1.2-K09, AMP-29, AMP-30, HC-025, HC-026, HC-037, M1.2-PA03, M4.2-PA01 | 8 |
| CIS 15 | Service Provider Management | 13 | M1.2-K03, M6.2-K01, M6.2-K07, M6.2-K08, M6.2-K10, AMP-48, AMP-49, AMP-50, HC-008, HC-023, HC-029, HC-031, M1.2-PA02 | 34 |
| CIS 16 | Application Software Security | 9 | G2.2-K02, M6.2-K03, M6.2-K09, AMP-49, AMP-50, HC-024, HC-029, HC-031, M6.2-PA02 | 17 |
| CIS 17 | Incident Response Management | 31 | G6.1-K08, M4.1-K05, M5.1-K01, M5.1-K02, M5.1-K03, M5.1-K04, M5.1-K05, M5.1-K06, M5.1-K07, M5.1-K08, M5.2-K01, M5.2-K02, M5.2-K03, M5.2-K04, M5.2-K05, M5.2-K06, M5.2-K07, M6.1-K02, M6.1-K09, AMP-39, AMP-43, AMP-45, HC-019, HC-020, HC-022 … | 13 |
| CIS 18 | Penetration Testing | 6 | M3.2-K04, M3.2-K06, M3.2-K09, M4.2-K01, AMP-37, HC-032 | 23 |

### CSA CCM v4

| Elemento | Nombre | Fuerte (n) | Fuerte (IDs) | Parcial (n) |
|---|---|---|---|---|
| A&A | Audit & Assurance | 34 | G2.2-K10, G3.1-K09, G3.2-K02, G3.2-K03, G3.2-K06, G3.2-K07, G5.1-K10, G5.2-K10, G6.2-K08, M1.1-K09, M2.1-K09, M2.2-K08, M3.2-K04, M3.2-K06, M3.2-K09, M4.2-K01, AMP-13, AMP-14, AMP-37, AMP-38, AMP-46, HC-003, HC-005, HC-012, HC-018 … | 22 |
| AIS | Application & Interface Security | 25 | G2.2-K02, M3.1-K01, M3.1-K02, M3.1-K03, M3.1-K04, M3.1-K05, M3.1-K08, M3.1-K09, M3.1-K10, M6.2-K03, M6.2-K09, AMP-18, AMP-28, AMP-35, AMP-36, AMP-41, AMP-50, HC-024, HC-031, M3.1-K11, AMP-52, M3.1-PA01, M3.1-PA02, M3.2-PA02, M6.2-PA02 | 30 |
| BCR | Business Continuity Management & Operational Resilience | 32 | M4.2-K04, M4.2-K08, M5.1-K01, M5.1-K02, M5.1-K03, M5.1-K04, M5.1-K05, M5.1-K06, M5.1-K07, M5.1-K08, M5.1-K09, M5.1-K10, M6.1-K01, M6.1-K02, M6.1-K03, M6.1-K04, M6.1-K05, M6.1-K06, M6.1-K07, M6.1-K08, M6.1-K10, AMP-43, AMP-47, AMP-48, HC-007 … | 7 |
| CCC | Change Control & Configuration Management | 33 | G2.2-K01, G2.2-K02, G2.2-K04, G2.2-K06, G2.2-K07, G2.2-K08, G4.2-K03, M3.2-K01, M3.2-K02, M3.2-K03, M3.2-K05, M3.2-K10, M6.2-K03, M6.2-K09, AMP-09, AMP-10, AMP-21, AMP-38, HC-004, HC-013, HC-031, HC-034, HC-040, M3.1-K12, G2.2-PA02 … | 24 |
| CEK | Cryptography, Encryption & Key Management | 5 | M2.1-K05, M2.1-K06, M2.1-K07, M2.1-K10, AMP-11 | 0 |
| DCS | Datacenter Security | 8 | M2.1-K01, M2.1-K02, M2.1-K03, M2.1-K08, M2.1-K09, M5.1-K05, M3.1-K12, M2.1-PA01 | 12 |
| DSP | Data Security & Privacy Lifecycle Management | 20 | G3.1-K02, G3.1-K06, M2.1-K01, M2.1-K02, M2.1-K03, M2.1-K05, M2.1-K06, M2.1-K07, M2.1-K08, M2.1-K09, M2.1-K10, M5.1-K05, AMP-11, AMP-31, AMP-32, AMP-42, HC-011, HC-024, HC-033, G3.1-PA01 | 16 |
| GRC | Governance, Risk & Compliance | 94 | G1.1-K01, G1.1-K02, G1.1-K03, G1.1-K05, G1.1-K10, G2.1-K01, G2.1-K02, G2.1-K03, G2.1-K04, G2.1-K05, G2.1-K06, G2.1-K07, G2.1-K08, G2.2-K01, G2.2-K02, G2.2-K03, G2.2-K04, G2.2-K06, G2.2-K07, G2.2-K08, G2.2-K09, G3.1-K01, G3.1-K02, G3.1-K03, G3.1-K04 … | 142 |
| HRS | Human Resources | 20 | G1.1-K05, G1.1-K09, G6.2-K01, G6.2-K02, G6.2-K03, G6.2-K04, M1.2-K04, M1.2-K05, M1.2-K06, M1.2-K07, M1.2-K08, M1.2-K09, M1.2-K10, AMP-29, AMP-30, HC-025, HC-026, HC-037, M1.1-PA01, M1.2-PA03 | 21 |
| IAM | Identity & Access Management | 27 | G5.2-K03, M2.2-K01, M2.2-K02, M2.2-K03, M2.2-K04, M2.2-K05, M2.2-K06, M2.2-K07, M2.2-K08, M2.2-K09, M2.2-K10, M3.1-K03, M3.1-K06, M3.1-K09, AMP-17, AMP-18, AMP-32, AMP-33, AMP-34, AMP-36, AMP-50, HC-009, HC-015, HC-038, M4.2-K11 … | 2 |
| IPY | Interoperability & Portability | 5 | M6.2-K02, HC-023, HC-033, M6.2-PA01, M6.2-PA03 | 0 |
| IVS | Infrastructure & Virtualization Security | 20 | M2.2-K05, M2.2-K06, M3.1-K01, M3.1-K02, M3.1-K03, M3.1-K04, M3.1-K05, M3.1-K06, M3.1-K07, M3.1-K08, M3.1-K09, M3.1-K10, M6.2-K02, M6.2-K05, AMP-51, HC-002, HC-015, HC-030, M3.1-K11, M3.1-PA01 | 31 |
| LOG | Logging & Monitoring | 26 | G3.2-K06, G5.1-K05, M4.1-K01, M4.1-K02, M4.1-K03, M4.1-K04, M4.1-K06, M4.1-K07, M4.1-K09, M4.1-K10, M4.2-K10, AMP-13, AMP-39, AMP-45, AMP-46, AMP-51, HC-017, HC-018, HC-019, HC-040, M4.1-K11, G4.2-PA01, M3.2-PA02, M4.1-PA01, M4.1-PA04 … | 10 |
| SEF | Security Incident Management, E-Discovery & Cloud Forensics | 33 | G6.1-K08, M4.1-K05, M5.1-K01, M5.1-K02, M5.1-K03, M5.1-K04, M5.1-K05, M5.1-K06, M5.1-K07, M5.1-K08, M5.2-K01, M5.2-K02, M5.2-K03, M5.2-K04, M5.2-K05, M5.2-K06, M5.2-K07, M6.1-K02, M6.1-K09, AMP-39, AMP-40, AMP-43, AMP-44, AMP-45, HC-019 … | 33 |
| STA | Supply Chain Management, Transparency & Accountability | 22 | M1.2-K03, M6.2-K01, M6.2-K02, M6.2-K07, M6.2-K08, M6.2-K10, AMP-12, AMP-15, AMP-42, AMP-48, AMP-49, AMP-50, HC-008, HC-023, HC-029, HC-031, HC-033, M3.1-K12, M1.2-PA02, M6.1-PA01, M6.2-PA01, M6.2-PA03 | 29 |
| TVM | Threat & Vulnerability Management | 31 | M3.2-K04, M3.2-K06, M3.2-K09, M4.1-K03, M4.1-K07, M4.1-K09, M4.1-K10, M4.2-K01, M4.2-K02, M4.2-K03, M4.2-K04, M4.2-K05, M4.2-K06, M4.2-K07, M4.2-K08, M4.2-K09, M4.2-K10, AMP-20, AMP-37, AMP-41, HC-016, HC-017, HC-032, M4.1-K11, M4.2-K11 … | 16 |
| UEM | Universal Endpoint Management | 2 | M6.2-K05, HC-030 | 23 |

### CSA AICM

| Elemento | Nombre | Fuerte (n) | Fuerte (IDs) | Parcial (n) |
|---|---|---|---|---|
| MDS | Model Security (AICM) | 26 | G1.1-K09, G1.2-K01, G3.2-K06, G4.2-K02, G4.2-K06, G5.2-K05, G6.1-K01, G6.2-K04, M3.1-K10, M4.1-K08, M4.1-K09, M5.1-K02, M5.2-K10, M6.1-K03, M6.2-K04, AMP-20, AMP-37, AMP-41, AMP-42, AMP-49, AMP-51, M4.2-K11, AMP-52, M3.2-PA02, M3.2-PA03 … | 0 |
| AIS-11 | Agents Security Boundaries (AICM) | 35 | G1.1-K09, G1.2-K01, G3.2-K06, G4.2-K02, G4.2-K06, G5.2-K05, G6.1-K01, G6.2-K04, M3.1-K10, M4.1-K08, M4.1-K09, M5.1-K02, M5.2-K10, M6.1-K03, M6.2-K04, AMP-17, AMP-18, AMP-22, AMP-26, AMP-28, AMP-34, AMP-35, AMP-36, AMP-40, AMP-41 … | 0 |
| IAM-19 | Agent Access Restriction (AICM) | 12 | AMP-17, AMP-18, AMP-33, AMP-34, AMP-36, AMP-50, HC-009, HC-010, M4.2-K11, G2.2-PA01, M2.2-PA01, M3.2-PA02 | 0 |
| AICM (dominios CCM) | AICM reutiliza los 17 dominios CCM + MDS | 9 | M6.2-K06, AMP-06, AMP-31, AMP-46, AMP-51, G2.1-PA02, M2.1-PA01, M4.1-PA05, M6.2-PA01 | 0 |

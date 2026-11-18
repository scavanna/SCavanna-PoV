# Defender for Cloud – Threat Protection for AI services: relación con Sentinel, MITRE ATT&CK, MITRE ATLAS y OWASP LLM Top 10

**Fecha:** 18-nov-2026 · **Para:** Santiago Cavanna (Prin CSA, CSU Security) · **Estado:** v1 – investigación + propuesta de matriz

---

## 1. Conclusión ejecutiva

1. **Microsoft publica para cada alerta de IA de Defender for Cloud (MDC-AI) únicamente tácticas MITRE ATT&CK** (kill chain de MDC alineado a ATT&CK v9). **No existe mapeo oficial publicado por alerta a MITRE ATLAS ni a OWASP LLM Top 10.**

2. **Sentinel sólo soporta ATT&CK** (página MITRE alineada a ATT&CK v18, en preview). No hay soporte de ATLAS en la matriz de cobertura, en analytics rules ni en incidentes. La necesidad fue planteada internamente (abr-2025) y no se encontró compromiso de roadmap.

3. **La relación Microsoft–MITRE ATLAS es profunda pero "upstream"**: Microsoft cofundó ATLAS (2020), aportó Counterfit al plugin Arsenal de CALDERA (2023) y el foco GenAI de ATLAS (nov-2023). Esa colaboración **no se tradujo aún en etiquetado ATLAS dentro de los productos** (MDC, Sentinel, Defender XDR).

   

   

---

## 2. Qué es MDC Threat Protection for AI services y cómo se integra con Sentinel

| Aspecto | Detalle | Fuente |
|---|---|---|
| Estado | GA. Plan "Defender for AI Services" en Defender for Cloud. 30 días de trial (tope 75 B tokens). Solo tokens de texto. | Learn – AI threat protection |
| Señales | Azure AI Content Safety **Prompt Shields** + Microsoft Threat Intelligence (MDTI) + clasificadores propios + anomalías de acceso/uso. | Learn – AI threat protection |
| Servicios soportados | Azure OpenAI y Azure AI Model Inference (Foundry). Comercial only (no Gov, no 21Vianet, no AWS). | Learn |
| Evidencia | *Prompt evidence* opcional en la alerta (prompt/respuesta sospechosa). | Learn |
| Defender XDR | Alertas MDC-AI se correlacionan en incidentes de Defender XDR. | Learn |
| **Sentinel** | Vía **conector Defender XDR** (incidentes/alertas) y/o **conector Microsoft Defender for Cloud (tenant-based)**. Nota propia (20-may-2026): habilitar ambos para evitar incidentes vacíos. En Sentinel las alertas llegan a `SecurityAlert` con `Tactics` = ATT&CK; la página **MITRE ATT&CK de Sentinel** (preview) muestra cobertura ATT&CK v18 — **sin ATLAS**. | Learn – mitre-coverage; chat interno |
| Capas de defensa (modelo útil con clientes) | 1) Alineamiento del modelo (refusal ≠ alerta) → 2) Content Safety filters → 3) Prompt Shields → 4) **Defender for AI** (convierte técnicas de ataque en alertas + TI) → 5) **Sentinel analytics rules** para el "inference gap" (lo que ningún detector marca). | Daemarys/Defender-for-AI-use-cases (fork propio) |

> 

---

## 3. Catálogo de alertas MDC-AI, significado y mapeo oficial ATT&CK

Fuente oficial: https://learn.microsoft.com/azure/defender-for-cloud/alerts-ai-workloads (verificar contra la página viva; Microsoft agrega/retira alertas con frecuencia).

| Alert ID | Qué detecta | Sev. | Tácticas ATT&CK (oficial) |
|---|---|---|---|
| AI.Azure_Jailbreak.ContentFiltering.**BlockedAttempt** | Inyección directa para manipular el system prompt; **bloqueada** por Prompt Shields | Medium | Privilege Escalation, Defense Evasion |
| AI.Azure_Jailbreak.ContentFiltering.**DetectedAttempt** | Igual, pero **no bloqueada** por configuración de filtros | Medium | Privilege Escalation, Defense Evasion |
| AI.Azure_CredentialTheftAttempt | Credenciales detectadas en la **respuesta** del modelo | Medium | Credential Access, Lateral Movement, Exfiltration |
| AI.Azure_DataLeakInModelResponse.Sensitive | Datos sensibles en la respuesta del modelo | Medium | Collection |
| AI.Azure_PhishingContentInModelResponse | URL de phishing en la respuesta → app/modelo/datos corruptos | High | Impact (Defacement), Collection |
| AI.Azure_PhishingContentInAIApplication | URL de phishing compartida en la app de IA | High | Initial Access |
| AI.Azure_PhishingContentInUserPrompt | Phishing en el prompt del usuario | High | Collection |
| AI.Azure_ASCIISmuggling | Inyección con caracteres Unicode invisibles | Medium | Impact |
| AI.Azure_AccessFromAnonymizedIP | Acceso desde Tor | High | Execution |
| AI.Azure_AccessFromSuspiciousIP | Acceso desde IP maliciosa (MDTI) | High | Execution |
| AI.Azure_AccessFromSuspiciousUserAgent | User agent de herramientas de ataque | Medium | Execution, Reconnaissance, Initial Access |
| AI.Azure_DOWDuplicateRequests | *Wallet attack* – solicitudes recurrentes | Medium | Impact |
| AI.Azure_AccessAnomaly | Anomalía de acceso al recurso | Medium | Execution |
| AI.Azure_Anomaly | Anomalía genérica en el recurso de IA | Medium | Execution |
| AI.Azure_SuspiciousInitialAccessOperation | Operación de alto riesgo por service principal sobre recursos de IA | Medium | Initial Access |
| Exposed Kubernetes service detected (AI apps on K8s) | LoadBalancer expone app de IA | Medium | — (señal de Defender for Containers) |
| *(Agentes)* Defender Real-Time Protection en Agent 365 Tool Gateway | Veredictos <1 s por invocación de herramienta: prompt injection, ASCII smuggling, dominios maliciosos, destinos de correo inseguros | n/d | No publicado como alerta MDC clásica (LevelUp 11-may-2026, Shay Amar / Liran Levy) |

---

## 4. Mapeo propuesto a MITRE ATLAS y OWASP LLM Top 10 (inferencia – validar con PM)

Resumen (detalle completo, confianza y notas en el Excel, hoja *Matriz MDC-AI x ATLAS x OWASP*):

| Alerta MDC-AI | ATLAS (técnicas) | OWASP LLM 2025 | Confianza |
|---|---|---|---|
| Jailbreak Blocked / Detected | AML.T0051.000 Direct Prompt Injection · AML.T0054 LLM Jailbreak · AML.T0065 LLM Prompt Crafting | LLM01 | Alta |
| CredentialTheftAttempt | AML.T0055 Unsecured Credentials · AML.T0057 LLM Data Leakage · AML.T0024 Exfiltration via AI Inference API | LLM02 | Alta |
| DataLeakInModelResponse.Sensitive | AML.T0057 · AML.T0024.000 · AML.T0063 | LLM02 (+LLM08 si RAG) | Alta |
| PhishingContentInModelResponse | AML.T0070 RAG Poisoning · AML.T0071 · AML.T0067 Trusted Output Components Manipulation · AML.T0077 Response Rendering · AML.T0052 Phishing | LLM04, LLM05, LLM09 | Media |
| PhishingContentInAIApplication | AML.T0051.001 Indirect Prompt Injection · AML.T0052 · AML.T0049 | LLM01 | Media |
| PhishingContentInUserPrompt | AML.T0052 · AML.T0051.000 | LLM01, LLM09 | Media |
| ASCIISmuggling | AML.T0068 LLM Prompt Obfuscation · AML.T0051.001 · AML.T0054 | LLM01, LLM05 | Alta |
| Access from Tor / Suspicious IP / Suspicious UA | AML.T0040 AI Model Inference API Access · AML.T0012 Valid Accounts · AML.T0006 Active Scanning · AML.T0016 Obtain Capabilities | LLM10 (abuso) | Media |
| DOWDuplicateRequests | AML.T0034 Cost Harvesting · AML.T0029 Denial of AI Service · AML.T0048.000 Financial Harm | LLM10 | Alta |
| AccessAnomaly / Anomaly | AML.T0040 · AML.T0012 · AML.T0075 Cloud Service Discovery · AML.T0043 (sondeo iterativo) | — | Baja-Media |
| SuspiciousInitialAccessOperation | AML.T0012 · AML.T0055 · AML.T0075 | LLM03 (parcial) | Media |
| Exposed K8s service | "Misconfigured or Publicly Exposed AI Services" (ATLAS 2026, ID a validar) · AML.T0049 | LLM03/LLM06 (parcial) | Media |
| Defender RTP – Agent 365 ATG | AML.T0051.001 · "AI Agent Tool Invocation" (ATLAS 2026, ID a validar) · AML.T0025 | LLM01, LLM06 | Media |

**Cambios OWASP 2026 relevantes para la narrativa:** LLM01 sigue #1; **Excessive Agency sube a #3**; **Unbounded Consumption sube a #6**; Improper Output Handling baja a #10; System Prompt Leakage pasa a *Hidden Context Exposure*. La edición 2026 ya trae crosswalk a MITRE ATLAS, NIST y CWE — útil para citar.

### Gaps ATLAS sin señal MDC-AI (hoja *Gaps ATLAS sin alerta*)
- **AML.T0056 / T0069** (extracción de system prompt / discovery de info del sistema) → regla KQL Sentinel sobre logs de prompt + Purview DSPM for AI.
- **AML.T0020 / T0070** (envenenamiento de entrenamiento / RAG) → AI Model Scanning (preview), integridad de índices, Defender for Storage.
- **AML.T0024.001/.002** (model inversion / extraction) → analítica de volumen por identidad; rate limiting APIM.
- **AML.T0053 / Tool Poisoning** → Agent 365 + Defender RTP (no MDC-AI clásico).
- **AML.T0062 / LLM09** (alucinación/desinformación) → Content Safety Groundedness Detection → log → Sentinel (idea de Heather Sze).
- **AML.T0061** (auto-replicación de prompts) → correlación multi-sesión en Sentinel.

---

## 5. Relación Microsoft ↔ MITRE (foco ATLAS)

| Hito | Año | Qué aporta |
|---|---|---|
| Adversarial ML Threat Matrix → **ATLAS** lanzado con Microsoft como cofundador | 2020–2021 | Ram Shankar Siva Kumar (Microsoft AI Red Team) lo llama la "Rosetta Stone" de AI security |
| **Counterfit** (open source, Microsoft) | 2021 | Automatiza técnicas de la matriz contra servicios de IA |
| **Arsenal** plugin para CALDERA (MITRE + Microsoft) | mar-2023 | Emula TTPs ATLAS usando Counterfit → base para purple teaming de AI |
| Foco **GenAI/LLM en ATLAS** (MITRE + Microsoft) | nov-2023 | Técnicas y case studies LLM (prompt injection, jailbreak, etc.) |
| **CAAT + AI Defense Capabilities** (Microsoft Learn, Zero Trust) | 2026 | Escenarios → OWASP → ATLAS → tecnologías Microsoft (MDC, Sentinel, Purview, Entra…) |
| ATLAS hoy | nov-2026 | 16 tácticas, 221 técnicas, 44 mitigaciones, 77 case studies; plataformas Predictive/Generative/Agentic/Enterprise |

**Lectura:** la colaboración es fuerte en *conocimiento* (framework, red teaming, case studies) y en *guía arquitectónica* (CAAT), pero **no en instrumentación de producto**. Ahí está el gap que tu matriz cubre.

---

## 6. Plugins / proyectos públicos que apuntan a esta necesidad

| Proyecto | Autor / tipo | Qué hace | Utilidad para la matriz |
|---|---|---|---|
| **mitre-atlas/atlas-data**, **atlas-navigator-data** | MITRE | Datos ATLAS en YAML/STIX + layers de Navigator | Fuente canónica de IDs; base para `externaldata` en KQL / watchlist Sentinel |
| **mitre-atlas/arsenal** | MITRE + Microsoft | Plugin CALDERA con Counterfit | Emulación ATLAS para validar que MDC-AI dispara |
| **mitre-atlas/atlas-knowledge-base-agent** | MITRE | Agente Q&A sobre grafo ATLAS | Referencia para un agente Security Copilot / Copilot Studio de enriquecimiento |
| **lizetpenamsft/sentinel-llm-owasp2025-rulepack** | alias Microsoft (personal) | Analytics rules Sentinel por LLM01–LLM10, tags OWASP, mapeadas a ATT&CK | Plantilla para "enriquecer" incidentes con OWASP vía tags/custom details |
| **Daemarys/ai-jailbreak-sentinel-101** y **Defender-for-AI-use-cases** | practitioner (fork propio: scavanna) | Workshop: simula ataques ATLAS (AML.T0065), detecta con Sentinel; capas y *inference gap*; playbook que etiqueta incidentes "AI Threat" | Patrón de playbook Logic App para **añadir tags ATLAS/OWASP a incidentes** |
| **sagarm365/ai-threat-detection** | detection engineer | KQL Defender XDR/Sentinel con columnas ATLAS (AML.T0054, T0012, T0035) + ATT&CK | Ejemplo de doble etiquetado ATLAS+ATT&CK en reglas |
| **jonarm/ai-security-llm-governance-controls** | practitioner | Programa de gobierno con mapeo OWASP/NIST/ISO 42001/ATLAS, reglas Sentinel, Terraform | Referencia de estructura documental |
| **rod-trent/Security-Copilot – MITREATLAS.yaml** | Rod Trent (Microsoft) | Plugin KQL de Security Copilot que carga referencia MITRE (ATT&CK y ATLAS) | **Base directa para un plugin de enriquecimiento ATLAS en Security Copilot** |
| **pisinger – Defender Cloud MITRE v2** | comunidad | Matriz ATT&CK × planes Defender (incl. Defender for AI: 3 Recon, 3 Initial Access, 5 Execution, …) | Muestra el estado del arte: solo ATT&CK |
| Qualys TotalAI 1.7 | partner/ISV | Reportes de scan de modelos mapeados a OWASP, MITRE ATLAS y EU AI Act | Ejemplo de enriquecimiento ATLAS por terceros (posture, no alertas) |
| Inspira – MITRE ATT&CK Coverage Insight (Security Store) | partner | Agente Security Copilot de cobertura ATT&CK en Sentinel | Patrón a replicar para ATLAS |

**Cómo enriquecer hoy (sin esperar producto):**
1. **Watchlist Sentinel** `MDCAI_ATLAS_OWASP` con la hoja *Matriz* del Excel (AlertName → ATLAS techniques, OWASP IDs).
2. **Analytics rule / automation rule** sobre `SecurityAlert where ProductName == "Azure Security Center" and AlertName startswith "AI."` → join con la watchlist → escribir `ExtendedProperties`/custom details y **tags** de incidente (`ATLAS:AML.T0051.000`, `OWASP:LLM01`).
3. **Playbook Logic App** (patrón Daemarys *Tag-AI-Threat-On-Jailbreak*) para tags + comentario con link a atlas.mitre.org/techniques/ID.
4. **Workbook** "Cobertura ATLAS" que reutilice el layer de `atlas-navigator-data` (heatmap propio, ya que la página MITRE de Sentinel no lo soporta).
5. **Plugin Security Copilot** (KQL `externaldata` sobre `atlas-data` YAML→CSV, patrón Rod Trent) para "explicar la alerta en términos ATLAS/OWASP".


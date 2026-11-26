# Análisis Competitivo Enterprise: Agentic SOC, SOAR & AppSec Agéntico (Corte 25-Nov-2026)

## 1. Resumen Ejecutivo y Alcance

Este paquete consolida la investigación técnica y competitiva actualizada al **25 de noviembre de 2026**, combinando:
1. **Línea base Microsoft Ignite 2026 (17–20 nov 2026) y GitHub (oct/nov 2026):** **Microsoft Perception** (GA), **ISOC in Microsoft Defender** (GA core), **Microsoft Security Copilot** (+18 agentes nativos en el ecosistema), **Codename MDASH** (Expanded Preview), **GitHub Advanced Security (GHAS) Agentic Autofix** (GA en GHEC / Public Preview en Azure DevOps), **Azure Logic Apps** (SOAR determinístico e híbrido) y **Agent 365 + Entra Agent ID + Defender Local Agent Runtime Protection** (GA en Windows).
2. **Navegación directa en vivo (Playwright + sitios oficiales, portales de documentación, release notes y comunicados técnicos)** de los **12 fabricantes enterprise** mejor posicionados (**Microsoft, CrowdStrike, Palo Alto Networks, Google Cloud + Wiz, Cisco / Splunk, SentinelOne, AWS, ServiceNow, IBM Security, Zscaler, Elastic y Fortinet**) más **6 especialistas pure-play** (**Torq, Swimlane, Snyk, Okta, SailPoint y OpenAI/Anthropic**).

---

## 2. Arquitectura Microsoft: Separación Limpia de los 6 Planos (Sin Solapamientos)

| Plano | Producto / Componente | Estado Real (Nov 2026) | Rol Arquitectónico Exacto |
| :--- | :--- | :--- | :--- |
| **1. Datos, Contexto y Actuadores** | **ISOC in Microsoft Defender** + Sentinel + Defender XDR + Exposure Mgmt | **GA Core** (17-nov-2026); retención 90d Defender y normalización en ingesta en **Preview** | Unifica SIEM + XDR + Data Lake en el portal Defender (>165T señales/día, >500 conectores, ingesta $2.40/GB, opt-in para clientes Sentinel con E5/E7/Defender Suite). |
| **2. Orquestación Multi-Agente por Outcomes** | **Microsoft Perception** (Red, Blue & Green Agents) | **Plataforma GA** (17-nov-2026); 6 agentes en GA y 3 en Preview | Coordina equipos de agentes Red/Blue/Green mediante Playbooks o Chat, con enrutamiento dinámico de modelos por tarea, MCP/APIs (Preview) y aprobación humana. |
| **3. Asistencia Interactiva y Agentes por Dominio** | **Microsoft Security Copilot** (+18 agentes nativos + >30 de partners) | **GA** + inclusión para clientes M365 E5/E7 (agentes mix GA/Preview) | Asiste al analista y automatiza colas repetitivas embebidas en Defender, Entra, Intune, Purview y Sentinel usando SCUs e identidades Entra Agent ID. |
| **4. SOAR Empresarial Determinístico e Híbrido** | **Azure Logic Apps** (Playbooks + On-Prem Data Gateway) | **GA Producción** | >1.400 conectores empresariales/ITSM/red y coexistencia plurianual con **Splunk on-prem** sin exigir migración forzada de logs. |
| **5. AppSec y Vulnerabilidades Agénticas** | **Codename MDASH** + **GHAS Agentic Autofix** | MDASH: **Expanded Preview** (5 GB) \| GHAS Autofix: **GA GHEC** (15-oct) y **Preview ADO** (23-nov) | MDASH descubre, debate y prueba vulnerabilidades profundas read-only en código (5 etapas, >100 subagentes); GHAS (`copilot-swe-agent`) repara en múltiples archivos, valida con CodeQL y abre PR. |
| **6. Gobierno y Contención de Agentes IA** | **Agent 365** + **Entra Agent ID** + **Defender** + **Purview** | Defender Local Agent Runtime Protection en Windows: **GA**; Purview Agent DLP: **Preview ene-2027** | Descubre 60 tipos de agentes locales (Claude Code, Codex, Copilot CLI, OpenClaw) y agentes cloud 3P, asigna identidad gobernable, bloquea instrucciones maliciosas en el agent loop y aplica DLP. |

---

## 3. Ranking Cuantitativo Ponderado (12 Fabricantes Enterprise — Escala 0 a 100)

| Posición | Fabricante | Índice (0-100) | Brecha vs. MS | Oferta Insignia Verificada a Noviembre 2026 |
| :---: | :--- | :---: | :---: | :--- |
| **#1** | **Microsoft** | **97.6** | `0.0` | ISOC in Defender + Perception (GA) + Security Copilot (+18 agentes) + MDASH + GHAS Autofix + Logic Apps + Agent 365 |
| **#2** | **Palo Alto Networks** | **86.5** | `-11.2` | Cortex XSIAM 3.6 + Cortex AgentiX 1.4 (FedRAMP High) + XSOAR 8.15 + Cortex XDR 5.2 AES / XDR One + Console NL |
| **#3** | **Google Cloud + Wiz** | **85.0** | `-12.7` | Google AI Threat Defense + SecOps SIEM/SOAR (RN 19-nov-2026) + CodeMender (Preview) + Wiz Red/Blue/Green Agents & AI SAST |
| **#4** | **CrowdStrike** | **81.7** | `-15.9` | Falcon Next-Gen SIEM (alianza Dynatrace) + Fusion SOAR + Charlotte AI Multi-Agent (GA oct-2026) + SafeMind + Falcon Guardian |
| **#5** | **AWS** | **76.0** | `-21.6` | AWS Continuum (GA code vulns 22-oct-2026 en 2 regiones US; pentest Preview) + AWS Security Incident Response Agent (nov-2026) |
| **#5** | **SentinelOne** | **76.0** | `-21.6` | Singularity ASOC (21-oct-2026) + Purple AI Agentic Investigation (>400k inv.) + Hyperautomation Closed-Loop + Agentic DR (EA) |
| **#7** | **Fortinet** | **75.1** | `-22.6` | FortiSOAR 8.0.0 + FortiAI v6.0.0 (>19 agentes IA y MCP bidireccional GA oct-2026) + FortiSIEM + FortiSOC (Preview) |
| **#8** | **Cisco / Splunk** | **74.6** | `-23.0` | Splunk ES 8.8.0 (GA 4-nov-2026) + Agentic SOC Workforce + Splunk SOAR HA + Cisco XDR Instant Attack Verification + Data Fabric |
| **#9** | **IBM Security** | **74.3** | `-23.4` | IBM Autonomous Security (ATOM + ARGO + ADA) + QRadar SOAR + watsonx Orchestrate AI Gateway Discover & Contain (Tech Preview) |
| **#10** | **Elastic** | **73.4** | `-24.2` | Elastic Security 9.4/9.5 (Workflows GA + Attack Discovery autónomo + 5 skills AI Agent) + Elastic 9.6 AlertZero (Tech Preview 23-nov) |
| **#11** | **Zscaler** | **67.0** | `-30.6` | Zscaler Agentic SOC (GA 9-sep-2026 sobre Zero Trust + Decoy Mesh) + Risk360 + Autonomous Application Shield (oct-2026) |
| **#12** | **ServiceNow** | **65.9** | `-31.7` | Security Operations (SIR/VR) + Now Assist SecOps (oct-2026) + Arc Agent (GA 21-oct) + AI Control Tower & AI Passport (Q4) |

*(Nota: Los puntajes exactos se recalculan dinámicamente con `SUMPRODUCT` en la hoja `02_Scoring_Ponderado_10Dim` según los pesos asignados).*

---

## 4. Hallazgos Críticos de Due Diligence (Marketing vs. Realidad Documentada a Nov 2026)

1. **Contención de Agentes IA ("Kill Switches"):** En octubre y noviembre de 2026 proliferaron anuncios de *Kill Switches*. La revisión técnica demuestra que el **AI Kill Switch de CrowdStrike** corta únicamente el acceso al modelo a través de *Falcon AI Gateway* (sin revocar identidad ni cubrir agentes con modelos locales); **SailPoint** e **IBM Discover & Contain** están en *Preview / Tech Preview*; y **ServiceNow AI Passport** requiere que terceros apliquen el bloqueo. Microsoft combina **Entra Agent ID** (revocación de identidad), **Defender en Windows** (bloqueo GA en el loop local para 60 agentes) y **Purview** (política de datos).
2. **AppSec y Vulnerabilidades Agénticas:** Tres gigantes convergen en validación dinámica con PoC: **Microsoft Codename MDASH** (Expanded Preview, repos hasta 5 GB) + **GHAS Agentic Autofix** (GA en GHEC), **Google DeepMind CodeMender** (Public Preview; integración invocada desde Wiz aún *"coming soon"*) y **AWS Continuum** (GA el 22-oct-2026 para vulnerabilidades de código, pero restringido inicialmente a **2 regiones de EE. UU.**).
3. **Coexistencia SOAR y SIEM:** **Splunk ES 8.8** (GA 4-nov-2026) usa por defecto *Model Runtime* que recurre externamente a **Azure OpenAI** cuando requiere mayor calidad de modelo, y su upgrade a 8.x es irreversible respecto a investigaciones previas sin backup. Frente al *rip-and-replace* exigido por Palo Alto XSIAM o CrowdStrike Next-Gen SIEM, **Azure Logic Apps + ISOC + Perception MCP** permiten coexistir varios años con Splunk on-prem optimizando costos dentro del beneficio de M365 E5 y Defender for Servers P2.

---

## 5. Composición del Paquete Entregable (100% Fuentes Públicas Verificadas)

Todos los datos, fechas de lanzamiento, estados de madurez (GA vs. Preview) y referencias arquitectónicas de este paquete provienen exclusivamente de **documentación técnica pública, *release notes* oficiales, blogs de ingeniería y comunicados públicos** verificados al **25 de noviembre de 2026** (46 fuentes URL públicas registradas con hipervínculos directos en `08_Fuentes_y_Evidencia_Web`):

- `Matriz_Competitiva_Agentic_SOC_12_Fabricantes_Nov2026.xlsx` — Benchmark integral de 9 hojas con modelo cuantitativo ponderado editable (`SUMPRODUCT`), auditoría GA vs. Preview de 56 capacidades, comparativas de SOAR/AppSec/Gobierno de Agentes IA, criterios de Due Diligence para el CISO y 46 fuentes URL públicas.
- `Catalogo_Microsoft_Agentic_Security_Ignite2026.xlsx` — Catálogo técnico de 5 hojas con la arquitectura Microsoft de 6 planos, agentes Red/Blue/Green de Perception, los +18 agentes nativos de Security Copilot, Codename MDASH + GHAS Agentic Autofix e ISOC + Azure Logic Apps SOAR.
- `Informe_Ejecutivo_Competitivo_Agentic_SOC_Nov2026.md` — Síntesis ejecutiva y arquitectónica del análisis.
- `infografias\` — Serie modular de **7 infografías ejecutivas y técnicas (`IG-01` a `IG-07`)** entregadas en `.svg` vectorial editable (`1920×1200`), `.png` 4K (`3840×2400`) y `.jpg` de alta resolución (`3840×2400`), acompañadas del visor interactivo `Galeria_Serie_7_Infografias_Nov2026.html` y `00_Arquitectura_Serie_Infografias.md`.


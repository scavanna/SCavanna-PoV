# Pre-ensayo · AMP-50

> **GM-24 V7.1 · The Next CISO + Sub-plan PO-GAC** · 2026-11-14. Catálogo: 379 conceptos (245 K · 52 AMP · 40 HC · 42 PA), todos con pre-ensayo íntegro y mapeados a 17 marcos (NIST/ISACA/MITRE/OWASP/CIS/CSA). V7.1 = ChangeSet editorial CS-GM24-V7.1-001 (4 títulos generalizados; sin cambio de IDs, cantidad ni mapeo). Plano A (corpus académico). Referencias DD/K4x/R/eo:OP/COE: marco interno.

### 092. AMP-50 — Seguridad de herramientas y conectores

**Unidad:** M6.2 Seguridad en Redes, Nube, Tecnologías Emergentes y SCRM · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Referencias por ID (V7-C09):** OWASP ASI04/ASI02 (2026 v2.01); CSA AICM AIS-11 · **Extensión:** 198 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** Conectores (incluido MCP) y herramientas amplían lo que un agente puede tocar: cada uno es una puerta hacia un sistema con sus propios permisos.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** Conectores (incluido MCP) y herramientas amplían lo que un agente puede tocar: cada uno es una puerta hacia un sistema con sus propios permisos. Requieren inventario (qué conectores existen y cuáles usa cada agente), autenticación propia (identidad del agente, no del constructor), permisos mínimos por operación y monitoreo de invocaciones. La tesis es que la seguridad de un agente se decide en sus conectores tanto como en su modelo.

**Tensión y límites.** La tensión es la riqueza del ecosistema (miles de conectores) frente a la capacidad de revisar cada uno. Otra tensión es MCP: un protocolo abierto que facilita integrar y también facilita que un servidor malicioso o comprometido inyecte herramientas. El ensayo debe proponer una lista de servidores MCP aprobados.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: gestión de integraciones, OAuth2, OWASP ASI04/ASI02, allowlists. Implementación: inventario de conectores y servidores MCP aprobados (Sentinel MCP en preview, Microsoft MCP Server for Enterprise solo lectura, Learn Docs MCP), políticas de datos de Power Platform, permisos por operación, registro de invocaciones.

**Evidencia y evaluación.** Evidencia: inventario de conectores/MCP aprobados con permisos y estado; política de datos aplicada. Se evalúa que ningún agente use conectores fuera de la lista.

**Puentes.** Extiende M6.2-K04; se relaciona con AMP-36, AMP-49 y M6.2-PA01; sostiene AGC-06 y AGC-20.

**Recomendaciones de práctica y ejercitación.**
1. Inventariar conectores y servidores MCP en uso y definir la lista aprobada.
2. Aplicar la política de datos de Power Platform que bloquea el resto.
3. Revisar permisos por operación y registro de invocaciones de los conectores de escritura.

**Próximos pasos.**
- Registrar como AGC-06/AGC-20.
- Incluir MCP en el AI BOM (AMP-49).
- Revisar al agregar conectores (ChangeSet).

**Relación con los conceptos de la(s) unidad(es) M6.2.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M6.2-K01 | K | C-SCRM (Cadena Suministro) | misma unidad |
| M6.2-K02 | K | Seguridad Nube | misma unidad |
| M6.2-K03 | K | DevSecOps | misma unidad |
| M6.2-K04 | K | Seguridad IA | misma unidad |
| M6.2-K05 | K | IoT/OT Security | misma unidad |
| M6.2-K06 | K | Shadow AI | misma unidad |
| M6.2-K07 | K | Responsabilidad Compartida | misma unidad |
| M6.2-K08 | K | Riesgo Terceros (TPRM) | misma unidad |
| M6.2-K09 | K | SDLC Seguro | misma unidad |
| M6.2-K10 | K | SBOM | misma unidad |
| AMP-49 | AMP | Supply chain de modelos | misma unidad |
| AMP-51 | AMP | Postura de IA en nube | misma unidad |
| HC-008 | HC | Cadena de confianza en terceros | misma unidad |
| HC-011 | HC | Seguridad de datos en la IA empresarial | misma unidad |
| HC-023 | HC | Riesgo de concentración tecnológica | misma unidad |
| HC-024 | HC | Cumplimiento y privacidad por diseño | misma unidad |
| HC-029 | HC | Aseguramiento de terceros y cadena de suministro | misma unidad |
| HC-030 | HC | Seguridad industrial y continuidad de negocio | misma unidad |
| HC-031 | HC | Seguridad del software y confianza en componentes | misma unidad |
| HC-032 | HC | Evaluación adversarial de sistemas autónomos | misma unidad |
| HC-033 | HC | Seguridad y soberanía de datos distribuidos | misma unidad |
| M6.2-PA01 | PA | Plataformas y rutas de construcción de agentes y responsabilidad compartida en IA | misma unidad |
| M6.2-PA02 | PA | AgentOps / ALM de agentes | misma unidad |
| M6.2-PA03 | PA | Bases multiplataforma, multicloud y multimodelo | misma unidad |

**Pregunta generadora:** Si un servidor MCP que usan sus agentes fuera comprometido, ¿qué podría hacer en su tenant y cómo lo notaría?

---

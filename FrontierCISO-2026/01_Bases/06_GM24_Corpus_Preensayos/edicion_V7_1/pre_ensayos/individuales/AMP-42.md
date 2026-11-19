# Pre-ensayo · AMP-42

> **GM-24 V7.1 · The Next CISO + Sub-plan PO-GAC** · 2026-11-14. Catálogo: 379 conceptos (245 K · 52 AMP · 40 HC · 42 PA), todos con pre-ensayo íntegro y mapeados a 17 marcos (NIST/ISACA/MITRE/OWASP/CIS/CSA). V7.1 = ChangeSet editorial CS-GM24-V7.1-001 (4 títulos generalizados; sin cambio de IDs, cantidad ni mapeo). Plano A (corpus académico). Referencias DD/K4x/R/eo:OP/COE: marco interno.

### 084. AMP-42 — Envenenamiento de datos y modelos

**Unidad:** M4.2 Gestión de Amenazas, Vulnerabilidades y Riesgos Emergentes · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Referencias por ID (V7-C09):** OWASP LLM04/LLM08 (2025), ASI06 (2026 v2.01); MITRE ATLAS AML.T0020 · **Extensión:** 180 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** El envenenamiento ataca la integridad del aprendizaje (datos de entrenamiento o ajuste) y de la recuperación (fuentes de conocimiento, índices, memoria): el agente razona correctamente sobre información corrupta.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** El envenenamiento ataca la integridad del aprendizaje (datos de entrenamiento o ajuste) y de la recuperación (fuentes de conocimiento, índices, memoria): el agente razona correctamente sobre información corrupta. La defensa exige procedencia (de dónde viene cada fuente), control de fuentes (quién puede escribir en ellas) y monitoreo de comportamiento (cambios inexplicados en las decisiones). La tesis es que las fuentes de conocimiento de un agente son activos de integridad crítica y deben gobernarse como tales.

**Tensión y límites.** La tensión es que las fuentes útiles son las que se actualizan (runbooks, listas, históricos) y por eso son escribibles por muchos. El ensayo debe mostrar cómo separar lectura y escritura, y cómo detectar envenenamiento por sus efectos.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: integridad de datos, procedencia (lineage), OWASP LLM04/LLM08/ASI06, ATLAS. Implementación: control de procedencia y de escritura sobre knowledge sources (SharePoint/Dataverse/Git), versionado, monitoreo de cambios de comportamiento con el dataset dorado (M3.2-PA03).

**Evidencia y evaluación.** Evidencia: inventario de fuentes con procedencia y permisos de escritura; prueba de detección de un cambio inducido. Se evalúa la cobertura de fuentes escribibles.

**Puentes.** Extiende M4.2-K07; se relaciona con AMP-32, AMP-49 y M4.2-PA02; sostiene AGC-07.

**Recomendaciones de práctica y ejercitación.**
1. Inventariar las fuentes de conocimiento de la flota con procedencia y permisos de escritura.
2. Inducir un cambio en una fuente de prueba y verificar si el dataset dorado lo detecta.
3. Separar lectura/escritura y versionar las fuentes.

**Próximos pasos.**
- Registrar como control de integridad (AGC-07).
- Incluir en pruebas adversariales.
- Revisar al agregar fuentes.

**Relación con los conceptos de la(s) unidad(es) M4.2.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M4.2-K01 | K | Gestión Vulnerabilidades | misma unidad |
| M4.2-K02 | K | Modelado de Amenazas | misma unidad |
| M4.2-K03 | K | Amenaza Interna | misma unidad |
| M4.2-K04 | K | RaaS (Ransomware) | misma unidad |
| M4.2-K05 | K | Priorización por Riesgo | misma unidad |
| M4.2-K06 | K | Superficie de Ataque | misma unidad |
| M4.2-K07 | K | Riesgos Emergentes | misma unidad |
| M4.2-K08 | K | Economía del Cibercrimen | misma unidad |
| M4.2-K09 | K | STRIDE | misma unidad |
| M4.2-K10 | K | IoC (Indicadores) | misma unidad |
| AMP-41 | AMP | Prompt injection | misma unidad |
| HC-016 | HC | Superficie de ataque contextualizada | misma unidad |
| HC-026 | HC | Ética, cultura y controles internos | misma unidad |
| HC-031 | HC | Seguridad del software y confianza en componentes | misma unidad |
| HC-032 | HC | Evaluación adversarial de sistemas autónomos | misma unidad |
| M4.2-K11 | K | Escalamiento de privilegios en identidades humanas y no humanas como táctica adversaria | misma unidad |
| M4.2-PA01 | PA | Amenazas del dominio Zero Trust (instancias: correo y colaboración · cross-domain · endpoints · identidades · datos) | misma unidad |
| M4.2-PA02 | PA | Catálogos de amenazas a sistemas agénticos aplicados a la flota | misma unidad |

**Pregunta generadora:** ¿Quién puede escribir hoy en las fuentes que lee su agente, y qué pasaría si alguien cambiara una regla del runbook?

---

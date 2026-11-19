# Pre-ensayo · AMP-11

> **GM-24 V7.1 · The Next CISO + Sub-plan PO-GAC** · 2026-11-14. Catálogo: 379 conceptos (245 K · 52 AMP · 40 HC · 42 PA), todos con pre-ensayo íntegro y mapeados a 17 marcos (NIST/ISACA/MITRE/OWASP/CIS/CSA). V7.1 = ChangeSet editorial CS-GM24-V7.1-001 (4 títulos generalizados; sin cambio de IDs, cantidad ni mapeo). Plano A (corpus académico). Referencias DD/K4x/R/eo:OP/COE: marco interno.

### 053. AMP-11 — Soberanía de datos

**Unidad:** G3.1 Requisitos Legales, Regulatorios y Contractuales · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 190 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** La soberanía de datos es una restricción de diseño, no un trámite posterior: ubicación, jurisdicción, control de claves y acceso de terceros se deciden antes de desplegar IA, porque después el costo de cambiarlos es prohibitivo.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** La soberanía de datos es una restricción de diseño, no un trámite posterior: ubicación, jurisdicción, control de claves y acceso de terceros se deciden antes de desplegar IA, porque después el costo de cambiarlos es prohibitivo. Con agentes que recuperan datos de múltiples fuentes y los envían a modelos, la pregunta '¿dónde se procesa y bajo qué ley?' se multiplica por cada conector. La tesis es que el owner debe poder responderla para cada agente.

**Tensión y límites.** La tensión es entre soberanía y capacidad: los mejores modelos y servicios pueden no estar en la región; la restricción cuesta funcionalidad o dinero. El ensayo debe mostrar cómo decidir con criterios explícitos y cómo documentar la decisión para auditoría.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: residencia de datos, jurisdicción, gestión de claves (BYOK/HYOK), transferencias internacionales. Implementación: checklist de soberanía por agente (región de Foundry, residencia de Copilot Studio, claves en Purview/Key Vault, subprocesadores), aplicada a los quince agentes.

**Evidencia y evaluación.** Evidencia: checklist completada para la flota con decisiones y excepciones documentadas. Se evalúa la trazabilidad de cada decisión a un requisito legal o contractual.

**Puentes.** Se apoya en HC-033 (soberanía y transferencias); se relaciona con AMP-12 y G3.1-PA01; alimenta M6.2-PA01 (rutas).

**Recomendaciones de práctica y ejercitación.**
1. Completar la checklist de soberanía para los 15 agentes.
2. Identificar los conectores que mueven datos fuera de la jurisdicción.
3. Documentar la decisión de región y claves para Foundry y Copilot Studio.

**Próximos pasos.**
- Incluirla en el expediente ATO (AMP-22).
- Revisar ante cambios de región o de proveedor.
- Conectar con el anexo contractual (M1.2-PA02).

**Relación con los conceptos de la(s) unidad(es) G3.1.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| G3.1-K01 | K | Identificación de Requisitos | misma unidad |
| G3.1-K02 | K | Leyes de Privacidad | misma unidad |
| G3.1-K03 | K | Regulaciones Sectoriales | misma unidad |
| G3.1-K04 | K | Obligaciones Contractuales | misma unidad |
| G3.1-K05 | K | Implicaciones CISO | misma unidad |
| G3.1-K06 | K | Gestión de Privacidad | misma unidad |
| G3.1-K07 | K | Cumplimiento Integrado | misma unidad |
| G3.1-K08 | K | Riesgos Legales | misma unidad |
| G3.1-K09 | K | Auditorías de Cumplimiento | misma unidad |
| G3.1-K10 | K | Responsabilidad Legal | misma unidad |
| AMP-12 | AMP | Responsabilidad por agentes | misma unidad |
| HC-005 | HC | Cumplimiento continuo orientado a resultados | misma unidad |
| HC-008 | HC | Cadena de confianza en terceros | misma unidad |
| HC-011 | HC | Seguridad de datos en la IA empresarial | misma unidad |
| HC-024 | HC | Cumplimiento y privacidad por diseño | misma unidad |
| HC-029 | HC | Aseguramiento de terceros y cadena de suministro | misma unidad |
| HC-033 | HC | Seguridad y soberanía de datos distribuidos | misma unidad |
| G3.1-PA01 | PA | Panorama regulatorio de IA y agentes | misma unidad |

**Pregunta generadora:** ¿En qué región se procesa hoy el contenido de correo que lee su agente de triaje, y quién lo decidió?

---

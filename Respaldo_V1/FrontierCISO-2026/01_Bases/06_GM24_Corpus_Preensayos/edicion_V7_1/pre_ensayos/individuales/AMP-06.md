# Pre-ensayo · AMP-06

> **GM-24 V7.1 · The Next CISO + Sub-plan PO-GAC** · 2026-11-14. Catálogo: 379 conceptos (245 K · 52 AMP · 40 HC · 42 PA), todos con pre-ensayo íntegro y mapeados a 17 marcos (NIST/ISACA/MITRE/OWASP/CIS/CSA). V7.1 = ChangeSet editorial CS-GM24-V7.1-001 (4 títulos generalizados; sin cambio de IDs, cantidad ni mapeo). Plano A (corpus académico). Referencias DD/K4x/R/eo:OP/COE: marco interno.

### 048. AMP-06 — Gobierno de la IA

**Unidad:** G1.2 Desarrollo de Estrategia y Alineación con el Negocio · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 231 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** Gobernar la IA es decidir quién la usa, con qué datos, con qué autonomía y con qué evidencia.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** Gobernar la IA es decidir quién la usa, con qué datos, con qué autonomía y con qué evidencia. Esas cuatro decisiones son el núcleo de cualquier marco (AI RMF, ISO/IEC 42001) y, sin ellas, Copilot y los agentes se adoptan sin dueños ni límites. La tesis es que el gobierno de la IA no requiere un comité nuevo sino cuatro respuestas escritas y aplicadas por la plataforma y por las personas, integradas al SGSI existente.

**Tensión y límites.** La tensión es la velocidad de adopción frente a la lentitud del gobierno: los usuarios ya crean agentes mientras el comité discute la política. La respuesta es gobernar primero lo que la plataforma permite aplicar (entornos, conectores, DLP, identidad) y después el resto. Otra tensión es la duplicación de estructuras de gobierno (SGSI, privacidad, IA).

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: NIST AI RMF (GOVERN), ISO/IEC 42001, principios de IA responsable. Implementación: las cuatro respuestas para la flota del control (quién: PO-GAC con sponsor; datos: fuentes aprobadas vía Purview; autonomía: L0–L3 con apetito declarado; evidencia: trazas en Sentinel/Agent 365), aplicadas en Power Platform admin center y Copilot Control System.

**Evidencia y evaluación.** Evidencia: documento de principios de gobierno de IA del programa (dos páginas) y matriz de aplicación técnica. Se evalúa que cada principio tenga un control de plataforma o un control humano asignado.

**Puentes.** Extiende M6.2-K06 (Shadow AI); es la base de G2.1-PA02 (marcos) y G2.2-PA01 (política de agentes); se relaciona con AMP-30.

**Recomendaciones de práctica y ejercitación.**
1. Escribir las cuatro respuestas (quién, datos, autonomía, evidencia) para la flota del control.
2. Mapear cada respuesta a un control de plataforma o humano.
3. Inventariar quién puede crear agentes hoy y con qué conectores.

**Próximos pasos.**
- Derivar la política de agentes (G2.2-PA01).
- Mapear a AI RMF e ISO 42001 (G2.1-PA02).
- Revisar tras cambios de plataforma (AG-09).

**Relación con los conceptos de la(s) unidad(es) G1.2.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| G1.2-K01 | K | Estrategia de Ciberseguridad | misma unidad |
| G1.2-K02 | K | Alineación con Negocio | misma unidad |
| G1.2-K03 | K | Influencias y Tendencias | misma unidad |
| G1.2-K04 | K | Conexión de Valor | misma unidad |
| G1.2-K05 | K | Casos de Negocio | misma unidad |
| G1.2-K06 | K | ROI en Seguridad | misma unidad |
| G1.2-K07 | K | Visión de Negocio | misma unidad |
| G1.2-K08 | K | Planificación Estratégica | misma unidad |
| G1.2-K09 | K | Integración ERM | misma unidad |
| G1.2-K10 | K | Comunicación a la Junta | misma unidad |
| AMP-04 | AMP | Estrategia adaptativa | misma unidad |
| AMP-05 | AMP | Evolución contextual H | misma unidad |
| HC-006 | HC | Valor de seguridad y medición causal | misma unidad |
| HC-013 | HC | Deuda de seguridad como riesgo de transformación | misma unidad |
| HC-014 | HC | Arquitectura de riesgo empresarial | misma unidad |
| HC-023 | HC | Riesgo de concentración tecnológica | misma unidad |
| HC-034 | HC | Decisiones reversibles y riesgo de transición | misma unidad |
| HC-035 | HC | Aprendizaje desde incidentes hasta políticas | misma unidad |
| HC-039 | HC | Riesgo cibernético como narrativa empresarial | misma unidad |
| G1.2-PA01 | PA | Economía unitaria de agentes: caso de negocio y TCO | misma unidad |

**Pregunta generadora:** ¿Quién, en su organización, puede hoy crear un agente que lea correo corporativo, y qué lo detiene?

---

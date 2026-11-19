# Pre-ensayo · AMP-02

> **GM-24 V7.1 · The Next CISO + Sub-plan PO-GAC** · 2026-11-14. Catálogo: 379 conceptos (245 K · 52 AMP · 40 HC · 42 PA), todos con pre-ensayo íntegro y mapeados a 17 marcos (NIST/ISACA/MITRE/OWASP/CIS/CSA). V7.1 = ChangeSet editorial CS-GM24-V7.1-001 (4 títulos generalizados; sin cambio de IDs, cantidad ni mapeo). Plano A (corpus académico). Referencias DD/K4x/R/eo:OP/COE: marco interno.

### 044. AMP-02 — Sesgos y límites cognitivos

**Unidad:** G1.1 Principios de Gobierno, Contexto Organizacional y Arquetipos CISO · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 254 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** Anclaje, confirmación y sesgo de automatización distorsionan las decisiones de riesgo de forma predecible: el primer número fija la estimación, la evidencia que confirma pesa más que la que contradice y la recomendación de una máquina se acepta con menos escrutinio que la de una persona.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** Anclaje, confirmación y sesgo de automatización distorsionan las decisiones de riesgo de forma predecible: el primer número fija la estimación, la evidencia que confirma pesa más que la que contradice y la recomendación de una máquina se acepta con menos escrutinio que la de una persona. Con asistentes de IA en el SOC y en el comité de riesgo, el tercer sesgo se vuelve dominante. La tesis es que la verificación humana debe diseñarse como proceso —quién verifica, con qué información, en cuánto tiempo— y no suponerse como actitud.

**Tensión y límites.** La tensión es que la verificación cuesta: si cada recomendación del asistente se revisa a fondo, el asistente no ahorra nada; si ninguna se revisa, el sesgo de automatización gobierna. El diseño debe graduar la verificación por riesgo y reversibilidad (lo que AMP-40 llama HITL por riesgo) y medir la tasa de corrección humana como señal de salud, no de fracaso.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: psicología de la decisión aplicada al riesgo; listas de verificación; muestreo. Implementación: en el triaje asistido por AG-01, una checklist de verificación en las aprobaciones L2 (¿qué evidencia miré además de la propuesta?, ¿qué habría decidido sin ella?) y la métrica de propuestas corregidas (KPI-11 leído al revés).

**Evidencia y evaluación.** Evidencia: un experimento de dos semanas comparando decisiones con y sin recomendación del asistente en los mismos casos; informe de sesgo observado. Se evalúa el diseño del experimento y la lectura prudente de los resultados.

**Puentes.** Extiende M4.1-K08 (IA en SecOps) y AMP-01 (metacognición); sostiene AMP-26 (supervisión efectiva) y AMP-40 (HITL); se relaciona con G6.1-K05.

**Recomendaciones de práctica y ejercitación.**
1. Diseñar la checklist de verificación para aprobaciones L2 de AG-01 y AG-02.
2. Correr un experimento A/B de dos semanas sobre decisiones de triaje con y sin recomendación.
3. Definir la tasa de corrección humana esperada y qué significa que sea 0 %.

**Próximos pasos.**
- Incorporar la checklist a la ficha de agente (G2.2-PA02).
- Vincular con la evaluación de calidad del agente (M3.2-PA03).
- Revisar el sesgo de automatización en la revisión trimestral (M4.1-PA06).

**Relación con los conceptos de la(s) unidad(es) G1.1.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| G1.1-K01 | K | Principios de Gobierno | misma unidad |
| G1.1-K02 | K | Contexto Organizacional | misma unidad |
| G1.1-K03 | K | Arquetipos CISO | misma unidad |
| G1.1-K04 | K | Alineación Estratégica | misma unidad |
| G1.1-K05 | K | Cultura de Seguridad | misma unidad |
| G1.1-K06 | K | Visión Holística | misma unidad |
| G1.1-K07 | K | CISO como Socio de Negocio | misma unidad |
| G1.1-K08 | K | Gestión Estratégica del Riesgo | misma unidad |
| G1.1-K09 | K | Liderazgo de Influencia | misma unidad |
| G1.1-K10 | K | Mejora Continua (Gobierno) | misma unidad |
| AMP-01 | AMP | Metacognición del CISO | misma unidad |
| AMP-03 | AMP | Autoridad frente a responsabilidad | misma unidad |
| HC-001 | HC | Gobierno de decisiones basadas en evidencia | misma unidad |
| HC-037 | HC | Alineación entre competencias y decisiones | misma unidad |
| HC-040 | HC | Homeostasis organizacional de seguridad | misma unidad |
| G1.1-PA01 | PA | Rol dual especialista/manager y Product Owner de control | misma unidad |

**Pregunta generadora:** Si el asistente de triaje se equivocara el 10 % de las veces con total seguridad en su redacción, ¿cuántas de esas veces su equipo lo notaría hoy?

---

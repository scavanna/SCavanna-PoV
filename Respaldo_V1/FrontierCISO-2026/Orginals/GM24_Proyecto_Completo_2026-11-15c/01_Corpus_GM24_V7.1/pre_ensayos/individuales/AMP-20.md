# Pre-ensayo · AMP-20

> **GM-24 V7.1 · The Next CISO + Sub-plan PO-GAC** · 2026-11-14. Catálogo: 379 conceptos (245 K · 52 AMP · 40 HC · 42 PA), todos con pre-ensayo íntegro y mapeados a 17 marcos (NIST/ISACA/MITRE/OWASP/CIS/CSA). V7.1 = ChangeSet editorial CS-GM24-V7.1-001 (4 títulos generalizados; sin cambio de IDs, cantidad ni mapeo). Plano A (corpus académico). Referencias DD/K4x/R/eo:OP/COE: marco interno.

### 062. AMP-20 — Riesgo de modelos de IA

**Unidad:** G5.1 Supervisión de la Evaluación y Análisis · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 184 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** Los modelos introducen riesgos propios —error, deriva, sesgo, manipulación y dependencia de proveedor— que deben evaluarse como riesgo empresarial, no como detalle técnico.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** Los modelos introducen riesgos propios —error, deriva, sesgo, manipulación y dependencia de proveedor— que deben evaluarse como riesgo empresarial, no como detalle técnico. Un modelo que clasifica incidentes puede degradarse sin aviso cuando cambian las amenazas o cuando el proveedor lo actualiza. La tesis es que cada modelo que usa la flota tiene un perfil de riesgo propio que el registro debe recoger y que la evaluación periódica debe vigilar.

**Tensión y límites.** La tensión es la opacidad: el owner no controla el modelo del proveedor ni conoce sus cambios. Otra tensión es la novedad del vocabulario para el comité de riesgo. El ensayo debe traducir los cinco riesgos a escenarios de negocio.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: AI RMF MAP/MEASURE, model risk management (origen financiero), NIST AI 600-1. Implementación: evaluación de riesgo de los modelos del catálogo de Foundry usados por la flota (error, deriva, sesgo, manipulación, dependencia), con KRIs y plan de evaluación periódica.

**Evidencia y evaluación.** Evidencia: perfil de riesgo de dos modelos en uso con escenarios, KRIs y tratamiento. Se evalúa la traducción a escenarios de negocio.

**Puentes.** Extiende M4.2-K07 (riesgos emergentes); se relaciona con AMP-48, AMP-42, G4.1-PA02 y M3.2-PA03.

**Recomendaciones de práctica y ejercitación.**
1. Perfilar el riesgo de dos modelos de la flota con los cinco riesgos y escenarios.
2. Definir KRIs de deriva y su fuente (evaluación periódica).
3. Registrar la dependencia de proveedor con plan alternativo.

**Próximos pasos.**
- Incorporar al registro de riesgos (G4.1-PA02).
- Programar la reevaluación (MDO-Q04).
- Vincular con la cadena de suministro de modelos (AMP-49).

**Relación con los conceptos de la(s) unidad(es) G5.1.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| G5.1-K01 | K | Supervisión del Proceso | misma unidad |
| G5.1-K02 | K | Metodologías | misma unidad |
| G5.1-K03 | K | Revisión de Resultados | misma unidad |
| G5.1-K04 | K | Identificación de Brechas | misma unidad |
| G5.1-K05 | K | Monitorización Continua | misma unidad |
| G5.1-K06 | K | Análisis Cuanti/Cuali | misma unidad |
| G5.1-K07 | K | Evaluación Amenazas | misma unidad |
| G5.1-K08 | K | Escenarios de Riesgo | misma unidad |
| G5.1-K09 | K | Herramientas GRC | misma unidad |
| G5.1-K10 | K | Auditoría Interna | misma unidad |
| AMP-19 | AMP | Calidad epistemológica de evidencia | misma unidad |
| HC-001 | HC | Gobierno de decisiones basadas en evidencia | misma unidad |
| HC-016 | HC | Superficie de ataque contextualizada | misma unidad |
| HC-017 | HC | Inteligencia que modifica decisiones | misma unidad |
| HC-039 | HC | Riesgo cibernético como narrativa empresarial | misma unidad |

**Pregunta generadora:** Si el proveedor actualizara mañana el modelo que usa su agente de triaje, ¿cómo se enteraría y qué haría?

---

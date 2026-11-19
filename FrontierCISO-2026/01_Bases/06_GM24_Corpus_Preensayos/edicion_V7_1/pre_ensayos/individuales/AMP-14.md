# Pre-ensayo · AMP-14

> **GM-24 V7.1 · The Next CISO + Sub-plan PO-GAC** · 2026-11-14. Catálogo: 379 conceptos (245 K · 52 AMP · 40 HC · 42 PA), todos con pre-ensayo íntegro y mapeados a 17 marcos (NIST/ISACA/MITRE/OWASP/CIS/CSA). V7.1 = ChangeSet editorial CS-GM24-V7.1-001 (4 títulos generalizados; sin cambio de IDs, cantidad ni mapeo). Plano A (corpus académico). Referencias DD/K4x/R/eo:OP/COE: marco interno.

### 056. AMP-14 — Aseguramiento de decisiones de IA

**Unidad:** G3.2 Gestión del Cumplimiento y Aseguramiento Continuo · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 188 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** Afirmar que una decisión asistida por IA es confiable exige pruebas, registros y revisión independiente, no solo métricas de desempeño del modelo.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** Afirmar que una decisión asistida por IA es confiable exige pruebas, registros y revisión independiente, no solo métricas de desempeño del modelo. Una precisión del 92 % no dice nada sobre los casos en que el modelo se equivoca con seguridad ni sobre si el humano que revisa realmente revisa. La tesis es que el aseguramiento de decisiones de IA combina evaluación del sistema, trazabilidad de cada decisión y una tercera línea que muestrea.

**Tensión y límites.** La tensión es que las métricas del modelo son fáciles de obtener y las otras dos piezas son caras. También está la opacidad: no siempre se puede explicar por qué el modelo decidió. El ensayo debe mostrar qué nivel de aseguramiento corresponde a cada nivel de autonomía.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: AI RMF MEASURE, auditoría de algoritmos, muestreo estadístico. Implementación: para AG-01, combinar evaluación con dataset dorado (M3.2-PA03), trazas por decisión (AMP-46) y muestreo trimestral independiente por la segunda línea.

**Evidencia y evaluación.** Evidencia: plan de aseguramiento de decisiones para un agente con las tres piezas y el primer muestreo. Se evalúa la independencia del muestreo.

**Puentes.** Se apoya en HC-012 (confianza verificable); se relaciona con M3.2-PA03, AMP-46 y G4.1-PA01.

**Recomendaciones de práctica y ejercitación.**
1. Diseñar el plan de aseguramiento de decisiones de AG-01 (evaluación, trazas, muestreo).
2. Ejecutar un muestreo de 30 decisiones por alguien ajeno al equipo.
3. Comparar la precisión declarada con la precisión observada en el muestreo.

**Próximos pasos.**
- Institucionalizar el muestreo en la revisión trimestral (M4.1-PA06).
- Entregar resultados a auditoría (AGC-22).
- Ajustar el nivel de autonomía según resultados.

**Relación con los conceptos de la(s) unidad(es) G3.2.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| G3.2-K01 | K | Procesos de Gestión | misma unidad |
| G3.2-K02 | K | Aseguramiento Continuo | misma unidad |
| G3.2-K03 | K | Supervisión de Auditorías | misma unidad |
| G3.2-K04 | K | Reporte de Incumplimiento | misma unidad |
| G3.2-K05 | K | Estrategias Proactivas | misma unidad |
| G3.2-K06 | K | Gestión de Evidencia | misma unidad |
| G3.2-K07 | K | Automatización | misma unidad |
| G3.2-K08 | K | KPIs de Cumplimiento | misma unidad |
| G3.2-K09 | K | Formación en Cumplimiento | misma unidad |
| G3.2-K10 | K | Relación con Reguladores | misma unidad |
| AMP-13 | AMP | Evidencia continua | misma unidad |
| HC-003 | HC | Riesgo residual y aceptación verificable | misma unidad |
| HC-004 | HC | Política como código gobernado | misma unidad |
| HC-005 | HC | Cumplimiento continuo orientado a resultados | misma unidad |
| HC-012 | HC | Confianza verificable en decisiones de IA | misma unidad |
| HC-018 | HC | Observabilidad y aseguramiento de controles | misma unidad |
| HC-024 | HC | Cumplimiento y privacidad por diseño | misma unidad |
| HC-029 | HC | Aseguramiento de terceros y cadena de suministro | misma unidad |
| G3.2-PA01 | PA | Aseguramiento continuo de la configuración del control (deriva) | misma unidad |

**Pregunta generadora:** ¿Qué sabe hoy de las decisiones de su asistente de triaje además de su tasa de acierto?

---

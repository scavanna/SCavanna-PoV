# Pre-ensayo · AMP-13

> **GM-24 V7.1 · The Next CISO + Sub-plan PO-GAC** · 2026-11-14. Catálogo: 379 conceptos (245 K · 52 AMP · 40 HC · 42 PA), todos con pre-ensayo íntegro y mapeados a 17 marcos (NIST/ISACA/MITRE/OWASP/CIS/CSA). V7.1 = ChangeSet editorial CS-GM24-V7.1-001 (4 títulos generalizados; sin cambio de IDs, cantidad ni mapeo). Plano A (corpus académico). Referencias DD/K4x/R/eo:OP/COE: marco interno.

### 055. AMP-13 — Evidencia continua

**Unidad:** G3.2 Gestión del Cumplimiento y Aseguramiento Continuo · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 191 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** El aseguramiento moderno se apoya en evidencia continua generada por los propios controles —informes automáticos, logs, estados de configuración— pero su valor depende de tres atributos: alcance (qué cubre y qué no), integridad (que nadie la haya alterado) y responsable (quién responde por ella).

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** El aseguramiento moderno se apoya en evidencia continua generada por los propios controles —informes automáticos, logs, estados de configuración— pero su valor depende de tres atributos: alcance (qué cubre y qué no), integridad (que nadie la haya alterado) y responsable (quién responde por ella). La tesis es que la evidencia continua no reemplaza al aseguramiento sino que cambia su objeto: ya no se audita el control, se audita la evidencia y su cadena.

**Tensión y límites.** La tensión es la abundancia: miles de registros que nadie lee producen una falsa sensación de control. Otra tensión es la circularidad: el control genera la evidencia de su propio funcionamiento; sin verificación independiente, un control roto puede reportar que funciona.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: continuous controls monitoring, cadena de custodia de evidencia, integridad de logs. Implementación: inventario de evidencias continuas del control (Configuration Analyzer, informes de protección, logs de agentes en Sentinel, Purview Audit) con alcance, integridad (retención inmutable) y responsable.

**Evidencia y evaluación.** Evidencia: inventario de evidencias continuas con los tres atributos y una prueba de integridad. Se evalúa la identificación de evidencias circulares y su compensación.

**Puentes.** Extiende G3.2-K02 (aseguramiento continuo); sostiene G3.2-PA01 y AGC-11; se relaciona con AMP-46 y HC-005.

**Recomendaciones de práctica y ejercitación.**
1. Inventariar las evidencias continuas del control con alcance, integridad y responsable.
2. Identificar evidencias circulares y proponer la verificación independiente.
3. Probar la integridad de una fuente de evidencia (retención, inmutabilidad).

**Próximos pasos.**
- Conectar con la auditoría interna (AGC-22).
- Usar el inventario en el expediente ATO.
- Mapear a ISO 27001/42001 (HC-005).

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
| AMP-14 | AMP | Aseguramiento de decisiones de IA | misma unidad |
| HC-003 | HC | Riesgo residual y aceptación verificable | misma unidad |
| HC-004 | HC | Política como código gobernado | misma unidad |
| HC-005 | HC | Cumplimiento continuo orientado a resultados | misma unidad |
| HC-012 | HC | Confianza verificable en decisiones de IA | misma unidad |
| HC-018 | HC | Observabilidad y aseguramiento de controles | misma unidad |
| HC-024 | HC | Cumplimiento y privacidad por diseño | misma unidad |
| HC-029 | HC | Aseguramiento de terceros y cadena de suministro | misma unidad |
| G3.2-PA01 | PA | Aseguramiento continuo de la configuración del control (deriva) | misma unidad |

**Pregunta generadora:** De las evidencias que su control produce automáticamente, ¿cuál podría estar diciendo que todo funciona mientras el control está roto?

---

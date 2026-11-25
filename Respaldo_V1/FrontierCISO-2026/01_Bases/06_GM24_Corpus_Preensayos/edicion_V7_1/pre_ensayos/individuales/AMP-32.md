# Pre-ensayo · AMP-32

> **GM-24 V7.1 · The Next CISO + Sub-plan PO-GAC** · 2026-11-14. Catálogo: 379 conceptos (245 K · 52 AMP · 40 HC · 42 PA), todos con pre-ensayo íntegro y mapeados a 17 marcos (NIST/ISACA/MITRE/OWASP/CIS/CSA). V7.1 = ChangeSet editorial CS-GM24-V7.1-001 (4 títulos generalizados; sin cambio de IDs, cantidad ni mapeo). Plano A (corpus académico). Referencias DD/K4x/R/eo:OP/COE: marco interno.

### 074. AMP-32 — Gobierno de datos para RAG

**Unidad:** M2.1 Gestión de Activos y Seguridad del Ciclo de Vida de los Datos · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 180 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** En RAG (generación aumentada por recuperación) la IA hereda los permisos y la calidad de los datos que recupera: sin clasificación, permisos correctos y control de sobrecompartición, el agente expone lo que nadie debía ver y razona sobre lo que nadie validó.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** En RAG (generación aumentada por recuperación) la IA hereda los permisos y la calidad de los datos que recupera: sin clasificación, permisos correctos y control de sobrecompartición, el agente expone lo que nadie debía ver y razona sobre lo que nadie validó. La tesis es que el gobierno de datos para RAG tiene tres controles mínimos —fuentes aprobadas, permisos verificados, calidad y procedencia— y que el owner los aplica por agente.

**Tensión y límites.** La tensión es que los agentes son más útiles cuanto más datos alcanzan; cada restricción cuesta capacidad. Otra tensión es la calidad: una fuente desactualizada produce respuestas seguras y erróneas. El ensayo debe argumentar fuentes pocas y curadas.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: gobierno de datos, data lineage, mínimo privilegio aplicado a datos. Implementación: política de datos de los agentes del control (fuentes aprobadas en SharePoint/Dataverse, etiquetas de sensibilidad, DLP para agentes, revisión de procedencia de knowledge sources).

**Evidencia y evaluación.** Evidencia: política de datos aplicada y verificación de fuentes de tres agentes. Se evalúa que ninguna fuente no aprobada esté conectada.

**Puentes.** Se apoya en HC-011; se relaciona con AMP-31, AMP-42 y M2.1-PA01; sostiene AGC-07.

**Recomendaciones de práctica y ejercitación.**
1. Redactar la política de datos de los agentes (fuentes, permisos, calidad).
2. Verificar las fuentes de conocimiento de AG-01, AG-02 y AG-14.
3. Configurar DLP de Purview para agentes y probarlo.

**Próximos pasos.**
- Registrar como AGC-07.
- Revisar fuentes en cada cambio de agente.
- Conectar con la procedencia (AMP-42).

**Relación con los conceptos de la(s) unidad(es) M2.1.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M2.1-K01 | K | Identificación Activos | misma unidad |
| M2.1-K02 | K | Clasificación | misma unidad |
| M2.1-K03 | K | Inventario | misma unidad |
| M2.1-K04 | K | Ciclo de Vida Datos | misma unidad |
| M2.1-K05 | K | Seguridad Reposo/Tránsito | misma unidad |
| M2.1-K06 | K | Retención/Destrucción | misma unidad |
| M2.1-K07 | K | Gobernanza Datos | misma unidad |
| M2.1-K08 | K | Activos Críticos | misma unidad |
| M2.1-K09 | K | Auditoría Activos | misma unidad |
| M2.1-K10 | K | Riesgos de Datos | misma unidad |
| AMP-31 | AMP | DSPM | misma unidad |
| HC-011 | HC | Seguridad de datos en la IA empresarial | misma unidad |
| HC-014 | HC | Arquitectura de riesgo empresarial | misma unidad |
| HC-016 | HC | Superficie de ataque contextualizada | misma unidad |
| HC-024 | HC | Cumplimiento y privacidad por diseño | misma unidad |
| HC-033 | HC | Seguridad y soberanía de datos distribuidos | misma unidad |
| M2.1-PA01 | PA | Registro de agentes como clase de activo | misma unidad |

**Pregunta generadora:** ¿Quién aprobó cada fuente de conocimiento conectada a sus agentes, y cuándo se revisó su calidad por última vez?

---

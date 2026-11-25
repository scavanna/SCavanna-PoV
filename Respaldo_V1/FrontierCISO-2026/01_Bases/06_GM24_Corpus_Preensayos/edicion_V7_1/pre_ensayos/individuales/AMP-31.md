# Pre-ensayo · AMP-31

> **GM-24 V7.1 · The Next CISO + Sub-plan PO-GAC** · 2026-11-14. Catálogo: 379 conceptos (245 K · 52 AMP · 40 HC · 42 PA), todos con pre-ensayo íntegro y mapeados a 17 marcos (NIST/ISACA/MITRE/OWASP/CIS/CSA). V7.1 = ChangeSet editorial CS-GM24-V7.1-001 (4 títulos generalizados; sin cambio de IDs, cantidad ni mapeo). Plano A (corpus académico). Referencias DD/K4x/R/eo:OP/COE: marco interno.

### 073. AMP-31 — DSPM

**Unidad:** M2.1 Gestión de Activos y Seguridad del Ciclo de Vida de los Datos · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 180 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** DSPM (Data Security Posture Management) convierte la protección de datos en gestión continua de exposición: dónde está el dato sensible, quién puede acceder y qué remediar primero.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** DSPM (Data Security Posture Management) convierte la protección de datos en gestión continua de exposición: dónde está el dato sensible, quién puede acceder y qué remediar primero. Para una flota de agentes la pregunta se vuelve 'qué dato sensible alcanza cada agente a través de sus fuentes y conectores'. La tesis es que el owner debe conocer la exposición de datos de la flota antes de ampliar su autonomía.

**Tensión y límites.** La tensión es la sobrecompartición heredada: los agentes exponen lo que los permisos ya permitían pero nadie veía. Corregirla es un proyecto de datos, no de agentes. El ensayo debe mostrar cómo priorizar la remediación por lo que los agentes alcanzan.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: DSPM, clasificación, gestión de exposición. Implementación: informe DSPM for AI de Purview sobre el alcance de la flota (sitios, buzones, tablas), priorización de remediación y restricción de fuentes de conocimiento.

**Evidencia y evaluación.** Evidencia: informe de exposición de datos de la flota con remediaciones priorizadas. Se evalúa la cobertura del alcance real de los agentes.

**Puentes.** Se apoya en HC-011 (flujo de información sensible); se relaciona con AMP-32 y M2.1-PA01; sostiene AGC-07.

**Recomendaciones de práctica y ejercitación.**
1. Ejecutar DSPM for AI sobre el alcance de la flota y listar exposiciones.
2. Priorizar remediaciones por agente y nivel de autonomía.
3. Restringir fuentes de conocimiento de AG-02 y AG-14.

**Próximos pasos.**
- Conectar con la política de datos (AMP-32).
- Incluir en el expediente ATO.
- Repetir trimestralmente.

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
| AMP-32 | AMP | Gobierno de datos para RAG | misma unidad |
| HC-011 | HC | Seguridad de datos en la IA empresarial | misma unidad |
| HC-014 | HC | Arquitectura de riesgo empresarial | misma unidad |
| HC-016 | HC | Superficie de ataque contextualizada | misma unidad |
| HC-024 | HC | Cumplimiento y privacidad por diseño | misma unidad |
| HC-033 | HC | Seguridad y soberanía de datos distribuidos | misma unidad |
| M2.1-PA01 | PA | Registro de agentes como clase de activo | misma unidad |

**Pregunta generadora:** ¿Qué dato sensible podría leer hoy su agente de investigación que ningún analista debería ver?

---

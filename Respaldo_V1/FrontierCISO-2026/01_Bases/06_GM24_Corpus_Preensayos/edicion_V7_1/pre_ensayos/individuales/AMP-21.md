# Pre-ensayo · AMP-21

> **GM-24 V7.1 · The Next CISO + Sub-plan PO-GAC** · 2026-11-14. Catálogo: 379 conceptos (245 K · 52 AMP · 40 HC · 42 PA), todos con pre-ensayo íntegro y mapeados a 17 marcos (NIST/ISACA/MITRE/OWASP/CIS/CSA). V7.1 = ChangeSet editorial CS-GM24-V7.1-001 (4 títulos generalizados; sin cambio de IDs, cantidad ni mapeo). Plano A (corpus académico). Referencias DD/K4x/R/eo:OP/COE: marco interno.

### 063. AMP-21 — Decisiones reversibles

**Unidad:** G5.2 Supervisión del Tratamiento y Aceptación · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 174 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** Preferir decisiones reversibles reduce el costo de equivocarse en transformaciones inciertas: si se puede volver atrás, se puede avanzar con menos información.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** Preferir decisiones reversibles reduce el costo de equivocarse en transformaciones inciertas: si se puede volver atrás, se puede avanzar con menos información. Pero la reversibilidad debe diseñarse y probarse: una acción 'reversible' que nadie revirtió nunca no lo es. La tesis es que la reversibilidad es un criterio de diseño para otorgar autonomía (L3 solo a acciones reversibles) y un control que se ensaya.

**Tensión y límites.** La tensión es que la reversibilidad cuesta (eliminación suave en vez de definitiva, versiones, respaldos) y que algunas acciones son irreversibles por naturaleza (una notificación enviada). El ensayo debe mostrar cómo clasificar y cómo tratar lo irreversible.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: decisiones de una y dos vías, rollback, versionado. Implementación: clasificar las acciones de los agentes por reversibilidad; preferir soft delete, bloqueos con vencimiento y despliegue por versiones; probar la reversión de una acción de AG-02 y de un cambio de agente (ALM).

**Evidencia y evaluación.** Evidencia: clasificación de acciones por reversibilidad y dos pruebas de reversión documentadas. Se evalúa el realismo de la clasificación.

**Puentes.** Se apoya en HC-034; sostiene AMP-04, AMP-18, M5.2-PA01 y M6.2-PA02.

**Recomendaciones de práctica y ejercitación.**
1. Clasificar las acciones de los 15 agentes por reversibilidad e impacto.
2. Probar la reversión de una remediación de correo y de un cambio de instrucción.
3. Definir qué acciones irreversibles quedan en L1.

**Próximos pasos.**
- Usar la clasificación en el árbol de decisión de autonomía.
- Incluir pruebas de reversión en el pipeline (M6.2-PA02).
- Revisar en el post-mortem (M5.2-PA02).

**Relación con los conceptos de la(s) unidad(es) G5.2.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| G5.2-K01 | K | Supervisión de Respuestas | misma unidad |
| G5.2-K02 | K | Alineación con Apetito | misma unidad |
| G5.2-K03 | K | Autorización Residual | misma unidad |
| G5.2-K04 | K | Mitigación | misma unidad |
| G5.2-K05 | K | Transferencia | misma unidad |
| G5.2-K06 | K | Evitación | misma unidad |
| G5.2-K07 | K | Gestión Residual | misma unidad |
| G5.2-K08 | K | Comunicación Decisiones | misma unidad |
| G5.2-K09 | K | Métricas Mitigación | misma unidad |
| G5.2-K10 | K | Auditoría Tratamiento | misma unidad |
| AMP-22 | AMP | Aceptación de riesgo de agentes | misma unidad |
| HC-003 | HC | Riesgo residual y aceptación verificable | misma unidad |
| HC-028 | HC | Gestión de excepciones y compensaciones | misma unidad |
| HC-034 | HC | Decisiones reversibles y riesgo de transición | misma unidad |

**Pregunta generadora:** ¿Qué acción de su flota considera reversible, y cuándo fue la última vez que alguien la revirtió de verdad?

---

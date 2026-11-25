# Pre-ensayo · AMP-38

> **GM-24 V7.1 · The Next CISO + Sub-plan PO-GAC** · 2026-11-14. Catálogo: 379 conceptos (245 K · 52 AMP · 40 HC · 42 PA), todos con pre-ensayo íntegro y mapeados a 17 marcos (NIST/ISACA/MITRE/OWASP/CIS/CSA). V7.1 = ChangeSet editorial CS-GM24-V7.1-001 (4 títulos generalizados; sin cambio de IDs, cantidad ni mapeo). Plano A (corpus académico). Referencias DD/K4x/R/eo:OP/COE: marco interno.

### 080. AMP-38 — Pruebas de controles autónomos

**Unidad:** M3.2 Selección, Implementación y Evaluación de Controles · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 194 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** Los controles que actúan solos —bloqueo, contención, remediación automática— deben probarse en escenarios de falla y con rollback antes de confiarles decisiones: qué pasa si el control actúa sobre un falso positivo masivo, si la fuente de datos falla, si la acción no se puede revertir.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** Los controles que actúan solos —bloqueo, contención, remediación automática— deben probarse en escenarios de falla y con rollback antes de confiarles decisiones: qué pasa si el control actúa sobre un falso positivo masivo, si la fuente de datos falla, si la acción no se puede revertir. La tesis es que la prueba de controles autónomos es una disciplina distinta de la prueba de detección: se prueba el daño que el control puede causar.

**Tensión y límites.** La tensión es que los controles autónomos nativos (AIR, ZAP) vienen activados y probados por el fabricante; el owner tiende a no probarlos. Pero su configuración local y sus agentes propios cambian el comportamiento. El ensayo debe mostrar cómo probar en escenarios de falla sin romper producción.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: pruebas de resiliencia, ingeniería del caos aplicada a controles, rollback. Implementación: probar AIR y ZAP con falsos positivos controlados en el entorno de prueba, probar AG-10 en modo corrección con un cambio inducido, medir rollback.

**Evidencia y evaluación.** Evidencia: informe de pruebas de dos controles autónomos en escenarios de falla con rollback medido. Se evalúa la identificación de modos de daño.

**Puentes.** Extiende M3.2-K09 (pruebas de efectividad); se relaciona con AMP-21, AMP-44 y M5.2-PA01; sostiene AGC-12.

**Recomendaciones de práctica y ejercitación.**
1. Diseñar escenarios de falla para AIR/ZAP y para AG-10.
2. Ejecutarlos en el entorno de prueba y medir el rollback.
3. Documentar modos de daño y límites recomendados.

**Próximos pasos.**
- Incorporar límites de lote a las fichas.
- Programar pruebas periódicas (MDO-Q04).
- Conectar con el tabletop (AMP-43).

**Relación con los conceptos de la(s) unidad(es) M3.2.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M3.2-K01 | K | Controles de Seguridad | misma unidad |
| M3.2-K02 | K | NIST SP 800-53 | misma unidad |
| M3.2-K03 | K | Selección y Adaptación | misma unidad |
| M3.2-K04 | K | Evaluación (Assess) | misma unidad |
| M3.2-K05 | K | Implementación | misma unidad |
| M3.2-K06 | K | Pentesting | misma unidad |
| M3.2-K07 | K | Controles Compensatorios | misma unidad |
| M3.2-K08 | K | Familias de Controles | misma unidad |
| M3.2-K09 | K | Pruebas de Efectividad | misma unidad |
| M3.2-K10 | K | POA&M | misma unidad |
| AMP-37 | AMP | Evaluación adversarial de agentes | misma unidad |
| HC-002 | HC | Apetito de riesgo convertido en arquitectura | misma unidad |
| HC-003 | HC | Riesgo residual y aceptación verificable | misma unidad |
| HC-004 | HC | Política como código gobernado | misma unidad |
| HC-005 | HC | Cumplimiento continuo orientado a resultados | misma unidad |
| HC-015 | HC | Gobierno y operación de Zero Trust | misma unidad |
| HC-018 | HC | Observabilidad y aseguramiento de controles | misma unidad |
| HC-028 | HC | Gestión de excepciones y compensaciones | misma unidad |
| HC-031 | HC | Seguridad del software y confianza en componentes | misma unidad |
| HC-032 | HC | Evaluación adversarial de sistemas autónomos | misma unidad |
| HC-034 | HC | Decisiones reversibles y riesgo de transición | misma unidad |
| HC-036 | HC | Portafolio de controles y capacidades | misma unidad |
| HC-038 | HC | Aseguramiento de la arquitectura Zero Trust | misma unidad |
| AMP-52 | AMP | Content safety y riesgos de contenido generado | misma unidad |
| M3.2-PA01 | PA | El control como producto: objetivo → configuración → evidencia | misma unidad |
| M3.2-PA02 | PA | Catálogo de controles de gobierno y gestión de agentes (AGC) | misma unidad |
| M3.2-PA03 | PA | Evaluación de calidad de agentes: datasets dorados, regresión y criterios de aceptación | misma unidad |

**Pregunta generadora:** Si la investigación automatizada de su tenant removiera mil mensajes legítimos por un veredicto erróneo, ¿cuánto tardaría en revertirlo?

---

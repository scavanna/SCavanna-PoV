# Pre-ensayo · AMP-37

> **GM-24 V7.1 · The Next CISO + Sub-plan PO-GAC** · 2026-11-14. Catálogo: 379 conceptos (245 K · 52 AMP · 40 HC · 42 PA), todos con pre-ensayo íntegro y mapeados a 17 marcos (NIST/ISACA/MITRE/OWASP/CIS/CSA). V7.1 = ChangeSet editorial CS-GM24-V7.1-001 (4 títulos generalizados; sin cambio de IDs, cantidad ni mapeo). Plano A (corpus académico). Referencias DD/K4x/R/eo:OP/COE: marco interno.

### 079. AMP-37 — Evaluación adversarial de agentes

**Unidad:** M3.2 Selección, Implementación y Evaluación de Controles · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 194 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** Antes de producción, un agente debe resistir pruebas adversariales —inyección de instrucciones, abuso de herramientas, fuga de datos, envenenamiento de contexto— con criterios de aceptación explícitos.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** Antes de producción, un agente debe resistir pruebas adversariales —inyección de instrucciones, abuso de herramientas, fuga de datos, envenenamiento de contexto— con criterios de aceptación explícitos. La tesis es que la evaluación adversarial es el 'pentest' del agente, que debe repetirse en cada versión y que sus resultados son parte del expediente de autorización.

**Tensión y límites.** La tensión es el costo y la cobertura: los ataques evolucionan y ninguna prueba es completa. Otra tensión es la no determinación: un agente puede resistir diez veces y caer en la undécima; los criterios deben expresarse como tasas. El ensayo debe proponer el conjunto mínimo de pruebas por nivel de autonomía.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: red teaming de IA, OWASP ASI/LLM Top 10, MITRE ATLAS, AI RMF MEASURE. Implementación: pruebas de inyección indirecta por correo sobre AG-01/AG-02, abuso de herramientas sobre AG-03, fuga sobre AG-14; herramientas de evaluación de Foundry y AI Red Teaming Agent/PyRIT como referencia; criterios de aceptación.

**Evidencia y evaluación.** Evidencia: informe de red teaming de un agente con casos, tasas y criterios. Se evalúa la cobertura de las amenazas relevantes al agente.

**Puentes.** Se apoya en HC-032 (evaluación adversarial integrada); se complementa con M3.2-PA03 (calidad); sostiene AGC-12; se relaciona con AMP-41/42.

**Recomendaciones de práctica y ejercitación.**
1. Diseñar el conjunto mínimo de pruebas adversariales por nivel de autonomía.
2. Ejecutar pruebas de inyección indirecta sobre AG-01 y AG-02 en el entorno de prueba.
3. Fijar criterios de aceptación como tasas y documentar el informe.

**Próximos pasos.**
- Incluir el informe en el expediente ATO.
- Repetir en cada versión (MDO-Q04).
- Actualizar con nuevas versiones de OWASP/ATLAS.

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
| AMP-38 | AMP | Pruebas de controles autónomos | misma unidad |
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

**Pregunta generadora:** Si un atacante escribiera un correo diseñado para que su agente de triaje lo clasifique como legítimo, ¿lo lograría hoy?

---

# Pre-ensayo · AMP-52

> **GM-24 V7.1 · The Next CISO + Sub-plan PO-GAC** · 2026-11-14. Catálogo: 379 conceptos (245 K · 52 AMP · 40 HC · 42 PA), todos con pre-ensayo íntegro y mapeados a 17 marcos (NIST/ISACA/MITRE/OWASP/CIS/CSA). V7.1 = ChangeSet editorial CS-GM24-V7.1-001 (4 títulos generalizados; sin cambio de IDs, cantidad ni mapeo). Plano A (corpus académico). Referencias DD/K4x/R/eo:OP/COE: marco interno.

### 094. AMP-52 — Content safety y riesgos de contenido generado

**Unidad:** G6.2 · M3.2 Liderazgo Ético y Medición de Efectividad · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V7 (V7-C07, cierra INC-03) · **Extensión:** 214 palabras · **Estado:** Idea central desarrollada (lote V7-01); ID curricular, no ESS.

**Definición / idea central.** Los sistemas generativos pueden producir contenido dañino, abusivo o engañoso aunque el objetivo sea legítimo; los guardrails de salida son un control de seguridad y de ética, con alcance declarado (qué riesgos de contenido quedan fuera del rol).

**Origen.** V7 (V7-C07, cierra INC-03)

**Tesis y sentido para el rol.** Los sistemas generativos pueden producir contenido dañino, abusivo, engañoso u ofensivo aunque su objetivo sea legítimo: un agente que redacta concientización o reportes puede generar texto inapropiado, inventar hechos o reproducir sesgos. Los guardrails de salida —filtros de contenido, validación de formato, revisión humana de lo publicable— son a la vez control de seguridad y control ético. La tesis es que el owner debe declarar qué riesgos de contenido trata (dañino, abusivo, desinformación) y cuáles quedan fuera del rol (CBRN, impacto ambiental), para no prometer coberturas que no gobierna.

**Tensión y límites.** La tensión es que los filtros de contenido afectan la utilidad (falsos positivos en lenguaje de seguridad: 'ataque', 'explotar') y que la desinformación generada (confabulación) no se filtra con listas. El ensayo debe combinar filtros, formato fijo y revisión humana según el destino de la salida.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: NIST AI 600-1 (contenido peligroso, abusivo, integridad de la información), OWASP LLM05/LLM09, IA responsable. Implementación: Azure AI Content Safety/Prompt Shields en Foundry, formato fijo de salida (SK-06), publicación solo humana para AG-12, etiquetado epistemológico (AMP-19); declaración de alcance de riesgos de contenido.

**Evidencia y evaluación.** Evidencia: configuración de guardrails verificada y declaración de alcance aprobada. Se evalúa la honestidad sobre lo que queda fuera.

**Puentes.** Se relaciona con AMP-25, AMP-26 y AMP-19; sostiene AGC-08 y M3.2-PA02. Nuevo en V7 (cierra INC-03).

**Recomendaciones de práctica y ejercitación.**
1. Configurar y probar guardrails de salida para AG-12 y AG-05.
2. Redactar la declaración de alcance de riesgos de contenido del rol.
3. Probar casos límite (lenguaje de seguridad legítimo vs. contenido dañino).

**Próximos pasos.**
- Registrar como AGC-08.
- Incluir en la política de agentes.
- Revisar con cambios de modelo.

**Relación con los conceptos de la(s) unidad(es) G6.2 · M3.2.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| G6.2-K01 | K | Liderazgo Ético | misma unidad |
| G6.2-K02 | K | Conducta Profesional | misma unidad |
| G6.2-K03 | K | Conflictos Interés | misma unidad |
| G6.2-K04 | K | Debida Diligencia | misma unidad |
| G6.2-K05 | K | Métricas Gobierno | misma unidad |
| G6.2-K06 | K | Efectividad Programa | misma unidad |
| G6.2-K07 | K | Mejora Continua | misma unidad |
| G6.2-K08 | K | Aseguramiento | misma unidad |
| G6.2-K09 | K | Balance Riesgo-Valor | misma unidad |
| G6.2-K10 | K | Rendición Cuentas | misma unidad |
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
| AMP-25 | AMP | Ética de autonomía | misma unidad |
| AMP-26 | AMP | Supervisión humana efectiva | misma unidad |
| AMP-37 | AMP | Evaluación adversarial de agentes | misma unidad |
| AMP-38 | AMP | Pruebas de controles autónomos | misma unidad |
| HC-002 | HC | Apetito de riesgo convertido en arquitectura | misma unidad |
| HC-003 | HC | Riesgo residual y aceptación verificable | misma unidad |
| HC-004 | HC | Política como código gobernado | misma unidad |
| HC-005 | HC | Cumplimiento continuo orientado a resultados | misma unidad |
| HC-006 | HC | Valor de seguridad y medición causal | misma unidad |
| HC-012 | HC | Confianza verificable en decisiones de IA | misma unidad |
| HC-015 | HC | Gobierno y operación de Zero Trust | misma unidad |
| HC-018 | HC | Observabilidad y aseguramiento de controles | misma unidad |
| HC-021 | HC | Recuperación como prueba de confianza | misma unidad |
| HC-026 | HC | Ética, cultura y controles internos | misma unidad |
| HC-027 | HC | Métricas que no engañan | misma unidad |
| HC-028 | HC | Gestión de excepciones y compensaciones | misma unidad |
| HC-031 | HC | Seguridad del software y confianza en componentes | misma unidad |
| HC-032 | HC | Evaluación adversarial de sistemas autónomos | misma unidad |
| HC-034 | HC | Decisiones reversibles y riesgo de transición | misma unidad |
| HC-036 | HC | Portafolio de controles y capacidades | misma unidad |
| HC-038 | HC | Aseguramiento de la arquitectura Zero Trust | misma unidad |
| G6.2-PA01 | PA | Métricas de efectividad del gobierno de la flota | misma unidad |
| M3.2-PA01 | PA | El control como producto: objetivo → configuración → evidencia | misma unidad |
| M3.2-PA02 | PA | Catálogo de controles de gobierno y gestión de agentes (AGC) | misma unidad |
| M3.2-PA03 | PA | Evaluación de calidad de agentes: datasets dorados, regresión y criterios de aceptación | misma unidad |

**Pregunta generadora:** ¿Qué contenido podría generar hoy un agente suyo que usted no querría ver publicado con el logo de la organización?

---

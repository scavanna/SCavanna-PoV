# Pre-ensayo · AMP-47

> **GM-24 V7.1 · The Next CISO + Sub-plan PO-GAC** · 2026-11-14. Catálogo: 379 conceptos (245 K · 52 AMP · 40 HC · 42 PA), todos con pre-ensayo íntegro y mapeados a 17 marcos (NIST/ISACA/MITRE/OWASP/CIS/CSA). V7.1 = ChangeSet editorial CS-GM24-V7.1-001 (4 títulos generalizados; sin cambio de IDs, cantidad ni mapeo). Plano A (corpus académico). Referencias DD/K4x/R/eo:OP/COE: marco interno.

### 089. AMP-47 — Recuperación de servicios de IA

**Unidad:** M6.1 Continuidad, DRP y Resiliencia Operativa · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 184 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** Recuperar un servicio de IA incluye modelos (versión y disponibilidad), índices y fuentes de conocimiento, instrucciones, conectores e identidades de agentes; no solo la infraestructura.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** Recuperar un servicio de IA incluye modelos (versión y disponibilidad), índices y fuentes de conocimiento, instrucciones, conectores e identidades de agentes; no solo la infraestructura. Un agente restaurado con instrucciones viejas o sin su identidad no está recuperado. La tesis es que el plan de recuperación de la flota debe inventariar esos componentes y probarse como cualquier plan de continuidad.

**Tensión y límites.** La tensión es que los componentes viven en plataformas distintas (Copilot Studio, Foundry, Entra, SharePoint) con mecanismos de respaldo distintos; nadie los recupera juntos por defecto. El ensayo debe proponer el inventario de componentes y el orden de recuperación.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: continuidad y recuperación (ISO 22301), RTO/RPO aplicados a servicios de IA. Implementación: plan de recuperación de la flota (soluciones de Power Platform versionadas, exportación de agentes, respaldo de knowledge sources, re-provisión de Agent ID), con RTO por agente crítico y prueba.

**Evidencia y evaluación.** Evidencia: plan de recuperación con inventario de componentes y una prueba de recuperación de un agente. Se evalúa que el agente recuperado sea funcional e idéntico.

**Puentes.** Se apoya en HC-021 (recuperación); se relaciona con AMP-48 y M6.1-PA01; sostiene la continuidad del control.

**Recomendaciones de práctica y ejercitación.**
1. Inventariar los componentes recuperables de cada agente (modelo, fuentes, instrucciones, conectores, identidad).
2. Definir RTO por agente crítico y el orden de recuperación.
3. Probar la recuperación completa de AG-03 en otro entorno.

**Próximos pasos.**
- Incluir en el BCDR del programa.
- Vincular con la operación degradada (M6.1-PA01).
- Repetir la prueba semestralmente.

**Relación con los conceptos de la(s) unidad(es) M6.1.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M6.1-K01 | K | Continuidad (BCP) | misma unidad |
| M6.1-K02 | K | Recuperación (DRP) | misma unidad |
| M6.1-K03 | K | Resiliencia Operativa | misma unidad |
| M6.1-K04 | K | ISO 22301 | misma unidad |
| M6.1-K05 | K | Pruebas Continuidad | misma unidad |
| M6.1-K06 | K | Backups Inmutables | misma unidad |
| M6.1-K07 | K | Alta Disponibilidad | misma unidad |
| M6.1-K08 | K | Sitio Alternativo | misma unidad |
| M6.1-K09 | K | Gestión Crisis (Negocio) | misma unidad |
| M6.1-K10 | K | Dependencias | misma unidad |
| AMP-48 | AMP | Dependencias de modelos | misma unidad |
| HC-007 | HC | Resiliencia gobernada por impacto | misma unidad |
| HC-008 | HC | Cadena de confianza en terceros | misma unidad |
| HC-021 | HC | Recuperación como prueba de confianza | misma unidad |
| HC-022 | HC | Gobierno de crisis multidisciplinario | misma unidad |
| HC-023 | HC | Riesgo de concentración tecnológica | misma unidad |
| HC-025 | HC | Competencias y resiliencia organizacional | misma unidad |
| HC-030 | HC | Seguridad industrial y continuidad de negocio | misma unidad |
| M6.1-PA01 | PA | Operación degradada del SOC sin agentes ni modelos | misma unidad |

**Pregunta generadora:** Si perdiera hoy el entorno donde viven sus agentes, ¿cuánto tardaría en tenerlos de vuelta con las mismas instrucciones, fuentes e identidades?

---

# Pre-ensayo · AMP-18

> **GM-24 V7.1 · The Next CISO + Sub-plan PO-GAC** · 2026-11-14. Catálogo: 379 conceptos (245 K · 52 AMP · 40 HC · 42 PA), todos con pre-ensayo íntegro y mapeados a 17 marcos (NIST/ISACA/MITRE/OWASP/CIS/CSA). V7.1 = ChangeSet editorial CS-GM24-V7.1-001 (4 títulos generalizados; sin cambio de IDs, cantidad ni mapeo). Plano A (corpus académico). Referencias DD/K4x/R/eo:OP/COE: marco interno.

### 060. AMP-18 — Límites de autonomía

**Unidad:** G4.2 Definición y Comunicación del Apetito de Riesgo · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 178 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** Los límites de autonomía —acciones permitidas, umbrales, aprobaciones requeridas y mecanismo de detención— traducen el apetito de riesgo en reglas operables para agentes.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** Los límites de autonomía —acciones permitidas, umbrales, aprobaciones requeridas y mecanismo de detención— traducen el apetito de riesgo en reglas operables para agentes. Sin ellos el apetito es una declaración; con ellos es configuración. La tesis es que los límites deben ser verificables en la plataforma (permisos de conectores, aprobaciones, cuotas, kill switch) y medibles con indicadores (KRIs) que avisen antes de la transgresión.

**Tensión y límites.** La tensión es la granularidad: la plataforma no siempre permite el límite exacto que el apetito pide; hay que compensar con aprobación humana o con alcance reducido. Otra tensión es la rigidez: límites demasiado estrictos hacen inútil al agente.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: control de acceso, cuotas, circuit breakers, HITL. Implementación: escala L0–L4 del sub-plan con árbol de decisión; permisos de conectores en Power Platform, Approvals para L2, límites de lote, kill switch en PPAC/Agent 365; KRIs en Sentinel.

**Evidencia y evaluación.** Evidencia: ficha de límites por agente con verificación en plataforma y KRI asociado. Se evalúa que cada límite declarado sea comprobable.

**Puentes.** Se apoya en HC-010 y AMP-17; sostiene AGC-04, AGC-09, AGC-10 y G4.2-PA01; se relaciona con AMP-44.

**Recomendaciones de práctica y ejercitación.**
1. Definir los límites de AG-02 y AG-03 (acciones, umbrales, aprobaciones, detención) y verificarlos en la plataforma.
2. Aplicar el árbol de decisión L0–L4 a las 31 tareas del modelo operativo.
3. Probar el kill switch de un agente y medir el tiempo.

**Próximos pasos.**
- Derivar los KRIs (G4.2-PA01).
- Documentar los límites en la ficha (G2.2-PA02).
- Revisar límites en cada revisión de desempeño.

**Relación con los conceptos de la(s) unidad(es) G4.2.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| G4.2-K01 | K | Apetito de Riesgo | misma unidad |
| G4.2-K02 | K | Tolerancia al Riesgo | misma unidad |
| G4.2-K03 | K | Documentación | misma unidad |
| G4.2-K04 | K | Comunicación | misma unidad |
| G4.2-K05 | K | Rol Ejecutivo | misma unidad |
| G4.2-K06 | K | Impacto en Estrategia | misma unidad |
| G4.2-K07 | K | Talleres de Definición | misma unidad |
| G4.2-K08 | K | Relación Apetito-Residual | misma unidad |
| G4.2-K09 | K | Métricas de Apetito | misma unidad |
| G4.2-K10 | K | Aceptación Formal | misma unidad |
| AMP-17 | AMP | Autoridad delegada | misma unidad |
| HC-002 | HC | Apetito de riesgo convertido en arquitectura | misma unidad |
| HC-003 | HC | Riesgo residual y aceptación verificable | misma unidad |
| HC-007 | HC | Resiliencia gobernada por impacto | misma unidad |
| HC-010 | HC | Autonomía delegada y límites de acción | misma unidad |
| HC-027 | HC | Métricas que no engañan | misma unidad |
| HC-040 | HC | Homeostasis organizacional de seguridad | misma unidad |
| G4.2-PA01 | PA | KRIs de la flota de agentes y umbrales de intervención | misma unidad |

**Pregunta generadora:** Para el agente más autónomo de su flota, ¿qué límite concreto de plataforma le impediría hoy hacer algo que su ficha prohíbe?

---

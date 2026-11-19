# Pre-ensayo · AMP-10

> **GM-24 V7.1 · The Next CISO + Sub-plan PO-GAC** · 2026-11-14. Catálogo: 379 conceptos (245 K · 52 AMP · 40 HC · 42 PA), todos con pre-ensayo íntegro y mapeados a 17 marcos (NIST/ISACA/MITRE/OWASP/CIS/CSA). V7.1 = ChangeSet editorial CS-GM24-V7.1-001 (4 títulos generalizados; sin cambio de IDs, cantidad ni mapeo). Plano A (corpus académico). Referencias DD/K4x/R/eo:OP/COE: marco interno.

### 052. AMP-10 — Gobierno de excepciones automatizadas

**Unidad:** G2.2 Ciclo de Vida de Políticas, Estándares y Procedimientos · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 186 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** Cuando las excepciones se conceden y vencen automáticamente —entradas de permiso, overrides, reglas de bypass— la automatización puede normalizar el desvío: lo excepcional se vuelve permanente porque nadie vuelve a mirar.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** Cuando las excepciones se conceden y vencen automáticamente —entradas de permiso, overrides, reglas de bypass— la automatización puede normalizar el desvío: lo excepcional se vuelve permanente porque nadie vuelve a mirar. La tesis es que toda excepción automatizada necesita dueño, caducidad y evidencia de la razón, y que el informe de excepciones vigentes es un control de gobierno, no un detalle administrativo.

**Tensión y límites.** La tensión es operativa: las excepciones resuelven problemas reales bajo presión y su revisión no tiene urgencia. Otra tensión es la escala: cientos de entradas no se revisan a mano; la caducidad por defecto y el agente auditor (AG-11) son la respuesta.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: gestión de excepciones, caducidad por defecto, revisión periódica. Implementación: Tenant Allow/Block List con vencimiento obligatorio, informe de overrides mensual (MDO-M02), registro de excepciones en Dataverse con dueño y justificación, KPI-07 (overrides sin justificación = 0).

**Evidencia y evaluación.** Evidencia: registro de excepciones del control con dueño, caducidad y justificación; informe mensual con excepciones vencidas y depuradas. Se evalúa que ninguna excepción carezca de fecha ni dueño.

**Puentes.** Se apoya en HC-028 (excepciones y compensaciones); sostiene G2.2-PA03 y el agente AG-11; se relaciona con AMP-09.

**Recomendaciones de práctica y ejercitación.**
1. Inventariar las excepciones vigentes del control y clasificarlas por antigüedad y justificación.
2. Definir la regla de caducidad por defecto y el flujo de renovación.
3. Diseñar el informe mensual de excepciones (MDO-M02) y su KPI.

**Próximos pasos.**
- Asignar AG-11 como auditor de overrides.
- Conectar con el registro de riesgos (excepciones como riesgo aceptado).
- Revisar la regla en la revisión trimestral de políticas (MDO-Q01).

**Relación con los conceptos de la(s) unidad(es) G2.2.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| G2.2-K01 | K | Jerarquía Documental | misma unidad |
| G2.2-K02 | K | Desarrollo de Políticas | misma unidad |
| G2.2-K03 | K | Estándares de Seguridad | misma unidad |
| G2.2-K04 | K | Procedimientos | misma unidad |
| G2.2-K05 | K | Comunicación | misma unidad |
| G2.2-K06 | K | Aplicación (Enforcement) | misma unidad |
| G2.2-K07 | K | Mantenimiento | misma unidad |
| G2.2-K08 | K | Control de Versiones | misma unidad |
| G2.2-K09 | K | Excepciones | misma unidad |
| G2.2-K10 | K | Rol de Auditoría | misma unidad |
| AMP-09 | AMP | Policy-as-code | misma unidad |
| HC-004 | HC | Política como código gobernado | misma unidad |
| HC-013 | HC | Deuda de seguridad como riesgo de transformación | misma unidad |
| HC-015 | HC | Gobierno y operación de Zero Trust | misma unidad |
| HC-028 | HC | Gestión de excepciones y compensaciones | misma unidad |
| HC-035 | HC | Aprendizaje desde incidentes hasta políticas | misma unidad |
| HC-038 | HC | Aseguramiento de la arquitectura Zero Trust | misma unidad |
| G2.2-PA01 | PA | Política de uso y gobierno de agentes | misma unidad |
| G2.2-PA02 | PA | Estándar de ficha de agente (charter) y runbooks de agentes | misma unidad |
| G2.2-PA03 | PA | Baseline, excepciones y overrides de un control técnico | misma unidad |

**Pregunta generadora:** ¿Cuántas excepciones vigentes en su control de correo tienen más de un año, y cuántas recuerda alguien por qué existen?

---

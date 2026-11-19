# Pre-ensayo · AMP-09

> **GM-24 V7.1 · The Next CISO + Sub-plan PO-GAC** · 2026-11-14. Catálogo: 379 conceptos (245 K · 52 AMP · 40 HC · 42 PA), todos con pre-ensayo íntegro y mapeados a 17 marcos (NIST/ISACA/MITRE/OWASP/CIS/CSA). V7.1 = ChangeSet editorial CS-GM24-V7.1-001 (4 títulos generalizados; sin cambio de IDs, cantidad ni mapeo). Plano A (corpus académico). Referencias DD/K4x/R/eo:OP/COE: marco interno.

### 051. AMP-09 — Policy-as-code

**Unidad:** G2.2 Ciclo de Vida de Políticas, Estándares y Procedimientos · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 194 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** Expresar políticas como código —configuraciones declarativas, baselines, reglas evaluables— vuelve verificable su aplicación: se puede comprobar en cualquier momento si el estado real coincide con el declarado.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** Expresar políticas como código —configuraciones declarativas, baselines, reglas evaluables— vuelve verificable su aplicación: se puede comprobar en cualquier momento si el estado real coincide con el declarado. Pero policy-as-code exige lo que todo código exige: control de versiones, gestión de excepciones y revisión humana para cambios de alto impacto. La tesis es que la política escrita en prosa y la política aplicada en configuración deben ser el mismo objeto gobernado.

**Tensión y límites.** La tensión es que la configuración vive en consolas y la política en documentos; quien cambia una no cambia la otra. Otra tensión es la ilusión de que todo se puede codificar: la autoridad, las prohibiciones y las excepciones siguen necesitando texto y firma.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: policy-as-code, configuration management, GitOps. Implementación: presets Standard/Strict de Defender for Office 365 como baseline versionado, Configuration Analyzer como verificación, políticas de Power Platform (DLP, conectores) como aplicación de la política de agentes; ChangeSets para cambios.

**Evidencia y evaluación.** Evidencia: baseline versionado del control con historial de cambios y procedimiento de revisión para cambios de alto impacto. Se evalúa la trazabilidad entre texto normativo y configuración.

**Puentes.** Se apoya en HC-004 (políticas y configuración) y G2.2-K03; sostiene G2.2-PA03 (baseline, excepciones) y G3.2-PA01 (deriva).

**Recomendaciones de práctica y ejercitación.**
1. Versionar el baseline de Defender for Office 365 (exportar configuración, Git) y definir la revisión por tipo de cambio.
2. Mapear tres reglas de la política de agentes a políticas de Power Platform.
3. Ejecutar Configuration Analyzer y conciliar con el baseline versionado.

**Próximos pasos.**
- Integrar con el control continuo de deriva (G3.2-PA01).
- Conectar con el ALM de agentes (M6.2-PA02).
- Revisar la política en prosa cuando cambie el baseline.

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
| AMP-10 | AMP | Gobierno de excepciones automatizadas | misma unidad |
| HC-004 | HC | Política como código gobernado | misma unidad |
| HC-013 | HC | Deuda de seguridad como riesgo de transformación | misma unidad |
| HC-015 | HC | Gobierno y operación de Zero Trust | misma unidad |
| HC-028 | HC | Gestión de excepciones y compensaciones | misma unidad |
| HC-035 | HC | Aprendizaje desde incidentes hasta políticas | misma unidad |
| HC-038 | HC | Aseguramiento de la arquitectura Zero Trust | misma unidad |
| G2.2-PA01 | PA | Política de uso y gobierno de agentes | misma unidad |
| G2.2-PA02 | PA | Estándar de ficha de agente (charter) y runbooks de agentes | misma unidad |
| G2.2-PA03 | PA | Baseline, excepciones y overrides de un control técnico | misma unidad |

**Pregunta generadora:** Si alguien cambiara hoy una política de correo en la consola, ¿qué documento quedaría desactualizado y quién lo notaría?

---

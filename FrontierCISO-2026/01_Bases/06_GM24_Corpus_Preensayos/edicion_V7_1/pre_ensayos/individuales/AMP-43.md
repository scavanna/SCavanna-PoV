# Pre-ensayo · AMP-43

> **GM-24 V7.1 · The Next CISO + Sub-plan PO-GAC** · 2026-11-14. Catálogo: 379 conceptos (245 K · 52 AMP · 40 HC · 42 PA), todos con pre-ensayo íntegro y mapeados a 17 marcos (NIST/ISACA/MITRE/OWASP/CIS/CSA). V7.1 = ChangeSet editorial CS-GM24-V7.1-001 (4 títulos generalizados; sin cambio de IDs, cantidad ni mapeo). Plano A (corpus académico). Referencias DD/K4x/R/eo:OP/COE: marco interno.

### 085. AMP-43 — Tabletop de incidentes con agentes

**Unidad:** M5.1 Planificación y Preparación (Incl. BIA) · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 182 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** Ejercitar incidentes donde un agente es víctima (manipulado, comprometido) o vector (causa o amplifica el daño) revela vacíos de autoridad (quién puede detenerlo), evidencia (qué trazas existen) y contención (cómo se aísla) antes de que ocurran.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** Ejercitar incidentes donde un agente es víctima (manipulado, comprometido) o vector (causa o amplifica el daño) revela vacíos de autoridad (quién puede detenerlo), evidencia (qué trazas existen) y contención (cómo se aísla) antes de que ocurran. La tesis es que el tabletop con agentes es el ensayo mínimo antes de otorgar autonomía L2 o superior, y que sus hallazgos alimentan directamente fichas, límites y playbooks.

**Tensión y límites.** La tensión es que los tabletops clásicos no contemplan actores no humanos y los equipos no saben cómo 'jugar' a un agente. Otra tensión es la ficción: el ejercicio debe usar los agentes y permisos reales para ser útil. El ensayo debe proponer escenarios concretos.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: ejercicios de mesa (SP 800-84), gestión de crisis. Implementación: tabletop con dos escenarios (AG-02 manipulado remedia correo legítimo; AG-03 comprometido crea permisos) usando fichas, permisos y kill switch reales; registro de vacíos y acciones.

**Evidencia y evaluación.** Evidencia: informe del tabletop con vacíos de autoridad, evidencia y contención y acciones correctivas. Se evalúa el realismo y el cierre de acciones.

**Puentes.** Extiende M5.1-K06 (ejercicios tabletop); se relaciona con AMP-44, AMP-28 y M5.1-PA01; sostiene AGC-17.

**Recomendaciones de práctica y ejercitación.**
1. Diseñar dos escenarios de tabletop con agente víctima y agente vector.
2. Ejecutarlos con permisos y kill switch reales en el entorno de prueba.
3. Registrar vacíos y convertirlos en cambios de fichas y playbooks.

**Próximos pasos.**
- Programar el tabletop semestral (MDO-A07).
- Alimentar el playbook 'agente comprometido'.
- Reportar hallazgos al comité.

**Relación con los conceptos de la(s) unidad(es) M5.1.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M5.1-K01 | K | IRP (Plan Respuesta) | misma unidad |
| M5.1-K02 | K | BIA (Impacto Negocio) | misma unidad |
| M5.1-K03 | K | CSIRT | misma unidad |
| M5.1-K04 | K | Preparación (Readiness) | misma unidad |
| M5.1-K05 | K | Clasificación Incidentes | misma unidad |
| M5.1-K06 | K | Ejercicios Tabletop | misma unidad |
| M5.1-K07 | K | Playbooks | misma unidad |
| M5.1-K08 | K | Cadena de Mando | misma unidad |
| M5.1-K09 | K | RTO/RPO | misma unidad |
| M5.1-K10 | K | Alineación BCDR | misma unidad |
| AMP-44 | AMP | Kill switch y escalamiento | misma unidad |
| HC-007 | HC | Resiliencia gobernada por impacto | misma unidad |
| HC-020 | HC | Respuesta y comunicación bajo incertidumbre | misma unidad |
| HC-022 | HC | Gobierno de crisis multidisciplinario | misma unidad |
| HC-025 | HC | Competencias y resiliencia organizacional | misma unidad |
| HC-030 | HC | Seguridad industrial y continuidad de negocio | misma unidad |
| HC-037 | HC | Alineación entre competencias y decisiones | misma unidad |
| HC-039 | HC | Riesgo cibernético como narrativa empresarial | misma unidad |
| M5.1-PA01 | PA | Playbooks de incidentes de correo con roles humano/agente | misma unidad |

**Pregunta generadora:** Si en el próximo tabletop el agente fuera el atacante, ¿quién en su equipo sabría cómo detenerlo y en cuánto tiempo?

---

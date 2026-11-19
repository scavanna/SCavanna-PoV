# Pre-ensayo · AMP-48

> **GM-24 V7.1 · The Next CISO + Sub-plan PO-GAC** · 2026-11-14. Catálogo: 379 conceptos (245 K · 52 AMP · 40 HC · 42 PA), todos con pre-ensayo íntegro y mapeados a 17 marcos (NIST/ISACA/MITRE/OWASP/CIS/CSA). V7.1 = ChangeSet editorial CS-GM24-V7.1-001 (4 títulos generalizados; sin cambio de IDs, cantidad ni mapeo). Plano A (corpus académico). Referencias DD/K4x/R/eo:OP/COE: marco interno.

### 090. AMP-48 — Dependencias de modelos

**Unidad:** M6.1 Continuidad, DRP y Resiliencia Operativa · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 182 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** Depender de un modelo o proveedor de IA crea riesgo de concentración y de cambio no controlado: el proveedor puede retirar el modelo, cambiar su comportamiento, su precio o su región.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** Depender de un modelo o proveedor de IA crea riesgo de concentración y de cambio no controlado: el proveedor puede retirar el modelo, cambiar su comportamiento, su precio o su región. La tesis es que el owner debe mapear sus dependencias de modelos y proveedores por agente y prever alternativas (otro modelo, otra ruta, modo manual), con disparadores que indiquen cuándo activarlas.

**Tensión y límites.** La tensión es que la alternativa cuesta (evaluar dos modelos, mantener dos rutas) y rara vez se usa. Otra tensión es la ilusión de portabilidad: cambiar de modelo cambia el comportamiento y exige reevaluación. El ensayo debe proponer alternativas proporcionales a la criticidad.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: riesgo de concentración, gestión de proveedores, portabilidad. Implementación: mapa de dependencias de modelos de la flota (catálogo de Foundry, modelos de Copilot Studio/Security Copilot), alternativa por agente crítico, disparadores (deprecación, cambio de precio, deriva) y procedimiento de reevaluación (M3.2-PA03).

**Evidencia y evaluación.** Evidencia: mapa de dependencias con alternativas y disparadores. Se evalúa la proporcionalidad y la existencia de una prueba de cambio de modelo.

**Puentes.** Se apoya en HC-023 (concentración); se relaciona con AMP-15, AMP-20 y M6.2-PA03; sostiene M6.1-PA01.

**Recomendaciones de práctica y ejercitación.**
1. Mapear las dependencias de modelos y proveedores de la flota.
2. Definir alternativa y disparadores para los agentes críticos.
3. Probar el cambio de modelo de un agente y reevaluarlo con el dataset dorado.

**Próximos pasos.**
- Registrar la concentración como riesgo sistémico (AMP-15).
- Incluir en el plan de recuperación (AMP-47).
- Revisar ante anuncios del proveedor (AG-09).

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
| AMP-47 | AMP | Recuperación de servicios de IA | misma unidad |
| HC-007 | HC | Resiliencia gobernada por impacto | misma unidad |
| HC-008 | HC | Cadena de confianza en terceros | misma unidad |
| HC-021 | HC | Recuperación como prueba de confianza | misma unidad |
| HC-022 | HC | Gobierno de crisis multidisciplinario | misma unidad |
| HC-023 | HC | Riesgo de concentración tecnológica | misma unidad |
| HC-025 | HC | Competencias y resiliencia organizacional | misma unidad |
| HC-030 | HC | Seguridad industrial y continuidad de negocio | misma unidad |
| M6.1-PA01 | PA | Operación degradada del SOC sin agentes ni modelos | misma unidad |

**Pregunta generadora:** Si el modelo que usan sus agentes fuera retirado con 90 días de aviso, ¿qué haría el día 1?

---

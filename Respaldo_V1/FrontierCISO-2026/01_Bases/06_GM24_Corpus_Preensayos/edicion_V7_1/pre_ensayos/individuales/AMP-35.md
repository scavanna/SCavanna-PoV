# Pre-ensayo · AMP-35

> **GM-24 V7.1 · The Next CISO + Sub-plan PO-GAC** · 2026-11-14. Catálogo: 379 conceptos (245 K · 52 AMP · 40 HC · 42 PA), todos con pre-ensayo íntegro y mapeados a 17 marcos (NIST/ISACA/MITRE/OWASP/CIS/CSA). V7.1 = ChangeSet editorial CS-GM24-V7.1-001 (4 títulos generalizados; sin cambio de IDs, cantidad ni mapeo). Plano A (corpus académico). Referencias DD/K4x/R/eo:OP/COE: marco interno.

### 077. AMP-35 — Arquitectura de sistemas agénticos

**Unidad:** M3.1 Arquitectura de Seguridad, Ingeniería y Diseño (Incl. Zero Trust) · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 192 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** Diseñar sistemas agénticos seguros implica separar planificación (el modelo decide qué hacer), herramientas (lo que puede ejecutar), datos (lo que puede leer) y permisos (lo que la identidad autoriza), con puntos de control y observabilidad desde el diseño.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** Diseñar sistemas agénticos seguros implica separar planificación (el modelo decide qué hacer), herramientas (lo que puede ejecutar), datos (lo que puede leer) y permisos (lo que la identidad autoriza), con puntos de control y observabilidad desde el diseño. La tesis es que esa separación —y no la confianza en el modelo— es lo que hace gobernable a un agente: cada capa se puede acotar, probar y observar por separado.

**Tensión y límites.** La tensión es que las plataformas low-code mezclan las capas para facilitar la construcción; separarlas exige disciplina del constructor. Otra tensión es el rendimiento: más puntos de control, más latencia. El ensayo debe proponer la separación mínima por nivel de autonomía.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: arquitectura de referencia de agentes, patrones (único, multiagente, orquestador), MAESTRO. Implementación: decisión de patrón para la flota (agentes especializados con orquestación explícita vía analista), separación de capas en Copilot Studio (instrucciones / tools / knowledge / Agent ID), puntos de control (Approvals) y observabilidad (Sentinel).

**Evidencia y evaluación.** Evidencia: decisión de arquitectura documentada con las cuatro capas por agente. Se evalúa la claridad de los límites entre capas.

**Puentes.** Extiende M6.2-K04 (seguridad IA); se relaciona con AMP-28, AMP-36 y M3.1-PA01; sostiene AGC-06 y AGC-08.

**Recomendaciones de práctica y ejercitación.**
1. Documentar las cuatro capas para AG-02 y verificar sus límites en la plataforma.
2. Elegir y justificar el patrón de orquestación de la flota.
3. Ubicar los puntos de control y observabilidad en el diseño.

**Próximos pasos.**
- Alimentar la arquitectura de referencia (M3.1-PA01).
- Probar la separación con pruebas adversariales (AMP-37).
- Revisar al cambiar de ruta de construcción.

**Relación con los conceptos de la(s) unidad(es) M3.1.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M3.1-K01 | K | Arquitectura de Seguridad | misma unidad |
| M3.1-K02 | K | Ingeniería de Seguridad | misma unidad |
| M3.1-K03 | K | Zero Trust (Arquitectura) | misma unidad |
| M3.1-K04 | K | Diseño Seguro (SbD) | misma unidad |
| M3.1-K05 | K | TOGAF y Seguridad | misma unidad |
| M3.1-K06 | K | ZTNA (Acceso) | misma unidad |
| M3.1-K07 | K | Microsegmentación | misma unidad |
| M3.1-K08 | K | Defensa en Profundidad | misma unidad |
| M3.1-K09 | K | Mínimo Privilegio (Arquitectura) | misma unidad |
| M3.1-K10 | K | Resiliencia (Diseño) | misma unidad |
| AMP-36 | AMP | Límites de herramientas y permisos | misma unidad |
| HC-002 | HC | Apetito de riesgo convertido en arquitectura | misma unidad |
| HC-010 | HC | Autonomía delegada y límites de acción | misma unidad |
| HC-013 | HC | Deuda de seguridad como riesgo de transformación | misma unidad |
| HC-014 | HC | Arquitectura de riesgo empresarial | misma unidad |
| HC-015 | HC | Gobierno y operación de Zero Trust | misma unidad |
| HC-023 | HC | Riesgo de concentración tecnológica | misma unidad |
| HC-030 | HC | Seguridad industrial y continuidad de negocio | misma unidad |
| HC-034 | HC | Decisiones reversibles y riesgo de transición | misma unidad |
| HC-038 | HC | Aseguramiento de la arquitectura Zero Trust | misma unidad |
| HC-040 | HC | Homeostasis organizacional de seguridad | misma unidad |
| M3.1-K11 | K | Arquitectura empresarial y arquitectura de seguridad de la información | misma unidad |
| M3.1-K12 | K | Seguridad física, ambiental y mantenimiento como dependencias del control | misma unidad |
| M3.1-PA01 | PA | Arquitectura de referencia del SOC agéntico con control plane | misma unidad |
| M3.1-PA02 | PA | Arquitectura de protección del dominio Zero Trust (instancias: correo y colaboración · detección y respuesta unificada · endpoints · identidades · datos) | misma unidad |

**Pregunta generadora:** En su agente de remediación, ¿qué impide que el modelo decida invocar una herramienta que su ficha no autoriza?

---

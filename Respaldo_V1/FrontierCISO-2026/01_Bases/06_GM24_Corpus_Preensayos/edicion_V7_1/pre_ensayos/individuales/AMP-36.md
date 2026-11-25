# Pre-ensayo · AMP-36

> **GM-24 V7.1 · The Next CISO + Sub-plan PO-GAC** · 2026-11-14. Catálogo: 379 conceptos (245 K · 52 AMP · 40 HC · 42 PA), todos con pre-ensayo íntegro y mapeados a 17 marcos (NIST/ISACA/MITRE/OWASP/CIS/CSA). V7.1 = ChangeSet editorial CS-GM24-V7.1-001 (4 títulos generalizados; sin cambio de IDs, cantidad ni mapeo). Plano A (corpus académico). Referencias DD/K4x/R/eo:OP/COE: marco interno.

### 078. AMP-36 — Límites de herramientas y permisos

**Unidad:** M3.1 Arquitectura de Seguridad, Ingeniería y Diseño (Incl. Zero Trust) · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 203 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** Las herramientas y conectores definen lo que un agente puede hacer en el mundo: acotar alcances (allowlist por agente), aprobar acciones de alto impacto y registrar cada invocación son los tres controles que convierten una capacidad técnica en una capacidad gobernada.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** Las herramientas y conectores definen lo que un agente puede hacer en el mundo: acotar alcances (allowlist por agente), aprobar acciones de alto impacto y registrar cada invocación son los tres controles que convierten una capacidad técnica en una capacidad gobernada. La tesis es que la lista de herramientas de un agente es parte de su ficha y de su autorización, y que agregar una herramienta es un cambio de riesgo.

**Tensión y límites.** La tensión es la utilidad: cada herramienta nueva hace al agente más útil y más peligroso. Otra tensión es la opacidad de los conectores: un conector 'Graph' puede permitir mucho más de lo que el nombre sugiere. El ensayo debe exigir permisos declarados por operación.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: least privilege aplicado a capacidades, allowlists, auditoría de invocaciones, OWASP ASI02. Implementación: allowlist de conectores por agente en Power Platform (políticas de datos), permisos de API por tool (anexos de agentes), Approvals para acciones de escritura, registro de invocaciones en Sentinel.

**Evidencia y evaluación.** Evidencia: allowlist y permisos por tool para tres agentes, verificados; registro de invocaciones de una semana. Se evalúa que ningún agente tenga herramientas fuera de su ficha.

**Puentes.** Extiende M3.1-K09 (mínimo privilegio en arquitectura); se relaciona con AMP-34, AMP-50 y M2.2-PA01; sostiene AGC-06 y AGC-11.

**Recomendaciones de práctica y ejercitación.**
1. Construir la allowlist de tools por agente desde los anexos y aplicarla en Power Platform.
2. Declarar permisos por operación para cada tool de escritura.
3. Revisar una semana de invocaciones y detectar anomalías.

**Próximos pasos.**
- Registrar como AGC-06.
- Incorporar al pipeline de cambios (agregar tool = ChangeSet).
- Vincular con la matriz amenaza→agente (M4.2-PA02).

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
| AMP-35 | AMP | Arquitectura de sistemas agénticos | misma unidad |
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

**Pregunta generadora:** ¿Qué podría hacer hoy el conector más amplio de su flota si el agente que lo usa fuera manipulado?

---

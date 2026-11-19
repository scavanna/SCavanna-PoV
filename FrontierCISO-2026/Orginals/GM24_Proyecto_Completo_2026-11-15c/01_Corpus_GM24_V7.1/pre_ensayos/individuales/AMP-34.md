# Pre-ensayo · AMP-34

> **GM-24 V7.1 · The Next CISO + Sub-plan PO-GAC** · 2026-11-14. Catálogo: 379 conceptos (245 K · 52 AMP · 40 HC · 42 PA), todos con pre-ensayo íntegro y mapeados a 17 marcos (NIST/ISACA/MITRE/OWASP/CIS/CSA). V7.1 = ChangeSet editorial CS-GM24-V7.1-001 (4 títulos generalizados; sin cambio de IDs, cantidad ni mapeo). Plano A (corpus académico). Referencias DD/K4x/R/eo:OP/COE: marco interno.

### 076. AMP-34 — Identidad y autorización de agentes

**Unidad:** M2.2 Gestión de Identidad y Acceso (IAM) y Principios de Confianza Cero · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Referencias por ID (V7-C09):** OWASP NHI Top 10 (2025); ASI03; CSA AICM IAM-19 · **Extensión:** 177 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** Cada agente necesita identidad propia, permisos mínimos, acceso condicional y ciclo de vida: es la base de un agente protegido.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** Cada agente necesita identidad propia, permisos mínimos, acceso condicional y ciclo de vida: es la base de un agente protegido. Identidad propia permite atribuir y revocar; permisos mínimos acotan el daño; acceso condicional aplica contexto (ubicación, riesgo); ciclo de vida garantiza que el agente muera cuando deja de ser útil. La tesis es que ninguna de las cuatro piezas es opcional para agentes L2 o superiores.

**Tensión y límites.** La tensión es la comodidad de reutilizar la identidad del constructor y la granularidad limitada de permisos de conectores. El ensayo debe mostrar cómo compensar (límites de herramientas, aprobación) cuando el permiso exacto no existe.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: identidad de carga de trabajo, least privilege, acceso basado en contexto, SP 800-207. Implementación: Entra Agent ID (blueprint, agent identity, agent user), API permissions por tool, Conditional Access para agentes, caducidad y recertificación en Entra ID Governance.

**Evidencia y evaluación.** Evidencia: ficha de identidad de un agente con las cuatro piezas verificadas en el tenant. Se evalúa la coherencia con la ficha de agente.

**Puentes.** Extiende M2.2-K03 (autorización); se relaciona con AMP-33, AMP-36 y M2.2-PA01; sostiene AGC-05, AGC-06.

**Recomendaciones de práctica y ejercitación.**
1. Provisionar la identidad de AG-03 con las cuatro piezas y documentarla.
2. Aplicar una política de acceso condicional a una identidad de agente y probarla.
3. Definir la caducidad y el flujo de recertificación.

**Próximos pasos.**
- Replicar para los 15 agentes.
- Registrar como AGC-05/06.
- Revisar permisos en cada cambio de tool.

**Relación con los conceptos de la(s) unidad(es) M2.2.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M2.2-K01 | K | Estrategias IAM | misma unidad |
| M2.2-K02 | K | Autenticación | misma unidad |
| M2.2-K03 | K | Autorización | misma unidad |
| M2.2-K04 | K | PAM (Privilegiados) | misma unidad |
| M2.2-K05 | K | Zero Trust | misma unidad |
| M2.2-K06 | K | ZTNA | misma unidad |
| M2.2-K07 | K | Ciclo Vida Identidad | misma unidad |
| M2.2-K08 | K | Auditoría IAM | misma unidad |
| M2.2-K09 | K | Federación | misma unidad |
| M2.2-K10 | K | Contexto de Acceso | misma unidad |
| AMP-33 | AMP | Identidades no humanas | misma unidad |
| HC-009 | HC | Gobierno de identidades no humanas | misma unidad |
| HC-010 | HC | Autonomía delegada y límites de acción | misma unidad |
| HC-015 | HC | Gobierno y operación de Zero Trust | misma unidad |
| HC-032 | HC | Evaluación adversarial de sistemas autónomos | misma unidad |
| HC-038 | HC | Aseguramiento de la arquitectura Zero Trust | misma unidad |
| M2.2-PA01 | PA | Permisos de humanos y agentes en el control: RBAC unificado, roles y conectores | misma unidad |

**Pregunta generadora:** Si revocara ahora la identidad de su agente más activo, ¿qué dejaría de funcionar y cuánto tardaría en saberlo?

---

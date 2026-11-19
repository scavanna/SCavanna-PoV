# Pre-ensayo · AMP-33

> **GM-24 V7.1 · The Next CISO + Sub-plan PO-GAC** · 2026-11-14. Catálogo: 379 conceptos (245 K · 52 AMP · 40 HC · 42 PA), todos con pre-ensayo íntegro y mapeados a 17 marcos (NIST/ISACA/MITRE/OWASP/CIS/CSA). V7.1 = ChangeSet editorial CS-GM24-V7.1-001 (4 títulos generalizados; sin cambio de IDs, cantidad ni mapeo). Plano A (corpus académico). Referencias DD/K4x/R/eo:OP/COE: marco interno.

### 075. AMP-33 — Identidades no humanas

**Unidad:** M2.2 Gestión de Identidad y Acceso (IAM) y Principios de Confianza Cero · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Referencias por ID (V7-C09):** OWASP Top 10 for Non-Human Identities (2025); ASI03 (2026 v2.01) · **Extensión:** 189 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** Las identidades no humanas —cuentas de servicio, principales, claves, tokens y ahora agentes— ya superan en número a las humanas y son la superficie menos vigilada: sin inventario, dueño, credenciales gestionadas y caducidad, cada una es una puerta sin cerradura.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** Las identidades no humanas —cuentas de servicio, principales, claves, tokens y ahora agentes— ya superan en número a las humanas y son la superficie menos vigilada: sin inventario, dueño, credenciales gestionadas y caducidad, cada una es una puerta sin cerradura. La tesis es que las identidades de agentes deben entrar al mismo régimen que las demás NHI (inventario, dueño, rotación, caducidad, revisión) y que la plataforma debe crearlas automáticamente para que ninguna nazca huérfana.

**Tensión y límites.** La tensión es la proliferación: crear un agente crea una identidad; sin automatización el inventario queda atrás desde el día uno. Otra tensión es la herencia: agentes antiguos usan app registrations con permisos amplios.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: gestión de identidades de carga de trabajo, OWASP NHI Top 10, rotación de credenciales. Implementación: inventario de NHI del control con Entra Agent ID (creación automática en Copilot Studio), sponsors, caducidad y migración de app registrations previas; regla de agentes sin dueño en Agent 365.

**Evidencia y evaluación.** Evidencia: inventario de identidades no humanas del control con dueño y caducidad; cero identidades huérfanas. Se evalúa la cobertura.

**Puentes.** Se apoya en HC-009; se relaciona con AMP-34 y M2.1-PA01; sostiene AGC-05, AGC-18 y AGC-19.

**Recomendaciones de práctica y ejercitación.**
1. Inventariar las identidades no humanas del control (app registrations, principales, agentes).
2. Asignar dueño y caducidad; detectar huérfanas.
3. Migrar un agente de app registration a Entra Agent ID.

**Próximos pasos.**
- Configurar la regla de agentes sin dueño (Agent 365).
- Programar la recertificación (AGC-18).
- Conectar con la matriz de permisos (M2.2-PA01).

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
| AMP-34 | AMP | Identidad y autorización de agentes | misma unidad |
| HC-009 | HC | Gobierno de identidades no humanas | misma unidad |
| HC-010 | HC | Autonomía delegada y límites de acción | misma unidad |
| HC-015 | HC | Gobierno y operación de Zero Trust | misma unidad |
| HC-032 | HC | Evaluación adversarial de sistemas autónomos | misma unidad |
| HC-038 | HC | Aseguramiento de la arquitectura Zero Trust | misma unidad |
| M2.2-PA01 | PA | Permisos de humanos y agentes en el control: RBAC unificado, roles y conectores | misma unidad |

**Pregunta generadora:** ¿Cuántas identidades no humanas con acceso a su correo corporativo existen hoy, y cuántas tienen un dueño que lo sepa?

---

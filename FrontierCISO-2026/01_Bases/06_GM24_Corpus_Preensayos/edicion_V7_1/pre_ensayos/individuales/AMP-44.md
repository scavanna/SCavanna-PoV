# Pre-ensayo · AMP-44

> **GM-24 V7.1 · The Next CISO + Sub-plan PO-GAC** · 2026-11-14. Catálogo: 379 conceptos (245 K · 52 AMP · 40 HC · 42 PA), todos con pre-ensayo íntegro y mapeados a 17 marcos (NIST/ISACA/MITRE/OWASP/CIS/CSA). V7.1 = ChangeSet editorial CS-GM24-V7.1-001 (4 títulos generalizados; sin cambio de IDs, cantidad ni mapeo). Plano A (corpus académico). Referencias DD/K4x/R/eo:OP/COE: marco interno.

### 086. AMP-44 — Kill switch y escalamiento

**Unidad:** M5.1 Planificación y Preparación (Incl. BIA) · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 179 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** Todo agente con capacidad de acción necesita un mecanismo probado para detenerlo y una ruta de escalamiento con autoridad clara: quién puede pulsar el kill switch, cómo, en cuánto tiempo y qué pasa después (rollback, comunicación).

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** Todo agente con capacidad de acción necesita un mecanismo probado para detenerlo y una ruta de escalamiento con autoridad clara: quién puede pulsar el kill switch, cómo, en cuánto tiempo y qué pasa después (rollback, comunicación). La tesis es que un kill switch no probado no existe, y que la prueba debe ser periódica porque los agentes y la plataforma cambian.

**Tensión y límites.** La tensión es que detener un agente puede detener un control (si AG-03 se pausa, nadie gestiona la cuarentena); el kill switch necesita el modo degradado (M6.1-PA01). Otra tensión es la autoridad: ¿puede un analista de turno detener un agente del que el owner es responsable?

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: circuit breakers, gestión de crisis, derechos de decisión. Implementación: desactivación en Power Platform admin center / Agent 365, revocación de Entra Agent ID, ruta de escalamiento (analista → PO-GAC → CISO), prueba trimestral con tiempo medido.

**Evidencia y evaluación.** Evidencia: procedimiento de kill switch con prueba trimestral documentada (tiempo, efecto, rollback). Se evalúa que cualquier turno pueda ejecutarlo.

**Puentes.** Se apoya en HC-010; se relaciona con AMP-18, AMP-43 y M6.1-PA01; sostiene AGC-10 y AGC-17.

**Recomendaciones de práctica y ejercitación.**
1. Documentar el procedimiento de kill switch y la ruta de escalamiento por agente.
2. Probarlo con AG-02 y medir tiempo y efecto.
3. Definir qué tareas pasan a modo manual al detener cada agente.

**Próximos pasos.**
- Programar la prueba trimestral (AGC-10).
- Incluir en el playbook 'agente comprometido'.
- Dar permisos de detención a los turnos.

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
| AMP-43 | AMP | Tabletop de incidentes con agentes | misma unidad |
| HC-007 | HC | Resiliencia gobernada por impacto | misma unidad |
| HC-020 | HC | Respuesta y comunicación bajo incertidumbre | misma unidad |
| HC-022 | HC | Gobierno de crisis multidisciplinario | misma unidad |
| HC-025 | HC | Competencias y resiliencia organizacional | misma unidad |
| HC-030 | HC | Seguridad industrial y continuidad de negocio | misma unidad |
| HC-037 | HC | Alineación entre competencias y decisiones | misma unidad |
| HC-039 | HC | Riesgo cibernético como narrativa empresarial | misma unidad |
| M5.1-PA01 | PA | Playbooks de incidentes de correo con roles humano/agente | misma unidad |

**Pregunta generadora:** ¿Cuánto tardaría el analista de guardia de esta noche en detener a su agente de remediación, y tiene permiso para hacerlo?

---

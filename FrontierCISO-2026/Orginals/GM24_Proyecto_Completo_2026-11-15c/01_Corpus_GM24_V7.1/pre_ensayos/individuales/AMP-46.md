# Pre-ensayo · AMP-46

> **GM-24 V7.1 · The Next CISO + Sub-plan PO-GAC** · 2026-11-14. Catálogo: 379 conceptos (245 K · 52 AMP · 40 HC · 42 PA), todos con pre-ensayo íntegro y mapeados a 17 marcos (NIST/ISACA/MITRE/OWASP/CIS/CSA). V7.1 = ChangeSet editorial CS-GM24-V7.1-001 (4 títulos generalizados; sin cambio de IDs, cantidad ni mapeo). Plano A (corpus académico). Referencias DD/K4x/R/eo:OP/COE: marco interno.

### 088. AMP-46 — Trazabilidad de decisiones autónomas

**Unidad:** M5.2 Ejecución, Post-Mortem y Comunicación · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 184 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** Registrar qué vio, qué decidió y con qué autoridad actuó un sistema autónomo es condición de rendición de cuentas y de mejora: sin ese registro no se puede atribuir, explicar ni corregir.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** Registrar qué vio, qué decidió y con qué autoridad actuó un sistema autónomo es condición de rendición de cuentas y de mejora: sin ese registro no se puede atribuir, explicar ni corregir. La tesis es que la trazabilidad de decisiones autónomas tiene un esquema mínimo —entrada, fuentes, decisión, herramientas, aprobador, resultado, versión— y que ese esquema es común a toda la flota para poder auditarla como conjunto.

**Tensión y límites.** La tensión es entre trazabilidad y rendimiento/costo, y entre registro y privacidad. Otra tensión es la interpretabilidad: registrar la 'decisión' de un modelo no explica su causa. El ensayo debe distinguir trazabilidad (qué pasó) de explicabilidad (por qué).

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: logging y trazabilidad (ISO 27001 A.8.15), AI RMF MEASURE, auditoría. Implementación: esquema de evidencia estándar (skill SK-03) escrito por todos los agentes en SharePoint/Dataverse y correlacionado en Sentinel; paquete de evidencia de un agente para auditoría.

**Evidencia y evaluación.** Evidencia: paquete de evidencia de un agente con el esquema completo para un mes. Se evalúa la completitud y la posibilidad de auditar sin el owner.

**Puentes.** Se apoya en HC-012; se relaciona con AMP-13, AMP-45 y G3.2-PA01; sostiene AGC-11 y AGC-22.

**Recomendaciones de práctica y ejercitación.**
1. Definir el esquema de evidencia común (SK-03) y aplicarlo a tres agentes.
2. Producir el paquete de evidencia de un mes para un agente.
3. Entregarlo a alguien ajeno y pedir que reconstruya tres decisiones.

**Próximos pasos.**
- Registrar como AGC-11.
- Conectar con la auditoría anual (AGC-22).
- Revisar el esquema al cambiar de ruta.

**Relación con los conceptos de la(s) unidad(es) M5.2.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M5.2-K01 | K | Contención | misma unidad |
| M5.2-K02 | K | Erradicación | misma unidad |
| M5.2-K03 | K | Recuperación | misma unidad |
| M5.2-K04 | K | Comunicación Crisis | misma unidad |
| M5.2-K05 | K | Post-Mortem | misma unidad |
| M5.2-K06 | K | Forense Digital | misma unidad |
| M5.2-K07 | K | Triaje | misma unidad |
| M5.2-K08 | K | Gestión Narrativa | misma unidad |
| M5.2-K09 | K | Notificación Brechas | misma unidad |
| M5.2-K10 | K | Resiliencia Adaptativa | misma unidad |
| AMP-45 | AMP | Forense de agentes | misma unidad |
| HC-019 | HC | SOC agéntico con supervisión humana | misma unidad |
| HC-020 | HC | Respuesta y comunicación bajo incertidumbre | misma unidad |
| HC-021 | HC | Recuperación como prueba de confianza | misma unidad |
| HC-035 | HC | Aprendizaje desde incidentes hasta políticas | misma unidad |
| M5.2-PA01 | PA | Ejecución de respuesta en correo: AIR, acciones manuales y acciones de agentes con aprobación | misma unidad |
| M5.2-PA02 | PA | Mejora gobernada de agentes: del post-mortem al ChangeSet con regresión | misma unidad |

**Pregunta generadora:** ¿Podría un auditor externo, sin hablar con usted, reconstruir las decisiones de su agente del último mes?

---

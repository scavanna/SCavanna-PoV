# Pre-ensayo · AMP-25

> **GM-24 V7.1 · The Next CISO + Sub-plan PO-GAC** · 2026-11-14. Catálogo: 379 conceptos (245 K · 52 AMP · 40 HC · 42 PA), todos con pre-ensayo íntegro y mapeados a 17 marcos (NIST/ISACA/MITRE/OWASP/CIS/CSA). V7.1 = ChangeSet editorial CS-GM24-V7.1-001 (4 títulos generalizados; sin cambio de IDs, cantidad ni mapeo). Plano A (corpus académico). Referencias DD/K4x/R/eo:OP/COE: marco interno.

### 067. AMP-25 — Ética de autonomía

**Unidad:** G6.2 Liderazgo Ético y Medición de Efectividad · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 200 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** Delegar decisiones en sistemas autónomos plantea preguntas de proporcionalidad (¿la acción automática es proporcional al riesgo?), transparencia (¿los afectados saben que decidió una máquina?) y derecho a revisión humana (¿pueden pedir que una persona reconsidere?).

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** Delegar decisiones en sistemas autónomos plantea preguntas de proporcionalidad (¿la acción automática es proporcional al riesgo?), transparencia (¿los afectados saben que decidió una máquina?) y derecho a revisión humana (¿pueden pedir que una persona reconsidere?). La tesis es que el CISO debe hacer explícitas esas preguntas para cada agente que actúa sobre personas —por ejemplo, el que remueve correo de un buzón— y documentar las respuestas como parte del gobierno, no de la ética abstracta.

**Tensión y límites.** La tensión es que la ética parece ajena al SOC, donde la urgencia manda. Pero remover un mensaje legítimo, bloquear un remitente o etiquetar a un usuario como riesgoso son decisiones sobre personas. Otra tensión es la transparencia frente a la seguridad: avisar demasiado ayuda al adversario.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: principios de IA responsable, proporcionalidad, derecho a revisión. Implementación: análisis de tres dilemas del SOC (remediación masiva, etiquetado de usuarios riesgosos, bloqueo de dominios legítimos) con decisión documentada; disclosure del uso de agentes (AGC-21).

**Evidencia y evaluación.** Evidencia: análisis de tres dilemas con decisión y justificación; texto de disclosure aprobado. Se evalúa la conexión con los principios y la operabilidad de las decisiones.

**Puentes.** Se apoya en HC-012 (confianza verificable); se relaciona con AMP-26, AMP-02 y G6.2-K05 (ética); sostiene AGC-21.

**Recomendaciones de práctica y ejercitación.**
1. Analizar tres dilemas de automatización del SOC con proporcionalidad, transparencia y revisión.
2. Redactar el texto de disclosure del uso de agentes para los usuarios.
3. Definir el canal de revisión humana para decisiones de agentes sobre personas.

**Próximos pasos.**
- Registrar como AGC-21.
- Incluir en la política de agentes.
- Revisar ante nuevos tipos de acción.

**Relación con los conceptos de la(s) unidad(es) G6.2.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| G6.2-K01 | K | Liderazgo Ético | misma unidad |
| G6.2-K02 | K | Conducta Profesional | misma unidad |
| G6.2-K03 | K | Conflictos Interés | misma unidad |
| G6.2-K04 | K | Debida Diligencia | misma unidad |
| G6.2-K05 | K | Métricas Gobierno | misma unidad |
| G6.2-K06 | K | Efectividad Programa | misma unidad |
| G6.2-K07 | K | Mejora Continua | misma unidad |
| G6.2-K08 | K | Aseguramiento | misma unidad |
| G6.2-K09 | K | Balance Riesgo-Valor | misma unidad |
| G6.2-K10 | K | Rendición Cuentas | misma unidad |
| AMP-26 | AMP | Supervisión humana efectiva | misma unidad |
| HC-006 | HC | Valor de seguridad y medición causal | misma unidad |
| HC-012 | HC | Confianza verificable en decisiones de IA | misma unidad |
| HC-021 | HC | Recuperación como prueba de confianza | misma unidad |
| HC-026 | HC | Ética, cultura y controles internos | misma unidad |
| HC-027 | HC | Métricas que no engañan | misma unidad |
| AMP-52 | AMP | Content safety y riesgos de contenido generado | misma unidad |
| G6.2-PA01 | PA | Métricas de efectividad del gobierno de la flota | misma unidad |

**Pregunta generadora:** ¿Saben los empleados de su organización que un agente puede remover mensajes de su buzón, y a quién pueden reclamar?

---

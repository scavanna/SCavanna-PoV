# Pre-ensayo · AMP-22

> **GM-24 V7.1 · The Next CISO + Sub-plan PO-GAC** · 2026-11-14. Catálogo: 379 conceptos (245 K · 52 AMP · 40 HC · 42 PA), todos con pre-ensayo íntegro y mapeados a 17 marcos (NIST/ISACA/MITRE/OWASP/CIS/CSA). V7.1 = ChangeSet editorial CS-GM24-V7.1-001 (4 títulos generalizados; sin cambio de IDs, cantidad ni mapeo). Plano A (corpus académico). Referencias DD/K4x/R/eo:OP/COE: marco interno.

### 064. AMP-22 — Aceptación de riesgo de agentes

**Unidad:** G5.2 Supervisión del Tratamiento y Aceptación · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 173 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** Aceptar el riesgo residual de un agente exige autoridad de negocio, condiciones de operación, caducidad y monitoreo; no una aprobación técnica implícita del constructor.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** Aceptar el riesgo residual de un agente exige autoridad de negocio, condiciones de operación, caducidad y monitoreo; no una aprobación técnica implícita del constructor. La tesis es que la aceptación debe formalizarse como autorización para operar (ATO) con expediente: ficha, clasificación de autonomía, evaluación, identidad y datos, modelo de amenazas, compensatorios, kill switch, presupuesto, exposición regulatoria y firma del dueño del riesgo con vigencia.

**Tensión y límites.** La tensión es la fricción: un ATO por agente puede frenar la adopción; la respuesta es proporcionalidad (expediente ligero para L1, completo para L2+). Otra tensión es la caducidad: un agente autorizado hace un año sobre un modelo distinto no debería seguir autorizado.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: NIST RMF Authorize, aceptación de riesgo (G4.2-K10). Implementación: plantilla de expediente ATO del sub-plan; registro en Agent 365; comité de ciberriesgo (DD17, referencia interna) para alto riesgo; revocación por desactivación en PPAC/Agent 365.

**Evidencia y evaluación.** Evidencia: tres expedientes ATO firmados con vigencia y condiciones. Se evalúa la proporcionalidad y la claridad de las condiciones.

**Puentes.** Extiende G5.2-K03 (autorización residual); sostiene AGC-13; se relaciona con HC-028 y AMP-17.

**Recomendaciones de práctica y ejercitación.**
1. Preparar el expediente ATO de AG-03 con las diez piezas.
2. Defenderlo ante un par que haga de dueño del riesgo.
3. Definir la proporcionalidad del expediente por nivel de autonomía.

**Próximos pasos.**
- Registrar la autorización en Agent 365 (AGC-13).
- Programar la caducidad y la re-autorización.
- Conectar con la revisión de desempeño.

**Relación con los conceptos de la(s) unidad(es) G5.2.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| G5.2-K01 | K | Supervisión de Respuestas | misma unidad |
| G5.2-K02 | K | Alineación con Apetito | misma unidad |
| G5.2-K03 | K | Autorización Residual | misma unidad |
| G5.2-K04 | K | Mitigación | misma unidad |
| G5.2-K05 | K | Transferencia | misma unidad |
| G5.2-K06 | K | Evitación | misma unidad |
| G5.2-K07 | K | Gestión Residual | misma unidad |
| G5.2-K08 | K | Comunicación Decisiones | misma unidad |
| G5.2-K09 | K | Métricas Mitigación | misma unidad |
| G5.2-K10 | K | Auditoría Tratamiento | misma unidad |
| AMP-21 | AMP | Decisiones reversibles | misma unidad |
| HC-003 | HC | Riesgo residual y aceptación verificable | misma unidad |
| HC-028 | HC | Gestión de excepciones y compensaciones | misma unidad |
| HC-034 | HC | Decisiones reversibles y riesgo de transición | misma unidad |

**Pregunta generadora:** ¿Quién autorizó al agente que hoy remedia correo en su tenant, con qué condiciones y hasta cuándo?

---

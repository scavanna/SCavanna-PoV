# Pre-ensayo · AMP-17

> **GM-24 V7.1 · The Next CISO + Sub-plan PO-GAC** · 2026-11-14. Catálogo: 379 conceptos (245 K · 52 AMP · 40 HC · 42 PA), todos con pre-ensayo íntegro y mapeados a 17 marcos (NIST/ISACA/MITRE/OWASP/CIS/CSA). V7.1 = ChangeSet editorial CS-GM24-V7.1-001 (4 títulos generalizados; sin cambio de IDs, cantidad ni mapeo). Plano A (corpus académico). Referencias DD/K4x/R/eo:OP/COE: marco interno.

### 059. AMP-17 — Autoridad delegada

**Unidad:** G4.2 Definición y Comunicación del Apetito de Riesgo · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 198 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** Delegar autoridad en sistemas autónomos es una decisión de apetito de riesgo: qué acciones puede ejecutar el agente, con qué límites, bajo qué supervisión y quién puede revocar la delegación.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** Delegar autoridad en sistemas autónomos es una decisión de apetito de riesgo: qué acciones puede ejecutar el agente, con qué límites, bajo qué supervisión y quién puede revocar la delegación. No es una decisión técnica del constructor sino una decisión de gobierno del dueño del riesgo. La tesis es que el apetito de autonomía debe declararse por tipo de acción (reversible/irreversible, impacto, alcance) antes de construir el agente.

**Tensión y límites.** La tensión es que el apetito se expresa en términos de negocio y la autonomía en términos técnicos; traducir uno a otro es el trabajo del owner. Otra tensión es la deriva: la autonomía se amplía 'porque funciona' sin volver a pasar por el dueño del riesgo.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: apetito de riesgo (ISO 31000), derechos de decisión, delegación. Implementación: declaración de apetito de autonomía del control de correo (qué puede hacer un agente en L1, L2, L3; qué nunca), firmada por el dueño del riesgo; registrada como DD18 (referencia interna).

**Evidencia y evaluación.** Evidencia: declaración de apetito de autonomía aprobada y aplicada a los quince agentes. Se evalúa que cada agente tenga nivel coherente con la declaración.

**Puentes.** Se apoya en HC-010 (capacidad, permiso, delegación, ejecución); se concreta en AMP-18; sostiene AGC-04 y G4.2-PA01.

**Recomendaciones de práctica y ejercitación.**
1. Redactar la declaración de apetito de autonomía por tipo de acción.
2. Clasificar los 15 agentes contra la declaración y detectar incoherencias.
3. Definir el procedimiento para ampliar autonomía (quién, con qué evidencia).

**Próximos pasos.**
- Operacionalizar en límites (AMP-18) y KRIs (G4.2-PA01).
- Incluir en el expediente ATO.
- Revisar en MDO-Q01.

**Relación con los conceptos de la(s) unidad(es) G4.2.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| G4.2-K01 | K | Apetito de Riesgo | misma unidad |
| G4.2-K02 | K | Tolerancia al Riesgo | misma unidad |
| G4.2-K03 | K | Documentación | misma unidad |
| G4.2-K04 | K | Comunicación | misma unidad |
| G4.2-K05 | K | Rol Ejecutivo | misma unidad |
| G4.2-K06 | K | Impacto en Estrategia | misma unidad |
| G4.2-K07 | K | Talleres de Definición | misma unidad |
| G4.2-K08 | K | Relación Apetito-Residual | misma unidad |
| G4.2-K09 | K | Métricas de Apetito | misma unidad |
| G4.2-K10 | K | Aceptación Formal | misma unidad |
| AMP-18 | AMP | Límites de autonomía | misma unidad |
| HC-002 | HC | Apetito de riesgo convertido en arquitectura | misma unidad |
| HC-003 | HC | Riesgo residual y aceptación verificable | misma unidad |
| HC-007 | HC | Resiliencia gobernada por impacto | misma unidad |
| HC-010 | HC | Autonomía delegada y límites de acción | misma unidad |
| HC-027 | HC | Métricas que no engañan | misma unidad |
| HC-040 | HC | Homeostasis organizacional de seguridad | misma unidad |
| G4.2-PA01 | PA | KRIs de la flota de agentes y umbrales de intervención | misma unidad |

**Pregunta generadora:** ¿Qué acción de su SOC jamás permitiría que un agente ejecute sin aprobación, y está escrito?

---

# Pre-ensayo · AMP-12

> **GM-24 V7.1 · The Next CISO + Sub-plan PO-GAC** · 2026-11-14. Catálogo: 379 conceptos (245 K · 52 AMP · 40 HC · 42 PA), todos con pre-ensayo íntegro y mapeados a 17 marcos (NIST/ISACA/MITRE/OWASP/CIS/CSA). V7.1 = ChangeSet editorial CS-GM24-V7.1-001 (4 títulos generalizados; sin cambio de IDs, cantidad ni mapeo). Plano A (corpus académico). Referencias DD/K4x/R/eo:OP/COE: marco interno.

### 054. AMP-12 — Responsabilidad por agentes

**Unidad:** G3.1 Requisitos Legales, Regulatorios y Contractuales · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 208 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** Cuando un agente actúa, la responsabilidad no se transfiere al software: debe existir un dueño identificable, límites contractuales claros cuando el agente es de un tercero y trazabilidad de lo actuado para poder atribuir.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** Cuando un agente actúa, la responsabilidad no se transfiere al software: debe existir un dueño identificable, límites contractuales claros cuando el agente es de un tercero y trazabilidad de lo actuado para poder atribuir. La tesis es que la responsabilidad por agentes se construye con tres piezas —dueño, contrato, traza— y que la ausencia de cualquiera deja a la organización sin posibilidad de responder ante un regulador, un cliente o un tribunal.

**Tensión y límites.** La tensión es la cadena de proveedores: modelo de un proveedor, plataforma de otro, agente construido por un integrador, operado por el cliente. La responsabilidad se reparte contractualmente pero la accountability ante el afectado no. El ensayo debe discutir qué cláusulas mínimas y qué evidencia necesita la organización para no quedar sola.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: responsabilidad civil y contractual, TPRM, principios de IA responsable. Implementación: cláusulas tipo para contratos de MDR con agentes y para plataformas (identidad propia del agente del proveedor, límites, trazas entregadas, derecho a desactivar), sponsor en Entra Agent ID, trazas en Sentinel.

**Evidencia y evaluación.** Evidencia: cláusulas tipo revisadas por Legal y verificación de trazabilidad para un agente de terceros. Se evalúa la completitud de las tres piezas.

**Puentes.** Se apoya en HC-009 (identidades no humanas) y AMP-03; sostiene M1.2-PA02 (contratos) y AGC-02; se relaciona con G3.1-PA01.

**Recomendaciones de práctica y ejercitación.**
1. Redactar las cláusulas tipo (identidad, límites, trazas, desactivación) para agentes de terceros.
2. Verificar la trazabilidad de un agente provisto por un tercero hasta el nivel de acción.
3. Recorrer un caso hipotético con Legal: quién responde ante quién.

**Próximos pasos.**
- Incorporar las cláusulas al anexo RFP (M1.2-PA02).
- Registrar a los agentes de terceros en el inventario (M2.1-PA01).
- Revisar anualmente con Legal.

**Relación con los conceptos de la(s) unidad(es) G3.1.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| G3.1-K01 | K | Identificación de Requisitos | misma unidad |
| G3.1-K02 | K | Leyes de Privacidad | misma unidad |
| G3.1-K03 | K | Regulaciones Sectoriales | misma unidad |
| G3.1-K04 | K | Obligaciones Contractuales | misma unidad |
| G3.1-K05 | K | Implicaciones CISO | misma unidad |
| G3.1-K06 | K | Gestión de Privacidad | misma unidad |
| G3.1-K07 | K | Cumplimiento Integrado | misma unidad |
| G3.1-K08 | K | Riesgos Legales | misma unidad |
| G3.1-K09 | K | Auditorías de Cumplimiento | misma unidad |
| G3.1-K10 | K | Responsabilidad Legal | misma unidad |
| AMP-11 | AMP | Soberanía de datos | misma unidad |
| HC-005 | HC | Cumplimiento continuo orientado a resultados | misma unidad |
| HC-008 | HC | Cadena de confianza en terceros | misma unidad |
| HC-011 | HC | Seguridad de datos en la IA empresarial | misma unidad |
| HC-024 | HC | Cumplimiento y privacidad por diseño | misma unidad |
| HC-029 | HC | Aseguramiento de terceros y cadena de suministro | misma unidad |
| HC-033 | HC | Seguridad y soberanía de datos distribuidos | misma unidad |
| G3.1-PA01 | PA | Panorama regulatorio de IA y agentes | misma unidad |

**Pregunta generadora:** Si el agente de su proveedor removiera correo legítimo de un ejecutivo, ¿qué cláusula se aplicaría y qué traza tendría usted para demostrarlo?

---

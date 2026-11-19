# Pre-ensayo · AMP-03

> **GM-24 V7.1 · The Next CISO + Sub-plan PO-GAC** · 2026-11-14. Catálogo: 379 conceptos (245 K · 52 AMP · 40 HC · 42 PA), todos con pre-ensayo íntegro y mapeados a 17 marcos (NIST/ISACA/MITRE/OWASP/CIS/CSA). V7.1 = ChangeSet editorial CS-GM24-V7.1-001 (4 títulos generalizados; sin cambio de IDs, cantidad ni mapeo). Plano A (corpus académico). Referencias DD/K4x/R/eo:OP/COE: marco interno.

### 045. AMP-03 — Autoridad frente a responsabilidad

**Unidad:** G1.1 Principios de Gobierno, Contexto Organizacional y Arquetipos CISO · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 261 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** Responder sin autoridad, o decidir sin responder, es la falla de gobierno más frecuente, y la llegada de agentes la vuelve aguda: un agente ejecuta una acción con autoridad delegada, pero no puede responder por ella.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** Responder sin autoridad, o decidir sin responder, es la falla de gobierno más frecuente, y la llegada de agentes la vuelve aguda: un agente ejecuta una acción con autoridad delegada, pero no puede responder por ella. La tesis es que toda delegación a un agente debe tener un humano identificable que responde por el resultado y por el proceso, que esa persona debe tener autoridad real sobre el agente (configurarlo, limitarlo, detenerlo) y que la organización debe poder nombrarla antes del despliegue y no después del incidente.

**Tensión y límites.** La tensión aparece cuando el agente es compartido entre equipos, construido por uno y usado por otro, o provisto por un tercero: la autoridad se fragmenta y la responsabilidad se diluye. Otra tensión es la asimetría de competencia: el responsable formal puede no entender lo que el agente hace. El ensayo debe discutir el sponsor como figura mínima y los límites de la delegación hacia abajo.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: accountability y derechos de decisión; teoría de agencia. Implementación: sponsor obligatorio en Entra Agent ID, owner en Agent 365, declaración de accountability firmada por el PO-GAC para cada agente, y matriz de derechos de decisión de tres niveles (owner / dueño del riesgo / CISO).

**Evidencia y evaluación.** Evidencia: declaración de accountability de la flota y verificación de que cada agente registrado tiene sponsor con autoridad efectiva (puede detenerlo). Se evalúa la ausencia de agentes sin responsable y la coherencia entre autoridad declarada y permisos reales.

**Puentes.** Extiende G6.2-K10 (rendición de cuentas) y G1.1-K03; es la base de AGC-02 y de G4.1-PA01 (tres líneas); se relaciona con AMP-12 y HC-009.

**Recomendaciones de práctica y ejercitación.**
1. Redactar la declaración de accountability del PO-GAC para la flota.
2. Verificar en Entra/Agent 365 que cada agente tiene sponsor con capacidad real de detenerlo.
3. Simular un incidente y recorrer la cadena de responsabilidad hasta el CISO.

**Próximos pasos.**
- Registrar la declaración como evidencia de AGC-02.
- Incluirla en el expediente ATO (AMP-22).
- Revisar la cadena cuando un agente cambie de owner.

**Relación con los conceptos de la(s) unidad(es) G1.1.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| G1.1-K01 | K | Principios de Gobierno | misma unidad |
| G1.1-K02 | K | Contexto Organizacional | misma unidad |
| G1.1-K03 | K | Arquetipos CISO | misma unidad |
| G1.1-K04 | K | Alineación Estratégica | misma unidad |
| G1.1-K05 | K | Cultura de Seguridad | misma unidad |
| G1.1-K06 | K | Visión Holística | misma unidad |
| G1.1-K07 | K | CISO como Socio de Negocio | misma unidad |
| G1.1-K08 | K | Gestión Estratégica del Riesgo | misma unidad |
| G1.1-K09 | K | Liderazgo de Influencia | misma unidad |
| G1.1-K10 | K | Mejora Continua (Gobierno) | misma unidad |
| AMP-01 | AMP | Metacognición del CISO | misma unidad |
| AMP-02 | AMP | Sesgos y límites cognitivos | misma unidad |
| HC-001 | HC | Gobierno de decisiones basadas en evidencia | misma unidad |
| HC-037 | HC | Alineación entre competencias y decisiones | misma unidad |
| HC-040 | HC | Homeostasis organizacional de seguridad | misma unidad |
| G1.1-PA01 | PA | Rol dual especialista/manager y Product Owner de control | misma unidad |

**Pregunta generadora:** Si mañana un agente de su flota tomara una decisión equivocada con impacto en un cliente, ¿quién daría la cara, y esa persona sabe hoy que lo haría?

---

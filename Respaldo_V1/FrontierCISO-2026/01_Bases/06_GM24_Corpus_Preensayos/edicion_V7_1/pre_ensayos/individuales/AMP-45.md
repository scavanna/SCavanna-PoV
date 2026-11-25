# Pre-ensayo · AMP-45

> **GM-24 V7.1 · The Next CISO + Sub-plan PO-GAC** · 2026-11-14. Catálogo: 379 conceptos (245 K · 52 AMP · 40 HC · 42 PA), todos con pre-ensayo íntegro y mapeados a 17 marcos (NIST/ISACA/MITRE/OWASP/CIS/CSA). V7.1 = ChangeSet editorial CS-GM24-V7.1-001 (4 títulos generalizados; sin cambio de IDs, cantidad ni mapeo). Plano A (corpus académico). Referencias DD/K4x/R/eo:OP/COE: marco interno.

### 087. AMP-45 — Forense de agentes

**Unidad:** M5.2 Ejecución, Post-Mortem y Comunicación · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 178 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** Investigar un incidente con agentes exige reconstruir qué instrucciones tenía, qué herramientas invocó, qué datos accedió y qué decisiones tomó; sin telemetría de agentes no hay forense, solo hipótesis.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** Investigar un incidente con agentes exige reconstruir qué instrucciones tenía, qué herramientas invocó, qué datos accedió y qué decisiones tomó; sin telemetría de agentes no hay forense, solo hipótesis. La tesis es que los requisitos de telemetría forense se definen antes del despliegue (qué se registra siempre, con qué retención e integridad) porque después del incidente es tarde.

**Tensión y límites.** La tensión es el volumen y el costo de registrar todo, y la privacidad de registrar contenido de correo que el agente leyó. El ensayo debe proponer qué registrar siempre (invocaciones, decisiones, aprobaciones, versión), qué por muestreo (razonamiento) y qué nunca (contenido sensible completo).

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: forense digital, cadena de custodia, logging. Implementación: requisitos de telemetría forense por agente (logs de Copilot Studio, tracing de Foundry, Purview Audit, sign-in logs de Agent ID, Sentinel con retención inmutable); reconstrucción de un caso simulado.

**Evidencia y evaluación.** Evidencia: requisitos de telemetría por agente y reconstrucción forense de un fallo simulado. Se evalúa que la reconstrucción sea posible solo con los registros definidos.

**Puentes.** Extiende M5.2-K06 (forense digital); se relaciona con AMP-46, M4.1-PA05 y M5.2-PA02; sostiene AGC-11.

**Recomendaciones de práctica y ejercitación.**
1. Definir los requisitos de telemetría forense por agente (siempre / muestreo / nunca).
2. Reconstruir un fallo simulado de AG-03 solo con los registros.
3. Verificar retención e integridad de las fuentes.

**Próximos pasos.**
- Incorporar al tablero de observabilidad (M4.1-PA05).
- Registrar como AGC-11.
- Probar la reconstrucción en el tabletop.

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
| AMP-46 | AMP | Trazabilidad de decisiones autónomas | misma unidad |
| HC-019 | HC | SOC agéntico con supervisión humana | misma unidad |
| HC-020 | HC | Respuesta y comunicación bajo incertidumbre | misma unidad |
| HC-021 | HC | Recuperación como prueba de confianza | misma unidad |
| HC-035 | HC | Aprendizaje desde incidentes hasta políticas | misma unidad |
| M5.2-PA01 | PA | Ejecución de respuesta en correo: AIR, acciones manuales y acciones de agentes con aprobación | misma unidad |
| M5.2-PA02 | PA | Mejora gobernada de agentes: del post-mortem al ChangeSet con regresión | misma unidad |

**Pregunta generadora:** Si su agente de FP/FN hubiera liberado un mensaje malicioso la semana pasada, ¿podría reconstruir hoy por qué lo hizo?

---

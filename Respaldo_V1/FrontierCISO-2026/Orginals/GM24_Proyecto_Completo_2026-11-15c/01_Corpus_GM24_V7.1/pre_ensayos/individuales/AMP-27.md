# Pre-ensayo · AMP-27

> **GM-24 V7.1 · The Next CISO + Sub-plan PO-GAC** · 2026-11-14. Catálogo: 379 conceptos (245 K · 52 AMP · 40 HC · 42 PA), todos con pre-ensayo íntegro y mapeados a 17 marcos (NIST/ISACA/MITRE/OWASP/CIS/CSA). V7.1 = ChangeSet editorial CS-GM24-V7.1-001 (4 títulos generalizados; sin cambio de IDs, cantidad ni mapeo). Plano A (corpus académico). Referencias DD/K4x/R/eo:OP/COE: marco interno.

### 069. AMP-27 — CISO-OS

**Unidad:** M1.1 Desarrollo, Gestión y Operaciones del Programa de Seguridad · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 181 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** Un sistema operativo del CISO integra datos (telemetría, riesgos, evidencias), decisiones (registro, derechos de decisión), agentes (que ejecutan tareas) y evidencia del programa, para gobernar la seguridad como un servicio continuo y no como una sucesión de proyectos.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** Un sistema operativo del CISO integra datos (telemetría, riesgos, evidencias), decisiones (registro, derechos de decisión), agentes (que ejecutan tareas) y evidencia del programa, para gobernar la seguridad como un servicio continuo y no como una sucesión de proyectos. La tesis es que el CISO-OS no es un producto sino una arquitectura de gobierno: define qué datos alimentan qué decisiones, qué agentes operan qué procesos y qué evidencia demuestra que todo funciona.

**Tensión y límites.** La tensión es la tentación de comprar una herramienta y llamarla CISO-OS. Otra tensión es la integración: datos y decisiones viven en sistemas distintos. El ensayo debe mostrar un mapa mínimo de componentes y sus interfaces.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: arquitectura de gobierno, gestión de servicios, sistemas de decisión. Implementación: mapa de componentes del CISO-OS para el control de correo (Defender/Sentinel como datos, registro de decisiones, flota de agentes, Purview/Agent 365 como evidencia) y sus interfaces.

**Evidencia y evaluación.** Evidencia: mapa de componentes con flujos de datos, decisiones y evidencia. Se evalúa la coherencia con el modelo operativo y la flota.

**Puentes.** Extiende M1.1-K03 (oficina del CISO); se relaciona con AMP-28, HC-036 y M1.1-PA01; sostiene G1.1-PA01.

**Recomendaciones de práctica y ejercitación.**
1. Dibujar el mapa de componentes del CISO-OS para el control de correo.
2. Identificar las interfaces inexistentes o manuales.
3. Ubicar a los 15 agentes en el mapa.

**Próximos pasos.**
- Usarlo como base del organigrama híbrido (M1.1-PA01).
- Priorizar las integraciones faltantes.
- Revisar al cambiar la plataforma.

**Relación con los conceptos de la(s) unidad(es) M1.1.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M1.1-K01 | K | Programa de Seguridad | misma unidad |
| M1.1-K02 | K | Alcance y Objetivos | misma unidad |
| M1.1-K03 | K | Oficina del CISO | misma unidad |
| M1.1-K04 | K | Alineación Operativa | misma unidad |
| M1.1-K05 | K | Ciclo de Vida | misma unidad |
| M1.1-K06 | K | Recursos | misma unidad |
| M1.1-K07 | K | Medición Rendimiento | misma unidad |
| M1.1-K08 | K | Interesados (Stakeholders) | misma unidad |
| M1.1-K09 | K | Integración Gobierno | misma unidad |
| M1.1-K10 | K | Mejora Continua | misma unidad |
| AMP-28 | AMP | Orquestación de agentes | misma unidad |
| HC-006 | HC | Valor de seguridad y medición causal | misma unidad |
| HC-027 | HC | Métricas que no engañan | misma unidad |
| HC-035 | HC | Aprendizaje desde incidentes hasta políticas | misma unidad |
| HC-036 | HC | Portafolio de controles y capacidades | misma unidad |
| M1.1-PA01 | PA | Diseño organizativo híbrido: roles, RACI y span of control | misma unidad |
| M1.1-PA02 | PA | Portafolio de productos-control con owners | misma unidad |
| M1.1-PA03 | PA | Modelo operativo por cadencias y excelencia operacional como requisito del programa | misma unidad |

**Pregunta generadora:** Si tuviera que dibujar en una página cómo fluye una señal hasta convertirse en decisión y evidencia en su programa, ¿qué cajas faltarían?

---

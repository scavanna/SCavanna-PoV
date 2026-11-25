# Pre-ensayo · AMP-28

> **GM-24 V7.1 · The Next CISO + Sub-plan PO-GAC** · 2026-11-14. Catálogo: 379 conceptos (245 K · 52 AMP · 40 HC · 42 PA), todos con pre-ensayo íntegro y mapeados a 17 marcos (NIST/ISACA/MITRE/OWASP/CIS/CSA). V7.1 = ChangeSet editorial CS-GM24-V7.1-001 (4 títulos generalizados; sin cambio de IDs, cantidad ni mapeo). Plano A (corpus académico). Referencias DD/K4x/R/eo:OP/COE: marco interno.

### 070. AMP-28 — Orquestación de agentes

**Unidad:** M1.1 Desarrollo, Gestión y Operaciones del Programa de Seguridad · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 187 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** Orquestar varios agentes exige roles, límites, traspasos y trazabilidad: cuando AG-01 deriva a AG-02 y este propone una acción, la autonomía se gobierna en el flujo (quién puede pasarle qué a quién, con qué contexto, bajo qué aprobación) y no solo en cada agente.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** Orquestar varios agentes exige roles, límites, traspasos y trazabilidad: cuando AG-01 deriva a AG-02 y este propone una acción, la autonomía se gobierna en el flujo (quién puede pasarle qué a quién, con qué contexto, bajo qué aprobación) y no solo en cada agente. La tesis es que los traspasos entre agentes son los puntos de mayor riesgo (pérdida de contexto, escalada de privilegios, fallos en cascada) y deben diseñarse como interfaces con contrato.

**Tensión y límites.** La tensión es que la orquestación emergente (agentes que se llaman entre sí) es más poderosa y menos gobernable que la orquestación explícita. Otra tensión es la atribución: en una cadena, ¿quién decidió? El ensayo debe discutir contratos de traspaso y trazas de extremo a extremo.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: patrones de sistemas distribuidos, orquestación vs. coreografía, OWASP ASI07/ASI08. Implementación: diagrama de traspasos de la flota (AG-01→AG-02→humano; AG-03↔AG-11), contrato por traspaso (contexto, permisos, aprobación) y traza correlacionada en Sentinel.

**Evidencia y evaluación.** Evidencia: diagrama de traspasos con contratos y una traza de extremo a extremo. Se evalúa la identificación de puntos de escalada.

**Puentes.** Se apoya en HC-019; se relaciona con AMP-35, AMP-36 y M3.1-PA01; sostiene AGC-06 y AGC-11.

**Recomendaciones de práctica y ejercitación.**
1. Dibujar los traspasos de la flota y escribir el contrato de cada uno.
2. Rastrear una cadena AG-01→AG-02→humano de extremo a extremo en Sentinel.
3. Identificar un punto donde un traspaso podría escalar privilegios.

**Próximos pasos.**
- Incorporar los contratos a las fichas.
- Probar fallos en cascada en el tabletop (AMP-43).
- Revisar al agregar agentes.

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
| AMP-27 | AMP | CISO-OS | misma unidad |
| HC-006 | HC | Valor de seguridad y medición causal | misma unidad |
| HC-027 | HC | Métricas que no engañan | misma unidad |
| HC-035 | HC | Aprendizaje desde incidentes hasta políticas | misma unidad |
| HC-036 | HC | Portafolio de controles y capacidades | misma unidad |
| M1.1-PA01 | PA | Diseño organizativo híbrido: roles, RACI y span of control | misma unidad |
| M1.1-PA02 | PA | Portafolio de productos-control con owners | misma unidad |
| M1.1-PA03 | PA | Modelo operativo por cadencias y excelencia operacional como requisito del programa | misma unidad |

**Pregunta generadora:** Cuando un agente le pasa trabajo a otro en su flota, ¿qué contexto viaja, qué permisos cambian y quién lo registra?

---

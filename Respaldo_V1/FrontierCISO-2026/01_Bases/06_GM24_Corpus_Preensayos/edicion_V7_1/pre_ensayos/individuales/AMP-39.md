# Pre-ensayo · AMP-39

> **GM-24 V7.1 · The Next CISO + Sub-plan PO-GAC** · 2026-11-14. Catálogo: 379 conceptos (245 K · 52 AMP · 40 HC · 42 PA), todos con pre-ensayo íntegro y mapeados a 17 marcos (NIST/ISACA/MITRE/OWASP/CIS/CSA). V7.1 = ChangeSet editorial CS-GM24-V7.1-001 (4 títulos generalizados; sin cambio de IDs, cantidad ni mapeo). Plano A (corpus académico). Referencias DD/K4x/R/eo:OP/COE: marco interno.

### 081. AMP-39 — SOC agéntico

**Unidad:** M4.1 Operaciones de Seguridad, Monitorización e Inteligencia · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 197 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** El SOC agéntico redistribuye el trabajo: agentes que priorizan, investigan y proponen respuesta; personas que supervisan, ajustan y deciden; todo medido por tiempo de respuesta, calidad de decisión y costo.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** El SOC agéntico redistribuye el trabajo: agentes que priorizan, investigan y proponen respuesta; personas que supervisan, ajustan y deciden; todo medido por tiempo de respuesta, calidad de decisión y costo. La tesis es que el SOC agéntico no es un SOC con herramientas de IA sino un modelo operativo distinto, donde la unidad de trabajo humano pasa de 'resolver el incidente' a 'gobernar a quien lo resuelve', y donde las métricas deben cambiar en consecuencia.

**Tensión y límites.** La tensión es la pérdida de criterio humano (si nadie tria, nadie sabe triar) y la dependencia de la plataforma (si los agentes caen, el SOC cae). Otra tensión es la medición: las métricas clásicas (MTTR) mejoran mientras la calidad puede degradarse sin que nadie lo vea.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: modelos operativos de SOC, teoría de la supervisión, métricas de calidad de decisión. Implementación: redistribución del runbook (31 tareas) entre agentes y personas con niveles L0–L3, métricas de la flota (KPI-11/12/13) y de retención de criterio (rotación), operación degradada (M6.1-PA01).

**Evidencia y evaluación.** Evidencia: runbook redistribuido con métricas y plan de retención de criterio. Se evalúa la coherencia con el apetito de autonomía.

**Puentes.** Se apoya en HC-019; se relaciona con AMP-29, AMP-40 y M4.1-PA01; sostiene M4.1-PA06.

**Recomendaciones de práctica y ejercitación.**
1. Redistribuir las 31 tareas del modelo operativo entre agentes y personas.
2. Definir las métricas de calidad de decisión además de las de tiempo.
3. Diseñar la rotación que mantiene el criterio humano.

**Próximos pasos.**
- Operar un trimestre y medir (E5).
- Ajustar niveles de autonomía según resultados.
- Vincular con la operación degradada.

**Relación con los conceptos de la(s) unidad(es) M4.1.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M4.1-K01 | K | SOC Moderno | misma unidad |
| M4.1-K02 | K | Monitorización Continua | misma unidad |
| M4.1-K03 | K | Threat Intelligence (CTI) | misma unidad |
| M4.1-K04 | K | SIEM | misma unidad |
| M4.1-K05 | K | SOAR | misma unidad |
| M4.1-K06 | K | XDR | misma unidad |
| M4.1-K07 | K | Threat Hunting | misma unidad |
| M4.1-K08 | K | IA en SecOps | misma unidad |
| M4.1-K09 | K | Ciclo Vida Inteligencia | misma unidad |
| M4.1-K10 | K | TTPs | misma unidad |
| AMP-40 | AMP | Human-in-the-loop | misma unidad |
| HC-001 | HC | Gobierno de decisiones basadas en evidencia | misma unidad |
| HC-005 | HC | Cumplimiento continuo orientado a resultados | misma unidad |
| HC-010 | HC | Autonomía delegada y límites de acción | misma unidad |
| HC-012 | HC | Confianza verificable en decisiones de IA | misma unidad |
| HC-017 | HC | Inteligencia que modifica decisiones | misma unidad |
| HC-018 | HC | Observabilidad y aseguramiento de controles | misma unidad |
| HC-019 | HC | SOC agéntico con supervisión humana | misma unidad |
| HC-040 | HC | Homeostasis organizacional de seguridad | misma unidad |
| M4.1-K11 | K | Deception y señuelos como control detectivo | misma unidad |
| M4.1-PA01 | PA | Modelo operativo del producto-control por cadencias (instancias: Defender for Office 365 · Defender XDR · Defender for Endpoint · Defender for Identity/Entra · Purview · Sentinel · Defender for Cloud) | misma unidad |
| M4.1-PA02 | PA | Gestión de incidentes y alertas en Defender XDR | misma unidad |
| M4.1-PA03 | PA | Gestión de la calidad de detección del dominio: FP/FN, tuning, listas, indicadores y supresiones (instancias: MDO · XDR · MDE · MDI/ID Protection · Purview DLP · Sentinel) | misma unidad |
| M4.1-PA04 | PA | Hunting y detecciones personalizadas | misma unidad |
| M4.1-PA05 | PA | Observabilidad de la flota de agentes: telemetría, trazas y tableros | misma unidad |
| M4.1-PA06 | PA | Gestión del desempeño de agentes: revisión periódica y drift | misma unidad |

**Pregunta generadora:** En su SOC agéntico, ¿qué medirá para saber que la calidad de las decisiones no se degradó mientras el tiempo de respuesta mejoraba?

---

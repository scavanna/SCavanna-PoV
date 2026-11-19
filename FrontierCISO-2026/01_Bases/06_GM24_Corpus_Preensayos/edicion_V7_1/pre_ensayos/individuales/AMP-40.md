# Pre-ensayo · AMP-40

> **GM-24 V7.1 · The Next CISO + Sub-plan PO-GAC** · 2026-11-14. Catálogo: 379 conceptos (245 K · 52 AMP · 40 HC · 42 PA), todos con pre-ensayo íntegro y mapeados a 17 marcos (NIST/ISACA/MITRE/OWASP/CIS/CSA). V7.1 = ChangeSet editorial CS-GM24-V7.1-001 (4 títulos generalizados; sin cambio de IDs, cantidad ni mapeo). Plano A (corpus académico). Referencias DD/K4x/R/eo:OP/COE: marco interno.

### 082. AMP-40 — Human-in-the-loop

**Unidad:** M4.1 Operaciones de Seguridad, Monitorización e Inteligencia · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 180 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** Human-in-the-loop se define por riesgo, no por principio: qué acciones requieren aprobación previa (irreversibles o de alto impacto), cuáles se auditan después por muestreo (reversibles, bajo impacto) y cuáles nunca se delegan (decisiones de juicio sobre personas, aceptación de riesgo).

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** Human-in-the-loop se define por riesgo, no por principio: qué acciones requieren aprobación previa (irreversibles o de alto impacto), cuáles se auditan después por muestreo (reversibles, bajo impacto) y cuáles nunca se delegan (decisiones de juicio sobre personas, aceptación de riesgo). La tesis es que la matriz tarea → nivel → gate es el instrumento que convierte HITL en configuración y que debe revisarse con la calidad medida del agente.

**Tensión y límites.** La tensión es que 'aprobar todo' anula el valor y 'auditar todo después' acepta el daño antes de detectarlo. Otra tensión es la fatiga de aprobación (AMP-26). El ensayo debe mostrar cómo mover tareas de aprobación previa a auditoría posterior con evidencia.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: meaningful human control, niveles de automatización, gestión de riesgo operacional. Implementación: matriz tarea→nivel→gate para las 31 tareas; Approvals para L2; muestreo desde Sentinel para L3; lista de 'nunca delegar'.

**Evidencia y evaluación.** Evidencia: matriz completa con justificación por tarea y criterio de promoción L2→L3. Se evalúa la coherencia con reversibilidad y calidad medida.

**Puentes.** Se apoya en HC-019 y HC-010; se relaciona con AMP-18, AMP-26 y AMP-02; sostiene AGC-09 y M5.1-PA01.

**Recomendaciones de práctica y ejercitación.**
1. Completar la matriz tarea→nivel→gate para las 31 tareas.
2. Redactar la lista de 'nunca delegar' y justificarla.
3. Definir el criterio de promoción L2→L3 (KPI-11/12).

**Próximos pasos.**
- Configurar Approvals y muestreo según la matriz.
- Revisar la matriz en cada revisión de desempeño.
- Incluirla en la política de agentes.

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
| AMP-39 | AMP | SOC agéntico | misma unidad |
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

**Pregunta generadora:** ¿Qué tarea de su SOC pasaría de aprobación previa a auditoría posterior, y qué evidencia necesitaría para decidirlo?

---

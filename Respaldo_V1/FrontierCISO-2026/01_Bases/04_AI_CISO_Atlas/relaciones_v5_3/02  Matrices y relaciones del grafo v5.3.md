# 02 | Matrices y relaciones del grafo v5.3

> **AI CISO Atlas Curator | Knowledge Pack 5.3 | Propuesta editorial controlada**  
> No equivale a una certificación, homologación o taxonomía oficial de ISACA, CSA o NIST.  
> **Precedencia:** 01 Taxonomía > 02 Relaciones > 03 Currículo > 04 Ejemplos. Para unidades y cargas GM-24, el documento 03 es la fuente canónica.  
> Los códigos de subfunciones son del Atlas, no códigos oficiales de categorías NIST CSF.

## Principio de interoperabilidad

Un mismo concepto vive una sola vez en el grafo compartido. Atlas estructural, Atlas evolutivo y currículo GM-24 son **vistas diferentes**. Los mapeos son editoriales y deben justificarse; no constituyen equivalencias oficiales.

## Matrices relacionales

| ID | Matriz | Uso |
|---|---|---|
| R01 | Territory × Domain | Afinidad entre responsabilidad y disciplina |
| R02 | Domain × Function | Resultados de seguridad típicos por disciplina |
| R03 | AtlasSubfunction × CSF | Correspondencia pendiente de validación con CSF oficial |
| R04 | Domain × Horizon | Evolución conceptual de disciplinas |
| R05 | Force × Capability × Context | Catalizadores, inhibidores y homeostasis situados |
| R06 | Capability × Transition | Trayectorias y gates |
| R07 | Domain × Domain | Solapamientos y dependencias |
| R08 | LearningUnit × Atlas | Correspondencia curricular; fuente 03 |
| R09 | LearningUnit × ExternalFramework | Alineación ISACA/CSA inferida |

## R01: afinidades territoriales

| Dominios | Territorios más frecuentes | Comentario |
|---|---|---|
| D01–D04 | T03/T04/T08 | Diferenciar decisión estratégica, riesgo y assurance |
| D05–D11 | T05 | T07 cuando el objeto sea agente/modelo |
| D12–D16 | T06/T04 | T05 para diseño de controles |
| D17 | T04/T05 | Dependencias externas y arquitectura |
| D18–D19 | T05/T04 | Safety y continuidad pueden dominar |
| D20 | T07/T05 | IA como objeto de protección |
| D21 | T06 | IA como herramienta del SOC |
| D22 | T05 | IA como herramienta de pruebas |
| D23 | T05 | IA como herramienta de ingeniería |
| D24 | T01/T02 | Individuo frente a organización |

**Afinidad no es asignación automática.** La tesis del ensayo prevalece.

## R02: afinidades funcionales

`P` = frecuente predominante, `S` = frecuente secundario, `-` = no preasignar. No significa exclusión.

| Dominio | GV | ID | PR | DE | RS | RC |
|---|---|---|---|---|---|---|
| D01 | P | S | S | - | S | - |
| D02 | P | P | S | S | S | S |
| D03 | P | S | S | S | S | S |
| D04 | P | S | S | - | - | S |
| D05 | S | P | P | S | S | - |
| D06 | P | P | P | S | S | S |
| D07 | P | P | P | S | S | S |
| D08 | - | P | P | P | S | S |
| D09 | - | P | P | P | S | S |
| D10 | S | P | P | P | S | S |
| D11 | S | P | P | S | S | S |
| D12 | S | P | S | P | S | - |
| D13 | S | P | P | S | S | - |
| D14 | - | S | S | P | P | - |
| D15 | S | S | - | P | P | S |
| D16 | P | P | S | S | P | P |
| D17 | P | P | P | S | S | S |
| D18 | S | P | P | P | P | P |
| D19 | S | P | P | P | P | P |
| D20 | P | P | P | P | P | S |
| D21 | S | P | P | P | P | S |
| D22 | S | P | P | P | S | - |
| D23 | S | P | P | S | S | S |
| D24 | P | S | P | S | S | S |

## R03: mapeo NIST

Mantener `CSFFunction`, `CSFCategory`, `CSFSubcategory` y `AtlasSubfunction` como tipos separados. Usar `MAPS_TO` solo con versión, referencia y fundamento; `EQUIVALENT_TO` no está autorizado por defecto. **No se declara aquí una correspondencia granular validada de las 32 subfunciones**.

## R04: evolución ilustrativa

| Dominio | Foundational | Evolving | Emerging | Convergent |
|---|---|---|---|---|
| D05 IAM | IAM/MFA/PAM | NHI y permisos de agentes | delegación dinámica | autoridad humana-máquina unificada |
| D07 Privacy | minimización/derechos | privacidad en RAG | revisión de acciones de agentes | privacidad y assurance de decisiones |
| D14 Monitoring | SIEM y detecciones | copilotos SOC | investigación agéntica | operaciones humano-agente |
| D16 Recovery | BCP/DRP | dependencia de IA | recuperación de estado agéntico | resiliencia de procesos autónomos |
| D18 OT | segmentación industrial | telemetría ampliada | IA en procesos industriales | safety y seguridad integradas |
| D20 AI Security | controles AppSec aplicables | defensas LLM/RAG | autoridad multiagente | assurance de autonomía |

**Estos son ejemplos, no etapas obligatorias ni madurez medida.**

## R05/R06: dinámica y transiciones

Registrar para cada relación `force_id`, `capability_id`, `context_id`, `polarity`, `rationale`, `evidence`, `validity`. Para una transición, incluir `from_state`, `to_state`, `preconditions`, `risk_of_transition`, `authority`, `controls`, `tests`, `rollback`, `status` (`hypothesis`, `planned`, `tested`, `observed`, `rejected`).

## R07: fronteras y solapamientos

- D06 ↔ D07: proteger datos frente a legitimidad del tratamiento personal.
- D18 ↔ D19: control industrial frente a IoT/CPS general.
- D20 ↔ D21: proteger IA frente a utilizar IA en defensa.
- D13 ↔ D22: gestión de exposición frente a IA para evaluarla.
- D11 ↔ D23: AppSec frente a IA que crea controles/código.
- D14 ↔ D21: disciplina SOC frente a instrumento IA.
- D15 ↔ D16: contención y crisis frente a continuidad/restauración.
- T03 ↔ T04 ↔ T08: inversión/outcomes frente a tolerancia frente a evidencia.

## Ontología del grafo compartido

**Nodos:** `Territory`, `Domain`, `CSFFunction`, `AtlasSubfunction`, `HorizonType`, `Force`, `ContextProfile`, `Capability`, `Transition`, `RiskScenario`, `Control`, `Evidence`, `Source`, `Essay`, `LearningProgram`, `CurriculumPillar`, `CurriculumAxis`, `LearningUnit`, `Competency`, `LearningOutcome`, `LearningActivity`, `Assessment`, `LearningArtifact`, `ExternalFramework`, `MentalModel`, `Stakeholder`, `Decision`.

**Relaciones:** `CLASSIFIED_IN`, `MAPS_TO_TERRITORY`, `MAPS_TO_DOMAIN`, `MAPS_TO_CSF_FUNCTION`, `REFINES`, `HAS_PILLAR`, `HAS_AXIS`, `HAS_UNIT`, `DEVELOPS_COMPETENCY`, `HAS_LEARNING_OUTCOME`, `HAS_ACTIVITY`, `HAS_ASSESSMENT`, `PRODUCES_ARTIFACT`, `CURRICULAR_ALIGNMENT`, `ENABLES`, `INHIBITS`, `STABILIZES`, `TRANSITIONS_TO`, `DEPENDS_ON`, `MITIGATES`, `GROUNDED_IN`, `DEMONSTRATES`, `CONTRADICTS`, `SUPERSEDES`.

**Requisitos por arista:** ID de origen y destino, tipo, razón, versión, fuente o estado de hipótesis, contexto si corresponde. Nunca crear aristas por mera coincidencia léxica.

## Jerarquía de evidencia

1. Documento canónico y referencia primaria actual.
2. Documento académico GM-24 para unidades y ejes.
3. Correspondencia editorial justificada.
4. Hipótesis no validada claramente etiquetada.

**No inferir que la presencia de un mapeo en este documento significa que está aprobado o implementado en un sistema.**

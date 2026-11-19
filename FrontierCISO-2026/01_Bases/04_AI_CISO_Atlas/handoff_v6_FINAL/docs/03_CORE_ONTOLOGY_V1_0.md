# 03 — Core Ontology v1.0

## Propósito

Core Ontology complementa —no reemplaza— la taxonomía. Es un contrato semántico para sidecars, ChangeSets y el grafo.

## Fundamentos

- The Open Group: estructura arquitectónica y relaciones generales.
- NIST: resultados, riesgo, controles y metodología de correspondencias.
- ISACA: gobierno, responsabilidad, decisiones y competencias.
- CSA: controles cloud/IA, responsabilidad compartida y assurance.
- Microsoft: identidad, activos, eventos, alertas y semántica operacional.

El modelo resultante es original del Atlas y no debe presentarse como ontología oficial de esos organismos.

## Ocho módulos y 57 entidades

| Módulo | Nombre | Tipos |
|---|---|---:|
| O01 | Enterprise & Strategy | 6 |
| O02 | Governance & Accountability | 6 |
| O03 | Risk & Resilience | 6 |
| O04 | Technology & Security | 7 |
| O05 | AI & Autonomous Systems | 6 |
| O06 | Operations & Assurance | 6 |
| O07 | Competency & Learning | 6 |
| O08 | Evolution & Transformation | 6 |
| OT | Transversales | 8 |
| **Total** |  | **57** |

El catálogo completo está en `data/entity_dictionary.json`.

## Relaciones y reglas

- 58 relaciones tipadas: origen, destino, dirección, evidencia y contexto.
- 21 reglas: 6 estructurales, 8 semánticas y 7 de gobierno/epistemología.
- Catálogos: `data/relationship_dictionary.json` y `data/semantic_rules.json`.

## Principios

Identidad estable; semántica explícita; separación conceptual; procedencia; contextualidad; evolución controlada; no equivalencia automática; gobierno humano.

## Estado

`proposed baseline`. Puede probarse con ensayos, pero no debe declararse exhaustiva ni definitiva. Toda extensión se tramita como solicitud gobernada y nunca como mutación silenciosa.

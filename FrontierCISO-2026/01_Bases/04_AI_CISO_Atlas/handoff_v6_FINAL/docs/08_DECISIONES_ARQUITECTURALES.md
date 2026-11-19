# 08 — Registro de decisiones arquitecturales

| ADR | Decisión | Razonamiento | Consecuencia |
|---|---|---|---|
| ADR-001 | Conservar Taxonomy 5.3 | Ontología complementa, no reemplaza | no renumerar X/Y/Z/H |
| ADR-002 | Core Ontology 1.0 federada | ninguna fuente externa cubre todo el problema | núcleo propio + mapeos versionados |
| ADR-003 | Property graph sobre SQLite | suficiente para MVP y fácil de auditar | posponer RDF/OWL |
| ADR-004 | Cuatro skills | validación puede residir en Graph Contributor + script | no crear quinto skill |
| ADR-005 | Graph Contributor se regenera | es la frontera entre interpretación y propuesta | mayor inversión de cambio |
| ADR-006 | Validación determinista | el modelo no puede autocertificarse | Python/JSON/SQLite son autoridad técnica |
| ADR-007 | Aprobación humana | riesgo semántico y operativo | agente sin permiso de escritura/aprobación |
| ADR-008 | No equivalencia automática | frameworks difieren en propósito y granularidad | `MAPS_TO` requiere fuente, versión y justificación |
| ADR-009 | H no es madurez | describe evolución conceptual/contextual | no inferir readiness de una organización |
| ADR-010 | Conservar contradicciones | eliminar conflicto destruye evidencia | modelar `CONTRADICTS` y revisión |
| ADR-011 | Extensiones gobernadas | lo novedoso no es automáticamente inválido | crear solicitud de extensión |
| ADR-012 | Siete fuentes de conocimiento | taxonomía y ontología evolucionan a ritmos distintos | no fusionar todos los documentos |

## Inconsistencias resueltas

- El inventario final es **57 entidades**: 49 de dominio (O04 tiene siete al incluir `ControlObjective`) + 8 transversales.
- La versión técnica canónica es `ontology_version: 1.0.0`; los textos pueden abreviar “v1.0”.
- Para aprendizaje se usa `ASSESSES` en Assessment→LearningOutcome y `EVALUATES` también cubre AssessmentResult→SecurityControl.
- Las transiciones se expresan con `Transition` + `FROM_STATE`/`TO_STATE`; no se depende de una arista transitiva implícita.

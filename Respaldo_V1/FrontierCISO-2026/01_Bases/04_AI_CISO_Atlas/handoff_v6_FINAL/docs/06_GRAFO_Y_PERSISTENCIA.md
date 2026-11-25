# 06 — Grafo y persistencia

## Modelo

Property graph implementado sobre SQLite. `nodes` contiene instancias tipadas y `edges` relaciones aprobadas. El catálogo ontológico reside en tablas separadas y se carga antes del grafo.

## Tablas principales

- Catálogo: `ontology_versions`, `entity_types`, `relation_types`, `relation_type_sources`, `relation_type_targets`, `semantic_rules`.
- Grafo: `nodes`, `edges`.
- Corpus y gobierno: `essays`, `changesets`, `approvals`, `ontology_change_requests`.

## Identificadores

- Ensayo: `ESS-######`.
- ChangeSet: `CHG-######`.
- Nodos/aristas: prefijos estables por familia; no reciclar IDs.
- Los alias y deprecaciones se versionan; no se reutiliza un código retirado para otro significado.

## Procedencia

Toda arista material debe permitir reconstruir: ensayo/fuente, evidencia, contexto, versión ontológica, versión taxonómica, autor/proponente, revisor y fecha.

## Consultas de aceptación

El grafo debe responder las diez competency questions de `data/ontology.json`, especialmente controles por riesgo, evidencia de efectividad, autoridad de aceptación, autoridad de agentes, fuerzas evolutivas y relación con GM-24.

## Escalamiento

Mantener SQLite hasta que existan necesidades medidas de concurrencia, volumen, interoperabilidad RDF/OWL o razonamiento formal. La preferencia tecnológica no debe adelantarse a la validación del modelo conceptual.

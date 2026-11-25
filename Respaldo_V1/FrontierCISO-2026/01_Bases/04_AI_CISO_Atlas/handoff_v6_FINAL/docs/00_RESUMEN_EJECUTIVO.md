# 00 — Resumen ejecutivo

## Resultado final

AI CISO Atlas se compone de cinco capas que no deben confundirse:

1. **Taxonomía Atlas 5.3:** ubica conocimiento mediante X (territorio), Y (dominio), Z (función) y H (evolución).
2. **Core Ontology 1.0:** define qué entidades existen, qué significan y qué relaciones son válidas.
3. **Grafo compartido:** conserva instancias, relaciones, procedencia, contradicciones y versiones.
4. **Curator 6.0:** coordina cuatro skills, prepara sidecars y propone ChangeSets.
5. **TheNextCISO GM-24:** convierte conocimiento en competencias, actividades, resultados y evaluación.

## Fórmula conceptual

> La taxonomía ubica. La ontología da significado. El grafo conserva relaciones. El agente interpreta y propone. El validador verifica. La autoridad humana aprueba. TheNextCISO operacionaliza mediante aprendizaje.

## Baselines

| Componente | Baseline | Estado |
|---|---|---|
| Taxonomía | 5.3 | canónica para X/Y/Z/H |
| Ontología | 1.0.0 | propuesta, gobernada y extensible |
| Agente | Curator 6.0 | diseño recomendado |
| Skills | 4 | conservar; regenerar Graph Contributor |
| Persistencia | SQLite property graph | suficiente para MVP |
| Intercambio | JSON | contratos versionados |
| Documentación | Markdown | fuente humana y Git |

## Decisiones irrevocables salvo ADR nuevo

- No crear un quinto skill por ahora.
- No modificar 8 territorios, 24 dominios, 6 funciones, 32 subfunciones, 4 horizontes ni GM-24 por incorporar ontología.
- No adoptar RDF/OWL todavía.
- No permitir inferencias ni escrituras autónomas sobre el grafo aprobado.
- No convertir mapeos entre frameworks en equivalencias automáticas.
- No aplicar ChangeSets sin validación determinista y aprobación humana.

## Próxima prioridad

Regenerar `ai-ciso-atlas-graph-contributor` conforme a `config/skill_graph_contributor.md`, ejecutar tres ensayos piloto y congelar la baseline operativa después de revisar errores, ambigüedades y propuestas de extensión.

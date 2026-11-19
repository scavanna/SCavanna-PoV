# 01 — Arquitectura final

## Vista por capas

| Capa | Pregunta | Artefactos | Autoridad |
|---|---|---|---|
| Taxonomía | ¿Dónde pertenece? | X/Y/Z/H, sidecar de clasificación | `AICISO_5_3_01_Taxonomia.pdf` |
| Ontología | ¿Qué es y cómo puede relacionarse? | entidades, relaciones, reglas | Core Ontology 1.0 |
| Corpus | ¿Qué dice y con qué evidencia? | ensayos, fuentes, claims, evidencia | repositorio editorial |
| Grafo | ¿Qué instancias y relaciones fueron aprobadas? | nodos, aristas, procedencia | SQLite + ChangeSets |
| Agente | ¿Cómo se interpreta y propone? | instrucciones y cuatro skills | Curator 6.0 |
| Aprendizaje | ¿Qué competencia se desarrolla? | GM-24, outcomes, actividades | currículo TheNextCISO |

## Vistas del Atlas

- **StructuralAtlasView:** Territorio × Dominio × Función, con subfunciones editoriales y coordenadas secundarias justificadas.
- **EvolutionaryAtlasView:** Capacidad + Contexto + Horizonte + Fuerzas + Transiciones + Evidencia.
- Ambas vistas comparten IDs y grafo; no se duplican nodos conceptuales.
- H no es un cuarto eje geométrico equivalente: se visualiza con bandas, transiciones, bifurcaciones y fuerzas.

## Componentes técnicos

- Repositorio Git como registro de documentación, catálogos, sidecars y ChangeSets.
- JSON como intercambio y contratos.
- SQLite como catálogo ontológico y property graph del MVP.
- Python estándar para validación/carga/aplicación.
- Mermaid para diagramas mantenibles.

## Fronteras

- Taxonomía ≠ ontología ≠ grafo ≠ corpus.
- Territorio ≠ módulo ontológico.
- Horizonte ≠ madurez organizacional.
- Role ≠ Authority; Threat ≠ RiskScenario; Event ≠ Alert ≠ Incident; SecurityControl ≠ ControlObjective.
- Relación válida ≠ afirmación verdadera. La verdad material requiere evidencia y contexto.

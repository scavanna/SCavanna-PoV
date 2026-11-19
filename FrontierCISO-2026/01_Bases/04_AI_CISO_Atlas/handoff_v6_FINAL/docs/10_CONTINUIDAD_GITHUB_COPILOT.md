# 10 — Continuidad en otra sesión o GitHub Copilot

## Archivos que debe leer primero el asistente

1. `README.md`
2. `docs/00_RESUMEN_EJECUTIVO.md`
3. `docs/08_DECISIONES_ARQUITECTURALES.md`
4. `docs/05_MODELO_OPERACION.md`
5. `data/ontology.json`
6. `.github/copilot-instructions.md`

## Prompt de reinicio

> Trabajá sobre AI CISO Atlas con Taxonomy 5.3, Core Ontology 1.0.0 y Curator 6.0. La taxonomía clasifica X/Y/Z/H; la ontología define tipos y relaciones; el grafo conserva solo cambios aprobados. Respetá los ADR, no inventes códigos, no declares equivalencias automáticas y no apliques ChangeSets. Antes de proponer cambios, ejecutá las pruebas y citá el archivo y la versión que gobiernan cada decisión.

## Primeras tareas en GitHub

1. Crear repo privado y copiar el paquete.
2. Agregar las siete fuentes canónicas en una ubicación controlada o como referencias externas.
3. Ejecutar pruebas en CI.
4. Crear ramas: `main`, `develop`, `ontology/*`, `taxonomy/*`.
5. Proteger `main` y exigir revisión para catálogos, schemas y SQL.
6. Implementar Graph Contributor conforme al contrato.
7. Usar tres ensayos piloto y registrar issues por ambigüedad.

## Definition of Done para el piloto

- Catálogos y tests verdes.
- Sidecar cumple schema.
- ChangeSet cumple validación estructural y semántica.
- No hay escritura automática.
- Un revisor humano documentó decisión.
- Se puede reconstruir la procedencia de cada arista.

# 05 — Modelo de operación

## Flujo recomendado

1. Ingestar ensayo con ID `ESS-######` y checksum.
2. Clasificar X/Y/Z y justificar cada coordenada.
3. Analizar H solo cuando haya evidencia evolutiva.
4. Mapear GM-24 como candidato, no como competencia demostrada.
5. Extraer entidades y relaciones ontológicas.
6. Generar sidecar Markdown/JSON.
7. Generar ChangeSet `proposed`.
8. Validar esquema y semántica localmente.
9. Revisar duplicados, contradicciones, evidencia, contexto y extensiones.
10. Obtener decisión humana.
11. Aplicar con script local y registrar trazabilidad.
12. Ejecutar controles post-aplicación y exportar snapshot.

## Estados

`proposed → schema_validated → semantically_validated → reviewed → approved → applied`

Ramas terminales: `rejected`; una novedad válida puede originar `ontology_change_request` sin aplicarse al grafo.

## RACI mínimo

| Actividad | Agente | Validador | Curador humano | Aplicador local |
|---|---|---|---|---|
| Clasificar/extraer | R |  | A/C |  |
| Validar contrato |  | R | C |  |
| Juzgar evidencia | C | C | A/R |  |
| Aprobar |  |  | A/R |  |
| Aplicar |  | C | A | R |

## Controles

- Principio de mínima autoridad.
- Dry-run por defecto.
- Aprobación separada de generación.
- Trazabilidad de versión, fuente, actor y fecha.
- Backups/snapshots antes de migraciones.
- Reversión mediante ChangeSet compensatorio; no borrado ad hoc.

# Catálogos, respuesta y casos de uso

| Pregunta | Fuente de esta edición | Cobertura comprobada |
|---|---|---|
| ¿Cuáles son las categorías? | `fuentes/data/amenazas.csv` | 15 agrupadores. |
| ¿Cuáles son las amenazas? | `fuentes/data/magerit-v3-amenazas.csv` y `fuentes/data/extensiones-amenazas.csv` | 57 entradas del núcleo, incluidos dos comodines, + 22 extensiones no oficiales. |
| ¿Qué respuesta tiene cada categoría? | `fuentes/docs/09-estado-del-arte/01-categorias-15/` | 60 filas: I inventario, P prevención/protección, D detección, R respuesta/recuperación. |
| ¿Qué respuesta tiene cada amenaza? | `fuentes/docs/09-estado-del-arte/02-magerit-v3-ampliado/` | 316 filas: 4 fases distintas por cada uno de los 79 IDs. |
| ¿Qué controles y productos se contemplaron? | Subcarpeta `microsoft` y `03-capacidades-microsoft` | Mapeo por amenaza y catálogo transversal. Es una capacidad candidata; el control real requiere evidencia. |
| ¿Dónde están los casos de uso? | `fuentes/data/casos-uso.csv`, `fuentes/docs/03-casos-uso/` y `fuentes/docs/08-ejemplos/` | 16 actividades de método, más ejemplos contextuales. No consta un catálogo de 79 relaciones nominales con esos IDs; no se inventaron. |

`Cobertura_Fases_Verificada.csv` registra los 94 IDs verificados contra las hojas de ciclo, no una nueva lista de amenazas.

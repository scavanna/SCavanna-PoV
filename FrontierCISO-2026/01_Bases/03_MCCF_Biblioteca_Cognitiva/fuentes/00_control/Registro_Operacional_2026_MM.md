# Consolidación operacional 2026_MM

- Fecha UTC: 2026-11-11T16:02:31.548410+00:00
- Edición anterior: 2026-11-08 (conservada sin sobrescribir).
- Edición vigente versionada: 2026_MM_2026-11-11.

## Archivos

| Fase | Cantidad |
|---|---:|
| Corpus nuevo inventariado y hasheado | 675 |
| Duplicados por SHA-256 que permanecen en `Duplicados` | 104 |
| Duplicados por texto y activos embebidos que permanecen en `Duplicados` | 211 |
| Documentos únicos nuevos incorporados | 113 |
| Copias nuevas más recientes que sustituyeron un curado anterior | 6 |
| Copias nuevas más recientes que sustituyeron un excluido anterior | 10 |
| Archivos no seleccionados que permanecen en `2026_MM` | 241 |
| Total único actual en `Curado01` | 401 |

Inicialmente se detectaron 106 duplicados binarios, que no se extrajeron, y 219 por texto y activos embebidos. La regla de conservar el más reciente hizo que **dos** copias nuevas binarias y **ocho** textuales sustituyeran a diez archivos antiguos no relevantes; por eso los totales finales en `Duplicados` son 104 y 211. Las seis copias anteriores curadas sustituidas se conservaron en `Duplicados\2026_MM\reemplazados_por_version_reciente`. Las diez copias anteriores no relevantes sustituidas se conservaron en `Duplicados\2026_MM\reemplazados_excluidos`; su copia nueva más reciente quedó en `2026_MM`. El total nuevo se reconcilia como **241 + 104 + 211 + 119 = 675**. El umbral de duplicados cercanos fue 0,05 %; no aparecieron pares distintos del contenido exacto dentro de ese intervalo.

## Biblioteca consolidada

- Conceptos previos: **1.356**, con IDs y nombres conservados.
- Conceptos nuevos: **48**.
- Conceptos totales: **1404**.
- Etiquetas locales propuestas sin validación empírica: **11** (marcadas individualmente).
- 50 capítulos del libro nuevo revisados: 23 enlazados a conceptos existentes y 27 incorporados como conceptos distintos.
- 77 candidatos primarios y 153 residuales revisados para evitar omitir conceptos por el formato de los encabezados.
- Se conservaron definiciones anteriores salvo dos correcciones con texto antes/después, fundamento y localizador.

## Tratamiento de la evidencia

- Las coincidencias SHA reutilizaron la clasificación previa.
- Para texto igual se compararon también imágenes/embebidos; no se confundieron fuentes con texto idéntico y gráficos distintos.
- Las etiquetas propuestas en documentos no se presentan como efectos empíricos establecidos.
- Las prácticas CISO, ejercicios y criterios de evaluación son propuestas pedagógicas, no resultados demostrados.
- El PowerPoint `Mentalidad Consultiva MSL 202608.pptx` contiene una diapositiva OOXML vacía sin texto ni multimedia; la búsqueda WorkIQ no estuvo disponible y no se atribuyó contenido ajeno.

## Registros de auditoría

- `inventario_2026_MM.csv`: 675 rutas, hashes, destino y decisión.
- `plan_duplicados_sha256.csv` y `plan_duplicados_contenido.csv`.
- `auditoria_activos_embebidos.csv`: comparación de 225 candidatos.
- `revision_documental_2026_MM.csv`: 344 decisiones individuales.
- `decisiones_conceptuales_2026_MM.csv`: revisión semántica y fuentes.
- `revision_capitulos_50.jsonl`: crosswalk de capítulos-modelo.
- `Registro_Cambios_Definiciones_2026_MM.md`.
- `registro_cambios_conceptos.csv`: alias, bibliografía, definición y prioridad con procedencia.

## Reproducibilidad

La base versionada y los scripts están en la carpeta de estado de sesión `ai-ciso-curation\2026_MM_update`. La versión previa y sus informes se conservan; las salidas de esta edición se generaron primero localmente, validaron y luego publicaron.
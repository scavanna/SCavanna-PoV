# Control de calidad del consolidado 2026_MM

**Decisión:** Aprobado

## Comprobaciones

- [x] QC-001 — Inventario original y cobertura de decisiones: `"889 previos + 675 nuevos; 675 decisiones SHA, 569 comparaciones textuales y 344 revisiones individuales."`
- [x] QC-002 — Reconciliación física del lote 2026_MM: `{"2026_MM": 241, "Curado01_nuevos": 119, "Duplicados_nuevos": 315, "Antiguos_excluidos_archivados": 10}`
- [x] QC-003 — Diferencia máxima de contenido y copia más reciente: `{"pares_duplicados": 557, "umbral_superado": 0, "copia_conservada_mas_antigua": 0}`
- [x] QC-004 — Imágenes y adjuntos en duplicados por texto: `{"equivalent_text_and_assets": 225}`
- [x] QC-005 — Persistencia y trazabilidad SHA-256 de los 675 nuevos: `{"missing": [], "unexplained_hash_changes": [], "mip_protected_after_original_hash": 0, "unmodified_hashes": 675}`
- [x] QC-006 — Identidad histórica estable y nuevos conceptos: `{"historical_ids": 1356, "new_ids": 48, "changed_old_names_or_categories": []}`
- [x] QC-007 — Cambios en definiciones antes/después, fuente y justificación: `{"modified_historical_definitions": ["DP-0123", "MM-0141"], "source_tracked": ["DP-0123", "MM-0141"]}`
- [x] QC-008 — Definiciones, prioridades y evidencia del corpus curado: `{"unenriched": 0, "concepts_without_source": 0, "evidence_outside_curated": 0, "total_occurrences": 37106}`
- [x] QC-009 — Fichas nuevas completas y etiquetas provisionales visibles: `{"invalid_concepts": []}`
- [x] QC-010 — Revisión exhaustiva de libro y candidatos de concepto: `"77 candidatos primarios; 50 capítulos del libro; al menos 150 candidatos residuales."`
- [x] QC-011 — Todos los documentos del corpus tienen ruta final existente: `"1.696 registros (1.564 archivos principales + 132 de contexto), todos presentes."`
- [x] QC-012 — Markdown y Excel completos, legibles y sin fórmulas rotas: `{"markdown": 19, "workbooks": 16, "read_errors": [], "formula_cells": []}`
- [x] QC-013 — 1.200 horas exactas por módulos, actividades y cronograma: `{"modules": 12, "module_hours": 1200, "activity_hours": 1200, "block_hours": 1200, "videos_observed_unverified": 36}`
- [x] QC-014 — Núcleo CISO es subconjunto de la biblioteca general: `{"core_unique_concepts": 300, "curriculum_unique_concepts": 300, "P1_P2_missing_from_core": []}`
- [x] QC-015 — Manifiestos de auditoría publicados en staging: `{"inventory": 675, "review": 344, "changes": 394}`
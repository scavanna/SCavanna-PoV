# GitHub Copilot instructions — AI CISO Atlas

- Trate `docs/08_DECISIONES_ARQUITECTURALES.md` como ADR vigente.
- No cambie IDs, significados o conteos sin ADR y migración.
- Mantenga separadas taxonomía, ontología, corpus y grafo.
- Use `ontology_version: 1.0.0` y `taxonomy_version: 5.3`.
- No invente el catálogo de 32 subfunciones; consulte la fuente canónica.
- Todo cambio en `data/`, `schemas/` o `sql/` requiere tests.
- Los scripts deben ser dry-run por defecto; aplicar requiere `approved` + validación `passed`.
- No agregue inferencias transitivas, equivalencias o escrituras automáticas.
- Preserve procedencia, contexto, evidencia, contradicciones y revisión humana.
- Antes de cerrar un cambio ejecute `bash scripts/run_recommended_order.sh`.

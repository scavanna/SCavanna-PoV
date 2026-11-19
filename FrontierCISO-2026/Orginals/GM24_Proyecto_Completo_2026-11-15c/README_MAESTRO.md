# GM-24 · Paquete maestro del proyecto (2026-11-15, revisión b)

379 conceptos con pre-ensayo íntegro (plano A, V7.1) + 8 instancias de dominio (plano B: Productividad, XDR, Endpoints, Identidades, Datos, SIEM, Nube, Apps) · 206 tareas · 96 agentes · mapeo a 17 marcos.

- 01_Corpus_GM24_V7.1 — documentos GM-24 V7.1 + Anexo + Documento Maestro original, sub-plan 00–11, 99 pre-ensayos nuevos + 280 originales + lotes fuente, mapeo, informes, XLSX, HTML con todo embebido.
- 02_Dominios_PlanoB — 8 instancias, estrategia, comparativa, ChangeSet V7.1.
- 03_Fuentes_y_Generadores — build/ (fuente de verdad) + docs narrativos. Regenerar: `cd build && python make_all.py --docx`.
- 04_Insumos_Externos — Matrices_Curriculares, HC-040, Documento Maestro. Los 3 DOCX V4 están embebidos en build/fuentes_GM24/V4_docx y cacheados en build/fuentes_V4; los documentos GM-24 incluyen el texto V4 íntegro.
- MANIFEST_SHA256.txt — `sha256sum -c`.

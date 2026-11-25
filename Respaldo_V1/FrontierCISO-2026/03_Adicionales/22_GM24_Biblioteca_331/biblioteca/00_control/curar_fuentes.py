#!/usr/bin/env python3
"""Screen the AI-CISOMindSet tree and copy versioned GM24 evidence, never move sources."""

import csv
import hashlib
import json
import os
import re
import shutil
import unicodedata
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(r"C:\Users\scavanna\OneDrive - Microsoft\AI-CISOMindSet")
DEST = ROOT / "Curado02"
CONTROL = ROOT / "Biblioteca_GM24" / "00_control"
CURRENT = "thenextciso_2026"
ARCHIVE = "202511-01"
QUESTION_BASE = (
    "preguntas-clave-de-ciso-para-ia-y-2026-11-06/"
    "output/ai-ciso-atlas-preguntas"
)

# Explicitly approved source roles are deterministic; a new release must be reviewed
# before it is added to this registry.
CURRENT_SOURCES = {
    "TheNextCISO_GM-24_Documento_Maestro.md": ("01_noviembre_2026", "24 units; 240 baseline concepts; 51 titled Atlas proposals"),
    "TheNextCISO GM-24 — 40 conceptos híbridos y vinculantes.md": ("01_noviembre_2026", "40 cross-unit candidate bridges"),
    "TheNextCISO GM-24 — 40 conceptos híbridos y vinculantes (1).md": ("01_noviembre_2026", "Byte-identical later copy; deduplicate by SHA-256"),
    "TheNextCISO_GM24_Cierre_Lotes_06_y_08.md": ("01_noviembre_2026", "Editorial status and coverage of lots 06 and 08"),
    "TheNextCISO_GM-24_Matrices_Curriculares (2).xlsx": ("01_noviembre_2026", "Accessible November matrix; 240+51, baseline editorial"),
    "TheNextCISO_GM-24_Matrices_Curriculares.xlsx": ("03_apoyo_y_versiones", "Protected through WorkIQ; do not infer its internal differences"),
    "AI_CISO_Atlas_Ensayos_TheNextCISO_x_Core_Accountabilities_FY27_2026-11-05.xlsx": ("01_noviembre_2026", "331 pre-essay inventory, includes 40 candidates and 51 proposals"),
    "AI_CISO_Atlas_Pesos_Criterios_9_Distribuciones_2026-11-05.xlsx": ("03_apoyo_y_versiones", "Contextual proposed weights, not approved learning outcomes"),
    "AI_CISO_Atlas_Pesos_Criterios_9_Distribuciones_2026-11-05.pptx": ("03_apoyo_y_versiones", "Contextual explanation of proposed weights; not a new curriculum"),
    "Formación CISO_ Gobierno y Gestión (Estructura 24 Clases) 4.docx": ("03_apoyo_y_versiones", "Structural source: transition from 32 to 24 units"),
    "Formación CISO_ Gobierno y Gestión (Versión Actualizada) 4.docx": ("03_apoyo_y_versiones", "Historically updated 32-unit predecessor; not the GM24 baseline"),
    "Formación CISO_ Gobierno y Gestión_ 4.docx": ("03_apoyo_y_versiones", "Original 32-unit predecessor"),
}
ESSAY_FILES = [
    "TheNextCISO GM-24 — Ensayos base 001–030.md",
    "TheNextCISO GM-24 — Ensayos base 031–060.md",
    "TheNextCISO GM-24 — Ensayos base 061–090.md",
    "TheNextCISO GM-24 — Ensayos base 091–120.md",
    "TheNextCISO GM-24 — Ensayos base 121–150.md",
    "TheNextCISO_GM24_Ensayos_Bases_151-180.md",
    "TheNextCISO GM-24 — Ensayos base 181–210.md",
    "TheNextCISO_GM24_Ensayos_Bases_211-240.md",
]
for name in ESSAY_FILES:
    CURRENT_SOURCES[name] = ("01_noviembre_2026", "One of eight base-concept essay lots (30 ideas, not approved essays)")

HISTORICAL_SOURCES = {
    "UdeSA-2512/SI/The Next CISO - Curricula 202506 v3.docx": "Potential June 2025 foundational curriculum; title/date not an approval",
    "UdeSA-2512/SI/Programa Maestro_ Gobierno y Gestión de la Ciberseguridad - The Next CISO.docx": "Historical master, not the current 331-object corpus",
    "UdeSA-2512/SI/Formación CISO_ Gobierno y Gestión (Estructura 24 Clases).docx": "24-unit historical structure; compare to the 2026 edition",
    "UdeSA-2512/SI/Consolidación Programa Académico _The Next CISO_.md": "Historical synthesis, trace the 24-unit teaching structure",
    "UdeSA-2512/SI/Consolidación de Documentos de Ciberseguridad.md": "Historical source synthesis",
    "UdeSA-2512/NoDocs/Estructura Academica color - 20250604.xlsx": "Potential June 2025 structure; date is only in filename",
}
MAYEUTIC_SOURCES = {
    "fuentes/preguntas_consolidadas.json": "543 consolidated questions with provenance and direct links",
    "fuentes/corpus_preensayos.json": "639 records: 331 pre-existing entries and 308 question-derived propositions",
    "fuentes/corpus_ideas_centrales.json": "280 editorial ideas for baseline and HC, not for AMP proposals",
    "fuentes/taxonomia.json": "24 unit identifiers and eight maieutic question templates",
    "fuentes/LEEME.md": "Provenance and explicit limits of the question corpus",
    "README.md": "Documentation of question-building rules and counts",
}
SELECTION = {
    **{f"{CURRENT}/{name}": (kind, why) for name, (kind, why) in CURRENT_SOURCES.items()},
    **{f"{ARCHIVE}/{name}": ("04_historia_2025", why) for name, why in HISTORICAL_SOURCES.items()},
    **{
        f"{ARCHIVE}/{QUESTION_BASE}/{name}": ("02_metodo_mayeutico", why)
        for name, why in MAYEUTIC_SOURCES.items()
    },
}


def digest(path):
    hasher = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def slug(value):
    latin = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", latin.lower())).strip("-")[:78].rstrip("-")


def to_posix(path):
    return path.relative_to(ROOT).as_posix()


def inventory():
    selected = set(SELECTION)
    rows = []
    for folder, directories, filenames in os.walk(ROOT):
        directories[:] = sorted(
            name for name in directories
            if name not in ("Curado02", "Biblioteca_GM24", ".git", "__pycache__")
        )
        for name in sorted(filenames):
            path = Path(folder) / name
            if not path.is_file():
                continue
            relative = to_posix(path)
            stat = path.stat()
            top = relative.split("/", 1)[0]
            if relative in selected:
                status = "selected_for_curation"
                reason = SELECTION[relative][1]
            elif top == CURRENT and "Informe-CSU-Security" in name:
                status = "excluded_unrelated"
                reason = "Commercial report unrelated to GM24 concept definitions"
            elif top == CURRENT:
                status = "unreviewed_current"
                reason = "New current file: review and add to explicit source registry"
            elif top == ARCHIVE:
                status = "historical_not_selected"
                reason = "Historical corpus; retain in place (prior curation exists)"
            elif top in ("Curado01", "Biblioteca_CISO_Frontera", "Duplicados"):
                status = "existing_other_library"
                reason = "Existing curation or generated outputs; link, do not recopy"
            else:
                status = "other"
                reason = "Root-level context, not a GM24 curricular document"
            rows.append({
                "path": relative, "group": top, "extension": path.suffix.lower(),
                "bytes": stat.st_size,
                "modified_utc": datetime.fromtimestamp(stat.st_mtime, timezone.utc).isoformat(),
                "triage": status, "reason": reason,
            })
    return rows


def curate():
    for relative in SELECTION:
        if not (ROOT / Path(relative)).is_file():
            raise FileNotFoundError(f"Declared source is missing: {relative}")
    rows = inventory()
    CONTROL.mkdir(parents=True, exist_ok=True)
    audit = CONTROL / "Inventario_Raiz_GM24.csv"
    with audit.open("w", encoding="utf-8-sig", newline="") as output:
        writer = csv.DictWriter(output, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    candidates = []
    for relative, (group, why) in SELECTION.items():
        path = ROOT / Path(relative)
        stat = path.stat()
        candidates.append({
            "source": relative, "group": group, "purpose": why,
            "sha256": digest(path), "bytes": stat.st_size,
            "modified_utc": datetime.fromtimestamp(stat.st_mtime, timezone.utc).isoformat(),
            "mtime": stat.st_mtime,
        })
    digest_groups = {}
    for item in candidates:
        digest_groups.setdefault((item["sha256"], Path(item["source"]).suffix.lower()), []).append(item)

    manifest = []
    for items in digest_groups.values():
        preferred = max(
            items,
            key=lambda row: (
                row["source"].startswith(CURRENT + "/"),
                row["mtime"], row["source"],
            ),
        )
        base = Path(preferred["source"])
        filename = f"src-{slug(base.stem)}__{preferred['sha256'][:12]}{base.suffix.lower()}"
        destination = DEST / preferred["group"] / filename
        destination.parent.mkdir(parents=True, exist_ok=True)
        if destination.exists():
            if digest(destination) != preferred["sha256"]:
                raise ValueError(f"Previously curated file differs; refusing overwrite: {destination}")
        else:
            shutil.copy2(ROOT / Path(preferred["source"]), destination)
        if digest(destination) != preferred["sha256"]:
            raise ValueError(f"Curated copy checksum mismatch: {destination}")
        manifest.append({
            "curated_path": to_posix(destination),
            "canonical_source": preferred["source"],
            "other_identical_origins": [
                candidate["source"] for candidate in items if candidate is not preferred
            ],
            "sha256": preferred["sha256"],
            "bytes": preferred["bytes"],
            "purpose": preferred["purpose"],
            "status": "copy_byte_preserved",
            "interpretation_note": (
                "Word/Excel/PowerPoint cloud content interpreted via WorkIQ Ask when accessible; "
                "copies are not evidence of MIP usage rights or curricular approval."
                if base.suffix.lower() in (".docx", ".xlsx", ".pptx")
                else "Text file; manuscript status stated in source."
            ),
        })

    manifest.sort(key=lambda item: item["curated_path"])
    manifest_path = DEST / "00_control" / "Manifiesto_Curado02.json"
    previous = json.loads(manifest_path.read_text(encoding="utf-8")) if manifest_path.exists() else {}
    archived = {
        row["curated_path"]: row for row in previous.get("archived_versions", [])
    }
    active_paths = {row["curated_path"] for row in manifest}
    for row in previous.get("items", []):
        if row["curated_path"] not in active_paths:
            copy = ROOT / row["curated_path"]
            if not copy.is_file() or digest(copy) != row["sha256"]:
                raise ValueError(f"Previous version no longer matches manifest: {copy}")
            archived[row["curated_path"]] = {
                **row, "status": "superseded_source_version_copy_retained"
            }
    for active in active_paths:
        archived.pop(active, None)
    info = {
        "selection_policy": (
            "Explicit registry of GM24 2026, 2025 lineage, and maieutic texts. "
            "SHA-256 exact deduplication (never name-only), prefer current version "
            "then newest mtime for byte-identical copies. Filename = normalized "
            "original stem + first 12 hex of SHA-256; a changed file gets a new name. "
            "Previous source versions are kept in archived_versions, not deleted. "
            "No source is moved, renamed, decrypted or overwritten."
        ),
        "root": str(ROOT),
        "selection_inputs": len(candidates),
        "unique_copies": len(manifest),
        "identical_duplicates": len(candidates) - len(manifest),
        "root_screened_files": len(rows),
        "items": manifest,
        "archived_versions": sorted(
            archived.values(), key=lambda item: item["curated_path"]
        ),
    }
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(info, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (CONTROL / "Manifiesto_Curado02.json").write_text(
        json.dumps(info, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(
        f"Raíz examinada: {len(rows)} archivos; {len(candidates)} entradas seleccionadas, "
        f"{len(manifest)} copias únicas, {len(candidates)-len(manifest)} duplicados exactos.\n"
        f"Manifest: {manifest_path}"
    )


if __name__ == "__main__":
    curate()

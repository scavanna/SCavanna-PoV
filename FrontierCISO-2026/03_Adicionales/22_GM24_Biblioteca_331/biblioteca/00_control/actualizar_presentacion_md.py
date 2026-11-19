#!/usr/bin/env python3
"""Refresh generated Markdown prose only, preserving edited files and Excel data."""

import json
import re
from pathlib import Path

from gm24_model import LIBRARY, build_model
from publicar_biblioteca import STATE, build_text_files, json_records, sha256


MARKER = re.compile(r"<!-- generado-gm24 sha256:([a-f0-9]{64}) -->\n")


def main():
    if not STATE.exists():
        raise FileNotFoundError("La edición aún no está publicada")
    model = build_model()
    files = build_text_files(model)
    if len(files) != 670:
        raise ValueError(f"Se esperaban 670 Markdown, encontrados {len(files)}")
    for path, rows in json_records(model).items():
        expected = "\n".join(
            json.dumps(row, ensure_ascii=False, separators=(",", ":"), allow_nan=False)
            for row in rows
        ) + "\n"
        if not path.exists() or path.read_text(encoding="utf-8") != expected:
            raise ValueError(f"El modelo de datos ya no coincide con la edición: {path}")
    changes = []
    for path, replacement in files.items():
        if not path.exists():
            raise FileNotFoundError(f"Falta una ficha publicada: {path}")
        old = path.read_text(encoding="utf-8")
        match = MARKER.match(old)
        if not match or sha256(old[match.end():].encode("utf-8")) != match.group(1):
            raise ValueError(f"Ficha modificada manualmente; no sobrescribir: {path}")
        if old != replacement:
            changes.append((path, replacement))
    for path, replacement in changes:
        path.write_text(replacement, encoding="utf-8")
    state = json.loads(STATE.read_text(encoding="utf-8"))
    state["markdown_presentation_revision"] = 2
    state["markdown_refresh_count"] = len(changes)
    STATE.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Presentación Markdown actualizada: {len(changes)} de 670 fichas; Excel y JSONL intactos.")


if __name__ == "__main__":
    main()

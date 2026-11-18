import argparse
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def build_layer(rows, reference, mapping_version):
    vocabulary = reference["atlas"]["techniques"]
    counts = {}
    for row in rows:
        tid = row["TechniqueId"].strip()
        if tid not in vocabulary or tid in counts:
            raise ValueError(f"Técnica no vigente o duplicada: {tid!r}")
        count = int(row["Alerts"])
        if count <= 0:
            raise ValueError(f"El conteo debe ser positivo para {tid}")
        counts[tid] = count
    nav = reference["navigator"]
    return {
        "name": f"MDCAI v{mapping_version} – actividad vinculada",
        "versions": nav["versions"],
        "domain": nav["domain"],
        "description": f"ATLAS {reference['atlas']['version']}. Alertas distintas con vínculo directo propuesto. No indica cobertura ni técnicas ejecutadas con éxito.",
        "techniques": [
            {"techniqueID": tid, "enabled": True, "score": count, "comment": f"{count} alertas distintas"}
            for tid, count in sorted(counts.items())
        ],
    }


def main():
    parser = argparse.ArgumentParser(description="Convierte el CSV de kql\\12 a una capa para ATLAS Navigator.")
    parser.add_argument("counts_csv", type=Path)
    parser.add_argument("output_json", type=Path)
    args = parser.parse_args()
    ref = json.loads((ROOT / "data" / "reference.json").read_text(encoding="utf-8-sig"))
    policy = json.loads((ROOT / "data" / "policy.json").read_text(encoding="utf-8-sig"))
    try:
        with args.counts_csv.open(encoding="utf-8-sig", newline="") as stream:
            reader = csv.DictReader(stream)
            if not reader.fieldnames or not {"TechniqueId", "Alerts"}.issubset(reader.fieldnames):
                raise ValueError("Se necesitan las columnas TechniqueId y Alerts de la consulta 12.")
            layer = build_layer(reader, ref, policy["release"])
    except ValueError as exc:
        parser.error(str(exc))
    args.output_json.write_text(json.dumps(layer, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()

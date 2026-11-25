#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DB="${1:-$ROOT/graph/atlas.sqlite}"
mkdir -p "$(dirname "$DB")"
python3 "$ROOT/scripts/validate_catalogs.py"
python3 "$ROOT/scripts/load_ontology.py" "$DB"
python3 "$ROOT/scripts/validate_changeset.py" "$ROOT/examples/example.changeset.json"
python3 -m unittest discover -s "$ROOT/tests" -p 'test_*.py'
echo "Pipeline baseline completed. No ChangeSet was applied."

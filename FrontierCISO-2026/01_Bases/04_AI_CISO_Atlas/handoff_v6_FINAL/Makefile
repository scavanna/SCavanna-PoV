.PHONY: validate test init
validate:
	python3 scripts/validate_catalogs.py
	python3 scripts/validate_changeset.py examples/example.changeset.json

test:
	python3 -m unittest discover -s tests -p 'test_*.py'

init:
	mkdir -p graph
	python3 scripts/load_ontology.py graph/atlas.sqlite

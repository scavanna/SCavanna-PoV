-- Frontier CISO Atlas · esquema del grafo de propiedades sobre SQLite (catálogo ontológico + grafo + gobierno)
-- El catálogo se carga antes que el grafo. En la base CANDIDATA todos los nodos y aristas tienen status = 'candidate'.
CREATE TABLE ontology_versions (version TEXT PRIMARY KEY, name TEXT, status TEXT, taxonomy_version TEXT, date TEXT);
CREATE TABLE entity_types (id TEXT PRIMARY KEY, name TEXT UNIQUE NOT NULL, module TEXT NOT NULL, definition TEXT, since TEXT);
CREATE TABLE relation_types (id TEXT PRIMARY KEY, name TEXT UNIQUE NOT NULL, family TEXT, definition TEXT, requires_evidence INTEGER, requires_context INTEGER, since TEXT);
CREATE TABLE relation_type_sources (relation TEXT NOT NULL REFERENCES relation_types(name), entity_type TEXT NOT NULL REFERENCES entity_types(name), PRIMARY KEY (relation, entity_type));
CREATE TABLE relation_type_targets (relation TEXT NOT NULL REFERENCES relation_types(name), entity_type TEXT NOT NULL REFERENCES entity_types(name), PRIMARY KEY (relation, entity_type));
CREATE TABLE relation_type_pairs (relation TEXT NOT NULL REFERENCES relation_types(name), source_type TEXT NOT NULL, target_type TEXT NOT NULL, PRIMARY KEY (relation, source_type, target_type));
CREATE TABLE semantic_rules (id TEXT PRIMARY KEY, level TEXT, name TEXT, description TEXT, severity TEXT);
CREATE TABLE nodes (id TEXT PRIMARY KEY, type TEXT NOT NULL REFERENCES entity_types(name), label TEXT NOT NULL, definition TEXT, properties TEXT, provenance TEXT, version TEXT, status TEXT NOT NULL, edition TEXT, changeset_id TEXT);
CREATE TABLE edges (id INTEGER PRIMARY KEY AUTOINCREMENT, edge_key TEXT UNIQUE, source TEXT NOT NULL REFERENCES nodes(id), target TEXT NOT NULL REFERENCES nodes(id), type TEXT NOT NULL REFERENCES relation_types(name), properties TEXT, evidence TEXT, context TEXT, version TEXT, status TEXT NOT NULL, changeset_id TEXT);
CREATE TABLE essays (essay_id TEXT PRIMARY KEY, title TEXT, version TEXT, path TEXT, sha256 TEXT, precursor_id TEXT, status TEXT);
CREATE TABLE changesets (changeset_id TEXT PRIMARY KEY, title TEXT, status TEXT, ontology_version TEXT, taxonomy_version TEXT, nodes INTEGER, edges INTEGER, semantic_validation TEXT);
CREATE TABLE approvals (changeset_id TEXT REFERENCES changesets(changeset_id), approver TEXT, decision TEXT, date TEXT, note TEXT);
CREATE TABLE ontology_change_requests (request_id TEXT PRIMARY KEY, title TEXT, status TEXT, date TEXT, note TEXT);
CREATE INDEX ix_edges_source ON edges(source); CREATE INDEX ix_edges_target ON edges(target); CREATE INDEX ix_edges_type ON edges(type); CREATE INDEX ix_nodes_type ON nodes(type);

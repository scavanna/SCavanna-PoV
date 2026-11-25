PRAGMA foreign_keys = ON;
CREATE TABLE IF NOT EXISTS ontology_versions (
  version TEXT PRIMARY KEY, status TEXT NOT NULL, created_at TEXT NOT NULL,
  effective_from TEXT, effective_to TEXT, notes TEXT
);
CREATE TABLE IF NOT EXISTS entity_types (
  name TEXT PRIMARY KEY, entity_id TEXT UNIQUE NOT NULL, module TEXT NOT NULL,
  definition TEXT NOT NULL, status TEXT NOT NULL, ontology_version TEXT NOT NULL,
  FOREIGN KEY (ontology_version) REFERENCES ontology_versions(version)
);
CREATE TABLE IF NOT EXISTS relation_types (
  name TEXT PRIMARY KEY, relation_id TEXT UNIQUE NOT NULL, family TEXT NOT NULL,
  definition TEXT NOT NULL, directed INTEGER NOT NULL CHECK(directed IN (0,1)),
  requires_evidence INTEGER NOT NULL CHECK(requires_evidence IN (0,1)),
  requires_context INTEGER NOT NULL CHECK(requires_context IN (0,1)),
  ontology_version TEXT NOT NULL,
  FOREIGN KEY (ontology_version) REFERENCES ontology_versions(version)
);
CREATE TABLE IF NOT EXISTS relation_type_sources (
  relation_name TEXT NOT NULL, entity_type TEXT NOT NULL,
  PRIMARY KEY (relation_name, entity_type),
  FOREIGN KEY (relation_name) REFERENCES relation_types(name),
  FOREIGN KEY (entity_type) REFERENCES entity_types(name)
);
CREATE TABLE IF NOT EXISTS relation_type_targets (
  relation_name TEXT NOT NULL, entity_type TEXT NOT NULL,
  PRIMARY KEY (relation_name, entity_type),
  FOREIGN KEY (relation_name) REFERENCES relation_types(name),
  FOREIGN KEY (entity_type) REFERENCES entity_types(name)
);
CREATE TABLE IF NOT EXISTS semantic_rules (
  rule_id TEXT PRIMARY KEY, level TEXT NOT NULL, name TEXT NOT NULL,
  description TEXT NOT NULL, severity TEXT NOT NULL, ontology_version TEXT NOT NULL,
  FOREIGN KEY (ontology_version) REFERENCES ontology_versions(version)
);

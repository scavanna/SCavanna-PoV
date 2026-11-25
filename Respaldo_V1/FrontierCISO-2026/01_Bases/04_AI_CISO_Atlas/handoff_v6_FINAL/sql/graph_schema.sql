PRAGMA foreign_keys = ON;
CREATE TABLE IF NOT EXISTS nodes (
  node_id TEXT PRIMARY KEY, node_type TEXT NOT NULL, name TEXT NOT NULL,
  description TEXT NOT NULL, version TEXT NOT NULL, review_status TEXT NOT NULL,
  context_json TEXT, provenance_json TEXT NOT NULL, created_at TEXT NOT NULL, updated_at TEXT NOT NULL,
  FOREIGN KEY (node_type) REFERENCES entity_types(name)
);
CREATE TABLE IF NOT EXISTS edges (
  edge_id TEXT PRIMARY KEY, source_id TEXT NOT NULL, relation_type TEXT NOT NULL,
  target_id TEXT NOT NULL, evidence_json TEXT, context_json TEXT, review_status TEXT NOT NULL,
  version TEXT NOT NULL, created_at TEXT NOT NULL, updated_at TEXT NOT NULL,
  FOREIGN KEY (source_id) REFERENCES nodes(node_id), FOREIGN KEY (target_id) REFERENCES nodes(node_id),
  FOREIGN KEY (relation_type) REFERENCES relation_types(name)
);
CREATE TABLE IF NOT EXISTS essays (
  essay_id TEXT PRIMARY KEY, title TEXT NOT NULL, content_path TEXT NOT NULL, checksum TEXT,
  review_status TEXT NOT NULL, created_at TEXT NOT NULL, updated_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS changesets (
  changeset_id TEXT PRIMARY KEY, essay_id TEXT NOT NULL, status TEXT NOT NULL,
  ontology_version TEXT NOT NULL, taxonomy_version TEXT NOT NULL, payload_json TEXT NOT NULL,
  validation_json TEXT NOT NULL, created_at TEXT NOT NULL, applied_at TEXT,
  FOREIGN KEY (essay_id) REFERENCES essays(essay_id)
);
CREATE TABLE IF NOT EXISTS approvals (
  approval_id INTEGER PRIMARY KEY AUTOINCREMENT, changeset_id TEXT NOT NULL,
  decision TEXT NOT NULL, approved_by TEXT NOT NULL, approved_at TEXT NOT NULL, notes TEXT,
  FOREIGN KEY (changeset_id) REFERENCES changesets(changeset_id)
);
CREATE TABLE IF NOT EXISTS ontology_change_requests (
  request_id TEXT PRIMARY KEY, proposed_kind TEXT NOT NULL, proposed_name TEXT NOT NULL,
  rationale TEXT NOT NULL, evidence_json TEXT, status TEXT NOT NULL, created_at TEXT NOT NULL,
  reviewed_by TEXT, reviewed_at TEXT
);
CREATE INDEX IF NOT EXISTS idx_edges_source ON edges(source_id);
CREATE INDEX IF NOT EXISTS idx_edges_target ON edges(target_id);
CREATE INDEX IF NOT EXISTS idx_edges_type ON edges(relation_type);

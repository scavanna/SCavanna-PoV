#!/usr/bin/env python3
import json, sqlite3, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def main(db_path):
    con=sqlite3.connect(db_path); con.execute('PRAGMA foreign_keys=ON')
    con.executescript((ROOT/'sql/ontology_sqlite.sql').read_text())
    con.executescript((ROOT/'sql/graph_schema.sql').read_text())
    ents=json.loads((ROOT/'data/entity_dictionary.json').read_text())['entities']
    rels=json.loads((ROOT/'data/relationship_dictionary.json').read_text())['relationships']
    rules=json.loads((ROOT/'data/semantic_rules.json').read_text())['rules']
    con.execute("INSERT OR REPLACE INTO ontology_versions(version,status,created_at,notes) VALUES(?,?,datetime('now'),?)",('1.0.0','proposed','Core Ontology v1.0 baseline'))
    for e in ents:
        con.execute('INSERT OR REPLACE INTO entity_types(name,entity_id,module,definition,status,ontology_version) VALUES(?,?,?,?,?,?)',(e['name'],e['id'],e['module'],e['definition'],e['status'],'1.0.0'))
    for r in rels:
        con.execute('INSERT OR REPLACE INTO relation_types(name,relation_id,family,definition,directed,requires_evidence,requires_context,ontology_version) VALUES(?,?,?,?,?,?,?,?)',(r['name'],r['id'],r['family'],r['definition'],int(r['directed']),int(r['requires_evidence']),int(r['requires_context']),'1.0.0'))
        con.execute('DELETE FROM relation_type_sources WHERE relation_name=?',(r['name'],)); con.execute('DELETE FROM relation_type_targets WHERE relation_name=?',(r['name'],))
        con.executemany('INSERT INTO relation_type_sources VALUES(?,?)',[(r['name'],x) for x in r['source_types']])
        con.executemany('INSERT INTO relation_type_targets VALUES(?,?)',[(r['name'],x) for x in r['target_types']])
    for x in rules:
        con.execute('INSERT OR REPLACE INTO semantic_rules VALUES(?,?,?,?,?,?)',(x['id'],x['level'],x['name'],x['description'],x['severity'],'1.0.0'))
    con.commit()
    print(f'Loaded {len(ents)} entity types, {len(rels)} relation types, {len(rules)} rules into {db_path}')
if __name__=='__main__': main(sys.argv[1] if len(sys.argv)>1 else str(ROOT/'graph/atlas.sqlite'))

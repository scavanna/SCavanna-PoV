#!/usr/bin/env python3
import json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
REQUIRED={'changeset_id','schema_version','ontology_version','taxonomy_version','essay_id','status','operations','semantic_validation','provenance'}
def main(path):
    cs=json.loads(Path(path).read_text()); errors=[]; warnings=[]
    missing=REQUIRED-set(cs); errors += [f'SV-003 missing field: {x}' for x in sorted(missing)]
    if cs.get('ontology_version')!='1.0.0': errors.append('SV-006 ontology_version must be 1.0.0')
    if cs.get('taxonomy_version')!='5.3': errors.append('SV-006 taxonomy_version must be 5.3')
    entities={x['name'] for x in json.loads((ROOT/'data/entity_dictionary.json').read_text())['entities']}
    rels={x['name']:x for x in json.loads((ROOT/'data/relationship_dictionary.json').read_text())['relationships']}
    nodes={}
    for op in cs.get('operations',[]):
        if op.get('operation')=='add_node':
            n=op.get('node',{}); typ=n.get('type')
            if typ not in entities: errors.append(f"SV-002 unknown type: {typ}")
            for k in ['id','type','name','description','version','review_status']:
                if k not in n: errors.append(f"SV-003 node missing {k}")
            if n.get('id'): nodes[n['id']]=typ
    for op in cs.get('operations',[]):
        if op.get('operation')=='add_edge':
            ed=op.get('edge',{}); rel=rels.get(ed.get('relation'))
            if not rel: errors.append(f"SV-002 unknown relation: {ed.get('relation')}"); continue
            st=ed.get('source_type') or nodes.get(ed.get('source')); tt=ed.get('target_type') or nodes.get(ed.get('target'))
            if st not in rel['source_types']: errors.append(f"SV-101 {rel['name']} rejects source type {st}")
            if tt not in rel['target_types']: errors.append(f"SV-102 {rel['name']} rejects target type {tt}")
            if rel['requires_evidence'] and not ed.get('evidence'): errors.append(f"SV-105 {rel['name']} requires evidence")
            if rel['requires_context'] and not ed.get('context'): errors.append(f"SV-106 {rel['name']} requires context")
    print(json.dumps({'valid':not errors,'violations':errors,'warnings':warnings},ensure_ascii=False,indent=2))
    return 0 if not errors else 1
if __name__=='__main__': raise SystemExit(main(sys.argv[1]))

#!/usr/bin/env python3
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def load(p): return json.loads((ROOT/p).read_text())
def main():
    e=load('data/entity_dictionary.json'); r=load('data/relationship_dictionary.json'); s=load('data/semantic_rules.json'); t=load('data/taxonomy_v5_3_structure.json')
    assert e['count']==57==len(e['entities'])
    assert r['count']==58==len(r['relationships'])
    assert s['count']==21==len(s['rules'])
    names={x['name'] for x in e['entities']}; assert len(names)==57
    for rel in r['relationships']:
        assert set(rel['source_types'])<=names, rel['name']
        assert set(rel['target_types'])<=names, rel['name']
    assert len(t['territories'])==8 and len(t['domains'])==24 and len(t['functions'])==6
    assert len(t['evolution']['horizons'])==4
    print('Catalog validation: PASS')
    print('Notice: v5.3 authoritative 32-subfunction catalog is intentionally not duplicated; sync from AICISO_5_3_01_Taxonomia.pdf.')
if __name__=='__main__': main()

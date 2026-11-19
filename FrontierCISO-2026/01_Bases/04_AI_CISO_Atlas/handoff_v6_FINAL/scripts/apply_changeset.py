#!/usr/bin/env python3
"""Safe MVP applicator. Dry-run by default; --apply requires approved + passed."""
import argparse,json,sqlite3,datetime
from pathlib import Path
def main():
 p=argparse.ArgumentParser(); p.add_argument('changeset'); p.add_argument('database'); p.add_argument('--apply',action='store_true'); a=p.parse_args()
 cs=json.loads(Path(a.changeset).read_text())
 if not a.apply:
  print(json.dumps({'dry_run':True,'changeset_id':cs.get('changeset_id'),'operations':len(cs.get('operations',[]))},indent=2)); return
 if cs.get('status')!='approved' or cs.get('semantic_validation',{}).get('status')!='passed':
  raise SystemExit('Refused: status must be approved and semantic_validation.status must be passed')
 con=sqlite3.connect(a.database); con.execute('PRAGMA foreign_keys=ON'); now=datetime.datetime.now(datetime.timezone.utc).isoformat()
 with con:
  for op in cs['operations']:
   if op['operation']=='add_node':
    n=op['node']; con.execute('INSERT INTO nodes VALUES(?,?,?,?,?,?,?,?,?,?)',(n['id'],n['type'],n['name'],n['description'],n['version'],n['review_status'],json.dumps(n.get('context')),json.dumps(n.get('provenance',{})),now,now))
   elif op['operation']=='add_edge':
    e=op['edge']; con.execute('INSERT INTO edges VALUES(?,?,?,?,?,?,?,?,?,?)',(e['id'],e['source'],e['relation'],e['target'],json.dumps(e.get('evidence')),json.dumps(e.get('context')),e.get('review_status','approved'),e.get('version','1.0.0'),now,now))
 print(f"Applied {cs['changeset_id']}")
if __name__=='__main__': main()

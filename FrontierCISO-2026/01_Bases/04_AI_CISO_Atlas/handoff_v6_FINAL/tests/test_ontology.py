import json,subprocess,sys,tempfile,unittest,sqlite3
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class TestOntology(unittest.TestCase):
 def test_counts(self):
  self.assertEqual(json.loads((ROOT/'data/entity_dictionary.json').read_text())['count'],57)
  self.assertEqual(json.loads((ROOT/'data/relationship_dictionary.json').read_text())['count'],58)
  self.assertEqual(json.loads((ROOT/'data/semantic_rules.json').read_text())['count'],21)
 def test_catalogs(self): subprocess.run([sys.executable,str(ROOT/'scripts/validate_catalogs.py')],check=True)
 def test_valid_changeset(self): subprocess.run([sys.executable,str(ROOT/'scripts/validate_changeset.py'),str(ROOT/'examples/example.changeset.json')],check=True)
 def test_invalid_changeset(self):
  p=subprocess.run([sys.executable,str(ROOT/'scripts/validate_changeset.py'),str(ROOT/'examples/example.invalid.changeset.json')]); self.assertNotEqual(p.returncode,0)
 def test_sql_load(self):
  with tempfile.NamedTemporaryFile(suffix='.sqlite') as f:
   subprocess.run([sys.executable,str(ROOT/'scripts/load_ontology.py'),f.name],check=True)
   con=sqlite3.connect(f.name); self.assertEqual(con.execute('select count(*) from entity_types').fetchone()[0],57); self.assertEqual(con.execute('select count(*) from relation_types').fetchone()[0],58)
if __name__=='__main__': unittest.main()

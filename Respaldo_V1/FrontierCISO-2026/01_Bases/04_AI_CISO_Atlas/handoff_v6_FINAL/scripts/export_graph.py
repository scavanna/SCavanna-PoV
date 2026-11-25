#!/usr/bin/env python3
import sqlite3,json,sys
con=sqlite3.connect(sys.argv[1]); con.row_factory=sqlite3.Row
out={'nodes':[dict(x) for x in con.execute('select * from nodes')],'edges':[dict(x) for x in con.execute('select * from edges')]}
print(json.dumps(out,ensure_ascii=False,indent=2))

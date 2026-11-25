# -*- coding: utf-8 -*-
"""Compara la primera lectura a ciegas con la coordenada vigente (versión 1.2) y arma los lotes de la segunda lectura.
Segunda lectura: todos los que difieren en algún eje, toda la serie APX y una muestra de control de los que coinciden en los tres ejes."""
import json, os, sys, random, collections, glob
B=os.path.dirname(os.path.abspath(__file__)); V12=os.path.join(B,'..','scripts','datos_de_trabajo','v12')
sys.path.insert(0,B); import preparar as PR
EJES=('territorio','dominio','subfuncion')
def vigente():
    v={}
    for p in json.load(open(V12+'/corpus_frontier_739.json',encoding='utf-8'))['preensayos']:
        f=p['fca']; v[p['id']]={'territorio':f['x']['primario'],'dominio':f['y']['primario'],'subfuncion':f['z']['subfuncion'],'serie':p['clase'],'mccs':f['mccs']}
    for p in json.load(open(V12+'/ampliacion_celdas_en_blanco.json',encoding='utf-8'))['preensayos']:
        f=p['fca']; v[p['id']]={'territorio':f['x']['primario'],'dominio':f['y']['primario'],'subfuncion':f['z']['subfuncion'],'serie':'APX','mccs':f['mccs']}
    return v
def lecturas(carpeta):
    o={}
    for p in sorted(glob.glob(os.path.join(B,carpeta,'salida_*.jsonl'))):
        for l in open(p,encoding='utf-8'):
            if l.strip():
                try: x=json.loads(l)
                except Exception: continue
                if x.get('id'): o[x['id']]=x
    return o
if __name__=='__main__':
    V=vigente(); R1=lecturas('salidas'); assert len(V)==755
    falt=[i for i in V if i not in R1]
    print('primera lectura:',len(R1),'de',len(V),'| faltan',len(falt))
    if falt and '--parcial' not in sys.argv: sys.exit('faltan lecturas; use --parcial para probar')
    dif={i:[e for e in EJES if R1[i].get(e)!=V[i][e]] for i in R1 if i in V}
    n=len(dif); 
    for e in EJES: print(f'  coincide en {e}:',sum(1 for i in dif if e not in dif[i]),'de',n)
    print('  coincide en los tres ejes:',sum(1 for i in dif if not dif[i]),'| difiere en alguno:',sum(1 for i in dif if dif[i]))
    if '--parcial' in sys.argv: sys.exit(0)
    difieren=sorted(i for i in dif if dif[i]); apx=sorted(i for i in V if V[i]['serie']=='APX')
    iguales=sorted(i for i in dif if not dif[i] and V[i]['serie']!='APX')
    control=sorted(random.Random(20261116).sample(iguales,min(40,len(iguales))))
    segunda=sorted(set(difieren)|set(apx)|set(control))
    RG={r['id']:r for r in json.load(open(B+'/registros_a_ciegas.json',encoding='utf-8'))}
    nl=max(1,round(len(segunda)/40)); tam=PR.lotes([RG[i] for i in segunda],nl,20261117,'lotes2')
    json.dump({'difieren':difieren,'apx':apx,'control':control,'segunda_lectura':segunda,'lotes':tam},open(B+'/segunda_lectura.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
    for k in range(1,nl+1):
        nn=f'{k:02d}'
        open(f'{B}/lotes2/DESPACHO_{nn}.md','w',encoding='utf-8').write(f"# Despacho · lote {nn} (segunda lectura)\n\nCarpeta de trabajo: `{B}/`\n\n1. Leé `{B}/ENCARGO.md` y seguilo.\n2. Reglas: `{B}/REGLAS.md`.\n3. Tu lote: `{B}/lotes2/lote_{nn}.jsonl`.\n4. Tu salida: `{B}/salidas2/salida_{nn}.jsonl` (una línea por pre-ensayo; agregá líneas cada 8).\n5. Validador: `cd {B} && python3 validar.py lotes2 salidas2 {nn}`.\n6. Cierre: `{B}/salidas2/cierre_{nn}.md`.\n\nNo abras ningún otro archivo ni carpeta. En particular, no abras `{B}/salidas/` ni `{B}/lotes/`.\n")
    print('segunda lectura:',len(segunda),'=',len(difieren),'que difieren +',len(set(apx)-set(difieren)),'APX que coinciden +',len(control),'de control | lotes',tam)

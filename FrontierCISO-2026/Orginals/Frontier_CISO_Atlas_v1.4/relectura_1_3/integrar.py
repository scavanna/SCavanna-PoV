# -*- coding: utf-8 -*-
"""Integra las dos lecturas a ciegas con la coordenada vigente (versión 1.2) y decide, eje por eje, qué cambia.
Regla (ADR-028 y ADR-030): un eje cambia cuando las dos lecturas coinciden entre sí y difieren del valor vigente, salvo que alguna lectura haya anotado
una pregunta abierta que afecta a ese eje, que alguna haya declarado confianza baja o que el cambio caiga en un punto que la revisión de la versión candidata dejó abierto.
En cualquier otro caso el valor queda como estaba y el caso se informa con las dos lecturas.
Uso: python3 integrar.py            escribe los ajustes de la versión 1.3
     python3 integrar.py --sin-revision   muestra, sin escribir, la integración anterior a la revisión de la versión candidata
     python3 integrar.py --prueba   ensayo con lo que haya de la primera lectura, tomando la segunda igual a la primera; no escribe nada
     python3 integrar.py --ensayo   escribe un archivo de ajustes de ENSAYO (segunda lectura = primera en los registros de la segunda lectura), marcado «ensayo»,
                                    para ejercitar la cadena antes de tener la segunda lectura. El empaquetado se niega a publicar un archivo de ensayo."""
import json, os, sys, collections, glob
B=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,B)
import comparar as CP, reglas13 as R
EJES=CP.EJES; SEC={'territorio':'territorios_sec','dominio':'dominios_sec','subfuncion':'subfunciones_sec'}; RG={'territorio':'reglas_territorio','dominio':'reglas_dominio','subfuncion':'reglas_subfuncion'}
EJE_ABIERTA={k:('subfuncion' if v[0]=='subfunción' else v[0]) for k,v in R.ABIERTAS_DE_CASO.items()}
# Enunciados que dicen cómo leer y no deciden una coordenada: no cuentan como «regla adoptada citada»
METODO={'RP-10.2','RP-10.4'}
# Decisiones tomadas el 16-nov-2026 con la primera lectura incompleta y antes de existir la segunda (para no ajustarlas al resultado):
#  1) un cambio no entra si alguna de las dos lecturas declaró confianza baja; el caso se informa al autor. Es más estricto que ADR-028.
#  2) los lectores no citan las reglas de modo uniforme: «regla adoptada citada» es un indicio, no una atribución.
SIN_REVISION='--sin-revision' in sys.argv      # reproduce la integración anterior a la revisión de la versión candidata
def decidir(V,R1,R2,ids):
    filas=[]
    for i in ids:
        v=V[i]; a=R1.get(i); b=R2.get(i)
        for e in EJES:
            f={'id':i,'serie':v['serie'],'eje':e,'vigente':v[e],'lectura_1':a and a.get(e),'lectura_2':b and b.get(e)}
            ab=sorted({q for x in (a,b) if x for q in x.get('abiertas',[]) if EJE_ABIERTA.get(q)==e})
            rp=sorted({q for x in (a,b) if x for q in x.get(RG[e],[]) if q.startswith('RP-') and q not in METODO})
            f.update({'preguntas_abiertas':ab,'reglas_adoptadas_citadas':rp,'confianzas':[x.get('confianza') for x in (a,b) if x]})
            if a is None: f['resultado']='sin lectura'
            elif a.get(e)==v[e] and (b is None or b.get(e)==v[e]): f['resultado']='coincide con la vigente' if b is None else 'dos lecturas coinciden con la vigente'
            elif b is None: f['resultado']='la primera lectura difiere y no hay segunda'
            elif a.get(e)==b.get(e)!=v[e]: f['resultado']='frenado por una pregunta abierta' if ab else ('coinciden, pero una lectura declaró confianza baja' if 'baja' in (a.get('confianza'),b.get('confianza')) else 'cambia')
            elif a.get(e)==v[e] or b.get(e)==v[e]: f['resultado']='una lectura difiere y la otra sostiene la vigente'
            else: f['resultado']='sin coincidencia: las dos difieren de la vigente y entre sí'
            if f['resultado'].startswith('frenado por una pregunta abierta') and 'baja' in (a.get('confianza'),b.get('confianza')): f['ademas']='una lectura declaró confianza baja'
            if f['resultado']=='cambia' and not SIN_REVISION:
                # después de la revisión de la versión candidata: un cambio que cae en un punto que esa revisión dejó abierto no se aplica
                _p=R.punto_de_la_revision(e,v[e],a.get(e),(v['dominio'],a.get('dominio'),b.get('dominio')),tuple(a.get('reglas_subfuncion') or [])+tuple(b.get('reglas_subfuncion') or []),v['serie'])
                if _p: f['resultado']='frenado por la revisión de la versión candidata'; f['punto_de_la_revision']=_p
            if f['resultado']=='cambia':
                f['origen']='relectura 1.3: dos lecturas a ciegas coinciden'  # una sola etiqueta; las reglas que citan las lecturas van en reglas_adoptadas_citadas
                f['motivo']=' / '.join(x.get('motivo','') for x in (a,b))
            filas.append(f)
    return filas
if __name__=='__main__':
    prueba='--prueba' in sys.argv; ensayo='--ensayo' in sys.argv
    V=CP.vigente(); R1=CP.lecturas('salidas'); R2=dict(R1) if prueba else CP.lecturas('salidas2')
    if ensayo:
        _seg=json.load(open(B+'/segunda_lectura.json',encoding='utf-8'))['segunda_lectura']; R2={i:R1[i] for i in _seg}
    ids=sorted(i for i in V if i in R1) if prueba else sorted(V)
    if not prueba:
        seg=json.load(open(B+'/segunda_lectura.json',encoding='utf-8'))
        f1=[i for i in V if i not in R1]; f2=[i for i in seg['segunda_lectura'] if i not in R2]
        if f1 or f2: sys.exit(f'faltan lecturas: primera {len(f1)}, segunda {len(f2)}')
        sin2=[i for i in V if any(R1[i][e]!=V[i][e] for e in EJES) and i not in R2]
        if sin2: sys.exit('hay pre-ensayos en que la primera lectura difiere y que no tienen segunda lectura: '+', '.join(sin2))
    F=decidir(V,R1,R2,ids)
    c=collections.Counter((f['eje'],f['resultado']) for f in F)
    print('pre-ensayos:',len(ids),'| filas:',len(F),'(ENSAYO: segunda lectura = primera)' if prueba else '')
    for e in EJES: print(' ',e,{k[1]:n for k,n in sorted(c.items()) if k[0]==e})
    cam=[f for f in F if f['resultado']=='cambia']
    print('  cambian:',len(cam),'ejes en',len({f['id'] for f in cam}),'pre-ensayos | con regla adoptada citada:',sum(1 for f in cam if f['reglas_adoptadas_citadas']),'| frenados:',sum(1 for f in F if f['resultado'].startswith('frenado')))
    print('  frenados por la revisión:',dict(collections.Counter(f.get('punto_de_la_revision') for f in F if f.get('punto_de_la_revision'))))
    if prueba or SIN_REVISION: sys.exit(0)
    corpus=[{'id':f['id'],'campo':f['eje'],'valor':f['lectura_1'],'origen':f['origen'],'motivo':f['motivo'],'reglas':f['reglas_adoptadas_citadas'],'confianzas':f['confianzas']} for f in cam if f['serie']!='APX']
    apx=[{'id':f['id'],'campo':f['eje'],'valor':f['lectura_1'],'origen':f['origen'],'motivo':f['motivo'],'reglas':f['reglas_adoptadas_citadas'],'confianzas':f['confianzas']} for f in cam if f['serie']=='APX']
    ctl=[i for i in seg['control'] if i in R2]
    def _lec(x): return None if x is None else {k:x.get(k) for k in ('territorio','territorios_sec','dominio','dominios_sec','subfuncion','subfunciones_sec','reglas_territorio','reglas_dominio','reglas_subfuncion','abiertas','escala_os','confianza','alternativa','motivo')}
    out={'fecha':'2026-11-16','ensayo':ensayo,'regla':' '.join(x.strip() for x in __doc__.strip().split('\n')[1:4]),'puntos_de_la_revision':{k:{'eje':v[0],'criterio':v[1],'que_falta':v[2],'hallazgos':v[3]} for k,v in R.PUNTOS_REVISION.items()},'corpus':corpus,'apx':apx,'filas':F,
      'lecturas':{i:{'primera':_lec(R1.get(i)),'segunda':_lec(R2.get(i))} for i in ids},'segunda_lectura':{k:seg[k] for k in ('difieren','apx','control')},'lotes':{'primera_lectura':len(glob.glob(os.path.join(B,'lotes','lote_*.jsonl'))),'segunda_lectura':len(glob.glob(os.path.join(B,'lotes2','lote_*.jsonl')))},'complemento_de_la_segunda_lectura':seg.get('complemento'),
      'control':{'pre_ensayos':len(ctl),'coinciden':{e:sum(1 for i in ctl if R1[i][e]==R2[i][e]) for e in EJES}},
      'escala_os':{i:{'lectura_1':R1[i].get('escala_os'),'lectura_2':(R2.get(i) or {}).get('escala_os')} for i in ids if V[i]['mccs']=='OS'}}
    json.dump(out,open(os.path.join(B,'..','scripts','datos_de_trabajo','ajustes_relectura_1_3.json'),'w',encoding='utf-8'),ensure_ascii=False,indent=1)
    print('escrito: corpus',len(corpus),'| apx',len(apx),'| control',out['control'])

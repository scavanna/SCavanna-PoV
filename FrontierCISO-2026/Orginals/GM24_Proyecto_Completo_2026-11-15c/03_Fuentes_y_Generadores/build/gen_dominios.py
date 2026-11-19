# -*- coding: utf-8 -*-
"""Genera paquetes Dominio_* (Endpoints, Identidades, Datos, SIEM, Nube, Productividad v1.1) + nota V7.1."""
import os, json, collections
import data as D, v7 as V, anexos as A, xdr as X, dominios as DM
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
BASE = os.path.join(os.path.dirname(__file__), "..")
CAT = {c["id"]: c for c in V.catalogo_v7()}
TOOLS = dict(A.TOOLS, **X.TOOLS, **DM.TOOLS)
def esc(s): return str(s).replace("|","\\|").replace("\n"," ")
def table(h, rows): return "\n".join(["| "+" | ".join(h)+" |","|"+"|".join(["---"]*len(h))+"|"]+["| "+" | ".join(esc(c) for c in r)+" |" for r in rows])
def write(p, t): open(p,"w",encoding="utf-8").write(t.strip()+"\n")
def hdr(nombre, ver="v1.0"): return f"> **GM-24 V7.1 · Sub-plan PO-GAC · Instancia de dominio: {nombre}** · 2026-11-14 · {ver}. Plano B (*ProductPractice* / escenario). No agrega ni modifica conceptos de la V7 (379): los instancia. Escenario 100 % Microsoft sobre bases agnósticas; estado GA/preview/verificar según Microsoft Learn. Referencias DD/K4x/R/eo:OP/COE: marco interno."

def build(key, ver="v1.0"):
    d = DM.DOMINIOS[key]; root = os.path.join(BASE, f"Dominio_{key}"); os.makedirs(os.path.join(root, "anexos_agentes"), exist_ok=True); os.makedirs(os.path.join(root, "json"), exist_ok=True)
    H = hdr(d["nombre"], ver); KN = dict(A.KNOWLEDGE, **X.KNOWLEDGE); SK = dict(A.SKILLS, **X.SKILLS)
    for dd in DM.DOMINIOS.values(): KN.update(dd.get("knowledge", {})); SK.update(dd.get("skills", {}))
    write(os.path.join(root, "01_Ficha_Producto_Control.md"), f"""# 01 · Ficha de producto-control: {d['nombre']}

{H}

| Campo | Contenido |
|---|---|
| Producto-control | {d['nombre']} |
| Dominio Zero Trust | {d['dominio_zt']} |
| Tecnología | {d['tecnologia']} |
| Funciones CSF 2.0 | {d['funciones_csf']} |
| Fuente oficial del modelo operativo | {d['fuente_oficial']} |
| Objetivo del control | {d['objetivo']} |
| SLO | {d['slo']} |
| Owner | PO-GAC {key.title()} (sponsor de los agentes {d['agente']}-xx en Entra Agent ID) |
| Diferencia frente a otros dominios | {d['diferencia']} |
| Interfaz con otros owners | {d['interfaz']} |
| Personas (Learn) | {d['personas']} |
| Permisos | {d['permisos']} |

## Grilla de ownership CSF 2.0 × dominio

{table(["Categoría CSF 2.0","Tareas del modelo operativo"], [(c, ", ".join(t[0] for t in d["tareas"] if c in t[4])) for c in sorted({x.strip() for t in d["tareas"] for x in t[4].split(",")})])}
""")
    by = collections.defaultdict(list)
    for t in d["tareas"]: by[t[2].split("/")[0].split(" ")[0]].append(t)
    eo = sorted({t[6] for t in d["tareas"]}); prevk = {t[6].split(" ")[0] for t in D.TAREAS} | {t[6].split(" ")[0] for t in X.TAREAS}
    body = f"# 03 · Modelo operativo ({len(d['tareas'])} tareas)\n\n{H}\n\nFuente: {d['fuente_oficial']}.\n\n## 1. Tareas\n\n" + table(["ID","Tarea","Cadencia","Persona","CSF 2.0","SAF","eo:OP","Autonomía","Agente","KPI","Fuente"], d["tareas"]) + "\n\n## 2. Vista por cadencia\n"
    for cad in ["Diaria","Semanal","Mensual","Trimestral","Por","Según"]:
        if by.get(cad): body += f"\n### {dict(Por='Por evento', Según='Según necesidad').get(cad, cad)}\n\n" + table(["ID","Tarea","Humano","Agente","Autonomía"], [(t[0],t[1],t[3],t[8],t[7]) for t in by[cad]]) + "\n"
    body += f"\n## 3. Prácticas agnósticas eo:OP ({len(eo)})\n\n" + table(["Práctica","Tareas","Origen"], [(e, ", ".join(t[0] for t in d["tareas"] if t[6]==e), "Reutilizada (productividad/XDR)" if e.split(" ")[0] in prevk else "Nueva (propuesta MAEO)") for e in eo])
    write(os.path.join(root, "03_Modelo_Operativo.md"), body)
    sh = {k: collections.defaultdict(list) for k in "tks"}
    for a in d["agentes"]:
        for t in a[12]: sh["t"][t].append(a[0])
        for k in a[13]: sh["k"][k].append(a[0])
        for s in a[14]: sh["s"][s].append(a[0])
    alc = lambda l: f"Compartido ({', '.join(l)})" if len(l) > 1 else "Propio"
    out = []
    for a in d["agentes"]:
        aid, nombre, prop, tareas, aut, gates, kpis, costo, asi, ident, owner, ruta, tl, kl, sl = a
        tr = [(t, TOOLS[t]["tipo"], TOOLS[t]["nombre"], TOOLS[t]["op"], TOOLS[t]["permiso"], TOOLS[t]["estado"], alc(sh["t"][t]), TOOLS[t]["fuente"]) for t in tl] + [(t, TOOLS[t]["tipo"], TOOLS[t]["nombre"], TOOLS[t]["op"], TOOLS[t]["permiso"], TOOLS[t]["estado"], "Común a la flota", TOOLS[t]["fuente"]) for t in X.COMUNES["tools"]]
        kr = [(k, KN[k]["nombre"], KN[k]["tipo"], alc(sh["k"][k]), KN[k]["fuente"]) for k in kl] + [(k, KN[k]["nombre"], KN[k]["tipo"], "Común a la flota", KN[k]["fuente"]) for k in X.COMUNES["knowledge"]]
        sr = [(s, SK[s]["nombre"], SK[s]["desc"], alc(sh["s"][s])) for s in sl] + [(s, SK[s]["nombre"], SK[s]["desc"], "Común a la flota") for s in X.COMUNES["skills"]]
        write(os.path.join(root, "anexos_agentes", f"{aid}_{nombre.replace(' ','_').replace('/','-')}.md"), f"""# Anexo de agente {aid} — {nombre}

{H}

## 1. Identificación

| Campo | Contenido |
|---|---|
| ID / nombre | {aid} · {nombre} |
| Propósito | {prop} |
| Tareas del modelo operativo | {tareas} |
| Nivel de autonomía | {aut} |
| Gates HITL / límites | {gates} |
| KPIs | {kpis} |
| Driver de costo | {costo} |
| Riesgos OWASP Agentic 2026 v2.01 | {asi} |
| Identidad y acceso | {ident} |
| Owner / sponsor | {owner} |
| Ruta de construcción | {ruta} — {A.RUTAS[ruta[:2]]} |
| Entorno | Copilot Studio en entorno de desarrollo (R2) o agente personalizado de Security Copilot (R1) |
| Controles AGC aplicables | AGC-03, 05, 06, 09, 11, 12, 14{', 10' if ('Manage' in ident or 'ReadWrite' in ident) else ''} |

## 2. Tareas que asiste

{table(["Tarea","Descripción","Cadencia","Autonomía"], [(t[0],t[1],t[2],t[7]) for t in d["tareas"] if t[8]==aid])}

## 3. Tools (propios, compartidos y comunes)

{table(["ID","Tipo","Tool","Operación","Permiso mínimo","Estado","Alcance","Fuente"], tr)}

## 4. Knowledge

{table(["ID","Fuente","Tipo","Alcance","Origen"], kr)}

## 5. Skills

{table(["ID","Skill","Descripción","Alcance"], sr)}

## 6. Notas

- Tools **verificar**: sin API pública confirmada; el agente opera por hunting o deja la tarea al humano. El agente nunca aprueba sus propias acciones (Approvals T-17).
""")
        out.append(dict(id=aid, nombre=nombre, proposito=prop, tareas=tareas, autonomia=aut, gates=gates, kpis=kpis, costo=costo, riesgos_asi=asi, identidad=ident, owner=owner, ruta=ruta, tools_propios=tl, knowledge_propios=kl, skills_propios=sl, tools_comunes=X.COMUNES["tools"], knowledge_comunes=X.COMUNES["knowledge"], skills_comunes=X.COMUNES["skills"]))
    alltools = sorted({t for a in d["agentes"] for t in a[12]} | set(X.COMUNES["tools"]))
    nuevos = {t: TOOLS[t] for t in alltools if t.startswith(d["prefijo"][0] + "T") and t in DM.TOOLS}
    write(os.path.join(root, "04_Catalogo_Agentes.md"), f"""# 04 · Catálogo de agentes ({len(d['agentes'])})

{H}

## 1. Resumen

{table(["ID","Agente","Tareas","Autonomía","Ruta"], [(a[0],a[1],a[3],a[4],a[11]) for a in d["agentes"]])}

## 2. Tools de la flota ({len(alltools)}; nuevos del dominio: {len(nuevos)})

{table(["ID","Tipo","Tool","Operación","Permiso mínimo","Estado","Alcance","Agentes","Fuente"], [(t,TOOLS[t]["tipo"],TOOLS[t]["nombre"],TOOLS[t]["op"],TOOLS[t]["permiso"],TOOLS[t]["estado"],"Común" if t in X.COMUNES["tools"] else ("Compartido" if len(sh["t"][t])>1 else "Propio"),", ".join(sh["t"][t]) or "flota",TOOLS[t]["fuente"]) for t in alltools])}

## 3. Knowledge nuevos ({len(d['knowledge'])})

{table(["ID","Fuente","Tipo","Agentes","Origen"], [(k,K["nombre"],K["tipo"],", ".join(sh["k"][k]),K["fuente"]) for k,K in d["knowledge"].items()])}

## 4. Skills nuevos ({len(d['skills'])})

{table(["ID","Skill","Descripción","Agentes"], [(s,K["nombre"],K["desc"],", ".join(sh["s"][s])) for s,K in d["skills"].items()])}

## 5. Matriz tools × agentes (● propio · ◎ común)

{table(["Tool"]+[a[0] for a in d["agentes"]], [[t]+[("●" if t in a[12] else ("◎" if t in X.COMUNES["tools"] else "")) for a in d["agentes"]] for t in alltools])}
""")
    hitos = ""
    if d.get("hitos"): hitos = "\n\n## Hitos de plataforma que condicionan esta instancia\n\n" + table(["Fecha","Hito","Efecto en el dominio"], d["hitos"])
    write(os.path.join(root, "02_Instanciacion_de_Conceptos_V7.md"), f"""# 02 · Cómo el dominio {key.title()} instancia los conceptos V7 (sin modificarlos)

{H}

{table(["Concepto V7","Tipo","Unidad(es)","Concepto","Instancia"], [(cid, CAT[cid]["tipo"], CAT[cid]["unidad"], CAT[cid]["concepto"], txt) for cid, txt in d["instancia"]])}{hitos}
""")
    json.dump(dict(ficha={k: v for k, v in d.items() if k not in ("tareas","agentes","knowledge","skills","instancia","hitos")}, hitos=d.get("hitos", []), tareas=d["tareas"], agentes=out, tools_nuevos=nuevos, knowledge_nuevos=d["knowledge"], skills_nuevos=d["skills"], instanciacion=d["instancia"]), open(os.path.join(root, "json", f"dominio_{key.lower()}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    FONT="Arial"; HF=PatternFill("solid",fgColor="17354F"); HFont=Font(name=FONT,bold=True,color="FFFFFF",size=10); BF=Font(name=FONT,size=9); TH=Side(style="thin",color="D0D7E2"); BR=Border(left=TH,right=TH,top=TH,bottom=TH)
    wb=Workbook(); wb.remove(wb.active)
    def sheet(name, headers, rows, widths=None):
        ws=wb.create_sheet(name[:31]); ws.append(headers)
        for r in rows: ws.append([("" if v is None else (", ".join(map(str,v)) if isinstance(v,(list,tuple)) else v)) for v in r])
        for c in range(1,len(headers)+1):
            cell=ws.cell(row=1,column=c); cell.fill=HF; cell.font=HFont; cell.alignment=Alignment(vertical="center",wrap_text=True); cell.border=BR
        for row in ws.iter_rows(min_row=2,max_row=ws.max_row,max_col=len(headers)):
            for cell in row: cell.font=BF; cell.alignment=Alignment(vertical="top",wrap_text=True); cell.border=BR
        for i,w in enumerate(widths or [18]*len(headers),1): ws.column_dimensions[get_column_letter(i)].width=w
        ws.row_dimensions[1].height=34; ws.freeze_panes="A2"; ws.auto_filter.ref=f"A1:{get_column_letter(len(headers))}{ws.max_row}"; ws.sheet_view.showGridLines=False
    sheet("00_Ficha",["Campo","Contenido"],[(k,v) for k,v in d.items() if k not in ("tareas","agentes","knowledge","skills","instancia","hitos")],[28,150])
    sheet("01_Modelo_Operativo",["ID","Tarea","Cadencia","Persona","CSF 2.0","SAF","eo:OP","Autonomía","Agente","KPI","Fuente"],d["tareas"],[9,56,12,26,14,8,46,9,8,30,40])
    sheet("02_Agentes",["ID","Agente","Propósito","Tareas","Autonomía","Gates","KPIs","Costo","Riesgos ASI","Identidad","Owner","Ruta","Tools propios","Knowledge propios","Skills propios"],[(o["id"],o["nombre"],o["proposito"],o["tareas"],o["autonomia"],o["gates"],o["kpis"],o["costo"],o["riesgos_asi"],o["identidad"],o["owner"],o["ruta"],o["tools_propios"],o["knowledge_propios"],o["skills_propios"]) for o in out],[7,30,50,18,10,40,28,16,12,34,16,12,22,18,18])
    sheet("03_Tools_Nuevos",["ID","Tipo","Tool","Operación","Permiso mínimo","Estado","Fuente"],[(t,T["tipo"],T["nombre"],T["op"],T["permiso"],T["estado"],T["fuente"]) for t,T in nuevos.items()],[7,20,50,44,44,20,50])
    sheet("04_Knowledge_Nuevos",["ID","Fuente","Tipo","Origen"],[(k,K["nombre"],K["tipo"],K["fuente"]) for k,K in d["knowledge"].items()],[8,70,24,36])
    sheet("05_Skills_Nuevos",["ID","Skill","Descripción"],[(s,K["nombre"],K["desc"]) for s,K in d["skills"].items()],[8,40,90])
    sheet("06_Instanciacion_V7",["Concepto V7","Tipo","Unidad(es)","Concepto","Instancia"],[(cid,CAT[cid]["tipo"],CAT[cid]["unidad"],CAT[cid]["concepto"],txt) for cid,txt in d["instancia"]],[11,6,12,40,90])
    wb.save(os.path.join(root, f"GM24_V7_Dominio_{key}.xlsx"))
    write(os.path.join(root, "README.md"), f"# Dominio {key.title()} — instancia del rol PO-GAC\n\n{H}\n\n01 Ficha · 02 Instanciación · 03 Modelo operativo ({len(d['tareas'])} tareas) · 04 Agentes ({len(d['agentes'])}) + anexos_agentes/ · XLSX · json/.")
    write(os.path.join(root, "VERSION.md"), f"# Dominio_{key} {ver} · 2026-11-14\n\nPlano B (capacidades contratadas). No es una versión del GM-24 (plano A, V7.1).\n")
    print("ok", key, len(d["tareas"]), len(d["agentes"]))
    return d, out

def v71_y_comparativa(res):
    write(os.path.join(BASE, "V7.1_Nota_Editorial_Generalizacion.md"), f"""# V7.1 — Nota editorial: generalización de 4 títulos (sin cambio de IDs, cantidad, pre-ensayos ni mapeo)

> GM-24 V7 → V7.1 · 2026-11-14. Cambio **editorial** derivado de las instancias de dominio: cuatro PA promovidos al programa en V7 llevaban título específico de correo; el concepto generalizable es "del dominio". No se crean conceptos, no cambian IDs ni cantidades (379), no cambia la matriz de estándares.

{table(["ID","Título V7","Título V7.1","Tratamiento del pre-ensayo"], DM.V71)}

**Efecto en los documentos GM-24:** título sustituido en catálogo, tres documentos GM-24 y Anexo PO-GAC (marcador ◆ V7.1); el pre-ensayo se conserva como instancia de referencia con nota "Instancias". No requiere nuevo mapeo.
""")

if __name__ == "__main__":
    res = {k: build(k) for k in DM.DOMINIOS}; v71_y_comparativa(res); print("DONE")

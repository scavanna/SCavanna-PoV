# -*- coding: utf-8 -*-
"""Genera el paquete 'Dominio_XDR' (instancia del rol PO-GAC para Defender XDR): MD + JSON + XLSX."""
import os, json, collections
import data as D, v7 as V, anexos as A, xdr as X
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
ROOT = os.path.join(os.path.dirname(__file__), "..", "Dominio_XDR"); os.makedirs(os.path.join(ROOT, "anexos_agentes"), exist_ok=True); os.makedirs(os.path.join(ROOT, "json"), exist_ok=True)
CAT = {c["id"]: c for c in V.catalogo_v7()}
def esc(s): return str(s).replace("|","\\|").replace("\n"," ")
def table(h, rows): return "\n".join(["| "+" | ".join(h)+" |","|"+"|".join(["---"]*len(h))+"|"]+["| "+" | ".join(esc(c) for c in r)+" |" for r in rows])
def write(p, t): open(p,"w",encoding="utf-8").write(t.strip()+"\n")
HDR = "> **GM-24 V7.1 · Sub-plan PO-GAC · Instancia de dominio: Detección y respuesta unificada (Microsoft Defender XDR)** · 2026-11-14 · Dominio_XDR v1.0. Nivel de abstracción: *ProductPractice* / escenario (plano B). No agrega ni modifica conceptos de la V7 (379): los instancia. Escenario 100 % Microsoft sobre bases agnósticas; estado GA/preview/verificar según Microsoft Learn. Referencias DD/K4x/R/eo:OP/COE: marco interno."
TOOLS = dict(A.TOOLS, **X.TOOLS); KN = dict(A.KNOWLEDGE, **X.KNOWLEDGE); SK = dict(A.SKILLS, **X.SKILLS)
EQUIV = {"XA-01":"AG-01","XA-02":"AG-02","XA-03":"—","XA-04":"AG-03/AG-11","XA-05":"—","XA-06":"AG-06","XA-07":"AG-14","XA-08":"AG-08","XA-09":"AG-05","XA-10":"AG-09","XA-11":"AG-10","XA-12":"AG-12","XA-13":"AG-13","XA-14":"—","XA-15":"AG-15"}

def ficha():
    f = X.FICHA
    write(os.path.join(ROOT, "01_Ficha_Producto_Control_XDR.md"), f"""# 01 · Ficha de producto-control: {f['nombre']}

{HDR}

## 1. Respuestas previas (por qué esta instancia no toca los 379)

- **Productividad fue un ejemplo.** El rol PO-GAC se define como función CSF × dominio Zero Trust × tecnología × modelo operativo; productividad fue un valor del eje "dominio".
- **XDR es la segunda instancia.** Mismo rol, mismas competencias, mismos conceptos; cambian el dominio (SecOps), la tecnología (Defender XDR) y el modelo operativo.
- **Nivel de abstracción.** Los 379 son conceptos-lección; este paquete es su instancia de dominio. 4 PA promovidos en V7 tenían título específico de correo: la V7.1 los generalizó sin cambiar IDs ni cantidad (ver §6).

## 2. Ficha

| Campo | Contenido |
|---|---|
| Producto-control | {f['nombre']} |
| Dominio Zero Trust | {f['dominio_zt']} |
| Tecnología | {f['tecnologia']} |
| Funciones CSF 2.0 | {f['funciones_csf']} |
| Fuente oficial del modelo operativo | {f['fuente_oficial']} |
| Objetivo del control | {f['objetivo']} |
| SLO | {f['slo']} |
| Owner | PO-GAC XDR (sponsor de los 15 agentes XA-01…XA-15 en Entra Agent ID) |
| Diferencia frente a productividad | {f['diferencia_vs_productividad']} |
| Interfaz con otros owners | {f['interfaz_con_otros_owners']} |
| Personas SOC (Learn, step 4) | SOC Oversight · Threat Intelligence & Analytics · Monitoring (Tier 1-3) · Engineering & SecOps · CSIRT |
| Permisos (Unified RBAC) | Security data basics (Read) · Alerts (Manage) · Response (Manage) · Basic/Advanced live response · File collection · Email & collaboration quarantine/advanced actions · Automation rules · Playbooks · Integrations |

## 3. Grilla de ownership CSF 2.0 × dominio SecOps (XDR)

{table(["Categoría CSF 2.0","Qué hace el control XDR","Tarea(s)","Dueño"], [
 ("GV.RR","Roles SOC y Unified RBAC para humanos y agentes","XDR-M02","PO-GAC XDR + IAM"),("GV.OV","Supervisión de la automatización, informes, cambios de plataforma","XDR-D03, XDR-M04, XDR-W05","PO-GAC XDR"),
 ("GV.PO","Casos de uso, playbooks, baseline de automatización","XDR-Q01, XDR-M01","PO-GAC XDR + CSIRT"),("ID.RA","Threat analytics, hunting, exposición","XDR-D07, XDR-W01, XDR-W03","TI + Monitoring"),
 ("ID.AM","Inventario de fuentes de señal","XDR-A04","Engineering"),("ID.IM","Clasificación, tuning, lecciones, Secure Score","XDR-D04, XDR-D05, XDR-M05","Monitoring + SOC Oversight"),
 ("PR.PS","Niveles AIR, políticas de alertas, salud de sensores","XDR-M01, XDR-D06","Security Administration"),("PR.AA","Unified RBAC, recertificación, identidades de agentes","XDR-M02, XDR-Q03","IAM"),
 ("DE.CM","Cola unificada, hunting, informes de amenazas","XDR-D01, XDR-W01, XDR-W04","Monitoring"),("DE.AE","Correlación, detecciones personalizadas, automation rules","XDR-W02, XDR-D04","Engineering + Monitoring"),
 ("RS.MA","Gestión de incidentes y casos, escalamiento ITSM","XDR-D01, XDR-D08, XDR-A03","Monitoring"),("RS.AN","Investigación, live response, forense","XDR-D02, XDR-A02","Tier 2-3 + CSIRT"),
 ("RS.MI","Acciones de respuesta, AIR","XDR-D02, XDR-D03, XDR-A01","Monitoring + CSIRT"),("RS.CO","Notificaciones, comunicación de incidentes mayores","XDR-D08, XDR-A01","SOC Oversight"),("RC.RP","Recuperación tras contención","XDR-A01","CSIRT + owners de dominio"),
])}

## 4. KPIs / KRIs del control XDR

{table(["ID","Indicador","Definición","Meta","Cadencia","Tipo"], [
 ("XKPI-01","SLA de triaje High/Medium","Incidentes H/M triados en SLA","≥95 %","Semanal","KPI control"),("XKPI-02","MTTR por severidad","Creación→resolución","High ≤8 h","Mensual","KPI control"),("XKPI-03","Acciones AIR pendientes >4 h","Sin decisión","0","Diaria","KRI control"),
 ("XKPI-04","Salud de sensores","% EDR/AV saludables; MDI sin issues","≥98 %; 0","Diaria","KPI control"),("XKPI-05","Dispositivos no onboarded","Sin EDR","Tendencia ↓","Semanal","KRI control"),("XKPI-06","Reglas de tuning sin vencimiento","Supresiones huérfanas","0","Mensual","KRI control"),
 ("XKPI-07","Grupos fuera del baseline AIR","Desviaciones","0","Mensual","KRI control"),("XKPI-08","Asignaciones RBAC sin justificación","Humanos y agentes","0","Mensual","KRI gobierno"),("XKPI-09","Precisión del agente de triaje","Propuestas aceptadas","≥90 %","Mensual","KPI agente"),
 ("XKPI-10","Acciones de respuesta revertidas","Aislamientos/revocaciones revertidos","<2 %","Mensual","KRI agente"),("XKPI-11","Tasa de escalamiento a humano","Fuera de alcance","10–30 %","Mensual","KPI agente"),("XKPI-12","Costo por incidente asistido","SCU/tokens / incidentes","Según presupuesto","Mensual","KPI FinOps"),
 ("XKPI-13","Cobertura de observabilidad","Agentes con telemetría en Sentinel","100 %","Mensual","KPI gobierno"),("XKPI-14","Horas humanas liberadas (medidas)","Tareas ejecutadas por agentes","Según caso de negocio","Trimestral","KPI valor"),
])}

## 5. Permisos mínimos por grupo de tareas (Unified RBAC)

{table(["Grupo","Humano","Agente"], [
 ("Triaje / clasificación / casos","Security data basics + Alerts (Manage)","Security data basics (Read); clasificación tras aprobación"),("Investigación y respuesta","Alerts + Response (Manage); live response según tier","Lectura + acciones acotadas tras aprobación; nunca live response"),
 ("Action center","Response (Manage)","Response (Read); prepara decisión"),("Tuning / detecciones / automation","Alerts (Manage), Custom detections, Automation rules","Lectura + propuestas; creación con aprobación"),
 ("Salud / postura / informes","Security data basics; Security Administrator","Solo lectura"),("RBAC / baseline","Authorization (Manage)","RoleManagement.Read.Defender (lectura)"),
])}

## 6. Generalización V7.1 (editorial, sin impacto en IDs ni cantidad)

{table(["ID","Título V7 (específico de correo)","Título V7.1"], X.GENERALIZAR_V71)}
""")

def modelo():
    by = collections.defaultdict(list)
    for t in X.TAREAS: by[t[2].split("/")[0].split(" ")[0]].append(t)
    body = f"# 03 · Modelo operativo del control XDR ({len(X.TAREAS)} tareas)\n\n{HDR}\n\nFuentes: Defender XDR SecOps guide (steps 4–6), MDE Security Operations Guide, MDI operational guide, MDA daily guide, AIR y Unified RBAC. XDR-Q02/Q03 son propuestas del sub-plan.\n\n## 1. Tareas\n\n" + table(["ID","Tarea","Cadencia","Persona (Learn)","CSF 2.0","SAF","Práctica agnóstica eo:OP","Autonomía","Agente","KPI","Fuente"], X.TAREAS) + "\n\n## 2. Vista por cadencia\n"
    for cad in ["Diaria","Semanal","Mensual","Trimestral","Por","Según"]:
        if by.get(cad): body += f"\n### {dict(Por='Por evento', Según='Según necesidad').get(cad, cad)}\n\n" + table(["ID","Tarea","Humano","Agente","Autonomía"], [(t[0],t[1],t[3],t[8],t[7]) for t in by[cad]]) + "\n"
    eo = sorted({t[6] for t in X.TAREAS}); prod_eo = {t[6].split(" ")[0] for t in D.TAREAS}
    body += f"\n## 3. Prácticas agnósticas ({len(eo)})\n\n" + table(["Práctica eo:OP","Tareas XDR","Origen"], [(e, ", ".join(t[0] for t in X.TAREAS if t[6]==e), "Reutilizada (instancia productividad)" if e.split(" ")[0] in prod_eo else "Nueva (propuesta MAEO)") for e in eo]) + "\n\nLa reutilización de prácticas eo:OP entre dominios demuestra que el modelo es portable: la tarea de producto cambia, la práctica agnóstica no.\n"
    write(os.path.join(ROOT, "03_Modelo_Operativo_XDR.md"), body)

def agentes():
    sh = {k: collections.defaultdict(list) for k in "tks"}
    for a in X.AGENTES:
        for t in a[12]: sh["t"][t].append(a[0])
        for k in a[13]: sh["k"][k].append(a[0])
        for s in a[14]: sh["s"][s].append(a[0])
    alc = lambda l: f"Compartido ({', '.join(l)})" if len(l) > 1 else "Propio"
    out = []
    for a in X.AGENTES:
        aid, nombre, prop, tareas, aut, gates, kpis, costo, asi, ident, owner, ruta, tl, kl, sl = a
        tr = [(t, TOOLS[t]["tipo"], TOOLS[t]["nombre"], TOOLS[t]["op"], TOOLS[t]["permiso"], TOOLS[t]["estado"], alc(sh["t"][t]), TOOLS[t]["fuente"]) for t in tl] + [(t, TOOLS[t]["tipo"], TOOLS[t]["nombre"], TOOLS[t]["op"], TOOLS[t]["permiso"], TOOLS[t]["estado"], "Común a la flota", TOOLS[t]["fuente"]) for t in X.COMUNES["tools"]]
        kr = [(k, KN[k]["nombre"], KN[k]["tipo"], alc(sh["k"][k]), KN[k]["fuente"]) for k in kl] + [(k, KN[k]["nombre"], KN[k]["tipo"], "Común a la flota", KN[k]["fuente"]) for k in X.COMUNES["knowledge"]]
        sr = [(s, SK[s]["nombre"], SK[s]["desc"], alc(sh["s"][s])) for s in sl] + [(s, SK[s]["nombre"], SK[s]["desc"], "Común a la flota") for s in X.COMUNES["skills"]]
        write(os.path.join(ROOT, "anexos_agentes", f"{aid}_{nombre.replace(' ','_').replace('/','-')}.md"), f"""# Anexo de agente {aid} — {nombre}

{HDR}

## 1. Identificación

| Campo | Contenido |
|---|---|
| ID / nombre | {aid} · {nombre} |
| Equivalente en productividad | {EQUIV[aid]} |
| Propósito | {prop} |
| Tareas del modelo operativo XDR | {tareas} |
| Nivel de autonomía | {aut} |
| Gates HITL / límites | {gates} |
| KPIs | {kpis} |
| Driver de costo | {costo} |
| Riesgos OWASP Agentic 2026 v2.01 | {asi} |
| Identidad y acceso | {ident} |
| Owner / sponsor | {owner} |
| Ruta de construcción | {ruta} — {A.RUTAS[ruta[:2]]} |
| Entorno | Copilot Studio en entorno de desarrollo (R2) o agente personalizado de Security Copilot (R1) |
| Controles AGC aplicables | AGC-03, 05, 06, 09, 11, 12, 14{', 10' if 'Response' in ident else ''} |

## 2. Tareas que asiste

{table(["Tarea","Descripción","Cadencia","Autonomía"], [(t[0],t[1],t[2],t[7]) for t in X.TAREAS if t[8]==aid])}

## 3. Tools (propios, compartidos y comunes)

{table(["ID","Tipo","Tool","Operación","Permiso mínimo","Estado","Alcance","Fuente"], tr)}

## 4. Knowledge

{table(["ID","Fuente","Tipo","Alcance","Origen"], kr)}

## 5. Skills

{table(["ID","Skill","Descripción","Alcance"], sr)}

## 6. Notas

- Las acciones de respuesta sobre dispositivos e identidades (XT-01, XT-02) son las de mayor impacto de la flota: solo L2 con límite de alcance y nunca live response para agentes.
- Tools **verificar**: el agente opera por hunting o deja la tarea al humano.
""")
        out.append(dict(id=aid, nombre=nombre, proposito=prop, tareas=tareas, autonomia=aut, gates=gates, kpis=kpis, costo=costo, riesgos_asi=asi, identidad=ident, owner=owner, ruta=ruta, equivalente_productividad=EQUIV[aid], tools_propios=tl, knowledge_propios=kl, skills_propios=sl, tools_comunes=X.COMUNES["tools"], knowledge_comunes=X.COMUNES["knowledge"], skills_comunes=X.COMUNES["skills"]))
    alltools = sorted({t for a in X.AGENTES for t in a[12]} | set(X.COMUNES["tools"]))
    write(os.path.join(ROOT, "04_Catalogo_Agentes_XDR.md"), f"""# 04 · Catálogo de agentes XDR ({len(X.AGENTES)})

{HDR}

## 1. Resumen

{table(["ID","Agente","Tareas","Autonomía","Ruta","Equivalente productividad"], [(a[0],a[1],a[3],a[4],a[11],EQUIV[a[0]]) for a in X.AGENTES])}

**Orden de construcción sugerido:** XA-05, XA-08/XA-09, XA-10, XA-03, XA-04, XA-01, XA-07, XA-14, XA-06, XA-11, XA-12, XA-13, XA-15, **XA-02 último**.

## 2. Tools de la flota XDR ({len(alltools)})

{table(["ID","Tipo","Tool","Operación","Permiso mínimo","Estado","Alcance","Agentes","Fuente"], [(t,TOOLS[t]["tipo"],TOOLS[t]["nombre"],TOOLS[t]["op"],TOOLS[t]["permiso"],TOOLS[t]["estado"],"Común" if t in X.COMUNES["tools"] else ("Compartido" if len(sh["t"][t])>1 else "Propio"),", ".join(sh["t"][t]) or "flota",TOOLS[t]["fuente"]) for t in alltools])}

## 3. Knowledge nuevos ({len(X.KNOWLEDGE)})

{table(["ID","Fuente","Tipo","Agentes","Origen"], [(k,K["nombre"],K["tipo"],", ".join(sh["k"][k]),K["fuente"]) for k,K in X.KNOWLEDGE.items()])}

## 4. Skills nuevos ({len(X.SKILLS)})

{table(["ID","Skill","Descripción","Agentes"], [(s,K["nombre"],K["desc"],", ".join(sh["s"][s])) for s,K in X.SKILLS.items()])}

## 5. Matriz tools × agentes (● propio · ◎ común)

{table(["Tool"]+[a[0] for a in X.AGENTES], [[t]+[("●" if t in a[12] else ("◎" if t in X.COMUNES["tools"] else "")) for a in X.AGENTES] for t in alltools])}
""")
    json.dump(dict(agentes=out, tools_nuevos=X.TOOLS, knowledge_nuevos=X.KNOWLEDGE, skills_nuevos=X.SKILLS, comunes=X.COMUNES), open(os.path.join(ROOT,"json","agentes_xdr.json"),"w",encoding="utf-8"), ensure_ascii=False, indent=1)
    return out

def instancia():
    write(os.path.join(ROOT, "02_Instanciacion_de_Conceptos_V7.md"), f"""# 02 · Cómo el dominio XDR instancia los conceptos V7 (sin modificarlos)

{HDR}

## 1. Principio

Los 379 conceptos son el nivel curricular. Un dominio es el nivel de **instancia**: el mismo concepto se ejercita con otra tecnología, otro modelo operativo y otros agentes (`ProductPractice` EXEMPLIFIES `eo:OP`; agente REALIZED_WITH capacidad). Construir XDR **no agrega conceptos**.

## 2. Tabla de instanciación ({len(X.INSTANCIA)})

{table(["Concepto V7","Tipo","Unidad(es)","Concepto","Instancia XDR"], [(cid, CAT[cid]["tipo"], CAT[cid]["unidad"], CAT[cid]["concepto"], txt) for cid, txt in X.INSTANCIA])}

## 3. Generalización V7.1

{table(["ID","Título V7","Título V7.1"], X.GENERALIZAR_V71)}
""")

def xlsx(out):
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
    sheet("00_Ficha",["Campo","Contenido"],[(k,v) for k,v in X.FICHA.items()],[28,150])
    sheet("01_Modelo_Operativo",["ID","Tarea","Cadencia","Persona","CSF 2.0","SAF","eo:OP","Autonomía","Agente","KPI","Fuente"],X.TAREAS,[9,56,12,26,14,8,46,9,8,30,40])
    sheet("02_Agentes",["ID","Agente","Propósito","Tareas","Autonomía","Gates","KPIs","Costo","Riesgos ASI","Identidad","Owner","Ruta","Equivalente MDO","Tools propios","Knowledge propios","Skills propios"],[(o["id"],o["nombre"],o["proposito"],o["tareas"],o["autonomia"],o["gates"],o["kpis"],o["costo"],o["riesgos_asi"],o["identidad"],o["owner"],o["ruta"],o["equivalente_productividad"],o["tools_propios"],o["knowledge_propios"],o["skills_propios"]) for o in out],[7,30,50,18,10,40,28,16,12,34,16,12,12,22,18,18])
    sheet("03_Tools_Nuevos",["ID","Tipo","Tool","Operación","Permiso mínimo","Estado","Fuente"],[(t,T["tipo"],T["nombre"],T["op"],T["permiso"],T["estado"],T["fuente"]) for t,T in X.TOOLS.items()],[7,20,50,44,44,20,50])
    sheet("04_Knowledge_Nuevos",["ID","Fuente","Tipo","Origen"],[(k,K["nombre"],K["tipo"],K["fuente"]) for k,K in X.KNOWLEDGE.items()],[8,70,24,36])
    sheet("05_Skills_Nuevos",["ID","Skill","Descripción"],[(s,K["nombre"],K["desc"]) for s,K in X.SKILLS.items()],[8,40,90])
    sheet("06_Instanciacion_V7",["Concepto V7","Tipo","Unidad(es)","Concepto","Instancia XDR"],[(cid,CAT[cid]["tipo"],CAT[cid]["unidad"],CAT[cid]["concepto"],txt) for cid,txt in X.INSTANCIA],[11,6,12,40,90])
    sheet("07_Generalizar_V7.1",["ID","Título V7","Título V7.1"],X.GENERALIZAR_V71,[11,60,90])
    wb.save(os.path.join(ROOT, "GM24_V7_Dominio_XDR.xlsx"))

if __name__ == "__main__":
    ficha(); modelo(); out = agentes(); instancia(); xlsx(out)
    json.dump(dict(ficha=X.FICHA, tareas=X.TAREAS, instanciacion=X.INSTANCIA, generalizar_v71=X.GENERALIZAR_V71), open(os.path.join(ROOT,"json","dominio_xdr.json"),"w",encoding="utf-8"), ensure_ascii=False, indent=1)
    write(os.path.join(ROOT, "README.md"), f"# Dominio XDR — instancia del rol PO-GAC\n\n{HDR}\n\n01 Ficha · 02 Instanciación · 03 Modelo operativo ({len(X.TAREAS)} tareas) · 04 Agentes ({len(X.AGENTES)}) + anexos_agentes/ · XLSX · json/.")
    write(os.path.join(ROOT, "VERSION.md"), "# Dominio_XDR v1.0 · 2026-11-14\n\nPlano B. No es una versión del GM-24 (plano A, V7.1).\n")
    print("ok XDR")

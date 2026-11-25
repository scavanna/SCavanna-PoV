# -*- coding: utf-8 -*-
"""Generador maestro GM-24 V7.1 (plano A): docs del sub-plan, documentos GM-24, pre-ensayos (99 nuevos + 280 originales), catálogo, matriz, informes, XLSX, HTML."""
import os, json, glob, shutil, html as H, collections, base64
import data as D
D.VERSION = "V7.1"
import v7 as V; V.VERSION = "V7.1"
import gen_md as G, gen_v6 as G6, gen_html as GH, mapeo as M, estandares as S, practica as PR, dominios as DM
import ensayos_pa_1, ensayos_pa_2, ensayos_pa_3, ensayos_amp_1, ensayos_amp_2, ensayos_amp_3
E = {}
for x in (ensayos_pa_1, ensayos_pa_2, ensayos_pa_3): E.update(x.E)
for k, (pr, nx) in PR.P.items(): E[k]["practica"] = pr; E[k]["proximos"] = nx
for x in (ensayos_amp_1, ensayos_amp_2, ensayos_amp_3): E.update(x.E)
HERE = os.path.dirname(os.path.abspath(__file__)); BASE = os.path.abspath(os.path.join(HERE, ".."))
ROOT = os.path.join(BASE, "GM24_V7.1"); os.makedirs(ROOT, exist_ok=True)
DIRS = {k: os.path.join(ROOT, k) for k in ["docs","GM24_V7.1_docs","pre_ensayos","pre_ensayos/individuales","pre_ensayos/originales_K_HC","mapeo","informe","json"]}
for p in DIRS.values(): os.makedirs(p, exist_ok=True)
FECHA = V.FECHA
TIT = json.load(open(os.path.join(HERE, "v71_titulos.json"), encoding="utf-8"))
CAT = V.catalogo_v7()
SRC = {c["id"]: c for c in D.CAT}
for c in CAT:
    if c["id"] in TIT: c["titulo_v7"] = TIT[c["id"]]["antes"]; c["estado"] += " — título generalizado (V7.1)"; c["origen_version"] += " → V7.1"
    s = SRC.get(c["id"])
    if s and s.get("texto_completo"): c["texto_completo"] = s["texto_completo"]; c["pregunta"] = s.get("pregunta", ""); c["relaciones_hc"] = s.get("relaciones_hc", []); c["tesis"] = s.get("tesis", c["tesis"])
    elif c["id"] in E: c["texto_completo"] = "\n\n".join(E[c["id"]][k] for k in ("tesis","tension","aplicacion","evidencia","puentes")); c["pregunta"] = E[c["id"]]["pregunta"]
CATX = {c["id"]: c for c in CAT}; PAX = {p[0]: p for p in D.PA}
def esc(s): return str(s).replace("|","\\|").replace("\n"," ")
def table(h, rows): return "\n".join(["| "+" | ".join(h)+" |","|"+"|".join(["---"]*len(h))+"|"]+["| "+" | ".join(esc(c) for c in r)+" |" for r in rows])
def write(p, t): open(p,"w",encoding="utf-8").write(t.strip()+"\n")
def jdump(n, o): json.dump(o, open(os.path.join(DIRS["json"], n),"w",encoding="utf-8"), ensure_ascii=False, indent=1)
HDR = f"> **GM-24 V7.1 · The Next CISO + Sub-plan PO-GAC** · {FECHA}. Catálogo: {len(CAT)} conceptos (245 K · 52 AMP · 40 HC · 42 PA), todos con pre-ensayo íntegro y mapeados a 17 marcos (NIST/ISACA/MITRE/OWASP/CIS/CSA). V7.1 = ChangeSet editorial CS-GM24-V7.1-001 (4 títulos generalizados; sin cambio de IDs, cantidad ni mapeo). Plano A (corpus académico). Referencias DD/K4x/R/eo:OP/COE: marco interno."
NOTA_INST = "\n\n> **Instancias de dominio (V7.1).** Este pre-ensayo desarrolla la instancia de referencia (productividad: Defender for Office 365). Las instancias XDR, Endpoints, Identidades, Datos, SIEM, Nube y Apps están en los paquetes `Dominio_*` (plano B), que no modifican este concepto.\n"
NOTA_RECON = "> **Nota de reconstrucción (15-nov-2026).** Paquete regenerado desde las fuentes recuperadas del historial de la sesión tras la pérdida del entorno del 14-nov, completado con los lotes 01–08 (240 K), el archivo HC-040 y el Documento Maestro re-adjuntados por el autor. **Los 379 conceptos tienen su pre-ensayo íntegro y los tres documentos GM-24 incluyen el texto V4 original completo (DOCX V4 embebidos en `build/fuentes_GM24/V4_docx/`).**"

def subplan_docs():
    G.OUT = DIRS["docs"]; G.HEADER = HDR
    G.plan(); G.competencias(); G.mapeo(); G.modelo_operativo(); G.gobierno(); G.subplan(); G.agentes(); G.agnostico(); G.conciliacion()
    for f in ("01_Marco_Conceptual_Rol.md", "07_Diagramas_y_Flujos.md"):
        src = os.path.join(BASE, "docs", f)
        if os.path.exists(src): shutil.copy(src, os.path.join(DIRS["docs"], f))
    dm = os.path.join(BASE, "docs", "TheNextCISO_GM-24_Documento_Maestro.md")
    if os.path.exists(dm): shutil.copy(dm, os.path.join(DIRS["GM24_V7.1_docs"], "TheNextCISO_GM-24_Documento_Maestro (original V4).md"))
    write(os.path.join(DIRS["docs"], "10b_Conciliacion_V6_a_V7.1.md"), f"""# 10b · Conciliación V6 → V7 → V7.1

{HDR}

## V6 → V7 (10 candidatos aprobados)
{table(["Candidato","Cambio","Unidad","Resultado"], [(n["candidato"], "Concepto nuevo", n["unidad"], f"{n['id']} {n['concepto']}") for n in V.NUEVOS] + [("V7-C03","Atributo","24 unidades","Columna AAISM"),("V7-C04","Promoción PA→programa","M3.1/M4.2/M4.1",", ".join(V.PROMOVIDOS)),("V7-C09","Referencias por ID","M4.2/M3.2/M6.2/AMP",f"{len(V.REFERENCIAS_ID)} conceptos con referencias versionadas"),("V7-C10","Desarrollo editorial","52 AMP","Pre-ensayos (lotes AMP-01/02/03)")])}

## V7 → V7.1 (ChangeSet editorial CS-GM24-V7.1-001)
{table(["ID","Título V7","Título V7.1"], [(k, v["antes"], v["despues"]) for k, v in TIT.items()])}

Sin cambio de IDs, cantidad (379), pre-ensayos ni mapeo.
""")

def gm24_docs():
    G6.OUT = DIRS["GM24_V7.1_docs"]
    NU = {}
    for n in V.NUEVOS:
        for u in str(n["unidad"]).replace("·", ",").split(","): NU.setdefault(u.strip(), []).append(n)
    def v7note(u24):
        parts = [f"**◆ V7.** AAISM: {V.AAISM_UNIDAD.get(u24,'—')}."]
        if u24 in NU: parts.append("Conceptos nuevos V7: " + "; ".join(f"**{n['id']}** {n['concepto']} ({n['candidato']})" for n in NU[u24]) + ".")
        prom = [p for p in V.PROMOVIDOS if PAX[p][1] == u24]
        if prom: parts.append("PA promovidos al programa (V7-C04): " + ", ".join(prom) + ".")
        gen = [k for k in TIT if PAX[k][1] == u24]
        if gen: parts.append("**◆ V7.1** títulos generalizados: " + "; ".join(f"{k} → «{TIT[k]['despues']}»" for k in gen) + ".")
        parts.append("Las 52 AMP cuentan con idea central desarrollada (lotes AMP-01/02/03).")
        return " ".join(parts)
    old = G6.bloque_v6; G6.bloque_v6 = lambda u: old(u) + " " + v7note(u)
    G6.FRONT = G6.FRONT.rstrip() + f"\n> **V7 ({FECHA})**: 10 candidatos incorporados (5 K nuevos, AMP-52, 4 PA promovidos, AAISM por unidad, referencias por ID, pre-ensayos de las 52 AMP). **V7.1 ({FECHA})**: ChangeSet editorial CS-GM24-V7.1-001 — cuatro títulos generalizados sin cambio de IDs, cantidad (379) ni mapeo. Marcadores ◆ V5/V6/V7/V7.1; el contenido V4 se mantiene íntegro.\n\n{NOTA_RECON}"
    G6.doc_32("Formación CISO_ Gobierno y Gestión_ 7.1.md", "Gobierno y Gestión de la Ciberseguridad - The Next CISO: Propuesta de Estructura Académica — V7.1", G6.INTRO_BASE.replace("◆ V6", "◆ V6/V7/V7.1"), strip=True)
    G6.doc_32("Formación CISO_ Gobierno y Gestión (Versión Actualizada) 7.1.md", "Gobierno y Gestión de la Ciberseguridad - The Next CISO: Propuesta de Estructura Académica (Versión Actualizada) — V7.1", G6.INTRO_ACT.replace("◆ V6", "◆ V6/V7/V7.1"), strip=False)
    G6.doc_24(); G6.anexo_maestro()
    p = os.path.join(G6.OUT, "TheNextCISO_GM-24_Documento_Maestro_Anexo_PO-GAC_V7.1.md")
    s = open(p, encoding="utf-8").read()
    s += "\n\n## 6. ◆ V7 — Conceptos incorporados al programa\n\n" + table(["ID","Tipo","Unidad(es)","Concepto","Candidato","Cierra"], [(n["id"], n["tipo"], n["unidad"], n["concepto"], n["candidato"], n["cierra"]) for n in V.NUEVOS]) + "\n\n**PA promovidos (V7-C04):** " + ", ".join(V.PROMOVIDOS) + ". **AAISM por unidad (V7-C03).** **Referencias por ID (V7-C09).** **Pre-ensayos AMP (V7-C10):** 52.\n\n## 7. ◆ V7.1 — ChangeSet editorial CS-GM24-V7.1-001\n\n" + table(["ID","Título V7","Título V7.1"], [(k, v["antes"], v["despues"]) for k, v in TIT.items()]) + "\n\nSin cambio de IDs, cantidad, pre-ensayos ni mapeo. Instancias de dominio (plano B): Productividad v1.1, XDR, Endpoints, Identidades, Datos, SIEM, Nube v1.0.\n"
    open(p, "w", encoding="utf-8").write(s)

def meta(cid):
    c = CATX[cid]
    if cid in PAX:
        p = PAX[cid]; return dict(unidad=p[1], nombre=p[2], definicion=p[3], extra=f"**Brecha frente a los 331.** {p[4]}", horas=p[10], comps=", ".join(p[11]), origen=p[12], relaciones=list(p[5]), agn=p[6], ms=p[7], act=p[8], ev=p[9])
    src = SRC.get(cid); nuevo = next((n for n in V.NUEVOS if n["id"]==cid), None)
    afin = (src or {}).get("afin") or (nuevo or {}).get("afin") or ""
    return dict(unidad=c["unidad"], nombre=c["concepto"], definicion=c["tesis"] or E[cid]["tesis"].split(". ")[0] + ".", extra="**Origen.** " + c["origen_version"], horas="—", comps="—", origen=c["origen_version"], relaciones=[(a.strip(),"SE_RELACIONA (afín)") for a in str(afin).split(",") if a.strip()], agn="", ms="", act="", ev="")
def unidad_rel(cid):
    c = CATX[cid]; rels = {}
    if cid in PAX: rels = dict(PAX[cid][5])
    for r in c.get("relaciones_hc", []): rels[r["id"]] = r["predicado"]
    us = {u.strip() for u in str(c["unidad"]).replace("·",",").split(",")}; rows = []
    for o in CAT:
        if o["id"] == cid: continue
        cu = {u.strip() for u in str(o["unidad"]).replace("·",",").split(",")}
        if us & cu: rows.append((o["id"], o["tipo"], o["concepto"], rels.get(o["id"], "misma unidad")))
    for rid, pred in rels.items():
        if rid in CATX and not (us & {u.strip() for u in str(CATX[rid]["unidad"]).replace("·",",").split(",")}): rows.append((rid, CATX[rid]["tipo"], CATX[rid]["concepto"], f"{pred} (otra unidad)"))
    return rows
def pe_md(i, cid):
    e = E[cid]; mm = meta(cid); words = sum(len(e[s].split()) for s in ("tesis","tension","aplicacion","evidencia","puentes"))
    u0 = str(mm["unidad"]).split(" ")[0]; ut = D.UNIT[u0]["title"] if u0 in D.UNIT else ""
    aplic = f"\n\n**Aplicación en el escenario de referencia.** Base agnóstica: {mm['agn']} Implementación Microsoft: {mm['ms']} Actividad: {mm['act']} Evidencia: {mm['ev']}" if mm["agn"] else ""
    tit71 = f" · **Título V7:** {CATX[cid]['titulo_v7']}" if "titulo_v7" in CATX[cid] else ""
    refs = f" · **Referencias por ID (V7-C09):** {CATX[cid]['referencias_id']}" if CATX[cid].get("referencias_id") else ""
    return f"""### {i:03d}. {cid} — {mm['nombre']}

**Unidad:** {mm['unidad']} {ut} · **Tipo:** {CATX[cid]['tipo']} · **Horas (sub-plan):** {mm['horas']} · **Competencias:** {mm['comps']} · **Origen:** {mm['origen']}{tit71}{refs} · **Extensión:** {words} palabras · **Estado:** {CATX[cid]['estado']}; ID curricular, no ESS.

**Definición / idea central.** {mm['definicion']}

{mm['extra']}

**Tesis y sentido para el rol.** {e['tesis']}

**Tensión y límites.** {e['tension']}

**Aplicación formativa (base agnóstica → implementación Microsoft).** {e['aplicacion']}

**Evidencia y evaluación.** {e['evidencia']}

**Puentes.** {e['puentes']}

**Recomendaciones de práctica y ejercitación.**
{chr(10).join(f"{n}. {x}" for n, x in enumerate(e['practica'], 1))}{aplic}

**Próximos pasos.**
{chr(10).join(f"- {x}" for x in e['proximos'])}

**Relación con los conceptos de la(s) unidad(es) {mm['unidad']}.**

{table(["ID","Tipo","Concepto","Relación"], unidad_rel(cid))}

**Pregunta generadora:** {e['pregunta']}{NOTA_INST if cid in TIT else ''}

---
"""
LOTES = [("PA-01",[p[0] for p in D.PA[:24]]),("PA-02",[p[0] for p in D.PA[24:]]),("AMP-01",[f"AMP-{i:02d}" for i in range(1,25)]),("AMP-02",[f"AMP-{i:02d}" for i in range(25,49)]),("AMP-03_V7-01",["AMP-49","AMP-50","AMP-51","AMP-52","G2.1-K11","M3.1-K11","M3.1-K12","M4.1-K11","M4.2-K11"])]
def pre_ensayos():
    n = 0; allj = []
    intro = "**Estado:** ideas centrales para desarrollo editorial; IDs curriculares (asignar `ESS-######` desde el registro SQLite). Estructura de los lotes GM-24 + práctica, próximos pasos y relación con la unidad."
    for lote, ids in LOTES:
        parts = [f"# TheNextCISO GM-24 — Pre-ensayos (archivos de inicialización), lote {lote} (V7.1)\n\n{HDR}\n\n{intro}\n\n## Inventario\n\n" + table(["N.º","ID","Tipo","Unidad","Concepto"], [(f"{n+i+1:03d}", cid, CATX[cid]["tipo"], CATX[cid]["unidad"], CATX[cid]["concepto"]) for i, cid in enumerate(ids)]) + "\n\n---\n"]
        for cid in ids:
            n += 1; parts.append(pe_md(n, cid)); write(os.path.join(DIRS["pre_ensayos/individuales"], f"{cid}.md"), f"# Pre-ensayo · {cid}\n\n{HDR}\n\n" + pe_md(n, cid))
            e = E[cid]; mm = meta(cid)
            allj.append(dict(n=n, lote=lote, id=cid, tipo=CATX[cid]["tipo"], unidad=mm["unidad"], concepto=mm["nombre"], titulo_v7=CATX[cid].get("titulo_v7",""), definicion=mm["definicion"], origen=mm["origen"], relaciones=[dict(id=a, predicado=b) for a,b in mm["relaciones"]], referencias_id=CATX[cid].get("referencias_id",""), **{"ensayo_"+k: e[k] for k in ("tesis","tension","aplicacion","evidencia","puentes","pregunta","practica","proximos")}))
        write(os.path.join(DIRS["pre_ensayos"], f"TheNextCISO GM-24 — Pre-ensayos lote {lote} (V7.1).md"), "\n".join(parts))
    jdump("pre_ensayos_nuevos_V7.1.json", allj)

def pre_ensayos_originales():
    """Archivos de inicialización para los 240 K y 40 HC (texto íntegro de lotes 01–08 y HC-040) + copia de los lotes fuente."""
    out = DIRS["pre_ensayos/originales_K_HC"]; n = 0
    for c in CAT:
        if c["tipo"] not in ("K","HC") or not c.get("texto_completo") or c["id"] in E: continue
        rel = ""
        if c.get("relaciones_hc"): rel = "\n\n**Relaciones explícitas (HC-040):**\n" + "\n".join(f"- `{r['id']}` — `{r['predicado']}`: {r['nota']}" for r in c["relaciones_hc"])
        write(os.path.join(out, f"{c['id']}.md"), f"# Pre-ensayo · {c['id']} — {c['concepto']}\n\n{HDR}\n\n**Unidad:** {c['unidad']} · **Tipo:** {c['tipo']} · **Estado:** {c['estado']} · **Fuente:** {'lotes 01–08' if c['tipo']=='K' else 'HC-040'} (texto original íntegro).\n\n{c['texto_completo']}{rel}\n\n" + (f"**Pregunta generadora:** {c['pregunta']}\n\n" if c.get('pregunta') else "") + f"**Relación con los conceptos de la(s) unidad(es) {c['unidad']}.**\n\n" + table(["ID","Tipo","Concepto","Relación"], unidad_rel(c["id"])) + "\n"); n += 1
    src = os.path.join(HERE, "fuentes_GM24"); dst = os.path.join(DIRS["pre_ensayos"], "lotes_originales_01-08_y_HC-040")
    if os.path.isdir(src): shutil.rmtree(dst, ignore_errors=True); shutil.copytree(src, dst)
    print("pre-ensayos originales:", n)

def clase(c):
    if c["tipo"] != "HC": return {"K":"Exclusivo","AMP":"Ampliación Atlas","PA":"Sub-plan PO-GAC"+(" (promovido)" if c["id"] in V.PROMOVIDOS else "")}[c["tipo"]]
    return V.clase_hc(c)
def catalogo_y_matriz():
    jdump("catalogo_V7.1.json", CAT)
    write(os.path.join(DIRS["docs"], "11_Catalogo_V7.1.md"), f"# Catálogo GM-24 V7.1 — {len(CAT)} conceptos\n\n{HDR}\n\n" + table(["ID","Tipo","Clase","Unidad(es)","Concepto (V7.1)","Título V7 (si cambió)","Estado","Origen / versión","AAISM","Pregunta generadora"], [(c["id"], c["tipo"], clase(c), c["unidad"], c["concepto"], c.get("titulo_v7",""), c["estado"], c["origen_version"], c["aaism"], c.get("pregunta","")) for c in CAT]))
    rows = M.build_matrix(CAT); cov = M.coverage(rows)
    jdump("matriz_mapeo_V7.1.json", [{k:v for k,v in r.items() if not k.startswith("_raw_") and k not in ("texto_completo","relaciones_hc")} | {"mapeo": {fw: [dict(elemento=e, nombre=S.NAMES.get(e,e), vinculo=v, nivel=n) for e,v,n in r["_raw_"+fw]] for fw in M.F if r["_raw_"+fw]}} for r in rows])
    jdump("cobertura_por_elemento_V7.1.json", [dict(framework=fw, elemento=e, nombre=S.NAMES.get(e,e), fuertes=h["Fuerte"], parciales=h["Parcial"], informativos=h["Informativo"]) for (fw,e),h in cov.items()])
    jdump("estandares_referencia.json", dict(fuentes=S.FUENTES, elementos={fw:[dict(id=e, nombre=S.NAMES.get(e,e)) for e in els] for fw,els in S.FRAMEWORK_ELEMENTS.items()}))
    resumen = [(fw, len(els), sum(1 for e in els if cov[(fw,e)]["Fuerte"]), sum(1 for e in els if not cov[(fw,e)]["Fuerte"] and (cov[(fw,e)]["Parcial"] or cov[(fw,e)]["Informativo"])), sum(1 for e in els if not (cov[(fw,e)]["Fuerte"] or cov[(fw,e)]["Parcial"] or cov[(fw,e)]["Informativo"]))) for fw, els in S.FRAMEWORK_ELEMENTS.items()]
    met = f"# Mapeo GM-24 V7.1 ({len(rows)} conceptos) → NIST · ISACA · MITRE · OWASP · CIS · CSA\n\n{HDR}\n\n## 1. Método\n\nHerencia de unidad (◐ Parcial) → reglas por palabra clave sobre K ({len(M.K_RULES)} reglas; 245/245) → explícitos AMP (52), HC (40), PA (42). Vínculo: cubre | instancia | referencia. No afirma conformidad (AMP-08). IDs validados contra `estandares.py` (0 desconocidos). **V7.1 no cambia el mapeo.**\n\n## 2. Marcos y fuentes\n\n" + table(["Clave","Marco / versión","Fuente"], [(k,v[0],v[1]) for k,v in S.FUENTES.items()]) + "\n\n## 3. Resumen de cobertura\n\n" + table(["Marco","Elementos","Con fuerte","Solo parcial/informativa","Sin cobertura"], resumen) + "\n\nResidual sin cobertura fuerte: GAI-CBRN y GAI-Env (AI 600-1), declarados fuera del alcance del rol en AMP-52.\n\n## 4. Cobertura por elemento\n"
    for fw, els in S.FRAMEWORK_ELEMENTS.items():
        met += f"\n### {fw}\n\n" + table(["Elemento","Nombre","Fuerte (n)","Fuerte (IDs)","Parcial (n)"], [(e, S.NAMES.get(e,e), len(cov[(fw,e)]["Fuerte"]), ", ".join(cov[(fw,e)]["Fuerte"][:25])+(" …" if len(cov[(fw,e)]["Fuerte"])>25 else ""), len(cov[(fw,e)]["Parcial"])) for e in els]) + "\n"
    write(os.path.join(DIRS["mapeo"], "00_Metodo_y_Cobertura_V7.1.md"), met)
    for tipo, titulo in [("K","01_Matriz_K"),("AMP","02_Matriz_AMP"),("HC","03_Matriz_HC"),("PA","04_Matriz_PA")]:
        rr = [r for r in rows if r["tipo"]==tipo]
        write(os.path.join(DIRS["mapeo"], titulo+".md"), f"# Matriz V7.1 — {tipo} ({len(rr)})\n\n{HDR}\n\n● Fuerte · ◐ Parcial · ○ Informativo; (cubre | instancia | referencia).\n\n" + table(["ID","Unidad(es)","Concepto","Método","N.º fuertes"]+M.F, [[r["id"],r["unidad"],r["concepto"],r["metodo"],r["n_fuertes"]]+[r[fw] for fw in M.F] for r in rr]))
    return rows, cov, resumen

def informes(resumen):
    cnt = collections.Counter(c["tipo"] for c in CAT); hc = collections.Counter(clase(c) for c in CAT if c["tipo"]=="HC")
    pilar = collections.Counter(("Gobierno" if str(c["unidad"]).startswith("G") else "Gestión") for c in CAT)
    write(os.path.join(DIRS["informe"], "Informe_de_Cambios_V4_a_V7.1.md"), f"""# Informe de cambios GM-24: de la V4 a la V7.1

{HDR}

{NOTA_RECON}

## 1. Línea de tiempo
| Versión | Base | Qué cambió | Fuente |
|---|---|---|---|
| **V4** | 240 K; 51 AMP como títulos; 32 unidades → 12 ejes / 24 unidades; 800 h | Estructura académica, Versión Actualizada, 24 Clases; Documento Maestro; lotes 01–08; HC-040 | `Formación CISO_… 4.docx` (×3), Matrices_Curriculares, Documento Maestro |
| **V5** | 240 K | Eje PO-GAC: 67 PA (316 h), 41 competencias, 31 tareas MDO, 15 agentes, 24 AGC, 20 KPIs | Sub-plan V5 |
| **V6** | 331 (240 K + 51 AMP + 40 HC) | 23 PA retirados (cubiertos por AMP/HC), 2 fusionados → 42 PA con pre-ensayo; lente sobre 91; tres rutas; documentos GM-24 V6 | Sub-plan V6 |
| **V6-R** | 373 | Anexos de agentes; pre-ensayos como archivos de inicialización; mapeo a 17 marcos; 11 inconsistencias; 10 candidatos | Paquete V6-R |
| **V7** | **379** (245 K + 52 AMP + 40 HC + 42 PA) | 10 candidatos incorporados; 57 pre-ensayos nuevos; matriz rehecha; documentos GM-24 V7 | Paquete V7 |
| **V7.1** | 379 | ChangeSet editorial: 4 títulos generalizados tras las instancias de dominio; sin cambio de IDs, cantidad ni mapeo; 7 instancias de dominio (plano B) | Este paquete |

## 2. Incorporado
- Conceptos nuevos V7: {", ".join(n["id"] for n in V.NUEVOS)}. PA promovidos: {", ".join(V.PROMOVIDOS)}. AAISM por unidad. Referencias por ID ({len(V.REFERENCIAS_ID)}). Pre-ensayos de las 52 AMP.
- Sub-plan PO-GAC completo y siete instancias de dominio en el plano B (Productividad v1.1, XDR, Endpoints, Identidades, Datos, SIEM, Nube, Apps v1.0).

## 3. Modificado
{table(["Elemento","V4","V7.1"], [("Base","240 K",f"{len(CAT)} con pre-ensayo íntegro"),("Mapeo","por unidad (CISM/CRISC/CSF/RMF)","por concepto, 17 marcos, 3 niveles, método trazable"),("AMP","títulos","idea central desarrollada"),("4 PA promovidos","títulos específicos de correo (V7)","títulos de dominio (V7.1)"),("Documentos GM-24","3 (V4) + Documento Maestro","3 + Anexo PO-GAC (V7.1, V4 íntegro + ◆ V5/V6/V7/V7.1) + Documento Maestro original")])}

## 4. Eliminado o retirado
- Ningún K, AMP ni HC del GM-24 original fue eliminado. 23 PA de V5 retirados en V6 con trazabilidad (`docs/10_Conciliacion_V5_a_V6.md`).

## 5. ChangeSet V7.1
{table(["ID","Antes (V7)","Después (V7.1)"], [(k, v["antes"], v["despues"]) for k, v in TIT.items()])}

## 6. Cobertura de marcos (V7.1 = V7)
{table(["Marco","Elementos","Con fuerte","Solo parcial/informativa","Sin cobertura"], resumen)}
""")
    write(os.path.join(DIRS["informe"], "Resumen_Ejecutivo_V7.1.md"), f"""# Resumen ejecutivo — GM-24 V7.1

{HDR}

## 1. Qué es
La V7.1 consolida el corpus que alimentará la taxonomía, la ontología y el grafo del MCP Server: **{len(CAT)} conceptos, cada uno con pre-ensayo íntegro y mapeado a 17 marcos**. Integra el sub-plan PO-GAC y se usa, sin modificarse, como marco de gobierno de capacidades contratadas en ocho instancias de dominio (plano B).

## 2. Inventario
| Clase | Cantidad | Pre-ensayo |
|---|---|---|
| Exclusivos (K) | {cnt['K']} | 240 (lotes 01–08, texto íntegro) + 5 (lote V7-01) |
| Ampliaciones Atlas (AMP) | {cnt['AMP']} | lotes AMP-01/02/03 |
| HC híbridos intra-pilar | {hc.get('Híbrido (intra-pilar)',0)} | HC-040 (texto íntegro) |
| HC vinculantes / puente G↔M | {hc.get('Vinculante (puente G↔M)',0)} | HC-040 (texto íntegro) |
| HC integradores (≥4 unidades) | {hc.get('Integrador',0)} | HC-040 (texto íntegro) |
| Sub-plan PO-GAC (PA) | {cnt['PA']} | lotes PA-01/02 (4 promovidos; 4 títulos generalizados en V7.1) |
| **Total** | **{len(CAT)}** | **{len(CAT)}** · Gobierno {pilar['Gobierno']} · Gestión {pilar['Gestión']} |

Complementos: 41 competencias en 8 dominios; 31 tareas del modelo operativo de referencia; 15 agentes con anexos; 24 AGC; 20 KPIs; AAISM en 24 unidades.

## 3. Mapeo a organizaciones y artefactos
{table(["Marco","Elementos","Con fuerte","Solo parcial/informativa","Sin cobertura"], resumen)}

Residual: GAI-CBRN y GAI-Env, fuera de alcance declarado (AMP-52). Planilla especial: `GM24_V7.1_Matriz_Estandares.xlsx`.

## 4. V4 → V7.1 en una línea
240 K (V4) → + eje PO-GAC (V5) → base 331 y 42 PA (V6) → anexos, mapeo, candidatos (V6-R) → 379 con pre-ensayo y mapeo (V7) → 4 títulos generalizados + 7 dominios (V7.1). **Nada del GM-24 original fue eliminado.**

## 5. Pendientes del programa
D07 (horas), D10 (licencias/preview), asignación de ESS a los 99 pre-ensayos nuevos, ChangeSets al Atlas.

{NOTA_RECON}
""")

def xlsx(rows, cov):
    from openpyxl import Workbook
    from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
    from openpyxl.utils import get_column_letter
    FONT="Arial"; HF=PatternFill("solid",fgColor="17354F"); HFont=Font(name=FONT,bold=True,color="FFFFFF",size=10); BF=Font(name=FONT,size=9); TH=Side(style="thin",color="D0D7E2"); BR=Border(left=TH,right=TH,top=TH,bottom=TH)
    wb=Workbook(); wb.remove(wb.active)
    def sheet(name, headers, rws, widths=None, freeze="A2"):
        ws=wb.create_sheet(name[:31]); ws.append(headers)
        for r in rws: ws.append([("" if v is None else (", ".join(map(str,v)) if isinstance(v,(list,tuple)) else v)) for v in r])
        for c in range(1,len(headers)+1):
            cell=ws.cell(row=1,column=c); cell.fill=HF; cell.font=HFont; cell.alignment=Alignment(vertical="center",wrap_text=True); cell.border=BR
        for row in ws.iter_rows(min_row=2,max_row=ws.max_row,max_col=len(headers)):
            for cell in row: cell.font=BF; cell.alignment=Alignment(vertical="top",wrap_text=True); cell.border=BR
        for i,w in enumerate(widths or [18]*len(headers),1): ws.column_dimensions[get_column_letter(i)].width=w
        ws.row_dimensions[1].height=34; ws.freeze_panes=freeze; ws.auto_filter.ref=f"A1:{get_column_letter(len(headers))}{ws.max_row}"; ws.sheet_view.showGridLines=False
    pe = json.load(open(os.path.join(DIRS["json"],"pre_ensayos_nuevos_V7.1.json"),encoding="utf-8"))
    sheet("00_Leeme",["Campo","Contenido"],[("GM-24 V7.1 · Matriz de estándares",FECHA),("Base",f"{len(CAT)} conceptos con pre-ensayo íntegro; V7.1 = 4 títulos generalizados (CS-GM24-V7.1-001)"),("Gemelos","json/ y mapeo/ generados por build/gen_v71_full.py"),("Leyenda","● Fuerte · ◐ Parcial · ○ Informativo; (cubre | instancia | referencia)"),("Advertencia","El mapeo no afirma conformidad (AMP-08). DD/K4x/R/eo:OP/COE: marco interno."),("Reconstrucción","Regenerado el 15-nov-2026; incluye el texto íntegro de los 331 pre-ensayos originales + 99 nuevos.")],[24,150])
    sheet("01_Catalogo_V7.1",["ID","Tipo","Clase","Unidad(es)","Concepto (V7.1)","Título V7","Estado","Origen","AAISM","Referencias por ID","Pregunta generadora","Pre-ensayo (texto íntegro)"],[(c["id"],c["tipo"],clase(c),c["unidad"],c["concepto"],c.get("titulo_v7",""),c["estado"],c["origen_version"],c["aaism"],c.get("referencias_id",""),c.get("pregunta",""),c.get("texto_completo","")) for c in CAT],[11,6,20,14,40,34,34,20,10,40,50,120],freeze="E2")
    sheet("02_Matriz_Mapeo",["ID","Tipo","Unidad(es)","Concepto","Método","N.º fuertes"]+M.F,[[r["id"],r["tipo"],r["unidad"],r["concepto"],r["metodo"],r["n_fuertes"]]+[r[fw] for fw in M.F] for r in rows],[11,6,14,32,24,7]+[30]*len(M.F),freeze="E2")
    sheet("03_Cobertura_Elemento",["Marco","Elemento","Nombre","Fuerte (n)","Fuerte (IDs)","Parcial (n)","Parcial (IDs)"],[(fw,e,S.NAMES.get(e,e),len(h["Fuerte"]),", ".join(h["Fuerte"]),len(h["Parcial"]),", ".join(h["Parcial"])) for (fw,e),h in cov.items()],[20,24,40,8,70,8,60],freeze="C2")
    sheet("04_Resumen_Cobertura",["Marco","Elementos","Con fuerte","Solo parcial/informativa","Sin cobertura"],[(fw,len(els),sum(1 for e in els if cov[(fw,e)]["Fuerte"]),sum(1 for e in els if not cov[(fw,e)]["Fuerte"] and (cov[(fw,e)]["Parcial"] or cov[(fw,e)]["Informativo"])),sum(1 for e in els if not (cov[(fw,e)]["Fuerte"] or cov[(fw,e)]["Parcial"] or cov[(fw,e)]["Informativo"]))) for fw,els in S.FRAMEWORK_ELEMENTS.items()],[26,10,10,16,12])
    sheet("05_Estandares_Ref",["Marco","Elemento","Nombre"],[(fw,e,S.NAMES.get(e,e)) for fw,els in S.FRAMEWORK_ELEMENTS.items() for e in els],[24,26,60],freeze="B2")
    sheet("06_AAISM_por_Unidad",["Unidad","Título","Pilar","CSF","CISM","CRISC","RMF","AAISM (V7)"],[(u["id"],u["title"],u["pilar"],u["csf"],u["cism"],u["crisc"],u["rmf"],V.AAISM_UNIDAD[u["id"]]) for u in D.UNITS],[7,44,9,18,10,10,18,12])
    sheet("07_ChangeSet_V7.1",["ID","Título V7","Título V7.1"],[(k,v["antes"],v["despues"]) for k,v in TIT.items()],[11,60,90])
    sheet("08_PreEnsayos_Nuevos",["N.º","Lote","ID","Tipo","Unidad","Concepto","Título V7","Definición","Origen","Relaciones","Referencias","Tesis","Tensión","Aplicación","Evidencia","Puentes","Práctica","Próximos","Pregunta"],[(p["n"],p["lote"],p["id"],p["tipo"],p["unidad"],p["concepto"],p["titulo_v7"],p["definicion"],p["origen"],"; ".join(f"{r['id']} ({r['predicado']})" for r in p["relaciones"]),p["referencias_id"],p["ensayo_tesis"],p["ensayo_tension"],p["ensayo_aplicacion"],p["ensayo_evidencia"],p["ensayo_puentes"]," | ".join(p["ensayo_practica"])," | ".join(p["ensayo_proximos"]),p["ensayo_pregunta"]) for p in pe],[5,10,11,6,12,30,30,50,20,36,36,60,60,60,50,46,60,50,50],freeze="D2")
    sheet("08b_PreEnsayos_Originales",["ID","Tipo","Unidad","Concepto","Estado","Pregunta","Relaciones HC","Texto íntegro"],[(c["id"],c["tipo"],c["unidad"],c["concepto"],c["estado"],c.get("pregunta",""),"; ".join(f"{r['id']} ({r['predicado']})" for r in c.get("relaciones_hc",[])),c.get("texto_completo","")) for c in CAT if c["tipo"] in ("K","HC") and c["id"] not in E],[11,6,10,36,30,50,40,120],freeze="D2")
    sheet("09_Lente_PO-GAC",["ID","Unidad","Concepto","Horas","Lectura","Instrumento","Competencias"],[(l[0],l[1],CATX.get(l[0],{}).get("concepto",""),l[2],l[3],l[4],", ".join(l[5])) for l in D.LENTE],[10,7,36,6,60,40,16])
    sheet("10_Competencias",["ID","Dominio","Competencia","Niveles","Conceptos"],[(c[0],c[1],c[2],c[3],", ".join(c[4])) for c in D.COMPETENCIAS],[7,6,60,60,40])
    sheet("11_AGC",["ID","Capa","Control","Objetivo","AI RMF","ISO 42001","OWASP ASI","Implementación MS","Base agnóstica","Evidencia","Responsable"],D.CONTROLES,[8,10,30,40,10,8,8,36,20,16,14])
    sheet("12_Fuentes",["Clave","Marco / versión","Fuente"],[(k,v[0],v[1]) for k,v in S.FUENTES.items()],[14,90,70])
    wb.save(os.path.join(ROOT, "GM24_V7.1_Matriz_Estandares.xlsx"))

def html71(rows):
    DOCS = DIRS["docs"]; G7D = DIRS["GM24_V7.1_docs"]; PRE = DIRS["pre_ensayos"]; MAP = DIRS["mapeo"]; INF = DIRS["informe"]
    GH.SECTIONS = [("inicio","Inicio",None),("resumen","Resumen ejecutivo V7.1",os.path.join(INF,"Resumen_Ejecutivo_V7.1.md")),("cambios","Informe de cambios V4 → V7.1",os.path.join(INF,"Informe_de_Cambios_V4_a_V7.1.md")),("estrategia","Estrategia de anexos y separación de planos",os.path.join(BASE,"Estrategia_Anexos_Tecnologicos_y_Separacion_de_Planos.md")),("comparativa","Comparativa de 8 dominios (plano B)",os.path.join(BASE,"Comparativa_8_Dominios_PO-GAC.md")),("guia","Guía de reconstrucción",os.path.join(BASE,"GUIA_DE_RECONSTRUCCION.md"))]
    for sid, title, fn in [("plan","00 · Plan de trabajo","00_Plan_de_Trabajo.md"),("rol","01 · Marco conceptual del rol","01_Marco_Conceptual_Rol.md"),("competencias","02 · Competencias","02_Marco_de_Competencias.md"),("mapeogm","03 · Mapeo GM-24 y gap","03_Mapeo_GM24_y_Gap.md"),("operativo","04 · Modelo operativo MDO/XDR","04_Modelo_Operativo_MDO_XDR.md"),("gobierno","05 · Gobierno y gestión de agentes","05_Gobierno_y_Gestion_de_Agentes.md"),("subplan","06 · Sub-plan de desarrollo","06_Subplan_de_Desarrollo.md"),("diagramas","07 · Diagramas y flujos","07_Diagramas_y_Flujos.md"),("agentes","08 · Catálogo de agentes","08_Catalogo_Agentes.md"),("agnostico","09 · Agnóstico vs Microsoft","09_Bases_Agnosticas_vs_Microsoft.md"),("conc56","10 · Conciliación V5 → V6","10_Conciliacion_V5_a_V6.md"),("conc67","10b · Conciliación V6 → V7 → V7.1","10b_Conciliacion_V6_a_V7.1.md")]:
        p = os.path.join(DOCS, fn)
        if os.path.exists(p): GH.SECTIONS.append((sid, title, p))
    GH.SECTIONS += [("catalogo","11 · Catálogo V7.1 (interactivo, 379 con texto)",None),("preensayos","Pre-ensayos (379: 280 originales + 99 nuevos)",None),("estandares","Mapeo a estándares: método y cobertura",os.path.join(MAP,"00_Metodo_y_Cobertura_V7.1.md")),("autoeval","Autoevaluación (interactiva)",None),
        ("v71base","GM-24 V7.1 · Estructura (32 unidades)",os.path.join(G7D,"Formación CISO_ Gobierno y Gestión_ 7.1.md")),("v71act","GM-24 V7.1 · Versión Actualizada",os.path.join(G7D,"Formación CISO_ Gobierno y Gestión (Versión Actualizada) 7.1.md")),("v7124","GM-24 V7.1 · 24 Clases / 12 Ejes",os.path.join(G7D,"Formación CISO_ Gobierno y Gestión (Estructura 24 Clases) 7.1.md")),("anexo","Anexo PO-GAC al Documento Maestro V7.1",os.path.join(G7D,"TheNextCISO_GM-24_Documento_Maestro_Anexo_PO-GAC_V7.1.md")),("maestro","Documento Maestro GM-24 (original)",os.path.join(G7D,"TheNextCISO_GM-24_Documento_Maestro (original V4).md"))]
    for key in ["PRODUCTIVIDAD","XDR","ENDPOINTS","IDENTIDADES","DATOS","SIEM","NUBE","APPS"]:
        for fn in sorted(glob.glob(os.path.join(BASE, f"Dominio_{key}", "0*.md"))):
            GH.SECTIONS.append((f"dom_{key.lower()}_{os.path.basename(fn)[:2]}", f"Dominio {key.title()} · {os.path.basename(fn)[3:-3].replace('_',' ')}", fn))
    GH.SECTIONS.append(("descargas","Descargas (Markdown y fuentes)",None))
    def catalogo():
        data=[dict(id=r["id"],tipo=r["tipo"],unidad=str(r["unidad"]),concepto=r["concepto"],estado=r["estado"],usado="Sí",horas=0,lectura=(r.get("texto_completo") or r["tesis"])[:1500],instrumento=r.get("titulo_v7",""),rel=r["metodo"],prio=f"fuertes: {r['n_fuertes']}",origen=r["origen_version"]) for r in rows]
        return f"""<h1>Catálogo GM-24 V7.1 — {len(data)} conceptos</h1><p>"Tesis" muestra el inicio del pre-ensayo íntegro; "Instrumento" el título V7 cuando cambió en V7.1; "Prioridad" el número de mapeos fuertes.</p><div class="toolbar"><label>Tipo <select id="cat-tipo"><option value="">Todos</option><option>K</option><option>AMP</option><option>HC</option><option>PA</option></select></label><label>Unidad <select id="cat-unidad"><option value="">Todas</option>{''.join(f'<option>{u["id"]}</option>' for u in D.UNITS)}</select></label><label>Usado <select id="cat-usado"><option value="">Todos</option><option>Sí</option></select></label><label>Prioridad <select id="cat-prio"><option value="">Todas</option></select></label><input id="cat-q" type="search" placeholder="Buscar…"><span id="cat-count" class="pill"></span></div><div id="cat-table"></div><script id="cat-data" type="application/json">{json.dumps(data, ensure_ascii=False)}</script>"""
    def preensayos():
        data=[]; i=0
        for c in CAT:
            i+=1; cid=c["id"]
            if cid in E:
                e=E[cid]; mm=meta(cid)
                data.append(dict(n=i,id=cid,unidad=str(mm["unidad"]),nombre=mm["nombre"],definicion=mm["definicion"],brecha=mm["extra"].replace("**",""),rel="; ".join(f"{a} ({b})" for a,b in mm["relaciones"]),horas=mm["horas"],comps=mm["comps"],origen=mm["origen"],tipo=c["tipo"],tesis=e["tesis"],tension=e["tension"],aplicacion=e["aplicacion"],evidencia=e["evidencia"],puentes=e["puentes"],pregunta=e["pregunta"],practica=" | ".join(e["practica"]),proximos=" | ".join(e["proximos"])))
            else:
                data.append(dict(n=i,id=cid,unidad=str(c["unidad"]),nombre=c["concepto"],definicion=c.get("tesis",""),brecha="Fuente: "+("lotes 01–08" if c["tipo"]=="K" else "HC-040")+" (texto original íntegro)",rel="; ".join(f"{r['id']} ({r['predicado']})" for r in c.get("relaciones_hc",[])),horas="—",comps="—",origen=c["origen_version"],tipo=c["tipo"],tesis=c.get("texto_completo",""),tension="",aplicacion="",evidencia="",puentes="",pregunta=c.get("pregunta",""),practica="",proximos=""))
        units=sorted({d["unidad"] for d in data})
        return f"""<h1>Pre-ensayos — {len(data)} conceptos (280 originales con texto íntegro + 99 nuevos V5–V7.1)</h1><div class="toolbar"><label>Tipo <select id="pe-tipo"><option value="">Todos</option><option>K</option><option>AMP</option><option>HC</option><option>PA</option></select></label><label>Unidad <select id="pe-unidad"><option value="">Todas</option>{''.join(f'<option>{H.escape(u)}</option>' for u in units)}</select></label><input id="pe-q" type="search" placeholder="Buscar…"><span id="pe-count" class="pill"></span></div><div id="pe-list"></div><script id="pe-data" type="application/json">{json.dumps(data, ensure_ascii=False)}</script>"""
    def descargas():
        files=[]
        for pat in [os.path.join(DOCS,"*.md"),os.path.join(G7D,"*.md"),os.path.join(PRE,"*.md"),os.path.join(PRE,"lotes_originales_01-08_y_HC-040","*.md"),os.path.join(MAP,"*.md"),os.path.join(INF,"*.md"),os.path.join(ROOT,"README.md"),os.path.join(HERE,"*.py"),os.path.join(HERE,"*.json"),os.path.join(DIRS["json"],"*.json"),os.path.join(BASE,"Dominio_*","*.md"),os.path.join(BASE,"Dominio_*","json","*.json"),os.path.join(BASE,"*.md"),os.path.join(BASE,"V7.1","*.md"),os.path.join(BASE,"V7.1","json","*.json"),os.path.join(BASE,"docs","0*.md")]:
            files+=sorted(glob.glob(pat))
        seen=set(); items=[]
        for f in files:
            if f in seen: continue
            seen.add(f); rel=os.path.relpath(f, BASE).replace(os.sep,"/"); data=open(f,"rb").read(); mime="text/markdown" if f.endswith(".md") else ("application/json" if f.endswith(".json") else "text/plain")
            items.append(f'<li><a download="{H.escape(os.path.basename(f))}" href="data:{mime};charset=utf-8;base64,{base64.b64encode(data).decode("ascii")}">{H.escape(rel)}</a> <span class="tcount">{len(data)//1024+1} KB</span></li>')
        return f"<h1>Descargas (V7.1): corpus, pre-ensayos (incl. lotes originales 01–08 y HC-040), mapeo, informes, 7 dominios, guía y generadores</h1><p>Todo embebido como data-URI. Para reconstruir: descargar los <code>.py</code> y <code>.json</code> a <code>build/</code> y ejecutar <code>python make_all.py</code> (ver Guía).</p><ul class=\"dl\">{''.join(items)}</ul>"
    def inicio():
        return f"""<h1>GM-24 V7.1 · The Next CISO + Sub-plan PO-GAC</h1><p class="lead">379 conceptos con pre-ensayo íntegro y mapeo a 17 marcos; V7.1 aplica el ChangeSet editorial CS-GM24-V7.1-001. Plano A = corpus académico; plano B = ocho instancias de dominio.</p><div class="cards"><div class="card"><div class="num">379</div><div class="lbl">conceptos con pre-ensayo</div></div><div class="card"><div class="num">280 + 99</div><div class="lbl">pre-ensayos originales + nuevos</div></div><div class="card"><div class="num">17</div><div class="lbl">marcos mapeados</div></div><div class="card"><div class="num">8</div><div class="lbl">instancias de dominio</div></div><div class="card"><div class="num">4</div><div class="lbl">títulos generalizados (V7.1)</div></div></div><blockquote>{H.escape(NOTA_RECON.lstrip('> '))}</blockquote>"""
    GH.catalogo=catalogo; GH.preensayos=preensayos; GH.descargas=descargas; GH.inicio=inicio
    GH.OUT = os.path.join(ROOT, "GM24_V7.1_PO_Agentes.html"); GH.build()

if __name__ == "__main__":
    subplan_docs(); gm24_docs(); pre_ensayos(); pre_ensayos_originales(); rows, cov, resumen = catalogo_y_matriz(); informes(resumen); xlsx(rows, cov); html71(rows)
    write(os.path.join(ROOT,"README.md"), f"# GM-24 V7.1 — paquete completo del corpus (plano A)\n\n{HDR}\n\n{NOTA_RECON}\n\n- informe/ · GM24_V7.1_docs/ (3 documentos GM-24 + Anexo PO-GAC + Documento Maestro original) · docs/ (00–11) · pre_ensayos/ (5 lotes nuevos + 99 individuales + 280 originales_K_HC + lotes fuente) · mapeo/ · json/ · GM24_V7.1_Matriz_Estandares.xlsx · GM24_V7.1_PO_Agentes.html.\n- Regenerar: `python build/make_all.py`.\n")
    print("DONE V7.1")

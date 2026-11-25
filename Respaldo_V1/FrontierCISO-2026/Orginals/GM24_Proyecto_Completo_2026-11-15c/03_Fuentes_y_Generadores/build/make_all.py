# -*- coding: utf-8 -*-
"""Orquestador de reconstrucción completa del proyecto GM-24 (plano A V7.1 + plano B 7 dominios).
Uso: python make_all.py [--docx] [--xlsx-recalc]
Requiere: Python 3.10+, openpyxl, pandoc (texto V4 desde los DOCX; DOCX de salida). Opcional: LibreOffice.
Variables: V4_DIR (carpeta con los 3 DOCX V4; por defecto /mnt/data, luego ../04_Insumos_Externos).
Salida: ../GM24_V7.1/, ../Dominio_*/, ../Estrategia_*.md, ../Comparativa_*.md, ../V7.1/, ../MANIFEST_SHA256.txt."""
import os, sys, subprocess, shutil, glob, json, hashlib
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, ".."))
os.chdir(HERE); sys.path.insert(0, HERE)
DOCX = "--docx" in sys.argv; RECALC = "--xlsx-recalc" in sys.argv
if not os.environ.get("V4_DIR"):
    for cand in (os.path.join(HERE, "fuentes_GM24", "V4_docx"), "/mnt/user-data/uploads", "/mnt/data", os.path.join(ROOT, "04_Insumos_Externos"), os.path.join(ROOT, "..", "04_Insumos_Externos")):
        if glob.glob(os.path.join(cand, "Formación CISO_*4.docx")): os.environ["V4_DIR"] = cand; break
def step(msg): print(f"\n=== {msg}", flush=True)

step("0. Verificación de fuentes")
req = ["apps.py","data.py","pa_v6.py","v7.py","ensayos_pa_1.py","ensayos_pa_2.py","ensayos_pa_3.py","ensayos_amp_1.py","ensayos_amp_2.py","ensayos_amp_3.py","practica.py","estandares.py","mapeo.py","anexos.py","xdr.py","dominios.py","dominios2.py","datos.py","gen_md.py","gen_v6.py","gen_html.py","gen_v71_full.py","gen_dominios.py","gen_xdr.py","gen_v71_estrategia.py","catalogo331.json","hc_rel.json","gm24_base.json","v71_titulos.json"]
missing = [f for f in req if not os.path.exists(f)]
if missing: sys.exit(f"Faltan fuentes: {missing}")
import pa_v6
TIT = json.load(open("v71_titulos.json", encoding="utf-8"))
bad = [k for k in TIT if not any(p[0]==k and p[2]==TIT[k]["despues"] for p in pa_v6.PA)]
if bad: sys.exit(f"pa_v6.py no tiene los títulos V7.1 aplicados en: {bad}")
cat = json.load(open("catalogo331.json", encoding="utf-8")); print(f"Fuentes OK; títulos V7.1 presentes; catálogo 331 con texto íntegro en {sum(1 for c in cat if c.get('texto_completo'))} conceptos.")
docs_dir = os.path.join(ROOT, "docs"); os.makedirs(docs_dir, exist_ok=True)
for f in ("01_Marco_Conceptual_Rol.md", "07_Diagramas_y_Flujos.md"):
    if not os.path.exists(os.path.join(docs_dir, f)): print(f"AVISO: falta docs/{f} (narrativo); se omitirá en el HTML.")
if shutil.which("pandoc") is None: print("AVISO: pandoc no disponible; los documentos GM-24 no incluirán el texto V4 y no se generarán DOCX.")
print("V4_DIR =", os.environ.get("V4_DIR", "(no encontrado)"))

step("1. Dominio XDR (plano B)")
subprocess.run([sys.executable, "gen_xdr.py"], check=True)

step("2. Dominios Endpoints, Identidades, Datos, SIEM, Nube, Productividad v1.1 (plano B)")
import dominios as DM, dominios2 as D2, datos as DT, apps as AP, gen_dominios as G, anexos as A
DM.TOOLS.update(D2.TOOLS); DM.TOOLS.update(DT.TOOLS); DM.TOOLS.update(AP.TOOLS); G.TOOLS.update(D2.TOOLS); G.TOOLS.update(DT.TOOLS); G.TOOLS.update(AP.TOOLS)
DM.DOMINIOS["DATOS"] = dict(prefijo="DP", agente="DA", nombre=DT.FICHA["nombre"], dominio_zt=DT.FICHA["dominio_zt"], tecnologia=DT.FICHA["tecnologia"], funciones_csf=DT.FICHA["funciones_csf"], fuente_oficial=DT.FICHA["fuente_oficial"], objetivo=DT.FICHA["objetivo"], slo=DT.FICHA["slo"], diferencia=DT.FICHA["diferencia_vs_otros"], interfaz=DT.FICHA["interfaz"], personas=DT.FICHA["personas"], permisos=DT.FICHA["permisos"], tareas=DT.TAREAS, agentes=DT.AGENTES, knowledge=DT.KNOWLEDGE, skills=DT.SKILLS, instancia=DT.INSTANCIA)
prod = D2.PROD; prod["agentes"] = [tuple(list(a[:12]) + [A.AG[a[0]]["tools"], A.AG[a[0]]["knowledge"], A.AG[a[0]]["skills"]]) for a in prod["agentes"]]
DM.DOMINIOS["SIEM"] = D2.SIEM; DM.DOMINIOS["NUBE"] = D2.NUBE; DM.DOMINIOS["PRODUCTIVIDAD"] = prod
DM.DOMINIOS["APPS"] = dict(prefijo="AP", agente="PA", nombre=AP.FICHA["nombre"], dominio_zt=AP.FICHA["dominio_zt"], tecnologia=AP.FICHA["tecnologia"], funciones_csf=AP.FICHA["funciones_csf"], fuente_oficial=AP.FICHA["fuente_oficial"], objetivo=AP.FICHA["objetivo"], slo=AP.FICHA["slo"], diferencia=AP.FICHA["diferencia_vs_otros"], interfaz=AP.FICHA["interfaz"], personas=AP.FICHA["personas"], permisos=AP.FICHA["permisos"], tareas=AP.TAREAS, agentes=AP.AGENTES, knowledge=AP.KNOWLEDGE, skills=AP.SKILLS, instancia=AP.INSTANCIA, hitos=AP.HITOS)
VERS = {"PRODUCTIVIDAD": "v1.1 (re-emisión en formato uniforme de la instancia V5/V6)"}
res = {}
for key in ("ENDPOINTS","IDENTIDADES","DATOS","SIEM","NUBE","APPS","PRODUCTIVIDAD"): res[key] = G.build(key, VERS.get(key, "v1.0"))
G.v71_y_comparativa(res)

step("3. Estrategia de anexos y ChangeSet V7.1")
subprocess.run([sys.executable, "gen_v71_estrategia.py"], check=True)

step("4. Comparativa de 8 dominios")
rows = []
for key, nm, tec, ver in [("PRODUCTIVIDAD","Productividad","Defender for Office 365 (EOP) en Defender XDR","v1.1"),("XDR","XDR","Defender XDR + sensores + Sentinel","v1.0"),("ENDPOINTS","Endpoints","Defender for Endpoint + Vulnerability Management + Intune","v1.0"),("IDENTIDADES","Identidades","Defender for Identity + Entra ID Protection + CA + ID Governance","v1.0"),("DATOS","Datos","Purview (labels, DLP, DSPM/DSPM for AI, Insider Risk) + MDA","v1.0"),("SIEM","SIEM/SOAR","Microsoft Sentinel (portal Defender)","v1.0"),("NUBE","Nube","Defender for Cloud (CSPM, CWPP, AI Services)","v1.0"),("APPS","Apps / SaaS","Defender for Cloud Apps + app governance + CA app control","v1.0")]:
    if key == "XDR":
        d = json.load(open(os.path.join(ROOT, "Dominio_XDR", "json", "dominio_xdr.json"), encoding="utf-8")); a = json.load(open(os.path.join(ROOT, "Dominio_XDR", "json", "agentes_xdr.json"), encoding="utf-8"))
        rows.append((nm, tec, ver, len(d["tareas"]), len(a["agentes"]), len(a["tools_nuevos"])))
    else:
        d = json.load(open(os.path.join(ROOT, f"Dominio_{key}", "json", f"dominio_{key.lower()}.json"), encoding="utf-8"))
        rows.append((nm, tec, ver, len(d["tareas"]), len(d["agentes"]), len(d["tools_nuevos"])))
md = "# Comparativa de las ocho instancias de dominio del rol PO-GAC\n\n> 2026-11-15 · Plano B. Todas comparten rol, 41 competencias, 379 conceptos (GM-24 V7.1), 24 AGC, RACI, L0–L4 y recursos comunes (5 tools, 2 knowledge, 5 skills). **Ninguna requirió conceptos nuevos en el plano A.**\n\n| Dominio | Tecnología | Versión | Tareas | Agentes | Tools nuevos |\n|---|---|---|---|---|---|\n" + "\n".join(f"| {r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]} | {r[5]} |" for r in rows) + f"\n\n**Totales:** {sum(r[3] for r in rows)} tareas · {sum(r[4] for r in rows)} agentes · 24 tools base + {sum(r[5] for r in rows)} específicos de dominio.\n\n## Lectura\n\n1. **Dominios de canal** (Productividad, Endpoints, Identidades, Datos): protegen una superficie con sensores propios.\n2. **Dominios de plataforma** (XDR, SIEM, Nube): integran, correlacionan, automatizan y dan postura; su riesgo principal es la pérdida de visibilidad, la automatización indebida y el costo.\n3. **Transversales a las flotas de agentes:** Identidades (AGC-05/06/18), Datos (AGC-07), SIEM (observabilidad, Sentinel MCP), Nube (postura de recursos de IA, AMP-51).\n4. **Hitos de plataforma:** AIR embebido en MDE (1-sep-2026); Sentinel solo en el portal de Defender (31-mar-2027); multicloud en Secure Score (jun-2026).\n5. **Apps/SaaS** (Dominio_APPS v1.0) cierra la hoja de ruta del plano B: gobierna consentimiento OAuth, shadow IT (incl. IA generativa) y sesiones; audita las apps OAuth de las flotas de agentes desde afuera. Hito: file policies de MDA se retiran el 6-ene-2027 (→ Purview DLP).\n6. **Transversales adicionales:** Apps (permisos OAuth de agentes, AMP-33/36/50).\n"
open(os.path.join(ROOT, "Comparativa_8_Dominios_PO-GAC.md"), "w", encoding="utf-8").write(md)

step("5. Corpus V7.1 (plano A): docs, GM-24, pre-ensayos (99 nuevos + 280 originales), matriz, informes, XLSX, HTML")
subprocess.run([sys.executable, "gen_v71_full.py"], check=True)

if RECALC and shutil.which("soffice"):
    step("6. Recalcular XLSX con LibreOffice")
    for x in glob.glob(os.path.join(ROOT, "**", "*.xlsx"), recursive=True):
        subprocess.run(["soffice", "--headless", "--convert-to", "xlsx", "--outdir", os.path.dirname(x), x], capture_output=True)
if DOCX and shutil.which("pandoc"):
    step("7. DOCX con pandoc")
    ref = os.path.join(HERE, "ref_land.docx"); refarg = ["--reference-doc", ref] if os.path.exists(ref) else []
    targets = glob.glob(os.path.join(ROOT, "GM24_V7.1", "GM24_V7.1_docs", "*.md")) + glob.glob(os.path.join(ROOT, "GM24_V7.1", "informe", "*.md")) + glob.glob(os.path.join(ROOT, "GM24_V7.1", "pre_ensayos", "*.md")) + glob.glob(os.path.join(ROOT, "Dominio_*", "0*.md")) + glob.glob(os.path.join(ROOT, "*.md")) + glob.glob(os.path.join(ROOT, "V7.1", "*.md"))
    for t in targets:
        if os.path.exists(t): subprocess.run(["pandoc", t, "-f", "gfm", "-t", "docx", *refarg, "-o", t[:-3] + ".docx"], check=False)
    # consolidado de pre-ensayos originales (280) en un solo Word
    orig = sorted(glob.glob(os.path.join(ROOT, "GM24_V7.1", "pre_ensayos", "originales_K_HC", "*.md")))
    if orig:
        tmp = os.path.join(ROOT, "GM24_V7.1", "pre_ensayos", "_orig_all.md"); open(tmp, "w", encoding="utf-8").write("\n\n\\newpage\n\n".join(open(f, encoding="utf-8").read() for f in orig))
        subprocess.run(["pandoc", tmp, "-f", "gfm", "-t", "docx", *refarg, "-o", os.path.join(ROOT, "GM24_V7.1", "pre_ensayos", "Pre-ensayos_originales_240K_40HC_consolidado.docx")], check=False); os.remove(tmp)
    for dd in glob.glob(os.path.join(ROOT, "Dominio_*")):
        anx = sorted(glob.glob(os.path.join(dd, "anexos_agentes", "*.md")))
        if anx:
            tmp = os.path.join(dd, "_anexos_all.md"); open(tmp, "w", encoding="utf-8").write("\n\n\\newpage\n\n".join(open(f, encoding="utf-8").read() for f in anx))
            subprocess.run(["pandoc", tmp, "-f", "gfm", "-t", "docx", *refarg, "-o", os.path.join(dd, f"Anexos_Agentes_{os.path.basename(dd)[8:]}.docx")], check=False); os.remove(tmp)

step("8. Manifiesto")
man = []
for f in sorted(glob.glob(os.path.join(ROOT, "**", "*"), recursive=True)):
    if os.path.isfile(f) and "__pycache__" not in f and not f.endswith("MANIFEST_SHA256.txt"):
        man.append(f"{hashlib.sha256(open(f,'rb').read()).hexdigest()}  {os.path.relpath(f, ROOT)}")
open(os.path.join(ROOT, "MANIFEST_SHA256.txt"), "w").write("\n".join(man) + "\n")
print(f"\nDONE · {len(man)} archivos · raíz: {ROOT}")

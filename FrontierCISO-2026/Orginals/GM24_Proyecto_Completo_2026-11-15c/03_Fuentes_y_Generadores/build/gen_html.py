# -*- coding: utf-8 -*-
"""Sitio HTML único (sin iframes): secciones desde Markdown, catálogo y pre-ensayos interactivos, autoevaluación, descargas embebidas."""
import os, re, json, html as H
import data as D
ROOT = os.path.join(os.path.dirname(__file__), ".."); OUT = os.path.join(ROOT, "GM24_V6_PO_Agentes.html"); SECTIONS = []

def md_to_html(path):
    if not path or not os.path.exists(path): return f"<p><em>Sección no disponible: {H.escape(str(path))}</em></p>"
    md = open(path, encoding="utf-8").read(); out, in_table, in_code, code_lang, rows, code = [], False, False, "", [], []
    def inline(s):
        s = H.escape(s); s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s); s = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<i>\1</i>", s)
        s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s); return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2" target="_blank" rel="noopener">\1</a>', s)
    def flush_table():
        nonlocal rows
        if not rows: return
        hdr = rows[0]; body = rows[2:] if len(rows) > 1 and re.match(r"^\|?\s*:?-{2,}", rows[1]) else rows[1:]
        cells = lambda r: [c.strip() for c in r.strip().strip("|").split("|")]
        out.append('<div class="tblwrap"><table><thead><tr>' + "".join(f"<th>{inline(c)}</th>" for c in cells(hdr)) + "</tr></thead><tbody>")
        for r in body: out.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in cells(r)) + "</tr>")
        out.append("</tbody></table></div>"); rows = []
    for line in md.splitlines():
        if line.strip().startswith("```"):
            if in_code: out.append('<div class="mermaid">' + "\n".join(code) + "</div>" if code_lang == "mermaid" else "<pre><code>" + H.escape("\n".join(code)) + "</code></pre>"); in_code = False
            else: in_code = True; code_lang = line.strip()[3:].strip(); code = []
            continue
        if in_code: code.append(line); continue
        if line.strip().startswith("|"): in_table = True; rows.append(line); continue
        elif in_table: flush_table(); in_table = False
        m = re.match(r"^(#{1,6})\s+(.*)", line)
        if m: out.append(f"<h{len(m.group(1))}>{inline(m.group(2))}</h{len(m.group(1))}>"); continue
        if line.startswith(">"): out.append(f"<blockquote>{inline(line[1:].strip())}</blockquote>"); continue
        if re.match(r"^\s*[-*]\s+", line): out.append(f"<li>{inline(re.sub(r'^\s*[-*]\s+', '', line))}</li>"); continue
        if re.match(r"^\s*\d+\.\s+", line): out.append(f"<li class='num'>{inline(re.sub(r'^\s*\d+\.\s+', '', line))}</li>"); continue
        if line.strip() == "---": out.append("<hr>"); continue
        if line.strip(): out.append(f"<p>{inline(line)}</p>")
    if in_table: flush_table()
    h = "\n".join(out); h = re.sub(r"((?:<li>.*?</li>\n?)+)", r"<ul>\1</ul>", h); return re.sub(r"((?:<li class='num'>.*?</li>\n?)+)", r"<ol>\1</ol>", h)

def inicio(): return "<h1>GM-24</h1>"
def catalogo(): return "<h1>Catálogo</h1>"
def preensayos(): return "<h1>Pre-ensayos</h1>"
def autoeval():
    data = [dict(id=c[0], dom=c[1], comp=c[2], niveles=c[3]) for c in D.COMPETENCIAS]
    return f"""<h1>Autoevaluación de competencias PO-GAC ({len(data)})</h1><p>Marcá tu nivel (N1–N4) por competencia; se guarda en este navegador (localStorage) y podés exportar CSV.</p><div class="toolbar"><button type="button" id="ae-export">Exportar CSV</button><button type="button" id="ae-reset">Reiniciar</button><span id="ae-summary" class="pill"></span></div><div id="ae-list"></div><script id="ae-data" type="application/json">{json.dumps(data, ensure_ascii=False)}</script>"""
def descargas(): return "<h1>Descargas</h1>"

TEMPLATE = """<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{{TITLE}}</title>
<script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
<style>
:root{--bg:#f6f8fb;--fg:#17243a;--mut:#5b6b82;--acc:#17354f;--acc2:#2f7ddf;--card:#fff;--bd:#d8e0ea}
@media(prefers-color-scheme:dark){:root{--bg:#0f1620;--fg:#e6edf5;--mut:#9fb0c4;--acc:#8fb8ff;--acc2:#5aa0ff;--card:#172231;--bd:#2a3a4f}}
*{box-sizing:border-box}body{margin:0;font:15px/1.55 -apple-system,Segoe UI,Roboto,Arial,sans-serif;background:var(--bg);color:var(--fg);display:flex;min-height:100vh}
nav{width:300px;flex:none;background:var(--card);border-right:1px solid var(--bd);padding:16px;position:sticky;top:0;height:100vh;overflow:auto}
nav h2{font-size:16px;margin:0 0 4px;color:var(--acc)}nav h2 small{display:block;font-weight:400;color:var(--mut);font-size:12px}
nav input{width:100%;padding:8px;border:1px solid var(--bd);border-radius:8px;margin:10px 0;background:var(--bg);color:var(--fg)}
nav a{display:block;padding:6px 8px;border-radius:6px;color:var(--fg);text-decoration:none;font-size:13px}nav a:hover,nav a.active{background:var(--acc2);color:#fff}
main{flex:1;padding:24px 36px;max-width:1400px}section.sec{display:none}section.sec.active{display:block}
h1{color:var(--acc);margin-top:0}h2{color:var(--acc);border-bottom:1px solid var(--bd);padding-bottom:4px;margin-top:28px}h3{margin-top:22px}
.tblwrap{overflow:auto;margin:10px 0}table{border-collapse:collapse;width:100%;font-size:13px}th,td{border:1px solid var(--bd);padding:6px 8px;vertical-align:top;text-align:left}th{background:var(--acc);color:#fff;position:sticky;top:0}
blockquote{border-left:4px solid var(--acc2);margin:10px 0;padding:6px 12px;background:var(--card);color:var(--mut)}code{background:var(--card);border:1px solid var(--bd);border-radius:4px;padding:1px 4px;font-size:12.5px}pre{background:var(--card);border:1px solid var(--bd);padding:10px;overflow:auto;border-radius:8px}
.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:12px;margin:16px 0}.card{background:var(--card);border:1px solid var(--bd);border-radius:10px;padding:14px}.card .num{font-size:28px;font-weight:700;color:var(--acc2)}.card .lbl{font-size:12px;color:var(--mut)}
.toolbar{display:flex;flex-wrap:wrap;gap:10px;align-items:center;margin:12px 0}.toolbar input,.toolbar select,.toolbar button{padding:7px 10px;border:1px solid var(--bd);border-radius:8px;background:var(--card);color:var(--fg)}.pill{background:var(--acc2);color:#fff;border-radius:999px;padding:3px 10px;font-size:12px}
.pe{background:var(--card);border:1px solid var(--bd);border-radius:10px;padding:14px 18px;margin:12px 0}.pe h3{margin-top:0}.pe .meta{color:var(--mut);font-size:12.5px}.lead{font-size:16px;color:var(--mut)}
ul.dl{columns:2;font-size:13px}ul.dl li{break-inside:avoid;margin:3px 0}.tcount{color:var(--mut);font-size:11px}
.ae{display:grid;grid-template-columns:90px 1fr 220px;gap:8px;align-items:center;border-bottom:1px solid var(--bd);padding:6px 0;font-size:13px}
@media(max-width:900px){body{flex-direction:column}nav{position:static;width:auto;height:auto}main{padding:14px}ul.dl{columns:1}}
</style></head><body>
<nav><h2>{{TITLE}}<small>Actualizado {{FECHA}} · 379 conceptos · 7 dominios · plano A / plano B</small></h2><input id="q" type="search" placeholder="Buscar en todo el sitio…">{{NAV}}</nav>
<main>{{CONTENT}}</main>
<script>
const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
function show(id){document.querySelectorAll('section.sec').forEach(s=>s.classList.toggle('active',s.id==='sec-'+id));document.querySelectorAll('nav a[data-sec]').forEach(a=>a.classList.toggle('active',a.dataset.sec===id));window.scrollTo(0,0);if(window.mermaid){try{mermaid.initialize({startOnLoad:false});mermaid.run({querySelector:'#sec-'+id+' .mermaid'});}catch(e){}}}
document.querySelectorAll('nav a[data-sec]').forEach(a=>a.addEventListener('click',e=>{e.preventDefault();location.hash=a.dataset.sec;}));
window.addEventListener('hashchange',()=>show(location.hash.slice(1)||'inicio'));show(location.hash.slice(1)||'inicio');
document.getElementById('q').addEventListener('input',e=>{const v=e.target.value.toLowerCase();document.querySelectorAll('nav a[data-sec]').forEach(a=>{const sec=document.getElementById('sec-'+a.dataset.sec);a.style.display=(!v||a.textContent.toLowerCase().includes(v)||(sec&&sec.textContent.toLowerCase().includes(v)))?'':'none';});});
const catEl=document.getElementById('cat-data');if(catEl){const cat=JSON.parse(catEl.textContent);const prios=[...new Set(cat.map(r=>r.prio))].sort();const ps=document.getElementById('cat-prio');prios.forEach(p=>{const o=document.createElement('option');o.textContent=p;ps.appendChild(o);});
function renderCat(){const t=document.getElementById('cat-tipo').value,u=document.getElementById('cat-unidad').value,us=document.getElementById('cat-usado').value,pr=ps.value,q=document.getElementById('cat-q').value.toLowerCase();const rows=cat.filter(r=>(!t||r.tipo===t)&&(!u||r.unidad.includes(u))&&(!us||r.usado===us)&&(!pr||r.prio===pr)&&(!q||JSON.stringify(r).toLowerCase().includes(q)));document.getElementById('cat-count').textContent=rows.length+' conceptos';document.getElementById('cat-table').innerHTML='<div class="tblwrap"><table><thead><tr><th>ID</th><th>Tipo</th><th>Unidad</th><th>Concepto</th><th>Estado</th><th>Origen</th><th>Idea central (inicio)</th><th>Título V7</th><th>Método</th><th>Mapeos fuertes</th></tr></thead><tbody>'+rows.map(r=>`<tr><td>${esc(r.id)}</td><td>${esc(r.tipo)}</td><td>${esc(r.unidad)}</td><td>${esc(r.concepto)}</td><td>${esc(r.estado)}</td><td>${esc(r.origen)}</td><td>${esc(r.lectura)}</td><td>${esc(r.instrumento)}</td><td>${esc(r.rel)}</td><td>${esc(r.prio)}</td></tr>`).join('')+'</tbody></table></div>';}
['cat-tipo','cat-unidad','cat-usado','cat-prio','cat-q'].forEach(i=>document.getElementById(i).addEventListener('input',renderCat));renderCat();}
const peEl=document.getElementById('pe-data');if(peEl){const pe=JSON.parse(peEl.textContent);const peU=document.getElementById('pe-unidad'),peQ=document.getElementById('pe-q');
function renderPE(){const u=peU.value,q=peQ.value.toLowerCase();const tp=document.getElementById('pe-tipo')?document.getElementById('pe-tipo').value:'';const rows=pe.filter(r=>(!tp||r.tipo===tp)&&(!u||r.unidad===u)&&(!q||JSON.stringify(r).toLowerCase().includes(q)));document.getElementById('pe-count').textContent=rows.length+' pre-ensayos';document.getElementById('pe-list').innerHTML=rows.map(r=>`<div class="pe"><h3>${String(r.n).padStart(3,'0')}. ${esc(r.id)} — ${esc(r.nombre)}</h3><div class="meta"><b>Tipo:</b> ${esc(r.tipo||'')} · <b>Unidad:</b> ${esc(r.unidad)} · <b>Horas:</b> ${r.horas} · <b>Competencias:</b> ${esc(r.comps)} · <b>Origen:</b> ${esc(r.origen)}</div><p><b>Definición.</b> ${esc(r.definicion)}</p><p>${esc(r.brecha)}</p><p><b>Tesis.</b> ${esc(r.tesis)}</p><p><b>Tensión.</b> ${esc(r.tension)}</p><p><b>Aplicación.</b> ${esc(r.aplicacion)}</p><p><b>Evidencia.</b> ${esc(r.evidencia)}</p><p><b>Puentes.</b> ${esc(r.puentes)}</p><p><b>Práctica.</b> ${esc(r.practica||'')}</p><p><b>Próximos pasos.</b> ${esc(r.proximos||'')}</p><p><b>Relaciones:</b> ${esc(r.rel)}</p><p><b>Pregunta generadora:</b> <i>${esc(r.pregunta)}</i></p></div>`).join('');}
peU.addEventListener('input',renderPE);const peT=document.getElementById('pe-tipo');if(peT)peT.addEventListener('input',renderPE);peQ.addEventListener('input',renderPE);renderPE();}
const aeEl=document.getElementById('ae-data');if(aeEl){const ae=JSON.parse(aeEl.textContent);const KEY='gm24_pogac_ae';let st=JSON.parse(localStorage.getItem(KEY)||'{}');
function renderAE(){document.getElementById('ae-list').innerHTML=ae.map(c=>`<div class="ae"><b>${esc(c.id)}</b><span>${esc(c.comp)}<br><small>${esc(c.niveles)}</small></span><select data-id="${esc(c.id)}"><option value="">—</option>${[1,2,3,4].map(n=>`<option value="N${n}" ${st[c.id]==='N'+n?'selected':''}>N${n}</option>`).join('')}</select></div>`).join('');document.querySelectorAll('.ae select').forEach(s=>s.addEventListener('change',e=>{st[e.target.dataset.id]=e.target.value;localStorage.setItem(KEY,JSON.stringify(st));summ();}));summ();}
function summ(){const v=Object.values(st).filter(Boolean);document.getElementById('ae-summary').textContent=v.length+' / '+ae.length+' evaluadas';}
document.getElementById('ae-export').addEventListener('click',()=>{const csv='id,competencia,nivel\\n'+ae.map(c=>`"${c.id}","${c.comp.replace(/"/g,'""')}","${st[c.id]||''}"`).join('\\n');const a=document.createElement('a');a.href='data:text/csv;charset=utf-8,'+encodeURIComponent(csv);a.download='autoevaluacion_pogac.csv';a.click();});
document.getElementById('ae-reset').addEventListener('click',()=>{st={};localStorage.removeItem(KEY);renderAE();});renderAE();}
</script></body></html>"""

def build():
    nav, content = [], []
    for sid, title, path in SECTIONS:
        body = {"inicio": inicio, "catalogo": catalogo, "preensayos": preensayos, "autoeval": autoeval, "descargas": descargas}.get(sid, lambda p=path: md_to_html(p))()
        nav.append(f'<a href="#{sid}" data-sec="{sid}">{H.escape(title)}</a>'); content.append(f'<section id="sec-{sid}" class="sec" data-title="{H.escape(title)}">{body}</section>')
    page = TEMPLATE.replace("{{NAV}}", "\n".join(nav)).replace("{{CONTENT}}", "\n".join(content)).replace("{{TITLE}}", f"GM-24 {D.VERSION} · PO-GAC").replace("{{FECHA}}", D.FECHA)
    open(OUT, "w", encoding="utf-8").write(page)

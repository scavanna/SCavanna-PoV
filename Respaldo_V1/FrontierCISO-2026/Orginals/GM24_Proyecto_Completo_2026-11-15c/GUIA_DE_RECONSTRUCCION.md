# Guía de reconstrucción del proyecto GM‑24 (The Next CISO + Sub‑plan PO‑GAC)

**Versión de la guía:** 1.3 · 15‑nov‑2026 · **Probada:** reconstrucción completa con `python make_all.py` (~30 s, 752 archivos sin DOCX) desde el ZIP P5 en sala limpia.

> **Historia.** El 14‑nov‑2026 el entorno se reinició y perdió los ZIP y el directorio de trabajo. El 15‑nov se reconstruyó desde el historial de la sesión (código) + `Matrices_Curriculares.xlsx` + `corpus_preensayos.csv` del Atlas, y se completó con los lotes 01–08 (240 K), el archivo HC‑040 y el Documento Maestro re‑adjuntados por el autor. **Resultado: los 379 conceptos tienen pre‑ensayo íntegro** (280 originales + 99 nuevos).

## 1. Organización

| Plano | Qué es | Versionado | Dónde vive |
|---|---|---|---|
| **A — Corpus académico GM‑24** | 379 conceptos (245 K · 52 AMP · 40 HC · 42 PA) con pre‑ensayo y mapeo a 17 marcos; 24 unidades / 12 ejes; sub‑plan PO‑GAC | V4 → V5 → V6 → V7 → **V7.1** | `GM24_V7.1/` |
| **B — Marco de gobierno de capacidades contratadas** | 8 instancias de dominio (Productividad, XDR, Endpoints, Identidades, Datos, SIEM, Nube, Apps) | `Dominio_X vX.Y` | `Dominio_*/` |

Regla: nada del plano B modifica el plano A. Todo se **genera** desde `build/`.

## 2. Qué necesitás

### 2.1 `build/` (fuente de verdad)

```
build/
├── data.py · pa_v6.py (títulos V7.1) · v7.py · practica.py · estandares.py · mapeo.py
├── ensayos_pa_1..3.py (42 PA) · ensayos_amp_1..3.py (52 AMP + 5 K nuevos)
├── anexos.py · xdr.py · dominios.py · dominios2.py · datos.py · apps.py        · plano B
├── gen_md.py · gen_v6.py · gen_html.py · gen_v71_full.py · gen_dominios.py · gen_xdr.py · gen_v71_estrategia.py
├── make_all.py                                                    ← ORQUESTADOR
├── gm24_base.json (unidades, 240 K, 51 AMP) · catalogo331.json (331 con texto íntegro) · hc_rel.json · v71_titulos.json
├── fuentes_GM24/  · lotes 01–08, HC-040, Documento Maestro, V4_docx/ (3 DOCX V4)
├── fuentes_V4/    · V4 convertido a Markdown (base, act, c24) — caché usada por gen_v6.py
└── ref_land.docx  · plantilla Word apaisada (opcional)
docs/01_Marco_Conceptual_Rol.md · docs/07_Diagramas_y_Flujos.md · docs/TheNextCISO_GM-24_Documento_Maestro.md
```

### 2.2 Insumos externos

- Ninguno obligatorio: los DOCX V4 ya están embebidos. `V4_DIR` solo se usa si se borra la caché.

### 2.3 Software

Python 3.10+ y `openpyxl` (obligatorios); `pandoc` (texto V4 + DOCX); LibreOffice (opcional).

## 3. Reconstrucción

```bash
unzip P5_Fuentes_y_Generadores.zip && cd <carpeta>/03_Fuentes_y_Generadores/build
python make_all.py            # MD, JSON, XLSX, HTML
python make_all.py --docx     # + Word (incl. consolidado de 280 pre-ensayos originales)
sha256sum -c ../MANIFEST_SHA256.txt | grep -v OK
```

## 4. Qué hace `make_all.py`

| Paso | Produce |
|---|---|
| 0 | Verifica 28 fuentes, títulos V7.1 y texto íntegro en el catálogo |
| 1–2 | 8 dominios (plano B) + nota V7.1 |
| 3 | Estrategia + `V7.1/` (ChangeSet, catálogo) |
| 4 | Comparativa de 8 dominios |
| 5 | Plano A: docs 00–11, 3 documentos GM‑24 + Anexo + Documento Maestro, 99 pre‑ensayos nuevos (5 lotes + individuales), **280 originales** (`originales_K_HC/`) + lotes fuente, matriz, informes, XLSX (13 hojas), HTML |
| 7 | DOCX (opcional) |
| 8 | `MANIFEST_SHA256.txt` |

## 5. Modificar sin romper trazabilidad

| Quiero… | Edito… | Versión |
|---|---|---|
| Título de un PA | `pa_v6.py` + `v71_titulos.json` | editorial (V7.x) |
| Concepto nuevo | `v7.py → NUEVOS` + pre‑ensayo en `ensayos_amp_3.py` + `gen_v71_full.py → LOTES` | **V8** |
| Pre‑ensayo PA / AMP / K nuevo | `ensayos_pa_*.py` + `practica.py` / `ensayos_amp_*.py` | editorial |
| Texto de un K o HC original | `catalogo331.json → texto_completo` (o re‑parsear desde `fuentes_GM24/`) | editorial |
| Mapeo / marco nuevo | `mapeo.py` (`UNIT_BASE`, `K_RULES`, `*_MAP`) / `estandares.py` | editorial |
| Dominio nuevo | copiar la estructura de `apps.py` (FICHA, TAREAS, AGENTES, TOOLS, KNOWLEDGE, SKILLS, INSTANCIA, HITOS); registrar en `make_all.py` pasos 2 y 4 y en la lista de dominios del HTML en `gen_v71_full.py` | `Dominio_X v1.0` |

## 6. Recuperación ante pérdida

| Perdí… | Recuperar desde… |
|---|---|
| Todo | ZIP de fuentes → `make_all.py` |
| Solo `build/` | Sección **Descargas** de cualquier HTML del proyecto (todos los `.py`/`.json`); script en §8 |
| `catalogo331.json` | `fuentes_GM24/` + `corpus_preensayos.csv` (parser en `README_MAESTRO`) |
| Texto V4 | `build/fuentes_V4/*.md` o `build/fuentes_GM24/V4_docx/*.docx` (embebidos) |

## 7. Verificación

```python
import json, glob, collections
cat=json.load(open('GM24_V7.1/json/catalogo_V7.1.json',encoding='utf-8'))
print(len(cat), collections.Counter(c['tipo'] for c in cat), sum(1 for c in cat if c.get('texto_completo')))   # 379 {K245,AMP52,HC40,PA42} 379
cov=json.load(open('GM24_V7.1/json/cobertura_por_elemento_V7.1.json',encoding='utf-8'))
print([c['elemento'] for c in cov if not (c['fuertes'] or c['parciales'] or c['informativos'])])              # ['GAI-CBRN','GAI-Env']
print(len(glob.glob('GM24_V7.1/pre_ensayos/individuales/*.md')), len(glob.glob('GM24_V7.1/pre_ensayos/originales_K_HC/*.md')), len(glob.glob('Dominio_*/anexos_agentes/*.md')))  # 99 280 96
```

## 8. Extraer fuentes de un HTML

```python
import re, base64, html, os
s = open("GM24_V7.1_PO_Agentes.html", encoding="utf-8").read(); os.makedirs("recuperado", exist_ok=True)
for name, mime, b64 in re.findall(r'<a download="([^"]+)" href="data:([^;]+);charset=utf-8;base64,([^"]+)"', s):
    open(os.path.join("recuperado", html.unescape(name)), "wb").write(base64.b64decode(b64))
```

## 9. Convenciones

IDs `Gx.y`/`Mx.y`, `-Knn`, `AMP-nn`, `HC-nnn`, `-PAnn`, `Cn.m`, tareas `MDO-/XDR-/EP-/ID-/DP-/SI-/CL-*`, agentes `AG-/XA-/EA-/IA-/DA-/SA-/CA-nn`, `AGC-nn`, `L0–L4`, `R1/R2/R3`. Marcadores ◆ V5/V6/V7/V7.1. Mapeo ● ◐ ○ (cubre | instancia | referencia); nunca afirma conformidad. IDs curriculares ≠ ESS. DD/K4x/R/eo:OP/COE = marco interno.

## 10. Pendientes del programa

D07 (horas), D10 (licencias/preview), ESS a los 99 pre‑ensayos nuevos, ChangeSets al Atlas.

> **Texto V4.** Los 3 DOCX V4 están embebidos en `build/fuentes_GM24/V4_docx/` y su conversión Markdown cacheada en `build/fuentes_V4/{base,act,c24}.md`; `gen_v6.py` usa la caché primero, luego `V4_DIR`. Ya no hay dependencia externa.

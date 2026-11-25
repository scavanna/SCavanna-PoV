# -*- coding: utf-8 -*-
"""V7.1 (ChangeSet editorial) + Estrategia de anexos tecnológicos y separación de planos."""
import os, json
import data as D, v7 as V, dominios as DM
BASE = os.path.join(os.path.dirname(__file__), ".."); V71D = os.path.join(BASE, "V7.1"); os.makedirs(os.path.join(V71D, "json"), exist_ok=True)
def esc(s): return str(s).replace("|","\\|").replace("\n"," ")
def table(h, rows): return "\n".join(["| "+" | ".join(h)+" |","|"+"|".join(["---"]*len(h))+"|"]+["| "+" | ".join(esc(c) for c in r)+" |" for r in rows])
def write(p, t): open(p,"w",encoding="utf-8").write(t.strip()+"\n")
TIT = json.load(open(os.path.join(os.path.dirname(__file__), "v71_titulos.json"), encoding="utf-8"))
cat = V.catalogo_v7()
for c in cat:
    if c["id"] in TIT: c["titulo_v7"] = TIT[c["id"]]["antes"]
json.dump(cat, open(os.path.join(V71D, "json", "catalogo_V7.1.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
changeset = dict(id="CS-GM24-V7.1-001", fecha=V.FECHA, tipo="editorial", alcance="4 conceptos PA promovidos", impacto_en_ids="ninguno", impacto_en_cantidad="ninguno (379)", impacto_en_mapeo="ninguno", impacto_en_pre_ensayos="se conservan como instancia de referencia + nota de instancias",
    cambios=[dict(id=k, campo="concepto", antes=v["antes"], despues=v["despues"]) for k, v in TIT.items()],
    aplicar_en=["build/pa_v6.py (fuente de verdad; ya aplicado)","docs/11_Catalogo_V7.1.md","GM24_V7.1_docs/* (bloques ◆ V7.1)","pre_ensayos/individuales/<ID>.md (cabecera 'Título V7' + nota de instancias)","json/catalogo_V7.1.json","GM24_V7.1_Matriz_Estandares.xlsx hoja 01"],
    instancias=dict(productividad="Dominio_PRODUCTIVIDAD v1.1", xdr="Dominio_XDR v1.0", endpoints="Dominio_ENDPOINTS v1.0", identidades="Dominio_IDENTIDADES v1.0", datos="Dominio_DATOS v1.0", siem="Dominio_SIEM v1.0", nube="Dominio_NUBE v1.0"))
json.dump(changeset, open(os.path.join(V71D, "json", "changeset_V7.1.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
write(os.path.join(V71D, "V7.1_ChangeSet_Editorial.md"), f"""# GM-24 V7.1 — ChangeSet editorial CS-GM24-V7.1-001

> {V.FECHA}. **Tipo:** editorial. **Alcance:** 4 conceptos PA promovidos al programa en V7. **Sin impacto** en IDs, cantidad (379), mapeo ni pre-ensayos (instancia de referencia). Aplicado en origen (`build/pa_v6.py`) y propagado por regeneración.

## 1. Cambios
{table(["ID","Título V7 (antes)","Título V7.1 (después)"], [(k, v["antes"], v["despues"]) for k, v in TIT.items()])}

## 2. Dónde queda aplicado
{chr(10).join('- ' + x for x in changeset['aplicar_en'])}

## 3. Nota de instancias (incluida en cada pre-ensayo afectado)
> **Instancias de dominio.** Este pre-ensayo desarrolla la instancia de referencia (productividad: Defender for Office 365). Las instancias XDR, Endpoints, Identidades, Datos, SIEM y Nube están en los paquetes `Dominio_*` (plano B), que no modifican este concepto.

## 4. Por qué es V7.1 y no V8
Las instancias de dominio demostraron que los 379 conceptos cubren siete dominios de un SOC de Microsoft 365 **sin conceptos nuevos**; solo cuatro títulos eran demasiado específicos. Un cambio de título sin cambio de contenido, ID ni mapeo es editorial.
""")
CAPAS = [
 ("Plano A — Corpus académico (GM-24)","Conceptos-lección (K, AMP, HC, PA), pre-ensayos, competencias, unidades, mapeo a estándares y certificaciones","V4…V7, V7.1 (editorial); V8 solo si una instancia exige un concepto nuevo","Comité curricular; ESS y ChangeSets al Atlas","Respaldado por NIST/ISACA/MITRE/OWASP/CIS/CSA; independiente de proveedor","Alumno/profesional; autor; ontología/MCP"),
 ("Plano B — Marco de gobierno de capacidades contratadas","Productos-control por dominio: ficha, grilla CSF, modelo operativo, agentes, anexos, KPIs, permisos; AGC","Versionado propio por dominio (Dominio_X vX.Y); cambia con releases de Microsoft","PO-GAC de cada dominio; CISO dueño del portafolio; proveedores vía anexos","Específico del escenario sobre bases agnósticas; verificable en Learn; sujeto a licencias y GA/preview","CISO y owners; SOC; proveedores; auditoría"),
]
REL = [("Concepto (A) → Instancia (B)","Un concepto se instancia en cada dominio (ProductPractice EXEMPLIFIES eo:OP)."),("Instancia (B) → Concepto (A)","Una instancia puede revelar brecha o sobre-especificidad (V7.1); si exige concepto nuevo, se propone candidato; nunca se edita el corpus desde una instancia."),("Estándares","A se mapea por concepto; B hereda y agrega evidencia técnica por control."),("Horas","Las horas curriculares viven en A; la práctica en un dominio se contabiliza como práctica (91 h)."),("Versionado","A cambia por ChangeSet con ESS. B cambia por release de plataforma, licencias o decisión del CISO; cada dominio lleva VERSION.md."),("Lo que un CISO contrató","B describe capacidades contratadas y cómo gobernarlas con el vocabulario de A. Un CISO sin Microsoft usa A íntegro y construye su propio B.")]
DOM = [("Productividad","Defender for Office 365 (EOP) en Defender XDR","Dominio_PRODUCTIVIDAD v1.1"),("XDR","Defender XDR + sensores + Sentinel","Dominio_XDR v1.0"),("Endpoints","Defender for Endpoint + Vulnerability Management + Intune","Dominio_ENDPOINTS v1.0"),("Identidades","Defender for Identity + Entra ID Protection + CA + ID Governance","Dominio_IDENTIDADES v1.0"),("Datos","Purview (labels, DLP, DSPM/DSPM for AI, Insider Risk) + MDA","Dominio_DATOS v1.0"),("SIEM/SOAR","Microsoft Sentinel (portal Defender)","Dominio_SIEM v1.0"),("Nube","Defender for Cloud (CSPM, CWPP, AI Services)","Dominio_NUBE v1.0"),("Apps / SaaS","Defender for Cloud Apps + app governance + CA app control","Dominio_APPS v1.0")]
PEND = [("Exposición","Security Exposure Management + Defender EASM","Dominio_EXPOSICION","Media","Puede absorberse como vista de XDR"),("IA y agentes (transversal)","Defender para IA, Agent 365, Entra Agent ID, Purview DLP para IA","Dominio_IA","Alta","Consolidar lo ya instanciado en AGC/Identidades/Datos/Nube")]
LIC = [("Microsoft 365 E5 / E7","Defender XDR (MDO P2, MDE P2, MDI, MDA), Purview, Entra ID P2; E7: Agent 365 + Entra Suite","Todos los dominios; gobierno de agentes"),("Microsoft Sentinel","SIEM/SOAR, data lake, MCP server (preview); portal de Defender desde 31-mar-2027","XDR, SIEM"),("Microsoft Defender for Cloud","CSPM/CWPP multicloud, attack paths, AI Services","Nube"),("Security Copilot","SCU; agentes (ruta R1)","Todas las flotas"),("Copilot Studio / Foundry","Créditos/capacidad; tokens (R2/R3)","Todas las flotas"),("Workload Identities Premium","Riesgo de service principals/agentes","Identidades")]
write(os.path.join(BASE, "Estrategia_Anexos_Tecnologicos_y_Separacion_de_Planos.md"), f"""# Estrategia de anexos tecnológicos y separación de planos: corpus académico (GM-24) vs. marco de gobierno de capacidades contratadas

> {V.FECHA}. Fija la distinción entre **el GM-24 como corpus académico respaldado** y **su uso como marco para gobernar y gestionar capacidades que un CISO ha contratado**, y define la estrategia de anexos por tecnología (Microsoft 365 E7, Sentinel, Defender for Cloud).

## 1. Los dos planos
{table(["Plano","Qué contiene","Versionado","Quién lo gobierna","Carácter","Audiencia"], CAPAS)}

**Regla de oro:** nada del plano B modifica el plano A directamente.

## 2. Relaciones entre planos
{table(["Relación","Regla"], REL)}

## 3. Instancias de dominio (plano B)
{table(["Dominio","Tecnología","Paquete / versión"], DOM)}

Comparten: rol PO-GAC, 41 competencias, 379 conceptos (V7.1), 24 AGC, RACI, L0–L4 y recursos comunes. **Ninguna de las ocho requirió conceptos nuevos.**

## 4. Próximas instancias
{table(["Dominio","Tecnología","Paquete","Prioridad","Observación"], PEND)}

## 5. Plantilla uniforme de una instancia
| Sección | Contenido | Fuente de verdad |
|---|---|---|
| 01 Ficha | Nombre, dominio ZT, tecnología, CSF, fuente oficial, objetivo, SLO, owner, diferencia, interfaces, personas, permisos, grilla CSF | Ops guide del producto + G2.1-PA01 |
| 02 Instanciación | Concepto V7 → cómo lo instancia el dominio; hallazgos para el corpus | Catálogo V7.1 |
| 03 Modelo operativo | Tareas por cadencia con persona, CSF, SAF, eo:OP, L0–L4, agente, KPI, fuente | Ops guide; MAEO |
| 04 Agentes + anexos | Tools/knowledge/skills propios, compartidos y comunes; permisos; estado GA/preview/verificar | Learn; AGC |
| VERSION.md · XLSX · JSON | Versionado propio; gemelos verificables | build/ |

## 6. Licencias y SKUs que condicionan el plano B
{table(["Producto / SKU","Qué habilita","Dominios"], LIC)}

## 7. Cómo leer el conjunto como CISO
1. Para formar personas: plano A (independiente de lo que compraste). 2. Para gobernar lo que compraste: plano B, con el vocabulario de A; auditar cobertura, madurez y autonomía. 3. Si cambiás de proveedor: A no cambia; reconstruís B. 4. Si el proveedor cambia el producto: cambia B, no el corpus.
""")
print("DONE V7.1 + estrategia")

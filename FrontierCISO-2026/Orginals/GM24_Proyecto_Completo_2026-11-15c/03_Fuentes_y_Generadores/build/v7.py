# -*- coding: utf-8 -*-
"""GM-24 V7: extensiones confirmadas el 14-nov-2026 (candidatos V7-C01…C10). Catálogo V7 = 245 K + 52 AMP + 40 HC + 42 PA = 379 conceptos."""
import data as D
VERSION = "V7.1"; FECHA = "2026-11-14"
NUEVOS = [
 dict(id="G2.1-K11", tipo="Base GM-24", unidad="G2.1", concepto="CSF 2.0 completo: funciones, categorías y perfiles organizacionales", candidato="V7-C01", cierra="INC-09", tesis="NIST CSF 2.0 solo gobierna cuando se usa entero: las seis funciones y sus 22 categorías como lenguaje común de resultados, y los perfiles (actual/objetivo) como instrumento de decisión; enseñar solo Govern deja a ID/PR/DE/RS/RC implícitos y sin dueño.", afin="G2.1-K04, AMP-07, G2.1-PA01"),
 dict(id="M3.1-K11", tipo="Base GM-24", unidad="M3.1", concepto="Arquitectura empresarial y arquitectura de seguridad de la información", candidato="V7-C02", cierra="INC-07", tesis="La arquitectura de seguridad de la información es una vista de la arquitectura empresarial: sin ese vínculo los controles se diseñan contra sistemas y no contra capacidades de negocio; CISM 2026 lo incorpora como contenido examinable.", afin="M3.1-K01, M3.1-K02, G1.2-K01"),
 dict(id="M4.1-K11", tipo="Base GM-24", unidad="M4.1", concepto="Deception y señuelos como control detectivo", candidato="V7-C05", cierra="INC-02", tesis="El engaño defensivo (honeytokens, cuentas y buzones señuelo, credenciales trampa) produce detecciones de alta fidelidad porque nadie legítimo debería tocarlos; en un SOC con agentes, los señuelos también detectan agentes que exceden su alcance.", afin="M4.1-K07, M4.1-K02, HC-017"),
 dict(id="M4.2-K11", tipo="Base GM-24", unidad="M4.2", concepto="Escalamiento de privilegios en identidades humanas y no humanas como táctica adversaria", candidato="V7-C06", cierra="INC-04", tesis="El escalamiento de privilegios es la táctica que convierte un acceso inicial en control del entorno; con agentes e identidades no humanas, el abuso de permisos de conectores y tokens es su versión más nueva y menos vigilada.", afin="M4.2-K02, M2.2-K04, AMP-33, AMP-34, HC-009"),
 dict(id="AMP-52", tipo="Ampliación Atlas", unidad="G6.2 · M3.2", concepto="Content safety y riesgos de contenido generado", candidato="V7-C07", cierra="INC-03", tesis="Los sistemas generativos pueden producir contenido dañino, abusivo o engañoso aunque el objetivo sea legítimo; los guardrails de salida son un control de seguridad y de ética, con alcance declarado (qué riesgos de contenido quedan fuera del rol).", afin="AMP-25, AMP-26, AGC-08, M3.2-PA02"),
 dict(id="M3.1-K12", tipo="Base GM-24", unidad="M3.1", concepto="Seguridad física, ambiental y mantenimiento como dependencias del control", candidato="V7-C08", cierra="INC-01", tesis="Ningún control lógico sobrevive a una sala de servidores sin control de acceso, a un centro de datos sin energía o a un sistema sin mantenimiento; aunque el CISO rara vez los opere, debe gobernarlos como dependencias y exigir evidencia a quien los opera.", afin="M3.1-K08, M6.1-K10, HC-030"),
]
PROMOVIDOS = ["M3.1-PA02", "M4.2-PA01", "M4.1-PA01", "M4.1-PA03"]
AAISM_UNIDAD = {"G1.1":"1A, 1B","G1.2":"1A, 1B","G2.1":"1A","G2.2":"1B","G3.1":"1A, 3D","G3.2":"1D, 3E","G4.1":"2A","G4.2":"2A","G5.1":"2A, 2B","G5.2":"2A","G6.1":"1D","G6.2":"3D","M1.1":"1D","M1.2":"1D, 2C","M2.1":"1C, 3C","M2.2":"3A, 3E","M3.1":"3A","M3.2":"3B, 3E","M4.1":"3E, 1E","M4.2":"2B","M5.1":"1E","M5.2":"1E","M6.1":"1E, 2C","M6.2":"2C, 3A, 3B"}
REFERENCIAS_ID = {
 "M4.2-PA02": "OWASP Top 10 for Agentic Applications 2026 v2.01 (ASI01–ASI10); OWASP Top 10 for LLM Applications 2025 (LLM01–LLM10); MITRE ATLAS; CSA MAESTRO",
 "M3.2-PA02": "CSA AI Controls Matrix v1.1 (AIS-11, IAM-19, MDS); NIST AI RMF 1.0 + AI 600-1; ISO/IEC 42001:2023 Anexo A",
 "M6.2-K04": "OWASP ASI 2026 v2.01; OWASP LLM 2025; MITRE ATLAS; NIST AI 600-1",
 "AMP-41": "OWASP LLM01 (2025), ASI01/ASI06 (2026 v2.01); MITRE ATLAS AML.T0051",
 "AMP-42": "OWASP LLM04/LLM08 (2025), ASI06 (2026 v2.01); MITRE ATLAS AML.T0020",
 "HC-032": "OWASP ASI 2026 v2.01; CSA MAESTRO; MITRE ATLAS",
 "M6.2-K06": "OWASP ASI10 Rogue Agents (2026 v2.01); CSA AICM v1.1",
 "AMP-33": "OWASP Top 10 for Non-Human Identities (2025); ASI03 (2026 v2.01)",
 "AMP-34": "OWASP NHI Top 10 (2025); ASI03; CSA AICM IAM-19",
 "AMP-50": "OWASP ASI04/ASI02 (2026 v2.01); CSA AICM AIS-11",
 "M4.1-K11": "MITRE D3FEND Deceive (D3-DO, D3-DE); MITRE Engage",
 "M4.2-K11": "MITRE ATT&CK TA0004; OWASP ASI03; OWASP NHI Top 10",
}
def catalogo_v7():
    out = []
    for c in D.CAT:
        t = {"Base GM-24":"K","Ampliación Atlas":"AMP","Híbrido (HC)":"HC"}[c["tipo"]]
        estado = c["estado"]
        if t == "AMP": estado = "Idea central desarrollada (lotes AMP-01/02/03, V7)"
        out.append(dict(id=c["id"], tipo=t, unidad=c["unidad"], concepto=c["concepto"], estado=estado, origen_version="V4" if t=="K" else ("V6 (AMP, título) → V7 (pre-ensayo)" if t=="AMP" else "V6"), tesis=c.get("tesis") or "", pregunta=c.get("pregunta") or "", afin=c.get("afin") or "", referencias_id=REFERENCIAS_ID.get(c["id"],""), aaism=AAISM_UNIDAD.get(str(c["unidad"]).split(" ")[0],"")))
    for n in NUEVOS:
        t = {"Base GM-24":"K","Ampliación Atlas":"AMP"}[n["tipo"]]
        out.append(dict(id=n["id"], tipo=t, unidad=n["unidad"], concepto=n["concepto"], estado="Idea central desarrollada (lote V7-01)", origen_version=f"V7 ({n['candidato']}, cierra {n['cierra']})", tesis=n["tesis"], pregunta="", afin=n["afin"], referencias_id=REFERENCIAS_ID.get(n["id"],""), aaism=AAISM_UNIDAD.get(n["unidad"].split(" ")[0],"")))
    for p in D.PA:
        prom = p[0] in PROMOVIDOS
        out.append(dict(id=p[0], tipo="PA", unidad=p[1], concepto=p[2], estado="Idea central desarrollada (lote PA-01/02) — " + ("PROMOVIDO al programa (V7-C04)" if prom else "sub-plan PO-GAC"), origen_version="V6 → V7 (promovido)" if prom else "V6", tesis=p[3], pregunta="", afin="", referencias_id=REFERENCIAS_ID.get(p[0],""), aaism=AAISM_UNIDAD.get(p[1],"")))
    return out
def clase_hc(c):
    us = [u.strip() for u in str(c["unidad"]).replace("·", ",").split(",") if u.strip()]
    pil = {u[0] for u in us}
    if len(us) >= 4: return "Integrador"
    if len(pil) > 1: return "Vinculante (puente G↔M)"
    return "Híbrido (intra-pilar)"

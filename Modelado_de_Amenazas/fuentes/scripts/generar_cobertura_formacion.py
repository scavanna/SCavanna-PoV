from __future__ import annotations

import csv
import hashlib
import importlib.util
import json
from collections import Counter
from pathlib import Path

from openpyxl import Workbook, load_workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.worksheet.table import Table, TableStyleInfo
from openpyxl.utils import get_column_letter

ROOT = Path(__file__).resolve().parents[1]
NINJA = Path(r"C:\SCavannaLocal\AF-202611\Ninja_Training_Seguridad_Microsoft_2026")
OE = Path(r"C:\SCavannaLocal\AF-202611\ExcelenciaOperacional_NinjaTraining_KPIsOKRs\Excelencia_Operacional")
OUT = ROOT / "docs" / "10-cobertura-formacion-microsoft"
TODAY = "2026-11-18"

spec = importlib.util.spec_from_file_location("estado_arte", ROOT / "scripts" / "generar_estado_arte.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
SOURCES = mod.SOURCES

NINJA_PROGRAMS = {
    "sentinel": ("Microsoft Sentinel", "01_Sentinel/README.md"),
    "xdr": ("Microsoft Defender XDR", "02_Defender_XDR/README.md"),
    "entra": ("Microsoft Entra: identidad y agentes", "03_Entra_Identidad_y_Agentes/README.md"),
    "security_copilot": ("Microsoft Security Copilot", "04_Security_Copilot/README.md"),
    "purview_ip": ("Purview Information Protection", "05_Purview_Information_Protection/README.md"),
    "purview_dlp": ("Purview Data Loss Prevention", "06_Purview_DLP/README.md"),
    "purview_irm": ("Purview Insider Risk Management", "07_Purview_Insider_Risk/README.md"),
    "purview_comm": ("Purview Communication Compliance e Information Barriers", "08_Purview_Communication_Compliance/README.md"),
    "purview_records": ("Purview Data Lifecycle y Records Management", "09_Purview_Ciclo_de_vida_y_Registros/README.md"),
    "purview_edisc_audit": ("Purview eDiscovery y Audit", "10_Purview_eDiscovery_y_Audit/README.md"),
    "purview_compliance": ("Purview Compliance Manager", "11_Purview_Compliance_Manager/README.md"),
    "purview_dspm": ("Purview DSPM y seguridad de datos para IA", "12_Purview_DSPM_y_Seguridad_de_datos_para_IA/README.md"),
    "copilot_agents": ("Seguridad de M365 Copilot, agentes y Copilot Studio", "13_Seguridad_de_Copilot_y_Copilot_Studio/README.md"),
    "defender_cloud": ("Microsoft Defender for Cloud", "14_Defender_for_Cloud/README.md"),
    "foundry_agents": ("Seguridad de agentes de IA en Microsoft Foundry", "15_Seguridad_de_agentes_de_IA_en_Foundry/README.md"),
}

OE_PROGRAMS = {
    "entra": ("Microsoft Entra ID", "01_Microsoft_Entra_ID/Microsoft_Entra_ID_Guia_Excelencia_Operacional.json"),
    "entra_governance": ("Microsoft Entra ID Governance", "02_Microsoft_Entra_ID_Governance/Microsoft_Entra_ID_Governance_Guia_Excelencia_Operacional.json"),
    "xdr": ("Microsoft Defender XDR", "03_Microsoft_Defender_XDR/Microsoft_Defender_XDR_Guia_Excelencia_Operacional.json"),
    "mde": ("Microsoft Defender for Endpoint", "04_Microsoft_Defender_for_Endpoint/Microsoft_Defender_for_Endpoint_Guia_Excelencia_Operacional.json"),
    "mdo": ("Microsoft Defender for Office 365", "05_Microsoft_Defender_for_Office_365/Microsoft_Defender_for_Office_365_Guia_Excelencia_Operacional.json"),
    "mdi": ("Microsoft Defender for Identity", "06_Microsoft_Defender_for_Identity/Microsoft_Defender_for_Identity_Guia_Excelencia_Operacional.json"),
    "mdca": ("Microsoft Defender for Cloud Apps", "07_Microsoft_Defender_for_Cloud_Apps/Microsoft_Defender_for_Cloud_Apps_Guia_Excelencia_Operacional.json"),
    "sentinel": ("Microsoft Sentinel", "08_Microsoft_Sentinel/Microsoft_Sentinel_Guia_Excelencia_Operacional.json"),
    "security_copilot": ("Microsoft Security Copilot", "09_Microsoft_Security_Copilot/Microsoft_Security_Copilot_Guia_Excelencia_Operacional.json"),
    "intune": ("Microsoft Intune Plan 1", "10_Microsoft_Intune_Plan_1/Microsoft_Intune_Plan_1_Guia_Excelencia_Operacional.json"),
    "intune_suite": ("Microsoft Intune Suite", "11_Microsoft_Intune_Suite/Microsoft_Intune_Suite_Guia_Excelencia_Operacional.json"),
    "windows": ("Windows Enterprise Security y Cifrado", "12_Windows_Enterprise_Security_y_Cifrado/Windows_Enterprise_Security_y_Cifrado_Guia_Excelencia_Operacional.json"),
    "purview_suite": ("Microsoft Purview Suite", "13_Microsoft_Purview_Suite_Arquitectura_y_Gobierno/Microsoft_Purview_Suite_Arquitectura_y_Gobierno_Guia_Excelencia_Operacional.json"),
    "purview_ip": ("Purview Information Protection", "14_Purview_Information_Protection/Purview_Information_Protection_Guia_Excelencia_Operacional.json"),
    "purview_dlp": ("Purview Data Loss Prevention", "15_Purview_Data_Loss_Prevention/Purview_Data_Loss_Prevention_Guia_Excelencia_Operacional.json"),
    "purview_records": ("Purview Data Lifecycle y Records Management", "16_Purview_Data_Lifecycle_y_Records_Management/Purview_Data_Lifecycle_y_Records_Management_Guia_Excelencia_Operacional.json"),
    "purview_irm": ("Purview Insider Risk Management", "17_Purview_Insider_Risk_Management/Purview_Insider_Risk_Management_Guia_Excelencia_Operacional.json"),
    "purview_comm": ("Purview Communication Compliance", "18_Purview_Communication_Compliance/Purview_Communication_Compliance_Guia_Excelencia_Operacional.json"),
    "purview_audit": ("Purview Audit Premium", "19_Purview_Audit_Premium/Purview_Audit_Premium_Guia_Excelencia_Operacional.json"),
    "purview_edisc": ("Purview eDiscovery Premium", "20_Purview_eDiscovery_Premium/Purview_eDiscovery_Premium_Guia_Excelencia_Operacional.json"),
    "lockbox": ("Customer Lockbox, Customer Key y M365 PAM", "21_Customer_Lockbox_Customer_Key_y_M365_PAM/Customer_Lockbox_Customer_Key_y_M365_PAM_Guia_Excelencia_Operacional.json"),
    "agent365": ("Microsoft Agent 365", "22_Microsoft_Agent_365/Microsoft_Agent_365_Guia_Excelencia_Operacional.json"),
}

# status: Directa (programa/guía de esa tecnología), Parcial (incluida en una familia o módulo), Sin artefacto específico.
NINJA_MAP = {
    "MS-001": ("Directa", ["xdr"], "Programa dedicado a Defender XDR; integra cargas Defender."),
    "MS-002": ("Directa", ["sentinel"], "Programa dedicado a Microsoft Sentinel."),
    "MS-003": ("Parcial", ["entra", "xdr"], "Cubierto como componente de identidad y detección; no existe programa exclusivo."),
    "MS-004": ("Parcial", ["xdr", "entra"], "Cubierto en rutas de XDR e identidad híbrida; sin programa dedicado."),
    "MS-005": ("Directa", ["defender_cloud"], "Programa dedicado a Defender for Cloud, sus planes y workloads."),
    "MS-006": ("Sin artefacto específico", [], "No existe programa Ninja dedicado ni cobertura explícita equivalente identificada."),
    "MS-007": ("Parcial", ["xdr", "defender_cloud"], "Tratado como carga XDR/CNAPP; no hay programa independiente de MDE."),
    "MS-008": ("Sin artefacto específico", [], "No existe programa Ninja dedicado a Intune en el repositorio."),
    "MS-009": ("Directa", ["purview_dlp"], "Programa dedicado a Purview DLP."),
    "MS-010": ("Directa", ["purview_ip"], "Programa dedicado a Purview Information Protection."),
    "MS-011": ("Directa", ["purview_irm"], "Programa dedicado a Purview Insider Risk Management."),
    "MS-012": ("Parcial", ["xdr"], "Incluido dentro de XDR y protección SaaS; no hay programa dedicado."),
    "MS-013": ("Parcial", ["entra"], "Capacidad central del programa Entra; no programa exclusivo de Conditional Access."),
    "MS-014": ("Parcial", ["entra"], "PIM aparece dentro del programa de Entra; no programa exclusivo."),
    "MS-015": ("Sin artefacto específico", [], "No existe programa Ninja específico para Azure Backup."),
    "MS-016": ("Sin artefacto específico", [], "No existe programa Ninja específico para Azure Site Recovery."),
    "MS-017": ("Parcial", ["sentinel", "defender_cloud"], "Log Analytics/Monitor aparecen como base de observabilidad; no hay programa dedicado."),
    "MS-018": ("Parcial", ["defender_cloud"], "Cobertura posible como servicio/workload perimetral; sin módulo dedicado verificado."),
    "MS-019": ("Parcial", ["defender_cloud", "foundry_agents"], "Tratada dentro de protección de aplicaciones/APIs/cloud; no programa dedicado."),
    "MS-020": ("Parcial", ["defender_cloud"], "Track W5 de aplicaciones, APIs y serverless dentro del programa Defender for Cloud."),
    "MS-021": ("Parcial", ["defender_cloud"], "DevOps/Code-to-cloud aparece en el programa Defender for Cloud; sin programa independiente GHAS/Azure DevOps."),
    "MS-022": ("Parcial", ["defender_cloud", "foundry_agents"], "Custodia de claves/secretos aparece en cargas cloud e IA; no programa dedicado."),
    "MS-023": ("Parcial", ["defender_cloud"], "Gobierno/configuración Azure cubierto en CNAPP/MCSB; no programa exclusivo de Azure Policy."),
    "MS-024": ("Directa", ["security_copilot"], "Programa dedicado a Microsoft Security Copilot."),
    "MS-025": ("Parcial", ["copilot_agents", "foundry_agents"], "Guardrails y seguridad de prompts están cubiertos en programas de IA; no programa exclusivo del servicio Content Safety."),
    "MS-026": ("Parcial", ["xdr"], "Defender for Office 365 se trata dentro de XDR y correo; no programa dedicado."),
    "MS-027": ("Directa", ["purview_edisc_audit", "purview_compliance"], "Cobertura directa repartida entre Audit/eDiscovery y Compliance Manager."),
    "MS-028": ("Parcial", ["xdr", "defender_cloud"], "Vulnerabilidades y exposición incluidas en XDR/Defender for Cloud; no programa exclusivo."),
    "MS-029": ("Sin artefacto específico", [], "No existe programa exclusivo conjunto para Front Door/Traffic Manager."),
    "MS-030": ("Parcial", ["xdr", "defender_cloud"], "Gestión de exposición se integra en las rutas XDR/CNAPP; no programa exclusivo."),
    "MS-031": ("Sin artefacto específico", [], "No existe programa Ninja dedicado a Microsoft Priva."),
    "MS-032": ("Sin artefacto específico", [], "No existe programa Ninja dedicado a Azure Service Health."),
    "MS-033": ("Parcial", ["defender_cloud", "sentinel"], "Azure Resource Graph aparece como capacidad de hunting/inventario; no programa exclusivo."),
    "MS-034": ("Sin artefacto específico", [], "No existe programa Ninja dedicado a Azure Traffic Manager."),
    "MS-035": ("Sin artefacto específico", [], "No existe programa Ninja dedicado a Azure Front Door."),
    "MS-036": ("Sin artefacto específico", [], "No se encontró mención explícita ni programa específico de Availability Zones."),
    "MS-037": ("Sin artefacto específico", [], "No existe programa Ninja dedicado a Azure Firewall."),
    "MS-038": ("Parcial", ["defender_cloud", "foundry_agents"], "Private connectivity aparece en arquitectura cloud/IA; no programa exclusivo de Private Link."),
    "MS-039": ("Sin artefacto específico", [], "No se encontró mención explícita ni programa específico de Network Watcher."),
    "MS-040": ("Parcial", ["defender_cloud"], "Defender for DevOps se cubre en el track DevOps/code-to-cloud; no programa dedicado."),
    "MS-041": ("Parcial", ["purview_dspm", "purview_ip"], "Catálogo/linaje de datos aparece en seguridad de datos y DSPM; no programa exclusivo de Data Map."),
    "MS-042": ("Directa", ["entra"], "Programa dedicado a Microsoft Entra, identidad y agentes."),
    "MS-043": ("Directa", ["purview_records"], "Programa dedicado al ciclo de vida y Records Management."),
}

OE_MAP = {
    "MS-001": ("Directa", ["xdr"], "Guía dedicada a Defender XDR."),
    "MS-002": ("Directa", ["sentinel"], "Guía dedicada a Microsoft Sentinel."),
    "MS-003": ("Parcial", ["entra", "xdr", "mdi"], "ID Protection aparece en guías de Entra/XDR/identidad; sin guía exclusiva."),
    "MS-004": ("Directa", ["mdi"], "Guía dedicada a Defender for Identity."),
    "MS-005": ("Sin artefacto específico", [], "No existe guía dedicada a Defender for Cloud en las 23 guías inventariadas."),
    "MS-006": ("Sin artefacto específico", [], "No existe guía dedicada a Defender for IoT."),
    "MS-007": ("Directa", ["mde"], "Guía dedicada a Defender for Endpoint."),
    "MS-008": ("Directa", ["intune", "intune_suite"], "Guías dedicadas a Intune Plan 1 y Suite."),
    "MS-009": ("Directa", ["purview_dlp"], "Guía dedicada a Purview DLP."),
    "MS-010": ("Directa", ["purview_ip"], "Guía dedicada a Information Protection."),
    "MS-011": ("Directa", ["purview_irm"], "Guía dedicada a Insider Risk Management."),
    "MS-012": ("Directa", ["mdca"], "Guía dedicada a Defender for Cloud Apps."),
    "MS-013": ("Parcial", ["entra", "entra_governance"], "Conditional Access forma parte de la guía Entra/Governance; no guía exclusiva."),
    "MS-014": ("Parcial", ["entra_governance", "entra"], "PIM aparece en Entra Governance/Entra; no guía exclusiva PIM."),
    "MS-015": ("Sin artefacto específico", [], "No existe guía operativa dedicada a Azure Backup."),
    "MS-016": ("Sin artefacto específico", [], "No existe guía operativa dedicada a Azure Site Recovery."),
    "MS-017": ("Parcial", ["sentinel", "xdr"], "Monitor/Log Analytics soportan SOC; no guía exclusiva del servicio."),
    "MS-018": ("Sin artefacto específico", [], "No existe guía operativa dedicada a Azure DDoS Protection."),
    "MS-019": ("Sin artefacto específico", [], "No existe guía operativa dedicada a Azure WAF."),
    "MS-020": ("Sin artefacto específico", [], "No existe guía operativa dedicada a Defender for APIs."),
    "MS-021": ("Sin artefacto específico", [], "No existe guía operativa dedicada a GHAS/Azure DevOps."),
    "MS-022": ("Parcial", ["lockbox"], "Key Vault aparece específicamente para Customer Key/Lockbox, no como guía integral de Key Vault/HSM."),
    "MS-023": ("Sin artefacto específico", [], "No existe guía operativa dedicada a Azure Policy/Guest Configuration."),
    "MS-024": ("Directa", ["security_copilot"], "Guía dedicada a Microsoft Security Copilot."),
    "MS-025": ("Parcial", ["agent365", "purview_suite"], "Guardrails/IA pueden estar cubiertos por gobierno Purview/Agent 365, no por guía del servicio Content Safety."),
    "MS-026": ("Directa", ["mdo"], "Guía dedicada a Defender for Office 365."),
    "MS-027": ("Directa", ["purview_audit", "purview_comm", "purview_suite"], "Audit/Compliance tiene guías Purview Audit y Suite; Compliance Manager se integra en la suite, no una guía exclusiva separada en este índice."),
    "MS-028": ("Parcial", ["mde", "xdr"], "Vulnerability Management está integrado a la guía MDE/XDR; no guía independiente."),
    "MS-029": ("Sin artefacto específico", [], "No existe guía operativa dedicada a Front Door/Traffic Manager."),
    "MS-030": ("Parcial", ["xdr"], "Exposure Management está incluido en la guía XDR; no guía independiente."),
    "MS-031": ("Sin artefacto específico", [], "No existe guía operativa dedicada a Microsoft Priva."),
    "MS-032": ("Sin artefacto específico", [], "No existe guía operativa dedicada a Azure Service Health."),
    "MS-033": ("Sin artefacto específico", [], "No se encontró mención explícita ni guía específica de Resource Graph."),
    "MS-034": ("Sin artefacto específico", [], "No existe guía operativa dedicada a Traffic Manager."),
    "MS-035": ("Sin artefacto específico", [], "No existe guía operativa dedicada a Front Door."),
    "MS-036": ("Sin artefacto específico", [], "No existe guía operativa dedicada a Availability Zones."),
    "MS-037": ("Sin artefacto específico", [], "No existe guía operativa dedicada a Azure Firewall."),
    "MS-038": ("Sin artefacto específico", [], "No existe guía operativa dedicada a Private Link."),
    "MS-039": ("Sin artefacto específico", [], "No existe guía operativa dedicada a Network Watcher."),
    "MS-040": ("Sin artefacto específico", [], "No existe guía operativa dedicada a Defender for DevOps."),
    "MS-041": ("Parcial", ["purview_suite"], "Data Map puede estar dentro de Purview Suite; no guía dedicada."),
    "MS-042": ("Directa", ["entra"], "Guía dedicada a Microsoft Entra ID."),
    "MS-043": ("Directa", ["purview_records"], "Guía dedicada a Data Lifecycle y Records Management."),
}



TERM_PATTERNS = {
    "MS-001": r"Defender XDR", "MS-002": r"Microsoft Sentinel", "MS-003": r"Entra ID Protection|Identity Protection",
    "MS-004": r"Defender for Identity|\bMDI\b", "MS-005": r"Defender for Cloud", "MS-006": r"Defender for IoT",
    "MS-007": r"Defender for Endpoint|\bMDE\b", "MS-008": r"Microsoft Intune|\bIntune\b", "MS-009": r"Data Loss Prevention|\bDLP\b",
    "MS-010": r"Information Protection", "MS-011": r"Insider Risk", "MS-012": r"Defender for Cloud Apps|\bMDCA\b",
    "MS-013": r"Conditional Access", "MS-014": r"Privileged Identity Management|\bPIM\b", "MS-015": r"Azure Backup",
    "MS-016": r"Azure Site Recovery|\bASR\b", "MS-017": r"Log Analytics|Azure Monitor", "MS-018": r"DDoS Protection|\bDDoS\b",
    "MS-019": r"Web Application Firewall|\bWAF\b", "MS-020": r"Defender for APIs", "MS-021": r"GitHub Advanced Security|Azure DevOps",
    "MS-022": r"Key Vault|Managed HSM", "MS-023": r"Azure Policy|Guest Configuration", "MS-024": r"Security Copilot",
    "MS-025": r"AI Content Safety|Content Safety|Prompt Shields", "MS-026": r"Defender for Office 365|\bMDO\b",
    "MS-027": r"Compliance Manager|Purview Audit", "MS-028": r"Defender Vulnerability Management|Vulnerability Management",
    "MS-029": r"Front Door.*Traffic Manager|Traffic Manager.*Front Door", "MS-030": r"Security Exposure Management|Exposure Management",
    "MS-031": r"Microsoft Priva|\bPriva\b", "MS-032": r"Azure Service Health|Service Health", "MS-033": r"Azure Resource Graph|Resource Graph|\bARG\b",
    "MS-034": r"Azure Traffic Manager|Traffic Manager", "MS-035": r"Azure Front Door|Front Door", "MS-036": r"Availability Zones?",
    "MS-037": r"Azure Firewall", "MS-038": r"Private Link", "MS-039": r"Network Watcher", "MS-040": r"Defender for DevOps",
    "MS-041": r"Purview Data Map|Data Map", "MS-042": r"Microsoft Entra|Entra ID", "MS-043": r"Records Management|Lifecycle.*Records",
}

def content_evidence(source_id, keys, catalog, base):
    if not keys:
        return ""
    hits=[]
    pattern=TERM_PATTERNS[source_id]
    for key in keys:
        rel=catalog[key][1]
        folder=(base/rel).parent
        for p in folder.rglob("*"):
            if p.suffix.lower() not in {".md", ".json"}:
                continue
            try:
                text=p.read_text(encoding="utf-8", errors="ignore")
            except OSError:
                continue
            if __import__("re").search(pattern, text, __import__("re").I):
                hits.append(p.relative_to(base).as_posix())
    return " | ".join(sorted(set(hits))[:5])


def source_rows():
    return [{"technology_id": s["source_id"], "technology": s["product"], "microsoft_area": s["area"], "learn_url": s["url"]} for s in SOURCES]


def program_evidence(keys, catalog, base):
    names=[]; paths=[]
    for key in keys:
        name, rel = catalog[key]
        p = base / rel
        assert p.exists(), p
        names.append(name)
        paths.append(rel)
    return " | ".join(names), " | ".join(paths)


def build_rows():
    result=[]
    for src in source_rows():
        sid=src["technology_id"]
        nstatus,nkeys,nwhy=NINJA_MAP[sid]
        ostatus,okeys,owhy=OE_MAP[sid]
        nn,np=program_evidence(nkeys,NINJA_PROGRAMS,NINJA) if nkeys else ("","")
        on,op=program_evidence(okeys,OE_PROGRAMS,OE) if okeys else ("","")
        if nstatus == "Parcial":
            np = content_evidence(sid,nkeys,NINJA_PROGRAMS,NINJA)
            assert np, (sid,"Ninja partial has no textual evidence")
        if ostatus == "Parcial":
            op = content_evidence(sid,okeys,OE_PROGRAMS,OE)
            assert op, (sid,"Operational excellence partial has no textual evidence")
        gap=[]
        if nstatus!="Directa": gap.append("Ninja: "+("ampliar/citar" if nstatus=="Parcial" else "crear"))
        if ostatus!="Directa": gap.append("Excelencia: "+("ampliar/citar" if ostatus=="Parcial" else "crear"))
        priority="Alta" if nstatus=="Sin artefacto específico" and ostatus=="Sin artefacto específico" else "Media" if (nstatus!="Directa" and ostatus!="Directa") else "Baja"
        result.append({**src,"ninja_status":nstatus,"ninja_programs":nn,"ninja_evidence":np,"ninja_rationale":nwhy,"operational_excellence_status":ostatus,"operational_excellence_guides":on,"operational_excellence_evidence":op,"operational_excellence_rationale":owhy,"gap_action":"; ".join(gap) or "Sin brecha de artefacto específico identificada","priority":priority})
    return result

def style_sheet(ws, title, widths=None):
    ws.freeze_panes="A2"; ws.auto_filter.ref=ws.dimensions; ws.sheet_view.showGridLines=False
    for c in ws[1]:
        c.fill=PatternFill("solid",fgColor="17365D"); c.font=Font(color="FFFFFF",bold=True); c.alignment=Alignment(wrap_text=True,vertical="center")
    for row in ws.iter_rows(min_row=2):
        for c in row: c.alignment=Alignment(wrap_text=True,vertical="top")
    ws.row_dimensions[1].height=36
    tab=Table(displayName="T"+''.join(ch for ch in title if ch.isalnum())[:24],ref=ws.dimensions)
    tab.tableStyleInfo=TableStyleInfo(name="TableStyleMedium2",showRowStripes=True)
    ws.add_table(tab)
    if widths:
        for i,w in widths.items(): ws.column_dimensions[get_column_letter(i)].width=w


def md_table(headers, rows):
    lines=["| "+" | ".join(headers)+" |","| "+" | ".join("---" for _ in headers)+" |"]
    for row in rows:
        lines.append("| "+" | ".join(str(x).replace("|","\\|").replace("\n"," ") for x in row)+" |")
    return "\n".join(lines)


def main():
    rows=build_rows()
    ninja_counts=Counter(r['ninja_status'] for r in rows); oe_counts=Counter(r['operational_excellence_status'] for r in rows)
    coverage=[
      "# Cobertura de formación Ninja y Excelencia Operacional",
      "",
      f"Fecha de corte: **{TODAY}**.",
      "",
      "Este directorio cruza las 43 capacidades Microsoft utilizadas en los mapeos de mitigación con los contenidos disponibles en:",
      f"- `{NINJA}`",
      f"- `{OE}`",
      "",
      "## Criterio",
      "",
      "- **Directa**: existe programa o guía específicamente dedicado a la tecnología o a una combinación declarada que cubre directamente el registro.",
      "- **Parcial**: la tecnología aparece como componente, módulo o workload dentro de una familia más amplia; no se debe presentar como entrenamiento/guía dedicado.",
      "- **Sin artefacto específico**: no se identificó programa o guía específica en los directorios inspeccionados.",
      "",
      "La ausencia aquí no significa ausencia de documentación Microsoft ni incapacidad del producto; significa que no existe un artefacto específico en los dos repositorios suministrados.",
      "",
      "## Resumen",
      "",
      md_table(["Repositorio","Directa","Parcial","Sin artefacto específico","Total"],[
          ["Ninja Training",ninja_counts['Directa'],ninja_counts['Parcial'],ninja_counts['Sin artefacto específico'],len(rows)],
          ["Excelencia Operacional",oe_counts['Directa'],oe_counts['Parcial'],oe_counts['Sin artefacto específico'],len(rows)],
      ]),
      "",
      "## Matriz de cobertura",
      "",
      md_table(["ID","Tecnología","Ninja","Programa/evidencia","Excelencia Operacional","Guía/evidencia"],[[r['technology_id'],r['technology'],r['ninja_status'],r['ninja_programs']+(' — '+r['ninja_evidence'] if r['ninja_evidence'] else ''),r['operational_excellence_status'],r['operational_excellence_guides']+(' — '+r['operational_excellence_evidence'] if r['operational_excellence_evidence'] else '')] for r in rows]),
      "",
      "## Regla de uso",
      "",
      "Una cobertura **Parcial** sirve para localizar material, pero debe complementarse con documentación oficial específica antes de declarar competencia o excelencia operativa. Una cobertura **Directa** tampoco elimina la necesidad de validar actualización, licencia, arquitectura y práctica efectiva.",
    ]
    (OUT/"README.md").write_text("\n".join(coverage),encoding="utf-8")
    with (OUT/"matriz-cobertura.csv").open("w",encoding="utf-8-sig",newline="") as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)

    gaps=[r for r in rows if r['ninja_status']!='Directa' or r['operational_excellence_status']!='Directa']
    double=[r for r in gaps if r['ninja_status']=='Sin artefacto específico' and r['operational_excellence_status']=='Sin artefacto específico']
    gap_text=["# Brechas y plan recomendado","","## Brecha total en ambos repositorios","",md_table(["ID","Tecnología","Acción recomendada"],[[r['technology_id'],r['technology'],r['gap_action']] for r in double]),"","## Cobertura parcial o unilateral","",md_table(["ID","Tecnología","Ninja","Excelencia Operacional","Acción","Prioridad"],[[r['technology_id'],r['technology'],r['ninja_status'],r['operational_excellence_status'],r['gap_action'],r['priority']] for r in gaps if r not in double]),"","## Orden sugerido","","1. Crear artefactos para brechas de continuidad, nube, red, OT/IoT y privacidad sin cobertura directa.","2. Convertir cobertura parcial en módulos específicos solo cuando haya suficiente profundidad, cadencia y evidencia independiente.","3. Evitar duplicar contenido transversal: enlazar Sentinel/XDR/Purview/Defender for Cloud donde ya exista y añadir el delta operativo faltante.","4. Para cada nuevo módulo, incluir objetivo, arquitectura, implementación, operación, KPI/KRI, KQL/queries, respuesta, recuperación, pruebas, licencias y fuentes oficiales."]
    (OUT/"brechas-y-recomendaciones.md").write_text("\n".join(gap_text),encoding="utf-8")

    wb=Workbook(); wb.remove(wb.active)
    ws=wb.create_sheet("Cobertura 43 tecnologías"); ws.append(list(rows[0]));
    for r in rows: ws.append([r[k] for k in rows[0]])
    style_sheet(ws,"Cobertura43",{1:14,2:38,3:60,4:68,5:20,6:46,7:70,8:70,9:22,10:46,11:70,12:72,13:72,14:16})
    ws2=wb.create_sheet("Resumen")
    ws2.append(["Repositorio","Directa","Parcial","Sin artefacto específico","Total"])
    ws2.append(["Ninja Training",ninja_counts['Directa'],ninja_counts['Parcial'],ninja_counts['Sin artefacto específico'],len(rows)])
    ws2.append(["Excelencia Operacional",oe_counts['Directa'],oe_counts['Parcial'],oe_counts['Sin artefacto específico'],len(rows)])
    style_sheet(ws2,"Resumen",{1:32,2:16,3:16,4:26,5:12})
    ws3=wb.create_sheet("Brechas")
    ws3.append(["ID","Tecnología","Ninja","Excelencia Operacional","Acción recomendada","Prioridad"])
    for r in gaps: ws3.append([r['technology_id'],r['technology'],r['ninja_status'],r['operational_excellence_status'],r['gap_action'],r['priority']])
    style_sheet(ws3,"Brechas",{1:14,2:38,3:24,4:26,5:76,6:14})
    ws4=wb.create_sheet("Catálogo local")
    ws4.append(["Tipo","ID/clave","Nombre del programa o guía","Evidencia local relativa"])
    for key,(name,path) in NINJA_PROGRAMS.items(): ws4.append(["Ninja Training",key,name,path])
    for key,(name,path) in OE_PROGRAMS.items(): ws4.append(["Excelencia Operacional",key,name,path])
    style_sheet(ws4,"CatalogoLocal",{1:24,2:18,3:54,4:95})
    path=OUT/"matriz-cobertura-formacion-excelencia.xlsx"; wb.save(path)
    check=load_workbook(path,read_only=True); assert check.sheetnames; check.close()

    manifest=[]
    for p in sorted(OUT.rglob('*')):
        if p.is_file() and p.name!='MANIFEST.json':
            b=p.read_bytes(); manifest.append({'path':p.relative_to(OUT).as_posix(),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
    (OUT/'MANIFEST.json').write_text(json.dumps({'version':'1.0.0','generated_at':TODAY,'technologies':len(rows),'ninja_summary':dict(ninja_counts),'operational_excellence_summary':dict(oe_counts),'source_directories':[str(NINJA),str(OE)],'files':manifest},ensure_ascii=False,indent=2),encoding='utf-8')
    print('technologies',len(rows))
    print('ninja',dict(ninja_counts),'oe',dict(oe_counts),'gaps',len(gaps),'total gaps',len(double))

if __name__=='__main__': main()

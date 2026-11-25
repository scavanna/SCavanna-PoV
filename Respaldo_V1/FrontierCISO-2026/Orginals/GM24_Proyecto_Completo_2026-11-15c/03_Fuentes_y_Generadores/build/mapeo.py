# -*- coding: utf-8 -*-
"""Motor de mapeo GM-24 V7/V7.1 (379 conceptos) → NIST / ISACA / MITRE / OWASP / CIS / CSA.
Herencia de unidad (Parcial) + reglas por palabra clave sobre K (Fuerte) + explícitos AMP/HC/PA. Vínculo: cubre | instancia | referencia."""
import re, collections
import data as D, v7 as V, estandares as S

F = ["NIST CSF 2.0","NIST RMF","NIST SP 800-53","NIST AI RMF","NIST AI 600-1","NIST otros","ISACA CISM 2026","ISACA CRISC 2025","ISACA AAISM","MITRE ATT&CK","MITRE ATLAS","MITRE D3FEND","OWASP LLM Top 10 2025","OWASP Agentic Top 10 2026","OWASP otros","CIS Controls v8.1","CIS otros","CSA CCM v4","CSA AICM","CSA otros"]
KEY = {"csf":"NIST CSF 2.0","rmf":"NIST RMF","sp53":"NIST SP 800-53","airmf":"NIST AI RMF","ai600":"NIST AI 600-1","nist":"NIST otros","cism":"ISACA CISM 2026","crisc":"ISACA CRISC 2025","aaism":"ISACA AAISM","attack":"MITRE ATT&CK","atlas":"MITRE ATLAS","d3":"MITRE D3FEND","llm":"OWASP LLM Top 10 2025","asi":"OWASP Agentic Top 10 2026","owasp":"OWASP otros","cis":"CIS Controls v8.1","cisx":"CIS otros","ccm":"CSA CCM v4","aicm":"CSA AICM","csa":"CSA otros"}
def m(**kw): return {KEY[k]: [(e if isinstance(e, tuple) else (e,"cubre","Fuerte")) for e in v] for k,v in kw.items()}
def P(*els): return [(e,"referencia","Parcial") for e in els]
def R(*els): return [(e,"referencia","Informativo") for e in els]

UNIT_BASE = {
 "G1.1": m(csf=P("GV.OC","GV.RR"), rmf=P("Prepare"), sp53=P("PM"), cism=P("CISM-1A"), crisc=P("CRISC-1A"), aaism=P("AAISM-1A"), ccm=P("GRC"), cis=R("CIS 14")),
 "G1.2": m(csf=P("GV.OC","GV.RM"), rmf=P("Prepare"), sp53=P("PM","PL"), cism=P("CISM-1B"), crisc=P("CRISC-1A","CRISC-1B"), aaism=P("AAISM-1B"), ccm=P("GRC")),
 "G2.1": m(csf=P("GV.PO","GV.OV"), rmf=P("Prepare","Select"), sp53=P("PL","PM"), cism=P("CISM-1B"), crisc=P("CRISC-1B"), aaism=P("AAISM-1A"), ccm=P("GRC"), cisx=R("CIS RAM"), csa=R("STAR / STAR for AI")),
 "G2.2": m(csf=P("GV.PO"), rmf=P("Prepare"), sp53=P("PL","PM"), cism=P("CISM-3A"), crisc=P("CRISC-1A"), aaism=P("AAISM-1B"), ccm=P("GRC","CCC")),
 "G3.1": m(csf=P("GV.OC","GV.PO"), sp53=P("PT","PM"), nist=P("NIST PF"), cism=P("CISM-1A"), crisc=P("CRISC-1B"), aaism=P("AAISM-1A","AAISM-3D"), ccm=P("GRC","DSP")),
 "G3.2": m(csf=P("GV.OV","ID.IM"), rmf=P("Assess","Monitor"), sp53=P("CA","AU"), cism=P("CISM-3B"), crisc=P("CRISC-3C"), aaism=P("AAISM-1D","AAISM-3E"), ccm=P("A&A","GRC")),
 "G4.1": m(csf=P("GV.RM","GV.RR"), rmf=P("Prepare"), sp53=P("PM","RA"), nist=P("SP 800-30"), cism=P("CISM-2A"), crisc=P("CRISC-1B"), aaism=P("AAISM-2A"), ccm=P("GRC")),
 "G4.2": m(csf=P("GV.RM"), rmf=P("Prepare"), sp53=P("PM","RA"), cism=P("CISM-2B"), crisc=P("CRISC-1B"), aaism=P("AAISM-2A"), ccm=P("GRC")),
 "G5.1": m(csf=P("ID.RA","GV.OV"), rmf=P("Prepare","Assess"), sp53=P("RA","CA"), nist=P("SP 800-30"), cism=P("CISM-2A"), crisc=P("CRISC-2A","CRISC-2B"), aaism=P("AAISM-2A","AAISM-2B"), ccm=P("GRC","TVM")),
 "G5.2": m(csf=P("GV.RM","ID.RA"), rmf=P("Authorize"), sp53=P("CA","RA"), cism=P("CISM-2B"), crisc=P("CRISC-3A"), aaism=P("AAISM-2A"), ccm=P("GRC")),
 "G6.1": m(csf=P("GV.OV","RS.CO"), sp53=P("PM"), cism=P("CISM-1A","CISM-3B"), crisc=P("CRISC-3C"), aaism=P("AAISM-1D"), ccm=P("GRC")),
 "G6.2": m(csf=P("GV.RR","GV.OV","ID.IM"), sp53=P("PM"), cism=P("CISM-1A"), crisc=P("CRISC-1A","CRISC-3C"), aaism=P("AAISM-3D"), ccm=P("GRC","HRS")),
 "M1.1": m(csf=P("GV.RR","GV.OC"), rmf=P("Prepare"), sp53=P("PM"), cism=P("CISM-3A","CISM-3B"), crisc=P("CRISC-1A"), aaism=P("AAISM-1D"), ccm=P("GRC")),
 "M1.2": m(csf=P("GV.RR","GV.SC","PR.AT"), sp53=P("PM","SA","AT"), cism=P("CISM-3B"), crisc=P("CRISC-1A"), aaism=P("AAISM-1D","AAISM-2C"), ccm=P("GRC","HRS","STA"), cis=P("CIS 14","CIS 15")),
 "M2.1": m(csf=P("ID.AM","PR.DS"), rmf=P("Categorize"), sp53=P("CM","MP","PT"), cism=P("CISM-3A"), crisc=P("CRISC-1A","CRISC-4B"), aaism=P("AAISM-1C","AAISM-3C"), ccm=P("DSP","DCS"), cis=P("CIS 1","CIS 2","CIS 3")),
 "M2.2": m(csf=P("PR.AA"), sp53=P("AC","IA"), nist=P("SP 800-207"), cism=P("CISM-3A"), crisc=P("CRISC-4B"), aaism=P("AAISM-3A","AAISM-3E"), ccm=P("IAM"), cis=P("CIS 5","CIS 6")),
 "M3.1": m(csf=P("PR.PS","PR.IR"), rmf=P("Select","Implement"), sp53=P("SA","SC","PL"), nist=P("SP 800-207"), cism=P("CISM-3A"), crisc=P("CRISC-4A"), aaism=P("AAISM-3A"), ccm=P("IVS","AIS"), cis=P("CIS 4","CIS 12")),
 "M3.2": m(csf=P("PR.PS","ID.IM"), rmf=P("Select","Implement","Assess"), sp53=P("CA","CM"), cism=P("CISM-3A","CISM-3B"), crisc=P("CRISC-3B"), aaism=P("AAISM-3B","AAISM-3E"), ccm=P("A&A","CCC"), cis=P("CIS 4","CIS 18")),
 "M4.1": m(csf=P("DE.CM","DE.AE","RS.AN"), rmf=P("Monitor"), sp53=P("AU","SI","IR"), nist=P("SP 800-61"), cism=P("CISM-4B"), crisc=P("CRISC-3C","CRISC-4B"), aaism=P("AAISM-3E","AAISM-1E"), ccm=P("LOG","SEF"), cis=P("CIS 8","CIS 13"), d3=P("D3FEND Detect")),
 "M4.2": m(csf=P("ID.RA","DE.AE"), sp53=P("RA","SI"), cism=P("CISM-2A"), crisc=P("CRISC-2A"), aaism=P("AAISM-2B"), ccm=P("TVM"), cis=P("CIS 7"), attack=P("TA0043 Reconnaissance","TA0001 Initial Access"), d3=P("D3FEND Model")),
 "M5.1": m(csf=P("RS.MA","GV.OC"), sp53=P("IR","CP"), nist=P("SP 800-61"), cism=P("CISM-4A"), crisc=P("CRISC-1A"), aaism=P("AAISM-1E"), ccm=P("SEF","BCR"), cis=P("CIS 17")),
 "M5.2": m(csf=P("RS.AN","RS.MI","RS.CO","RC.CO"), sp53=P("IR","AU"), nist=P("SP 800-61"), cism=P("CISM-4B"), crisc=P("CRISC-3A"), aaism=P("AAISM-1E"), ccm=P("SEF"), cis=P("CIS 17"), d3=P("D3FEND Isolate","D3FEND Evict")),
 "M6.1": m(csf=P("RC.RP","PR.IR"), sp53=P("CP"), cism=P("CISM-4A"), crisc=P("CRISC-1A"), aaism=P("AAISM-1E","AAISM-2C"), ccm=P("BCR"), cis=P("CIS 11"), d3=P("D3FEND Restore")),
 "M6.2": m(csf=P("GV.SC","PR.PS","PR.DS"), sp53=P("SA","SR","SC"), nist=P("SP 800-161"), cism=P("CISM-3A"), crisc=P("CRISC-4A"), aaism=P("AAISM-2C","AAISM-3A","AAISM-3B"), ccm=P("STA","IVS","AIS","UEM"), cis=P("CIS 12","CIS 15","CIS 16"), owasp=P("SAMM Implementation")),
}

K_RULES = [
 (r"Tres Líneas|Roles y Responsabilidades|Supervisión\b|Rendición", m(csf=["GV.RR","GV.OV"], cism=["CISM-1A"], crisc=["CRISC-1B"], airmf=P("GOVERN-2"))),
 (r"NIST CSF|Marcos de Gobierno|Estándares Relevantes|Estándares de Seguridad|Interoperabilidad|Adaptación \(Tailoring\)|COBIT|ISO 27001|SGSI|Familias de Controles", m(csf=["GV.PO","GV.OV"], rmf=["Prepare","Select"], sp53=["PL","PM"], cism=["CISM-1B"], crisc=["CRISC-1B"], ccm=["GRC"])),
 (r"Medición de Madurez|Efectividad Programa|Medición Rendimiento|Métricas|KPIs", m(csf=["GV.OV","ID.IM"], cism=["CISM-3B"], crisc=["CRISC-3C"], sp53=["PM"])),
 (r"Jerarquía Documental|Procedimientos|Aplicación \(Enforcement\)|Mantenimiento|Control de Versiones|Desarrollo de Políticas", m(csf=["GV.PO"], cism=["CISM-3A"], crisc=["CRISC-1A"], sp53=["PL"], ccm=["GRC","CCC"])),
 (r"Excepciones", m(csf=["GV.PO","GV.RM"], crisc=["CRISC-3A"], ccm=["GRC"])),
 (r"Privacidad|Datos Personales", m(csf=["GV.OC","PR.DS"], sp53=["PT"], nist=["NIST PF"], ccm=["DSP"], cis=["CIS 3"], aaism=P("AAISM-3D"))),
 (r"Obligaciones Contractuales|Responsabilidad Legal|Leyes|Regulaciones|Regulatorio|Cumplimiento|Identificación de Requisitos|Riesgos Legales|Reguladores|Notificación|Implicaciones CISO", m(csf=["GV.OC","RS.CO"], cism=["CISM-1A"], crisc=["CRISC-1B"], ccm=["GRC"])),
 (r"Aseguramiento Continuo|Automatización|Auditoría|^Aseguramiento$|Integración Gobierno", m(csf=["GV.OV","ID.IM"], rmf=["Monitor","Assess"], sp53=["CA","AU"], ccm=["A&A"], cis=["CIS 8"])),
 (r"Gestión de Evidencia", m(csf=["GV.OV"], sp53=["AU","CA"], ccm=["A&A","LOG"])),
 (r"Apetito|Tolerancia|Aceptación Formal|Autorización Residual|Evitación|Gestión Residual", m(csf=["GV.RM"], rmf=["Authorize"], cism=["CISM-2B"], crisc=["CRISC-1B","CRISC-3A"], sp53=["CA","RA"])),
 (r"Marcos de Riesgo|Escenarios de Riesgo|Monitorización Continua|Herramientas GRC|Evaluación de Riesgo|Análisis de Riesgo|Metodologías|Identificación de Brechas|Análisis Cuanti|Evaluación Amenazas|Evaluación Organizacional", m(csf=["ID.RA","GV.RM"], rmf=["Prepare","Assess"], sp53=["RA"], nist=["SP 800-30"], cism=["CISM-2A"], crisc=["CRISC-2A","CRISC-2B","CRISC-3C"], ccm=["GRC"], cisx=P("CIS RAM"))),
 (r"Mitigación|Tratamiento|Respuesta al Riesgo|Controles Compensatorios", m(csf=["ID.RA","GV.RM"], cism=["CISM-2B"], crisc=["CRISC-3A","CRISC-3B"], sp53=["RA","CA"])),
 (r"Reportes Factuales|Lenguaje de Negocio|Comunicación|Junta|Ejecutivos|Interesados|Reporte a Dirección|Rol Ejecutivo|Talleres|Expectativas|Narrativa", m(csf=["GV.OC","GV.OV","RS.CO"], cism=["CISM-1A"], crisc=["CRISC-3C"], sp53=["PM"])),
 (r"Étic|Debida Diligencia|Conflictos|Confidencialidad|Conducta Profesional", m(csf=["GV.RR"], cism=["CISM-1A"], crisc=["CRISC-1A"], ccm=["HRS"], airmf=P("GOVERN-4"))),
 (r"Oficina del CISO|Alcance y Objetivos|Recursos|Ciclo de Vida\b|Programa|Procesos de Gestión", m(csf=["GV.RR","GV.OC"], cism=["CISM-3A","CISM-3B"], crisc=["CRISC-1A"], sp53=["PM"])),
 (r"Presupuesto|Optimización Recursos|ROI|Casos de Negocio|Financ|Socio de Negocio|Conexión de Valor|Enfoque en Negocio|Balance Riesgo|Habilitador", m(csf=["GV.RM","GV.OC"], cism=["CISM-1B","CISM-3B"], crisc=["CRISC-1A"], sp53=["PM"])),
 (r"RFI/RFP|Adquisición|Licenciamiento|Proveedor|Terceros|TPRM|Responsabilidad Compartida|Cadena de Suministro|SBOM|C-SCRM", m(csf=["GV.SC"], sp53=["SA","SR"], nist=["SP 800-161"], cism=["CISM-3B"], crisc=["CRISC-1A"], ccm=["STA"], cis=["CIS 15"], airmf=P("GOVERN-6","MANAGE-3"))),
 (r"Liderazgo de Equipo|Capacitación|Gestión Talento|Habilidades|Concienciación|Cultura de Seguridad|Concientización|Liderazgo", m(csf=["PR.AT","GV.RR"], sp53=["AT","PS"], cism=["CISM-3B"], ccm=["HRS"], cis=["CIS 14"])),
 (r"Inventario|Clasificación\b|Activos", m(csf=["ID.AM"], rmf=["Categorize"], sp53=["CM","RA"], cism=["CISM-3A"], crisc=["CRISC-1A"], ccm=["DSP","DCS"], cis=["CIS 1","CIS 2"])),
 (r"Gobernanza Datos|Ciclo de Vida de Datos|Retención|Destrucción|Protección de Datos|Cifrado|Datos en|Reposo/Tránsito|Riesgos de Datos", m(csf=["PR.DS"], sp53=["MP","SC","PT"], ccm=["DSP","CEK"], cis=["CIS 3"], aaism=P("AAISM-3C"), attack=P("TA0010 Exfiltration","TA0009 Collection"))),
 (r"Autenticación|Autorización|PAM|Privilegiados|Identidad|IAM|Contexto de Acceso|Control de Acceso|Mínimo Privilegio|Federación", m(csf=["PR.AA"], sp53=["AC","IA"], cism=["CISM-3A"], crisc=["CRISC-4B"], ccm=["IAM"], cis=["CIS 5","CIS 6"], attack=P("TA0006 Credential Access","TA0004 Privilege Escalation"), d3=P("D3FEND Harden"))),
 (r"Zero Trust|ZTNA", m(csf=["PR.AA","PR.PS"], nist=["SP 800-207"], cism=["CISM-3A"], ccm=["IAM","IVS"], csa=["Zero Trust Advancement Center"], d3=P("D3FEND Harden"))),
 (r"Arquitectura|TOGAF|Diseño Seguro|Defensa en Profundidad|Resiliencia \(Diseño\)|Ingeniería", m(csf=["PR.PS","PR.IR"], rmf=["Select","Implement"], sp53=["SA","SC","PL"], cism=["CISM-1B","CISM-3A"], crisc=["CRISC-4A"], ccm=["IVS","AIS"], owasp=P("SAMM Design"))),
 (r"Controles de Seguridad|Selección y Adaptación|Implementación|SP 800-53|POA&M|Documentación", m(csf=["PR.PS","ID.IM"], rmf=["Select","Implement"], sp53=["CA","CM","PL"], cism=["CISM-3A"], crisc=["CRISC-3B"], ccm=["CCC"], cis=["CIS 4"])),
 (r"Evaluación \(Assess\)|Pruebas de Efectividad|Pentest|Penetración|Vulnerabilidad", m(csf=["ID.RA","ID.IM"], rmf=["Assess"], sp53=["CA","RA","SI"], cism=["CISM-3B"], crisc=["CRISC-3B","CRISC-3C"], ccm=["A&A","TVM"], cis=["CIS 7","CIS 18"], owasp=P("SAMM Verification"))),
 (r"SOC Moderno|SIEM|XDR|Detección|Monitorización Continua", m(csf=["DE.CM","DE.AE"], rmf=["Monitor"], sp53=["AU","SI","IR"], cism=["CISM-4B"], crisc=["CRISC-4B"], ccm=["LOG"], cis=["CIS 8","CIS 13"], d3=["D3FEND Detect"])),
 (r"SOAR", m(csf=["RS.MI","DE.AE"], sp53=["IR","SI"], cism=["CISM-4B"], ccm=["SEF"], cis=["CIS 17"])),
 (r"Threat Hunting|TTPs|IoC|Threat Intelligence|Inteligencia|Indicadores", m(csf=["DE.CM","ID.RA"], sp53=["SI","RA"], cism=["CISM-4B","CISM-2A"], crisc=["CRISC-2A"], ccm=["TVM","LOG"], cis=["CIS 13"], attack=["TA0043 Reconnaissance","TA0001 Initial Access","TA0002 Execution","TA0003 Persistence","TA0005 Defense Evasion","TA0007 Discovery","TA0011 Command and Control","TA0010 Exfiltration"], d3=["D3FEND Detect","D3FEND Model"])),
 (r"IA en SecOps", m(csf=["DE.AE","RS.AN"], airmf=["MAP-3","MANAGE-1"], aaism=["AAISM-3E"], cism=["CISM-4B"], llm=P("LLM06"), asi=P("ASI01","ASI09"))),
 (r"Modelado de Amenazas|Superficie de Ataque|Riesgos Emergentes|Priorización por Riesgo|Amenaza Interna|Híbrid|STRIDE", m(csf=["ID.RA"], sp53=["RA","SA"], cism=["CISM-2A"], crisc=["CRISC-2A"], ccm=["TVM"], cis=["CIS 7"], attack=["TA0043 Reconnaissance","TA0042 Resource Development","TA0001 Initial Access"], d3=["D3FEND Model"], owasp=P("SAMM Design"))),
 (r"RaaS|Ransomware|Economía del Cibercrimen|Modelos de Negocio Criminal", m(csf=["ID.RA","RC.RP"], sp53=["RA","CP"], cism=["CISM-2A"], crisc=["CRISC-2A"], ccm=["TVM","BCR"], cis=["CIS 10","CIS 11"], attack=["TA0040 Impact","TA0010 Exfiltration","TA0008 Lateral Movement","TA0007 Discovery"], d3=["D3FEND Restore"])),
 (r"Gestión Vulnerabilidades|Causa Raíz", m(csf=["ID.RA","ID.IM"], sp53=["RA","SI","CA"], crisc=["CRISC-2A","CRISC-3B"], ccm=["TVM"], cis=["CIS 7"])),
 (r"Playbooks|Clasificación Incidentes|Cadena de Mando|Tabletop|IRP|Preparación|BIA|Equipos de Respuesta|CSIRT", m(csf=["RS.MA","GV.OC"], sp53=["IR","CP"], nist=["SP 800-61"], cism=["CISM-4A"], crisc=["CRISC-1A"], ccm=["SEF","BCR"], cis=["CIS 17"])),
 (r"Triaje|Contención|Erradicación|Recuperación|Post-Mortem|Forense|Lecciones|Crisis", m(csf=["RS.AN","RS.MI","RS.CO","RC.CO","ID.IM"], sp53=["IR","AU"], nist=["SP 800-61"], cism=["CISM-4B"], crisc=["CRISC-3A"], ccm=["SEF"], cis=["CIS 17"], d3=["D3FEND Isolate","D3FEND Evict","D3FEND Restore"])),
 (r"Dependencias|Resiliencia Operativa|Pruebas Continuidad|BCP|DRP|BCDR|Continuidad|Recuperación ante|RTO/RPO|ISO 22301|Backups|Alta Disponibilidad|Sitio Alternativo", m(csf=["RC.RP","PR.IR","GV.OC"], sp53=["CP"], cism=["CISM-4A"], crisc=["CRISC-1A"], ccm=["BCR"], cis=["CIS 11"], d3=["D3FEND Restore"])),
 (r"Seguridad IA|Inteligencia Artificial|IA\b", m(csf=["GV.SC","ID.RA"], airmf=["MAP-1","MAP-4","MANAGE-1"], ai600=P("GAI-InfoSec","GAI-ValueChain"), aaism=["AAISM-2B","AAISM-3A","AAISM-3E"], atlas=["ATLAS AI Model Access","ATLAS AI Attack Staging"], llm=["LLM01","LLM02","LLM03","LLM06"], asi=P("ASI01","ASI02","ASI03"), aicm=["MDS","AIS-11"], csa=["MAESTRO (threat modeling agéntico)"])),
 (r"Shadow AI", m(csf=["ID.AM","GV.PO"], airmf=["MAP-1","GOVERN-1"], aaism=["AAISM-1C"], asi=["ASI10"], aicm=["AICM (dominios CCM)"], cis=["CIS 2"])),
 (r"Seguridad Nube|Multicloud|Híbrido|IaaS|PaaS|SaaS|Nube", m(csf=["PR.PS","GV.SC"], sp53=["SA","SC"], crisc=["CRISC-4A"], ccm=["IVS","IPY","STA"], cisx=["CIS Benchmarks"], csa=["STAR / STAR for AI"])),
 (r"IoT|OT\b|Industriales", m(csf=["PR.PS","ID.AM"], sp53=["SC","CM"], crisc=["CRISC-4A"], ccm=["UEM","IVS"], cis=["CIS 1","CIS 4"])),
 (r"DevSecOps|SDLC|AppSec|Desarrollo|Aplicaciones", m(csf=["PR.PS","GV.SC"], sp53=["SA","SI"], cism=["CISM-3A"], crisc=["CRISC-4A"], ccm=["AIS","CCC"], cis=["CIS 16"], owasp=["SAMM Governance","SAMM Design","SAMM Implementation","SAMM Verification","SAMM Operations","OWASP ASVS","OWASP Top 10 2021"])),
 (r"Redes|Red\b|Firewall|IDS|Segmentación|Comunicaciones|VPN", m(csf=["PR.PS","PR.IR","DE.CM"], sp53=["SC","AC"], crisc=["CRISC-4A"], ccm=["IVS"], cis=["CIS 12","CIS 13"], attack=["TA0008 Lateral Movement","TA0011 Command and Control"])),
 (r"Malware|Correo|Phishing|Email|Navegador", m(csf=["PR.PS","DE.CM"], sp53=["SI"], ccm=["TVM","UEM"], cis=["CIS 9","CIS 10"], attack=["TA0001 Initial Access","TA0002 Execution"])),
 (r"Endpoint|Dispositivo|Puesto de Trabajo", m(csf=["PR.PS","DE.CM"], sp53=["CM","SI"], ccm=["UEM"], cis=["CIS 4","CIS 10"])),
 (r"Blockchain", m(csf=["ID.RA"], crisc=["CRISC-4A"], ccm=["CEK"])),
 (r"Estrategia|Planificación Estratégica|Tendencias|Influencias|Visión|Alineación|Integración ERM|Enfoque Organizacional|Gestión Avanzada|Perfil de Riesgo|Gestión Estratégica", m(csf=["GV.OC","GV.RM"], rmf=["Prepare"], cism=["CISM-1B"], crisc=["CRISC-1A","CRISC-1B"], sp53=["PM"])),
 (r"Principios de Gobierno|Gobierno vs|Gobierno Corporativo|Estructura|Contexto|Arquetipos|PyME|Cultura", m(csf=["GV.OC","GV.RR"], cism=["CISM-1A"], crisc=["CRISC-1A"], ccm=["GRC"])),
 (r"Mejora Continua|Lecciones Aprendidas|O-ISM3|Madurez", m(csf=["ID.IM"], rmf=["Monitor"], cism=["CISM-3B"], crisc=["CRISC-3C"], ccm=["GRC"])),
 (r"Evolución Histórica", m(csf=R("GV.OC"), cism=R("CISM-1B"))),
 (r"CSF 2.0 completo", m(csf=list(S.CSF), rmf=["Prepare","Select"], cism=["CISM-1B","CISM-1A"], crisc=["CRISC-1B"], sp53=["PL","PM"], ccm=["GRC"])),
 (r"Arquitectura empresarial y arquitectura de seguridad", m(csf=["GV.OC","PR.PS","GV.RM"], rmf=["Select","Implement"], sp53=["PL","SA","PM"], nist=["SP 800-207"], cism=["CISM-1B","CISM-3A"], crisc=["CRISC-4A","CRISC-1A"], aaism=["AAISM-3A"], ccm=["GRC","IVS","AIS"], owasp=["SAMM Design"])),
 (r"Deception y señuelos", m(csf=["DE.CM","DE.AE"], sp53=["SI","AU","SC"], cism=["CISM-4B"], crisc=["CRISC-4B"], ccm=["LOG","TVM"], cis=["CIS 13","CIS 8"], d3=["D3FEND Deceive","D3FEND Detect"], attack=["TA0006 Credential Access","TA0007 Discovery","TA0009 Collection"], asi=["ASI10","ASI03"])),
 (r"Escalamiento de privilegios", m(csf=["ID.RA","PR.AA","DE.CM"], sp53=["AC","RA","SI"], cism=["CISM-2A","CISM-3A"], crisc=["CRISC-2A","CRISC-4B"], aaism=["AAISM-2B","AAISM-3E"], ccm=["IAM","TVM"], cis=["CIS 5","CIS 6"], attack=["TA0004 Privilege Escalation","TA0006 Credential Access","TA0003 Persistence"], atlas=["ATLAS Privilege Escalation","ATLAS Credential Access"], llm=["LLM06"], asi=["ASI03","ASI02"], owasp=["OWASP NHI Top 10"], aicm=["IAM-19"], d3=["D3FEND Harden","D3FEND Detect"])),
 (r"Seguridad física, ambiental y mantenimiento", m(csf=["PR.IR","PR.PS","GV.SC"], sp53=["PE","MA","CP"], cism=["CISM-3A"], crisc=["CRISC-4A"], ccm=["DCS","BCR","STA"], cis=["CIS 11"])),
]
K_FALLBACK = [(r"^G", m(csf=["GV.OC"], cism=["CISM-1A"], crisc=["CRISC-1A"])),(r"^M", m(csf=["PR.PS"], cism=["CISM-3A"], crisc=["CRISC-4A"]))]

AMP_MAP = {
 "AMP-01": m(csf=P("GV.RR"), airmf=P("GOVERN-4"), cism=P("CISM-1A"), aaism=P("AAISM-1A"), ai600=P("GAI-HAI")),
 "AMP-02": m(csf=P("GV.RR"), airmf=["GOVERN-4","MAP-5"], ai600=["GAI-HAI","GAI-Confab"], aaism=["AAISM-3D"], asi=["ASI09"], cism=P("CISM-1A")),
 "AMP-03": m(csf=["GV.RR"], airmf=["GOVERN-2"], aaism=["AAISM-1A","AAISM-1B"], cism=["CISM-1A"], crisc=["CRISC-1B"], asi=P("ASI10"), ccm=P("GRC")),
 "AMP-04": m(csf=["GV.RM","GV.OC"], airmf=["MAP-1","MANAGE-2"], aaism=["AAISM-1B"], cism=["CISM-1B"], crisc=["CRISC-1A"]),
 "AMP-05": m(csf=P("GV.OC"), airmf=P("MAP-1"), cism=P("CISM-1B")),
 "AMP-06": m(csf=["GV.PO","GV.RM","GV.OV"], airmf=["GOVERN-1","GOVERN-2","MAP-1"], aaism=["AAISM-1A","AAISM-1B","AAISM-1D"], cism=["CISM-1A","CISM-1B"], crisc=["CRISC-1B"], aicm=["AICM (dominios CCM)"], csa=["NIST AI RMF Agentic Profile (borrador CSA)"], ccm=["GRC"]),
 "AMP-07": m(csf=["GV.OC","GV.RM","GV.RR","GV.PO","GV.OV","GV.SC"], cism=["CISM-1A","CISM-1B"], crisc=["CRISC-1B"], rmf=["Prepare"]),
 "AMP-08": m(csf=["GV.PO"], airmf=P("GOVERN-1"), aaism=P("AAISM-1A"), cism=P("CISM-1B"), crisc=P("CRISC-1B"), ccm=P("GRC"), csa=P("STAR / STAR for AI")),
 "AMP-09": m(csf=["GV.PO","PR.PS"], sp53=["CM","PL"], cism=["CISM-3A"], crisc=["CRISC-3B"], ccm=["CCC","GRC"], cis=["CIS 4"], cisx=["CIS Benchmarks"]),
 "AMP-10": m(csf=["GV.PO","GV.RM"], sp53=["CM","CA"], crisc=["CRISC-3A","CRISC-3C"], ccm=["CCC","GRC"], airmf=P("MANAGE-4")),
 "AMP-11": m(csf=["GV.OC","PR.DS"], sp53=["PT","SC"], nist=["NIST PF"], aaism=["AAISM-1A","AAISM-3C"], ai600=["GAI-Privacy"], ccm=["DSP","CEK"], cism=P("CISM-1A")),
 "AMP-12": m(csf=["GV.RR","GV.SC"], airmf=["GOVERN-2","GOVERN-6"], aaism=["AAISM-1A","AAISM-2C"], cism=["CISM-1A"], crisc=["CRISC-1B"], asi=["ASI10","ASI03"], ccm=["STA","GRC"], cis=P("CIS 15")),
 "AMP-13": m(csf=["GV.OV","ID.IM"], rmf=["Monitor","Assess"], sp53=["CA","AU"], airmf=["MEASURE-3"], aaism=["AAISM-3E"], cism=["CISM-3B"], crisc=["CRISC-3C"], ccm=["A&A","LOG"], cis=["CIS 8"]),
 "AMP-14": m(csf=["GV.OV"], rmf=["Assess"], airmf=["MEASURE-2","MEASURE-4"], aaism=["AAISM-3D","AAISM-3E"], ai600=["GAI-Confab","GAI-HAI"], crisc=["CRISC-3C"], ccm=["A&A"]),
 "AMP-15": m(csf=["GV.RM","ID.RA","GV.SC"], sp53=["RA","SR"], airmf=["MAP-4","MAP-5"], aaism=["AAISM-2A"], cism=["CISM-2A"], crisc=["CRISC-1B","CRISC-2A"], asi=["ASI08"], ccm=["GRC","STA"]),
 "AMP-16": m(csf=P("GV.RM","ID.IM"), airmf=P("MEASURE-3"), crisc=P("CRISC-1B"), cism=P("CISM-1B")),
 "AMP-17": m(csf=["GV.RM","GV.RR"], airmf=["GOVERN-1","GOVERN-2","MANAGE-1"], aaism=["AAISM-1B","AAISM-2A"], cism=["CISM-2B"], crisc=["CRISC-1B"], llm=["LLM06"], asi=["ASI03","ASI10"], aicm=["AIS-11","IAM-19"], ccm=["GRC","IAM"]),
 "AMP-18": m(csf=["GV.RM","PR.AA"], airmf=["MANAGE-1","MANAGE-4"], aaism=["AAISM-2A","AAISM-3E"], ai600=["GAI-HAI"], crisc=["CRISC-1B","CRISC-3B"], llm=["LLM06"], asi=["ASI02","ASI03","ASI08"], aicm=["AIS-11","IAM-19"], ccm=["IAM","AIS"]),
 "AMP-19": m(csf=["ID.RA","GV.OV"], airmf=["MEASURE-1","MEASURE-2"], ai600=["GAI-Confab","GAI-InfoInt"], aaism=["AAISM-3D"], crisc=["CRISC-2B"]),
 "AMP-20": m(csf=["ID.RA","GV.SC"], sp53=["RA","SR"], airmf=["MAP-4","MEASURE-2","MANAGE-3"], ai600=["GAI-Confab","GAI-Bias","GAI-ValueChain"], aaism=["AAISM-2A","AAISM-2B","AAISM-3B"], cism=["CISM-2A"], crisc=["CRISC-2A","CRISC-2B"], llm=["LLM03","LLM04","LLM09"], atlas=["ATLAS AI Model Access","ATLAS AI Attack Staging"], aicm=["MDS"], ccm=["TVM"]),
 "AMP-21": m(csf=["GV.RM","ID.IM"], airmf=["MANAGE-2"], aaism=["AAISM-1D"], crisc=["CRISC-3A"], ccm=["CCC"], asi=P("ASI08")),
 "AMP-22": m(csf=["GV.RM"], rmf=["Authorize"], sp53=["CA"], airmf=["MANAGE-1","GOVERN-2"], aaism=["AAISM-2A","AAISM-1D"], cism=["CISM-2B"], crisc=["CRISC-3A"], asi=["ASI10"], aicm=["AIS-11"], ccm=["GRC"]),
 "AMP-23": m(csf=["GV.OV","RS.CO"], airmf=["GOVERN-5"], cism=["CISM-1A"], crisc=["CRISC-3C"], ccm=["GRC"]),
 "AMP-24": m(csf=["GV.OV","RS.CO"], airmf=["MEASURE-1"], cism=["CISM-1A"], crisc=["CRISC-3C"]),
 "AMP-25": m(csf=["GV.RR"], airmf=["GOVERN-1","GOVERN-4","MAP-5"], ai600=["GAI-HAI","GAI-Bias"], aaism=["AAISM-3D"], cism=["CISM-1A"], asi=["ASI09"]),
 "AMP-26": m(csf=["GV.RR","GV.OV"], airmf=["GOVERN-2","MANAGE-1","MEASURE-2"], ai600=["GAI-HAI"], aaism=["AAISM-3D","AAISM-3E"], cism=["CISM-1A"], llm=["LLM06"], asi=["ASI09","ASI01"], aicm=["AIS-11"]),
 "AMP-27": m(csf=["GV.RR","GV.OV","ID.IM"], airmf=["GOVERN-1"], aaism=["AAISM-1D"], cism=["CISM-3A","CISM-3B"], crisc=["CRISC-1A"], ccm=["GRC"]),
 "AMP-28": m(csf=["PR.PS","PR.AA"], airmf=["MAP-2","MANAGE-1"], aaism=["AAISM-3A"], asi=["ASI07","ASI08","ASI10"], llm=["LLM06"], aicm=["AIS-11"], ccm=["AIS"], cism=P("CISM-3A")),
 "AMP-29": m(csf=["GV.RR","PR.AT"], airmf=["GOVERN-3","GOVERN-2"], aaism=["AAISM-1D"], cism=["CISM-3B"], sp53=["AT","PS"], ccm=["HRS"], cis=["CIS 14"]),
 "AMP-30": m(csf=["GV.OC","PR.AT"], airmf=["GOVERN-1","MANAGE-2"], aaism=["AAISM-1B","AAISM-1D"], cism=["CISM-3B"], ccm=["HRS","GRC"], cis=["CIS 14"]),
 "AMP-31": m(csf=["ID.AM","PR.DS"], sp53=["RA","PT"], airmf=["MAP-1"], aaism=["AAISM-1C","AAISM-3C"], ai600=["GAI-Privacy"], ccm=["DSP"], cis=["CIS 3"], llm=["LLM02"], aicm=["AICM (dominios CCM)"]),
 "AMP-32": m(csf=["PR.DS","PR.AA"], sp53=["AC","PT"], airmf=["MAP-4","MANAGE-1"], aaism=["AAISM-3C"], ai600=["GAI-Privacy","GAI-InfoInt"], llm=["LLM02","LLM08","LLM04"], asi=["ASI06"], ccm=["DSP","IAM"], cis=["CIS 3"]),
 "AMP-33": m(csf=["PR.AA","ID.AM"], sp53=["IA","AC"], airmf=["GOVERN-1"], aaism=["AAISM-1C","AAISM-3E"], cism=["CISM-3A"], crisc=["CRISC-4B"], asi=["ASI03","ASI10"], owasp=["OWASP NHI Top 10"], aicm=["IAM-19"], ccm=["IAM"], cis=["CIS 5","CIS 6"]),
 "AMP-34": m(csf=["PR.AA"], sp53=["IA","AC"], nist=["SP 800-207"], airmf=["MANAGE-1"], aaism=["AAISM-3A","AAISM-3E"], cism=["CISM-3A"], crisc=["CRISC-4B"], llm=["LLM06"], asi=["ASI03"], owasp=["OWASP NHI Top 10"], aicm=["IAM-19","AIS-11"], ccm=["IAM"], cis=["CIS 5","CIS 6"], csa=["Zero Trust Advancement Center"]),
 "AMP-35": m(csf=["PR.PS"], sp53=["SA","SC"], airmf=["MAP-2","MAP-3"], aaism=["AAISM-3A"], cism=["CISM-3A"], crisc=["CRISC-4A"], llm=["LLM06","LLM05"], asi=["ASI07","ASI08","ASI05"], aicm=["AIS-11"], ccm=["AIS"], csa=["MAESTRO (threat modeling agéntico)"], owasp=["SAMM Design"]),
 "AMP-36": m(csf=["PR.AA","PR.PS"], sp53=["AC","CM"], airmf=["MANAGE-1"], aaism=["AAISM-3A","AAISM-3E"], llm=["LLM06","LLM05"], asi=["ASI02","ASI03","ASI05"], aicm=["AIS-11","IAM-19"], ccm=["AIS","IAM"], cis=["CIS 6"]),
 "AMP-37": m(csf=["ID.RA","ID.IM"], rmf=["Assess"], sp53=["CA","RA"], airmf=["MEASURE-1","MEASURE-2"], aaism=["AAISM-2B","AAISM-3B"], cism=["CISM-3B"], crisc=["CRISC-3B"], llm=["LLM01","LLM02","LLM06"], asi=["ASI01","ASI02","ASI06"], atlas=["ATLAS AI Attack Staging","ATLAS Execution"], aicm=["MDS"], ccm=["A&A","TVM"], cis=["CIS 18"], owasp=["SAMM Verification"]),
 "AMP-38": m(csf=["ID.IM","PR.PS"], rmf=["Assess"], sp53=["CA","SI"], airmf=["MEASURE-2","MANAGE-4"], aaism=["AAISM-3E"], crisc=["CRISC-3B","CRISC-3C"], asi=["ASI08"], ccm=["A&A","CCC"]),
 "AMP-39": m(csf=["DE.AE","RS.AN","RS.MI"], sp53=["IR","SI"], nist=["SP 800-61"], airmf=["MAP-3","MANAGE-1"], aaism=["AAISM-3E","AAISM-1E"], cism=["CISM-4B"], crisc=["CRISC-4B"], llm=["LLM06"], asi=["ASI01","ASI02","ASI08"], ccm=["SEF","LOG"], cis=["CIS 17","CIS 13"], d3=["D3FEND Detect","D3FEND Isolate"]),
 "AMP-40": m(csf=["GV.RR","RS.MI"], airmf=["GOVERN-2","MANAGE-1"], ai600=["GAI-HAI"], aaism=["AAISM-3D","AAISM-3E"], cism=["CISM-4B"], llm=["LLM06"], asi=["ASI02","ASI09"], aicm=["AIS-11"], ccm=["SEF"]),
 "AMP-41": m(csf=["ID.RA","PR.PS","DE.AE"], sp53=["SI","RA"], airmf=["MAP-4","MEASURE-2"], ai600=["GAI-InfoSec"], aaism=["AAISM-2B","AAISM-3E"], llm=["LLM01","LLM07","LLM05"], asi=["ASI01","ASI06"], atlas=["ATLAS Initial Access","ATLAS Execution","ATLAS Defense Evasion"], aicm=["MDS","AIS-11"], ccm=["AIS","TVM"], attack=P("TA0001 Initial Access")),
 "AMP-42": m(csf=["ID.RA","PR.DS"], sp53=["SI","SR"], airmf=["MAP-4","MANAGE-3"], ai600=["GAI-InfoInt","GAI-ValueChain"], aaism=["AAISM-2B","AAISM-3B","AAISM-3C"], llm=["LLM04","LLM08","LLM03"], asi=["ASI06","ASI04"], atlas=["ATLAS Resource Development","ATLAS Persistence","ATLAS AI Attack Staging"], aicm=["MDS"], ccm=["DSP","STA"]),
 "AMP-43": m(csf=["RS.MA","ID.IM"], sp53=["IR","CP"], nist=["SP 800-61","SP 800-84"], airmf=["MANAGE-4"], aaism=["AAISM-1E"], cism=["CISM-4A"], crisc=["CRISC-1A"], asi=["ASI08","ASI10"], ccm=["SEF","BCR"], cis=["CIS 17"]),
 "AMP-44": m(csf=["RS.MI","RS.MA"], sp53=["IR"], airmf=["MANAGE-1","MANAGE-4"], aaism=["AAISM-1E","AAISM-3E"], cism=["CISM-4A","CISM-4B"], llm=["LLM06"], asi=["ASI08","ASI10"], aicm=["AIS-11"], ccm=["SEF"], d3=["D3FEND Isolate","D3FEND Evict"]),
 "AMP-45": m(csf=["RS.AN"], sp53=["IR","AU"], nist=["SP 800-61"], airmf=["MEASURE-3"], aaism=["AAISM-1E","AAISM-3E"], cism=["CISM-4B"], asi=["ASI01","ASI02"], ccm=["SEF","LOG"], cis=["CIS 8","CIS 17"]),
 "AMP-46": m(csf=["RS.AN","GV.OV","DE.CM"], sp53=["AU"], airmf=["MEASURE-3","GOVERN-1"], aaism=["AAISM-3E"], cism=["CISM-4B","CISM-3B"], crisc=["CRISC-3C"], asi=["ASI07"], ccm=["LOG","A&A"], cis=["CIS 8"], aicm=["AICM (dominios CCM)"]),
 "AMP-47": m(csf=["RC.RP","PR.IR"], sp53=["CP"], airmf=["MANAGE-2"], aaism=["AAISM-1E"], cism=["CISM-4A"], crisc=["CRISC-1A"], ccm=["BCR"], cis=["CIS 11"], d3=["D3FEND Restore"]),
 "AMP-48": m(csf=["GV.SC","PR.IR","ID.RA"], sp53=["SR","CP"], nist=["SP 800-161"], airmf=["GOVERN-6","MAP-4"], ai600=["GAI-ValueChain"], aaism=["AAISM-2C","AAISM-1E"], crisc=["CRISC-1A","CRISC-2A"], llm=["LLM03"], asi=["ASI04"], ccm=["BCR","STA"], cis=["CIS 15"]),
 "AMP-49": m(csf=["GV.SC","ID.AM"], sp53=["SR","SA"], nist=["SP 800-161"], airmf=["GOVERN-6","MAP-4","MANAGE-3"], ai600=["GAI-ValueChain","GAI-IP"], aaism=["AAISM-2C","AAISM-3B"], cism=["CISM-3B"], crisc=["CRISC-1A"], llm=["LLM03","LLM04"], asi=["ASI04"], atlas=["ATLAS Resource Development"], aicm=["MDS"], ccm=["STA"], cis=["CIS 15","CIS 16"], owasp=["SAMM Implementation"]),
 "AMP-50": m(csf=["GV.SC","PR.AA","PR.PS"], sp53=["SA","AC","SR"], airmf=["GOVERN-6","MANAGE-3"], aaism=["AAISM-2C","AAISM-3A","AAISM-3E"], llm=["LLM03","LLM06"], asi=["ASI04","ASI02","ASI07"], aicm=["AIS-11","IAM-19"], ccm=["STA","AIS","IAM"], cis=["CIS 15","CIS 16"], csa=["MAESTRO (threat modeling agéntico)"]),
 "AMP-51": m(csf=["PR.PS","ID.AM","DE.CM"], sp53=["CM","RA"], airmf=["MAP-1","MEASURE-3"], aaism=["AAISM-3E","AAISM-1C"], crisc=["CRISC-4A"], ccm=["IVS","LOG"], aicm=["MDS","AICM (dominios CCM)"], cis=["CIS 4","CIS 7"], cisx=["CIS Benchmarks"], csa=["STAR / STAR for AI"]),
 "AMP-52": m(csf=["GV.RR","PR.PS"], sp53=["SI"], airmf=["MANAGE-1","MEASURE-2","MAP-5"], ai600=["GAI-Dangerous","GAI-Obscene","GAI-InfoInt","GAI-Confab","GAI-Bias"], aaism=["AAISM-3D","AAISM-3E"], llm=["LLM05","LLM09"], asi=["ASI09"], aicm=["MDS"], ccm=["AIS"]),
}

HC_MAP = {
 "HC-001": m(csf=["GV.OV","GV.RR","ID.RA"], sp53=["PM","AU"], cism=["CISM-1A","CISM-2A"], crisc=["CRISC-1B","CRISC-3C"], airmf=P("MEASURE-1"), ccm=["GRC"]),
 "HC-002": m(csf=["GV.RM","PR.PS"], rmf=["Select","Implement"], sp53=["PL","SA"], cism=["CISM-2B","CISM-3A"], crisc=["CRISC-1B","CRISC-3B","CRISC-4A"], ccm=["GRC","IVS"]),
 "HC-003": m(csf=["GV.RM","ID.RA","GV.OV"], rmf=["Authorize","Assess"], sp53=["CA","RA"], cism=["CISM-2B"], crisc=["CRISC-3A","CRISC-3C"], ccm=["GRC","A&A"]),
 "HC-004": m(csf=["GV.PO","PR.PS","ID.IM"], sp53=["CM","PL","CA"], cism=["CISM-3A","CISM-3B"], crisc=["CRISC-3B"], ccm=["CCC","GRC"], cis=["CIS 4"], cisx=["CIS Benchmarks"], owasp=P("SAMM Implementation")),
 "HC-005": m(csf=["GV.OV","ID.IM","GV.OC"], rmf=["Monitor"], sp53=["CA","AU"], cism=["CISM-1A","CISM-3B"], crisc=["CRISC-3C"], ccm=["A&A","GRC"], cis=["CIS 8"]),
 "HC-006": m(csf=["GV.RM","GV.OV"], cism=["CISM-1B","CISM-3B"], crisc=["CRISC-3C"], sp53=["PM"]),
 "HC-007": m(csf=["GV.RM","RC.RP","PR.IR"], sp53=["CP","RA"], cism=["CISM-2B","CISM-4A"], crisc=["CRISC-1A","CRISC-1B"], ccm=["BCR"], cis=["CIS 11"], d3=["D3FEND Restore"]),
 "HC-008": m(csf=["GV.SC","GV.OC"], sp53=["SR","SA"], nist=["SP 800-161"], cism=["CISM-1A","CISM-3B"], crisc=["CRISC-1A"], ccm=["STA"], cis=["CIS 15"], airmf=P("GOVERN-6")),
 "HC-009": m(csf=["PR.AA","GV.RR"], sp53=["IA","AC"], airmf=["GOVERN-2"], aaism=["AAISM-1C","AAISM-3E"], cism=["CISM-3A"], crisc=["CRISC-1B","CRISC-4B"], asi=["ASI03","ASI10"], owasp=["OWASP NHI Top 10"], aicm=["IAM-19"], ccm=["IAM"], cis=["CIS 5","CIS 6"]),
 "HC-010": m(csf=["GV.RR","PR.AA","PR.PS"], airmf=["GOVERN-2","MANAGE-1"], aaism=["AAISM-1B","AAISM-3E"], cism=["CISM-2B","CISM-4B"], crisc=["CRISC-1B"], llm=["LLM06"], asi=["ASI03","ASI02"], aicm=["AIS-11","IAM-19"]),
 "HC-011": m(csf=["PR.DS","ID.AM","GV.OC"], sp53=["PT","AC","SC"], nist=["NIST PF"], airmf=["MAP-4"], aaism=["AAISM-3C"], ai600=["GAI-Privacy"], llm=["LLM02"], ccm=["DSP"], cis=["CIS 3"]),
 "HC-012": m(csf=["GV.OV","GV.PO"], rmf=["Assess","Authorize"], sp53=["CA"], airmf=["MEASURE-2","GOVERN-1"], aaism=["AAISM-1A","AAISM-3E"], cism=["CISM-1B","CISM-4B"], ccm=["A&A","GRC"], csa=["STAR / STAR for AI"]),
 "HC-013": m(csf=["GV.RM","GV.PO","PR.PS"], sp53=["PM","PL","SA"], cism=["CISM-1B","CISM-3A","CISM-3B"], crisc=["CRISC-1A","CRISC-3A"], ccm=["GRC","CCC"]),
 "HC-014": m(csf=["GV.RM","GV.OC","ID.AM","PR.PS"], rmf=["Prepare","Categorize"], sp53=["PM","RA","PL"], cism=["CISM-1B","CISM-2A"], crisc=["CRISC-1B","CRISC-2A","CRISC-4A"], ccm=["GRC"]),
 "HC-015": m(csf=["PR.AA","PR.PS","GV.PO"], nist=["SP 800-207"], cism=["CISM-3A"], crisc=["CRISC-4B"], ccm=["IAM","IVS"], csa=["Zero Trust Advancement Center"], d3=["D3FEND Harden"]),
 "HC-016": m(csf=["ID.RA","ID.AM"], sp53=["RA","CM"], cism=["CISM-2A"], crisc=["CRISC-2A"], ccm=["TVM"], cis=["CIS 7","CIS 1"], attack=["TA0043 Reconnaissance","TA0001 Initial Access"], d3=["D3FEND Model"]),
 "HC-017": m(csf=["ID.RA","DE.CM","GV.OV","RS.MA"], sp53=["RA","SI","PM"], cism=["CISM-2A","CISM-4B"], crisc=["CRISC-2A","CRISC-3C"], ccm=["TVM","LOG"], cis=["CIS 13"], attack=["TA0043 Reconnaissance","TA0042 Resource Development"], d3=["D3FEND Model","D3FEND Detect"]),
 "HC-018": m(csf=["DE.CM","GV.OV","ID.IM"], rmf=["Monitor"], sp53=["AU","CA","SI"], airmf=P("MEASURE-3"), cism=["CISM-3B"], crisc=["CRISC-3C"], ccm=["LOG","A&A"], cis=["CIS 8"], d3=["D3FEND Detect"]),
 "HC-019": m(csf=["DE.AE","RS.AN","RS.MI","GV.RR"], sp53=["IR","SI"], nist=["SP 800-61"], airmf=["MANAGE-1"], aaism=["AAISM-3E"], cism=["CISM-4B"], crisc=["CRISC-4B"], llm=["LLM06"], asi=["ASI02","ASI09"], ccm=["SEF","LOG"], cis=["CIS 13","CIS 17"], d3=["D3FEND Detect","D3FEND Isolate"]),
 "HC-020": m(csf=["RS.CO","RC.CO","GV.OV","RS.MA"], sp53=["IR"], cism=["CISM-4A","CISM-4B","CISM-1A"], crisc=["CRISC-3C"], ccm=["SEF"], cis=["CIS 17"]),
 "HC-021": m(csf=["RC.RP","RC.CO","GV.OV"], sp53=["CP","IR"], cism=["CISM-4B"], crisc=["CRISC-1A","CRISC-3C"], ccm=["BCR"], cis=["CIS 11"], d3=["D3FEND Restore"]),
 "HC-022": m(csf=["GV.RR","RS.MA","RS.CO","RC.CO","GV.OC"], sp53=["IR","CP","PM"], cism=["CISM-4A","CISM-1A"], crisc=["CRISC-1A","CRISC-1B"], ccm=["SEF","BCR","GRC"], cis=["CIS 17"]),
 "HC-023": m(csf=["GV.SC","GV.RM","PR.IR"], sp53=["SR","CP"], nist=["SP 800-161"], airmf=["GOVERN-6"], aaism=["AAISM-2C"], crisc=["CRISC-1B"], ccm=["STA","BCR","IPY"], cis=["CIS 15"]),
 "HC-024": m(csf=["GV.OC","PR.DS","PR.PS","ID.IM"], sp53=["PT","SA","CA"], nist=["NIST PF"], cism=["CISM-1A","CISM-3A"], crisc=["CRISC-1B","CRISC-3B"], ccm=["DSP","AIS","A&A"], cis=["CIS 3","CIS 16"], owasp=["SAMM Governance","SAMM Verification"]),
 "HC-025": m(csf=["PR.AT","GV.RR","PR.IR"], sp53=["AT","PS","CP"], cism=["CISM-3B","CISM-4A"], crisc=["CRISC-1A"], ccm=["HRS","BCR"], cis=["CIS 14"]),
 "HC-026": m(csf=["GV.RR","GV.OC","ID.RA"], sp53=["PS","PM","AC"], cism=["CISM-1A","CISM-3B"], crisc=["CRISC-1A","CRISC-2A"], ccm=["HRS","GRC"], cis=["CIS 14"], attack=["TA0009 Collection","TA0010 Exfiltration"]),
 "HC-027": m(csf=["GV.OV","ID.IM","GV.RM"], cism=["CISM-3B","CISM-2B"], crisc=["CRISC-3C"], airmf=["MEASURE-1","MEASURE-4"], sp53=["PM"]),
 "HC-028": m(csf=["GV.RM","ID.RA","GV.PO"], rmf=["Authorize"], sp53=["CA","RA"], cism=["CISM-2B","CISM-3A"], crisc=["CRISC-3A","CRISC-3B"], ccm=["GRC"]),
 "HC-029": m(csf=["GV.SC","GV.OC"], sp53=["SR","SA"], nist=["SP 800-161"], cism=["CISM-1A","CISM-3B"], crisc=["CRISC-1A"], ccm=["STA","A&A"], cis=["CIS 15","CIS 16"], airmf=P("GOVERN-6")),
 "HC-030": m(csf=["PR.PS","PR.IR","RC.RP","ID.AM"], sp53=["SC","CP","CM"], cism=["CISM-3A","CISM-4A"], crisc=["CRISC-4A","CRISC-1A"], ccm=["IVS","UEM","BCR"], cis=["CIS 1","CIS 4","CIS 11","CIS 12"]),
 "HC-031": m(csf=["PR.PS","GV.SC","ID.RA"], sp53=["SA","SI","SR"], nist=["SP 800-161"], cism=["CISM-3A"], crisc=["CRISC-4A","CRISC-3B"], ccm=["AIS","STA","CCC"], cis=["CIS 16","CIS 15"], owasp=["SAMM Implementation","SAMM Verification","OWASP ASVS"], llm=P("LLM03")),
 "HC-032": m(csf=["ID.RA","ID.IM"], rmf=["Assess"], sp53=["RA","CA"], airmf=["MAP-4","MEASURE-2"], aaism=["AAISM-2B"], cism=["CISM-2A","CISM-3B"], crisc=["CRISC-2A","CRISC-3B"], llm=["LLM01","LLM06"], asi=["ASI01","ASI02","ASI03"], atlas=["ATLAS Reconnaissance","ATLAS AI Attack Staging"], ccm=["TVM","A&A"], cis=["CIS 18"], csa=["MAESTRO (threat modeling agéntico)"], owasp=["SAMM Verification"]),
 "HC-033": m(csf=["PR.DS","GV.OC","GV.SC"], sp53=["PT","SC","SA"], nist=["NIST PF"], aaism=P("AAISM-3C"), ccm=["DSP","IPY","STA"], cis=["CIS 3"], csa=["STAR / STAR for AI"]),
 "HC-034": m(csf=["GV.RM","ID.IM","PR.PS"], sp53=["CM","PL"], airmf=["MANAGE-2","MANAGE-4"], cism=["CISM-1B","CISM-3A"], crisc=["CRISC-3A","CRISC-3B"], ccm=["CCC"]),
 "HC-035": m(csf=["ID.IM","RS.AN","GV.PO"], sp53=["IR","PL"], nist=["SP 800-61"], cism=["CISM-4B","CISM-3A"], crisc=["CRISC-3C"], ccm=["SEF","GRC"], cis=["CIS 17"]),
 "HC-036": m(csf=["GV.RM","ID.IM","PR.PS"], rmf=["Select","Implement","Assess"], sp53=["PM","CA"], cism=["CISM-3A","CISM-3B"], crisc=["CRISC-3B"], ccm=["GRC"]),
 "HC-037": m(csf=["GV.RR","PR.AT"], sp53=["AT","PS"], cism=["CISM-3B","CISM-1A"], crisc=["CRISC-1A"], ccm=["HRS"], cis=["CIS 14"]),
 "HC-038": m(csf=["GV.OV","PR.AA","PR.PS"], nist=["SP 800-207"], rmf=["Assess"], sp53=["CA"], cism=["CISM-3B"], ccm=["A&A","IAM"], csa=["Zero Trust Advancement Center"]),
 "HC-039": m(csf=["GV.OC","GV.RM","GV.OV","RS.CO"], sp53=["PM","RA"], nist=["SP 800-30"], cism=["CISM-1A","CISM-1B","CISM-2A"], crisc=["CRISC-1A","CRISC-1B","CRISC-3C"], ccm=["GRC"]),
 "HC-040": m(csf=["GV.OC","GV.RM","GV.PO","DE.CM","ID.IM"], sp53=["PM","CM","CA"], cism=["CISM-1A","CISM-2B","CISM-3B"], crisc=["CRISC-1B","CRISC-3C"], ccm=["GRC","CCC","LOG"]),
}

PA_MAP = {
 "G1.1-PA01": m(csf=["GV.RR","GV.OC"], airmf=["GOVERN-2"], aaism=["AAISM-1D"], cism=["CISM-1A","CISM-3B"], crisc=["CRISC-1A"], ccm=["GRC"]),
 "G1.2-PA01": m(csf=["GV.RM","GV.OC"], airmf=["MAP-3"], aaism=["AAISM-1D"], cism=["CISM-1B"], crisc=["CRISC-1A"], llm=["LLM10"], sp53=["PM"]),
 "G2.1-PA01": m(csf=list(S.CSF), nist=["SP 800-207"], cism=["CISM-1B"], crisc=["CRISC-1B"], csa=["Zero Trust Advancement Center"], ccm=["GRC"]),
 "G2.1-PA02": m(csf=["GV.PO","GV.OV"], airmf=list(S.AIRMF), aaism=["AAISM-1A"], cism=["CISM-1B"], crisc=["CRISC-1B"], aicm=["AICM (dominios CCM)"], csa=["NIST AI RMF Agentic Profile (borrador CSA)","STAR / STAR for AI"], ccm=["GRC"]),
 "G2.2-PA01": m(csf=["GV.PO"], sp53=["PL"], airmf=["GOVERN-1"], aaism=["AAISM-1B"], cism=["CISM-3A"], crisc=["CRISC-1A"], asi=["ASI10","ASI03"], aicm=["AIS-11","IAM-19"], ccm=["GRC"]),
 "G2.2-PA02": m(csf=["GV.PO","ID.AM"], sp53=["PL","CM"], airmf=["MAP-2","MAP-3","GOVERN-1"], aaism=["AAISM-1B","AAISM-1C"], cism=["CISM-3A"], asi=["ASI01","ASI03"], aicm=["AIS-11"], ccm=["GRC","CCC"]),
 "G2.2-PA03": m(csf=["GV.PO","PR.PS"], sp53=["CM","CA"], cism=["CISM-3A","CISM-3B"], crisc=["CRISC-3A","CRISC-3B"], ccm=["CCC"], cis=["CIS 4","CIS 9"], cisx=["CIS Benchmarks"]),
 "G3.1-PA01": m(csf=["GV.OC"], sp53=["PT"], nist=["NIST PF"], airmf=["GOVERN-1","MAP-1"], ai600=["GAI-Privacy","GAI-HAI"], aaism=["AAISM-1A","AAISM-3D"], cism=["CISM-1A"], crisc=["CRISC-1B"], ccm=["GRC","DSP"]),
 "G3.2-PA01": m(csf=["PR.PS","ID.IM","GV.OV"], rmf=["Monitor"], sp53=["CM","CA"], cism=["CISM-3B"], crisc=["CRISC-3C"], ccm=["CCC","A&A"], cis=["CIS 4","CIS 9"], cisx=["CIS Benchmarks"]),
 "G4.1-PA01": m(csf=["GV.RR","GV.OV"], airmf=["GOVERN-2"], aaism=["AAISM-1A","AAISM-1D"], cism=["CISM-1A"], crisc=["CRISC-1B"], ccm=["GRC","A&A"]),
 "G4.1-PA02": m(csf=["ID.RA","GV.RM"], sp53=["RA"], nist=["SP 800-30"], airmf=["MAP-4","MAP-5","MANAGE-1"], aaism=["AAISM-2A","AAISM-2B"], cism=["CISM-2A"], crisc=["CRISC-2A","CRISC-2B"], llm=["LLM01","LLM02","LLM06","LLM10"], asi=list(S.ASI10), atlas=["ATLAS Initial Access","ATLAS AI Attack Staging","ATLAS Impact"], ccm=["GRC","TVM"]),
 "G4.2-PA01": m(csf=["GV.RM","DE.CM"], airmf=["MEASURE-1","MEASURE-3","MANAGE-4"], aaism=["AAISM-2A","AAISM-3E"], cism=["CISM-2B"], crisc=["CRISC-3C"], llm=["LLM10","LLM06"], ccm=["GRC","LOG"]),
 "G6.1-PA01": m(csf=["GV.OV","RS.CO"], airmf=["GOVERN-5","MEASURE-1"], aaism=["AAISM-1D"], cism=["CISM-1A","CISM-3B"], crisc=["CRISC-3C"], sp53=["PM"]),
 "G6.2-PA01": m(csf=["GV.OV","ID.IM"], airmf=["MEASURE-1","MEASURE-4","GOVERN-1"], aaism=["AAISM-1D"], cism=["CISM-3B"], crisc=["CRISC-3C"], asi=["ASI10"], ccm=["GRC"]),
 "M1.1-PA01": m(csf=["GV.RR"], sp53=["PM","PS"], airmf=["GOVERN-2","GOVERN-3"], aaism=["AAISM-1D"], cism=["CISM-3A","CISM-3B"], crisc=["CRISC-1A"], ccm=["GRC","HRS"]),
 "M1.1-PA02": m(csf=["GV.RM","ID.IM","PR.PS"], rmf=["Select"], sp53=["PM"], cism=["CISM-3A","CISM-3B"], crisc=["CRISC-3B"], ccm=["GRC"]),
 "M1.1-PA03": m(csf=["GV.OV","ID.IM","PR.PS"], rmf=["Monitor"], sp53=["PM","CA"], cism=["CISM-3B"], crisc=["CRISC-3C"], ccm=["GRC","CCC"]),
 "M1.2-PA01": m(csf=["GV.RM","GV.OV"], airmf=["MAP-3","MANAGE-4"], aaism=["AAISM-1D"], cism=["CISM-3B"], crisc=["CRISC-1A"], llm=["LLM10"], sp53=["PM"]),
 "M1.2-PA02": m(csf=["GV.SC"], sp53=["SA","SR"], nist=["SP 800-161"], airmf=["GOVERN-6","MANAGE-3"], aaism=["AAISM-2C"], cism=["CISM-3B"], crisc=["CRISC-1A"], asi=["ASI04","ASI10"], ccm=["STA"], cis=["CIS 15"]),
 "M1.2-PA03": m(csf=["PR.AT","GV.RR"], sp53=["AT","PS"], airmf=["GOVERN-3"], aaism=["AAISM-1D"], cism=["CISM-3B"], ccm=["HRS"], cis=["CIS 14"]),
 "M2.1-PA01": m(csf=["ID.AM"], rmf=["Categorize"], sp53=["CM"], airmf=["MAP-1","MAP-2"], aaism=["AAISM-1C"], cism=["CISM-3A"], crisc=["CRISC-1A"], asi=["ASI10"], aicm=["AICM (dominios CCM)"], ccm=["DCS","GRC"], cis=["CIS 1","CIS 2"]),
 "M2.2-PA01": m(csf=["PR.AA"], sp53=["AC","IA"], nist=["SP 800-207"], airmf=["MANAGE-1"], aaism=["AAISM-3A","AAISM-3E"], cism=["CISM-3A"], crisc=["CRISC-4B"], llm=["LLM06"], asi=["ASI03","ASI02"], owasp=["OWASP NHI Top 10"], aicm=["IAM-19","AIS-11"], ccm=["IAM"], cis=["CIS 5","CIS 6"]),
 "M3.1-PA01": m(csf=["PR.PS","PR.IR"], rmf=["Select","Implement"], sp53=["SA","SC","PL"], nist=["SP 800-207"], airmf=["MAP-2","MAP-3"], aaism=["AAISM-3A"], cism=["CISM-1B","CISM-3A"], crisc=["CRISC-4A"], asi=["ASI07","ASI08"], aicm=["AIS-11"], ccm=["AIS","IVS"], csa=["MAESTRO (threat modeling agéntico)","Zero Trust Advancement Center"], owasp=["SAMM Design"]),
 "M3.1-PA02": m(csf=["PR.PS","DE.CM"], sp53=["SC","SI"], cism=["CISM-3A"], crisc=["CRISC-4A"], ccm=["TVM","AIS"], cis=["CIS 9","CIS 10"], attack=["TA0001 Initial Access","TA0002 Execution","TA0006 Credential Access"], d3=["D3FEND Harden","D3FEND Detect"]),
 "M3.2-PA01": m(csf=["PR.PS","ID.IM","GV.OV"], rmf=["Implement","Assess"], sp53=["CA","CM"], cism=["CISM-3A","CISM-3B"], crisc=["CRISC-3B","CRISC-3C"], ccm=["A&A","CCC"], cis=["CIS 4","CIS 9"]),
 "M3.2-PA02": m(csf=["GV.PO","PR.PS","PR.AA"], rmf=["Select"], sp53=["PL","CA"], airmf=["GOVERN-1","MANAGE-1"], aaism=["AAISM-1B","AAISM-3E"], cism=["CISM-3A"], crisc=["CRISC-3B"], llm=["LLM01","LLM02","LLM06","LLM10"], asi=["ASI01","ASI02","ASI03","ASI04","ASI06","ASI08","ASI10"], aicm=["AIS-11","IAM-19","MDS"], ccm=["GRC","IAM","AIS","LOG"]),
 "M3.2-PA03": m(csf=["ID.IM","ID.RA"], rmf=["Assess"], sp53=["CA","SI"], airmf=["MEASURE-1","MEASURE-2","MEASURE-4"], ai600=["GAI-Confab"], aaism=["AAISM-3B","AAISM-3E"], cism=["CISM-3B"], crisc=["CRISC-3B"], aicm=["MDS"], ccm=["A&A"], owasp=["SAMM Verification"]),
 "M4.1-PA01": m(csf=["DE.CM","DE.AE","RS.MA","PR.PS","ID.IM"], rmf=["Monitor"], sp53=["IR","SI","AU","CM"], nist=["SP 800-61"], cism=["CISM-4B","CISM-3B"], crisc=["CRISC-3C","CRISC-4B"], ccm=["SEF","LOG","CCC"], cis=["CIS 9","CIS 13","CIS 17"]),
 "M4.1-PA02": m(csf=["DE.AE","RS.MA","RS.AN"], sp53=["IR"], nist=["SP 800-61"], cism=["CISM-4B"], crisc=["CRISC-4B"], ccm=["SEF"], cis=["CIS 17"], d3=["D3FEND Detect"]),
 "M4.1-PA03": m(csf=["DE.AE","ID.IM","PR.PS"], sp53=["SI","CM"], cism=["CISM-4B","CISM-3B"], crisc=["CRISC-3C"], ccm=["TVM","CCC"], cis=["CIS 9"]),
 "M4.1-PA04": m(csf=["DE.CM","DE.AE","ID.RA"], sp53=["SI","AU"], cism=["CISM-4B"], crisc=["CRISC-4B"], ccm=["LOG","TVM"], cis=["CIS 8","CIS 13"], attack=["TA0001 Initial Access","TA0002 Execution","TA0006 Credential Access","TA0011 Command and Control"], d3=["D3FEND Detect","D3FEND Model"]),
 "M4.1-PA05": m(csf=["DE.CM","DE.AE"], sp53=["AU","SI"], airmf=["MEASURE-3"], aaism=["AAISM-3E"], cism=["CISM-4B"], crisc=["CRISC-3C"], asi=["ASI10","ASI07"], aicm=["AICM (dominios CCM)"], ccm=["LOG"], cis=["CIS 8","CIS 13"], d3=["D3FEND Detect"]),
 "M4.1-PA06": m(csf=["GV.OV","ID.IM"], airmf=["MEASURE-2","MEASURE-3","MEASURE-4","MANAGE-4"], ai600=["GAI-Confab"], aaism=["AAISM-3E","AAISM-1D"], cism=["CISM-3B"], crisc=["CRISC-3C"], asi=["ASI08"], ccm=["A&A"]),
 "M4.2-PA01": m(csf=["ID.RA","DE.AE","PR.AT"], sp53=["RA","SI","AT"], cism=["CISM-2A"], crisc=["CRISC-2A"], ccm=["TVM"], cis=["CIS 9","CIS 14"], attack=["TA0043 Reconnaissance","TA0042 Resource Development","TA0001 Initial Access","TA0002 Execution","TA0006 Credential Access","TA0009 Collection"], d3=["D3FEND Model","D3FEND Detect"]),
 "M4.2-PA02": m(csf=["ID.RA"], sp53=["RA","SI"], airmf=["MAP-4","MANAGE-1"], ai600=["GAI-InfoSec"], aaism=["AAISM-2B"], cism=["CISM-2A"], crisc=["CRISC-2A"], llm=list(S.LLM10), asi=list(S.ASI10), atlas=list(S.ATLAS), aicm=["AIS-11","MDS"], ccm=["TVM"], csa=["MAESTRO (threat modeling agéntico)"], d3=["D3FEND Model"]),
 "M5.1-PA01": m(csf=["RS.MA","RS.MI"], sp53=["IR"], nist=["SP 800-61"], airmf=["MANAGE-1"], aaism=["AAISM-1E"], cism=["CISM-4A"], crisc=["CRISC-1A"], llm=["LLM06"], asi=["ASI02"], ccm=["SEF"], cis=["CIS 17"]),
 "M5.2-PA01": m(csf=["RS.MI","RS.AN"], sp53=["IR"], nist=["SP 800-61"], airmf=["MANAGE-1"], aaism=["AAISM-1E"], cism=["CISM-4B"], crisc=["CRISC-3A"], llm=["LLM06"], asi=["ASI02","ASI08"], ccm=["SEF"], cis=["CIS 17"], d3=["D3FEND Isolate","D3FEND Evict"]),
 "M5.2-PA02": m(csf=["ID.IM","RS.AN"], sp53=["IR","CM"], airmf=["MANAGE-4","MEASURE-4"], aaism=["AAISM-1E","AAISM-3B"], cism=["CISM-4B"], crisc=["CRISC-3C"], asi=["ASI06"], ccm=["SEF","CCC"], cis=["CIS 17"]),
 "M6.1-PA01": m(csf=["RC.RP","PR.IR","GV.SC"], sp53=["CP","SR"], airmf=["MANAGE-2"], aaism=["AAISM-1E","AAISM-2C"], cism=["CISM-4A"], crisc=["CRISC-1A"], asi=["ASI08"], ccm=["BCR","STA"], cis=["CIS 11"], d3=["D3FEND Restore"]),
 "M6.2-PA01": m(csf=["GV.SC","PR.PS"], sp53=["SA","SR"], airmf=["GOVERN-6","MAP-4","MANAGE-3"], ai600=["GAI-ValueChain"], aaism=["AAISM-2C","AAISM-3A"], cism=["CISM-3A"], crisc=["CRISC-4A"], llm=["LLM03"], asi=["ASI04"], aicm=["AICM (dominios CCM)"], ccm=["STA","IPY"], csa=["STAR / STAR for AI"]),
 "M6.2-PA02": m(csf=["PR.PS","ID.IM"], sp53=["CM","SA"], airmf=["MANAGE-4"], aaism=["AAISM-3B"], cism=["CISM-3A"], crisc=["CRISC-3B"], asi=["ASI04","ASI06"], ccm=["CCC","AIS"], cis=["CIS 16"], owasp=["SAMM Implementation","SAMM Operations"]),
 "M6.2-PA03": m(csf=["GV.SC","PR.PS"], sp53=["SA"], airmf=["GOVERN-6"], aaism=["AAISM-3A"], cism=["CISM-1B"], crisc=["CRISC-4A"], ccm=["IPY","STA"], asi=["ASI07"]),
}

def merge(*maps):
    out = collections.defaultdict(dict); rank = {"Fuerte":3,"Parcial":2,"Informativo":1}
    for mp in maps:
        for fw, lst in mp.items():
            for e, v, n in lst:
                prev = out[fw].get(e)
                if prev is None or rank[n] > rank[prev[1]]: out[fw][e] = (v, n)
    return {fw: [(e, v, n) for e, (v, n) in d.items()] for fw, d in out.items()}
def units_of(c): return [u.strip() for u in str(c["unidad"]).replace("·", ",").split(",") if u.strip() in UNIT_BASE]
def map_concept(c):
    t = c["tipo"]; bases = [UNIT_BASE[u] for u in units_of(c)]
    if t == "K":
        adds = [mp for pat, mp in K_RULES if re.search(pat, c["concepto"], flags=re.I)]
        if not adds: adds = [mp for pat, mp in K_FALLBACK if re.search(pat, c["id"])]
        return merge(*bases, *adds), "herencia de unidad + regla por palabra clave" + (" (nuevo V7)" if c["origen_version"].startswith("V7") else "")
    if t == "AMP": return merge(*bases, AMP_MAP[c["id"]]), "herencia de unidad + explícito AMP" + (" (nuevo V7)" if c["id"]=="AMP-52" else "")
    if t == "HC": return merge(*bases, HC_MAP[c["id"]]), "herencia de unidades (multi) + explícito HC"
    if t == "PA": return merge(*bases, PA_MAP[c["id"]]), "herencia de unidad + explícito PA" + (" (promovido V7)" if c["id"] in V.PROMOVIDOS else "")
def cell(lst):
    mark = {"Fuerte":"●","Parcial":"◐","Informativo":"○"}; rk = {"Fuerte":3,"Parcial":2,"Informativo":1}
    return "; ".join(f"{mark[n]}{e} ({v})" for e, v, n in sorted(lst, key=lambda x: (-rk[x[2]], x[0]))) if lst else ""
def build_matrix(cat=None):
    rows = []
    for c in (cat or V.catalogo_v7()):
        mp, metodo = map_concept(c); row = dict(c); row["metodo"] = metodo
        row["n_fuertes"] = sum(1 for fw in mp for e, v, n in mp[fw] if n == "Fuerte")
        for fw in F: row[fw] = cell(mp.get(fw, [])); row["_raw_"+fw] = mp.get(fw, [])
        rows.append(row)
    return rows
def coverage(rows):
    cov = {}; alias = {"OWASP SAMM":"OWASP otros"}
    for fw, els in S.FRAMEWORK_ELEMENTS.items():
        col = alias.get(fw, fw)
        for e in els:
            h = {"Fuerte":[],"Parcial":[],"Informativo":[]}
            for r in rows:
                for ee, v, n in r.get("_raw_"+col, []):
                    if ee == e: h[n].append(r["id"])
            cov[(fw, e)] = h
    return cov

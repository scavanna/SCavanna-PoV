from __future__ import annotations

import csv
import hashlib
import json
import re
from collections import Counter
from pathlib import Path

import yaml
from openpyxl import Workbook, load_workbook
from openpyxl.formatting.rule import ColorScaleRule
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.table import Table, TableStyleInfo

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "09-estado-del-arte"
TODAY = "2026-11-18"

PHASES = ["Identificación e inventario", "Prevención y protección", "Detección", "Respuesta y recuperación"]
PHASE_CODES = ["I", "P", "D", "R"]

SOURCES = [
    {"source_id": "MS-001", "product": "Microsoft Defender XDR", "area": "XDR unificado: prevención, detección, investigación y respuesta", "url": "https://learn.microsoft.com/en-us/defender-xdr/microsoft-365-defender", "scope_note": "Correlaciona señales de productos licenciados y aprovisionados; no es cobertura universal."},
    {"source_id": "MS-002", "product": "Microsoft Sentinel", "area": "SIEM/SOAR: ingesta, analítica, hunting, incidentes, automatización", "url": "https://learn.microsoft.com/en-us/azure/sentinel/overview", "scope_note": "La cobertura depende de conectores, fuentes de datos, retención y reglas implementadas."},
    {"source_id": "MS-003", "product": "Microsoft Entra ID Protection", "area": "Riesgo de identidad, detección, investigación y remediación", "url": "https://learn.microsoft.com/en-us/entra/id-protection/overview-identity-protection", "scope_note": "Varias capacidades requieren Entra ID P2/Suite y señales de productos asociados."},
    {"source_id": "MS-004", "product": "Microsoft Defender for Identity", "area": "Postura, detección e investigación de identidades híbridas", "url": "https://learn.microsoft.com/en-us/defender-for-identity/what-is", "scope_note": "Requiere sensores/API y cobertura de los sistemas de identidad pertinentes."},
    {"source_id": "MS-005", "product": "Microsoft Defender for Cloud", "area": "CNAPP/CSPM/DevSecOps/CWPP para nube híbrida y multicloud", "url": "https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-cloud-introduction", "scope_note": "Funciones varían entre CSPM fundacional, Defender CSPM y planes CWPP."},
    {"source_id": "MS-006", "product": "Microsoft Defender for IoT", "area": "Inventario, vulnerabilidades y detección IoT/OT sin agente", "url": "https://learn.microsoft.com/en-us/defender-for-iot/", "scope_note": "La respuesta debe coordinarse con operaciones y safety; integra Sentinel/XDR/partners."},
    {"source_id": "MS-007", "product": "Microsoft Defender for Endpoint", "area": "Protección, EDR, inventario, vulnerabilidades y respuesta de endpoints", "url": "https://learn.microsoft.com/en-us/defender-endpoint/microsoft-defender-endpoint", "scope_note": "Disponibilidad y funciones dependen de plataforma y licencia."},
    {"source_id": "MS-008", "product": "Microsoft Intune", "area": "Gestión, cumplimiento y configuración de endpoints", "url": "https://learn.microsoft.com/en-us/mem/intune/fundamentals/what-is-intune", "scope_note": "Controla dispositivos y políticas según plataforma, método de inscripción y licencias."},
    {"source_id": "MS-009", "product": "Microsoft Purview Data Loss Prevention", "area": "Prevención de pérdida de datos", "url": "https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp", "scope_note": "Cobertura depende de ubicación, licencia, clasificación y política."},
    {"source_id": "MS-010", "product": "Microsoft Purview Information Protection", "area": "Descubrimiento, clasificación, etiquetado y cifrado", "url": "https://learn.microsoft.com/en-us/purview/information-protection", "scope_note": "Necesita taxonomía, fuentes soportadas, etiquetas y gobierno de datos."},
    {"source_id": "MS-011", "product": "Microsoft Purview Insider Risk Management", "area": "Detección e investigación de riesgo interno", "url": "https://learn.microsoft.com/en-us/purview/insider-risk-management-solution-overview", "scope_note": "Requiere licencias, privacidad, alcance y aprobación de políticas; no sustituye RR. HH./Legal."},
    {"source_id": "MS-012", "product": "Microsoft Defender for Cloud Apps", "area": "CASB/SaaS: descubrimiento, sesión, app governance y amenazas", "url": "https://learn.microsoft.com/en-us/defender-cloud-apps/what-is-defender-for-cloud-apps", "scope_note": "La cobertura varía por SaaS y modo de integración; App Governance puede requerir licencias."},
    {"source_id": "MS-013", "product": "Microsoft Entra Conditional Access", "area": "Decisiones de acceso basadas en usuario, dispositivo, riesgo y sesión", "url": "https://learn.microsoft.com/en-us/entra/identity/conditional-access/overview", "scope_note": "No sustituye MFA resistente a phishing ni gobernanza; requiere señales y aplicaciones integrables."},
    {"source_id": "MS-014", "product": "Microsoft Entra Privileged Identity Management", "area": "Acceso privilegiado just-in-time, aprobación y revisión", "url": "https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-configure", "scope_note": "Necesita diseño de roles, aprobadores, ventanas y licencias aplicables."},
    {"source_id": "MS-015", "product": "Azure Backup", "area": "Copia, inmutabilidad, soft delete y restauración", "url": "https://learn.microsoft.com/en-us/azure/backup/backup-overview", "scope_note": "Soporte por workload/región; la eficacia exige pruebas de restauración y diseño RPO/RTO."},
    {"source_id": "MS-016", "product": "Azure Site Recovery", "area": "Replicación, failover, failback y pruebas de recuperación", "url": "https://learn.microsoft.com/en-us/azure/site-recovery/site-recovery-overview", "scope_note": "Cobertura depende de sistemas soportados, topología, dependencias y capacidad regional."},
    {"source_id": "MS-017", "product": "Azure Monitor y Log Analytics", "area": "Telemetría, consultas, alertas y diagnóstico", "url": "https://learn.microsoft.com/en-us/azure/azure-monitor/overview", "scope_note": "Detecta únicamente lo instrumentado; requiere diseño de logs, retención y calidad."},
    {"source_id": "MS-018", "product": "Azure DDoS Protection", "area": "Mitigación de DDoS en redes de Azure", "url": "https://learn.microsoft.com/en-us/azure/ddos-protection/ddos-protection-overview", "scope_note": "Cobertura según topología y planes; coordinar con WAF/CDN y socios para capa aplicación."},
    {"source_id": "MS-019", "product": "Azure Web Application Firewall", "area": "Filtrado de tráfico web y mitigación OWASP", "url": "https://learn.microsoft.com/en-us/azure/web-application-firewall/overview", "scope_note": "No sustituye autorización segura ni prueba de aplicaciones; requiere tuning."},
    {"source_id": "MS-020", "product": "Microsoft Defender for APIs", "area": "Inventario, postura, amenazas y respuesta para APIs soportadas", "url": "https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-apis-introduction", "scope_note": "Cobertura principal para APIs gestionadas en Azure API Management; revisar limitaciones por región/tipo."},
    {"source_id": "MS-021", "product": "GitHub Advanced Security y Azure DevOps", "area": "Code scanning, secret scanning y dependencia durante desarrollo", "url": "https://learn.microsoft.com/en-us/azure/devops/repos/security/github-advanced-security-security-overview", "scope_note": "Requiere repositorios compatibles, licenciamiento y configuración; no elimina revisión humana."},
    {"source_id": "MS-022", "product": "Azure Key Vault y Managed HSM", "area": "Protección de secretos, claves y certificados", "url": "https://learn.microsoft.com/en-us/azure/key-vault/general/overview", "scope_note": "Controla custodia; la rotación, permisos, red y recuperación también deben diseñarse."},
    {"source_id": "MS-023", "product": "Azure Policy y Guest Configuration", "area": "Inventario, cumplimiento, prevención y remediación de configuración", "url": "https://learn.microsoft.com/en-us/azure/governance/policy/overview", "scope_note": "Cobertura según proveedores y modos de efecto; no toda política impide cambios."},
    {"source_id": "MS-024", "product": "Microsoft Security Copilot", "area": "Asistencia IA para investigación, hunting, resumen y respuesta", "url": "https://learn.microsoft.com/en-us/copilot/security/microsoft-security-copilot", "scope_note": "Asistencia a analistas; validar resultados, permisos, prompts y automatizaciones."},
    {"source_id": "MS-025", "product": "Azure AI Content Safety", "area": "Prompt Shields, task adherence y guardrails de IA", "url": "https://learn.microsoft.com/en-us/azure/ai-services/content-safety/overview", "scope_note": "Cubierta específica de contenido/LLM; no sustituye IAM, DLP, validación de herramientas ni red team."},
    {"source_id": "MS-026", "product": "Microsoft Defender for Office 365", "area": "Protección de correo y colaboración, links y adjuntos", "url": "https://learn.microsoft.com/en-us/defender-office-365/mdo-about", "scope_note": "Cobertura y automatización dependen del plan y de políticas configuradas."},
    {"source_id": "MS-027", "product": "Microsoft Purview Audit y Compliance Manager", "area": "Auditoría, evidencia, evaluaciones y cumplimiento", "url": "https://learn.microsoft.com/en-us/purview/audit-solutions-overview", "scope_note": "Registra y organiza evidencia soportada; no certifica cumplimiento ni sustituye asesoría legal."},
    {"source_id": "MS-028", "product": "Microsoft Defender Vulnerability Management", "area": "Inventario, evaluación y priorización de vulnerabilidades/configuración", "url": "https://learn.microsoft.com/en-us/defender-vulnerability-management/defender-vulnerability-management", "scope_note": "Alcance depende del endpoint, fuente de inventario y licencia; usar datos de exposición."},
    {"source_id": "MS-029", "product": "Azure Front Door y Traffic Manager", "area": "Distribución global, failover y mitigación perimetral", "url": "https://learn.microsoft.com/en-us/azure/architecture/best-practices/transient-faults", "scope_note": "No sustituye arquitectura activa-activa o recuperación de datos; requiere origen saludable."},
    {"source_id": "MS-030", "product": "Microsoft Security Exposure Management", "area": "Inventario de postura, rutas de ataque y exposición", "url": "https://learn.microsoft.com/en-us/security-exposure-management/", "scope_note": "La visibilidad depende de fuentes conectadas, licencias y telemetría disponible."},
    {"source_id": "MS-031", "product": "Microsoft Priva", "area": "Gestión de riesgos y solicitudes de privacidad", "url": "https://learn.microsoft.com/en-us/privacy/priva/priva-overview", "scope_note": "Privacidad requiere finalidad, base legal, inventario de datos, DPO/Legal y capacidades licenciadas."},
    {"source_id": "MS-032", "product": "Azure Service Health", "area": "Eventos de servicio, salud planificada y avisos de Azure", "url": "https://learn.microsoft.com/en-us/azure/service-health/overview", "scope_note": "Es visibilidad y notificación de plataforma; no sustituye monitorización de aplicación o proveedor."},
    {"source_id": "MS-033", "product": "Azure Resource Graph", "area": "Inventario y consulta de recursos Azure a escala", "url": "https://learn.microsoft.com/en-us/azure/governance/resource-graph/overview", "scope_note": "Inventaría recursos accesibles; la clasificación, criticidad y cobertura multicloud/on-prem deben añadirse."},
    {"source_id": "MS-034", "product": "Azure Traffic Manager", "area": "Enrutamiento DNS y failover", "url": "https://learn.microsoft.com/en-us/azure/traffic-manager/traffic-manager-overview", "scope_note": "Necesita orígenes saludables, DNS TTL y una arquitectura de recuperación coherente."},
    {"source_id": "MS-035", "product": "Azure Front Door", "area": "Entrada global, WAF, aceleración y enrutamiento", "url": "https://learn.microsoft.com/en-us/azure/frontdoor/front-door-overview", "scope_note": "La protección depende de origen, políticas WAF, DNS, health probes y plan seleccionado."},
    {"source_id": "MS-036", "product": "Availability Zones", "area": "Resiliencia zonal de Azure", "url": "https://learn.microsoft.com/en-us/azure/reliability/availability-zones-overview", "scope_note": "La zonalidad depende del servicio/región y del diseño activo-activo/replicación de la aplicación."},
    {"source_id": "MS-037", "product": "Azure Firewall", "area": "Firewall gestionado y filtrado de red", "url": "https://learn.microsoft.com/en-us/azure/firewall/overview", "scope_note": "Requiere arquitectura de red, reglas, routing, logging y operación; no sustituye autorización de aplicación."},
    {"source_id": "MS-038", "product": "Azure Private Link", "area": "Acceso privado a servicios PaaS", "url": "https://learn.microsoft.com/en-us/azure/private-link/private-link-overview", "scope_note": "Reduce exposición pública cuando está soportado; requiere DNS, routing y diseño de endpoints privados."},
    {"source_id": "MS-039", "product": "Azure Network Watcher", "area": "Monitorización, diagnóstico y captura de red Azure", "url": "https://learn.microsoft.com/en-us/azure/network-watcher/network-watcher-overview", "scope_note": "Requiere habilitación regional, permisos, retención y alcance; no captura automáticamente toda red/on-prem."},
    {"source_id": "MS-040", "product": "Microsoft Defender for DevOps", "area": "Visibilidad y postura de seguridad de pipelines y repositorios", "url": "https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-devops-introduction", "scope_note": "Requiere conectar repositorios/pipelines y no sustituye controles propios de repositorio ni revisión de código."},
    {"source_id": "MS-041", "product": "Microsoft Purview Data Map", "area": "Inventario, lineage y clasificación de patrimonio de datos", "url": "https://learn.microsoft.com/en-us/purview/data-map", "scope_note": "Requiere conectores, permisos, scans, taxonomía y cobertura de fuentes compatibles."},
    {"source_id": "MS-042", "product": "Microsoft Entra", "area": "Directorio, identidades, acceso y gobierno", "url": "https://learn.microsoft.com/en-us/entra/fundamentals/whatis", "scope_note": "Funciones exactas dependen de producto, SKU, identidades, aplicaciones y configuración."},
    {"source_id": "MS-043", "product": "Microsoft Purview Records Management", "area": "Retención, eliminación y gestión de registros", "url": "https://learn.microsoft.com/en-us/purview/records-management", "scope_note": "Requiere clasificación, políticas, disposición, owners y requisitos regulatorios validados."},
]


def category_profiles() -> dict[str, dict]:
    return {
        "THR-001": {"assets": "endpoints, servidores, estaciones de usuario, VDI, cloud workloads, correo/colaboración, storage, OT/IoT que ejecuta o distribuye software", "inventory": "inventario normalizado de dispositivos/software; versión, propietario, criticidad, cobertura EDR, superficie expuesta, backups y dependencias", "prevent": "hardening; ASR y allowlisting; MFA; patching; menor privilegio; segmentación; filtros de correo; controles de ejecución; backups aislados/inmutables", "detect": "EDR/XDR y protección de correo; sandbox; comportamiento de cifrado; cambios masivos; comandos sospechosos; telemetría OT pasiva; correlación SIEM", "respond": "aislar dispositivo/zona; revocar identidad y sesiones; preservar evidencia; bloquear indicadores; erradicar persistencia; restaurar desde copia probada; validar integridad y comunicar extorsión"},
        "THR-002": {"assets": "cuentas humanas y no humanas, administradores, sesiones, tokens, directorios, aplicaciones, correo, métodos MFA y federación", "inventory": "identidades, roles, privilegios, cuentas huérfanas, métodos de autenticación, aplicaciones consentidas, accesos de terceros y relaciones de confianza", "prevent": "MFA resistente al phishing; acceso condicional; PIM/JIT; managed identity; protección de tokens; formación y flujos fuera de banda; mínimo privilegio", "detect": "riesgo de identidad; ITDR; anomalías de inicio de sesión/sesión; cambios de roles; credenciales filtradas; imposibilidad de viaje; UEBA; correlación endpoint-email", "respond": "confirmar compromiso; revocar sesiones/tokens; resetear credenciales; deshabilitar cuenta/aplicación; retirar privilegios; investigar movimiento; reconstruir identidad y revisar persistencia"},
        "THR-003": {"assets": "aplicaciones web, APIs, código, dependencias, contenedores, pipelines, gateways, bases de datos, identidades de servicio", "inventory": "APIs, endpoints, versiones, propietarios, exposición, authN/authZ, dependencias/SBOM, secretos, datos de entrada/salida, criticidad y ruta de ataque", "prevent": "SDLC seguro; revisión; SAST/DAST/IAST/SCA; gateway; autenticación/autorización; validación de esquemas; WAF; secretos gestionados; segmented network", "detect": "DAST; WAF/RASP; anomalías API; logs de autorización; detección runtime de workload; escaneo continuo; telemetría de errores y volumen", "respond": "contener endpoint/aplicación; bloquear exploit; rotar secretos; retirar versión; corregir; restaurar datos; investigar abuso; divulgar con Legal si procede"},
        "THR-004": {"assets": "edge, DNS, CDN, WAF, aplicaciones, redes, enlaces, APIs, colas, bases de datos, capacidad cloud/on-prem", "inventory": "superficie pública, dependencias, capacidad pico, rutas, cuotas, RTO, health checks, proveedor de conectividad y modos degradados", "prevent": "DDoS protection; scrubbing; WAF/rate limiting; autoscaling; caching; redundancia; colas; circuit breakers; capacidad reservada y pruebas", "detect": "telemetría de tráfico/saturación; SLO; anomalía volumétrica/aplicativa; DNS; health checks; alertas de capacidad y error rate", "respond": "activar mitigación/scrubbing; rate limit; bloquear orígenes; escalar; desviar tráfico; cambiar a modo degradado; failover; comunicar; ajustar capacidad y postmortem"},
        "THR-005": {"assets": "datos sensibles, propiedad intelectual, repositorios, administración, transacciones, endpoints, medios, cuentas privilegiadas y procesos críticos", "inventory": "clasificación de datos, permisos, compartidos, cuentas/roles, procesos críticos, joiner-mover-leaver, transferencias de conocimiento y dispositivos", "prevent": "mínimo privilegio; PAM/JIT; separación de funciones; DLP; controles de salida de datos; procesos HR/offboarding; doble autorización; masking", "detect": "UEBA; insider risk; DLP; monitorización de accesos/descargas; uso anómalo de privilegios; correos/repositorios y cambios de patrón", "respond": "preservar evidencia con privacidad; restringir acceso; coordinar Legal/HR/DPO; contener copia/fuga; recuperar datos; investigar trazabilidad; revisar privilegios y cultura"},
        "THR-006": {"assets": "proveedores, SaaS, BPO, software, paquetes, contenedores, updates, credenciales, pipelines, contratos y cuartos niveles", "inventory": "registro de terceros, acceso, datos, ubicación, subprocesadores, SBOM, dependencias, integridad, SLA, contratos, concentración y salida", "prevent": "due diligence; cláusulas de notificación/auditoría; mínimo acceso y segmentación; SBOM/provenance/signing; SLSA; pinning; JIT de proveedor; sandbox", "detect": "alertas de proveedor; integridad de artefactos; drift; consumo anómalo; acceso tercero; actividad CI/CD; escaneo de dependencias y reputación", "respond": "revocar acceso/actualización; aislar artefacto; bloquear paquete/versión; activar proveedor alternativo; reconstruir; evaluar datos; notificación contractual/regulatoria"},
        "THR-007": {"assets": "sistemas, cloud, firmware, aplicaciones, contenedores, identidades, configuraciones, redes, certificados, APIs y secretos", "inventory": "inventario continuo, SBOM, exposición, CVE/CWE, configuración, baseline, propietario, edad, compensación, excepciones y alcance de internet", "prevent": "secure baseline; hardening; patching priorizado por exposición; IaC/policy; secret management; JIT; configuración segura; testing y change control", "detect": "vulnerability scanning; CSPM/CNAPP; EASM; FIM; configuration drift; secret scanning; pentest/BAS; validación contra baseline", "respond": "priorizar por riesgo; aislar o retirar; mitigar virtualmente; desplegar fix; rotar secreto/certificado; validar; cerrar excepción y comprobar no reincidencia"},
        "THR-008": {"assets": "centros de datos, sedes, salas, plantas, redes eléctricas, comunicaciones, terminales, medios, personal e instalaciones dependientes", "inventory": "mapa de sitios, utilidades, zonas, equipos críticos, sensores, capacidad, repuestos, rutas, acuerdos, proveedores y escenarios físicos/ambientales", "prevent": "redundancia geográfica; dual feed; UPS/generación; fire/smoke/water controls; HVAC; seguridad física; DR; stock; zoning; construcción resiliente", "detect": "BMS; sensores ambientales, humo, agua, temperatura, energía; CCTV/access control; health of utilities; alarmas; inspección", "respond": "proteger personas; evacuación/lockdown; activar EOC/BCP; failover; comunicación; restaurar utilidades/site; inspección; reconstrucción y lecciones"},
        "THR-009": {"assets": "sistemas, workflows, cambios, datos, configuraciones, backups, integraciones, personas, proveedores y automatizaciones", "inventory": "CMDB, cambios, dependencias, SLO, owner, runbook, versionado, cadencia, fallos, deuda técnica, capacidad y pruebas", "prevent": "IaC; CI/CD; revisión y separación; testing; canary/rollback; validación; SOP; automatización; resiliencia; formación y límites humanos", "detect": "observabilidad; synthetic monitoring; integridad; drift; alertas de error; SRE/SLI; change correlation; reconciliación; audit logs", "respond": "stabilize; rollback; failover; restaurar/recuperar; corregir datos; reconstruir; gestión de problema; postmortem sin culpa y mejora del control"},
        "THR-010": {"assets": "datos, logs, DNS, redes, mensajería, firma/código, configuraciones, parámetros, sistemas de decisión y cadenas de custodia", "inventory": "fuentes de verdad, integridad requerida, firmas/llaves, flujo de datos, logging, replicas, reconciliación, tiempo y propietarios", "prevent": "TLS/mTLS, DNSSEC donde aplique, firmado, hashing, inmutabilidad, append-only, RBAC, separación, validación de secuencia y tripwire", "detect": "FIM; integridad; detección de logs alterados; anomalía de tráfico; reconciliación; attestation; validación de firma/hash/tiempo", "respond": "aislar canal/sistema; revocar claves; restablecer fuente autoritativa; invalidar artefacto; reproducir; reconstruir cadena; preservar evidencia y notificar fraude/datos"},
        "THR-011": {"assets": "modelos, agentes, herramientas, prompts, RAG, embeddings, datasets, memoria, identidades, APIs, evaluaciones y proveedores de IA", "inventory": "AI bill of materials, modelos/versiones, datos/finalidad/base, prompts, tools/permissions, memoria, conectores, owner, región, dependencias y evaluaciones", "prevent": "IAM y mínimo privilegio por agente; sandbox; aprobación humana; validación de tool calls; Prompt Shields; filtrado; segregación; minimización; evals/red team; kill switch", "detect": "telemetría de prompts/tool calls; DLP; drift; anomalías de agente; prompt/jailbreak; task adherence; groundedness; abuso de APIs y cambios de modelo/datos", "respond": "deshabilitar agente/tool; bloquear flujo; rotar credenciales; aislar contexto/memoria; revertir modelo/datos; revisar logs; informar privacidad/safety; retest y redeploy"},
        "THR-012": {"assets": "datos personales, titulares, tratamientos, modelos, perfiles, logs, bases analíticas, transferencias, consentimientos y derechos", "inventory": "RoPA/data map, finalidad/base, categorías, titulares, destinos, transferencias, retención, perfiles, algoritmos, tercero y derechos", "prevent": "privacy by design; minimización; pseudonimización; segregación; encryption; purpose limitation; DLP; DPIA/PIA; consentimiento/control y gestión de lifecycle", "detect": "data discovery/classification; DLP; audit; anomalias de acceso; lineage; privacy risk; requests audit; detección de reidentificación/uso secundario", "respond": "contener acceso/uso; evaluar brecha y daño; conservar prueba; activar DPO/Legal; notificar si aplica; derechos/rectificación; reducir datos; corregir transparencia"},
        "THR-013": {"assets": "transacciones, pagos, clientes, cuentas, promociones, identidad, reglas de negocio, APIs y canales digitales", "inventory": "productos, journeys, transacciones, límites, patrones, pérdida esperada, cuentas de riesgo, conectores de pago, reglas y excepciones", "prevent": "strong customer auth; step-up; rules/velocity; separation; limits; device/risk signals; approval; secure business logic; monitoring and training", "detect": "behavioral analytics; anomaly detection; reconciliation; velocity; device/session; UEBA; rules/ML; complaint and loss signals", "respond": "bloquear/reversar; step-up; investigar caso; preservar evidencia; clawback; contactar cliente; ajustar regla/modelo; reportar cuando aplique y revisar pérdidas"},
        "THR-014": {"assets": "regiones, zonas, cloud, red, proveedores, instalaciones, licencias, habilidades, repuestos, SaaS y capacidad humana", "inventory": "dependency map, concentración, SPOF, SLA, capacidad, región, sustitución, RTO/RPO, portability, lock-in, skills y modos degradados", "prevent": "diversificación; multi-zone/region apropiado; active-active o DR según coste/mission; spare capacity; exit plan; interoperability; chaos/resilience testing", "detect": "health monitoring; capacity; SLA/SLO; supplier health; concentration KRI; synthetic tests; dependency telemetry y señales externas", "respond": "failover/traffic shift; activate alternate supplier/region; preserve data consistency; capacity scaling; degraded mode; backout; communicate and reprotect"},
        "THR-015": {"assets": "requisitos, políticas, controles, evidencia, contratos, registros, datos, aprobaciones, excepciones, owners y plazos", "inventory": "obligation register, jurisdicción, alcance, owner, control mapping, evidence, expiry, audit trail, excepción, changes y evidencia de terceros", "prevent": "governance; control design; policy lifecycle; approvals; training; GRC mapping; compliance as code; privacy/legal review; evidence collection", "detect": "continuous compliance; audit; exception monitoring; DLP/audit logs; control testing; policy drift; regulatory and supplier change monitoring", "respond": "activar Legal/DPO/riesgo; contener incumplimiento; remediar; evaluar notificación/impacto; preservar evidencia; corregir control; comunicar y demostrar cierre"},
    }


def control_family(threat_id: str, name: str, origin: str, domain: str = "") -> str:
    text = (name + " " + domain).lower()
    if origin == "Natural" or any(k in text for k in ["fuego", "agua", "desastres naturales", "climáticos"]):
        return "physical_disaster"
    if origin == "Industrial":
        if any(k in text for k in ["comunicaciones", "suministros esenciales", "corte"]):
            return "dependency"
        if "electromagn" in text: return "physical_integrity"
        return "physical_ops"
    if any(k in text for k in ["software dañino", "ransomware", "wiper", "malware"]): return "malware"
    if any(k in text for k in ["identidad", "privilegios", "sesión", "acceso no autorizado", "suplant", "ingeniería social", "fraude"]): return "identity"
    if any(k in text for k in ["programas", "configuración", "software", "aplic", "api", "ci/cd", "secreto", "vulnerabilidad", "código"]): return "app_config"
    if any(k in text for k in ["personal", "organización", "usuarios", "administrador"]): return "people_process"
    if any(k in text for k in ["información", "logs", "registros", "secuencia", "mensajes", "programas"]): return "data_integrity"
    if any(k in text for k in ["denegación", "agotamiento", "disponibilidad", "indisponibilidad", "concentración", "cadena de suministro"]): return "availability_supply"
    if any(k in text for k in ["robo", "equipos", "destructivo", "ocupación", "extorsión"]): return "physical_attack"
    if any(k in text for k in ["prompt", "modelo", "agente", "ia", "memoria"]): return "ai"
    if any(k in text for k in ["privacidad", "linking", "identifying", "detecting", "transparencia"]): return "privacy"
    if any(k in text for k in ["cumplimiento", "compliance"]): return "compliance"
    if any(k in text for k in ["interceptación", "escucha", "tráfico", "repudio"]): return "network_integrity"
    return "generic"


def family_controls() -> dict[str, dict]:
    return {
        "malware": {"assets": "endpoints, servers, email/collaboration, cloud workloads, storage, endpoints de administración y dispositivos IoT/OT afectados", "I": "inventario hardware/software/versión, criticidad, propietario, exposición, cobertura antimalware/EDR, backups y excepciones", "P": "hardening, patching, mínimo privilegio, ASR/allowlisting, filtros, segmentación, backups aislados/inmutables y controles de ejecución", "D": "EDR/XDR, antimalware, sandbox, detección de cifrado/cambios masivos, SIEM, investigación e indicadores", "R": "aislar, revocar identidad, bloquear indicadores, preservar evidencia, erradicar, restaurar desde copia probada y validar"},
        "identity": {"assets": "identidades humanas y no humanas, privilegios, sesiones, tokens, métodos MFA, cuentas de servicio, aplicaciones y federaciones", "I": "inventario de identidades, roles, privilegios, dispositivos, sesiones, aplicaciones consentidas, terceros, cuentas huérfanas y caminos de confianza", "P": "MFA resistente a phishing, Conditional Access, PIM/JIT, managed identity, mínimo privilegio, rotación de secretos y validación fuera de banda", "D": "riesgo de identidad/ITDR, anomalías, cambio de privilegios, credenciales filtradas, UEBA, correlación de correo/endpoints/apps", "R": "revocar sesiones/tokens, deshabilitar o restablecer, retirar privilegios/consent, investigar persistencia y movimiento, y volver a emitir credenciales"},
        "app_config": {"assets": "aplicaciones, APIs, código, pipelines, dependencias, contenedores, secretos, bases de datos y configuraciones", "I": "inventario por propietario, versión, exposición, SBOM, secret/config state, dependencias, entorno, datos y ruta de despliegue", "P": "SDLC seguro, policy/IaC, SAST/DAST/SCA, signed artifacts, secret management, hardening, gateway/WAF y change control", "D": "drift/config scanning, CSPM/CWPP, pipeline scanning, runtime/API anomalies, FIM, logs y pruebas continuas", "R": "aislar/revertir componente, rotar secretos, bloquear tráfico/versión, corregir, restaurar, retestear, eliminar excepción y comunicar"},
        "availability_supply": {"assets": "servicios, redes, regiones, proveedores, capacidad, colas, links, SaaS, utilidades, identidad y dependencias críticas", "I": "mapa de dependencias, propietarios, SLA/SLO, capacidad, SPOF, RTO/RPO, rutas alternativas, proveedores y modos degradados", "P": "redundancia, multi-zone/region proporcional, rate limiting, autoscaling, caching, circuit breaker, reservas, contratos y planes de salida", "D": "health, SLO, capacidad, dependencia/proveedor, synthetic monitoring, tráfico anómalo y correlación de fallos", "R": "activar mitigación/failover/degraded mode, escalar o desviar, recuperar ordenado, validar consistencia y comunicar/replicar dependencias"},
        "people_process": {"assets": "personas, roles, administradores, procesos, operaciones, aprobaciones, cambios, formación, guardias y conocimiento", "I": "inventario de roles, críticas, turnos, owners, competencias, privilegios, cambios, runbooks, sucesión y dependencia de personas clave", "P": "segregación de funciones, cuatro ojos, SOP, automatización, formación, gestión de cambios, accesos JML y planes de continuidad de personal", "D": "controles de proceso, QA, auditoría, anomalías, cambios y resultados, incidentes repetidos, KPIs de formación/errores", "R": "detener/corregir proceso, rollback, disponer respaldo, preservar evidencia, gestión de problema, postmortem y mejora/entrenamiento"},
        "data_integrity": {"assets": "datos, información, logs, registros, mensajes, código/configuración, replicas, backups, rutas, fuentes de verdad y evidencia", "I": "clasificación, lineage, propietarios, integridad esperada, fuentes de verdad, replicación, logging, retención, llaves y cadenas de custodia", "P": "mínimo privilegio, immutable/append-only, firma/hash, cifrado, versionado, validación, separación, backup aislado y change controls", "D": "FIM, DLP, audit, tamper detection, reconciliación, anomalías de volumen/secuencia y monitoreo de integridad/retención", "R": "aislar, preservar, identificar fuente autoritativa, revertir/restaurar, invalidar artefacto/llave, reconstruir y notificar según impacto"},
        "physical_ops": {"assets": "sedes, salas, equipos, utilidades, almacenamiento, redes físicas, HVAC, personal y servicios ambientales", "I": "site/equipment inventory, dependencia, criticidad, capacidad, condiciones, sensores, repuestos, rutas, contratos y operadores", "P": "redundancia física, UPS/generación, HVAC, mantenimiento, fire/water controls, spare parts, seguridad física y BCP/DR", "D": "sensores BMS, alarmas, health, inspecciones, acceso físico, temperatura/humedad, energía/comunicación y mantenimientos", "R": "proteger personas, activar EOC/BCP, failover, restaurar utilidades/equipo, inspeccionar, reconstruir y validar antes de reabrir"},
        "physical_disaster": {"assets": "sitios, regiones, personas, instalaciones, infraestructura, utilidades y servicios dependientes", "I": "mapas de amenaza por localización, criticidad de sitios, personal, proveedores, redundancia, accesos, RTO/RPO y rutas de evacuación", "P": "redundancia geográfica proporcional, resiliencia estructural, seguros, BCP/DR, protección contra fuego/agua y ejercicios", "D": "alertas meteorológicas/emergencia, sensores, BMS, health regional, seguridad física y comunicaciones de crisis", "R": "protección humana, evacuación, mando de crisis, failover, operación alterna, comunicación, evaluación del sitio y recuperación"},
        "physical_integrity": {"assets": "equipos, cables, racks, radio/EMI, sensores, soportes, shielding, ubicaciones y comunicaciones", "I": "inventory físico/topológico, cableado, emisiones, compatibilidad, blindaje, distancia, rutas y owner técnico", "P": "shielding, grounding, zoning, filtro, maintenance, physical controls, duplicación y pruebas de compatibilidad", "D": "EM/ambiente monitoring, interferencias, errores, inspección, FIM/configuración y sensores de facility", "R": "aislar fuente, switch route/equipment, reemplazar/reparar, validar interferencia y restaurar operación/registro"},
        "physical_attack": {"assets": "equipos, instalaciones, personas, medios, inventario, credenciales físicas, seguridad, backups y zonas", "I": "inventario y ubicación de activos, valor, riesgo, accesos, cámaras, custodios, medios, rutas de evacuación y terceros", "P": "physical access control, CCTV, guarding, zoning, tracking, tamper-evident, secure storage, seguros y separation", "D": "access anomalies, CCTV, alarms, inventory reconciliation, loss signals, tamper and personnel reports", "R": "proteger personas, lockdown, preservar escena/evidencia, activar seguridad/legal, localizar/revocar, recuperar y reforzar"},
        "dependency": {"assets": "electricidad, comunicaciones, utilities, SaaS, proveedores, capacidad, regiones, logística y contratos", "I": "dependency register, criticality, supplier/site, SLA, SPOF, capacity, alternate path, RTO/RPO y subdependencias", "P": "redundancy, alternate supplier/site, capacity buffer, DR, contract, portable architecture y degraded mode", "D": "provider/service health, SLA, capacity, network/utility telemetry, external advisories y synthetic transactions", "R": "failover/alternate supplier, degraded mode, queue/reroute, validate data, communicate, restore normal service and re-protect"},
        "ai": {"assets": "modelos, agentes, herramientas, prompts, RAG, datos, embeddings, memoria, evaluaciones, identidades, APIs y proveedores", "I": "AI BOM, owners, modelo/version, finalidad/datos/base, tools/permissions, connectors, memoria, región, proveedores, pruebas y riesgo", "P": "least-privilege agent identity, sandbox, human approval, Prompt Shields/task adherence, DLP, minimization, validation y red-team/evals", "D": "prompt/tool/memory telemetry, Content Safety, anomaly/drift, DLP, model/data integrity, usage/permission changes", "R": "disable agent/tool, rotate credentials, isolate memory/context, revert model/data, preserve logs, notify and retest before redeploy"},
        "privacy": {"assets": "datos personales, titulares, tratamientos, consentimientos, perfiles, algoritmos, transferencias, logs y destinatarios", "I": "data map/RoPA, finalidad/base, categorías/titulares, lineage, destinatarios, transferencias, retención y derechos", "P": "privacy by design, minimización, propósito, encryption/pseudonymization, DLP, DPIA, consent/control, retention/deletion", "D": "discovery/classification, DLP/audit, access anomaly, data lineage, privacy risk, requests, reidentification/secondary-use indicators", "R": "contener tratamiento/acceso, DPO/Legal, evaluar daño/breach, derechos/notificación según ley, corregir y documentar cierre"},
        "compliance": {"assets": "requisitos, jurisdicciones, contratos, políticas, controles, evidencia, excepciones, registros, dueños y plazos", "I": "registro de obligaciones, alcance, owner, evidence, controls, expiry, exceptions, jurisdictions y cambios", "P": "GRC/control mapping, policy lifecycle, approvals, training, compliance-as-code, legal/privacy reviews y evidence automation", "D": "continuous compliance, audits, control testing, policy drift, DLP/audit, exception and regulatory changes", "R": "activar Legal/DPO, contener, remediar, evaluar notificación, preservar evidencia, aprobar residual y demostrar cierre"},
        "network_integrity": {"assets": "redes, DNS, tráfico, PKI, mensajería, logs, sesiones, tiempos y canales externos", "I": "mapa de flujos, TLS/DNS/PKI, endpoints, protocolos, owners, certificados, logging y dependencias", "P": "segmentación, TLS/mTLS, DNSSEC donde aplique, PKI, autenticación, controls de encaminamiento, egress filtering y NDR", "D": "NDR, DNS/firewall/proxy logs, certificate anomalies, traffic baselines, SIEM, capture authorized y DLP", "R": "block/reroute, revoke certificates/keys, isolate channel/endpoint, restore trusted configuration and validate communications"},
        "generic": {"assets": "activos, procesos, personas, datos, identidades, tecnología, terceros y dependencias afectados por el evento", "I": "inventario por criticidad/owner, dependencias, exposición, requisitos, datos, tercero, baselines, cambios y controles existentes", "P": "mínimo privilegio, secure configuration, segmented design, resiliency, testing, training, supplier controls y change management", "D": "telemetría suficiente, integrity/anomaly rules, audit, SIEM, continuous control monitoring y pruebas", "R": "clasificar, contener, preservar, erradicar, recuperar, comunicar, validar residual y registrar lecciones"},
    }


def ms_phase_map() -> dict[str, dict[str, tuple[str, ...]]]:
    return {
        "malware": {"I": ("Defender XDR", "Defender for Endpoint", "Defender Vulnerability Management", "Security Exposure Management"), "P": ("Defender for Endpoint", "Intune", "Defender for Office 365", "Azure Backup", "Entra Conditional Access"), "D": ("Defender XDR", "Defender for Endpoint", "Defender for Office 365", "Sentinel"), "R": ("Defender XDR", "Defender for Endpoint", "Sentinel", "Azure Backup", "Security Copilot")},
        "identity": {"I": ("Entra ID Protection", "Defender for Identity", "Entra PIM", "Security Exposure Management"), "P": ("Entra Conditional Access", "Entra PIM", "Defender for Cloud Apps", "Key Vault"), "D": ("Entra ID Protection", "Defender for Identity", "Defender for Cloud Apps", "Defender XDR", "Sentinel"), "R": ("Entra ID Protection", "Defender XDR", "Defender for Identity", "Sentinel")},
        "app_config": {"I": ("Defender for Cloud", "Defender Vulnerability Management", "Defender for APIs", "GitHub Advanced Security", "Defender for DevOps"), "P": ("Defender for Cloud", "Azure Policy", "Defender for APIs", "Azure WAF", "Key Vault", "GitHub Advanced Security"), "D": ("Defender for Cloud", "Defender for APIs", "Defender XDR", "Azure Monitor", "Sentinel"), "R": ("Defender for Cloud", "Sentinel", "Azure Backup", "Security Copilot")},
        "availability_supply": {"I": ("Azure Monitor", "Defender for Cloud", "Azure Policy", "Security Exposure Management"), "P": ("Azure DDoS Protection", "Azure WAF", "Front Door", "Traffic Manager", "Site Recovery", "Azure Backup"), "D": ("Azure Monitor", "Service Health", "Sentinel", "Defender for Cloud"), "R": ("Site Recovery", "Azure Backup", "Front Door", "Traffic Manager", "Sentinel")},
        "people_process": {"I": ("Entra", "Purview Audit", "Intune", "Compliance Manager"), "P": ("Entra PIM", "Intune", "Conditional Access", "Purview DLP"), "D": ("Purview Insider Risk", "Purview Audit", "Defender XDR", "Sentinel"), "R": ("Defender XDR", "Sentinel", "Purview Audit", "Security Copilot")},
        "data_integrity": {"I": ("Purview Information Protection", "Purview Data Map", "Defender for Cloud"), "P": ("Purview DLP", "Information Protection", "Key Vault", "Azure Backup", "Azure Policy"), "D": ("Purview Audit", "Defender for Cloud", "Defender for Endpoint", "Sentinel", "Azure Monitor"), "R": ("Azure Backup", "Defender XDR", "Sentinel", "Purview Audit")},
        "physical_ops": {"I": ("Defender for IoT", "Defender for Endpoint", "Intune", "Azure Monitor"), "P": ("Defender for IoT", "Intune", "Site Recovery", "Azure Backup"), "D": ("Defender for IoT", "Azure Monitor", "Sentinel"), "R": ("Sentinel", "Site Recovery", "Azure Backup", "Security Copilot")},
        "physical_disaster": {"I": ("Azure Resource Graph", "Defender for Cloud", "Service Health", "Azure Monitor"), "P": ("Site Recovery", "Azure Backup", "Availability Zones", "Traffic Manager"), "D": ("Service Health", "Azure Monitor"), "R": ("Site Recovery", "Azure Backup", "Traffic Manager", "Sentinel")},
        "physical_integrity": {"I": ("Defender for Endpoint", "Defender for IoT", "Intune", "Azure Monitor"), "P": ("Intune", "Defender for IoT", "Azure Policy"), "D": ("Defender for IoT", "Defender for Endpoint", "Azure Monitor", "Sentinel"), "R": ("Sentinel", "Site Recovery", "Azure Backup")},
        "physical_attack": {"I": ("Defender for Endpoint", "Defender for IoT", "Intune", "Security Exposure Management"), "P": ("Intune", "Defender for Endpoint", "Defender for IoT", "Azure Policy"), "D": ("Defender XDR", "Defender for IoT", "Sentinel", "Purview Audit"), "R": ("Defender XDR", "Sentinel", "Site Recovery", "Azure Backup")},
        "dependency": {"I": ("Defender for Cloud", "Azure Resource Graph", "Security Exposure Management", "Service Health"), "P": ("Site Recovery", "Availability Zones", "Traffic Manager", "Azure Backup"), "D": ("Azure Monitor", "Service Health", "Sentinel"), "R": ("Site Recovery", "Traffic Manager", "Azure Backup", "Sentinel")},
        "ai": {"I": ("Defender for Cloud AI SPM", "Purview Data Security", "Security Exposure Management"), "P": ("Azure AI Content Safety", "Entra", "Key Vault", "Purview DLP", "Conditional Access"), "D": ("Defender for Cloud AI threat protection", "Azure AI Content Safety", "Azure Monitor", "Sentinel"), "R": ("Sentinel", "Security Copilot", "Defender XDR", "Azure AI Content Safety")},
        "privacy": {"I": ("Purview Data Map", "Purview Information Protection", "Microsoft Priva"), "P": ("Purview DLP", "Information Protection", "Purview records", "Entra", "Key Vault"), "D": ("Purview Audit", "Purview Insider Risk", "Defender for Cloud Apps", "Compliance Manager"), "R": ("Microsoft Priva", "Purview Audit", "Defender XDR", "Sentinel", "Security Copilot")},
        "compliance": {"I": ("Purview Compliance Manager", "Azure Policy", "Defender for Cloud", "Security Exposure Management"), "P": ("Compliance Manager", "Azure Policy", "Purview", "Entra PIM"), "D": ("Compliance Manager", "Purview Audit", "Defender for Cloud", "Sentinel"), "R": ("Purview Audit", "Sentinel", "Security Copilot")},
        "network_integrity": {"I": ("Defender for Cloud", "Azure Monitor", "Security Exposure Management"), "P": ("Azure Firewall", "Azure WAF", "Private Link", "Key Vault", "Defender for Cloud"), "D": ("Defender for Cloud", "Defender XDR", "Sentinel", "Azure Monitor"), "R": ("Defender XDR", "Sentinel", "Azure Network Watcher", "Security Copilot")},
        "generic": {"I": ("Security Exposure Management", "Defender for Cloud", "Purview"), "P": ("Entra", "Defender for Cloud", "Intune", "Azure Policy"), "D": ("Defender XDR", "Sentinel", "Azure Monitor"), "R": ("Defender XDR", "Sentinel", "Azure Backup", "Site Recovery")},
    }


def source_by_product() -> dict[str, dict]:
    return {s["product"]: s for s in SOURCES}


def category_ms_notes(category_id: str) -> dict[str, str]:
    base = {
        "I": "Inventario y superficie; validar cobertura real por plataforma, nube, SaaS y estado de onboarding.",
        "P": "Controles de diseño requieren configuración, licencias, dueños, excepciones y pruebas; producto no equivale a mitigación.",
        "D": "La detección existe solo donde hay telemetría, conectores, reglas, calidad y retención suficientes.",
        "R": "Respuesta y recuperación requieren playbook, autoridad, pruebas RTO/RPO, comunicación y evidencia; las automatizaciones deben ser aprobadas.",
    }
    if category_id in {"THR-008", "THR-014"}:
        base["R"] += " En physical/disaster, priorizar personas, facility/operations y continuidad antes que la acción digital."
    if category_id == "THR-011":
        base["P"] += " Para agentes, separar guardrails de contenido de IAM, herramientas, memoria, datos y kill switch."
    return base


def load_csv(path: Path) -> list[dict]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_md(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def style_ws(ws, title: str, widths: dict[int, int] | None = None) -> None:
    ws.freeze_panes = "A2"
    ws.auto_filter.ref = ws.dimensions
    ws.sheet_view.showGridLines = False
    for cell in ws[1]:
        cell.fill = PatternFill("solid", fgColor="17365D")
        cell.font = Font(color="FFFFFF", bold=True)
        cell.alignment = Alignment(wrap_text=True, vertical="center")
    ws.row_dimensions[1].height = 38
    for row in ws.iter_rows(min_row=2):
        for c in row:
            c.alignment = Alignment(vertical="top", wrap_text=True)
    if ws.max_row > 1:
        tab = Table(displayName=re.sub(r"\W+", "", title)[:24] + "Table", ref=ws.dimensions)
        tab.tableStyleInfo = TableStyleInfo(name="TableStyleMedium2", showFirstColumn=False, showLastColumn=False, showRowStripes=True, showColumnStripes=False)
        ws.add_table(tab)
    if widths:
        for idx, width in widths.items():
            ws.column_dimensions[get_column_letter(idx)].width = width
    else:
        for i in range(1, ws.max_column + 1):
            ws.column_dimensions[get_column_letter(i)].width = min(45, max(12, max(len(str(ws.cell(r, i).value or "")) for r in range(1, min(ws.max_row, 100) + 1)) + 2))


def add_sheet(wb: Workbook, title: str, headers: list[str], rows: list[list], widths: dict[int, int] | None = None):
    ws = wb.create_sheet(title)
    ws.append(headers)
    for row in rows:
        ws.append(row)
    style_ws(ws, title, widths)
    return ws


def save_workbook(path: Path, wb: Workbook) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    wb.save(path)
    check = load_workbook(path, data_only=False, read_only=False)
    assert check.sheetnames
    for ws in check.worksheets:
        assert ws.max_row >= 1 and ws.max_column >= 1
    check.close()


def md_table(headers: list[str], rows: list[list]) -> str:
    out = ["| " + " | ".join(headers) + " |", "| " + " | ".join("---" for _ in headers) + " |"]
    for row in rows:
        vals = [str(v).replace("|", "\\|").replace("\n", " ") for v in row]
        out.append("| " + " | ".join(vals) + " |")
    return "\n".join(out)


def build_categories(categories: list[dict], profiles: dict[str, dict]) -> tuple[list[dict], list[dict]]:
    summary = []
    lifecycle = []
    for c in categories:
        p = profiles[c["id"]]
        summary.append({"category_id": c["id"], "category": c["name"], "domain": c["domain"], "vulnerable_assets": p["assets"], "identification": p["inventory"], "prevention": p["prevent"], "detection": p["detect"], "response_recovery": p["respond"], "status": "estado_del_arte_base", "validated_at": TODAY})
        for phase_code, phase, text_key in zip(PHASE_CODES, PHASES, ["inventory", "prevent", "detect", "respond"]):
            lifecycle.append({"category_id": c["id"], "category": c["name"], "phase_code": phase_code, "phase": phase, "vulnerable_asset_types": p["assets"], "state_of_art_requirement": p[text_key], "control_types": "; ".join({"I":"asset inventory; dependency mapping; risk context; owner", "P":"governance; architecture; configuration; access; resilience; secure lifecycle", "D":"telemetry; monitoring; analytics; audit; testing", "R":"incident command; containment; eradication; recovery; communication; lessons"}[phase_code].split("; ")), "evidence_examples": {"I":"CMDB/asset inventory; data map; architecture; owner; exposure", "P":"policy; configuration; design; coverage; approvals; exception", "D":"rule/connector; alert; test case; dashboard; detection efficacy", "R":"playbook; timeline; isolation log; restore proof; communications; post-incident action"}[phase_code], "metric_examples": {"I":"% activos inventariados con owner/criticidad; dependencias no resueltas", "P":"% controles y excepciones; cobertura por plataforma", "D":"MTTD; coverage; FP/FN; fuente/retención; prueba de detección", "R":"MTTC; MTTRecover; RTO/RPO real; acciones vencidas"}[phase_code]})
    return summary, lifecycle


def build_magerit(magerit: list[dict], extensions: list[dict], profiles: dict[str, dict]) -> tuple[list[dict], list[dict]]:
    items = []
    for t in magerit:
        items.append({"id": t["magerit_id"], "kind": "MAGERIT_OFFICIAL", "family": t["family"], "origin": t["origin"], "name": t["name"], "domain": t["origin"], "magerit_base": t["magerit_id"], "specificity": t["specificity"], "external_mapping": ""})
    for e in extensions:
        items.append({"id": e["extension_id"], "kind": "SCAVANNA_NON_OFFICIAL_EXTENSION", "family": "EXT", "origin": e["domain"], "name": e["name"], "domain": e["domain"], "magerit_base": e["magerit_base"], "specificity": "extension", "external_mapping": e["external_mapping"]})
    summary=[]; lifecycle=[]
    for item in items:
        fam=control_family(item["id"], item["name"], item["origin"], item["domain"])
        p=profiles[fam]
        summary.append({**item, "control_family": fam, "vulnerable_assets": p["assets"], "identification": p["I"], "prevention": p["P"], "detection": p["D"], "response_recovery": p["R"], "status": "state_of_art_baseline", "validated_at": TODAY})
        for pc,phase,key in zip(PHASE_CODES,PHASES,["I","P","D","R"]):
            lifecycle.append({"threat_id":item["id"],"threat_name":item["name"],"record_type":item["kind"],"family":item["family"],"origin":item["origin"],"control_family":fam,"phase_code":pc,"phase":phase,"vulnerable_asset_types":p["assets"],"state_of_art_requirement":p[key],"magerit_base":item["magerit_base"],"external_mapping":item["external_mapping"],"evidence_examples": {"I":"asset/CMDB/data map; owner; architecture; dependency; exposure", "P":"design/policy/config; coverage; exception; owner; test", "D":"connector/log; rule; alert; tuning; test; incident correlation", "R":"playbook; authorization; containment timeline; restore/validation; postmortem"}[pc],"test_examples": {"I":"sample reconciliation and completeness", "P":"configuration review; control simulation", "D":"purple team/BAS/tabletop; false positive and negative review", "R":"tabletop/restore/failover; RTO/RPO and authority validation"}[pc]})
    return summary,lifecycle


def lookup_source(product: str, aliases: dict[str, str], by_product: dict[str, dict]) -> dict:
    if product in by_product: return by_product[product]
    aliases_exact={
        "Defender XDR":"Microsoft Defender XDR", "Defender for Endpoint":"Microsoft Defender for Endpoint", "Defender for Identity":"Microsoft Defender for Identity",
        "Defender for Cloud":"Microsoft Defender for Cloud", "Defender for IoT":"Microsoft Defender for IoT", "Defender for APIs":"Microsoft Defender for APIs",
        "Defender Vulnerability Management":"Microsoft Defender Vulnerability Management", "Security Exposure Management":"Microsoft Security Exposure Management",
        "Sentinel":"Microsoft Sentinel", "Intune":"Microsoft Intune", "Entra PIM":"Microsoft Entra Privileged Identity Management", "Entra Conditional Access":"Microsoft Entra Conditional Access",
        "Conditional Access":"Microsoft Entra Conditional Access", "Entra ID Protection":"Microsoft Entra ID Protection", "Entra":"Microsoft Entra",
        "Defender for Office 365":"Microsoft Defender for Office 365", "Purview DLP":"Microsoft Purview Data Loss Prevention", "Information Protection":"Microsoft Purview Information Protection",
        "Purview Information Protection":"Microsoft Purview Information Protection", "Purview Insider Risk":"Microsoft Purview Insider Risk Management", "Purview Audit":"Microsoft Purview Audit y Compliance Manager",
        "Compliance Manager":"Microsoft Purview Audit y Compliance Manager", "Purview":"Microsoft Purview Information Protection", "Defender for Cloud Apps":"Microsoft Defender for Cloud Apps",
        "Key Vault":"Azure Key Vault y Managed HSM", "Azure Backup":"Azure Backup", "Site Recovery":"Azure Site Recovery", "Azure Monitor":"Azure Monitor y Log Analytics",
        "Azure DDoS Protection":"Azure DDoS Protection", "Azure WAF":"Azure Web Application Firewall", "GitHub Advanced Security":"GitHub Advanced Security y Azure DevOps",
        "Defender for DevOps":"Microsoft Defender for DevOps", "Azure Policy":"Azure Policy y Guest Configuration", "Security Copilot":"Microsoft Security Copilot",
        "Azure AI Content Safety":"Azure AI Content Safety", "Defender for Cloud AI SPM":"Microsoft Defender for Cloud", "Defender for Cloud AI threat protection":"Microsoft Defender for Cloud",
        "Purview Data Map":"Microsoft Purview Data Map", "Purview Data Security":"Microsoft Purview Information Protection", "Microsoft Priva":"Microsoft Priva",
        "Purview records":"Microsoft Purview Records Management", "Front Door":"Azure Front Door", "Traffic Manager":"Azure Traffic Manager",
        "Service Health":"Azure Service Health", "Azure Resource Graph":"Azure Resource Graph", "Availability Zones":"Availability Zones",
        "Private Link":"Azure Private Link", "Azure Firewall":"Azure Firewall", "Azure Network Watcher":"Azure Network Watcher"
    }
    key=aliases_exact.get(product, product)
    if key in by_product: return by_product[key]
    return {"source_id":"MS-GAP","product":product,"area":"Capacidad nombrada en Learn/arquitectura; requiere validar la página oficial específica","url":"","scope_note":"Validación de producto/licencia/ámbito requerida antes de decidir."}


def build_ms_rows(base_rows: list[dict], scope: str, profiles: dict[str, dict], ms_map: dict[str, dict[str, tuple[str,...]]]) -> list[dict]:
    aliases={}; by_product=source_by_product(); rows=[]
    for item in base_rows:
        tid=item.get("category_id") or item.get("threat_id") or item.get("id")
        name=item.get("category") or item.get("name") or item.get("threat_name")
        fam=item.get("control_family")
        if not fam:
            fam=control_family(tid,name,"",item.get("domain",""))
        for pc,phase in zip(PHASE_CODES,PHASES):
            for product in ms_map[fam][pc]:
                source=lookup_source(product,aliases,by_product)
                req=item.get({"I":"identification","P":"prevention","D":"detection","R":"response_recovery"}[pc],"") or profiles[fam][pc]
                rows.append({"scope":scope,"record_id":tid,"record_name":name,"record_type":item.get("kind", "CATEGORY"),"control_family":fam,"phase_code":pc,"phase":phase,"state_of_art_requirement":req,"microsoft_product_capability":product,"learn_source_id":source["source_id"],"official_url":source["url"],"documented_area":source["area"],"coverage_scope":source["scope_note"],"mapping_status":"candidate", "validation_required":"Confirmar licencia, región, plataforma, integración, configuración, cobertura y eficacia antes de declarar cobertura", "validated_at":TODAY})
    return rows


def build_docs(categories, magerit, extensions, cat_summary, cat_lifecycle, mag_summary, mag_lifecycle, ms_cat, ms_mag, ms_sources):
    base=OUT
    write_md(base/"README.md", f"""# Estado del arte: mitigación por ciclo de amenaza

Fecha de corte: **{TODAY}**.

Este paquete responde a cuatro preguntas para cada registro:

1. **Identificación/inventario**: qué activos pueden verse afectados y qué debe inventariarse.
2. **Prevención/protección**: qué medidas reducen la probabilidad o degradación.
3. **Detección**: qué telemetría, controles o procesos permiten saber si ocurre.
4. **Respuesta/recuperación**: cómo contener, erradicar, recuperar y aprender.

> “Estado del arte” significa un baseline razonado para diseño y evaluación. No equivale a cobertura garantizada, lista exhaustiva ni obligación normativa. Debe contextualizarse por activos, sector, jurisdicción, arquitectura, licencia y evidencia.

## Paquetes

- `01-categorias-15/`: evaluación y Excel para las 15 categorías agregadas.
- `02-magerit-v3-ampliado/`: evaluación y Excel para las 57 entradas MAGERIT v3 más 22 extensiones no oficiales.
- `02-magerit-v3-ampliado/microsoft/`: mapeo Microsoft por las 79 amenazas y cuatro fases.
- `03-capacidades-microsoft/`: catálogo transversal de capacidades Microsoft, fuentes Learn y reglas de validación.

## Resultado de la validación previa

No existía el modelo de cuatro fases completo ni uniforme para los dos universos. La auditoría y las correcciones están documentadas en `VALIDACION.md`.

## Criterio de auditoría

El resultado se considera completo únicamente si cada registro tiene 4 filas de ciclo de vida y su respuesta declara activos, controles, evidencia, pruebas y límites. Una tecnología es una capacidad candidata, no una mitigación comprobada.

## Nota sobre los puntos 3 y 4 del encargo

Se interpreta el cuarto punto, que repite el tercero, como una segunda vista complementaria: un **catálogo transversal de capacidades Microsoft** y una **matriz requisito–producto** además del mapeo individual por amenaza. Ambas se entregan en este paquete.
""")
    cat_rows=[[r['category_id'],r['category'],r['domain'],r['vulnerable_assets'],r['identification'],r['prevention'],r['detection'],r['response_recovery']] for r in cat_summary]
    write_md(base/"01-categorias-15/README.md", "# Mitigación por las 15 categorías\n\nEstas 15 categorías son vistas agregadas; no sustituyen las 55 amenazas específicas de MAGERIT ni sus 2 entradas comodín.\n\n" + md_table(["ID","Categoría","Dominio","Activos vulnerables","Identificación/inventario","Prevención/protección","Detección","Respuesta/recuperación"],cat_rows) + "\n\n## Uso\n\nFiltrar primero por categoría, aplicar al inventario real y bajar a amenazas MAGERIT/extensiones. Medir cobertura y eficacia; no marcar una fase como cubierta por la sola compra o activación nominal de una tecnología.\n")
    mag_rows=[[r['id'],r['kind'],r['family'],r['name'],r['control_family'],r['magerit_base'],r['identification'],r['prevention'],r['detection'],r['response_recovery']] for r in mag_summary]
    write_md(base/"02-magerit-v3-ampliado/README.md", "# Mitigación MAGERIT v3 y extensiones no oficiales\n\nIncluye 57 entradas del índice MAGERIT v3 (55 específicas + 2 comodines) y 22 extensiones `EXT-*`; total: 79 registros.\n\nEl namespace oficial no se modifica. El detalle Microsoft se encuentra en `microsoft/`.\n\n" + md_table(["ID","Tipo","Familia","Amenaza","Familia de control","Base MAGERIT","Inventario","Prevención","Detección","Respuesta"],mag_rows) + "\n")
    ms_rows=[[s['source_id'],s['product'],s['area'],s['url'],s['scope_note']] for s in ms_sources]
    write_md(base/"03-capacidades-microsoft/README.md", "# Capacidades Microsoft basadas en Microsoft Learn\n\nFuentes consultadas oficialmente mediante **Microsoft Learn MCP Server** y páginas de Microsoft Learn. Fecha de consulta: 2026-11-18.\n\n## Reglas\n\n- Microsoft Defender XDR correlaciona señales de productos licenciados y aprovisionados.\n- La presencia de un servicio no prueba configuración, cobertura, telemetría ni efectividad.\n- Licencias, regiones, plataformas y nombres comerciales cambian; validar antes de adquisición o diseño.\n- Para OT/IoT, respuesta y aislamiento deben estar autorizados por operación y safety.\n- Seguridad Copilot asiste; sus resultados deben ser revisados.\n- Azure Backup y Site Recovery requieren RPO/RTO, arquitectura, pruebas y capacidad.\n\n" + md_table(["ID","Producto","Área oficial","Fuente Microsoft Learn","Alcance/limitación"],ms_rows) + "\n")
    write_md(base/"02-magerit-v3-ampliado/microsoft/README.md", "# Mapeo de capacidades Microsoft a amenazas MAGERIT-ampliadas\n\nEste directorio mapea cada una de las 79 entradas contra capacidades Microsoft candidatas para las cuatro fases.\n\nEs una matriz de diseño, no una garantía: confirmar cobertura por plataforma, licencia, región, conector, política, telemetría, owner, prueba y eficacia.\n\nTambién existe una vista equivalente para las 15 categorías en `01-categorias-15/` y un catálogo transversal en `03-capacidades-microsoft/`.\n")

def main():
    categories=load_csv(ROOT/"data/amenazas.csv")
    mag=load_csv(ROOT/"data/magerit-v3-amenazas.csv")
    ext=load_csv(ROOT/"data/extensiones-amenazas.csv")
    assert len(categories)==15 and len(mag)==57 and len(ext)==22
    cp=category_profiles(); fp=family_controls(); msm=ms_phase_map()
    cat_summary,cat_lifecycle=build_categories(categories,cp)
    mag_summary,mag_lifecycle=build_magerit(mag,ext,fp)
    ms_cat=build_ms_rows(cat_summary,"15_CATEGORIES",fp,msm)
    ms_mag=build_ms_rows(mag_summary,"MAGERIT_V3_SCAVANNA_NON_OFFICIAL",fp,msm)
    build_docs(categories,mag,ext,cat_summary,cat_lifecycle,mag_summary,mag_lifecycle,ms_cat,ms_mag,SOURCES)

    wb=Workbook(); wb.remove(wb.active)
    add_sheet(wb,"Resumen categorías",list(cat_summary[0].keys()),[[r[k] for k in cat_summary[0].keys()] for r in cat_summary],{1:14,2:28,3:14,4:42,5:50,6:50,7:50,8:50,9:20,10:14})
    add_sheet(wb,"Ciclo por categoría",list(cat_lifecycle[0].keys()),[[r[k] for k in cat_lifecycle[0].keys()] for r in cat_lifecycle],{1:14,2:28,3:10,4:25,5:40,6:55,7:50,8:55,9:38})
    add_sheet(wb,"Microsoft categorías",list(ms_cat[0].keys()),[[r[k] for k in ms_cat[0].keys()] for r in ms_cat],{1:18,2:14,3:28,4:20,5:20,6:9,7:24,8:55,9:38,10:14,11:48,12:38,13:50,14:12,15:55,16:14})
    add_sheet(wb,"Guía de uso",["Tema","Regla"],[
        ["Cobertura","15 categorías × 4 fases = 60 filas"],
        ["Interpretación","Categorías son vistas agregadas; bajar a amenazas específicas y escenarios"],
        ["Estado","Baseline no equivale a evaluación real ni certificación"],
        ["Microsoft","Capacidad candidata; validar licencia, región, plataforma, telemetría, configuración y evidencia"],
    ],{1:26,2:95})
    save_workbook(OUT/"01-categorias-15/matriz-estado-del-arte-15-categorias.xlsx",wb)

    wb=Workbook(); wb.remove(wb.active)
    add_sheet(wb,"Resumen 79 amenazas",list(mag_summary[0].keys()),[[r[k] for k in mag_summary[0].keys()] for r in mag_summary],{1:14,2:30,3:10,4:16,5:38,6:16,7:35,8:18,9:20,10:22,11:45,12:55,13:55,14:55,15:55,16:20,17:14})
    add_sheet(wb,"Ciclo 79 amenazas",list(mag_lifecycle[0].keys()),[[r[k] for k in mag_lifecycle[0].keys()] for r in mag_lifecycle],{1:14,2:38,3:30,4:10,5:16,6:22,7:9,8:24,9:42,10:55,11:35,12:36,13:46,14:45})
    add_sheet(wb,"Controles por fase",["Familia de control","Activos","Identificación","Prevención","Detección","Respuesta"],[[k,v['assets'],v['I'],v['P'],v['D'],v['R']] for k,v in fp.items()],{1:24,2:42,3:55,4:55,5:55,6:55})
    save_workbook(OUT/"02-magerit-v3-ampliado/matriz-estado-del-arte-magerit-v3-ampliado.xlsx",wb)

    wb=Workbook(); wb.remove(wb.active)
    add_sheet(wb,"Mapeo Microsoft amenazas",list(ms_mag[0].keys()),[[r[k] for k in ms_mag[0].keys()] for r in ms_mag],{1:26,2:14,3:38,4:30,5:22,6:9,7:25,8:55,9:38,10:14,11:50,12:40,13:55,14:12,15:60,16:14})
    add_sheet(wb,"Fuentes Microsoft Learn",["ID","Producto","Área","URL","Alcance y limitación"],[[s['source_id'],s['product'],s['area'],s['url'],s['scope_note']] for s in SOURCES],{1:12,2:38,3:55,4:75,5:70})
    add_sheet(wb,"Cobertura por fase",["Fase","Entradas con mapeo","Total esperado","Porcentaje"],[[phase,len({r['record_id'] for r in ms_mag if r['phase']==phase}),79,100.0] for phase in PHASES],{1:28,2:24,3:18,4:14})
    save_workbook(OUT/"02-magerit-v3-ampliado/microsoft/mapeo-microsoft-magerit-v3-ampliado.xlsx",wb)

    unique_cap={}
    for row in ms_cat+ms_mag:
        key=(row['microsoft_product_capability'],row['phase_code'])
        unique_cap.setdefault(key,{"capability":row['microsoft_product_capability'],"phase":row['phase'],"phase_code":row['phase_code'],"requirements":set(),"records":set(),"source_id":row['learn_source_id'],"url":row['official_url'],"scope":row['coverage_scope']})
        unique_cap[key]["requirements"].add(row['state_of_art_requirement'])
        unique_cap[key]["records"].add(row['record_id'])
    cap_rows=[]
    for v in unique_cap.values():
        cap_rows.append([v['capability'],v['phase_code'],v['phase']," | ".join(sorted(v['requirements'])[:5]),len(v['records']),v['source_id'],v['url'],v['scope']])
    wb=Workbook(); wb.remove(wb.active)
    add_sheet(wb,"Catálogo transversal",["Capacidad Microsoft","Código fase","Fase","Requisitos candidatos que apoya","Registros mapeados","Fuente","URL oficial","Límite/validación"],cap_rows,{1:36,2:12,3:26,4:80,5:18,6:14,7:70,8:70})
    add_sheet(wb,"Fuentes oficiales",["ID","Producto","Área","URL","Alcance"],[[s['source_id'],s['product'],s['area'],s['url'],s['scope_note']] for s in SOURCES],{1:12,2:38,3:55,4:75,5:70})
    add_sheet(wb,"Reglas de decisión",["Regla","Criterio"],[
        ["Producto no es control","Requiere configuración, proceso, owner, prueba y evidencia"],
        ["XDR no es universal","Defender XDR correlaciona señales de productos licenciados/aprovisionados"],
        ["OT/Safety","Respuesta Microsoft debe coordinarse con operación, ingeniería y safety"],
        ["Privacidad","DLP/AI no sustituye base legal, DPIA, minimización ni DPO/Legal"],
        ["Recuperación","Backup sin restore probado ni backup/políticas/alcance no es recuperación"],
        ["Licenciamiento","Validar Microsoft Learn y acuerdos comerciales actuales antes de decidir"],
    ],{1:28,2:90})
    save_workbook(OUT/"03-capacidades-microsoft/catalogo-capacidades-microsoft.xlsx",wb)

    manifest=[]
    for p in sorted(OUT.rglob('*')):
        if p.is_file() and p.name != 'MANIFEST.json':
            b=p.read_bytes(); manifest.append({'path':p.relative_to(OUT).as_posix(),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
    (OUT/'MANIFEST.json').write_text(json.dumps({'version':'1.0.0','generated_at':TODAY,'official_status':'state_of_art_adaptation_non_official','records':{'categories':15,'magerit':57,'extensions':22,'threat_total':79},'files':manifest},ensure_ascii=False,indent=2),encoding='utf-8')
    print('category summary',len(cat_summary),'lifecycle',len(cat_lifecycle),'ms rows',len(ms_cat))
    print('magerit summary',len(mag_summary),'lifecycle',len(mag_lifecycle),'ms rows',len(ms_mag))
    print('sources',len(SOURCES),'capability rows',len(cap_rows))


if __name__ == '__main__':
    main()

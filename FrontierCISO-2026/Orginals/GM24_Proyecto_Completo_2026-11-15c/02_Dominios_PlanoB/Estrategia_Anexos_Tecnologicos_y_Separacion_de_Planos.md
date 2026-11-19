# Estrategia de anexos tecnológicos y separación de planos: corpus académico (GM-24) vs. marco de gobierno de capacidades contratadas

> 2026-11-14. Fija la distinción entre **el GM-24 como corpus académico respaldado** y **su uso como marco para gobernar y gestionar capacidades que un CISO ha contratado**, y define la estrategia de anexos por tecnología (Microsoft 365 E7, Sentinel, Defender for Cloud).

## 1. Los dos planos
| Plano | Qué contiene | Versionado | Quién lo gobierna | Carácter | Audiencia |
|---|---|---|---|---|---|
| Plano A — Corpus académico (GM-24) | Conceptos-lección (K, AMP, HC, PA), pre-ensayos, competencias, unidades, mapeo a estándares y certificaciones | V4…V7, V7.1 (editorial); V8 solo si una instancia exige un concepto nuevo | Comité curricular; ESS y ChangeSets al Atlas | Respaldado por NIST/ISACA/MITRE/OWASP/CIS/CSA; independiente de proveedor | Alumno/profesional; autor; ontología/MCP |
| Plano B — Marco de gobierno de capacidades contratadas | Productos-control por dominio: ficha, grilla CSF, modelo operativo, agentes, anexos, KPIs, permisos; AGC | Versionado propio por dominio (Dominio_X vX.Y); cambia con releases de Microsoft | PO-GAC de cada dominio; CISO dueño del portafolio; proveedores vía anexos | Específico del escenario sobre bases agnósticas; verificable en Learn; sujeto a licencias y GA/preview | CISO y owners; SOC; proveedores; auditoría |

**Regla de oro:** nada del plano B modifica el plano A directamente.

## 2. Relaciones entre planos
| Relación | Regla |
|---|---|
| Concepto (A) → Instancia (B) | Un concepto se instancia en cada dominio (ProductPractice EXEMPLIFIES eo:OP). |
| Instancia (B) → Concepto (A) | Una instancia puede revelar brecha o sobre-especificidad (V7.1); si exige concepto nuevo, se propone candidato; nunca se edita el corpus desde una instancia. |
| Estándares | A se mapea por concepto; B hereda y agrega evidencia técnica por control. |
| Horas | Las horas curriculares viven en A; la práctica en un dominio se contabiliza como práctica (91 h). |
| Versionado | A cambia por ChangeSet con ESS. B cambia por release de plataforma, licencias o decisión del CISO; cada dominio lleva VERSION.md. |
| Lo que un CISO contrató | B describe capacidades contratadas y cómo gobernarlas con el vocabulario de A. Un CISO sin Microsoft usa A íntegro y construye su propio B. |

## 3. Instancias de dominio (plano B)
| Dominio | Tecnología | Paquete / versión |
|---|---|---|
| Productividad | Defender for Office 365 (EOP) en Defender XDR | Dominio_PRODUCTIVIDAD v1.1 |
| XDR | Defender XDR + sensores + Sentinel | Dominio_XDR v1.0 |
| Endpoints | Defender for Endpoint + Vulnerability Management + Intune | Dominio_ENDPOINTS v1.0 |
| Identidades | Defender for Identity + Entra ID Protection + CA + ID Governance | Dominio_IDENTIDADES v1.0 |
| Datos | Purview (labels, DLP, DSPM/DSPM for AI, Insider Risk) + MDA | Dominio_DATOS v1.0 |
| SIEM/SOAR | Microsoft Sentinel (portal Defender) | Dominio_SIEM v1.0 |
| Nube | Defender for Cloud (CSPM, CWPP, AI Services) | Dominio_NUBE v1.0 |
| Apps / SaaS | Defender for Cloud Apps + app governance + CA app control | Dominio_APPS v1.0 |

Comparten: rol PO-GAC, 41 competencias, 379 conceptos (V7.1), 24 AGC, RACI, L0–L4 y recursos comunes. **Ninguna de las ocho requirió conceptos nuevos.**

## 4. Próximas instancias
| Dominio | Tecnología | Paquete | Prioridad | Observación |
|---|---|---|---|---|
| Exposición | Security Exposure Management + Defender EASM | Dominio_EXPOSICION | Media | Puede absorberse como vista de XDR |
| IA y agentes (transversal) | Defender para IA, Agent 365, Entra Agent ID, Purview DLP para IA | Dominio_IA | Alta | Consolidar lo ya instanciado en AGC/Identidades/Datos/Nube |

## 5. Plantilla uniforme de una instancia
| Sección | Contenido | Fuente de verdad |
|---|---|---|
| 01 Ficha | Nombre, dominio ZT, tecnología, CSF, fuente oficial, objetivo, SLO, owner, diferencia, interfaces, personas, permisos, grilla CSF | Ops guide del producto + G2.1-PA01 |
| 02 Instanciación | Concepto V7 → cómo lo instancia el dominio; hallazgos para el corpus | Catálogo V7.1 |
| 03 Modelo operativo | Tareas por cadencia con persona, CSF, SAF, eo:OP, L0–L4, agente, KPI, fuente | Ops guide; MAEO |
| 04 Agentes + anexos | Tools/knowledge/skills propios, compartidos y comunes; permisos; estado GA/preview/verificar | Learn; AGC |
| VERSION.md · XLSX · JSON | Versionado propio; gemelos verificables | build/ |

## 6. Licencias y SKUs que condicionan el plano B
| Producto / SKU | Qué habilita | Dominios |
|---|---|---|
| Microsoft 365 E5 / E7 | Defender XDR (MDO P2, MDE P2, MDI, MDA), Purview, Entra ID P2; E7: Agent 365 + Entra Suite | Todos los dominios; gobierno de agentes |
| Microsoft Sentinel | SIEM/SOAR, data lake, MCP server (preview); portal de Defender desde 31-mar-2027 | XDR, SIEM |
| Microsoft Defender for Cloud | CSPM/CWPP multicloud, attack paths, AI Services | Nube |
| Security Copilot | SCU; agentes (ruta R1) | Todas las flotas |
| Copilot Studio / Foundry | Créditos/capacidad; tokens (R2/R3) | Todas las flotas |
| Workload Identities Premium | Riesgo de service principals/agentes | Identidades |

## 7. Cómo leer el conjunto como CISO
1. Para formar personas: plano A (independiente de lo que compraste). 2. Para gobernar lo que compraste: plano B, con el vocabulario de A; auditar cobertura, madurez y autonomía. 3. Si cambiás de proveedor: A no cambia; reconstruís B. 4. Si el proveedor cambia el producto: cambia B, no el corpus.

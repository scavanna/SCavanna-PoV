# Catálogo del stack de seguridad Microsoft × Gartner Peer Insights — versión validada y corregida

**AI CISO Atlas · dimensión `Technology → ProvidesCapability → MarketCategory`**

| Campo | Valor |
|---|---|
| Versión | v2 validada (reemplaza al borrador v1) |
| Fecha de verificación | 4 de noviembre de 2026 |
| Alcance | 255 elementos del borrador: 239 afirmaciones (tablas y texto) y 16 inconsistencias internas |
| Fuentes | Microsoft Learn, service descriptions, Product Terms, notas oficiales de licenciamiento, páginas oficiales de producto y precios, blogs oficiales de Microsoft y Gartner Peer Insights (detalle en el Anexo C) |
| Prelación | Product Terms y notas de licenciamiento > Learn y service descriptions > páginas de producto y precios > blogs oficiales |
| Precios | USD de lista por usuario/mes, compromiso anual, vigentes desde el 1-jul-2026; varían por país, moneda y contrato |

## 0. Resumen de la validación

Se revisaron **239 afirmaciones** del borrador. De ellas, 8 son criterios editoriales o metodológicos (se conservan o se amplían) y **231 son afirmaciones verificables**, con este resultado:

| Resultado | Afirmaciones verificables |
|---|---|
| ✅ Correctas | 148 |
| ⚠️ Correctas con matiz (texto corregido) | 71 |
| 🕒 Desactualizadas (actualizadas) | 8 |
| ❌ Incorrectas (corregidas) | 3 |
| ❔ No verificables (eliminadas o reemplazadas) | 1 |
| **Total** | **231** |

Además se resolvieron **16 inconsistencias internas** (mercados ausentes en la sección 5, contradicciones entre las secciones 4 y 5, filas duplicadas y nombres distintos para un mismo producto). El detalle por sección está en el Anexo A.

| Sección | Elementos | ✅ | ⚠️ | ❌ | 🕒 | ❔ | 📝 |
|---|---|---|---|---|---|---|---|
| Introducción (E7) | 1 | 1 | 0 | 0 | 0 | 0 | 0 |
| 1.A Microsoft Entra | 21 | 15 | 6 | 0 | 0 | 0 | 0 |
| 1.B Microsoft Defender | 19 | 11 | 6 | 0 | 2 | 0 | 0 |
| 1.C Microsoft Purview | 21 | 12 | 7 | 1 | 1 | 0 | 0 |
| 2.A Microsoft Intune | 13 | 8 | 5 | 0 | 0 | 0 | 0 |
| 2.B Seguridad de Windows | 24 | 19 | 3 | 0 | 2 | 0 | 0 |
| 3.A Defender for Cloud | 17 | 11 | 5 | 1 | 0 | 0 | 0 |
| 3.B Servicios de Azure | 30 | 25 | 4 | 0 | 1 | 0 | 0 |
| 4–5 Mercados Gartner | 42 | 16 | 26 | 0 | 0 | 0 | 0 |
| 6 Servicios | 10 | 5 | 3 | 0 | 1 | 1 | 0 |
| 7 Licenciamiento E3/E5/E7 | 20 | 14 | 4 | 1 | 1 | 0 | 0 |
| Afirmaciones de texto (todas las secciones) | 21 | 11 | 2 | 0 | 0 | 0 | 8 |
| Coherencia interna del borrador | 16 | 0 | 16 | 0 | 0 | 0 | 0 |
| **Total** | **255** | **148** | **87** | **3** | **8** | **1** | **8** |

### Correcciones de mayor impacto

1. **Licenciamiento vigente desde el 1-jul-2026.** E3 sumó Defender for Office 365 P1, Intune Plan 2, Remote Help y Advanced Analytics; E5 (y por lo tanto E7) sumó Security Copilot, Endpoint Privilege Management, Microsoft Cloud PKI y Enterprise Application Management. Precios de lista: E3 US$39, E5 US$60, E7 US$99 [L5], [L1].
2. **Entra Suite también es add-on sobre E3** (el borrador decía "No"): solo requiere Entra ID P1 [L6].
3. **Agent 365** está en disponibilidad general desde el 1-may-2026: incluido en E7, add-on de US$15 sobre E5 y **no elegible con E3 solo** (requiere además Defender Suite y Purview Suite) [L8], [L4].
4. **Security Copilot está incluido en E5 y E7**: 400 SCU por cada 1.000 licencias pagas por mes, hasta 10.000 [L1].
5. **Defender XDR no se limita a E5/E7**, y **Defender for Cloud Apps en E3 es solo Cloud App Discovery** [D2], [L4].
6. **Defender Threat Intelligence (MDTI)** se retiró como portal standalone el 1-ago-2026; la inteligencia quedó integrada en Defender XDR y Sentinel sin costo adicional [D11].
7. **Purview:** Data Security Investigations se factura solo por consumo; el nuevo DSPM está en disponibilidad general desde mayo de 2026; Data Estate Insights pasó a ser "Reports" en Unified Catalog; "Purview Data Security for AI" no es un nombre oficial [P5], [P3], [P7], [P8].
8. **Defender for Cloud:** la tabla duplicaba Defender CSPM y omitía Foundational CSPM; DevOps security y el cumplimiento regulatorio no son planes; Defender for Databases incluye Cosmos DB; la integración en el portal de Defender factura por DWU [A2], [A5], [A6], [A4].
9. **Azure:** Dedicated HSM está en retiro (sucesor: Azure Cloud HSM); Azure Migrate no es un servicio de seguridad; el private endpoint es parte de Private Link; Sentinel deja de tener soporte en el portal de Azure después del 31-mar-2027 [A16], [A27], [A15], [A9].
10. **SIEM en el portal de Defender:** ISOC en Microsoft Defender está en preview para E5/E7 y Defender Suite sin workspace de Sentinel activo; E5/E7 tienen además un beneficio de ingesta en Sentinel [D15], [D25].
11. **Windows:** nombres vigentes (Microsoft Defender Antivirus, Windows Firewall); Personal Data Encryption es cifrado por archivo vinculado a Windows Hello for Business; AppLocker ya no recibe mejoras; los certificados de Secure Boot de 2011 vencen desde junio de 2026; las baselines de oct-2026 habilitan Administrator protection [D16], [W13], [W14], [W12], [W15], [W16].
12. **Servicios:** FastTrack for Microsoft 365 (FastTrack for Azure se retiró), Microsoft Unified, Defender Experts Suite; "Microsoft Security Assessment" no es una oferta verificable y se eliminó [D19], [D20], [D18].
13. **Gartner Peer Insights:** los 38 mercados existen, pero Microsoft figura listado solo en 21; 4 mercados cambiaron de nombre o de estado, y varios listados usan un nombre distinto del comercial (secciones 4 y 5).

### Cómo leer este documento

- Las secciones 1 a 9 y la conclusión son el **catálogo corregido**, listo para usar. La columna **Val.** indica el resultado de la validación de cada fila y 🆕 marca lo agregado.
- Los códigos entre corchetes ([L5], [E2], [G20]…) remiten a las fuentes del **Anexo C**.
- El **Anexo A** registra cada afirmación del borrador con su veredicto, la corrección aplicada y la evidencia; el **Anexo B** reúne los cambios con fecha; el **Anexo D**, las discrepancias entre fuentes oficiales, el método y las limitaciones.

### Contenido

- 1. Inventario de tecnologías de seguridad Microsoft (Entra, Defender, Purview)
- 2. Microsoft Intune y seguridad integrada en Windows
- 3. Seguridad de Azure (Defender for Cloud y servicios de Azure)
- 4. Mercados de Gartner Peer Insights verificados
- 5. Correspondencia consolidada mercados Gartner → Microsoft
- 6. Servicios de seguridad ofrecidos por Microsoft
- 7. Diferencias entre Microsoft 365 E3, E5 y E7
- 8. Incorporación al AI CISO Atlas
- 9. Consideraciones para interpretar el catálogo
- Conclusión
- Anexo A — Registro de validación por afirmación
- Anexo B — Cambios, lanzamientos y retiros con fecha
- Anexo C — Fuentes
- Anexo D — Discrepancias, método y limitaciones

---

# 1. Inventario de tecnologías de seguridad Microsoft

> Columna **Val.**: ✅ confirmado · ⚠️ confirmado con matiz (texto corregido) · ❌ era incorrecto (corregido) · 🕒 desactualizado (renombre, retiro o cambio reciente; actualizado) · 🆕 agregado por omisión relevante. Las **Fuentes** remiten a los códigos del Anexo C.
>
> Convenciones de disponibilidad: **E3 / E5 / E7** = incluido en Microsoft 365 E3/E5/E7. **Add-on** = licencia adicional por usuario. **PAYG** = pago por uso facturado a una suscripción de Azure. Precios: lista en USD por usuario/mes con compromiso anual, vigentes desde el 1-jul-2026; varían por país, moneda y contrato.

## A. Microsoft Entra — Identidad y acceso

| # | Tecnología | Descripción | Disponibilidad validada (nov-2026) | Val. | Fuentes |
|---|---|---|---|---|---|
| 1 | Microsoft Entra ID | Directorio e identidad empresarial: autenticación, SSO y autorización | Edición Free con toda suscripción de Microsoft 365 o Azure; P1 en E3; P2 en E5/E7 | ✅ | [E3], [E2] |
| 2 | Entra ID P1 | Conditional Access, MFA y administración avanzada de identidad | E3/E5/E7 (en E5/E7, dentro de P2). Standalone US$7 | ✅ | [E2], [L5] |
| 3 | Entra ID P2 | P1 + ID Protection, PIM, entitlement management y access reviews básicos | E5/E7. Standalone US$10 | ✅ | [E3], [L5] |
| 4 | Conditional Access | Políticas adaptativas de acceso | P1 (E3 en adelante). La versión basada en riesgo requiere P2 (E5/E7) o Entra Suite | ✅ | [E3] |
| 5 | Entra ID Protection | Detección y respuesta ante riesgo de identidad | Completa con P2 (E5/E7) o Entra Suite; P1 incluye detecciones básicas | ✅ | [E3], [E2] |
| 6 | Privileged Identity Management (PIM) | Acceso privilegiado just-in-time, con aprobación y vencimiento, para roles de Entra, recursos de Azure y grupos | P2 (E5/E7) o ID Governance | ✅ | [E8], [E2] |
| 7 | Entra ID Governance | Ciclo de vida, revisiones y paquetes de acceso avanzados | Add-on US$7 (requiere P1; opción "Step Up" para clientes con P2). Incluido en Entra Suite y en E7 | ✅ | [E2], [E3] |
| 8 | Lifecycle Workflows | Automatización de altas, movimientos y bajas | Solo con ID Governance, Entra Suite o E7 | ✅ | [E2] |
| 9 | Entitlement Management | Paquetes de acceso, aprobaciones, vencimiento y segregación de funciones | Básico con P2 (E5/E7); avanzado con ID Governance, Entra Suite o E7; para agentes, Agent 365 | ⚠️ | [E2], [E3] |
| 10 | Access Reviews | Recertificación de accesos | Básicas con P2 (E5/E7); avanzadas (asistidas por ML, usuarios inactivos, PIM for Groups) con ID Governance o E7. Microsoft no agregará nuevas funciones IGA a P2 | ✅ | [E2] |
| 11 | Workload ID | Identidades de aplicaciones, servicios y cargas de trabajo | Free: managed identities y federación de identidades de workload. **Workload ID Premium**: US$3 por identidad/mes, SKU independiente no incluido en ningún suite (tampoco en E7). No es un servicio de Azure | ⚠️ | [E7], [E3] |
| 12 | Entra Agent ID | Identidad, registro y trazabilidad de agentes de IA | Plataforma disponible para todo cliente de Entra; Conditional Access, ID Protection, gobierno y controles de red **para agentes** requieren Agent 365 (incluido en E7) | ⚠️ | [E6], [E4], [L6] |
| 13 | Entra External ID | Identidad de clientes, socios y usuarios externos (CIAM) | PAYG por usuarios activos mensuales (MAU) con suscripción de Azure; los primeros 50.000 MAU sin cargo | ✅ | [E3] |
| 14 | Entra Verified ID | Credenciales verificables y prueba de identidad | Base incluida con P1/P2 (E3 en adelante). **Face Check** (premium): Entra Suite/E7 o pago por uso | ⚠️ | [E3], [E5], [L6] |
| 15 | Entra Internet Access | Secure Web Gateway centrado en identidad | El perfil de tráfico de Microsoft ("Internet Access for Microsoft services": red compatible, tenant restrictions, restauración de IP de origen) viene con P1/P2 (E3 en adelante). El SWG completo requiere Entra Suite (E7) o licencia standalone, sobre P1/P2 | ⚠️ | [E4], [L6] |
| 16 | Entra Private Access | Zero Trust Network Access para aplicaciones privadas | Entra Suite (E7) o standalone; requiere P1/P2 | ✅ | [E4] |
| 17 | Global Secure Access | Término unificador y consola de Internet Access y Private Access | Standalone "Microsoft Entra Global Secure Access" US$10; incluido en Entra Suite (E7) | ✅ | [E4], [E3] |
| 18 | Microsoft Authenticator | MFA y autenticación passwordless | MFA desde Entra ID Free; passwordless y autenticación resistente a phishing figuran en P1 | ✅ | [E3] |
| 19 | Windows Hello for Business | Autenticación passwordless resistente a phishing (clave asimétrica protegida por TPM) | Windows (desde Pro) con Entra; incluido en E3/E5/E7 | ✅ | [L4], [W9] |
| 20 | **Microsoft Entra Suite** | Private Access, Internet Access, ID Governance, ID Protection y Verified ID premium (Face Check) | Add-on US$12 sobre E3 o E5 (requiere P1; precio especial para clientes P2/E5). Incluido en E7 | 🆕 | [L6], [E9], [L1] |

**Cambios respecto del borrador**

- Workload ID, Agent ID, Verified ID, Internet Access y Entitlement Management: se corrigió la disponibilidad (filas 9, 11, 12, 14 y 15).
- Se agregó Microsoft Entra Suite como entidad de licencia (fila 20).
- **Entra Permissions Management (CIEM)** no debe figurar como vigente: fin de venta el 1-abr-2025 y retiro el 1-oct-2025 [E10]. Si el Atlas modela CIEM, hoy esa capacidad vive en Defender CSPM (sección 3.A).
- Fuentes del borrador: el hub de Entra [E1] sí respalda que Entra ID, Agent ID, ID Protection, ID Governance, External ID, Internet Access, Private Access, Verified ID y Workload ID son productos diferenciados. La segunda URL [E9] existe, pero solo describe escenarios de **Entra Suite** (no menciona Agent ID, External ID ni Workload ID); se reemplaza por [E2] como fuente de licenciamiento.

## B. Microsoft Defender — Protección y operaciones

| # | Tecnología | Descripción | Disponibilidad validada (nov-2026) | Val. | Fuentes |
|---|---|---|---|---|---|
| 1 | Microsoft Defender XDR | Correlación de incidentes entre endpoint, identidad, correo, aplicaciones y nube en el portal unificado de Defender | Sin costo adicional con cualquier licencia Defender calificada: E5/E7, E3 + Defender Suite, E3 + EMS E5, MDE, MDI, Defender for Cloud Apps o Cloud App Discovery, MDO P2, Business Premium, Defender for Business, entre otras. Las señales dependen de las cargas licenciadas; la interrupción automática de ataques y Threat analytics requieren MDE P2 | ⚠️ | [D2] |
| 2 | Defender for Endpoint P1 | Antimalware de nueva generación, reducción de superficie de ataque, control de dispositivos, firewall y control de aplicaciones | E3 (también A3/G3) o standalone. Cubre hasta 5 dispositivos por usuario; servidores se licencian aparte | ✅ | [D3], [L6], [D23] |
| 3 | Defender for Endpoint P2 | P1 + EDR, investigación y remediación automatizadas, Threat analytics | E5/E7, Windows Enterprise E5, Defender Suite o standalone | ✅ | [D3] |
| 4 | Microsoft Defender Antivirus | Antimalware integrado; componente de protección de nueva generación de MDE | Integrado en Windows 10/11 y Windows Server | ✅ | [D16] |
| 5 | Defender Vulnerability Management | Evaluación y priorización de vulnerabilidades | **Core** incluido en MDE P2 (E5/E7). **Premium**: add-on sobre MDE P2/E5/Defender Suite. **Standalone** (core + premium) para clientes con MDE P1/E3 u otro EDR. Para servidores, las capacidades premium vienen en Defender for Servers P2 | ⚠️ | [D7], [D3] |
| 6 | Defender for Office 365 P1 | Protección avanzada de correo y colaboración (vínculos y adjuntos seguros, anti-phishing) | **Incluido en Microsoft 365 E3 y Office 365 E3 desde el 1-jul-2026**; también Business Premium y standalone. Sin integración con Defender XDR | ✅ 🕒 | [D4], [L5], [L2] |
| 7 | Defender for Office 365 P2 | P1 + Explorer, investigación y respuesta automatizadas, rastreadores de amenazas y Attack simulation training | E5/E7, Office 365 E5, Defender Suite o standalone | ✅ | [D3], [D4] |
| 8 | Attack simulation training | Simulaciones de phishing y capacitación | Requiere E5 o MDO P2 (E3 solo tiene un subconjunto de prueba) | 🆕 | [D6] |
| 9 | Seguridad integrada para buzones en la nube (antes Exchange Online Protection, EOP) | Antimalware, antispam y anti-phishing/anti-spoofing | Incluida en todo buzón de Exchange Online; add-on para buzones on-premises | 🕒 | [D5] |
| 10 | Defender for Identity | Detección de ataques a identidades híbridas | E5/E7, EMS E5, Defender Suite o standalone | ✅ | [D3] |
| 11 | Defender for Cloud Apps | Seguridad de SaaS: CASB, descubrimiento, postura, gobierno de aplicaciones e IA generativa | Completo en E5/E7, EMS E5, Defender Suite y Purview Suite; **E3 solo incluye Cloud App Discovery** (shadow IT). El control de sesión con Conditional Access requiere Entra ID P1 | ✅ | [D3], [L4] |
| 12 | Defender for IoT | Visibilidad y protección de dispositivos OT/IoT | **OT**: licencia por sitio en el Microsoft 365 admin center (los planes heredados de Azure deben migrarse). **Enterprise IoT**: incluido en E5/E7 y E5 Security/Defender Suite (5 dispositivos por licencia) | ⚠️ | [D8], [L1] |
| 13 | Microsoft Security Exposure Management | Gestión unificada de exposición, rutas de ataque e iniciativas | Sin licencia propia: incluido con E5/E7, E3 con add-ons o Defender Suite. Los conectores de datos externos tienen precio por consumo. Solo nube pública | ⚠️ | [D9] |
| 14 | Defender External Attack Surface Management (EASM) | Descubrimiento de activos expuestos a Internet | Recurso de Azure facturado por activo (prueba de 30 días). Exposure Management ofrece además una iniciativa EASM con huella predefinida | ✅ | [D10], [D21] |
| 15 | **Inteligencia de amenazas de Microsoft en Defender** (antes Defender Threat Intelligence, MDTI) | Intel explorer, Threat analytics, perfiles de actores e indicadores | El portal standalone de MDTI se **retiró el 1-ago-2026**; la inteligencia se integró en Defender XDR y Sentinel sin costo adicional | 🕒 | [D11] |
| 16 | Microsoft Security Copilot | IA generativa y agentes para operaciones de seguridad en Defender, Entra, Intune, Purview y Sentinel | Incluido en E5/E7: **400 SCU por cada 1.000 licencias pagas por mes, hasta 10.000 SCU/mes**. Sin E5/E7: SCU aprovisionadas por hora más overage | ⚠️ | [L1], [L6], [D12] |
| 17 | **ISOC en Microsoft Defender** (preview) | XDR + SIEM + inteligencia de amenazas + automatización en el portal de Defender | Preview para clientes con Defender Suite, E5 o E7 **sin workspace de Sentinel activo**; incluye 30 días de retención de datos de Defender; la ingesta adicional puede tener costo y el workspace requiere suscripción de Azure | 🆕 | [D15], [L6] |
| 18 | **Microsoft Defender Suite** (antes Microsoft 365 E5 Security) | Add-on de protección XDR por capas para clientes E3 | US$12; requiere Microsoft 365 E3 (u Office 365 E3 + EMS E3). Incluye MDE P2, MDO P2, MDI y Defender for Cloud Apps según la service description; confirmar la composición completa en Product Terms | 🆕 | [L6], [D3], [L5] |
| 19 | **Microsoft Defender for Business** | Variante de MDE para pymes (hasta 300 usuarios) | Incluido en Business Premium; habilita el portal de Defender | 🆕 | [D3], [D2] |
| — | Servicios Defender Experts | MDR, Hunting, Servers, Threat Intelligence e Incident Response | Se tratan como servicios en la **sección 6** | — | [D13] |

**Cambios respecto del borrador**

- Defender XDR no está limitado a E5/E7 (fila 1). MDO P1 forma parte de E3 desde el 1-jul-2026 (fila 6).
- EOP pasó a documentarse como "seguridad integrada para buzones en la nube" (fila 9). MDTI dejó de existir como producto standalone (fila 15).
- Se agregaron Attack simulation training, ISOC en Defender (preview), Defender Suite y Defender for Business (filas 8, 17, 18 y 19).
- Las filas de Defender Experts se trasladaron a la sección 6 para separar productos de servicios.
- Fuentes del borrador: el hub [D1] respalda la diferenciación entre Defender XDR, MDE, MDO, MDI, Defender for Cloud Apps, MDVM, Defender for IoT y Sentinel. El overview de Defender Experts [D13] no respalda esa frase; se usa solo para los servicios.

## C. Microsoft Purview — Seguridad, gobierno y cumplimiento de datos

| # | Tecnología | Descripción | Disponibilidad validada (nov-2026) | Val. | Fuentes |
|---|---|---|---|---|---|
| 1 | Purview Information Protection | Clasificación, etiquetado y cifrado | **E3 ("Plan 1")**: etiquetado manual, por defecto y obligatorio; cifrado por etiqueta; cifrado de correo básico. **E5/E7 ("Plan 2") o add-on** (Purview Suite, E5 Information Protection & Governance): etiquetado automático, Content/Activity Explorer, cifrado avanzado de correo, Customer Key y Double Key Encryption. Fuentes fuera de Microsoft 365: PAYG | ⚠️ | [L12], [P1], [P2], [L4] |
| 2 | Etiquetas de sensibilidad | Etiquetado y protección por etiqueta | E3 en adelante para etiquetado manual, por defecto y obligatorio; funciones avanzadas en E5/E7 o add-on | ✅ | [L12], [P1] |
| 3 | Etiquetado automático | Clasificación y etiquetado automatizados | E5/E7, Purview Suite, E5 IP&G u Office 365 E5 (EMS E5 solo del lado del cliente). Activos fuera de Microsoft 365: PAYG | ✅ | [P1], [P2] |
| 4 | Purview Data Loss Prevention | Prevención de fuga de información | **E3: correo y archivos** (Exchange, SharePoint, OneDrive). **E5/E7 o add-on**: Teams, Endpoint DLP y controles para Copilot. DLP de red y de navegador hacia apps no gestionadas: licencia de nivel E5 + PAYG | ⚠️ | [P1], [L2], [P12] |
| 5 | Endpoint DLP | Protección de información en dispositivos Windows 10/11 y macOS | E5/E7, Purview Suite o E5 IP&G (no incluido en Office 365 E5) | ✅ | [P1] |
| 6 | Data Security Posture Management (DSPM) | Visibilidad y evaluación de exposición de datos, incluida la IA | La **nueva versión es GA desde mayo de 2026** y unifica DSPM y DSPM for AI (ambos pasan a "classic"). Requiere licencia de soporte (la versión classic exigía E5 o Purview Suite). Apps de IA fuera de Microsoft 365, insights proactivos y Security Copilot se cobran por consumo; los conectores de terceros siguen en preview | ⚠️ | [P3], [P4] |
| 7 | Data Security Investigations (DSI) | Investigación de incidentes de datos con IA | **No se licencia por usuario**: se factura solo por consumo (almacenamiento por GB/mes + unidades de cómputo de IA). Requiere suscripción y grupo de recursos de Azure en el mismo tenant | ❌ | [P5], [P20] |
| 8 | Insider Risk Management | Detección e investigación de riesgos internos | E5/E7, Purview Suite o E5 Insider Risk Management. Indicadores de fuentes no Microsoft 365 y de IA: PAYG. Forensic evidence: add-on de capacidad | ✅ | [L12], [P2] |
| 9 | Information Barriers | Restricción de comunicación y colaboración entre segmentos | E5/E7, Purview Suite o E5 Insider Risk Management | ✅ | [L12] |
| 10 | Communication Compliance | Supervisión de comunicaciones según políticas | E5/E7, Office 365 E5, Purview Suite o E5 IRM. El análisis de prompts y respuestas de Copilot requiere además licencia de Copilot. IA fuera de Microsoft 365: PAYG | ✅ | [P1], [P2] |
| 11 | Audit (Standard) | Registro y búsqueda de actividades | E3 en adelante; retención de 180 días | ✅ | [P1], [P9] |
| 12 | Audit (Premium) | Auditoría avanzada y retención ampliada | E5/E7, Office 365 E5, Purview Suite o E5 eDiscovery & Audit; retención de 1 año, hasta 10 años con add-on por usuario | ✅ | [P1], [P9], [L9] |
| 13 | eDiscovery | Preservación, búsqueda y producción de evidencia electrónica | **Standard**: E3 en adelante. **Premium** (custodios, conjuntos de revisión, analítica): E5/E7, Office 365 E5, Purview Suite o E5 eDiscovery & Audit. Experiencia unificada en el portal de Purview (Content Search integrado) | ⚠️ | [P1], [P10] |
| 14 | Data Lifecycle Management | Retención y eliminación de información | E3: políticas de retención a nivel organización o ubicación y etiquetas manuales. E5/E7 o add-on: ámbitos adaptativos y aplicación automática de etiquetas | ✅ | [L12], [P1] |
| 15 | Records Management | Registros, retención por eventos y revisión de disposición | E5/E7, Purview Suite, E5 IP&G u Office 365 E5 | ✅ | [P1] |
| 16 | Compliance Manager | Evaluación y seguimiento de controles regulatorios | Todos los planes incluyen la plantilla Data Protection Baseline; E5/A5/G5 suman 3 plantillas premium; el resto (incluidas las de IA: EU AI Act, ISO 42001, NIST AI RMF) se compra por plantilla | ✅ | [P11] |
| 17 | Data Map | Inventario y metadatos de datos | En el modelo vigente, el escaneo no tiene cargo para clientes de Unified Catalog que aceptaron el nuevo modelo; Capacity Units y vCore-hora corresponden a Azure Purview (Classic). Facturación vía suscripción de Azure | ⚠️ | [P6], [P12] |
| 18 | Unified Catalog | Catálogo, productos de datos y calidad de datos | PAYG: activos gobernados únicos por día + unidades de procesamiento de gobierno de datos (DGPU) | ✅ | [P6] |
| 19 | **Reports** en Unified Catalog > Health management (antes Data Estate Insights) | Análisis del patrimonio y de la salud de los datos | Data Estate Insights fue renombrado y movido; la versión clásica no acepta clientes nuevos | 🕒 | [P7], [P19] |
| 20 | **Protecciones de Purview para IA generativa** (Copilot, agentes y apps de IA) — antes listado como "Purview Data Security for AI", que no es un nombre oficial | DSPM como punto de entrada; DLP, auditoría, retención y eDiscovery sobre interacciones con IA | Copilot: cubierto por licencias por usuario (algunas funciones requieren E5). Agentes en Foundry y apps conectadas a Entra: E7 y Agent 365. Apps de IA fuera de Microsoft 365: PAYG | ⚠️ | [P8], [P1], [P2] |
| 21 | Customer Key | Cifrado en reposo con claves del cliente | E5/E7, Purview Suite, E5 IP&G u Office 365 E5 | 🆕 | [P1] |
| 22 | Double Key Encryption | Protección con dos claves para contenido altamente sensible (no accesible para Copilot) | E5/E7, Purview Suite, E5 IP&G o EMS E5 | 🆕 | [P1], [P18] |
| 23 | Message Encryption (básico y avanzado) | Cifrado de correo | Básico en E3 en adelante; avanzado en E5/E7 o add-on | 🆕 | [L12], [P1] |
| 24 | Customer Lockbox | Aprobación del acceso de ingenieros de Microsoft al contenido | E5/E7, Office 365 E5, Purview Suite o E5 IRM | 🆕 | [P1] |
| 25 | Adaptive Protection | Controles dinámicos de DLP y Conditional Access según el nivel de riesgo interno | Capacidad de Insider Risk Management | 🆕 | [P17] |
| 26 | Privileged Access Management (Purview) | Aprobación just-in-time de tareas administrativas en Microsoft 365 | E5/E7, Purview Suite o E5 IRM | 🆕 | [L12], [P14] |
| 27 | Network Data Security (DLP de red) | DLP sobre tráfico de red integrado con Global Secure Access | GA en sep-2026; licencia de nivel E5 + PAYG | 🆕 | [P3], [P1] |
| 28 | Microsoft Priva Privacy Risk Management | Gestión de riesgos de privacidad | Add-on sobre Microsoft 365/Office 365 E3/E5. Priva Subject Rights Requests ya no figura en la service description de Priva y su página en Learn redirige a eDiscovery | 🆕 | [P16], [P10] |
| 29 | **Microsoft Purview Suite** (antes Microsoft 365 E5 Compliance) | Add-on de seguridad y cumplimiento de datos para clientes E3 | US$12; requiere Microsoft 365 E3 (u Office 365 E3 + EMS E3) | 🆕 | [L6], [L5] |

**Cambios respecto del borrador**

- Information Protection, DLP y eDiscovery tienen alcance distinto en E3 y en E5/E7: se separaron los niveles (filas 1, 4 y 13).
- DSI es solo de consumo (fila 7, era incorrecto). DSPM es GA en su nueva versión (fila 6). Data Estate Insights pasó a ser "Reports" en Unified Catalog (fila 19).
- "Purview Data Security for AI" no es un nombre oficial; se reemplazó por el nombre de la documentación (fila 20).
- Se agregaron 9 capacidades y la entidad de licencia Purview Suite (filas 21 a 29).
- La nota del borrador ("Purview es una familia… no todo está en E5") es correcta, pero las tres URLs citadas [P13], [P14] y [P15] solo respaldan la estructura de familia. Lo que no está en E5 lo respaldan la página de modelos de facturación [P2] y la Licensing Guidance [L12]: el pago por uso cubre datos y apps fuera de Microsoft 365 y se factura en Azure. La página general [P15] todavía marca DSPM como preview, en contradicción con [P3].

---

# 2. Microsoft Intune y seguridad integrada en Windows

Un inventario limitado a los productos Defender omitiría controles de endpoint fundamentales. Esta sección se corrigió en dos puntos estructurales: el **empaquetado de Microsoft 365 vigente desde el 1-jul-2026**, que incorporó gran parte de las capacidades de Intune Suite a E3/E5/E7, y los **requisitos por edición de Windows 11**.

## A. Microsoft Intune

| # | Tecnología | Descripción | Inclusión validada (desde jul-2026) | Val. | Fuentes |
|---|---|---|---|---|---|
| 1 | Intune Plan 1 | Servicio base de gestión unificada de dispositivos y aplicaciones (MDM/MAM) | E3/E5/E7; standalone US$8 | ✅ | [W1], [W3] |
| 2 | **Intune Plan 2** | Microsoft Tunnel for MAM, gestión de dispositivos especializados y compartidos, actualizaciones de firmware over-the-air | **E3/E5/E7** (desde jul-2026); add-on US$4. Sus componentes no se venden por separado | 🆕 | [W3], [L5], [L6] |
| 3 | Intune Suite | Paquete de capacidades avanzadas de gestión y seguridad; incluye Plan 2 | Add-on US$10 sobre Plan 1. Desde jul-2026 la mayoría de sus componentes ya vienen en E3/E5/E7 | ⚠️ | [W1], [W3] |
| 4 | Endpoint Privilege Management | Elevación controlada para usuarios estándar con mínimo privilegio | **E5/E7** según la nota oficial de licenciamiento y la FAQ de precios de Intune; add-on US$3. La página de producto de E3 también lo menciona: discrepancia a confirmar (Anexo D) | ✅ ⚠️ | [L5], [W3], [L2] |
| 5 | Enterprise Application Management | Catálogo de aplicaciones Win32 empaquetadas y hospedadas por Microsoft para desplegarlas y actualizarlas | E5/E7; add-on US$2 | ⚠️ | [W2], [L5] |
| 6 | Advanced Analytics | Analítica avanzada de endpoints y de experiencia de usuario, con detección de anomalías | E3/E5/E7; add-on US$5 | ✅ | [W2], [L5] |
| 7 | Remote Help | Asistencia remota en la nube con control de acceso basado en roles | E3/E5/E7; add-on US$3,50 | ✅ | [W2], [L5] |
| 8 | **Microsoft Cloud PKI** (antes listado como "Intune Cloud PKI") | Autoridad de certificación administrada para dispositivos gestionados por Intune | E5/E7; add-on US$2 | ⚠️ | [W2], [L5] |
| 9 | Políticas de protección de aplicaciones (MAM) | Protección de datos en apps, con o sin inscripción del dispositivo | Plan 1 (Tunnel for MAM es Plan 2) | ✅ | [W5] |
| 10 | Políticas de cumplimiento | Evaluación de cumplimiento de dispositivos; alimentan Conditional Access | Plan 1 | ✅ | [W6] |
| 11 | Políticas de seguridad de endpoint | Antivirus, firewall, cifrado de disco, reglas ASR, EDR, App Control for Business y protección de cuentas (LAPS) | Plan 1 | ⚠️ | [W4] |
| 12 | Windows Autopilot | Aprovisionamiento, restablecimiento y reasignación de dispositivos | La inscripción automática en MDM requiere Entra ID P1/P2 | ✅ | [W7] |
| 13 | Windows Autopatch | Gestión automatizada de actualizaciones (incluye Hotpatch) | Windows Enterprise E3/E5 (incluido en Microsoft 365 E3/E5/E7 y F3), Business Premium, Education A3/A5; requiere Entra ID P1/P2 e Intune | ✅ | [W8] |

**Precisiones**

- Las capacidades avanzadas de Intune requieren Intune Plan 1 o un plan que lo incluya; E3 y E5 cubren hasta 15 dispositivos inscritos por usuario [L6].
- Gartner Peer Insights: Microsoft Intune **figura listado** en el mercado *Endpoint Management Tools* [G6]. Se reemplaza la palabra "reconocido" para no sugerir un premio.

## B. Seguridad integrada en Windows 11 (requisitos por edición y licencia)

El borrador titulaba esta tabla "Windows Enterprise", pero la mayoría de estas funciones también existen en Windows Pro; algunas requieren licencia Enterprise/Education [W9]. La tabla asume **Windows 11**: Windows 10 dejó de tener soporte el 14-oct-2025 [W19].

| # | Tecnología | Función | Edición / licencia | Por defecto | Val. | Fuentes |
|---|---|---|---|---|---|---|
| 1 | BitLocker | Cifrado de volúmenes completos | Desde Pro; la gestión avanzada requiere Enterprise/Education | — | ✅ | [W9] |
| 2 | BitLocker To Go | Cifrado de unidades extraíbles | Parte de BitLocker | — | ✅ | [W9] |
| 3 | **Microsoft Defender Antivirus** (antes "Windows Defender Antivirus") | Protección antimalware de nueva generación | Todas las ediciones | Sí | 🕒 | [D16] |
| 4 | **Windows Firewall** (el servicio aún figura como "Windows Defender Firewall") | Firewall de host con estado y soporte de IPsec | Todas las ediciones | Sí | 🕒 | [W13] |
| 5 | Microsoft Defender SmartScreen | Protección contra sitios, descargas y apps maliciosas o de phishing (no cubre recursos internos/UNC) | Incluido en Windows | — | ✅ | [W31] |
| 6 | Windows Hello for Business | Autenticación passwordless resistente a phishing | Desde Pro | — | ✅ | [W9] |
| 7 | Credential Guard | Aislamiento de secretos con VBS | **Enterprise/Education** (no Pro) | Sí, desde Windows 11 22H2 en equipos que cumplen los requisitos | ✅ | [W20], [W11] |
| 8 | Remote Credential Guard | Protege credenciales en sesiones RDP con Kerberos | Desde Pro | — | ✅ | [W9] |
| 9 | Virtualization-Based Security (VBS) | Entorno aislado por hipervisor que aloja funciones de seguridad (p. ej., Credential Guard, integridad de memoria) | Requiere hardware compatible (CPU de 64 bits con virtualización y SLAT, IOMMU, TPM 2.0 y Secure Boot) | — | ✅ | [W32] |
| 10 | Integridad de memoria (HVCI) | Integridad de código en modo kernel dentro de VBS | Hardware compatible | — | ✅ | [W29] |
| 11 | App Control for Business (antes WDAC) | Control de ejecución de aplicaciones y drivers | Todas las ediciones cliente | — | ✅ | [W12] |
| 12 | AppLocker | Restricción de aplicaciones por usuario o grupo | Licencia Enterprise/Education. Microsoft recomienda App Control for Business: AppLocker no cumple los criterios de servicio de MSRC como función de seguridad y ya no recibe mejoras | — | ⚠️ | [W12], [W9] |
| 13 | Reglas de reducción de superficie de ataque (ASR) | Bloqueo de comportamientos que explota el malware | Cualquier edición con Microsoft Defender Antivirus activo; reportes y analítica avanzados en Defender XDR requieren E5 o equivalente | — | ✅ | [W21] |
| 14 | Controlled Folder Access | Protección anti-ransomware de carpetas | Requiere Microsoft Defender Antivirus activo | No | ✅ | [W30] |
| 15 | Secure Boot | Protección de la cadena de arranque | Hardware UEFI. **Los certificados de 2011 empiezan a vencer en junio de 2026**: hay que desplegar los certificados de 2023 para seguir recibiendo protecciones de arranque | — | ⚠️ | [W15] |
| 16 | Trusted Platform Module (TPM) | Protección de claves, medición del arranque y atestación | Hardware | — | ✅ | [W33] |
| 17 | Microsoft Pluton | Procesador de seguridad integrado en la CPU que puede actuar como TPM | Windows 11 en chipsets compatibles | — | ✅ | [W28] |
| 18 | Windows LAPS | Rotación y respaldo de la contraseña de administrador local en Entra ID o AD | Incluido en Windows sin costo adicional; el LAPS heredado está deprecado desde Windows 11 23H2 | — | ✅ | [W19] |
| 19 | Windows Sandbox | Entorno de escritorio aislado y desechable | Pro, Enterprise y Education (no Home) | — | ✅ | [W22] |
| 20 | Security baselines | Configuraciones recomendadas por Microsoft (GPO con Security Compliance Toolkit o baselines MDM de Intune) | — | Desde oct-2026 habilitan Administrator protection (fila 23) | ✅ | [W34], [W16] |
| 21 | Personal Data Encryption | **Cifrado a nivel de archivo vinculado a Windows Hello for Business** (no es protección de "datos personales") | Enterprise/Education, Windows 11 22H2 o posterior | — | ⚠️ | [W14] |
| 22 | Protección de LSA | Ejecuta LSASS como proceso protegido | Incluida en Windows | Sí, en instalaciones nuevas de 22H2 o posterior, unidas a la empresa y con capacidad HVCI | ✅ | [W17] |
| 23 | Administrator protection | Elevación just-in-time con token aislado y verificación con Windows Hello | Windows 11 | Se habilita por defecto con las security baselines desde la actualización de oct-2026. Learn indica no habilitarlo en equipos gestionados con LAPS | 🆕 | [W16] |
| 24 | Smart App Control | Control de ejecución basado en reputación | Todas las ediciones | Se apaga en equipos gestionados salvo activación previa | 🆕 | [W23], [W9] |
| 25 | Enhanced Sign-in Security (Windows Hello) | Aísla con VBS y TPM los datos biométricos y el canal de autenticación | Hardware compatible | Sí, en Copilot+ PC | 🆕 | [W24] |
| 26 | Kernel DMA Protection | Protege contra ataques DMA por puertos externos | Pro/Enterprise/Education con soporte de firmware | Sí, en sistemas compatibles | 🆕 | [W25] |
| 27 | Secured-core PC configuration lock | Revierte la deriva de configuración de funciones secured-core | Windows 11 vía MDM | No | 🆕 | [W26] |
| 28 | Hotpatch | Actualizaciones de seguridad mensuales sin reinicio | Windows 11 24H2 o posterior con VBS, vía Windows Autopatch; licencias Enterprise E3/E5, Microsoft 365 F3, Education A3/A5, Business Premium o Windows 365 Enterprise | — | 🆕 | [W18] |
| 29 | Quick machine recovery | Recuperación automática ante fallas de arranque masivas | Windows 11; Windows E3 lo recibe en el empaquetado 2026 | En equipos gestionados, la remediación en la nube está desactivada por defecto | 🆕 | [W27], [L5] |

**Otras funciones con página oficial** (incluir si el Atlas busca exhaustividad): Tamper protection, Exploit protection, lista de bloqueo de drivers vulnerables, passkeys, Windows protected print, Device health attestation y Zero Trust DNS (solo Enterprise/Education) [W9].

**Nota del borrador validada:** "no todas son exclusivas de Windows Enterprise ni están habilitadas automáticamente" es correcta [W9]. Las tres URLs citadas [W11], [W10] y [W12] existen.

---

# 3. Seguridad de Azure

## A. Microsoft Defender for Cloud

Defender for Cloud **es una CNAPP** (la categoría paraguas, no un componente) que unifica tres componentes —**CSPM, DevSecOps y CWPP**— y agrega seguridad para cargas de IA generativa [A1]. Se factura por consumo en Azure y no forma parte de E3/E5/E7 [A3].

| # | Plan o capacidad | Alcance protegido | Modelo | Val. | Fuentes |
|---|---|---|---|---|---|
| 1 | **Foundational CSPM** (reemplaza la fila duplicada "Defender Cloud Security Posture Management") | Recomendaciones, Secure Score, Microsoft cloud security benchmark e inventario en Azure, AWS y GCP; DevOps security básico | Sin costo | ❌ | [A2], [A3] |
| 2 | Defender CSPM | Rutas de ataque, cloud security explorer, escaneo sin agente, DSPM, postura de IA, postura de APIs, gestión de permisos (CIEM), EASM, gobernanza y cumplimiento regulatorio | Por recurso facturable | ✅ | [A2] |
| 3 | Defender for Servers Plan 1 | EDR de servidores (integración con MDE) en Azure, AWS, GCP y on-premises | Consumo en Azure. Desde el 1-nov-2026 los dispositivos de escritorio dejan de facturarse en P1 | ✅ | [A4], [A3] |
| 4 | Defender for Servers Plan 2 | P1 + escaneo sin agente, MDVM premium, monitoreo de integridad de archivos, acceso JIT a VM y alertas DNS | Consumo en Azure | ✅ | [A4], [A36] |
| 5 | Defender for Containers | Endurecimiento, evaluación de vulnerabilidades y protección en runtime para AKS, EKS, GKE, Kubernetes con Arc y registros | Consumo en Azure; reemplaza los planes heredados de Kubernetes y Container Registries (deprecados) | ✅ | [A1], [A4] |
| 6 | Defender for Storage | Blobs, Azure Files y ADLS Gen2; Malware Scanning como complemento con cargo propio | Consumo en Azure; Malware Scanning con cargo propio | ✅ | [A3] |
| 7 | **Defender for Databases** (nombre paraguas; "Defender for SQL" es un plan dentro) | Azure SQL, SQL Server en máquinas, bases relacionales open source (PostgreSQL y MySQL flexibles; AWS RDS GA desde 1-jun-2026) y **Azure Cosmos DB** | Consumo en Azure (Cosmos DB por RU). Las APIs clásicas de Defender for SQL se retiran el 16-ago-2027 | ⚠️ | [A1], [A4], [A3] |
| 8 | Defender for App Service | Ataques contra aplicaciones en App Service | Consumo en Azure | ✅ | [A1] |
| 9 | Defender for Key Vault | Accesos anómalos a Key Vault | Precio fijo por vault (el modelo heredado por transacción está deprecado) | ✅ | [A1], [A4] |
| 10 | Defender for Resource Manager | Operaciones de administración sospechosas | Precio fijo por suscripción | ✅ | [A1], [A4] |
| 11 | Defender for APIs | APIs publicadas en Azure API Management; la postura de APIs vive en Defender CSPM | Planes 1 a 5 en la página de precios. Sin retiro anunciado | ✅ | [A7], [A4], [A3] |
| 12 | Defender for AI Services | Detección en tiempo real para apps de IA generativa (Azure OpenAI, inferencia de modelos), integrada con Prompt Shields y Defender XDR | GA; por tokens | ✅ | [A8] |
| 13 | **DevOps security** (antes "Defender for DevOps") | Azure DevOps, GitHub y GitLab: hallazgos de código, anotaciones de PR, mapeo código-nube | No es un plan con precio propio: básico en Foundational CSPM, avanzado en Defender CSPM | ⚠️ | [A5], [A2] |
| 14 | **Cumplimiento regulatorio** (capacidad, no plan) | Microsoft cloud security benchmark por defecto; otros estándares (ISO 27001, PCI DSS, NIS2, DORA, EU AI Act, etc.) | Asignar estándares adicionales requiere un plan pago, excepto Servers P1 o APIs P1 | ⚠️ | [A6], [A2] |
| 15 | Defender for DNS | Alertas DNS | Incluido en Servers P2; el plan independiente no puede habilitarse en altas nuevas desde el 5-jul-2026 | 🆕 🕒 | [A36], [A4] |
| 16 | **Defender for Cloud en el portal de Defender** | Postura de nube unificada con Exposure Management | Integración GA desde el 5-may-2026; la gestión de planes en el portal de Defender (preview desde el 20-oct-2026) factura por Defender Workload Units (DWU) | 🆕 | [A26], [A4] |

**Precisiones**

- La frase del borrador sobre la documentación enumera bien servidores, contenedores, bases de datos, almacenamiento, App Service, Key Vault, Resource Manager e IA, pero **omite APIs** (que sí figura en la introducción y en el módulo de entrenamiento citado [A34]). Además, DevOps es una capacidad de CSPM, no un plan de protección de cargas [A35].
- Defender Experts for Servers (MDR para servidores) se trata en la sección 6 y requiere Defender for Servers P1 o P2.

## B. Azure — Servicios de seguridad y capacidades de plataforma

La tabla del borrador mezclaba servicios de seguridad dedicados con capacidades de plataforma que cumplen funciones de seguridad. Se reorganizó en cuatro grupos, siguiendo el catálogo oficial *Security services and technologies in Azure* [A18].

### B.1 Servicios de seguridad dedicados

| # | Servicio | Función | Precisiones validadas | Val. | Fuentes |
|---|---|---|---|---|---|
| 1 | Microsoft Sentinel | SIEM nativo de la nube | Opera en el portal de Defender; **sin soporte en el portal de Azure después del 31-mar-2027** (antes 1-jul-2026). Incluye **Sentinel data lake** (retención de hasta 12 años) además del nivel analytics. Beneficio para E5/E7: ingesta sin costo de hasta 5 MB por usuario/día de datos de Microsoft 365 | ✅ | [A9], [A30], [A10], [D25] |
| 2 | **Automatización de Sentinel** (antes "Sentinel SOAR") | Reglas de automatización y playbooks basados en Azure Logic Apps | No es un producto ni un SKU separado | ⚠️ | [A9] |
| 3 | Azure Firewall | Firewall de red administrado, con estado, L3–L7 | Tres SKU: Basic, Standard y Premium | ✅ | [A11] |
| 4 | Azure Firewall Premium (SKU de Azure Firewall) | Inspección TLS saliente, IDPS y filtrado por URL | Es un SKU, no un servicio separado | ✅ | [A11] |
| 5 | Azure Firewall Manager | Gestión central de políticas de Firewall, WAF y DDoS | — | 🆕 | [A23] |
| 6 | Azure Web Application Firewall | Protección de aplicaciones web (OWASP, bots) | Se despliega con Application Gateway, Application Gateway for Containers, Front Door y CDN (preview) | ✅ | [A13] |
| 7 | Azure DDoS Protection | Mitigación de DDoS | Niveles DDoS Network Protection y DDoS IP Protection; la protección básica de infraestructura no tiene costo | ✅ | [A12] |
| 8 | Azure Key Vault | Claves, secretos y certificados | Niveles Standard y Premium (claves en HSM) | ✅ | [A33], [A14] |
| 9 | Azure Key Vault Managed HSM | HSM administrado de un solo inquilino, FIPS 140-3 nivel 3; solo claves | — | ✅ | [A14] |
| 10 | **Azure Cloud HSM** (reemplaza a Azure Dedicated HSM) | HSM de un solo inquilino, FIPS 140-3 nivel 3, IaaS | Sucesor GA de Dedicated HSM | 🕒 | [A16], [A17] |
| 11 | Azure Payment HSM | HSM para procesamiento de pagos (PCI PIN, PCI 3DS) | Relevante para el sector financiero | 🆕 | [A14] |
| 12 | Azure Bastion | Acceso RDP/SSH sobre TLS sin IP pública en las VM | SKU Developer, Basic, Standard y Premium | ✅ | [A37] |
| 13 | Azure Confidential Computing | Protección de datos en uso con entornos de ejecución de confianza | Familia de ofertas (VM y contenedores confidenciales), no un servicio único | ✅ | [A38] |
| 14 | Azure Attestation | Verificación remota de la integridad de plataformas y binarios | — | ✅ | [A39] |
| 15 | Azure Confidential Ledger | Registro de solo anexado y evidencia de manipulación | — | ✅ | [A40] |
| 16 | Network Security Perimeter | Perímetro lógico para servicios PaaS contra la exfiltración | GA en regiones públicas | 🆕 | [A22] |
| 17 | Prompt Shields (Azure AI Content Safety) | Detección de ataques de prompt directos e indirectos en apps de IA | Base preventiva de Defender for AI Services | 🆕 | [A24], [A8] |
| 18 | Azure DNS resolver policy (antes "DNS security policy") | Filtrado y registro de consultas DNS por red virtual | — | 🆕 | [A29] |

### B.2 Capacidades de plataforma con función de seguridad

| # | Capacidad | Función | Precisiones validadas | Val. | Fuentes |
|---|---|---|---|---|---|
| 1 | Azure Private Link (incluye **private endpoints**) | Acceso privado a servicios | El private endpoint es un componente de Private Link, no un servicio separado (se fusionaron dos filas del borrador) | ⚠️ | [A31], [A15] |
| 2 | Network Security Groups | Filtrado de tráfico de red | Los NSG flow logs ya no admiten configuraciones nuevas y se retiran el 30-sep-2027: migrar a VNet flow logs | ✅ | [A21] |
| 3 | Azure Virtual Network Manager | Administración centralizada de redes | Sus reglas de administración de seguridad se evalúan antes que las de NSG | ✅ | [A41], [A21] |
| 4 | Azure Policy | Gobierno y cumplimiento de configuraciones | Defender for Cloud implementa sus estándares como iniciativas de Policy | ✅ | [A42], [A6] |
| 5 | Azure RBAC | Control de acceso a recursos | Sistema de autorización de Azure Resource Manager, sin costo | ✅ | [A43] |
| 6 | Azure Monitor y Azure Monitor Logs | Observabilidad y almacenamiento de telemetría | Monitor Logs es parte de Azure Monitor; Sentinel y Defender for Cloud usan sus workspaces | ✅ | [A44], [A45] |
| 7 | Azure Arc | Gobierno de recursos híbridos y multinube | Habilita Defender for Servers/Containers, Policy y Update Manager fuera de Azure | ✅ | [A46] |
| 8 | Azure Update Manager | Gestión de actualizaciones | Azure, on-premises y otras nubes vía Arc | ✅ | [A47] |
| 9 | Azure API Management | Gobierno, autenticación y control de APIs | La protección en runtime proviene de Defender for APIs | ✅ | [A48], [A7] |
| 10 | Azure Front Door | CDN y entrada global con DDoS de capa 3-4 y WAF | **Front Door (classic) se retira el 31-mar-2027**: usar Standard/Premium | ✅ | [A50], [A20] |
| 11 | Azure Application Gateway | Balanceador de capa 7 con terminación TLS y WAF | **La v1 se retiró el 28-abr-2026**; solo v2 | ✅ | [A19] |
| 12 | Microsoft cloud security benchmark | Marco de controles por defecto de Defender for Cloud | La v2 (preview) agrega un dominio de seguridad de IA | 🆕 | [A25] |

### B.3 Resiliencia y continuidad

| # | Servicio | Función | Precisiones validadas | Val. | Fuentes |
|---|---|---|---|---|---|
| 1 | Azure Backup | Copias de seguridad | Bóveda aislada, eliminación temporal y copias inmutables contra ransomware | ✅ | [A28] |
| 2 | Azure Site Recovery | Recuperación ante desastres | Servicio de resiliencia, no de seguridad en sentido estricto | ✅ | [A49] |
| 3 | **Microsoft 365 Backup** | Backup y restauración de SharePoint, OneDrive y Exchange Online | PAYG US$0,15 por GiB/mes; restauraciones sin cargo; almacenamiento de solo anexado | 🆕 | [P21] |

### B.4 Elementos retirados del catálogo

| Elemento del borrador | Motivo | Fuentes |
|---|---|---|
| Azure Migrate | Servicio de evaluación y migración: no figura en el catálogo oficial de seguridad. Si se conserva, moverlo a un anexo de servicios habilitadores | [A27], [A18] |
| Azure Dedicated HSM | En retiro: no acepta clientes nuevos; soporte a clientes existentes hasta el 31-jul-2028. Reemplazado por Azure Cloud HSM (B.1, fila 10) | [A16] |
| Azure Private Endpoint (fila propia) | Fusionado con Azure Private Link (B.2, fila 1) | [A15] |

**Nota del borrador corregida:** la idea de que "algunos son controles integrados en servicios de infraestructura" es razonable, pero las fuentes que citaba no la respaldan: la página de seguridad de red [A32] presenta Firewall, DDoS Protection y WAF como servicios dedicados, y la de Key Vault [A33] es una guía de buenas prácticas. La agrupación anterior se apoya en el catálogo oficial [A18].

---

# 4. Mercados de Gartner Peer Insights relevantes para un CISO (verificados al 4-nov-2026)

Se verificaron los 38 mercados citados por el borrador directamente en Gartner Peer Insights. **Todos existen** y las 27 URLs que citaba el borrador abren correctamente (sin errores ni redirecciones). Para los 11 mercados sin enlace se agregó la URL oficial.

- **Cambios de estado:** 4 mercados cambiaron de nombre o de estado: Access Management (en transición a CIAM), Endpoint Protection Platforms (renombrado Endpoint Protection), Extended Detection and Response (retirado) y Security Orchestration, Automation and Response (en transición a SIEM).
- **Presencia de Microsoft:** Gartner lista algún producto Microsoft en 21 de los 38 mercados, a veces con un nombre distinto del que usaba el borrador (por ejemplo, "Microsoft Purview" en DLP o "Microsoft Defender for Cloud" en CSPM). En los otros 17 no figura ningún producto Microsoft.
- **Lectura correcta:** que Microsoft no figure en un mercado no invalida la correspondencia funcional de la sección 5; solo indica que Gartner no registra ese producto como participante de ese mercado.

## A. Identidad, acceso y dispositivos

| ID | Mercado (nombre oficial) | Estado | Producto Microsoft listado en Peer Insights | Val. | Fuente |
|---|---|---|---|---|---|
| A1 | Access Management (Transitioning to Customer Identity and Access Management (CIAM)) | En transición a CIAM | Microsoft Entra ID; Microsoft Entra External ID | ⚠️ | [G1] |
| A2 | Identity Governance and Administration | Vigente | Microsoft Entra ID; Microsoft Entra ID Governance | ✅ | [G2] |
| A3 | Privileged Access Management | Vigente | No figura | ⚠️ | [G3] |
| A4 | Identity Threat Detection and Response (ITDR) | Vigente | Microsoft Defender for Identity | ⚠️ | [G4] |
| A5 | Endpoint Protection (antes Endpoint Protection Platforms) | Renombrado | Microsoft Defender for Endpoint | ✅ | [G5] |
| A6 | Endpoint Management Tools | Vigente | Microsoft Intune | ✅ | [G6] |
| A7 | Security Awareness Computer-Based Training | Vigente | No figura | ⚠️ | [G7] |

## B. Operaciones y detección

| ID | Mercado (nombre oficial) | Estado | Producto Microsoft listado en Peer Insights | Val. | Fuente |
|---|---|---|---|---|---|
| B1 | Security Information and Event Management | Vigente | Microsoft Sentinel | ✅ | [G8] |
| B2 | Integrated Security Operations Center Solutions | Vigente | Microsoft Sentinel (sin reseñas aún) | ⚠️ | [G9] |
| B3 | Extended Detection and Response (Retired) | Retirado | Microsoft Defender Suite | ⚠️ | [G10] |
| B4 | Security Orchestration, Automation and Response Solutions (Transitioning to Security Information and Event Management) | En transición a SIEM | Microsoft Sentinel | ✅ | [G11] |
| B5 | Network Detection and Response | Vigente | No figura | ⚠️ | [G12] |
| B6 | Managed Detection and Response | Vigente | No figura | ⚠️ | [G13] |
| B7 | Co-Managed Security Monitoring Services | Vigente | Microsoft Defender Suite | ⚠️ | [G14] |
| B8 | Cybersecurity Incident Response Management | Vigente | No figura | ⚠️ | [G15] |
| B9 | External Attack Surface Management | Vigente | Microsoft Defender External Attack Surface Management | ✅ | [G16] |
| B10 | Cyber Asset Attack Surface Management (CAASM) | Vigente | No figura | ⚠️ | [G17] |
| B11 | Exposure Assessment Platforms | Vigente | Microsoft Security Exposure Management | ⚠️ | [G18] |
| B12 | Adversarial Exposure Validation | Vigente | No figura | ✅ | [G19] |

## C. Cloud, aplicaciones y redes

| ID | Mercado (nombre oficial) | Estado | Producto Microsoft listado en Peer Insights | Val. | Fuente |
|---|---|---|---|---|---|
| C1 | Cloud-Native Application Protection Platforms | Vigente | Microsoft Defender for Cloud | ✅ | [G20] |
| C2 | Cloud Security Posture Management Tools | Vigente | Microsoft Defender for Cloud | ⚠️ | [G21] |
| C3 | Security Service Edge | Vigente | No figura | ⚠️ | [G22] |
| C4 | SASE Platforms (la URL conserva el nombre anterior single-vendor-sase) | Vigente | No figura | ⚠️ | [G23] |
| C5 | Network Security Microsegmentation | Vigente | Microsoft Azure (genérico) | ⚠️ | [G24] |
| C6 | Cloud Web Application and API Protection | Vigente | No figura | ⚠️ | [G25] |
| C7 | AI Application Security | Vigente | No figura | ⚠️ | [G26] |
| C8 | AI Usage Control | Vigente | No figura | ⚠️ | [G27] |

## D. Datos, cumplimiento y resiliencia

| ID | Mercado (nombre oficial) | Estado | Producto Microsoft listado en Peer Insights | Val. | Fuente |
|---|---|---|---|---|---|
| D1 | Data Loss Prevention | Vigente | Microsoft Purview | ⚠️ | [G28] |
| D2 | Data Security Posture Management | Vigente | No figura | ⚠️ | [G29] |
| D3 | Data Security Platforms | Vigente | Microsoft Purview Data Governance | ⚠️ | [G30] |
| D4 | Email Security | Vigente | Microsoft Defender for Office 365 | ✅ | [G31] |
| D5 | Digital Communications Governance and Archiving Solutions | Vigente | Microsoft Purview Data Lifecycle Management | ⚠️ | [G32] |
| D6 | Data and Analytics Governance Platforms | Vigente | Microsoft Purview Data Governance | ✅ | [G33] |
| D7 | Privacy UX | Vigente | No figura | ✅ | [G34] |
| D8 | Microsoft 365 Governance Tools | Vigente | No figura | ✅ | [G35] |
| D9 | Backup and Data Protection Platforms | Vigente | Microsoft Azure Backup; Microsoft 365 Backup | ✅ | [G36] |
| D10 | IT Risk Management (ITRM) | Vigente | No figura | ⚠️ | [G37] |
| D11 | Security Consulting Services, Worldwide | Vigente | No figura | ⚠️ | [G38] |

## E. Mercados adyacentes donde Microsoft figura (no estaban en el borrador)

| Mercado Gartner | Producto Microsoft listado | Fuente |
|---|---|---|
| DDoS Mitigation Solutions | Azure DDoS Protection | [G0] |
| Edge Distribution Platforms | Azure Front Door | [G0] |
| E-Discovery Solutions | Microsoft Purview eDiscovery | [G41] |
| Hybrid Mesh Firewall | Azure Firewall | [G42] |
| CPS Protection Platforms; IoT Security | Microsoft Defender for IoT | [G43] |
| Cyberthreat Intelligence Technologies; Workspace Cybersecurity Platforms | Microsoft Defender Suite | [G40] |
| User Authentication | Microsoft Entra ID | [G46] |
| AI Governance Platforms | Microsoft Purview | [G45] |
| Mobile Threat Defense (Transitioning to Workspace Cybersecurity Platforms) | Microsoft Defender for Endpoint | [G47] |
| Decentralized Identity | Microsoft Entra Verified ID | [G0] |
| Vulnerability Assessment (Retired) | Microsoft Defender Vulnerability Management | [G44] |
| IT Security (categoría genérica, sin mercado específico) | Entra ID Protection, Entra Internet Access, Entra Private Access, Defender for Cloud Apps, Azure Web Application Firewall, Purview Compliance Manager, Microsoft Privileged Access Management y Security Copilot | [G39] |

**Notas del borrador validadas**

- "Algunas están en transición de denominación": ✅ (Access Management hacia CIAM; Endpoint Protection Platforms pasó a Endpoint Protection).
- "Gartner distingue SIEM, ISOC, MDR, NDR, ITDR y gestión de exposición": ✅ son mercados separados y vigentes.
- "CNAPP incluye capacidades preventivas y reactivas desde el código hasta el runtime": ✅ paráfrasis fiel de la definición del mercado; Defender for Cloud figura listado [G20].
- "Gartner tiene mercados específicos para DLP, DSPM, correo, backup, archivo de comunicaciones y gobierno de Microsoft 365": ⚠️ todos existen, pero el borrador apoyaba DSPM en la URL de Data Security Platforms; DSPM tiene URL propia [G29].
- "No es un inventario exhaustivo; los mercados cambian, se fusionan o se retiran": ✅ lo confirman el retiro de XDR y las transiciones de Access Management y SOAR.
- Método y límites del acceso a Gartner: ver Anexo D. No se reproduce contenido de Gartner; solo nombres de mercados y productos.

---

# 5. Correspondencia consolidada: mercados Gartner → Microsoft (corregida)

El borrador tenía 29 filas: 9 mercados de la sección 4 no aparecían y 4 filas contradecían a la sección 4 (IT Risk Management, Data Security Platforms, NDR y Exposure Assessment Platforms). Esta versión cubre los **38 mercados** y separa dos dimensiones que el borrador mezclaba:

1. **Tipo de correspondencia (funcional):** cuánto cubre la oferta Microsoft los requisitos típicos del mercado, según la documentación oficial de Microsoft.
2. **Listado en Peer Insights:** si Gartner registra un producto Microsoft en ese mercado, y con qué nombre.

| Tipo | Criterio |
|---|---|
| Directa | Microsoft tiene un producto o servicio diseñado para ese mercado |
| Parcial | Cubre capacidades relevantes, pero no todos los requisitos típicos del mercado |
| Complementaria | Contribuye al resultado sin constituir por sí sola una solución del mercado |
| Sin correspondencia | No hay oferta Microsoft equivalente |
| Histórico | El mercado está retirado; se conserva solo como referencia |

| ID | Mercado Gartner | Correspondencia Microsoft (funcional) | Tipo | Listado en Peer Insights | Licencia / consumo | Cambio respecto del borrador |
|---|---|---|---|---|---|---|
| A1 | Access Management (en transición a CIAM) | Entra ID (fuerza laboral) y Entra External ID (clientes y externos) | Directa | Sí: Microsoft Entra ID; Microsoft Entra External ID | P1/P2 (E3/E5/E7); External ID: PAYG por MAU | Nombre oficial con sufijo de transición; se agrega External ID |
| A2 | Identity Governance and Administration | Entra ID Governance (más capacidades básicas de P2) | Directa | Sí: Microsoft Entra ID; Microsoft Entra ID Governance | ID Governance (add-on), Entra Suite o E7 | Sin cambio |
| A3 | Privileged Access Management | Entra PIM (roles de Entra, recursos de Azure y grupos) y Privileged Access Management de Purview (tareas de Microsoft 365) | Parcial | No figura | P2 o ID Governance; Purview PAM en E5/E7 | Se aclara que Microsoft no figura en este mercado |
| A4 | Identity Threat Detection and Response (ITDR) | Defender for Identity, con Entra ID Protection y Defender XDR como complemento | Directa | Sí: Microsoft Defender for Identity | E5/E7 o Defender Suite; ID Protection con P2 o Entra Suite | Entra ID Protection no figura en ITDR (Gartner lo ubica en IT Security) |
| A5 | Endpoint Protection (antes Endpoint Protection Platforms) | Defender for Endpoint P1/P2 y Defender for Business | Directa | Sí: Microsoft Defender for Endpoint | P1 en E3; P2 en E5/E7 | Se agrega nombre oficial y URL |
| A6 | Endpoint Management Tools | Intune, con Windows Autopilot y Windows Autopatch | Directa | Sí: Microsoft Intune | E3/E5/E7 | Sin cambio |
| A7 | Security Awareness Computer-Based Training | Attack simulation training (parte de Defender for Office 365 P2) | Parcial | No figura | E5/E7 o MDO P2 | Se aclara que Microsoft no figura (MDO se lista solo en Email Security) |
| B1 | Security Information and Event Management | Microsoft Sentinel (incluido Sentinel data lake) | Directa | Sí: Microsoft Sentinel | Consumo en Azure; beneficio de ingesta para E5/E7 | Sin cambio |
| B2 | Integrated Security Operations Center Solutions | Sentinel y Defender XDR en el portal de Defender; ISOC en Microsoft Defender (preview) | Directa | Sí: Microsoft Sentinel (sin reseñas aún) | Defender XDR con E5/E7 o Defender Suite; Sentinel por consumo; ISOC en preview | Solo Sentinel figura listado; se agrega ISOC en Defender |
| B3 | Extended Detection and Response (Retired) | Defender XDR (usar los mercados SIEM e ISOC como referencia vigente) | Histórico | Sí: Microsoft Defender Suite | — | Mercado retirado; el listado figura como Microsoft Defender Suite |
| B4 | SOAR Solutions (en transición a SIEM) | Automatización de Sentinel (reglas de automatización y playbooks de Logic Apps) | Directa | Sí: Microsoft Sentinel | Consumo en Azure | Se agrega nombre oficial y URL |
| B5 | Network Detection and Response | Sin NDR nativo. Señales de red complementarias: Defender for IoT (OT/IoT), IDPS de Azure Firewall y VNet flow logs hacia Sentinel | Complementaria | No figura | Varios | Se unifica: la sección 4 decía parcial y la 5, complementaria. Sentinel es un SIEM, no un NDR |
| B6 | Managed Detection and Response | Defender Experts MDR (Plan 1 y Plan 2) y Defender Experts for Servers | Directa | No figura | Servicio contratado aparte | Se mantiene directa como correspondencia funcional, sin listado de Gartner |
| B7 | Co-Managed Security Monitoring Services | Defender Experts (MDR y Hunting) junto al SOC del cliente | Parcial | Sí: Microsoft Defender Suite | Servicio contratado aparte | Se registra el nombre del listado |
| B8 | Cybersecurity Incident Response Management | Incidentes de Defender XDR y gestión de casos de Sentinel/ISOC (preview) | Parcial | No figura | E5/E7 o Defender Suite; Sentinel por consumo | Se explicita el tipo; es un mercado de gestión de casos para equipos CIRT |
| B9 | External Attack Surface Management | Defender EASM y la iniciativa EASM de Exposure Management | Directa | Sí: Microsoft Defender External Attack Surface Management | Azure, por activo facturable | Sin cambio |
| B10 | Cyber Asset Attack Surface Management (CAASM) | Security Exposure Management (inventario, grafo de exposición y conectores externos) | Parcial | No figura | Incluido con E5/E7 o Defender Suite; conectores por consumo | Sin cambio de tipo; Microsoft no figura |
| B11 | Exposure Assessment Platforms | Security Exposure Management, con Defender Vulnerability Management como capacidad | Directa | Sí: Microsoft Security Exposure Management | Incluido con E5/E7 o Defender Suite | MDVM no figura en este mercado (Gartner lo ubica en Vulnerability Assessment, retirado) |
| B12 | Adversarial Exposure Validation | Sin equivalente; las rutas de ataque de Exposure Management y Attack simulation training solo complementan | Complementaria | No figura | — | La sección 5 decía parcial; se ajusta a complementaria |
| C1 | Cloud-Native Application Protection Platforms | Defender for Cloud | Directa | Sí: Microsoft Defender for Cloud | Consumo en Azure | Sin cambio |
| C2 | Cloud Security Posture Management Tools | Foundational CSPM (gratis) y Defender CSPM | Directa | Sí: Microsoft Defender for Cloud | Gratis / por recurso facturable | El listado es Defender for Cloud, no Defender CSPM |
| C3 | Security Service Edge | Global Secure Access (Entra Internet Access y Private Access) con Defender for Cloud Apps | Parcial | No figura | Entra Suite (E7) o standalone; Defender for Cloud Apps en E5/E7 | Microsoft no figura (sus productos se listan en IT Security); validar requisitos SWG, CASB y ZTNA |
| C4 | SASE Platforms | Global Secure Access y redes de Azure, sin SD-WAN propio | Parcial | No figura | — | Nombre oficial actualizado; Microsoft no figura |
| C5 | Network Security Microsegmentation | NSG, reglas de administración de seguridad de Virtual Network Manager y Azure Firewall (ámbito Azure) | Parcial | Sí: Microsoft Azure (genérico) | Consumo en Azure | Se agrega URL y nombre del listado; Azure Firewall figura aparte en Hybrid Mesh Firewall |
| C6 | Cloud Web Application and API Protection | Azure WAF, Front Door, DDoS Protection y Defender for APIs con API Management | Parcial | No figura | Consumo en Azure | Microsoft no figura; cada servicio se lista en otro mercado (ver 4.E) |
| C7 | AI Application Security | Defender for AI Services, postura de IA en Defender CSPM y Prompt Shields | Parcial | No figura | Consumo en Azure | Microsoft no figura; validar cobertura en runtime |
| C8 | AI Usage Control | Defender for Cloud Apps (apps de IA), Purview DSPM y DLP de navegador y red, Entra Internet Access y descubrimiento de agentes de IA locales en MDE | Parcial | No figura | E5/E7 y PAYG | Se agregan MDE y DLP de red; Microsoft no figura |
| D1 | Data Loss Prevention | Purview DLP, incluidos Endpoint DLP y DLP de red | Directa | Sí: Microsoft Purview | E3 parcial (correo y archivos); E5/E7 completo; red por consumo | El listado es Microsoft Purview |
| D2 | Data Security Posture Management | Purview DSPM y la postura de datos de Defender CSPM | Directa | No figura | Licencia de soporte y PAYG | Se agrega la URL propia del mercado; Microsoft no figura |
| D3 | Data Security Platforms | Purview (Information Protection, DLP, DSPM, IRM) con Key Vault y Managed HSM | Parcial | Sí: Microsoft Purview Data Governance | E5/E7, Purview Suite y PAYG | Se registra el nombre del listado; Key Vault no figura |
| D4 | Email Security | Defender for Office 365 y la seguridad integrada de buzones en la nube | Directa | Sí: Microsoft Defender for Office 365 | P1 en E3; P2 en E5/E7 | Sin cambio |
| D5 | Digital Communications Governance and Archiving Solutions | Purview Data Lifecycle Management y Records Management, Communication Compliance, eDiscovery y conectores de datos | Parcial | Sí: Microsoft Purview Data Lifecycle Management | Básico en E3; completo en E5/E7 | Se registra el listado; eDiscovery figura en E-Discovery Solutions |
| D6 | Data and Analytics Governance Platforms | Purview Unified Catalog y Data Map | Directa | Sí: Microsoft Purview Data Governance | PAYG | Se agrega URL |
| D7 | Privacy UX | Sin equivalente integral; Priva Privacy Risk Management solo complementa | Sin correspondencia | No figura | — | Se explicita Priva como complemento |
| D8 | Microsoft 365 Governance Tools | Capacidades nativas de administración y gobierno de Microsoft 365 (Purview, Entra ID Governance) | Complementaria | No figura | — | Sin cambio; el mercado reúne herramientas de terceros |
| D9 | Backup and Data Protection Platforms | Azure Backup y Microsoft 365 Backup | Directa | Sí: Microsoft Azure Backup; Microsoft 365 Backup | Consumo en Azure / PAYG | Sin cambio; Microsoft 365 Backup se agrega al inventario (3.B.3) |
| D10 | IT Risk Management (ITRM) | Purview Compliance Manager, con el cumplimiento regulatorio de Defender for Cloud y Azure Policy | Complementaria | No figura | Plantillas según licencia | Se unifican las secciones 4 y 5, que diferían |
| D11 | Security Consulting Services, Worldwide | Servicios proactivos de Microsoft Incident Response, evaluaciones de Unified Enterprise, Enhanced Designated Engineering y FastTrack for Microsoft 365 | Complementaria | No figura | Contratos de servicio | El borrador decía directa; se ajusta y se usa el nombre oficial |

**Resumen calculado**

| Tipo de correspondencia | Mercados |
|---|---|
| Directa | 18 |
| Parcial | 13 |
| Complementaria | 5 |
| Sin correspondencia | 1 |
| Histórico | 1 |
| **Total** | **38** |

- En 21 de los 38 mercados Gartner lista un producto Microsoft. De los 18 mercados con correspondencia directa, 2 no tienen listado en Peer Insights: Managed Detection and Response (B6), Data Security Posture Management (D2).
- Esta tabla sigue siendo un **mapeo funcional propuesto**: no afirma que Gartner reconozca cada producto Microsoft en cada mercado. Ese reconocimiento solo existe donde la columna de listado dice "Sí".

---

# 6. Servicios de seguridad ofrecidos por Microsoft (corregido)

Se mantienen separados de los productos tecnológicos. **Security Copilot se trasladó a la sección 1.B**: es un producto licenciado por capacidad (SCU), no un servicio profesional [D12].

| # | Servicio | Descripción validada | Categoría relacionada | Val. | Fuentes |
|---|---|---|---|---|---|
| 1 | Defender Experts MDR | MDR 24×7 que **complementa** el SOC del cliente, no lo reemplaza. **Plan 1** (antes "Defender Experts for XDR") cubre las cargas de Defender; **Plan 2** suma fuentes de terceros vía Sentinel (requiere Sentinel y un mínimo de 1.500 puestos) y no es un SIEM gestionado | MDR | ⚠️ | [D14] |
| 2 | Defender Experts Hunting | Búsqueda proactiva de amenazas para clientes con SOC propio; ofertas Hunting – XDR y Hunting – Servers | Threat hunting | ✅ | [D13] |
| 3 | Defender Experts for Servers | MDR para servidores en Azure, AWS, GCP y on-premises; medidor de pago por uso; requiere Defender for Servers P1 o P2, Entra ID P2 y Defender for Endpoint en los servidores | MDR / CWPP | ✅ | [D13], [D22] |
| 4 | Defender Experts Threat Intelligence | Informes mensuales y alertas proactivas adaptados a industria, geografía y entorno. No confundir con MDTI (producto retirado) | Servicios de inteligencia de amenazas | ✅ | [D13] |
| 5 | Defender Experts Cybersecurity Incident Response | Marca vigente de **Microsoft Incident Response** (antes DART): servicios proactivos (planificación, evaluación, simulación) y reactivos (investigación, contención, recuperación); contrato separado | Servicios de respuesta a incidentes | ✅ | [D13], [D24] |
| 6 | **Defender Experts Suite** | Paquete lanzado el 1-ene-2026: MDR, Microsoft Incident Response y Enhanced Designated Engineering | Servicios administrados | 🆕 | [D18] |
| 7 | **FastTrack for Microsoft 365** (el borrador decía "Microsoft Security FastTrack", nombre no oficial) | Asistencia remota de despliegue y adopción para tenants con 150 o más licencias elegibles (incluye Defender, Purview, Entra e Intune). FastTrack for Azure se retiró el 31-dic-2024 | Servicios de implementación | ⚠️ | [D19], [D27] |
| 8 | **Microsoft Unified** (el borrador decía "Microsoft Unified Support") | Servicio base Unified Enterprise (soporte reactivo 24×7, gestión del éxito, evaluaciones) con complementos Value Acceleration Services y Mission Critical Services | Servicios de soporte | 🕒 | [D20] |
| — | "Microsoft Security Assessment" | **Eliminado**: no se encontró una oferta oficial vigente con ese nombre (solo una herramienta descargable heredada). Alternativas oficiales: servicios proactivos de Microsoft Incident Response, evaluaciones de Unified Enterprise y Enhanced Designated Engineering | Consultoría de seguridad | ❔ | [D13], [D20], [D18] |

**Nota validada:** el borrador acierta al decir que Defender Experts es una familia de servicios y que MDR se comercializa por separado de las licencias Defender; ambas URLs citadas existen [D13], [D14]. Precisión: **cada** servicio Defender Experts se vende por separado [D13].

---

# 7. Diferencias entre Microsoft 365 E3, E5 y E7 (vigente desde el 1-jul-2026)

El borrador describía el empaquetado anterior a julio de 2026. Desde el **1-jul-2026** rigen nuevos precios y, con despliegue completo al **1-ago-2026**, E3 sumó Defender for Office 365 P1, Intune Plan 2, Remote Help y Advanced Analytics; E5 sumó además Security Copilot, Endpoint Privilege Management, Microsoft Cloud PKI y Enterprise Application Management [L5]. E7 incluye todo E5 más Microsoft 365 Copilot, Agent 365 y Entra Suite [L1], y hereda las incorporaciones de E5 [L13].

**Precios de lista (USD por usuario/mes, compromiso anual, con Teams):** E3 US$39 · E5 US$60 · E7 US$99. Sin Teams: E3 US$30,45 · E5 US$51,45 · E7 US$90,45 [L5], [L6]. Los clientes existentes mantienen su precio hasta la renovación [L5].

| Capacidad | Microsoft 365 E3 | Microsoft 365 E5 | Microsoft 365 E7 | Val. | Fuentes |
|---|---|---|---|---|---|
| Entra ID | P1 | P2 | P2 | ✅ | [L4] |
| Microsoft Entra Suite | **Add-on** (US$12; requiere P1) | Add-on (precio especial para P2/E5) | Incluido | ❌ corregido | [L6], [E3], [L1] |
| Entra ID Governance | Add-on (US$7) | Add-on (opción Step Up) | Incluido (vía Entra Suite) | 🆕 | [E2] |
| Defender for Endpoint | P1 | P2 | P2 | ✅ | [L4] |
| Defender for Office 365 | **P1 (desde 1-jul-2026)** | P2 | P2 | 🕒 corregido | [D4], [L5] |
| Defender for Identity | No (sí con Defender Suite) | Sí | Sí | ✅ | [L4] |
| Defender for Cloud Apps | **Solo Cloud App Discovery** | Completo | Completo | ⚠️ corregido | [L4] |
| Defender for IoT (Enterprise IoT) | No | Sí | Sí | 🆕 | [L4], [D8] |
| Defender XDR | Acceso con las señales de E3 (MDE P1, Cloud App Discovery); completo con Defender Suite | Completo | Completo | ✅ | [D2] |
| Microsoft Security Copilot | No (SCU aprovisionadas) | **Incluido: 400 SCU por cada 1.000 licencias/mes, hasta 10.000** | Igual que E5 | 🆕 | [L1], [L3], [L6] |
| Purview Information Protection | Plan 1 (núcleo) | Plan 2 | Plan 2 | ✅ | [L4] |
| Purview DLP | Correo y archivos | Completo (incluye Teams y Endpoint DLP) | Completo | ✅ | [L2], [L4] |
| Purview Insider Risk Management | No (sí con Purview Suite) | Sí | Sí | ✅ | [L4] |
| Purview Communication Compliance | No | Sí | Sí | 🆕 | [L4] |
| Purview Audit | Standard (180 días) | Premium (1 año) | Premium | 🆕 | [L4], [P9] |
| Purview eDiscovery | Standard | Premium | Premium | ✅ | [L4] |
| Intune | **Plan 1 + Plan 2 + Remote Help + Advanced Analytics** | E3 + Endpoint Privilege Management + Enterprise Application Management + Microsoft Cloud PKI | Igual que E5 | 🕒 corregido | [L5], [W3] |
| Windows Enterprise | Windows 11 Enterprise E3 | Windows 11 Enterprise E5 | Windows 11 Enterprise E5 | ✅ | [L4] |
| Microsoft 365 Copilot | Add-on (US$30) | Add-on (US$30) | Incluido | ✅ | [L4] |
| Agent 365 | **No elegible solo con E3**: requiere además Defender Suite y Purview Suite | Add-on (US$15) | Incluido | ⚠️ corregido | [L8], [L4] |
| Microsoft Sentinel | Consumo en Azure | Consumo en Azure + beneficio de ingesta de hasta 5 MB por usuario/día de datos de Microsoft 365; ISOC en Defender (preview) sin workspace de Sentinel activo | Igual que E5 | ⚠️ corregido | [D25], [D15] |
| Defender for Cloud | Consumo en Azure (Foundational CSPM sin costo) | Igual | Igual | ✅ | [A3] |
| Azure Firewall / WAF | Consumo en Azure | Consumo en Azure | Consumo en Azure | ✅ | [A11], [A13] |
| Purview pay-as-you-go (datos fuera de Microsoft 365, IA de terceros, red) | PAYG | PAYG | PAYG | 🆕 | [L1], [P2] |
| Microsoft 365 Backup | PAYG | PAYG | PAYG | 🆕 | [P21] |

**Rutas de add-on validadas**

| Add-on | Precio de lista | Requisito | Fuentes |
|---|---|---|---|
| Microsoft Defender Suite (antes Microsoft 365 E5 Security) | US$12 | Microsoft 365 E3, u Office 365 E3 + EMS E3 | [L6], [L5] |
| Microsoft Purview Suite (antes Microsoft 365 E5 Compliance) | US$12 | Microsoft 365 E3, u Office 365 E3 + EMS E3 | [L6], [L5] |
| Microsoft Entra Suite | US$12 | Entra ID P1 o un plan que lo incluya | [L6] |
| Microsoft Intune Suite | US$10 | Intune Plan 1 o un plan que lo incluya | [W3], [L6] |
| Microsoft 365 Copilot | US$30 | Plan de Microsoft 365 elegible | [L4] |
| Agent 365 | US$15 | Microsoft 365 E5/A5/G5, Business Premium, Defender Suite + Purview Suite (también Edu y FLW) | [L8], [L4] |

**Notas**

- La nota del borrador ("las inclusiones pueden variar por SKU, contrato y país") es correcta y sus tres URLs existen [L6], [L4], [L7]. Se agregan como fuentes los **Product Terms** (contractuales) y la nota de licenciamiento de 2026 [L5], [L8].
- **Discrepancia abierta:** la página de producto de E3 menciona Endpoint Privilege Management [L2], mientras la nota de licenciamiento [L5] y la FAQ de Intune [W3] lo ubican solo en E5. Se adopta la nota de licenciamiento; confirmar en Product Terms o en el tenant (Anexo D).
- En nubes de gobierno el alcance de las incorporaciones es menor (por ejemplo, G5 GCC High/DoD solo suma Endpoint Privilege Management) [L5].

---

# 8. Cómo incorporar este catálogo al AI CISO Atlas (ajustado)

La propuesta del borrador se mantiene (evitar una relación única `MicrosoftProduct → GartnerCategory`). La validación mostró tres problemas que el modelo debe poder representar: **productos con un nombre distinto en Gartner**, **capacidades que cambian de licencia o de estado** y **fuentes oficiales que se contradicen**. Por eso se proponen entidades y relaciones adicionales.

## 8.1 Entidades

| Entidad | Propósito | Cambio |
|---|---|---|
| `Technology` | Producto o capacidad Microsoft | Se mantiene |
| `SecurityCapability` | Capacidad funcional (p. ej., EDR, ZTNA, DSPM) | Se mantiene |
| `MarketCategory` | Mercado de Gartner Peer Insights, con estado (vigente, en transición, retirado) | Se agrega el estado |
| `LicenseEntitlement` | Plan o SKU (E3, E5, E7, add-ons) | Se mantiene |
| `ServicePlan` | Plan de servicio dentro de un SKU, con su identificador oficial | **Nuevo** |
| `ManagedService` | Servicio Defender Experts, Microsoft Incident Response, FastTrack, Unified | Se mantiene |
| `GartnerListing` | Producto tal como lo nombra Gartner en un mercado (puede diferir del nombre comercial) | **Nuevo** |
| `LifecycleEvent` | Preview, GA, renombre, retiro, cambio de precio o de empaquetado, con fecha | **Nuevo** |
| `Evidence` | URL oficial, fecha de consulta, fecha de actualización de la página y tipo de fuente (contractual, documentación, comercial, blog) | **Nuevo** |

**Clave estable recomendada para licencias.** Usar los identificadores oficiales de productos y planes de servicio (nombre de producto, String ID y GUID) que Microsoft publica en Learn, con descarga en CSV; la página se actualizó el 19-ago-2026 [L9]. Ejemplo verificado: el SKU `AGENT_365` incluye, entre otros, los planes de servicio Microsoft Defender for AI, Entra ID Governance y Entra Network Controls para agentes asistivos, y varias capacidades de Purview "for Agents" (Audit, DLP, Information Protection, Insider Risk Management, eDiscovery y Communication Compliance) [L9]. Este nivel permite modelar `LicenseEntitlement → ServicePlan → SecurityCapability` sin depender de páginas comerciales.

## 8.2 Relaciones

| Relación | Significado | Cambio |
|---|---|---|
| `PROVIDES_CAPABILITY` | Una tecnología proporciona una capacidad | Se mantiene |
| `ALIGNS_WITH_MARKET` | Correspondencia **funcional** con un mercado (Directa, Parcial, Complementaria, Sin correspondencia) | Se precisa el alcance |
| `LISTED_IN_MARKET` | Gartner lista el producto en ese mercado (con el nombre de `GartnerListing`) | **Nueva**: separa reconocimiento de correspondencia |
| `INCLUDED_IN_LICENSE` | Una capacidad está incluida en un plan | Se mantiene |
| `CONTAINS_SERVICE_PLAN` | Un SKU contiene un plan de servicio | **Nueva** |
| `REQUIRES_ADDON` / `REQUIRES_PREREQUISITE` | Necesita licencia adicional o un prerrequisito de compra (p. ej., Agent 365) | Se amplía |
| `BILLED_AS` | Por usuario, por recurso, por sitio, PAYG o SCU | **Nueva** |
| `DELIVERED_AS_SERVICE` | Capacidad entregada como servicio administrado | Se mantiene |
| `PROTECTS_WORKLOAD` | Protege un workload específico | Se mantiene |
| `SUPPORTS_CONTROL_OBJECTIVE` | Contribuye a un objetivo de control | Se mantiene |
| `MAPS_TO_ATLAS_DOMAIN` | Se relaciona con un dominio del Atlas | Se mantiene |
| `RENAMED_FROM` / `SUPERSEDED_BY` | Trazabilidad de renombres y reemplazos (p. ej., MDTI → inteligencia en Defender; Dedicated HSM → Cloud HSM) | **Nueva** |
| `HAS_LIFECYCLE_EVENT` | Vincula una tecnología o un mercado con sus eventos fechados | **Nueva** |
| `SUPPORTED_BY` | Vincula cualquier relación con su `Evidence` | **Nueva** |

## 8.3 Atributos mínimos por relación

Se mantienen los del borrador (fuente oficial, fecha de verificación, versión o estado, tipo de correspondencia, nivel de cobertura y restricciones de licencia) y se agregan: **fecha de actualización de la página fuente**, **tipo de fuente** (prevalece la contractual: Product Terms) y **marca de discrepancia** cuando dos fuentes oficiales difieran (ver Anexo D).

## 8.4 Cruce analítico

**Microsoft Technology × Gartner Category × AI CISO Atlas Domain × NIST CSF Function × License**. Para la dimensión NIST conviene usar **CSF 2.0**, publicado el 26-feb-2024, cuyo núcleo se organiza en seis funciones: **Govern, Identify, Protect, Detect, Respond y Recover**; Govern es la función nueva [N1].

---

# 9. Consideraciones para interpretar el catálogo

Las cuatro distinciones del borrador se confirman con la evidencia de esta validación y se agregan tres.

1. **Producto no equivale a mercado.** Defender for Cloud es una CNAPP que reúne CSPM, DevSecOps y CWPP [A1]; Gartner lo lista tanto en CNAPP como en CSPM Tools [G20], [G21]. ✅
2. **Mercado no equivale a capacidad.** Gartner agrupa capacidades en categorías comerciales que cambian: XDR está retirado y SOAR está en transición hacia SIEM [G10], [G11]. ✅
3. **Capacidad no equivale a licencia.** Ejemplo verificado: Entra Agent ID está disponible para todo cliente de Entra, pero aplicar Conditional Access, ID Protection o gobierno a los agentes requiere Agent 365 [E6], [L6]. ✅
4. **Correspondencia no equivale a cobertura completa.** PIM gestiona el acceso privilegiado just-in-time sobre recursos de Entra ID, Azure y otros servicios en línea de Microsoft como Microsoft 365 o Intune [E8]; no reemplaza todos los escenarios de un producto PAM especializado, y Microsoft no figura en el mercado PAM de Gartner [G3]. ✅
5. **Listado en Gartner no equivale a correspondencia funcional** (nueva). En 17 de los 38 mercados Microsoft no figura, aunque en varios tenga una oferta directa (MDR, DSPM); y donde figura, el nombre puede diferir del comercial ("Microsoft Purview" en DLP, "Microsoft Defender Suite" en Co-Managed Security Monitoring).
6. **Disponibilidad no equivale a madurez** (nueva). Conviven funciones en preview (ISOC en Defender), GA recientes (nuevo DSPM, Agent 365) y retiros con fecha (MDTI, Dedicated HSM, NSG flow logs). Cada fila del Atlas debe llevar su estado y su fecha.
7. **Página comercial no equivale a fuente contractual** (nueva). Cuando las fuentes difieren (por ejemplo, Endpoint Privilege Management en E3, o los prerrequisitos de Agent 365), prevalecen los Product Terms y las notas oficiales de licenciamiento [L8], [L5].

---

# Conclusión

Microsoft ofrece un stack de seguridad que abarca identidad y acceso; endpoint y dispositivos; correo y colaboración; protección y gobierno de datos; seguridad de aplicaciones y APIs; seguridad cloud y multinube; operaciones SOC (SIEM, XDR e ISOC); exposición y vulnerabilidades; inteligencia de amenazas, hoy **integrada** en Defender y Sentinel; seguridad de IA y agentes (Agent 365, Entra Agent ID, Defender for AI Services y protecciones de Purview para IA); continuidad y recuperación; y servicios administrados de seguridad.

**La conclusión principal del borrador se confirma:** Microsoft no debe modelarse como una lista de productos que compiten uno a uno con las categorías de Gartner. La correspondencia es de muchos a muchos —**productos → capacidades → mercados → objetivos de control**— y la validación agrega dos ejes que el modelo debe registrar: el **reconocimiento de Gartner** (listado o no, y con qué nombre) y el **ciclo de vida** de cada capacidad (preview, GA, renombre, retiro, cambio de empaquetado).

**Vigencia de este documento:** la validación se hizo el 4-nov-2026 contra fuentes oficiales; el Anexo A registra cada afirmación con su veredicto y su evidencia. Para usarlo como matriz contractual de licenciamiento, confirmar cada SKU en los Product Terms vigentes y revisar los eventos con fecha futura del Anexo B.

---

# Anexo A — Registro de validación por afirmación

Cada fila corresponde a una afirmación o a una fila del borrador v1. **Val.**: ✅ correcta · ⚠️ correcta con matiz · ❌ incorrecta · 🕒 desactualizada · ❔ no verificable · 📝 editorial. Las URL marcadas "en resultados de búsqueda" se identificaron pero no se abrieron.

## A.1 Introducción (Microsoft 365 E7)

| ID | Ítem | Afirmación del borrador | Val. | Corrección aplicada | Fuente(s) | Evidencia |
|---|---|---|---|---|---|---|
| INTRO-01 | Composición de E7 y alcance | "E7 incorpora E5, Copilot, Agent 365 y Entra Suite; no es licencia universal de los servicios de seguridad de Azure" | ✅ | Opcional: agregar que E7 (igual que E5) trae capacidad incluida de Security Copilot y que Sentinel, Defender for Cloud, Azure Firewall/WAF y la protección de datos sobre data estates/IA se facturan aparte (Azure / pay-as-you-go). | https://www.microsoft.com/en-us/microsoft-365/enterprise/microsoft-365-plans-and-pricing ; https://www.microsoft.com/en-us/microsoft-365/enterprise/e7 | La comparativa dice "Includes Microsoft 365 E5, Copilot, Agent 365, and Microsoft Entra Suite"; E7 aclara que data security sobre data estates/IA es pay-as-you-go con cuenta Azure. |

## A.2 Microsoft Entra (1.A)

| ID | Ítem | Afirmación del borrador | Val. | Corrección aplicada | Fuente(s) | Evidencia |
|---|---|---|---|---|---|---|
| ENT-01 | Microsoft Entra ID | Directorio e identidad empresarial — E3/E5/E7 | ✅ | Matiz útil: Entra ID Free viene con cualquier suscripción M365/Azure; E3 aporta P1 y E5/E7 aportan P2. | https://www.microsoft.com/en-us/security/microsoft-entra-pricing ; https://learn.microsoft.com/en-us/entra/id-governance/licensing-fundamentals | Entra ID Free se incluye con suscripciones de Microsoft 365 o Azure; P1 viene en E3/E5/E7. |
| ENT-02 | Entra ID P1 | Conditional Access y administración avanzada — E3/E5/E7 | ✅ | Matiz: también en Business Premium y EMS E3; standalone US$7 (antes US$6) desde 1-jul-2026. | https://learn.microsoft.com/en-us/entra/id-governance/licensing-fundamentals ; https://www.microsoft.com/en-us/licensing/news/2026-M365-Packaging-Pricing-Updates | Learn: P1 "included with Microsoft 365 E3, E5 or E7"; Entra Plan 1 pasa de US$6 a US$7. |
| ENT-03 | Entra ID P2 | Protección basada en riesgo y capacidades privilegiadas — E5/E7 | ✅ | Matiz: P2 incluye ID Protection, PIM, entitlement management y access reviews **básicos**; standalone US$10 (antes US$9). | https://www.microsoft.com/en-us/security/microsoft-entra-pricing ; https://learn.microsoft.com/en-us/entra/id-governance/licensing-fundamentals | Precios Entra: P2 suma ID Protection, CA basada en riesgo, PIM, "Basic entitlement management", "Basic access reviews". |
| ENT-04 | Entra Conditional Access | Políticas adaptativas — E3+ | ✅ | Matiz: CA requiere P1 (E3+); la CA **basada en riesgo** requiere P2 (E5/E7) o Entra Suite (incluye ID Protection). | https://www.microsoft.com/en-us/security/microsoft-entra-pricing | FAQ: E3 incluye P1 con SSO, MFA y Conditional Access; P2 agrega "Risk-based Conditional Access". |
| ENT-05 | Entra ID Protection | Detección y respuesta ante riesgos de identidad — E5/E7 | ✅ | Matiz: P1 trae algunas detecciones de riesgo; la funcionalidad completa está en P2 y también en Entra Suite (ruta E3 + Entra Suite). | https://www.microsoft.com/en-us/security/microsoft-entra-pricing ; https://learn.microsoft.com/en-us/entra/id-governance/licensing-fundamentals | Nota 4 de precios: P1 incluye detección de riesgo; P2 agrega detecciones avanzadas. Entra Suite integra ID Protection. |
| ENT-06 | Entra PIM | Acceso privilegiado just-in-time — E5/E7 | ✅ | Matiz: PIM requiere P2 **o** Entra ID Governance (ruta E3 + ID Governance/Entra Suite). | https://learn.microsoft.com/en-us/entra/id-governance/licensing-fundamentals | "You need either Microsoft Entra ID Governance licenses or Microsoft Entra ID P2 licenses" para PIM. |
| ENT-07 | Entra ID Governance | Ciclo de vida, revisiones y paquetes — E7 / Add-on | ✅ | Precisar: add-on US$7 que requiere P1 (vale sobre E3) o "Step Up for P2" sobre E5; incluido en Entra Suite y en E7. | https://learn.microsoft.com/en-us/entra/id-governance/licensing-fundamentals ; https://www.microsoft.com/en-us/security/microsoft-entra-pricing | Requiere un producto con AAD_PREMIUM (P1), p. ej., M365 E3/E5; también incluido en Entra Suite y M365 E7. |
| ENT-08 | Entra Lifecycle Workflows | Altas, movimientos y bajas — E7 / Add-on | ✅ | — (no está en P2; requiere ID Governance, Entra Suite o E7). | https://learn.microsoft.com/en-us/entra/id-governance/licensing-fundamentals | Matriz: LCW solo con ID Governance, Entra Suite y M365 E7. |
| ENT-09 | Entra Entitlement Management | Gobierno de autorizaciones y paquetes — E7 / Add-on | ⚠️ | Cambiar a "E5/E7 (básico, vía P2); avanzado: ID Governance / Entra Suite / E7; para agentes: Agent 365". Paquetes para usuarios, autoservicio, aprobaciones, vencimiento y SoD funcionan con P2. | https://learn.microsoft.com/en-us/entra/id-governance/licensing-fundamentals ; https://www.microsoft.com/en-us/security/microsoft-entra-pricing | Learn: algunas capacidades "can operate with a Microsoft Entra ID P2 subscription"; P2 incluye "Basic entitlement management". |
| ENT-10 | Entra Access Reviews | Recertificación — E5/E7; alcance según licencia | ✅ | Matiz: básicas con P2 (E5); ML-assisted, usuarios inactivos, PIM for Groups y catálogos requieren ID Governance/E7. Microsoft no agregará nuevas funciones IGA a P2. | https://learn.microsoft.com/en-us/entra/id-governance/licensing-fundamentals | FAQ: "no new Identity Governance & Administration (IGA) features" se agregarán a P2. |
| ENT-11 | Entra Workload ID | Identidades de apps y servicios — Azure / Add-on | ⚠️ | Cambiar a "Free incluido / Workload ID Premium standalone (US$3 por identidad de workload/mes), no incluido en ningún suite (tampoco E7)". No es un servicio de Azure: se compra en el Entra admin center con suscripción Azure **o** Microsoft 365. Free: managed identities, workload identity federation; Premium: CA e ID Protection para workloads, access reviews de service principals privilegiados, App Health. | https://learn.microsoft.com/en-us/entra/workload-id/workload-identities-faqs ; https://www.microsoft.com/en-us/security/microsoft-entra-pricing | FAQ: SKU standalone, "$3 per workload identity per month, and not part of another SKU". |
| ENT-12 | Entra Agent ID | Identidad y trazabilidad de agentes — Según capacidades habilitadas | ⚠️ | Precisar: la plataforma Agent ID (blueprints e identidades) está disponible para todo cliente Entra; CA, ID Protection, gobierno y controles de red para agentes requieren **Agent 365** (incluido en E7; add-on sobre E5/A5/Business Premium o Defender Suite + Purview Suite). | https://learn.microsoft.com/en-us/entra/agent-id/what-is-microsoft-entra-agent-id ; https://learn.microsoft.com/en-us/entra/global-secure-access/overview-what-is-global-secure-access | "Agent ID is available for all Microsoft Entra customers"; "Extending Microsoft Entra security features to agents requires Microsoft Agent 365". |
| ENT-13 | Entra External ID | Identidad de clientes, socios y externos — Consumo separado | ✅ | Matiz: pay-as-you-go por MAU con suscripción Azure vinculada; primeros 50.000 MAU gratis. El gobierno de invitados con ID Governance también se factura por MAU. | https://www.microsoft.com/en-us/security/microsoft-entra-pricing ; https://learn.microsoft.com/en-us/entra/id-governance/licensing-fundamentals | External ID: "Pay-as-you-go Azure subscription required"; gratis hasta 50.000 MAU. |
| ENT-14 | Entra Verified ID | Credenciales verificables y prueba de identidad — E7 / Add-on | ⚠️ | Cambiar a "Base: incluida con Entra ID P1/P2 (E3/E5/E7), 50.000 transacciones/mes gratis; Face Check (premium): Entra Suite/E7 o pay-as-you-go vía Azure". | https://www.microsoft.com/en-us/security/microsoft-entra-pricing ; https://learn.microsoft.com/en-us/entra/verified-id/verified-id-pricing | P1 lista "Verifiable credentials issuance and verification"; Face Check incluido en Entra Suite o pago por verificación. |
| ENT-15 | Entra Internet Access | SWG centrado en identidad — E7 / Add-on | ⚠️ | Agregar: "Internet Access for Microsoft services" (perfil de tráfico Microsoft: compliant network, Universal Tenant Restrictions, source IP restoration) está incluido en Entra ID P1/P2 (E3+). El SWG completo (filtrado web, TLS inspection, threat intel, prompt injection) requiere Entra Suite (E7) o licencia standalone; requiere P1/P2. | https://learn.microsoft.com/en-us/entra/global-secure-access/overview-what-is-global-secure-access | Internet Access for Microsoft services: "capabilities are included in a Microsoft Entra ID P1 or ... P2 license". |
| ENT-16 | Entra Private Access | ZTNA para apps privadas — E7 / Add-on | ✅ | Matiz: requiere P1/P2; en Entra Suite o standalone. | https://learn.microsoft.com/en-us/entra/global-secure-access/overview-what-is-global-secure-access | "Private Access capabilities are included in the Microsoft Entra Suite license and standalone". |
| ENT-17 | Entra Global Secure Access | Plataforma que integra Internet y Private Access — E7 / Add-on | ✅ | Matiz: GSA es el término unificador y la consola; hoy se vende un standalone "Microsoft Entra Global Secure Access" (US$10/usuario/mes); el perfil de tráfico Microsoft ya viene con P1. | https://learn.microsoft.com/en-us/entra/global-secure-access/overview-what-is-global-secure-access ; https://www.microsoft.com/en-us/security/microsoft-entra-pricing | "Global Secure Access is the unifying term used for both" Internet y Private Access; precio standalone US$10. |
| ENT-18 | Microsoft Authenticator | MFA y passwordless — Capacidades base y avanzadas | ✅ | Matiz: MFA disponible desde Entra ID Free; CA con MFA y passwordless/phishing-resistant listados en P1. | https://www.microsoft.com/en-us/security/microsoft-entra-pricing | Free: "MFA, unlimited SSO, and password self-service"; P1: "Passwordless and phishing-resistant authentication". |
| ENT-19 | Windows Hello for Business | Autenticación resistente al phishing — Windows / Entra | ✅ | — | https://www.microsoft.com/en-us/microsoft-365/enterprise/microsoft-365-plans-and-pricing | La comparativa marca WHfB como incluido en E7, E5 y E3. |
| ENT-F01 | Fuente citada: learn.microsoft.com/en-us/entra/ | Respalda que Entra ID, Agent ID, ID Governance, External ID, Internet Access, Private Access, Verified ID y Workload ID son componentes diferenciados | ✅ | Agregar ID Protection, que el hub también lista por separado. | https://learn.microsoft.com/en-us/entra/ | El hub lista cada producto con su propia sección, incluido "Microsoft Entra Agent ID". |
| ENT-F02 | Fuente citada: entra/architecture/deployment-scenario-intro | Ídem | ⚠️ | La página existe pero es la introducción a escenarios de **Entra Suite** (ID Protection, ID Governance, Verified ID premium, Internet Access y Private Access); no menciona Agent ID, External ID ni Workload ID. Reemplazar o complementar con https://learn.microsoft.com/en-us/entra/id-governance/licensing-fundamentals y el hub /entra/. | https://learn.microsoft.com/en-us/entra/architecture/deployment-scenario-intro | Título: "Microsoft Entra Suite deployment scenarios introduction" (actualizada 10-jul-2024). |

## A.3 Microsoft Defender (1.B)

| ID | Ítem | Afirmación del borrador | Val. | Corrección aplicada | Fuente(s) | Evidencia |
|---|---|---|---|---|---|---|
| DEF-01 | Microsoft Defender XDR | Correlación entre endpoints, identidades, correo y apps · **E5/E7** | ⚠️ | Descripción correcta, disponibilidad incompleta. El acceso a Defender XDR (portal unificado) no exige E5/E7: lo habilita **cualquiera** de: M365 E5/A5; M365 E3 + **Microsoft Defender Suite**; M365 E3 + EMS E5; Windows 10/11 Enterprise E5/A5; EMS E5/A5; O365 E5/A5; MDE; Defender for IoT (Enterprise IoT); MDI; MDA o Cloud App Discovery; MDO P2; M365 Business Premium; Defender for Business. Las señales correlacionadas dependen de las licencias. *Automatic attack disruption* y *Threat analytics* requieren MDE P2. Texto sugerido: «Incluido sin costo adicional con E5/E7 y otras licencias Defender calificadas; alcance según cargas licenciadas». | https://learn.microsoft.com/en-us/defender-xdr/prerequisites (actualizada 08/07/2026) | Lista de licencias que dan acceso "without any additional cost"; nota: attack disruption "requires Microsoft Defender for Endpoint Plan 2". |
| DEF-02 | Defender for Endpoint P1 | Prevención y reducción de superficie de ataque · **E3** | ✅ | Opcional: "M365 E3/A3/G3 o standalone". Los servidores requieren licencia aparte (Defender for Servers P1/P2 o MDE for Servers). | https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-defender-service-description (actualizada 10/29/2026); https://learn.microsoft.com/en-us/defender-endpoint/minimum-requirements | MDE P1 "standalone user subscription license and as part of Microsoft 365 E3/A3/G3"; P1 = antimalware de nueva generación, ASR, device control, firewall, network protection, application control. MDE P1/P2 "don't include server licenses". |
| DEF-03 | Defender for Endpoint P2 | EDR, investigación y respuesta avanzadas · **E5/E7** | ✅ | Opcional: añadir Windows 10/11 Enterprise E5/A5, Microsoft Defender Suite y standalone. | Service description Defender (URL de B-02); https://www.microsoft.com/en-us/microsoft-365/enterprise/e7 (ya verificado) | P2 suma EDR, investigación y remediación automatizadas, sandbox, threat analytics; incluido en M365 E5/A5/G5, Windows E5 y Defender Suite. |
| DEF-04 | Microsoft Defender Antivirus | Antivirus y antimalware · **Windows** | ✅ | Opcional: "integrado en Windows 10/11 y Windows Server; componente de protección de nueva generación de MDE". (Nota fuera de alcance: la sección 3 del borrador usa el nombre antiguo "Windows Defender Antivirus".) | https://learn.microsoft.com/en-us/defender-endpoint/microsoft-defender-antivirus-windows (actualizada 10/05/2026) | "Microsoft Defender Antivirus is built into Windows"; disponible en Windows 10/11 y versiones de Windows Server. |
| DEF-05 | Defender Vulnerability Management (MDVM) | Evaluación y priorización de vulnerabilidades · **Capacidades base / Add-on** | ⚠️ | Incompleto. Hay **tres** vías: (1) **Core** incluido en MDE P2 (E5/E7); (2) **Premium** como *add-on* para MDE P2 / M365 E5 / Defender Suite / Windows E5; (3) **Standalone** (core + premium) para clientes con MDE P1/M365 E3 u otro EDR. Para servidores: Defender for Servers P1 incluye capacidades básicas y **P2 incluye las premium**. No disponible para Defender for Business. Desde nov-2025 (preview) la sección de VM vive bajo *Exposure management* en el portal. | Service description Defender (URL de B-02); https://learn.microsoft.com/en-us/defender-vulnerability-management/defender-vulnerability-management-capabilities (actualizada 01/21/2026); https://learn.microsoft.com/en-us/defender-endpoint/whats-new-in-microsoft-defender-endpoint | "core and premium capabilities are available as a standalone user subscription license"; premium "available to server devices with Microsoft Defender for Servers Plan 2"; "Vulnerability management moves under Exposure management" (nov-2025). |
| DEF-06 | Defender for Office 365 P1 | Protección avanzada de correo y colaboración · **E3, según plan** | ✅ | Correcto **desde el 1-jul-2026**: MDO P1 se incluye en Microsoft 365 E3 y Office 365 E3 (además de Business Premium y standalone). Sugerido: quitar "según plan" y poner "M365/O365 E3 (desde 1-jul-2026), Business Premium". Ajustar también la tabla 7 del borrador. | https://learn.microsoft.com/en-us/office365/servicedescriptions/office-365-advanced-threat-protection-service-description (actualizada 07/17/2026); service description Defender (URL de B-02) | desde el 1-jul-2026, "Plan 1 is included with Office 365 E3 and Microsoft 365 E3"; no incluye capacidades de Plan 2. |
| DEF-07 | Defender for Office 365 P2 | Investigación, automatización y protección avanzada · **E5/E7** | ✅ | Opcional: añadir O365 E5, Microsoft Defender Suite y standalone. | Service description MDO y Defender (URLs de B-06/B-02) | P2 = P1 + Threat Trackers, Campaign Views, Explorer, AIR, Attack simulation training, integración con Defender XDR; incluido en M365 E5/A5/G5 y O365 E5. |
| DEF-08 | Exchange Online Protection (EOP) | Antispam y antimalware · **Exchange Online** | 🕒 | Función y disponibilidad correctas, **nombre desactualizado** en la documentación 2026: Learn lo titula "**Built-in security features for (all) cloud mailboxes**" (seguridad integrada de buzones en la nube) y el EOP standalone para on-premises figura como "Built-in security add-on for on-premises mailboxes". Sugerido: «Seguridad integrada de buzones en la nube (antes EOP): antimalware, antispam y anti-phishing/anti-spoofing; incluida en todo buzón de Exchange Online; add-on para Exchange on-premises». | https://learn.microsoft.com/en-us/defender-office-365/eop-about (actualizada 01/28/2026); https://learn.microsoft.com/en-us/office365/servicedescriptions/exchange-online-protection-service-description/exchange-online-protection-service-description (vista en resultados de búsqueda) | "included in all organizations with cloud mailboxes"; políticas por defecto: anti-malware, anti-spam y anti-phishing (spoofing); "available as an add-on for Exchange on-premises mailboxes". |
| DEF-09 | Defender for Identity (MDI) | Ataques a identidades híbridas · **E5/E7** | ✅ | Opcional: añadir EMS E5/A5, Microsoft Defender Suite y standalone. | Service description Defender (URL de B-02) | MDI "helps protect enterprise hybrid environments"; incluido en EMS E5/A5, M365 E5/A5/G5, Defender Suite; también standalone. |
| DEF-10 | Defender for Cloud Apps (MDA) | CASB, descubrimiento y control de apps cloud · **E5/E7** | ✅ | Opcional: añadir EMS E5, Defender Suite, Purview Suite y standalone; App Control (Conditional Access App Control) requiere además Entra ID P1. Learn hoy lo define como solución de seguridad SaaS (descubrimiento, postura, gobierno app-to-app, IA generativa). | Service description Defender (URL de B-02) | MDA "available as a standalone license" y en EMS E5, M365 E5/A5/G5, Defender Suite, Purview Suite; CA App Control requiere Entra ID P1. |
| DEF-11 | Defender for IoT | Seguridad y visibilidad IoT/OT · **Azure / Separado** | ⚠️ | Parcial. **OT**: licencia **por sitio** (tallas XS–XL, anual) comprada en el **Microsoft 365 admin center**; los planes legados de Azure (ACR) deben migrarse; gestión en Azure portal y, en preview, en el portal de Defender. **Enterprise IoT**: incluido en **M365 E5 / E5 Security (Defender Suite)** — 5 dispositivos por licencia — y add-on por dispositivo para clientes MDE P2. La página de E7 lista "Defender for IoT". Sugerido: «OT: licencia por sitio (M365 admin center); Enterprise IoT: incluido en E5/E7 (5 disp./licencia) + add-on». | https://learn.microsoft.com/en-us/azure/defender-for-iot/organizations/billing (07/05/2026); https://learn.microsoft.com/en-us/azure/defender-for-iot/organizations/license-and-trial-license-extention (07/05/2026, en resultados); https://learn.microsoft.com/en-us/defender-for-iot/manage-license (08/08/2026, en resultados); https://learn.microsoft.com/en-us/defender-xdr/prerequisites | "OT monitoring is billed using site-based licenses"; Enterprise IoT "supports 5 devices per Microsoft 365 E5 (ME5) or E5 Security license"; "The legacy ACR license can be migrated to the new Microsoft 365 license". |
| DEF-12 | Microsoft Security Exposure Management (MSEM) | Exposición y rutas de ataque · **Según capacidades/licencias** | ⚠️ | Correcto pero vago: **no tiene licencia propia**; viene incluido en el portal de Defender con M365 E5, M365 E3 + add-ons, licencias Microsoft Defender Suite y otras licencias calificadas; el valor depende de las cargas conectadas (Defender CSPM, MDVM). Excepción: **conectores de datos externos** (preview gratis; costo por consumo al pasar a GA). Solo nube pública (no disponible en nubes soberanas/US Gov). Sugerido: «Incluido con licencias Defender calificadas (E5/E7); conectores de terceros por consumo». | https://learn.microsoft.com/en-us/security-exposure-management/prerequisites (actualizada 07/26/2026) | Licencias: "Microsoft 365 E5", "E3 with certain add-ons", "Microsoft Defender suite licenses"; conectores externos "separate consumption-based pricing". |
| DEF-13 | Microsoft Defender External Attack Surface Management (Defender EASM) | Activos expuestos a Internet · **Separado** | ✅ | Correcto: sigue vigente como **recurso de Azure** facturado por **activos facturables** (prueba gratuita de 30 días); no se encontró aviso de retiro. Matiz útil: MSEM ofrece una **iniciativa EASM** con *pre-built footprint* sin suscripción MDEASM completa, o integración total con el recurso EASM. | https://learn.microsoft.com/en-us/azure/external-attack-surface-management/ ; https://learn.microsoft.com/en-us/azure/external-attack-surface-management/overview (04/24/2026, en resultados); https://learn.microsoft.com/en-us/security-exposure-management/external-attack-surface-management-initiative (en resultados de búsqueda) | Hub EASM con "Understand billable assets" y "Create a Defender EASM Azure resource"; iniciativa MSEM: footprint predefinido "without requiring a full MDEASM subscription". |
| DEF-14 | Microsoft Defender Threat Intelligence (MDTI) | Inteligencia de amenazas · **Según oferta vigente** | 🕒 | **Retirado como producto standalone el 1-ago-2026** y fusionado en Microsoft Defender (portal) y Sentinel. La inteligencia pública de Microsoft está disponible para clientes de Defender XDR **sin costo adicional** (Threat intelligence > Intel explorer, Threat analytics, Intel profiles). Sugerido: reemplazar por "Microsoft Threat Intelligence en Defender/Sentinel (incluido)" y, para servicio experto, "Defender Experts Threat Intelligence". | https://learn.microsoft.com/en-us/defender-xdr/threat-intelligence-explorer (actualizada 09/23/2026); https://learn.microsoft.com/en-ca/defender/threat-intelligence/learn-how-to-access-microsoft-defender-threat-intelligence-and-make-customizations-in-your-portal (en resultados de búsqueda); https://techcommunity.microsoft.com/blog/microsoftthreatprotectionblog/mdti-is-converging-into-microsoft-sentinel-and-defender-xdr/4427991 (22-jul-2025; no abrió; visto en resultados de búsqueda) | "legacy standalone Microsoft Threat Intelligence portal ... retired on August 1, 2026"; datos "available to Microsoft Defender XDR customers at no additional cost". |
| DEF-15 | Microsoft Security Copilot | IA para operaciones de seguridad · **Según licencia/capacidad** | ⚠️ | Correcto pero incompleto: **incluido en M365 E5 y E7** con capacidad por defecto auto-aprovisionada — **400 SCU/mes por cada 1.000 licencias, tope 10.000 SCU/mes** (despliegue por fases desde 18-nov-2025). Sin E5/E7: SCU **aprovisionadas** (mín. 1, facturación por hora) + **overage** por uso (con tope opcional). Sugerido: «Incluido en E5/E7 (400 SCU/1.000 lic./mes, máx. 10.000) + SCU aprovisionadas/overage». | https://learn.microsoft.com/en-us/copilot/security/security-compute-units-capacity (04/29/2026); https://learn.microsoft.com/en-us/copilot/security/auto-provisioning-security-copilot (en resultados de búsqueda); https://www.microsoft.com/en-us/security/security-copilot-in-microsoft-365-e5 (en resultados de búsqueda); E7 (ya verificado) | "For eligible and onboarded Microsoft 365 E5 customers, Security Copilot is auto provisioned"; "400 Security Compute Units (SCUs) per month for every 1000 user licenses, up to 10,000". |
| DEF-16 | Defender Experts MDR | Detección y respuesta administradas · **Servicio separado** | ✅ | Opcional: indicar **Plan 1** (cargas Defender; ex "Defender Experts for XDR") y **Plan 2** (+ fuentes de terceros vía Sentinel; requiere Sentinel y mín. 1.500 asientos). También se vende dentro de **Defender Experts Suite**. | https://learn.microsoft.com/en-us/defender-xdr/defender-experts/defender-experts-mdr-overview (08/07/2026) | "sold separately from other Microsoft Defender products"; "Plan 1 is the service previously offered as Defender Experts for XDR". |
| DEF-17 | Defender Experts Hunting | Threat hunting administrado · **Servicio separado** | ✅ | Opcional: dos ofertas standalone — **Hunting – XDR** y **Hunting – Servers**; además viene incluido en MDR Plan 1 y en Defender Experts for Servers. | https://learn.microsoft.com/en-us/defender-xdr/defender-experts/defender-experts-overview (07/27/2026) | "Two standalone offerings are available: Defender Experts Hunting - XDR ... Hunting - Servers". |
| DEF-18 | Defender Experts Cybersecurity Incident Response | Preparación y respuesta ante incidentes · **Servicio separado** | ✅ | Opcional: aclarar que es la marca vigente de **Microsoft Incident Response (ex DART)**: la página oficial conserva el título "Microsoft Incident Response" y su encabezado es "Microsoft Defender Experts Cybersecurity Incident Response". Servicio profesional con contrato propio. | Overview Defender Experts (URL de B-17); https://www.microsoft.com/en-us/security/business/microsoft-defender-experts-cybersecurity-incident-response (en resultados de búsqueda) | "This service requires a separate contract"; ciclo completo preparar/responder/recuperar en Microsoft 365, Azure y Windows. |
| DEF-19 | Párrafo de cierre 1.B | "Microsoft diferencia explícitamente Defender for Endpoint, Office 365, Identity, Cloud Apps, Vulnerability Management, IoT, Sentinel y Defender for Cloud" + 2 citas | ⚠️ | El contenido lo respalda **solo** https://learn.microsoft.com/en-us/defender/ (hub que lista Defender XDR, MDE, MDO, MDI, MDA, MDVM, Defender for IoT y Sentinel; MSEM y Defender for Cloud figuran en "Other content"). La 2.ª cita (Defender Experts overview) **no** respalda esa frase: moverla a las filas de Defender Experts. Sugerido: añadir Defender XDR y Security Exposure Management a la enumeración. | https://learn.microsoft.com/en-us/defender/ ; https://learn.microsoft.com/en-us/defender-xdr/defender-experts/defender-experts-overview | El hub enumera las cargas por separado; la página de Experts solo describe la suite de servicios. |

## A.4 Microsoft Purview (1.C)

| ID | Ítem | Afirmación del borrador | Val. | Corrección aplicada | Fuente(s) | Evidencia |
|---|---|---|---|---|---|---|
| PUR-01 | Purview Information Protection | Clasificación, etiquetado y cifrado — E3/E5/E7 | ⚠️ | Separar niveles: **E3** = núcleo (etiquetado manual/por defecto/obligatorio en apps M365, cifrado por etiqueta, Message Encryption básico). **E5/E7 o add-on sobre E3** (Purview Suite o E5 Information Protection & Governance) = avanzado: auto-etiquetado cliente/servicio, Content/Activity Explorer, Advanced Message Encryption, Customer Key, Double Key Encryption (DKE también con EMS E5). Etiquetado/protección de **fuentes no-M365** (Data Map, Fabric, etc.) = **pay-as-you-go** (*At Rest Protection*, por activo/día). | https://www.microsoft.com/licensing/guidance/Microsoft-Purview ; https://learn.microsoft.com/zh-cn/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description (SD en zh-CN, misma SD traducida, act. 2026-08-03; la versión en-US se trunca en el lector) ; https://learn.microsoft.com/en-us/purview/purview-billing-models ; https://azure.microsoft.com/en-us/pricing/details/purview/ | LIC: núcleo E3 = "manual, default, and mandatory sensitivity labeling in Microsoft 365 apps". SD (zh-CN): auto-etiquetado cliente+servicio solo E5/Purview Suite/IP&G/O365 E5; DKE en E5/Purview Suite/IP&G/EMS E5; Content & Activity Explorer requieren E5 (E3 solo agrega datos). BILL: PAYG para etiquetas en fuentes no-M365. |
| PUR-02 | Sensitivity Labels | Etiquetas de sensibilidad y protección — E3+ | ✅ | Matiz: E3+ cubre etiquetado manual/por defecto/obligatorio (incl. cifrado por etiqueta). Requieren E5/add-on: auto-etiquetado (C03), etiqueta por defecto en bibliotecas SharePoint, marcas de agua dinámicas, etiquetado de reuniones (Teams además requiere Teams Premium). | https://www.microsoft.com/licensing/guidance/Microsoft-Purview ; https://learn.microsoft.com/zh-cn/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description ; https://learn.microsoft.com/en-us/purview/get-started-with-sensitivity-labels | SD (zh-CN): etiquetado manual = Sí en M365 E3/E5/F1/F3/Business Premium, O365 E3/E5, EMS E3/E5, AIP P1/P2. SL-GS: los requisitos dependen de la funcionalidad y los admins también necesitan licencia. |
| PUR-03 | Automatic Labeling | Clasificación y etiquetado automatizado — E5/E7 / Add-on | ✅ | Precisar add-on: **Microsoft Purview Suite** (ex Microsoft 365 E5 Compliance) o **E5 Information Protection & Governance**, sobre E3 (también O365 E5; EMS E5 solo cliente). Auto-etiquetado de activos no-M365 (Data Map) = pay-as-you-go. | https://learn.microsoft.com/zh-cn/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description ; https://www.microsoft.com/licensing/guidance/Microsoft-Purview ; https://learn.microsoft.com/en-us/purview/purview-billing-models | SD (zh-CN): auto-etiquetado de cliente y de servicio = Sí en M365 E5, Purview Suite, Defender + Purview Suite FLW, E5 IP&G y O365 E5; EMS E5 solo del lado cliente. BILL: auto-labeling sobre Azure SQL/ADLS/Blob se cobra por activo/día. |
| PUR-04 | Purview Data Loss Prevention | Prevención de fuga — E3/E5/E7 | ⚠️ | **E3**: DLP solo para Exchange, SharePoint y OneDrive. **E5/E7 o add-on** (Purview Suite / IP&G): DLP para Teams, Endpoint DLP, policy tips avanzados en Outlook, DLP para impedir que Copilot procese archivos/correos. DLP de *prompts* de Copilot: todos los usuarios de Copilot. **Licencia de nivel E5 + pay-as-you-go**: DLP de red (GA sep-2026 con Entra Global Secure Access) y DLP en Edge for Business hacia apps no gestionadas (*In Transit Protection*, por requests). | https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description ; https://www.microsoft.com/licensing/guidance/Microsoft-Purview ; https://azure.microsoft.com/en-us/pricing/details/purview/ ; https://learn.microsoft.com/en-us/purview/whats-new | SD: DLP EXO/SPO/ODB incluido en M365 E3/E5; DLP Teams solo E5/Purview Suite/IP&G/O365 E5; red = "pay-as-you-go capabilities"; navegador a apps no gestionadas "is a pay-as-you-go capability". Precios Azure: In Transit Protection por 10K requests. |
| PUR-05 | Endpoint DLP | Protección en dispositivos — E5/E7 / Add-on | ✅ | Add-on = Purview Suite o E5 IP&G. Nota: Office 365 E5 **no** figura en la tabla de Endpoint DLP. Cubre Windows 10/11 y macOS. | https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description | SD: Endpoint DLP = M365 E5/A5/G5, Purview Suite, Defender + Purview Suite FLW, E5 IP&G; Windows 10, 11 y macOS. |
| PUR-06 | Purview Data Security Posture Management (DSPM) | Visibilidad y evaluación de exposición de datos — Según oferta y consumo | ⚠️ | Actualizar estado y licenciamiento: la **nueva versión de DSPM es GA desde mayo-2026** y unifica el DSPM anterior y **DSPM for AI** (ambos pasan a "classic"). Licencia base: la página del nuevo DSPM solo exige "a supporting license" y remite a la SD (sin SKU explícito); DSPM classic requería **M365 E5 o Purview Suite**. Componentes con costo adicional: apps de IA distintas de M365 Copilot (pay-as-you-go), *proactive AI insights* vía DSI (pay-as-you-go), Security Copilot (SCU); fuentes no-Microsoft (GCP, Snowflake, Databricks, Salesforce) vía partners + Sentinel data lake **siguen en preview**. Sugerido: "E5/E7 o Purview Suite + PAYG para IA no-M365 y extensiones". | https://learn.microsoft.com/en-us/purview/whats-new ; https://learn.microsoft.com/en-us/purview/data-security-posture-management-learn-about ; https://learn.microsoft.com/en-us/purview/data-security-posture-management-get-started ; https://learn.microsoft.com/en-us/purview/data-security-posture-management-considerations ; https://learn.microsoft.com/en-us/purview/dspm-for-ai-considerations | WN (mayo-2026): "new version of Data Security Posture Management is now generally available"; partners y Posture Agent siguen en preview. DSPM: versiones previas renombradas "DSPM (classic)" y "DSPM for AI (classic)". DSPM-C: requiere "Microsoft 365 E5 or Microsoft Purview Suite". DSPM4AI-C: PAYG para apps de IA distintas de M365 Copilot. Nota: P-ALL (05/15/2026) aún decía "Now in preview" (desfasada). |
| PUR-07 | Purview Data Security Investigations (DSI) | Investigación de incidentes de datos — Según licencia | ❌ | **No es por licencia**: DSI se factura solo por consumo (pay-as-you-go vía Azure): **almacenamiento (GB/mes)** + **DSI Compute Units** para análisis de IA. Prerrequisitos: suscripción y resource group de Azure en el mismo tenant, Global Admin para configurar, rol Owner/Contributor del RG. Los *proactive AI insights* de DSPM generan costo continuo. | https://learn.microsoft.com/en-us/purview/data-security-investigations-billing ; https://learn.microsoft.com/en-us/purview/data-security-investigations ; https://learn.microsoft.com/en-us/purview/purview-billing-models | DSI-B: billing "isn't based on a dedicated enterprise plan or license"; storage meter y compute units PAYG. DSI (06/22/2026): "you don't need a dedicated enterprise plan or license". |
| PUR-08 | Purview Insider Risk Management (IRM) | Riesgos internos — E5/E7 | ✅ | Agregar add-ons: **Purview Suite** o **E5 Insider Risk Management** (sobre E3). Indicadores para fuentes no-M365 (Box, Dropbox, Google Drive, AWS, Azure, Fabric/Power BI) y de IA generativa = **pay-as-you-go** (data security processing units). *Forensic Evidence* = add-on de capacidad (bloques de 100 GB/mes). Incluye Adaptive Protection (ver Omisiones). | https://www.microsoft.com/licensing/guidance/Microsoft-Purview ; https://learn.microsoft.com/zh-cn/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description ; https://learn.microsoft.com/en-us/purview/purview-billing-models ; https://azure.microsoft.com/en-us/pricing/details/purview/ | LIC: IRM en M365 E5, Purview Suite, Defender + Purview Suite FLW y E5 IRM. SD (zh-CN): Forensic Evidence se compra en unidades de 100 GB/mes. BILL: indicadores no-M365 "are billed on data security processing units". |
| PUR-09 | Purview Information Barriers (IB) | Restricción de colaboración entre grupos — E5/E7 | ✅ | Agregar add-ons: **Purview Suite** o **E5 Insider Risk Management**. Requieren licencia los usuarios de los segmentos asignados en la política. | https://www.microsoft.com/licensing/guidance/Microsoft-Purview ; https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description | LIC: IB marcado en M365 E5, Purview Suite, Defender + Purview Suite FLW y E5 IRM (no en IP&G ni eDiscovery & Audit). SD: usuarios en "Assigned Segments" requieren licencia. |
| PUR-10 | Purview Communication Compliance | Supervisión de comunicaciones — E5/E7 | ✅ | Agregar: también **Office 365 E5**, **Purview Suite** y **E5 IRM**. Análisis de prompts/respuestas de M365 Copilot requiere E5 (o Purview Suite) **+ licencia Copilot**. Interacciones con IA no-M365 = pay-as-you-go (text records). | https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description ; https://learn.microsoft.com/en-us/purview/purview-billing-models | SD: CC = M365 E5, Purview Suite, E5 IRM, O365 E5; Copilot prompt/response solo con "+ Microsoft Copilot". BILL: CC para IA no-M365 por "Number of text records scanned". |
| PUR-11 | Purview Audit (Standard) | Registro y consulta de actividades — E3/E5/E7 | ✅ | Agregar: retención **180 días** (desde 17-oct-2023; antes 90). También en Business Basic/Standard/Premium y F1/F3. Auditoría de interacciones con IA **no-Microsoft** = pay-as-you-go. | https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description ; https://learn.microsoft.com/en-us/purview/audit-solutions-overview ; https://learn.microsoft.com/en-us/purview/purview-billing-models | SD: Audit (Standard) = Yes en M365 E3/F1/F3 y Business. AUD: "In Audit (Standard), the system retains records for 180 days". |
| PUR-12 | Purview Audit (Premium) | Auditoría avanzada y retención ampliada — E5/E7 | ✅ | Agregar add-ons: **Purview Suite** o **E5 eDiscovery & Audit**; también O365 E5. Retención por defecto **1 año** (Entra ID, Exchange, OneDrive, SharePoint); hasta **10 años** con add-on por usuario *10-Year Audit Log Retention*. | https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description ; https://learn.microsoft.com/en-us/purview/audit-solutions-overview | SD: Audit (Premium) en M365 E5, O365 E5, Purview Suite, E5 eDiscovery & Audit. AUD: 10 años requiere "an additional per-user add-on license". |
| PUR-13 | Purview eDiscovery | Evidencia electrónica — E3/E5/E7 | ⚠️ | Distinguir: **eDiscovery (Standard)** en E3/E5/E7 (casos, búsqueda, hold, export); **eDiscovery (Premium)** (custodios, review sets, analítica, legal hold notifications) solo en **E5/E7, O365 E5 o add-on** (Purview Suite o E5 eDiscovery & Audit, sobre M365 E3 u O365 E3 + EMS E3). La experiencia es **unificada** en el portal Purview (Content Search integrado como componente de eDiscovery). **Pay-as-you-go**: almacenamiento de datos de IA no-M365 y Graph Export API para tenants con eDiscovery E3. | https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description ; https://learn.microsoft.com/en-us/purview/edisc ; https://learn.microsoft.com/en-us/purview/edisc-get-started ; https://learn.microsoft.com/en-us/purview/purview-portal ; https://www.microsoft.com/licensing/guidance/Microsoft-Purview ; https://learn.microsoft.com/en-us/purview/edisc-billing (resultado de búsqueda) ; https://learn.microsoft.com/en-us/purview/purview-billing-models | SD: eDiscovery (premium) = Sí en M365 E5, Purview Suite, E5 eDiscovery & Audit y O365 E5; "No" en M365 E3/O365 E3. EDISC (06/29/2026): premium con E5 "or related E5 add-on subscriptions". PORTAL: "Content Search features are now included as core components in eDiscovery". BILL: storage de IA no-M365 y Export API para "Standard licensed tenants" = PAYG. |
| PUR-14 | Purview Data Lifecycle Management (DLM) | Retención y eliminación — E3/E5/E7 | ✅ | Matiz: **E3** = políticas de retención org-wide/por ubicación y etiquetas de retención manuales. **E5/E7 o add-on** (Purview Suite / IP&G): ámbitos adaptativos, auto-aplicación de etiquetas (SIT, keywords, trainable classifiers), etiqueta por defecto en bibliotecas, *priority cleanup*. Retención de interacciones con IA **no-M365** = pay-as-you-go. | https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description ; https://www.microsoft.com/licensing/guidance/Microsoft-Purview ; https://learn.microsoft.com/en-us/purview/purview-billing-models | LIC: núcleo E3 = "manual retention labels and basic org-wide or location-wide retention policies". SD: ámbitos adaptativos y auto-apply requieren E5/Purview Suite/IP&G/O365 E5. |
| PUR-15 | Purview Records Management | Gestión avanzada de registros — E5/E7 | ✅ | Agregar add-ons (Purview Suite / E5 IP&G) y O365 E5. Funciones que lo requieren: declarar *record*/*regulatory record*, retención basada en eventos, *disposition review*, file plan. | https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description | SD: event-based, disposition review y "mark items as a record or a regulatory record" requieren M365 E5, Purview Suite, O365 E5 o E5 IP&G. |
| PUR-16 | Purview Compliance Manager | Evaluación de controles — Capacidades base / Add-on | ✅ | Precisar: todos los niveles incluyen la plantilla **Microsoft Data Protection Baseline**; **E5/A5/G5** suman **3 plantillas premium gratis**; el resto (incl. *Premium AI templates*: EU AI Act, ISO 42001, NIST AI RMF) se compra **por plantilla** (licencia anual). Más de 360 plantillas; soporte multicloud. | https://learn.microsoft.com/en-us/purview/compliance-manager-regulations-list ; https://learn.microsoft.com/en-us/purview/compliance-manager-regulations ; https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description ; https://learn.microsoft.com/en-us/purview/purview-compliance | CM-LIST: E5 "can choose any three premium regulations to use for free". CM-REG: premium "require purchase of a license"; licencias "good for one year". SD: disponible con licencias O365/M365 (incl. Business Premium). |
| PUR-17 | Purview Data Map | Inventario y metadatos — Azure / Consumo | ⚠️ | Matizar: en el **modelo vigente** (pay-as-you-go desde 6-ene-2025, portal Purview) el escaneo/población del Data Map **no se cobra** para clientes de Unified Catalog que aceptaron el nuevo modelo o pasaron a *enterprise tier*; el costo se genera en Unified Catalog (activos gobernados + DGPU) y en extras como *Advanced Resource Set* (vCore-hora). El esquema de **Capacity Units + vCore-hora de escaneo** corresponde a **Azure Purview (Classic)**. Existe versión **gratuita** limitada (live view). Facturación vía suscripción de Azure. Etiquetas/protección sobre activos del Data Map = PAYG por activo/día. | https://learn.microsoft.com/en-us/purview/data-governance-billing ; https://azure.microsoft.com/en-us/pricing/details/purview/ ; https://learn.microsoft.com/en-us/purview/purview-portal | DG-B: "Data Map and scan charges don't apply to Unified Catalog customers" tras consentir/upgrade. Precios Azure (FAQ): "In the new cost model scanning will not have an associated cost"; Capacity Unit y escaneo por vCore-hora listados bajo "Azure Purview (Classic)". |
| PUR-18 | Purview Unified Catalog | Catálogo y gobierno de datos — Azure / Consumo | ✅ | Precisar medidores: **activos gobernados únicos/día** (activos vinculados a data products, CDE, glosario, data quality) + **DGPU** (Basic/Standard/Advanced) para data quality y *health management*. Requiere suscripción + resource group de Azure en el mismo tenant. | https://learn.microsoft.com/en-us/purview/data-governance-billing ; https://learn.microsoft.com/en-us/purview/purview-billing-models ; https://azure.microsoft.com/en-us/pricing/details/purview/ | DG-B: "For Unified Catalog, you pay for governed assets and data health management capabilities"; activos no vinculados a conceptos de gobierno no cuentan. |
| PUR-19 | Purview Data Estate Insights | Análisis del patrimonio de datos — Según oferta | 🕒 | **Renombrado/reubicado**: en el portal Purview actual pasó a **Reports** dentro de *Unified Catalog > Health management* (consumo vía DGPU, SKU Basic). "Data Estate Insights (Classic)" queda como app del **Azure Purview (Classic)** (Insights Generation por vCore-hora + consumo por llamada API); los servicios clásicos de gobierno ya no aceptan clientes nuevos (*customer support mode*). Sugerido: reemplazar por "Unified Catalog – Health management (reports, data health controls)". | https://learn.microsoft.com/en-us/purview/purview-portal ; https://learn.microsoft.com/en-us/purview/legacy/concept-insights ; https://azure.microsoft.com/en-us/pricing/details/purview/ ; https://learn.microsoft.com/en-us/purview/data-governance-billing | PORTAL (08/05/2026): "Data Estate Insights is renamed to Reports and moved to Unified Catalog". Legacy: Data Catalog/Data Health Insights/Workflow (classic) "no longer taking on new customers". DG-B: reports de Health management usan SKU Basic. |
| PUR-20 | Purview Data Security for AI | Protección de datos usados por IA y agentes — Según licencia/consumo | ⚠️ | **No es nombre oficial de producto**. Usar: "Microsoft Purview data security and compliance protections for generative AI apps (Copilot, agentes y apps de IA)", con **DSPM** como puerta de entrada (DSPM for AI —ex *AI Hub*— quedó como "classic"). Licenciamiento: experiencias de **M365 Copilot** cubiertas por licencias por usuario (varias requieren E5: p. ej., DLP que impide procesar archivos; CC sobre prompts requiere E5 + Copilot); **agentes en Foundry y apps conectadas a Entra**: soportados por **Microsoft 365 E7 y Agent 365**; **apps de IA no-M365**: pay-as-you-go (DLP/clasificación de prompts, Audit, CC, DLM, eDiscovery). | https://learn.microsoft.com/en-us/purview/ai-microsoft-purview ; https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description ; https://learn.microsoft.com/en-us/purview/purview-billing-models ; https://learn.microsoft.com/en-us/purview/dspm-for-ai-considerations ; https://learn.microsoft.com/en-us/purview/whats-new | SD: capacidades para agentes en Foundry y apps Entra "will be supported by Microsoft 365 E7 and Agent365 SKUs". BILL: "Microsoft 365 Copilot experiences aren't charged"; medidor "Data Security for Gen AI Applications". WN (may-2026): GA de protecciones para Microsoft Agent 365. DSPM4AI-C: políticas creadas en preview conservan prefijo "Microsoft AI Hub". |
| PUR-21 | Nota "Purview es una familia… No todos sus componentes están incluidos en E5" | Cita purview-compliance, purview-security y purview | ⚠️ | Las 3 URLs **existen** y respaldan la estructura de familia (data security, data governance —Data Map, Unified Catalog— y data compliance). **No** afirman explícitamente que "no todo está en E5": agregar como respaldo la página de **billing models** (PAYG para datos/apps no-M365, facturación Azure), la **Licensing Guidance** y la SD. Matizar "gobierno de datos en Azure": hoy se opera en el **portal Purview** y se factura vía suscripción de Azure. Nota: purview (05/15/2026) aún marca DSPM "Now in preview", desfasado frente a What's new (GA mayo-2026). | https://learn.microsoft.com/en-us/purview/purview-compliance ; https://learn.microsoft.com/en-us/purview/purview-security ; https://learn.microsoft.com/en-us/purview/purview ; https://learn.microsoft.com/en-us/purview/purview-billing-models ; https://www.microsoft.com/licensing/guidance/Microsoft-Purview | P-ALL: lista Data Map y Unified Catalog como data governance. BILL: PAYG extiende capacidades "beyond Microsoft 365"; "billing mechanisms are Azure based". LIC: user-based para datos M365; PAYG para datos no-M365. |

## A.5 Microsoft Intune (2.A)

| ID | Ítem | Afirmación del borrador | Val. | Corrección aplicada | Fuente(s) | Evidencia |
|---|---|---|---|---|---|---|
| INT-01 | Intune Plan 1 | Gestión de dispositivos y aplicaciones | ✅ | Opcional: "Servicio base de gestión unificada de endpoints (MDM/MAM) en la nube". | https://learn.microsoft.com/en-us/intune/fundamentals/licensing | Plan 1 es "the base service": gestión unificada de dispositivos y apps en la nube. |
| INT-02 | Intune Suite | Capacidades avanzadas de administración y seguridad | ⚠️ | Descripción correcta, pero agregar: (a) es aditivo a Plan 1 e **incluye Plan 2**; (b) Learn agrupa estas funciones como "advanced capabilities"; (c) **desde jul-2026** M365 E3 incluye Remote Help, Advanced Analytics y Plan 2, y M365 E5 (y E7) suma EPM, Cloud PKI y EAM; el Suite (USD 10/usuario/mes) queda como opción sobre todo para quien no tiene E3/E5. Falta en la tabla "Intune Plan 2". | https://learn.microsoft.com/en-us/intune/fundamentals/licensing ; https://www.microsoft.com/en-us/security/microsoft-intune-pricing ; https://www.microsoft.com/en-us/licensing/news/2026-M365-Packaging-Pricing-Updates | L1: Suite "Unifies advanced endpoint management and security capabilities. Includes Plan 2." L3 (FAQ): E3 recibe Remote Help, Advanced Analytics y Plan 2; E5 suma EPM, Cloud PKI y EAM. |
| INT-03 | Intune Endpoint Privilege Management | Administración de elevaciones de privilegios locales | ✅ | Nombre oficial: "Microsoft Intune Endpoint Privilege Management". Matiz de licencia: incluido en M365 E5/E7 desde jul-2026; no incluido en E3 (add-on standalone USD 3/usuario/mes o Intune Suite). | https://learn.microsoft.com/en-us/intune/fundamentals/advanced-capabilities ; https://www.microsoft.com/en-us/security/microsoft-intune-pricing | Usuarios con mínimo privilegio que pueden ejecutar tareas aprobadas que requieren elevación. |
| INT-04 | Intune Enterprise Application Management | Administración de aplicaciones empresariales | ⚠️ | Demasiado genérica (la gestión de apps base ya está en Plan 1). Proponer: "Catálogo de apps Win32 empaquetadas y hospedadas por Microsoft (Enterprise App Catalog) para desplegarlas y actualizarlas". Incluido en M365 E5/E7 desde jul-2026. | https://learn.microsoft.com/en-us/intune/fundamentals/advanced-capabilities | "Deploy curated Win32 apps from a Microsoft-hosted Enterprise App Catalog". |
| INT-05 | Intune Advanced Analytics | Análisis avanzado de dispositivos | ✅ | Opcional: "Analítica avanzada de endpoints y experiencia de usuario (detección de anomalías, insights granulares)". Incluido en M365 E3/E5/E7 desde jul-2026. | https://learn.microsoft.com/en-us/intune/fundamentals/advanced-capabilities ; https://www.microsoft.com/en-us/security/microsoft-intune-pricing | Insights basados en analítica para mejorar la experiencia en los endpoints; L3 cita detección de anomalías. |
| INT-06 | Intune Remote Help | Asistencia remota administrada | ✅ | Opcional: "Asistencia remota en la nube para help desk, con RBAC". Incluido en M365 E3/E5/E7 desde jul-2026. | https://learn.microsoft.com/en-us/intune/fundamentals/advanced-capabilities | Conexión segura a dispositivos de usuarios para soporte con control de acceso basado en roles. |
| INT-07 | Intune Cloud PKI | Infraestructura de certificados administrada | ⚠️ | Corregir nombre: **"Microsoft Cloud PKI"** (no "Intune Cloud PKI"). Descripción correcta: CA administrada para emisión, renovación y revocación de certificados en plataformas gestionadas por Intune. Incluido en M365 E5/E7 desde jul-2026. | https://learn.microsoft.com/en-us/intune/fundamentals/advanced-capabilities ; https://www.microsoft.com/en-us/licensing/news/2026-M365-Packaging-Pricing-Updates | Learn, la página de precios y el anuncio de licencias usan "Microsoft Cloud PKI". |
| INT-08 | Intune Mobile Application Management | Protección de datos en aplicaciones móviles | ✅ | Precisar: se implementa con **app protection policies** (incluidas en Plan 1), funcionan con o sin inscripción del dispositivo (BYOD) y también existen para Windows. "Microsoft Tunnel for MAM" es Plan 2. | https://learn.microsoft.com/en-us/intune/app-management/protection/overview (solicitada como /intune/intune-service/apps/app-protection-policy; redirige) | Las políticas mantienen los datos "safe or contained in a managed app", sin requerir inscripción. |
| INT-09 | Intune Compliance Policies | Evaluación de cumplimiento de dispositivos | ✅ | Opcional: agregar que el estado de cumplimiento alimenta el Acceso Condicional de Microsoft Entra. | https://learn.microsoft.com/en-us/intune/device-security/compliance/overview (solicitada como /intune/intune-service/protect/device-compliance-get-started; redirige) | Reglas y condiciones para evaluar la configuración de los dispositivos gestionados; integración con Conditional Access. |
| INT-10 | Intune Endpoint Security Policies | Administración de antivirus, firewall y cifrado | ⚠️ | Incompleta. Las políticas de seguridad de endpoint incluyen además: protección de cuentas (Windows LAPS, pertenencia a grupos locales), App Control for Business, reducción de superficie de ataque (reglas ASR, device control, exploit protection), EDR (onboarding a Defender for Endpoint) y cifrado (BitLocker, Personal Data Encryption, FileVault). Proponer: "Antivirus, firewall, cifrado de disco, ASR, EDR, App Control y protección de cuentas". | https://learn.microsoft.com/en-us/intune/device-configuration/endpoint-security/manage-policies (solicitada como /intune/intune-service/protect/endpoint-security-policy; redirige) | Tipos de política: Account protection, Antivirus, App Control for Business, Attack surface reduction, Disk encryption, EDR, Firewall. |
| INT-11 | Windows Autopilot | Aprovisionamiento de dispositivos | ✅ | Matiz: es un conjunto de tecnologías de Windows (no un módulo de Intune) que también permite reset, repropósito y recuperación; la inscripción automática en MDM requiere Entra ID P1/P2. Considerar mencionar "Windows Autopilot device preparation" (experiencia más nueva). | https://learn.microsoft.com/en-us/autopilot/overview | "a collection of technologies used to set up and pre-configure new devices". |
| INT-12 | Windows Autopatch | Gestión automatizada de actualizaciones | ✅ | Agregar requisitos: disponible con M365 Business Premium, Windows Enterprise E3/E5 (incl. en M365 F3/E3/E5), Education A3/A5 y E3/E5 VDA; requiere Entra ID P1/P2 + Intune; dispositivos corporativos inscritos en Intune o co-gestión; las solicitudes de soporte solo están en E3+/F3. | https://learn.microsoft.com/en-us/windows/deployment/windows-autopatch/prepare/windows-autopatch-prerequisites | Lista de licencias habilitantes; "Microsoft Entra ID P1 or P2 and Microsoft Intune are required." (actualizada 26-feb-2026) |
| INT-13 | Frase Gartner | "Intune está reconocido por Gartner Peer Insights dentro de Endpoint Management Tools" | ⚠️ | La página abre y **Microsoft Intune figura** en el mercado (4,2/5; 1.144 calificaciones al 4-nov-2026), pero **no muestra el distintivo "Customers' Choice 2026"** (sí aparece en ManageEngine, Jamf, NinjaOne y Tanium). Reformular: "Microsoft Intune está listado y evaluado por usuarios en Gartner Peer Insights – Endpoint Management Tools". Evitar "reconocido" si se lee como premio y fechar la métrica. Fuente de terceros (Gartner), no de Microsoft. | https://www.gartner.com/reviews/market/endpoint-management-tools | "Microsoft Intune By Microsoft 4.2 (1144 Ratings)". |

## A.6 Seguridad de Windows (2.B)

| ID | Ítem | Afirmación del borrador | Val. | Corrección aplicada | Fuente(s) | Evidencia |
|---|---|---|---|---|---|---|
| WIN-01 | BitLocker | Cifrado de unidades | ✅ | Opcional: "Cifrado de volúmenes completos (mejor con TPM)". Disponible desde Pro; la *gestión avanzada* de BitLocker requiere Enterprise/Education. | https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/bitlocker/ ; https://learn.microsoft.com/en-us/windows/security/licensing-and-edition-requirements | "provides encryption for entire volumes". En la tabla de licencias, "BitLocker advanced management" = ❌ en Windows Pro. |
| WIN-02 | BitLocker To Go | Cifrado de unidades extraíbles | ✅ | Sin cambios. | https://support.microsoft.com/en-us/windows/security/encryption/bitlocker-drive-encryption ; https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/bitlocker/faq (vista en resultados de búsqueda, sección "BitLocker To Go") | Las unidades extraíbles aparecen como "Removable data drives - BitLocker To Go". |
| WIN-03 | Windows Defender Antivirus | Protección antimalware | 🕒 | Nombre vigente: **"Microsoft Defender Antivirus"**. Matiz: integrado en Windows (incl. Home/Pro); es el componente de protección de nueva generación de Defender for Endpoint; puede operar en modo pasivo solo en equipos incorporados a MDE. | https://learn.microsoft.com/en-us/defender-endpoint/microsoft-defender-antivirus-windows | La documentación y la tabla de licencias de Windows usan "Microsoft Defender Antivirus". |
| WIN-04 | Windows Defender Firewall | Firewall del dispositivo | 🕒 | Nombre vigente en la documentación: **"Windows Firewall"** (el servicio aún se muestra como "Windows Defender Firewall"). Matiz: firewall de host incluido y habilitado por defecto en todas las ediciones; soporta IPsec. | https://learn.microsoft.com/en-us/windows/security/operating-system-security/network-security/windows-firewall/ | "Windows Firewall is a host-based firewall ... enabled by default on all Windows editions"; nombre del servicio: "Windows Defender Firewall". |
| WIN-05 | Microsoft Defender SmartScreen | Protección contra sitios y archivos maliciosos | ✅ | Opcional: agregar "phishing" y reputación de apps. Nota: no protege archivos en recursos internos/UNC. | https://learn.microsoft.com/en-us/windows/security/operating-system-security/virus-and-threat-protection/microsoft-defender-smartscreen/ | Protege contra sitios y apps de phishing/malware y descargas potencialmente maliciosas. |
| WIN-06 | Windows Hello for Business | Autenticación passwordless | ✅ | Precisar: "Autenticación sin contraseña resistente a phishing (clave asimétrica protegida por TPM + PIN/biometría)". Disponible desde Pro. | https://learn.microsoft.com/en-us/windows/security/identity-protection/hello-for-business/ | "phish-resistant two-factor authentication"; sin secreto simétrico que pueda robarse. |
| WIN-07 | Credential Guard | Aislamiento de secretos y credenciales | ✅ | Agregar matiz: **habilitado por defecto desde Windows 11 22H2 y Windows Server 2025** (Learn lo describe para sistemas unidos a dominio que no son DC) cuando se cumplen requisitos de **licencia (Enterprise E3/E5, Education A3/A5; no Pro)** y de hardware, salvo deshabilitación explícita previa (sin UEFI lock por defecto). | https://learn.microsoft.com/en-us/windows/security/identity-protection/credential-guard/ ; https://learn.microsoft.com/en-us/windows/security/identity-protection/credential-guard/configure | Usa VBS para aislar secretos; "enabled by default on devices which meet the requirements"; Pro = No. |
| WIN-08 | Remote Credential Guard | Protección de credenciales en conexiones remotas | ✅ | Precisar: solo RDP con Kerberos hacia hosts unidos a AD; para escenarios de help desk Microsoft recomienda Restricted Admin mode. Disponible desde Pro. | https://learn.microsoft.com/en-us/windows/security/identity-protection/remote-credential-guard | Redirige las solicitudes Kerberos al dispositivo cliente; las credenciales no viajan al host remoto. |
| WIN-09 | Virtualization-Based Security | Aislamiento de componentes críticos | ✅ | Opcional: "Entorno aislado por hipervisor que aloja soluciones de seguridad (p. ej., Credential Guard, integridad de memoria)". Requisitos de hardware (guía OEM): CPU 64-bit con virtualización y SLAT, IOMMU, TPM 2.0 y Secure Boot. | https://learn.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-vbs | VBS crea un entorno virtual aislado que es raíz de confianza del SO. |
| WIN-10 | Hypervisor-Protected Code Integrity | Protección de integridad del código | ✅ | Agregar nombre en UI: **"Integridad de memoria" (Memory integrity)**; es una función de VBS que ejecuta la integridad de código en modo kernel dentro del entorno aislado. Puede tener incompatibilidades con drivers. | https://learn.microsoft.com/en-us/windows/security/hardware-security/enable-virtualization-based-protection-of-code-integrity | "Memory integrity is sometimes referred to as hypervisor-protected code integrity (HVCI)". |
| WIN-11 | App Control for Business | Control de ejecución de aplicaciones | ✅ | Agregar: ex **Windows Defender Application Control (WDAC)** / "configurable code integrity"; controla drivers y apps; es característica de seguridad bajo criterios de servicio de MSRC; disponible en todas las ediciones cliente. Nota: Intune aún rotula el perfil como "Windows Defender Application Control (WDAC)". | https://learn.microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/appcontrol-and-applocker-overview ; https://learn.microsoft.com/en-us/intune/device-configuration/endpoint-security/manage-policies | Controla "which drivers and applications are allowed to run"; diseñada como característica de seguridad según MSRC. |
| WIN-12 | AppLocker | Restricción de aplicaciones | ⚠️ | Agregar matices: (a) Microsoft recomienda **App Control for Business** cuando sea posible; (b) AppLocker **no cumple los criterios de servicio de MSRC como característica de seguridad** y ya **no recibe mejoras de funcionalidad** (solo correcciones de seguridad); (c) útil para reglas por usuario/grupo en equipos compartidos; (d) licencia: requiere Enterprise/Education (la edición Pro lo soporta técnicamente, pero la licencia Pro no lo otorga). | https://learn.microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/appcontrol-and-applocker-overview ; https://learn.microsoft.com/en-us/windows/security/licensing-and-edition-requirements | "doesn't meet the servicing criteria for being a security feature"; "isn't getting new feature improvements". |
| WIN-13 | Attack Surface Reduction Rules | Reducción de comportamientos explotables | ✅ | Agregar requisitos: son función de **Microsoft Defender Antivirus** (requiere MDAV activo, protección en tiempo real y nube); disponibles en cualquier edición con MDAV (incl. Home). No requieren E5, pero la **gestión avanzada (monitoreo, analítica y reportes en Defender XDR)** requiere E5 o equivalente; no está disponible con Windows Pro ni M365 E3. Despliegue recomendado: políticas de seguridad de endpoint de Intune (Plan 1). | https://learn.microsoft.com/en-us/defender-endpoint/attack-surface-reduction-rules-overview (solicitada como /defender-endpoint/attack-surface-reduction; redirige) | Las reglas apuntan a comportamientos de software riesgosos que explota el malware; "ASR rules don't require Microsoft 365 E5". |
| WIN-14 | Controlled Folder Access | Protección contra modificaciones no autorizadas | ✅ | Precisar: "Protección anti-ransomware: solo apps confiables pueden modificar archivos en carpetas protegidas (y sectores de arranque)". Desactivado por defecto; requiere MDAV en modo activo; misma lógica de licencias que ASR. | https://learn.microsoft.com/en-us/defender-endpoint/controlled-folder-access-overview (solicitada como /defender-endpoint/controlled-folders; redirige) | Permite "only trusted apps to change files in protected folders"; "CFA is turned off by default". |
| WIN-15 | Secure Boot | Protección de la cadena de arranque | ⚠️ | Descripción correcta, pero en nov-2026 requiere matiz: **agregar alerta 2026**: los certificados de Secure Boot de 2011 comienzan a **vencer en junio de 2026**; hay que desplegar los CA 2023 (y firmware OEM cuando aplique) para seguir recibiendo protecciones de arranque. Nombre en Learn: "Secure Boot and Trusted Boot". | https://learn.microsoft.com/en-us/troubleshoot/windows-client/windows-security/update-secure-boot-certificates (vista en resultados de búsqueda) ; https://support.microsoft.com/en-us/servicing/os/secure-boot/2025/06/windows-secure-boot-certificate-expiration-and-ca-updates (vista en resultados de búsqueda) | Certificados 2011 "will expire in June 2026"; sin actualizar, el equipo arranca pero no recibe nuevas protecciones de arranque. |
| WIN-16 | Trusted Platform Module | Protección de claves mediante hardware | ✅ | Opcional: agregar mediciones de integridad del arranque y atestación de salud del dispositivo. | https://learn.microsoft.com/en-us/windows/security/hardware-security/tpm/trusted-platform-module-overview | Cripto-procesador seguro: generar, almacenar y limitar el uso de claves; medir el arranque. |
| WIN-17 | Microsoft Pluton | Procesador de seguridad integrado en hardware compatible | ✅ | Precisar: "Cripto-procesador integrado en la CPU/SoC que puede funcionar como TPM, con firmware actualizable vía Windows Update"; solo Windows 11 en chipsets AMD/Intel/Qualcomm específicos. | https://learn.microsoft.com/en-us/windows/security/hardware-security/pluton/microsoft-pluton-security-processor | "secure crypto-processor built into the CPU"; provee la funcionalidad de TPM y más. |
| WIN-18 | Windows LAPS | Gestión de contraseñas de administrador local | ✅ | Agregar: rota y respalda la contraseña en Entra ID o AD (y DSRM en DC); sin costo; el **LAPS legado está deprecado desde Windows 11 23H2**; "Automatic Account Management" requiere Windows 11 24H2 / Server 2025. | https://learn.microsoft.com/en-us/windows-server/identity/laps/laps-overview | Gestiona y respalda automáticamente la contraseña del administrador local; legacy LAPS deprecado. |
| WIN-19 | Windows Sandbox | Entorno aislado de ejecución | ✅ | Agregar: desechable, aislado por hipervisor; ediciones **Pro, Enterprise y Education (no Home)**; la red está habilitada por defecto (conviene deshabilitarla para analizar archivos no confiables). | https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/ (solicitada como /windows-sandbox/windows-sandbox-overview; redirige) | Entorno de escritorio aislado y liviano; "not supported on Windows Home edition". |
| WIN-20 | Windows Security Baselines | Configuraciones de seguridad recomendadas | ✅ | Opcional: "Conjuntos de configuración recomendados por Microsoft (GPO vía Security Compliance Toolkit o baselines MDM en Intune)". Nota 2026: las baselines de Windows 11 24H2/25H2/26H2 habilitan **Administrator protection** por defecto desde la actualización de octubre de 2026. | https://learn.microsoft.com/en-us/windows/security/operating-system-security/device-management/windows-security-configuration-framework/windows-security-baselines ; https://learn.microsoft.com/en-us/windows/security/application-security/application-control/administrator-protection/ | "a group of Microsoft-recommended configuration settings". |
| WIN-21 | Personal Data Encryption | Protección adicional de datos personales | ⚠️ | Descripción engañosa: no es protección de "datos personales" (PII) sino **cifrado de archivos por usuario ligado a Windows Hello for Business** (claves liberadas al iniciar sesión con Hello, descartadas al cerrar sesión/bloquear); complementa BitLocker. Requisitos: Windows 11 22H2+ (carpetas conocidas: 24H2+), **Enterprise/Education** (licencias E3/E5/A3/A5), Entra joined o híbrido (no solo dominio). Proponer: "Cifrado a nivel de archivo vinculado a Windows Hello for Business". | https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/personal-data-encryption/ | "file-based data encryption"; usa Windows Hello for Business para vincular claves a credenciales; Pro = No. |
| WIN-22 | Local Security Authority Protection | Protección del proceso de autenticación | ✅ | Agregar: ejecuta LSASS como proceso protegido (evita inyección de código y lectura de memoria). Habilitada automáticamente en **instalaciones nuevas** de Windows 11 22H2+ unidas a empresa y con capacidad HVCI (no en upgrades); modo auditoría activo por defecto en 22H2+. | https://learn.microsoft.com/en-us/windows-server/security/credentials-protection-and-management/configuring-additional-lsa-protection | Habilitación automática si es instalación nueva 22H2+, "enterprise joined" y con capacidad HVCI. |
| WIN-23 | Nota final | "No todas son exclusivas de Windows Enterprise ni están habilitadas automáticamente. Dependen de edición, versión, hardware y configuración" | ✅ | Correcta. Sugerencia: cambiar el título "Windows Enterprise — Seguridad integrada" por "Seguridad integrada en Windows 11 (requisitos por edición/licencia)" y marcar por ítem qué requiere Enterprise/Education (Credential Guard, PDE, AppLocker, gestión avanzada de BitLocker) y cuáles se habilitan por defecto (Credential Guard, LSA protection, Windows Firewall, Microsoft Defender Antivirus). | https://learn.microsoft.com/en-us/windows/security/licensing-and-edition-requirements | La tabla oficial muestra la mayoría de funciones en Windows Pro y algunas solo en Enterprise/Education. |
| WIN-24 | URLs citadas en la nota | credential-guard/configure ; /windows/security/ ; appcontrol-and-applocker-overview | ✅ | Las tres URLs existen y abren (4-nov-2026). Sugerencia: agregar la página de licencias y ediciones como fuente principal de la nota. | https://learn.microsoft.com/en-us/windows/security/identity-protection/credential-guard/configure ; https://learn.microsoft.com/en-us/windows/security/ ; https://learn.microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/appcontrol-and-applocker-overview | Abiertas: "Configure Credential Guard" (act. 29-mar-2026), "Windows security documentation", "App Control and AppLocker Overview" (act. 29-mar-2026). |

## A.7 Defender for Cloud (3.A)

| ID | Ítem | Afirmación del borrador | Val. | Corrección aplicada | Fuente(s) | Evidencia |
|---|---|---|---|---|---|---|
| DFC-00 | Frase de apertura | "Defender for Cloud combina CNAPP, CSPM, DevSecOps y protección de workloads" | ⚠️ | Defender for Cloud **es** una CNAPP (la categoría paraguas, no un componente) que unifica tres componentes: **CSPM, DevSecOps y CWPP**, y suma **seguridad de IA** (AI-SPM + protección de amenazas para IA). Redactar: "Defender for Cloud es una CNAPP que unifica CSPM, DevSecOps y CWPP, además de seguridad para cargas de IA generativa". | https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-cloud-introduction | La página define a Defender for Cloud como CNAPP y dice "It has three core components" (CSPM, DevSecOps, CWPP); agrega AI security y AI threat protection "in addition to its core CNAPP capabilities". |
| DFC-01 | Defender Cloud Security Posture Management | Postura de seguridad multicloud | ❌ | **Duplica la fila A-14**: "Defender Cloud Security Posture Management (CSPM)" es el nombre largo del plan pago Defender CSPM. Reemplazar por **Foundational CSPM (gratuito)**: evaluación continua, recomendaciones, Secure Score y Microsoft cloud security benchmark (MCSB) en Azure, AWS y GCP. | https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-cloud-security-posture-management ; https://azure.microsoft.com/en-us/pricing/details/defender-for-cloud/ | Learn: "Defender for Cloud offers two CSPM plans": Foundational CSPM (free) y Defender CSPM (paid). La página de precios lista "Defender Cloud Security Posture Management (CSPM)" como el plan pago ($/recurso facturable). |
| DFC-02 | Defender for Servers Plan 1 | Servidores y máquinas virtuales | ✅ | Precisión opcional: P1 es el nivel de entrada centrado en EDR (integración con Defender for Endpoint) para Windows/Linux en Azure, AWS, GCP y on-premises. Desde el 1-nov-2026 los dispositivos cliente/desktop (p. ej., Windows 10/11) dejan de facturarse como servidores en P1. | https://learn.microsoft.com/en-us/azure/defender-for-cloud/plan-defender-for-servers-select-plan ; https://learn.microsoft.com/en-us/azure/defender-for-cloud/release-notes | P1 "is entry-level, and focuses on the endpoint detection and response (EDR)". Release notes (30-sep-2026): actualización de facturación efectiva 1-nov-2026. |
| DFC-03 | Defender for Servers Plan 2 | Protección avanzada de servidores | ✅ | Precisión opcional: P2 = P1 + escaneo sin agente (vulnerabilidades, malware, secretos), MDVM premium, FIM, JIT, evaluación de cumplimiento, beneficio de ingesta gratuita; incluye alertas DNS para suscripciones nuevas. | https://learn.microsoft.com/en-us/azure/defender-for-cloud/plan-defender-for-servers-select-plan ; https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-dns-introduction | P2 "provides the same features as Plan 1, and more" (agentless scanning, FIM, JIT, etc.). Alertas DNS incluidas en P2 para suscripciones nuevas desde ago-2023. |
| DFC-04 | Defender for Containers | Kubernetes y contenedores | ✅ | Precisión opcional: hardening, evaluación de vulnerabilidades y protección en runtime para AKS, EKS, GKE y Kubernetes habilitado por Arc, más registries. Reemplaza a los planes heredados Defender for Kubernetes / for Container Registries (deprecados). | https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-cloud-introduction ; https://learn.microsoft.com/en-us/azure/defender-for-cloud/release-notes | Intro: "environment hardening, vulnerability assessment, run time protection of Kubernetes nodes and clusters". Release notes (5-jul-2026): planes AKS/ACR deprecados → migrar a Defender for Containers. |
| DFC-05 | Defender for Storage | Cuentas de almacenamiento y objetos | ✅ | Precisión opcional: cubre Azure Blobs, Azure Files y ADLS Gen2; Malware Scanning es complemento con cargo propio (on-upload y on-demand). | https://azure.microsoft.com/en-us/pricing/details/defender-for-cloud/ ; https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-cloud-introduction | Precios: protege "Azure Blobs, Azure Files and Azure Data Lake Storage Gen2"; Malware Scanning "add-on to Defender for Storage". |
| DFC-06 | Defender for SQL | SQL Server y bases SQL | ⚠️ | Nombre comercial válido en precios, pero en Learn el plan paraguas es **Defender for Databases**, que agrupa: Defender for Azure SQL Databases, Defender for SQL servers on machines, Defender for open-source relational databases y **Defender for Azure Cosmos DB** (ausente en el borrador). Nota: las APIs clásicas de Defender for SQL se retiran el 16-ago-2027. | https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-cloud-introduction ; https://azure.microsoft.com/en-us/pricing/details/defender-for-cloud/ ; https://learn.microsoft.com/en-us/azure/defender-for-cloud/release-notes | Intro lista bajo Defender for Databases: Azure SQL Databases, SQL servers on machines, OSS relational y "Defender for Azure Cosmos DB". Release notes: APIs clásicas "will be retired on August 16, 2027". |
| DFC-07 | Defender for Open-Source Relational Databases | Bases de datos relacionales compatibles | ✅ | Precisar "compatibles": Azure Database for PostgreSQL y MySQL (Flexible Server) y AWS RDS (Aurora PostgreSQL/MySQL, PostgreSQL, MySQL, MariaDB; GA en AWS RDS desde 1-jun-2026). No soportado en máquinas Arc. | https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-databases-introduction ; https://learn.microsoft.com/en-us/azure/defender-for-cloud/release-notes | Plan "within Defender for Databases"; soportado en PaaS de Azure y AWS; "It isn't supported on Azure Arc-enabled machines". GA en AWS RDS el 1-jun-2026. |
| DFC-08 | Defender for App Service | Aplicaciones alojadas en App Service | ✅ | — | https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-cloud-introduction | "Identifies attacks that target applications running over App Service." |
| DFC-09 | Defender for Key Vault | Actividades sospechosas sobre secretos y claves | ✅ | Precisión: el modelo heredado (por transacción) figura como plan deprecado; el vigente es de precio fijo por vault ($0,25/vault/mes). | https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-cloud-introduction ; https://learn.microsoft.com/en-us/azure/defender-for-cloud/release-notes ; https://azure.microsoft.com/en-us/pricing/details/defender-for-cloud/ | Intro: "Detects unusual and potentially harmful attempts to access or exploit Key Vault accounts". Release notes (5-jul-2026): migración del plan deprecado a "Fixed pricing model". |
| DFC-10 | Defender for Resource Manager | Operaciones sospechosas de administración | ✅ | Misma precisión que A-09: modelo heredado deprecado; vigente precio fijo por suscripción. | https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-cloud-introduction ; https://learn.microsoft.com/en-us/azure/defender-for-cloud/release-notes | "Detects unusual and potentially harmful activity by automatically monitoring the resource management operations." |
| DFC-11 | Defender for APIs | Protección y visibilidad de APIs | ✅ | **Sin retiro anunciado** en fuentes oficiales: plan activo (Planes 1–5 en precios; expansión regional jun-2026). Precisar: protege APIs **publicadas en Azure API Management**; el descubrimiento/postura de APIs (incluidas Function Apps y Logic Apps, GA 18-jun-2026) es **API security posture management dentro de Defender CSPM**. | https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-apis-introduction ; https://learn.microsoft.com/en-us/azure/defender-for-cloud/release-notes ; https://azure.microsoft.com/en-us/pricing/details/defender-for-cloud/ | "Defender for APIs currently provides security for APIs published in Azure API Management." Release notes: API security posture management en Defender CSPM para Function/Logic Apps "is now generally available". |
| DFC-12 | Defender for AI Services | Amenazas sobre servicios de IA | ✅ | Estado: **GA**. Precisar: detección en tiempo real para apps de IA generativa (Azure OpenAI, Azure AI Model Inference), integrada con Azure AI Content Safety Prompt Shields y Defender XDR; solo nubes comerciales; facturación por tokens. La postura (AI-SPM) va en Defender CSPM. | https://learn.microsoft.com/en-us/azure/defender-for-cloud/ai-threat-protection ; https://azure.microsoft.com/en-us/pricing/details/defender-for-cloud/ | Tabla de disponibilidad: "Release state Generally available (GA)"; "works with Azure AI Content Safety Prompt Shields". |
| DFC-13 | Defender for DevOps | Seguridad integrada con repositorios y pipelines | ⚠️ | "Defender for DevOps" es la etiqueta heredada (aún visible en el índice de Learn y en "Security services and technologies in Azure"), pero **no es un plan con precio propio**: el artículo vigente se titula "DevOps security" y las capacidades se entregan vía **Foundational CSPM** (básicas, gratis) y **Defender CSPM** (avanzadas: anotaciones de PR, code-to-cloud, attack paths, explorer); conecta Azure DevOps, GitHub y GitLab. Sugerido: "DevOps security (Defender for Cloud) — incluido en Foundational/Defender CSPM" y moverlo como sub-capacidad de CSPM. | https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-devops-introduction ; https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-cloud-security-posture-management ; https://azure.microsoft.com/en-us/pricing/details/defender-for-cloud/ ; https://learn.microsoft.com/en-us/azure/security/fundamentals/services-technologies | Artículo: "Overview of Microsoft Defender for Cloud DevOps security". CSPM: funciones DevOps avanzadas "require the paid Defender CSPM plan". Precios: Defender CSPM "includes DevOps security capabilities"; no hay precio de plan DevOps. |
| DFC-14 | Defender CSPM | Configuraciones, riesgos y rutas de ataque | ✅ | Precisión: plan pago; incluye attack path analysis, cloud security explorer, escaneo sin agente, DSPM, AI-SPM, API security posture, CIEM, EASM, gobernanza, cumplimiento regulatorio y serverless protection. | https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-cloud-security-posture-management | "Defender CSPM (paid): Provides extra capabilities beyond the Foundational CSPM plan" (attack path, risk prioritization, AI security posture). |
| DFC-15 | Defender for Cloud Regulatory Compliance | Evaluación de cumplimiento cloud | ⚠️ | **No es un plan**: es una capacidad/dashboard. MCSB viene por defecto (gratis); asignar otros estándares (ISO 27001, PCI DSS 4.0.1, NIS2, DORA, EU AI Act, etc.) requiere un plan pago: la matriz de CSPM lo ubica en Defender CSPM y la guía de asignación exige cualquier plan pago **excepto** Servers P1 o APIs P1. En el portal de Defender es solo de consulta; la asignación se hace en el portal de Azure. | https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-cloud-security-posture-management ; https://learn.microsoft.com/en-us/azure/defender-for-cloud/assign-regulatory-compliance-standards ; https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-regulatory-compliance-standards | Prerrequisito: cualquier plan pago, "except Defender for Servers Plan 1 or Defender for API Plan 1". Por defecto se habilita MCSB. |
| DFC-16 | Frase de cierre 3.A | "La documentación actual enumera protecciones para servidores, contenedores, bases de datos, almacenamiento, DevOps, App Service, Key Vault, Resource Manager e IA" | ⚠️ | Coincide con el índice de Learn (Workload protection + AI security), pero **omite APIs**, que figuran en la introducción y en el módulo de entrenamiento citado. Aclarar que DevOps es capacidad de CSPM, no un plan CWPP. Redactar: "…almacenamiento, App Service, Key Vault, Resource Manager, APIs e IA; y DevOps security como parte de CSPM". | https://learn.microsoft.com/en-us/azure/defender-for-cloud/ ; https://learn.microsoft.com/en-us/training/modules/enable-configure-workload-protection-plans/ | El índice lista Servers, Containers, Databases, Storage, DevOps, App Service, Key Vault, Resource Manager y una sección AI security. El módulo cubre "Servers, Storage, Databases, APIs, and AI Services". |

## A.8 Servicios de Azure (3.B)

| ID | Ítem | Afirmación del borrador | Val. | Corrección aplicada | Fuente(s) | Evidencia |
|---|---|---|---|---|---|---|
| AZ-01 | Microsoft Sentinel | SIEM y operaciones de seguridad | ✅ | Agregar contexto 2026: Sentinel es GA en el **portal de Microsoft Defender** (también sin Defender XDR/E5); la experiencia en el **portal de Azure deja de tener soporte después del 31-mar-2027** (antes 1-jul-2026). Incluye **Sentinel data lake** (nivel lago, retención hasta 12 años, formato Parquet) además del nivel analytics. | https://learn.microsoft.com/en-us/azure/sentinel/overview ; https://learn.microsoft.com/en-us/partner-center/announcements/2026-february ; https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-lake-overview | "After March 31, 2027, Microsoft Sentinel will no longer be supported in the Azure portal". Partner Center: extensión "to March 31, 2027 (previously July 1, 2026)". Data lake: retención "for up to 12 years". |
| AZ-02 | Sentinel SOAR | Automatización y orquestación de respuesta | ⚠️ | "Sentinel SOAR" no es un producto/SKU separado: es la capacidad SOAR nativa de Sentinel = **reglas de automatización + playbooks basados en Azure Logic Apps**. Renombrar a "Automatización de Microsoft Sentinel (automation rules + playbooks)". En el portal de Defender hay limitaciones (p. ej., playbooks manuales sobre alertas/entidades no soportados). | https://learn.microsoft.com/en-us/azure/sentinel/overview ; https://learn.microsoft.com/en-us/azure/sentinel/move-to-defender | "Playbooks in Microsoft Sentinel are based on workflows built in Azure Logic Apps." Automation rules gestionan centralmente la automatización de incidentes. |
| AZ-03 | Azure Firewall | Firewall administrado de red | ✅ | Precisión: firewall nativo, con estado, L3–L7; tres SKU: **Basic** (≤250 Mbps), **Standard** (≤30 Gbps; threat intel, DNS proxy, categorías web) y **Premium** (≤100 Gbps). | https://learn.microsoft.com/en-us/azure/firewall/choose-firewall-sku ; https://learn.microsoft.com/en-us/azure/networking/security/network-security | "Azure Firewall offers three SKUs to meet various customer needs" (Basic, Standard, Premium). |
| AZ-04 | Azure Firewall Premium | Inspección avanzada y protección de amenazas | ✅ | Presentarlo como **SKU de Azure Firewall**, no como servicio separado. Funciones exclusivas: inspección TLS saliente, **IDPS** administrado y **filtrado de URL** (ruta completa). | https://learn.microsoft.com/en-us/azure/firewall/choose-firewall-sku | Premium "includes advanced threat protection features like malware and TLS inspection"; IDPS y URL filtering solo en Premium. |
| AZ-05 | Azure Web Application Firewall | Protección de aplicaciones web | ✅ | Precisión: se despliega con **Application Gateway**, Application Gateway for Containers, **Azure Front Door** y Azure CDN (preview); protege contra OWASP Top 10 y bots. | https://learn.microsoft.com/en-us/azure/web-application-firewall/overview ; https://learn.microsoft.com/en-us/azure/networking/security/network-security | WAF "provides centralized protection of your web applications from common exploits and vulnerabilities". |
| AZ-06 | Azure DDoS Protection | Protección contra ataques DDoS | ✅ | Precisión: dos niveles pagos, **DDoS Network Protection** (incluye DDoS Rapid Response, protección de costos, descuento WAF) y **DDoS IP Protection** (por IP). La protección de infraestructura básica es gratuita y automática. | https://learn.microsoft.com/en-us/azure/ddos-protection/ddos-protection-sku-comparison | "supports two tier types, DDoS IP Protection and DDoS Network Protection"; infraestructura protegida "at no additional cost". |
| AZ-07 | Azure Key Vault | Administración de claves, secretos y certificados | ✅ | Precisión opcional: niveles Standard (software) y Premium (claves HSM; FIPS 140-3 L3 en HSM Platform 2). | https://learn.microsoft.com/en-us/azure/key-vault/general/secure-key-vault ; https://learn.microsoft.com/en-us/azure/security/fundamentals/key-management-choose | Key Vault "protects cryptographic keys, certificates … and secrets". |
| AZ-08 | Azure Managed HSM | Módulos de seguridad de hardware administrados | ✅ | Usar el nombre oficial **Azure Key Vault Managed HSM**: PaaS de un solo inquilino, FIPS 140-3 Nivel 3, soberanía de claves; **solo claves** (no secretos ni certificados). | https://learn.microsoft.com/en-us/azure/security/fundamentals/key-management-choose | Managed HSM "is FIPS 140-3 Level 3 compliant"; "stores cryptographic keys only". |
| AZ-09 | Azure Private Link | Acceso privado a servicios | ✅ | — (ver B-10). | https://learn.microsoft.com/en-us/azure/private-link/private-link-overview | Permite acceder a PaaS y servicios propios/de socios "over a private endpoint in your virtual network". |
| AZ-10 | Azure Private Endpoint | Conectividad privada a recursos | ⚠️ | **No es un servicio separado**: el private endpoint es un **componente de Azure Private Link** (NIC con IP privada que conecta a un recurso habilitado para Private Link). Fusionar B-09 y B-10: "Azure Private Link (private endpoints y Private Link service)". | https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview ; https://learn.microsoft.com/en-us/azure/private-link/private-link-overview | "A private endpoint is a network interface that uses a private IP address" y conecta a un servicio "powered by Azure Private Link". |
| AZ-11 | Azure Bastion | Acceso administrativo seguro a máquinas virtuales | ✅ | Precisión opcional: PaaS para RDP/SSH sobre TLS sin IP pública en las VMs; SKU Developer, Basic, Standard y Premium (grabación de sesiones y despliegue solo privado). | https://learn.microsoft.com/en-us/azure/bastion/bastion-overview | "fully managed PaaS service that provides secure and seamless RDP/SSH connectivity"; las VMs no necesitan IP pública. |
| AZ-12 | Azure Policy | Gobierno y cumplimiento de configuraciones | ✅ | — (Defender for Cloud implementa sus estándares de cumplimiento como iniciativas de Azure Policy). | https://learn.microsoft.com/en-us/azure/governance/policy/overview ; https://learn.microsoft.com/en-us/azure/defender-for-cloud/assign-regulatory-compliance-standards | "helps to enforce organizational standards and to assess compliance at-scale". |
| AZ-13 | Azure RBAC | Control de acceso a recursos | ✅ | Precisión: sistema de autorización de Azure Resource Manager (no un producto aparte); sin costo adicional. | https://learn.microsoft.com/en-us/azure/role-based-access-control/overview | "an authorization system built on Azure Resource Manager"; "free and included in your Azure subscription". |
| AZ-14 | Azure Monitor | Observabilidad y registros | ✅ | — | https://learn.microsoft.com/en-us/azure/azure-monitor/fundamentals/overview | "Microsoft's unified observability service for collecting, analyzing, and acting on telemetry". |
| AZ-15 | Azure Monitor Logs | Almacenamiento y consulta de telemetría | ✅ | Precisión: es parte de Azure Monitor (no servicio separado); workspace de Log Analytics con planes Analytics/Basic/Auxiliary; Sentinel y Defender for Cloud almacenan allí sus datos. | https://learn.microsoft.com/en-us/azure/azure-monitor/logs/data-platform-logs | "a centralized software as a service (SaaS) platform for collecting, analyzing, and acting on telemetry". |
| AZ-16 | Azure Confidential Computing | Protección de datos durante procesamiento | ✅ | Precisión: es una **familia de ofertas** (VMs confidenciales AMD SEV-SNP/Intel TDX, contenedores confidenciales, etc.), no un servicio único. | https://learn.microsoft.com/en-us/azure/confidential-computing/overview | "Confidential computing helps to protect data in use" mediante TEE basados en hardware y atestados. |
| AZ-17 | Azure Backup | Copias de seguridad | ✅ | Agregar valor de seguridad: vault aislado, soft delete, backups inmutables y RBAC como protección ante ransomware. | https://learn.microsoft.com/en-us/azure/backup/backup-overview | Azure Backup protege contra "accidental deletion, corruption, or ransomware"; incluye soft delete e immutable backup. |
| AZ-18 | Azure Site Recovery | Recuperación ante desastres | ✅ | — (servicio de resiliencia/BCDR, no de seguridad en sentido estricto). | https://learn.microsoft.com/en-us/azure/site-recovery/site-recovery-overview | ASR "provides infrastructure resiliency" con replicación continua, failover y recuperación. |
| AZ-19 | Azure Migrate | Evaluación y migración de workloads | ⚠️ | La función descrita es correcta, pero **no es un servicio de seguridad** (no figura en "Security services and technologies in Azure"). Recomendación: quitarlo de la tabla 3.B o moverlo a un anexo de "servicios habilitadores". | https://learn.microsoft.com/en-us/azure/migrate/migrate-services-overview ; https://learn.microsoft.com/en-us/azure/security/fundamentals/services-technologies | "helps you decide on, plan, and execute your migration to Azure"; el catálogo oficial de seguridad de Azure no lo incluye. |
| AZ-20 | Azure API Management | Gobierno, autenticación y control de APIs | ✅ | Precisión: plataforma de gestión de APIs (gateway valida claves/JWT/certificados, cuotas y rate limits); la protección en runtime proviene de Defender for APIs y DDoS Protection. | https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts | "a hybrid, multicloud management platform for APIs across all environments". |
| AZ-21 | Azure Front Door | Protección y distribución de aplicaciones web | ✅ | Precisión: CDN/entrada global (categoría load-balancing y content delivery) con DDoS L3-4 integrado y WAF adjunto. **Front Door (classic) se retira el 31-mar-2027**: usar Standard/Premium. | https://learn.microsoft.com/en-us/azure/frontdoor/front-door-overview ; https://learn.microsoft.com/en-us/azure/frontdoor/classic-retirement-faq | "an advanced content delivery network (CDN) for the cloud"; "Azure Front Door (classic) retires on March 31, 2027." |
| AZ-22 | Azure Application Gateway | Publicación y protección de aplicaciones | ✅ | Precisión: balanceador L7 con terminación TLS y WAF integrado. **Application Gateway v1 (Standard/WAF) se retiró el 28-abr-2026**; solo v2 (Standard_v2/WAF_v2). | https://learn.microsoft.com/en-us/azure/application-gateway/overview | "The v1 SKUs, Standard and WAF, retire on April 28, 2026". |
| AZ-23 | Azure Network Security Groups | Filtrado de tráfico de red | ✅ | Nota 2025–2027: **NSG flow logs** ya no admite nuevas configuraciones y se retira el 30-sep-2027 → migrar a **VNet flow logs**. | https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview | NSG filtra tráfico con reglas allow/deny; los NSG "flow logs retire on September 30, 2027". |
| AZ-24 | Azure Virtual Network Manager | Administración centralizada de redes y reglas | ✅ | Precisión: las **security admin rules** se evalúan antes que las reglas de NSG (guardrails globales). | https://learn.microsoft.com/en-us/azure/virtual-network-manager/overview ; https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview | AVNM agrupa, configura y gestiona VNets "globally across subscriptions and tenants"; reglas evaluadas "before network security group rules". |
| AZ-25 | Azure Arc | Gobierno y administración de recursos híbridos | ✅ | Precisión: proyecta recursos no-Azure a Azure Resource Manager; habilita Defender for Servers/Containers, Policy y Update Manager fuera de Azure (cobro por servicio usado). | https://learn.microsoft.com/en-us/azure/azure-arc/overview | "simplifies governance and management by delivering a consistent multicloud and on-premises management platform". |
| AZ-26 | Azure Update Manager | Gestión de actualizaciones | ✅ | — | https://learn.microsoft.com/en-us/azure/update-manager/overview | "a unified service to help manage and govern updates for all your machines" (Azure, on-prem y otras nubes vía Arc). |
| AZ-27 | Azure Attestation | Verificación de integridad y confianza | ✅ | — | https://learn.microsoft.com/en-us/azure/attestation/overview | "unified solution for remotely verifying the trustworthiness of a platform and integrity of the binaries". |
| AZ-28 | Azure Dedicated HSM | HSM dedicado | 🕒 | **En retiro**: no acepta nuevos clientes; soporte a clientes existentes hasta el **31-jul-2028**. Sucesor: **Azure Cloud HSM** (GA, FIPS 140-3 L3, PKCS#11, IaaS) o **Managed HSM** para PaaS. Reemplazar la fila por "Azure Cloud HSM" y mencionar Dedicated HSM solo como legado. | https://learn.microsoft.com/en-us/azure/dedicated-hsm/overview ; https://learn.microsoft.com/en-us/azure/security/fundamentals/key-management-choose | "Azure Dedicated HSM is being retired." "Azure Cloud HSM is now generally available and the successor". |
| AZ-29 | Azure Confidential Ledger | Registro verificable resistente a alteraciones | ✅ | — | https://learn.microsoft.com/en-us/azure/confidential-ledger/overview | Ledger "append-only" con "immutability, tamper-evident records" sobre enclaves de hardware. |
| AZ-30 | Frase de cierre 3.B | "Estos servicios no deben confundirse con productos de seguridad independientes: algunos son controles de seguridad integrados en servicios de infraestructura" | ⚠️ | La idea es razonable, pero **las fuentes citadas no la respaldan**: la página de seguridad de red presenta Firewall, DDoS Protection y WAF como servicios de seguridad dedicados, y la de Key Vault es una guía de buenas prácticas. Sugerido: "La tabla combina servicios de seguridad dedicados (Sentinel, Firewall, WAF, DDoS Protection, Key Vault/HSM, Bastion) con capacidades de plataforma que cumplen funciones de seguridad (NSG, Private Link, RBAC, Policy, Monitor, Backup/ASR, Update Manager, Arc)". Citar el catálogo oficial "Security services and technologies in Azure". | https://learn.microsoft.com/en-us/azure/networking/security/network-security ; https://learn.microsoft.com/en-us/azure/key-vault/general/secure-key-vault ; https://learn.microsoft.com/en-us/azure/security/fundamentals/services-technologies | Red: "Azure network security centers on three core services" (Firewall, DDoS, WAF). El catálogo oficial organiza las capacidades de seguridad por dominio, incluidos NSG, Monitor, Policy, Backup y ASR. |

## A.9 Mercados de Gartner Peer Insights (4 y 5)

| ID | Ítem | Afirmación del borrador | Val. | Corrección aplicada | Fuente(s) | Evidencia |
|---|---|---|---|---|---|---|
| GPI-A1 | Access Management → Entra ID | Mercado y correspondencia del borrador. URL citada: https://www.gartner.com/reviews/market/access-management | ⚠️ | Usar el nombre oficial con el sufijo de transición a CIAM. El mercado deriva hacia identidad de clientes (Entra External ID). Entra ID también figura en "User Authentication". | URL citada; https://www.gartner.com/reviews/product/microsoft-entra-id (Market Presence) | Existe: Sí. Oficial: "Access Management (Transitioning to Customer Identity and Access Management (CIAM))". Listado Microsoft: "Microsoft Entra ID" y "Microsoft Entra External ID" |
| GPI-A2 | Identity Governance and Administration → Entra ID Governance | Mercado y correspondencia del borrador. URL citada: https://www.gartner.com/reviews/market/identity-governance-administration | ✅ | — | https://www.gartner.com/reviews/market/identity-governance-administration/vendor/microsoft | Existe: Sí, "Identity Governance and Administration". Listado Microsoft: "Microsoft Entra ID" y "Microsoft Entra ID Governance" |
| GPI-A3 | Privileged Access Management → Entra PIM (parcial) | Mercado y correspondencia del borrador. URL citada: https://www.gartner.com/reviews/market/privileged-access-management | ⚠️ | Dejarlo como mapeo funcional del autor, sin listado de Microsoft en PAM. | https://www.gartner.com/reviews/product/microsoft-privileged-access-management ; https://www.gartner.com/reviews/market/it-security/vendor/microsoft | Existe: Sí, "Privileged Access Management". Listado Microsoft: No figura. "Microsoft Privileged Access Management" está solo en la categoría genérica "IT Security" |
| GPI-A4 | Identity Threat Detection and Response → Defender for Identity + Entra ID Protection | Mercado y correspondencia del borrador. URL citada: https://www.gartner.com/reviews/market/identity-threat-detection-and-response-itdr | ⚠️ | Entra ID Protection está en "IT Security", no en ITDR. Queda como mapeo funcional. | https://www.gartner.com/reviews/market/identity-threat-detection-and-response-itdr/vendor/microsoft ; https://www.gartner.com/reviews/product/microsoft-entra-id-protection | Existe: Sí, "Identity Threat Detection and Response (ITDR)". Listado Microsoft: Solo "Microsoft Defender for Identity" |
| GPI-A5 | Endpoint Protection → Defender for Endpoint | Mercado y correspondencia del borrador. URL citada: (sin URL) | ✅ | — (añadir URL) | https://www.gartner.com/reviews/market/endpoint-protection-platforms/vendor/microsoft ; https://www.gartner.com/reviews/product/microsoft-defender-for-endpoint | Existe: Sí. Hoy "Endpoint Protection"; la página de proveedor por mercado aún muestra "Endpoint Protection Platforms (Transitioning to Endpoint Protection)". Listado Microsoft: "Microsoft Defender for Endpoint" |
| GPI-A6 | Endpoint Management Tools → Intune | Mercado y correspondencia del borrador. URL citada: https://www.gartner.com/reviews/market/endpoint-management-tools | ✅ | — | URL citada | Existe: Sí, "Endpoint Management Tools" (categoría IT Infrastructure and IoT). Listado Microsoft: "Microsoft Intune" |
| GPI-A7 | Security Awareness Computer-Based Training → Attack Simulation Training (parcial) | Mercado y correspondencia del borrador. URL citada: https://www.gartner.com/reviews/market/security-awareness-computer-based-training | ⚠️ | Dejarlo como mapeo funcional del autor. | URL citada; https://www.gartner.com/reviews/product/microsoft-defender-for-office-365 | Existe: Sí, "Security Awareness Computer-Based Training". Listado Microsoft: No figura. Defender for Office 365 está listado solo en "Email Security" |
| GPI-B1 | Security Information and Event Management → Sentinel | Mercado y correspondencia del borrador. URL citada: https://www.gartner.com/reviews/market/security-information-event-management | ✅ | — | URL citada; https://www.gartner.com/reviews/product/microsoft-sentinel | Existe: Sí, "Security Information and Event Management". Listado Microsoft: "Microsoft Sentinel" |
| GPI-B2 | Integrated Security Operations Center Solutions → Defender XDR + Sentinel | Mercado y correspondencia del borrador. URL citada: https://www.gartner.com/reviews/market/integrated-security-operations-center-solutions | ⚠️ | Registrar solo Sentinel como listado. Defender XDR queda como mapeo funcional. | URL citada | Existe: Sí, "Integrated Security Operations Center Solutions" (mercado chico: todos sus productos son visibles). Listado Microsoft: Solo "Microsoft Sentinel", todavía sin reseñas. No figura Defender XDR ni "Microsoft Defender Suite" |
| GPI-B3 | Extended Detection and Response — retirada → Defender XDR | Mercado y correspondencia del borrador. URL citada: (sin URL) | ⚠️ | Registrar el listado como "Microsoft Defender Suite". No usar este mercado retirado como categoría vigente. | https://www.gartner.com/reviews/market/extended-detection-and-response/vendor/microsoft | Existe: Sí, "Extended Detection and Response (Retired)". El borrador acierta en que está retirado. Listado Microsoft: Sí, como "Microsoft Defender Suite" (un rastro de 2025 muestra el nombre anterior "Microsoft Defender XDR") |
| GPI-B4 | Security Orchestration, Automation and Response — en transición → Sentinel Automation | Mercado y correspondencia del borrador. URL citada: (sin URL) | ✅ | — (añadir URL y nombre oficial) | https://www.gartner.com/reviews/market/security-orchestration-automation-and-response-solutions ; https://www.gartner.com/reviews/market/security-orchestration-automation-and-response-solutions/vendor/microsoft | Existe: Sí. Oficial: "Security Orchestration, Automation and Response Solutions (Transitioning to Security Information and Event Management)". Listado Microsoft: "Microsoft Sentinel" |
| GPI-B5 | Network Detection and Response → parcial vía Sentinel y señales de red | Mercado y correspondencia del borrador. URL citada: https://www.gartner.com/reviews/market/network-detection-and-response | ⚠️ | **El mapeo es inconsistente:** Sentinel es un SIEM, no un NDR, y Microsoft no tiene producto NDR listado. Su detección con sensores de red (Defender for IoT, orientado a OT/IoT) figura en "CPS Protection Platforms" e "IoT Security". Reclasificar como "sin oferta NDR nativa / complementaria vía integraciones", como ya dice la sección 5. | URL citada; https://www.gartner.com/reviews/product/microsoft-defender-for-iot | Existe: Sí, "Network Detection and Response". Listado Microsoft: No figura |
| GPI-B6 | Managed Detection and Response → Defender Experts MDR | Mercado y correspondencia del borrador. URL citada: https://www.gartner.com/reviews/market/managed-detection-and-response | ⚠️ | La sección 5 la califica "Directa": rebajarla a mapeo funcional, sin listado Gartner. | URL citada; https://www.gartner.com/reviews/product/microsoft-defender-suite-1683939452 | Existe: Sí, "Managed Detection and Response". Listado Microsoft: No figura. Gartner no tiene ficha "Defender Experts". "Microsoft Defender Suite" está en 4 mercados y ninguno es MDR |
| GPI-B7 | Co-Managed Security Monitoring Services → servicios de expertos | Mercado y correspondencia del borrador. URL citada: (sin URL) | ⚠️ | El borrador no nombra producto. El listado es "Microsoft Defender Suite". | https://www.gartner.com/reviews/market/co-managed-security-monitoring-services | Existe: Sí, "Co-Managed Security Monitoring Services". Listado Microsoft: Sí, como "Microsoft Defender Suite" (con pocas reseñas) |
| GPI-B8 | Cybersecurity Incident Response Management → Defender XDR, Sentinel | Mercado y correspondencia del borrador. URL citada: (sin URL) | ⚠️ | Mapeo funcional del autor (aproximado). | https://www.gartner.com/reviews/market/cybersecurity-incident-response-management | Existe: Sí, "Cybersecurity Incident Response Management". Es un mercado de gestión de casos y flujos para equipos CIRT; todos sus productos son visibles. Listado Microsoft: No figura |
| GPI-B9 | External Attack Surface Management → Defender EASM | Mercado y correspondencia del borrador. URL citada: https://www.gartner.com/reviews/market/external-attack-surface-management | ✅ | — | URL citada; https://www.gartner.com/reviews/vendor/microsoft | Existe: Sí, "External Attack Surface Management". Listado Microsoft: "Microsoft Defender External Attack Surface Management" |
| GPI-B10 | Cyber Asset Attack Surface Management → Security Exposure Management (parcial) | Mercado y correspondencia del borrador. URL citada: https://www.gartner.com/reviews/market/cyber-asset-attack-surface-management | ⚠️ | Mapeo funcional del autor. Security Exposure Management figura en Exposure Assessment Platforms. | URL citada; https://www.gartner.com/reviews/vendor/microsoft | Existe: Sí, "Cyber Asset Attack Surface Management (CAASM)". Listado Microsoft: No figura |
| GPI-B11 | Exposure Assessment Platforms → Security Exposure Management + Defender Vulnerability Management | Mercado y correspondencia del borrador. URL citada: https://www.gartner.com/reviews/market/exposure-assessment-platforms | ⚠️ | Quitar Defender Vulnerability Management como listado: Gartner lo ubica en "Vulnerability Assessment (Retired)". | https://www.gartner.com/reviews/market/exposure-assessment-platforms/vendor/microsoft ; https://www.gartner.com/reviews/product/microsoft-defender-vulnerability-management | Existe: Sí, "Exposure Assessment Platforms". Listado Microsoft: Solo "Microsoft Security Exposure Management" |
| GPI-B12 | Adversarial Exposure Validation → sin equivalencia completa | Mercado y correspondencia del borrador. URL citada: https://www.gartner.com/reviews/market/adversarial-exposure-validation | ✅ | — (coherente con "no equivalencia") | URL citada; https://www.gartner.com/reviews/vendor/microsoft | Existe: Sí, "Adversarial Exposure Validation". Listado Microsoft: No figura |
| GPI-C1 | Cloud-Native Application Protection Platforms → Defender for Cloud | Mercado y correspondencia del borrador. URL citada: https://www.gartner.com/reviews/market/cloud-native-application-protection-platforms | ✅ | — | URL citada; https://www.gartner.com/reviews/product/microsoft-defender-for-cloud | Existe: Sí, "Cloud-Native Application Protection Platforms". Listado Microsoft: "Microsoft Defender for Cloud" |
| GPI-C2 | Cloud Security Posture Management Tools → Defender CSPM | Mercado y correspondencia del borrador. URL citada: https://www.gartner.com/reviews/market/cloud-security-posture-management-tools | ⚠️ | Registrar el listado como "Microsoft Defender for Cloud" (Defender CSPM es un plan dentro de ese producto). | URL citada; https://www.gartner.com/reviews/product/microsoft-defender-for-cloud | Existe: Sí, "Cloud Security Posture Management Tools". Sus características no se actualizan desde 2023. Listado Microsoft: Sí, como "Microsoft Defender for Cloud" |
| GPI-C3 | Security Service Edge → Entra Internet Access + Private Access | Mercado y correspondencia del borrador. URL citada: https://www.gartner.com/reviews/market/security-service-edge | ⚠️ | Mapeo funcional del autor. | URL citada; https://www.gartner.com/reviews/product/microsoft-entra-internet-access ; https://www.gartner.com/reviews/market/it-security/vendor/microsoft | Existe: Sí, "Security Service Edge". Listado Microsoft: No figura con reseñas. Entra Internet Access y Entra Private Access están en "IT Security". Una página de 2025 de "Microsoft Entra Suite" en SSE aparece vacía |
| GPI-C4 | SASE Platforms (cita single-vendor-sase) → parcial | Mercado y correspondencia del borrador. URL citada: https://www.gartner.com/reviews/market/single-vendor-sase | ⚠️ | El nombre y la URL son válidos. La sección 5 ("Entra + Azure Networking") es solo un mapeo funcional. | URL citada | Existe: Sí. La URL con nombre anterior abre hoy "SASE Platforms". Listado Microsoft: No figura |
| GPI-C5 | Network Security Microsegmentation → Azure NSG, Firewall (parcial) | Mercado y correspondencia del borrador. URL citada: (sin URL) | ⚠️ | Registrar el listado como "Microsoft Azure". Azure Firewall figura aparte, en "Hybrid Mesh Firewall". | https://www.gartner.com/reviews/market/network-security-microsegmentation ; https://www.gartner.com/reviews/market/network-security-microsegmentation/vendor/microsoft ; https://www.gartner.com/reviews/product/azure-firewall | Existe: Sí, "Network Security Microsegmentation". Listado Microsoft: Sí, como "Microsoft Azure" (genérico) |
| GPI-C6 | Cloud Web Application and API Protection → Azure WAF, Front Door, DDoS | Mercado y correspondencia del borrador. URL citada: https://www.gartner.com/reviews/market/cloud-web-application-and-api-protection | ⚠️ | Mapear cada servicio a su mercado real. Para WAAP queda como mapeo funcional. | https://www.gartner.com/reviews/product/azure-web-application-firewall ; https://www.gartner.com/reviews/vendor/microsoft | Existe: Sí, "Cloud Web Application and API Protection". Listado Microsoft: No figura. Azure WAF está en "IT Security", Azure Front Door en "Edge Distribution Platforms" y Azure DDoS Protection en "DDoS Mitigation Solutions" |
| GPI-C7 | AI Application Security → Defender for Cloud (AI) | Mercado y correspondencia del borrador. URL citada: https://www.gartner.com/reviews/market/ai-application-security | ⚠️ | Mapeo funcional del autor. | URL citada; https://www.gartner.com/reviews/vendor/microsoft | Existe: Sí, "AI Application Security". Listado Microsoft: No figura |
| GPI-C8 | AI Usage Control → Entra Internet Access, Purview, Defender for Cloud Apps | Mercado y correspondencia del borrador. URL citada: https://www.gartner.com/reviews/market/ai-usage-control | ⚠️ | Mapeo funcional del autor. | URL citada; https://www.gartner.com/reviews/product/microsoft-purview-1861237758 | Existe: Sí, "AI Usage Control". Listado Microsoft: No figura. Defender for Cloud Apps está en "IT Security"; Purview figura en "AI Governance Platforms" y en DLP |
| GPI-D1 | Data Loss Prevention → Purview DLP | Mercado y correspondencia del borrador. URL citada: https://www.gartner.com/reviews/market/data-loss-prevention | ⚠️ | Registrar el listado como "Microsoft Purview", no como "Purview Data Loss Prevention". | https://www.gartner.com/reviews/market/data-loss-prevention/vendor/microsoft | Existe: Sí, "Data Loss Prevention". Listado Microsoft: Sí, como "Microsoft Purview" |
| GPI-D2 | Data Security Posture Management → Purview DSPM | Mercado y correspondencia del borrador. URL citada: (sin URL; el texto la apoya en la URL de Data Security Platforms) | ⚠️ | Añadir la URL propia del mercado. Purview DSPM queda como mapeo funcional, no "Directa". | https://www.gartner.com/reviews/market/data-security-posture-management | Existe: Sí, "Data Security Posture Management". Listado Microsoft: No figura |
| GPI-D3 | Data Security Platforms → Purview + Azure Key Vault (parcial) | Mercado y correspondencia del borrador. URL citada: https://www.gartner.com/reviews/market/data-security-platforms | ⚠️ | Registrar ese nombre de listado. Key Vault no figura (mapeo funcional). | URL citada; https://www.gartner.com/reviews/vendor/microsoft | Existe: Sí, "Data Security Platforms". Listado Microsoft: Solo "Microsoft Purview Data Governance" (con pocas reseñas) |
| GPI-D4 | Email Security → Defender for Office 365 | Mercado y correspondencia del borrador. URL citada: https://www.gartner.com/reviews/market/email-security | ✅ | — | https://www.gartner.com/reviews/market/email-security/vendor/microsoft | Existe: Sí, "Email Security". Listado Microsoft: "Microsoft Defender for Office 365" |
| GPI-D5 | Digital Communications Governance and Archiving Solutions → Purview Audit, eDiscovery, Records | Mercado y correspondencia del borrador. URL citada: https://www.gartner.com/reviews/market/digital-communications-governance-and-archiving-solutions | ⚠️ | Registrar ese nombre de listado. Purview eDiscovery figura en otro mercado, "E-Discovery Solutions". | https://www.gartner.com/reviews/product/microsoft-purview-data-lifecycle-management ; https://www.gartner.com/reviews/product/microsoft-purview-ediscovery | Existe: Sí (categoría IT Infrastructure and IoT). Listado Microsoft: Solo "Microsoft Purview Data Lifecycle Management" |
| GPI-D6 | Data and Analytics Governance Platforms → Purview Data Governance | Mercado y correspondencia del borrador. URL citada: (sin URL) | ✅ | — (añadir URL) | https://www.gartner.com/reviews/market/data-and-analytics-governance-platforms | Existe: Sí, "Data and Analytics Governance Platforms" (categoría Data and Analytics). Listado Microsoft: "Microsoft Purview Data Governance" |
| GPI-D7 | Privacy UX → parcial | Mercado y correspondencia del borrador. URL citada: (sin URL) | ✅ | — (coherente con "no equivalente integral"; añadir URL) | https://www.gartner.com/reviews/market/privacy-ux | Existe: Sí, "Privacy UX". Listado Microsoft: No figura |
| GPI-D8 | Microsoft 365 Governance Tools → capacidades nativas | Mercado y correspondencia del borrador. URL citada: https://www.gartner.com/reviews/market/microsoft-365-governance-tools | ✅ | — | URL citada | Existe: Sí. Mercado chico: todos sus productos son de terceros y visibles. Listado Microsoft: No figura (es lo esperable) |
| GPI-D9 | Backup and Data Protection Platforms → Azure Backup, Microsoft 365 Backup | Mercado y correspondencia del borrador. URL citada: https://www.gartner.com/reviews/market/backup-and-data-protection-platforms | ✅ | — | URL citada; https://www.gartner.com/reviews/vendor/microsoft | Existe: Sí (categoría Cloud Computing). Listado Microsoft: "Microsoft Azure Backup" y "Microsoft 365 Backup" |
| GPI-D10 | IT Risk Management → Compliance Manager, Defender for Cloud | Mercado y correspondencia del borrador. URL citada: (sin URL) | ⚠️ | Mapeo funcional del autor. Unificar el borrador: la sección 4 dice Defender for Cloud y la sección 5 dice Azure Policy. | https://www.gartner.com/reviews/market/it-risk-management-solutions ; https://www.gartner.com/reviews/product/microsoft-purview-compliance-manager | Existe: Sí, "IT Risk Management (ITRM)". Listado Microsoft: No figura. Purview Compliance Manager está en "IT Security" |
| GPI-D11 | Security Consulting Services → Microsoft Security Services | Mercado y correspondencia del borrador. URL citada: (sin URL) | ⚠️ | Usar el nombre oficial. Queda como mapeo funcional del autor. | https://www.gartner.com/reviews/market/security-consulting-services-worldwide | Existe: Sí. Oficial: "Security Consulting Services, Worldwide". Listado Microsoft: No figura |
| GPI-T1 | 4.A — nota | Algunas categorías están en transición de denominación | ✅ | — | [G1], [G5] | Access Management en transición a CIAM; Endpoint Protection Platforms pasó a Endpoint Protection |
| GPI-T2 | 4.B — nota | Gartner distingue SIEM, ISOC, MDR, NDR, ITDR y gestión de exposición | ✅ | — | [G8], [G9], [G13], [G12], [G4], [G18] | Son mercados separados y vigentes |
| GPI-T3 | 4.C — nota | CNAPP incluye capacidades preventivas y reactivas desde el código hasta el runtime; Defender for Cloud es la correspondencia más directa | ✅ | — | [G20], [A1] | Paráfrasis fiel de la definición del mercado; Defender for Cloud figura listado |
| GPI-T4 | 4.D — nota | Gartner tiene mercados específicos para DLP, DSPM, correo, backup, archivo de comunicaciones y gobierno de Microsoft 365 | ⚠️ | Todos existen, pero DSPM tiene URL propia; el borrador la apoyaba en la de Data Security Platforms | [G29], [G30] | URL propia del mercado DSPM verificada |

## A.10 Servicios de seguridad (6)

| ID | Ítem | Afirmación del borrador | Val. | Corrección aplicada | Fuente(s) | Evidencia |
|---|---|---|---|---|---|---|
| SRV-01 | Defender Experts MDR | SOC administrado y respuesta · **MDR** | ⚠️ | Categoría correcta (MDR), descripción exagerada: Microsoft aclara que **complementa** el SOC del cliente, no lo reemplaza; Plan 2 **no** es un SIEM gestionado; no incluye respuesta a incidentes ante compromiso activo (→ Cybersecurity IR) ni cargas de Defender for Cloud (→ Experts for Servers). Sugerido: «MDR 24x7 que complementa el SOC (triage, investigación, respuesta guiada o en nombre del cliente); Plan 1 / Plan 2». | https://learn.microsoft.com/en-us/defender-xdr/defender-experts/defender-experts-mdr-overview (08/07/2026) | "augments your security operations center (SOC) rather than replacing it"; "Plan 2 isn't a managed security information and event management (SIEM) service". |
| SRV-02 | Defender Experts Hunting | Búsqueda proactiva de amenazas · **Threat Hunting / MDR** | ✅ | Opcional: variantes Hunting – XDR y Hunting – Servers. | https://learn.microsoft.com/en-us/defender-xdr/defender-experts/defender-experts-overview (07/27/2026) | "proactive threat hunting service for customers who have a robust SOC". |
| SRV-03 | Defender Experts for Servers | MDR para servidores · **MDR / CWPP** | ✅ | Opcional: requiere **Defender for Servers P1 o P2** (Defender for Cloud), **Entra ID P2** y MDE en los servidores; medidor **pay-as-you-go**; cubre Azure, AWS, GCP y on-premises; no requiere Defender Experts MDR. | https://learn.microsoft.com/en-us/defender-xdr/defender-experts/defender-experts-servers-overview (en resultados de búsqueda); https://learn.microsoft.com/en-us/defender-xdr/defender-experts/defender-experts-servers-get-started (en resultados de búsqueda); overview (URL de S-02) | "sold separately from other Microsoft Defender products and uses pay-as-you-go consumption meter". |
| SRV-04 | Defender Experts Threat Intelligence | Inteligencia y alertas contextualizadas · **Threat Intelligence** | ✅ | **Existe** (hipótesis confirmada): briefings mensuales y alertas proactivas adaptadas a industria, geografía y entorno; se contrata vía account team. No confundir con MDTI (producto retirado el 1-ago-2026, ver B-14). | Overview (URL de S-02); https://www.microsoft.com/en-us/security/business/microsoft-defender-experts-cybersecurity-incident-response (en resultados; lista el servicio) | "Curated threat briefings and proactive threat alerts"; entrega por "monthly briefings". |
| SRV-05 | Defender Experts Cybersecurity Incident Response | Preparación, investigación y respuesta · **Incident Response Services** | ✅ | Opcional: es la marca vigente de **Microsoft Incident Response (equipo DART)**; incluye servicios proactivos (planificación de IR, assessment, simulación, advisory) y reactivos (investigación, contención, recuperación); contrato separado. Es también componente de **Defender Experts Suite** (el blog de ene-2026 aún lo llama "Microsoft Incident Response"). | Overview (URL de S-02); página oficial IR (URL de S-04); https://www.microsoft.com/en-us/security/blog/2026/01/06/introducing-the-microsoft-defender-experts-suite-elevate-your-security-with-expert-led-services/ | "professional service that helps your organization prepare for, respond to, and recover"; página oficial: "Your first call before, during, and after a cybersecurity incident." |
| SRV-06 | Microsoft Security FastTrack | Orientación de despliegue y adopción · **Servicios de implementación** | ⚠️ | **Nombre no oficial**. La oferta es **FastTrack for Microsoft 365**: asistencia remota y guiada para tenants con **≥150 licencias** de planes elegibles (M365 E3/E5/E7, Defender Suite/E5 Security, Business Premium, EMS, Entra, Intune…); cubre Defender XDR, MDE, MDI, MDO, MDA, Defender for Servers, Purview, Entra e Intune. **FastTrack for Azure fue retirado el 31-dic-2024**. | https://learn.microsoft.com/en-us/microsoft-365/fasttrack/eligibility (05/04/2026); https://techcommunity.microsoft.com/blog/fasttrackforazureblog/fasttrack-for-azure-fta-program-retiring-december-2024/4357383 (en resultados de búsqueda) | "available for customer tenants with 150 or more licenses for Copilot, Security"; FTA "will be retired" desde 31-dic-2024. |
| SRV-07 | Microsoft Unified Support | Soporte técnico empresarial · **Servicios de soporte** | 🕒 | Denominación anterior. Marca vigente: **Microsoft Unified**, cuyo servicio base es **Unified Enterprise** (soporte reactivo 24x7, success management, evaluaciones on-demand/proactivas, Flex Allowance), con add-ons **Value Acceleration Services** y **Mission Critical Services**. Precio escalonado según gasto Microsoft (mínimo USD 50.000). | https://www.microsoft.com/en-us/microsoft-unified (en resultados de búsqueda); https://www.microsoft.com/en-us/microsoft-unified/unified-enterprise (en resultados de búsqueda); https://www.microsoft.com/en-us/microsoft-unified/plan-details (en resultados de búsqueda) | "Unified Enterprise is the foundational service"; incluye "technical reactive support with incident management, on-demand training, and assessments". |
| SRV-08 | Microsoft Security Assessment | Evaluaciones según programa y elegibilidad · **Security Consulting** | ❔ | **No se encontró una oferta oficial vigente con ese nombre.** Búsqueda "Microsoft Security Assessment": solo aparecen la herramienta legada *Microsoft Security Assessment Tool 4.0* (MSAT, descargable) y una evaluación gratuita específica para ONG. Alternativas oficiales verificadas: componentes proactivos de **Defender Experts Cybersecurity IR** (assessment, simulación, advisory), evaluaciones de **Unified Enterprise** y **Enhanced Designated Engineering** (Defender Experts Suite). Sugerido: reemplazar por esas ofertas o eliminar. | https://www.microsoft.com/en-us/download/details.aspx?id=12273 (en resultados de búsqueda); página oficial IR (URL de S-04); Unified Enterprise (URL de S-07); blog Defender Experts Suite (URL de S-05) | MSAT es una "risk-assessment application" descargable, no un servicio de consultoría. |
| SRV-09 | Microsoft Security Copilot | Asistencia de IA para analistas · **AI-assisted Security Operations** | ⚠️ | Es un **producto** SaaS licenciado por capacidad (SCU), no un servicio profesional; además duplica B-15. Moverlo a la tabla de tecnologías o rotularlo "Producto (incluido en E5/E7)". | https://learn.microsoft.com/en-us/copilot/security/security-compute-units-capacity ; https://www.microsoft.com/en-us/security/security-copilot-in-microsoft-365-e5 (en resultados de búsqueda) | Se consume como capacidad: "SCUs are the units of compute resources"; incluido en E5 "at no extra cost". |
| SRV-10 | Párrafo de cierre T6 | "Defender Experts como familia… MDR se comercializa por separado" + 2 citas | ✅ | Ambas URLs **existen** y respaldan la frase. Mejoras: mencionar Defender Experts for Servers y la oferta empaquetada **Defender Experts Suite**; precisar que **cada** servicio Defender Experts se vende por separado. | Overview (URL de S-02); MDR overview (URL de S-01) | "Each Defender Experts service is sold separately"; MDR "sold separately from other Microsoft Defender products". |

## A.11 Licenciamiento E3/E5/E7 (7)

| ID | Ítem | Afirmación del borrador | Val. | Corrección aplicada | Fuente(s) | Evidencia |
|---|---|---|---|---|---|---|
| LIC-01 | Entra ID P1 | Sí / Sí / Sí | ✅ | — (en E5/E7 viene dentro de P2). | https://www.microsoft.com/en-us/microsoft-365/enterprise/microsoft-365-plans-and-pricing | Comparativa: Entra ID "Plan 2 / Plan 2 / Plan 1" (E7/E5/E3). |
| LIC-02 | Entra ID P2 | No / Sí / Sí | ✅ | — | https://www.microsoft.com/en-us/microsoft-365/enterprise/microsoft-365-plans-and-pricing ; https://learn.microsoft.com/en-us/entra/id-governance/licensing-fundamentals | P2 "included with Microsoft 365 E5 or E7". |
| LIC-03 | Defender for Endpoint | P1 / P2 / P2 | ✅ | Matiz: cubre hasta 5 dispositivos por usuario; servidores se licencian aparte. | https://www.microsoft.com/en-us/microsoft-365/enterprise/microsoft-365-plans-and-pricing ; https://www.microsoft.com/en-us/security/pricing/enterprise-plans | Comparativa: MDE "Plan 2 / Plan 2 / Plan 1"; FAQ: servidores "must be licensed separately". |
| LIC-04 | Defender for Office 365 | "P1 según plan" / P2 / P2 | ⚠️ | Reemplazar "P1 según plan" por "P1 (incluido en M365 E3 desde 1-jul-2026; antes solo EOP)". P1 no integra con Defender XDR ni trae AIR/Attack simulation. | https://learn.microsoft.com/en-us/office365/servicedescriptions/office-365-advanced-threat-protection-service-description ; https://www.microsoft.com/en-us/licensing/news/2026-M365-Packaging-Pricing-Updates | Service description: P1 incluido en O365 E3 y M365 E3 "effective July 1, 2026". |
| LIC-05 | Defender for Identity | No / Sí / Sí | ✅ | Matiz: E3 puede sumarlo con Microsoft Defender Suite (ex "M365 E5 Security"). | https://www.microsoft.com/en-us/microsoft-365/enterprise/microsoft-365-plans-and-pricing ; https://www.microsoft.com/en-us/security/pricing/enterprise-plans | Comparativa: MDI incluido en E7 y E5, no en E3. |
| LIC-06 | Defender for Cloud Apps | No / Sí / Sí | ⚠️ | Cambiar E3 a "Solo Discovery (Cloud App Discovery / shadow IT)". La protección SaaS completa (CASB, OAuth malicioso) es E5/E7. | https://www.microsoft.com/en-us/microsoft-365/enterprise/microsoft-365-plans-and-pricing | Comparativa: "Defender for Cloud Apps Discovery" incluido en E7, E5 y E3; protección completa solo E7/E5. |
| LIC-07 | Defender XDR avanzado | Parcial / Sí / Sí | ✅ | Matiz: E3 accede al portal Defender con MDE P1 y Cloud App Discovery; attack disruption y threat analytics requieren MDE P2; E3 + Defender Suite habilita XDR completo. | https://learn.microsoft.com/en-us/defender-xdr/prerequisites | Licencias válidas incluyen "Microsoft 365 E3 with the Microsoft Defender Suite add-on"; attack disruption requiere MDE P2. |
| LIC-08 | Purview Information Protection | Base / Avanzado / Avanzado | ✅ | Usar la nomenclatura oficial: "Plan 1" (E3) / "Plan 2" (E5/E7). | https://www.microsoft.com/en-us/microsoft-365/enterprise/microsoft-365-plans-and-pricing | Comparativa: Information Protection "Plan 2 / Plan 2 / Plan 1". |
| LIC-09 | Purview DLP | Base / Avanzado / Avanzado | ✅ | Precisar E3: "correo y archivos". | https://www.microsoft.com/en-us/microsoft-365/enterprise/microsoft-365-plans-and-pricing | Comparativa: DLP en E3 "For emails and files". |
| LIC-10 | Purview Insider Risk Management | No / Sí / Sí | ✅ | Matiz: E3 puede sumarlo con Microsoft Purview Suite (ex "M365 E5 Compliance", US$12, requiere M365 E3). | https://www.microsoft.com/en-us/microsoft-365/enterprise/microsoft-365-plans-and-pricing ; https://www.microsoft.com/en-us/security/pricing/enterprise-plans | Comparativa: IRM incluido en E7 y E5, no en E3. |
| LIC-11 | Purview eDiscovery | Base / Avanzado / Avanzado | ✅ | Usar nombres oficiales "Standard" (E3) / "Premium" (E5/E7); ídem Audit Standard/Premium. | https://www.microsoft.com/en-us/microsoft-365/enterprise/microsoft-365-plans-and-pricing | Comparativa: eDiscovery "Premium / Premium / Standard". |
| LIC-12 | Intune | Plan 1 / Plan 1 / Plan 1 | 🕒 | Desde 1-jul-2026 (rollout completo al 1-ago-2026): **E3** = Plan 1 + Plan 2 (Tunnel for MAM, dispositivos especiales, FOTA) + Remote Help + Advanced Analytics. **E5 y E7** = todo lo anterior + Endpoint Privilege Management + Enterprise App Management + Cloud PKI. Nota: la página de producto E3 menciona EPM, pero el anuncio de licenciamiento, el FAQ de precios de Intune y la comparativa M365 vs O365 ubican EPM solo en E5; validar en Intune admin center > Intune add-ons y en Product Terms. | https://www.microsoft.com/en-us/licensing/news/2026-M365-Packaging-Pricing-Updates ; https://www.microsoft.com/en-us/security/microsoft-intune-pricing ; https://www.microsoft.com/en-us/microsoft-365/enterprise/e5 ; https://www.microsoft.com/en-us/microsoft-365/enterprise/e3 | FAQ Intune: E3 recibe "Remote Help, Advanced Analytics, Intune Plan 2"; E5 suma "EPM, Cloud PKI, and Enterprise App Management". |
| LIC-13 | Windows Enterprise | Sí / Sí / Sí | ✅ | Precisar edición: E3 = Windows 11 Enterprise E3; E5/E7 = Windows 11 Enterprise E5 (Windows Pro como SO calificante). | https://www.microsoft.com/en-us/microsoft-365/enterprise/microsoft-365-plans-and-pricing | Comparativa: "Windows 11 Enterprise E5 / E5 / E3". |
| LIC-14 | Microsoft Entra Suite | No / Add-on / Sí | ❌ | E3 = **Add-on** (único prerrequisito: Entra ID P1, que E3 incluye). Microsoft la posiciona para "Microsoft 365 E3 or E5" (US$12; precio especial para clientes P2/E5). | https://www.microsoft.com/en-us/security/microsoft-entra-pricing ; https://www.microsoft.com/en-us/security/pricing/enterprise-plans | Entra Suite "Requires: Microsoft Entra ID P1 or a plan that includes Microsoft Entra ID P1". |
| LIC-15 | Microsoft 365 Copilot | Add-on / Add-on / Sí | ✅ | Matiz: add-on US$30/usuario/mes (lista, anual). | https://www.microsoft.com/en-us/microsoft-365/enterprise/microsoft-365-plans-and-pricing | "Microsoft 365 Copilot (add-on) $30.00"; "Included in Microsoft 365 E7". |
| LIC-16 | Agent 365 | Add-on / Add-on / Sí | ⚠️ | E3: **no elegible por sí solo**; desde 1-jun-2026 requiere M365 E5/A5/G5, Business Premium o Defender Suite + Purview Suite. Corregir a "Solo con Defender Suite + Purview Suite / Add-on (US$15) / Incluido". GA: 1-may-2026. Nota: la página Learn de ID Governance todavía cita P1/E3 como prerrequisito técnico; prevalece Product Terms. | https://www.microsoft.com/licensing/terms/en-US/productoffering/Agent365/EAEAS ; https://learn.microsoft.com/en-us/entra/agent-id/what-is-microsoft-entra-agent-id ; https://www.microsoft.com/en-us/microsoft-365/enterprise/microsoft-365-plans-and-pricing | Product Terms: prerrequisito "Microsoft 365 A5, E5, G5; Business Premium, Microsoft Defender Suite and Microsoft Purview Suite". |
| LIC-17 | Microsoft Sentinel | Azure separado (E3/E5/E7) | ⚠️ | Mantener "facturado en Azure", con dos matices para E5/E7: (a) beneficio de ingesta sin costo de hasta 5 MB/usuario/día de datos M365 (también A5/F5/G5); (b) desde 23-sep-2026, ISOC en Defender (preview) ofrece capacidades SIEM a clientes Defender Suite/E5/E7 sin workspace Sentinel activo; datos adicionales se cobran. | https://azure.microsoft.com/en-us/pricing/offers/sentinel-microsoft-365-offer/ ; https://learn.microsoft.com/en-us/defender-xdr/isoc-overview | Beneficio: "data grant of up to 5 MB per user per day"; ISOC: Defender Suite, E5 o E7 "that don't have an active Microsoft Sentinel workspace". |
| LIC-18 | Defender for Cloud | Azure separado (E3/E5/E7) | ✅ | Matiz: CSPM básico gratis; Defender CSPM y planes de workload por recurso en Azure. | https://azure.microsoft.com/en-us/pricing/details/defender-for-cloud/ | Página de precios Azure: "Foundational CSPM Free"; Defender CSPM por recurso facturable/mes. |
| LIC-19 | Azure Firewall / WAF | Azure separado (E3/E5/E7) | ✅ | — | https://azure.microsoft.com/en-us/pricing/details/azure-firewall/ ; https://azure.microsoft.com/en-us/pricing/details/web-application-firewall/ | Firewall: tarifa fija por hora + procesamiento de datos; WAF: "you only pay for what you use". |
| LIC-20 | Nota y fuentes del borrador | "Las inclusiones pueden variar..." + 3 URLs de microsoft.com | ✅ | Las 3 URLs existen y abren. Sumar Product Terms (fuente contractual) y el anuncio de empaquetado de jul-2026. | https://www.microsoft.com/en-us/security/pricing/enterprise-plans ; https://www.microsoft.com/en-us/microsoft-365/enterprise/microsoft-365-plans-and-pricing ; https://www.microsoft.com/en-us/microsoft-365/enterprise/compare-microsoft-365-and-office-365 | Las tres páginas cargaron el 4-nov-2026 con precios E3 US$39, E5 US$60 y E7 US$99. |

## A.12 Afirmaciones de texto (todas las secciones)

| ID | Ítem | Afirmación del borrador | Val. | Corrección aplicada | Fuente(s) | Evidencia |
|---|---|---|---|---|---|---|
| TXT-01 | Introducción | Conviene separar tecnologías, mercados y correspondencias | 📝 | Se conserva | — | Criterio metodológico, no fáctico |
| TXT-02 | Introducción | El catálogo puede ser una nueva dimensión del grafo Technology → ProvidesCapability → MarketCategory | 📝 | Se conserva y se amplía en la sección 8 | — | Criterio de diseño |
| TXT-03 | Sección 2 — introducción | Un inventario limitado a Defender omitiría controles fundamentales | 📝 | Se conserva | [W9], [W1] | Intune y Windows aportan controles propios (cumplimiento, cifrado, aislamiento) |
| TXT-04 | Sección 4 — introducción | La lista reúne categorías verificadas en Gartner Peer Insights | ✅ | — | [G0] | Los 38 mercados existen; las 27 URLs citadas abren |
| TXT-05 | Sección 4 — introducción | No es un inventario exhaustivo; los mercados cambian, se fusionan o se retiran | ✅ | — | [G10], [G1], [G11] | XDR retirado; Access Management y SOAR en transición |
| TXT-06 | Sección 5 — introducción | Tres niveles de correspondencia: Directa, Parcial y Complementaria | 📝 | Se conservan; se agregan Sin correspondencia e Histórico y una columna separada de listado en Peer Insights | — | Criterio de clasificación |
| TXT-07 | Sección 5 — cierre | La tabla es un mapeo funcional propuesto, no una afirmación de reconocimiento oficial de Gartner | ✅ | Se refuerza con la columna de listado | [G0] | En 17 de 38 mercados Microsoft no figura |
| TXT-08 | Sección 6 — introducción | Conviene separar los servicios de los productos tecnológicos | 📝 | Se conserva; Security Copilot pasa a productos | [D12] | Security Copilot se licencia por capacidad (SCU) |
| TXT-09 | Sección 7 — introducción | La tabla E3/E5/E7 es una primera aproximación | 📝 | Se reemplaza por la tabla vigente desde el 1-jul-2026 | [L5] | Cambio de empaquetado y precios |
| TXT-10 | Sección 8 | Modelo de cinco entidades y ocho relaciones | 📝 | Se conserva y se amplía (ServicePlan, GartnerListing, LifecycleEvent, Evidence) | [L9] | Identificadores oficiales de SKU y planes de servicio disponibles en Learn |
| TXT-11 | Sección 8 | Cada relación debe registrar fuente, fecha, estado, tipo, cobertura y restricciones de licencia | 📝 | Se conserva y se agregan fecha de actualización de la fuente, tipo de fuente y marca de discrepancia | — | Criterio de diseño |
| TXT-12 | Sección 8 | Cruce Technology × Gartner × Atlas × NIST Function × License | ✅ | Precisar NIST CSF 2.0 y sus seis funciones | [N1] | CSF 2.0 (26-feb-2024): Govern, Identify, Protect, Detect, Respond, Recover |
| TXT-13 | Sección 9.1 | Defender for Cloud participa en CNAPP, CSPM, CWPP y DevSecOps | ✅ | — | [A1], [G20], [G21] | Learn la define como CNAPP con CSPM, DevSecOps y CWPP; Gartner la lista en CNAPP y CSPM |
| TXT-14 | Sección 9.2 | Gartner agrupa capacidades en categorías comerciales | ✅ | — | [G10], [G11] | Mercados retirados y en transición |
| TXT-15 | Sección 9.3 | Una función puede existir técnicamente y requerir un plan adicional | ✅ | — | [E6], [L6] | Entra Agent ID disponible para todos; protecciones para agentes requieren Agent 365 |
| TXT-16 | Sección 9.4 | Entra PIM no cubre todos los escenarios de un PAM especializado | ✅ | — | [E8], [G3] | Alcance de PIM: Entra ID, Azure y servicios en línea de Microsoft; Microsoft no figura en el mercado PAM |
| TXT-17 | Conclusión | Lista de 12 dominios del stack | ⚠️ | La inteligencia de amenazas ya no es un producto separado: está integrada en Defender y Sentinel | [D11] | Portal standalone de MDTI retirado el 1-ago-2026 |
| TXT-18 | Conclusión | Microsoft no debe modelarse como productos que compiten uno a uno con categorías Gartner | ✅ | — | [G0] | Nombres de listado distintos del comercial y 17 mercados sin listado |
| TXT-19 | Conclusión | La correspondencia correcta es de muchos a muchos | ✅ | — | [G20], [G21], [A1] | Un mismo producto figura en varios mercados |
| TXT-20 | Limitación | Selección verificada a noviembre de 2026 | ⚠️ | El borrador contenía elementos desactualizados (MDTI, EOP, empaquetado previo a jul-2026, Dedicated HSM); esta versión documenta la verificación del 4-nov-2026 | [D11], [D5], [L5], [A16] | Ver Anexo A |
| TXT-21 | Limitación | Para uso contractual, validar cada SKU individualmente | ✅ | Prevalecen los Product Terms | [L8] | Ejemplo: prerrequisitos de Agent 365 |

## A.13 Coherencia interna del borrador

| ID | Ítem | Afirmación del borrador | Val. | Corrección aplicada | Fuente(s) | Evidencia |
|---|---|---|---|---|---|---|
| COH-01 | Sección 5 | 9 mercados de la sección 4 no aparecían en la sección 5 | ⚠️ | La sección 5 cubre los 38 mercados | Revisión estructural del borrador | — |
| COH-02 | IT Risk Management | Sección 4: Compliance Manager + Defender for Cloud; sección 5: Compliance Manager + Azure Policy | ⚠️ | Unificado | Revisión estructural del borrador | — |
| COH-03 | Data Security Platforms | Sección 4: Purview y Key Vault; sección 5: Purview + Azure | ⚠️ | Unificado | Revisión estructural del borrador | — |
| COH-04 | NDR | Sección 4: parcial; sección 5: complementaria | ⚠️ | Unificado como complementaria (sin NDR nativo) | Revisión estructural del borrador | — |
| COH-05 | Exposure Assessment Platforms | La sección 4 incluía MDVM; la sección 5, no | ⚠️ | MDVM como capacidad; listado solo Exposure Management | Revisión estructural del borrador | — |
| COH-06 | Adversarial Exposure Validation | Sección 4: sin equivalencia completa; sección 5: parcial | ⚠️ | Unificado como complementaria | Revisión estructural del borrador | — |
| COH-07 | Windows Hello for Business | Aparece en 1.A y en 2.B | ⚠️ | Se mantiene en ambas vistas; en el Atlas, una sola entidad con dos relaciones | Revisión estructural del borrador | — |
| COH-08 | Defender Antivirus | "Microsoft Defender Antivirus" (1.B) y "Windows Defender Antivirus" (2.B) | ⚠️ | Nombre unificado: Microsoft Defender Antivirus | Revisión estructural del borrador | — |
| COH-09 | Defender CSPM | Dos filas para el mismo plan en 3.A | ⚠️ | Se reemplazó una por Foundational CSPM | Revisión estructural del borrador | — |
| COH-10 | Automatización de Sentinel | "Sentinel SOAR" (3.B) y "Sentinel Automation" (4 y 5) | ⚠️ | Nombre unificado | Revisión estructural del borrador | — |
| COH-11 | Defender for AI Services | "Defender for AI Services" (3.A) y "Defender for Cloud AI Security" (4 y 5) | ⚠️ | Nombre unificado | Revisión estructural del borrador | — |
| COH-12 | Purview Data Governance | Nombre de la sección 4 frente a Data Map y Unified Catalog (1.C) | ⚠️ | Purview Data Governance es el nombre del listado; sus componentes son Unified Catalog y Data Map | Revisión estructural del borrador | — |
| COH-13 | Security Copilot | Clasificado como producto (1.B) y como servicio (6) | ⚠️ | Se mantiene solo como producto | Revisión estructural del borrador | — |
| COH-14 | Defender Experts | Experts for Servers y Threat Intelligence solo en la sección 6 | ⚠️ | Servicios consolidados en la sección 6 | Revisión estructural del borrador | — |
| COH-15 | Microsoft 365 Backup y Attack simulation training | Mencionados en 4 y 5, ausentes del inventario | ⚠️ | Agregados (3.B.3 y 1.B) | Revisión estructural del borrador | — |
| COH-16 | Tabla 7 | La fila "Defender for Endpoint P1" ponía "Sí" en E3 y "P2" en E5/E7, mezclando etiqueta y valor | ⚠️ | Corregida: fila "Defender for Endpoint" con P1 / P2 / P2 | Revisión estructural del borrador | — |

## A.14 Verificaciones cruzadas sobre los hallazgos de mayor impacto

Lecturas directas adicionales hechas para confirmar los hallazgos que cambian el licenciamiento o en los que las fuentes podían contradecirse. No se cuentan como afirmaciones del borrador.

| ID | Verificación | Resultado | Fuente |
|---|---|---|---|
| QA-01 | Composición y precio de Microsoft 365 E7 | Incluye E5, Microsoft 365 Copilot, Agent 365 y Entra Suite; US$99; E5 y E7 reciben 400 SCU de Security Copilot por cada 1.000 licencias pagas por mes, hasta 10.000 | [L1] |
| QA-02 | Composición de Microsoft 365 E3 | La página lista Entra ID P1, MDE P1, MDO P1, Intune Plan 1 y Plan 2, Remote Help y **Endpoint Privilege Management**; DLP "para correo y archivos"; US$39. Lo de EPM contradice la nota de licenciamiento (Anexo D) | [L2] |
| QA-03 | Nota de precios y empaquetado 2026 | E3 suma MDO P1, Remote Help, Advanced Analytics e Intune Plan 2; E5 suma además Security Copilot, EPM, Cloud PKI y EAM; precios efectivos el 1-jul-2026; despliegue completo al 1-ago-2026 | [L5] |
| QA-04 | Prerrequisitos de compra de Agent 365 (Product Terms) | Microsoft 365 A5/E5/G5, Business Premium, Defender Suite + Purview Suite (también Edu) o Defender and Purview Suite FLW | [L8] |
| QA-05 | ISOC en Microsoft Defender | En preview; disponible para Defender Suite, E5 o E7 sin workspace de Sentinel activo; 30 días de retención incluidos; la ingesta adicional puede tener cargo; el workspace requiere suscripción de Azure | [D15] |
| QA-06 | Add-ons de seguridad | Defender Suite y Purview Suite: US$12, requieren Microsoft 365 E3 (u Office 365 E3 + EMS E3). Entra Suite: US$12, requiere Entra ID P1. Las capacidades avanzadas de Intune requieren Intune Plan 1 | [L6] |
| QA-07 | Identificadores de licencias | La tabla oficial (act. 19-ago-2026, con CSV) detalla los planes de servicio de AGENT_365 (Defender for AI, Entra para agentes y Purview para agentes) | [L9] |
| QA-08 | Microsoft 365 Backup | Backup de SharePoint, OneDrive y Exchange; pago por uso de US$0,15 por GiB/mes; restauraciones sin cargo | [P21] |
| QA-09 | Attack simulation training | Requiere E5 o Defender for Office 365 Plan 2; E3 solo accede a un subconjunto de prueba | [D6] |
| QA-10 | Alcance de PIM | Acceso just-in-time, con aprobación y vencimiento, a recursos de Entra ID, Azure y otros servicios en línea de Microsoft; la licencia se rige por ID Governance | [E8] |
| QA-11 | NIST CSF 2.0 | Publicado el 26-feb-2024; seis funciones: Govern, Identify, Protect, Detect, Respond y Recover | [N1] |

---

# Anexo B — Cambios, lanzamientos y retiros que afectan el catálogo (2024–2028)

Ordenados por fecha. Las fechas futuras son anuncios oficiales y pueden cambiar.

| Fecha | Producto | Cambio | Impacto en el catálogo | Fuentes |
|---|---|---|---|---|
| 31-dic-2024 | FastTrack for Azure | Retiro del programa | Solo queda FastTrack for Microsoft 365 (sección 6) | [D27] |
| 6-ene-2025 | Purview (gobierno de datos) | Entra en vigor el modelo de pago por uso de Unified Catalog | Data Map y Unified Catalog (1.C) | [P6] |
| 1-abr-2025 / 1-oct-2025 | Entra Permissions Management | Fin de venta y retiro | No incluir como vigente (1.A) | [E10] |
| jul-2025 | Microsoft Sentinel | Los clientes nuevos se incorporan automáticamente al portal de Defender | Sentinel (3.B) | [A9] |
| 30-sep-2025 | Microsoft Sentinel | Sentinel data lake en disponibilidad general | Sentinel (3.B) | [A10] |
| 14-oct-2025 | Windows 10 | Fin de soporte | La sección 2.B asume Windows 11 | [W19] |
| 18-nov-2025 | Security Copilot | Inclusión en Microsoft 365 E5 (despliegue por fases), luego también en E7 | Security Copilot (1.B, 7) | [D26], [L1] |
| 4-dic-2025 | Microsoft 365 | Anuncio de nuevos precios y empaquetado | Sección 7 | [L5] |
| 1-ene-2026 | Defender Experts Suite | Lanzamiento del paquete de servicios | Sección 6 | [D18] |
| 12-feb-2026 | Microsoft Sentinel | Fin de soporte en el portal de Azure extendido al 31-mar-2027 (antes 1-jul-2026) | Sentinel (3.B) | [A30] |
| 9-mar-2026 | Microsoft 365 E7 y Agent 365 | Anuncio oficial | Sección 7 | [L10] |
| 28-abr-2026 | Application Gateway | Retiro de la v1 | 3.B.2 | [A19] |
| 1-may-2026 | Microsoft 365 E7 y Agent 365 | Disponibilidad general (E7 US$99; Agent 365 US$15) | Sección 7 | [L10], [L11], [L14] |
| 5-may-2026 | Defender for Cloud | Integración en el portal de Defender en disponibilidad general | 3.A | [A4] |
| may-2026 | Purview | Nueva versión de DSPM en disponibilidad general (DSPM y DSPM for AI pasan a classic); protecciones para Agent 365 en disponibilidad general | 1.C | [P3] |
| 18-may-2026 | Defender Experts for Servers | Disponibilidad general | Sección 6 | [A4] |
| 1-jun-2026 | Defender for Cloud | Bases relacionales open source en AWS RDS y protección serverless en disponibilidad general | 3.A | [A4] |
| jun-2026 | Secure Boot | Comienzan a vencer los certificados de 2011 | 2.B | [W15] |
| jun-2026 → 1-ago-2026 | Microsoft 365 | Despliegue del nuevo empaquetado (MDO P1 en E3; Intune Plan 2, Remote Help y Advanced Analytics en E3; Security Copilot, EPM, Cloud PKI y EAM en E5) | Secciones 1.B, 2.A y 7 | [L5] |
| 1-jul-2026 | Microsoft 365 | Nuevos precios: E3 US$39, E5 US$60, Entra P1 US$7, Entra P2 US$10, Defender Suite y Purview Suite US$12 | Sección 7 | [L5] |
| 5-jul-2026 | Defender for Cloud | Ya no se pueden habilitar planes deprecados (Kubernetes y Container Registries heredados, Key Vault y Resource Manager heredados, Defender for DNS) | 3.A | [A4] |
| jul-2026 | Purview | Las políticas de protección dejan de soportar Azure SQL Database | 1.C | [P3] |
| 1-ago-2026 | Defender Threat Intelligence | Retiro del portal standalone; la inteligencia queda integrada en Defender XDR y Sentinel | 1.B | [D11] |
| 1-sep-2026 | Defender Experts MDR | En Plan 1 se depreca el enriquecimiento con señales de red de terceros (pasa a Plan 2) | Sección 6 | [D14] |
| sep-2026 | Purview | Network Data Security (con Global Secure Access) en disponibilidad general | 1.C | [P3] |
| 23-sep-2026 | Microsoft Defender | ISOC en Microsoft Defender en preview | 1.B, 7 | [D15] |
| oct-2026 | Windows | Las security baselines habilitan Administrator protection por defecto | 2.B | [W16] |
| oct-2026 | Defender for Endpoint | Descubrimiento de agentes de IA locales en disponibilidad general | Sección 5 (AI Usage Control) | [D17] |
| 20-oct-2026 | Defender for Cloud | Gestión de planes en el portal de Defender (preview), con facturación por DWU | 3.A | [A4] |
| 1-nov-2026 | Defender for Servers | Los dispositivos de escritorio dejan de facturarse en Plan 1 | 3.A | [A4] |
| 14-dic-2026 | Defender for Cloud | Se depreca la recomendación "Machines should have a vulnerability assessment solution" | 3.A | [A4] |
| 6-ene-2027 | Defender for Cloud Apps | Retiro de las file policies (migrar a Purview DLP y etiquetado automático) | 1.B, 1.C | [P3] |
| 31-mar-2027 | Front Door / Sentinel | Retiro de Front Door (classic); fin de soporte de Sentinel en el portal de Azure | 3.B | [A20], [A9] |
| 16-ago-2027 | Defender for SQL | Retiro de las APIs clásicas | 3.A | [A4] |
| 30-sep-2027 | Network security groups | Retiro de NSG flow logs (migrar a VNet flow logs) | 3.B.2 | [A21] |
| 31-jul-2028 | Azure Dedicated HSM | Fin de soporte a clientes existentes | 3.B.4 | [A16] |

---

# Anexo C — Fuentes

Estado: **A** = abierta y leída el 4-nov-2026 · **R** = identificada en resultados de búsqueda, sin lectura completa.

## Licenciamiento y planes

| Código | Fuente | Estado | URL |
|---|---|---|---|
| L1 | Microsoft 365 E7 — composición, precio y Security Copilot incluido | A | https://www.microsoft.com/en-us/microsoft-365/enterprise/e7 |
| L2 | Microsoft 365 E3 — composición y precio | A | https://www.microsoft.com/en-us/microsoft-365/enterprise/e3 |
| L3 | Microsoft 365 E5 — composición y precio | A | https://www.microsoft.com/en-us/microsoft-365/enterprise/e5 |
| L4 | Comparativa oficial de planes E3/E5/E7 | A | https://www.microsoft.com/en-us/microsoft-365/enterprise/microsoft-365-plans-and-pricing |
| L5 | Actualización de precios y empaquetado M365 (efectiva 1-jul-2026) | A | https://www.microsoft.com/en-us/licensing/news/2026-M365-Packaging-Pricing-Updates |
| L6 | Planes de seguridad enterprise y add-ons (Defender/Purview/Entra Suite) | A | https://www.microsoft.com/en-us/security/pricing/enterprise-plans |
| L7 | Comparativa Microsoft 365 vs Office 365 | A | https://www.microsoft.com/en-us/microsoft-365/enterprise/compare-microsoft-365-and-office-365 |
| L8 | Product Terms — Agent 365 (prerrequisitos de compra) | A | https://www.microsoft.com/licensing/terms/en-US/productoffering/Agent365/EAEAS |
| L9 | Identificadores de productos y planes de servicio (act. 19-ago-2026; CSV) | A | https://learn.microsoft.com/en-us/entra/identity/users/licensing-service-plan-reference |
| L10 | Anuncio M365 E7 y Agent 365 (9-mar-2026) | R | https://blogs.microsoft.com/blog/2026/03/09/introducing-the-first-frontier-suite-built-on-intelligence-trust/ |
| L11 | Agent 365 — visión general | R | https://learn.microsoft.com/en-us/microsoft-agent-365/overview |
| L12 | Licensing Guidance — Microsoft Purview | A | https://www.microsoft.com/licensing/guidance/Microsoft-Purview |
| L13 | FAQ del cambio de empaquetado 2026 | R | https://www.microsoft.com/en-us/licensing/news/2026-M365-Packaging-Pricing-Updates-FAQ |
| L14 | Anuncios de Partner Center (índice) | A | https://learn.microsoft.com/en-us/partner-center/announcements/ |

## Microsoft Entra

| Código | Fuente | Estado | URL |
|---|---|---|---|
| E1 | Hub de documentación de Microsoft Entra | A | https://learn.microsoft.com/en-us/entra/ |
| E2 | Entra ID Governance — fundamentos de licenciamiento (act. 16-oct-2026) | A | https://learn.microsoft.com/en-us/entra/id-governance/licensing-fundamentals |
| E3 | Precios de Microsoft Entra | A | https://www.microsoft.com/en-us/security/microsoft-entra-pricing |
| E4 | Global Secure Access — visión general y licencias | A | https://learn.microsoft.com/en-us/entra/global-secure-access/overview-what-is-global-secure-access |
| E5 | Verified ID — precios y Face Check | R | https://learn.microsoft.com/en-us/entra/verified-id/verified-id-pricing |
| E6 | Microsoft Entra Agent ID | R | https://learn.microsoft.com/en-us/entra/agent-id/what-is-microsoft-entra-agent-id |
| E7 | Workload ID — preguntas frecuentes y licencia | A | https://learn.microsoft.com/en-us/entra/workload-id/workload-identities-faqs |
| E8 | ¿Qué es Privileged Identity Management? (act. 23-abr-2026) | A | https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-configure |
| E9 | Escenarios de despliegue de Microsoft Entra Suite | A | https://learn.microsoft.com/en-us/entra/architecture/deployment-scenario-intro |
| E10 | Retiro de Entra Permissions Management (blog oficial, 2-abr-2025) | R | https://techcommunity.microsoft.com/blog/microsoft-entra-blog/microsoft-collaborates-with-delinea-to-offer-cloud-infrastructure-entitlements-m/4400198 |

## Microsoft Defender, Security Copilot y servicios

| Código | Fuente | Estado | URL |
|---|---|---|---|
| D1 | Hub de documentación de Microsoft Defender | A | https://learn.microsoft.com/en-us/defender/ |
| D2 | Defender XDR — requisitos y licencias (act. 7-ago-2026) | A | https://learn.microsoft.com/en-us/defender-xdr/prerequisites |
| D3 | Service description de Microsoft Defender (act. 29-oct-2026) | A | https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-defender-service-description |
| D4 | Service description de Defender for Office 365 (act. 17-jul-2026) | A | https://learn.microsoft.com/en-us/office365/servicedescriptions/office-365-advanced-threat-protection-service-description |
| D5 | Seguridad integrada para buzones en la nube (ex EOP) | A | https://learn.microsoft.com/en-us/defender-office-365/eop-about |
| D6 | Attack simulation training — licencias (act. 3-jul-2026) | A | https://learn.microsoft.com/en-us/defender-office-365/attack-simulation-training-get-started |
| D7 | Defender Vulnerability Management — capacidades por licencia | A | https://learn.microsoft.com/en-us/defender-vulnerability-management/defender-vulnerability-management-capabilities |
| D8 | Defender for IoT — licenciamiento | A | https://learn.microsoft.com/en-us/azure/defender-for-iot/organizations/billing |
| D9 | Security Exposure Management — requisitos | A | https://learn.microsoft.com/en-us/security-exposure-management/prerequisites |
| D10 | Defender EASM — documentación | A | https://learn.microsoft.com/en-us/azure/external-attack-surface-management/ |
| D11 | Threat intelligence en Defender; retiro del portal MDTI (act. 23-sep-2026) | A | https://learn.microsoft.com/en-us/defender-xdr/threat-intelligence-explorer |
| D12 | Security Copilot — SCU y capacidad | A | https://learn.microsoft.com/en-us/copilot/security/security-compute-units-capacity |
| D13 | Familia Defender Experts (act. 27-jul-2026) | A | https://learn.microsoft.com/en-us/defender-xdr/defender-experts/defender-experts-overview |
| D14 | Defender Experts MDR (act. 7-ago-2026) | A | https://learn.microsoft.com/en-us/defender-xdr/defender-experts/defender-experts-mdr-overview |
| D15 | ISOC en Microsoft Defender — preview (act. 23-sep-2026) | A | https://learn.microsoft.com/en-us/defender-xdr/isoc-overview |
| D16 | Microsoft Defender Antivirus en Windows | A | https://learn.microsoft.com/en-us/defender-endpoint/microsoft-defender-antivirus-windows |
| D17 | Novedades de Defender for Endpoint (act. 30-oct-2026) | A | https://learn.microsoft.com/en-us/defender-endpoint/whats-new-in-microsoft-defender-endpoint |
| D18 | Lanzamiento de Defender Experts Suite (6-ene-2026) | A | https://www.microsoft.com/en-us/security/blog/2026/01/06/introducing-the-microsoft-defender-experts-suite-elevate-your-security-with-expert-led-services/ |
| D19 | FastTrack for Microsoft 365 — elegibilidad | A | https://learn.microsoft.com/en-us/microsoft-365/fasttrack/eligibility |
| D20 | Microsoft Unified (Unified Enterprise, VAS, MCS) | R | https://www.microsoft.com/en-us/microsoft-unified |
| D21 | Iniciativa EASM en Security Exposure Management | R | https://learn.microsoft.com/en-us/security-exposure-management/external-attack-surface-management-initiative |
| D22 | Defender Experts for Servers | R | https://learn.microsoft.com/en-us/defender-xdr/defender-experts/defender-experts-servers-overview |
| D23 | Defender for Endpoint — requisitos mínimos y licencias de servidores | A | https://learn.microsoft.com/en-us/defender-endpoint/minimum-requirements |
| D24 | Defender Experts Cybersecurity Incident Response (Microsoft Incident Response) | R | https://www.microsoft.com/en-us/security/business/microsoft-defender-experts-cybersecurity-incident-response |
| D25 | Beneficio de Sentinel para clientes Microsoft 365 E5/E7 | R | https://azure.microsoft.com/en-us/pricing/offers/sentinel-microsoft-365-offer/ |
| D26 | Inclusión de Security Copilot en Microsoft 365 E5/E7 | R | https://learn.microsoft.com/en-us/copilot/security/security-copilot-inclusion |
| D27 | Retiro de FastTrack for Azure (31-dic-2024) | R | https://techcommunity.microsoft.com/blog/fasttrackforazureblog/fasttrack-for-azure-fta-program-retiring-december-2024/4357383 |

## Microsoft Purview y resiliencia de Microsoft 365

| Código | Fuente | Estado | URL |
|---|---|---|---|
| P1 | Service description de Microsoft Purview (versión zh-CN completa act. 3-ago-2026 usada donde la en-US se truncó) | A | https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description |
| P2 | Modelos de facturación de Purview (pay-as-you-go) | A | https://learn.microsoft.com/en-us/purview/purview-billing-models |
| P3 | Novedades de Microsoft Purview (act. 16-oct-2026) | A | https://learn.microsoft.com/en-us/purview/whats-new |
| P4 | DSPM — nueva versión | A | https://learn.microsoft.com/en-us/purview/data-security-posture-management-learn-about |
| P5 | Data Security Investigations — facturación (act. 11-jun-2026) | A | https://learn.microsoft.com/en-us/purview/data-security-investigations-billing |
| P6 | Facturación de gobierno de datos (Unified Catalog, Data Map) | A | https://learn.microsoft.com/en-us/purview/data-governance-billing |
| P7 | Portal de Microsoft Purview (act. 5-ago-2026) | A | https://learn.microsoft.com/en-us/purview/purview-portal |
| P8 | Purview para IA generativa (act. 27-may-2026) | A | https://learn.microsoft.com/en-us/purview/ai-microsoft-purview |
| P9 | Soluciones de auditoría (Standard/Premium) | A | https://learn.microsoft.com/en-us/purview/audit-solutions-overview |
| P10 | eDiscovery (act. 29-jun-2026) | A | https://learn.microsoft.com/en-us/purview/edisc |
| P11 | Compliance Manager — plantillas y licencias | A | https://learn.microsoft.com/en-us/purview/compliance-manager-regulations-list |
| P12 | Precios de Microsoft Purview (Azure) | A | https://azure.microsoft.com/en-us/pricing/details/purview/ |
| P13 | Purview — cumplimiento (fuente citada por el borrador) | A | https://learn.microsoft.com/en-us/purview/purview-compliance |
| P14 | Purview — seguridad de datos (fuente citada por el borrador) | A | https://learn.microsoft.com/en-us/purview/purview-security |
| P15 | Purview — visión general (fuente citada por el borrador) | A | https://learn.microsoft.com/en-us/purview/purview |
| P16 | Service description de Microsoft Priva (act. 11-may-2026) | A | https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-priva-service-description |
| P17 | Adaptive Protection | A | https://learn.microsoft.com/en-us/purview/insider-risk-management-adaptive-protection |
| P18 | Double Key Encryption (act. 27-oct-2026) | A | https://learn.microsoft.com/en-us/purview/double-key-encryption |
| P19 | Data Estate Insights (classic) | A | https://learn.microsoft.com/en-us/purview/legacy/concept-insights |
| P20 | Data Security Investigations (act. 22-jun-2026) | A | https://learn.microsoft.com/en-us/purview/data-security-investigations |
| P21 | Microsoft 365 Backup (act. 18-ago-2026) | A | https://learn.microsoft.com/en-us/microsoft-365/backup/backup-overview |

## Microsoft Intune y Windows

| Código | Fuente | Estado | URL |
|---|---|---|---|
| W1 | Licencias de Intune (Plan 1, Plan 2, Suite) | A | https://learn.microsoft.com/en-us/intune/fundamentals/licensing |
| W2 | Capacidades avanzadas de Intune | A | https://learn.microsoft.com/en-us/intune/fundamentals/advanced-capabilities |
| W3 | Precios de Intune y FAQ de inclusión en E3/E5 | A | https://www.microsoft.com/en-us/security/microsoft-intune-pricing |
| W4 | Políticas de seguridad de endpoint en Intune | A | https://learn.microsoft.com/en-us/intune/device-configuration/endpoint-security/manage-policies |
| W5 | Políticas de protección de apps (MAM) | A | https://learn.microsoft.com/en-us/intune/app-management/protection/overview |
| W6 | Políticas de cumplimiento de dispositivos | A | https://learn.microsoft.com/en-us/intune/device-security/compliance/overview |
| W7 | Windows Autopilot | A | https://learn.microsoft.com/en-us/autopilot/overview |
| W8 | Windows Autopatch — requisitos (act. 26-feb-2026) | A | https://learn.microsoft.com/en-us/windows/deployment/windows-autopatch/prepare/windows-autopatch-prerequisites |
| W9 | Seguridad de Windows — requisitos de edición y licencia | A | https://learn.microsoft.com/en-us/windows/security/licensing-and-edition-requirements |
| W10 | Documentación de seguridad de Windows (fuente citada por el borrador) | A | https://learn.microsoft.com/en-us/windows/security/ |
| W11 | Configurar Credential Guard (fuente citada por el borrador) | A | https://learn.microsoft.com/en-us/windows/security/identity-protection/credential-guard/configure |
| W12 | App Control for Business y AppLocker (fuente citada por el borrador) | A | https://learn.microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/appcontrol-and-applocker-overview |
| W13 | Windows Firewall | A | https://learn.microsoft.com/en-us/windows/security/operating-system-security/network-security/windows-firewall/ |
| W14 | Personal Data Encryption | A | https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/personal-data-encryption/ |
| W15 | Actualización de certificados de Secure Boot (vencimiento 2026) | R | https://learn.microsoft.com/en-us/troubleshoot/windows-client/windows-security/update-secure-boot-certificates |
| W16 | Administrator protection | A | https://learn.microsoft.com/en-us/windows/security/application-security/application-control/administrator-protection/ |
| W17 | Protección adicional de LSA | A | https://learn.microsoft.com/en-us/windows-server/security/credentials-protection-and-management/configuring-additional-lsa-protection |
| W18 | Hotpatch con Windows Autopatch | A | https://learn.microsoft.com/en-us/windows/deployment/windows-autopatch/manage/windows-autopatch-hotpatch-updates |
| W19 | Windows LAPS | A | https://learn.microsoft.com/en-us/windows-server/identity/laps/laps-overview |
| W20 | Credential Guard — visión general | A | https://learn.microsoft.com/en-us/windows/security/identity-protection/credential-guard/ |
| W21 | Reglas de reducción de superficie de ataque | A | https://learn.microsoft.com/en-us/defender-endpoint/attack-surface-reduction-rules-overview |
| W22 | Windows Sandbox | A | https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/ |
| W23 | Smart App Control | A | https://learn.microsoft.com/en-us/windows/apps/develop/smart-app-control/overview |
| W24 | Windows Hello Enhanced Sign-in Security | A | https://learn.microsoft.com/en-us/windows-hardware/design/device-experiences/windows-hello-enhanced-sign-in-security |
| W25 | Kernel DMA Protection | A | https://learn.microsoft.com/en-us/windows/security/hardware-security/kernel-dma-protection-for-thunderbolt |
| W26 | Secured-core PC configuration lock | A | https://learn.microsoft.com/en-us/windows/client-management/config-lock |
| W27 | Quick machine recovery | R | https://learn.microsoft.com/en-us/windows/configuration/quick-machine-recovery/ |
| W28 | Microsoft Pluton | A | https://learn.microsoft.com/en-us/windows/security/hardware-security/pluton/microsoft-pluton-security-processor |
| W29 | Integridad de memoria (HVCI) | A | https://learn.microsoft.com/en-us/windows/security/hardware-security/enable-virtualization-based-protection-of-code-integrity |
| W30 | Controlled folder access | A | https://learn.microsoft.com/en-us/defender-endpoint/controlled-folder-access-overview |
| W31 | Microsoft Defender SmartScreen | A | https://learn.microsoft.com/en-us/windows/security/operating-system-security/virus-and-threat-protection/microsoft-defender-smartscreen/ |
| W32 | Requisitos de hardware para VBS (guía OEM) | A | https://learn.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-vbs |
| W33 | Trusted Platform Module | A | https://learn.microsoft.com/en-us/windows/security/hardware-security/tpm/trusted-platform-module-overview |
| W34 | Windows security baselines | A | https://learn.microsoft.com/en-us/windows/security/operating-system-security/device-management/windows-security-configuration-framework/windows-security-baselines |

## Azure y Defender for Cloud

| Código | Fuente | Estado | URL |
|---|---|---|---|
| A1 | Defender for Cloud — introducción | A | https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-cloud-introduction |
| A2 | CSPM: Foundational CSPM y Defender CSPM | A | https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-cloud-security-posture-management |
| A3 | Precios de Defender for Cloud | A | https://azure.microsoft.com/en-us/pricing/details/defender-for-cloud/ |
| A4 | Novedades de Defender for Cloud | A | https://learn.microsoft.com/en-us/azure/defender-for-cloud/release-notes |
| A5 | DevOps security en Defender for Cloud | A | https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-devops-introduction |
| A6 | Asignación de estándares de cumplimiento | A | https://learn.microsoft.com/en-us/azure/defender-for-cloud/assign-regulatory-compliance-standards |
| A7 | Defender for APIs | A | https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-apis-introduction |
| A8 | Protección contra amenazas para servicios de IA | A | https://learn.microsoft.com/en-us/azure/defender-for-cloud/ai-threat-protection |
| A9 | Microsoft Sentinel — visión general (act. 14-may-2026) | A | https://learn.microsoft.com/en-us/azure/sentinel/overview |
| A10 | Microsoft Sentinel data lake | A | https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-lake-overview |
| A11 | Azure Firewall — SKU | A | https://learn.microsoft.com/en-us/azure/firewall/choose-firewall-sku |
| A12 | Azure DDoS Protection — niveles | A | https://learn.microsoft.com/en-us/azure/ddos-protection/ddos-protection-sku-comparison |
| A13 | Azure Web Application Firewall | A | https://learn.microsoft.com/en-us/azure/web-application-firewall/overview |
| A14 | Elegir solución de administración de claves en Azure | A | https://learn.microsoft.com/en-us/azure/security/fundamentals/key-management-choose |
| A15 | Private endpoint (componente de Private Link) | A | https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview |
| A16 | Azure Dedicated HSM — retiro | A | https://learn.microsoft.com/en-us/azure/dedicated-hsm/overview |
| A17 | Azure Cloud HSM | A | https://learn.microsoft.com/en-us/azure/cloud-hsm/overview |
| A18 | Servicios y tecnologías de seguridad en Azure | A | https://learn.microsoft.com/en-us/azure/security/fundamentals/services-technologies |
| A19 | Application Gateway (retiro de v1) | A | https://learn.microsoft.com/en-us/azure/application-gateway/overview |
| A20 | Retiro de Azure Front Door (classic) | A | https://learn.microsoft.com/en-us/azure/frontdoor/classic-retirement-faq |
| A21 | Network security groups (retiro de NSG flow logs) | A | https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview |
| A22 | Network Security Perimeter | A | https://learn.microsoft.com/en-us/azure/private-link/network-security-perimeter-concepts |
| A23 | Azure Firewall Manager | A | https://learn.microsoft.com/en-us/azure/firewall-manager/overview |
| A24 | Prompt Shields (Azure AI Content Safety) | A | https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection |
| A25 | Microsoft cloud security benchmark | A | https://learn.microsoft.com/en-us/security/benchmark/azure/introduction |
| A26 | Defender for Cloud en el portal de Defender | A | https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-portal/defender-for-cloud-defender-portal |
| A27 | Azure Migrate | A | https://learn.microsoft.com/en-us/azure/migrate/migrate-services-overview |
| A28 | Azure Backup | A | https://learn.microsoft.com/en-us/azure/backup/backup-overview |
| A29 | Azure DNS resolver policy | A | https://learn.microsoft.com/en-us/azure/dns/dns-security-policy |
| A30 | Partner Center feb-2026 (extensión del retiro de Sentinel en portal de Azure) | A | https://learn.microsoft.com/en-us/partner-center/announcements/2026-february |
| A31 | Azure Private Link | A | https://learn.microsoft.com/en-us/azure/private-link/private-link-overview |
| A32 | Seguridad de red en Azure (fuente citada por el borrador) | A | https://learn.microsoft.com/en-us/azure/networking/security/network-security |
| A33 | Proteger Azure Key Vault (fuente citada por el borrador) | A | https://learn.microsoft.com/en-us/azure/key-vault/general/secure-key-vault |
| A34 | Módulo de entrenamiento de planes de protección (fuente citada por el borrador) | A | https://learn.microsoft.com/en-us/training/modules/enable-configure-workload-protection-plans/ |
| A35 | Hub de Defender for Cloud (fuente citada por el borrador) | A | https://learn.microsoft.com/en-us/azure/defender-for-cloud/ |
| A36 | Defender for DNS | A | https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-dns-introduction |
| A37 | Azure Bastion | A | https://learn.microsoft.com/en-us/azure/bastion/bastion-overview |
| A38 | Azure Confidential Computing | A | https://learn.microsoft.com/en-us/azure/confidential-computing/overview |
| A39 | Azure Attestation | A | https://learn.microsoft.com/en-us/azure/attestation/overview |
| A40 | Azure Confidential Ledger | A | https://learn.microsoft.com/en-us/azure/confidential-ledger/overview |
| A41 | Azure Virtual Network Manager | A | https://learn.microsoft.com/en-us/azure/virtual-network-manager/overview |
| A42 | Azure Policy | A | https://learn.microsoft.com/en-us/azure/governance/policy/overview |
| A43 | Azure RBAC | A | https://learn.microsoft.com/en-us/azure/role-based-access-control/overview |
| A44 | Azure Monitor | A | https://learn.microsoft.com/en-us/azure/azure-monitor/fundamentals/overview |
| A45 | Azure Monitor Logs | A | https://learn.microsoft.com/en-us/azure/azure-monitor/logs/data-platform-logs |
| A46 | Azure Arc | A | https://learn.microsoft.com/en-us/azure/azure-arc/overview |
| A47 | Azure Update Manager | A | https://learn.microsoft.com/en-us/azure/update-manager/overview |
| A48 | Azure API Management | A | https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts |
| A49 | Azure Site Recovery | A | https://learn.microsoft.com/en-us/azure/site-recovery/site-recovery-overview |
| A50 | Azure Front Door | A | https://learn.microsoft.com/en-us/azure/frontdoor/front-door-overview |

## Marcos de referencia

| Código | Fuente | Estado | URL |
|---|---|---|---|
| N1 | NIST CSF 2.0 — seis funciones (26-feb-2024) | A | https://www.nist.gov/news-events/news/2024/02/nist-releases-version-20-landmark-cybersecurity-framework |

## Gartner Peer Insights

| Código | Página | Estado | URL |
|---|---|---|---|
| G0 | Página del proveedor Microsoft (lectura completa de los mercados A–G) | A | https://www.gartner.com/reviews/vendor/microsoft |
| G1 | Mercado: Access Management (Transitioning to Customer Identity and Access Management (CIAM)) | A | https://www.gartner.com/reviews/market/access-management |
| G2 | Mercado: Identity Governance and Administration | A | https://www.gartner.com/reviews/market/identity-governance-administration |
| G3 | Mercado: Privileged Access Management | A | https://www.gartner.com/reviews/market/privileged-access-management |
| G4 | Mercado: Identity Threat Detection and Response (ITDR) | A | https://www.gartner.com/reviews/market/identity-threat-detection-and-response-itdr |
| G5 | Mercado: Endpoint Protection (antes Endpoint Protection Platforms) | A | https://www.gartner.com/reviews/market/endpoint-protection-platforms/vendor/microsoft |
| G6 | Mercado: Endpoint Management Tools | A | https://www.gartner.com/reviews/market/endpoint-management-tools |
| G7 | Mercado: Security Awareness Computer-Based Training | A | https://www.gartner.com/reviews/market/security-awareness-computer-based-training |
| G8 | Mercado: Security Information and Event Management | A | https://www.gartner.com/reviews/market/security-information-event-management |
| G9 | Mercado: Integrated Security Operations Center Solutions | A | https://www.gartner.com/reviews/market/integrated-security-operations-center-solutions |
| G10 | Mercado: Extended Detection and Response (Retired) | A | https://www.gartner.com/reviews/market/extended-detection-and-response/vendor/microsoft |
| G11 | Mercado: Security Orchestration, Automation and Response Solutions (Transitioning to Security Information and Event Management) | A | https://www.gartner.com/reviews/market/security-orchestration-automation-and-response-solutions |
| G12 | Mercado: Network Detection and Response | A | https://www.gartner.com/reviews/market/network-detection-and-response |
| G13 | Mercado: Managed Detection and Response | A | https://www.gartner.com/reviews/market/managed-detection-and-response |
| G14 | Mercado: Co-Managed Security Monitoring Services | A | https://www.gartner.com/reviews/market/co-managed-security-monitoring-services |
| G15 | Mercado: Cybersecurity Incident Response Management | A | https://www.gartner.com/reviews/market/cybersecurity-incident-response-management |
| G16 | Mercado: External Attack Surface Management | A | https://www.gartner.com/reviews/market/external-attack-surface-management |
| G17 | Mercado: Cyber Asset Attack Surface Management (CAASM) | A | https://www.gartner.com/reviews/market/cyber-asset-attack-surface-management |
| G18 | Mercado: Exposure Assessment Platforms | A | https://www.gartner.com/reviews/market/exposure-assessment-platforms |
| G19 | Mercado: Adversarial Exposure Validation | A | https://www.gartner.com/reviews/market/adversarial-exposure-validation |
| G20 | Mercado: Cloud-Native Application Protection Platforms | A | https://www.gartner.com/reviews/market/cloud-native-application-protection-platforms |
| G21 | Mercado: Cloud Security Posture Management Tools | A | https://www.gartner.com/reviews/market/cloud-security-posture-management-tools |
| G22 | Mercado: Security Service Edge | A | https://www.gartner.com/reviews/market/security-service-edge |
| G23 | Mercado: SASE Platforms (la URL conserva el nombre anterior single-vendor-sase) | A | https://www.gartner.com/reviews/market/single-vendor-sase |
| G24 | Mercado: Network Security Microsegmentation | A | https://www.gartner.com/reviews/market/network-security-microsegmentation |
| G25 | Mercado: Cloud Web Application and API Protection | A | https://www.gartner.com/reviews/market/cloud-web-application-and-api-protection |
| G26 | Mercado: AI Application Security | A | https://www.gartner.com/reviews/market/ai-application-security |
| G27 | Mercado: AI Usage Control | A | https://www.gartner.com/reviews/market/ai-usage-control |
| G28 | Mercado: Data Loss Prevention | A | https://www.gartner.com/reviews/market/data-loss-prevention |
| G29 | Mercado: Data Security Posture Management | A | https://www.gartner.com/reviews/market/data-security-posture-management |
| G30 | Mercado: Data Security Platforms | A | https://www.gartner.com/reviews/market/data-security-platforms |
| G31 | Mercado: Email Security | A | https://www.gartner.com/reviews/market/email-security |
| G32 | Mercado: Digital Communications Governance and Archiving Solutions | A | https://www.gartner.com/reviews/market/digital-communications-governance-and-archiving-solutions |
| G33 | Mercado: Data and Analytics Governance Platforms | A | https://www.gartner.com/reviews/market/data-and-analytics-governance-platforms |
| G34 | Mercado: Privacy UX | A | https://www.gartner.com/reviews/market/privacy-ux |
| G35 | Mercado: Microsoft 365 Governance Tools | A | https://www.gartner.com/reviews/market/microsoft-365-governance-tools |
| G36 | Mercado: Backup and Data Protection Platforms | A | https://www.gartner.com/reviews/market/backup-and-data-protection-platforms |
| G37 | Mercado: IT Risk Management (ITRM) | A | https://www.gartner.com/reviews/market/it-risk-management-solutions |
| G38 | Mercado: Security Consulting Services, Worldwide | A | https://www.gartner.com/reviews/market/security-consulting-services-worldwide |
| G39 | Productos Microsoft en la categoría genérica IT Security | A | https://www.gartner.com/reviews/market/it-security/vendor/microsoft |
| G40 | Ficha: Microsoft Defender Suite | A | https://www.gartner.com/reviews/product/microsoft-defender-suite-1683939452 |
| G41 | Ficha: Microsoft Purview eDiscovery | A | https://www.gartner.com/reviews/product/microsoft-purview-ediscovery |
| G42 | Ficha: Azure Firewall | A | https://www.gartner.com/reviews/product/azure-firewall |
| G43 | Ficha: Microsoft Defender for IoT | A | https://www.gartner.com/reviews/product/microsoft-defender-for-iot |
| G44 | Ficha: Microsoft Defender Vulnerability Management | A | https://www.gartner.com/reviews/product/microsoft-defender-vulnerability-management |
| G45 | Ficha: Microsoft Purview | A | https://www.gartner.com/reviews/product/microsoft-purview-1861237758 |
| G46 | Ficha: Microsoft Entra ID | A | https://www.gartner.com/reviews/product/microsoft-entra-id |
| G47 | Ficha: Microsoft Defender for Endpoint | A | https://www.gartner.com/reviews/product/microsoft-defender-for-endpoint |

---

# Anexo D — Discrepancias entre fuentes oficiales, método y limitaciones

## D.1 Discrepancias entre fuentes oficiales

| # | Tema | Qué dice cada fuente | Criterio adoptado | Fuentes |
|---|---|---|---|---|
| 1 | Endpoint Privilege Management en E3 | La página de producto de E3 lo lista; la nota de licenciamiento 2026, la FAQ de precios de Intune y la comparativa Microsoft 365 vs Office 365 lo ubican solo en E5 | Se adopta la nota de licenciamiento (E5/E7). Confirmar en Product Terms o en el tenant (Intune admin center > Intune add-ons) | [L2], [L5], [W3], [L7] |
| 2 | Remote Help y Advanced Analytics frente a Intune Plan 2 | La página de licencias de Intune en Learn los describe dentro de Plan 2; la página de precios los vende por separado y define Plan 2 como Tunnel for MAM, dispositivos especializados y firmware | No se atribuyen a Plan 2; en E3/E5/E7 vienen incluidos desde jul-2026 | [W1], [W3], [L6] |
| 3 | Prerrequisito de Agent 365 | Los Product Terms exigen E5/A5/G5, Business Premium o Defender Suite + Purview Suite; la página de licencias de ID Governance en Learn aún cita P1/E3 como prerrequisito técnico | Prevalecen los Product Terms | [L8], [E2] |
| 4 | Estado de DSPM | La página general de Purview (act. 15-may-2026) lo marca en preview; Novedades de Purview lo da en disponibilidad general desde mayo de 2026 | Disponibilidad general | [P15], [P3] |
| 5 | Nombres de Defender Experts y MDTI | La service description de Defender (act. 29-oct-2026) conserva "Defender Experts for XDR/Hunting" y la tabla de MDTI; la documentación de producto refleja el renombre a Defender Experts MDR y el retiro de MDTI | Se adopta la documentación de producto más reciente | [D3], [D14], [D11] |
| 6 | SKU de Defender Threat Intelligence | La tabla de identificadores de licencias (act. 19-ago-2026) todavía lista el SKU, aunque el portal standalone se retiró el 1-ago-2026 | Se registra como identificador histórico, no como producto vigente | [L9], [D11] |
| 7 | "Defender for DevOps" | El índice de Learn y el catálogo de servicios de seguridad de Azure aún usan el nombre heredado; el artículo vigente se titula "DevOps security" y no hay plan con precio propio | DevOps security como capacidad de CSPM | [A35], [A18], [A5] |
| 8 | Fecha de retiro de Defender for Cloud en Azure operado por 21Vianet | Learn indica el 1-oct-2026; un aviso previo de Azure Updates decía 18-ago-2026 | Prevalece Learn (más reciente) | [A4] |
| 9 | Autopatch y Hotpatch en Windows Pro | La tabla general de licencias de Windows los marca para Pro; las páginas específicas exigen licencias Enterprise u otras calificadas | Prevalecen las páginas específicas | [W9], [W8], [W18] |
| 10 | Nombre de la suite de seguridad | La página de elegibilidad de FastTrack aún dice "Microsoft 365 E5 Security"; el resto de las fuentes usa "Microsoft Defender Suite" | Microsoft Defender Suite | [D19], [L6] |

## D.2 Método

- **Alcance:** 255 elementos del borrador (filas de tablas, notas, afirmaciones de texto e inconsistencias internas), registrados uno por uno en el Anexo A.
- **Fuentes, en orden de prelación:** Product Terms y notas oficiales de licenciamiento; documentación de Microsoft Learn y service descriptions; páginas oficiales de producto y precios; blogs oficiales de Microsoft. Para los mercados, Gartner Peer Insights. Las fuentes de terceros se usaron solo como pista y nunca como única evidencia.
- **Microsoft Learn:** el servidor MCP de Microsoft Learn no estaba disponible en esta sesión; se consultó directamente el mismo contenido público de learn.microsoft.com.
- **Evidencia:** las páginas se leyeron el 4-nov-2026. En el Anexo C cada fuente indica si se abrió y leyó (A) o si solo se identificó en resultados de búsqueda (R). Los hallazgos que dependen solo de fuentes R están señalados en el registro.
- **Contenido de terceros:** no se reproduce contenido de Gartner; solo nombres de mercados y de productos listados.

## D.3 Limitaciones

- **Gartner Peer Insights:** la página del proveedor Microsoft solo pudo leerse completa para los mercados de la A a la G; el resto se verificó con la página de cada mercado y las fichas de producto. Peer Insights puede listar productos sin reseñas que no son visibles en mercados grandes, por lo que "no figura" tiene confianza alta pero no absoluta. En ISOC, Cybersecurity Incident Response Management y Microsoft 365 Governance Tools todos los productos son visibles, así que ahí la ausencia es completa.
- **Precios:** son de lista en USD con compromiso anual; varían por país, moneda, programa y contrato. Los clientes existentes mantienen su precio hasta la renovación.
- **Nubes de gobierno:** el empaquetado y la disponibilidad difieren (ver sección 7).
- **Service description de Purview:** la versión en inglés se truncó al leerla; para etiquetado, Double Key Encryption, cifrado de correo e Insider Risk Management se usó la misma service description traducida al chino (act. 3-ago-2026).
- **Vigencia:** el catálogo refleja el 4-nov-2026. Revisar el Anexo B para los eventos con fecha futura.

































----





Santiago, 1 2 3 4 ya está listo el Markdown corregido: **Catalogo_Seguridad_Microsoft_x_Gartner_v2_validado_2026-11-04.md**. Contiene el catálogo completo con las correcciones aplicadas. Tiene además un registro donde cada afirmación del borrador figura con su veredicto, la corrección y la fuente, una línea de tiempo de cambios y retiros y la lista de fuentes oficiales.

**Resultado:** revisé las 239 afirmaciones del borrador. 8 son criterios de diseño o de método, sin hechos que verificar. De las otras 231:

- 148 son correctas.
- 71 eran correctas pero necesitaban un matiz.
- 8 estaban desactualizadas.
- 3 eran incorrectas.
- 1 no se pudo verificar y la eliminé.

Además encontré y corregí 16 inconsistencias internas, como mercados que faltaban en la tabla consolidada, filas duplicadas o un mismo producto con dos nombres.

**Correcciones principales:**

- **E3/E5/E7:** la tabla describía el empaquetado anterior a julio. Desde el 1-jul-2026, E3 suma Defender for Office 365 Plan 1, Remote Help, Advanced Analytics e Intune Plan 2, y E5 agrega Security Copilot, Endpoint Privilege Management, Cloud PKI y Enterprise Application Management.
- **Security Copilot:** E5 y E7 reciben 400 SCU por cada 1.000 licencias pagas por mes, hasta 10.000.
- **Entra Suite:** el borrador decía "No" para E3, pero solo requiere Entra ID P1.
- **Agent 365:** exige E5/A5/G5, Business Premium o Defender Suite más Purview Suite. Con E3 solo no alcanza.
- **Retiros y renombres:**
  - El portal standalone de Defender Threat Intelligence se retiró el 1-ago-2026.
  - Dedicated HSM está en retiro y lo reemplaza Cloud HSM.
  - Data Estate Insights ahora se llama "Reports".
  - Data Security Investigations se cobra solo por consumo.
  - Defender for Cloud tenía Defender CSPM duplicado y le faltaba Foundational CSPM.
- **SIEM integrado:** el SIEM integrado en el portal de Defender (en preview) está disponible para E5, E7 o Defender Suite sin un workspace de Sentinel activo.
- **Gartner:** los 38 mercados existen, pero Microsoft figura listado solo en 21. Separé en dos columnas la correspondencia funcional y el listado de Gartner.

**Puntos a confirmar:**

- **Endpoint Privilege Management en E3:**  5la página de producto de E3 lo incluye, pero la nota oficial de licenciamiento lo ubica solo en E5. Usé la nota de licenciamiento; conviene confirmarlo en los Product Terms o en el tenant.
- **Beneficio de ingesta de Sentinel para E5/E7:** solo lo vi en resultados de búsqueda; no abrí la página para confirmarlo.

El servidor MCP de Microsoft Learn no estaba disponible en esta sesión. Por eso leí directamente las páginas de learn.microsoft.com, además de los Product Terms, las páginas oficiales de precios y Gartner Peer Insights. Quedó abierta una pestaña de Gartner en tu navegador; podés cerrarla.

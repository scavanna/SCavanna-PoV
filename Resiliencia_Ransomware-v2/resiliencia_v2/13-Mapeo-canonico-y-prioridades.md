# 13. Registro canónico, prioridades organizacionales y matrices de correlación

**Propósito:** conectar de forma portable este paquete (`PKG-RANSOM` v2.0) con **Modelo Operativo CISO 365** (`PKG-CISO365`), **KPIs y OKRs del CISO de Empresa de Frontera** (`PKG-KPI-OKR`) y **Ninja Training de Seguridad Microsoft 2026** (`PKG-NINJA`), usando exclusivamente **nombres canónicos e identificadores estables** para que funcionen con independencia de la carpeta o URL definitiva donde se alojen.

## 1. Convención de referencias canónicas sin ruta fija

Mientras no se defina la estructura definitiva de carpetas o sitios de publicación, toda referencia entre artefactos utiliza la sintaxis:

`PAQUETE_CANONICO :: ARTEFACTO_CANONICO [Hoja o Sección] :: ID_ESTABLE`

Ejemplos:
- `PKG-CISO365 :: AI_CISO_Atlas_CISO365_Plan_y_Ciclo_Anual_v1.0.xlsx [Plan 365] :: ACT-041`
- `PKG-KPI-OKR :: AI_CISO_Atlas_KPIs_OKRs_CISO_de_Frontera_v1.2_2026-11-10.xlsx [Catalogo_KPI] :: K28`
- `PKG-NINJA :: 02_Defender_XDR/Defender_XDR_Ninja_Training_2026 :: M7, A1, A8`

En `03-Correlacion-Prioridades-FullMS-Ninja.xlsx` (hoja `Artefactos_Canonicos`) y en `Mapa-de-correlacion-y-prioridades.html` existe un campo opcional de **ubicación base** por paquete para resolver rutas locales o URLs automáticamente cuando se decida su destino final.

| Paquete | ID canónico | Nombre canónico del artefacto | Tipo y versión | Propósito operativo | Prefijos / IDs |
|---|---|---|---|---|---|
| `PKG-RANSOM` | `RANSOM-README` | `README.md + Guías 01 a 15 (.md)` | Serie Markdown · v2.0 (2026-11-12) | Gobierno, evaluación, controles, SOC/IR, forense, continuidad, comunicaciones, Full Microsoft y plan Ninja | `CT-01..21; DE-01..13; PB-01..07; SRC-01..09; E1..E3` |
| `PKG-RANSOM` | `RANSOM-XLSX-01` | `01-Evaluacion-y-controles.xlsx` | Libro Excel · v2.0 | BIA, catálogo CT-01..21 enriquecido, evaluaciones por corte, plan de brechas y referencias | `CT-01..21; MS-01..10; EXT-01..03; INT-01..04` |
| `PKG-RANSOM` | `RANSOM-XLSX-02` | `02-Operacion-y-pruebas.xlsx` | Libro Excel · v2.0 | Fuentes SRC-01..09, detecciones DE-01..13, incidentes, decisiones DD##, evidencia, comunicaciones, pruebas y competencias | `SRC-01..09; DE-01..13; PB-01..07; T-01..04; E1..E3; ROL-01..09` |
| `PKG-RANSOM` | `RANSOM-XLSX-03` | `03-Correlacion-Prioridades-FullMS-Ninja.xlsx` | Libro Excel · v2.0 | Matrices 360° de correlación con CISO 365, KPIs/OKRs, prioridades por sector, arquitectura operativa Full Microsoft y rutas Ninja | `PKG-*; MS-CAP-01..12; NT-01..15` |
| `PKG-RANSOM` | `RANSOM-JSON` | `Catalogo-correlacion-v2.json` | Catálogo JSON · v2.0 | Grafo estructurado portable de artefactos canónicos, controles, detecciones, playbooks, stack Full Microsoft, sectores y rutas Ninja | `Esquema ransomware-resiliencia-v2` |
| `PKG-RANSOM` | `RANSOM-HTML-01` | `Panel-de-resiliencia.html` | App HTML local · v2.0 | Explorador de controles CT-01..21 y BIA con filtros por fase CISO 365, pregunta del directorio, capa Full Microsoft y programa Ninja | `CT-01..21; Q1..Q6; F0..F6` |
| `PKG-RANSOM` | `RANSOM-HTML-02` | `Mapa-de-correlacion-y-prioridades.html` | App HTML local · v2.0 | Planificador interactivo por sector, horizonte 365 y rol: prioridades KPI/OKR, matriz 360°, calculadora de horas Ninja y operación Full Microsoft | `LOG/OYG/IND/FIN/GOB/ELE/ORG; ROL-01..09; NT-01..15` |
| `PKG-RANSOM` | `RANSOM-HTML-03` | `Consola-de-incidente.html` | App HTML local · v2.0 | Bitácora local fuera de banda con derechos de decisión DD##, playbooks PB-01..07, custodia SHA-256 y borradores sin envío | `INC-*; EV-*; PB-01..07; DD10..18` |
| `PKG-CISO365` | `CISO365-XLSX-PLAN` | `AI_CISO_Atlas_CISO365_Plan_y_Ciclo_Anual_v1.0.xlsx` | Libro Excel · v1.0 (2026-11-10) | 7 fases y hitos (H0..H365), 130 actividades, 32 rubros de recepción, 54 rituales, 22 derechos de decisión, indicadores y OKR año 1 | `F0..F6; H0..H365; ACT-001..130; RC01..32; R01..54; DD01..22; A1-O1..O6` |
| `PKG-CISO365` | `CISO365-XLSX-EVAL` | `AI_CISO_Atlas_CISO365_Evaluacion_y_Entrevistas_v1.0.xlsx` | Libro Excel · v1.0 (2026-11-10) | 51 prácticas de evaluación con escala de evidencia 0–4, 56 preguntas de entrevista y 18 servicios de asesoría | `EV01..51; EN01..56; S01..18; KSG05` |
| `PKG-CISO365` | `CISO365-XLSX-TAB` | `AI_CISO_Atlas_CISO365_Tablero_Rendicion_de_Cuentas_v1.0.xlsx` | Libro Excel · v1.0 (2026-11-10) | 40 criterios de salida de hitos, 39 indicadores agrupados en 6 preguntas del directorio y seguimiento OKR año 1 | `Q1..Q6; H0-1..H365-6; A1-O1-KR1..A1-O6-KR3` |
| `PKG-CISO365` | `CISO365-MD-SERIE` | `AI_CISO_Atlas_CISO365_00_Indice_y_Guia_de_Uso_v1.0.md .. 08_Validacion_con_la_Formacion_v1.0.md` | Serie Markdown (9 docs) · v1.0 (2026-11-10) | Índice (00), Modelo Operativo (01), Playbook Primer Año (02), Ciclo Anual (03), Evaluación/Entrevistas (04), Informe Anual (05), Trazabilidad (06), Medición KPIs/OKR (07), Validación Formación (08) | `F0..F6; ACT-*; R*; EV*; KSG01..06` |
| `PKG-CISO365` | `CISO365-JSON` | `AI_CISO_Atlas_CISO365_Catalogo_v1.0.json` | Catálogo JSON · v1.0 (2026-11-10) | Modelo estructurado completo con fases, puertas, actividades, rituales, prácticas, medición y 713 relaciones | `ACT-*; R*; EV*; DD*; K*; KSG*` |
| `PKG-KPI-OKR` | `KPI-XLSX-V10` | `AI_CISO_Atlas_KPIs_OKRs_CISO_de_Frontera_v1.0_2026-11-09.xlsx` | Libro Excel (base) · v1.0 (2026-11-09) | 64 KPIs (8 territorios × 8), estadios E1–E5, motor sectorial, paquetes de Directorio/Esenciales y OKR por territorio y sector | `T01..T08; GV/ID/PR/DE/RS/RC; K01..K64` |
| `PKG-KPI-OKR` | `KPI-XLSX-V12` | `AI_CISO_Atlas_KPIs_OKRs_CISO_de_Frontera_v1.2_2026-11-10.xlsx` | Libro Excel (integrado CISO 365) · v1.2 / v1.1 (2026-11-10) | Integra K01..K64 con KSG01..KSG06 (70 indicadores), OKR_Anio1 (A1-O1..O6) y trazabilidad Plan365_Integracion | `K01..K64; KSG01..KSG06; A1-O1..O6; T01-O1..T08-O1; FIN/GOB/ELE/OYG/IND/LOG-O1..O3` |
| `PKG-KPI-OKR` | `KPI-MD-JSON` | `AI_CISO_Atlas_KPIs_OKRs_CISO_de_Frontera_Guia_v1.0.md / v1.2.md + AI_CISO_Atlas_KPIs_OKRs_Catalogo_v1.0.json / v1.2.json` | Guía MD + JSON · v1.0–v1.2 | Definición analítica de los 64+6 indicadores, fórmulas, polaridad, evidencia en plataforma Microsoft, umbrales E1–E5 y marco regulatorio | `K01..K64; KSG01..KSG06; E1..E5` |
| `PKG-NINJA` | `NINJA-PORTAL` | `Ninja_Training_Seguridad_Microsoft_2026/README.md + index.html + MANIFIESTO_VERSION.json` | Serie formativa (15 programas) · v2026-11-08 | Portada unificada de 15 programas, 387 módulos, ~2.000 h, 4.319 recursos, 2.165 ejercicios y 872 preguntas de evaluación | `NT-01..NT-15; [LAB]/[LAB-PARCIAL]/[SOLO-PRODUCCION]` |
| `PKG-NINJA` | `NINJA-ANEXOS` | `Anexo_Entorno_de_practica.md + Anexo_Laboratorio_Azure_Defender_for_Cloud_y_Foundry.md + Plan_Arquitectura_Segura_Agentes_IA_Azure.md` | Anexos transversales · v2026-11-08 | Diseño de laboratorio con crédito Visual Studio Enterprise + trial M365 E5, control de costos y protocolo de práctica segura en producción | `LAB-VS150; E5-TRIAL; Ficha de práctica en producción` |
| `PKG-NINJA` | `NT-01` | `01_Sentinel/Sentinel_Ninja_Training_2026 (.html · _Plan_y_catalogo.xlsx · README.md)` | Programa Ninja #01 · 2026-11-06 | Microsoft Sentinel: SIEM, KQL, conectores, analítica, hunting, UEBA, salud SOC, SOAR Logic Apps y SOC agéntico (41 mód., 237 h) | `NT-01: P0,I0..I5,M1..M13,A1..A9,X1..X7,C1..C5` |
| `PKG-NINJA` | `NT-02` | `02_Defender_XDR/Defender_XDR_Ninja_Training_2026 (.html · _Plan_y_catalogo.xlsx · README.md)` | Programa Ninja #02 · 2026-11-06 | Microsoft Defender XDR: MDO, MDE, MDI v3.x, Entra ID Protection, vulnerabilidades, AIR/Attack Disruption, IR y excelencia SOC (38 mód., 250 h) | `NT-02: P0,I0..I8,M1..M10,A1..A8,S1..S7,C1..C3` |
| `PKG-NINJA` | `NT-03` | `03_Entra_Identidad_y_Agentes/Entra_Identidad_Ninja_Training_2026 (.html · _Plan_y_catalogo.xlsx · README.md)` | Programa Ninja #03 · 2026-11-06 | Microsoft Entra: passkeys/FIDO2, Acceso Condicional, CAE, PIM, ID Governance, GSA, Workload ID, ITDR/IR de identidad y Entra Agent ID (31 mód., 225 h) | `NT-03: P0,I0..I6,M1..M8,A1..A5,X1..X7,C1..C3` |
| `PKG-NINJA` | `NT-04` | `04_Security_Copilot/Security_Copilot_Ninja_Training_2026 (.html · _Plan_y_catalogo.xlsx · README.md)` | Programa Ninja #04 · 2026-11-06 | Microsoft Security Copilot: SCU, triage, hunting, identidad, endpoints, Purview, promptbooks, Logic Apps y agentes SOC (30 mód., 146 h) | `NT-04: P0,I0..I6,M1..M7,A1..A7,X1..X5,C1..C3` |
| `PKG-NINJA` | `NT-05` | `05_Purview_Information_Protection/Purview_Information_Protection_Ninja_Training_2026 (.html · _Plan_y_catalogo.xlsx · README.md)` | Programa Ninja #05 · 2026-11-06 | Purview Information Protection: clasificadores, etiquetas de sensibilidad, cifrado RMS/revocación, DKE/Customer Key y contenedores (18 mód., 78 h) | `NT-05: P0,I0..I3,M1..M4,A1..A4,O1..O3,C1..C2` |
| `PKG-NINJA` | `NT-06` | `06_Purview_DLP/Purview_DLP_Ninja_Training_2026 (.html · _Plan_y_catalogo.xlsx · README.md)` | Programa Ninja #06 · 2026-11-06 | Purview Data Loss Prevention: Endpoint DLP, navegador, Exchange/SharePoint/Teams, Copilot/IA, Adaptive Protection e integración XDR/Sentinel (18 mód., 87 h) | `NT-06: P0,I0..I3,M1..M4,A1..A4,O1..O3,C1..C2` |
| `PKG-NINJA` | `NT-07` | `07_Purview_Insider_Risk/Purview_Insider_Risk_Ninja_Training_2026 (.html · _Plan_y_catalogo.xlsx · README.md)` | Programa Ninja #07 · 2026-11-06 | Purview Insider Risk Management: exfiltración interna, evidencia forense, Adaptive Protection y coordinación Legal/RR. HH. (18 mód., 75 h) | `NT-07: P0,I0..I3,M1..M4,A1..A4,O1..O3,C1..C2` |
| `PKG-NINJA` | `NT-08` | `08_Purview_Communication_Compliance/Purview_Communication_Compliance_Ninja_Training_2026 (.html · _Plan_y_catalogo.xlsx · README.md)` | Programa Ninja #08 · 2026-11-06 | Purview Communication Compliance e Information Barriers: supervisión de canales, barreras de información y evidencia regulatoria (18 mód., 57 h) | `NT-08: P0,I0..I3,M1..M4,A1..A4,O1..O3,C1..C2` |
| `PKG-NINJA` | `NT-09` | `09_Purview_Ciclo_de_vida_y_Registros/Purview_Lifecycle_Records_Ninja_Training_2026 (.html · _Plan_y_catalogo.xlsx · README.md)` | Programa Ninja #09 · 2026-11-06 | Purview Data Lifecycle y Records Management: retención, etiquetas de registro, inmutabilidad/preservation lock e integración con holds (18 mód., 61 h) | `NT-09: P0,I0..I3,M1..M4,A1..A4,O1..O3,C1..C2` |
| `PKG-NINJA` | `NT-10` | `10_Purview_eDiscovery_y_Audit/Purview_eDiscovery_Audit_Ninja_Training_2026 (.html · _Plan_y_catalogo.xlsx · README.md)` | Programa Ninja #10 · 2026-11-06 | Purview eDiscovery y Audit: Audit Standard/Premium, KeyQL, retenciones legales, custodios, cadena de custodia e IR con XDR/Sentinel (18 mód., 70 h) | `NT-10: P0,I0..I3,M1..M4,A1..A4,O1..O3,C1..C2` |
| `PKG-NINJA` | `NT-11` | `11_Purview_Compliance_Manager/Purview_Compliance_Manager_Ninja_Training_2026 (.html · _Plan_y_catalogo.xlsx · README.md)` | Programa Ninja #11 · 2026-11-06 | Purview Compliance Manager: plantillas NIST/ISO/regulatorias, pruebas, evidencias, mapeo cruzado y reportes al comité (18 mód., 63 h) | `NT-11: P0,I0..I3,M1..M4,A1..A4,O1..O3,C1..C2` |
| `PKG-NINJA` | `NT-12` | `12_Purview_DSPM_y_Seguridad_de_datos_para_IA/Purview_DSPM_IA_Ninja_Training_2026 (.html · _Plan_y_catalogo.xlsx · README.md)` | Programa Ninja #12 · 2026-11-06 | Purview DSPM y seguridad de datos para IA: sobreexposición en SharePoint (SAM), protección de prompts/agentes y Shadow AI (18 mód., 80 h) | `NT-12: P0,I0..I3,M1..M4,A1..A4,O1..O3,C1..C2` |
| `PKG-NINJA` | `NT-13` | `13_Seguridad_de_Copilot_y_Copilot_Studio/Seguridad_Copilot_Copilot_Studio_Ninja_Training_2026 (.html · _Plan_y_catalogo.xlsx · README.md)` | Programa Ninja #13 · 2026-11-06 | Seguridad de M365 Copilot, agentes y Copilot Studio: Copilot Control System, Managed Environments, DLP/auditoría/XDR/Sentinel y red teaming IA (34 mód., 184 h) | `NT-13: P0,I0..I7,M1..M8,A1..A8,O1..O6,C1..C3` |
| `PKG-NINJA` | `NT-14` | `14_Defender_for_Cloud/Defender_for_Cloud_Ninja_Training_2026 (.html · _Plan_y_catalogo.xlsx · README.md)` | Programa Ninja #14 · 2026-11-08 | Microsoft Defender for Cloud: CSPM, rutas de ataque, Servers Plan 2, Storage, Databases, Containers, Key Vault/ARM, AI-SPM e IR cloud (41 mód., 236 h) | `NT-14: P0,B0..B7,M1..M9,A1..A9,W1..W7,O1..O4,C1..C3` |
| `PKG-NINJA` | `NT-15` | `15_Seguridad_de_agentes_de_IA_en_Foundry/Seguridad_Agentes_IA_Foundry_Ninja_Training_2026 (.html · _Plan_y_catalogo.xlsx · README.md)` | Programa Ninja #15 · 2026-11-07 | Seguridad de agentes de IA en Microsoft Foundry: Agent Service, Entra Agent ID, Prompt Shields, red Zero Trust, AI Red Teaming e IR de agentes (28 mód., 151 h) | `NT-15: P0,F0..F5,M1..M7,A1..A7,O1..O4,C1..C3` |

## 2. Secuencia en los primeros 365 días de un CISO (`PKG-CISO365`)

Un programa anti-ransomware fracasa tanto si intenta desplegar 21 controles el día 1 como si posterga respaldos e identidad privilegiada hasta terminar un diagnóstico teórico. Así se inserta en las 7 fases del primer año:

| Fase y ventana | Hito de salida | Qué debe lograr el CISO en resiliencia ante ransomware | Controles `CT-*` activados/revisados | Trampa habitual |
|---|---|---|---|---|
| `F0` (Antes del día 1 (D-30 a D0)) | `H0` · Mandato acordado (día 0) | Llegar con un mandato explícito, una hipótesis de trabajo y la agenda de escucha preparada; no con un plan cerrado. | `Seguimiento transversal` | Llegar con la solución decidida o aceptar el cargo sin acordar alcance, línea de reporte y acceso al directorio. |
| `F1` (Días 1–30) | `H30` · Acta de recepción (día 30) | Saber qué se recibe (personas, presupuesto, compromisos, riesgos abiertos), estabilizar lo urgente y escuchar a quienes deciden, sin anunciar cambios estructurales. | `CT-01;CT-02;CT-03;CT-04;CT-08;CT-13;CT-18` | Confundir la escucha con pasividad, o actuar sobre lo urgente sin registrar lo recibido y sin separar herencia de gestión propia. |
| `F2` (Días 31–60) | `H60` · Diagnóstico base (día 60) | Construir una línea base objetiva y defendible: madurez, escenarios de riesgo, servicios y activos críticos, obligaciones, capacidades y terceros. | `CT-01;CT-05;CT-06;CT-07;CT-09;CT-10;CT-11;CT-12;CT-14;CT-15;CT-16;CT-17;CT-19;CT-20;CT-21` | El diagnóstico eterno: medir todo, con todos los marcos, sin decidir nada; o un diagnóstico que es solo una opinión. |
| `F3` (Días 61–100) | `H100` · Informe de los 100 días (día 100) | Convertir el diagnóstico en pocas prioridades con dueño, mostrar resultados tempranos y pedir explícitamente los apoyos necesarios. | `CT-02;CT-04;CT-13;CT-16;CT-20` | Prometer sin pedir: un plan ambicioso sin recursos, sin dueños y sin decisiones explícitas de la dirección. |
| `F4` (Días 101–180) | `H180` · Sistema de gobierno operando (día 180) | Formalizar decisiones (apetito, políticas, comité, dueños de riesgo, métricas, presupuesto) para que el programa funcione sin depender del CISO en cada decisión. | `CT-03;CT-04;CT-05;CT-06;CT-07;CT-08;CT-09;CT-10;CT-11;CT-12;CT-13;CT-14;CT-17;CT-18;CT-19;CT-21` | Gobierno decorativo: comités informativos, apetito sin umbrales y métricas sin meta ni uso. |
| `F5` (Días 181–270) | `H270` · Capacidades probadas (día 270) | Ejecutar la hoja de ruta y someter a prueba lo que se afirma: crisis, recuperación, controles, terceros e IA. | `CT-01;CT-02;CT-03;CT-09;CT-15;CT-16;CT-17;CT-18;CT-20;CT-21` | Confundir actividad con efectividad: controles configurados que nunca se probaron y planes que nadie ensayó. |
| `F6` (Días 271–365) | `H365` · Rendición de cuentas anual (día 365) | Rendir cuentas con evidencia, recalibrar riesgo y madurez, y convertir lo aprendido en el plan y los compromisos del año 2. | `CT-06;CT-07;CT-08;CT-15;CT-17;CT-21` | Un informe de logros sin pendientes ni aprendizajes, o un año 2 que repite el plan del año 1 sin recalibrar. |

## 3. Contextualización según las prioridades y sector de la organización (`PKG-KPI-OKR`)

El peso relativo de disponibilidad física, confidencialidad/exfiltración, riesgo de cadena de suministro y presión regulatoria cambia por industria. Usar esta guía junto con `Perfiles_Sector`, `Paquetes_Sector` y `OKR_Sectores` del catálogo de KPIs/OKRs:

### `LOG` · Logística

- **Contexto de negocio y escenarios críticos:** Flujo físico detenido por caída de WMS/TMS/aduanas o contagio vía socios EDI/API: priorizar desconexión/reingreso seguro de integraciones (K31/K62), operación manual numerada (K29), restauración dentro de RTO (K30/K47) y operación sin agentes de optimización (K56).
- **Controles `CT-*` de máxima prioridad:** `CT-01, CT-02, CT-04, CT-13, CT-15, CT-16, CT-18, CT-19, CT-21`
- **Capas Full Microsoft prioritarias:** `MS-CAP-01, MS-CAP-07, MS-CAP-08, MS-CAP-12`
- **10 KPIs de Directorio (`Paquetes_Sector`):** `K24, K25, K31, K27, K56, K15, K28, K30, K45, K61`
- **10 KPIs Esenciales de gestión (`Paquetes_Sector`):** `K34, K21, K37, K47, K62, K29, K49, K33, K39, K05`
- **OKR sectoriales de referencia:** **Gobernar**: Gobernar el riesgo de la red de socios como riesgo propio. (`K31`→80, `K27`→15, `K23`→90); **Gestionar**: Mantener el flujo operativo ante ransomware o caída de sistemas. (`K29`→75, `K47`→100, `K62`→80); **Evolucionar**: Escalar la optimización con IA y agentes sin perder el control. (`K49`→75, `K50`→75, `K56`→75)
- **Trampa de medición a evitar:** Medir solo la seguridad propia cuando el riesgo está en la red de socios.

### `OYG` · Oil & Gas

- **Contexto de negocio y escenarios críticos:** Procesos físicos continuos de alta consecuencia y sitios remotos con contratistas: priorizar segmentación TI/OT (K36/K40), control de accesos remotos y vulnerabilidades explotadas (K34/K46), operación degradada (K29) y ejercicios ejecutivos (K15).
- **Controles `CT-*` de máxima prioridad:** `CT-01, CT-02, CT-04, CT-06, CT-07, CT-11, CT-13, CT-15, CT-17, CT-18`
- **Capas Full Microsoft prioritarias:** `MS-CAP-02, MS-CAP-03, MS-CAP-06, MS-CAP-07, MS-CAP-12`
- **10 KPIs de Directorio (`Paquetes_Sector`):** `K24, K25, K15, K31, K30, K40, K29, K27, K28, K45`
- **10 KPIs Esenciales de gestión (`Paquetes_Sector`):** `K34, K39, K33, K61, K32, K36, K47, K21, K26, K05`
- **OKR sectoriales de referencia:** **Gobernar**: Integrar el ciberriesgo OT en el apetito y en la gestión de seguridad de procesos. (`K26`→75, `K31`→80, `K09`→80); **Gestionar**: Cerrar las rutas de ataque hacia OT. (`K36`→80, `K34`→75, `K46`→85); **Evolucionar**: Operar sitios remotos con monitoreo y respuesta asistidos por IA. (`K45`→4, `K15`→75, `K53`→70)
- **Trampa de medición a evitar:** Trasladar métricas de TI (parches al 100%) a OT, donde mandan la disponibilidad y la seguridad física.

### `IND` · Industrial

- **Contexto de negocio y escenarios críticos:** Parada de planta (OEE) y robo de propiedad intelectual (diseños, fórmulas): integrar inventario TI/OT (K39/K40), respaldos inmutables de ingeniería/MES/ERP (K28), protección MIP/DLP (K37/K52) y control de integradores (K31).
- **Controles `CT-*` de máxima prioridad:** `CT-01, CT-02, CT-04, CT-05, CT-07, CT-10, CT-15, CT-18, CT-19, CT-21`
- **Capas Full Microsoft prioritarias:** `MS-CAP-03, MS-CAP-06, MS-CAP-10, MS-CAP-12`
- **10 KPIs de Directorio (`Paquetes_Sector`):** `K24, K25, K37, K15, K28, K31, K45, K29, K56, K61`
- **10 KPIs Esenciales de gestión (`Paquetes_Sector`):** `K34, K39, K30, K33, K40, K47, K27, K32, K36, K52`
- **OKR sectoriales de referencia:** **Gobernar**: Proteger la propiedad intelectual y la disponibilidad de planta como decisiones de negocio. (`K37`→75, `K22`→70, `K31`→80); **Gestionar**: Reducir el radio de explosión entre TI, OT y proveedores. (`K40`→70, `K39`→90, `K28`→85); **Evolucionar**: Llevar la seguridad desde el diseño a productos conectados y a la IA de ingeniería. (`K38`→75, `K51`→80, `K20`→5)
- **Trampa de medición a evitar:** Separar TI y OT en tableros distintos sin una visión integrada del riesgo.

### `FIN` · Financiero

- **Contexto de negocio y escenarios críticos:** Pagos, canales digitales 24×7 y confianza sistémica: la doble extorsión (datos regulados + indisponibilidad) y la caída de un proveedor cloud/core exigen MTTC en horas, notificaciones precisas al supervisor (K61) y gobierno estricto de agentes en atención/crédito (K50–K52).
- **Controles `CT-*` de máxima prioridad:** `CT-01, CT-02, CT-04, CT-10, CT-13, CT-14, CT-16, CT-18, CT-19, CT-20, CT-21`
- **Capas Full Microsoft prioritarias:** `MS-CAP-01, MS-CAP-07, MS-CAP-10, MS-CAP-11, MS-CAP-12`
- **10 KPIs de Directorio (`Paquetes_Sector`):** `K24, K25, K37, K61, K64, K51, K27, K28, K30, K45`
- **10 KPIs Esenciales de gestión (`Paquetes_Sector`):** `K52, K50, K33, K49, K57, K59, K15, K56, K26, K34`
- **OKR sectoriales de referencia:** **Gobernar**: Gobernar el ciberriesgo como riesgo operacional dentro del apetito aprobado. (`K25`→5, `K61`→95, `K59`→85); **Gestionar**: Reducir la exposición a fuga de datos, ransomware y terceros críticos. (`K37`→75, `K30`→80, `K27`→15); **Evolucionar**: Escalar la IA y los agentes con autoridad acotada y sin fuga de datos. (`K50`→75, `K51`→80, `K52`→75)
- **Trampa de medición a evitar:** Responder la lista de verificación del supervisor y confundirla con resiliencia probada.

### `GOB` · Gobierno

- **Contexto de negocio y escenarios críticos:** Servicios esenciales a ciudadanos cautivos y bases sensibles (identidad, salud, tributos) sobre infraestructura heterogénea: priorizar MFA resistente al phishing (K33), línea base (K35), respaldos probados fuera del dominio (K28/K30) y evidencia auditable ante contralorías (K57/K61).
- **Controles `CT-*` de máxima prioridad:** `CT-01, CT-02, CT-03, CT-04, CT-05, CT-10, CT-14, CT-16, CT-19, CT-21`
- **Capas Full Microsoft prioritarias:** `MS-CAP-01, MS-CAP-03, MS-CAP-10, MS-CAP-11, MS-CAP-12`
- **10 KPIs de Directorio (`Paquetes_Sector`):** `K24, K25, K37, K61, K64, K57, K30, K33, K28, K45`
- **10 KPIs Esenciales de gestión (`Paquetes_Sector`):** `K52, K26, K51, K42, K35, K50, K38, K08, K15, K47`
- **OKR sectoriales de referencia:** **Gobernar**: Demostrar cumplimiento con evidencia y rendición de cuentas ante los órganos de control. (`K57`→85, `K61`→95, `K64`→75); **Gestionar**: Asegurar la continuidad de los servicios críticos al ciudadano. (`K30`→80, `K33`→80, `K35`→85); **Evolucionar**: Proteger los datos de los ciudadanos en la adopción de IA. (`K51`→80, `K49`→75, `K52`→75)
- **Trampa de medición a evitar:** Medir el cumplimiento formal de la norma sin probar la recuperación.

### `ELE` · Generación eléctrica

- **Contexto de negocio y escenarios críticos:** Disponibilidad de MW y seguridad física en DCS/SCADA: impedir que un compromiso de TI o acceso remoto de OEM cruce a OT (K36/K40), eliminar privilegios permanentes (K34) y ensayar operación degradada/manual y sin IA (K29/K56) antes de reconectar.
- **Controles `CT-*` de máxima prioridad:** `CT-01, CT-02, CT-03, CT-04, CT-07, CT-12, CT-13, CT-15, CT-17, CT-18, CT-21`
- **Capas Full Microsoft prioritarias:** `MS-CAP-02, MS-CAP-04, MS-CAP-06, MS-CAP-07, MS-CAP-12`
- **10 KPIs de Directorio (`Paquetes_Sector`):** `K24, K25, K15, K30, K29, K61, K27, K28, K45, K40`
- **10 KPIs Esenciales de gestión (`Paquetes_Sector`):** `K34, K39, K47, K31, K05, K59, K21, K32, K26, K56`
- **OKR sectoriales de referencia:** **Gobernar**: Gobernar el riesgo OT con el mismo rigor que la seguridad de los procesos. (`K40`→70, `K59`→85, `K14`→75); **Gestionar**: Mantener la disponibilidad frente a un adversario capaz. (`K29`→75, `K34`→75, `K30`→80); **Evolucionar**: Incorporar IA a la operación sin crear nuevas dependencias críticas. (`K56`→75, `K43`→70, `K12`→85)
- **Trampa de medición a evitar:** Informar cumplimiento de la norma técnica como si fuera resiliencia frente a un adversario capaz.

### `ORG` · Mi organización

- **Contexto de negocio y escenarios críticos:** Perfil base personalizable: completar BIA (CT-01), proteger copias e identidad fuera del plano productivo (CT-02/03/04), asegurar detección/contención verificada (CT-11..13) y exigir pruebas anuales reales (E1/E2/E3) antes de declarar madurez.
- **Controles `CT-*` de máxima prioridad:** `CT-01, CT-02, CT-03, CT-04, CT-05, CT-11, CT-13, CT-15, CT-16, CT-17, CT-21`
- **Capas Full Microsoft prioritarias:** `MS-CAP-01, MS-CAP-03, MS-CAP-07, MS-CAP-10, MS-CAP-12`
- **10 KPIs de Directorio (`Paquetes_Sector`):** `K24, K25, K37, K61, K28, K30, K31, K33, K45, K26`
- **10 KPIs Esenciales de gestión (`Paquetes_Sector`):** `K34, K39, K49, K50, K57, K15, K27, K52, K64, K08`
- **OKR sectoriales de referencia:** Configurable según `OKR_Sectores` del catálogo.
- **Trampa de medición a evitar:** Qué métricas actuales no ayudan a decidir.


## 4. Trazabilidad hacia las 6 preguntas del Directorio (`Tablero_Rendicion_de_Cuentas`)

| Código | Pregunta del Directorio | Indicadores del tablero Año 1 (`PKG-KPI-OKR` / `PKG-CISO365`) |
|---|---|---|
| `Q1` | ¿Cuál es nuestro nivel real de riesgo? | `K25, K26, K46, K33, K39` |
| `Q2` | ¿Estamos mejorando? | `K22, K18, K60, K42, K45` |
| `Q3` | ¿Estamos invirtiendo correctamente? | `K17, K19, K20, K12` |
| `Q4` | ¿Estamos preparados para una interrupción significativa? | `K30, K28, K15, K32, K31, K21` |
| `Q5` | ¿Gobernamos el riesgo con evidencia? | `K09, K14, K58, K04, K63, K57, K59, K03, K49, K50, K51` |
| `Q6` | ¿Cumplimos lo que prometimos? (sistema de gestión y práctica del CISO) | `KSG01, KSG02, KSG03, KSG04, KSG05, KSG06, K02, K01` |

Para explorar interactivamente qué hacer por sector, fase y rol, abrir `Mapa-de-correlacion-y-prioridades.html` o filtrar `03-Correlacion-Prioridades-FullMS-Ninja.xlsx`.

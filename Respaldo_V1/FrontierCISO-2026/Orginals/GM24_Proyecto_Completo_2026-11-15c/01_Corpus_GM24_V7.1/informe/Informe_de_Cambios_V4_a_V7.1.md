# Informe de cambios GM-24: de la V4 a la V7.1

> **GM-24 V7.1 · The Next CISO + Sub-plan PO-GAC** · 2026-11-14. Catálogo: 379 conceptos (245 K · 52 AMP · 40 HC · 42 PA), todos con pre-ensayo íntegro y mapeados a 17 marcos (NIST/ISACA/MITRE/OWASP/CIS/CSA). V7.1 = ChangeSet editorial CS-GM24-V7.1-001 (4 títulos generalizados; sin cambio de IDs, cantidad ni mapeo). Plano A (corpus académico). Referencias DD/K4x/R/eo:OP/COE: marco interno.

> **Nota de reconstrucción (15-nov-2026).** Paquete regenerado desde las fuentes recuperadas del historial de la sesión tras la pérdida del entorno del 14-nov, completado con los lotes 01–08 (240 K), el archivo HC-040 y el Documento Maestro re-adjuntados por el autor. **Los 379 conceptos tienen su pre-ensayo íntegro y los tres documentos GM-24 incluyen el texto V4 original completo (DOCX V4 embebidos en `build/fuentes_GM24/V4_docx/`).**

## 1. Línea de tiempo
| Versión | Base | Qué cambió | Fuente |
|---|---|---|---|
| **V4** | 240 K; 51 AMP como títulos; 32 unidades → 12 ejes / 24 unidades; 800 h | Estructura académica, Versión Actualizada, 24 Clases; Documento Maestro; lotes 01–08; HC-040 | `Formación CISO_… 4.docx` (×3), Matrices_Curriculares, Documento Maestro |
| **V5** | 240 K | Eje PO-GAC: 67 PA (316 h), 41 competencias, 31 tareas MDO, 15 agentes, 24 AGC, 20 KPIs | Sub-plan V5 |
| **V6** | 331 (240 K + 51 AMP + 40 HC) | 23 PA retirados (cubiertos por AMP/HC), 2 fusionados → 42 PA con pre-ensayo; lente sobre 91; tres rutas; documentos GM-24 V6 | Sub-plan V6 |
| **V6-R** | 373 | Anexos de agentes; pre-ensayos como archivos de inicialización; mapeo a 17 marcos; 11 inconsistencias; 10 candidatos | Paquete V6-R |
| **V7** | **379** (245 K + 52 AMP + 40 HC + 42 PA) | 10 candidatos incorporados; 57 pre-ensayos nuevos; matriz rehecha; documentos GM-24 V7 | Paquete V7 |
| **V7.1** | 379 | ChangeSet editorial: 4 títulos generalizados tras las instancias de dominio; sin cambio de IDs, cantidad ni mapeo; 7 instancias de dominio (plano B) | Este paquete |

## 2. Incorporado
- Conceptos nuevos V7: G2.1-K11, M3.1-K11, M4.1-K11, M4.2-K11, AMP-52, M3.1-K12. PA promovidos: M3.1-PA02, M4.2-PA01, M4.1-PA01, M4.1-PA03. AAISM por unidad. Referencias por ID (12). Pre-ensayos de las 52 AMP.
- Sub-plan PO-GAC completo y siete instancias de dominio en el plano B (Productividad v1.1, XDR, Endpoints, Identidades, Datos, SIEM, Nube, Apps v1.0).

## 3. Modificado
| Elemento | V4 | V7.1 |
|---|---|---|
| Base | 240 K | 379 con pre-ensayo íntegro |
| Mapeo | por unidad (CISM/CRISC/CSF/RMF) | por concepto, 17 marcos, 3 niveles, método trazable |
| AMP | títulos | idea central desarrollada |
| 4 PA promovidos | títulos específicos de correo (V7) | títulos de dominio (V7.1) |
| Documentos GM-24 | 3 (V4) + Documento Maestro | 3 + Anexo PO-GAC (V7.1, V4 íntegro + ◆ V5/V6/V7/V7.1) + Documento Maestro original |

## 4. Eliminado o retirado
- Ningún K, AMP ni HC del GM-24 original fue eliminado. 23 PA de V5 retirados en V6 con trazabilidad (`docs/10_Conciliacion_V5_a_V6.md`).

## 5. ChangeSet V7.1
| ID | Antes (V7) | Después (V7.1) |
|---|---|---|
| M3.1-PA02 | Arquitectura de protección de correo y colaboración | Arquitectura de protección del dominio Zero Trust (instancias: correo y colaboración · detección y respuesta unificada · endpoints · identidades · datos) |
| M4.2-PA01 | Amenazas al correo y la colaboración | Amenazas del dominio Zero Trust (instancias: correo y colaboración · cross-domain · endpoints · identidades · datos) |
| M4.1-PA01 | Modelo operativo de Defender for Office 365 en Defender XDR | Modelo operativo del producto-control por cadencias (instancias: Defender for Office 365 · Defender XDR · Defender for Endpoint · Defender for Identity/Entra · Purview · Sentinel · Defender for Cloud) |
| M4.1-PA03 | Gestión de falsos positivos/negativos y listas | Gestión de la calidad de detección del dominio: FP/FN, tuning, listas, indicadores y supresiones (instancias: MDO · XDR · MDE · MDI/ID Protection · Purview DLP · Sentinel) |

## 6. Cobertura de marcos (V7.1 = V7)
| Marco | Elementos | Con fuerte | Solo parcial/informativa | Sin cobertura |
|---|---|---|---|---|
| NIST CSF 2.0 | 22 | 22 | 0 | 0 |
| NIST RMF | 7 | 7 | 0 | 0 |
| NIST SP 800-53 | 20 | 20 | 0 | 0 |
| NIST AI RMF | 19 | 19 | 0 | 0 |
| NIST AI 600-1 | 12 | 10 | 0 | 2 |
| ISACA CISM 2026 | 8 | 8 | 0 | 0 |
| ISACA CRISC 2025 | 9 | 9 | 0 | 0 |
| ISACA AAISM | 13 | 13 | 0 | 0 |
| MITRE ATT&CK | 14 | 14 | 0 | 0 |
| MITRE ATLAS | 14 | 14 | 0 | 0 |
| MITRE D3FEND | 7 | 7 | 0 | 0 |
| OWASP LLM Top 10 2025 | 10 | 10 | 0 | 0 |
| OWASP Agentic Top 10 2026 | 10 | 10 | 0 | 0 |
| OWASP SAMM | 5 | 5 | 0 | 0 |
| CIS Controls v8.1 | 18 | 18 | 0 | 0 |
| CSA CCM v4 | 17 | 17 | 0 | 0 |
| CSA AICM | 4 | 4 | 0 | 0 |

# 02 · Marco de competencias PO-GAC (41 competencias en 8 dominios)

> **GM-24 V7.1 · The Next CISO + Sub-plan PO-GAC** · 2026-11-14. Catálogo: 379 conceptos (245 K · 52 AMP · 40 HC · 42 PA), todos con pre-ensayo íntegro y mapeados a 17 marcos (NIST/ISACA/MITRE/OWASP/CIS/CSA). V7.1 = ChangeSet editorial CS-GM24-V7.1-001 (4 títulos generalizados; sin cambio de IDs, cantidad ni mapeo). Plano A (corpus académico). Referencias DD/K4x/R/eo:OP/COE: marco interno.

## Dominios
| ID | Dominio |
|---|---|
| D1 | Gobierno del producto-control |
| D2 | Operación del control (Defender for Office 365 / XDR) |
| D3 | Modelo operativo y excelencia operacional |
| D4 | Ingeniería y arquitectura de agentes |
| D5 | Gobierno, riesgo y cumplimiento de IA/agentes |
| D6 | Gestión de la fuerza de trabajo híbrida |
| D7 | Proveedores, plataformas y competencias |
| D8 | Liderazgo, decisión y comunicación |

## Competencias (N1 reconoce · N2 aplica con apoyo · N3 decide y defiende · N4 diseña y gobierna)
| ID | Dominio | Competencia | Niveles | Conceptos que la sostienen |
|---|---|---|---|---|
| C1.1 | D1 | Definir y mantener la ficha del producto-control (objetivo, alcance, métricas, backlog) | N1 describe · N2 redacta con apoyo · N3 define y defiende · N4 diseña portafolio | G1.1-PA01, M3.2-PA01, M1.1-PA02 |
| C1.2 | D1 | Usar CSF 2.0 × Zero Trust como grilla de ownership | N1 reconoce · N2 completa celdas · N3 asigna owners y arbitra · N4 gobierna portafolio | G2.1-PA01, HC-015, AMP-07 |
| C1.3 | D1 | Priorizar el backlog del control por riesgo y valor | N1 lista · N2 prioriza con criterio · N3 negocia · N4 optimiza portafolio | M1.1-PA02, HC-036, AMP-04 |
| C1.4 | D1 | Definir KPIs del control que no engañen | N1 recopila · N2 define · N3 valida con datos · N4 diseña sistema de medición | HC-027, M3.2-PA01 |
| C1.5 | D1 | Gestionar baseline, excepciones y overrides con vencimiento | N1 registra · N2 evalúa · N3 aprueba y audita · N4 diseña política | G2.2-PA03, AMP-09, AMP-10, HC-028 |
| C2.1 | D2 | Explicar la arquitectura de protección de correo y colaboración | N1 nombra capas · N2 diagnostica entrega · N3 diseña excepciones · N4 arquitectura | M3.1-PA02 |
| C2.2 | D2 | Triar, investigar y responder incidentes de correo en Defender XDR | N1 asistido · N2 autónomo · N3 lidera · N4 diseña playbooks | M4.1-PA02, M5.2-PA01, M4.2-PA01, M4.1-PA04 |
| C2.3 | D2 | Gestionar FP/FN, envíos y listas | N1 ejecuta · N2 analiza causa · N3 ajusta política · N4 diseña calidad | M4.1-PA03 |
| C2.4 | D2 | Verificar configuración frente a baseline y detectar deriva | N1 ejecuta analizador · N2 interpreta · N3 corrige/excepciona · N4 control continuo | G3.2-PA01, M3.2-PA01, G2.2-PA03 |
| C2.5 | D2 | Operar simulaciones y concientización | N1 ejecuta · N2 diseña campaña · N3 mide · N4 integra con SOC | M4.2-PA01 |
| C2.6 | D2 | Gestionar permisos de humanos y agentes en el control | N1 lee roles · N2 asigna mínimo · N3 audita · N4 diseña RBAC | M2.2-PA01, AMP-34, AMP-36 |
| C3.1 | D3 | Ejecutar y mantener el modelo operativo por cadencias | N1 ejecuta runbook · N2 mantiene evidencia · N3 mejora · N4 diseña modelo | M4.1-PA01, M1.1-PA03 |
| C3.2 | D3 | Ejecutar playbooks híbridos | N1 sigue · N2 adapta · N3 redacta · N4 gobierna | M5.1-PA01, M4.1-PA02 |
| C3.3 | D3 | Medir excelencia operacional | N1 reporta · N2 analiza · N3 decide · N4 diseña | G6.2-K06, M1.1-PA03 |
| C3.4 | D3 | Curar consultas de hunting y detecciones como código | N1 ejecuta · N2 documenta · N3 versiona · N4 gobierna repositorio | M4.1-PA04 |
| C3.5 | D3 | Decidir niveles de autonomía por tarea | N1 aplica escala · N2 justifica · N3 aprueba L2 · N4 define apetito | AMP-17, AMP-18, AMP-40, HC-010, HC-019 |
| C4.1 | D4 | Elegir el patrón de agente y la ruta de construcción | N1 reconoce · N2 compara · N3 decide · N4 arquitectura | AMP-35, M6.2-PA01, M6.2-PA03 |
| C4.2 | D4 | Diseñar la ficha del agente y sus traspasos | N1 completa · N2 diseña · N3 revisa · N4 estándar | G2.2-PA02, AMP-28, M3.1-PA01 |
| C4.3 | D4 | Construir agentes en Copilot Studio/Foundry con ALM | N1 configura · N2 construye · N3 pipeline · N4 plataforma | M6.2-PA01, M6.2-PA02 |
| C4.4 | D4 | Gestionar postura de recursos de IA en nube | N1 lee · N2 corrige · N3 gobierna · N4 integra | AMP-51, M6.2-PA01 |
| C4.5 | D4 | Evaluar calidad y resistencia adversarial | N1 ejecuta · N2 diseña dataset · N3 criterios · N4 programa | M3.2-PA03, AMP-37, AMP-38, M4.1-K08 |
| C4.6 | D4 | Modelar amenazas a agentes y aplicar guardrails | N1 reconoce · N2 modela · N3 mitiga · N4 diseña defensa | M4.2-PA02, HC-032, AMP-41, AMP-42, AMP-36, HC-028 |
| C5.1 | D5 | Aplicar marcos de gobierno de IA y el catálogo AGC | N1 conoce · N2 mapea · N3 evalúa · N4 diseña | G2.1-PA02, G2.2-PA01, M3.2-PA02, AMP-06, AMP-08, HC-005, M4.2-PA02, G6.2-PA01 |
| C5.2 | D5 | Gobernar identidades no humanas | N1 inventaría · N2 asigna dueño · N3 recertifica · N4 política | AMP-33, AMP-34, HC-009, M2.2-PA01 |
| C5.3 | D5 | Mantener el registro de agentes | N1 registra · N2 reconcilia · N3 detecta shadow · N4 diseña | M2.1-PA01, M6.2-K06 |
| C5.4 | D5 | Gobernar datos de agentes y soberanía | N1 clasifica · N2 restringe · N3 audita · N4 política | AMP-31, AMP-32, HC-011, AMP-11, G3.1-PA01 |
| C5.5 | D5 | Operar el ATO y las tres líneas | N1 prepara · N2 defiende · N3 autoriza (2ª línea) · N4 diseña | AMP-22, G4.1-PA01, G4.2-K10, HC-028, M3.2-PA02 |
| C5.6 | D5 | Gestionar evidencia y trazabilidad | N1 registra · N2 verifica · N3 audita · N4 esquema | AMP-46, AMP-13, AMP-45, G3.2-K06, AMP-19, HC-005 |
| C6.1 | D6 | Diseñar la estructura híbrida y el RACI | N1 describe · N2 asigna · N3 diseña · N4 gobierna | M1.1-PA01, AMP-27, AMP-28, G1.1-PA01 |
| C6.2 | D6 | Supervisar y revisar el desempeño de agentes | N1 muestrea · N2 revisa · N3 decide · N4 diseña | M4.1-PA06, AMP-26, AMP-39, G4.2-PA01, G6.2-PA01 |
| C6.3 | D6 | Operar la observabilidad de la flota | N1 lee tablero · N2 construye · N3 alerta · N4 arquitectura | M4.1-PA05, HC-018, G5.1-K05, M6.2-PA03 |
| C6.4 | D6 | Gestionar FinOps de agentes | N1 lee costos · N2 modela · N3 optimiza · N4 presupuesta | M1.2-PA01, G1.2-PA01, M1.2-K01 |
| C6.5 | D6 | Gestionar incidentes de agentes y operación degradada | N1 ejecuta · N2 contiene · N3 lidera · N4 diseña | AMP-43, AMP-44, AMP-45, AMP-47, AMP-48, M6.1-PA01, HC-023, HC-020, M6.1-K10 |
| C6.6 | D6 | Mejorar agentes con cambios gobernados | N1 propone · N2 ChangeSet · N3 aprueba · N4 pipeline | M5.2-PA02, M6.2-PA02, HC-035, M5.2-K05 |
| C7.1 | D7 | Desarrollar competencias propias y del equipo | N1 autoevalúa · N2 plan · N3 mentorea · N4 programa | M1.2-PA03, AMP-29, AMP-30, HC-037 |
| C7.2 | D7 | Gestionar proveedores y plataformas de IA | N1 lee contratos · N2 requisitos · N3 negocia · N4 estrategia | M1.2-PA02, AMP-12, M6.2-K07, M6.2-K08, AMP-49, AMP-50, M6.2-PA01, G1.1-PA01 |
| C7.3 | D7 | Gestionar la relación con el MDR y la mesa de mensajería | N1 coordina · N2 define interfaces · N3 gobierna · N4 diseña | M1.1-PA01 |
| C8.1 | D8 | Gestionar el riesgo de la flota | N1 registra · N2 evalúa · N3 trata · N4 apetito | G4.1-PA02, G4.2-PA01, AMP-15, AMP-17, AMP-20, G4.2-K09, G5.1-K05 |
| C8.2 | D8 | Construir casos de negocio y hojas de ruta | N1 recopila · N2 modela · N3 defiende · N4 estrategia | G1.2-PA01, AMP-04, AMP-30, M1.2-PA01 |
| C8.3 | D8 | Comunicar a la dirección con hechos | N1 prepara datos · N2 redacta · N3 presenta · N4 narrativa | G6.1-PA01, AMP-23, AMP-24, HC-027, HC-020, G6.1-K05 |
| C8.4 | D8 | Ejercer accountability y ética sobre agentes | N1 conoce · N2 aplica · N3 decide · N4 cultura | AMP-03, AMP-02, AMP-25, AMP-26, AMP-12 |

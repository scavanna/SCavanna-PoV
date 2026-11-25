# 04 · Modelo operativo del control de correo y colaboración (Defender for Office 365 en Defender XDR)

> **GM-24 V7.1 · The Next CISO + Sub-plan PO-GAC** · 2026-11-14. Catálogo: 379 conceptos (245 K · 52 AMP · 40 HC · 42 PA), todos con pre-ensayo íntegro y mapeados a 17 marcos (NIST/ISACA/MITRE/OWASP/CIS/CSA). V7.1 = ChangeSet editorial CS-GM24-V7.1-001 (4 títulos generalizados; sin cambio de IDs, cantidad ni mapeo). Plano A (corpus académico). Referencias DD/K4x/R/eo:OP/COE: marco interno.

31 tareas con cadencia, persona (según Microsoft Learn), función CSF, práctica agnóstica eo:OP, nivel de autonomía recomendado, agente y KPI.

| ID | Tarea | Cadencia | Persona | CSF 2.0 | SAF | eo:OP | Autonomía | Agente | KPI | Fuente |
|---|---|---|---|---|---|---|---|---|---|---|
| MDO-D01 | Triar incidentes de la cola (Medium/High de Defender for Office 365) | Diaria | Security Operations Team | DE.AE, RS.MA | SOP | eo:OP-SOP-10 Triar incidentes por prioridad dentro del SLA | L2 | AG-01 | KPI-01 | Learn: mdo-sec-ops-guide |
| MDO-D02 | Investigar y ejecutar acciones de respuesta sobre incidentes | Diaria | Security Operations Team | RS.AN, RS.MI | SOP | eo:OP-SOP-11 Investigar y remediar incidentes con evidencia | L2 | AG-02 | KPI-02 | Learn: mdo-sec-ops-guide |
| MDO-D03 | Resolver incidentes remediados | Diaria | Security Operations Team | RS.MA | SOP | eo:OP-SOP-12 Cerrar incidentes con criterio documentado | L2 | AG-01 | KPI-01 | Learn |
| MDO-D04 | Clasificar incidentes (true/false; tipo de amenaza) | Diaria | Security Operations Team | ID.IM | SOP | eo:OP-SOP-13 Clasificar incidentes para aprender patrones | L2 | AG-01 | KPI-03 | Learn |
| MDO-D05 | Enviar FP/FN a Microsoft (Submissions) | Diaria | Security Operations Team | ID.IM | SOP | eo:OP-SOP-14 Retroalimentar al fabricante con FP/FN | L2 | AG-03 | KPI-04 | Learn |
| MDO-D06 | Analizar detalles de los envíos | Diaria | Security Operations Team | ID.IM | SOP | eo:OP-SOP-15 Analizar causa raíz de errores de detección | L1 | AG-03 | KPI-04 | Learn |
| MDO-D07 | Agregar bloqueos en Tenant Allow/Block List | Diaria | Security Operations Team | PR.PS | SOP | eo:OP-SOP-16 Mantener listas de bloqueo con vencimiento | L2 | AG-03 | KPI-05 | Learn |
| MDO-D08 | Liberar falsos positivos de cuarentena | Diaria | Security Operations Team | RS.MI | SOP | eo:OP-SOP-17 Liberar cuarentena con segunda aprobación | L2 | AG-03 | KPI-04 | Learn |
| MDO-D09 | Revisar campañas con correo entregado y remover mensajes | Diaria | Security Operations Team | RS.MI, DE.AE | SOP | eo:OP-SOP-18 Remediar mensajes residentes | L2 | AG-04 | KPI-02 | Learn |
| MDO-W01 | Revisar informes de tendencias de detección | Semanal | Security Operations Team | DE.CM | POS | eo:OP-SOP-19 Revisar tendencias de detección y ajustar políticas | L3 | AG-05 | KPI-08 | Learn |
| MDO-W02 | Revisar amenazas activas en Threat analytics | Semanal | Security Operations Team | ID.RA | SOP | eo:OP-SOP-20 Revisar inteligencia de amenazas y derivar acciones | L2 | AG-06 | KPI-08 | Learn |
| MDO-W03 | Revisar usuarios más atacados y cuentas prioritarias | Semanal | Security Operations Team | ID.RA, PR.AA | POS | eo:OP-SOP-21 Proteger cuentas prioritarias | L2 | AG-07 | KPI-09 | Learn |
| MDO-W04 | Revisar Campaign Views | Semanal | Security Operations Team | DE.AE | SOP | eo:OP-SOP-18 Remediar mensajes residentes | L2 | AG-04 | KPI-02 | Learn |
| MDO-W05 | Generar informe de Secure Score | Semanal | Security Administration | ID.IM | POS | eo:OP-POS-11 Reportar la postura y su tendencia | L3 | AG-08 | KPI-06 | Learn |
| MDO-W06 | Revisar anuncios del Message Center | Semanal | Security Administration | GV.OV | SIG | eo:OP-SIG-10 Vigilar cambios de la plataforma y evaluar impacto | L3 | AG-09 | KPI-10 | Learn |
| MDO-W07 | Desplegar/probar automatización aprobada | Semanal | Security Operations Team | PR.PS | SOP | eo:OP-SOP-22 Mantener la automatización operativa | L1 | — | KPI-16 | Learn |
| MDO-M01 | Revisar configuración con Configuration Analyzer/ORCA | Mensual | Security Administration | PR.PS | POS | eo:OP-POS-12 Detectar y corregir deriva de configuración frente al baseline | L3 | AG-10 | KPI-06 | Learn |
| MDO-M02 | Revisar overrides de detección | Mensual | Security Administration | ID.IM | POS | eo:OP-POS-13 Revisar y depurar excepciones que debilitan la detección | L2 | AG-11 | KPI-07 | Learn |
| MDO-M03 | Revisar Spoof intelligence e Impersonation insights | Mensual | Security Administration | DE.AE | POS | eo:OP-POS-14 Afinar protección contra suplantación | L2 | AG-11 | KPI-07 | Learn |
| MDO-M04 | Actualizar concientización con lecciones del SOC | Mensual | Security Operations Team | PR.AT | SIG | eo:OP-SIG-11 Convertir lecciones del SOC en concientización | L1 | AG-12 | KPI-09 | Learn |
| MDO-Q01 | Revisar políticas, excepciones y apetito de autonomía | Trimestral | PO-GAC + CISO | GV.PO | SIG | eo:OP-SIG-12 Revisar políticas y excepciones del control | L1 | — | KPI-10 | Propuesta |
| MDO-Q02 | Revisar desempeño y costo de la flota | Trimestral | PO-GAC | GV.OV | IA | eo:OP-IA-02 Revisar desempeño, costo y riesgo de los agentes | L1 | AG-13 | KPI-11..15 | Propuesta |
| MDO-Q03 | Recertificar accesos de agentes y humanos | Trimestral | PO-GAC + IAM | PR.AA | AYI | eo:OP-AYI-01 Recertificar accesos privilegiados, no humanos y de agentes | L2 | AG-13 | KPI-17 | Propuesta |
| MDO-Q04 | Evaluaciones/regresión y red teaming de agentes | Trimestral | PO-GAC + AppSec | ID.IM | IA | eo:OP-IA-03 Evaluar y probar adversarialmente a los agentes | L2 | — | KPI-13 | Propuesta |
| MDO-A01 | Investigar/remover correo a pedido o disparar AIR | Por evento | Security Operations Team | RS.MI | SOP | eo:OP-SOP-11 Investigar y remediar incidentes con evidencia | L2 | AG-02 | KPI-02 | Learn |
| MDO-A02 | Hunting proactivo | Por evento | Threat hunting team | DE.CM | SOP | eo:OP-SOP-02 Buscar amenazas por técnicas priorizadas y convertir hallazgos en detecciones | L1 | AG-14 | KPI-08 | Learn |
| MDO-A03 | Compartir consultas de hunting | Por evento | Threat hunting team | DE.CM | SOP | eo:OP-SOP-23 Curar y compartir consultas de hunting | L2 | AG-14 | KPI-08 | Learn |
| MDO-A04 | Crear detecciones personalizadas | Por evento | Threat hunting team | DE.AE | SOP | eo:OP-SOP-24 Convertir hunting en detecciones automatizadas | L2 | AG-14 | KPI-08 | Learn |
| MDO-A05 | Revisar cuentas prioritarias y etiquetas | Por evento | Security Administration | PR.AA | POS | eo:OP-SOP-21 Proteger cuentas prioritarias | L2 | AG-07 | KPI-09 | Learn |
| MDO-A06 | Actualizar tickets ITSM | Diaria | Security Operations Team | RS.MA | SOP | eo:OP-SOP-25 Mantener trazabilidad de escalamientos | L3 | AG-15 | KPI-01 | Learn |
| MDO-A07 | Tabletop (incl. 'agente comprometido') | Según necesidad | SOC Oversight | ID.IM | SOP | eo:OP-SOP-26 Probar los planes de respuesta | L1 | — | KPI-16 | Propuesta |

## KPIs del control y de la flota
| ID | KPI | Definición | Meta | Cadencia | Tipo |
|---|---|---|---|---|---|
| KPI-01 | SLA de triaje M/H | % incidentes M/H triados en SLA | ≥95 % | Semanal | Control |
| KPI-02 | MTTR correo | Creación→resolución | ≤8 h High | Mensual | Control |
| KPI-03 | Consistencia de clasificación | Acuerdo entre analistas | ≥85 % | Mensual | Control |
| KPI-04 | FP de cuarentena | Liberaciones / total | <1 % | Semanal | Control |
| KPI-05 | Entradas TABL con vencimiento | % con fecha | 100 % | Mensual | Control |
| KPI-06 | Desviaciones críticas de configuración | Abiertas | 0 | Mensual | Control |
| KPI-07 | Overrides sin justificación | Cantidad | 0 | Mensual | Control |
| KPI-08 | Acciones derivadas de inteligencia | Por semana | ≥2 | Semanal | Control |
| KPI-09 | Cobertura de cuentas prioritarias | % etiquetadas | 100 % | Mensual | Control |
| KPI-10 | Cambios de plataforma evaluados | ≤7 días | 100 % | Mensual | Gobierno |
| KPI-11 | Precisión del agente de triaje | Propuestas aceptadas | ≥90 % | Mensual | Agente |
| KPI-12 | Acciones de agentes revertidas | % revertidas | <2 % | Mensual | Agente |
| KPI-13 | Agentes evaluados | % con evaluación vigente | 100 % | Trimestral | Gobierno |
| KPI-14 | Costo por tarea | SCU/tokens por tarea | Según presupuesto | Mensual | FinOps |
| KPI-15 | Desvío de consumo | vs. presupuesto | ≤10 % | Trimestral | FinOps |
| KPI-16 | Automatizaciones operativas | Fallidas | 0 | Semanal | Control |
| KPI-17 | Recertificación a tiempo | % agentes y humanos | 100 % | Trimestral | Gobierno |
| KPI-18 | Horas liberadas medidas | Tareas del runbook por agentes | Según caso de negocio | Trimestral | Valor |
| KPI-19 | Tasa de escalamiento a humano | Casos fuera de alcance | 10–30 % | Mensual | Agente |
| KPI-20 | Cobertura de observabilidad | Agentes con telemetría en Sentinel | 100 % | Mensual | Gobierno |

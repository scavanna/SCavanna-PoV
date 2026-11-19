# 03 · Modelo operativo (31 tareas)

> **GM-24 V7.1 · Sub-plan PO-GAC · Instancia de dominio: Seguridad de correo y colaboración (Microsoft Defender for Office 365 sobre Exchange Online Protection, en Microsoft Defender XDR)** · 2026-11-14 · v1.1 (re-emisión en formato uniforme de la instancia V5/V6). Plano B (*ProductPractice* / escenario). No agrega ni modifica conceptos de la V7 (379): los instancia. Escenario 100 % Microsoft sobre bases agnósticas; estado GA/preview/verificar según Microsoft Learn. Referencias DD/K4x/R/eo:OP/COE: marco interno.

Fuente: Microsoft Defender for Office 365 Security Operations Guide + tareas de mantenimiento del SOC de Defender XDR.

## 1. Tareas

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

## 2. Vista por cadencia

### Diaria

| ID | Tarea | Humano | Agente | Autonomía |
|---|---|---|---|---|
| MDO-D01 | Triar incidentes de la cola (Medium/High de Defender for Office 365) | Security Operations Team | AG-01 | L2 |
| MDO-D02 | Investigar y ejecutar acciones de respuesta sobre incidentes | Security Operations Team | AG-02 | L2 |
| MDO-D03 | Resolver incidentes remediados | Security Operations Team | AG-01 | L2 |
| MDO-D04 | Clasificar incidentes (true/false; tipo de amenaza) | Security Operations Team | AG-01 | L2 |
| MDO-D05 | Enviar FP/FN a Microsoft (Submissions) | Security Operations Team | AG-03 | L2 |
| MDO-D06 | Analizar detalles de los envíos | Security Operations Team | AG-03 | L1 |
| MDO-D07 | Agregar bloqueos en Tenant Allow/Block List | Security Operations Team | AG-03 | L2 |
| MDO-D08 | Liberar falsos positivos de cuarentena | Security Operations Team | AG-03 | L2 |
| MDO-D09 | Revisar campañas con correo entregado y remover mensajes | Security Operations Team | AG-04 | L2 |
| MDO-A06 | Actualizar tickets ITSM | Security Operations Team | AG-15 | L3 |

### Semanal

| ID | Tarea | Humano | Agente | Autonomía |
|---|---|---|---|---|
| MDO-W01 | Revisar informes de tendencias de detección | Security Operations Team | AG-05 | L3 |
| MDO-W02 | Revisar amenazas activas en Threat analytics | Security Operations Team | AG-06 | L2 |
| MDO-W03 | Revisar usuarios más atacados y cuentas prioritarias | Security Operations Team | AG-07 | L2 |
| MDO-W04 | Revisar Campaign Views | Security Operations Team | AG-04 | L2 |
| MDO-W05 | Generar informe de Secure Score | Security Administration | AG-08 | L3 |
| MDO-W06 | Revisar anuncios del Message Center | Security Administration | AG-09 | L3 |
| MDO-W07 | Desplegar/probar automatización aprobada | Security Operations Team | — | L1 |

### Mensual

| ID | Tarea | Humano | Agente | Autonomía |
|---|---|---|---|---|
| MDO-M01 | Revisar configuración con Configuration Analyzer/ORCA | Security Administration | AG-10 | L3 |
| MDO-M02 | Revisar overrides de detección | Security Administration | AG-11 | L2 |
| MDO-M03 | Revisar Spoof intelligence e Impersonation insights | Security Administration | AG-11 | L2 |
| MDO-M04 | Actualizar concientización con lecciones del SOC | Security Operations Team | AG-12 | L1 |

### Trimestral

| ID | Tarea | Humano | Agente | Autonomía |
|---|---|---|---|---|
| MDO-Q01 | Revisar políticas, excepciones y apetito de autonomía | PO-GAC + CISO | — | L1 |
| MDO-Q02 | Revisar desempeño y costo de la flota | PO-GAC | AG-13 | L1 |
| MDO-Q03 | Recertificar accesos de agentes y humanos | PO-GAC + IAM | AG-13 | L2 |
| MDO-Q04 | Evaluaciones/regresión y red teaming de agentes | PO-GAC + AppSec | — | L2 |

### Por evento

| ID | Tarea | Humano | Agente | Autonomía |
|---|---|---|---|---|
| MDO-A01 | Investigar/remover correo a pedido o disparar AIR | Security Operations Team | AG-02 | L2 |
| MDO-A02 | Hunting proactivo | Threat hunting team | AG-14 | L1 |
| MDO-A03 | Compartir consultas de hunting | Threat hunting team | AG-14 | L2 |
| MDO-A04 | Crear detecciones personalizadas | Threat hunting team | AG-14 | L2 |
| MDO-A05 | Revisar cuentas prioritarias y etiquetas | Security Administration | AG-07 | L2 |

### Según necesidad

| ID | Tarea | Humano | Agente | Autonomía |
|---|---|---|---|---|
| MDO-A07 | Tabletop (incl. 'agente comprometido') | SOC Oversight | — | L1 |

## 3. Prácticas agnósticas eo:OP (28)

| Práctica | Tareas | Origen |
|---|---|---|
| eo:OP-AYI-01 Recertificar accesos privilegiados, no humanos y de agentes | MDO-Q03 | Reutilizada (productividad/XDR) |
| eo:OP-IA-02 Revisar desempeño, costo y riesgo de los agentes | MDO-Q02 | Reutilizada (productividad/XDR) |
| eo:OP-IA-03 Evaluar y probar adversarialmente a los agentes | MDO-Q04 | Reutilizada (productividad/XDR) |
| eo:OP-POS-11 Reportar la postura y su tendencia | MDO-W05 | Reutilizada (productividad/XDR) |
| eo:OP-POS-12 Detectar y corregir deriva de configuración frente al baseline | MDO-M01 | Reutilizada (productividad/XDR) |
| eo:OP-POS-13 Revisar y depurar excepciones que debilitan la detección | MDO-M02 | Reutilizada (productividad/XDR) |
| eo:OP-POS-14 Afinar protección contra suplantación | MDO-M03 | Reutilizada (productividad/XDR) |
| eo:OP-SIG-10 Vigilar cambios de la plataforma y evaluar impacto | MDO-W06 | Reutilizada (productividad/XDR) |
| eo:OP-SIG-11 Convertir lecciones del SOC en concientización | MDO-M04 | Reutilizada (productividad/XDR) |
| eo:OP-SIG-12 Revisar políticas y excepciones del control | MDO-Q01 | Reutilizada (productividad/XDR) |
| eo:OP-SOP-02 Buscar amenazas por técnicas priorizadas y convertir hallazgos en detecciones | MDO-A02 | Reutilizada (productividad/XDR) |
| eo:OP-SOP-10 Triar incidentes por prioridad dentro del SLA | MDO-D01 | Reutilizada (productividad/XDR) |
| eo:OP-SOP-11 Investigar y remediar incidentes con evidencia | MDO-D02, MDO-A01 | Reutilizada (productividad/XDR) |
| eo:OP-SOP-12 Cerrar incidentes con criterio documentado | MDO-D03 | Reutilizada (productividad/XDR) |
| eo:OP-SOP-13 Clasificar incidentes para aprender patrones | MDO-D04 | Reutilizada (productividad/XDR) |
| eo:OP-SOP-14 Retroalimentar al fabricante con FP/FN | MDO-D05 | Reutilizada (productividad/XDR) |
| eo:OP-SOP-15 Analizar causa raíz de errores de detección | MDO-D06 | Reutilizada (productividad/XDR) |
| eo:OP-SOP-16 Mantener listas de bloqueo con vencimiento | MDO-D07 | Reutilizada (productividad/XDR) |
| eo:OP-SOP-17 Liberar cuarentena con segunda aprobación | MDO-D08 | Reutilizada (productividad/XDR) |
| eo:OP-SOP-18 Remediar mensajes residentes | MDO-D09, MDO-W04 | Reutilizada (productividad/XDR) |
| eo:OP-SOP-19 Revisar tendencias de detección y ajustar políticas | MDO-W01 | Reutilizada (productividad/XDR) |
| eo:OP-SOP-20 Revisar inteligencia de amenazas y derivar acciones | MDO-W02 | Reutilizada (productividad/XDR) |
| eo:OP-SOP-21 Proteger cuentas prioritarias | MDO-W03, MDO-A05 | Reutilizada (productividad/XDR) |
| eo:OP-SOP-22 Mantener la automatización operativa | MDO-W07 | Reutilizada (productividad/XDR) |
| eo:OP-SOP-23 Curar y compartir consultas de hunting | MDO-A03 | Reutilizada (productividad/XDR) |
| eo:OP-SOP-24 Convertir hunting en detecciones automatizadas | MDO-A04 | Reutilizada (productividad/XDR) |
| eo:OP-SOP-25 Mantener trazabilidad de escalamientos | MDO-A06 | Reutilizada (productividad/XDR) |
| eo:OP-SOP-26 Probar los planes de respuesta | MDO-A07 | Reutilizada (productividad/XDR) |

# Guías de excelencia operacional del autor: qué aportan y cómo se incorporaron

**Frontier CISO Atlas · Modelo Operativo CISO 365 · edición Microsoft · versión 2.1, revisión 3** · documento M10 · 15 de noviembre de 2026 · @SCavanna

> Propuesta de base. Las capacidades, las licencias y la cobertura se verificaron en fuentes oficiales con fecha de corte al 15 de noviembre de 2026; revalidar después de Microsoft Ignite (17 al 20 de noviembre de 2026).

## 1. Qué se hizo en cada revisión

La primera entrega de la edición Microsoft usó dos de las guías de excelencia operacional del autor: el marco de gobernanza de las operaciones de seguridad y la guía de Defender for Cloud Apps. La revisión 2 leyó los borradores de las otras nueve guías por producto. La revisión 3 incorporó las guías de riesgo interno y de ciclo de vida de los datos, tomadas del repositorio del autor. Este documento registra qué se leyó, qué se agregó al libro y con qué criterio.

| Resultado | Revisión 2 | Revisión 3 |
|---|:--:|:--:|
| Guías por producto con tareas por cadencia | 10 | 12 |
| Tareas leídas en esas guías | 323 | 379 |
| Tareas de las guías que son filas del libro | 98: las 37 de Defender for Cloud Apps y 61 nuevas | 145: las 37 de Defender for Cloud Apps y 108 nuevas |
| Tareas de las guías que ya estaban cubiertas por una fila | 225: 199 equivalentes y 26 repetidas en otra guía | 234: 208 equivalentes y 26 repetidas en otra guía |
| Casos en que la guía propone otra cadencia | 89 | 92 |
| Tareas del plano B de GM-24 que indican la guía donde está su procedimiento | 106 de 180 | 108 de 180 |
| Tareas de operación por cadencia del libro | 278 (antes, 217) | 325 |

El núcleo 2.0 no cambia en sus funciones, sus indicadores ni sus resultados clave. Tampoco cambian las capacidades, la cobertura por entorno, las licencias ni la medición de los indicadores de esta edición.

Las guías de riesgo interno y de ciclo de vida de los datos tienen un tratamiento distinto de las otras diez: se leyeron en su versión vigente, del repositorio del autor, y cada tarea nueva lleva su práctica independiente de la plataforma y, cuando la guía lo trae, su indicador técnico. El documento M11 «Puente con el repositorio del autor: guías, acciones, indicadores técnicos y formación» explica el repositorio completo.

## 2. Guías leídas

| Código | Producto | Dominio | Archivo | Fecha del archivo | Tareas leídas | Nuevas | Equivalentes | Repetidas en otra guía |
|---|---|---|---|---|:--:|:--:|:--:|:--:|
| MDO | Microsoft Defender for Office 365 | Correo y colaboración | MDO_Manual_Excelencia_Operacional_SOC.md | 28 de febrero de 2026 | 43 | 15 | 24 | 4 |
| XDR | Microsoft Defender XDR | Detección y respuesta | Microsoft_Defender_XDR_Manual_Excelencia_Operacional_SOC.md | 28 de febrero de 2026 | 50 | 13 | 33 | 4 |
| MDE | Microsoft Defender for Endpoint | Dispositivos | MDE_SecOps_Guia_Consolidada_v3.md | 9 de marzo de 2026 | 28 | 3 | 24 | 1 |
| INT | Microsoft Intune | Dispositivos | Guía de Operaciones SecOps Intune.docx | 8 de noviembre de 2026 | 13 | 6 | 6 | 1 |
| MDI | Microsoft Defender for Identity | Identidades | MDI_SecOps_Excellence_v4.md | 9 de marzo de 2026 | 24 | 5 | 19 | 0 |
| ENT | Microsoft Entra | Identidades | SecOps_Entra_Operational_Guide.md | 27 de febrero de 2026 | 44 | 5 | 33 | 6 |
| MIP | Microsoft Purview Information Protection | Datos | MIP_SecOps_ModeloOperacional_v2.md | 1 de marzo de 2026 | 35 | 6 | 23 | 6 |
| DLP | Microsoft Purview Data Loss Prevention | Datos | purview-dlp-secops-consolidado.md | 27 de abril de 2026 | 22 | 4 | 16 | 2 |
| SEN | Microsoft Sentinel | SIEM y automatización | Microsoft_Sentinel_SecOps_Operational_Guide.md | 27 de febrero de 2026 | 27 | 4 | 21 | 2 |
| MDA | Microsoft Defender for Cloud Apps | Aplicaciones y SaaS | MDCA_SecOps_Excelencia_Operacional.md | 27 de febrero de 2026 | 37 | 37 | 0 | 0 |
| IRM | Microsoft Purview Insider Risk Management | Datos | Repositorio del autor · guía 17 · Purview_Insider_Risk_Management_Guia_Excelencia_Operacional | 11 de noviembre de 2026 | 28 | 21 | 7 | 0 |
| DLM | Microsoft Purview Data Lifecycle Management y Records Management | Datos | Repositorio del autor · guía 16 · Purview_Data_Lifecycle_y_Records_Management_Guia_Excelencia_Operacional | 11 de noviembre de 2026 | 28 | 26 | 2 | 0 |
| Total |  |  |  |  | 379 | 145 | 208 | 26 |

En los diez borradores, la fecha es la de la última modificación del archivo; en las dos guías del repositorio, la de su validación. La guía de Intune está en inglés: los títulos de sus tareas se tradujeron para esta edición y el título original queda en la hoja «Tareas de las guías del autor».

Otros documentos del autor leídos. No traen tareas por cadencia:

| Dominio | Archivo | Uso en esta edición |
|---|---|---|
| Marco general | CISO_Excelencia_Gobernanza_SecOps_MASTER.md | Marco de referencia: definición y dominios de la excelencia operacional. |
| Marco general | Marco_Maestro_Excelencia_Operacional_CISO_v1.md | Marco de referencia y contraste de sus tareas con las funciones del núcleo. |
| Marco general | Excelencia_Operacional_CISO_v2.md | Ensayo y manifiesto de seis principios. No trae tareas por cadencia. |
| Dispositivos | intune-nist-csf2-mapping.md | Correspondencia de Intune con el marco. No trae tareas por cadencia. |
| Datos | Microsoft_Purview_IRM_Consolidated.md | Referencia de capacidades, licencias y correspondencia con los marcos. No trae tareas por cadencia: las tareas de riesgo interno se tomaron de la guía 17 del repositorio. |
| Datos | Microsoft_Purview_DLM_NIST_CSF2_Consolidated.md | Correspondencia con el marco, evidencia de auditoría e indicadores de madurez por fase. No trae tareas por cadencia: las tareas de ciclo de vida de los datos se tomaron de la guía 16 del repositorio. |

El dominio de nube no tiene una guía del autor entre las localizadas: sus 23 tareas provienen solo del plano B de GM-24.

## 3. Cómo se decidió qué tarea es nueva

1. **Equivalente.** Una fila del libro tiene el mismo objeto (la misma consola, el mismo control o el mismo proceso) y el mismo propósito, aunque esté en otro dominio o tenga otra cadencia. No se agrega una fila: la fila existente recibe la referencia a la guía.
2. **Repetida en otra guía.** Dos guías describen la misma tarea. Se conserva una, en el dominio de la guía donde la tarea es propia, y la otra queda como referencia. Ejemplo: el relevo entre turnos aparece en las guías de Defender XDR, de Defender for Office 365 y de Sentinel; el libro tiene una sola fila.
3. **Nueva.** Ninguna fila cubre su objeto o su propósito. Se agrega con el título de la guía, sin reescribirlo.
4. **Tareas de proceso por dominio.** El plano B de GM-24 repite en cada dominio sus tareas de proceso: el ejercicio de mesa, la recertificación de accesos y, en seis de los siete dominios, el informe mensual. Se respetó ese patrón: los informes y las revisiones de programa de cada guía quedan en su dominio.
5. **No es una tarea.** Encabezados de sección y material de referencia. Son 6 entradas, todas de la guía de Entra.

| Elemento | Convención |
|---|---|
| Identificador de una tarea nueva | G, el código de la guía y la sección original. Ejemplo: GMDO-D-5 es la tarea D-5 de la guía de Defender for Office 365. |
| Referencia a una guía | Código de la guía y sección. Ejemplo: XDR 3.8. |
| Columna Origen del libro | En una tarea del plano B: «Guías del autor» y las referencias. En una tarea nueva: la guía, la sección y, si otra guía la repite, «También en». |
| Columna Fuente del libro | Indica si la guía del autor se apoya en una guía de operación oficial con cadencias, en una guía oficial sin cadencias o en ninguna. |

Estas equivalencias son una propuesta de esta edición. La hoja «Tareas de las guías del autor» tiene la lista completa y permite corregir la fila asignada: las columnas que muestran la tarea y la cadencia del libro se recalculan solas.

## 4. Qué agregan las guías: 108 tareas nuevas

Las guías agregan cuatro cosas que el plano B no tenía: controles propios de cada producto (por ejemplo, los usuarios restringidos, las reglas de flujo de correo, las rutas de movimiento lateral y los protocolos inseguros), tareas de proceso del centro de operaciones (el relevo entre turnos, el registro de métricas diarias y la revisión de incidentes cerrados), cadencias largas, semestral y anual, y dos disciplinas completas del dominio de datos: el riesgo interno (21 tareas) y el ciclo de vida de los datos (26 tareas).

| Dominio | Tareas nuevas | Guías de origen |
|---|:--:|---|
| Correo y colaboración | 15 | Defender for Office 365 |
| Datos | 57 | Purview Data Lifecycle Management y Records Management · Purview Data Loss Prevention · Purview Information Protection · Purview Insider Risk Management |
| Detección y respuesta | 13 | Defender XDR |
| Dispositivos | 9 | Defender for Endpoint · Intune |
| Identidades | 10 | Defender for Identity · Entra |
| SIEM y automatización | 4 | Sentinel |
| Total | 108 |  |

### Correo y colaboración (15)

| ID | Tarea | Cadencia | Tipo de práctica | También en |
|---|---|:--:|---|---|
| GMDO-D-5 | Gestión de Entidades Restringidas (Restricted Users) | Diaria | Operación | — |
| GMDO-D-7 | Validación de Detecciones ZAP | Diaria | Operación | — |
| GMDO-D-8 | Verificación de Patrones de Envío Sospechosos (BEC Detection) | Diaria | Operación | — |
| GMDO-S-7 | Auditoría de Reglas de Transporte (Mail Flow Rules) | Semanal | Postura | — |
| GMDO-S-10 | Reporte Semanal al Manager | Semanal | Operación | — |
| GMDO-M-4 | Auditoría de Políticas de Cuarentena | Mensual | Postura | — |
| GMDO-M-5 | Programa de Attack Simulation Training — Análisis y Planificación Mensual | Mensual | Operación | MDO S-6; MDO Sem-2; XDR 7.5 |
| GMDO-M-7 | Análisis de Tendencias de User Reporting (Efectividad como Sensores) | Mensual | Operación | — |
| GMDO-M-9 | Backup de Políticas de Seguridad (PowerShell Automation) | Mensual | Operación | — |
| GMDO-M-10 | Informe Ejecutivo Mensual al CISO y Board | Mensual | Operación | — |
| GMDO-Sem-1 | Recalibración de Postura de Seguridad | Semestral | Postura | — |
| GMDO-An-1 | Revisión del Programa Operativo Completo | Anual | Operación | — |
| GMDO-A-1 | Respuesta a Brote de Phishing/Malware (Outbreak Response) | Por evento | Operación | XDR 8.2 |
| GMDO-A-4 | Message Trace — Investigación Forense de Entrega | Por evento | Operación | — |
| GMDO-A-5 | Búsqueda de Auditoría — Actividades Administrativas Sospechosas | Por evento | Operación | — |

### Datos (57)

| ID | Tarea | Cadencia | Tipo de práctica | También en |
|---|---|:--:|---|---|
| GMIP-D-04 | Validación de Accesos a Contenido Cifrado (Azure Rights Management) | Diaria | Operación | MIP D-09; MIP S-04 |
| GMIP-D-08 | Validación de Cambios Administrativos del Día Anterior | Diaria | Señales y cambios | MIP M-03; DLM D-02 |
| GMIP-S-05 | Pruebas de Acceso Controlado a Datos Altamente Sensibles | Semanal | Operación | — |
| GMIP-S-08 | Validación de Cobertura de Logging de Purview | Semanal | Postura | — |
| GMIP-S-10 | Reporte Semanal de Postura de Seguridad de Datos | Semanal | Operación | — |
| GMIP-M-02 | Evaluación de Efectividad del Cifrado Persistente | Mensual | Postura | — |
| GDLP-8.1-3 | Verificar salud de sensores Endpoint DLP: cobertura del agente MDE y sincronización de políticas (~1 hora desde cambio) | Diaria | Operación | DLP 8.3-3 |
| GDLP-8.3-2 | Actualización de datasets EDM si la fuente de datos cambió | Mensual | Operación | — |
| GDLP-8.3-5 | Revisión del estado de clasificadores entrenables: verificar que la precisión no haya degradado por cambios en el corpus documental | Mensual | Operación | — |
| GDLP-8.5-1 | Revisión estratégica del programa: alcance de cobertura vs. riesgo residual aceptado | Anual | Operación | — |
| GIRM-D-01 | Verificación de salud de conectores de señales (HR Data, Physical Badging y endpoints) | Diaria | Postura | — |
| GIRM-D-03 | Análisis contextual de secuencias y exfiltración acumulada en Activity Explorer | Diaria | Señales y cambios | — |
| GIRM-D-04 | Monitoreo diario de alertas de Risky AI Usage y Risky Agents (Preview) | Diaria | Postura | — |
| GIRM-D-06 | Supervisión operativa de usuarios en nivel Elevated bajo Adaptive Protection | Diaria | Postura | — |
| GIRM-D-07 | Verificación diaria de seudonimización e inspección del Insider Risk Audit Log independiente | Diaria | Señales y cambios | — |
| GIRM-D-08 | Evaluación independiente de solicitudes de doble autorización en Forensic Evidence | Diaria | Operación | — |
| GIRM-S-01 | Gestión de casos activos, cadena de custodia en Case Notes e inspección en Content Explorer | Semanal | Señales y cambios | — |
| GIRM-S-02 | Chequeo semanal de salud de políticas (Policy Health Check) y advertencias pendientes | Semanal | Señales y cambios | — |
| GIRM-S-03 | Calibración de umbrales (Tuning), variantes de indicadores y Detection Groups | Semanal | Postura | — |
| GIRM-S-05 | Actualización de Priority User Groups y alineación con Information Barriers | Semanal | Acceso e identidad | — |
| GIRM-S-06 | Verificación de automatizaciones Power Automate y conector Microsoft Sentinel | Semanal | Operación | — |
| GIRM-M-01 | Exportación y auditoría independiente del Insider Risk Audit Log (previo a purga de 180 días) | Mensual | Señales y cambios | — |
| GIRM-M-03 | Revisión mensual de efectividad preventiva de Adaptive Protection (DLP + Entra CA + DLCM) | Mensual | Postura | — |
| GIRM-T-01 | Revisión trimestral de Evaluación de Impacto de Privacidad (DPIA) y cumplimiento laboral | Trimestral | Señales y cambios | — |
| GIRM-T-02 | Prueba end-to-end de Adaptive Protection y sincronización bidireccional con Defender XDR | Trimestral | Postura | — |
| GIRM-SM-01 | Análisis semestral de lecciones aprendidas de casos cerrados y efectividad conductual | Semestral | Señales y cambios | — |
| GIRM-A-01 | Recertificación anual del Estatuto Tripartito y simulacro ejecutivo de robo de IP | Anual | Señales y cambios | — |
| GIRM-AH-01 | Investigación urgente de robo de propiedad intelectual por usuario saliente o prioritario | Por evento | Señales y cambios | — |
| GIRM-AH-02 | Activación controlada de captura visual Forensic Evidence con doble autorización | Por evento | Operación | — |
| GIRM-AH-03 | Escalamiento formal de caso confirmado hacia Microsoft Purview eDiscovery (Premium) | Por evento | Operación | — |
| GIRM-AH-05 | Contención de exposición sensible en IA generativa o agentes autónomos (Risky AI / Risky Agents) | Por evento | Operación | — |
| GDLM-D-01 | Monitoreo de estado de distribución y errores en políticas de retención y etiquetas | Diaria | Postura | — |
| GDLM-D-03 | Seguimiento de cola activa de revisiones de disposición próximas a vencer o auto-aprobarse | Diaria | Operación | — |
| GDLM-D-04 | Conciliación diaria de eventos transaccionales en Event-Based Retention | Diaria | Operación | — |
| GDLM-D-05 | Supervisión de alertas y ejecuciones activas de Priority Cleanup | Diaria | Operación | — |
| GDLM-D-06 | Verificación de conversión a Inactive Mailboxes en bajas críticas de personal | Diaria | Operación | — |
| GDLM-D-07 | Monitoreo de cuotas en Recoverable Items y Auto-Expanding Archives hasta 3 TB | Diaria | Postura | — |
| GDLM-D-08 | Verificación de políticas de retención y Collection Policies para Copilot y aplicaciones IA | Diaria | Postura | — |
| GDLM-S-01 | Muestreo de precisión en políticas de auto-aplicación de etiquetas y Cloud Attachments | Semanal | Postura | — |
| GDLM-S-02 | Auditoría de membresía dinámica e higiene de atributos en Adaptive Policy Scopes | Semanal | Postura | — |
| GDLM-S-03 | Ejecución de mesas semanales de revisión de disposición multi-etapa (etapas 1 a 5) | Semanal | Operación | — |
| GDLM-S-04 | Monitoreo de crecimiento en Preservation Hold Libraries y paso a Microsoft 365 Archive | Semanal | Postura | — |
| GDLM-S-05 | Revisión de intentos bloqueados o remoción administrativa de etiquetas en Records | Semanal | Operación | — |
| GDLM-S-06 | Gobernanza de ciclo de vida sobre nuevos sitios M365, Teams y agentes Copilot Studio | Semanal | Postura | — |
| GDLM-M-01 | Exportación, conciliación y archivo firmado de Proof of Disposal | Mensual | Operación | — |
| GDLM-M-02 | Medición y saneamiento de deuda de retención en Inactive Mailboxes y OneDrive | Mensual | Postura | — |
| GDLM-M-03 | Evaluación de superficie ROT pre-IA y verificación de purga en SubstrateHolds | Mensual | Postura | — |
| GDLM-M-04 | Conciliación mensual de registros basados en eventos sin Asset ID o con evento omitido | Mensual | Operación | — |
| GDLM-T-01 | Revisión integral del File Plan frente a cambios normativos y simplificación de series | Trimestral | Señales y cambios | — |
| GDLM-T-02 | Prueba controlada de los 4 principios de precedencia y validación de registros migrados | Trimestral | Operación | — |
| GDLM-SM-01 | Auditoría de Preservation Lock, Regulatory Records y holgura de límites del tenant | Semestral | Señales y cambios | — |
| GDLM-A-01 | Recertificación ejecutiva de la Tabla de Retención (ISO 15489-1), RACI y simulacro tabletop | Anual | Señales y cambios | — |
| GDLM-AH-01 | Ejecución de Priority Cleanup ante derrame crítico de datos sensibles (Data Spillage) | Por evento | Operación | — |
| GDLM-AH-02 | Congelamiento inmediato de disposición y aplicación de eDiscovery Hold ante litigio o brecha | Por evento | Operación | — |
| GDLM-AH-03 | Respuesta ante desactivación o alteración maliciosa de políticas de retención | Por evento | Operación | — |
| GDLM-AH-04 | Incorporación masiva de nueva regulación o entidad adquirida (M&A) al File Plan | Por evento | Señales y cambios | — |
| GDLM-AH-05 | Remediación de emergencia por saturación de Recoverable Items o Preservation Hold Library | Por evento | Postura | — |

### Detección y respuesta (13)

| ID | Tarea | Cadencia | Tipo de práctica | También en |
|---|---|:--:|---|---|
| GXDR-3.7 | Registro de Métricas Diarias | Diaria | Operación | MIP D-10 |
| GXDR-3.8 | Hand-over entre Turnos | Diaria | Operación | MDO D-10; SEN 3.8 |
| GXDR-4.3 | Revisión de Incidentes Cerrados (Post-Incident Review Semanal) | Semanal | Operación | MIP S-06; SEN 4.7 |
| GXDR-4.4 | Evaluación de Configuraciones (Configuration Drift) | Semanal | Postura | — |
| GXDR-4.10 | Revisión de SLAs Operativos y Actualización de Runbooks | Semanal | Operación | — |
| GXDR-5.9 | Auditoría de Funcionalidades y ROI Review | Mensual | Operación | MDO An-3; XDR 6.5 |
| GXDR-5.11 | Validación de Backups y Recuperación | Mensual | Operación | — |
| GXDR-6.1 | Revisión de Roles y Responsabilidades (SOC Governance) | Semestral | Operación | — |
| GXDR-6.7 | Revisión de Coordinación con Stakeholders | Semestral | Operación | — |
| GXDR-7.1 | Revisión Completa del Programa (Full Program Review) | Anual | Operación | — |
| GXDR-7.2 | Reevaluación Estratégica de Postura (Strategic Posture Reassessment) | Anual | Operación | — |
| GXDR-7.4 | Auditoría Externa y Compliance | Anual | Operación | XDR 8.3; DLP 8.5-3 |
| GXDR-8.5 | Despliegue de Nuevas Funcionalidades | Por evento | Señales y cambios | — |

### Dispositivos (9)

| ID | Tarea | Cadencia | Tipo de práctica | También en |
|---|---|:--:|---|---|
| GMDE-5.4 | Prueba End-to-End del Pipeline de Detección | Mensual | Operación | — |
| GMDE-8.1 | Métricas Anuales de Desempeño del Programa | Anual | Operación | MDE 8.2 |
| GMDE-6.5 | Coordinar con Microsoft Threat Experts | Por evento | Operación | — |
| GINT-1.1 | Supervisar el cumplimiento de los dispositivos y el estado de las líneas base de seguridad | Diaria | Postura | INT 3.1 |
| GINT-1.2 | Revisar Endpoint analytics para identificar riesgos en dispositivos Windows | Diaria | Operación | — |
| GINT-1.3 | Supervisar la inscripción automática de dispositivos y sus notificaciones | Diaria | Operación | — |
| GINT-2.2 | Detectar dispositivos inactivos y aplicar reglas de limpieza | Semanal | Operación | — |
| GINT-3.3 | Verificar el uso de las funciones de seguridad: firewall, BitLocker y reducción de la superficie de ataque | Mensual | Postura | — |
| GINT-4.2 | Actualizar términos y condiciones o directivas de acceso | Por evento | Operación | — |

### Identidades (10)

| ID | Tarea | Cadencia | Tipo de práctica | También en |
|---|---|:--:|---|---|
| GMDI-W4 | Análisis de Lateral Movement Paths (LMP) | Semanal | Operación | — |
| GMDI-W5 | Auditoría de Protocolos Inseguros | Semanal | Postura | — |
| GMDI-8.2a | Capacity Planning de Sensores | Anual | Operación | — |
| GMDI-8.2b | Purple Team — Validación de Detección | Anual | Operación | — |
| GMDI-Q3 | Proceso de Servidor — Onboarding de Nuevos DCs | Por evento | Operación | — |
| GENT-2.7 | Monitoreo de Actividades Privilegiadas (PIM / Entra) | Diaria | Acceso e identidad | ENT 6.4.2; ENT 6.4.3 |
| GENT-6.1 | Gestión del Ciclo de Vida de Identidades | Diaria | Acceso e identidad | — |
| GENT-3.7 | Revisión de Cambios en el Entorno (Change Management) | Semanal | Señales y cambios | — |
| GENT-7.2 | Verificación de Apps y SSO | Mensual | Acceso e identidad | — |
| GENT-5.4 | Offboarding de Emergencia (Lifecycle Workflows) | Por evento | Acceso e identidad | — |

### SIEM y automatización (4)

| ID | Tarea | Cadencia | Tipo de práctica | También en |
|---|---|:--:|---|---|
| GSEN-4.2 | Revisión y Tuning de Reglas Analíticas | Semanal | Operación | ENT 3.2; MIP S-07 |
| GSEN-4.8 | Reporte Semanal a Stakeholders | Semanal | Operación | ENT 3.10 |
| GSEN-5.9 | Revisión de Arquitectura SOC | Mensual | Operación | ENT 4.7 |
| GSEN-5.10 | Roadmap de Mejoras del SOC | Mensual | Operación | ENT 4.10 |

## 5. Dónde las guías proponen otra cadencia

En 92 de las 234 tareas ya cubiertas, la guía del autor propone una cadencia distinta de la que tiene la fila del libro. No se cambió la cadencia de ninguna fila: la diferencia queda a la vista para que la decida el dueño de cada control. En 9 casos, la fila del libro dice «según necesidad» y la guía fija una frecuencia: son los ejercicios de mesa.

| Cadencia en la guía | Cadencia en el libro | Casos |
|---|---|:--:|
| Mensual | Semanal | 15 |
| Semanal | Mensual | 13 |
| Semanal | Diaria | 8 |
| Diaria | Semanal | 6 |
| Mensual | Diaria | 6 |
| Mensual | Trimestral | 6 |
| Semestral | Trimestral | 5 |
| Anual | Según necesidad | 4 |
| Semanal | Trimestral | 4 |
| Anual | Mensual | 3 |
| Mensual | Según necesidad | 3 |
| Por evento | Semanal | 3 |
| Semestral | Mensual | 3 |
| Semanal | Por evento | 2 |
| Semestral | Semanal | 2 |
| Trimestral | Mensual | 2 |
| Anual | Semanal | 1 |
| Diaria | Por evento | 1 |
| Por evento | Anual | 1 |
| Por evento | Diaria | 1 |
| Por evento | Mensual | 1 |
| Por evento | Según necesidad | 1 |
| Semestral | Según necesidad | 1 |
| Total |  | 92 |

| Referencia | Tarea de la guía | Cadencia en la guía | Fila del libro | Cadencia en el libro |
|---|---|:--:|---|:--:|
| MDO D-9 | Revisión de Top Targeted Users | Diaria | MDO-W03 | Semanal |
| MDO S-1 | Threat Hunting con Threat Explorer y Advanced Hunting | Semanal | MDO-A02 | Por evento |
| MDO S-4 | Auditoría de Configuración (Configuration Analyzer) | Semanal | MDO-M01 | Mensual |
| MDO S-5 | Gestión de Inteligencia de Suplantación (Spoof Intelligence) | Semanal | MDO-M03 | Mensual |
| MDO S-6 | Revisión de Resultados de Simulaciones de Ataque (AST) | Semanal | GMDO-M-5 | Mensual |
| MDO S-8 | Análisis y Actualización de Priority Accounts | Semanal | MDO-A05 | Por evento |
| MDO S-9 | Revisión de Detection Overrides (Excepciones activas) | Semanal | MDO-M02 | Mensual |
| MDO M-1 | Revisión Integral de Postura de Seguridad (Secure Score) | Mensual | MDO-W05 | Semanal |
| MDO M-6 | Revisión de Integración SIEM (Microsoft Sentinel) | Mensual | XDR-W06 | Semanal |
| MDO A-3 | Bloqueo de Emergencia (Tenant Allow/Block List) | Por evento | MDO-D07 | Diaria |
| MDO Sem-2 | Refresh del Programa de Simulación y Training | Semestral | GMDO-M-5 | Mensual |
| MDO Sem-3 | Revisión de Integración con Herramientas del Ecosistema | Semestral | XDR-W06 | Semanal |
| MDO An-2 | Ejercicio de Mesa (Tabletop) de Respuesta a Incidentes | Anual | MDO-A07 | Según necesidad |
| MDO An-3 | Revisión de Licencias y Capacidades Nuevas | Anual | GXDR-5.9 | Mensual |
| XDR 4.7 | Revisión de Cuentas Privilegiadas | Semanal | ID-M02 | Mensual |
| XDR 5.3 | Afinamiento de Attack Surface Reduction (ASR) | Mensual | EP-W04 | Semanal |
| XDR 5.7 | Análisis de Exposición y Vulnerabilidades | Mensual | XDR-W03 | Semanal |
| XDR 5.8 | Revisión de Automatizaciones (Logic Apps / SOAR) | Mensual | XDR-W06 | Semanal |
| XDR 5.13 | Tracking de Cambios en Productos | Mensual | XDR-W05 | Semanal |
| XDR 6.2 | Mantenimiento de Runbooks y Playbooks | Semestral | XDR-Q01 | Trimestral |
| XDR 6.3 | Evaluación de Cobertura MITRE ATT&CK | Semestral | SI-W03 | Semanal |
| XDR 6.4 | Revisión de Controles de Identidad y Zero Trust | Semestral | ID-M04 | Mensual |
| XDR 6.5 | Revisión de Licenciamiento y Feature Register | Semestral | GXDR-5.9 | Mensual |
| XDR 6.6 | Revisión de Service Health & Domain Configuration | Semestral | ID-Q01 | Trimestral |
| XDR 7.3 | Ejercicio de Red Team / Purple Team Anual | Anual | XDR-A05 | Según necesidad |
| XDR 7.5 | Revisión de Campañas de Phishing Simulation y DLP | Anual | GMDO-M-5 | Mensual |
| XDR 8.3 | Ante Eventos Regulatorios o Auditoría | Por evento | GXDR-7.4 | Anual |
| XDR 8.4 | Threat Hunting Proactivo Específico | Por evento | XDR-W01 | Semanal |
| XDR 8.6 | Despliegue de Automation (SOAR) | Por evento | XDR-W06 | Semanal |
| XDR 8.7 | Tabletop Exercises (IR Readiness) | Por evento | XDR-A05 | Según necesidad |
| MDE 3.5 | Validar Políticas ASR y Cobertura de Endpoints | Diaria | EP-W04 | Semanal |
| MDE 3.6 | Monitorear Exposure Score (MDVM) | Diaria | EP-W03 | Semanal |
| MDE 4.2 | Revisar y Actualizar Playbooks de Respuesta | Semanal | XDR-Q01 | Trimestral |
| MDE 4.3 | Auditar Permisos RBAC | Semanal | EP-M01 | Mensual |
| MDE 4.5 | Revisar Exclusiones de Antivirus | Semanal | EP-M05 | Mensual |
| MDE 4.6 | Auditar Onboarding/Offboarding de Dispositivos | Semanal | EP-M03 | Mensual |
| MDE 5.1 | Revisar Security Posture (Secure Score) | Mensual | XDR-W03 | Semanal |
| MDE 5.3 | Vulnerability Assessment Completo (MDVM) | Mensual | EP-W03 | Semanal |
| MDE 5.5 | Ejercicios Tabletop de Incident Response | Mensual | EP-A05 | Según necesidad |
| MDE 6.4 | Bloqueo de Indicadores de Compromiso (IoC) | Por evento | EP-W05 | Semanal |
| MDE 7.1 | Revisión Completa de RBAC | Semestral | EP-Q03 | Trimestral |
| MDE 7.2 | Detection Engineering Refresh | Semestral | XDR-Q01 | Trimestral |
| MDE 7.3 | Revisión Estratégica de Attack Surface Reduction | Semestral | EP-Q01 | Trimestral |
| MDE 8.3 | Ejercicio Anual IR — Full Scale | Anual | EP-A05 | Según necesidad |
| INT 2.1 | Auditar las asignaciones de las líneas base de seguridad | Semanal | EP-M02 | Mensual |
| INT 2.3 | Actualizar las versiones de las líneas base de seguridad | Semanal | EP-M02 | Mensual |
| INT 3.1 | Revisar el cumplimiento y la eficacia de las directivas | Mensual | GINT-1.1 | Diaria |
| INT 4.3 | Probar en piloto las nuevas líneas base de seguridad | Por evento | EP-M02 | Mensual |
| MDI D4 | Respuesta sobre Identidades | Diaria | ID-A01 | Por evento |
| MDI W1 | Alert Tuning y Reducción de Ruido | Semanal | ID-D04 | Diaria |
| MDI M1 | Evaluación de Postura — Identity Secure Score | Mensual | ID-W01 | Semanal |
| MDI M3 | Revisión de Identities Security Initiative | Mensual | XDR-W03 | Semanal |
| MDI M5 | Seguimiento de Cambios en la Plataforma | Mensual | ID-W05 | Semanal |
| MDI 8.1 | Tabletop Exercises: Compromiso de Cuenta Privilegiada y Movimiento Lateral / Pre-Ransomware | Semestral | ID-A04 | Según necesidad |
| ENT 3.5 | Revisión de Cuentas Comprometidas o de Alto Riesgo | Semanal | ID-D03 | Diaria |
| ENT 3.6 | Pruebas de Playbooks y Runbooks | Semanal | SI-Q04 | Trimestral |
| ENT 4.1 | Revisión Formal de Postura de Seguridad | Mensual | XDR-W03 | Semanal |
| ENT 4.2 | Actualización de Runbooks y Procedimientos | Mensual | XDR-Q01 | Trimestral |
| ENT 4.5 | Simulacros de Respuesta a Incidentes (Tabletop Exercises) | Mensual | XDR-A05 | Según necesidad |
| ENT 4.8 | Revisión de Integraciones y Conectores | Mensual | SI-D02 | Diaria |
| ENT 6.4.1 | Revisión Semanal de Assignments | Semanal | ID-M02 | Mensual |
| ENT 6.4.2 | Análisis del Resource Audit (Activaciones) | Semanal | GENT-2.7 | Diaria |
| ENT 6.4.3 | Configuración de Alertas PIM | Mensual | GENT-2.7 | Diaria |
| ENT 6.5.1 | Monitoreo de Reviews Activos | Semanal | ID-Q03 | Trimestral |
| MIP D-02 | Monitoreo del M365 Unified Audit Log — Eventos de Information Protection | Diaria | DP-W04 | Semanal |
| MIP D-05 | Revisión de Eventos de Oversharing (Teams / SharePoint) | Diaria | DP-W03 | Semanal |
| MIP S-01 | Revisión y Tuning de Falsos Positivos en Alertas de Purview | Semanal | DP-D03 | Diaria |
| MIP S-04 | Revisión de Eventos de Revocación de Acceso | Semanal | GMIP-D-04 | Diaria |
| MIP S-09 | Revisión de Cuentas Privilegiadas con Acceso a Datos Protegidos | Semanal | DP-Q03 | Trimestral |
| MIP M-03 | Auditoría Formal de Cambios Administrativos del Mes | Mensual | GMIP-D-08 | Diaria |
| MIP M-05 | Ejercicio de Tabletop: Incidente de Fuga de Datos | Mensual | DP-A04 | Según necesidad |
| MIP M-06 | Revisión de Cobertura del Information Protection Scanner | Mensual | DP-D05 | Diaria |
| MIP M-08 | Validación de Integración Purview–Sentinel–Defender | Mensual | XDR-W06 | Semanal |
| DLP 8.2-2 | Revisión de justificaciones de override: identificar patrones de evasión (justificaciones genéricas repetidas) | Semanal | DP-M02 | Mensual |
| DLP 8.2-3 | Revisión de incidentes DLP abiertos y tiempo de resolución | Semanal | DP-D02 | Diaria |
| DLP 8.2-4 | Actualización de listas de dominios de confianza y excepciones de grupos | Semanal | DP-M02 | Mensual |
| DLP 8.3-3 | Revisión de cobertura Endpoint DLP (% de dispositivos gestionados con agente activo) | Mensual | GDLP-8.1-3 | Diaria |
| DLP 8.4-2 | Re-certificación de excepciones documentadas (grupos excluidos, dominios de confianza) | Trimestral | DP-M02 | Mensual |
| DLP 8.4-4 | Presentación de KPIs al CISO/Board | Trimestral | DP-M04 | Mensual |
| DLP 8.5-2 | Simulación de respuesta a incidente de exfiltración masiva (tabletop exercise) | Anual | DP-A04 | Según necesidad |
| DLP 8.5-4 | Capacitación de analistas en nuevas capacidades de la plataforma | Anual | XDR-M05 | Mensual |
| DLP 8.5-5 | Revisión del roadmap Microsoft Purview para planificar adopción de nuevas funciones | Anual | DP-W05 | Semanal |
| SEN 3.7 | Revisión de Threat Intelligence Matches | Diaria | SI-W06 | Semanal |
| SEN 4.4 | Threat Hunting Programado | Semanal | SI-D04 | Diaria |
| SEN 4.6 | Validación de Automation Rules | Semanal | SI-D05 | Diaria |
| SEN 5.2 | Revisión de SOC Optimization | Mensual | SI-W05 | Semanal |
| SEN 5.3 | Evaluación de Cobertura MITRE ATT&CK | Mensual | SI-W03 | Semanal |
| SEN 5.5 | Pruebas de Playbooks Críticos | Mensual | SI-Q04 | Trimestral |
| SEN 5.7 | Actualización de Runbooks Operativos | Mensual | XDR-Q01 | Trimestral |
| IRM M-04 | Renovación preventiva del contexto del Alert Triage Agent (ventana 90 días) y control de SCUs | Mensual | DP-Q02 | Trimestral |
| IRM M-05 | Auditoría mensual de los 6 Role Groups, Administrative Units, capacidad forense y comité ejecutivo | Mensual | DP-Q03 | Trimestral |
| DLM M-05 | Auditoría mensual de privilegios RBAC/PIM, límite de revisores y costos Pay-As-You-Go | Mensual | DP-Q03 | Trimestral |

## 6. Correspondencia completa, por guía

Las 37 tareas de la guía de Defender for Cloud Apps son filas del libro desde la primera entrega, con identificadores MDA; no se repiten aquí.

### Microsoft Defender for Office 365 (MDO): 43 tareas

| Referencia | Tarea de la guía | Cadencia | Relación | Fila del libro | Tarea del libro |
|---|---|:--:|---|:--:|---|
| MDO D-1 | Monitoreo y Triaje de la Cola de Incidentes | Diaria | Equivalente | MDO-D01 | Triar incidentes de la cola (Medium/High de Defender for Office 365) |
| MDO D-2 | Supervisión del Centro de Acciones (Action Center) — AIR | Diaria | Equivalente | XDR-D03 | Revisar el Action center: acciones pendientes y ejecutadas (AIR) |
| MDO D-3 | Gestión de Envíos de Usuarios (User Reported Messages) | Diaria | Equivalente | MDO-D06 | Analizar detalles de los envíos |
| MDO D-4 | Gestión de Cuarentena | Diaria | Equivalente | MDO-D08 | Liberar falsos positivos de cuarentena |
| MDO D-5 | Gestión de Entidades Restringidas (Restricted Users) | Diaria | Nueva | GMDO-D-5 | — |
| MDO D-6 | Revisión de Campañas Entregadas | Diaria | Equivalente | MDO-D09 | Revisar campañas con correo entregado y remover mensajes |
| MDO D-7 | Validación de Detecciones ZAP | Diaria | Nueva | GMDO-D-7 | — |
| MDO D-8 | Verificación de Patrones de Envío Sospechosos (BEC Detection) | Diaria | Nueva | GMDO-D-8 | — |
| MDO D-9 | Revisión de Top Targeted Users | Diaria | Equivalente | MDO-W03 | Revisar usuarios más atacados y cuentas prioritarias |
| MDO D-10 | Cierre de Turno — Asegurar Cola de Incidentes | Diaria | Repetida en otra guía | GXDR-3.8 | Hand-over entre Turnos |
| MDO S-1 | Threat Hunting con Threat Explorer y Advanced Hunting | Semanal | Equivalente | MDO-A02 | Hunting proactivo |
| MDO S-2 | Análisis de Tendencias de Detección | Semanal | Equivalente | MDO-W01 | Revisar informes de tendencias de detección |
| MDO S-3 | Inteligencia de Amenazas (Threat Analytics) | Semanal | Equivalente | MDO-W02 | Revisar amenazas activas en Threat analytics |
| MDO S-4 | Auditoría de Configuración (Configuration Analyzer) | Semanal | Equivalente | MDO-M01 | Revisar configuración con Configuration Analyzer/ORCA |
| MDO S-5 | Gestión de Inteligencia de Suplantación (Spoof Intelligence) | Semanal | Equivalente | MDO-M03 | Revisar Spoof intelligence e Impersonation insights |
| MDO S-6 | Revisión de Resultados de Simulaciones de Ataque (AST) | Semanal | Repetida en otra guía | GMDO-M-5 | Programa de Attack Simulation Training — Análisis y Planificación Mensual |
| MDO S-7 | Auditoría de Reglas de Transporte (Mail Flow Rules) | Semanal | Nueva | GMDO-S-7 | — |
| MDO S-8 | Análisis y Actualización de Priority Accounts | Semanal | Equivalente | MDO-A05 | Revisar cuentas prioritarias y etiquetas |
| MDO S-9 | Revisión de Detection Overrides (Excepciones activas) | Semanal | Equivalente | MDO-M02 | Revisar overrides de detección |
| MDO S-10 | Reporte Semanal al Manager | Semanal | Nueva | GMDO-S-10 | — |
| MDO M-1 | Revisión Integral de Postura de Seguridad (Secure Score) | Mensual | Equivalente | MDO-W05 | Generar informe de Secure Score |
| MDO M-2 | Ajuste Fino de Políticas Anti-Phishing | Mensual | Equivalente | MDO-M03 | Revisar Spoof intelligence e Impersonation insights |
| MDO M-3 | Limpieza de Tenant Allow/Block List (TABL) | Mensual | Equivalente | MDO-M02 | Revisar overrides de detección |
| MDO M-4 | Auditoría de Políticas de Cuarentena | Mensual | Nueva | GMDO-M-4 | — |
| MDO M-5 | Programa de Attack Simulation Training — Análisis y Planificación Mensual | Mensual | Nueva | GMDO-M-5 | — |
| MDO M-6 | Revisión de Integración SIEM (Microsoft Sentinel) | Mensual | Equivalente | XDR-W06 | Desplegar/probar automatizaciones aprobadas; verificar conectividad SIEM |
| MDO M-7 | Análisis de Tendencias de User Reporting (Efectividad como Sensores) | Mensual | Nueva | GMDO-M-7 | — |
| MDO M-8 | Auditoría de Roles y Permisos RBAC | Mensual | Equivalente | XDR-M02 | Revisar Unified RBAC: roles, permisos y asignaciones de humanos y agentes |
| MDO M-9 | Backup de Políticas de Seguridad (PowerShell Automation) | Mensual | Nueva | GMDO-M-9 | — |
| MDO M-10 | Informe Ejecutivo Mensual al CISO y Board | Mensual | Nueva | GMDO-M-10 | — |
| MDO A-1 | Respuesta a Brote de Phishing/Malware (Outbreak Response) | Por evento | Nueva | GMDO-A-1 | — |
| MDO A-2 | Búsqueda y Purga de Correos (Search and Purge) | Por evento | Equivalente | MDO-A01 | Investigar/remover correo a pedido o disparar AIR |
| MDO A-3 | Bloqueo de Emergencia (Tenant Allow/Block List) | Por evento | Equivalente | MDO-D07 | Agregar bloqueos en Tenant Allow/Block List |
| MDO A-4 | Message Trace — Investigación Forense de Entrega | Por evento | Nueva | GMDO-A-4 | — |
| MDO A-5 | Búsqueda de Auditoría — Actividades Administrativas Sospechosas | Por evento | Nueva | GMDO-A-5 | — |
| MDO A-6 | Creación de Custom Detection Rules (Advanced Hunting) | Por evento | Equivalente | MDO-A04 | Crear detecciones personalizadas |
| MDO A-7 | Plantilla de Comunicación de Incidentes Críticos a Ejecutivos | Por evento | Equivalente | XDR-A01 | Responder a incidentes mayores con el CSIRT (aislar, revocar, deshabilitar, contener) |
| MDO Sem-1 | Recalibración de Postura de Seguridad | Semestral | Nueva | GMDO-Sem-1 | — |
| MDO Sem-2 | Refresh del Programa de Simulación y Training | Semestral | Repetida en otra guía | GMDO-M-5 | Programa de Attack Simulation Training — Análisis y Planificación Mensual |
| MDO Sem-3 | Revisión de Integración con Herramientas del Ecosistema | Semestral | Equivalente | XDR-W06 | Desplegar/probar automatizaciones aprobadas; verificar conectividad SIEM |
| MDO An-1 | Revisión del Programa Operativo Completo | Anual | Nueva | GMDO-An-1 | — |
| MDO An-2 | Ejercicio de Mesa (Tabletop) de Respuesta a Incidentes | Anual | Equivalente | MDO-A07 | Tabletop (incl. 'agente comprometido') |
| MDO An-3 | Revisión de Licencias y Capacidades Nuevas | Anual | Repetida en otra guía | GXDR-5.9 | Auditoría de Funcionalidades y ROI Review |

### Microsoft Defender XDR (XDR): 50 tareas

| Referencia | Tarea de la guía | Cadencia | Relación | Fila del libro | Tarea del libro |
|---|---|:--:|---|:--:|---|
| XDR 3.1 | Monitoreo y Triaje de la Cola de Incidentes | Diaria | Equivalente | XDR-D01 | Triar la cola de incidentes unificada (todas las fuentes; High/Medium primero) |
| XDR 3.2 | Revisión del Centro de Acciones (Action Center) | Diaria | Equivalente | XDR-D03 | Revisar el Action center: acciones pendientes y ejecutadas (AIR) |
| XDR 3.3 | Revisión de Alertas Críticas de Identidad y Correo | Diaria | Equivalente | XDR-D01 | Triar la cola de incidentes unificada (todas las fuentes; High/Medium primero) |
| XDR 3.4 | Verificación de Integridad del Pipeline de Telemetría | Diaria | Equivalente | XDR-D06 | Revisar salud de sensores (EDR/AV, MDI, conectores de apps) |
| XDR 3.5 | Identificación y Envío de Falsos Positivos / Negativos | Diaria | Equivalente | XDR-D05 | Gestionar FP/FN y tuning de alertas en todos los sensores |
| XDR 3.6 | Verificación de Salud Operativa del Sistema (Daily Health Check) | Diaria | Equivalente | XDR-D06 | Revisar salud de sensores (EDR/AV, MDI, conectores de apps) |
| XDR 3.7 | Registro de Métricas Diarias | Diaria | Nueva | GXDR-3.7 | — |
| XDR 3.8 | Hand-over entre Turnos | Diaria | Nueva | GXDR-3.8 | — |
| XDR 4.1 | Revisión Profunda de Incidentes y Threat Hunting | Semanal | Equivalente | XDR-W01 | Hunting proactivo cross-domain y guided hunting para Tier 1 |
| XDR 4.2 | Ajuste de Reglas y Detecciones (Tuning) | Semanal | Equivalente | XDR-W02 | Crear/revisar detecciones personalizadas y automation rules |
| XDR 4.3 | Revisión de Incidentes Cerrados (Post-Incident Review Semanal) | Semanal | Nueva | GXDR-4.3 | — |
| XDR 4.4 | Evaluación de Configuraciones (Configuration Drift) | Semanal | Nueva | GXDR-4.4 | — |
| XDR 4.5 | Revisión de Secure Score | Semanal | Equivalente | XDR-W03 | Revisar Secure Score y Exposure Management; alimentar backlog |
| XDR 4.6 | Revisión de Vulnerability Management | Semanal | Equivalente | EP-W03 | Revisar Defender Vulnerability Management: nuevas vulnerabilidades, recomendaciones, exposure score; solicitudes a Intune |
| XDR 4.7 | Revisión de Cuentas Privilegiadas | Semanal | Equivalente | ID-M02 | Revisar cuentas sensibles, inactivas, admins sin PIM |
| XDR 4.8 | Análisis de Campañas y Tendencias de Email | Semanal | Equivalente | MDO-W04 | Revisar Campaign Views |
| XDR 4.9 | Confirmación de Integraciones SIEM y Flujo de Datos | Semanal | Equivalente | XDR-W06 | Desplegar/probar automatizaciones aprobadas; verificar conectividad SIEM |
| XDR 4.10 | Revisión de SLAs Operativos y Actualización de Runbooks | Semanal | Nueva | GXDR-4.10 | — |
| XDR 5.1 | Revisión Formal de Métricas SOC (SOC Report Mensual) | Mensual | Equivalente | XDR-M04 | Informe mensual de seguridad para el CISO |
| XDR 5.2 | Gestión de la Lista de Permitidos/Bloqueados (Tenant Allow/Block List) | Mensual | Equivalente | MDO-M02 | Revisar overrides de detección |
| XDR 5.3 | Afinamiento de Attack Surface Reduction (ASR) | Mensual | Equivalente | EP-W04 | Revisar ASR rules report y proponer paso de audit a block |
| XDR 5.4 | Afinamiento de Custom Detection Rules | Mensual | Equivalente | XDR-M03 | Revisar alertas tuned/suprimidas y reglas sin coincidencias |
| XDR 5.5 | Revisión de Device Onboarding y Cobertura | Mensual | Equivalente | EP-M03 | Revisar device discovery: no gestionados y de red; plan de onboarding |
| XDR 5.6 | Revisión de RBAC y Segregación de Funciones | Mensual | Equivalente | XDR-M02 | Revisar Unified RBAC: roles, permisos y asignaciones de humanos y agentes |
| XDR 5.7 | Análisis de Exposición y Vulnerabilidades | Mensual | Equivalente | XDR-W03 | Revisar Secure Score y Exposure Management; alimentar backlog |
| XDR 5.8 | Revisión de Automatizaciones (Logic Apps / SOAR) | Mensual | Equivalente | XDR-W06 | Desplegar/probar automatizaciones aprobadas; verificar conectividad SIEM |
| XDR 5.9 | Auditoría de Funcionalidades y ROI Review | Mensual | Nueva | GXDR-5.9 | — |
| XDR 5.10 | Revisión de Configuraciones Específicas de Email | Mensual | Equivalente | MDO-M01 | Revisar configuración con Configuration Analyzer/ORCA |
| XDR 5.11 | Validación de Backups y Recuperación | Mensual | Nueva | GXDR-5.11 | — |
| XDR 5.12 | Revisión de Identidades Afinadas y Exclusiones | Mensual | Equivalente | ID-M01 | Revisar alertas tuned y retirar reglas sin coincidencias |
| XDR 5.13 | Tracking de Cambios en Productos | Mensual | Equivalente | XDR-W05 | Revisar Message Center y novedades; evaluar impacto |
| XDR 6.1 | Revisión de Roles y Responsabilidades (SOC Governance) | Semestral | Nueva | GXDR-6.1 | — |
| XDR 6.2 | Mantenimiento de Runbooks y Playbooks | Semestral | Equivalente | XDR-Q01 | Revisar casos de uso del SOC, playbooks del CSIRT y modelo de amenazas por sensor |
| XDR 6.3 | Evaluación de Cobertura MITRE ATT&CK | Semestral | Equivalente | SI-W03 | Revisar cobertura MITRE de reglas vs. técnicas priorizadas |
| XDR 6.4 | Revisión de Controles de Identidad y Zero Trust | Semestral | Equivalente | ID-M04 | Revisar baseline de CA y excepciones (break-glass) con vencimiento |
| XDR 6.5 | Revisión de Licenciamiento y Feature Register | Semestral | Repetida en otra guía | GXDR-5.9 | Auditoría de Funcionalidades y ROI Review |
| XDR 6.6 | Revisión de Service Health & Domain Configuration | Semestral | Equivalente | ID-Q01 | Revisar service health, setup de sensores y configuración de dominio |
| XDR 6.7 | Revisión de Coordinación con Stakeholders | Semestral | Nueva | GXDR-6.7 | — |
| XDR 7.1 | Revisión Completa del Programa (Full Program Review) | Anual | Nueva | GXDR-7.1 | — |
| XDR 7.2 | Reevaluación Estratégica de Postura (Strategic Posture Reassessment) | Anual | Nueva | GXDR-7.2 | — |
| XDR 7.3 | Ejercicio de Red Team / Purple Team Anual | Anual | Equivalente | XDR-A05 | Tabletop / Purple team cross-domain (incl. 'agente comprometido') |
| XDR 7.4 | Auditoría Externa y Compliance | Anual | Nueva | GXDR-7.4 | — |
| XDR 7.5 | Revisión de Campañas de Phishing Simulation y DLP | Anual | Repetida en otra guía | GMDO-M-5 | Programa de Attack Simulation Training — Análisis y Planificación Mensual |
| XDR 8.1 | Respuesta a Incidentes de Seguridad Mayores | Por evento | Equivalente | XDR-A01 | Responder a incidentes mayores con el CSIRT (aislar, revocar, deshabilitar, contener) |
| XDR 8.2 | Respuesta ante Campañas Activas (Phishing Masivo / Malware Campaign) | Por evento | Repetida en otra guía | GMDO-A-1 | Respuesta a Brote de Phishing/Malware (Outbreak Response) |
| XDR 8.3 | Ante Eventos Regulatorios o Auditoría | Por evento | Repetida en otra guía | GXDR-7.4 | Auditoría Externa y Compliance |
| XDR 8.4 | Threat Hunting Proactivo Específico | Por evento | Equivalente | XDR-W01 | Hunting proactivo cross-domain y guided hunting para Tier 1 |
| XDR 8.5 | Despliegue de Nuevas Funcionalidades | Por evento | Nueva | GXDR-8.5 | — |
| XDR 8.6 | Despliegue de Automation (SOAR) | Por evento | Equivalente | XDR-W06 | Desplegar/probar automatizaciones aprobadas; verificar conectividad SIEM |
| XDR 8.7 | Tabletop Exercises (IR Readiness) | Por evento | Equivalente | XDR-A05 | Tabletop / Purple team cross-domain (incl. 'agente comprometido') |

### Microsoft Defender for Endpoint (MDE): 28 tareas

| Referencia | Tarea de la guía | Cadencia | Relación | Fila del libro | Tarea del libro |
|---|---|:--:|---|:--:|---|
| MDE 3.1 | Revisar el Action Center (AIR) | Diaria | Equivalente | EP-D01 | Revisar acciones automáticas y manuales en el Action center |
| MDE 3.2 | Monitorear Cola de Incidentes | Diaria | Equivalente | EP-D02 | Triar incidentes de la cola con alertas de MDE y resolver remediados |
| MDE 3.3 | Gestionar Falsos Positivos / Falsos Negativos | Diaria | Equivalente | EP-D03 | Gestionar FP/FN: indicadores, exclusiones, envíos; causa (ASR, AV, EDR) |
| MDE 3.4 | Verificar Sensor Health (Silent Failures) | Diaria | Equivalente | EP-D05 | Revisar salud de dispositivos (AV signature/platform/engine, EDR sensor) |
| MDE 3.5 | Validar Políticas ASR y Cobertura de Endpoints | Diaria | Equivalente | EP-W04 | Revisar ASR rules report y proponer paso de audit a block |
| MDE 3.6 | Monitorear Exposure Score (MDVM) | Diaria | Equivalente | EP-W03 | Revisar Defender Vulnerability Management: nuevas vulnerabilidades, recomendaciones, exposure score; solicitudes a Intune |
| MDE 4.1 | Analizar Tendencias de Incidentes | Semanal | Equivalente | EP-W02 | Revisar threat protection report y tendencias |
| MDE 4.2 | Revisar y Actualizar Playbooks de Respuesta | Semanal | Equivalente | XDR-Q01 | Revisar casos de uso del SOC, playbooks del CSIRT y modelo de amenazas por sensor |
| MDE 4.3 | Auditar Permisos RBAC | Semanal | Equivalente | EP-M01 | Revisar device groups, niveles de automatización y RBAC por grupo |
| MDE 4.4 | Análisis de Vulnerabilidades con Exploits Activos | Semanal | Equivalente | EP-W03 | Revisar Defender Vulnerability Management: nuevas vulnerabilidades, recomendaciones, exposure score; solicitudes a Intune |
| MDE 4.5 | Revisar Exclusiones de Antivirus | Semanal | Equivalente | EP-M05 | Revisar indicadores y exclusiones con vencimiento; retirar obsoletos |
| MDE 4.6 | Auditar Onboarding/Offboarding de Dispositivos | Semanal | Equivalente | EP-M03 | Revisar device discovery: no gestionados y de red; plan de onboarding |
| MDE 5.1 | Revisar Security Posture (Secure Score) | Mensual | Equivalente | XDR-W03 | Revisar Secure Score y Exposure Management; alimentar backlog |
| MDE 5.2 | Reportes Disponibles en MDE | Mensual | Equivalente | EP-M04 | Informe mensual de seguridad de endpoints |
| MDE 5.3 | Vulnerability Assessment Completo (MDVM) | Mensual | Equivalente | EP-W03 | Revisar Defender Vulnerability Management: nuevas vulnerabilidades, recomendaciones, exposure score; solicitudes a Intune |
| MDE 5.4 | Prueba End-to-End del Pipeline de Detección | Mensual | Nueva | GMDE-5.4 | — |
| MDE 5.5 | Ejercicios Tabletop de Incident Response | Mensual | Equivalente | EP-A05 | Tabletop ransomware/dispositivo comprometido (incl. 'agente comprometido') |
| MDE 6.1 | Responder a Incidentes Mayores — Live Response | Por evento | Equivalente | EP-A02 | Live response / recolección de paquetes |
| MDE 6.2 | Investigation Package — Contenido por Plataforma | Por evento | Equivalente | EP-A02 | Live response / recolección de paquetes |
| MDE 6.3 | Respuesta a Incidentes — Acciones de Respuesta en Dispositivos | Por evento | Equivalente | EP-A01 | Respuesta a incidente mayor: aislamiento masivo acotado, restricción, offboarding |
| MDE 6.4 | Bloqueo de Indicadores de Compromiso (IoC) | Por evento | Equivalente | EP-W05 | Revisar web protection / network protection y custom indicators |
| MDE 6.5 | Coordinar con Microsoft Threat Experts | Por evento | Nueva | GMDE-6.5 | — |
| MDE 7.1 | Revisión Completa de RBAC | Semestral | Equivalente | EP-Q03 | Recertificar accesos (Unified RBAC por device group; Agent ID) |
| MDE 7.2 | Detection Engineering Refresh | Semestral | Equivalente | XDR-Q01 | Revisar casos de uso del SOC, playbooks del CSIRT y modelo de amenazas por sensor |
| MDE 7.3 | Revisión Estratégica de Attack Surface Reduction | Semestral | Equivalente | EP-Q01 | Revisar política de endpoints, excepciones y apetito de autonomía |
| MDE 8.1 | Métricas Anuales de Desempeño del Programa | Anual | Nueva | GMDE-8.1 | — |
| MDE 8.2 | Entregables Anuales | Anual | Repetida en otra guía | GMDE-8.1 | Métricas Anuales de Desempeño del Programa |
| MDE 8.3 | Ejercicio Anual IR — Full Scale | Anual | Equivalente | EP-A05 | Tabletop ransomware/dispositivo comprometido (incl. 'agente comprometido') |

### Microsoft Intune (INT): 13 tareas

| Referencia | Tarea de la guía | Cadencia | Relación | Fila del libro | Tarea del libro |
|---|---|:--:|---|:--:|---|
| INT 1.1 | Supervisar el cumplimiento de los dispositivos y el estado de las líneas base de seguridad | Diaria | Nueva | GINT-1.1 | — |
| INT 1.2 | Revisar Endpoint analytics para identificar riesgos en dispositivos Windows | Diaria | Nueva | GINT-1.2 | — |
| INT 1.3 | Supervisar la inscripción automática de dispositivos y sus notificaciones | Diaria | Nueva | GINT-1.3 | — |
| INT 1.4 | Revisar alertas y amenazas con Defender for Endpoint | Diaria | Equivalente | EP-D02 | Triar incidentes de la cola con alertas de MDE y resolver remediados |
| INT 2.1 | Auditar las asignaciones de las líneas base de seguridad | Semanal | Equivalente | EP-M02 | Revisar baselines de Intune y su deriva |
| INT 2.2 | Detectar dispositivos inactivos y aplicar reglas de limpieza | Semanal | Nueva | GINT-2.2 | — |
| INT 2.3 | Actualizar las versiones de las líneas base de seguridad | Semanal | Equivalente | EP-M02 | Revisar baselines de Intune y su deriva |
| INT 3.1 | Revisar el cumplimiento y la eficacia de las directivas | Mensual | Repetida en otra guía | GINT-1.1 | Supervisar el cumplimiento de los dispositivos y el estado de las líneas base de seguridad |
| INT 3.2 | Evaluar y ajustar las líneas base de seguridad | Mensual | Equivalente | EP-M02 | Revisar baselines de Intune y su deriva |
| INT 3.3 | Verificar el uso de las funciones de seguridad: firewall, BitLocker y reducción de la superficie de ataque | Mensual | Nueva | GINT-3.3 | — |
| INT 4.1 | Responder a incidentes de seguridad | Por evento | Equivalente | EP-A01 | Respuesta a incidente mayor: aislamiento masivo acotado, restricción, offboarding |
| INT 4.2 | Actualizar términos y condiciones o directivas de acceso | Por evento | Nueva | GINT-4.2 | — |
| INT 4.3 | Probar en piloto las nuevas líneas base de seguridad | Por evento | Equivalente | EP-M02 | Revisar baselines de Intune y su deriva |

### Microsoft Defender for Identity (MDI): 24 tareas

| Referencia | Tarea de la guía | Cadencia | Relación | Fila del libro | Tarea del libro |
|---|---|:--:|---|:--:|---|
| MDI D1 | Revisión del Dashboard ITDR | Diaria | Equivalente | ID-D01 | Revisar el Identity Security dashboard |
| MDI D2 | Triaje de Incidentes por Prioridad | Diaria | Equivalente | ID-D02 | Triar incidentes de identidad por prioridad y resolver remediados |
| MDI D3 | Investigación de Incidentes y Alertas | Diaria | Equivalente | ID-D02 | Triar incidentes de identidad por prioridad y resolver remediados |
| MDI D4 | Respuesta sobre Identidades | Diaria | Equivalente | ID-A01 | Respuesta a compromiso de identidad: revocar, reset, deshabilitar, bloquear por CA |
| MDI D5 | Revisión de Health Issues de Sensores | Diaria | Equivalente | ID-D05 | Revisar salud de sensores MDI |
| MDI D6 | Threat Hunting Diario (KQL) | Diaria | Equivalente | ID-D06 | Hunting proactivo sobre identidad |
| MDI W1 | Alert Tuning y Reducción de Ruido | Semanal | Equivalente | ID-D04 | Configurar reglas de tuning para benign true positives de MDI |
| MDI W2 | Secure Score Semanal | Semanal | Equivalente | ID-W01 | Revisar Secure Score y posture assessments; alimentar backlog |
| MDI W3 | Threat Hunting Proactivo (KQL Semanales) | Semanal | Equivalente | ID-D06 | Hunting proactivo sobre identidad |
| MDI W4 | Análisis de Lateral Movement Paths (LMP) | Semanal | Nueva | GMDI-W4 | — |
| MDI W5 | Auditoría de Protocolos Inseguros | Semanal | Nueva | GMDI-W5 | — |
| MDI M1 | Evaluación de Postura — Identity Secure Score | Mensual | Equivalente | ID-W01 | Revisar Secure Score y posture assessments; alimentar backlog |
| MDI M2 | Revisión de Alertas Tuneadas | Mensual | Equivalente | ID-M01 | Revisar alertas tuned y retirar reglas sin coincidencias |
| MDI M3 | Revisión de Identities Security Initiative | Mensual | Equivalente | XDR-W03 | Revisar Secure Score y Exposure Management; alimentar backlog |
| MDI M4 | Auditoría de Inventario de Identidades | Mensual | Equivalente | ID-M02 | Revisar cuentas sensibles, inactivas, admins sin PIM |
| MDI M5 | Seguimiento de Cambios en la Plataforma | Mensual | Equivalente | ID-W05 | Revisar Message Center y novedades |
| MDI M6 | Generación de Reportes Ejecutivos | Mensual | Equivalente | ID-M03 | Informe mensual de identidad para el CISO |
| MDI Q1 | Revisión de Service Health | Trimestral | Equivalente | ID-Q01 | Revisar service health, setup de sensores y configuración de dominio |
| MDI Q2 | Validación de Configuración del Dominio | Trimestral | Equivalente | ID-Q01 | Revisar service health, setup de sensores y configuración de dominio |
| MDI Q3 | Proceso de Servidor — Onboarding de Nuevos DCs | Por evento | Nueva | GMDI-Q3 | — |
| MDI Q4 | Tareas Ad-Hoc ante Incidentes Activos | Por evento | Equivalente | ID-A01 | Respuesta a compromiso de identidad: revocar, reset, deshabilitar, bloquear por CA |
| MDI 8.1 | Tabletop Exercises: Compromiso de Cuenta Privilegiada y Movimiento Lateral / Pre-Ransomware | Semestral | Equivalente | ID-A04 | Tabletop de compromiso de identidad privilegiada (incl. 'agente comprometido') |
| MDI 8.2a | Capacity Planning de Sensores | Anual | Nueva | GMDI-8.2a | — |
| MDI 8.2b | Purple Team — Validación de Detección | Anual | Nueva | GMDI-8.2b | — |

### Microsoft Entra (ENT): 44 tareas

| Referencia | Tarea de la guía | Cadencia | Relación | Fila del libro | Tarea del libro |
|---|---|:--:|---|:--:|---|
| ENT 2.1 | Revisión y Triage de Incidentes Activos | Diaria | Equivalente | XDR-D01 | Triar la cola de incidentes unificada (todas las fuentes; High/Medium primero) |
| ENT 2.2 | Análisis de Alertas Críticas de Microsoft Defender XDR | Diaria | Equivalente | XDR-D02 | Investigar incidentes correlacionados y ejecutar/aprobar acciones de respuesta |
| ENT 2.3 | Validación de Alertas de Identidad (Entra ID Protection) | Diaria | Equivalente | ID-D03 | Investigar risky users / sign-ins; confirmar o descartar; remediar o dejar que CA auto-remedie |
| ENT 2.4 | Ejecución y Verificación de Playbooks Automáticos (Logic Apps / SOAR) | Diaria | Equivalente | SI-D05 | Verificar ejecución de playbooks y automation rules |
| ENT 2.5 | Revisión de Alertas de Malware / Ransomware | Diaria | Equivalente | EP-D02 | Triar incidentes de la cola con alertas de MDE y resolver remediados |
| ENT 2.6 | Validación de Salud de Conectores de Datos en Sentinel | Diaria | Equivalente | SI-D02 | Revisar salud de conectores y agentes AMA |
| ENT 2.7 | Monitoreo de Actividades Privilegiadas (PIM / Entra) | Diaria | Nueva | GENT-2.7 | — |
| ENT 2.8 | Revisión de Alertas de Exfiltración / Actividad Anómala | Diaria | Equivalente | DP-D01 | Triar alertas DLP (High/Medium) e Insider Risk correlacionadas; clasificar y resolver |
| ENT 2.9 | Actualización del Estado de Incidentes y Tickets | Diaria | Equivalente | XDR-D08 | Actualizar tickets de escalamiento (ITSM) y notificaciones |
| ENT 2.10 | Revisión de Alertas No Atendidas (Alert Backlog) | Diaria | Equivalente | XDR-D01 | Triar la cola de incidentes unificada (todas las fuentes; High/Medium primero) |
| ENT 3.1 | Threat Hunting Proactivo | Semanal | Equivalente | XDR-W01 | Hunting proactivo cross-domain y guided hunting para Tier 1 |
| ENT 3.2 | Revisión de Reglas Analíticas y Tuning de Alertas | Semanal | Repetida en otra guía | GSEN-4.2 | Revisión y Tuning de Reglas Analíticas |
| ENT 3.3 | Análisis de Tendencias de Incidentes | Semanal | Equivalente | XDR-W04 | Revisar informes de amenazas y protección |
| ENT 3.4 | Validación de Cobertura MITRE ATT&CK | Semanal | Equivalente | SI-W03 | Revisar cobertura MITRE de reglas vs. técnicas priorizadas |
| ENT 3.5 | Revisión de Cuentas Comprometidas o de Alto Riesgo | Semanal | Equivalente | ID-D03 | Investigar risky users / sign-ins; confirmar o descartar; remediar o dejar que CA auto-remedie |
| ENT 3.6 | Pruebas de Playbooks y Runbooks | Semanal | Equivalente | SI-Q04 | Evaluaciones/regresión de agentes y pruebas de playbooks en escenarios de falla |
| ENT 3.7 | Revisión de Cambios en el Entorno (Change Management) | Semanal | Nueva | GENT-3.7 | — |
| ENT 3.8 | Optimización de Costos y Uso de Datos en Sentinel | Semanal | Equivalente | SI-W04 | Revisar ingesta y costo vs. commitment tier |
| ENT 3.9 | Revisión de Indicadores de Compromiso (IoC) | Semanal | Equivalente | SI-W06 | Revisar ingesta de TI y reglas de matching |
| ENT 3.10 | Reporte Operativo Semanal del SOC | Semanal | Repetida en otra guía | GSEN-4.8 | Reporte Semanal a Stakeholders |
| ENT 4.1 | Revisión Formal de Postura de Seguridad | Mensual | Equivalente | XDR-W03 | Revisar Secure Score y Exposure Management; alimentar backlog |
| ENT 4.2 | Actualización de Runbooks y Procedimientos | Mensual | Equivalente | XDR-Q01 | Revisar casos de uso del SOC, playbooks del CSIRT y modelo de amenazas por sensor |
| ENT 4.3 | Evaluación de Efectividad de Controles de Detección | Mensual | Equivalente | XDR-M03 | Revisar alertas tuned/suprimidas y reglas sin coincidencias |
| ENT 4.4 | Revisión de Accesos Privilegiados (con IAM) | Mensual | Equivalente | ID-M02 | Revisar cuentas sensibles, inactivas, admins sin PIM |
| ENT 4.5 | Simulacros de Respuesta a Incidentes (Tabletop Exercises) | Mensual | Equivalente | XDR-A05 | Tabletop / Purple team cross-domain (incl. 'agente comprometido') |
| ENT 4.6 | Revisión de Cumplimiento (NIST CSF / ISO 27001) | Mensual | Equivalente | DP-M05 | Revisar Compliance Manager: acciones de mejora y evidencias |
| ENT 4.7 | Optimización de Arquitectura de Sentinel | Mensual | Repetida en otra guía | GSEN-5.9 | Revisión de Arquitectura SOC |
| ENT 4.8 | Revisión de Integraciones y Conectores | Mensual | Equivalente | SI-D02 | Revisar salud de conectores y agentes AMA |
| ENT 4.9 | Reporte Ejecutivo Mensual (CISO / Dirección) | Mensual | Equivalente | XDR-M04 | Informe mensual de seguridad para el CISO |
| ENT 4.10 | Plan de Mejora Continua del SOC | Mensual | Repetida en otra guía | GSEN-5.10 | Roadmap de Mejoras del SOC |
| ENT 5.1 | Investigación Profunda de Incidentes Críticos | Por evento | Equivalente | XDR-A01 | Responder a incidentes mayores con el CSIRT (aislar, revocar, deshabilitar, contener) |
| ENT 5.2 | Contención y Erradicación de Amenazas Avanzadas | Por evento | Equivalente | XDR-A01 | Responder a incidentes mayores con el CSIRT (aislar, revocar, deshabilitar, contener) |
| ENT 5.3 | Respuesta a Cuenta Comprometida (IR Playbook) | Por evento | Equivalente | ID-A01 | Respuesta a compromiso de identidad: revocar, reset, deshabilitar, bloquear por CA |
| ENT 5.4 | Offboarding de Emergencia (Lifecycle Workflows) | Por evento | Nueva | GENT-5.4 | — |
| ENT 5.5 | Análisis Forense (Endpoint / Identidad / Cloud) | Por evento | Equivalente | XDR-A02 | Live response / recolección de paquetes de investigación |
| ENT 5.6 | Activación del IR Plan / DR Plan | Por evento | Equivalente | XDR-A01 | Responder a incidentes mayores con el CSIRT (aislar, revocar, deshabilitar, contener) |
| ENT 6.1 | Gestión del Ciclo de Vida de Identidades | Diaria | Nueva | GENT-6.1 | — |
| ENT 6.1.1 | Creación de Usuarios Cloud | — | No es una tarea | — | Paso de la tarea 6.1 |
| ENT 6.1.2 | Asignación de Roles con Mínimo Privilegio | — | No es una tarea | — | Paso de la tarea 6.1 |
| ENT 6.1.3 | Soft Delete y Recuperación de Cuentas | — | No es una tarea | — | Paso de la tarea 6.1 |
| ENT 6.2 | Análisis Avanzado de Sign-in Logs | Diaria | Equivalente | ID-D03 | Investigar risky users / sign-ins; confirmar o descartar; remediar o dejar que CA auto-remedie |
| ENT 6.3 | Gestión de Conditional Access | Semanal | Equivalente | ID-W03 | Revisar efectos de Conditional Access (report-only) y proponer ajustes |
| ENT 6.4 | Privileged Identity Management – Operaciones Detalladas (Weekly/Monthly) | — | No es una tarea | — | Encabezado de sección |
| ENT 6.4.1 | Revisión Semanal de Assignments | Semanal | Equivalente | ID-M02 | Revisar cuentas sensibles, inactivas, admins sin PIM |
| ENT 6.4.2 | Análisis del Resource Audit (Activaciones) | Semanal | Repetida en otra guía | GENT-2.7 | Monitoreo de Actividades Privilegiadas (PIM / Entra) |
| ENT 6.4.3 | Configuración de Alertas PIM | Mensual | Repetida en otra guía | GENT-2.7 | Monitoreo de Actividades Privilegiadas (PIM / Entra) |
| ENT 6.5 | Access Reviews – Identity Governance (Weekly/Monthly) | — | No es una tarea | — | Encabezado de sección |
| ENT 6.5.1 | Monitoreo de Reviews Activos | Semanal | Equivalente | ID-Q03 | Recertificación de accesos (humanos, grupos privilegiados, agentes) |
| ENT 6.5.2 | Tipos de Access Reviews Recomendados | — | No es una tarea | — | Material de referencia |
| ENT 7.2 | Verificación de Apps y SSO | Mensual | Nueva | GENT-7.2 | — |

### Microsoft Purview Information Protection (MIP): 35 tareas

| Referencia | Tarea de la guía | Cadencia | Relación | Fila del libro | Tarea del libro |
|---|---|:--:|---|:--:|---|
| MIP D-01 | Revisión de Alertas de Microsoft Purview | Diaria | Equivalente | DP-D01 | Triar alertas DLP (High/Medium) e Insider Risk correlacionadas; clasificar y resolver |
| MIP D-02 | Monitoreo del M365 Unified Audit Log — Eventos de Information Protection | Diaria | Equivalente | DP-W04 | Hunting sobre CloudAppEvents / EmailEvents: egress, descargas masivas, etiquetas degradadas |
| MIP D-03 | Correlación de Eventos de Purview en Microsoft Sentinel | Diaria | Equivalente | DP-D01 | Triar alertas DLP (High/Medium) e Insider Risk correlacionadas; clasificar y resolver |
| MIP D-04 | Validación de Accesos a Contenido Cifrado (Azure Rights Management) | Diaria | Nueva | GMIP-D-04 | — |
| MIP D-05 | Revisión de Eventos de Oversharing (Teams / SharePoint) | Diaria | Equivalente | DP-W03 | Revisar sobrecompartición: 'Anyone', externos, sitios sensibles |
| MIP D-06 | Seguimiento de Incidentes Abiertos Relacionados con Datos | Diaria | Equivalente | DP-D02 | Investigar alertas DLP (Activity/Content explorer); decidir acción |
| MIP D-07 | Verificación de Integridad de Conectores (Purview → Sentinel) | Diaria | Equivalente | SI-D02 | Revisar salud de conectores y agentes AMA |
| MIP D-08 | Validación de Cambios Administrativos del Día Anterior | Diaria | Nueva | GMIP-D-08 | — |
| MIP D-09 | Revisión de Accesos Fallidos a Contenido Protegido | Diaria | Repetida en otra guía | GMIP-D-04 | Validación de Accesos a Contenido Cifrado (Azure Rights Management) |
| MIP D-10 | Actualización del Tablero Operativo del SOC | Diaria | Repetida en otra guía | GXDR-3.7 | Registro de Métricas Diarias |
| MIP S-01 | Revisión y Tuning de Falsos Positivos en Alertas de Purview | Semanal | Equivalente | DP-D03 | Gestionar FP DLP: coincidencias de SIT, umbrales, excepciones con vencimiento; simulación antes de bloquear |
| MIP S-02 | Análisis de Tendencias de Clasificación de Datos | Semanal | Equivalente | DP-W02 | Revisar cobertura de etiquetado y tendencia |
| MIP S-03 | Validación de Políticas de Auto-Labeling (Simulación vs. Producción) | Semanal | Equivalente | DP-W01 | Revisar simulación de auto-etiquetado y DLP en prueba; proponer producción |
| MIP S-04 | Revisión de Eventos de Revocación de Acceso | Semanal | Repetida en otra guía | GMIP-D-04 | Validación de Accesos a Contenido Cifrado (Azure Rights Management) |
| MIP S-05 | Pruebas de Acceso Controlado a Datos Altamente Sensibles | Semanal | Nueva | GMIP-S-05 | — |
| MIP S-06 | Revisión de Incidentes Cerrados y Lecciones Aprendidas | Semanal | Repetida en otra guía | GXDR-4.3 | Revisión de Incidentes Cerrados (Post-Incident Review Semanal) |
| MIP S-07 | Ajuste de Reglas de Correlación en Microsoft Sentinel | Semanal | Repetida en otra guía | GSEN-4.2 | Revisión y Tuning de Reglas Analíticas |
| MIP S-08 | Validación de Cobertura de Logging de Purview | Semanal | Nueva | GMIP-S-08 | — |
| MIP S-09 | Revisión de Cuentas Privilegiadas con Acceso a Datos Protegidos | Semanal | Equivalente | DP-Q03 | Recertificar roles de Purview y permisos de agentes |
| MIP S-10 | Reporte Semanal de Postura de Seguridad de Datos | Semanal | Nueva | GMIP-S-10 | — |
| MIP M-01 | Revisión Integral de la Taxonomía de Sensitivity Labels | Mensual | Equivalente | DP-M01 | Revisar taxonomía de etiquetas y políticas de publicación con dueños de negocio |
| MIP M-02 | Evaluación de Efectividad del Cifrado Persistente | Mensual | Nueva | GMIP-M-02 | — |
| MIP M-03 | Auditoría Formal de Cambios Administrativos del Mes | Mensual | Repetida en otra guía | GMIP-D-08 | Validación de Cambios Administrativos del Día Anterior |
| MIP M-04 | Revisión de Métricas MTTA y MTTR para Incidentes de Datos | Mensual | Equivalente | DP-M04 | Informe mensual de protección de datos para CISO y CDO |
| MIP M-05 | Ejercicio de Tabletop: Incidente de Fuga de Datos | Mensual | Equivalente | DP-A04 | Tabletop de fuga de datos / insider (incl. 'agente filtra datos') |
| MIP M-06 | Revisión de Cobertura del Information Protection Scanner | Mensual | Equivalente | DP-D05 | Revisar salud de la clasificación: auto-labeling, scanner, conectores MDA |
| MIP M-07 | Optimización de Costos de Logging y Retención | Mensual | Equivalente | SI-M02 | Revisar retención y almacenamiento a largo plazo |
| MIP M-08 | Validación de Integración Purview–Sentinel–Defender | Mensual | Equivalente | XDR-W06 | Desplegar/probar automatizaciones aprobadas; verificar conectividad SIEM |
| MIP M-09 | Reporte Ejecutivo Mensual de Riesgo de Datos | Mensual | Equivalente | DP-M04 | Informe mensual de protección de datos para CISO y CDO |
| MIP M-10 | Revisión de Cumplimiento con NIST CSF 2.0 | Mensual | Equivalente | DP-M05 | Revisar Compliance Manager: acciones de mejora y evidencias |
| MIP AH-A | Investigación de Alerta Crítica de Purview | Por evento | Equivalente | DP-A01 | Respuesta a fuga de datos: alcance, quitar compartición, cuarentena, revocar, notificar (Legal) |
| MIP AH-B | Contención Inmediata — Revocación de Acceso y Bloqueo de Cuenta | Por evento | Equivalente | DP-A01 | Respuesta a fuga de datos: alcance, quitar compartición, cuarentena, revocar, notificar (Legal) |
| MIP AH-C | Análisis Forense de Actividades de Datos | Por evento | Equivalente | DP-A01 | Respuesta a fuga de datos: alcance, quitar compartición, cuarentena, revocar, notificar (Legal) |
| MIP AH-D | Escalamiento Legal y Compliance | Por evento | Equivalente | DP-A01 | Respuesta a fuga de datos: alcance, quitar compartición, cuarentena, revocar, notificar (Legal) |
| MIP AH-E | Comunicación Ejecutiva y Post-Mortem | Por evento | Equivalente | DP-A01 | Respuesta a fuga de datos: alcance, quitar compartición, cuarentena, revocar, notificar (Legal) |

### Microsoft Purview Data Loss Prevention (DLP): 22 tareas

| Referencia | Tarea de la guía | Cadencia | Relación | Fila del libro | Tarea del libro |
|---|---|:--:|---|:--:|---|
| DLP 8.1-1 | Triage del DLP Alerts Dashboard: priorizar alertas de alta severidad y usuarios VIP | Diaria | Equivalente | DP-D01 | Triar alertas DLP (High/Medium) e Insider Risk correlacionadas; clasificar y resolver |
| DLP 8.1-2 | Clasificar cada alerta: (a) falso positivo → retroalimentar proceso de optimización; (b) actividad legítima con override documentado → revisar justificación; (c) actividad sospechosa → escalar a Tier 2 / IRM | Diaria | Equivalente | DP-D02 | Investigar alertas DLP (Activity/Content explorer); decidir acción |
| DLP 8.1-3 | Verificar salud de sensores Endpoint DLP: cobertura del agente MDE y sincronización de políticas (~1 hora desde cambio) | Diaria | Nueva | GDLP-8.1-3 | — |
| DLP 8.2-1 | Análisis de Activity Explorer para detectar patrones no capturados por alertas | Semanal | Equivalente | DP-W04 | Hunting sobre CloudAppEvents / EmailEvents: egress, descargas masivas, etiquetas degradadas |
| DLP 8.2-2 | Revisión de justificaciones de override: identificar patrones de evasión (justificaciones genéricas repetidas) | Semanal | Equivalente | DP-M02 | Revisar excepciones DLP y overrides de usuario con vencimiento |
| DLP 8.2-3 | Revisión de incidentes DLP abiertos y tiempo de resolución | Semanal | Equivalente | DP-D02 | Investigar alertas DLP (Activity/Content explorer); decidir acción |
| DLP 8.2-4 | Actualización de listas de dominios de confianza y excepciones de grupos | Semanal | Equivalente | DP-M02 | Revisar excepciones DLP y overrides de usuario con vencimiento |
| DLP 8.3-1 | KPI pack: volumen de alertas por política, tasa de FP, MTTR, volumen de overrides por área | Mensual | Equivalente | DP-M04 | Informe mensual de protección de datos para CISO y CDO |
| DLP 8.3-2 | Actualización de datasets EDM si la fuente de datos cambió | Mensual | Nueva | GDLP-8.3-2 | — |
| DLP 8.3-3 | Revisión de cobertura Endpoint DLP (% de dispositivos gestionados con agente activo) | Mensual | Repetida en otra guía | GDLP-8.1-3 | Verificar salud de sensores Endpoint DLP: cobertura del agente MDE y sincronización de políticas (~1 hora desde cambio) |
| DLP 8.3-4 | Sincronización con equipo de IRM: correlación de señales DLP con perfiles de riesgo interno | Mensual | Equivalente | DP-M03 | Revisar políticas de Insider Risk con Privacidad/Legal; casos abiertos |
| DLP 8.3-5 | Revisión del estado de clasificadores entrenables: verificar que la precisión no haya degradado por cambios en el corpus documental | Mensual | Nueva | GDLP-8.3-5 | — |
| DLP 8.4-1 | Revisión formal de todas las políticas DLP: alineación con apetito de riesgo, nuevos casos de uso, retiro de políticas obsoletas | Trimestral | Equivalente | DP-Q01 | Revisar política de protección de datos, apetito y mapa de datos sensibles |
| DLP 8.4-2 | Re-certificación de excepciones documentadas (grupos excluidos, dominios de confianza) | Trimestral | Equivalente | DP-M02 | Revisar excepciones DLP y overrides de usuario con vencimiento |
| DLP 8.4-3 | Ejercicio de prueba: generar deliberadamente un evento que debería ser bloqueado y verificar que la política actúa correctamente | Trimestral | Equivalente | DP-Q04 | Evaluaciones/regresión y red teaming (fuga de datos en salidas, evasión de DLP) |
| DLP 8.4-4 | Presentación de KPIs al CISO/Board | Trimestral | Equivalente | DP-M04 | Informe mensual de protección de datos para CISO y CDO |
| DLP 8.4-5 | Revisión de la arquitectura frente a nuevas regulaciones o cambios en el modelo de negocio | Trimestral | Equivalente | DP-Q01 | Revisar política de protección de datos, apetito y mapa de datos sensibles |
| DLP 8.5-1 | Revisión estratégica del programa: alcance de cobertura vs. riesgo residual aceptado | Anual | Nueva | GDLP-8.5-1 | — |
| DLP 8.5-2 | Simulación de respuesta a incidente de exfiltración masiva (tabletop exercise) | Anual | Equivalente | DP-A04 | Tabletop de fuga de datos / insider (incl. 'agente filtra datos') |
| DLP 8.5-3 | Auditoría independiente de registros y evidencias para cumplimiento regulatorio | Anual | Repetida en otra guía | GXDR-7.4 | Auditoría Externa y Compliance |
| DLP 8.5-4 | Capacitación de analistas en nuevas capacidades de la plataforma | Anual | Equivalente | XDR-M05 | Actualizar entrenamiento del SOC con lecciones; ejercicios Blue/Red/Purple |
| DLP 8.5-5 | Revisión del roadmap Microsoft Purview para planificar adopción de nuevas funciones | Anual | Equivalente | DP-W05 | Revisar Message Center y novedades de Purview |

### Microsoft Sentinel (SEN): 27 tareas

| Referencia | Tarea de la guía | Cadencia | Relación | Fila del libro | Tarea del libro |
|---|---|:--:|---|:--:|---|
| SEN 3.1 | Revisión y Triage de Incidentes Nuevos | Diaria | Equivalente | SI-D01 | Triar e investigar incidentes de Sentinel en el portal unificado |
| SEN 3.2 | Validación de Alertas Automáticas y Gestión de Estado | Diaria | Equivalente | SI-D01 | Triar e investigar incidentes de Sentinel en el portal unificado |
| SEN 3.3 | Ejecución y Verificación de Playbooks Automáticos | Diaria | Equivalente | SI-D05 | Verificar ejecución de playbooks y automation rules |
| SEN 3.4 | Revisión y Habilitación de Analytics Rules | Diaria | Equivalente | SI-D03 | Revisar/habilitar reglas analíticas nuevas; monitorear salud de reglas |
| SEN 3.5 | Monitoreo de Salud de Conectores de Datos | Diaria | Equivalente | SI-D02 | Revisar salud de conectores y agentes AMA |
| SEN 3.6 | Verificación de Conexiones del Azure Monitor Agent (AMA) | Diaria | Equivalente | SI-D02 | Revisar salud de conectores y agentes AMA |
| SEN 3.7 | Revisión de Threat Intelligence Matches | Diaria | Equivalente | SI-W06 | Revisar ingesta de TI y reglas de matching |
| SEN 3.8 | Registro de Actividades del Turno y Hand-off | Diaria | Repetida en otra guía | GXDR-3.8 | Hand-over entre Turnos |
| SEN 4.1 | Análisis de Tendencias de Incidentes | Semanal | Equivalente | XDR-W04 | Revisar informes de amenazas y protección |
| SEN 4.2 | Revisión y Tuning de Reglas Analíticas | Semanal | Nueva | GSEN-4.2 | — |
| SEN 4.3 | Revisión y Actualización de Contenido (Content Hub) | Semanal | Equivalente | SI-W01 | Revisar Content hub (soluciones, reglas, workbooks, playbooks) |
| SEN 4.4 | Threat Hunting Programado | Semanal | Equivalente | SI-D04 | Explorar hunting queries y bookmarks |
| SEN 4.5 | Revisión de Cobertura de Datos | Semanal | Equivalente | SI-W05 | Revisar recomendaciones de SOC optimization |
| SEN 4.6 | Validación de Automation Rules | Semanal | Equivalente | SI-D05 | Verificar ejecución de playbooks y automation rules |
| SEN 4.7 | Revisión de Lecciones Aprendidas (Post-Incident) | Semanal | Repetida en otra guía | GXDR-4.3 | Revisión de Incidentes Cerrados (Post-Incident Review Semanal) |
| SEN 4.8 | Reporte Semanal a Stakeholders | Semanal | Nueva | GSEN-4.8 | — |
| SEN 5.1 | Revisión Ejecutiva de KPIs del SOC | Mensual | Equivalente | SI-M05 | Informe mensual del SOC (eficiencia) para el CISO |
| SEN 5.2 | Revisión de SOC Optimization | Mensual | Equivalente | SI-W05 | Revisar recomendaciones de SOC optimization |
| SEN 5.3 | Evaluación de Cobertura MITRE ATT&CK | Mensual | Equivalente | SI-W03 | Revisar cobertura MITRE de reglas vs. técnicas priorizadas |
| SEN 5.4 | Auditoría de Accesos y Roles SOC | Mensual | Equivalente | SI-M01 | Revisar accesos a Sentinel y Log Analytics; inactivos |
| SEN 5.5 | Pruebas de Playbooks Críticos | Mensual | Equivalente | SI-Q04 | Evaluaciones/regresión de agentes y pruebas de playbooks en escenarios de falla |
| SEN 5.6 | Revisión de Retención y Costos | Mensual | Equivalente | SI-M02 | Revisar retención y almacenamiento a largo plazo |
| SEN 5.7 | Actualización de Runbooks Operativos | Mensual | Equivalente | XDR-Q01 | Revisar casos de uso del SOC, playbooks del CSIRT y modelo de amenazas por sensor |
| SEN 5.8 | Evaluación de Cumplimiento (CSF / ISO / Regulatorio) | Mensual | Equivalente | DP-M05 | Revisar Compliance Manager: acciones de mejora y evidencias |
| SEN 5.9 | Revisión de Arquitectura SOC | Mensual | Nueva | GSEN-5.9 | — |
| SEN 5.10 | Roadmap de Mejoras del SOC | Mensual | Nueva | GSEN-5.10 | — |
| SEN 6 | Respuesta ad-hoc: análisis de entidades, escalamiento según runbook, playbooks manuales, preservación de evidencia y reporte posincidente | Por evento | Equivalente | XDR-A01 | Responder a incidentes mayores con el CSIRT (aislar, revocar, deshabilitar, contener) |

### Microsoft Purview Insider Risk Management (IRM): 28 tareas

| Referencia | Tarea de la guía | Cadencia | Relación | Fila del libro | Tarea del libro |
|---|---|:--:|---|:--:|---|
| IRM D-01 | Verificación de salud de conectores de señales (HR Data, Physical Badging y endpoints) | Diaria | Nueva | GIRM-D-01 | — |
| IRM D-02 | Triaje priorizado de alertas High Severity y vista del Purview Alert Triage Agent | Diaria | Equivalente | DP-D01 | Triar alertas DLP (High/Medium) e Insider Risk correlacionadas; clasificar y resolver |
| IRM D-03 | Análisis contextual de secuencias y exfiltración acumulada en Activity Explorer | Diaria | Nueva | GIRM-D-03 | — |
| IRM D-04 | Monitoreo diario de alertas de Risky AI Usage y Risky Agents (Preview) | Diaria | Nueva | GIRM-D-04 | — |
| IRM D-05 | Correlación diaria en cola unificada de incidentes de Microsoft Defender XDR | Diaria | Equivalente | DP-D01 | Triar alertas DLP (High/Medium) e Insider Risk correlacionadas; clasificar y resolver |
| IRM D-06 | Supervisión operativa de usuarios en nivel Elevated bajo Adaptive Protection | Diaria | Nueva | GIRM-D-06 | — |
| IRM D-07 | Verificación diaria de seudonimización e inspección del Insider Risk Audit Log independiente | Diaria | Nueva | GIRM-D-07 | — |
| IRM D-08 | Evaluación independiente de solicitudes de doble autorización en Forensic Evidence | Diaria | Nueva | GIRM-D-08 | — |
| IRM S-01 | Gestión de casos activos, cadena de custodia en Case Notes e inspección en Content Explorer | Semanal | Nueva | GIRM-S-01 | — |
| IRM S-02 | Chequeo semanal de salud de políticas (Policy Health Check) y advertencias pendientes | Semanal | Nueva | GIRM-S-02 | — |
| IRM S-03 | Calibración de umbrales (Tuning), variantes de indicadores y Detection Groups | Semanal | Nueva | GIRM-S-03 | — |
| IRM S-04 | Caza proactiva semanal KQL en Microsoft Defender Portal sobre seguridad de datos | Semanal | Equivalente | DP-W04 | Hunting sobre CloudAppEvents / EmailEvents: egress, descargas masivas, etiquetas degradadas |
| IRM S-05 | Actualización de Priority User Groups y alineación con Information Barriers | Semanal | Nueva | GIRM-S-05 | — |
| IRM S-06 | Verificación de automatizaciones Power Automate y conector Microsoft Sentinel | Semanal | Nueva | GIRM-S-06 | — |
| IRM M-01 | Exportación y auditoría independiente del Insider Risk Audit Log (previo a purga de 180 días) | Mensual | Nueva | GIRM-M-01 | — |
| IRM M-02 | Evaluación mensual de Insider Risk Analytics y brechas de cobertura de plantillas | Mensual | Equivalente | DP-M03 | Revisar políticas de Insider Risk con Privacidad/Legal; casos abiertos |
| IRM M-03 | Revisión mensual de efectividad preventiva de Adaptive Protection (DLP + Entra CA + DLCM) | Mensual | Nueva | GIRM-M-03 | — |
| IRM M-04 | Renovación preventiva del contexto del Alert Triage Agent (ventana 90 días) y control de SCUs | Mensual | Equivalente | DP-Q02 | Revisar desempeño y costo de la flota Datos |
| IRM M-05 | Auditoría mensual de los 6 Role Groups, Administrative Units, capacidad forense y comité ejecutivo | Mensual | Equivalente | DP-Q03 | Recertificar roles de Purview y permisos de agentes |
| IRM T-01 | Revisión trimestral de Evaluación de Impacto de Privacidad (DPIA) y cumplimiento laboral | Trimestral | Nueva | GIRM-T-01 | — |
| IRM T-02 | Prueba end-to-end de Adaptive Protection y sincronización bidireccional con Defender XDR | Trimestral | Nueva | GIRM-T-02 | — |
| IRM SM-01 | Análisis semestral de lecciones aprendidas de casos cerrados y efectividad conductual | Semestral | Nueva | GIRM-SM-01 | — |
| IRM A-01 | Recertificación anual del Estatuto Tripartito y simulacro ejecutivo de robo de IP | Anual | Nueva | GIRM-A-01 | — |
| IRM AH-01 | Investigación urgente de robo de propiedad intelectual por usuario saliente o prioritario | Por evento | Nueva | GIRM-AH-01 | — |
| IRM AH-02 | Activación controlada de captura visual Forensic Evidence con doble autorización | Por evento | Nueva | GIRM-AH-02 | — |
| IRM AH-03 | Escalamiento formal de caso confirmado hacia Microsoft Purview eDiscovery (Premium) | Por evento | Nueva | GIRM-AH-03 | — |
| IRM AH-04 | Respuesta conjunta SOC ante incidente unificado Defender XDR + Insider Risk Management | Por evento | Equivalente | ID-A02 | Investigación de insider risk correlacionada con riesgo de identidad |
| IRM AH-05 | Contención de exposición sensible en IA generativa o agentes autónomos (Risky AI / Risky Agents) | Por evento | Nueva | GIRM-AH-05 | — |

### Microsoft Purview Data Lifecycle Management y Records Management (DLM): 28 tareas

| Referencia | Tarea de la guía | Cadencia | Relación | Fila del libro | Tarea del libro |
|---|---|:--:|---|:--:|---|
| DLM D-01 | Monitoreo de estado de distribución y errores en políticas de retención y etiquetas | Diaria | Nueva | GDLM-D-01 | — |
| DLM D-02 | Auditoría diaria de cambios administrativos en políticas, etiquetas y Set-RegulatoryComplianceUI | Diaria | Equivalente | GMIP-D-08 | Validación de Cambios Administrativos del Día Anterior |
| DLM D-03 | Seguimiento de cola activa de revisiones de disposición próximas a vencer o auto-aprobarse | Diaria | Nueva | GDLM-D-03 | — |
| DLM D-04 | Conciliación diaria de eventos transaccionales en Event-Based Retention | Diaria | Nueva | GDLM-D-04 | — |
| DLM D-05 | Supervisión de alertas y ejecuciones activas de Priority Cleanup | Diaria | Nueva | GDLM-D-05 | — |
| DLM D-06 | Verificación de conversión a Inactive Mailboxes en bajas críticas de personal | Diaria | Nueva | GDLM-D-06 | — |
| DLM D-07 | Monitoreo de cuotas en Recoverable Items y Auto-Expanding Archives hasta 3 TB | Diaria | Nueva | GDLM-D-07 | — |
| DLM D-08 | Verificación de políticas de retención y Collection Policies para Copilot y aplicaciones IA | Diaria | Nueva | GDLM-D-08 | — |
| DLM S-01 | Muestreo de precisión en políticas de auto-aplicación de etiquetas y Cloud Attachments | Semanal | Nueva | GDLM-S-01 | — |
| DLM S-02 | Auditoría de membresía dinámica e higiene de atributos en Adaptive Policy Scopes | Semanal | Nueva | GDLM-S-02 | — |
| DLM S-03 | Ejecución de mesas semanales de revisión de disposición multi-etapa (etapas 1 a 5) | Semanal | Nueva | GDLM-S-03 | — |
| DLM S-04 | Monitoreo de crecimiento en Preservation Hold Libraries y paso a Microsoft 365 Archive | Semanal | Nueva | GDLM-S-04 | — |
| DLM S-05 | Revisión de intentos bloqueados o remoción administrativa de etiquetas en Records | Semanal | Nueva | GDLM-S-05 | — |
| DLM S-06 | Gobernanza de ciclo de vida sobre nuevos sitios M365, Teams y agentes Copilot Studio | Semanal | Nueva | GDLM-S-06 | — |
| DLM M-01 | Exportación, conciliación y archivo firmado de Proof of Disposal | Mensual | Nueva | GDLM-M-01 | — |
| DLM M-02 | Medición y saneamiento de deuda de retención en Inactive Mailboxes y OneDrive | Mensual | Nueva | GDLM-M-02 | — |
| DLM M-03 | Evaluación de superficie ROT pre-IA y verificación de purga en SubstrateHolds | Mensual | Nueva | GDLM-M-03 | — |
| DLM M-04 | Conciliación mensual de registros basados en eventos sin Asset ID o con evento omitido | Mensual | Nueva | GDLM-M-04 | — |
| DLM M-05 | Auditoría mensual de privilegios RBAC/PIM, límite de revisores y costos Pay-As-You-Go | Mensual | Equivalente | DP-Q03 | Recertificar roles de Purview y permisos de agentes |
| DLM T-01 | Revisión integral del File Plan frente a cambios normativos y simplificación de series | Trimestral | Nueva | GDLM-T-01 | — |
| DLM T-02 | Prueba controlada de los 4 principios de precedencia y validación de registros migrados | Trimestral | Nueva | GDLM-T-02 | — |
| DLM SM-01 | Auditoría de Preservation Lock, Regulatory Records y holgura de límites del tenant | Semestral | Nueva | GDLM-SM-01 | — |
| DLM A-01 | Recertificación ejecutiva de la Tabla de Retención (ISO 15489-1), RACI y simulacro tabletop | Anual | Nueva | GDLM-A-01 | — |
| DLM AH-01 | Ejecución de Priority Cleanup ante derrame crítico de datos sensibles (Data Spillage) | Por evento | Nueva | GDLM-AH-01 | — |
| DLM AH-02 | Congelamiento inmediato de disposición y aplicación de eDiscovery Hold ante litigio o brecha | Por evento | Nueva | GDLM-AH-02 | — |
| DLM AH-03 | Respuesta ante desactivación o alteración maliciosa de políticas de retención | Por evento | Nueva | GDLM-AH-03 | — |
| DLM AH-04 | Incorporación masiva de nueva regulación o entidad adquirida (M&A) al File Plan | Por evento | Nueva | GDLM-AH-04 | — |
| DLM AH-05 | Remediación de emergencia por saturación de Recoverable Items o Preservation Hold Library | Por evento | Nueva | GDLM-AH-05 | — |

## 7. Contraste del marco maestro con el núcleo 2.0

El marco maestro de excelencia operacional del autor ordena 57 tareas y métricas por subcategoría de NIST CSF 2.0, con su frecuencia. Cada una se asignó a la función del núcleo que la contiene. Es un control de coherencia entre un escrito previo del autor y el modelo; el núcleo no se modificó.

- Las 57 tareas y métricas del marco maestro tienen una función del núcleo que las contiene.
- Usan 36 de las 59 funciones.
- Las otras 23 funciones no tienen una tarea en el marco maestro. Entre ellas están las de IA y agentes, las identidades no humanas, el acceso privilegiado y la recuperación de la identidad.
- La asignación de cada tarea a una función es una propuesta de esta edición.

| Subcategoría | Tarea o métrica del marco maestro | Frecuencia en el marco maestro | Función del núcleo |
|---|---|---|---|
| GV.OC-01 | Comprender la misión organizacional para informar la gestión de riesgos | Anual + durante planificación estratégica | GOB-G1.1 · Contexto, mandato y autoridad del CISO |
| GV.OC-03 | Comprender y gestionar requisitos legales, regulatorios y contractuales | Continuo (monitoreo), Anual (revisión formal) | GOB-G3.1 · Requisitos legales, regulatorios y contractuales |
| GV.RM-01 | Establecer y acordar objetivos de la gestión de riesgos | Anual + tras cambios importantes en el negocio | GOB-G4.1 · Gobernanza del riesgo: estructuras y dueños |
| GV.RM-02 | Establecer, comunicar y mantener declaraciones de apetito y tolerancia al riesgo | Anual + tras cambios en negocio o amenazas | GOB-G4.2 · Apetito de riesgo: definición y comunicación |
| GV.RM-03 | Incluir ciberseguridad en procesos de ERM | Trimestral | GOB-G4.1 · Gobernanza del riesgo: estructuras y dueños |
| GV.RM-06 | Establecer metodología estandarizada de cálculo y priorización de riesgos | Anual (revisión), continuo (aplicación) | GOB-G5.1 · Supervisión de la evaluación y el análisis de riesgos |
| GV.SC-05 | Establecer requisitos de ciberseguridad en contratos con proveedores | Al inicio y renovación del contrato | GES-M6.2 · Nube, tecnologías emergentes y cadena de suministro |
| GV.SC-06 | Realizar due diligence antes de formalizar relaciones con terceros | Antes de firma del contrato | OPE-ID-04 · Evaluación de riesgo de terceros |
| GV.SC-07 | Monitorizar riesgos planteados por el proveedor durante la relación | Mensual (revisión), Trimestral (estratégica) | OPE-ID-04 · Evaluación de riesgo de terceros |
| GV.SC-08 | Incluir proveedores en la planificación de la respuesta a incidentes | Semestral (simulacros) | GES-M5.1 · Preparación de la respuesta a incidentes |
| GV.RR-02 | Establecer, comunicar y hacer cumplir roles y responsabilidades | Anual + en onboarding de personal clave | GOB-G2.1 · Marcos, estándares y grilla de propiedad |
| GV.PO-01 | Establecer y comunicar la política de gestión de riesgos | Anual + ante cambios significativos | GOB-G2.2 · Políticas, estándares y procedimientos |
| GV.PO-02 | Revisar y actualizar política para reflejar cambios | Trimestral + tras incidentes importantes | GOB-G2.2 · Políticas, estándares y procedimientos |
| GV.OV-01 | Reducción porcentual del riesgo agregado en registro de riesgos | Trimestral | GOB-G5.2 · Supervisión del tratamiento y la aceptación de riesgos |
| GV.OV-02 | % de cobertura de controles para marcos regulatorios clave | Semestral | GOB-G3.2 · Cumplimiento y aseguramiento continuo |
| GV.OV-03 | KRI: Vulnerabilidades críticas (>90 días) en sistemas expuestos | Mensual (revisión), Trimestral (tendencias) | OPE-ID-02 · Gestión de vulnerabilidades y de la exposición |
| GV.OV-03 | KPI: MTTD y MTTR para incidentes críticos | Mensual | GES-M4.1 · Gestión de las operaciones de seguridad |
| GV.OV-03 | KPI: Satisfacción de partes interesadas del negocio con servicios de seguridad | Anualmente | GOB-G6.2 · Liderazgo ético y medición de la efectividad |
| ID.AM-01 | Inventario de activos físicos y de software | Continuo (auto), Formal semestral | OPE-ID-01 · Inventario y descubrimiento de activos |
| ID.AM-02 | Inventario de flujos de datos y sistemas externos | Anual + ante cambios | GES-M2.1 · Activos, datos y protección de datos personales |
| ID.AM-04 | Establecer y mantener criticidad de activos | Anual + ante cambios de negocio | GES-M2.1 · Activos, datos y protección de datos personales |
| ID.RA-01 | Identificar y documentar vulnerabilidades | Mensual (escaneos), Continuo para activos críticos | OPE-ID-02 · Gestión de vulnerabilidades y de la exposición |
| ID.RA-02 | Recibir y gestionar inteligencia de amenazas | Diario (monitoreo), Semanal (análisis) | OPE-DE-04 · Inteligencia de amenazas |
| ID.RA-06 | Realizar evaluaciones de riesgo | Anual (formal), Continuo (emergentes) | GOB-G5.1 · Supervisión de la evaluación y el análisis de riesgos |
| ID.AM especial | Pruebas de penetración y evaluaciones de seguridad | Anual o bi-anual por aplicación crítica | OPE-ID-05 · Pruebas ofensivas y validación de controles |
| ID.AM especial | Modelado de amenazas para nuevas arquitecturas | En cada proyecto importante | GES-M3.1 · Arquitectura de seguridad e ingeniería (Zero Trust) |
| PR.AA-01 | Gestionar identidades, credenciales y ciclo de vida de accesos | Continuo (on/off-boarding); Revisión privilegios trimestral | OPE-PR-01 · Identidades y accesos de las personas |
| PR.DS-01 | Proteger datos en reposo | Continuo | OPE-PR-06 · Protección de datos |
| PR.DS-02 | Proteger datos en tránsito | Continuo | OPE-PR-06 · Protección de datos |
| PR.AT-01 | Formación y concienciación para todos los usuarios | Continuo (campañas), Anual (formal) | OPE-PR-10 · Concientización y cultura de seguridad |
| PR.PS-01 | Gestionar configuración de plataformas para prevenir explotación | Periódico (nuevos sistemas), Continuo (drift) | OPE-ID-03 · Postura de nube y de configuración |
| PR.IR-01 | Gestión de parches y actualizaciones de vulnerabilidades | Mensual (estándar), Urgente (0-days) | OPE-ID-02 · Gestión de vulnerabilidades y de la exposición |
| PR especial | Hardening de sistemas y aplicaciones | Antes de implementar, revisiones trimestrales | OPE-ID-03 · Postura de nube y de configuración |
| PR especial | Seguridad de aplicaciones (AppSec/DevSecOps) | En cada ciclo de desarrollo (CI/CD) | OPE-PR-07 · Seguridad de aplicaciones y del desarrollo |
| DE.CM-01 | Monitorizar la red para detectar eventos potenciales | 24/7 continuo | OPE-DE-01 · Monitoreo continuo y gestión de alertas |
| DE.CM-04 | Monitorizar activos físicos y correlacionar con eventos de red | Continuo | OPE-DE-01 · Monitoreo continuo y gestión de alertas |
| DE.CM-08 | Monitorizar endpoints para detectar eventos potenciales | 24/7 continuo | OPE-DE-01 · Monitoreo continuo y gestión de alertas |
| DE.AE-01 | Analizar alertas de sistemas de detección (triaje N1) | 24/7 continuo por alerta | OPE-DE-01 · Monitoreo continuo y gestión de alertas |
| DE.AE-05 | Threat Hunting proactivo | Campañas periódicas (mensual); continuo para IOC críticos | OPE-DE-03 · Búsqueda proactiva de amenazas |
| DE especial | Desarrollo de nuevas detecciones y reglas SIEM | Mensual (ciclos de mejora), Post-incidente | OPE-DE-02 · Ingeniería y calidad de la detección |
| DE especial | Integración de threat intelligence en detecciones | Diario (IOC ingestion), Por incidente | OPE-DE-04 · Inteligencia de amenazas |
| DE especial | Supervisión de seguridad en entornos cloud | Continuo; Revisión diaria de alertas | OPE-DE-01 · Monitoreo continuo y gestión de alertas |
| RS.MA-01 | Declarar incidente y activar CSIRT | Inmediatamente al detectarlo | OPE-RS-01 · Gestión y coordinación de incidentes |
| RS.MA-01 | Ejecutar el plan de respuesta a incidentes | Primeras horas del incidente | OPE-RS-01 · Gestión y coordinación de incidentes |
| RS.AN-01 | Investigar notificaciones de sistemas de detección | Durante y post-contención | OPE-RS-02 · Análisis e investigación forense |
| RS.CO-01 | Informar a partes interesadas internas sobre incidentes | Durante incidente (updates continuos) | OPE-RS-04 · Comunicación y notificación de incidentes |
| RS.CO-02 | Coordinar con partes externas (fuerzas del orden) | Según necesidad | OPE-RS-04 · Comunicación y notificación de incidentes |
| RS.MI-01 | Contener los incidentes | Inmediatamente (primeras horas) | OPE-RS-03 · Contención, erradicación y respuesta automatizada |
| RS.MI-02 | Erradicar los incidentes | Post-contención (24–48h) | OPE-RS-03 · Contención, erradicación y respuesta automatizada |
| RS especial | Documentar incidente y lecciones aprendidas (post-mortem) | 1 semana post-incidente | GES-M5.2 · Conducción de la respuesta y aprendizaje |
| RS especial | Desarrollar y mantener playbooks de respuesta | Anual (revisión), Post-incidente (ajustes) | GES-M5.1 · Preparación de la respuesta a incidentes |
| RC.RP-01 | Ejecutar el plan de recuperación de incidentes | Post-erradicación | OPE-RC-02 · Recuperación de servicios críticos |
| RC.CO-01 | Gestionar relaciones públicas y reputación post-incidente | Post-incidente | OPE-RC-05 · Comunicación de la recuperación y lecciones aprendidas |
| RC.CO-02 | Comunicar actividades de recuperación a stakeholders | Post-incidente | OPE-RC-05 · Comunicación de la recuperación y lecciones aprendidas |
| RC.IM-01 | Incorporar lecciones aprendidas en planes de recuperación | 1–2 semanas post-incidente | OPE-RC-05 · Comunicación de la recuperación y lecciones aprendidas |
| RC especial | Restaurar sistemas y datos desde backups | Post-contención (horas–días) | OPE-RC-01 · Respaldo y restauración |
| RC especial | Validar seguridad antes de re-conectar sistemas restaurados | Antes de poner en producción | OPE-RC-02 · Recuperación de servicios críticos |

Funciones del núcleo sin una tarea en el marco maestro:

| ID | Función |
|---|---|
| GOB-G1.2 | Estrategia de seguridad y alineación con el negocio |
| GOB-G6.1 | Comunicación estratégica y reporte a la dirección |
| GES-M1.1 | Programa de seguridad y portafolio de productos-control |
| GES-M1.2 | Finanzas, equipo, proveedores y capacitación |
| GES-M2.2 | Gestión de identidades y accesos |
| GES-M3.2 | Selección, implementación y evaluación de controles |
| GES-M4.2 | Gestión de amenazas, vulnerabilidades y riesgos emergentes |
| GES-M6.1 | Continuidad, recuperación y resiliencia |
| OPE-ID-06 | Descubrimiento y clasificación de datos |
| OPE-ID-07 | Inventario y evaluación de sistemas de IA y agentes |
| OPE-PR-02 | Acceso privilegiado |
| OPE-PR-03 | Identidades no humanas, de cargas y de agentes |
| OPE-PR-04 | Protección y gestión de dispositivos |
| OPE-PR-05 | Protección del correo y la colaboración |
| OPE-PR-08 | Seguridad de red y segmentación |
| OPE-PR-09 | Protección de cargas e infraestructura de nube |
| OPE-PR-11 | Protección de sistemas de IA y agentes |
| OPE-PR-12 | Seguridad de tecnología operacional y dispositivos conectados |
| OPE-DE-05 | Gestión de registros y telemetría |
| OPE-DE-06 | Observabilidad de IA y agentes |
| OPE-RS-05 | Gestión de crisis y ejercicios |
| OPE-RC-03 | Recuperación de la identidad y de la plataforma de control |
| OPE-RC-04 | Continuidad y operación degradada |

## 8. Límites

- **Las equivalencias son una propuesta.** Dos tareas se consideraron equivalentes por su objeto y su propósito, leídos en el título y, en los casos dudosos, en el texto de la guía. Otra persona puede agrupar distinto.
- **Los procedimientos no se revalidaron.** De cada guía se tomaron el título, la cadencia, el rol y las categorías del marco de cada tarea. Los pasos, las rutas de consola y los nombres de producto no se compararon con la documentación oficial vigente.
- **Las guías tienen fecha.** Los borradores van de febrero a abril de 2026; el de Intune, de noviembre. Las dos guías del repositorio se validaron el 11 de noviembre de 2026. Microsoft Ignite (17 al 20 de noviembre de 2026) puede cambiar nombres y portales.
- **Diez productos siguen con las tareas del borrador.** El repositorio del autor tiene una versión vigente de esas guías, con otra estructura. No se integró tarea por tarea: está en los catálogos del libro y en el documento M11 «Puente con el repositorio del autor: guías, acciones, indicadores técnicos y formación».
- **Los borradores de riesgo interno y de ciclo de vida de los datos no traen tareas por cadencia.** `Microsoft_Purview_IRM_Consolidated.md` y `Microsoft_Purview_DLM_NIST_CSF2_Consolidated.md` son documentos de referencia: capacidades, licencias y correspondencia con los marcos. Las tareas de esas dos disciplinas se tomaron de las guías 17 y 16 del repositorio.
- **No hay una guía del autor para el dominio de nube.**
- **Las tareas tomadas de los borradores no tienen práctica independiente de la plataforma, autonomía sugerida ni indicador.** Las 47 tareas de riesgo interno y de ciclo de vida de los datos sí tienen práctica, y 38 de ellas tienen el indicador técnico de su guía; ninguna tiene autonomía sugerida.

---

*Frontier CISO Atlas · Modelo Operativo CISO 365 · edición Microsoft · versión 2.1 · revisión 3 · 15 de noviembre de 2026 · propuesta sujeta a validación · @SCavanna*

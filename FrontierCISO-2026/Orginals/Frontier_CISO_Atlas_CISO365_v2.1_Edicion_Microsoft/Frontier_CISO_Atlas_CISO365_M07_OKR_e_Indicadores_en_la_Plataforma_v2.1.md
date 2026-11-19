# OKR e indicadores sobre la plataforma de Microsoft

**Frontier CISO Atlas · Modelo Operativo CISO 365 · edición Microsoft · versión 2.1, revisión 3** · documento M07 · 15 de noviembre de 2026 · @SCavanna

> Propuesta de base. Las capacidades, las licencias y la cobertura se verificaron en fuentes oficiales con fecha de corte al 15 de noviembre de 2026; revalidar después de Microsoft Ignite (17 al 20 de noviembre de 2026).

## 1. De dónde sale cada dato

| Tipo de medición | Indicadores | Qué significa |
|---|:--:|---|
| Directa | 12 | El dato está en un informe o en un tablero del producto. |
| Derivada | 99 | Requiere una consulta, una exportación o un cálculo sobre datos de la plataforma. |
| Registro de gestión | 113 | Es un dato de gestión: se lleva en un registro propio, fuera de la plataforma. |
| Total | 224 |  |

113 de los 224 indicadores son registros de gestión: no salen de ninguna plataforma. Son, en su mayoría, los de gobierno y los que el directorio mira. La plataforma aporta el dato de los otros 111, casi siempre mediante una consulta o una exportación.

La fuente se asignó por función, salvo en los 42 indicadores principales, que tienen fuente propia. Es una guía inicial: la fuente de cada indicador elegido se confirma con la línea base y se anota en la hoja «Indicadores × Microsoft».

## 2. Indicadores principales y su fuente

### Directorio y síndicos (12)

| ID | Indicador | Tipo de medición | Fuente del dato en Microsoft |
|---|---|---|---|
| K14 | Supervisión activa del Directorio sobre el ciberriesgo | Registro de gestión | Actas del directorio: registro propio. |
| K24 | Pérdidas por incidentes frente a la tolerancia anual | Registro de gestión | Registro de pérdidas; los incidentes provienen de Defender XDR y de Sentinel. |
| K25 | Riesgos residuales fuera del apetito | Registro de gestión | Registro de riesgos. |
| K26 | Pérdida esperada de los escenarios prioritarios frente al apetito | Registro de gestión | Cuantificación de escenarios; Exposure Management aporta las rutas de ataque y los activos críticos. |
| K27 | Servicios críticos concentrados en un proveedor sin alternativa | Registro de gestión | Registro de servicios externalizados. En esta edición incluye a Microsoft como proveedor. |
| K30 | Pruebas de recuperación que cumplen RTO y RPO | Derivada | Azure Site Recovery: simulacros de conmutación por error. Azure Backup y Microsoft 365 Backup: restauraciones de prueba. Para las demás cargas, registro propio. |
| K58 | Calidad del reporte de ciberriesgo al Directorio | Registro de gestión | Evaluación del informe por parte del directorio: registro propio. |
| K59 | Hallazgos de auditoría y de reguladores cerrados en plazo | Registro de gestión | Registro de hallazgos; Compliance Manager para las acciones de mejora. |
| K60 | Controles clave con efectividad probada | Derivada | Compliance Manager: acciones probadas. Defender for Cloud: cumplimiento regulatorio. Pruebas independientes: registro propio. |
| K61 | Notificaciones obligatorias emitidas en plazo | Registro de gestión | Registro de notificaciones. |
| K98 | Decisiones automatizadas de alto impacto con supervisión humana verificada | Registro de gestión | Registro de sistemas de IA; Agent 365 aporta el inventario y la actividad de los agentes. |
| KX03 | Cumplimiento de los niveles de servicio | Registro de gestión | Informes de servicio de cada proveedor. En un servicio gestionado de detección, los tiempos de los incidentes en Defender XDR y en Sentinel permiten verificarlos. |

### CEO, CFO y comité ejecutivo (14)

| ID | Indicador | Tipo de medición | Fuente del dato en Microsoft |
|---|---|---|---|
| K09 | Procesos y activos críticos con dueño de riesgo designado | Registro de gestión | Registro de dueños de riesgo; Exposure Management permite marcar los activos críticos. |
| K10 | Ejecutivos con objetivos de ciberseguridad en su evaluación | Registro de gestión | Registro de objetivos de los ejecutivos. |
| K11 | Comportamiento seguro: tasa de reporte de phishing | Directa | Attack simulation training: informes de simulación. Defender for Office 365: mensajes reportados por los usuarios. |
| K12 | Cobertura de capacidades críticas del equipo de seguridad | Registro de gestión | Matriz de capacidades del equipo; el plan de formación de esta edición asigna programas Ninja por rol. |
| K13 | Retención del talento crítico de seguridad | Registro de gestión | Registro de personas. |
| K17 | Inversión en seguridad trazada a riesgos y objetivos del negocio | Registro de gestión | Presupuesto trazado a riesgos: registro propio. |
| K18 | Avance del roadmap estratégico de seguridad | Registro de gestión | Hoja de ruta: registro propio. |
| K19 | Reducción de riesgo por unidad de inversión | Registro de gestión | Registro de riesgos y presupuesto. |
| K23 | Requisitos de seguridad de clientes y contratos cumplidos en plazo | Registro de gestión | Registro de requisitos de clientes; Compliance Manager aporta la evidencia por norma. |
| K103 | Desvío de la ejecución presupuestaria | Registro de gestión | Presupuesto; la facturación de Azure aporta el consumo de los servicios de seguridad. |
| K104 | Gasto de seguridad con costo total conocido | Registro de gestión | Presupuesto; facturación de Azure y licencias asignadas. |
| K122 | Capacidades con herramientas solapadas sin justificación | Registro de gestión | Libro de diagnóstico, hoja «Pila y cobertura»; la hoja Capacidades de este libro muestra lo ya licenciado. |
| KX14 | Funciones críticas concentradas en un mismo proveedor | Registro de gestión | Hoja «Funciones × Microsoft» de este libro: funciones cuya herramienta principal es de Microsoft. |
| KX16 | Desvío del costo por unidad de resultado | Registro de gestión | Contratos y facturación. |

### CIO y CTO (16)

| ID | Indicador | Tipo de medición | Fuente del dato en Microsoft |
|---|---|---|---|
| K20 | Tiempo de habilitación segura de iniciativas | Registro de gestión | Herramienta de gestión de servicios: fecha de pedido y fecha de habilitación. |
| K33 | Autenticación resistente al phishing | Directa | Microsoft Entra: informe de métodos de autenticación y registros de inicio de sesión. |
| K34 | Accesos privilegiados sin privilegios permanentes (JIT) | Derivada | Privileged Identity Management: asignaciones aptas frente a asignaciones activas permanentes. |
| K36 | Segmentación de activos críticos verificada | Registro de gestión | Pruebas de segmentación; Exposure Management aporta las rutas de ataque hacia los activos críticos. |
| K38 | Aplicaciones críticas con controles automatizados en el pipeline | Derivada | DevOps security de Defender for Cloud: repositorios y canalizaciones conectados y sus hallazgos. |
| K41 | Cobertura de telemetría y protección de activos críticos | Derivada | Defender for Endpoint: dispositivos incorporados. Sentinel: estado de los conectores. Defender for Cloud: cobertura de planes. |
| K42 | Tiempo medio de detección (MTTD) | Derivada | Defender XDR y Sentinel: marcas de tiempo de los incidentes. |
| K45 | Tiempo medio de contención (MTTC) | Derivada | Defender XDR y Sentinel: marcas de tiempo de los incidentes y acciones del centro de actividades. |
| K47 | Tiempo de restauración de servicios críticos frente al RTO | Derivada | Azure Site Recovery y Azure Backup: duración de los simulacros y de las restauraciones. |
| K116 | Iniciativas con revisión de arquitectura antes de producción | Registro de gestión | Registro de revisiones de arquitectura. |
| K118 | Accesos evaluados por política con señales de contexto | Derivada | Microsoft Entra: información y registros de acceso condicional. |
| K120 | Desviaciones críticas de configuración abiertas | Derivada | Defender for Cloud: recomendaciones de severidad alta. Intune: dispositivos no conformes. |
| K123 | Paridad de control entre entornos | Derivada | Defender for Cloud: puntuación y cumplimiento por entorno conectado. |
| K134 | Cuentas y suscripciones de nube bajo la línea base | Derivada | Defender for Cloud: suscripciones, cuentas y proyectos conectados. Azure Policy: asignaciones. |
| K138 | Tiempo de corrección de vulnerabilidades críticas | Derivada | Defender Vulnerability Management: exposición y tiempos de corrección. |
| K141 | Recursos conformes a la línea base en el entorno menos conforme | Derivada | Defender for Cloud: cumplimiento del benchmark por entorno. |

## 3. El resto de los indicadores

Los demás indicadores toman la fuente de su función. La tabla completa está en la hoja «Indicadores × Microsoft» del libro y, por función, en el documento M02 «Capacidades de Microsoft por función y por licencia».

| Plano | Indicadores | Directa | Derivada | Registro de gestión |
|---|:--:|:--:|:--:|:--:|
| Gobierno | 57 | 0 | 8 | 49 |
| Gestión | 55 | 0 | 32 | 23 |
| Operación | 90 | 12 | 59 | 19 |
| Externalización | 22 | 0 | 0 | 22 |

## 4. Disponibilidad del dato

Un dato de la plataforma existe solo si la capacidad que lo produce está desplegada. El libro lo calcula con el despliegue cargado en la hoja Capacidades:

| Disponibilidad | Regla |
|---|---|
| Registro propio | El indicador es un registro de gestión. |
| Disponible | La adopción de las capacidades de la función alcanza el mínimo fijado en Parámetros (por defecto, 50%). |
| Parcial | Hay despliegue, pero por debajo del mínimo. |
| Falta desplegar | Ninguna capacidad de la función está desplegada. |
| Sin capacidad asociada | La función no tiene capacidades de la plataforma. |

## 5. Los resultados clave sobre la plataforma

Los 72 resultados clave son los del núcleo. La tabla muestra qué capacidades sostienen cada uno. La hoja «OKR × Microsoft» agrega la adopción y la preparación: lista, en despliegue o falta desplegar.

### Ciclo 1 · Conocer, estabilizar y ordenar

| ID | Resultado clave (operación propia) | Función | Aporte de Microsoft | Capacidades |
|---|---|---|---|---|
| C1-F1-KR1 | El plan anual, el presupuesto y las decisiones requeridas están aprobados por el sponsor y presentados al directorio. | GOB-G1.2 | Fuera de la plataforma | — |
| C1-F1-KR2 | Los procesos y los activos críticos tienen un dueño de riesgo designado. | GOB-G4.1 | Fuera de la plataforma | — |
| C1-F1-KR3 | Las decisiones materiales de seguridad las toma el rol que tiene la autoridad y quedan registradas. | GOB-G4.1 | Fuera de la plataforma | — |
| C1-F2-KR1 | Los cruces críticos de la grilla de propiedad tienen un dueño nominado. | GOB-G2.1 | Apoya | Microsoft Purview Compliance Manager · Defender for Cloud: postura (Foundational CSPM y Defender CSPM) |
| C1-F2-KR2 | Los controles prioritarios del portafolio tienen dueño, objetivo medible y evidencia definidos. | GES-M1.1 | Apoya | Microsoft Security Exposure Management · Microsoft Defender XDR |
| C1-F2-KR3 | El gasto de seguridad tiene su costo total conocido. | GES-M1.2 | Apoya | — |
| C1-F3-KR1 | Las cuentas privilegiadas y las de acceso remoto usan autenticación resistente a la suplantación; el resto avanza. | OPE-PR-01 | Cubre | Microsoft Entra ID con Conditional Access · Microsoft Entra ID Protection · Microsoft Entra ID Governance |
| C1-F3-KR2 | El inventario de activos cubre todos los entornos del alcance. | OPE-ID-01 | Cubre | Microsoft Security Exposure Management · Microsoft Defender for Endpoint · Defender for Cloud: postura (Foundational CSPM y Defender CSPM) · Microsoft Defender External Attack Surface Management |
| C1-F3-KR3 | Las vulnerabilidades explotadas activamente y las exposiciones críticas se corrigen en plazo. | OPE-ID-02 | Cubre | Microsoft Defender Vulnerability Management · Microsoft Security Exposure Management · Defender for Servers · Defender for Containers |
| C1-F4-KR1 | Los activos críticos tienen telemetría y protección. | OPE-DE-05 | Cubre | Microsoft Sentinel · Microsoft Purview Audit y eDiscovery · Azure Arc, Azure Policy y Azure Update Manager |
| C1-F4-KR2 | Los acuerdos y los contactos de respuesta están vigentes y verificados. | GES-M5.1 | Cubre en parte | Automatización de Microsoft Sentinel · Microsoft Defender XDR |
| C1-F4-KR3 | Los sistemas críticos tienen respaldos inalterables y una restauración probada. | OPE-RC-01 | Cubre en parte | Azure Backup · Microsoft 365 Backup |
| C1-F5-KR1 | Los proveedores críticos están identificados, evaluados y con cláusulas de seguridad. | OPE-ID-04 | Apoya | Microsoft Defender for Cloud Apps · Microsoft Defender External Attack Surface Management |
| C1-F5-KR2 | La cobertura de control está medida en cada entorno y la paridad entre entornos mejora. | GES-M3.2 | Apoya | Azure Arc, Azure Policy y Azure Update Manager · Microsoft Intune · Microsoft Purview Compliance Manager |
| C1-F5-KR3 | Las capacidades con herramientas solapadas tienen una decisión: consolidar, mantener o reemplazar. | GES-M3.2 | Apoya | Azure Arc, Azure Policy y Azure Update Manager · Microsoft Intune · Microsoft Purview Compliance Manager |
| C1-F6-KR1 | Los sistemas de IA y los agentes están inventariados, con dueño y propósito. | OPE-ID-07 | Cubre | Microsoft Agent 365 · Defender for Cloud: postura de IA y Defender for AI Services · Microsoft Purview Data Security Posture Management · Microsoft Defender for Cloud Apps |
| C1-F6-KR2 | Los casos de uso nuevos de IA tienen una evaluación de riesgo e impacto antes de ponerse en marcha. | GOB-G2.2 | Apoya | Azure Arc, Azure Policy y Azure Update Manager · Microsoft Intune · Microsoft Entra ID con Conditional Access |
| C1-F6-KR3 | Cada agente tiene un dueño humano y una autoridad delegada acotada. | GES-M2.2 | Cubre | Microsoft Entra ID con Conditional Access · Microsoft Entra ID Governance · Microsoft Entra Privileged Identity Management · Microsoft Entra ID Protection |

### Ciclo 2 · Adecuar

| ID | Resultado clave (operación propia) | Función | Aporte de Microsoft | Capacidades |
|---|---|---|---|---|
| C2-F1-KR1 | El directorio aprobó el apetito de riesgo, con umbrales medibles para los escenarios prioritarios. | GOB-G4.2 | Fuera de la plataforma | — |
| C2-F1-KR2 | Las políticas y los estándares están dentro de su ciclo de revisión. | GOB-G2.2 | Apoya | Azure Arc, Azure Policy y Azure Update Manager · Microsoft Intune · Microsoft Entra ID con Conditional Access |
| C2-F1-KR3 | Las obligaciones aplicables están mapeadas a controles con evidencia vigente. | GOB-G3.2 | Cubre en parte | Microsoft Purview Compliance Manager · Defender for Cloud: postura (Foundational CSPM y Defender CSPM) · Microsoft Purview Audit y eDiscovery |
| C2-F2-KR1 | La estructura y la dotación objetivo están aprobadas, y las capacidades críticas, cubiertas. | GES-M1.2 | Apoya | — |
| C2-F2-KR2 | Las cadencias operativas de los controles prioritarios se cumplen. | GES-M1.1 | Apoya | Microsoft Security Exposure Management · Microsoft Defender XDR |
| C2-F2-KR3 | La hoja de ruta del año avanza según lo comprometido. | GES-M1.1 | Apoya | Microsoft Security Exposure Management · Microsoft Defender XDR |
| C2-F3-KR1 | La paridad de control entre entornos alcanza el nivel objetivo. | GES-M3.2 | Apoya | Azure Arc, Azure Policy y Azure Update Manager · Microsoft Intune · Microsoft Purview Compliance Manager |
| C2-F3-KR2 | Los accesos privilegiados dejan de ser permanentes. | OPE-PR-02 | Cubre | Microsoft Entra Privileged Identity Management · Microsoft Entra ID con Conditional Access · Segmentación y acceso privado en Azure |
| C2-F3-KR3 | Los datos sensibles están clasificados y protegidos. | OPE-PR-06 | Cubre | Microsoft Purview Information Protection · Microsoft Purview Data Loss Prevention · Microsoft Purview Insider Risk Management · Customer Key y Double Key Encryption |
| C2-F4-KR1 | Las técnicas de ataque priorizadas tienen detección validada. | OPE-DE-02 | Cubre | Microsoft Sentinel · Microsoft Defender XDR |
| C2-F4-KR2 | El tiempo medio de detección está dentro del objetivo. | OPE-DE-01 | Cubre | Microsoft Defender XDR · Microsoft Sentinel · Microsoft Security Copilot |
| C2-F4-KR3 | Los escenarios críticos tienen una guía de actuación probada. | GES-M5.1 | Cubre en parte | Automatización de Microsoft Sentinel · Microsoft Defender XDR |
| C2-F5-KR1 | Los proveedores críticos entregan evidencia de control actualizada. | GES-M6.2 | Cubre en parte | Defender for Cloud: postura (Foundational CSPM y Defender CSPM) · Microsoft Defender for Cloud Apps · Microsoft Agent 365 · DevOps security de Defender for Cloud |
| C2-F5-KR2 | Las cuentas, las suscripciones y los proyectos de nube están bajo la línea base de la organización. | GES-M6.2 | Cubre en parte | Defender for Cloud: postura (Foundational CSPM y Defender CSPM) · Microsoft Defender for Cloud Apps · Microsoft Agent 365 · DevOps security de Defender for Cloud |
| C2-F5-KR3 | Los incidentes de terceros se notifican dentro del plazo contractual. | GES-M6.2 | Cubre en parte | Defender for Cloud: postura (Foundational CSPM y Defender CSPM) · Microsoft Defender for Cloud Apps · Microsoft Agent 365 · DevOps security de Defender for Cloud |
| C2-F6-KR1 | Los agentes en producción tienen identidad propia y permisos por herramienta revisados. | OPE-PR-11 | Cubre | Controles de seguridad de Microsoft Foundry · Protecciones de Microsoft Purview para IA generativa · Defender for Cloud: postura de IA y Defender for AI Services · Microsoft Entra Agent ID |
| C2-F6-KR2 | Las interacciones con IA están protegidas contra la fuga de datos. | OPE-PR-06 | Cubre | Microsoft Purview Information Protection · Microsoft Purview Data Loss Prevention · Microsoft Purview Insider Risk Management · Customer Key y Double Key Encryption |
| C2-F6-KR3 | La actividad de los agentes está integrada a la vigilancia. | OPE-DE-06 | Cubre en parte | Microsoft Agent 365 · Defender for Cloud: postura de IA y Defender for AI Services · Protecciones de Microsoft Purview para IA generativa · Microsoft Sentinel |

### Ciclo 3 · Evolucionar y probar

| ID | Resultado clave (operación propia) | Función | Aporte de Microsoft | Capacidades |
|---|---|---|---|---|
| C3-F1-KR1 | Los escenarios prioritarios están cuantificados. | GOB-G5.1 | Apoya | Microsoft Security Exposure Management · Defender for Cloud: postura (Foundational CSPM y Defender CSPM) |
| C3-F1-KR2 | Los controles clave entregan su evidencia de forma automática. | GOB-G3.2 | Cubre en parte | Microsoft Purview Compliance Manager · Defender for Cloud: postura (Foundational CSPM y Defender CSPM) · Microsoft Purview Audit y eDiscovery |
| C3-F1-KR3 | Las decisiones solicitadas a la dirección se resuelven en plazo. | GOB-G6.1 | Apoya | Microsoft Security Exposure Management · Microsoft Defender XDR |
| C3-F2-KR1 | El trabajo no planificado del equipo baja al nivel objetivo. | GES-M1.1 | Apoya | Microsoft Security Exposure Management · Microsoft Defender XDR |
| C3-F2-KR2 | El personal con funciones de alto riesgo tiene formación específica vigente. | GES-M1.2 | Apoya | — |
| C3-F2-KR3 | Cada tarea operativa tiene un responsable definido: persona, proveedor o agente. | GES-M1.2 | Apoya | — |
| C3-F3-KR1 | El acceso a los recursos críticos lo decide una política que evalúa identidad, dispositivo y contexto. | GES-M3.1 | Apoya | Microsoft Security Exposure Management · Defender for Cloud: postura (Foundational CSPM y Defender CSPM) |
| C3-F3-KR2 | La segmentación de los activos críticos está verificada con pruebas. | OPE-PR-08 | Cubre en parte | Global Secure Access (Entra Internet Access y Private Access) · Azure Firewall, Web Application Firewall y DDoS Protection · Segmentación y acceso privado en Azure |
| C3-F3-KR3 | Las identidades no humanas tienen dueño, rotación y privilegio revisado. | OPE-PR-03 | Cubre | Microsoft Entra Workload ID · Microsoft Entra Agent ID · Microsoft Defender for Cloud Apps · Azure Key Vault y Managed HSM |
| C3-F4-KR1 | Se realizó un ejercicio de adversario de extremo a extremo y sus hallazgos críticos se corrigieron y se revalidaron. | OPE-ID-05 | Cubre en parte | Attack simulation training · Microsoft Security Exposure Management · Controles de seguridad de Microsoft Foundry |
| C3-F4-KR2 | Las pruebas de recuperación cumplen los objetivos de tiempo y de punto de recuperación. | OPE-RC-02 | Cubre en parte | Azure Site Recovery · Azure Backup |
| C3-F4-KR3 | La recuperación de la identidad y de la plataforma de control está probada en un entorno aislado. | OPE-RC-03 | Cubre en parte | Microsoft Defender for Identity · Microsoft Entra ID con Conditional Access · Azure Backup |
| C3-F5-KR1 | Los servicios críticos concentrados en un proveedor sin alternativa están dentro del límite del apetito. | GES-M6.2 | Cubre en parte | Defender for Cloud: postura (Foundational CSPM y Defender CSPM) · Microsoft Defender for Cloud Apps · Microsoft Agent 365 · DevOps security de Defender for Cloud |
| C3-F5-KR2 | Los servicios críticos usan telemetría, identidad y evidencia portables. | GES-M6.2 | Cubre en parte | Defender for Cloud: postura (Foundational CSPM y Defender CSPM) · Microsoft Defender for Cloud Apps · Microsoft Agent 365 · DevOps security de Defender for Cloud |
| C3-F5-KR3 | Los hallazgos de los proveedores críticos se corrigen en plazo. | OPE-ID-04 | Apoya | Microsoft Defender for Cloud Apps · Microsoft Defender External Attack Surface Management |
| C3-F6-KR1 | Los agentes en producción tienen una evaluación adversarial vigente. | OPE-PR-11 | Cubre | Controles de seguridad de Microsoft Foundry · Protecciones de Microsoft Purview para IA generativa · Defender for Cloud: postura de IA y Defender for AI Services · Microsoft Entra Agent ID |
| C3-F6-KR2 | La detención de emergencia de los agentes con autonomía de ejecución está probada. | OPE-PR-11 | Cubre | Controles de seguridad de Microsoft Foundry · Protecciones de Microsoft Purview para IA generativa · Defender for Cloud: postura de IA y Defender for AI Services · Microsoft Entra Agent ID |
| C3-F6-KR3 | Los procesos críticos que usan IA pueden operar sin ella. | OPE-RC-04 | Fuera de la plataforma | — |

### Ciclo 4 · Demostrar y sostener

| ID | Resultado clave (operación propia) | Función | Aporte de Microsoft | Capacidades |
|---|---|---|---|---|
| C4-F1-KR1 | El informe anual se presentó al directorio y a los síndicos, con resultados, pendientes y aprendizajes. | GOB-G6.1 | Apoya | Microsoft Security Exposure Management · Microsoft Defender XDR |
| C4-F1-KR2 | Los riesgos altos tuvieron una revisión independiente. | GOB-G4.1 | Fuera de la plataforma | — |
| C4-F1-KR3 | El mandato se revisó, y el plan y el presupuesto del año 2 están aprobados. | GOB-G1.1 | Fuera de la plataforma | — |
| C4-F2-KR1 | La ejecución presupuestaria cierra dentro del desvío tolerado. | GES-M1.2 | Apoya | — |
| C4-F2-KR2 | El talento crítico se retiene. | GES-M1.2 | Apoya | — |
| C4-F2-KR3 | Las funciones críticas alcanzan el nivel de evidencia «Probado». | GES-M1.1 | Apoya | Microsoft Security Exposure Management · Microsoft Defender XDR |
| C4-F3-KR1 | Los resultados del perfil objetivo se alcanzan. | GOB-G2.1 | Apoya | Microsoft Purview Compliance Manager · Defender for Cloud: postura (Foundational CSPM y Defender CSPM) |
| C4-F3-KR2 | No quedan desviaciones críticas de configuración abiertas más allá de lo tolerado. | GES-M3.2 | Apoya | Azure Arc, Azure Policy y Azure Update Manager · Microsoft Intune · Microsoft Purview Compliance Manager |
| C4-F3-KR3 | Los controles clave tienen su efectividad probada. | GES-M3.2 | Apoya | Azure Arc, Azure Policy y Azure Update Manager · Microsoft Intune · Microsoft Purview Compliance Manager |
| C4-F4-KR1 | Las acciones correctivas posteriores a los incidentes se cierran en plazo. | GES-M5.2 | Cubre en parte | Microsoft Defender XDR · Microsoft Sentinel · Microsoft Security Copilot |
| C4-F4-KR2 | El tiempo de restauración de los servicios críticos queda dentro del objetivo. | OPE-RC-02 | Cubre en parte | Azure Site Recovery · Azure Backup |
| C4-F4-KR3 | Los falsos positivos de las detecciones prioritarias bajan al nivel objetivo. | OPE-DE-02 | Cubre | Microsoft Sentinel · Microsoft Defender XDR |
| C4-F5-KR1 | La decisión de provisión de cada función —propia, co-gestionada o externalizada— se revisó con el costo y el resultado del año. | GES-M1.2 | Apoya | — |
| C4-F5-KR2 | Los requisitos de seguridad de clientes y contratos se cumplen en plazo. | GOB-G3.1 | Apoya | Microsoft Purview Compliance Manager · Microsoft Purview Data Lifecycle Management y Records Management · Microsoft Purview Communication Compliance e Information Barriers |
| C4-F5-KR3 | La paridad de control entre entornos alcanza el nivel de fin de año. | GES-M3.2 | Apoya | Azure Arc, Azure Policy y Azure Update Manager · Microsoft Intune · Microsoft Purview Compliance Manager |
| C4-F6-KR1 | Cada tipo de acción de los agentes en producción tiene un nivel de autonomía aprobado por el dueño del riesgo. | GOB-G4.2 | Fuera de la plataforma | — |
| C4-F6-KR2 | Las acciones de agentes que deben revertirse se mantienen por debajo del límite. | OPE-DE-06 | Cubre en parte | Microsoft Agent 365 · Defender for Cloud: postura de IA y Defender for AI Services · Protecciones de Microsoft Purview para IA generativa · Microsoft Sentinel |
| C4-F6-KR3 | Las decisiones automatizadas de alto impacto tienen supervisión humana verificada. | GOB-G6.2 | Fuera de la plataforma | — |

## 6. Lo que la plataforma no mide

- **Los resultados clave de gobierno.** 9 de los 72 resultados clave pertenecen a funciones que están fuera de la plataforma: mandato, apetito, comité, ejercicios y rendición de cuentas.
- **Lo que está fuera de su alcance.** Un entorno sin conectar no aparece en ninguna puntuación. La paridad entre entornos (K123) se calcula sobre los entornos conectados y se completa con un registro de los que no lo están.
- **La efectividad.** Una configuración correcta no prueba que el control funcione. El nivel «Probado» y el indicador K60 exigen una prueba.
- **Al propio proveedor.** La concentración (K27 y KX14) y el cumplimiento de los niveles de servicio (KX03) se miden fuera de la plataforma.

---

*Frontier CISO Atlas · Modelo Operativo CISO 365 · edición Microsoft · versión 2.1 · revisión 3 · 15 de noviembre de 2026 · propuesta sujeta a validación · @SCavanna*

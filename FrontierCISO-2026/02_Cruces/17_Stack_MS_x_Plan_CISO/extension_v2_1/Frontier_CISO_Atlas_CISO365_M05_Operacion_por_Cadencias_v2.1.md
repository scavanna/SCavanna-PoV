# Operación por cadencias: excelencia operacional

**Frontier CISO Atlas · Modelo Operativo CISO 365 · edición Microsoft · versión 2.1, revisión 3** · documento M05 · 15 de noviembre de 2026 · @SCavanna

> Propuesta de base. Las capacidades, las licencias y la cobertura se verificaron en fuentes oficiales con fecha de corte al 15 de noviembre de 2026; revalidar después de Microsoft Ignite (17 al 20 de noviembre de 2026).

## 1. Qué se entiende por excelencia operacional

El marco de excelencia operacional del autor para la oficina del CISO la define como la capacidad de una organización para «entregar valor de seguridad de manera predecible, escalable y sostenible», con poca fricción para el negocio y con un equipo que trabaja en condiciones sostenibles. Tiene tres dominios: el técnico (detección, respuesta, automatización y calidad de los datos), el humano (carga, formación y cultura de mejora) y el estratégico (gobierno del riesgo y comunicación con la dirección).

El núcleo 2.0 lo expresa con un principio: cada control es un producto con dueño, objetivo, configuración de referencia y evidencia. Un control desplegado y sin operar no es un control: es una herramienta instalada.

## 2. De la guía del fabricante a la tarea con dueño

| Eslabón | Qué es | Dónde está |
|---|---|---|
| Guía de operación oficial | Lo que el fabricante recomienda hacer cada día, cada semana y cada mes | Sección 3 |
| Tarea por cadencia | La acción concreta, con rol, frecuencia y fuente | Hoja Operación por cadencias; sección 8 |
| Práctica independiente de la plataforma | Lo que la tarea ejemplifica y que valdría con cualquier producto | Sección 5 |
| Indicador | Cómo se sabe si la tarea da resultado | Hoja Indicadores × Microsoft; documento M07 «OKR e indicadores sobre la plataforma de Microsoft» |
| Evidencia | Lo que queda registrado y sostiene el nivel de la función | Libro de diagnóstico del núcleo |

## 3. Guías de operación oficiales

| Dominio | Producto | Guía | Cadencias que propone | Fecha de la página | Fuente |
|---|---|---|---|---|---|
| Identidades | Microsoft Entra | Microsoft Entra operations reference guide | No trae tabla diaria/semanal/mensual en las páginas abiertas: organiza tareas continuas con propietario en cuatro áreas (identidad y acceso, autenticación, gobierno, operaciones). La sección de operaciones (ops-guide-ops, 2024-04-12) pide impulsar mejoras de Identity Secure Score, mantener Microsoft Entra Connect, cribar alertas de Connect Health y supervisar agentes híbridos; indica que la puntuación se recalcula cada 24 h y que los componentes locales con 6 o más meses de retraso deben actualizarse. Secciones de identidad, autenticación y gobierno: cadencias no confirmadas. | 2023-10-23 | https://learn.microsoft.com/en-us/entra/architecture/ops-guide-intro |
| Identidades | Microsoft Entra (complementaria) | Microsoft Entra security operations guide | Sin cadencias calendarizadas: guía de supervisión y alertas continuas para cuentas de usuario, cuentas con privilegios, PIM, aplicaciones, dispositivos e infraestructura, con fuentes de registro e integración con SIEM. | 2026-03-26 | https://learn.microsoft.com/en-us/entra/architecture/security-operations-introduction |
| Detección y respuesta | Microsoft Defender XDR | Integrating Microsoft Defender XDR into your security operations (paso 6: SOC maintenance tasks) | Según integrate-microsoft-365-defender-secops-tasks (2026-08-07). Diaria: actualizar tickets de escalado del SOC; seguir la remediación de Defender Vulnerability Management. Semanal: revisar anuncios y Centro de mensajes; informe de Secure Score. Semanal y a demanda: coordinación con administración de servicios (CMDB, licencias, cambios); desplegar automatizaciones. Mensual y a demanda: actualizar campañas antiphishing y DLP con lecciones aprendidas. A demanda: ejercicio de simulación de incidentes. Sin cadencia trimestral. | 2026-08-07 | https://learn.microsoft.com/en-us/defender-xdr/integrate-microsoft-365-defender-secops |
| Correo y colaboración | Microsoft Defender for Office 365 | Microsoft Defender for Office 365 Security Operations Guide | Diaria: cribar e investigar incidentes en Defender XDR; gestionar envíos de falsos positivos y negativos; Tenant Allow/Block List; liberar cuarentena; revisar campañas con correo entregado. Semanal: tendencias de detección y flujo de correo; Threat analytics; usuarios más atacados y cuentas prioritarias; principales campañas. A demanda: investigación con Threat Explorer, búsqueda proactiva, reglas de detección personalizadas. A demanda/mensual: revisar directivas con Configuration analyzer, anulaciones de detección e información de suplantación. | 2026-07-03 | https://learn.microsoft.com/en-us/defender-office-365/mdo-sec-ops-guide |
| Dispositivos | Microsoft Defender for Endpoint | Microsoft Defender for Endpoint Security Operations Guide | Diaria: Centro de actividades; cola de incidentes; falsos positivos y negativos; amenazas de alto impacto en Threat analytics; salud del sensor EDR y del antivirus. Semanal: Centro de mensajes; Threat analytics; estado de gestión de vulnerabilidades; informes de reducción de superficie de ataque; protección web. Mensual: novedades del producto; dispositivos excluidos de directivas. Periódica (sin frecuencia fija): exclusiones, configuración de directivas, automatización, detecciones personalizadas y supresiones. | 2026-05-22 | https://learn.microsoft.com/en-us/defender-endpoint/mde-sec-ops-guide |
| Identidades | Microsoft Defender for Identity | Microsoft Defender for Identity operational guide | Diaria: cribar incidentes; reglas de ajuste de alertas; panel Identity Security; búsqueda proactiva; problemas de estado. Semanal: recomendaciones de Secure Score; amenazas emergentes; búsqueda proactiva. Mensual: revisar alertas ajustadas; novedades. Trimestral/a demanda: estado del servicio; que el alta de servidores incluya sensores; configuración del dominio con PowerShell. | 2026-06-14 | https://learn.microsoft.com/en-us/defender-for-identity/ops-guide/ops-guide |
| Aplicaciones y SaaS | Microsoft Defender for Cloud Apps | Microsoft Defender for Cloud Apps operational guide | Diaria: alertas e incidentes, detección de amenazas, app governance, Conditional Access app control, shadow IT (cloud discovery) y protección de la información. Semanal: postura de seguridad SaaS; estado de conectores, recopiladores de registros y agente SIEM; novedades; registro de gobierno. Mensual: evaluaciones de directivas y registros de actividad. A demanda: estado del servicio, búsqueda avanzada, cuarentenas, puntuaciones de riesgo de aplicaciones, informes de cloud discovery. | 2026-06-14 | https://learn.microsoft.com/en-us/defender-cloud-apps/ops-guide/ops-guide |
| SIEM y automatización | Microsoft Sentinel | Microsoft Sentinel operational guide | Diaria: cribar e investigar incidentes; consultas de búsqueda y marcadores; estado de reglas de análisis; estado de conectores e ingesta; Azure Monitor Agent; fallos de playbooks. Semanal: actualizaciones del Content hub; auditoría de actividad de Microsoft Sentinel. Mensual: accesos de usuarios e inactivos; retención del área de trabajo de Log Analytics. Sin cadencia trimestral. | 2026-04-22 | https://learn.microsoft.com/en-us/azure/sentinel/ops-guide |
| Nube | Microsoft Defender for Cloud | Planning and operations guide | Sin tabla de cadencias. Solo menciona consultar la inteligencia de amenazas en las operaciones diarias; el resto es continuo o «regular»: revisar recomendaciones, supervisar recursos nuevos o modificados y deriva de configuración, y atender alertas por etapas. | 2026-06-17 | https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-cloud-planning-and-operations-guide |
| Datos | Microsoft Purview (protección de la información y DLP) | Deploy an information protection solution with Microsoft Purview (complementaria: Plan for data loss prevention (DLP)) | Sin cadencias calendarizadas; es guía de despliegue, no de operación: ciclo iterativo conocer-proteger-prevenir y despliegue en fases. «Plan for data loss prevention» (dlp-overview-plan-for-dlp, 2026-06-26) propone modo simulación, luego simulación con avisos y después aplicación, con supervisión de informes y revisiones «regulares» sin frecuencia concreta. | 2026-03-31 | https://learn.microsoft.com/en-us/purview/information-protection-solution |
| Dispositivos | Microsoft Intune | Microsoft Intune planning guide (no es guía de operación) | No propone cadencias operativas: siete pasos de planificación de la adopción. No se localizó guía de operación oficial de Intune (ver silencios). | 2026-05-28 | https://learn.microsoft.com/en-us/intune/fundamentals/planning-guide |

Cinco productos tienen una guía oficial con cadencias explícitas: Defender for Office 365, Defender for Endpoint, Defender for Identity, Defender for Cloud Apps y Microsoft Sentinel; Defender XDR las incluye en su guía de integración con las operaciones de seguridad. Intune y Purview no tienen una guía de operación oficial con cadencias, y las de Defender for Cloud y de Entra no traen una tabla de cadencias. En esos dominios, las tareas de esta edición son una propuesta.

## 4. 325 tareas en ocho dominios

| Dominio | Diaria | Diaria/Semanal | Semanal | Mensual | Trimestral | Semestral | Anual | Por evento | Según necesidad | Total |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Aplicaciones y SaaS | 10 | 0 | 10 | 10 | 0 | 0 | 0 | 7 | 0 | 37 |
| Correo y colaboración | 13 | 0 | 9 | 9 | 4 | 1 | 1 | 8 | 1 | 46 |
| Datos | 21 | 0 | 20 | 15 | 8 | 2 | 3 | 12 | 1 | 82 |
| Detección y respuesta | 9 | 1 | 9 | 7 | 4 | 2 | 3 | 5 | 1 | 41 |
| Dispositivos | 9 | 0 | 7 | 7 | 4 | 0 | 1 | 6 | 1 | 35 |
| Identidades | 7 | 1 | 8 | 5 | 4 | 0 | 2 | 5 | 1 | 33 |
| Nube | 3 | 0 | 7 | 5 | 4 | 0 | 0 | 3 | 1 | 23 |
| SIEM y automatización | 5 | 0 | 8 | 7 | 4 | 0 | 0 | 3 | 1 | 28 |
| Total | 77 | 2 | 78 | 65 | 32 | 5 | 10 | 49 | 7 | 325 |

180 tareas provienen del plano B de TheNextCISO GM-24 V7.1, que instancia siete dominios sobre las guías oficiales. Las otras 145 provienen de 12 guías de excelencia operacional del autor: las 37 del dominio de aplicaciones y SaaS, y 108 que agregan a los demás dominios lo que el plano B no tenía. De esas 108, 47 son de riesgo interno y de ciclo de vida de los datos, y provienen de las guías 17 y 16 del repositorio del autor. El dominio de nube no tiene una guía del autor. Las cadencias semestral y anual provienen de esas guías: el plano B no las usa.

Las guías del autor describen más tareas de las que se agregaron: 379 en total. Las que ya estaban cubiertas por una fila no se duplicaron; la fila indica en qué guía está el procedimiento. El detalle está en el documento M10 «Guías de excelencia operacional del autor: qué aportan y cómo se incorporaron».

## 5. 69 prácticas independientes de la plataforma

Cada tarea de GM-24 indica la práctica que ejemplifica. La tarea de producto cambia cuando cambia el producto; la práctica no. Es el puente entre el plano B y el núcleo: si la organización cambia de herramienta, conserva la práctica y reescribe la tarea.

Las tareas de riesgo interno y de ciclo de vida de los datos también indican su práctica. 23 de esas prácticas son nuevas y tienen identificadores PR-RI y PR-CV: están descritas, con su rutina y su evidencia mínima, en el documento 16 del núcleo, «Prácticas de operación: riesgo interno y ciclo de vida de los datos». Las tareas tomadas de los borradores de las otras diez guías no tienen práctica asignada.

| ID | Práctica | Tipo | Tareas | Dominios donde aparece |
|---|---|---|:--:|---|
| OP-SOP-10 | Triar incidentes por prioridad dentro del SLA | Operación | 7 | Correo y colaboración · Datos · Detección y respuesta · Dispositivos · Identidades · Nube · SIEM y automatización |
| OP-SOP-11 | Investigar y remediar incidentes con evidencia | Operación | 13 | Correo y colaboración · Datos · Detección y respuesta · Dispositivos · Identidades · Nube |
| OP-SOP-15 | Analizar causa raíz de errores de detección | Operación | 5 | Correo y colaboración · Datos · Detección y respuesta · Dispositivos · Identidades |
| OP-POS-19 | Vigilar la postura de datos y su uso por IA | Postura | 2 | Datos |
| OP-POS-15 | Mantener la salud de la ingesta de señales | Postura | 7 | Datos · Detección y respuesta · Dispositivos · Identidades · SIEM y automatización |
| OP-POS-20 | Promover políticas de protección de datos de simulación a producción con evidencia | Postura | 2 | Datos |
| OP-POS-11 | Reportar la postura y su tendencia | Postura | 6 | Correo y colaboración · Datos · Detección y respuesta · Identidades · Nube |
| OP-POS-21 | Reducir la sobrecompartición de información sensible | Postura | 2 | Datos |
| OP-SOP-02 | Buscar amenazas por técnicas priorizadas y convertir hallazgos en detecciones | Operación | 6 | Correo y colaboración · Datos · Detección y respuesta · Dispositivos · Identidades · SIEM y automatización |
| OP-SIG-10 | Vigilar cambios de la plataforma y evaluar impacto | Señales y cambios | 8 | Correo y colaboración · Datos · Detección y respuesta · Dispositivos · Identidades · Nube · SIEM y automatización |
| OP-SIG-12 | Revisar políticas y excepciones del control | Señales y cambios | 8 | Correo y colaboración · Datos · Detección y respuesta · Dispositivos · Nube · SIEM y automatización |
| OP-POS-13 | Revisar y depurar excepciones que debilitan la detección | Postura | 6 | Correo y colaboración · Datos · Detección y respuesta · Dispositivos · Identidades · Nube |
| OP-SOP-30 | Investigar riesgo interno con proporcionalidad y privacidad | Señales y cambios | 5 | Datos · Identidades |
| OP-SIG-13 | Reportar resultados del SOC a la dirección | Señales y cambios | 6 | Datos · Detección y respuesta · Dispositivos · Identidades · Nube · SIEM y automatización |
| OP-AYI-01 | Recertificar accesos privilegiados, no humanos y de agentes | Acceso e identidad | 9 | Correo y colaboración · Datos · Detección y respuesta · Dispositivos · Identidades · Nube · SIEM y automatización |
| OP-POS-16 | Mantener el inventario de fuentes de señal | Postura | 8 | Datos · Detección y respuesta · Dispositivos · Nube · SIEM y automatización |
| OP-SOP-26 | Probar los planes de respuesta | Operación | 7 | Correo y colaboración · Datos · Detección y respuesta · Dispositivos · Identidades · Nube · SIEM y automatización |
| OP-SOP-27 | Supervisar la remediación automatizada | Operación | 2 | Detección y respuesta · Dispositivos |
| OP-SOP-20 | Revisar inteligencia de amenazas y derivar acciones | Operación | 4 | Correo y colaboración · Detección y respuesta · Dispositivos · SIEM y automatización |
| OP-SOP-19 | Revisar tendencias de detección y ajustar políticas | Postura | 5 | Correo y colaboración · Datos · Detección y respuesta · Dispositivos |
| OP-POS-17 | Priorizar y seguir la remediación de vulnerabilidades por riesgo | Postura | 2 | Dispositivos |
| OP-POS-12 | Detectar y corregir deriva de configuración frente al baseline | Postura | 7 | Correo y colaboración · Detección y respuesta · Dispositivos · Identidades · Nube |
| OP-SOP-28 | Recolectar evidencia forense con autoridad y registro | Operación | 4 | Datos · Detección y respuesta · Dispositivos |
| OP-SOP-29 | Revisar el tablero de postura y riesgo del dominio | Operación | 1 | Identidades |
| OP-SOP-24 | Convertir hunting en detecciones automatizadas | Operación | 5 | Correo y colaboración · Detección y respuesta · Identidades · SIEM y automatización |
| OP-POS-18 | Evaluar el efecto de las políticas de acceso y ajustarlas | Postura | 1 | Identidades |
| OP-AYI-02 | Vigilar el riesgo de identidades no humanas | Acceso e identidad | 2 | Identidades |
| OP-AYI-03 | Mantener el inventario y la higiene de identidades privilegiadas | Acceso e identidad | 1 | Identidades |
| OP-POS-25 | Priorizar la reducción de exposición por rutas de ataque | Postura | 1 | Nube |
| OP-POS-26 | Gobernar la remediación de recomendaciones con dueño y fecha | Postura | 2 | Nube |
| OP-POS-27 | Sostener el cumplimiento regulatorio de la nube con evidencia | Postura | 2 | Nube |
| OP-SOP-22 | Mantener la automatización operativa | Operación | 5 | Correo y colaboración · Datos · Detección y respuesta · Nube · SIEM y automatización |
| OP-POS-24 | Gobernar el costo de ingesta y retención | Postura | 5 | Nube · SIEM y automatización |
| OP-SOP-12 | Cerrar incidentes con criterio documentado | Operación | 2 | Correo y colaboración · Detección y respuesta |
| OP-SOP-13 | Clasificar incidentes para aprender patrones | Operación | 2 | Correo y colaboración · Detección y respuesta |
| OP-SOP-14 | Retroalimentar al fabricante con FP/FN | Operación | 1 | Correo y colaboración |
| OP-SOP-16 | Mantener listas de bloqueo con vencimiento | Operación | 1 | Correo y colaboración |
| OP-SOP-17 | Liberar cuarentena con segunda aprobación | Operación | 1 | Correo y colaboración |
| OP-SOP-18 | Remediar mensajes residentes | Operación | 2 | Correo y colaboración |
| OP-SOP-21 | Proteger cuentas prioritarias | Postura | 2 | Correo y colaboración |
| OP-POS-14 | Afinar protección contra suplantación | Postura | 1 | Correo y colaboración |
| OP-SIG-11 | Convertir lecciones del SOC en concientización | Señales y cambios | 3 | Correo y colaboración · Datos · Detección y respuesta |
| OP-SOP-23 | Curar y compartir consultas de hunting | Operación | 1 | Correo y colaboración |
| OP-SOP-25 | Mantener trazabilidad de escalamientos | Operación | 3 | Correo y colaboración · Datos · Detección y respuesta |
| OP-POS-22 | Auditar cambios de la plataforma de detección y automatización | Postura | 1 | SIEM y automatización |
| OP-POS-23 | Medir y cerrar la cobertura de detección por técnica | Postura | 2 | SIEM y automatización |
| PR-RI-01 | Supervisar, medir y probar los controles que se endurecen según el riesgo de la persona | Postura | 3 | Datos |
| PR-RI-02 | Verificar la seudonimización y revisar quién accedió a las alertas y a los casos | Señales y cambios | 1 | Datos |
| PR-RI-03 | Mantener al día los grupos de personas prioritarias y las barreras de información | Acceso e identidad | 1 | Datos |
| PR-RI-04 | Auditar de forma independiente el registro de actividad del programa | Señales y cambios | 1 | Datos |
| PR-RI-05 | Revisar el impacto en la privacidad y el encuadre laboral del programa | Señales y cambios | 1 | Datos |
| PR-RI-06 | Recertificar el estatuto de gobierno del programa con Legal, Recursos Humanos y privacidad | Señales y cambios | 1 | Datos |
| PR-CV-01 | Verificar que las reglas de retención están aplicadas y sin errores | Postura | 1 | Datos |
| PR-CV-03 | Revisar y aprobar la disposición dentro del plazo | Operación | 2 | Datos |
| PR-CV-04 | Conciliar los eventos de negocio que inician los plazos de retención | Operación | 2 | Datos |
| PR-CV-05 | Controlar las eliminaciones prioritarias con aprobación de varias partes | Operación | 2 | Datos |
| PR-CV-06 | Preservar la información de las personas que dejan la organización | Operación | 1 | Datos |
| PR-CV-07 | Vigilar la capacidad del almacenamiento de retención y de archivo | Postura | 3 | Datos |
| PR-CV-08 | Extender la retención a las interacciones con IA y a los agentes | Postura | 1 | Datos |
| PR-CV-09 | Muestrear la precisión de la clasificación automática de retención | Postura | 1 | Datos |
| PR-CV-10 | Mantener el alcance de las reglas: repositorios nuevos y atributos al día | Postura | 2 | Datos |
| PR-CV-11 | Revisar los intentos de alterar o eliminar registros protegidos | Operación | 1 | Datos |
| PR-CV-12 | Conservar la prueba de eliminación | Operación | 1 | Datos |
| PR-CV-13 | Sanear las retenciones sin fundamento vigente | Postura | 1 | Datos |
| PR-CV-14 | Reducir los datos redundantes, obsoletos y triviales antes de exponerlos a la IA | Postura | 1 | Datos |
| PR-CV-15 | Mantener la tabla de retención al día con la norma y con el negocio | Señales y cambios | 3 | Datos |
| PR-CV-16 | Probar que la retención prevalece sobre la eliminación | Operación | 1 | Datos |
| PR-CV-17 | Auditar los bloqueos irreversibles y los registros regulatorios | Señales y cambios | 1 | Datos |
| PR-CV-18 | Suspender la eliminación y preservar ante un litigio o una brecha | Operación | 1 | Datos |

## 6. Cómo instalar la operación en un dominio

1. **Designar al dueño del producto-control** del dominio (rol R22 del núcleo).
2. **Revisar las tareas** del dominio y quitar las que no aplican a lo desplegado.
3. **Asignar cada tarea**: equipo propio, proveedor, agente o una combinación. Anotar el responsable.
4. **Marcar qué se ejecuta hoy.** La hoja Resumen calcula el nivel de operación por cadencia y por dominio.
5. **Atar cada tarea a su evidencia**: qué queda registrado y dónde.
6. **Revisar cada semana** en la cadencia RT01 del núcleo, y cerrar los indicadores cada mes en RT05.

| Cadencia del núcleo | Qué se revisa de este dominio |
|---|---|
| RT01 · Revisión operativa de los controles (semanal) | Tareas diarias y semanales ejecutadas, pendientes y excepciones |
| RT04 · Revisión de servicio con cada proveedor crítico (mensual) | Tareas operadas por el proveedor y su evidencia |
| RT05 · Cierre de indicadores (mensual) | Indicadores de la tarea y del dominio |
| RT12 · Recertificación de accesos y de agentes (trimestral) | Permisos de los agentes que ejecutan tareas y su nivel de autonomía |
| RT15 · Diagnóstico completo (anual) | Vigencia de las tareas frente a las guías oficiales |

## 7. Tareas operadas por un proveedor o por un agente

- **Proveedor.** Si un servicio gestionado ejecuta las tareas, la lista de tareas es parte del contrato y cada una tiene su evidencia. El dueño interno verifica por muestreo. Aplica la versión externalizada de los resultados clave y de los indicadores del núcleo.
- **Agente.** Cada tarea de GM-24 trae una autonomía sugerida, de L0 a L4. Es una propuesta: un agente solo opera en el nivel cuya condición cumple, tiene identidad propia y un gestor humano.
- **Lo que no se delega.** Decidir qué excepción se acepta, qué automatización se aprueba y cuándo se escala.

| Nivel | Qué puede hacer | Condición para habilitarlo |
|:--:|---|---|
| L0 | Solo informa | Ficha del agente e identidad de lectura. |
| L1 | Propone; la persona ejecuta | Además, evaluación de calidad. |
| L2 | Propone y ejecuta tras aprobación humana registrada | Además, límites de lote, detención de emergencia probada y prueba adversarial. |
| L3 | Ejecuta acciones reversibles y de bajo impacto, con auditoría posterior por muestreo | Además, indicadores de riesgo con umbrales, revisión trimestral y autorización formal. |
| L4 | Autónomo con límites estrictos | No previsto en este plan. |

## 8. Las tareas, por dominio

### Aplicaciones y SaaS (37)

| ID | Tarea | Cadencia | Rol | Práctica | Autonomía | Indicador de la tarea | Procedimiento en las guías del autor |
|---|---|:--:|---|:--:|:--:|---|---|
| MDA-D01 | Revisión de Alertas e Incidentes | Diaria | Operaciones de seguridad | — | — | — | MDA DIARIA-01 |
| MDA-D02 | Análisis de Datos de Detección de Amenazas y Anomalías (UEBA) | Diaria | Operaciones de seguridad | — | — | — | MDA DIARIA-02 |
| MDA-D03 | Monitoreo de App Governance y Risk Scores de Aplicaciones OAuth | Diaria | Operaciones de seguridad | — | — | — | MDA DIARIA-03 |
| MDA-D04 | Verificación de Estado de Conditional Access App Control (CAAC) | Diaria | Operaciones de seguridad | — | — | — | MDA DIARIA-04 |
| MDA-D05 | Evaluación de Shadow IT y Cloud Discovery Dashboard | Diaria | Operaciones de seguridad | — | — | — | MDA DIARIA-05 |
| MDA-D06 | Inspección de Protección de Información y Triggers DLP | Diaria | Operaciones de seguridad | — | — | — | MDA DIARIA-06 |
| MDA-D07 | Validación de Salud de App Connectors y Log Collectors | Diaria | Operaciones de seguridad | — | — | — | MDA DIARIA-07 |
| MDA-D08 | Escalamiento de Incidentes No Resueltos | Diaria | Operaciones de seguridad | — | — | — | MDA DIARIA-08 |
| MDA-D09 | Actualización de Documentación de Incidentes (Audit Trail) | Diaria | Operaciones de seguridad | — | — | — | MDA DIARIA-09 |
| MDA-D10 | Comunicación de Hallazgos Críticos al Manager o CISO | Diaria | Operaciones de seguridad | — | — | — | MDA DIARIA-10 |
| MDA-S01 | Revisión de Recomendaciones SSPM (SaaS Security Posture Management) | Semanal | Operaciones de seguridad | — | — | — | MDA SEMANAL-01 |
| MDA-S02 | Seguimiento de Cambios y Actualizaciones en Microsoft Defender XDR | Semanal | Operaciones de seguridad | — | — | — | MDA SEMANAL-02 |
| MDA-S03 | Auditoría de Logs de Gobernanza y Efectividad de Políticas | Semanal | Operaciones de seguridad | — | — | — | MDA SEMANAL-03 |
| MDA-S04 | Verificación de Salud de Agentes SIEM e Integraciones | Semanal | Operaciones de seguridad | — | — | — | MDA SEMANAL-04 |
| MDA-S05 | Revisión de UEBA — User and Entity Behavior Analytics | Semanal | Operaciones de seguridad | — | — | — | MDA SEMANAL-05 |
| MDA-S06 | Prueba y Validación de Playbooks Automatizados | Semanal | Operaciones de seguridad | — | — | — | MDA SEMANAL-06 |
| MDA-S07 | Auditoría de Permisos de Apps y Acceso OAuth | Semanal | Operaciones de seguridad | — | — | — | MDA SEMANAL-07 |
| MDA-S08 | Revisión de Cumplimiento con Políticas Organizacionales | Semanal | Operaciones de seguridad | — | — | — | MDA SEMANAL-08 |
| MDA-S09 | Reporte Semanal de Tendencias de Incidentes | Semanal | Operaciones de seguridad | — | — | — | MDA SEMANAL-09 |
| MDA-S10 | Actualización de Matriz de Escalamiento y Procedimientos de Respuesta | Semanal | Operaciones de seguridad | — | — | — | MDA SEMANAL-10 |
| MDA-M01 | Evaluación de Efectividad y Enforcement de Políticas | Mensual | Operaciones de seguridad | — | — | — | MDA MENSUAL-01 |
| MDA-M02 | Revisión de Activity Logs y Acciones de Gobernanza | Mensual | Operaciones de seguridad | — | — | — | MDA MENSUAL-02 |
| MDA-M03 | Análisis de Tendencias de Incidentes y Ajuste de Controles | Mensual | Operaciones de seguridad | — | — | — | MDA MENSUAL-03 |
| MDA-M04 | Actualización de Documentación de Arquitectura de Seguridad | Mensual | Operaciones de seguridad | — | — | — | MDA MENSUAL-04 |
| MDA-M05 | Revisión de Integración con Otras Herramientas de Seguridad | Mensual | Operaciones de seguridad | — | — | — | MDA MENSUAL-05 |
| MDA-M06 | Validación de Mecanismos de Reporting al CISO y Board | Mensual | Operaciones de seguridad | — | — | — | MDA MENSUAL-06 |
| MDA-M07 | Presentación Mensual de Postura de Seguridad al Board/CISO | Mensual | Operaciones de seguridad | — | — | — | MDA MENSUAL-07 |
| MDA-M08 | Revisión y Renovación de Licencias y Subscriptions | Mensual | Operaciones de seguridad | — | — | — | MDA MENSUAL-08 |
| MDA-M09 | Ejercicios Tabletop para Respuesta a Incidentes | Mensual | Operaciones de seguridad | — | — | — | MDA MENSUAL-09 |
| MDA-M10 | Actualización de Materiales de Entrenamiento para Personal SOC | Mensual | Operaciones de seguridad | — | — | — | MDA MENSUAL-10 |
| MDA-A01 | Respuesta a Amenazas Emergentes o Incidentes Zero-Day | Por evento | Operaciones de seguridad | — | — | — | MDA AD-HOC-01 |
| MDA-A02 | Investigación Completa de Incidente de Exfiltración (IR Playbook) | Por evento | Operaciones de seguridad | — | — | — | MDA AD-HOC-02 |
| MDA-A03 | Implementación de Nuevas Features de Seguridad | Por evento | Operaciones de seguridad | — | — | — | MDA AD-HOC-03 |
| MDA-A04 | Atención a Hallazgos de Auditoría de Cumplimiento | Por evento | Operaciones de seguridad | — | — | — | MDA AD-HOC-04 |
| MDA-A05 | Coordinación con Agencias Externas para Threat Intelligence | Por evento | Operaciones de seguridad | — | — | — | MDA AD-HOC-05 |
| MDA-A06 | Revisión de Cuarentena de Archivos | Por evento | Operaciones de seguridad | — | — | — | MDA AD-HOC-06 |
| MDA-A07 | Generación de Reportes Ejecutivos de Cloud Discovery | Por evento | Operaciones de seguridad | — | — | — | MDA AD-HOC-07 |

### Correo y colaboración (46)

| ID | Tarea | Cadencia | Rol | Práctica | Autonomía | Indicador de la tarea | Procedimiento en las guías del autor |
|---|---|:--:|---|:--:|:--:|---|---|
| MDO-D01 | Triar incidentes de la cola (Medium/High de Defender for Office 365) | Diaria | Security Operations Team | OP-SOP-10 | L2 | KPI-01 | MDO D-1 |
| MDO-D02 | Investigar y ejecutar acciones de respuesta sobre incidentes | Diaria | Security Operations Team | OP-SOP-11 | L2 | KPI-02 | — |
| MDO-D03 | Resolver incidentes remediados | Diaria | Security Operations Team | OP-SOP-12 | L2 | KPI-01 | — |
| MDO-D04 | Clasificar incidentes (true/false; tipo de amenaza) | Diaria | Security Operations Team | OP-SOP-13 | L2 | KPI-03 | — |
| MDO-D05 | Enviar FP/FN a Microsoft (Submissions) | Diaria | Security Operations Team | OP-SOP-14 | L2 | KPI-04 | — |
| MDO-D06 | Analizar detalles de los envíos | Diaria | Security Operations Team | OP-SOP-15 | L1 | KPI-04 | MDO D-3 |
| MDO-D07 | Agregar bloqueos en Tenant Allow/Block List | Diaria | Security Operations Team | OP-SOP-16 | L2 | KPI-05 | MDO A-3 |
| MDO-D08 | Liberar falsos positivos de cuarentena | Diaria | Security Operations Team | OP-SOP-17 | L2 | KPI-04 | MDO D-4 |
| MDO-D09 | Revisar campañas con correo entregado y remover mensajes | Diaria | Security Operations Team | OP-SOP-18 | L2 | KPI-02 | MDO D-6 |
| MDO-W01 | Revisar informes de tendencias de detección | Semanal | Security Operations Team | OP-SOP-19 | L3 | KPI-08 | MDO S-2 |
| MDO-W02 | Revisar amenazas activas en Threat analytics | Semanal | Security Operations Team | OP-SOP-20 | L2 | KPI-08 | MDO S-3 |
| MDO-W03 | Revisar usuarios más atacados y cuentas prioritarias | Semanal | Security Operations Team | OP-SOP-21 | L2 | KPI-09 | MDO D-9 |
| MDO-W04 | Revisar Campaign Views | Semanal | Security Operations Team | OP-SOP-18 | L2 | KPI-02 | XDR 4.8 |
| MDO-W05 | Generar informe de Secure Score | Semanal | Security Administration | OP-POS-11 | L3 | KPI-06 | MDO M-1 |
| MDO-W06 | Revisar anuncios del Message Center | Semanal | Security Administration | OP-SIG-10 | L3 | KPI-10 | — |
| MDO-W07 | Desplegar/probar automatización aprobada | Semanal | Security Operations Team | OP-SOP-22 | L1 | KPI-16 | — |
| MDO-M01 | Revisar configuración con Configuration Analyzer/ORCA | Mensual | Security Administration | OP-POS-12 | L3 | KPI-06 | MDO S-4; XDR 5.10 |
| MDO-M02 | Revisar overrides de detección | Mensual | Security Administration | OP-POS-13 | L2 | KPI-07 | MDO S-9; MDO M-3; XDR 5.2 |
| MDO-M03 | Revisar Spoof intelligence e Impersonation insights | Mensual | Security Administration | OP-POS-14 | L2 | KPI-07 | MDO S-5; MDO M-2 |
| MDO-M04 | Actualizar concientización con lecciones del SOC | Mensual | Security Operations Team | OP-SIG-11 | L1 | KPI-09 | — |
| MDO-Q01 | Revisar políticas, excepciones y apetito de autonomía | Trimestral | PO-GAC + CISO | OP-SIG-12 | L1 | KPI-10 | — |
| MDO-Q02 | Revisar desempeño y costo de la flota | Trimestral | PO-GAC | — | L1 | KPI-11..15 | — |
| MDO-Q03 | Recertificar accesos de agentes y humanos | Trimestral | PO-GAC + IAM | OP-AYI-01 | L2 | KPI-17 | — |
| MDO-Q04 | Evaluaciones/regresión y red teaming de agentes | Trimestral | PO-GAC + AppSec | — | L2 | KPI-13 | — |
| MDO-A01 | Investigar/remover correo a pedido o disparar AIR | Por evento | Security Operations Team | OP-SOP-11 | L2 | KPI-02 | MDO A-2 |
| MDO-A02 | Hunting proactivo | Por evento | Threat hunting team | OP-SOP-02 | L1 | KPI-08 | MDO S-1 |
| MDO-A03 | Compartir consultas de hunting | Por evento | Threat hunting team | OP-SOP-23 | L2 | KPI-08 | — |
| MDO-A04 | Crear detecciones personalizadas | Por evento | Threat hunting team | OP-SOP-24 | L2 | KPI-08 | MDO A-6 |
| MDO-A05 | Revisar cuentas prioritarias y etiquetas | Por evento | Security Administration | OP-SOP-21 | L2 | KPI-09 | MDO S-8 |
| MDO-A06 | Actualizar tickets ITSM | Diaria | Security Operations Team | OP-SOP-25 | L3 | KPI-01 | — |
| MDO-A07 | Tabletop (incl. 'agente comprometido') | Según necesidad | SOC Oversight | OP-SOP-26 | L1 | KPI-16 | MDO An-2 |
| GMDO-D-5 | Gestión de Entidades Restringidas (Restricted Users) | Diaria | Security Operator | — | — | — | MDO D-5 |
| GMDO-D-7 | Validación de Detecciones ZAP | Diaria | Security Operator | — | — | — | MDO D-7 |
| GMDO-D-8 | Verificación de Patrones de Envío Sospechosos (BEC Detection) | Diaria | Security Operator · Incident Responder | — | — | — | MDO D-8 |
| GMDO-S-7 | Auditoría de Reglas de Transporte (Mail Flow Rules) | Semanal | Security Administrator | — | — | — | MDO S-7 |
| GMDO-S-10 | Reporte Semanal al Manager | Semanal | Incident Responder · Gerente SOC | — | — | — | MDO S-10 |
| GMDO-M-4 | Auditoría de Políticas de Cuarentena | Mensual | Security Administrator | — | — | — | MDO M-4 |
| GMDO-M-5 | Programa de Attack Simulation Training — Análisis y Planificación Mensual | Mensual | Security Administrator · Manager | — | — | — | MDO M-5; MDO S-6; MDO Sem-2; XDR 7.5 |
| GMDO-M-7 | Análisis de Tendencias de User Reporting (Efectividad como Sensores) | Mensual | Security Administrator · Manager | — | — | — | MDO M-7 |
| GMDO-M-9 | Backup de Políticas de Seguridad (PowerShell Automation) | Mensual | Architect · Security Administrator | — | — | — | MDO M-9 |
| GMDO-M-10 | Informe Ejecutivo Mensual al CISO y Board | Mensual | Manager · CISO | — | — | — | MDO M-10 |
| GMDO-Sem-1 | Recalibración de Postura de Seguridad | Semestral | Operaciones de seguridad | — | — | — | MDO Sem-1 |
| GMDO-An-1 | Revisión del Programa Operativo Completo | Anual | Operaciones de seguridad | — | — | — | MDO An-1 |
| GMDO-A-1 | Respuesta a Brote de Phishing/Malware (Outbreak Response) | Por evento | Operaciones de seguridad | — | — | — | MDO A-1; XDR 8.2 |
| GMDO-A-4 | Message Trace — Investigación Forense de Entrega | Por evento | Incident Responder · Security Operator | — | — | — | MDO A-4 |
| GMDO-A-5 | Búsqueda de Auditoría — Actividades Administrativas Sospechosas | Por evento | Incident Responder · Security Administrator | — | — | — | MDO A-5 |

### Datos (82)

| ID | Tarea | Cadencia | Rol | Práctica | Autonomía | Indicador de la tarea | Procedimiento en las guías del autor |
|---|---|:--:|---|:--:|:--:|---|---|
| DP-D01 | Triar alertas DLP (High/Medium) e Insider Risk correlacionadas; clasificar y resolver | Diaria | Information Protection Analyst | OP-SOP-10 | L2 | % High ≤4 h | ENT 2.8; MIP D-01; MIP D-03; DLP 8.1-1; IRM D-02; IRM D-05 |
| DP-D02 | Investigar alertas DLP (Activity/Content explorer); decidir acción | Diaria | Information Protection Investigator | OP-SOP-11 | L2 | MTTR; revertidas <2 % | MIP D-06; DLP 8.1-2; DLP 8.2-3 |
| DP-D03 | Gestionar FP DLP: coincidencias de SIT, umbrales, excepciones con vencimiento; simulación antes de bloquear | Diaria | Information Protection Admin | OP-SOP-15 | L2 | FP recurrentes ↓ | MIP S-01 |
| DP-D04 | Revisar DSPM / DSPM for AI: uso de datos sensibles por Copilot y agentes, prompts riesgosos | Diaria | Data Security Management | OP-POS-19 | L3 | Recomendaciones críticas abiertas | — |
| DP-D05 | Revisar salud de la clasificación: auto-labeling, scanner, conectores MDA | Diaria | Information Protection Admin | OP-POS-15 | L3 | Políticas en error = 0 | MIP M-06 |
| DP-W01 | Revisar simulación de auto-etiquetado y DLP en prueba; proponer producción | Semanal | Information Protection Admin + data owners | OP-POS-20 | L2 | Políticas promovidas | MIP S-03 |
| DP-W02 | Revisar cobertura de etiquetado y tendencia | Semanal | Information Protection Analyst | OP-POS-11 | L3 | Cobertura ≥90 % | MIP S-02 |
| DP-W03 | Revisar sobrecompartición: 'Anyone', externos, sitios sensibles | Semanal | Information Protection Analyst + SharePoint admin | OP-POS-21 | L2 | 'Anyone' en sensibles = 0 | MIP D-05 |
| DP-W04 | Hunting sobre CloudAppEvents / EmailEvents: egress, descargas masivas, etiquetas degradadas | Semanal | Investigator | OP-SOP-02 | L1 | Hunts | MIP D-02; DLP 8.2-1; IRM S-04 |
| DP-W05 | Revisar Message Center y novedades de Purview | Semanal | Information Protection Admin | OP-SIG-10 | L3 | Cambios evaluados ≤7 días | DLP 8.5-5 |
| DP-W06 | Revisar file policies de MDA (SaaS) y acciones de gobierno | Semanal | Information Protection Admin + SecOps | OP-POS-21 | L2 | Archivos expuestos en SaaS ↓ | — |
| DP-M01 | Revisar taxonomía de etiquetas y políticas de publicación con dueños de negocio | Mensual | Information Protection Admin + data owners | OP-SIG-12 | L1 | Taxonomía vigente | MIP M-01 |
| DP-M02 | Revisar excepciones DLP y overrides de usuario con vencimiento | Mensual | Information Protection Admin | OP-POS-13 | L2 | Overrides sin justificación = 0 | DLP 8.2-2; DLP 8.2-4; DLP 8.4-2 |
| DP-M03 | Revisar políticas de Insider Risk con Privacidad/Legal; casos abiertos | Mensual | IRM Admin + Privacidad | OP-SOP-30 | L1 | Casos en SLA | DLP 8.3-4; IRM M-02 |
| DP-M04 | Informe mensual de protección de datos para CISO y CDO | Mensual | Data Security Management | OP-SIG-13 | L3 | Informe a tiempo | MIP M-04; MIP M-09; DLP 8.3-1; DLP 8.4-4 |
| DP-M05 | Revisar Compliance Manager: acciones de mejora y evidencias | Mensual | Compliance Administrator | OP-POS-11 | L3 | Acciones cerradas | ENT 4.6; MIP M-10; SEN 5.8 |
| DP-M06 | Revisar fuentes de conocimiento y DLP para IA de las flotas (todos los dominios) | Mensual | Information Protection Admin + PO-GAC de cada dominio | — | L2 | Fuentes no aprobadas = 0 | — |
| DP-Q01 | Revisar política de protección de datos, apetito y mapa de datos sensibles | Trimestral | PO-GAC Datos + CISO + CDO | OP-SIG-12 | L1 | Decisiones registradas | DLP 8.4-1; DLP 8.4-5 |
| DP-Q02 | Revisar desempeño y costo de la flota Datos | Trimestral | PO-GAC Datos | — | L1 | KPIs vs. meta | IRM M-04 |
| DP-Q03 | Recertificar roles de Purview y permisos de agentes | Trimestral | PO-GAC + IAM | OP-AYI-01 | L2 | % recertificados | MIP S-09; IRM M-05; DLM M-05 |
| DP-Q04 | Evaluaciones/regresión y red teaming (fuga de datos en salidas, evasión de DLP) | Trimestral | PO-GAC + AppSec | — | L2 | % evaluados | DLP 8.4-3 |
| DP-A01 | Respuesta a fuga de datos: alcance, quitar compartición, cuarentena, revocar, notificar (Legal) | Por evento | Investigator + SecOps + Legal | OP-SOP-11 | L2 | Tiempo a contención | MIP AH-A; MIP AH-B; MIP AH-C; MIP AH-D; MIP AH-E |
| DP-A02 | Descubrimiento y etiquetado de un nuevo repositorio (on-prem, SaaS, Azure Storage) | Por evento | Information Protection Admin | OP-POS-16 | L2 | Repositorios sin descubrir ↓ | — |
| DP-A03 | Alta de etiqueta/SIT/clasificador y su política (simulación → producción) | Por evento | Information Protection Admin + data owners | OP-POS-20 | L2 | Políticas promovidas | — |
| DP-A04 | Tabletop de fuga de datos / insider (incl. 'agente filtra datos') | Según necesidad | PO-GAC Datos + Legal + CSIRT | OP-SOP-26 | L1 | Ejercicios/año | MIP M-05; DLP 8.5-2 |
| GMIP-D-04 | Validación de Accesos a Contenido Cifrado (Azure Rights Management) | Diaria | Operaciones de seguridad | — | — | — | MIP D-04; MIP D-09; MIP S-04 |
| GMIP-D-08 | Validación de Cambios Administrativos del Día Anterior | Diaria | Operaciones de seguridad | — | — | — | MIP D-08; MIP M-03; DLM D-02 |
| GMIP-S-05 | Pruebas de Acceso Controlado a Datos Altamente Sensibles | Semanal | Operaciones de seguridad | — | — | — | MIP S-05 |
| GMIP-S-08 | Validación de Cobertura de Logging de Purview | Semanal | Operaciones de seguridad | — | — | — | MIP S-08 |
| GMIP-S-10 | Reporte Semanal de Postura de Seguridad de Datos | Semanal | Operaciones de seguridad | — | — | — | MIP S-10 |
| GMIP-M-02 | Evaluación de Efectividad del Cifrado Persistente | Mensual | Operaciones de seguridad | — | — | — | MIP M-02 |
| GDLP-8.1-3 | Verificar salud de sensores Endpoint DLP: cobertura del agente MDE y sincronización de políticas (~1 hora desde cambio) | Diaria | Operaciones de seguridad | — | — | — | DLP 8.1-3; DLP 8.3-3 |
| GDLP-8.3-2 | Actualización de datasets EDM si la fuente de datos cambió | Mensual | Operaciones de seguridad | — | — | — | DLP 8.3-2 |
| GDLP-8.3-5 | Revisión del estado de clasificadores entrenables: verificar que la precisión no haya degradado por cambios en el corpus documental | Mensual | Operaciones de seguridad | — | — | — | DLP 8.3-5 |
| GDLP-8.5-1 | Revisión estratégica del programa: alcance de cobertura vs. riesgo residual aceptado | Anual | Operaciones de seguridad | — | — | — | DLP 8.5-1 |
| GIRM-D-01 | Verificación de salud de conectores de señales (HR Data, Physical Badging y endpoints) | Diaria | Insider Risk Management Admins | OP-POS-15 | — | Disponibilidad y Frescura de Conectores Críticos (HR y Endpoints) · meta de la guía: >= 99% | IRM D-01 |
| GIRM-D-03 | Análisis contextual de secuencias y exfiltración acumulada en Activity Explorer | Diaria | Insider Risk Management Analysts / Investigators | OP-SOP-30 | — | Tasa de Verdaderos Positivos por Política (Signal-to-Noise Ratio) · meta de la guía: >= 65% | IRM D-03 |
| GIRM-D-04 | Monitoreo diario de alertas de Risky AI Usage y Risky Agents (Preview) | Diaria | Insider Risk Management Analysts (perfil irrestricto) | OP-POS-19 | — | Continuidad del Alert Triage Agent y Cobertura de Políticas IA / Agentes · meta de la guía: 100% | IRM D-04 |
| GIRM-D-06 | Supervisión operativa de usuarios en nivel Elevated bajo Adaptive Protection | Diaria | Insider Risk Management Analysts / Investigators | PR-RI-01 | — | Efectividad de Contención Automática (Adaptive Protection) · meta de la guía: >= 95% | IRM D-06 |
| GIRM-D-07 | Verificación diaria de seudonimización e inspección del Insider Risk Audit Log independiente | Diaria | Insider Risk Management Auditors | PR-RI-02 | — | Cumplimiento de Privacidad, Segregación SoD y Doble Autorización Forense · meta de la guía: 100% | IRM D-07 |
| GIRM-D-08 | Evaluación independiente de solicitudes de doble autorización en Forensic Evidence | Diaria | Insider Risk Management Approvers (Legal / DPO / RR. HH.) | OP-SOP-28 | — | Cumplimiento de Privacidad, Segregación SoD y Doble Autorización Forense · meta de la guía: 100% | IRM D-08 |
| GIRM-S-01 | Gestión de casos activos, cadena de custodia en Case Notes e inspección en Content Explorer | Semanal | Insider Risk Management Investigators | OP-SOP-30 | — | Tiempo Medio de Escalamiento Defensible a Purview eDiscovery · meta de la guía: <= 8 horas | IRM S-01 |
| GIRM-S-02 | Chequeo semanal de salud de políticas (Policy Health Check) y advertencias pendientes | Semanal | Insider Risk Management Admins | OP-SIG-12 | — | Tasa de Verdaderos Positivos por Política (Signal-to-Noise Ratio) · meta de la guía: >= 65% | IRM S-02 |
| GIRM-S-03 | Calibración de umbrales (Tuning), variantes de indicadores y Detection Groups | Semanal | Insider Risk Management Admins | OP-SOP-19 | — | Tasa de Verdaderos Positivos por Política (Signal-to-Noise Ratio) · meta de la guía: >= 65% | IRM S-03 |
| GIRM-S-05 | Actualización de Priority User Groups y alineación con Information Barriers | Semanal | Insider Risk Management Admins (irrestricto) | PR-RI-03 | — | — | IRM S-05 |
| GIRM-S-06 | Verificación de automatizaciones Power Automate y conector Microsoft Sentinel | Semanal | Ingeniero SOAR / Insider Risk Management Admins | OP-SOP-22 | — | — | IRM S-06 |
| GIRM-M-01 | Exportación y auditoría independiente del Insider Risk Audit Log (previo a purga de 180 días) | Mensual | Insider Risk Management Auditors (Auditoría Interna / DPO) | PR-RI-04 | — | Cumplimiento de Privacidad, Segregación SoD y Doble Autorización Forense · meta de la guía: 100% | IRM M-01 |
| GIRM-M-03 | Revisión mensual de efectividad preventiva de Adaptive Protection (DLP + Entra CA + DLCM) | Mensual | Arquitecto Zero Trust + IRM Admins + Conditional Access Admin | PR-RI-01 | — | Efectividad de Contención Automática (Adaptive Protection) · meta de la guía: >= 95% | IRM M-03 |
| GIRM-T-01 | Revisión trimestral de Evaluación de Impacto de Privacidad (DPIA) y cumplimiento laboral | Trimestral | DPO + Asesoría Legal Laboral + IRM Admins | PR-RI-05 | — | Cumplimiento de Privacidad, Segregación SoD y Doble Autorización Forense · meta de la guía: 100% | IRM T-01 |
| GIRM-T-02 | Prueba end-to-end de Adaptive Protection y sincronización bidireccional con Defender XDR | Trimestral | Arquitecto SecOps + Ingeniería Purview y Entra ID | PR-RI-01 | — | Efectividad de Contención Automática (Adaptive Protection) · meta de la guía: >= 95% | IRM T-02 |
| GIRM-SM-01 | Análisis semestral de lecciones aprendidas de casos cerrados y efectividad conductual | Semestral | CISO + Líder IRM + RR. HH. + Concientización | OP-SIG-11 | — | Tasa de Corrección Conductual Post-Notificación (Notices) · meta de la guía: >= 85% | IRM SM-01 |
| GIRM-A-01 | Recertificación anual del Estatuto Tripartito y simulacro ejecutivo de robo de IP | Anual | CISO, General Counsel, CHRO, DPO y SOC Manager | PR-RI-06 | — | Cumplimiento de Privacidad, Segregación SoD y Doble Autorización Forense · meta de la guía: 100% | IRM A-01 |
| GIRM-AH-01 | Investigación urgente de robo de propiedad intelectual por usuario saliente o prioritario | Por evento | Insider Risk Management Investigators + Legal + RR. HH. | OP-SOP-30 | — | Tiempo Medio de Triaje de Alertas Críticas (MTTA - High Severity) · meta de la guía: <= 4 horas hábiles (100% < 24 h) | IRM AH-01 |
| GIRM-AH-02 | Activación controlada de captura visual Forensic Evidence con doble autorización | Por evento | IRM Admins + IRM Approvers + IRM Investigators | OP-SOP-28 | — | Cumplimiento de Privacidad, Segregación SoD y Doble Autorización Forense · meta de la guía: 100% | IRM AH-02 |
| GIRM-AH-03 | Escalamiento formal de caso confirmado hacia Microsoft Purview eDiscovery (Premium) | Por evento | Insider Risk Management Investigators -> eDiscovery Manager (Legal) | OP-SOP-25 | — | Tiempo Medio de Escalamiento Defensible a Purview eDiscovery · meta de la guía: <= 8 horas | IRM AH-03 |
| GIRM-AH-05 | Contención de exposición sensible en IA generativa o agentes autónomos (Risky AI / Risky Agents) | Por evento | IRM Investigator + Administrador de Seguridad IA | OP-SOP-11 | — | Continuidad del Alert Triage Agent y Cobertura de Políticas IA / Agentes · meta de la guía: 100% | IRM AH-05 |
| GDLM-D-01 | Monitoreo de estado de distribución y errores en políticas de retención y etiquetas | Diaria | Administrador DLCM (View-Only / Retention Manager) | PR-CV-01 | — | Cobertura de Cargas de Trabajo con Directiva Base (Incluyendo IA) · meta de la guía: 100% | DLM D-01 |
| GDLM-D-03 | Seguimiento de cola activa de revisiones de disposición próximas a vencer o auto-aprobarse | Diaria | Records Manager | PR-CV-03 | — | Cumplimiento de SLA en Revisiones de Disposición · meta de la guía: >= 95% (0 ítems > 30 días) | DLM D-03 |
| GDLM-D-04 | Conciliación diaria de eventos transaccionales en Event-Based Retention | Diaria | Records Manager / Ingeniero GRC | PR-CV-04 | — | Conciliación de Eventos y Asset ID en Event-Based Retention · meta de la guía: >= 99% | DLM D-04 |
| GDLM-D-05 | Supervisión de alertas y ejecuciones activas de Priority Cleanup | Diaria | Oficial de Cumplimiento / SOC L2 | PR-CV-05 | — | Integridad de Cambios Administrativos y Priority Cleanup · meta de la guía: 100% | DLM D-05 |
| GDLM-D-06 | Verificación de conversión a Inactive Mailboxes en bajas críticas de personal | Diaria | Administrador Exchange / Analista IAM | PR-CV-06 | — | Reducción de Deuda de Retención en Exempleados · meta de la guía: Reducción sostenida hasta 0 retenciones infinitas sin causa legal | DLM D-06 |
| GDLM-D-07 | Monitoreo de cuotas en Recoverable Items y Auto-Expanding Archives hasta 3 TB | Diaria | Administrador Exchange Online | PR-CV-07 | — | — | DLM D-07 |
| GDLM-D-08 | Verificación de políticas de retención y Collection Policies para Copilot y aplicaciones IA | Diaria | Administrador DLCM / Especialista Seguridad IA | PR-CV-08 | — | Cobertura de Cargas de Trabajo con Directiva Base (Incluyendo IA) · meta de la guía: 100% | DLM D-08 |
| GDLM-S-01 | Muestreo de precisión en políticas de auto-aplicación de etiquetas y Cloud Attachments | Semanal | Records Manager / Ingeniero DLCM | PR-CV-09 | — | Precisión en Políticas de Auto-Aplicación de Etiquetas · meta de la guía: >= 92% | DLM S-01 |
| GDLM-S-02 | Auditoría de membresía dinámica e higiene de atributos en Adaptive Policy Scopes | Semanal | Administrador DLCM | PR-CV-10 | — | Cobertura de Cargas de Trabajo con Directiva Base (Incluyendo IA) · meta de la guía: 100% | DLM S-02 |
| GDLM-S-03 | Ejecución de mesas semanales de revisión de disposición multi-etapa (etapas 1 a 5) | Semanal | Disposition Reviewers y Records Manager | PR-CV-03 | — | Cumplimiento de SLA en Revisiones de Disposición · meta de la guía: >= 95% (0 ítems > 30 días) | DLM S-03 |
| GDLM-S-04 | Monitoreo de crecimiento en Preservation Hold Libraries y paso a Microsoft 365 Archive | Semanal | Administrador SharePoint / FinOps / DLCM Lead | PR-CV-07 | — | — | DLM S-04 |
| GDLM-S-05 | Revisión de intentos bloqueados o remoción administrativa de etiquetas en Records | Semanal | Analista SOC L2 / Records Manager | PR-CV-11 | — | Integridad de Cambios Administrativos y Priority Cleanup · meta de la guía: 100% | DLM S-05 |
| GDLM-S-06 | Gobernanza de ciclo de vida sobre nuevos sitios M365, Teams y agentes Copilot Studio | Semanal | Ingeniero de Gobierno de Datos | PR-CV-10 | — | Cobertura de Cargas de Trabajo con Directiva Base (Incluyendo IA) · meta de la guía: 100% | DLM S-06 |
| GDLM-M-01 | Exportación, conciliación y archivo firmado de Proof of Disposal | Mensual | Records Manager | PR-CV-12 | — | Completitud de Resguardo Mensual de Proof of Disposal · meta de la guía: 100% (12/12 meses) | DLM M-01 |
| GDLM-M-02 | Medición y saneamiento de deuda de retención en Inactive Mailboxes y OneDrive | Mensual | Oficial de Cumplimiento / Administrador Exchange | PR-CV-13 | — | Reducción de Deuda de Retención en Exempleados · meta de la guía: Reducción sostenida hasta 0 retenciones infinitas sin causa legal | DLM M-02 |
| GDLM-M-03 | Evaluación de superficie ROT pre-IA y verificación de purga en SubstrateHolds | Mensual | Data Governance Lead / Arquitecto Seguridad IA | PR-CV-14 | — | Tasa de Minimización de Datos ROT Pre-IA · meta de la guía: >= 85% anual | DLM M-03 |
| GDLM-M-04 | Conciliación mensual de registros basados en eventos sin Asset ID o con evento omitido | Mensual | Records Manager y Dueños de Proceso | PR-CV-04 | — | Conciliación de Eventos y Asset ID en Event-Based Retention · meta de la guía: >= 99% | DLM M-04 |
| GDLM-T-01 | Revisión integral del File Plan frente a cambios normativos y simplificación de series | Trimestral | Comité de Retención (Records Manager, Legal, DPO, CISO) | PR-CV-15 | — | — | DLM T-01 |
| GDLM-T-02 | Prueba controlada de los 4 principios de precedencia y validación de registros migrados | Trimestral | Arquitecto Purview + Equipo Legal (eDiscovery) | PR-CV-16 | — | — | DLM T-02 |
| GDLM-SM-01 | Auditoría de Preservation Lock, Regulatory Records y holgura de límites del tenant | Semestral | Auditoría Interna + CISO + Oficial de Cumplimiento | PR-CV-17 | — | Integridad de Cambios Administrativos y Priority Cleanup · meta de la guía: 100% | DLM SM-01 |
| GDLM-A-01 | Recertificación ejecutiva de la Tabla de Retención (ISO 15489-1), RACI y simulacro tabletop | Anual | CISO, General Counsel, DPO y Comité Ejecutivo | PR-CV-15 | — | — | DLM A-01 |
| GDLM-AH-01 | Ejecución de Priority Cleanup ante derrame crítico de datos sensibles (Data Spillage) | Por evento | Tríada Priority Cleanup + SOC | PR-CV-05 | — | Integridad de Cambios Administrativos y Priority Cleanup · meta de la guía: 100% | DLM AH-01 |
| GDLM-AH-02 | Congelamiento inmediato de disposición y aplicación de eDiscovery Hold ante litigio o brecha | Por evento | eDiscovery Manager (Legal) + Records Manager | PR-CV-18 | — | — | DLM AH-02 |
| GDLM-AH-03 | Respuesta ante desactivación o alteración maliciosa de políticas de retención | Por evento | SOC L2/L3 + Ingeniero Senior Purview | OP-SOP-11 | — | Integridad de Cambios Administrativos y Priority Cleanup · meta de la guía: 100% | DLM AH-03 |
| GDLM-AH-04 | Incorporación masiva de nueva regulación o entidad adquirida (M&A) al File Plan | Por evento | Arquitecto de Gobierno + Records Manager + Legal | PR-CV-15 | — | Cobertura de Cargas de Trabajo con Directiva Base (Incluyendo IA) · meta de la guía: 100% | DLM AH-04 |
| GDLM-AH-05 | Remediación de emergencia por saturación de Recoverable Items o Preservation Hold Library | Por evento | Administrador Exchange / SharePoint + DLCM Lead | PR-CV-07 | — | — | DLM AH-05 |

### Detección y respuesta (41)

| ID | Tarea | Cadencia | Rol | Práctica | Autonomía | Indicador de la tarea | Procedimiento en las guías del autor |
|---|---|:--:|---|:--:|:--:|---|---|
| XDR-D01 | Triar la cola de incidentes unificada (todas las fuentes; High/Medium primero) | Diaria | Monitoring (Tier 1-2) | OP-SOP-10 | L2 | % H/M triados en SLA | XDR 3.1; XDR 3.3; ENT 2.1; ENT 2.10 |
| XDR-D02 | Investigar incidentes correlacionados y ejecutar/aprobar acciones de respuesta | Diaria | Monitoring (Tier 2) + CSIRT | OP-SOP-11 | L2 | MTTR por severidad | ENT 2.2 |
| XDR-D03 | Revisar el Action center: acciones pendientes y ejecutadas (AIR) | Diaria | Monitoring + Engineering | OP-SOP-27 | L2 | Pendientes >4 h = 0 | MDO D-2; XDR 3.2 |
| XDR-D04 | Clasificar incidentes y resolver los remediados | Diaria | Monitoring | OP-SOP-13 | L2 | % clasificados | — |
| XDR-D05 | Gestionar FP/FN y tuning de alertas en todos los sensores | Diaria | Monitoring + Security Administration | OP-SOP-15 | L2 | Alertas suprimidas con justificación | XDR 3.5 |
| XDR-D06 | Revisar salud de sensores (EDR/AV, MDI, conectores de apps) | Diaria | Security Administration | OP-POS-15 | L3 | % EDR saludable; MDI issues = 0 | XDR 3.4; XDR 3.6 |
| XDR-D07 | Revisar Threat analytics de alto impacto y derivar acciones | Diaria/Semanal | Threat Intelligence & Analytics | OP-SOP-20 | L2 | Acciones derivadas | — |
| XDR-D08 | Actualizar tickets de escalamiento (ITSM) y notificaciones | Diaria | Todos los equipos SOC | OP-SOP-25 | L3 | Tickets sincronizados | ENT 2.9 |
| XDR-W01 | Hunting proactivo cross-domain y guided hunting para Tier 1 | Semanal | Monitoring (Tier 2-3) + TI | OP-SOP-02 | L1 | Hunts/semana | XDR 4.1; XDR 8.4; ENT 3.1 |
| XDR-W02 | Crear/revisar detecciones personalizadas y automation rules | Semanal | Engineering & SecOps | OP-SOP-24 | L2 | Detecciones vigentes; precisión | XDR 4.2 |
| XDR-W03 | Revisar Secure Score y Exposure Management; alimentar backlog | Semanal | SOC Monitoring + Security Administration | OP-POS-11 | L3 | Secure Score por producto | XDR 4.5; XDR 5.7; MDE 5.1; MDI M3; ENT 4.1 |
| XDR-W04 | Revisar informes de amenazas y protección | Semanal | Monitoring + Security Administration | OP-SOP-19 | L3 | Informe semanal | ENT 3.3; SEN 4.1 |
| XDR-W05 | Revisar Message Center y novedades; evaluar impacto | Semanal | SOC Oversight | OP-SIG-10 | L3 | Cambios evaluados ≤7 días | XDR 5.13 |
| XDR-W06 | Desplegar/probar automatizaciones aprobadas; verificar conectividad SIEM | Semanal | Engineering & SecOps | OP-SOP-22 | L1 | Automatizaciones probadas | MDO M-6; MDO Sem-3; XDR 4.9; XDR 5.8; XDR 8.6; MIP M-08 |
| XDR-M01 | Revisar niveles de automatización por grupo de dispositivos y políticas de alertas | Mensual | Security Administration + SOC Oversight | OP-POS-12 | L2 | Grupos fuera de baseline = 0 | — |
| XDR-M02 | Revisar Unified RBAC: roles, permisos y asignaciones de humanos y agentes | Mensual | SOC Oversight + IAM | OP-AYI-01 | L2 | Asignaciones sin justificación = 0 | MDO M-8; XDR 5.6 |
| XDR-M03 | Revisar alertas tuned/suprimidas y reglas sin coincidencias | Mensual | Security Administration | OP-POS-13 | L2 | Reglas obsoletas retiradas | XDR 5.4; ENT 4.3 |
| XDR-M04 | Informe mensual de seguridad para el CISO | Mensual | SOC Oversight | OP-SIG-13 | L3 | Informe a tiempo | XDR 5.1; ENT 4.9 |
| XDR-M05 | Actualizar entrenamiento del SOC con lecciones; ejercicios Blue/Red/Purple | Mensual | SOC Oversight | OP-SIG-11 | L1 | Ejercicios realizados | DLP 8.5-4 |
| XDR-Q01 | Revisar casos de uso del SOC, playbooks del CSIRT y modelo de amenazas por sensor | Trimestral | SOC Oversight + CSIRT + TI | OP-SIG-12 | L1 | Casos de uso vigentes | XDR 6.2; MDE 4.2; MDE 7.2; ENT 4.2; SEN 5.7 |
| XDR-Q02 | Revisar desempeño y costo de la flota de agentes XDR | Trimestral | PO-GAC | — | L1 | KPIs vs. meta | — |
| XDR-Q03 | Recertificar accesos de humanos y agentes (Unified RBAC + Entra Agent ID) | Trimestral | PO-GAC + IAM | OP-AYI-01 | L2 | % recertificados | — |
| XDR-Q04 | Evaluaciones/regresión y red teaming de agentes; service health; setup de sensores | Trimestral | PO-GAC + AppSec + Security Administration | — | L2 | % agentes evaluados | — |
| XDR-A01 | Responder a incidentes mayores con el CSIRT (aislar, revocar, deshabilitar, contener) | Por evento | CSIRT + Monitoring | OP-SOP-11 | L2 | Tiempo a contención | MDO A-7; XDR 8.1; ENT 5.1; ENT 5.2; ENT 5.6; SEN 6 |
| XDR-A02 | Live response / recolección de paquetes de investigación | Por evento | Tier 3 / CSIRT | OP-SOP-28 | L1 | Paquetes con registro | ENT 5.5 |
| XDR-A03 | Crear incidentes/alertas manuales; fusionar o dividir incidentes | Por evento | Monitoring | OP-SOP-12 | L2 | Incidentes manuales trazados | — |
| XDR-A04 | Onboarding/offboarding de dispositivos y fuentes; device discovery | Por evento | Engineering & SecOps | OP-POS-16 | L2 | Dispositivos no onboarded | — |
| XDR-A05 | Tabletop / Purple team cross-domain (incl. 'agente comprometido') | Según necesidad | SOC Oversight + CSIRT | OP-SOP-26 | L1 | Ejercicios/año | XDR 7.3; XDR 8.7; ENT 4.5 |
| GXDR-3.7 | Registro de Métricas Diarias | Diaria | Operaciones de seguridad | — | — | — | XDR 3.7; MIP D-10 |
| GXDR-3.8 | Hand-over entre Turnos | Diaria | Operaciones de seguridad | — | — | — | XDR 3.8; MDO D-10; SEN 3.8 |
| GXDR-4.3 | Revisión de Incidentes Cerrados (Post-Incident Review Semanal) | Semanal | Operaciones de seguridad | — | — | — | XDR 4.3; MIP S-06; SEN 4.7 |
| GXDR-4.4 | Evaluación de Configuraciones (Configuration Drift) | Semanal | Operaciones de seguridad | — | — | — | XDR 4.4 |
| GXDR-4.10 | Revisión de SLAs Operativos y Actualización de Runbooks | Semanal | Operaciones de seguridad | — | — | — | XDR 4.10 |
| GXDR-5.9 | Auditoría de Funcionalidades y ROI Review | Mensual | Operaciones de seguridad | — | — | — | XDR 5.9; MDO An-3; XDR 6.5 |
| GXDR-5.11 | Validación de Backups y Recuperación | Mensual | Operaciones de seguridad | — | — | — | XDR 5.11 |
| GXDR-6.1 | Revisión de Roles y Responsabilidades (SOC Governance) | Semestral | Operaciones de seguridad | — | — | — | XDR 6.1 |
| GXDR-6.7 | Revisión de Coordinación con Stakeholders | Semestral | Operaciones de seguridad | — | — | — | XDR 6.7 |
| GXDR-7.1 | Revisión Completa del Programa (Full Program Review) | Anual | Operaciones de seguridad | — | — | — | XDR 7.1 |
| GXDR-7.2 | Reevaluación Estratégica de Postura (Strategic Posture Reassessment) | Anual | Operaciones de seguridad | — | — | — | XDR 7.2 |
| GXDR-7.4 | Auditoría Externa y Compliance | Anual | Operaciones de seguridad | — | — | — | XDR 7.4; XDR 8.3; DLP 8.5-3 |
| GXDR-8.5 | Despliegue de Nuevas Funcionalidades | Por evento | Operaciones de seguridad | — | — | — | XDR 8.5 |

### Dispositivos (35)

| ID | Tarea | Cadencia | Rol | Práctica | Autonomía | Indicador de la tarea | Procedimiento en las guías del autor |
|---|---|:--:|---|:--:|:--:|---|---|
| EP-D01 | Revisar acciones automáticas y manuales en el Action center | Diaria | Security Operations Team | OP-SOP-27 | L2 | Pendientes >4 h = 0 | MDE 3.1 |
| EP-D02 | Triar incidentes de la cola con alertas de MDE y resolver remediados | Diaria | Security Operations Team | OP-SOP-10 | L2 | % H/M en SLA | MDE 3.2; INT 1.4; ENT 2.5 |
| EP-D03 | Gestionar FP/FN: indicadores, exclusiones, envíos; causa (ASR, AV, EDR) | Diaria | Security Operations Team | OP-SOP-15 | L2 | FP recurrentes ↓ | MDE 3.3 |
| EP-D04 | Revisar Threat analytics de alto impacto y derivar acciones | Diaria | Security Operations Team | OP-SOP-20 | L2 | Acciones derivadas | — |
| EP-D05 | Revisar salud de dispositivos (AV signature/platform/engine, EDR sensor) | Diaria | Security Administration Team | OP-POS-15 | L3 | % saludables ≥98 % | MDE 3.4 |
| EP-D06 | Investigar incidentes de endpoint y ejecutar/aprobar acciones (aislar, restringir, scan, paquete) | Diaria | Tier 2-3 + CSIRT | OP-SOP-11 | L2 | MTTR; aislamientos revertidos <2 % | — |
| EP-W01 | Revisar Message Center (MDE/Intune) y evaluar impacto | Semanal | General | OP-SIG-10 | L3 | Cambios evaluados ≤7 días | — |
| EP-W02 | Revisar threat protection report y tendencias | Semanal | Security Operations Team | OP-SOP-19 | L3 | Informe semanal | MDE 4.1 |
| EP-W03 | Revisar Defender Vulnerability Management: nuevas vulnerabilidades, recomendaciones, exposure score; solicitudes a Intune | Semanal | Security Administration Team + IT | OP-POS-17 | L2 | CVEs críticos ≤7 días | XDR 4.6; MDE 3.6; MDE 4.4; MDE 5.3 |
| EP-W04 | Revisar ASR rules report y proponer paso de audit a block | Semanal | Security Administration Team | OP-POS-12 | L2 | % reglas en block | XDR 5.3; MDE 3.5 |
| EP-W05 | Revisar web protection / network protection y custom indicators | Semanal | Security Administration Team | OP-SOP-19 | L3 | Bloqueos; indicadores vigentes | MDE 6.4 |
| EP-W06 | Hunting proactivo sobre Device* y detecciones personalizadas | Semanal | Tier 2-3 | OP-SOP-02 | L1 | Hunts; hallazgos→detecciones | — |
| EP-M01 | Revisar device groups, niveles de automatización y RBAC por grupo | Mensual | Security Administration + SOC Oversight | OP-POS-12 | L2 | Grupos fuera de baseline = 0 | MDE 4.3 |
| EP-M02 | Revisar baselines de Intune y su deriva | Mensual | Security Administration + IT | OP-POS-12 | L2 | No conformes ↓ | INT 2.1; INT 2.3; INT 3.2; INT 4.3 |
| EP-M03 | Revisar device discovery: no gestionados y de red; plan de onboarding | Mensual | Engineering & SecOps | OP-POS-16 | L2 | No gestionados ↓ | XDR 5.5; MDE 4.6 |
| EP-M04 | Informe mensual de seguridad de endpoints | Mensual | SOC Oversight | OP-SIG-13 | L3 | Informe a tiempo | MDE 5.2 |
| EP-M05 | Revisar indicadores y exclusiones con vencimiento; retirar obsoletos | Mensual | Security Administration | OP-POS-13 | L2 | Sin vencimiento = 0 | MDE 4.5 |
| EP-Q01 | Revisar política de endpoints, excepciones y apetito de autonomía | Trimestral | PO-GAC Endpoints + CISO | OP-SIG-12 | L1 | Decisiones registradas | MDE 7.3 |
| EP-Q02 | Revisar desempeño y costo de la flota Endpoints | Trimestral | PO-GAC Endpoints | — | L1 | KPIs vs. meta | — |
| EP-Q03 | Recertificar accesos (Unified RBAC por device group; Agent ID) | Trimestral | PO-GAC + IAM | OP-AYI-01 | L2 | % recertificados | MDE 7.1 |
| EP-Q04 | Evaluaciones/regresión y red teaming de agentes; prueba de reversión de aislamiento | Trimestral | PO-GAC + AppSec | — | L2 | % evaluados | — |
| EP-A01 | Respuesta a incidente mayor: aislamiento masivo acotado, restricción, offboarding | Por evento | CSIRT | OP-SOP-11 | L2 | Tiempo a contención | MDE 6.3; INT 4.1 |
| EP-A02 | Live response / recolección de paquetes | Por evento | Tier 3 / CSIRT | OP-SOP-28 | L1 | Paquetes con registro | MDE 6.1; MDE 6.2 |
| EP-A03 | Onboarding/offboarding de dispositivos; grupos y tags | Por evento | Engineering & SecOps | OP-POS-16 | L2 | No onboarded | — |
| EP-A04 | Bloquear aplicación vulnerable (TVM) o mitigación alternativa | Por evento | Security Administration + IT | OP-POS-17 | L2 | Apps bloqueadas | — |
| EP-A05 | Tabletop ransomware/dispositivo comprometido (incl. 'agente comprometido') | Según necesidad | SOC Oversight + CSIRT | OP-SOP-26 | L1 | Ejercicios/año | MDE 5.5; MDE 8.3 |
| GMDE-5.4 | Prueba End-to-End del Pipeline de Detección | Mensual | Operaciones de seguridad | — | — | — | MDE 5.4 |
| GMDE-8.1 | Métricas Anuales de Desempeño del Programa | Anual | Operaciones de seguridad | — | — | — | MDE 8.1; MDE 8.2 |
| GMDE-6.5 | Coordinar con Microsoft Threat Experts | Por evento | Operaciones de seguridad | — | — | — | MDE 6.5 |
| GINT-1.1 | Supervisar el cumplimiento de los dispositivos y el estado de las líneas base de seguridad | Diaria | Operaciones de seguridad | — | — | — | INT 1.1; INT 3.1 |
| GINT-1.2 | Revisar Endpoint analytics para identificar riesgos en dispositivos Windows | Diaria | Operaciones de seguridad | — | — | — | INT 1.2 |
| GINT-1.3 | Supervisar la inscripción automática de dispositivos y sus notificaciones | Diaria | Operaciones de seguridad | — | — | — | INT 1.3 |
| GINT-2.2 | Detectar dispositivos inactivos y aplicar reglas de limpieza | Semanal | Operaciones de seguridad | — | — | — | INT 2.2 |
| GINT-3.3 | Verificar el uso de las funciones de seguridad: firewall, BitLocker y reducción de la superficie de ataque | Mensual | Operaciones de seguridad | — | — | — | INT 3.3 |
| GINT-4.2 | Actualizar términos y condiciones o directivas de acceso | Por evento | Operaciones de seguridad | — | — | — | INT 4.2 |

### Identidades (33)

| ID | Tarea | Cadencia | Rol | Práctica | Autonomía | Indicador de la tarea | Procedimiento en las guías del autor |
|---|---|:--:|---|:--:|:--:|---|---|
| ID-D01 | Revisar el Identity Security dashboard | Diaria | SOC analysts + IAM admins | OP-SOP-29 | L3 | Insights revisados | MDI D1 |
| ID-D02 | Triar incidentes de identidad por prioridad y resolver remediados | Diaria | SOC analysts | OP-SOP-10 | L2 | % H/M en SLA | MDI D2; MDI D3 |
| ID-D03 | Investigar risky users / sign-ins; confirmar o descartar; remediar o dejar que CA auto-remedie | Diaria | SOC analysts | OP-SOP-11 | L2 | Risky users High ≤4 h | ENT 2.3; ENT 3.5; ENT 6.2 |
| ID-D04 | Configurar reglas de tuning para benign true positives de MDI | Diaria | SOC analysts + Security admins | OP-SOP-15 | L2 | Reglas con vencimiento | MDI W1 |
| ID-D05 | Revisar salud de sensores MDI | Diaria | Security admins | OP-POS-15 | L3 | Health issues = 0 | MDI D5 |
| ID-D06 | Hunting proactivo sobre identidad | Diaria/Semanal | SOC analysts | OP-SOP-02 | L1 | Hunts | MDI D6; MDI W3 |
| ID-W01 | Revisar Secure Score y posture assessments; alimentar backlog | Semanal | Security admins + SOC | OP-POS-11 | L3 | Secure Score ↑ | MDI W2; MDI M1 |
| ID-W02 | Responder a amenazas emergentes con detecciones personalizadas | Semanal | Security admins + SOC | OP-SOP-24 | L2 | Detecciones vigentes | — |
| ID-W03 | Revisar efectos de Conditional Access (report-only) y proponer ajustes | Semanal | IAM admins + SOC | OP-POS-18 | L2 | Report-only → on | ENT 6.3 |
| ID-W04 | Revisar riesgo de identidades de carga de trabajo (SPs, agentes) | Semanal | IAM admins + PO-GAC | OP-AYI-02 | L2 | NHI sin dueño = 0 | — |
| ID-W05 | Revisar Message Center y novedades | Semanal | Security admins | OP-SIG-10 | L3 | Cambios evaluados ≤7 días | MDI M5 |
| ID-M01 | Revisar alertas tuned y retirar reglas sin coincidencias | Mensual | Security admins + SOC | OP-POS-13 | L2 | Reglas obsoletas retiradas | XDR 5.12; MDI M2 |
| ID-M02 | Revisar cuentas sensibles, inactivas, admins sin PIM | Mensual | IAM admins | OP-AYI-03 | L2 | Admins fuera de PIM = 0 | XDR 4.7; MDI M4; ENT 4.4; ENT 6.4.1 |
| ID-M03 | Informe mensual de identidad para el CISO | Mensual | Security admins | OP-SIG-13 | L3 | Informe a tiempo | MDI M6 |
| ID-M04 | Revisar baseline de CA y excepciones (break-glass) con vencimiento | Mensual | IAM admins + SOC Oversight | OP-POS-12 | L2 | Exclusiones justificadas | XDR 6.4 |
| ID-Q01 | Revisar service health, setup de sensores y configuración de dominio | Trimestral | Security admins | OP-POS-15 | L1 | Hallazgos cerrados | XDR 6.6; MDI Q1; MDI Q2 |
| ID-Q02 | Revisar desempeño y costo de la flota Identidades | Trimestral | PO-GAC Identidades | — | L1 | KPIs vs. meta | — |
| ID-Q03 | Recertificación de accesos (humanos, grupos privilegiados, agentes) | Trimestral | IAM + PO-GAC | OP-AYI-01 | L2 | % a tiempo | ENT 6.5.1 |
| ID-Q04 | Evaluaciones/regresión y red teaming; prueba de bloqueo indebido y rollback | Trimestral | PO-GAC + AppSec | — | L2 | % evaluados | — |
| ID-A01 | Respuesta a compromiso de identidad: revocar, reset, deshabilitar, bloquear por CA | Por evento | SOC + IAM | OP-SOP-11 | L2 | Tiempo a contención | MDI D4; MDI Q4; ENT 5.3 |
| ID-A02 | Investigación de insider risk correlacionada con riesgo de identidad | Por evento | SOC + Privacidad | OP-SOP-30 | L1 | Casos autorizados | IRM AH-04 |
| ID-A03 | Alta/baja de identidades de agentes (Entra Agent ID), sponsors y permisos | Por evento | IAM + PO-GAC | OP-AYI-02 | L2 | Agentes sin sponsor = 0 | — |
| ID-A04 | Tabletop de compromiso de identidad privilegiada (incl. 'agente comprometido') | Según necesidad | SOC Oversight + IAM | OP-SOP-26 | L1 | Ejercicios/año | MDI 8.1 |
| GMDI-W4 | Análisis de Lateral Movement Paths (LMP) | Semanal | Operaciones de seguridad | — | — | — | MDI W4 |
| GMDI-W5 | Auditoría de Protocolos Inseguros | Semanal | Operaciones de seguridad | — | — | — | MDI W5 |
| GMDI-8.2a | Capacity Planning de Sensores | Anual | Operaciones de seguridad | — | — | — | MDI 8.2a |
| GMDI-8.2b | Purple Team — Validación de Detección | Anual | Operaciones de seguridad | — | — | — | MDI 8.2b |
| GMDI-Q3 | Proceso de Servidor — Onboarding de Nuevos DCs | Por evento | Operaciones de seguridad | — | — | — | MDI Q3 |
| GENT-2.7 | Monitoreo de Actividades Privilegiadas (PIM / Entra) | Diaria | Privileged Role Administrator · Security Administrator | — | — | — | ENT 2.7; ENT 6.4.2; ENT 6.4.3 |
| GENT-6.1 | Gestión del Ciclo de Vida de Identidades | Diaria | Operaciones de seguridad | — | — | — | ENT 6.1 |
| GENT-3.7 | Revisión de Cambios en el Entorno (Change Management) | Semanal | Security Analyst (L2) · Change Advisory Board participant | — | — | — | ENT 3.7 |
| GENT-7.2 | Verificación de Apps y SSO | Mensual | Operaciones de seguridad | — | — | — | ENT 7.2 |
| GENT-5.4 | Offboarding de Emergencia (Lifecycle Workflows) | Por evento | Operaciones de seguridad | — | — | — | ENT 5.4 |

### Nube (23)

| ID | Tarea | Cadencia | Rol | Práctica | Autonomía | Indicador de la tarea | Procedimiento en las guías del autor |
|---|---|:--:|---|:--:|:--:|---|---|
| CL-D01 | Triar alertas de carga de trabajo en la cola unificada; correlar con XDR | Diaria | SOC analysts | OP-SOP-10 | L2 | % High ≤30 min | — |
| CL-D02 | Revisar attack paths nuevos/críticos; asignar dueño | Diaria | Security Admin + Plataforma | OP-POS-25 | L2 | Attack paths críticos >30 días = 0 | — |
| CL-D03 | Revisar recomendaciones nuevas de alto riesgo; asignar dueño/fecha (governance rules) | Diaria | Security Admin | OP-POS-26 | L2 | Críticas sin dueño = 0 | — |
| CL-W01 | Revisar secure score por suscripción/conector y tendencia | Semanal | Security Admin | OP-POS-11 | L3 | Score ↑ | — |
| CL-W02 | Revisar recomendaciones vencidas y notificar a dueños | Semanal | Security Admin | OP-POS-26 | L3 | Vencidas ≤5 % | — |
| CL-W03 | Revisar cumplimiento regulatorio y exenciones | Semanal | Cumplimiento + Security Admin | OP-POS-27 | L3 | Cumplimiento ≥90 % | — |
| CL-W04 | Revisar cobertura de planes Defender y recursos sin protección (incl. AI services) | Semanal | Security Admin + FinOps | OP-POS-16 | L3 | Críticas sin plan = 0 | — |
| CL-W05 | Revisar postura y alertas de recursos de IA (Defender for AI Services; AI-SPM) | Semanal | Security Admin + PO-GAC de dominios | — | L3 | Recomendaciones de IA críticas abiertas | — |
| CL-W06 | Verificar workflow automations y continuous export a Sentinel | Semanal | Security engineers | OP-SOP-22 | L2 | Fallidas = 0 | — |
| CL-W07 | Revisar release notes / Message Center; evaluar impacto | Semanal | Security Admin | OP-SIG-10 | L3 | Cambios evaluados ≤7 días | — |
| CL-M01 | Revisar governance rules y exenciones con vencimiento | Mensual | Security Admin + SOC Oversight | OP-POS-13 | L2 | Exenciones sin vencimiento = 0 | — |
| CL-M02 | Revisar costo (DWU, planes) y optimizar | Mensual | FinOps + Security Admin | OP-POS-24 | L3 | Desvío ≤10 % | — |
| CL-M03 | Revisar inventario cloud y conectores multicloud; recursos no evaluados | Mensual | Security Admin + Plataforma | OP-POS-16 | L2 | No evaluados ↓ | — |
| CL-M04 | Revisar hardening preventivo (deny/enforce, JIT) y su efecto | Mensual | Security Admin + Plataforma | OP-POS-12 | L2 | No conformes creados = 0 | — |
| CL-M05 | Informe mensual de postura cloud | Mensual | Security Admin | OP-SIG-13 | L3 | Informe a tiempo | — |
| CL-Q01 | Revisar estándares asignados, recomendaciones personalizadas y apetito (deny) | Trimestral | PO-GAC Nube + Cumplimiento + CISO | OP-SIG-12 | L1 | Decisiones registradas | — |
| CL-Q02 | Revisar desempeño y costo de la flota Nube | Trimestral | PO-GAC Nube | — | L1 | KPIs vs. meta | — |
| CL-Q03 | Recertificar roles (Security Admin/Reader, Owner/Contributor, cloud scopes) | Trimestral | PO-GAC + IAM | OP-AYI-01 | L2 | % recertificados | — |
| CL-Q04 | Evaluaciones/regresión de agentes; prueba de workflow automation en falla | Trimestral | PO-GAC + Security engineers | — | L2 | % evaluados | — |
| CL-A01 | Respuesta a alerta crítica de carga de trabajo; coordinar con XDR/Endpoints | Por evento | SOC + Plataforma | OP-SOP-11 | L2 | Tiempo a contención | — |
| CL-A02 | Onboarding de suscripción / cuenta AWS / proyecto GCP / Arc; asignar estándar y planes | Por evento | Security Admin + Plataforma | OP-POS-16 | L2 | Onboarded con planes | — |
| CL-A03 | Crear recomendación o estándar personalizado | Por evento | Security Admin | OP-POS-27 | L1 | Custom vigentes | — |
| CL-A04 | Tabletop de ruta de ataque explotada (incl. agente de IA como objetivo) | Según necesidad | PO-GAC Nube + CSIRT | OP-SOP-26 | L1 | Ejercicios/año | — |

### SIEM y automatización (28)

| ID | Tarea | Cadencia | Rol | Práctica | Autonomía | Indicador de la tarea | Procedimiento en las guías del autor |
|---|---|:--:|---|:--:|:--:|---|---|
| SI-D01 | Triar e investigar incidentes de Sentinel en el portal unificado | Diaria | SOC analysts | OP-SOP-10 | L2 | % H/M en SLA | SEN 3.1; SEN 3.2 |
| SI-D02 | Revisar salud de conectores y agentes AMA | Diaria | Sentinel admins | OP-POS-15 | L3 | Conectores en error = 0 | ENT 2.6; ENT 4.8; MIP D-07; SEN 3.5; SEN 3.6 |
| SI-D03 | Revisar/habilitar reglas analíticas nuevas; monitorear salud de reglas | Diaria | Security engineers | OP-SOP-24 | L2 | Reglas fallidas = 0 | SEN 3.4 |
| SI-D04 | Explorar hunting queries y bookmarks | Diaria | SOC analysts (Tier 2-3) | OP-SOP-02 | L1 | Hunts | SEN 4.4 |
| SI-D05 | Verificar ejecución de playbooks y automation rules | Diaria | Security engineers | OP-SOP-22 | L2 | Fallidos ≤24 h | ENT 2.4; SEN 3.3; SEN 4.6 |
| SI-W01 | Revisar Content hub (soluciones, reglas, workbooks, playbooks) | Semanal | Security engineers | OP-SIG-10 | L3 | Contenido evaluado | SEN 4.3 |
| SI-W02 | Auditar actividad de Sentinel (cambios de reglas, bookmarks, automatización) | Semanal | Sentinel admins | OP-POS-22 | L3 | Cambios no autorizados = 0 | — |
| SI-W03 | Revisar cobertura MITRE de reglas vs. técnicas priorizadas | Semanal | Security engineers + TI | OP-POS-23 | L3 | Cobertura ≥90 % | XDR 6.3; ENT 3.4; SEN 5.3 |
| SI-W04 | Revisar ingesta y costo vs. commitment tier | Semanal | Sentinel admins + FinOps | OP-POS-24 | L3 | Desvío ≤10 % | ENT 3.8 |
| SI-W05 | Revisar recomendaciones de SOC optimization | Semanal | Security engineers | OP-POS-23 | L2 | Recomendaciones tratadas | SEN 4.5; SEN 5.2 |
| SI-W06 | Revisar ingesta de TI y reglas de matching | Semanal | TI | OP-SOP-20 | L2 | Indicadores vigentes | ENT 3.9; SEN 3.7 |
| SI-M01 | Revisar accesos a Sentinel y Log Analytics; inactivos | Mensual | Sentinel admins + IAM | OP-AYI-01 | L2 | Inactivos removidos | SEN 5.4 |
| SI-M02 | Revisar retención y almacenamiento a largo plazo | Mensual | Sentinel admins | OP-POS-24 | L2 | Retención alineada | MIP M-07; SEN 5.6 |
| SI-M03 | Actualizar watchlists y revisar commitment tiers | Mensual | Security engineers + FinOps | OP-POS-24 | L2 | Watchlists al día | — |
| SI-M04 | Afinar DCRs y transformaciones de ingesta | Mensual | Security engineers | OP-POS-24 | L1 | Datos sin valor filtrados | — |
| SI-M05 | Informe mensual del SOC (eficiencia) para el CISO | Mensual | SOC Lead | OP-SIG-13 | L3 | Informe a tiempo | SEN 5.1 |
| SI-Q01 | Revisar casos de uso, supresión y apetito de automatización | Trimestral | SOC Lead + CISO | OP-SIG-12 | L1 | Decisiones registradas | — |
| SI-Q02 | Revisar desempeño y costo de la flota SIEM | Trimestral | PO-GAC SIEM | — | L1 | KPIs vs. meta | — |
| SI-Q03 | Recertificar roles de Sentinel/Logic Apps (humanos y agentes, incl. Sentinel MCP) | Trimestral | PO-GAC + IAM | OP-AYI-01 | L2 | % recertificados | — |
| SI-Q04 | Evaluaciones/regresión de agentes y pruebas de playbooks en escenarios de falla | Trimestral | PO-GAC + Security engineers | — | L2 | % evaluados | ENT 3.6; SEN 5.5 |
| SI-A01 | Onboarding de una fuente de datos (conector, DCR, parser, reglas, costo) | Por evento | Security engineers | OP-POS-16 | L1 | Fuentes onboarded | — |
| SI-A02 | Crear/modificar regla analítica o automation rule (prueba, versión, aprobación) | Por evento | Security engineers | OP-SOP-24 | L2 | Reglas versionadas | — |
| SI-A03 | Migración al portal de Defender (antes del 31-mar-2027) | Por evento | Sentinel admins | OP-SIG-10 | L1 | Hito cumplido | — |
| SI-A04 | Tabletop de pérdida de visibilidad | Según necesidad | SOC Lead | OP-SOP-26 | L1 | Ejercicios/año | — |
| GSEN-4.2 | Revisión y Tuning de Reglas Analíticas | Semanal | Operaciones de seguridad | — | — | — | SEN 4.2; ENT 3.2; MIP S-07 |
| GSEN-4.8 | Reporte Semanal a Stakeholders | Semanal | Operaciones de seguridad | — | — | — | SEN 4.8; ENT 3.10 |
| GSEN-5.9 | Revisión de Arquitectura SOC | Mensual | Operaciones de seguridad | — | — | — | SEN 5.9; ENT 4.7 |
| GSEN-5.10 | Roadmap de Mejoras del SOC | Mensual | Operaciones de seguridad | — | — | — | SEN 5.10; ENT 4.10 |

## 9. Guías de excelencia operacional del autor

Además de las guías oficiales, el autor tiene guías de excelencia operacional por producto, con el procedimiento de cada tarea: consola, pasos, consultas y evidencia. Esta edición usa 12. La última columna de las tablas de la sección 8 indica la guía y la sección donde está cada procedimiento.

| Código | Dominio | Guía | Tareas leídas | Nuevas en el libro | Ya cubiertas por una fila |
|---|---|---|:--:|:--:|:--:|
| MDO | Correo y colaboración | MDO_Manual_Excelencia_Operacional_SOC.md | 43 | 15 | 28 |
| XDR | Detección y respuesta | Microsoft_Defender_XDR_Manual_Excelencia_Operacional_SOC.md | 50 | 13 | 37 |
| MDE | Dispositivos | MDE_SecOps_Guia_Consolidada_v3.md | 28 | 3 | 25 |
| INT | Dispositivos | Guía de Operaciones SecOps Intune.docx | 13 | 6 | 7 |
| MDI | Identidades | MDI_SecOps_Excellence_v4.md | 24 | 5 | 19 |
| ENT | Identidades | SecOps_Entra_Operational_Guide.md | 44 | 5 | 39 |
| MIP | Datos | MIP_SecOps_ModeloOperacional_v2.md | 35 | 6 | 29 |
| DLP | Datos | purview-dlp-secops-consolidado.md | 22 | 4 | 18 |
| SEN | SIEM y automatización | Microsoft_Sentinel_SecOps_Operational_Guide.md | 27 | 4 | 23 |
| MDA | Aplicaciones y SaaS | MDCA_SecOps_Excelencia_Operacional.md | 37 | 37 | 0 |
| IRM | Datos | Repositorio del autor · guía 17 · Purview_Insider_Risk_Management_Guia_Excelencia_Operacional | 28 | 21 | 7 |
| DLM | Datos | Repositorio del autor · guía 16 · Purview_Data_Lifecycle_y_Records_Management_Guia_Excelencia_Operacional | 28 | 26 | 2 |
| Total |  |  | 379 | 145 | 234 |

Otros documentos del autor que dan el marco de esta sección:

| Dominio | Archivo | Uso en esta edición |
|---|---|---|
| Marco general | CISO_Excelencia_Gobernanza_SecOps_MASTER.md | Marco de referencia: definición y dominios de la excelencia operacional. |
| Marco general | Marco_Maestro_Excelencia_Operacional_CISO_v1.md | Marco de referencia y contraste de sus tareas con las funciones del núcleo. |
| Marco general | Excelencia_Operacional_CISO_v2.md | Ensayo y manifiesto de seis principios. No trae tareas por cadencia. |
| Dispositivos | intune-nist-csf2-mapping.md | Correspondencia de Intune con el marco. No trae tareas por cadencia. |
| Datos | Microsoft_Purview_IRM_Consolidated.md | Referencia de capacidades, licencias y correspondencia con los marcos. No trae tareas por cadencia: las tareas de riesgo interno se tomaron de la guía 17 del repositorio. |
| Datos | Microsoft_Purview_DLM_NIST_CSF2_Consolidated.md | Correspondencia con el marco, evidencia de auditoría e indicadores de madurez por fase. No trae tareas por cadencia: las tareas de ciclo de vida de los datos se tomaron de la guía 16 del repositorio. |

Cómo se decidió qué tarea es nueva y cuál ya estaba cubierta, y la correspondencia completa, están en el documento M10 «Guías de excelencia operacional del autor: qué aportan y cómo se incorporaron».

## 10. El repositorio del autor

Los archivos de la tabla anterior son, salvo los dos últimos, borradores de febrero a abril de 2026. Su versión vigente son las 23 guías del repositorio del autor, validadas el 11 de noviembre de 2026. Cada guía ordena su contenido en tres momentos: la configuración puntual, las rutinas periódicas y la respuesta por evento.

| Qué aporta el repositorio | Cantidad | Dónde está en esta edición |
|---|:--:|---|
| Guías de excelencia operacional | 23 | Hoja Guías del repositorio |
| Acciones | 833: 187 de configuración puntual, 536 rutinas periódicas y 110 de respuesta por evento | Hoja Acciones de las guías |
| Indicadores técnicos | 184 | Hoja Indicadores técnicos |
| Guías integradas tarea por tarea en la hoja Operación por cadencias | 2: riesgo interno y ciclo de vida de los datos | 47 filas nuevas del dominio Datos |
| Guías cuyo producto tiene filas tomadas del borrador anterior | 10 | El procedimiento vigente es el del repositorio |
| Guías sin tareas en la hoja | 11 | Solo en los catálogos de acciones y de indicadores |

La relación de cada guía con los dominios, las funciones, las capacidades y los ciclos del plan está en el documento M11 «Puente con el repositorio del autor: guías, acciones, indicadores técnicos y formación».

---

*Frontier CISO Atlas · Modelo Operativo CISO 365 · edición Microsoft · versión 2.1 · revisión 3 · 15 de noviembre de 2026 · propuesta sujeta a validación · @SCavanna*

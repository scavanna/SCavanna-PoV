# Nivel 2 · Intermedio · Operar, investigar y responder

*Microsoft Defender XDR Ninja Training · Edición 2026*

[← Nivel 1 · Inicial](01_Nivel_1_Inicial.md) · [Índice del programa](README.md) · [Nivel 3 · Avanzado →](03_Nivel_3_Avanzado.md)

<a id="intermedio"></a>

Gestión de incidentes, investigación y respuesta por producto, exposición, respuesta automatizada nativa, integración con Microsoft Sentinel, hunting y detecciones personalizadas. Terminas operando el SOC diario con criterio y con detecciones propias.

*L300 · 10 módulos · ~76 horas · 90 recursos*

**Módulos de este nivel:** [M1 Incidentes y alertas](#m1) · [M2 MDO: investigación](#m2) · [M3 MDE: ASR y protección](#m3) · [M4 MDI: postura y respuesta](#m4) · [M5 ID Protection: riesgo y CA](#m5) · [M6 Vulnerabilidades y exposición](#m6) · [M7 AIR e interrupción](#m7) · [M8 Integración con Sentinel](#m8) · [M9 Hunting](#m9) · [M10 Detecciones y ajuste](#m10)

<a id="m1"></a>

## M1 · Gestión de incidentes y alertas en Defender XDR

*L300 · ~6 h · Origen: Ninja oficial de Defender XDR, Fundamentals e Intermediate (incidentes e investigación)*

En Defender XDR la unidad de trabajo es el **incidente**: el motor de correlación agrupa alertas de todas las cargas —y de Sentinel, si lo integraste— en una historia de ataque con activos, evidencias y acciones. La cola de incidentes prioriza con un puntaje de 0 a 100 y, desde 2026, la experiencia recomendada son los **incident cases** (vista previa), con tareas, SLA, plantillas, sesiones agénticas, resumen de Security Copilot, análisis de radio de impacto (blast radius) y auditoría en la tabla `SecurityCaseEvent`.

Gestionar bien un incidente no es solo investigarlo: es asignarlo, clasificarlo al cerrarlo, etiquetarlo para la automatización, fusionarlo o dividirlo cuando la correlación se equivoca y dejar evidencia de cada decisión. Este módulo cubre ese ciclo, los permisos necesarios y las particularidades que aparecen cuando integras un ITSM o vienes de operar Sentinel por separado.

**Por qué importa**

La calidad del cierre de incidentes determina todo lo que viene después: métricas de MTTA y MTTR confiables, ajuste de detecciones basado en falsos positivos reales y automatización que no rompe el ITSM. Un proceso uniforme de clasificación y etiquetado es la base del track de excelencia ([S2](04_Nivel_4_Excelencia_del_SOC.md#s2) y [S3](04_Nivel_4_Excelencia_del_SOC.md#s3)).

**Qué vas a lograr**

- Priorizar incidentes con la cola y el puntaje de prioridad.
- Investigar un incidente con la historia de ataque, las evidencias y el radio de impacto.
- Gestionar casos de incidente: asignación, tareas, clasificación, fusión y cierre.
- Configurar permisos de lectura y gestión con el RBAC unificado.

> **Novedad.** Los **casos de incidente** (vista previa) son la experiencia recomendada para gestionar incidentes en el portal de Defender: la experiencia clásica sigue disponible, la auditoría queda en la tabla `SecurityCaseEvent` y los casos solo existen en el portal de Defender ([gestión de casos](https://learn.microsoft.com/en-us/defender-xdr/siem-defender-case-management)). La investigación de casos suma el resumen de Copilot, el grafo de ataque y el radio de impacto ([investigar casos](https://learn.microsoft.com/en-us/defender-xdr/investigate-incident-cases)).

> **Atención.** Permisos: ver casos requiere Security Data Read y gestionarlos, Security Data Manage ([gestionar casos](https://learn.microsoft.com/en-us/defender-xdr/manage-incident-cases)). Sepáralos en roles distintos para que un analista en formación no pueda cerrar ni fusionar casos.

> **Consejo Ninja.** La cola de incidentes asigna un puntaje de prioridad de 0 a 100: rojo por encima de 85, naranja entre 15 y 85 y gris por debajo de 15. La página ya figura como experiencia heredada frente a los casos ([priorizar incidentes](https://learn.microsoft.com/en-us/defender-xdr/incident-queue)); usa el puntaje como insumo del triage, no como sustituto del criterio del analista.

> **Atención.** El motor de correlación puede fusionar incidentes después de creados. Si sincronizas incidentes con una herramienta de ITSM, prueba qué pasa con los tickets de los incidentes fusionados antes de automatizar ([experiencia de la comunidad](https://hugo.hybridbrothers.com/posts/transition-from-microsoft-sentinel-to-defender-xdr-practical-challenges/)).

**¿Tienes poco tiempo?**

- [Case management in the Microsoft Defender portal](https://learn.microsoft.com/en-us/defender-xdr/siem-defender-case-management) · Documentación
- [Manage incident cases in the Microsoft Defender portal (preview)](https://learn.microsoft.com/en-us/defender-xdr/manage-incident-cases) · Documentación
- [Investigate incident cases in the Microsoft Defender portal](https://learn.microsoft.com/en-us/defender-xdr/investigate-incident-cases) · Documentación
- [Prioritize incidents in the Microsoft Defender portal (Legacy)](https://learn.microsoft.com/en-us/defender-xdr/incident-queue) · Documentación

### Documentación, cursos y credenciales

- [Case management in the Microsoft Defender portal](https://learn.microsoft.com/en-us/defender-xdr/siem-defender-case-management) · Documentación · Oficial · Vista previa · Microsoft Learn. Describe la gestión de casos nativa del portal Defender: casos de incidente (preview) y genéricos con tareas, SLA, plantillas, sesiones agénticas y auditoría en la tabla SecurityCaseEvent. *Nota:* Los casos de incidente están en preview y son la experiencia recomendada; la experiencia clásica de incidentes sigue disponible
- [Manage incident cases in the Microsoft Defender portal (preview)](https://learn.microsoft.com/en-us/defender-xdr/manage-incident-cases) · Documentación · Oficial · Vista previa · Microsoft Learn. Procedimientos para asignar, priorizar, clasificar, etiquetar, fusionar y cerrar casos de incidente, incluyendo tareas y sesiones agénticas, con permisos de RBAC unificado. *Nota:* Permisos: Security Data Read (ver) y Security Data Manage (gestionar)
- [Investigate incident cases in the Microsoft Defender portal](https://learn.microsoft.com/en-us/defender-xdr/investigate-incident-cases) · Documentación · Oficial · Vista previa · Microsoft Learn. Guía para investigar un caso de incidente: resumen por Copilot, attack story, análisis de blast radius, alertas, activos, evidencias e historial. *Nota:* Blast radius depende de datos y permisos disponibles

### Laboratorios, GitHub y herramientas

- [Hunting-Queries-Detection-Rules (KQL for Defender XDR & Sentinel)](https://github.com/alexverboon/Hunting-Queries-Detection-Rules) · GitHub · MVP · Nuevo · Alex Verboon · GitHub (alexverboon) · nov 2026. Repositorio MIT con consultas KQL de detección, hunting y auditoría para MDE, MDI, MDO, MDCA, Exposure Management y Entra, con plantilla y mapeo MITRE.
- [Azure-Sentinel / Hunting Queries / Microsoft 365 Defender](https://github.com/Azure/Azure-Sentinel/tree/master/Hunting%20Queries/Microsoft%20365%20Defender) · GitHub · Oficial · Microsoft y comunidad · GitHub (Azure/Azure-Sentinel). Repositorio oficial unificado de consultas de hunting para Defender XDR (ASR, campañas, correo y colaboración, ransomware, TVM) mantenido junto a Sentinel.

### Comunidad: blogs, libros, newsletters y eventos

- [Transition from Microsoft Sentinel to Defender XDR - Practical challenges](https://hugo.hybridbrothers.com/posts/transition-from-microsoft-sentinel-to-defender-xdr-practical-challenges/) · Blog · MVP · Legado aún útil · Robbe Van den Daele · Hybrid Brothers · 4 jul 2025. Lecciones de campo sobre el motor de correlación de Defender XDR (fusión de incidentes), descripciones dinámicas y sincronización con ITSM al unificar Sentinel en el portal. *Nota:* Escrito antes de ISOC; la fecha de retiro del portal Azure citada (jul-2026) fue luego extendida a 31-mar-2027 según Learn

**Manos a la obra**

1. `Laboratorio` Genera un incidente con la prueba de detección de MDE o con una simulación de [I8](01_Nivel_1_Inicial.md#i8) y haz el triage desde la cola: puntaje de prioridad, severidad, etiquetas, activos afectados y asignación. Evidencia: captura del incidente asignado con su prioridad y una nota de triage.
2. `Laboratorio` Gestiónalo como caso ([gestionar casos](https://learn.microsoft.com/en-us/defender-xdr/manage-incident-cases)): crea dos tareas, agrega comentarios y ciérralo con su clasificación; luego consulta la auditoría en `SecurityCaseEvent` desde la búsqueda avanzada. Evidencia: consulta con los eventos del caso.
3. `Laboratorio parcial` Investiga el caso con la historia de ataque, las evidencias, el grafo y el radio de impacto ([investigar casos](https://learn.microsoft.com/en-us/defender-xdr/investigate-incident-cases)). Limitación: el resumen de Security Copilot requiere SCU, que la prueba de E5 no incluye; sin capacidad, documenta la investigación sin el resumen. Evidencia: informe de investigación de una página.
4. `Laboratorio` Crea dos roles en el RBAC unificado —N1 con Security Data Read y N2 con Security Data Manage— y comprueba con cuentas de prueba qué puede hacer cada uno sobre el caso. Evidencia: tabla de acciones permitidas y denegadas.
5. `Laboratorio` Escribe el estándar de clasificación del SOC (verdadero positivo, informativo o actividad esperada, y falso positivo, con sus determinaciones) y aplícalo a tres incidentes de prueba. Evidencia: estándar de una página y los tres incidentes clasificados.
6. `Solo producción` Revisa con el equipo de ITSM cómo se reflejan en los tickets los incidentes que el motor de correlación fusionó. Requiere volumen real y la integración productiva. Cómo hacerlo seguro: toma una muestra de 20 incidentes con un rol de solo lectura, no cambies las reglas de sincronización durante la revisión y entrega los hallazgos al dueño de la integración.

**¿Quieres profundizar?**

- [Hunting-Queries-Detection-Rules (KQL for Defender XDR & Sentinel)](https://github.com/alexverboon/Hunting-Queries-Detection-Rules) · GitHub
- [Transition from Microsoft Sentinel to Defender XDR - Practical challenges](https://hugo.hybridbrothers.com/posts/transition-from-microsoft-sentinel-to-defender-xdr-practical-challenges/) · Blog
- [Azure-Sentinel / Hunting Queries / Microsoft 365 Defender](https://github.com/Azure/Azure-Sentinel/tree/master/Hunting%20Queries/Microsoft%20365%20Defender) · GitHub

<a id="m2"></a>

## M2 · Defender for Office 365: investigación y respuesta de correo y colaboración

*L300 · ~8 h · Origen: Ninja oficial de Defender for Office 365 (investigación y respuesta) y Ninja de Defender XDR (AIR)*

Cuando un usuario reporta un correo o MDO detecta una campaña, el SOC necesita responder tres preguntas en minutos: quién lo recibió, quién hizo clic y qué más llegó del mismo remitente. **Threat Explorer** (Plan 2) y **Real-time detections** (Plan 1) responden con vistas, filtros —incluido el de URL en códigos QR— y acciones de remediación masiva; la **investigación y respuesta automatizadas (AIR)** del Plan 2 se dispara por alertas, ZAP, reportes de usuario y clics, agrupa mensajes en clústeres y propone o ejecuta acciones.

Este módulo cubre el ciclo completo: reportes de usuario (también en Teams), AIR y el Action center, Threat Explorer, la respuesta a un buzón comprometido (BEC) y **Attack simulation training** para medir y entrenar a los usuarios. AIR de Defender for Office 365 sigue plenamente vigente: el cambio de septiembre de 2026 sobre AIR solo afecta a Defender for Endpoint.

**Por qué importa**

En el Microsoft Digital Defense Report 2025, el phishing y la ingeniería social explican el 28 % de los accesos iniciales. Reducir el tiempo entre el primer reporte y la purga de toda la campaña limita las credenciales expuestas; AIR y la remediación masiva convierten horas de trabajo manual en minutos, y las simulaciones convierten a los usuarios en sensores.

**Qué vas a lograr**

- Investigar una campaña con Threat Explorer o Real-time detections.
- Operar AIR de correo: aprobar, rechazar y auditar acciones en el Action center.
- Responder a un buzón comprometido (BEC) con el orden correcto de acciones.
- Diseñar y medir una campaña de Attack simulation training.

> **Consejo Ninja.** AIR de Defender for Office 365 (Plan 2) se dispara por alertas, ZAP, reportes de usuario, clics y buzones sospechosos, aprueba de forma automática la remediación de clústeres maliciosos y requiere la auditoría activa ([AIR en MDO](https://learn.microsoft.com/en-us/defender-office-365/air-about)). A diferencia de MDE, el AIR de MDO no cambió el 1 de septiembre de 2026, y el Action center conserva aprobación, historial y deshacer ([Action center](https://learn.microsoft.com/en-us/defender-xdr/m365d-action-center)).

> **Atención.** Threat Explorer es Plan 2 y Real-time detections es Plan 1; ambos permiten filtrar por URL de códigos QR ([Threat Explorer](https://learn.microsoft.com/en-us/defender-office-365/threat-explorer-threat-hunting)). Si tu organización usa E3 con el Plan 1 incluido desde julio de 2026, tus analistas trabajarán con Real-time detections y sin AIR.

> **Consejo Ninja.** Ante un buzón comprometido (BEC), deshabilitar la cuenta es la acción preferida mientras investigas; después vienen el cambio de contraseña, la revisión de reglas de buzón y reenvíos y la de delegaciones ([responder a un BEC](https://learn.microsoft.com/en-us/defender-office-365/responding-to-a-compromised-email-account)). Si hubo robo de tokens, revoca también las sesiones, como verás en [A1](03_Nivel_3_Avanzado.md#a1).

> **Novedad.** Attack simulation training requiere Microsoft 365 E5 o MDO P2, está disponible en las regiones LAM, BRA, CHL y MEX y no admite RBAC unificado ni PowerShell ([AST](https://learn.microsoft.com/en-us/defender-office-365/attack-simulation-training-get-started)). Desde septiembre de 2026, la configuración de reportes de Teams es independiente de la del correo (MC1478463), según las [novedades de MDO](https://learn.microsoft.com/en-us/defender-office-365/defender-for-office-365-whats-new).

**¿Tienes poco tiempo?**

- [Automated investigation and response (AIR) in Microsoft Defender for Office 365 Plan 2](https://learn.microsoft.com/en-us/defender-office-365/air-about) · Documentación
- [Email security with Threat Explorer and Real-time detections in Microsoft Defender for Office 365](https://learn.microsoft.com/en-us/defender-office-365/threat-explorer-email-security) · Documentación
- [Respond to a compromised cloud email account (Business Email Compromise)](https://learn.microsoft.com/en-us/defender-office-365/responding-to-a-compromised-email-account) · Documentación
- [Automated investigation and response (AIR) examples in Microsoft Defender for Office 365 Plan 2](https://learn.microsoft.com/en-us/defender-office-365/air-examples) · Documentación

### Documentación, cursos y credenciales

- [Get started using Attack simulation training](https://learn.microsoft.com/en-us/defender-office-365/attack-simulation-training-get-started) · Documentación · Oficial · Nuevo · Microsoft Learn · 3 jul 2026. Requisitos y roles para simulaciones de phishing (M365 E5 o MDO P2), regiones soportadas incluyendo LAM, BRA, CHL y MEX, y ausencia de soporte de RBAC unificado.
- [Automated investigation and response (AIR) in Microsoft Defender for Office 365 Plan 2](https://learn.microsoft.com/en-us/defender-office-365/air-about) · Documentación · Oficial · Microsoft Learn. Describe el flujo de AIR para correo (alertas, ZAP, reportes de usuario, clics), las acciones pendientes de aprobación en el Action center y la auto-remediación de clústeres maliciosos.
- [Email security with Threat Explorer and Real-time detections in Microsoft Defender for Office 365](https://learn.microsoft.com/en-us/defender-office-365/threat-explorer-email-security) · Documentación · Oficial · Microsoft Learn. Procedimientos para ver suplantaciones, exportar clics de URL, revisar malware y lanzar AIR desde Threat Explorer (P2) o Real-time detections (P1).
- [Automated investigation and response (AIR) examples in Microsoft Defender for Office 365 Plan 2](https://learn.microsoft.com/en-us/defender-office-365/air-examples) · Documentación · Oficial · Microsoft Learn. Ejemplos de AIR: phishing reportado por usuario, investigación iniciada desde Threat Explorer e integración con SIEM vía Office 365 Management Activity API.
- [Threat hunting in Threat Explorer and Real-time detections in Microsoft Defender for Office 365](https://learn.microsoft.com/en-us/defender-office-365/threat-explorer-threat-hunting) · Documentación · Oficial · Microsoft Learn. Recorrido por vistas, filtros (incluido URL de códigos QR) y acciones de remediación de Threat Explorer frente a Real-time detections.

**Manos a la obra**

1. `Laboratorio` Reporta un correo de prueba como phishing desde un buzón de prueba, sigue la investigación de AIR y aprueba o rechaza las acciones propuestas en el Action center ([ejemplos de AIR](https://learn.microsoft.com/en-us/defender-office-365/air-examples)). Evidencia: investigación con sus acciones y el registro de quién las aprobó.
2. `Laboratorio` Investiga una campaña de prueba en Threat Explorer ([seguridad del correo con Explorer](https://learn.microsoft.com/en-us/defender-office-365/threat-explorer-email-security)): filtra por remitente, URL y tipo de entrega, y elimina de forma recuperable (soft delete) los mensajes de los buzones de prueba. Evidencia: filtro de Explorer y la acción en el Action center.
3. `Laboratorio` Ejecuta el procedimiento de BEC sobre una cuenta de prueba a la que antes agregaste una regla de reenvío y una regla que borra mensajes: deshabilita la cuenta, revoca sesiones, cambia la contraseña, elimina reglas y reenvíos y revisa delegaciones ([responder a un BEC](https://learn.microsoft.com/en-us/defender-office-365/responding-to-a-compromised-email-account)). Evidencia: lista de verificación con la hora de cada paso.
4. `Laboratorio` Diseña una campaña de Attack simulation training con payload, página de aterrizaje y capacitación, y mide la tasa de clics, la de credenciales ingresadas y la de reportes ([AST](https://learn.microsoft.com/en-us/defender-office-365/attack-simulation-training-get-started)). Evidencia: informe con las tres tasas y una acción de mejora.
5. `Laboratorio` Busca en `EmailEvents` y `UrlClickEvents` los clics sobre las URL de la campaña y si Safe Links los permitió o bloqueó, y contrasta el resultado con lo que muestra Threat Explorer ([hunting con Threat Explorer](https://learn.microsoft.com/en-us/defender-office-365/threat-explorer-threat-hunting)). Evidencia: consulta guardada con su resultado.
6. `Solo producción` Purga una campaña real de los buzones productivos. Requiere mensajes reales y permisos de remediación sobre buzones de usuarios. Cómo hacerlo seguro: empieza con eliminación recuperable, pide la aprobación de un segundo analista en el Action center, avisa a la mesa de ayuda y conserva la consulta que definió el alcance para poder deshacer.

<a id="m3"></a>

## M3 · Defender for Endpoint: reducción de superficie de ataque y protección avanzada

*L300 · ~8 h · Origen: Ninja oficial de Defender for Endpoint, rol SecAdmin (Intermediate y Expert)*

La mejor alerta es la que no hace falta. Las **reglas de reducción de superficie de ataque (ASR)** bloquean comportamientos que el malware usa a diario —macros que crean procesos, robo de credenciales de LSASS, ejecución desde el correo— y, junto con la protección de red, la protección contra manipulaciones (tamper protection) y el acceso controlado a carpetas, endurecen el endpoint antes del ataque.

El despliegue sigue cuatro fases: planificar, probar en modo **Audit**, habilitar en Block o Warn por anillos y monitorear; solo las reglas de protección estándar pueden ir directo a bloqueo. Este módulo cubre también **EDR en modo bloqueo** para convivir con otro antivirus, el **modo de solución de problemas** para cambiar ajustes protegidos sin desactivar la protección y las acciones de respuesta sobre el dispositivo: aislar, restringir la ejecución, live response y paquete de investigación.

**Por qué importa**

Cada regla ASR en bloqueo elimina una técnica entera del repertorio del atacante, y la protección contra manipulaciones evita que el ransomware apague las defensas. Medir el porcentaje de equipos con ASR en bloqueo y sin exclusiones amplias es uno de los indicadores de postura más directos que puede reportar un SOC.

**Qué vas a lograr**

- Desplegar reglas ASR en Audit, analizar el impacto y pasar a Block o Warn por anillos.
- Decidir exclusiones mínimas con evidencia.
- Explicar EDR en modo bloqueo y qué no funciona con el antivirus en modo pasivo.
- Usar el modo de solución de problemas y las acciones de respuesta del dispositivo.

> **Consejo Ninja.** Despliega ASR por fases: solo las reglas de protección estándar pueden ir directo a Block o Warn; el resto se prueba primero en Audit, que registra el evento 1122 ([guía de despliegue](https://learn.microsoft.com/en-us/defender-endpoint/attack-surface-reduction-rules-deployment), [prueba de ASR](https://learn.microsoft.com/en-us/defender-endpoint/attack-surface-reduction-rules-deployment-test)).

> **Atención.** EDR en modo bloqueo (Plan 2) remedia detecciones de comportamiento aunque el antivirus de Defender esté en modo pasivo, pero en modo pasivo no funcionan la protección en tiempo real, ASR, network protection ni los indicadores ([EDR en modo bloqueo](https://learn.microsoft.com/en-us/defender-endpoint/edr-in-block-mode)). Si convives con otro antivirus, documenta qué capas pierdes.

> **Atención.** El modo de solución de problemas dura 4 horas, con un máximo de 8 horas por día; no existe en Linux y en macOS no desactiva la protección contra alteraciones ([modo de solución de problemas](https://learn.microsoft.com/en-us/defender-endpoint/troubleshooting-mode-enable)). Regístralo como cambio, porque abre una ventana sin protección contra alteraciones.

**¿Tienes poco tiempo?**

- [Attack surface reduction (ASR) rules deployment guide](https://learn.microsoft.com/en-us/defender-endpoint/attack-surface-reduction-rules-deployment) · Documentación
- [Test your attack surface reduction (ASR) rules deployment](https://learn.microsoft.com/en-us/defender-endpoint/attack-surface-reduction-rules-deployment-test) · Laboratorio
- [Endpoint detection and response in block mode](https://learn.microsoft.com/en-us/defender-endpoint/edr-in-block-mode) · Documentación
- [Enable and use troubleshooting mode in Microsoft Defender for Endpoint](https://learn.microsoft.com/en-us/defender-endpoint/troubleshooting-mode-enable) · Documentación

### Documentación, cursos y credenciales

- [Attack surface reduction (ASR) rules deployment guide](https://learn.microsoft.com/en-us/defender-endpoint/attack-surface-reduction-rules-deployment) · Documentación · Oficial · Nuevo · Microsoft Learn · 22 may 2026. Guía de despliegue de reglas ASR en cuatro fases (planificar, probar en Audit, habilitar en Block/Warn por anillos, monitorear), recordando que solo las reglas de protección estándar pueden activarse sin prueba.
- [Endpoint detection and response in block mode](https://learn.microsoft.com/en-us/defender-endpoint/edr-in-block-mode) · Documentación · Oficial · Microsoft Learn. Explica EDR en modo bloqueo (MDE P2) para remediar artefactos detectados por comportamiento cuando Defender Antivirus está en modo pasivo junto a un antivirus de terceros.
- [Enable and use troubleshooting mode in Microsoft Defender for Endpoint](https://learn.microsoft.com/en-us/defender-endpoint/troubleshooting-mode-enable) · Documentación · Oficial · Microsoft Learn. Cómo activar el modo de solución de problemas (4 horas, máximo 8 horas/día por dispositivo) para cambiar temporalmente ajustes protegidos por tamper protection en Windows y macOS.

### Laboratorios, GitHub y herramientas

- [Test your attack surface reduction (ASR) rules deployment](https://learn.microsoft.com/en-us/defender-endpoint/attack-surface-reduction-rules-deployment-test) · Laboratorio · Oficial · Microsoft Learn. Procedimiento para probar todas las reglas ASR en modo Audit con un anillo piloto, revisar el informe ASR, hunting o el evento 1122 y definir exclusiones antes de bloquear.
- [Troubleshooting mode scenarios in Microsoft Defender for Endpoint](https://learn.microsoft.com/en-us/defender-endpoint/troubleshooting-mode-scenarios) · Laboratorio · Oficial · Microsoft Learn. Escenarios guiados para diagnosticar instalaciones bloqueadas, alto CPU de MsMpEng, lentitud, complementos bloqueados por ASR y dominios bloqueados por network protection.

### Comunidad: blogs, libros, newsletters y eventos

- [Microsoft Defender XDR (categoría) - Hybrid Brothers](https://hybridbrothers.com/categories/microsoft-defender-xdr/) · Blog · MVP · Nuevo · Robbe Van den Daele · Hybrid Brothers · 21 sep 2026. Blog de un MVP con artículos prácticos de MDE: onboarding en Ubuntu vía Intune (sep-2026), estrategias de aislamiento y contención, y descubrimiento de dispositivos.

**Manos a la obra**

1. `Laboratorio` Activa todas las reglas ASR en Audit en tus VM, genera eventos 1122 con los escenarios de la [guía de prueba](https://learn.microsoft.com/en-us/defender-endpoint/attack-surface-reduction-rules-deployment-test), revisa el informe de ASR y propone exclusiones mínimas con justificación. Evidencia: informe y tabla de exclusiones propuestas.
2. `Laboratorio` Mide los aciertos de auditoría por regla y por dispositivo con una consulta a `DeviceEvents` que filtre los `ActionType` de ASR. Evidencia: consulta y gráfico que usarás para decidir qué regla pasa a Block.
3. `Laboratorio` Pasa a Block las reglas de protección estándar en el grupo del anillo 1 y valida que el escenario de prueba ahora se bloquea ([guía de despliegue](https://learn.microsoft.com/en-us/defender-endpoint/attack-surface-reduction-rules-deployment)). Evidencia: evento de bloqueo y alerta asociada.
4. `Laboratorio` Activa el modo de solución de problemas en una VM, desactiva por un rato la protección contra alteraciones para un cambio controlado y recoge el paquete de investigación ([escenarios](https://learn.microsoft.com/en-us/defender-endpoint/troubleshooting-mode-scenarios)). Evidencia: registro del cambio con hora de inicio y de fin.
5. `Laboratorio` Practica las acciones de respuesta sobre un dispositivo: aislar y liberar, análisis antivirus, recolección del paquete de investigación y una sesión de live response con `getfile`. Evidencia: historial del Action center con las cuatro acciones.
6. `Laboratorio` Documenta para tu parque qué dispositivos tienen el antivirus de Defender en modo activo, en modo pasivo o con EDR en modo bloqueo, y qué protecciones pierde cada caso según la [página de EDR en modo bloqueo](https://learn.microsoft.com/en-us/defender-endpoint/edr-in-block-mode). Evidencia: tabla con el riesgo residual de cada caso.
7. `Solo producción` Pasa reglas ASR de Audit a Block por anillos en producción. Requiere aplicaciones de negocio reales que pueden romperse. Cómo hacerlo seguro: decide con los datos de auditoría, usa Warn cuando exista, empieza por un grupo piloto con los dueños de las aplicaciones avisados, define un proceso de exclusión con aprobación y ten lista la reversión a Audit.

**¿Quieres profundizar?**

- [Microsoft Defender XDR (categoría) - Hybrid Brothers](https://hybridbrothers.com/categories/microsoft-defender-xdr/) · Blog
- [Troubleshooting mode scenarios in Microsoft Defender for Endpoint](https://learn.microsoft.com/en-us/defender-endpoint/troubleshooting-mode-scenarios) · Laboratorio

<a id="m4"></a>

## M4 · Defender for Identity: postura, rutas de movimiento lateral y respuesta

*L300 · ~8 h · Origen: Ninja oficial de Defender for Identity (postura, movimiento lateral e investigación), actualizado con los cambios de 2025 y 2026*

Con el sensor desplegado, Defender for Identity se convierte en varias herramientas: **detección** de ataques a Active Directory (DCSync, Pass-the-Ticket, golden y diamond ticket, abuso de AD CS como ESC1, ESC8 y ESC11), **postura** con evaluaciones de seguridad de identidad (ISPM) publicadas en Secure Score e **inventario** de identidades humanas y no humanas con un puntaje de riesgo de 0 a 100, en GA desde junio de 2026.

Y una más: **respuesta**. Desde la página de la identidad puedes deshabilitar, revocar sesiones, marcar como comprometida o forzar el cambio de contraseña en AD, Entra ID y otros proveedores como Okta, CyberArk o SailPoint; esas mismas acciones las usa la interrupción automática de ataques. El módulo cubre también un cambio que muchos no notaron: los mapas de rutas de movimiento lateral (LMP) dejaron de actualizarse en 2025 y hoy se reemplazan por las rutas de ataque de Exposure Management e Identity Explorer.

**Por qué importa**

Las cuentas privilegiadas mal protegidas son el atajo del atacante a todo el dominio. Las evaluaciones de postura convierten ese riesgo en un backlog concreto, los honeytokens dan detecciones de alta fidelidad casi sin ruido y unas acciones de respuesta bien configuradas permiten contener una cuenta en segundos, de forma manual o automática.

**Qué vas a lograr**

- Configurar etiquetas de entidades sensibles y honeytokens.
- Priorizar evaluaciones de postura de identidad y medir su avance.
- Ejecutar y auditar acciones de remediación sobre identidades.
- Planificar la migración del sensor v2.x al v3.x sin perder capacidad de respuesta.
- Usar los reemplazos modernos de los mapas de movimiento lateral.

> **Qué cambió.** Los mapas de rutas de movimiento lateral dejaron de actualizarse: desde mediados de mayo de 2025 MDI no recolecta administradores locales por SAM-R ([MC1073068](https://mc.merill.net/message/MC1073068)). Los reemplazos modernos son la pestaña Attack paths de la identidad (Exposure Management) e Identity Explorer, en vista previa desde abril de 2026 y con licencia del data lake de Sentinel ([novedades de MDI](https://learn.microsoft.com/en-us/defender-for-identity/whats-new)).

> **Atención.** Si al migrar al v3.x la cuenta de acción queda en gMSA, las acciones de respuesta —incluida la interrupción automática— dejan de funcionar. La migración desde el portal está en GA desde julio de 2026, solo para controladores de dominio, sin tiempo de inactividad y con hasta 20 minutos por servidor; después el v3.x se actualiza por Windows Update ([migrar al v3.x](https://learn.microsoft.com/en-us/defender-for-identity/deploy/migrate-to-sensor-v3)).

> **Novedad.** Postura de identidad: el identity risk score (0 a 100) llegó a GA en junio de 2026 y se sumaron evaluaciones de cuentas de AD obsoletas (90 días), privilegiados de Entra que también lo son en AD, cuentas de servicio en grupos privilegiados, cuentas en grupos Operator integrados y cuentas locales con credenciales filtradas ([novedades de MDI](https://learn.microsoft.com/en-us/defender-for-identity/whats-new)). Los puntajes de las evaluaciones se actualizan cada 24 horas ([evaluaciones](https://learn.microsoft.com/en-us/defender-for-identity/security-assessment)).

> **Consejo Ninja.** Conviven alertas clásicas y en formato Defender, sin depender de la versión del sensor: las clásicas se ajustan con exclusiones de MDI y las nuevas con reglas de ajuste de Defender ([alertas de MDI](https://learn.microsoft.com/en-us/defender-for-identity/alerts-overview)). En 2026 se sumaron detecciones como DCSync, Pass-the-Ticket (GA), diamond ticket, abuso de AD CS (ESC1, ESC8 y ESC11) y TAP sospechoso.

**¿Tienes poco tiempo?**

- [What's new in Microsoft Defender for Identity](https://learn.microsoft.com/en-us/defender-for-identity/whats-new) · Documentación
- [Remediation actions in Microsoft Defender for Identity](https://learn.microsoft.com/en-us/defender-for-identity/remediation-actions) · Documentación
- [Defender for Identity entity tags in Microsoft Defender](https://learn.microsoft.com/en-us/defender-for-identity/entity-tags) · Documentación
- [Microsoft Defender for Identity's security posture assessments](https://learn.microsoft.com/en-us/defender-for-identity/security-assessment) · Documentación

### Documentación, cursos y credenciales

- [What's new in Microsoft Defender for Identity](https://learn.microsoft.com/en-us/defender-for-identity/whats-new) · Documentación · Oficial · Nuevo · Microsoft Learn · 28 oct 2026. Registro mensual oficial de novedades de Defender for Identity (sensor v3.x, nuevas alertas de AD/Entra/Okta, inventario de identidades, evaluaciones de postura) hasta octubre de 2026.
- [Security alerts in Microsoft Defender for Identity](https://learn.microsoft.com/en-us/defender-for-identity/alerts-overview) · Documentación · Oficial · Nuevo · Microsoft Learn · 11 ago 2026. Explica las alertas de MDI por fase de la cadena de ataque y la transición de alertas 'clásicas' al formato unificado de Defender, con implicaciones de ajuste (exclusiones vs reglas de ajuste de alertas).
- [Remediation actions in Microsoft Defender for Identity](https://learn.microsoft.com/en-us/defender-for-identity/remediation-actions) · Documentación · Oficial · Microsoft Learn. Acciones de respuesta sobre identidades (deshabilitar/habilitar, revocar sesión, marcar como comprometido, forzar cambio de contraseña) en AD, Entra ID, Okta, CyberArk, SailPoint y apps vía Defender for Cloud Apps, y su uso por la interrupción automática de ataques.
- [Defender for Identity entity tags in Microsoft Defender](https://learn.microsoft.com/en-us/defender-for-identity/entity-tags) · Documentación · Oficial · Microsoft Learn. Cómo etiquetar entidades como sensibles, servidores Exchange o honeytoken, y lista de grupos/roles (AD, Entra, Okta, CyberArk, SailPoint) considerados sensibles por defecto.
- [Microsoft Defender for Identity's security posture assessments](https://learn.microsoft.com/en-us/defender-for-identity/security-assessment) · Documentación · Oficial · Microsoft Learn. Introducción a las evaluaciones de postura de identidad (ISPM) en Microsoft Secure Score, con seis categorías (híbrido, infraestructura, certificados, GPO, cuentas, identidades cloud) y requisitos de sensor.
- [View the Identity inventory - Microsoft Defender for Identity](https://learn.microsoft.com/en-us/defender-for-identity/identity-inventory) · Documentación · Oficial · Microsoft Learn. Inventario centralizado de identidades humanas y no humanas (Assets > Identities) con tarjetas para clasificar activos críticos, identidades altamente privilegiadas y cuentas de servicio críticas de AD.
- [Migrate from sensor v2.x to sensor v3.x - Microsoft Defender for Identity](https://learn.microsoft.com/en-us/defender-for-identity/deploy/migrate-to-sensor-v3) · Documentación · Oficial · Microsoft Learn. Procedimiento de migración desde el portal (sin tiempo de inactividad, hasta 20 minutos por servidor) con prerrequisitos, estados de migración, solución de problemas y limpieza del sensor v2.x.
- [Investigate assets - Microsoft Defender for Identity](https://learn.microsoft.com/en-ie/defender-for-identity/investigate-assets) · Documentación · Oficial · Microsoft Learn. Guía de investigación de usuarios, grupos y dispositivos sospechosos con la página de identidad (pestañas de alertas, observado en la organización, timeline de 180 días, recomendaciones ISPM y rutas de ataque).
- [Microsoft Defender for Identity classic alerts](https://learn.microsoft.com/en-us/defender-for-identity/alerts-mdi-classic) · Documentación · Oficial · Microsoft Learn. Catálogo de alertas clásicas de MDI (reconocimiento, persistencia, acceso a credenciales, movimiento lateral) con descripción, periodo de aprendizaje, MITRE y prevención.
- [MC1073068 - Microsoft Defender for Identity: We will disable collection of local administrators' group members (using SAM-R)](https://mc.merill.net/message/MC1073068) · Documentación · Oficial · Microsoft 365 Message Center (archivo mc.merill.net) · 18 jul 2025. Aviso oficial de que MDI deshabilitó (inicio de mayo a mediados de mayo de 2025) la recolección remota de miembros de administradores locales mediante SAM-R, afectando el mapa de rutas de movimiento lateral.
- [Non-human identities in Microsoft Defender](https://learn.microsoft.com/en-us/defender-xdr/investigate-non-human-identities) · Documentación · Oficial · Vista previa · Nuevo · Microsoft Learn · 29 sep 2026. Cómo ver e investigar identidades no humanas (principales de servicio de Entra, cuentas de servicio de AD, apps OAuth de Google Workspace y Salesforce) con insights de riesgo, privilegio, inactividad y uso por agentes de IA.
- [Understand and investigate Lateral Movement Paths (LMPs) with Microsoft Defender for Identity](https://learn.microsoft.com/lv-lv/defender-for-identity/understand-lateral-movement-paths) · Documentación · Oficial · Legado aún útil · Microsoft Learn. Explica las rutas de movimiento lateral hacia cuentas sensibles, dónde verlas, su consulta en hunting y la evaluación de LMP más riesgosas. *Nota:* Página en inglés bajo locale lv-lv. Desde mediados de mayo 2025 MDI dejó de recolectar administradores locales vía SAM-R, por lo que los mapas de LMP ya no se actualizan; usar rutas de ataque de Exposure Management e Identity Explorer
- [Defender for Identity Training (8-hour live training)](https://docs.kaidojarvemets.com/training/defender-for-identity) · Curso · MVP · Kaido Järvemets. Curso en vivo de pago (8 h) de un MVP sobre despliegue de sensores en DC, AD FS, AD CS y Entra Connect, hunting, respuesta y APIs de Defender for Identity.
- [Configure Microsoft Defender for Identity action accounts](https://learn.microsoft.com/en-us/defender-for-identity/deploy/manage-action-accounts?culture=en-us) · Documentación · Oficial · Legado aún útil · Microsoft Learn · 27 nov 2024. Explica la cuenta de acción para remediaciones en AD (LocalSystem por defecto o gMSA opcional) y sus permisos mínimos. *Nota:* Con sensor v3.x solo se admite LocalSystem; la opción gMSA aplica a v2.x

### Webinars, videos y podcasts

- [Identity Centric Protection in the Cloud Era (webinar)](https://www.youtube.com/watch?v=2UhmAX9IV_s) · Webinar · Empleado de Microsoft · Itai Zauer y Naya Hashem · Microsoft Security Community (YouTube) · 3 dic 2025. Webinar sobre protección centrada en la identidad con integraciones de Okta y CyberArk y el inventario unificado de identidades en Defender for Identity.

**Manos a la obra**

1. `Laboratorio` Crea una cuenta señuelo inactiva, etiquétala como Honeytoken ([etiquetas](https://learn.microsoft.com/en-us/defender-for-identity/entity-tags)), autentícate con ella desde otra VM y revisa la alerta y el incidente. Evidencia: alerta del honeytoken con su línea de tiempo.
2. `Laboratorio` Etiqueta como Sensitive un grupo de prueba y agrégale un usuario para disparar la detección de cambios en grupos sensibles. Evidencia: alerta y evento en `IdentityDirectoryEvents`.
3. `Laboratorio` Genera hallazgos de postura: crea una delegación sin restricciones y una plantilla vulnerable de AD CS (ESC1) en el laboratorio, espera 24 horas y revisa las evaluaciones de identidad en Secure Score ([evaluaciones](https://learn.microsoft.com/en-us/defender-for-identity/security-assessment)); las de AD CS requieren el sensor en el servidor AD CS. Evidencia: los dos hallazgos con su plan de corrección.
4. `Laboratorio parcial` Desde la página de la identidad, deshabilita y fuerza el cambio de contraseña de usuarios de prueba en AD y en Entra ID, y revisa el Action center y la auditoría ([acciones de remediación](https://learn.microsoft.com/en-us/defender-for-identity/remediation-actions)). Limitación: no hay conectores de Okta, CyberArk o SailPoint ni volumen para disparar la interrupción automática de forma determinista. Evidencia: historial de las acciones.
5. `Laboratorio` Antes de migrar, confirma que la cuenta de acción del v3.x es LocalSystem y no una gMSA ([migrar al v3.x](https://learn.microsoft.com/en-us/defender-for-identity/deploy/migrate-to-sensor-v3)). Evidencia: captura de la configuración de cuentas de acción.
6. `Laboratorio` En el [inventario de identidades](https://learn.microsoft.com/en-us/defender-for-identity/identity-inventory), filtra las identidades altamente privilegiadas y las cuentas de servicio críticas de AD y exporta el resultado (límite de 5.000 filas). Evidencia: CSV y tres acciones de reducción de privilegios.
7. `Solo producción` Migra de forma masiva del v2.x al v3.x. Requiere controladores de dominio reales y diversidad de roles. Cómo hacerlo seguro: piloto en un DC por sitio, confirma LocalSystem como cuenta de acción antes de empezar, migra en ventana de cambio, conserva el software v2.x hasta validar y limpia después.
8. `Solo producción` Ajusta alertas de MDI y exclusiones con falsos positivos reales ([alertas de MDI](https://learn.microsoft.com/en-us/defender-for-identity/alerts-overview)). Cómo hacerlo seguro: revisa con un rol de solo lectura, documenta exclusiones mínimas, prueba las reglas de ajuste sobre un alcance acotado y revísalas cada mes.

**¿Quieres profundizar?**

- [Identity Centric Protection in the Cloud Era (webinar)](https://www.youtube.com/watch?v=2UhmAX9IV_s) · Webinar

<a id="m5"></a>

## M5 · Entra ID Protection: riesgo, acceso condicional y remediación

*L300 · ~8 h · Origen: Nuevo en esta edición (se profundiza en el programa de Entra, módulo M2)*

El riesgo solo sirve si dispara algo. Desde el **1 de octubre de 2026** las directivas de riesgo heredadas de ID Protection están retiradas y todo pasa por **acceso condicional**: riesgo de usuario alto con «Require risk remediation» —que agrega automáticamente authentication strength y la frecuencia de inicio de sesión «Every time»— y riesgo de inicio de sesión medio o alto con MFA resistente y la misma frecuencia, en directivas separadas. Microsoft, además, empezó a crear una directiva administrada para usuarios de alto riesgo en algunos inquilinos (MC1476122).

La remediación moderna cubre a usuarios con contraseña (cambio seguro) y sin contraseña (revocación de sesiones), deshabilita dispositivos agregados por el atacante y se alimenta de **señales de riesgo unificadas** que componen el riesgo con Defender for Identity, Endpoint, Cloud Apps y Purview. El módulo cierra con las identidades de carga de trabajo, los agentes con Entra Agent ID y el Identity Risk Management Agent de Security Copilot.

**Por qué importa**

Una directiva de riesgo bien diseñada contiene una identidad comprometida en el siguiente inicio de sesión, sin esperar a que un analista la vea. Migrar desde las directivas heredadas no es opcional desde octubre de 2026, y hacerlo con modo solo informe, grupos piloto y cuentas de emergencia excluidas evita bloqueos masivos que paralizan al negocio.

**Qué vas a lograr**

- Diseñar directivas de acceso condicional basadas en riesgo, separadas para usuario e inicio de sesión.
- Migrar desde las directivas heredadas con modo solo informe y grupos piloto.
- Remediar, descartar y desbloquear riesgo con los roles mínimos.
- Explicar las señales unificadas y su dependencia de Defender for Identity.
- Reconocer qué requiere Workload ID Premium y qué cambia para los agentes.

> **Qué cambió.** Las directivas de riesgo heredadas de ID Protection se retiraron el **1 de octubre de 2026**: hay que recrearlas como directivas de acceso condicional —primero en modo solo informe— y deshabilitar las heredadas ([configurar directivas de riesgo](https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-configure-risk-policies)).

> **Consejo Ninja.** Recomendación oficial: riesgo de usuario alto → «Require risk remediation», que agrega de forma automática authentication strength y sign-in frequency «Every time»; riesgo de inicio de sesión medio o alto → MFA con authentication strength y «Every time»; y nunca combines ambas condiciones en una directiva ([configurar directivas de riesgo](https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-configure-risk-policies)). «Require risk remediation» cubre usuarios con y sin contraseña, deshabilita dispositivos agregados por el atacante y no aplica a invitados ([directivas basadas en riesgo](https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-policies)).

> **Atención.** Directiva administrada por Microsoft «Require risk remediation for high-risk users»: se creó en solo informe la semana del 28 de septiembre de 2026 y se activa sola la semana del 28 de octubre en inquilinos con P2 si no actúas. El archivo del Message Center solo la registró en inquilinos educativos, así que verifica tu caso ([MC1476122](https://mc.merill.net/message/MC1476122)).

> **Novedad.** Las **señales de riesgo unificadas** componen el riesgo de usuario con señales de MDI, MDE, Defender for Cloud Apps y Purview, y pueden elevar a alto una suma de riesgos medios; requieren P2 y Defender for Identity configurado ([señales unificadas](https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-unified-risk)). Para identidades de carga de trabajo, el detalle completo y el acceso condicional por riesgo requieren Workload ID Premium, una SKU aparte que no está en E5 ([workload identities](https://learn.microsoft.com/en-us/entra/id-protection/concept-workload-identity-risk)), e ID Protection para agentes «pronto» requerirá Agent 365 ([agentes](https://learn.microsoft.com/en-us/entra/id-protection/concept-risky-agents)).

**¿Tienes poco tiempo?**

- [Configure and enable risk policies - Microsoft Entra ID Protection](https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-configure-risk-policies) · Documentación
- [Remediate risks and unblock users - Microsoft Entra ID Protection](https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-remediate-unblock) · Documentación
- [Unified risk signals in Microsoft Entra ID Protection](https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-unified-risk) · Documentación
- [Require remediation for risky users (Conditional Access policy)](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-risk-based-user) · Documentación

### Documentación, cursos y credenciales

- [MC1476122 - Microsoft-managed CA policy coming to your tenant: Require risk remediation for high-risk users](https://mc.merill.net/message/MC1476122) · Documentación · Oficial · Nuevo · Microsoft 365 Message Center (archivo mc.merill.net) · 21 sep 2026. Aviso del Centro de mensajes: Microsoft crea una directiva de acceso condicional administrada por Microsoft que exige remediación de riesgo para usuarios de riesgo alto, en solo informe 30 días y luego activada.
- [Unified risk signals in Microsoft Entra ID Protection](https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-unified-risk) · Documentación · Oficial · Nuevo · Microsoft Learn · 30 jun 2026. Explica cómo ID Protection compone el riesgo de usuario correlacionando señales de Entra, Defender for Identity, Endpoint, Cloud Apps y Purview, pudiendo elevar a riesgo alto la suma de señales medias o bajas.
- [Remediate risks and unblock users - Microsoft Entra ID Protection](https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-remediate-unblock) · Documentación · Oficial · Nuevo · Microsoft Learn · 15 may 2026. Opciones de autorremediación, remediación del sistema y manual, desbloqueo de usuarios, cambio de contraseña local para remediar riesgo y manejo de detecciones de robo de tokens.
- [Investigate risk with Microsoft Entra ID Protection](https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-investigate-risk) · Documentación · Oficial · Microsoft Learn. Marco oficial de triaje, investigación y remediación de riesgo (autorremediación primero, luego remediación administrativa) con integración con Defender XDR y Sentinel.
- [Microsoft Entra ID Protection risk-based access policies](https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-policies) · Documentación · Oficial · Microsoft Learn. Conceptos de directivas de acceso basadas en riesgo de usuario e inicio de sesión, el control de remediación adaptativa y sus reglas de precedencia y limitaciones.
- [Securing workload identities with Microsoft Entra ID Protection](https://learn.microsoft.com/en-us/entra/id-protection/concept-workload-identity-risk) · Documentación · Oficial · Microsoft Learn. Detecciones de riesgo para identidades de carga de trabajo (principales de servicio) como credenciales filtradas, inicios de sesión sospechosos y apps maliciosas, y su remediación.
- [Configure and enable risk policies - Microsoft Entra ID Protection](https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-configure-risk-policies) · Documentación · Oficial · Microsoft Learn · 28 abr 2026. Recomendaciones oficiales (riesgo de usuario alto -> Require risk remediation; riesgo de sign-in medio/alto -> MFA con frecuencia 'cada vez') y procedimiento de migración de las directivas heredadas a acceso condicional.
- [Require remediation for risky users (Conditional Access policy)](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-risk-based-user) · Documentación · Oficial · Microsoft Learn · 24 mar 2026. Paso a paso para crear la directiva de acceso condicional de riesgo de usuario alto con el control 'Require risk remediation' (autorremediación con o sin contraseña) empezando en modo solo informe.
- [ID Protection for agents - Microsoft Entra ID Protection](https://learn.microsoft.com/en-us/entra/id-protection/concept-risky-agents) · Documentación · Oficial · Nuevo · Microsoft Learn · 17 jun 2026. Explica cómo ID Protection detecta riesgo en agentes de IA con identidad de Microsoft Entra Agent ID (informe Risky Agents, detecciones offline, acciones y acceso condicional basado en riesgo de agente).
- [Microsoft Entra Workload ID (product and pricing page)](https://www.microsoft.com/en-us/security/business/identity-access/microsoft-entra-workload-id) · Documentación · Oficial · Microsoft Security. Página comercial de Microsoft Entra Workload ID Premium con precio de lista, prueba gratuita de 90 días y FAQ de licenciamiento del acceso condicional para identidades de carga de trabajo.
- [User self-remediation with Microsoft Entra ID Protection](https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-user-experience) · Documentación · Oficial · Microsoft Learn · 25 mar 2026. Describe la experiencia de usuario en registro de MFA, autorremediación de riesgo, remediación adaptativa y desbloqueo administrativo, incluido el caso de técnicos MSP/CSP de alto riesgo.
- [Microsoft Entra ID Protection and the Microsoft Graph PowerShell SDK](https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-graph-api) · Documentación · Oficial · Microsoft Learn · 23 feb 2026. Comandos de Graph PowerShell para listar detecciones y usuarios de riesgo, confirmar compromiso y descartar riesgo en bloque.
- [Identity Risk Management Agent (Preview) - Microsoft Entra ID Protection](https://learn.microsoft.com/en-us/entra/id-protection/identity-risk-management-agent-get-started) · Documentación · Oficial · Vista previa · Nuevo · Microsoft Learn · 1 may 2026. Agente de Security Copilot en Entra que investiga hasta 100 usuarios de riesgo por ejecución, resume hallazgos y sugiere remediaciones que requieren aprobación manual. *Nota:* Requiere Entra ID P2 y unidades de cómputo de seguridad (SCU); solo identidades de usuario (no workload identities); sin remediación automática
- [How do enterprises know which agents are risky? (Microsoft Agent 365)](https://learn.microsoft.com/en-us/microsoft-agent-365/guidance/detect-risky-agents) · Documentación · Oficial · Nuevo · Microsoft Learn · 25 sep 2026. Guía conceptual de Agent 365 sobre cómo se consolidan señales de riesgo de agentes desde Entra, Purview y Defender en el centro de administración de Microsoft 365.

### Comunidad: blogs, libros, newsletters y eventos

- [Migrate Microsoft Entra Risk Policies to Conditional Access](https://www.sentinelidentity.ca/posts/migrate-microsoft-entra-risk-policies-conditional-access) · Blog · Comunidad · Nuevo · MU.A · Sentinel Identity · 6 sep 2026. Guía práctica comunitaria para migrar las directivas de riesgo heredadas a acceso condicional con pruebas en solo informe, evidencias, reversión y monitoreo.
- [Entra ID Protection - User Risk with Unified Identity Signals from Defender is here!](https://blog.sonnes.cloud/entra-id-protection-user-risk-with-unified-identity-signals-from-defender-is-here/) · Blog · MVP · Nuevo · Michael Morten Sonne · blog.sonnes.cloud · 6 ago 2026. Recorrido práctico por las señales de riesgo unificadas (preview pública): prerrequisitos, conjuntos de cuentas, acceso condicional basado en riesgo e investigación en el portal Defender.
- [Identity Protection – Sam's Corner](https://samilamppu.com/category/azure-active-directory-aad/identity-protection/) · Blog · MVP · Legado aún útil · Sami Lamppu · Sam's Corner · 25 oct 2023. Serie de artículos sobre ID Protection: APIs, integraciones con soluciones de seguridad de Microsoft, envío a SIEM y remediación de riesgo de usuarios híbridos. *Nota:* Contenido 2016-2023 con nombre 'Azure AD Identity Protection'; conceptos vigentes, revisar cambios de 2025-2026 (retiro de directivas heredadas)

**Manos a la obra**

1. `Laboratorio` Crea dos directivas de acceso condicional separadas —riesgo de usuario alto con «Require risk remediation» y riesgo de inicio de sesión medio o alto con MFA y «Every time»— en [modo solo informe](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-report-only), excluye las cuentas de emergencia, valida con la herramienta [What If](https://learn.microsoft.com/en-us/entra/identity/conditional-access/what-if-tool) y actívalas para un grupo piloto. Evidencia: configuración de ambas directivas y resultado de What If.
2. `Laboratorio` Verifica que no queden directivas heredadas de riesgo activas y documenta la equivalencia de cada una en acceso condicional ([configurar directivas de riesgo](https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-configure-risk-policies)). Evidencia: tabla de equivalencias.
3. `Laboratorio` Con un usuario de prueba en riesgo, compara la autorremediación con cambio seguro de contraseña, el restablecimiento por un administrador y el descarte por un Security Operator ([remediar y desbloquear](https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-remediate-unblock)). Evidencia: historial de riesgo de cada caso y el rol mínimo usado.
4. `Laboratorio parcial` Simula la credencial filtrada de una aplicación de prueba deshabilitada y sin permisos, publicándola en un repositorio público de GitHub como describe la [guía de simulación](https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-simulate-risk), y borra el secreto al terminar ([workload identities](https://learn.microsoft.com/en-us/entra/id-protection/concept-workload-identity-risk)). Limitación: el detalle completo y el acceso condicional por riesgo requieren Workload ID Premium (usa la prueba de 90 días). Evidencia: detección de riesgo de la entidad de servicio.
5. `Laboratorio parcial` Con P2 y MDI en el inquilino de prueba, genera una alerta de MDI (por ejemplo, el honeytoken de [M4](#m4)) y un inicio de sesión riesgoso del mismo usuario vinculado, y busca el evento de riesgo compuesto `aiCompoundAccountRisk` ([señales unificadas](https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-unified-risk)). Limitación: la composición no es determinista y depende de la correlación temporal. Evidencia: historial de riesgo del usuario.
6. `Laboratorio parcial` Inicia el Identity Risk Management Agent desde Risky users con usuarios de prueba en riesgo y revisa sus recomendaciones ([agente](https://learn.microsoft.com/en-us/entra/id-protection/identity-risk-management-agent-get-started)). Limitación: está en vista previa, investiga hasta 100 usuarios por ejecución, no remedia por sí solo y consume SCU, que la prueba no incluye; usa una capacidad temporal como indica el anexo y bórrala al terminar. Evidencia: resumen del agente y tu decisión sobre cada recomendación.
7. `Solo producción` Gestiona la directiva administrada por Microsoft ([MC1476122](https://mc.merill.net/message/MC1476122)). Requiere un inquilino con P2 y usuarios reales. Cómo hacerlo seguro: revísala en solo informe, excluye las cuentas de emergencia mediante el grupo de la directiva y avisa a la mesa de ayuda antes de activarla.

<a id="m6"></a>

## M6 · Gestión de vulnerabilidades y exposición

*L300 · ~6 h · Origen: Ninja de Defender Vulnerability Management y Ninja de Defender for Endpoint, rol SecAdmin*

Detectar rápido no alcanza si el atacante entra por una vulnerabilidad conocida. **Defender Vulnerability Management** (DVM), hoy bajo Exposure management en el portal, inventaría software y configuraciones, evalúa vulnerabilidades y prioriza por riesgo con los datos del propio Defender for Endpoint. Las capacidades núcleo vienen con MDE Plan 2 (y por tanto con Microsoft 365 E5); las premium —líneas base de seguridad, bloqueo de aplicaciones vulnerables, extensiones, certificados y firmware— requieren el complemento o la versión independiente.

**Microsoft Security Exposure Management** lleva la mirada más allá del endpoint: activos críticos, rutas de ataque, iniciativas con puntaje y objetivo, y Secure Score. Este módulo te enseña a separar lo incluido de lo que se paga aparte y a convertir la exposición en métricas que el negocio entiende, en la línea que propone el Microsoft Digital Defense Report 2026.

**Por qué importa**

El MDDR 2026 reporta que la mediana entre el descubrimiento de una vulnerabilidad y su explotación ya es menor de 24 horas, mientras las empresas tardan de 30 a 60 días en remediar. Priorizar por exposición real y medir el tiempo de mitigación es la única forma de cerrar esa brecha con recursos finitos.

**Qué vas a lograr**

- Distinguir las capacidades núcleo y premium de DVM y su licencia.
- Priorizar recomendaciones de seguridad por riesgo y por activos críticos.
- Usar iniciativas y rutas de ataque de Exposure Management.
- Definir métricas de exposición para el reporte ejecutivo.

> **Atención.** MDE P2, incluido en Microsoft 365 E5, trae las capacidades núcleo de Defender Vulnerability Management; las premium —evaluación de líneas base de seguridad, bloqueo de aplicaciones vulnerables, extensiones del navegador, certificados y firmware— requieren el complemento o la versión independiente, y los servidores las obtienen con Defender for Servers Plan 2 ([comparar planes de DVM](https://learn.microsoft.com/en-us/defender-vulnerability-management/defender-vulnerability-management-capabilities)).

> **Atención.** Exposure Management completo viene con Microsoft 365 E5 o A5, E3 con Defender Suite, MDE, MDI, Defender for Cloud Apps, MDO P2 o Business Premium, entre otros; con Microsoft 365 E3/A3 o MDO P1 solo accedes a Secure Score, y los conectores de terceros serán de consumo. Su página de licencias (marzo de 2025) todavía usa el nombre anterior de Defender Suite ([licencias de Exposure Management](https://learn.microsoft.com/en-us/security-exposure-management/integration-licensing)). Los permisos se asignan en el RBAC unificado y el servicio solo está en la nube pública ([requisitos](https://learn.microsoft.com/en-us/security-exposure-management/prerequisites)).

> **Novedad.** Para reportar avance, las iniciativas de Exposure Management muestran un puntaje con objetivo, la tendencia de 14 días y el historial ([iniciativas](https://learn.microsoft.com/en-us/security-exposure-management/initiatives)). En septiembre de 2026 llegaron a GA las recomendaciones de AI-Readiness en Secure Score ([novedades de MDE](https://learn.microsoft.com/en-us/defender-endpoint/whats-new-in-microsoft-defender-endpoint)).

> **Consejo Ninja.** El Microsoft Digital Defense Report 2026 explica por qué la priorización importa: la mediana entre el descubrimiento de una vulnerabilidad y su explotación baja de 24 horas, mientras la remediación empresarial tarda entre 30 y 60 días ([MDDR 2026](https://www.microsoft.com/en-us/security/security-insider/threat-landscape/2026-digital-defense-report)). Prioriza por explotación y criticidad del activo, no por cantidad de CVE.

**¿Tienes poco tiempo?**

- [Compare Microsoft Defender Vulnerability Management plans and capabilities](https://learn.microsoft.com/en-us/defender-vulnerability-management/defender-vulnerability-management-capabilities) · Documentación
- [Integration and licensing for Microsoft Security Exposure Management](https://learn.microsoft.com/en-us/security-exposure-management/integration-licensing) · Documentación
- [Prerequisites and support in Microsoft Security Exposure Management](https://learn.microsoft.com/en-us/security-exposure-management/prerequisites) · Documentación
- [Review security initiatives in Microsoft Security Exposure Management](https://learn.microsoft.com/en-us/security-exposure-management/initiatives) · Documentación

### Documentación, cursos y credenciales

- [Compare Microsoft Defender Vulnerability Management plans and capabilities](https://learn.microsoft.com/en-us/defender-vulnerability-management/defender-vulnerability-management-capabilities) · Documentación · Oficial · Microsoft Learn. Tabla oficial que separa las capacidades núcleo de DVM incluidas en MDE P2 (y por tanto en M365 E5) de las premium del Add-on o Standalone (líneas base, bloqueo de apps vulnerables, extensiones, certificados, firmware).
- [Integration and licensing for Microsoft Security Exposure Management](https://learn.microsoft.com/en-us/security-exposure-management/integration-licensing) · Documentación · Oficial · Microsoft Learn · 6 mar 2025. Indica qué licencias dan acceso completo a Exposure Management (M365 E5, E3 + E5 Security, MDE, MDI, MDCA, MDO P2, etc.) y que E3/A3/MDO P1 solo acceden a Secure Score; los conectores de terceros serán de consumo.
- [Prerequisites and support in Microsoft Security Exposure Management](https://learn.microsoft.com/en-us/security-exposure-management/prerequisites) · Documentación · Oficial · Microsoft Learn. Requisitos de Exposure Management: integrado en security.microsoft.com, solo nube pública, permisos Exposure Management (read/manage) en RBAC unificado y conectores externos en preview gratuitos.

### Webinars, videos y podcasts

- [MS Defender Vulnerability Management Premium Capabilities | Virtual Ninja Training w/ Heike Ritter](https://www.youtube.com/watch?v=g-O1iNQ3d5U) · Video · Empleado de Microsoft · Legado aún útil · Heike Ritter, Brandon Lawson · YouTube - Microsoft Security Community. Episodio del Virtual Ninja Training sobre capacidades premium de DVM (líneas base, evaluaciones de aplicaciones y certificados). *Nota:* Usa nombres antiguos (Microsoft 365 Defender); hoy DVM vive bajo Exposure management en el portal

**Manos a la obra**

1. `Laboratorio` Compara qué recomendaciones muestra Defender Vulnerability Management con MDE P2 y con la prueba del complemento (líneas base, extensiones y certificados) ([comparar planes](https://learn.microsoft.com/en-us/defender-vulnerability-management/defender-vulnerability-management-capabilities)). Evidencia: tabla de capacidades observadas por plan.
2. `Laboratorio` Exporta las diez recomendaciones de seguridad de mayor exposición en tus VM y asigna dueño y fecha a cada una. Evidencia: lista priorizada con el criterio de riesgo y el activo afectado.
3. `Laboratorio` Cuenta con KQL las vulnerabilidades por severidad, por software y por dispositivo en `DeviceTvmSoftwareVulnerabilities`, y compara el resultado con la priorización que propone el portal. Evidencia: consulta guardada y su resultado.
4. `Laboratorio` Elige una iniciativa de Exposure Management, fija un puntaje objetivo y registra la tendencia de 14 días como línea base ([iniciativas](https://learn.microsoft.com/en-us/security-exposure-management/initiatives)). Evidencia: captura de la iniciativa con su objetivo.
5. `Laboratorio` Define tres métricas de exposición para el reporte ejecutivo de [S7](04_Nivel_4_Excelencia_del_SOC.md#s7), por ejemplo: porcentaje de activos críticos con vulnerabilidades críticas abiertas por más de 30 días, puntaje de la iniciativa y tiempo de mitigación. Evidencia: ficha de cada métrica con fuente y dueño.
6. `Solo producción` Lanza un programa de reducción de exposición con los dueños de TI. Requiere activos reales y equipos responsables de corregir. Cómo hacerlo seguro: el SOC usa permisos de solo lectura de Exposure Management, los cambios pasan por la gestión de cambios de TI y el avance de la iniciativa se revisa cada dos semanas.

<a id="m7"></a>

## M7 · Respuesta automatizada nativa: AIR e interrupción automática de ataques

*L300 · ~6 h · Origen: Ninja oficial de Defender XDR, Fundamentals e Intermediate (AIR y attack disruption)*

Defender XDR responde solo de dos maneras complementarias. La **investigación y respuesta automatizadas (AIR)** analiza alertas y propone o ejecuta remediaciones según el nivel de automatización; en Defender for Office 365 sigue siendo una experiencia completa, mientras que en Defender for Endpoint, desde el **1 de septiembre de 2026**, dejó de ejecutarse como investigación separada y no se puede disparar manualmente: sus capacidades quedaron en la pila antivirus.

La **interrupción automática de ataques** (attack disruption) correlaciona señales de varias cargas y, con una confianza de 99 % o más, contiene activos comprometidos en plena intrusión: deshabilita o contiene usuarios en AD y Entra ID, contiene dispositivos y, en vista previa, actúa sobre Okta y AWS vía Sentinel y aísla estaciones de trabajo automáticamente durante una ventana definida. **Predictive shielding** restringe de forma proactiva identidades privilegiadas expuestas. Todo queda en el Action center, con opción de deshacer.

**Por qué importa**

Los ataques operados por humanos avanzan en minutos; un SOC que depende de que alguien vea la alerta llega tarde. La interrupción automática y AIR reducen el tiempo de contención a minutos y liberan analistas para el trabajo de juicio, siempre que los requisitos estén completos y las exclusiones sean mínimas y revisadas.

**Qué vas a lograr**

- Explicar qué hace AIR en Defender for Office 365 y qué cambió en Defender for Endpoint el 1 de septiembre de 2026.
- Verificar los requisitos de la interrupción automática por carga.
- Gestionar exclusiones, acciones pendientes y reversiones en el Action center.
- Decidir qué mecanismo de respuesta usar en cada escenario.

> **Qué cambió.** Desde el **1 de septiembre de 2026**, AIR de Defender for Endpoint deja de ejecutarse como experiencia de investigación separada y no puede dispararse manualmente; sus capacidades quedan en la pila antivirus predeterminada. Microsoft sigue recomendando la automatización completa (40 % más muestras de malware removidas) y las acciones pendientes vencen a los 7 días ([niveles de automatización](https://learn.microsoft.com/en-us/defender-endpoint/automation-levels)). El AIR de MDO sigue disponible ([Action center](https://learn.microsoft.com/en-us/defender-xdr/m365d-action-center)).

> **Consejo Ninja.** La interrupción automática de ataques actúa con una confianza de al menos 99 % y con acciones reversibles sobre Entra ID, Active Directory y, en vista previa, Okta y AWS; admite exclusiones de usuarios, dispositivos e IP ([interrupción automática](https://learn.microsoft.com/en-us/defender-xdr/automatic-attack-disruption)), aunque Microsoft desaconseja excluir activos porque reduce su eficacia ([exclusiones](https://learn.microsoft.com/en-us/defender-xdr/automatic-attack-disruption-exclusions)).

> **Atención.** Requisitos que suelen fallar: descubrimiento de dispositivos en modo Standard para «Contain device», sensor Sense 10.8470 o posterior para «Contain user», auditoría de buzones (MailItemsAccessed, UpdateInboxRules, entre otros) y Sentinel conectado al portal unificado para las acciones en Okta y AWS. El aislamiento automático de estaciones de trabajo está en vista previa y se revierte tras una ventana definida ([configurar la interrupción](https://learn.microsoft.com/en-us/defender-xdr/configure-attack-disruption)).

> **Novedad.** El **predictive shielding** extiende la interrupción: restringe de forma proactiva identidades de alto privilegio expuestas, para clientes de MDE P2 que cumplan los requisitos. Microsoft publicó dos casos en 2026: un ransomware por GPO detenido antes de empezar (23 de marzo) y un compromiso de dominio contenido (17 de abril) ([caso de compromiso de dominio](https://www.microsoft.com/en-us/security/blog/2026/04/17/domain-compromise-predictive-shielding-shut-down-lateral-movement/)).

**¿Tienes poco tiempo?**

- [Automatic attack disruption in Microsoft Defender](https://learn.microsoft.com/en-us/defender-xdr/automatic-attack-disruption) · Documentación
- [Configure automatic attack disruption in Microsoft Defender XDR](https://learn.microsoft.com/en-us/defender-xdr/configure-attack-disruption) · Documentación
- [A Deep Dive into Automated Attack Disruption](https://www.youtube.com/watch?v=5nk6d170Cnw) · Webinar
- [Containing a domain compromise: How predictive shielding shut down lateral movement](https://www.microsoft.com/en-us/security/blog/2026/04/17/domain-compromise-predictive-shielding-shut-down-lateral-movement/) · Blog oficial

**¿Qué mecanismo de respuesta uso?**

| Mecanismo | Qué hace | Quién decide | Reversión | Licencia y costo | Úsalo para |
|---|---|---|---|---|---|
| Interrupción automática de ataques | Contiene usuarios, dispositivos e IP durante un ataque en curso, con una confianza de al menos 99 % | La plataforma, sin aprobación previa; tú gobiernas las exclusiones | Acciones reversibles, visibles en el incidente y en el Action center; el aislamiento automático (vista previa) se revierte tras una ventana definida | Incluida, por ejemplo, en Microsoft 365 E5, E3 con Defender Suite, MDE P2, MDI o MDO P2 | Ataques de alta confianza en curso: ransomware operado por humanos, BEC o AiTM |
| AIR de Defender for Office 365 | Investiga alertas de correo, reportes de usuario y clics, y propone o ejecuta remediaciones | El analista en el Action center; los clústeres maliciosos se remedian de forma automática | Deshacer desde el Action center | MDO Plan 2 (E5, A5, G5 o Defender Suite) | Phishing reportado y campañas de correo |
| Automatización de Defender for Endpoint | Desde el 1 de septiembre de 2026, las capacidades de AIR de MDE corren dentro de la pila antivirus | El nivel de automatización de cada grupo de dispositivos | Action center; las acciones pendientes vencen a los 7 días | MDE P2 | Malware en equipos con remediación de alta confianza |
| Acciones de detecciones personalizadas | Aíslan, recolectan el paquete de investigación, restringen ejecución, ponen archivos en cuarentena, marcan usuarios comprometidos o mueven y borran correos al dispararse la regla | Tú, al diseñar y probar la regla | Según la acción: liberar, deshacer o restaurar | Incluidas con Defender XDR | Patrones propios de alta precisión, probados en el laboratorio |
| Reglas de automatización y playbooks de Logic Apps | Orquestan pasos en varios productos, enriquecen, notifican y piden aprobación | Tu diseño, con aprobación humana en Teams cuando corresponda | Playbook de reversión probado (por ejemplo, Unisolate-MDEMachine) | Logic Apps se paga aparte en Azure | Respuestas de varios pasos e integración con ITSM |
| Automatización de ISOC (vista previa) | Playbooks en Python generados desde lenguaje natural, con una acción por regla | Tu diseño, después de revisar el código generado | Desactivar la regla y revisar el código | Defender Suite, E5 o E7 sin workspace de Sentinel activo | Organizaciones que todavía no tienen Sentinel |
| Agentes de Security Copilot | Clasifican alertas, investigan y proponen acciones con razonamiento visible | El analista revisa y aprueba según tu política de autonomía | Retroalimentación al agente y desactivación | SCU (incluidas en E5 según las licencias pagas) | Volumen alto y repetitivo, como el correo reportado |

Fuentes: [interrupción automática](https://learn.microsoft.com/en-us/defender-xdr/automatic-attack-disruption), [configurar la interrupción](https://learn.microsoft.com/en-us/defender-xdr/configure-attack-disruption), [AIR en MDO](https://learn.microsoft.com/en-us/defender-office-365/air-about), [niveles de automatización](https://learn.microsoft.com/en-us/defender-endpoint/automation-levels), [detecciones personalizadas](https://learn.microsoft.com/en-us/defender-xdr/custom-detection-rules), [automatización en Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/automation/automation), [automatización con ISOC](https://learn.microsoft.com/en-us/defender-xdr/siem-defender-automation) y [agente de triage](https://learn.microsoft.com/en-us/defender-xdr/security-alert-triage-agent).

### Documentación, cursos y credenciales

- [Automatic attack disruption in Microsoft Defender](https://learn.microsoft.com/en-us/defender-xdr/automatic-attack-disruption) · Documentación · Oficial · Microsoft Learn. Explica cómo la interrupción automática correlaciona señales XDR para contener activos comprometidos con confianza ≥99% y cómo el SOC puede deshacer acciones o excluir activos.
- [Configure automatic attack disruption in Microsoft Defender XDR](https://learn.microsoft.com/en-us/defender-xdr/configure-attack-disruption) · Documentación · Oficial · Microsoft Learn. Requisitos de licencias (p. ej., M365 E5, E3 + Defender Suite, MDE P2, MDO P2), despliegue, permisos y versión mínima del sensor Sense (v10.8470) para la interrupción automática.

### Anuncios y blogs oficiales

- [Containing a domain compromise: How predictive shielding shut down lateral movement](https://www.microsoft.com/en-us/security/blog/2026/04/17/domain-compromise-predictive-shielding-shut-down-lateral-movement/) · Blog oficial · Oficial · Microsoft Defender Security Research Team · Microsoft Security Blog · 17 abr 2026. Caso real de compromiso de dominio en el que la interrupción automática y el 'predictive shielding' contuvieron identidades de alto privilegio expuestas y frenaron el movimiento lateral.
- [Case study: How predictive shielding in Defender stopped GPO-based ransomware before it started](https://www.microsoft.com/en-us/security/blog/2026/03/23/case-study-predictive-shielding-defender-stopped-gpo-based-ransomware-before-started/) · Blog oficial · Oficial · Microsoft Defender Security Research Team · Microsoft Security Blog · 23 mar 2026. Caso en el que la interrupción de cuentas comprometidas y el predictive shielding bloquearon ransomware distribuido por GPO tras Kerberoasting y volcado de NTDS.

### Webinars, videos y podcasts

- [A Deep Dive into Automated Attack Disruption](https://www.youtube.com/watch?v=5nk6d170Cnw) · Webinar · Empleado de Microsoft · Ayelet Artzi, Christos Ventouris · YouTube - Microsoft Security Community · 9 dic 2025. Webinar del equipo de producto con demo, notificaciones, Action center, hunting, disrupción en terceros y predictive shielding.
- [The future of identity protection with Predictive Shielding (Virtual Ninja Show)](https://www.youtube.com/watch?v=u9nXRABIw1k) · Webinar · Empleado de Microsoft · Nimrod Roimy y Aviv Sharon · Microsoft Security Community (YouTube). Episodio del Virtual Ninja Show sobre cómo predictive shielding usa grafos de rutas de ataque para endurecer dispositivos con identidades críticas y bloquear compromisos de dominio.
- [Microsoft Defender | Attack Disruption on external sources](https://www.youtube.com/watch?v=M_9u--5hHn0) · Video · Oficial · Vista previa · Microsoft Security · YouTube - Microsoft Security. Video corto que demuestra attack disruption sobre AWS, Okta y Proofpoint a partir de señales correlacionadas en un incidente unificado. *Nota:* Integraciones con terceros vía Sentinel en preview

**Manos a la obra**

1. `Laboratorio` Configura los niveles de automatización por grupo de dispositivos (completo para el grupo de laboratorio y semiautomático para un grupo piloto) y practica aprobar, rechazar y deshacer acciones de AIR de MDO en el [Action center](https://learn.microsoft.com/en-us/defender-xdr/m365d-action-center). Evidencia: historial con una acción aprobada, una rechazada y una deshecha.
2. `Laboratorio parcial` Revisa en el inquilino de prueba los requisitos de la interrupción automática —descubrimiento de dispositivos, versión del sensor y auditoría de buzones— y configura exclusiones solo para las cuentas de emergencia ([configurar la interrupción](https://learn.microsoft.com/en-us/defender-xdr/configure-attack-disruption)). Limitación: la interrupción real solo ocurre ante ataques reales de alta confianza y no se puede forzar. Evidencia: lista de verificación con brechas y responsables.
3. `Laboratorio` Prepara y guarda una consulta sobre `DisruptionAndResponseEvents` (GA desde junio de 2026) que liste las acciones de interrupción por entidad y tipo; en el laboratorio quedará vacía, pero la usarás en producción y en [S3](04_Nivel_4_Excelencia_del_SOC.md#s3). Evidencia: consulta guardada con su descripción.
4. `Laboratorio` Completa para tu organización la tabla de decisión de este módulo: qué mecanismo de respuesta usarás en cinco escenarios (phishing reportado, malware en un equipo, robo de token, ransomware y cuenta privilegiada expuesta). Evidencia: tabla aprobada por el líder del SOC.
5. `Laboratorio` Mira el webinar [A Deep Dive into Automated Attack Disruption](https://www.youtube.com/watch?v=5nk6d170Cnw) y documenta cada acción de contención y cómo se revierte. Evidencia: procedimiento de reversión de una página.
6. `Solo producción` Valida la interrupción automática en producción. Requiere señales reales de alta confianza y un despliegue amplio de MDE, MDI, MDO y Defender for Cloud Apps. Cómo hacerlo seguro: revisa las exclusiones (solo cuentas de emergencia y servidores críticos documentados), usa roles de solo lectura para la revisión y haz un ejercicio de mesa sobre qué hacer cuando la interrupción contiene a un usuario VIP ([exclusiones](https://learn.microsoft.com/en-us/defender-xdr/automatic-attack-disruption-exclusions)).

**¿Quieres profundizar?**

- [The future of identity protection with Predictive Shielding (Virtual Ninja Show)](https://www.youtube.com/watch?v=u9nXRABIw1k) · Webinar
- [Microsoft Defender | Attack Disruption on external sources](https://www.youtube.com/watch?v=M_9u--5hHn0) · Video

<a id="m8"></a>

## M8 · Integración con Microsoft Sentinel

*L300 · ~8 h · Origen: Ninja oficial de Defender XDR, Expert (APIs e integración con SIEM), actualizado a la plataforma unificada*

Defender XDR y Microsoft Sentinel ya no son dos consolas: Sentinel está en disponibilidad general dentro del portal de Defender y, después del **31 de marzo de 2027**, deja de tener soporte en el portal de Azure. Al incorporar un workspace como **primario**, el conector de Defender XDR se configura solo, los conectores independientes de MDE, MDI, MDO, alertas de Defender for Cloud Apps y Entra ID Protection se desconectan, y alertas e incidentes de ambos mundos comparten correlación, cola, búsqueda avanzada y automatización.

Las decisiones importantes son de datos y costos: las alertas e incidentes de Defender XDR se ingieren en Sentinel sin cargo, pero las tablas de búsqueda avanzada (`DeviceProcessEvents`, `EmailEvents`…) sí se cobran; los datos de XDR tienen 30 días en analítica sin costo y pueden extenderse a 90 días o enviarse al data lake, con retención de hasta 12 años. Este módulo te enseña a incorporar, a decidir qué tablas llevar y a qué nivel, y a evitar las trampas de la transición. La profundidad de Sentinel está en su propio programa.

**Por qué importa**

Correlacionar las señales de XDR con identidad, red, nube y terceros es lo que convierte alertas aisladas en historias completas, y hacerlo en un solo portal elimina el cambio de contexto que más tiempo le roba al analista. Decidir bien qué tablas de XDR ingerir y a qué nivel puede significar miles de dólares al mes de diferencia sin perder capacidad de detección.

**Qué vas a lograr**

- Incorporar un workspace primario al portal de Defender y verificar el conector de Defender XDR.
- Explicar qué datos de XDR se ingieren gratis, cuáles se cobran y cómo cambia la retención.
- Diseñar el modelo de workspace primario y secundarios.
- Adaptar automatizaciones y reglas a la plataforma unificada.

> **Novedad.** Sentinel está en GA en el portal de Defender, con o sin Defender XDR o E5, y después del **31 de marzo de 2027** deja de estar soportado en el portal de Azure ([búsqueda con datos de Sentinel](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-microsoft-defender)); la fecha original era el 1 de julio de 2026 y se extendió el 29 de enero de 2026 ([anuncio](https://techcommunity.microsoft.com/blog/microsoftsentinelblog/update-new-timeline-for-transitioning-sentinel-experience-to-defender-portal/4490464)). Quien incorporó Sentinel por primera vez después del 1 de julio de 2025 con rol Owner o User Access Administrator quedó en el portal de Defender de forma automática.

> **Atención.** Al incorporar el workspace con licencia de Defender XDR, el conector de Defender XDR se configura solo y se desconectan los conectores independientes de Defender for Cloud Apps (alertas), MDE, MDI, MDO y Entra ID Protection. Las «Microsoft incident creation rules» no existen en el portal de Defender, no conviene condicionar automatizaciones al título del incidente (usa etiquetas) y los incidentes de Sentinel admiten hasta 150 alertas ([integración](https://learn.microsoft.com/en-us/azure/sentinel/microsoft-365-defender-sentinel-integration)).

> **Atención.** Costos: las alertas y los incidentes (`SecurityAlert`, `SecurityIncident`) se ingieren sin cargo; las tablas de búsqueda como `DeviceInfo`, `DeviceFileEvents` o `EmailEvents` sí se cobran, y las de gestión de vulnerabilidades no se ingieren. Los datos de XDR tienen 30 días sin costo en el nivel de análisis; extenderlos a 90 días cuesta ingesta, y también puedes enviarlos solo al data lake con retención total de hasta 12 años ([niveles y retención](https://learn.microsoft.com/en-us/azure/sentinel/manage-data-overview)). La comunidad cita unos 0,05 USD por GB de ingesta y 0,10 USD por GB de procesamiento en el lago: contrástalo con el estimador oficial ([log tiering](https://charbelnemnom.com/log-tiering-with-microsoft-sentinel-data-lake/)).

> **Consejo Ninja.** Cada inquilino tiene un workspace primario y secundarios ilimitados, y las alertas e incidentes de Defender XDR solo se sincronizan con el primario ([varios workspaces](https://learn.microsoft.com/en-us/azure/sentinel/workspaces-defender-portal)). Elige el primario con criterio de operación, no solo de costo. El SIEM se profundiza en el programa de Sentinel.

**¿Tienes poco tiempo?**

- [Microsoft Defender XDR integration with Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/microsoft-365-defender-sentinel-integration) · Documentación
- [Connect Microsoft Sentinel to the Microsoft Defender portal](https://learn.microsoft.com/en-us/azure/sentinel/microsoft-sentinel-onboard) · Documentación
- [Multiple Microsoft Sentinel workspaces in the Defender portal](https://learn.microsoft.com/en-us/azure/sentinel/workspaces-defender-portal) · Documentación
- [UPDATE: New timeline for transitioning Sentinel experience to Defender portal](https://techcommunity.microsoft.com/blog/microsoftsentinelblog/update-new-timeline-for-transitioning-sentinel-experience-to-defender-portal/4490464) · Blog oficial

### Documentación, cursos y credenciales

- [Microsoft Defender XDR integration with Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/microsoft-365-defender-sentinel-integration) · Documentación · Oficial · Nuevo · Microsoft Learn · 17 jun 2026. Explica el conector de Defender XDR para Sentinel: sincronización bidireccional de incidentes, transmisión de eventos de búsqueda avanzada, costos y efecto sobre las reglas de creación de incidentes de Microsoft.
- [Connect Microsoft Sentinel to the Microsoft Defender portal](https://learn.microsoft.com/en-us/azure/sentinel/microsoft-sentinel-onboard) · Documentación · Oficial · Microsoft Learn. Procedimiento para incorporar un workspace de Sentinel al portal Defender, con roles requeridos, workspace primario y secundarios, y desincorporación.
- [Multiple Microsoft Sentinel workspaces in the Defender portal](https://learn.microsoft.com/en-us/azure/sentinel/workspaces-defender-portal) · Documentación · Oficial · Microsoft Learn. Explica el modelo de un workspace primario y múltiples secundarios por tenant, dónde se sincronizan alertas e incidentes de Defender XDR y cómo afecta a conectores y correlación.
- [Manage data tiers and retention in Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/manage-data-overview) · Documentación · Oficial · Microsoft Learn. Describe los niveles analytics y data lake, la retención por tabla y las opciones para los datos XDR (30 días incluidos, extensión a 90 días con costo de ingesta o ingesta directa al data lake).

### Anuncios y blogs oficiales

- [UPDATE: New timeline for transitioning Sentinel experience to Defender portal](https://techcommunity.microsoft.com/blog/microsoftsentinelblog/update-new-timeline-for-transitioning-sentinel-experience-to-defender-portal/4490464) · Blog oficial · Empleado de Microsoft · aklausner · Microsoft Tech Community - Microsoft Sentinel Blog · 29 ene 2026. Anuncia la extensión de la fecha de retiro de Sentinel en el portal de Azure del 1 de julio de 2026 al 31 de marzo de 2027 y enumera capacidades exclusivas del portal Defender.
- [Planning your move to Microsoft Defender portal for all Microsoft Sentinel customers](https://techcommunity.microsoft.com/blog/microsoft-security-blog/planning-your-move-to-microsoft-defender-portal-for-all-microsoft-sentinel-custo/4428613) · Blog oficial · Empleado de Microsoft · Legado aún útil · Tomer Brand · Microsoft Tech Community - Microsoft Security Community Blog · 1 jul 2025. Explica la estrategia de operaciones de seguridad unificadas y por qué planificar el paso de Sentinel al portal Defender. *Nota:* La fecha de retiro del 2026-07-01 indicada aquí fue extendida al 2027-03-31 (blog de enero de 2026)

### Comunidad: blogs, libros, newsletters y eventos

- [Microsoft Sentinel Cost Estimation And Optimization — The Definitive Guide!](https://charbelnemnom.com/sentinel-cost-estimation-and-optimization/) · Blog · MVP · Nuevo · Charbel Nemnom · charbelnemnom.com · 22 jun 2026. Guía extensa y actualizada de costos de Sentinel (niveles analytics y data lake, compromisos, beneficio E5, fuentes gratuitas y envío de datos de hunting XDR directo al data lake).
- [Log Tiering With Microsoft Sentinel Data Lake](https://charbelnemnom.com/log-tiering-with-microsoft-sentinel-data-lake/) · Blog · MVP · Charbel Nemnom · charbelnemnom.com · 9 abr 2026. Explica el escalonamiento de logs entre analytics y data lake de Sentinel, incluida la transmisión directa de tablas XDR compatibles (MDE/MDO/MDA) al data lake manteniendo 30 días de retención XDR.

**Manos a la obra**

1. `Laboratorio parcial` Crea un workspace con Sentinel, incorpóralo como primario al portal de Defender ([conectar Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/microsoft-sentinel-onboard)), extiende `DeviceProcessEvents` a 90 días y consulta juntos datos de XDR y `SigninLogs`. Limitación: consume crédito de Azure por ingesta y el volumen del inquilino de prueba es mínimo; mantén la retención corta y borra el workspace al terminar. En producción, incorpora en ventana de cambio, cambia la retención en una sola tabla piloto y activa alertas de presupuesto. Evidencia: conector activo y consulta combinada.
2. `Laboratorio` Verifica que `SecurityIncident` y `SecurityAlert` llegan al workspace y que los conectores independientes de MDE, MDI, MDO y Entra ID Protection quedaron desconectados ([integración](https://learn.microsoft.com/en-us/azure/sentinel/microsoft-365-defender-sentinel-integration)). Evidencia: consulta y captura de la página de conectores.
3. `Laboratorio` Inventaria las reglas de automatización y de análisis que dependen del título del incidente o de conectores independientes y reescríbelas con etiquetas. Evidencia: lista de reglas con el antes y el después.
4. `Laboratorio` Diseña el modelo de workspaces para una organización con operaciones en tres países: cuál es el primario, qué datos van a los secundarios y quién accede a cada uno ([varios workspaces](https://learn.microsoft.com/en-us/azure/sentinel/workspaces-defender-portal)). Evidencia: diagrama con la justificación.
5. `Laboratorio` Desde la búsqueda avanzada, une una tabla de Sentinel con una de XDR y comprueba las limitaciones: el modo guiado y «Take actions» solo funcionan con datos de XDR, y si los datos llegan con más de 48 horas de atraso conviene usar `Timestamp` en lugar de `TimeGenerated` ([búsqueda con datos de Sentinel](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-microsoft-defender)). Evidencia: consulta y nota de limitaciones.
6. `Solo producción` Modela el costo de ingerir tablas de XDR en Sentinel o en el data lake con tus volúmenes reales ([niveles y retención](https://learn.microsoft.com/en-us/azure/sentinel/manage-data-overview)). Cómo hacerlo seguro: analiza primero con consultas de solo lectura y un rol de lector, pilota una sola tabla o un grupo de dispositivos y ten un plan de reversión de la retención.

**¿Quieres profundizar?**

- [Microsoft Sentinel Cost Estimation And Optimization — The Definitive Guide!](https://charbelnemnom.com/sentinel-cost-estimation-and-optimization/) · Blog

<a id="m9"></a>

## M9 · Hunting con búsqueda avanzada

*L300 · ~8 h · Origen: Ninja oficial de Defender XDR, Intermediate (hunting) y Ninja de Defender for Endpoint, rol SecOps*

Cazar es buscar lo que tus detecciones todavía no ven. Con la búsqueda avanzada cruzas endpoints, correo, identidades y aplicaciones en la nube —y, con Sentinel incorporado, cualquier tabla de tu workspace— para validar hipótesis: ¿alguien hizo clic en la URL de la campaña de ayer?, ¿qué cuentas hicieron reconocimiento LDAP?, ¿qué dispositivos ejecutaron el binario que apareció en un informe de inteligencia?

Este módulo construye el hábito: hipótesis, consulta, evidencia y acción. Usarás las tablas de identidad que cambiaron en 2026 (`EntraIdSignInEvents` reemplazó a `AADSignInEventsBeta` el 19 de octubre), el asistente «Take action» para responder desde los resultados y los mejores repositorios de la comunidad, mantenidos por MVP que publican consultas cada semana.

**Por qué importa**

El hunting proactivo encuentra intrusiones que eluden las reglas, reduce el tiempo de permanencia y, sobre todo, alimenta la ingeniería de detección: cada hipótesis confirmada se convierte en una regla. Un SOC que caza con regularidad mejora su cobertura de ATT&CK con evidencia, no con suposiciones.

**Qué vas a lograr**

- Formular hipótesis de caza y traducirlas a consultas KQL multidominio.
- Consultar en una misma búsqueda datos de Defender XDR y de Sentinel.
- Usar las tablas de identidad vigentes y migrar consultas antiguas.
- Responder desde los resultados con el asistente Take action.
- Reutilizar y adaptar consultas de la comunidad con criterio.

> **Novedad.** Tablas de identidad vigentes: `EntraIdSignInEvents` reemplazó a `AADSignInEventsBeta` el 19 de octubre de 2026 con migración automática de consultas y detecciones, y requiere Entra ID P2 ([EntraIdSignInEvents](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-entraidsigninevents-table)); `IdentityLogonEvents` registra autenticaciones de AD y de servicios en línea, pero no los inicios no interactivos de Entra ([IdentityLogonEvents](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-identitylogonevents-table)); `IdentityQueryEvents` incluye búsquedas LDAP por ADWS desde diciembre de 2025, e `IdentityAccountInfo` (enero de 2026) vincula cuentas de varias fuentes a una identidad ([IdentityAccountInfo](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-identityaccountinfo-table)).

> **Atención.** Para consultar Sentinel y Defender juntos necesitas al menos Microsoft Sentinel Reader. Las consultas de Sentinel, incluido `adx()`, funcionan en la búsqueda avanzada, pero las funciones personalizadas guardadas en Sentinel no se admiten en detecciones ([búsqueda con datos de Sentinel](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-microsoft-defender)).

> **Novedad.** Desde mayo de 2026, el asistente «Take action» permite bloquear o permitir dominios de nivel superior (TLD) y hashes de adjuntos de correo directamente desde los resultados de una consulta, y el hunting graph suma escenarios de identidad ([novedades](https://learn.microsoft.com/en-us/defender-xdr/whats-new)).

> **Consejo Ninja.** Repositorios de la comunidad activos en noviembre de 2026: [Bert-Jan Pals](https://github.com/Bert-JanP/Hunting-Queries-Detection-Rules), [Alex Verboon](https://github.com/alexverboon/Hunting-Queries-Detection-Rules), [Sergio Albea](https://github.com/Sergio-Albea-Git/Threat-Hunting-KQL-Queries) y [Jay Kerai](https://github.com/jkerai1/KQL-Queries/tree/main), además del buscador [KQL Search](https://www.kqlsearch.com/) y las sesiones de [KQL Cafe](https://kqlcafe.com/) (la próxima, el 24 de noviembre de 2026). Antes de reutilizar una consulta, verifica los nombres de tablas vigentes y pruébala en el laboratorio.

**¿Tienes poco tiempo?**

- [EntraIdSignInEvents table in the advanced hunting schema](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-entraidsigninevents-table) · Documentación
- [Advanced hunting with Microsoft Sentinel data in Microsoft Defender portal](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-microsoft-defender) · Documentación
- [Bert-JanP/Hunting-Queries-Detection-Rules](https://github.com/Bert-JanP/Hunting-Queries-Detection-Rules) · GitHub
- [KQL Search - Search engine for KQL Queries](https://www.kqlsearch.com/) · Herramienta

### Documentación, cursos y credenciales

- [Advanced hunting with Microsoft Sentinel data in Microsoft Defender portal](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-microsoft-defender) · Documentación · Oficial · Nuevo · Microsoft Learn · 23 sep 2026. Describe cómo consultar en una sola búsqueda avanzada datos de Defender XDR y de un espacio de trabajo de Sentinel incorporado, con roles necesarios, retención y limitaciones conocidas.
- [EntraIdSignInEvents table in the advanced hunting schema](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-entraidsigninevents-table) · Documentación · Oficial · Nuevo · Microsoft Learn · 3 ago 2026. Referencia de la tabla de hunting que contiene inicios de sesión interactivos y no interactivos de Entra ID y que reemplaza a AADSignInEventsBeta.
- [IdentityLogonEvents table in the advanced hunting schema](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-identitylogonevents-table) · Documentación · Oficial · Microsoft Learn. Referencia de la tabla con autenticaciones de AD local capturadas por Defender for Identity y de servicios en línea capturadas por Defender for Cloud Apps, con tipos de logon soportados.
- [IdentityAccountInfo table in the advanced hunting schema](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-identityaccountinfo-table) · Documentación · Oficial · Microsoft Learn. Nueva tabla de hunting con información de cuentas de múltiples proveedores (Entra ID, AD, otros IdP) vinculadas a una identidad, con criticidad, riesgo de Defender, MFA registrados y roles.
- [IdentityInfo table in the advanced hunting schema](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-identityinfo-table) · Documentación · Oficial · Microsoft Learn. Referencia de la tabla unificada de información de cuentas (antes AccountInfo) con criticidad, nivel de riesgo de Entra, etiquetas de MDI, roles asignados y roles PIM (preview).
- [IdentityQueryEvents table in the advanced hunting schema](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-identityqueryevents-table) · Documentación · Oficial · Microsoft Learn · 20 jun 2025. Referencia de la tabla con consultas contra objetos de AD (LDAP, SAMR, DNS, ADWS) útil para cazar reconocimiento.
- [IdentityDirectoryEvents table in the advanced hunting schema](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-identitydirectoryevents-table) · Documentación · Oficial · Nuevo · Microsoft Learn · 26 jun 2026. Referencia de la tabla con eventos de controladores de dominio (cambios de contraseña, UPN, tareas programadas, PowerShell) poblada por Defender for Identity.
- [Azure Monitor Logs reference - SigninLogs](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/signinlogs) · Documentación · Oficial · Microsoft Learn. Esquema de la tabla de inicios de sesión interactivos de Entra ID en Log Analytics/Sentinel, incluida la nueva columna Agent para inicios de sesión agénticos.
- [Azure Monitor Logs reference - AADNonInteractiveUserSignInLogs](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/AADNonInteractiveUserSignInLogs) · Documentación · Oficial · Microsoft Learn. Esquema de la tabla de inicios de sesión no interactivos de usuarios (renovación de tokens), clave para cazar robo y repetición de tokens.

### Laboratorios, GitHub y herramientas

- [KQL Search - Search engine for KQL Queries](https://www.kqlsearch.com/) · Herramienta · MVP · Nuevo · Ugur Koc · Ugur Labs · nov 2026. Buscador comunitario que indexa consultas KQL públicas para Sentinel, Defender y ADX con filtros por tabla, autor y fecha, además de herramientas de IA y MCP.
- [Bert-JanP/Hunting-Queries-Detection-Rules](https://github.com/Bert-JanP/Hunting-Queries-Detection-Rules) · GitHub · MVP · Nuevo · Bert-Jan Pals · GitHub · oct 2026. Repositorio comunitario de referencia con cientos de consultas KQL de hunting y detección para Defender XDR y Sentinel, mapeadas a MITRE ATT&CK, con plantilla de detección y casos DFIR.
- [Hunting-Queries-Detection-Rules (KQL for Defender XDR & Sentinel)](https://github.com/alexverboon/Hunting-Queries-Detection-Rules) · GitHub · MVP · Nuevo · Alex Verboon · GitHub (alexverboon) · nov 2026. Repositorio MIT con consultas KQL de detección, hunting y auditoría para MDE, MDI, MDO, MDCA, Exposure Management y Entra, con plantilla y mapeo MITRE.
- [SlimKQL/Hunting-Queries-Detection-Rules (KQLWizard)](https://github.com/SlimKQL/Hunting-Queries-Detection-Rules) · GitHub · MVP · Nuevo · Steven Lim · GitHub · nov 2026. Repositorio de Steven Lim con cientos de consultas de hunting y detección para Defender XDR, Sentinel, Azure y ADX, más enlaces a su comunidad de detecciones.
- [Sergio-Albea-Git/Threat-Hunting-KQL-Queries](https://github.com/Sergio-Albea-Git/Threat-Hunting-KQL-Queries) · GitHub · MVP · Nuevo · Sergio Albea · GitHub · nov 2026. Repositorio muy activo de Sergio Albea con consultas KQL para Defender XDR, recolectores de IOC hacia MISP, listas de dominios falsos de Microsoft y comandos ClickFix actualizados automáticamente.
- [jkerai1/KQL-Queries](https://github.com/jkerai1/KQL-Queries/tree/main) · GitHub · MVP · Nuevo · Jay Kerai · GitHub · oct 2026. Colección de consultas KQL de Jay Kerai para Defender (MDE, MDA, TVM), Entra y Office 365, incluidas detecciones de manipulación de MDE y de cambios en detecciones personalizadas.

### Comunidad: blogs, libros, newsletters y eventos

- [KQL Cafe](https://kqlcafe.com/) · Evento · MVP · Nuevo · Gianni Castaldi y Alex Verboon · KQL Cafe · nov 2026. Comunidad y show mensual sobre KQL para Sentinel y Defender XDR con charlas de expertos, demos y grabaciones en YouTube.

**Manos a la obra**

1. `Laboratorio` Formula la hipótesis «un usuario hizo clic en una URL de phishing y luego inició sesión desde una IP nueva» y tradúcela a una consulta que una `UrlClickEvents` con `EntraIdSignInEvents`. Evidencia: hipótesis, consulta, resultado y conclusión en una ficha de hunting.
2. `Laboratorio` Ejecuta en el laboratorio una enumeración LDAP o ADWS benigna, cázala en `IdentityQueryEvents` ([IdentityQueryEvents](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-identityqueryevents-table)), correlaciónala con `IdentityLogonEvents` e `IdentityInfo` y termina consultando `EntraIdSignInEvents` por nivel de riesgo agregado. Evidencia: tres consultas encadenadas.
3. `Laboratorio` Busca en tus consultas guardadas y repositorios referencias a `AADSignInEventsBeta` y adáptalas a `EntraIdSignInEvents`, verificando las columnas equivalentes. Evidencia: diferencias antes y después.
4. `Laboratorio` Desde los resultados de una consulta sobre adjuntos, usa «Take action» para bloquear el hash de un archivo de prueba y luego revierte el bloqueo ([novedades](https://learn.microsoft.com/en-us/defender-xdr/whats-new)). Evidencia: la entrada creada y su eliminación en el historial.
5. `Laboratorio parcial` Repite la hipótesis del primer ejercicio sumando `SigninLogs` y `AADNonInteractiveUserSignInLogs` del workspace de [M8](#m8) ([SigninLogs](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/signinlogs)). Limitación: el volumen del laboratorio es bajo y los registros no interactivos generan costo de ingesta; conéctalos solo durante el ejercicio. Evidencia: consulta combinada.
6. `Laboratorio` Toma cinco consultas de los repositorios de la comunidad o de [KQL Search](https://www.kqlsearch.com/), pruébalas en el laboratorio y regístralas en la biblioteca del equipo con fuente, tablas, adaptación y fecha de revisión. Evidencia: cinco entradas en la biblioteca.

**¿Quieres profundizar?**

- [Hunting-Queries-Detection-Rules (KQL for Defender XDR & Sentinel)](https://github.com/alexverboon/Hunting-Queries-Detection-Rules) · GitHub
- [SlimKQL/Hunting-Queries-Detection-Rules (KQLWizard)](https://github.com/SlimKQL/Hunting-Queries-Detection-Rules) · GitHub
- [Sergio-Albea-Git/Threat-Hunting-KQL-Queries](https://github.com/Sergio-Albea-Git/Threat-Hunting-KQL-Queries) · GitHub
- [KQL Cafe](https://kqlcafe.com/) · Evento

<a id="m10"></a>

## M10 · Detecciones personalizadas y ajuste de alertas

*L300 · ~10 h · Origen: Ninja de Defender for Endpoint, rol SecOps (detecciones personalizadas e indicadores), actualizado a la experiencia unificada*

Desde el **28 de octubre de 2025**, las **detecciones personalizadas** son la experiencia unificada para crear reglas sobre datos de Defender XDR y de Sentinel: una consulta de búsqueda avanzada programada que genera alertas con entidades mapeadas, títulos dinámicos, detalles personalizados y acciones de respuesta automáticas sobre dispositivos, archivos, usuarios y correos. Las reglas de análisis de Sentinel siguen funcionando, pero las reglas nuevas conviene crearlas aquí.

La otra mitad del trabajo es quitar ruido sin perder señal. El **ajuste de alertas** (alert tuning, antes alert suppression) oculta, resuelve o convierte alertas en comportamientos con hasta 200 condiciones por regla; las reglas integradas están en GA desde abril de 2026 y la selección por fuente de detección entra en vigor el **8 de noviembre de 2026**. Este módulo te enseña a escribir, probar, desplegar y ajustar detecciones con disciplina de ingeniería.

**Por qué importa**

Las detecciones propias cubren lo que el producto no sabe de tu negocio: tus cuentas privilegiadas, tus aplicaciones críticas, tus patrones de abuso. Y el ajuste disciplinado reduce la fatiga del analista: cada falso positivo eliminado con una regla documentada es tiempo devuelto a investigar lo que importa.

**Qué vas a lograr**

- Crear detecciones personalizadas con columnas requeridas, entidades y acciones de respuesta.
- Elegir frecuencia y lookback según la fuente de datos, incluido NRT.
- Diseñar reglas de ajuste de alertas sin crear puntos ciegos.
- Gestionar detecciones por API y prepararlas para el ciclo como código.

> **Qué cambió.** Desde el 28 de octubre de 2025, las detecciones personalizadas son la experiencia unificada para crear reglas sobre datos de Defender XDR y de Sentinel; las reglas de análisis siguen disponibles sin migración inmediata y las reglas NRT no tienen límite de cantidad ([anuncio](https://techcommunity.microsoft.com/t5/microsoft-defender-xdr-blog/custom-detections-are-now-the-unified-experience-for-creating/ba-p/4463875)).

> **Atención.** Frecuencias: Continuous (NRT), 1, 3, 12 o 24 horas; «Custom» (5 minutos a 14 días) solo si la regla usa exclusivamente datos de Sentinel. NRT exige una sola tabla, sin `join`, `union`, `externaldata` ni comentarios, y solo columnas GA. Cada ejecución genera hasta 150 alertas, los detalles personalizados admiten 20 pares clave-valor y 4 KB, y el título dinámico usa hasta 3 columnas ([crear detecciones](https://learn.microsoft.com/en-us/defender-xdr/custom-detection-rules)). Hay contradicciones documentales sobre NRT con datos de Sentinel: revisa [Metodología y fuentes](08_Cierre_glosario_y_fuentes.md#metodologia).

> **Novedad.** El ajuste de alertas (antes alert suppression) admite hasta 200 condiciones por regla y las acciones Hide (solo MDE), Resolve y Set as behavior (no para MDO ni Defender for Cloud). Las reglas integradas están en GA desde abril de 2026 y la selección por detection source (vista previa) entra en vigor el **8 de noviembre de 2026**: las reglas no editadas seguirán aplicando a todas las fuentes, incluidas tus detecciones personalizadas ([ajuste de alertas](https://learn.microsoft.com/en-us/defender-xdr/investigate-alerts)).

> **Consejo Ninja.** Permisos: Security settings (manage) o Security Administrator para crear reglas, y Microsoft Sentinel Contributor si usan datos de Sentinel ([crear detecciones](https://learn.microsoft.com/en-us/defender-xdr/custom-detection-rules)). Las detecciones personalizadas entran en la correlación de incidentes por defecto y puedes excluir una regla si lo necesitas ([gestionar detecciones](https://learn.microsoft.com/en-us/defender-xdr/custom-detection-manage)).

**¿Tienes poco tiempo?**

- [Custom detections overview](https://learn.microsoft.com/en-us/defender-xdr/custom-detections-overview) · Documentación
- [Create custom detection rules in Microsoft Defender XDR](https://learn.microsoft.com/en-us/defender-xdr/custom-detection-rules) · Documentación
- [Custom detections are now the unified experience for creating detections in Microsoft Defender](https://techcommunity.microsoft.com/t5/microsoft-defender-xdr-blog/custom-detections-are-now-the-unified-experience-for-creating/ba-p/4463875) · Blog oficial
- [Investigate alerts in Microsoft Defender XDR (Built-in alert tuning rules / Tune an alert)](https://learn.microsoft.com/en-us/defender-xdr/investigate-alerts) · Documentación

**Frecuencia y lookback de las detecciones personalizadas**

| Frecuencia | Lookback con datos de Defender XDR | Notas |
|---|---|---|
| Continuous (NRT) | Casi en tiempo real | Una sola tabla, sin join, union, externaldata ni comentarios y solo con columnas GA; sin límite de cantidad de reglas |
| Cada hora | 4 horas | Lookback fijo cuando la regla usa datos de Defender XDR |
| Cada 3 horas | 12 horas | Lookback fijo cuando la regla usa datos de Defender XDR |
| Cada 12 horas | 48 horas | Lookback fijo cuando la regla usa datos de Defender XDR |
| Cada 24 horas | 30 días | Lookback fijo; útil para patrones de baja frecuencia |
| Custom (de 5 minutos a 14 días) | No disponible con datos de Defender XDR | Solo si la regla usa exclusivamente datos de Sentinel; la extensión a otras fuentes se publicó y se revirtió en octubre de 2026 |

Fuente: [crear detecciones personalizadas](https://learn.microsoft.com/en-us/defender-xdr/custom-detection-rules). Cada ejecución genera hasta 150 alertas.

### Documentación, cursos y credenciales

- [Create custom detection rules in Microsoft Defender XDR](https://learn.microsoft.com/en-us/defender-xdr/custom-detection-rules) · Documentación · Oficial · Nuevo · Microsoft Learn · 4 oct 2026. Guía paso a paso para crear reglas de detección personalizadas: columnas requeridas, frecuencias (NRT, 1/3/12/24 h, personalizada para datos de Sentinel), lookback, enriquecimiento de alertas, mapeo de entidades y acciones automáticas sobre dispositivos, archivos, usuarios y correos.
- [Investigate alerts in Microsoft Defender XDR (Built-in alert tuning rules / Tune an alert)](https://learn.microsoft.com/en-us/defender-xdr/investigate-alerts) · Documentación · Oficial · Nuevo · Microsoft Learn · 10 sep 2026. Explica la investigación y clasificación de alertas y el ajuste de alertas (antes supresión) con reglas integradas y personalizadas que ocultan, resuelven o convierten alertas en comportamientos.
- [Custom detections overview](https://learn.microsoft.com/en-us/defender-xdr/custom-detections-overview) · Documentación · Oficial · Nuevo · Microsoft Learn · 6 jul 2026. Introduce las detecciones personalizadas basadas en consultas de búsqueda avanzada que generan alertas y acciones de respuesta automáticas, incluida su gestión como código (preview).

### Anuncios y blogs oficiales

- [Detection and automation, reimagined (Part 3 of 6 - The USX Transition Series)](https://techcommunity.microsoft.com/blog/microsoftsentinelblog/detection-and-automation-reimagined/4527933) · Blog oficial · Empleado de Microsoft · Nuevo · Mohit Kumar (con Lizet Pena, Caroline Mutua, Alvin Kua y Marco Sudahl) · Microsoft Tech Community - Microsoft Sentinel Blog · 18 jun 2026. Explica cómo evolucionan reglas de análisis, detecciones personalizadas, playbooks, workbooks y hunting al mover Sentinel al portal Defender, incluida la sustitución de Fusion por el motor de correlación de Defender.
- [Custom detections are now the unified experience for creating detections in Microsoft Defender](https://techcommunity.microsoft.com/t5/microsoft-defender-xdr-blog/custom-detections-are-now-the-unified-experience-for-creating/ba-p/4463875) · Blog oficial · Empleado de Microsoft · Noa Nutkevitch (coautor Jeremy Tan) · Microsoft Tech Community - Microsoft Defender XDR Blog · 28 oct 2025. Anuncia que las detecciones personalizadas pasan a ser la experiencia unificada para crear reglas sobre datos de Defender XDR y Sentinel, manteniendo disponibles las reglas de análisis.
- [Custom detection rules get a boost—explore what's new in Microsoft Defender](https://techcommunity.microsoft.com/t5/microsoft-defender-xdr-blog/custom-detection-rules-get-a-boost-explore-what-s-new-in/ba-p/4443602) · Blog oficial · Empleado de Microsoft · Noa Nutkevitch (coautor Jeremy Tan) · Microsoft Tech Community - Microsoft Defender XDR Blog · 3 sep 2025. Presenta las mejoras de las detecciones personalizadas (lista unificada de reglas, títulos dinámicos, mapeo avanzado de entidades, detalles personalizados, soporte de datos solo de Sentinel) y sus ventajas de costo frente a ingerir datos XDR en Sentinel.

**Manos a la obra**

1. `Laboratorio` Convierte una consulta de una sola tabla sobre `DeviceProcessEvents` en una regla Continuous (NRT) con la acción «Collect investigation package» limitada a un grupo de dispositivos de prueba, y comprueba la deduplicación de alertas ([crear detecciones](https://learn.microsoft.com/en-us/defender-xdr/custom-detection-rules)). Evidencia: regla, alerta y paquete recolectado.
2. `Laboratorio` Agrega a la regla el mapeo de entidades, un título dinámico con hasta tres columnas y detalles personalizados. Evidencia: alerta con el título dinámico y los detalles visibles.
3. `Laboratorio parcial` Genera una alerta benigna repetible en el cliente de prueba y crea una regla de ajuste «Resolve alert» con condiciones de archivo y proceso; valida que la alerta queda resuelta y sigue en `AlertInfo`, y revisa la configuración por detection source ([ajuste de alertas](https://learn.microsoft.com/en-us/defender-xdr/investigate-alerts)). Limitación: sin falsos positivos reales el ejercicio no muestra todo el valor del ajuste. Evidencia: regla y alerta resuelta.
4. `Laboratorio` Recrea la regla por API con `POST /security/rules/detectionRules` (beta) y el permiso `CustomDetection.ReadWrite.All`, usando `status` en lugar de las propiedades eliminadas el 1 de octubre de 2026 ([crear detectionRule](https://learn.microsoft.com/en-us/graph/api/security-rulesroot-post-detectionrules?view=graph-rest-beta)). Evidencia: JSON de la regla en tu repositorio.
5. `Laboratorio parcial` Crea una detección personalizada solo con datos de Sentinel (`SigninLogs` del workspace de [M8](#m8)) y frecuencia «Custom». Limitación: requiere el workspace incorporado y su costo, y el alcance de esta frecuencia cambió en la documentación durante 2026. Evidencia: regla con su frecuencia y lookback.
6. `Solo producción` Ajusta reglas sobre el ruido real de tu SOC. Requiere volumen real de alertas y falsos positivos. Cómo hacerlo seguro: analiza primero con consultas de solo lectura, usa reglas «Resolve» y no «Hide», limita el alcance, documenta la reversión y revisa las reglas cada mes.

<a id="reto-intermedio"></a>

## Reto del nivel

**Del hallazgo a la detección, con costo controlado.** Elige un riesgo concreto —por ejemplo, un phishing con AiTM contra cuentas privilegiadas—. Cázalo con una hipótesis que cruce correo, identidad y endpoint; conviértelo en una detección personalizada NRT con acción de respuesta y mapeo de entidades; agrega una regla de ajuste sin crear puntos ciegos; protege a los usuarios con directivas de riesgo en acceso condicional, y conecta el workspace de Sentinel para medir el tiempo de triage. Cierra con la estimación del costo mensual de las tablas que ingeriste y la decisión de qué mecanismo de respuesta usarías en producción.

<a id="quiz-intermedio"></a>

## Evaluación del nivel

Responde y compara con [Evaluaciones y respuestas](06_Evaluaciones_y_respuestas.md#eval-intermedio). Con 80 % o más, ¡nivel aprobado! (En la versión web puedes corregir en línea y generar tu certificado).

1. En el RBAC unificado, ¿qué permiso te deja gestionar casos de incidente (asignar, clasificar y cerrar)?
   - a) Security Data Read
   - b) Security Data Manage
   - c) Security settings (manage)
   - d) System settings (read)

2. Durante la investigación de un buzón comprometido (BEC), ¿cuál es la acción preferida según Microsoft?
   - a) Deshabilitar la cuenta
   - b) Borrar el buzón
   - c) Enviar un aviso a todos los contactos
   - d) Esperar a que termine la investigación de AIR

3. En un despliegue de reglas ASR, ¿cuáles pueden pasar directamente a Block o Warn sin una fase de auditoría?
   - a) Todas
   - b) Ninguna
   - c) Solo las reglas de Office
   - d) Las reglas de protección estándar

4. Con el antivirus de Defender en modo pasivo y EDR en modo bloqueo, ¿qué capacidad NO funciona?
   - a) La remediación de detecciones de EDR
   - b) Las reglas ASR
   - c) Las alertas de EDR
   - d) El Action center

5. ¿Por qué los mapas de rutas de movimiento lateral de Defender for Identity dejaron de actualizarse?
   - a) Por el retiro del portal clásico de MDI
   - b) Por la migración al sensor v3.x
   - c) Porque desde mayo de 2025 MDI dejó de recolectar administradores locales por SAM-R
   - d) Por falta de licencia de Exposure Management

6. Si después de migrar al sensor v3.x la cuenta de acción sigue configurada como gMSA, ¿qué ocurre?
   - a) Nada: el v3.x la convierte solo
   - b) La migración falla y vuelve al v2.x
   - c) Se desactiva el sensor
   - d) Las acciones de respuesta, incluida la interrupción automática, no funcionan

7. ¿Cuándo se retiraron las directivas de riesgo heredadas de Entra ID Protection?
   - a) El 1 de octubre de 2026
   - b) El 1 de julio de 2025
   - c) El 19 de octubre de 2026
   - d) Siguen vigentes

8. ¿Qué agrega automáticamente el control «Require risk remediation» en una directiva de riesgo de usuario?
   - a) Bloqueo de acceso y dispositivo conforme
   - b) Ubicación de confianza y MFA por SMS
   - c) Authentication strength y sign-in frequency «Every time»
   - d) Nada más

9. ¿Qué capacidad de Defender Vulnerability Management NO viene con MDE P2 sin el complemento?
   - a) El inventario de software
   - b) La evaluación de vulnerabilidades
   - c) La priorización por riesgo
   - d) La evaluación de líneas base de seguridad

10. ¿Con qué nivel de confianza actúa la interrupción automática de ataques al contener?
   - a) 80 %
   - b) 90 %
   - c) Al menos 99 %
   - d) 100 % garantizado

11. Desde el 1 de septiembre de 2026, ¿qué cambió en AIR?
   - a) Desapareció en todo Defender
   - b) En MDE deja de ser una experiencia separada y no se dispara manualmente; en MDO sigue disponible
   - c) Solo funciona con MDO Plan 1
   - d) Requiere Defender Experts

12. Al incorporar un workspace al portal de Defender con licencia de Defender XDR, ¿qué pasa con el conector independiente de MDE en Sentinel?
   - a) Se desconecta automáticamente
   - b) Sigue activo y duplica alertas
   - c) Se replica en los workspaces secundarios
   - d) Se convierte en un conector del data lake

13. ¿Qué tabla reemplazó a AADSignInEventsBeta el 19 de octubre de 2026?
   - a) SigninLogs
   - b) IdentityLogonEvents
   - c) IdentityAccountInfo
   - d) EntraIdSignInEvents

14. ¿Qué impide que una detección personalizada use la frecuencia Continuous (NRT)?
   - a) Usar un join
   - b) Usar una sola tabla
   - c) Proyectar ReportId
   - d) Consultar DeviceEvents

15. En el ajuste de alertas, ¿qué acción solo aplica a alertas de Defender for Endpoint?
   - a) Resolve alert
   - b) Set as behavior
   - c) Hide alert
   - d) Add tag

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

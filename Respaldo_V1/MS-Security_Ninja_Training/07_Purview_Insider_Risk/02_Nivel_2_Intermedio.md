# Nivel 2 · Intermedio · Políticas, investigación y respuesta proporcional

*Microsoft Purview Insider Risk Management Ninja Training · Edición 2026*

[← Nivel 1 · Inicial](01_Nivel_1_Inicial.md) · [Índice del programa](README.md) · [Nivel 3 · Avanzado →](03_Nivel_3_Avanzado.md)

<a id="intermedio"></a>

Políticas por escenario, investigación con evidencia forense y Data Security Investigations, Protección adaptativa y colaboración con RR. HH., Legal y eDiscovery. Terminas con un caso simulado de punta a punta y una respuesta proporcional al riesgo.

*L300 · 4 módulos · ~23 horas · 15 recursos*

**Módulos de este nivel:** [M1 Políticas por escenario](#m1) · [M2 Investigación y forense](#m2) · [M3 Protección adaptativa](#m3) · [M4 RR. HH., Legal y eDiscovery](#m4)

<a id="m1"></a>

## M1 · Políticas por escenario: plantillas, disparadores e indicadores

*L300 · ~8 h · Origen: Ninja oficial de IRM · «Getting Started» (políticas), ampliado con IA, agentes, navegación y apps de terceros*

Cada plantilla responde a un escenario: **Data theft by departing users** (robo de datos por usuarios que se van), **Data leaks** y sus variantes por usuarios prioritarios o por usuarios con estresores laborales (*risky users*), **Security policy violations** en sus cuatro variantes con Defender for Endpoint, **Patient data misuse** para el sector salud (vista previa), **Risky browser usage** (vista previa), **Risky AI usage** y **Risky Agents** (vista previa, activa por defecto). En 2026 se sumó una plantilla rápida para el robo de datos desde apps que no son de Microsoft 365 por usuarios que se van, en disponibilidad general desde marzo. Puedes crear hasta 100 políticas por plantilla, con configuración rápida o personalizada.

Lo importante está en los detalles. El evento desencadenante de los usuarios que se van puede ser el conector de RR. HH. o, según la página de plantillas, el borrado de la cuenta en Entra. Data leaks admite hasta 20 políticas DLP como disparador, pero solo cuentan las alertas de severidad **alta** de Exchange Online, SharePoint Online y OneDrive: Endpoint DLP, Teams, Microsoft 365 Copilot, los repositorios locales y Power BI no se evalúan. Solo Data leaks y Data leaks by priority users permiten personalizar los eventos desencadenantes, y las *collection policies* prevalecen sobre los indicadores de dispositivo de IRM si entran en conflicto. Security policy violations usa alertas de Defender for Endpoint que se importan a diario según los estados de triage que elijas.

Las **ventanas de tiempo** definen cuánto tiempo permanece un usuario en el alcance (activación de 1 a 30 días) y cuánta actividad previa se evalúa (de 0 a 90 días; 10 para correo), y el panel de políticas muestra la salud de cada una. Las políticas de agentes se gestionan aparte de las de usuarios. La configuración de las políticas DLP que actúan como disparador se profundiza en el programa de Purview DLP (módulos I2 y M2).

**Por qué importa**

La plantilla equivocada produce ruido o deja ciegos escenarios completos. Elegir por escenario de negocio —salidas, fugas, violaciones de seguridad, IA—, acotar el alcance a un piloto aprobado y documentar cada disparador reduce el impacto en la privacidad, el costo de pago por uso y el tiempo que el equipo pierde en falsos positivos.

**Qué vas a lograr**

- Elegir la plantilla adecuada para cada escenario de riesgo y justificar la elección.
- Configurar disparadores con el conector de RR. HH., el borrado de cuentas en Entra o alertas DLP de severidad alta.
- Ajustar indicadores, umbrales, contenido prioritario y variantes en una política.
- Configurar las ventanas de activación y de actividad previa y explicar su efecto.
- Leer la salud de las políticas y reconocer sus límites (100 por plantilla, 20 políticas DLP como disparador).

> **Atención.** La página de plantillas permite usar el borrado de la cuenta en Microsoft Entra en lugar del conector de RR. HH. en Data theft by departing users, pero «Get started» lista el conector como requerido para esa plantilla y para Security policy violations by departing users ([plantillas](https://learn.microsoft.com/en-us/purview/insider-risk-management-policy-templates) frente a [Get started](https://learn.microsoft.com/en-us/purview/insider-risk-management-configure)). Diseña con el conector como opción preferente y documenta qué disparador usa cada política.

> **Atención.** Data leaks admite hasta 20 políticas DLP como disparador y solo cuenta las alertas de severidad alta de Exchange Online, SharePoint Online y OneDrive; Endpoint DLP, Teams, Microsoft 365 Copilot, los repositorios locales y Power BI no se evalúan ([plantillas](https://learn.microsoft.com/en-us/purview/insider-risk-management-policy-templates); [indicadores](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-policy-indicators)). Configura esas políticas DLP con el programa de Purview DLP (módulos I2 y M2).

> **Novedad.** Plantilla rápida para el robo de datos desde apps que no son de Microsoft 365 por usuarios que se van: vista previa en febrero y disponibilidad general en marzo de 2026 ([What's new](https://learn.microsoft.com/en-us/purview/whats-new)). Sus prerrequisitos exactos —indicadores de nube conectados en Microsoft Defender y la señal de salida— y si consume pago por uso no están detallados en las fuentes revisadas: verifícalos antes de activarla.

> **Consejo Ninja.** Ventanas de política: la activación va de 1 a 30 días y la detección de actividad previa de 0 a 90 días (10 para correo) ([ventanas de política](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-policy-timeframes)); en el laboratorio, genera actividad antes y después del evento de RR. HH. para ver ambas. Recuerda también los límites: hasta 100 políticas por plantilla, y las collection policies prevalecen sobre los indicadores de dispositivo si entran en conflicto ([plantillas](https://learn.microsoft.com/en-us/purview/insider-risk-management-policy-templates)).

**¿Tienes poco tiempo?**

- [Learn about Insider Risk Management policy templates](https://learn.microsoft.com/en-us/purview/insider-risk-management-policy-templates) · Documentación
- [Create and manage Insider Risk Management policies](https://learn.microsoft.com/en-us/purview/insider-risk-management-policies) · Documentación
- [Create and manage Insider Risk Management policies](https://learn.microsoft.com/en-us/training/modules/purview-create-manage-insider-risk-policy/) · Curso
- [Learn about and configure Insider Risk Management browser signal detection](https://learn.microsoft.com/en-us/purview/insider-risk-management-browser-support) · Documentación

### Documentación, cursos y credenciales

- [Create and manage Insider Risk Management policies](https://learn.microsoft.com/en-us/purview/insider-risk-management-policies) · Documentación · Oficial · Microsoft Learn. Guía oficial para crear, priorizar contenido, usar políticas rápidas, detección de secuencias, exfiltración acumulativa y salud de políticas, separando políticas de usuario y de agente.
- [Learn about and configure Insider Risk Management browser signal detection](https://learn.microsoft.com/en-us/purview/insider-risk-management-browser-support) · Documentación · Oficial · Microsoft Learn. Requisitos y despliegue (manual, Intune o GPO) de la extensión Microsoft Compliance para Edge y Chrome que habilita señales de exfiltración y navegación riesgosa.
- [Learn about Insider Risk Management policy templates](https://learn.microsoft.com/en-us/purview/insider-risk-management-policy-templates) · Documentación · Oficial · Microsoft Learn · 21 nov 2025. Catálogo oficial de plantillas de política de IRM con prerrequisitos, eventos desencadenantes y límites por plantilla.
- [Create and manage Insider Risk Management policies](https://learn.microsoft.com/en-us/training/modules/purview-create-manage-insider-risk-policy/) · Curso · Oficial · Microsoft Learn. Módulo (36 min) que explica plantillas de política, cuándo usar políticas rápidas o personalizadas y cómo mantenerlas.

**Manos a la obra**

1. `Laboratorio` Crea `PRUEBA-IRM-SalidaEmpleados-v1` con la plantilla Data theft by departing users, alcance a los tres usuarios del CSV de I2 y el conector de RR. HH. como disparador; genera descargas y copias de archivos de prueba después de la fecha de renuncia ([plantillas](https://learn.microsoft.com/en-us/purview/insider-risk-management-policy-templates); [conector de RR. HH.](https://learn.microsoft.com/en-us/purview/import-hr-data)). Variante: una segunda política con el borrado de la cuenta en Entra como disparador. Evidencia: comparación de las alertas de ambas.
2. `Laboratorio parcial` Data leaks con DLP de severidad alta: crea una política DLP para Exchange, SharePoint y OneDrive con «Incident reports = High», asígnala como disparador y provoca coincidencias con datos sintéticos ([plantillas](https://learn.microsoft.com/en-us/purview/insider-risk-management-policy-templates)). Evidencia: alerta DLP y su efecto en IRM. Limitación: con poco volumen los umbrales casi no se alcanzan; agregar temporalmente al usuario a la política permite puntuar la actividad de los 90 días previos.
3. `Laboratorio parcial` Security policy violations: activa la integración entre Defender for Endpoint e IRM en las funciones avanzadas de MDE, incorpora la VM de I2, elige los estados de alerta a importar y genera una alerta de prueba ([plantillas](https://learn.microsoft.com/en-us/purview/insider-risk-management-policy-templates); [detecciones inteligentes](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-intelligent-detections)). Evidencia: alerta importada en IRM. Limitación: la importación es diaria y depende de los estados de triage elegidos.
4. `Laboratorio` Risky browser usage (vista previa): en la VM Windows 11 incorporada de I2 (la extensión requiere Windows 10 x64 1809 o posterior), despliega la extensión de navegador (manual, con Intune o por GPO), activa al menos un indicador de navegación y visita categorías de prueba con una cuenta de laboratorio ([señales del navegador](https://learn.microsoft.com/en-us/purview/insider-risk-management-browser-support)). Evidencia: actividad registrada por categoría y política creada.
5. `Laboratorio` Data leaks by priority users: usa el grupo prioritario de I2 y define como contenido prioritario un sitio de SharePoint con documentos de prueba; compara la severidad de las alertas con la política Data leaks general ([plantillas](https://learn.microsoft.com/en-us/purview/insider-risk-management-policy-templates)). Evidencia: dos alertas equivalentes con severidad distinta.
6. `Laboratorio` Crea una variante de indicador (por ejemplo, excluir el dominio de un socio aprobado) y documenta el orden de evaluación: exclusiones globales, variante y contenido prioritario ([indicadores](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-policy-indicators)). Evidencia: ficha de configuración y alertas antes y después de la variante.
7. `Solo producción` Patient data misuse (vista previa) para organizaciones de salud: requiere el conector Microsoft Healthcare o Epic y el conector de RR. HH. con perfil de empleado ([plantillas](https://learn.microsoft.com/en-us/purview/insider-risk-management-policy-templates); [Get started](https://learn.microsoft.com/en-us/purview/insider-risk-management-configure)). Cómo hacerlo seguro: piloto aprobado por privacidad, Legal y el comité de ética o de seguridad del paciente, alcance a una sola unidad, analistas de solo lectura y revisión mensual de accesos.

<a id="m2"></a>

## M2 · Investigación, evidencia forense y Data Security Investigations

*L300 · ~6 h · Origen: Ninja oficial de IRM (investigación de alertas), ampliado con evidencia forense y Data Security Investigations*

Investigar es reconstruir qué pasó, con proporcionalidad. Las herramientas base son el explorador de actividad, el grafo de riesgo de datos (no disponible con seudonimización), el explorador de contenido —solo para IRM Investigators— y los **informes de actividad de usuario**, que cubren hasta 90 días por usuario: los datos llegan unas 48 horas después y el informe tarda hasta 10 horas. El OCR, en vista previa y con pago por uso, extrae texto de imágenes en endpoints Windows, SharePoint y Teams, pero no en Exchange, OneDrive ni en los clips forenses.

La **evidencia forense** es la capacidad más sensible: graba clips de video de la actividad riesgosa en el dispositivo. Es un complemento opcional, desactivado por defecto, con doble autorización (los grupos IRM o IRM Admins solicitan; IRM Approvers aprueba) y captura por actividad específica o continua. Requiere Windows 10/11 Enterprise de 64 bits (incluido Windows 365) con GPU integrada, el cliente de Microsoft Purview y, en máquinas virtuales, 16 GB de RAM y 8 vCPU. Los clips se borran a los 120 días, se exportan de a 10 como máximo y se guardan en la región de Exchange Online del tenant; la prueba ofrece hasta 20 GB y la capacidad adicional se compra en bloques de 100 GB.

Cuando el caso necesita analizar contenido a escala, desde abril de 2026 los miembros del grupo de roles Insider Risk Management tienen acceso de colaborador a **Data Security Investigations** (DSI), que puede crearse directamente desde un caso con contexto en lenguaje natural y se factura por pago por uso. DSI y la cadena de custodia se profundizan en el programa de eDiscovery y Audit (módulos A4 y M4).

**Por qué importa**

Una investigación desproporcionada puede costar más que el incidente: grabar pantallas captura datos de terceros, y una conclusión sin evidencia completa expone a la organización frente al empleado y a la autoridad. La doble aprobación, el alcance mínimo, la retención limitada y el registro de cada decisión convierten la investigación en algo defendible.

**Qué vas a lograr**

- Generar e interpretar un informe de actividad de usuario y el explorador de actividad.
- Configurar la evidencia forense con doble aprobación, alcance mínimo y aviso al usuario según la política interna.
- Explicar los requisitos, los costos y la retención de los clips forenses.
- Escalar un caso a Data Security Investigations estimando su costo.
- Documentar la cadena de decisiones y de evidencia de una investigación.

> **Atención.** Evidencia forense: complemento opcional, desactivado por defecto y con doble autorización (los grupos IRM o IRM Admins solicitan; IRM Approvers aprueba). Requisitos: Windows 10/11 Enterprise de 64 bits (incluido Windows 365) con GPU integrada —no discreta—, el cliente de Microsoft Purview y, en VM, 16 GB de RAM y 8 vCPU. Los clips se borran a los 120 días y se exportan de a 10 como máximo; la captura de Enhanced Phishing Protection está en vista previa. Página actualizada el 3 de noviembre de 2026 ([evidencia forense](https://learn.microsoft.com/en-us/purview/insider-risk-management-forensic-evidence)).

> **Atención.** La misma página dice que los clips se borran a los 120 días «o al final del período de vista previa», un texto que parece heredado. La capacidad de prueba llega a 20 GB y la adicional se vende en bloques de 100 GB («Microsoft 365 Insider Risk Management Forensic Evidence – additional 100 GB capacity») ([evidencia forense](https://learn.microsoft.com/en-us/purview/insider-risk-management-forensic-evidence); [CDW](https://www.cdw.com/product/microsoft-365-insider-risk-management-forensic-evidence-subscription-lice/7387563)): confirma el estado comercial con tu revendedor.

> **Novedad.** Desde abril de 2026, los miembros del grupo de roles Insider Risk Management tienen acceso de colaborador a Data Security Investigations (rol Data Security Investigation Contributor), y la investigación puede crearse desde un caso de IRM ([What's new](https://learn.microsoft.com/en-us/purview/whats-new); [crear una investigación](https://learn.microsoft.com/en-us/purview/data-security-investigations-investigation)). DSI se factura por pago por uso: almacenamiento y unidades de cómputo ([facturación de DSI](https://learn.microsoft.com/en-us/purview/data-security-investigations-billing)).

> **Consejo Ninja.** Los informes de actividad de usuario cubren hasta 90 días; los datos llegan unas 48 horas después, el informe tarda hasta 10 horas y se requiere el grupo IRM Investigators ([informes](https://learn.microsoft.com/en-us/purview/insider-risk-management-reports)). El OCR (vista previa, pago por uso) cubre endpoints Windows, SharePoint y Teams, pero no Exchange, OneDrive ni los clips forenses ([Get started](https://learn.microsoft.com/en-us/purview/insider-risk-management-configure)).

**¿Tienes poco tiempo?**

- [Learn about Insider Risk Management forensic evidence](https://learn.microsoft.com/en-us/purview/insider-risk-management-forensic-evidence) · Documentación
- [Get started with Insider Risk Management forensic evidence](https://learn.microsoft.com/en-us/purview/insider-risk-management-forensic-evidence-configure) · Documentación
- [Use reports in Insider Risk Management](https://learn.microsoft.com/en-us/purview/insider-risk-management-reports) · Documentación
- [Create an investigation in Data Security Investigations](https://learn.microsoft.com/en-us/purview/data-security-investigations-investigation) · Documentación

### Documentación, cursos y credenciales

- [Learn about Insider Risk Management forensic evidence](https://learn.microsoft.com/en-us/purview/insider-risk-management-forensic-evidence) · Documentación · Oficial · Nuevo · Microsoft Learn · 3 nov 2026. Explica la captura visual opt-in de evidencia forense (clips de actividad) con disparadores, exclusiones de apps/sitios, doble aprobación y RBAC.
- [Manage Insider Risk Management forensic evidence](https://learn.microsoft.com/en-us/purview/insider-risk-management-forensic-evidence-manage) · Documentación · Oficial · Microsoft Learn. Gestión de evidencia forense: solicitudes y aprobaciones por usuario, plantillas de notificación, revisión de clips, salud de dispositivos y capacidad/facturación.
- [Get started with Insider Risk Management forensic evidence](https://learn.microsoft.com/en-us/purview/insider-risk-management-forensic-evidence-configure) · Documentación · Oficial · Microsoft Learn. Pasos para habilitar evidencia forense: suscripción, dominios permitidos, instalación del cliente Microsoft Purview en dispositivos y políticas.
- [Create an investigation in Data Security Investigations](https://learn.microsoft.com/en-us/purview/data-security-investigations-investigation) · Documentación · Oficial · Microsoft Learn. Cómo crear investigaciones de Data Security Investigations, incluida la creación directa desde un caso de IRM con contexto en lenguaje natural para el análisis con IA.
- [Learn about the Data Security Investigations workflow](https://learn.microsoft.com/en-us/purview/data-security-investigations-workflow) · Documentación · Oficial · Microsoft Learn. Flujo de DSI para identificar, escalar (desde Defender XDR, IRM o DSPM), buscar, analizar con IA y mitigar incidentes de datos.

**Manos a la obra**

1. `Laboratorio` Genera un informe de actividad de usuario de 90 días para una cuenta de prueba de I2 y compara su contenido con el explorador de actividad ([informes](https://learn.microsoft.com/en-us/purview/insider-risk-management-reports)). Evidencia: hora de solicitud, hora de disponibilidad (hasta 10 horas) y principales actividades.
2. `Laboratorio` Flujo de aprobación forense: con la cuenta de IRM Admins solicita la captura de un usuario de prueba y apruébala con la de IRM Approvers; configura la plantilla de notificación al usuario aprobado y revisa la expiración de solicitudes no atendidas (6 meses) ([gestionar la evidencia forense](https://learn.microsoft.com/en-us/purview/insider-risk-management-forensic-evidence-manage)). Evidencia: solicitud, aprobación y notificación.
3. `Laboratorio parcial` Captura forense con voluntarios: usa una VM con 16 GB de RAM y 8 vCPU (costosa en créditos), instala el cliente de Microsoft Purview (x64), habilita la captura «Specific activities» con la capacidad de prueba de 20 GB, genera la actividad que dispara la captura y revisa el clip ([configurar la evidencia forense](https://learn.microsoft.com/en-us/purview/insider-risk-management-forensic-evidence-configure)). Evidencia: clip revisado y su metadato. Limitación: costo de la VM y requisito de GPU integrada; borra los clips y apaga la VM al terminar.
4. `Laboratorio parcial` Desde el caso de I3, crea una investigación de Data Security Investigations sobre uno o dos buzones de prueba, con contexto en lenguaje natural y una estimación de costos previa ([crear una investigación](https://learn.microsoft.com/en-us/purview/data-security-investigations-investigation)). Evidencia: hallazgos del análisis. Limitación: pago por uso; fija presupuesto con alertas al 50, 75 y 90 % y elimina la investigación al terminar ([facturación de DSI](https://learn.microsoft.com/en-us/purview/data-security-investigations-billing)).
5. `Laboratorio parcial` OCR (vista previa, pago por uso): actívalo y sube una imagen con datos sensibles sintéticos desde el endpoint Windows de prueba; comprueba si la detección aparece en la actividad ([Get started](https://learn.microsoft.com/en-us/purview/insider-risk-management-configure)). Evidencia: evento con el texto detectado. Limitación: no cubre Exchange, OneDrive ni los clips forenses.
6. `Solo producción` Evidencia forense en producción: solo con aprobación previa de Legal y RR. HH., para usuarios concretos con un caso abierto, en ventanas cortas y con aviso a los usuarios según la política interna ([evidencia forense](https://learn.microsoft.com/en-us/purview/insider-risk-management-forensic-evidence)). Cómo hacerlo seguro: captura de actividades específicas (no continua), retención mínima, acceso exclusivo de IRM Investigators y registro de cada aprobación en el expediente.

<a id="m3"></a>

## M3 · Protección adaptativa: DLP, Acceso condicional y ciclo de vida según el riesgo

*L300 · ~5 h · Origen: Nuevo en esta edición; se apoya en el módulo de Protección adaptativa de la ruta SC-401*

La **Protección adaptativa** convierte el riesgo interno en controles dinámicos: IRM asigna a cada usuario un **nivel de riesgo interno** —Elevated, Moderate o Minor, distinto de la severidad de una alerta— y las políticas de DLP, de Data Lifecycle Management (vista previa) y de Acceso condicional (vista previa) se aplican según ese nivel. Así, las restricciones fuertes recaen solo en las pocas personas con riesgo elevado, en vez de bloquear a toda la organización.

Los valores por defecto importan: la detección mira 7 días hacia atrás y el nivel dura 7 días (ambos configurables de 5 a 30), y caduca automáticamente al descartar la alerta o cerrar el caso. La configuración rápida crea una política Data leaks, una política de Acceso condicional en modo solo informe y dos políticas DLP en modo prueba, y tarda hasta 72 horas; la personalizada tarda hasta 36 horas en aplicarse y apagarla, hasta 6. La DLP adaptativa solo actúa en Exchange, Teams y dispositivos, y Data Lifecycle Management preserva durante 120 días lo que borre un usuario con nivel Elevated.

Dos advertencias: los nombres **no** se seudonimizan en Acceso condicional y aparecen reales en las alertas DLP y en el explorador de actividad; y los niveles ya pueden asignarse también a **agentes**. La DLP adaptativa se profundiza en el programa de Purview DLP (módulo M4) y el Acceso condicional, en el programa de Entra (módulo M1).

**Por qué importa**

Es la diferencia entre detectar y prevenir: la Protección adaptativa frena la exfiltración del usuario de riesgo elevado sin fricción para el resto. Se mide con facilidad —intentos bloqueados en usuarios Elevated, tickets de soporte generados, falsos positivos— y suele ser el argumento más convincente para que el CISO financie el programa.

**Qué vas a lograr**

- Explicar la diferencia entre nivel de riesgo interno y severidad de alerta.
- Configurar los niveles, las condiciones y las ventanas de la Protección adaptativa.
- Desplegar la configuración rápida en modo prueba y verificar las políticas que crea.
- Usar la condición de riesgo interno de Acceso condicional en modo solo informe.
- Documentar dónde se pierde la seudonimización al aplicar controles adaptativos.

> **Novedad.** Página actualizada el 26 de junio de 2026: DLP adaptativa en disponibilidad general, Acceso condicional y Data Lifecycle Management en vista previa, y niveles de riesgo asignables también a agentes ([Protección adaptativa](https://learn.microsoft.com/en-us/purview/insider-risk-management-adaptive-protection)). La guía actual separa los niveles de riesgo para usuarios y para agentes, y las sugerencias de directiva no se admiten en la DLP adaptativa ([guía de Protección adaptativa](https://learn.microsoft.com/en-us/purview/insider-risk-management-adaptive-protection-guide)).

> **Atención.** Privacidad: con Protección adaptativa los nombres **no** se seudonimizan en Acceso condicional y aparecen reales en las alertas DLP y en el explorador de actividad ([Protección adaptativa](https://learn.microsoft.com/en-us/purview/insider-risk-management-adaptive-protection)). Inclúyelo en la evaluación de impacto de privacidad y limita quién ve esas alertas.

> **Consejo Ninja.** Planifica los tiempos: la configuración rápida tarda hasta 72 horas, la personalizada hasta 36 horas en aplicarse y apagarla, hasta 6 horas. La configuración rápida crea una política Data leaks, una política de Acceso condicional en solo informe, una de retención (120 días para Elevated) y dos DLP en modo prueba: bloqueo para Elevated y auditoría para Moderate y Minor ([Protección adaptativa](https://learn.microsoft.com/en-us/purview/insider-risk-management-adaptive-protection)).

> **Atención.** La página de Protección adaptativa afirma que IRM no está disponible en las nubes de gobierno de EE. UU., mientras que MC1430536 fija fechas para esas nubes y el conector de RR. HH. existe en GCC ([Protección adaptativa](https://learn.microsoft.com/en-us/purview/insider-risk-management-adaptive-protection) frente a [MC1430536](https://mc.merill.net/message/MC1430536)). El impacto es bajo para MCSA, pero muestra por qué conviene confirmar cada estado en la fuente más reciente.

**¿Tienes poco tiempo?**

- [Help dynamically mitigate risks with Adaptive Protection](https://learn.microsoft.com/en-us/purview/insider-risk-management-adaptive-protection) · Documentación
- [Insider Risk in Conditional Access | Microsoft Entra + Microsoft Purview Adaptive Protection](https://www.youtube.com/watch?v=C9jXvvZqVyI) · Video
- [Data Protection with Microsoft Purview: How it Detects and Responds](https://www.youtube.com/watch?v=Bt0qFtjwTMA) · Video

**Protección adaptativa: parámetros y tiempos (página del 26 de junio de 2026)**

| Parámetro | Valor o comportamiento | Implicación práctica |
|---|---|---|
| Niveles de riesgo interno | Elevated, Moderate y Minor (distintos de la severidad de la alerta) | Diseña un control por nivel; no confundas nivel con severidad |
| Detección de actividad previa | 7 días por defecto (configurable de 5 a 30) | Ventanas cortas reducen falsos positivos; las largas capturan patrones lentos |
| Vigencia del nivel | 7 días por defecto (configurable de 5 a 30) | Define cuánto dura una restricción sin intervención humana |
| Expiración automática | Al descartar la alerta o cerrar el caso (activa por defecto) | Un triage oportuno libera al usuario de controles innecesarios |
| Configuración rápida | Política Data leaks, Acceso condicional en solo informe, retención de 120 días para Elevated y dos DLP en modo prueba (bloqueo para Elevated; auditoría para Moderate y Minor); hasta 72 h | Ideal para el laboratorio; revisa todo antes de pasar a aplicación |
| Configuración personalizada | Hasta 36 h en aplicarse; apagarla tarda hasta 6 h | Planifica ventanas de cambio y de reversión |
| DLP adaptativa | Solo Exchange, Teams y dispositivos; disponibilidad general; sin sugerencias de directiva | No esperes efecto en SharePoint ni en OneDrive por esta vía |
| Acceso condicional | Condición de riesgo interno (vista previa); nombres sin seudonimizar | Diseño en el programa de Entra (M1); evalúa el impacto en la privacidad |
| Data Lifecycle Management | Preserva 120 días lo que borra un usuario Elevated en SharePoint, OneDrive y Exchange (vista previa) | La evidencia sigue disponible aunque el usuario intente borrarla |
| Agentes | Los niveles también se asignan a agentes; la guía separa los niveles de usuarios y de agentes | Coordina con el programa de DSPM (M2) |

Fuentes: [Protección adaptativa](https://learn.microsoft.com/en-us/purview/insider-risk-management-adaptive-protection) · [guía de Protección adaptativa](https://learn.microsoft.com/en-us/purview/insider-risk-management-adaptive-protection-guide).

### Documentación, cursos y credenciales

- [Help dynamically mitigate risks with Adaptive Protection](https://learn.microsoft.com/en-us/purview/insider-risk-management-adaptive-protection) · Documentación · Oficial · Nuevo · Microsoft Learn · 26 jun 2026. Documento central de Protección adaptativa: niveles de riesgo interno (Elevated, Moderate, Minor) que aplican dinámicamente políticas de DLP, Acceso condicional y gestión del ciclo de vida de datos.

### Webinars, videos y podcasts

- [Insider Risk in Conditional Access | Microsoft Entra + Microsoft Purview Adaptive Protection](https://www.youtube.com/watch?v=C9jXvvZqVyI) · Video · Empleado de Microsoft · Erin Miyake · Microsoft Mechanics. Demostración de cómo Protección adaptativa lleva el nivel de riesgo interno a Acceso condicional de Entra para bloquear acceso a activos críticos.
- [Data Protection with Microsoft Purview: How it Detects and Responds](https://www.youtube.com/watch?v=Bt0qFtjwTMA) · Video · Oficial · Legado aún útil · Microsoft Mechanics. Caso inspirado en espionaje corporativo real que muestra cómo clasificación, DLP adaptativa según nivel de riesgo interno e IRM se combinan para detectar y prevenir fugas. *Nota:* Video de ~2023; interfaz anterior, concepto de Protección adaptativa vigente

**Manos a la obra**

1. `Laboratorio` Ejecuta la configuración rápida de Protección adaptativa y, cuando termine (hasta 72 horas), revisa la política Data leaks, la política de Acceso condicional en solo informe y las dos políticas DLP en modo prueba ([Protección adaptativa](https://learn.microsoft.com/en-us/purview/insider-risk-management-adaptive-protection)). Evidencia: capturas de cada política creada y de sus condiciones por nivel.
2. `Laboratorio parcial` Lleva a un usuario de prueba al nivel Elevated generando actividad de exfiltración simulada y verifica el resultado de las DLP en modo prueba ([Protección adaptativa](https://learn.microsoft.com/en-us/purview/insider-risk-management-adaptive-protection)). Evidencia: nivel asignado y coincidencias DLP. Limitación: con poco volumen puede no alcanzarse el umbral; registra los intentos y el nivel obtenido.
3. `Laboratorio` Fuerza la expiración del nivel de riesgo de ese usuario y documenta qué datos aparecieron sin seudonimizar mientras estuvo vigente: alertas DLP, explorador de actividad y Acceso condicional ([Protección adaptativa](https://learn.microsoft.com/en-us/purview/insider-risk-management-adaptive-protection)). Evidencia: nota de privacidad para la evaluación de impacto.
4. `Laboratorio` Revisa la política de Acceso condicional con la condición de riesgo interno en modo solo informe y consulta en los registros de inicio de sesión qué habría hecho con el usuario Elevated; el video [Insider Risk in Conditional Access](https://www.youtube.com/watch?v=C9jXvvZqVyI) muestra el flujo completo. Evidencia: entrada del registro con el resultado del modo solo informe. El diseño de Acceso condicional se profundiza en el programa de Entra (M1).
5. `Laboratorio parcial` Data Lifecycle Management (vista previa): verifica la política de retención creada automáticamente y borra un archivo de prueba con el usuario Elevated; comprueba que queda preservado ([Protección adaptativa](https://learn.microsoft.com/en-us/purview/insider-risk-management-adaptive-protection)). Evidencia: elemento preservado. Limitación: vista previa y tiempos de aplicación de hasta 36 horas.
6. `Solo producción` Pasar la DLP adaptativa de modo prueba a aplicación requiere una línea base real de falsos positivos. Cómo hacerlo seguro: grupo piloto aprobado, dos semanas en modo prueba, revisión de coincidencias con el negocio, control de cambios con reversión documentada (apagarla tarda hasta 6 horas) y aviso previo a la mesa de ayuda ([Protección adaptativa](https://learn.microsoft.com/en-us/purview/insider-risk-management-adaptive-protection)).

<a id="m4"></a>

## M4 · Colaboración con RR. HH., Legal, privacidad y eDiscovery

*L300 · ~4 h · Origen: Ninja oficial de IRM (casos), ampliado con avisos, Teams por caso, notas y escalamiento a eDiscovery*

IRM detecta e investiga, pero las decisiones sobre personas las toman RR. HH. y Legal con evidencia completa. La guía de planificación de Microsoft pide incluir desde el principio a TI, Cumplimiento, Privacidad, Seguridad, RR. HH. y Legal y, cuando la normativa local lo exija, usar políticas idénticas separadas por región e investigadores que hablen el idioma de los usuarios. En la práctica, la colaboración tiene tres momentos: el acuerdo de datos (el conector de RR. HH.), el traspaso del caso y el cierre.

Las herramientas de colaboración son varias. Las **plantillas de aviso** envían por correo, solo al usuario del caso, recordatorios de política o de capacitación, en texto o HTML, y dejan rastro auditable; su redacción conviene validarla con RR. HH. y Legal. La **colaboración en Teams** (vista previa) crea un equipo privado por caso con los grupos IRM, Analysts e Investigators y lo archiva —oculto y de solo lectura— al resolver el caso. Las **notas** en alertas y casos documentan el razonamiento de cada decisión.

Cuando el caso necesita preservación o revisión legal, se **escala a eDiscovery (Premium)**: la retención legal, la revisión y la exportación con cadena de custodia se profundizan en el programa de eDiscovery y Audit (módulos M1 y M4). Si la señal viene de mensajes, la integración con Communication Compliance se explica en su propio programa (módulo M4).

**Por qué importa**

Los programas de riesgo interno fracasan más por procesos que por tecnología: traspasos informales, avisos redactados por el analista o expedientes incompletos generan reclamos laborales y legales. Un acuerdo explícito de quién decide qué, con evidencia y tiempos, protege a la organización y a los empleados.

**Qué vas a lograr**

- Definir una matriz RACI del traspaso de casos entre Seguridad, RR. HH., Legal y privacidad.
- Crear plantillas de aviso validadas y enviarlas desde un caso.
- Habilitar la colaboración en Teams por caso y verificar su archivo al cierre.
- Escalar un caso a eDiscovery (Premium) y explicar qué ocurre después.
- Acotar casos y analistas por región con unidades administrativas cuando la normativa lo requiera.

> **Consejo Ninja.** La guía de planificación pide incluir a TI, Cumplimiento, Privacidad, Seguridad, RR. HH. y Legal y, cuando la normativa local lo exija, usar políticas idénticas separadas por región e investigadores que hablen el idioma de los usuarios ([planificar IRM](https://learn.microsoft.com/es-es/purview/insider-risk-management-plan)). Ese criterio encaja con las diferencias normativas entre los países de MCSA.

> **Atención.** Las plantillas de aviso solo se envían al correo del usuario del caso, y en HTML los enlaces deben usar comillas simples en href ([plantillas de aviso](https://learn.microsoft.com/en-us/purview/insider-risk-management-notices)). La redacción de un aviso puede tener efectos laborales: valídala con RR. HH. y Legal antes de usarla.

> **Novedad.** Colaboración en Teams por caso (vista previa; página del 22 de junio de 2026): crea un equipo privado con los grupos IRM, Analysts e Investigators (hasta 100 usuarios iniciales) y lo archiva —oculto y de solo lectura— al resolver el caso; requiere permiso para crear grupos de Microsoft 365 ([Teams para casos](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-teams)).

> **Consejo Ninja.** Escalar a eDiscovery (Premium) es la puerta a la preservación y la revisión legal ([gestionar casos](https://learn.microsoft.com/en-us/purview/insider-risk-management-cases)). La retención legal y la exportación con cadena de custodia se profundizan en el programa de eDiscovery y Audit (M1 y M4), y la integración con Communication Compliance, en su programa (M4).

**¿Tienes poco tiempo?**

- [Plan for Insider Risk Management](https://learn.microsoft.com/en-us/purview/insider-risk-management-plan) · Documentación
- [Create Insider Risk Management notice templates](https://learn.microsoft.com/en-us/purview/insider-risk-management-notices) · Documentación
- [Enable Microsoft Teams for collaborating on Insider Risk Management cases](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-teams) · Documentación
- [Take action on Insider Risk Management cases](https://learn.microsoft.com/en-us/purview/insider-risk-management-cases) · Documentación

### Documentación, cursos y credenciales

- [Enable Microsoft Teams for collaborating on Insider Risk Management cases](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-teams) · Documentación · Oficial · Vista previa · Nuevo · Microsoft Learn · 22 jun 2026. Cómo habilitar Teams (preview) para que cada caso de IRM cree un equipo privado donde analistas, investigadores y partes interesadas (RR. HH., Legal) coordinen y guarden evidencia. *Nota:* Incluye automáticamente a los grupos de roles IRM, Analysts e Investigators (hasta 100 usuarios iniciales); el equipo se archiva (oculto y solo lectura) al resolver el caso; requiere permiso para crear grupos de Microsoft 365
- [MC1430534 - Microsoft Purview: Insider Risk Management - Expanding note capabilities across alerts and cases](https://mc.merill.net/message/MC1430534) · Documentación · Oficial · Nuevo · Microsoft 365 Message Center (archivo mc.merill.net) · 17 jul 2026. Anuncio de notas de investigador y notas automáticas del sistema en alertas y casos, más detalles ampliados del perfil del usuario desde Entra (ocultos si la seudonimización está activa).
- [Create Insider Risk Management notice templates](https://learn.microsoft.com/en-us/purview/insider-risk-management-notices) · Documentación · Oficial · Microsoft Learn. Cómo crear plantillas de aviso por correo (texto o HTML) para recordar políticas o capacitación al usuario de un caso y dejar rastro auditable.

**Manos a la obra**

1. `Laboratorio` Crea una plantilla de aviso en HTML (recordatorio de la política de uso aceptable) y envíala desde un caso a un usuario de prueba ([plantillas de aviso](https://learn.microsoft.com/en-us/purview/insider-risk-management-notices)). Evidencia: correo recibido y entrada en el historial del caso.
2. `Laboratorio` Habilita la colaboración en Teams (vista previa), crea un caso y verifica la membresía del equipo privado; resuelve el caso y comprueba que el equipo queda archivado ([Teams para casos](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-teams)). Evidencia: capturas antes y después de resolver.
3. `Laboratorio` Escala un caso de prueba a eDiscovery (Premium) y verifica en eDiscovery el caso creado y sus custodios ([gestionar casos](https://learn.microsoft.com/en-us/purview/insider-risk-management-cases); [IRM en español](https://learn.microsoft.com/es-es/purview/insider-risk-management)). Evidencia: identificador del caso de eDiscovery y nota en el caso de IRM.
4. `Laboratorio` Acota por región con unidades administrativas: crea una unidad con los usuarios de prueba de un país, asigna un analista con ese alcance y verifica que solo ve los casos de su región ([permisos](https://learn.microsoft.com/en-us/purview/insider-risk-management-permissions)). Evidencia: captura con el alcance aplicado.
5. `Laboratorio` Arma la matriz RACI del traspaso de un caso entre Seguridad, RR. HH., Legal y privacidad, con tiempos objetivo y la evidencia a entregar en cada paso, apoyándote en la tabla [Gobierno, privacidad y proceso de casos](00_Programa.md#gobierno-casos). Evidencia: RACI aprobada por el líder del programa.
6. `Solo producción` Ejercicio de mesa con RR. HH., Legal, privacidad y, si corresponde, la representación de los trabajadores, sobre un caso ficticio de salida de un empleado ([planificar IRM](https://learn.microsoft.com/es-es/purview/insider-risk-management-plan)). Cómo hacerlo seguro: datos inventados, ningún usuario real en el alcance, acta con los acuerdos de traspaso y tiempos, y revisión de la plantilla de aviso por Legal.

<a id="reto-intermedio"></a>

## Reto del nivel

**De la alerta a la respuesta proporcional.** Combina una política Data leaks con una DLP de severidad alta como disparador y la configuración rápida de Protección adaptativa en modo prueba. Lleva a un usuario de prueba a Elevated, muestra el resultado del Acceso condicional en solo informe y de las DLP en modo prueba, abre el caso, envía un aviso validado (en un ejercicio de mesa) por RR. HH. y Legal y escala a eDiscovery (Premium). Opcional: evidencia forense con doble aprobación en una VM de voluntarios. Entrega el expediente del caso con la cadena de decisiones, la RACI usada y una nota de privacidad que liste dónde aparecieron nombres sin seudonimizar.

<a id="quiz-intermedio"></a>

## Evaluación del nivel

Responde y compara con [Evaluaciones y respuestas](06_Evaluaciones_y_respuestas.md#eval-intermedio). Con 80 % o más, ¡nivel aprobado! (En la versión web puedes corregir en línea y generar tu certificado).

1. En Data theft by departing users, ¿qué puede reemplazar al conector de RR. HH. como disparador, según la página de plantillas?
   - a) Una alerta DLP de severidad alta
   - b) El borrado de la cuenta del usuario en Microsoft Entra
   - c) Una alerta de Defender for Endpoint
   - d) Un mensaje detectado por Communication Compliance

2. ¿Qué alertas DLP **no** se evalúan cuando una política DLP actúa como disparador de Data leaks?
   - a) Las de Exchange Online y SharePoint Online de severidad alta
   - b) Las de OneDrive de severidad alta escritas en la auditoría
   - c) Las de SharePoint Online y OneDrive de severidad alta
   - d) Las de Endpoint DLP, Teams y Microsoft 365 Copilot

3. ¿Cuántas políticas DLP puedes asignar como disparador de una política Data leaks?
   - a) Hasta 5
   - b) Hasta 10
   - c) Hasta 20
   - d) Hasta 100

4. ¿Qué plantillas permiten personalizar los eventos desencadenantes?
   - a) Data leaks y Data leaks by priority users
   - b) Todas las plantillas
   - c) Solo Data theft by departing users
   - d) Solo Risky AI usage

5. ¿Qué necesitas para usar las plantillas Security policy violations?
   - a) El conector de acceso físico y un grupo de activos físicos prioritarios configurado
   - b) Defender for Endpoint activo y su integración con IRM habilitada en las funciones avanzadas
   - c) Microsoft 365 E7 y la política Risky Agents activa por defecto en el tenant
   - d) El complemento de evidencia forense y el cliente de Purview en cada dispositivo

6. Sobre la evidencia forense, ¿qué afirmación es correcta?
   - a) Viene activada por defecto para todos los usuarios con licencia de IRM
   - b) Los clips se conservan mientras el caso siga abierto, sin límite de tiempo
   - c) Antes de capturar a un usuario se requiere la aprobación del grupo IRM Approvers
   - d) Funciona en macOS y en Windows siempre que el equipo esté incorporado

7. ¿Qué equipo cumple los requisitos de la evidencia forense?
   - a) Windows 11 Enterprise de 64 bits con GPU integrada y el cliente de Microsoft Purview
   - b) Windows 11 Pro de 64 bits con GPU discreta y la extensión de Purview para Edge
   - c) macOS en una de sus tres últimas versiones con la extensión de Purview para Chrome
   - d) Cualquier VM Windows con 4 GB de RAM, 2 vCPU y el dispositivo incorporado

8. ¿Qué es cierto sobre el informe de actividad de usuario?
   - a) Cubre hasta 7 días y se genera para todos los usuarios de una política
   - b) Está disponible para cualquier administrador global sin roles de IRM
   - c) Se genera en tiempo real a partir de la cola unificada de alertas
   - d) Requiere el grupo IRM Investigators y cubre hasta 90 días por usuario

9. Por defecto, ¿cuánto dura un nivel de riesgo interno de Protección adaptativa antes de restablecerse?
   - a) 24 horas, renovables por el analista
   - b) 7 días, configurable de 5 a 30
   - c) 30 días fijos, sin opción de cambio
   - d) 120 días, igual que la retención de clips

10. ¿Qué hace la integración de Protección adaptativa con Data Lifecycle Management?
   - a) Bloquea el acceso a aplicaciones en la nube a los usuarios con nivel Elevated
   - b) Aplica etiquetas de confidencialidad al contenido que crea un usuario Elevated
   - c) Activa la evidencia forense para los usuarios que alcanzan el nivel Elevated
   - d) Preserva durante 120 días el contenido que borra un usuario con nivel Elevated

11. ¿Dónde aparecen nombres reales (sin seudonimizar) al usar Protección adaptativa?
   - a) En Acceso condicional, en las alertas DLP y en el explorador de actividad
   - b) En ninguna parte: la seudonimización se conserva en todos los productos
   - c) Solo en los informes de analíticas, que se exportan con identidades
   - d) Solo en el panel de políticas de IRM, visible para los administradores

12. ¿En qué ubicaciones actúa la DLP adaptativa?
   - a) SharePoint y OneDrive
   - b) Todas las ubicaciones de DLP
   - c) Exchange, Teams y dispositivos
   - d) Solo Power BI

13. ¿Qué ocurre con el equipo de Teams de un caso de IRM (vista previa) cuando se resuelve el caso?
   - a) Se elimina con su contenido
   - b) Se archiva: queda oculto y de solo lectura
   - c) Se convierte en un equipo público
   - d) Se transfiere a RR. HH.

14. ¿A quién se envían las plantillas de aviso de IRM?
   - a) A todo el departamento del usuario
   - b) Al gerente del usuario
   - c) Al equipo de RR. HH.
   - d) Solo al correo del usuario del caso

15. Cuando un caso de IRM necesita preservación y revisión legal, ¿a qué se escala?
   - a) A eDiscovery (Premium)
   - b) A Communication Compliance
   - c) A Compliance Manager
   - d) A Defender for Cloud Apps

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. No constituye asesoría legal ni laboral: usar Insider Risk Management sobre personas reales exige la evaluación previa de tus áreas de Legal, RR. HH. y privacidad y, cuando corresponda, de la representación de los trabajadores. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

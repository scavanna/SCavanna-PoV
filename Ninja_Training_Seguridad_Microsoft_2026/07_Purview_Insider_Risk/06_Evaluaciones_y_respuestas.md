# Evaluaciones y respuestas

*Microsoft Purview Insider Risk Management Ninja Training · Edición 2026*

[← Comunidad](05_Comunidad.md) · [Índice del programa](README.md) · [Laboratorio y práctica en producción →](07_Laboratorio_y_practica_en_produccion.md)

<a id="respuestas"></a>

Cada evaluación tiene preguntas de opción múltiple. Con 80 % o más el nivel se considera aprobado. Es una autoevaluación de esta guía, no una certificación de Microsoft.

<a id="eval-inicial"></a>

## Nivel 1 · Inicial · Fundamentos con privacidad por diseño

**1. ¿Cuál de estas combinaciones **no** otorga derechos de uso de Insider Risk Management?**

- a) Microsoft 365 E5
- b) Microsoft 365 E3 con Microsoft Purview Suite (antes E5 Compliance)
- c) Microsoft 365 E3 con el complemento Microsoft 365 E5 Insider Risk Management
- d) Microsoft 365 E3 con Microsoft Defender Suite (antes E5 Security)  ✅

*Respuesta: d).* Defender Suite incluye Defender for Endpoint P2, Defender for Office 365 P2, Defender for Identity, Defender for Cloud Apps y Entra ID P2, pero no IRM; IRM viene en E5, en Purview Suite o en el complemento de IRM. [Fuente](https://www.hbs.net/blog/microsoft-365-security-smbs) · Repasa [I1](01_Nivel_1_Inicial.md#i1)

**2. ¿Qué cambió el 1 de octubre de 2025 con Microsoft 365 E5 Compliance?**

- a) Pasó a llamarse Microsoft Purview Suite, sin cambios de servicio, funcionalidad ni precio  ✅
- b) Se fusionó con Microsoft Defender Suite en un único SKU de seguridad y cumplimiento
- c) Pasó a incluir Microsoft 365 Copilot y subió de precio para los clientes nuevos
- d) Dejó de requerir Microsoft 365 E3 como base y se vende como plan independiente

*Respuesta: a).* Es un cambio de nombre: Purview Suite mantiene el servicio y el precio (USD 12 por usuario al mes con pago anual) y sigue requiriendo Microsoft 365 E3 u Office 365 E3 más EMS E3. [Fuente](https://www.microsoft.com/en-us/security/pricing-overview) · Repasa [I1](01_Nivel_1_Inicial.md#i1)

**3. Vas a practicar con una prueba de Microsoft 365 E5 en un tenant nuevo no administrado. ¿Qué debes verificar antes de crear políticas de IRM?**

- a) Que haya SCU de Security Copilot aprovisionadas, porque IRM las usa para puntuar el riesgo
- b) Que el registro de auditoría unificado esté activo, porque en esos tenants puede venir apagado  ✅
- c) Que la solución de IRM de Sentinel esté instalada, porque IRM guarda allí sus alertas
- d) Que la seudonimización esté desactivada, porque impide que las políticas generen alertas

*Respuesta: b).* IRM usa el registro de auditoría para sus políticas y analíticas; en tenants no administrados con pruebas gratuitas puede no venir activado, y activarlo tarda hasta 60 minutos. [Fuente](https://learn.microsoft.com/en-us/purview/audit-log-enable-disable) · Repasa [P0](01_Nivel_1_Inicial.md#p0)

**4. Desde julio de 2026, ¿qué admiten las asignaciones a grupos de roles de Purview?**

- a) Aprobación obligatoria de dos administradores para cualquier grupo de roles de Purview
- b) Asignación exclusiva mediante unidades administrativas, sin asignaciones a todo el tenant
- c) Fecha de vencimiento de 1 día a 2 años, salvo eDiscovery Administrator y eDiscovery Manager  ✅
- d) Herencia automática desde los roles de Entra ID, sin necesidad de una asignación explícita

*Respuesta: c).* La novedad de julio de 2026 permite dar acceso temporal, por ejemplo a investigadores, con vencimiento de 1 día a 2 años. [Fuente](https://learn.microsoft.com/en-us/purview/whats-new) · Repasa [P0](01_Nivel_1_Inicial.md#p0)

**5. ¿Qué examen cubre hoy Insider Risk Management dentro de su dominio «Manage risks, alerts, and activities»?**

- a) SC-400
- b) SC-200
- c) MS-102
- d) SC-401  ✅

*Respuesta: d).* SC-401 reemplazó a SC-400 (retirado el 31 de mayo de 2025); su guía de estudio se actualizó el 28 de octubre de 2026 y ese dominio pesa entre 30 y 35 %. [Fuente](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-401) · Repasa [I0](01_Nivel_1_Inicial.md#i0)

**6. Según Microsoft, ¿quién es responsable de que el uso de IRM cumpla la ley aplicable?**

- a) Microsoft, porque la herramienta seudonimiza a los usuarios por defecto
- b) El cliente, que además debe hacer su propia investigación sin basarse solo en IRM  ✅
- c) El revendedor que vendió la licencia y configuró el tenant inicial
- d) La autoridad de protección de datos del país donde está hospedado el tenant

*Respuesta: b).* La guía de inicio aclara que el cliente es el único responsable y que no debe basarse solo en las conclusiones de IRM; por eso se involucra a Legal, RR. HH. y privacidad. [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-configure) · Repasa [I1](01_Nivel_1_Inicial.md#i1)

**7. ¿En qué estado vienen los indicadores globales de IRM al empezar?**

- a) Todos desactivados; hay que activar al menos uno para crear una política  ✅
- b) Todos activados, incluidos los de pago por uso, hasta que alguien los apague
- c) Solo los de dispositivo activados; los de Office se activan al crear una política
- d) Activados según la plantilla elegida, sin posibilidad de cambiarlos globalmente

*Respuesta: a).* Es parte de la privacidad por diseño: nada se recolecta hasta que alguien decide activar indicadores. [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-policy-indicators) · Repasa [I2](01_Nivel_1_Inicial.md#i2)

**8. ¿Cuál de estos indicadores requiere activar el pago por uso?**

- a) Indicadores de Office, como descargas y uso compartido en SharePoint
- b) Interacciones de los usuarios con Microsoft 365 Copilot en sus aplicaciones
- c) Almacenamiento en la nube de terceros, como Box, Dropbox o Google Drive  ✅
- d) Booster de riesgo por pertenencia a un grupo de usuarios prioritarios

*Respuesta: c).* Los indicadores de nube, red de terceros, Fabric y varias experiencias de IA son de pago por uso; Microsoft 365 Copilot no genera cargo de pago por uso. [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-policy-indicators) · Repasa [I2](01_Nivel_1_Inicial.md#i2)

**9. ¿Cuál es un límite real del conector de RR. HH.?**

- a) Solo acepta renuncias; los cambios de nivel y las evaluaciones requieren otro conector
- b) Requiere el rol Global Administrator en cada carga, además de la app registrada en Entra
- c) Admite hasta 5.000 registros por archivo, cargados solo de forma manual desde el portal
- d) Hasta 500 registros por CSV en cada carga; los perfiles sin actualizar se borran a los 30 días  ✅

*Respuesta: d).* La guía (30 de marzo de 2026) fija 500 registros por CSV, la ventana de LastWorkingDate, el rol Data Connector Admin y el borrado de los perfiles sin actualizar a los 30 días. [Fuente](https://learn.microsoft.com/en-us/purview/import-hr-data) · Repasa [I2](01_Nivel_1_Inicial.md#i2)

**10. ¿Qué acepta el conector Insider Risk Indicators (vista previa)?**

- a) Señales crudas de cualquier SIEM, que IRM agrega y normaliza por su cuenta
- b) Detecciones de terceros ya agregadas y procesadas, por ejemplo desde Sentinel o Splunk  ✅
- c) Solo datos de RR. HH. en CSV, como alternativa al conector de RR. HH.
- d) Registros de historias clínicas exportados desde un sistema de salud

*Respuesta: b).* Importa detecciones agregadas para usarlas como disparadores o indicadores personalizados; no acepta señales crudas. [Fuente](https://learn.microsoft.com/en-us/purview/import-insider-risk-indicators) · Repasa [I2](01_Nivel_1_Inicial.md#i2)

**11. Según MC1430536, ¿qué se retira con la experiencia unificada de alertas?**

- a) La seudonimización de los nombres en la cola de alertas
- b) Los casos, que pasan a gestionarse dentro de la cola
- c) La pestaña «Alerts (classic)» y Alert Spotlight  ✅
- d) El Triage Agent, que se reemplaza por reglas de prioridad

*Respuesta: c).* «Alerts (classic)» se deprecó el 1 de octubre de 2026 en la nube comercial (el 31 de octubre en gobierno) y se retiró Alert Spotlight; la privacidad no cambia. [Fuente](https://mc.merill.net/message/MC1430536) · Repasa [I3](01_Nivel_1_Inicial.md#i3)

**12. ¿Cuánto tardan, aproximadamente, las primeras alertas después de crear una política?**

- a) Unas 24 horas  ✅
- b) Aparecen de inmediato
- c) 7 días
- d) 30 días

*Respuesta: a).* La guía de inicio indica que las alertas comienzan unas 24 horas después de crear la política; las analíticas tardan hasta 48 horas. [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-configure) · Repasa [I3](01_Nivel_1_Inicial.md#i3)

**13. ¿Qué ocurre con el perfil de usuario ampliado (datos de Entra) cuando la seudonimización está activa?**

- a) Muestra todos los datos de Entra
- b) Se envía automáticamente a RR. HH.
- c) Muestra solo el departamento
- d) Queda oculto  ✅

*Respuesta: d).* MC1430534 indica que los detalles ampliados del perfil se ocultan si la seudonimización está activa. [Fuente](https://mc.merill.net/message/MC1430534) · Repasa [I3](01_Nivel_1_Inicial.md#i3)

<a id="eval-intermedio"></a>

## Nivel 2 · Intermedio · Políticas, investigación y respuesta proporcional

**1. En Data theft by departing users, ¿qué puede reemplazar al conector de RR. HH. como disparador, según la página de plantillas?**

- a) Una alerta DLP de severidad alta
- b) El borrado de la cuenta del usuario en Microsoft Entra  ✅
- c) Una alerta de Defender for Endpoint
- d) Un mensaje detectado por Communication Compliance

*Respuesta: b).* La plantilla permite elegir el borrado de la cuenta en Entra. Ojo: «Get started» lista el conector como requerido, una contradicción documentada en Limitaciones. [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-policy-templates) · Repasa [M1](02_Nivel_2_Intermedio.md#m1)

**2. ¿Qué alertas DLP **no** se evalúan cuando una política DLP actúa como disparador de Data leaks?**

- a) Las de Exchange Online y SharePoint Online de severidad alta
- b) Las de OneDrive de severidad alta escritas en la auditoría
- c) Las de SharePoint Online y OneDrive de severidad alta
- d) Las de Endpoint DLP, Teams y Microsoft 365 Copilot  ✅

*Respuesta: d).* Solo cuentan las alertas de severidad alta de Exchange Online, SharePoint Online y OneDrive. [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-policy-indicators) · Repasa [M1](02_Nivel_2_Intermedio.md#m1)

**3. ¿Cuántas políticas DLP puedes asignar como disparador de una política Data leaks?**

- a) Hasta 5
- b) Hasta 10
- c) Hasta 20  ✅
- d) Hasta 100

*Respuesta: c).* Data leaks admite hasta 20 políticas DLP; el límite de 100 corresponde a las políticas por plantilla. [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-policy-templates) · Repasa [M1](02_Nivel_2_Intermedio.md#m1)

**4. ¿Qué plantillas permiten personalizar los eventos desencadenantes?**

- a) Data leaks y Data leaks by priority users  ✅
- b) Todas las plantillas
- c) Solo Data theft by departing users
- d) Solo Risky AI usage

*Respuesta: a).* Solo esas dos plantillas permiten elegir indicadores desencadenantes propios en lugar de la alerta DLP. [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-policy-indicators) · Repasa [M1](02_Nivel_2_Intermedio.md#m1)

**5. ¿Qué necesitas para usar las plantillas Security policy violations?**

- a) El conector de acceso físico y un grupo de activos físicos prioritarios configurado
- b) Defender for Endpoint activo y su integración con IRM habilitada en las funciones avanzadas  ✅
- c) Microsoft 365 E7 y la política Risky Agents activa por defecto en el tenant
- d) El complemento de evidencia forense y el cliente de Purview en cada dispositivo

*Respuesta: b).* Usan alertas de Defender for Endpoint, que se importan a diario según los estados de triage elegidos. [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-policy-templates) · Repasa [M1](02_Nivel_2_Intermedio.md#m1)

**6. Sobre la evidencia forense, ¿qué afirmación es correcta?**

- a) Viene activada por defecto para todos los usuarios con licencia de IRM
- b) Los clips se conservan mientras el caso siga abierto, sin límite de tiempo
- c) Antes de capturar a un usuario se requiere la aprobación del grupo IRM Approvers  ✅
- d) Funciona en macOS y en Windows siempre que el equipo esté incorporado

*Respuesta: c).* Está desactivada por defecto, usa doble autorización, borra los clips a los 120 días y solo admite Windows 10/11 Enterprise de 64 bits. [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-forensic-evidence) · Repasa [M2](02_Nivel_2_Intermedio.md#m2)

**7. ¿Qué equipo cumple los requisitos de la evidencia forense?**

- a) Windows 11 Enterprise de 64 bits con GPU integrada y el cliente de Microsoft Purview  ✅
- b) Windows 11 Pro de 64 bits con GPU discreta y la extensión de Purview para Edge
- c) macOS en una de sus tres últimas versiones con la extensión de Purview para Chrome
- d) Cualquier VM Windows con 4 GB de RAM, 2 vCPU y el dispositivo incorporado

*Respuesta: a).* Requiere Windows 10/11 Enterprise de 64 bits (incluido Windows 365) con GPU integrada, el cliente de Purview y, en VM, 16 GB de RAM y 8 vCPU. [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-forensic-evidence) · Repasa [M2](02_Nivel_2_Intermedio.md#m2)

**8. ¿Qué es cierto sobre el informe de actividad de usuario?**

- a) Cubre hasta 7 días y se genera para todos los usuarios de una política
- b) Está disponible para cualquier administrador global sin roles de IRM
- c) Se genera en tiempo real a partir de la cola unificada de alertas
- d) Requiere el grupo IRM Investigators y cubre hasta 90 días por usuario  ✅

*Respuesta: d).* Los datos llegan unas 48 horas después y el informe tarda hasta 10 horas en generarse. [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-reports) · Repasa [M2](02_Nivel_2_Intermedio.md#m2)

**9. Por defecto, ¿cuánto dura un nivel de riesgo interno de Protección adaptativa antes de restablecerse?**

- a) 24 horas, renovables por el analista
- b) 7 días, configurable de 5 a 30  ✅
- c) 30 días fijos, sin opción de cambio
- d) 120 días, igual que la retención de clips

*Respuesta: b).* Tanto la vigencia del nivel como la detección de actividad previa valen 7 días por defecto. [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-adaptive-protection) · Repasa [M3](02_Nivel_2_Intermedio.md#m3)

**10. ¿Qué hace la integración de Protección adaptativa con Data Lifecycle Management?**

- a) Bloquea el acceso a aplicaciones en la nube a los usuarios con nivel Elevated
- b) Aplica etiquetas de confidencialidad al contenido que crea un usuario Elevated
- c) Activa la evidencia forense para los usuarios que alcanzan el nivel Elevated
- d) Preserva durante 120 días el contenido que borra un usuario con nivel Elevated  ✅

*Respuesta: d).* Una política de retención creada automáticamente preserva lo borrado en SharePoint, OneDrive y Exchange (vista previa). [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-adaptive-protection) · Repasa [M3](02_Nivel_2_Intermedio.md#m3)

**11. ¿Dónde aparecen nombres reales (sin seudonimizar) al usar Protección adaptativa?**

- a) En Acceso condicional, en las alertas DLP y en el explorador de actividad  ✅
- b) En ninguna parte: la seudonimización se conserva en todos los productos
- c) Solo en los informes de analíticas, que se exportan con identidades
- d) Solo en el panel de políticas de IRM, visible para los administradores

*Respuesta: a).* La seudonimización de IRM no se conserva en esos lugares; inclúyelo en la evaluación de impacto de privacidad. [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-adaptive-protection) · Repasa [M3](02_Nivel_2_Intermedio.md#m3)

**12. ¿En qué ubicaciones actúa la DLP adaptativa?**

- a) SharePoint y OneDrive
- b) Todas las ubicaciones de DLP
- c) Exchange, Teams y dispositivos  ✅
- d) Solo Power BI

*Respuesta: c).* Aunque la política DLP tenga otras ubicaciones, la Protección adaptativa solo actúa en esas tres. [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-adaptive-protection) · Repasa [M3](02_Nivel_2_Intermedio.md#m3)

**13. ¿Qué ocurre con el equipo de Teams de un caso de IRM (vista previa) cuando se resuelve el caso?**

- a) Se elimina con su contenido
- b) Se archiva: queda oculto y de solo lectura  ✅
- c) Se convierte en un equipo público
- d) Se transfiere a RR. HH.

*Respuesta: b).* El equipo privado del caso se archiva al resolverlo, lo que preserva la colaboración sin dejarla activa. [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-teams) · Repasa [M4](02_Nivel_2_Intermedio.md#m4)

**14. ¿A quién se envían las plantillas de aviso de IRM?**

- a) A todo el departamento del usuario
- b) Al gerente del usuario
- c) Al equipo de RR. HH.
- d) Solo al correo del usuario del caso  ✅

*Respuesta: d).* Los avisos se envían únicamente al usuario del caso y quedan en su historial; su redacción conviene validarla con RR. HH. y Legal. [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-notices) · Repasa [M4](02_Nivel_2_Intermedio.md#m4)

**15. Cuando un caso de IRM necesita preservación y revisión legal, ¿a qué se escala?**

- a) A eDiscovery (Premium)  ✅
- b) A Communication Compliance
- c) A Compliance Manager
- d) A Defender for Cloud Apps

*Respuesta: a).* El escalamiento a eDiscovery (Premium) permite retener, revisar y exportar con cadena de custodia. [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-cases) · Repasa [M4](02_Nivel_2_Intermedio.md#m4)

<a id="eval-avanzado"></a>

## Nivel 3 · Avanzado · IA, agentes, SOC y automatización

**1. ¿Qué interacción de IA **no** genera cargos de pago por uso en IRM?**

- a) Enterprise AI apps
- b) Microsoft 365 Copilot  ✅
- c) Other AI apps detectadas por el navegador
- d) Copilot experiences con datos que no son de Microsoft 365

*Respuesta: b).* Las interacciones con Microsoft 365 Copilot no tienen cargo de pago por uso; las otras tres opciones sí. [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-policy-indicators) · Repasa [A1](03_Nivel_3_Avanzado.md#a1)

**2. ¿Qué agentes cubre la política Risky Agents?**

- a) Solo agentes de Copilot Studio publicados en Teams
- b) Cualquier agente de terceros, aunque no tenga conector
- c) Copilot Studio, Microsoft Foundry y agentes creados con el SDK P4AI  ✅
- d) Solo agentes registrados en Agent 365 con identidad propia

*Respuesta: c).* Así lo indica la página de monitoreo de agentes (4 de agosto de 2026); MC1200579 suma los agentes de Agent 365. [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-monitoring-agents) · Repasa [A1](03_Nivel_3_Avanzado.md#a1)

**3. Según MC1280556, ¿qué licencia es necesaria para Insider Risk Management para agentes?**

- a) Microsoft 365 E7 o Agent 365  ✅
- b) Microsoft Purview Suite
- c) Microsoft Defender Suite
- d) Microsoft 365 E3

*Respuesta: a).* El aviso marca la disponibilidad general entre junio y julio de 2026 e indica que no está disponible sin E7 o Agent 365; Learn todavía la marca en vista previa. [Fuente](https://message.cengizyilmaz.net/message/mc1280556-microsoft-purview-for-agents-ai-observability-and-insider-risk-management-now-generally-available) · Repasa [A1](03_Nivel_3_Avanzado.md#a1)

**4. ¿Qué ve el equipo de IRM cuando un usuario invitado interactúa con un agente monitoreado por Risky Agents?**

- a) El prompt completo y la respuesta del agente, como con empleados
- b) Nada: los invitados quedan fuera de toda política de IRM
- c) El historial de navegación del invitado durante la sesión
- d) Solo indicadores de tipos de información sensible, no el contenido  ✅

*Respuesta: d).* Con invitados, la política solo muestra los indicadores de información sensible; además, las unidades administrativas no admiten alertas de agentes. [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-monitoring-agents) · Repasa [A1](03_Nivel_3_Avanzado.md#a1)

**5. ¿Qué ocurre al activar los indicadores de Azure AI Content Safety en IRM?**

- a) Se crea una política de Communication Compliance  ✅
- b) Se desactiva la seudonimización de los prompts
- c) Se crea automáticamente un caso de eDiscovery
- d) Se habilita la evidencia forense del dispositivo

*Respuesta: a).* Esos indicadores se apoyan en una política de Communication Compliance creada para ese fin. [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-policy-indicators) · Repasa [A1](03_Nivel_3_Avanzado.md#a1)

**6. ¿Qué dato de IRM **todavía no** llega a la integración con Defender XDR?**

- a) El estado de la alerta
- b) La severidad
- c) Los eventos de Risky AI usage  ✅
- d) La clasificación de la alerta

*Respuesta: c).* Tampoco llegan la exfiltración por correo, las apps cloud de terceros, los eventos previos a la alerta ni las exclusiones. [Fuente](https://learn.microsoft.com/en-us/defender-xdr/irm-investigate-alerts-defender) · Repasa [A2](03_Nivel_3_Avanzado.md#a2)

**7. ¿Por qué la integración de IRM con Defender XDR puede romper automatizaciones de Sentinel?**

- a) Porque cambia el esquema de todas las tablas
- b) Porque los incidentes de IRM no contienen alertas  ✅
- c) Porque desactiva el conector de Defender XDR
- d) Porque elimina la seudonimización en Sentinel

*Respuesta: b).* Microsoft recomienda usar el conector de IRM para Sentinel o desactivar el uso compartido de datos. [Fuente](https://learn.microsoft.com/en-us/defender-xdr/irm-investigate-alerts-defender) · Repasa [A2](03_Nivel_3_Avanzado.md#a2)

**8. ¿Qué necesita un analista del SOC para ver alertas de IRM en Defender XDR?**

- a) Global Administrator, que ya incluye el acceso a los datos de IRM en Defender
- b) Solo el grupo IRM Auditors, que exporta los registros de IRM a Defender
- c) Security Administrator más IRM Approvers, que aprueba el uso compartido
- d) Security Operator o Security Reader, más pertenecer a IRM, IRM Analysts o IRM Investigators  ✅

*Respuesta: d).* Además debe estar activado el uso compartido de datos en IRM. [Fuente](https://learn.microsoft.com/en-us/defender-xdr/irm-investigate-alerts-defender) · Repasa [A2](03_Nivel_3_Avanzado.md#a2)

**9. ¿Qué ocurre con la seudonimización al exportar alertas por la Office 365 Management Activity API?**

- a) Se conserva siempre
- b) No se conserva; la exportación a CSV sí la conserva  ✅
- c) Se conserva solo en alertas de severidad alta
- d) La API no exporta alertas de IRM

*Respuesta: b).* La exportación por API corre cada 60 minutos, está desactivada por defecto y no conserva la seudonimización. [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-share-data) · Repasa [A4](03_Nivel_3_Avanzado.md#a4)

**10. ¿Qué ocurre con el Triage Agent 90 días después de la última vez que se guardó su configuración?**

- a) Se elimina y hay que desplegar una nueva instancia del agente
- b) Pasa a modo manual y solo clasifica alertas a pedido del analista
- c) Deja de ejecutarse hasta que alguien vuelva a guardar su configuración  ✅
- d) Reinicia la ventana de alertas y vuelve a clasificar todo el historial

*Respuesta: c).* El agente corre con el contexto del último usuario que guardó la configuración, y esa autenticación dura 90 días. [Fuente](https://learn.microsoft.com/en-us/purview/copilot-in-purview-triage-irm-agent-get-started) · Repasa [A3](03_Nivel_3_Avanzado.md#a3)

**11. Según Learn, ¿qué necesita el Triage Agent de IRM además de la licencia por usuario de IRM?**

- a) El modelo de pago por uso y SCU de Security Copilot aprovisionadas  ✅
- b) Solo Microsoft 365 E7, que reemplaza la licencia de IRM
- c) El complemento de evidencia forense con capacidad adicional
- d) Una licencia de Microsoft 365 Copilot para cada analista

*Respuesta: a).* También requiere el tenant incorporado a Security Copilot, el uso compartido de datos de Microsoft 365 y el plugin de Purview habilitado. [Fuente](https://learn.microsoft.com/en-us/purview/copilot-in-purview-triage-irm-agent-get-started) · Repasa [A3](03_Nivel_3_Avanzado.md#a3)

**12. ¿Cuántas SCU aporta la inclusión de Security Copilot en Microsoft 365 E5 y E7?**

- a) 100 SCU fijas al mes por tenant, sin importar las licencias
- b) 1 SCU por usuario licenciado, sin tope mensual
- c) Ninguna: las SCU siempre se compran aparte por hora
- d) 400 SCU al mes por cada 1.000 licencias pagas, hasta 10.000  ✅

*Respuesta: d).* Se calcula sobre licencias pagas y se despliega gradualmente desde el 18 de noviembre de 2025; un tenant de prueba no la garantiza. [Fuente](https://learn.microsoft.com/en-us/copilot/security/security-copilot-inclusion) · Repasa [A3](03_Nivel_3_Avanzado.md#a3)

**13. ¿Qué pasa con las plantillas de Power Automate para IRM si la seudonimización está activa?**

- a) Funcionan igual
- b) No funcionan como se espera  ✅
- c) La seudonimización se desactiva automáticamente
- d) Exigen una licencia premium

*Respuesta: b).* La documentación advierte que, con la seudonimización activa, estas plantillas no funcionan como se espera. [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-power-automate) · Repasa [A4](03_Nivel_3_Avanzado.md#a4)

**14. ¿Dónde se pueden usar los indicadores personalizados del conector Insider Risk Indicators?**

- a) En todas las plantillas, incluidas las de agentes
- b) Solo en Risky AI usage y Risky browser usage
- c) Solo en las plantillas Data theft y Data leaks  ✅
- d) Solo en las variantes de Security policy violations

*Respuesta: c).* Además, tras actualizar un indicador hay que esperar 24 horas antes de cargar datos. [Fuente](https://learn.microsoft.com/en-us/purview/import-insider-risk-indicators) · Repasa [A4](03_Nivel_3_Avanzado.md#a4)

<a id="eval-operacion"></a>

## Nivel 4 · Operación · Modelo operativo, métricas y gobierno

**1. ¿Qué grupo de roles puede ver las capturas de evidencia forense y el explorador de contenido?**

- a) IRM Analysts
- b) IRM Auditors
- c) IRM Investigators  ✅
- d) IRM Admins

*Respuesta: c).* Solo IRM Investigators accede a las capturas forenses y al explorador de contenido; por eso es el rol más sensible. [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-permissions) · Repasa [O1](04_Nivel_4_Operacion.md#o1)

**2. ¿Quién aprueba la captura de evidencia forense de un usuario?**

- a) El grupo IRM Approvers  ✅
- b) El administrador global
- c) El propio usuario
- d) El grupo IRM Analysts

*Respuesta: a).* La evidencia forense usa doble autorización: IRM o IRM Admins solicitan e IRM Approvers aprueba. [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-forensic-evidence) · Repasa [O1](04_Nivel_4_Operacion.md#o1)

**3. ¿Qué notificaciones a administradores ofrece IRM?**

- a) Solo un resumen mensual de alertas, enviado por correo al administrador global del tenant
- b) Avisos por SMS al usuario investigado y a su gerente directo cuando se abre un caso
- c) Ninguna: el equipo debe revisar el portal de Purview cada día para ver alertas nuevas
- d) Primera alerta, resumen diario de alertas altas y resumen semanal de advertencias de políticas  ✅

*Respuesta: d).* Se configuran en los ajustes globales de IRM y evitan depender de que alguien abra el portal. [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings) · Repasa [O1](04_Nivel_4_Operacion.md#o1)

**4. ¿Qué marco agnóstico de la herramienta organiza un programa de riesgo interno en detectar, evaluar y gestionar, con una edición de 2026?**

- a) La Insider Threat Mitigation Guide de CISA  ✅
- b) La guía de estudio de SC-401
- c) La descripción del servicio de Purview
- d) El Ninja oficial de IRM

*Respuesta: a).* La edición 2026 de la guía de CISA incorpora el trabajo híbrido y la IA y propone un equipo multidisciplinario con gobierno y cultura. [Fuente](https://www.cisa.gov/resources-tools/resources/insider-threat-mitigation-guide) · Repasa [O1](04_Nivel_4_Operacion.md#o1)

**5. ¿Cómo calcula el panel de políticas la eficacia de las alertas?**

- a) Alertas activas / alertas totales generadas en los últimos 30 días
- b) Alertas confirmadas / (confirmadas + descartadas) en los últimos 365 días  ✅
- c) Casos cerrados / casos abiertos durante el último trimestre
- d) Alertas de severidad alta / alertas de severidad baja del año

*Respuesta: b).* Se calcula sobre las acciones de los últimos 365 días y sirve para comparar políticas y versiones de una misma política. [Fuente](https://learn.microsoft.com/es-es/purview/insider-risk-management-policies) · Repasa [O2](04_Nivel_4_Operacion.md#o2)

**6. ¿Cómo funcionan las analíticas de IRM?**

- a) Requieren crear al menos tres políticas activas antes de ejecutar el primer escaneo
- b) Muestran en tiempo real los nombres de los usuarios más riesgosos de la organización
- c) Escanean a diario hasta 10 días de actividad y entregan resultados agregados y anonimizados  ✅
- d) Solo funcionan con pago por uso y una suscripción de Azure vinculada al tenant

*Respuesta: c).* Permiten estimar el riesgo sin crear políticas y recomiendan umbrales en tiempo real. [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-analytics) · Repasa [O2](04_Nivel_4_Operacion.md#o2)

**7. ¿Qué riesgo tiene elegir «Fewer alerts» en las detecciones inteligentes?**

- a) Que aumenten los falsos positivos
- b) Que se desactive la seudonimización
- c) Que se borren las alertas existentes
- d) Que se oculten verdaderos positivos  ✅

*Respuesta: d).* «Fewer alerts» puede ocultar verdaderos positivos y «More alerts» sube los falsos positivos: registra y mide cada cambio. [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-intelligent-detections) · Repasa [O2](04_Nivel_4_Operacion.md#o2)

**8. ¿Qué indicador de los informes de IRM mide de forma directa la agilidad del triage?**

- a) Días promedio en «Needs review»  ✅
- b) Número de políticas por plantilla
- c) Capacidad usada de evidencia forense
- d) Cantidad de indicadores activados

*Respuesta: a).* El informe de alertas muestra los días promedio en «Needs review»; el de casos, los días promedio activos. [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-reports) · Repasa [O2](04_Nivel_4_Operacion.md#o2)

**9. ¿En cuál de estos casos se conserva la seudonimización de IRM?**

- a) En las alertas DLP generadas por la Protección adaptativa
- b) En la exportación a CSV  ✅
- c) En la exportación por la Office 365 Management Activity API
- d) En el panel del Triage Agent

*Respuesta: b).* La exportación a CSV conserva la seudonimización; la exportación por API, las alertas DLP y el panel del agente muestran nombres. [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-privacy) · Repasa [O3](04_Nivel_4_Operacion.md#o3)

**10. Según el texto de LeyChile citado en este programa, ¿desde cuándo rige la Ley 21.719 de Chile?**

- a) 1 de enero de 2025
- b) 20 de marzo de 2025
- c) 1 de diciembre de 2026  ✅
- d) 26 de mayo de 2026

*Respuesta: c).* Entra en vigencia el 1 de diciembre de 2026 y crea la Agencia de Protección de Datos Personales. El 20 de marzo de 2025 es la publicación de la nueva LFPDPPP de México y el 26 de mayo de 2026, la aprobación de los Estándares Iberoamericanos. Su aplicación a tu caso la define Legal. [Fuente](https://www.bcn.cl/leychile/navegar?i=1209272&f=2026-12-01) · Repasa [O3](04_Nivel_4_Operacion.md#o3)

**11. Si la normativa local lo exige, ¿qué recomienda la guía de planificación de IRM?**

- a) Desactivar IRM en ese país hasta que la autoridad local apruebe expresamente su uso
- b) Usar una única política global sin segmentación, para tratar a todos los usuarios igual
- c) Reemplazar la seudonimización por cifrado de los nombres de usuario en esa región
- d) Usar políticas idénticas separadas por región e investigadores que hablen el idioma de los usuarios  ✅

*Respuesta: d).* La guía también pide involucrar desde el inicio a TI, Cumplimiento, Privacidad, Seguridad, RR. HH. y Legal. [Fuente](https://learn.microsoft.com/es-es/purview/insider-risk-management-plan) · Repasa [O3](04_Nivel_4_Operacion.md#o3)

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. No constituye asesoría legal ni laboral: usar Insider Risk Management sobre personas reales exige la evaluación previa de tus áreas de Legal, RR. HH. y privacidad y, cuando corresponda, de la representación de los trabajadores. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

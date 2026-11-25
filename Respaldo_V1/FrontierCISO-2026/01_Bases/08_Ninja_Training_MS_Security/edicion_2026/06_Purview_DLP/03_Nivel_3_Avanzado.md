# Nivel 3 · Avanzado · Código, SOC y clasificación a escala

*Microsoft Purview Data Loss Prevention Ninja Training · Edición 2026*

[← Nivel 2 · Intermedio](02_Nivel_2_Intermedio.md) · [Índice del programa](README.md) · [Nivel 4 · Operación →](04_Nivel_4_Operacion.md)

<a id="avanzado"></a>

DLP como código, integración con Defender XDR y Sentinel tras el cambio a behaviors, EDM, huellas digitales y OCR a escala, y Security Copilot con el agente de triage. Terminas con directivas versionadas, una decisión documentada sobre las señales DLP en el SOC y un plan de consumo de SCU.

*L400 · 4 módulos · ~22 horas · 29 recursos*

**Módulos de este nivel:** [A1 DLP como código](#a1) · [A2 SOC: Defender XDR y Sentinel](#a2) · [A3 EDM, huellas y OCR](#a3) · [A4 Security Copilot y agentes](#a4)

<a id="a1"></a>

## A1 · DLP como código y automatización

*L400 · ~6 h · Origen: Nuevo en esta edición*

Cuando un programa DLP crece a decenas de directivas y varios países, el portal deja de ser suficiente: necesitas control de versiones, revisión de cambios y despliegues repetibles. Security & Compliance PowerShell lo permite con **New-DlpCompliancePolicy** y **New-DlpComplianceRule**: todas las ubicaciones (incluida Copilot, con `-Locations` en JSON), planos de aplicación, validación previa y parámetros recientes como `RestrictWebGrounding` o `TriggerPowerAutomateFlow`. Desde abril de 2026 puedes además exportar la configuración de directivas DLP y de etiquetas a un ZIP para soporte, control de cambios y análisis.

La automatización también va hacia afuera. **Power Automate** puede ejecutarse como acción de una regla (Exchange, SharePoint y OneDrive, y Windows 24H2 o posterior) sin licencia adicional de Purview, y la **API processContent** de Microsoft Graph permite que una app de IA evalúe prompts contra tus directivas; su variante de tenant para interacciones de agentes está en beta desde el 23 de octubre de 2026. Las directivas para apps registradas en Entra solo se crean con PowerShell.

**Por qué importa**

Las directivas creadas a mano derivan con el tiempo: nadie recuerda por qué existe una excepción ni quién cambió un umbral. Tratar DLP como código deja historial, revisión por pares y reversión en minutos, reduce errores en despliegues multipaís y permite demostrar ante auditoría qué estaba vigente en cada fecha. También acelera la respuesta: un cambio probado en simulación se promueve sin rehacerlo en el portal.

**Qué vas a lograr**

- Exportar la configuración de DLP y versionarla en un repositorio.
- Crear directivas y reglas con PowerShell en modo de simulación, de forma idempotente.
- Usar Power Automate como acción de una regla DLP.
- Evaluar un prompt de una app propia con la API processContent.
- Definir un control de cambios con revisión por pares y reversión.

> **Novedad.** [New-DlpCompliancePolicy](https://learn.microsoft.com/en-us/powershell/module/exchangepowershell/new-dlpcompliancepolicy?view=exchange-ps) admite todas las ubicaciones, incluida Copilot mediante `-Locations` en JSON, además de `-EnforcementPlanes` y validación previa; [New-DlpComplianceRule](https://learn.microsoft.com/en-us/powershell/module/exchangepowershell/new-dlpcompliancerule?view=exchange-ps) incorpora parámetros como `RestrictWebGrounding` y `TriggerPowerAutomateFlow`, y conviene versionar las reglas y desplegarlas con validación.

> **Qué cambió.** Para la DLP de apps de IA personalizadas, el plano de aplicación «Entra» quedó obsoleto y se reemplazó por «Application» ([muestras de Purview](https://github.com/microsoft/purview-api-samples)). Las directivas para apps registradas en Entra solo se crean con PowerShell y no hay APIs para extraer datos de Purview ([usar las APIs](https://learn.microsoft.com/en-us/purview/developer/use-the-api), [visión general de las APIs](https://learn.microsoft.com/en-us/purview/developer/microsoft-purview-sdk-documentation-overview)).

> **Novedad.** La variante de tenant de processContent, que evalúa interacciones de agentes (incluidas las de agente a herramienta), está en beta desde el 23 de octubre de 2026 y no tiene soporte para producción ([processContent de tenant](https://learn.microsoft.com/en-us/graph/api/tenantdatasecurityandgovernance-processcontent?view=graph-rest-beta)); la versión por usuario está en v1.0 ([processContent](https://learn.microsoft.com/en-us/graph/api/userdatasecurityandgovernance-processcontent?view=graph-rest-1.0)). Sin directivas de recopilación o DLP configuradas, el cálculo de protection scopes devuelve un alcance vacío ([APIs de seguridad y gobierno de datos](https://learn.microsoft.com/en-us/graph/security-datasecurityandgovernance-overview)).

> **Consejo Ninja.** Power Automate como acción de regla funciona en Exchange, SharePoint y OneDrive, y Windows 24H2 o posterior, sin licencia adicional de Purview; los conectores premium requieren un plan de Power Automate y, en SharePoint y OneDrive, solo se dispara con contenido nuevo o modificado ([Power Automate en DLP](https://learn.microsoft.com/en-us/purview/dlp-powerautomate-int-get-started)). El ejemplo idempotente de Microsoft marca las directivas con una etiqueta «managed by» y arranca siempre en simulación ([ejemplo de DLP como código](https://github.com/microsoft/BestPractice_Deploy-Scripts/blob/main/Products/Purview/Examples/DLP-Policy-Example.md)).

**¿Tienes poco tiempo?**

- [New-DlpCompliancePolicy](https://learn.microsoft.com/en-us/powershell/module/exchangepowershell/new-dlpcompliancepolicy?view=exchange-ps) · Documentación
- [New-DlpComplianceRule](https://learn.microsoft.com/en-us/powershell/module/exchangepowershell/new-dlpcompliancerule?view=exchange-ps) · Documentación
- [DLP Policy Creation Example (SMBTool Purview Toolkit)](https://github.com/microsoft/BestPractice_Deploy-Scripts/blob/main/Products/Purview/Examples/DLP-Policy-Example.md) · GitHub
- [microsoft/purview-api-samples](https://github.com/microsoft/purview-api-samples) · GitHub

### Documentación, cursos y credenciales

- [Get started with Power Automate integration in Microsoft Purview DLP](https://learn.microsoft.com/en-us/purview/dlp-powerautomate-int-get-started) · Documentación · Oficial · Nuevo · Microsoft Learn · 26 jun 2026. Permite disparar flujos de Power Automate como acción de regla DLP (p. ej., plantilla "Notificar al gerente") en Exchange, SharePoint/OneDrive y Windows 24H2+.
- [New-DlpCompliancePolicy](https://learn.microsoft.com/en-us/powershell/module/exchangepowershell/new-dlpcompliancepolicy?view=exchange-ps) · Documentación · Oficial · Microsoft Learn (PowerShell). Referencia del cmdlet de Security & Compliance PowerShell para crear directivas DLP por código, con parámetros de ubicación (Exchange, SharePoint, OneDrive, Teams, Endpoint, Power BI, escáner, terceros), alcances adaptativos y modo.
- [New-DlpComplianceRule](https://learn.microsoft.com/en-us/powershell/module/exchangepowershell/new-dlpcompliancerule?view=exchange-ps) · Documentación · Oficial · Microsoft Learn (PowerShell). Referencia del cmdlet para crear reglas DLP (condiciones, excepciones, acciones, notificaciones, alertas, AdvancedRule), incluidos parámetros recientes como RestrictWebGrounding y TriggerPowerAutomateFlow.
- [userDataSecurityAndGovernance: processContent](https://learn.microsoft.com/en-us/graph/api/userdatasecurityandgovernance-processcontent?view=graph-rest-1.0) · Documentación · Oficial · Microsoft Learn (Microsoft Graph). API de Graph v1.0 que permite a una app empresarial o de IA enviar texto (prompts, mensajes) para evaluarlo contra las directivas de Purview y recibir la acción a aplicar.
- [Overview of Microsoft Purview APIs](https://learn.microsoft.com/en-us/purview/developer/microsoft-purview-sdk-documentation-overview) · Documentación · Oficial · Microsoft Learn (Purview Developer Platform). Visión general de las APIs de Purview en Graph (protectionScopes, processContent, contentActivities, sensitivityLabels) para que apps empresariales y de IA apliquen DLP y etiquetas en tiempo de ejecución.
- [Use Microsoft Purview APIs to leverage your policies in your apps](https://learn.microsoft.com/en-us/purview/developer/use-the-api) · Documentación · Oficial · Microsoft Learn (Purview Developer Platform). Tutorial para integrar una app (p. ej., GenAI) con Purview: calcular protection scopes por usuario, enviar contenido a processContent y aplicar la acción devuelta.
- [Microsoft Purview data security and governance APIs](https://learn.microsoft.com/en-us/graph/security-datasecurityandgovernance-overview) · Documentación · Oficial · Microsoft Learn (Microsoft Graph). Descripción de las APIs de seguridad y gobierno de datos de Purview en Graph: escenarios, requisitos de directivas (colección y DLP) y flujo de evaluación de contenido.
- [tenantDataSecurityAndGovernance: processContent](https://learn.microsoft.com/en-us/graph/api/tenantdatasecurityandgovernance-processcontent?view=graph-rest-beta) · Documentación · Oficial · Vista previa · Nuevo · Microsoft Learn (Microsoft Graph) · 23 oct 2026. Variante beta a nivel de tenant para evaluar interacciones de agentes (incluidas agente-a-herramienta) contra directivas DLP de Purview y devolver acciones como bloquear. *Nota:* API beta no soportada en producción; requiere Content.Process.All con consentimiento de administrador; usa metadatos de Entra Agent ID

### Anuncios y blogs oficiales

- [From DLP Alert Volume to Measurable Detection Assurance](https://techcommunity.microsoft.com/blog/microsoft-security-blog/from-dlp-alert-volume-to-measurable-detection-assurance/4545973) · Blog oficial · Empleado de Microsoft · Nuevo · Jon Nordstrom · Microsoft Security Community Blog (Tech Community) · 15 sep 2026. Presenta Data Security Workbench, un punto de partida open-source sobre la nueva API DLP de Purview que vincula incidentes con evidencia, usa IA gobernada para separar ruido, propone ajustes y mide su efecto.

### Laboratorios, GitHub y herramientas

- [microsoft/purview-api-samples](https://github.com/microsoft/purview-api-samples) · GitHub · Oficial · GitHub (Microsoft). Repositorio oficial de muestras de la plataforma de desarrollo de Purview: colección Postman de APIs Graph, app .NET, agente multicloud en AWS Bedrock y script para DLP de apps de IA personalizadas.
- [jonnords/dataworkbench: Agentic Data Security Workbench (DLP Response Studio)](https://github.com/jonnords/dataworkbench) · GitHub · Empleado de Microsoft · Jon Nordstrom · GitHub. Repositorio MIT de DLP Response Studio: consulta masiva, planificación y respuesta guiada sobre alertas DLP vía Graph delegado, con valores sensibles redactados y aplicación en vivo deshabilitada por defecto.
- [DLP Policy Creation Example (SMBTool Purview Toolkit)](https://github.com/microsoft/BestPractice_Deploy-Scripts/blob/main/Products/Purview/Examples/DLP-Policy-Example.md) · GitHub · Oficial · GitHub (Microsoft). Ejemplo idempotente de DLP como código que crea directivas por carga de trabajo basadas en GUID de etiquetas, arrancando en simulación y con runbook de salida de simulación.

**Manos a la obra**

1. `Laboratorio` Exporta la configuración de DLP a ZIP, descomprímela en un repositorio Git privado y haz el primer *commit* como línea base ([novedades](https://learn.microsoft.com/en-us/purview/whats-new)). Evidencia: repositorio con el *commit* y un README de lo que contiene.
2. `Laboratorio` Con Security & Compliance PowerShell, recrea tu directiva de [I2](01_Nivel_1_Inicial.md#i2) como `PRUEBA-DLP-<país>-v3-202611` en modo de simulación con [New-DlpCompliancePolicy](https://learn.microsoft.com/en-us/powershell/module/exchangepowershell/new-dlpcompliancepolicy?view=exchange-ps) y [New-DlpComplianceRule](https://learn.microsoft.com/en-us/powershell/module/exchangepowershell/new-dlpcompliancerule?view=exchange-ps), siguiendo el patrón idempotente del [ejemplo de Microsoft](https://github.com/microsoft/BestPractice_Deploy-Scripts/blob/main/Products/Purview/Examples/DLP-Policy-Example.md): si existe, reconcilia; si no, crea. Evidencia: script en el repositorio y dos ejecuciones seguidas, la segunda sin cambios.
3. `Laboratorio` Agrega a una regla de Exchange la acción de Power Automate con la plantilla «Notificar al gerente» y pruébala con una persona de prueba ([Power Automate en DLP](https://learn.microsoft.com/en-us/purview/dlp-powerautomate-int-get-started)). Evidencia: ejecución del flujo y correo recibido.
4. `Laboratorio` Define un control de cambios mínimo: toda modificación de directivas entra por *pull request*, se valida en simulación y se promueve con un mensaje que cita el ticket. Evidencia: un *pull request* revisado y la directiva resultante en simulación.
5. `Laboratorio parcial` Con la colección de Postman de las [muestras de Purview](https://github.com/microsoft/purview-api-samples), calcula los protection scopes de una persona de prueba y evalúa con processContent un prompt sintético de una app registrada en Entra ([usar las APIs](https://learn.microsoft.com/en-us/purview/developer/use-the-api)). Limitación: la directiva para la app solo se crea con PowerShell, puede requerir pago por uso y la variante de tenant está en beta. Evidencia: respuesta de la API con la acción devuelta.
6. `Solo producción` Despliega cambios de DLP desde el repositorio al tenant productivo. Cómo hacerlo seguro: exportación previa de la configuración, ejecución con una identidad dedicada y activación con PIM, prefijo y etiqueta «managed by» para no tocar directivas ajenas, arranque en simulación, revisión por pares y reversión con la exportación anterior.

**¿Quieres profundizar?**

- [jonnords/dataworkbench: Agentic Data Security Workbench (DLP Response Studio)](https://github.com/jonnords/dataworkbench) · GitHub

<a id="a2"></a>

## A2 · Integración con el SOC: Defender XDR y Sentinel

*L400 · ~6 h · Origen: Nuevo en esta edición*

El cambio más importante de 2026 para el SOC: desde inicios de octubre, una **regla integrada de ajuste de alertas** de Defender XDR registra las señales DLP como *behaviors* (tablas BehaviorInfo y BehaviorEntities) en lugar de alertas. Ya no generan incidentes ni aparecen en la cola, salvo que deshabilites o ajustes la regla en Settings > Microsoft Defender XDR > Alert tuning. Muchos equipos lo descubren cuando su tablero de incidentes DLP baja a cero de un día para otro.

A eso se suma el retiro de la API heredada `/security/alerts` de Microsoft Graph, que dejó de devolver datos el 15 de octubre de 2026: las integraciones de SOAR e ITSM deben migrar a `alerts_v2` e `incidents`, que incluyen DLP e Insider Risk pero no devuelven las alertas suprimidas por reglas de ajuste. En Sentinel, los incidentes DLP llegan por el conector de Defender XDR y se enriquecen con `CloudAppEvents`. Este módulo te ayuda a decidir qué señales DLP deben ser incidentes y cuáles comportamientos para la caza; el ajuste de alertas en general se profundiza en el programa de Defender XDR (M10).

**Por qué importa**

Si el SOC no ve las señales DLP, la exfiltración se detecta tarde o nunca; si las ve todas, se ahoga en ruido. Decidir de forma consciente qué directivas generan incidentes, qué queda como comportamiento y cómo se correlaciona con identidad y endpoint reduce el tiempo de detección de una fuga, evita integraciones rotas tras el retiro de la API y deja una decisión documentada ante auditoría.

**Qué vas a lograr**

- Explicar el modelo de behaviors y el efecto de la regla integrada de ajuste de alertas.
- Decidir y documentar qué directivas DLP deben generar incidentes en Defender XDR.
- Investigar señales DLP con búsqueda avanzada en CloudAppEvents, BehaviorInfo y BehaviorEntities.
- Migrar integraciones a alerts_v2 e incidents de Microsoft Graph.
- Llevar los incidentes DLP a Sentinel y enriquecerlos con CloudAppEvents.

> **Qué cambió.** **Desde inicios de octubre de 2026**, una regla integrada de ajuste de alertas convierte las señales DLP en *behaviors* (tablas `BehaviorInfo` y `BehaviorEntities`): no generan alertas ni incidentes en Defender XDR salvo que la deshabilites en Settings > Microsoft Defender XDR > Alert tuning ([investigar DLP en Defender](https://learn.microsoft.com/en-us/defender-xdr/dlp-investigate-alerts-defender)). La página general de DLP todavía dice que las alertas se envían a Defender y se conservan seis meses: para el comportamiento actual, prevalece la página de Defender.

> **Qué cambió.** La API heredada `/security/alerts` de Microsoft Graph dejó de devolver datos el **15 de octubre de 2026**. `alerts_v2` e `incidents` incluyen las alertas de DLP e Insider Risk, pero no devuelven las alertas suprimidas por reglas de ajuste, y la guía indica que Sentinel debe estar conectado al portal de Defender ([migración](https://learn.microsoft.com/en-us/graph/alertsv1-alertsv2-migration)). Revisa tus integraciones de SOAR e ITSM.

> **Atención.** Licencia para investigar DLP en Defender: Office 365 E5/A5, Microsoft 365 E5/A5, E5/A5 Compliance o E5/A5 Information Protection & Governance. `CloudAppEvents` cubre 30 días de auditoría y las consultas integradas «Go Hunt» están en vista previa ([investigar DLP en Defender](https://learn.microsoft.com/en-us/defender-xdr/dlp-investigate-alerts-defender)). El ajuste de alertas en general —acciones Hide, Resolve y Set as behavior, y la selección por origen de detección (vista previa), que entra en vigor el 8 de noviembre de 2026— se profundiza en el programa de Defender XDR (M10) ([ajuste de alertas](https://learn.microsoft.com/en-us/defender-xdr/investigate-alerts)).

> **Consejo Ninja.** En Sentinel, los incidentes DLP llegan por el conector de Defender XDR y se enriquecen con `CloudAppEvents` ([DLP en Sentinel](https://learn.microsoft.com/en-us/defender-xdr/dlp-investigate-alerts-sentinel)): si cambias la regla de ajuste, cambia también lo que llega a Sentinel, así que documenta la decisión en ambos lados. Las alertas de Insider Risk se cazan además en `DataSecurityBehaviors` ([tabla](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-datasecuritybehaviors-table)), tema del programa de Insider Risk Management (A2).

**¿Tienes poco tiempo?**

- [Investigate data loss prevention alerts with Microsoft Defender XDR](https://learn.microsoft.com/en-us/defender-xdr/dlp-investigate-alerts-defender) · Documentación
- [Migrate from legacy alerts to the alerts and incidents API](https://learn.microsoft.com/en-us/graph/alertsv1-alertsv2-migration) · Documentación
- [Investigate data loss prevention alerts with Microsoft Sentinel](https://learn.microsoft.com/en-us/defender-xdr/dlp-investigate-alerts-sentinel) · Documentación

**Dónde ver las señales DLP después de octubre de 2026**

| Lugar | Qué muestra | Ventana o retención | Cuándo usarlo | Fuente |
|---|---|---|---|---|
| Panel de alertas DLP (Purview) | Alertas de directivas activas, vista del agente de triage (vista previa) y resumen con Security Copilot | 30 días según la página general; la retención de auditoría también influye | Triage del equipo DLP | [Panel de alertas](https://learn.microsoft.com/en-us/purview/dlp-alerts-dashboard-get-started) |
| Explorador de actividad | Actividades y coincidencias, incluidas las de endpoint, red y navegador | 30 días, con 60 a 90 minutos de demora | Investigación y ajuste | [Explorador de actividad](https://learn.microsoft.com/en-us/purview/data-classification-activity-explorer) |
| Cola de incidentes de Defender XDR | Alertas DLP correlacionadas con identidad, correo y endpoint, solo si la regla integrada de ajuste se deshabilita o se acota | Seis meses | Respuesta del SOC con contexto completo | [DLP en Defender](https://learn.microsoft.com/en-us/defender-xdr/dlp-investigate-alerts-defender) |
| BehaviorInfo y BehaviorEntities | Señales DLP convertidas en behaviors por la regla integrada | Según la búsqueda avanzada | Caza y correlación sin abrir incidentes | [DLP en Defender](https://learn.microsoft.com/en-us/defender-xdr/dlp-investigate-alerts-defender) |
| CloudAppEvents | Eventos de auditoría que originan las coincidencias | 30 días | Enriquecimiento y caza | [DLP en Defender](https://learn.microsoft.com/en-us/defender-xdr/dlp-investigate-alerts-defender) |
| alerts_v2 e incidents (Microsoft Graph) | Alertas e incidentes de DLP e Insider Risk, sin las alertas suprimidas por ajuste | Según el servicio | Integraciones de SOAR e ITSM | [Migración](https://learn.microsoft.com/en-us/graph/alertsv1-alertsv2-migration) |
| Microsoft Sentinel (conector de Defender XDR) | Incidentes DLP enriquecidos con CloudAppEvents | Según la retención del workspace | Correlación de largo plazo y automatización | [DLP en Sentinel](https://learn.microsoft.com/en-us/defender-xdr/dlp-investigate-alerts-sentinel) |

La API heredada /security/alerts dejó de devolver datos el 15 de octubre de 2026. Fuentes: páginas citadas en cada fila, verificadas al 6 de noviembre de 2026.

### Documentación, cursos y credenciales

- [Migrate from legacy alerts to the alerts and incidents API](https://learn.microsoft.com/en-us/graph/alertsv1-alertsv2-migration) · Documentación · Oficial · Nuevo · Microsoft Learn (Microsoft Graph) · 25 sep 2026. Guía para migrar del API heredado /security/alerts (retirado el 15-oct-2026) a alerts_v2/incidents, que incluye alertas de Purview DLP e Insider Risk.
- [Investigate data loss prevention alerts with Microsoft Defender XDR](https://learn.microsoft.com/en-us/defender-xdr/dlp-investigate-alerts-defender) · Documentación · Oficial · Nuevo · Microsoft Learn (Defender XDR) · 31 ago 2026. Cómo investigar alertas DLP en el portal de Defender: cola unificada de incidentes, correlación con otras soluciones, búsqueda avanzada (CloudAppEvents), resumen con Security Copilot y acciones de remediación.
- [Investigate data loss prevention alerts with Microsoft Sentinel](https://learn.microsoft.com/en-us/defender-xdr/dlp-investigate-alerts-sentinel) · Documentación · Oficial · Nuevo · Microsoft Learn (Defender XDR) · 11 ago 2026. Uso del conector de Defender XDR y de CloudAppEvents en Sentinel para importar incidentes DLP, correlacionarlos y consultar con KQL las actividades que originaron cada alerta.

**Manos a la obra**

1. `Laboratorio` En el portal de Defender, abre Settings > Microsoft Defender XDR > Alert tuning, localiza la regla integrada de DLP y documenta su alcance. Genera una coincidencia DLP con una directiva activa de auditoría y búscala como *behavior* en `BehaviorInfo` y `BehaviorEntities` con búsqueda avanzada ([investigar DLP en Defender](https://learn.microsoft.com/en-us/defender-xdr/dlp-investigate-alerts-defender)). Evidencia: consulta KQL y resultado con el behavior.
2. `Laboratorio` Deshabilita la regla solo en el laboratorio, genera otra coincidencia y compara: ahora aparece como alerta e incidente. Usa el resumen de Security Copilot si tu tenant lo tiene disponible. Evidencia: incidente generado y tabla «con regla» frente a «sin regla».
3. `Laboratorio` Con búsqueda avanzada, consulta en `CloudAppEvents` las actividades asociadas a tus coincidencias DLP de los últimos 7 días (filtra por el archivo o la persona de prueba) y, en `DeviceInfo`, la columna `DlpInfo` de la VM. Prueba también una consulta integrada «Go Hunt» (vista previa). Evidencia: dos consultas guardadas con su resultado.
4. `Laboratorio` En Graph Explorer, con el permiso SecurityAlert.Read.All, consulta `/security/alerts_v2` e `/security/incidents` y comprueba qué alertas DLP aparecen con la regla de ajuste activa y sin ella ([migración](https://learn.microsoft.com/en-us/graph/alertsv1-alertsv2-migration)). Evidencia: respuestas JSON comparadas.
5. `Laboratorio` Verifica que el conector de Defender XDR del workspace de Sentinel del laboratorio trae el incidente DLP y enriquécelo con una consulta a `CloudAppEvents` ([DLP en Sentinel](https://learn.microsoft.com/en-us/defender-xdr/dlp-investigate-alerts-sentinel)). Evidencia: incidente en Sentinel con la consulta de enriquecimiento.
6. `Solo producción` Decide qué directivas DLP deben generar incidentes en producción (por ejemplo, bloqueos con invalidación sobre datos de alto impacto o coincidencias de personas en nivel Elevated) y cuáles quedan como behaviors para la caza. Cómo hacerlo seguro: análisis del volumen de un mes con rol de solo lectura, regla de ajuste modificada solo para las directivas elegidas, aviso previo al SOC, revisión a las dos semanas y reversión documentada. Evidencia: acta de decisión acordada entre DLP y el SOC.

<a id="a3"></a>

## A3 · Escenarios avanzados: EDM a escala, huellas digitales y OCR

*L400 · ~6 h · Origen: Ruta Ninja de Learn, módulo 1 (EDM y huellas digitales), llevado a escala*

Cuando los SIT por patrones no alcanzan, Purview ofrece herramientas de precisión. **Exact Data Match (EDM)** compara contra los valores reales de tus tablas (clientes, empleados, pacientes) mediante hashes; la nueva experiencia unificada crea el esquema y el SIT desde un archivo de muestra. La regla de oro: el elemento primario debe ser un SIT estricto, nunca uno laxo como nombres completos, direcciones o expresiones regulares amplias, porque degradan el rendimiento y causan falsos negativos. Antes de cargar datos reales, revisa las regiones donde EDM está disponible.

Las **huellas digitales de documentos** detectan formularios y plantillas (contratos, fichas, formularios regulatorios) con coincidencia parcial o exacta; evita el 100 % salvo en documentos críticos, porque una conversión a PDF lo rompe, y recuerda que desde abril de 2023 los clientes E3 no pueden crear huellas nuevas. Los **clasificadores entrenables** cubren contenido conceptual y el **OCR** extiende la detección a imágenes y PDF escaneados en DLP, etiquetado automático e Insider Risk, con pago por uso por imagen o página. La clasificación en sí se profundiza en el programa de Information Protection (I2).

**Por qué importa**

En sectores regulados, la diferencia entre detectar «un número de 16 dígitos» y detectar «la tarjeta de uno de nuestros clientes» es la diferencia entre un programa que alerta todo y uno que bloquea con precisión. EDM y las huellas permiten bloquear sin falsos positivos lo que realmente importa, y el OCR cierra el hueco de las fotos de documentos de identidad y los escaneos, frecuentes en banca, seguros y salud.

**Qué vas a lograr**

- Diseñar un esquema EDM con un elemento primario estricto y evidencia corroborante.
- Crear y probar un SIT de huella digital con el umbral adecuado.
- Combinar clasificadores entrenables con SIT para contenido complejo.
- Activar OCR con alcance acotado y control de costos.
- Verificar la residencia de datos de EDM para las regiones de MCSA.

> **Atención.** Residencia de datos: la lista de regiones de EDM incluye Brasil y EE. UU., pero no otras regiones de Latinoamérica ([EDM](https://learn.microsoft.com/en-us/purview/sit-get-started-exact-data-match-based-sits-overview)). Antes de cargar tablas reales de clientes de México, Chile o Colombia, revisa con privacidad y Legal qué región corresponde a tu tenant y si cumple tus requisitos.

> **Consejo Ninja.** Para un EDM preciso, el elemento primario debe ser un SIT estricto; evita SIT laxos como nombres completos, direcciones o expresiones regulares amplias, que degradan el rendimiento y causan falsos negativos; ignora delimitadores y usa columnas de evidencia corroborante ([paso 2](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-reduce-false-positives-step2)). El archivo de muestra debe imitar el formato real con valores sintéticos ([archivo de muestra](https://learn.microsoft.com/en-us/purview/sit-create-edm-sit-unified-ux-sample-file)).

> **Qué cambió.** Desde abril de 2023, los clientes E3 no pueden crear ni modificar huellas digitales nuevas ([huellas digitales](https://learn.microsoft.com/en-us/purview/sit-document-fingerprinting)). Usa coincidencia parcial (50, 70 o 90 %) y evita el 100 % salvo en documentos críticos: una conversión a PDF o un encabezado alterado rompen la coincidencia ([paso 4](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-reduce-false-positives-step4)).

> **Atención.** El OCR se factura por pago por uso, por imagen o por página, y requiere vincular una suscripción de Azure: define el alcance por ubicación para controlar el costo ([OCR](https://learn.microsoft.com/en-us/purview/ocr-learn-about)). En Endpoint DLP, la clasificación avanzada envía contenido a la nube con límites de 64 MB para texto y 50 MB para imágenes con OCR, y «pegar en el navegador» no la admite ([configuración de Endpoint DLP](https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings)).

**¿Tienes poco tiempo?**

- [Get started with exact data match sensitive information types in Microsoft Purview](https://learn.microsoft.com/en-us/purview/sit-get-started-exact-data-match-based-sits-overview) · Documentación
- [Step 2: Implement Exact Data Match for precise matching](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-reduce-false-positives-step2) · Documentación
- [Document fingerprinting](https://learn.microsoft.com/en-us/purview/sit-document-fingerprinting) · Documentación
- [Learn about optical character recognition in Microsoft Purview](https://learn.microsoft.com/en-us/purview/ocr-learn-about) · Documentación

### Documentación, cursos y credenciales

- [Get started with exact data match sensitive information types in Microsoft Purview](https://learn.microsoft.com/en-us/purview/sit-get-started-exact-data-match-based-sits-overview) · Documentación · Oficial · Microsoft Learn. Introducción a EDM: compara la nueva experiencia (esquema y SIT en un solo flujo con archivo de muestra) con la clásica y PowerShell, e indica regiones soportadas y roles.
- [Learn about optical character recognition in Microsoft Purview](https://learn.microsoft.com/en-us/purview/ocr-learn-about) · Documentación · Oficial · Microsoft Learn. OCR en Purview: escaneo de imágenes y PDFs escaneados para detectar SIT en DLP, autoetiquetado e IRM, con facturación de pago por uso por imagen o página.
- [Step 2: Implement Exact Data Match for precise matching](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-reduce-false-positives-step2) · Documentación · Oficial · Microsoft Learn (Deployment models) · 3 abr 2026. Guía para EDM preciso: esquema desde archivo de muestra, mapear el elemento primario a un SIT estrictamente definido, ignorar delimitadores y usar columnas de evidencia corroborante.
- [Document fingerprinting](https://learn.microsoft.com/en-us/purview/sit-document-fingerprinting) · Documentación · Oficial · Microsoft Learn. Explica cómo crear SIT a partir de formularios estándar (huella hash, sin almacenar el original) para usarlos en DLP de Exchange, SharePoint, OneDrive, Teams y dispositivos.
- [Implement information protection with Microsoft Purview (learning path)](https://learn.microsoft.com/en-us/training/paths/purview-implement-information-protection/) · Curso · Oficial · Microsoft Learn. Ruta de Learn (SC-401) sobre clasificación: SIT personalizados, EDM, fingerprinting, clasificadores entrenables y etiquetas, base para ajustar DLP a escala.
- [Step 3: Use trainable classifiers for complex content](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-reduce-false-positives-step3) · Documentación · Oficial · Microsoft Learn (Deployment models) · 3 abr 2026. Cómo usar clasificadores entrenables integrados o personalizados (muestras positivas/negativas, retroalimentación) y combinarlos con SIT para mayor precisión.
- [Step 4: Apply document fingerprinting for templates](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-reduce-false-positives-step4) · Documentación · Oficial · Microsoft Learn (Deployment models) · 3 abr 2026. Cómo aplicar huellas digitales de documentos a plantillas de alto valor con coincidencia parcial (50/70/90%) o exacta y ajustar umbrales según resultados reales.

**Manos a la obra**

1. `Laboratorio parcial` Crea un SIT EDM con la experiencia unificada a partir de un archivo de muestra sintético de 10 a 20 filas (por ejemplo, clientes con RFC, RUT o cédula), con un elemento primario estricto y dos columnas corroborantes; carga los datos con hash y prueba después de al menos una hora ([EDM](https://learn.microsoft.com/en-us/purview/sit-get-started-exact-data-match-based-sits-overview), [paso 2](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-reduce-false-positives-step2)). Limitación: con datos sintéticos aprendes el procedimiento, no el rendimiento a escala. Evidencia: SIT probado con un archivo que coincide y otro que no.
2. `Laboratorio` Crea un SIT de huella digital desde una plantilla de contrato sintética con coincidencia parcial del 70 % y pruébalo con la plantilla completada, una versión convertida a PDF y otra con el encabezado cambiado ([huellas digitales](https://learn.microsoft.com/en-us/purview/sit-document-fingerprinting)). Evidencia: tabla de resultados por variante y umbral.
3. `Laboratorio parcial` Combina un clasificador entrenable integrado (por ejemplo, de contratos o de currículums) con un SIT de monto en una regla en simulación ([paso 3](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-reduce-false-positives-step3)). Limitación: un clasificador personalizado necesita de 50 a 500 muestras positivas y de 150 a 1.500 negativas ([clasificadores entrenables](https://learn.microsoft.com/en-us/purview/trainable-classifiers-get-started-with)); con datos sintéticos no medirás la precisión real. Evidencia: coincidencias de la regla combinada frente a la de solo SIT.
4. `Laboratorio parcial` Activa el OCR solo para una ubicación de prueba y verifica que la imagen de un documento de identidad sintético dispara la regla ([OCR](https://learn.microsoft.com/en-us/purview/ocr-learn-about)). Limitación: es pago por uso por imagen; usa una suscripción con presupuesto, porque la cobertura por el crédito de Visual Studio no está confirmada. Evidencia: coincidencia y costo registrado en el [uso de pago por uso](https://learn.microsoft.com/en-us/purview/purview-billing-usage).
5. `Laboratorio` Completa los módulos de clasificación de la ruta [Implement information protection with Microsoft Purview](https://learn.microsoft.com/en-us/training/paths/purview-implement-information-protection/) (SIT personalizados, EDM, huellas digitales y clasificadores entrenables) y los laboratorios de SC-401 que los acompañan antes de llevar EDM a producción. Evidencia: módulos completados.
6. `Solo producción` Lleva un SIT EDM a producción con la tabla real de clientes. Cómo hacerlo seguro: aprobación del dueño de los datos y de privacidad, verificación de la región de EDM, carga de hashes desde un equipo administrado con roles mínimos, directiva v2 en simulación durante dos semanas y comparación de precisión con el SIT por patrones antes de activar el bloqueo.

<a id="a4"></a>

## A4 · Security Copilot y agentes para DLP

*L400 · ~4 h · Origen: Ruta Ninja de Learn, módulo 3 (agentes de triage), ampliado*

Security Copilot llega a DLP de tres formas. **Embebido**: resume alertas DLP, genera filtros del explorador de actividad en lenguaje natural (vista previa) y aporta recomendaciones en el diagnóstico guiado para tenants elegibles. **Agéntico**: el **Microsoft Purview Triage Agent** (Data Security Triage Agent en el Centro de mensajes) prioriza alertas de Exchange, Teams, SharePoint, OneDrive y dispositivos, explica su razonamiento y aprende de tus instrucciones. Y **de postura**: el Data Security Posture Agent, que se trata en el programa de DSPM (A1).

Los requisitos son concretos: licencia DLP por usuario, modelo de pago por uso habilitado y SCU aprovisionadas. El agente solo tría directivas activas (no en simulación), mira hasta 30 días atrás, analiza archivos de hasta 2 MB, necesita la recolección de evidencia para los endpoints y se gestiona solo desde Purview, aunque se despliegue desde Defender. Su estado es contradictorio entre fuentes y sus resúmenes en Defender XDR siguen en vista previa, con GA pospuesta a agosto de 2027. El gobierno de Security Copilot en general se profundiza en su propio programa (M5 y M7).

**Por qué importa**

El triage manual de alertas DLP no escala: la mayoría son de bajo riesgo y el analista dedica su tiempo a descartarlas. Un agente bien acotado concentra la atención humana en lo urgente, pero consume SCU y procesa contenido sensible. Este módulo te ayuda a decidir dónde aporta valor, cuánto cuesta y cómo gobernarlo antes de habilitarlo en producción.

**Qué vas a lograr**

- Usar las capacidades embebidas de Security Copilot en alertas, explorador de actividad y diagnóstico.
- Verificar los requisitos de licencia, pago por uso, SCU, identidad y evidencia del agente de triage.
- Desplegar el agente de triage con alcance acotado y medir su consumo de SCU.
- Gobernar el agente: identidad de agente, permisos, instrucciones, presupuesto y revisión humana.

> **Atención.** **Estado contradictorio del agente de triage.** La guía de inicio (25 de junio de 2026) no lo rotula como vista previa ([agente de triage en DLP](https://learn.microsoft.com/en-us/purview/copilot-in-purview-triage-dlp-agent-get-started)), la página de agentes de Purview sí ([agentes en Purview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-agents)), y el Centro de mensajes pospuso a agosto de 2027 la GA de sus resúmenes en las alertas DLP de Defender XDR ([MC1255406](https://mc.merill.net/message/MC1255406)). Trátalo como vista previa en tus decisiones de producción.

> **Consejo Ninja.** Requisitos y límites: licencia DLP por usuario, modelo de pago por uso y SCU aprovisionadas; tría Exchange, Teams, SharePoint, OneDrive y dispositivos (estos con recolección de evidencia), solo directivas activas, hasta 30 días atrás y archivos de hasta 2 MB; usa una identidad de agente de Entra y se gestiona solo desde Purview ([guía](https://learn.microsoft.com/en-us/purview/copilot-in-purview-triage-dlp-agent-get-started)). Todos los agentes de Purview consumen SCU y no reconocen unidades administrativas salvo por el contexto del administrador ([visión general](https://learn.microsoft.com/en-us/purview/copilot-in-purview-agents-overview)).

> **Novedad.** Microsoft 365 E5 y E7 incluyen Security Copilot: 400 SCU al mes por cada 1.000 licencias pagas, hasta 10.000 ([inclusión](https://learn.microsoft.com/en-us/copilot/security/security-copilot-inclusion)); una prueba no las habilita. En la hoja de ruta, la traza de razonamiento y el puntaje de confianza por decisión del agente figuran con vista previa en septiembre y GA prevista en octubre de 2026, pero con estado «In development» ([hoja de ruta 560597](https://www.microsoft.com/releasecommunications/api/v2/m365/rss/560597)).

> **Consejo Ninja.** Las capacidades generales de Security Copilot —prompts, plugins, roles y gobierno del consumo— se profundizan en el programa de Security Copilot (M5 y M7), y el Data Security Posture Agent, en el de DSPM (A1). La demostración [New Agents in Microsoft Purview](https://www.youtube.com/watch?v=cu2FJ2f7Jho) muestra el agente de triage priorizando alertas y explicando su razonamiento.

**¿Tienes poco tiempo?**

- [Get started with the Microsoft Purview Triage Agent in Data Loss Prevention](https://learn.microsoft.com/en-us/purview/copilot-in-purview-triage-dlp-agent-get-started) · Documentación
- [Security Copilot agents in Microsoft Purview overview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-agents-overview) · Documentación
- [New Agents in Microsoft Purview](https://www.youtube.com/watch?v=cu2FJ2f7Jho) · Video

### Documentación, cursos y credenciales

- [Security Copilot agents in Microsoft Purview overview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-agents-overview) · Documentación · Oficial · Microsoft Learn. Visión general de los agentes de Purview: Data Security Triage Agent (DLP e IRM) y Data Security Posture Agent (DSPM y DSI, preview), conceptos de disparadores, ventanas de tiempo e instrucciones personalizadas.
- [Get started with the Microsoft Purview Triage Agent in Data Loss Prevention](https://learn.microsoft.com/en-us/purview/copilot-in-purview-triage-dlp-agent-get-started) · Documentación · Oficial · Vista previa · Nuevo · Microsoft Learn · 25 jun 2026. Despliegue del agente de triaje de DLP (alertas de Exchange, Teams, OneDrive, SharePoint y endpoint) en Purview y Defender XDR, con identidad de agente de Entra recomendada y consumo de SCU. *Nota:* Verificado (actualizado 25-jun-2026; la página no rotula el agente como preview, pero recordatorios en Teams e instrucciones personalizadas sí lo están). Requiere licencia DLP por usuario + modelo de pago por uso + SCU aprovisionadas…
- [Microsoft 365 Roadmap 560597 - Data Security Triage Agent in DLP: Reasoning Trace and Confidence Score](https://www.microsoft.com/releasecommunications/api/v2/m365/rss/560597) · Documentación · Oficial · Vista previa · Nuevo · Microsoft 365 Roadmap (RSS) · 19 ago 2026. Elemento de hoja de ruta que agrega traza de razonamiento y puntaje de confianza a cada decisión del agente de triaje DLP para que el SOC pueda auditarlas. *Nota:* Preview sep-2026, GA prevista oct-2026 (estado "In development" en el feed)
- [MC1255406 - Microsoft Purview | Data Security Triage Agent Summaries for DLP Alerts in Microsoft Defender XDR](https://mc.merill.net/message/MC1255406) · Documentación · Oficial · Vista previa · Nuevo · Microsoft 365 Message Center Archive (mc.merill.net) · 17 ago 2026. Aviso: resúmenes y categorizaciones del Data Security Triage Agent visibles en alertas DLP del portal Defender XDR, con despliegue del agente desde Defender y gestión en Purview. *Nota:* Preview abr-2026; GA pospuesta a agosto de 2027 (antes ago-2026)
- [MC1293479 - Microsoft Purview | Data Loss Prevention: New guided diagnostics experience for DLP](https://mc.merill.net/message/MC1293479) · Documentación · Oficial · Vista previa · Nuevo · Microsoft 365 Message Center Archive (mc.merill.net) · 4 ago 2026. Aviso de la nueva experiencia de diagnóstico guiado de DLP (orden de evaluación, condiciones coincidentes y acciones) con recomendaciones de Security Copilot para tenants elegibles. *Nota:* Preview inicio sep-2026; GA desde oct-2026; insights de Copilot solo con E5 + licenciamiento Copilot elegible
- [Microsoft Security Copilot agents in Microsoft Purview (preview)](https://learn.microsoft.com/en-us/purview/copilot-in-purview-agents) · Documentación · Oficial · Vista previa · Microsoft Learn · 24 feb 2026. Ficha de atributos de los agentes de triaje DLP e IRM: criterios (sensibilidad, exfiltración, riesgo de directiva), cuatro categorías, licencias, identidad, permisos y disparadores. *Nota:* Indica autenticación que expira a 90 días (modelo previo a Entra Agent ID) y licencia DLP con E3/E5/A5/F5/G5 + pago por uso

### Webinars, videos y podcasts

- [New Agents in Microsoft Purview](https://www.youtube.com/watch?v=cu2FJ2f7Jho) · Video · Empleado de Microsoft · Microsoft Mechanics · Microsoft Mechanics (YouTube). Demostración del Data Security Triage Agent (DLP/IRM) que prioriza alertas, explica su razonamiento y contacta usuarios en Teams, y del Data Security Posture Agent con consultas en lenguaje natural.

**Manos a la obra**

1. `Laboratorio parcial` Usa el resumen de Security Copilot de una alerta DLP en el panel de alertas y, si está disponible, la generación de filtros en lenguaje natural del explorador de actividad (vista previa); compáralos con tu triage manual de [M2](02_Nivel_2_Intermedio.md#m2). Limitación: necesitas capacidad de Security Copilot; en el laboratorio, crea una capacidad temporal de 1 SCU con excedente 0 y bórrala al terminar ([incorporación manual](https://learn.microsoft.com/en-us/copilot/security/manual-onboarding)). Evidencia: resumen generado y diferencias anotadas.
2. `Laboratorio parcial` Prepara los requisitos del agente de triage: modelo de pago por uso habilitado con una suscripción del mismo tenant, capacidad de SCU, plugin de Purview e identidad de agente de Entra ([guía](https://learn.microsoft.com/en-us/purview/copilot-in-purview-triage-dlp-agent-get-started)). Limitación: 1 SCU cuesta 4 USD por hora, se factura por bloques de hora y no hay prueba gratuita ([precios](https://www.microsoft.com/en-us/security/pricing/microsoft-security-copilot/)). Evidencia: lista de verificación completada.
3. `Laboratorio parcial` Despliega el agente sobre una directiva activa de auditoría (no en simulación) con «solo alertas nuevas», ejecútalo de forma manual sobre las alertas de tus personas de prueba y revisa su categorización y su razonamiento. Limitación: con pocas alertas sintéticas no medirás su precisión real. Evidencia: alertas categorizadas y SCU consumidas en el panel de uso.
4. `Laboratorio` Escribe las instrucciones personalizadas del agente (qué datos son críticos para tu negocio y qué destinos son de riesgo; las instrucciones personalizadas están en vista previa) y su ficha de gobierno: dueño, identidad, permisos, alcance, revisión humana y presupuesto mensual de SCU ([visión general de agentes](https://learn.microsoft.com/en-us/purview/copilot-in-purview-agents-overview)). Evidencia: ficha de una página.
5. `Solo producción` Habilita el agente en producción con la inclusión de E5 o una capacidad productiva. Cómo hacerlo seguro: alcance a pocas directivas activas, solo alertas nuevas, ejecuciones manuales al principio, límite de excedente, aprobación del dueño del presupuesto, revisión humana de cada categorización durante un mes y comparación semanal con el triage manual.

<a id="reto-avanzado"></a>

## Reto del nivel

**DLP como código conectado al SOC.** Publica en un repositorio tus directivas de prueba recreadas por PowerShell en simulación, un SIT EDM o de huella digital probado, la decisión documentada sobre la regla integrada de ajuste de alertas (qué directivas generan incidentes y cuáles quedan como behaviors), las consultas de búsqueda avanzada que usará el SOC y la ficha de gobierno del agente de triage con su presupuesto de SCU. Entregables: repositorio y presentación de diez minutos.

<a id="quiz-avanzado"></a>

## Evaluación del nivel

Responde y compara con [Evaluaciones y respuestas](06_Evaluaciones_y_respuestas.md#eval-avanzado). Con 80 % o más, ¡nivel aprobado! (En la versión web puedes corregir en línea y generar tu certificado).

1. Desde inicios de octubre de 2026, ¿qué ocurre por defecto con las señales DLP en Defender XDR?
   - a) Se eliminan
   - b) Solo se envían a Sentinel
   - c) Se convierten en casos de Insider Risk
   - d) Una regla integrada de ajuste las registra como behaviors y no crean incidentes

2. ¿Cuándo dejó de devolver datos la API heredada /security/alerts de Microsoft Graph?
   - a) 1 de julio de 2026
   - b) 15 de octubre de 2026
   - c) 6 de enero de 2027
   - d) 31 de marzo de 2027

3. ¿Qué limitación tiene alerts_v2 de Microsoft Graph respecto de las alertas DLP?
   - a) No incluye alertas de DLP
   - b) Solo devuelve alertas de los últimos 7 días
   - c) No devuelve las alertas suprimidas por reglas de ajuste
   - d) Requiere Microsoft 365 E7

4. ¿Dónde se deshabilita o acota la regla integrada que convierte las señales DLP en behaviors?
   - a) En Purview > Data loss prevention > Settings
   - b) En Settings > Microsoft Defender XDR > Alert tuning, en el portal de Defender
   - c) En el centro de administración de Entra
   - d) En la configuración del workspace de Sentinel

5. ¿Cómo se crean las directivas DLP para apps registradas en Entra?
   - a) Solo con PowerShell
   - b) Desde el portal de Purview con una plantilla
   - c) Con Power Automate
   - d) Desde el centro de administración de Entra

6. ¿Qué plano de aplicación reemplaza al obsoleto «Entra» en la DLP de apps de IA personalizadas?
   - a) Endpoint
   - b) Network
   - c) Browser
   - d) Application

7. ¿Qué es cierto sobre Power Automate como acción de una regla DLP?
   - a) Requiere una licencia adicional de Purview
   - b) Funciona en Exchange, SharePoint y OneDrive, y Windows 24H2 o posterior, sin licencia adicional de Purview
   - c) Solo funciona en Teams
   - d) En SharePoint se dispara también con contenido existente sin cambios

8. ¿Cuál es el estado de la variante de tenant de processContent para interacciones de agentes?
   - a) Disponible en general desde mayo de 2026
   - b) Retirada
   - c) Beta desde el 23 de octubre de 2026, sin soporte para producción
   - d) Disponible solo en nubes de Government

9. Para un SIT EDM preciso, ¿qué elemento primario recomienda la guía?
   - a) Un SIT estrictamente definido
   - b) Un nombre completo
   - c) Una dirección postal
   - d) Una expresión regular amplia

10. ¿Qué limitación tienen los clientes E3 con las huellas digitales de documentos?
   - a) No pueden usarlas en Exchange
   - b) Solo pueden usar coincidencia exacta
   - c) Deben pagarlas por uso
   - d) Desde abril de 2023 no pueden crear ni modificar huellas nuevas

11. ¿Cómo se factura el OCR de Purview?
   - a) Está incluido en E3
   - b) Por pago por uso, por imagen o por página
   - c) Con SCU de Security Copilot
   - d) Con la licencia de Microsoft 365 Copilot

12. ¿Qué es cierto sobre el agente de triage de DLP?
   - a) Tría alertas de directivas en simulación
   - b) Se administra desde el portal de Defender
   - c) Requiere licencia DLP, pago por uso y SCU, y tría Exchange, Teams, SharePoint, OneDrive y dispositivos
   - d) Analiza archivos de cualquier tamaño

13. Según el Centro de mensajes, ¿cuándo se espera la disponibilidad general de los resúmenes del agente de triage en las alertas DLP de Defender XDR?
   - a) Octubre de 2026
   - b) Diciembre de 2026
   - c) Ya están en disponibilidad general
   - d) Agosto de 2027

14. ¿Cuántas SCU de Security Copilot incluye Microsoft 365 E5?
   - a) 400 SCU al mes por cada 1.000 licencias pagas, hasta 10.000
   - b) 100 SCU fijas por tenant
   - c) Ninguna
   - d) SCU ilimitadas

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. No constituye asesoría legal ni laboral: las decisiones sobre monitoreo, evidencias, privacidad y normativa corresponden a tus áreas de Legal, RR. HH. y privacidad. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

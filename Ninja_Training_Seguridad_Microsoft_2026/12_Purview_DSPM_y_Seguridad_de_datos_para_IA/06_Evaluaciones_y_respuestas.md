# Evaluaciones y respuestas

*Microsoft Purview DSPM y seguridad de datos para IA Ninja Training · Edición 2026*

[← Comunidad](05_Comunidad.md) · [Índice del programa](README.md) · [Laboratorio y práctica en producción →](07_Laboratorio_y_practica_en_produccion.md)

<a id="respuestas"></a>

Cada evaluación tiene preguntas de opción múltiple. Con 80 % o más el nivel se considera aprobado. Es una autoevaluación de esta guía, no una certificación de Microsoft.

<a id="eval-inicial"></a>

## Nivel 1 · Inicial · Ver la postura y la exposición

**1. Según la versión vigente de MC1481315, ¿cuándo se completa el retiro de DSPM (classic) y DSPM for AI (classic)?**

- a) Fines de noviembre de 2026
- b) Fines de diciembre de 2026
- c) Fines de enero de 2027  ✅
- d) 31 de marzo de 2027

*Respuesta: c).* MC1481315 se actualizó el 27 de octubre de 2026 y movió el inicio y el fin del retiro a fines de enero de 2027; la versión original indicaba de fines de noviembre a fines de diciembre de 2026. [Fuente](https://mc.merill.net/message/MC1481315) · Repasa [I1](01_Nivel_1_Inicial.md#i1)

**2. ¿Qué licencia base habilita DSPM sobre los datos de Microsoft 365?**

- a) Microsoft 365 E5 o Microsoft Purview Suite (antes E5 Compliance)  ✅
- b) Microsoft 365 E3 sin complementos
- c) Solo Agent 365
- d) Solo el pago por uso

*Respuesta: a).* La documentación indica E5 o Purview Suite. El pago por uso se reserva para orígenes que no son Microsoft 365, la red y las apps y agentes de IA, y Agent 365 se exige para las capacidades de agentes. [Fuente](https://learn.microsoft.com/en-us/purview/data-security-posture-management-get-started) · Repasa [P0](01_Nivel_1_Inicial.md#p0)

**3. ¿En qué página de DSPM aparecen los agentes de Agent 365?**

- a) Discover > Apps and agents
- b) Data risk assessments
- c) Asset explorer
- d) AI observability  ✅

*Respuesta: d).* AI observability inventaría las apps y agentes con actividad en los últimos 30 días, incluido Agent 365; el panel Apps and agents no lo incluye. [Fuente](https://learn.microsoft.com/en-us/purview/data-security-posture-management-learn-about) · Repasa [I2](01_Nivel_1_Inicial.md#i2)

**4. ¿Qué revisa la evaluación de riesgo de datos predeterminada de DSPM?**

- a) Todos los sitios de SharePoint, cada día
- b) Los 100 sitios de SharePoint más usados, cada semana  ✅
- c) Solo los OneDrive de los administradores
- d) Los 1.000 sitios más grandes, cada mes

*Respuesta: b).* La evaluación predeterminada revisa cada semana los 100 sitios más usados; la primera tarda unos 4 días y las personalizadas unas 48 horas. [Fuente](https://learn.microsoft.com/en-us/purview/data-security-posture-management-oversharing) · Repasa [I3](01_Nivel_1_Inicial.md#i3)

**5. ¿Qué se necesita para usar el escaneo y la remediación a nivel de elemento en las evaluaciones de riesgo de datos?**

- a) Nada: está activo por defecto
- b) Una licencia de Agent 365
- c) Un conector de Microsoft Sentinel
- d) Una aplicación de Entra configurada por el administrador  ✅

*Respuesta: d).* MC1254556 (GA en marzo de 2026) indica que requiere una aplicación de Entra configurada por el administrador y que no está activo por defecto. [Fuente](https://mc.merill.net/message/MC1254556) · Repasa [I3](01_Nivel_1_Inicial.md#i3)

**6. Para registrar el evento «AI interaction» de Copilot en Fabric, Security Copilot o apps que no son Copilot, ¿qué se requiere?**

- a) Solo la auditoría activa
- b) Una directiva de colección con captura de contenido  ✅
- c) Restricted Content Discovery
- d) Una etiqueta de contenedor

*Respuesta: b).* Con Microsoft 365 Copilot y Copilot Chat basta la auditoría activa; con Copilot en Fabric, Security Copilot y apps que no son Copilot hace falta una directiva de colección con captura de contenido. [Fuente](https://learn.microsoft.com/en-us/purview/data-security-posture-management-considerations) · Repasa [I2](01_Nivel_1_Inicial.md#i2)

**7. En un inquilino con unidades administrativas, ¿quién puede crear políticas de un clic desde DSPM?**

- a) Cualquier administrador restringido de su unidad
- b) Solo un administrador no restringido  ✅
- c) El propietario de cada sitio
- d) Cualquier usuario con licencia de Copilot

*Respuesta: b).* Los administradores restringidos solo ven datos de sus unidades y no pueden crear políticas de un clic; eso requiere un administrador no restringido. [Fuente](https://learn.microsoft.com/en-us/purview/data-security-posture-management-considerations) · Repasa [P0](01_Nivel_1_Inicial.md#p0)

**8. ¿Cómo se factura la cobertura de orígenes que no son Microsoft 365, como Azure SQL o Fabric?**

- a) Por usuario con Microsoft 365 E5
- b) Incluida en Microsoft 365 Copilot
- c) Con pago por uso facturado en Azure  ✅
- d) Con SCU de Security Copilot

*Respuesta: c).* Los datos de Microsoft 365 se licencian por usuario; los que no son de Microsoft 365, la red y las apps y agentes de IA usan pago por uso en Azure. Las experiencias de Microsoft 365 Copilot no generan cargos de pago por uso. [Fuente](https://learn.microsoft.com/en-us/purview/purview-billing-models) · Repasa [I1](01_Nivel_1_Inicial.md#i1)

**9. ¿Qué ubicaciones Microsoft muestra por ahora Asset explorer?**

- a) Solo Microsoft 365  ✅
- b) Microsoft 365, Azure y Fabric
- c) Solo Azure
- d) Microsoft 365 y Dynamics 365

*Respuesta: a).* Por ahora la única ubicación Microsoft de Asset explorer es Microsoft 365; las ubicaciones no Microsoft dependen de socios y la integración con el data lake de Sentinel está en preview. [Fuente](https://learn.microsoft.com/en-us/purview/data-security-posture-management-learn-about) · Repasa [I1](01_Nivel_1_Inicial.md#i1)

**10. ¿Qué afirmación sobre Restricted Content Discovery es correcta?**

- a) Cambia los permisos del sitio
- b) Aplica también a OneDrive
- c) Requiere licencia de Copilot y no aplica a OneDrive  ✅
- d) Reemplaza de forma permanente la revisión de permisos

*Respuesta: c).* RCD oculta sitios de la búsqueda organizacional y de Copilot sin cambiar permisos; requiere licencia de Copilot, no aplica a OneDrive y debe usarse como control temporal. [Fuente](https://learn.microsoft.com/en-us/sharepoint/restricted-content-discovery) · Repasa [I3](01_Nivel_1_Inicial.md#i3)

**11. ¿Qué prefijo conservan las políticas creadas cuando la solución se llamaba AI Hub?**

- a) «Microsoft AI Hub»  ✅
- b) «DSPM classic»
- c) «Copilot Hub»
- d) «Purview AI»

*Respuesta: a).* Las políticas de la etapa AI Hub conservan el prefijo «Microsoft AI Hub»; conviene inventariarlas antes del retiro de la experiencia classic. [Fuente](https://techcommunity.microsoft.com/blog/microsoft-purview-blog/microsoft-purview-%E2%80%93-data-security-posture-management-dspm-for-ai/4394685) · Repasa [I2](01_Nivel_1_Inicial.md#i2)

**12. ¿Quién necesita licencia según la regla de licenciamiento de Purview?**

- a) Solo los administradores de Purview
- b) Solo los usuarios que tienen Copilot
- c) Todo usuario que se beneficia del servicio, incluidos dueños y miembros de sitios en ubicaciones compartidas  ✅
- d) Todos los usuarios del inquilino, incluidos los visitantes

*Respuesta: c).* Necesita licencia todo usuario que se beneficia del servicio, incluidos quienes tienen roles de Purview y los dueños o miembros de sitios y grupos en ubicaciones compartidas; los visitantes no. [Fuente](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description) · Repasa [P0](01_Nivel_1_Inicial.md#p0)

**13. ¿Cuál es el puntaje de aprobación del examen SC-401?**

- a) 500
- b) 600
- c) 800
- d) 700  ✅

*Respuesta: d).* La guía de estudio del SC-401, actualizada el 28 de octubre de 2026, indica un puntaje de aprobación de 700 e incluye proteger los datos que usan los servicios de IA. [Fuente](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-401) · Repasa [I0](01_Nivel_1_Inicial.md#i0)

<a id="eval-intermedio"></a>

## Nivel 2 · Intermedio · Proteger Copilot, agentes e IA de terceros

**1. ¿Quién puede beneficiarse de la DLP que bloquea prompts con tipos de información confidencial en Copilot?**

- a) Solo usuarios con Microsoft 365 E5
- b) Todos los usuarios de Microsoft Copilot y Copilot Chat, incluidos E3 y Business  ✅
- c) Solo organizaciones con pago por uso habilitado
- d) Solo organizaciones con Agent 365

*Respuesta: b).* La DLP de prompts está disponible para todos los usuarios de Microsoft Copilot y Copilot Chat; lo que exige E5 o Purview Suite es impedir que Copilot procese archivos y correos etiquetados. [Fuente](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description) · Repasa [M1](02_Nivel_2_Intermedio.md#m1)

**2. ¿Qué licenciamiento permite analizar prompts y respuestas de Copilot con Communication Compliance?**

- a) Microsoft 365 E3
- b) Microsoft 365 E5 sola
- c) Solo el pago por uso
- d) Microsoft 365 E5 o Purview Suite más Microsoft Copilot  ✅

*Respuesta: d).* La descripción del servicio marca «No» para E5 sin Copilot: hace falta E5 o Purview Suite combinada con Microsoft Copilot. [Fuente](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description) · Repasa [M1](02_Nivel_2_Intermedio.md#m1)

**3. ¿En qué modo arranca la política DLP predeterminada «Protect sensitive M365 Copilot interactions»?**

- a) Simulación  ✅
- b) Bloqueo
- c) Desactivada
- d) Bloqueo con invalidación

*Respuesta: a).* La política predeterminada detecta SIT en los prompts y arranca en modo simulación, con sugerencias de ajuste antes de activarla. [Fuente](https://learn.microsoft.com/en-us/purview/dlp-microsoft365-copilot-location-default-policy) · Repasa [M1](02_Nivel_2_Intermedio.md#m1)

**4. ¿Qué ubicaciones de retención usan hoy las interacciones de IA?**

- a) «Teams chats and Copilot interactions»
- b) Exchange y OneDrive
- c) Microsoft Copilot experiences, Enterprise AI apps y Other AI apps  ✅
- d) SharePoint y Viva Engage

*Respuesta: c).* La retención de IA se separó de Teams en tres ubicaciones: Microsoft Copilot experiences, Enterprise AI apps y Other AI apps. [Fuente](https://learn.microsoft.com/en-us/purview/retention-policies-copilot) · Repasa [M1](02_Nivel_2_Intermedio.md#m1)

**5. Con Microsoft 365 E3 más licencias de Copilot, ¿qué puedes hacer en eDiscovery con las interacciones de Copilot?**

- a) Nada: el eDiscovery de IA requiere E5
- b) Solo la búsqueda Premium
- c) Buscar, retener y exportar  ✅
- d) Solo eliminarlas

*Respuesta: c).* Con E3 + Copilot puedes buscar, retener y exportar; la búsqueda Premium de esas interacciones requiere E5 o Purview Suite + Copilot. [Fuente](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description) · Repasa [M1](02_Nivel_2_Intermedio.md#m1)

**6. ¿Qué suscripción se requiere para la AI observability de agentes y para Insider Risk Management para agentes?**

- a) Microsoft 365 E5
- b) Microsoft Purview Suite
- c) Copilot Studio
- d) Microsoft 365 E7 o Agent 365  ✅

*Respuesta: d).* MC1280556 indica que, sin Microsoft 365 E7 o Agent 365, estas capacidades no están disponibles; su GA fue de mediados de junio a fines de julio de 2026. [Fuente](https://message.cengizyilmaz.net/message/mc1280556-microsoft-purview-for-agents-ai-observability-and-insider-risk-management-now-generally-available) · Repasa [M2](02_Nivel_2_Intermedio.md#m2)

**7. Al integrar Microsoft Foundry con Purview, ¿qué queda incluido en la licencia de Purview?**

- a) Las políticas DLP
- b) La auditoría de Foundry  ✅
- c) La postura de agentes de Foundry
- d) Las políticas de Insider Risk

*Respuesta: b).* Las políticas requieren pago por uso, pero la auditoría de Foundry está incluida en la licencia de Purview; la postura de agentes requiere Agent 365. [Fuente](https://learn.microsoft.com/en-us/purview/ai-azure-foundry) · Repasa [M2](02_Nivel_2_Intermedio.md#m2)

**8. Si un archivo tiene una etiqueta que cifra, ¿qué derechos de uso necesita un agente para devolver su contenido?**

- a) VIEW y EXTRACT  ✅
- b) Solo VIEW
- c) EDIT y PRINT
- d) Solo OWNER

*Respuesta: a).* Con etiquetas que cifran, la IA necesita los derechos VIEW y EXTRACT para devolver el contenido. [Fuente](https://learn.microsoft.com/en-us/purview/ai-agent-365) · Repasa [M2](02_Nivel_2_Intermedio.md#m2)

**9. ¿Qué requisito previo exige Purview para gestionar interacciones con ChatGPT (consumo), Gemini o DeepSeek?**

- a) Ninguno
- b) Licencia de Agent 365
- c) Pago por uso habilitado  ✅
- d) Licencia de Microsoft 365 Copilot

*Respuesta: c).* La página de otras apps de IA exige de forma explícita habilitar el pago por uso; además, la mayoría de las capacidades requiere la extensión de navegador y dispositivos incorporados. [Fuente](https://learn.microsoft.com/en-us/purview/ai-other-apps) · Repasa [M3](02_Nivel_2_Intermedio.md#m3)

**10. ¿Qué licencia exige Network Data Security con Global Secure Access?**

- a) Microsoft 365 E3
- b) Microsoft 365 E7 o Purview E5 + Entra Internet Access  ✅
- c) Solo Defender for Cloud Apps
- d) Solo Agent 365

*Respuesta: b).* Con Global Secure Access se requiere E7 o Purview E5 + Entra Internet Access; con un SASE de terceros, Purview E5 + pago por uso. [Fuente](https://learn.microsoft.com/en-us/purview/dlp-network-data-security-learn) · Repasa [M3](02_Nivel_2_Intermedio.md#m3)

**11. ¿Cómo se licencia la DLP de Edge for Business para proteger datos de un dispositivo administrado hacia una app de IA no administrada?**

- a) Incluida en E3
- b) Pago por uso  ✅
- c) Incluida en Microsoft 365 Copilot
- d) Requiere Agent 365

*Respuesta: b).* Ese flujo se cobra por uso; los escenarios con apps registradas en Entra están incluidos en E5. [Fuente](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description) · Repasa [M3](02_Nivel_2_Intermedio.md#m3)

**12. ¿Qué afirmación sobre las etiquetas de confidencialidad con la IA de terceros es correcta?**

- a) Se admiten en todos los sitios de IA
- b) Solo se admiten en Edge
- c) Solo se admiten con la extensión de Chrome
- d) No se admiten  ✅

*Respuesta: d).* La página de otras apps de IA indica que las etiquetas de confidencialidad no se admiten con sitios de IA de terceros. [Fuente](https://learn.microsoft.com/en-us/purview/ai-other-apps) · Repasa [M3](02_Nivel_2_Intermedio.md#m3)

**13. ¿Qué habilita asignar al menos una licencia de Copilot en SharePoint Advanced Management?**

- a) Todas las funciones de SAM, incluida la creación restringida de sitios por apps
- b) Solo Restricted Content Discovery
- c) RAC, RCD, informes de gobierno de acceso, revisiones de acceso, sitios inactivos y propiedad  ✅
- d) Nada: SAM siempre requiere un complemento

*Respuesta: c).* Con al menos una licencia de Copilot se habilitan esas funciones; la creación restringida de sitios por apps requiere el complemento SAM Plan 1. [Fuente](https://learn.microsoft.com/en-us/sharepoint/sharepoint-advanced-management-features-copilot-license) · Repasa [M4](02_Nivel_2_Intermedio.md#m4)

**14. Según el marco de controles de Copilot, ¿qué distingue la capa fundamental de la optimizada?**

- a) Fundamental: E3 + SAM; optimizada: E5 (DSPM, autoetiquetado, Insider Risk y Defender for Cloud Apps)  ✅
- b) Fundamental: E5; optimizada: E3
- c) Ambas requieren Microsoft 365 E7
- d) Fundamental: Agent 365; optimizada: Purview Suite

*Respuesta: a).* El marco separa los controles fundamentales (E3 + SAM) de los optimizados que aporta E5. [Fuente](https://learn.microsoft.com/en-us/copilot/implement/copilot-controls-security-governance) · Repasa [M4](02_Nivel_2_Intermedio.md#m4)

<a id="eval-avanzado"></a>

## Nivel 3 · Avanzado · Agentes de IA, postura de IA, regulación y SOC

**1. ¿Cuánta capacidad de Security Copilot incluye Microsoft 365 E5?**

- a) 100 SCU fijas al mes
- b) 400 SCU al mes por cada 1.000 licencias, hasta 10.000  ✅
- c) Capacidad ilimitada
- d) 1 SCU por usuario

*Respuesta: b).* Por ejemplo, 4.000 licencias equivalen a 1.600 SCU al mes; la capacidad se calcula sobre licencias pagas. [Fuente](https://www.microsoft.com/en-us/security/security-copilot-in-microsoft-365-e5) · Repasa [A1](03_Nivel_3_Avanzado.md#a1)

**2. ¿Qué límites tiene el Data Security Posture Agent?**

- a) Una instancia por inquilino y dos prompts concurrentes  ✅
- b) Diez instancias por inquilino
- c) Una instancia por usuario y prompts ilimitados
- d) No tiene límites documentados

*Respuesta: a).* Además, escanea hasta 5 GB o 10.000 elementos, devuelve los 1.000 primeros y etiqueta hasta 10 archivos a la vez. [Fuente](https://learn.microsoft.com/en-us/purview/copilot-in-purview-posture-agent-get-started) · Repasa [A1](03_Nivel_3_Avanzado.md#a1)

**3. ¿Cómo se factura Data Security Investigations?**

- a) Incluida en Microsoft 365 E5
- b) Con licencias de Agent 365
- c) Por consumo (almacenamiento y cómputo de IA), sin licencia específica de Microsoft 365  ✅
- d) Con las SCU incluidas en E5

*Respuesta: c).* DSI se factura solo por consumo en Azure, incluidas las investigaciones proactivas creadas desde DSPM. [Fuente](https://learn.microsoft.com/en-us/purview/data-security-investigations-billing) · Repasa [A1](03_Nivel_3_Avanzado.md#a1)

**4. ¿Qué alertas de DLP clasifica el Data Security Triage Agent?**

- a) Todas, incluidas las de red
- b) Solo las de Endpoint
- c) Solo las de apps de IA de terceros
- d) Las de Exchange, Teams, OneDrive, SharePoint y Endpoint  ✅

*Respuesta: d).* El agente de triaje de DLP solo clasifica alertas de esas cinco cargas y combina licencia por usuario con consumo de SCU. [Fuente](https://learn.microsoft.com/en-us/purview/copilot-in-purview-triage-dlp-agent-get-started) · Repasa [A1](03_Nivel_3_Avanzado.md#a1)

**5. Al 6 de noviembre de 2026, ¿qué describe mejor el estado del Data Security Posture Agent?**

- a) Learn y el Message Center coinciden en que está en GA
- b) MC1318248 anunció la GA para junio y julio de 2026, pero Learn todavía dice preview  ✅
- c) Learn dice GA y el Message Center dice preview
- d) Fue retirado en octubre de 2026

*Respuesta: b).* Es una contradicción abierta: el aviso anunció la GA, pero la página de Learn actualizada el 23 de junio de 2026 sigue diciendo preview. [Fuente](https://mc.merill.net/message/MC1318248) · Repasa [A1](03_Nivel_3_Avanzado.md#a1)

**6. Desde el 1 de julio de 2026, ¿qué requiere el descubrimiento de agentes de Foundry en Defender for Cloud?**

- a) Defender CSPM
- b) Defender for AI Services
- c) Microsoft Purview Suite
- d) Microsoft Agent 365  ✅

*Respuesta: d).* Defender CSPM sigue descubriendo cuentas y proyectos de Foundry, pero el descubrimiento y la postura de los agentes pasaron a requerir Agent 365. [Fuente](https://learn.microsoft.com/en-us/azure/defender-for-cloud/ai-security-posture) · Repasa [A2](03_Nivel_3_Avanzado.md#a2)

**7. ¿Qué tecnología usa Defender for AI Services para alertar sobre jailbreak, fuga de datos o robo de credenciales?**

- a) Prompt Shields  ✅
- b) Customer Key
- c) Restricted Content Discovery
- d) Directivas de colección

*Respuesta: a).* La protección contra amenazas de IA usa Prompt Shields y envía sus alertas a Defender XDR. [Fuente](https://learn.microsoft.com/en-us/azure/defender-for-cloud/ai-threat-protection) · Repasa [A2](03_Nivel_3_Avanzado.md#a2)

**8. ¿Qué admite la protección contra inyección de prompts del AI Gateway de Entra Internet Access?**

- a) Texto, imágenes y audio
- b) Solo texto, hasta 64.000 caracteres por prompt  ✅
- c) Cualquier formato y sin límite
- d) Solo archivos PDF

*Respuesta: b).* Requiere licencia de Entra Internet Access y admite solo texto, hasta 64.000 caracteres por prompt. [Fuente](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-ai-prompt-injection-protection) · Repasa [A2](03_Nivel_3_Avanzado.md#a2)

**9. ¿Cuántas plantillas premium de Compliance Manager puede usar sin costo una organización con Microsoft 365 E5?**

- a) Una
- b) Cinco
- c) Tres  ✅
- d) Ilimitadas

*Respuesta: c).* E5 permite usar tres plantillas premium sin costo, entre ellas las de IA como EU AI Act, ISO/IEC 42001, ISO/IEC 23894 y NIST AI RMF. [Fuente](https://learn.microsoft.com/en-us/purview/compliance-manager-regulations-list) · Repasa [A3](03_Nivel_3_Avanzado.md#a3)

**10. ¿Qué cambió en Defender XDR a inicios de octubre de 2026 con las señales de DLP?**

- a) Las alertas de DLP dejaron de llegar a Defender XDR por diseño
- b) Las alertas de DLP pasaron a llegar solo a Sentinel
- c) Se retiró la cola unificada de incidentes
- d) Una regla de ajuste integrada convierte señales de DLP en comportamientos (BehaviorInfo)  ✅

*Respuesta: d).* La regla de ajuste integrada convierte señales en comportamientos; si el SOC deja de ver alertas de DLP, es lo primero que hay que revisar. [Fuente](https://learn.microsoft.com/en-us/defender-xdr/dlp-investigate-alerts-defender) · Repasa [A4](03_Nivel_3_Avanzado.md#a4)

**11. ¿Cómo se crean las políticas DLP para apps registradas en Entra que usan las APIs de Purview?**

- a) Desde la ubicación Microsoft Copilot del portal
- b) Con PowerShell (New-DlpComplianceRule)  ✅
- c) Con la API processContent
- d) Desde Defender XDR

*Respuesta: b).* El tutorial de las APIs de Purview indica que esas políticas se crean con PowerShell, no desde el portal. [Fuente](https://learn.microsoft.com/en-us/purview/developer/use-the-api) · Repasa [A4](03_Nivel_3_Avanzado.md#a4)

**12. ¿Qué pasa con la seudonimización al exportar alertas de Insider Risk por la Office 365 Management Activity API?**

- a) Se conserva siempre
- b) Solo se conserva en Sentinel
- c) No se conserva  ✅
- d) La exportación por API no está disponible

*Respuesta: c).* La exportación por API no conserva la seudonimización, así que hay que acordar con privacidad quién ve esos datos en el SIEM. [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-share-data) · Repasa [A4](03_Nivel_3_Avanzado.md#a4)

**13. ¿Qué cubre la integración nativa de Foundry con Purview frente a las APIs de Purview?**

- a) La integración nativa no cubre DLP ni sobreexposición; las APIs sí  ✅
- b) La integración nativa cubre DLP y sobreexposición; las APIs no
- c) Ninguna cubre la auditoría
- d) Ambas requieren Agent 365 para cualquier función

*Respuesta: a).* Según la guía para desarrolladores, la integración nativa de Foundry no cubre DLP ni sobreexposición; las APIs de Purview en Graph sí. [Fuente](https://learn.microsoft.com/en-us/purview/developer/secure-ai-with-purview) · Repasa [A4](03_Nivel_3_Avanzado.md#a4)

<a id="eval-operacion"></a>

## Nivel 4 · Operación · Modelo operativo, métricas y gobierno

**1. ¿Qué propone el modelo de despliegue oficial de DSPM?**

- a) Cuatro pasos y un ciclo mensual de revisión de recomendaciones  ✅
- b) Dos pasos y una revisión anual
- c) Seis pasos y una revisión semanal obligatoria
- d) Un único paso de activación sin ciclo de revisión

*Respuesta: a).* El modelo tiene cuatro pasos (fundamentos, acceso y analítica, entender los riesgos, y actuar e investigar con Security Copilot) y un ciclo mensual de revisión. [Fuente](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-dspm-intro) · Repasa [O1](04_Nivel_4_Operacion.md#o1)

**2. ¿Cómo se tratan las acciones de los agentes en DSPM?**

- a) Se ejecutan sin registro para no generar ruido
- b) Solo se auditan si fallan
- c) Se revisan, aprueban y siempre se auditan  ✅
- d) Solo se registran con Microsoft 365 E7

*Respuesta: c).* La IA de DSPM actúa bajo supervisión: las acciones de los agentes se revisan, aprueban y siempre se auditan. [Fuente](https://learn.microsoft.com/en-us/purview/data-security-posture-management-learn-about) · Repasa [O1](04_Nivel_4_Operacion.md#o1)

**3. ¿Qué ofrece FastTrack para Agent 365?**

- a) Licencias gratuitas de Agent 365
- b) Asistencia remota para inventario de agentes, identidad, controles base en Entra, Defender y Purview, y flujos de monitoreo y respuesta  ✅
- c) Asesoría legal sobre normativa de IA
- d) Soporte de producción 24×7 para incidentes

*Respuesta: b).* FastTrack ofrece asistencia remota para planificar la adopción de Agent 365; no reemplaza la asesoría legal ni el soporte de incidentes. [Fuente](https://learn.microsoft.com/en-us/microsoft-365/fasttrack/microsoft-agent-365) · Repasa [O1](04_Nivel_4_Operacion.md#o1)

**4. Según el Data Security Index 2026, ¿qué porcentaje de los incidentes de datos involucra IA generativa?**

- a) 12 %
- b) 47 %
- c) 80 %
- d) 32 %  ✅

*Respuesta: d).* El 32 % de los incidentes involucra IA generativa y solo el 47 % de las organizaciones aplica controles específicos de IA; la muestra representa a Latinoamérica solo con Brasil. [Fuente](https://www.microsoft.com/en-us/security/blog/2026/01/29/new-microsoft-data-security-index-report-explores-secure-ai-adoption-to-protect-sensitive-data/) · Repasa [O2](04_Nivel_4_Operacion.md#o2)

**5. ¿Qué período cubre la tendencia de la página Posture de DSPM?**

- a) 7 días
- b) 30 días  ✅
- c) 90 días
- d) 1 año

*Respuesta: b).* La página Posture muestra métricas clave, objetivos priorizados por riesgo y una tendencia de 30 días. [Fuente](https://learn.microsoft.com/en-us/purview/data-security-posture-management-learn-about) · Repasa [O2](04_Nivel_4_Operacion.md#o2)

**6. ¿Qué muestra el Usage center de Purview y en qué estado está?**

- a) El consumo de pago por uso por función y los usuarios en alcance sin licencia; está en preview  ✅
- b) Solo las SCU de Security Copilot; está en GA
- c) La puntuación de Secure Score; fue retirado
- d) El inventario de agentes; requiere Agent 365

*Respuesta: a).* El Usage center, en preview, muestra el consumo de pago por uso por función y detecta usuarios en alcance sin licencia. [Fuente](https://learn.microsoft.com/en-us/purview/purview-billing-usage) · Repasa [O2](04_Nivel_4_Operacion.md#o2)

**7. Al eliminar prompts y respuestas con eDiscovery y Graph Explorer, ¿cuál es el límite por ejecución?**

- a) 100 elementos por buzón
- b) 10 elementos por buzón  ✅
- c) 1.000 elementos por buzón
- d) Sin límite

*Respuesta: b).* Se eliminan como máximo 10 elementos por buzón por ejecución: es una herramienta de respuesta a solicitudes y derrames, no de limpieza masiva. [Fuente](https://learn.microsoft.com/en-us/purview/edisc-search-copilot-data) · Repasa [O3](04_Nivel_4_Operacion.md#o3)

**8. ¿Qué permisos se necesitan para buscar y para eliminar interacciones de IA?**

- a) Global Administrator para ambas tareas
- b) AI Content Viewer para ambas tareas
- c) Compliance Administrator para buscar y Data Security AI Viewer para eliminar
- d) El grupo eDiscovery Manager para buscar y el rol Search And Purge para eliminar  ✅

*Respuesta: d).* Buscar requiere el grupo de roles eDiscovery Manager y eliminar requiere el rol Search And Purge. [Fuente](https://learn.microsoft.com/en-us/purview/edisc-search-copilot-data) · Repasa [O3](04_Nivel_4_Operacion.md#o3)

**9. ¿Cuándo se publicó el D.S. 115-2025-PCM, Reglamento de la Ley 31814 de IA del Perú?**

- a) 21 de agosto de 2024
- b) 9 de septiembre de 2025  ✅
- c) 22 de enero de 2026
- d) 1 de diciembre de 2026

*Respuesta: b).* Se publicó el 9 de septiembre de 2025; según el resumen de Cuatrecasas, entró en vigor el 22 de enero de 2026. [Fuente](https://www.gob.pe/institucion/pcm/normas-legales/7133522-115-2025-pcm) · Repasa [O3](04_Nivel_4_Operacion.md#o3)

**10. ¿Qué hace la Circular Externa 002 de 2024 de la SIC de Colombia?**

- a) Aplica la Ley 1581 de 2012 al desarrollo, despliegue y uso de sistemas de IA  ✅
- b) Regula la ciberseguridad de los bancos
- c) Crea una autoridad nacional de IA
- d) Fija la retención de los correos electrónicos

*Respuesta: a).* La circular aplica el régimen de datos personales a la IA y exige responsabilidad demostrada y privacidad desde el diseño. [Fuente](https://normograma.mintic.gov.co/mintic/compilacion/docs/circular_superindustria_0002_2024.htm) · Repasa [O3](04_Nivel_4_Operacion.md#o3)

**11. ¿Qué soluciones de Purview seudonimizan a los usuarios por defecto en el contexto de IA?**

- a) DLP y Audit
- b) eDiscovery y retención
- c) Insider Risk para agentes y Communication Compliance  ✅
- d) Restricted Content Discovery

*Respuesta: c).* Insider Risk para agentes y Communication Compliance seudonimizan por defecto y se apoyan en RBAC y auditoría. [Fuente](https://message.cengizyilmaz.net/message/mc1280556-microsoft-purview-for-agents-ai-observability-and-insider-risk-management-now-generally-available) · Repasa [O3](04_Nivel_4_Operacion.md#o3)

**12. Al eliminar interacciones de IA de un buzón sujeto a retención, ¿qué debes hacer?**

- a) Nada especial
- b) Eliminar el buzón completo
- c) Retirar y luego reaplicar las retenciones y los holds  ✅
- d) Desactivar la auditoría del inquilino

*Respuesta: c).* El procedimiento oficial pide retirar las retenciones y los holds, eliminar los elementos y luego reaplicarlos. [Fuente](https://learn.microsoft.com/en-us/purview/edisc-search-copilot-data) · Repasa [O3](04_Nivel_4_Operacion.md#o3)

**13. ¿Qué compromiso de privacidad documenta Microsoft para Copilot?**

- a) Usa los prompts para entrenar los modelos fundacionales
- b) Solo procesa datos en Estados Unidos
- c) Requiere consentimiento individual para cada prompt
- d) No usa los prompts ni los datos de Graph para entrenar modelos fundacionales  ✅

*Respuesta: d).* Copilot no usa los prompts ni los datos de Graph para entrenar modelos fundacionales; Anthropic y OpenAI figuran como subprocesadores. [Fuente](https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-privacy) · Repasa [O3](04_Nivel_4_Operacion.md#o3)

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. No constituye asesoría legal ni laboral: las decisiones sobre privacidad, captura de contenido, monitoreo y normativa corresponden a tus áreas de Legal, RR. HH. y privacidad. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

# Programa: cómo usar, justificación, rutas y plan

*Microsoft Purview Communication Compliance e Information Barriers Ninja Training · Edición 2026*

[Índice del programa](README.md) · [Nivel 1 · Inicial →](01_Nivel_1_Inicial.md)

<a id="como-usar"></a>

## Cómo usar esta guía

¿Quieres convertirte en Ninja de Communication Compliance e Information Barriers? Esta guía reúne, ordenados como un curso, los mejores recursos públicos para detectar, revisar y remediar comunicaciones de riesgo en correo, Teams, Viva Engage, Microsoft 365 Copilot y otras apps de IA, y para impedir que grupos que no deben comunicarse colaboren en Teams, SharePoint y OneDrive. Documentación de Microsoft Learn, anuncios oficiales, avisos del Message Center, el Ninja oficial de 2022 y el trabajo de MVPs y empleados de Microsoft, todo verificado al 6 de noviembre de 2026.

Está pensada para equipos que operan estas capacidades por razones distintas: cumplimiento y conducta, supervisión regulada (por ejemplo, en el sector financiero), RR. HH., Legal, privacidad y los administradores de colaboración que mantienen las barreras de información. Puedes seguirla completa o por rol. Cada nivel cierra con una evaluación y un reto; con 80 % o más generas tu certificado de finalización, como en el Ninja original. Y una regla atraviesa todo el recorrido: supervisar a personas reales exige aprobación previa y políticas de prueba con alcance acotado.

**Estructura.** Tres niveles técnicos —Inicial (L100–L200), Intermedio (L300) y Avanzado (L400)—, un track de operación (L300–L400) para el modelo operativo, las métricas y el gobierno, y una sección transversal de comunidad. El nivel inicial cubre Communication Compliance de punta a punta; el intermedio suma la IA, Information Barriers, la privacidad y la integración con Insider Risk y eDiscovery; el avanzado, la evidencia, los conectores y la supervisión regulada.

**Cada módulo** sigue la forma Ninja: una introducción con el porqué, la justificación de negocio (*Por qué importa*), lo que vas a lograr, novedades y advertencias con fecha y fuente, una ruta rápida (*¿Tienes poco tiempo?*), los recursos agrupados por tipo, la práctica guiada (*Manos a la obra*) y lecturas para profundizar.

**Evaluación y certificado.** Los niveles Inicial, Intermedio y Avanzado y el track de operación cierran con una evaluación de opción múltiple, con la explicación y la fuente de cada respuesta, y con un reto integrador. Con 80 % o más puedes generar el certificado de finalización. Es una autoevaluación de esta guía, no una certificación de Microsoft: para eso están la credencial Applied Skills de retención, eDiscovery y Communication Compliance y el knowledge check del Ninja oficial.

**Laboratorio.** Cada ejercicio indica dónde se puede hacer: [LAB] completo en una prueba de Microsoft 365 E5 o un sandbox, con una suscripción de Azure con el crédito de Visual Studio Enterprise; [LAB-PARCIAL] con las limitaciones que se explican; [SOLO-PRODUCCION] cuando requiere licencias pagas, conectores contratados o personas reales, siempre con una forma segura de practicar: aprobación previa, cuentas de prueba, alcance mínimo, seudonimización y reversión. La matriz de laboratorio y el anexo del entorno de práctica lo detallan.

**Fechas y estados.** Cada dato lleva fuente y fecha. Microsoft Ignite se realiza del 17 al 20 de noviembre de 2026 y puede cambiar estados de vista previa: verifica la página de novedades de Purview. Las versiones en español de Learn suelen ir detrás de las de inglés; ante diferencias, prevalece la documentación en inglés vigente. Esta guía no es asesoría legal ni laboral.

**Leyenda de etiquetas**

| Etiqueta | Significado |
|---|---|
| Microsoft oficial | Documentación, blogs y videos publicados por Microsoft. |
| Empleado de Microsoft | Material de ingenieros, gerentes de producto o arquitectos de Microsoft en canales propios o comunitarios. |
| MVP de Microsoft | Material de Most Valuable Professionals, con estado verificado en fuentes públicas. |
| Comunidad o partner | Autores de la comunidad o de partners; útil, pero contrástalo con la documentación oficial. |
| Vista previa | Funcionalidad en preview: puede cambiar y no siempre tiene soporte de producción. |
| Legado aún útil | Recurso anterior a los cambios de 2025–2026 que sigue explicando bien el concepto; lee la nota de qué cambió. |
| Ninja original | Recurso que formaba parte del Ninja oficial del producto. |
| Nuevo | Recurso publicado o actualizado desde mayo de 2026. |
| ES | Recurso disponible en español. |
| Laboratorio | Ejercicio que puedes hacer completo en el entorno de práctica (prueba de Microsoft 365 E5 o sandbox y suscripción de Azure). |
| Laboratorio parcial | Ejercicio posible en el entorno de práctica con limitaciones que se indican. |
| Solo producción | Requiere licencias pagas, datos o usuarios reales, o varios inquilinos: síguelo con la estrategia de práctica segura en producción. |

<a id="por-que"></a>

## Por qué este programa

**Por qué ahora.** Communication Compliance cambió más desde 2024 que en sus primeros años: el portal de cumplimiento clásico se retiró entre noviembre y diciembre de 2024; Microsoft 365 Copilot y otras apps de IA se convirtieron en canales supervisables, varias con pago por uso; llegaron los clasificadores de seguridad de contenido basados en modelos de lenguaje y la conservación configurable de coincidencias (junio de 2025); y en 2026 se sumaron Claude Enterprise y el reporte de cumplimiento de Information Barriers. Además, `Search-UnifiedAuditLog`, del que depende hoy la evidencia de auditoría de CC, se retira el 15 de octubre de 2027. Un equipo formado con el Ninja de 2022 no conoce nada de esto.

**Qué gana la organización.** Supervisión defendible y proporcional, con resultados medibles: antigüedad de los pendientes de revisión, tasa de falsos positivos por clasificador e idioma, porcentaje de políticas con aprobación documentada de Legal, RR. HH. y privacidad, almacenamiento por política frente a los avisos de 80, 90 y 95 %, costo de pago por uso por política de IA, evidencia de auditoría exportada cada mes y reportes de Information Barriers sin sitios incompatibles. Cada nivel deja entregables reutilizables: matriz de licencias, políticas piloto, procedimiento de revisión, segmentos de prueba, scripts de evidencia y un expediente de gobierno.

**Para quién.** Administradores de Communication Compliance, revisores e investigadores, oficiales de cumplimiento y supervisores de industrias reguladas, RR. HH., Legal, oficiales de privacidad y administradores de colaboración que operan Information Barriers. Las rutas por rol permiten que cada perfil recorra solo lo que necesita.

**Cómo se conecta con el resto de la serie.** Es uno de los ocho programas de Purview, porque cada capacidad la operan equipos distintos por razones distintas. Las señales de riesgo y los casos se profundizan en el programa de **Insider Risk Management**; el escalamiento a investigación, los casos y la auditoría, en **eDiscovery y Audit**; las políticas de un clic para IA, en **DSPM y seguridad de datos para IA**; la retención regulatoria, en **Data Lifecycle y Records Management**; los tipos de información confidencial y los clasificadores, en **Information Protection**; el ajuste de falsos positivos, en **DLP**; y los marcos regulatorios, en **Compliance Manager**. Fuera de Purview, **Entra** aporta identidades, PIM y unidades administrativas; **Sentinel** y **Defender XDR**, el análisis de los eventos de auditoría; y **Security Copilot**, los resúmenes de coincidencias.

<a id="licencias"></a>

## Licencias: Microsoft 365 E3, E5, Purview Suite, E7, Agent 365 y pago por uso

Communication Compliance no está incluido en Microsoft 365 E3. Se obtiene con Microsoft 365 E5/A5/G5, con Microsoft Purview Suite (el nombre de Microsoft 365 E5 Compliance desde el 1 de octubre de 2025), con el complemento Microsoft 365 E5 Insider Risk Management o con Office 365 E5, y cada usuario que se beneficia del servicio necesita licencia, incluidos quienes tienen roles de Purview. Encima de esa base, Microsoft 365 Copilot exige su propia licencia y la IA que no es de Microsoft 365 se factura por pago por uso. Microsoft 365 E7 (GA el 1 de mayo de 2026) reúne E5, Microsoft 365 Copilot, Entra Suite y Agent 365.

Usa esta tabla para conversar con tu equipo de licenciamiento, no como cotización: las descripciones de servicio cambian y algunos puntos (Information Barriers, agentes y apps conectadas a Entra) no están del todo claros en las fuentes revisadas.

**Qué incluye cada licencia para Communication Compliance e Information Barriers**

| Capacidad | Microsoft 365 E3 | Microsoft 365 E5 / Purview Suite | Complemento o pago por uso | Fuente |
|---|---|---|---|---|
| Communication Compliance en Exchange, Teams y Viva Engage: plantillas, clasificadores integrados, OCR, revisión y remediación | No incluido (no figura en la descripción de servicio) | Incluido; también en A5/G5, Office 365 E5 y Purview Suite EDU, GOV y FLW | Complemento Microsoft 365 E5 Insider Risk Management o Purview Suite sobre E3; licencia para cada usuario que se beneficia | [Descripción de servicio](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description) |
| Prompts y respuestas de Microsoft 365 Copilot y Copilot Chat | No incluido | Solo con licencia de Microsoft 365 Copilot («E5 + Copilot» o «Purview Suite + Copilot»); no con el complemento IRM ni con Office 365 E5. Microsoft 365 E7 reúne E5 y Copilot | Sin cargos de pago por uso | [Descripción de servicio](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description) · [Canales](https://learn.microsoft.com/en-us/purview/communication-compliance-channels) · [E7 y Agent 365](https://techcommunity.microsoft.com/blog/microsoft_365blog/microsoft-365-e7-and-agent-365-are-now-generally-available/4516295) |
| Copilot Studio, Copilot en Fabric y Security Copilot | No incluido | Requiere además pago por uso; en Security Copilot hay que habilitar el permiso para que Purview procese los datos | Pago por uso: registros de texto de 1.000 caracteres, medidor estándar o premium | [Canales](https://learn.microsoft.com/en-us/purview/communication-compliance-channels) · [Security Copilot](https://learn.microsoft.com/en-us/purview/ai-security-copilot) |
| Apps de IA empresariales (ChatGPT Enterprise; Claude Enterprise por conector) y otras apps de IA detectadas por navegador o red | No incluido | Requiere además pago por uso; el conector de Claude está en vista previa | Pago por uso (registros de texto) | [Canales](https://learn.microsoft.com/en-us/purview/communication-compliance-channels) · [Claude Enterprise](https://learn.microsoft.com/en-us/purview/ai-claude-enterprise) |
| Agentes de Microsoft Foundry y apps de IA conectadas a Entra | No incluido | E5 o Purview Suite no alcanzan: la descripción de servicio indica soporte con Microsoft 365 E7 y Agent 365 | Microsoft 365 E7 o Agent 365 (también se vende por separado); confirma si además aplica pago por uso | [Descripción de servicio](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description) · [E7 y Agent 365](https://techcommunity.microsoft.com/blog/microsoft_365blog/microsoft-365-e7-and-agent-365-are-now-generally-available/4516295) |
| Clasificadores premium (odio, autolesión, violencia, sexual, Prompt Shields y material protegido) | No incluido | Incluidos sobre canales de Microsoft 365 y Copilot | Medidor premium de pago por uso sobre IA que no es de Microsoft 365; si un mensaje se evalúa con ambos medidores, se cobra solo el premium | [Modelos de facturación](https://learn.microsoft.com/en-us/purview/purview-billing-models) |
| Política de mensajes notificados por usuarios | No incluido | Incluida; puede tardar hasta 30 días en estar disponible tras la compra (Teams activado por defecto; Viva Engage en vista previa) | — | [Políticas](https://learn.microsoft.com/en-us/purview/communication-compliance-policies) |
| Conectores de datos de terceros | No incluido | Licencia para cada usuario beneficiado: E5, E5 IP&G, Purview Suite, E5 IRM, E5 eDiscovery and Audit u Office 365 E5 | Conectores de partners: relación comercial con el partner (TeleMessage, 17a-4, CellTrust) | [Descripción de servicio](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description) · [Conectores](https://learn.microsoft.com/en-us/purview/archive-third-party-data) |
| Escalar para investigación (caso de eDiscovery Premium) | No incluido | Incluido: el custodio necesita E5, o E1/E3 con Purview Suite o con el complemento eDiscovery and Audit | Complemento E5 eDiscovery and Audit | [Permisos de eDiscovery](https://learn.microsoft.com/en-us/purview/edisc-permissions) · [Investigar y remediar](https://learn.microsoft.com/en-us/purview/communication-compliance-investigate-remediate) |
| Integración con Insider Risk Management (Insider risk trigger e indicadores de CC) | No incluido | Incluida con E5 o Purview Suite | Complemento E5 Insider Risk Management; algunos indicadores de IRM requieren pago por uso | [Descripción de servicio](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description) · [Indicadores de IRM](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-policy-indicators) |
| Information Barriers | No lo asumas incluido: la sección revisada no enumera SKU | Requiere licencia para los usuarios de los segmentos asignados («Assigned Segments») en políticas de bloqueo o de permiso; la sección no enumera SKU | Confírmalo con tu equipo de licenciamiento antes de diseñar | [Descripción de servicio](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description) |
| Resúmenes de Security Copilot sobre coincidencias de CC | No incluido | Security Copilot incluido en Microsoft 365 E5 y E7: 400 SCU al mes por cada 1.000 licencias pagas, hasta 10.000 (despliegue desde el 18 de noviembre de 2025) | Capacidad adicional según el contrato de Security Copilot | [Inclusión en E5](https://learn.microsoft.com/en-us/copilot/security/security-copilot-inclusion) · [Security Copilot en Purview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-overview) |
| Auditoría para la evidencia de supervisión | Audit (Standard): 180 días de retención | Audit (Premium): hasta 1 año | Complemento de retención de 10 años por usuario | [Soluciones de auditoría](https://learn.microsoft.com/en-us/purview/audit-solutions-overview) |
| Power Automate con alertas de CC | No (requiere CC) | La plantilla por defecto no requiere licencias adicionales de Power Automate | Funciones premium o el conector de Purview pueden requerir licencias de Power Automate | [Power Automate](https://learn.microsoft.com/en-us/purview/communication-compliance-power-automate) |

Fuentes: [descripción de servicio de Microsoft Purview](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description), [modelos de facturación](https://learn.microsoft.com/en-us/purview/purview-billing-models), [canales](https://learn.microsoft.com/en-us/purview/communication-compliance-channels), [precios de seguridad](https://www.microsoft.com/en-us/security/pricing-overview) y [E7 y Agent 365](https://techcommunity.microsoft.com/blog/microsoft_365blog/microsoft-365-e7-and-agent-365-are-now-generally-available/4516295). Verificado al 6 de noviembre de 2026.

<a id="plantillas-canales"></a>

## Plantillas, clasificadores, canales e Information Barriers

La referencia rápida de qué detecta cada plantilla y clasificador, en qué canales funciona, cómo se licencia y en qué estado está. Fíjate en la columna de estado: varios clasificadores clave para el sector financiero solo funcionan en inglés, y los clasificadores LLM no evalúan adjuntos, OCR ni transcripciones.

**Plantillas, clasificadores, canales e Information Barriers (noviembre de 2026)**

| Elemento | Qué hace | Canales o apps cubiertos | Licenciamiento | Estado y fecha | Fuente |
|---|---|---|---|---|---|
| Plantilla: conflicto de intereses | Detecta comunicaciones entre grupos o personas que no deberían comunicarse; revisión del 100 % y sin condiciones | Exchange, Teams, Viva Engage | Incluida en E5/A5/G5, Purview Suite, E5 IRM y Office 365 E5 | GA | [Políticas](https://learn.microsoft.com/en-us/purview/communication-compliance-policies) |
| Plantilla: interacciones de Copilot | Aplica Prompt Shields a los prompts y Protected material a las respuestas | Microsoft 365 Copilot y Copilot Chat | E5 o Purview Suite + Microsoft 365 Copilot; sin pago por uso | GA | [Políticas](https://learn.microsoft.com/en-us/purview/communication-compliance-policies) |
| Plantilla: contenido inapropiado | Clasificadores LLM Hate, Violence, Sexual y Self-harm con nivel de severidad | Teams, Viva Engage | Incluida; medidor premium de pago por uso si se aplica a IA que no es de Microsoft 365 | GA | [Políticas](https://learn.microsoft.com/en-us/purview/communication-compliance-policies) |
| Plantilla: imágenes inapropiadas | Clasificadores de imagen Adult y Racy (sobre la imagen o su OCR) | Exchange, Teams | Incluida | GA | [Políticas](https://learn.microsoft.com/en-us/purview/communication-compliance-policies) |
| Plantilla: texto inapropiado | Threat, Discrimination y Targeted harassment | Exchange, Teams, Viva Engage | Incluida | GA; el nombre «Targeted harassment» no coincide con la tabla de definiciones | [Políticas](https://learn.microsoft.com/en-us/purview/communication-compliance-policies) |
| Plantilla: cumplimiento normativo financiero | Seis clasificadores financieros; revisión del 10 % | Exchange, Teams, Viva Engage y conectores | Incluida | GA; clasificadores solo en inglés | [Políticas](https://learn.microsoft.com/en-us/purview/communication-compliance-policies) |
| Plantilla: información confidencial | SIT, diccionario personalizado y adjuntos de más de 1 MB; revisión del 10 % | Exchange, Teams, Viva Engage | Incluida | GA | [Políticas](https://learn.microsoft.com/en-us/purview/communication-compliance-policies) |
| Política de mensajes notificados por usuarios | Las personas reportan mensajes, que se evalúan con clasificadores de Azure AI Content Safety | Teams (activada por defecto) y Viva Engage | Incluida; hasta 30 días para estar disponible tras la compra | Teams GA; Viva Engage en vista previa | [Políticas](https://learn.microsoft.com/en-us/purview/communication-compliance-policies) |
| Clasificadores Threat, Harassment y Profanity | Amenazas, acoso por rasgos protegidos y lenguaje soez | Texto e imágenes (OCR) en los canales de CC | Incluidos | GA; 12 idiomas, incluido el español (definiciones del 16 de octubre de 2026) | [Definiciones](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions) |
| Clasificador Discrimination | Lenguaje discriminatorio explícito | Texto | Incluido | GA; solo inglés | [Definiciones](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions) |
| Clasificador Regulatory collusion | Colusión o elusión antimonopolio y ocultamiento (Sherman Act, leyes de valores) | Texto e imágenes | Incluido | GA; solo inglés; genera ruido con boletines (usa Filter email blasts) | [Definiciones](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions) |
| Stock manipulation, Money laundering, Gifts & entertainment, Customer complaints y Unauthorized disclosure | Riesgos de conducta financiera asociados a FINRA, SEC, BSA y FCPA | Texto; Customer complaints solo en .msg y .eml dentro de CC | Incluidos | GA; solo inglés (mínimo 6 palabras) | [Definiciones](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions) |
| Corporate sabotage | Daño o destrucción de activos | Texto | Incluido | Figura en las definiciones; no aparece en plantillas | [Definiciones](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions) |
| Hate, Sexual, Violence y Self-harm (LLM) | Severidad de 0 a 7; alerta desde 4 | Copilot, Teams y Viva Engage (sin adjuntos, OCR ni transcripciones) | Incluidos; medidor premium para IA que no es de Microsoft 365 | Disponibles; hasta 10.000 caracteres por mensaje | [Políticas](https://learn.microsoft.com/en-us/purview/communication-compliance-policies) |
| Prompt Shields | Detecta jailbreak o inyección de prompts | Solo prompts de IA | Incluido con Copilot; premium de pago por uso para otras IA | GA (anunciado en Ignite 2024); solo inglés | [Definiciones](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions) |
| Protected material | Detecta texto protegido por derechos de autor o de marca | Solo respuestas de IA | Incluido con Copilot; premium de pago por uso para otras IA | GA; solo inglés | [Definiciones](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions) |
| Canal Exchange Online | Correo y adjuntos | Buzones de Exchange Online | Incluido | GA | [Canales](https://learn.microsoft.com/en-us/purview/communication-compliance-channels) |
| Canal Microsoft Teams | Chats, canales públicos, privados y compartidos, adjuntos modernos y transcripciones | Teams (usuarios híbridos mediante un grupo de distribución) | Incluido | GA; canales públicos con ámbito estático de hasta 250 usuarios | [Canales](https://learn.microsoft.com/en-us/purview/communication-compliance-channels) |
| Canal Viva Engage | Mensajes privados, conversaciones públicas y adjuntos | Viva Engage en modo nativo | Incluido | GA | [Canales](https://learn.microsoft.com/en-us/purview/communication-compliance-channels) |
| Canal Microsoft 365 Copilot | Prompts y respuestas (clase de elemento IPM.SkypeTeams.Message.Copilot.*) | Copilot en Teams, Outlook, Word y otras apps | E5 o Purview Suite + Copilot; sin pago por uso | GA | [IA generativa](https://learn.microsoft.com/en-us/purview/communication-compliance-copilot) |
| Canal Copilot Studio, Fabric y Security Copilot | Prompts y respuestas de Copilots que no son de Microsoft 365 | Copilot Studio, Copilot en Fabric, Security Copilot | Pago por uso (registros de texto) | Disponible según la documentación actual (vista previa en Ignite 2024) | [Canales](https://learn.microsoft.com/en-us/purview/communication-compliance-channels) |
| Canal de apps de IA empresariales | IA registrada en Entra o conectada (ChatGPT Enterprise, Claude Enterprise) | Conectores de Entra, Data Map y de terceros | Pago por uso; el conector de Claude está en vista previa | Claude con CC desde agosto de 2026 | [Claude Enterprise](https://learn.microsoft.com/en-us/purview/ai-claude-enterprise) |
| Canal de otras apps de IA | IA detectada por navegador o red (catálogo de IA generativa de Defender for Cloud Apps) | Navegador, red y dispositivos incorporados | Pago por uso | Disponible | [Canales](https://learn.microsoft.com/en-us/purview/communication-compliance-channels) |
| Conectores de terceros | Importan chats y mensajes a buzones para aplicar CC | Instant Bloomberg, Bloomberg Message, ICE Chat, LinkedIn y partners (TeleMessage, 17a-4, CellTrust) | Licencia de conectores por usuario + contrato con el partner | GA; Veritas retirado el 30 de junio de 2024 | [Conectores](https://learn.microsoft.com/en-us/purview/archive-third-party-data) |
| Information Barriers en Teams | Bloquea búsqueda, chat, llamadas, reuniones, pantalla compartida y archivos entre segmentos | Teams | Licencia para los usuarios de segmentos asignados | GA | [Information Barriers](https://learn.microsoft.com/en-us/purview/information-barriers) |
| Information Barriers en SharePoint y OneDrive | Modos Open, Owner Moderated, Implicit y Explicit que restringen acceso, uso compartido y membresía | SharePoint, OneDrive | Igual que en Teams | GA | [SharePoint](https://learn.microsoft.com/en-us/purview/information-barriers-sharepoint) |
| Information Barriers en Planner | Filtra el selector de personas al compartir planes o asignar tareas | Solo planes básicos (web y Teams) | Igual que en Teams | GA | [Information Barriers](https://learn.microsoft.com/en-us/purview/information-barriers) |
| Information Barriers y Exchange | No restringe el correo; las libretas de direcciones dependen del modo (Legacy o segmentos) | Libreta de direcciones de Exchange | — | Sin soporte para correo: usa reglas de flujo de correo | [Information Barriers](https://learn.microsoft.com/en-us/purview/information-barriers) |
| Modos de IB: Legacy, segmento único y multisegmento | Multisegmento: hasta 10 segmentos por usuario y 5.000 en total; Legacy: uno por usuario y hasta 250 | Teams, SharePoint, OneDrive | — | GA | [Multisegmento](https://learn.microsoft.com/en-us/purview/information-barriers-multi-segment) |
| Reporte de cumplimiento de IB | Detecta sitios, OneDrive y contenedores de SharePoint Embedded incompatibles después de cambiar políticas | SharePoint, OneDrive, SharePoint Embedded | — | Nuevo en septiembre de 2026 | [Reporte](https://learn.microsoft.com/en-us/purview/information-barriers-sharepoint-report) |

Fuentes: [políticas](https://learn.microsoft.com/en-us/purview/communication-compliance-policies), [definiciones de clasificadores](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions), [canales](https://learn.microsoft.com/en-us/purview/communication-compliance-channels), [Information Barriers](https://learn.microsoft.com/en-us/purview/information-barriers). Verificado al 6 de noviembre de 2026.

<a id="gobierno-privacidad"></a>

## Gobierno y privacidad de la supervisión

Supervisar comunicaciones de personas reales es una decisión de la organización, no del administrador. Microsoft deja la responsabilidad legal de monitorear, bloquear o retener contenido en el cliente y recomienda consultar asesoría legal antes de desplegar clasificadores. Esta tabla no interpreta ninguna ley: lista las decisiones y controles que tu programa debería documentar, quién debería aprobarlos y qué evidencia conservar.

Regla de oro de esta guía: ninguna política sobre personas reales sin aprobación previa y sin una versión de prueba con alcance acotado. Para la normativa por país, usa la hoja «Normativa MCSA» del libro de Excel como agenda de la conversación con Legal.

**Decisiones y controles de gobierno y privacidad en Communication Compliance e Information Barriers**

| Decisión o control | Por qué importa | Quién debe aprobar | Evidencia a conservar | Fuente |
|---|---|---|---|---|
| Finalidad y base legal de cada política | Supervisar comunicaciones toca derechos de las personas; Microsoft deja la responsabilidad legal en la organización | Legal, privacidad y cumplimiento; RR. HH. si afecta a empleados | Acta o ticket de aprobación con la finalidad, el riesgo que se atiende y la norma interna aplicable | [Definiciones de clasificadores](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions) |
| Aviso a las personas supervisadas | La transparencia es un principio de las leyes de datos de la región (por ejemplo, el aviso de privacidad de la LFPDPPP); su forma la define Legal | Legal, RR. HH. y privacidad | Texto del aviso o de la política de uso aceptable, versión y fecha de publicación | [LFPDPPP](https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPDPPP.pdf?version=published) |
| Consulta a la representación de los trabajadores | En algunos países o contratos colectivos la supervisión requiere consulta o acuerdo previo; no lo asumas, pregúntalo | RR. HH. y Legal; consejo de empresa, sindicato o comité si aplica | Acta de consulta o constancia de Legal de que no aplica | [Planificación de CC](https://learn.microsoft.com/es-es/purview/communication-compliance-plan) |
| Población en alcance, exclusiones y pilotos | El alcance debe ser mínimo y proporcional; supervisar a personas reales exige aprobación previa y políticas de prueba acotadas | Cumplimiento y privacidad; dueño del área supervisada | Lista de grupos o ámbitos, criterios de exclusión y fecha de revisión del piloto | [Políticas](https://learn.microsoft.com/en-us/purview/communication-compliance-policies) |
| Plantillas, clasificadores e idioma | Discrimination y los clasificadores financieros solo funcionan en inglés; elegirlos sin saberlo da una falsa sensación de control | Cumplimiento, con privacidad | Matriz de riesgo, clasificador e idioma, diccionarios aprobados y resultados de «Probar condiciones» | [Definiciones de clasificadores](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions) |
| Seudonimización | Viene activa por defecto y reduce sesgos y exposición de identidades durante la revisión | Privacidad (cualquier desactivación requiere justificación) | Captura de la configuración y registro de cambios | [Guía de privacidad](https://learn.microsoft.com/en-us/purview/insider-risk-solution-privacy) |
| Separación de funciones y grupos de roles | Quien configura no debería revisar, y el administrador global no tiene acceso por defecto | Privacidad y cumplimiento | Matriz de roles, revisión trimestral de miembros y asignaciones con vencimiento | [Permisos de CC](https://learn.microsoft.com/en-us/purview/communication-compliance-permissions) |
| Selección, capacitación y rotación de revisores | Revisores que hablen el idioma de los usuarios y estén fuera de su línea jerárquica reducen errores y conflictos de interés | Cumplimiento y RR. HH. | Lista de revisores, constancia de capacitación y calendario de rotación | [Planificación de IRM](https://learn.microsoft.com/en-us/purview/insider-risk-management-plan) |
| Unidades administrativas por país o región | Limitan qué políticas y alertas ve cada revisor, pero no aplican a los reportes ni se combinan con ámbitos adaptables | Privacidad y cumplimiento | Definición de cada unidad, sus miembros y los destinatarios de reportes | [Unidades administrativas](https://learn.microsoft.com/en-us/purview/purview-admin-units) |
| Conservación de coincidencias | Desde el 1 de junio de 2025 va de 1 mes a 7 años (1 año por defecto) y lo más antiguo puede eliminarse definitivamente | Legal, gestión de registros y privacidad | Período elegido, justificación y relación con la tabla de retención | [Investigar y remediar](https://learn.microsoft.com/es-es/purview/communication-compliance-investigate-remediate) |
| Notificación y medidas sobre una persona | Un aviso por un falso positivo daña la confianza; las medidas disciplinarias son decisión de RR. HH. | RR. HH. y Legal | Plantillas de aviso aprobadas, doble revisión y registro de la decisión | [Investigar y remediar](https://learn.microsoft.com/en-us/purview/communication-compliance-investigate-remediate) |
| Escalamiento a investigación e integración con Insider Risk | Lleva la evidencia a eDiscovery (Premium) o suma señales a IRM, y aumenta el nivel de intrusión | Legal, RR. HH. y cumplimiento | Criterios de escalamiento, identificador del caso y lista de quién tiene acceso | [Políticas](https://learn.microsoft.com/en-us/purview/communication-compliance-policies) |
| Supervisión de prompts de Copilot y otras IA | Los prompts pueden contener datos personales o sensibles, y la IA que no es de Microsoft 365 genera costos de pago por uso | Privacidad, Legal y dueño del presupuesto | Ficha de aprobación, evaluación de impacto si la norma la exige, presupuesto y alertas de costo | [IA generativa](https://learn.microsoft.com/en-us/purview/communication-compliance-copilot) |
| Conectores de comunicaciones de terceros | Ingresan comunicaciones de clientes y canales externos, y los datos que procesa el partner quedan fuera de los compromisos de Purview | Legal, compras, privacidad y cumplimiento | Contrato y acuerdo de tratamiento con el partner, mapeo de usuarios y alcance | [Conector de 17a-4](https://learn.microsoft.com/en-us/purview/archive-17a-4-bloomberg-data) |
| Segmentos y políticas de Information Barriers | Una barrera mal diseñada corta la colaboración del negocio o deja pasar un conflicto de interés | Cumplimiento, Legal y dueños de negocio; los administradores de colaboración ejecutan | Matriz de segmentos y políticas, reporte de cumplimiento y plan de suspensión | [Information Barriers](https://learn.microsoft.com/en-us/purview/information-barriers) |
| Auditoría de revisores y de cambios | Demuestra quién vio qué y quién cambió qué; el cmdlet actual se retira el 15 de octubre de 2027 | Privacidad y auditoría interna | Exportación mensual de etiquetas de revisión y cambios de políticas con la API AuditLogQuery | [MC1505599](https://mc.merill.net/message/MC1505599) |
| Supervisión regulada del sector financiero | El regulador puede exigir procedimientos escritos y evidencia de revisión por personas designadas | Oficial de cumplimiento y supervisor designado, con Legal | Procedimientos de supervisión escritos, muestras revisadas y constancia de cada revisión | [Guía de un partner](https://i3solutions.com/answers/finra-sec-microsoft-365-recordkeeping-supervision/) |

Fuentes: [guía de privacidad de IRM y CC](https://learn.microsoft.com/en-us/purview/insider-risk-solution-privacy), [planificación de CC](https://learn.microsoft.com/es-es/purview/communication-compliance-plan), [permisos](https://learn.microsoft.com/en-us/purview/communication-compliance-permissions) y la normativa de la hoja «Normativa MCSA». No es asesoría legal ni laboral.

<a id="cronologia"></a>

## Cronología, cambios de nombre y retiros (2022–2027)

Las fechas que explican por qué el material de 2022 ya no alcanza y qué viene. Los cambios de nombre más frecuentes en la documentación: Supervision pasó a llamarse Communication Compliance (los cmdlets conservan el prefijo SupervisoryReview), Yammer pasó a Viva Engage, Microsoft 365 E5 Compliance pasó a Microsoft Purview Suite y el portal de cumplimiento pasó al portal de Microsoft Purview.

**Cronología de Communication Compliance e Information Barriers**

| Fecha | Hecho | Fuente | Módulo |
|---|---|---|---|
| 15 de marzo de 2022 | Fecha de referencia para habilitar Information Barriers en SharePoint y OneDrive; los tenants anteriores siguen pasos especiales | [SharePoint](https://learn.microsoft.com/en-us/purview/information-barriers-sharepoint) | [M2](02_Nivel_2_Intermedio.md#m2) |
| 19 de abril de 2022 | Se publica el Ninja oficial de Communication Compliance (actualizado en junio de 2023) | [Ninja oficial](https://techcommunity.microsoft.com/blog/microsoft-security-blog/become-a-communication-compliance-ninja/3283283) | [I0](01_Nivel_1_Inicial.md#i0) |
| 31 de julio de 2022 y 28 de febrero de 2023 | Nueva latencia de detección para políticas creadas desde el 31 de julio de 2022; migración automática de las anteriores hasta el 28 de febrero de 2023 | [Políticas](https://learn.microsoft.com/en-us/purview/communication-compliance-policies) | [I2](01_Nivel_1_Inicial.md#i2) |
| 3 de enero de 2023 | Rige la opción de registro de auditoría (audit trail) o WORM para los registros electrónicos de la SEC | [Oferta SEC 17a-4](https://learn.microsoft.com/en-us/compliance/regulatory/offering-SEC-docs) | [A4](03_Nivel_3_Avanzado.md#a4) |
| 30 de junio de 2024 | Se retiran todos los conectores de Veritas | [Conectores](https://learn.microsoft.com/en-us/purview/archive-third-party-data) | [A1](03_Nivel_3_Avanzado.md#a1) |
| 14 de noviembre a 14 de diciembre de 2024 | Se retira el portal de cumplimiento clásico | [MC939918](https://mc.merill.net/message/MC939918) | [P0](01_Nivel_1_Inicial.md#p0) |
| 19 de noviembre de 2024 | Ignite 2024: CC para Security Copilot, Copilot en Fabric, Copilot Studio y ChatGPT Enterprise (vista previa), Prompt Shields y Protected material | [Anuncio](https://techcommunity.microsoft.com/blog/microsoft-security-blog/new-purview-communication-compliance-features-for-copilot-and-insider-risk-manag/4296775) | [M1](02_Nivel_2_Intermedio.md#m1) |
| 13 de diciembre de 2024 | Se publica la Ley 21.719 de Chile | [Ley 21.719](https://www.bcn.cl/leychile/navegar?i=1209272&f=2026-12-01) | [O3](04_Nivel_4_Operacion.md#o3) |
| 20 de marzo de 2025 | México publica en el DOF la nueva LFPDPPP | [LFPDPPP](https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPDPPP.pdf?version=published) | [O3](04_Nivel_4_Operacion.md#o3) |
| 31 de marzo de 2025 | Rige el nuevo reglamento peruano de protección de datos (DS 016-2024-JUS) según la ANPD; algunas firmas citan el 30 de marzo | [DS 016-2024-JUS](https://www.gob.pe/institucion/anpd/normas-legales/6554453) | [O3](04_Nivel_4_Operacion.md#o3) |
| 1 de junio de 2025 | Entra en vigor la conservación configurable de coincidencias de política | [Investigar y remediar](https://learn.microsoft.com/es-es/purview/communication-compliance-investigate-remediate) | [I3](01_Nivel_1_Inicial.md#i3) |
| 1 de octubre de 2025 | Microsoft 365 E5 Compliance pasa a llamarse Microsoft Purview Suite | [Precios de seguridad](https://www.microsoft.com/en-us/security/pricing-overview) | [I1](01_Nivel_1_Inicial.md#i1) |
| 18 de noviembre de 2025 | Ignite 2025: novedades de Purview en DSPM y observabilidad de agentes | [Novedades de Ignite 2025](https://techcommunity.microsoft.com/blog/microsoft-security-blog/empowering-organizations-with-integrated-data-security-what%E2%80%99s-new-in-microsoft-p/4470663) | [M1](02_Nivel_2_Intermedio.md#m1) |
| Enero de 2026 | Mejoras de alertas por política en GA para GCC, GCC High y DoD | [RM529852](https://mc.merill.net/message/RM529852) | [I3](01_Nivel_1_Inicial.md#i3) |
| 9 de marzo de 2026 | MC920304 retrasa la vista previa mundial de las mejoras de alertas a octubre de 2026 | [MC920304](https://mc.merill.net/message/MC920304) | [I3](01_Nivel_1_Inicial.md#i3), [O2](04_Nivel_4_Operacion.md#o2) |
| 1 de mayo de 2026 | GA de Microsoft 365 E7 y Agent 365 | [E7 y Agent 365](https://techcommunity.microsoft.com/blog/microsoft_365blog/microsoft-365-e7-and-agent-365-are-now-generally-available/4516295) | [I1](01_Nivel_1_Inicial.md#i1), [M1](02_Nivel_2_Intermedio.md#m1) |
| Julio de 2026 | Asignaciones a grupos de roles de Purview con vencimiento | [Novedades](https://learn.microsoft.com/en-us/purview/whats-new) | [P0](01_Nivel_1_Inicial.md#p0), [M3](02_Nivel_2_Intermedio.md#m3) |
| Agosto de 2026 | Claude Enterprise suma Communication Compliance entre las capacidades de Purview | [Claude Enterprise](https://learn.microsoft.com/en-us/purview/ai-claude-enterprise) | [M1](02_Nivel_2_Intermedio.md#m1) |
| Septiembre de 2026 | El reporte de cumplimiento de IB incluye contenedores de SharePoint Embedded propiedad de usuarios | [Reporte de IB](https://learn.microsoft.com/en-us/purview/information-barriers-sharepoint-report) | [M2](02_Nivel_2_Intermedio.md#m2) |
| Octubre de 2026 | GA de la API AuditLogQuery de Microsoft Graph y anuncio del retiro de Search-UnifiedAuditLog | [MC1505599](https://mc.merill.net/message/MC1505599) | [A2](03_Nivel_3_Avanzado.md#a2), [A3](03_Nivel_3_Avanzado.md#a3) |
| 16 de octubre de 2026 | Actualización de las definiciones de clasificadores entrenables y de la página de novedades de Purview | [Definiciones](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions) | [I2](01_Nivel_1_Inicial.md#i2), [C2](05_Comunidad.md#c2) |
| 17 a 20 de noviembre de 2026 | Microsoft Ignite 2026: posibles cambios de estado de vista previa | [Novedades](https://learn.microsoft.com/en-us/purview/whats-new) | [C2](05_Comunidad.md#c2) |
| 1 de diciembre de 2026 | Entra en vigencia la Ley 21.719 de Chile | [Ley 21.719](https://www.bcn.cl/leychile/navegar?i=1209272&f=2026-12-01) | [O3](04_Nivel_4_Operacion.md#o3) |
| 15 de octubre de 2027 | Se retira Search-UnifiedAuditLog | [MC1505599](https://mc.merill.net/message/MC1505599) | [A2](03_Nivel_3_Avanzado.md#a2), [A3](03_Nivel_3_Avanzado.md#a3) |

Fuentes: la de cada fila. Verificado al 6 de noviembre de 2026.

<a id="formato"></a>

## El formato Ninja: historia y familia

El Ninja oficial de Communication Compliance se publicó el 19 de abril de 2022 en el Microsoft Security Community Blog, escrito por Patrick David (Microsoft). No se organizaba por niveles, sino en secciones: por qué necesitas Communication Compliance, visión general, primeros pasos (guías, licencias, permisos, privacidad, políticas, investigación y remediación), comunicaciones que no son de Microsoft, integración con otras herramientas (Insider Risk, Power Automate, DLP, tipos de información confidencial, eDiscovery Premium y SIEM), ajuste de condiciones, reportes y auditoría, y recursos adicionales como el roadmap y el Message Center. Cada recurso llevaba una etiqueta según su tipo: VIDEO, WEBCAST, COMMUNITY, DOC, BLOG, GITHUB, NEW, GUIDE, LEARN, EXT o PODCAST.

Cada sección cerraba con una verificación de conocimientos y, al terminar, el certificado se solicitaba en un portal de atestación y llegaba por correo en 3 a 5 días hábiles. Su última actualización indicada es de junio de 2023: prometía revisiones semestrales, pero no hay versiones posteriores visibles. Por eso usa nombres antiguos (compliance portal, Yammer) y no cubre Copilot ni la IA, el pago por uso, el portal unificado, las acciones de Security Copilot ni Information Barriers, que nunca tuvo un Ninja propio. Mientras tanto, la familia Ninja de Purview empezó a migrar a rutas de Microsoft Learn con insignia, como pasó con Information Protection, retirado de Tech Community en julio de 2025.

Esta edición respeta esa forma —módulos con introducción, recursos curados, práctica y evaluación— y la reorganiza en niveles con evaluación al 80 %, un track de operación para el modelo operativo y el gobierno, y la cobertura que faltaba: IA generativa, Information Barriers, supervisión financiera, auditoría con la API de Microsoft Graph y la realidad normativa de MCSA.

**La familia Ninja relacionada**

| Ninja | Qué cubre | Estado y última actualización |
|---|---|---|
| [Become a Communication Compliance Ninja](https://techcommunity.microsoft.com/blog/microsoft-security-blog/become-a-communication-compliance-ninja/3283283) | Secciones temáticas de Communication Compliance, con knowledge check por sección y certificado por portal de atestación | Legado aún útil: publicado el 19 de abril de 2022 y actualizado en junio de 2023 |
| [Become an Insider Risk Management Ninja](https://techcommunity.microsoft.com/t5/security-compliance-and-identity/become-an-insider-risk-management-ninja/ba-p/3282306) | Secciones temáticas de Insider Risk Management con knowledge checks | Abril de 2022; última actualización conocida en septiembre de 2024 (ver el programa de Insider Risk Management) |
| [Become a Microsoft Purview eDiscovery Ninja](https://techcommunity.microsoft.com/blog/microsoft-security-blog/become-a-microsoft-purview-ediscovery-ninja/2793108) | eDiscovery de punta a punta, de la identificación a la producción | 5 de mayo de 2026 según el índice de Tech Community (ver el programa de eDiscovery y Audit) |
| [Compliance Manager Ninja](https://techcommunity.microsoft.com/blog/microsoft-security-blog/microsoft-purview-compliance-manager-mspcm-ninja-training-q1-2023/3181322) | Tres niveles con knowledge checks y certificado no oficial | Edición Q1 2023 (publicado el 18 de febrero de 2022) |
| [Become a Microsoft Priva Ninja](https://techcommunity.microsoft.com/blog/microsoft-security-blog/become-a-microsoft-priva-ninja/3876888) | Privacy Risk Management y solicitudes de derechos de los titulares, en tres niveles | 18 de julio de 2023 (legado) |
| [Data Lifecycle y Records Management Ninja](https://techcommunity.microsoft.com/discussions/microsoft-security/new-blog--become-a-microsoft-purview-data-lifecycle-and-records-management-ninja/3883998) | Retención, registros y eliminación; sin evaluación | 25 de julio de 2023 |
| [Information Protection Ninja](https://aka.ms/MIPNinja) | Clasificación, etiquetado y DLP | Retirado de Tech Community en julio de 2025 y trasladado a un nuevo alojamiento en agosto de 2025 |
| [Secure sensitive data with Microsoft Purview Ninja training scenarios](https://learn.microsoft.com/en-us/training/paths/purview-ninja-safeguard-data/) | Ruta de Learn con insignia: SIT, etiquetas, Security Copilot en Purview, DLP y Endpoint DLP | Vigente; la página no muestra fecha de actualización |

**Del Ninja oficial a esta edición**

| Ninja oficial | Contenido | En esta edición |
|---|---|---|
| 1 · Why do I need Communication Compliance? | Escenarios y valor de negocio | [I1](01_Nivel_1_Inicial.md#i1), [O1](04_Nivel_4_Operacion.md#o1) |
| 2 · Overview | Qué hace Communication Compliance y cómo funciona | [I1](01_Nivel_1_Inicial.md#i1), [I2](01_Nivel_1_Inicial.md#i2) |
| 3 · Getting Started | Guías, licencias, permisos, privacidad, políticas, investigación y remediación | [P0](01_Nivel_1_Inicial.md#p0), [I1](01_Nivel_1_Inicial.md#i1), [I2](01_Nivel_1_Inicial.md#i2), [I3](01_Nivel_1_Inicial.md#i3), [M3](02_Nivel_2_Intermedio.md#m3) |
| 4 · Comunicaciones que no son de Microsoft | Conectores de datos de terceros | [A1](03_Nivel_3_Avanzado.md#a1) |
| 5 · Integración con otras herramientas | Insider Risk, Power Automate, DLP, SIT, eDiscovery (Premium) y SIEM | [M4](02_Nivel_2_Intermedio.md#m4), [A2](03_Nivel_3_Avanzado.md#a2), [A3](03_Nivel_3_Avanzado.md#a3) |
| 6 · Ajuste de condiciones | Condiciones, diccionarios y reducción de falsos positivos | [I2](01_Nivel_1_Inicial.md#i2), [O2](04_Nivel_4_Operacion.md#o2) |
| 7 · Reportes y auditoría | Widgets, reportes detallados y registro de auditoría | [A2](03_Nivel_3_Avanzado.md#a2) |
| Recursos adicionales | Roadmap, Message Center y foro de comentarios | [C1](05_Comunidad.md#c1), [C2](05_Comunidad.md#c2) |
| Knowledge checks y certificado | Verificación por sección y certificado por portal de atestación | [I0](01_Nivel_1_Inicial.md#i0) |
| Nuevo en esta edición | Copilot y apps de IA, Information Barriers, supervisión financiera, track de operación y recursos en español | [M1](02_Nivel_2_Intermedio.md#m1), [M2](02_Nivel_2_Intermedio.md#m2), [A4](03_Nivel_3_Avanzado.md#a4), [O1](04_Nivel_4_Operacion.md#o1), [O2](04_Nivel_4_Operacion.md#o2), [O3](04_Nivel_4_Operacion.md#o3), [C2](05_Comunidad.md#c2) |

**Recursos sobre el Ninja oficial y su familia**

- [Become a Communication Compliance Ninja](https://techcommunity.microsoft.com/blog/microsoft-security-blog/become-a-communication-compliance-ninja/3283283) · Blog oficial · Empleado de Microsoft · Legado aún útil · Patrick_David · Microsoft Tech Community (Microsoft Security Community Blog) · 19 abr 2022. Ninja oficial de Communication Compliance: secciones Why, Overview, Getting Started, fuentes no Microsoft, integraciones, ajuste fino, reportes/auditoría, con knowledge checks por sección y certificado vía portal de atestación. *Nota:* Última actualización indicada: junio de 2023; usa nombres antiguos (compliance portal, Yammer) y no cubre Copilot/IA, PAYG ni Information Barriers
- [Become a Microsoft Priva Ninja](https://techcommunity.microsoft.com/blog/microsoft-security-blog/become-a-microsoft-priva-ninja/3876888) · Blog oficial · Empleado de Microsoft · Legado aún útil · John_Wirtala1608 · Microsoft Tech Community (Microsoft Security Community Blog) · 18 jul 2023. Otro ejemplo de la familia Ninja de seguridad/cumplimiento: recursos curados por módulo (Risk Management y Subject Rights Requests) en tres niveles: principiante, intermedio y avanzado. *Nota:* Referencia de formato de la serie Ninja (2023); Privacy Risk Management se movió al portal de Microsoft Priva
- [Microsoft Purview Compliance Manager (MSPCM) Ninja Training: Q1 2023](https://techcommunity.microsoft.com/blog/microsoft-security-blog/microsoft-purview-compliance-manager-mspcm-ninja-training-q1-2023/3181322) · Blog oficial · Empleado de Microsoft · Legado aún útil · garyasp · Microsoft Tech Community · 18 feb 2022. Ejemplo de la familia Ninja de Purview con tres niveles (básico, intermedio, avanzado), knowledge checks y certificado no oficial emitido vía portal de atestación. *Nota:* Referencia de formato de la familia Ninja de Purview; contenido 2022-2023

<a id="cambios"></a>

## Qué cambió y por qué importa

Cada fila remite al módulo donde se explica en detalle.

| Tema | Ninja oficial (2022–2023) | Ahora (noviembre de 2026) | Módulo |
|---|---|---|---|
| Portal | Centro o portal de cumplimiento de Microsoft 365 | Portal unificado de Microsoft Purview; el portal clásico se retiró entre el 14 de noviembre y el 14 de diciembre de 2024 con paridad de configuraciones | [P0](01_Nivel_1_Inicial.md#p0) |
| Roles | Grupos de roles con asignaciones permanentes | Asignaciones con vencimiento de 1 día a 2 años (julio de 2026) y PIM para grupos, que puede tardar hasta 2 horas en aplicarse | [P0](01_Nivel_1_Inicial.md#p0), [M3](02_Nivel_2_Intermedio.md#m3) |
| Licencias | Microsoft 365 E5 o E5 Compliance (y menciones a Office 365 E3 + Advanced Compliance) | Microsoft 365 E5/A5/G5, Microsoft Purview Suite (nuevo nombre de E5 Compliance desde el 1 de octubre de 2025), complemento E5 Insider Risk Management y Office 365 E5; Microsoft 365 E3 no lo incluye | [I1](01_Nivel_1_Inicial.md#i1) |
| Viva Engage | Yammer | Viva Engage, solo en modo nativo | [I1](01_Nivel_1_Inicial.md#i1) |
| Canales de IA | No existían | Microsoft 365 Copilot y Copilot Chat (licencia de Copilot, sin pago por uso); Copilot Studio, Copilot en Fabric, Security Copilot, apps de IA empresariales y otras apps de IA con pago por uso | [M1](02_Nivel_2_Intermedio.md#m1) |
| Facturación | Solo licencias por usuario | Licencia por usuario más pago por uso en registros de texto de 1.000 caracteres, con medidor estándar y premium (página del 6 de enero de 2026) | [I1](01_Nivel_1_Inicial.md#i1), [M1](02_Nivel_2_Intermedio.md#m1) |
| Agentes | No existían | Según la descripción de servicio, Purview para agentes de Microsoft Foundry y apps conectadas a Entra se soporta con Microsoft 365 E7 y Agent 365 (ambos en GA desde el 1 de mayo de 2026) | [M1](02_Nivel_2_Intermedio.md#m1) |
| Plantillas | Conducta, conflicto de intereses, cumplimiento normativo e información confidencial | Siete plantillas, entre ellas interacciones de Copilot y contenido inapropiado con clasificadores LLM, más la política de mensajes notificados por usuarios | [I2](01_Nivel_1_Inicial.md#i2) |
| Clasificadores | Threat, Harassment, Profanity, Discrimination, imágenes y financieros | Se suman Hate, Sexual, Violence y Self-harm (LLM, con severidad) y Prompt Shields y Protected material (Ignite 2024); CC no admite clasificadores personalizados | [I2](01_Nivel_1_Inicial.md#i2), [M1](02_Nivel_2_Intermedio.md#m1) |
| Idiomas | Mayormente inglés | Threat, Harassment y Profanity en 12 idiomas, incluido el español (mínimo 6 palabras); Discrimination y los seis financieros siguen solo en inglés (definiciones del 16 de octubre de 2026) | [I2](01_Nivel_1_Inicial.md#i2), [A4](03_Nivel_3_Avanzado.md#a4) |
| Latencia de detección | Hasta 24 a 48 horas | Políticas creadas desde el 31 de julio de 2022: cuerpo de correo, Teams y Copilot en 1 hora; adjuntos, OCR y canales compartidos en 24 horas (la página de canales aún indica 24 a 48 horas) | [I2](01_Nivel_1_Inicial.md#i2) |
| Salud de políticas | Sin recomendaciones | Policy health (vista previa) recomienda filtrar envíos masivos y reducir puntos ciegos de alcance | [I2](01_Nivel_1_Inicial.md#i2), [O2](04_Nivel_4_Operacion.md#o2) |
| Conservación de coincidencias | Sin configuración propia | Configurable desde el 1 de junio de 2025: de 1 mes a 7 años, 1 año por defecto; lo más antiguo puede eliminarse definitivamente | [I3](01_Nivel_1_Inicial.md#i3) |
| Resúmenes | Lectura manual de cada mensaje | Security Copilot resume coincidencias de políticas basadas en clasificadores entrenables y responde prompts de seguimiento | [I3](01_Nivel_1_Inicial.md#i3) |
| Alertas por política | Configuración general | Frecuencia y destinatarios por política: GA en enero de 2026 para GCC, GCC High y DoD (RM529852); vista previa mundial retrasada a octubre de 2026 y GA por anunciar (MC920304) | [I3](01_Nivel_1_Inicial.md#i3), [O2](04_Nivel_4_Operacion.md#o2) |
| Integración con Insider Risk | Indicadores de CC en IRM | Política «Insider risk trigger» automática (5 o más mensajes de riesgo en 24 horas) e indicadores de IA generativa (Prompt Shields y Protected material) | [M4](02_Nivel_2_Intermedio.md#m4) |
| Conectores | Veritas y conectores nativos | Veritas retirado el 30 de junio de 2024; partners TeleMessage, 17a-4 y CellTrust; conectores nativos que incluyen ChatGPT Enterprise y Anthropic Claude | [A1](03_Nivel_3_Avanzado.md#a1) |
| Claude Enterprise | No existía | Communication Compliance compatible desde agosto de 2026, mediante un conector en vista previa y con pago por uso | [M1](02_Nivel_2_Intermedio.md#m1) |
| Auditoría | Search-UnifiedAuditLog | API AuditLogQuery de Microsoft Graph en GA desde octubre de 2026; Search-UnifiedAuditLog se retira el 15 de octubre de 2027 | [A2](03_Nivel_3_Avanzado.md#a2), [A3](03_Nivel_3_Avanzado.md#a3) |
| PowerShell | Cmdlets SupervisoryReview para crear políticas | La página de políticas dice que PowerShell no es compatible para crear o administrar políticas de CC; los cmdlets heredados siguen documentados (solo para inventario) | [A3](03_Nivel_3_Avanzado.md#a3) |
| Information Barriers | Fuera del Ninja | Modos Legacy, segmento único y multisegmento (hasta 5.000 segmentos y 10 por usuario), modos de sitio en SharePoint y OneDrive, y Planner en planes básicos | [M2](02_Nivel_2_Intermedio.md#m2) |
| Reporte de Information Barriers | No existía | Desde septiembre de 2026, el reporte de cumplimiento de políticas cubre sitios, OneDrive y contenedores de SharePoint Embedded propiedad de usuarios | [M2](02_Nivel_2_Intermedio.md#m2) |
| Credenciales | SC-400 y knowledge checks del Ninja | Applied Skills APL-5007 (retención, eDiscovery y CC, laboratorio de 2 horas) y SC-401, que no mide CC ni IB | [I0](01_Nivel_1_Inicial.md#i0) |

<a id="rutas"></a>

## Rutas por rol

Las horas son estimaciones de lectura y práctica.

- **Administrador de Communication Compliance** (~39 h). Configura políticas, canales, licencias, pago por uso, conectores y automatizaciones. Módulos: [P0](01_Nivel_1_Inicial.md#p0), [I0](01_Nivel_1_Inicial.md#i0), [I1](01_Nivel_1_Inicial.md#i1), [I2](01_Nivel_1_Inicial.md#i2), [I3](01_Nivel_1_Inicial.md#i3), [M1](02_Nivel_2_Intermedio.md#m1), [M3](02_Nivel_2_Intermedio.md#m3), [M4](02_Nivel_2_Intermedio.md#m4), [A1](03_Nivel_3_Avanzado.md#a1), [A2](03_Nivel_3_Avanzado.md#a2), [A3](03_Nivel_3_Avanzado.md#a3), [O2](04_Nivel_4_Operacion.md#o2).
- **Revisores e investigadores** (~29 h). Revisan alertas, documentan decisiones, remedian y escalan con criterio y privacidad. Módulos: [P0](01_Nivel_1_Inicial.md#p0), [I0](01_Nivel_1_Inicial.md#i0), [I2](01_Nivel_1_Inicial.md#i2), [I3](01_Nivel_1_Inicial.md#i3), [M3](02_Nivel_2_Intermedio.md#m3), [M4](02_Nivel_2_Intermedio.md#m4), [A2](03_Nivel_3_Avanzado.md#a2), [O1](04_Nivel_4_Operacion.md#o1), [O2](04_Nivel_4_Operacion.md#o2).
- **Oficial de cumplimiento y supervisión financiera** (~41 h). Diseña la supervisión regulada, las barreras éticas y la evidencia ante el regulador. Módulos: [I1](01_Nivel_1_Inicial.md#i1), [I2](01_Nivel_1_Inicial.md#i2), [I3](01_Nivel_1_Inicial.md#i3), [M2](02_Nivel_2_Intermedio.md#m2), [M4](02_Nivel_2_Intermedio.md#m4), [A1](03_Nivel_3_Avanzado.md#a1), [A2](03_Nivel_3_Avanzado.md#a2), [A4](03_Nivel_3_Avanzado.md#a4), [O1](04_Nivel_4_Operacion.md#o1), [O2](04_Nivel_4_Operacion.md#o2), [O3](04_Nivel_4_Operacion.md#o3).
- **Recursos Humanos** (~19 h). Define avisos y criterios de notificación y de medidas, y participa en el gobierno y en la consulta a los trabajadores. Módulos: [I1](01_Nivel_1_Inicial.md#i1), [I3](01_Nivel_1_Inicial.md#i3), [M3](02_Nivel_2_Intermedio.md#m3), [M4](02_Nivel_2_Intermedio.md#m4), [O1](04_Nivel_4_Operacion.md#o1), [O3](04_Nivel_4_Operacion.md#o3).
- **Legal** (~31 h). Aprueba finalidad, alcance, conservación, escalamientos y contratos de conectores. Módulos: [I1](01_Nivel_1_Inicial.md#i1), [I3](01_Nivel_1_Inicial.md#i3), [M1](02_Nivel_2_Intermedio.md#m1), [M3](02_Nivel_2_Intermedio.md#m3), [M4](02_Nivel_2_Intermedio.md#m4), [A1](03_Nivel_3_Avanzado.md#a1), [A2](03_Nivel_3_Avanzado.md#a2), [A4](03_Nivel_3_Avanzado.md#a4), [O3](04_Nivel_4_Operacion.md#o3).
- **Oficial de privacidad** (~22 h). Asegura seudonimización, minimización, control de accesos y auditoría de revisores. Módulos: [I1](01_Nivel_1_Inicial.md#i1), [M1](02_Nivel_2_Intermedio.md#m1), [M3](02_Nivel_2_Intermedio.md#m3), [A2](03_Nivel_3_Avanzado.md#a2), [O1](04_Nivel_4_Operacion.md#o1), [O2](04_Nivel_4_Operacion.md#o2), [O3](04_Nivel_4_Operacion.md#o3).
- **Administradores de colaboración (Information Barriers)** (~20 h). Implementan segmentos, políticas y modos de sitio en Teams, SharePoint y OneDrive, y verifican su cumplimiento. Módulos: [P0](01_Nivel_1_Inicial.md#p0), [I0](01_Nivel_1_Inicial.md#i0), [M2](02_Nivel_2_Intermedio.md#m2), [M3](02_Nivel_2_Intermedio.md#m3), [A2](03_Nivel_3_Avanzado.md#a2), [A3](03_Nivel_3_Avanzado.md#a3).

<a id="plan"></a>

## Plan de entrenamiento sugerido

Calendario de referencia de 12 semanas para una dedicación de 4 a 5 horas por semana (unas 57 horas). Cada semana deja un entregable verificable; las evaluaciones cierran las semanas 4, 8, 10 y 12.

| Semana | Módulos | Foco | Entregable |
|---|---|---|---|
| 1 | [P0](01_Nivel_1_Inicial.md#p0), [I0](01_Nivel_1_Inicial.md#i0) | Portal, permisos, auditoría y ruta de aprendizaje | Auditoría activa, grupos de roles con vencimiento asignados a cuentas de prueba y plan de estudio mapeado a APL-5007 |
| 2 | [I1](01_Nivel_1_Inicial.md#i1) | Canales, licencias y pago por uso | Matriz de canales y licencias validada con licenciamiento y cálculo de registros de texto |
| 3 | [I2](01_Nivel_1_Inicial.md#i2) | Plantillas, clasificadores, condiciones e idioma | Política piloto con diccionario en español validado con «Probar condiciones» |
| 4 | [I3](01_Nivel_1_Inicial.md#i3) | Revisión, remediación y conservación | Flujo de revisión completo con evidencia; evaluación del nivel 1 aprobada |
| 5 | [M3](02_Nivel_2_Intermedio.md#m3) | Privacidad, roles y unidades administrativas | Matriz de roles probada y unidades administrativas por país |
| 6 | [M1](02_Nivel_2_Intermedio.md#m1) | Copilot y apps de IA | Política de Copilot (o su diseño aprobado) y estimación de costo con pago por uso |
| 7 | [M2](02_Nivel_2_Intermedio.md#m2) | Information Barriers | Segmentos y políticas de prueba aplicados, modos de sitio verificados y reporte de cumplimiento |
| 8 | [M4](02_Nivel_2_Intermedio.md#m4) | Insider Risk Management y eDiscovery | Insider risk trigger verificado y caso de eDiscovery escalado; evaluación del nivel 2 aprobada |
| 9 | [A1](03_Nivel_3_Avanzado.md#a1), [A2](03_Nivel_3_Avanzado.md#a2) | Conectores, reportes y auditoría | Diseño del conector piloto y consultas de auditoría con el cmdlet y con la API comparadas |
| 10 | [A3](03_Nivel_3_Avanzado.md#a3), [A4](03_Nivel_3_Avanzado.md#a4) | Automatización y supervisión financiera | Flujo de Power Automate, script de evidencia y arquitectura de una mesa de negociación; evaluación del nivel 3 aprobada |
| 11 | [O1](04_Nivel_4_Operacion.md#o1), [O2](04_Nivel_4_Operacion.md#o2) | Modelo operativo y métricas | Matriz RACI, procedimiento de revisión y tablero de indicadores |
| 12 | [O3](04_Nivel_4_Operacion.md#o3), [C1](05_Comunidad.md#c1), [C2](05_Comunidad.md#c2) | Gobierno en MCSA y comunidad | Expediente de gobierno, preguntas para Legal por país y rutina de actualización; evaluación del track de operación aprobada |

<a id="laboratorio"></a>

## Tu laboratorio

**Tu entorno.** La base es una prueba de Microsoft 365 E5 (25 licencias durante un mes), que incluye Communication Compliance (Information Barriers se practica con segmentos de prueba y las limitaciones del módulo M2), o un sandbox de desarrollador vinculado a tu suscripción de Visual Studio para prácticas más largas, más una suscripción de Azure con el crédito mensual de Visual Studio Enterprise para el pago por uso. El día 0 activa la auditoría, crea entre 10 y 16 personas de prueba con atributos completos (Department, país), confirma que los revisores tengan buzón de Exchange Online y que Viva Engage esté en modo nativo. El detalle está en el anexo del entorno de práctica.

**Tiempos.** La página de políticas de Communication Compliance indica 1 hora para el cuerpo de los mensajes y 24 horas para adjuntos y OCR, pero la página de canales habla de unas 24 horas en correo y hasta 48 en Teams, Viva Engage y fuentes de terceros: planifica con el escenario más lento; Information Barriers arranca en unos 30 minutos, procesa unos 5.000 usuarios por hora y Teams necesita hasta 24 horas para la búsqueda de directorio con ámbito; la integración con Insider Risk puede tardar hasta 48 horas. Envía mensajes sintéticos los días 1 y 2 y practica otros módulos mientras esperas.

**Qué no se puede practicar en el laboratorio.** Microsoft 365 Copilot (la prueba de E5 no incluye sus licencias), los conectores de terceros (requieren contratos con Bloomberg o con partners), la supervisión financiera con volumen real y supervisores designados, y los despliegues de Information Barriers a toda la organización. Esos ejercicios están etiquetados [LAB-PARCIAL] o [SOLO-PRODUCCION], con una forma segura de practicar en producción.

**Personas reales.** Supervisar comunicaciones de personas reales, incluso en un piloto, exige aprobación previa de Legal, RR. HH. y privacidad (y de la representación de los trabajadores cuando la ley o un contrato colectivo lo pidan), aviso a las personas, políticas de prueba con alcance acotado, seudonimización activa y revisores fuera de la línea jerárquica. En el laboratorio usa solo mensajes sintéticos: nunca copies conversaciones reales.

**Costos a vigilar.** Registros de texto de pago por uso (estándar y premium) en políticas sobre IA que no es de Microsoft 365, unidades de Security Copilot y la ingesta en Sentinel si exportas la auditoría. Ninguna página revisada confirma que el crédito de Visual Studio cubra los medidores de Purview: configura presupuesto y alertas al 50, 75 y 90 % y revisa los costos a las 48 horas de cada prueba.

**Limpieza.** Nombra todo con el prefijo `PRUEBA-CC-` (los nombres de política de CC no se pueden cambiar después de crearlas), desactiva o elimina las políticas piloto, quita el pago por uso que no uses, retira los segmentos y políticas de Information Barriers de prueba y deja que venzan las asignaciones temporales de roles.

La matriz de qué se puede practicar en el laboratorio y qué solo en producción está en [07_Laboratorio_y_practica_en_produccion.md](07_Laboratorio_y_practica_en_produccion.md). La guía para construir el entorno está en el [anexo común](../Anexo_Entorno_de_practica.md).

<a id="mapa"></a>

## Mapa de módulos

- **Nivel 1 · Inicial:** [P0 Portal y permisos](01_Nivel_1_Inicial.md#p0) · [I0 Cómo aprender](01_Nivel_1_Inicial.md#i0) · [I1 Canales y licencias](01_Nivel_1_Inicial.md#i1) · [I2 Políticas y clasificadores](01_Nivel_1_Inicial.md#i2) · [I3 Revisión y remediación](01_Nivel_1_Inicial.md#i3)
- **Nivel 2 · Intermedio:** [M1 Copilot y apps de IA](02_Nivel_2_Intermedio.md#m1) · [M2 Information Barriers](02_Nivel_2_Intermedio.md#m2) · [M3 Privacidad y roles](02_Nivel_2_Intermedio.md#m3) · [M4 Insider Risk y eDiscovery](02_Nivel_2_Intermedio.md#m4)
- **Nivel 3 · Avanzado:** [A1 Conectores de terceros](03_Nivel_3_Avanzado.md#a1) · [A2 Reportes y auditoría](03_Nivel_3_Avanzado.md#a2) · [A3 Power Automate y APIs](03_Nivel_3_Avanzado.md#a3) · [A4 Supervisión financiera](03_Nivel_3_Avanzado.md#a4)
- **Nivel 4 · Operación:** [O1 Modelo operativo](04_Nivel_4_Operacion.md#o1) · [O2 Métricas y mejora continua](04_Nivel_4_Operacion.md#o2) · [O3 Gobierno, privacidad y MCSA](04_Nivel_4_Operacion.md#o3)
- **Comunidad:** [C1 Referentes y libros](05_Comunidad.md#c1) · [C2 Español y actualización](05_Comunidad.md#c2)

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. No constituye asesoría legal ni laboral: las decisiones sobre supervisión de comunicaciones, privacidad, avisos a empleados y relaciones laborales corresponden a tus áreas de Legal, RR. HH. y privacidad. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

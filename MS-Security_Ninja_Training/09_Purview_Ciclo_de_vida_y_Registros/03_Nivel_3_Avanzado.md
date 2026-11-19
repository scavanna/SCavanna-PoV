# Nivel 3 · Avanzado · IA, APIs, holds y regulación

*Microsoft Purview Ciclo de vida de los datos y Gestión de registros Ninja Training · Edición 2026*

[← Nivel 2 · Intermedio](02_Nivel_2_Intermedio.md) · [Índice del programa](README.md) · [Nivel 4 · Operación →](04_Nivel_4_Operacion.md)

<a id="avanzado"></a>

Retención para Copilot y apps de IA, automatización con Microsoft Graph, PowerShell y Power Automate, convivencia con los holds de eDiscovery, requisitos regulatorios y Multi-Geo. Terminas con un plan de archivos como código y decisiones documentadas con Legal.

*L400 · 4 módulos · ~15 horas · 16 recursos*

**Módulos de este nivel:** [A1 Retención de Copilot e IA](#a1) · [A2 APIs y automatización](#a2) · [A3 Holds y eDiscovery](#a3) · [A4 Regulación y multigeografía](#a4)

<a id="a1"></a>

## A1 · Retención para Copilot y aplicaciones de IA

*L400 · ~4 h · Origen: Nuevo en esta edición (el Ninja de 2023 es anterior a Copilot)*

Las conversaciones con IA son contenido de negocio: pueden ser evidencia, contener datos personales o recoger decisiones. Purview las retiene con tres ubicaciones propias: **Microsoft Copilot experiences** (Microsoft 365 Copilot, Security Copilot, Copilot en Fabric y Copilot Studio), **Enterprise AI apps** (apps registradas en Entra, ChatGPT Enterprise y Microsoft Foundry) y **Other AI apps** (como ChatGPT, Gemini, Copilot para consumidores o DeepSeek). Desde noviembre de 2024 son ubicaciones separadas de los chats de Teams.

Los prompts y las respuestas se guardan en una carpeta oculta del buzón del usuario. El temporizador tarda de 1 a 7 días, los elementos pasan al menos un día en SubstrateHolds y cualquier hold suspende la eliminación. Para las apps de IA distintas de Microsoft 365 Copilot y Copilot Studio necesitas además una **directiva de recopilación** con captura de contenido. Las tres ubicaciones exigen facturación de pago por uso, aunque las interacciones de Microsoft 365 Copilot no generan cargo.

En licencias: retener interacciones de Copilot requiere E3 o E5 más Microsoft 365 Copilot; los ámbitos adaptables y la retención de la versión exacta del documento compartido requieren E5 más Copilot, o E3 más Purview Suite o IP&G más Copilot. En 2026 se sumaron Anthropic Claude Enterprise (agosto) y protecciones disponibles para Agent 365 (mayo) y Copilot Cowork (junio). La seguridad de datos para IA se profundiza en el programa de DSPM y seguridad de datos para IA, módulos I2 y M1.

**Por qué importa**

Sin una decisión explícita, las interacciones con IA quedan sin retener —y se pierde evidencia— o se acumulan sin límite con datos personales. Definir con Legal y privacidad cuánto conservar, para quién y con qué excepciones reduce el riesgo regulatorio y de litigio, y controla el costo de pago por uso de las apps de IA que no son de Microsoft.

**Qué vas a lograr**

- Identificar las tres ubicaciones de IA y qué aplicaciones cubre cada una.
- Configurar una directiva de retención para interacciones de Copilot con un ámbito piloto.
- Habilitar el pago por uso y una directiva de recopilación para IA que no es de Microsoft.
- Explicar cómo interactúan la retención de IA y los holds de eDiscovery.
- Evaluar licencias y costos con Legal y privacidad, y documentar la decisión.

> **Qué cambió.** Desde el 19 de noviembre de 2024, las interacciones de Copilot tienen una ubicación propia, separada de los chats de Teams ([anuncio](https://techcommunity.microsoft.com/blog/microsoft-security-blog/new-m365-copilot-data-lifecycle-management-options/4304636)). Hoy son tres ubicaciones: Microsoft Copilot experiences, Enterprise AI apps y Other AI apps ([retención para Copilot e IA](https://learn.microsoft.com/en-us/purview/retention-policies-copilot)).

> **Atención.** Las tres ubicaciones de IA exigen facturación de pago por uso, aunque las interacciones de Microsoft 365 Copilot no generan cargo ([primeros pasos con DLM](https://learn.microsoft.com/en-us/purview/get-started-with-data-lifecycle-management), [modelos de facturación](https://learn.microsoft.com/en-us/purview/purview-billing-models)). Para la IA distinta de Microsoft 365 Copilot y Copilot Studio necesitas además una directiva de recopilación con captura de contenido ([directivas de recopilación](https://learn.microsoft.com/en-us/purview/collection-policies-solution-overview)).

> **Novedad.** En 2026 Purview sumó soporte de ciclo de vida para Anthropic Claude Enterprise (agosto) y protecciones disponibles en general para Agent 365 (mayo) y Copilot Cowork (junio) ([novedades](https://learn.microsoft.com/en-us/purview/whats-new)). La descripción del servicio anticipa que las capacidades para agentes de Microsoft Foundry y apps de IA conectadas a Entra se licenciarán con Microsoft 365 E7 y SKU de Agent 365 ([descripción del servicio](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)).

> **Consejo Ninja.** Los prompts y las respuestas se guardan en una carpeta oculta del buzón del usuario, el temporizador tarda de 1 a 7 días y los elementos pasan al menos un día en SubstrateHolds; cualquier hold suspende la eliminación ([retención para Copilot e IA](https://learn.microsoft.com/en-us/purview/retention-policies-copilot)). Verifica el resultado con eDiscovery ([buscar datos de Copilot](https://learn.microsoft.com/en-us/purview/edisc-search-copilot-data)). La protección de datos para IA se profundiza en el programa de DSPM y seguridad de datos para IA, módulos I2 y M1.

**¿Tienes poco tiempo?**

- [Learn about retention for Copilot & AI apps](https://learn.microsoft.com/en-us/purview/retention-policies-copilot) · Documentación
- [Collection Policies solution overview](https://learn.microsoft.com/en-us/purview/collection-policies-solution-overview) · Documentación
- [New M365 Copilot Data Lifecycle Management options](https://techcommunity.microsoft.com/blog/microsoft-security-blog/new-m365-copilot-data-lifecycle-management-options/4304636) · Blog oficial

**Ubicaciones de retención para Copilot y aplicaciones de IA**

| Ubicación | Qué incluye | Qué necesitas además de la directiva | Licencia y facturación |
|---|---|---|---|
| Microsoft Copilot experiences | Microsoft 365 Copilot, Security Copilot, Copilot en Fabric y Copilot Studio | Nada para Microsoft 365 Copilot y Copilot Studio; directiva de recopilación con captura de contenido para las demás experiencias | E3 o E5 + Microsoft 365 Copilot; pago por uso activo, sin cargo por Microsoft 365 Copilot; ámbitos adaptables y versión exacta del documento compartido con nivel E5 |
| Enterprise AI apps | Apps registradas en Entra, ChatGPT Enterprise y Microsoft Foundry | Directiva de recopilación con captura de contenido | Pago por uso; para agentes de Microsoft Foundry y apps de IA conectadas a Entra, Microsoft 365 E7 o SKU de Agent 365 según la descripción del servicio |
| Other AI apps | Apps de IA de consumo, como ChatGPT, Gemini, Copilot para consumidores o DeepSeek | Directiva de recopilación con captura de contenido | Pago por uso |

Fuentes: [retención para Copilot e IA](https://learn.microsoft.com/en-us/purview/retention-policies-copilot), [directivas de recopilación](https://learn.microsoft.com/en-us/purview/collection-policies-solution-overview), [primeros pasos con DLM](https://learn.microsoft.com/en-us/purview/get-started-with-data-lifecycle-management) y [descripción del servicio](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description). En todas: los elementos se guardan en una carpeta oculta del buzón y un hold suspende la eliminación.

### Documentación, cursos y credenciales

- [Learn about retention for Copilot & AI apps](https://learn.microsoft.com/en-us/purview/retention-policies-copilot) · Documentación · Oficial · Microsoft Learn. Describe las ubicaciones separadas Microsoft Copilot experiences, Enterprise AI apps y Other AI apps, el almacenamiento en carpeta oculta del buzón, SubstrateHolds y el temporizador de 1-7 días.
- [Collection Policies solution overview](https://learn.microsoft.com/en-us/purview/collection-policies-solution-overview) · Documentación · Oficial · Microsoft Learn. Explica las directivas de recopilación que filtran eventos y habilitan la captura de prompts y respuestas de IA (Copilot, IA empresarial y apps no administradas), requisito previo para retenerlos con DLM.
- [Create and deploy collection policies](https://learn.microsoft.com/en-us/purview/collection-policies-create-deploy-policy) · Documentación · Oficial · Microsoft Learn. Escenarios de creación de directivas de recopilación, roles requeridos y modelo de facturación por uso o por usuario con seguimiento en el Usage center.

### Anuncios y blogs oficiales

- [New M365 Copilot Data Lifecycle Management options](https://techcommunity.microsoft.com/blog/microsoft-security-blog/new-m365-copilot-data-lifecycle-management-options/4304636) · Blog oficial · Empleado de Microsoft · Legado aún útil · EricaToelle · Microsoft Tech Community (Microsoft Security Community Blog) · 19 nov 2024. Anuncio de la ubicación de directiva dedicada a Microsoft Copilot experiences, separada de chats de Teams, y de cómo migrar desde la ubicación combinada. *Nota:* Anuncio de Ignite 2024; hoy la lista de ubicaciones se amplió a Enterprise AI apps y Other AI apps. Incluye enlaces cortos oficiales (Ninja, roadmap, blog)

**Manos a la obra**

1. `Laboratorio parcial` Con el pago por uso habilitado en [P0](01_Nivel_1_Inicial.md#p0), crea una directiva de solo retener (1 año) para la ubicación Microsoft Copilot experiences con un ámbito adaptable piloto ([retención para Copilot e IA](https://learn.microsoft.com/en-us/purview/retention-policies-copilot)). Limitación: la prueba de E5 no incluye Microsoft 365 Copilot, así que sin licencias no habrá interacciones que verificar; el anexo de entorno de práctica explica qué complementos admite el sandbox de desarrollador. Evidencia: directiva creada con su ámbito y sus ubicaciones.
2. `Laboratorio parcial` Crea una directiva de recopilación con captura de contenido para una app de la ubicación Other AI apps y, después, una directiva de retención para esa ubicación ([crear directivas de recopilación](https://learn.microsoft.com/en-us/purview/collection-policies-create-deploy-policy)). Limitación: requiere pago por uso y una app que genere interacciones capturables en tu laboratorio. Evidencia: ambas directivas y, si hubo interacciones, el resultado de una búsqueda.
3. `Laboratorio parcial` Con un usuario piloto con licencia de Microsoft 365 Copilot, genera interacciones, búscalas con eDiscovery y coloca un hold para comprobar que suspende la eliminación ([buscar datos de Copilot](https://learn.microsoft.com/en-us/purview/edisc-search-copilot-data)). Limitación: requiere licencias pagas de Copilot, que la prueba de E5 no incluye. Evidencia: resultados de la búsqueda antes y después del período.
4. `Laboratorio` Diseña con Legal y privacidad la matriz de decisión para IA: cuánto conservar prompts y respuestas por población (dirección, áreas reguladas y resto), qué ubicaciones cubrir, qué excepciones admitir y qué ocurre ante un litigio. Evidencia: matriz aprobada con su justificación.
5. `Laboratorio` Estima y controla el costo: con los [modelos de facturación](https://learn.microsoft.com/en-us/purview/purview-billing-models) y el [uso facturable](https://learn.microsoft.com/en-us/purview/purview-billing-usage) de Purview, identifica qué medidores afectan a tus directivas de IA y configura en Azure un presupuesto con alertas. Evidencia: ficha de costos y presupuesto configurado.
6. `Solo producción` Despliega la retención de interacciones de IA para la organización. Cómo hacerlo seguro: empieza con una directiva de solo retener y un ámbito adaptable para un grupo piloto, verifica por eDiscovery, obtén la aprobación de privacidad para los plazos antes de agregar una acción de eliminación, comunica la medida a los usuarios y revisa la decisión cada año. Evidencia: aprobación de privacidad, resultados del piloto y plan de ampliación.

<a id="a2"></a>

## A2 · Automatización y APIs de registros: Microsoft Graph, PowerShell y Power Automate

*L400 · ~5 h · Origen: Ninja oficial de ciclo de vida y registros (2023): Power Automate, ampliado con Microsoft Graph y PowerShell*

Un plan de archivos con decenas o cientos de etiquetas no se mantiene a mano. **Microsoft Graph** v1.0 expone en el espacio de nombres `microsoft.graph.security` los recursos `retentionLabel`, `filePlanDescriptor`, `retentionEvent` y `retentionEventType`: puedes leer y crear etiquetas con su comportamiento (retener, registro o registro regulatorio), su disparador, sus etapas de revisión de eliminación y su reetiquetado, y disparar eventos desde un sistema de recursos humanos o un ERP.

**PowerShell** sigue siendo la vía para operaciones masivas: `New-ComplianceTag` y `New-RetentionCompliancePolicy` crean y publican etiquetas desde CSV (el script de ejemplo de Microsoft no tiene soporte y no cubre la autoaplicación), y `Get-AdaptiveScopeMembers`, que documenta la comunidad, reporta la membresía de los ámbitos adaptables. Desde agosto de 2026 la autenticación solo de aplicación para los cmdlets de eDiscovery no tiene soporte: Microsoft recomienda migrar esas automatizaciones a Graph.

Al final del período, una etiqueta puede ejecutar un flujo de **Power Automate** para notificar, mover a un archivo central, reetiquetar o eliminar, con límites claros: solo en etiquetas nuevas, el flujo debe estar en «My flows» (no en Solutions) y no puede reetiquetar a registro regulatorio.

**Por qué importa**

Versionar el plan de archivos como código da trazabilidad ante auditoría, permite revisar cambios por pares y repetir despliegues entre el tenant de prueba y el de producción. Automatizar eventos y reportes elimina trabajo manual propenso a errores, que es donde suelen nacer las eliminaciones indebidas y la deuda de retención.

**Qué vas a lograr**

- Consultar y crear etiquetas, descriptores y eventos con Microsoft Graph.
- Crear y publicar etiquetas en masa con PowerShell desde un CSV.
- Configurar un flujo de Power Automate al final del período de retención.
- Reportar la membresía de los ámbitos adaptables por script.
- Aplicar mínimo privilegio y control de cambios a la automatización.

> **Novedad.** Microsoft Graph v1.0 expone `retentionLabel`, `filePlanDescriptor`, `retentionEvent` y `retentionEventType` en el espacio de nombres `microsoft.graph.security` ([API de registros](https://learn.microsoft.com/en-us/graph/api/resources/security-recordsmanagement-overview?view=graph-rest-1.0)). Con `retentionLabel` defines el comportamiento, el disparador, las etapas de revisión de eliminación y el reetiquetado ([retentionLabel](https://learn.microsoft.com/en-us/graph/api/resources/security-retentionlabel?view=graph-rest-1.0)).

> **Qué cambió.** Desde agosto de 2026, la autenticación solo de aplicación para los cmdlets de eDiscovery no tiene soporte y Microsoft recomienda migrar esas automatizaciones a Graph ([novedades](https://learn.microsoft.com/en-us/purview/whats-new)). Para auditoría, `Search-UnifiedAuditLog` se retira el 15 de octubre de 2027 y la API AuditLogQuery de Graph está disponible en general desde octubre de 2026 ([MC1505599](https://mc.merill.net/message/MC1505599)).

> **Atención.** Power Automate al final del período tiene límites claros: solo en etiquetas nuevas, el flujo debe estar en «My flows» (no en Solutions) y no puede reetiquetar a registro regulatorio ([flujo al final de la retención](https://learn.microsoft.com/en-us/purview/retention-label-flow)). El script de creación masiva con `New-ComplianceTag` y `New-RetentionCompliancePolicy` es un ejemplo sin soporte que no cubre la autoaplicación ([creación masiva](https://learn.microsoft.com/en-us/purview/bulk-create-publish-labels-using-powershell)).

> **Consejo Ninja.** Para reportar la membresía de los ámbitos adaptables, Microsoft 365 for IT Pros documenta `Get-AdaptiveScopeMembers`, junto con otros scripts de cumplimiento ([categoría Compliance](https://office365itpros.com/category/compliance/)). Contrasta su salida con la vista del portal antes de basar decisiones en ella.

**¿Tienes poco tiempo?**

- [Use the Microsoft Graph records management APIs](https://learn.microsoft.com/en-us/graph/api/resources/security-recordsmanagement-overview?view=graph-rest-1.0) · Documentación
- [Create and publish retention labels by using PowerShell](https://learn.microsoft.com/en-us/purview/bulk-create-publish-labels-using-powershell) · Documentación
- [Customize what happens at the end of the retention period (Power Automate)](https://learn.microsoft.com/en-us/purview/retention-label-flow) · Documentación

**Herramientas para automatizar retención y registros**

| Herramienta | Úsala para | Límites conocidos | Fuente |
|---|---|---|---|
| Microsoft Graph · API de registros (v1.0) | Leer y crear etiquetas, descriptores del plan de archivos, tipos de evento y eventos desde sistemas de origen | App con permisos de Records Management; los eventos tardan hasta 7 días en sincronizarse | [API de registros](https://learn.microsoft.com/en-us/graph/api/resources/security-recordsmanagement-overview?view=graph-rest-1.0) |
| Security & Compliance PowerShell (`New-ComplianceTag`, `New-RetentionCompliancePolicy`) | Crear y publicar etiquetas en masa desde CSV e inventariar la configuración | El script de ejemplo no tiene soporte y no cubre la autoaplicación | [Creación masiva](https://learn.microsoft.com/en-us/purview/bulk-create-publish-labels-using-powershell) |
| Power Automate al final del período | Notificar, mover a un archivo central, reetiquetar o eliminar | Solo etiquetas nuevas; flujo en «My flows»; no reetiqueta a registro regulatorio | [Flujo al final de la retención](https://learn.microsoft.com/en-us/purview/retention-label-flow) |
| `Get-AdaptiveScopeMembers` | Reportar la membresía de los ámbitos adaptables | Documentado por la comunidad: contrasta con el portal | [Microsoft 365 for IT Pros](https://office365itpros.com/category/compliance/) |
| API AuditLogQuery de Microsoft Graph | Métricas y evidencias de auditoría por script | Disponible en general desde octubre de 2026; reemplaza a `Search-UnifiedAuditLog`, que se retira el 15 de octubre de 2027 | [MC1505599](https://mc.merill.net/message/MC1505599) |
| Cmdlets de eDiscovery con autenticación solo de aplicación | Nada nuevo: migra lo existente | Sin soporte desde agosto de 2026; Microsoft recomienda Graph | [Novedades de Purview](https://learn.microsoft.com/en-us/purview/whats-new) |

Datos al 6 de noviembre de 2026. La automatización de eDiscovery y Audit se profundiza en el programa de eDiscovery y Audit, módulo A2.

### Documentación, cursos y credenciales

- [Use the Microsoft Graph records management APIs](https://learn.microsoft.com/en-us/graph/api/resources/security-recordsmanagement-overview?view=graph-rest-1.0) · Documentación · Oficial · Microsoft Learn (Microsoft Graph) · 10 jun 2024. Visión general de las API de Graph para etiquetas de retención, descriptores de plan de archivos, eventos y tipos de evento, con el ejemplo de integración con RR. HH. por AssetID.
- [retentionLabel resource type (Microsoft Graph v1.0)](https://learn.microsoft.com/en-us/graph/api/resources/security-retentionlabel?view=graph-rest-1.0) · Documentación · Oficial · Microsoft Learn (Microsoft Graph). Referencia del recurso retentionLabel con propiedades de comportamiento (retener, registro, registro regulatorio), disparador (fecha de evento), etapas de revisión de eliminación y reetiquetado.
- [Customize what happens at the end of the retention period (Power Automate)](https://learn.microsoft.com/en-us/purview/retention-label-flow) · Documentación · Oficial · Microsoft Learn. Cómo configurar una etiqueta que ejecuta un flujo de Power Automate al final de la retención para notificar, mover a un archivo central, reetiquetar o eliminar.
- [Create and publish retention labels by using PowerShell](https://learn.microsoft.com/en-us/purview/bulk-create-publish-labels-using-powershell) · Documentación · Oficial · Microsoft Learn. Plantillas CSV y script de ejemplo (New-ComplianceTag, New-RetentionCompliancePolicy) para crear y publicar etiquetas y directivas de etiquetas en masa.

### Comunidad: blogs, libros, newsletters y eventos

- [Compliance Archives - Microsoft 365 for IT Pros](https://office365itpros.com/category/compliance/) · Blog · MVP · Nuevo · Tony Redmond · Microsoft 365 for IT Pros (office365itpros.com) · 20 ago 2026. Archivo de artículos de cumplimiento con scripts PowerShell (p. ej., Get-AdaptiveScopeMembers, eliminación de holds en buzones inactivos) y análisis críticos de novedades de DLM.

**Manos a la obra**

1. `Laboratorio` Registra una app en Entra ID con el permiso de aplicación `RecordsManagement.Read.All`, obtén un token y lista las etiquetas con `GET /security/labels/retentionLabels` en Microsoft Graph v1.0 ([API de registros](https://learn.microsoft.com/en-us/graph/api/resources/security-recordsmanagement-overview?view=graph-rest-1.0)). Evidencia: JSON con las etiquetas de tu plan de archivos.
2. `Laboratorio parcial` Crea por Graph un `retentionEventType` y una etiqueta con `retentionTrigger` igual a `dateOfEvent`; aplícala a un documento con ID de activo y dispara un `retentionEvent` con `eventQueries` sobre ese ID ([retentionLabel](https://learn.microsoft.com/en-us/graph/api/resources/security-retentionlabel?view=graph-rest-1.0)). Limitación: la app necesita permisos de escritura de Records Management y el evento tarda hasta 7 días en sincronizarse. Evidencia: respuestas de la API y estado del evento en el portal.
3. `Laboratorio` Adapta el script de ejemplo para crear cinco etiquetas y una directiva de publicación desde CSV con `New-ComplianceTag` y `New-RetentionCompliancePolicy`, y ejecútalo primero en el tenant de prueba ([creación masiva con PowerShell](https://learn.microsoft.com/en-us/purview/bulk-create-publish-labels-using-powershell)). Evidencia: salida del script y etiquetas visibles en el plan de archivos.
4. `Laboratorio` Plan de archivos como código: guarda en un repositorio Git la exportación de etiquetas y descriptores, propón un cambio mediante una solicitud revisada por un par y aplícalo con tu script. Evidencia: historial de cambios con la revisión y la etiqueta actualizada en el portal.
5. `Laboratorio parcial` Crea una etiqueta nueva cuya acción final ejecute un flujo de Power Automate guardado en «My flows», que notifique al dueño y registre el elemento en una lista ([flujo al final de la retención](https://learn.microsoft.com/en-us/purview/retention-label-flow)). Limitación: el flujo solo se dispara al final del período (usa 1 día, con temporizadores de hasta 7 días); verifica en tu tenant los requisitos de licencia del conector. Evidencia: historial de ejecución del flujo.
6. `Laboratorio` Reporta por PowerShell la membresía de un ámbito adaptable con `Get-AdaptiveScopeMembers`, según lo documenta [Microsoft 365 for IT Pros](https://office365itpros.com/category/compliance/), y compárala con la vista del portal. Evidencia: CSV de miembros y lista de diferencias.
7. `Solo producción` Integra la automatización con sistemas reales (recursos humanos, ERP o gestión de contratos). Cómo hacerlo seguro: una app por integración con permisos mínimos y autenticación por certificado, ejecución primero contra etiquetas de prueba sin eliminación, registro de cada llamada, revisión por pares de cada cambio y migración a Graph de toda automatización de eDiscovery con autenticación solo de aplicación. Evidencia: inventario de apps con permisos y responsables, y bitácora de la primera ejecución.

**¿Quieres profundizar?**

- [Compliance Archives - Microsoft 365 for IT Pros](https://office365itpros.com/category/compliance/) · Blog

<a id="a3"></a>

## A3 · Integración con retenciones legales y eDiscovery

*L400 · ~3 h · Origen: Nuevo en esta edición (se apoya en los principios de retención del Ninja de 2023)*

La retención y las retenciones legales (holds) conviven, y el primer principio decide: retener gana sobre eliminar. Un hold de eDiscovery suspende cualquier eliminación de directivas o etiquetas, incluida la de Teams, Viva Engage y Copilot en SubstrateHolds. Un hold puede tardar hasta 24 horas en aplicarse y toma la membresía de los grupos como una instantánea al crearlo. Desde el 16 de febrero de 2026 las búsquedas de contenido se limitan a buscar y exportar: los holds requieren un caso completo en la experiencia unificada de eDiscovery, que reemplazó a la clásica en agosto de 2025.

Hay interacciones que sorprenden. Si un hold de eDiscovery es lo único que mantiene un buzón inactivo y el caso se cierra o el hold se libera, el buzón inactivo se elimina; desde agosto de 2026, después de un delay hold de 30 días. En la migración de canales privados de Teams, las versiones retenidas antes de la migración no se mueven y quedan en los buzones de los usuarios. Y si operas por país o subsidiaria, los **límites de cumplimiento** restringen las búsquedas por atributo.

La regla de oro: la retención no reemplaza al hold legal, ni el hold reemplaza a la retención. Legal es dueño de los holds; el equipo de registros, de la retención. Este módulo construye el procedimiento conjunto; los holds en detalle se profundizan en el programa de eDiscovery y Audit, módulo M1.

**Por qué importa**

Los incidentes más graves en este terreno son destruir contenido sujeto a una obligación de preservación o cerrar un caso que, sin que nadie lo note, elimina buzones inactivos. Un procedimiento conjunto entre Legal y registros, con verificación previa a cada liberación, reduce el riesgo de sanciones y protege la evidencia.

**Qué vas a lograr**

- Explicar cómo interactúan los holds de eDiscovery con directivas y etiquetas según los principios de retención.
- Prever el efecto de cerrar un caso sobre buzones inactivos y contenido en SubstrateHolds.
- Diseñar un procedimiento conjunto entre Legal y registros para liberar holds.
- Usar límites de cumplimiento para operar por país o subsidiaria.

> **Atención.** Si un hold de eDiscovery es lo único que mantiene un buzón inactivo y se libera o se cierra el caso, el buzón inactivo se elimina ([duración del hold de buzones inactivos](https://learn.microsoft.com/en-us/purview/change-the-hold-duration-for-an-inactive-mailbox)); desde agosto de 2026, después de un delay hold de 30 días ([novedades](https://learn.microsoft.com/en-us/purview/whats-new)).

> **Qué cambió.** Desde el 16 de febrero de 2026, las búsquedas de contenido se limitan a buscar y exportar: los holds requieren un caso completo ([Microsoft 365 for IT Pros](https://office365itpros.com/2026/01/15/content-searches-change/)). La experiencia clásica de eDiscovery se retiró en agosto de 2025 ([webinar de la transición](https://www.youtube.com/watch?v=bmpY8QRmBnw)).

> **Atención.** Un hold puede tardar hasta 24 horas en aplicarse y toma la membresía de los grupos como una instantánea al crearlo: quienes se sumen después no quedan retenidos ([crear un hold](https://learn.microsoft.com/en-us/purview/edisc-hold-create)). Revisa la membresía de los holds de grupos con cada alta relevante.

> **Consejo Ninja.** En la migración de canales privados, las versiones retenidas antes de migrar no se mueven y quedan en los buzones de los usuarios; tenlo en cuenta en búsquedas y holds sobre períodos anteriores ([modelo de cumplimiento de canales privados](https://techcommunity.microsoft.com/blog/microsoft-security-blog/teams-private-channels-group-based-compliance-model--purview-ediscovery-consider/4457229)).

**¿Tienes poco tiempo?**

- [Change the hold duration for an inactive mailbox](https://learn.microsoft.com/en-us/purview/change-the-hold-duration-for-an-inactive-mailbox) · Documentación
- [Teams Private Channels: Group-Based Compliance Model & Purview eDiscovery Considerations](https://techcommunity.microsoft.com/blog/microsoft-security-blog/teams-private-channels-group-based-compliance-model--purview-ediscovery-consider/4457229) · Blog oficial
- [Set up compliance boundaries in eDiscovery](https://learn.microsoft.com/en-us/purview/edisc-compliance-boundaries) · Documentación

### Documentación, cursos y credenciales

- [Change the hold duration for an inactive mailbox](https://learn.microsoft.com/en-us/purview/change-the-hold-duration-for-an-inactive-mailbox) · Documentación · Oficial · Microsoft Learn. Cómo identificar con PowerShell los tipos de hold de un buzón inactivo y cambiar su duración, advirtiendo que cerrar un caso de eDiscovery puede eliminar el buzón inactivo.
- [Set up compliance boundaries in eDiscovery](https://learn.microsoft.com/en-us/purview/edisc-compliance-boundaries) · Documentación · Oficial · Microsoft Learn. Cómo crear límites de cumplimiento con filtros de permisos de búsqueda por atributo para subsidiarias o países, aplicables también a Data Security Investigations.

### Anuncios y blogs oficiales

- [Teams Private Channels: Group-Based Compliance Model & Purview eDiscovery Considerations](https://techcommunity.microsoft.com/blog/microsoft-security-blog/teams-private-channels-group-based-compliance-model--purview-ediscovery-consider/4457229) · Blog oficial · Empleado de Microsoft · Alastair_Sharp_MS · Microsoft Tech Community (Microsoft Security Community Blog) · 30 sep 2025. Explica el impacto del nuevo modelo de canales privados en búsquedas y retenciones legales, incluido que las versiones retenidas previas no migran del buzón del usuario.

### Webinars, videos y podcasts

- [eDiscovery New User Experience and Retirement of Classic (webinar)](https://www.youtube.com/watch?v=bmpY8QRmBnw) · Webinar · Empleado de Microsoft · David Robbins, John Wirtala, Alastair Sharp · Microsoft Security Community (YouTube) · 22 abr 2025. Explica la nueva experiencia unificada de eDiscovery y la creación de holds, necesaria para entender la convivencia entre retenciones legales y retención de Purview.

**Manos a la obra**

1. `Laboratorio` En el sitio piloto, aplica una directiva de solo eliminar a 1 día, coloca un hold de eDiscovery sobre el mismo sitio en un caso de prueba, borra un documento y verifica, una semana después, que sigue en la biblioteca de conservación ([crear un hold](https://learn.microsoft.com/en-us/purview/edisc-hold-create)). Evidencia: captura del documento conservado y del hold activo.
2. `Laboratorio` Con un hold sobre un usuario de prueba, borra mensajes de chat de Teams y verifica con eDiscovery que siguen disponibles, porque el hold suspende la eliminación en SubstrateHolds ([retención en Teams](https://learn.microsoft.com/en-us/purview/retention-policies-teams)). Evidencia: resultados de la búsqueda.
3. `Laboratorio` Crea un buzón inactivo retenido solo por un hold de eDiscovery (sin directiva de retención), confirma con `Get-Mailbox -InactiveMailboxOnly | Format-List DisplayName,InPlaceHolds` qué lo retiene y documenta qué ocurriría al cerrar el caso ([duración del hold de buzones inactivos](https://learn.microsoft.com/en-us/purview/change-the-hold-duration-for-an-inactive-mailbox)). Evidencia: salida del cmdlet y nota de impacto.
4. `Laboratorio` Escribe con Legal el checklist de liberación de holds: listar los buzones inactivos y el contenido de Teams, Viva Engage y Copilot que dependen del hold, verificar si alguna directiva los cubre, aprobar la liberación y comunicarla, contando con el delay hold de 30 días como ventana de corrección. Evidencia: checklist aprobado por Legal y por el gestor de registros.
5. `Laboratorio parcial` Configura límites de cumplimiento para dos países ficticios con un atributo de usuario y filtros de permisos de búsqueda (`New-ComplianceSecurityFilter`), y verifica que cada gestor de eDiscovery solo ve su país ([límites de cumplimiento](https://learn.microsoft.com/en-us/purview/edisc-compliance-boundaries)). Limitación: el atributo puede tardar en reflejarse en OneDrive y SharePoint, así que valida después de unos días. Evidencia: resultados de búsqueda de ambos gestores.
6. `Solo producción` Revisa con Legal los casos abiertos y los buzones inactivos que dependen de ellos. Cómo hacerlo seguro: usa roles de solo lectura para el inventario, no liberes ningún hold sin el checklist aprobado, ensaya cada liberación sobre un caso de prueba y deja constancia de cada decisión. Evidencia: inventario trimestral y actas de liberación.

**¿Quieres profundizar?**

- [eDiscovery New User Experience and Retirement of Classic (webinar)](https://www.youtube.com/watch?v=bmpY8QRmBnw) · Webinar

<a id="a4"></a>

## A4 · Requisitos regulatorios, inmutabilidad y Multi-Geo

*L400 · ~3 h · Origen: Nuevo en esta edición*

Microsoft no certifica que cumplas una ley: publica evaluaciones independientes que muestran cómo configurar Microsoft 365 para requisitos de registros. Cohasset evaluó la retención frente a SEC 17a-4(f), FINRA 4511(c) y CFTC 1.31 (julio de 2022) y frente a la Ley de Registros Públicos de Nueva Zelanda (enero de 2021). Esas evaluaciones describen los controles de inmutabilidad —registros regulatorios y Preservation Lock— que también sirven de referencia ante supervisores de la región, aunque no hay evaluaciones específicas para países de MCSA.

En la región, la retención documental suele nacer de leyes de archivos: la **Ley General de Archivos** de México (DOF del 15 de junio de 2018, última reforma del 14 de noviembre de 2025), para sujetos obligados y para quienes reciben recursos públicos, o la **Ley 594 de 2000** de Colombia, que define la tabla de retención documental (TRD). Tu trabajo técnico es trazar requisito, control y evidencia; la interpretación corresponde a Legal.

En un tenant **Multi-Geo** hay un único portal de Purview y las directivas de retención se gestionan de forma central; para eDiscovery en ubicaciones satélite se usa el filtro de seguridad «Region», con México (MEX), Brasil (BRA) y Chile (CHL) disponibles.

**Por qué importa**

Bancos, aseguradoras y organismos públicos deben demostrar que conservan registros inmutables durante el plazo exigido y que los eliminan según su tabla de retención. Una matriz de requisito, control y evidencia validada por Legal acelera auditorías y conversaciones con supervisores, y evita que decisiones que en realidad son interpretaciones legales se tomen como decisiones técnicas.

**Qué vas a lograr**

- Usar las evaluaciones de terceros para diseñar registros inmutables.
- Explicar cómo se gestionan la retención y eDiscovery en un tenant Multi-Geo.
- Trasladar una tabla de retención documental regional a un plan de archivos, con validación de Legal.
- Documentar la trazabilidad entre requisito, control y evidencia sin interpretar la ley.

> **Novedad.** Microsoft publica evaluaciones de terceros sobre la retención de Microsoft 365: Cohasset la evaluó frente a SEC 17a-4(f), FINRA 4511(c) y CFTC 1.31 (julio de 2022) y frente a la Ley de Registros Públicos de Nueva Zelanda (enero de 2021) ([requisitos regulatorios](https://learn.microsoft.com/en-us/purview/retention-regulatory-requirements)). La investigación no encontró evaluaciones equivalentes para países de MCSA.

> **Atención.** Preservation Lock es irreversible: nadie, ni siquiera el administrador global, puede desactivar ni eliminar la directiva bloqueada, que en adelante solo puede ampliarse ([Preservation Lock](https://learn.microsoft.com/en-us/purview/retention-preservation-lock)). Úsalo solo ante un requisito regulatorio documentado y aprobado por Legal.

> **Consejo Ninja.** En Multi-Geo hay un único portal de Purview; para eDiscovery en ubicaciones satélite se usa el filtro de seguridad «Region», con México (MEX), Brasil (BRA) y Chile (CHL) entre las disponibles ([eDiscovery en Multi-Geo](https://learn.microsoft.com/en-us/microsoft-365/enterprise/multi-geo-ediscovery-configuration?view=o365-worldwide), [servicios en Multi-Geo](https://learn.microsoft.com/en-us/microsoft-365/enterprise/administering-a-multi-geo-environment?view=o365-worldwide)).

> **Atención.** Leyes de archivos en la región: la Ley General de Archivos de México (DOF del 15 de junio de 2018) tuvo su última reforma el 14 de noviembre de 2025 ([texto vigente](https://www.diputados.gob.mx/LeyesBiblio/pdf/LGA.pdf)), y en Colombia la Ley 594 de 2000 define la tabla de retención documental ([Ley 594](https://www1.funcionpublica.gov.co/eva//gestornormativo/norma.php?i=4275)). Su interpretación corresponde a Legal y al área de archivo, no al equipo técnico.

**¿Tienes poco tiempo?**

- [Resources to help you meet regulatory requirements for data lifecycle management and records management](https://learn.microsoft.com/en-us/purview/retention-regulatory-requirements) · Documentación
- [Microsoft 365 Multi-Geo eDiscovery configuration](https://learn.microsoft.com/en-us/microsoft-365/enterprise/multi-geo-ediscovery-configuration?view=o365-worldwide) · Documentación

### Documentación, cursos y credenciales

- [Microsoft 365 Multi-Geo eDiscovery configuration](https://learn.microsoft.com/en-us/microsoft-365/enterprise/multi-geo-ediscovery-configuration?view=o365-worldwide) · Documentación · Oficial · Microsoft Learn · 11 dic 2025. Explica el filtro de seguridad 'Region' para eDiscovery en ubicaciones satélite (incluye México MEX, Brasil BRA y Chile CHL) y cuándo se requieren funciones premium.
- [Resources to help you meet regulatory requirements for data lifecycle management and records management](https://learn.microsoft.com/en-us/purview/retention-regulatory-requirements) · Documentación · Oficial · Legado aún útil · Microsoft Learn · 26 sep 2025. Reúne evaluaciones de terceros (Cohasset para SEC 17a-4(f), FINRA 4511(c), CFTC 1.31 y la Ley de Registros Públicos de Nueva Zelanda) sobre cómo configurar Microsoft 365 para registros inmutables. *Nota:* La evaluación Cohasset es de julio de 2022; no hay evaluaciones específicas para países de MCSA
- [Service behavior in a Multi-Geo enabled environment](https://learn.microsoft.com/en-us/microsoft-365/enterprise/administering-a-multi-geo-environment?view=o365-worldwide) · Documentación · Oficial · Microsoft Learn. Describe que en Multi-Geo hay un único portal de Purview y cómo se comportan auditoría, eDiscovery, buzones y cuotas de SharePoint por geografía.

**Manos a la obra**

1. `Laboratorio` Lee las evaluaciones de terceros enlazadas en [requisitos regulatorios](https://learn.microsoft.com/en-us/purview/retention-regulatory-requirements) y arma una matriz requisito–control–evidencia para un requisito de inmutabilidad: registro regulatorio, Preservation Lock, auditoría y prueba de eliminación. Evidencia: matriz con la fuente de cada control.
2. `Laboratorio parcial` Solo en un tenant desechable, bloquea una directiva de prueba con `Set-RetentionCompliancePolicy -Identity Prueba-Lock -RestrictiveRetention $true` y comprueba que ya no puedes desactivarla, eliminarla ni acortar su período ([Preservation Lock](https://learn.microsoft.com/en-us/purview/retention-preservation-lock)). Limitación: es irreversible; nunca lo hagas en producción ni en el tenant que seguirás usando. Evidencia: capturas de los intentos rechazados.
3. `Laboratorio` Traslada tres series de una tabla de retención documental regional a etiquetas del plan de archivos, con la norma en el descriptor de cita y la aprobación de Legal registrada; por ejemplo, desde la [Ley General de Archivos de México](https://www.diputados.gob.mx/LeyesBiblio/pdf/LGA.pdf) o la tabla de retención documental de la [Ley 594 de 2000 de Colombia](https://www1.funcionpublica.gov.co/eva//gestornormativo/norma.php?i=4275). Evidencia: exportación del plan de archivos con descriptores y aprobación.
4. `Laboratorio` Prepara una ficha para el supervisor o el auditor: qué controles de Purview usas, qué evidencias entregas, qué no cubre la plataforma (Microsoft no certifica tu cumplimiento) y quién interpreta la norma. Evidencia: ficha revisada por Legal.
5. `Solo producción` Multi-Geo: inventaría en qué geografía están los datos de cada país y configura eDiscovery por región. Cómo hacerlo seguro: requiere un tenant con ubicaciones satélite; trabaja con roles de solo lectura para el inventario, prueba el filtro «Region» con un gestor de eDiscovery de prueba y no cambies la ubicación de datos preferida de nadie sin control de cambios ([eDiscovery en Multi-Geo](https://learn.microsoft.com/en-us/microsoft-365/enterprise/multi-geo-ediscovery-configuration?view=o365-worldwide)). Evidencia: inventario por geografía y resultado de la prueba del filtro.

<a id="reto-avanzado"></a>

## Reto del nivel

**Plan de archivos como código y decisiones de IA con Legal.** Entrega un repositorio con: (1) la exportación de etiquetas y descriptores por Graph y el script de PowerShell que los despliega en un tenant limpio; (2) un tipo de evento y un evento creados por Graph, con su conciliación; (3) la directiva de retención para interacciones de Copilot e IA, con la matriz de decisión aprobada por Legal y privacidad y su costo estimado; (4) el checklist de liberación de holds probado con un buzón inactivo; y (5) una matriz requisito–control–evidencia para una norma de tu país, revisada por Legal. Criterio de éxito: alguien de tu equipo reproduce el plan de archivos en un tenant nuevo en menos de una hora.

<a id="quiz-avanzado"></a>

## Evaluación del nivel

Responde y compara con [Evaluaciones y respuestas](06_Evaluaciones_y_respuestas.md#eval-avanzado). Con 80 % o más, ¡nivel aprobado! (En la versión web puedes corregir en línea y generar tu certificado).

1. ¿Qué ubicaciones de retención exigen facturación de pago por uso?
   - a) Buzones de Exchange
   - b) Mensajes de Viva Engage
   - c) Microsoft Copilot experiences, Enterprise AI apps y Other AI apps
   - d) Chats de Teams

2. ¿Dónde se guardan los prompts y las respuestas de Copilot que conserva una directiva de retención?
   - a) En una carpeta oculta del buzón del usuario
   - b) En el OneDrive del usuario
   - c) En un sitio de SharePoint del tenant
   - d) En una cuenta de Azure Blob Storage del cliente

3. ¿Para qué interacciones de IA necesitas una directiva de recopilación con captura de contenido antes de poder retenerlas?
   - a) Para las de Microsoft 365 Copilot
   - b) Para las de Copilot Studio
   - c) Para ninguna: basta la directiva de retención
   - d) Para las de apps de IA distintas de Microsoft 365 Copilot y Copilot Studio, como ChatGPT Enterprise

4. ¿Qué combinación habilita ámbitos adaptables para la retención de Copilot y la retención de la versión exacta del documento compartido?
   - a) E3 + Microsoft 365 Copilot
   - b) E5 + Microsoft 365 Copilot, o E3 + Purview Suite o IP&G + Microsoft 365 Copilot
   - c) Solo Microsoft 365 E7
   - d) Business Premium + Copilot Chat

5. En un tenant Multi-Geo, ¿cómo se acota eDiscovery a una ubicación satélite como México?
   - a) Con un portal de Purview distinto por geografía
   - b) Con unidades administrativas en las directivas de etiquetas
   - c) Con el filtro de seguridad «Region» (por ejemplo, MEX)
   - d) No es posible acotarlo

6. En Microsoft Graph, ¿qué valor de `retentionTrigger` habilita la retención basada en eventos?
   - a) dateLabeled
   - b) dateCreated
   - c) dateModified
   - d) dateOfEvent

7. ¿Qué restricción tiene la acción de Power Automate al final del período de retención?
   - a) Solo funciona con registros regulatorios
   - b) Solo en etiquetas nuevas y con el flujo en «My flows», no en Solutions
   - c) Requiere Logic Apps Standard
   - d) Solo aplica a Exchange

8. Desde agosto de 2026, ¿qué recomienda Microsoft para las automatizaciones de eDiscovery que usan cmdlets con autenticación solo de aplicación?
   - a) Migrarlas a Microsoft Graph
   - b) Mantenerlas: siguen con soporte completo
   - c) Pasarlas a Power Automate
   - d) Ejecutarlas con una cuenta de administrador global

9. ¿Qué es cierto del script de ejemplo para crear y publicar etiquetas en masa con PowerShell?
   - a) Tiene soporte de Microsoft y cubre la autoaplicación
   - b) Solo funciona con Microsoft Graph
   - c) Es un ejemplo sin soporte y no cubre la autoaplicación
   - d) Requiere Power Automate

10. Un buzón inactivo se conserva solo por un hold de eDiscovery. ¿Qué ocurre si Legal cierra el caso?
   - a) Nada: el buzón inactivo se conserva para siempre
   - b) El buzón inactivo se elimina; desde agosto de 2026, después de un delay hold de 30 días
   - c) Se convierte en buzón compartido
   - d) Se exporta automáticamente a PST

11. Un documento tiene una etiqueta que lo elimina hoy y está bajo un hold de eDiscovery. ¿Qué ocurre?
   - a) Se elimina porque la etiqueta es explícita
   - b) Se mueve a Microsoft 365 Archive
   - c) Se elimina y queda una copia en la papelera
   - d) Se conserva mientras dure el hold, porque retener gana sobre eliminar

12. ¿Qué cambió el 16 de febrero de 2026 en las búsquedas de contenido?
   - a) Se retiraron por completo
   - b) Solo admiten buzones de Exchange
   - c) Pasaron a requerir Microsoft 365 E7
   - d) Se limitan a buscar y exportar; los holds requieren un caso

13. Creas un hold sobre un grupo y una semana después se suma un miembro nuevo. ¿Queda retenido su contenido?
   - a) No: la membresía se toma como instantánea al crear el hold
   - b) Sí: la membresía se actualiza a diario
   - c) Solo si tiene licencia E5
   - d) Solo su OneDrive

14. ¿Qué evaluación de terceros publica Microsoft sobre la retención de Microsoft 365?
   - a) Una certificación ISO 27701 emitida por BSI
   - b) Un informe SOC 2 tipo II
   - c) La de Cohasset frente a SEC 17a-4(f), FINRA 4511(c) y CFTC 1.31
   - d) Ninguna: Microsoft no publica evaluaciones

15. ¿Qué ocurre después de aplicar Preservation Lock a una directiva de retención?
   - a) Un administrador global puede desactivarla
   - b) No puede desactivarse ni eliminarse y solo puede ampliarse
   - c) Caduca a los 2 años
   - d) Se convierte en un hold de eDiscovery

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. No es asesoría legal: las decisiones de retención y eliminación deben validarse con Legal y privacidad. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

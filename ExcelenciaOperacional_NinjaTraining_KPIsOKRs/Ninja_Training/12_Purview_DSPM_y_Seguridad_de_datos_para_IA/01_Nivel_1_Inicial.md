# Nivel 1 · Inicial · Ver la postura y la exposición

*Microsoft Purview DSPM y seguridad de datos para IA Ninja Training · Edición 2026*

[← Programa](00_Programa.md) · [Índice del programa](README.md) · [Nivel 2 · Intermedio →](02_Nivel_2_Intermedio.md)

<a id="inicial"></a>

Purview y sus licencias, la DSPM unificada, la observabilidad de IA y las evaluaciones de sobreexposición. Terminas con DSPM configurada en tu laboratorio, una línea base de postura, un inventario de IA y una lista priorizada de sitios sobrecompartidos.

*L100–L200 · 5 módulos · ~17 horas · 28 recursos*

**Módulos de este nivel:** [P0 Prerrequisitos y licencias](#p0) · [I0 Cómo aprender](#i0) · [I1 DSPM hoy](#i1) · [I2 DSPM para IA](#i2) · [I3 Riesgo de datos y exposición](#i3)

<a id="p0"></a>

## P0 · Prerrequisitos: Microsoft Purview, el portal unificado y las licencias para DSPM

*L100–L200 · ~3 h · Origen: Nuevo en esta edición (la ruta Ninja oficial de Purview asume estos conocimientos)*

La gestión de la postura de seguridad de datos (DSPM, por sus siglas en inglés) vive en el **portal de Microsoft Purview**, en *Soluciones > DSPM*. Antes de abrirla conviene dominar tres bases. La primera es el **modelo de permisos** del portal: roles de Microsoft Entra, grupos de roles de Purview y unidades administrativas. La segunda son las **señales** que DSPM consume: tipos de información confidencial, etiquetas de confidencialidad, DLP, Insider Risk Management y auditoría. La tercera es el **licenciamiento**, que en seguridad de datos para IA es más complejo que en cualquier otra solución de Purview.

Purview combina dos modelos de facturación: **por usuario** (E3, E5, A5, F5 y G5) y **pago por uso** (PAYG) facturado en una suscripción de Azure. El pago por uso aplica a orígenes que no son Microsoft 365, a la red y a las apps y agentes de IA. La base de DSPM es **Microsoft 365 E5** o **Microsoft Purview Suite** (antes Microsoft 365 E5 Compliance) sobre E3. Para la IA se suman las licencias de **Microsoft 365 Copilot**, **Microsoft 365 E7** o **Agent 365** para los agentes, y el pago por uso para la IA de terceros. La regla de oro: necesita licencia todo usuario que se beneficia del servicio.

Desde la disponibilidad general de la experiencia unificada (mayo de 2026), las versiones anteriores aparecen como «DSPM (classic)» y «DSPM for AI (classic)» y se retiran a fines de enero de 2027. Si tu equipo aprendió con ellas, este módulo te ubica en el portal actual y en la terminología vigente.

**Por qué importa**

Los proyectos de seguridad de datos para IA suelen frenarse por licencias y permisos, no por tecnología. Pasa con políticas que no aplican porque falta Copilot, con consumo de pago por uso sin presupuesto y con administradores restringidos que no pueden crear políticas de un clic. También pasa con lectores de reportes que terminan viendo prompts con datos personales. Este módulo resuelve quién puede ver qué y qué paga quién antes de encender nada.

**Qué vas a lograr**

- Ubicar DSPM y las experiencias classic en el portal de Microsoft Purview.
- Diseñar una matriz de roles de mínimo privilegio que separe edición, lectura de reportes y lectura del contenido de prompts.
- Distinguir qué cubre Microsoft 365 E5 o Purview Suite, qué exige Microsoft 365 Copilot, qué exige E7 o Agent 365 y qué se cobra por uso.
- Explicar cómo afectan las unidades administrativas a DSPM y a las políticas de un clic.
- Activar la auditoría y el pago por uso con presupuesto y alertas.

> **Qué cambió.** Desde la disponibilidad general de la experiencia unificada (mayo de 2026), DSPM se abre en *Soluciones > DSPM* del portal de Purview y las versiones anteriores aparecen como «DSPM (classic)» y «DSPM for AI (classic)» ([DSPM](https://learn.microsoft.com/en-us/purview/data-security-posture-management-learn-about)). Microsoft 365 E5 Compliance ahora se llama **Microsoft Purview Suite** ([primeros pasos](https://learn.microsoft.com/en-us/purview/data-security-posture-management-get-started)).

> **Atención.** Necesita licencia todo usuario que se beneficia del servicio, incluidos quienes tienen roles de Purview y los dueños o miembros de sitios y grupos en ubicaciones compartidas; los visitantes no ([descripción del servicio](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)). Con unidades administrativas, los administradores restringidos solo ven datos de sus unidades y no pueden crear políticas de un clic ([consideraciones](https://learn.microsoft.com/en-us/purview/data-security-posture-management-considerations)).

> **Consejo Ninja.** Separa tres niveles de acceso: edición (por ejemplo, el grupo de roles Compliance Administrator), lectura de reportes (Data Security AI Viewer) y lectura del contenido de prompts y respuestas (AI Content Viewer). Usar Security Copilot en DSPM exige además el rol Data Security Viewer. La matriz completa, con los roles para Sentinel y DSI, está en [permisos de DSPM](https://learn.microsoft.com/en-us/purview/data-security-posture-management-permissions).

> **Novedad.** Microsoft publicó en abril de 2026 diagramas de arquitectura de referencia de Purview, actualizados el 9 de septiembre de 2026 con una arquitectura interactiva de clasificación y autoetiquetado. Sirven para explicar de dónde obtiene sus señales DSPM ([diagramas de referencia](https://techcommunity.microsoft.com/blog/microsoft-purview-blog/microsoft-purview-referential-architecture-diagrams/4510925)).

**¿Tienes poco tiempo?**

- [Permissions for Microsoft Purview Data Security Posture Management](https://learn.microsoft.com/en-us/purview/data-security-posture-management-permissions) · Documentación
- [Microsoft Purview service description](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description) · Documentación
- [Learn about Microsoft Purview billing models](https://learn.microsoft.com/en-us/purview/purview-billing-models) · Documentación
- [Microsoft Purview Referential Architecture Diagrams](https://techcommunity.microsoft.com/blog/microsoft-purview-blog/microsoft-purview-referential-architecture-diagrams/4510925) · Blog oficial

**Roles para DSPM y la seguridad de datos para IA**

| Tarea | Rol o grupo de roles | Notas | Fuente |
|---|---|---|---|
| Configurar DSPM y aceptar las tareas iniciales | Rol de Entra Compliance Administrator o grupo de roles Compliance Administrator de Purview | Ejemplo que cita Learn; revisa la matriz completa antes de asignar | [DSPM](https://learn.microsoft.com/en-us/purview/data-security-posture-management-learn-about) |
| Crear políticas de un clic cuando hay unidades administrativas | Administrador no restringido | Los administradores restringidos solo ven datos de sus unidades | [Consideraciones](https://learn.microsoft.com/en-us/purview/data-security-posture-management-considerations) |
| Ver informes de IA sin acceder al contenido | Data Security AI Viewer | Rol de solo lectura | [Permisos de DSPM](https://learn.microsoft.com/en-us/purview/data-security-posture-management-permissions) |
| Leer el contenido de prompts y respuestas | AI Content Viewer | Asígnalo solo con aprobación de privacidad y por tiempo limitado | [Permisos de DSPM](https://learn.microsoft.com/en-us/purview/data-security-posture-management-permissions) |
| Usar Security Copilot en DSPM | Data Security Viewer, además del acceso a Security Copilot | Security Copilot debe estar en el mismo inquilino | [DSPM](https://learn.microsoft.com/en-us/purview/data-security-posture-management-learn-about) |
| Configurar DLP para Copilot | Roles de DLP, como Purview Data Security AI Admin | Revisa la lista de roles en la página de DLP para Copilot | [DLP para Copilot](https://learn.microsoft.com/en-us/purview/dlp-microsoft365-copilot-location-learn-about) |
| Buscar interacciones de IA en eDiscovery | Grupo de roles eDiscovery Manager | Las interacciones se guardan en el buzón del usuario | [Buscar y eliminar datos de IA](https://learn.microsoft.com/en-us/purview/edisc-search-copilot-data) |
| Eliminar interacciones de IA con Graph Explorer | Rol Search And Purge | Máximo 10 elementos por buzón por ejecución | [Buscar y eliminar datos de IA](https://learn.microsoft.com/en-us/purview/edisc-search-copilot-data) |
| Ver el Security Dashboard for AI | Security Reader como mínimo | Reúne señales de Entra, Defender y Purview | [Security Dashboard for AI](https://learn.microsoft.com/en-us/security/security-for-ai/security-dashboard-for-ai) |
| Desplegar el Data Security Posture Agent | Roles según el nivel de visibilidad de contenido; identidad de agente recomendada | Requiere E5 con SCU aprovisionadas | [Posture Agent](https://learn.microsoft.com/en-us/purview/copilot-in-purview-posture-agent-get-started) |

Fuente principal: [permisos de DSPM](https://learn.microsoft.com/en-us/purview/data-security-posture-management-permissions) y [permisos del portal de Purview](https://learn.microsoft.com/en-us/purview/purview-permissions). Asigna roles a grupos y, si puedes, con activación temporal.

### Documentación, cursos y credenciales

- [Permissions for Microsoft Purview Data Security Posture Management](https://learn.microsoft.com/en-us/purview/data-security-posture-management-permissions) · Documentación · Oficial · Microsoft Learn. Matriz de permisos de la nueva DSPM: roles de edición, roles de solo lectura (Data Security AI Viewer, AI Content Viewer, Data Security Viewers) y roles adicionales para Security Copilot, Sentinel y DSI.
- [Microsoft Purview service description](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description) · Documentación · Oficial · Microsoft Learn (Service Descriptions). Descripción oficial de licencias de Purview por función (DLP para Copilot, DLP en navegador y red, Purview para cargas agénticas, IRM, auditoría) y reglas de quién necesita licencia.
- [Permissions in the Microsoft Purview portal](https://learn.microsoft.com/en-us/purview/purview-permissions) · Documentación · Oficial · Microsoft Learn. Explica el modelo RBAC del portal de Purview (roles, grupos de roles, roles de Entra, PIM para grupos) y enlaza permisos por solución, incluidos DSPM y agentes de triaje.

### Anuncios y blogs oficiales

- [Microsoft Purview Referential Architecture Diagrams](https://techcommunity.microsoft.com/blog/microsoft-purview-blog/microsoft-purview-referential-architecture-diagrams/4510925) · Blog oficial · Empleado de Microsoft · Maxime Bombardier · Microsoft Purview Blog (Tech Community) · 13 abr 2026. Diagramas de referencia de cómo fluyen clasificación, etiquetas, DLP e Insider Risk entre cargas de Microsoft 365, base para entender de dónde obtiene señales DSPM.

**Manos a la obra**

1. `Laboratorio` Activa la auditoría en tu prueba de Microsoft 365 E5 (en los inquilinos de prueba viene apagada) y verifícala con `Get-AdminAuditLogConfig | Format-List UnifiedAuditLogIngestionEnabled` en Exchange Online PowerShell ([activar la auditoría](https://learn.microsoft.com/en-us/purview/audit-log-enable-disable)). Evidencia: captura con el valor `True` y la fecha de activación.
2. `Laboratorio` Matriz de roles: asigna a tres cuentas de prueba el grupo de roles Compliance Administrator, el rol Data Security AI Viewer y el rol AI Content Viewer, e inicia sesión con cada una para documentar qué ve en DSPM ([permisos de DSPM](https://learn.microsoft.com/en-us/purview/data-security-posture-management-permissions)). Evidencia: tabla de tres filas con capturas.
3. `Laboratorio` Unidades administrativas: crea una unidad administrativa de prueba, asígnale un administrador restringido y comprueba que no puede crear políticas de un clic ([consideraciones](https://learn.microsoft.com/en-us/purview/data-security-posture-management-considerations)). Evidencia: captura del intento y nota en la matriz de roles.
4. `Laboratorio` Mapa de licencias: completa la tabla [Licencias](00_Programa.md#licencias) para tu organización, marca qué tienes (E3, E5, Purview Suite, Copilot, E7, Agent 365) y qué capacidades dependerían del pago por uso, usando la [descripción del servicio](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description). Evidencia: mapa revisado por el área de licenciamiento.
5. `Laboratorio parcial` Pago por uso: vincula el inquilino a una suscripción y un grupo de recursos de Azure del mismo inquilino (solo un Global Administrator puede hacerlo y el país queda fijo) y crea un presupuesto con alertas al 50, 75 y 90 % ([habilitar el pago por uso](https://learn.microsoft.com/en-us/purview/purview-payg-subscription-based-enablement)). Limitación: no está confirmado que el crédito de Visual Studio cubra los medidores de Purview, así que usa una suscripción separada. Evidencia: suscripción vinculada y presupuesto activo.

<a id="i0"></a>

## I0 · Cómo aprender DSPM y seguridad de datos para IA, y dónde pedir ayuda

*L100–L200 · ~2 h · Origen: Equivale a «Other learning and support options» de la familia Ninja; no existe un Ninja oficial de DSPM*

No existe un «Become a DSPM Ninja». La columna vertebral oficial está formada por tres rutas de Microsoft Learn. La primera es la **ruta Ninja de Purview** (escenarios de Information Protection y DLP), cuyo tercer módulo trata Security Copilot en Purview e incluye la investigación en DSPM. La segunda es la **ruta de la nueva DSPM** (4 módulos, 2 h 42 min). La tercera es la **ruta SC-401 sobre IA** (4 módulos, 3 h 30 min), también disponible en español. Este programa las ordena por niveles y les suma licencias, laboratorio, operación y el contexto de MCSA.

Si buscas una credencial, el examen **SC-401** (Information Security Administrator Associate) ya incluye proteger los datos que usan los servicios de IA. Para mantenerte al día, tu radar son el Message Center (los avisos MC sobre DSPM, Copilot y Agent 365), los blogs de Purview y de Microsoft Security, la etiqueta *dspm* de Tech Community y los webinars de la Microsoft Security Community. Ten cuidado con el material anterior a 2026: buena parte describe DSPM for AI (classic), que se retira en enero de 2027.

**Por qué importa**

Sin un Ninja oficial de DSPM, el riesgo es formar al equipo con material de la experiencia classic o con capturas de pantalla de 2024. Este módulo te da un plan de estudio vigente, una credencial reconocida y canales para resolver dudas. Así cada hora de formación se invierte en lo que aplica hoy y en lo que pedirá el examen.

**Qué vas a lograr**

- Combinar la ruta Ninja de Purview, la ruta de DSPM y la ruta SC-401 de IA con este programa.
- Planificar la certificación SC-401 con la guía de estudio del 28 de octubre de 2026.
- Distinguir el material vigente del que describe las experiencias classic.
- Suscribirte a las fuentes de novedades y a los canales de la comunidad.

> **Novedad.** La guía de estudio del SC-401 se actualizó el 28 de octubre de 2026 e incluye proteger los datos que usan los servicios de IA; el puntaje de aprobación es 700 ([guía SC-401](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-401)). La certificación Information Security Administrator Associate se renueva gratis cada año y el examen está disponible en español ([certificación](https://learn.microsoft.com/en-us/credentials/certifications/information-security-administrator/)).

> **Atención.** La ruta «Govern and protect sensitive information in the age of AI» (3 módulos, 2 h 8 min) usa DSPM for AI (classic) y evaluaciones que estaban en preview ([ruta legada](https://learn.microsoft.com/en-us/training/paths/purview-protect-govern-ai/)). Complétala con la [ruta de la nueva DSPM](https://learn.microsoft.com/en-us/training/paths/purview-data-security-posture-management/), de 4 módulos y 2 h 42 min.

> **Consejo Ninja.** Orden recomendado de las rutas oficiales: la de la nueva DSPM, luego la ruta SC-401 de IA (3 h 30 min, también en [español](https://learn.microsoft.com/es-es/training/paths/purview-protect-ai/)) y por último el módulo 3 de la [ruta Ninja de Purview](https://learn.microsoft.com/en-us/training/paths/purview-ninja-safeguard-data/) (Security Copilot en Purview, 17 minutos).

**¿Tienes poco tiempo?**

- [Reduce data exposure risk with Data Security Posture Management in Microsoft Purview (learning path)](https://learn.microsoft.com/en-us/training/paths/purview-data-security-posture-management/) · Curso
- [Secure AI interactions and environments with Microsoft Purview (SC-401 learning path)](https://learn.microsoft.com/en-us/training/paths/purview-protect-ai/) · Curso
- [Study guide for Exam SC-401: Administering Information Security in Microsoft 365](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-401) · Credencial

### Documentación, cursos y credenciales

- [Study guide for Exam SC-401: Administering Information Security in Microsoft 365](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-401) · Credencial · Oficial · Nuevo · Microsoft Learn · 28 oct 2026. Guía oficial del examen SC-401 con habilidades medidas al 28-oct-2026, que incluyen proteger datos usados por servicios de IA, DLP, retención, Insider Risk y alertas.
- [Microsoft Certified: Information Security Administrator Associate](https://learn.microsoft.com/en-us/credentials/certifications/information-security-administrator/) · Credencial · Oficial · Nuevo · Microsoft Learn · 14 oct 2026. Página de la certificación asociada al SC-401 con el curso Protect sensitive information with Microsoft Purview in the AI era, evaluación de práctica, precio de 165 USD y examen disponible en español.
- [Reduce data exposure risk with Data Security Posture Management in Microsoft Purview (learning path)](https://learn.microsoft.com/en-us/training/paths/purview-data-security-posture-management/) · Curso · Oficial · Microsoft Learn. Ruta oficial de 4 módulos (2 h 42 min) sobre la nueva DSPM: entender la postura, evaluarla con observabilidad de IA y explorador de activos, remediar con objetivos y políticas de un clic, e investigar con Security Copilot.
- [Secure AI interactions and environments with Microsoft Purview (SC-401 learning path)](https://learn.microsoft.com/en-us/training/paths/purview-protect-ai/) · Curso · Oficial · Microsoft Learn. Ruta oficial de 4 módulos (3 h 30 min) alineada a SC-401: proteger datos de IA con DSPM y auditoría, interacciones de Copilot, apps de IA empresariales y de navegador, y entornos de desarrollo (Foundry, Copilot Studio, Fabric).
- [Govern and protect sensitive information in the age of AI (learning path)](https://learn.microsoft.com/en-us/training/paths/purview-protect-govern-ai/) · Curso · Oficial · Legado aún útil · Microsoft Learn. Ruta de 3 módulos (2 h 8 min) sobre retos de seguridad de datos de IA, cumplimiento para Copilot e identificación de riesgos con DSPM for AI y evaluaciones de datos. *Nota:* Usa la experiencia DSPM for AI (classic) y evaluaciones en preview; complementar con la ruta de la nueva DSPM

**Manos a la obra**

1. `Laboratorio` Lee la [guía de estudio del SC-401](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-401) y marca, para cada habilidad medida sobre IA y DSPM, el módulo de este programa que la cubre. Evidencia: matriz habilidad–módulo.
2. `Laboratorio` Completa la [ruta de la nueva DSPM](https://learn.microsoft.com/en-us/training/paths/purview-data-security-posture-management/) con sus evaluaciones de módulo. Evidencia: progreso registrado en tu perfil de Microsoft Learn.
3. `Laboratorio` Suscríbete a la [etiqueta dspm de Tech Community](https://techcommunity.microsoft.com/tag/dspm) y define un filtro del Message Center para DSPM, Copilot y Agent 365. Evidencia: lista de cinco fuentes con su frecuencia de revisión.

<a id="i1"></a>

## I1 · DSPM hoy: la experiencia unificada y qué incluye Microsoft 365 E5

*L100–L200 · ~4 h · Origen: Ruta de Learn de DSPM, módulos 1 y 2 (entender y evaluar la postura)*

DSPM responde cuatro preguntas: dónde están tus datos sensibles, quién puede acceder a ellos, cómo se usan (también por la IA) y qué controles faltan. La experiencia actual **unifica** la postura de las apps tradicionales y la de las apps y agentes de IA. Cubre Microsoft 365, Azure y Fabric, y llega a SaaS e IaaS de terceros (GCP, Snowflake, Databricks) mediante integraciones con Varonis, Cyera, BigID y OneTrust. Reúne información de DLP, Insider Risk Management, etiquetas de confidencialidad y Data Security Investigations, y la organiza en **objetivos de seguridad de datos**. Entre esos objetivos están prevenir la exposición en Copilot, prevenir la sobreexposición, prevenir la exfiltración a destinos riesgosos y descubrir datos sensibles.

La cronología importa. Microsoft anunció la nueva DSPM en Ignite 2025, la preview corrió de diciembre de 2025 a abril de 2026 y la disponibilidad general llegó en mayo de 2026. Las experiencias classic se retiran a fines de enero de 2027. Sus páginas clave son *Posture* (métricas, objetivos priorizados por riesgo y tendencia de 30 días), *Objectives*, *AI observability*, *Asset explorer*, *Reports* y *Setup tasks*. Tras aceptar las tareas iniciales, los datos accionables tardan alrededor de un día en aparecer.

La IA de DSPM también puede **actuar**: quitar vínculos públicos, aplicar DLP o revocar permisos, siempre bajo supervisión y con auditoría. En facturación, los datos de Microsoft 365 se licencian por usuario. Los orígenes que no son Microsoft 365, la red y las apps y agentes de IA se cobran por uso, y las experiencias de Microsoft 365 Copilot no generan cargos de pago por uso.

**Por qué importa**

Una vista unificada de la postura reemplaza planillas e informes desconectados por una métrica con tendencia que el CISO puede seguir mes a mes. También prioriza el trabajo por objetivo de riesgo y no por herramienta. Además hay una fecha límite concreta: todo procedimiento, informe o política que dependa de las experiencias classic debe migrar antes de fines de enero de 2027.

**Qué vas a lograr**

- Explicar qué es DSPM y en qué se diferencia de la gestión de postura en la nube (CSPM).
- Recorrer Posture, Objectives, AI observability, Asset explorer, Reports y Setup tasks.
- Explicar la cronología: preview, disponibilidad general en mayo de 2026 y retiro de las experiencias classic a fines de enero de 2027.
- Distinguir qué orígenes se cubren con licencia por usuario y cuáles con pago por uso.
- Completar las tareas iniciales y documentar una línea base de postura.

> **Novedad.** La nueva DSPM llegó a disponibilidad general de inicios a fines de mayo de 2026, tras una preview de diciembre de 2025 a abril de 2026 (MC1191257, Roadmap 532728) ([MC1191257](https://message.cengizyilmaz.net/message/mc1191257-new-microsoft-purview-data-security-posture-management-experience)). El blog [What’s new in Microsoft Security: May 2026](https://www.microsoft.com/en-us/security/blog/2026/05/21/whats-new-in-microsoft-security-may-2026/) la anunció el 21 de mayo.

> **Atención.** DSPM (classic) y DSPM for AI (classic) se retiran a fines de enero de 2027 en Worldwide, GCC, GCC High y DoD. MC1481315 se publicó el 28 de septiembre de 2026 con fechas de noviembre y diciembre de 2026 y se actualizó el 27 de octubre de 2026 ([MC1481315](https://mc.merill.net/message/MC1481315)). Migra flujos, informes y procedimientos antes de esa fecha.

> **Atención.** Límites que conviene conocer: en Asset explorer, las ubicaciones Microsoft incluyen por ahora solo Microsoft 365 y las no Microsoft dependen de socios. La integración con el data lake de Sentinel para orígenes no Microsoft está en preview, y tras aceptar las tareas iniciales los datos accionables tardan alrededor de un día ([DSPM](https://learn.microsoft.com/en-us/purview/data-security-posture-management-learn-about)).

> **Consejo Ninja.** Facturación en una línea: datos de Microsoft 365 por usuario; Azure SQL, Fabric y otros orígenes que no son Microsoft 365, la red y las apps y agentes de IA, por pago por uso en Azure. Las experiencias de Microsoft 365 Copilot no se cobran por uso ([modelos de facturación](https://learn.microsoft.com/en-us/purview/purview-billing-models), [guía de licenciamiento](https://www.microsoft.com/licensing/guidance/Microsoft-Purview)).

**¿Tienes poco tiempo?**

- [Learn about Microsoft Purview Data Security Posture Management (DSPM)](https://learn.microsoft.com/en-us/purview/data-security-posture-management-learn-about) · Documentación
- [New Data Security Posture Management | Microsoft Purview (Microsoft Mechanics)](https://www.youtube.com/watch?v=NLfoFpFxhrA) · Video
- [MC1481315 – Retirement of DSPM classic and DSPM for AI classic experiences (archivo, versión actualizada)](https://mc.merill.net/message/MC1481315) · Herramienta

### Documentación, cursos y credenciales

- [Learn about Microsoft Purview Data Security Posture Management (DSPM)](https://learn.microsoft.com/en-us/purview/data-security-posture-management-learn-about) · Documentación · Oficial · Microsoft Learn. Página principal de la versión actual (unificada) de DSPM: objetivos de seguridad de datos, observabilidad de IA, cobertura de Microsoft 365, Azure, Fabric y SaaS/IaaS de terceros con integraciones de socios.
- [Learn about Microsoft Purview billing models](https://learn.microsoft.com/en-us/purview/purview-billing-models) · Documentación · Oficial · Microsoft Learn · 6 ene 2026. Describe el modelo por usuario (E3/E5/A5/F5/G5) y el modelo pay-as-you-go facturado en Azure para orígenes no Microsoft 365, red, apps y agentes de IA; las experiencias de Microsoft 365 Copilot no se cobran.
- [What is data security posture management (DSPM)?](https://www.microsoft.com/en-us/security/business/security-101/what-is-data-security-posture-management-dspm) · Documentación · Oficial · Microsoft Security · 26 ene 2026. Artículo introductorio que explica qué es DSPM, su flujo (descubrir, clasificar, evaluar, detectar, remediar) y su diferencia con CSPM.

### Anuncios y blogs oficiales

- [What’s new in Microsoft Security: May 2026](https://www.microsoft.com/en-us/security/blog/2026/05/21/whats-new-in-microsoft-security-may-2026/) · Blog oficial · Oficial · Nuevo · Alym Rayani · Microsoft Security Blog · 21 may 2026. Anuncia la disponibilidad general de la nueva experiencia DSPM de Purview, la API de cumplimiento de Claude para Purview y OCR y exámenes personalizados en Data Security Investigations.
- [Empowering organizations with integrated data security: What’s new in Microsoft Purview (Ignite 2025)](https://techcommunity.microsoft.com/blog/microsoft-security-blog/empowering-organizations-with-integrated-data-security-what%E2%80%99s-new-in-microsoft-p/4470663) · Blog oficial · Empleado de Microsoft · Raman Kalyan · Microsoft Security Community Blog · 18 nov 2025. Anuncio de Ignite 2025 de la nueva DSPM unificada: flujos por objetivos, evaluaciones a nivel de elemento, informes de postura, observabilidad de IA, agente de Security Copilot y visibilidad de Salesforce, Snowflake, GCP y Databricks vía Sentinel.
- [Beyond Visibility: The new Microsoft Purview Data Security Posture Management (DSPM) experience](https://techcommunity.microsoft.com/blog/microsoft-security-blog/beyond-visibility-the-new-microsoft-purview-data-security-posture-management-dsp/4470984) · Blog oficial · Oficial · Microsoft Purview · Microsoft Security Community Blog · nov 2025. Blog oficial de anuncio de la nueva DSPM (Ignite 2025) con objetivos, observabilidad de IA, informes, agente de postura e integraciones de socios.

### Webinars, videos y podcasts

- [New Data Security Posture Management | Microsoft Purview (Microsoft Mechanics)](https://www.youtube.com/watch?v=NLfoFpFxhrA) · Video · Empleado de Microsoft · Talhah Mir · Microsoft Mechanics · dic 2025. Video oficial de la nueva DSPM: uso diario, prevención de sobreexposición, observabilidad de IA y cómo ponerla en marcha en la organización.
- [Beyond Visibility: Microsoft Purview Data Security Posture Management (BRK253, Ignite 2025)](https://tech.hub.ms/ai/videos/beyond-visibility-microsoft-purview-data-security-posture-management) · Video · Empleado de Microsoft · Rudra Mitra, Nathalia Borges, Yaki Faitelson, Talhah Mir · Tech Hub (agregador de sesiones Microsoft Events) · 25 nov 2025. Ficha de la sesión avanzada (300) de Ignite 2025 sobre la estrategia de DSPM de extremo a extremo con agentes de IA, con el video embebido de Microsoft Events.

### Laboratorios, GitHub y herramientas

- [MC1481315 – Retirement of DSPM classic and DSPM for AI classic experiences (archivo, versión actualizada)](https://mc.merill.net/message/MC1481315) · Herramienta · Comunidad · Nuevo · Microsoft (archivado por Merill Fernando) · Microsoft 365 Message Center Archive (merill.net) · 27 oct 2026. Anuncia el retiro de DSPM (classic) y DSPM for AI (classic), aplazado el 27-oct-2026 para iniciar y completarse a finales de enero de 2027, por lo que todo flujo debe migrar a la DSPM actual.
- [MC1191257 – New Microsoft Purview data security posture management experience (archivo Message Center)](https://message.cengizyilmaz.net/message/mc1191257-new-microsoft-purview-data-security-posture-management-experience) · Herramienta · Comunidad · Microsoft (archivado por Cengiz Yilmaz) · Microsoft 365 Message Center Archive (cengizyilmaz.net) · 10 abr 2026. Cronología oficial de la nueva DSPM: preview desde diciembre de 2025 y GA en mayo de 2026, con DSPM (classic) y DSPM for AI (classic) aún accesibles y migración automática de la incorporación.
- [Data Security Posture Management – Microsoft Security Workshop (lab)](https://indra-pr.github.io/msft-security-workshop/purview/data-security/dspm/) · Laboratorio · Comunidad · indra-pr (autor no verificado) · Microsoft Security Workshop (GitHub Pages, comunidad). Laboratorio guiado de 1,5–2,5 h para habilitar DSPM, revisar insights, convertir una recomendación de sobreexposición en política de un clic y evaluar DSPM para IA.

**Manos a la obra**

1. `Laboratorio parcial` Activa DSPM: entra a *Purview > DSPM*, acepta las tareas iniciales y, al día siguiente, documenta las métricas de Posture, las tarjetas de objetivos y Asset explorer ([DSPM](https://learn.microsoft.com/en-us/purview/data-security-posture-management-learn-about)). Limitación: con datos sintéticos aparecen pocos hallazgos; aprendes el flujo, no la postura real. Evidencia: informe de línea base con capturas y fecha.
2. `Laboratorio parcial` Convierte una recomendación del objetivo de sobreexposición en una política de un clic, ajusta su alcance a un grupo piloto y anota su modo inicial (auditoría o prueba). Limitación: sin volumen real la política casi no tendrá coincidencias. Evidencia: política con prefijo `PRUEBA-` y alcance acotado.
3. `Laboratorio parcial` Recorre el [laboratorio comunitario de DSPM](https://indra-pr.github.io/msft-security-workshop/purview/data-security/dspm/) (1,5 a 2,5 horas) y anota las diferencias con la documentación oficial. Limitación: es material no oficial y sus requisitos de licencia deben confirmarse en la descripción del servicio. Evidencia: lista de pasos completados y de diferencias encontradas.
4. `Laboratorio` Dependencias de las experiencias classic: lista los informes, las políticas con prefijo «Microsoft AI Hub» y los procedimientos que usan DSPM (classic) o DSPM for AI (classic), y asigna a cada uno su equivalente en la nueva DSPM con una fecha anterior a fines de enero de 2027 ([MC1481315](https://mc.merill.net/message/MC1481315)). Evidencia: tabla de migración aprobada.
5. `Solo producción` Línea base real: con un rol de solo lectura de DSPM, exporta el informe de postura y la tendencia de 30 días de producción para el comité de IA. Cómo hacerlo seguro: no crees ni modifiques políticas, comparte solo métricas agregadas y deja constancia de quién accedió. Evidencia: informe fechado.

**¿Quieres profundizar?**

- [Beyond Visibility: Microsoft Purview Data Security Posture Management (BRK253, Ignite 2025)](https://tech.hub.ms/ai/videos/beyond-visibility-microsoft-purview-data-security-posture-management) · Video
- [MC1191257 – New Microsoft Purview data security posture management experience (archivo Message Center)](https://message.cengizyilmaz.net/message/mc1191257-new-microsoft-purview-data-security-posture-management-experience) · Herramienta

<a id="i2"></a>

## I2 · DSPM para IA: Copilot, agentes y aplicaciones de IA

*L100–L200 · ~4 h · Origen: Ruta SC-401 de IA, módulo 1 (DSPM y auditoría), y ruta de DSPM, módulo 2 (observabilidad de IA)*

Lo que empezó como **AI Hub** y luego se llamó **DSPM for AI** hoy está integrado en la DSPM unificada. La página **AI observability** inventaría las apps y agentes de IA con actividad en los últimos 30 días, incluido Agent 365, y muestra su riesgo y sus interacciones con datos sensibles. El panel *Discover > Apps and agents* no incluye Agent 365. Las políticas creadas en la etapa de AI Hub conservan el prefijo «Microsoft AI Hub».

Cada tipo de IA tiene sus **prerrequisitos**. Microsoft 365 Copilot y sus agentes requieren licencia de Copilot, y el evento «AI interaction» exige la auditoría activa. Copilot en Fabric y Security Copilot requieren la versión empresarial de Purview data governance y una directiva de colección con captura de contenido. Las apps de IA de terceros en Edge necesitan una directiva de configuración de Edge, y las apps propias registradas en Entra deben integrarse con el SDK de Purview. Copilot Cowork se documenta aparte: sus interacciones aparecen en el explorador de actividad, pero no en *Apps and agents* ni en *AI observability*.

Desde los objetivos y las recomendaciones se crean **políticas de un clic** de DLP, Insider Risk, Communication Compliance, etiquetas y colección. Muchas arrancan en modo auditoría o prueba. Son el atajo para pasar de la visibilidad a la protección, siempre que ajustes su alcance a un grupo piloto.

**Por qué importa**

No puedes proteger lo que no ves. La adopción de IA abre flujos nuevos de datos sensibles: prompts, respuestas, archivos de contexto y agentes que actúan solos. DSPM para IA da al comité de gobierno de IA un inventario y evidencia para decidir qué apps sancionar, qué datos proteger primero y qué controles faltan. Si faltan los prerrequisitos, los paneles quedan vacíos y el equipo saca conclusiones equivocadas.

**Qué vas a lograr**

- Describir qué muestra AI observability y qué queda fuera (Agent 365 en Apps and agents, Copilot Cowork).
- Enumerar los prerrequisitos por tipo de IA: Copilot, Copilot en Fabric, Security Copilot, IA de terceros en Edge y apps registradas en Entra.
- Explicar el evento «AI interaction» y cuándo exige una directiva de colección con captura de contenido.
- Identificar las políticas heredadas de AI Hub y decidir qué conservar.
- Activar una política de un clic con alcance piloto y revisar su modo inicial.

> **Atención.** AI observability inventaría apps y agentes con actividad en los últimos 30 días, incluido Agent 365; el panel *Discover > Apps and agents* no incluye Agent 365 ([DSPM](https://learn.microsoft.com/en-us/purview/data-security-posture-management-learn-about)). Las interacciones de Copilot Cowork aparecen en el explorador de actividad, pero no en *Apps and agents* ni en *AI observability* ([Copilot Cowork](https://learn.microsoft.com/es-es/purview/ai-copilot-cowork)).

> **Consejo Ninja.** El evento «AI interaction» depende del origen. Con Microsoft 365 Copilot y Copilot Chat basta la auditoría activa; con Copilot en Fabric, Security Copilot y las apps que no son Copilot hace falta una directiva de colección con captura de contenido ([consideraciones](https://learn.microsoft.com/en-us/purview/data-security-posture-management-considerations)).

> **Qué cambió.** Las políticas creadas cuando la solución se llamaba AI Hub conservan el prefijo «Microsoft AI Hub» ([DSPM for AI](https://techcommunity.microsoft.com/blog/microsoft-purview-blog/microsoft-purview-%E2%80%93-data-security-posture-management-dspm-for-ai/4394685)). Inventaríalas y decide cuáles conservar antes del retiro de la experiencia classic.

> **Atención.** Gestionar Copilot en Fabric con Purview requiere pago por uso, y el soporte para otras experiencias de Copilot en Fabric y para Fabric Data Agent está en preview ([Copilot en Fabric](https://learn.microsoft.com/es-es/purview/ai-copilot-fabric)).

**¿Tienes poco tiempo?**

- [Considerations for deploying Microsoft Purview Data Security Posture Management](https://learn.microsoft.com/en-us/purview/data-security-posture-management-considerations) · Documentación
- [Use Microsoft Purview to manage data security & compliance for Microsoft 365 Copilot & Copilot Chat](https://learn.microsoft.com/en-us/purview/ai-m365-copilot) · Documentación
- [AI and Agent Data Security Controls in Microsoft Purview (Microsoft Mechanics)](https://www.youtube.com/watch?v=4BcVWkSTZ3I) · Video

### Documentación, cursos y credenciales

- [Considerations for deploying Microsoft Purview Data Security Posture Management](https://learn.microsoft.com/en-us/purview/data-security-posture-management-considerations) · Documentación · Oficial · Microsoft Learn. Prerrequisitos de la DSPM actual para IA (licencia de Copilot, directiva de colección, configuración de Edge, SDK de Purview, Security Copilot), soporte de unidades administrativas y eventos del explorador de actividad.
- [Considerations for deploying Microsoft Purview DSPM for AI (classic)](https://learn.microsoft.com/en-us/purview/dspm-for-ai-considerations) · Documentación · Oficial · Legado aún útil · Nuevo · Microsoft Learn · 1 may 2026. Prerrequisitos de DSPM for AI: auditoría, licencias de Microsoft 365 Copilot, extensión de navegador, incorporación de dispositivos, SDK de Purview para apps registradas en Entra, PAYG para apps distintas de Copilot, evaluaciones de Fabric y escaneo a nivel de elemento. *Nota:* Lista oficial de políticas de un clic con su modo inicial (auditoría/prueba) y eventos del explorador de actividad; artículo classic, prerrequisitos vigentes
- [Learn about Data Security Posture Management for AI (classic)](https://learn.microsoft.com/en-us/purview/dspm-for-ai) · Documentación · Oficial · Legado aún útil · Microsoft Learn. Describe DSPM for AI clásico: políticas de un clic, informes de actividad de IA, evaluación semanal automática de los 100 sitios de SharePoint más usados y controles de cumplimiento para Copilot y apps de IA de terceros. *Nota:* Reemplazado por la nueva DSPM con soporte para apps y agentes de IA

### Anuncios y blogs oficiales

- [Microsoft Purview – Data Security Posture Management (DSPM) for AI](https://techcommunity.microsoft.com/blog/microsoft-purview-blog/microsoft-purview-%E2%80%93-data-security-posture-management-dspm-for-ai/4394685) · Blog oficial · Empleado de Microsoft · Legado aún útil · Kunal Parmar · Microsoft Purview Blog (Tech Community) · 21 mar 2025. Explica una a una las recomendaciones de DSPM for AI (políticas de un clic, guía regulatoria basada en NIST AI RMF, evaluaciones de datos) y sus prerrequisitos. *Nota:* Describe DSPM for AI (hoy classic); las políticas creadas en la etapa AI Hub conservan el prefijo Microsoft AI Hub

### Webinars, videos y podcasts

- [AI and Agent Data Security Controls in Microsoft Purview (Microsoft Mechanics)](https://www.youtube.com/watch?v=4BcVWkSTZ3I) · Video · Empleado de Microsoft · Legado aún útil · Shilpa Ranganathan · Microsoft Mechanics. Demostración de DSPM for AI: registro de actividad, monitoreo de riesgos, ChatGPT Enterprise, barreras para agentes, sobreexposición y registros de auditoría. *Nota:* Grabado sobre DSPM for AI (hoy classic); los conceptos siguen vigentes en la nueva DSPM. YouTube muestra "hace 1 año" (2025, mes no visible)

**Manos a la obra**

1. `Laboratorio parcial` Revisa AI observability y el panel *Apps and agents* y documenta qué apps aparecen y por qué faltan otras: licencias de Copilot, pago por uso o Agent 365 ([consideraciones](https://learn.microsoft.com/en-us/purview/data-security-posture-management-considerations)). Limitación: sin licencias de Copilot ni pago por uso el inventario estará casi vacío. Evidencia: tabla de inventario con la causa de cada ausencia.
2. `Laboratorio parcial` Genera interacciones en Copilot Chat con una cuenta de prueba y verifica el evento «AI interaction» en el explorador de actividad, con la auditoría activa. Limitación: la visibilidad completa de Microsoft 365 Copilot requiere licencias; el sandbox de desarrollador permite comprarlas. Evidencia: captura del evento con fecha y usuario de prueba.
3. `Laboratorio parcial` Activa una política de un clic para Copilot, por ejemplo la de uso riesgoso de IA o la de comportamiento no ético, con alcance a las cuentas de prueba, y revisa su modo inicial ([Purview para Copilot](https://learn.microsoft.com/en-us/purview/ai-m365-copilot)). Limitación: sin actividad real la política no generará alertas útiles. Evidencia: política creada con su alcance y su modo.
4. `Laboratorio` Checklist de prerrequisitos por tipo de IA: Copilot (licencias y auditoría), Copilot en Fabric y Security Copilot (data governance empresarial y directiva de colección), IA de terceros (configuración de Edge, extensión y pago por uso) y apps propias (SDK de Purview). Evidencia: checklist con el estado de tu organización.
5. `Solo producción` Inventario real de IA: con el rol Data Security AI Viewer, exporta las apps y agentes con actividad de los últimos 30 días y clasifícalos con el comité de IA en sancionados, tolerados y no autorizados; la parte de agentes requiere E7 o Agent 365. Cómo hacerlo seguro: no asignes AI Content Viewer para esta tarea, trabaja con datos agregados y registra la decisión en el acta del comité. Evidencia: inventario clasificado.

<a id="i3"></a>

## I3 · Evaluaciones de riesgo de datos y sobreexposición

*L100–L200 · ~4 h · Origen: Ruta de Learn de DSPM, módulo 3 (proteger y remediar), y guía oficial para proteger y gobernar Copilot*

La sobreexposición es el primer riesgo de Copilot. Copilot respeta los permisos, así que todo lo que una persona puede abrir puede aparecer en una respuesta. Eso incluye lo que quedó abierto por accidente: un sitio compartido con toda la organización o un vínculo «Cualquier persona» olvidado. Las **evaluaciones de riesgo de datos** de DSPM lo encuentran. La evaluación predeterminada revisa cada semana los 100 sitios de SharePoint más usados, y las evaluaciones personalizadas cubren Microsoft 365 y Fabric. La primera evaluación predeterminada tarda unos 4 días y las personalizadas, unas 48 horas.

En marzo de 2026 llegaron a disponibilidad general el **escaneo y la remediación a nivel de elemento**, que requieren una aplicación de Entra configurada por el administrador y no están activos por defecto. La nueva DSPM además permite desactivar en bloque los vínculos sobrecompartidos de SharePoint. Las remediaciones disponibles son restringir por etiqueta, Restricted Content Discovery (RCD), autoetiquetado, retención y revisión de acceso por el propietario. RCD requiere licencia de Copilot y no aplica a OneDrive.

La guía oficial para proteger y gobernar Copilot organiza el trabajo en tres pilares: remediar la sobreexposición, establecer barreras y cumplir regulaciones. Este módulo cubre el primero desde Purview; el módulo [M4](02_Nivel_2_Intermedio.md#m4) lo completa con SharePoint Advanced Management.

**Por qué importa**

Reducir la sobreexposición baja la probabilidad de que Copilot o un agente muestren datos sensibles a quien no debería verlos. También produce una lista priorizada de sitios con dueño y remediación, y respalda la decisión de ampliar Copilot a nuevas oleadas de usuarios. Se mide con indicadores concretos: sitios sobrecompartidos, elementos sensibles con acceso amplio y vínculos desactivados.

**Qué vas a lograr**

- Explicar cómo funcionan las evaluaciones predeterminada y personalizadas, y cuánto tardan.
- Configurar el escaneo a nivel de elemento con una aplicación de Entra de uso exclusivo y retirarla al terminar.
- Elegir la remediación adecuada: etiqueta, RCD, autoetiquetado, retención, revisión del propietario o desactivación de vínculos.
- Priorizar sitios sobrecompartidos y documentar un plan con propietarios y fechas.

> **Novedad.** El escaneo y la remediación a nivel de elemento llegaron a GA en marzo de 2026: requieren una aplicación de Entra que configura el administrador y no están activos por defecto ([MC1254556](https://mc.merill.net/message/MC1254556)). La nueva DSPM sumó evaluaciones de Fabric y la desactivación masiva de vínculos sobrecompartidos de SharePoint ([MC1191257](https://message.cengizyilmaz.net/message/mc1191257-new-microsoft-purview-data-security-posture-management-experience)).

> **Atención.** Tiempos: la evaluación predeterminada revisa cada semana los 100 sitios más usados y la primera tarda unos 4 días; las personalizadas tardan unas 48 horas ([evaluaciones](https://learn.microsoft.com/en-us/purview/data-security-posture-management-oversharing)). En una prueba de un mes, lanza la evaluación personalizada el primer día.

> **Atención.** La aplicación de Entra para el escaneo de elementos usa permisos de aplicación amplios, como Files.ReadWrite.All y Sites.ReadWrite.All ([consideraciones](https://learn.microsoft.com/en-us/purview/dspm-for-ai-considerations)). Crea una aplicación exclusiva para el piloto, guarda el secreto en Key Vault, revisa el consentimiento y elimínala al terminar.

> **Consejo Ninja.** Restricted Content Discovery es un control temporal: oculta sitios de la búsqueda organizacional y de Copilot sin cambiar permisos, requiere licencia de Copilot y no aplica a OneDrive ([RCD](https://learn.microsoft.com/en-us/sharepoint/restricted-content-discovery)). Úsalo mientras corriges permisos, no como solución definitiva.

**¿Tienes poco tiempo?**

- [Prevent oversharing with data risk assessments from Microsoft Purview DSPM](https://learn.microsoft.com/en-us/purview/data-security-posture-management-oversharing) · Documentación
- [Secure and govern Microsoft Copilot: foundational deployment guidance (blueprint)](https://learn.microsoft.com/en-us/microsoft-365/copilot/secure-govern-copilot-foundational-deployment-guidance) · Documentación
- [Protect and remediate sensitive data in Microsoft Purview (module)](https://learn.microsoft.com/en-us/training/modules/purview-data-security-posture-management-protect-remediate/) · Curso

### Documentación, cursos y credenciales

- [Secure and govern Microsoft Copilot: foundational deployment guidance (blueprint)](https://learn.microsoft.com/en-us/microsoft-365/copilot/secure-govern-copilot-foundational-deployment-guidance) · Documentación · Oficial · Nuevo · Microsoft Learn · 30 oct 2026. Blueprint oficial en tres pilares (remediar sobreexposición, establecer barreras, cumplir regulaciones) basado en Purview y SharePoint Advanced Management, con PDF y PowerPoint descargables.
- [Prevent oversharing with data risk assessments from Microsoft Purview DSPM](https://learn.microsoft.com/en-us/purview/data-security-posture-management-oversharing) · Documentación · Oficial · Microsoft Learn. Explica la evaluación predeterminada semanal de los 100 sitios de SharePoint más usados, las evaluaciones personalizadas (Microsoft 365 y Fabric) y las acciones de remediación: restringir por etiqueta, Restricted Content Discovery, autoetiquetado, retención y revisión de acceso.

### Laboratorios, GitHub y herramientas

- [MC1254556 – Purview DSPM’s Data Risk Assessments now support item-level investigation and remediation of SharePoint (archivo)](https://mc.merill.net/message/MC1254556) · Herramienta · Comunidad · Microsoft (archivado por Merill Fernando) · Microsoft 365 Message Center Archive (merill.net) · 17 mar 2026. Anuncia la GA (marzo de 2026) del escaneo y la remediación a nivel de elemento en SharePoint, que requiere una aplicación de Entra (service principal) configurada por el administrador.

**Manos a la obra**

1. `Laboratorio parcial` Crea una evaluación personalizada sobre dos o tres sitios con datos sintéticos y vínculos de uso compartido amplio, y revisa las remediaciones propuestas ([evaluaciones de riesgo de datos](https://learn.microsoft.com/en-us/purview/data-security-posture-management-oversharing)). Limitación: el volumen es bajo, el nivel de elemento requiere una app de Entra y RCD requiere Copilot. Evidencia: resultados de la evaluación y lista de sitios con su remediación.
2. `Laboratorio parcial` Configura el escaneo a nivel de elemento con una aplicación de Entra exclusiva para el piloto, documenta los permisos concedidos y elimínala al terminar ([MC1254556](https://mc.merill.net/message/MC1254556)). Limitación: la app tiene permisos de escritura amplios; en producción usa Key Vault y revisión del consentimiento. Evidencia: registro de la app, permisos y fecha de eliminación.
3. `Laboratorio parcial` En un sitio de prueba con vínculos sobrecompartidos, usa la desactivación masiva de vínculos de DSPM y comprueba con una cuenta de prueba que los vínculos dejaron de funcionar. Limitación: en el laboratorio no ves el impacto sobre usuarios reales. Evidencia: capturas antes y después.
4. `Laboratorio` Plan de remediación: para cada sitio priorizado elige la remediación (etiqueta, RCD, autoetiquetado, retención o revisión del propietario), el responsable y la fecha, siguiendo el pilar de sobreexposición de la [guía para proteger y gobernar Copilot](https://learn.microsoft.com/en-us/microsoft-365/copilot/secure-govern-copilot-foundational-deployment-guidance). Evidencia: plan aprobado por seguridad de datos.
5. `Solo producción` Evaluación predeterminada en producción: toma los 10 sitios más expuestos de la evaluación semanal y valida cada hallazgo con su propietario antes de remediar. Cómo hacerlo seguro: lectura primero, remediación por oleadas con aviso a los propietarios y reversión documentada por si se corta un acceso legítimo. Evidencia: lista validada con fecha de remediación.

**¿Quieres profundizar?**

- [MC1254556 – Purview DSPM’s Data Risk Assessments now support item-level investigation and remediation of SharePoint (archivo)](https://mc.merill.net/message/MC1254556) · Herramienta

<a id="reto-inicial"></a>

## Reto del nivel

**Radiografía de exposición antes de Copilot.** En tu laboratorio activa la auditoría y DSPM, siembra datos sintéticos en tres sitios (con vínculos de uso compartido amplio y un grupo de toda la organización) y lanza una evaluación personalizada. Entrega un informe de dos páginas con la línea base de postura, los sitios priorizados con su remediación y responsable, el inventario de IA con los prerrequisitos que faltan, el mapa de licencias (E5 o Purview Suite, Copilot, E7 o Agent 365 y pago por uso) y la lista de dependencias de las experiencias classic que deben migrar antes de fines de enero de 2027.

<a id="quiz-inicial"></a>

## Evaluación del nivel

Responde y compara con [Evaluaciones y respuestas](06_Evaluaciones_y_respuestas.md#eval-inicial). Con 80 % o más, ¡nivel aprobado! (En la versión web puedes corregir en línea y generar tu certificado).

1. Según la versión vigente de MC1481315, ¿cuándo se completa el retiro de DSPM (classic) y DSPM for AI (classic)?
   - a) Fines de noviembre de 2026
   - b) Fines de diciembre de 2026
   - c) Fines de enero de 2027
   - d) 31 de marzo de 2027

2. ¿Qué licencia base habilita DSPM sobre los datos de Microsoft 365?
   - a) Microsoft 365 E5 o Microsoft Purview Suite (antes E5 Compliance)
   - b) Microsoft 365 E3 sin complementos
   - c) Solo Agent 365
   - d) Solo el pago por uso

3. ¿En qué página de DSPM aparecen los agentes de Agent 365?
   - a) Discover > Apps and agents
   - b) Data risk assessments
   - c) Asset explorer
   - d) AI observability

4. ¿Qué revisa la evaluación de riesgo de datos predeterminada de DSPM?
   - a) Todos los sitios de SharePoint, cada día
   - b) Los 100 sitios de SharePoint más usados, cada semana
   - c) Solo los OneDrive de los administradores
   - d) Los 1.000 sitios más grandes, cada mes

5. ¿Qué se necesita para usar el escaneo y la remediación a nivel de elemento en las evaluaciones de riesgo de datos?
   - a) Nada: está activo por defecto
   - b) Una licencia de Agent 365
   - c) Un conector de Microsoft Sentinel
   - d) Una aplicación de Entra configurada por el administrador

6. Para registrar el evento «AI interaction» de Copilot en Fabric, Security Copilot o apps que no son Copilot, ¿qué se requiere?
   - a) Solo la auditoría activa
   - b) Una directiva de colección con captura de contenido
   - c) Restricted Content Discovery
   - d) Una etiqueta de contenedor

7. En un inquilino con unidades administrativas, ¿quién puede crear políticas de un clic desde DSPM?
   - a) Cualquier administrador restringido de su unidad
   - b) Solo un administrador no restringido
   - c) El propietario de cada sitio
   - d) Cualquier usuario con licencia de Copilot

8. ¿Cómo se factura la cobertura de orígenes que no son Microsoft 365, como Azure SQL o Fabric?
   - a) Por usuario con Microsoft 365 E5
   - b) Incluida en Microsoft 365 Copilot
   - c) Con pago por uso facturado en Azure
   - d) Con SCU de Security Copilot

9. ¿Qué ubicaciones Microsoft muestra por ahora Asset explorer?
   - a) Solo Microsoft 365
   - b) Microsoft 365, Azure y Fabric
   - c) Solo Azure
   - d) Microsoft 365 y Dynamics 365

10. ¿Qué afirmación sobre Restricted Content Discovery es correcta?
   - a) Cambia los permisos del sitio
   - b) Aplica también a OneDrive
   - c) Requiere licencia de Copilot y no aplica a OneDrive
   - d) Reemplaza de forma permanente la revisión de permisos

11. ¿Qué prefijo conservan las políticas creadas cuando la solución se llamaba AI Hub?
   - a) «Microsoft AI Hub»
   - b) «DSPM classic»
   - c) «Copilot Hub»
   - d) «Purview AI»

12. ¿Quién necesita licencia según la regla de licenciamiento de Purview?
   - a) Solo los administradores de Purview
   - b) Solo los usuarios que tienen Copilot
   - c) Todo usuario que se beneficia del servicio, incluidos dueños y miembros de sitios en ubicaciones compartidas
   - d) Todos los usuarios del inquilino, incluidos los visitantes

13. ¿Cuál es el puntaje de aprobación del examen SC-401?
   - a) 500
   - b) 600
   - c) 800
   - d) 700

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. No constituye asesoría legal ni laboral: las decisiones sobre privacidad, captura de contenido, monitoreo y normativa corresponden a tus áreas de Legal, RR. HH. y privacidad. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

# Nivel 3 · Avanzado · IA, agentes, SOC y automatización

*Microsoft Purview Insider Risk Management Ninja Training · Edición 2026*

[← Nivel 2 · Intermedio](02_Nivel_2_Intermedio.md) · [Índice del programa](README.md) · [Nivel 4 · Operación →](04_Nivel_4_Operacion.md)

<a id="avanzado"></a>

Riesgo interno en el uso de IA y en los agentes, integración con Defender XDR y Sentinel, el Triage Agent de Security Copilot y la automatización con Power Automate y APIs. Terminas con una arquitectura integrada, su costo y sus controles de privacidad.

*L400 · 4 módulos · ~20 horas · 25 recursos*

**Módulos de este nivel:** [A1 IA y agentes](#a1) · [A2 Defender XDR y Sentinel](#a2) · [A3 Triage Agent](#a3) · [A4 Automatización y APIs](#a4)

<a id="a1"></a>

## A1 · Riesgo interno en el uso de IA y en los agentes

*L400 · ~5 h · Origen: Nuevo en esta edición (el Ninja oficial de 2024 no cubre IA ni agentes)*

La IA generativa abrió un canal nuevo de exfiltración: pegar datos sensibles en un prompt, recibir información sensible en una respuesta o usar apps de IA no aprobadas. La plantilla **Risky AI usage** detecta prompts riesgosos o con datos sensibles, respuestas con información sensible y visitas a sitios de IA generativa; requiere la extensión Microsoft Insider risk en Edge o Microsoft Purview en Chrome, puede crearse con un clic desde DSPM for AI y suma al puntaje de la Protección adaptativa. Sus indicadores cubren Copilot experiences, Enterprise AI apps, Other AI apps y Azure AI Content Safety (este último crea una política de Communication Compliance).

El costo depende del origen: las interacciones con **Microsoft 365 Copilot no generan cargos de pago por uso**, pero sí las Copilot experiences con datos que no son de Microsoft 365 (Fabric, Security Copilot, Copilot Studio y apps conectadas), las Enterprise AI apps y las Other AI apps que detecta el navegador. Desde junio de 2026 puedes elegir qué apps de IA monitorear, lo que reduce ruido y costo. En 2026 también llegaron el soporte para Anthropic Claude Enterprise (agosto) y la integración con Global Secure Access (septiembre), que detecta actividad riesgosa en la red vía IRM.

Los agentes son el nuevo «insider»: la política **Risky Agents** cubre agentes de Copilot Studio, Microsoft Foundry y los creados con el SDK P4AI, y detecta prompts riesgosos, respuestas sensibles, acceso a archivos sensibles o a sitios riesgosos, compartir hacia afuera y actividad por encima de su línea base; el riesgo del agente se comparte con DSPM for AI y el centro de administración de Microsoft 365. Learn todavía la marca en vista previa, mientras el Centro de mensajes anunció su disponibilidad general entre junio y julio de 2026 con Microsoft 365 E7 o Agent 365 como requisito. La postura de IA y los agentes se profundizan en el programa de DSPM (módulos I2 y M2).

**Por qué importa**

La IA multiplica la velocidad con la que un dato sale de su contexto, y los agentes actúan con permisos reales sin que nadie revise cada paso. Medir el riesgo de ambos con alcance acotado y apps seleccionadas permite habilitar la IA con confianza, controlar el costo de pago por uso y responder la pregunta del directorio: «¿quién vigila a los agentes?».

**Qué vas a lograr**

- Configurar Risky AI usage con las extensiones de navegador y un alcance piloto.
- Seleccionar las apps de IA a monitorear y presupuestar el pago por uso.
- Explicar el alcance, los límites y el licenciamiento de Risky Agents (E7 / Agent 365).
- Interpretar el riesgo de agentes compartido con DSPM for AI y con la Protección adaptativa.
- Coordinar con los programas de DSPM y de Communication Compliance sin duplicar controles.

> **Atención.** Cuidado con el costo: la interacción con Microsoft 365 Copilot no genera cargos de pago por uso, pero sí las Copilot experiences con datos que no son de Microsoft 365 (Fabric, Security Copilot, Copilot Studio y apps conectadas), las Enterprise AI apps y las Other AI apps detectadas por el navegador; los indicadores de Azure AI Content Safety crean una política de Communication Compliance ([indicadores](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-policy-indicators)). Desde junio de 2026 (disponibilidad general) puedes elegir qué apps de IA monitorear ([What's new](https://learn.microsoft.com/en-us/purview/whats-new)).

> **Atención.** Risky Agents: [MC1200579](https://mc.merill.net/message/MC1200579) reprogramó su disponibilidad general para mediados de junio a fines de julio de 2026 (Roadmap 516032) e incluye agentes de Agent 365, y [MC1280556](https://message.cengizyilmaz.net/message/mc1280556-microsoft-purview-for-agents-ai-observability-and-insider-risk-management-now-generally-available) la anuncia en disponibilidad general, con la condición de que no está disponible sin Microsoft 365 E7 o Agent 365. Sin embargo, las páginas de plantillas, de indicadores y de [monitoreo de agentes](https://learn.microsoft.com/en-us/purview/insider-risk-management-monitoring-agents) (4 de agosto de 2026) siguen diciendo «preview». Trátala como vista previa hasta que Learn cambie.

> **Consejo Ninja.** Límites de Risky Agents: viene activa por defecto en organizaciones con licencias compatibles y puede eliminarse si no quieres monitorear agentes; con usuarios invitados solo se ven indicadores de tipos de información sensible (no el contenido) y las unidades administrativas no admiten alertas de agentes ([monitoreo de agentes](https://learn.microsoft.com/en-us/purview/insider-risk-management-monitoring-agents); [MC1200579](https://mc.merill.net/message/MC1200579)). El riesgo del agente alimenta la observabilidad de IA de DSPM ([novedades de Purview en Ignite 2025](https://techcommunity.microsoft.com/blog/microsoft-security-blog/empowering-organizations-with-integrated-data-security-what%E2%80%99s-new-in-microsoft-p/4470663)).

> **Novedad.** Hitos de 2026 en IA: disponibilidad general de las protecciones de seguridad de datos y cumplimiento para Agent 365 (mayo), soporte de Purview para Anthropic Claude Enterprise con IRM incluido (agosto) e integración con Global Secure Access para la seguridad de datos en la red, que también detecta actividad riesgosa vía IRM (septiembre) ([What's new](https://learn.microsoft.com/en-us/purview/whats-new)). La seguridad de datos en la red con Global Secure Access exige Microsoft 365 E7, o Purview más Entra Internet Access; con un SASE de terceros, Purview más pago por uso ([seguridad de datos en la red](https://learn.microsoft.com/en-us/purview/dlp-network-data-security-learn)).

**¿Tienes poco tiempo?**

- [Monitoring agents with Insider Risk Management](https://learn.microsoft.com/en-us/purview/insider-risk-management-monitoring-agents) · Documentación
- [Learn about Insider Risk Management policy templates](https://learn.microsoft.com/en-us/purview/insider-risk-management-policy-templates) · Documentación
- [Configure policy indicators in Insider Risk Management](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-policy-indicators) · Documentación
- [MC1200579 - Microsoft Purview | Insider risk management - Insider risk management for risky agents](https://mc.merill.net/message/MC1200579) · Documentación

### Documentación, cursos y credenciales

- [Monitoring agents with Insider Risk Management](https://learn.microsoft.com/en-us/purview/insider-risk-management-monitoring-agents) · Documentación · Oficial · Vista previa · Nuevo · Microsoft Learn · 4 ago 2026. Documenta la política Risky Agents (preview), desplegada por defecto, que detecta prompts riesgosos, respuestas o accesos a datos sensibles y sitios riesgosos en agentes de Copilot Studio, Microsoft Foundry y SDK. *Nota:* Las unidades administrativas no soportan alertas de agentes; con invitados solo se ven indicadores de información sensible, no el prompt completo; el riesgo del agente se comparte con DSPM for AI y el centro de administración de Microsoft 365
- [MC1200579 - Microsoft Purview | Insider risk management - Insider risk management for risky agents](https://mc.merill.net/message/MC1200579) · Documentación · Oficial · Nuevo · Microsoft 365 Message Center (archivo mc.merill.net) · 21 may 2026. Aviso oficial que extiende IRM a agentes de IA (Copilot Studio, Foundry y Agent 365) con una política Risky Agents desplegada automáticamente y una sección Agents en el portal.

### Anuncios y blogs oficiales

- [Empowering organizations with integrated data security: What's new in Microsoft Purview (Ignite 2025)](https://techcommunity.microsoft.com/blog/microsoft-security-blog/empowering-organizations-with-integrated-data-security-what%E2%80%99s-new-in-microsoft-p/4470663) · Blog oficial · Empleado de Microsoft · Raman Kalyan · Microsoft Tech Community · 18 nov 2025. Resumen oficial de novedades de Purview en Ignite 2025, incluida la observabilidad de IA con inventario de agentes y nivel de riesgo por agente en DSPM unificado.

### Webinars, videos y podcasts

- [Prevent data loss and insider risks for Microsoft 365 Copilot with Microsoft Purview](https://techcommunity.microsoft.com/event/microsoft-copilot-events/prevent-data-loss-and-insider-risks-for-microsoft-365-copilot-with-microsoft-pur/4420208) · Webinar · Empleado de Microsoft · Microsoft (AMA con Jeremy Chapman y equipo) · Microsoft Tech Community (Copilot Control System Digital Deep Dive) · 17 jun 2025. Sesión AMA sobre cómo DLP e IRM protegen interacciones de Copilot y agentes, con preguntas reales sobre privacidad (RGPD) de prompts y respuestas.

**Manos a la obra**

1. `Laboratorio parcial` Risky AI usage: despliega la extensión Microsoft Insider risk (Edge) o Microsoft Purview (Chrome), crea la política desde DSPM for AI o desde IRM con alcance a dos usuarios de prueba y genera prompts con datos sensibles sintéticos en un sitio de IA de prueba ([plantillas](https://learn.microsoft.com/en-us/purview/insider-risk-management-policy-templates); [indicadores](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-policy-indicators)). Evidencia: actividad y alerta resultante. Limitaciones: Microsoft 365 Copilot requiere una licencia que la prueba E5 no incluye, y las apps que no son de Microsoft 365 son de pago por uso (vincula Azure, deja solo las apps necesarias y fija un presupuesto).
2. `Laboratorio parcial` Selección de apps de IA (disponibilidad general desde junio de 2026): deja solo dos apps monitoreadas, documenta el motivo de cada una y estima el costo de pago por uso del piloto ([What's new](https://learn.microsoft.com/en-us/purview/whats-new); [indicadores](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-policy-indicators)). Evidencia: ficha de decisión con el presupuesto. Limitación: la selección afecta a indicadores de pago por uso; sin facturación vinculada solo podrás documentar la decisión.
3. `Laboratorio parcial` Risky Agents: crea un agente de Copilot Studio (prueba) que consulte un sitio con datos sensibles de prueba, ejercítalo con prompts de riesgo y revisa la política de agentes y la sección Agents ([monitoreo de agentes](https://learn.microsoft.com/en-us/purview/insider-risk-management-monitoring-agents)). Evidencia: actividad del agente y su nivel de riesgo. Limitación: según MC1280556, la cobertura de agentes requiere Microsoft 365 E7 o Agent 365, que el laboratorio puede no tener ([descripción del servicio](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)).
4. `Laboratorio parcial` Privacidad en IA: con la seudonimización activa, revisa qué contenido de prompts y respuestas ve cada rol y qué ocurre con un usuario invitado (solo indicadores de tipos de información sensible) ([monitoreo de agentes](https://learn.microsoft.com/en-us/purview/insider-risk-management-monitoring-agents); [privacidad](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-privacy)). Evidencia: tabla de visibilidad por rol para la evaluación de impacto. Limitación: depende de haber capturado actividad de IA en los ejercicios anteriores, que requieren licencias de Copilot o pago por uso.
5. `Solo producción` Risky AI usage con usuarios reales requiere aprobaciones previas de Legal, RR. HH., privacidad y, cuando corresponda, la representación de los trabajadores ([plantillas](https://learn.microsoft.com/en-us/purview/insider-risk-management-policy-templates); [Get started](https://learn.microsoft.com/en-us/purview/insider-risk-management-configure)). Cómo hacerlo seguro: seudonimización activa, piloto informado de 30 días, empezar solo con visitas a sitios de IA (sin revisar contenido de prompts), apps seleccionadas y presupuesto de pago por uso con alertas.
6. `Solo producción` Agentes con Microsoft 365 E7 o Agent 365: confirma la licencia, inventaría los agentes con actividad y elige uno o dos de bajo riesgo cuyo dueño sea TI ([MC1280556](https://message.cengizyilmaz.net/message/mc1280556-microsoft-purview-for-agents-ai-observability-and-insider-risk-management-now-generally-available)). Cómo hacerlo seguro: política de agentes separada de la de usuarios, revisión semanal del riesgo compartido con DSPM for AI y un criterio documentado para desactivar un agente. La postura de agentes se profundiza en el programa de DSPM (M2).

<a id="a2"></a>

## A2 · Integración con Defender XDR y Sentinel

*L400 · ~6 h · Origen: Nuevo en esta edición; se apoya en el Virtual Ninja Show de Defender XDR (febrero de 2025)*

El SOC ve ataques externos; IRM ve comportamiento. Al activar el uso compartido de datos, las alertas de IRM llegan a los **incidentes de Defender XDR** (en *prerelease*; documento actualizado el 17 de febrero de 2025), se correlacionan con alertas de DLP y de Entra, el riesgo interno aparece en la página del usuario y el estado se sincroniza en 30 minutos o menos. Para verlas, el analista necesita Security Operator o Security Reader en Defender y pertenecer a IRM, IRM Analysts o IRM Investigators. Así el SOC distingue mejor una cuenta comprometida de una amenaza interna.

Hay límites que conviene conocer: todavía no se integran la exfiltración por correo, los eventos de Risky AI usage, las apps cloud de terceros, los eventos previos a la alerta ni las exclusiones, y los incidentes de IRM no contienen alertas, lo que puede romper automatizaciones de Sentinel; Microsoft recomienda usar el conector de IRM para Sentinel o desactivar el uso compartido. En la búsqueda avanzada están AlertInfo, AlertEvidence y las tablas **DataSecurityEvents** y **DataSecurityBehaviors** (vista previa), que solo se pueblan si compartes las alertas con Defender.

Del lado de Sentinel, la solución de IRM del Content hub trae conector, libro, reglas analíticas, consultas de caza y un playbook; el conector depende de exportar alertas por la Office 365 Management Activity API, que corre cada 60 minutos y **no conserva la seudonimización**. Además, el Centro de mensajes anunció los resúmenes del Triage Agent en las alertas de IRM del portal de Defender, con disponibilidad general prevista para diciembre de 2026. Los incidentes y la caza se profundizan en el programa de Defender XDR (módulos M1 y M9) y la ingesta, en el de Sentinel (M2).

**Por qué importa**

Correlacionar señales internas y externas acelera la respuesta y evita errores costosos, como tratar como insider a la víctima de un robo de credenciales. Pero compartir datos de riesgo interno con el SOC amplía quién ve información sensible: decidir qué se comparte, con quién y por qué canal es tan importante como la integración técnica.

**Qué vas a lograr**

- Activar el uso compartido de datos y asignar los roles mínimos para el SOC.
- Investigar incidentes de IRM en Defender XDR y explicar qué datos todavía no llegan.
- Escribir consultas KQL sobre DataSecurityEvents y DataSecurityBehaviors.
- Decidir entre el uso compartido y el conector de Sentinel considerando automatizaciones y seudonimización.
- Diseñar un traspaso entre el SOC y el equipo de riesgo interno con datos mínimos.

> **Atención.** La integración de IRM con Defender XDR sigue en *prerelease* (documento actualizado el 17 de febrero de 2025), aunque [MC1438568](https://mc.merill.net/message/MC1438568) ya suma los resúmenes del Triage Agent en Defender, con vista previa entre mediados de agosto e inicios de septiembre de 2026 y disponibilidad general prevista entre inicios y fines de diciembre de 2026. El estado de disponibilidad general de la integración base no está confirmado ([IRM en Defender XDR](https://learn.microsoft.com/en-us/defender-xdr/irm-investigate-alerts-defender)).

> **Atención.** Los incidentes de IRM no contienen alertas, lo que puede romper automatizaciones de Sentinel: Microsoft recomienda el conector de IRM para Sentinel o desactivar el uso compartido. Todavía no llegan la exfiltración por correo, los eventos de Risky AI usage, las apps cloud de terceros, los eventos previos a la alerta ni las exclusiones ([IRM en Defender XDR](https://learn.microsoft.com/en-us/defender-xdr/irm-investigate-alerts-defender)).

> **Atención.** La exportación de alertas por la Office 365 Management Activity API —base del conector de Sentinel— corre cada 60 minutos, viene desactivada y **no** conserva la seudonimización; la exportación a CSV sí ([compartir datos de IRM](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-share-data); [conectores de API de Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/connect-services-api-based)). Decide con privacidad antes de activarla.

> **Consejo Ninja.** Para cazar, combina AlertInfo y AlertEvidence con DataSecurityEvents (eventos de usuario enriquecidos por IRM) y DataSecurityBehaviors (comportamientos agregados por día, con técnicas de MITRE), ambas en vista previa; requieren IRM Analysts o IRM Investigators y solo se pueblan si compartes las alertas ([DataSecurityEvents](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-datasecurityevents-table); [DataSecurityBehaviors](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-datasecuritybehaviors-table)). La caza se profundiza en el programa de Defender XDR (M9).

**¿Tienes poco tiempo?**

- [Investigate insider risk threats in the Microsoft Defender portal with insights from Microsoft Purview Insider Risk Management](https://learn.microsoft.com/en-us/defender-xdr/irm-investigate-alerts-defender) · Documentación
- [DataSecurityEvents table in the advanced hunting schema](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-datasecurityevents-table) · Documentación
- [Defender XDR's Data Security Context with Insider Risk Management](https://learn.microsoft.com/en-us/shows/microsoft-sentinel-defender-xdr-virtual-ninja-training/defender-xdrs-data-security-context-with-insider-risk-management) · Webinar
- [Microsoft Purview Insider Risk Management (solución de Microsoft Sentinel)](https://marketplace.microsoft.com/en-us/product/azuresentinel.azure-sentinel-solution-insiderriskmanagement) · Herramienta

**Qué comparte IRM con Defender XDR (noviembre de 2026)**

| Elemento | ¿Llega a Defender XDR? | Comentario |
|---|---|---|
| Alertas de IRM agrupadas en incidentes | Sí (prerelease) | Requiere activar el uso compartido de datos en IRM |
| Estado de la alerta | Sí | Se sincroniza en 30 minutos o menos |
| Riesgo interno en la página del usuario | Sí | Visible para roles de Defender que además pertenecen a IRM, IRM Analysts o IRM Investigators |
| DataSecurityEvents y DataSecurityBehaviors | Sí (vista previa) | Solo si compartes las alertas; requieren IRM Analysts o IRM Investigators |
| Alertas dentro del incidente de IRM | No | Puede romper automatizaciones de Sentinel: usa el conector de IRM o desactiva el uso compartido |
| Exfiltración por correo | Todavía no | Investígala en IRM |
| Eventos de Risky AI usage | Todavía no | Investígalos en IRM |
| Apps cloud de terceros | Todavía no | Investígalas en IRM |
| Eventos previos a la alerta y exclusiones | Todavía no | El contexto previo queda en IRM |
| Resúmenes del Triage Agent | Vista previa desde agosto–septiembre de 2026 | Disponibilidad general prevista entre inicios y fines de diciembre de 2026 (MC1438568) |
| Niveles de riesgo para alertas de Defender y DLP | Vista previa | IRM analiza entre 90 y 120 días de actividad |

Fuentes: [IRM en Defender XDR](https://learn.microsoft.com/en-us/defender-xdr/irm-investigate-alerts-defender) · [MC1438568](https://mc.merill.net/message/MC1438568) · [Get started](https://learn.microsoft.com/en-us/purview/insider-risk-management-configure).

### Documentación, cursos y credenciales

- [Connect Microsoft Sentinel to other Microsoft services with an API-based data connector](https://learn.microsoft.com/en-us/azure/sentinel/connect-services-api-based) · Documentación · Oficial · Nuevo · Microsoft Learn · 2 jul 2026. Requisitos de los conectores API de Sentinel, incluido el de Microsoft Purview Insider Risk Management (licencia E5/A5/G5 o add-on, IRM con políticas activas y exportación de alertas a la Office 365 Management Activity API).
- [DataSecurityBehaviors table in the advanced hunting schema](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-datasecuritybehaviors-table) · Documentación · Oficial · Vista previa · Microsoft Learn. Referencia de la tabla de Advanced Hunting con comportamientos de seguridad de datos agregados por día (exfiltración, ofuscación, IA riesgosa) generados por IRM, con técnicas MITRE. *Nota:* Solo se puebla si la organización comparte alertas de IRM con Defender; algunas versiones localizadas aún la marcan como preview
- [DataSecurityEvents table in the advanced hunting schema](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-datasecurityevents-table) · Documentación · Oficial · Vista previa · Microsoft Learn. Referencia de la tabla de Advanced Hunting con eventos individuales de usuario enriquecidos por IRM (DLP, etiquetas, medios extraíbles, acceso físico, Teams, correo). *Nota:* Requiere compartir alertas de IRM con Defender; útil para consultas KQL que correlacionen IRM con identidad y endpoint
- [Investigate insider risk threats in the Microsoft Defender portal with insights from Microsoft Purview Insider Risk Management](https://learn.microsoft.com/en-us/defender-xdr/irm-investigate-alerts-defender) · Documentación · Oficial · Vista previa · Microsoft Learn · 17 feb 2025. Explica cómo ver alertas de IRM agrupadas en incidentes de Defender XDR, correlacionarlas con DLP y Entra, cazarlas en Advanced Hunting y ver el riesgo en la página de usuario. *Nota:* Requiere activar el uso compartido de datos en IRM, roles de Defender (Security Operator/Reader) y pertenecer a un grupo de roles de IRM; documenta permisos de Graph security API para SIEM…
- [MC1438568 - Microsoft Purview | Insider Risk Management triage agent summaries available in Microsoft Defender](https://mc.merill.net/message/MC1438568) · Documentación · Oficial · Vista previa · Nuevo · Microsoft 365 Message Center (archivo mc.merill.net) · 24 jul 2026. Los resúmenes del triage agent de IRM aparecerán en las alertas de IRM dentro del portal de Microsoft Defender si se comparten alertas y el agente está activo. *Nota:* Preview mediados de ago - inicios de sep-2026; GA prevista inicios - fines de dic-2026 (Roadmap 567472)

### Webinars, videos y podcasts

- [Defender XDR's Data Security Context with Insider Risk Management](https://learn.microsoft.com/en-us/shows/microsoft-sentinel-defender-xdr-virtual-ninja-training/defender-xdrs-data-security-context-with-insider-risk-management) · Webinar · Empleado de Microsoft · Maayan Magenheim y Sravan Kumar Mera · Microsoft Learn Shows (Sentinel & Defender XDR Virtual Ninja Training) · 5 feb 2025. Sesión del Virtual Ninja Training que demuestra la integración de IRM en Defender XDR para distinguir amenazas internas y externas y correlacionar alertas.

### Laboratorios, GitHub y herramientas

- [Microsoft Purview Insider Risk Management (solución de Microsoft Sentinel)](https://marketplace.microsoft.com/en-us/product/azuresentinel.azure-sentinel-solution-insiderriskmanagement) · Herramienta · Oficial · Microsoft Sentinel (Microsoft Corporation) · Microsoft Marketplace. Solución del Content hub de Sentinel con conector de datos, workbook, 5 reglas analíticas, 5 consultas de caza y 1 playbook para investigar riesgo interno junto con otras señales Microsoft.

**Manos a la obra**

1. `Laboratorio parcial` Activa el uso compartido de datos en IRM, asigna Security Reader e IRM Analysts a una cuenta del SOC y filtra los incidentes por la fuente «Microsoft Purview Insider Risk Management» ([IRM en Defender XDR](https://learn.microsoft.com/en-us/defender-xdr/irm-investigate-alerts-defender)). Evidencia: incidente con la alerta de IRM y la página del usuario. Limitación: es *prerelease* y los incidentes de IRM no traen alertas para las automatizaciones de Sentinel.
2. `Laboratorio parcial` Consulta en la búsqueda avanzada la tabla DataSecurityEvents para un usuario de prueba durante siete días y DataSecurityBehaviors para ver la agregación diaria; guarda ambas consultas KQL ([DataSecurityEvents](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-datasecurityevents-table); [DataSecurityBehaviors](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-datasecuritybehaviors-table)). Evidencia: consultas y resultados. Limitación: las tablas solo se pueblan si compartes alertas, y el volumen del laboratorio es bajo.
3. `Laboratorio` En un workspace de Sentinel de laboratorio, instala la solución de IRM desde el Content hub, activa «Export alerts» en IRM y verifica la llegada de datos en la hora siguiente; comprueba que los nombres llegan sin seudonimizar ([solución de Sentinel](https://marketplace.microsoft.com/en-us/product/azuresentinel.azure-sentinel-solution-insiderriskmanagement); [conectores de API](https://learn.microsoft.com/en-us/azure/sentinel/connect-services-api-based); [compartir datos](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-share-data)). Evidencia: memo de decisión de privacidad sobre el uso del conector.
4. `Laboratorio` Revisa las reglas de automatización y los playbooks de Sentinel que dependan de alertas dentro de incidentes y documenta el impacto de los incidentes de IRM sin alertas; decide entre uso compartido y conector ([IRM en Defender XDR](https://learn.microsoft.com/en-us/defender-xdr/irm-investigate-alerts-defender)). Evidencia: matriz de decisión firmada por el líder del SOC y por privacidad.
5. `Laboratorio` Mira la sesión del [Virtual Ninja Show sobre IRM en Defender XDR](https://learn.microsoft.com/en-us/shows/microsoft-sentinel-defender-xdr-virtual-ninja-training/defender-xdrs-data-security-context-with-insider-risk-management) y redacta un procedimiento de traspaso para dos escenarios: cuenta comprometida (lo lleva el SOC) y posible amenaza interna (lo lleva el equipo de riesgo interno). Evidencia: procedimiento de una página con criterios de traspaso.
6. `Solo producción` Traspaso SOC–IRM en producción: define qué analistas del SOC ven incidentes de IRM (Security Reader más IRM Analysts, solo para personas designadas) y qué datos mínimos reciben ([IRM en Defender XDR](https://learn.microsoft.com/en-us/defender-xdr/irm-investigate-alerts-defender)). Cómo hacerlo seguro: piloto con dos analistas, revisión mensual de accesos con IRM Auditors y ninguna exportación de alertas a sistemas sin control de privacidad. Los incidentes se profundizan en el programa de Defender XDR (M1).

<a id="a3"></a>

## A3 · Triage Agent de Insider Risk Management con Security Copilot

*L400 · ~4 h · Origen: Nuevo en esta edición*

El agente de triage de IRM se anunció en vista previa el 24 de marzo de 2025 como Alert Triage Agent, llegó a disponibilidad general entre fines de noviembre y mediados de diciembre de 2025 y cambió de nombre dos veces: «Data Security Triage Agent» en el Centro de mensajes y **Microsoft Purview Triage Agent** en Learn. Clasifica las alertas en **Needs attention**, **Less urgent** y **Not categorized**, aprende de la retroalimentación del analista y, desde octubre de 2026, trabaja dentro de la cola unificada. En 2026 sumó priorización según el riesgo del usuario y contexto ampliado (rol, último día laboral e historial), que no se activa por defecto.

Sus requisitos son precisos: tenant incorporado a Security Copilot, uso compartido de datos de Microsoft 365 activado y plugin de Purview habilitado; según Learn, además, la licencia por usuario de IRM, el modelo de **pago por uso** y **SCU** aprovisionadas. Hay una sola instancia por tenant, la primera pasada tarda hasta 2 horas y el agente corre con el contexto del último usuario que guardó su configuración: esa autenticación vence a los 90 días. Desde el 18 de noviembre de 2025, Microsoft 365 E5 y E7 incluyen Security Copilot con 400 SCU al mes por cada 1.000 licencias pagas (hasta 10.000), algo que un tenant de prueba no garantiza.

Un punto de privacidad: el panel del agente **no** seudonimiza los nombres en las alertas priorizadas. Las SCU y el gobierno de agentes se profundizan en el programa de Security Copilot (módulos I2 y M6), y el agente equivalente de DLP, en el programa de Purview DLP (módulo A4).

**Por qué importa**

El cuello de botella del riesgo interno es el tiempo de triage. Un agente que ordena la cola permite que los analistas dediquen su tiempo a lo que realmente necesita atención; pero consume SCU, muestra nombres y depende de una autenticación que vence. Es una decisión de valor, costo y privacidad que conviene medir, no suponer.

**Qué vas a lograr**

- Verificar los prerrequisitos técnicos y de licencia del Triage Agent.
- Desplegar y configurar el agente y explicar sus categorías.
- Dar retroalimentación al agente y medir su efecto en la priorización.
- Monitorear el consumo de SCU y planificar la reautenticación cada 90 días.
- Definir controles de privacidad sobre quién ve el panel del agente.

> **Atención.** Licencia del Triage Agent: Learn exige la licencia por usuario de IRM, el modelo de pago por uso y SCU aprovisionadas ([Triage Agent](https://learn.microsoft.com/en-us/purview/copilot-in-purview-triage-irm-agent-get-started)), mientras que la inclusión de Security Copilot en Microsoft 365 E5 y E7 aporta 400 SCU al mes por cada 1.000 licencias pagas, hasta 10.000, desde el 18 de noviembre de 2025 ([inclusión de Security Copilot](https://learn.microsoft.com/en-us/copilot/security/security-copilot-inclusion)). Valida en tu tenant si además hace falta vincular una suscripción de Azure.

> **Atención.** Privacidad: el panel del Triage Agent **no** seudonimiza los nombres de usuario en las alertas priorizadas ([privacidad de nombres de usuario](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-privacy)). Restringe quién lo ve y regístralo en la evaluación de impacto.

> **Novedad.** [MC1246005](https://mc.merill.net/message/MC1246005) agregó priorización según el riesgo del usuario, patrones de comportamiento resumidos y contexto ampliado (rol, último día laboral, historial): vista previa entre marzo y abril y disponibilidad general entre fines de junio y fines de julio de 2026; no se habilita por defecto. Antes, [MC1180884](https://message.cengizyilmaz.net/message/mc1180884-microsoft-purview-insider-risk-management-data-security-alert-triage-agent-generally-available) había anunciado la disponibilidad general (fines de noviembre a mediados de diciembre de 2025, Roadmap 503764), con las instrucciones personalizadas deshabilitadas temporalmente.

> **Consejo Ninja.** El agente corre con el contexto del último usuario que guardó su configuración y esa autenticación vence a los 90 días: agenda la renovación ([Triage Agent](https://learn.microsoft.com/en-us/purview/copilot-in-purview-triage-irm-agent-get-started)). Para gestionarlo se requiere además el rol Purview Content Analyst del grupo Purview Agent Management, y algunas páginas todavía lo titulan «(preview)» pese a la disponibilidad general ([agentes de Security Copilot en Purview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-agents)).

**¿Tienes poco tiempo?**

- [Get started with the Microsoft Purview Triage Agent in Insider Risk Management](https://learn.microsoft.com/en-us/purview/copilot-in-purview-triage-irm-agent-get-started) · Documentación
- [Learn about Security Copilot for Microsoft 365 E5 and E7 customers](https://learn.microsoft.com/en-us/copilot/security/security-copilot-inclusion) · Documentación
- [New Agents in Microsoft Purview](https://techcommunity.microsoft.com/blog/microsoftmechanicsblog/new-agents-in-microsoft-purview/4478096) · Video
- [Microsoft Security Copilot agents in Microsoft Purview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-agents) · Documentación

### Documentación, cursos y credenciales

- [Get started with the Microsoft Purview Triage Agent in Insider Risk Management](https://learn.microsoft.com/en-us/purview/copilot-in-purview-triage-irm-agent-get-started) · Documentación · Oficial · Nuevo · Microsoft Learn · 26 jun 2026. Requisitos y pasos para desplegar el Triage Agent de IRM: licencias, SCU, roles para administradores y analistas y hoja de ruta de configuración.
- [Learn about Security Copilot for Microsoft 365 E5 and E7 customers](https://learn.microsoft.com/en-us/copilot/security/security-copilot-inclusion) · Documentación · Oficial · Microsoft Learn. Explica la inclusión de Security Copilot en Microsoft 365 E5 y E7: 400 SCU/mes por cada 1.000 licencias pagas (hasta 10.000), aprovisionamiento automático y despliegue gradual desde el 18-nov-2025.
- [Microsoft Security Copilot agents in Microsoft Purview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-agents) · Documentación · Oficial · Microsoft Learn · 24 feb 2026. Ficha técnica de los agentes de triage de Purview (IRM y DLP): identidad, licencias, permisos, roles y disparadores.
- [Security Copilot Agents in Microsoft Purview overview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-agents-overview) · Documentación · Oficial · Microsoft Learn. Visión general de los agentes de Purview: Triage Agent de DLP e IRM y Posture Agent de DSPM y DSI (preview), con conceptos de disparadores e instrucciones personalizadas.
- [MC1246005 - Microsoft Purview | Insider Risk Management - Enhancements to the Data Security Triage Agent](https://mc.merill.net/message/MC1246005) · Documentación · Oficial · Microsoft 365 Message Center (archivo mc.merill.net) · 6 mar 2026. Mejoras del Data Security Triage Agent: priorización por riesgo de usuario, patrones de comportamiento resumidos y contexto ampliado (rol, último día laboral, historial).
- [MC1180884 - Microsoft Purview | Insider Risk Management - Data security alert triage agent generally available](https://message.cengizyilmaz.net/message/mc1180884-microsoft-purview-insider-risk-management-data-security-alert-triage-agent-generally-available) · Documentación · Oficial · Microsoft 365 Message Center (archivo message.cengizyilmaz.net) · 14 nov 2025. Aviso de disponibilidad general del agente de triage de alertas de IRM (Security Copilot) con feedback de priorización y retiro de la sección de riesgo de archivo.
- [Security Copilot agents in Microsoft 365 E5](https://www.microsoft.com/en-us/security/security-copilot-in-microsoft-365-e5) · Documentación · Oficial · Microsoft Security. Página comercial con preguntas frecuentes sobre los agentes de Security Copilot incluidos en Microsoft 365 E5 y la capacidad de SCU asignada.

### Anuncios y blogs oficiales

- [Agents built into your workflow: Get Security Copilot with Microsoft 365 E5](https://www.microsoft.com/en-us/security/blog/2025/11/18/agents-built-into-your-workflow-get-security-copilot-with-microsoft-365-e5/) · Blog oficial · Empleado de Microsoft · Dorothy Li · Microsoft Security Blog · 18 nov 2025. Anuncio de Ignite 2025 que incluye Security Copilot y sus agentes (incluidos los de seguridad de datos de Purview) en Microsoft 365 E5.
- [Announcing Alert Triage Agents in Microsoft Purview, powered by Security Copilot](https://techcommunity.microsoft.com/blog/microsoft-security-blog/announcing-alert-triage-agents-in-microsoft-purview-powered-by-security-copilot/4396041) · Blog oficial · Empleado de Microsoft · Legado aún útil · Nathalia Borges · Microsoft Tech Community · 24 mar 2025. Anuncio original de los agentes de triage de alertas para DLP e IRM, con categorías Needs attention/Less urgent y ajuste por feedback en lenguaje natural. *Nota:* Hoy se denomina Data Security Triage Agent / Triage Agent in Insider Risk Management; GA en nov-dic 2025 y unificado con la cola de alertas en oct-2026

### Webinars, videos y podcasts

- [New Agents in Microsoft Purview](https://techcommunity.microsoft.com/blog/microsoftmechanicsblog/new-agents-in-microsoft-purview/4478096) · Video · Oficial · Microsoft Mechanics · Microsoft Mechanics (Tech Community) · 18 dic 2025. Episodio de Mechanics que muestra el Data Security Triage Agent (prioriza alertas de IRM/DLP y contacta usuarios por Teams) y el Data Security Posture Agent.
- [Introducing Microsoft Purview Alert Triage Agents for Data Loss Prevention & Insider Risk Management (Microsoft Mechanics Podcast)](https://microsoftmechanics.libsyn.com/podcast/introducing-microsoft-purview-alert-triage-agents-for-data-loss-prevention-insider-risk-management) · Podcast · Empleado de Microsoft · Legado aún útil · Talhah Mir · Microsoft Mechanics · 16 jun 2025. Demostración de los agentes de triage de alertas de DLP e IRM: personalización, priorización, calibración con feedback y seguimiento de uso. *Nota:* Hoy el agente se llama Data Security Triage Agent y su cola se unificó en oct-2026; Talhah Mir era entonces Principal GPM de Purview (dejó Microsoft en ago-2026). Rol de autor válido a la fecha de publicación

**Manos a la obra**

1. `Laboratorio parcial` Despliegue del Triage Agent: aprovisiona 1 SCU por unas horas (y elimínala al terminar), habilita el plugin de Purview, verifica el uso compartido de datos de Microsoft 365 y despliega el agente sobre las políticas de prueba ([Triage Agent](https://learn.microsoft.com/en-us/purview/copilot-in-purview-triage-irm-agent-get-started)). Evidencia: primera pasada completada (hasta 2 horas) y distribución de alertas por categoría. Limitación: la prueba E5 puede no recibir SCU incluidas, porque se calculan sobre licencias pagas ([inclusión](https://learn.microsoft.com/en-us/copilot/security/security-copilot-inclusion)), y 1 SCU aprovisionada cuesta USD 4 por hora.
2. `Laboratorio parcial` Da retroalimentación sobre tres categorizaciones del agente y observa si cambia la priorización; registra el consumo de SCU de la sesión ([agentes de Purview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-agents-overview)). Evidencia: categorías antes y después y SCU consumidas. Limitación: con pocas alertas el efecto del aprendizaje es poco visible.
3. `Laboratorio` Ficha de gobierno del agente: responsable del servicio (quien guarda la configuración), calendario de reautenticación cada 90 días, roles necesarios (Purview Content Analyst y grupos de IRM), quién ve el panel sin seudonimización y presupuesto de SCU ([agentes de Security Copilot en Purview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-agents); [privacidad](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-privacy)). Evidencia: ficha aprobada por privacidad.
4. `Laboratorio` Mira [New Agents in Microsoft Purview](https://techcommunity.microsoft.com/blog/microsoftmechanicsblog/new-agents-in-microsoft-purview/4478096) y compara lo que muestra con tu laboratorio actual (nombre del agente, cola unificada, categorías y contexto). Evidencia: lista de diferencias con su fecha.
5. `Solo producción` Medir el valor del agente con alertas reales: compara durante 30 días el tiempo hasta el triage de «Needs attention» frente al resto y el porcentaje de categorizaciones corregidas por analistas ([Triage Agent](https://learn.microsoft.com/en-us/purview/copilot-in-purview-triage-irm-agent-get-started); [informes](https://learn.microsoft.com/en-us/purview/insider-risk-management-reports)). Cómo hacerlo seguro: agente sobre alertas nuevas y pocas políticas, revisión mensual de SCU, acceso al panel solo para analistas autorizados y decisión documentada de continuar o apagar. Las SCU se profundizan en el programa de Security Copilot (I2).

<a id="a4"></a>

## A4 · Automatización y APIs: Power Automate, exportación de alertas y conectores

*L400 · ~5 h · Origen: Nuevo en esta edición*

La automatización acorta el tiempo entre una alerta y una acción, pero en riesgo interno cada flujo es también un flujo de datos personales. IRM ofrece **flujos de Power Automate** (vista previa) con plantillas para notificar al usuario incluido en una política, pedir información a RR. HH. o al negocio, avisar al gerente y crear un registro en ServiceNow. Las plantillas recomendadas no requieren licencias adicionales de Power Automate (las funciones premium o los conectores personalizados sí podrían), y con la seudonimización activa no funcionan como se espera.

Para llevar datos a otros sistemas, el **uso compartido de datos** exporta alertas por la Office 365 Management Activity API —cada 60 minutos, desactivado por defecto y sin conservar la seudonimización, a diferencia de la exportación a CSV—, las comparte con Defender XDR y comparte los niveles de riesgo con DLP y Defender. Microsoft recomienda migrar de esa API a la **Graph security API**, con permisos como SecurityIncident, SecurityAlert, SecurityEvents y ThreatHunting, para alimentar un SIEM o un sistema de tickets.

En la dirección inversa, el conector **Insider Risk Indicators** (vista previa) trae detecciones de terceros —por ejemplo, de Salesforce o Dropbox— ya agregadas por un SIEM como Sentinel o Splunk, para usarlas como disparadores o indicadores personalizados en las plantillas Data theft y Data leaks; no acepta señales crudas y, tras cada cambio, hay que esperar 24 horas antes de cargar datos. La carga del conector de RR. HH. también se automatiza con un script diario o una plantilla de Power Automate.

**Por qué importa**

Automatizar bien reduce de días a minutos el traspaso a RR. HH. o al SOC y elimina pasos manuales propensos a error. Automatizar mal publica identidades fuera del alcance de la seudonimización. Documentar cada flujo —qué datos mueve, a quién y con qué permisos— es lo que permite auditarlo y sostenerlo frente a privacidad.

**Qué vas a lograr**

- Construir un flujo de Power Automate para IRM y documentar los datos que mueve.
- Configurar la exportación de alertas y evaluar su impacto en la seudonimización.
- Consumir alertas de IRM con la Graph security API para un SIEM o un sistema de tickets.
- Importar detecciones de terceros como indicadores personalizados.
- Programar y supervisar la carga del conector de RR. HH.

> **Atención.** Las plantillas de Power Automate para IRM (vista previa) no requieren licencias adicionales en sus versiones recomendadas, pero las funciones premium o los conectores personalizados podrían; con la seudonimización activa, estas plantillas no funcionan como se espera ([Power Automate en IRM](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-power-automate)). Decide con privacidad qué flujos justifican revelar identidades.

> **Atención.** La exportación de alertas por la Office 365 Management Activity API ocurre cada 60 minutos, está desactivada por defecto y **no** conserva la seudonimización; la exportación a CSV sí la conserva ([compartir datos de IRM](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-share-data)).

> **Consejo Ninja.** Microsoft recomienda migrar de la Office 365 Management Activity API a la Graph security API; los permisos documentados para llevar datos de IRM a un SIEM o a un sistema de tickets son SecurityIncident, SecurityAlert, SecurityEvents y ThreatHunting ([IRM en Defender XDR](https://learn.microsoft.com/en-us/defender-xdr/irm-investigate-alerts-defender)).

> **Consejo Ninja.** El conector Insider Risk Indicators (vista previa) solo acepta agregaciones preprocesadas en CSV (no señales crudas), sus indicadores personalizados solo sirven en las plantillas Data theft y Data leaks, y tras actualizar un indicador hay que esperar 24 horas antes de cargar datos ([conector de detecciones de terceros](https://learn.microsoft.com/en-us/purview/import-insider-risk-indicators); [indicadores](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-policy-indicators)).

**¿Tienes poco tiempo?**

- [Automate Insider Risk Management actions with Microsoft Power Automate flows](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-power-automate) · Documentación
- [Share Insider Risk Management data with other solutions](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-share-data) · Documentación
- [Set up a connector to import third-party insider risk detections (preview)](https://learn.microsoft.com/en-us/purview/import-insider-risk-indicators) · Documentación

### Documentación, cursos y credenciales

- [Share Insider Risk Management data with other solutions](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-share-data) · Documentación · Oficial · Microsoft Learn. Describe cómo exportar alertas de IRM a SIEM/SOAR vía Office 365 Management Activity API, compartirlas con Defender XDR y compartir niveles de riesgo con DLP y Communication Compliance.
- [Automate Insider Risk Management actions with Microsoft Power Automate flows](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-power-automate) · Documentación · Oficial · Microsoft Learn. Plantillas de Power Automate para IRM: notificar al usuario incluido en una política, pedir información a RR. HH./negocio, avisar al gerente y crear registro en ServiceNow.
- [Set up a connector to import third-party insider risk detections (preview)](https://learn.microsoft.com/en-us/purview/import-insider-risk-indicators) · Documentación · Oficial · Vista previa · Microsoft Learn. Conector Insider Risk Indicators (preview) para traer detecciones agregadas de terceros (p. ej. Salesforce, Dropbox vía Sentinel o Splunk) como disparadores o indicadores personalizados. *Nota:* Solo agregaciones preprocesadas en CSV (no señales crudas); los indicadores personalizados solo sirven en plantillas Data theft y Data leaks; esperar 24 h tras cambios antes de cargar datos

**Manos a la obra**

1. `Laboratorio` Crea un flujo de IRM con Power Automate (vista previa) que, al confirmar una alerta, notifique en Teams a la cuenta del investigador o cree un ticket de prueba; documenta los campos que envía y quién los recibe ([Power Automate en IRM](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-power-automate)). Evidencia: ejecución exitosa y ficha de datos del flujo.
2. `Laboratorio` Automatiza la carga del conector de RR. HH. con el script programado a diario o con la plantilla de Power Automate, y verifica que los perfiles de empleado se renuevan antes de los 30 días ([conector de RR. HH.](https://learn.microsoft.com/en-us/purview/import-hr-data)). Evidencia: historial de ejecuciones de una semana.
3. `Laboratorio parcial` Conector Insider Risk Indicators: carga un CSV agregado con detecciones sintéticas de un tercero (por ejemplo, «exportación masiva desde el CRM»), mapéalo a un indicador personalizado en una política Data leaks y espera 24 horas ([conector de detecciones de terceros](https://learn.microsoft.com/en-us/purview/import-insider-risk-indicators)). Evidencia: indicador visible en la actividad del usuario. Limitación: vista previa; en producción la agregación la hace un SIEM como Sentinel o Splunk.
4. `Laboratorio parcial` Graph security API: registra una aplicación con los permisos mínimos para leer alertas, lista las alertas de IRM compartidas con Defender y guarda la respuesta ([IRM en Defender XDR](https://learn.microsoft.com/en-us/defender-xdr/irm-investigate-alerts-defender)). Evidencia: respuesta de la API con los campos de la alerta. Limitación: requiere el uso compartido de datos activo y la integración está en *prerelease*.
5. `Laboratorio` Inventario de flujos de datos: por cada automatización (Power Automate, exportación de alertas, conector de Sentinel, Graph), registra los datos que mueve, el destino, si conserva la seudonimización, los permisos y el dueño ([compartir datos](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-share-data)). Evidencia: inventario revisado por privacidad.
6. `Solo producción` Integración con ServiceNow con tickets reales: cola restringida, campos mínimos (identificador de caso seudonimizado, severidad y política) y aprobación de privacidad ([Power Automate en IRM](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-power-automate); [casos](https://learn.microsoft.com/en-us/purview/insider-risk-management-cases)). Cómo hacerlo seguro: probar primero en una instancia de desarrollo de ServiceNow, revisar los permisos de la cola y registrar cada cambio del flujo.

<a id="reto-avanzado"></a>

## Reto del nivel

**Riesgo interno para la IA y el SOC.** Diseña e implementa en tu laboratorio: una política Risky AI usage con dos apps de IA seleccionadas y presupuesto de pago por uso; el uso compartido con Defender XDR y dos consultas KQL sobre DataSecurityEvents y DataSecurityBehaviors; un memo de decisión entre uso compartido y conector de Sentinel; el Triage Agent en una sesión con 1 SCU (o su diseño completo si no tienes SCU); y un flujo de Power Automate que abra un ticket con datos mínimos. Entrega un diagrama de arquitectura, la estimación de costos (pago por uso y SCU), el inventario de flujos de datos y los controles de privacidad de cada integración.

<a id="quiz-avanzado"></a>

## Evaluación del nivel

Responde y compara con [Evaluaciones y respuestas](06_Evaluaciones_y_respuestas.md#eval-avanzado). Con 80 % o más, ¡nivel aprobado! (En la versión web puedes corregir en línea y generar tu certificado).

1. ¿Qué interacción de IA **no** genera cargos de pago por uso en IRM?
   - a) Enterprise AI apps
   - b) Microsoft 365 Copilot
   - c) Other AI apps detectadas por el navegador
   - d) Copilot experiences con datos que no son de Microsoft 365

2. ¿Qué agentes cubre la política Risky Agents?
   - a) Solo agentes de Copilot Studio publicados en Teams
   - b) Cualquier agente de terceros, aunque no tenga conector
   - c) Copilot Studio, Microsoft Foundry y agentes creados con el SDK P4AI
   - d) Solo agentes registrados en Agent 365 con identidad propia

3. Según MC1280556, ¿qué licencia es necesaria para Insider Risk Management para agentes?
   - a) Microsoft 365 E7 o Agent 365
   - b) Microsoft Purview Suite
   - c) Microsoft Defender Suite
   - d) Microsoft 365 E3

4. ¿Qué ve el equipo de IRM cuando un usuario invitado interactúa con un agente monitoreado por Risky Agents?
   - a) El prompt completo y la respuesta del agente, como con empleados
   - b) Nada: los invitados quedan fuera de toda política de IRM
   - c) El historial de navegación del invitado durante la sesión
   - d) Solo indicadores de tipos de información sensible, no el contenido

5. ¿Qué ocurre al activar los indicadores de Azure AI Content Safety en IRM?
   - a) Se crea una política de Communication Compliance
   - b) Se desactiva la seudonimización de los prompts
   - c) Se crea automáticamente un caso de eDiscovery
   - d) Se habilita la evidencia forense del dispositivo

6. ¿Qué dato de IRM **todavía no** llega a la integración con Defender XDR?
   - a) El estado de la alerta
   - b) La severidad
   - c) Los eventos de Risky AI usage
   - d) La clasificación de la alerta

7. ¿Por qué la integración de IRM con Defender XDR puede romper automatizaciones de Sentinel?
   - a) Porque cambia el esquema de todas las tablas
   - b) Porque los incidentes de IRM no contienen alertas
   - c) Porque desactiva el conector de Defender XDR
   - d) Porque elimina la seudonimización en Sentinel

8. ¿Qué necesita un analista del SOC para ver alertas de IRM en Defender XDR?
   - a) Global Administrator, que ya incluye el acceso a los datos de IRM en Defender
   - b) Solo el grupo IRM Auditors, que exporta los registros de IRM a Defender
   - c) Security Administrator más IRM Approvers, que aprueba el uso compartido
   - d) Security Operator o Security Reader, más pertenecer a IRM, IRM Analysts o IRM Investigators

9. ¿Qué ocurre con la seudonimización al exportar alertas por la Office 365 Management Activity API?
   - a) Se conserva siempre
   - b) No se conserva; la exportación a CSV sí la conserva
   - c) Se conserva solo en alertas de severidad alta
   - d) La API no exporta alertas de IRM

10. ¿Qué ocurre con el Triage Agent 90 días después de la última vez que se guardó su configuración?
   - a) Se elimina y hay que desplegar una nueva instancia del agente
   - b) Pasa a modo manual y solo clasifica alertas a pedido del analista
   - c) Deja de ejecutarse hasta que alguien vuelva a guardar su configuración
   - d) Reinicia la ventana de alertas y vuelve a clasificar todo el historial

11. Según Learn, ¿qué necesita el Triage Agent de IRM además de la licencia por usuario de IRM?
   - a) El modelo de pago por uso y SCU de Security Copilot aprovisionadas
   - b) Solo Microsoft 365 E7, que reemplaza la licencia de IRM
   - c) El complemento de evidencia forense con capacidad adicional
   - d) Una licencia de Microsoft 365 Copilot para cada analista

12. ¿Cuántas SCU aporta la inclusión de Security Copilot en Microsoft 365 E5 y E7?
   - a) 100 SCU fijas al mes por tenant, sin importar las licencias
   - b) 1 SCU por usuario licenciado, sin tope mensual
   - c) Ninguna: las SCU siempre se compran aparte por hora
   - d) 400 SCU al mes por cada 1.000 licencias pagas, hasta 10.000

13. ¿Qué pasa con las plantillas de Power Automate para IRM si la seudonimización está activa?
   - a) Funcionan igual
   - b) No funcionan como se espera
   - c) La seudonimización se desactiva automáticamente
   - d) Exigen una licencia premium

14. ¿Dónde se pueden usar los indicadores personalizados del conector Insider Risk Indicators?
   - a) En todas las plantillas, incluidas las de agentes
   - b) Solo en Risky AI usage y Risky browser usage
   - c) Solo en las plantillas Data theft y Data leaks
   - d) Solo en las variantes de Security policy violations

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. No constituye asesoría legal ni laboral: usar Insider Risk Management sobre personas reales exige la evaluación previa de tus áreas de Legal, RR. HH. y privacidad y, cuando corresponda, de la representación de los trabajadores. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

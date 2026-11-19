# Nivel 2 · Intermedio · Plantillas propias, multinube, IA y dirección

*Microsoft Purview Compliance Manager Ninja Training · Edición 2026*

[← Nivel 1 · Inicial](01_Nivel_1_Inicial.md) · [Índice del programa](README.md) · [Nivel 3 · Avanzado →](03_Nivel_3_Avanzado.md)

<a id="intermedio"></a>

Evaluaciones y plantillas personalizadas, incluidas las generadas desde el PDF de una norma, la integración con Defender for Cloud para Azure, AWS y GCP, las plantillas y evaluaciones de IA y el reporte a la dirección. Terminas con una plantilla propia para una norma local sin plantilla y un informe ejecutivo de una página.

*L300 · 4 módulos · ~17 horas · 26 recursos*

**Módulos de este nivel:** [M1 Evaluaciones personalizadas](#m1) · [M2 Multinube y Defender for Cloud](#m2) · [M3 Cumplimiento para IA](#m3) · [M4 Reportes para la dirección](#m4)

<a id="m1"></a>

## M1 · Evaluaciones y plantillas personalizadas: copia, en blanco o desde el PDF de la norma

*L300 · ~5 h · Origen: Ninja oficial de 2023, nivel Intermediate (extender, modificar y crear plantillas), ampliado con las plantillas generadas con IA*

Cuando Microsoft no tiene la plantilla que necesitas —el caso más común en MCSA— hay tres caminos. El primero es **personalizar una regulación existente**: la copias, agregas controles, acciones y servicios y la publicas (función documentada como vista previa; copiar una plantilla premium consume su licencia). El segundo es **crear una plantilla en blanco** con tus controles y acciones. El tercero es **subir el PDF oficial de la norma**: el sistema lo analiza en busca de malware, extrae los controles y los mapea a acciones de mejora existentes, y tú revisas el borrador antes de publicarlo.

Las **plantillas regulatorias con IA** que hacen posible el tercer camino estuvieron en vista previa desde mediados de noviembre de 2025 y llegaron a disponibilidad general, con despliegue mundial, entre inicios y mediados de octubre de 2026, después de dos reprogramaciones. Son la vía natural para normas sin plantilla, como la Ley 21.719 o el Decreto 295 de Chile y la Comunicación «A» 8280 del BCRA. Pero el mapeo automático no es una interpretación legal: cada control extraído debe revisarlo Legal y validarlo auditoría interna antes de que la evaluación cuente.

**Por qué importa**

En MCSA la mayoría de las normas no tiene plantilla. Sin plantillas propias, los equipos mantienen planillas paralelas y pierden la reutilización de acciones de mejora entre regulaciones. La generación desde PDF recorta semanas de mapeo inicial, siempre que la revisión esté gobernada y documentada.

**Qué vas a lograr**

- Copiar y extender una plantilla para cubrir requisitos locales o internos.
- Crear una plantilla en blanco con controles y acciones propias.
- Generar una plantilla desde el PDF oficial de una norma y revisar el borrador con Legal.
- Gobernar nombres, versiones y publicación de las plantillas propias.

> **Novedad.** Las plantillas regulatorias con IA convierten el PDF de una norma en controles accionables: vista previa desde mediados de noviembre de 2025 y disponibilidad general con despliegue mundial entre inicios y mediados de octubre de 2026; la fecha prevista se movió de mediados de enero a agosto y luego a octubre de 2026 ([MC1192260, actualizado el 26 de agosto de 2026](https://mc.merill.net/message/MC1192260)). Verifica que la función llegó a tu inquilino antes de planificar.

> **Atención.** La creación desde PDF exige un documento publicado por un regulador u organismo de normas, solo en formato PDF, y el rol Compliance Manager Administration o Assessor. El sistema analiza malware, extrae los controles y los mapea a acciones existentes; tú corriges errores, agregas controles y asignas acciones antes de publicar ([crear plantillas, actualizada el 3 de diciembre de 2025](https://learn.microsoft.com/en-us/purview/compliance-manager-create-template)).

> **Atención.** Copiar una plantilla premium para personalizarla activa la regulación y consume su licencia. La copia hereda las actualizaciones de Microsoft salvo en las acciones que modifiques, una regulación copiada no se puede eliminar y Learn recomienda no editar copias ya publicadas porque el historial de versiones aún no refleja esos cambios ([evaluaciones personalizadas, vista previa](https://learn.microsoft.com/en-us/purview/compliance-manager-assessments-custom)). La página de evaluaciones, en cambio, indica que las evaluaciones personalizadas no reciben actualizaciones de plantilla: ver [puntos a confirmar](08_Cierre_glosario_y_fuentes.md#metodologia).

> **Consejo Ninja.** El mapeo automático no es interpretación legal. Archiva junto a cada plantilla publicada el PDF fuente, la fecha de publicación de la norma, el nombre de regulación general que agrupa sus versiones y el acta de revisión de Legal; si la norma cambia, publica una plantilla nueva en lugar de editar la anterior.

**¿Tienes poco tiempo?**

- [Creating regulation templates in Compliance Manager](https://learn.microsoft.com/en-us/purview/compliance-manager-create-template) · Documentación
- [MC1192260 - Microsoft Purview | Compliance Manager - AI Powered Regulatory Templates](https://mc.merill.net/message/MC1192260) · Documentación
- [Compilación de evaluaciones personalizadas (versión preliminar) en Microsoft Purview Compliance Manager](https://learn.microsoft.com/es-es/purview/compliance-manager-assessments-custom) · Documentación

### Documentación, cursos y credenciales

- [MC1192260 - Microsoft Purview | Compliance Manager - AI Powered Regulatory Templates](https://mc.merill.net/message/MC1192260) · Documentación · Comunidad · Nuevo · Microsoft (archivo de Merill Fernando) · Microsoft 365 Message Center Archive (merill.net) · 26 ago 2026. Aviso del Message Center sobre plantillas regulatorias generadas con IA a partir de PDF: vista previa desde mediados de noviembre de 2025 y disponibilidad general reprogramada para octubre de 2026.
- [Build and manage assessments in Microsoft Purview Compliance Manager](https://learn.microsoft.com/en-us/purview/compliance-manager-assessments) · Documentación · Oficial · Nuevo · Microsoft Learn · 1 jul 2026. Cómo crear y gestionar evaluaciones: grupos, conectores, estados, exportación de informes, evaluaciones de IA, evaluaciones automáticas de apps/agentes con AI Foundry y línea base para Microsoft 365 Copilot.
- [Creating regulation templates in Compliance Manager](https://learn.microsoft.com/en-us/purview/compliance-manager-create-template) · Documentación · Oficial · Microsoft Learn · 3 dic 2025. Crear plantillas regulatorias personalizadas subiendo el PDF oficial de la norma (extracción y mapeo automático de controles) o desde una plantilla en blanco.
- [Compilación de evaluaciones personalizadas (versión preliminar) en Microsoft Purview Compliance Manager](https://learn.microsoft.com/es-es/purview/compliance-manager-assessments-custom) · Documentación · Oficial · Vista previa · ES · Microsoft Learn. Cómo copiar una regulación existente, agregar controles, acciones y servicios propios y publicarla para crear evaluaciones personalizadas. *Nota:* Copiar una regulación premium consume una licencia; se recomienda no editar copias publicadas porque el control de versiones aún no refleja esos cambios

**Manos a la obra**

1. `Laboratorio parcial` Crea la plantilla en blanco `PRUEBA-CM-Chile-21719-v1` con al menos ocho controles (bases de licitud, derechos de los titulares, deber de seguridad, reporte de vulneraciones, modelo de prevención de infracciones, entre otros), importa acciones existentes y crea dos propias; publícala y construye una evaluación ([crear plantillas](https://learn.microsoft.com/en-us/purview/compliance-manager-create-template), [Ley 21.719](https://www.bcn.cl/leychile/navegar?i=1209272&f=2026-12-01)). Limitación: requiere el rol Administration o Assessor y el mapeo es manual.
2. `Laboratorio parcial` Genera una plantilla desde el PDF oficial del Decreto 295 de Chile, descargado desde [LeyChile](https://www.leychile.cl/leychile/Navegar/imprimir?idNorma=1211466), y compara los controles extraídos con el texto: cuántos son correctos, cuántos faltan y cuántos sobran. Limitación: confirma que la disponibilidad general de octubre de 2026 llegó a tu inquilino de prueba ([MC1192260](https://mc.merill.net/message/MC1192260)).
3. `Laboratorio parcial` Repite la extracción con el PDF de la [Comunicación «A» 8280 del BCRA](https://www.bcra.gob.ar/archivos/Pdfs/comytexord/A8280.pdf) y verifica que la notificación inicial en la primera hora y el reporte de cierre en cinco días corridos quedaron como controles con una acción asignada. Limitación: la misma de la práctica anterior.
4. `Laboratorio parcial` Personaliza la plantilla de la Ley 25.326 de Argentina (activada en la prueba o en un cupo): agrégale tres controles de la [Resolución AAIP 47/2018](https://www.argentina.gob.ar/normativa/nacional/norma-312662/texto) con sus acciones, publícala y verifica en Regulations que aparece con contenido personalizado. Limitación: copiar una plantilla premium consume su licencia y la copia no se puede eliminar ([evaluaciones personalizadas](https://learn.microsoft.com/en-us/purview/compliance-manager-assessments-custom)).
5. `Laboratorio` Define la gobernanza de plantillas propias: convención de nombres, nombre de regulación general para agrupar versiones, responsable de publicación, revisión de Legal, criterio de versión nueva frente a edición y archivo del PDF fuente. Evidencia: procedimiento de una página aprobado por el gestor de GRC.
6. `Solo producción` Publica en producción la plantilla de una norma local sin plantilla y construye la evaluación oficial. Motivo: la plantilla pasa a ser evidencia ante auditores y supervisores. Cómo hacerlo seguro: borrador revisado y firmado por Legal y auditoría interna, publicación en un grupo nuevo, sin editar la copia publicada y con el PDF fuente archivado como evidencia.

<a id="m2"></a>

## M2 · Multinube: Azure, AWS y GCP con Defender for Cloud, y conectores para SaaS

*L300 · ~5 h · Origen: Nuevo en esta edición (el Ninja de 2023 no cubre la integración multinube actual)*

Una misma evaluación de Compliance Manager puede cubrir Microsoft 365, Azure, AWS y Google Cloud. La pieza que lo hace posible es **Microsoft Defender for Cloud**: cuando asignas un estándar en su panel de cumplimiento normativo, los resultados a nivel de recurso aparecen en Compliance Manager para el mismo estándar, con progreso por servicio y por suscripción. La configuración pide una suscripción de Azure, Defender for Cloud con Foundational CSPM o Defender CSPM, los estándares asignados y los conectores de AWS o GCP; la mayoría de los pasos requiere el rol Owner en Azure.

Hay matices de costo y alcance. Los estándares no predeterminados requieren al menos un plan pago de Defender for Cloud (distinto de Servers P1 o API P1) y las evaluaciones corren aproximadamente cada 12 horas. Entre los estándares soportados a la vez por ambas soluciones están CIS, ISO 27001, NIST 800-53 r5, PCI DSS, SOC 2 y SWIFT CSP-CDCF. Para SaaS, Compliance Manager tiene conectores propios (Corporate Sustainability, Salesforce y Zoom), distintos de los conectores de datos de Purview; cualquier otro servicio se agrega como «nuevo servicio» con la versión universal de la plantilla.

**Por qué importa**

Los supervisores de la región revisan la externalización a la nube: el Capítulo 20-7 de la CMF en Chile, la Circular Externa 005 de 2019 de la SFC en Colombia o el régimen de tercerización del BCU en Uruguay. Evidenciar en una sola evaluación los controles de Microsoft 365 y de cada nube evita auditorías paralelas y deja claro qué controles son del equipo de nube y cuáles del de colaboración.

**Qué vas a lograr**

- Configurar los prerrequisitos de nube con permisos mínimos y costos controlados.
- Crear una evaluación con Microsoft 365 y una suscripción de Azure y leer el progreso por servicio.
- Decidir entre conectores de Compliance Manager y la versión universal de la plantilla.
- Estimar el costo de Defender for Cloud que implica cada estándar.

> **Atención.** Al agregar un estándar al panel de cumplimiento normativo de Defender for Cloud, los datos a nivel de recurso aparecen automáticamente en Compliance Manager para ese estándar. Los estándares no predeterminados requieren al menos un plan pago de Defender for Cloud y las evaluaciones corren aproximadamente cada 12 horas ([panel de cumplimiento](https://learn.microsoft.com/en-us/azure/defender-for-cloud/regulatory-compliance-dashboard)); asignarlos pide un plan distinto de Servers P1 o API P1 y el rol Owner o Policy Contributor ([asignar estándares, actualizada el 8 de agosto de 2026](https://learn.microsoft.com/en-us/azure/defender-for-cloud/assign-regulatory-compliance-standards)).

> **Consejo Ninja.** Las acciones probadas por Defender for Cloud no pasan a prueba manual: si un resultado no te convence, corrige la configuración o la evaluación en Defender for Cloud, no en Compliance Manager ([acciones de mejora](https://learn.microsoft.com/en-us/purview/compliance-manager-improvement-actions)). Los errores de acceso a suscripciones también se corrigen allí ([evaluaciones](https://learn.microsoft.com/en-us/purview/compliance-manager-assessments)).

> **Consejo Ninja.** Los conectores de Compliance Manager (Corporate Sustainability, Salesforce y Zoom) no son los conectores de datos del menú de Purview: requieren el rol Data Connector Admin o Global Admin y un conector por instancia o cuenta ([conectores](https://learn.microsoft.com/en-us/purview/compliance-manager-connectors)). Los servicios sin conector se agregan como nuevo servicio con la versión universal de la plantilla ([multinube, actualizada el 26 de septiembre de 2025](https://learn.microsoft.com/en-us/purview/compliance-manager-multicloud)).

> **Qué cambió.** La integración con Defender for Cloud para las nubes de gobierno de EE. UU. (GCC, GCC High y DoD) tenía disponibilidad general prevista para diciembre de 2025 ([RM167331](https://mc.merill.net/message/RM167331)); para clientes comerciales de MCSA ya está documentada como disponible. El video de Microsoft Mechanics sobre multinube (aproximadamente de 2023) sigue sirviendo para ver el flujo completo ([video](https://www.youtube.com/watch?v=WvxkL8AwlVg)).

**¿Tienes poco tiempo?**

- [Multicloud support in Microsoft Purview Compliance Manager](https://learn.microsoft.com/en-us/purview/compliance-manager-multicloud) · Documentación
- [Configure cloud settings for use with Microsoft Purview Compliance Manager](https://learn.microsoft.com/en-us/purview/compliance-manager-cloud-settings) · Documentación
- [Improve regulatory compliance in Microsoft Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/regulatory-compliance-dashboard) · Documentación
- [Multicloud Vulnerability Detection and Mitigation with Microsoft Purview (Microsoft Mechanics)](https://www.youtube.com/watch?v=WvxkL8AwlVg) · Video

### Documentación, cursos y credenciales

- [Configure cloud settings for use with Microsoft Purview Compliance Manager](https://learn.microsoft.com/en-us/purview/compliance-manager-cloud-settings) · Documentación · Oficial · Microsoft Learn. Pasos para habilitar la multinube: suscripción de Azure, Defender for Cloud con Foundational CSPM o Defender CSPM, asignación de estándares y conectores de AWS/GCP.
- [Improve regulatory compliance in Microsoft Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/regulatory-compliance-dashboard) · Documentación · Oficial · Microsoft Learn. Panel de cumplimiento normativo de Defender for Cloud, su integración con Compliance Manager, remediación, informes, exportación continua y flujos de trabajo ante cambios.
- [Multicloud support in Microsoft Purview Compliance Manager](https://learn.microsoft.com/en-us/purview/compliance-manager-multicloud) · Documentación · Oficial · Microsoft Learn · 26 sep 2025. Describe cómo la integración con Microsoft Defender for Cloud permite evaluar Microsoft 365, Azure, AWS y GCP con pruebas a nivel de recurso dentro de una misma evaluación.
- [Assign regulatory compliance standards in Microsoft Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/assign-regulatory-compliance-standards) · Documentación · Oficial · Nuevo · Microsoft Learn · 8 ago 2026. Cómo asignar estándares regulatorios a suscripciones de Azure, cuentas de AWS y proyectos de GCP para que se evalúen y fluyan a Compliance Manager.
- [Working with connectors in Compliance Manager](https://learn.microsoft.com/en-us/purview/compliance-manager-connectors) · Documentación · Oficial · Microsoft Learn. Conectores propios de Compliance Manager (Corporate Sustainability, Salesforce y Zoom) para incluir servicios no Microsoft en evaluaciones con monitoreo automático.
- [RM167331 - Compliance Manager: Microsoft Defender for Cloud (MDC) integration (GCC, GCC High, DoD)](https://mc.merill.net/message/RM167331) · Documentación · Comunidad · Microsoft (archivo de Merill Fernando) · Microsoft 365 Message Center Archive (merill.net) · 30 jul 2025. Elemento de roadmap de la integración de Compliance Manager con Defender for Cloud para nubes de gobierno de EE. UU., con GA prevista para diciembre de 2025.

### Webinars, videos y podcasts

- [Multicloud Vulnerability Detection and Mitigation with Microsoft Purview (Microsoft Mechanics)](https://www.youtube.com/watch?v=WvxkL8AwlVg) · Video · Empleado de Microsoft · Legado aún útil · Daniel Hidalgo · Microsoft Mechanics. Demostración de evaluaciones multinube (PCI DSS) con Defender for Cloud, conector de Salesforce y enlaces directos a la configuración que hay que corregir. *Nota:* Publicado hace ~3 años (aprox. 2023); la integración sigue vigente según Learn (actualizado sep-2025)

**Manos a la obra**

1. `Laboratorio` Sigue [configurar los ajustes de nube](https://learn.microsoft.com/en-us/purview/compliance-manager-cloud-settings) en tu suscripción con créditos de Visual Studio Enterprise: habilita Defender for Cloud con Foundational CSPM y documenta qué roles de Azure usaste, idealmente Owner temporal con [PIM](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-configure). Evidencia: captura de la configuración y lista de roles.
2. `Laboratorio parcial` Asigna ISO 27001 en el panel de cumplimiento normativo de Defender for Cloud y, tras unas 12 horas, crea en Compliance Manager una evaluación ISO 27001 que incluya Microsoft 365 y esa suscripción; compara el progreso por servicio ([asignar estándares](https://learn.microsoft.com/en-us/azure/defender-for-cloud/assign-regulatory-compliance-standards)). Limitación: los estándares no predeterminados requieren un plan pago de Defender for Cloud, con costo sobre el crédito.
3. `Laboratorio parcial` Conecta a Defender for Cloud una cuenta de AWS o un proyecto de GCP propios y agrégalos a la evaluación como servicios ([ajustes de nube](https://learn.microsoft.com/en-us/purview/compliance-manager-cloud-settings)). Limitación: requiere cuentas propias en esas nubes y puede generar costos.
4. `Laboratorio` Agrega a una evaluación un servicio no listado como «nuevo servicio» y documenta las acciones que pasan a implementación y prueba manuales ([multinube](https://learn.microsoft.com/en-us/purview/compliance-manager-multicloud)).
5. `Laboratorio` Estima con la [página de precios de Defender for Cloud](https://azure.microsoft.com/en-us/pricing/details/defender-for-cloud/) el costo mensual de los planes que exigen tus estándares, con los supuestos de recursos; compáralo con el costo de una auditoría paralela por nube.
6. `Solo producción` Conecta Salesforce o Zoom con un conector de Compliance Manager. Motivo: requiere cuentas reales de esos servicios. Cómo hacerlo seguro: instancia de prueba o sandbox del SaaS, cuenta de servicio de mínimo privilegio, rol Data Connector Admin temporal y revisión de permisos al terminar ([conectores](https://learn.microsoft.com/en-us/purview/compliance-manager-connectors)).
7. `Solo producción` Lleva la evaluación multinube a las suscripciones productivas. Motivo: los recursos y sus configuraciones reales solo existen allí. Cómo hacerlo seguro: permisos de lectura donde alcance, Owner temporal con PIM solo para la configuración, estándares asignados primero a una suscripción piloto y presupuesto con alertas.

<a id="m3"></a>

## M3 · Cumplimiento para IA: plantillas, evaluaciones de agentes y regulación

*L300 · ~4 h · Origen: Nuevo en esta edición*

Compliance Manager ofrece cuatro **plantillas premium de IA** —EU AI Act, ISO/IEC 23894:2023, ISO/IEC 42001:2023 y NIST AI RMF 1.0— aplicables a las apps de IA generativa que Purview soporta, como Microsoft 365 Copilot, Security Copilot, ChatGPT Enterprise, Microsoft Foundry, Gemini y DeepSeek; desde agosto de 2026, el soporte para Anthropic Claude Enterprise también incluye Compliance Manager. Al comprar Microsoft 365 Copilot o Copilot Chat se aprovisiona además una evaluación base para esos servicios, visible en el centro de administración de Microsoft 365.

Para agentes construidos en **Microsoft Foundry**, la integración ofrece evaluaciones automáticas: 75 acciones, 15 de ellas con evaluaciones sincronizadas desde Foundry (fiabilidad, BLEU, coherencia y fluidez), y evaluaciones integradas para EU AI Act, NIST AI RMF e ISO gratuitas durante seis meses con licencias de Copilot o de agentes; requiere el rol Azure AI Project Manager o Azure AI User. La regulación local avanza: Perú publicó en septiembre de 2025 el reglamento de su ley de IA, sin plantilla en Compliance Manager. Los controles de datos para agentes y los marcos de gobierno de IA se profundizan en el programa de DSPM y seguridad de datos para IA (módulos M2 y A3).

**Por qué importa**

La regulación de IA ya alcanza a la región y los clientes globales piden evidencia de EU AI Act o ISO/IEC 42001. Documentar los controles de IA en la misma herramienta que el resto de las normas permite reutilizar acciones —DLP, etiquetas, auditoría— y le da al comité una vista única del riesgo de IA, en lugar de un anexo aislado.

**Qué vas a lograr**

- Elegir la plantilla de IA adecuada según obligación, clientes y madurez.
- Crear una evaluación de IA y vincularle evidencias de DSPM, DLP y auditoría.
- Explicar las evaluaciones automáticas de agentes de Microsoft Foundry y sus requisitos.
- Mapear una norma local de IA contra EU AI Act, ISO/IEC 42001 y NIST AI RMF.

> **Novedad.** Hay cuatro plantillas premium de IA —EU AI Act, ISO/IEC 23894:2023, ISO/IEC 42001:2023 y NIST AI RMF 1.0— aplicables a apps de IA generativa compatibles con Purview (Microsoft 365 Copilot, Security Copilot, ChatGPT Enterprise, Microsoft Foundry, Gemini y DeepSeek), y consumen licencias premium ([evaluaciones, actualizada el 1 de julio de 2026](https://learn.microsoft.com/en-us/purview/compliance-manager-assessments)). En agosto de 2026, el soporte de Purview para Anthropic Claude Enterprise pasó a incluir Compliance Manager ([novedades de Purview](https://learn.microsoft.com/en-us/purview/whats-new)).

> **Atención.** Licencias de IA con señales cruzadas: Learn dice que las plantillas de IA consumen licencias premium, pero también que las evaluaciones integradas para EU AI Act, NIST AI RMF e ISO son gratuitas durante seis meses con licencias de Copilot o de agentes ([evaluaciones](https://learn.microsoft.com/en-us/purview/compliance-manager-assessments)); además, un análisis comunitario describe una regulación «AI Baseline» que aparece al activar licencias de Copilot, con 179 acciones (80 tuyas y 99 de Microsoft) ([AI Baseline](https://informasjonsbeskyttelse.no/en/ai-baseline-in-microsoft-purview)). Confirma en tu inquilino qué se consume y desde cuándo.

> **Novedad.** La integración con Microsoft Foundry para mapear agentes a regulaciones de IA y evaluar controles de forma automática tuvo vista previa en diciembre de 2025 y GA prevista para octubre de 2026, en estado «In development» al 26 de agosto de 2026 ([RM536576](https://mc.merill.net/message/RM536576)); Learn todavía la presenta con el nombre anterior, Azure AI Foundry (hoy Microsoft Foundry). Las capacidades de Purview para agentes de Foundry y apps de IA conectadas a Entra se soportarán con Microsoft 365 E7 y las SKU de Agent 365 ([descripción del servicio](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)).

> **Consejo Ninja.** DSPM para IA detecta y Compliance Manager documenta: la recomendación de asistencia guiada para regulaciones de IA, basada en NIST AI RMF, enlaza ambos mundos ([DSPM para IA](https://techcommunity.microsoft.com/blog/microsoft-purview-blog/microsoft-purview-%E2%80%93-data-security-posture-management-dspm-for-ai/4394685)). Usa como evidencia los informes de DSPM y los reportes operativos de Foundry, como propone el Zero Trust Workshop ([AI_107](https://microsoft.github.io/zerotrustassessment/docs/workshop-guidance/AI/AI_107)). Los controles de datos para agentes se profundizan en el programa de DSPM y seguridad de datos para IA.

**¿Tienes poco tiempo?**

- [Build and manage assessments in Microsoft Purview Compliance Manager](https://learn.microsoft.com/en-us/purview/compliance-manager-assessments) · Documentación
- [RM536576 - Compliance Manager integration with Microsoft Foundry for automated mapping of AI regulations and evaluation of compliance controls for Foundry Agents](https://mc.merill.net/message/RM536576) · Documentación
- [Managing and monitoring your EU AI Act compliance with Compliance Manager](https://rencore.com/en/blog/managing-monitoring-eu-ai-act-compliance-manager/) · Blog
- [Leading with Trust: Building & Deploying Agents in a Regulated World (Ignite 2025 BRK1733)](https://tech.hub.ms/ai/videos/leading-with-trust-building-and-deploying-agents-in-a-regulated-world) · Video

**Plantillas y evaluaciones de IA en Compliance Manager**

| Plantilla o evaluación | Para qué sirve | Licencia | Estado y notas |
|---|---|---|---|
| EU AI Act | Obligaciones del reglamento europeo de IA según el nivel de riesgo del sistema | Premium de IA: consume una licencia o uno de los tres cupos de E5 | Útil para operaciones con alcance europeo y como referencia para normas locales basadas en riesgo |
| ISO/IEC 42001:2023 | Sistema de gestión de la IA: políticas, roles, ciclo de vida y mejora continua | Premium de IA | Norma certificable; combínala con ISO/IEC 27001 si ya tienes un SGSI |
| ISO/IEC 23894:2023 | Gestión de riesgos de la IA | Premium de IA | Complementa a ISO/IEC 42001 en la evaluación de riesgos |
| NIST AI RMF 1.0 | Marco voluntario de gestión de riesgos de la IA | Premium de IA | Base de la recomendación de asistencia guiada para regulaciones de IA de DSPM para IA |
| Evaluación base de Microsoft 365 Copilot y Copilot Chat | Controles base para Copilot y Copilot Chat | Se aprovisiona sola al comprar Microsoft 365 Copilot o Copilot Chat | Visible en el centro de administración de Microsoft 365 |
| AI Baseline (según un análisis comunitario) | Regulación que aparece al activar licencias de Copilot: 179 acciones, 80 tuyas y 99 de Microsoft | Sin licencia premium según la comunidad; confírmalo en tu inquilino | Puede subir la puntuación sin trabajo propio: reporta tus puntos por separado |
| Evaluaciones automáticas de agentes de Microsoft Foundry | 75 acciones, 15 de ellas con evaluaciones sincronizadas desde Foundry | Evaluaciones integradas gratis por seis meses con licencias de Copilot o de agentes; Purview para agentes de Foundry se soportará con E7 y Agent 365 | GA prevista para octubre de 2026 (RM536576); requiere el rol Azure AI User o Azure AI Project Manager |

Fuentes: [Learn · evaluaciones](https://learn.microsoft.com/en-us/purview/compliance-manager-assessments), [análisis de AI Baseline](https://informasjonsbeskyttelse.no/en/ai-baseline-in-microsoft-purview), [RM536576](https://mc.merill.net/message/RM536576), [DSPM para IA](https://techcommunity.microsoft.com/blog/microsoft-purview-blog/microsoft-purview-%E2%80%93-data-security-posture-management-dspm-for-ai/4394685) y [descripción del servicio de Purview](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description).

### Documentación, cursos y credenciales

- [RM536576 - Compliance Manager integration with Microsoft Foundry for automated mapping of AI regulations and evaluation of compliance controls for Foundry Agents](https://mc.merill.net/message/RM536576) · Documentación · Comunidad · Nuevo · Microsoft (archivo de Merill Fernando) · Microsoft 365 Message Center Archive (merill.net) · 26 ago 2026. Elemento de roadmap que integra Compliance Manager con Microsoft Foundry para mapear agentes a regulaciones de IA y evaluar controles automáticamente, con vista previa en diciembre de 2025 y GA en octubre de 2026.
- [Use Microsoft Purview to manage data security & compliance for Microsoft 365 Copilot & Microsoft 365 Copilot Chat](https://learn.microsoft.com/en-us/purview/ai-m365-copilot) · Documentación · Oficial · Microsoft Learn. Matriz de capacidades de Purview soportadas para Microsoft 365 Copilot, incluida Compliance Manager, y la recomendación de DSPM para IA que guía el uso de plantillas regulatorias de IA.
- [Decreto Supremo 115-2025-PCM – Reglamento de la Ley 31814 que promueve el uso de la inteligencia artificial (Perú)](https://busquedas.elperuano.pe/dispositivo/NL/2436426-1) · Documentación · Comunidad · ES · Diario Oficial El Peruano · 9 sep 2025. Primer reglamento de IA vigente en la región, con enfoque basado en riesgos; sirve para practicar el mapeo de una norma local de IA contra las plantillas EU AI Act, ISO/IEC 42001 y NIST AI RMF de Compliance Manager.

### Anuncios y blogs oficiales

- [Microsoft Ignite: Ambient and autonomous security for the agentic era](https://www.microsoft.com/en-us/security/blog/2025/11/18/ambient-and-autonomous-security-for-the-agentic-era/) · Blog oficial · Empleado de Microsoft · Vasu Jakkal · Microsoft Security Blog · 18 nov 2025. Anuncios de Ignite 2025 (Agent 365, Purview, Defender, Entra) donde la seguridad de agentes incluye evaluar la preparación de cumplimiento y recomendar controles para nuevas regulaciones.
- [Microsoft Purview – Data Security Posture Management (DSPM) for AI](https://techcommunity.microsoft.com/blog/microsoft-purview-blog/microsoft-purview-%E2%80%93-data-security-posture-management-dspm-for-ai/4394685) · Blog oficial · Empleado de Microsoft · kunal_parmar · Microsoft Purview Blog (Tech Community) · 21 mar 2025. Explica las recomendaciones de DSPM para IA, incluida la de 'asistencia guiada para regulaciones de IA' basada en NIST AI RMF que conecta con Compliance Manager.
- [How Azure AI Foundry and Partners Simplify Governance Without Slowing Developers Down](https://devblogs.microsoft.com/foundry/how-azure-ai-foundry-and-partners-simplify-governance-without-slowing-developers-down/) · Blog oficial · Empleado de Microsoft · Legado aún útil · Mehrnoosh Sameki · Microsoft Foundry Blog · 19 may 2025. Anuncio de integraciones de evaluación de Azure AI Foundry con plataformas de gobierno de IA, entre ellas Purview Compliance Manager, Credo AI y Saidot. *Nota:* Azure AI Foundry hoy se llama Microsoft Foundry

### Webinars, videos y podcasts

- [Leading with Trust: Building & Deploying Agents in a Regulated World (Ignite 2025 BRK1733)](https://tech.hub.ms/ai/videos/leading-with-trust-building-and-deploying-agents-in-a-regulated-world) · Video · Empleado de Microsoft · Sourabh Pandey, Manny Sahota, Tony Thampan · Tech Hub (resumen de sesión de Microsoft Ignite) · 24 nov 2025. Sesión de Ignite 2025 que demuestra evaluaciones automáticas de cumplimiento para agentes de Foundry, plantillas regulatorias con IA y 'Regulatory Navigator' (EU AI Act, NIS2, DORA, DPDP).
- [Data security and governance in the age of AI with Microsoft Purview (Ignite 2025 BRK251)](https://tech.hub.ms/ai/videos/comprehensive-data-security-and-governance-in-ai-workloads-with-microsoft-purview) · Video · Empleado de Microsoft · Rohan Kumar, Rudra Mitra, Nick O'Keefe · Tech Hub (resumen de sesión de Microsoft Ignite) · 20 nov 2025. Sesión principal de Purview en Ignite 2025 que presenta Compliance Manager para evaluar aplicaciones de IA frente a requisitos regulatorios y la integración con Foundry.

### Laboratorios, GitHub y herramientas

- [Establish AI Compliance Documentation (Zero Trust Workshop)](https://microsoft.github.io/zerotrustassessment/docs/workshop-guidance/AI/AI_107) · GitHub · Oficial · Microsoft (Zero Trust Assessment / Workshop). Guía del Zero Trust Workshop para crear evaluaciones de IA en Compliance Manager y complementarlas con reportes operativos de Foundry como evidencia.

### Comunidad: blogs, libros, newsletters y eventos

- [AI Baseline regulatory template](https://informasjonsbeskyttelse.no/en/ai-baseline-in-microsoft-purview) · Blog · Comunidad · Nuevo · Roy Allan Hansen · informasjonsbeskyttelse.no · 22 oct 2026. Análisis de la regulación 'AI Baseline' que aparece al activar licencias de Copilot: 179 acciones (80 del cliente y 99 de Microsoft), origen en cuatro marcos de IA y por qué la puntuación puede subir sin trabajo real.
- [Managing and monitoring your EU AI Act compliance with Compliance Manager](https://rencore.com/en/blog/managing-monitoring-eu-ai-act-compliance-manager/) · Blog · Comunidad · Nuevo · Jasper Oosterveld · Rencore · 24 ago 2026. Recorrido práctico para montar una evaluación de EU AI Act en Compliance Manager, con grupos, roles, licencias y limitaciones.

**Manos a la obra**

1. `Laboratorio parcial` Crea una evaluación EU AI Act o ISO/IEC 42001 para Microsoft 365 Copilot en el grupo `PRUEBA-CM-IA` y asigna cinco acciones a dueños de prueba ([evaluaciones](https://learn.microsoft.com/en-us/purview/compliance-manager-assessments)). Limitación: consume un cupo premium o parte de la prueba de 90 días.
2. `Laboratorio parcial` Crea una evaluación EU AI Act para un agente de Microsoft Foundry y observa las acciones con evaluación automática (fiabilidad, BLEU, coherencia y fluidez). Limitación: requiere un proyecto de Foundry (créditos de Azure), el rol Azure AI User o Azure AI Project Manager y, para la oferta gratuita, licencias de Copilot o de agentes.
3. `Laboratorio parcial` Sigue la guía del Zero Trust Workshop para documentar el cumplimiento de IA ([AI_107](https://microsoft.github.io/zerotrustassessment/docs/workshop-guidance/AI/AI_107)) y adjunta como evidencia un informe de DSPM para IA de tu laboratorio, sin prompts reales. Limitación: sin licencias de Copilot, DSPM para IA mostrará poca actividad.
4. `Laboratorio` Construye una matriz de la Ley 31814 de Perú y su reglamento ([DS 115-2025-PCM](https://busquedas.elperuano.pe/dispositivo/NL/2436426-1)) frente a EU AI Act, ISO/IEC 42001 y NIST AI RMF por tema (enfoque de riesgo, transparencia, supervisión humana, gestión de datos) y marca las brechas que irían a una plantilla propia.
5. `Laboratorio parcial` Si tu laboratorio tiene licencias de Microsoft 365 Copilot (por ejemplo, compradas en el sandbox de desarrollador), verifica en el centro de administración de Microsoft 365 que se aprovisionó la evaluación base de Copilot y Copilot Chat y anota cuántas acciones son tuyas. Limitación: las licencias de Copilot no vienen en la prueba de E5.
6. `Solo producción` Evalúa un agente productivo contra la plantilla de IA elegida. Motivo: requiere el agente, sus datos y sus dueños reales. Cómo hacerlo seguro: agente piloto con datos de prueba, evidencias de DSPM y DLP en lugar de capturas de prompts reales, privacidad involucrada desde el inicio y sin presentar acciones en vista previa como controles operativos.

**¿Quieres profundizar?**

- [AI Baseline regulatory template](https://informasjonsbeskyttelse.no/en/ai-baseline-in-microsoft-purview) · Blog
- [Establish AI Compliance Documentation (Zero Trust Workshop)](https://microsoft.github.io/zerotrustassessment/docs/workshop-guidance/AI/AI_107) · GitHub

<a id="m4"></a>

## M4 · Reportes para la dirección y el comité de riesgos

*L300 · ~3 h · Origen: Ninja oficial de 2023, nivel Advanced (reportes)*

Compliance Manager produce dos insumos para reportar. El **informe de evaluación** se exporta a Excel como una instantánea fechada con los controles de Microsoft y los tuyos, su estado, la fecha y el resultado de las pruebas; conviene exportarlo antes de borrar una evaluación o de aceptar una actualización. Los **informes de postura de Purview** (Information Protection, DLP y personalizados), en vista previa, usan una ventana móvil de 30 días, se guardan en PDF y complementan la puntuación con datos de protección reales.

Lo difícil no es exportar, sino traducir. La dirección necesita tendencias, riesgos, dueños y decisiones, no un porcentaje aislado. Este módulo propone un reporte de una página que separa la puntuación de cumplimiento de **Microsoft Secure Score**, anota la fecha y las actualizaciones de plantillas aceptadas y no presenta funciones en vista previa como controles operativos. El reporte ejecutivo del SOC se profundiza en el programa de Defender XDR, en su track de excelencia del SOC (módulo S7).

**Por qué importa**

El comité decide presupuesto y aceptación de riesgos con lo que ve. Un reporte que mezcla puntuación, Secure Score y funciones en vista previa lleva a decisiones equivocadas o a una tranquilidad falsa; uno fechado, con evidencia y responsables, crea rendición de cuentas.

**Qué vas a lograr**

- Exportar el informe de una evaluación y conservarlo como instantánea fechada.
- Diseñar un reporte de una página con tendencia, brechas, dueños y decisiones pedidas.
- Separar puntuación de cumplimiento, Secure Score y riesgo residual.
- Usar los informes de postura de Purview como complemento, con sus límites.

> **Consejo Ninja.** El informe de evaluación es una instantánea fechada en Excel con los controles de Microsoft y los tuyos, su estado, la fecha y el resultado de las pruebas; Microsoft recomienda exportarlo antes de borrar una evaluación ([evaluaciones](https://learn.microsoft.com/en-us/purview/compliance-manager-assessments)). Archívalo con la fecha en el nombre: es tu evidencia histórica.

> **Atención.** Los informes de postura de Purview (Information Protection, DLP y personalizados) están en vista previa, usan una ventana móvil de 30 días y se guardan en PDF ([informes de postura](https://learn.microsoft.com/en-us/purview/purview-reports)). Úsalos como anexo, no como control operativo: la lectura ejecutiva de la comunidad advierte contra presentar funciones en vista previa como controles ([Purview, septiembre de 2026](https://alberthoitingh.com/2026/09/04/things-to-know-about-microsoft-purview-september-2026/)).

> **Consejo Ninja.** Secure Score y puntuación de cumplimiento responden preguntas distintas: repórtalas por separado, cada una con su audiencia ([Secure Score](https://learn.microsoft.com/en-us/defender-xdr/microsoft-secure-score), [comparación comunitaria](https://www.m365.fm/blog/bridging-the-gap-compliance-scores-vs-secure-scores/)). Para el lenguaje con el directorio, el archivo del Microsoft Security Blog sobre Compliance Manager incluye una guía para trabajar con el comité de ciberseguridad del directorio (junio de 2024) ([archivo](https://www.microsoft.com/en-us/security/blog/product/microsoft-purview-compliance-manager/)).

> **Atención.** Al aceptar una actualización de plantilla la puntuación cambia: anota la fecha de corte y las actualizaciones aceptadas cada vez que reportes el indicador ([cómo Purview apoya un SGSI](https://informasjonsbeskyttelse.no/en/how-purview-supports-an-isms)).

**¿Tienes poco tiempo?**

- [Microsoft Purview posture reports overview](https://learn.microsoft.com/en-us/purview/purview-reports) · Documentación
- [Bridging the Gap: Compliance Scores vs. Secure Scores](https://www.m365.fm/blog/bridging-the-gap-compliance-scores-vs-secure-scores/) · Blog
- [Things to Know About Microsoft Purview – September 2026](https://alberthoitingh.com/2026/09/04/things-to-know-about-microsoft-purview-september-2026/) · Blog

### Documentación, cursos y credenciales

- [Microsoft Purview posture reports overview](https://learn.microsoft.com/en-us/purview/purview-reports) · Documentación · Oficial · Vista previa · Microsoft Learn. Informes de postura de Purview (Information Protection, DLP y personalizados) pensados para responder preguntas de ejecutivos; sirven para complementar la puntuación de cumplimiento en un reporte para la dirección. *Nota:* Los informes de postura de IP, DLP y personalizados están en versión preliminar; datos en ventana móvil de 30 días y se pueden guardar en PDF

### Laboratorios, GitHub y herramientas

- [FSI Agent Governance Solutions – Compliance Dashboard Power BI Setup](https://github.com/judeper/FSI-AgentGov-Solutions/blob/main/compliance-dashboard/docs/power-bi-setup.md) · GitHub · Comunidad · judeper · GitHub. Patrón de tablero Power BI de cumplimiento (resumen ejecutivo, controles, excepciones, tendencias) sobre Dataverse que puede alimentarse con exportaciones de Compliance Manager.

### Comunidad: blogs, libros, newsletters y eventos

- [Things to Know About Microsoft Purview – September 2026](https://alberthoitingh.com/2026/09/04/things-to-know-about-microsoft-purview-september-2026/) · Blog · MVP · Nuevo · Albert Hoitingh · alberthoitingh.com · 4 sep 2026. Compendio de mayo a agosto de 2026 sobre Purview con lectura ejecutiva de impactos y advertencia de no presentar funciones en vista previa como controles operativos.
- [Bridging the Gap: Compliance Scores vs. Secure Scores](https://www.m365.fm/blog/bridging-the-gap-compliance-scores-vs-secure-scores/) · Blog · Comunidad · Nuevo · Mirko Peters · M365.FM · 12 ago 2026. Contrasta puntuación de cumplimiento y secure score (enfoque, cálculo y audiencia) y cómo presentar ambas métricas a la dirección y al SOC.

**Manos a la obra**

1. `Laboratorio` Exporta el informe de tu evaluación de práctica y verifica sus columnas (controles de Microsoft y tuyos, estado, fecha y resultado de pruebas); archívalo con la fecha en el nombre ([evaluaciones](https://learn.microsoft.com/en-us/purview/compliance-manager-assessments)).
2. `Laboratorio` Arma un tablero en Excel o Power BI con al menos dos exportaciones fechadas que muestre tendencia, acciones vencidas por dueño y, en una sección separada, Microsoft Secure Score ([Secure Score](https://learn.microsoft.com/en-us/defender-xdr/microsoft-secure-score)).
3. `Laboratorio` Redacta un informe ejecutivo de una página: tres mensajes, tres riesgos con dueño y tres decisiones pedidas, con la advertencia explícita de que la puntuación no es una certificación ([FAQ](https://learn.microsoft.com/en-us/purview/compliance-manager-faq)).
4. `Laboratorio parcial` Genera un informe de postura de Purview (DLP o Information Protection), guárdalo en PDF y úsalo como anexo ([informes de postura](https://learn.microsoft.com/en-us/purview/purview-reports)). Limitación: está en vista previa y usa 30 días de datos; en un laboratorio nuevo habrá poca actividad.
5. `Solo producción` Presenta el informe al comité de riesgos. Motivo: requiere cifras, riesgos y decisiones reales. Cómo hacerlo seguro: revisión previa del gestor de GRC y de auditoría interna, cifras con fecha de corte, sin datos personales en los anexos y con registro de las decisiones tomadas.

<a id="reto-intermedio"></a>

## Reto del nivel

**Una norma local sin plantilla, de punta a punta.** Genera desde el PDF oficial (o en blanco, si la función aún no llegó a tu inquilino) la plantilla del Decreto 295 de Chile o de la Comunicación «A» 8280 del BCRA, revisa el borrador con una lista de control y publícalo. Crea una evaluación que incluya Microsoft 365 y, si puedes, una suscripción de Azure; suma una evaluación de IA para un piloto de Copilot o de un agente, y cierra con un informe ejecutivo de una página con tres decisiones pedidas al comité.

<a id="quiz-intermedio"></a>

## Evaluación del nivel

Responde y compara con [Evaluaciones y respuestas](06_Evaluaciones_y_respuestas.md#eval-intermedio). Con 80 % o más, ¡nivel aprobado! (En la versión web puedes corregir en línea y generar tu certificado).

1. ¿Qué hacen las plantillas regulatorias con IA anunciadas en MC1192260?
   - a) Traducen la interfaz de Compliance Manager al español
   - b) Calculan las multas regulatorias aplicables
   - c) Crean políticas de DLP automáticamente
   - d) Convierten el PDF de una regulación en una plantilla con controles accionables

2. ¿Qué requisitos tiene crear una plantilla a partir de un PDF?
   - a) Un PDF publicado por un regulador u organismo de normas y el rol Compliance Manager Administration o Assessor
   - b) Cualquier documento de Word con controles numerados
   - c) Una licencia de Microsoft 365 Copilot
   - d) El rol Compliance Manager Reader y la aprobación de Microsoft

3. ¿Qué ocurre al copiar una plantilla premium para personalizarla?
   - a) Nada: las copias nunca consumen licencias
   - b) Se activa la regulación y se consume su licencia
   - c) Se convierte automáticamente en una plantilla incluida
   - d) Se elimina la plantilla original

4. ¿En qué estado están las evaluaciones personalizadas (copiar y extender una regulación) en noviembre de 2026?
   - a) En disponibilidad general desde 2022
   - b) Retiradas en 2025
   - c) Siguen documentadas como vista previa
   - d) Disponibles solo en GCC High

5. ¿De dónde obtiene Compliance Manager el progreso de las suscripciones de Azure, AWS y GCP?
   - a) De Microsoft Sentinel
   - b) De Microsoft Defender for Cloud
   - c) De Azure Monitor directamente
   - d) De conectores de Power Automate

6. Quieres evaluar ISO 27001 en Azure con resultados a nivel de recurso. ¿Qué necesitas en Defender for Cloud?
   - a) Nada: Foundational CSPM incluye todos los estándares
   - b) Solo el plan Servers P1
   - c) Una licencia premium de Compliance Manager para Azure
   - d) Asignar el estándar con al menos un plan pago distinto de Servers P1 o API P1

7. ¿Qué son los conectores de Compliance Manager?
   - a) Conectores propios para incluir servicios como Salesforce y Zoom en las evaluaciones, distintos de los conectores de datos de Purview
   - b) Los mismos conectores de datos que usa Insider Risk
   - c) Conectores de Defender for Cloud para AWS
   - d) Integraciones de Power BI para reportes

8. Necesitas evaluar un servicio no Microsoft que no tiene conector. ¿Qué haces?
   - a) No es posible evaluarlo
   - b) Lo agregas como nuevo servicio y se usa la versión universal de la plantilla, con implementación y pruebas manuales
   - c) Pides a Microsoft que cree un conector
   - d) Lo conectas a Defender for Cloud como si fuera AWS

9. ¿Cuál de estas NO es una de las cuatro plantillas premium de IA?
   - a) EU AI Act
   - b) ISO/IEC 42001:2023
   - c) NIST AI RMF 1.0
   - d) ISO/IEC 27701:2019

10. ¿Qué ocurre al comprar Microsoft 365 Copilot o Copilot Chat?
   - a) Se habilitan gratis todas las plantillas premium
   - b) Se crea una evaluación EU AI Act obligatoria
   - c) Se aprovisiona automáticamente una evaluación base para Microsoft 365 Copilot y Copilot Chat
   - d) Se desactiva la Data Protection Baseline

11. ¿Qué rol de Azure requieren las evaluaciones automáticas de agentes de Microsoft Foundry en Compliance Manager?
   - a) Azure AI Project Manager o Azure AI User
   - b) Owner de la suscripción
   - c) Security Reader de Entra ID
   - d) Policy Contributor

12. Al exportar el informe de una evaluación, ¿qué obtienes?
   - a) Un PDF firmado por Microsoft
   - b) Un enlace público para el auditor
   - c) Una instantánea en Excel con controles de Microsoft y tuyos, estado, fecha y resultado de pruebas
   - d) Un certificado ISO

13. ¿Qué características tienen los informes de postura de Purview?
   - a) Están en vista previa, usan una ventana móvil de 30 días y se guardan en PDF
   - b) Están en disponibilidad general y muestran tres años de historia
   - c) Reemplazan a la puntuación de cumplimiento
   - d) Solo están disponibles en GCC High

14. Al reportar la puntuación de cumplimiento a la dirección, ¿qué conviene anotar siempre?
   - a) El precio de cada plantilla
   - b) La fecha de corte y las actualizaciones de plantillas aceptadas
   - c) La contraseña del administrador
   - d) El Secure Score sumado a la puntuación

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. No constituye asesoría legal: la normativa citada es material de referencia y las decisiones de aplicabilidad corresponden a tus áreas de Legal, privacidad y, cuando aplique, RR. HH. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

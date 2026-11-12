# Nivel 2 · Intermedio · Proteger Copilot, agentes e IA de terceros

*Microsoft Purview DSPM y seguridad de datos para IA Ninja Training · Edición 2026*

[← Nivel 1 · Inicial](01_Nivel_1_Inicial.md) · [Índice del programa](README.md) · [Nivel 3 · Avanzado →](03_Nivel_3_Avanzado.md)

<a id="intermedio"></a>

DLP, retención, auditoría, eDiscovery, Insider Risk y Communication Compliance aplicados a Copilot; agentes de Copilot Studio, Microsoft Foundry y Agent 365; IA de terceros en navegador, endpoint y red; y remediación con SharePoint Advanced Management. Terminas con controles en simulación o auditoría para un grupo piloto y su matriz de licencias.

*L300 · 4 módulos · ~27 horas · 42 recursos*

**Módulos de este nivel:** [M1 Interacciones de Copilot](#m1) · [M2 Agentes y Agent 365](#m2) · [M3 IA de terceros](#m3) · [M4 SharePoint y sobreexposición](#m4)

<a id="m1"></a>

## M1 · Proteger las interacciones de Copilot

*L300 · ~8 h · Origen: Ruta SC-401 de IA, módulo 2, y ruta «Secure and govern Microsoft 365 Copilot interactions with Microsoft Purview» (7 módulos)*

Copilot hereda los controles de Purview. Respeta los permisos del usuario y necesita los derechos de uso VIEW y EXTRACT para leer contenido cifrado. Sus respuestas heredan la etiqueta de mayor prioridad de las fuentes, y prompts y respuestas quedan registrados para auditoría, eDiscovery y retención. Sobre esa base, la **DLP para la ubicación Microsoft Copilot** ofrece cuatro controles: bloquear prompts con tipos de información confidencial (SIT), bloquear la búsqueda web con SIT, excluir archivos y correos etiquetados, y excluir correo externo (en preview). La política predeterminada «Protect sensitive M365 Copilot interactions» arranca en modo simulación, y en una misma regla no se combinan condiciones de SIT y de etiquetas.

Otras cinco soluciones completan el cuadro. **Insider Risk Management** detecta uso riesgoso de IA con la plantilla Risky AI usage, y **Communication Compliance** analiza prompts y respuestas. **Audit** registra cada interacción con los recursos accedidos, la etiqueta, la detección de inyección indirecta (XPIADetected) y el identificador del agente. La **retención** usa ubicaciones separadas (Microsoft Copilot experiences, Enterprise AI apps y Other AI apps), y **eDiscovery** busca, retiene, exporta y elimina interacciones. Cada solución tiene su programa en esta serie; aquí se combinan para Copilot.

La clave está en las licencias, porque no todo exige E5. La DLP de prompts está disponible para todos los usuarios de Microsoft Copilot y Copilot Chat, incluso con E3. En cambio, impedir que Copilot procese archivos etiquetados requiere E5 o Purview Suite, y Communication Compliance sobre Copilot exige E5 o Purview Suite **más** Copilot. La tabla [Licencias](00_Programa.md#licencias) resume cada caso.

**Por qué importa**

Copilot multiplica la productividad y también la exposición de los datos. Estos controles convierten el debate de «Copilot sí o no» en una configuración medible: qué no puede procesar Copilot, qué se bloquea en un prompt, qué interacciones se conservan para un litigio y cuánto tarda el SOC en ver un uso riesgoso. Además, producen la evidencia que piden auditores y reguladores.

**Qué vas a lograr**

- Configurar DLP para la ubicación Microsoft Copilot: prompts con SIT, búsqueda web y exclusión de contenido etiquetado.
- Explicar qué controles están disponibles con E3, cuáles requieren E5 o Purview Suite y cuáles exigen Microsoft 365 Copilot.
- Configurar la retención de las ubicaciones de IA y verificarla con eDiscovery.
- Reconstruir una interacción con Audit: recursos accedidos, etiqueta, XPIA y agente.
- Activar Communication Compliance y la plantilla Risky AI usage con privacidad por diseño.

> **Atención.** Licencias, la confusión más común. La DLP de prompts está disponible para todos los usuarios de Microsoft Copilot y Copilot Chat, incluidos E3 y Business. La DLP que impide a Copilot procesar archivos y correos etiquetados exige E5/A5, Purview Suite, E5 Information Protection & Governance u Office 365 E5. Communication Compliance sobre prompts requiere E5 o Purview Suite **más** Microsoft Copilot; con E5 sola, no ([descripción del servicio](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)).

> **Novedad.** La política predeterminada «Protect sensitive M365 Copilot interactions» detecta SIT en los prompts y arranca en modo simulación ([política predeterminada](https://learn.microsoft.com/en-us/purview/dlp-microsoft365-copilot-location-default-policy)). El blog del 21 de abril de 2026 resume la GA de la DLP de prompts y la preview del bloqueo de búsqueda web con SIT ([DLP para Copilot](https://techcommunity.microsoft.com/blog/microsoft-security-blog/safeguarding-sensitive-data-in-microsoft-365-copilot-interactions-dlp-for-micros/4512497)). En una misma regla no se combinan condiciones de SIT y de etiquetas, y la exclusión de correo externo está en preview ([DLP para Copilot en Learn](https://learn.microsoft.com/en-us/purview/dlp-microsoft365-copilot-location-learn-about)).

> **Qué cambió.** Las interacciones de IA ya no usan la ubicación de retención «Teams chats and Copilot interactions», sino tres ubicaciones: Microsoft Copilot experiences, Enterprise AI apps y Other AI apps ([retención para IA](https://learn.microsoft.com/en-us/purview/retention-policies-copilot)). En eDiscovery, con E3 + Copilot puedes buscar, retener y exportar; la búsqueda Premium requiere E5 o Purview Suite + Copilot.

> **Consejo Ninja.** Audit (Standard) registra interacciones de Copilot en E3 y Business solo si Copilot está licenciado y en uso; Audit (Premium) agrega retención extendida con E5 o Purview Suite. Los registros incluyen AccessedResources, la etiqueta, XPIADetected y AgentId. La auditoría de apps de IA no Microsoft (AIAppInteraction) se cobra por uso y se conserva 180 días ([auditoría de IA](https://learn.microsoft.com/en-us/purview/audit-copilot)).

**¿Tienes poco tiempo?**

- [Learn about using Microsoft Purview DLP to protect interactions with Microsoft 365 Copilot, Copilot Chat, and Cowork](https://learn.microsoft.com/en-us/purview/dlp-microsoft365-copilot-location-learn-about) · Documentación
- [Microsoft Copilot data protection architecture](https://learn.microsoft.com/en-us/microsoft-365/copilot/architecture-data-protection-auditing) · Documentación
- [Secure and govern Microsoft 365 Copilot interactions with Microsoft Purview (learning path)](https://learn.microsoft.com/en-us/training/paths/purview-secure-govern-copilot-interactions/) · Curso
- [Safeguarding Sensitive Data in Microsoft 365 Copilot Interactions: DLP for Microsoft 365 Copilot](https://techcommunity.microsoft.com/blog/microsoft-security-blog/safeguarding-sensitive-data-in-microsoft-365-copilot-interactions-dlp-for-micros/4512497) · Blog oficial

### Documentación, cursos y credenciales

- [Microsoft Copilot data protection architecture](https://learn.microsoft.com/en-us/microsoft-365/copilot/architecture-data-protection-auditing) · Documentación · Oficial · Nuevo · Microsoft Learn · 19 oct 2026. Arquitectura de protección de datos de Copilot: respeta permisos, requiere derechos EXTRACT y VIEW en contenido cifrado, hereda la etiqueta de mayor prioridad y registra prompts y respuestas para auditoría, eDiscovery y retención.
- [Learn about using Microsoft Purview DLP to protect interactions with Microsoft 365 Copilot, Copilot Chat, and Cowork](https://learn.microsoft.com/en-us/purview/dlp-microsoft365-copilot-location-learn-about) · Documentación · Oficial · Microsoft Learn. Describe los cuatro controles DLP para Copilot: bloquear búsqueda web con SIT, bloquear prompts con SIT, excluir archivos y correos etiquetados y excluir correo externo (preview), con roles como Purview Data Security AI Admin.
- [Learn about the default DLP policy for Microsoft 365 Copilot location](https://learn.microsoft.com/en-us/purview/dlp-microsoft365-copilot-location-default-policy) · Documentación · Oficial · Microsoft Learn. Política DLP predeterminada Protect sensitive M365 Copilot interactions que detecta SIT en prompts y arranca en modo simulación con sugerencias de directiva.
- [Configure a Communication Compliance policy to detect generative AI interactions](https://learn.microsoft.com/en-us/purview/communication-compliance-copilot) · Documentación · Oficial · Microsoft Learn. Configura Communication Compliance para analizar prompts y respuestas de Microsoft 365 Copilot, agentes de Copilot Studio y apps de IA conectadas; las apps no Microsoft 365 requieren pay-as-you-go.
- [Learn about Insider Risk Management policy templates](https://learn.microsoft.com/en-us/purview/insider-risk-management-policy-templates) · Documentación · Oficial · Microsoft Learn. Catálogo de plantillas de IRM, incluidas Risky AI usage y Risky Agents, con prerrequisitos, eventos desencadenantes y límites de 100 directivas por plantilla.
- [Learn about retention for Copilot & AI apps](https://learn.microsoft.com/en-us/purview/retention-policies-copilot) · Documentación · Oficial · Microsoft Learn. Explica las nuevas ubicaciones de retención separadas de Teams (Microsoft Copilot experiences, Enterprise AI apps y Other AI apps) y cómo se conservan prompts y respuestas en carpetas ocultas del buzón.
- [Use Microsoft Purview to manage data security & compliance for Microsoft 365 Copilot & Copilot Chat](https://learn.microsoft.com/en-us/purview/ai-m365-copilot) · Documentación · Oficial · Microsoft Learn. Tabla de capacidades de Purview para Microsoft 365 Copilot y Copilot Chat y lista de políticas de un clic (etiquetas, uso riesgoso de IA, comportamiento no ético, protección de datos etiquetados).
- [Audit logs for Copilot and AI applications](https://learn.microsoft.com/en-us/purview/audit-copilot) · Documentación · Oficial · Microsoft Learn. Describe los registros de auditoría de Copilot, Cowork y apps de IA (AccessedResources, etiqueta, XPIADetected, AgentId) y aclara que las apps de IA no Microsoft (AIAppInteraction) se facturan por PAYG con 180 días de retención.
- [Secure and govern Microsoft 365 Copilot interactions with Microsoft Purview (learning path)](https://learn.microsoft.com/en-us/training/paths/purview-secure-govern-copilot-interactions/) · Curso · Oficial · Microsoft Learn. Ruta de 7 módulos (6 h 8 min) que integra auditoría, etiquetas, DLP, Insider Risk y Communication Compliance para gobernar las interacciones con Copilot.
- [Create and manage Insider Risk Management policies](https://learn.microsoft.com/en-us/purview/insider-risk-management-policies) · Documentación · Oficial · Microsoft Learn. Explica el panel de directivas de IRM con categorías de usuario y de agente (Copilot Studio y Foundry), directivas rápidas y recomendaciones desde analítica.

### Anuncios y blogs oficiales

- [Safeguarding Sensitive Data in Microsoft 365 Copilot Interactions: DLP for Microsoft 365 Copilot](https://techcommunity.microsoft.com/blog/microsoft-security-blog/safeguarding-sensitive-data-in-microsoft-365-copilot-interactions-dlp-for-micros/4512497) · Blog oficial · Empleado de Microsoft · Aaron Thorp · Microsoft Security Community Blog · 21 abr 2026. Explica la GA de DLP para prompts de Microsoft 365 Copilot y Copilot Chat (incluida para todos sus usuarios), el control por etiquetas desde noviembre de 2024 y la preview de bloqueo de búsqueda web con SIT.

### Comunidad: blogs, libros, newsletters y eventos

- [How to Deploy Microsoft Purview DLP for Copilot and Generative AI](https://nikkichapple.com/microsoft-purview-dlp-copilot-genai-setup-guide/) · Blog · Comunidad · Nuevo · Nikki Chapple · nikkichapple.com · 16 may 2026. Guía práctica con los seis controles DLP de mayor valor para Copilot e IA generativa (prompts, búsqueda web, contenido etiquetado, pegar/subir a sitios de IA, Edge) y estrategia de despliegue.

**Manos a la obra**

1. `Laboratorio parcial` DLP de prompts: en la ubicación Microsoft Copilot crea una política que bloquee prompts con un SIT de prueba (un número de tarjeta sintético) y pruébala en Copilot Chat con una cuenta de prueba ([DLP para Copilot](https://learn.microsoft.com/en-us/purview/dlp-microsoft365-copilot-location-learn-about)). Limitación: la exclusión de archivos etiquetados solo se comprueba con Microsoft 365 Copilot licenciado. Evidencia: captura del bloqueo y de la coincidencia en el explorador de actividad.
2. `Laboratorio parcial` Activa en simulación la política predeterminada «Protect sensitive M365 Copilot interactions», revisa sus coincidencias y sugerencias y documenta qué ajustarías antes de activarla ([política predeterminada](https://learn.microsoft.com/en-us/purview/dlp-microsoft365-copilot-location-default-policy)). Limitación: necesitas actividad de Copilot para ver coincidencias. Evidencia: informe de simulación con decisiones.
3. `Laboratorio parcial` Exclusión de contenido etiquetado: crea una regla que impida a Copilot procesar archivos con tu etiqueta más restrictiva y comprueba que Copilot no los resume; recuerda que no se mezclan condiciones de SIT y de etiquetas en la misma regla. Limitación: requiere E5 y Microsoft 365 Copilot, que puedes comprar en el sandbox. Evidencia: prueba con y sin la regla.
4. `Laboratorio parcial` Retención: crea una política para la ubicación Microsoft Copilot experiences con un período corto para las cuentas de prueba y verifica con eDiscovery, una semana después, que se aplicó ([retención para IA](https://learn.microsoft.com/en-us/purview/retention-policies-copilot)). Limitación: requiere Copilot licenciado y el temporizador tarda de 1 a 7 días. Evidencia: política publicada y búsqueda con resultados.
5. `Laboratorio parcial` Auditoría: busca en Audit las actividades de Copilot de una cuenta de prueba y reconstruye una interacción con sus recursos accedidos, la etiqueta y el campo XPIADetected ([auditoría de IA](https://learn.microsoft.com/en-us/purview/audit-copilot)). Limitación: Audit (Standard) registra Copilot solo si está licenciado y en uso. Evidencia: exportación de la búsqueda con una interacción explicada.
6. `Laboratorio parcial` Crea con plantillas una política de Communication Compliance para IA generativa ([Communication Compliance para IA](https://learn.microsoft.com/en-us/purview/communication-compliance-copilot)) y la política Risky AI usage ([plantillas de Insider Risk](https://learn.microsoft.com/en-us/purview/insider-risk-management-policy-templates)), ambas acotadas a cuentas de prueba, y verifica que la seudonimización está activa. Limitación: Communication Compliance sobre Copilot requiere E5 + Copilot, y las alertas tardan entre 24 y 48 horas. Evidencia: políticas creadas y captura de la seudonimización.
7. `Solo producción` Piloto de DLP para Copilot: aplica la DLP de prompts en simulación a un grupo piloto con Copilot, revisa dos semanas de coincidencias con el dueño del proceso y pasa a bloqueo solo con aprobación. Cómo hacerlo seguro: modo simulación, grupo piloto informado, comunicación previa y reversión inmediata desactivando la regla. Evidencia: informe de simulación y aprobación del cambio.

**¿Quieres profundizar?**

- [How to Deploy Microsoft Purview DLP for Copilot and Generative AI](https://nikkichapple.com/microsoft-purview-dlp-copilot-genai-setup-guide/) · Blog

<a id="m2"></a>

## M2 · Seguridad de datos para agentes de Copilot Studio, Microsoft Foundry y Agent 365

*L300 · ~8 h · Origen: Ruta SC-401 de IA, módulo 4 (entornos de desarrollo: Foundry, Copilot Studio y Fabric)*

Los agentes son los nuevos consumidores de datos: leen, combinan y actúan con identidad propia o delegada. Purview trata a las instancias de agente de **Agent 365** como si fueran usuarios: las audita y clasifica automáticamente, las incluye en las políticas y las muestra en la observabilidad de IA de la nueva DSPM. Si el contenido tiene una etiqueta que cifra, el agente necesita los derechos VIEW y EXTRACT para devolverlo. Así, los agentes heredan etiquetas, DLP, retención, auditoría y eDiscovery sin un modelo de seguridad paralelo.

El 1 de mayo de 2026 llegaron a disponibilidad general **Microsoft 365 E7** y **Agent 365**. E7 cuesta 99 USD por usuario al mes e incluye Microsoft 365 Copilot, Microsoft 365 E5, Entra Suite y Agent 365; Agent 365 también se vende aparte a 15 USD (precios de lista de EE. UU.). La observabilidad de IA y la gestión del riesgo interno para agentes llegaron a GA entre mediados de junio y fines de julio de 2026 y **no están disponibles sin E7 o Agent 365**.

Cada plataforma tiene sus particularidades. En **Copilot Studio**, los agentes publicados en canales que no son de Microsoft requieren pago por uso. En **Microsoft Foundry**, la integración se habilita desde el Foundry Control Plane o desde Defender for Cloud; las políticas son de pago por uso, pero la auditoría está incluida en la licencia de Purview. La política **Risky Agents** de Insider Risk cubre agentes de Copilot Studio, Foundry y del SDK y comparte su riesgo con DSPM. La identidad de los agentes se trata en el programa de Entra (módulos X2, X4 y X6).

**Por qué importa**

Un agente con acceso excesivo multiplica la sobreexposición y trabaja las 24 horas. Este módulo da al centro de excelencia de IA un inventario de agentes con su riesgo y políticas que los cubren como a cualquier usuario. También le da una decisión de licencias fundamentada (E5 frente a E7 o Agent 365, más pago por uso) y un procedimiento para proteger los datos de contexto antes de publicar un agente.

**Qué vas a lograr**

- Explicar cómo trata Purview a los agentes de Agent 365, Copilot Studio y Microsoft Foundry.
- Decidir qué capacidades requieren E7 o Agent 365 y cuáles pago por uso.
- Habilitar Purview para Microsoft Foundry desde el Foundry Control Plane o desde Defender for Cloud.
- Configurar la política Risky Agents y conocer sus límites, como las unidades administrativas.
- Proteger los datos de contexto de un agente con etiquetas, retención y DLP para Copilot.

> **Novedad.** Microsoft 365 E7 y Agent 365 llegaron a GA el 1 de mayo de 2026. E7 cuesta 99 USD por usuario al mes e incluye Microsoft 365 Copilot, Microsoft 365 E5, Entra Suite y Agent 365; Agent 365 se vende también por separado a 15 USD por usuario al mes, en precios de lista de EE. UU. ([anuncio](https://techcommunity.microsoft.com/blog/microsoft_365blog/microsoft-365-e7-and-agent-365-are-now-generally-available/4516295)).

> **Atención.** AI observability de DSPM e Insider Risk Management para agentes: GA mundial de mediados de junio a fines de julio de 2026, tras una preview de diciembre de 2025 a abril de 2026. Sin Microsoft 365 E7 o Agent 365 no están disponibles ([MC1280556](https://message.cengizyilmaz.net/message/mc1280556-microsoft-purview-for-agents-ai-observability-and-insider-risk-management-now-generally-available)). La página de la política Risky Agents, actualizada el 4 de agosto de 2026, todavía la marca como preview, y las unidades administrativas no admiten alertas de agentes ([monitorear agentes](https://learn.microsoft.com/en-us/purview/insider-risk-management-monitoring-agents)).

> **Atención.** La descripción del servicio todavía dice que las capacidades de Purview para agentes de Microsoft Foundry y apps conectadas a Entra «serán soportadas» por E7 y Agent 365, aunque MC1280556 ya marcó la GA ([descripción del servicio](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)). Confírmalo con tu equipo de licenciamiento antes de comprar.

> **Consejo Ninja.** En Foundry, habilita Purview desde el Foundry Control Plane o desde Defender for Cloud: las políticas requieren pago por uso, pero la auditoría está incluida en la licencia de Purview ([Purview para Foundry](https://learn.microsoft.com/en-us/purview/ai-azure-foundry)). En Copilot Studio, los agentes publicados en canales que no son de Microsoft requieren pago por uso ([Purview para Copilot Studio](https://learn.microsoft.com/en-us/purview/ai-copilot-studio)).

**¿Tienes poco tiempo?**

- [Use Microsoft Purview to manage data security & compliance for Microsoft Agent 365](https://learn.microsoft.com/en-us/purview/ai-agent-365) · Documentación
- [MC1280556 – Microsoft Purview for agents: AI observability and insider risk management now generally available (archivo)](https://message.cengizyilmaz.net/message/mc1280556-microsoft-purview-for-agents-ai-observability-and-insider-risk-management-now-generally-available) · Herramienta
- [Use Microsoft Purview to manage data security & compliance for Microsoft Foundry](https://learn.microsoft.com/en-us/purview/ai-azure-foundry) · Documentación
- [Data Security & Compliance for Azure Foundry AI Apps & Agents (webinar)](https://www.youtube.com/watch?v=j3lgwtAOnZU) · Webinar

### Documentación, cursos y credenciales

- [Use Microsoft Purview to manage data security & compliance for Entra-registered AI apps](https://learn.microsoft.com/en-us/purview/ai-entra-registered) · Documentación · Oficial · Microsoft Learn. Capacidades de Purview para apps de IA personalizadas registradas en Entra e integradas con el SDK de Purview (auditoría, clasificación, etiquetas, DLP, IRM, retención), con facturación pay-as-you-go.
- [Secure AI agents at scale using Microsoft Agent 365](https://learn.microsoft.com/en-us/security/security-for-ai/agent-365-security) · Documentación · Oficial · Microsoft Learn. Explica cómo Agent 365 extiende Entra, Purview y Defender a los agentes: identidad y acceso condicional, DSPM, etiquetas, DLP, IRM, auditoría, retención, eDiscovery y postura de agentes.
- [Use Microsoft Purview to manage data security & compliance for Microsoft Agent 365](https://learn.microsoft.com/en-us/purview/ai-agent-365) · Documentación · Oficial · Microsoft Learn. Tabla de capacidades de Purview para instancias de agente de Agent 365: auditoría y clasificación automáticas, inclusión en directivas como si fueran usuarios y observabilidad de IA solo en la nueva DSPM.
- [Use Microsoft Purview to manage data security & compliance for Microsoft Foundry](https://learn.microsoft.com/en-us/purview/ai-azure-foundry) · Documentación · Oficial · Microsoft Learn. Capacidades de Purview para interacciones de Microsoft Foundry y cómo habilitarlas desde el Foundry Control Plane o desde Defender for Cloud; las directivas requieren PAYG pero la auditoría está incluida en la licencia.
- [Use Microsoft Purview to manage data security & compliance for Microsoft Copilot Studio](https://learn.microsoft.com/en-us/purview/ai-copilot-studio) · Documentación · Oficial · Microsoft Learn. Capacidades de Purview para agentes de Copilot Studio, con PAYG obligatorio cuando los agentes se publican en canales que no son de Microsoft.
- [Step 2: Protect sensitive info in grounding data - Secure and govern Microsoft 365 Copilot agents](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-sc-agents-step2) · Documentación · Oficial · Microsoft Learn · 3 abr 2026. Paso del modelo de despliegue para agentes: etiquetar SharePoint y Dataverse, reducir datos obsoletos con retención, excluir archivos etiquetados con DLP para Copilot y políticas de datos de Dataverse.
- [Monitoring agents with Insider Risk Management](https://learn.microsoft.com/en-us/purview/insider-risk-management-monitoring-agents) · Documentación · Oficial · Vista previa · Nuevo · Microsoft Learn · 4 ago 2026. Explica la directiva predeterminada Risky Agents (preview) para agentes de Copilot Studio, Foundry y del SDK, sus detecciones y cómo el riesgo del agente se comparte con DSPM y el centro de administración de Microsoft 365. *Nota:* Las unidades administrativas no admiten alertas de agentes
- [How does Microsoft Purview support Agent 365?](https://learn.microsoft.com/en-us/microsoft-agent-365/guidance/purview-agent-365) · Documentación · Oficial · Nuevo · Microsoft Learn · 19 ago 2026. Guía conceptual que explica cómo los agentes de Agent 365 heredan etiquetas, DLP, retención, auditoría y eDiscovery de Purview sin un modelo de seguridad paralelo.
- [Step 1: Discover risks and identify gaps - Secure and govern Microsoft 365 Copilot agents](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-sc-agents-step1) · Documentación · Oficial · Microsoft Learn · 3 abr 2026. Primer paso del modelo para agentes: activar auditoría, evaluar sobreexposición, descubrir datos sensibles en Dataverse con Unified Catalog, revisar el informe de apps y agentes y brechas regulatorias con Compliance Manager.

### Anuncios y blogs oficiales

- [Microsoft 365 E7 and Agent 365 are now generally available](https://techcommunity.microsoft.com/blog/microsoft_365blog/microsoft-365-e7-and-agent-365-are-now-generally-available/4516295) · Blog oficial · Empleado de Microsoft · Nuevo · Caroline Stanford · Microsoft 365 Blog (Tech Community) · 1 may 2026. Anuncia la GA de Microsoft 365 E7 (Copilot + E5 + Entra Suite + Agent 365, 99 USD/usuario/mes) y de Agent 365 (también independiente a 15 USD/usuario/mes).

### Webinars, videos y podcasts

- [Data Security & Compliance for Azure Foundry AI Apps & Agents (webinar)](https://www.youtube.com/watch?v=j3lgwtAOnZU) · Webinar · Empleado de Microsoft · Ajay Kallur, Safeena Begum Lepakshi · Microsoft Security Community (YouTube) · 8 ene 2026. Webinar oficial sobre controles de Purview y DSPM para IA en apps y agentes de Foundry: informes, explorador de actividad, inventario de apps y agentes y gobierno de interacciones.

### Laboratorios, GitHub y herramientas

- [MC1280556 – Microsoft Purview for agents: AI observability and insider risk management now generally available (archivo)](https://message.cengizyilmaz.net/message/mc1280556-microsoft-purview-for-agents-ai-observability-and-insider-risk-management-now-generally-available) · Herramienta · Comunidad · Nuevo · Microsoft (archivado por Cengiz Yilmaz) · Microsoft 365 Message Center Archive (cengizyilmaz.net) · 21 may 2026. Confirma la GA (mediados de junio a fin de julio de 2026) de DSPM – AI Observability e Insider Risk Management para agentes, disponibles solo con suscripciones Microsoft 365 E7 o Agent 365.

**Manos a la obra**

1. `Laboratorio parcial` Purview en Microsoft Foundry: habilita la seguridad de datos de Purview para Foundry desde Defender for Cloud o desde el Foundry Control Plane, envía prompts a un modelo desplegado y revisa la actividad en DSPM ([Purview para Foundry](https://learn.microsoft.com/en-us/purview/ai-azure-foundry)). Limitación: las políticas requieren pago por uso y la postura de agentes requiere Agent 365; usa una suscripción con presupuesto. Evidencia: eventos de la app de Foundry en el explorador de actividad.
2. `Laboratorio parcial` Derechos de uso y agentes: crea un agente de prueba en Copilot Studio con conocimiento de un sitio que contenga un archivo con una etiqueta que cifra, y compara la respuesta con y sin los derechos VIEW y EXTRACT ([Purview para Agent 365](https://learn.microsoft.com/en-us/purview/ai-agent-365)). Limitación: necesitas un entorno de Copilot Studio en el inquilino de prueba. Evidencia: las dos respuestas comparadas.
3. `Laboratorio` Modelo para agentes, pasos 1 y 2: para un agente piloto completa el checklist de descubrir riesgos (auditoría, sobreexposición e informe de apps y agentes) y de proteger los datos de contexto (etiquetas en SharePoint y Dataverse, retención de datos obsoletos y DLP para Copilot) ([paso 1](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-sc-agents-step1), [paso 2](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-sc-agents-step2)). Evidencia: checklist con responsables.
4. `Laboratorio` Matriz de licencias de agentes: para tres agentes (uno de Copilot Studio interno, uno de Copilot Studio publicado en un canal que no es de Microsoft y uno de Foundry) indica qué capacidades de Purview aplican con E5, cuáles con E7 o Agent 365 y cuáles con pago por uso ([Purview para Copilot Studio](https://learn.microsoft.com/en-us/purview/ai-copilot-studio)). Evidencia: matriz revisada por licenciamiento.
5. `Solo producción` Risky Agents con E7 o Agent 365: aplica la plantilla con un alcance piloto, mantén la seudonimización activa, revisa sin acciones automáticas y documenta qué decisiones requieren supervisión humana ([monitorear agentes](https://learn.microsoft.com/en-us/purview/insider-risk-management-monitoring-agents)). Cómo hacerlo seguro: piloto acotado, revisión manual y roles mínimos; las unidades administrativas no admiten alertas de agentes. Evidencia: política activa y procedimiento de revisión.
6. `Solo producción` AI observability de agentes: revisa los agentes con actividad en los últimos 30 días y su riesgo y, para el de mayor riesgo, acuerda con su patrocinador acciones como reducir su conocimiento, etiquetar las fuentes o aplicar DLP ([MC1280556](https://message.cengizyilmaz.net/message/mc1280556-microsoft-purview-for-agents-ai-observability-and-insider-risk-management-now-generally-available)). Cómo hacerlo seguro: solo lectura, ningún bloqueo de agentes productivos sin aprobación y registro de la decisión. Evidencia: plan de acción del agente.

<a id="m3"></a>

## M3 · IA de terceros: navegador, endpoint, red e IA en la sombra

*L300 · ~6 h · Origen: Ruta SC-401 de IA, módulo 3 (apps de IA empresariales y de navegador), y ruta Ninja de Purview, módulo 5 (Endpoint DLP)*

La IA en la sombra es la fuga más cotidiana: alguien pega un contrato en ChatGPT, Gemini o DeepSeek para resumirlo. El modelo oficial «Prevent data leak to shadow AI» tiene cuatro pasos y empieza por descubrir antes de bloquear. Una forma práctica de resumirlo, que propone la comunidad, son dos capas. La primera **controla las apps**: las descubre, las sanciona o las bloquea con Defender for Cloud Apps, Entra Internet Access, la protección adaptable con acceso condicional e Intune. La segunda **controla los datos** con Purview: Endpoint DLP, la extensión de navegador, la DLP de Edge for Business y Network Data Security.

Gestionar la IA de terceros con Purview exige tener habilitado el **pago por uso**. La mayoría de las capacidades requieren la extensión de navegador de Purview y dispositivos incorporados; las excepciones son la seguridad de datos en la red y en Edge. Las etiquetas de confidencialidad no se admiten. Communication Compliance, eDiscovery y retención solo funcionan en Edge con ChatGPT, Microsoft Chat (consumo), Gemini y DeepSeek, y además requieren una directiva de colección con captura de contenido. Para empezar hay cuatro políticas de un clic: detectar información sensible agregada a sitios de IA, detectar visitas a sitios de IA, detectar información sensible en prompts en Edge y detectar información sensible compartida con IA por la red.

Para la IA empresarial existen **conectores**: ChatGPT Enterprise y Claude Enterprise (este último en preview) ingieren interacciones por sus Compliance API, sin DLP ni etiquetas y con pago por uso. Las **directivas de colección** no tienen licencia propia, usan la del workload y pueden filtrar eventos por región para respetar requisitos de privacidad distintos. La DLP de endpoint y de navegador se profundiza en el programa de DLP (módulos I3 y M3).

**Por qué importa**

Según el Data Security Index 2026, el 32 % de los incidentes de datos ya involucra IA generativa y solo el 47 % de las organizaciones aplica controles específicos de IA. Este módulo te da visibilidad primero (modo auditoría) y bloqueo dirigido después, sin prohibir la IA en bloque. Lo acompaña un modelo de costos de pago por uso que el dueño del presupuesto puede aprobar.

**Qué vas a lograr**

- Descubrir y clasificar apps de IA con Defender for Cloud Apps y bloquear las no autorizadas.
- Elegir la vía de control adecuada: extensión y endpoint, Edge for Business, red o conector.
- Activar en modo auditoría las políticas de un clic para sitios de IA.
- Crear una directiva de colección acotada por grupo o región, con y sin captura de contenido.
- Estimar y vigilar el costo de pago por uso en el Usage center y en Azure.

> **Atención.** Requisitos para la IA de terceros: pago por uso habilitado y, para la mayoría de las capacidades, la extensión de navegador de Purview y dispositivos incorporados (las excepciones son la red y Edge). Las etiquetas no se admiten. Communication Compliance, eDiscovery y retención funcionan solo en Edge con ChatGPT, Microsoft Chat (consumo), Gemini y DeepSeek, y con una directiva de colección con captura de contenido ([otras apps de IA](https://learn.microsoft.com/en-us/purview/ai-other-apps)).

> **Consejo Ninja.** Licencias de cada vía: la DLP de Edge for Business es de pago por uso de dispositivo administrado a app no administrada, y está incluida en E5 para apps registradas en Entra ([descripción del servicio](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)). Network Data Security con Global Secure Access requiere E7 o Purview E5 + Entra Internet Access, y con un SASE de terceros, Purview E5 + pago por uso ([Network Data Security](https://learn.microsoft.com/en-us/purview/dlp-network-data-security-learn)). iboss y Netskope llegaron a GA entre mediados de noviembre y diciembre de 2025 ([MC1182008](https://message.cengizyilmaz.net/message/mc1182008-microsoft-purview-inline-protection-for-sensitive-data-shared-over-the-network-with-nonmicrosoft-sase-integrations)).

> **Novedad.** Conectores para IA empresarial: ChatGPT Enterprise (vigente) y Claude Enterprise (preview) ingieren interacciones por sus Compliance API, sin DLP ni etiquetas y con pago por uso. Las conversaciones de ChatGPT llegan con 24 horas de retraso ([ChatGPT Enterprise](https://learn.microsoft.com/en-us/purview/archive-chatgpt-interactions), [Claude Enterprise](https://learn.microsoft.com/en-us/purview/ai-claude-enterprise)). La Claude Compliance API para Purview se anunció el 21 de mayo de 2026 ([novedades de mayo](https://www.microsoft.com/en-us/security/blog/2026/05/21/whats-new-in-microsoft-security-may-2026/)).

> **Atención.** La guía de inicio para IA de terceros, actualizada el 1 de mayo de 2026, todavía usa DSPM for AI (classic) como punto de partida, aunque esa experiencia se retira en enero de 2027 ([otras apps de IA](https://learn.microsoft.com/en-us/purview/ai-other-apps)). Traduce cada paso a la nueva DSPM.

**¿Tienes poco tiempo?**

- [Use Microsoft Purview to manage data security & compliance for other AI apps](https://learn.microsoft.com/en-us/purview/ai-other-apps) · Documentación
- [Step 1: Discover AI apps - Prevent data leak to shadow AI](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-data-leak-shadow-ai-step1) · Documentación
- [Collection Policies solution overview](https://learn.microsoft.com/en-us/purview/collection-policies-solution-overview) · Documentación

**Vías de control para la IA de terceros**

| Vía | Qué controla | Requisitos | Licencia | Límites | Fuente |
|---|---|---|---|---|---|
| Defender for Cloud Apps | La app: descubre, sanciona y bloquea apps de IA generativa del catálogo | Integración con Defender for Endpoint para bloquear en el dispositivo | Incluido en E5 | Controla el acceso a la app, no el dato que se comparte | [Apps de IA generativa](https://learn.microsoft.com/en-us/copilot/manage/manage-generative-ai-apps) |
| Extensión de navegador y Endpoint DLP | El dato: advierte o bloquea pegar y subir información sensible a sitios de IA; políticas de un clic | Dispositivos incorporados y extensión de Purview | E5 o Purview Suite + pago por uso para IA de terceros | Sin etiquetas; Communication Compliance, eDiscovery y retención solo en Edge con ChatGPT, Microsoft Chat, Gemini y DeepSeek | [Otras apps de IA](https://learn.microsoft.com/en-us/purview/ai-other-apps) |
| DLP en Edge for Business | El dato en el navegador, sin incorporar el dispositivo; apps administradas en dispositivos personales | Edge for Business | Pago por uso de dispositivo administrado a app no administrada; E5 para apps registradas en Entra | No aplica a invitados B2B | [DLP en Edge for Business](https://learn.microsoft.com/en-us/purview/dlp-browser-dlp-learn) |
| Network Data Security | El dato en la red, con inspección en línea del tráfico hacia apps de IA | Global Secure Access o un SASE de terceros (iboss y Netskope en GA desde noviembre y diciembre de 2025) | E7 o Purview E5 + Entra Internet Access (Global Secure Access); Purview E5 + pago por uso (terceros) | Algunas funciones están en preview según el socio | [Network Data Security](https://learn.microsoft.com/en-us/purview/dlp-network-data-security-learn) |
| Conectores de ChatGPT Enterprise y Claude Enterprise | Las interacciones ingeridas: auditoría, clasificación, Insider Risk, Communication Compliance, eDiscovery y retención | Compliance API del proveedor; Data Map y Key Vault para ChatGPT Enterprise | Pago por uso | Sin DLP ni etiquetas; ChatGPT llega con 24 horas de retraso; Claude en preview | [ChatGPT Enterprise](https://learn.microsoft.com/en-us/purview/ai-chatgpt-enterprise) · [Claude Enterprise](https://learn.microsoft.com/en-us/purview/ai-claude-enterprise) |
| Directivas de colección | Qué eventos y qué contenido de IA se ingieren en Purview (captura de prompts y respuestas) | Workload licenciado; para la red, inquilino vinculado a Azure | Sin licencia propia | Capturar contenido almacena datos personales: requiere evaluación de impacto | [Directivas de colección](https://learn.microsoft.com/en-us/purview/collection-policies-solution-overview) |

Modelo de dos capas (controlar la app y controlar el dato) según el modelo oficial contra la IA en la sombra ([paso 1](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-data-leak-shadow-ai-step1)) y su resumen comunitario ([guía de Nikki Chapple](https://nikkichapple.com/govern-shadow-ai-microsoft-purview-defender-dspm/)).

### Documentación, cursos y credenciales

- [Use Microsoft Purview to manage data security & compliance for other AI apps](https://learn.microsoft.com/en-us/purview/ai-other-apps) · Documentación · Oficial · Nuevo · Microsoft Learn · 1 may 2026. Tabla de capacidades de Purview para sitios de IA de terceros (ChatGPT, Gemini, DeepSeek) vía navegador, endpoint y red; requiere pay-as-you-go y no admite etiquetas de sensibilidad.
- [Learn about Microsoft Purview Network Data Security](https://learn.microsoft.com/en-us/purview/dlp-network-data-security-learn) · Documentación · Oficial · Microsoft Learn. Explica la seguridad de datos en red con SASE o navegadores seguros y su licenciamiento: Microsoft 365 E7 o Purview E5 + Entra Internet Access para GSA, y Purview E5 + PAYG para SASE de terceros.
- [Manage generative AI apps for your organization](https://learn.microsoft.com/en-us/copilot/manage/manage-generative-ai-apps) · Documentación · Oficial · Microsoft Learn. Explica cómo combinar DSPM para IA, Defender for Cloud Apps (catálogo Generative AI, políticas y bloqueo) y Defender CSPM para gobernar apps de IA de Microsoft y de terceros.
- [Use Microsoft Purview to manage data security & compliance for ChatGPT Enterprise](https://learn.microsoft.com/en-us/purview/ai-chatgpt-enterprise) · Documentación · Oficial · Microsoft Learn. Capacidades de Purview para ChatGPT Enterprise vía conector (auditoría, clasificación, IRM, Communication Compliance, eDiscovery, retención) sin DLP ni etiquetas, con PAYG obligatorio.
- [Learn about Data Loss Prevention for Cloud Apps in Edge for Business](https://learn.microsoft.com/en-us/purview/dlp-browser-dlp-learn) · Documentación · Oficial · Microsoft Learn. DLP integrada en Edge for Business sin incorporar el dispositivo: bloquea compartir datos sensibles con apps de IA no administradas (ChatGPT, Gemini, DeepSeek) y protege apps administradas en dispositivos BYOD.
- [Collection Policies solution overview](https://learn.microsoft.com/en-us/purview/collection-policies-solution-overview) · Documentación · Oficial · Microsoft Learn. Explica las directivas de colección que filtran qué eventos, clasificaciones y prompts/respuestas de IA se ingieren en Purview (captura de contenido) y cómo alimentan explorador de actividad, DSPM, IRM, eDiscovery y DLM.
- [Step 1: Discover AI apps - Prevent data leak to shadow AI](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-data-leak-shadow-ai-step1) · Documentación · Oficial · Microsoft Learn · 3 abr 2026. Primer paso del modelo contra la IA en la sombra: descubrir apps con Defender for Cloud Apps, interacciones con DSPM e IRM antes de bloquear.
- [Step 2: Block access to unsanctioned AI apps - Prevent data leak to shadow AI](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-data-leak-shadow-ai-step2) · Documentación · Oficial · Microsoft Learn · 3 abr 2026. Bloquea apps de IA no autorizadas con Defender for Cloud Apps, Entra Internet Access, Protección adaptable con acceso condicional e Intune.
- [Use Network Data Security to help prevent sharing sensitive information with unmanaged AI](https://learn.microsoft.com/en-us/purview/dlp-create-policy-ai-network-data-security) · Documentación · Oficial · Vista previa · Microsoft Learn. Escenario paso a paso para crear una directiva DLP que bloquee el envío de datos sensibles a apps de IA no administradas mediante Entra Global Secure Access o un SASE/navegador seguro de terceros. *Nota:* Algunas funciones del escenario están en preview
- [Connect to and manage ChatGPT Enterprise AI interactions in Microsoft Purview (preview)](https://learn.microsoft.com/en-us/purview/archive-chatgpt-interactions) · Documentación · Oficial · Vista previa · Microsoft Learn. Pasos para registrar y escanear un workspace de ChatGPT Enterprise en el Data Map con Key Vault, clave de Compliance API con alcance de lectura y política de colección. *Nota:* Las conversaciones se ingieren con 24 h de retraso por límites de la API de OpenAI
- [Use Microsoft Purview to manage data security & compliance for Anthropic Claude (Enterprise)](https://learn.microsoft.com/en-us/purview/ai-claude-enterprise) · Documentación · Oficial · Vista previa · Microsoft Learn. Capacidades de Purview para Claude Enterprise mediante conector en preview (auditoría, clasificación, IRM, Communication Compliance, eDiscovery, retención), sin DLP ni etiquetas y con PAYG. *Nota:* Sin políticas de un clic aún; agentes de Claude no aparecen en AI observability

### Laboratorios, GitHub y herramientas

- [Block Access to Unsanctioned AI Apps with Defender for Cloud Apps (Zero Trust Workshop – AI)](https://microsoft.github.io/zerotrustassessment/docs/workshop-guidance/AI/AI_099) · Laboratorio · Oficial · Microsoft Zero Trust Workshop (GitHub Pages). Tarea del taller Zero Trust que explica cómo pasar del descubrimiento de IA en la sombra al bloqueo por app en Defender for Cloud Apps, complementando el filtrado por categoría de Global Secure Access.
- [MC1182008 – Inline protection for sensitive data shared over the network with non-Microsoft SASE integrations (archivo)](https://message.cengizyilmaz.net/message/mc1182008-microsoft-purview-inline-protection-for-sensitive-data-shared-over-the-network-with-nonmicrosoft-sase-integrations) · Herramienta · Comunidad · Microsoft (archivado por Cengiz Yilmaz) · Microsoft 365 Message Center Archive (cengizyilmaz.net) · nov 2025. Anuncia la GA (mediados de noviembre a diciembre de 2025) de la protección DLP en línea con iboss y Netskope para más de 35.000 apps en la nube, que requiere PAYG.

### Comunidad: blogs, libros, newsletters y eventos

- [How to Govern Shadow AI with Microsoft Purview, Defender and DSPM](https://nikkichapple.com/govern-shadow-ai-microsoft-purview-defender-dspm/) · Blog · Comunidad · Nuevo · Nikki Chapple · nikkichapple.com · 31 may 2026. Simplifica el modelo oficial Prevent data leak to shadow AI en dos capas (controlar apps y controlar datos) con pasos de descubrimiento, evaluación, bloqueo, DLP y auditoría.

**Manos a la obra**

1. `Laboratorio` IA en la sombra: en Defender for Cloud Apps revisa el catálogo de IA generativa, marca una app como no autorizada y verifica el bloqueo en un dispositivo de prueba incorporado a Defender for Endpoint ([bloquear apps no autorizadas](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-data-leak-shadow-ai-step2), [taller Zero Trust](https://microsoft.github.io/zerotrustassessment/docs/workshop-guidance/AI/AI_099)). Evidencia: captura del bloqueo en el navegador y del evento.
2. `Laboratorio parcial` Políticas de un clic para sitios de IA: en una VM Windows 11 en Azure incorpora el dispositivo a Purview, instala la extensión de navegador y activa «Detect sensitive info added to AI sites» y «Detect when users visit AI sites» ([otras apps de IA](https://learn.microsoft.com/en-us/purview/ai-other-apps)). Limitación: requiere pago por uso, que el crédito de Visual Studio puede no cubrir. Evidencia: políticas en auditoría y eventos en el explorador de actividad.
3. `Laboratorio parcial` Endpoint DLP en sitios de IA: crea una regla que advierta con posibilidad de invalidación al pegar un SIT de prueba en un sitio de IA generativa y pruébala en Edge y en Chrome con la extensión. Limitación: gestionar IA de terceros requiere pago por uso y la VM no reproduce el comportamiento de usuarios reales. Evidencia: aviso al usuario y evento con la justificación.
4. `Laboratorio parcial` Directiva de colección: crea una directiva acotada a Edge y a apps de IA, primero sin captura de contenido y luego con captura de prompts y respuestas para una cuenta de prueba, y comprueba el evento «AI interaction» ([directivas de colección](https://learn.microsoft.com/en-us/purview/collection-policies-solution-overview)). Limitación: requiere pago por uso y apps soportadas; en producción, acota por región o grupo y documenta la finalidad del tratamiento. Evidencia: directiva configurada y evento registrado.
5. `Laboratorio parcial` Costos: a las 48 horas revisa en el Usage center el consumo de pago por uso por función y configura alertas de presupuesto de Azure al 50, 75 y 90 % ([Usage center](https://learn.microsoft.com/en-us/purview/purview-billing-usage)). Limitación: el Usage center está en preview. Evidencia: captura del consumo y presupuesto configurado.
6. `Solo producción` Network Data Security: con Global Secure Access (E7 o E5 + Entra Internet Access) o con un SASE de terceros (E5 + pago por uso), crea una política DLP en modo auditoría para un grupo piloto que detecte datos sensibles enviados a apps de IA no administradas ([escenario de red](https://learn.microsoft.com/en-us/purview/dlp-create-policy-ai-network-data-security)). Cómo hacerlo seguro: auditoría primero, grupo piloto, lista de IA aprobadas para no bloquear herramientas sancionadas y presupuesto por solicitud. Evidencia: informe de dos semanas.

**¿Quieres profundizar?**

- [How to Govern Shadow AI with Microsoft Purview, Defender and DSPM](https://nikkichapple.com/govern-shadow-ai-microsoft-purview-defender-dspm/) · Blog
- [Block Access to Unsanctioned AI Apps with Defender for Cloud Apps (Zero Trust Workshop – AI)](https://microsoft.github.io/zerotrustassessment/docs/workshop-guidance/AI/AI_099) · Laboratorio
- [MC1182008 – Inline protection for sensitive data shared over the network with non-Microsoft SASE integrations (archivo)](https://message.cengizyilmaz.net/message/mc1182008-microsoft-purview-inline-protection-for-sensitive-data-shared-over-the-network-with-nonmicrosoft-sase-integrations) · Herramienta

<a id="m4"></a>

## M4 · SharePoint Advanced Management y la remediación de la sobreexposición

*L300 · ~5 h · Origen: Ruta de Learn de DSPM, módulo «Protect and remediate sensitive data in Microsoft Purview», y guía oficial para proteger y gobernar Copilot*

Purview encuentra la sobreexposición; **SharePoint Advanced Management (SAM)** la corrige en el origen. Basta asignar al menos una licencia de Copilot para habilitar funciones de SAM. Entre ellas están Restricted Access Control (RAC), Restricted Content Discovery (RCD), los informes de gobierno de acceso a datos (DAG), las revisiones de acceso del propietario, las políticas de sitios inactivos y las de propiedad del sitio. La creación restringida de sitios por apps requiere el complemento SAM Plan 1.

El marco oficial de controles de Copilot distingue dos capas. La capa **fundamental** se logra con E3 y SAM; la **optimizada** suma lo que trae E5: DSPM, autoetiquetado, Insider Risk y Defender for Cloud Apps. Para prevenir en lugar de corregir, las **etiquetas de contenedor** fijan la privacidad y el uso compartido desde que se crea el equipo o el sitio. RCD es un control temporal: oculta un sitio de la búsqueda organizacional y de Copilot sin cambiar sus permisos.

Lo que viene: Microsoft anunció experiencias de preparación para Copilot y un explorador de datos dentro de DSPM, con preview en septiembre de 2026 y disponibilidad prevista para enero de 2027. También se anunciaron controles de sobreexposición en el centro de administración de Microsoft 365, todavía en desarrollo. Las etiquetas de contenedor se profundizan en el programa de Information Protection (módulo M3).

**Por qué importa**

SAM es el puente entre quien encuentra el problema (seguridad de datos) y quien lo corrige (los administradores de Microsoft 365 y SharePoint, con los propietarios de sitios). Sin ese puente, las evaluaciones de DSPM se acumulan sin remediar. Los indicadores son concretos: sitios compartidos con toda la organización, vínculos «Cualquier persona», sitios sin propietario, sitios inactivos y revisiones de acceso completadas.

**Qué vas a lograr**

- Identificar qué funciones de SAM se habilitan con licencias de Copilot y cuáles requieren SAM Plan 1.
- Usar los informes de gobierno de acceso y las revisiones del propietario para remediar sitios.
- Aplicar RCD o RAC de forma temporal, reversible y comunicada.
- Diseñar etiquetas de contenedor que prevengan la sobreexposición desde la creación del sitio.
- Distinguir los controles fundamentales (E3 + SAM) de los optimizados (E5).

> **Atención.** Al asignar al menos una licencia de Copilot se habilitan funciones de SAM: RAC, RCD, informes de gobierno de acceso, revisiones de acceso, sitios inactivos y propiedad. La creación restringida de sitios por apps requiere el complemento SAM Plan 1 ([SAM con licencias de Copilot](https://learn.microsoft.com/en-us/sharepoint/sharepoint-advanced-management-features-copilot-license)).

> **Consejo Ninja.** El marco de controles de Copilot separa lo fundamental (E3 + SAM) de lo optimizado (E5: DSPM, autoetiquetado, Insider Risk y Defender for Cloud Apps) ([controles de Copilot](https://learn.microsoft.com/en-us/copilot/implement/copilot-controls-security-governance)). Úsalo para explicar al comité qué se logra sin E5 y qué agrega E5.

> **Novedad.** Microsoft anunció experiencias de preparación para Copilot y un explorador de datos en DSPM: preview en septiembre de 2026 y disponibilidad prevista para enero de 2027 (Roadmap 571157), con fechas sujetas a cambio tras Ignite ([aviso](https://m365admin.handsontek.net/microsoft-purview-dspm-copilot-readiness-data-explorer/)). Un partner con presencia en la región resume en español qué corregir primero: grupos de toda la organización, vínculos «Cualquier persona», RCD y RAC, sitios sin propietario y archivos sin etiqueta ([Synergy Advisors](https://synergyadvisors.biz/es/sobreexposicion-copilot-centro-administracion-microsoft-365/)).

> **Consejo Ninja.** Las etiquetas de contenedor en Teams, grupos y sitios reducen la sobreexposición desde la creación del espacio de trabajo y complementan la remediación posterior ([etiquetas de contenedor contra la sobreexposición](https://nikkichapple.com/m365-copilot-oversharing-container-labels/)).

**¿Tienes poco tiempo?**

- [SharePoint Advanced Management features in Microsoft Copilot licenses](https://learn.microsoft.com/en-us/sharepoint/sharepoint-advanced-management-features-copilot-license) · Documentación
- [Restrict discovery of SharePoint sites and content (Restricted Content Discovery)](https://learn.microsoft.com/en-us/sharepoint/restricted-content-discovery) · Documentación
- [Copilot controls security and governance](https://learn.microsoft.com/en-us/copilot/implement/copilot-controls-security-governance) · Documentación

### Documentación, cursos y credenciales

- [Protect and remediate sensitive data in Microsoft Purview (module)](https://learn.microsoft.com/en-us/training/modules/purview-data-security-posture-management-protect-remediate/) · Curso · Oficial · Microsoft Learn. Módulo que enseña a elegir remediaciones desde objetivos de DSPM, aplicar políticas de un clic y evaluar y remediar la sobreexposición con evaluaciones de riesgo predeterminadas y personalizadas.
- [SharePoint Advanced Management features in Microsoft Copilot licenses](https://learn.microsoft.com/en-us/sharepoint/sharepoint-advanced-management-features-copilot-license) · Documentación · Oficial · Microsoft Learn. Tabla oficial de funciones de SharePoint Advanced Management incluidas al asignar al menos una licencia de Copilot: RAC, RCD, informes de gobierno de acceso, revisiones de acceso, políticas de sitios inactivos, propiedad y atestación.
- [Restrict discovery of SharePoint sites and content (Restricted Content Discovery)](https://learn.microsoft.com/en-us/sharepoint/restricted-content-discovery) · Documentación · Oficial · Microsoft Learn. Explica Restricted Content Discovery como control temporal que oculta sitios de SharePoint de la búsqueda organizacional y de Copilot sin cambiar permisos, y elimina puntos de entrada de IA en esos sitios.

### Comunidad: blogs, libros, newsletters y eventos

- [Container Sensitivity Labels: The Purview “Hack” That Fixes Copilot Oversharing Fast](https://nikkichapple.com/m365-copilot-oversharing-container-labels/) · Blog · Comunidad · Nuevo · Nikki Chapple · nikkichapple.com · 16 may 2026. Explica cómo las etiquetas de contenedor en Teams, Grupos y sitios reducen la sobreexposición desde la creación del espacio de trabajo, complemento de la remediación posterior.

**Manos a la obra**

1. `Laboratorio` Etiqueta de contenedor: crea una etiqueta para sitios con privacidad privada y uso compartido externo restringido, aplícala a un sitio nuevo y verifica que la configuración se hereda, esperando 24 horas tras publicarla ([etiquetas de contenedor contra la sobreexposición](https://nikkichapple.com/m365-copilot-oversharing-container-labels/)). Evidencia: captura de la configuración del sitio.
2. `Laboratorio parcial` Gobierno de acceso: genera un informe DAG de sitios con uso compartido amplio y lanza una revisión de acceso del propietario sobre un sitio de prueba ([SAM con licencias de Copilot](https://learn.microsoft.com/en-us/sharepoint/sharepoint-advanced-management-features-copilot-license)). Limitación: requiere SAM, que se habilita con al menos una licencia de Copilot (puedes comprarla en el sandbox). Evidencia: informe generado y revisión completada.
3. `Laboratorio parcial` Restricted Content Discovery: aplica RCD a un sitio de prueba y verifica con una cuenta de prueba que el sitio ya no aparece en la búsqueda organizacional ni en Copilot, aunque sus permisos no cambiaron ([RCD](https://learn.microsoft.com/en-us/sharepoint/restricted-content-discovery), [en español](https://learn.microsoft.com/es-es/sharepoint/restricted-content-discovery)). Limitación: requiere licencia de Copilot y no aplica a OneDrive. Evidencia: búsquedas antes y después.
4. `Laboratorio` Brechas frente al marco de controles: compara tu configuración con las capas fundamental (E3 + SAM) y optimizada (E5) del [marco de controles de Copilot](https://learn.microsoft.com/en-us/copilot/implement/copilot-controls-security-governance) y marca lo que falta. Evidencia: matriz de brechas con prioridad.
5. `Solo producción` RCD en producción: aplica RCD a un sitio piloto sobreexpuesto, verifica el efecto con una cuenta de prueba en la búsqueda y en Copilot y deja documentada la ventana de reversión. Cómo hacerlo seguro: aviso previo al propietario, retiro de RCD cuando se corrijan los permisos y registro del cambio. Evidencia: ticket con las fechas de aplicación y de retiro.
6. `Solo producción` Plan de 30 días con los propietarios: prioriza grupos de toda la organización, vínculos «Cualquier persona», sitios sin propietario y archivos sin etiqueta, y asigna cada acción a un propietario ([prioridades en español](https://synergyadvisors.biz/es/sobreexposicion-copilot-centro-administracion-microsoft-365/)). Cómo hacerlo seguro: oleadas semanales, comunicación a los usuarios afectados y reversión documentada. Evidencia: tablero semanal de avance.

**¿Quieres profundizar?**

- [Container Sensitivity Labels: The Purview “Hack” That Fixes Copilot Oversharing Fast](https://nikkichapple.com/m365-copilot-oversharing-container-labels/) · Blog

<a id="reto-intermedio"></a>

## Reto del nivel

**Copilot y agentes con barandas, en piloto.** Para un grupo piloto configura la DLP de prompts y la exclusión de contenido etiquetado (primero en simulación), la retención de las interacciones de IA, Communication Compliance y Risky AI usage con seudonimización, las políticas de un clic para sitios de IA en auditoría con una directiva de colección sin captura de contenido, RCD sobre un sitio sobrecompartido y Purview para un proyecto de Foundry. Entrega una matriz de evidencias (control, licencia requerida, modo, evidencia y responsable) y el consumo de pago por uso a los 7 días.

<a id="quiz-intermedio"></a>

## Evaluación del nivel

Responde y compara con [Evaluaciones y respuestas](06_Evaluaciones_y_respuestas.md#eval-intermedio). Con 80 % o más, ¡nivel aprobado! (En la versión web puedes corregir en línea y generar tu certificado).

1. ¿Quién puede beneficiarse de la DLP que bloquea prompts con tipos de información confidencial en Copilot?
   - a) Solo usuarios con Microsoft 365 E5
   - b) Todos los usuarios de Microsoft Copilot y Copilot Chat, incluidos E3 y Business
   - c) Solo organizaciones con pago por uso habilitado
   - d) Solo organizaciones con Agent 365

2. ¿Qué licenciamiento permite analizar prompts y respuestas de Copilot con Communication Compliance?
   - a) Microsoft 365 E3
   - b) Microsoft 365 E5 sola
   - c) Solo el pago por uso
   - d) Microsoft 365 E5 o Purview Suite más Microsoft Copilot

3. ¿En qué modo arranca la política DLP predeterminada «Protect sensitive M365 Copilot interactions»?
   - a) Simulación
   - b) Bloqueo
   - c) Desactivada
   - d) Bloqueo con invalidación

4. ¿Qué ubicaciones de retención usan hoy las interacciones de IA?
   - a) «Teams chats and Copilot interactions»
   - b) Exchange y OneDrive
   - c) Microsoft Copilot experiences, Enterprise AI apps y Other AI apps
   - d) SharePoint y Viva Engage

5. Con Microsoft 365 E3 más licencias de Copilot, ¿qué puedes hacer en eDiscovery con las interacciones de Copilot?
   - a) Nada: el eDiscovery de IA requiere E5
   - b) Solo la búsqueda Premium
   - c) Buscar, retener y exportar
   - d) Solo eliminarlas

6. ¿Qué suscripción se requiere para la AI observability de agentes y para Insider Risk Management para agentes?
   - a) Microsoft 365 E5
   - b) Microsoft Purview Suite
   - c) Copilot Studio
   - d) Microsoft 365 E7 o Agent 365

7. Al integrar Microsoft Foundry con Purview, ¿qué queda incluido en la licencia de Purview?
   - a) Las políticas DLP
   - b) La auditoría de Foundry
   - c) La postura de agentes de Foundry
   - d) Las políticas de Insider Risk

8. Si un archivo tiene una etiqueta que cifra, ¿qué derechos de uso necesita un agente para devolver su contenido?
   - a) VIEW y EXTRACT
   - b) Solo VIEW
   - c) EDIT y PRINT
   - d) Solo OWNER

9. ¿Qué requisito previo exige Purview para gestionar interacciones con ChatGPT (consumo), Gemini o DeepSeek?
   - a) Ninguno
   - b) Licencia de Agent 365
   - c) Pago por uso habilitado
   - d) Licencia de Microsoft 365 Copilot

10. ¿Qué licencia exige Network Data Security con Global Secure Access?
   - a) Microsoft 365 E3
   - b) Microsoft 365 E7 o Purview E5 + Entra Internet Access
   - c) Solo Defender for Cloud Apps
   - d) Solo Agent 365

11. ¿Cómo se licencia la DLP de Edge for Business para proteger datos de un dispositivo administrado hacia una app de IA no administrada?
   - a) Incluida en E3
   - b) Pago por uso
   - c) Incluida en Microsoft 365 Copilot
   - d) Requiere Agent 365

12. ¿Qué afirmación sobre las etiquetas de confidencialidad con la IA de terceros es correcta?
   - a) Se admiten en todos los sitios de IA
   - b) Solo se admiten en Edge
   - c) Solo se admiten con la extensión de Chrome
   - d) No se admiten

13. ¿Qué habilita asignar al menos una licencia de Copilot en SharePoint Advanced Management?
   - a) Todas las funciones de SAM, incluida la creación restringida de sitios por apps
   - b) Solo Restricted Content Discovery
   - c) RAC, RCD, informes de gobierno de acceso, revisiones de acceso, sitios inactivos y propiedad
   - d) Nada: SAM siempre requiere un complemento

14. Según el marco de controles de Copilot, ¿qué distingue la capa fundamental de la optimizada?
   - a) Fundamental: E3 + SAM; optimizada: E5 (DSPM, autoetiquetado, Insider Risk y Defender for Cloud Apps)
   - b) Fundamental: E5; optimizada: E3
   - c) Ambas requieren Microsoft 365 E7
   - d) Fundamental: Agent 365; optimizada: Purview Suite

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. No constituye asesoría legal ni laboral: las decisiones sobre privacidad, captura de contenido, monitoreo y normativa corresponden a tus áreas de Legal, RR. HH. y privacidad. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

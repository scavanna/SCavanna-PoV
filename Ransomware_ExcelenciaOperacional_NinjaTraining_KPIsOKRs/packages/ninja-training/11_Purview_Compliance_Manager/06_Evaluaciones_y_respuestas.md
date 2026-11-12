# Evaluaciones y respuestas

*Microsoft Purview Compliance Manager Ninja Training · Edición 2026*

[← Comunidad](05_Comunidad.md) · [Índice del programa](README.md) · [Laboratorio y práctica en producción →](07_Laboratorio_y_practica_en_produccion.md)

<a id="respuestas"></a>

Cada evaluación tiene preguntas de opción múltiple. Con 80 % o más el nivel se considera aprobado. Es una autoevaluación de esta guía, no una certificación de Microsoft.

<a id="eval-inicial"></a>

## Nivel 1 · Inicial · Fundamentos

**1. ¿Qué plantillas puede usar sin costo adicional una organización con Microsoft 365 E5?**

- a) Todas las plantillas premium de la biblioteca
- b) Solo ISO 27001, NIST 800-53 y GDPR
- c) La Data Protection Baseline y hasta tres plantillas premium a elección  ✅
- d) Ninguna: todas requieren compra

*Respuesta: c).* E5, A5 y G5 incluyen la Data Protection Baseline y tres regulaciones premium a elección; el resto se compra por plantilla. Las afirmaciones de «300+ plantillas incluidas» contradicen Learn. [Fuente](https://learn.microsoft.com/en-us/purview/compliance-manager-regulations-list) · Repasa [I1](01_Nivel_1_Inicial.md#i1)

**2. ¿Qué ofrece la prueba de evaluaciones premium?**

- a) 10 plantillas durante 30 días, renovable
- b) 25 plantillas premium durante 90 días, una sola vez por inquilino  ✅
- c) Plantillas ilimitadas durante un año
- d) Solo las plantillas de IA durante 60 días

*Respuesta: b).* La prueba es única: 25 plantillas premium durante 90 días. Al terminar, las plantillas usadas dejan de recibir actualizaciones. [Fuente](https://learn.microsoft.com/en-us/purview/purview-compliance-manager-assessments-trial) · Repasa [I2](01_Nivel_1_Inicial.md#i2)

**3. Una organización con E5 usa CMMC niveles 1 y 2. ¿Cuántos cupos premium consume?**

- a) Uno, porque las plantillas de una misma familia cuentan como una  ✅
- b) Dos, uno por nivel
- c) Ninguno, porque CMMC está incluido para todos
- d) Cinco, uno por cada nivel de la familia

*Respuesta: a).* Desde el cambio de licencias de diciembre de 2022, las plantillas de una misma familia cuentan como una sola. [Fuente](https://learn.microsoft.com/en-us/purview/compliance-manager-faq) · Repasa [I1](01_Nivel_1_Inicial.md#i1)

**4. ¿Qué mide la puntuación de cumplimiento de Compliance Manager?**

- a) El cumplimiento legal certificado de la organización
- b) La postura de seguridad comparada con organizaciones similares
- c) La cantidad de alertas de DLP resueltas
- d) El avance en acciones de mejora, con puntos ponderados por tipo de acción  ✅

*Respuesta: d).* Mide el avance en acciones de mejora con puntos según sean preventivas, detectivas o correctivas, y obligatorias o discrecionales; no garantiza cumplimiento. La comparación con organizaciones similares es propia de Secure Score. [Fuente](https://learn.microsoft.com/en-us/purview/compliance-manager-scoring) · Repasa [I1](01_Nivel_1_Inicial.md#i1)

**5. ¿Por qué la puntuación global puede diferir del promedio de tus evaluaciones?**

- a) Porque Microsoft redondea cada regulación
- b) Porque las acciones técnicas cuentan una vez por inquilino y las no técnicas una vez por grupo  ✅
- c) Porque las evaluaciones premium pesan el doble
- d) Porque solo cuenta la última evaluación creada

*Respuesta: b).* Las acciones técnicas se cuentan una vez por inquilino y las no técnicas una vez por grupo, así que el total no es el promedio de las evaluaciones. [Fuente](https://learn.microsoft.com/en-us/purview/compliance-manager-scoring) · Repasa [I1](01_Nivel_1_Inicial.md#i1)

**6. ¿Qué tipo de acción de mejora otorga más puntos?**

- a) Detectiva obligatoria
- b) Correctiva obligatoria
- c) Preventiva obligatoria  ✅
- d) Preventiva discrecional

*Respuesta: c).* Preventiva obligatoria vale 27 puntos; preventiva discrecional, 9; detectivas y correctivas obligatorias, 3; y las discrecionales de esos tipos, 1. [Fuente](https://learn.microsoft.com/en-us/purview/compliance-manager-scoring) · Repasa [I1](01_Nivel_1_Inicial.md#i1)

**7. ¿Qué país de MCSA tiene plantilla en Compliance Manager para su ley general de datos personales?**

- a) Chile
- b) Uruguay
- c) Panamá
- d) Perú  ✅

*Respuesta: d).* La lista de regulaciones incluye la Ley 29733 de Perú; Chile, Uruguay y Panamá no tienen plantilla y requieren una plantilla propia. [Fuente](https://learn.microsoft.com/en-us/purview/compliance-manager-regulations-list) · Repasa [I2](01_Nivel_1_Inicial.md#i2)

**8. ¿Qué problema tiene hoy la plantilla de México sobre datos personales?**

- a) Corresponde a la ley de 2010, reemplazada por la nueva LFPDPPP publicada el 20 de marzo de 2025  ✅
- b) Solo está disponible para nubes de gobierno
- c) No existe: México no tiene plantilla
- d) Cubre solo al sector público

*Respuesta: a).* Compliance Manager mantiene la plantilla de la ley de 2010; la nueva ley se publicó el 20 de marzo de 2025 y la lista de regulaciones no se actualiza desde el 6 de marzo de 2025. [Fuente](https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPDPPP.pdf) · Repasa [I2](01_Nivel_1_Inicial.md#i2)

**9. ¿A qué acciones aplica la actualización masiva desde Excel?**

- a) A todas, incluidas las gestionadas por Microsoft
- b) Solo a las acciones gestionadas por tu organización que ya están asociadas a una evaluación  ✅
- c) Solo a las acciones probadas por Defender for Cloud
- d) A las acciones de cualquier inquilino del mismo contrato

*Respuesta: b).* La carga masiva solo aplica a acciones gestionadas por la organización y ya asociadas a una evaluación; el mapeo de controles exportado no se puede modificar. [Fuente](https://learn.microsoft.com/en-us/purview/compliance-manager-update-actions) · Repasa [I3](01_Nivel_1_Inicial.md#i3)

**10. No estás de acuerdo con el resultado de una acción probada por Defender for Cloud. ¿Qué haces?**

- a) La cambias a prueba manual en Compliance Manager
- b) Borras la acción y la vuelves a crear
- c) Ajustas la configuración o la evaluación en Defender for Cloud  ✅
- d) Pides a Microsoft que cambie la puntuación

*Respuesta: c).* Las acciones evaluadas por Defender for Cloud no pueden pasar a prueba manual; el ajuste se hace en Defender for Cloud. [Fuente](https://learn.microsoft.com/en-us/purview/compliance-manager-improvement-actions) · Repasa [I3](01_Nivel_1_Inicial.md#i3)

**11. Marcas como implementada una acción técnica en una evaluación del grupo A. ¿Qué ocurre?**

- a) Solo cambia en la evaluación donde la marcaste
- b) Cambia en las evaluaciones del grupo A, pero no en las de otros grupos
- c) No cambia nada hasta que auditoría interna la pruebe
- d) Impacta todas las evaluaciones de todos los grupos  ✅

*Respuesta: d).* Las acciones técnicas actualizadas impactan todas las evaluaciones de todos los grupos; las no técnicas, solo las de su grupo. [Fuente](https://learn.microsoft.com/en-us/purview/compliance-manager-assessments) · Repasa [I3](01_Nivel_1_Inicial.md#i3)

**12. ¿Para qué sirve el Service Trust Portal en un programa de cumplimiento?**

- a) Para descargar informes de auditoría de Microsoft que evidencian los controles que gestiona Microsoft  ✅
- b) Para crear evaluaciones de Compliance Manager
- c) Para comprar plantillas premium
- d) Para configurar conectores de AWS y GCP

*Respuesta: a).* Con una cuenta de Entra ID y aceptando los términos de confidencialidad descargas informes ISO, SOC, PCI y otros: la evidencia de la parte que gestiona Microsoft. [Fuente](https://learn.microsoft.com/en-ie/purview/get-started-with-service-trust-portal?view=o365-worldwide) · Repasa [P0](01_Nivel_1_Inicial.md#p0)

**13. ¿Qué credencial vigente evalúa Compliance Manager de forma explícita?**

- a) SC-400
- b) SC-401
- c) SC-900  ✅
- d) MS-101

*Respuesta: c).* La guía de SC-900 (habilidades al 21 de octubre de 2026) incluye describir Compliance Manager y la puntuación; SC-401 no tiene objetivos explícitos y SC-400 se retiró el 31 de mayo de 2025. [Fuente](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-900) · Repasa [I0](01_Nivel_1_Inicial.md#i0)

**14. ¿Cuándo se retiró el portal de cumplimiento clásico?**

- a) En julio de 2024, el mismo día de la disponibilidad general del nuevo portal
- b) Entre el 14 de noviembre y el 14 de diciembre de 2024  ✅
- c) El 1 de octubre de 2025
- d) Sigue disponible hasta 2027

*Respuesta: b).* El nuevo portal de Purview llegó a disponibilidad general en julio de 2024 (MC807798) y el clásico se retiró entre el 14 de noviembre y el 14 de diciembre de 2024 (MC939918). [Fuente](https://mc.merill.net/message/MC939918) · Repasa [P0](01_Nivel_1_Inicial.md#p0)

<a id="eval-intermedio"></a>

## Nivel 2 · Intermedio · Plantillas propias, multinube, IA y dirección

**1. ¿Qué hacen las plantillas regulatorias con IA anunciadas en MC1192260?**

- a) Traducen la interfaz de Compliance Manager al español
- b) Calculan las multas regulatorias aplicables
- c) Crean políticas de DLP automáticamente
- d) Convierten el PDF de una regulación en una plantilla con controles accionables  ✅

*Respuesta: d).* Convierten documentos regulatorios en PDF en plantillas con controles; vista previa desde mediados de noviembre de 2025 y disponibilidad general mundial en octubre de 2026. [Fuente](https://mc.merill.net/message/MC1192260) · Repasa [M1](02_Nivel_2_Intermedio.md#m1)

**2. ¿Qué requisitos tiene crear una plantilla a partir de un PDF?**

- a) Un PDF publicado por un regulador u organismo de normas y el rol Compliance Manager Administration o Assessor  ✅
- b) Cualquier documento de Word con controles numerados
- c) Una licencia de Microsoft 365 Copilot
- d) El rol Compliance Manager Reader y la aprobación de Microsoft

*Respuesta: a).* La página de creación de plantillas exige un PDF oficial de un regulador u organismo de normas y el rol Administration o Assessor. [Fuente](https://learn.microsoft.com/en-us/purview/compliance-manager-create-template) · Repasa [M1](02_Nivel_2_Intermedio.md#m1)

**3. ¿Qué ocurre al copiar una plantilla premium para personalizarla?**

- a) Nada: las copias nunca consumen licencias
- b) Se activa la regulación y se consume su licencia  ✅
- c) Se convierte automáticamente en una plantilla incluida
- d) Se elimina la plantilla original

*Respuesta: b).* Copiar una regulación premium la activa y consume su licencia; esa licencia permite varias copias y evaluaciones. [Fuente](https://learn.microsoft.com/en-us/purview/compliance-manager-assessments-custom) · Repasa [M1](02_Nivel_2_Intermedio.md#m1)

**4. ¿En qué estado están las evaluaciones personalizadas (copiar y extender una regulación) en noviembre de 2026?**

- a) En disponibilidad general desde 2022
- b) Retiradas en 2025
- c) Siguen documentadas como vista previa  ✅
- d) Disponibles solo en GCC High

*Respuesta: c).* La página de evaluaciones personalizadas sigue marcada como vista previa; la creación desde PDF, en cambio, llegó a disponibilidad general en octubre de 2026. [Fuente](https://learn.microsoft.com/en-us/purview/compliance-manager-assessments-custom) · Repasa [M1](02_Nivel_2_Intermedio.md#m1)

**5. ¿De dónde obtiene Compliance Manager el progreso de las suscripciones de Azure, AWS y GCP?**

- a) De Microsoft Sentinel
- b) De Microsoft Defender for Cloud  ✅
- c) De Azure Monitor directamente
- d) De conectores de Power Automate

*Respuesta: b).* El progreso por servicio y por suscripción proviene de Defender for Cloud, donde también se corrigen los errores de acceso. [Fuente](https://learn.microsoft.com/en-us/purview/compliance-manager-assessments) · Repasa [M2](02_Nivel_2_Intermedio.md#m2)

**6. Quieres evaluar ISO 27001 en Azure con resultados a nivel de recurso. ¿Qué necesitas en Defender for Cloud?**

- a) Nada: Foundational CSPM incluye todos los estándares
- b) Solo el plan Servers P1
- c) Una licencia premium de Compliance Manager para Azure
- d) Asignar el estándar con al menos un plan pago distinto de Servers P1 o API P1  ✅

*Respuesta: d).* Los estándares no predeterminados requieren un plan pago de Defender for Cloud distinto de Servers P1 o API P1 y permisos Owner o Policy Contributor; las evaluaciones corren aproximadamente cada 12 horas. [Fuente](https://learn.microsoft.com/en-us/azure/defender-for-cloud/assign-regulatory-compliance-standards) · Repasa [M2](02_Nivel_2_Intermedio.md#m2)

**7. ¿Qué son los conectores de Compliance Manager?**

- a) Conectores propios para incluir servicios como Salesforce y Zoom en las evaluaciones, distintos de los conectores de datos de Purview  ✅
- b) Los mismos conectores de datos que usa Insider Risk
- c) Conectores de Defender for Cloud para AWS
- d) Integraciones de Power BI para reportes

*Respuesta: a).* Son conectores propios (Corporate Sustainability, Salesforce y Zoom); requieren Data Connector Admin o Global Admin y un conector por instancia. [Fuente](https://learn.microsoft.com/en-us/purview/compliance-manager-connectors) · Repasa [M2](02_Nivel_2_Intermedio.md#m2)

**8. Necesitas evaluar un servicio no Microsoft que no tiene conector. ¿Qué haces?**

- a) No es posible evaluarlo
- b) Lo agregas como nuevo servicio y se usa la versión universal de la plantilla, con implementación y pruebas manuales  ✅
- c) Pides a Microsoft que cree un conector
- d) Lo conectas a Defender for Cloud como si fuera AWS

*Respuesta: b).* Al agregar un servicio no listado se usa la versión universal de la regulación y tu equipo implementa y prueba de forma manual. [Fuente](https://learn.microsoft.com/en-us/purview/compliance-manager-multicloud) · Repasa [M2](02_Nivel_2_Intermedio.md#m2)

**9. ¿Cuál de estas NO es una de las cuatro plantillas premium de IA?**

- a) EU AI Act
- b) ISO/IEC 42001:2023
- c) NIST AI RMF 1.0
- d) ISO/IEC 27701:2019  ✅

*Respuesta: d).* Las plantillas premium de IA son EU AI Act, ISO/IEC 23894:2023, ISO/IEC 42001:2023 y NIST AI RMF 1.0. [Fuente](https://learn.microsoft.com/en-us/purview/compliance-manager-assessments) · Repasa [M3](02_Nivel_2_Intermedio.md#m3)

**10. ¿Qué ocurre al comprar Microsoft 365 Copilot o Copilot Chat?**

- a) Se habilitan gratis todas las plantillas premium
- b) Se crea una evaluación EU AI Act obligatoria
- c) Se aprovisiona automáticamente una evaluación base para Microsoft 365 Copilot y Copilot Chat  ✅
- d) Se desactiva la Data Protection Baseline

*Respuesta: c).* La evaluación base de Microsoft 365 Copilot y Copilot Chat se aprovisiona sola y es visible en el centro de administración de Microsoft 365. [Fuente](https://learn.microsoft.com/en-us/purview/compliance-manager-assessments) · Repasa [M3](02_Nivel_2_Intermedio.md#m3)

**11. ¿Qué rol de Azure requieren las evaluaciones automáticas de agentes de Microsoft Foundry en Compliance Manager?**

- a) Azure AI Project Manager o Azure AI User  ✅
- b) Owner de la suscripción
- c) Security Reader de Entra ID
- d) Policy Contributor

*Respuesta: a).* La integración con Foundry requiere el rol Azure AI Project Manager o Azure AI User. [Fuente](https://learn.microsoft.com/en-us/purview/compliance-manager-assessments) · Repasa [M3](02_Nivel_2_Intermedio.md#m3)

**12. Al exportar el informe de una evaluación, ¿qué obtienes?**

- a) Un PDF firmado por Microsoft
- b) Un enlace público para el auditor
- c) Una instantánea en Excel con controles de Microsoft y tuyos, estado, fecha y resultado de pruebas  ✅
- d) Un certificado ISO

*Respuesta: c).* El informe es una instantánea fechada en Excel; conviene exportarlo antes de borrar una evaluación o aceptar una actualización. [Fuente](https://learn.microsoft.com/en-us/purview/compliance-manager-assessments) · Repasa [M4](02_Nivel_2_Intermedio.md#m4)

**13. ¿Qué características tienen los informes de postura de Purview?**

- a) Están en vista previa, usan una ventana móvil de 30 días y se guardan en PDF  ✅
- b) Están en disponibilidad general y muestran tres años de historia
- c) Reemplazan a la puntuación de cumplimiento
- d) Solo están disponibles en GCC High

*Respuesta: a).* Los informes de postura de Information Protection, DLP y personalizados están en vista previa, usan 30 días de datos y se guardan en PDF. [Fuente](https://learn.microsoft.com/en-us/purview/purview-reports) · Repasa [M4](02_Nivel_2_Intermedio.md#m4)

**14. Al reportar la puntuación de cumplimiento a la dirección, ¿qué conviene anotar siempre?**

- a) El precio de cada plantilla
- b) La fecha de corte y las actualizaciones de plantillas aceptadas  ✅
- c) La contraseña del administrador
- d) El Secure Score sumado a la puntuación

*Respuesta: b).* Aceptar una actualización de plantilla cambia la puntuación: anotar fecha y actualizaciones aceptadas hace comparable el indicador. Secure Score se reporta por separado. [Fuente](https://informasjonsbeskyttelse.no/en/how-purview-supports-an-isms) · Repasa [M4](02_Nivel_2_Intermedio.md#m4)

<a id="eval-avanzado"></a>

## Nivel 3 · Avanzado · Automatizar, mapear y sostener

**1. ¿Qué afirma la documentación sobre extraer datos de Purview mediante APIs?**

- a) Hay un endpoint de Graph para la puntuación de cumplimiento
- b) Solo existe un cmdlet de PowerShell para exportar evaluaciones
- c) No hay APIs para extraer datos ni analíticas de Purview  ✅
- d) Se usa la API de Secure Score para Compliance Manager

*Respuesta: c).* Las APIs de Purview sirven para enviar contenido y aplicar políticas en aplicaciones, no para extraer analíticas. [Fuente](https://learn.microsoft.com/en-us/purview/developer/use-the-api) · Repasa [A1](03_Nivel_3_Avanzado.md#a1)

**2. ¿Para qué sirven las APIs de Purview en Microsoft Graph, como protectionScopes y processContent?**

- a) Para que tus aplicaciones envíen contenido a Purview y apliquen sus políticas  ✅
- b) Para leer la puntuación de cumplimiento
- c) Para crear plantillas regulatorias
- d) Para descargar informes del Service Trust Portal

*Respuesta: a).* Integran las políticas de Purview en aplicaciones propias; no incluyen endpoints de Compliance Manager. [Fuente](https://learn.microsoft.com/en-us/purview/developer/microsoft-purview-sdk-documentation-overview) · Repasa [A1](03_Nivel_3_Avanzado.md#a1)

**3. ¿Adónde puede exportar Defender for Cloud de forma continua los datos de cumplimiento normativo?**

- a) Solo a un archivo de Excel mensual
- b) A Compliance Manager por API
- c) A una biblioteca de SharePoint
- d) A Log Analytics o Event Hubs, en streaming o con instantáneas semanales  ✅

*Respuesta: d).* La exportación continua envía cumplimiento normativo, secure score y recomendaciones a Log Analytics o Event Hubs. [Fuente](https://learn.microsoft.com/en-us/azure/defender-for-cloud/benefits-of-continuous-export) · Repasa [A1](03_Nivel_3_Avanzado.md#a1)

**4. ¿Qué permite que una acción técnica satisfaga varias regulaciones a la vez?**

- a) Que las acciones de mejora se comparten entre las evaluaciones del mismo grupo  ✅
- b) Que Microsoft fusiona las regulaciones similares
- c) Que cada evaluación copia sus acciones
- d) Que la puntuación se promedia entre evaluaciones

*Respuesta: a).* Las acciones se comparten entre las evaluaciones del grupo: implementar una acción técnica cubre requisitos de varias regulaciones. [Fuente](https://learn.microsoft.com/en-us/purview/compliance-manager-assessments) · Repasa [A2](03_Nivel_3_Avanzado.md#a2)

**5. ¿Qué ofrece la preparación previa al despliegue (Sub-service compliance readiness)?**

- a) Evaluaciones premium gratis
- b) El aporte de un servicio de Azure a ISO 27001, NIST 800-53, PCI DSS y SOC 2, con controles relacionados entre marcos y sin consumir licencias  ✅
- c) El despliegue de servicios de Azure ya configurados
- d) La certificación de servicios ante el supervisor

*Respuesta: b).* Está en vista previa, no consume licencias ni crea evaluaciones, muestra controles relacionados entre regulaciones y exporta en CSV o JSON. [Fuente](https://learn.microsoft.com/en-us/purview/compliance-manager-predeployment-compliance) · Repasa [A2](03_Nivel_3_Avanzado.md#a2)

**6. Asignaste una evaluación al grupo equivocado. ¿Qué dice la documentación?**

- a) Puedes moverla de grupo en cualquier momento
- b) Microsoft la reasigna en 24 horas
- c) Los grupos no se pueden cambiar una vez asignados  ✅
- d) Se mueve sola al aceptar una actualización

*Respuesta: c).* Una vez asignado, el grupo de una evaluación no se puede cambiar: planifica los grupos antes de mapear. [Fuente](https://learn.microsoft.com/en-us/purview/compliance-manager-assessments) · Repasa [A2](03_Nivel_3_Avanzado.md#a2)

**7. ¿Qué implica aceptar una actualización pendiente (Pending update) de una plantilla?**

- a) Es reversible durante 30 días
- b) Es permanente y se aplica por grupo; conviene diferirla si hay una auditoría en curso  ✅
- c) Solo afecta a la evaluación abierta
- d) Requiere la aprobación de Microsoft

*Respuesta: b).* La aceptación es permanente y se aplica por grupo; exporta el informe antes y difiérela durante las auditorías. [Fuente](https://learn.microsoft.com/en-us/purview/compliance-manager-assessments) · Repasa [A3](03_Nivel_3_Avanzado.md#a3)

**8. ¿Cómo funciona la política de alertas predeterminada de cambio de puntuación?**

- a) Envía una alerta por cada cambio, sin agrupar
- b) No existe: hay que crearla
- c) Solo alerta al auditor interno
- d) Agrupa las coincidencias de 60 minutos en una alerta de severidad media, enviada por defecto al Global Admin  ✅

*Respuesta: d).* Todas las organizaciones la tienen: agrupa coincidencias de 60 minutos, tiene severidad media y notifica al Global Admin; puedes agregar destinatarios y desactivarla, pero no eliminarla. [Fuente](https://learn.microsoft.com/en-us/purview/compliance-manager-alert-policies) · Repasa [A3](03_Nivel_3_Avanzado.md#a3)

**9. ¿Qué rol de Entra ID se necesita para ver las páginas Policies y Alerts de Compliance Manager?**

- a) Global Administrator
- b) Security reader  ✅
- c) Ninguno: basta con Compliance Manager Reader
- d) Billing Administrator

*Respuesta: b).* Ver alertas y políticas requiere Security reader en Entra ID; crearlas, Compliance Administrator, Compliance Data Administrator, Security Administrator o Security Operator. [Fuente](https://learn.microsoft.com/en-us/purview/compliance-manager-alert-policies) · Repasa [A3](03_Nivel_3_Avanzado.md#a3)

**10. Según el Decreto 295 de Chile, ¿en qué plazo se envía la alerta temprana de un incidente?**

- a) 1 hora
- b) 3 horas  ✅
- c) 24 horas
- d) 72 horas

*Respuesta: b).* La alerta temprana se envía en un máximo de tres horas; el segundo reporte, en 72 horas (24 horas para operadores de importancia vital con un servicio esencial afectado). [Fuente](https://www.leychile.cl/leychile/Navegar/imprimir?idNorma=1211466) · Repasa [A4](03_Nivel_3_Avanzado.md#a4)

**11. Según la Comunicación BCRA «A» 8280, ¿cuándo se envía la notificación inicial de un ciberincidente importante?**

- a) Dentro de la primera hora  ✅
- b) En 24 horas
- c) En 72 horas
- d) En 5 días corridos

*Respuesta: a).* La notificación inicial va dentro de la primera hora; el reporte de cierre, en un máximo de cinco días corridos. [Fuente](https://www.bcra.gob.ar/archivos/Pdfs/comytexord/A8280.pdf) · Repasa [A4](03_Nivel_3_Avanzado.md#a4)

**12. ¿Qué dice la Ley 21.719 de Chile sobre el plazo para reportar vulneraciones a la Agencia?**

- a) 72 horas, como el RGPD
- b) 24 horas hábiles
- c) Sin dilaciones indebidas y por el medio más expedito; la ley no fija horas  ✅
- d) Cinco días hábiles

*Respuesta: c).* El art. 14 sexies exige reportar sin dilaciones indebidas y no fija horas; la cifra de 72 horas que cita una firma no aparece en el texto oficial. [Fuente](https://www.leychile.cl/leychile/Navegar?idNorma=1209272&idParte=1) · Repasa [A4](03_Nivel_3_Avanzado.md#a4)

**13. ¿Qué grupo de países no tenía ley general de datos personales a noviembre de 2026?**

- a) Guatemala, Honduras, Venezuela y Bolivia  ✅
- b) Chile, Perú, Colombia y Uruguay
- c) México, Panamá, Costa Rica y Paraguay
- d) Argentina, Ecuador, El Salvador y Nicaragua

*Respuesta: a).* Guatemala, Honduras, Venezuela y Bolivia tienen iniciativas o anteproyectos, pero no una ley general vigente; Guatemala presentó una iniciativa en 2025. [Fuente](https://www.congreso.gob.gt/noticias_congreso/13884/2025/) · Repasa [A4](03_Nivel_3_Avanzado.md#a4)

**14. ¿Qué plazo fija el Decreto 64/020 de Uruguay para comunicar vulneraciones a la URCDP?**

- a) 24 horas
- b) 48 horas
- c) 15 días hábiles
- d) 72 horas desde que se conoce la vulneración  ✅

*Respuesta: d).* El art. 4 del Decreto 64/020 fija 72 horas y exige comunicar a los titulares cuando la afectación es significativa. [Fuente](https://www.impo.com.uy/bases/decretos/64-2020/4) · Repasa [A4](03_Nivel_3_Avanzado.md#a4)

<a id="eval-operacion"></a>

## Nivel 4 · Operación · Modelo operativo, métricas y gobierno

**1. Un auditor externo debe revisar solo la evaluación ISO 27001 durante dos semanas. ¿Qué configuración es la más adecuada?**

- a) Global Administrator temporal
- b) Compliance Manager Administration sin restricciones
- c) Compliance Manager Reader con acceso restringido a esa evaluación y asignación con fecha de expiración  ✅
- d) Una cuenta de servicio compartida

*Respuesta: c).* El acceso se puede restringir por evaluación o regulación y, desde julio de 2026, las asignaciones de grupos de roles de Purview admiten expiración. [Fuente](https://learn.microsoft.com/en-us/purview/compliance-manager-setup) · Repasa [O1](04_Nivel_4_Operacion.md#o1)

**2. ¿Cuántos roles de Compliance Manager puede tener un usuario a la vez?**

- a) Uno  ✅
- b) Dos, si uno es Reader
- c) Todos los que necesite
- d) Ninguno: se usan solo roles de Entra ID

*Respuesta: a).* Un usuario solo puede tener un rol de Compliance Manager a la vez; por eso la segregación se diseña con personas y grupos distintos. [Fuente](https://learn.microsoft.com/en-us/purview/compliance-manager-setup) · Repasa [O1](04_Nivel_4_Operacion.md#o1)

**3. ¿Qué rango admite la fecha de expiración de las asignaciones de grupos de roles de Purview introducida en julio de 2026?**

- a) Entre una hora y 30 días
- b) Entre un día y dos años  ✅
- c) Solo 90 días fijos
- d) No tiene límite máximo

*Respuesta: b).* Las asignaciones pueden expirar entre un día y dos años, útil para auditores externos temporales. [Fuente](https://learn.microsoft.com/en-us/purview/whats-new) · Repasa [O1](04_Nivel_4_Operacion.md#o1)

**4. ¿Qué rol de Compliance Manager no puede crear ni editar políticas de alertas?**

- a) Administration
- b) Assessor
- c) Contributor
- d) Reader  ✅

*Respuesta: d).* Administration, Assessor y Contributor pueden crear y editar políticas y alertas; Reader no. [Fuente](https://learn.microsoft.com/en-us/purview/compliance-manager-alert-policies) · Repasa [O1](04_Nivel_4_Operacion.md#o1)

**5. ¿Cuál es la relación correcta entre Secure Score y la puntuación de cumplimiento?**

- a) Son la misma métrica con distinto nombre
- b) Secure Score mide postura de seguridad y la puntuación de cumplimiento, avance en acciones de cumplimiento: se reportan por separado  ✅
- c) La puntuación de cumplimiento es el promedio de Secure Score
- d) Secure Score solo aplica a Azure

*Respuesta: b).* Secure Score asigna hasta 10 puntos por acción y compara con organizaciones similares; la puntuación de cumplimiento mide otra cosa. [Fuente](https://learn.microsoft.com/en-us/defender-xdr/microsoft-secure-score) · Repasa [O2](04_Nivel_4_Operacion.md#o2)

**6. ¿Qué indicador es más defendible ante auditoría interna?**

- a) La puntuación global sin fecha
- b) La cantidad de evaluaciones creadas
- c) El porcentaje de acciones propias implementadas y probadas con evidencia aceptada  ✅
- d) El número de plantillas premium compradas

*Respuesta: c).* Mide trabajo real verificado. Si no hay evidencia razonable, el control no se marca como cumplido, como exige el BCU en sus autoevaluaciones. [Fuente](https://www.bcu.gub.uy/Comunicados/Anexo%201%20-%20Nota%20metodologica%20V2.pdf) · Repasa [O2](04_Nivel_4_Operacion.md#o2)

**7. ¿Qué cláusula de ISO/IEC 27001 puede apoyar Compliance Manager al medir el sistema de gestión?**

- a) 9.1 (seguimiento, medición, análisis y evaluación)  ✅
- b) 4.1 (contexto de la organización)
- c) 7.5 (información documentada)
- d) 10.2 (no conformidad y acción correctiva)

*Respuesta: a).* Un análisis comunitario del SGSI ubica a Compliance Manager como soporte de la cláusula 9.1 y del control 5.36. [Fuente](https://informasjonsbeskyttelse.no/en/how-purview-supports-an-isms) · Repasa [O2](04_Nivel_4_Operacion.md#o2)

**8. ¿Desde cuándo rige la Ley 21.719 de protección de datos de Chile?**

- a) Desde su publicación en diciembre de 2024
- b) Desde el 1 de marzo de 2025
- c) Desde el 1 de diciembre de 2026  ✅
- d) Desde enero de 2028

*Respuesta: c).* La ley se publicó en diciembre de 2024 y entra en vigencia el 1 de diciembre de 2026; el 1 de marzo de 2025 es la fecha del reporte obligatorio a la ANCI. [Fuente](https://www.bcn.cl/leychile/navegar?i=1209272&f=2026-12-01) · Repasa [O3](04_Nivel_4_Operacion.md#o3)

**9. ¿En qué estado está la Ley Marco de Ciberseguridad de Guatemala al 6 de noviembre de 2026?**

- a) Vigente desde 2024
- b) Rechazada por el Congreso
- c) Reemplazada por una norma del supervisor bancario
- d) Aprobada el 3 de noviembre de 2026 y pendiente de publicación; regiría 30 días después de publicarse  ✅

*Respuesta: d).* El Congreso la aprobó el 3 de noviembre de 2026 (Decreto 26-2026); entraría en vigor 30 días después de su publicación en el Diario Oficial. [Fuente](https://dca.gob.gt/noticias-guatemala-diario-centro-america/nueva-ley-blinda-el-ciberespacio-de-guatemala/) · Repasa [O3](04_Nivel_4_Operacion.md#o3)

**10. Según el concepto de la SIC de Colombia, ¿en qué plazo se reportan los incidentes de seguridad de datos personales?**

- a) 15 días hábiles desde la detección  ✅
- b) 72 horas
- c) De inmediato
- d) 30 días corridos

*Respuesta: a).* La SIC fija 15 días hábiles desde la detección, mediante el RNBD o su aplicativo. [Fuente](https://sedeelectronica.sic.gov.co/publicaciones/boletin-juridico/concepto/cumplimiento-de-la-obligacion-del-reporte-de-incidentes-de-seguridad) · Repasa [O3](04_Nivel_4_Operacion.md#o3)

**11. ¿Cuándo se prevé la plena vigencia de la Ley 7593/2025 de Paraguay?**

- a) De inmediato, desde su promulgación
- b) A fines de noviembre de 2027, tras 24 meses de adecuación  ✅
- c) En marzo de 2026
- d) Cuando Microsoft publique una plantilla

*Respuesta: b).* La ley se promulgó y publicó el 27 de noviembre de 2025 con 24 meses de adecuación. [Fuente](https://www.bacn.gov.py/leyes-paraguayas/12924/ley-n-75932025--de-proteccin-de-datos-personales-en-la-repblica-del-paraguay) · Repasa [O3](04_Nivel_4_Operacion.md#o3)

**12. En el gobierno normativo, ¿qué corresponde a Legal y qué a Compliance Manager?**

- a) Compliance Manager decide qué leyes aplican
- b) Legal decide la aplicabilidad y Compliance Manager organiza controles, acciones y evidencias de lo decidido  ✅
- c) El proveedor de la plantilla responde por el cumplimiento
- d) La puntuación reemplaza la opinión legal

*Respuesta: b).* Una puntuación alta no equivale a cumplimiento; la herramienta organiza el trabajo, pero la interpretación de la ley es de Legal. [Fuente](https://learn.microsoft.com/en-us/purview/compliance-manager-faq) · Repasa [O3](04_Nivel_4_Operacion.md#o3)

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. No constituye asesoría legal: la normativa citada es material de referencia y las decisiones de aplicabilidad corresponden a tus áreas de Legal, privacidad y, cuando aplique, RR. HH. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

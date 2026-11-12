# Evaluaciones y respuestas

*Seguridad de Microsoft 365 Copilot, agentes y Copilot Studio Ninja Training · Edición 2026*

[← Comunidad](05_Comunidad.md) · [Índice del programa](README.md) · [Laboratorio y práctica en producción →](07_Laboratorio_y_practica_en_produccion.md)

<a id="respuestas"></a>

Cada evaluación tiene preguntas de opción múltiple. Con 80 % o más el nivel se considera aprobado. Es una autoevaluación de esta guía, no una certificación de Microsoft.

<a id="eval-inicial"></a>

## Nivel 1 · Inicial · Fundamentos

**1. ¿Por qué un servidor MCP agregado a un agente de Copilot Studio puede gobernarse con directivas de datos?**

- a) Porque MCP cifra los prompts de extremo a extremo
- b) Porque se expone mediante la infraestructura de conectores, con directivas de datos, VNet y autenticación  ✅
- c) Porque requiere una licencia de Agent 365
- d) No puede gobernarse con directivas de datos

*Respuesta: b).* Desde abril de 2025 MCP llega a Copilot Studio sobre la infraestructura de conectores, que admite directivas de datos (DLP), integración con VNet y varios métodos de autenticación. No requiere Agent 365. [Fuente](https://devblogs.microsoft.com/powerplatform/microsoft-copilot-studio-mcp/) · Repasa [P0](01_Nivel_1_Inicial.md#p0)

**2. ¿Qué examen otorga la certificación «Microsoft 365 Certified: Copilot and Agent Administration Fundamentals»?**

- a) SC-401
- b) AB-650
- c) AB-900  ✅
- d) MS-4002

*Respuesta: c).* AB-900 es el examen de fundamentos (45 minutos, disponible en español). AB-650 lleva al nivel asociado y está en beta, SC-401 es de protección de la información y MS-4002 es un curso, no un examen. [Fuente](https://learn.microsoft.com/en-us/credentials/certifications/copilot-and-agent-administration-fundamentals/) · Repasa [I0](01_Nivel_1_Inicial.md#i0)

**3. Con la búsqueda web activa, ¿qué envía Copilot a Bing?**

- a) El prompt completo y los documentos citados
- b) El ID del tenant para personalizar los resultados
- c) Nada: Bing se ejecuta dentro del límite de Microsoft 365
- d) Una consulta corta derivada del prompt, sin identificadores de Entra, junto con la IP del cliente  ✅

*Respuesta: d).* Copilot genera una consulta de pocas palabras, sin archivos completos ni identificadores de Entra; la IP se envía para localizar resultados y Bing actúa como responsable independiente, fuera del límite de Microsoft 365. [Fuente](https://learn.microsoft.com/en-us/microsoft-365/copilot/manage-public-web-access) · Repasa [I1](01_Nivel_1_Inicial.md#i1)

**4. ¿Qué afirmación sobre la protección de datos empresariales (EDP) de Copilot es correcta?**

- a) Microsoft entrena modelos fundacionales con los prompts si el tenant lo permite
- b) Aplica a Copilot y Copilot Chat bajo el DPA y los Product Terms, y Microsoft no entrena modelos fundacionales con prompts, respuestas ni datos de Graph  ✅
- c) Solo aplica a usuarios con licencia de Microsoft 365 Copilot
- d) Solo aplica a tenants con Multi-Geo

*Respuesta: b).* La EDP cubre tanto a Copilot como a Copilot Chat, con Microsoft como encargado del tratamiento, e incluye el compromiso de no entrenar modelos fundacionales con los datos del cliente. [Fuente](https://learn.microsoft.com/en-us/microsoft-365/copilot/enterprise-data-protection) · Repasa [I1](01_Nivel_1_Inicial.md#i1)

**5. ¿Cuántas licencias de Copilot hacen falta para desbloquear las funciones de SharePoint Advanced Management pensadas para Copilot?**

- a) Una por cada sitio
- b) 300 como mínimo
- c) Al menos una licencia asignada en el tenant  ✅
- d) Ninguna: vienen con E3

*Respuesta: c).* Basta una licencia de Copilot asignada. Siguen requiriendo SAM Plan 1 la restricción de creación de sitios por apps y el renombrado avanzado de tenants con más de 10.000 sitios. [Fuente](https://learn.microsoft.com/en-us/sharepoint/sharepoint-advanced-management-features-copilot-license) · Repasa [I2](01_Nivel_1_Inicial.md#i2)

**6. Un tenant con capacidad prepagada de Copilot Studio y sin pago por uso llega al 125 % de consumo. ¿Qué ocurre?**

- a) Se bloquean los agentes del entorno, incluso en conversaciones en curso  ✅
- b) Solo se envía un correo al administrador
- c) Se activa automáticamente el pago por uso
- d) Solo se bloquean los agent flows

*Respuesta: a).* Al 125 % de la capacidad prepagada se bloquean los agentes del entorno; un entorno con pago por uso no se bloquea. Los agent flows se bloquean por separado. [Fuente](https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-messages-management) · Repasa [I2](01_Nivel_1_Inicial.md#i2)

**7. Configuraste el pago por uso de Copilot Chat con un presupuesto mensual. ¿Qué pasa al superarlo?**

- a) El consumo se corta de inmediato
- b) El presupuesto solo avisa; para cortar hay que desconectar la directiva, y el corte tarda hasta 2 horas  ✅
- c) Se cobra a la tarjeta del usuario
- d) Microsoft suspende la suscripción de Azure

*Respuesta: b).* El presupuesto del pago por uso de Copilot solo envía alertas y no detiene el consumo; al desconectar la directiva de facturación, el acceso tarda hasta 2 horas en cortarse. [Fuente](https://learn.microsoft.com/en-us/copilot/implement/setup-pay-as-you-go) · Repasa [I2](01_Nivel_1_Inicial.md#i2)

**8. ¿Qué rol se recomienda para cambiar los ajustes de Copilot en el centro de administración sin usar Global Administrator?**

- a) Global Reader
- b) Teams Administrator
- c) Billing Administrator
- d) AI Administrator  ✅

*Respuesta: d).* La página Copilot > Settings se administra con AI Administrator; Global Reader solo puede ver y los ajustes que abren otro servicio piden el rol de ese servicio. [Fuente](https://learn.microsoft.com/en-us/copilot/implement/configure-copilot-admin-center) · Repasa [I3](01_Nivel_1_Inicial.md#i3)

**9. ¿Qué propiedad de la auditoría de Copilot indica una inyección cruzada (XPIA) detectada en un recurso accedido?**

- a) JailbreakDetected
- b) PolicyDetails
- c) XPIADetected  ✅
- d) SensitivityLabelId

*Respuesta: c).* XPIADetected va dentro de AccessedResources; JailbreakDetected marca intentos de jailbreak en los mensajes. [Fuente](https://learn.microsoft.com/en-us/purview/audit-copilot) · Repasa [I4](01_Nivel_1_Inicial.md#i4)

**10. Tras la publicación de EchoLeak (CVE-2025-32711), ¿qué debía hacer el cliente para corregirla?**

- a) Nada: Microsoft la mitigó en el servicio, aunque conviene reducir la sobreexposición y auditar  ✅
- b) Instalar un parche en los clientes de Office
- c) Desactivar Copilot hasta nuevo aviso
- d) Comprar Agent 365

*Respuesta: a).* El aviso de MSRC indica corrección del lado del servicio, sin acción del cliente y sin explotación conocida. La defensa en profundidad del cliente sigue siendo necesaria. [Fuente](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-32711) · Repasa [I4](01_Nivel_1_Inicial.md#i4)

**11. Según Microsoft Incident Response, ¿a qué riesgos del Top 10 agéntico de OWASP corresponde el envenenamiento de la descripción de una herramienta MCP usada por un agente de Copilot Studio?**

- a) LLM10 y ASI09
- b) Solo LLM02
- c) A la táctica de reconocimiento de ATLAS
- d) ASI02 (uso indebido de herramientas) y ASI04 (cadena de suministro agéntica)  ✅

*Respuesta: d).* Microsoft mapeó el caso de junio de 2026 a ASI02 y ASI04: una actualización silenciosa de la descripción del servidor MCP hizo que el agente enviara facturas al atacante. [Fuente](https://www.microsoft.com/en-us/security/blog/2026/06/30/securing-ai-agents-ai-tools-move-from-reading-acting/) · Repasa [I4](01_Nivel_1_Inicial.md#i4)

**12. Desde el 31 de julio de 2026, ¿qué pasa con Restricted SharePoint Search?**

- a) Se amplía a 1.000 sitios
- b) Pasa a ser un límite de seguridad
- c) No admite nuevas habilitaciones y Microsoft recomienda Restricted Content Discovery  ✅
- d) Se incluye en E5 sin licencia de Copilot

*Respuesta: c).* RSS está en retiro: desde esa fecha se bloquean nuevas habilitaciones. Nunca fue un límite de seguridad y su reemplazo es Restricted Content Discovery. [Fuente](https://learn.microsoft.com/en-us/sharepoint/restricted-sharepoint-search) · Repasa [I5](01_Nivel_1_Inicial.md#i5)

**13. Para apuntar una política de acceso condicional específicamente a Microsoft 365 Copilot, ¿qué haces?**

- a) Creas el service principal «Enterprise Copilot Platform» (AppId fb8d773d-…) y lo seleccionas como recurso  ✅
- b) Seleccionas «Microsoft Copilot (consumer)»
- c) Seleccionas solo «Office 365 Exchange Online»
- d) Usas una identidad de agente de Entra

*Respuesta: a).* La guía de Entra pide crear el service principal con New-MgServicePrincipal para que aparezca en el selector. La recomendación base sigue siendo cubrir All resources. [Fuente](https://raw.githubusercontent.com/MicrosoftDocs/entra-docs/main/docs/identity/conditional-access/policy-all-users-copilot-ai-security.md) · Repasa [I6](01_Nivel_1_Inicial.md#i6)

**14. ¿Qué recomienda Microsoft para impedir que los empleados usen Copilot con cuentas personales en equipos corporativos?**

- a) Tenant Restrictions v2  ✅
- b) Bloquear copilot.cloud.microsoft en el proxy
- c) Desinstalar la app Microsoft Copilot
- d) Desactivar Copilot Chat

*Respuesta: a).* Tenant Restrictions v2 bloquea cuentas personales y de otros tenants. No se debe bloquear copilot.cloud.microsoft, porque también lo usa la experiencia empresarial. [Fuente](https://learn.microsoft.com/en-us/copilot/manage/manage-copilot-chat) · Repasa [I6](01_Nivel_1_Inicial.md#i6)

**15. ¿Qué limitación tiene la prueba individual de Copilot Studio en tu laboratorio?**

- a) No permite crear agentes
- b) No permite usar el chat de prueba
- c) Solo dura 7 días
- d) No permite publicar el agente  ✅

*Respuesta: d).* La prueba permite crear y probar agentes, pero no publicarlos; se amplía 30 días y el agente funciona hasta 90 días tras vencer. Para publicar hace falta pago por uso o capacidad. [Fuente](https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-licensing-subscriptions) · Repasa [I7](01_Nivel_1_Inicial.md#i7)

<a id="eval-intermedio"></a>

## Nivel 2 · Intermedio · Proteger

**1. ¿Cuál de estas afirmaciones sobre Restricted Content Discovery (RCD) es correcta?**

- a) Cambia los permisos del sitio para quitar a EEEU
- b) Aplica también a las OneDrive de los usuarios
- c) Oculta el sitio de la búsqueda organizacional y de Copilot y quita sus puntos de entrada de IA, sin cambiar permisos  ✅
- d) Saca el contenido del índice y desactiva eDiscovery

*Respuesta: c).* RCD no cambia permisos ni saca el sitio del índice; lo oculta de la búsqueda organizacional y del descubrimiento de Copilot y quita el botón de Copilot y la creación de agentes en el sitio. No aplica a OneDrive. [Fuente](https://learn.microsoft.com/en-us/sharepoint/restricted-content-discovery) · Repasa [M1](02_Nivel_2_Intermedio.md#m1)

**2. ¿Qué vista de DSPM no está disponible sin Microsoft 365 E7 o Agent 365?**

- a) AI observability  ✅
- b) La pestaña AI activities del explorador de actividad
- c) Las evaluaciones de riesgo de datos
- d) Reports

*Respuesta: a).* Según MC1280556, AI observability e Insider Risk para agentes requieren E7 o Agent 365. Las demás vistas están disponibles con las licencias de Purview. [Fuente](https://message.cengizyilmaz.net/message/mc1280556-microsoft-purview-for-agents-ai-observability-and-insider-risk-management-now-generally-available) · Repasa [M2](02_Nivel_2_Intermedio.md#m2)

**3. ¿En qué modo se crea la política de un clic «DSPM for AI: Detect sensitive info added to AI sites»?**

- a) Bloqueo
- b) Prueba con anulación
- c) Deshabilitada
- d) Solo auditoría, para todos los usuarios  ✅

*Respuesta: d).* La política se crea en modo solo auditoría y cubre a todos los usuarios; es una política de descubrimiento. [Fuente](https://learn.microsoft.com/en-us/purview/dspm-for-ai-considerations) · Repasa [M2](02_Nivel_2_Intermedio.md#m2)

**4. ¿Qué derechos de uso necesita un usuario para que Copilot use contenido cifrado?**

- a) EDIT y PRINT
- b) OWNER
- c) VIEW y EXTRACT  ✅
- d) FORWARD y REPLY

*Respuesta: c).* Copilot exige VIEW y EXTRACT. Si la etiqueta solo concede VIEW, Copilot no puede usar el contenido. [Fuente](https://learn.microsoft.com/en-us/copilot/plan/architecture-data-protection-auditing) · Repasa [M3](02_Nivel_2_Intermedio.md#m3)

**5. ¿Qué contenido no devuelve Copilot?**

- a) Correos protegidos con S/MIME  ✅
- b) Archivos cifrados con Customer Key
- c) Archivos etiquetados sin cifrado
- d) Archivos cifrados con BYOK

*Respuesta: a).* Copilot no devuelve correos S/MIME y no está disponible en Outlook con uno abierto; Customer Key y BYOK sí se admiten. [Fuente](https://learn.microsoft.com/en-us/purview/ai-m365-copilot) · Repasa [M3](02_Nivel_2_Intermedio.md#m3)

**6. ¿Cómo arranca la política «Default DLP policy - Protect sensitive M365 Copilot interactions»?**

- a) Forzada, con sugerencias al usuario
- b) Desactivada
- c) Solo para administradores
- d) En simulación, con una alerta y un correo de baja severidad  ✅

*Respuesta: d).* Microsoft la crea para todos los usuarios en modo simulación, con una alerta y un correo de baja severidad y sin sugerencias al usuario. [Fuente](https://learn.microsoft.com/en-us/purview/dlp-microsoft365-copilot-location-default-policy) · Repasa [M4](02_Nivel_2_Intermedio.md#m4)

**7. Un usuario sube a Copilot un PDF con números de tarjeta y escribe un prompt sin datos sensibles. ¿Qué evalúa la DLP de la ubicación de Copilot?**

- a) El contenido del PDF
- b) Solo el texto escrito en el prompt  ✅
- c) Ambos
- d) Ninguno

*Respuesta: b).* La ubicación de Copilot no analiza los archivos subidos al prompt: solo evalúa el texto. [Fuente](https://learn.microsoft.com/en-us/purview/dlp-microsoft365-copilot-location-learn-about) · Repasa [M4](02_Nivel_2_Intermedio.md#m4)

**8. ¿Qué controla el ajuste «Advanced package uploads» del centro de administración?**

- a) Quién puede subir agentes declarativos con acciones o servidores MCP  ✅
- b) El tamaño máximo de los archivos en Copilot
- c) La publicación en la tienda de socios
- d) La subida de documentos a Notebooks

*Respuesta: a).* El ajuste decide quién sube paquetes avanzados (agentes declarativos con acciones o servidores MCP): todos, nadie o grupos específicos. Los paquetes básicos siguen permitidos. [Fuente](https://learn.microsoft.com/en-us/copilot/manage/configure-copilot-advanced-package-uploads) · Repasa [M5](02_Nivel_2_Intermedio.md#m5)

**9. Bloqueas en el centro de administración un plugin que usa un conector de Copilot y un servidor MCP remoto. ¿Qué ocurre?**

- a) Se revoca automáticamente el consentimiento de la app en Entra
- b) Los usuarios dejan de poder usarlo, pero el consentimiento, los datos indexados por el conector y el servidor MCP remoto siguen intactos  ✅
- c) Se borran los datos que el conector indexó
- d) Se detiene el servidor MCP remoto

*Respuesta: b).* Cada objeto tiene su propio control: bloquear un plugin no revoca el consentimiento, no borra los datos indexados ni detiene el servidor MCP remoto. Tu procedimiento de contención debe cubrir esas capas. [Fuente](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/manage) · Repasa [M5](02_Nivel_2_Intermedio.md#m5)

**10. ¿Qué sucede desde el 15 de diciembre de 2026 con un entorno de desarrollador no administrado de Power Platform?**

- a) Se convierte automáticamente en administrado
- b) Se mueve a un sandbox
- c) Se suspende y sus apps, flujos y agentes dejan de estar disponibles; se elimina desde el 15 de enero de 2027  ✅
- d) Se borra de inmediato

*Respuesta: c).* La retirada tiene tres fechas: sin entornos nuevos desde el 15 de noviembre de 2026, suspensión desde el 15 de diciembre de 2026 y eliminación desde el 15 de enero de 2027. [Fuente](https://learn.microsoft.com/en-us/power-platform/developer/plan) · Repasa [M6](02_Nivel_2_Intermedio.md#m6)

**11. ¿Qué afirmación sobre el enrutamiento de entornos es correcta?**

- a) Está activado por defecto para Copilot Studio
- b) Envía a cada creador a su propio entorno de desarrollador administrado  ✅
- c) Lo bloquea el ajuste «Environment assignment: Developer»
- d) No requiere Managed Environments

*Respuesta: b).* El enrutamiento es una función premium, desactivada por defecto, que envía a los creadores a su entorno de desarrollador administrado; el ajuste de asignación solo afecta a la creación manual. [Fuente](https://learn.microsoft.com/en-us/power-platform/admin/default-environment-routing) · Repasa [M6](02_Nivel_2_Intermedio.md#m6)

**12. Para impedir que los creadores publiquen agentes sin autenticación, ¿qué conector bloqueas en la directiva de datos?**

- a) HTTP
- b) Direct Line channels in Copilot Studio
- c) Chat without Microsoft Entra ID authentication in Copilot Studio  ✅
- d) Microsoft Copilot Studio

*Respuesta: c).* «Chat without Microsoft Entra ID authentication in Copilot Studio» habilita los agentes sin autenticación. Direct Line controla canales, HTTP el nodo de solicitudes y «Microsoft Copilot Studio» los desencadenadores de eventos. [Fuente](https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-data-loss-prevention) · Repasa [M7](02_Nivel_2_Intermedio.md#m7)

**13. ¿Qué efecto tiene forzar las credenciales del usuario final en «Control maker credential options»?**

- a) Ninguno sobre los agentes existentes
- b) Solo afecta a los agentes nuevos
- c) Bloquea la publicación en Teams
- d) Las herramientas exigen el inicio de sesión del usuario y fallan los agentes autónomos o programados  ✅

*Respuesta: d).* Con credenciales del usuario final, nadie actúa con los permisos del creador; a cambio, los agentes autónomos o programados, que dependen de las credenciales del autor, fallan. [Fuente](https://learn.microsoft.com/en-us/microsoft-copilot-studio/configure-no-maker-authentication) · Repasa [M7](02_Nivel_2_Intermedio.md#m7)

**14. ¿Dónde encuentras las apps de IA generativa en Defender for Cloud Apps?**

- a) En el Cloud app catalog, con la categoría «Generative AI»  ✅
- b) En App governance
- c) En Exposure Management
- d) En el Action center

*Respuesta: a).* En el portal de Defender, Cloud apps > Cloud app catalog con el filtro de categoría «Generative AI»; desde allí se revisa el riesgo, se crean políticas y se desautorizan apps. [Fuente](https://learn.microsoft.com/en-us/copilot/manage/manage-generative-ai-apps) · Repasa [M8](02_Nivel_2_Intermedio.md#m8)

**15. ¿Qué licencia exige la DLP de red de Purview (Network Data Security) con Global Secure Access?**

- a) Solo Microsoft 365 E3
- b) Microsoft 365 E7, o Purview E5 más Entra Internet Access  ✅
- c) Defender for Cloud Apps
- d) Agent 365

*Respuesta: b).* Con Global Secure Access requiere E7 o Purview E5 más Entra Internet Access; con un SASE de terceros, Purview E5 y pago por uso. Entra Internet Access no viene en E5. [Fuente](https://learn.microsoft.com/en-us/purview/dlp-network-data-security-learn) · Repasa [M8](02_Nivel_2_Intermedio.md#m8)

<a id="eval-avanzado"></a>

## Nivel 3 · Avanzado · Detectar, auditar y responder

**1. ¿Qué campo de un registro CopilotInteraction indica que Copilot usó la búsqueda web pública para responder?**

- a) Contexts.Type con el valor Web
- b) AppHost con el valor Edge
- c) AISystemPlugin.Id con el valor BingWebSearch  ✅
- d) AccessedResources.XPIADetected con el valor true

*Respuesta: c).* AISystemPlugin con el valor BingWebSearch revela el uso de la web; XPIADetected marca una inyección indirecta detectada en un recurso accedido y AppHost indica dónde ocurrió la interacción. [Fuente](https://learn.microsoft.com/en-us/purview/audit-copilot) · Repasa [A1](03_Nivel_3_Avanzado.md#a1)

**2. Tu organización tiene Microsoft 365 E5 y nadie creó políticas de retención de auditoría. ¿Cuánto tiempo se conservan los registros CopilotInteraction?**

- a) 180 días  ✅
- b) 1 año, igual que Exchange y SharePoint
- c) 10 años
- d) 90 días

*Respuesta: a).* Con E5, el año predeterminado solo cubre Entra, Exchange y SharePoint. Para CopilotInteraction hace falta una política de retención de auditoría explícita: hasta un año, o diez con el complemento. [Fuente](https://learn.microsoft.com/en-us/purview/audit-log-retention-policies) · Repasa [A1](03_Nivel_3_Avanzado.md#a1)

**3. ¿Dónde guarda Purview la copia de cumplimiento de los prompts y las respuestas de Copilot?**

- a) En la biblioteca de conservación de OneDrive del usuario
- b) En una carpeta oculta del buzón de Exchange del usuario  ✅
- c) En una cuenta de Azure Storage del cliente
- d) En el área de trabajo de Sentinel

*Respuesta: b).* Las interacciones se guardan en una carpeta oculta del buzón; por eso la retención, los holds y los buzones inactivos aplican igual que al correo. [Fuente](https://learn.microsoft.com/en-us/purview/retention-policies-copilot) · Repasa [A2](03_Nivel_3_Avanzado.md#a2)

**4. En el flujo de búsqueda y eliminación de datos de IA de eDiscovery, ¿cuántos elementos por buzón se borran como máximo en cada ejecución?**

- a) 1
- b) 100
- c) 10  ✅
- d) Sin límite, mientras no haya holds

*Respuesta: c).* Se borran hasta 10 elementos por buzón en cada ejecución, con purgeData en Microsoft Graph; además hay que retirar los holds y luego reaplicarlos, y borrar requiere el rol Search And Purge. [Fuente](https://learn.microsoft.com/en-us/purview/edisc-search-copilot-data) · Repasa [A2](03_Nivel_3_Avanzado.md#a2)

**5. ¿Para qué origen NO genera cargos de pago por uso Communication Compliance?**

- a) Copilot Studio
- b) Security Copilot
- c) Other AI apps
- d) Microsoft 365 Copilot  ✅

*Respuesta: d).* Microsoft 365 Copilot no genera cargos de pago por uso en Communication Compliance; Copilot en Fabric, Security Copilot, Copilot Studio y las apps de IA conectadas o en la nube sí. [Fuente](https://learn.microsoft.com/en-us/purview/communication-compliance-copilot) · Repasa [A3](03_Nivel_3_Avanzado.md#a3)

**6. ¿Qué necesita la plantilla Risky AI usage de Insider Risk Management para detectar visitas a sitios de IA generativa?**

- a) Una licencia de Agent 365
- b) La extensión Microsoft Insider risk en Edge o Microsoft Purview en Chrome y al menos un indicador de navegación  ✅
- c) Una directiva de sesión de Defender for Cloud Apps
- d) Que cada usuario tenga licencia de Microsoft 365 Copilot

*Respuesta: b).* La plantilla requiere la extensión de navegador y al menos un indicador de navegación; se crea con un clic desde la política «DSPM for AI - Detect risky AI usage». [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-policy-templates) · Repasa [A3](03_Nivel_3_Avanzado.md#a3)

**7. Desde el 1 de julio de 2026, ¿qué licencia exigen la detección de amenazas y la protección en tiempo real de agentes de Copilot Studio y Foundry en Defender?**

- a) Defender for Cloud Apps
- b) Defender CSPM
- c) Microsoft Agent 365  ✅
- d) Unidades SCU de Security Copilot

*Respuesta: c).* La seguridad de agentes de Copilot Studio y Foundry en Defender pasó a requerir Agent 365, que está fuera del alcance de este programa; las alternativas son la protección integrada de Copilot Studio, la detección externa propia, la auditoría y Sentinel. [Fuente](https://learn.microsoft.com/en-us/defender-xdr/security-for-ai/transition-agent-security-to-agent-365) · Repasa [A4](03_Nivel_3_Avanzado.md#a4)

**8. Sin Agent 365, ¿cuál de estas capacidades de Defender XDR sigue disponible con Microsoft 365 E5 para proteger el uso de Copilot?**

- a) Investigar en el portal de Defender las alertas DLP de la ubicación de Copilot  ✅
- b) Ver los agentes de Copilot Studio en Assets > AI agents
- c) Bloquear en tiempo real las invocaciones de herramientas de los agentes
- d) Consultar en AgentsInfo los agentes de nube

*Respuesta: a).* Las alertas DLP de Purview se investigan en Defender XDR con licencias E5; el inventario de agentes de nube, el bloqueo en tiempo real y AgentsInfo para esos agentes dependen de Agent 365. [Fuente](https://learn.microsoft.com/en-us/defender-xdr/dlp-investigate-alerts-defender) · Repasa [A4](03_Nivel_3_Avanzado.md#a4)

**9. ¿A qué tabla escribe el conector de datos de Microsoft Copilot de Sentinel?**

- a) CopilotActivity  ✅
- b) OfficeActivity
- c) AIAgentsInfo
- d) PowerPlatformAdminActivity

*Respuesta: a).* El conector lleva la auditoría de Copilot a CopilotActivity; las consultas de ejemplo oficiales todavía usan el nombre anterior, LLMActivity. [Fuente](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/copilotactivity) · Repasa [A5](03_Nivel_3_Avanzado.md#a5)

**10. Configuraste la detección externa de amenazas en un entorno de Copilot Studio. Si el servicio no responde en un segundo, ¿qué ocurre con la configuración por defecto?**

- a) Se bloquea la herramienta
- b) El agente queda en cuarentena
- c) Se reintenta tres veces antes de decidir
- d) Se permite la ejecución de la herramienta  ✅

*Respuesta: d).* Por defecto se permite la acción; puede cambiarse para bloquear la consulta, algo recomendable en los entornos sensibles una vez medida la latencia. [Fuente](https://learn.microsoft.com/en-us/microsoft-copilot-studio/external-security-provider) · Repasa [A6](03_Nivel_3_Avanzado.md#a6)

**11. ¿Con qué credenciales se autentican los desencadenadores de eventos de un agente autónomo de Copilot Studio?**

- a) Las del usuario final que conversa con el agente
- b) Las del administrador del entorno
- c) Las de un service principal obligatorio
- d) Las del autor del agente  ✅

*Respuesta: d).* Se autentican con la cuenta del autor; por eso Copilot Studio advierte al publicar que usuarios sin autorización propia podrían acceder a datos con esos permisos. [Fuente](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-trigger-event) · Repasa [A6](03_Nivel_3_Avanzado.md#a6)

**12. Desde mayo de 2026, ¿qué ocurre al crear un agente nuevo en Copilot Studio?**

- a) Se crea un registro de aplicación por agente
- b) Se crea un Microsoft Entra Agent ID hijo del blueprint global de Copilot Studio, sin opción de exclusión  ✅
- c) No se crea ninguna identidad hasta que se publica
- d) Se exige Agent 365 para crearlo

*Respuesta: b).* Cada agente nuevo recibe un Agent ID; los anteriores conservan su registro de aplicación hasta que se migren, y extender controles de seguridad a esas identidades requiere Agent 365. [Fuente](https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-use-entra-agent-identities) · Repasa [A7](03_Nivel_3_Avanzado.md#a7)

**13. ¿Qué afirmación sobre Workload ID Premium es correcta?**

- a) Está incluido en Microsoft 365 E5
- b) Forma parte de Entra Suite
- c) Cuesta 3 USD por workload identity al mes y no viene en E5 ni en E7  ✅
- d) Es gratuito para las identidades administradas

*Respuesta: c).* Workload ID Premium se licencia aparte, con una prueba de 90 días, y habilita acceso condicional, ID Protection y revisiones para los service principals. [Fuente](https://learn.microsoft.com/en-us/entra/workload-id/workload-identities-faqs) · Repasa [A7](03_Nivel_3_Avanzado.md#a7)

**14. ¿Qué ocurre con un agente de Copilot Studio puesto en cuarentena con la Power Platform API?**

- a) Sigue visible y sus creadores pueden probarlo, pero deja de funcionar en los demás canales  ✅
- b) Se elimina junto con su Agent ID
- c) Solo deja de funcionar en Teams
- d) Pierde sus conexiones y debe recrearse

*Respuesta: a).* La cuarentena es reversible y no aplica a los chatbots clásicos; se ejecuta con una app que tiene el ámbito CopilotStudio.AdminActions.Invoke. [Fuente](https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-api-quarantine) · Repasa [A8](03_Nivel_3_Avanzado.md#a8)

**15. Según el patrón de respuesta a incidentes de IA de la Secure Future Initiative, ¿qué corresponde a la primera hora?**

- a) Corregir el defecto en el origen y cerrar el incidente
- b) Bloquear entradas conocidas, activar filtros y restringir el acceso  ✅
- c) Notificar a todos los usuarios y apagar Copilot en el inquilino
- d) Esperar el informe forense antes de actuar

*Respuesta: b).* La remediación es por etapas: primera hora para contener, 24 horas para ampliar las mitigaciones y días o semanas para corregir en el origen, con periodos de observación. [Fuente](https://learn.microsoft.com/en-us/security/zero-trust/sfi/incident-response-ai-systems) · Repasa [A8](03_Nivel_3_Avanzado.md#a8)

<a id="eval-operacion"></a>

## Nivel 4 · Gobierno y operación continua · Operar la IA con excelencia

**1. Según el marco de seguridad y gobierno de los Copilot controls, ¿qué combinación corresponde a los controles fundamentales?**

- a) Purview y Defender for Cloud Apps con licencias A5, E5 o G5
- b) Centro de administración de Microsoft 365, SharePoint Advanced Management y Purview con licencias A3, E3 o G3  ✅
- c) Agent 365 con Microsoft 365 E7
- d) Defender XDR y Sentinel con E5

*Respuesta: b).* Los controles optimizados son los de Purview y Defender for Cloud Apps con A5, E5 o G5; Agent 365 queda fuera del marco que se enseña en este programa. [Fuente](https://learn.microsoft.com/en-us/copilot/implement/copilot-controls-security-governance) · Repasa [O1](04_Nivel_4_Gobierno_y_operacion_continua.md#o1)

**2. ¿Cuáles son las cuatro funciones del NIST AI RMF 1.0?**

- a) Identify, Protect, Detect y Respond
- b) Plan, Do, Check y Act
- c) Govern, Map, Measure y Manage  ✅
- d) Discover, Classify, Protect y Monitor

*Respuesta: c).* El AI RMF organiza la gestión del riesgo de IA en Govern, Map, Measure y Manage; Govern AI del Cloud Adoption Framework sigue ese enfoque. [Fuente](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf) · Repasa [O1](04_Nivel_4_Gobierno_y_operacion_continua.md#o1)

**3. Con licencias Microsoft 365 E5, ¿cuántas plantillas premium puedes elegir en Compliance Manager, por ejemplo para EU AI Act o ISO/IEC 42001?**

- a) Hasta tres  ✅
- b) Una
- c) Hasta diez
- d) Ilimitadas

*Respuesta: a).* Las licencias E5, A5 y G5 permiten elegir hasta tres plantillas premium; las de IA consumen esas licencias premium. [Fuente](https://learn.microsoft.com/en-us/purview/compliance-manager-faq) · Repasa [O1](04_Nivel_4_Gobierno_y_operacion_continua.md#o1)

**4. ¿Cuál es el estado del Power Platform CoE Starter Kit en noviembre de 2026?**

- a) Recibe nuevas funciones cada mes
- b) Se convirtió en el Copilot Agent Kit
- c) Ya no se mantiene: sus escenarios pasan a Inventory, Usage, Monitor y Actions del centro de administración de Power Platform  ✅
- d) Solo funciona con Agent 365

*Respuesta: c).* Desde el 7 de mayo de 2026 sigue disponible, pero sin mejoras ni revisión de incidencias; el Copilot Agent Kit es otro proyecto, antes llamado Copilot Studio Kit. [Fuente](https://learn.microsoft.com/en-us/power-platform/guidance/coe/starter-kit) · Repasa [O2](04_Nivel_4_Gobierno_y_operacion_continua.md#o2)

**5. ¿Qué rol de Purview permite editar la DLP de la ubicación de Copilot sin poder leer los prompts?**

- a) Purview Data Security AI Admin  ✅
- b) Content Explorer Content Viewer
- c) eDiscovery Manager
- d) Global Reader

*Respuesta: a).* Purview Data Security AI Admin edita la DLP de Copilot sin acceso al contenido; Content Explorer Content Viewer, en cambio, permite leer los prompts. [Fuente](https://learn.microsoft.com/en-us/purview/dlp-microsoft365-copilot-location-learn-about) · Repasa [O2](04_Nivel_4_Gobierno_y_operacion_continua.md#o2)

**6. En el centro de administración de Microsoft 365, ¿durante cuántos días se puede recuperar un agente eliminado?**

- a) 7
- b) 14
- c) 30  ✅
- d) 90

*Respuesta: c).* La eliminación deja 30 días para restaurar el agente o eliminarlo definitivamente; las acciones fallan sobre agentes protegidos por el firewall de Power Platform. [Fuente](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-actions?view=o365-worldwide) · Repasa [O3](04_Nivel_4_Gobierno_y_operacion_continua.md#o3)

**7. Una creadora de agentes con Agent Builder deja la empresa. Sin Agent 365, ¿qué permite el centro de administración de Microsoft 365?**

- a) Nada: el agente se borra automáticamente
- b) Asignar un nuevo dueño o crear una regla que reasigne al gerente de la creadora los agentes de Agent Builder sin dueño  ✅
- c) Solo aplicar una plantilla de seguridad
- d) Solo actuar desde Defender

*Respuesta: b).* Las reglas de gestión de agentes están incluidas en los planes de Microsoft 365; las plantillas («Apply template») sí requieren Agent 365. [Fuente](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-settings?view=o365-worldwide) · Repasa [O3](04_Nivel_4_Gobierno_y_operacion_continua.md#o3)

**8. ¿Qué elementos de un agente de Copilot Studio NO viajan en la solución y deben reconfigurarse en cada entorno?**

- a) Las variables de entorno
- b) Las referencias de conexión
- c) Los temas del agente
- d) La autenticación manual, los canales desplegados y el uso compartido  ✅

*Respuesta: d).* Application Insights, la autenticación manual, la seguridad del canal web y de Direct Line, los canales desplegados y el uso compartido se configuran después del despliegue. [Fuente](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/alm) · Repasa [O3](04_Nivel_4_Gobierno_y_operacion_continua.md#o3)

**9. ¿Qué necesitas para ver en el Copilot Dashboard información de agentes, benchmarks y la vista por grupos?**

- a) Una licencia paga de Viva Insights por usuario
- b) 50 licencias de Copilot  ✅
- c) Agent 365
- d) Una licencia de Copilot por cada gerente

*Respuesta: b).* El Copilot Dashboard está disponible sin licencia paga de Viva Insights; con una licencia de Copilot incluye Copilot y Copilot Chat, y con 50 agrega agentes, benchmarks y vista por grupos. [Fuente](https://learn.microsoft.com/en-us/viva/insights/org-team-insights/copilot-dashboard) · Repasa [O4](04_Nivel_4_Gobierno_y_operacion_continua.md#o4)

**10. ¿Qué indicador propone el modelo de despliegue de DSPM como punto de partida?**

- a) El porcentaje de activos sensibles protegidos por al menos una política DLP, con revisión de recomendaciones cada 30 días  ✅
- b) El número de prompts por usuario y día
- c) La cantidad de agentes visibles en AI observability
- d) Las licencias de Copilot asignadas sobre las compradas

*Respuesta: a).* Es un indicador de resultado; AI observability no sirve como indicador del programa porque exige E7 o Agent 365. [Fuente](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-dspm-step3) · Repasa [O4](04_Nivel_4_Gobierno_y_operacion_continua.md#o4)

**11. ¿Cuánta capacidad de Security Copilot incluye Microsoft 365 E5?**

- a) 100 SCU al mes por inquilino
- b) 400 SCU al mes por cada 1.000 licencias pagadas, hasta 10.000 SCU mensuales  ✅
- c) 1 SCU por usuario y mes
- d) Ninguna: Security Copilot se compra aparte

*Respuesta: b).* La inclusión aplica a E5 y E7 con licencias pagadas; el data lake de Sentinel y Logic Apps se pagan aparte. [Fuente](https://learn.microsoft.com/en-us/copilot/security/security-copilot-inclusion) · Repasa [O5](04_Nivel_4_Gobierno_y_operacion_continua.md#o5)

**12. ¿Qué afirmación sobre el Conditional Access Optimization Agent es correcta?**

- a) Aplica políticas en modo activo de forma automática
- b) Requiere Agent 365
- c) Es gratuito y no consume SCU
- d) Requiere Entra ID P1 y SCU, y crea las políticas en modo solo informe  ✅

*Respuesta: d).* Está en disponibilidad general desde el 14 de julio de 2025, revisa hasta 300 usuarios y 150 apps por ejecución y factura al menos una SCU al mes. [Fuente](https://learn.microsoft.com/en-us/entra/security-copilot/conditional-access-agent-optimization) · Repasa [O5](04_Nivel_4_Gobierno_y_operacion_continua.md#o5)

**13. ¿Qué alertas procesa el Triage Agent de Purview en DLP?**

- a) Solo las de políticas activas, no las de políticas en simulación  ✅
- b) Solo las de Copilot Studio
- c) Todas, incluidas las de políticas en simulación
- d) Solo las de endpoint

*Respuesta: a).* El agente clasifica alertas de Exchange, dispositivos, SharePoint, OneDrive y Teams de políticas activas, revisa hasta 30 días antes de habilitarlo y consume SCU. [Fuente](https://learn.microsoft.com/en-us/purview/copilot-in-purview-agents-overview) · Repasa [O5](04_Nivel_4_Gobierno_y_operacion_continua.md#o5)

**14. ¿Qué país de MCSA tiene ley de IA y reglamento vigentes que clasifican los usos en indebido, de riesgo alto y de riesgo aceptable?**

- a) Chile
- b) Colombia
- c) Perú  ✅
- d) México

*Respuesta: c).* El DS 115-2025-PCM reglamenta la Ley 31814 y rige desde el 22 de enero de 2026. Es referencia, no asesoría legal. [Fuente](https://www.gob.pe/institucion/pcm/normas-legales/7133522-115-2025-pcm) · Repasa [O6](04_Nivel_4_Gobierno_y_operacion_continua.md#o6)

**15. ¿Cuál es la situación de Panamá a inicios de noviembre de 2026?**

- a) Tiene una ley de IA vigente desde 2024
- b) Adoptó la Ley de IA de la Unión Europea
- c) No registra ningún avance
- d) Aprobó su Estrategia Nacional de IA por la Resolución de Gabinete 75 y el proyecto 588 pasó el tercer debate, pendiente de sanción  ✅

*Respuesta: d).* El proyecto no obliga hasta su sanción y publicación en la Gaceta Oficial, pero anticipa una clasificación por impacto que conviene preparar. [Fuente](https://www.asamblea.gob.pa/Noticias/Actualidad/REGLAS-DE-GOBERNANZA-EN-APLICACION-DE-LA-IA-) · Repasa [O6](04_Nivel_4_Gobierno_y_operacion_continua.md#o6)

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. El contenido regulatorio y de privacidad es una referencia y no constituye asesoría legal ni laboral: las decisiones sobre captura de prompts, monitoreo, retención y normativa corresponden a tus áreas de Legal, privacidad y RR. HH. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

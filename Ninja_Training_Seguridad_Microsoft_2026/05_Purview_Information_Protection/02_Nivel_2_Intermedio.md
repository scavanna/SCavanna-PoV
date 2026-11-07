# Nivel 2 · Intermedio · Automatizar y proteger

*Microsoft Purview Information Protection Ninja Training: clasificación, etiquetado y cifrado · Edición 2026*

[← Nivel 1 · Inicial](01_Nivel_1_Inicial.md) · [Índice del programa](README.md) · [Nivel 3 · Avanzado →](03_Nivel_3_Avanzado.md)

<a id="intermedio"></a>

Etiquetado automático en cliente y en servicio, cifrado y control de uso, etiquetas en contenedores, reuniones, Loop, PDF, Power BI, Fabric y Data Map, y el escáner junto con el retiro de las directivas de archivo de Defender for Cloud Apps. Terminas con un proyecto confidencial protegido de punta a punta y un plan de migración con fecha.

*L300 · 4 módulos · ~24 horas · 37 recursos*

**Módulos de este nivel:** [M1 Etiquetado automático](#m1) · [M2 Cifrado y control de uso](#m2) · [M3 Contenedores, Teams y Fabric](#m3) · [M4 Escáner y Cloud Apps](#m4)

<a id="m1"></a>

## M1 · Etiquetado automático en cliente y en servicio

*L300 · ~6 h · Origen: Ruta Ninja de Learn · módulo 2 (etiquetado automático) y ruta de la credencial SC-5003*

Hay dos formas de etiquetar sin depender de la memoria de las personas. El **etiquetado en cliente** se configura en la propia etiqueta: mientras alguien trabaja en Word, Excel, PowerPoint u Outlook, la app recomienda o aplica la etiqueta cuando detecta SIT o clasificadores, y la persona puede rechazar una recomendación. El **etiquetado en servicio** usa políticas que etiquetan archivos en reposo en SharePoint y OneDrive y correo en tránsito en Exchange (no buzones en reposo), siempre con un modo **simulación** previo para revisar qué se etiquetaría.

Los límites importan para planificar: el techo es de 500.000 archivos por día por tenant (antes 100.000) y no es una tasa garantizada; hay un máximo de 100 políticas, 1.000 sitios seleccionados de forma explícita y 20 millones de coincidencias por simulación. Desde septiembre de 2026 las simulaciones llegan a 20 millones de elementos, los ámbitos adaptables a 50.000 sitios y se pueden editar políticas sin volver a simular. Una política especial (MC1477181) aplica la etiqueta predeterminada de biblioteca a archivos existentes sin etiqueta.

La estrategia del modelo secure by default combina ambos métodos: recomendar con pocas coincidencias, aplicar con muchas, simular en reposo y reducir falsos positivos con clasificadores. Para medir, la pestaña **Insights** de cada política muestra 30 días de métricas de SharePoint y OneDrive; para Exchange se usa el explorador de actividades. Y recuerda que lo que una política etiqueta queda etiquetado: no hay un botón para deshacer una oleada.

**Por qué importa**

Nadie va a etiquetar a mano millones de archivos existentes. El auto-etiquetado en servicio es la palanca que sube la cobertura sobre el contenido heredado, y las recomendaciones en cliente educan a las personas en el momento de crear. Hacerlo con simulación, oleadas y métricas evita etiquetar —o cifrar— en masa el contenido equivocado e interrumpir procesos de negocio.

**Qué vas a lograr**

- Elegir entre etiquetado automático en cliente y en servicio según la ubicación, la experiencia de usuario y la licencia.
- Configurar recomendaciones en Office con umbrales de coincidencias.
- Ejecutar una política en servicio en modo simulación, revisar muestras y activarla por etapas.
- Planificar contra los límites vigentes de archivos por día, políticas, sitios y simulación.
- Medir los resultados con la pestaña Insights y el explorador de actividades.

> **Novedad.** Desde agosto de 2026 las políticas de auto-etiquetado procesan hasta 500.000 archivos de SharePoint y OneDrive por día, antes 100.000 ([blog de agosto](https://www.microsoft.com/en-us/security/blog/2026/08/27/whats-new-in-microsoft-security-august-2026/)). Es un techo por tenant, no una tasa garantizada, y se suma a los límites de 100 políticas, 1.000 sitios seleccionados de forma explícita y 20 millones de coincidencias por simulación ([auto-etiquetado](https://learn.microsoft.com/en-us/purview/apply-sensitivity-label-automatically)). El mapa interactivo de Microsoft todavía marca el aumento como vista previa.

> **Novedad.** Septiembre de 2026: simulaciones de hasta 20 millones de elementos, ámbitos adaptables de hasta 50.000 sitios y edición de políticas sin volver a simular ([blog de septiembre](https://www.microsoft.com/en-us/security/blog/2026/09/24/whats-new-in-microsoft-security-september-2026/)).

> **Qué cambió.** MC1477181 (22 de septiembre de 2026) agrega una política especial para aplicar la etiqueta predeterminada de biblioteca a archivos existentes sin etiqueta: una política por tenant y hasta 10 sitios. Un MVP la describe como disponible en general y la arquitectura de referencia de Microsoft, como vista previa pública: verifica en tu tenant ([análisis](https://office365itpros.com/2026/11/05/auto-label-policy-default-label/)).

> **Consejo Ninja.** Estrategia por umbrales del modelo secure by default: recomendar con 1 a 9 coincidencias, aplicar con 10 o más, simular en reposo y bajar falsos positivos con clasificadores ([paso 3](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-secure-by-default-step3)). La pestaña Insights muestra 30 días de métricas solo para SharePoint y OneDrive; para Exchange usa el explorador de actividades ([Insights](https://learn.microsoft.com/en-us/purview/auto-label-insights-tab)).

**¿Tienes poco tiempo?**

- [Automatically apply a sensitivity label to Microsoft 365 data](https://learn.microsoft.com/en-us/purview/apply-sensitivity-label-automatically) · Documentación
- [Step 3: Expand protection to your entire Microsoft 365 data estate - Secure by default with Microsoft Purview](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-secure-by-default-step3) · Documentación
- [Use the Insights tab to analyze auto-labeling policies in Microsoft Purview](https://learn.microsoft.com/en-us/purview/auto-label-insights-tab) · Documentación
- [What’s new in Microsoft Security: August 2026](https://www.microsoft.com/en-us/security/blog/2026/08/27/whats-new-in-microsoft-security-august-2026/) · Blog oficial

### Documentación, cursos y credenciales

- [Automatically apply a sensitivity label to Microsoft 365 data](https://learn.microsoft.com/en-us/purview/apply-sensitivity-label-automatically) · Documentación · Oficial · Microsoft Learn. Compara el auto-etiquetado en cliente (recomendar o aplicar en apps de Office) con las políticas de auto-etiquetado en servicio (SharePoint, OneDrive y Exchange en tránsito), su modo simulación y sus límites.
- [Step 3: Expand protection to your entire Microsoft 365 data estate - Secure by default with Microsoft Purview](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-secure-by-default-step3) · Documentación · Oficial · Microsoft Learn - Purview deployment models. Estrategia de auto-etiquetado por umbrales (recomendar con 1-9 coincidencias, aplicar con 10+), simulación de auto-etiquetado en reposo y reducción de falsos positivos con clasificadores.

### Anuncios y blogs oficiales

- [What’s new in Microsoft Security: September 2026](https://www.microsoft.com/en-us/security/blog/2026/09/24/whats-new-in-microsoft-security-september-2026/) · Blog oficial · Empleado de Microsoft · Nuevo · Alym Rayani · Microsoft Security Blog · 24 sep 2026. Resumen mensual oficial que anuncia mejoras de auto-etiquetado (simulaciones de hasta 20 millones de elementos, hasta 50.000 sitios con ámbitos adaptables y edición sin re-simular) y la GA de Purview + Entra Global Secure Access para seguridad de datos en red.
- [What’s new in Microsoft Security: August 2026](https://www.microsoft.com/en-us/security/blog/2026/08/27/whats-new-in-microsoft-security-august-2026/) · Blog oficial · Empleado de Microsoft · Nuevo · Alym Rayani · Microsoft Security Blog · 27 ago 2026. Anuncio oficial de que las directivas de etiquetado automático de Purview procesan hasta 500.000 archivos de SharePoint y OneDrive al día (antes 100.000).

### Comunidad: blogs, libros, newsletters y eventos

- [SharePoint Online Extends Auto-Labeling of Sensitivity Labels to Cover Older Files](https://office365itpros.com/2026/11/05/auto-label-policy-default-label/) · Blog · MVP · Nuevo · Tony Redmond · Office 365 for IT Pros · 5 nov 2026. Analiza la política especial de auto-etiquetado (MC1477181, 22-sep-2026) que aplica la etiqueta predeterminada de biblioteca a archivos existentes sin etiqueta, limitada a una política por tenant y 10 sitios.

**Manos a la obra**

1. `Laboratorio` Configura en una etiqueta el etiquetado automático para archivos y correo que la recomiende cuando detecte números de tarjeta de crédito; prueba en Word y Outlook con números de tarjeta de prueba publicados por los emisores y captura la recomendación ([auto-etiquetado](https://learn.microsoft.com/en-us/purview/apply-sensitivity-label-automatically), [experiencia del usuario](https://support.microsoft.com/en-us/office/security-privacy/sensitivity-labels-are-automatically-applied-or-recommended-for-your-files-and-emails-in-office)).
2. `Laboratorio` Ajusta la condición con umbrales —recomendar con 1 a 9 coincidencias y aplicar con 10 o más— y documenta qué ve la persona en cada caso, incluido el rechazo de una recomendación ([paso 3](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-secure-by-default-step3)).
3. `Laboratorio parcial` Crea una política de auto-etiquetado en servicio en modo simulación para dos sitios de prueba y para Exchange; revisa coincidencias, muestras y la pestaña Insights ([Insights](https://learn.microsoft.com/en-us/purview/auto-label-insights-tab)). Limitación: con poco volumen y una latencia de horas a días, la simulación no refleja los falsos positivos reales. En producción: simula primero, limita el alcance a pocos sitios y activa por etapas.
4. `Laboratorio parcial` Configura la etiqueta predeterminada de una biblioteca de prueba y, si tu tenant ya muestra la política especial de MC1477181, aplícala a los archivos existentes sin etiqueta; documenta qué archivos cambiaron ([etiqueta de biblioteca](https://learn.microsoft.com/en-us/purview/sensitivity-labels-sharepoint-default-label), [análisis](https://office365itpros.com/2026/11/05/auto-label-policy-default-label/)). Limitación: su disponibilidad varía por tenant (GA o vista previa según la fuente).
5. `Laboratorio` Exporta con `Export-ActivityExplorerData` los eventos de etiquetado automático del correo de las últimas 24 horas y compáralos con lo esperado ([cmdlet](https://learn.microsoft.com/en-us/powershell/module/exchangepowershell/export-activityexplorerdata?view=exchange-ps)).
6. `Solo producción` Activa el auto-etiquetado en producción: elige de 1 a 3 sitios piloto con dueño identificado, simula, revisa con el dueño de los datos una muestra de 50 coincidencias y activa por oleadas semanales, la primera sin cifrado. Forma segura: ticket de cambio, ventana acordada y plan de reversión manual, porque lo que la política etiqueta queda etiquetado.

**¿Quieres profundizar?**

- [SharePoint Online Extends Auto-Labeling of Sensitivity Labels to Cover Older Files](https://office365itpros.com/2026/11/05/auto-label-policy-default-label/) · Blog

<a id="m2"></a>

## M2 · Cifrado y control de uso: Rights Management, cifrado de mensajes y revocación

*L300 · ~5 h · Origen: Ruta Ninja de Learn · módulo 2 (protección) y guía SC-401 (OME y Advanced Message Encryption)*

Una etiqueta puede cifrar con el servicio **Rights Management**: la protección viaja con el archivo o el correo y sigue vigente cuando sale del tenant. Los **derechos de uso** —VIEW, EDIT, EXTRACT, PRINT, EXPORT, FORWARD y OWNER, entre otros— definen qué puede hacer cada persona, agrupados en niveles de permiso como Copropietario, Coautor, Revisor y Visor. Puedes asignar permisos de antemano, dejar que el usuario los defina o, en el correo, usar Encrypt-Only y Do Not Forward. La **licencia de uso** permite abrir el contenido sin conexión hasta que vence, 30 días por defecto.

El cifrado tiene efectos que conviene conocer: los servicios también necesitan leer el contenido. Habilitar las etiquetas para SharePoint y OneDrive permite coautoría, búsqueda, eDiscovery, DLP y Office web sobre archivos cifrados (no con DKE ni HYOK). La característica de **superusuario**, deshabilitada por defecto, permite recuperar contenido. El **seguimiento y la revocación** usan el ContentID del documento, y **Advanced Message Encryption** agrega expiración y revocación para el correo enviado a externos por el portal de OME.

La regla de oro: un error de cifrado puede dejar a las personas sin acceso a su propio contenido. Por eso este módulo trabaja con etiquetas de prueba, un invitado de un segundo tenant y un plan de reversión: nunca elimines una etiqueta que cifra; quítala de la política.

**Por qué importa**

El cifrado es el único control que sigue protegiendo los datos después de que salen del tenant, en un correo reenviado o en un archivo copiado a una memoria USB. Mal diseñado, bloquea a los socios, rompe aplicaciones de negocio y vuelve el contenido invisible para la búsqueda, eDiscovery y Copilot. Diseñar bien los derechos de uso, el superusuario y la revocación lo convierte en un control reversible y auditable en lugar de una crisis para la mesa de ayuda.

**Qué vas a lograr**

- Configurar una etiqueta con permisos asignados y elegir el nivel de permisos según el uso.
- Explicar el efecto de cada derecho de uso, en especial VIEW y EXTRACT.
- Habilitar y operar la característica de superusuario con auditoría.
- Rastrear y revocar documentos y correos cifrados con OME y Advanced Message Encryption.
- Diseñar pruebas de acceso externo y un plan de reversión.

> **Atención.** Copilot y otros servicios dependen de los derechos de uso: para usar contenido cifrado necesitan VIEW y EXTRACT. En los niveles de permiso, EXTRACT (Copiar) está en Coautor y Copropietario, pero no en Revisor ni en Visor ([derechos de uso](https://learn.microsoft.com/en-us/purview/rights-management-usage-rights)). Diseña cada etiqueta sabiendo qué personas y qué servicios deben poder leerla.

> **Atención.** Nunca elimines una etiqueta que cifra: quítala de la política. Si se elimina, su plantilla de protección se archiva y no debe borrarse, porque el contenido quedaría inaccesible ([crear etiquetas](https://learn.microsoft.com/en-us/purview/create-sensitivity-labels)). En SharePoint y OneDrive, los archivos cifrados antes de habilitar las etiquetas deben editarse o volver a subirse para beneficiarse ([SharePoint y OneDrive](https://learn.microsoft.com/en-us/purview/sensitivity-labels-sharepoint-onedrive-files)).

> **Consejo Ninja.** La característica de superusuario concede control total sobre todo el contenido cifrado del tenant y está deshabilitada por defecto: habilítala solo cuando haga falta y audítala con `Get-AipServiceAdminLog` ([superusuarios](https://learn.microsoft.com/en-us/purview/encryption-super-users)). El seguimiento y la revocación de documentos no aplican a archivos con contraseña, y el acceso sin conexión persiste hasta que vence la licencia de uso ([seguimiento y revocación](https://learn.microsoft.com/en-us/purview/track-and-revoke-admin)).

> **Novedad.** Advanced Message Encryption (Microsoft 365 E5, Purview Suite, E5 IP&G y Office 365 E5) agrega varias plantillas de marca, expiración y revocación del correo enviado a externos, pero solo para el correo entregado por el portal de OME con una plantilla de marca personalizada ([AME](https://learn.microsoft.com/en-us/purview/ome-advanced-message-encryption)). Si el destinatario recibió la experiencia nativa de Outlook, no se puede revocar ([revocar](https://learn.microsoft.com/en-us/purview/revoke-ome-encrypted-mail)).

**¿Tienes poco tiempo?**

- [Configure usage rights for the Azure Rights Management service](https://learn.microsoft.com/en-us/purview/rights-management-usage-rights) · Documentación
- [Configure Azure Rights Management super users for discovery services or data recovery](https://learn.microsoft.com/en-us/purview/encryption-super-users) · Documentación
- [Track and revoke document access](https://learn.microsoft.com/en-us/purview/track-and-revoke-admin) · Documentación
- [Advanced Message Encryption](https://learn.microsoft.com/en-us/purview/ome-advanced-message-encryption) · Documentación

### Documentación, cursos y credenciales

- [Advanced Message Encryption](https://learn.microsoft.com/en-us/purview/ome-advanced-message-encryption) · Documentación · Oficial · Nuevo · Microsoft Learn · 14 may 2026. Describe Advanced Message Encryption: plantillas de marca múltiples, expiración y revocación de correos cifrados para destinatarios externos vía portal OME y registro de acceso al portal.
- [Configure usage rights for the Azure Rights Management service](https://learn.microsoft.com/en-us/purview/rights-management-usage-rights) · Documentación · Oficial · Microsoft Learn. Tabla de derechos de uso de Rights Management (VIEW, DOCEDIT, EDIT, EXPORT, EXTRACT, FORWARD, etc.), niveles de permiso, opciones Do Not Forward y Encrypt-Only y conceptos de emisor/propietario y licencia de uso.
- [Track and revoke document access](https://learn.microsoft.com/en-us/purview/track-and-revoke-admin) · Documentación · Oficial · Microsoft Learn. Cómo los administradores rastrean accesos y revocan documentos de Office protegidos mediante el ContentID con el módulo AIPService (Get-AipServiceDocumentLog, Get-AipServiceTrackingLog, Set-AIPServiceDocumentRevoked).
- [Configure Azure Rights Management super users for discovery services or data recovery](https://learn.microsoft.com/en-us/purview/encryption-super-users) · Documentación · Oficial · Microsoft Learn. Explica la característica de superusuario de Azure RMS (derecho Full Control sobre todo contenido cifrado del tenant), cómo habilitarla con el módulo AIPService y buenas prácticas de seguridad y auditoría.
- [Revoke email encrypted by Advanced Message Encryption](https://learn.microsoft.com/en-us/purview/revoke-ome-encrypted-mail) · Documentación · Oficial · Microsoft Learn. Procedimiento para que remitentes (Outlook web) o administradores (PowerShell) revoquen correos cifrados con experiencia basada en vínculo enviados a destinatarios externos.
- [Track and revoke access to your files](https://support.microsoft.com/en-us/office/track-and-revoke-access-to-your-files) · Documentación · Oficial · Microsoft Support. Guía para usuarios finales sobre cómo rastrear y revocar el acceso a archivos locales cifrados con etiqueta desde el menú Confidencialidad de Word, Excel y PowerPoint.

**Manos a la obra**

1. `Laboratorio` Crea la etiqueta PRUEBA-Confidencial-Proyecto con cifrado de permisos asignados: Coautor para un grupo interno y Revisor para el invitado del segundo tenant. Aplícala a un documento y verifica con cada cuenta qué puede hacer (editar, copiar, imprimir y reenviar). Evidencia: tabla de resultados por cuenta ([derechos de uso](https://learn.microsoft.com/en-us/purview/rights-management-usage-rights)).
2. `Laboratorio` Sube el documento cifrado a una biblioteca con etiquetas habilitadas, ábrelo en Office web y prueba la coautoría con dos personas internas ([SharePoint y OneDrive](https://learn.microsoft.com/en-us/purview/sensitivity-labels-sharepoint-onedrive-files)). Anota qué pasa con un archivo cifrado que subiste antes de habilitar las etiquetas.
3. `Laboratorio` Envía correos con Encrypt-Only y con Do Not Forward a un destinatario interno y a uno externo y documenta qué puede hacer cada uno: reenviar, imprimir o copiar.
4. `Laboratorio` Rastrea y revoca un documento local cifrado desde Word como usuario ([guía para usuarios](https://support.microsoft.com/en-us/office/track-and-revoke-access-to-your-files)) y luego como administrador con `Get-AipServiceDocumentLog` y `Set-AIPServiceDocumentRevoked` ([seguimiento y revocación](https://learn.microsoft.com/en-us/purview/track-and-revoke-admin)). Comprueba que el invitado pierde el acceso en línea y anota que el acceso sin conexión persiste hasta que vence la licencia de uso.
5. `Laboratorio` Habilita temporalmente un superusuario de prueba, abre un archivo cifrado del que no es destinatario, deshabilita la característica y revisa el registro con `Get-AipServiceAdminLog` ([superusuarios](https://learn.microsoft.com/en-us/purview/encryption-super-users)).
6. `Laboratorio parcial` Configura una plantilla de marca personalizada de OME, envía con Advanced Message Encryption un correo a una cuenta de un proveedor de correo público, ábrelo en el portal y revócalo ([AME](https://learn.microsoft.com/en-us/purview/ome-advanced-message-encryption), [revocar](https://learn.microsoft.com/en-us/purview/revoke-ome-encrypted-mail)). Limitación: necesitas un destinatario que reciba la experiencia por vínculo; con cuentas de Microsoft 365 la experiencia es nativa y no se puede revocar.
7. `Solo producción` Piloto de cifrado en producción: aplica la etiqueta cifrante a un grupo piloto con documentos sintéticos y a un socio externo de confianza durante dos semanas. Forma segura: superusuario definido y probado antes de empezar, sin cifrado retroactivo masivo, mesa de ayuda informada y reversión quitando la etiqueta de la política, nunca eliminándola.

<a id="m3"></a>

## M3 · Etiquetas en contenedores, reuniones, Loop, PDF, Power BI, Fabric y Data Map

*L300 · ~7 h · Origen: Ruta Ninja de Learn · módulo 2 y guía SC-401 (contenedores y Power BI); Data Map, nuevo en esta edición*

Aplicada a un equipo de Teams, un grupo, un sitio de SharePoint, una comunidad de Viva Engage o un área de trabajo de Loop, una **etiqueta de contenedor** no clasifica los elementos internos: gobierna el contenedor. Controla la privacidad, el acceso de invitados, el uso compartido externo, el acceso desde dispositivos no administrados y los contextos de autenticación (estos dos con Acceso condicional). Los archivos no heredan la etiqueta del contenedor, aunque los canales compartidos sí heredan la del equipo. Antes de usarlas hay que habilitar el soporte en Entra ID y sincronizar las etiquetas.

Las **reuniones** se etiquetan desde Outlook o Teams para cifrar la invitación y aplicar opciones como sala de espera, grabación, marca de agua, cifrado de audio y video o bloqueo de copia del chat; varias requieren Teams Premium y no hay auto-etiquetado. En **Loop**, las etiquetas son manuales en componentes, páginas (incluidas las Copilot Pages) y áreas de trabajo, sin permisos definidos por el usuario, expiración ni DKE. El **PDF** se etiqueta al exportar desde Office y en SharePoint, donde su soporte se habilita aparte.

En **Power BI y Fabric** se etiquetan informes, paneles, modelos semánticos, flujos y archivos .pbix, con herencia al crear, desde orígenes de datos y descendente; en el servicio la etiqueta no restringe el acceso, pero protege lo que sale por rutas de exportación compatibles. Fuera de Microsoft 365, el etiquetado en **Data Map y Unified Catalog** está en vista previa: solo auto-etiquetado como metadatos, sin cifrado ni marcas, y con pago por uso para orígenes no Microsoft 365.

**Por qué importa**

Los datos no viven solo en archivos de Word: están en Teams, sitios, reuniones, páginas de Loop, informes de Power BI y bases de datos. Las etiquetas de contenedor frenan la sobreexposición desde la creación —una de las causas principales de lo que Copilot puede encontrar—, las de reuniones protegen las conversaciones más sensibles y las de Fabric y Data Map extienden el mismo vocabulario a la analítica. Una sola taxonomía en todas las superficies hace coherentes las métricas, la DLP y los controles de Copilot.

**Qué vas a lograr**

- Configurar etiquetas de contenedor con privacidad, invitados, uso compartido externo y dispositivos no administrados.
- Etiquetar reuniones de Teams y saber qué opciones requieren Teams Premium.
- Aplicar etiquetas en Loop y PDF y explicar sus limitaciones.
- Habilitar las etiquetas en Fabric y Power BI, comprobar la herencia y proteger las exportaciones.
- Evaluar el etiquetado en Data Map (vista previa) y su costo por uso.

> **Atención.** Los archivos de un equipo o sitio no heredan la etiqueta del contenedor; los canales compartidos sí heredan la del equipo. Los controles de dispositivos no administrados y de contextos de autenticación dependen de Acceso condicional, y el vínculo de uso compartido predeterminado solo se configura con PowerShell ([contenedores](https://learn.microsoft.com/en-us/purview/sensitivity-labels-teams-groups-sites)). Aplicar la etiqueta no elimina a los invitados existentes y los propietarios pueden cambiarla, lo que queda en la auditoría ([a escala](https://nikkichapple.com/how-do-i-add-sensitivity-labels-to-your-existing-groups-teams-and-sites/)).

> **Novedad.** Las comunidades de Viva Engage admiten etiquetas de contenedor desde marzo y abril de 2026 (MC1250283) ([análisis](https://office365itpros.com/2026/04/03/container-management-labels-viva/)). En reuniones, «Apply meeting label to artifacts» sigue en vista previa (página actualizada el 10 de junio de 2026), varias opciones exigen Teams Premium y no hay auto-etiquetado ni soporte de S/MIME o DKE ([reuniones](https://learn.microsoft.com/en-us/purview/sensitivity-labels-meetings)).

> **Atención.** Power BI y Fabric: ver y aplicar etiquetas requiere Azure Information Protection Premium P1 o P2 (incluidas en las suites) y, para aplicarlas, Power BI Pro o PPU ([habilitar](https://learn.microsoft.com/en-us/fabric/enterprise/powerbi/service-security-enable-data-sensitivity-labels)). En el servicio la etiqueta no restringe el acceso, lo hacen los permisos de Power BI; el cifrado se aplica al exportar por rutas compatibles ([etiquetas en Power BI](https://learn.microsoft.com/en-us/fabric/enterprise/powerbi/service-security-sensitivity-label-overview)). La herencia desde orígenes solo funciona en modo Import ([herencia desde orígenes](https://learn.microsoft.com/en-us/fabric/governance/service-security-sensitivity-label-inheritance-from-data-sources)).

> **Novedad.** Etiquetas en Data Map y Unified Catalog: vista previa, solo auto-etiquetado al escanear, aplicado como metadatos del activo, sin cifrado ni marcas y sin SIT personalizados ni clasificadores avanzados; licencias de la familia E5 y pago por uso para orígenes no Microsoft 365 (FAQ actualizada el 1 de junio de 2026) ([FAQ](https://learn.microsoft.com/en-us/purview/data-map-sensitivity-labels-faq)).

**¿Tienes poco tiempo?**

- [Use sensitivity labels to protect collaborative workspaces (groups and sites)](https://learn.microsoft.com/en-us/purview/sensitivity-labels-teams-groups-sites) · Documentación
- [Use sensitivity labels to protect calendar items, Teams meetings, and chat](https://learn.microsoft.com/en-us/purview/sensitivity-labels-meetings) · Documentación
- [Enable sensitivity labels in Fabric and Power BI](https://learn.microsoft.com/en-us/fabric/enterprise/powerbi/service-security-enable-data-sensitivity-labels) · Documentación
- [Sensitivity labels in Microsoft Purview Data Map FAQ (preview)](https://learn.microsoft.com/en-us/purview/data-map-sensitivity-labels-faq) · Documentación

### Documentación, cursos y credenciales

- [Use sensitivity labels to protect calendar items, Teams meetings, and chat](https://learn.microsoft.com/en-us/purview/sensitivity-labels-meetings) · Documentación · Oficial · Nuevo · Microsoft Learn · 10 jun 2026. Cómo etiquetar y cifrar invitaciones y reuniones de Teams, aplicar opciones de reunión (lobby, grabación, marca de agua, cifrado de audio/video, bloqueo de copia del chat) y heredar la etiqueta desde archivos compartidos o hacia grabaciones y notas.
- [Use sensitivity labels to protect collaborative workspaces (groups and sites)](https://learn.microsoft.com/en-us/purview/sensitivity-labels-teams-groups-sites) · Documentación · Oficial · Microsoft Learn. Cómo habilitar y configurar etiquetas para contenedores (Teams, grupos de M365, sitios de SharePoint, comunidades de Viva Engage y áreas de Loop): privacidad, acceso externo, dispositivos no administrados, contextos de autenticación y vínculo de uso compartido predeterminado.
- [Sensitivity labels in Power BI](https://learn.microsoft.com/en-us/fabric/enterprise/powerbi/service-security-sensitivity-label-overview) · Documentación · Oficial · Microsoft Learn - Microsoft Fabric. Cómo funcionan las etiquetas en Power BI/Fabric: herencia al crear, desde orígenes y descendente, políticas de etiqueta predeterminada y obligatoria, APIs de administración y protección al exportar a Excel, PowerPoint, PDF o .pbix.
- [Enable sensitivity labels for files in SharePoint and OneDrive](https://learn.microsoft.com/en-us/purview/sensitivity-labels-sharepoint-onedrive-files) · Documentación · Oficial · Microsoft Learn. Paso habilitador para que SharePoint y OneDrive procesen archivos de Office y PDF cifrados con etiquetas (coautoría, búsqueda, eDiscovery, DLP, Office web) y para el auto-etiquetado en reposo.
- [Configure a default sensitivity label for a SharePoint document library](https://learn.microsoft.com/en-us/purview/sensitivity-labels-sharepoint-default-label) · Documentación · Oficial · Microsoft Learn. Cómo configurar la etiqueta predeterminada de una biblioteca de SharePoint (etiquetado por ubicación sin inspección de contenido), cuándo sobrescribe etiquetas existentes y sus limitaciones.
- [Enable sensitivity labels in Fabric and Power BI](https://learn.microsoft.com/en-us/fabric/enterprise/powerbi/service-security-enable-data-sensitivity-labels) · Documentación · Oficial · Microsoft Learn (Fabric). Requisitos y pasos para habilitar las etiquetas de Purview en el inquilino de Fabric/Power BI y limitar quién puede aplicarlas mediante grupos de seguridad.
- [Sensitivity label downstream inheritance in Power BI](https://learn.microsoft.com/en-us/fabric/governance/service-security-sensitivity-label-downstream-inheritance) · Documentación · Oficial · Microsoft Learn - Microsoft Fabric. Explica la herencia descendente de etiquetas desde modelos semánticos e informes hacia contenido dependiente, con modo de consentimiento del usuario o totalmente automatizado.
- [Use sensitivity labels with Microsoft Loop](https://learn.microsoft.com/en-us/purview/sensitivity-labels-loop) · Documentación · Oficial · Microsoft Learn. Etiquetas en componentes y páginas de Loop (incluidas Copilot Pages) y en áreas de trabajo de Loop como contenedores, con herencia de la etiqueta de la página y de archivos referenciados por Copilot.
- [Sensitivity labels in Microsoft Purview Data Map FAQ (preview)](https://learn.microsoft.com/en-us/purview/data-map-sensitivity-labels-faq) · Documentación · Oficial · Vista previa · Nuevo · Microsoft Learn · 1 jun 2026. Preguntas frecuentes sobre etiquetado en Purview Data Map: licencias, diferencia entre clasificaciones y etiquetas y que las etiquetas se aplican solo a los metadatos del activo. *Nota:* Verificado (actualizado 1-jun-2026): etiquetado en Data Map en preview; solo auto-etiquetado (sin etiquetado manual) y solo como metadatos, sin cifrado ni marcas; licencias de la familia E5 y facturación pay-as-you-go para orígenes no Microsoft 365…
- [Sensitivity label inheritance from data sources in Power BI](https://learn.microsoft.com/en-us/fabric/governance/service-security-sensitivity-label-inheritance-from-data-sources) · Documentación · Oficial · Microsoft Learn - Microsoft Fabric. Describe cómo los modelos semánticos heredan etiquetas de Excel en SharePoint/OneDrive, Azure Synapse y Azure SQL Database, con sus requisitos y limitaciones.

### Comunidad: blogs, libros, newsletters y eventos

- [How to Configure Container Sensitivity Labels in Microsoft Purview (Step-by-Step)](https://nikkichapple.com/configure-container-sensitivity-labels-microsoft-365/) · Blog · MVP · Nuevo · Nikki Chapple · 5 jul 2026. Guía paso a paso para configurar etiquetas de contenedor basadas en riesgo (privacidad, invitados, uso compartido, dispositivos no administrados y PowerShell avanzado) para reducir la sobreexposición ante Copilot.
- [How To Apply Container Sensitivity Labels at Scale in Microsoft 365](https://nikkichapple.com/how-do-i-add-sensitivity-labels-to-your-existing-groups-teams-and-sites/) · Blog · MVP · Nuevo · Nikki Chapple · 5 jul 2026. Metodología para analizar grupos, Teams y sitios existentes (SAM y DSPM) y aplicar etiquetas de contenedor a escala con PowerShell.
- [Container Sensitivity Labels: The Purview “Hack” That Fixes Copilot Oversharing Fast](https://nikkichapple.com/m365-copilot-oversharing-container-labels/) · Blog · MVP · Nuevo · Nikki Chapple · 31 may 2026. Explica por qué la sobreexposición ante Copilot nace en la creación de Teams y sitios y cómo las etiquetas de contenedor aplican controles por riesgo desde el inicio.
- [Use a Default Sensitivity Label to Extend Protection for SPO](https://office365itpros.com/2026/02/26/sensitivity-label-extend-protection/) · Blog · MVP · Tony Redmond · Office 365 for IT Pros · 26 feb 2026. Muestra cómo extender la protección de SharePoint a archivos descargados usando una etiqueta predeterminada de biblioteca con permisos definidos por el usuario (Set-SPOTenant -ExtendPermissionsToUnprotectedFiles).
- [Viva Engage Communities Gain Support for Sensitivity Labels](https://office365itpros.com/2026/04/03/container-management-labels-viva/) · Blog · MVP · Tony Redmond · Office 365 for IT Pros · 3 abr 2026. Describe la llegada (MC1250283, mar-abr 2026) del soporte de etiquetas de contenedor a comunidades de Viva Engage y cómo monitorear que las etiquetas asignadas se mantengan.

**Manos a la obra**

1. `Laboratorio` Habilita las etiquetas para grupos y sitios en Entra ID, sincronízalas con `Execute-AzureAdLabelSync` y crea la etiqueta de contenedor PRUEBA-Altamente confidencial (privada, sin invitados y con acceso solo web desde dispositivos no administrados). Aplícala a un equipo nuevo y verifica que no puedes agregar un invitado ([contenedores](https://learn.microsoft.com/en-us/purview/sensitivity-labels-teams-groups-sites), [paso a paso](https://nikkichapple.com/configure-container-sensitivity-labels-microsoft-365/)).
2. `Laboratorio` Crea un área de trabajo de Loop y un componente con la etiqueta cifrante de permisos asignados; verifica qué etiquetas te ofrece Loop y que no admite etiquetas con permisos definidos por el usuario ([Loop](https://learn.microsoft.com/en-us/purview/sensitivity-labels-loop)).
3. `Laboratorio parcial` Configura una etiqueta para reuniones con marca de agua y bloqueo de copia del chat y programa una reunión de prueba entre dos cuentas ([reuniones](https://learn.microsoft.com/en-us/purview/sensitivity-labels-meetings)). Limitación: sin Teams Premium no podrás configurar todas las opciones; en producción, haz un piloto con personas licenciadas y reuniones entre cuentas de prueba.
4. `Laboratorio` Exporta un documento etiquetado a PDF desde Word y verifica que conserva la etiqueta y el cifrado; documenta cómo se habilita el soporte de PDF en SharePoint ([etiquetas en Office](https://learn.microsoft.com/en-us/purview/sensitivity-labels-office-apps)).
5. `Laboratorio` Habilita las etiquetas en Fabric y Power BI para un grupo de seguridad, etiqueta un modelo semántico y un informe, exporta a Excel y PDF y comprueba la herencia descendente ([habilitar](https://learn.microsoft.com/en-us/fabric/enterprise/powerbi/service-security-enable-data-sensitivity-labels), [herencia descendente](https://learn.microsoft.com/en-us/fabric/governance/service-security-sensitivity-label-downstream-inheritance)). Requiere Power BI Pro o PPU, incluido en la licencia o en prueba.
6. `Laboratorio parcial` Data Map: con el pago por uso vinculado, escanea una cuenta de Azure Storage con datos sintéticos, aplica auto-etiquetado a los activos y revisa el informe clásico de etiquetas de Unified Catalog ([FAQ](https://learn.microsoft.com/en-us/purview/data-map-sensitivity-labels-faq), [informe](https://learn.microsoft.com/en-us/purview/unified-catalog-reports-classic-sensitivity-labels)). Limitación: está en vista previa y cobra por activo y por día; limita el alcance a un recurso de prueba y revisa el consumo a las 48 horas.
7. `Solo producción` Aplica etiquetas de contenedor a equipos y sitios existentes: inventaríalos con SharePoint Advanced Management o DSPM, prioriza por sensibilidad y aplica por lotes con PowerShell ([a escala](https://nikkichapple.com/how-do-i-add-sensitivity-labels-to-your-existing-groups-teams-and-sites/)). Forma segura: aviso a propietarios, piloto con sitios no críticos, informe previo de invitados y dispositivos afectados y reversión documentada, sabiendo que si eliminas una etiqueta de contenedor SharePoint tarda de 48 a 72 horas en dejar de aplicarla.

**¿Quieres profundizar?**

- [How to Configure Container Sensitivity Labels in Microsoft Purview (Step-by-Step)](https://nikkichapple.com/configure-container-sensitivity-labels-microsoft-365/) · Blog
- [How To Apply Container Sensitivity Labels at Scale in Microsoft 365](https://nikkichapple.com/how-do-i-add-sensitivity-labels-to-your-existing-groups-teams-and-sites/) · Blog
- [Container Sensitivity Labels: The Purview “Hack” That Fixes Copilot Oversharing Fast](https://nikkichapple.com/m365-copilot-oversharing-container-labels/) · Blog
- [Use a Default Sensitivity Label to Extend Protection for SPO](https://office365itpros.com/2026/02/26/sensitivity-label-extend-protection/) · Blog

<a id="m4"></a>

## M4 · Escáner de Information Protection, cliente para Windows y el retiro de las directivas de archivo de Defender for Cloud Apps

*L300 · ~6 h · Origen: Guía SC-401 (cliente y escáner) y ruta Ninja de Learn · módulo 5 (contexto de endpoint); retiro de Defender for Cloud Apps, nuevo en esta edición*

No todo está en Microsoft 365: recursos compartidos, NAS y SharePoint Server guardan años de información sin clasificar. El **cliente de Microsoft Purview Information Protection** (solo Windows) reemplazó al cliente de etiquetado unificado de AIP e incluye el escáner, el etiquetador del Explorador de archivos, el visor y un módulo de PowerShell, sin complemento de Office: el complemento de AIP se retiró el 11 de abril de 2024. En ARM64 solo funcionan el visor y el etiquetador, y el cliente requiere una suscripción en la nube y Entra ID.

El **escáner** es un servicio de Windows Server que descubre, clasifica y protege archivos en recursos SMB, NFS (vista previa) y bibliotecas de SharePoint Server. No etiqueta en tiempo real: rastrea por ciclos, admite clústeres multinodo y un modo **solo descubrimiento** ideal para empezar. Pide 4 núcleos, 8 GB de RAM, SQL Server y una cuenta de servicio de Active Directory sincronizada con Entra ID, y ya admite autenticación por certificado en vista previa pública.

La otra mitad del módulo es una fecha: las **directivas de archivo de Defender for Cloud Apps se retiran el 6 de enero de 2027**. Defender for Cloud Apps conserva el descubrimiento de apps SaaS, la postura y la detección de amenazas, pero la protección de archivos pasa a Purview: la herramienta de migración convierte las directivas de SharePoint y OneDrive en DLP o auto-etiquetado, y la DLP de Purview para Box, Dropbox, Google Workspace y Salesforce está en vista previa.

**Por qué importa**

Los recursos compartidos suelen ser el repositorio de datos sin clasificar más grande y el que más aprovechan el ransomware y las personas que dejan la empresa. El escáner da inventario antes que protección, y una migración ordenada de Defender for Cloud Apps antes del 6 de enero de 2027 evita perder controles de archivos en SaaS sin que nadie lo note. Ambos reducen puntos ciegos fuera de Microsoft 365 y alimentan al SOC con eventos de etiquetas.

**Qué vas a lograr**

- Instalar el cliente de Information Protection y etiquetar desde el Explorador de archivos y con PowerShell.
- Desplegar el escáner en modo solo descubrimiento y luego con etiquetado automático.
- Planificar la actualización desde el escáner de AIP 2.x.
- Inventariar las directivas de archivo de Defender for Cloud Apps y planificar su migración a Purview antes del 6 de enero de 2027.

> **Qué cambió.** El complemento de AIP para Office se retiró el 11 de abril de 2024 y quedó deshabilitado en mayo de 2024; ese día salió el cliente de Information Protection 3.0, que mantiene escáner, visor, etiquetador y PowerShell ([MC775357](https://mc.merill.net/message/MC775357), [aviso de retiro](https://techcommunity.microsoft.com/blog/microsoft-security-blog/retirement-notification-for-the-azure-information-protection-unified-labeling-ad/3791908)). Audita los equipos que todavía dependan del complemento.

> **Atención.** Las directivas de archivo de Defender for Cloud Apps se retiran el **6 de enero de 2027**. La herramienta de migración convierte las de SharePoint y OneDrive en DLP o auto-etiquetado de Purview, pero todavía no migra las de apps no Microsoft; su reemplazo, la DLP de Purview para Box, Dropbox, Google Workspace y Salesforce, está en vista previa, requiere el conector de Defender for Cloud Apps y licencia E5, E5 Compliance o DLP equivalente, y no está disponible en nubes gubernamentales o soberanas ([guía de migración](https://learn.microsoft.com/en-us/defender-cloud-apps/migrate-file-policies-to-purview)). No hay un auto-etiquetado equivalente listado para apps no Microsoft.

> **Novedad.** La versión GA 3.2.176.0 del cliente se publicó el 23 de octubre de 2026 en el Download Center, aunque otras réplicas mostraban la 3.2.173.0: verifica la versión al descargar ([descarga](https://www.microsoft.com/en-sa/download/details.aspx?id=53018)). El escáner admite autenticación por certificado en vista previa pública ([instalar el escáner](https://learn.microsoft.com/en-us/purview/deploy-scanner-configure-install)) y recursos NFS en vista previa ([escáner](https://learn.microsoft.com/en-us/purview/deploy-scanner)).

> **Consejo Ninja.** Para pruebas, el escáner acepta cualquier Windows compatible con el cliente, y en modo solo descubrimiento basta con permiso de lectura sobre los repositorios ([prerrequisitos](https://learn.microsoft.com/en-us/purview/deploy-scanner-prereqs)). Si vienes del escáner de AIP 2.x (servicio AIPScanner, fuera de soporte), actualiza al servicio MIPScanner con `Update-ScannerDatabase` ([actualizar](https://learn.microsoft.com/en-us/purview/upgrade-scanner-migrate)).

**¿Tienes poco tiempo?**

- [Migrate file policies to Microsoft Purview (Defender for Cloud Apps)](https://learn.microsoft.com/en-us/defender-cloud-apps/migrate-file-policies-to-purview) · Documentación
- [Extend sensitivity labeling on Windows (Microsoft Purview Information Protection client)](https://learn.microsoft.com/en-us/purview/information-protection-client) · Documentación
- [Learn about the Microsoft Purview Information Protection scanner](https://learn.microsoft.com/en-us/purview/deploy-scanner) · Documentación
- [Get started with the information protection scanner](https://learn.microsoft.com/en-us/purview/deploy-scanner-prereqs) · Documentación

**Del retiro de las directivas de archivo de Defender for Cloud Apps a Purview**

| Caso de uso en Defender for Cloud Apps | Reemplazo en Purview | ¿La herramienta lo migra? | Estado y licencia |
|---|---|---|---|
| Directiva de archivo con DLP sobre SharePoint y OneDrive | Directiva DLP de Purview para SharePoint y OneDrive | Sí | GA; Microsoft 365 E5, E5 Compliance (hoy Purview Suite) o licencia de DLP equivalente |
| Directiva de archivo con acción de etiquetado sobre SharePoint y OneDrive | Política de auto-etiquetado en servicio | Sí | GA; derechos de auto-etiquetado de nivel E5 (indicativo) |
| Directiva de archivo con DLP sobre Box, Dropbox, Google Workspace o Salesforce | DLP de Purview para apps no Microsoft | Todavía no | Vista previa; requiere el conector de la app en Defender for Cloud Apps |
| Directiva de archivo con acción de etiquetado sobre apps no Microsoft | Sin auto-etiquetado equivalente listado | No | Evalúa la DLP en vista previa y sigue la contradicción descrita en los puntos a confirmar |
| Descubrimiento de apps SaaS, postura y detección de amenazas | Se quedan en Defender for Cloud Apps | No aplica | Vigentes |
| Tenants en nubes gubernamentales o soberanas | Migración no disponible con la herramienta | No | Consulta la guía y a tu equipo de cuenta |

Fuente: [guía de migración de directivas de archivo a Purview](https://learn.microsoft.com/en-us/defender-cloud-apps/migrate-file-policies-to-purview) (actualizada el 28 de agosto de 2026; retiro el 6 de enero de 2027). La versión en español describe un alcance menor de la herramienta: prevalece la versión en inglés.

### Documentación, cursos y credenciales

- [Migrate file policies to Microsoft Purview (Defender for Cloud Apps)](https://learn.microsoft.com/en-us/defender-cloud-apps/migrate-file-policies-to-purview) · Documentación · Oficial · Nuevo · Microsoft Learn · 28 ago 2026. Guía oficial para migrar las directivas de archivo de Defender for Cloud Apps a políticas DLP o de auto-etiquetado de Purview con la herramienta de migración y una tabla comparativa de capacidades.
- [Learn about the Microsoft Purview Information Protection scanner](https://learn.microsoft.com/en-us/purview/deploy-scanner) · Documentación · Oficial · Microsoft Learn. Describe el escáner local de Information Protection que, como servicio de Windows Server, descubre, clasifica y protege archivos en recursos compartidos SMB/NFS y bibliotecas de SharePoint Server, con modo solo descubrimiento.
- [Configure and install the Microsoft Purview Information Protection scanner](https://learn.microsoft.com/en-us/purview/deploy-scanner-configure-install) · Documentación · Oficial · Microsoft Learn. Paso a paso para crear el clúster y los trabajos de escaneo en el portal de Purview, instalar el escáner, obtener el token de Entra y aplicar clasificación, protección y reglas DLP.
- [Extend sensitivity labeling on Windows (Microsoft Purview Information Protection client)](https://learn.microsoft.com/en-us/purview/information-protection-client) · Documentación · Oficial · Microsoft Learn. Describe el cliente MPIP para Windows (escáner, etiquetador de Explorador de archivos, visor y módulo de PowerShell) que reemplaza al cliente de etiquetado unificado de AIP y no incluye complemento de Office.
- [Manage sensitivity labels in Office apps](https://learn.microsoft.com/en-us/purview/sensitivity-labels-office-apps) · Documentación · Oficial · Microsoft Learn. Referencia de etiquetado integrado en Office: requisitos (Office por suscripción, buzón en Exchange Online), etiquetado obligatorio, etiqueta predeterminada en Outlook, herencia desde adjuntos, soporte de PDF y barra de confidencialidad.
- [Get started with the information protection scanner](https://learn.microsoft.com/en-us/purview/deploy-scanner-prereqs) · Documentación · Oficial · Microsoft Learn. Prerrequisitos del escáner: Windows Server de 64 bits (4 núcleos, 8 GB RAM, ~10 GB de disco temporal), cuenta de servicio de AD sincronizada con Entra ID, SQL Server, URLs a permitir por HTTPS y alternativas cuando la política impide cumplirlos.
- [Upgrade the Microsoft Purview Information Protection scanner](https://learn.microsoft.com/en-us/purview/upgrade-scanner-migrate) · Documentación · Oficial · Legado aún útil · Microsoft Learn · 28 jun 2024. Procedimiento para actualizar el escáner desde el cliente AIP 2.x (servicio AIPScanner) al cliente MPIP 3.x (servicio MIPScanner) o entre versiones 3.x con Update-ScannerDatabase. *Nota:* El escáner AIP 2.x está fuera de soporte; consultar la página 'Release management and supportability' para fechas por versión

### Anuncios y blogs oficiales

- [Retirement notification for the Azure Information Protection Unified Labeling add-in for Office](https://techcommunity.microsoft.com/blog/microsoft-security-blog/retirement-notification-for-the-azure-information-protection-unified-labeling-ad/3791908) · Blog oficial · Empleado de Microsoft · Legado aún útil · AashishRamdas · Microsoft Tech Community - Microsoft Security Community Blog · 11 abr 2023. Anuncio oficial del retiro del complemento de Office de AIP Unified Labeling el 11-abr-2024 y migración al etiquetado integrado en Microsoft 365 Apps, manteniendo visor, PowerShell, clasificación por clic derecho y escáner. *Nota:* El retiro ya se cumplió (abr-2024); el resto de componentes se renombró a Microsoft Purview Information Protection client. Útil para entender la cronología AIP→MPIP

### Laboratorios, GitHub y herramientas

- [Download Microsoft Purview Information Protection client (Download Center)](https://www.microsoft.com/en-sa/download/details.aspx?id=53018) · Herramienta · Oficial · Nuevo · Microsoft Download Center · 23 oct 2026. Página oficial de descarga del cliente MPIP (PurviewInfoProtection .exe/.msi), con versión GA 3.2.176.0 publicada el 23-oct-2026 y versión preview 3.2.172.

### Comunidad: blogs, libros, newsletters y eventos

- [MC775357 - Reminder: Azure Information Protection Add-in for Office is retired](https://mc.merill.net/message/MC775357) · Blog · Oficial · Legado aún útil · Microsoft (archivado por Merill Fernando) · Microsoft 365 Message Center Archive (mc.merill.net) · 11 abr 2024. Copia pública del aviso oficial: el complemento de AIP para Office se retiró el 11-abr-2024, el cliente MPIP 3.0 salió ese día y el complemento quedó deshabilitado de forma permanente en mayo de 2024. *Nota:* Histórico de retiro (MC541158 anunció el retiro en abril de 2023); útil para la cronología y para auditar equipos que aún dependan del complemento
- [Microsoft Purview Information Protection Scanner: April 2026 Update Points for Admins](https://en.ittrip.xyz/microsoft-365/purview-scanner-2026-update) · Blog · Comunidad · Vista previa · IT trip. Resume la versión preview 3.2.89.0 del cliente/escáner (22-abr-2026) con control de características por clúster, Custom Reporting y autenticación por certificado. *Nota:* Fuente secundaria de baja confiabilidad (sitio agregador sin autor identificable): usar solo como pista; confirmar versiones y fechas de soporte en Microsoft Learn y en el Download Center oficial antes de citar

**Manos a la obra**

1. `Laboratorio` Instala el cliente de Information Protection en una VM Windows 11 de Azure y etiqueta archivos desde el Explorador de archivos y con PowerShell (`Set-FileLabel` y `Get-FileStatus`), incluidos tipos que Office no etiqueta ([cliente para Windows](https://learn.microsoft.com/en-us/purview/information-protection-client)).
2. `Laboratorio parcial` Despliega el escáner en una VM Windows Server con SQL Server Express contra un recurso SMB con 200 archivos sintéticos: crea el clúster y el trabajo de escaneo en el portal, ejecútalo en modo solo descubrimiento y revisa el informe ([prerrequisitos](https://learn.microsoft.com/en-us/purview/deploy-scanner-prereqs), [instalar](https://learn.microsoft.com/en-us/purview/deploy-scanner-configure-install)). Limitación: el volumen y el rendimiento no se parecen a un recurso real y NFS está en vista previa.
3. `Laboratorio parcial` En el mismo trabajo, activa el etiquetado automático con una condición de SIT y una etiqueta sin cifrado, vuelve a escanear y compara los resultados ([escáner](https://learn.microsoft.com/en-us/purview/deploy-scanner)). Limitación: el escáner no etiqueta en tiempo real; documenta la duración de cada ciclo.
4. `Laboratorio` Con la [guía de migración](https://learn.microsoft.com/en-us/defender-cloud-apps/migrate-file-policies-to-purview) y la tabla de este módulo, arma el plan de tu organización: cada directiva de archivo o caso de uso de Defender for Cloud Apps, su reemplazo en Purview, si la herramienta lo migra, el responsable y una fecha anterior al 6 de enero de 2027.
5. `Solo producción` Migra las directivas de archivo con la herramienta. Requiere directivas existentes de Defender for Cloud Apps, conectores de apps reales y un entorno comercial de producción. Forma segura: deja las políticas de Purview en modo de prueba con notificaciones («Test with notifications»), con un piloto pequeño, y deshabilita (no borres) la directiva original hasta validar ([guía de migración](https://learn.microsoft.com/en-us/defender-cloud-apps/migrate-file-policies-to-purview)).
6. `Solo producción` Escanea un recurso compartido real: primero en modo solo descubrimiento sobre una carpeta acotada, con una cuenta de servicio de permisos mínimos y en una ventana acordada. Forma segura: pasa a etiquetar, y siempre sin cifrado al principio, solo con el visto bueno del dueño de la aplicación que usa esos archivos.

**¿Quieres profundizar?**

- [Download Microsoft Purview Information Protection client (Download Center)](https://www.microsoft.com/en-sa/download/details.aspx?id=53018) · Herramienta
- [MC775357 - Reminder: Azure Information Protection Add-in for Office is retired](https://mc.merill.net/message/MC775357) · Blog

<a id="reto-intermedio"></a>

## Reto del nivel

**Un proyecto confidencial protegido de punta a punta.** Para un proyecto ficticio de fusión: crea el equipo con la etiqueta de contenedor Altamente confidencial, define la etiqueta predeterminada de su biblioteca, publica una etiqueta cifrante (Coautor para el equipo interno y Revisor para un asesor externo del segundo tenant), etiqueta las reuniones del proyecto, corre en simulación una política de auto-etiquetado con un SIT del proyecto y protege un informe de Power BI. Suma el escáner en modo solo descubrimiento sobre una carpeta heredada del proyecto y el plan de migración de Defender for Cloud Apps. Entrega el diagrama, la tabla de pruebas por persona, los resultados de la simulación y el plan de reversión.

<a id="quiz-intermedio"></a>

## Evaluación del nivel

Responde y compara con [Evaluaciones y respuestas](06_Evaluaciones_y_respuestas.md#eval-intermedio). Con 80 % o más, ¡nivel aprobado! (En la versión web puedes corregir en línea y generar tu certificado).

1. ¿Cuál es el techo del auto-etiquetado en servicio para SharePoint y OneDrive desde agosto de 2026?
   - a) 25.000 archivos por día
   - b) 100.000 archivos por día
   - c) 500.000 archivos por día
   - d) Sin límite diario

2. ¿Sobre qué correo actúa el auto-etiquetado en servicio de Exchange?
   - a) Sobre el correo en tránsito
   - b) Sobre todos los buzones en reposo
   - c) Solo sobre carpetas públicas
   - d) Sobre archivos PST importados

3. La pestaña Insights de una política de auto-etiquetado en modo de aplicación muestra métricas de 30 días para…
   - a) Exchange y Teams
   - b) Endpoints con Windows
   - c) Activos de Data Map
   - d) Solo SharePoint y OneDrive

4. ¿Qué agrega la política especial de MC1477181 (22 de septiembre de 2026)?
   - a) El etiquetado de buzones de Exchange en reposo, con hasta 10 buzones por política
   - b) Aplicar la etiqueta predeterminada de biblioteca a archivos existentes sin etiqueta (una política por tenant y hasta 10 sitios)
   - c) El auto-etiquetado de reuniones de Teams a partir de la etiqueta de contenedor del equipo, sin Teams Premium
   - d) El cifrado con DKE de bibliotecas completas de SharePoint mediante la etiqueta predeterminada de biblioteca

5. ¿Qué afirmación sobre el escáner de Information Protection es correcta?
   - a) Etiqueta en tiempo real cada archivo que se guarda
   - b) Solo admite recursos NFS y ya en disponibilidad general
   - c) Rastrea por ciclos y admite un modo solo descubrimiento
   - d) No admite bibliotecas de SharePoint Server

6. ¿Qué nivel de permisos de Rights Management incluye el derecho EXTRACT (Copiar)?
   - a) Visor
   - b) Revisor
   - c) Ninguno: EXTRACT solo se concede por PowerShell
   - d) Coautor

7. Con Advanced Message Encryption, ¿qué correos se pueden revocar?
   - a) Los entregados por el portal de OME con una plantilla de marca personalizada
   - b) Cualquier correo cifrado, incluso si el destinatario lo recibió de forma nativa en Outlook
   - c) Solo los correos internos cifrados con Encrypt-Only
   - d) Solo los correos cifrados con DKE desde Outlook para Windows

8. ¿Cuál es el estado predeterminado de la característica de superusuario de Rights Management?
   - a) Habilitada para todos los Global Administrators
   - b) Deshabilitada; se habilita cuando hace falta y se audita
   - c) Habilitada solo para el contenido cifrado con DKE
   - d) Habilitada de forma permanente para el grupo Information Protection Admins

9. Ya no quieres usar una etiqueta que cifra. ¿Qué conviene hacer?
   - a) Eliminarla y borrar su plantilla de protección
   - b) Cambiarle el nombre a Público
   - c) Quitarla de la política de etiquetas
   - d) Eliminarla y crearla de nuevo con el mismo nombre

10. Sobre las etiquetas para reuniones de Teams, ¿qué es cierto?
   - a) Admiten auto-etiquetado a partir del contenido de la invitación
   - b) Pueden usar DKE para cifrar la invitación y el chat
   - c) Aplican también a los eventos en vivo de Teams
   - d) Varias opciones de reunión requieren Teams Premium

11. ¿Qué licencias se requieren para aplicar etiquetas a elementos de Power BI?
   - a) Solo Power BI gratuito, porque la etiqueta no restringe el acceso
   - b) AIP Premium P1 o P2 (incluidas en las suites) más Power BI Pro o PPU
   - c) Solo Teams Premium para las personas que crean informes
   - d) Una capacidad F64, sin licencias por usuario

12. ¿Cómo funcionan hoy las etiquetas en Data Map?
   - a) Solo auto-etiquetado como metadatos del activo, en vista previa y con pago por uso para orígenes no Microsoft 365
   - b) Cifran los archivos de origen en Azure Storage y Amazon S3 con Rights Management
   - c) Admiten etiquetado manual y automático, con las mismas marcas de contenido que Office
   - d) Están en disponibilidad general e incluidas en Microsoft 365 E3 sin costo adicional

13. Aplicas la etiqueta de contenedor Altamente confidencial a un equipo de Teams. ¿Qué pasa con los archivos del equipo?
   - a) Heredan la etiqueta y se cifran
   - b) Se mueven a una biblioteca protegida
   - c) No heredan la etiqueta del contenedor
   - d) Se cifran con DKE

14. ¿Cuándo se retiran las directivas de archivo de Defender for Cloud Apps?
   - a) El 11 de abril de 2024
   - b) El 6 de enero de 2027
   - c) El 31 de marzo de 2027
   - d) El 1 de octubre de 2026

15. ¿Qué hace hoy la herramienta de migración de directivas de archivo de Defender for Cloud Apps?
   - a) Migra todas las directivas, incluidas las de apps no Microsoft, a políticas de auto-etiquetado
   - b) Solo funciona en nubes gubernamentales y soberanas, como paso previo al retiro
   - c) Convierte las directivas en políticas de cifrado de Customer Key para SharePoint
   - d) Convierte las directivas de SharePoint y OneDrive en DLP o auto-etiquetado de Purview; las de apps no Microsoft, todavía no

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. No es asesoría legal: las decisiones sobre datos personales deben validarse con Legal y Privacidad. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

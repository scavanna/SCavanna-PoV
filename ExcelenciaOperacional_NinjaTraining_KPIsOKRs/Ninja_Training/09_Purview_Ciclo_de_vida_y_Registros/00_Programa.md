# Programa: cómo usar, justificación, rutas y plan

*Microsoft Purview Ciclo de vida de los datos y Gestión de registros Ninja Training · Edición 2026*

[Índice del programa](README.md) · [Nivel 1 · Inicial →](01_Nivel_1_Inicial.md)

<a id="como-usar"></a>

## Cómo usar esta guía

¿Quieres convertirte en Ninja del ciclo de vida de los datos y la gestión de registros en Microsoft Purview? Esta guía te lleva de los principios de retención a un programa de registros que resiste una auditoría. Reúne, ordenados como un curso, la documentación de Microsoft Learn, los anuncios del equipo de producto, los webinars de la Microsoft Security Community y el trabajo de MVPs y empleados de Microsoft que enseñan retención y registros todos los días.

Puedes seguirla de punta a punta o por tu rol: gestión de registros, cumplimiento, Legal, privacidad, dueños de datos o administración de Exchange, SharePoint y Teams. Cada nivel cierra con una evaluación y, si alcanzas el 80 %, puedes generar tu certificado de finalización. Y como la retención ya no termina en el correo y los archivos, el recorrido llega hasta las interacciones con Copilot y otras apps de IA, la automatización con Microsoft Graph y el gobierno con Legal y privacidad en MCSA (México, Centroamérica y Sudamérica).

**Estructura.** Tres niveles técnicos —Inicial (L100–L200), Intermedio (L300) y Avanzado (L400)—, un nivel de Operación (L300–L400) para quienes dirigen el programa y una sección transversal de comunidad: 18 módulos en total. Los niveles inicial e intermedio reconstruyen las secciones del Ninja oficial de 2023 actualizadas a noviembre de 2026; el nivel avanzado y el de operación son la ampliación de esta edición (IA, APIs, holds, regulación, métricas y gobierno).

**Cada módulo** sigue la forma Ninja: una introducción que explica qué es y por qué importa, la justificación de negocio, lo que vas a lograr, las novedades y advertencias con fecha y fuente, una ruta rápida (*¿Tienes poco tiempo?*), los recursos agrupados por tipo, una práctica guiada y etiquetada (*Manos a la obra*) y lecturas para ir más allá.

**Evaluación y certificado.** Los niveles Inicial, Intermedio, Avanzado y Operación cierran con una evaluación de opción múltiple con la explicación y la fuente de cada respuesta, y con un reto integrador. Con 80 % o más puedes generar un certificado de finalización. Es una autoevaluación de esta guía, no una certificación de Microsoft: para eso están el examen SC-401 y la credencial Applied Skills de retención, eDiscovery y Communication Compliance.

**Laboratorio.** Cada ejercicio indica dónde se puede hacer: `[LAB]` completo en una prueba de Microsoft 365 E5 con una suscripción de Azure; `[LAB-PARCIAL]` con limitaciones que se explican; `[SOLO-PRODUCCION]` cuando requiere licencias, volumen o usuarios reales, con la forma segura de practicarlo. En este programa hay acciones irreversibles —eliminar, declarar registros regulatorios, bloquear directivas, habilitar el archivo de expansión automática— reunidas en [Acciones irreversibles](#irreversibles).

**Fechas y estados.** Cada dato tiene su fuente y su fecha de corte: 6 de noviembre de 2026. Microsoft Ignite se realiza del 17 al 20 de noviembre de 2026 y puede cambiar estados de vista previa; muchas funciones de este programa tardan hasta 7 días en verse, así que planifica ventanas de espera. Las contradicciones que encontró la investigación están en [puntos a confirmar](08_Cierre_glosario_y_fuentes.md#metodologia).

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

**Por qué ahora.** Entre 2025 y 2026 la retención cambió de alcance: las interacciones con Copilot, ChatGPT Enterprise o Claude Enterprise son contenido que hay que retener o eliminar con criterio; los canales privados de Teams pasaron a buzones de grupo; los registros de llamadas salieron de las directivas de chat; llegaron la limpieza prioritaria con triple aprobación, el delay hold de 30 días para buzones inactivos, los archivos de 3 TB, Azure PST Import y la acción de archivo hacia Microsoft 365 Archive. En la región, México renovó su ley de datos personales en 2025 y reformó su Ley General de Archivos, y Chile aplica su Ley 21.719 desde el 1 de diciembre de 2026. Un equipo formado con el Ninja de 2023 usa nombres de ubicaciones que ya no existen y no ve la IA.

**Qué gana la organización.** Resultados medibles: porcentaje de ubicaciones con directiva de base, porcentaje de categorías del plan de archivos con etiqueta aplicada, antigüedad del backlog de revisión de eliminación, prueba de eliminación exportada cada mes, reducción de la deuda de retención (buzones y OneDrive de exempleados retenidos sin plazo), costo de almacenamiento (Microsoft 365 Archive frente a más cuota), tiempo de respuesta a una retención legal y cero eliminaciones sin aprobación. Cada nivel deja entregables reutilizables: matriz de retención, plan de archivos, runbooks, scripts y un tablero.

**Para quién.** Gestores de registros, oficiales de cumplimiento, asesoría legal, oficiales de privacidad, dueños de datos de las áreas de negocio y administradores de Exchange, SharePoint y Teams. Las [rutas por rol](#rutas) permiten que cada perfil recorra solo lo que necesita, con un tronco común en el nivel inicial.

**Cómo se conecta con el resto de la serie.** Este es uno de los ocho programas de Purview, porque cada capacidad la operan equipos distintos por razones distintas. Los holds, las búsquedas y la auditoría se profundizan en el programa de **eDiscovery y Audit**; la clasificación (SIT y clasificadores) y las etiquetas de confidencialidad, en **Information Protection**; Copilot y los agentes, en **DSPM y seguridad de datos para IA**; el mapeo de controles, en **Compliance Manager**; y los conectores de datos de terceros, en **Communication Compliance**. Los roles privilegiados y las unidades administrativas se apoyan en **Entra**, y las señales de auditoría llegan al SOC de **Sentinel** y **Defender XDR**.

<a id="licencias"></a>

## Licencias: qué incluye Microsoft 365 E3, qué exige E5 y qué se paga aparte

La retención de base está en Microsoft 365 E3 (y en Office 365 E3 y Business Premium): directivas estáticas y etiquetas de aplicación manual. Todo lo que convierte la retención en gestión de registros —ámbitos adaptables, autoaplicación, etiquetas predeterminadas de SharePoint, plan de archivos, eventos, registros, revisión de eliminación y limpieza prioritaria— exige nivel E5: Microsoft 365 E5, Office 365 E5 (con la excepción de los clasificadores entrenables), Microsoft Purview Suite —el antiguo Microsoft 365 E5 Compliance, complemento sobre E3— o el complemento E5 Information Protection & Governance (IP&G).

Aparte del plan por usuario, Purview factura por consumo a través de una suscripción de Azure vinculada al tenant: lo exigen las ubicaciones de IA, las directivas de recopilación y Microsoft 365 Archive. La descripción del servicio es la fuente autorizada; esta tabla resume la investigación al 6 de noviembre de 2026 y marca lo que no se pudo confirmar.

**Licencias de ciclo de vida de los datos y gestión de registros**

| Capacidad | Microsoft 365 E3 | Microsoft 365 E5 / E5 Compliance (hoy Purview Suite) | Complemento o pago por uso | Fuente |
|---|---|---|---|---|
| Directivas de retención estáticas (Exchange, SharePoint, OneDrive, Grupos, Teams, Viva Engage) | Sí (también Office 365 E3 y Business Premium) | Sí | No requiere | [Descripción del servicio](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description) |
| Crear y publicar etiquetas de retención para aplicación manual | Sí (también F3 y F1) | Sí | No requiere | [Descripción del servicio](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description) |
| Ámbitos adaptables | No | Sí (también Office 365 E5, A5 y G5) | Purview Suite o IP&G sobre E3 | [Descripción del servicio](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description) |
| Autoaplicar etiquetas por SIT, palabras clave o propiedades (KQL) | No | Sí (también Office 365 E5) | Purview Suite o IP&G | [Descripción del servicio](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description) |
| Autoaplicar etiquetas con clasificadores entrenables | No | Sí en Microsoft 365 E5, A5 y G5 (Office 365 E5 no figura en esta fila) | Purview Suite, IP&G o Defender + Purview Suite FLW | [Descripción del servicio](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description) |
| Etiquetas predeterminadas de SharePoint y plan de archivos | No | Sí | Purview Suite o IP&G | [Descripción del servicio](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description) |
| Retención basada en eventos | No | Sí | Purview Suite o IP&G | [Descripción del servicio](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description) |
| Declarar registros y registros regulatorios | No | Sí | Purview Suite o IP&G | [Descripción del servicio](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description) |
| Revisión de eliminación, prueba de eliminación y reetiquetado al final del período | No | Sí | Purview Suite o IP&G | [Descripción del servicio](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description) |
| Limpieza prioritaria (vista previa) | No | Sí | Purview Suite o IP&G; se puede desactivar para todo el tenant | [Descripción del servicio](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description), [limpieza prioritaria](https://learn.microsoft.com/en-us/purview/priority-cleanup-exchange) |
| Retener interacciones de Microsoft 365 Copilot | Sí, con licencia de Microsoft 365 Copilot (ámbitos estáticos) | Sí, con Microsoft 365 Copilot; suma ámbitos adaptables y la retención de la versión exacta del documento compartido | E3 + Purview Suite o IP&G + Copilot para las funciones de nivel E5; pago por uso activo, sin cargo por las interacciones de Microsoft 365 Copilot | [Descripción del servicio](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description), [primeros pasos con DLM](https://learn.microsoft.com/en-us/purview/get-started-with-data-lifecycle-management) |
| Retener Enterprise AI apps y Other AI apps | Con pago por uso (sin requisito de plan por usuario documentado) | Con pago por uso | Pago por uso y directiva de recopilación; agentes de Microsoft Foundry y apps de IA conectadas a Entra: Microsoft 365 E7 o SKU de Agent 365, según la descripción del servicio | [Retención para Copilot e IA](https://learn.microsoft.com/en-us/purview/retention-policies-copilot), [directivas de recopilación](https://learn.microsoft.com/en-us/purview/collection-policies-solution-overview) |
| Buzones inactivos | Sí; el buzón inactivo no requiere licencia (necesita retención o hold previo) | Sí | No requiere | [Buzones inactivos](https://learn.microsoft.com/en-us/purview/inactive-mailboxes-in-office-365) |
| Archivo de expansión automática | Hasta 1,5 TB | Hasta 3 TB desde mediados de octubre de 2026 si el plan Records Management de la licencia está habilitado (la descripción del servicio aún dice 1,5 TB) | Purview Suite, F5 Compliance o E7 también habilitan 3 TB | [Archivo de expansión automática](https://learn.microsoft.com/en-us/purview/autoexpanding-archiving) |
| Tamaño de buzones compartidos | 50 GB sin licencia en el buzón compartido | Igual que E3 | 100 GB con Exchange Online Plan 2, o con Exchange Online Archiving más Plan 1 | [Descripción del servicio](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description) |
| Importación de PST | Carga por red sin costo adicional | Igual que E3 | Envío de discos con costo y solo con Enterprise Agreement; Azure PST Import (vista previa) usa tu propio Azure Blob Storage | [Importación de PST](https://learn.microsoft.com/en-us/purview/pst-import-overview), [MC1281505](https://mc.merill.net/message/MC1281505) |
| Microsoft 365 Archive (sitios y archivos de SharePoint) | No incluido | No incluido | Pago por uso: USD 0,05 por GB al mes solo por encima de la cuota; reactivación sin cargo desde el 31 de marzo de 2025 (no aplica a OneDrive) | [Precios de Microsoft 365 Archive](https://learn.microsoft.com/en-us/microsoft-365/archive/archive-pricing?view=o365-worldwide) |

Fuentes: [descripción del servicio de Microsoft Purview](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description), [precios de Microsoft Purview](https://www.microsoft.com/en-us/security/microsoft-purview-pricing) (Purview Suite, antes E5 Compliance, requiere Microsoft 365 E3) y [modelos de facturación](https://learn.microsoft.com/en-us/purview/purview-billing-models). Datos al 6 de noviembre de 2026; ante diferencias, prevalece la descripción del servicio vigente.

<a id="matriz-retencion"></a>

## Matriz de retención por carga de trabajo

Qué admite cada ubicación: directiva de retención, etiqueta, autoaplicación y ámbito adaptable, con la licencia mínima. Úsala como plantilla para documentar el estado de tu tenant en el módulo [I2](01_Nivel_1_Inicial.md#i2). Las celdas «No verificado» son puntos que la investigación no pudo confirmar en fuentes oficiales: pruébalos en tu laboratorio antes de diseñar sobre ellos.

**Matriz de retención por carga de trabajo (noviembre de 2026)**

| Ubicación | Directiva | Etiqueta | Autoaplicación | Ámbito adaptable | Licencia | Fuente | Módulo |
|---|---|---|---|---|---|---|---|
| Buzones de Exchange | Sí | Sí | Sí | Sí (usuarios) | E3 o superior; autoaplicación y ámbitos adaptables con nivel E5 | [Crear directivas](https://learn.microsoft.com/en-us/purview/create-retention-policies) | [I2](01_Nivel_1_Inicial.md#i2), [M1](02_Nivel_2_Intermedio.md#m1) |
| Carpetas públicas de Exchange | Sí | No verificado | No verificado | No verificado | E3 o superior | [Crear directivas](https://learn.microsoft.com/en-us/purview/create-retention-policies) | [I2](01_Nivel_1_Inicial.md#i2) |
| Sitios de SharePoint (incluidos sitios archivados, Loop y Copilot Pages) | Sí | Sí, también como etiqueta predeterminada | Sí | Sí (sitios) | E3 o superior; etiquetas predeterminadas y autoaplicación con nivel E5 | [SharePoint y OneDrive](https://learn.microsoft.com/en-us/purview/retention-policies-sharepoint) | [I2](01_Nivel_1_Inicial.md#i2), [M1](02_Nivel_2_Intermedio.md#m1) |
| Cuentas de OneDrive | Sí | Sí | Sí | Sí (usuarios) | E3 o superior; autoaplicación y ámbitos adaptables con nivel E5 | [SharePoint y OneDrive](https://learn.microsoft.com/en-us/purview/retention-policies-sharepoint) | [I2](01_Nivel_1_Inicial.md#i2) |
| Grupos de Microsoft 365 | Sí | Sí | Sí | Sí (grupos) | E3 o superior; autoaplicación y ámbitos adaptables con nivel E5 | [Crear directivas](https://learn.microsoft.com/en-us/purview/create-retention-policies) | [I2](01_Nivel_1_Inicial.md#i2) |
| Mensajes de canales de Teams (estándar, compartidos y privados tras la migración) | Sí | No | No | Sí | E3/F3 o superior | [Retención en Teams](https://learn.microsoft.com/en-us/purview/retention-policies-teams) | [I2](01_Nivel_1_Inicial.md#i2), [A3](03_Nivel_3_Avanzado.md#a3) |
| Chats de Teams | Sí | No | No | Sí | E3/F3 o superior | [Retención en Teams](https://learn.microsoft.com/en-us/purview/retention-policies-teams) | [I2](01_Nivel_1_Inicial.md#i2) |
| Registros de llamadas de Teams | Sí, solo con PowerShell (desde abril de 2026) | No | No | No verificado | E3 o superior | [Crear directivas](https://learn.microsoft.com/en-us/purview/create-retention-policies) | [I2](01_Nivel_1_Inicial.md#i2) |
| Grabaciones y transcripciones de reuniones | A través de OneDrive o SharePoint | Sí | Sí | Sí | E3 o superior; autoaplicación con nivel E5 | [Autoaplicación](https://learn.microsoft.com/en-us/purview/apply-retention-labels-automatically) | [I2](01_Nivel_1_Inicial.md#i2), [M1](02_Nivel_2_Intermedio.md#m1) |
| Viva Engage (mensajes de usuarios y comunidades) | Sí | No | No | Sí | E3 o superior | [Retención en Viva Engage](https://learn.microsoft.com/en-us/purview/retention-policies-viva-engage) | [I2](01_Nivel_1_Inicial.md#i2) |
| Microsoft Copilot experiences | Sí | No | No | Sí | E3/E5 + Microsoft 365 Copilot; pago por uso activo, sin cargo para Microsoft 365 Copilot; ámbitos adaptables con nivel E5 | [Retención para Copilot e IA](https://learn.microsoft.com/en-us/purview/retention-policies-copilot) | [A1](03_Nivel_3_Avanzado.md#a1) |
| Enterprise AI apps | Sí, con directiva de recopilación | No | No | Sí | Pago por uso; agentes de Microsoft Foundry: E7 o Agent 365 | [Retención para Copilot e IA](https://learn.microsoft.com/en-us/purview/retention-policies-copilot) | [A1](03_Nivel_3_Avanzado.md#a1) |
| Other AI apps | Sí, con directiva de recopilación | No | No | Sí | Pago por uso | [Retención para Copilot e IA](https://learn.microsoft.com/en-us/purview/retention-policies-copilot) | [A1](03_Nivel_3_Avanzado.md#a1) |
| Skype Empresarial | Sí | No | No | No verificado | E3 o superior | [Crear directivas](https://learn.microsoft.com/en-us/purview/create-retention-policies) | [I2](01_Nivel_1_Inicial.md#i2) |
| Tareas de Planner | Sí, desde julio–agosto de 2026 (fuente comunitaria) | No | No | No verificado | No verificado | [Planner (comunidad)](https://office365itpros.com/2026/07/28/planner-tasks-retention/) | [I2](01_Nivel_1_Inicial.md#i2) |

Fuente principal: sección de matriz de la investigación de este programa, basada en [crear directivas de retención](https://learn.microsoft.com/en-us/purview/create-retention-policies), las páginas de retención por carga de trabajo y la [descripción del servicio](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description). En directivas estáticas, elegir Teams o Viva Engage excluye el resto de las ubicaciones; con ámbitos adaptables, una sola directiva puede incluir Teams y Viva Engage.

<a id="plan-archivos"></a>

## Plan de archivos de ejemplo

**Ejemplo didáctico, no asesoría legal.** Esta tabla muestra cómo se ve un plan de archivos bien construido —categorías claras, un disparador y una acción al final para cada etiqueta, el tipo de registro y un dueño—, para que practiques en el laboratorio y en los módulos [I3](01_Nivel_1_Inicial.md#i3), [M2](02_Nivel_2_Intermedio.md#m2) y [M3](02_Nivel_2_Intermedio.md#m3). Los períodos son ilustrativos: los reales deben salir de la tabla de retención documental de tu organización, validada por Legal, archivo y privacidad frente a la normativa que te aplique (por ejemplo, la Ley General de Archivos de México o la tabla de retención documental de la Ley 594 de 2000 en Colombia).

Fíjate en el diseño: pocas categorías amplias en lugar de cientos de series, revisión de eliminación solo donde aporta valor, registro regulatorio únicamente cuando una norma exige inmutabilidad y las directivas de retención como base para el contenido que no es registro.

**Plan de archivos de ejemplo (períodos ilustrativos; no es asesoría legal)**

| Categoría (función · serie) | Etiqueta de retención | Período | Inicio del período | Acción al final | Tipo de registro | Dueño |
|---|---|---|---|---|---|---|
| Legal · Contratos con clientes y proveedores | LEG-Contratos | 10 años (ilustrativo) | Evento «Fin de contrato» (ID de activo = número de contrato) | Revisión de eliminación en dos etapas: dueño del contrato y Legal | Registro bloqueado | Legal |
| Recursos humanos · Expediente del empleado | RH-Expediente | 5 años (ilustrativo) | Evento «Baja del empleado» (ID de activo = número de empleado) | Revisión de eliminación: RR. HH. y privacidad | Registro bloqueado | Recursos humanos |
| Finanzas · Facturas y comprobantes contables | FIN-Comprobantes | 7 años (ilustrativo) | Fecha de creación | Eliminar automáticamente | Registro bloqueado | Finanzas |
| Gobierno corporativo · Actas de directorio | GOB-Actas | Permanente | Fecha de creación | Ninguna: se conserva para siempre | Registro bloqueado | Secretaría corporativa |
| Gobierno corporativo · Políticas y procedimientos vigentes | GOB-Politicas | 5 años (ilustrativo) | Fecha de la última modificación | Revisión de eliminación por el dueño de la política | Registro desbloqueado con versionado | Cumplimiento |
| Cumplimiento · Operaciones sujetas a norma que exige inmutabilidad | REG-Operaciones | Plazo de la norma aplicable (ilustrativo: 6 años) | Fecha de creación | Eliminar automáticamente al vencer | Registro regulatorio (irreversible) | Cumplimiento |
| Clientes · Expediente de conocimiento del cliente | CLI-Expediente | 10 años (ilustrativo) | Evento «Fin de la relación con el cliente» | Revisión de eliminación: operaciones y cumplimiento | Registro bloqueado | Operaciones |
| Proyectos · Documentación de proyecto | OPS-Proyectos | 3 años (ilustrativo) | Evento «Cierre del proyecto» | Mover a Microsoft 365 Archive y luego eliminar (acción en vista previa) | Etiqueta estándar (no es registro) | Oficina de proyectos |
| Contenido transitorio · Correo, chats y archivos de trabajo | Sin etiqueta: directiva de retención de base | 3 años (ilustrativo) | Fecha de creación o de última modificación | Eliminar automáticamente | No aplica | TI y cumplimiento |
| IA · Interacciones con Copilot y apps de IA | Directiva de la ubicación Microsoft Copilot experiences | 1 año (ilustrativo) | Fecha de creación | Eliminar automáticamente (un hold la suspende) | No aplica | Cumplimiento y privacidad |

Basado en las capacidades descritas en [plan de archivos](https://learn.microsoft.com/en-us/purview/file-plan-manager), [registros](https://learn.microsoft.com/en-us/purview/records-management), [retención basada en eventos](https://learn.microsoft.com/en-us/purview/event-driven-retention) y [revisión de eliminación](https://learn.microsoft.com/en-us/purview/disposition). Ejemplo didáctico: los períodos, disparadores y tipos de registro deben definirse con Legal y privacidad.

<a id="irreversibles"></a>

## Acciones irreversibles o de alto impacto

En retención y registros hay acciones que no se pueden deshacer. Esta tabla las reúne con la forma segura de practicarlas; en producción, cada una debería pasar por control de cambios con aprobación de Legal o del comité de retención.

**Acciones irreversibles o de alto impacto**

| Acción | Por qué es crítica | Cómo practicarla con seguridad | Módulo |
|---|---|---|---|
| Eliminación al final del período (automática o tras la revisión) | Pasados los plazos de papelera y de Recoverable Items, el contenido no se recupera; la prueba de eliminación solo deja constancia | Etiquetas piloto sobre documentos de prueba, períodos cortos y revisión de eliminación antes de habilitar eliminaciones automáticas en producción | [M2](02_Nivel_2_Intermedio.md#m2) |
| Etiqueta de registro regulatorio | Nadie puede quitarla ni cambiarla, y el contenido no se puede editar ni eliminar | Solo en un tenant desechable; en producción, aprobación de Legal y cumplimiento y piloto con documentos de prueba | [I3](01_Nivel_1_Inicial.md#i3), [A4](03_Nivel_3_Avanzado.md#a4) |
| Preservation Lock en una directiva | La directiva no se puede desactivar, eliminar ni hacer menos restrictiva | Solo ante un requisito regulatorio documentado; prueba previa en un tenant desechable | [A4](03_Nivel_3_Avanzado.md#a4) |
| Archivo de expansión automática | No se puede desactivar e impide recuperar o restaurar buzones inactivos | Piloto con usuarios aprobados y verificación por PowerShell, sin habilitarlo para toda la organización | [M4](02_Nivel_2_Intermedio.md#m4) |
| Limpieza prioritaria | Elimina de forma permanente aunque haya retención, holds o Preservation Lock (no afecta a registros) | Buzón de prueba, simulación, tres aprobadores distintos y seguimiento en auditoría por su ID | [M2](02_Nivel_2_Intermedio.md#m2) |
| Quitar la última inclusión de una directiva estática de eliminación | La directiva vuelve a aplicarse a «Todos» y puede eliminar contenido de toda la organización | Revisión por pares antes de guardar, inclusiones documentadas y preferencia por ámbitos adaptables | [I1](01_Nivel_1_Inicial.md#i1) |
| Cerrar un caso o liberar el único hold de un buzón inactivo | El buzón inactivo se elimina (desde agosto de 2026, después de un delay hold de 30 días) | Antes de liberar, listar los buzones inactivos que dependen del hold y acordar con Legal y registros | [A3](03_Nivel_3_Avanzado.md#a3), [M4](02_Nivel_2_Intermedio.md#m4) |

Fuentes: [revisión de eliminación](https://learn.microsoft.com/en-us/purview/disposition), [registros](https://learn.microsoft.com/en-us/purview/records-management), [retención](https://learn.microsoft.com/en-us/purview/retention), [archivo de expansión automática](https://learn.microsoft.com/en-us/purview/enable-autoexpanding-archiving), [limpieza prioritaria](https://learn.microsoft.com/en-us/purview/priority-cleanup-exchange), [configuración común](https://learn.microsoft.com/en-us/purview/retention-settings) y [duración del hold de buzones inactivos](https://learn.microsoft.com/en-us/purview/change-the-hold-duration-for-an-inactive-mailbox).

<a id="formato"></a>

## El formato Ninja: historia y familia

El Ninja oficial de ciclo de vida de los datos y gestión de registros se publicó el 25 de julio de 2023 en la Microsoft Security Community de Tech Community ([anuncio](https://techcommunity.microsoft.com/discussions/microsoft-security/new-blog--become-a-microsoft-purview-data-lifecycle-and-records-management-ninja/3883998)), firmado por BrittanyCCP, hoy identificada como exempleada. Formaba parte de la serie de Ninjas de cumplimiento de ese mes, junto con el de Priva del 18 de julio. A diferencia del Ninja de Sentinel, no estaba organizado en niveles numerados sino en secciones: introducción, primeros pasos, licencias y permisos, retención y sus principios, cargas de trabajo, otros usos de las etiquetas, plan de archivos, eventos, registros, autoaplicación, ámbitos adaptables, unidades administrativas, fin de la retención, eliminación, Power Automate, monitoreo, funciones heredadas, Syntex y examen. Una [copia sindicada](https://thewindowsupdate.com/2023/07/25/become-a-microsoft-purview-data-lifecycle-and-records-management-ninja/) permite ver la estructura completa.

Ese Ninja no tenía evaluación ni certificado: recomendaba el examen SC-400, que hoy es SC-401. Su última actualización visible es de 2023 y el enlace corto aka.ms/DLM/NinjaTraining, citado en 2024, ya no se pudo resolver. Mientras tanto la familia cambió de formato: otros Ninjas de Purview usaban knowledge checks con certificado de participación ([Compliance Manager Ninja](https://techcommunity.microsoft.com/blog/microsoft-security-blog/microsoft-purview-compliance-manager-mspcm-ninja-training-q1-2023/3181322)), el de Information Protection se retiró de Tech Community en julio de 2025 y se trasladó en agosto ([aviso de retiro](https://techcommunity.microsoft.com/blog/microsoft-security-blog/retired-the-microsoft-purview-information-protection-ninja-training-is-here/2887478/replies/4014737)), y Microsoft Learn publica ahora rutas «Ninja training scenarios» con insignia ([ruta de escenarios](https://learn.microsoft.com/en-us/training/paths/purview-ninja-safeguard-data/)).

Esta edición respeta la forma Ninja —módulos con introducción, recursos curados y práctica— y le agrega lo que faltaba: niveles con evaluación al 80 % y reto, un nivel de operación, ejercicios etiquetados según dónde se pueden practicar, tablas de referencia (licencias, matriz de retención, plan de archivos de ejemplo y acciones irreversibles) y todo lo que llegó después de 2023: IA, archivo e importación, holds en la experiencia unificada de eDiscovery, regulación regional y métricas.

**La familia Ninja relacionada**

| Ninja | Qué cubre | Estado y última actualización |
|---|---|---|
| [Become a Microsoft Purview Data Lifecycle and Records Management Ninja](https://techcommunity.microsoft.com/discussions/microsoft-security/new-blog--become-a-microsoft-purview-data-lifecycle-and-records-management-ninja/3883998) | Retención, plan de archivos, eventos, registros, autoaplicación, ámbitos adaptables, eliminación, Power Automate y Syntex | Publicado el 25 de julio de 2023; sin actualizaciones visibles desde entonces; sin evaluación |
| [Become a Microsoft Priva Ninja](https://techcommunity.microsoft.com/discussions/microsoft-security/new-blog--become-a-microsoft-priva-ninja/3877925) | Priva (privacidad) en niveles principiante, intermedio y avanzado | 18 de julio de 2023; misma serie de cumplimiento |
| [Become a Microsoft 365 Advanced eDiscovery Ninja](https://techcommunity.microsoft.com/discussions/microsoft-security/new-blog-post--become-a-microsoft-365-advanced-ediscovery-ninja/2810216) | eDiscovery en ocho secciones alineadas al modelo EDRM, con knowledge check por nivel | 2021; el Ninja de eDiscovery sigue activo en el [índice de Ninjas de Tech Community](https://techcommunity.microsoft.com/tag/ninja%20training), con mayo de 2026 como fecha más reciente |
| [Compliance Manager Ninja](https://techcommunity.microsoft.com/blog/microsoft-security-blog/microsoft-purview-compliance-manager-mspcm-ninja-training-q1-2023/3181322) | Compliance Manager; muestra el mecanismo de knowledge checks y certificado de participación de la familia | Primer trimestre de 2023 |
| [Information Protection Ninja](https://techcommunity.microsoft.com/blog/microsoft-security-blog/retired-the-microsoft-purview-information-protection-ninja-training-is-here/2887478/replies/4014737) | Clasificación, etiquetas de confidencialidad y cifrado | Retirado en julio de 2025 y trasladado en agosto de 2025 |
| [Secure sensitive data with Microsoft Purview Ninja training scenarios](https://learn.microsoft.com/en-us/training/paths/purview-ninja-safeguard-data/) | Information Protection y DLP por escenarios, 5 módulos con insignia en Microsoft Learn | Vigente: es el formato actual de la familia Ninja de Purview |
| [MS Cloud Explorers · índice de Ninja Training](https://mscloudexplorers.com/learn/) | Índice comunitario que reúne las guías Ninja de Microsoft en un solo lugar | Vigente (comunidad) |

**Del Ninja oficial a esta edición**

| Ninja oficial (2023) y rutas oficiales | Contenido | En esta edición |
|---|---|---|
| Introducción y primeros pasos | Qué son DLM y Records Management y cómo se despliegan | [P0](01_Nivel_1_Inicial.md#p0), [I1](01_Nivel_1_Inicial.md#i1) |
| Licencias y permisos | Planes, grupos de roles y roles de solo lectura | [P0](01_Nivel_1_Inicial.md#p0) |
| Retención y principios de retención | Directivas, etiquetas, ubicaciones y precedencia | [I1](01_Nivel_1_Inicial.md#i1) |
| Cargas de trabajo | Exchange, SharePoint, OneDrive, Teams y Yammer (hoy Viva Engage) | [I2](01_Nivel_1_Inicial.md#i2) |
| Otros usos de las etiquetas de retención | Etiquetas predeterminadas, reglas de Outlook y usos complementarios | [I3](01_Nivel_1_Inicial.md#i3), [M1](02_Nivel_2_Intermedio.md#m1) |
| Plan de archivos | Descriptores, importación y exportación | [I3](01_Nivel_1_Inicial.md#i3) |
| Retención basada en eventos | Tipos de evento, ID de activo y automatización | [M3](02_Nivel_2_Intermedio.md#m3) |
| Declarar registros | Registros, registros regulatorios y versionado | [I3](01_Nivel_1_Inicial.md#i3) |
| Aplicación automática y Syntex | SIT, palabras clave, clasificadores entrenables (Syntex no se profundiza) | [M1](02_Nivel_2_Intermedio.md#m1) |
| Ámbitos adaptables y unidades administrativas | Consultas por atributo, límites y delegación | [I1](01_Nivel_1_Inicial.md#i1), [P0](01_Nivel_1_Inicial.md#p0) |
| Fin de la retención y eliminación | Revisión de eliminación y prueba de eliminación | [M2](02_Nivel_2_Intermedio.md#m2) |
| Power Automate | Flujos al final del período de retención | [A2](03_Nivel_3_Avanzado.md#a2) |
| Monitoreo | Seguimiento de directivas y de la eliminación | [O2](04_Nivel_4_Operacion.md#o2) |
| Funciones heredadas | MRM, reglas de diario e In-Place Holds | [P0](01_Nivel_1_Inicial.md#p0), [M4](02_Nivel_2_Intermedio.md#m4) |
| Examen (SC-400) | Hoy SC-401 y la credencial Applied Skills con laboratorio | [I0](01_Nivel_1_Inicial.md#i0) |
| Rutas de Learn de retención (SC-401 y SC-5007) | Retención, recuperación, registros y eliminación con ejercicios | [I1](01_Nivel_1_Inicial.md#i1), [I3](01_Nivel_1_Inicial.md#i3), [M1](02_Nivel_2_Intermedio.md#m1), [M2](02_Nivel_2_Intermedio.md#m2) |
| Nuevo en esta edición | IA, archivo e importación, holds, regulación, operación y comunidad | [A1](03_Nivel_3_Avanzado.md#a1), [M4](02_Nivel_2_Intermedio.md#m4), [A3](03_Nivel_3_Avanzado.md#a3), [A4](03_Nivel_3_Avanzado.md#a4), [O1](04_Nivel_4_Operacion.md#o1), [O2](04_Nivel_4_Operacion.md#o2), [O3](04_Nivel_4_Operacion.md#o3), [C1](05_Comunidad.md#c1), [C2](05_Comunidad.md#c2) |

**Recursos sobre el Ninja oficial y su familia**

- [New Blog | Become a Microsoft Purview Data Lifecycle and Records Management Ninja](https://techcommunity.microsoft.com/discussions/microsoft-security/new-blog--become-a-microsoft-purview-data-lifecycle-and-records-management-ninja/3883998) · Blog oficial · Empleado de Microsoft · Legado aún útil · Ninja original · BrittanyCCP · Microsoft Tech Community (Microsoft Security Community) · 25 jul 2023. Anuncio oficial del Ninja de Data Lifecycle y Records Management que resume ambas soluciones y enlaza al blog completo con la ruta de recursos. *Nota:* Ninja oficial publicado en 2023; menciona SC-400 (reemplazado por SC-401), Yammer (hoy Viva Engage) y el portal de cumplimiento (hoy portal de Microsoft Purview). La autora figura como 'Former Employee'…
- [Secure sensitive data with Microsoft Purview Ninja training scenarios](https://learn.microsoft.com/en-us/training/paths/purview-ninja-safeguard-data/) · Curso · Oficial · Microsoft Learn. Ruta de Learn con el nuevo formato 'Ninja por escenarios' de Information Protection y DLP (5 módulos, insignia al completar), referencia del formato actual de la familia Ninja de Purview.
- [Become a Microsoft Purview Data Lifecycle and Records Management Ninja (republicación)](https://thewindowsupdate.com/2023/07/25/become-a-microsoft-purview-data-lifecycle-and-records-management-ninja/) · Blog · Comunidad · Legado aún útil · Microsoft (contenido sindicado) · TheWindowsUpdate.com (sindicación RSS del Tech Community) · 25 jul 2023. Copia íntegra sindicada del Ninja oficial de 2023 que permite ver su estructura completa: introducción, primeros pasos, retención, plan de archivos, eventos, autoaplicación, ámbitos adaptables, disposición, Power Automate, Syntex y examen. *Nota:* Espejo no oficial del blog original; usar solo para reconstruir la estructura del Ninja. Contenido de 2023 (SC-400, Yammer, compliance portal)
- [Retired: The Microsoft Purview Information Protection Ninja Training is here! (comentarios)](https://techcommunity.microsoft.com/blog/microsoft-security-blog/retired-the-microsoft-purview-information-protection-ninja-training-is-here/2887478/replies/4014737) · Blog oficial · Empleado de Microsoft · Retirado · Sarahzin_Shane · Microsoft Tech Community (Microsoft Security Community Blog) · 28 ago 2025. Muestra el retiro del Ninja de Information Protection en julio de 2025 y su traslado en agosto de 2025 a un nuevo alojamiento (aka.ms/MIPNinja), patrón probable para el resto de Ninjas de Purview. *Nota:* URL de la vista de comentarios del post original (versión 16.0, actualizada 28-ago-2025)
- [New Blog | Become a Microsoft Priva Ninja](https://techcommunity.microsoft.com/discussions/microsoft-security/new-blog--become-a-microsoft-priva-ninja/3877925) · Blog oficial · Empleado de Microsoft · Legado aún útil · BrittanyCCP · Microsoft Tech Community (Microsoft Security Community) · 18 jul 2023. Anuncio del Ninja de Priva de la misma serie 2023, organizado en niveles principiante, intermedio y avanzado, útil para comparar el formato de la familia. *Nota:* Familia Ninja de cumplimiento 2023; la autora figura hoy como 'Former Employee'

<a id="cambios"></a>

## Qué cambió y por qué importa

Cada fila remite al módulo donde se explica en detalle.

| Tema | Antes (Ninja de 2023) | Ahora (noviembre de 2026) | Módulo |
|---|---|---|---|
| Nombre de la solución | Microsoft Information Governance | Data Lifecycle Management y Records Management en el portal de Microsoft Purview | [P0](01_Nivel_1_Inicial.md#p0) |
| Portal | Centro de cumplimiento de Microsoft 365 | Portal de Microsoft Purview | [P0](01_Nivel_1_Inicial.md#p0) |
| Licencias | Microsoft 365 E5 Compliance | Microsoft Purview Suite (antes E5 Compliance) sobre E3; E7 y SKU de Agent 365 para agentes | [P0](01_Nivel_1_Inicial.md#p0), [A1](03_Nivel_3_Avanzado.md#a1) |
| Roles | Asignaciones permanentes | Asignaciones con expiración de 1 día a 2 años (julio de 2026) | [P0](01_Nivel_1_Inicial.md#p0), [O1](04_Nivel_4_Operacion.md#o1) |
| Certificación | SC-400 | SC-401, con habilidades actualizadas el 28 de octubre de 2026 | [I0](01_Nivel_1_Inicial.md#i0) |
| Yammer | Directivas para Yammer | Viva Engage: mensajes en carpetas ocultas de buzones y archivos con directivas propias | [I2](01_Nivel_1_Inicial.md#i2) |
| Canales privados de Teams | Ubicación «Teams private channel messages» en buzones de usuario | Buzones de grupo (octubre a diciembre de 2025); heredan la directiva de mensajes de canal del equipo | [I2](01_Nivel_1_Inicial.md#i2), [A3](03_Nivel_3_Avanzado.md#a3) |
| Registros de llamadas de Teams | Incluidos en las directivas de chats | Directivas «Teams call logs» creadas por PowerShell (finales de abril de 2026) | [I2](01_Nivel_1_Inicial.md#i2) |
| Tareas de Planner | Sin retención | Directivas de retención (julio–agosto de 2026, MC1384412, fuente comunitaria) | [I2](01_Nivel_1_Inicial.md#i2) |
| Copilot e IA | Ubicación combinada con los chats de Teams | Ubicaciones Microsoft Copilot experiences (noviembre de 2024), Enterprise AI apps y Other AI apps, con pago por uso | [A1](03_Nivel_3_Avanzado.md#a1) |
| IA de terceros y agentes | No existía | Anthropic Claude Enterprise (agosto de 2026), Agent 365 (mayo de 2026) y Copilot Cowork (junio de 2026) | [A1](03_Nivel_3_Avanzado.md#a1) |
| Limpieza prioritaria | No existía | Vista previa para buzones con tres aprobaciones (julio de 2026); SharePoint y OneDrive en vista previa | [M2](02_Nivel_2_Intermedio.md#m2) |
| Buzones inactivos | Al quitar el último hold, eliminación | Delay hold automático de 30 días (agosto de 2026) | [M4](02_Nivel_2_Intermedio.md#m4), [A3](03_Nivel_3_Avanzado.md#a3) |
| Archivo de expansión automática | Hasta 1,5 TB | Hasta 3 TB para licencias de nivel E5 con el plan Records Management habilitado (mediados de octubre de 2026) | [M4](02_Nivel_2_Intermedio.md#m4) |
| Importación de PST | Carga por red y envío de discos | Más Azure PST Import por PowerShell (vista previa desde octubre de 2026; GA en 2027 con fechas en conflicto) | [M4](02_Nivel_2_Intermedio.md#m4) |
| Microsoft 365 Archive | Tarifa de reactivación | Sin tarifa de reactivación desde el 31 de marzo de 2025; acción de archivo en retención (MC1325441, 2026) | [M4](02_Nivel_2_Intermedio.md#m4) |
| Holds | In-Place Holds y eDiscovery clásico | In-Place Holds retirados en 2020; eDiscovery clásico retirado en agosto de 2025; búsquedas de contenido solo para buscar y exportar desde el 16 de febrero de 2026 | [A3](03_Nivel_3_Avanzado.md#a3) |
| APIs de registros | Portal y PowerShell | Microsoft Graph v1.0: retentionLabel, filePlanDescriptor, retentionEvent y retentionEventType | [A2](03_Nivel_3_Avanzado.md#a2), [M3](02_Nivel_2_Intermedio.md#m3) |
| Automatización de eDiscovery | Cmdlets con autenticación solo de aplicación | Sin soporte desde agosto de 2026: migrar a Microsoft Graph | [A2](03_Nivel_3_Avanzado.md#a2) |
| Auditoría por script | Search-UnifiedAuditLog | API AuditLogQuery de Graph disponible (octubre de 2026); el cmdlet se retira el 15 de octubre de 2027 | [O2](04_Nivel_4_Operacion.md#o2) |
| Normativa en MCSA | Leyes de datos de primera generación | Nueva LFPDPPP de México (marzo de 2025), reforma de la Ley General de Archivos (noviembre de 2025) y Ley 21.719 de Chile vigente desde el 1 de diciembre de 2026 | [O3](04_Nivel_4_Operacion.md#o3), [A4](03_Nivel_3_Avanzado.md#a4) |
| Formato Ninja | Blog de 2023 sin evaluación | La familia de Purview migra a rutas de Learn con insignia; esta edición agrega niveles, evaluaciones y retos | [I0](01_Nivel_1_Inicial.md#i0) |

<a id="rutas"></a>

## Rutas por rol

Las horas son estimaciones de lectura y práctica.

- **Gestor de registros** (~44 h). Dueño del plan de archivos, de la revisión de eliminación y de la evidencia ante auditoría. Módulos: [P0](01_Nivel_1_Inicial.md#p0), [I1](01_Nivel_1_Inicial.md#i1), [I3](01_Nivel_1_Inicial.md#i3), [M1](02_Nivel_2_Intermedio.md#m1), [M2](02_Nivel_2_Intermedio.md#m2), [M3](02_Nivel_2_Intermedio.md#m3), [M4](02_Nivel_2_Intermedio.md#m4), [A2](03_Nivel_3_Avanzado.md#a2), [A4](03_Nivel_3_Avanzado.md#a4), [O1](04_Nivel_4_Operacion.md#o1), [O2](04_Nivel_4_Operacion.md#o2), [O3](04_Nivel_4_Operacion.md#o3).
- **Oficial de cumplimiento** (~35 h). Traduce obligaciones en controles y métricas, y coordina con Legal y auditoría. Módulos: [P0](01_Nivel_1_Inicial.md#p0), [I0](01_Nivel_1_Inicial.md#i0), [I1](01_Nivel_1_Inicial.md#i1), [I3](01_Nivel_1_Inicial.md#i3), [M2](02_Nivel_2_Intermedio.md#m2), [A1](03_Nivel_3_Avanzado.md#a1), [A3](03_Nivel_3_Avanzado.md#a3), [A4](03_Nivel_3_Avanzado.md#a4), [O1](04_Nivel_4_Operacion.md#o1), [O2](04_Nivel_4_Operacion.md#o2), [O3](04_Nivel_4_Operacion.md#o3).
- **Asesoría legal** (~30 h). Retenciones legales, interpretación regulatoria, aprobación de eliminaciones y riesgos de la IA. Módulos: [P0](01_Nivel_1_Inicial.md#p0), [I1](01_Nivel_1_Inicial.md#i1), [I3](01_Nivel_1_Inicial.md#i3), [M2](02_Nivel_2_Intermedio.md#m2), [M3](02_Nivel_2_Intermedio.md#m3), [A1](03_Nivel_3_Avanzado.md#a1), [A3](03_Nivel_3_Avanzado.md#a3), [A4](03_Nivel_3_Avanzado.md#a4), [O3](04_Nivel_4_Operacion.md#o3).
- **Administradores de Exchange, SharePoint y Teams** (~41 h). Implementan directivas, archivo, buzones inactivos, importación y automatización. Módulos: [P0](01_Nivel_1_Inicial.md#p0), [I0](01_Nivel_1_Inicial.md#i0), [I1](01_Nivel_1_Inicial.md#i1), [I2](01_Nivel_1_Inicial.md#i2), [M1](02_Nivel_2_Intermedio.md#m1), [M2](02_Nivel_2_Intermedio.md#m2), [M4](02_Nivel_2_Intermedio.md#m4), [A1](03_Nivel_3_Avanzado.md#a1), [A2](03_Nivel_3_Avanzado.md#a2), [A3](03_Nivel_3_Avanzado.md#a3), [O2](04_Nivel_4_Operacion.md#o2).
- **Dueños de datos de las áreas de negocio** (~25 h). Definen qué es un registro en su área, validan etiquetas y revisan eliminaciones. Módulos: [P0](01_Nivel_1_Inicial.md#p0), [I1](01_Nivel_1_Inicial.md#i1), [I3](01_Nivel_1_Inicial.md#i3), [M1](02_Nivel_2_Intermedio.md#m1), [M2](02_Nivel_2_Intermedio.md#m2), [M3](02_Nivel_2_Intermedio.md#m3), [O1](04_Nivel_4_Operacion.md#o1).
- **Oficial de privacidad** (~27 h). Minimización, plazos de conservación de datos personales, IA y solicitudes de los titulares. Módulos: [P0](01_Nivel_1_Inicial.md#p0), [I1](01_Nivel_1_Inicial.md#i1), [I2](01_Nivel_1_Inicial.md#i2), [M2](02_Nivel_2_Intermedio.md#m2), [A1](03_Nivel_3_Avanzado.md#a1), [A3](03_Nivel_3_Avanzado.md#a3), [O1](04_Nivel_4_Operacion.md#o1), [O3](04_Nivel_4_Operacion.md#o3).

<a id="plan"></a>

## Plan de entrenamiento sugerido

Calendario de referencia de 11 semanas para una dedicación de 5 a 8 horas por semana (unas 61 horas). Cada semana deja un entregable verificable y las evaluaciones cierran las semanas 4, 7, 9 y 11. Reserva ventanas de espera: varias configuraciones tardan hasta 7 días en verse, así que conviene dejar listo el laboratorio de la semana siguiente antes de cerrar la actual.

| Semana | Módulos | Foco | Entregable |
|---|---|---|---|
| 1 | [P0](01_Nivel_1_Inicial.md#p0), [I0](01_Nivel_1_Inicial.md#i0) | Portal, licencias, roles y plan de estudio | Matriz de licencias del tenant completada, grupos de roles asignados con expiración y plan personal mapeado a SC-401 |
| 2 | [I1](01_Nivel_1_Inicial.md#i1) | Principios de retención, directivas, etiquetas y ámbitos adaptables | Directiva estática piloto con evidencia en la biblioteca de conservación y ámbito adaptable validado |
| 3 | [I2](01_Nivel_1_Inicial.md#i2) | Retención en Exchange, SharePoint, OneDrive, Teams y Viva Engage | Matriz de retención del tenant y directiva de Teams verificada con una búsqueda de eDiscovery |
| 4 | [I3](01_Nivel_1_Inicial.md#i3), [C1](05_Comunidad.md#c1) | Registros, plan de archivos y referentes | Plan de archivos importado y exportado, registro con versionado probado; evaluación del nivel 1 aprobada |
| 5 | [M1](02_Nivel_2_Intermedio.md#m1) | Autoaplicación y simulación | Simulaciones por SIT y por KQL con muestras revisadas y decisión documentada |
| 6 | [M2](02_Nivel_2_Intermedio.md#m2), [M3](02_Nivel_2_Intermedio.md#m3) | Revisión de eliminación, limpieza prioritaria y eventos | Revisión en dos etapas configurada, evento disparado y runbook de limpieza prioritaria |
| 7 | [M4](02_Nivel_2_Intermedio.md#m4) | Archivo, buzones inactivos, PST y Microsoft 365 Archive | Buzón inactivo verificado, PST importado y análisis de costo de Microsoft 365 Archive; evaluación del nivel 2 aprobada |
| 8 | [A1](03_Nivel_3_Avanzado.md#a1), [A3](03_Nivel_3_Avanzado.md#a3) | Retención para IA y convivencia con los holds | Directiva para interacciones de Copilot diseñada con Legal y prueba de un hold frente a una directiva de eliminación |
| 9 | [A2](03_Nivel_3_Avanzado.md#a2), [A4](03_Nivel_3_Avanzado.md#a4) | APIs, regulación y Multi-Geo | Plan de archivos exportado como código y matriz requisito–control–evidencia; evaluación del nivel 3 aprobada |
| 10 | [O1](04_Nivel_4_Operacion.md#o1), [O2](04_Nivel_4_Operacion.md#o2) | Modelo operativo y métricas | Matriz RACI, grupos de roles con separación de funciones y tablero de métricas con datos del laboratorio |
| 11 | [O3](04_Nivel_4_Operacion.md#o3), [C2](05_Comunidad.md#c2) | Gobierno, normativa y rutina de actualización | Inventario normativo validado por Legal y rutina de actualización; evaluación de operación y reto final |

<a id="laboratorio"></a>

## Tu laboratorio

**Tu entorno.** Una prueba de Microsoft 365 E5 (o un sandbox) incluye las funciones de nivel E5 de este programa: ámbitos adaptables, autoaplicación, plan de archivos, eventos, registros y revisión de eliminación. Súmale una suscripción de Azure con créditos de Visual Studio Enterprise para vincular el pago por uso de Purview, que exigen las ubicaciones de IA, Microsoft 365 Archive y las directivas de recopilación. Prepara cinco usuarios de prueba con el atributo de departamento completo, un sitio piloto de SharePoint, un equipo de Teams con un canal privado, una comunidad de Viva Engage y buzones con al menos 10 MB, porque la retención no se aplica a buzones más pequeños.

**Qué no se puede practicar en el laboratorio.** Las interacciones de Microsoft 365 Copilot (la prueba de E5 no incluye Copilot), la precisión de los clasificadores entrenables (necesitan volumen real), el archivo de expansión automática (se activa con más de 90 GB y es irreversible), el envío de discos para PST (solo con Enterprise Agreement y con costo), la limpieza prioritaria ante un incidente real con tres aprobadores, Multi-Geo (requiere ubicaciones satélite) y las métricas con volumen de producción. Para esos casos cada módulo indica cómo practicar en producción con riesgo controlado.

**Tiempos de espera.** Las etiquetas publicadas tardan hasta 7 días en aparecer; los temporizadores de SharePoint y de eliminación corren cada 7 días; los ámbitos adaptables se recalculan a diario; la fecha de un evento se sincroniza en hasta 7 días; la retención de Copilot actúa en 1 a 7 días; y la acción de archivo puede tardar hasta 10 días. Configura el lunes y verifica la semana siguiente.

**Costos a vigilar.** El pago por uso de las ubicaciones de IA y de las directivas de recopilación (las interacciones de Microsoft 365 Copilot no generan cargo), Microsoft 365 Archive (USD 0,05 por GB al mes solo por encima de la cuota) y el almacenamiento de Azure Blob si pruebas Azure PST Import. Define alertas de presupuesto en Azure desde el primer día.

**Acciones irreversibles y limpieza.** Eliminar contenido, declarar registros regulatorios, aplicar Preservation Lock, habilitar el archivo de expansión automática y ejecutar una limpieza prioritaria no tienen vuelta atrás: practícalas solo con contenido desechable y revisa [Acciones irreversibles](#irreversibles). Al terminar, desactiva las directivas de prueba, elimina las etiquetas que no uses, desvincula el pago por uso si ya no lo necesitas y borra la cuenta de almacenamiento. Recuerda que, desde agosto de 2026, quitar el último hold de un buzón inactivo deja un delay hold de 30 días.

La matriz de qué se puede practicar en el laboratorio y qué solo en producción está en [07_Laboratorio_y_practica_en_produccion.md](07_Laboratorio_y_practica_en_produccion.md). La guía para construir el entorno está en el [anexo común](../Anexo_Entorno_de_practica.md).

<a id="mapa"></a>

## Mapa de módulos

- **Nivel 1 · Inicial:** [P0 Prerrequisitos y licencias](01_Nivel_1_Inicial.md#p0) · [I0 Cómo aprender](01_Nivel_1_Inicial.md#i0) · [I1 Directivas y etiquetas](01_Nivel_1_Inicial.md#i1) · [I2 Retención por carga de trabajo](01_Nivel_1_Inicial.md#i2) · [I3 Registros y plan de archivos](01_Nivel_1_Inicial.md#i3)
- **Nivel 2 · Intermedio:** [M1 Autoaplicación de etiquetas](02_Nivel_2_Intermedio.md#m1) · [M2 Revisión de eliminación](02_Nivel_2_Intermedio.md#m2) · [M3 Retención por eventos](02_Nivel_2_Intermedio.md#m3) · [M4 Archivo, inactivos y PST](02_Nivel_2_Intermedio.md#m4)
- **Nivel 3 · Avanzado:** [A1 Retención de Copilot e IA](03_Nivel_3_Avanzado.md#a1) · [A2 APIs y automatización](03_Nivel_3_Avanzado.md#a2) · [A3 Holds y eDiscovery](03_Nivel_3_Avanzado.md#a3) · [A4 Regulación y multigeografía](03_Nivel_3_Avanzado.md#a4)
- **Nivel 4 · Operación:** [O1 Modelo operativo](04_Nivel_4_Operacion.md#o1) · [O2 Métricas y mejora continua](04_Nivel_4_Operacion.md#o2) · [O3 Gobierno y normativa MCSA](04_Nivel_4_Operacion.md#o3)
- **Comunidad:** [C1 Referentes y libros](05_Comunidad.md#c1) · [C2 Español y actualización](05_Comunidad.md#c2)

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. No es asesoría legal: las decisiones de retención y eliminación deben validarse con Legal y privacidad. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

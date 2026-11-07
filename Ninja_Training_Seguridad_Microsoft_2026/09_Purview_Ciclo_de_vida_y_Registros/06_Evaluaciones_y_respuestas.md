# Evaluaciones y respuestas

*Microsoft Purview Ciclo de vida de los datos y Gestión de registros Ninja Training · Edición 2026*

[← Comunidad](05_Comunidad.md) · [Índice del programa](README.md) · [Laboratorio y práctica en producción →](07_Laboratorio_y_practica_en_produccion.md)

<a id="respuestas"></a>

Cada evaluación tiene preguntas de opción múltiple. Con 80 % o más el nivel se considera aprobado. Es una autoevaluación de esta guía, no una certificación de Microsoft.

<a id="eval-inicial"></a>

## Nivel 1 · Inicial · Fundamentos

**1. ¿Qué es Data Lifecycle Management en Microsoft Purview?**

- a) Una solución nueva que reemplaza a Records Management
- b) Un complemento de pago por uso para archivar sitios inactivos
- c) El nuevo nombre de Microsoft Information Governance  ✅
- d) El nombre actual de eDiscovery Standard

*Respuesta: c).* DLM es el nuevo nombre de Microsoft Information Governance; Records Management sigue existiendo para el contenido de alto valor con obligaciones legales o regulatorias. [Fuente](https://learn.microsoft.com/en-us/purview/data-lifecycle-management) · Repasa [P0](01_Nivel_1_Inicial.md#p0)

**2. ¿Cuál de estas capacidades está incluida en Microsoft 365 E3 sin complementos?**

- a) Directivas de retención estáticas  ✅
- b) Ámbitos adaptables
- c) Revisión de eliminación
- d) Retención basada en eventos

*Respuesta: a).* Las directivas estáticas están en E3 (también en Office 365 E3 y Business Premium). Los ámbitos adaptables, la revisión de eliminación y los eventos exigen nivel E5, Purview Suite o IP&G. [Fuente](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description) · Repasa [P0](01_Nivel_1_Inicial.md#p0)

**3. Un administrador global intenta revisar elementos pendientes de eliminación y no puede. ¿Cuál es la causa más probable?**

- a) La revisión solo puede hacerse con PowerShell
- b) Su cuenta no tiene licencia E5
- c) La auditoría está desactivada por diseño
- d) No tiene el rol Disposition Management, que no recibe por defecto  ✅

*Respuesta: d).* El rol Disposition Management forma parte del grupo Records Management y debe asignarse explícitamente; el administrador global no lo tiene por defecto. [Fuente](https://learn.microsoft.com/en-us/purview/disposition) · Repasa [P0](01_Nivel_1_Inicial.md#p0)

**4. Desde julio de 2026, ¿qué cambio tienen las asignaciones a grupos de roles de Purview?**

- a) Solo pueden hacerse con PIM
- b) Pueden tener fecha de expiración de 1 día a 2 años, salvo eDiscovery Administrator y eDiscovery Manager  ✅
- c) Vencen automáticamente a los 90 días
- d) Ya no admiten grupos de seguridad

*Respuesta: b).* La expiración es opcional y va de 1 día a 2 años; no aplica a eDiscovery Administrator ni a eDiscovery Manager. [Fuente](https://learn.microsoft.com/en-us/purview/whats-new) · Repasa [P0](01_Nivel_1_Inicial.md#p0)

**5. En SC-401, con las habilidades vigentes desde el 28 de octubre de 2026, ¿cuánto pesa el bloque «Implementar DLP y retención»?**

- a) 10–15 %
- b) 15–20 %
- c) 20–25 %
- d) 30–35 %  ✅

*Respuesta: d).* Pesa entre 30 y 35 % e incluye etiquetas, ámbitos adaptables, autoaplicación, precedencia y recuperación de contenido retenido. [Fuente](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-401) · Repasa [I0](01_Nivel_1_Inicial.md#i0)

**6. Un elemento tiene una directiva «retener 7 años» y una etiqueta «eliminar a los 2 años». ¿Qué ocurre?**

- a) Se elimina a los 2 años porque la etiqueta es más explícita
- b) Se elimina a los 2 años y queda una copia por 5 años más
- c) Se conserva durante 7 años porque retener gana sobre eliminar  ✅
- d) El elemento queda bloqueado por conflicto

*Respuesta: c).* El primer principio decide: retener gana sobre eliminar. El principio de lo explícito solo se aplica para resolver conflictos entre acciones de eliminación. [Fuente](https://learn.microsoft.com/en-us/purview/retention) · Repasa [I1](01_Nivel_1_Inicial.md#i1)

**7. Dos directivas de solo eliminar aplican al mismo sitio: una de toda la organización (3 años) y otra con ámbito específico para ese sitio (5 años). ¿Cuándo se elimina el contenido?**

- a) A los 5 años, porque la directiva con ámbito es más explícita  ✅
- b) A los 3 años, porque gana el período de eliminación más corto
- c) Nunca, porque las directivas entran en conflicto
- d) A los 8 años, porque los períodos se suman

*Respuesta: a).* El tercer principio (lo explícito gana sobre lo implícito para la eliminación) se evalúa antes que el cuarto (gana la eliminación más corta). [Fuente](https://learn.microsoft.com/en-us/purview/retention) · Repasa [I1](01_Nivel_1_Inicial.md#i1)

**8. ¿Cuántos atributos admite como máximo un grupo de un ámbito adaptable?**

- a) 5
- b) 20
- c) Sin límite
- d) 10  ✅

*Respuesta: d).* El límite es de 10 atributos por grupo y 10 grupos, con 200 caracteres por valor y 10.000 en la consulta avanzada. [Fuente](https://learn.microsoft.com/en-us/purview/purview-adaptive-scopes) · Repasa [I1](01_Nivel_1_Inicial.md#i1)

**9. ¿Qué ocurre si quitas la última inclusión de una directiva de retención con ámbito estático?**

- a) La directiva se desactiva
- b) Se convierte en una directiva con ámbito adaptable
- c) Vuelve a aplicarse a «Todos»  ✅
- d) Se elimina la directiva

*Respuesta: c).* Sin inclusiones, la directiva vuelve a «Todos»: en una directiva de eliminación, el impacto puede alcanzar a toda la organización. [Fuente](https://learn.microsoft.com/en-us/purview/retention-settings) · Repasa [I1](01_Nivel_1_Inicial.md#i1)

**10. ¿Qué requisito mínimo tiene un buzón de Exchange para que se le aplique la retención?**

- a) Tener al menos 10 MB  ✅
- b) Tener al menos 1 GB
- c) Tener el buzón de archivo habilitado
- d) Tener licencia E5

*Respuesta: a).* La retención de Exchange solo se aplica a buzones con al menos 10 MB; en el laboratorio, siembra correo antes de probar. [Fuente](https://learn.microsoft.com/en-us/purview/retention-settings) · Repasa [I1](01_Nivel_1_Inicial.md#i1)

**11. Desde finales de abril de 2026, ¿cómo se retienen los nuevos registros de llamadas de Teams?**

- a) Siguen incluidos en la directiva de chats de Teams
- b) Con etiquetas autoaplicadas
- c) No se pueden retener
- d) Con directivas «Teams call logs» creadas por PowerShell  ✅

*Respuesta: d).* Los nuevos registros de llamadas salieron de las directivas de chats y requieren directivas propias creadas por PowerShell. [Fuente](https://learn.microsoft.com/en-us/purview/whats-new) · Repasa [I2](01_Nivel_1_Inicial.md#i2)

**12. Tras la migración de los canales privados a buzones de grupo, ¿qué ubicación retiene sus mensajes?**

- a) Teams chats
- b) Teams channel messages  ✅
- c) Teams private channel messages
- d) Los buzones de Exchange de cada miembro

*Respuesta: b).* Los mensajes de canales privados pasan al buzón del grupo y heredan la directiva de mensajes de canal del equipo. [Fuente](https://learn.microsoft.com/en-us/purview/retention-policies-teams) · Repasa [I2](01_Nivel_1_Inicial.md#i2)

**13. ¿Cada cuánto corre el trabajo del temporizador que procesa la biblioteca de conservación en SharePoint y OneDrive?**

- a) Cada 24 horas
- b) Cada 93 días
- c) Cada 7 días  ✅
- d) Cada 30 días

*Respuesta: c).* Corre cada 7 días sobre el contenido con más de 30 días en la biblioteca de conservación; después, la papelera de segunda etapa suma 93 días. [Fuente](https://learn.microsoft.com/en-us/purview/retention-policies-sharepoint) · Repasa [I2](01_Nivel_1_Inicial.md#i2)

**14. ¿Qué tipo de etiqueta permite editar el contenido sin perder la etiqueta?**

- a) Registro regulatorio
- b) Registro desbloqueado  ✅
- c) Registro bloqueado
- d) Ninguno: ningún registro admite edición

*Respuesta: b).* El registro desbloqueado permite editar; el bloqueado impide editar y eliminar; el regulatorio además impide cambiar o quitar la etiqueta. [Fuente](https://learn.microsoft.com/en-us/purview/records-management) · Repasa [I3](01_Nivel_1_Inicial.md#i3)

**15. Con el versionado de registros, ¿dónde se guardan las versiones bloqueadas?**

- a) En la carpeta Records de la biblioteca de conservación  ✅
- b) En la papelera de segunda etapa
- c) En Recoverable Items
- d) En SubstrateHolds

*Respuesta: a).* Cada versión bloqueada se conserva como registro en la carpeta Records de la biblioteca de conservación; el versionado no aplica a registros regulatorios. [Fuente](https://learn.microsoft.com/en-us/purview/record-versioning) · Repasa [I3](01_Nivel_1_Inicial.md#i3)

<a id="eval-intermedio"></a>

## Nivel 2 · Intermedio · Automatizar y eliminar con evidencia

**1. ¿Qué licencia NO figura en la fila de la descripción del servicio para autoaplicar etiquetas de retención con clasificadores entrenables?**

- a) Microsoft 365 E5
- b) E5 Information Protection & Governance
- c) Microsoft Purview Suite
- d) Office 365 E5  ✅

*Respuesta: d).* La fila de clasificadores entrenables no incluye Office 365 E5, a diferencia de la autoaplicación por SIT o palabras clave. [Fuente](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description) · Repasa [M1](02_Nivel_2_Intermedio.md#m1)

**2. La simulación de una directiva de autoaplicación de etiquetas de retención admite…**

- a) SIT y consultas por palabras clave o propiedades  ✅
- b) Solo clasificadores entrenables
- c) Etiquetas predeterminadas de SharePoint
- d) Etiquetas de registro regulatorio

*Respuesta: a).* La simulación funciona con SIT y consultas; la autoaplicación no sirve para registros regulatorios ni para etiquetas predeterminadas. [Fuente](https://learn.microsoft.com/en-us/purview/apply-retention-labels-automatically) · Repasa [M1](02_Nivel_2_Intermedio.md#m1)

**3. ¿Cuánto pueden tardar las etiquetas de retención publicadas en aparecer en Exchange?**

- a) Una hora
- b) Hasta 7 días  ✅
- c) Exactamente 24 horas
- d) 30 días

*Respuesta: b).* En Exchange pueden tardar hasta 7 días; en SharePoint y OneDrive suelen aparecer en 1 día, con un máximo de 7. [Fuente](https://learn.microsoft.com/en-us/purview/create-apply-retention-labels) · Repasa [M1](02_Nivel_2_Intermedio.md#m1)

**4. ¿Qué etiqueta NO puede aplicarse con una directiva de autoaplicación?**

- a) Una etiqueta de solo retener
- b) Una etiqueta de solo eliminar
- c) Una etiqueta de registro regulatorio  ✅
- d) Una etiqueta que retiene y luego elimina

*Respuesta: c).* La autoaplicación no está disponible para etiquetas de registro regulatorio; esas se aplican de forma manual y deliberada. [Fuente](https://learn.microsoft.com/en-us/purview/apply-retention-labels-automatically) · Repasa [M1](02_Nivel_2_Intermedio.md#m1)

**5. En la autoaplicación de etiquetas de retención, KQL significa…**

- a) Keyword Query Language, el lenguaje de búsqueda de Microsoft 365  ✅
- b) Kusto Query Language, el lenguaje de Sentinel
- c) Knowledge Query Layer, una función de Copilot
- d) Una lista de palabras clave sin sintaxis

*Respuesta: a).* Es Keyword Query Language, la misma sintaxis de propiedades que usa eDiscovery; no debe confundirse con Kusto Query Language. [Fuente](https://learn.microsoft.com/en-us/purview/edisc-keyword-query-language) · Repasa [M1](02_Nivel_2_Intermedio.md#m1)

**6. ¿Tiene el administrador global el rol Disposition Management por defecto?**

- a) Sí, siempre
- b) Solo si tiene licencia E5
- c) Solo si activa su rol con PIM
- d) No: debe asignarse de forma explícita  ✅

*Respuesta: d).* Disposition Management pertenece al grupo Records Management y debe asignarse; lo recomendable es un grupo personalizado de revisores. [Fuente](https://learn.microsoft.com/en-us/purview/disposition) · Repasa [M2](02_Nivel_2_Intermedio.md#m2)

**7. ¿Qué NO puede eliminar la limpieza prioritaria de buzones?**

- a) Correo bajo un hold de eDiscovery
- b) Registros y registros regulatorios  ✅
- c) Correo con una directiva de retención
- d) Correo bajo Preservation Lock

*Respuesta: b).* La limpieza prioritaria anula retenciones, holds y Preservation Lock, pero no aplica a ningún tipo de registro. [Fuente](https://learn.microsoft.com/en-us/purview/priority-cleanup-exchange) · Repasa [M2](02_Nivel_2_Intermedio.md#m2)

**8. Desde julio de 2026, ¿cuántas aprobaciones separadas requiere la limpieza prioritaria de buzones?**

- a) Una
- b) Dos
- c) Tres  ✅
- d) Cuatro

*Respuesta: c).* Tres: administrador de limpieza prioritaria, administrador de retención y administrador de eDiscovery. MC1183292 hablaba de dos, por eso conviene diseñar para tres. [Fuente](https://learn.microsoft.com/en-us/purview/whats-new) · Repasa [M2](02_Nivel_2_Intermedio.md#m2)

**9. ¿Cómo obtienes la prueba de eliminación?**

- a) Desde la papelera de reciclaje del sitio
- b) Con un informe de Compliance Manager
- c) Desde el explorador de actividad
- d) Exportando los elementos eliminados desde la página de eliminación  ✅

*Respuesta: d).* La página de eliminación permite filtrar y exportar los elementos pendientes y los eliminados; esa exportación es la prueba de eliminación. [Fuente](https://learn.microsoft.com/en-us/purview/disposition) · Repasa [M2](02_Nivel_2_Intermedio.md#m2)

**10. En la retención basada en eventos, ¿qué identifica los correos de Exchange afectados por un evento?**

- a) El ID de activo
- b) Palabras clave  ✅
- c) Una etiqueta de confidencialidad
- d) La fecha de creación

*Respuesta: b).* El ID de activo se usa en SharePoint y OneDrive; en Exchange, el evento encuentra los elementos por palabras clave. [Fuente](https://learn.microsoft.com/en-us/purview/event-driven-retention) · Repasa [M3](02_Nivel_2_Intermedio.md#m3)

**11. ¿Qué ocurre con un elemento con etiqueta basada en eventos cuyo evento nunca se crea?**

- a) Se elimina a los 7 días
- b) Pierde la etiqueta
- c) Se retiene indefinidamente  ✅
- d) Se convierte en registro regulatorio

*Respuesta: c).* Sin evento no empieza el período, así que el elemento queda retenido indefinidamente: por eso hay que conciliar los eventos con el sistema de origen. [Fuente](https://learn.microsoft.com/en-us/purview/event-driven-retention) · Repasa [M3](02_Nivel_2_Intermedio.md#m3)

**12. ¿Qué es cierto del archivo de expansión automática?**

- a) Es irreversible y se habilita con Exchange Online PowerShell  ✅
- b) Se desactiva desde el centro de administración de Exchange
- c) Se habilita desde el portal de Purview
- d) Siempre ofrece 3 TB

*Respuesta: a).* No puede desactivarse y solo se habilita por PowerShell; los 3 TB aplican desde octubre de 2026 a licencias elegibles con el plan Records Management habilitado. [Fuente](https://learn.microsoft.com/en-us/purview/enable-autoexpanding-archiving) · Repasa [M4](02_Nivel_2_Intermedio.md#m4)

**13. ¿Qué configuración previa NO convierte un buzón en inactivo al eliminar la cuenta?**

- a) Una directiva de solo retener
- b) Una directiva de retener y luego eliminar
- c) Litigation Hold
- d) Una directiva de solo eliminar  ✅

*Respuesta: d).* Hace falta una acción de retener o un hold antes de eliminar la cuenta; una directiva de solo eliminar no conserva el buzón. [Fuente](https://learn.microsoft.com/en-us/purview/inactive-mailboxes-in-office-365) · Repasa [M4](02_Nivel_2_Intermedio.md#m4)

**14. ¿Cuándo cobra Microsoft 365 Archive?**

- a) Por cada usuario licenciado
- b) Solo por el almacenamiento archivado que supera la cuota, a USD 0,05 por GB al mes  ✅
- c) Cada vez que se reactiva un sitio
- d) Siempre, desde el primer GB

*Respuesta: b).* Solo se factura lo que excede la cuota del tenant, y la reactivación es gratuita desde el 31 de marzo de 2025. [Fuente](https://learn.microsoft.com/en-us/microsoft-365/archive/archive-pricing?view=o365-worldwide) · Repasa [M4](02_Nivel_2_Intermedio.md#m4)

**15. Desde agosto de 2026, ¿qué ocurre al quitar el último hold de un buzón inactivo?**

- a) Se elimina de inmediato
- b) Pasa a ser un buzón compartido
- c) Se aplica automáticamente un delay hold de 30 días  ✅
- d) Se exporta a un PST

*Respuesta: c).* El delay hold de 30 días da una ventana para detectar liberaciones por error antes de que el buzón inactivo se elimine. [Fuente](https://learn.microsoft.com/en-us/purview/whats-new) · Repasa [M4](02_Nivel_2_Intermedio.md#m4)

<a id="eval-avanzado"></a>

## Nivel 3 · Avanzado · IA, APIs, holds y regulación

**1. ¿Qué ubicaciones de retención exigen facturación de pago por uso?**

- a) Buzones de Exchange
- b) Mensajes de Viva Engage
- c) Microsoft Copilot experiences, Enterprise AI apps y Other AI apps  ✅
- d) Chats de Teams

*Respuesta: c).* Las tres ubicaciones de IA requieren pago por uso, aunque las interacciones de Microsoft 365 Copilot no generan cargo. [Fuente](https://learn.microsoft.com/en-us/purview/get-started-with-data-lifecycle-management) · Repasa [A1](03_Nivel_3_Avanzado.md#a1)

**2. ¿Dónde se guardan los prompts y las respuestas de Copilot que conserva una directiva de retención?**

- a) En una carpeta oculta del buzón del usuario  ✅
- b) En el OneDrive del usuario
- c) En un sitio de SharePoint del tenant
- d) En una cuenta de Azure Blob Storage del cliente

*Respuesta: a).* Se guardan en una carpeta oculta del buzón; al eliminarse pasan al menos un día por SubstrateHolds, y cualquier hold suspende la eliminación. [Fuente](https://learn.microsoft.com/en-us/purview/retention-policies-copilot) · Repasa [A1](03_Nivel_3_Avanzado.md#a1)

**3. ¿Para qué interacciones de IA necesitas una directiva de recopilación con captura de contenido antes de poder retenerlas?**

- a) Para las de Microsoft 365 Copilot
- b) Para las de Copilot Studio
- c) Para ninguna: basta la directiva de retención
- d) Para las de apps de IA distintas de Microsoft 365 Copilot y Copilot Studio, como ChatGPT Enterprise  ✅

*Respuesta: d).* Microsoft 365 Copilot y Copilot Studio no la necesitan; el resto de la IA sí requiere una directiva de recopilación con captura de contenido. [Fuente](https://learn.microsoft.com/en-us/purview/collection-policies-solution-overview) · Repasa [A1](03_Nivel_3_Avanzado.md#a1)

**4. ¿Qué combinación habilita ámbitos adaptables para la retención de Copilot y la retención de la versión exacta del documento compartido?**

- a) E3 + Microsoft 365 Copilot
- b) E5 + Microsoft 365 Copilot, o E3 + Purview Suite o IP&G + Microsoft 365 Copilot  ✅
- c) Solo Microsoft 365 E7
- d) Business Premium + Copilot Chat

*Respuesta: b).* E3 o E5 con Copilot permiten retener interacciones; las funciones de nivel E5 requieren E5, o E3 con Purview Suite o IP&G, además de Copilot. [Fuente](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description) · Repasa [A1](03_Nivel_3_Avanzado.md#a1)

**5. En un tenant Multi-Geo, ¿cómo se acota eDiscovery a una ubicación satélite como México?**

- a) Con un portal de Purview distinto por geografía
- b) Con unidades administrativas en las directivas de etiquetas
- c) Con el filtro de seguridad «Region» (por ejemplo, MEX)  ✅
- d) No es posible acotarlo

*Respuesta: c).* Multi-Geo mantiene un único portal de Purview; eDiscovery en ubicaciones satélite usa el filtro «Region», con MEX, BRA y CHL disponibles. [Fuente](https://learn.microsoft.com/en-us/microsoft-365/enterprise/multi-geo-ediscovery-configuration?view=o365-worldwide) · Repasa [A4](03_Nivel_3_Avanzado.md#a4)

**6. En Microsoft Graph, ¿qué valor de `retentionTrigger` habilita la retención basada en eventos?**

- a) dateLabeled
- b) dateCreated
- c) dateModified
- d) dateOfEvent  ✅

*Respuesta: d).* dateOfEvent asocia la etiqueta a un retentionEventType; el evento se crea después con eventQueries como AssetID:1234. [Fuente](https://learn.microsoft.com/en-us/graph/api/resources/security-recordsmanagement-overview?view=graph-rest-1.0) · Repasa [A2](03_Nivel_3_Avanzado.md#a2)

**7. ¿Qué restricción tiene la acción de Power Automate al final del período de retención?**

- a) Solo funciona con registros regulatorios
- b) Solo en etiquetas nuevas y con el flujo en «My flows», no en Solutions  ✅
- c) Requiere Logic Apps Standard
- d) Solo aplica a Exchange

*Respuesta: b).* Además, el flujo no puede reetiquetar el contenido con una etiqueta de registro regulatorio. [Fuente](https://learn.microsoft.com/en-us/purview/retention-label-flow) · Repasa [A2](03_Nivel_3_Avanzado.md#a2)

**8. Desde agosto de 2026, ¿qué recomienda Microsoft para las automatizaciones de eDiscovery que usan cmdlets con autenticación solo de aplicación?**

- a) Migrarlas a Microsoft Graph  ✅
- b) Mantenerlas: siguen con soporte completo
- c) Pasarlas a Power Automate
- d) Ejecutarlas con una cuenta de administrador global

*Respuesta: a).* Esa autenticación dejó de tener soporte en los cmdlets de eDiscovery; la vía recomendada es Microsoft Graph. [Fuente](https://learn.microsoft.com/en-us/purview/whats-new) · Repasa [A2](03_Nivel_3_Avanzado.md#a2)

**9. ¿Qué es cierto del script de ejemplo para crear y publicar etiquetas en masa con PowerShell?**

- a) Tiene soporte de Microsoft y cubre la autoaplicación
- b) Solo funciona con Microsoft Graph
- c) Es un ejemplo sin soporte y no cubre la autoaplicación  ✅
- d) Requiere Power Automate

*Respuesta: c).* Usa New-ComplianceTag y New-RetentionCompliancePolicy desde CSV; es un ejemplo sin soporte y no crea directivas de autoaplicación. [Fuente](https://learn.microsoft.com/en-us/purview/bulk-create-publish-labels-using-powershell) · Repasa [A2](03_Nivel_3_Avanzado.md#a2)

**10. Un buzón inactivo se conserva solo por un hold de eDiscovery. ¿Qué ocurre si Legal cierra el caso?**

- a) Nada: el buzón inactivo se conserva para siempre
- b) El buzón inactivo se elimina; desde agosto de 2026, después de un delay hold de 30 días  ✅
- c) Se convierte en buzón compartido
- d) Se exporta automáticamente a PST

*Respuesta: b).* Si el hold era lo único que lo mantenía, el buzón inactivo se elimina; el delay hold de 30 días da una ventana para corregir. [Fuente](https://learn.microsoft.com/en-us/purview/change-the-hold-duration-for-an-inactive-mailbox) · Repasa [A3](03_Nivel_3_Avanzado.md#a3)

**11. Un documento tiene una etiqueta que lo elimina hoy y está bajo un hold de eDiscovery. ¿Qué ocurre?**

- a) Se elimina porque la etiqueta es explícita
- b) Se mueve a Microsoft 365 Archive
- c) Se elimina y queda una copia en la papelera
- d) Se conserva mientras dure el hold, porque retener gana sobre eliminar  ✅

*Respuesta: d).* El primer principio de retención decide: el hold retiene y suspende cualquier eliminación de directivas o etiquetas. [Fuente](https://learn.microsoft.com/en-us/purview/retention) · Repasa [A3](03_Nivel_3_Avanzado.md#a3)

**12. ¿Qué cambió el 16 de febrero de 2026 en las búsquedas de contenido?**

- a) Se retiraron por completo
- b) Solo admiten buzones de Exchange
- c) Pasaron a requerir Microsoft 365 E7
- d) Se limitan a buscar y exportar; los holds requieren un caso  ✅

*Respuesta: d).* Desde esa fecha, los holds y los conjuntos de revisión requieren un caso completo de eDiscovery. [Fuente](https://office365itpros.com/2026/01/15/content-searches-change/) · Repasa [A3](03_Nivel_3_Avanzado.md#a3)

**13. Creas un hold sobre un grupo y una semana después se suma un miembro nuevo. ¿Queda retenido su contenido?**

- a) No: la membresía se toma como instantánea al crear el hold  ✅
- b) Sí: la membresía se actualiza a diario
- c) Solo si tiene licencia E5
- d) Solo su OneDrive

*Respuesta: a).* El hold toma la membresía al crearse y puede tardar hasta 24 horas en aplicarse; las altas posteriores no quedan retenidas. [Fuente](https://learn.microsoft.com/en-us/purview/edisc-hold-create) · Repasa [A3](03_Nivel_3_Avanzado.md#a3)

**14. ¿Qué evaluación de terceros publica Microsoft sobre la retención de Microsoft 365?**

- a) Una certificación ISO 27701 emitida por BSI
- b) Un informe SOC 2 tipo II
- c) La de Cohasset frente a SEC 17a-4(f), FINRA 4511(c) y CFTC 1.31  ✅
- d) Ninguna: Microsoft no publica evaluaciones

*Respuesta: c).* Cohasset evaluó la retención en julio de 2022 frente a esas normas de Estados Unidos y en enero de 2021 frente a la Ley de Registros Públicos de Nueva Zelanda. [Fuente](https://learn.microsoft.com/en-us/purview/retention-regulatory-requirements) · Repasa [A4](03_Nivel_3_Avanzado.md#a4)

**15. ¿Qué ocurre después de aplicar Preservation Lock a una directiva de retención?**

- a) Un administrador global puede desactivarla
- b) No puede desactivarse ni eliminarse y solo puede ampliarse  ✅
- c) Caduca a los 2 años
- d) Se convierte en un hold de eDiscovery

*Respuesta: b).* Preservation Lock es irreversible: úsalo solo ante un requisito regulatorio documentado y aprobado por Legal. [Fuente](https://learn.microsoft.com/en-us/purview/retention-preservation-lock) · Repasa [A4](03_Nivel_3_Avanzado.md#a4)

<a id="eval-operacion"></a>

## Nivel 4 · Operación · Programa, métricas y gobierno

**1. ¿Qué configuración respeta la separación de funciones que recomienda la documentación de eliminación?**

- a) Un único grupo Records Management para diseñar, revisar y aprobar la limpieza prioritaria
- b) El administrador global para todas las tareas, con auditoría posterior
- c) Records Management para el diseño, un grupo personalizado de revisores con Disposition Management y aprobadores distintos para la limpieza prioritaria  ✅
- d) Compliance Administrator para todos los revisores

*Respuesta: c).* Separar diseño, revisión y aprobación impide que una sola persona elimine registros y es lo primero que pide un auditor. [Fuente](https://learn.microsoft.com/en-us/purview/disposition) · Repasa [O1](04_Nivel_4_Operacion.md#o1)

**2. ¿Qué norma internacional define políticas, responsabilidades, valoración, controles y autoridades de disposición para la gestión de registros?**

- a) ISO 15489-1:2016  ✅
- b) ISO/IEC 27001
- c) ISO 9001
- d) ISO 22301

*Respuesta: a).* ISO 15489-1:2016, confirmada en 2021, establece los conceptos y principios de la gestión de registros. [Fuente](https://www.iso.org/standard/62542.html) · Repasa [O1](04_Nivel_4_Operacion.md#o1)

**3. Según el caso que resume Nikki Chapple, ¿qué hizo un programa global con su tabla de retención?**

- a) Creó una etiqueta por cada serie documental
- b) Pasó de más de 5.000 categorías a 180 tipos de registro y usó la revisión de eliminación solo como excepción  ✅
- c) Eliminó por completo la revisión de eliminación
- d) Usó solo directivas de toda la organización

*Respuesta: b).* Simplificar en tipos de registro mejora la precisión del etiquetado; la revisión de eliminación se reservó para unos 10 tipos. [Fuente](https://nikkichapple.com/microsoft-purview-records-management-guide/) · Repasa [O1](04_Nivel_4_Operacion.md#o1)

**4. Un auditor externo necesita consultar la configuración de retención durante tres semanas. ¿Qué es lo más adecuado desde julio de 2026?**

- a) Asignarle Compliance Administrator de forma permanente
- b) Asignarle View-Only Retention Management con fecha de expiración  ✅
- c) Compartirle la cuenta de un administrador
- d) Enviarle cada semana por correo una exportación de las directivas

*Respuesta: b).* Desde julio de 2026 las asignaciones a grupos de roles de Purview admiten expiración; un rol de solo lectura cumple con el mínimo privilegio. [Fuente](https://learn.microsoft.com/en-us/purview/whats-new) · Repasa [O1](04_Nivel_4_Operacion.md#o1)

**5. ¿Qué evidencia mensual demuestra que las eliminaciones se hicieron con autorización?**

- a) La exportación de los elementos eliminados desde la página de eliminación  ✅
- b) Una captura del sitio vacío
- c) El informe de uso de Copilot
- d) La lista de etiquetas publicadas

*Respuesta: a).* La página de eliminación permite filtrar y exportar pendientes y eliminados: esa exportación es la prueba de eliminación. [Fuente](https://learn.microsoft.com/en-us/purview/disposition) · Repasa [O2](04_Nivel_4_Operacion.md#o2)

**6. ¿Qué describe la «deuda de retención»?**

- a) Etiquetas creadas que nunca se publicaron
- b) Directivas de solo retener que mantienen indefinidamente el OneDrive y el buzón de exempleados  ✅
- c) Costos de pago por uso pendientes de pago
- d) Eventos de retención creados dos veces

*Respuesta: b).* Es contenido de exempleados retenido sin plazo; se corrige con ámbitos adaptables alineados al ciclo de vida del usuario. [Fuente](https://nikkichapple.com/purview-lightning-talks-microsoft-security-community/) · Repasa [O2](04_Nivel_4_Operacion.md#o2)

**7. ¿Cómo se monitorea una limpieza prioritaria?**

- a) En el explorador de actividad
- b) En Compliance Manager
- c) En la auditoría, con el ID de la limpieza  ✅
- d) No deja rastro, por diseño

*Respuesta: c).* Cada limpieza prioritaria se sigue en la auditoría por su ID, junto con sus aprobaciones. [Fuente](https://learn.microsoft.com/en-us/purview/priority-cleanup-exchange) · Repasa [O2](04_Nivel_4_Operacion.md#o2)

**8. Un script de métricas usa `Search-UnifiedAuditLog`. ¿Qué deberías planificar?**

- a) Cambiarlo por Get-AdminAuditLogConfig
- b) Reemplazarlo por búsquedas de contenido
- c) Usar el explorador de contenido
- d) Migrarlo a la API AuditLogQuery de Graph antes del retiro del cmdlet, el 15 de octubre de 2027  ✅

*Respuesta: d).* AuditLogQuery está disponible en general desde octubre de 2026 y Search-UnifiedAuditLog se retira el 15 de octubre de 2027. [Fuente](https://mc.merill.net/message/MC1505599) · Repasa [O2](04_Nivel_4_Operacion.md#o2)

**9. ¿Qué roles permiten a un analista de métricas ver la configuración de retención y registros sin modificarla?**

- a) View-Only Retention Management y View-Only Record Management  ✅
- b) Records Management
- c) Priority Cleanup Admin
- d) Compliance Administrator

*Respuesta: a).* Los roles de solo lectura permiten extraer métricas sin riesgo de cambiar directivas, etiquetas o eliminaciones. [Fuente](https://learn.microsoft.com/en-us/purview/get-started-with-records-management) · Repasa [O2](04_Nivel_4_Operacion.md#o2)

**10. ¿Desde cuándo rige la Ley 21.719 de protección de datos personales de Chile?**

- a) 1 de enero de 2025
- b) 1 de marzo de 2025
- c) 1 de diciembre de 2026  ✅
- d) 1 de diciembre de 2027

*Respuesta: c).* Publicada en diciembre de 2024, entra en vigencia el 1 de diciembre de 2026 y crea la Agencia de Protección de Datos Personales. [Fuente](https://www.leychile.cl/leychile/Navegar?idNorma=1209272&idParte=1) · Repasa [O3](04_Nivel_4_Operacion.md#o3)

**11. Según el texto vigente consultado, ¿cuándo fue la última reforma de la Ley General de Archivos de México?**

- a) 15 de junio de 2018
- b) 20 de marzo de 2025
- c) 1 de diciembre de 2026
- d) 14 de noviembre de 2025  ✅

*Respuesta: d).* La ley se publicó en el DOF el 15 de junio de 2018 y su última reforma es del 14 de noviembre de 2025. [Fuente](https://www.diputados.gob.mx/LeyesBiblio/pdf/LGA.pdf) · Repasa [O3](04_Nivel_4_Operacion.md#o3)

**12. ¿Qué norma colombiana define la tabla de retención documental (TRD)?**

- a) Ley 1581 de 2012
- b) Decreto 1377 de 2013
- c) Ley 594 de 2000  ✅
- d) Circular Externa 007 de 2018

*Respuesta: c).* La Ley 594 de 2000, Ley General de Archivos, define la TRD; la 1581 y el Decreto 1377 regulan datos personales. [Fuente](https://www1.funcionpublica.gov.co/eva//gestornormativo/norma.php?i=4275) · Repasa [O3](04_Nivel_4_Operacion.md#o3)

**13. ¿Cuándo se publicó en el DOF la nueva Ley Federal de Protección de Datos Personales en Posesión de los Particulares de México?**

- a) 20 de marzo de 2025  ✅
- b) 5 de julio de 2010
- c) 14 de noviembre de 2025
- d) 1 de diciembre de 2026

*Respuesta: a).* La nueva ley sustituye a la de 2010; la plantilla de Compliance Manager se diseñó para la ley anterior y conviene extenderla. [Fuente](https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPDPPP.pdf) · Repasa [O3](04_Nivel_4_Operacion.md#o3)

**14. ¿Qué período de adecuación da la Ley 7593/2025 de protección de datos personales de Paraguay?**

- a) 6 meses
- b) 12 meses
- c) 36 meses
- d) 24 meses  ✅

*Respuesta: d).* Se publicó el 27 de noviembre de 2025 con 24 meses de adecuación: la plena vigencia se prevé para fines de noviembre de 2027. [Fuente](https://www.bacn.gov.py/leyes-paraguayas/12924/ley-n-75932025--de-proteccin-de-datos-personales-en-la-repblica-del-paraguay) · Repasa [O3](04_Nivel_4_Operacion.md#o3)

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. No es asesoría legal: las decisiones de retención y eliminación deben validarse con Legal y privacidad. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

# Evaluaciones y respuestas

*Microsoft Purview Communication Compliance e Information Barriers Ninja Training · Edición 2026*

[← Comunidad](05_Comunidad.md) · [Índice del programa](README.md) · [Laboratorio y práctica en producción →](07_Laboratorio_y_practica_en_produccion.md)

<a id="respuestas"></a>

Cada evaluación tiene preguntas de opción múltiple. Con 80 % o más el nivel se considera aprobado. Es una autoevaluación de esta guía, no una certificación de Microsoft.

<a id="eval-inicial"></a>

## Nivel 1 · Inicial · Fundamentos

**1. ¿Con qué combinación queda incluido el análisis de prompts y respuestas de Microsoft 365 Copilot en Communication Compliance?**

- a) Office 365 E5, sin ninguna licencia adicional de Copilot
- b) Microsoft 365 E5 o Purview Suite más una licencia de Microsoft 365 Copilot  ✅
- c) Microsoft 365 E3 más el complemento E5 Insider Risk Management
- d) Cualquier licencia de Microsoft 365 Copilot, aunque el usuario no tenga E5

*Respuesta: b).* La descripción de servicio solo lo marca con «E5 + Copilot» o «Purview Suite + Copilot»; no con Office 365 E5, E3 ni el complemento de IRM. Además, no genera cargos de pago por uso. [Fuente](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description) · Repasa [I1](01_Nivel_1_Inicial.md#i1)

**2. Un mensaje de 7.500 caracteres analizado con pago por uso equivale a:**

- a) 1 registro de texto
- b) 7 registros de texto
- c) 8 registros de texto  ✅
- d) 75 registros de texto

*Respuesta: c).* Un registro de texto son 1.000 caracteres y se redondea hacia arriba: 7.500 caracteres son 8 registros. [Fuente](https://learn.microsoft.com/en-us/purview/purview-billing-models) · Repasa [I1](01_Nivel_1_Inicial.md#i1)

**3. ¿Qué clasificadores usa la plantilla Detect inappropriate text?**

- a) Hate, Violence, Sexual y Self-harm
- b) Prompt Shields y Protected material
- c) Adult y Racy
- d) Threat, Discrimination y Targeted harassment  ✅

*Respuesta: d).* La plantilla de texto inapropiado usa Threat, Discrimination y Targeted harassment. Hate, Violence, Sexual y Self-harm son de la plantilla de contenido inapropiado; Adult y Racy, de la de imágenes; Prompt Shields y Protected material, de la de Copilot. [Fuente](https://learn.microsoft.com/en-us/purview/communication-compliance-policies) · Repasa [I2](01_Nivel_1_Inicial.md#i2)

**4. Para mensajes en español, ¿qué afirmación es correcta?**

- a) Todos los clasificadores admiten español con un mínimo de 3 palabras
- b) Threat, Harassment y Profanity admiten español (mínimo 6 palabras), pero los financieros son solo en inglés  ✅
- c) Solo los clasificadores financieros admiten español; los de conducta son solo en inglés
- d) Discrimination y Threat funcionan en 12 idiomas, pero Harassment solo en inglés

*Respuesta: b).* Threat, Harassment y Profanity funcionan en 12 idiomas, incluido el español; Discrimination y los financieros son solo en inglés. Compleméntalos con diccionarios en español. [Fuente](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions) · Repasa [I2](01_Nivel_1_Inicial.md#i2)

**5. ¿Qué ocurre cuando una política alcanza 100 GB o 1 millón de mensajes?**

- a) Se desactiva automáticamente; copiar la política mantiene la cobertura  ✅
- b) Elimina las coincidencias más antiguas para liberar espacio
- c) Sigue capturando y factura el excedente por pago por uso
- d) Amplía su capacidad a 200 GB si tienes Audit (Premium)

*Respuesta: a).* La política avisa al 80, 90 y 95 % y se desactiva al llegar al límite; copiarla mantiene la cobertura. [Fuente](https://learn.microsoft.com/en-us/purview/communication-compliance-policies) · Repasa [I2](01_Nivel_1_Inicial.md#i2)

**6. ¿Cuándo se retiró el portal de cumplimiento clásico?**

- a) Entre el 14 de noviembre y el 14 de diciembre de 2024  ✅
- b) El 1 de junio de 2025
- c) El 15 de octubre de 2027
- d) Sigue disponible en paralelo al portal de Purview

*Respuesta: a).* Según MC939918, se retiró entre el 14 de noviembre y el 14 de diciembre de 2024, y las configuraciones pasaron con paridad al portal de Microsoft Purview. [Fuente](https://mc.merill.net/message/MC939918) · Repasa [P0](01_Nivel_1_Inicial.md#p0)

**7. Un administrador global sin roles de Communication Compliance intenta abrir las alertas. ¿Qué ocurre?**

- a) Ve todas las alertas por defecto
- b) Puede revisarlas, pero no remediarlas
- c) Solo ve las alertas de su unidad administrativa
- d) No tiene acceso por defecto a las alertas de CC  ✅

*Respuesta: d).* Por privacidad por diseño, los administradores globales no tienen acceso por defecto a CC ni a IRM: se necesita un grupo de roles de la solución. [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-solution-privacy) · Repasa [P0](01_Nivel_1_Inicial.md#p0)

**8. ¿Qué acción de revisión crea un caso de eDiscovery (Premium) a partir de una alerta de CC?**

- a) Resolver
- b) Etiquetar
- c) Escalar para investigación  ✅
- d) Notificar

*Respuesta: c).* «Escalar para investigación» crea un caso de eDiscovery (Premium) con hasta 100 mensajes; las demás acciones no crean casos. [Fuente](https://learn.microsoft.com/en-us/purview/communication-compliance-investigate-remediate) · Repasa [I3](01_Nivel_1_Inicial.md#i3)

**9. ¿Cuál es el período por defecto de conservación de coincidencias de política, vigente desde el 1 de junio de 2025?**

- a) 30 días
- b) 1 año  ✅
- c) 7 años
- d) Indefinido

*Respuesta: b).* La conservación va de 1 mes a 7 años, con 1 año por defecto; las coincidencias más antiguas que el período elegido pueden eliminarse definitivamente. [Fuente](https://learn.microsoft.com/es-es/purview/communication-compliance-investigate-remediate) · Repasa [I3](01_Nivel_1_Inicial.md#i3)

**10. ¿Qué requisito tiene el canal Viva Engage en Communication Compliance?**

- a) Una licencia de Copilot
- b) Pago por uso
- c) Estar en modo nativo  ✅
- d) Un conector de terceros

*Respuesta: c).* Viva Engage debe estar en modo nativo para que Communication Compliance lo supervise. [Fuente](https://learn.microsoft.com/en-us/purview/communication-compliance-channels) · Repasa [I1](01_Nivel_1_Inicial.md#i1)

**11. ¿Qué afirmación sobre los clasificadores LLM de seguridad de contenido (Hate, Sexual, Violence y Self-harm) es correcta?**

- a) Evalúan correo, adjuntos, OCR y transcripciones de Teams
- b) Generan alerta desde severidad 1 en cualquier canal
- c) Solo funcionan sobre contenido importado por conectores de terceros
- d) Solo evalúan Copilot, Teams y Viva Engage y alertan desde severidad 4  ✅

*Respuesta: d).* Evalúan Copilot, Teams y Viva Engage con una severidad de 0 a 7 y alertan desde 4; no evalúan adjuntos, OCR ni transcripciones. [Fuente](https://learn.microsoft.com/en-us/purview/communication-compliance-policies) · Repasa [I2](01_Nivel_1_Inicial.md#i2)

**12. ¿Qué credencial valida en un laboratorio la implementación de Communication Compliance?**

- a) El examen SC-401, cuyo temario vigente incluye CC e IB
- b) El examen SC-900 de fundamentos de seguridad, cumplimiento e identidad
- c) Applied Skills «Implement retention, eDiscovery, and Communication Compliance in Microsoft Purview»  ✅
- d) El Ninja oficial de 2022, que emite una certificación de Microsoft

*Respuesta: c).* La Applied Skill (APL-5007) evalúa en un laboratorio de 2 horas, entre otras tareas, delegar permisos y crear políticas de CC; la guía vigente de SC-401 no mide CC ni IB. [Fuente](https://learn.microsoft.com/en-us/credentials/applied-skills/implement-retention-ediscovery-and-communication-compliance-in-microsoft-purview/) · Repasa [I0](01_Nivel_1_Inicial.md#i0)

**13. ¿Qué límite aplica a los canales públicos de Teams en Communication Compliance?**

- a) Hasta 250 usuarios con ámbitos estáticos y sin cobertura con ámbitos adaptables  ✅
- b) Hasta 1.000 usuarios con cualquier tipo de ámbito
- c) Solo se cubren con ámbitos adaptables, sin límite de usuarios
- d) No se supervisan: CC solo cubre chats y canales privados

*Respuesta: a).* Los canales públicos se limitan a 250 usuarios con ámbitos estáticos y no se cubren con ámbitos adaptables: es un punto ciego típico de diseño. [Fuente](https://learn.microsoft.com/en-us/purview/communication-compliance-channels) · Repasa [I1](01_Nivel_1_Inicial.md#i1)

<a id="eval-intermedio"></a>

## Nivel 2 · Intermedio · IA, barreras, privacidad e integración

**1. ¿Qué interacciones requieren habilitar el pago por uso en Communication Compliance?**

- a) Chats y canales de Teams con adjuntos
- b) Microsoft 365 Copilot y Copilot Chat
- c) Copilot Studio, Copilot en Fabric y Security Copilot  ✅
- d) Viva Engage en modo nativo

*Respuesta: c).* Los datos de IA que no son de Microsoft 365 requieren pago por uso; Microsoft 365 Copilot no genera cargos de pago por uso, aunque exige su licencia. [Fuente](https://learn.microsoft.com/en-us/purview/communication-compliance-channels) · Repasa [M1](02_Nivel_2_Intermedio.md#m1)

**2. ¿Qué detectan Prompt Shields y Protected material?**

- a) Ambos analizan solo correo de Exchange y sus adjuntos
- b) Prompt Shields: jailbreak o inyección en prompts; Protected material: texto protegido en respuestas  ✅
- c) Prompt Shields: imágenes en los prompts; Protected material: adjuntos de las respuestas
- d) Ambos detectan lenguaje soez y amenazas en 12 idiomas

*Respuesta: b).* Prompt Shields evalúa solo prompts (jailbreak o inyección) y Protected material solo respuestas (texto protegido por derechos de autor o de marca); ambos funcionan solo en inglés. [Fuente](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions) · Repasa [M1](02_Nivel_2_Intermedio.md#m1)

**3. ¿Desde cuándo incluye la compatibilidad de Purview con Claude Enterprise a Communication Compliance, y en qué estado está el conector?**

- a) Desde mayo de 2026, con el conector en GA y sin pago por uso
- b) Desde agosto de 2026; el conector sigue en vista previa y requiere pago por uso  ✅
- c) Desde Ignite 2024, incluido en E5 sin pago por uso
- d) No es compatible: Purview solo aplica DLP y etiquetas a Claude

*Respuesta: b).* La compatibilidad con CC se agregó en agosto de 2026; el conector sigue en vista previa y requiere pago por uso. En mayo de 2026 llegó la vista previa del conector para DSPM. [Fuente](https://learn.microsoft.com/en-us/purview/ai-claude-enterprise) · Repasa [M1](02_Nivel_2_Intermedio.md#m1)

**4. ¿Qué paso adicional exige Communication Compliance para supervisar interacciones con Security Copilot?**

- a) Ninguno: basta con la licencia E5 de los usuarios
- b) Una licencia de Microsoft 365 Copilot para cada analista del SOC
- c) Un conector de partner aprovisionado con una entidad de servicio
- d) Habilitar en Security Copilot el permiso para que Purview procese los datos, además del pago por uso  ✅

*Respuesta: d).* Hay que activar en Security Copilot el permiso para que Purview procese los datos y habilitar el pago por uso; DLP y etiquetas no aplican a esas interacciones. [Fuente](https://learn.microsoft.com/en-us/purview/ai-security-copilot) · Repasa [M1](02_Nivel_2_Intermedio.md#m1)

**5. Un banco quiere impedir los correos entre Investigación y Banca de Inversión. ¿Qué usa?**

- a) Una política de Information Barriers
- b) Reglas de flujo de correo de Exchange  ✅
- c) Una política de Communication Compliance
- d) Unidades administrativas

*Respuesta: b).* Information Barriers no restringe el correo de Exchange Online; para eso se usan reglas de flujo de correo. CC detecta, pero no bloquea. [Fuente](https://learn.microsoft.com/en-us/purview/information-barriers) · Repasa [M2](02_Nivel_2_Intermedio.md#m2)

**6. ¿Qué modo de IB en SharePoint fija Teams y no puede administrar el administrador de SharePoint?**

- a) Open
- b) Owner Moderated
- c) Implicit  ✅
- d) Explicit

*Respuesta: c).* El modo Implicit lo fija Teams; Owner Moderated, Implicit y Explicit deshabilitan los vínculos «Cualquier persona» y «Toda la empresa». [Fuente](https://learn.microsoft.com/en-us/purview/information-barriers-sharepoint) · Repasa [M2](02_Nivel_2_Intermedio.md#m2)

**7. ¿Cuántos segmentos admite el modo multisegmento de Information Barriers?**

- a) Hasta 10 por usuario y 5.000 en total  ✅
- b) Uno por usuario y 250 en total
- c) Ilimitados por usuario y en total
- d) Hasta 3 por usuario y 1.000 en total

*Respuesta: a).* Multisegmento admite hasta 10 segmentos por usuario y 5.000 en total; Legacy, uno por usuario y hasta 250. [Fuente](https://learn.microsoft.com/en-us/purview/information-barriers-multi-segment) · Repasa [M2](02_Nivel_2_Intermedio.md#m2)

**8. ¿Qué cubre el reporte de cumplimiento de Information Barriers actualizado en septiembre de 2026?**

- a) Solo buzones de Exchange
- b) Chats y reuniones de Teams
- c) Sitios, OneDrive y contenedores de SharePoint Embedded propiedad de usuarios  ✅
- d) Planes premium de Planner

*Respuesta: c).* El reporte detecta sitios, OneDrive y contenedores de SharePoint Embedded propiedad de usuarios con segmentos incompatibles después de cambiar políticas. [Fuente](https://learn.microsoft.com/en-us/purview/information-barriers-sharepoint-report) · Repasa [M2](02_Nivel_2_Intermedio.md#m2)

**9. ¿En qué aplicaciones restringe Information Barriers la comunicación y la colaboración?**

- a) Exchange Online, Outlook y Teams
- b) Solo Teams, en chats y reuniones
- c) Teams, Viva Engage y Exchange Online
- d) Teams, SharePoint y OneDrive, y Planner solo en planes básicos  ✅

*Respuesta: d).* IB aplica en Teams, SharePoint y OneDrive, y en Planner solo para planes básicos; no restringe el correo. [Fuente](https://learn.microsoft.com/en-us/purview/information-barriers) · Repasa [M2](02_Nivel_2_Intermedio.md#m2)

**10. ¿Cuál es el comportamiento de privacidad por defecto en Communication Compliance?**

- a) El administrador global ve todas las alertas con los nombres reales
- b) Seudonimización activa y sin acceso por defecto para los administradores globales  ✅
- c) Los indicadores vienen activados y los nombres visibles para analistas
- d) Los nombres solo se ocultan en las exportaciones a eDiscovery

*Respuesta: b).* La privacidad por diseño incluye seudonimización por defecto, control de acceso por roles, opt-in explícito y auditoría; los administradores globales no tienen acceso por defecto. [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-solution-privacy) · Repasa [M3](02_Nivel_2_Intermedio.md#m3)

**11. ¿Qué limitación tienen las unidades administrativas en Communication Compliance?**

- a) No aplican a los reportes y no se combinan con ámbitos adaptables  ✅
- b) Solo funcionan para Information Barriers, no para políticas de CC
- c) Requieren pago por uso por cada unidad administrativa
- d) Desactivan la seudonimización para los revisores de la unidad

*Respuesta: a).* Las unidades administrativas acotan políticas y alertas por región o departamento, pero no aplican a los reportes y no se pueden combinar con ámbitos adaptables en CC. [Fuente](https://learn.microsoft.com/en-us/purview/communication-compliance-permissions) · Repasa [M3](02_Nivel_2_Intermedio.md#m3)

**12. En la integración entre Insider Risk Management y CC, ¿cuándo entra una persona en el alcance de IRM?**

- a) Con 1 mensaje de riesgo
- b) Con 10 mensajes de riesgo en una semana
- c) Cuando lo decide RR. HH.
- d) Con 5 o más mensajes de riesgo en 24 horas  ✅

*Respuesta: d).* Con la política «Insider risk trigger», quien envía 5 o más mensajes de riesgo en 24 horas entra en el alcance de IRM; puede tardar hasta 48 horas. [Fuente](https://learn.microsoft.com/en-us/purview/communication-compliance-policies) · Repasa [M4](02_Nivel_2_Intermedio.md#m4)

**13. ¿Qué clasificadores usa la política «Insider risk trigger» que se crea automáticamente?**

- a) Threat, Harassment y Discrimination  ✅
- b) Los seis clasificadores financieros
- c) Prompt Shields y Protected material
- d) Adult y Racy

*Respuesta: a).* La política se crea con Threat, Harassment y Discrimination; como Discrimination es solo en inglés, en español el desencadenante depende sobre todo de los otros dos. [Fuente](https://learn.microsoft.com/en-us/purview/communication-compliance-policies) · Repasa [M4](02_Nivel_2_Intermedio.md#m4)

<a id="eval-avanzado"></a>

## Nivel 3 · Avanzado · Evidencia, conectores y supervisión regulada

**1. ¿Qué debes planificar para la evidencia de auditoría de Communication Compliance (por ejemplo, SupervisionRuleMatch)?**

- a) Nada: la lista de actividades del portal ya muestra estas operaciones
- b) Migrar de Search-UnifiedAuditLog a la API AuditLogQuery antes del 15 de octubre de 2027  ✅
- c) Exportar las coincidencias desde eDiscovery (Premium) en lugar de usar la auditoría
- d) Activar Audit (Premium), que mantiene Search-UnifiedAuditLog después de 2027

*Respuesta: b).* Las actividades de CC se consultan con Search-UnifiedAuditLog, que se retira el 15 de octubre de 2027; la API AuditLogQuery está en GA desde octubre de 2026. [Fuente](https://mc.merill.net/message/MC1505599) · Repasa [A2](03_Nivel_3_Avanzado.md#a2)

**2. ¿Qué tipo de registro de auditoría corresponde a Communication Compliance?**

- a) InformationBarrierPolicyApplication
- b) ComplianceConnector
- c) ComplianceSupervisionExchange  ✅
- d) SharePointFileOperation

*Respuesta: c).* CC usa ComplianceSupervisionExchange; Information Barriers, InformationBarrierPolicyApplication; y los conectores de datos, ComplianceConnector. [Fuente](https://learn.microsoft.com/en-us/purview/audit-supported-services) · Repasa [A2](03_Nivel_3_Avanzado.md#a2)

**3. ¿Cuál es la retención por defecto del registro de auditoría con Audit (Standard)?**

- a) 90 días
- b) 180 días  ✅
- c) 1 año
- d) 10 años

*Respuesta: b).* Audit (Standard) retiene 180 días; Audit (Premium), hasta 1 año; y 10 años requiere un complemento por usuario. [Fuente](https://learn.microsoft.com/en-us/purview/audit-solutions-overview) · Repasa [A2](03_Nivel_3_Avanzado.md#a2)

**4. ¿Qué límites tiene la API AuditLogQuery según el aviso MC1505599?**

- a) Hasta 1 millón de registros por consulta, 200 búsquedas cada 24 horas y 50 en cola por tenant  ✅
- b) Hasta 50.000 registros por consulta y 10 búsquedas simultáneas por usuario
- c) Sin límites mientras exista una licencia de Audit (Premium)
- d) Hasta 100.000 registros por consulta y 20 búsquedas cada 24 horas

*Respuesta: a).* La API admite hasta 1 millón de registros por consulta, 200 búsquedas cada 24 horas y 50 búsquedas en cola por tenant. [Fuente](https://mc.merill.net/message/MC1505599) · Repasa [A2](03_Nivel_3_Avanzado.md#a2)

**5. ¿Qué requiere un conector de un partner, como 17a-4 o TeleMessage?**

- a) Nada adicional a la licencia E5 de los usuarios
- b) Audit (Premium) y una licencia de Copilot para el administrador
- c) Un servidor local de Veritas como intermediario
- d) Una entidad de servicio aprovisionada y una relación comercial con el partner  ✅

*Respuesta: d).* Los conectores de partners requieren una entidad de servicio aprovisionada y, según la descripción de servicio, una relación comercial con el partner. [Fuente](https://learn.microsoft.com/en-us/purview/archive-third-party-data) · Repasa [A1](03_Nivel_3_Avanzado.md#a1)

**6. ¿Cómo mapea usuarios el conector de Instant Bloomberg?**

- a) Por CorporateEmailAddress o con un archivo CSV  ✅
- b) Por el número de teléfono registrado en Bloomberg
- c) Por la dirección IP del terminal de Bloomberg
- d) No mapea usuarios: importa todo a un buzón común

*Respuesta: a).* El conector mapea por CorporateEmailAddress o con un CSV; los elementos sin un usuario válido no se importan. [Fuente](https://learn.microsoft.com/en-us/purview/archive-instant-bloomberg-data) · Repasa [A1](03_Nivel_3_Avanzado.md#a1)

**7. ¿Qué ocurrió con los conectores de Veritas?**

- a) Siguen disponibles
- b) Pasaron a vista previa
- c) Se retiraron el 30 de junio de 2024  ✅
- d) Se integraron a Information Barriers

*Respuesta: c).* Todos los conectores de Veritas se retiraron el 30 de junio de 2024; hoy los partners son TeleMessage, 17a-4 y CellTrust. [Fuente](https://learn.microsoft.com/en-us/purview/archive-third-party-data) · Repasa [A1](03_Nivel_3_Avanzado.md#a1)

**8. ¿Qué dice la documentación sobre PowerShell para las políticas de Communication Compliance?**

- a) Es la vía recomendada y la única que admite plantillas
- b) La página de políticas dice que no es compatible, aunque los cmdlets SupervisoryReviewPolicyV2 siguen documentados  ✅
- c) Solo funciona en las nubes GCC y GCC High
- d) Es obligatorio para crear la plantilla financiera

*Respuesta: b).* Es una contradicción documental: la página de políticas dice que PowerShell no es compatible, pero los cmdlets heredados siguen publicados. Úsalos solo para inventario. [Fuente](https://learn.microsoft.com/en-us/purview/communication-compliance-policies) · Repasa [A3](03_Nivel_3_Avanzado.md#a3)

**9. ¿Qué licencia necesita la plantilla de Power Automate «Notify manager when a user has a Communication Compliance alert»?**

- a) Power Automate Premium para cada revisor que reciba avisos
- b) Una licencia de Copilot Studio para el flujo
- c) No requiere licencias adicionales de Power Automate; las funciones premium sí pueden requerirlas  ✅
- d) Pago por uso de Purview por cada ejecución del flujo

*Respuesta: c).* La plantilla por defecto no requiere licencias extra de Power Automate; las funciones premium o el conector de Purview pueden requerirlas. [Fuente](https://learn.microsoft.com/en-us/purview/communication-compliance-power-automate) · Repasa [A3](03_Nivel_3_Avanzado.md#a3)

**10. ¿Qué afirmación sobre la plantilla de cumplimiento normativo financiero es correcta?**

- a) Usa seis clasificadores que funcionan en español y portugués
- b) Revisa el 100 % de los mensajes y no admite conectores
- c) Usa seis clasificadores solo en inglés y una revisión del 10 %  ✅
- d) Bloquea los mensajes antes de enviarse si detecta manipulación

*Respuesta: c).* La plantilla usa seis clasificadores financieros, solo en inglés, con una revisión del 10 %; CC no bloquea mensajes. [Fuente](https://learn.microsoft.com/en-us/purview/communication-compliance-policies) · Repasa [A4](03_Nivel_3_Avanzado.md#a4)

**11. Según una guía de un partner sobre FINRA 3110, ¿qué papel cumple Communication Compliance?**

- a) Reemplaza los procedimientos de supervisión escritos si la política está documentada
- b) Cubre la conservación WORM que exigen SEC 17a-4 y FINRA 4511
- c) Elimina la necesidad de un principal registrado gracias a los clasificadores
- d) Apoya la revisión, pero no reemplaza los procedimientos escritos ni la revisión por un principal registrado  ✅

*Respuesta: d).* FINRA 3110 exige revisión por un principal registrado con evidencia escrita; CC apoya esa revisión, pero no sustituye los procedimientos de supervisión escritos. [Fuente](https://i3solutions.com/answers/finra-sec-microsoft-365-recordkeeping-supervision/) · Repasa [A4](03_Nivel_3_Avanzado.md#a4)

**12. ¿Qué capacidad de Purview cubre la conservación exigida por SEC 17a-4, FINRA 4511 y CFTC 1.31?**

- a) La retención y la gestión de registros, según la evaluación de Cohasset  ✅
- b) Communication Compliance, que conserva las coincidencias hasta 7 años
- c) Information Barriers, que congela los chats entre segmentos
- d) Power Automate, que copia los mensajes a un repositorio WORM

*Respuesta: a).* La evaluación de Cohasset concluye que Exchange, Teams, SharePoint, OneDrive y Viva Engage, bien configurados con retención, cumplen esas reglas; CC cubre la supervisión, no la conservación. [Fuente](https://learn.microsoft.com/en-us/purview/retention-regulatory-requirements) · Repasa [A4](03_Nivel_3_Avanzado.md#a4)

**13. ¿Qué clasificador financiero genera ruido con boletines y se beneficia de Filter email blasts?**

- a) Customer complaints
- b) Money laundering
- c) Gifts & entertainment
- d) Regulatory collusion  ✅

*Respuesta: d).* Las definiciones advierten que Regulatory collusion genera ruido con boletines; filtrar envíos masivos lo reduce. [Fuente](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions) · Repasa [A4](03_Nivel_3_Avanzado.md#a4)

<a id="eval-operacion"></a>

## Nivel 4 · Operación · Modelo operativo, métricas y gobierno

**1. ¿Qué partes interesadas recomienda Microsoft involucrar al planificar Communication Compliance?**

- a) TI y seguridad; Legal y RR. HH. solo si hay un incidente
- b) TI, cumplimiento, privacidad, seguridad, RR. HH. y Legal  ✅
- c) Cumplimiento y Legal; TI solo ejecuta
- d) El SOC y el administrador global

*Respuesta: b).* La planificación recomienda involucrar a TI, cumplimiento, privacidad, seguridad, RR. HH. y Legal desde el inicio. [Fuente](https://learn.microsoft.com/es-es/purview/communication-compliance-plan) · Repasa [O1](04_Nivel_4_Operacion.md#o1)

**2. ¿Qué recomienda la planificación sobre políticas y revisores en organizaciones con varios países?**

- a) Que los revisores sean los gerentes directos de las personas supervisadas
- b) Una sola política global con revisores centralizados que trabajen en inglés
- c) Separar políticas por región y usar revisores que hablen el idioma de los usuarios  ✅
- d) Que los revisores sean administradores globales para ver todas las alertas

*Respuesta: c).* Separar políticas por región y asignar revisores que hablen el idioma de las personas supervisadas mejora la calidad de la revisión y facilita el cumplimiento local. [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-plan) · Repasa [O1](04_Nivel_4_Operacion.md#o1)

**3. ¿Cómo se reparte la separación de funciones en Communication Compliance?**

- a) Los administradores configuran políticas; analistas e investigadores revisan alertas  ✅
- b) Un mismo rol configura, revisa e investiga para ganar agilidad
- c) RR. HH. configura las políticas y TI revisa las alertas
- d) Cada revisor crea y ajusta sus propias políticas

*Respuesta: a).* La guía de privacidad separa a quienes configuran (administradores) de quienes revisan e investigan alertas (analistas e investigadores). [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-solution-privacy) · Repasa [O1](04_Nivel_4_Operacion.md#o1)

**4. El contador de pendientes nuevos de hoy en Communication Compliance…**

- a) Acumula toda la semana
- b) Se reinicia cada día en UTC  ✅
- c) Se reinicia cada mes
- d) Nunca se reinicia

*Respuesta: b).* El contador de pendientes nuevos se reinicia cada día en UTC; tenlo en cuenta si tu equipo trabaja en otra zona horaria. [Fuente](https://learn.microsoft.com/es-es/purview/communication-compliance-investigate-remediate) · Repasa [O2](04_Nivel_4_Operacion.md#o2)

**5. ¿En qué porcentajes avisa Communication Compliance sobre el almacenamiento de una política?**

- a) 50, 75 y 90 %
- b) 60, 80 y 100 %
- c) 80, 90 y 95 %  ✅
- d) Solo al 100 %

*Respuesta: c).* Avisa al 80, 90 y 95 % del límite de 100 GB o 1 millón de mensajes; al llegar al límite, la política se desactiva. [Fuente](https://learn.microsoft.com/en-us/purview/communication-compliance-policies) · Repasa [O2](04_Nivel_4_Operacion.md#o2)

**6. ¿Qué opción reduce el ruido de boletines y envíos masivos en una política?**

- a) Desactivar el OCR
- b) Aumentar el porcentaje de revisión
- c) Agregar más revisores
- d) Filter email blasts  ✅

*Respuesta: d).* Filter email blasts excluye envíos masivos; Policy health (vista previa) lo recomienda cuando detecta ese ruido. [Fuente](https://learn.microsoft.com/en-us/purview/communication-compliance-policies) · Repasa [O2](04_Nivel_4_Operacion.md#o2)

**7. ¿Qué función permite retroalimentar un clasificador cuando una coincidencia es incorrecta?**

- a) Report as Misclassified  ✅
- b) Escalar para investigación
- c) Quitar mensaje de Teams
- d) Notificar

*Respuesta: a).* La nota de transparencia describe «Report as Misclassified» como el mecanismo para reportar clasificaciones erróneas. [Fuente](https://learn.microsoft.com/en-us/purview/communication-compliance-solution-overview) · Repasa [O2](04_Nivel_4_Operacion.md#o2)

**8. Según Microsoft, ¿quién es responsable de la legalidad de monitorear, bloquear o retener comunicaciones?**

- a) Microsoft, como proveedor del servicio en la nube
- b) El proveedor de la app de IA supervisada
- c) La organización, que debe consultar asesoría legal  ✅
- d) El regulador local, que aprueba cada política

*Respuesta: c).* Microsoft deja esa responsabilidad en la organización y recomienda consultar asesoría legal antes de desplegar clasificadores. [Fuente](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions) · Repasa [O3](04_Nivel_4_Operacion.md#o3)

**9. ¿Desde cuándo está vigente la Ley 21.719 de Chile?**

- a) 13 de diciembre de 2024
- b) 20 de marzo de 2025
- c) 31 de marzo de 2025
- d) 1 de diciembre de 2026  ✅

*Respuesta: d).* Se publicó el 13 de diciembre de 2024 y entra en vigencia el 1 de diciembre de 2026; el 20 de marzo de 2025 es la publicación de la LFPDPPP de México. [Fuente](https://www.bcn.cl/leychile/navegar?i=1209272&f=2026-12-01) · Repasa [O3](04_Nivel_4_Operacion.md#o3)

**10. ¿Qué incorpora el reglamento peruano DS 016-2024-JUS según la fuente oficial?**

- a) Un oficial de datos personales y la notificación de incidentes en 48 horas  ✅
- b) La prohibición de supervisar comunicaciones de empleados
- c) El uso obligatorio de herramientas certificadas de supervisión
- d) La notificación de incidentes en 30 días hábiles a la ANPD

*Respuesta: a).* El reglamento incorpora el oficial de datos personales y la notificación de incidentes en 48 horas; su interpretación para tu caso corresponde a Legal. [Fuente](https://www.gob.pe/institucion/anpd/normas-legales/6554453) · Repasa [O3](04_Nivel_4_Operacion.md#o3)

**11. Antes de supervisar las comunicaciones de un grupo piloto de personas reales, ¿qué debes tener?**

- a) Solo la licencia E5 y la seudonimización activa
- b) Aprobación previa de Legal, RR. HH. y privacidad, aviso a las personas y una política de prueba con alcance acotado  ✅
- c) Un reporte de cumplimiento de IB y la auditoría activa
- d) La aprobación del administrador global y del gerente del área

*Respuesta: b).* Es la regla de esta guía, apoyada en las partes interesadas que recomienda la planificación de CC: sin aprobación previa ni alcance acotado no se supervisa a personas reales. [Fuente](https://learn.microsoft.com/es-es/purview/communication-compliance-plan) · Repasa [O3](04_Nivel_4_Operacion.md#o3)

**12. ¿Qué recomienda una guía independiente para supervisar poblaciones grandes sin saturar a los revisores?**

- a) Revisar siempre el 100 % de los mensajes para no perder nada
- b) Desactivar la seudonimización para acelerar la revisión
- c) Concentrar la revisión en un único revisor experto
- d) Muestreo y pilotos acotados por departamento o clasificador  ✅

*Respuesta: d).* La guía recomienda pilotos acotados, muestreo para poblaciones grandes y vigilar los falsos positivos durante las primeras semanas. [Fuente](https://solvingmicrosoft365.com/guides/purview-communication-compliance/) · Repasa [O1](04_Nivel_4_Operacion.md#o1)

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. No constituye asesoría legal ni laboral: las decisiones sobre supervisión de comunicaciones, privacidad, avisos a empleados y relaciones laborales corresponden a tus áreas de Legal, RR. HH. y privacidad. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

# Cierre, glosario y fuentes

*Microsoft Purview Communication Compliance e Information Barriers Ninja Training · Edición 2026*

[← Laboratorio y práctica en producción](07_Laboratorio_y_practica_en_produccion.md) · [Índice del programa](README.md)

<a id="cierre"></a>

## ¿Y ahora?

Ser Ninja de Communication Compliance e Information Barriers no es saber dónde está cada botón: es poder defender cada decisión ante Legal, RR. HH., privacidad, un regulador o la persona supervisada. Tus siguientes pasos: la credencial Applied Skills de retención, eDiscovery y Communication Compliance, el knowledge check del Ninja oficial y los programas de Insider Risk Management, eDiscovery y Audit, y DSPM y seguridad de datos para IA de esta serie.

Dedica media hora al mes a la página de novedades de Purview y al Message Center, revisa este programa después de Microsoft Ignite y comparte con tu equipo cualquier dato desactualizado o enlace roto que encuentres: la guía está pensada para mantenerse viva, como el Ninja original. Para preguntas técnicas, la Microsoft Security Community y Microsoft Q&A son los mejores lugares; para preguntas legales, tu área de Legal.

<a id="glosario"></a>

## Glosario

| Término | Definición |
|---|---|
| Communication Compliance (CC) | Solución de Microsoft Purview que detecta, captura y permite revisar comunicaciones que podrían infringir políticas internas o requisitos regulatorios, con revisión humana y privacidad por diseño. |
| Information Barriers (IB) | Solución que impide, en ambos sentidos, la comunicación y la colaboración entre segmentos de usuarios en Teams, SharePoint, OneDrive y Planner (planes básicos); no restringe el correo. |
| Política de CC | Configuración que define usuarios supervisados, canales, condiciones, porcentaje de revisión y revisores; su nombre no se puede cambiar después de crearla. |
| Plantilla | Política preconfigurada para un escenario: conflicto de intereses, interacciones de Copilot, contenido inapropiado, imágenes o texto inapropiados, cumplimiento financiero o información confidencial. |
| Clasificador entrenable preentrenado | Modelo de Microsoft que reconoce un tipo de contenido (por ejemplo, Threat o Money laundering); CC no admite clasificadores personalizados. |
| Clasificadores LLM de seguridad de contenido | Hate, Sexual, Violence y Self-harm: evalúan Copilot, Teams y Viva Engage con una severidad de 0 a 7 y alertan desde 4. |
| Prompt Shields | Clasificador que detecta intentos de jailbreak o de inyección en los prompts de IA. |
| Protected material | Clasificador que detecta texto protegido por derechos de autor o de marca en las respuestas de IA. |
| SIT | Tipo de información confidencial: patrón con validaciones y palabras clave que identifica datos como números de identificación o de tarjetas. |
| Diccionario de palabras clave | Lista de términos que se usa como condición de una política; admite hasta 100 KB comprimidos. |
| Probar condiciones | Función que valida clasificadores y SIT con un mensaje o un archivo de texto antes de crear la política. |
| OCR de CC | Extracción de texto de imágenes de 100 KB a 4 MB en correo y chats de Teams; es propio de CC y puede tardar hasta 48 horas. |
| Coincidencia de política | Mensaje que cumplió las condiciones de una política y queda pendiente de revisión. |
| Conservación de coincidencias | Período de 1 mes a 7 años (1 año por defecto) durante el cual se conservan las coincidencias de una política; vigente desde el 1 de junio de 2025. |
| Seudonimización | Sustitución de los nombres de usuario por alias durante la revisión; viene activa por defecto. |
| Unidad administrativa | Agrupación de usuarios de Entra que limita qué políticas y alertas ve un administrador o revisor; no aplica a los reportes. |
| Ámbito adaptable | Alcance dinámico basado en atributos; en CC no se combina con unidades administrativas ni cubre los canales públicos de Teams. |
| Escalar para investigación | Acción de revisión que crea un caso de eDiscovery (Premium) con hasta 100 mensajes. |
| Insider risk trigger | Política de CC creada automáticamente al usar CC como desencadenante de Insider Risk Management; con 5 o más mensajes de riesgo en 24 horas, la persona entra en el alcance de IRM. |
| Mensajes notificados por usuarios | Política que recibe los mensajes que las personas reportan en Teams (y en Viva Engage, en vista previa). |
| Filter email blasts | Opción que excluye envíos masivos y boletines para reducir falsos positivos. |
| Policy health | Función en vista previa que recomienda mejoras de una política, como filtrar envíos masivos o reducir puntos ciegos de alcance. |
| Pago por uso (PAYG) | Facturación mensual por consumo, vinculada a una suscripción de Azure del mismo tenant, que CC usa para la IA que no es de Microsoft 365. |
| Registro de texto | Unidad de cobro de CC con pago por uso: 1.000 caracteres, redondeados hacia arriba; hay un medidor estándar y uno premium. |
| Segmento | Grupo de usuarios definido por un atributo de directorio (por ejemplo, Department) al que se aplican las políticas de IB. |
| Modo de IB | Legacy (un segmento por usuario, hasta 250, con libretas de direcciones), segmento único o multisegmento (hasta 10 por usuario y 5.000 en total). |
| Modo de sitio de IB | Open, Owner Moderated, Implicit o Explicit: define el acceso, el uso compartido y la membresía de sitios de SharePoint y OneDrive. |
| ABP | Directiva de libreta de direcciones de Exchange; en el modo Legacy hay que eliminar las existentes antes de habilitar IB. |
| Búsqueda de directorio con ámbito | Configuración de Teams que IB necesita para limitar la búsqueda de personas según las políticas. |
| Reporte de cumplimiento de IB | Reporte de SharePoint Online Management Shell que detecta sitios, OneDrive y contenedores de SharePoint Embedded con segmentos incompatibles. |
| SupervisionRuleMatch | Operación de auditoría que registra una coincidencia de una política de CC (tipo de registro ComplianceSupervisionExchange). |
| AuditLogQuery | API de Microsoft Graph para búsquedas asíncronas del registro de auditoría; en GA desde octubre de 2026 y reemplazo de Search-UnifiedAuditLog. |
| Conector de datos | Integración que importa comunicaciones de terceros (Bloomberg, ICE Chat, partners) a buzones de Microsoft 365 para aplicarles CC, retención y eDiscovery. |
| Principal registrado | En la normativa estadounidense (FINRA 3110), persona habilitada que revisa comunicaciones y deja evidencia escrita; en MCSA, el equivalente lo define el regulador local. |

<a id="metodologia"></a>

## Metodología y fuentes

Esta guía se construyó con líneas de investigación en paralelo sobre fuentes públicas: la forma y la historia del Ninja oficial, cada nivel técnico, la operación y la comunidad. Cada enlace se registró solo si apareció literalmente en un resultado de búsqueda o en una página leída, y luego se consolidó, se depuró y se verificó. Se descartaron recursos retirados, alojados en espacios no públicos o duplicados. Fecha de corte: 6 de noviembre de 2026.

Puntos a confirmar en fuentes oficiales antes de recomendarlos:

- PowerShell: la página de políticas afirma que PowerShell no es compatible para crear o administrar políticas de CC, pero los cmdlets `*-SupervisoryReviewPolicyV2` siguen documentados y aún mencionan el portal retirado ([políticas](https://learn.microsoft.com/en-us/purview/communication-compliance-policies), [cmdlet](https://learn.microsoft.com/en-us/powershell/module/exchangepowershell/new-supervisoryreviewpolicyv2?view=exchange-ps)).
- Nombre del clasificador: la plantilla de texto inapropiado cita «Targeted harassment», mientras la tabla de definiciones solo incluye «Harassment» ([definiciones](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions)).
- Latencia: la página de canales (actualizada en agosto de 2025) indica hasta 48 horas en Teams y unas 24 horas en Exchange, mientras la página de políticas indica 1 hora para el cuerpo del mensaje en políticas creadas desde el 31 de julio de 2022 ([canales](https://learn.microsoft.com/en-us/purview/communication-compliance-channels)).
- Clasificadores LLM: la misma página de políticas dice que evalúan mensajes de 3 o más palabras y, más abajo, de 5 o más ([políticas](https://learn.microsoft.com/en-us/purview/communication-compliance-policies)).
- Licencias en español: la página de planeamiento en español aún menciona «Office 365 E3 + complemento Advanced Compliance», que no figura en la descripción de servicio vigente; prevalece la descripción de servicio ([planeamiento](https://learn.microsoft.com/es-es/purview/communication-compliance-plan)). El laboratorio comunitario de Indra y el marco FSI Copilot Governance repiten esa licencia antigua.
- Alertas por política: RM529852 anunció GA en enero de 2026 para GCC, GCC High y DoD, mientras MC920304 retrasó la vista previa mundial a octubre de 2026 y deja la GA por anunciar; confírmalo en el [roadmap oficial](https://www.microsoft.com/microsoft-365/roadmap?id=529852).
- Auditoría: la documentación de CC depende de `Search-UnifiedAuditLog`, que se retira el 15 de octubre de 2027, y ninguna página revisada confirma explícitamente que todas las operaciones de CC se consulten igual con la API AuditLogQuery: pruébalo en tu tenant antes de migrar ([MC1505599](https://mc.merill.net/message/MC1505599)).
- Transcripciones de Teams: la página de canales las da por incluidas, la página de Teams las menciona como vista previa y los clasificadores LLM no las evalúan ([Teams](https://learn.microsoft.com/en-us/purview/communication-compliance-teams)).
- Claude Enterprise: la versión en inglés indica que CC es compatible (agosto de 2026), pero algunas copias localizadas aún dicen que no ([Claude Enterprise](https://learn.microsoft.com/en-us/purview/ai-claude-enterprise)).
- Agentes y apps de IA conectadas a Entra: la página de canales las trata con pago por uso y la descripción de servicio indica que las capacidades de Purview para agentes de Microsoft Foundry y apps conectadas a Entra se soportan con Microsoft 365 E7 y Agent 365; no queda claro cuál aplica a CC ([descripción de servicio](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)).
- Licencia de Information Barriers: la descripción de servicio exige licencia para los usuarios de los segmentos asignados, pero la sección revisada no enumera los SKU; confírmalo con tu equipo de licenciamiento.
- Information Barriers en Teams: la guía de inicio pide esperar 24 horas tras habilitar la búsqueda de directorio con ámbito y la página de Teams habla de «algunas horas»; además, la guía de solución de problemas usa `Get-InformationBarrierRecipientStatus` y la guía de inicio vigente, `Get-ExoInformationBarrierRelationship` ([solución de problemas](https://learn.microsoft.com/en-us/troubleshoot/microsoft-365/purview/information-barriers/information-barriers-troubleshooting)).
- Libro de terceros: «Microsoft Purview 2025: Security Solutions» afirma que Information Barriers aplica a Exchange; la documentación oficial lo niega ([Information Barriers](https://learn.microsoft.com/en-us/purview/information-barriers)).
- Perú: la ANPD indica que el nuevo reglamento de la Ley 29733 rige desde el 31 de marzo de 2025 y algunas firmas legales citan el 30 de marzo ([DS 016-2024-JUS](https://www.gob.pe/institucion/anpd/normas-legales/6554453)).
- Copilot Studio, Fabric y Security Copilot: se anunciaron en vista previa en Ignite 2024 y la documentación actual los trata como canales disponibles con pago por uso, sin un anuncio de GA identificado ([anuncio de Ignite 2024](https://techcommunity.microsoft.com/blog/microsoft-security-blog/new-purview-communication-compliance-features-for-copilot-and-insider-risk-manag/4296775)).
- Crédito de Visual Studio Enterprise: ninguna página revisada confirma que cubra los medidores de pago por uso de Purview; trátalo como no garantizado y configura presupuesto y alertas.
- Fechas aproximadas y credenciales: el episodio 11 de la serie SC-401 (marzo de 2026, fecha aproximada) y el video de Microsoft Mechanics sobre IRM y CC (unos cuatro años) tienen fecha estimada, y la guía de SC-401 vigente no mide CC ni IB ([guía SC-401](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-401)).
- Fuentes de partners y comunidad: la guía de i3solutions cita reglas de EE. UU. al 21 de septiembre de 2026 y no sustituye la lectura de la norma ni la interpretación de tu regulador local; el autor del marco FSI Copilot Governance no está verificado y la guía de Solving Microsoft 365 simplifica algunas descripciones de roles.
- Microsoft Ignite (17 al 20 de noviembre de 2026) puede cambiar estados de vista previa citados aquí —mejoras de alertas, Policy health, mensajes notificados en Viva Engage, conector de Claude—: revisa la [página de novedades](https://learn.microsoft.com/en-us/purview/whats-new) después del evento.

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. No constituye asesoría legal ni laboral: las decisiones sobre supervisión de comunicaciones, privacidad, avisos a empleados y relaciones laborales corresponden a tus áreas de Legal, RR. HH. y privacidad. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

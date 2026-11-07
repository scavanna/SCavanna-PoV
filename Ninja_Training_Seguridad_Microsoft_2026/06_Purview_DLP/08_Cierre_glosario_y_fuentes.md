# Cierre, glosario y fuentes

*Microsoft Purview Data Loss Prevention Ninja Training · Edición 2026*

[← Laboratorio y práctica en producción](07_Laboratorio_y_practica_en_produccion.md) · [Índice del programa](README.md)

<a id="cierre"></a>

## ¿Y ahora?

Ser Ninja de DLP es un hábito: lee cada mes las [novedades de Purview](https://learn.microsoft.com/en-us/purview/whats-new), revisa tus directivas con datos y no con intuición, y mantén siempre una copia v2 en simulación antes de tocar lo que protege al negocio. Después de Ignite (17 al 20 de noviembre de 2026), vuelve a validar los estados de vista previa y las contradicciones que esta guía señala.

Próximos pasos: el examen [SC-401](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-401), la [ruta Ninja de Learn](https://learn.microsoft.com/en-us/training/paths/purview-ninja-safeguard-data/) y los programas hermanos de esta serie: Information Protection para la clasificación y las etiquetas, Insider Risk Management para la protección adaptativa, DSPM para la postura de IA, Defender XDR y Sentinel para el SOC, Security Copilot para los agentes y Entra para Global Secure Access.

<a id="glosario"></a>

## Glosario

| Término | Definición |
|---|---|
| Activity explorer (explorador de actividad) | Vista de Purview con hasta 30 días de actividades sobre contenido etiquetado y coincidencias DLP, con una demora de 60 a 90 minutos. |
| Adaptive Protection (protección adaptativa) | Integración de Insider Risk Management con DLP, retención y Acceso condicional que aplica controles según el nivel de riesgo de cada persona: Elevated, Moderate o Minor. |
| Agent 365 | Plataforma de Microsoft para gobernar agentes de IA; sus instancias pueden incluirse en directivas DLP como si fueran usuarios. |
| Alert tuning (ajuste de alertas) | Reglas de Defender XDR que ocultan, resuelven o convierten alertas en behaviors; una regla integrada lo hace con las señales DLP desde octubre de 2026. |
| Behavior (comportamiento) | Señal registrada en las tablas BehaviorInfo y BehaviorEntities de Defender XDR que no genera alerta ni incidente por sí misma. |
| Clasificador entrenable | Modelo de aprendizaje automático, integrado o personalizado, que reconoce tipos de contenido como contratos o currículums. |
| Content explorer | Vista de Purview que muestra dónde está el contenido clasificado y permite dar retroalimentación sobre las coincidencias. |
| Data Security Investigations | Solución de pago por uso para buscar y analizar con IA el contenido afectado por un incidente de seguridad de datos. |
| Directiva de recopilación | Directiva que define qué actividades y contenidos se capturan, incluidos los prompts y las respuestas de IA. |
| DSPM | Data Security Posture Management: postura de seguridad de datos de Purview; su nueva versión está en disponibilidad general desde mayo de 2026. |
| Edge for Business (protección en línea) | DLP integrada en el navegador que protege apps gestionadas y no gestionadas sin incorporar el dispositivo. |
| EDM (Exact Data Match) | Tipo de información confidencial que compara el contenido contra valores reales de una tabla mediante hashes. |
| Endpoint DLP | DLP en Windows 10/11 y macOS que audita o restringe actividades como USB, impresión, nube, portapapeles, red y FTP/SFTP. |
| Global Secure Access | Solución de acceso seguro de Microsoft Entra (Internet Access y Private Access) que habilita la seguridad de datos de red de Purview. |
| Huella digital de documento | Tipo de información confidencial creado a partir de un formulario o una plantilla, con coincidencia parcial o exacta. |
| Instances | Ubicación clásica de DLP para apps en la nube de terceros mediante Defender for Cloud Apps; se retira el 6 de enero de 2027. Algunas páginas aún la llaman «Microsoft Cloud App Security instance». |
| Invalidación (override) | Opción que permite a la persona continuar pese a un bloqueo, con una justificación que queda registrada. |
| JIT (just-in-time) | Protección de Endpoint DLP que controla las salidas mientras un archivo se clasifica; no genera eventos DLPRuleMatch ni alertas. |
| Modo de simulación | Estado de una directiva que evalúa contenido sin aplicar acciones; reemplazó a los antiguos estados de prueba. |
| Nivel de confianza | Grado de certeza de una coincidencia de un tipo de información confidencial: baja (≤65), media (75) o alta (85). |
| OCR | Reconocimiento óptico de caracteres para detectar información sensible en imágenes y PDF escaneados; se factura por pago por uso. |
| Pago por uso (pay-as-you-go) | Modelo de facturación de Purview mediante una suscripción de Azure que se suma a la licencia por usuario y no la reemplaza. |
| processContent | API de Microsoft Graph con la que una app evalúa contenido, como un prompt, contra las directivas de Purview. |
| Purview Data Security AI Admin | Rol de mínimo privilegio para administrar la DLP de Copilot sin poder leer prompts ni respuestas. |
| Purview Suite | Microsoft Purview Suite, nombre actual del complemento antes llamado Microsoft 365 E5 Compliance. |
| Recolección de evidencia | Copia a Azure Storage de los archivos que coinciden con directivas de Endpoint DLP, para investigación y triage. |
| SASE / SSE | Arquitecturas de seguridad de red entregadas desde la nube; Purview se integra con socios del Security Store para inspección en línea. |
| SCU | Security Compute Unit: unidad de capacidad que consumen Security Copilot y sus agentes. |
| SIT | Tipo de información confidencial (sensitive information type): patrón, palabras clave y validaciones que identifican un dato sensible. |
| Sugerencia de directiva (policy tip) | Aviso que informa a la persona que su acción coincide con una directiva DLP y, según la configuración, le permite invalidar o reportar. |
| Triage Agent | Microsoft Purview Triage Agent (Data Security Triage Agent en el Centro de mensajes): agente de Security Copilot que prioriza alertas de DLP e Insider Risk. |
| Unidad administrativa | Ámbito de Entra ID que limita qué usuarios, grupos o sitios puede administrar o investigar un rol. |

<a id="metodologia"></a>

## Metodología y fuentes

Esta guía se construyó con líneas de investigación en paralelo sobre fuentes públicas: la forma y la historia del Ninja oficial, cada nivel técnico, la operación y la comunidad. Cada enlace se registró solo si apareció literalmente en un resultado de búsqueda o en una página leída, y luego se consolidó, se depuró y se verificó. Se descartaron recursos retirados, alojados en espacios no públicos o duplicados. Fecha de corte: 6 de noviembre de 2026.

Puntos a confirmar en fuentes oficiales antes de recomendarlos:

- **DLP de prompts en Copilot.** El [blog oficial del 21 de abril de 2026](https://techcommunity.microsoft.com/blog/microsoft-security-blog/safeguarding-sensitive-data-in-microsoft-365-copilot-interactions-dlp-for-micros/4512497) la declara en disponibilidad general, mientras que la [página de Learn del 27 de octubre de 2026](https://learn.microsoft.com/en-us/purview/dlp-microsoft365-copilot-location-learn-about) la describe como vista previa en despliegue. Esta guía la trata como vista previa hasta confirmarlo después de Ignite.
- **Estado de la ubicación Microsoft 365 Copilot.** La [página general de DLP](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp) (26 de junio de 2026) la rotula como vista previa, aunque el control por etiquetas existe desde noviembre de 2024 y la descripción de servicio lo licencia.
- **Búsqueda web en Copilot.** El blog de abril de 2026 la presentaba como vista previa, un MVP citó una GA prevista para junio de 2026 ([Office 365 for IT Pros](https://office365itpros.com/2026/04/16/dlp-policy-for-copilot-web/)) y Learn ya no la rotula como vista previa.
- **Licencia de la DLP de red.** La [descripción de servicio](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description) dice que es pago por uso; la [página de seguridad de datos de red](https://learn.microsoft.com/en-us/purview/dlp-network-data-security-learn) indica que con Global Secure Access no se requiere pago por uso (sí Microsoft 365 E7, o Purview E5 más Entra Internet Access) y que el pago por uso aplica a los socios SASE.
- **Versiones de macOS.** La descripción de servicio dice «Catalina 10.15 y superior»; [Learn](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp), «las tres versiones más recientes». Planifica con la más restrictiva.
- **Estado y licencia del agente de triage.** La [guía de inicio](https://learn.microsoft.com/en-us/purview/copilot-in-purview-triage-dlp-agent-get-started) (25 de junio de 2026) no lo rotula como vista previa, la [página de agentes de Purview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-agents) sí (y describe una autenticación que vence a los 90 días, anterior a Entra Agent ID), y el Centro de mensajes pospuso a agosto de 2027 la GA de sus resúmenes en Defender XDR ([MC1255406](https://mc.merill.net/message/MC1255406)). La traza de razonamiento figura con GA prevista para octubre de 2026, pero con estado «In development» en la hoja de ruta.
- **Alertas DLP en Defender XDR.** La página general de DLP dice que las alertas se envían a Defender y se conservan seis meses; desde octubre de 2026 la regla integrada las convierte en behaviors ([investigar DLP en Defender](https://learn.microsoft.com/en-us/defender-xdr/dlp-investigate-alerts-defender)) y `alerts_v2` no devuelve las alertas ajustadas ([migración](https://learn.microsoft.com/en-us/graph/alertsv1-alertsv2-migration)).
- **Retención del panel de alertas DLP.** La página general indica 30 días, mientras que la [página del panel](https://learn.microsoft.com/en-us/purview/dlp-alerts-dashboard-get-started) dice que la retención de la auditoría controla cuánto tiempo se ve una alerta. Verifícalo en tu tenant antes de definir procedimientos de conservación.
- **Ubicaciones sin fila propia en la descripción de servicio.** Repositorios locales, Fabric y Power BI y apps no Microsoft conectadas no tienen fila de licencia propia; para repositorios locales se exige licencia a todas las personas que agregan o consumen archivos. Confirma el SKU con tu equipo de licenciamiento.
- **Ninja exclusivo de DLP.** Un [rastreador comunitario](https://github.com/peterschmidtdk/Microsoft-Ninja-Training/blob/main/README.md) (27 de febrero de 2026) lista el enlace corto [aka.ms/DLPNinja](https://aka.ms/DLPNinja), pero la verificación automática solo devolvió un título genérico de Microsoft y la investigación no encontró un Ninja exclusivo de DLP vigente. Esta guía toma como Ninja oficial la ruta de Learn.
- **Práctica de red y costos de laboratorio.** La matriz de laboratorio clasifica la seguridad de datos de red como solo producción. En teoría, una [prueba de Entra Suite](https://learn.microsoft.com/en-us/entra/fundamentals/try-microsoft-entra-suite) (que incluye Internet Access) sumada a la prueba E5 cumpliría los requisitos de la página de red, pero no se verificó. Tampoco está confirmado que el crédito de Visual Studio cubra los medidores de pago por uso de Purview ni las SCU.
- **Residencia de datos de EDM.** La [lista de regiones de EDM](https://learn.microsoft.com/en-us/purview/sit-get-started-exact-data-match-based-sits-overview) incluye Brasil y EE. UU., pero no otras regiones de Latinoamérica; valida el impacto con privacidad antes de cargar tablas reales.
- **Roles de los referentes.** Algunos roles difieren entre los programas de Purview de esta serie (por ejemplo, Albert Hoitingh figura como MVP en unos y como empleado de Microsoft en otros); este programa usa la evidencia más reciente.
- **Ignite 2026.** Microsoft Ignite (17 al 20 de noviembre de 2026) puede cambiar estados de vista previa, fechas y licencias; revalida esta guía después del evento.

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. No constituye asesoría legal ni laboral: las decisiones sobre monitoreo, evidencias, privacidad y normativa corresponden a tus áreas de Legal, RR. HH. y privacidad. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

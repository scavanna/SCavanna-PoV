# Cierre, glosario y fuentes

*Microsoft Purview DSPM y seguridad de datos para IA Ninja Training · Edición 2026*

[← Laboratorio y práctica en producción](07_Laboratorio_y_practica_en_produccion.md) · [Índice del programa](README.md)

<a id="cierre"></a>

## ¿Y ahora?

Ser Ninja de la seguridad de datos para IA no es un estado, es un hábito mensual: revisar objetivos y recomendaciones, cerrar hallazgos con sus responsables, ajustar políticas que nacieron en simulación y explicar la tendencia al comité de IA. Después de Microsoft Ignite (17 al 20 de noviembre de 2026), verifica el estado del Posture Agent, de la política Risky Agents, de la integración con el data lake de Sentinel y de la preparación para Copilot anunciada para enero de 2027.

Próximos pasos: el examen SC-401, las insignias de las rutas de Learn de DSPM y de IA, y los programas de la serie que profundizan lo que aquí se integra: Information Protection, DLP, Insider Risk, Communication Compliance, Data Lifecycle, eDiscovery y Audit, Compliance Manager, Entra (identidad de agentes) y Security Copilot. Si encuentras un enlace roto o un dato desactualizado, anótalo y compártelo con tu equipo: esta guía está pensada para mantenerse viva, como los Ninja originales.

<a id="glosario"></a>

## Glosario

| Término | Definición |
|---|---|
| DSPM | Data Security Posture Management: solución de Purview que muestra dónde están los datos sensibles, quién accede, cómo se usan (incluida la IA) y qué controles faltan. |
| DSPM (classic) y DSPM for AI (classic) | Experiencias anteriores a la DSPM unificada; se retiran a fines de enero de 2027. |
| AI Hub | Nombre original de DSPM for AI; las políticas de esa etapa conservan el prefijo «Microsoft AI Hub». |
| Objetivo de seguridad de datos | Agrupación de hallazgos, métricas y acciones de DSPM en torno a un riesgo, por ejemplo prevenir la sobreexposición o la exfiltración. |
| AI observability | Página de DSPM que inventaría apps y agentes de IA con actividad en los últimos 30 días, con su riesgo e interacciones sensibles. |
| Asset explorer | Vista de DSPM para explorar activos de datos; por ahora, la única ubicación Microsoft es Microsoft 365. |
| Evaluación de riesgo de datos | Análisis de sobreexposición de DSPM: predeterminada (100 sitios más usados, cada semana) o personalizada (Microsoft 365 y Fabric). |
| Sobreexposición (oversharing) | Contenido accesible para más personas de las necesarias, por ejemplo por vínculos amplios o grupos de toda la organización; Copilot puede mostrarlo en sus respuestas. |
| Política de un clic | Política de DLP, Insider Risk, Communication Compliance, etiquetas o colección creada desde un objetivo o recomendación de DSPM. |
| Directiva de colección | Configuración que define qué eventos, clasificaciones y contenido de IA se ingieren en Purview; no tiene licencia propia. |
| Captura de contenido | Opción de una directiva de colección que guarda el texto de prompts y respuestas; exige evaluar el impacto en la privacidad. |
| AI interaction | Evento del explorador de actividad que registra una interacción con una app de IA. |
| Pago por uso (PAYG) | Modelo de facturación de Purview por consumo, cobrado en una suscripción de Azure del mismo inquilino. |
| Microsoft Purview Suite | Nuevo nombre de Microsoft 365 E5 Compliance: complemento de cumplimiento y seguridad de datos sobre E3. |
| Microsoft 365 E7 | Suite que incluye Microsoft 365 E5, Microsoft 365 Copilot, Entra Suite y Agent 365 (99 USD por usuario al mes, precio de lista de EE. UU.). |
| Agent 365 | Plataforma para observar, gobernar y proteger agentes de IA; requisito para la observabilidad y el riesgo interno de agentes en Purview. |
| SAM | SharePoint Advanced Management: funciones de gobierno de SharePoint, varias habilitadas con al menos una licencia de Copilot. |
| RCD | Restricted Content Discovery: oculta un sitio de la búsqueda organizacional y de Copilot sin cambiar permisos; temporal y no aplica a OneDrive. |
| RAC | Restricted Access Control: restringe el acceso a un sitio a un grupo definido, aunque haya permisos más amplios. |
| Informes DAG | Informes de gobierno de acceso a datos de SAM para encontrar sitios con uso compartido amplio. |
| Risky AI usage | Plantilla de Insider Risk Management que detecta uso riesgoso de IA, como inyección de prompts o acceso a material protegido. |
| Risky Agents | Política de Insider Risk Management que evalúa el riesgo de agentes de Copilot Studio, Foundry y del SDK y lo comparte con DSPM. |
| Data Security Posture Agent | Agente de Security Copilot en DSPM que descubre datos sensibles con lenguaje natural, etiqueta y programa ejecuciones. |
| Data Security Triage Agent | Agente de Security Copilot que clasifica alertas de DLP e Insider Risk para reducir el ruido. |
| DSI | Data Security Investigations: investigaciones asistidas por IA sobre datos de Microsoft 365, con facturación por consumo. |
| SCU | Security Compute Unit: unidad de capacidad de Security Copilot; E5 incluye 400 al mes por cada 1.000 licencias pagas, hasta 10.000. |
| Network Data Security | Inspección en línea del tráfico hacia apps de IA mediante Global Secure Access o un SASE/SSE de terceros. |
| IA en la sombra (shadow AI) | Uso de apps de IA no autorizadas por la organización, por ejemplo servicios de consumo en el navegador. |
| AI-SPM | Gestión de la postura de seguridad de la IA en Defender for Cloud (plan Defender CSPM). |
| AI BOM | Lista de materiales de IA: inventario de modelos, servicios y dependencias de una carga de trabajo de IA. |
| Prompt Shields | Detección de ataques en prompts (jailbreak e inyección) que usa Defender for AI Services. |
| XPIA | Inyección indirecta de prompts (cross-prompt injection); Audit marca su detección en las interacciones de Copilot (XPIADetected). |
| protectionScopes y processContent | APIs de Purview en Microsoft Graph para consultar qué políticas aplican y evaluar contenido desde apps propias. |
| Derechos ARCO | Acceso, rectificación, cancelación y oposición: derechos de los titulares de datos personales en varias leyes de la región. |

<a id="metodologia"></a>

## Metodología y fuentes

Esta guía se construyó con líneas de investigación en paralelo sobre fuentes públicas: la forma y la historia del Ninja oficial, cada nivel técnico, la operación y la comunidad. Cada enlace se registró solo si apareció literalmente en un resultado de búsqueda o en una página leída, y luego se consolidó, se depuró y se verificó. Se descartaron recursos retirados, alojados en espacios no públicos o duplicados. Fecha de corte: 6 de noviembre de 2026.

Puntos a confirmar en fuentes oficiales antes de recomendarlos:

- **Estado del Data Security Posture Agent.** MC1318248 anunció la GA entre mediados de junio y fines de julio de 2026, pero la página de Learn actualizada el 23 de junio de 2026 y la vista general de agentes siguen diciendo preview ([MC1318248](https://mc.merill.net/message/MC1318248), [Posture Agent](https://learn.microsoft.com/en-us/purview/copilot-in-purview-posture-agent-get-started)). Esta guía lo trata como preview para compromisos de servicio.
- **Fecha de GA de la nueva DSPM.** MC1191257 y el blog del 21 de mayo de 2026 la sitúan en mayo de 2026; MC1318248, publicado el mismo día, menciona que «DSPM» es GA de junio a julio. Lo más probable es que esa fecha se refiera al agente y no a la experiencia completa ([MC1191257](https://message.cengizyilmaz.net/message/mc1191257-new-microsoft-purview-data-security-posture-management-experience)).
- **Retiro de las experiencias classic.** La versión original de MC1481315 (28 de septiembre de 2026) indicaba de fines de noviembre a fines de diciembre de 2026; la versión del 27 de octubre de 2026 lo movió a fines de enero de 2027 ([MC1481315](https://mc.merill.net/message/MC1481315)). Algunos documentos de terceros pueden seguir citando la fecha anterior.
- **Agentes en tiempo futuro.** La descripción del servicio todavía dice que las capacidades de Purview para agentes de Foundry y apps conectadas a Entra «serán soportadas» por E7 y Agent 365, aunque MC1280556 ya marcó la GA de junio a julio de 2026 ([descripción del servicio](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)).
- **Risky Agents: preview o GA.** MC1280556 anuncia la GA de Insider Risk Management para agentes, mientras la página de la política Risky Agents (actualizada el 4 de agosto de 2026) la sigue marcando como preview ([monitorear agentes](https://learn.microsoft.com/en-us/purview/insider-risk-management-monitoring-agents)).
- **Instrucciones que apuntan a la experiencia classic.** La guía para apps de IA de terceros (actualizada el 1 de mayo de 2026) todavía usa DSPM for AI (classic) como punto de partida, y la lista oficial de políticas de un clic con su modo inicial sigue publicada en la página de consideraciones de la experiencia classic, aunque esa experiencia se retira en enero de 2027 ([otras apps de IA](https://learn.microsoft.com/en-us/purview/ai-other-apps), [consideraciones classic](https://learn.microsoft.com/en-us/purview/dspm-for-ai-considerations)).
- **Unidades de cómputo de DSI.** Una fuente de terceros afirma que unidades de cómputo propias de Data Security Investigations reemplazaron a las SCU, mientras el Posture Agent dentro de DSI consume SCU. Confírmalo en la página de facturación antes de presupuestar ([4sysops](https://4sysops.com/archives/microsoft-purview-data-security-investigations-ai-powered-threat-detection-for-microsoft-365/), [facturación de DSI](https://learn.microsoft.com/en-us/purview/data-security-investigations-billing)).
- **Licencia de Network Data Security.** La descripción del servicio clasifica la DLP de red como pago por uso, y la página de Network Data Security pide Microsoft 365 E7 o Purview E5 + Entra Internet Access para Global Secure Access y Purview E5 + pago por uso para un SASE de terceros. Confirma si tu escenario genera cargos por solicitud ([Network Data Security](https://learn.microsoft.com/en-us/purview/dlp-network-data-security-learn)).
- **Requisitos dispersos de Copilot en Fabric.** La página de consideraciones exige la versión empresarial de Purview data governance y una directiva de colección, y la página de Copilot en Fabric exige pago por uso; el soporte de otras experiencias de Copilot en Fabric y de Fabric Data Agent está en preview ([consideraciones](https://learn.microsoft.com/en-us/purview/data-security-posture-management-considerations), [Copilot en Fabric](https://learn.microsoft.com/es-es/purview/ai-copilot-fabric)).
- **Fechas no verificadas.** No se encontró la fecha de GA de las directivas de colección, del Data Security Triage Agent ni del Security Dashboard for AI; el bloqueo de búsqueda web con SIT en la DLP para Copilot figuraba en preview según el anuncio de Ignite 2025 y no se volvió a verificar.
- **Crédito de Visual Studio.** Ninguna página oficial confirma si el crédito mensual de Azure de Visual Studio cubre los medidores de pago por uso de Purview o las SCU de Security Copilot; trátalo como no garantizado.
- **Límites de la comunidad sin confirmar.** Una guía en español de DSPM para IA menciona límites (200.000 elementos, 30 días) que no se pudieron confirmar en Learn ([guía de JP Márquez](https://jpmarquez.com/es/blog/microsoft-purview-dspm-ia-guia-despliegue-copilot/)).
- **Muestra del Data Security Index 2026.** La encuesta representa a Latinoamérica solo con Brasil; sus porcentajes no son una línea base de MCSA ([informe](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/security/Data-Security-Index-Unifying-Data-Protection.pdf)).
- **Precios y nombres.** Los precios de E7, Agent 365, E5 y Purview Suite son de lista de EE. UU. y varían por país y acuerdo. Learn usa cada vez más «Microsoft Copilot» para Microsoft 365 Copilot, sin cambios de seguridad o cumplimiento, lo que puede confundir al buscar documentación.
- **Microsoft Ignite 2026.** El evento (17 al 20 de noviembre de 2026) ocurre después de la fecha de corte y puede cambiar estados de preview, licencias y fechas de este programa.

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. No constituye asesoría legal ni laboral: las decisiones sobre privacidad, captura de contenido, monitoreo y normativa corresponden a tus áreas de Legal, RR. HH. y privacidad. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

# Cierre, glosario y fuentes

*Microsoft Purview Compliance Manager Ninja Training · Edición 2026*

[← Laboratorio y práctica en producción](07_Laboratorio_y_practica_en_produccion.md) · [Índice del programa](README.md)

<a id="cierre"></a>

## ¿Y ahora?

Ser Ninja de Compliance Manager no es tener la puntuación más alta, sino poder defender cada cifra: de dónde sale, qué evidencia la respalda, quién la probó y qué norma cubre. Tus siguientes pasos: el examen [SC-900](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-900), el [Ninja oficial de 2023](https://techcommunity.microsoft.com/blog/microsoft-security-blog/microsoft-purview-compliance-manager-mspcm-ninja-training-q1-2023/3181322) para repasar conceptos y, si tu organización usa IA, las plantillas de IA junto con el programa de DSPM y seguridad de datos para IA.

Continúa con los programas hermanos según tu rol: Information Protection y DLP (las acciones que más puntos mueven), ciclo de vida de los datos y registros (retención), eDiscovery y Audit (auditoría como evidencia), riesgo interno y cumplimiento de comunicaciones (sectores regulados) y DSPM. Del lado de seguridad, Entra (PIM y roles), Defender XDR (Secure Score y reporte ejecutivo del SOC), Sentinel y Security Copilot. Dedica media hora al mes a [What's new in Microsoft Purview](https://learn.microsoft.com/en-us/purview/whats-new) y revisa los avisos del Message Center antes de cambiar un procedimiento.

Si encuentras un enlace roto, un dato desactualizado o una norma que cambió, anótalo y compártelo con tu equipo: la guía está pensada para revisarse periódicamente, como el Ninja original. Y ante cualquier duda regulatoria, la última palabra la tiene tu área de Legal.

<a id="glosario"></a>

## Glosario

| Término | Definición |
|---|---|
| Acción de mejora | Tarea concreta que implementa un control; tiene responsable, estado de implementación y de prueba, notas y evidencias. |
| Acción técnica y no técnica | Las técnicas se implementan con configuración del inquilino y cuentan una vez por inquilino; las no técnicas (procesos y documentos) cuentan una vez por grupo. |
| AI Baseline | Regulación que, según un análisis comunitario, aparece al activar licencias de Copilot, con 179 acciones (99 de Microsoft); su licenciamiento debe confirmarse en el inquilino. |
| Alerta temprana | Primer reporte de un incidente al CSIRT Nacional de Chile, en un máximo de tres horas según el Decreto 295. |
| Conector de Compliance Manager | Integración propia (Corporate Sustainability, Salesforce y Zoom) para evaluar servicios no Microsoft; distinta de los conectores de datos de Purview. |
| Control | Requisito de una regulación; puede gestionarlo Microsoft, el cliente o ambos (compartido). |
| Cupo premium | Cada una de las tres plantillas premium que Microsoft 365 E5, A5 y G5 pueden usar sin costo; una familia de plantillas cuenta como un cupo. |
| Data Protection Baseline | Plantilla incluida en todas las suscripciones y base de la puntuación inicial. |
| Defender for Cloud | Solución de Microsoft que evalúa la postura de Azure, AWS y GCP y entrega a Compliance Manager los resultados a nivel de recurso. |
| Evaluación (assessment) | Agrupación de los controles de una regulación para uno o varios servicios, con sus acciones y su puntuación. |
| Evaluación base de Microsoft 365 Copilot | Evaluación que se aprovisiona sola al comprar Microsoft 365 Copilot o Copilot Chat. |
| Evaluación personalizada | Copia extendida de una regulación con controles, acciones y servicios propios; está en vista previa. |
| Exportación continua | Función de Defender for Cloud que envía cumplimiento normativo, secure score y recomendaciones a Log Analytics o Event Hubs. |
| Foundational CSPM y Defender CSPM | Niveles de gestión de postura de Defender for Cloud; los estándares no predeterminados requieren un plan pago. |
| Grupo de evaluaciones | Contenedor de evaluaciones que comparten acciones no técnicas; no se puede cambiar una vez asignado. |
| Informe de evaluación | Instantánea en Excel con controles, estados, fechas y resultados de prueba. |
| Informes de postura de Purview | Informes ejecutivos de Information Protection, DLP y personalizados, en vista previa, con una ventana de 30 días. |
| Licencia de regulación | Derecho a usar una plantilla premium durante un año; permite evaluaciones ilimitadas de sus versiones. |
| Microsoft Purview Suite | Nombre, desde el 1 de octubre de 2025, del complemento antes llamado Microsoft 365 E5 Compliance. |
| Pending update | Actualización de plantilla publicada por Microsoft; aceptarla es permanente y se aplica por grupo. |
| Plantilla generada desde PDF | Plantilla creada al subir el PDF oficial de una norma: el sistema extrae controles y los mapea a acciones (GA en octubre de 2026). |
| Plantilla premium de IA | Plantillas de EU AI Act, ISO/IEC 23894, ISO/IEC 42001 y NIST AI RMF para apps y agentes de IA. |
| Plantilla regulatoria (regulación) | Contenido que Microsoft mantiene para una norma o un estándar: controles, acciones y mapeo. |
| Preparación previa al despliegue | Agrupación Sub-service compliance readiness (vista previa) que muestra el aporte de servicios de Azure a varios marcos sin consumir licencias. |
| Prueba de evaluaciones premium | 25 plantillas premium durante 90 días, una sola vez por inquilino. |
| Puntuación de cumplimiento | Medida basada en riesgo del avance en acciones de mejora; no equivale a cumplimiento legal. |
| RACI | Matriz de responsabilidades: responsable, aprueba y rinde cuentas, consultado e informado. |
| Responsabilidad compartida | Reparto de los controles entre Microsoft, el cliente y ambos, según el servicio. |
| RRCI | Lineamientos del BCRA para la respuesta y recuperación ante ciberincidentes, actualizados por la Comunicación «A» 8280. |
| Secure Score | Métrica de postura de seguridad de Microsoft (hasta 10 puntos por acción), distinta de la puntuación de cumplimiento. |
| Service Trust Portal | Portal de Microsoft con informes de auditoría y documentos de cumplimiento de sus servicios. |
| Versión universal | Variante de una plantilla para servicios no Microsoft, con implementación y pruebas manuales. |

<a id="metodologia"></a>

## Metodología y fuentes

Esta guía se construyó con líneas de investigación en paralelo sobre fuentes públicas: la forma y la historia del Ninja oficial, cada nivel técnico, la operación y la comunidad. Cada enlace se registró solo si apareció literalmente en un resultado de búsqueda o en una página leída, y luego se consolidó, se depuró y se verificó. Se descartaron recursos retirados, alojados en espacios no públicos o duplicados. Fecha de corte: 6 de noviembre de 2026.

Puntos a confirmar en fuentes oficiales antes de recomendarlos:

- Licencias: un blog de licenciamiento de 2026 afirma que E5 o E5 Compliance dan acceso a «300+ plantillas premium» ([blog](https://microsoftnegotiations.com/blog/microsoft-compliance-manager-licensing)), mientras Learn indica tres plantillas premium sin costo para A5, E5 y G5 y compra por plantilla para el resto ([lista de regulaciones](https://learn.microsoft.com/en-us/purview/compliance-manager-regulations-list)). Prevalece Learn.
- Purview Suite y E7: Learn habla de «A5/E5/G5» para los cupos premium y la descripción del servicio no menciona el complemento Purview Suite (antes E5 Compliance) ni E7 ([descripción del servicio](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)). Confirma con tu equipo de licencias si heredan las tres plantillas premium gratuitas.
- Plantilla de México: Compliance Manager mantiene la plantilla de la ley de 2010, pero la LFPDPPP fue reemplazada el 20 de marzo de 2025 ([LFPDPPP](https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPDPPP.pdf)) y la lista de regulaciones no se actualiza desde el 6 de marzo de 2025. Verifica también si las plantillas de Perú (nuevo reglamento de 2025) y de la Circular Externa 007 de Colombia (actualizada por la CE 033 de 2020) reflejan la versión vigente.
- Plantillas de IA: Learn indica que consumen licencias premium, pero también que las evaluaciones integradas de IA son gratuitas durante seis meses con licencias de Copilot o de agentes ([evaluaciones](https://learn.microsoft.com/en-us/purview/compliance-manager-assessments)); un análisis comunitario describe además una plantilla «AI Baseline» sin licencia ([AI Baseline](https://informasjonsbeskyttelse.no/en/ai-baseline-in-microsoft-purview)). Confírmalo en tu inquilino.
- Evaluaciones personalizadas: según la investigación, la página de evaluaciones indica que no reciben actualizaciones de plantilla de Microsoft, mientras la página de evaluaciones personalizadas (vista previa, 27 de noviembre de 2024) dice que las copias heredan las actualizaciones salvo en las acciones modificadas y recomienda no editar copias publicadas ([evaluaciones personalizadas](https://learn.microsoft.com/en-us/purview/compliance-manager-assessments-custom)).
- Plantillas generadas con IA: la disponibilidad general se reprogramó de mediados de enero a agosto y luego a octubre de 2026 ([MC1192260](https://mc.merill.net/message/MC1192260)); la integración con Foundry figuraba «In development» el 26 de agosto de 2026, con GA prevista para octubre ([RM536576](https://mc.merill.net/message/RM536576)). Verifica la llegada a tu inquilino.
- Licencia para crear plantillas: la página de creación de plantillas (desde PDF o en blanco) no indica si consumen licencias premium; solo la copia de una plantilla premium lo hace de forma explícita ([crear plantillas](https://learn.microsoft.com/en-us/purview/compliance-manager-create-template)).
- Nombres: la página de evaluaciones todavía usa Azure AI Foundry (hoy Microsoft Foundry) en la sección de evaluaciones automáticas, y el rol de colaboración aparece como «Contribution», «Contributor» o «Contributors» según la página.
- Tamaño y vigencia de las plantillas: Learn habla de «más de 360», un laboratorio comunitario contó 391 y el video de Microsoft Mechanics (aproximadamente de 2022) mencionaba «más de 350»; un análisis comunitario indica que el mapeo de ISO/IEC 27001:2022 no se actualiza desde octubre de 2023 ([análisis](https://informasjonsbeskyttelse.no/en/premium-templates)). Contrasta con tu inquilino.
- Defender for Cloud: la matriz de laboratorio sugiere Foundational CSPM para contener costos, pero los estándares no predeterminados, como ISO 27001, requieren al menos un plan pago ([panel de cumplimiento](https://learn.microsoft.com/en-us/azure/defender-for-cloud/regulatory-compliance-dashboard)); considéralo al presupuestar.
- Configuration Analyzer for Microsoft Purview (antes MCCA), parte del nivel Advanced del Ninja de 2023, no aparece en la investigación de 2026: no lo recomiendes sin verificar su estado.
- APIs: al 6 de noviembre de 2026 la documentación indica que no hay APIs para extraer datos ni analíticas de Purview ([APIs](https://learn.microsoft.com/en-us/purview/developer/use-the-api)); Microsoft Ignite (17 al 20 de noviembre de 2026) podría cambiarlo, igual que otros estados de vista previa (evaluaciones personalizadas, preparación previa al despliegue e informes de postura).
- Chile, Ley 21.719: una firma cita 72 horas para notificar vulneraciones, pero el texto oficial (art. 14 sexies) dice «sin dilaciones indebidas» y no fija horas ([Ley 21.719](https://www.leychile.cl/leychile/Navegar?idNorma=1209272&idParte=1)).
- Plazos sin confirmar en texto oficial: Perú 48 horas (fuentes de firmas), Costa Rica cinco días hábiles (art. 38 del reglamento), aviso inmediato a la CNBV en México, 24 horas al CERTuy en Uruguay, 72 horas en la ley de ciberseguridad de Ecuador, la doble notificación peruana del DS 126-2025-PCM (según un artículo del diario oficial) y Guatemala 3, 6 y 72 horas (ley aprobada, pendiente de publicación).
- Uruguay, Comunicación BCU 2024/018: la investigación le atribuye un reporte inicial en 4 horas para instituciones del sistema de pagos, mientras la ficha normativa la describe como reporte unificado de las entidades supervisadas y otra fuente remite a la Comunicación 2021/105 para las de intermediación financiera; verifica el alcance.
- Panamá: la ficha normativa da 72 horas según el Decreto Ejecutivo 285, pero otra fuente de la investigación atribuye el plazo a análisis de terceros y pide verificar el artículo del decreto.
- Autores y roles: algunos autores se presentan como MVP en sus sitios y figuran como empleados de Microsoft en el directorio de referentes (por ejemplo, Albert Hoitingh); el estado MVP de otros autores comunitarios no se verificó.
- Ninja oficial: varios comentarios reportan knowledge checks inaccesibles en la edición Q1 2023; el certificado de esta guía es una autoevaluación propia.

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. No constituye asesoría legal: la normativa citada es material de referencia y las decisiones de aplicabilidad corresponden a tus áreas de Legal, privacidad y, cuando aplique, RR. HH. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

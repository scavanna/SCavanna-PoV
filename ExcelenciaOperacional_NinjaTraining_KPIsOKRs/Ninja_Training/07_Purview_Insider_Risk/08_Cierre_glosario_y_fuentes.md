# Cierre, glosario y fuentes

*Microsoft Purview Insider Risk Management Ninja Training · Edición 2026*

[← Laboratorio y práctica en producción](07_Laboratorio_y_practica_en_produccion.md) · [Índice del programa](README.md)

<a id="cierre"></a>

## ¿Y ahora?

**Próximos pasos.** Si buscas una credencial formal, prepara SC-401 con su guía de estudio del 28 de octubre de 2026 y completa la ruta oficial de IRM en Microsoft Learn. Haz también los knowledge checks del Ninja oficial de Tech Community: aunque su última actualización conocida es de 2024, sus fundamentos siguen vigentes y otorgan el certificado no oficial «Ninja Cat».

**Sigue con la serie.** Purview DLP, para las políticas que disparan y ejecutan la Protección adaptativa; Communication Compliance, para las señales de conducta; DSPM y seguridad de datos para IA, para la postura de Copilot y de los agentes; eDiscovery y Audit, para la preservación y la cadena de custodia; Defender XDR y Sentinel, para la correlación en el SOC; Entra, para el Acceso condicional y Global Secure Access; y Security Copilot, para las SCU y los agentes.

**Mantente al día.** Revisa cada mes la página de novedades de Purview y el Centro de mensajes y, después de Microsoft Ignite (17 al 20 de noviembre de 2026), confirma los estados que esta edición marca como vista previa o como contradictorios en la lista de puntos a confirmar.

**Y recuerda lo esencial.** Insider Risk Management protege a la organización y a las personas solo si se usa con proporcionalidad: aprobaciones previas, seudonimización, roles separados, auditoría de los investigadores y decisiones finales en manos de RR. HH. y Legal, con evidencia completa.

<a id="glosario"></a>

## Glosario

| Término | Definición |
|---|---|
| Riesgo interno (insider risk) | Riesgo de que personas con acceso legítimo —empleados, contratistas o agentes— causen, por error o con intención, fugas, robos o violaciones de seguridad. |
| Insider Risk Management (IRM) | Solución de Microsoft Purview que correlaciona señales para detectar, investigar y responder al riesgo interno; en Learn en español aparece como «Administración de riesgos internos». |
| Política (directiva) | Configuración basada en una plantilla que define a quién se evalúa, con qué disparadores e indicadores y con qué umbrales; la documentación en español usa «directiva». |
| Seudonimización | Reemplazo de los nombres de usuario por alias dentro de IRM, activo por defecto; no se conserva en Acceso condicional, alertas DLP, el explorador de actividad, la exportación por API ni el panel del Triage Agent. |
| Evento desencadenante | Señal que pone a un usuario en el alcance de una política, como una renuncia informada por el conector de RR. HH. o una alerta DLP de severidad alta. |
| Indicador global e indicador de política | El global define qué actividad recolecta IRM en el tenant (todos vienen desactivados); el de política define qué actividad puntúa en una política concreta. |
| Variante de indicador | Versión ajustada de un indicador, por ejemplo con un dominio excluido; hasta 10 por indicador y 100 en total. |
| Booster de riesgo | Factor que eleva la puntuación: actividad inusual, caso previo confirmado, pertenencia a un grupo prioritario o usuario de alto impacto. |
| Exfiltración acumulativa | Detección que compara los últimos 30 días del usuario con la organización y con su grupo de pares. |
| Grupo de usuarios prioritarios | Usuarios de mayor impacto cuyas alertas reciben más severidad; obligatorio en las plantillas «by priority users» y no combinable con unidades administrativas. |
| Exclusiones globales | Usuarios, dominios, rutas o actividades que IRM no evalúa; hoy se configuran en «Global exclusions (preview)». |
| Analíticas | Escaneo diario de hasta 10 días de actividad con resultados agregados y anonimizados para estimar el riesgo antes de crear políticas. |
| Cola unificada de alertas | Experiencia que reúne las alertas clásicas y las del Triage Agent, con la vista «Needs attention»; disponibilidad general en octubre de 2026. |
| Caso | Expediente centrado en un usuario que reúne alertas, actividad, contenido, notas, avisos y acciones de escalamiento. |
| Plantilla de aviso | Correo que se envía al usuario de un caso para recordarle políticas o capacitación y que deja rastro auditable. |
| Evidencia forense | Complemento opcional que graba clips de video de actividad riesgosa en dispositivos Windows; requiere la aprobación de IRM Approvers y borra los clips a los 120 días. |
| Protección adaptativa | Capacidad que aplica controles de DLP, Acceso condicional y Data Lifecycle Management según el nivel de riesgo interno. |
| Nivel de riesgo interno | Elevated, Moderate o Minor: clasificación dinámica del usuario o del agente para la Protección adaptativa, distinta de la severidad de la alerta. |
| Conector de RR. HH. | Importación por CSV de renuncias, cambios de nivel, evaluaciones, planes de mejora y perfiles de empleado. |
| Conector Insider Risk Indicators | Conector en vista previa que importa detecciones de terceros ya agregadas para usarlas como disparadores o indicadores personalizados. |
| Pago por uso (PAYG) | Facturación por consumo en una suscripción de Azure del mismo tenant para indicadores de nube, red, Fabric e IA de terceros, OCR y Data Security Investigations. |
| SCU | Unidad de cómputo de seguridad de Security Copilot; el Triage Agent la consume según el número y el tipo de alertas. |
| Triage Agent | Agente de Security Copilot (Microsoft Purview Triage Agent) que clasifica las alertas en Needs attention, Less urgent y Not categorized. |
| Risky AI usage | Plantilla que detecta prompts y respuestas riesgosos o con datos sensibles y visitas a sitios de IA generativa. |
| Risky Agents | Política para agentes de Copilot Studio, Microsoft Foundry y el SDK P4AI; en vista previa según Learn y sujeta a E7 o Agent 365 según MC1280556. |
| DataSecurityEvents y DataSecurityBehaviors | Tablas de la búsqueda avanzada de Defender XDR con eventos enriquecidos y comportamientos diarios generados por IRM (vista previa). |
| Data Security Investigations (DSI) | Solución de pago por uso para analizar contenido a escala con IA; puede iniciarse desde un caso de IRM. |
| Eficacia de alertas | Alertas confirmadas sobre confirmadas más descartadas en los últimos 365 días, por política. |
| Microsoft Purview Suite | Nombre de Microsoft 365 E5 Compliance desde el 1 de octubre de 2025; incluye IRM y se agrega a Microsoft 365 E3. |
| Microsoft 365 E7 y Agent 365 | E7 suma Microsoft 365 E5, Microsoft 365 Copilot, Entra Suite y Agent 365; Agent 365 también se vende aparte. Según MC1280556, son el requisito de IRM para agentes. |

<a id="metodologia"></a>

## Metodología y fuentes

Esta guía se construyó con líneas de investigación en paralelo sobre fuentes públicas: la forma y la historia del Ninja oficial, cada nivel técnico, la operación y la comunidad. Cada enlace se registró solo si apareció literalmente en un resultado de búsqueda o en una página leída, y luego se consolidó, se depuró y se verificó. Se descartaron recursos retirados, alojados en espacios no públicos o duplicados. Fecha de corte: 6 de noviembre de 2026.

Puntos a confirmar en fuentes oficiales antes de recomendarlos:

- **Conector de RR. HH. en las plantillas de salida.** La página de plantillas permite usar el borrado de la cuenta en Entra en lugar del conector en Data theft by departing users, pero «Get started» lo lista como requerido para esa plantilla y para Security policy violations by departing users ([plantillas](https://learn.microsoft.com/en-us/purview/insider-risk-management-policy-templates) frente a [Get started](https://learn.microsoft.com/en-us/purview/insider-risk-management-configure)).
- **Estado de Risky Agents.** MC1200579 reprogramó la disponibilidad general para mediados de junio a fines de julio de 2026 y MC1280556 la anuncia con E7 o Agent 365 como requisito, pero las páginas de Learn de plantillas, indicadores y monitoreo de agentes (4 de agosto de 2026) siguen diciendo «preview» ([MC1200579](https://mc.merill.net/message/MC1200579); [MC1280556](https://message.cengizyilmaz.net/message/mc1280556-microsoft-purview-for-agents-ai-observability-and-insider-risk-management-now-generally-available); [monitoreo de agentes](https://learn.microsoft.com/en-us/purview/insider-risk-management-monitoring-agents)).
- **Licencias para agentes en futuro.** La descripción del servicio de Purview todavía dice que las capacidades para agentes de Microsoft Foundry y apps conectadas a Entra «se soportarán» con E7 y Agent 365, aunque MC1280556 ya marca la disponibilidad general ([descripción del servicio](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)).
- **Fechas internas de MC1430536.** El aviso dice que ambas experiencias de alertas convivirían «al menos 60 días» con soporte «hasta el 31 de agosto de 2026», fecha anterior a la disponibilidad general de octubre y a la depreciación del 1 de octubre; además, What's new solo registra la vista previa de julio ([MC1430536](https://mc.merill.net/message/MC1430536); [What's new](https://learn.microsoft.com/en-us/purview/whats-new)).
- **Etiqueta de Risky AI usage.** La plantilla no lleva etiqueta de vista previa, pero los indicadores de Risky AI usage sí ([plantillas](https://learn.microsoft.com/en-us/purview/insider-risk-management-policy-templates) frente a [indicadores](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-policy-indicators)).
- **Nubes de gobierno de EE. UU.** La página de Protección adaptativa dice que IRM no está disponible en esas nubes, mientras que MC1430536 fija fechas para ellas y el conector de RR. HH. existe en GCC; el impacto es bajo para MCSA ([Protección adaptativa](https://learn.microsoft.com/en-us/purview/insider-risk-management-adaptive-protection); [conector de RR. HH.](https://learn.microsoft.com/en-us/purview/import-hr-data)).
- **Integración con Defender XDR.** El documento base (17 de febrero de 2025) sigue en *prerelease*, pero MC1438568 ya agrega los resúmenes del Triage Agent en Defender, con disponibilidad general prevista para diciembre de 2026; el estado de disponibilidad general de la integración base no está confirmado ([IRM en Defender XDR](https://learn.microsoft.com/en-us/defender-xdr/irm-investigate-alerts-defender); [MC1438568](https://mc.merill.net/message/MC1438568)).
- **Retención de clips forenses.** La página dice que los clips se borran a los 120 días «o al final del período de vista previa», texto que parece heredado; confirma el estado comercial y la capacidad adicional de 100 GB con tu revendedor ([evidencia forense](https://learn.microsoft.com/en-us/purview/insider-risk-management-forensic-evidence); [CDW](https://www.cdw.com/product/microsoft-365-insider-risk-management-forensic-evidence-subscription-lice/7387563)).
- **Licencia del Triage Agent.** Learn exige el modelo de pago por uso además de las SCU, mientras que la inclusión de Security Copilot en E5 y E7 aporta SCU; valida en tu tenant si hace falta vincular una suscripción de Azure. Además, algunas páginas de agentes de Purview todavía lo titulan «(preview)» pese a la disponibilidad general anunciada en MC1180884 ([Triage Agent](https://learn.microsoft.com/en-us/purview/copilot-in-purview-triage-irm-agent-get-started); [inclusión de Security Copilot](https://learn.microsoft.com/en-us/copilot/security/security-copilot-inclusion); [agentes en Purview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-agents)).
- **Product Terms y SKU de componente.** Tras el cambio de nombre de octubre de 2025, los Product Terms siguen mostrando nombres anteriores como prerrequisitos y los SKU de componente de IRM no cambiaron de nombre; confirma el SKU exacto con tu revendedor ([SAMexpert](https://samexpert.com/microsoft-365-defender-purview-renames/)).
- **Plantilla rápida para apps que no son de Microsoft 365.** Sus prerrequisitos (indicadores de nube conectados en Microsoft Defender y una señal de salida) y si consume pago por uso se infieren de la documentación de indicadores; no se confirmaron en una página propia ([What's new](https://learn.microsoft.com/en-us/purview/whats-new); [indicadores](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-policy-indicators)).
- **Indicadores de red y métrica de facturación.** Las fuentes confirman que los indicadores de red de terceros son de pago por uso, pero no su estado. La matriz de laboratorio de la serie indica que los indicadores de nube de terceros y Fabric se facturan por unidades de procesamiento (una por cada 10.000 actividades): confirma la métrica y el precio vigentes en los [modelos de facturación](https://learn.microsoft.com/en-us/purview/purview-billing-models) antes de presupuestar.
- **Crédito de Visual Studio.** No hay confirmación oficial de que el crédito de Azure de Visual Studio Enterprise cubra los medidores de pago por uso de Purview ni las SCU de Security Copilot; trátalo como un gasto no garantizado.
- **Ninja oficial.** La descarga directa del post de Tech Community falló en la verificación y la nota mínima del 80 % típica de la familia no se pudo confirmar para el Ninja de IRM; su estructura se reconstruyó con la [copia sindicada de abril de 2022](https://thewindowsupdate.com/2022/04/19/become-a-insider-risk-management-ninja/) y las publicaciones de 2023 y 2024.
- **Referentes en otros programas.** El programa de DSPM lista a Talhah Mir como empleado de Microsoft, pero según esta investigación dejó la empresa en agosto de 2026; en este programa figura como ex empleado.
- **Traducciones.** Las páginas de Learn en español son traducciones automáticas y pueden ir atrasadas respecto de la versión en inglés; ante cualquier diferencia, prevalece la versión en inglés.
- **Microsoft Ignite 2026.** Ignite (17 al 20 de noviembre de 2026) puede cambiar estados de vista previa y nombres después de la fecha de corte de esta edición.

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. No constituye asesoría legal ni laboral: usar Insider Risk Management sobre personas reales exige la evaluación previa de tus áreas de Legal, RR. HH. y privacidad y, cuando corresponda, de la representación de los trabajadores. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

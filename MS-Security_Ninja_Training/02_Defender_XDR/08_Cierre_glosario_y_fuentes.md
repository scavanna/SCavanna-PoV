# Cierre, glosario y fuentes

*Microsoft Defender XDR Ninja Training · Edición 2026*

[← Laboratorio y práctica en producción](07_Laboratorio_y_practica_en_produccion.md) · [Índice del programa](README.md)

<a id="cierre"></a>

## ¿Y ahora?

Ser Ninja no es un estado, es un hábito. Defender XDR publica novedades cada semana: dedica media hora a la rutina de [C3](05_Comunidad.md#c3), vuelve a esta guía cuando un cambio afecte a tu operación y agenda el knowledge check del Ninja oficial y el examen SC-200 cuando termines el nivel intermedio.

Sigue con la serie: el programa de **Sentinel** para el SIEM, los datos y la automatización avanzada; el de **Entra** para identidad, acceso condicional e identidades de agentes; el de **Security Copilot** para el SOC agéntico; y los de **Purview** para las señales de datos que también llegan al portal de Defender. Si encuentras un enlace roto o un dato desactualizado, regístralo y compártelo: la guía está pensada para revisarse después de cada Ignite, como el Ninja oficial.

<a id="glosario"></a>

## Glosario

| Término | Definición |
|---|---|
| Action center | Lugar del portal de Defender donde se aprueban, rechazan, auditan y deshacen las acciones de respuesta manuales y automáticas. |
| AiTM | Adversary-in-the-middle: phishing con proxy inverso que roba la cookie de sesión y elude la MFA tradicional. |
| AIR | Investigación y respuesta automatizadas: completa en Defender for Office 365 y, desde el 1 de septiembre de 2026, integrada a la pila antivirus en Defender for Endpoint. |
| Alert tuning | Reglas que ocultan, resuelven o convierten alertas en comportamientos para reducir ruido (antes alert suppression). |
| ASR | Reglas de reducción de superficie de ataque de Defender for Endpoint que bloquean comportamientos usados por el malware. |
| Attack disruption | Interrupción automática de ataques: contención de usuarios, dispositivos e IP con confianza de 99 % o más a partir de señales correlacionadas. |
| BEC | Business email compromise: fraude que usa un buzón comprometido o suplantado para desviar pagos o datos. |
| Custom detection | Detección personalizada: consulta de búsqueda avanzada programada que genera alertas y acciones de respuesta; experiencia unificada para reglas nuevas. |
| DVM | Defender Vulnerability Management: inventario, evaluación y priorización de vulnerabilidades; el núcleo viene con MDE P2 y lo premium es un complemento. |
| Enhanced Alert Trigger | Disparador de reglas de automatización que actúa sobre alertas de Defender XDR en el portal de Defender. |
| Exposure Management | Microsoft Security Exposure Management: activos críticos, rutas de ataque, iniciativas con objetivo y Secure Score. |
| GDAP | Granular Delegated Admin Privileges: delegación granular de administración entre inquilinos, usada por partners. |
| Honeytoken | Cuenta señuelo etiquetada en Defender for Identity cuyo uso genera una alerta de alta fidelidad. |
| Incident case | Experiencia de gestión de casos del portal de Defender con tareas, SLA, plantillas, sesiones agénticas y auditoría. |
| ISOC | Integrated Security Operations Center: capacidades SIEM nativas en Defender, en vista previa, para clientes sin workspace activo de Sentinel. |
| ISPM | Gestión de la postura de seguridad de identidad: evaluaciones de Defender for Identity publicadas en Secure Score. |
| KQL | Kusto Query Language: lenguaje de la búsqueda avanzada, de Sentinel y de las detecciones personalizadas. |
| MDR | Managed detection and response: servicio gestionado de detección y respuesta, como Defender Experts MDR. |
| MTO | Gestión multi-inquilino del portal de Defender, para hasta 100 inquilinos. |
| MTTA / MTTR / MTTC | Tiempo medio para reconocer, para remediar y para contener un incidente; publica siempre la definición que usas. |
| NRT | Near real time: frecuencia Continuous de las detecciones personalizadas, limitada a una tabla y sin joins. |
| Predictive shielding | Capacidad de la interrupción automática que restringe de forma proactiva identidades privilegiadas expuestas. |
| SAF | Security Adoption Framework: marco de Microsoft con disciplinas, talleres y guías públicas para modernizar la seguridad, incluida la operación del SOC. |
| SCU | Security Compute Unit: unidad de capacidad de Security Copilot; Microsoft 365 E5 incluye 400 por cada 1.000 licencias pagas, hasta 10.000 al mes. |
| Security Alert Triage Agent | Agente de Security Copilot que clasifica alertas con razonamiento transparente; se llamaba Phishing Triage Agent (antes de ampliarse a identidad y nube). |
| Sensor v3.x | Sensor unificado de Defender for Identity que se activa desde el portal, usa LocalSystem y se actualiza por Windows Update. |
| SOC-CMM | Modelo independiente de madurez y capacidad del SOC con 5 dominios, 27 aspectos y niveles de madurez de 0 a 5. |
| URBAC | RBAC unificado del portal de Defender para MDE, MDI, MDO, gestión de vulnerabilidades, Exposure Management y Sentinel. |
| ZAP | Zero-hour auto purge: purga automática de mensajes ya entregados que luego se identifican como maliciosos. |

<a id="metodologia"></a>

## Metodología y fuentes

Esta guía se construyó con líneas de investigación en paralelo sobre fuentes públicas: la forma y la historia del Ninja oficial, cada nivel técnico, la operación y la comunidad. Cada enlace se registró solo si apareció literalmente en un resultado de búsqueda o en una página leída, y luego se consolidó, se depuró y se verificó. Se descartaron recursos retirados, alojados en espacios no públicos o duplicados. Fecha de corte: 6 de noviembre de 2026.

Puntos a confirmar en fuentes oficiales antes de recomendarlos:

- **Ninja oficial de Defender XDR:** la estructura de niveles y módulos solo pudo verificarse en una copia indexada con banner de julio de 2024, mientras la [etiqueta de Tech Community](https://techcommunity.microsoft.com/tag/ninja%20training) muestra actividad del 19 de octubre de 2026; el crosswalk puede no reflejar cambios recientes, y el umbral y el formato del certificado del knowledge check no se confirmaron.
- **Fechas de la familia Ninja:** el [Ninja de MDE](https://techcommunity.microsoft.com/blog/microsoftdefenderatpblog/become-a-microsoft-defender-for-endpoint-ninja/1515647) muestra 28 de septiembre de 2026 en la etiqueta, «Updated Aug 05, 2026, Version 45.0» en el pie y un aviso de actualización en curso; el de MDO conserva «June 2022» en el título pese a la actividad de marzo de 2026; el de MDI (enero de 2024) no confirma el umbral del 80 % ([MS Cloud Explorers](https://mscloudexplorers.com/learn/)).
- **Escritorios Linux en MDE:** Learn los lista en vista previa en septiembre de 2026 ([novedades de MDE](https://learn.microsoft.com/en-us/defender-endpoint/whats-new-in-microsoft-defender-endpoint)) y un medio externo habla de un anuncio del 14 de octubre ([tech-insider](https://tech-insider.org/defender-for-endpoint-setup-2026/)).
- **Exposure Management:** la [página de licencias](https://learn.microsoft.com/en-us/security-exposure-management/integration-licensing) (marzo de 2025) todavía dice «Microsoft 365 E5 Security add-on», hoy Microsoft Defender Suite.
- **Dynamic Threat Detection Agent:** Learn lo describe como vista previa gratuita que consumirá SCU en GA ([DTDA](https://learn.microsoft.com/en-us/defender-xdr/dynamic-threat-detection-agent)); un blog comunitario afirma su inclusión en E5 desde julio y un foro habla de GA a fines de 2026, sin confirmación oficial ([Security Point Break](https://securitypointbreak.com/2026/05/21/microsoft-defender-dynamic-threat-detection-agent-production-metrics/)).
- **Security Alert Triage Agent:** su página conserva «(Preview)» en el título aunque el correo está en GA ([agente](https://learn.microsoft.com/en-us/defender-xdr/security-alert-triage-agent)); el cambio de nombre y la GA se anunciaron en Ignite 2025 ([anuncio](https://techcommunity.microsoft.com/blog/MicrosoftDefenderforOffice365Blog/microsoft-ignite-2025-transforming-phishing-response-with-agentic-innovation/4470791)) y reaparecen en las noticias mensuales de enero de 2026.
- **Defender Experts:** las páginas comerciales y algunas noticias mensuales usan «Defender Experts for XDR» ([página de producto](https://www.microsoft.com/en-us/security/business/services/microsoft-defender-experts-mdr)), mientras Learn usa «Defender Experts MDR» Plan 1 y Plan 2 ([Learn](https://learn.microsoft.com/en-us/defender-xdr/defender-experts/defender-experts-overview)).
- **Examen SC-200:** la [página oficial](https://learn.microsoft.com/en-us/credentials/certifications/security-operations-analyst/) indica 100 minutos; algunas guías de terceros dicen 120 ([ejemplo](https://mscertquiz.com/blog/sc-200-study-guide)).
- **AADSignInEventsBeta:** copias traducidas antiguas indicaban el reemplazo el 9 de diciembre de 2025; la versión en inglés vigente dice 19 de octubre de 2026 ([EntraIdSignInEvents](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-entraidsigninevents-table)).
- **Sensor v3.x de MDI:** la [página de despliegue](https://learn.microsoft.com/en-us/defender-for-identity/deploy/deploy-sensor-v3) marca en vista previa la activación manual en servidores AD FS, AD CS y Entra Connect que no son DC, mientras las [novedades de octubre de 2026](https://learn.microsoft.com/en-us/defender-for-identity/whats-new) anuncian GA de la activación sin MDE para esos roles; además, copias traducidas citan otra actualización acumulativa requerida (marzo o julio de 2026) frente a la de septiembre de 2026 en inglés.
- **Señales de riesgo unificadas de ID Protection:** la [página oficial](https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-unified-risk) no las marca como vista previa, pero un [blog de MVP](https://blog.sonnes.cloud/entra-id-protection-user-risk-with-unified-identity-signals-from-defender-is-here/) (6 de agosto de 2026) las describe así.
- **Directiva administrada MC1476122:** el [archivo del Message Center](https://mc.merill.net/message/MC1476122) solo la registró en inquilinos educativos; no asumas que todos los inquilinos comerciales la recibieron.
- **NRT con datos de Sentinel:** las [novedades de Defender XDR](https://learn.microsoft.com/en-us/defender-xdr/whats-new) lo anuncian en vista previa (enero de 2026) y la página de reglas lista tablas de Sentinel compatibles, pero la [búsqueda con datos de Sentinel](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-microsoft-defender) (23 de septiembre de 2026) dice que no está disponible.
- **AIR de Defender for Endpoint:** desde el 1 de septiembre de 2026 no corre como experiencia separada ni se dispara manualmente ([niveles de automatización](https://learn.microsoft.com/en-us/defender-endpoint/automation-levels)), pero la [página de detecciones personalizadas](https://learn.microsoft.com/en-us/defender-xdr/custom-detection-rules) aún ofrece «Initiate investigation», el ajuste de alertas menciona investigaciones de AIR y la guía de piloto muestra AIR en la simulación.
- **Frecuencia personalizada de detecciones:** según un rastreador comunitario de cambios, el 4 de octubre de 2026 la documentación publicó y luego revirtió su extensión a todas las fuentes; la [página de reglas](https://learn.microsoft.com/en-us/defender-xdr/custom-detection-rules) vigente la limita a reglas con datos solo de Sentinel.
- **Retiro de Sentinel del portal de Azure:** blogs de 2025 y variantes regionales de Learn mencionan el 1 de julio de 2026 ([ejemplo](https://learn.microsoft.com/en-my/azure/sentinel/ci-cd)); la fecha vigente es el 31 de marzo de 2027 ([anuncio](https://techcommunity.microsoft.com/blog/microsoftsentinelblog/update-new-timeline-for-transitioning-sentinel-experience-to-defender-portal/4490464)).
- **Páginas con nombres antiguos:** «Train your security staff» todavía cita el nombre anterior de Security Copilot y la versión en-ie de la guía de piloto envía a tutoriales de Defender Threat Intelligence, retirado el 1 de agosto de 2026; el [índice de playbooks](https://learn.microsoft.com/en-us/security/operations/incident-response-playbooks) (2024) no refleja que phishing, password spray y consentimiento de apps pasaron a la disciplina SecOps del SAF.
- **Detecciones como código:** la fecha de inicio de la vista previa en Sentinel Repositories (junio de 2026) proviene de la comunidad, y las reglas gestionadas como código no reciben las migraciones automáticas de nombres de tablas ([análisis comunitario](https://techcommunity.microsoft.com/discussions/microsoft-security/custom-detection-rules-as-code-in-sentinel-repositories-what-your-pipeline-owns-/4536196)).
- **SAF:** el [catálogo de talleres](https://learn.microsoft.com/en-us/security/zero-trust/workshop-business-overview) indica dos a tres días para el ADS de Modern Security Operations y la [página de la disciplina](https://learn.microsoft.com/en-us/security/zero-trust/security-adoption-discipline-security-operations), dos días. El track de excelencia usa solo las páginas públicas del SAF en Learn.
- **MTTR:** SAF lo mide desde el reconocimiento hasta la corrección y el [workbook de Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/manage-soc-with-incident-metrics) desde la creación hasta el cierre; las fórmulas de [Métricas del SOC](00_Programa.md#metricas-soc) y los estados del [Marco de excelencia del SOC](00_Programa.md#excelencia-soc) son una propuesta de este programa construida sobre fuentes oficiales y marcos públicos.
- **Cifras de contexto:** la traducción al español del [brief del CDOC](https://learn.microsoft.com/es-es/security/engineering/FY18-Strategy-Brief) dice «más de 100 millones» donde el [original](https://learn.microsoft.com/en-us/security/engineering/fy18-strategy-brief) dice más de 1.000 millones de USD; las señales diarias de inteligencia de Microsoft figuran como 78 billones ([MCRA, abril de 2025](https://learn.microsoft.com/es-es/security/adoption/mcra)), más de 100 billones ([MCRA, junio de 2026](https://learn.microsoft.com/en-us/security/zero-trust/microsoft-reference-architecture)) y más de 165 billones ([MDDR 2026](https://www.microsoft.com/en-us/corporate-responsibility/topics/cybersecurity/reports/microsoft-digital-defense-report/)): cita siempre con fecha.
- **GDAP y RBAC unificado:** en el programa de Sentinel se documentaron contradicciones sobre el soporte de GDAP en el RBAC unificado; en esta investigación, la [gestión multi-inquilino](https://learn.microsoft.com/en-us/defender-xdr/mto-requirements) indica GDAP o B2B para datos de Defender y solo B2B para Sentinel, y la [activación de URBAC](https://learn.microsoft.com/en-us/defender-xdr/activate-defender-rbac) excluye GDAP para Sentinel. Valídalo antes de diseñar el acceso de un MSSP.
- **Security Copilot en E5:** la inclusión cuenta solo licencias pagas y no está garantizada en inquilinos de prueba; los precios de SCU que cita la comunidad (4 USD aprovisionada y 6 USD de excedente) deben contrastarse con la página oficial ([notas operativas de la comunidad](https://techcommunity.microsoft.com/discussions/microsoftthreatprotection/operational-notes-on-microsoft-security-copilot-agents-in-defender-xdr-and-micro/4525826)).
- **Referentes:** los roles cambian; por ejemplo, la anfitriona histórica del [podcast de Microsoft Threat Intelligence](https://www.listennotes.com/podcasts/microsoft-threat-intelligence-podcast-bPK4qAi_025/) dejó Microsoft en julio de 2026 y el registro de referentes se corrigió. Verifica antes de citar a alguien como voz oficial.

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

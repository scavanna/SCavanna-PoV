# Track · Operación y excelencia · Operar la seguridad en la nube con excelencia

*Microsoft Defender for Cloud Ninja Training · Edición 2026*

[← Track · Especialización por workload](03b_Track_Especializacion_por_workload.md) · [Índice del programa](README.md) · [Comunidad →](05_Comunidad.md)

<a id="operacion"></a>

La capa de excelencia que aplica los tres niveles al día a día: modelo operativo y RACI, KPI e informes ejecutivos, cumplimiento regulatorio con evidencia y mejora continua con gestión de cambios. Terminas con un proyecto integrador de punta a punta defendido ante un comité, con tablero de KPI y reporte de costos.

*L300–L400 · 4 módulos · ~20 horas · 36 recursos*

**Módulos de este nivel:** [O1 Modelo operativo y RACI](#o1) · [O2 KPI e informes ejecutivos](#o2) · [O3 Cumplimiento y evidencia](#o3) · [O4 Mejora continua e integrador](#o4)

<a id="o1"></a>

## O1 · Modelo operativo: roles, RACI y centro de excelencia de seguridad en la nube

*L300–L400 · ~5 h · Origen: Nuevo en esta edición (base: metodología Secure del Cloud Adoption Framework, versión pública del Security Adoption Framework y guía de planeación de Defender for Cloud)*

Defender for Cloud cruza a plataforma, seguridad, SOC, DevOps, FinOps y dueños de cargas: si nadie es dueño de una recomendación, la recomendación envejece. La metodología Secure del **Cloud Adoption Framework** describe roles de arquitectura, ingeniería, operaciones, postura y DevSecOps, y pide documentar un modelo de responsabilidad compartida que funcione como matriz RACI. El **Security Adoption Framework**, en su versión pública de Learn, organiza disciplinas de planificación y supervisión, estrategia técnica y operación con resultados medibles compartidos. La base técnica para que el RACI sea ejecutable son los roles de Azure (Security Reader, Security Admin, Contributor y Owner), el RBAC unificado del portal de Defender y las reglas de gobernanza.

Un **centro de excelencia** (CCoE) de seguridad en la nube convierte el modelo en rutina: decide estándares y exenciones, aprueba la habilitación de planes y la migración al modelo DWU, revisa la postura cada semana y la presenta cada trimestre. Dos detalles técnicos condicionan el diseño: los permisos de Azure **no fluyen** al RBAC unificado del portal de Defender y los cloud scopes (preview) no agregan solos los entornos nuevos. Las reglas de gobernanza, que requieren Defender CSPM, toman el dueño de una etiqueta, fijan plazos y envían correos semanales al dueño y a su jefe. El modelo operativo del SOC se profundiza en el programa de Defender XDR (S1).

**Por qué importa**

La mayoría de los fracasos de una CNAPP no son técnicos: son recomendaciones sin dueño, exenciones sin vencimiento y equipos que se culpan entre sí. Un RACI explícito, roles de mínimo privilegio y un centro de excelencia con cadencia fija reducen la antigüedad del backlog, aceleran las decisiones de riesgo y hacen auditable quién aceptó qué y hasta cuándo.

**Qué vas a lograr**

- Diseñar el RACI de seguridad en la nube para plataforma, seguridad, SOC, DevOps, FinOps y dueños de recursos.
- Traducir el RACI a roles de Azure, RBAC unificado del portal de Defender y reglas de gobernanza.
- Definir la carta, la cadencia y los derechos de decisión de un centro de excelencia.
- Gobernar exenciones y aceptación de riesgos con vencimiento y responsable.

> **Atención.** No existe un RACI oficial de Microsoft para Defender for Cloud: la tabla de este módulo es una propuesta del programa basada en la metodología Secure del CAF, que pide documentar un modelo de responsabilidad compartida que funcione como RACI, y en la matriz de permisos de Defender for Cloud. Adáptala a tu organización ([roles y equipos del CAF](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/secure/teams-roles), [permisos](https://learn.microsoft.com/en-us/azure/defender-for-cloud/permissions)).

> **Consejo Ninja.** Los permisos de Azure no fluyen al RBAC unificado del portal de Defender: un Owner de la suscripción no ve automáticamente allí los datos de nube. Los cloud scopes (preview) agrupan suscripciones, cuentas de AWS, proyectos de GCP, organizaciones de DevOps y registros, pero los entornos nuevos no se agregan solos: inclúyelo en tu proceso de alta ([cloud scopes y RBAC unificado](https://learn.microsoft.com/en-us/azure/defender-for-cloud/cloud-scopes-unified-rbac)).

> **Novedad.** Las reglas de gobernanza (Defender CSPM) toman el dueño de una etiqueta, fijan plazos de 7, 14, 30 o 90 días con período de gracia, envían correos semanales al dueño y a su jefe, tienen prioridad de 1 a 1.000 y se pueden aplicar a un grupo de administración; las exclusiones solo se configuran por API. A noviembre de 2026 siguen siendo exclusivas del portal de Azure ([reglas de gobernanza](https://learn.microsoft.com/en-us/azure/defender-for-cloud/governance-rules), [comparación de portales](https://learn.microsoft.com/en-us/azure/defender-for-cloud/azure-portal-vs-defender-portal-comparison)).

> **Consejo Ninja.** Usa la versión pública del Security Adoption Framework en Learn —escenarios, disciplinas y resultados compartidos— y los recursos públicos asociados, como el CISO Workshop y la MCRA. El webinar «Go Beyond Checkboxes» muestra cómo pasar de casillas de cumplimiento a una postura proactiva con Defender CSPM ([Security Adoption Framework](https://learn.microsoft.com/en-us/security/zero-trust/security-adoption-model), [webinar](https://www.youtube.com/watch?v=SZx4ztnt8RE)).

**¿Tienes poco tiempo?**

- [Security teams, roles, and functions (Cloud Adoption Framework – Secure)](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/secure/teams-roles) · Documentación
- [Microsoft Security Adoption Framework (SAF)](https://learn.microsoft.com/en-us/security/zero-trust/security-adoption-model) · Documentación
- [Drive recommendation remediation by using governance rules](https://learn.microsoft.com/en-us/azure/defender-for-cloud/governance-rules) · Documentación
- [Go Beyond Checkboxes: Proactive Cloud Security with Microsoft Defender CSPM (webinar)](https://www.youtube.com/watch?v=SZx4ztnt8RE) · Webinar

**RACI de seguridad en la nube**

| Actividad | Plataforma | Seguridad y arquitectura | SOC | DevOps | FinOps | Dueño del recurso | Referencia |
|---|---|---|---|---|---|---|---|
| Definir la línea base, los estándares y las directivas de postura | C | A/R | I | C | I | I | [Learn](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/secure/teams-roles) |
| Habilitar planes y definir su alcance (por plan o DWU) | R | A | I | I | C | I | [Learn](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-portal/plan-management-changes-defender-portal) |
| Decidir la migración de la gestión de planes al portal de Defender (DWU) | C | A | I | I | R | I | [Learn](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-portal/estimate-track-costs) |
| Estimar el costo, presupuestar y decidir el prepago | C | C | I | I | A/R | I | [Learn](https://learn.microsoft.com/en-us/azure/defender-for-cloud/prepurchase-plan) |
| Conectar AWS, GCP, Arc y los entornos de DevOps | R | A | I | R | I | C | [Learn](https://learn.microsoft.com/en-us/azure/defender-for-cloud/permissions) |
| Clasificar y responder alertas e incidentes | I | C | A/R | C | I | C | [Learn](https://learn.microsoft.com/en-us/security/zero-trust/security-adoption-discipline-security-operations-incidents) |
| Remediar recomendaciones | C | A | I | C | I | R | [Learn](https://learn.microsoft.com/en-us/azure/defender-for-cloud/governance-rules) |
| Gestionar reglas de gobernanza y exenciones (aceptar riesgos) | C | A/R | I | C | I | C | [Learn](https://learn.microsoft.com/en-us/azure/defender-for-cloud/exempt-resource) |
| Proteger el código: secretos, IaC e imágenes | I | C | I | A/R | I | C | [Learn](https://learn.microsoft.com/en-us/azure/defender-for-cloud/secrets-scanning-code) |
| Proteger cargas de IA (AI-SPM, Defender for AI Services y evidencia de prompts) | R | A | C | C | I | R | [Learn](https://learn.microsoft.com/en-us/azure/defender-for-cloud/ai-onboarding) |
| Cerrar rutas de ataque hacia activos críticos | R | A | C | R | I | R | [Learn](https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-attack-path) |
| Mantener la exportación continua, la integración con el SIEM y los tableros de KPI | R | A | R | I | C | I | [Learn](https://learn.microsoft.com/en-us/azure/defender-for-cloud/benefits-of-continuous-export) |
| Automatizar la respuesta (workflow automation y Logic Apps) | R | A | R | C | I | I | [Learn](https://learn.microsoft.com/en-us/azure/defender-for-cloud/workflow-automations) |
| Operar Security Copilot (SCU, casos de uso y revisión humana) | I | A | R | I | C | I | [Learn](https://learn.microsoft.com/en-us/copilot/security/security-copilot-inclusion) |
| Revisar la postura cada trimestre y gestionar los cambios de producto | C | A/R | C | C | C | I | [Learn](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/secure/overview) |

R = responsable, A = rinde cuentas, C = consultado, I = informado. Propuesta del programa: no existe un RACI oficial de Microsoft para Defender for Cloud. El CAF recomienda documentar un modelo de responsabilidad compartida que funcione como RACI, y la [matriz de permisos](https://learn.microsoft.com/en-us/azure/defender-for-cloud/permissions) y las [reglas de gobernanza](https://learn.microsoft.com/en-us/azure/defender-for-cloud/governance-rules) lo hacen ejecutable. «Seguridad y arquitectura» incluye al CISO y al centro de excelencia.

### Documentación, cursos y credenciales

- [User roles and permissions (Defender for Cloud)](https://learn.microsoft.com/en-us/azure/defender-for-cloud/permissions) · Documentación · Oficial · Nuevo · Microsoft Learn · 17 jun 2026. Tabla oficial de roles de Azure (Security Reader, Security Admin, Reader, Contributor, Owner) y acciones permitidas: habilitar planes, editar políticas, descartar alertas, exenciones, Fix; además, roles y permisos que crean los conectores de AWS y GCP por plan.
- [Drive recommendation remediation by using governance rules](https://learn.microsoft.com/en-us/azure/defender-for-cloud/governance-rules) · Documentación · Oficial · Microsoft Learn. Reglas de gobernanza (Defender CSPM) que asignan dueño (incluso por etiqueta) y fecha límite de 7, 14, 30 o 90 días, con período de gracia, prioridad 1-1000, notificaciones semanales al dueño y a su jefe, e informe de gobernanza.
- [Security teams, roles, and functions (Cloud Adoption Framework – Secure)](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/secure/teams-roles) · Documentación · Oficial · Microsoft Learn (CAF). Describe los roles y funciones de seguridad en la nube (arquitectura, ingeniería, operaciones, postura, DevSecOps) y recomienda documentar un modelo de responsabilidad compartida que funcione como una matriz RACI.
- [Secure overview (Cloud Adoption Framework)](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/secure/overview) · Documentación · Oficial · Microsoft Learn (CAF). Metodología Secure del CAF: modernizar la postura, preparar y responder a incidentes, tríada CIA y sostener la postura midiendo con la puntuación segura de Defender for Cloud y automatizando la detección de deriva.
- [Microsoft Security Adoption Framework (SAF)](https://learn.microsoft.com/en-us/security/zero-trust/security-adoption-model) · Documentación · Oficial · Microsoft Learn (Security). SAF como modelo operativo: escenarios de negocio, disciplinas de seguridad, tecnologías y soluciones técnicas, con roles de negocio, tecnología y seguridad que comparten resultados medibles bajo principios Zero Trust.
- [Perform your cloud adoption securely (CAF Secure – Adopt)](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/secure/adopt) · Documentación · Oficial · Microsoft Learn (CAF). Recomendaciones de seguridad para la fase Adopt (líneas base, automatización, controles Zero Trust) e institucionalización del cambio con ADKAR, Kotter, Lewin y el marco de adopción de Microsoft.
- [Security considerations for your cloud strategy (CAF Strategy)](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/strategy/inform/security) · Documentación · Oficial · Microsoft Learn (CAF). Cómo ajustar equipos y roles al pasar a la nube, adoptar la metodología Secure, la Secure Future Initiative, Zero Trust y los talleres CISO y MCRA.
- [Security Adoption Resources (SAF workshops, CISO Workshop, MCRA)](https://learn.microsoft.com/en-us/security/adoption/adoption) · Documentación · Oficial · Microsoft Learn (Security). Puerta de entrada a los recursos públicos del SAF: CISO Workshop, Microsoft Cybersecurity Reference Architectures, guías de modernización, antipatrones y talleres de Microsoft Unified (de 4 horas a varios días).
- [Overview - security disciplines (Security Adoption Framework)](https://learn.microsoft.com/en-us/security/zero-trust/security-adoption-discipline-overview) · Documentación · Oficial · Microsoft Learn (Security). Disciplinas del SAF agrupadas en planificación y supervisión, estrategia técnica y operación, que definen la propiedad y rendición de cuentas de cada capacidad de seguridad.

### Anuncios y blogs oficiales

- [New Blog | Best Practices to Manage and Mitigate Security Recommendations](https://techcommunity.microsoft.com/discussions/microsoftdefendercloud/new-blog--best-practices-to-manage-and-mitigate-security-recommendations/4154262) · Blog oficial · Empleado de Microsoft · Legado aún útil · Giulio Astori · Microsoft Tech Community – Microsoft Defender for Cloud · 28 may 2024. Buenas prácticas de reglas de gobernanza en Defender CSPM: dueños claros, ETA y periodos de gracia realistas, priorización por riesgo, integración con flujos y revisión continua. *Nota:* Resumen de un post más largo; las capturas son del Azure portal

### Webinars, videos y podcasts

- [Go Beyond Checkboxes: Proactive Cloud Security with Microsoft Defender CSPM (webinar)](https://www.youtube.com/watch?v=SZx4ztnt8RE) · Webinar · Empleado de Microsoft · Giulio Astori · YouTube · Microsoft Security Community · 30 abr 2025. Webinar de la comunidad de seguridad de Microsoft sobre pasar de una seguridad orientada a casillas de cumplimiento a una postura proactiva con Defender CSPM, integrando CSPM en flujos de desarrollo y operaciones.
- [Governance capability improvements in Defender for Cloud (Defender for Cloud in the Field)](https://learn.microsoft.com/en-us/azure/defender-for-cloud/episode-twenty-six) · Video · Empleado de Microsoft · Legado aún útil · Nuevo · Lior Arviv y Yuri Diogenes · Microsoft Learn · 17 jun 2026. Por qué se necesita gobernanza de recomendaciones, reglas a escala, opciones de despliegue y monitoreo de asignaciones y prioridades. *Nota:* Página actualizada en jun-2026; el episodio es anterior a la integración con el portal de Defender

**Manos a la obra**

1. `Laboratorio` Adapta la tabla RACI de este módulo a tu organización —nombres de equipos, aprobadores y excepciones— y tradúcela a asignaciones de roles de Azure (Security Reader, Security Admin, Contributor y Owner) y del RBAC unificado del portal de Defender ([permisos](https://learn.microsoft.com/en-us/azure/defender-for-cloud/permissions), [cloud scopes y RBAC unificado](https://learn.microsoft.com/en-us/azure/defender-for-cloud/cloud-scopes-unified-rbac)). Evidencia: RACI aprobado y matriz de roles por equipo.
2. `Laboratorio` Convierte el RACI en reglas de gobernanza: una regla para las recomendaciones de severidad alta con dueño leído de la etiqueta `owner`, 14 días de plazo y período de gracia, y otra de mayor prioridad para un grupo de recursos que simule producción ([reglas de gobernanza](https://learn.microsoft.com/en-us/azure/defender-for-cloud/governance-rules)). Evidencia: reglas creadas y el informe de gobernanza con las primeras asignaciones.
3. `Laboratorio` Redacta la carta del centro de excelencia de seguridad en la nube: alcance, miembros, cadencia (semanal operativa, mensual de postura y trimestral ejecutiva), derechos de decisión —exenciones, habilitación de planes y migración a DWU— y métricas ([metodología Secure del CAF](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/secure/overview), [disciplinas del Security Adoption Framework](https://learn.microsoft.com/en-us/security/zero-trust/security-adoption-discipline-overview)). Evidencia: carta aprobada por el CISO.
4. `Laboratorio` Define el proceso de exenciones —categorías Mitigated y Risk accepted, vencimiento obligatorio, aprobador y revisión mensual— y crea una exención de prueba con vencimiento a 7 días ([exenciones](https://learn.microsoft.com/en-us/azure/defender-for-cloud/exempt-resource)). Evidencia: procedimiento publicado y la exención visible con su vencimiento.
5. `Laboratorio` Haz que Owner y Security Admin sean roles elegibles con aprobación y justificación en la suscripción del laboratorio y prueba una activación; registra qué tareas del RACI exigen cada rol según la matriz de permisos ([permisos](https://learn.microsoft.com/en-us/azure/defender-for-cloud/permissions)). Evidencia: asignación elegible, registro de activación y la tabla tarea-rol. Privileged Identity Management se profundiza en el programa de Entra (M3).
6. `Solo producción` Crea cloud scopes por unidad de negocio o por frontera regulatoria y asigna permisos del RBAC unificado ([cloud scopes y RBAC unificado](https://learn.microsoft.com/en-us/azure/defender-for-cloud/cloud-scopes-unified-rbac)). Requiere varias suscripciones o cuentas y analistas reales, y la función está en preview. Cómo hacerlo seguro: empieza con un scope «Piloto» de solo lectura, valida los filtros con un analista y documenta que los entornos nuevos no se agregan solos. Evidencia: scopes creados y prueba de acceso del analista.

**¿Quieres profundizar?**

- [Governance capability improvements in Defender for Cloud (Defender for Cloud in the Field)](https://learn.microsoft.com/en-us/azure/defender-for-cloud/episode-twenty-six) · Video

<a id="o2"></a>

## O2 · Métricas, KPI e informes ejecutivos

*L300–L400 · ~5 h · Origen: Nuevo en esta edición (base: libros integrados de Defender for Cloud, métricas de Exposure Management y métricas de incidentes de Microsoft Sentinel)*

Medir la seguridad en la nube exige elegir bien la fuente. Defender for Cloud trae libros integrados —Coverage, Secure Score Over Time, System Updates, Vulnerability Assessment Findings, Compliance Over Time, Active Alerts, Price Estimation, Governance y DevOps Security—, y Secure Score Over Time necesita **exportación continua** con streaming e instantáneas semanales. Conviven **dos puntuaciones**: la Cloud Secure Score basada en riesgo, solo en el portal de Defender, y la clásica del portal de Azure; no son comparables, se recalculan cada 8 horas y las recomendaciones en preview no cuentan. Desde el 30 de junio de 2026, más de 200 recomendaciones de AWS y GCP afectan la puntuación: cada cambio así exige una nueva línea base.

Para el SOC, la tabla `SecurityIncident` y el libro «Security operations efficiency» de Sentinel dan MTTA y MTTR con percentiles, con las definiciones del Security Adoption Framework. Para la exposición, las **iniciativas de Exposure Management** tienen puntuación, meta configurable, tendencia de 14 días e historial, y sus métricas de nube requieren Defender CSPM. Un buen tablero ejecutivo combina pocas métricas de resultado —tendencia de la puntuación, burn-down de recomendaciones altas, rutas de ataque cerradas, cobertura, MTTA y MTTR, cumplimiento y costo por recurso protegido— con su fuente, su latencia y su meta. Las métricas del SOC se profundizan en el programa de Defender XDR (S3).

**Por qué importa**

Lo que no se mide no se financia. Un tablero con definiciones estables, fuentes trazables y metas acordadas convierte a Defender for Cloud de «otra consola» en un programa que rinde cuentas: muestra a la dirección si el riesgo baja, cuánto cuesta y dónde se atasca la remediación, y evita discutir cifras incomparables entre portales.

**Qué vas a lograr**

- Seleccionar KPI de resultado con fórmula, fuente, latencia y meta.
- Configurar la exportación continua y los libros que alimentan las tendencias.
- Calcular MTTA y MTTR de los incidentes de nube con KQL sobre SecurityIncident.
- Explicar por qué las dos puntuaciones seguras no son comparables y cuándo rehacer la línea base.
- Producir un informe ejecutivo mensual de una página con decisiones concretas.

> **Atención.** Comparabilidad: la Cloud Secure Score (portal de Defender) y la clásica (portal de Azure) usan cálculos distintos y no se comparan; las recomendaciones en preview no cuentan, más de 200 recomendaciones de AWS y GCP cuentan desde el 30 de junio de 2026 y las recomendaciones agrupadas desaparecieron el 31 de julio. Cada cambio exige una nueva línea base y una nota en el tablero ([puntuación segura](https://learn.microsoft.com/en-us/azure/defender-for-cloud/secure-score-security-controls), [transición a recomendaciones individuales](https://learn.microsoft.com/en-us/azure/defender-for-cloud/transition-grouped-individual-recommendations)).

> **Consejo Ninja.** La exportación continua no tiene un cargo propio documentado: el costo está en la ingesta y la retención del destino (Log Analytics o Event Hubs), con un límite de 32 KB por registro. Filtra por tipo y severidad y usa las instantáneas semanales para las tendencias ([exportación continua](https://learn.microsoft.com/en-us/azure/defender-for-cloud/continuous-export), [beneficios de la exportación](https://learn.microsoft.com/en-us/azure/defender-for-cloud/benefits-of-continuous-export)).

> **Novedad.** Desde el 30 de junio de 2026 los informes de seguridad en la nube del portal de Defender son GA, y desde el 5 de mayo la Cloud Secure Score guarda instantáneas diarias de fin de día. Las métricas de exposición van de 0 a 100, con peso editable y la opción «Risk accepted»; las de nube requieren Defender CSPM ([notas de versión](https://learn.microsoft.com/en-us/azure/defender-for-cloud/release-notes), [métricas de seguridad](https://learn.microsoft.com/en-us/security-exposure-management/security-metrics)).

> **Consejo Ninja.** Las metas de la tabla de KPI del programa son propuestas para organizaciones grandes, no valores oficiales de Microsoft: fíjalas a partir de tu línea base y publica cada valor con su fuente y su latencia. Para el SOC, usa las definiciones de MTTA y MTTR del Security Adoption Framework ([métricas de incidentes](https://learn.microsoft.com/en-us/azure/sentinel/manage-soc-with-incident-metrics), [incidentes en el SAF](https://learn.microsoft.com/en-us/security/zero-trust/security-adoption-discipline-security-operations-incidents)).

**¿Tienes poco tiempo?**

- [Create interactive reports with Azure Monitor workbooks (Defender for Cloud gallery)](https://learn.microsoft.com/en-us/azure/defender-for-cloud/custom-dashboards-azure-workbooks) · Documentación
- [Secure score in Defender for Cloud (classic Secure Score and Cloud Secure Score)](https://learn.microsoft.com/en-us/azure/defender-for-cloud/secure-score-security-controls) · Documentación
- [Manage your SOC better with incident metrics](https://learn.microsoft.com/en-us/azure/sentinel/manage-soc-with-incident-metrics) · Documentación
- [Microsoft Security Exposure Management initiatives](https://learn.microsoft.com/en-us/security-exposure-management/initiatives) · Documentación

### Documentación, cursos y credenciales

- [Secure score in Defender for Cloud (classic Secure Score and Cloud Secure Score)](https://learn.microsoft.com/en-us/azure/defender-for-cloud/secure-score-security-controls) · Documentación · Oficial · Nuevo · Microsoft Learn · 30 jun 2026. Explica los dos modelos: la puntuación segura clásica (portal de Azure, basada en controles del MCSB, recalculada cada 8 h) y la nueva Cloud Secure Score basada en riesgo (portal de Defender, 0-100, pondera nivel de riesgo, factores de riesgo y criticidad del activo).
- [Create interactive reports with Azure Monitor workbooks (Defender for Cloud gallery)](https://learn.microsoft.com/en-us/azure/defender-for-cloud/custom-dashboards-azure-workbooks) · Documentación · Oficial · Microsoft Learn. Describe los libros integrados de Defender for Cloud: Coverage, System Updates, Vulnerability Assessment Findings, Price Estimation, Active Alerts, Governance y otros, con sus requisitos.
- [Plan for incident response in the security adoption model (SAF SecOps)](https://learn.microsoft.com/en-us/security/zero-trust/security-adoption-discipline-security-operations-incidents) · Documentación · Oficial · Microsoft Learn (Security). Define MTTA (tiempo para reconocer una alerta o incidente desde su generación) y MTTR (tiempo para corregir tras el reconocimiento) como métricas críticas de SecOps, más principios y playbooks de respuesta.
- [Manage your SOC better with incident metrics](https://learn.microsoft.com/en-us/azure/sentinel/manage-soc-with-incident-metrics) · Documentación · Oficial · Microsoft Learn. Tabla SecurityIncident y libro Security operations efficiency con tiempo medio de triage y de cierre, percentiles y consultas KQL de ejemplo para KPI del SOC (incluidas alertas de Defender for Cloud que llegan como incidentes).
- [Microsoft Security Exposure Management initiatives](https://learn.microsoft.com/en-us/security-exposure-management/initiatives) · Documentación · Oficial · Microsoft Learn. Iniciativas de Exposure Management (incluida la iniciativa Cloud Security donde vive la Cloud Secure Score) para medir y priorizar la reducción de exposición por dominio.
- [Exposure insights overview (Microsoft Security Exposure Management)](https://learn.microsoft.com/en-us/security-exposure-management/exposure-insights-overview) · Documentación · Oficial · Microsoft Learn. Iniciativas (cargas como nube, amenazas horizontales como ransomware, Zero Trust, EASM), métricas, recomendaciones y eventos de caída de puntuación para que el CISO mida exposición en el tiempo.
- [Review security metrics in Microsoft Security Exposure Management](https://learn.microsoft.com/en-us/security-exposure-management/security-metrics) · Documentación · Oficial · Microsoft Learn · 12 ene 2025. Métricas con progreso de 0 a 100, activos afectados, peso editable y opción «Risk accepted»; las métricas de nube requieren Defender CSPM habilitado.

### Anuncios y blogs oficiales

- [New Blog | Operationalizing Attack Path Insights](https://techcommunity.microsoft.com/discussions/microsoftdefendercloud/new-blog--operationalizing-attack-path-insights/4121709) · Blog oficial · Empleado de Microsoft · Legado aún útil · Giulio Astori · Microsoft Tech Community – Microsoft Defender for Cloud · 23 abr 2024. Workbook de rutas de ataque en el tiempo alimentado por exportación continua a Log Analytics (retención recomendada 90 días) para medir tendencias de exposición. *Nota:* La ingesta en Log Analytics tiene costo

### Webinars, videos y podcasts

- [Defender for Cloud in the field (Learn Shows)](https://learn.microsoft.com/en-us/shows/mdc-in-the-field/) · Video · Oficial · Yuri Diogenes (presentador) y PM invitados · Microsoft Learn Shows · 3 feb 2026. Serie oficial de episodios cortos (66 en Learn) en la que product managers del equipo demuestran cada capacidad nueva de Defender for Cloud; último episodio «New Secure Score» del 3-feb-2026.

### Laboratorios, GitHub y herramientas

- [Azure Workbooks for Microsoft Defender for Cloud (README)](https://github.com/Azure/Microsoft-Defender-for-Cloud/blob/main/Workbooks/README.md) · GitHub · Oficial · Legado aún útil · Tom Janetscheck y comunidad · GitHub – Azure. Catálogo de workbooks (cobertura, estado de despliegue y monitoreo de Defender for Servers, CVE, cumplimiento, gamificación del Secure Score, estimación de precios por plan) con guía para contribuir. *Nota:* Los workbooks de precio no reflejan DWU. Fecha exacta no visible (año de referencia: 2022)

**Manos a la obra**

1. `Laboratorio parcial` Configura la exportación continua a `log-lab-mdc-eus2` con streaming e instantáneas semanales, filtrando por severidad, y activa los libros Secure Score Over Time y Coverage ([exportación continua](https://learn.microsoft.com/en-us/azure/defender-for-cloud/continuous-export), [libros](https://learn.microsoft.com/en-us/azure/defender-for-cloud/custom-dashboards-azure-workbooks)). Limitación: la tendencia necesita al menos una semana de instantáneas. Evidencia: libros con datos y GB ingeridos por la exportación.
2. `Laboratorio` Calcula la línea base de burn-down: cuenta con Azure Resource Graph las recomendaciones no saludables de severidad alta por suscripción con el modelo individual y guárdala con fecha ([ejemplos de Azure Resource Graph](https://learn.microsoft.com/en-us/azure/defender-for-cloud/resource-graph-samples), [transición a recomendaciones individuales](https://learn.microsoft.com/en-us/azure/defender-for-cloud/transition-grouped-individual-recommendations)). Evidencia: consulta y valor inicial del KPI.
3. `Laboratorio parcial` Escribe la consulta KQL de MTTA y MTTR (mediana y percentil 90) sobre `SecurityIncident` para los incidentes de Defender for Cloud y compárala con el libro «Security operations efficiency» ([métricas de incidentes](https://learn.microsoft.com/en-us/azure/sentinel/manage-soc-with-incident-metrics), [incidentes en el Security Adoption Framework](https://learn.microsoft.com/en-us/security/zero-trust/security-adoption-discipline-security-operations-incidents)). Limitación: un laboratorio genera pocos incidentes para que los percentiles signifiquen algo. Evidencia: consulta versionada y resultado.
4. `Laboratorio` Registra en la misma fecha la Cloud Secure Score del portal de Defender y la puntuación clásica del portal de Azure, y escribe la nota metodológica que explica por qué no se comparan y cuál usará tu tablero ([puntuación segura](https://learn.microsoft.com/en-us/azure/defender-for-cloud/secure-score-security-controls)). Evidencia: ambos valores con su captura y la nota aprobada.
5. `Laboratorio parcial` En Exposure Management, revisa la iniciativa de seguridad en la nube, fija una meta y anota su tendencia de 14 días; ajusta el peso de una métrica y documenta el cambio ([iniciativas](https://learn.microsoft.com/en-us/security-exposure-management/initiatives), [métricas de seguridad](https://learn.microsoft.com/en-us/security-exposure-management/security-metrics)). Limitación: las métricas de nube requieren Defender CSPM y la tendencia necesita días de datos. Evidencia: meta configurada y captura de la tendencia.
6. `Solo producción` Produce el informe ejecutivo mensual de una página: de seis a ocho KPI de la tabla del programa con tendencia, meta, fuente y latencia, el costo por recurso protegido y tres decisiones que pides a la dirección ([libros](https://learn.microsoft.com/en-us/azure/defender-for-cloud/custom-dashboards-azure-workbooks), [costos en el portal de Defender](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-portal/estimate-track-costs)). Requiere datos reales de varias semanas. Cómo hacerlo seguro: obtén los datos con roles de lectura (Security Reader y Log Analytics Reader) desde un área de trabajo de reporting y valida las cifras con sus dueños antes de publicar. Evidencia: informe presentado y decisiones registradas.

**¿Quieres profundizar?**

- [Defender for Cloud in the field (Learn Shows)](https://learn.microsoft.com/en-us/shows/mdc-in-the-field/) · Video
- [Azure Workbooks for Microsoft Defender for Cloud (README)](https://github.com/Azure/Microsoft-Defender-for-Cloud/blob/main/Workbooks/README.md) · GitHub

<a id="o3"></a>

## O3 · Cumplimiento regulatorio, estándares personalizados y evidencia

*L300–L400 · ~5 h · Origen: Ninja oficial de Defender for Cloud: cumplimiento regulatorio; alineado con la Applied Skill vigente de cumplimiento regulatorio con Defender for Cloud*

El panel de cumplimiento regulatorio de Defender for Cloud evalúa tus recursos contra estándares implementados como iniciativas de Azure Policy. Por defecto asigna el **MCSB** en Azure, el MCSB más **AWS Foundational Security Best Practices** en AWS y el MCSB más **GCP Default** en GCP; el MCSB v2 sigue en preview aunque Azure Landing Zones lo asigna por defecto. El catálogo de noviembre de 2026 incluye, entre otros, PCI DSS 4.0.1, ISO/IEC 27001:2022, NIST CSF 2.0, NIST SP 800-53 R5.1.1, CIS, SOC 2, DORA y la Ley de IA de la UE. Las evaluaciones corren aproximadamente cada 12 horas, los controles manuales admiten atestación con evidencia y los informes se descargan desde el panel.

Tres matices son clave. Qué plan habilita los estándares adicionales es **contradictorio** entre páginas de Learn: solo Defender CSPM, cualquier plan pago salvo Servers P1 o APIs P1, o «al menos un plan pago». Asignar estándares requiere Owner o Policy Contributor y, para leer el cumplimiento, Reader sirve y Security Reader no. Y no hay estándares de México, Colombia, Chile, Perú o Argentina: mapea la regulación local a ISO/IEC 27001:2022, NIST CSF 2.0 o un **estándar personalizado** con recomendaciones KQL (Defender CSPM). Los datos fluyen solos a Purview Compliance Manager, que se profundiza en ese programa (M2). Este módulo es referencia técnica, no asesoría legal.

**Por qué importa**

Los reguladores financieros de la región piden evidencia continua de controles en la nube, no capturas de pantalla anuales. Convertir los estándares en iniciativas evaluadas, con controles manuales atestados, exportación continua y acceso de solo lectura para auditores, reduce el esfuerzo de auditoría y te permite demostrar cumplimiento en días en lugar de semanas.

**Qué vas a lograr**

- Asignar estándares regulatorios con el rol y el plan correctos y leer el panel de cumplimiento.
- Crear un estándar personalizado con recomendaciones KQL para la línea base de tu organización.
- Gestionar controles manuales, atestaciones y exenciones con vencimiento.
- Automatizar la evidencia con exportación continua, workflow automation y Purview Compliance Manager.
- Mapear la regulación financiera y de ciberseguridad de MCSA a controles evaluados, junto con Legal.

> **Atención.** ¿Qué plan habilita los estándares adicionales? Learn da tres versiones: «Regulatory compliance assessments» solo en Defender CSPM (tabla de CSPM), cualquier plan de Defender salvo Servers P1 o APIs P1 (asignar estándares) y «al menos un plan pago» (panel de cumplimiento). La matriz de Defender for Servers también los ubica en P1 y P2. Verifica en tu inquilino y documenta la decisión ([CSPM](https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-cloud-security-posture-management), [asignar estándares](https://learn.microsoft.com/en-us/azure/defender-for-cloud/assign-regulatory-compliance-standards), [panel de cumplimiento](https://learn.microsoft.com/en-us/azure/defender-for-cloud/regulatory-compliance-dashboard)).

> **Atención.** Este módulo es referencia técnica, no asesoría legal. Las obligaciones, los plazos de notificación y su aplicación a tu organización los define tu área de Legal con el texto oficial vigente, junto con privacidad y cumplimiento. La hoja «Normativa MCSA» del libro de Excel resume privacidad, ciberseguridad y sector financiero por país, con sus fuentes y su estado de verificación.

> **Novedad.** Defender for Cloud agregó cuatro marcos regulatorios en julio de 2025 y el catálogo de noviembre de 2026 incluye DORA, la Ley de IA de la UE, NIST CSF 2.0, PCI DSS 4.0.1 e ISO/IEC 27001:2022. El MCSB v2, con un dominio de seguridad de IA y más de 420 definiciones de Azure Policy, sigue en preview aunque ALZ lo asigna por defecto ([nuevos marcos](https://techcommunity.microsoft.com/blog/microsoftdefendercloudblog/microsoft-defender-for-cloud-adds-four-new-regulatory-frameworks/4433440), [estándares disponibles](https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-regulatory-compliance-standards), [MCSB](https://learn.microsoft.com/en-us/security/benchmark/azure/introduction)).

> **Consejo Ninja.** Compliance Manager recibe automáticamente los datos por recurso de los estándares asignados en Defender for Cloud (incluidos AWS y GCP), pero su lista de regulaciones comunes muestra versiones antiguas (PCI DSS 3.2.1, NIST 800-53 Rev. 4): alinea versiones antes de presentar cifras. En el portal de Defender el cumplimiento es solo de consumo; las asignaciones siguen en el portal de Azure ([Compliance Manager multinube](https://learn.microsoft.com/en-us/purview/compliance-manager-multicloud), [configuración de Compliance Manager](https://learn.microsoft.com/en-us/purview/compliance-manager-cloud-settings)).

**¿Tienes poco tiempo?**

- [Regulatory compliance standards in Microsoft Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-regulatory-compliance-standards) · Documentación
- [Assign regulatory compliance standards in Microsoft Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/assign-regulatory-compliance-standards) · Documentación
- [Improve regulatory compliance in Microsoft Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/regulatory-compliance-dashboard) · Documentación
- [Microsoft Defender for Cloud Adds Four New Regulatory Frameworks](https://techcommunity.microsoft.com/blog/microsoftdefendercloudblog/microsoft-defender-for-cloud-adds-four-new-regulatory-frameworks/4433440) · Blog oficial

**Estándares regulatorios en Defender for Cloud**

| Estándar | Versión | Plan requerido | Nubes | Uso sugerido en MCSA | Fuente |
|---|---|---|---|---|---|
| Microsoft cloud security benchmark (MCSB) | v1 (por defecto) | Ninguno (incluido) | Azure, AWS y GCP | Línea base técnica de todo el programa y base de la puntuación clásica | [Learn](https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-regulatory-compliance-standards) |
| Microsoft cloud security benchmark (MCSB) | v2 (preview) | Se activa desde el panel de cumplimiento; Azure Landing Zones lo asigna por defecto | Azure (guía multinube) | Evalúalo en paralelo: agrega un dominio de seguridad de IA | [Learn](https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-regulatory-compliance) · [Learn](https://learn.microsoft.com/en-us/security/benchmark/azure/introduction) |
| AWS Foundational Security Best Practices | Por defecto en AWS | Ninguno | AWS | Línea base de las cuentas de AWS | [Learn](https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-regulatory-compliance-standards) |
| GCP Default | Por defecto en GCP | Ninguno | GCP | Línea base de los proyectos de GCP | [Learn](https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-regulatory-compliance-standards) |
| PCI DSS | v4.0.1 | Plan pago (contradictorio entre páginas) | Azure, AWS y GCP | Emisores, adquirentes y comercios que procesan tarjetas | [Learn](https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-regulatory-compliance-standards) |
| ISO/IEC 27001, 27002 y 27017 | 2022, 2022 y 2015 | Plan pago | Azure, AWS y GCP | Marco común para mapear normas financieras locales (SFC, CMF, SBS o BCRA) | [Learn](https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-regulatory-compliance-standards) |
| NIST CSF | v2.0 | Plan pago | Azure, AWS y GCP | Programas de riesgo y el Marco de Ciberseguridad de Uruguay, alineado con NIST CSF 2.0 | [Learn](https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-regulatory-compliance-standards) · [impo.com.uy](https://www.impo.com.uy/bases/decretos/66-2025/8) |
| NIST SP 800-53 y NIST 800-171 | R5.1.1 y Rev3 | Plan pago | Azure, AWS y GCP | Catálogo de controles detallado para mapeos; proveedores de clientes de EE. UU. | [Learn](https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-regulatory-compliance-standards) |
| CIS Azure Foundations | v2.1.0 y v3.0 | Plan pago | Azure | Endurecimiento técnico de suscripciones | [Learn](https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-regulatory-compliance-standards) |
| CIS AWS Foundations y CIS GCP Foundations | v3.0.0 y v3.0 | Plan pago | AWS y GCP | Endurecimiento técnico multinube | [Learn](https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-regulatory-compliance-standards) |
| CIS Controls y benchmarks de AKS, EKS y GKE | v8.1 | Plan pago | Azure, AWS y GCP | Programa de controles y Kubernetes | [Learn](https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-regulatory-compliance-standards) |
| SOC 2 y SOC 2023 | — | Plan pago | Azure y GCP / Azure, AWS y GCP | Proveedores de servicios que reportan a sus clientes | [Learn](https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-regulatory-compliance-standards) |
| CSA Cloud Controls Matrix | v4.0.12 | Plan pago | Azure, AWS y GCP | Evaluación de proveedores de nube | [Learn](https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-regulatory-compliance-standards) |
| HITRUST CSF | v11.3.0 | Plan pago | Azure, AWS y GCP | Organizaciones de salud | [Learn](https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-regulatory-compliance-standards) |
| NIS2, GDPR, DORA y Ley de IA de la UE | 2022, 2016 y vigentes | Plan pago | Azure, AWS y GCP | Grupos con operaciones en la UE; referencia comparada, no normativa de MCSA | [Learn](https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-regulatory-compliance-standards) |
| SWIFT CSCF, SOX, FFIEC CAT, CJIS y CMMC L2 | 2024, 2022, 2017, v5.9.5 y v2.0 | Plan pago | Azure, AWS y GCP | Bancos conectados a SWIFT y emisoras listadas en EE. UU. | [Learn](https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-regulatory-compliance-standards) |
| LGPD | 2018 | Plan pago | Azure, AWS y GCP | Es de Brasil, fuera de MCSA: solo para grupos regionales con operaciones allí | [Learn](https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-regulatory-compliance-standards) |
| FedRAMP High y Moderate, HIPAA, Spanish ENS y RMIT Malaysia | — | Plan pago | Azure | Casos específicos | [Learn](https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-regulatory-compliance-standards) |
| Estándar personalizado | — | Recomendaciones KQL: Defender CSPM y Security Admin; el estándar requiere Owner | Azure, AWS y GCP | Normas locales sin plantilla, como la regulación financiera de cada país | [Learn](https://learn.microsoft.com/en-us/azure/defender-for-cloud/create-custom-recommendations) |

Catálogo al 7 de noviembre de 2026. No hay estándares específicos de México, Colombia, Chile, Perú o Argentina. Qué plan habilita los estándares adicionales es contradictorio en Learn; asignar requiere Owner o Policy Contributor y leer el cumplimiento, Reader ([asignar estándares](https://learn.microsoft.com/en-us/azure/defender-for-cloud/assign-regulatory-compliance-standards), [panel de cumplimiento](https://learn.microsoft.com/en-us/azure/defender-for-cloud/regulatory-compliance-dashboard)). Referencia técnica, no asesoría legal.

**Normativa financiera y de ciberseguridad de MCSA: qué evidencia técnica puede aportar Defender for Cloud**

| País | Norma | Qué exige (resumen de la fuente) | Plazo de notificación según la fuente | Evidencia técnica de Defender for Cloud | Fuente |
|---|---|---|---|---|---|
| México | CUB de la CNBV (arts. 168 Bis) | Oficial de seguridad, plan director, gestión de incidentes con aviso a la CNBV y requisitos para terceros, incluida la nube | Aviso inmediato según análisis secundarios (confirmar en el texto vigente) | Estándar ISO/IEC 27001:2022 asignado, historial de incidentes y exportación continua | [cnbv.gob.mx](https://www.cnbv.gob.mx/Normatividad/Disposiciones%20de%20car%C3%A1cter%20general%20aplicables%20a%20las%20instituciones%20de%20cr%C3%A9dito.pdf) |
| Guatemala | Resolución JM-104-2021 (riesgo tecnológico) | Gobierno de TI, seguridad de la información, continuidad y control de servicios de terceros | — | Inventario multinube, reglas de gobernanza con dueño y plazo | [banguat.gob.gt](https://banguat.gob.gt/sites/default/files/banguat/Publica/Res_JM/2021/Res_JM-104-2021.pdf) |
| Costa Rica | Acuerdo CONASSIF 5-24 | Gobierno y gestión de TI, riesgos tecnológicos y ciberseguridad, terceros y auditoría externa de TI | — | Informes de cumplimiento descargables y acceso Reader para auditores | [sugef.fi.cr](https://www.sugef.fi.cr/normativa/normativa_transversal/documentos/CONASSIF%205-24%20%28v03%2015%20julio%202025%29.pdf) |
| Panamá | Acuerdo 3-2012 de la Superintendencia de Bancos | Gestión del riesgo de TI: gobierno, seguridad de la información y continuidad | — | Postura, recomendaciones con dueño y evidencia de remediación | [superbancos.gob.pa](https://www.superbancos.gob.pa/documentos/leyes_y_regulaciones/acuerdos/2012/Acuerdo_3-2012.pdf) |
| Colombia | Circular Externa 007 de 2018 de la SFC (ciberseguridad) | Política y unidad responsable, gestión y reporte de incidentes, pruebas y gestión de terceros | — (Compliance Manager tiene plantilla) | Incidentes con línea de tiempo, playbooks probados e integración con Sentinel | [superfinanciera.gov.co](https://www.superfinanciera.gov.co/loader.php?lServicio=Tools2&lTipo=descargas&lFuncion=descargar&idFile=1031904) |
| Colombia | Circular Externa 005 de 2019 de la SFC (nube) | Gestión de riesgos de la nube, requisitos contractuales mínimos e información disponible para la SFC | — | Inventario multinube, residencia de datos documentada y exportación de evidencia | [superfinanciera.gov.co](https://www.superfinanciera.gov.co/loader.php?lServicio=Tools2&lTipo=descargas&lFuncion=descargar&idFile=1070310) |
| Ecuador | Ley Orgánica para el Fortalecimiento de la Ciberseguridad (vigente desde el 22-may-2026) | Gestión y notificación de incidentes para entidades públicas, infraestructura crítica y prestadores de servicios digitales, incluida la nube | 72 horas según análisis de firmas; formatos por normativa secundaria | Línea de tiempo del incidente y evidencia del plano de control | [asambleanacional.gob.ec](https://www.asambleanacional.gob.ec/es/system/files/ro_29.pdf) |
| Perú | Resolución SBS 504-2021 | Sistema de gestión de seguridad de la información y ciberseguridad, gestión de incidentes y requisitos para la nube | — | Estándares asignados, controles manuales atestados y KPI de remediación | [intranet2.sbs.gob.pe](https://intranet2.sbs.gob.pe/dv_int_cn/2046/v4.0/Adjuntos/504-2021.R.pdf) |
| Chile | Ley 21.663 y Decreto 295 de 2024 | Gestión de riesgos y reporte de incidentes al CSIRT Nacional para servicios esenciales y operadores de importancia vital | Alerta temprana en 3 horas y segundo reporte en 72 horas (24 horas en ciertos casos de operadores de importancia vital) | MTTA medido, playbooks con hitos de notificación y evidencia exportada | [leychile.cl](https://www.leychile.cl/leychile/Navegar/imprimir?idNorma=1211466) · [leychile.cl](https://www.leychile.cl/leychile/Navegar/imprimir?idNorma=1202434) |
| Chile | RAN Capítulo 20-10 de la CMF | Sistema de gestión de seguridad de la información y ciberseguridad aprobado por el directorio, con gestión de incidentes | — | Informe ejecutivo de postura y cumplimiento para el directorio | [cmfchile.cl](https://www.cmfchile.cl/portal/normativa/624/w4-article-29310.html) |
| Argentina | Comunicaciones BCRA «A» 7724 y «A» 8280 (lineamientos RRCI) | Gestión de riesgos de tecnología y seguridad; clasificación y reporte de ciberincidentes | Notificación inicial en la primera hora y cierre en hasta 5 días corridos («A» 8280) | Detección y triage medidos, playbooks y evidencia por incidente | [bcra.gob.ar](https://www.bcra.gob.ar/archivos/Pdfs/comytexord/A7724.pdf) · [bcra.gob.ar](https://www.bcra.gob.ar/archivos/Pdfs/comytexord/A8280.pdf) |
| Uruguay | Ley 20.212 (arts. 78 a 84) y Decreto 66/025 | Responsable de seguridad, Marco de Ciberseguridad alineado con NIST CSF 2.0 y reporte de incidentes al CERTuy | 24 horas según análisis especializados | Estándar NIST CSF 2.0 asignado, MTTA y evidencia de incidentes | [impo.com.uy](https://www.impo.com.uy/bases/decretos/66-2025/8) |

Referencia, no asesoría legal: resumen de la hoja «Normativa MCSA» del libro de Excel (fuentes públicas al 7 de noviembre de 2026, con su estado de verificación). Las obligaciones, los plazos y su aplicación los define tu área de Legal con el texto oficial vigente. La última columna describe capacidades técnicas que ayudan a documentar controles; no implica cumplimiento.

### Documentación, cursos y credenciales

- [Assign regulatory compliance standards in Microsoft Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/assign-regulatory-compliance-standards) · Documentación · Oficial · Nuevo · Microsoft Learn · 8 ago 2026. Cómo asignar estándares a suscripciones, grupos de administración, cuentas/organizaciones de AWS y proyectos/organizaciones de GCP; requiere cualquier plan de Defender excepto Servers P1 o APIs P1, y rol Owner o Policy Contributor.
- [Regulatory compliance standards in Microsoft Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-regulatory-compliance-standards) · Documentación · Oficial · Nuevo · Microsoft Learn · 17 jun 2026. Lista de estándares disponibles por nube (NIS2, GDPR, NIST CSF 2.0, NIST 800-53 R5.1.1, PCI DSS 4.0.1, ISO 27001:2022, CIS, SOC 2, CSA CCM, DORA, EU AI Act, LGPD, etc.) y estándares por defecto (MCSB; AWS FSBP; GCP Default).
- [Improve regulatory compliance in Microsoft Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/regulatory-compliance-dashboard) · Documentación · Oficial · Microsoft Learn. Panel de cumplimiento: controles automáticos y manuales (atestación con evidencia), pestañas Your Actions y Microsoft Actions, informes y certificados descargables, exportación continua, workflow automation e integración automática con Purview Compliance Manager.
- [Multicloud support in Microsoft Purview Compliance Manager](https://learn.microsoft.com/en-us/purview/compliance-manager-multicloud) · Documentación · Oficial · Microsoft Learn · 26 sep 2025. Compliance Manager usa señales de Defender for Cloud para evaluar Azure, AWS y GCP con pruebas por recurso dentro de evaluaciones y acciones de mejora.
- [Configure cloud settings for use with Microsoft Purview Compliance Manager](https://learn.microsoft.com/en-us/purview/compliance-manager-cloud-settings) · Documentación · Oficial · Microsoft Learn. Pasos para conectar Defender for Cloud con Compliance Manager (suscripción de Azure, planes CSPM y asignación de estándares) y lista de regulaciones soportadas en ambos productos.

### Anuncios y blogs oficiales

- [Microsoft Defender for Cloud Adds Four New Regulatory Frameworks](https://techcommunity.microsoft.com/blog/microsoftdefendercloudblog/microsoft-defender-for-cloud-adds-four-new-regulatory-frameworks/4433440) · Blog oficial · Empleado de Microsoft · Vista previa · Giulio Astori · Microsoft Tech Community – Microsoft Defender for Cloud Blog · 15 jul 2025. Public preview de DORA, EU AI Act, k-ISMS-P y CIS Azure Foundations v3.0 en el panel de cumplimiento para Azure, AWS y GCP. *Nota:* Útil como plantilla para mapear marcos locales de MCSA con estándares personalizados

### Laboratorios, GitHub y herramientas

- [Azure/Microsoft-Defender-for-Cloud - Workflow automation templates](https://github.com/Azure/Microsoft-Defender-for-Cloud/tree/main/Workflow%20automation) · GitHub · Oficial · Equipo de producto de Defender for Cloud · GitHub (Azure). Plantillas de Logic Apps para evidencias y automatización de cumplimiento (Export-ComplianceData, Send-WeeklyComplianceReport, Notify-NewAttackPath, Create-SNOWCRfromASCRec para ServiceNow, Request-ResourceExemption).

### Comunidad: blogs, libros, newsletters y eventos

- [Microsoft Cloud Security Benchmark Guide: v2 Domains, Controls and Framework Mapping](https://nhimg.org/microsoft-cloud-security-benchmark-guide) · Blog · Comunidad · Nuevo · Lalit Choda (editor) · NHI Mgmt Group · 27 oct 2026. Guía independiente del MCSB v2 (12 dominios, nuevo dominio de IA, más de 420 definiciones de Azure Policy, criticidad Must/Should/Nice to have) y advertencias para no confundir mapeos con cumplimiento.

**Manos a la obra**

1. `Laboratorio` Con un plan pago activo y rol Owner o Policy Contributor, asigna PCI DSS v4.0.1 e ISO/IEC 27001:2022 a la suscripción del laboratorio, espera la evaluación (unas 12 horas) y descarga el informe ([asignar estándares](https://learn.microsoft.com/en-us/azure/defender-for-cloud/assign-regulatory-compliance-standards), [panel de cumplimiento](https://learn.microsoft.com/en-us/azure/defender-for-cloud/regulatory-compliance-dashboard)). Evidencia: informe descargado y la lista de controles sin datos por falta de recursos.
2. `Laboratorio` Como Security Admin, crea con la plantilla KQL sobre `RawEntityMetadata` la recomendación «VM sin etiquetas CostCenter u Owner» y, como Owner, agrégala a un estándar personalizado «Línea base MCSA» ([recomendaciones personalizadas](https://learn.microsoft.com/en-us/azure/defender-for-cloud/create-custom-recommendations)). Evidencia: estándar asignado y su resultado tras la siguiente evaluación.
3. `Laboratorio` Atesta un control manual con su evidencia y crea una exención «Risk accepted» con vencimiento a 7 días sobre una recomendación del MCSB; verifica que el recurso pasa a «Not applicable» y que no afecta la puntuación ([panel de cumplimiento](https://learn.microsoft.com/en-us/azure/defender-for-cloud/regulatory-compliance-dashboard), [exenciones](https://learn.microsoft.com/en-us/azure/defender-for-cloud/exempt-resource)). Evidencia: atestación registrada y exención con vencimiento.
4. `Laboratorio` Automatiza la evidencia: exporta de forma continua el cumplimiento regulatorio a Log Analytics y crea una workflow automation con el disparador de evaluación de cumplimiento basada en la plantilla `Send-WeeklyComplianceReport` ([exportación continua](https://learn.microsoft.com/en-us/azure/defender-for-cloud/continuous-export), [plantillas](https://github.com/Azure/Microsoft-Defender-for-Cloud/tree/main/Workflow%20automation)). Evidencia: datos de cumplimiento en el área de trabajo y el primer informe semanal recibido.
5. `Laboratorio parcial` Verifica en Microsoft Purview Compliance Manager del inquilino E5 de prueba que aparecen los datos por recurso de los estándares asignados y compara las versiones de sus plantillas con las de Defender for Cloud ([Compliance Manager multinube](https://learn.microsoft.com/en-us/purview/compliance-manager-multicloud)). Limitación: con pocos recursos muchos controles quedan sin datos y la lista de regulaciones de Compliance Manager muestra versiones antiguas. Evidencia: evaluación con datos de Defender for Cloud y tabla de diferencias de versión.
6. `Laboratorio` Con Legal, mapea una norma financiera de tu país —por ejemplo, la [Circular Externa 007 de 2018 de la SFC](https://www.superfinanciera.gov.co/loader.php?lServicio=Tools2&lTipo=descargas&lFuncion=descargar&idFile=1031904), el [Capítulo 20-10 de la RAN de la CMF](https://www.cmfchile.cl/portal/normativa/624/w4-article-29310.html) o la [Resolución SBS 504-2021](https://intranet2.sbs.gob.pe/dv_int_cn/2046/v4.0/Adjuntos/504-2021.R.pdf)— a controles de ISO/IEC 27001:2022 o NIST CSF 2.0 evaluados en Defender for Cloud y a la evidencia técnica que aporta cada uno. Evidencia: tabla de mapeo revisada por Legal, sin interpretación jurídica propia.
7. `Solo producción` Prepara la evidencia para una auditoría externa ([panel de cumplimiento](https://learn.microsoft.com/en-us/azure/defender-for-cloud/regulatory-compliance-dashboard)). Requiere el estándar asignado sobre recursos reales y auditores con acceso. Cómo hacerlo seguro: asigna Reader a los auditores (Security Reader no ve el cumplimiento), exporta a un área de trabajo dedicada, desactiva cualquier remediación automática en el alcance auditado y registra cada exportación. Evidencia: paquete de evidencia entregado y registro de accesos.

**¿Quieres profundizar?**

- [Azure/Microsoft-Defender-for-Cloud - Workflow automation templates](https://github.com/Azure/Microsoft-Defender-for-Cloud/tree/main/Workflow%20automation) · GitHub

<a id="o4"></a>

## O4 · Mejora continua, gestión de cambios y proyecto integrador

*L300–L400 · ~5 h · Origen: Nuevo en esta edición (base: What's new de Defender for Cloud y sus feeds, guía de transición a recomendaciones individuales y fase Adopt del Cloud Adoption Framework)*

Defender for Cloud cambia cada mes y algunos cambios rompen cosas: las recomendaciones agrupadas se retiraron el 31 de julio de 2026 y dejaron sin datos consultas, tableros y exportaciones; la API bloquea desde el 5 de julio cinco planes en desuso que versiones antiguas de ALZ o EPAC aún referencian; la facturación de Servers cambió el 1 de noviembre (escritorios fuera de P1 y servidores clonados contados por separado). Las fuentes de cambio también cambiaron: la página «Important upcoming changes» redirige a **What's new**, que publica lo próximo y lo retirado con su feed (`aka.ms/mdc/rss`) y otro para recomendaciones y alertas, y el boletín mensual terminó el 3 de agosto de 2026.

La mejora continua es un proceso con dueño: un radar semanal de cambios, un triage que clasifica cada novedad por su impacto en costo, puntuación, automatización y consultas, pruebas en una suscripción piloto con políticas en modo Audit y una revisión trimestral de postura ante el comité. Algunos cambios exigen verificar en lugar de suponer, como el opt-in de Foundational CSPM para suscripciones nuevas «desde el 27 de octubre de 2026», cuya página en inglés se retiró. Microsoft Ignite (17 al 20 de noviembre de 2026) puede cambiar estados de vista previa. El módulo cierra con el proyecto integrador del track, que aplica los tres niveles del programa.

**Por qué importa**

Sin gestión de cambios, un retiro silencioso apaga una automatización o una consulta que alimentaba un KPI y nadie lo nota hasta la auditoría. Un proceso con radar, triage, piloto y comunicación mantiene estable la operación, protege las métricas y convierte cada novedad en una decisión explícita en lugar de una sorpresa.

**Qué vas a lograr**

- Operar un radar de cambios con los feeds oficiales y fuentes comunitarias de alerta temprana.
- Evaluar el impacto de cada cambio en costo, puntuación, automatización y consultas, y probarlo en un piloto.
- Migrar consultas, reglas y exportaciones afectadas por retiros, como el de las recomendaciones agrupadas.
- Conducir una revisión trimestral de postura y entregar el proyecto integrador del track.

> **Atención.** Foundational CSPM opt-in: una página de Learn del 30 de julio de 2026 anunciaba que las suscripciones de Azure nuevas empezarían con Foundational CSPM apagado desde el 27 de octubre de 2026, pero la página en inglés y la entrada de las notas de versión se eliminaron el 30 de septiembre y solo quedan copias traducidas. Estado incierto: verifica en una suscripción nueva y habilítalo de forma explícita en tu proceso de alta ([copia traducida](https://learn.microsoft.com/pl-pl/azure/defender-for-cloud/foundational-cspm-opt-in), [rastreador de cambios](https://daily.defender.admin.news/changes/2026-09-30/foundational-cspm-opt-in-10/)).

> **Qué cambió.** Fuentes de cambio: la URL de «Important upcoming changes» redirige a What's new, que incluye lo próximo y lo retirado y archiva lo anterior a seis meses. El boletín mensual de Defender for Cloud publicó su último número el 3 de agosto de 2026 y el Defender Monthly News oficial no publica desde agosto; un MVP lo continúa como edición comunitaria desde el 22 de octubre ([What's new](https://learn.microsoft.com/en-us/azure/defender-for-cloud/release-notes), [edición comunitaria](https://jeffreyappel.nl/defender-monthly-news-october-2026/)).

> **Atención.** La copia de la iniciativa de Defender for Cloud en Azure-Landing-Zones-Library (v2.4.1) mantiene por defecto subplanes que la API bloquea desde el 5 de julio de 2026 —Resource Manager «PerApiCall» y Key Vault «PerTransaction»—, mientras Enterprise-Scale (v2.4.2) ya los corrigió. Revisa la versión de ALZ o de EPAC en cada ciclo de cambios ([ALZ Library](https://github.com/Azure/Azure-Landing-Zones-Library/blob/main/platform/alz/policy_set_definitions/Deploy-MDFC-Config_20240319.alz_policy_set_definition.json), [Enterprise-Scale](https://github.com/Azure/Enterprise-Scale/blob/main/src/resources/Microsoft.Authorization/policySetDefinitions/Deploy-MDFC-Config_20240319.json)).

> **Consejo Ninja.** Usa rastreadores comunitarios como Daily Defender News (resúmenes generados por IA) solo como alerta temprana y confirma cada cambio en Learn antes de actuar. Después de Microsoft Ignite (17 al 20 de noviembre de 2026), repite el triage: pueden cambiar los estados de DWU, de la gestión de planes, de las políticas de postura y de los agentes ([Daily Defender News](https://daily.defender.admin.news/month/2026-10/), [Microsoft Ignite](https://ignite.microsoft.com/)).

**¿Tienes poco tiempo?**

- [What's new in Defender for Cloud features](https://learn.microsoft.com/en-us/azure/defender-for-cloud/release-notes) · Documentación
- [New and upcoming changes in recommendations, alerts, and incidents](https://learn.microsoft.com/en-us/azure/defender-for-cloud/release-notes-recommendations-alerts) · Documentación
- [Transition from grouped to individual recommendations in Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/transition-grouped-individual-recommendations) · Documentación
- [Defender Monthly News - October 2026 (Community Edition)](https://jeffreyappel.nl/defender-monthly-news-october-2026/) · Blog

**Calendario de mejora continua**

| Cadencia | Actividad | Fuente o herramienta | Entregable | Módulos |
|---|---|---|---|---|
| Semanal | Radar de cambios: What's new y novedades de recomendaciones, alertas e incidentes | Feeds RSS oficiales y blog de Tech Community; rastreadores comunitarios solo como alerta temprana | Registro de cambios clasificado (GA, preview, cambio o retiro) | O4, C3 |
| Semanal | Revisión operativa: alertas ruidosas, supresiones que vencen y salud de conectores | Reglas de supresión, alert tuning y consultas de salud de Sentinel | Decisiones de ajuste con su fuente de verdad | A4, A5 |
| Mensual | Tablero de KPI y costos | Libros de Defender for Cloud, SecurityIncident, Cost Management o Cost & usage | Informe ejecutivo de una página | O2, A8 |
| Mensual | Revisión de exenciones, reglas de gobernanza y recomendaciones vencidas | Informe de gobernanza y lista de exenciones | Exenciones renovadas o cerradas con su aprobador | O1, O3 |
| Trimestral | Revisión de postura ante el comité y actualización de ALZ o EPAC | Fase Adopt del CAF y versiones de la iniciativa de Defender for Cloud | Acta con decisiones, dueños y fechas | O1, O4 |
| Trimestral | Regresión de casos de uso | Alertas de ejemplo, simulador de Kubernetes y prompts benignos | Tiempos por caso y brechas detectadas | A9 |
| Después de cada evento (Ignite, 17 al 20 de noviembre de 2026) | Diferencias de estado entre preview y GA y nuevos precios | What's new y anuncios del evento | Matriz de estados y de precios actualizada | O4, A8 |
| Anual | Renovación del prepago y revisión del modelo de facturación | Plan de prepago y Cloud Security Cost Estimator | Memo de decisión para FinOps | A8 |
| Ante cada retiro anunciado | Plan de migración con fecha límite (por ejemplo, Sentinel fuera del portal de Azure el 31-mar-2027 y las APIs clásicas de Defender for SQL el 16-ago-2027) | What's new y avisos de retiro | Plan con dueño, pruebas y fecha de corte | A4, O4 |

Propuesta del programa basada en [What's new](https://learn.microsoft.com/en-us/azure/defender-for-cloud/release-notes), [novedades de recomendaciones y alertas](https://learn.microsoft.com/en-us/azure/defender-for-cloud/release-notes-recommendations-alerts) y la [fase Adopt del CAF](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/secure/adopt).

### Documentación, cursos y credenciales

- [What's new in Defender for Cloud features](https://learn.microsoft.com/en-us/azure/defender-for-cloud/release-notes) · Documentación · Oficial · Nuevo · Microsoft Learn · 4 nov 2026. Notas de versión mensuales (GA, preview, cambios próximos y retiros) con feed RSS aka.ms/mdc/rss; incluye el GA de la integración en el portal de Defender (5-may-2026) y la gestión de planes con DWU (20-oct-2026).
- [New and upcoming changes in recommendations, alerts, and incidents](https://learn.microsoft.com/en-us/azure/defender-for-cloud/release-notes-recommendations-alerts) · Documentación · Oficial · Nuevo · Microsoft Learn · 31 jul 2026. Registro de recomendaciones, alertas e incidentes nuevos, modificados y retirados (feed aka.ms/mdc/rss-recommendations-alerts), p. ej. el retiro de recomendaciones agrupadas (31-jul-2026).
- [Transition from grouped to individual recommendations in Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/transition-grouped-individual-recommendations) · Documentación · Oficial · Microsoft Learn. Ejemplo de gestión del cambio: las recomendaciones agrupadas se retiraron el 31-jul-2026; explica cómo actualizar consultas ARG, reglas de gobernanza, exenciones y exportación continua por categoría de recomendación.

### Anuncios y blogs oficiales

- [Microsoft Defender for Cloud Blog (Tech Community)](https://techcommunity.microsoft.com/category/microsoft-security/blog/microsoftdefendercloudblog) · Blog oficial · Oficial · Nuevo · Equipo de producto de Defender for Cloud · Microsoft Tech Community · 20 oct 2026. Blog oficial del producto: anuncio de DWU (20-oct-2026), último boletín mensual para clientes (3-ago-2026), integración en el portal de Defender, multinube y seguridad de contenedores.

### Laboratorios, GitHub y herramientas

- [Daily Defender News (tracker de cambios de Microsoft Learn y Message Center)](https://daily.defender.admin.news/month/2026-10/) · Herramienta · Comunidad · Nuevo · Proyecto comunitario (resúmenes generados por IA) · daily.defender.admin.news · oct 2026. Rastreador comunitario que resume diariamente cambios en la documentación de Defender y del Message Center; en oct-2026 destacó la gestión de planes y DWU, el onboarding directo a nivel de inquilino y que los escaneos sin agente suspendidos siguen generando cargos.

### Comunidad: blogs, libros, newsletters y eventos

- [Defender Monthly News - October 2026 (Community Edition)](https://jeffreyappel.nl/defender-monthly-news-october-2026/) · Blog · MVP · Nuevo · Jeffrey Appel · jeffreyappel.nl · 22 oct 2026. Edición comunitaria del resumen mensual de novedades de Defender (incluye Defender for Cloud); explica que el «Microsoft Defender Monthly News» oficial no publica desde la edición de agosto de 2026.

**Manos a la obra**

1. `Laboratorio` Arma tu radar de cambios: agrega a un lector RSS los feeds de What's new (`aka.ms/mdc/rss`), de recomendaciones y alertas (`aka.ms/mdc/rss-recommendations-alerts`) y del blog de Tech Community, y clasifica cada entrada de octubre y noviembre de 2026 como GA, preview, cambio o retiro, con el módulo del programa que afecta ([What's new](https://learn.microsoft.com/en-us/azure/defender-for-cloud/release-notes), [recomendaciones y alertas](https://learn.microsoft.com/en-us/azure/defender-for-cloud/release-notes-recommendations-alerts), [feed del blog](https://techcommunity.microsoft.com/t5/s/gxcuf89792/rss/Category?category.id=microsoft-defender-for-cloud)). Evidencia: registro de cambios con clasificación e impacto.
2. `Laboratorio` Haz el triage de impacto de tres cambios recientes —recomendaciones individuales (31 de julio), planes bloqueados por la API (5 de julio) y facturación de Servers (1 de noviembre)— sobre costo, puntuación, automatizaciones, consultas y exportaciones, y define la acción y el dueño de cada uno ([notas de versión](https://learn.microsoft.com/en-us/azure/defender-for-cloud/release-notes), [transición a recomendaciones individuales](https://learn.microsoft.com/en-us/azure/defender-for-cloud/transition-grouped-individual-recommendations)). Evidencia: matriz de impacto aprobada.
3. `Laboratorio` Comprueba el estado de Foundational CSPM en una suscripción nueva y documenta si arrancó apagado; según el resultado, ajusta tu proceso de alta para habilitarlo de forma explícita ([Foundational y Defender CSPM](https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-cloud-security-posture-management)). Evidencia: captura de Environment settings con la fecha y el cambio en el procedimiento de alta.
4. `Laboratorio parcial` Prueba una actualización de policy-as-code antes de aplicarla: extrae con EPAC las asignaciones de un grupo de administración de pruebas, compara los subplanes por defecto de tu versión de la iniciativa con los planes bloqueados y simula el plan de despliegue ([EPAC](https://azure.github.io/enterprise-azure-policy-as-code/), [asignaciones de Defender for Cloud en EPAC](https://github.com/Azure/enterprise-azure-policy-as-code/blob/main/Docs/settings-dfc-assignments.md)). Limitación: necesitas permisos a nivel de grupo de administración y EPAC aplica estado deseado, así que toma posesión de los recursos de Policy de su alcance: usa `keepDfcSecurityAssignments`, efectos Audit y aprobación manual. Evidencia: plan de despliegue revisado y diferencias documentadas.
5. `Solo producción` Concilia la factura de Defender for Servers de noviembre de 2026 con la de octubre: escritorios fuera de P1, Linux en P1 solo con MDE y máquinas que comparten ID de Arc contadas por separado ([notas de versión](https://learn.microsoft.com/en-us/azure/defender-for-cloud/release-notes)). Requiere datos reales de facturación. Cómo hacerlo seguro: usa los roles Cost Management Reader y Security Reader, inventaría con Azure Resource Graph y documenta las diferencias sin cambiar planes; cualquier ajuste, en una ventana de cambio. Evidencia: conciliación por medidor.
6. `Solo producción` Conduce la revisión trimestral de postura ante el comité: cambios del trimestre, KPI de [O2](#o2), exenciones vencidas, costos y decisiones pendientes, como la migración al modelo DWU ([fase Adopt del CAF](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/secure/adopt)). Requiere varias suscripciones, dueños reales y datos de tendencia. Cómo hacerlo seguro: prepara el análisis con roles de lectura, prueba los cambios en una suscripción piloto con políticas en modo Audit y aplica las reglas de gobernanza con período de gracia. Evidencia: acta con decisiones, dueños y fechas.

<a id="reto-operacion"></a>

## Reto del nivel

**Proyecto integrador: un programa de seguridad en la nube de punta a punta, con evidencia.** Aplica los tres niveles del programa —base, avanzado y experto— a una organización de referencia o a tu propio piloto y demuestra ante el comité, con evidencia verificable, que puedes diseñar, desplegar, operar y optimizar Defender for Cloud. Usa el laboratorio para todo lo que admita práctica y, para lo que exige producción, una suscripción piloto con roles de lectura, modo Audit y aviso al SOC. Formato de cierre: documento de diseño, repositorio con el código y una presentación de diez minutos con un informe ejecutivo de una página.

**Fase 1 · Documento de diseño.** Jerarquía de grupos de administración y landing zones, decisión de portal y de modelo de facturación (el clásico como base y el DWU solo como piloto evaluado con el estimador), residencia de datos para MCSA, RACI y carta del centro de excelencia ([M1](02_Nivel_2_Avanzado.md#m1), [O1](#o1)). Evidencia: documento aprobado por el CISO.

**Fase 2 · Habilitación como código.** Defender for Cloud habilitado con policy-as-code (iniciativa de Azure Landing Zones en su versión corregida o EPAC) y `Microsoft.Security/pricings` en Bicep, conectores de AWS o GCP y estándares regulatorios asignados ([M1](02_Nivel_2_Avanzado.md#m1), [B3](01_Nivel_1_Base.md#b3), [O3](#o3)). Evidencia: pipeline ejecutado y cumplimiento de políticas al 100 % en el piloto.

**Fase 3 · Evidencia de Servers P2 y de IA.** Defender for Endpoint, vulnerabilidades, escaneo sin agente con la cadena de prueba de malware, JIT, FIM y líneas base en dos servidores; AI BOM, recomendaciones de IA cerradas y alertas de Defender for AI Services con contexto de usuario y prompts en español ([B4](01_Nivel_1_Base.md#b4), [M3](02_Nivel_2_Avanzado.md#m3), [M4](02_Nivel_2_Avanzado.md#m4), [A1](03_Nivel_3_Experto.md#a1), [A2](03_Nivel_3_Experto.md#a2)). Evidencia: capturas y exportaciones fechadas.

**Fase 4 · Ajuste de alertas y analítica en Sentinel.** Una sola ruta de ingesta sin duplicados, una sola fuente de verdad de supresión documentada y dos reglas de análisis o detecciones personalizadas como código sobre `CloudAuditEvents` o `SecurityAlert` ([M9](02_Nivel_2_Avanzado.md#m9), [A4](03_Nivel_3_Experto.md#a4), [A7](03_Nivel_3_Experto.md#a7)). Evidencia: consultas de salud y alertas de prueba.

**Fase 5 · Respuesta automatizada.** Un playbook probado de punta a punta —detección, notificación, contención con aprobación humana y cierre—, con su runbook y un simulacro medido ([A3](03_Nivel_3_Experto.md#a3), [A5](03_Nivel_3_Experto.md#a5), [A6](03_Nivel_3_Experto.md#a6)). Evidencia: historial de ejecuciones y acta del simulacro con MTTA y MTTR.

**Fase 6 · KPI, costos y cumplimiento.** Tablero con los KPI del programa (fuente, latencia y meta), informe de costos del modelo clásico con la estimación DWU del Cloud Security Cost Estimator y paquete de evidencia regulatoria revisado por Legal ([O2](#o2), [A8](03_Nivel_3_Experto.md#a8), [O3](#o3)). Evidencia: tablero publicado e informe de costos.

**Fase 7 · Mejora continua.** Registro de cambios del trimestre con su triage, revisión trimestral ante el comité y plan de verificación posterior a Microsoft Ignite ([O4](#o4)). Evidencia: acta con decisiones, dueños y fechas.

<a id="quiz-operacion"></a>

## Evaluación del nivel

Responde y compara con [Evaluaciones y respuestas](06_Evaluaciones_y_respuestas.md#eval-operacion). Con 80 % o más, ¡nivel aprobado! (En la versión web puedes corregir en línea y generar tu certificado).

1. ¿Qué necesitas para usar reglas de gobernanza que asignen dueño y fecha límite a las recomendaciones?
   - a) Solo Foundational CSPM
   - b) Una licencia de Microsoft Sentinel
   - c) Defender CSPM y un rol como Security Admin, Contributor u Owner
   - d) Defender for Servers Plan 1

2. Un usuario es Owner de la suscripción. ¿Ve automáticamente los datos de nube en el portal de Defender con RBAC unificado?
   - a) No: los permisos de Azure no fluyen al RBAC unificado y hay que asignarlos allí
   - b) Sí, se heredan siempre
   - c) Solo si además es Security Reader
   - d) Solo para los recursos de AWS

3. ¿Qué recomienda la metodología Secure del Cloud Adoption Framework sobre las responsabilidades de seguridad?
   - a) Delegar toda la seguridad de la nube en el proveedor
   - b) Centralizar todas las tareas en el SOC
   - c) Asignar todo al equipo de plataforma
   - d) Documentar un modelo de responsabilidad compartida que funcione como matriz RACI

4. ¿Qué afirmación sobre las exenciones de recomendaciones es correcta?
   - a) No tienen límite y aplican a las recomendaciones personalizadas
   - b) Requieren el MCSB asignado, admiten hasta 5.000 recursos exentos por suscripción y pueden tener vencimiento
   - c) Solo se crean por API
   - d) Siempre bajan la puntuación segura

5. ¿Qué requisito tiene el libro Secure Score Over Time?
   - a) Ninguno: muestra el historial desde la creación de la suscripción
   - b) Exportación continua a Log Analytics con streaming e instantáneas semanales
   - c) Una licencia de Power BI Pro
   - d) Microsoft Security Exposure Management con licencia aparte

6. ¿Qué afirmación sobre las dos puntuaciones seguras es correcta?
   - a) Tienen el mismo valor en ambos portales
   - b) La clásica solo existe en el portal de Defender
   - c) La Cloud Secure Score basada en riesgo está solo en el portal de Defender y no es comparable con la clásica del portal de Azure
   - d) Las recomendaciones en preview cuentan en ambas

7. Según el Security Adoption Framework, ¿qué mide el MTTA?
   - a) El tiempo desde que se reconoce un incidente hasta que se corrige
   - b) El tiempo medio entre dos incidentes
   - c) El tiempo desde la detección hasta el cierre administrativo
   - d) El tiempo para reconocer una alerta o un incidente desde que se genera

8. ¿Qué ofrecen las iniciativas de Exposure Management para medir la postura de la nube?
   - a) Puntuación, meta configurable, tendencia de 14 días e historial; las métricas de nube requieren Defender CSPM
   - b) Una puntuación fija que no se puede ajustar
   - c) Solo datos de endpoints
   - d) Una exportación mensual en PDF sin historial

9. ¿Qué estándares se asignan por defecto al conectar una cuenta de AWS?
   - a) Solo el MCSB
   - b) El MCSB y AWS Foundational Security Best Practices
   - c) CIS AWS v3.0.0 y PCI DSS
   - d) Ninguno

10. Un auditor externo necesita leer el panel de cumplimiento regulatorio sin cambiar nada. ¿Qué rol le asignas?
   - a) Security Reader
   - b) Owner
   - c) Policy Contributor
   - d) Reader

11. ¿Qué dice Microsoft Learn sobre el plan necesario para asignar estándares regulatorios adicionales?
   - a) Todas las páginas coinciden en que basta Foundational CSPM
   - b) Solo se habilitan con Defender for Servers Plan 1
   - c) Hay versiones contradictorias (solo Defender CSPM, cualquier plan pago salvo Servers P1 o APIs P1, o al menos un plan pago): verifica en tu inquilino
   - d) Requieren una licencia premium de Purview Compliance Manager

12. No hay un estándar de Defender for Cloud para la regulación financiera de tu país. ¿Qué haces?
   - a) Mapeas, con Legal, la norma a ISO/IEC 27001:2022 o NIST CSF 2.0 y creas un estándar personalizado con recomendaciones KQL
   - b) Asignas LGPD, porque cubre toda la región
   - c) Esperas a que Microsoft publique el estándar
   - d) Usas solo la puntuación segura como evidencia

13. Tras el fin del boletín mensual, ¿cuál es la fuente oficial para seguir los cambios próximos y los retiros de Defender for Cloud?
   - a) La página «Important upcoming changes»
   - b) El Ninja oficial
   - c) What's new, con su feed RSS, que incluye cambios próximos y funciones en desuso
   - d) Azure Status

14. ¿Qué sabes con certeza sobre Foundational CSPM en las suscripciones nuevas «desde el 27 de octubre de 2026»?
   - a) Que se retiró por completo
   - b) Que pasó a ser de pago
   - c) Que solo se habilita desde el portal de Defender
   - d) Nada con certeza: la página en inglés que anunciaba el opt-in se eliminó el 30 de septiembre, así que debes verificarlo en una suscripción nueva

15. Las recomendaciones agrupadas se retiraron el 31 de julio de 2026. ¿Qué acción corresponde?
   - a) Ninguna: los tableros se actualizan solos
   - b) Migrar consultas ARG, reglas de gobernanza, exenciones y exportaciones al modelo individual y convertir las reglas de deshabilitación en exenciones
   - c) Desactivar Defender CSPM
   - d) Volver a la puntuación clásica

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. Los precios son de lista, en USD, cambian con frecuencia y dependen de tu contrato, canal, región y moneda: confírmalos en la página oficial y con tu proveedor antes de presupuestar. El contenido regulatorio es una referencia y no constituye asesoría legal: las decisiones de cumplimiento corresponden a tus áreas de Legal, riesgo y privacidad. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 7 de noviembre de 2026

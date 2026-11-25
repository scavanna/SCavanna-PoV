# Nivel 4 · Operación · Modelo operativo, métricas y gobierno

*Microsoft Purview Insider Risk Management Ninja Training · Edición 2026*

[← Nivel 3 · Avanzado](03_Nivel_3_Avanzado.md) · [Índice del programa](README.md) · [Comunidad →](05_Comunidad.md)

<a id="operacion"></a>

Cómo opera un programa de riesgo interno que trabaja con RR. HH., Legal, privacidad, la representación de los trabajadores y el SOC: responsabilidades, métricas, mejora continua y gobierno en MCSA, sin interpretar la ley.

*L300–L400 · 3 módulos · ~10 horas · 12 recursos*

**Módulos de este nivel:** [O1 Modelo operativo](#o1) · [O2 Métricas y mejora continua](#o2) · [O3 Gobierno, privacidad y MCSA](#o3)

<a id="o1"></a>

## O1 · Modelo operativo del programa de riesgo interno

*L300–L400 · ~3 h · Origen: Nuevo en esta edición (marcos de CISA y de SEI/CERT)*

Un programa de riesgo interno es multidisciplinario por definición. La **Insider Threat Mitigation Guide** de CISA (edición 2026, que incorpora el trabajo híbrido y la IA) lo organiza en detectar, evaluar y gestionar, con un equipo multidisciplinario, gobierno y cultura; la **Common Sense Guide to Mitigating Insider Threats** de SEI/CERT (séptima edición) aporta 22 buenas prácticas basadas en más de 3.000 casos reales, mapeadas a ISO 27002, NIST CSF y el NIST Privacy Framework. Ambas son agnósticas de la herramienta: dan el marco; IRM aporta la ejecución.

En IRM, el modelo operativo se apoya en seis grupos de roles: Insider Risk Management, IRM Admins, IRM Analysts, IRM Investigators, IRM Auditors e IRM Approvers. Solo los Investigators ven las capturas forenses y el explorador de contenido; los Auditors ven y exportan los registros de auditoría; los Approvers aprueban la evidencia forense. Los cambios de permisos tardan hasta 30 minutos, conviene evitar el escenario de «cero administradores» y las unidades administrativas permiten acotar por región o departamento.

Sobre esa base se definen un estatuto del programa, un comité de gobierno (CISO, RR. HH., Legal, privacidad y, cuando corresponda, la representación de los trabajadores), procedimientos operativos, notificaciones a administradores —primera alerta, resumen diario de alertas de severidad alta y resumen semanal de advertencias de políticas— y la capacidad del equipo.

**Por qué importa**

Sin modelo operativo, IRM termina como una herramienta que nadie mira o como un riesgo de vigilancia. Un estatuto con responsabilidades claras acorta los tiempos de cada caso, hace defendibles las decisiones y facilita la conversación con la representación de los trabajadores y con auditoría interna.

**Qué vas a lograr**

- Redactar el estatuto del programa con propósito, alcance, gobierno y límites.
- Construir una matriz RACI por rol y mapearla a los grupos de roles de IRM.
- Configurar grupos de roles con mínimo privilegio, vencimiento y revisión periódica.
- Configurar las notificaciones a administradores y los procedimientos operativos.
- Usar los marcos de CISA y de SEI/CERT como referencia agnóstica.

> **Consejo Ninja.** Para el marco del programa, usa la [Insider Threat Mitigation Guide de CISA](https://www.cisa.gov/resources-tools/resources/insider-threat-mitigation-guide) (edición 2026: detectar, evaluar y gestionar con un equipo multidisciplinario) y la [Common Sense Guide de SEI/CERT](https://www.sei.cmu.edu/library/common-sense-guide-to-mitigating-insider-threats-seventh-edition/) (séptima edición: 22 prácticas mapeadas a ISO 27002, NIST CSF y NIST Privacy Framework, con roles para RR. HH., Legal y Seguridad). Son agnósticas de la herramienta y ayudan a explicar el programa fuera de TI.

> **Atención.** Seis grupos de roles: Insider Risk Management, IRM Admins, IRM Analysts, IRM Investigators, IRM Auditors e IRM Approvers. Solo los Investigators ven las capturas forenses y el explorador de contenido; los Auditors ven y exportan los registros de auditoría; los Approvers aprueban la evidencia forense. Los permisos tardan hasta 30 minutos en aplicarse y conviene evitar el escenario de «cero administradores» ([permisos de IRM](https://learn.microsoft.com/en-us/purview/insider-risk-management-permissions)).

> **Consejo Ninja.** Configura las notificaciones a administradores —primera alerta, resumen diario de alertas de severidad alta y resumen semanal de advertencias de políticas— para que nada dependa de que alguien abra el portal ([ajustes de IRM](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings)). Usa asignaciones con vencimiento para los roles temporales ([What's new](https://learn.microsoft.com/en-us/purview/whats-new)).

**¿Tienes poco tiempo?**

- [Assign permissions in Insider Risk Management](https://learn.microsoft.com/en-us/purview/insider-risk-management-permissions) · Documentación
- [Plan for Insider Risk Management](https://learn.microsoft.com/en-us/purview/insider-risk-management-plan) · Documentación
- [Insider Threat Mitigation Guide (2026 Edition)](https://www.cisa.gov/resources-tools/resources/insider-threat-mitigation-guide) · Documentación

**Grupos de roles de Insider Risk Management y a quién asignarlos**

| Grupo de roles | Qué permite | Asígnalo a | Precaución |
|---|---|---|---|
| Insider Risk Management | Acceso completo a la solución (configuración, alertas, casos e investigación); puede solicitar evidencia forense; acceso de colaborador a Data Security Investigations desde abril de 2026 | Muy pocas personas: líder técnico del programa y acceso de emergencia | Evita usarlo en el día a día; asígnalo con PIM y vencimiento |
| IRM Admins | Configurar ajustes globales y políticas; solicitar evidencia forense | Administradores de Insider Risk | No necesita ver el contenido de los casos |
| IRM Analysts | Clasificar alertas y ver casos, analíticas y plantillas de aviso; ver IRM en Defender XDR | Analistas de triage y analistas del SOC designados | Sin acceso al explorador de contenido ni a capturas forenses |
| IRM Investigators | Lo de Analysts más el explorador de contenido, las capturas forenses y los informes de actividad de usuario | Investigadores asignados a casos | Es el rol más sensible: revisión mensual de accesos y auditoría de sus acciones |
| IRM Auditors | Ver y exportar los registros de auditoría de IRM | Auditoría interna y privacidad | Independiente de quienes investigan |
| IRM Approvers | Aprobar las solicitudes de captura de evidencia forense | Responsable designado por Legal o RR. HH. según el estatuto | Separación de funciones: quien aprueba no solicita |

Fuentes: [permisos de IRM](https://learn.microsoft.com/en-us/purview/insider-risk-management-permissions) · [evidencia forense](https://learn.microsoft.com/en-us/purview/insider-risk-management-forensic-evidence) · [What's new](https://learn.microsoft.com/en-us/purview/whats-new). Los cambios de permisos tardan hasta 30 minutos y las unidades administrativas permiten acotar por región o departamento.

### Documentación, cursos y credenciales

- [Insider Threat Mitigation Guide (2026 Edition)](https://www.cisa.gov/resources-tools/resources/insider-threat-mitigation-guide) · Documentación · Comunidad · Nuevo · CISA · CISA (Cybersecurity and Infrastructure Security Agency) · sep 2026. Guía gubernamental para crear o mejorar un programa de mitigación de amenazas internas (detectar, evaluar, gestionar) con equipo multidisciplinario, gobierno y cultura.
- [Assign permissions in Insider Risk Management](https://learn.microsoft.com/en-us/purview/insider-risk-management-permissions) · Documentación · Oficial · Microsoft Learn. Matriz oficial de los seis grupos de roles de IRM (Insider Risk Management, Admins, Analysts, Investigators, Auditors y Approvers) y uso de unidades administrativas para acotar por región o departamento.
- [Plan for Insider Risk Management](https://learn.microsoft.com/en-us/purview/insider-risk-management-plan) · Documentación · Oficial · Microsoft Learn. Guía de planificación: involucrar a TI, Cumplimiento, Privacidad, Seguridad, RR. HH. y Legal, requisitos regionales, permisos, dependencias y piloto con grupo reducido en producción.

**Manos a la obra**

1. `Laboratorio` Matriz RACI de los siete roles del programa (administrador de Insider Risk, analista o investigador, socio de RR. HH., asesoría legal, oficial de privacidad, analista del SOC y CISO) mapeada a los grupos de roles de IRM y a la tabla de grupos de este módulo ([permisos de IRM](https://learn.microsoft.com/en-us/purview/insider-risk-management-permissions)). Evidencia: RACI con el grupo de roles de cada persona.
2. `Laboratorio` Configura las notificaciones a administradores y verifica en el laboratorio el correo de primera alerta ([ajustes de IRM](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings)). Evidencia: captura del correo y de la configuración.
3. `Laboratorio` Revisión de accesos: con la cuenta de IRM Auditors, exporta la membresía de los grupos de roles y busca en la auditoría los cambios de roles de IRM del último mes ([permisos](https://learn.microsoft.com/en-us/purview/insider-risk-management-permissions); [auditoría](https://learn.microsoft.com/en-us/purview/audit-get-started)). Evidencia: informe de revisión de accesos con hallazgos.
4. `Laboratorio` Escribe y prueba el procedimiento de «cero administradores»: quién tiene el acceso de emergencia, cómo se activa con PIM y cómo se audita ([permisos de IRM](https://learn.microsoft.com/en-us/purview/insider-risk-management-permissions); [permisos del portal de Purview](https://learn.microsoft.com/en-us/purview/purview-permissions)). Evidencia: procedimiento ejecutado en el laboratorio con su registro de auditoría.
5. `Solo producción` Aprobación del estatuto del programa ante el comité (CISO, RR. HH., Legal, privacidad y, cuando corresponda, la representación de los trabajadores) ([guía de CISA](https://www.cisa.gov/resources-tools/resources/insider-threat-mitigation-guide); [planificar IRM](https://learn.microsoft.com/en-us/purview/insider-risk-management-plan)). Cómo hacerlo seguro: ninguna política sobre usuarios reales hasta la aprobación formal; mientras tanto, solo analíticas agregadas y anonimizadas; acta firmada y fecha de revisión anual.

<a id="o2"></a>

## O2 · Métricas, reportes y mejora continua

*L300–L400 · ~3 h · Origen: Nuevo en esta edición*

IRM ofrece cinco informes: Alertas (vista previa), Analíticas, Casos (vista previa), Actividad de usuario y Uso de pago por uso. Sus indicadores incluyen alertas por severidad, alertas atendidas, motivos de descarte, alertas por departamento o país, principales desencadenantes y días promedio en «Needs review»; en casos, los días promedio activos. Todo se exporta a CSV o imagen. El panel de políticas agrega la **eficacia de alertas** —confirmadas sobre confirmadas más descartadas en los últimos 365 días— y el estado de salud de cada política.

La mejora continua se apoya en las **analíticas** (escaneo diario con hasta 10 días de actividad, resultados agregados y anonimizados y recomendaciones de umbrales en tiempo real), en el **ajuste fino** de las detecciones inteligentes —volumen de alertas (Fewer, Default o More), umbral de descargas inusuales y dominios no permitidos o de terceros— y en las exclusiones, que pasaron a «Global exclusions (preview)». En 2026 llegaron el informe de uso de pago por uso (disponibilidad general en marzo) y un panel de recomendaciones que detecta brechas de cobertura de políticas (julio).

**Por qué importa**

Lo que no se mide no se puede ajustar ni defender. Las métricas justifican el presupuesto, muestran proporcionalidad a privacidad y a la representación de los trabajadores (por ejemplo, cuántas alertas se descartan y por qué) y convierten el ajuste en un proceso con hipótesis, cambio, medición y reversión.

**Qué vas a lograr**

- Construir un tablero mensual con los informes de alertas, casos y pago por uso.
- Calcular la eficacia de alertas por política y explicar sus límites.
- Ejecutar un ciclo de ajuste controlado con registro de cambios y reversión.
- Usar las analíticas y el panel de recomendaciones para detectar brechas de cobertura.
- Reportar al comité de gobierno con indicadores de valor, costo y proporcionalidad.

> **Novedad.** El informe de uso de pago por uso está en disponibilidad general desde marzo de 2026 ([What's new](https://learn.microsoft.com/en-us/purview/whats-new)), y el panel de recomendaciones de políticas ([MC1387681](https://m365admin.handsontek.net/microsoft-purview-insider-risk-management-policy-recommendation-panel-irm-2/)) detecta brechas de cobertura —fuga, robo, IA riesgosa, propiedad intelectual y violaciones de seguridad— a partir de las analíticas: vista previa a mediados de junio y disponibilidad general a mediados de julio de 2026, habilitado por defecto.

> **Consejo Ninja.** La eficacia de alertas del panel de políticas es confirmadas / (confirmadas + descartadas) en los últimos 365 días ([políticas](https://learn.microsoft.com/es-es/purview/insider-risk-management-policies)). Los informes de Alertas y Casos están en vista previa y muestran alertas atendidas, motivos de descarte, alertas por departamento o país, principales desencadenantes y días promedio en «Needs review» ([informes](https://learn.microsoft.com/en-us/purview/insider-risk-management-reports)).

> **Atención.** Ajustar el volumen de alertas tiene costo: «Fewer alerts» puede ocultar verdaderos positivos y «More alerts» sube los falsos positivos; registra cada cambio y mide su efecto en los informes. Las exclusiones globales salieron de las detecciones inteligentes y ahora están en «Global exclusions (preview)» ([detecciones inteligentes](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-intelligent-detections)).

**¿Tienes poco tiempo?**

- [Use reports in Insider Risk Management](https://learn.microsoft.com/en-us/purview/insider-risk-management-reports) · Documentación
- [Enable analytics in Insider Risk Management](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-analytics) · Documentación
- [Configure intelligent detections in Insider Risk Management](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-intelligent-detections) · Documentación
- [Create and manage Insider Risk Management policies](https://learn.microsoft.com/en-us/purview/insider-risk-management-policies) · Documentación

### Documentación, cursos y credenciales

- [Use reports in Insider Risk Management](https://learn.microsoft.com/en-us/purview/insider-risk-management-reports) · Documentación · Oficial · Nuevo · Microsoft Learn · 26 jun 2026. Describe los informes de IRM (alertas y casos, analíticas, actividad de usuario y uso de pago por uso) con indicadores como alertas atendidas, motivos de descarte y días promedio en revisión, exportables a CSV.
- [Enable analytics in Insider Risk Management](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-analytics) · Documentación · Oficial · Microsoft Learn. Explica cómo activar las analíticas de IRM para estimar riesgos sin crear políticas, con resultados agregados y anonimizados, y recibir recomendaciones de umbrales en tiempo real.
- [Common Sense Guide to Mitigating Insider Threats, Seventh Edition](https://www.sei.cmu.edu/library/common-sense-guide-to-mitigating-insider-threats-seventh-edition/) · Documentación · Comunidad · Legado aún útil · CERT National Insider Threat Center · Carnegie Mellon University - Software Engineering Institute (CERT) · 7 sep 2022. 22 buenas prácticas basadas en más de 3.000 casos reales, mapeadas a ISO 27002, NIST CSF y NIST Privacy Framework, con roles para RR. HH., Legal y Seguridad. *Nota:* Edición 2022 aún vigente como referencia agnóstica de herramientas; incluye la práctica 22 "aprender de incidentes pasados" útil para métricas y mejora continua
- [Microsoft Purview | Insider Risk Management: Policy recommendation panel in IRM (MC1387681)](https://m365admin.handsontek.net/microsoft-purview-insider-risk-management-policy-recommendation-panel-irm-2/) · Documentación · Oficial · Nuevo · M365 Admin (HANDS ON tek, archivo de Message Center) · 14 jun 2026. Aviso de un panel de recomendaciones que detecta brechas de cobertura de políticas (fuga, robo, IA riesgosa, PI, violaciones de seguridad) usando analíticas.
- [Configure intelligent detections in Insider Risk Management](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-intelligent-detections) · Documentación · Oficial · Microsoft Learn. Muestra cómo ajustar el volumen de alertas (menos, predeterminado o más), el umbral de descargas inusuales, la importación de alertas de Defender for Endpoint por estado y los dominios no permitidos o de terceros.

**Manos a la obra**

1. `Laboratorio` Exporta a CSV los informes de alertas y casos y arma un tablero mensual con el KPI de días en «Needs review», la eficacia por política y los motivos de descarte ([informes](https://learn.microsoft.com/en-us/purview/insider-risk-management-reports); [políticas](https://learn.microsoft.com/es-es/purview/insider-risk-management-policies)). Evidencia: tablero en Excel o Power BI con una página de lectura para el comité.
2. `Laboratorio` Revisa el informe de uso de pago por uso y crea un presupuesto de Azure con alertas; calcula el costo por política del piloto ([informes](https://learn.microsoft.com/en-us/purview/insider-risk-management-reports); [Usage center](https://learn.microsoft.com/en-us/purview/purview-billing-usage)). Evidencia: tabla de costo por política y alerta de presupuesto configurada.
3. `Laboratorio` Revisa el panel de recomendaciones de políticas y registra cada brecha de cobertura detectada, con la decisión tomada y su dueño ([MC1387681](https://m365admin.handsontek.net/microsoft-purview-insider-risk-management-policy-recommendation-panel-irm-2/)). Evidencia: registro de decisiones.
4. `Laboratorio` Compara las analíticas antes y después de un cambio de configuración (por ejemplo, un indicador nuevo) usando el escaneo diario y sus recomendaciones de umbrales ([analíticas](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-analytics)). Evidencia: dos capturas fechadas y una conclusión.
5. `Solo producción` Ajuste con volumen real: hacen falta unos 30 días de actividad real para medir falsos positivos ([detecciones inteligentes](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-intelligent-detections)). Cómo hacerlo seguro: copia la política, cambia umbrales o variantes en la copia acotada a un piloto, compara en el mismo período la eficacia de alertas y los motivos de descarte, y revierte si empeora; registra cada cambio en el control de cambios ([políticas](https://learn.microsoft.com/es-es/purview/insider-risk-management-policies); [informes](https://learn.microsoft.com/en-us/purview/insider-risk-management-reports)).

<a id="o3"></a>

## O3 · Gobierno, privacidad y cumplimiento normativo en MCSA

*L300–L400 · ~4 h · Origen: Nuevo en esta edición*

La legitimidad del programa depende de su gobierno. Microsoft deja explícito que el cliente es el único responsable de usar IRM conforme a la ley aplicable, y la privacidad por diseño de la herramienta tiene bordes que hay que conocer: la seudonimización **no** se conserva fuera de IRM —Acceso condicional, alertas DLP y el explorador de actividad muestran nombres reales—, la exportación por API o a eDiscovery tampoco la conserva (la exportación a CSV sí) y el panel del Triage Agent muestra nombres. Todo eso debe constar en la evaluación de impacto de privacidad.

En MCSA, la normativa de protección de datos se está renovando: la **Ley 21.719** de Chile entra en vigencia el 1 de diciembre de 2026 y crea la Agencia de Protección de Datos Personales; México publicó una nueva **LFPDPPP** en el DOF el 20 de marzo de 2025; y la Red Iberoamericana de Protección de Datos aprobó en mayo de 2026 sus **Estándares Iberoamericanos**, un marco orientador común. La hoja «Normativa MCSA» del libro de Excel resume 45 normas de la región. Este módulo no interpreta la ley: te ayuda a preparar las preguntas y la evidencia para Legal, privacidad, RR. HH. y, cuando un contrato colectivo o la ley lo exijan, la representación de los trabajadores.

El monitoreo de empleados reales requiere aprobaciones previas, seudonimización activa y políticas de prueba acotadas; la tabla [Gobierno, privacidad y proceso de casos](00_Programa.md#gobierno-casos) resume cada etapa con sus participantes, sus controles y la evidencia que conviene conservar.

**Por qué importa**

Un programa de riesgo interno impugnado por la representación de los trabajadores o por una autoridad de datos puede suspenderse y arrastrar consigo la confianza en todo el plan de seguridad. Documentar finalidad, proporcionalidad, minimización, accesos y retención protege a la organización y a las personas, y acelera las aprobaciones.

**Qué vas a lograr**

- Preparar los insumos de la evaluación de impacto de privacidad para IRM.
- Identificar dónde se pierde la seudonimización y qué controles lo compensan.
- Configurar y revisar la auditoría de las acciones de los investigadores.
- Mapear con Legal la normativa regional aplicable, sin interpretarla.
- Definir con RR. HH. la comunicación a los empleados y los avisos.

> **Atención.** La seudonimización no se conserva fuera de IRM: Acceso condicional, alertas DLP y el explorador de actividad muestran nombres reales ([Protección adaptativa](https://learn.microsoft.com/en-us/purview/insider-risk-management-adaptive-protection)); la exportación por API y a eDiscovery tampoco la conserva, mientras que la exportación a CSV sí; y el panel del Triage Agent no anonimiza los nombres en las alertas priorizadas ([privacidad de nombres de usuario](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-privacy)). Inclúyelo en la evaluación de impacto de privacidad.

> **Novedad.** Normativa en movimiento en la región: la [Ley 21.719 de Chile](https://www.bcn.cl/leychile/navegar?i=1209272&f=2026-12-01) entra en vigencia el 1 de diciembre de 2026 y crea la Agencia de Protección de Datos Personales; la nueva [LFPDPPP de México](https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPDPPP.pdf?web=1) se publicó en el DOF el 20 de marzo de 2025 (última reforma, 14 de noviembre de 2025); y la RIPD aprobó el 26 de mayo de 2026 los [Estándares Iberoamericanos](https://www.redipd.org/documento/estandares-iberoamericanos-2026.pdf). La hoja «Normativa MCSA» del libro de Excel resume 45 normas de la región. Nada de esto es asesoría legal: valídalo con Legal y con tu oficial de protección de datos.

> **Consejo Ninja.** Cuando la normativa local lo exija, usa políticas idénticas separadas por región e investigadores que hablen el idioma de los usuarios ([planificar IRM](https://learn.microsoft.com/es-es/purview/insider-risk-management-plan)); el portal de la [RIPD](https://www.redipd.org/) ayuda a ubicar la autoridad y la normativa de cada país. Cuando un contrato colectivo o la ley lo exijan, involucra a la representación de los trabajadores antes del piloto, no después.

**¿Tienes poco tiempo?**

- [Manage username privacy in Insider Risk Management](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-privacy) · Documentación
- [Plan for Insider Risk Management](https://learn.microsoft.com/en-us/purview/insider-risk-management-plan) · Documentación
- [Ley 21.719 - Regula la protección y el tratamiento de los datos personales y crea la Agencia de Protección de Datos Personales (Chile)](https://www.bcn.cl/leychile/navegar?i=1209272&f=2026-12-01) · Documentación
- [Estándares de Protección de Datos de los Estados Iberoamericanos (RIPD, 2026)](https://www.redipd.org/documento/estandares-iberoamericanos-2026.pdf) · Documentación

### Documentación, cursos y credenciales

- [Ley Federal de Protección de Datos Personales en Posesión de los Particulares (México, nueva ley 2025)](https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPDPPP.pdf?web=1) · Documentación · Comunidad · ES · Congreso de la Unión · Cámara de Diputados (México) · 14 nov 2025. Texto vigente de la nueva LFPDPPP publicada en el DOF el 20-mar-2025 (última reforma 14-nov-2025), con aviso de privacidad, consentimiento y derechos ARCO aplicables a datos de empleados.
- [Ley 21.719 - Regula la protección y el tratamiento de los datos personales y crea la Agencia de Protección de Datos Personales (Chile)](https://www.bcn.cl/leychile/navegar?i=1209272&f=2026-12-01) · Documentación · Comunidad · ES · Congreso Nacional de Chile · Biblioteca del Congreso Nacional de Chile · 13 dic 2024. Texto oficial de la nueva ley chilena de datos personales que crea la Agencia de Protección de Datos y exige modelos de cumplimiento, relevante para monitoreo de empleados.
- [Estándares de Protección de Datos de los Estados Iberoamericanos (RIPD, 2026)](https://www.redipd.org/documento/estandares-iberoamericanos-2026.pdf) · Documentación · Comunidad · Nuevo · ES · RIPD · Red Iberoamericana de Protección de Datos (RIPD) · 26 may 2026. Estándares regionales de principios y derechos de protección de datos aprobados en Cartagena de Indias, referencia común para programas de riesgo interno en MCSA.

### Laboratorios, GitHub y herramientas

- [Red Iberoamericana de Protección de Datos (portal)](https://www.redipd.org/) · Herramienta · Comunidad · Nuevo · ES · RIPD · 4 nov 2026. Portal de la RIPD con legislación por país, guías (IA, nube, biometría) y noticias de autoridades de protección de datos iberoamericanas.

**Manos a la obra**

1. `Laboratorio` Paquete de evidencia de privacidad del laboratorio: capturas de la seudonimización activa, de los grupos de roles con vencimiento y una búsqueda de auditoría de las acciones de un investigador (quién vio qué y cuándo) ([privacidad](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-privacy); [auditoría](https://learn.microsoft.com/en-us/purview/audit-get-started)). Evidencia: paquete fechado y firmado por el responsable del laboratorio.
2. `Laboratorio` Hoja de insumos para la evaluación de impacto de privacidad: finalidad, categorías de datos (indicadores activados), destinatarios (SOC, RR. HH., Legal), retenciones (clips forenses, 120 días; preservación de DLM, 120 días) y puntos donde se pierde la seudonimización ([Protección adaptativa](https://learn.microsoft.com/en-us/purview/insider-risk-management-adaptive-protection); [evidencia forense](https://learn.microsoft.com/en-us/purview/insider-risk-management-forensic-evidence); [compartir datos](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-share-data)). Evidencia: hoja revisada por el oficial de privacidad.
3. `Laboratorio` Mapa regional: a partir de la hoja «Normativa MCSA», lista las normas de los países donde opera tu organización y redacta preguntas para Legal, sin interpretarlas, por ejemplo sobre aviso a los empleados, transferencias y derechos de los titulares ([Ley 21.719](https://www.bcn.cl/leychile/navegar?i=1209272&f=2026-12-01); [LFPDPPP](https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPDPPP.pdf?web=1); [Estándares Iberoamericanos](https://www.redipd.org/documento/estandares-iberoamericanos-2026.pdf)). Otros ejemplos de la hoja: la [Ley 1581 de Colombia](http://www.secretariasenado.gov.co/senado/basedoc/ley_1581_2012.html), el [reglamento de la Ley 29733 de Perú](https://cdn.www.gob.pe/uploads/document/file/7756037/6554453-reglamento-de-la-ley-n-29733.pdf?v=1741726731) y la [Ley 25.326 de Argentina](https://www.argentina.gob.ar/normativa/nacional/norma-64790/actualizacion). Evidencia: cuestionario enviado a Legal.
4. `Laboratorio` Borrador de comunicación a empleados con RR. HH.: qué se monitorea, para qué, con qué salvaguardas (seudonimización, roles, auditoría) y a quién consultar, coherente con la cláusula de responsabilidad del cliente ([Get started](https://learn.microsoft.com/en-us/purview/insider-risk-management-configure)). Evidencia: borrador para revisión de RR. HH. y Legal (no es un documento legal).
5. `Solo producción` Aprobación y comunicación del programa: presenta el estatuto, la evaluación de impacto y la comunicación a Legal, RR. HH., privacidad y, cuando corresponda, la representación de los trabajadores ([planificar IRM](https://learn.microsoft.com/es-es/purview/insider-risk-management-plan); [Get started](https://learn.microsoft.com/en-us/purview/insider-risk-management-configure)). Cómo hacerlo seguro: aprobación documentada antes de cualquier política sobre usuarios reales; mientras tanto, solo analíticas agregadas y anonimizadas; revisión anual del programa.

**¿Quieres profundizar?**

- [Red Iberoamericana de Protección de Datos (portal)](https://www.redipd.org/) · Herramienta

<a id="reto-operacion"></a>

## Reto del nivel

**Estatuto del programa ante el comité.** Presenta, como si fuera ante el comité de riesgos, el estatuto del programa de riesgo interno: propósito, alcance, RACI de los siete roles, mapa de grupos de roles, tabla de gobierno y proceso de casos, tablero mensual (eficacia de alertas, días en «Needs review», costo por política), insumos de la evaluación de impacto de privacidad y preguntas para Legal sobre la normativa de tus países en MCSA (sin interpretarla), con un plan de consulta a la representación de los trabajadores cuando corresponda. Formato: diez minutos de exposición y una página de resumen ejecutivo.

<a id="quiz-operacion"></a>

## Evaluación del nivel

Responde y compara con [Evaluaciones y respuestas](06_Evaluaciones_y_respuestas.md#eval-operacion). Con 80 % o más, ¡nivel aprobado! (En la versión web puedes corregir en línea y generar tu certificado).

1. ¿Qué grupo de roles puede ver las capturas de evidencia forense y el explorador de contenido?
   - a) IRM Analysts
   - b) IRM Auditors
   - c) IRM Investigators
   - d) IRM Admins

2. ¿Quién aprueba la captura de evidencia forense de un usuario?
   - a) El grupo IRM Approvers
   - b) El administrador global
   - c) El propio usuario
   - d) El grupo IRM Analysts

3. ¿Qué notificaciones a administradores ofrece IRM?
   - a) Solo un resumen mensual de alertas, enviado por correo al administrador global del tenant
   - b) Avisos por SMS al usuario investigado y a su gerente directo cuando se abre un caso
   - c) Ninguna: el equipo debe revisar el portal de Purview cada día para ver alertas nuevas
   - d) Primera alerta, resumen diario de alertas altas y resumen semanal de advertencias de políticas

4. ¿Qué marco agnóstico de la herramienta organiza un programa de riesgo interno en detectar, evaluar y gestionar, con una edición de 2026?
   - a) La Insider Threat Mitigation Guide de CISA
   - b) La guía de estudio de SC-401
   - c) La descripción del servicio de Purview
   - d) El Ninja oficial de IRM

5. ¿Cómo calcula el panel de políticas la eficacia de las alertas?
   - a) Alertas activas / alertas totales generadas en los últimos 30 días
   - b) Alertas confirmadas / (confirmadas + descartadas) en los últimos 365 días
   - c) Casos cerrados / casos abiertos durante el último trimestre
   - d) Alertas de severidad alta / alertas de severidad baja del año

6. ¿Cómo funcionan las analíticas de IRM?
   - a) Requieren crear al menos tres políticas activas antes de ejecutar el primer escaneo
   - b) Muestran en tiempo real los nombres de los usuarios más riesgosos de la organización
   - c) Escanean a diario hasta 10 días de actividad y entregan resultados agregados y anonimizados
   - d) Solo funcionan con pago por uso y una suscripción de Azure vinculada al tenant

7. ¿Qué riesgo tiene elegir «Fewer alerts» en las detecciones inteligentes?
   - a) Que aumenten los falsos positivos
   - b) Que se desactive la seudonimización
   - c) Que se borren las alertas existentes
   - d) Que se oculten verdaderos positivos

8. ¿Qué indicador de los informes de IRM mide de forma directa la agilidad del triage?
   - a) Días promedio en «Needs review»
   - b) Número de políticas por plantilla
   - c) Capacidad usada de evidencia forense
   - d) Cantidad de indicadores activados

9. ¿En cuál de estos casos se conserva la seudonimización de IRM?
   - a) En las alertas DLP generadas por la Protección adaptativa
   - b) En la exportación a CSV
   - c) En la exportación por la Office 365 Management Activity API
   - d) En el panel del Triage Agent

10. Según el texto de LeyChile citado en este programa, ¿desde cuándo rige la Ley 21.719 de Chile?
   - a) 1 de enero de 2025
   - b) 20 de marzo de 2025
   - c) 1 de diciembre de 2026
   - d) 26 de mayo de 2026

11. Si la normativa local lo exige, ¿qué recomienda la guía de planificación de IRM?
   - a) Desactivar IRM en ese país hasta que la autoridad local apruebe expresamente su uso
   - b) Usar una única política global sin segmentación, para tratar a todos los usuarios igual
   - c) Reemplazar la seudonimización por cifrado de los nombres de usuario en esa región
   - d) Usar políticas idénticas separadas por región e investigadores que hablen el idioma de los usuarios

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. No constituye asesoría legal ni laboral: usar Insider Risk Management sobre personas reales exige la evaluación previa de tus áreas de Legal, RR. HH. y privacidad y, cuando corresponda, de la representación de los trabajadores. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

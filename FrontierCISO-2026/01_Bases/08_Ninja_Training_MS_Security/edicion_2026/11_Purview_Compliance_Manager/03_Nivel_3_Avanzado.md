# Nivel 3 · Avanzado · Automatizar, mapear y sostener

*Microsoft Purview Compliance Manager Ninja Training · Edición 2026*

[← Nivel 2 · Intermedio](02_Nivel_2_Intermedio.md) · [Índice del programa](README.md) · [Nivel 4 · Operación →](04_Nivel_4_Operacion.md)

<a id="avanzado"></a>

Automatización con exportaciones y cargas masivas (y los límites reales de las APIs), mapeo de controles entre marcos, un programa de cumplimiento continuo y la normativa de privacidad, ciberseguridad y sector financiero de MCSA. Terminas con un mapa de controles y un calendario anual de cumplimiento.

*L400 · 4 módulos · ~17 horas · 40 recursos*

**Módulos de este nivel:** [A1 Automatización y APIs](#a1) · [A2 Mapeo de controles](#a2) · [A3 Cumplimiento continuo](#a3) · [A4 Normativa regional](#a4)

<a id="a1"></a>

## A1 · Automatización y APIs: lo que se puede y lo que no

*L400 · ~3 h · Origen: Ninja oficial de 2023, nivel Advanced (Configuration Analyzer y escenarios avanzados), reorientado a la automatización actual*

Empieza por la verdad incómoda: las **APIs de Purview en Microsoft Graph** (protectionScopes, processContent, contentActivities y las de etiquetas de confidencialidad) sirven para que tus aplicaciones envíen contenido a Purview y apliquen sus políticas, y la documentación aclara que **no hay APIs para extraer datos ni analíticas de Purview**. Tampoco hay un cmdlet documentado para la puntuación de Compliance Manager: la comunidad lo pregunta desde 2021 y la respuesta sigue siendo exportar. Antes de construir un conector propio o raspar el portal, asume este límite.

Dentro de ese límite se puede automatizar bastante. El ciclo **exportar–actualizar–cargar** de acciones de mejora en Excel se estandariza con versiones y aprobaciones; las **alertas** llegan por correo y pueden entrar al flujo de tareas del equipo; y para la infraestructura, **Defender for Cloud** exporta de forma continua el cumplimiento normativo, secure score y recomendaciones a Log Analytics o Event Hubs, en streaming o con instantáneas semanales. Con esas piezas se arma un tablero sostenible. Microsoft Ignite (17 al 20 de noviembre de 2026) podría cambiar este panorama: verifica antes de invertir.

**Por qué importa**

Los equipos pierden semanas buscando una API que no existe o construyen extracciones frágiles que se rompen con cada cambio del portal. Conocer los límites permite diseñar una automatización sostenible y fijar expectativas realistas con la dirección y con auditoría.

**Qué vas a lograr**

- Explicar qué APIs de Purview existen y por qué no extraen datos de Compliance Manager.
- Estandarizar el ciclo exportar–actualizar–cargar con control de versiones.
- Configurar la exportación continua de Defender for Cloud para el cumplimiento de infraestructura.
- Integrar las alertas por correo en la gestión de tareas del equipo.

> **Atención.** Las APIs de Purview en Microsoft Graph sirven para **enviar** contenido y aplicar políticas en tus aplicaciones; la documentación indica que no hay APIs para extraer datos ni analíticas de Purview ([tutorial](https://learn.microsoft.com/en-us/purview/developer/use-the-api), [visión general](https://learn.microsoft.com/en-us/purview/developer/microsoft-purview-sdk-documentation-overview)). La automatización de Compliance Manager se apoya en exportaciones a Excel y cargas masivas ([actualizar acciones](https://learn.microsoft.com/en-us/purview/compliance-manager-update-actions)).

> **Qué cambió.** La pregunta es antigua: en 2021 la comunidad de Fabric confirmó que no había extracción automática de la puntuación hacia Power BI ([hilo de 2021](https://community.fabric.microsoft.com/t5/Power-Query/Compliance-Secure-Score-Data-Exportation/m-p/1902080)) y en noviembre de 2024 un hilo de Microsoft Q&A seguía sin una API ni un cmdlet específicos ([Q&A](https://learn.microsoft.com/en-gb/answers/questions/2081811/what-api-or-powershell-cmdlet-can-be-used-to-colle)). Al 6 de noviembre de 2026 no hay cambios documentados; revisa de nuevo después de Ignite.

> **Consejo Ninja.** Para la infraestructura sí hay automatización nativa: Defender for Cloud exporta de forma continua el cumplimiento normativo, secure score y recomendaciones a Log Analytics o Event Hubs, en streaming o con instantáneas semanales ([exportación continua](https://learn.microsoft.com/en-us/azure/defender-for-cloud/benefits-of-continuous-export)). Desde Log Analytics, esos datos pueden llegar a Sentinel y a tus tableros.

> **Consejo Ninja.** Un patrón de tablero de cumplimiento en Power BI (resumen ejecutivo, controles, excepciones y tendencias) puede alimentarse con las exportaciones de Compliance Manager; no es específico del producto, pero sirve como diseño de partida ([patrón de tablero](https://github.com/judeper/FSI-AgentGov-Solutions/blob/main/compliance-dashboard/docs/power-bi-setup.md)).

**¿Tienes poco tiempo?**

- [Tutorial - Use Microsoft Purview APIs to leverage your policies in your apps](https://learn.microsoft.com/en-us/purview/developer/use-the-api) · Documentación
- [Update improvement actions and bring compliance data into Microsoft Purview Compliance Manager](https://learn.microsoft.com/en-us/purview/compliance-manager-update-actions) · Documentación
- [Export alerts and recommendations with continuous export (Microsoft Defender for Cloud)](https://learn.microsoft.com/en-us/azure/defender-for-cloud/benefits-of-continuous-export) · Documentación

### Documentación, cursos y credenciales

- [Overview of Microsoft Purview APIs (Microsoft Graph)](https://learn.microsoft.com/en-us/purview/developer/microsoft-purview-sdk-documentation-overview) · Documentación · Oficial · Microsoft Learn. Panorama de las APIs de Purview en Microsoft Graph (protectionScopes, processContent, contentActivities, sensitivityLabels) para integrar políticas en aplicaciones.
- [Tutorial - Use Microsoft Purview APIs to leverage your policies in your apps](https://learn.microsoft.com/en-us/purview/developer/use-the-api) · Documentación · Oficial · Microsoft Learn. Tutorial de integración de apps con las APIs de Purview, con la nota explícita de que no existen APIs para extraer datos o analítica de Purview.

### Comunidad: blogs, libros, newsletters y eventos

- [Compliance Secure Score Data Exportation (Fabric Community)](https://community.fabric.microsoft.com/t5/Power-Query/Compliance-Secure-Score-Data-Exportation/m-p/1902080) · Blog · Comunidad · Legado aún útil · v-yingjl (Community Support) · Microsoft Fabric Community · 23 jun 2021. Hilo que confirma que no había forma automática de extraer la puntuación de cumplimiento hacia Power BI y propone exportar o incrustar el panel. *Nota:* Respuesta de 2021; sigue sin documentarse una API pública de Compliance Manager (verificar en Ignite 2026)

**Manos a la obra**

1. `Laboratorio` Lee el [tutorial de APIs de Purview](https://learn.microsoft.com/en-us/purview/developer/use-the-api) y la [visión general de las APIs](https://learn.microsoft.com/en-us/purview/developer/microsoft-purview-sdk-documentation-overview) y documenta en una tabla qué hace cada endpoint (protectionScopes, processContent, contentActivities y etiquetas) y por qué ninguno devuelve la puntuación ni las evaluaciones.
2. `Laboratorio` Estandariza el ciclo mensual exportar–actualizar–cargar: exporta las acciones a Excel, guarda el archivo con fecha y responsable en un repositorio con versiones, aplica los cambios con revisión de una segunda persona y vuelve a cargarlo ([actualizar acciones](https://learn.microsoft.com/en-us/purview/compliance-manager-update-actions)). Evidencia: procedimiento y dos versiones del archivo.
3. `Laboratorio parcial` Configura la exportación continua de Defender for Cloud del cumplimiento normativo y el secure score a un workspace de Log Analytics y consulta los datos exportados ([exportación continua](https://learn.microsoft.com/en-us/azure/defender-for-cloud/benefits-of-continuous-export)). Limitación: requiere la suscripción de laboratorio con Defender for Cloud y genera costo de ingesta.
4. `Laboratorio` Crea una política de alertas de Compliance Manager con un buzón compartido del equipo como destinatario y define cómo se convierte cada alerta en tarea: ticket, responsable y plazo ([alertas](https://learn.microsoft.com/en-us/purview/compliance-manager-alert-policies)).
5. `Laboratorio` Construye un modelo de Power BI que lea las exportaciones mensuales de evaluaciones y muestre la tendencia por evaluación y por dueño, usando como guía de diseño el [patrón de tablero de cumplimiento](https://github.com/judeper/FSI-AgentGov-Solutions/blob/main/compliance-dashboard/docs/power-bi-setup.md).
6. `Solo producción` Integra los datos de cumplimiento de infraestructura con el SIEM. Motivo: requiere suscripciones y volumen reales. Cómo hacerlo seguro: exportación continua a un workspace dedicado, solo los tipos de datos necesarios, presupuesto con alertas y acceso de solo lectura para el equipo de GRC.

<a id="a2"></a>

## A2 · Mapeo de controles entre marcos: ISO 27001, NIST, normas locales e IA

*L400 · ~4 h · Origen: Nuevo en esta edición*

Compliance Manager mapea por diseño: las acciones de mejora se comparten entre las evaluaciones de un mismo grupo, así que implementar una acción técnica satisface requisitos de varias regulaciones a la vez. Esa es la base para mapear ISO/IEC 27001 con NIST CSF y con las normas locales. Un insumo adicional es la **preparación previa al despliegue** (*Sub-service compliance readiness*, vista previa): para un servicio de Azure muestra su aporte a ISO 27001, NIST 800-53 r4, PCI DSS v4.0 y SOC 2, con una pestaña de controles relacionados entre marcos y exportación en CSV o JSON, sin consumir licencias ni crear evaluaciones.

La región ya trabaja así: el Banco Central del Uruguay publicó una guía que mapea sus estándares mínimos de gestión al Marco de Ciberseguridad de AGESIC, basado en NIST CSF, ISO 27001 y COBIT, con un modelo de madurez. Este módulo te propone un mapa por dominios —gobierno, acceso, datos, monitoreo, incidentes, terceros y nube, continuidad, retención e IA— que conecta cada marco con la evidencia de Compliance Manager. El mapa es una herramienta de trabajo, no una opinión jurídica: las equivalencias con normas locales las valida Legal.

**Por qué importa**

Un banco de la región responde a la vez a la ley de datos, a la norma de ciberseguridad del supervisor, a ISO 27001, a PCI y a los requisitos de sus clientes. Sin mapa, cada auditoría pide la misma evidencia otra vez. Un mapa mantenido reduce el esfuerzo de prueba y muestra al comité dónde una inversión cubre varias obligaciones.

**Qué vas a lograr**

- Usar los grupos de evaluaciones para que una acción cubra varias regulaciones.
- Construir un mapa por dominios entre ISO/IEC 27001:2022, NIST CSF 2.0 y una norma local.
- Usar los controles relacionados de la preparación previa al despliegue como insumo.
- Documentar supuestos y revisiones del mapa con Legal y auditoría interna.

> **Consejo Ninja.** Las acciones de mejora se comparten entre las evaluaciones de un mismo grupo: implementar una acción técnica satisface requisitos de varias regulaciones a la vez, y esa es la base del mapeo entre ISO 27001, NIST CSF y las normas locales ([evaluaciones](https://learn.microsoft.com/en-us/purview/compliance-manager-assessments)).

> **Novedad.** La preparación previa al despliegue (vista previa, página actualizada el 26 de septiembre de 2025) analiza servicios de Azure frente a ISO 27001, NIST 800-53 r4, PCI DSS v4.0 y SOC 2 antes de desplegarlos; su pestaña *Related controls* muestra controles equivalentes entre regulaciones y exporta en CSV o JSON, sin consumir licencias ni crear evaluaciones ([preparación previa](https://learn.microsoft.com/en-us/purview/compliance-manager-predeployment-compliance)).

> **Atención.** Planifica los grupos antes de mapear: una evaluación no se puede cambiar de grupo una vez asignada y las acciones no técnicas solo se comparten dentro del grupo ([evaluaciones](https://learn.microsoft.com/en-us/purview/compliance-manager-assessments)). En Defender for Cloud, los estándares se configuran en el portal de Azure y el libro de cumplimiento en el tiempo muestra tendencias ([estándares](https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-regulatory-compliance-standards)).

> **Consejo Ninja.** Ejemplos regionales: la guía del BCU mapea sus estándares mínimos de gestión al Marco de Ciberseguridad de AGESIC, basado en NIST CSF, ISO 27001 y COBIT, con un modelo de madurez ([guía del BCU](https://www.bcu.gub.uy/Comunicados/seggco21196_Anexo.pdf)), y el Decreto 66/025 obliga a sectores críticos a adoptar ese Marco, alineado con NIST CSF 2.0 ([Decreto 66/025](https://www.impo.com.uy/bases/decretos/66-2025/8)). Para ISO 27001, un análisis comunitario mapea cláusulas y controles del Anexo A a soluciones de Purview ([SGSI](https://informasjonsbeskyttelse.no/en/how-purview-supports-an-isms)).

**¿Tienes poco tiempo?**

- [Assess predeployment compliance with Compliance Manager (preview)](https://learn.microsoft.com/en-us/purview/compliance-manager-predeployment-compliance) · Documentación
- [How Purview supports an ISMS](https://informasjonsbeskyttelse.no/en/how-purview-supports-an-isms) · Blog
- [Regulatory compliance standards in Microsoft Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-regulatory-compliance-standards) · Documentación
- [BCU – Guía de los Estándares Mínimos de Gestión relativos a Seguridad de la Información](https://www.bcu.gub.uy/Comunicados/seggco21196_Anexo.pdf) · Documentación

**Mapa de controles por dominio (punto de partida, no opinión jurídica)**

| Dominio | ISO/IEC 27001:2022 | NIST CSF 2.0 | Normas locales de ejemplo | Evidencia en Compliance Manager y Purview |
|---|---|---|---|---|
| Gobierno y supervisión | Cláusulas 5 y 9.1 a 9.3; controles 5.1, 5.35 y 5.36 | GV.RR, GV.PO, GV.OV | RAN 20-10 (rol del directorio), BCRA «A» 7724 (gobierno de TI), CONASSIF 5-24, SFC CE 007 (política y unidad responsable) | Evaluaciones con dueños, informes exportados y actas del comité |
| Identidad y control de acceso | 5.15 a 5.18, 8.2 y 8.5 | PR.AA | SBS 504-2021 (gestión de identidades), Res. AAIP 47/2018 (control de acceso), normas de la Superintendencia de Bancos de Ecuador | Acciones técnicas probadas por Secure Score; PIM y roles (programa de Entra) |
| Clasificación y protección de datos | 5.12, 5.13, 5.34, 8.12 y 8.24 | PR.DS | LFPDPPP 2025 (medidas de seguridad), Ley 21.719 (deber de seguridad), Ley 29733 y su reglamento, CONASSIF 5-24 (clasificación de activos) | Acciones probadas por la integración con Purview (programas de Information Protection y DLP) |
| Registro, monitoreo y vulnerabilidades | 8.8, 8.15 y 8.16 | DE.CM, ID.RA | Res. AAIP 47/2018 (vulnerabilidades), normas de la Superintendencia de Bancos de Ecuador (auditorías periódicas) | Auditoría de Purview con retención definida (programa de eDiscovery y Audit) y recomendaciones de Defender for Cloud |
| Gestión y notificación de incidentes | 5.24 a 5.28 y 6.8 | RS.MA, RS.CO | Decreto 295 de Chile, BCRA «A» 8280, concepto de la SIC sobre la Ley 1581, Decreto 64/020 de Uruguay, SBS 504-2021 | Procedimiento y simulacros adjuntos como evidencia; prueba manual de auditoría interna |
| Terceros y nube | 5.19 a 5.23 | GV.SC | RAN 20-7 (externalización), SFC CE 005 de 2019 (nube), BCU 2026/009 (tercerización), CNBS 025/2022, CONASSIF 5-24 | Evaluación multinube con Defender for Cloud e informes del Service Trust Portal para los controles de Microsoft |
| Continuidad y respaldo | 5.29, 5.30, 8.13 y 8.14 | PR.IR, RC.RP | JM-104-2021 de Guatemala, Acuerdo 3-2012 de Panamá, CD-SIBOIF-500-1 de Nicaragua, Res. AAIP 47/2018 (respaldo) | Acciones manuales con evidencia de pruebas de continuidad y restauración |
| Retención y eliminación | 5.33 y 8.10 | PR.DS | Leyes de datos de la región (conservación limitada); plazos a validar con Legal | Acciones probadas por la integración con Purview (programa de ciclo de vida y registros) |
| IA responsable | Fuera del Anexo A: usa ISO/IEC 42001 e ISO/IEC 23894 | GV y NIST AI RMF | Ley 31814 de Perú y su reglamento (DS 115-2025-PCM), BCRA «A» 7724 (incluye inteligencia artificial) | Evaluación con plantilla de IA y evidencias de DSPM para IA |

Mapa construido para esta guía a partir de las acciones compartidas por grupo ([evaluaciones](https://learn.microsoft.com/en-us/purview/compliance-manager-assessments)), la [preparación previa al despliegue](https://learn.microsoft.com/en-us/purview/compliance-manager-predeployment-compliance), el [mapeo de un SGSI a Purview](https://informasjonsbeskyttelse.no/en/how-purview-supports-an-isms), la [guía del BCU](https://www.bcu.gub.uy/Comunicados/seggco21196_Anexo.pdf) y la hoja «Normativa MCSA». Las referencias a ISO/IEC 27001:2022 y NIST CSF 2.0 son orientativas: valida cada equivalencia con auditoría interna y las de normas locales con Legal.

### Documentación, cursos y credenciales

- [Regulatory compliance standards in Microsoft Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-regulatory-compliance-standards) · Documentación · Oficial · Microsoft Learn. Conceptos de estándares, controles y evaluaciones en Defender for Cloud, con libro de 'cumplimiento en el tiempo', consultas personalizadas y descarga de informes de auditoría.
- [BCU – Guía de los Estándares Mínimos de Gestión relativos a Seguridad de la Información](https://www.bcu.gub.uy/Comunicados/seggco21196_Anexo.pdf) · Documentación · Comunidad · ES · BCU · Banco Central del Uruguay. Guía que mapea los EMG del BCU al Marco de Ciberseguridad de AGESIC (basado en NIST CSF, ISO 27001 y COBIT) con modelo de madurez.
- [Assess predeployment compliance with Compliance Manager (preview)](https://learn.microsoft.com/en-us/purview/compliance-manager-predeployment-compliance) · Documentación · Oficial · Vista previa · Microsoft Learn · 26 sep 2025. Grupo 'Sub-service compliance readiness' para analizar antes de desplegar servicios de Azure su aporte a ISO 27001, NIST 800-53 r4, PCI DSS v4.0 y SOC 2, con controles relacionados entre marcos y exportación CSV/JSON. *Nota:* No consume licencias ni crea evaluaciones; la pestaña 'Related controls' muestra controles equivalentes entre regulaciones (útil para mapeo)

### Comunidad: blogs, libros, newsletters y eventos

- [How Purview supports an ISMS](https://informasjonsbeskyttelse.no/en/how-purview-supports-an-isms) · Blog · MVP · Nuevo · Roy Allan Hansen · informasjonsbeskyttelse.no · 22 oct 2026. Mapeo de cláusulas y controles del Anexo A de ISO/IEC 27001:2022 a soluciones de Purview, con Compliance Manager como soporte de la cláusula 9.1 y del control 5.36.

**Manos a la obra**

1. `Laboratorio` Crea en el mismo grupo dos evaluaciones con las plantillas que activaste en [I2](01_Nivel_1_Inicial.md#i2) (por ejemplo, ISO 27001 y NIST CSF 2.0, o ISO 27001 y GDPR) y verifica qué acciones compartidas suman a ambas ([evaluaciones](https://learn.microsoft.com/en-us/purview/compliance-manager-assessments)). Evidencia: lista de acciones compartidas con sus puntos en cada evaluación.
2. `Laboratorio` En la preparación previa al despliegue, elige un servicio de Azure, abre la pestaña de controles relacionados y exporta en CSV los equivalentes entre ISO 27001 y PCI DSS v4.0 ([preparación previa](https://learn.microsoft.com/en-us/purview/compliance-manager-predeployment-compliance)).
3. `Laboratorio` Completa la tabla de mapeo de este módulo para tu organización con al menos ocho dominios y una norma local (por ejemplo, la RAN 20-10, la Resolución SBS 504-2021 o la Circular Externa 007 de la SFC) y marca qué acción de Compliance Manager evidencia cada fila.
4. `Laboratorio` Compara la [guía de estándares mínimos del BCU](https://www.bcu.gub.uy/Comunicados/seggco21196_Anexo.pdf) con tu mapa y anota cómo resuelve las equivalencias y la madurez; adopta lo que te sirva, por ejemplo un nivel de madurez por dominio.
5. `Solo producción` Mapea la RAN 20-10 de la CMF, la Circular Externa 007 de la SFC o la Resolución SBS 504-2021 contra ISO 27001 en la evaluación real del banco. Motivo: requiere licencias premium y evidencias reales. Cómo hacerlo seguro: grupo de evaluaciones separado, roles de solo lectura para los revisores y sin aceptar actualizaciones de plantilla a mitad de un ciclo de auditoría ([RAN 20-10](https://www.cmfchile.cl/portal/normativa/624/w4-article-29310.html)).

<a id="a3"></a>

## A3 · Programa de cumplimiento continuo

*L400 · ~4 h · Origen: Ninja oficial de 2023, nivel Intermediate (actualizaciones de plantillas), ampliado a un programa continuo*

Cumplir una vez al año para la auditoría ya no alcanza. Un programa continuo combina cuatro mecanismos de Compliance Manager: **alertas** por cambios de puntuación, asignaciones, estado de implementación, estado de prueba y evidencias (todas las organizaciones tienen una política predeterminada de cambio de puntuación); **actualizaciones de plantillas** que aparecen como *Pending update* y cuya aceptación es permanente y por grupo; **exportaciones** periódicas como instantáneas, y la **carga masiva** para sostener ciclos de revisión. Para la infraestructura se suma la exportación continua de Defender for Cloud.

Los supervisores de la región van en la misma dirección: el Banco Central del Uruguay pide autoevaluaciones con evidencia referenciada que valida, observa o rechaza, y en 2026 empezó a recibir reportes periódicos de capacidades de ciberseguridad. Este módulo convierte esos mecanismos en un calendario con dueños y evidencias —la tabla [Programa de cumplimiento continuo](00_Programa.md#cumplimiento-continuo)— que incluye simulacros de notificación de incidentes, porque plazos como la primera hora del BCRA o las tres horas de la alerta temprana chilena no se cumplen improvisando.

**Por qué importa**

Un programa continuo evita la carrera de último minuto antes de cada auditoría, detecta retrocesos apenas ocurren —una caída de puntos tras un cambio de configuración— y mantiene las evidencias vigentes. También responde a la supervisión basada en evidencia y madurez que ya aplican reguladores de la región.

**Qué vas a lograr**

- Configurar políticas de alertas por tipo de evento, severidad y destinatarios.
- Gestionar actualizaciones pendientes de plantillas sin romper un ciclo de auditoría.
- Operar un calendario de actividades con responsables y evidencias.
- Preparar autoevaluaciones periódicas con evidencia referenciada.

> **Consejo Ninja.** Las políticas de alertas cubren cinco eventos: cambio de puntuación, de asignación, de estado de implementación, de estado de prueba y de evidencia. La política predeterminada de cambio de puntuación agrupa las coincidencias de 60 minutos en una sola alerta de severidad media y notifica por defecto al Global Admin: agrégale destinatarios. Una política nueva o editada puede tardar hasta 24 horas en generar alertas ([alertas](https://learn.microsoft.com/en-us/purview/compliance-manager-alert-policies)).

> **Atención.** Para ver las páginas Policies y Alerts se necesita el rol Security reader de Entra ID; para crear o editar políticas, Compliance Administrator, Compliance Data Administrator, Security Administrator o Security Operator, además de un rol de Compliance Manager distinto de Reader ([alertas](https://learn.microsoft.com/en-us/purview/compliance-manager-alert-policies)).

> **Atención.** Las actualizaciones de plantillas aparecen como *Pending update*; aceptarlas es permanente y se aplica por grupo. Si hay una auditoría en curso, difiérelas y exporta el informe antes y después de aceptarlas ([evaluaciones](https://learn.microsoft.com/en-us/purview/compliance-manager-assessments)).

> **Novedad.** Los supervisores piden evidencia periódica: el BCU publicó en abril de 2026 su procedimiento de envío, validación y revisión de evidencias del Marco de Ciberseguridad ([nota metodológica V2](https://www.bcu.gub.uy/Comunicados/Anexo%201%20-%20Nota%20metodologica%20V2.pdf)) y en junio de 2026 inició el reporte periódico de capacidades de ciberseguridad, empezando por los emisores de dinero electrónico ([anuncio del BCU](https://www.bcu.gub.uy/Comunicaciones/Paginas/Detalle-Noticia.aspx?noticia=518&title=El-BCU-avanza-en-la-implementaci%C3%B3n-de-nuevos-est%C3%A1ndares-de-ciberseguridad-para-la-industria-financiera-)).

**¿Tienes poco tiempo?**

- [Microsoft Purview Compliance Manager alerts and alert policies](https://learn.microsoft.com/en-us/purview/compliance-manager-alert-policies) · Documentación
- [Update improvement actions and bring compliance data into Microsoft Purview Compliance Manager](https://learn.microsoft.com/en-us/purview/compliance-manager-update-actions) · Documentación
- [Procedimiento de Envío, Validación y Revisión de Evidencias – Marco de Ciberseguridad (BCU, Nota metodológica V2)](https://www.bcu.gub.uy/Comunicados/Anexo%201%20-%20Nota%20metodologica%20V2.pdf) · Documentación

### Documentación, cursos y credenciales

- [Update improvement actions and bring compliance data into Microsoft Purview Compliance Manager](https://learn.microsoft.com/en-us/purview/compliance-manager-update-actions) · Documentación · Oficial · Microsoft Learn. Procedimiento para exportar acciones de mejora a Excel, actualizarlas en bloque (estado, pruebas, evidencias, responsables) y volver a cargarlas, útil para migrar trabajo previo y sostener ciclos de revisión periódicos.
- [Microsoft Purview Compliance Manager alerts and alert policies](https://learn.microsoft.com/en-us/purview/compliance-manager-alert-policies) · Documentación · Oficial · Microsoft Learn. Configuración de políticas de alerta por cambios de puntuación o asignaciones de acciones, con notificación por correo y política predeterminada de cambio de puntuación.
- [Export alerts and recommendations with continuous export (Microsoft Defender for Cloud)](https://learn.microsoft.com/en-us/azure/defender-for-cloud/benefits-of-continuous-export) · Documentación · Oficial · Microsoft Learn. Describe cómo Defender for Cloud exporta de forma continua recomendaciones, secure score y datos de cumplimiento regulatorio a Log Analytics o Event Hubs para monitoreo y tableros de cumplimiento continuo.
- [Procedimiento de Envío, Validación y Revisión de Evidencias – Marco de Ciberseguridad (BCU, Nota metodológica V2)](https://www.bcu.gub.uy/Comunicados/Anexo%201%20-%20Nota%20metodologica%20V2.pdf) · Documentación · Comunidad · ES · BCU · Banco Central del Uruguay · 30 abr 2026. Procedimiento del BCU para que las instituciones envíen autoevaluaciones del Marco de Ciberseguridad con evidencias referenciadas que el supervisor valida, observa o rechaza.

**Manos a la obra**

1. `Laboratorio` Agrega destinatarios a la política predeterminada de cambio de puntuación y crea una política nueva para cambios de evidencia y de estado de prueba con severidad alta; provoca un cambio y verifica la alerta y el correo (una política nueva puede tardar hasta 24 horas en generar alertas) ([alertas](https://learn.microsoft.com/en-us/purview/compliance-manager-alert-policies)).
2. `Laboratorio parcial` Ensaya la gestión de una actualización pendiente: exporta el informe, registra la decisión (aceptar o diferir) con su justificación y, si aceptas, exporta de nuevo y compara puntuación y acciones ([evaluaciones](https://learn.microsoft.com/en-us/purview/compliance-manager-assessments)). Limitación: depende de que Microsoft publique una actualización de alguna de tus plantillas durante la prueba.
3. `Laboratorio` Arma el calendario anual a partir de la tabla [Programa de cumplimiento continuo](00_Programa.md#cumplimiento-continuo), con frecuencias, responsables por puesto y evidencias, y cárgalo como tareas en la herramienta de trabajo del equipo.
4. `Laboratorio` Prepara una autoevaluación tipo supervisor: para diez controles, referencia la evidencia (documento, fecha, ubicación y responsable) siguiendo la [nota metodológica del BCU](https://www.bcu.gub.uy/Comunicados/Anexo%201%20-%20Nota%20metodologica%20V2.pdf).
5. `Solo producción` Opera el programa con responsables reales y evidencias de auditoría. Motivo: requiere datos, dueños de controles y auditores reales. Cómo hacerlo seguro: grupo piloto, auditores con rol Reader por evaluación, exportación de una instantánea antes de aceptar actualizaciones y actualizaciones diferidas durante las auditorías ([evaluaciones](https://learn.microsoft.com/en-us/purview/compliance-manager-assessments)).
6. `Solo producción` Haz un simulacro de notificación (por ejemplo, la alerta temprana de tres horas del [Decreto 295](https://www.leychile.cl/leychile/Navegar/imprimir?idNorma=1211466) o la notificación inicial en la primera hora de la [Comunicación «A» 8280](https://www.bcra.gob.ar/archivos/Pdfs/comytexord/A8280.pdf)) con el SOC, Legal y comunicaciones. Motivo: requiere a las personas y los procesos reales. Cómo hacerlo seguro: escenario ficticio anunciado, nada se envía al regulador, tiempos medidos y lecciones registradas como acciones de mejora.

<a id="a4"></a>

## A4 · Normativa de la región: privacidad, ciberseguridad y sector financiero

*L400 · ~6 h · Origen: Nuevo en esta edición*

MCSA vive una ola regulatoria. En privacidad, México publicó una nueva LFPDPPP el 20 de marzo de 2025, Chile aplica la Ley 21.719 desde el 1 de diciembre de 2026, Perú tiene un nuevo reglamento de la Ley 29733 desde el 31 de marzo de 2025, Ecuador emitió en 2026 una norma técnica de notificación de vulneraciones y Paraguay promulgó la Ley 7593/2025, con plena vigencia prevista para fines de noviembre de 2027. Guatemala, Honduras, Venezuela y Bolivia siguen sin ley general de datos personales.

En ciberseguridad y sector financiero los plazos son cortos: el BCRA exige la notificación inicial de un ciberincidente importante dentro de la primera hora y Chile, una alerta temprana en tres horas; casi todos los supervisores financieros de la región —de la CNBV en México y el CONASSIF en Costa Rica a la SFC en Colombia, la SBS en Perú o el BCU en Uruguay— tienen normas de seguridad de la información, y Ecuador y Guatemala aprobaron leyes de ciberseguridad en 2026. Este módulo usa la hoja **Normativa MCSA** del libro de Excel (45 normas de 16 países) como referencia, no como asesoría legal: la aplicabilidad la decide tu área de Legal, junto con privacidad.

**Por qué importa**

Antes de elegir plantillas y cupos hay que saber qué normas aplican y cuáles tienen plantilla. Los plazos de notificación, de una hora a varios días, condicionan los procesos del SOC, de Legal y de comunicaciones. Hacerlo sabiendo que las plantillas son escasas o están desactualizadas evita una falsa sensación de cumplimiento.

**Qué vas a lograr**

- Inventariar las normas de privacidad, ciberseguridad y sector financiero aplicables, con su fuente oficial.
- Distinguir plazos confirmados en texto oficial de los que provienen de análisis secundarios.
- Elegir para cada norma el enfoque en Compliance Manager: plantilla premium, copia extendida o plantilla desde PDF.
- Preparar el insumo para que Legal y privacidad validen la aplicabilidad.

> **Atención.** Esta sección es referencia, no asesoría legal. La aplicabilidad de cada norma depende de tu actividad, de tus licencias y de tu supervisor: decídela con Legal y privacidad. El detalle de 45 normas de 16 países, con fuente oficial y estado de verificación, está en la hoja «Normativa MCSA» del libro de Excel; el enfoque recomendado en Compliance Manager, en [Plantillas para MCSA](00_Programa.md#plantillas-mcsa).

> **Novedad.** Argentina: la Comunicación «A» 8280 del BCRA (17 de julio de 2025) actualizó los lineamientos de respuesta y recuperación ante ciberincidentes: notificación inicial de incidentes importantes y críticos dentro de la primera hora, actualizaciones hasta su resolución y reporte de cierre en un máximo de cinco días corridos; los proveedores de servicios de pago del registro (excepto PSPCP) tienen 60 días hábiles para implementarlo ([A 8280](https://www.bcra.gob.ar/archivos/Pdfs/comytexord/A8280.pdf)).

> **Novedad.** Chile: el Decreto 295, publicado el 1 de marzo de 2025, fija una alerta temprana en tres horas y un segundo reporte en 72 horas (24 horas si un operador de importancia vital ve afectado un servicio esencial) ([Decreto 295](https://www.leychile.cl/leychile/Navegar/imprimir?idNorma=1211466)). La Ley 21.719, vigente desde el 1 de diciembre de 2026, exige reportar vulneraciones a la Agencia «sin dilaciones indebidas» (art. 14 sexies) y no fija horas, aunque una firma cita 72 ([Ley 21.719](https://www.leychile.cl/leychile/Navegar?idNorma=1209272&idParte=1)).

> **Atención.** Plazos sin confirmar en texto oficial a la fecha de corte: Perú, 48 horas a la ANPD (según firmas); Costa Rica, cinco días hábiles al titular (art. 38 del reglamento); México, aviso inmediato a la CNBV; Uruguay, 24 horas al CERTuy; Ecuador, 72 horas en la ley de ciberseguridad; y Guatemala, 3, 6 y 72 horas (ley aprobada, pendiente de publicación). Trátalos como hipótesis de trabajo hasta que Legal los confirme.

**¿Tienes poco tiempo?**

- [Comunicación “A” 8280 – Actualización de los Lineamientos para la respuesta y recuperación ante ciberincidentes (RRCI), BCRA](https://www.bcra.gob.ar/archivos/Pdfs/comytexord/A8280.pdf) · Documentación
- [Decreto 295 – Aprueba reglamento de reporte de incidentes de ciberseguridad de la Ley 21.663 (Chile)](https://www.leychile.cl/leychile/Navegar/imprimir?idNorma=1211466) · Documentación
- [Ley Federal de Protección de Datos Personales en Posesión de los Particulares (México, 2025)](https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPDPPP.pdf) · Documentación
- [Ley 21.719 – Regula la protección y el tratamiento de los datos personales (Chile, versión vigente desde 01-12-2026)](https://www.bcn.cl/leychile/navegar?i=1209272&f=2026-12-01) · Documentación

**Plazos de notificación de incidentes y vulneraciones en MCSA (referencia, no asesoría legal)**

| País | Norma | A quién se notifica | Plazo | ¿Confirmado en texto oficial? | Fuente |
|---|---|---|---|---|---|
| Argentina | Comunicación BCRA «A» 8280 (RRCI) | BCRA | Inicial: dentro de la primera hora; cierre: hasta 5 días corridos | Sí | [BCRA · A 8280](https://www.bcra.gob.ar/archivos/Pdfs/comytexord/A8280.pdf) |
| Argentina | Ley 25.326 y Res. AAIP 47/2018 | — | Sin plazo legal específico; la AAIP recomienda gestionar y documentar los incidentes | Sí | [Ley 25.326](https://www.argentina.gob.ar/normativa/nacional/norma-64790/actualizacion) |
| Chile | Decreto 295 (Ley 21.663) | CSIRT Nacional (ANCI) | Alerta temprana: 3 h; segundo reporte: 72 h (24 h si un operador de importancia vital ve afectado un servicio esencial) | Sí | [Decreto 295](https://www.leychile.cl/leychile/Navegar/imprimir?idNorma=1211466) |
| Chile | Ley 21.719 (vigente desde el 1 de diciembre de 2026) | Agencia de Protección de Datos Personales | Sin dilaciones indebidas (art. 14 sexies); la ley no fija horas | Sí; una firma cita 72 h sin respaldo en el texto | [Ley 21.719](https://www.leychile.cl/leychile/Navegar?idNorma=1209272&idParte=1) |
| Colombia | Ley 1581 de 2012 (concepto de la SIC) | SIC, mediante el RNBD o su aplicativo | 15 días hábiles desde la detección | Concepto oficial de la SIC | [SIC](https://sedeelectronica.sic.gov.co/publicaciones/boletin-juridico/concepto/cumplimiento-de-la-obligacion-del-reporte-de-incidentes-de-seguridad) |
| Costa Rica | Reglamento de la Ley 8968 (Decreto 37554-JP, art. 38) | Titular | 5 días hábiles | No: confirmar en el texto consolidado | [Reglamento](http://pgrweb.go.cr/TextoCompleto/NORMAS/1/VIGENTE/D/2010-2019/2010-2014/2012/12270/74352_115361-3.html) |
| Ecuador | LOPDP y norma técnica de notificación de la SPDP (2026) | SPDP y ARCOTEL; titulares si hay riesgo | 5 días a la autoridad; 3 días a los titulares; el encargado avisa al responsable en 2 días | Parcial: guía oficial de EcuCERT sobre el art. 43 | [EcuCERT](https://www.ecucert.gob.ec/que-medidas-deben-tomar-los-prestadores-de-servicios-de-telecomunicaciones-para-gestionar-una-vulneracion-de-la-seguridad-de-datos-personales/) |
| Ecuador | Ley Orgánica para el Fortalecimiento de la Ciberseguridad (vigente desde el 22 de mayo de 2026) | Ente rector y CSIRT Nacional | 72 h según análisis de firmas; formatos por normativa secundaria | No | [Registro Oficial](https://www.asambleanacional.gob.ec/es/system/files/ro_29.pdf) |
| El Salvador | Ley para la Protección de Datos Personales (Decreto Legislativo 144, art. 25) | Agencia de Ciberseguridad del Estado, Fiscalía General y titulares | 72 h desde que se conoce la vulneración | Sí | [Decreto 144](https://www.asamblea.gob.sv/sites/default/files/documents/decretos/F6986BF6-25C7-428B-9B74-325A6760AC2C.pdf) |
| El Salvador | NRP-23 (seguridad de la información en entidades financieras) | Alta gerencia y Superintendencia | Al conocerse un incidente materializado (art. 13, según resumen especializado) | No | [NRP-23](https://www.bcr.gob.sv/regulaciones/upload/NRP-23.pdf) |
| Guatemala | Ley Marco de Ciberseguridad (Decreto 26-2026) | Estructura estatal de ciberseguridad | 3 h si afecta infraestructura crítica, 6 h en otros casos e informe completo en 72 h, según prensa | No: aprobada el 3 de noviembre de 2026, pendiente de publicación | [Diario de Centro América](https://dca.gob.gt/noticias-guatemala-diario-centro-america/nueva-ley-blinda-el-ciberespacio-de-guatemala/) |
| México | LFPDPPP de 2025 (art. 19) | Titular | Inmediato cuando la vulneración afecte de forma significativa sus derechos patrimoniales o morales | Sí | [LFPDPPP](https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPDPPP.pdf) |
| México | Disposiciones de la CNBV para instituciones de crédito (arts. 168 Bis) | CNBV | Aviso inmediato, según análisis secundarios | No: confirmar en los artículos vigentes | [CNBV](https://www.cnbv.gob.mx/Normatividad/Disposiciones%20de%20car%C3%A1cter%20general%20aplicables%20a%20las%20instituciones%20de%20cr%C3%A9dito.pdf) |
| Panamá | Ley 81 de 2019 y Decreto Ejecutivo 285 de 2021 | ANTAI y titulares | 72 h desde que se conoce el incidente | Parcial: verificar el artículo del decreto | [Decreto 285](https://antai.gob.pa/wp-content/uploads/2021/05/Reglamentacio%CC%81n-de-Ley-81-de-Proteccio%CC%81n-de-Datos-Personales.pdf) |
| Paraguay | Ley 7593/2025 (plena vigencia prevista a fines de noviembre de 2027) | Autoridad de control y, en su caso, el titular | 72 h | Sí | [Ley 7593/2025](https://www.bacn.gov.py/leyes-paraguayas/12924/ley-n-75932025--de-proteccin-de-datos-personales-en-la-repblica-del-paraguay) |
| Perú | Ley 29733 y nuevo reglamento (DS 016-2024-JUS) | ANPD | 48 h para incidentes con grandes volúmenes de datos o grave perjuicio, según firmas | No: confirmar | [Reglamento](https://cdn.www.gob.pe/uploads/document/file/7756037/6554453-reglamento-de-la-ley-n-29733.pdf?v=1741726731) |
| Perú | Confianza digital (DS 126-2025-PCM, según el diario oficial) | Centro Nacional de Seguridad Digital | 48 h para incidentes digitales críticos | No: verificar en el decreto | [El Peruano](https://elperuano.pe/noticia/292188-incidente-de-seguridad-digital-o-de-datos-personales) |
| Uruguay | Decreto 64/020 (art. 4) | URCDP y titulares si la afectación es significativa | 72 h desde que se conoce la vulneración | Sí | [Decreto 64/020](https://www.impo.com.uy/bases/decretos/64-2020/4) |
| Uruguay | Ley 20.212 y Decreto 66/025 (art. 8) | CERTuy | 24 h según análisis especializados; el CERTuy fija los plazos | No | [Decreto 66/025](https://www.impo.com.uy/bases/decretos/66-2025/8) |
| Uruguay | Comunicación BCU 2024/018 | BCU | Inicial en 4 h, seguimiento cada 48 h y cierre en 15 días corridos (instituciones del sistema de pagos, según la investigación) | Verificar el alcance por tipo de institución | [BCU 2024/018](https://www.bcu.gub.uy/Comunicados/seggco24018.pdf) |

Referencia, no asesoría legal: confirma cada plazo con Legal antes de fijarlo en un procedimiento. El detalle de las 45 normas está en la hoja «Normativa MCSA» del libro de Excel.

### Documentación, cursos y credenciales

- [Ley Orgánica para el Fortalecimiento de la Ciberseguridad (Registro Oficial, Quinto Suplemento) – Ecuador](https://www.asambleanacional.gob.ec/es/system/files/ro_29.pdf) · Documentación · Comunidad · Nuevo · ES · Asamblea Nacional del Ecuador · may 2026. Primera ley de ciberseguridad de Ecuador: obligaciones de gestión y notificación de incidentes para entidades públicas, infraestructura crítica y prestadores de servicios digitales, con coordinación permanente con el CSIRT Nacional.
- [CNBV – Normatividad Banca Múltiple (Disposiciones de carácter general aplicables a las instituciones de crédito)](https://www.cnbv.gob.mx/SECTORES-SUPERVISADOS/BANCA-MULTIPLE/Paginas/Normatividad.aspx) · Documentación · Comunidad · ES · CNBV · Comisión Nacional Bancaria y de Valores. Página oficial de la CNBV con la Circular Única de Bancos, cuya sección 'De la seguridad de la información' (arts. 168 Bis 11 a 168 Bis 17) exige un CISO y reporte de incidentes.
- [Ley 7593/2025 de Protección de Datos Personales en la República del Paraguay](https://www.bacn.gov.py/leyes-paraguayas/12924/ley-n-7593-2025-de-protecci-n-de-datos-personales-en-la-rep-blica-del-paraguay) · Documentación · Comunidad · ES · Congreso Nacional de Paraguay · Biblioteca y Archivo Central del Congreso Nacional (Paraguay) · 27 nov 2025. Primera ley integral paraguaya de datos personales con medidas de seguridad, notificación de vulneraciones en 72 horas y oficial de protección de datos.
- [Ley Federal de Protección de Datos Personales en Posesión de los Particulares (México, 2025)](https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPDPPP.pdf) · Documentación · Comunidad · ES · Congreso de la Unión · Cámara de Diputados (texto vigente) · 14 nov 2025. Texto vigente de la nueva LFPDPPP (DOF 20-03-2025, última reforma 14-11-2025) con medidas de seguridad, aviso de privacidad, vulneraciones y sanciones.
- [BCRA – Texto ordenado 'Reporte de incidentes de ciberseguridad' (RRCI), actualizado por Com. 'A' 8280](https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-rrci.pdf) · Documentación · Comunidad · ES · BCRA · Banco Central de la República Argentina · 17 jul 2025. Régimen de reporte obligatorio de ciberincidentes a la SEFyC con plazos de reporte inicial, actualizaciones e informe final.
- [Comunicación “A” 8280 – Actualización de los Lineamientos para la respuesta y recuperación ante ciberincidentes (RRCI), BCRA](https://www.bcra.gob.ar/archivos/Pdfs/comytexord/A8280.pdf) · Documentación · Comunidad · ES · Banco Central de la República Argentina · 17 jul 2025. Actualiza los lineamientos RRCI: notificación inicial de incidentes importantes y críticos dentro de la primera hora, actualizaciones hasta su resolución y reporte de cierre en un máximo de 5 días corridos.
- [Acuerdo CONASSIF 5-24 – Reglamento General de Gobierno y Gestión de la Tecnología de Información (v03 julio 2025)](https://www.sugef.fi.cr/normativa/normativa_transversal/documentos/CONASSIF%205-24%20%28v03%2015%20julio%202025%29.pdf) · Documentación · Comunidad · ES · CONASSIF · SUGEF / CONASSIF · 15 jul 2025. Reglamento costarricense de gobierno de TI que cubre seguridad de la información, ciberseguridad, resiliencia digital, nube y clasificación de activos para entidades supervisadas.
- [Decreto 295 – Aprueba reglamento de reporte de incidentes de ciberseguridad de la Ley 21.663 (Chile)](https://www.leychile.cl/leychile/Navegar/imprimir?idNorma=1211466) · Documentación · Comunidad · ES · Biblioteca del Congreso Nacional de Chile · 1 mar 2025. Reglamento que fija la plataforma y los plazos de reporte de incidentes al CSIRT Nacional: alerta temprana en 3 horas y segundo reporte en 72 horas (24 horas para operadores de importancia vital con servicios esenciales afectados).
- [Ley 21.719 – Regula la protección y el tratamiento de los datos personales (Chile, versión vigente desde 01-12-2026)](https://www.bcn.cl/leychile/navegar?i=1209272&f=2026-12-01) · Documentación · Comunidad · ES · Congreso Nacional de Chile · Biblioteca del Congreso Nacional de Chile · 13 dic 2024. Nueva ley chilena de datos con Agencia de Protección de Datos, deber de seguridad, reporte de vulneraciones sin dilaciones indebidas y modelo de prevención de infracciones.
- [Decreto Supremo 016-2024-JUS – Reglamento de la Ley 29733 (Perú)](https://www.gob.pe/institucion/anpd/normas-legales/6554453-16-2024-jus) · Documentación · Comunidad · ES · Ministerio de Justicia y Derechos Humanos · Autoridad Nacional de Protección de Datos Personales (gob.pe) · 30 nov 2024. Nuevo reglamento peruano que exige notificar incidentes a la ANPD en 48 horas, documento de seguridad y oficial de datos personales de forma progresiva.
- [Ley 21.663 – Ley Marco de Ciberseguridad (Chile)](https://www.bcn.cl/leychile/navegar?i=1202434) · Documentación · Comunidad · ES · Congreso Nacional de Chile · Biblioteca del Congreso Nacional de Chile · 8 abr 2024. Ley que crea la ANCI y obliga a servicios esenciales, incluida la banca y los medios de pago, a gestionar riesgos y reportar incidentes.
- [BCRA Comunicación 'A' 7724 – Requisitos mínimos de gestión, implementación y control de riesgos de tecnología y seguridad de la información](https://www.bcra.gob.ar/archivos/Pdfs/comytexord/A7724.pdf) · Documentación · Comunidad · ES · BCRA · Banco Central de la República Argentina · 10 mar 2023. Norma del BCRA que reemplaza el régimen de la 'A' 4609 con requisitos de gobierno de TI, seguridad, ciberincidentes, terceros e inteligencia artificial para entidades financieras.
- [Decreto Ejecutivo 285 de 2021 – Reglamenta la Ley 81 de 2019 de Protección de Datos Personales (Panamá)](https://www.gacetaoficial.gob.pa/storage/gacetas/2021/05/29296_A/85281.pdf) · Documentación · Comunidad · ES · Presidencia de la República de Panamá · Gaceta Oficial de Panamá · 28 may 2021. Reglamento panameño con obligaciones de seguridad, registro de tratamientos y notificación de vulneraciones a la ANTAI y a los titulares.
- [SIC – Cumplimiento de la obligación del reporte de incidentes de seguridad (Colombia)](https://sedeelectronica.sic.gov.co/publicaciones/boletin-juridico/concepto/cumplimiento-de-la-obligacion-del-reporte-de-incidentes-de-seguridad) · Documentación · Comunidad · ES · SIC · Superintendencia de Industria y Comercio · 20 abr 2021. Concepto oficial de la SIC que fija en 15 días hábiles desde la detección el reporte de incidentes de seguridad bajo la Ley 1581 de 2012.
- [SBS Resolución 504-2021 – Reglamento para la Gestión de la Seguridad de la Información y la Ciberseguridad (Perú)](https://intranet2.sbs.gob.pe/dv_int_cn/2046/v4.0/Adjuntos/504-2021.R.pdf) · Documentación · Comunidad · ES · SBS · Superintendencia de Banca, Seguros y AFP · 19 feb 2021. Reglamento de la SBS que exige SGSI-C, gestión de identidades, ciberseguridad, terceros y reporte de incidentes significativos a la SBS.
- [CMF – Circular 2.261 / RAN Capítulo 20-10 Gestión de la seguridad de la información y ciberseguridad](https://www.cmfchile.cl/portal/normativa/624/w4-article-29310.html) · Documentación · Comunidad · ES · CMF · Comisión para el Mercado Financiero (Chile) · 6 jul 2020. Norma de la CMF que exige a bancos un sistema de gestión de seguridad de la información y ciberseguridad con rol del directorio y gestión de incidentes.
- [Decreto 64/020 art. 4 – Vulneraciones de seguridad (Uruguay)](https://www.impo.com.uy/bases/decretos/64-2020/4) · Documentación · Comunidad · ES · Poder Ejecutivo de Uruguay · IMPO (Centro de Información Oficial) · 17 feb 2020. Obliga a comunicar vulneraciones de seguridad a la URCDP dentro de 72 horas y a los titulares cuando la afectación sea significativa.
- [SFC – Circular Externa 007 de 2018 (ciberseguridad, CBJ Parte I Título IV Capítulo V)](https://www.superfinanciera.gov.co/loader.php?idFile=1031741&lFuncion=descargar&lServicio=Tools2&lTipo=descargas) · Documentación · Comunidad · ES · SFC · Superintendencia Financiera de Colombia · 5 jun 2018. Requerimientos mínimos para la gestión del riesgo de ciberseguridad de las entidades vigiladas por la SFC.
- [DOF – Resolución que modifica las disposiciones aplicables a las instituciones de crédito (sustituye Anexo 72 'Indicadores de seguridad de la información')](https://dof.gob.mx/nota_detalle_popup.php?codigo=5605312) · Documentación · Comunidad · ES · CNBV · Diario Oficial de la Federación. Resolución publicada en el DOF que actualiza los tipos y subtipos de eventos del Anexo 72 de indicadores de seguridad de la información de la banca.
- [SFC – Capítulo V Título IV Parte I CBJ actualizado por Circular Externa 033 de 2020](https://www.superfinanciera.gov.co/loader.php?lServicio=Tools2&lTipo=descargas&lFuncion=descargar&idFile=1031904) · Documentación · Comunidad · ES · SFC · Superintendencia Financiera de Colombia. Versión del capítulo de ciberseguridad modificada por la CE 033 de 2020 que añade el reporte de información a la SFC.
- [EcuCERT – Medidas para gestionar una vulneración de la seguridad de datos personales (LOPDP Ecuador)](https://www.ecucert.gob.ec/que-medidas-deben-tomar-los-prestadores-de-servicios-de-telecomunicaciones-para-gestionar-una-vulneracion-de-la-seguridad-de-datos-personales/) · Documentación · Comunidad · ES · EcuCERT · EcuCERT (ARCOTEL). Guía oficial que cita el art. 43 de la LOPDP: notificar vulneraciones a la Autoridad y a ARCOTEL en 5 días y a los titulares en 3 días.
- [Reglamento a la Ley 8968 (Decreto Ejecutivo 37554-JP, Costa Rica)](https://iafa.go.cr/wp-content/uploads/2025/01/Reglamento-a-la-Ley-de-Proteccion-de-la-Persona-frente-al-Tratamiento-de-sus-Datos-Personales.pdf) · Documentación · Comunidad · ES · Poder Ejecutivo de Costa Rica · IAFA (copia gubernamental del reglamento). Reglamento de la ley costarricense de datos personales con protocolos de actuación, medidas de seguridad y aviso de vulneraciones a los titulares.
- [Decreto N° 66/025 – Reglamentación de la Ley 20.212 en ciberseguridad (Uruguay)](https://www.impo.com.uy/bases/decretos/66-2025/8) · Documentación · Comunidad · ES · IMPO · 14 mar 2025. Reglamenta las obligaciones de ciberseguridad de entidades públicas y privadas de sectores críticos y las potestades del CERTuy, que define criterios y plazos de comunicación de incidentes.
- [El Salvador: Cybersecurity and Data Protection Laws Enacted (Library of Congress)](https://www.loc.gov/item/global-legal-monitor/2025-01-21/el-salvador-cybersecurity-and-data-protection-laws-enacted/) · Documentación · Comunidad · Library of Congress · Library of Congress – Global Legal Monitor · 21 ene 2025. Resumen oficial estadounidense de los Decretos 143 (ciberseguridad) y 144 (datos personales) de El Salvador, publicados el 15-11-2024 y supervisados por la Agencia de Ciberseguridad del Estado.
- [Decreto Legislativo 144 – Ley para la Protección de Datos Personales (El Salvador)](https://www.asamblea.gob.sv/sites/default/files/documents/decretos/F6986BF6-25C7-428B-9B74-325A6760AC2C.pdf) · Documentación · Comunidad · ES · Asamblea Legislativa de El Salvador · nov 2024. Ley general de datos personales de El Salvador; obliga a notificar vulneraciones a la Agencia de Ciberseguridad del Estado, a la Fiscalía y a los titulares en un máximo de 72 horas.
- [BCU Comunicación 2024/018 – Comunicación de eventos de tecnología, sistemas y seguridad de la información](https://www.bcu.gub.uy/Comunicados/seggco24018.pdf) · Documentación · Comunidad · ES · BCU · Banco Central del Uruguay · 11 ene 2024. Exige a las instituciones del sistema de pagos reportar eventos en 4 horas, seguimiento cada 48 horas y cierre en 15 días corridos.
- [SBP Acuerdo 001-2022 – Lineamientos para la protección de datos personales tratados por entidades bancarias (Panamá)](https://www.superbancos.gob.pa/documentos/leyes_y_regulaciones/acuerdos/2022/Acuerdo_01-2022.pdf) · Documentación · Comunidad · ES · SBP · Superintendencia de Bancos de Panamá · 24 feb 2022. Acuerdo de la SBP que fija estándares de protección de datos para bancos, apoyado en los acuerdos de riesgo de TI (3-2012), banca electrónica (6-2011) y riesgo operativo (11-2018).
- [Resolución JM-104-2021 – Reglamento para la Administración del Riesgo Tecnológico (Guatemala)](https://banguat.gob.gt/sites/default/files/banguat/Publica/Res_JM/2021/Res_JM-104-2021.pdf) · Documentación · Comunidad · ES · Junta Monetaria · Banco de Guatemala (Junta Monetaria) · 26 nov 2021. Reglamento de riesgo tecnológico para entidades supervisadas que deroga la JM-102-2011 e incluye ciberseguridad, terceros y respaldo local de información crítica.
- [Resolución AAIP 47/2018 – Medidas de seguridad recomendadas para el tratamiento de datos personales (Argentina)](https://www.argentina.gob.ar/normativa/nacional/norma-312662/texto) · Documentación · Comunidad · ES · Agencia de Acceso a la Información Pública · Argentina.gob.ar (InfoLEG) · 23 jul 2018. Guía oficial de medidas de seguridad (recolección, control de acceso, cambios, respaldo, incidentes, vulnerabilidades) que complementa la Ley 25.326.

**Manos a la obra**

1. `Laboratorio` Filtra la hoja «Normativa MCSA» del libro de Excel por tus países de operación y construye tu inventario de normas aplicables con autoridad, tipo, plazo de notificación, fuente oficial y estado de verificación.
2. `Laboratorio` Para cada norma del inventario, elige el enfoque en Compliance Manager con la tabla [Plantillas para MCSA](00_Programa.md#plantillas-mcsa) —plantilla premium, copia extendida o plantilla desde PDF— y justifícalo en una línea.
3. `Laboratorio` Verifica en el texto oficial dos plazos marcados como «según análisis» (por ejemplo, Perú 48 horas en el [reglamento de la Ley 29733](https://cdn.www.gob.pe/uploads/document/file/7756037/6554453-reglamento-de-la-ley-n-29733.pdf?v=1741726731) y Costa Rica cinco días hábiles en el [Reglamento 37554-JP](http://pgrweb.go.cr/TextoCompleto/NORMAS/1/VIGENTE/D/2010-2019/2010-2014/2012/12270/74352_115361-3.html)) y registra qué encontraste y dónde, o que no se pudo confirmar.
4. `Laboratorio parcial` Compara la plantilla de México (ley de 2010) con la [LFPDPPP de 2025](https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPDPPP.pdf) y lista los cambios que agregarías como controles en una copia extendida. Limitación: abrir la plantilla consume un cupo premium o parte de la prueba.
5. `Laboratorio` Prepara para el SOC la tabla de plazos de notificación de este módulo filtrada por tus países y define quién avisa a quién (SOC, CISO, Legal, privacidad y comunicaciones) y con qué plantilla de mensaje.
6. `Solo producción` Valida con Legal y privacidad el inventario de normas y el enfoque elegido. Motivo: la aplicabilidad depende de la actividad, las licencias y el supervisor reales. Cómo hacerlo seguro: entrega el inventario como borrador de trabajo, sin conclusiones jurídicas propias, y archiva la validación como evidencia de la evaluación.

<a id="reto-avanzado"></a>

## Reto del nivel

**Mapa y calendario de un banco regional.** Para un banco ficticio que opera en Chile, Colombia y Perú: inventaria las normas aplicables con su fuente oficial, elige el enfoque en Compliance Manager para cada una, completa el mapa de controles de nueve dominios entre ISO/IEC 27001:2022, NIST CSF 2.0 y las normas locales, y diseña el calendario anual de cumplimiento continuo con alertas, exportaciones, revisión de actualizaciones y un simulacro de notificación medido contra los plazos regulatorios. Documenta qué parte se automatiza y qué parte no, y por qué.

<a id="quiz-avanzado"></a>

## Evaluación del nivel

Responde y compara con [Evaluaciones y respuestas](06_Evaluaciones_y_respuestas.md#eval-avanzado). Con 80 % o más, ¡nivel aprobado! (En la versión web puedes corregir en línea y generar tu certificado).

1. ¿Qué afirma la documentación sobre extraer datos de Purview mediante APIs?
   - a) Hay un endpoint de Graph para la puntuación de cumplimiento
   - b) Solo existe un cmdlet de PowerShell para exportar evaluaciones
   - c) No hay APIs para extraer datos ni analíticas de Purview
   - d) Se usa la API de Secure Score para Compliance Manager

2. ¿Para qué sirven las APIs de Purview en Microsoft Graph, como protectionScopes y processContent?
   - a) Para que tus aplicaciones envíen contenido a Purview y apliquen sus políticas
   - b) Para leer la puntuación de cumplimiento
   - c) Para crear plantillas regulatorias
   - d) Para descargar informes del Service Trust Portal

3. ¿Adónde puede exportar Defender for Cloud de forma continua los datos de cumplimiento normativo?
   - a) Solo a un archivo de Excel mensual
   - b) A Compliance Manager por API
   - c) A una biblioteca de SharePoint
   - d) A Log Analytics o Event Hubs, en streaming o con instantáneas semanales

4. ¿Qué permite que una acción técnica satisfaga varias regulaciones a la vez?
   - a) Que las acciones de mejora se comparten entre las evaluaciones del mismo grupo
   - b) Que Microsoft fusiona las regulaciones similares
   - c) Que cada evaluación copia sus acciones
   - d) Que la puntuación se promedia entre evaluaciones

5. ¿Qué ofrece la preparación previa al despliegue (Sub-service compliance readiness)?
   - a) Evaluaciones premium gratis
   - b) El aporte de un servicio de Azure a ISO 27001, NIST 800-53, PCI DSS y SOC 2, con controles relacionados entre marcos y sin consumir licencias
   - c) El despliegue de servicios de Azure ya configurados
   - d) La certificación de servicios ante el supervisor

6. Asignaste una evaluación al grupo equivocado. ¿Qué dice la documentación?
   - a) Puedes moverla de grupo en cualquier momento
   - b) Microsoft la reasigna en 24 horas
   - c) Los grupos no se pueden cambiar una vez asignados
   - d) Se mueve sola al aceptar una actualización

7. ¿Qué implica aceptar una actualización pendiente (Pending update) de una plantilla?
   - a) Es reversible durante 30 días
   - b) Es permanente y se aplica por grupo; conviene diferirla si hay una auditoría en curso
   - c) Solo afecta a la evaluación abierta
   - d) Requiere la aprobación de Microsoft

8. ¿Cómo funciona la política de alertas predeterminada de cambio de puntuación?
   - a) Envía una alerta por cada cambio, sin agrupar
   - b) No existe: hay que crearla
   - c) Solo alerta al auditor interno
   - d) Agrupa las coincidencias de 60 minutos en una alerta de severidad media, enviada por defecto al Global Admin

9. ¿Qué rol de Entra ID se necesita para ver las páginas Policies y Alerts de Compliance Manager?
   - a) Global Administrator
   - b) Security reader
   - c) Ninguno: basta con Compliance Manager Reader
   - d) Billing Administrator

10. Según el Decreto 295 de Chile, ¿en qué plazo se envía la alerta temprana de un incidente?
   - a) 1 hora
   - b) 3 horas
   - c) 24 horas
   - d) 72 horas

11. Según la Comunicación BCRA «A» 8280, ¿cuándo se envía la notificación inicial de un ciberincidente importante?
   - a) Dentro de la primera hora
   - b) En 24 horas
   - c) En 72 horas
   - d) En 5 días corridos

12. ¿Qué dice la Ley 21.719 de Chile sobre el plazo para reportar vulneraciones a la Agencia?
   - a) 72 horas, como el RGPD
   - b) 24 horas hábiles
   - c) Sin dilaciones indebidas y por el medio más expedito; la ley no fija horas
   - d) Cinco días hábiles

13. ¿Qué grupo de países no tenía ley general de datos personales a noviembre de 2026?
   - a) Guatemala, Honduras, Venezuela y Bolivia
   - b) Chile, Perú, Colombia y Uruguay
   - c) México, Panamá, Costa Rica y Paraguay
   - d) Argentina, Ecuador, El Salvador y Nicaragua

14. ¿Qué plazo fija el Decreto 64/020 de Uruguay para comunicar vulneraciones a la URCDP?
   - a) 24 horas
   - b) 48 horas
   - c) 15 días hábiles
   - d) 72 horas desde que se conoce la vulneración

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. No constituye asesoría legal: la normativa citada es material de referencia y las decisiones de aplicabilidad corresponden a tus áreas de Legal, privacidad y, cuando aplique, RR. HH. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

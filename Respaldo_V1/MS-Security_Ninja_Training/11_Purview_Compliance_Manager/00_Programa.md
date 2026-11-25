# Programa: cómo usar, justificación, rutas y plan

*Microsoft Purview Compliance Manager Ninja Training · Edición 2026*

[Índice del programa](README.md) · [Nivel 1 · Inicial →](01_Nivel_1_Inicial.md)

<a id="como-usar"></a>

## Cómo usar esta guía

¿Quieres convertirte en Ninja de Compliance Manager? Esta guía reúne, ordenados como un curso, los mejores recursos públicos para gestionar el cumplimiento regulatorio con Microsoft Purview Compliance Manager: documentación de Microsoft Learn, avisos del Message Center, videos de Microsoft Mechanics, el Ninja oficial de 2023 y el trabajo de MVPs y especialistas, todo verificado al 6 de noviembre de 2026. Y como el cumplimiento se juega en la normativa local, incluye el panorama de privacidad, ciberseguridad y sector financiero de México, Centroamérica y Sudamérica (sin Brasil).

Está pensada para quienes operan Compliance Manager por razones distintas: equipos de GRC y cumplimiento, auditoría interna, dueños de controles de TI, seguridad y nube, privacidad y el comité de riesgos. Puedes seguirla completa o por tu rol. Cada nivel cierra con una evaluación y un reto; con 80 % o más generas tu certificado de finalización, como en el Ninja original. Y como los reguladores ya miran la IA, el recorrido llega a las plantillas de IA, las evaluaciones de agentes y las plantillas generadas desde el PDF de una norma.

**Estructura.** Tres niveles técnicos —Inicial (L100–L200), Intermedio (L300) y Avanzado (L400)—, un track de operación (L300–L400) para el modelo operativo, los indicadores y el gobierno, y una sección transversal de comunidad. El orden sigue la vida de un programa de cumplimiento: entender la herramienta y sus licencias, evaluar, extenderla a lo que no trae, automatizar y mapear, y operarla con gobierno.

**Cada módulo** sigue la forma Ninja: una introducción con el porqué, la justificación de negocio (*Por qué importa*), lo que vas a lograr, novedades y advertencias con fecha y fuente, una ruta rápida (*¿Tienes poco tiempo?*), los recursos agrupados por tipo, la práctica guiada (*Manos a la obra*) y lecturas para profundizar. Tres tablas de referencia —[licencias](#licencias), [plantillas para MCSA](#plantillas-mcsa) y [programa de cumplimiento continuo](#cumplimiento-continuo)— se exportan también al libro de Excel, junto con la hoja «Normativa MCSA».

**Evaluación y certificado.** Cada nivel técnico y el track de operación cierran con una evaluación de opción múltiple, con la explicación y la fuente de cada respuesta, y un reto integrador. Con 80 % o más puedes generar el certificado de finalización. Es una autoevaluación de esta guía, no una certificación de Microsoft: para eso están el examen SC-900 y el Ninja oficial de Tech Community.

**Laboratorio.** Cada ejercicio indica dónde se puede hacer: `[LAB]` completo en una prueba de Microsoft 365 E5 con una suscripción de Azure; `[LAB-PARCIAL]` con las limitaciones que se explican (cupos premium, prueba única de 90 días, costos de Defender for Cloud o Foundry, funciones recién lanzadas); `[SOLO-PRODUCCION]` cuando hacen falta dueños, auditores, licencias o evidencias reales, con la forma segura de practicar.

**Fechas, estados y alcance legal.** Cada dato tiene fuente y fecha. Microsoft Ignite (17 al 20 de noviembre de 2026) puede cambiar estados de vista previa, y la documentación en español suele actualizarse después que la inglesa. Esta guía no es asesoría legal: la normativa es material de referencia y las decisiones de aplicabilidad corresponden a Legal, privacidad y, cuando aplique, RR. HH.

**Leyenda de etiquetas**

| Etiqueta | Significado |
|---|---|
| Microsoft oficial | Documentación, blogs y videos publicados por Microsoft. |
| Empleado de Microsoft | Material de ingenieros, gerentes de producto o arquitectos de Microsoft en canales propios o comunitarios. |
| MVP de Microsoft | Material de Most Valuable Professionals, con estado verificado en fuentes públicas. |
| Comunidad o partner | Autores de la comunidad o de partners; útil, pero contrástalo con la documentación oficial. |
| Vista previa | Funcionalidad en preview: puede cambiar y no siempre tiene soporte de producción. |
| Legado aún útil | Recurso anterior a los cambios de 2025–2026 que sigue explicando bien el concepto; lee la nota de qué cambió. |
| Ninja original | Recurso que formaba parte del Ninja oficial del producto. |
| Nuevo | Recurso publicado o actualizado desde mayo de 2026. |
| ES | Recurso disponible en español. |
| Laboratorio | Ejercicio que puedes hacer completo en el entorno de práctica (prueba de Microsoft 365 E5 o sandbox y suscripción de Azure). |
| Laboratorio parcial | Ejercicio posible en el entorno de práctica con limitaciones que se indican. |
| Solo producción | Requiere licencias pagas, datos o usuarios reales, o varios inquilinos: síguelo con la estrategia de práctica segura en producción. |

<a id="por-que"></a>

## Por qué este programa

**Por qué ahora.** Entre 2024 y 2026 Compliance Manager cambió de portal, de licencias y de alcance: el portal de cumplimiento clásico se retiró, E5 Compliance pasó a llamarse Microsoft Purview Suite, llegaron las plantillas premium de IA, las evaluaciones automáticas de agentes, la multinube con Defender for Cloud y, en octubre de 2026, las plantillas generadas desde el PDF de una norma. Al mismo tiempo, la región aceleró: nueva ley de datos en México (marzo de 2025), Ley 21.719 en Chile (vigente desde el 1 de diciembre de 2026), Decreto 295 con alertas en tres horas, Comunicación «A» 8280 del BCRA con notificación en la primera hora, nuevas leyes en Ecuador, Paraguay y Guatemala. Un equipo formado con el Ninja de 2023 cree que E5 incluye «todas» las plantillas, usa una plantilla mexicana desactualizada y no conoce el camino para las normas que no tienen plantilla.

**Qué gana la organización.** Resultados medibles: porcentaje de acciones propias implementadas y probadas con evidencia aceptada, acciones vencidas por dueño, tiempo medio de cierre, normas aplicables con evaluación activa, cupos premium alineados con prioridades, reutilización de controles entre regulaciones, tiempo de preparación de una auditoría y simulacros que cumplen los plazos regulatorios. Cada nivel deja entregables reutilizables: ficha de licencias y decisión de cupos, plantillas propias para normas locales, mapa de controles, calendario de cumplimiento continuo, tablero de indicadores y matriz RACI.

**Para quién.** Gestores de cumplimiento y GRC, auditoría interna, dueños de controles de TI, seguridad y nube, oficiales de privacidad y el comité de riesgos o el CISO. Cada perfil usa la herramienta por una razón distinta —obligación regulatoria, prueba independiente, implementación técnica, protección de datos personales o decisión de riesgo— y las rutas por rol permiten recorrer solo lo necesario, con un tronco común en el nivel inicial.

**Cómo se conecta con el resto de la serie.** Es uno de los ocho programas de Purview, porque cada capacidad la operan equipos distintos por razones distintas. Muchas acciones de mejora se implementan en otros programas: Information Protection (etiquetas y cifrado), DLP, ciclo de vida de los datos y registros (retención), eDiscovery y Audit (auditoría como evidencia), riesgo interno y cumplimiento de comunicaciones (sectores regulados) y DSPM y seguridad de datos para IA (controles de datos para Copilot y agentes). Fuera de Purview, **Entra** aporta PIM y roles; **Defender XDR**, Secure Score y el reporte ejecutivo del SOC; **Sentinel**, el destino de la exportación continua de Defender for Cloud; y **Security Copilot**, la asistencia en protección de datos y cumplimiento.

<a id="licencias"></a>

## Licencias: qué incluye cada plan

Compliance Manager está disponible con licencias de Office 365 y Microsoft 365 (incluido Business Premium) y para GCC, GCC High y DoD; lo que cambia según el plan es qué plantillas puedes usar sin costo y qué acciones de mejora puedes implementar. Esta tabla resume lo que dice Microsoft Learn al 6 de noviembre de 2026 y marca «confírmalo» donde la documentación no es explícita.

Tres reglas prácticas: (1) Microsoft 365 E5, A5 y G5 incluyen la Data Protection Baseline más **tres** plantillas premium a elección, no «todas»; (2) el resto se compra por plantilla, con licencia de un año que se renueva sola; y (3) muchas acciones se implementan con capacidades de nivel E5 —por ejemplo, DLP en Teams o riesgo interno—, así que con E3 verás acciones que no podrás completar sin un complemento como Microsoft Purview Suite.

**Licencias de Compliance Manager**

| Capacidad | Microsoft 365 E3 | Microsoft 365 E5 / Purview Suite | Plantillas premium o complemento | Fuente |
|---|---|---|---|---|
| Compliance Manager: panel, puntuación, evaluaciones, acciones de mejora y alertas | Incluido (también en Office 365 y Business Premium) | Incluido | No requiere | [Learn · descripción del servicio](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description) |
| Plantilla Microsoft Data Protection Baseline | Incluida | Incluida | No requiere | [Learn · lista de regulaciones](https://learn.microsoft.com/en-us/purview/compliance-manager-regulations-list) |
| Plantillas premium (más de 360 en la biblioteca) | Compra por plantilla | E5, A5 y G5: tres a elección sin costo. Purview Suite: Learn no lo menciona; confírmalo | Licencia por plantilla durante un año con renovación automática; se compra en el centro de administración, por CSP o por licenciamiento por volumen y aparece en hasta 48 h | [Learn · regulaciones](https://learn.microsoft.com/en-us/purview/compliance-manager-regulations) |
| Familias de una regulación (por ejemplo, CMMC niveles 1 a 5) | Una licencia por familia | Cuentan como un solo cupo | Cuentan como una plantilla | [Learn · FAQ](https://learn.microsoft.com/en-us/purview/compliance-manager-faq) |
| NIST 800-53, ISO 27001 y GDPR | Compra por plantilla | Incluidas hasta diciembre de 2022; hoy ocupan cupo | Compra por plantilla si no entran en tus cupos | [Learn · FAQ](https://learn.microsoft.com/en-us/purview/compliance-manager-faq) |
| Prueba de evaluaciones premium | Disponible (licencias comerciales) | Disponible (licencias comerciales) | 25 plantillas durante 90 días, una vez por inquilino; al terminar dejan de actualizarse | [Learn · prueba premium](https://learn.microsoft.com/en-us/purview/purview-compliance-manager-assessments-trial) |
| Plantillas premium de IA (EU AI Act, ISO/IEC 23894, ISO/IEC 42001 y NIST AI RMF) | Compra por plantilla | Pueden ocupar cupos premium; consumen licencia | Evaluaciones integradas de IA gratis por seis meses con licencias de Copilot o de agentes (confírmalo en tu inquilino) | [Learn · evaluaciones](https://learn.microsoft.com/en-us/purview/compliance-manager-assessments) |
| Evaluación base de Microsoft 365 Copilot y Copilot Chat | Requiere licencias de Microsoft 365 Copilot o Copilot Chat | Igual que en E3 | Se aprovisiona automáticamente al comprar Copilot | [Learn · evaluaciones](https://learn.microsoft.com/en-us/purview/compliance-manager-assessments) |
| Evaluaciones automáticas de agentes de Microsoft Foundry | Requiere un proyecto de Foundry y roles de Azure AI | Igual que en E3 | Purview para agentes de Foundry y apps conectadas a Entra se soportará con Microsoft 365 E7 y las SKU de Agent 365 | [Learn · descripción del servicio](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description) |
| Plantillas propias (en blanco o desde PDF) y copias personalizadas | Learn no documenta un requisito premium para crear plantillas | Igual que en E3 | Copiar una plantilla premium consume su licencia | [Learn · crear plantillas](https://learn.microsoft.com/en-us/purview/compliance-manager-create-template) |
| Multinube con Defender for Cloud (Azure, AWS y GCP) | Requiere Defender for Cloud en una suscripción de Azure | Igual que en E3 | Foundational CSPM o Defender CSPM; los estándares no predeterminados requieren un plan pago de Defender for Cloud | [Learn · ajustes de nube](https://learn.microsoft.com/en-us/purview/compliance-manager-cloud-settings) |
| Conectores de Compliance Manager (Salesforce, Zoom y Corporate Sustainability) | Requieren una cuenta del servicio y el rol Data Connector Admin o Global Admin | Igual que en E3 | Un conector por instancia o cuenta | [Learn · conectores](https://learn.microsoft.com/en-us/purview/compliance-manager-connectors) |
| Preparación previa al despliegue (vista previa) | Sin licencia | Sin licencia | No consume licencias ni crea evaluaciones | [Learn · preparación previa](https://learn.microsoft.com/en-us/purview/compliance-manager-predeployment-compliance) |
| Acciones que se implementan con capacidades de nivel E5 (por ejemplo, DLP en Teams, Endpoint DLP o riesgo interno) | Aparecen, pero la capacidad que las implementa requiere nivel E5 | Implementables | Microsoft Purview Suite (antes E5 Compliance): complemento sobre Microsoft 365 E3; precio de lista de USD 12 por usuario al mes con pago anual | [Precios de Microsoft Security](https://www.microsoft.com/en-us/security/pricing-overview) |
| Microsoft 365 E7 | No aplica | E7 incluye E5 más Microsoft 365 Copilot, Agent 365 y Entra Suite (GA el 1 de mayo de 2026) | Cupos premium: Learn menciona A5, E5 y G5, no E7; confírmalo | [Microsoft 365 E7](https://www.microsoft.com/en-us/microsoft-365/enterprise/e7) |
| Pago por uso de Purview | Compliance Manager no figura entre sus capacidades | Igual que en E3 | Otras capacidades que aportan evidencia sí usan pago por uso (por ejemplo, la auditoría de apps de IA no Microsoft) | [Learn · pago por uso](https://learn.microsoft.com/en-us/purview/purview-payg-subscription-based-enablement) |

Fuentes principales: [descripción del servicio de Purview](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description), [lista de regulaciones](https://learn.microsoft.com/en-us/purview/compliance-manager-regulations-list), [FAQ](https://learn.microsoft.com/en-us/purview/compliance-manager-faq) y [anuncio de GA de Microsoft 365 E7 y Agent 365](https://techcommunity.microsoft.com/blog/microsoft_365blog/microsoft-365-e7-and-agent-365-are-now-generally-available/4516295). Ante cualquier diferencia mandan tu contrato y la documentación oficial vigente; los precios son de lista y pueden variar por acuerdo y país.

<a id="plantillas-mcsa"></a>

## Plantillas de Compliance Manager para MCSA

Microsoft mantiene plantillas para pocas normas de la región y algunas no reflejan la versión vigente de la ley. Esta tabla cruza la hoja «Normativa MCSA» con la lista de regulaciones de Compliance Manager y propone un enfoque para cada norma: **plantilla premium** cuando existe y está vigente; **evaluación personalizada** (copia extendida de una plantilla) cuando existe pero está desactualizada o incompleta; y **plantilla generada desde el PDF** de la norma, o en blanco, cuando no existe.

Es material de referencia, no asesoría legal: la aplicabilidad de cada norma la decide tu área de Legal, junto con privacidad. «Plantilla disponible» refleja la lista de regulaciones actualizada el 6 de marzo de 2025: verifica en tu inquilino antes de decidir.

**Plantillas de Compliance Manager para la normativa de MCSA**

| País | Regulación | Plantilla disponible | Enfoque recomendado | Notas | Fuente |
|---|---|---|---|---|---|
| México | Ley Federal de Protección de Datos Personales en Posesión de los Particulares (nueva ley, DOF 20 de marzo de 2025) | Desactualizada | Evaluación personalizada (copia extendida de la plantilla premium) o plantilla generada desde el PDF de la ley de 2025 | La plantilla «Mexico - Federal Law on Protection of Personal Data Held by Private Parties» sigue la ley de 2010; aviso inmediato al titular ante vulneraciones significativas (art. 19) | [LFPDPPP](https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPDPPP.pdf) |
| México | Ley Federal de Protección al Consumidor | Sí | Plantilla premium, si aplica a tu negocio | Verifica con Legal la versión que refleja la plantilla | [Learn · lista de regulaciones](https://learn.microsoft.com/en-us/purview/compliance-manager-regulations-list) |
| México | Ley General de Protección de Datos Personales en Posesión de Sujetos Obligados (2025) | No | Plantilla generada desde el PDF | Sector público; última reforma del 14 de noviembre de 2025 | [LGPDPPSO](http://www.diputados.gob.mx/LeyesBiblio/pdf/LGPDPPSO.pdf) |
| México | Disposiciones de la CNBV para instituciones de crédito (seguridad de la información, arts. 168 Bis) | No | Plantilla generada desde el PDF de los artículos aplicables, o en blanco | Exige un oficial en jefe de seguridad de la información; la norma se reforma con frecuencia | [CNBV](https://www.cnbv.gob.mx/Normatividad/Disposiciones%20de%20car%C3%A1cter%20general%20aplicables%20a%20las%20instituciones%20de%20cr%C3%A9dito.pdf) |
| Guatemala | Ley Marco de Ciberseguridad (Decreto 26-2026) | No | Esperar la publicación; luego, plantilla generada desde el PDF | Aprobada el 3 de noviembre de 2026, pendiente de publicación; Guatemala no tiene ley general de datos personales | [Diario de Centro América](https://dca.gob.gt/noticias-guatemala-diario-centro-america/nueva-ley-blinda-el-ciberespacio-de-guatemala/) |
| Guatemala | Reglamento para la Administración del Riesgo Tecnológico (JM-104-2021) | No | Plantilla generada desde el PDF | Gobierno de TI, seguridad, continuidad y servicios de terceros | [Banguat](https://banguat.gob.gt/sites/default/files/banguat/Publica/Res_JM/2021/Res_JM-104-2021.pdf) |
| El Salvador | Ley para la Protección de Datos Personales (Decreto Legislativo 144) | No | Plantilla generada desde el PDF | 72 h para notificar a la Agencia de Ciberseguridad del Estado, la Fiscalía y los titulares (art. 25) | [Decreto 144](https://www.asamblea.gob.sv/sites/default/files/documents/decretos/F6986BF6-25C7-428B-9B74-325A6760AC2C.pdf) |
| El Salvador | Ley de Ciberseguridad y Seguridad de la Información (Decreto Legislativo 143) | No | Plantilla generada desde el PDF | Crea la Agencia de Ciberseguridad del Estado | [Decreto 143](https://www.asamblea.gob.sv/sites/default/files/documents/decretos/A0373897-3BAE-4A20-8F5F-E4DF22626D03.pdf) |
| El Salvador | NRP-23 (seguridad de la información en entidades financieras) | No | Plantilla generada desde el PDF | Notificación de incidentes a la alta gerencia y a la Superintendencia | [NRP-23](https://www.bcr.gob.sv/regulaciones/upload/NRP-23.pdf) |
| Honduras | Circular CNBS 025/2022 (TI, seguridad de la información y ciberseguridad) | No | Plantilla generada desde el PDF | Incluye controles mínimos para la nube; Honduras no tiene ley general de datos personales | [CNBS](https://circulares.cnbs.gob.hn/Archivo/Viewer/2520/025-2022%20NORMAS%20GESTION%20TECNOLOGIAS%20INFORMACION.pdf) |
| Nicaragua | Ley 787 de Protección de Datos Personales y su Reglamento | No | Plantilla generada desde el PDF o en blanco | Ley general con deberes de seguridad para ficheros públicos y privados | [Ley 787](http://legislacion.asamblea.gob.ni/normaweb.nsf/9e314815a08d4a6206257265005d21f9/e5d37e9b4827fc06062579ed0076ce1d) |
| Nicaragua | Norma sobre Gestión de Riesgo Tecnológico (SIBOIF) | No | Plantilla generada desde el PDF | Riesgo tecnológico, continuidad e incidentes en instituciones financieras | [SIBOIF](https://www.superintendencia.gob.ni/sites/default/files/documentos/normas/cd-siboif-500-1-sep19-2007_-_nrt_2015.pdf) |
| Costa Rica | Ley 8968 y su Reglamento (Decreto Ejecutivo 37554-JP) | No | Plantilla generada desde el PDF | El expediente 23.097, que la reemplazaría, sigue en trámite | [Reglamento](http://pgrweb.go.cr/TextoCompleto/NORMAS/1/VIGENTE/D/2010-2019/2010-2014/2012/12270/74352_115361-3.html) |
| Costa Rica | Acuerdo CONASSIF 5-24 (gobierno y gestión de la tecnología de información) | No | Plantilla generada desde el PDF | Versión 3 del 15 de julio de 2025; incluye terceros y nube | [CONASSIF 5-24](https://www.sugef.fi.cr/normativa/normativa_transversal/documentos/CONASSIF%205-24%20%28v03%2015%20julio%202025%29.pdf) |
| Panamá | Ley 81 de 2019 y Decreto Ejecutivo 285 de 2021 | No | Plantilla generada desde el PDF | 72 h para notificar incidentes (verificar el artículo del decreto) | [Decreto 285](https://antai.gob.pa/wp-content/uploads/2021/05/Reglamentacio%CC%81n-de-Ley-81-de-Proteccio%CC%81n-de-Datos-Personales.pdf) |
| Panamá | Acuerdo SBP 3-2012 (riesgo de tecnología de la información) | No | Plantilla generada desde el PDF | Gobierno de TI, seguridad y continuidad en bancos | [Acuerdo 3-2012](https://www.superbancos.gob.pa/documentos/leyes_y_regulaciones/acuerdos/2012/Acuerdo_3-2012.pdf) |
| Colombia | Ley 1581 de 2012 y Decreto 1377 de 2013 | Sí | Plantilla premium («Colombia - Decree No. 1377/2013»), extendida con el reporte a la SIC | Reporte de incidentes a la SIC en 15 días hábiles | [Ley 1581](http://www.secretariasenado.gov.co/senado/basedoc/ley_1581_2012.html) |
| Colombia | Ley 1266 de 2008 (habeas data financiero) | Sí | Plantilla premium | Verifica con Legal la versión que refleja la plantilla | [Learn · lista de regulaciones](https://learn.microsoft.com/en-us/purview/compliance-manager-regulations-list) |
| Colombia | Circular Externa 007 de 2018 de la SFC (ciberseguridad) | Sí (verificar vigencia) | Plantilla premium («External Circular Letter 007 of 2018»), extendida con los cambios de la CE 033 de 2020 | Política, unidad responsable, incidentes, pruebas y terceros | [SFC](https://www.superfinanciera.gov.co/loader.php?lServicio=Tools2&lTipo=descargas&lFuncion=descargar&idFile=1031904) |
| Colombia | Circular Externa 005 de 2019 de la SFC (computación en la nube) | No | Plantilla generada desde el PDF | Complementa la evaluación multinube | [SFC](https://www.superfinanciera.gov.co/loader.php?lServicio=Tools2&lTipo=descargas&lFuncion=descargar&idFile=1070310) |
| Venezuela | Normativa de tecnología de la información y banca electrónica de SUDEBAN | No | Plantilla generada desde el PDF | Venezuela no tiene ley general de datos personales | [SUDEBAN](https://sudeban.gob.ve/wp-content/uploads/NORMAS_PRUDENCIALES/26-LA-ADECUADA-TECNOLOGIA-DE-LA-INFORMACION/26-4-1-ANEXO-CC-SBIF-DSB-II-GGTI-GRT-01907.pdf) |
| Ecuador | LOPDP, reglamento y norma técnica de notificación de vulneraciones (2026) | No | Plantilla generada desde el PDF | 5 días a la SPDP y ARCOTEL; 3 días a los titulares si hay riesgo | [LOPDP](https://www.gob.ec/sites/default/files/regulations/2025-01/01%20Ley%20Org%C3%A1nica%20de%20Protecci%C3%B3n%20de%20Datos%20Personales.pdf) |
| Ecuador | Ley Orgánica para el Fortalecimiento de la Ciberseguridad | No | Plantilla generada desde el PDF | Vigente desde el 22 de mayo de 2026; reglamento pendiente | [Registro Oficial](https://www.asambleanacional.gob.ec/es/system/files/ro_29.pdf) |
| Ecuador | Codificación de normas de la Superintendencia de Bancos (seguridad de la información) | No | Plantilla generada desde el PDF de la versión vigente | La codificación se reforma con frecuencia | [Superintendencia de Bancos](https://www.superbancos.gob.ec/bancos/normativa-de-la-sb/) |
| Perú | Ley 29733 y nuevo reglamento (DS 016-2024-JUS) | Sí (verificar vigencia) | Plantilla premium («Peruvian Legislation Law 29733»), extendida con el nuevo reglamento si no lo refleja | Reglamento vigente desde el 31 de marzo de 2025, posterior a la última actualización de la lista | [Reglamento](https://cdn.www.gob.pe/uploads/document/file/7756037/6554453-reglamento-de-la-ley-n-29733.pdf?v=1741726731) |
| Perú | Resolución SBS 504-2021 (seguridad de la información y ciberseguridad) | No | Plantilla generada desde el PDF | Vigente desde el 1 de julio de 2021 | [SBS 504-2021](https://intranet2.sbs.gob.pe/dv_int_cn/2046/v4.0/Adjuntos/504-2021.R.pdf) |
| Perú | Decreto de Urgencia 007-2020 (Marco de Confianza Digital) | No | Plantilla generada desde el PDF | Reporte de incidentes al Centro Nacional de Seguridad Digital | [DU 007-2020](https://cdn.www.gob.pe/uploads/document/file/2790485/Decreto%20de%20Urgencia%20N%C2%BA%20007-2020.pdf) |
| Perú | Ley 31814 de inteligencia artificial y su reglamento (DS 115-2025-PCM) | No | Plantilla generada desde el PDF, mapeada contra las plantillas de IA | Reglamento publicado el 9 de septiembre de 2025 | [DS 115-2025-PCM](https://busquedas.elperuano.pe/dispositivo/NL/2436426-1) |
| Bolivia | Reglamento para la Gestión de Seguridad de la Información (ASFI) | No | Plantilla generada desde el PDF | Bolivia no tiene ley general de datos personales | [ASFI](https://www.asfi.gob.bo/la/recopilacion-normas-para-servicios-financieros-rnsf) |
| Chile | Ley 21.719 de protección de datos personales | No | Plantilla generada desde el PDF o en blanco | Vigente desde el 1 de diciembre de 2026; reporte «sin dilaciones indebidas» | [Ley 21.719](https://www.leychile.cl/leychile/Navegar?idNorma=1209272&idParte=1) |
| Chile | Ley 21.663 y Decreto 295 (ciberseguridad) | No | Plantilla generada desde el PDF | Alerta temprana en 3 h y segundo reporte en 72 h | [Decreto 295](https://www.leychile.cl/leychile/Navegar/imprimir?idNorma=1211466) |
| Chile | RAN Capítulo 20-10 de la CMF (seguridad de la información y ciberseguridad) | No | Plantilla generada desde el PDF | Sistema de gestión aprobado por el directorio | [RAN 20-10](https://www.cmfchile.cl/portal/normativa/624/w4-article-29310.html) |
| Chile | RAN Capítulo 20-7 de la CMF (externalización, incluida la nube) | No | Plantilla generada desde el PDF | La CMF publicó en abril de 2026 un informe normativo para actualizarlo | [RAN 20-7](https://www.cmfchile.cl/portal/normativa/624/articles-28982_doc_pdf.pdf) |
| Argentina | Ley 25.326 y Resolución AAIP 47/2018 | Sí | Plantilla premium («Argentina - Personal Data Protection Act 25.326»), extendida con controles de la Res. AAIP 47/2018 | Sin plazo legal específico de notificación | [Ley 25.326](https://www.argentina.gob.ar/normativa/nacional/norma-64790/actualizacion) |
| Argentina | Comunicación BCRA «A» 7724 (riesgos de tecnología y seguridad de la información) | No | Plantilla generada desde el PDF | Gobierno de TI, terceros e inteligencia artificial | [BCRA · A 7724](https://www.bcra.gob.ar/archivos/Pdfs/comytexord/A7724.pdf) |
| Argentina | RRCI: Comunicaciones «A» 7266 y «A» 8280 | No | Plantilla generada desde el PDF | Notificación inicial en la primera hora y cierre en 5 días corridos | [BCRA · A 8280](https://www.bcra.gob.ar/archivos/Pdfs/comytexord/A8280.pdf) |
| Paraguay | Ley 7593/2025 de Protección de Datos Personales | No | Plantilla generada desde el PDF | Plena vigencia prevista a fines de noviembre de 2027; 72 h para notificar | [Ley 7593/2025](https://www.bacn.gov.py/leyes-paraguayas/12924/ley-n-75932025--de-proteccin-de-datos-personales-en-la-repblica-del-paraguay) |
| Paraguay | Resolución BCP 25/2025 (proveedores de servicios de pago) | No | Plantilla generada desde el PDF | Seguridad de la información para proveedores de servicios de pago | [BCP](https://www.bcp.gov.py/documents/20117/1485220/Resoluci%C3%B3n25.pdf/b2977004-72a6-4fe8-8947-72aac3145c67?t=1766422591466) |
| Uruguay | Ley 18.331, Ley 19.670 y Decreto 64/020 | No | Plantilla generada desde el PDF | 72 h a la URCDP desde que se conoce la vulneración | [Decreto 64/020](https://www.impo.com.uy/bases/decretos/64-2020/4) |
| Uruguay | Ley 20.212 y Decreto 66/025 (ciberseguridad) | No | Plantilla generada desde el PDF; mapeo con NIST CSF 2.0 | Marco de Ciberseguridad alineado con NIST CSF 2.0 | [Decreto 66/025](https://www.impo.com.uy/bases/decretos/66-2025/8) |
| Uruguay | Comunicaciones BCU 2024/018 y 2026/009 (eventos de TI y tercerización) | No | Plantilla generada desde el PDF | Verifica el alcance por tipo de institución | [BCU 2024/018](https://www.bcu.gub.uy/Comunicados/seggco24018.pdf) |

Fuentes: [Learn · lista de regulaciones](https://learn.microsoft.com/en-us/purview/compliance-manager-regulations-list) (actualizada el 6 de marzo de 2025), [Learn · crear plantillas](https://learn.microsoft.com/en-us/purview/compliance-manager-create-template) y la hoja «Normativa MCSA», con la fuente oficial de cada norma. Referencia, no asesoría legal.

<a id="cumplimiento-continuo"></a>

## Programa de cumplimiento continuo

Un calendario de referencia para operar Compliance Manager todo el año. Ajusta frecuencias y responsables a tu organización y a los ciclos de tu supervisor; la columna de evidencia indica qué debe quedar archivado para demostrar que la actividad ocurrió. Se trabaja en el módulo [A3](03_Nivel_3_Avanzado.md#a3) y se gobierna en [O1](04_Nivel_4_Operacion.md#o1) y [O3](04_Nivel_4_Operacion.md#o3).

**Programa de cumplimiento continuo con Compliance Manager**

| Actividad | Frecuencia | Responsable | Evidencia | Herramienta o capacidad | Fuente |
|---|---|---|---|---|---|
| Atender alertas de puntuación, asignación, implementación, prueba y evidencias | Continua, al recibir el correo | Gestor de GRC y dueños de controles | Alerta cerrada con comentario o tarea creada | Políticas de alertas de Compliance Manager | [Learn · alertas](https://learn.microsoft.com/en-us/purview/compliance-manager-alert-policies) |
| Revisar la puntuación y sus variaciones por evaluación | Semanal | Gestor de GRC | Nota de variaciones con fecha de corte | Panel y puntuación de Compliance Manager | [Learn · puntuación](https://learn.microsoft.com/en-us/purview/compliance-manager-scoring) |
| Seguir las acciones asignadas y vencidas | Semanal | Dueños de controles de TI, seguridad y nube | Estado de implementación, notas y documentos al día | Acciones de mejora | [Learn · acciones de mejora](https://learn.microsoft.com/en-us/purview/compliance-manager-improvement-actions) |
| Actualizar acciones en bloque (estado, pruebas, responsables y evidencias) | Mensual o por ciclo | Gestor de GRC | Archivo exportado y archivo cargado, ambos versionados | Exportación e importación en Excel | [Learn · actualizar acciones](https://learn.microsoft.com/en-us/purview/compliance-manager-update-actions) |
| Exportar el informe de cada evaluación | Mensual y al cierre de cada ciclo de auditoría | Gestor de GRC | Excel fechado y archivado | Informe de evaluación | [Learn · evaluaciones](https://learn.microsoft.com/en-us/purview/compliance-manager-assessments) |
| Decidir sobre las actualizaciones pendientes de plantillas | Mensual (diferir durante auditorías) | Gestor de GRC, con auditoría interna | Registro de la decisión e informes antes y después | Pending update | [Learn · evaluaciones](https://learn.microsoft.com/en-us/purview/compliance-manager-assessments) |
| Revisar el estado multinube y los errores de acceso a suscripciones | Mensual | Dueños de controles de nube | Progreso por servicio y suscripción; datos exportados | Defender for Cloud y exportación continua | [Learn · exportación continua](https://learn.microsoft.com/en-us/azure/defender-for-cloud/benefits-of-continuous-export) |
| Probar acciones manuales por muestreo | Trimestral | Auditoría interna (rol Assessor) | Resultados de prueba con evidencia referenciada | Pruebas de acciones de mejora | [Nota metodológica del BCU](https://www.bcu.gub.uy/Comunicados/Anexo%201%20-%20Nota%20metodologica%20V2.pdf) |
| Revisar accesos, roles y expiraciones | Trimestral | Administrador de Compliance Manager y equipo de identidad | Lista de asignaciones, expiraciones y cambios | Roles de Compliance Manager y grupos de roles de Purview | [Learn · configuración](https://learn.microsoft.com/en-us/purview/compliance-manager-setup) |
| Reportar al comité de riesgos | Trimestral | CISO y gestor de GRC | Informe de una página con tendencia, riesgos y decisiones | Informe de evaluación e informes de postura de Purview | [Learn · informes de postura](https://learn.microsoft.com/en-us/purview/purview-reports) |
| Revisar las evaluaciones de IA de Copilot y de los agentes | Trimestral y ante cada agente nuevo | Dueño del agente y privacidad | Evaluación de IA actualizada con evidencias de DSPM | Plantillas de IA y evaluaciones de Foundry | [Learn · evaluaciones](https://learn.microsoft.com/en-us/purview/compliance-manager-assessments) |
| Vigilar las novedades del producto y del Message Center | Mensual | Gestor de GRC | Bitácora de cambios con impacto | What's new in Microsoft Purview y Message Center | [Learn · novedades de Purview](https://learn.microsoft.com/en-us/purview/whats-new) |
| Vigilar cambios normativos y fechas de entrada en vigor | Mensual | Legal y privacidad, con GRC | Inventario de normas actualizado | Hoja «Normativa MCSA» y fuentes oficiales | [Ley 21.719, versión vigente desde el 1 de diciembre de 2026](https://www.bcn.cl/leychile/navegar?i=1209272&f=2026-12-01) |
| Simulacro de notificación de incidentes | Semestral | CISO, SOC, Legal y comunicaciones | Informe con tiempos frente a los plazos regulatorios | Procedimiento de incidentes y acciones de mejora | [Decreto 295](https://www.leychile.cl/leychile/Navegar/imprimir?idNorma=1211466) |
| Revisar el uso y la renovación de las plantillas premium | Anual, antes de la renovación | Gestor de GRC y compras | Contador de licencias y decisión de renovar o no | Página Regulations | [Learn · regulaciones](https://learn.microsoft.com/en-us/purview/compliance-manager-regulations) |
| Actualizar la evidencia de los controles de Microsoft | Anual o al iniciar una auditoría | Auditoría interna | Informes descargados del Service Trust Portal | Service Trust Portal | [Service Trust Portal](https://learn.microsoft.com/en-ie/purview/get-started-with-service-trust-portal?view=o365-worldwide) |
| Autoevaluación para el supervisor, cuando aplique | Según el calendario del supervisor | Gestor de GRC y auditoría interna | Autoevaluación con evidencia referenciada | Informe de evaluación y evidencias | [Nota metodológica del BCU](https://www.bcu.gub.uy/Comunicados/Anexo%201%20-%20Nota%20metodologica%20V2.pdf) |

Calendario construido para esta guía a partir de la documentación de Compliance Manager y de Defender for Cloud citada en cada fila y de la práctica de supervisión basada en evidencia del BCU. Ajusta frecuencias y responsables a tu organización.

<a id="formato"></a>

## El formato Ninja: historia y familia

El Ninja oficial, **Microsoft Purview Compliance Manager (MSPCM) Ninja Training**, se publicó en el blog de seguridad de Tech Community el 18 de febrero de 2022, firmado por garyasp (Microsoft), y su versión «Q1 2023» se actualizó por última vez el 27 de febrero de 2023 ([Ninja oficial](https://techcommunity.microsoft.com/blog/microsoft-security-blog/microsoft-purview-compliance-manager-mspcm-ninja-training-q1-2023/3181322)). Se organizaba en Welcome/Introduction y tres niveles —**Basic** (el lugar de Compliance Manager en el ecosistema de Microsoft 365 y un recorrido por la herramienta), **Intermediate** (plantillas y sus actualizaciones; extender, modificar y crear plantillas; acciones de mejora) y **Advanced** (reportes, Configuration Analyzer for Microsoft Purview —antes MCCA—, diferencias entre puntuación de cumplimiento y Secure Score y escenarios avanzados)—, más una sección de **New Features**.

Cada nivel y la sección de novedades cerraban con un knowledge check. Quien lo aprobaba pedía un certificado no oficial («fun certificate») en un portal de atestación y lo recibía por correo en tres a cinco días hábiles, con la aclaración de que no era una certificación de Microsoft; varios comentarios en la publicación reportan knowledge checks inaccesibles. El contenido sigue siendo útil para los conceptos, pero no cubre la multinube actual, las plantillas de IA, las plantillas generadas desde PDF ni el portal unificado. La familia de Purview creció con Ninja de Communication Compliance, Insider Risk, eDiscovery, ciclo de vida y registros y Priva, y hoy migra hacia rutas de Learn con insignia, como los [escenarios Ninja de Information Protection y DLP](https://learn.microsoft.com/en-us/training/paths/purview-ninja-safeguard-data/).

Esta edición respeta la forma Ninja —módulos con introducción, recursos curados, práctica y evaluación— y agrega lo que un equipo de GRC necesita en 2026: licencias precisas, plantillas propias y generadas con IA, multinube, cumplimiento para IA, reportes para la dirección, automatización con sus límites reales, mapeo entre marcos, un programa de cumplimiento continuo, un track de operación y el panorama normativo de MCSA, siempre como referencia y no como asesoría legal.

**La familia Ninja relacionada**

| Ninja | Qué cubre | Estado y última actualización |
|---|---|---|
| [Microsoft Purview Compliance Manager (MSPCM) Ninja Training Q1 2023](https://techcommunity.microsoft.com/blog/microsoft-security-blog/microsoft-purview-compliance-manager-mspcm-ninja-training-q1-2023/3181322) | Basic, Intermediate y Advanced (plantillas, acciones de mejora, reportes, Configuration Analyzer y puntuación frente a Secure Score) y New Features, con knowledge check por nivel | Legado aún útil: publicado el 18 de febrero de 2022 y actualizado por última vez el 27 de febrero de 2023 |
| [Become a Communication Compliance Ninja](https://techcommunity.microsoft.com/blog/microsoft-security-blog/become-a-communication-compliance-ninja/3283283) | Políticas, revisión e integraciones de Communication Compliance | Legado aún útil (abril de 2022, actualizado en junio de 2023) |
| [Become an Insider Risk Management Ninja](https://techcommunity.microsoft.com/t5/security-compliance-and-identity/become-an-insider-risk-management-ninja/ba-p/3282306) | Riesgo interno: políticas, alertas, casos y knowledge checks por sección | Legado aún útil (abril de 2022; última actualización conocida en septiembre de 2024) |
| [Become a Microsoft Purview eDiscovery Ninja](https://techcommunity.microsoft.com/blog/microsoft-security-blog/become-a-microsoft-purview-ediscovery-ninja/2793108) | eDiscovery unificado: permisos, retenciones, búsqueda, conjuntos de revisión y exportación | Vigente; actualizado el 5 de mayo de 2026 según el [índice de Tech Community](https://techcommunity.microsoft.com/tag/ninja%20training) |
| [Data Lifecycle and Records Management Ninja (anuncio)](https://techcommunity.microsoft.com/discussions/microsoft-security/new-blog--become-a-microsoft-purview-data-lifecycle-and-records-management-ninja/3883998) | Retención, etiquetas, plan de archivos y disposición | Legado aún útil (25 de julio de 2023) |
| [Become a Microsoft Priva Ninja](https://techcommunity.microsoft.com/blog/microsoft-security-blog/become-a-microsoft-priva-ninja/3876888) | Privacy Risk Management y solicitudes de derechos de los titulares | Legado aún útil (julio de 2023); revisa el estado actual de Priva |
| [Escenarios Ninja de Purview en Learn](https://learn.microsoft.com/en-us/training/paths/purview-ninja-safeguard-data/) | Information Protection y DLP en cinco escenarios, con evaluación por módulo e insignia | Vigente; es el formato hacia el que migra la familia y tiene versión en español |
| [Defender for Cloud Ninja](https://kurtsh.com/2024/02/24/training-updated-microsoft-defender-for-cloud-ninja-training/) | Defender for Cloud, incluido el cumplimiento normativo que alimenta la multinube de Compliance Manager | Actualizado en febrero de 2024; knowledge check de 30 preguntas |
| [Índice comunitario de Ninja Training](https://github.com/peterschmidtdk/Microsoft-Ninja-Training/blob/main/README.md) | URL de toda la familia Ninja, incluida Compliance Manager | Actualizado el 27 de febrero de 2026 |

**Del Ninja oficial a esta edición**

| Ninja oficial (Q1 2023) | Contenido | En esta edición |
|---|---|---|
| Welcome / Introduction | Presentación, cómo usar el entrenamiento y certificado | [I0](01_Nivel_1_Inicial.md#i0) |
| Basic · Compliance Manager en el ecosistema de Microsoft 365 | Dónde encaja en Purview y en la responsabilidad compartida | [P0](01_Nivel_1_Inicial.md#p0), [I1](01_Nivel_1_Inicial.md#i1) |
| Basic · Recorrido por la herramienta | Panel, puntuación, evaluaciones, acciones y regulaciones | [I1](01_Nivel_1_Inicial.md#i1), [I2](01_Nivel_1_Inicial.md#i2) |
| Intermediate · Plantillas y sus actualizaciones | Biblioteca de plantillas y actualizaciones pendientes | [I2](01_Nivel_1_Inicial.md#i2), [A3](03_Nivel_3_Avanzado.md#a3) |
| Intermediate · Extender, modificar y crear plantillas | Plantillas propias y personalizadas | [M1](02_Nivel_2_Intermedio.md#m1) |
| Intermediate · Acciones de mejora | Implementación, pruebas y evidencias | [I3](01_Nivel_1_Inicial.md#i3) |
| Advanced · Reportes | Exportación e informes para auditores y dirección | [M4](02_Nivel_2_Intermedio.md#m4), [O2](04_Nivel_4_Operacion.md#o2) |
| Advanced · Configuration Analyzer for Microsoft Purview (antes MCCA) | Análisis de configuración; la investigación de 2026 no encontró documentación vigente (ver puntos a confirmar) | [A1](03_Nivel_3_Avanzado.md#a1) |
| Advanced · Puntuación de cumplimiento frente a Secure Score | Diferencias y uso de cada métrica | [O2](04_Nivel_4_Operacion.md#o2), [M4](02_Nivel_2_Intermedio.md#m4) |
| Advanced · Escenarios avanzados | Casos de uso avanzados | [A2](03_Nivel_3_Avanzado.md#a2), [A3](03_Nivel_3_Avanzado.md#a3) |
| New Features | Novedades de la época | [I0](01_Nivel_1_Inicial.md#i0), [C2](05_Comunidad.md#c2) |
| Nuevo en esta edición | Multinube y Defender for Cloud, cumplimiento para IA, automatización y APIs, mapeo entre marcos, normativa de MCSA, modelo operativo, gobierno y comunidad | [M2](02_Nivel_2_Intermedio.md#m2), [M3](02_Nivel_2_Intermedio.md#m3), [A1](03_Nivel_3_Avanzado.md#a1), [A2](03_Nivel_3_Avanzado.md#a2), [A4](03_Nivel_3_Avanzado.md#a4), [O1](04_Nivel_4_Operacion.md#o1), [O3](04_Nivel_4_Operacion.md#o3), [C1](05_Comunidad.md#c1) |

**Recursos sobre el Ninja oficial y su familia**

- [Microsoft Purview Compliance Manager (MSPCM) Ninja Training: Q1 2023](https://techcommunity.microsoft.com/blog/microsoft-security-blog/microsoft-purview-compliance-manager-mspcm-ninja-training-q1-2023/3181322) · Curso · Empleado de Microsoft · Legado aún útil · garyasp · Microsoft Tech Community (Microsoft Security Community Blog) · 27 feb 2023. Ninja oficial de Compliance Manager con tres niveles (básico, intermedio y avanzado) más una sección de novedades, cada uno con video, documentación y knowledge check, y certificado no oficial vía portal de atestación. *Nota:* Publicado 18-feb-2022, última actualización 27-feb-2023 (versión 6.0); no cubre multinube actual, plantillas de IA, plantillas por PDF ni el portal unificado de Purview; varios comentarios reportan knowledge checks inaccesibles
- [Secure sensitive data with Microsoft Purview Ninja training scenarios](https://learn.microsoft.com/en-us/training/paths/purview-ninja-safeguard-data/) · Curso · Oficial · Microsoft Learn. Ruta de aprendizaje oficial «Ninja» de Purview en Microsoft Learn (Information Protection + DLP) con cinco escenarios reales, evaluaciones por módulo y una insignia al completar; es la evolución del formato Ninja hacia Learn.
- [Become a Microsoft Priva Ninja](https://techcommunity.microsoft.com/blog/microsoft-security-blog/become-a-microsoft-priva-ninja/3876888) · Curso · Empleado de Microsoft · Legado aún útil · John_Wirtala1608 · Microsoft Tech Community (Microsoft Security Community Blog) · 18 jul 2023. Ninja de Microsoft Priva (privacidad) organizado en niveles principiante, intermedio y avanzado para Privacy Risk Management y Subject Rights Requests; complementa a Compliance Manager en el frente de privacidad. *Nota:* Julio de 2023; revisar el estado actual de Priva antes de usarlo
- [Become a Communication Compliance Ninja](https://techcommunity.microsoft.com/blog/microsoft-security-blog/become-a-communication-compliance-ninja/3283283) · Curso · Empleado de Microsoft · Legado aún útil · Patrick_David · Microsoft Tech Community (Microsoft Security Community Blog) · 19 abr 2022. Ninja hermano de la familia Purview (Communication Compliance) con leyenda de tipos de recurso, knowledge checks al final de cada sección y promesa de actualización semestral. *Nota:* Publicado 19-abr-2022, actualizado en junio de 2023; útil como referencia del formato de la familia Ninja de Purview

<a id="cambios"></a>

## Qué cambió y por qué importa

Cada fila remite al módulo donde se explica en detalle.

| Tema | Antes (Ninja oficial y documentación de 2022 a 2024) | Ahora (noviembre de 2026) | Módulo |
|---|---|---|---|
| Portal | Portal de cumplimiento clásico | Portal de Microsoft Purview (GA en julio de 2024); el clásico se retiró entre el 14 de noviembre y el 14 de diciembre de 2024 | [P0](01_Nivel_1_Inicial.md#p0) |
| Nombre de la licencia | Microsoft 365 E5 Compliance | Microsoft Purview Suite desde el 1 de octubre de 2025, sin cambios de funciones ni de precio | [P0](01_Nivel_1_Inicial.md#p0), [I1](01_Nivel_1_Inicial.md#i1) |
| Plantillas premium incluidas en E5 | Conjunto fijo, con NIST 800-53, ISO 27001 y GDPR incluidas | Tres plantillas premium a elección (desde diciembre de 2022); las familias cuentan como una y el resto se compra por plantilla y por un año | [I1](01_Nivel_1_Inicial.md#i1) |
| Biblioteca de plantillas | «Más de 350 regulaciones» (video de Microsoft Mechanics) | Más de 360 plantillas en cuatro agrupaciones, incluidas las premium de IA y la preparación previa al despliegue | [I2](01_Nivel_1_Inicial.md#i2) |
| Prueba premium | Documentada para el portal clásico (2024) | 25 plantillas durante 90 días, una vez por inquilino, en el portal de Purview | [I2](01_Nivel_1_Inicial.md#i2) |
| Plantillas propias | Extender, modificar o crear plantillas a mano | Copia personalizada (vista previa), plantilla en blanco o generada desde el PDF de la norma con IA (vista previa desde noviembre de 2025; GA en octubre de 2026) | [M1](02_Nivel_2_Intermedio.md#m1) |
| Normas de MCSA sin plantilla | Planillas paralelas | Plantilla generada desde el PDF oficial (por ejemplo, Ley 21.719 o Decreto 295 de Chile) | [M1](02_Nivel_2_Intermedio.md#m1), [A4](03_Nivel_3_Avanzado.md#a4) |
| Multinube | No cubierta por el Ninja oficial | Microsoft 365, Azure, AWS y GCP en una evaluación con Defender for Cloud; conectores para Salesforce y Zoom | [M2](02_Nivel_2_Intermedio.md#m2) |
| IA | No existía | Cuatro plantillas premium de IA, evaluación base de Microsoft 365 Copilot y Copilot Chat y evaluaciones automáticas de agentes de Microsoft Foundry | [M3](02_Nivel_2_Intermedio.md#m3) |
| Apps de IA de terceros | No existía | ChatGPT Enterprise, Gemini y DeepSeek; Anthropic Claude Enterprise desde agosto de 2026 | [M3](02_Nivel_2_Intermedio.md#m3) |
| Plataforma de agentes | Azure AI Foundry (nombre anterior) | Microsoft Foundry; Purview para agentes de Foundry y apps conectadas a Entra se soportará con Microsoft 365 E7 y Agent 365 | [M3](02_Nivel_2_Intermedio.md#m3) |
| Microsoft 365 E7 | No existía | E5 más Microsoft 365 Copilot, Agent 365 y Entra Suite (GA el 1 de mayo de 2026); Learn no aclara si hereda los cupos premium | [I1](01_Nivel_1_Inicial.md#i1) |
| Mapeo entre marcos | Acciones compartidas por grupo | Además, controles relacionados en la preparación previa al despliegue (vista previa, sin licencia) | [A2](03_Nivel_3_Avanzado.md#a2) |
| Alertas | Alert policies en el portal clásico | Policies y Alerts en la navegación del portal, cinco tipos de evento y una política predeterminada de cambio de puntuación | [A3](03_Nivel_3_Avanzado.md#a3) |
| Reportes | Exportación del informe de evaluación | Además, informes de postura de Purview (vista previa, 30 días, PDF) | [M4](02_Nivel_2_Intermedio.md#m4) |
| APIs y automatización | Sin API pública para la puntuación (consultas de 2021) | Sigue sin API de extracción: las APIs de Purview en Graph sirven para enviar contenido y aplicar políticas; exportación continua de Defender for Cloud para la infraestructura | [A1](03_Nivel_3_Avanzado.md#a1) |
| Roles | Asignaciones permanentes | Asignaciones de grupos de roles de Purview con expiración de un día a dos años (julio de 2026) | [O1](04_Nivel_4_Operacion.md#o1) |
| Puntuación frente a Secure Score | El Ninja pedía distinguirlas | Sigue vigente: se reportan por separado y con fecha de corte | [O2](04_Nivel_4_Operacion.md#o2) |
| Credenciales | SC-400 y certificado no oficial del Ninja | SC-400 retirado el 31 de mayo de 2025; SC-900 (habilidades al 21 de octubre de 2026) es la que evalúa Compliance Manager | [I0](01_Nivel_1_Inicial.md#i0) |
| Normativa de privacidad en MCSA | Leyes de datos anteriores | Nueva LFPDPPP (20 de marzo de 2025), Ley 21.719 de Chile (vigente desde el 1 de diciembre de 2026), nuevo reglamento en Perú y Ley 7593/2025 de Paraguay | [A4](03_Nivel_3_Avanzado.md#a4), [O3](04_Nivel_4_Operacion.md#o3) |
| Ciberseguridad y sector financiero en MCSA | Reglas de reporte heterogéneas | Decreto 295 de Chile (3 h), Comunicación «A» 8280 del BCRA (1 h), leyes de ciberseguridad de Ecuador (2026) y Guatemala (aprobada en noviembre de 2026) | [A4](03_Nivel_3_Avanzado.md#a4), [A3](03_Nivel_3_Avanzado.md#a3) |

<a id="rutas"></a>

## Rutas por rol

Las horas son estimaciones de lectura y práctica.

- **Gestor de cumplimiento o GRC** (~61 h). Dueño del programa: elige normas y cupos, administra evaluaciones y plantillas y reporta a la dirección. Módulos: [P0](01_Nivel_1_Inicial.md#p0), [I0](01_Nivel_1_Inicial.md#i0), [I1](01_Nivel_1_Inicial.md#i1), [I2](01_Nivel_1_Inicial.md#i2), [I3](01_Nivel_1_Inicial.md#i3), [M1](02_Nivel_2_Intermedio.md#m1), [M2](02_Nivel_2_Intermedio.md#m2), [M3](02_Nivel_2_Intermedio.md#m3), [M4](02_Nivel_2_Intermedio.md#m4), [A1](03_Nivel_3_Avanzado.md#a1), [A2](03_Nivel_3_Avanzado.md#a2), [A3](03_Nivel_3_Avanzado.md#a3), [A4](03_Nivel_3_Avanzado.md#a4), [O1](04_Nivel_4_Operacion.md#o1), [O2](04_Nivel_4_Operacion.md#o2), [O3](04_Nivel_4_Operacion.md#o3).
- **Auditor interno** (~35 h). Prueba controles de forma independiente, valida evidencias y usa los informes como papeles de trabajo. Módulos: [P0](01_Nivel_1_Inicial.md#p0), [I0](01_Nivel_1_Inicial.md#i0), [I1](01_Nivel_1_Inicial.md#i1), [I3](01_Nivel_1_Inicial.md#i3), [M1](02_Nivel_2_Intermedio.md#m1), [M4](02_Nivel_2_Intermedio.md#m4), [A2](03_Nivel_3_Avanzado.md#a2), [A3](03_Nivel_3_Avanzado.md#a3), [O1](04_Nivel_4_Operacion.md#o1), [O2](04_Nivel_4_Operacion.md#o2).
- **Dueño de controles de TI y seguridad** (~25 h). Implementa acciones de mejora en Microsoft 365 y aporta la evidencia técnica. Módulos: [P0](01_Nivel_1_Inicial.md#p0), [I1](01_Nivel_1_Inicial.md#i1), [I3](01_Nivel_1_Inicial.md#i3), [M3](02_Nivel_2_Intermedio.md#m3), [A1](03_Nivel_3_Avanzado.md#a1), [A3](03_Nivel_3_Avanzado.md#a3), [O1](04_Nivel_4_Operacion.md#o1).
- **Dueño de controles de nube** (~23 h). Lleva los controles de Azure, AWS y GCP a las evaluaciones con Defender for Cloud. Módulos: [P0](01_Nivel_1_Inicial.md#p0), [I1](01_Nivel_1_Inicial.md#i1), [I3](01_Nivel_1_Inicial.md#i3), [M2](02_Nivel_2_Intermedio.md#m2), [A1](03_Nivel_3_Avanzado.md#a1), [A2](03_Nivel_3_Avanzado.md#a2).
- **Oficial de privacidad** (~33 h). Valida acciones y evidencias que tocan datos personales y sigue la normativa de privacidad de la región. Módulos: [P0](01_Nivel_1_Inicial.md#p0), [I1](01_Nivel_1_Inicial.md#i1), [I2](01_Nivel_1_Inicial.md#i2), [M1](02_Nivel_2_Intermedio.md#m1), [M3](02_Nivel_2_Intermedio.md#m3), [A4](03_Nivel_3_Avanzado.md#a4), [O1](04_Nivel_4_Operacion.md#o1), [O3](04_Nivel_4_Operacion.md#o3).
- **Comité de riesgos o CISO** (~28 h). Decide cupos, prioridades y aceptación de riesgos con reportes defendibles. Módulos: [I1](01_Nivel_1_Inicial.md#i1), [I2](01_Nivel_1_Inicial.md#i2), [M3](02_Nivel_2_Intermedio.md#m3), [M4](02_Nivel_2_Intermedio.md#m4), [A4](03_Nivel_3_Avanzado.md#a4), [O2](04_Nivel_4_Operacion.md#o2), [O3](04_Nivel_4_Operacion.md#o3).

<a id="plan"></a>

## Plan de entrenamiento sugerido

Calendario de referencia de 13 semanas para una dedicación de 3 a 7 horas por semana (unas 63 horas). Cada semana deja un entregable verificable; las evaluaciones cierran las semanas 4, 8, 11 y 13. Si tu rol tiene una ruta propia, recorre solo sus módulos y conserva el orden.

| Semana | Módulos | Foco | Entregable |
|---|---|---|---|
| 1 | [P0](01_Nivel_1_Inicial.md#p0), [I0](01_Nivel_1_Inicial.md#i0) | Purview, el portal, los roles y el Service Trust Portal; cómo aprender | Inquilino de práctica con Compliance Manager abierto, convención de nombres y matriz de habilidades de SC-900 |
| 2 | [I1](01_Nivel_1_Inicial.md#i1) | Puntuación, evaluaciones, roles y licencias | Ficha de licencias y explicación de la puntuación con tus puntos y los de Microsoft |
| 3 | [I2](01_Nivel_1_Inicial.md#i2) | Plantillas regulatorias, cupos premium y prueba de 90 días | Matriz de decisión de cupos y evaluaciones ISO/IEC 27001 y NIST CSF 2.0 en un grupo de prueba |
| 4 | [I3](01_Nivel_1_Inicial.md#i3), [C2](05_Comunidad.md#c2) | Acciones de mejora y evidencias; recursos en español | Ciclo exportar–actualizar–cargar completado y guía de evidencia aceptable; evaluación del nivel 1 aprobada |
| 5 | [M1](02_Nivel_2_Intermedio.md#m1) | Plantillas propias: copia, en blanco y desde PDF | Plantilla publicada de una norma local sin plantilla, con revisión documentada |
| 6 | [M2](02_Nivel_2_Intermedio.md#m2) | Multinube con Defender for Cloud y conectores | Evaluación con Microsoft 365 y una suscripción de Azure y estimación de costos |
| 7 | [M3](02_Nivel_2_Intermedio.md#m3) | Cumplimiento para IA | Evaluación de IA con evidencias de DSPM y matriz de la Ley 31814 de Perú |
| 8 | [M4](02_Nivel_2_Intermedio.md#m4), [C1](05_Comunidad.md#c1) | Reportes para la dirección; referentes | Informe ejecutivo de una página y tablero con Secure Score separado; evaluación del nivel 2 aprobada |
| 9 | [A1](03_Nivel_3_Avanzado.md#a1), [A2](03_Nivel_3_Avanzado.md#a2) | Automatización con sus límites y mapeo entre marcos | Procedimiento de exportación mensual y mapa de controles de al menos ocho dominios |
| 10 | [A3](03_Nivel_3_Avanzado.md#a3) | Programa de cumplimiento continuo | Políticas de alertas activas y calendario anual con dueños y evidencias |
| 11 | [A4](03_Nivel_3_Avanzado.md#a4) | Normativa de la región | Inventario de normas aplicables con su enfoque y tabla de plazos para el SOC; evaluación del nivel 3 aprobada |
| 12 | [O1](04_Nivel_4_Operacion.md#o1), [O2](04_Nivel_4_Operacion.md#o2) | Modelo operativo e indicadores | Matriz RACI, roles con expiración y tablero de diez indicadores |
| 13 | [O3](04_Nivel_4_Operacion.md#o3) | Gobierno, privacidad y normativa en MCSA | Procedimiento de vigilancia normativa y resumen para el comité; evaluación del track de operación y reto final |

<a id="laboratorio"></a>

## Tu laboratorio

**Tu entorno.** Una prueba de Microsoft 365 E5 (un mes, 25 licencias) incluye Compliance Manager con la Data Protection Baseline y, como inquilino E5, debería permitir elegir tres plantillas premium: verifícalo en el contador de licencias de la página Regulations. La [prueba de evaluaciones premium](https://learn.microsoft.com/en-us/purview/purview-compliance-manager-assessments-trial) suma 25 plantillas por 90 días, pero es única por inquilino: actívala cuando tengas listo el plan de ejercicios de I2, M1, M3 y A2. Si tu organización parte de E3, la [prueba de Microsoft Purview Suite](https://learn.microsoft.com/en-us/purview/purview-trial) sirve para practicar en producción. Suma una suscripción de Azure con los créditos de Visual Studio Enterprise para Defender for Cloud y Microsoft Foundry; el detalle está en el anexo común de entorno de práctica.

**Datos y nombres de práctica.** Trabaja con evidencias sintéticas —documentos ficticios y capturas de configuración del laboratorio— y nunca con datos personales ni de clientes. Usa el prefijo `PRUEBA-CM-` en evaluaciones, grupos y plantillas, y crea grupos de evaluaciones separados para practicar: un grupo no se puede cambiar después y las acciones técnicas impactan todos los grupos.

**Qué no se puede practicar en el laboratorio.** Conectores con Salesforce o Zoom reales, un programa de cumplimiento continuo con dueños y auditores reales, la renovación de licencias premium, las evaluaciones de IA gratuitas que dependen de licencias pagas de Copilot o de agentes, los estándares no predeterminados de Defender for Cloud sin un plan pago y, sobre todo, la realidad regulatoria de una entidad supervisada. Para esos casos, cada ejercicio `[SOLO-PRODUCCION]` describe cómo practicar de forma segura.

**Costos a vigilar.** Compliance Manager no figura entre las capacidades de [pago por uso de Purview](https://learn.microsoft.com/en-us/purview/purview-payg-subscription-based-enablement): los costos del laboratorio están en Azure, con los planes pagos de Defender for Cloud que exigen los estándares no predeterminados ([precios](https://azure.microsoft.com/en-us/pricing/details/defender-for-cloud/)), el cómputo de Microsoft Foundry, la ingesta en Log Analytics si usas la exportación continua y tus cuentas de AWS o GCP. Configura presupuesto y alertas al 50, 75 y 90 % antes de empezar. Y no compres plantillas premium en el laboratorio: la licencia dura un año y se renueva sola.

**Práctica en producción.** Usa el rol Reader por evaluación para estudiar y grupos piloto para probar, exporta el informe antes de aceptar cualquier actualización de plantilla, no cargues evidencias con datos personales y no copies plantillas premium «para probar»: consume la licencia y la copia no se puede eliminar. Ante cualquier decisión regulatoria, involucra a Legal y privacidad.

**Limpieza.** Exporta los informes y borra las evaluaciones de práctica, revoca los roles temporales, quita los estándares asignados y desactiva los planes pagos de Defender for Cloud, elimina el proyecto de Foundry y la exportación continua, y desconecta las cuentas de AWS o GCP. Las regulaciones copiadas no se pueden eliminar: por eso conviene hacer las copias solo en el inquilino de laboratorio.

La matriz de qué se puede practicar en el laboratorio y qué solo en producción está en [07_Laboratorio_y_practica_en_produccion.md](07_Laboratorio_y_practica_en_produccion.md). La guía para construir el entorno está en el [anexo común](../Anexo_Entorno_de_practica.md).

<a id="mapa"></a>

## Mapa de módulos

- **Nivel 1 · Inicial:** [P0 Purview y el portal](01_Nivel_1_Inicial.md#p0) · [I0 Cómo aprender](01_Nivel_1_Inicial.md#i0) · [I1 Puntuación y licencias](01_Nivel_1_Inicial.md#i1) · [I2 Plantillas regulatorias](01_Nivel_1_Inicial.md#i2) · [I3 Acciones y evidencias](01_Nivel_1_Inicial.md#i3)
- **Nivel 2 · Intermedio:** [M1 Evaluaciones personalizadas](02_Nivel_2_Intermedio.md#m1) · [M2 Multinube y Defender for Cloud](02_Nivel_2_Intermedio.md#m2) · [M3 Cumplimiento para IA](02_Nivel_2_Intermedio.md#m3) · [M4 Reportes para la dirección](02_Nivel_2_Intermedio.md#m4)
- **Nivel 3 · Avanzado:** [A1 Automatización y APIs](03_Nivel_3_Avanzado.md#a1) · [A2 Mapeo de controles](03_Nivel_3_Avanzado.md#a2) · [A3 Cumplimiento continuo](03_Nivel_3_Avanzado.md#a3) · [A4 Normativa regional](03_Nivel_3_Avanzado.md#a4)
- **Nivel 4 · Operación:** [O1 Modelo operativo](04_Nivel_4_Operacion.md#o1) · [O2 Métricas y mejora continua](04_Nivel_4_Operacion.md#o2) · [O3 Gobierno y normativa MCSA](04_Nivel_4_Operacion.md#o3)
- **Comunidad:** [C1 Referentes y libros](05_Comunidad.md#c1) · [C2 Español y actualización](05_Comunidad.md#c2)

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. No constituye asesoría legal: la normativa citada es material de referencia y las decisiones de aplicabilidad corresponden a tus áreas de Legal, privacidad y, cuando aplique, RR. HH. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

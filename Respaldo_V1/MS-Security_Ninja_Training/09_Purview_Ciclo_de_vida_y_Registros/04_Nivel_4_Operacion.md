# Nivel 4 · Operación · Programa, métricas y gobierno

*Microsoft Purview Ciclo de vida de los datos y Gestión de registros Ninja Training · Edición 2026*

[← Nivel 3 · Avanzado](03_Nivel_3_Avanzado.md) · [Índice del programa](README.md) · [Comunidad →](05_Comunidad.md)

<a id="operacion"></a>

Modelo operativo y separación de funciones, métricas y mejora continua, y gobierno con Legal y privacidad frente a la normativa de MCSA. Terminas con un programa de registros que puedes defender ante un comité o una auditoría.

*L300–L400 · 3 módulos · ~9 horas · 6 recursos*

**Módulos de este nivel:** [O1 Modelo operativo](#o1) · [O2 Métricas y mejora continua](#o2) · [O3 Gobierno y normativa MCSA](#o3)

<a id="o1"></a>

## O1 · Modelo operativo del equipo y responsabilidades

*L300–L400 · ~3 h · Origen: Nuevo en esta edición*

La gestión de registros es un programa, no una configuración. La norma ISO 15489-1:2016, confirmada en 2021, ordena sus elementos: políticas, responsabilidades, valoración, controles y autoridades de disposición. En la práctica, eso significa nombres y apellidos: el gestor de registros es dueño del plan de archivos; los dueños de datos definen qué es un registro en su área; Legal administra los holds e interpreta la norma; privacidad vela por la minimización; cumplimiento traduce obligaciones en controles; y los administradores de Exchange, SharePoint y Teams implementan.

En Purview, la separación de funciones se construye con grupos de roles: Records Management para diseñar, un grupo personalizado de revisores con el rol Disposition Management y la limpieza prioritaria con aprobadores distintos; desde julio de 2026, además, las asignaciones pueden vencer. La comunidad aporta lecciones valiosas: un programa global pasó de más de 5.000 categorías a 180 tipos de registro y reservó la revisión de eliminación para unos 10.

**Por qué importa**

Sin dueños claros, la retención termina en «guardar todo» o en eliminaciones improvisadas. La separación de funciones impide que una sola persona elimine registros y es lo primero que pide un auditor. Una tabla de retención simplificada mejora la precisión del etiquetado y reduce el trabajo de revisión.

**Qué vas a lograr**

- Definir una matriz RACI para registros, retención, holds, eventos y limpieza prioritaria.
- Configurar grupos de roles que separen diseño, revisión, aprobación y auditoría.
- Simplificar una tabla de retención en tipos de registro manejables.
- Establecer el ciclo de cambios y revisiones periódicas del programa.

> **Consejo Ninja.** Separa funciones con grupos de roles: Records Management para el diseño, un grupo personalizado «Disposition Reviewers» con el rol Disposition Management para la revisión y la limpieza prioritaria con aprobadores distintos ([eliminación](https://learn.microsoft.com/en-us/purview/disposition)). Desde julio de 2026, además, las asignaciones pueden vencer ([novedades](https://learn.microsoft.com/en-us/purview/whats-new)).

> **Consejo Ninja.** Un caso de la comunidad muestra el valor de simplificar: un programa global pasó de más de 5.000 categorías a 180 tipos de registro y usó la revisión de eliminación solo como excepción, en unos 10 tipos ([guía de Nikki Chapple, actualizada en mayo de 2026](https://nikkichapple.com/microsoft-purview-records-management-guide/)). Menos categorías significa un etiquetado más preciso y menos trabajo de revisión.

> **Novedad.** En 2026, Joanne Klein publica la serie «Retention Schedule Hot Spots» sobre los puntos críticos al llevar una tabla de retención real a Purview: número de series, disparadores de eventos, registros con revisión de eliminación y etiquetas en carpetas y conjuntos de documentos ([serie](https://joannecklein.com/category/microsoft-purview/)). Úsala para preparar las conversaciones con archivo y Legal.

> **Atención.** La norma ISO 15489-1:2016, confirmada en 2021, define los conceptos y principios de la gestión de registros —políticas, responsabilidades, valoración, controles y autoridades de disposición— ([ISO 15489-1](https://www.iso.org/standard/62542.html)). Es un marco de gestión, no una configuración de Purview: tradúcela a roles, procedimientos y evidencias.

**¿Tienes poco tiempo?**

- [Mastering Records Management in Microsoft Purview: A Practical Guide for AI-Ready Governance](https://nikkichapple.com/microsoft-purview-records-management-guide/) · Blog
- [Retention Schedule Hot Spots Blog Series for Purview (categoría Microsoft Purview)](https://joannecklein.com/category/microsoft-purview/) · Blog
- [ISO 15489-1:2016 Information and documentation — Records management — Part 1: Concepts and principles](https://www.iso.org/standard/62542.html) · Documentación

**Matriz RACI de ejemplo para el programa de registros**

| Actividad | Gestor de registros | Legal | Privacidad | Cumplimiento | Administradores de Microsoft 365 | Dueños de datos |
|---|---|---|---|---|---|---|
| Mantener el plan de archivos y las etiquetas | R/A | C | C | C | I | C |
| Aprobar períodos, disparadores y tipos de registro | R | A | C | C | I | C |
| Configurar directivas, ámbitos y autoaplicación | A | I | I | C | R | I |
| Disparar y conciliar eventos (fin de contrato, baja) | A | I | I | I | C | R |
| Revisar y aprobar eliminaciones | A | C | C | I | I | R |
| Colocar y liberar holds de eDiscovery | C | R/A | C | I | C | I |
| Aprobar una limpieza prioritaria (tres aprobaciones) | R (administrador de retención) | R (administrador de eDiscovery) | C | A | R (administrador de limpieza prioritaria) | I |
| Definir la retención de interacciones con IA | R | C | A | C | R | I |
| Medir y reportar el programa | R | I | I | A | C | I |

Ejemplo didáctico (R: responsable; A: aprueba y rinde cuentas; C: consultado; I: informado), basado en la separación de funciones de [revisión de eliminación](https://learn.microsoft.com/en-us/purview/disposition) y [limpieza prioritaria](https://learn.microsoft.com/en-us/purview/priority-cleanup-exchange) y en los elementos de [ISO 15489-1](https://www.iso.org/standard/62542.html). Ajústalo con tu comité de retención.

### Documentación, cursos y credenciales

- [ISO 15489-1:2016 Information and documentation — Records management — Part 1: Concepts and principles](https://www.iso.org/standard/62542.html) · Documentación · Comunidad · ISO/TC 46/SC 11 · ISO · abr 2016. Norma internacional de conceptos y principios de gestión de registros (políticas, responsabilidades, valoración, controles, autoridades de disposición), revisada y confirmada en 2021.

### Comunidad: blogs, libros, newsletters y eventos

- [Retention Schedule Hot Spots Blog Series for Purview (categoría Microsoft Purview)](https://joannecklein.com/category/microsoft-purview/) · Blog · MVP · Nuevo · Joanne Klein · joannecklein.com · 13 ago 2026. Serie práctica 2026 sobre puntos críticos al mapear calendarios de retención (número de series, disparadores de eventos, registros con revisión de eliminación) y etiquetas en carpetas y conjuntos de documentos.
- [Mastering Records Management in Microsoft Purview: A Practical Guide for AI-Ready Governance](https://nikkichapple.com/microsoft-purview-records-management-guide/) · Blog · MVP · Nikki Chapple · nikkichapple.com · 9 sep 2025. Resumen de un episodio del podcast All Things M365 Compliance con lecciones de un programa global (de más de 5.000 categorías a 180 tipos de registro) y uso de revisión de eliminación solo como excepción.

**Manos a la obra**

1. `Laboratorio` Arma la matriz RACI de tu programa a partir de la tabla de este módulo: plan de archivos, publicación y autoaplicación de etiquetas, eventos, revisión de eliminación, holds, limpieza prioritaria, buzones inactivos e IA, con nombres y suplentes. Evidencia: RACI aprobada por el sponsor del programa.
2. `Laboratorio` Configura en el laboratorio los grupos de roles que exige tu RACI, con cuentas distintas y fecha de expiración: uno de diseño sin Disposition Management, uno de revisores con ese rol y uno de solo lectura para auditoría; comprueba que el revisor no puede editar etiquetas ([permisos de Purview](https://learn.microsoft.com/en-us/purview/purview-permissions)). Evidencia: capturas de las asignaciones y de los intentos denegados.
3. `Laboratorio` Simplifica una tabla de retención (real o pública) de más de 50 series en no más de 15 tipos de registro, justificando cada agrupación y marcando dónde hace falta revisión de eliminación. Evidencia: tabla de equivalencias revisada por el área de archivo.
4. `Laboratorio` Define el ciclo de cambios del plan de archivos: solicitud, análisis de impacto, aprobación de Legal y privacidad, prueba en el laboratorio, despliegue, comunicación y revisión anual. Evidencia: procedimiento publicado y una solicitud de cambio de ejemplo cerrada.
5. `Solo producción` Pon en marcha el modelo operativo con las áreas reales. Cómo hacerlo seguro: empieza por un área piloto, asigna los roles con fecha de expiración y de solo lectura a quienes observan, y no habilites eliminaciones hasta que la RACI, el procedimiento de cambios y el comité estén aprobados. Evidencia: acta de arranque y asignaciones vigentes revisadas a los 30 días.

<a id="o2"></a>

## O2 · Métricas, reportes y mejora continua

*L300–L400 · ~3 h · Origen: Ninja oficial de ciclo de vida y registros (2023): monitoreo, ampliado a métricas de programa*

Lo que no se mide se acumula. Un tablero útil cubre cuatro frentes: **cobertura** (ubicaciones con directiva de base, sitios con etiqueta predeterminada, porcentaje de contenido etiquetado por categoría), **eliminación** (elementos pendientes de revisión y su antigüedad, prueba de eliminación exportada), **eventos** (registros cuyo evento no se registró y quedan retenidos indefinidamente) y **costo** (crecimiento de bibliotecas de conservación y archivos, pago por uso de IA y Microsoft 365 Archive).

Las fuentes están a mano: la página de eliminación exporta pendientes y eliminados; la auditoría registra la limpieza prioritaria por su ID; PowerShell y Graph listan directivas, etiquetas y miembros de los ámbitos. La comunidad bautizó un problema frecuente: la **deuda de retención**, que aparece cuando directivas de solo retener mantienen indefinidamente el OneDrive y el buzón de exempleados. Medirla y corregirla con ámbitos adaptables alineados al ciclo de vida del usuario es una mejora de alto impacto.

**Por qué importa**

La dirección y la auditoría necesitan evidencia de que el programa funciona, y el equipo necesita saber dónde está el riesgo. Las métricas muestran el backlog, la deuda y el costo, justifican inversiones (E5 frente a complementos, Microsoft 365 Archive frente a más almacenamiento) y convierten la mejora continua en un ritual con fecha.

**Qué vas a lograr**

- Definir un tablero de indicadores de cobertura, eliminación, eventos y costo.
- Extraer datos de la página de eliminación, de la auditoría y de scripts.
- Detectar y reducir la deuda de retención.
- Presentar resultados a la dirección y a auditoría.

> **Consejo Ninja.** La página de eliminación permite filtrar y exportar los elementos pendientes y los ya eliminados ([eliminación](https://learn.microsoft.com/en-us/purview/disposition)): programa una exportación mensual y archívala como prueba de eliminación, con responsable y fecha.

> **Atención.** La «deuda de retención» aparece cuando directivas de solo retener mantienen indefinidamente el OneDrive y el buzón de exempleados; la comunidad propone corregirla con ámbitos adaptables alineados al ciclo de vida del usuario ([Nikki Chapple](https://nikkichapple.com/purview-lightning-talks-microsoft-security-community/)). Mídela por cantidad y antigüedad de buzones inactivos y de cuentas de OneDrive retenidas.

> **Qué cambió.** Para reportes de auditoría por script, `Search-UnifiedAuditLog` se retira el 15 de octubre de 2027 y la API AuditLogQuery de Graph está disponible en general desde octubre de 2026 ([MC1505599](https://mc.merill.net/message/MC1505599), [AuditLogQuery](https://learn.microsoft.com/en-us/graph/api/security-auditlogquery-get?view=graph-rest-1.0)). La limpieza prioritaria se sigue en la auditoría por su ID ([limpieza prioritaria](https://learn.microsoft.com/en-us/purview/priority-cleanup-exchange)).

**¿Tienes poco tiempo?**

- [Disposition of content](https://learn.microsoft.com/en-us/purview/disposition) · Documentación
- [Purview Lightning Talks – Microsoft Security Community (The Day Offboarding Exposed Infinite Retention)](https://nikkichapple.com/purview-lightning-talks-microsoft-security-community/) · Blog

**Tablero de indicadores del programa de registros**

| Indicador | Fuente o cálculo | Frecuencia | Meta ilustrativa | Dueño |
|---|---|---|---|---|
| Ubicaciones con directiva de base | Inventario de directivas (`Get-RetentionCompliancePolicy`) frente a la matriz de retención | Mensual | 100 % de las ubicaciones en uso | Gestor de registros |
| Categorías del plan de archivos con etiqueta aplicada | Exportación del plan de archivos y búsquedas por etiqueta | Trimestral | Tendencia creciente en cada categoría | Gestor de registros |
| Elementos pendientes de revisión de eliminación y su antigüedad | Exportación de la página de eliminación | Mensual | Ninguno con más de 30 días de espera | Revisores |
| Prueba de eliminación archivada | Exportación de los elementos eliminados | Mensual | 12 de 12 meses archivados | Gestor de registros |
| Registros con evento pendiente | Conciliación entre la etiqueta basada en eventos y el sistema de origen | Mensual | Cero eventos vencidos sin crear | Dueños de proceso |
| Deuda de retención | Buzones inactivos (`Get-Mailbox -InactiveMailboxOnly`) y OneDrive de exempleados retenidos sin plazo | Trimestral | Reducción trimestre a trimestre | Cumplimiento |
| Limpiezas prioritarias ejecutadas | Auditoría por el ID de cada limpieza | Por evento | Todas con tres aprobaciones registradas | Cumplimiento |
| Costo de almacenamiento y pago por uso | Cost Management de Azure y uso de Microsoft 365 Archive | Mensual | Dentro del presupuesto aprobado | Dueño del presupuesto |
| Cambios al plan de archivos con aprobación | Registro de cambios (repositorio o actas) | Por cambio | 100 % aprobados por el comité | Comité de retención |

Fuentes: [revisión de eliminación](https://learn.microsoft.com/en-us/purview/disposition), [limpieza prioritaria](https://learn.microsoft.com/en-us/purview/priority-cleanup-exchange), [deuda de retención (comunidad)](https://nikkichapple.com/purview-lightning-talks-microsoft-security-community/) y [precios de Microsoft 365 Archive](https://learn.microsoft.com/en-us/microsoft-365/archive/archive-pricing?view=o365-worldwide). Las metas son ilustrativas: fíjalas con tu comité.

### Comunidad: blogs, libros, newsletters y eventos

- [Purview Lightning Talks – Microsoft Security Community (The Day Offboarding Exposed Infinite Retention)](https://nikkichapple.com/purview-lightning-talks-microsoft-security-community/) · Blog · MVP · Nuevo · Nikki Chapple · nikkichapple.com · 31 may 2026. Resumen de charla sobre 'deuda de retención' por directivas solo-retener que mantienen OneDrive y buzones de exempleados, y cómo usar ámbitos adaptables alineados al ciclo de vida del usuario.

**Manos a la obra**

1. `Laboratorio` Diseña tu tablero con la tabla de indicadores de este módulo: elige de 8 a 10 indicadores con su fuente, frecuencia, meta y dueño, y constrúyelo en Excel o Power BI con datos del laboratorio. Evidencia: tablero con al menos un mes de datos de prueba.
2. `Laboratorio` Extrae las fuentes del tablero en el laboratorio: exportación de la página de eliminación, inventario de directivas y etiquetas con `Get-RetentionCompliancePolicy` y `Get-ComplianceTag`, y membresía de los ámbitos adaptables. Evidencia: archivos CSV con la fecha de extracción.
3. `Laboratorio` Mide la deuda de retención del laboratorio: lista los buzones inactivos con `Get-Mailbox -InactiveMailboxOnly`, la fecha de baja de cada cuenta y la directiva o el hold que los retiene. Evidencia: informe con una propuesta de corrección.
4. `Laboratorio` Consulta en la auditoría las actividades de retención y eliminación del último mes con la [búsqueda de auditoría](https://learn.microsoft.com/en-us/purview/audit-search) o con la API AuditLogQuery, y guarda la consulta como plantilla mensual. Evidencia: resultado exportado y consulta documentada.
5. `Solo producción` Calcula las métricas con datos reales: cobertura de etiquetado, backlog de eliminación y deuda de retención. Cómo hacerlo seguro: usa roles de solo lectura (View-Only Retention Management y View-Only Record Management), exporta desde la página de eliminación sin cambiar configuraciones y comparte resultados agregados, sin el contenido de los elementos. Evidencia: primer informe mensual presentado al comité.

<a id="o3"></a>

## O3 · Gobierno, privacidad y cumplimiento normativo en MCSA

*L300–L400 · ~3 h · Origen: Nuevo en esta edición*

La retención vive en tensión con la privacidad: conservar lo que la ley exige y, al mismo tiempo, no conservar datos personales más de lo necesario. En MCSA el mapa normativo se movió en 2025–2026: México publicó una nueva Ley Federal de Protección de Datos Personales en Posesión de los Particulares (DOF del 20 de marzo de 2025), Chile aplica su Ley 21.719 desde el 1 de diciembre de 2026, Perú renovó el reglamento de su ley de datos personales y Paraguay aprobó su primera ley integral. A esto se suman las leyes de archivos, como las de México y Colombia.

Este módulo no interpreta la ley: te ayuda a construir el gobierno que la aplica. Un comité de retención con registros, Legal, privacidad, cumplimiento y TI que decide, documenta y revisa; un inventario normativo por país con enlaces a fuentes oficiales; decisiones registradas para cada categoría sensible, como las interacciones con IA; y el vínculo con Compliance Manager, que se profundiza en su propio programa (módulos A4 y O3).

**Por qué importa**

Una decisión de retención afecta a la vez derechos de las personas y obligaciones legales. Un gobierno formal con Legal y privacidad reduce el riesgo de sanciones y de daño reputacional, y los cambios regionales de 2025–2026 obligan a revisar tablas de retención que muchas organizaciones no tocan desde hace años.

**Qué vas a lograr**

- Identificar las fuentes oficiales de normativa de archivos y de datos personales relevantes para tu país.
- Establecer un comité de retención con Legal, privacidad, cumplimiento y TI.
- Documentar decisiones de retención y eliminación con su justificación y aprobación.
- Conectar el programa de registros con Compliance Manager y con los procesos de privacidad.

> **Novedad.** Cambios recientes de privacidad en MCSA: México publicó una nueva LFPDPPP (DOF del 20 de marzo de 2025) ([texto](https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPDPPP.pdf)); Perú aplica un nuevo reglamento de la Ley 29733 desde el 31 de marzo de 2025 ([reglamento](https://cdn.www.gob.pe/uploads/document/file/7756037/6554453-reglamento-de-la-ley-n-29733.pdf?v=1741726731)); Paraguay promulgó la Ley 7593/2025 con 24 meses de adecuación ([Ley 7593](https://www.bacn.gov.py/leyes-paraguayas/12924/ley-n-75932025--de-proteccin-de-datos-personales-en-la-repblica-del-paraguay)); y Chile aplica la Ley 21.719 desde el 1 de diciembre de 2026 ([Ley 21.719](https://www.leychile.cl/leychile/Navegar?idNorma=1209272&idParte=1)). El resumen regional completo está en la hoja «Normativa MCSA» del libro de Excel.

> **Atención.** Esta guía no interpreta la ley ni da asesoría legal o laboral: la investigación no pasó por revisión jurídica, y los plazos de conservación y supresión los deciden Legal, el área de archivo, RR. HH. y privacidad. Usa las fuentes oficiales como punto de partida para la conversación, no como conclusión.

> **Consejo Ninja.** Compliance Manager tiene plantillas para algunas leyes de datos personales de la región —México (diseñada para la ley de 2010), Colombia, Perú y Argentina— y evaluaciones personalizadas para el resto ([lista de regulaciones](https://learn.microsoft.com/en-us/purview/compliance-manager-regulations-list), [evaluaciones personalizadas](https://learn.microsoft.com/en-us/purview/compliance-manager-assessments-custom)). El mapeo se profundiza en el programa de Compliance Manager, módulos A4 y O3.

**¿Tienes poco tiempo?**

- [Ley General de Archivos (México)](https://www.diputados.gob.mx/LeyesBiblio/pdf/LGA.pdf) · Documentación
- [Ley 594 de 2000 - Ley General de Archivos (Colombia) - Gestor Normativo](https://www1.funcionpublica.gov.co/eva//gestornormativo/norma.php?i=4275) · Documentación
- [Resources to help you meet regulatory requirements for data lifecycle management and records management](https://learn.microsoft.com/en-us/purview/retention-regulatory-requirements) · Documentación

**Normas de la región que tocan la retención: preguntas para Legal**

| País | Norma | Qué revisar con Legal para la retención | Fuente oficial |
|---|---|---|---|
| México | Ley General de Archivos (DOF 15-06-2018; última reforma 14-11-2025) | Si la organización es sujeto obligado o recibe recursos públicos, y cómo se reflejan sus obligaciones archivísticas en el plan de archivos | [LGA](https://www.diputados.gob.mx/LeyesBiblio/pdf/LGA.pdf) |
| México | Ley Federal de Protección de Datos Personales en Posesión de los Particulares (nueva ley, DOF 20-03-2025) | Plazos de conservación y supresión de datos personales y medidas de seguridad; la plantilla de Compliance Manager se diseñó para la ley de 2010 | [LFPDPPP](https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPDPPP.pdf) |
| México | Ley General de Protección de Datos Personales en Posesión de Sujetos Obligados (2025; última reforma 14-11-2025) | Tratamiento de datos personales en el sector público | [LGPDPPSO](http://www.diputados.gob.mx/LeyesBiblio/pdf/LGPDPPSO.pdf) |
| Colombia | Ley 594 de 2000 (Ley General de Archivos) | Cómo trasladar las tablas de retención documental (TRD) al plan de archivos | [Ley 594](https://www1.funcionpublica.gov.co/eva//gestornormativo/norma.php?i=4275) |
| Colombia | Ley Estatutaria 1581 de 2012 y Decreto 1377 de 2013 | Políticas de tratamiento y supresión de datos personales; hay plantilla de Compliance Manager | [Ley 1581](http://www.secretariasenado.gov.co/senado/basedoc/ley_1581_2012.html) |
| Chile | Ley 21.719 (vigente desde el 1-12-2026) | Bases de licitud, derechos de los titulares y modelo de prevención de infracciones frente a los plazos de conservación | [Ley 21.719](https://www.leychile.cl/leychile/Navegar?idNorma=1209272&idParte=1) |
| Perú | Ley 29733 y nuevo reglamento (vigente desde el 31-03-2025) | Medidas de seguridad y oficial de datos personales; hay plantilla de Compliance Manager | [Reglamento](https://cdn.www.gob.pe/uploads/document/file/7756037/6554453-reglamento-de-la-ley-n-29733.pdf?v=1741726731) |
| Argentina | Ley 25.326 y Decreto 1558/2001 | Principios de calidad, confidencialidad y seguridad de los datos frente a su conservación; hay plantilla de Compliance Manager | [Ley 25.326](https://www.argentina.gob.ar/normativa/nacional/norma-64790/actualizacion) |
| Paraguay | Ley 7593/2025 (24 meses de adecuación, hasta fines de noviembre de 2027) | Bases de licitud, oficial de protección de datos y evaluaciones de impacto | [Ley 7593](https://www.bacn.gov.py/leyes-paraguayas/12924/ley-n-75932025--de-proteccin-de-datos-personales-en-la-repblica-del-paraguay) |
| Uruguay | Ley 18.331, Ley 19.670 y Decreto 64/020 | Responsabilidad proactiva, delegado de protección de datos y evaluaciones de impacto | [Decreto 64/020](https://www.impo.com.uy/bases/decretos/64-2020/4) |

Resumen orientativo de la hoja «Normativa MCSA» y de la investigación de este programa, con fuentes consultadas al 6 de noviembre de 2026. No es asesoría legal: cada fila es una pregunta para Legal, no una conclusión.

### Documentación, cursos y credenciales

- [Ley General de Archivos (México)](https://www.diputados.gob.mx/LeyesBiblio/pdf/LGA.pdf) · Documentación · Comunidad · ES · Congreso de la Unión · Cámara de Diputados del H. Congreso de la Unión (México) · 14 nov 2025. Texto vigente de la Ley General de Archivos de México (DOF 15-jun-2018, última reforma DOF 14-nov-2025) que define el sistema institucional de archivos, los archivos de trámite/concentración y la disposición documental para sujetos obligados.
- [Ley 594 de 2000 - Ley General de Archivos (Colombia) - Gestor Normativo](https://www1.funcionpublica.gov.co/eva//gestornormativo/norma.php?i=4275) · Documentación · Comunidad · ES · Congreso de Colombia · Función Pública (Colombia) · 14 jul 2000. Ley General de Archivos de Colombia que define la tabla de retención documental (TRD), la gestión documental y el rol del Archivo General de la Nación, base para trasladar TRD a etiquetas de retención.

**Manos a la obra**

1. `Laboratorio` Arma el inventario normativo de tu país a partir de la tabla de este módulo y de la hoja «Normativa MCSA»: normas de archivos, de datos personales y del sector que afectan a la retención, con su enlace oficial y la pregunta abierta para Legal. Evidencia: inventario con la fecha de consulta de cada fuente.
2. `Laboratorio` Para tres categorías con datos personales (expediente de empleado, interacciones con IA y currículums de candidatos), documenta el plazo mínimo que fija Legal, el máximo razonable según privacidad y la decisión aprobada. Evidencia: registro de decisiones con la aprobación de Legal y privacidad.
3. `Laboratorio` Redacta el acta constitutiva del comité de retención: miembros (registros, Legal, privacidad, RR. HH., cumplimiento y TI), quórum, frecuencia, criterios de decisión y plantilla del registro de decisiones. Evidencia: acta y plantilla aprobadas.
4. `Laboratorio` Conecta el programa con Compliance Manager: crea una evaluación con la plantilla de tu país o una evaluación personalizada y vincula las acciones de mejora relacionadas con retención y registros ([evaluaciones personalizadas](https://learn.microsoft.com/en-us/purview/compliance-manager-assessments-custom)). Evidencia: evaluación con acciones asignadas.
5. `Solo producción` Revisa la tabla de retención de la organización frente a los cambios normativos de 2025–2026. Cómo hacerlo seguro: no cambies etiquetas ni directivas en producción sin la aprobación del comité, prueba las etiquetas nuevas en un área piloto sin eliminación y comunica los cambios a los dueños de datos. Evidencia: versión aprobada de la tabla y plan de despliegue.

<a id="reto-operacion"></a>

## Reto del nivel

**Defensa del programa ante el comité.** Prepara y presenta en 20 minutos, ante un comité simulado (Legal, privacidad, auditoría interna y TI): (1) la matriz RACI y los grupos de roles con expiración que la implementan; (2) el tablero con 8 a 10 indicadores y datos del laboratorio, incluida la deuda de retención; (3) el inventario normativo de tu país validado por Legal y el registro de decisiones de las categorías sensibles, incluida la IA; (4) la evidencia de un ciclo completo: plan de archivos aprobado, eliminación revisada y prueba exportada; y (5) un plan de mejora a 90 días con riesgos y costos. Criterio de éxito: el comité puede rastrear cualquier eliminación hasta su regla, su aprobación y su evidencia.

<a id="quiz-operacion"></a>

## Evaluación del nivel

Responde y compara con [Evaluaciones y respuestas](06_Evaluaciones_y_respuestas.md#eval-operacion). Con 80 % o más, ¡nivel aprobado! (En la versión web puedes corregir en línea y generar tu certificado).

1. ¿Qué configuración respeta la separación de funciones que recomienda la documentación de eliminación?
   - a) Un único grupo Records Management para diseñar, revisar y aprobar la limpieza prioritaria
   - b) El administrador global para todas las tareas, con auditoría posterior
   - c) Records Management para el diseño, un grupo personalizado de revisores con Disposition Management y aprobadores distintos para la limpieza prioritaria
   - d) Compliance Administrator para todos los revisores

2. ¿Qué norma internacional define políticas, responsabilidades, valoración, controles y autoridades de disposición para la gestión de registros?
   - a) ISO 15489-1:2016
   - b) ISO/IEC 27001
   - c) ISO 9001
   - d) ISO 22301

3. Según el caso que resume Nikki Chapple, ¿qué hizo un programa global con su tabla de retención?
   - a) Creó una etiqueta por cada serie documental
   - b) Pasó de más de 5.000 categorías a 180 tipos de registro y usó la revisión de eliminación solo como excepción
   - c) Eliminó por completo la revisión de eliminación
   - d) Usó solo directivas de toda la organización

4. Un auditor externo necesita consultar la configuración de retención durante tres semanas. ¿Qué es lo más adecuado desde julio de 2026?
   - a) Asignarle Compliance Administrator de forma permanente
   - b) Asignarle View-Only Retention Management con fecha de expiración
   - c) Compartirle la cuenta de un administrador
   - d) Enviarle cada semana por correo una exportación de las directivas

5. ¿Qué evidencia mensual demuestra que las eliminaciones se hicieron con autorización?
   - a) La exportación de los elementos eliminados desde la página de eliminación
   - b) Una captura del sitio vacío
   - c) El informe de uso de Copilot
   - d) La lista de etiquetas publicadas

6. ¿Qué describe la «deuda de retención»?
   - a) Etiquetas creadas que nunca se publicaron
   - b) Directivas de solo retener que mantienen indefinidamente el OneDrive y el buzón de exempleados
   - c) Costos de pago por uso pendientes de pago
   - d) Eventos de retención creados dos veces

7. ¿Cómo se monitorea una limpieza prioritaria?
   - a) En el explorador de actividad
   - b) En Compliance Manager
   - c) En la auditoría, con el ID de la limpieza
   - d) No deja rastro, por diseño

8. Un script de métricas usa `Search-UnifiedAuditLog`. ¿Qué deberías planificar?
   - a) Cambiarlo por Get-AdminAuditLogConfig
   - b) Reemplazarlo por búsquedas de contenido
   - c) Usar el explorador de contenido
   - d) Migrarlo a la API AuditLogQuery de Graph antes del retiro del cmdlet, el 15 de octubre de 2027

9. ¿Qué roles permiten a un analista de métricas ver la configuración de retención y registros sin modificarla?
   - a) View-Only Retention Management y View-Only Record Management
   - b) Records Management
   - c) Priority Cleanup Admin
   - d) Compliance Administrator

10. ¿Desde cuándo rige la Ley 21.719 de protección de datos personales de Chile?
   - a) 1 de enero de 2025
   - b) 1 de marzo de 2025
   - c) 1 de diciembre de 2026
   - d) 1 de diciembre de 2027

11. Según el texto vigente consultado, ¿cuándo fue la última reforma de la Ley General de Archivos de México?
   - a) 15 de junio de 2018
   - b) 20 de marzo de 2025
   - c) 1 de diciembre de 2026
   - d) 14 de noviembre de 2025

12. ¿Qué norma colombiana define la tabla de retención documental (TRD)?
   - a) Ley 1581 de 2012
   - b) Decreto 1377 de 2013
   - c) Ley 594 de 2000
   - d) Circular Externa 007 de 2018

13. ¿Cuándo se publicó en el DOF la nueva Ley Federal de Protección de Datos Personales en Posesión de los Particulares de México?
   - a) 20 de marzo de 2025
   - b) 5 de julio de 2010
   - c) 14 de noviembre de 2025
   - d) 1 de diciembre de 2026

14. ¿Qué período de adecuación da la Ley 7593/2025 de protección de datos personales de Paraguay?
   - a) 6 meses
   - b) 12 meses
   - c) 36 meses
   - d) 24 meses

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. No es asesoría legal: las decisiones de retención y eliminación deben validarse con Legal y privacidad. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

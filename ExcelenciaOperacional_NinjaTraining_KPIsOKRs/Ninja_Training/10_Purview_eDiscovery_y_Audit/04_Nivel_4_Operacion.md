# Nivel 4 · Operación · Modelo operativo, métricas y gobierno

*Microsoft Purview eDiscovery y Audit Ninja Training · Edición 2026*

[← Nivel 3 · Avanzado](03_Nivel_3_Avanzado.md) · [Índice del programa](README.md) · [Comunidad →](05_Comunidad.md)

<a id="operacion"></a>

Cómo se organiza un equipo de eDiscovery y auditoría que trabaja con Legal, RR. HH., cumplimiento, auditoría interna, privacidad y el SOC: responsabilidades, procedimientos, métricas y gobierno en MCSA, sin interpretar la ley.

*L300–L400 · 3 módulos · ~9 horas · 9 recursos*

**Módulos de este nivel:** [O1 Modelo operativo](#o1) · [O2 Métricas y mejora continua](#o2) · [O3 Gobierno, privacidad y MCSA](#o3)

<a id="o1"></a>

## O1 · Modelo operativo del equipo y responsabilidades

*L300–L400 · ~3 h · Origen: Nuevo en esta edición*

eDiscovery y Audit son capacidades compartidas: Legal decide qué preservar, TI o el equipo de plataforma administra, los investigadores buscan y revisan, privacidad vigila la proporcionalidad, auditoría interna verifica los controles y el SOC consume la auditoría. Sin un modelo operativo explícito, cada asunto se negocia desde cero y los permisos crecen sin control. El modelo se construye con cuatro piezas: un **intake** de solicitudes, una **matriz RACI**, procedimientos estándar por tipo de asunto y un **catálogo de roles** con mínimo privilegio.

Dos marcos te ayudan a hablar el mismo idioma con Legal y con el SOC. **EDRM 2.0**, publicado el 1 de septiembre de 2026, agrupa identificación, preservación, recolección y procesamiento en «Data Acquisition», agrega la disposición y se apoya en el modelo de gobierno de la información. **NIST SP 800-61 Rev. 3** (abril de 2025) integra la respuesta a incidentes con la gestión de riesgos del CSF 2.0. Este módulo los aterriza en un procedimiento para tu organización.

**Por qué importa**

Un modelo operativo claro reduce el tiempo desde la solicitud hasta el hold, evita que un asunto quede sin dueño y limita quién ve qué. También es lo primero que pedirán un auditor interno o un regulador: evidencia de que el acceso a información sensible está gobernado, separado por funciones y registrado.

**Qué vas a lograr**

- Diseñar el intake de solicitudes de eDiscovery y de auditoría con sus datos mínimos.
- Construir una matriz RACI entre Legal, RR. HH., TI, seguridad, privacidad y auditoría interna.
- Mapear el procedimiento estándar a EDRM 2.0 y a NIST SP 800-61 Rev. 3.
- Definir un catálogo de roles con mínimo privilegio, PIM y separación de funciones.

> **Novedad.** EDRM 2.0, publicado el 1 de septiembre de 2026 con licencia CC BY 4.0, agrupa identificación, preservación, recolección y procesamiento en «Data Acquisition», agrega la disposición y se apoya en el modelo de gobierno de la información (IGRM) ([EDRM](https://edrm.net/edrm-model/current/)).

> **Atención.** Mantén mínimo el grupo eDiscovery Administrator, porque accede a todos los casos ([permisos de eDiscovery](https://learn.microsoft.com/en-us/purview/edisc-permissions)). Desde julio de 2026 las asignaciones a grupos de roles de Purview admiten fecha de expiración, de un día a dos años, **salvo** eDiscovery Administrator y eDiscovery Manager ([novedades de Purview](https://learn.microsoft.com/en-us/purview/whats-new)): para esos roles usa PIM para grupos ([PIM para grupos](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/concept-pim-for-groups)).

> **Consejo Ninja.** Un runbook de partner de 18 pasos sobre un caso sintético —licencias, roles mínimos, hold, estadísticas, exportación y conciliación de Items.csv— sirve como plantilla para tu procedimiento estándar; contrástalo siempre con Learn ([runbook](https://www.epcgroup.net/answers/microsoft-purview-ediscovery-premium-implementation-2026)).

**¿Tienes poco tiempo?**

- [Current EDRM Model (Electronic Discovery Reference Model 2.0, 2026)](https://edrm.net/edrm-model/current/) · Documentación
- [SP 800-61 Rev. 3, Incident Response Recommendations and Considerations for Cybersecurity Risk Management](https://csrc.nist.gov/pubs/sp/800/61/r3/final) · Documentación
- [Purview eDiscovery Premium Implementation (2026) – case runbook](https://www.epcgroup.net/answers/microsoft-purview-ediscovery-premium-implementation-2026) · Blog

**RACI de referencia para eDiscovery y Audit (ajústala a tu organización)**

| Actividad | Legal (gestión de eDiscovery) | Investigación interna y RR. HH. | Registros y cumplimiento | Plataforma (TI) | SOC | Privacidad | Auditoría interna |
|---|---|---|---|---|---|---|---|
| Recibir y aprobar la solicitud (intake) | A | C | C | I | C | C | I |
| Abrir el caso y asignar miembros | A | I | I | R | I | I | I |
| Aplicar, verificar y renovar holds | A | I | R | R | I | C | I |
| Notificar a custodios | A/R | C | C | I | I | C | I |
| Buscar y refinar consultas | A | R | C | C | C | C | I |
| Revisar en review sets | A/R | R | I | I | I | C | I |
| Exportar y registrar la cadena de custodia | A | R | C | C | I | C | I |
| Buscar en la auditoría para un incidente | C | I | I | C | R | C | I |
| Configurar la retención de auditoría | C | I | A | R | C | C | I |
| Asignar y revisar roles privilegiados | A | I | C | R | I | C | C |
| Liberar holds y cerrar el caso | A | I | R | R | I | C | I |
| Probar los controles del programa | C | I | C | C | C | C | R |

R = responsable, A = aprueba, C = consultado, I = informado. Propuesta de esta guía alineada con [EDRM 2.0](https://edrm.net/edrm-model/current/) y [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final); no reemplaza tus políticas internas.

### Documentación, cursos y credenciales

- [Current EDRM Model (Electronic Discovery Reference Model 2.0, 2026)](https://edrm.net/edrm-model/current/) · Documentación · Comunidad · Nuevo · Ninja original · EDRM · 1 sep 2026. EDRM 2.0 (1-sep-2026) agrupa Identificación, Preservación, Recolección y Procesamiento en "Data Acquisition", añade Disposición y pone el IGRM como base, bajo licencia CC BY 4.0. *Nota:* El Ninja original de 2021 se alineaba al EDRM; recomendable actualizar el temario a EDRM 2.0
- [SP 800-61 Rev. 3, Incident Response Recommendations and Considerations for Cybersecurity Risk Management](https://csrc.nist.gov/pubs/sp/800/61/r3/final) · Documentación · Comunidad · NIST · NIST CSRC · abr 2025. Guía NIST de respuesta a incidentes alineada a CSF 2.0 (abril de 2025) que reemplaza la Rev. 2 y sirve de marco para integrar Audit/eDiscovery en IR.

### Comunidad: blogs, libros, newsletters y eventos

- [Purview eDiscovery Premium Implementation (2026) – case runbook](https://www.epcgroup.net/answers/microsoft-purview-ediscovery-premium-implementation-2026) · Blog · Comunidad · Nuevo · Errin O'Connor · EPC Group · 28 oct 2026. Runbook de partner con 18 pasos de un caso sintético (licencias, roles mínimos, hold, estadísticas, exportación y conciliación de Items.csv) para validar el proceso antes del primer asunto real.

**Manos a la obra**

1. `Laboratorio` Organiza una mesa de trabajo de 90 minutos con Legal, RR. HH., TI, seguridad, privacidad y auditoría interna, y completa la RACI de referencia de este módulo para cuatro tipos de asunto (litigio, investigación interna, requerimiento regulatorio e incidente), mapeada a [EDRM 2.0](https://edrm.net/edrm-model/current/) y a [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final). Evidencia: RACI aprobada y minuta.
2. `Laboratorio` Diseña el formulario de intake con los datos mínimos: solicitante, tipo de asunto, base de la solicitud, custodios, rango de fechas, orígenes, urgencia, revisión de privacidad y aprobación de Legal. Pruébalo con dos solicitudes simuladas. Evidencia: formulario y dos registros completos.
3. `Laboratorio` Escribe tu procedimiento estándar de caso, del intake al cierre, usando como lista de control el [runbook de 18 pasos](https://www.epcgroup.net/answers/microsoft-purview-ediscovery-premium-implementation-2026) validado contra Learn, y ejecútalo de punta a punta en `PRUEBA-005`. Evidencia: procedimiento versión 1 con la evidencia de cada paso.
4. `Laboratorio` Arma el catálogo de roles: por cada función, grupo de roles, tipo de asignación (permanente, justo a tiempo con [PIM para grupos](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/concept-pim-for-groups) o con fecha de expiración donde Purview lo permite), aprobador y revisión trimestral. Verifica en el laboratorio que el tipo de grupo que eliges es compatible con cada grupo de roles ([permisos del portal](https://learn.microsoft.com/en-us/purview/purview-permissions)). Evidencia: catálogo y una asignación de prueba funcionando.
5. `Solo producción` Pilotea el modelo con una solicitud real de baja sensibilidad. Cómo hacerlo seguro: patrocinio de Legal, alcance mínimo, roles asignados justo a tiempo, tiempos medidos en cada etapa y revisión posterior sin culpables. Evidencia: informe del piloto con tiempos y mejoras acordadas.

<a id="o2"></a>

## O2 · Métricas, reportes y mejora continua

*L300–L400 · ~3 h · Origen: Nuevo en esta edición*

Lo que no se mide no mejora, y en eDiscovery y Audit las métricas tienen una ventaja: la propia plataforma registra lo que hace el equipo. Las actividades de eDiscovery —crear casos, buscar, generar estadísticas, exportar, aplicar holds, agregar a review sets— quedan en la auditoría con la dirección IP del cliente, y desde septiembre y octubre de 2026 el portal registra nuevas operaciones de auditoría de RBAC. Con eso mides tiempos, volúmenes y accesos sin depender de planillas manuales.

Un buen tablero combina métricas de servicio (tiempo de la solicitud al hold, del hold a la exportación, exportaciones descargadas antes de vencer), de calidad (conciliaciones sin diferencias, consultas versionadas), de costo (pago por uso, SCU, almacenamiento de DSI) y de control (accesos a casos fuera del equipo, cambios de roles, políticas de retención de auditoría). Este módulo te deja un tablero mínimo y un ciclo trimestral de mejora.

**Por qué importa**

Las métricas convierten el trabajo de eDiscovery en un servicio gestionable: permiten justificar personal y licencias con datos, detectar cuellos de botella antes de que se incumpla un plazo judicial y demostrar a auditoría interna que los accesos a información sensible están controlados.

**Qué vas a lograr**

- Definir métricas de servicio, calidad, costo y control para eDiscovery y Audit.
- Extraer de la auditoría las actividades del propio equipo de eDiscovery.
- Detectar cambios de roles y accesos anómalos a casos.
- Establecer un ciclo trimestral de revisión y mejora.

> **Novedad.** Entre fines de septiembre y octubre de 2026, el portal de Purview empezó a registrar nuevas operaciones de auditoría de RBAC, como `CheckUsersInRoles` y `CheckUserInRolesWithScopes`. No son retroactivas ([MC1473155](https://mc.merill.net/message/MC1473155)).

> **Consejo Ninja.** Las actividades de la experiencia unificada de eDiscovery quedan en Audit con la IP del cliente; un IP vacío indica la experiencia heredada ([actividades de eDiscovery en Audit](https://learn.microsoft.com/en-us/purview/edisc-ref-audit-log)). Es la base para medir tiempos y accesos sin planillas manuales.

> **Consejo Ninja.** Para las métricas de costo, el Usage center de Purview (vista previa) muestra el consumo de pago por uso por función ([Usage center](https://learn.microsoft.com/en-us/purview/purview-billing-usage)) y el panel de Security Copilot muestra 90 días de consumo de SCU por sesión, usuario y experiencia ([uso de SCU](https://learn.microsoft.com/en-us/copilot/security/manage-usage)).

> **Atención.** Medir al equipo también es tratar datos personales de sus integrantes. Acuerda con privacidad y RR. HH. qué métricas se publican de forma individual y cuáles agregadas, con el mismo criterio de privacidad por diseño que aplican Insider Risk y Communication Compliance ([guía de privacidad](https://learn.microsoft.com/en-us/purview/insider-risk-solution-privacy)).

**¿Tienes poco tiempo?**

- [Search for eDiscovery activities in the audit log](https://learn.microsoft.com/en-us/purview/edisc-ref-audit-log) · Documentación
- [MC1473155 - Microsoft Purview: permissions audit log improvements](https://mc.merill.net/message/MC1473155) · Documentación

**Tablero mínimo de métricas de eDiscovery y Audit**

| Métrica | Tipo | Cómo se calcula | Fuente de datos |
|---|---|---|---|
| Tiempo de la solicitud al hold efectivo | Servicio | Fecha del intake frente a la fecha en que el hold quedó efectivo | Intake y actividades de eDiscovery en Audit |
| Custodios preservados dentro de 24 horas | Servicio | Custodios con hold efectivo a las 24 horas sobre el total solicitado | Estado de los holds del caso |
| Exportaciones descargadas antes de vencer | Servicio | Descargas dentro de 14 días (búsquedas) o 30 días (review sets) sobre el total | Formulario de custodia y actividades de eDiscovery |
| Conciliaciones sin diferencias | Calidad | Producciones cuyo informe de ítems coincide con las estadísticas | Formulario de custodia |
| Consultas versionadas y justificadas | Calidad | Consultas con versión, autor y justificación sobre el total ejecutado | Registro de consultas |
| Reducción de volumen por analítica | Eficiencia | Ítems para revisión después de casi duplicados e hilos, sobre el total del review set | Analítica del review set |
| Gasto de pago por uso por asunto | Costo | Consumo de DSI, auditoría de IA y exportación por Graph por caso | Usage center y Azure Cost Management |
| SCU consumidas por asunto | Costo | SCU de Security Copilot atribuidas a cada caso | Panel de uso de Security Copilot |
| Accesos a casos fuera del equipo autorizado | Control | Actividades en casos por cuentas que no figuran en la RACI | Actividades de eDiscovery en Audit (con IP del cliente) |
| Cambios de roles privilegiados sin ticket | Control | Altas en grupos de roles de eDiscovery, Audit y Search And Purge sin aprobación | Operaciones de auditoría de RBAC |
| Cobertura de retención de auditoría | Control | Usuarios y cargas cuya retención cumple la política interna | Políticas de retención de auditoría |

Fuentes de datos: [actividades de eDiscovery en Audit](https://learn.microsoft.com/en-us/purview/edisc-ref-audit-log), [MC1473155](https://mc.merill.net/message/MC1473155), [Usage center](https://learn.microsoft.com/en-us/purview/purview-billing-usage) y [uso de SCU](https://learn.microsoft.com/en-us/copilot/security/manage-usage). Publica las métricas por persona solo con el acuerdo de privacidad y RR. HH.

### Documentación, cursos y credenciales

- [Search for eDiscovery activities in the audit log](https://learn.microsoft.com/en-us/purview/edisc-ref-audit-log) · Documentación · Oficial · Nuevo · Microsoft Learn · 25 jun 2026. Cómo buscar en Audit las actividades de eDiscovery (casos, búsquedas, estadísticas, exportaciones, holds, review sets), base para métricas y supervisión del propio equipo de eDiscovery.
- [MC1473155 - Microsoft Purview: permissions audit log improvements](https://mc.merill.net/message/MC1473155) · Documentación · Oficial · Nuevo · Message Center (archivo mc.merill.net) · 16 sep 2026. Anuncia nuevas operaciones de auditoría RBAC del portal Purview (CheckUsersInRoles, CheckUserInRolesWithScopes) desplegadas entre fines de septiembre y octubre de 2026.

**Manos a la obra**

1. `Laboratorio` Extrae de la auditoría las actividades de eDiscovery de tu laboratorio (creación de casos, búsquedas, holds, review sets y exportaciones) y calcula tres métricas de servicio: tiempo del caso al hold, de la búsqueda a la exportación y porcentaje de exportaciones descargadas antes de vencer ([actividades de eDiscovery en Audit](https://learn.microsoft.com/en-us/purview/edisc-ref-audit-log)). Evidencia: planilla con las tres métricas.
2. `Laboratorio` Cambia la membresía de un grupo de roles de prueba, encuentra el cambio en la auditoría (incluidas las operaciones de RBAC de [MC1473155](https://mc.merill.net/message/MC1473155)) y redacta el criterio de alerta para cambios en eDiscovery Administrator, eDiscovery Manager, Audit Manager y Search And Purge. Evidencia: registro encontrado y criterio de alerta.
3. `Laboratorio` Construye el tablero mínimo de este módulo con datos del laboratorio en una planilla o en Power BI: al menos una métrica de servicio, una de calidad, una de costo y una de control, cada una con su fuente de datos. Evidencia: tablero con fecha de corte.
4. `Laboratorio parcial` Registra el costo del laboratorio: consumo por uso en el Usage center de Purview (vista previa) y en Azure Cost Management, y SCU en el panel de Security Copilot si tienes capacidad. Limitación: sin licencias E5 pagadas no hay SCU incluidas que medir ([Usage center](https://learn.microsoft.com/en-us/purview/purview-billing-usage), [uso de SCU](https://learn.microsoft.com/en-us/copilot/security/manage-usage)). Evidencia: tabla de costos por ejercicio.
5. `Solo producción` Haz la primera revisión trimestral con métricas reales. Cómo hacerlo seguro: extracción con roles de solo lectura, métricas individuales acordadas antes con privacidad y RR. HH., publicación agregada y acciones de mejora con dueño y fecha. Evidencia: minuta de la revisión y lista de mejoras.

<a id="o3"></a>

## O3 · Gobierno, privacidad y cumplimiento normativo en MCSA

*L300–L400 · ~3 h · Origen: Nuevo en esta edición*

eDiscovery y Audit tratan datos personales a escala: buscar en el buzón de una persona, leer su chat con Copilot o extraer su actividad es tratamiento de datos. En México, Centroamérica y Sudamérica el marco cambia rápido: Chile tiene una nueva ley de datos personales, la 21.719, que entra en vigencia el 1 de diciembre de 2026 e incluye la transferencia internacional; México publicó su nueva LFPDPPP el 20 de marzo de 2025, y Paraguay promulgó la Ley 7593 en noviembre de 2025. Esta guía no interpreta la ley: te ayuda a hacer las preguntas correctas y a llevarlas a Legal, RR. HH. y privacidad con evidencia técnica.

Las decisiones técnicas con impacto jurídico son concretas: dónde se aprovisiona el almacenamiento del review set (en la geografía del caso, con soporte de Customer Key y sin acceso directo por SAS), adónde viaja una exportación, en qué región corre el cómputo de IA de DSI, sobre quién se habilita SearchQueryInitiated, cuánto se retiene la auditoría y quién puede borrar contenido retenido con Priority Cleanup. Este módulo arma un registro de decisiones para que cada una tenga dueño, fundamento y fecha.

**Por qué importa**

Una investigación técnicamente impecable puede volverse inutilizable o sancionable si se hizo sin base legal, sin proporcionalidad o transfiriendo datos sin cumplir los requisitos aplicables. Llevar las decisiones técnicas a un registro revisado por Legal y privacidad protege a las personas investigadas, a la organización y al propio equipo de eDiscovery.

**Qué vas a lograr**

- Identificar las decisiones técnicas de eDiscovery, Audit y DSI con impacto en privacidad y transferencias.
- Ubicar las fuentes oficiales de protección de datos de los países de MCSA sin interpretarlas.
- Construir un registro de decisiones con dueño, fundamento y fecha, revisado por Legal.
- Incorporar Priority Cleanup, las solicitudes de titulares y la retención de auditoría al gobierno del programa.

> **Novedad.** Chile: la Ley 21.719 entra en vigencia el 1 de diciembre de 2026 e incluye la transferencia internacional de datos ([BCN](https://www.bcn.cl/leychile/N?i=1209272&f=2026-12-01)). México: la nueva LFPDPPP se publicó el 20 de marzo de 2025 ([texto](https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPDPPP.pdf?version=published)). Paraguay: la Ley 7593/2025 se publicó el 27 de noviembre de 2025 con 24 meses de adecuación ([BACN](https://www.bacn.gov.py/leyes-paraguayas/12924/ley-n-75932025--de-proteccin-de-datos-personales-en-la-repblica-del-paraguay)). La hoja «Normativa MCSA» del libro de Excel resume el resto de la región.

> **Atención.** Esta guía no interpreta la ley. Las preguntas técnicas —dónde se aprovisiona el review set (en la geografía del caso, con Customer Key y sin acceso directo por SAS), adónde viaja una exportación y en qué región corre el cómputo de DSI— se llevan a Legal y privacidad con evidencia ([review sets](https://learn.microsoft.com/en-us/purview/edisc-search-add-to-review-set), [facturación de DSI](https://learn.microsoft.com/en-us/purview/data-security-investigations-billing)).

> **Consejo Ninja.** En tenants multigeográficos, eDiscovery usa el filtro de seguridad «Region» para las ubicaciones satélite, entre ellas México (MEX) y Chile (CHL) ([Multi-Geo](https://learn.microsoft.com/en-us/microsoft-365/enterprise/multi-geo-ediscovery-configuration?view=o365-worldwide)); los límites de cumplimiento restringen qué puede buscar cada equipo por país o subsidiaria, también en DSI ([límites de cumplimiento](https://learn.microsoft.com/en-us/purview/edisc-compliance-boundaries)).

> **Consejo Ninja.** Security Copilot: en tenants E5 o E7 aprovisionados automáticamente, la opción de compartir datos con Microsoft viene desactivada por defecto, y la ubicación de datos del workspace no se puede cambiar después de crearlo. Decide esa ubicación con privacidad antes del primer uso ([privacidad de Security Copilot](https://learn.microsoft.com/en-us/copilot/security/privacy-data-security)).

**¿Tienes poco tiempo?**

- [Add search results to a review set in eDiscovery](https://learn.microsoft.com/en-us/purview/edisc-search-add-to-review-set) · Documentación
- [Ley Chile - Ley 21719 (Regula la protección y el tratamiento de los datos personales)](https://www.bcn.cl/leychile/N?i=1209272&f=2026-12-01) · Documentación
- [Ley Federal de Protección de Datos Personales en Posesión de los Particulares (México, 2025)](https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPDPPP.pdf?version=published) · Documentación

**Decisiones técnicas con impacto en privacidad (para llevar a Legal)**

| Decisión | Dato técnico | Pregunta para Legal y privacidad | Fuente |
|---|---|---|---|
| Ubicación del review set | Se aprovisiona en la geografía del caso, admite Customer Key y no ofrece acceso directo por SAS | ¿La geografía del caso es aceptable para los custodios de cada país? | [Learn](https://learn.microsoft.com/en-us/purview/edisc-search-add-to-review-set) |
| Destino de una exportación | Paquetes de búsqueda que vencen a los 14 días; exportaciones de review set con 30 días para descargar | ¿La entrega a un tercero o a otro país requiere algún requisito adicional? | [Learn](https://learn.microsoft.com/en-us/purview/edisc-search-export) |
| Cómputo de IA de DSI | Australia y Nueva Zelanda, UE, Reino Unido, EE. UU. o «en cualquier lugar»; sin opción en Latinoamérica | ¿Qué ubicación es aceptable para cada país y tipo de dato? | [Learn](https://learn.microsoft.com/en-us/purview/data-security-investigations-billing) |
| Alcance de SearchQueryInitiated | En Exchange se habilita buzón por buzón | ¿Sobre quién se justifica registrar sus búsquedas y durante cuánto tiempo? | [Learn](https://learn.microsoft.com/en-us/purview/audit-get-started) |
| Retención de la auditoría | 180 días en Standard, un año en Premium y hasta 10 años con complemento | ¿Cuál es el plazo proporcional a la finalidad? | [Learn](https://learn.microsoft.com/en-us/purview/audit-log-retention-policies) |
| Limpieza prioritaria | Elimina contenido retenido, que deja de ser descubrible; requiere aprobaciones y se puede desactivar | ¿Se habilita? ¿Quién aprueba y cómo se verifica que no afecte un asunto activo? | [Learn](https://learn.microsoft.com/en-us/purview/priority-cleanup-exchange) |
| Compartición de datos de Security Copilot | Desactivada por defecto en E5 o E7 aprovisionados automáticamente; la ubicación del workspace no cambia después de crearlo | ¿Se mantiene desactivada? ¿Dónde se ubica el workspace? | [Learn](https://learn.microsoft.com/en-us/copilot/security/privacy-data-security) |
| Búsquedas en tenants multigeográficos | Filtro de seguridad «Region» para ubicaciones satélite (por ejemplo, MEX y CHL) | ¿Quién puede buscar en cada geografía? | [Learn](https://learn.microsoft.com/en-us/microsoft-365/enterprise/multi-geo-ediscovery-configuration?view=o365-worldwide) |
| Límites de cumplimiento | Filtros de permisos de búsqueda por país o subsidiaria, también en DSI | ¿Qué equipo puede buscar en qué país o empresa del grupo? | [Learn](https://learn.microsoft.com/en-us/purview/edisc-compliance-boundaries) |
| Envío de auditoría a un SIEM en otra región | El conector de Purview Information Protection advierte posible transmisión entre regiones | ¿Es aceptable el traslado de esos registros? | [Learn](https://learn.microsoft.com/en-us/azure/sentinel/connect-microsoft-purview) |
| Solicitudes de titulares de datos | La antigua User Data Search está integrada en eDiscovery | ¿Qué plazo, formato y verificación de identidad exige cada ley? | [Learn](https://learn.microsoft.com/en-us/purview/edisc-search-query) |

Esta tabla ordena preguntas; no interpreta la ley. Las respuestas corresponden a Legal, privacidad y, cuando aplique, RR. HH., con las fuentes oficiales de la hoja «Normativa MCSA».

### Documentación, cursos y credenciales

- [Add search results to a review set in eDiscovery](https://learn.microsoft.com/en-us/purview/edisc-search-add-to-review-set) · Documentación · Oficial · Microsoft Learn. Explica qué ocurre al agregar resultados a un review set (re-ejecución, copia a almacenamiento Azure gestionado por Microsoft por caso, reindexación, descifrado) y que el almacenamiento se aprovisiona en la geo del caso con soporte de Customer Key.
- [Ley Federal de Protección de Datos Personales en Posesión de los Particulares (México, 2025)](https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPDPPP.pdf?version=published) · Documentación · Comunidad · ES · Congreso de la Unión · Cámara de Diputados (México) · 20 mar 2025. Nueva LFPDPPP mexicana publicada en el DOF el 20-mar-2025 (última reforma 14-nov-2025) que regula el tratamiento de datos personales por particulares, incluidos derechos ARCO y encargados.
- [Ley Chile - Ley 21719 (Regula la protección y el tratamiento de los datos personales)](https://www.bcn.cl/leychile/N?i=1209272&f=2026-12-01) · Documentación · Comunidad · ES · Congreso Nacional de Chile · Biblioteca del Congreso Nacional de Chile · 13 dic 2024. Ley chilena de protección de datos personales (publicada 13-dic-2024) que entra en vigencia el 1-dic-2026 e incluye transferencia internacional de datos y una nueva agencia de protección.

### Anuncios y blogs oficiales

- [Become a Microsoft Priva Ninja](https://techcommunity.microsoft.com/blog/microsoft-security-blog/become-a-microsoft-priva-ninja/3876888) · Blog oficial · Empleado de Microsoft · Legado aún útil · John_Wirtala1608 · Microsoft Security Community Blog · 18 jul 2023. Ninja de Priva (privacidad y solicitudes de derechos) útil para coordinar eDiscovery con el equipo de privacidad en solicitudes DSR. *Nota:* Contexto para el modelo operativo legal-privacidad; Priva tiene licencia propia

**Manos a la obra**

1. `Laboratorio` Completa el registro de decisiones con al menos ocho entradas —ubicación del review set, destino de exportaciones, cómputo de DSI, alcance de SearchQueryInitiated, retención de auditoría, limpieza prioritaria, compartición de datos de Security Copilot y filtros por región— usando la tabla de decisiones de este módulo. Cada entrada lleva dueño, opciones, pregunta para Legal, aprobador y fecha. Evidencia: registro revisado por Legal y privacidad.
2. `Laboratorio` Con la hoja «Normativa MCSA» del libro de Excel, arma el mapa de tus países de operación: norma, autoridad, enlace oficial y las preguntas para Legal sobre preservación, exportación y transferencias, sin interpretar la ley (por ejemplo, la [Ley 21.719 de Chile](https://www.bcn.cl/leychile/N?i=1209272&f=2026-12-01) o la [LFPDPPP de México](https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPDPPP.pdf?version=published)). Evidencia: mapa con fuentes.
3. `Laboratorio` Configura un límite de cumplimiento para dos «países» de prueba (atributo en las cuentas sintéticas) y verifica que una investigadora del país A no encuentra contenido del país B. Evidencia: filtro creado y dos búsquedas con resultados distintos ([límites de cumplimiento](https://learn.microsoft.com/en-us/purview/edisc-compliance-boundaries)).
4. `Laboratorio parcial` Ejecuta una búsqueda de solicitud de titular de datos (DSR) sobre una persona sintética con eDiscovery y prepara el informe de ubicaciones. Limitación: una solicitud real tiene plazos legales, verificación de identidad y, si usas Priva, una licencia propia ([crear una búsqueda](https://learn.microsoft.com/en-us/purview/edisc-search-query), [Priva Ninja](https://techcommunity.microsoft.com/blog/microsoft-security-blog/become-a-microsoft-priva-ninja/3876888)). Evidencia: consulta e informe.
5. `Solo producción` Presenta el registro de decisiones a Legal y privacidad para la revisión de impacto del programa de eDiscovery y Audit: a quién se le habilita SearchQueryInitiated, cuánto se retiene la auditoría, qué exportaciones salen del país y dónde corre el cómputo de IA. Cómo hacerlo seguro: ningún cambio técnico hasta tener la aprobación, y decisiones firmadas con fecha. Evidencia: registro aprobado.

<a id="reto-operacion"></a>

## Reto del nivel

**Programa listo para auditoría interna.** Prepara el paquete que mostrarías a auditoría interna y a un regulador: RACI aprobada, formulario de intake, procedimiento estándar probado en un caso de práctica, catálogo de roles con PIM y fechas de expiración donde aplican, tablero de al menos ocho métricas con su fuente de datos, registro de decisiones de privacidad revisado por Legal (ubicación del review set, exportaciones, cómputo de DSI, SearchQueryInitiated, retención de auditoría y limpieza prioritaria) y mapa normativo de tus países de MCSA con sus fuentes oficiales. Presenta en diez minutos los tres riesgos principales y la decisión que pides al comité.

<a id="quiz-operacion"></a>

## Evaluación del nivel

Responde y compara con [Evaluaciones y respuestas](06_Evaluaciones_y_respuestas.md#eval-operacion). Con 80 % o más, ¡nivel aprobado! (En la versión web puedes corregir en línea y generar tu certificado).

1. ¿Qué etapas agrupa EDRM 2.0 bajo «Data Acquisition»?
   - a) Revisión, análisis y producción
   - b) Identificación, preservación, recolección y procesamiento
   - c) Disposición y gobierno de la información
   - d) Presentación y producción

2. ¿Qué publicación de NIST reemplazó en abril de 2025 a la SP 800-61 Rev. 2?
   - a) SP 800-53 Rev. 5
   - b) CSF 2.0
   - c) SP 800-61 Rev. 3
   - d) SP 800-86

3. Desde julio de 2026 las asignaciones a grupos de roles de Purview admiten fecha de expiración. ¿Cuáles quedan excluidas?
   - a) Audit Reader y Audit Manager
   - b) eDiscovery Administrator y eDiscovery Manager
   - c) Organization Configuration
   - d) Reviewer

4. ¿Por qué conviene mantener pequeño el grupo eDiscovery Administrator?
   - a) Porque consume licencias E5 adicionales
   - b) Porque solo admite cinco miembros
   - c) Porque su actividad no se audita
   - d) Porque accede a todos los casos y a sus datos

5. ¿Qué dato registran en Audit las actividades de la experiencia unificada de eDiscovery y faltaba en las heredadas?
   - a) La dirección IP del cliente
   - b) El hash del paquete exportado
   - c) El nombre del abogado responsable
   - d) El consumo de SCU

6. ¿Qué anunció MC1473155 para fines de septiembre y octubre de 2026?
   - a) El retiro de Audit (Standard)
   - b) Nuevas operaciones de auditoría de RBAC en Purview
   - c) La expiración de exportaciones a 14 días
   - d) La disponibilidad general de AuditLogQuery

7. ¿Dónde ves el consumo de pago por uso de Purview por función?
   - a) En el Usage center de Purview (vista previa)
   - b) En el panel de SCU de Security Copilot
   - c) En la tabla OfficeActivity
   - d) En el review set del caso

8. ¿Dónde se aprovisiona el almacenamiento de un review set?
   - a) En la región del workspace de Sentinel
   - b) En una cuenta de Azure Storage del cliente
   - c) En la geografía del caso, con soporte de Customer Key
   - d) En el OneDrive del eDiscovery Manager

9. ¿Cuándo entra en vigencia la Ley 21.719 de protección de datos personales de Chile?
   - a) 13 de diciembre de 2024
   - b) 20 de marzo de 2025
   - c) 1 de diciembre de 2026
   - d) 15 de octubre de 2027

10. Legal duda si entregar una exportación a un estudio jurídico de otro país es una transferencia internacional. ¿Qué corresponde según esta guía?
   - a) Decidirlo según la región del tenant
   - b) Llevar la pregunta a Legal y privacidad con la evidencia técnica y las fuentes oficiales
   - c) Exportar primero y notificar después
   - d) Procesarla en DSI con ubicación «en cualquier lugar»

11. ¿Qué permite restringir las búsquedas de un equipo de eDiscovery a un país o a una empresa del grupo?
   - a) Las Compute Units de DSI
   - b) Las etiquetas de retención
   - c) El rol Reviewer
   - d) Los límites de cumplimiento (filtros de permisos de búsqueda)

12. ¿Qué consecuencia tiene la limpieza prioritaria (vista previa) para eDiscovery?
   - a) El contenido eliminado deja de ser descubrible
   - b) El contenido pasa a un review set
   - c) Se crea un hold automático
   - d) Solo afecta a registros regulatorios

13. Desde julio de 2026, ¿qué aprobaciones exige la limpieza prioritaria?
   - a) Una, del Global Administrator
   - b) Dos, de cualquier administrador de Purview
   - c) Tres: limpieza prioritaria, retención y eDiscovery
   - d) Ninguna si antes se ejecutó la simulación

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. No constituye asesoría legal: las decisiones sobre preservación, exportación, transferencias y privacidad corresponden a tus áreas de Legal, RR. HH. y privacidad. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

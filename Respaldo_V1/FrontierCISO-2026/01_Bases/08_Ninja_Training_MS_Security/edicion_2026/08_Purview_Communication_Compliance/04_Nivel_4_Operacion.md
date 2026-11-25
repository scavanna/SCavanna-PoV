# Nivel 4 · Operación · Modelo operativo, métricas y gobierno

*Microsoft Purview Communication Compliance e Information Barriers Ninja Training · Edición 2026*

[← Nivel 3 · Avanzado](03_Nivel_3_Avanzado.md) · [Índice del programa](README.md) · [Comunidad →](05_Comunidad.md)

<a id="operacion"></a>

Cómo se organiza el equipo con Legal, RR. HH., privacidad, cumplimiento y, cuando corresponde, la representación de los trabajadores: responsabilidades, carga de los revisores, métricas y gobierno en MCSA, sin interpretar la ley.

*L300–L400 · 3 módulos · ~8 horas · 9 recursos*

**Módulos de este nivel:** [O1 Modelo operativo](#o1) · [O2 Métricas y mejora continua](#o2) · [O3 Gobierno, privacidad y MCSA](#o3)

<a id="o1"></a>

## O1 · Modelo operativo del equipo y responsabilidades

*L300–L400 · ~3 h · Origen: Nuevo en esta edición*

Communication Compliance es un programa, no una consola. Microsoft recomienda involucrar desde el inicio a TI, cumplimiento, privacidad, seguridad, RR. HH. y Legal, separar políticas por región y asignar revisores que hablen el idioma de las personas supervisadas. A eso se suman, en muchas organizaciones de MCSA, la representación de los trabajadores o el comité que corresponda cuando la ley o un contrato colectivo lo exigen, los dueños de negocio que definen las barreras de información y los administradores de colaboración que las mantienen.

El modelo operativo responde quién aprueba cada política, quién la configura, quién revisa y en qué plazo, quién decide notificar o escalar, cómo se rota y capacita a los revisores, cómo se gestiona su carga de trabajo y cómo se cierra el ciclo con RR. HH. y Legal. Este módulo te ayuda a escribirlo como una matriz RACI y un procedimiento de revisión, sin interpretar la ley: las decisiones legales y laborales son de Legal, RR. HH. y privacidad.

**Por qué importa**

La mayoría de los programas de supervisión fracasan por organización, no por tecnología: alertas sin dueño, revisores saturados o decisiones disciplinarias sin criterio. Un modelo operativo claro reduce el tiempo de revisión, protege a los revisores y a las personas supervisadas, y deja trazabilidad de cada decisión ante auditorías y reguladores.

**Qué vas a lograr**

- Identificar a las partes interesadas de Communication Compliance e Information Barriers y sus decisiones.
- Construir una matriz RACI para políticas, revisión, escalamiento, IA, conectores y barreras.
- Dimensionar la carga de revisión con muestreo, filtros y pilotos por departamento.
- Definir el procedimiento de revisión, la capacitación y la rotación de revisores.

> **Consejo Ninja.** Partes interesadas recomendadas: TI, cumplimiento, privacidad, seguridad, RR. HH. y Legal; además, conviene separar políticas por región y usar revisores que hablen el idioma de las personas supervisadas ([planificación de CC](https://learn.microsoft.com/es-es/purview/communication-compliance-plan), [planificación de IRM](https://learn.microsoft.com/en-us/purview/insider-risk-management-plan)).

> **Atención.** Separación de funciones: los administradores de CC configuran políticas y los analistas e investigadores revisan alertas. No asignes ambas funciones a la misma persona fuera del laboratorio ([guía de privacidad](https://learn.microsoft.com/en-us/purview/insider-risk-solution-privacy)).

> **Consejo Ninja.** Una guía independiente revisada el 5 de septiembre de 2026 recomienda pilotos acotados por departamento o por clasificador, muestreo para poblaciones grandes y vigilancia de falsos positivos durante las primeras semanas; algunas descripciones de roles simplifican la documentación oficial, así que contrástalas ([Solving Microsoft 365](https://solvingmicrosoft365.com/guides/purview-communication-compliance/)).

**¿Tienes poco tiempo?**

- [Plan for Communication Compliance](https://learn.microsoft.com/en-us/purview/communication-compliance-plan) · Documentación
- [Plan for Insider Risk Management](https://learn.microsoft.com/en-us/purview/insider-risk-management-plan) · Documentación
- [Purview Communication Compliance (Solving Microsoft 365 guide)](https://solvingmicrosoft365.com/guides/purview-communication-compliance/) · Blog

**Matriz RACI de referencia para Communication Compliance e Information Barriers**

| Actividad | Responsable (R) | Aprueba (A) | Consultado (C) | Informado (I) |
|---|---|---|---|---|
| Definir finalidad, alcance y población de una política | Administrador de CC | Comité de gobierno (Legal, RR. HH., privacidad y cumplimiento) | Representación de los trabajadores si aplica; seguridad | Dirección del área supervisada |
| Configurar políticas, condiciones y diccionarios | Administrador de CC | Oficial de cumplimiento | Privacidad; revisores | Auditoría interna |
| Probar condiciones y pasar de piloto a producción | Administrador de CC | Comité de gobierno | Revisores; privacidad | RR. HH. |
| Revisar alertas y documentar el criterio | Revisores (Analysts) | Supervisor de revisión | Investigadores | — |
| Notificar a una persona | Revisor | RR. HH. | Legal | Supervisor de revisión |
| Escalar para investigación (eDiscovery Premium) | Investigador | Legal | RR. HH.; privacidad | Comité de gobierno |
| Activar el desencadenante de Insider Risk | Administradores de CC y de IRM | Comité de gobierno | Seguridad; RR. HH. | Privacidad |
| Supervisar prompts de Copilot y otras IA | Administrador de CC | Privacidad, Legal y dueño del presupuesto | Seguridad; TI | Comité de gobierno |
| Contratar y operar conectores de terceros | Administrador de conectores (Data Connector Admin) | Legal y compras | Cumplimiento; privacidad | TI |
| Diseñar segmentos y políticas de Information Barriers | Administrador de colaboración | Cumplimiento y dueños de negocio | Legal; TI | Personas afectadas (comunicación previa) |
| Ejecutar el reporte de cumplimiento de IB tras cada cambio | Administrador de colaboración | Cumplimiento | — | Auditoría interna |
| Revisar accesos de revisores y exportar la auditoría | Privacidad | Comité de gobierno | Administrador de CC | Auditoría interna |
| Revisión trimestral de políticas y métricas | Administrador de CC | Comité de gobierno | Revisores; RR. HH. | Dirección |

Matriz de referencia de esta guía, basada en las partes interesadas de la [planificación de CC](https://learn.microsoft.com/es-es/purview/communication-compliance-plan) y en la separación de funciones de la [guía de privacidad](https://learn.microsoft.com/en-us/purview/insider-risk-solution-privacy). Adáptala a tu organización con Legal y RR. HH.

### Documentación, cursos y credenciales

- [Plan for Communication Compliance](https://learn.microsoft.com/en-us/purview/communication-compliance-plan) · Documentación · Oficial · Microsoft Learn. Planificación: partes interesadas (TI, cumplimiento, privacidad, seguridad, RR. HH., legal), flujo de investigación, seis grupos de roles, usuarios en alcance y revisores.
- [Plan for Insider Risk Management](https://learn.microsoft.com/en-us/purview/insider-risk-management-plan) · Documentación · Oficial · Microsoft Learn. Modelo de gobierno reutilizable para CC: involucrar a TI, cumplimiento, privacidad, seguridad, RR. HH. y legal, separar políticas por región y usar revisores que hablen el idioma de los usuarios.

### Comunidad: blogs, libros, newsletters y eventos

- [Purview Communication Compliance (Solving Microsoft 365 guide)](https://solvingmicrosoft365.com/guides/purview-communication-compliance/) · Blog · Comunidad · Nuevo · Emil Björk · Solving Microsoft 365 · 5 sep 2026. Guía práctica de operación: separación de funciones entre roles, piloto acotado por departamento o clasificador, muestreo para poblaciones grandes y vigilancia de falsos positivos durante las primeras semanas.

**Manos a la obra**

1. `Laboratorio` Construye la matriz RACI de CC e IB de tu organización a partir de la tabla de este módulo y valídala en una revisión con RR. HH., Legal y privacidad; guarda la versión aprobada ([planificación de CC](https://learn.microsoft.com/es-es/purview/communication-compliance-plan)).
2. `Laboratorio` Dimensiona la carga de revisión de una política piloto: mensajes analizados por día, porcentaje de revisión, minutos por alerta y revisores necesarios; documenta los supuestos y cuándo los revisarás ([investigar y remediar](https://learn.microsoft.com/es-es/purview/communication-compliance-investigate-remediate)).
3. `Laboratorio` Redacta el procedimiento de revisión (plazos, criterios, notas del revisor, escalamiento, rotación y capacitación) y pruébalo con alertas sintéticas de tu laboratorio ([planificación de IRM](https://learn.microsoft.com/en-us/purview/insider-risk-management-plan)).
4. `Solo producción` Pon en marcha el piloto con personas reales. Por qué: implica supervisar a empleados. Práctica segura: aprobación escrita de Legal, RR. HH. y privacidad (y de la representación de los trabajadores si corresponde), aviso a las personas, alcance mínimo por departamento, seudonimización, revisores fuera de la línea jerárquica y fecha de revisión del piloto con criterios de suspensión ([planificación de CC](https://learn.microsoft.com/es-es/purview/communication-compliance-plan)).

<a id="o2"></a>

## O2 · Métricas, reportes y mejora continua

*L300–L400 · ~2 h · Origen: Nuevo en esta edición (amplía la sección de ajuste de condiciones del Ninja oficial)*

Lo que no se mide no mejora. Communication Compliance entrega los datos de base: mensajes analizados hoy, pendientes nuevos del día (el contador se reinicia cada día en UTC), resueltos y escalados, almacenamiento por política con avisos al 80, 90 y 95 %, y el consumo de registros de texto de pago por uso. A eso se suman los falsos positivos por clasificador e idioma, que puedes reportar con «Report as Misclassified», y las recomendaciones de Policy health (vista previa), como filtrar envíos masivos.

La mejora continua se apoya en técnicas conocidas: Filter email blasts, condiciones con NOT, diccionarios en español y combinaciones de tipos de información confidencial, siguiendo el modelo de despliegue de Microsoft para reducir falsos positivos, pensado para DLP y profundizado en el programa de DLP (módulo M1). La nota de transparencia de CC explica cómo evaluar el desempeño de sus modelos, y la métrica de efectividad de alertas de Insider Risk Management sirve de referencia para definir una equivalente.

**Por qué importa**

Los indicadores convierten la supervisión en una conversación de gestión: cuántas horas de revisión consume cada política, cuántas alertas terminan en una acción, cuánto cuesta la IA supervisada y qué política está por llenarse. Con esos datos, el comité de gobierno puede ajustar alcance, recursos y presupuesto con evidencia y no con percepciones.

**Qué vas a lograr**

- Definir un tablero de indicadores de CC e IB con fuente, frecuencia y responsable.
- Medir falsos positivos por clasificador e idioma y planificar su reducción.
- Vigilar el almacenamiento por política y el consumo de pago por uso.
- Establecer un ciclo trimestral de revisión de políticas con el comité de gobierno.

> **Consejo Ninja.** Métricas de base de la solución: mensajes analizados hoy, pendientes nuevos de hoy (el contador se reinicia cada día en UTC), resueltos y escalados ([investigar y remediar](https://learn.microsoft.com/es-es/purview/communication-compliance-investigate-remediate)). Súmales el almacenamiento por política (avisos al 80, 90 y 95 %) y los registros de texto de pago por uso ([modelos de facturación](https://learn.microsoft.com/en-us/purview/purview-billing-models)).

> **Novedad.** La nota de transparencia de Communication Compliance describe usos previstos, métricas para evaluar el desempeño de sus modelos, factores operativos y limitaciones, e incluye «Report as Misclassified» para retroalimentar clasificadores ([nota de transparencia](https://learn.microsoft.com/en-us/purview/communication-compliance-solution-overview)).

> **Consejo Ninja.** El modelo de despliegue para reducir falsos positivos (actualizado el 3 de abril de 2026) está pensado para DLP, pero su secuencia de SIT, EDM, clasificadores y huellas digitales se aplica a las condiciones de CC, recordando que CC no admite clasificadores personalizados ([modelo de despliegue](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-reduce-false-positives)). Como referencia de efectividad, IRM publica la métrica «Policy alert effectiveness» ([políticas de IRM](https://learn.microsoft.com/en-us/purview/insider-risk-management-policies)).

**¿Tienes poco tiempo?**

- [Communication Compliance (solution overview / transparency)](https://learn.microsoft.com/en-us/purview/communication-compliance-solution-overview) · Documentación
- [Reduce false positives by using SITs and advanced classifiers (Microsoft Purview deployment model)](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-reduce-false-positives) · Documentación
- [MC920304 - Microsoft Purview | Communication Compliance: Policy alerts improvements](https://mc.merill.net/message/MC920304) · Herramienta

**Indicadores de Communication Compliance e Information Barriers**

| Indicador | Qué mide | Fuente de datos | Frecuencia | Para qué decisión |
|---|---|---|---|---|
| Pendientes nuevos de hoy | Coincidencias nuevas del día (el contador se reinicia cada día en UTC) | Página de alertas de CC | Diaria | Asignar revisores |
| Antigüedad de los pendientes | Días entre la coincidencia y la decisión del revisor | Coincidencias y auditoría (SupervisoryReviewTag) | Semanal | Cumplir el plazo de revisión acordado |
| Resueltos y escalados | Decisiones del período por política | Página de la política y reportes | Semanal | Medir el flujo de trabajo |
| Falsos positivos por clasificador e idioma | Coincidencias sin infracción o reportadas con «Report as Misclassified» | Etiquetas y decisiones del revisor | Mensual | Ajustar condiciones, diccionarios y Filter email blasts |
| Efectividad de las alertas | Proporción de alertas que terminan en notificar, escalar o remediar | Reportes y auditoría | Mensual | Mantener o retirar una política (referencia: la métrica de efectividad de IRM) |
| Almacenamiento por política | Uso frente a 100 GB o 1 millón de mensajes | Avisos al 80, 90 y 95 % | Semanal | Copiar la política antes de que se desactive |
| Registros de texto de pago por uso | Consumo por política y medidor (estándar o premium) | Centro de uso y Cost Management | Semanal | Controlar el presupuesto de la supervisión de IA |
| Cambios en políticas | Creaciones, cambios y eliminaciones | Auditoría (SupervisionPolicyCreated, Updated y Deleted) | Mensual | Control de cambios y gobierno |
| Accesos de revisores | Quién revisó qué alertas | Auditoría | Mensual | Informe a privacidad |
| Sitios incompatibles con IB | Sitios, OneDrive y contenedores con segmentos incompatibles | Reporte de cumplimiento de IB | Tras cada cambio de política | Corregir segmentos |
| Cobertura de canales | Canales en uso frente a canales supervisados | Matriz de canales | Trimestral | Cerrar puntos ciegos |
| Capacitación de revisores | Revisores con capacitación vigente | Registro de capacitación | Trimestral | Calidad y defensa del programa |

Fuentes: [investigar y remediar](https://learn.microsoft.com/es-es/purview/communication-compliance-investigate-remediate), [políticas](https://learn.microsoft.com/en-us/purview/communication-compliance-policies), [modelos de facturación](https://learn.microsoft.com/en-us/purview/purview-billing-models), [nota de transparencia](https://learn.microsoft.com/en-us/purview/communication-compliance-solution-overview) y [políticas de IRM](https://learn.microsoft.com/en-us/purview/insider-risk-management-policies). La selección de indicadores es una propuesta de esta guía.

### Documentación, cursos y credenciales

- [Communication Compliance (solution overview / transparency)](https://learn.microsoft.com/en-us/purview/communication-compliance-solution-overview) · Documentación · Oficial · Microsoft Learn. Nota de transparencia: capacidades, usos previstos, métricas para evaluar desempeño, factores operativos y limitaciones de los modelos de Communication Compliance.
- [Reduce false positives by using SITs and advanced classifiers (Microsoft Purview deployment model)](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-reduce-false-positives) · Documentación · Oficial · Microsoft Purview Product Engineering · Microsoft Learn (Purview deployment models) · 3 abr 2026. Modelo de despliegue de ingeniería en 4 pasos (SIT, EDM, clasificadores entrenables, huellas digitales) para reducir falsos positivos, la fatiga de alertas y los costos operativos.

### Laboratorios, GitHub y herramientas

- [MC920304 - Microsoft Purview | Communication Compliance: Policy alerts improvements](https://mc.merill.net/message/MC920304) · Herramienta · Oficial · Vista previa · Nuevo · Microsoft (Message Center) · Microsoft 365 Message Center Archive (mc.merill.net) · 22 oct 2026. Aviso con historial de versiones: CC permitirá personalizar por política la frecuencia de alertas y los destinatarios de correos; la versión preliminar pública se retrasó a octubre de 2026 y la GA mundial está por anunciarse. *Nota:* Roadmap 181825; el cronograma cambió varias veces (antes julio-agosto de 2025). Contrasta con RM529852 (GA enero 2026 para GCC/GCCH/DoD)

**Manos a la obra**

1. `Laboratorio` Define un tablero con 8 a 10 indicadores (fuente, frecuencia y responsable) a partir de la tabla de este módulo y calcula los valores de tu laboratorio ([nota de transparencia](https://learn.microsoft.com/en-us/purview/communication-compliance-solution-overview)).
2. `Laboratorio` Mide la tasa de falsos positivos por clasificador e idioma sobre 30 mensajes sintéticos y propón un ajuste (Filter email blasts, NOT o diccionario) para el peor caso ([modelo de despliegue](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-reduce-false-positives)).
3. `Laboratorio` Define qué harás cuando una política llegue al 80, 90 y 95 % de almacenamiento y revisa en el centro de uso cómo seguirías el consumo de pago por uso ([políticas](https://learn.microsoft.com/en-us/purview/communication-compliance-policies), [uso y facturación](https://learn.microsoft.com/en-us/purview/purview-billing-usage)).
4. `Laboratorio parcial` Configura las alertas por política (frecuencia y destinatarios) si ya están disponibles en tu tenant. Limitación: la vista previa mundial se retrasó a octubre de 2026 y puede no estar habilitada; si no la ves, documenta el estado y la fecha de revisión ([MC920304](https://mc.merill.net/message/MC920304)).

<a id="o3"></a>

## O3 · Gobierno, privacidad y cumplimiento normativo en MCSA

*L300–L400 · ~3 h · Origen: Nuevo en esta edición*

Supervisar comunicaciones de personas toca derechos fundamentales y normas laborales, y Microsoft lo dice expresamente: la responsabilidad legal de monitorear, bloquear o retener contenido es de la organización, que debe consultar asesoría legal antes de desplegar clasificadores. En MCSA el marco se mueve: México publicó una nueva LFPDPPP el 20 de marzo de 2025; Chile tiene la Ley 21.719, vigente desde el 1 de diciembre de 2026, con una nueva Agencia de Protección de Datos Personales; Perú renovó el reglamento de la Ley 29733 (DS 016-2024-JUS) con un oficial de datos personales y la notificación de incidentes en 48 horas.

Este módulo no interpreta esas normas: te da un método para que Legal, RR. HH., privacidad, cumplimiento y, cuando corresponda, la representación de los trabajadores decidan con información técnica precisa. Verás qué decisiones necesitan aprobación, qué evidencia conservar y cómo usar la hoja «Normativa MCSA» del libro de Excel como agenda de la conversación con Legal en cada país. Los marcos regulatorios como evaluaciones se profundizan en el programa de Compliance Manager.

**Por qué importa**

Un despliegue técnicamente impecable puede ser ilegal o éticamente inaceptable si no tiene base legal, aviso a las personas o proporcionalidad. Un gobierno explícito, con aprobaciones y evidencia, protege a las personas supervisadas, a los revisores y a la organización, y es lo que permite sostener el programa ante un regulador, un tribunal o un comité de ética.

**Qué vas a lograr**

- Identificar las decisiones de CC e IB que requieren aprobación de Legal, RR. HH., privacidad o la representación de los trabajadores.
- Preparar un expediente de gobierno con finalidad, alcance, controles y evidencia.
- Ubicar las normas de privacidad de MCSA relevantes con sus fuentes oficiales, sin interpretarlas.
- Planificar la revisión periódica del programa ante cambios normativos.

> **Atención.** Microsoft deja la responsabilidad legal de monitorear, bloquear o retener contenido en la organización y recomienda consultar asesoría legal antes de desplegar clasificadores ([definiciones de clasificadores](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions)). Esta guía no es asesoría legal ni laboral.

> **Novedad.** Chile: la Ley 21.719, publicada el 13 de diciembre de 2024, entra en vigencia el 1 de diciembre de 2026 y crea la Agencia de Protección de Datos Personales ([Ley 21.719](https://www.bcn.cl/leychile/navegar?i=1209272&f=2026-12-01)). México: la nueva LFPDPPP se publicó en el DOF el 20 de marzo de 2025 ([LFPDPPP](https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPDPPP.pdf?version=published)).

> **Atención.** Perú: el reglamento de la Ley 29733 (DS 016-2024-JUS) incorpora el oficial de datos personales y la notificación de incidentes en 48 horas; la ANPD indica vigencia desde el 31 de marzo de 2025, mientras algunas firmas legales citan el 30 de marzo ([DS 016-2024-JUS](https://www.gob.pe/institucion/anpd/normas-legales/6554453)). Confírmalo con Legal.

> **Consejo Ninja.** El libro de Excel incluye la hoja «Normativa MCSA» con normas de privacidad, ciberseguridad y sector financiero por país. Úsala como agenda de la conversación con Legal, no como interpretación: en la tabla de este módulo verás las de privacidad resumidas.

**¿Tienes poco tiempo?**

- [Ley Federal de Protección de Datos Personales en Posesión de los Particulares (México, texto vigente)](https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPDPPP.pdf?version=published) · Documentación
- [Ley 21.719 que regula la protección y el tratamiento de los datos personales y crea la Agencia de Protección de Datos Personales (Chile)](https://www.bcn.cl/leychile/navegar?i=1209272&f=2026-12-01) · Documentación
- [Decreto Supremo N.° 016-2024-JUS - Reglamento de la Ley N.° 29733, Ley de Protección de Datos Personales (Perú)](https://www.gob.pe/institucion/anpd/normas-legales/6554453) · Documentación

**Normas de privacidad de MCSA para llevar a la conversación con Legal (resumen de la hoja «Normativa MCSA»)**

| País | Norma | Autoridad | Dato de referencia | Fuente |
|---|---|---|---|---|
| México | LFPDPPP (nueva ley, DOF 20 de marzo de 2025) | Secretaría Anticorrupción y Buen Gobierno (asumió las funciones del INAI) | Aviso de privacidad y medidas de seguridad; aviso inmediato al titular ante vulneraciones significativas (art. 19) | [LFPDPPP](https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPDPPP.pdf) |
| Colombia | Ley 1581 de 2012 y Decreto 1377 de 2013 | Superintendencia de Industria y Comercio | Autorización del titular, políticas de tratamiento y reporte de incidentes en 15 días hábiles | [Ley 1581](http://www.secretariasenado.gov.co/senado/basedoc/ley_1581_2012.html) |
| Chile | Ley 21.719 | Agencia de Protección de Datos Personales | Vigente desde el 1 de diciembre de 2026; notificación a la Agencia sin dilaciones indebidas | [Ley 21.719](https://www.leychile.cl/leychile/Navegar?idNorma=1209272&idParte=1) |
| Perú | Ley 29733 y DS 016-2024-JUS | Autoridad Nacional de Protección de Datos Personales | Oficial de datos personales; 48 horas a la ANPD para ciertos incidentes | [Reglamento](https://cdn.www.gob.pe/uploads/document/file/7756037/6554453-reglamento-de-la-ley-n-29733.pdf?v=1741726731) |
| Argentina | Ley 25.326 y Decreto 1558/2001 | Agencia de Acceso a la Información Pública | Sin plazo legal específico de notificación; la Res. AAIP 47/2018 recomienda gestionar y documentar incidentes | [Ley 25.326](https://www.argentina.gob.ar/normativa/nacional/norma-64790/actualizacion) |
| Ecuador | LOPDP, reglamento y norma técnica de notificación | Superintendencia de Protección de Datos Personales | 5 días a la SPDP desde que se conoce la vulneración | [LOPDP](https://www.gob.ec/sites/default/files/regulations/2025-01/01%20Ley%20Org%C3%A1nica%20de%20Protecci%C3%B3n%20de%20Datos%20Personales.pdf) |
| Uruguay | Ley 18.331 y Decreto 64/020 | Unidad Reguladora y de Control de Datos Personales | 72 horas a la URCDP desde que se conoce la vulneración | [Decreto 64/020](https://www.impo.com.uy/bases/decretos/64-2020/4) |
| Costa Rica | Ley 8968 y su reglamento | PRODHAB | 5 días hábiles para informar al titular (confirmar en el texto consolidado) | [Ley 8968](http://pgrweb.go.cr/TextoCompleto/NORMAS/1/VIGENTE/D/2010-2019/2010-2014/2012/12270/74352_115361-3.html) |
| Panamá | Ley 81 de 2019 y Decreto Ejecutivo 285 de 2021 | ANTAI | 72 horas desde que se conoce el incidente | [Reglamentación](https://antai.gob.pa/wp-content/uploads/2021/05/Reglamentacio%CC%81n-de-Ley-81-de-Proteccio%CC%81n-de-Datos-Personales.pdf) |
| Paraguay | Ley 7593/2025 | Agencia Nacional de Protección de Datos Personales (en creación) | Plena vigencia prevista para fines de noviembre de 2027; 72 horas a la autoridad | [Ley 7593/2025](https://www.bacn.gov.py/leyes-paraguayas/12924/ley-n-75932025--de-proteccin-de-datos-personales-en-la-repblica-del-paraguay) |
| El Salvador | Ley para la Protección de Datos Personales (Decreto Legislativo 144) | Agencia de Ciberseguridad del Estado | 72 horas a la ACE, a la Fiscalía General y a los titulares afectados | [Decreto 144](https://www.asamblea.gob.sv/sites/default/files/documents/decretos/F6986BF6-25C7-428B-9B74-325A6760AC2C.pdf) |
| Nicaragua | Ley 787 y Decreto 36-2012 | Dirección de Protección de Datos Personales | Principios, derechos de los titulares y deberes de seguridad | [Ley 787](http://legislacion.asamblea.gob.ni/normaweb.nsf/9e314815a08d4a6206257265005d21f9/e5d37e9b4827fc06062579ed0076ce1d) |
| Guatemala | Sin ley general de datos personales (iniciativa en el Congreso, 2025) | Congreso de la República | La protección se apoya en el habeas data constitucional | [Iniciativa](https://www.congreso.gob.gt/noticias_congreso/13884/2025/) |

Resumen de la hoja «Normativa MCSA» del libro de Excel; no es asesoría legal ni una interpretación. Para Honduras, Bolivia y Venezuela la hoja registra normas financieras o penales, no una ley general de datos. Confirma cada dato con Legal en el texto oficial vigente.

### Documentación, cursos y credenciales

- [Ley 21.719 que regula la protección y el tratamiento de los datos personales y crea la Agencia de Protección de Datos Personales (Chile)](https://www.bcn.cl/leychile/navegar?i=1209272&f=2026-12-01) · Documentación · Comunidad · ES · Congreso Nacional de Chile · Biblioteca del Congreso Nacional de Chile (LeyChile) · 5 feb 2026. Nueva ley chilena de datos personales (publicada el 13-dic-2024, vigente desde el 01-dic-2026) con derechos de acceso, rectificación, supresión, oposición, portabilidad y bloqueo, datos sensibles, modelos de cumplimiento y una nueva Agencia con potestad sancionatoria.
- [Ley Federal de Protección de Datos Personales en Posesión de los Particulares (México, texto vigente)](https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPDPPP.pdf?version=published) · Documentación · Comunidad · ES · Congreso de la Unión · Cámara de Diputados de México · 14 nov 2025. Nueva LFPDPPP publicada en el DOF el 20-mar-2025 (última reforma DOF 14-11-2025) que define datos sensibles, disociación, avisos de privacidad y derechos ARCO, relevantes para supervisar comunicaciones de empleados.
- [Decreto Supremo N.° 016-2024-JUS - Reglamento de la Ley N.° 29733, Ley de Protección de Datos Personales (Perú)](https://www.gob.pe/institucion/anpd/normas-legales/6554453) · Documentación · Comunidad · ES · Ministerio de Justicia y Derechos Humanos del Perú · Autoridad Nacional de Protección de Datos Personales (gob.pe) · 30 nov 2024. Nuevo reglamento peruano de protección de datos: alcance extraterritorial, oficial de datos personales, notificación de incidentes en 48 horas y documento de seguridad con controles de acceso y auditoría.

**Manos a la obra**

1. `Laboratorio` Prepara el expediente de gobierno de una política: finalidad, población, canales, clasificadores, seudonimización, conservación, revisores, aprobaciones y fecha de revisión, usando la tabla «Gobierno y privacidad de la supervisión» ([guía de privacidad](https://learn.microsoft.com/en-us/purview/insider-risk-solution-privacy)).
2. `Laboratorio` Con la tabla de este módulo y la hoja «Normativa MCSA», arma para cada país donde operas una lista de preguntas para Legal (base de licitud, aviso, datos sensibles, derechos de los titulares, transferencias y conservación), sin responderlas tú ([Ley 21.719](https://www.bcn.cl/leychile/navegar?i=1209272&f=2026-12-01), [LFPDPPP](https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPDPPP.pdf?version=published)).
3. `Laboratorio` Define el calendario de revisión del programa: revisión anual del expediente, revisión extraordinaria ante cambios normativos (por ejemplo, la entrada en vigencia de la Ley 21.719 el 1 de diciembre de 2026) y responsables ([DS 016-2024-JUS](https://www.gob.pe/institucion/anpd/normas-legales/6554453)).
4. `Solo producción` Presenta el programa al comité de gobierno o de ética y obtén la aprobación formal. Por qué: requiere decisiones de la organización y, según el país o el contrato colectivo, consulta a la representación de los trabajadores. Práctica segura: expediente completo, versión piloto acotada, criterios de suspensión y revisión anual ([planificación de CC](https://learn.microsoft.com/es-es/purview/communication-compliance-plan)).

<a id="reto-operacion"></a>

## Reto del nivel

**Expediente de gobierno ante el comité.** Prepara el expediente para aprobar un piloto real de Communication Compliance: finalidad, población, canales, plantillas y clasificadores (con sus límites de idioma), seudonimización, revisores y matriz RACI, conservación de coincidencias, métricas y umbrales, costos de pago por uso, preguntas para Legal por país (sin interpretarlas), aviso a las personas y consulta a la representación de los trabajadores si corresponde. Formato: diez minutos de exposición y una página de resumen ejecutivo.

<a id="quiz-operacion"></a>

## Evaluación del nivel

Responde y compara con [Evaluaciones y respuestas](06_Evaluaciones_y_respuestas.md#eval-operacion). Con 80 % o más, ¡nivel aprobado! (En la versión web puedes corregir en línea y generar tu certificado).

1. ¿Qué partes interesadas recomienda Microsoft involucrar al planificar Communication Compliance?
   - a) TI y seguridad; Legal y RR. HH. solo si hay un incidente
   - b) TI, cumplimiento, privacidad, seguridad, RR. HH. y Legal
   - c) Cumplimiento y Legal; TI solo ejecuta
   - d) El SOC y el administrador global

2. ¿Qué recomienda la planificación sobre políticas y revisores en organizaciones con varios países?
   - a) Que los revisores sean los gerentes directos de las personas supervisadas
   - b) Una sola política global con revisores centralizados que trabajen en inglés
   - c) Separar políticas por región y usar revisores que hablen el idioma de los usuarios
   - d) Que los revisores sean administradores globales para ver todas las alertas

3. ¿Cómo se reparte la separación de funciones en Communication Compliance?
   - a) Los administradores configuran políticas; analistas e investigadores revisan alertas
   - b) Un mismo rol configura, revisa e investiga para ganar agilidad
   - c) RR. HH. configura las políticas y TI revisa las alertas
   - d) Cada revisor crea y ajusta sus propias políticas

4. El contador de pendientes nuevos de hoy en Communication Compliance…
   - a) Acumula toda la semana
   - b) Se reinicia cada día en UTC
   - c) Se reinicia cada mes
   - d) Nunca se reinicia

5. ¿En qué porcentajes avisa Communication Compliance sobre el almacenamiento de una política?
   - a) 50, 75 y 90 %
   - b) 60, 80 y 100 %
   - c) 80, 90 y 95 %
   - d) Solo al 100 %

6. ¿Qué opción reduce el ruido de boletines y envíos masivos en una política?
   - a) Desactivar el OCR
   - b) Aumentar el porcentaje de revisión
   - c) Agregar más revisores
   - d) Filter email blasts

7. ¿Qué función permite retroalimentar un clasificador cuando una coincidencia es incorrecta?
   - a) Report as Misclassified
   - b) Escalar para investigación
   - c) Quitar mensaje de Teams
   - d) Notificar

8. Según Microsoft, ¿quién es responsable de la legalidad de monitorear, bloquear o retener comunicaciones?
   - a) Microsoft, como proveedor del servicio en la nube
   - b) El proveedor de la app de IA supervisada
   - c) La organización, que debe consultar asesoría legal
   - d) El regulador local, que aprueba cada política

9. ¿Desde cuándo está vigente la Ley 21.719 de Chile?
   - a) 13 de diciembre de 2024
   - b) 20 de marzo de 2025
   - c) 31 de marzo de 2025
   - d) 1 de diciembre de 2026

10. ¿Qué incorpora el reglamento peruano DS 016-2024-JUS según la fuente oficial?
   - a) Un oficial de datos personales y la notificación de incidentes en 48 horas
   - b) La prohibición de supervisar comunicaciones de empleados
   - c) El uso obligatorio de herramientas certificadas de supervisión
   - d) La notificación de incidentes en 30 días hábiles a la ANPD

11. Antes de supervisar las comunicaciones de un grupo piloto de personas reales, ¿qué debes tener?
   - a) Solo la licencia E5 y la seudonimización activa
   - b) Aprobación previa de Legal, RR. HH. y privacidad, aviso a las personas y una política de prueba con alcance acotado
   - c) Un reporte de cumplimiento de IB y la auditoría activa
   - d) La aprobación del administrador global y del gerente del área

12. ¿Qué recomienda una guía independiente para supervisar poblaciones grandes sin saturar a los revisores?
   - a) Revisar siempre el 100 % de los mensajes para no perder nada
   - b) Desactivar la seudonimización para acelerar la revisión
   - c) Concentrar la revisión en un único revisor experto
   - d) Muestreo y pilotos acotados por departamento o clasificador

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. No constituye asesoría legal ni laboral: las decisiones sobre supervisión de comunicaciones, privacidad, avisos a empleados y relaciones laborales corresponden a tus áreas de Legal, RR. HH. y privacidad. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

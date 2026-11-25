# Prácticas de operación: riesgo interno y ciclo de vida de los datos

**Frontier CISO Atlas · Modelo Operativo CISO 365 · versión 2.0, revisión 2** · documento 16 de 16 · 15 de noviembre de 2026 · @SCavanna

> Propuesta de base, sujeta a validación y a calibración en cada organización. La ejecución se puede contratar; la rendición de cuentas, no.

## 1. Qué agrega este documento

El núcleo define funciones, indicadores y resultados clave. Hasta esta revisión no describía la rutina de operación de ninguna disciplina: esa descripción estaba en la serie GM-24 y, para una plataforma concreta, en la edición Microsoft. La revisión 2 incorpora al núcleo dos disciplinas, **riesgo interno** y **ciclo de vida de los datos**, escritas sin nombres de producto, igual que el resto del modelo.

Son 56 rutinas por cadencia: 28 de riesgo interno y 28 de ciclo de vida de los datos. Se apoyan en 14 prácticas que GM-24 V7.1 ya definía y en 24 prácticas nuevas. Ninguna agrega funciones ni indicadores: cada rutina se asigna a una de las 59 funciones existentes.

| Disciplina | Rutinas | Diaria | Semanal | Mensual | Trimestral | Semestral | Anual | Por evento |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Riesgo interno | 28 | 8 | 6 | 5 | 2 | 1 | 1 | 5 |
| Ciclo de vida de los datos | 28 | 8 | 6 | 5 | 2 | 1 | 1 | 5 |

## 2. Cómo leerlo

- **Práctica.** Un enunciado estable, independiente de la herramienta. Las que empiezan con OP- son de TheNextCISO GM-24 V7.1 y se usan sin cambios. Las que empiezan con PR-RI- y PR-CV- son nuevas de esta revisión.
- **Rutina.** La práctica aplicada con una cadencia: qué se hace y qué evidencia mínima deja. El identificador indica la disciplina (RI o CV) y la cadencia (D diaria, S semanal, M mensual, T trimestral, SM semestral, A anual y AH por evento).
- **Función e indicador.** Los del núcleo. Cuando ningún indicador del catálogo mide la rutina, la columna queda vacía; la sección 7 lo resume.
- **Tres momentos de un control.** Un control se configura (una vez, o cuando cambia), se opera con una rutina periódica y se usa para responder cuando ocurre un evento. Este documento cubre la rutina y la respuesta. La configuración depende de la plataforma y queda en la edición que la implementa.

## 3. Riesgo interno

**Propósito.** Detectar, investigar y contener el daño que puede causar quien ya tiene acceso —por descuido, por abuso o por una cuenta comprometida—, con proporcionalidad y respeto de la privacidad.

**Lo que no se delega.** La decisión de investigar a una persona, la doble autorización para capturar evidencia, el estatuto acordado con Legal, Recursos Humanos y privacidad, y la decisión disciplinaria o legal.

**Si un proveedor opera la disciplina.** Un proveedor puede operar el triaje y mantener la plataforma. No puede ver identidades sin seudonimizar salvo autorización escrita, ni cerrar un caso sin la decisión interna.

### Diaria (8)

| ID | Cadencia | Práctica | Qué se hace | Evidencia mínima | Función | Indicador |
|:--:|:--:|---|---|---|---|---|
| RI-D-01 | Diaria | OP-POS-15 Mantener la salud de la ingesta de señales | Comprobar que las fuentes de señales —recursos humanos, acceso físico y dispositivos— siguen entregando datos. | Última importación correcta de cada fuente. | OPE-DE-05 | K173 Fuentes críticas con registro íntegro y retención conforme |
| RI-D-02 | Diaria | OP-SOP-10 Triar incidentes por prioridad dentro del SLA | Triar las alertas de severidad alta dentro del plazo acordado, con la identidad seudonimizada. | Cola del día sin alertas altas fuera de plazo. | OPE-DE-01 | K168 Alertas de severidad alta clasificadas dentro del objetivo |
| RI-D-03 | Diaria | OP-SOP-30 Investigar riesgo interno con proporcionalidad y privacidad | Analizar las secuencias de actividad y la salida acumulada de datos antes de abrir o descartar un caso. | Nota de análisis en cada alerta escalada o descartada. | OPE-PR-06 | K154 Eventos de salida de datos sensibles resueltos en plazo |
| RI-D-04 | Diaria | OP-POS-19 Vigilar la postura de datos y su uso por IA | Revisar las alertas de uso riesgoso de la IA y de actividad de agentes sobre datos sensibles. | Alertas revisadas y las que pasaron a caso. | OPE-DE-06 | K53 Observabilidad de agentes integrada a la detección |
| RI-D-05 | Diaria | OP-SOP-10 Triar incidentes por prioridad dentro del SLA | Vincular las alertas de riesgo interno con los incidentes de la plataforma de detección y respuesta. | Incidentes con la señal de riesgo interno asociada. | OPE-DE-01 | K168 Alertas de severidad alta clasificadas dentro del objetivo |
| RI-D-06 | Diaria | PR-RI-01 Supervisar, medir y probar los controles que se endurecen según el riesgo de la persona | Supervisar a las personas con nivel de riesgo elevado y los controles que se les endurecieron de forma automática. | Personas en nivel elevado y controles aplicados en el día. | OPE-PR-06 | K154 Eventos de salida de datos sensibles resueltos en plazo |
| RI-D-07 | Diaria | PR-RI-02 Verificar la seudonimización y revisar quién accedió a las alertas y a los casos | Verificar que la seudonimización sigue activa y revisar quién accedió a alertas y casos. | Registro de actividad del programa revisado. | GOB-G6.2 | — |
| RI-D-08 | Diaria | OP-SOP-28 Recolectar evidencia forense con autoridad y registro | Resolver las solicitudes de captura de evidencia sobre una persona con una segunda autorización independiente. | Cada solicitud, con un autorizante distinto del solicitante. | OPE-RS-02 | K190 Evidencia de incidentes preservada con cadena de custodia |

### Semanal (6)

| ID | Cadencia | Práctica | Qué se hace | Evidencia mínima | Función | Indicador |
|:--:|:--:|---|---|---|---|---|
| RI-S-01 | Semanal | OP-SOP-30 Investigar riesgo interno con proporcionalidad y privacidad | Revisar los casos abiertos: avance, notas, cadena de custodia y próxima decisión. | Casos con nota de la semana y custodia documentada. | OPE-RS-02 | K190 Evidencia de incidentes preservada con cadena de custodia |
| RI-S-02 | Semanal | OP-SIG-12 Revisar políticas y excepciones del control | Revisar la salud de las políticas y resolver sus advertencias. | Advertencias resueltas o con fecha. | OPE-PR-06 | — |
| RI-S-03 | Semanal | OP-SOP-19 Revisar tendencias de detección y ajustar políticas | Ajustar umbrales, indicadores y exclusiones para reducir los falsos positivos. | Cambios de ajuste registrados con su efecto. | OPE-DE-02 | K170 Falsos positivos de las detecciones prioritarias |
| RI-S-04 | Semanal | OP-SOP-02 Buscar amenazas por técnicas priorizadas y convertir hallazgos en detecciones | Buscar de forma proactiva la salida de datos que las políticas no detectaron. | Consultas ejecutadas y hallazgos convertidos en ajuste o en caso. | OPE-DE-03 | K44 Campañas de hunting que mejoran la detección |
| RI-S-05 | Semanal | PR-RI-03 Mantener al día los grupos de personas prioritarias y las barreras de información | Actualizar los grupos de personas prioritarias y las barreras de información según altas, bajas y cambios de función. | Grupos actualizados, con fecha y origen del cambio. | GES-M2.2 | — |
| RI-S-06 | Semanal | OP-SOP-22 Mantener la automatización operativa | Verificar las automatizaciones de respuesta y la entrega de alertas a la plataforma de detección. | Prueba de ejecución de cada automatización. | OPE-RS-03 | K55 Incidentes contenidos con respuesta automatizada o asistida por IA |

### Mensual (5)

| ID | Cadencia | Práctica | Qué se hace | Evidencia mínima | Función | Indicador |
|:--:|:--:|---|---|---|---|---|
| RI-M-01 | Mensual | PR-RI-04 Auditar de forma independiente el registro de actividad del programa | Exportar y auditar de forma independiente el registro de actividad del programa antes de que venza su retención. | Exportación archivada y acta de la revisión. | GOB-G3.2 | — |
| RI-M-02 | Mensual | OP-SOP-30 Investigar riesgo interno con proporcionalidad y privacidad | Evaluar la cobertura de las políticas frente a los escenarios de riesgo interno y cerrar las brechas con Legal y privacidad. | Brechas de cobertura con decisión y fecha. | OPE-PR-06 | — |
| RI-M-03 | Mensual | PR-RI-01 Supervisar, medir y probar los controles que se endurecen según el riesgo de la persona | Medir la efectividad de los controles que se endurecen según el riesgo de la persona. | Eventos de riesgo elevado contenidos de forma automática. | OPE-PR-06 | K154 Eventos de salida de datos sensibles resueltos en plazo |
| RI-M-04 | Mensual | OP-IA-02 Revisar desempeño, costo y riesgo de los agentes | Mantener vigente el contexto de los agentes de triaje y controlar su consumo. | Contexto renovado antes de vencer; consumo dentro del presupuesto. | OPE-DE-06 | — |
| RI-M-05 | Mensual | OP-AYI-01 Recertificar accesos privilegiados, no humanos y de agentes | Auditar los roles del programa, la separación de funciones y los accesos privilegiados. | Roles revisados, sin funciones incompatibles acumuladas. | GES-M2.2 | K114 Accesos recertificados en plazo |

### Trimestral (2)

| ID | Cadencia | Práctica | Qué se hace | Evidencia mínima | Función | Indicador |
|:--:|:--:|---|---|---|---|---|
| RI-T-01 | Trimestral | PR-RI-05 Revisar el impacto en la privacidad y el encuadre laboral del programa | Revisar la evaluación de impacto en la privacidad y el encuadre laboral con Legal, Recursos Humanos y el responsable de privacidad. | Evaluación de impacto vigente y acta de la revisión. | GES-M2.1 | K64 Tratamientos de datos personales de alto riesgo con evaluación de impacto |
| RI-T-02 | Trimestral | PR-RI-01 Supervisar, medir y probar los controles que se endurecen según el riesgo de la persona | Probar de punta a punta que el cambio de nivel de riesgo endurece los controles y llega a la plataforma de detección. | Informe de la prueba con tiempos medidos. | GES-M3.2 | K60 Controles clave con efectividad probada |

### Semestral (1)

| ID | Cadencia | Práctica | Qué se hace | Evidencia mínima | Función | Indicador |
|:--:|:--:|---|---|---|---|---|
| RI-SM-01 | Semestral | OP-SIG-11 Convertir lecciones del SOC en concientización | Analizar las lecciones de los casos cerrados y el efecto de los avisos sobre la conducta; llevarlas a la concientización. | Informe semestral con acciones de concientización. | OPE-PR-10 | — |

### Anual (1)

| ID | Cadencia | Práctica | Qué se hace | Evidencia mínima | Función | Indicador |
|:--:|:--:|---|---|---|---|---|
| RI-A-01 | Anual | PR-RI-06 Recertificar el estatuto de gobierno del programa con Legal, Recursos Humanos y privacidad | Recertificar el estatuto de gobierno del programa y ensayar con la dirección un caso de sustracción de información. | Estatuto firmado en el año y acta del ejercicio. | GOB-G6.2 | K15 Ejercicios de crisis con participación ejecutiva |

### Por evento (5)

| ID | Cadencia | Práctica | Qué se hace | Evidencia mínima | Función | Indicador |
|:--:|:--:|---|---|---|---|---|
| RI-AH-01 | Por evento | OP-SOP-30 Investigar riesgo interno con proporcionalidad y privacidad | Investigar con urgencia la posible sustracción de información por una persona que deja la organización o que integra un grupo prioritario. | Expediente del caso con línea de tiempo y decisión. | OPE-RS-02 | K178 Incidentes significativos con causa raíz determinada |
| RI-AH-02 | Por evento | OP-SOP-28 Recolectar evidencia forense con autoridad y registro | Activar la captura de evidencia sobre una persona solo con doble autorización y por tiempo acotado. | Autorización doble, alcance y fecha de fin. | OPE-RS-02 | K190 Evidencia de incidentes preservada con cadena de custodia |
| RI-AH-03 | Por evento | OP-SOP-25 Mantener trazabilidad de escalamientos | Escalar el caso confirmado al proceso legal de preservación y revisión de evidencia. | Caso legal abierto con la evidencia transferida y su custodia. | OPE-RS-02 | K190 Evidencia de incidentes preservada con cadena de custodia |
| RI-AH-04 | Por evento | OP-SOP-11 Investigar y remediar incidentes con evidencia | Responder junto con el equipo de detección y respuesta un incidente que combina amenaza externa y riesgo interno. | Un solo incidente con ambas señales y sus acciones de contención. | OPE-RS-01 | K176 Incidentes gestionados con guía y registro completo |
| RI-AH-05 | Por evento | OP-SOP-11 Investigar y remediar incidentes con evidencia | Contener la exposición de datos sensibles en herramientas de IA generativa o por un agente. | Acceso revocado o agente detenido; alcance documentado. | OPE-RS-03 | K45 Tiempo medio de contención (MTTC) |

## 4. Ciclo de vida de los datos

**Propósito.** Conservar lo que la ley y el negocio exigen, eliminar lo que ya no debe existir y poder demostrar ambas cosas.

**Lo que no se delega.** La tabla de retención, la aprobación de cada disposición, la suspensión de la eliminación ante un litigio y la decisión de usar bloqueos irreversibles.

**Si un proveedor opera la disciplina.** Un proveedor puede aplicar las reglas, vigilar su estado y preparar las revisiones. No aprueba la eliminación ni cambia la tabla de retención.

### Diaria (8)

| ID | Cadencia | Práctica | Qué se hace | Evidencia mínima | Función | Indicador |
|:--:|:--:|---|---|---|---|---|
| CV-D-01 | Diaria | PR-CV-01 Verificar que las reglas de retención están aplicadas y sin errores | Comprobar que las reglas de retención y las etiquetas de registro están distribuidas y sin errores. | Estado de distribución sin errores, o incidencia abierta. | GES-M2.1 | K111 Repositorios con política de retención aplicada |
| CV-D-02 | Diaria | PR-CV-02 Auditar los cambios en las reglas de retención y de registro | Revisar los cambios administrativos del día anterior en reglas y etiquetas de retención. | Cambios del día con autor y orden de cambio. | GOB-G3.2 | — |
| CV-D-03 | Diaria | PR-CV-03 Revisar y aprobar la disposición dentro del plazo | Seguir la cola de revisiones de disposición para que ninguna venza ni se apruebe sola. | Cola sin revisiones vencidas. | GES-M2.1 | K111 Repositorios con política de retención aplicada |
| CV-D-04 | Diaria | PR-CV-04 Conciliar los eventos de negocio que inician los plazos de retención | Conciliar los eventos de negocio que inician los plazos de retención. | Eventos del día recibidos y aplicados. | GES-M2.1 | — |
| CV-D-05 | Diaria | PR-CV-05 Controlar las eliminaciones prioritarias con aprobación de varias partes | Supervisar las eliminaciones prioritarias en curso y sus alertas. | Estado y aprobaciones de cada eliminación prioritaria. | OPE-RS-03 | — |
| CV-D-06 | Diaria | PR-CV-06 Preservar la información de las personas que dejan la organización | Verificar que la información de las personas que dejan la organización queda preservada según la regla. | Bajas del día con su preservación confirmada. | GES-M2.1 | K111 Repositorios con política de retención aplicada |
| CV-D-07 | Diaria | PR-CV-07 Vigilar la capacidad del almacenamiento de retención y de archivo | Vigilar la capacidad del almacenamiento de retención y de archivo. | Uso frente al límite, con alerta si supera el umbral. | GES-M2.1 | — |
| CV-D-08 | Diaria | PR-CV-08 Extender la retención a las interacciones con IA y a los agentes | Verificar que las interacciones con IA y los agentes están cubiertos por las reglas de retención. | Aplicaciones de IA del alcance con regla aplicada. | GES-M2.1 | K111 Repositorios con política de retención aplicada |

### Semanal (6)

| ID | Cadencia | Práctica | Qué se hace | Evidencia mínima | Función | Indicador |
|:--:|:--:|---|---|---|---|---|
| CV-S-01 | Semanal | PR-CV-09 Muestrear la precisión de la clasificación automática de retención | Muestrear la precisión de la aplicación automática de etiquetas de retención. | Muestra revisada con su tasa de acierto. | OPE-ID-06 | K110 Cobertura del descubrimiento de datos sensibles |
| CV-S-02 | Semanal | PR-CV-10 Mantener el alcance de las reglas: repositorios nuevos y atributos al día | Revisar que los alcances dinámicos de las reglas siguen alineados con los atributos de personas y de sitios. | Diferencias de alcance corregidas. | GES-M2.1 | K111 Repositorios con política de retención aplicada |
| CV-S-03 | Semanal | PR-CV-03 Revisar y aprobar la disposición dentro del plazo | Reunir a los revisores y resolver las disposiciones pendientes, por etapas. | Acta con las disposiciones aprobadas, extendidas o reclasificadas. | GES-M2.1 | K111 Repositorios con política de retención aplicada |
| CV-S-04 | Semanal | PR-CV-07 Vigilar la capacidad del almacenamiento de retención y de archivo | Revisar el crecimiento de lo retenido y decidir su paso a almacenamiento de archivo. | Tendencia de crecimiento y decisión de archivo. | GES-M2.1 | — |
| CV-S-05 | Semanal | PR-CV-11 Revisar los intentos de alterar o eliminar registros protegidos | Revisar los intentos bloqueados de modificar o eliminar registros y las remociones administrativas de etiquetas. | Intentos revisados y casos derivados. | OPE-DE-01 | — |
| CV-S-06 | Semanal | PR-CV-10 Mantener el alcance de las reglas: repositorios nuevos y atributos al día | Incorporar a las reglas de retención los sitios, los equipos y los agentes nuevos. | Repositorios nuevos con regla asignada. | GES-M2.1 | K111 Repositorios con política de retención aplicada |

### Mensual (5)

| ID | Cadencia | Práctica | Qué se hace | Evidencia mínima | Función | Indicador |
|:--:|:--:|---|---|---|---|---|
| CV-M-01 | Mensual | PR-CV-12 Conservar la prueba de eliminación | Exportar, conciliar y archivar la prueba de eliminación. | Prueba de eliminación del mes archivada y conciliada. | GOB-G3.2 | K57 Obligaciones aplicables mapeadas a controles con evidencia vigente |
| CV-M-02 | Mensual | PR-CV-13 Sanear las retenciones sin fundamento vigente | Medir y sanear las retenciones sin fundamento vigente sobre datos de personas que ya no están. | Retenciones sin causa identificadas y resueltas. | GES-M2.1 | K111 Repositorios con política de retención aplicada |
| CV-M-03 | Mensual | PR-CV-14 Reducir los datos redundantes, obsoletos y triviales antes de exponerlos a la IA | Medir los datos redundantes, obsoletos y triviales expuestos a la IA y verificar su depuración. | Volumen depurado y volumen pendiente. | OPE-PR-06 | K155 Datos sensibles sobreexpuestos corregidos |
| CV-M-04 | Mensual | PR-CV-04 Conciliar los eventos de negocio que inician los plazos de retención | Conciliar los registros basados en eventos que quedaron sin identificador o sin evento. | Registros sin evento identificados y corregidos. | GES-M2.1 | — |
| CV-M-05 | Mensual | OP-AYI-01 Recertificar accesos privilegiados, no humanos y de agentes | Auditar los roles con permiso sobre la retención y la disposición, y su costo. | Roles revisados. | GES-M2.2 | K114 Accesos recertificados en plazo |

### Trimestral (2)

| ID | Cadencia | Práctica | Qué se hace | Evidencia mínima | Función | Indicador |
|:--:|:--:|---|---|---|---|---|
| CV-T-01 | Trimestral | PR-CV-15 Mantener la tabla de retención al día con la norma y con el negocio | Revisar la tabla de retención frente a los cambios normativos y simplificar sus series. | Tabla de retención revisada, con acta. | GOB-G3.1 | K78 Cambios regulatorios evaluados en plazo |
| CV-T-02 | Trimestral | PR-CV-16 Probar que la retención prevalece sobre la eliminación | Probar que la retención prevalece sobre la eliminación y validar los registros migrados. | Informe de la prueba. | GES-M3.2 | K60 Controles clave con efectividad probada |

### Semestral (1)

| ID | Cadencia | Práctica | Qué se hace | Evidencia mínima | Función | Indicador |
|:--:|:--:|---|---|---|---|---|
| CV-SM-01 | Semestral | PR-CV-17 Auditar los bloqueos irreversibles y los registros regulatorios | Auditar los bloqueos irreversibles, los registros regulatorios y el margen frente a los límites de la plataforma. | Informe de auditoría semestral. | GOB-G3.2 | K82 Cobertura del plan de aseguramiento |

### Anual (1)

| ID | Cadencia | Práctica | Qué se hace | Evidencia mínima | Función | Indicador |
|:--:|:--:|---|---|---|---|---|
| CV-A-01 | Anual | PR-CV-15 Mantener la tabla de retención al día con la norma y con el negocio | Recertificar con la dirección la tabla de retención y sus responsables, y ensayar un caso. | Tabla de retención aprobada en el año y acta del ejercicio. | GOB-G3.1 | K77 Obligaciones aplicables con dueño y fecha de revisión |

### Por evento (5)

| ID | Cadencia | Práctica | Qué se hace | Evidencia mínima | Función | Indicador |
|:--:|:--:|---|---|---|---|---|
| CV-AH-01 | Por evento | PR-CV-05 Controlar las eliminaciones prioritarias con aprobación de varias partes | Ejecutar una eliminación prioritaria ante un derrame de datos sensibles, con aprobación de varias partes. | Aprobaciones, alcance y resultado de la eliminación. | OPE-RS-03 | K45 Tiempo medio de contención (MTTC) |
| CV-AH-02 | Por evento | PR-CV-18 Suspender la eliminación y preservar ante un litigio o una brecha | Suspender la disposición y preservar la información ante un litigio o una brecha. | Preservación aplicada, con fecha, alcance y solicitante. | OPE-RS-02 | K190 Evidencia de incidentes preservada con cadena de custodia |
| CV-AH-03 | Por evento | OP-SOP-11 Investigar y remediar incidentes con evidencia | Responder a la desactivación o a la alteración maliciosa de reglas de retención. | Regla restituida; causa y responsable identificados. | OPE-RS-01 | K176 Incidentes gestionados con guía y registro completo |
| CV-AH-04 | Por evento | PR-CV-15 Mantener la tabla de retención al día con la norma y con el negocio | Incorporar a la tabla de retención una regulación nueva o una entidad adquirida. | Series nuevas aprobadas y aplicadas. | GOB-G3.1 | K78 Cambios regulatorios evaluados en plazo |
| CV-AH-05 | Por evento | PR-CV-07 Vigilar la capacidad del almacenamiento de retención y de archivo | Remediar la saturación del almacenamiento de retención. | Capacidad recuperada sin pérdida de datos retenidos. | GES-M2.1 | — |

## 5. Prácticas

### Nuevas en esta revisión (24)

| ID | Disciplina | Tipo | Práctica | Rutinas que la usan |
|:--:|---|---|---|:--:|
| PR-RI-01 | Riesgo interno | Postura | Supervisar, medir y probar los controles que se endurecen según el riesgo de la persona | 3 |
| PR-RI-02 | Riesgo interno | Señales y cambios | Verificar la seudonimización y revisar quién accedió a las alertas y a los casos | 1 |
| PR-RI-03 | Riesgo interno | Acceso e identidad | Mantener al día los grupos de personas prioritarias y las barreras de información | 1 |
| PR-RI-04 | Riesgo interno | Señales y cambios | Auditar de forma independiente el registro de actividad del programa | 1 |
| PR-RI-05 | Riesgo interno | Señales y cambios | Revisar el impacto en la privacidad y el encuadre laboral del programa | 1 |
| PR-RI-06 | Riesgo interno | Señales y cambios | Recertificar el estatuto de gobierno del programa con Legal, Recursos Humanos y privacidad | 1 |
| PR-CV-01 | Ciclo de vida de los datos | Postura | Verificar que las reglas de retención están aplicadas y sin errores | 1 |
| PR-CV-02 | Ciclo de vida de los datos | Señales y cambios | Auditar los cambios en las reglas de retención y de registro | 1 |
| PR-CV-03 | Ciclo de vida de los datos | Operación | Revisar y aprobar la disposición dentro del plazo | 2 |
| PR-CV-04 | Ciclo de vida de los datos | Operación | Conciliar los eventos de negocio que inician los plazos de retención | 2 |
| PR-CV-05 | Ciclo de vida de los datos | Operación | Controlar las eliminaciones prioritarias con aprobación de varias partes | 2 |
| PR-CV-06 | Ciclo de vida de los datos | Operación | Preservar la información de las personas que dejan la organización | 1 |
| PR-CV-07 | Ciclo de vida de los datos | Postura | Vigilar la capacidad del almacenamiento de retención y de archivo | 3 |
| PR-CV-08 | Ciclo de vida de los datos | Postura | Extender la retención a las interacciones con IA y a los agentes | 1 |
| PR-CV-09 | Ciclo de vida de los datos | Postura | Muestrear la precisión de la clasificación automática de retención | 1 |
| PR-CV-10 | Ciclo de vida de los datos | Postura | Mantener el alcance de las reglas: repositorios nuevos y atributos al día | 2 |
| PR-CV-11 | Ciclo de vida de los datos | Operación | Revisar los intentos de alterar o eliminar registros protegidos | 1 |
| PR-CV-12 | Ciclo de vida de los datos | Operación | Conservar la prueba de eliminación | 1 |
| PR-CV-13 | Ciclo de vida de los datos | Postura | Sanear las retenciones sin fundamento vigente | 1 |
| PR-CV-14 | Ciclo de vida de los datos | Postura | Reducir los datos redundantes, obsoletos y triviales antes de exponerlos a la IA | 1 |
| PR-CV-15 | Ciclo de vida de los datos | Señales y cambios | Mantener la tabla de retención al día con la norma y con el negocio | 3 |
| PR-CV-16 | Ciclo de vida de los datos | Operación | Probar que la retención prevalece sobre la eliminación | 1 |
| PR-CV-17 | Ciclo de vida de los datos | Señales y cambios | Auditar los bloqueos irreversibles y los registros regulatorios | 1 |
| PR-CV-18 | Ciclo de vida de los datos | Operación | Suspender la eliminación y preservar ante un litigio o una brecha | 1 |

### De GM-24 V7.1 que estas disciplinas reutilizan (14)

| ID | Tipo | Práctica | Rutinas que la usan |
|:--:|---|---|:--:|
| OP-SOP-10 | Operación | Triar incidentes por prioridad dentro del SLA | 2 |
| OP-SOP-11 | Operación | Investigar y remediar incidentes con evidencia | 3 |
| OP-SOP-02 | Operación | Buscar amenazas por técnicas priorizadas y convertir hallazgos en detecciones | 1 |
| OP-SOP-19 | Postura | Revisar tendencias de detección y ajustar políticas | 1 |
| OP-SOP-22 | Operación | Mantener la automatización operativa | 1 |
| OP-SOP-25 | Operación | Mantener trazabilidad de escalamientos | 1 |
| OP-SOP-28 | Operación | Recolectar evidencia forense con autoridad y registro | 2 |
| OP-SOP-30 | Señales y cambios | Investigar riesgo interno con proporcionalidad y privacidad | 4 |
| OP-POS-15 | Postura | Mantener la salud de la ingesta de señales | 1 |
| OP-POS-19 | Postura | Vigilar la postura de datos y su uso por IA | 1 |
| OP-SIG-11 | Señales y cambios | Convertir lecciones del SOC en concientización | 1 |
| OP-SIG-12 | Señales y cambios | Revisar políticas y excepciones del control | 1 |
| OP-AYI-01 | Acceso e identidad | Recertificar accesos privilegiados, no humanos y de agentes | 2 |
| OP-IA-02 | Gobierno de agentes | Revisar desempeño, costo y riesgo de los agentes | 1 |

## 6. Funciones que sostienen estas disciplinas

Las rutinas se reparten entre 17 funciones. Ninguna de las dos disciplinas tiene una función propia en el núcleo: el riesgo interno se apoya en la protección de datos, en el monitoreo y en la investigación; el ciclo de vida de los datos, en la gestión de activos y datos y en el cumplimiento.

| Función | Nombre | Rutinas de riesgo interno | Rutinas de ciclo de vida |
|:--:|---|:--:|:--:|
| GOB-G3.1 | Requisitos legales, regulatorios y contractuales | — | 3 |
| GOB-G3.2 | Cumplimiento y aseguramiento continuo | 1 | 3 |
| GOB-G6.2 | Liderazgo ético y medición de la efectividad | 2 | — |
| GES-M2.1 | Activos, datos y protección de datos personales | 1 | 13 |
| GES-M2.2 | Gestión de identidades y accesos | 2 | 1 |
| GES-M3.2 | Selección, implementación y evaluación de controles | 1 | 1 |
| OPE-ID-06 | Descubrimiento y clasificación de datos | — | 1 |
| OPE-PR-06 | Protección de datos | 5 | 1 |
| OPE-PR-10 | Concientización y cultura de seguridad | 1 | — |
| OPE-DE-01 | Monitoreo continuo y gestión de alertas | 2 | 1 |
| OPE-DE-02 | Ingeniería y calidad de la detección | 1 | — |
| OPE-DE-03 | Búsqueda proactiva de amenazas | 1 | — |
| OPE-DE-05 | Gestión de registros y telemetría | 1 | — |
| OPE-DE-06 | Observabilidad de IA y agentes | 2 | — |
| OPE-RS-01 | Gestión y coordinación de incidentes | 1 | 1 |
| OPE-RS-02 | Análisis e investigación forense | 5 | 1 |
| OPE-RS-03 | Contención, erradicación y respuesta automatizada | 2 | 2 |

## 7. Lo que el núcleo todavía no mide

De las 56 rutinas, 41 tienen un indicador del catálogo y 15 no. Los indicadores más usados son K111 Repositorios con política de retención aplicada, K190 Evidencia de incidentes preservada con cadena de custodia, K154 Eventos de salida de datos sensibles resueltos en plazo. Esta revisión no agrega indicadores: deja escrito qué falta.

| Disciplina | Medida que falta | Cómo se aproxima hoy |
|---|---|---|
| Riesgo interno | Proporción de alertas de riesgo interno que resultan verdaderas | Se aproxima con K170 (falsos positivos de las detecciones prioritarias). |
| Riesgo interno | Cumplimiento de la seudonimización, de la separación de funciones y de la doble autorización | Sin indicador en el núcleo. |
| Riesgo interno | Corrección de la conducta después de un aviso | Sin indicador en el núcleo. |
| Ciclo de vida de los datos | Disposiciones revisadas en plazo | Sin indicador en el núcleo; K111 mide solo que la regla esté aplicada. |
| Ciclo de vida de los datos | Prueba de eliminación conservada | Se aproxima con K57 (obligaciones con evidencia vigente). |
| Ciclo de vida de los datos | Retenciones sin fundamento vigente | Sin indicador en el núcleo. |
| Ciclo de vida de los datos | Tiempo hasta preservar la información ante un litigio | Se aproxima con K190 (evidencia preservada con cadena de custodia). |

## 8. Cómo entran en el año

| Ciclo | Qué se hace con estas disciplinas |
|---|---|
| Ciclo 1 · Conocer, estabilizar y ordenar | En el diagnóstico se releva si existen el estatuto de gobierno del programa de riesgo interno, la tabla de retención y quién aprueba una disposición. Se acuerda a quién se llama ante un caso (rutinas por evento). |
| Ciclo 2 · Adecuar | Se instalan las rutinas diarias y semanales, con dueño y evidencia. Se decide qué parte opera un proveedor y qué no se delega. |
| Ciclo 3 · Evolucionar y probar | Se ejecutan las pruebas trimestrales: los controles que se endurecen según el riesgo y la precedencia de la retención sobre la eliminación. |
| Ciclo 4 · Demostrar y sostener | Se hacen la auditoría semestral y la recertificación anual, y sus resultados entran en el informe del año. |

Es una secuencia sugerida. La prioridad real sale del diagnóstico: una organización con obligaciones de retención exigentes o con casos recientes de fuga adelanta estas rutinas.

**Dónde se registra.** La hoja «Prácticas de operación» del libro `Frontier_CISO_Atlas_CISO365_Plan_Anual_y_OKR_v2.0.xlsx` lista las 56 rutinas con su práctica, su evidencia mínima, su función y su indicador. En ella se marca qué rutinas ya se ejecutan, quién las opera y quién responde, y se calcula el nivel de operación por disciplina y por cadencia. La provisión de cada función se toma de la hoja Provisión del mismo libro.

## 9. Origen y límites

- **Origen.** Las rutinas provienen de las guías de excelencia operacional 17 (riesgo interno) y 16 (ciclo de vida de los datos y gestión de registros) del repositorio del autor, validadas el 11 de noviembre de 2026. Aquí se reescribieron sin nombres de producto; la edición Microsoft conserva cada tarea con su código.
- **Asignación propuesta.** La práctica, la función y el indicador de cada rutina son una propuesta de esta revisión. Se pueden corregir sin afectar el resto del modelo.
- **Cadencias.** Son las de las guías de origen. Una organización pequeña puede pasar a semanal una rutina diaria si deja escrito el riesgo que acepta.
- **Alcance.** Solo dos disciplinas. Las demás rutinas de operación siguen en GM-24 V7.1 y, para una plataforma concreta, en la edición Microsoft.
- **Privacidad.** El riesgo interno trata datos de personas. Antes de instalar estas rutinas, la función GOB-G3.1 debe confirmar el encuadre legal y laboral aplicable.

---

*Frontier CISO Atlas · Modelo Operativo CISO 365 · versión 2.0, revisión 2 · 15 de noviembre de 2026 · propuesta sujeta a validación · @SCavanna*

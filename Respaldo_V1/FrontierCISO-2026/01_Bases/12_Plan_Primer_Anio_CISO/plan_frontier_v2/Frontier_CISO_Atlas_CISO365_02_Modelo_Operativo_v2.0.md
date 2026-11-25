# Modelo operativo

**Frontier CISO Atlas · Modelo Operativo CISO 365 · versión 2.0, revisión 2** · documento 02 de 16 · 15 de noviembre de 2026 · @SCavanna

> Propuesta de base, sujeta a validación y a calibración en cada organización. La ejecución se puede contratar; la rendición de cuentas, no.

## 1. Principios

| N.º | Principio | Qué significa |
|:--:|---|---|
| 1 | La rendición de cuentas no se delega | Un proveedor o un agente pueden ejecutar una función; quien responde ante el directorio es siempre la organización. |
| 2 | Primero medir, después prometer | El plan nace del diagnóstico y de una línea base; ningún objetivo se compromete sin un valor de partida. |
| 3 | Cada función tiene un dueño | Y cada control, un objetivo, una configuración de referencia y una evidencia. Sin dueño no hay control: hay una herramienta instalada. |
| 4 | Una misma regla para todos los entornos | La política se define una vez y se aplica igual en cada nube, en el centro de datos y en lo que opera un tercero. |
| 5 | El proveedor se gobierna por resultados y se verifica | Niveles de servicio medibles, evidencia periódica, verificación independiente y salida probada. |
| 6 | Ninguna confianza implícita | Ni en la red, ni en el dispositivo, ni en el proveedor, ni en el agente: cada acceso se decide con evidencia. |
| 7 | Los agentes son una tercera clase de trabajador | Junto con las personas y los proveedores: tienen identidad propia, límites, supervisión y retiro. |
| 8 | Lo específico de un proveedor es implementación | El plan se escribe sobre funciones, resultados y estándares abiertos; cada organización lo instancia con su tecnología. |
| 9 | Proporcionalidad | El modelo se ajusta al tamaño, al sector y al riesgo: una organización pequeña usa menos funciones y menos indicadores, no otra lógica. |
| 10 | Lo que no se probó, no se afirma | El nivel «Probado» exige una prueba, un ejercicio o una revisión independiente de los últimos 12 meses. |

## 2. Tres planos y 59 funciones

| Plano | Qué hace | Funciones |
|---|---|:--:|
| Gobierno | Decide y supervisa: fija la dirección, el apetito y las reglas, y rinde cuentas. | 12 |
| Gestión | Planifica, organiza, dota y mejora: convierte las decisiones en un programa con dueños, presupuesto y medición. | 12 |
| Operación | Ejecuta los servicios de cada día: identificar, proteger, detectar, responder y recuperar. | 35 |

Las funciones de gobierno y de gestión corresponden a las 24 unidades de TheNextCISO GM-24. Los 35 servicios de operación se agrupan por las funciones de NIST CSF 2.0: identificar, proteger, detectar, responder y recuperar.

| ID | Función | Plano | Categorías del marco | Dominio Zero Trust | Criticidad |
|---|---|---|---|---|:--:|
| GOB-G1.1 | Contexto, mandato y autoridad del CISO | Gobierno | GV.OC · GV.RR | — | 3 |
| GOB-G1.2 | Estrategia de seguridad y alineación con el negocio | Gobierno | GV.OC · GV.RM | — | 3 |
| GOB-G2.1 | Marcos, estándares y grilla de propiedad | Gobierno | GV.PO · GV.RR | Visibilidad, automatización y gobierno | 2 |
| GOB-G2.2 | Políticas, estándares y procedimientos | Gobierno | GV.PO | Visibilidad, automatización y gobierno | 2 |
| GOB-G3.1 | Requisitos legales, regulatorios y contractuales | Gobierno | GV.OC | — | 3 |
| GOB-G3.2 | Cumplimiento y aseguramiento continuo | Gobierno | GV.OV · ID.IM | Visibilidad, automatización y gobierno | 2 |
| GOB-G4.1 | Gobernanza del riesgo: estructuras y dueños | Gobierno | GV.RM · GV.RR | — | 3 |
| GOB-G4.2 | Apetito de riesgo: definición y comunicación | Gobierno | GV.RM | — | 3 |
| GOB-G5.1 | Supervisión de la evaluación y el análisis de riesgos | Gobierno | ID.RA · GV.OV | — | 3 |
| GOB-G5.2 | Supervisión del tratamiento y la aceptación de riesgos | Gobierno | GV.RM · ID.RA | — | 2 |
| GOB-G6.1 | Comunicación estratégica y reporte a la dirección | Gobierno | GV.OV · GV.RR | — | 3 |
| GOB-G6.2 | Liderazgo ético y medición de la efectividad | Gobierno | GV.OV | IA y agentes | 2 |
| GES-M1.1 | Programa de seguridad y portafolio de productos-control | Gestión | GV.RM · ID.IM | Visibilidad, automatización y gobierno | 3 |
| GES-M1.2 | Finanzas, equipo, proveedores y capacitación | Gestión | GV.RR · PR.AT | — | 3 |
| GES-M2.1 | Activos, datos y protección de datos personales | Gestión | ID.AM · PR.DS | Datos | 3 |
| GES-M2.2 | Gestión de identidades y accesos | Gestión | PR.AA | Identidades | 3 |
| GES-M3.1 | Arquitectura de seguridad e ingeniería (Zero Trust) | Gestión | PR.IR · ID.RA | Visibilidad, automatización y gobierno | 3 |
| GES-M3.2 | Selección, implementación y evaluación de controles | Gestión | PR.PS · ID.IM | Visibilidad, automatización y gobierno | 3 |
| GES-M4.1 | Gestión de las operaciones de seguridad | Gestión | DE.CM · DE.AE | Visibilidad, automatización y gobierno | 3 |
| GES-M4.2 | Gestión de amenazas, vulnerabilidades y riesgos emergentes | Gestión | ID.RA | — | 2 |
| GES-M5.1 | Preparación de la respuesta a incidentes | Gestión | RS.MA · ID.IM | — | 3 |
| GES-M5.2 | Conducción de la respuesta y aprendizaje | Gestión | RS.MA · RS.CO | — | 3 |
| GES-M6.1 | Continuidad, recuperación y resiliencia | Gestión | RC.RP · RC.CO | — | 3 |
| GES-M6.2 | Nube, tecnologías emergentes y cadena de suministro | Gestión | GV.SC | Infraestructura | 3 |
| OPE-ID-01 | Inventario y descubrimiento de activos | Operación | ID.AM | Visibilidad, automatización y gobierno | 3 |
| OPE-ID-02 | Gestión de vulnerabilidades y de la exposición | Operación | ID.RA | Visibilidad, automatización y gobierno | 3 |
| OPE-ID-03 | Postura de nube y de configuración | Operación | ID.RA · PR.PS | Infraestructura | 3 |
| OPE-ID-04 | Evaluación de riesgo de terceros | Operación | GV.SC · ID.RA | — | 3 |
| OPE-ID-05 | Pruebas ofensivas y validación de controles | Operación | ID.RA · ID.IM | Visibilidad, automatización y gobierno | 2 |
| OPE-ID-06 | Descubrimiento y clasificación de datos | Operación | ID.AM | Datos | 3 |
| OPE-ID-07 | Inventario y evaluación de sistemas de IA y agentes | Operación | ID.AM · ID.RA | IA y agentes | 3 |
| OPE-PR-01 | Identidades y accesos de las personas | Operación | PR.AA | Identidades | 3 |
| OPE-PR-02 | Acceso privilegiado | Operación | PR.AA | Identidades | 3 |
| OPE-PR-03 | Identidades no humanas, de cargas y de agentes | Operación | PR.AA | Identidades · IA y agentes | 3 |
| OPE-PR-04 | Protección y gestión de dispositivos | Operación | PR.PS | Dispositivos | 3 |
| OPE-PR-05 | Protección del correo y la colaboración | Operación | PR.DS · PR.PS | Aplicaciones y cargas | 3 |
| OPE-PR-06 | Protección de datos | Operación | PR.DS | Datos | 3 |
| OPE-PR-07 | Seguridad de aplicaciones y del desarrollo | Operación | PR.PS | Aplicaciones y cargas | 3 |
| OPE-PR-08 | Seguridad de red y segmentación | Operación | PR.IR | Red | 3 |
| OPE-PR-09 | Protección de cargas e infraestructura de nube | Operación | PR.PS · PR.IR | Infraestructura | 3 |
| OPE-PR-10 | Concientización y cultura de seguridad | Operación | PR.AT | — | 2 |
| OPE-PR-11 | Protección de sistemas de IA y agentes | Operación | PR.DS · PR.PS | IA y agentes | 3 |
| OPE-PR-12 | Seguridad de tecnología operacional y dispositivos conectados | Operación | PR.IR · PR.PS | Infraestructura | 2 |
| OPE-DE-01 | Monitoreo continuo y gestión de alertas | Operación | DE.CM · DE.AE | Visibilidad, automatización y gobierno | 3 |
| OPE-DE-02 | Ingeniería y calidad de la detección | Operación | DE.AE | Visibilidad, automatización y gobierno | 3 |
| OPE-DE-03 | Búsqueda proactiva de amenazas | Operación | DE.CM | Visibilidad, automatización y gobierno | 2 |
| OPE-DE-04 | Inteligencia de amenazas | Operación | ID.RA · DE.AE | Visibilidad, automatización y gobierno | 2 |
| OPE-DE-05 | Gestión de registros y telemetría | Operación | DE.CM · PR.PS | Visibilidad, automatización y gobierno | 3 |
| OPE-DE-06 | Observabilidad de IA y agentes | Operación | DE.CM | IA y agentes | 3 |
| OPE-RS-01 | Gestión y coordinación de incidentes | Operación | RS.MA | Visibilidad, automatización y gobierno | 3 |
| OPE-RS-02 | Análisis e investigación forense | Operación | RS.AN | Visibilidad, automatización y gobierno | 2 |
| OPE-RS-03 | Contención, erradicación y respuesta automatizada | Operación | RS.MI | Visibilidad, automatización y gobierno | 3 |
| OPE-RS-04 | Comunicación y notificación de incidentes | Operación | RS.CO | — | 3 |
| OPE-RS-05 | Gestión de crisis y ejercicios | Operación | RS.MA · ID.IM | — | 3 |
| OPE-RC-01 | Respaldo y restauración | Operación | RC.RP · PR.DS | Datos | 3 |
| OPE-RC-02 | Recuperación de servicios críticos | Operación | RC.RP | Infraestructura | 3 |
| OPE-RC-03 | Recuperación de la identidad y de la plataforma de control | Operación | RC.RP | Identidades · Infraestructura | 3 |
| OPE-RC-04 | Continuidad y operación degradada | Operación | RC.RP | — | 3 |
| OPE-RC-05 | Comunicación de la recuperación y lecciones aprendidas | Operación | RC.CO · ID.IM | — | 2 |

Cada función tiene, en el catálogo y en el explorador, su propósito, la evidencia que corresponde a «Implementado» y a «Probado», sus indicadores y su versión externalizada.

## 3. Quién opera cada función

| Modelo de provisión | Qué significa |
|---|---|
| Propio | La organización opera la función con personal y herramientas bajo su gestión. |
| Co-gestionado | Un proveedor ejecuta una parte definida; la organización conserva la decisión y opera el resto. |
| Externalizado | Un proveedor opera la función de punta a punta bajo contrato; la organización conserva la rendición de cuentas, las decisiones reservadas y la verificación. |
| No existe | Nadie cumple la función. |

Cuando un proveedor opera una función cambian tres cosas: el objetivo se expresa como resultado contratado, el indicador se mide como nivel de servicio o como dato compartido, y la evidencia la aporta el proveedor y la verifica la organización. No cambia quién responde ante el directorio. El documento 06 «Funciones externalizadas: cómo gobernarlas y medirlas» lo desarrolla.

## 4. Cómo se califica: la escala de evidencia

| Nivel | Nombre | Significado |
|:--:|---|---|
| 0 | No definido | No existe, o depende de la memoria de las personas. |
| 1 | Documentado | Está definido por escrito y aprobado; no hay evidencia de que opere. |
| 2 | Implementado | Opera de forma regular y deja evidencia. |
| 3 | Probado | Su efectividad se verificó con pruebas, ejercicios o revisión independiente en los últimos 12 meses. |
| 4 | Adaptativo | Se mide, se mejora con los resultados y se ajusta ante cambios del contexto. |

El nivel objetivo propuesto es 3 para las funciones críticas y 2 para el resto. De las 59 funciones, 46 tienen criticidad alta en la propuesta del modelo; cada organización ajusta esa columna.

## 5. El año en cuatro ciclos trimestrales

El primer ciclo tiene dos tramos: el diagnóstico (días 1 a 60) y el compromiso (hasta el día 90). Por eso la tabla muestra el diagnóstico como parte del ciclo 1.

| Etapa | Días | Tema | Pregunta que responde | Resultado |
|---|:--:|---|---|---|
| Diagnóstico y entendimiento (primer tramo del ciclo 1) | 1 a 60 | Conocer | ¿Qué tenemos, quién lo opera, qué evidencia lo respalda y qué puede dañar al negocio? | Diagnóstico base, línea base de indicadores, metas del ciclo 1 confirmadas y propuesta de plan anual con presupuesto y decisiones requeridas. |
| Ciclo 1 · Conocer, estabilizar y ordenar | 1 a 90 | Adecuación | ¿Qué puede dañarnos hoy, quién responde por cada función y qué necesito que la dirección decida? | Diagnóstico cerrado en el día 60; mandato, plan y presupuesto aprobados; dueños designados; exposiciones críticas cerradas; informe de los 90 días a las tres audiencias. |
| Ciclo 2 · Adecuar | 91 a 180 | Adecuación | ¿Cada función opera al nivel requerido, en todos los entornos y con quien corresponde? | Sistema de gobierno operando; funciones críticas en nivel «Implementado»; contratos críticos con niveles de servicio y evidencia. |
| Ciclo 3 · Evolucionar y probar | 181 a 270 | Evolución | ¿Lo que decimos que tenemos funciona cuando se lo exige, también en lo que opera un tercero? | Capacidades críticas en nivel «Probado»; reversibilidad de los servicios críticos comprobada; agentes evaluados antes de ampliar su autonomía. |
| Ciclo 4 · Demostrar y sostener | 271 a 365 | Evolución | ¿Cuál es nuestro nivel real de riesgo, mejoramos, invertimos bien y estamos preparados? | Informe anual al directorio y a los síndicos; plan y presupuesto del año 2; mandato renovado. |

## 6. Dos sistemas de medición

El modelo separa lo que se quiere **cambiar** de lo que se quiere **sostener**.

|  | OKR | Indicadores |
|---|---|---|
| Para qué | Adecuar y evolucionar: cerrar brechas y construir capacidades | Operar con regularidad: saber si cada función cumple |
| Horizonte | Un ciclo | Permanente |
| Cantidad | 24 objetivos y 72 resultados clave en el año | 224 en el catálogo; cada organización elige |
| Cómo se lee | Avance entre la línea base y la meta | Estadio E1 a E5 según cuatro umbrales |
| Dónde | Frontier_CISO_Atlas_CISO365_Plan_Anual_y_OKR_v2.0.xlsx | Frontier_CISO_Atlas_CISO365_KPIs_y_Tablero_v2.0.xlsx |

Un resultado clave usa un indicador como medida, pero no al revés: cuando el resultado clave se cumple, el indicador sigue midiéndose.

## 7. Cómo se conectan las piezas

1. Cada **función** tiene un dueño y un modelo de provisión.
2. El **diagnóstico** califica cada función con evidencia y calcula la brecha, la prioridad y la etapa sugerida.
3. Las brechas prioritarias se convierten en **resultados clave** de un ciclo, en la versión que corresponde a quien opera la función.
4. Cada función se sostiene con **indicadores**, y cada indicador tiene fórmula, fuente, frecuencia y umbrales.
5. Las **cadencias** hacen que todo ocurra: revisión semanal, seguimiento quincenal, comité mensual y cierre trimestral de cada ciclo, con informe a las tres audiencias.
6. Al cierre de cada ciclo se **rinde cuentas** a tres audiencias con los mismos datos y distinto nivel de detalle.

## 8. Agentes: una tercera clase de trabajador

Un agente de IA que ejecuta tareas se trata como una identidad con dueño, límites, supervisión y retiro. El modelo usa una escala de autonomía tomada de GM-24:

| Nivel | Qué puede hacer | Condición para habilitarlo |
|:--:|---|---|
| L0 | Solo informa | Ficha del agente e identidad de lectura. |
| L1 | Propone; la persona ejecuta | Además, evaluación de calidad. |
| L2 | Propone y ejecuta tras aprobación humana registrada | Además, límites de lote, detención de emergencia probada y prueba adversarial. |
| L3 | Ejecuta acciones reversibles y de bajo impacto, con auditoría posterior por muestreo | Además, indicadores de riesgo con umbrales, revisión trimestral y autorización formal. |
| L4 | Autónomo con límites estrictos | No previsto en este plan. |

---

*Frontier CISO Atlas · Modelo Operativo CISO 365 · versión 2.0, revisión 2 · 15 de noviembre de 2026 · propuesta sujeta a validación · @SCavanna*

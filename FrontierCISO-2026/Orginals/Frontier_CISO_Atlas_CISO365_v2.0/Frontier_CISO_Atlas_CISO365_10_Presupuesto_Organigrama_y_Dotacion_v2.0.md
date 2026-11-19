# Presupuesto, organigrama y dotación

**Frontier CISO Atlas · Modelo Operativo CISO 365 · versión 2.0, revisión 2** · documento 10 de 16 · 15 de noviembre de 2026 · @SCavanna

> Propuesta de base, sujeta a validación y a calibración en cada organización. La ejecución se puede contratar; la rendición de cuentas, no.

## 1. Por qué este plan cambia el presupuesto y la estructura

El plan convierte un conjunto de proyectos y de contratos en un programa con funciones, dueños y medición. Eso tiene tres consecuencias: el gasto se ordena por categoría y se conoce su costo total; aparecen roles que antes no existían o que estaban repartidos; y cada función externalizada necesita un dueño interno. El modelo no fija montos ni cantidad de personas: da las categorías, los roles y el método para decidir.

## 2. Presupuesto

| ID | Categoría | Tipo | Provisión | Qué incluye |
|:--:|---|---|---|---|
| P01 | Personas: dotación propia | Operar | Propia | Sueldos y cargas del equipo de seguridad y de protección de datos. |
| P02 | Servicios externalizados de operación | Operar | Externa | Detección y respuesta gestionadas, gestión de vulnerabilidades, operación de identidades y otros servicios recurrentes. |
| P03 | Plataformas y licencias de seguridad | Operar | Externa | Suscripciones y licencias de las herramientas de seguridad. |
| P04 | Infraestructura y consumo | Operar | Externa | Telemetría, almacenamiento de registros, cómputo y capacidad consumidos por la seguridad. |
| P05 | Proyectos de adecuación y evolución | Cambiar | Mixta | Iniciativas de los cuatro ciclos: implementación, integración y migraciones. |
| P06 | Aseguramiento independiente | Operar | Externa | Auditorías, pruebas ofensivas, certificaciones y verificación de los servicios externalizados. |
| P07 | Formación, certificación y cultura | Operar | Mixta | Desarrollo del equipo, formación por función y programa de cultura. |
| P08 | Respuesta y resiliencia | Operar | Externa | Acuerdos de respuesta por adelantado, ejercicios, seguro y pruebas de recuperación. |
| P09 | Protección de datos y privacidad | Operar | Mixta | Delegado de protección de datos, evaluaciones de impacto y herramientas de privacidad. |
| P10 | IA y agentes | Cambiar | Mixta | Plataforma, evaluación y consumo de los agentes del área, y controles para la IA de la organización. |
| P11 | Consultoría y asesoría | Cambiar | Externa | Estrategia, arquitectura y asesoría legal y regulatoria. |
| P12 | Contingencia | Operar | Propia | Reserva para incidentes y cambios no previstos. |

- **Operar y cambiar.** «Operar» sostiene las funciones regulares; «Cambiar» paga la adecuación y la evolución. Separarlos evita que los proyectos se coman la operación.
- **Costo total.** El gasto de seguridad incluye lo que está en otros presupuestos: licencias en tecnología, servicios en compras, personas en otras áreas. El indicador K104 mide cuánto de ese gasto se conoce.
- **Por etapa.** La hoja Presupuesto del libro de plan anual distribuye cada categoría entre los dos tramos del ciclo 1 —el diagnóstico y el resto— y los ciclos 2, 3 y 4.
- **Cuándo se aprueba.** El presupuesto del año se presenta al cierre del diagnóstico y se aprueba en el ciclo 1, junto con el plan.

| ID | Indicador de presupuesto | Umbrales E2 · E3 · E4 · E5 |
|---|---|---|
| K17 | Inversión en seguridad trazada a riesgos y objetivos del negocio | 40 · 60 · 80 · 95 |
| K19 | Reducción de riesgo por unidad de inversión | 0,5 · 1 · 2 · 4 |
| K103 | Desvío de la ejecución presupuestaria | 25 · 15 · 10 · 5 |
| K104 | Gasto de seguridad con costo total conocido | 40 · 60 · 80 · 95 |
| KX16 | Desvío del costo por unidad de resultado | 40 · 25 · 15 · 5 |

## 3. Organigrama: 25 roles en 11 familias

| ID | Familia | Rol | Funciones que cubre | Provisión habitual | Nota |
|:--:|---|---|---|---|---|
| R01 | Dirección | CISO | GOB-G1.1 · GOB-G1.2 · GOB-G6.1 | Propio | Responde ante el directorio. La rendición de cuentas no se delega, aunque la dirección se apoye en un servicio. |
| R02 | Dirección | Oficina del CISO: planificación, OKR e indicadores | GES-M1.1 · GOB-G6.2 | Propio | Sostiene los ciclos, el tablero y la preparación de los informes. |
| R03 | Gobierno, riesgo y cumplimiento | Responsable de gobierno, riesgo y cumplimiento | GOB-G2.1 · GOB-G2.2 · GOB-G4.1 · GOB-G4.2 | Propio | Marcos, políticas, comité y apetito. |
| R04 | Gobierno, riesgo y cumplimiento | Analista de riesgo | GOB-G5.1 · GOB-G5.2 | Mixto | Escenarios, cuantificación y seguimiento de tratamientos. |
| R05 | Gobierno, riesgo y cumplimiento | Analista de cumplimiento y aseguramiento | GOB-G3.2 | Mixto | Evidencia, auditorías y hallazgos. |
| R06 | Gobierno, riesgo y cumplimiento | Gestor de riesgo de terceros | OPE-ID-04 · GES-M6.2 | Mixto | Evaluación de proveedores y socios. |
| R07 | Protección de datos | Delegado de protección de datos | GOB-G3.1 · GES-M2.1 | Propio o externo | Figura exigida por algunas normas; su independencia y su relación con seguridad se definen por escrito. |
| R08 | Protección de datos | Analista de privacidad | GES-M2.1 | Mixto | Registro de tratamientos y evaluaciones de impacto. |
| R09 | Protección de datos | Especialista en seguridad de datos | OPE-ID-06 · OPE-PR-06 | Propio | Descubrimiento, clasificación, control de salida y claves. |
| R10 | Arquitectura e ingeniería | Arquitecto de seguridad | GES-M3.1 | Propio | Arquitectura objetivo Zero Trust, patrones y revisión de diseños. |
| R11 | Arquitectura e ingeniería | Ingeniero de seguridad de nube | OPE-ID-03 · OPE-PR-09 | Mixto | Línea base y protección en todos los entornos. |
| R12 | Arquitectura e ingeniería | Ingeniero de seguridad de aplicaciones | OPE-PR-07 | Mixto | Controles en el ciclo de desarrollo. |
| R13 | Arquitectura e ingeniería | Ingeniero de identidad | GES-M2.2 · OPE-PR-01 · OPE-PR-02 · OPE-PR-03 | Propio | Plano de identidad para personas, cargas y agentes. |
| R14 | Operaciones de seguridad | Responsable de operaciones de seguridad | GES-M4.1 | Propio | Dirige la detección y la respuesta, propias o contratadas. |
| R15 | Operaciones de seguridad | Analista de detección y respuesta | OPE-DE-01 · OPE-RS-01 · OPE-RS-03 | Mixto o externo | Vigilancia, clasificación y contención. |
| R16 | Operaciones de seguridad | Ingeniero de detección | OPE-DE-02 · OPE-DE-05 | Propio o mixto | Detecciones, calidad y telemetría. |
| R17 | Operaciones de seguridad | Especialista en inteligencia y búsqueda de amenazas | OPE-DE-03 · OPE-DE-04 | Mixto | Hipótesis, campañas e inteligencia accionable. |
| R18 | Operaciones de seguridad | Responsable de respuesta a incidentes | GES-M5.1 · GES-M5.2 · OPE-RS-02 · OPE-RS-04 · OPE-RS-05 · OPE-RC-05 | Propio | Preparación, conducción, análisis, notificación y aprendizaje. |
| R19 | Operaciones de seguridad | Gestor de vulnerabilidades y exposición | OPE-ID-01 · OPE-ID-02 · OPE-ID-05 · GES-M4.2 | Mixto | Inventario, priorización, pruebas y seguimiento de la corrección. |
| R20 | Resiliencia | Responsable de continuidad y recuperación | GES-M6.1 · OPE-RC-01 · OPE-RC-02 · OPE-RC-03 · OPE-RC-04 | Propio | Objetivos de recuperación, pruebas y operación degradada. |
| R21 | Cultura | Responsable de concientización y cultura | OPE-PR-10 | Mixto | Comportamientos, formación por función y red de referentes. |
| R22 | Producto-control | Dueños de producto-control | GES-M1.1 · GES-M3.2 · OPE-PR-04 · OPE-PR-05 · OPE-PR-08 | Propio | Un dueño por dominio: identidades, dispositivos, datos, aplicaciones, red y nube, y detección y respuesta. Responde por el objetivo, la configuración y la evidencia. |
| R23 | IA y agentes | Responsable de seguridad de IA y gestor de agentes | OPE-ID-07 · OPE-PR-11 · OPE-DE-06 | Propio | Registro, identidad, límites, evaluación y retiro de los agentes. |
| R24 | Servicios externalizados | Gestor de servicios externalizados | GES-M1.2 · GES-M6.2 | Propio | Dueño interno de los contratos: niveles de servicio, evidencia, verificación y salida. |
| R25 | Tecnología operacional | Especialista en seguridad de tecnología operacional | OPE-PR-12 | Mixto | Solo si la organización opera procesos físicos. |

Un rol no es un puesto. En una organización chica una persona cubre varios roles; en una grande, un rol puede ser un equipo. Lo que no debe pasar es que una función quede sin rol que responda por ella.

Cuatro definiciones de estructura que el plan obliga a tomar:

1. **A quién reporta el CISO** y con qué acceso al directorio (GOB-G1.1).
2. **Dónde queda la protección de datos**: el delegado de protección de datos necesita independencia, y su relación con seguridad se define por escrito.
3. **Quién es dueño de cada producto-control**: identidades, dispositivos, datos, aplicaciones, red y nube.
4. **Quién gobierna cada servicio externalizado**: el gestor de servicios externalizados es un rol interno.

## 4. Dotación: el método

1. Partir de las funciones y de su modelo de provisión (hoja Provisión del libro de plan anual).
2. Asignar cada función a un rol y anotar la dotación actual, propia y externa (hoja Dotación).
3. Fijar la dotación objetivo según la brecha del diagnóstico y la etapa sugerida.
4. Decidir, por rol, si se cubre con personal propio, con un proveedor o con una combinación.
5. Considerar a los agentes como una tercera clase de trabajador: cada agente tiene un gestor humano y un nivel de autonomía.

| ID | Indicador de personas | Umbrales E2 · E3 · E4 · E5 |
|---|---|---|
| K12 | Cobertura de capacidades críticas del equipo de seguridad | 50 · 70 · 85 · 95 |
| K13 | Retención del talento crítico de seguridad | 75 · 85 · 90 · 95 |

## 5. Decisiones que el plan pide

| Dimensión | Impacto | Decisión requerida | Quién decide | Etapa |
|---|---|---|---|---|
| Presupuesto | El gasto pasa de proyectos aislados a un programa con costo total conocido. | Aprobar el presupuesto del año por categoría, separando operar de cambiar. | CEO, CFO y comité ejecutivo | Ciclo 1 |
| Presupuesto | Verificar de forma independiente los servicios externalizados tiene un costo propio. | Incluir el costo de la verificación en cada contrato o en el presupuesto. | CEO, CFO y comité ejecutivo | Ciclo 1 |
| Presupuesto | Una reserva de contingencia evita financiar los incidentes con el presupuesto del programa. | Constituir la reserva y definir quién la libera. | CEO, CFO y comité ejecutivo | Ciclo 1 |
| Presupuesto | Racionalizar las herramientas solapadas libera gasto, pero la migración cuesta. | Aprobar el plan de consolidación con su costo de transición. | CEO, CFO y comité ejecutivo · CIO y CTO | Ciclo 2 |
| Presupuesto | La IA y los agentes agregan costos de consumo variables. | Fijar el presupuesto de consumo y sus alertas. | CEO, CFO y comité ejecutivo | Ciclo 2 |
| Organigrama | La línea de reporte del CISO define su independencia. | Definir a quién reporta el CISO y su acceso al directorio. | Directorio y síndicos · CEO, CFO y comité ejecutivo | Diagnóstico |
| Organigrama | Los riesgos tienen dueño en el negocio, no en el área de seguridad. | Designar dueños de riesgo por proceso crítico. | CEO, CFO y comité ejecutivo | Ciclo 1 |
| Organigrama | Aparece un comité de seguridad y riesgo con poder de decisión. | Constituir el comité con sus derechos de decisión. | CEO, CFO y comité ejecutivo | Ciclo 1 |
| Organigrama | Cada control pasa a tener un dueño de producto. | Designar dueños de producto-control por dominio. | CIO y CTO | Ciclo 1 |
| Organigrama | Seguridad y tecnología comparten la operación: hace falta una frontera clara. | Aprobar la matriz de responsabilidades entre seguridad y tecnología. | CIO y CTO | Ciclo 1 |
| Organigrama | Protección de datos y seguridad necesitan una relación definida. | Definir la relación entre el delegado de protección de datos, legal y seguridad. | CEO, CFO y comité ejecutivo | Ciclo 2 |
| Dotación | Hay capacidades críticas sin cubrir. | Aprobar la dotación objetivo y el modelo de provisión por función. | CEO, CFO y comité ejecutivo | Ciclo 2 |
| Dotación | Externalizar no elimina la necesidad de saber: hay que conservar la capacidad de supervisar. | Definir qué capacidades se retienen aunque la función se contrate. | CEO, CFO y comité ejecutivo | Ciclo 2 |
| Dotación | Aparecen roles nuevos: dueño de producto-control, gestor de servicios externalizados y gestor de agentes. | Aprobar los perfiles y su plan de carrera. | CEO, CFO y comité ejecutivo | Ciclo 2 |
| Dotación | Los agentes ejecutan tareas: cambia el trabajo de los analistas. | Aprobar el itinerario de desarrollo del equipo y los niveles de autonomía de los agentes. | CEO, CFO y comité ejecutivo · CIO y CTO | Ciclo 3 |
| Dotación | El talento crítico es escaso. | Aprobar las medidas de retención y los suplentes de los roles críticos. | CEO, CFO y comité ejecutivo | Ciclo 3 |

El estado de cada decisión se sigue en la hoja «Impacto y decisiones» del libro de plan anual.

---

*Frontier CISO Atlas · Modelo Operativo CISO 365 · versión 2.0, revisión 2 · 15 de noviembre de 2026 · propuesta sujeta a validación · @SCavanna*

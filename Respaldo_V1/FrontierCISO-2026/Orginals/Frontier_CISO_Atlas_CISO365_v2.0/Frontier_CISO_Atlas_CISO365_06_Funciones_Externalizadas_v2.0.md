# Funciones externalizadas: cómo gobernarlas y medirlas

**Frontier CISO Atlas · Modelo Operativo CISO 365 · versión 2.0, revisión 2** · documento 06 de 16 · 15 de noviembre de 2026 · @SCavanna

> Propuesta de base, sujeta a validación y a calibración en cada organización. La ejecución se puede contratar; la rendición de cuentas, no.

## 1. El principio

La ejecución se puede contratar; la rendición de cuentas, no. Un proveedor puede operar una función de punta a punta. Lo que la organización no puede transferir es la decisión sobre el riesgo, la responsabilidad ante el regulador y ante el directorio, y la obligación de comprobar que el servicio cumple.

De ahí salen tres reglas:

1. Cada servicio externalizado tiene un **dueño interno** con autoridad sobre el contrato.
2. El proveedor se gobierna por **resultados medibles** y se **verifica**: nivel de servicio, evidencia periódica y una prueba independiente.
3. La **salida** se ensaya: los datos, los registros y la configuración pueden volver a la organización o pasar a otro proveedor.

## 2. Modelos de provisión

| Modelo | Qué significa |
|---|---|
| Propio | La organización opera la función con personal y herramientas bajo su gestión. |
| Co-gestionado | Un proveedor ejecuta una parte definida; la organización conserva la decisión y opera el resto. |
| Externalizado | Un proveedor opera la función de punta a punta bajo contrato; la organización conserva la rendición de cuentas, las decisiones reservadas y la verificación. |
| No existe | Nadie cumple la función. |

## 3. Qué cambia cuando un tercero opera la función

| Elemento | Operación propia | Función externalizada |
|---|---|---|
| Objetivo | Resultado que logra el equipo | Resultado contratado, con nivel de servicio |
| Resultado clave | Versión propia | Versión externalizada; en 39 de 72 cambia el indicador |
| Indicador | Lo mide la organización | Según el código: nivel de servicio, compartido, insumo o interno |
| Evidencia | La produce el equipo | La aporta el proveedor y la organización la verifica |
| Quién responde | La organización | La organización |

| Código | Cómo se mide | Qué significa | Indicadores |
|:--:|---|---|---|
| SLO | Nivel de servicio | Se pacta como nivel de servicio por resultado. Lo mide el proveedor y la organización lo verifica por muestreo o con una prueba independiente (KX05, KX06). | 80 |
| COM | Compartido | El proveedor ejecuta una parte o aporta el dato; la organización conserva la meta, decide y verifica. | 30 |
| INS | Insumo | El proveedor aporta insumos o evidencia; la medición y la decisión son internas. | 31 |
| INT | Interno | No se externaliza: mide una decisión o una responsabilidad que la organización no puede delegar. | 61 |
| EXT | Gobierno de la externalización | Indicador propio del gobierno de los servicios externalizados (KX): mide a la organización como contratante, no al proveedor. | 22 |

## 4. Qué exigir en cada función

| ID | Función | Modalidad habitual de externalización | Lo que no se delega | Objetivo si está externalizada | Evidencia a exigir | Indicadores KX |
|---|---|---|---|---|---|---|
| GOB-G1.1 | Contexto, mandato y autoridad del CISO | Dirección de seguridad como servicio (CISO externo o interino); asesoría de gobierno. | Designar un responsable interno ante el directorio, aprobar el mandato y decidir el apetito de riesgo. | La organización conserva un responsable interno con acceso al directorio y un mandato aprobado, aunque la dirección de seguridad se preste como servicio. | Acta de designación del responsable interno; plan de trabajo del servicio; registro mensual de decisiones. | KX01 · KX04 · KX15 · KX20 |
| GOB-G1.2 | Estrategia de seguridad y alineación con el negocio | Consultoría para formular o revisar la estrategia y el caso de inversión. | Aprobar las prioridades, la inversión y las renuncias. | La estrategia formulada con apoyo externo queda aprobada por la dirección, con sus supuestos, las opciones descartadas y la transferencia de conocimiento al equipo. | Supuestos y alternativas documentados; sesiones de transferencia; acta de aprobación. | KX01 · KX04 · KX15 |
| GOB-G2.1 | Marcos, estándares y grilla de propiedad | Evaluación de madurez y armado del marco de control por un tercero. | Decidir qué marcos obligan, cuál es el perfil objetivo y quién es dueño de cada cruce. | La evaluación externa deja un perfil y una grilla que la organización mantiene sin depender del evaluador. | Método, evidencias y papeles de trabajo entregados; perfil en formato editable. | KX01 · KX04 · KX09 · KX15 |
| GOB-G2.2 | Políticas, estándares y procedimientos | Redacción y mantenimiento de normativa por un tercero. | Aprobar las políticas y las excepciones. | Las políticas aplicables están incorporadas a los contratos de servicio y cada proveedor demuestra su cumplimiento. | Anexo de políticas aplicables por contrato; declaración de cumplimiento con evidencia; excepciones solicitadas por el proveedor. | KX01 · KX04 · KX21 |
| GOB-G3.1 | Requisitos legales, regulatorios y contractuales | Seguimiento regulatorio y asesoría legal especializada; delegado de protección de datos externo. | Responder ante el regulador y decidir cómo cumplir. | El asesor externo mantiene al día el inventario de obligaciones y la organización decide y responde ante cada regulador. | Informes periódicos de cambios; opinión escrita sobre obligaciones nuevas; registro de consultas. | KX01 · KX04 · KX15 · KX22 |
| GOB-G3.2 | Cumplimiento y aseguramiento continuo | Auditoría externa, certificación y pruebas de control por terceros. | Definir el alcance del aseguramiento y responder por los hallazgos. | El aseguramiento contratado cubre los riesgos altos, es independiente de quien opera y sus hallazgos se cierran en plazo. | Plan y alcance; informes con evidencia; declaración de independencia. | KX01 · KX04 · KX05 · KX18 |
| GOB-G4.1 | Gobernanza del riesgo: estructuras y dueños | Secretaría técnica o facilitación del comité por un tercero. | Ser dueño del riesgo y decidir su tratamiento. | Todo riesgo originado en un proveedor tiene dueño interno y llega al comité con la misma regla que los riesgos propios. | Registro de riesgos por servicio; actas con decisiones; riesgos escalados por el proveedor. | KX01 · KX13 · KX14 · KX20 |
| GOB-G4.2 | Apetito de riesgo: definición y comunicación | Apoyo metodológico para formular el apetito y cuantificar escenarios. | Aprobar el apetito: es una decisión del directorio. | El apetito incluye límites para la dependencia de proveedores y las decisiones que ningún tercero —persona, proveedor o agente— puede tomar. | Límites de concentración; lista de decisiones reservadas incorporada a los contratos. | KX13 · KX14 |
| GOB-G5.1 | Supervisión de la evaluación y el análisis de riesgos | Evaluación de riesgos y cuantificación por un tercero. | Validar los escenarios y sus supuestos con los dueños del negocio. | Las evaluaciones externas usan un método explícito, supuestos validados por los dueños del negocio y datos que quedan en la organización. | Modelo y datos entregados; supuestos firmados por los dueños; sensibilidad de los resultados. | KX01 · KX04 · KX09 · KX15 |
| GOB-G5.2 | Supervisión del tratamiento y la aceptación de riesgos | Seguimiento de planes por una oficina de proyectos externa. | Aceptar el riesgo: solo puede hacerlo su dueño. | Los riesgos que un proveedor no puede mitigar se aceptan de forma explícita por el dueño interno, con vencimiento. | Solicitudes de aceptación originadas en el servicio; estado de los planes a cargo del proveedor. | KX01 · KX13 · KX18 |
| GOB-G6.1 | Comunicación estratégica y reporte a la dirección | Preparación de informes y tableros por un tercero. | Presentar ante el directorio y responder sus preguntas. | El reporte integra, con la misma vara, el desempeño de lo que opera la organización y de lo que operan los proveedores. | Datos del proveedor en el formato del tablero; notas sobre la calidad del dato. | KX03 · KX04 · KX06 |
| GOB-G6.2 | Liderazgo ético y medición de la efectividad | Evaluación independiente de la gestión del CISO. | La conducta y la rendición de cuentas. | Los proveedores críticos declaran sus conflictos de interés y sus indicadores se verifican antes de llegar al tablero. | Declaraciones de conflicto de interés; resultado de la verificación de indicadores. | KX05 · KX06 · KX17 |
| GES-M1.1 | Programa de seguridad y portafolio de productos-control | Oficina de gestión del programa operada por un tercero. | Priorizar el portafolio y ser dueño de cada producto-control. | Cada control operado por un proveedor tiene dueño interno, objetivo y evidencia definidos en un anexo operativo. | Anexo operativo por control: objetivo, configuración de referencia, evidencia y cadencias. | KX01 · KX02 · KX04 · KX20 |
| GES-M1.2 | Finanzas, equipo, proveedores y capacitación | Dotación complementaria, servicios gestionados y formación por terceros. | Decidir el modelo de provisión de cada función y conservar la capacidad de supervisarla. | Para cada función externalizada la organización conserva capacidad interna acreditada para supervisarla y conoce su costo por unidad de resultado. | Matriz de capacidades de supervisión; costo del servicio por unidad de resultado. | KX14 · KX15 · KX16 |
| GES-M2.1 | Activos, datos y protección de datos personales | Descubrimiento y clasificación como servicio; delegado de protección de datos externo. | Ser dueño del dato y decidir su clasificación y su uso. | Los datos que trata o custodia un proveedor están inventariados y clasificados, con su localización y su devolución acordadas. | Inventario de datos en poder del proveedor; localización; registro de accesos; certificado de devolución o destrucción. | KX01 · KX04 · KX09 · KX22 |
| GES-M2.2 | Gestión de identidades y accesos | Administración de identidades y accesos gestionada. | Aprobar los accesos y los privilegios, y ser dueño de la política. | Los accesos del proveedor, y los que el proveedor administra, cumplen la misma política, con privilegio mínimo y registro. | Listado de cuentas del proveedor; registro de sesiones privilegiadas; resultado de las recertificaciones. | KX01 · KX03 · KX10 · KX13 |
| GES-M3.1 | Arquitectura de seguridad e ingeniería (Zero Trust) | Arquitectura e ingeniería por una consultora o un integrador. | Aprobar la arquitectura objetivo y las excepciones. | Los diseños de terceros siguen los patrones aprobados, son portables entre entornos y dejan la documentación en la organización. | Diseños y decisiones documentados; uso de patrones aprobados; plan de portabilidad. | KX01 · KX04 · KX09 · KX15 |
| GES-M3.2 | Selección, implementación y evaluación de controles | Implementación por integradores; evaluación de controles por terceros. | Decidir qué control se adopta y aceptar el riesgo residual. | El proveedor mantiene la configuración de referencia, informa la deriva y la corrige en el plazo pactado. | Informe de deriva; cambios aprobados; evidencia de corrección. | KX01 · KX03 · KX04 · KX05 · KX19 |
| GES-M4.1 | Gestión de las operaciones de seguridad | Centro de operaciones de seguridad como servicio; detección y respuesta gestionadas. | Decidir qué se vigila, qué se considera incidente y qué acciones requieren aprobación. | La operación contratada cubre todos los entornos críticos y se gobierna por tiempos y calidad verificados, no por volumen de alertas. | Cobertura por entorno; tiempos por severidad; casos de uso activos; resultado de las simulaciones. | KX01 · KX02 · KX03 · KX05 · KX06 · KX12 · KX19 |
| GES-M4.2 | Gestión de amenazas, vulnerabilidades y riesgos emergentes | Inteligencia de amenazas y gestión de exposición como servicio. | Priorizar según el negocio y aceptar lo que no se corrige. | La inteligencia y la priorización contratadas producen acciones concretas en los entornos de la organización. | Acciones recomendadas y aplicadas; relevancia de la inteligencia para el sector. | KX01 · KX03 · KX04 |
| GES-M5.1 | Preparación de la respuesta a incidentes | Acuerdo de respuesta a incidentes por adelantado; ejercicios facilitados por terceros. | Declarar la crisis y decidir sobre el negocio. | Los acuerdos de apoyo externo están vigentes, probados en un ejercicio y con tiempos de activación conocidos. | Contrato vigente; tiempo de activación medido; informe del ejercicio. | KX01 · KX02 · KX12 · KX20 |
| GES-M5.2 | Conducción de la respuesta y aprendizaje | Conducción técnica por el proveedor de respuesta; comunicación de crisis por una agencia. | Las decisiones de negocio, la notificación al regulador y la comunicación pública. | El proveedor conduce la respuesta técnica y la organización decide, notifica y aprende, con un traspaso medido. | Cronología del incidente; tiempos de traspaso; informe posterior con causa raíz. | KX07 · KX12 · KX13 · KX18 |
| GES-M6.1 | Continuidad, recuperación y resiliencia | Recuperación ante desastres como servicio; sitio alterno contratado. | Fijar los objetivos de recuperación y decidir la activación. | La recuperación contratada se prueba con la organización presente y cumple los objetivos fijados por el negocio. | Informe de prueba con tiempos; alcance cubierto; dependencias del proveedor. | KX01 · KX02 · KX03 · KX05 · KX08 · KX19 |
| GES-M6.2 | Nube, tecnologías emergentes y cadena de suministro | Gestión de riesgo de terceros como servicio; operación de nube gestionada. | Decidir con quién se contrata, cuánta dependencia se tolera y cuándo salir. | Los proveedores críticos entregan evidencia vigente, notifican en plazo y cada servicio crítico tiene una salida probada. | Evidencia de control del proveedor; notificaciones; resultado del ensayo de salida. | KX07 · KX08 · KX09 · KX11 · KX14 · KX21 |
| OPE-ID-01 | Inventario y descubrimiento de activos | Descubrimiento de activos y de superficie de ataque externa como servicio. | Decidir qué entra en el alcance y quién es dueño de cada activo. | El inventario del proveedor se reconcilia con el propio y no deja activos del alcance sin dueño. | Inventario exportable; diferencias de la reconciliación; activos nuevos detectados. | KX01 · KX03 · KX04 · KX09 · KX19 |
| OPE-ID-02 | Gestión de vulnerabilidades y de la exposición | Gestión de vulnerabilidades como servicio. | Aceptar el riesgo de lo que no se corrige. | Los plazos de corrección están pactados como nivel de servicio y se verifican por muestreo. | Cobertura de la evaluación; plazos por criticidad; excepciones solicitadas. | KX01 · KX02 · KX03 · KX05 · KX06 · KX19 |
| OPE-ID-03 | Postura de nube y de configuración | Gestión de la postura de nube como servicio. | Definir la línea base y aprobar las excepciones. | El proveedor mide la postura con la línea base de la organización en todos los entornos y corrige en plazo. | Cumplimiento por entorno; hallazgos abiertos y su antigüedad. | KX01 · KX03 · KX04 · KX05 · KX19 |
| OPE-ID-04 | Evaluación de riesgo de terceros | Evaluación de terceros como servicio; calificaciones externas. | Decidir si se contrata y con qué condiciones. | Las evaluaciones contratadas usan los criterios de la organización y alcanzan a los subcontratistas de los proveedores críticos. | Informes por proveedor; hallazgos y seguimiento; cobertura de subcontratistas. | KX01 · KX04 · KX11 · KX18 |
| OPE-ID-05 | Pruebas ofensivas y validación de controles | Pruebas de penetración y ejercicios de equipo rojo por terceros. | Definir el alcance y las reglas, y aceptar lo que no se corrige. | Las pruebas las realiza un tercero independiente de quien opera el control, y sus hallazgos se revalidan. | Informe con evidencia reproducible; revalidación; independencia declarada. | KX01 · KX04 · KX05 · KX18 |
| OPE-ID-06 | Descubrimiento y clasificación de datos | Descubrimiento y clasificación como servicio. | Decidir la clasificación: corresponde al dueño del dato. | El servicio cubre todos los entornos y deja el mapa de datos en poder de la organización. | Mapa de datos exportable; cobertura por entorno. | KX01 · KX04 · KX09 · KX19 · KX22 |
| OPE-ID-07 | Inventario y evaluación de sistemas de IA y agentes | Descubrimiento de IA no autorizada como servicio. | Aprobar cada caso de uso y su nivel de autonomía. | La IA y los agentes que los proveedores usan para prestar sus servicios están declarados y registrados. | Declaración de uso de IA por servicio; datos empleados; supervisión humana prevista. | KX01 · KX04 · KX17 |
| OPE-PR-01 | Identidades y accesos de las personas | Operación gestionada de identidades. | Aprobar los accesos. | La operación contratada cumple los tiempos de alta, cambio y baja, y no concede accesos sin aprobación. | Tiempos de alta y de baja; accesos concedidos con aprobación registrada. | KX01 · KX02 · KX03 · KX10 · KX13 |
| OPE-PR-02 | Acceso privilegiado | Gestión del acceso privilegiado como servicio. | Aprobar la elevación sobre los sistemas críticos. | El personal del proveedor opera sin privilegios permanentes y cada sesión queda registrada a nombre de una persona. | Registro de sesiones; lista nominal de los administradores del proveedor. | KX01 · KX03 · KX10 · KX13 |
| OPE-PR-03 | Identidades no humanas, de cargas y de agentes | Gestión de secretos y de identidades de carga como servicio. | Aprobar la autoridad delegada a cada agente. | Las integraciones y los agentes del proveedor usan identidades propias, sin credenciales compartidas ni permanentes. | Inventario de identidades del servicio; fecha de rotación; permisos efectivos. | KX01 · KX03 · KX10 · KX17 |
| OPE-PR-04 | Protección y gestión de dispositivos | Gestión de dispositivos y protección de puestos como servicio. | Definir la línea base del dispositivo. | El servicio mantiene los dispositivos conformes y con los parches críticos dentro del plazo pactado. | Cumplimiento por tipo de dispositivo; antigüedad de los parches. | KX01 · KX02 · KX03 · KX05 |
| OPE-PR-05 | Protección del correo y la colaboración | Protección del correo gestionada. | Definir qué se bloquea y aprobar las excepciones. | El servicio retira los mensajes maliciosos entregados dentro del tiempo pactado y justifica cada excepción. | Tiempos de retiro; excepciones con vencimiento; falsos positivos. | KX01 · KX02 · KX03 · KX05 |
| OPE-PR-06 | Protección de datos | Operación de prevención de fuga de datos como servicio; custodia de claves. | Decidir qué datos pueden salir y conservar el control de las claves. | Las claves quedan bajo el control de la organización y el proveedor gestiona los eventos de salida con un criterio aprobado. | Eventos gestionados; custodia de las claves; accesos del proveedor a los datos. | KX01 · KX03 · KX04 · KX10 · KX22 |
| OPE-PR-07 | Seguridad de aplicaciones y del desarrollo | Desarrollo por terceros; pruebas de seguridad de aplicaciones como servicio. | Aceptar el riesgo de liberar con vulnerabilidades. | El software desarrollado por terceros pasa los mismos controles y se entrega con su inventario de componentes. | Resultados de los controles; inventario de componentes por entrega. | KX01 · KX03 · KX04 · KX11 |
| OPE-PR-08 | Seguridad de red y segmentación | Operación gestionada de la seguridad de red. | Aprobar la política de segmentación. | El proveedor aplica la política de segmentación de la organización y cada cambio de regla queda aprobado y registrado. | Cambios de reglas con aprobación; resultado de las pruebas de segmentación. | KX01 · KX03 · KX05 · KX13 |
| OPE-PR-09 | Protección de cargas e infraestructura de nube | Protección de cargas gestionada; operación de la plataforma por terceros. | Definir qué puede desplegarse. | La protección contratada cubre todos los entornos del alcance con el mismo nivel de servicio. | Cobertura por entorno; despliegues bloqueados; incidentes por carga. | KX01 · KX03 · KX05 · KX19 |
| OPE-PR-10 | Concientización y cultura de seguridad | Concientización como servicio. | El ejemplo de la dirección y las consecuencias. | El programa contratado se mide por el cambio de comportamiento, no por la cantidad de cursos completados. | Tasa de reporte y de falla por área; contenidos adaptados al sector. | KX01 · KX02 · KX03 |
| OPE-PR-11 | Protección de sistemas de IA y agentes | Plataformas de IA de terceros; agentes operados por proveedores. | Aprobar el nivel de autonomía y las acciones de alto impacto. | Los agentes de terceros que actúan sobre los entornos de la organización cumplen los mismos límites y pueden detenerse. | Ficha del agente; permisos efectivos; resultado de la evaluación; prueba de detención. | KX01 · KX04 · KX10 · KX13 · KX17 |
| OPE-PR-12 | Seguridad de tecnología operacional y dispositivos conectados | Mantenimiento remoto por fabricantes e integradores. | La seguridad de las personas y del proceso. | Todo acceso remoto de fabricantes e integradores es temporal, aprobado, registrado y supervisado. | Registro de sesiones remotas; aprobaciones; inventario de conexiones de terceros. | KX01 · KX10 · KX13 |
| OPE-DE-01 | Monitoreo continuo y gestión de alertas | Centro de operaciones de seguridad como servicio; detección y respuesta gestionadas. | Declarar el incidente y autorizar las acciones de alto impacto. | El proveedor cumple los tiempos de detección y de clasificación en todos los entornos, verificados con simulaciones independientes. | Tiempos por severidad; simulaciones detectadas; alertas escaladas. | KX01 · KX02 · KX03 · KX05 · KX06 · KX12 · KX19 |
| OPE-DE-02 | Ingeniería y calidad de la detección | Contenido de detección provisto por el proveedor. | Priorizar las técnicas según los escenarios del negocio. | Las detecciones del proveedor se validan contra las técnicas priorizadas por la organización, y las reglas son recuperables. | Cobertura de técnicas; reglas exportables; tasa de falsos positivos. | KX01 · KX03 · KX05 · KX06 · KX09 |
| OPE-DE-03 | Búsqueda proactiva de amenazas | Búsqueda de amenazas como servicio. | Priorizar las hipótesis según los escenarios. | Cada campaña contratada entrega hallazgos, hipótesis y detecciones nuevas que quedan en la organización. | Informe por campaña; detecciones derivadas. | KX01 · KX04 · KX09 |
| OPE-DE-04 | Inteligencia de amenazas | Suscripciones e informes de inteligencia; centros sectoriales de intercambio. | Definir qué se necesita saber. | La inteligencia contratada responde a requerimientos definidos por la organización y se mide por las acciones que produce. | Informes vinculados con los requerimientos; acciones derivadas. | KX01 · KX04 |
| OPE-DE-05 | Gestión de registros y telemetría | Plataforma de registros operada por terceros. | Conservar la propiedad de los registros y el acceso a ellos. | Los registros que custodia el proveedor son propiedad de la organización, accesibles en todo momento y exportables. | Fuentes integradas; retención; prueba de exportación. | KX01 · KX03 · KX09 · KX19 · KX22 |
| OPE-DE-06 | Observabilidad de IA y agentes | Plataformas de IA de terceros con registro propio. | Decidir qué anomalía detiene a un agente. | Los agentes operados por proveedores entregan sus trazas a la vigilancia de la organización. | Trazas por agente; anomalías informadas. | KX01 · KX04 · KX09 · KX17 |
| OPE-RS-01 | Gestión y coordinación de incidentes | Respuesta gestionada; acuerdo de respuesta por adelantado. | Declarar la severidad y decidir sobre el negocio. | El traspaso entre el proveedor y el equipo interno ocurre dentro del tiempo pactado y sin pérdida de información. | Tiempo de traspaso; registro completo por incidente. | KX01 · KX02 · KX03 · KX12 · KX13 |
| OPE-RS-02 | Análisis e investigación forense | Investigación forense digital por terceros. | Decidir el uso legal de la evidencia. | El análisis contratado determina la causa raíz y entrega la evidencia con su cadena de custodia. | Informe forense; cadena de custodia; evidencia entregada. | KX01 · KX04 · KX22 |
| OPE-RS-03 | Contención, erradicación y respuesta automatizada | Contención ejecutada por el proveedor. | Autorizar las acciones que interrumpen el negocio. | El proveedor contiene dentro del tiempo pactado y no ejecuta acciones reservadas sin una aprobación registrada. | Tiempos de contención; acciones con aprobación; acciones revertidas. | KX01 · KX02 · KX03 · KX12 · KX13 |
| OPE-RS-04 | Comunicación y notificación de incidentes | Asesoría legal y de comunicación de crisis. | Notificar: corresponde a la organización. | El proveedor notifica sus incidentes dentro del plazo contractual, con el contenido que la organización necesita para cumplir los suyos. | Notificaciones del proveedor con hora y contenido. | KX01 · KX07 |
| OPE-RS-05 | Gestión de crisis y ejercicios | Ejercicios facilitados por terceros. | Decidir en la crisis. | Los ejercicios incluyen a los proveedores críticos y miden su tiempo de activación y de traspaso. | Informe del ejercicio; tiempos medidos; hallazgos. | KX01 · KX12 · KX18 |
| OPE-RC-01 | Respaldo y restauración | Respaldo como servicio. | Fijar qué se respalda y por cuánto tiempo. | El proveedor restaura en presencia de la organización, dentro del tiempo objetivo, y los respaldos son recuperables sin él. | Informe de restauración; prueba de acceso independiente a los respaldos. | KX01 · KX02 · KX03 · KX05 · KX09 · KX22 |
| OPE-RC-02 | Recuperación de servicios críticos | Recuperación ante desastres como servicio. | Fijar los objetivos y decidir la activación. | Las pruebas de recuperación del servicio contratado cumplen los objetivos y cubren todos los entornos. | Informe de prueba; tiempos; brechas. | KX01 · KX02 · KX03 · KX05 · KX08 · KX19 |
| OPE-RC-03 | Recuperación de la identidad y de la plataforma de control | Recuperación asistida por especialistas. | Custodiar las credenciales de emergencia. | La recuperación de la plataforma de control no depende de un proveedor que use esa misma plataforma para acceder. | Informe de prueba; custodia de las credenciales de emergencia. | KX01 · KX05 · KX10 |
| OPE-RC-04 | Continuidad y operación degradada | Sitios y servicios alternos contratados. | Decidir qué proceso se sostiene y cuál se suspende. | La continuidad de cada proveedor crítico está probada y su caída tiene un procedimiento alterno ensayado. | Plan de continuidad del proveedor; resultado del ensayo conjunto. | KX01 · KX05 · KX08 · KX14 |
| OPE-RC-05 | Comunicación de la recuperación y lecciones aprendidas | Informe posterior elaborado por el proveedor de respuesta. | Aprobar y difundir las lecciones. | Cada incidente con participación de un proveedor termina con una revisión conjunta y acciones a cargo de cada parte. | Informe conjunto; acciones del proveedor con fecha. | KX01 · KX18 |

## 5. Indicadores de gobierno de los servicios externalizados
Los 22 indicadores KX miden a la organización como contratante, no al proveedor.

| ID | Indicador | Fórmula | Unidad | Frecuencia | Umbrales E2 · E3 · E4 · E5 |
|---|---|---|---|---|---|
| KX01 | Servicios externalizados con dueño interno designado | Servicios externalizados con un dueño interno nominado y con autoridad sobre el contrato ÷ servicios externalizados × 100. | % | Trimestral | 60 · 80 · 95 · 100 |
| KX02 | Servicios críticos con niveles de servicio medibles por resultado | Servicios críticos con niveles de servicio definidos como resultados medibles ÷ servicios críticos externalizados × 100. | % | Semestral | 40 · 65 · 85 · 100 |
| KX03 | Cumplimiento de los niveles de servicio | Mediciones de nivel de servicio dentro del objetivo ÷ mediciones del período × 100. | % | Mensual | 70 · 85 · 95 · 99 |
| KX04 | Evidencia del proveedor entregada en plazo y verificable | Entregas de evidencia en plazo y que permiten verificar ÷ entregas comprometidas × 100. | % | Mensual | 60 · 80 · 95 · 100 |
| KX05 | Verificación independiente realizada según el plan | Verificaciones (muestreo, prueba o auditoría) realizadas ÷ verificaciones planificadas × 100. | % | Trimestral | 40 · 65 · 85 · 100 |
| KX06 | Discrepancia entre lo informado y lo verificado | Mediciones verificadas que difieren de lo informado por el proveedor más allá de la tolerancia ÷ mediciones verificadas × 100. | % | Trimestral | 30 · 20 · 10 · 5 |
| KX07 | Incidentes del proveedor notificados en el plazo contractual | Incidentes notificados en plazo ÷ incidentes del proveedor conocidos × 100. Equivale a K62 aplicado a cada servicio. | % | Trimestral | 60 · 80 · 95 · 100 |
| KX08 | Servicios críticos con plan de salida probado | Servicios críticos con plan de salida ensayado en los últimos 24 meses ÷ servicios críticos externalizados × 100. | % | Anual | 15 · 40 · 70 · 90 |
| KX09 | Portabilidad comprobada de datos, configuraciones y reglas | Servicios críticos cuya exportación de datos, configuraciones y reglas se comprobó en un formato utilizable ÷ servicios críticos externalizados × 100. | % | Anual | 25 · 50 · 75 · 95 |
| KX10 | Accesos del proveedor con privilegio mínimo, autenticación fuerte y registro | Cuentas del proveedor que cumplen las tres condiciones ÷ cuentas del proveedor × 100. | % | Trimestral | 60 · 80 · 95 · 100 |
| KX11 | Subcontratistas identificados y aprobados | Servicios críticos cuyos subcontratistas están identificados y aprobados ÷ servicios críticos externalizados × 100. | % | Semestral | 40 · 65 · 85 · 100 |
| KX12 | Tiempo de traspaso entre el proveedor y el equipo interno | Mediana de minutos entre el escalamiento del proveedor y la toma de control por el responsable interno. | minutos | Trimestral | 120 · 60 · 30 · 15 |
| KX13 | Decisiones reservadas ejecutadas sin aprobación | Cantidad de acciones reservadas a la organización que el proveedor ejecutó sin una aprobación registrada. | n.º | Trimestral | 5 · 2 · 1 · 0 |
| KX14 | Funciones críticas concentradas en un mismo proveedor | Mayor cantidad de funciones críticas que dependen de un solo proveedor ÷ funciones críticas × 100. | % | Semestral | 60 · 45 · 30 · 20 |
| KX15 | Funciones externalizadas con capacidad interna de supervisión | Funciones externalizadas para las que hay al menos una persona interna capacitada para supervisarlas ÷ funciones externalizadas × 100. | % | Semestral | 50 · 75 · 90 · 100 |
| KX16 | Desvío del costo por unidad de resultado | Valor absoluto de (costo real por unidad de resultado − costo de referencia) ÷ costo de referencia × 100. | % | Semestral | 40 · 25 · 15 · 5 |
| KX17 | Servicios con uso de IA y agentes declarado y gobernado | Servicios cuyo proveedor declaró el uso de IA, los datos empleados y la supervisión humana ÷ servicios externalizados × 100. | % | Semestral | 30 · 60 · 85 · 100 |
| KX18 | Hallazgos de la revisión del servicio corregidos en plazo | Hallazgos corregidos en fecha ÷ hallazgos con fecha vencida × 100. | % | Trimestral | 50 · 70 · 85 · 95 |
| KX19 | Cobertura de entornos del servicio | Entornos del alcance cubiertos por el contrato ÷ entornos del alcance × 100, en el servicio crítico menos cubierto. | % | Semestral | 60 · 80 · 95 · 100 |
| KX20 | Revisiones periódicas del servicio con decisiones registradas | Revisiones realizadas con acta y decisiones ÷ revisiones programadas × 100. | % | Trimestral | 50 · 75 · 90 · 100 |
| KX21 | Cláusulas mínimas presentes en los contratos críticos | Cláusulas mínimas presentes ÷ (cláusulas mínimas × contratos críticos) × 100. | % | Semestral | 50 · 70 · 90 · 100 |
| KX22 | Datos y registros en poder del proveedor con localización y devolución acordadas | Servicios con la localización, la retención y la devolución de datos y registros acordadas ÷ servicios que tratan datos o registros × 100. | % | Semestral | 50 · 70 · 90 · 100 |

## 6. Las 14 comprobaciones de cada contrato

| ID | Tema | Qué se comprueba | Indicador |
|---|---|---|:--:|
| CX01 | Dueño interno | El servicio tiene un dueño interno designado, con autoridad sobre el contrato. | KX01 |
| CX02 | Alcance | El alcance está documentado: funciones, entornos y activos cubiertos, y lo que queda fuera. | KX19 |
| CX03 | Niveles de servicio | Los niveles de servicio se miden por resultado, no solo por actividad. | KX02 |
| CX04 | Decisiones reservadas | Están definidas las decisiones que el proveedor no puede tomar sin aprobación. | KX13 |
| CX05 | Evidencia | El proveedor entrega evidencia periódica que permite verificar, no solo informes de estado. | KX04 |
| CX06 | Auditoría y prueba | El contrato reconoce el derecho de auditoría y de prueba independiente, y se ejerce. | KX05 |
| CX07 | Notificación | La notificación de incidentes tiene plazo y contenido definidos. | KX07 |
| CX08 | Accesos | Los accesos del proveedor usan privilegio mínimo, autenticación fuerte y registro. | KX10 |
| CX09 | Datos | Están acordados la localización, el tratamiento, la retención y la devolución de los datos y los registros. | KX22 |
| CX10 | Subcontratistas | Los subcontratistas están identificados y sujetos a las mismas obligaciones. | KX11 |
| CX11 | IA y agentes | El proveedor declaró el uso de IA y de agentes, los datos que emplean y la supervisión humana. | KX17 |
| CX12 | Salida | Existe un plan de salida, con devolución de datos, configuraciones y reglas en un formato utilizable. | KX08 |
| CX13 | Continuidad | El proveedor tiene un plan de continuidad probado y se conoce su dependencia de terceros. | KX14 |
| CX14 | Revisión | Hay una revisión periódica del servicio, con acta y decisiones. | KX20 |

Se responden con Sí, Parcial o No en el libro de diagnóstico. Con menos de 70% el contrato requiere acción: mantener, renegociar o reemplazar es una decisión que se registra.

## 7. Cláusulas mínimas

1. Derecho de auditoría y de prueba independiente
2. Notificación de incidentes con plazo y contenido
3. Localización, tratamiento y devolución de los datos
4. Subcontratación sujeta a aprobación
5. Plan de salida y transición
6. Continuidad del servicio
7. Decisiones reservadas a la organización
8. Uso de IA y agentes declarado

## 8. Resultados clave que cambian de indicador

| ID | Función | Indicador propio | Indicador si está externalizada | Meta si está externalizada |
|---|---|:--:|:--:|---|
| C1-F1-KR2 | GOB-G4.1 | K09 | KX01 | KX01 ≥ 100% |
| C1-F1-KR3 | GOB-G4.1 | KSG03 | KX20 | KX20 ≥ 75% |
| C1-F3-KR1 | OPE-PR-01 | K33 | KX10 | KX10 ≥ 80% |
| C1-F3-KR3 | OPE-ID-02 | K46 | KX03 | KX03 ≥ 85% |
| C1-F4-KR1 | OPE-DE-05 | K41 | KX19 | KX19 ≥ 80% |
| C1-F4-KR2 | GES-M5.1 | K130 | KX12 | KX12 ≤ 60 minutos |
| C1-F5-KR1 | OPE-ID-04 | K31 | KX02 | KX02 ≥ 65% |
| C1-F5-KR2 | GES-M3.2 | K123 | KX22 | KX22 ≥ 70% |
| C1-F5-KR3 | GES-M3.2 | K122 | KX21 | KX21 ≥ 70% |
| C1-F6-KR1 | OPE-ID-07 | K49 | KX17 | KX17 ≥ 60% |
| C1-F6-KR3 | GES-M2.2 | K50 | K165 | K165 ≥ 65% |
| C2-F1-KR1 | GOB-G4.2 | K86 | KX14 | KX14 ≤ 45% |
| C2-F1-KR2 | GOB-G2.2 | K74 | KX21 | KX21 ≥ 90% |
| C2-F1-KR3 | GOB-G3.2 | K57 | KX04 | KX04 ≥ 80% |
| C2-F2-KR1 | GES-M1.2 | K12 | KX15 | KX15 ≥ 75% |
| C2-F2-KR2 | GES-M1.1 | K100 | KX20 | KX20 ≥ 90% |
| C2-F3-KR1 | GES-M3.2 | K123 | KX19 | KX19 ≥ 95% |
| C2-F3-KR2 | OPE-PR-02 | K34 | KX10 | KX10 ≥ 95% |
| C2-F3-KR3 | OPE-PR-06 | K37 | KX22 | KX22 ≥ 90% |
| C2-F4-KR1 | OPE-DE-02 | K43 | KX05 | KX05 ≥ 65% |
| C2-F4-KR2 | OPE-DE-01 | K42 | KX03 | KX03 ≥ 90% |
| C2-F4-KR3 | GES-M5.1 | K32 | KX13 | KX13 ≤ 0 n.º |
| C2-F5-KR1 | GES-M6.2 | K132 | KX02 | KX02 ≥ 100% |
| C2-F5-KR2 | GES-M6.2 | K134 | KX06 | KX06 ≤ 10% |
| C2-F5-KR3 | GES-M6.2 | K62 | KX11 | KX11 ≥ 85% |
| C2-F6-KR1 | OPE-PR-11 | K165 | KX17 | KX17 ≥ 85% |
| C3-F1-KR2 | GOB-G3.2 | K80 | KX04 | KX04 ≥ 95% |
| C3-F2-KR1 | GES-M1.1 | K101 | KX12 | KX12 ≤ 30 minutos |
| C3-F2-KR2 | GES-M1.2 | K106 | KX15 | KX15 ≥ 90% |
| C3-F3-KR1 | GES-M3.1 | K118 | KX10 | KX10 ≥ 100% |
| C3-F4-KR1 | OPE-ID-05 | K144 | KX06 | KX06 ≤ 10% |
| C3-F5-KR1 | GES-M6.2 | K27 | KX08 | KX08 ≥ 40% |
| C3-F5-KR2 | GES-M6.2 | K135 | KX09 | KX09 ≥ 50% |
| C3-F5-KR3 | OPE-ID-04 | K143 | KX18 | KX18 ≥ 70% |
| C4-F1-KR2 | GOB-G4.1 | K85 | KX05 | KX05 ≥ 85% |
| C4-F2-KR1 | GES-M1.2 | K103 | KX16 | KX16 ≤ 15% |
| C4-F2-KR2 | GES-M1.2 | K13 | KX15 | KX15 ≥ 100% |
| C4-F4-KR1 | GES-M5.2 | K48 | KX18 | KX18 ≥ 85% |
| C4-F5-KR3 | GES-M3.2 | K123 | KX19 | KX19 ≥ 100% |

## 9. Cadencias del gobierno de proveedores

| ID | Cadencia | Rito | Propósito |
|---|---|---|---|
| RT04 | Mensual | Revisión de servicio con cada proveedor crítico | Revisar niveles de servicio, evidencia, hallazgos, cambios y riesgos. |
| RT13 | Semestral | Revisión del modelo de provisión y de los contratos | Decidir por función si se opera, se co-gestiona o se externaliza, y el estado de cada contrato. |
| RT16 | Anual | Ensayo de salida y recuperación de la plataforma de control | Probar la reversibilidad de un servicio crítico y la recuperación en un entorno aislado. |
| RT17 | Anual | Verificación independiente | Someter los riesgos altos y los servicios críticos a una revisión de un tercero. |

## 10. IA y agentes del proveedor

Si el proveedor usa IA o agentes para prestar el servicio, eso se declara y se registra: qué hacen, con qué datos y bajo qué supervisión humana. Es la cláusula ocho y el objetivo externalizado de los servicios OPE-ID-07, OPE-PR-11 y OPE-DE-06. Es un tema de base provisoria.

---

*Frontier CISO Atlas · Modelo Operativo CISO 365 · versión 2.0, revisión 2 · 15 de noviembre de 2026 · propuesta sujeta a validación · @SCavanna*

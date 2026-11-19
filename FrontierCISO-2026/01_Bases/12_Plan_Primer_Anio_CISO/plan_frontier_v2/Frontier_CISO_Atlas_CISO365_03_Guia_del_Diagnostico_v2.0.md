# Guía del diagnóstico

**Frontier CISO Atlas · Modelo Operativo CISO 365 · versión 2.0, revisión 2** · documento 03 de 16 · 15 de noviembre de 2026 · @SCavanna

> Propuesta de base, sujeta a validación y a calibración en cada organización. La ejecución se puede contratar; la rendición de cuentas, no.

## 1. Para qué sirve el diagnóstico

El diagnóstico responde una pregunta: ¿Qué tenemos, quién lo opera, qué evidencia lo respalda y qué puede dañar al negocio? Ocupa los primeros 60 días del ciclo 1. Su resultado es una línea base con evidencia, no una opinión.

**Trampa habitual:** El diagnóstico sin fecha de cierre, o el plan escrito antes de medir.

## 2. Instrumentos

| Instrumento | Contenido |
|---|---|
| Frontier_CISO_Atlas_CISO365_Diagnostico_v2.0.xlsx | Hojas Parámetros, Funciones, Zero Trust, Pila y cobertura, Servicios externalizados, Preguntas y Resultados. Es el registro formal. |
| CISO365_v2.0_Diagnostico_interactivo.html | La misma lógica en un archivo que se abre en el navegador. Útil para un taller o una entrevista; exporta a JSON y a CSV. |
| Versión 1.0 | Las 56 entrevistas y los 32 elementos de recepción del libro de evaluación y entrevistas siguen vigentes. |

## 3. Pasos

| Días | Qué se hace | Qué queda |
|:--:|---|---|
| 1 a 10 | Recibir el área: personas, presupuesto, contratos, compromisos y riesgos abiertos. Fijar el alcance y los entornos. | Acta de recepción; lista de entornos; lista de contratos. |
| 11 a 30 | Calificar las 59 funciones con la escala de evidencia. Registrar quién opera cada una y quién es su dueño. | Hoja Funciones completa; funciones sin dueño identificadas. |
| 21 a 40 | Calificar los 42 criterios Zero Trust. Relevar la pila de herramientas y la cobertura por entorno. | Postura Zero Trust; solapamientos; paridad entre entornos. |
| 31 a 50 | Revisar cada contrato de servicio externalizado con las 14 comprobaciones. | Puntaje por contrato; decisión de mantener, renegociar o reemplazar. |
| 41 a 55 | Medir la línea base de los indicadores elegidos. | Valores de partida en el libro de KPIs y tablero. |
| 51 a 60 | Leer los resultados, ordenar las prioridades y preparar el plan del ciclo 1. | Informe de diagnóstico; propuesta de OKR; decisiones a pedir. |

Los rangos de días son una guía: se solapan a propósito.

## 4. Cómo calificar una función

1. Lea la evidencia que corresponde a «Implementado» y a «Probado» en la fila de la función.
2. Asigne el nivel que la evidencia disponible sostiene, no el que se declara. Sin evidencia a la vista, el nivel es 1 o menos.
3. Registre el modelo de provisión y el nombre del dueño. Una función sin dueño no puede superar el nivel 1.
4. Ajuste la criticidad (1 a 3) si la propuesta del modelo no refleja a la organización.

El libro y el archivo HTML calculan el resto con estas reglas:

| Cálculo | Regla |
|---|---|
| Nivel objetivo | 3 si la criticidad es alta; 2 en el resto. Ambos valores son parámetros. |
| Brecha | Nivel objetivo menos nivel de evidencia; nunca negativa. |
| Prioridad | Brecha × criticidad. |
| Etapa sugerida | Ciclo 1 si la función no existe o si es crítica y está en nivel 0 o 1. Ciclo 2 si es crítica y tiene brecha. Ciclo 3 si tiene brecha y no es crítica. «Sostener» si no hay brecha. |
| Versión externalizada | Se aplica si la función está externalizada o co-gestionada. |

## 5. Postura Zero Trust

42 criterios en ocho dominios y tres principios, independientes de proveedores. Se califican con la misma escala. Los seis del dominio «IA y agentes» son de base provisoria.

| ID | Dominio | Principio | Criterio | Base |
|---|---|---|---|:--:|
| ZT-ID-1 | Identidades | Verificar de forma explícita | Todas las personas se autentican con métodos resistentes a la suplantación; las cuentas privilegiadas, sin excepción. | Firme |
| ZT-ID-2 | Identidades | Verificar de forma explícita | Cada solicitud de acceso se evalúa con señales de identidad, dispositivo, ubicación y riesgo antes de concederse. | Firme |
| ZT-ID-3 | Identidades | Mínimo privilegio | Los privilegios se conceden por tiempo limitado y por tarea; no hay privilegios permanentes. | Firme |
| ZT-ID-4 | Identidades | Mínimo privilegio | Las altas, los cambios y las bajas de identidades están automatizados y los accesos se recertifican. | Firme |
| ZT-ID-5 | Identidades | Asumir la vulneración | Las identidades no humanas —servicios, cargas y agentes— tienen dueño, credenciales rotadas y privilegio revisado. | Firme |
| ZT-ID-6 | Identidades | Asumir la vulneración | Un proveedor de identidad central federa las aplicaciones críticas de todos los entornos. | Firme |
| ZT-DI-1 | Dispositivos | Verificar de forma explícita | Solo los dispositivos inventariados, gestionados y conformes acceden a los recursos corporativos. | Firme |
| ZT-DI-2 | Dispositivos | Verificar de forma explícita | El estado del dispositivo se evalúa en cada acceso, no solo cuando se lo registra. | Firme |
| ZT-DI-3 | Dispositivos | Mínimo privilegio | Los usuarios no trabajan con privilegios de administrador local. | Firme |
| ZT-DI-4 | Dispositivos | Asumir la vulneración | Todos los dispositivos tienen protección y respuesta, con telemetría centralizada. | Firme |
| ZT-DI-5 | Dispositivos | Asumir la vulneración | Los parches críticos se aplican dentro del plazo definido. | Firme |
| ZT-AP-1 | Aplicaciones y cargas | Verificar de forma explícita | Las aplicaciones autentican a los usuarios y a otras cargas mediante la identidad central; no hay cuentas locales compartidas. | Firme |
| ZT-AP-2 | Aplicaciones y cargas | Mínimo privilegio | El acceso se concede por aplicación, no por pertenecer a una red. | Firme |
| ZT-AP-3 | Aplicaciones y cargas | Asumir la vulneración | El ciclo de desarrollo incluye controles automatizados y bloquea lo que no los supera. | Firme |
| ZT-AP-4 | Aplicaciones y cargas | Asumir la vulneración | Los componentes de terceros están inventariados y sus vulnerabilidades se gestionan. | Firme |
| ZT-AP-5 | Aplicaciones y cargas | Asumir la vulneración | Los secretos no están en el código ni en las configuraciones: se guardan en una bóveda y se rotan. | Firme |
| ZT-DA-1 | Datos | Verificar de forma explícita | Los datos sensibles están descubiertos, clasificados y etiquetados en todos los entornos. | Firme |
| ZT-DA-2 | Datos | Mínimo privilegio | El acceso a los datos se concede por necesidad y la sobreexposición se corrige. | Firme |
| ZT-DA-3 | Datos | Asumir la vulneración | La salida de datos sensibles se controla en el correo, la nube, los dispositivos y la IA. | Firme |
| ZT-DA-4 | Datos | Asumir la vulneración | Los datos están cifrados en tránsito y en reposo, con las claves bajo el control de la organización. | Firme |
| ZT-DA-5 | Datos | Asumir la vulneración | Existen respaldos inalterables con restauración probada. | Firme |
| ZT-IN-1 | Infraestructura | Verificar de forma explícita | Todos los entornos —nubes y centros de datos— se despliegan bajo una línea base común y su cumplimiento se verifica. | Firme |
| ZT-IN-2 | Infraestructura | Mínimo privilegio | La administración de la infraestructura usa acceso privilegiado por tiempo limitado y estaciones dedicadas. | Firme |
| ZT-IN-3 | Infraestructura | Asumir la vulneración | La deriva de configuración se detecta y se corrige en plazo. | Firme |
| ZT-IN-4 | Infraestructura | Asumir la vulneración | Las cargas tienen protección en tiempo de ejecución y las imágenes se analizan antes de desplegarlas. | Firme |
| ZT-IN-5 | Infraestructura | Asumir la vulneración | La plataforma de control —identidad, gestión y respaldo— puede recuperarse en un entorno aislado. | Firme |
| ZT-RE-1 | Red | Verificar de forma explícita | Ninguna ubicación de red otorga confianza por sí misma: la red interna se trata como no confiable. | Firme |
| ZT-RE-2 | Red | Mínimo privilegio | Los activos críticos están segmentados y la segmentación se verifica con pruebas. | Firme |
| ZT-RE-3 | Red | Mínimo privilegio | El acceso remoto llega a aplicaciones concretas, no a segmentos completos de la red. | Firme |
| ZT-RE-4 | Red | Asumir la vulneración | El tráfico está cifrado y el que cruza entre segmentos críticos se inspecciona. | Firme |
| ZT-RE-5 | Red | Asumir la vulneración | Las reglas de red se revisan y se eliminan las que no se usan o son demasiado amplias. | Firme |
| ZT-VA-1 | Visibilidad, automatización y gobierno | Verificar de forma explícita | La telemetría de identidades, dispositivos, aplicaciones, datos, infraestructura y red llega a una plataforma central. | Firme |
| ZT-VA-2 | Visibilidad, automatización y gobierno | Verificar de forma explícita | Las políticas de acceso se definen una vez y se aplican de manera uniforme en todos los entornos. | Firme |
| ZT-VA-3 | Visibilidad, automatización y gobierno | Asumir la vulneración | Las detecciones se prueban contra las técnicas de ataque priorizadas. | Firme |
| ZT-VA-4 | Visibilidad, automatización y gobierno | Asumir la vulneración | La respuesta a los eventos frecuentes está automatizada, con aprobación humana donde el impacto lo exige. | Firme |
| ZT-VA-5 | Visibilidad, automatización y gobierno | Asumir la vulneración | La arquitectura Zero Trust tiene dueño, hoja de ruta y medición informada a la dirección. | Firme |
| ZT-IA-1 | IA y agentes | Verificar de forma explícita | Todo sistema de IA y todo agente está inventariado, con dueño y propósito. | Provisoria |
| ZT-IA-2 | IA y agentes | Verificar de forma explícita | Cada agente tiene identidad propia: no usa la de su creador ni credenciales compartidas. | Provisoria |
| ZT-IA-3 | IA y agentes | Mínimo privilegio | Cada agente accede solo a las herramientas, los datos y las acciones que su tarea requiere, con un nivel de autonomía aprobado. | Provisoria |
| ZT-IA-4 | IA y agentes | Mínimo privilegio | Los datos que usan los sistemas de IA están clasificados y la IA respeta sus permisos y sus etiquetas. | Provisoria |
| ZT-IA-5 | IA y agentes | Asumir la vulneración | El contenido que el agente procesa nunca se trata como una instrucción: hay filtros, límites de acción fuera del modelo y pruebas adversariales. | Provisoria |
| ZT-IA-6 | IA y agentes | Asumir la vulneración | La actividad de los agentes se registra fuera de su alcance, se vigila y puede detenerse y revertirse. | Provisoria |

## 6. Pila de herramientas y cobertura por entorno

Para cada uno de los 35 servicios de operación se registra la cobertura en cada entorno, la herramienta principal, quién la opera, si hay herramientas solapadas y si está integrada a la telemetría central. El libro admite hasta 6 entornos: nube pública a, nube pública b, centro de datos propio, servicios en línea críticos, puestos de trabajo y movilidad, tecnología operacional. De ahí salen dos medidas: la paridad de control entre entornos (K123) y el solapamiento sin justificación (K122).

## 7. Servicios externalizados

Un renglón por contrato y 14 comprobaciones, que se responden con Sí, Parcial o No. El puntaje es la proporción de respuestas afirmativas; una respuesta parcial vale la mitad. Con menos de 70% el contrato requiere acción.

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

## 8. Preguntas de relevamiento

| N.º | Tema | A quién | Pregunta | Evidencia que pedir |
|:--:|---|---|---|---|
| 1 | Servicios externalizados | Dueño interno del servicio | ¿Qué servicios de seguridad opera hoy un tercero y quién responde internamente por cada uno? | Registro de contratos; nombre de cada dueño. |
| 2 | Servicios externalizados | Compras y legal | ¿Qué contratos vencen en los próximos 12 meses y cuáles se renuevan de forma automática? | Calendario de contratos. |
| 3 | Servicios externalizados | Dueño interno del servicio | ¿Cómo sabemos que el proveedor cumple: por sus informes o por una verificación propia? | Última verificación independiente. |
| 4 | Servicios externalizados | Proveedor | ¿Qué decisiones toma el proveedor sin consultar y cuáles escala? | Matriz de decisiones; registro de escalamientos. |
| 5 | Servicios externalizados | Proveedor | Si mañana se dejara el servicio, ¿qué entrega el proveedor, en qué formato y en cuánto tiempo? | Plan de salida; prueba de exportación. |
| 6 | Servicios externalizados | Proveedor | ¿El proveedor usa IA o agentes para prestar el servicio? ¿Con qué datos de la organización y con qué supervisión humana? | Declaración de uso de IA. |
| 7 | Entornos y herramientas | CIO y CTO | ¿En qué nubes, centros de datos y servicios en línea corren los procesos críticos, y quién administra cada entorno? | Mapa de entornos. |
| 8 | Entornos y herramientas | Arquitectura | ¿Qué control existe en el entorno principal y falta en los demás? | Matriz de cobertura por entorno. |
| 9 | Entornos y herramientas | Operaciones | ¿Qué capacidades están cubiertas por dos herramientas y cuáles por ninguna? | Inventario de herramientas. |
| 10 | Entornos y herramientas | CIO y CTO | ¿Qué cuentas, suscripciones o proyectos de nube existen fuera de la línea base? | Inventario de nube. |
| 11 | Entornos y herramientas | Operaciones | ¿Qué fuentes críticas no envían sus registros a la plataforma central? | Lista de fuentes integradas. |
| 12 | Entornos y herramientas | Finanzas | ¿Cuál es el costo total de cada herramienta: licencias, operación, personas y servicios? | Presupuesto y contratos. |
| 13 | Zero Trust | Identidad | ¿Quién puede entrar hoy a un sistema crítico solo con usuario y contraseña? | Reporte de métodos de autenticación. |
| 14 | Zero Trust | Identidad | ¿Cuántas cuentas tienen privilegios permanentes y cuántas de ellas son de proveedores? | Inventario de cuentas privilegiadas. |
| 15 | Zero Trust | Redes | Si un atacante toma un puesto de trabajo, ¿hasta dónde llega sin encontrar un control? | Prueba de segmentación. |
| 16 | Zero Trust | Datos | ¿Dónde están los datos más sensibles y quién puede leerlos hoy? | Mapa de datos; análisis de permisos. |
| 17 | Zero Trust | Operaciones | ¿Cuándo se restauró por última vez un sistema crítico desde un respaldo y cuánto tardó? | Informe de restauración. |
| 18 | Zero Trust | CIO y CTO | ¿Se puede reconstruir el servicio de identidad en un entorno aislado? ¿Se probó? | Prueba de recuperación. |
| 19 | IA y agentes | Negocio y tecnología | ¿Qué sistemas de IA y qué agentes usa la organización, incluidos los que nadie aprobó? | Registro; descubrimiento. |
| 20 | IA y agentes | Dueños de agentes | ¿Con qué identidad actúa cada agente y qué puede hacer con ella? | Permisos efectivos por agente. |
| 21 | IA y agentes | Dueños de agentes | ¿Qué acciones puede ejecutar un agente sin aprobación humana y quién lo autorizó? | Niveles de autonomía aprobados. |
| 22 | IA y agentes | Operaciones | ¿Queda registro de lo que hace cada agente en un lugar que el agente no puede modificar? | Trazas. |
| 23 | IA y agentes | Dueños de agentes | ¿Se probó detener a cada agente? ¿Cuánto tarda? | Prueba de detención. |
| 24 | IA y agentes | Legal y datos | ¿Qué datos de la organización llegan a servicios de IA de terceros y bajo qué condiciones? | Contratos; control de salida de datos. |

## 9. Cuándo termina el diagnóstico

El diagnóstico termina cuando se cumplen sus criterios de salida, no cuando se acaba el tiempo.

1. Acta de recepción firmada: personas, presupuesto, contratos, compromisos y riesgos abiertos.
2. Diagnóstico por función completo: nivel de evidencia y modelo de provisión de las 59 funciones.
3. Registro de servicios externalizados con dueño interno, alcance y fecha de fin de contrato.
4. Mapa de entornos y cobertura de control medida en cada uno.
5. Postura Zero Trust evaluada en los ocho dominios.
6. Línea base medida para los indicadores principales de las tres audiencias.
7. Escenarios de riesgo prioritarios acordados con los dueños del negocio.
8. Propuesta de cuatro ciclos, presupuesto y decisiones requeridas presentada al sponsor.

## 10. Uso como evaluación de la gestión de un CISO

El mismo instrumento sirve para evaluar una gestión en curso o para ordenar una serie de entrevistas.

- **Como autoevaluación.** El CISO califica con su equipo y repite la calificación una vez por año (cadencia RT15). La diferencia entre dos mediciones es el avance.
- **Como evaluación independiente.** Un tercero califica con la misma escala y pide la evidencia de cada nivel. La comparación con la autoevaluación muestra dónde se sobrestima.
- **Como guía de entrevistas.** Las preguntas de la sección 8 y las 56 entrevistas de la versión 1.0 se asignan por interlocutor; cada respuesta se ata a una función y a una evidencia.
- **Para definir servicios de asesoría o consultoría.** Cada brecha prioritaria sugiere un tipo de ayuda: una función que no existe pide diseño; una documentada y sin operar pide implementación; una implementada y sin probar pide verificación; un contrato por debajo del umbral pide renegociación.

| Hallazgo del diagnóstico | Tipo de servicio que sugiere |
|---|---|
| Función en nivel 0 o «No existe» | Diseño de la función, de su dueño y de su modelo de provisión |
| Función en nivel 1 (documentada, sin operar) | Implementación y puesta en operación |
| Función en nivel 2 (implementada, sin probar) | Prueba, ejercicio o revisión independiente |
| Contrato con puntaje menor que el umbral | Revisión del contrato, de los niveles de servicio y de la evidencia |
| Paridad baja entre entornos | Línea base común y plan de cobertura por entorno |
| Herramientas solapadas sin justificación | Racionalización de la pila |
| Indicadores sin línea base, dueño o fuente | Diseño del sistema de medición y del tablero |
| Criterios de IA y agentes en nivel 0 o 1 | Inventario, identidad y límites de los agentes |

---

*Frontier CISO Atlas · Modelo Operativo CISO 365 · versión 2.0, revisión 2 · 15 de noviembre de 2026 · propuesta sujeta a validación · @SCavanna*

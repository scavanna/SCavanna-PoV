# Modelo Operativo CISO 365 · 04 · Guía de evaluación y entrevistas

**AI CISO Atlas · v1.0 · 10 de noviembre de 2026** · Cómo evaluar la gestión de un CISO y descubrir áreas de mejora y servicios.


## 1. Ética y alcance

- **Evalúa el sistema, no a la persona.** Se evalúa el sistema de gobierno y gestión que el CISO lidera, con evidencia. No es una evaluación de desempeño individual ni reemplaza procesos de recursos humanos.
- **No es una auditoría ni una certificación.** Un nivel alto no equivale a cumplimiento normativo.
- **Confidencialidad.** Respuestas y evidencias son información sensible de la organización evaluada.
- **Contexto.** La exigencia depende de los días en el cargo: no se le pide al día 100 lo que corresponde al día 365.

## 2. Modos de uso

| Modo | Quién | Cuándo | Resultado |
|---|---|---|---|
| Autoevaluación | CISO y su equipo | Cada año (ritual R42) y en H100 como línea base | Nivel de evidencia por práctica (KSG05) y plan de mejora |
| Evaluación externa | Asesor independiente | A pedido del sponsor, del comité o del directorio | Informe de evaluación con evidencia y recomendaciones |
| Entrevista de descubrimiento | Asesor o consultor | Antes de proponer servicios | Brechas priorizadas y servicios sugeridos |

## 3. Escala de evidencia

| Nivel | Nombre | Qué hay que ver |
|---|---|---|
| 0 | No definido | No existe o existe solo de palabra. |
| 1 | Documentado | Está escrito y aprobado, pero no se aplica de forma consistente. |
| 2 | Implementado | Se aplica en la mayoría de los casos y hay registros. |
| 3 | Probado | Se probó (ejercicio, auditoría, muestra) y funciona; para este nivel, al menos dos fuentes independientes. |
| 4 | Adaptativo | Se mejora con lo aprendido y se anticipa a cambios del contexto; también con dos fuentes independientes. |

## 4. Reglas

- Dos prácticas por unidad GM-24 y tres de la práctica del CISO; cuando una unidad fusiona unidades del programa de 32 de la formación, cada unidad de origen queda cubierta por al menos una práctica (G6.2: ética y medición; M3.2: selección y evaluación de controles; M6.2: redes, nube, OT, IA, desarrollo seguro y cadena de suministro).
- La evidencia vale más que la declaración: se puntúa lo que la evidencia sostiene.
- Lo no evaluado se deja en blanco, no en cero.
- Un cero en una práctica crítica no se compensa con promedios: el libro lo advierte.
- Cada práctica tiene un hito en el que debería estar instalada y un nivel mínimo esperado; con los días en el cargo, el libro calcula si ya es exigible y si cumple.

## 5. Procedimiento

1. Acordar alcance, interlocutores y confidencialidad con el sponsor.
2. Pedir la evidencia mínima (carta, actas, registro de riesgos, tablero, plan de respuesta, resultados de pruebas).
3. Entrevistar por interlocutor con la guía de preguntas; registrar notas y la preparación de la respuesta (0 a 4).
4. Puntuar cada práctica con la escala de evidencia y registrar la evidencia revisada.
5. Revisar resultados por línea de trabajo y por hito, y las prácticas críticas en nivel 0.
6. Priorizar las 10 brechas ponderadas más altas (hoja Plan de mejora) y vincularlas a servicios.
7. Presentar el informe y acordar acciones, responsables y fechas.

## 6. Prácticas evaluadas

| ID | Línea | Práctica | Hito | Nivel mínimo | Peso | Indicador de verificación | Señal de alerta |
|---|---|---|---|---|---|---|---|
| EV01 | G1 · Base estratégica y contextual | Mandato y carta de la función acordados por escrito y revisados cada año | H100 | 2 | 3 | K14; KSG03 | El alcance se deduce del organigrama; el CISO no accede al directorio; reporta a quien opera lo que debe supervisar sin contrapesos. |
| EV02 | G1 · Base estratégica y contextual | Contexto organizacional y cultura diagnosticados y usados para priorizar | H60 | 2 | 3 | K21 | Lista de sistemas sin vínculo con procesos; el dueño de todo es tecnología. |
| EV03 | G1 · Base estratégica y contextual | Estrategia en una página, ligada a objetivos del negocio, con 3 a 5 prioridades | H100 | 2 | 3 | K17 | La estrategia es una lista de proyectos tecnológicos o tiene más de siete prioridades. |
| EV04 | G1 · Base estratégica y contextual | Inversión trazada a riesgos: inversión, capacidad y riesgo reducido | H180 | 2 | 2 | K17; K19 | Presupuesto por histórico y renovaciones; nadie mide el beneficio. |
| EV05 | G2 · Marcos normativos y políticos | Marco de referencia elegido y adaptado, con perfil actual y objetivo | H60 | 2 | 2 | K22 | Puntajes sin evidencia; cambio de marco cada año; perfil objetivo nunca aprobado. |
| EV06 | G2 · Marcos normativos y políticos | Reevaluación anual con el mismo método y validación independiente periódica | H365 | 3 | 2 | K22; KSG05 | La madurez sube sin cambios en los controles; la autoevaluación no se contrasta. |
| EV07 | G2 · Marcos normativos y políticos | Marco de políticas con jerarquía, dueños, vigencia y aplicabilidad probada (incluye IA) | H180 | 2 | 2 | K63 | Políticas copiadas de plantillas, vencidas o que nadie sabe cuál rige. |
| EV08 | G2 · Marcos normativos y políticos | Excepciones justificadas, con dueño, compensación y vencimiento | H180 | 2 | 2 | K63 | Excepciones permanentes o aprobadas por el área técnica. |
| EV09 | G3 · Entorno legal y de cumplimiento | Obligaciones y plazos de notificación inventariados, con dueño | H60 | 2 | 3 | K61; K57 | No se conocen los plazos; legal se entera tarde. |
| EV10 | G3 · Entorno legal y de cumplimiento | Requisitos de seguridad de clientes y contratos cumplidos en plazo | H270 | 2 | 1 | K23 | Se firman cláusulas sin consultar y se descubren en una auditoría del cliente. |
| EV11 | G3 · Entorno legal y de cumplimiento | Obligaciones mapeadas a controles con evidencia vigente | H270 | 2 | 2 | K57 | La evidencia se fabrica para la auditoría. |
| EV12 | G3 · Entorno legal y de cumplimiento | Hallazgos cerrados en plazo y plan de aseguramiento coordinado | H180 | 2 | 2 | K59 | Reprogramaciones sucesivas sin aceptación formal del riesgo. |
| EV13 | G4 · Gobernanza y apetito de riesgo | Comité de ciberriesgo con mandato, calendario, actas y decisiones | H180 | 2 | 3 | K14; KSG02 | El comité es informativo; no asisten los titulares; no hay decisiones registradas. |
| EV14 | G4 · Gobernanza y apetito de riesgo | Dueños de riesgo en el negocio, con matriz RACI aprobada | H180 | 2 | 3 | K09; KSG03 | Todos los riesgos tienen al CISO o a tecnología como dueño. |
| EV15 | G4 · Gobernanza y apetito de riesgo | Apetito y tolerancias aprobados, accionables y ratificados cada año | H180 | 2 | 3 | K25 | Apetito genérico («bajo») sin umbrales; nadie lo usa para decidir. |
| EV16 | G4 · Gobernanza y apetito de riesgo | Riesgo residual comparado con el apetito; desvíos con plan o aceptación | H270 | 2 | 3 | K25; K08 | No se puede responder o los desvíos no se reportan. |
| EV17 | G5 · Supervisión de la gestión de riesgos | Escenarios prioritarios con impacto estimado en rangos y supuestos explícitos | H60 | 2 | 3 | K26 | Mapas de calor sin supuestos o cifras precisas sin rango. |
| EV18 | G5 · Supervisión de la gestión de riesgos | Pronósticos registrados y calibración del juicio revisada | H365 | 1 | 1 | K01 | No existe registro; todo error se atribuye a la mala suerte. |
| EV19 | G5 · Supervisión de la gestión de riesgos | Aceptaciones de riesgo con alternativas, autoridad correcta, compensaciones y vencimiento | H180 | 2 | 3 | K04; KSG03 | Aceptaciones firmadas por el área técnica, sin vencimiento ni compensación. |
| EV20 | G5 · Supervisión de la gestión de riesgos | Transferencia revisada: seguro con coberturas, exclusiones y requisitos frente a controles reales | H270 | 2 | 1 | K24 | La póliza se renueva sin revisar requisitos ni exclusiones. |
| EV21 | G6 · Liderazgo, comunicación y medición | Reporte al directorio con riesgo frente al apetito, tendencia, incertidumbre y decisiones | H180 | 2 | 3 | K58; K14 | Reportes de actividad técnica; el directorio no decide nada. |
| EV22 | G6 · Liderazgo, comunicación y medición | Comunicación ejecutiva y de crisis preparada, con formación ejecutiva periódica | H270 | 2 | 2 | K05; K15 | No hay voceros definidos; la decisión se improvisa. |
| EV23 | G6 · Liderazgo, comunicación y medición | Medición de la efectividad del gobierno y del programa: tablero de KPI, KRI y KCI con fórmula, fuente, meta y uso en decisiones | H180 | 2 | 2 | K58; KSG04 | Decenas de métricas técnicas y ninguna con meta. |
| EV24 | G6 · Liderazgo, comunicación y medición | Liderazgo ético y rendición de cuentas: conflictos de interés declarados, debida diligencia en las decisiones y lo prometido frente a lo cumplido | H365 | 2 | 3 | K03; KSG06; KSG01 | El informe solo muestra logros; no hay compromisos medibles ni declaraciones de conflictos de interés. |
| EV25 | M1 · Fundación del programa y liderazgo | Recepción formal del área y decisión sobre el portafolio heredado | H30 | 2 | 2 | K18 | No hay registro de lo recibido; se arrastran proyectos sin dueño. |
| EV26 | M1 · Fundación del programa y liderazgo | Hoja de ruta de 12 a 24 meses con dueños, dependencias y avance medido | H100 | 2 | 3 | K18 | La hoja de ruta no se actualiza; todo figura «en curso». |
| EV27 | M1 · Fundación del programa y liderazgo | Presupuesto planificado con el ciclo fiscal, seguido y defendido con riesgo | H180 | 2 | 2 | K17 | El CISO no conoce su presupuesto o depende de tecnología sin trazabilidad. |
| EV28 | M1 · Fundación del programa y liderazgo | Equipo con roles claros, capacidades críticas cubiertas, suplentes y plan de desarrollo | H180 | 2 | 2 | K12; K16 | Dependencia de una persona; alta rotación sin plan. |
| EV29 | M2 · Protección de activos e identidades | Inventario de activos y servicios críticos con dueño y criticidad | H60 | 2 | 3 | K39 | Inventario desactualizado; nube u OT fuera del inventario. |
| EV30 | M2 · Protección de activos e identidades | Datos sensibles clasificados y protegidos, incluida su interacción con IA | H270 | 2 | 2 | K37; K52 | Clasificación sin uso; prevención de fuga solo en modo auditoría. |
| EV31 | M2 · Protección de activos e identidades | Autenticación resistente al phishing y sin privilegios permanentes | H270 | 2 | 3 | K33; K34 | Excepciones masivas de autenticación; administradores permanentes. |
| EV32 | M2 · Protección de activos e identidades | Identidades no humanas y agentes con dueño humano y autoridad acotada | H365 | 2 | 2 | K50 | Cuentas de servicio sin dueño; agentes con permisos amplios. |
| EV33 | M3 · Arquitectura y controles técnicos | Arquitectura objetivo y seguridad integrada temprano en proyectos | H270 | 2 | 2 | K20 | Seguridad llega al final y se percibe como freno. |
| EV34 | M3 · Arquitectura y controles técnicos | Confianza Cero como estrategia de arquitectura: segmentación de activos críticos verificada y herramientas alineadas a la arquitectura | H365 | 2 | 2 | K36 | Red plana; herramientas superpuestas compradas sin una arquitectura de referencia. |
| EV35 | M3 · Arquitectura y controles técnicos | Controles seleccionados según el riesgo, implementados con responsable y documentados, incluida la configuración segura | H270 | 2 | 2 | K35 | Controles elegidos por herramienta y no por riesgo; nadie responde por ellos; desvíos de configuración sin medir. |
| EV36 | M3 · Arquitectura y controles técnicos | Efectividad de los controles evaluada y probada: muestreo de controles clave, análisis de vulnerabilidades y pruebas de penetración o red team, con plan de remediación | H270 | 2 | 3 | K60 | Se confunde control configurado con control efectivo; alcance cosmético; hallazgos repetidos año tras año. |
| EV37 | M4 · Operaciones proactivas y gestión de amenazas | Detección con cobertura de activos críticos y técnicas priorizadas validadas | H180 | 2 | 3 | K41; K42; K43 | Monitoreo sin casos de uso; se mide el volumen de alertas. |
| EV38 | M4 · Operaciones proactivas y gestión de amenazas | Modelo de operaciones gobernado por resultados, con decisiones indelegables internas | H180 | 2 | 2 | K45; K55 | El proveedor declara incidentes; acuerdos de nivel de servicio de actividad. |
| EV39 | M4 · Operaciones proactivas y gestión de amenazas | Ciclo continuo de exposición priorizado por riesgo, con plazos por criticidad | H180 | 2 | 3 | K46 | Se reporta la cantidad total de vulnerabilidades sin priorización. |
| EV40 | M4 · Operaciones proactivas y gestión de amenazas | Inteligencia de amenazas y panorama del sector que informan prioridades | H270 | 2 | 1 | K43; K44 | La inteligencia son listas de indicadores sin análisis. |
| EV41 | M5 · Respuesta a incidentes y gestión de crisis | Plan de respuesta vigente con matriz de decisión y playbooks probados | H180 | 2 | 3 | K32 | Plan genérico con roles que ya no existen. |
| EV42 | M5 · Respuesta a incidentes y gestión de crisis | Ejercicios: técnico semestral y de crisis ejecutiva anual, con acciones cerradas | H270 | 3 | 3 | K15 | Ejercicios sin observadores, sin acciones o sin ejecutivos. |
| EV43 | M5 · Respuesta a incidentes y gestión de crisis | Revisiones posteriores que evalúan decisiones y cierran acciones en plazo | H270 | 2 | 2 | K48; K06 | Revisiones técnicas sin acciones o con búsqueda de culpables. |
| EV44 | M5 · Respuesta a incidentes y gestión de crisis | Notificaciones en plazo y tiempo hasta la decisión ejecutiva medido | H270 | 2 | 2 | K61; K05 | Notificaciones tardías; nadie mide el tiempo de decisión. |
| EV45 | M6 · Resiliencia, tecnologías clave y cadena de suministro | Recuperación de servicios críticos probada frente a RTO y RPO | H270 | 3 | 3 | K30; K28 | Tiempos de recuperación declarados y nunca probados. |
| EV46 | M6 · Resiliencia, tecnologías clave y cadena de suministro | BIA vigente con dependencias y operación degradada probada | H365 | 2 | 2 | K21; K29; K56 | BIA de hace años; no existe modo degradado. |
| EV47 | M6 · Resiliencia, tecnologías clave y cadena de suministro | Cadena de suministro y desarrollo seguro: terceros críticos evaluados y con cláusulas, concentración conocida y seguridad integrada en el ciclo de desarrollo | H270 | 2 | 3 | K31; K27; K38 | Cuestionarios sin seguimiento; concentración no evaluada; aplicaciones críticas sin controles en el ciclo de desarrollo. |
| EV48 | M6 · Resiliencia, tecnologías clave y cadena de suministro | Tecnologías clave bajo gobierno: red, nube híbrida y OT evaluadas; IA con inventario, evaluación previa, política y pruebas adversariales | H180 | 2 | 3 | K49; K51; K54; K40 | IA no autorizada sin inventario; nube u OT sin evaluación ni dueño. |
| EV49 | J · Juicio y práctica del CISO (territorio T01) | Diario de decisiones con supuestos, alternativas y revisión posterior | H100 | 1 | 2 | K03 | Decisiones sin registro; justificación construida después del resultado. |
| EV50 | J · Juicio y práctica del CISO (territorio T01) | Agenda protegida para gobierno y negocio; delegación efectiva | H180 | 2 | 2 | K02 | El CISO es el principal operador del SOC. |
| EV51 | J · Juicio y práctica del CISO (territorio T01) | Plan de desarrollo personal con práctica deliberada y retroalimentación | H365 | 1 | 1 | K07 | No hay mentor ni retroalimentación; aprendizaje solo técnico. |

## 7. Protocolo de entrevista por interlocutor

### CISO (6)

| ID | Pregunta | Qué se busca entender | Señal positiva | Señal de alerta | Prácticas | Momento |
|---|---|---|---|---|---|---|
| EN01 | ¿Cuál es su mandato y cómo lo comprobaría alguien ajeno a su área? | Claridad de alcance, autoridad y línea de reporte. | Carta aprobada y ejemplos de decisiones tomadas dentro del mandato. | «Depende» o «se sobreentiende»; no hay documento. | EV01 | Recepción · Evaluación · Descubrimiento |
| EN02 | ¿Qué riesgos le quitan el sueño y qué decidió la dirección sobre cada uno? | Escenarios priorizados y decisiones de gobierno. | Tres a cinco escenarios con dueño, decisión y seguimiento. | Lista técnica sin decisiones ni dueños. | EV17; EV15 | Recepción · Evaluación · Descubrimiento |
| EN03 | ¿Qué prometió al asumir o al inicio del año, y qué cumplió? | Compromisos medibles y rendición de cuentas. | Compromisos con evidencia, incluidos los no cumplidos y su explicación. | No hubo compromisos o solo se mencionan logros. | EV24; EV26 | Recepción · Evaluación · Descubrimiento |
| EN04 | ¿Qué hace hoy que debería hacer otra persona o un proveedor? | Delegación y foco en gobierno. | Lista concreta con plan de delegación. | El CISO opera personalmente lo cotidiano. | EV50; EV38 | Recepción · Evaluación · Descubrimiento |
| EN05 | ¿Qué evidencia mostraría para probar que puede recuperar su servicio más crítico? | Resiliencia demostrada, no declarada. | Prueba reciente con tiempos medidos frente a RTO y RPO. | Respuestas basadas en lo que dice el contrato o el plan. | EV45 | Recepción · Evaluación · Descubrimiento |
| EN06 | ¿Qué necesita de la dirección que todavía no pidió formalmente? | Apoyos y decisiones pendientes. | Pedidos concretos con impacto en riesgo si no se conceden. | Quejas genéricas sin pedido formal. | EV27; EV03 | Recepción · Evaluación · Descubrimiento |

### Sponsor o CEO (5)

| ID | Pregunta | Qué se busca entender | Señal positiva | Señal de alerta | Prácticas | Momento |
|---|---|---|---|---|---|---|
| EN07 | ¿Qué espera de la función de seguridad en los próximos 12 meses y cómo sabrá que se cumplió? | Expectativas medibles y alineación con el CISO. | Expectativas concretas que coinciden con las del CISO. | Expectativas vagas («que no pase nada»). | EV01; EV24 | Recepción · Evaluación · Descubrimiento |
| EN08 | ¿Qué decisiones de riesgo cibernético tomó la dirección este año? | Ejercicio real del gobierno. | Ejemplos de aceptaciones, inversiones o límites decididos. | «Eso lo decide el CISO». | EV15; EV19 | Recepción · Evaluación · Descubrimiento |
| EN09 | ¿Cómo se entera de que algo va mal en seguridad, y con cuánta anticipación? | Reporte y escalamiento. | Indicadores de alerta temprana y escalamiento acordado. | Se entera por un incidente o por la prensa. | EV21; EV44 | Recepción · Evaluación · Descubrimiento |
| EN10 | ¿Qué iniciativa de negocio se aceleró o se frenó por seguridad este año? | Seguridad como habilitador. | Ejemplos de habilitación con tiempos medidos. | Solo ejemplos de bloqueo. | EV33 | Recepción · Evaluación · Descubrimiento |
| EN11 | Si mañana hubiera un incidente mayor, ¿qué haría usted en la primera hora? | Preparación ejecutiva. | Conoce su rol, la cadena de decisión y los voceros. | No sabe a quién llamar ni qué decidir. | EV22; EV42 | Recepción · Evaluación · Descubrimiento |

### Directorio o comité de auditoría y riesgos (5)

| ID | Pregunta | Qué se busca entender | Señal positiva | Señal de alerta | Prácticas | Momento |
|---|---|---|---|---|---|---|
| EN12 | ¿El reporte de seguridad le permite decidir o solo informarse? | Calidad del reporte al directorio. | Decisiones tomadas a partir del reporte. | Reportes extensos de actividad técnica. | EV21 | Recepción · Evaluación · Descubrimiento |
| EN13 | ¿Conoce el apetito de riesgo cibernético aprobado y cuándo se usó por última vez? | Apetito vivo. | Ejemplo reciente de uso para decidir. | Desconoce el apetito o es una frase genérica. | EV15 | Recepción · Evaluación · Descubrimiento |
| EN14 | ¿Cuáles son los tres escenarios que podrían afectar materialmente a la organización? | Comprensión de la materialidad. | Escenarios con impacto estimado y estado de preparación. | Respuestas técnicas o ninguna respuesta. | EV17 | Recepción · Evaluación · Descubrimiento |
| EN15 | ¿Cómo evalúa el directorio su propia supervisión de este riesgo? | Madurez de la supervisión. | Agenda anual, formación y seguimiento de pedidos. | El tema llega solo después de un incidente. | EV13 | Recepción · Evaluación · Descubrimiento |
| EN16 | ¿Participó el directorio o el comité ejecutivo en un ejercicio de crisis este año? | Preparación de quienes deciden. | Participación con decisiones registradas. | Nunca participó. | EV42 | Recepción · Evaluación · Descubrimiento |

### CFO / Finanzas (5)

| ID | Pregunta | Qué se busca entender | Señal positiva | Señal de alerta | Prácticas | Momento |
|---|---|---|---|---|---|---|
| EN17 | ¿Cómo se decide el presupuesto de seguridad y con qué información? | Trazabilidad de la inversión. | Decisión basada en escenarios y beneficio esperado. | Histórico más inflación o renovaciones. | EV04; EV27 | Recepción · Evaluación · Descubrimiento |
| EN18 | ¿Qué reducción de riesgo espera de la inversión de este año y cómo la medirá? | Medición del beneficio. | Indicador de beneficio acordado con el CISO. | No se espera nada medible. | EV04 | Recepción · Evaluación · Descubrimiento |
| EN19 | ¿Cuál sería el impacto financiero de un día sin operar el servicio más crítico? | Comprensión económica del riesgo. | Cifra estimada con supuestos compartidos con seguridad. | Nunca se estimó. | EV17 | Recepción · Evaluación · Descubrimiento |
| EN20 | ¿Qué cubre y qué excluye la póliza de seguro cibernético? | Transferencia de riesgo informada. | Conoce coberturas, exclusiones y requisitos. | Renovación automática sin revisión. | EV20 | Recepción · Evaluación · Descubrimiento |
| EN21 | ¿Qué riesgos de fraude de pagos o de proveedores ve vinculados a seguridad? | Riesgos financieros digitales. | Controles conjuntos con seguridad. | Lo ve como problema exclusivo de finanzas. | EV17; EV47 | Recepción · Evaluación · Descubrimiento |

### CIO / CTO (5)

| ID | Pregunta | Qué se busca entender | Señal positiva | Señal de alerta | Prácticas | Momento |
|---|---|---|---|---|---|---|
| EN22 | ¿Dónde colaboran bien seguridad y tecnología y dónde chocan? | Relación con tecnología. | Acuerdos de trabajo y escalamientos claros. | Conflicto crónico o seguridad subordinada a la operación. | EV33 | Recepción · Evaluación · Descubrimiento |
| EN23 | ¿Cómo se resuelve un conflicto entre el plazo de un proyecto y un requisito de seguridad? | Decisión de riesgo en proyectos. | Excepción o aceptación formal con dueño y vencimiento. | Se resuelve por jerarquía o se ignora el requisito. | EV08; EV19 | Recepción · Evaluación · Descubrimiento |
| EN24 | ¿Qué deuda tecnológica limita hoy la seguridad y qué plan existe? | Restricciones estructurales. | Inventario de deuda con plan y riesgo aceptado. | No hay plan; se acepta tácitamente. | EV34; EV31 | Recepción · Evaluación · Descubrimiento |
| EN25 | ¿Quién decide las excepciones a estándares de seguridad y cómo se vigilan? | Gobierno de excepciones. | Proceso con dueño, compensación y vencimiento. | Las decide el área que las pide. | EV08 | Recepción · Evaluación · Descubrimiento |
| EN26 | ¿Cómo se gobiernan las iniciativas de IA y los agentes que se están desplegando? | Gobierno de IA. | Inventario, evaluación previa y dueños humanos. | Cada área despliega lo que quiere. | EV48; EV32 | Recepción · Evaluación · Descubrimiento |

### CRO / Riesgos (5)

| ID | Pregunta | Qué se busca entender | Señal positiva | Señal de alerta | Prácticas | Momento |
|---|---|---|---|---|---|---|
| EN27 | ¿Cómo se integra el riesgo cibernético al mapa de riesgos de la empresa? | Integración con la gestión de riesgos. | Misma escala y método; revisión semestral. | Registro paralelo con otra escala. | EV14; EV13 | Recepción · Evaluación · Descubrimiento |
| EN28 | ¿Quién firma las aceptaciones de riesgo cibernético y con qué límites? | Autoridad de aceptación. | Niveles de autoridad según tamaño del riesgo. | Las firma el CISO o tecnología. | EV19 | Recepción · Evaluación · Descubrimiento |
| EN29 | ¿Cuántos riesgos cibernéticos están fuera del apetito y desde cuándo? | Seguimiento del residual. | Cifra conocida con planes y fechas. | No se puede responder. | EV16 | Recepción · Evaluación · Descubrimiento |
| EN30 | ¿Cómo se estiman la probabilidad y el impacto de los escenarios cibernéticos? | Calidad del análisis. | Supuestos explícitos, rangos y revisión. | Opiniones sin método. | EV17; EV18 | Recepción · Evaluación · Descubrimiento |
| EN31 | ¿Cómo se evalúan la concentración y las dependencias de terceros críticos? | Riesgo de terceros. | Mapa de concentración con planes de salida. | No se evalúa. | EV47 | Recepción · Evaluación · Descubrimiento |

### Legal, cumplimiento y privacidad (6)

| ID | Pregunta | Qué se busca entender | Señal positiva | Señal de alerta | Prácticas | Momento |
|---|---|---|---|---|---|---|
| EN32 | ¿Qué obligaciones de notificación aplican y quién decide notificar? | Preparación legal ante incidentes. | Plazos conocidos, plantillas y cadena de decisión. | Se definiría durante el incidente. | EV09; EV44 | Recepción · Evaluación · Descubrimiento |
| EN33 | ¿Qué requisitos contractuales de seguridad son los más exigentes? | Compromisos con clientes y socios. | Matriz de requisitos y verificación. | No se conocen hasta que el cliente audita. | EV10 | Recepción · Evaluación · Descubrimiento |
| EN34 | ¿Cómo se evalúan los tratamientos de datos personales de alto riesgo, incluidos los de IA? | Privacidad y protección de datos. | Evaluaciones de impacto con controles acordados. | No se evalúan o se hacen después. | EV30 | Recepción · Evaluación · Descubrimiento |
| EN35 | ¿Qué cambios regulatorios afectarán a la organización el próximo año? | Anticipación regulatoria. | Calendario con análisis de impacto. | Se reacciona cuando el regulador pregunta. | EV09 | Recepción · Evaluación · Descubrimiento |
| EN36 | ¿Cómo se preserva la evidencia y el privilegio legal en una investigación? | Investigación y forense. | Procedimiento acordado con legal. | No hay procedimiento. | EV43 | Recepción · Evaluación · Descubrimiento |
| EN56 | ¿El CISO y el equipo de seguridad tienen declaraciones de conflictos de interés vigentes y reglas escritas de confidencialidad para investigaciones y accesos privilegiados? | Conducta profesional y debida diligencia de la función de seguridad. | Declaraciones anuales vigentes, reglas aprobadas y casos resueltos con transparencia. | Relaciones con proveedores no declaradas; investigaciones o accesos privilegiados sin reglas ni registro. | EV24 | Evaluación · Descubrimiento |

### Auditoría interna (5)

| ID | Pregunta | Qué se busca entender | Señal positiva | Señal de alerta | Prácticas | Momento |
|---|---|---|---|---|---|---|
| EN37 | ¿Qué hallazgos de seguridad se repiten y qué dicen de la causa raíz? | Patrones de falla. | Análisis de causa raíz con acciones estructurales. | Los mismos hallazgos cada año. | EV12 | Recepción · Evaluación · Descubrimiento |
| EN38 | ¿Confía en la evidencia que presenta seguridad? ¿Por qué? | Calidad de la evidencia. | Evidencia continua, trazable y anterior a la auditoría. | Evidencia preparada para la ocasión. | EV11 | Recepción · Evaluación · Descubrimiento |
| EN39 | ¿Cómo se coordina el plan de auditoría con la función de seguridad? | Aseguramiento coordinado. | Plan anual acordado sobre las áreas de mayor riesgo. | Auditoría sorpresa sin coordinación ni prioridad. | EV12 | Recepción · Evaluación · Descubrimiento |
| EN40 | ¿Qué controles clave nunca se probaron? | Brechas de aseguramiento. | Lista conocida con plan de prueba. | No se sabe. | EV36 | Recepción · Evaluación · Descubrimiento |
| EN41 | ¿Cómo distingue un control configurado de uno efectivo? | Criterio de efectividad. | Pruebas de diseño y operación con muestra. | Se considera efectivo lo configurado. | EV35; EV36 | Recepción · Evaluación · Descubrimiento |

### Dueños de negocio y procesos (5)

| ID | Pregunta | Qué se busca entender | Señal positiva | Señal de alerta | Prácticas | Momento |
|---|---|---|---|---|---|---|
| EN42 | ¿Qué proceso nunca puede detenerse y cuánto tiempo toleraría sin él? | Criticidad y tolerancia. | Respuesta concreta, alineada con el BIA. | Nunca se lo preguntaron. | EV02; EV46 | Recepción · Evaluación · Descubrimiento |
| EN43 | ¿Sabe que es dueño de los riesgos cibernéticos de su proceso? ¿Qué decidió? | Dueños de riesgo en el negocio. | Conoce su rol y ejemplos de decisiones. | Cree que es un tema de tecnología. | EV14 | Recepción · Evaluación · Descubrimiento |
| EN44 | ¿Qué le pide seguridad que no entiende o no puede cumplir? | Aplicabilidad de políticas. | Pocas fricciones, con canal para resolverlas. | Reglas imposibles que se esquivan. | EV07 | Recepción · Evaluación · Descubrimiento |
| EN45 | ¿Cuánto tarda seguridad en habilitar una iniciativa suya? | Habilitación segura. | Plazos conocidos y razonables. | Seguridad aparece al final y frena. | EV33 | Recepción · Evaluación · Descubrimiento |
| EN46 | ¿Qué usos de IA tiene su equipo y quién los aprobó? | IA en el negocio. | Usos inventariados y aprobados. | IA gratuita sin control con datos de clientes. | EV48 | Recepción · Evaluación · Descubrimiento |

### RR. HH. (4)

| ID | Pregunta | Qué se busca entender | Señal positiva | Señal de alerta | Prácticas | Momento |
|---|---|---|---|---|---|---|
| EN47 | ¿Qué roles de seguridad son más difíciles de cubrir o retener? | Talento crítico. | Plan de retención y sucesión. | Rotación alta sin plan. | EV28 | Recepción · Evaluación · Descubrimiento |
| EN48 | ¿Los ejecutivos tienen objetivos de ciberseguridad en su evaluación? | Incentivos y responsabilidad distribuida. | Objetivos concretos en la evaluación de ejecutivos clave. | Solo el CISO tiene objetivos de seguridad. | EV14; EV24 | Recepción · Evaluación · Descubrimiento |
| EN49 | ¿Cómo participan seguridad y RR. HH. en altas, cambios y bajas de personas? | Ciclo de vida de identidades. | Proceso integrado con plazos medidos. | Bajas que tardan semanas en reflejarse en los accesos. | EV31 | Recepción · Evaluación · Descubrimiento |
| EN50 | ¿Qué conductas seguras se reconocen y cómo se tratan los errores honestos? | Cultura justa. | Reconocimiento y aprendizaje sin culpa para errores honestos. | Sanciones que desalientan el reporte. | EV02 | Recepción · Evaluación · Descubrimiento |

### Equipo de seguridad (5)

| ID | Pregunta | Qué se busca entender | Señal positiva | Señal de alerta | Prácticas | Momento |
|---|---|---|---|---|---|---|
| EN51 | Describa una semana típica: ¿qué tareas consumen tiempo sin reducir riesgos importantes? | Foco y carga del equipo. | Identifica tareas a eliminar o automatizar. | Todo es urgente; no hay tiempo para mejorar. | EV50; EV28 | Recepción · Evaluación · Descubrimiento |
| EN52 | ¿Qué funciona bien y no debería cambiar? | Prácticas a preservar. | Prácticas concretas con evidencia. | Nada funciona o todo funciona. | EV25 | Recepción · Evaluación · Descubrimiento |
| EN53 | ¿Qué obstáculo concreto eliminaría primero si pudiera? | Restricciones operativas. | Obstáculo específico con impacto conocido. | Respuestas genéricas sobre presupuesto. | EV28 | Recepción · Evaluación · Descubrimiento |
| EN54 | ¿Qué riesgo cree que la dirección subestima? | Señales desde la operación. | Riesgo concreto con argumentos. | Miedo a responder. | EV17 | Recepción · Evaluación · Descubrimiento |
| EN55 | ¿Cómo se entera de las prioridades y de por qué se eligieron? | Comunicación de la estrategia. | Conoce las prioridades y su razón. | Se entera por rumores. | EV03 | Recepción · Evaluación · Descubrimiento |

## 8. De las brechas a los servicios

Cada práctica apunta a un servicio sugerido. El libro cuenta las prácticas con brecha igual o mayor al umbral y recomienda servicios; los indicadores que mueve cada servicio permiten medir su efecto. La columna de referencias de apoyo de Microsoft del libro es de uso interno del asesor y se retira antes de compartir con el cliente.

| ID | Servicio | Objetivo | Entregables | Duración orientativa | Fases | Indicadores que mueve |
|---|---|---|---|---|---|---|
| S01 | Diagnóstico de recepción y mandato | Acta de recepción independiente, mandato y agenda de escucha para un CISO entrante o un cambio de gestión. | Acta de recepción; minuta de mandato; mapa de interesados; urgencias. | 2–4 semanas | F0–F1 | K14; KSG03 |
| S02 | Diagnóstico base (línea base) | Perfil actual con marco elegido, servicios y activos críticos, obligaciones, capacidades y terceros. | Perfil actual NIST CSF 2.0; catálogo de servicios críticos; diagnóstico consolidado. | 4–6 semanas | F2 | K22; K39; KSG04 |
| S03 | Evaluación independiente de madurez y de efectividad de controles | Validación externa de la madurez y prueba de controles clave; coordinación de pruebas de penetración. | Informe de madurez validado; pruebas de controles; plan de remediación. | 4–8 semanas | F2 · F5 · F6 | K60; K22; KSG05 |
| S04 | Diseño del modelo de gobierno | Carta de la función, comité y foros, derechos de decisión, dueños de riesgo, políticas y excepciones. | Carta; mandatos de comité; RACI; catálogo de políticas; proceso de excepciones. | 4–8 semanas | F3–F4 | K14; K09; K63; KSG02; KSG03 |
| S05 | Estrategia y hoja de ruta | Estrategia en una página, prioridades y hoja de ruta de 12 a 24 meses con gestión de portafolio. | Estrategia; hoja de ruta; tablero de portafolio. | 4–6 semanas | F3 | K17; K18; KSG01 |
| S06 | Cuantificación del riesgo y caso de negocio | Escenarios con pérdida esperada, costo de interrupción, caso de negocio y revisión del seguro. | Catálogo cuantificado; caso de negocio; revisión de póliza. | 3–6 semanas | F2–F4 | K26; K17; K19 |
| S07 | Cumplimiento y aseguramiento continuo | Inventario de obligaciones, mapa obligación–control–evidencia, notificaciones y relación con reguladores. | Inventario; matriz de evidencias; plantillas de notificación. | 4–8 semanas | F2 · F4 | K57; K59; K61 |
| S08 | Taller de apetito y proceso de aceptación de riesgo | Talleres con la dirección para fijar apetito y tolerancias; proceso de aceptación con niveles de autoridad. | Declaración de apetito; procedimiento de aceptación. | 2–4 semanas | F3–F4 | K25; K04 |
| S09 | Tablero y reporte al directorio | Indicadores de negocio, formato de reporte, ensayo y plantilla de informe anual. | Tablero v1; formato de reporte; informe anual. | 3–6 semanas | F3–F4 · F6 | K58; K14; KSG04; KSG06 |
| S10 | Preparación y ejercicios de crisis | Plan de respuesta, playbooks, ejercicio técnico, crisis ejecutiva y revisiones posteriores. | Plan y playbooks; informes de ejercicios; acciones. | 3–6 semanas por ciclo | F3–F5 | K15; K32; K05 |
| S11 | Diseño organizacional y desarrollo del equipo | Estructura, roles, capacidades, sucesión y modelo interno o tercerizado. | Organigrama; mapa de capacidades; plan de desarrollo. | 4–8 semanas | F2 · F4 | K12; K16 |
| S12 | Mentoría y desarrollo del CISO | Juicio, modelos mentales, sesgos y comunicación ejecutiva; acompañamiento con el programa TheNextCISO GM-24. | Plan personal; sesiones mensuales; diario de decisiones. | Continua (mensual) | F0–F6 | K01; K03; K02 |
| S13 | Gobierno y seguridad de IA y agentes | Inventario, política, evaluación previa de casos, identidad y autoridad de agentes, datos para IA y pruebas. | Inventario; política; procedimiento de evaluación; pruebas. | 4–8 semanas | F2–F5 | K49; K50; K51 |
| S14 | Arquitectura de seguridad y Zero Trust | Arquitectura objetivo, identidad, segmentación y configuración segura. | Arquitectura objetivo; estándares; hoja de ruta técnica. | 6–12 semanas | F4–F5 | K33; K34; K36; K35 |
| S15 | Optimización de operaciones de seguridad | Cobertura de detección, validación de técnicas, gestión de exposición y gobierno del proveedor de SOC. | Diagnóstico y plan de operaciones; acuerdos de nivel de servicio por resultados. | 6–12 semanas | F4–F5 | K41; K42; K45; K46 |
| S16 | Resiliencia y recuperación | BIA, RTO y RPO, respaldos inmutables, pruebas de recuperación y operación degradada. | BIA; plan y resultados de pruebas. | 4–8 semanas | F4–F5 | K30; K28; K21 |
| S17 | Programa de terceros y cadena de suministro | Clasificación, evaluación, cláusulas, concentración y foro de terceros. | Programa de terceros; evaluaciones; cláusulas. | 4–8 semanas | F4–F5 | K31; K27; K62 |
| S18 | Acompañamiento estratégico de 12 meses | Asesoría y co-gobierno a lo largo del modelo completo, con revisión formal trimestral con el sponsor. | Todos los hitos del modelo; revisiones trimestrales. | 12 meses | F0–F6 | Todos; KSG01; KSG06 |

## 9. Estructura del informe de evaluación

1. Alcance, interlocutores, evidencia revisada y limitaciones.
2. Resultado general: nivel de evidencia (KSG05), prácticas críticas en nivel 0 y cumplimiento de lo esperado por hito.
3. Resultados por línea de trabajo (gobierno, gestión y juicio del CISO).
4. Fortalezas que conviene preservar.
5. Diez brechas prioritarias, con riesgo asociado.
6. Plan de mejora: acciones, responsables, fechas e indicadores.
7. Servicios sugeridos y secuencia.
8. Próxima evaluación y criterio de comparación.

---
@SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre de 2026 · Propuesta sujeta a validación y a ajustes por organización.

# TheNextCISO GM-24 — Ideas centrales para ensayos, lote 06

**Conceptos 151–180 · Pilar Gestión de la Ciberseguridad**

**Unidades:** M2.2, M3.1, M3.2

**Estado:** ideas centrales propuestas para futuros ensayos; no representan nodos aprobados del Atlas ni ensayos completos.

## Criterio editorial

Cada concepto mantiene el nombre y la secuencia curricular GM-24. El desarrollo argumental es original y diferencia decisiones de Gobierno de ejecución, operación y evidencia de Gestión. Los códigos curriculares no son identificadores permanentes `ESS-######`; éstos requieren reserva autoritativa en SQLite.

## M2.2 — Gestión de Identidad y Acceso (IAM) y Principios de Confianza Cero

### 151. M2.2-K01 — Estrategias IAM

**Unidad:** M2.2 · **Palabras:** 410 · **Estado:** idea central propuesta.

**Tesis central.** IAM debe conectar identidades humanas y no humanas, recursos y autorizaciones con responsabilidades y riesgos del negocio. En el contexto del Programa Ejecutivo TheNextCISO, «Estrategias IAM» no debe abordarse como una etiqueta de producto ni como una lista de pasos aislados. El ensayo debe explicar qué capacidad necesita desarrollar quien lidera la seguridad, cuál es su propósito empresarial y qué relación mantiene con el riesgo. Es esencial distinguir el mandato de gobierno —apetito, prioridades, responsabilidades y autoridad— de la gestión que diseña, opera y verifica la práctica. Esta distinción permite analizar decisiones sin atribuir automáticamente al CISO la ejecución de cada control.

**Problema y controversia.** El escenario que conviene examinar es el siguiente: una empresa integra aplicaciones heredadas y agentes con permisos persistentes. El lector debe reconocer que una solución aparentemente correcta puede introducir nuevos riesgos, costos o dependencias. La discusión debe explorar al menos dos alternativas y sus efectos sobre personas, procesos, datos, tecnología y terceros. También debe separar hechos de hipótesis, controles configurados de controles probados, y señales de alerta de incidentes confirmados. Cuando intervengan agentes de IA, se analizarán permisos, límites de autonomía, supervisión y trazabilidad, sin convertir la automatización en sustituto del juicio responsable.

**Aplicación formativa.** El participante trabajará un caso realista y elaborará mapa de identidades, owners y prioridades de modernización. Tendrá que definir el alcance, identificar activos y procesos afectados, documentar supuestos, asignar responsables y describir condiciones de entrada, éxito y reversión. La propuesta debe poder explicarse tanto a especialistas técnicos como a responsables de negocio. Para evitar soluciones decorativas, deberá incluir una prueba, simulación o procedimiento de revisión que permita observar resultados. Cuando el riesgo residual exceda los límites autorizados, se exigirá escalamiento a la autoridad correspondiente y registro de la decisión.

**Resultado esperado y evaluación.** El ensayo debe concluir con una recomendación ejecutable, sus dependencias, una explicación de por qué se eligió y qué evidencia podría refutarla. La evaluación del aprendizaje considerará precisión conceptual, razonamiento causal, viabilidad, evidencia, límites y comunicación. La relación con las otras unidades de GM-24 debe hacerse explícita: la estrategia y el gobierno del riesgo condicionan la arquitectura; la operación produce observaciones; la respuesta y la recuperación aportan lecciones para revisar el programa. El valor de «Estrategias IAM» se demuestra cuando mejora una decisión y una capacidad verificable, no cuando aumenta la cantidad de documentos, herramientas o reuniones. La pregunta abierta es qué cambiaría la recomendación ante un incidente, un nuevo requisito o una dependencia inesperada.

**Pregunta generadora:** ¿Qué decisión y qué evidencia demostrarían la utilidad de «Estrategias IAM» en una organización concreta?

---

### 152. M2.2-K02 — Autenticación

**Unidad:** M2.2 · **Palabras:** 418 · **Estado:** idea central propuesta.

**Tesis central.** La autenticación establece evidencia de identidad y nivel de confianza adecuado a la operación, sin garantizar por sí misma que una acción esté autorizada. En el contexto del Programa Ejecutivo TheNextCISO, «Autenticación» no debe abordarse como una etiqueta de producto ni como una lista de pasos aislados. El ensayo debe explicar qué capacidad necesita desarrollar quien lidera la seguridad, cuál es su propósito empresarial y qué relación mantiene con el riesgo. Es esencial distinguir el mandato de gobierno —apetito, prioridades, responsabilidades y autoridad— de la gestión que diseña, opera y verifica la práctica. Esta distinción permite analizar decisiones sin atribuir automáticamente al CISO la ejecución de cada control.

**Problema y controversia.** El escenario que conviene examinar es el siguiente: una autenticación resistente al phishing convive con sesiones robadas y excepciones de emergencia. El lector debe reconocer que una solución aparentemente correcta puede introducir nuevos riesgos, costos o dependencias. La discusión debe explorar al menos dos alternativas y sus efectos sobre personas, procesos, datos, tecnología y terceros. También debe separar hechos de hipótesis, controles configurados de controles probados, y señales de alerta de incidentes confirmados. Cuando intervengan agentes de IA, se analizarán permisos, límites de autonomía, supervisión y trazabilidad, sin convertir la automatización en sustituto del juicio responsable.

**Aplicación formativa.** El participante trabajará un caso realista y elaborará diseño de autenticación con amenazas, métodos y pruebas. Tendrá que definir el alcance, identificar activos y procesos afectados, documentar supuestos, asignar responsables y describir condiciones de entrada, éxito y reversión. La propuesta debe poder explicarse tanto a especialistas técnicos como a responsables de negocio. Para evitar soluciones decorativas, deberá incluir una prueba, simulación o procedimiento de revisión que permita observar resultados. Cuando el riesgo residual exceda los límites autorizados, se exigirá escalamiento a la autoridad correspondiente y registro de la decisión.

**Resultado esperado y evaluación.** El ensayo debe concluir con una recomendación ejecutable, sus dependencias, una explicación de por qué se eligió y qué evidencia podría refutarla. La evaluación del aprendizaje considerará precisión conceptual, razonamiento causal, viabilidad, evidencia, límites y comunicación. La relación con las otras unidades de GM-24 debe hacerse explícita: la estrategia y el gobierno del riesgo condicionan la arquitectura; la operación produce observaciones; la respuesta y la recuperación aportan lecciones para revisar el programa. El valor de «Autenticación» se demuestra cuando mejora una decisión y una capacidad verificable, no cuando aumenta la cantidad de documentos, herramientas o reuniones. La pregunta abierta es qué cambiaría la recomendación ante un incidente, un nuevo requisito o una dependencia inesperada.

**Pregunta generadora:** ¿Qué decisión y qué evidencia demostrarían la utilidad de «Autenticación» en una organización concreta?

---

### 153. M2.2-K03 — Autorización

**Unidad:** M2.2 · **Palabras:** 416 · **Estado:** idea central propuesta.

**Tesis central.** La autorización limita acciones y recursos conforme a propósito, contexto y mínimo privilegio, y debe revisarse a lo largo del ciclo de vida. En el contexto del Programa Ejecutivo TheNextCISO, «Autorización» no debe abordarse como una etiqueta de producto ni como una lista de pasos aislados. El ensayo debe explicar qué capacidad necesita desarrollar quien lidera la seguridad, cuál es su propósito empresarial y qué relación mantiene con el riesgo. Es esencial distinguir el mandato de gobierno —apetito, prioridades, responsabilidades y autoridad— de la gestión que diseña, opera y verifica la práctica. Esta distinción permite analizar decisiones sin atribuir automáticamente al CISO la ejecución de cada control.

**Problema y controversia.** El escenario que conviene examinar es el siguiente: un agente autenticado invoca una herramienta con facultades mayores que las delegadas. El lector debe reconocer que una solución aparentemente correcta puede introducir nuevos riesgos, costos o dependencias. La discusión debe explorar al menos dos alternativas y sus efectos sobre personas, procesos, datos, tecnología y terceros. También debe separar hechos de hipótesis, controles configurados de controles probados, y señales de alerta de incidentes confirmados. Cuando intervengan agentes de IA, se analizarán permisos, límites de autonomía, supervisión y trazabilidad, sin convertir la automatización en sustituto del juicio responsable.

**Aplicación formativa.** El participante trabajará un caso realista y elaborará modelo de permisos, políticas y pruebas de abuso. Tendrá que definir el alcance, identificar activos y procesos afectados, documentar supuestos, asignar responsables y describir condiciones de entrada, éxito y reversión. La propuesta debe poder explicarse tanto a especialistas técnicos como a responsables de negocio. Para evitar soluciones decorativas, deberá incluir una prueba, simulación o procedimiento de revisión que permita observar resultados. Cuando el riesgo residual exceda los límites autorizados, se exigirá escalamiento a la autoridad correspondiente y registro de la decisión.

**Resultado esperado y evaluación.** El ensayo debe concluir con una recomendación ejecutable, sus dependencias, una explicación de por qué se eligió y qué evidencia podría refutarla. La evaluación del aprendizaje considerará precisión conceptual, razonamiento causal, viabilidad, evidencia, límites y comunicación. La relación con las otras unidades de GM-24 debe hacerse explícita: la estrategia y el gobierno del riesgo condicionan la arquitectura; la operación produce observaciones; la respuesta y la recuperación aportan lecciones para revisar el programa. El valor de «Autorización» se demuestra cuando mejora una decisión y una capacidad verificable, no cuando aumenta la cantidad de documentos, herramientas o reuniones. La pregunta abierta es qué cambiaría la recomendación ante un incidente, un nuevo requisito o una dependencia inesperada.

**Pregunta generadora:** ¿Qué decisión y qué evidencia demostrarían la utilidad de «Autorización» en una organización concreta?

---

### 154. M2.2-K04 — PAM (Privilegiados)

**Unidad:** M2.2 · **Palabras:** 404 · **Estado:** idea central propuesta.

**Tesis central.** La gestión de accesos privilegiados reduce exposición al limitar, registrar y supervisar elevaciones administrativas. En el contexto del Programa Ejecutivo TheNextCISO, «PAM (Privilegiados)» no debe abordarse como una etiqueta de producto ni como una lista de pasos aislados. El ensayo debe explicar qué capacidad necesita desarrollar quien lidera la seguridad, cuál es su propósito empresarial y qué relación mantiene con el riesgo. Es esencial distinguir el mandato de gobierno —apetito, prioridades, responsabilidades y autoridad— de la gestión que diseña, opera y verifica la práctica. Esta distinción permite analizar decisiones sin atribuir automáticamente al CISO la ejecución de cada control.

**Problema y controversia.** El escenario que conviene examinar es el siguiente: administradores conservan privilegios permanentes por razones de continuidad. El lector debe reconocer que una solución aparentemente correcta puede introducir nuevos riesgos, costos o dependencias. La discusión debe explorar al menos dos alternativas y sus efectos sobre personas, procesos, datos, tecnología y terceros. También debe separar hechos de hipótesis, controles configurados de controles probados, y señales de alerta de incidentes confirmados. Cuando intervengan agentes de IA, se analizarán permisos, límites de autonomía, supervisión y trazabilidad, sin convertir la automatización en sustituto del juicio responsable.

**Aplicación formativa.** El participante trabajará un caso realista y elaborará plan de elevación temporal, emergencia y revisión. Tendrá que definir el alcance, identificar activos y procesos afectados, documentar supuestos, asignar responsables y describir condiciones de entrada, éxito y reversión. La propuesta debe poder explicarse tanto a especialistas técnicos como a responsables de negocio. Para evitar soluciones decorativas, deberá incluir una prueba, simulación o procedimiento de revisión que permita observar resultados. Cuando el riesgo residual exceda los límites autorizados, se exigirá escalamiento a la autoridad correspondiente y registro de la decisión.

**Resultado esperado y evaluación.** El ensayo debe concluir con una recomendación ejecutable, sus dependencias, una explicación de por qué se eligió y qué evidencia podría refutarla. La evaluación del aprendizaje considerará precisión conceptual, razonamiento causal, viabilidad, evidencia, límites y comunicación. La relación con las otras unidades de GM-24 debe hacerse explícita: la estrategia y el gobierno del riesgo condicionan la arquitectura; la operación produce observaciones; la respuesta y la recuperación aportan lecciones para revisar el programa. El valor de «PAM (Privilegiados)» se demuestra cuando mejora una decisión y una capacidad verificable, no cuando aumenta la cantidad de documentos, herramientas o reuniones. La pregunta abierta es qué cambiaría la recomendación ante un incidente, un nuevo requisito o una dependencia inesperada.

**Pregunta generadora:** ¿Qué decisión y qué evidencia demostrarían la utilidad de «PAM (Privilegiados)» en una organización concreta?

---

### 155. M2.2-K05 — Zero Trust

**Unidad:** M2.2 · **Palabras:** 413 · **Estado:** idea central propuesta.

**Tesis central.** Zero Trust requiere verificar explícitamente, usar mínimo privilegio y asumir compromiso, articulando identidad, dispositivos, redes, aplicaciones y datos. En el contexto del Programa Ejecutivo TheNextCISO, «Zero Trust» no debe abordarse como una etiqueta de producto ni como una lista de pasos aislados. El ensayo debe explicar qué capacidad necesita desarrollar quien lidera la seguridad, cuál es su propósito empresarial y qué relación mantiene con el riesgo. Es esencial distinguir el mandato de gobierno —apetito, prioridades, responsabilidades y autoridad— de la gestión que diseña, opera y verifica la práctica. Esta distinción permite analizar decisiones sin atribuir automáticamente al CISO la ejecución de cada control.

**Problema y controversia.** El escenario que conviene examinar es el siguiente: la organización confunde Zero Trust con comprar una solución de acceso. El lector debe reconocer que una solución aparentemente correcta puede introducir nuevos riesgos, costos o dependencias. La discusión debe explorar al menos dos alternativas y sus efectos sobre personas, procesos, datos, tecnología y terceros. También debe separar hechos de hipótesis, controles configurados de controles probados, y señales de alerta de incidentes confirmados. Cuando intervengan agentes de IA, se analizarán permisos, límites de autonomía, supervisión y trazabilidad, sin convertir la automatización en sustituto del juicio responsable.

**Aplicación formativa.** El participante trabajará un caso realista y elaborará arquitectura de decisiones de acceso y métricas de cobertura. Tendrá que definir el alcance, identificar activos y procesos afectados, documentar supuestos, asignar responsables y describir condiciones de entrada, éxito y reversión. La propuesta debe poder explicarse tanto a especialistas técnicos como a responsables de negocio. Para evitar soluciones decorativas, deberá incluir una prueba, simulación o procedimiento de revisión que permita observar resultados. Cuando el riesgo residual exceda los límites autorizados, se exigirá escalamiento a la autoridad correspondiente y registro de la decisión.

**Resultado esperado y evaluación.** El ensayo debe concluir con una recomendación ejecutable, sus dependencias, una explicación de por qué se eligió y qué evidencia podría refutarla. La evaluación del aprendizaje considerará precisión conceptual, razonamiento causal, viabilidad, evidencia, límites y comunicación. La relación con las otras unidades de GM-24 debe hacerse explícita: la estrategia y el gobierno del riesgo condicionan la arquitectura; la operación produce observaciones; la respuesta y la recuperación aportan lecciones para revisar el programa. El valor de «Zero Trust» se demuestra cuando mejora una decisión y una capacidad verificable, no cuando aumenta la cantidad de documentos, herramientas o reuniones. La pregunta abierta es qué cambiaría la recomendación ante un incidente, un nuevo requisito o una dependencia inesperada.

**Pregunta generadora:** ¿Qué decisión y qué evidencia demostrarían la utilidad de «Zero Trust» en una organización concreta?

---

### 156. M2.2-K06 — ZTNA

**Unidad:** M2.2 · **Palabras:** 411 · **Estado:** idea central propuesta.

**Tesis central.** ZTNA restringe acceso a aplicaciones privadas por identidad, contexto y política, sin asumir confianza por ubicación de red. En el contexto del Programa Ejecutivo TheNextCISO, «ZTNA» no debe abordarse como una etiqueta de producto ni como una lista de pasos aislados. El ensayo debe explicar qué capacidad necesita desarrollar quien lidera la seguridad, cuál es su propósito empresarial y qué relación mantiene con el riesgo. Es esencial distinguir el mandato de gobierno —apetito, prioridades, responsabilidades y autoridad— de la gestión que diseña, opera y verifica la práctica. Esta distinción permite analizar decisiones sin atribuir automáticamente al CISO la ejecución de cada control.

**Problema y controversia.** El escenario que conviene examinar es el siguiente: una VPN concede acceso amplio a servicios internos no relacionados con el trabajo. El lector debe reconocer que una solución aparentemente correcta puede introducir nuevos riesgos, costos o dependencias. La discusión debe explorar al menos dos alternativas y sus efectos sobre personas, procesos, datos, tecnología y terceros. También debe separar hechos de hipótesis, controles configurados de controles probados, y señales de alerta de incidentes confirmados. Cuando intervengan agentes de IA, se analizarán permisos, límites de autonomía, supervisión y trazabilidad, sin convertir la automatización en sustituto del juicio responsable.

**Aplicación formativa.** El participante trabajará un caso realista y elaborará diseño de segmentación lógica, políticas y fallback. Tendrá que definir el alcance, identificar activos y procesos afectados, documentar supuestos, asignar responsables y describir condiciones de entrada, éxito y reversión. La propuesta debe poder explicarse tanto a especialistas técnicos como a responsables de negocio. Para evitar soluciones decorativas, deberá incluir una prueba, simulación o procedimiento de revisión que permita observar resultados. Cuando el riesgo residual exceda los límites autorizados, se exigirá escalamiento a la autoridad correspondiente y registro de la decisión.

**Resultado esperado y evaluación.** El ensayo debe concluir con una recomendación ejecutable, sus dependencias, una explicación de por qué se eligió y qué evidencia podría refutarla. La evaluación del aprendizaje considerará precisión conceptual, razonamiento causal, viabilidad, evidencia, límites y comunicación. La relación con las otras unidades de GM-24 debe hacerse explícita: la estrategia y el gobierno del riesgo condicionan la arquitectura; la operación produce observaciones; la respuesta y la recuperación aportan lecciones para revisar el programa. El valor de «ZTNA» se demuestra cuando mejora una decisión y una capacidad verificable, no cuando aumenta la cantidad de documentos, herramientas o reuniones. La pregunta abierta es qué cambiaría la recomendación ante un incidente, un nuevo requisito o una dependencia inesperada.

**Pregunta generadora:** ¿Qué decisión y qué evidencia demostrarían la utilidad de «ZTNA» en una organización concreta?

---

### 157. M2.2-K07 — Ciclo Vida Identidad

**Unidad:** M2.2 · **Palabras:** 414 · **Estado:** idea central propuesta.

**Tesis central.** El ciclo de vida de identidad gobierna creación, cambios, privilegios y baja de sujetos humanos, servicios y agentes. En el contexto del Programa Ejecutivo TheNextCISO, «Ciclo Vida Identidad» no debe abordarse como una etiqueta de producto ni como una lista de pasos aislados. El ensayo debe explicar qué capacidad necesita desarrollar quien lidera la seguridad, cuál es su propósito empresarial y qué relación mantiene con el riesgo. Es esencial distinguir el mandato de gobierno —apetito, prioridades, responsabilidades y autoridad— de la gestión que diseña, opera y verifica la práctica. Esta distinción permite analizar decisiones sin atribuir automáticamente al CISO la ejecución de cada control.

**Problema y controversia.** El escenario que conviene examinar es el siguiente: una identidad de servicio queda activa después del retiro de la aplicación. El lector debe reconocer que una solución aparentemente correcta puede introducir nuevos riesgos, costos o dependencias. La discusión debe explorar al menos dos alternativas y sus efectos sobre personas, procesos, datos, tecnología y terceros. También debe separar hechos de hipótesis, controles configurados de controles probados, y señales de alerta de incidentes confirmados. Cuando intervengan agentes de IA, se analizarán permisos, límites de autonomía, supervisión y trazabilidad, sin convertir la automatización en sustituto del juicio responsable.

**Aplicación formativa.** El participante trabajará un caso realista y elaborará workflow de alta, revisión, revocación y evidencia. Tendrá que definir el alcance, identificar activos y procesos afectados, documentar supuestos, asignar responsables y describir condiciones de entrada, éxito y reversión. La propuesta debe poder explicarse tanto a especialistas técnicos como a responsables de negocio. Para evitar soluciones decorativas, deberá incluir una prueba, simulación o procedimiento de revisión que permita observar resultados. Cuando el riesgo residual exceda los límites autorizados, se exigirá escalamiento a la autoridad correspondiente y registro de la decisión.

**Resultado esperado y evaluación.** El ensayo debe concluir con una recomendación ejecutable, sus dependencias, una explicación de por qué se eligió y qué evidencia podría refutarla. La evaluación del aprendizaje considerará precisión conceptual, razonamiento causal, viabilidad, evidencia, límites y comunicación. La relación con las otras unidades de GM-24 debe hacerse explícita: la estrategia y el gobierno del riesgo condicionan la arquitectura; la operación produce observaciones; la respuesta y la recuperación aportan lecciones para revisar el programa. El valor de «Ciclo Vida Identidad» se demuestra cuando mejora una decisión y una capacidad verificable, no cuando aumenta la cantidad de documentos, herramientas o reuniones. La pregunta abierta es qué cambiaría la recomendación ante un incidente, un nuevo requisito o una dependencia inesperada.

**Pregunta generadora:** ¿Qué decisión y qué evidencia demostrarían la utilidad de «Ciclo Vida Identidad» en una organización concreta?

---

### 158. M2.2-K08 — Auditoría IAM

**Unidad:** M2.2 · **Palabras:** 411 · **Estado:** idea central propuesta.

**Tesis central.** La auditoría de IAM evalúa autorizaciones, cambios, privilegios y controles de acceso con evidencia independiente y contextual. En el contexto del Programa Ejecutivo TheNextCISO, «Auditoría IAM» no debe abordarse como una etiqueta de producto ni como una lista de pasos aislados. El ensayo debe explicar qué capacidad necesita desarrollar quien lidera la seguridad, cuál es su propósito empresarial y qué relación mantiene con el riesgo. Es esencial distinguir el mandato de gobierno —apetito, prioridades, responsabilidades y autoridad— de la gestión que diseña, opera y verifica la práctica. Esta distinción permite analizar decisiones sin atribuir automáticamente al CISO la ejecución de cada control.

**Problema y controversia.** El escenario que conviene examinar es el siguiente: el inventario de cuentas parece correcto pero las autorizaciones efectivas difieren. El lector debe reconocer que una solución aparentemente correcta puede introducir nuevos riesgos, costos o dependencias. La discusión debe explorar al menos dos alternativas y sus efectos sobre personas, procesos, datos, tecnología y terceros. También debe separar hechos de hipótesis, controles configurados de controles probados, y señales de alerta de incidentes confirmados. Cuando intervengan agentes de IA, se analizarán permisos, límites de autonomía, supervisión y trazabilidad, sin convertir la automatización en sustituto del juicio responsable.

**Aplicación formativa.** El participante trabajará un caso realista y elaborará plan de pruebas de acceso, excepciones y hallazgos. Tendrá que definir el alcance, identificar activos y procesos afectados, documentar supuestos, asignar responsables y describir condiciones de entrada, éxito y reversión. La propuesta debe poder explicarse tanto a especialistas técnicos como a responsables de negocio. Para evitar soluciones decorativas, deberá incluir una prueba, simulación o procedimiento de revisión que permita observar resultados. Cuando el riesgo residual exceda los límites autorizados, se exigirá escalamiento a la autoridad correspondiente y registro de la decisión.

**Resultado esperado y evaluación.** El ensayo debe concluir con una recomendación ejecutable, sus dependencias, una explicación de por qué se eligió y qué evidencia podría refutarla. La evaluación del aprendizaje considerará precisión conceptual, razonamiento causal, viabilidad, evidencia, límites y comunicación. La relación con las otras unidades de GM-24 debe hacerse explícita: la estrategia y el gobierno del riesgo condicionan la arquitectura; la operación produce observaciones; la respuesta y la recuperación aportan lecciones para revisar el programa. El valor de «Auditoría IAM» se demuestra cuando mejora una decisión y una capacidad verificable, no cuando aumenta la cantidad de documentos, herramientas o reuniones. La pregunta abierta es qué cambiaría la recomendación ante un incidente, un nuevo requisito o una dependencia inesperada.

**Pregunta generadora:** ¿Qué decisión y qué evidencia demostrarían la utilidad de «Auditoría IAM» en una organización concreta?

---

### 159. M2.2-K09 — Federación

**Unidad:** M2.2 · **Palabras:** 409 · **Estado:** idea central propuesta.

**Tesis central.** La federación permite establecer confianza entre dominios de identidad con protocolos, acuerdos y límites de responsabilidad explícitos. En el contexto del Programa Ejecutivo TheNextCISO, «Federación» no debe abordarse como una etiqueta de producto ni como una lista de pasos aislados. El ensayo debe explicar qué capacidad necesita desarrollar quien lidera la seguridad, cuál es su propósito empresarial y qué relación mantiene con el riesgo. Es esencial distinguir el mandato de gobierno —apetito, prioridades, responsabilidades y autoridad— de la gestión que diseña, opera y verifica la práctica. Esta distinción permite analizar decisiones sin atribuir automáticamente al CISO la ejecución de cada control.

**Problema y controversia.** El escenario que conviene examinar es el siguiente: una aplicación externa acepta tokens sin validar audiencia o condiciones de emisión. El lector debe reconocer que una solución aparentemente correcta puede introducir nuevos riesgos, costos o dependencias. La discusión debe explorar al menos dos alternativas y sus efectos sobre personas, procesos, datos, tecnología y terceros. También debe separar hechos de hipótesis, controles configurados de controles probados, y señales de alerta de incidentes confirmados. Cuando intervengan agentes de IA, se analizarán permisos, límites de autonomía, supervisión y trazabilidad, sin convertir la automatización en sustituto del juicio responsable.

**Aplicación formativa.** El participante trabajará un caso realista y elaborará modelo de confianza, tokens, claves y responsabilidades. Tendrá que definir el alcance, identificar activos y procesos afectados, documentar supuestos, asignar responsables y describir condiciones de entrada, éxito y reversión. La propuesta debe poder explicarse tanto a especialistas técnicos como a responsables de negocio. Para evitar soluciones decorativas, deberá incluir una prueba, simulación o procedimiento de revisión que permita observar resultados. Cuando el riesgo residual exceda los límites autorizados, se exigirá escalamiento a la autoridad correspondiente y registro de la decisión.

**Resultado esperado y evaluación.** El ensayo debe concluir con una recomendación ejecutable, sus dependencias, una explicación de por qué se eligió y qué evidencia podría refutarla. La evaluación del aprendizaje considerará precisión conceptual, razonamiento causal, viabilidad, evidencia, límites y comunicación. La relación con las otras unidades de GM-24 debe hacerse explícita: la estrategia y el gobierno del riesgo condicionan la arquitectura; la operación produce observaciones; la respuesta y la recuperación aportan lecciones para revisar el programa. El valor de «Federación» se demuestra cuando mejora una decisión y una capacidad verificable, no cuando aumenta la cantidad de documentos, herramientas o reuniones. La pregunta abierta es qué cambiaría la recomendación ante un incidente, un nuevo requisito o una dependencia inesperada.

**Pregunta generadora:** ¿Qué decisión y qué evidencia demostrarían la utilidad de «Federación» en una organización concreta?

---

### 160. M2.2-K10 — Contexto de Acceso

**Unidad:** M2.2 · **Palabras:** 414 · **Estado:** idea central propuesta.

**Tesis central.** El contexto de acceso integra señales de identidad, dispositivo, ubicación, riesgo y operación para decidir políticas proporcionales. En el contexto del Programa Ejecutivo TheNextCISO, «Contexto de Acceso» no debe abordarse como una etiqueta de producto ni como una lista de pasos aislados. El ensayo debe explicar qué capacidad necesita desarrollar quien lidera la seguridad, cuál es su propósito empresarial y qué relación mantiene con el riesgo. Es esencial distinguir el mandato de gobierno —apetito, prioridades, responsabilidades y autoridad— de la gestión que diseña, opera y verifica la práctica. Esta distinción permite analizar decisiones sin atribuir automáticamente al CISO la ejecución de cada control.

**Problema y controversia.** El escenario que conviene examinar es el siguiente: una regla demasiado amplia bloquea procesos críticos o permite accesos de alto riesgo. El lector debe reconocer que una solución aparentemente correcta puede introducir nuevos riesgos, costos o dependencias. La discusión debe explorar al menos dos alternativas y sus efectos sobre personas, procesos, datos, tecnología y terceros. También debe separar hechos de hipótesis, controles configurados de controles probados, y señales de alerta de incidentes confirmados. Cuando intervengan agentes de IA, se analizarán permisos, límites de autonomía, supervisión y trazabilidad, sin convertir la automatización en sustituto del juicio responsable.

**Aplicación formativa.** El participante trabajará un caso realista y elaborará política adaptativa con pruebas de casos límite. Tendrá que definir el alcance, identificar activos y procesos afectados, documentar supuestos, asignar responsables y describir condiciones de entrada, éxito y reversión. La propuesta debe poder explicarse tanto a especialistas técnicos como a responsables de negocio. Para evitar soluciones decorativas, deberá incluir una prueba, simulación o procedimiento de revisión que permita observar resultados. Cuando el riesgo residual exceda los límites autorizados, se exigirá escalamiento a la autoridad correspondiente y registro de la decisión.

**Resultado esperado y evaluación.** El ensayo debe concluir con una recomendación ejecutable, sus dependencias, una explicación de por qué se eligió y qué evidencia podría refutarla. La evaluación del aprendizaje considerará precisión conceptual, razonamiento causal, viabilidad, evidencia, límites y comunicación. La relación con las otras unidades de GM-24 debe hacerse explícita: la estrategia y el gobierno del riesgo condicionan la arquitectura; la operación produce observaciones; la respuesta y la recuperación aportan lecciones para revisar el programa. El valor de «Contexto de Acceso» se demuestra cuando mejora una decisión y una capacidad verificable, no cuando aumenta la cantidad de documentos, herramientas o reuniones. La pregunta abierta es qué cambiaría la recomendación ante un incidente, un nuevo requisito o una dependencia inesperada.

**Pregunta generadora:** ¿Qué decisión y qué evidencia demostrarían la utilidad de «Contexto de Acceso» en una organización concreta?

---

## M3.1 — Arquitectura de Seguridad, Ingeniería y Diseño (Incl. Zero Trust)

### 161. M3.1-K01 — Arquitectura de Seguridad

**Unidad:** M3.1 · **Palabras:** 413 · **Estado:** idea central propuesta.

**Tesis central.** La arquitectura de seguridad organiza principios, patrones, componentes y decisiones para que los sistemas alcancen resultados verificables. En el contexto del Programa Ejecutivo TheNextCISO, «Arquitectura de Seguridad» no debe abordarse como una etiqueta de producto ni como una lista de pasos aislados. El ensayo debe explicar qué capacidad necesita desarrollar quien lidera la seguridad, cuál es su propósito empresarial y qué relación mantiene con el riesgo. Es esencial distinguir el mandato de gobierno —apetito, prioridades, responsabilidades y autoridad— de la gestión que diseña, opera y verifica la práctica. Esta distinción permite analizar decisiones sin atribuir automáticamente al CISO la ejecución de cada control.

**Problema y controversia.** El escenario que conviene examinar es el siguiente: cada proyecto incorpora controles incompatibles y sin modelo de confianza común. El lector debe reconocer que una solución aparentemente correcta puede introducir nuevos riesgos, costos o dependencias. La discusión debe explorar al menos dos alternativas y sus efectos sobre personas, procesos, datos, tecnología y terceros. También debe separar hechos de hipótesis, controles configurados de controles probados, y señales de alerta de incidentes confirmados. Cuando intervengan agentes de IA, se analizarán permisos, límites de autonomía, supervisión y trazabilidad, sin convertir la automatización en sustituto del juicio responsable.

**Aplicación formativa.** El participante trabajará un caso realista y elaborará vista de arquitectura con amenazas, controles y decisiones. Tendrá que definir el alcance, identificar activos y procesos afectados, documentar supuestos, asignar responsables y describir condiciones de entrada, éxito y reversión. La propuesta debe poder explicarse tanto a especialistas técnicos como a responsables de negocio. Para evitar soluciones decorativas, deberá incluir una prueba, simulación o procedimiento de revisión que permita observar resultados. Cuando el riesgo residual exceda los límites autorizados, se exigirá escalamiento a la autoridad correspondiente y registro de la decisión.

**Resultado esperado y evaluación.** El ensayo debe concluir con una recomendación ejecutable, sus dependencias, una explicación de por qué se eligió y qué evidencia podría refutarla. La evaluación del aprendizaje considerará precisión conceptual, razonamiento causal, viabilidad, evidencia, límites y comunicación. La relación con las otras unidades de GM-24 debe hacerse explícita: la estrategia y el gobierno del riesgo condicionan la arquitectura; la operación produce observaciones; la respuesta y la recuperación aportan lecciones para revisar el programa. El valor de «Arquitectura de Seguridad» se demuestra cuando mejora una decisión y una capacidad verificable, no cuando aumenta la cantidad de documentos, herramientas o reuniones. La pregunta abierta es qué cambiaría la recomendación ante un incidente, un nuevo requisito o una dependencia inesperada.

**Pregunta generadora:** ¿Qué decisión y qué evidencia demostrarían la utilidad de «Arquitectura de Seguridad» en una organización concreta?

---

### 162. M3.1-K02 — Ingeniería de Seguridad

**Unidad:** M3.1 · **Palabras:** 415 · **Estado:** idea central propuesta.

**Tesis central.** La ingeniería de seguridad traduce requisitos de riesgo en mecanismos implementables, medibles y sostenibles durante el ciclo de vida. En el contexto del Programa Ejecutivo TheNextCISO, «Ingeniería de Seguridad» no debe abordarse como una etiqueta de producto ni como una lista de pasos aislados. El ensayo debe explicar qué capacidad necesita desarrollar quien lidera la seguridad, cuál es su propósito empresarial y qué relación mantiene con el riesgo. Es esencial distinguir el mandato de gobierno —apetito, prioridades, responsabilidades y autoridad— de la gestión que diseña, opera y verifica la práctica. Esta distinción permite analizar decisiones sin atribuir automáticamente al CISO la ejecución de cada control.

**Problema y controversia.** El escenario que conviene examinar es el siguiente: los controles se diseñan sin capacidad de operación ni pruebas. El lector debe reconocer que una solución aparentemente correcta puede introducir nuevos riesgos, costos o dependencias. La discusión debe explorar al menos dos alternativas y sus efectos sobre personas, procesos, datos, tecnología y terceros. También debe separar hechos de hipótesis, controles configurados de controles probados, y señales de alerta de incidentes confirmados. Cuando intervengan agentes de IA, se analizarán permisos, límites de autonomía, supervisión y trazabilidad, sin convertir la automatización en sustituto del juicio responsable.

**Aplicación formativa.** El participante trabajará un caso realista y elaborará plan de ingeniería con criterios de aceptación y telemetría. Tendrá que definir el alcance, identificar activos y procesos afectados, documentar supuestos, asignar responsables y describir condiciones de entrada, éxito y reversión. La propuesta debe poder explicarse tanto a especialistas técnicos como a responsables de negocio. Para evitar soluciones decorativas, deberá incluir una prueba, simulación o procedimiento de revisión que permita observar resultados. Cuando el riesgo residual exceda los límites autorizados, se exigirá escalamiento a la autoridad correspondiente y registro de la decisión.

**Resultado esperado y evaluación.** El ensayo debe concluir con una recomendación ejecutable, sus dependencias, una explicación de por qué se eligió y qué evidencia podría refutarla. La evaluación del aprendizaje considerará precisión conceptual, razonamiento causal, viabilidad, evidencia, límites y comunicación. La relación con las otras unidades de GM-24 debe hacerse explícita: la estrategia y el gobierno del riesgo condicionan la arquitectura; la operación produce observaciones; la respuesta y la recuperación aportan lecciones para revisar el programa. El valor de «Ingeniería de Seguridad» se demuestra cuando mejora una decisión y una capacidad verificable, no cuando aumenta la cantidad de documentos, herramientas o reuniones. La pregunta abierta es qué cambiaría la recomendación ante un incidente, un nuevo requisito o una dependencia inesperada.

**Pregunta generadora:** ¿Qué decisión y qué evidencia demostrarían la utilidad de «Ingeniería de Seguridad» en una organización concreta?

---

### 163. M3.1-K03 — Zero Trust (Arquitectura)

**Unidad:** M3.1 · **Palabras:** 414 · **Estado:** idea central propuesta.

**Tesis central.** Zero Trust como arquitectura distribuye decisiones continuas de acceso y protección entre identidades, dispositivos, aplicaciones, redes y datos. En el contexto del Programa Ejecutivo TheNextCISO, «Zero Trust (Arquitectura)» no debe abordarse como una etiqueta de producto ni como una lista de pasos aislados. El ensayo debe explicar qué capacidad necesita desarrollar quien lidera la seguridad, cuál es su propósito empresarial y qué relación mantiene con el riesgo. Es esencial distinguir el mandato de gobierno —apetito, prioridades, responsabilidades y autoridad— de la gestión que diseña, opera y verifica la práctica. Esta distinción permite analizar decisiones sin atribuir automáticamente al CISO la ejecución de cada control.

**Problema y controversia.** El escenario que conviene examinar es el siguiente: una iniciativa solo reemplaza la VPN sin revisar autorizaciones ni protección de datos. El lector debe reconocer que una solución aparentemente correcta puede introducir nuevos riesgos, costos o dependencias. La discusión debe explorar al menos dos alternativas y sus efectos sobre personas, procesos, datos, tecnología y terceros. También debe separar hechos de hipótesis, controles configurados de controles probados, y señales de alerta de incidentes confirmados. Cuando intervengan agentes de IA, se analizarán permisos, límites de autonomía, supervisión y trazabilidad, sin convertir la automatización en sustituto del juicio responsable.

**Aplicación formativa.** El participante trabajará un caso realista y elaborará arquitectura objetivo con dependencias y fases. Tendrá que definir el alcance, identificar activos y procesos afectados, documentar supuestos, asignar responsables y describir condiciones de entrada, éxito y reversión. La propuesta debe poder explicarse tanto a especialistas técnicos como a responsables de negocio. Para evitar soluciones decorativas, deberá incluir una prueba, simulación o procedimiento de revisión que permita observar resultados. Cuando el riesgo residual exceda los límites autorizados, se exigirá escalamiento a la autoridad correspondiente y registro de la decisión.

**Resultado esperado y evaluación.** El ensayo debe concluir con una recomendación ejecutable, sus dependencias, una explicación de por qué se eligió y qué evidencia podría refutarla. La evaluación del aprendizaje considerará precisión conceptual, razonamiento causal, viabilidad, evidencia, límites y comunicación. La relación con las otras unidades de GM-24 debe hacerse explícita: la estrategia y el gobierno del riesgo condicionan la arquitectura; la operación produce observaciones; la respuesta y la recuperación aportan lecciones para revisar el programa. El valor de «Zero Trust (Arquitectura)» se demuestra cuando mejora una decisión y una capacidad verificable, no cuando aumenta la cantidad de documentos, herramientas o reuniones. La pregunta abierta es qué cambiaría la recomendación ante un incidente, un nuevo requisito o una dependencia inesperada.

**Pregunta generadora:** ¿Qué decisión y qué evidencia demostrarían la utilidad de «Zero Trust (Arquitectura)» en una organización concreta?

---

### 164. M3.1-K04 — Diseño Seguro (SbD)

**Unidad:** M3.1 · **Palabras:** 413 · **Estado:** idea central propuesta.

**Tesis central.** Secure by Design incorpora requisitos de seguridad desde decisiones iniciales de producto, evitando trasladar riesgos innecesarios a usuarios y operadores. En el contexto del Programa Ejecutivo TheNextCISO, «Diseño Seguro (SbD)» no debe abordarse como una etiqueta de producto ni como una lista de pasos aislados. El ensayo debe explicar qué capacidad necesita desarrollar quien lidera la seguridad, cuál es su propósito empresarial y qué relación mantiene con el riesgo. Es esencial distinguir el mandato de gobierno —apetito, prioridades, responsabilidades y autoridad— de la gestión que diseña, opera y verifica la práctica. Esta distinción permite analizar decisiones sin atribuir automáticamente al CISO la ejecución de cada control.

**Problema y controversia.** El escenario que conviene examinar es el siguiente: el equipo descubre amenazas críticas después del despliegue. El lector debe reconocer que una solución aparentemente correcta puede introducir nuevos riesgos, costos o dependencias. La discusión debe explorar al menos dos alternativas y sus efectos sobre personas, procesos, datos, tecnología y terceros. También debe separar hechos de hipótesis, controles configurados de controles probados, y señales de alerta de incidentes confirmados. Cuando intervengan agentes de IA, se analizarán permisos, límites de autonomía, supervisión y trazabilidad, sin convertir la automatización en sustituto del juicio responsable.

**Aplicación formativa.** El participante trabajará un caso realista y elaborará revisión de diseño con amenazas, mitigaciones y pruebas. Tendrá que definir el alcance, identificar activos y procesos afectados, documentar supuestos, asignar responsables y describir condiciones de entrada, éxito y reversión. La propuesta debe poder explicarse tanto a especialistas técnicos como a responsables de negocio. Para evitar soluciones decorativas, deberá incluir una prueba, simulación o procedimiento de revisión que permita observar resultados. Cuando el riesgo residual exceda los límites autorizados, se exigirá escalamiento a la autoridad correspondiente y registro de la decisión.

**Resultado esperado y evaluación.** El ensayo debe concluir con una recomendación ejecutable, sus dependencias, una explicación de por qué se eligió y qué evidencia podría refutarla. La evaluación del aprendizaje considerará precisión conceptual, razonamiento causal, viabilidad, evidencia, límites y comunicación. La relación con las otras unidades de GM-24 debe hacerse explícita: la estrategia y el gobierno del riesgo condicionan la arquitectura; la operación produce observaciones; la respuesta y la recuperación aportan lecciones para revisar el programa. El valor de «Diseño Seguro (SbD)» se demuestra cuando mejora una decisión y una capacidad verificable, no cuando aumenta la cantidad de documentos, herramientas o reuniones. La pregunta abierta es qué cambiaría la recomendación ante un incidente, un nuevo requisito o una dependencia inesperada.

**Pregunta generadora:** ¿Qué decisión y qué evidencia demostrarían la utilidad de «Diseño Seguro (SbD)» en una organización concreta?

---

### 165. M3.1-K05 — TOGAF y Seguridad

**Unidad:** M3.1 · **Palabras:** 414 · **Estado:** idea central propuesta.

**Tesis central.** TOGAF puede conectar arquitectura empresarial y seguridad al relacionar capacidades, procesos, datos, aplicaciones y tecnología con decisiones de gobierno. En el contexto del Programa Ejecutivo TheNextCISO, «TOGAF y Seguridad» no debe abordarse como una etiqueta de producto ni como una lista de pasos aislados. El ensayo debe explicar qué capacidad necesita desarrollar quien lidera la seguridad, cuál es su propósito empresarial y qué relación mantiene con el riesgo. Es esencial distinguir el mandato de gobierno —apetito, prioridades, responsabilidades y autoridad— de la gestión que diseña, opera y verifica la práctica. Esta distinción permite analizar decisiones sin atribuir automáticamente al CISO la ejecución de cada control.

**Problema y controversia.** El escenario que conviene examinar es el siguiente: la arquitectura se documenta como inventario de componentes sin resultados empresariales. El lector debe reconocer que una solución aparentemente correcta puede introducir nuevos riesgos, costos o dependencias. La discusión debe explorar al menos dos alternativas y sus efectos sobre personas, procesos, datos, tecnología y terceros. También debe separar hechos de hipótesis, controles configurados de controles probados, y señales de alerta de incidentes confirmados. Cuando intervengan agentes de IA, se analizarán permisos, límites de autonomía, supervisión y trazabilidad, sin convertir la automatización en sustituto del juicio responsable.

**Aplicación formativa.** El participante trabajará un caso realista y elaborará modelo de capacidades y controles con trazabilidad. Tendrá que definir el alcance, identificar activos y procesos afectados, documentar supuestos, asignar responsables y describir condiciones de entrada, éxito y reversión. La propuesta debe poder explicarse tanto a especialistas técnicos como a responsables de negocio. Para evitar soluciones decorativas, deberá incluir una prueba, simulación o procedimiento de revisión que permita observar resultados. Cuando el riesgo residual exceda los límites autorizados, se exigirá escalamiento a la autoridad correspondiente y registro de la decisión.

**Resultado esperado y evaluación.** El ensayo debe concluir con una recomendación ejecutable, sus dependencias, una explicación de por qué se eligió y qué evidencia podría refutarla. La evaluación del aprendizaje considerará precisión conceptual, razonamiento causal, viabilidad, evidencia, límites y comunicación. La relación con las otras unidades de GM-24 debe hacerse explícita: la estrategia y el gobierno del riesgo condicionan la arquitectura; la operación produce observaciones; la respuesta y la recuperación aportan lecciones para revisar el programa. El valor de «TOGAF y Seguridad» se demuestra cuando mejora una decisión y una capacidad verificable, no cuando aumenta la cantidad de documentos, herramientas o reuniones. La pregunta abierta es qué cambiaría la recomendación ante un incidente, un nuevo requisito o una dependencia inesperada.

**Pregunta generadora:** ¿Qué decisión y qué evidencia demostrarían la utilidad de «TOGAF y Seguridad» en una organización concreta?

---

### 166. M3.1-K06 — ZTNA (Acceso)

**Unidad:** M3.1 · **Palabras:** 410 · **Estado:** idea central propuesta.

**Tesis central.** El diseño de acceso Zero Trust para aplicaciones privadas exige políticas por identidad y contexto, aislamiento y continuidad operativa. En el contexto del Programa Ejecutivo TheNextCISO, «ZTNA (Acceso)» no debe abordarse como una etiqueta de producto ni como una lista de pasos aislados. El ensayo debe explicar qué capacidad necesita desarrollar quien lidera la seguridad, cuál es su propósito empresarial y qué relación mantiene con el riesgo. Es esencial distinguir el mandato de gobierno —apetito, prioridades, responsabilidades y autoridad— de la gestión que diseña, opera y verifica la práctica. Esta distinción permite analizar decisiones sin atribuir automáticamente al CISO la ejecución de cada control.

**Problema y controversia.** El escenario que conviene examinar es el siguiente: se implementa ZTNA sin contemplar dependencias de aplicaciones heredadas. El lector debe reconocer que una solución aparentemente correcta puede introducir nuevos riesgos, costos o dependencias. La discusión debe explorar al menos dos alternativas y sus efectos sobre personas, procesos, datos, tecnología y terceros. También debe separar hechos de hipótesis, controles configurados de controles probados, y señales de alerta de incidentes confirmados. Cuando intervengan agentes de IA, se analizarán permisos, límites de autonomía, supervisión y trazabilidad, sin convertir la automatización en sustituto del juicio responsable.

**Aplicación formativa.** El participante trabajará un caso realista y elaborará patrón de acceso con excepciones y pruebas. Tendrá que definir el alcance, identificar activos y procesos afectados, documentar supuestos, asignar responsables y describir condiciones de entrada, éxito y reversión. La propuesta debe poder explicarse tanto a especialistas técnicos como a responsables de negocio. Para evitar soluciones decorativas, deberá incluir una prueba, simulación o procedimiento de revisión que permita observar resultados. Cuando el riesgo residual exceda los límites autorizados, se exigirá escalamiento a la autoridad correspondiente y registro de la decisión.

**Resultado esperado y evaluación.** El ensayo debe concluir con una recomendación ejecutable, sus dependencias, una explicación de por qué se eligió y qué evidencia podría refutarla. La evaluación del aprendizaje considerará precisión conceptual, razonamiento causal, viabilidad, evidencia, límites y comunicación. La relación con las otras unidades de GM-24 debe hacerse explícita: la estrategia y el gobierno del riesgo condicionan la arquitectura; la operación produce observaciones; la respuesta y la recuperación aportan lecciones para revisar el programa. El valor de «ZTNA (Acceso)» se demuestra cuando mejora una decisión y una capacidad verificable, no cuando aumenta la cantidad de documentos, herramientas o reuniones. La pregunta abierta es qué cambiaría la recomendación ante un incidente, un nuevo requisito o una dependencia inesperada.

**Pregunta generadora:** ¿Qué decisión y qué evidencia demostrarían la utilidad de «ZTNA (Acceso)» en una organización concreta?

---

### 167. M3.1-K07 — Microsegmentación

**Unidad:** M3.1 · **Palabras:** 408 · **Estado:** idea central propuesta.

**Tesis central.** La microsegmentación limita movimientos laterales y propagación mediante límites de comunicación basados en dependencias reales. En el contexto del Programa Ejecutivo TheNextCISO, «Microsegmentación» no debe abordarse como una etiqueta de producto ni como una lista de pasos aislados. El ensayo debe explicar qué capacidad necesita desarrollar quien lidera la seguridad, cuál es su propósito empresarial y qué relación mantiene con el riesgo. Es esencial distinguir el mandato de gobierno —apetito, prioridades, responsabilidades y autoridad— de la gestión que diseña, opera y verifica la práctica. Esta distinción permite analizar decisiones sin atribuir automáticamente al CISO la ejecución de cada control.

**Problema y controversia.** El escenario que conviene examinar es el siguiente: reglas demasiado estrictas interrumpen servicios y reglas amplias mantienen rutas de ataque. El lector debe reconocer que una solución aparentemente correcta puede introducir nuevos riesgos, costos o dependencias. La discusión debe explorar al menos dos alternativas y sus efectos sobre personas, procesos, datos, tecnología y terceros. También debe separar hechos de hipótesis, controles configurados de controles probados, y señales de alerta de incidentes confirmados. Cuando intervengan agentes de IA, se analizarán permisos, límites de autonomía, supervisión y trazabilidad, sin convertir la automatización en sustituto del juicio responsable.

**Aplicación formativa.** El participante trabajará un caso realista y elaborará matriz de flujos, políticas y pruebas de resiliencia. Tendrá que definir el alcance, identificar activos y procesos afectados, documentar supuestos, asignar responsables y describir condiciones de entrada, éxito y reversión. La propuesta debe poder explicarse tanto a especialistas técnicos como a responsables de negocio. Para evitar soluciones decorativas, deberá incluir una prueba, simulación o procedimiento de revisión que permita observar resultados. Cuando el riesgo residual exceda los límites autorizados, se exigirá escalamiento a la autoridad correspondiente y registro de la decisión.

**Resultado esperado y evaluación.** El ensayo debe concluir con una recomendación ejecutable, sus dependencias, una explicación de por qué se eligió y qué evidencia podría refutarla. La evaluación del aprendizaje considerará precisión conceptual, razonamiento causal, viabilidad, evidencia, límites y comunicación. La relación con las otras unidades de GM-24 debe hacerse explícita: la estrategia y el gobierno del riesgo condicionan la arquitectura; la operación produce observaciones; la respuesta y la recuperación aportan lecciones para revisar el programa. El valor de «Microsegmentación» se demuestra cuando mejora una decisión y una capacidad verificable, no cuando aumenta la cantidad de documentos, herramientas o reuniones. La pregunta abierta es qué cambiaría la recomendación ante un incidente, un nuevo requisito o una dependencia inesperada.

**Pregunta generadora:** ¿Qué decisión y qué evidencia demostrarían la utilidad de «Microsegmentación» en una organización concreta?

---

### 168. M3.1-K08 — Defensa en Profundidad

**Unidad:** M3.1 · **Palabras:** 416 · **Estado:** idea central propuesta.

**Tesis central.** La defensa en profundidad combina controles complementarios para reducir fallas comunes y limitar consecuencias cuando una barrera no funciona. En el contexto del Programa Ejecutivo TheNextCISO, «Defensa en Profundidad» no debe abordarse como una etiqueta de producto ni como una lista de pasos aislados. El ensayo debe explicar qué capacidad necesita desarrollar quien lidera la seguridad, cuál es su propósito empresarial y qué relación mantiene con el riesgo. Es esencial distinguir el mandato de gobierno —apetito, prioridades, responsabilidades y autoridad— de la gestión que diseña, opera y verifica la práctica. Esta distinción permite analizar decisiones sin atribuir automáticamente al CISO la ejecución de cada control.

**Problema y controversia.** El escenario que conviene examinar es el siguiente: varias herramientas dependen de la misma identidad comprometida y generan falsa redundancia. El lector debe reconocer que una solución aparentemente correcta puede introducir nuevos riesgos, costos o dependencias. La discusión debe explorar al menos dos alternativas y sus efectos sobre personas, procesos, datos, tecnología y terceros. También debe separar hechos de hipótesis, controles configurados de controles probados, y señales de alerta de incidentes confirmados. Cuando intervengan agentes de IA, se analizarán permisos, límites de autonomía, supervisión y trazabilidad, sin convertir la automatización en sustituto del juicio responsable.

**Aplicación formativa.** El participante trabajará un caso realista y elaborará mapa de capas, dependencias y pruebas de fallo. Tendrá que definir el alcance, identificar activos y procesos afectados, documentar supuestos, asignar responsables y describir condiciones de entrada, éxito y reversión. La propuesta debe poder explicarse tanto a especialistas técnicos como a responsables de negocio. Para evitar soluciones decorativas, deberá incluir una prueba, simulación o procedimiento de revisión que permita observar resultados. Cuando el riesgo residual exceda los límites autorizados, se exigirá escalamiento a la autoridad correspondiente y registro de la decisión.

**Resultado esperado y evaluación.** El ensayo debe concluir con una recomendación ejecutable, sus dependencias, una explicación de por qué se eligió y qué evidencia podría refutarla. La evaluación del aprendizaje considerará precisión conceptual, razonamiento causal, viabilidad, evidencia, límites y comunicación. La relación con las otras unidades de GM-24 debe hacerse explícita: la estrategia y el gobierno del riesgo condicionan la arquitectura; la operación produce observaciones; la respuesta y la recuperación aportan lecciones para revisar el programa. El valor de «Defensa en Profundidad» se demuestra cuando mejora una decisión y una capacidad verificable, no cuando aumenta la cantidad de documentos, herramientas o reuniones. La pregunta abierta es qué cambiaría la recomendación ante un incidente, un nuevo requisito o una dependencia inesperada.

**Pregunta generadora:** ¿Qué decisión y qué evidencia demostrarían la utilidad de «Defensa en Profundidad» en una organización concreta?

---

### 169. M3.1-K09 — Mínimo Privilegio (Arquitectura)

**Unidad:** M3.1 · **Palabras:** 412 · **Estado:** idea central propuesta.

**Tesis central.** El mínimo privilegio debe diseñarse en identidades, APIs, herramientas, datos y procesos con mecanismos de revisión y revocación. En el contexto del Programa Ejecutivo TheNextCISO, «Mínimo Privilegio (Arquitectura)» no debe abordarse como una etiqueta de producto ni como una lista de pasos aislados. El ensayo debe explicar qué capacidad necesita desarrollar quien lidera la seguridad, cuál es su propósito empresarial y qué relación mantiene con el riesgo. Es esencial distinguir el mandato de gobierno —apetito, prioridades, responsabilidades y autoridad— de la gestión que diseña, opera y verifica la práctica. Esta distinción permite analizar decisiones sin atribuir automáticamente al CISO la ejecución de cada control.

**Problema y controversia.** El escenario que conviene examinar es el siguiente: un agente hereda permisos globales para simplificar una integración. El lector debe reconocer que una solución aparentemente correcta puede introducir nuevos riesgos, costos o dependencias. La discusión debe explorar al menos dos alternativas y sus efectos sobre personas, procesos, datos, tecnología y terceros. También debe separar hechos de hipótesis, controles configurados de controles probados, y señales de alerta de incidentes confirmados. Cuando intervengan agentes de IA, se analizarán permisos, límites de autonomía, supervisión y trazabilidad, sin convertir la automatización en sustituto del juicio responsable.

**Aplicación formativa.** El participante trabajará un caso realista y elaborará diseño de scopes, delegaciones y pruebas de abuso. Tendrá que definir el alcance, identificar activos y procesos afectados, documentar supuestos, asignar responsables y describir condiciones de entrada, éxito y reversión. La propuesta debe poder explicarse tanto a especialistas técnicos como a responsables de negocio. Para evitar soluciones decorativas, deberá incluir una prueba, simulación o procedimiento de revisión que permita observar resultados. Cuando el riesgo residual exceda los límites autorizados, se exigirá escalamiento a la autoridad correspondiente y registro de la decisión.

**Resultado esperado y evaluación.** El ensayo debe concluir con una recomendación ejecutable, sus dependencias, una explicación de por qué se eligió y qué evidencia podría refutarla. La evaluación del aprendizaje considerará precisión conceptual, razonamiento causal, viabilidad, evidencia, límites y comunicación. La relación con las otras unidades de GM-24 debe hacerse explícita: la estrategia y el gobierno del riesgo condicionan la arquitectura; la operación produce observaciones; la respuesta y la recuperación aportan lecciones para revisar el programa. El valor de «Mínimo Privilegio (Arquitectura)» se demuestra cuando mejora una decisión y una capacidad verificable, no cuando aumenta la cantidad de documentos, herramientas o reuniones. La pregunta abierta es qué cambiaría la recomendación ante un incidente, un nuevo requisito o una dependencia inesperada.

**Pregunta generadora:** ¿Qué decisión y qué evidencia demostrarían la utilidad de «Mínimo Privilegio (Arquitectura)» en una organización concreta?

---

### 170. M3.1-K10 — Resiliencia (Diseño)

**Unidad:** M3.1 · **Palabras:** 409 · **Estado:** idea central propuesta.

**Tesis central.** La resiliencia por diseño incorpora degradación controlada, aislamiento, recuperación y observabilidad desde la arquitectura inicial. En el contexto del Programa Ejecutivo TheNextCISO, «Resiliencia (Diseño)» no debe abordarse como una etiqueta de producto ni como una lista de pasos aislados. El ensayo debe explicar qué capacidad necesita desarrollar quien lidera la seguridad, cuál es su propósito empresarial y qué relación mantiene con el riesgo. Es esencial distinguir el mandato de gobierno —apetito, prioridades, responsabilidades y autoridad— de la gestión que diseña, opera y verifica la práctica. Esta distinción permite analizar decisiones sin atribuir automáticamente al CISO la ejecución de cada control.

**Problema y controversia.** El escenario que conviene examinar es el siguiente: un servicio crítico carece de ruta de recuperación ante pérdida de proveedor. El lector debe reconocer que una solución aparentemente correcta puede introducir nuevos riesgos, costos o dependencias. La discusión debe explorar al menos dos alternativas y sus efectos sobre personas, procesos, datos, tecnología y terceros. También debe separar hechos de hipótesis, controles configurados de controles probados, y señales de alerta de incidentes confirmados. Cuando intervengan agentes de IA, se analizarán permisos, límites de autonomía, supervisión y trazabilidad, sin convertir la automatización en sustituto del juicio responsable.

**Aplicación formativa.** El participante trabajará un caso realista y elaborará arquitectura de fallos, RTO/RPO y pruebas. Tendrá que definir el alcance, identificar activos y procesos afectados, documentar supuestos, asignar responsables y describir condiciones de entrada, éxito y reversión. La propuesta debe poder explicarse tanto a especialistas técnicos como a responsables de negocio. Para evitar soluciones decorativas, deberá incluir una prueba, simulación o procedimiento de revisión que permita observar resultados. Cuando el riesgo residual exceda los límites autorizados, se exigirá escalamiento a la autoridad correspondiente y registro de la decisión.

**Resultado esperado y evaluación.** El ensayo debe concluir con una recomendación ejecutable, sus dependencias, una explicación de por qué se eligió y qué evidencia podría refutarla. La evaluación del aprendizaje considerará precisión conceptual, razonamiento causal, viabilidad, evidencia, límites y comunicación. La relación con las otras unidades de GM-24 debe hacerse explícita: la estrategia y el gobierno del riesgo condicionan la arquitectura; la operación produce observaciones; la respuesta y la recuperación aportan lecciones para revisar el programa. El valor de «Resiliencia (Diseño)» se demuestra cuando mejora una decisión y una capacidad verificable, no cuando aumenta la cantidad de documentos, herramientas o reuniones. La pregunta abierta es qué cambiaría la recomendación ante un incidente, un nuevo requisito o una dependencia inesperada.

**Pregunta generadora:** ¿Qué decisión y qué evidencia demostrarían la utilidad de «Resiliencia (Diseño)» en una organización concreta?

---

## M3.2 — Selección, Implementación y Evaluación de Controles

### 171. M3.2-K01 — Controles de Seguridad

**Unidad:** M3.2 · **Palabras:** 417 · **Estado:** idea central propuesta.

**Tesis central.** Un control de seguridad es una salvaguarda con propósito, condiciones y evidencia; no debe confundirse con el resultado que intenta producir. En el contexto del Programa Ejecutivo TheNextCISO, «Controles de Seguridad» no debe abordarse como una etiqueta de producto ni como una lista de pasos aislados. El ensayo debe explicar qué capacidad necesita desarrollar quien lidera la seguridad, cuál es su propósito empresarial y qué relación mantiene con el riesgo. Es esencial distinguir el mandato de gobierno —apetito, prioridades, responsabilidades y autoridad— de la gestión que diseña, opera y verifica la práctica. Esta distinción permite analizar decisiones sin atribuir automáticamente al CISO la ejecución de cada control.

**Problema y controversia.** El escenario que conviene examinar es el siguiente: un producto se registra como control efectivo sin configuración ni pruebas. El lector debe reconocer que una solución aparentemente correcta puede introducir nuevos riesgos, costos o dependencias. La discusión debe explorar al menos dos alternativas y sus efectos sobre personas, procesos, datos, tecnología y terceros. También debe separar hechos de hipótesis, controles configurados de controles probados, y señales de alerta de incidentes confirmados. Cuando intervengan agentes de IA, se analizarán permisos, límites de autonomía, supervisión y trazabilidad, sin convertir la automatización en sustituto del juicio responsable.

**Aplicación formativa.** El participante trabajará un caso realista y elaborará ficha de control con objetivo, owner y evidencia. Tendrá que definir el alcance, identificar activos y procesos afectados, documentar supuestos, asignar responsables y describir condiciones de entrada, éxito y reversión. La propuesta debe poder explicarse tanto a especialistas técnicos como a responsables de negocio. Para evitar soluciones decorativas, deberá incluir una prueba, simulación o procedimiento de revisión que permita observar resultados. Cuando el riesgo residual exceda los límites autorizados, se exigirá escalamiento a la autoridad correspondiente y registro de la decisión.

**Resultado esperado y evaluación.** El ensayo debe concluir con una recomendación ejecutable, sus dependencias, una explicación de por qué se eligió y qué evidencia podría refutarla. La evaluación del aprendizaje considerará precisión conceptual, razonamiento causal, viabilidad, evidencia, límites y comunicación. La relación con las otras unidades de GM-24 debe hacerse explícita: la estrategia y el gobierno del riesgo condicionan la arquitectura; la operación produce observaciones; la respuesta y la recuperación aportan lecciones para revisar el programa. El valor de «Controles de Seguridad» se demuestra cuando mejora una decisión y una capacidad verificable, no cuando aumenta la cantidad de documentos, herramientas o reuniones. La pregunta abierta es qué cambiaría la recomendación ante un incidente, un nuevo requisito o una dependencia inesperada.

**Pregunta generadora:** ¿Qué decisión y qué evidencia demostrarían la utilidad de «Controles de Seguridad» en una organización concreta?

---

### 172. M3.2-K02 — NIST SP 800-53

**Unidad:** M3.2 · **Palabras:** 417 · **Estado:** idea central propuesta.

**Tesis central.** NIST SP 800-53 ofrece un catálogo de controles que requiere selección y adaptación según sistema, riesgo y obligaciones, no aplicación literal indiscriminada. En el contexto del Programa Ejecutivo TheNextCISO, «NIST SP 800-53» no debe abordarse como una etiqueta de producto ni como una lista de pasos aislados. El ensayo debe explicar qué capacidad necesita desarrollar quien lidera la seguridad, cuál es su propósito empresarial y qué relación mantiene con el riesgo. Es esencial distinguir el mandato de gobierno —apetito, prioridades, responsabilidades y autoridad— de la gestión que diseña, opera y verifica la práctica. Esta distinción permite analizar decisiones sin atribuir automáticamente al CISO la ejecución de cada control.

**Problema y controversia.** El escenario que conviene examinar es el siguiente: se declara cumplimiento de una familia por haber comprado una plataforma. El lector debe reconocer que una solución aparentemente correcta puede introducir nuevos riesgos, costos o dependencias. La discusión debe explorar al menos dos alternativas y sus efectos sobre personas, procesos, datos, tecnología y terceros. También debe separar hechos de hipótesis, controles configurados de controles probados, y señales de alerta de incidentes confirmados. Cuando intervengan agentes de IA, se analizarán permisos, límites de autonomía, supervisión y trazabilidad, sin convertir la automatización en sustituto del juicio responsable.

**Aplicación formativa.** El participante trabajará un caso realista y elaborará selección de controles con referencias y justificación. Tendrá que definir el alcance, identificar activos y procesos afectados, documentar supuestos, asignar responsables y describir condiciones de entrada, éxito y reversión. La propuesta debe poder explicarse tanto a especialistas técnicos como a responsables de negocio. Para evitar soluciones decorativas, deberá incluir una prueba, simulación o procedimiento de revisión que permita observar resultados. Cuando el riesgo residual exceda los límites autorizados, se exigirá escalamiento a la autoridad correspondiente y registro de la decisión.

**Resultado esperado y evaluación.** El ensayo debe concluir con una recomendación ejecutable, sus dependencias, una explicación de por qué se eligió y qué evidencia podría refutarla. La evaluación del aprendizaje considerará precisión conceptual, razonamiento causal, viabilidad, evidencia, límites y comunicación. La relación con las otras unidades de GM-24 debe hacerse explícita: la estrategia y el gobierno del riesgo condicionan la arquitectura; la operación produce observaciones; la respuesta y la recuperación aportan lecciones para revisar el programa. El valor de «NIST SP 800-53» se demuestra cuando mejora una decisión y una capacidad verificable, no cuando aumenta la cantidad de documentos, herramientas o reuniones. La pregunta abierta es qué cambiaría la recomendación ante un incidente, un nuevo requisito o una dependencia inesperada.

**Pregunta generadora:** ¿Qué decisión y qué evidencia demostrarían la utilidad de «NIST SP 800-53» en una organización concreta?

---

### 173. M3.2-K03 — Selección y Adaptación

**Unidad:** M3.2 · **Palabras:** 405 · **Estado:** idea central propuesta.

**Tesis central.** Seleccionar y adaptar controles exige evaluar aplicabilidad, costo, dependencias, riesgos y medidas compensatorias. En el contexto del Programa Ejecutivo TheNextCISO, «Selección y Adaptación» no debe abordarse como una etiqueta de producto ni como una lista de pasos aislados. El ensayo debe explicar qué capacidad necesita desarrollar quien lidera la seguridad, cuál es su propósito empresarial y qué relación mantiene con el riesgo. Es esencial distinguir el mandato de gobierno —apetito, prioridades, responsabilidades y autoridad— de la gestión que diseña, opera y verifica la práctica. Esta distinción permite analizar decisiones sin atribuir automáticamente al CISO la ejecución de cada control.

**Problema y controversia.** El escenario que conviene examinar es el siguiente: un control estándar interrumpe operaciones industriales sin alternativa. El lector debe reconocer que una solución aparentemente correcta puede introducir nuevos riesgos, costos o dependencias. La discusión debe explorar al menos dos alternativas y sus efectos sobre personas, procesos, datos, tecnología y terceros. También debe separar hechos de hipótesis, controles configurados de controles probados, y señales de alerta de incidentes confirmados. Cuando intervengan agentes de IA, se analizarán permisos, límites de autonomía, supervisión y trazabilidad, sin convertir la automatización en sustituto del juicio responsable.

**Aplicación formativa.** El participante trabajará un caso realista y elaborará decisión de tailoring con riesgos y excepciones. Tendrá que definir el alcance, identificar activos y procesos afectados, documentar supuestos, asignar responsables y describir condiciones de entrada, éxito y reversión. La propuesta debe poder explicarse tanto a especialistas técnicos como a responsables de negocio. Para evitar soluciones decorativas, deberá incluir una prueba, simulación o procedimiento de revisión que permita observar resultados. Cuando el riesgo residual exceda los límites autorizados, se exigirá escalamiento a la autoridad correspondiente y registro de la decisión.

**Resultado esperado y evaluación.** El ensayo debe concluir con una recomendación ejecutable, sus dependencias, una explicación de por qué se eligió y qué evidencia podría refutarla. La evaluación del aprendizaje considerará precisión conceptual, razonamiento causal, viabilidad, evidencia, límites y comunicación. La relación con las otras unidades de GM-24 debe hacerse explícita: la estrategia y el gobierno del riesgo condicionan la arquitectura; la operación produce observaciones; la respuesta y la recuperación aportan lecciones para revisar el programa. El valor de «Selección y Adaptación» se demuestra cuando mejora una decisión y una capacidad verificable, no cuando aumenta la cantidad de documentos, herramientas o reuniones. La pregunta abierta es qué cambiaría la recomendación ante un incidente, un nuevo requisito o una dependencia inesperada.

**Pregunta generadora:** ¿Qué decisión y qué evidencia demostrarían la utilidad de «Selección y Adaptación» en una organización concreta?

---

### 174. M3.2-K04 — Evaluación (Assess)

**Unidad:** M3.2 · **Palabras:** 404 · **Estado:** idea central propuesta.

**Tesis central.** Evaluar controles implica comprobar diseño e implementación con procedimientos y evidencia suficientes para sostener conclusiones limitadas. En el contexto del Programa Ejecutivo TheNextCISO, «Evaluación (Assess)» no debe abordarse como una etiqueta de producto ni como una lista de pasos aislados. El ensayo debe explicar qué capacidad necesita desarrollar quien lidera la seguridad, cuál es su propósito empresarial y qué relación mantiene con el riesgo. Es esencial distinguir el mandato de gobierno —apetito, prioridades, responsabilidades y autoridad— de la gestión que diseña, opera y verifica la práctica. Esta distinción permite analizar decisiones sin atribuir automáticamente al CISO la ejecución de cada control.

**Problema y controversia.** El escenario que conviene examinar es el siguiente: un dashboard favorable sustituye pruebas de funcionamiento. El lector debe reconocer que una solución aparentemente correcta puede introducir nuevos riesgos, costos o dependencias. La discusión debe explorar al menos dos alternativas y sus efectos sobre personas, procesos, datos, tecnología y terceros. También debe separar hechos de hipótesis, controles configurados de controles probados, y señales de alerta de incidentes confirmados. Cuando intervengan agentes de IA, se analizarán permisos, límites de autonomía, supervisión y trazabilidad, sin convertir la automatización en sustituto del juicio responsable.

**Aplicación formativa.** El participante trabajará un caso realista y elaborará plan de evaluación, muestras y hallazgos. Tendrá que definir el alcance, identificar activos y procesos afectados, documentar supuestos, asignar responsables y describir condiciones de entrada, éxito y reversión. La propuesta debe poder explicarse tanto a especialistas técnicos como a responsables de negocio. Para evitar soluciones decorativas, deberá incluir una prueba, simulación o procedimiento de revisión que permita observar resultados. Cuando el riesgo residual exceda los límites autorizados, se exigirá escalamiento a la autoridad correspondiente y registro de la decisión.

**Resultado esperado y evaluación.** El ensayo debe concluir con una recomendación ejecutable, sus dependencias, una explicación de por qué se eligió y qué evidencia podría refutarla. La evaluación del aprendizaje considerará precisión conceptual, razonamiento causal, viabilidad, evidencia, límites y comunicación. La relación con las otras unidades de GM-24 debe hacerse explícita: la estrategia y el gobierno del riesgo condicionan la arquitectura; la operación produce observaciones; la respuesta y la recuperación aportan lecciones para revisar el programa. El valor de «Evaluación (Assess)» se demuestra cuando mejora una decisión y una capacidad verificable, no cuando aumenta la cantidad de documentos, herramientas o reuniones. La pregunta abierta es qué cambiaría la recomendación ante un incidente, un nuevo requisito o una dependencia inesperada.

**Pregunta generadora:** ¿Qué decisión y qué evidencia demostrarían la utilidad de «Evaluación (Assess)» en una organización concreta?

---

### 175. M3.2-K05 — Implementación

**Unidad:** M3.2 · **Palabras:** 402 · **Estado:** idea central propuesta.

**Tesis central.** La implementación requiere traducir diseños a configuraciones, procesos, responsabilidades y despliegues controlados con rollback. En el contexto del Programa Ejecutivo TheNextCISO, «Implementación» no debe abordarse como una etiqueta de producto ni como una lista de pasos aislados. El ensayo debe explicar qué capacidad necesita desarrollar quien lidera la seguridad, cuál es su propósito empresarial y qué relación mantiene con el riesgo. Es esencial distinguir el mandato de gobierno —apetito, prioridades, responsabilidades y autoridad— de la gestión que diseña, opera y verifica la práctica. Esta distinción permite analizar decisiones sin atribuir automáticamente al CISO la ejecución de cada control.

**Problema y controversia.** El escenario que conviene examinar es el siguiente: una política se habilita globalmente sin piloto ni comunicación. El lector debe reconocer que una solución aparentemente correcta puede introducir nuevos riesgos, costos o dependencias. La discusión debe explorar al menos dos alternativas y sus efectos sobre personas, procesos, datos, tecnología y terceros. También debe separar hechos de hipótesis, controles configurados de controles probados, y señales de alerta de incidentes confirmados. Cuando intervengan agentes de IA, se analizarán permisos, límites de autonomía, supervisión y trazabilidad, sin convertir la automatización en sustituto del juicio responsable.

**Aplicación formativa.** El participante trabajará un caso realista y elaborará plan de implementación, pruebas y aceptación. Tendrá que definir el alcance, identificar activos y procesos afectados, documentar supuestos, asignar responsables y describir condiciones de entrada, éxito y reversión. La propuesta debe poder explicarse tanto a especialistas técnicos como a responsables de negocio. Para evitar soluciones decorativas, deberá incluir una prueba, simulación o procedimiento de revisión que permita observar resultados. Cuando el riesgo residual exceda los límites autorizados, se exigirá escalamiento a la autoridad correspondiente y registro de la decisión.

**Resultado esperado y evaluación.** El ensayo debe concluir con una recomendación ejecutable, sus dependencias, una explicación de por qué se eligió y qué evidencia podría refutarla. La evaluación del aprendizaje considerará precisión conceptual, razonamiento causal, viabilidad, evidencia, límites y comunicación. La relación con las otras unidades de GM-24 debe hacerse explícita: la estrategia y el gobierno del riesgo condicionan la arquitectura; la operación produce observaciones; la respuesta y la recuperación aportan lecciones para revisar el programa. El valor de «Implementación» se demuestra cuando mejora una decisión y una capacidad verificable, no cuando aumenta la cantidad de documentos, herramientas o reuniones. La pregunta abierta es qué cambiaría la recomendación ante un incidente, un nuevo requisito o una dependencia inesperada.

**Pregunta generadora:** ¿Qué decisión y qué evidencia demostrarían la utilidad de «Implementación» en una organización concreta?

---

### 176. M3.2-K06 — Pentesting

**Unidad:** M3.2 · **Palabras:** 413 · **Estado:** idea central propuesta.

**Tesis central.** Las pruebas de penetración exploran rutas de explotación en un alcance autorizado, complementando pero no sustituyendo evaluación de controles y gestión de riesgos. En el contexto del Programa Ejecutivo TheNextCISO, «Pentesting» no debe abordarse como una etiqueta de producto ni como una lista de pasos aislados. El ensayo debe explicar qué capacidad necesita desarrollar quien lidera la seguridad, cuál es su propósito empresarial y qué relación mantiene con el riesgo. Es esencial distinguir el mandato de gobierno —apetito, prioridades, responsabilidades y autoridad— de la gestión que diseña, opera y verifica la práctica. Esta distinción permite analizar decisiones sin atribuir automáticamente al CISO la ejecución de cada control.

**Problema y controversia.** El escenario que conviene examinar es el siguiente: un resultado sin hallazgos se interpreta como ausencia de vulnerabilidades. El lector debe reconocer que una solución aparentemente correcta puede introducir nuevos riesgos, costos o dependencias. La discusión debe explorar al menos dos alternativas y sus efectos sobre personas, procesos, datos, tecnología y terceros. También debe separar hechos de hipótesis, controles configurados de controles probados, y señales de alerta de incidentes confirmados. Cuando intervengan agentes de IA, se analizarán permisos, límites de autonomía, supervisión y trazabilidad, sin convertir la automatización en sustituto del juicio responsable.

**Aplicación formativa.** El participante trabajará un caso realista y elaborará alcance, reglas de engagement, hallazgos y remediación. Tendrá que definir el alcance, identificar activos y procesos afectados, documentar supuestos, asignar responsables y describir condiciones de entrada, éxito y reversión. La propuesta debe poder explicarse tanto a especialistas técnicos como a responsables de negocio. Para evitar soluciones decorativas, deberá incluir una prueba, simulación o procedimiento de revisión que permita observar resultados. Cuando el riesgo residual exceda los límites autorizados, se exigirá escalamiento a la autoridad correspondiente y registro de la decisión.

**Resultado esperado y evaluación.** El ensayo debe concluir con una recomendación ejecutable, sus dependencias, una explicación de por qué se eligió y qué evidencia podría refutarla. La evaluación del aprendizaje considerará precisión conceptual, razonamiento causal, viabilidad, evidencia, límites y comunicación. La relación con las otras unidades de GM-24 debe hacerse explícita: la estrategia y el gobierno del riesgo condicionan la arquitectura; la operación produce observaciones; la respuesta y la recuperación aportan lecciones para revisar el programa. El valor de «Pentesting» se demuestra cuando mejora una decisión y una capacidad verificable, no cuando aumenta la cantidad de documentos, herramientas o reuniones. La pregunta abierta es qué cambiaría la recomendación ante un incidente, un nuevo requisito o una dependencia inesperada.

**Pregunta generadora:** ¿Qué decisión y qué evidencia demostrarían la utilidad de «Pentesting» en una organización concreta?

---

### 177. M3.2-K07 — Controles Compensatorios

**Unidad:** M3.2 · **Palabras:** 408 · **Estado:** idea central propuesta.

**Tesis central.** Un control compensatorio reduce exposición cuando el requisito primario no puede cumplirse, con justificación, límite temporal y evidencia. En el contexto del Programa Ejecutivo TheNextCISO, «Controles Compensatorios» no debe abordarse como una etiqueta de producto ni como una lista de pasos aislados. El ensayo debe explicar qué capacidad necesita desarrollar quien lidera la seguridad, cuál es su propósito empresarial y qué relación mantiene con el riesgo. Es esencial distinguir el mandato de gobierno —apetito, prioridades, responsabilidades y autoridad— de la gestión que diseña, opera y verifica la práctica. Esta distinción permite analizar decisiones sin atribuir automáticamente al CISO la ejecución de cada control.

**Problema y controversia.** El escenario que conviene examinar es el siguiente: una excepción temporal se convierte en deuda permanente. El lector debe reconocer que una solución aparentemente correcta puede introducir nuevos riesgos, costos o dependencias. La discusión debe explorar al menos dos alternativas y sus efectos sobre personas, procesos, datos, tecnología y terceros. También debe separar hechos de hipótesis, controles configurados de controles probados, y señales de alerta de incidentes confirmados. Cuando intervengan agentes de IA, se analizarán permisos, límites de autonomía, supervisión y trazabilidad, sin convertir la automatización en sustituto del juicio responsable.

**Aplicación formativa.** El participante trabajará un caso realista y elaborará expediente de compensación, riesgo residual y expiración. Tendrá que definir el alcance, identificar activos y procesos afectados, documentar supuestos, asignar responsables y describir condiciones de entrada, éxito y reversión. La propuesta debe poder explicarse tanto a especialistas técnicos como a responsables de negocio. Para evitar soluciones decorativas, deberá incluir una prueba, simulación o procedimiento de revisión que permita observar resultados. Cuando el riesgo residual exceda los límites autorizados, se exigirá escalamiento a la autoridad correspondiente y registro de la decisión.

**Resultado esperado y evaluación.** El ensayo debe concluir con una recomendación ejecutable, sus dependencias, una explicación de por qué se eligió y qué evidencia podría refutarla. La evaluación del aprendizaje considerará precisión conceptual, razonamiento causal, viabilidad, evidencia, límites y comunicación. La relación con las otras unidades de GM-24 debe hacerse explícita: la estrategia y el gobierno del riesgo condicionan la arquitectura; la operación produce observaciones; la respuesta y la recuperación aportan lecciones para revisar el programa. El valor de «Controles Compensatorios» se demuestra cuando mejora una decisión y una capacidad verificable, no cuando aumenta la cantidad de documentos, herramientas o reuniones. La pregunta abierta es qué cambiaría la recomendación ante un incidente, un nuevo requisito o una dependencia inesperada.

**Pregunta generadora:** ¿Qué decisión y qué evidencia demostrarían la utilidad de «Controles Compensatorios» en una organización concreta?

---

### 178. M3.2-K08 — Familias de Controles

**Unidad:** M3.2 · **Palabras:** 410 · **Estado:** idea central propuesta.

**Tesis central.** Las familias de controles permiten organizar objetivos relacionados y responsabilidades sin asumir equivalencia entre controles individuales. En el contexto del Programa Ejecutivo TheNextCISO, «Familias de Controles» no debe abordarse como una etiqueta de producto ni como una lista de pasos aislados. El ensayo debe explicar qué capacidad necesita desarrollar quien lidera la seguridad, cuál es su propósito empresarial y qué relación mantiene con el riesgo. Es esencial distinguir el mandato de gobierno —apetito, prioridades, responsabilidades y autoridad— de la gestión que diseña, opera y verifica la práctica. Esta distinción permite analizar decisiones sin atribuir automáticamente al CISO la ejecución de cada control.

**Problema y controversia.** El escenario que conviene examinar es el siguiente: se contabilizan controles por cantidad y no por cobertura de escenarios. El lector debe reconocer que una solución aparentemente correcta puede introducir nuevos riesgos, costos o dependencias. La discusión debe explorar al menos dos alternativas y sus efectos sobre personas, procesos, datos, tecnología y terceros. También debe separar hechos de hipótesis, controles configurados de controles probados, y señales de alerta de incidentes confirmados. Cuando intervengan agentes de IA, se analizarán permisos, límites de autonomía, supervisión y trazabilidad, sin convertir la automatización en sustituto del juicio responsable.

**Aplicación formativa.** El participante trabajará un caso realista y elaborará matriz de familias, objetivos y dependencias. Tendrá que definir el alcance, identificar activos y procesos afectados, documentar supuestos, asignar responsables y describir condiciones de entrada, éxito y reversión. La propuesta debe poder explicarse tanto a especialistas técnicos como a responsables de negocio. Para evitar soluciones decorativas, deberá incluir una prueba, simulación o procedimiento de revisión que permita observar resultados. Cuando el riesgo residual exceda los límites autorizados, se exigirá escalamiento a la autoridad correspondiente y registro de la decisión.

**Resultado esperado y evaluación.** El ensayo debe concluir con una recomendación ejecutable, sus dependencias, una explicación de por qué se eligió y qué evidencia podría refutarla. La evaluación del aprendizaje considerará precisión conceptual, razonamiento causal, viabilidad, evidencia, límites y comunicación. La relación con las otras unidades de GM-24 debe hacerse explícita: la estrategia y el gobierno del riesgo condicionan la arquitectura; la operación produce observaciones; la respuesta y la recuperación aportan lecciones para revisar el programa. El valor de «Familias de Controles» se demuestra cuando mejora una decisión y una capacidad verificable, no cuando aumenta la cantidad de documentos, herramientas o reuniones. La pregunta abierta es qué cambiaría la recomendación ante un incidente, un nuevo requisito o una dependencia inesperada.

**Pregunta generadora:** ¿Qué decisión y qué evidencia demostrarían la utilidad de «Familias de Controles» en una organización concreta?

---

### 179. M3.2-K09 — Pruebas de Efectividad

**Unidad:** M3.2 · **Palabras:** 410 · **Estado:** idea central propuesta.

**Tesis central.** Las pruebas de efectividad verifican resultados bajo escenarios definidos, distinguiendo cobertura, operación y consecuencia observable. En el contexto del Programa Ejecutivo TheNextCISO, «Pruebas de Efectividad» no debe abordarse como una etiqueta de producto ni como una lista de pasos aislados. El ensayo debe explicar qué capacidad necesita desarrollar quien lidera la seguridad, cuál es su propósito empresarial y qué relación mantiene con el riesgo. Es esencial distinguir el mandato de gobierno —apetito, prioridades, responsabilidades y autoridad— de la gestión que diseña, opera y verifica la práctica. Esta distinción permite analizar decisiones sin atribuir automáticamente al CISO la ejecución de cada control.

**Problema y controversia.** El escenario que conviene examinar es el siguiente: un control configurado se declara eficaz sin ejercicio de ataque o recuperación. El lector debe reconocer que una solución aparentemente correcta puede introducir nuevos riesgos, costos o dependencias. La discusión debe explorar al menos dos alternativas y sus efectos sobre personas, procesos, datos, tecnología y terceros. También debe separar hechos de hipótesis, controles configurados de controles probados, y señales de alerta de incidentes confirmados. Cuando intervengan agentes de IA, se analizarán permisos, límites de autonomía, supervisión y trazabilidad, sin convertir la automatización en sustituto del juicio responsable.

**Aplicación formativa.** El participante trabajará un caso realista y elaborará protocolo de prueba, criterios y resultados. Tendrá que definir el alcance, identificar activos y procesos afectados, documentar supuestos, asignar responsables y describir condiciones de entrada, éxito y reversión. La propuesta debe poder explicarse tanto a especialistas técnicos como a responsables de negocio. Para evitar soluciones decorativas, deberá incluir una prueba, simulación o procedimiento de revisión que permita observar resultados. Cuando el riesgo residual exceda los límites autorizados, se exigirá escalamiento a la autoridad correspondiente y registro de la decisión.

**Resultado esperado y evaluación.** El ensayo debe concluir con una recomendación ejecutable, sus dependencias, una explicación de por qué se eligió y qué evidencia podría refutarla. La evaluación del aprendizaje considerará precisión conceptual, razonamiento causal, viabilidad, evidencia, límites y comunicación. La relación con las otras unidades de GM-24 debe hacerse explícita: la estrategia y el gobierno del riesgo condicionan la arquitectura; la operación produce observaciones; la respuesta y la recuperación aportan lecciones para revisar el programa. El valor de «Pruebas de Efectividad» se demuestra cuando mejora una decisión y una capacidad verificable, no cuando aumenta la cantidad de documentos, herramientas o reuniones. La pregunta abierta es qué cambiaría la recomendación ante un incidente, un nuevo requisito o una dependencia inesperada.

**Pregunta generadora:** ¿Qué decisión y qué evidencia demostrarían la utilidad de «Pruebas de Efectividad» en una organización concreta?

---

### 180. M3.2-K10 — POA&M

**Unidad:** M3.2 · **Palabras:** 408 · **Estado:** idea central propuesta.

**Tesis central.** El Plan of Action and Milestones conecta hallazgos con responsables, recursos, fechas, riesgos y evidencia de cierre verificable. En el contexto del Programa Ejecutivo TheNextCISO, «POA&M» no debe abordarse como una etiqueta de producto ni como una lista de pasos aislados. El ensayo debe explicar qué capacidad necesita desarrollar quien lidera la seguridad, cuál es su propósito empresarial y qué relación mantiene con el riesgo. Es esencial distinguir el mandato de gobierno —apetito, prioridades, responsabilidades y autoridad— de la gestión que diseña, opera y verifica la práctica. Esta distinción permite analizar decisiones sin atribuir automáticamente al CISO la ejecución de cada control.

**Problema y controversia.** El escenario que conviene examinar es el siguiente: los hallazgos se cierran administrativamente sin corregir causas. El lector debe reconocer que una solución aparentemente correcta puede introducir nuevos riesgos, costos o dependencias. La discusión debe explorar al menos dos alternativas y sus efectos sobre personas, procesos, datos, tecnología y terceros. También debe separar hechos de hipótesis, controles configurados de controles probados, y señales de alerta de incidentes confirmados. Cuando intervengan agentes de IA, se analizarán permisos, límites de autonomía, supervisión y trazabilidad, sin convertir la automatización en sustituto del juicio responsable.

**Aplicación formativa.** El participante trabajará un caso realista y elaborará POA&M priorizado con pruebas de cierre. Tendrá que definir el alcance, identificar activos y procesos afectados, documentar supuestos, asignar responsables y describir condiciones de entrada, éxito y reversión. La propuesta debe poder explicarse tanto a especialistas técnicos como a responsables de negocio. Para evitar soluciones decorativas, deberá incluir una prueba, simulación o procedimiento de revisión que permita observar resultados. Cuando el riesgo residual exceda los límites autorizados, se exigirá escalamiento a la autoridad correspondiente y registro de la decisión.

**Resultado esperado y evaluación.** El ensayo debe concluir con una recomendación ejecutable, sus dependencias, una explicación de por qué se eligió y qué evidencia podría refutarla. La evaluación del aprendizaje considerará precisión conceptual, razonamiento causal, viabilidad, evidencia, límites y comunicación. La relación con las otras unidades de GM-24 debe hacerse explícita: la estrategia y el gobierno del riesgo condicionan la arquitectura; la operación produce observaciones; la respuesta y la recuperación aportan lecciones para revisar el programa. El valor de «POA&M» se demuestra cuando mejora una decisión y una capacidad verificable, no cuando aumenta la cantidad de documentos, herramientas o reuniones. La pregunta abierta es qué cambiaría la recomendación ante un incidente, un nuevo requisito o una dependencia inesperada.

**Pregunta generadora:** ¿Qué decisión y qué evidencia demostrarían la utilidad de «POA&M» en una organización concreta?

---

## Control de calidad y continuidad

- Conceptos incluidos: **30** (151–180).
- Extensión comprobada: **402–418 palabras** por idea central.
- Los conceptos y nombres se preservan en el orden del Documento Maestro GM-24.
- No se asignaron IDs de ensayos ni se aplicaron ChangeSets.

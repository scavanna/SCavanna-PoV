# TheNextCISO GM-24 — Ideas centrales para ensayos, lote 08

**Conceptos 211–240 · Pilar Gestión de la Ciberseguridad**

**Unidades:** M5.2, M6.1, M6.2

**Estado:** ideas centrales propuestas para futuros ensayos; no representan nodos aprobados del Atlas ni ensayos completos.

## Criterio editorial

Cada concepto mantiene el nombre y la secuencia curricular GM-24. El desarrollo argumental es original y diferencia decisiones de Gobierno de ejecución, operación y evidencia de Gestión. Los códigos curriculares no son identificadores permanentes `ESS-######`; éstos requieren reserva autoritativa en SQLite.

## M5.2 — Ejecución, Post-Mortem y Comunicación

### 211. M5.2-K01 — Contención

**Unidad:** M5.2 · **Palabras:** 412 · **Estado:** idea central propuesta.

**Tesis central.** La contención limita propagación y consecuencias de un incidente con decisiones proporcionales, reversibles cuando sea posible y coordinadas con negocio. En el contexto del Programa Ejecutivo TheNextCISO, «Contención» no debe abordarse como una etiqueta de producto ni como una lista de pasos aislados. El ensayo debe explicar qué capacidad necesita desarrollar quien lidera la seguridad, cuál es su propósito empresarial y qué relación mantiene con el riesgo. Es esencial distinguir el mandato de gobierno —apetito, prioridades, responsabilidades y autoridad— de la gestión que diseña, opera y verifica la práctica. Esta distinción permite analizar decisiones sin atribuir automáticamente al CISO la ejecución de cada control.

**Problema y controversia.** El escenario que conviene examinar es el siguiente: aislar un servicio detiene al adversario pero interrumpe una operación crítica. El lector debe reconocer que una solución aparentemente correcta puede introducir nuevos riesgos, costos o dependencias. La discusión debe explorar al menos dos alternativas y sus efectos sobre personas, procesos, datos, tecnología y terceros. También debe separar hechos de hipótesis, controles configurados de controles probados, y señales de alerta de incidentes confirmados. Cuando intervengan agentes de IA, se analizarán permisos, límites de autonomía, supervisión y trazabilidad, sin convertir la automatización en sustituto del juicio responsable.

**Aplicación formativa.** El participante trabajará un caso realista y elaborará árbol de decisión de contención, autorizaciones y pruebas. Tendrá que definir el alcance, identificar activos y procesos afectados, documentar supuestos, asignar responsables y describir condiciones de entrada, éxito y reversión. La propuesta debe poder explicarse tanto a especialistas técnicos como a responsables de negocio. Para evitar soluciones decorativas, deberá incluir una prueba, simulación o procedimiento de revisión que permita observar resultados. Cuando el riesgo residual exceda los límites autorizados, se exigirá escalamiento a la autoridad correspondiente y registro de la decisión.

**Resultado esperado y evaluación.** El ensayo debe concluir con una recomendación ejecutable, sus dependencias, una explicación de por qué se eligió y qué evidencia podría refutarla. La evaluación del aprendizaje considerará precisión conceptual, razonamiento causal, viabilidad, evidencia, límites y comunicación. La relación con las otras unidades de GM-24 debe hacerse explícita: la estrategia y el gobierno del riesgo condicionan la arquitectura; la operación produce observaciones; la respuesta y la recuperación aportan lecciones para revisar el programa. El valor de «Contención» se demuestra cuando mejora una decisión y una capacidad verificable, no cuando aumenta la cantidad de documentos, herramientas o reuniones. La pregunta abierta es qué cambiaría la recomendación ante un incidente, un nuevo requisito o una dependencia inesperada.

**Pregunta generadora:** ¿Qué decisión y qué evidencia demostrarían la utilidad de «Contención» en una organización concreta?

---

### 212. M5.2-K02 — Erradicación

**Unidad:** M5.2 · **Palabras:** 405 · **Estado:** idea central propuesta.

**Tesis central.** La erradicación elimina persistencia y causas explotables después de preservar evidencia y comprender el alcance suficiente del incidente. En el contexto del Programa Ejecutivo TheNextCISO, «Erradicación» no debe abordarse como una etiqueta de producto ni como una lista de pasos aislados. El ensayo debe explicar qué capacidad necesita desarrollar quien lidera la seguridad, cuál es su propósito empresarial y qué relación mantiene con el riesgo. Es esencial distinguir el mandato de gobierno —apetito, prioridades, responsabilidades y autoridad— de la gestión que diseña, opera y verifica la práctica. Esta distinción permite analizar decisiones sin atribuir automáticamente al CISO la ejecución de cada control.

**Problema y controversia.** El escenario que conviene examinar es el siguiente: se reinstala un servidor sin corregir credenciales comprometidas. El lector debe reconocer que una solución aparentemente correcta puede introducir nuevos riesgos, costos o dependencias. La discusión debe explorar al menos dos alternativas y sus efectos sobre personas, procesos, datos, tecnología y terceros. También debe separar hechos de hipótesis, controles configurados de controles probados, y señales de alerta de incidentes confirmados. Cuando intervengan agentes de IA, se analizarán permisos, límites de autonomía, supervisión y trazabilidad, sin convertir la automatización en sustituto del juicio responsable.

**Aplicación formativa.** El participante trabajará un caso realista y elaborará plan de erradicación, hipótesis y validación. Tendrá que definir el alcance, identificar activos y procesos afectados, documentar supuestos, asignar responsables y describir condiciones de entrada, éxito y reversión. La propuesta debe poder explicarse tanto a especialistas técnicos como a responsables de negocio. Para evitar soluciones decorativas, deberá incluir una prueba, simulación o procedimiento de revisión que permita observar resultados. Cuando el riesgo residual exceda los límites autorizados, se exigirá escalamiento a la autoridad correspondiente y registro de la decisión.

**Resultado esperado y evaluación.** El ensayo debe concluir con una recomendación ejecutable, sus dependencias, una explicación de por qué se eligió y qué evidencia podría refutarla. La evaluación del aprendizaje considerará precisión conceptual, razonamiento causal, viabilidad, evidencia, límites y comunicación. La relación con las otras unidades de GM-24 debe hacerse explícita: la estrategia y el gobierno del riesgo condicionan la arquitectura; la operación produce observaciones; la respuesta y la recuperación aportan lecciones para revisar el programa. El valor de «Erradicación» se demuestra cuando mejora una decisión y una capacidad verificable, no cuando aumenta la cantidad de documentos, herramientas o reuniones. La pregunta abierta es qué cambiaría la recomendación ante un incidente, un nuevo requisito o una dependencia inesperada.

**Pregunta generadora:** ¿Qué decisión y qué evidencia demostrarían la utilidad de «Erradicación» en una organización concreta?

---

### 213. M5.2-K03 — Recuperación

**Unidad:** M5.2 · **Palabras:** 407 · **Estado:** idea central propuesta.

**Tesis central.** La recuperación tras incidentes restaura servicios confiables y datos íntegros mediante criterios de retorno seguro, no solo encendido de sistemas. En el contexto del Programa Ejecutivo TheNextCISO, «Recuperación» no debe abordarse como una etiqueta de producto ni como una lista de pasos aislados. El ensayo debe explicar qué capacidad necesita desarrollar quien lidera la seguridad, cuál es su propósito empresarial y qué relación mantiene con el riesgo. Es esencial distinguir el mandato de gobierno —apetito, prioridades, responsabilidades y autoridad— de la gestión que diseña, opera y verifica la práctica. Esta distinción permite analizar decisiones sin atribuir automáticamente al CISO la ejecución de cada control.

**Problema y controversia.** El escenario que conviene examinar es el siguiente: un backup restaura malware o permisos comprometidos. El lector debe reconocer que una solución aparentemente correcta puede introducir nuevos riesgos, costos o dependencias. La discusión debe explorar al menos dos alternativas y sus efectos sobre personas, procesos, datos, tecnología y terceros. También debe separar hechos de hipótesis, controles configurados de controles probados, y señales de alerta de incidentes confirmados. Cuando intervengan agentes de IA, se analizarán permisos, límites de autonomía, supervisión y trazabilidad, sin convertir la automatización en sustituto del juicio responsable.

**Aplicación formativa.** El participante trabajará un caso realista y elaborará plan de retorno con pruebas y aceptación. Tendrá que definir el alcance, identificar activos y procesos afectados, documentar supuestos, asignar responsables y describir condiciones de entrada, éxito y reversión. La propuesta debe poder explicarse tanto a especialistas técnicos como a responsables de negocio. Para evitar soluciones decorativas, deberá incluir una prueba, simulación o procedimiento de revisión que permita observar resultados. Cuando el riesgo residual exceda los límites autorizados, se exigirá escalamiento a la autoridad correspondiente y registro de la decisión.

**Resultado esperado y evaluación.** El ensayo debe concluir con una recomendación ejecutable, sus dependencias, una explicación de por qué se eligió y qué evidencia podría refutarla. La evaluación del aprendizaje considerará precisión conceptual, razonamiento causal, viabilidad, evidencia, límites y comunicación. La relación con las otras unidades de GM-24 debe hacerse explícita: la estrategia y el gobierno del riesgo condicionan la arquitectura; la operación produce observaciones; la respuesta y la recuperación aportan lecciones para revisar el programa. El valor de «Recuperación» se demuestra cuando mejora una decisión y una capacidad verificable, no cuando aumenta la cantidad de documentos, herramientas o reuniones. La pregunta abierta es qué cambiaría la recomendación ante un incidente, un nuevo requisito o una dependencia inesperada.

**Pregunta generadora:** ¿Qué decisión y qué evidencia demostrarían la utilidad de «Recuperación» en una organización concreta?

---

### 214. M5.2-K04 — Comunicación Crisis

**Unidad:** M5.2 · **Palabras:** 405 · **Estado:** idea central propuesta.

**Tesis central.** La comunicación de crisis coordina hechos, incertidumbres, audiencias, tiempos y autoridad para evitar mensajes contradictorios. En el contexto del Programa Ejecutivo TheNextCISO, «Comunicación Crisis» no debe abordarse como una etiqueta de producto ni como una lista de pasos aislados. El ensayo debe explicar qué capacidad necesita desarrollar quien lidera la seguridad, cuál es su propósito empresarial y qué relación mantiene con el riesgo. Es esencial distinguir el mandato de gobierno —apetito, prioridades, responsabilidades y autoridad— de la gestión que diseña, opera y verifica la práctica. Esta distinción permite analizar decisiones sin atribuir automáticamente al CISO la ejecución de cada control.

**Problema y controversia.** El escenario que conviene examinar es el siguiente: un portavoz anuncia causa e impacto antes de validarlos. El lector debe reconocer que una solución aparentemente correcta puede introducir nuevos riesgos, costos o dependencias. La discusión debe explorar al menos dos alternativas y sus efectos sobre personas, procesos, datos, tecnología y terceros. También debe separar hechos de hipótesis, controles configurados de controles probados, y señales de alerta de incidentes confirmados. Cuando intervengan agentes de IA, se analizarán permisos, límites de autonomía, supervisión y trazabilidad, sin convertir la automatización en sustituto del juicio responsable.

**Aplicación formativa.** El participante trabajará un caso realista y elaborará plan de mensajes, aprobaciones y actualizaciones. Tendrá que definir el alcance, identificar activos y procesos afectados, documentar supuestos, asignar responsables y describir condiciones de entrada, éxito y reversión. La propuesta debe poder explicarse tanto a especialistas técnicos como a responsables de negocio. Para evitar soluciones decorativas, deberá incluir una prueba, simulación o procedimiento de revisión que permita observar resultados. Cuando el riesgo residual exceda los límites autorizados, se exigirá escalamiento a la autoridad correspondiente y registro de la decisión.

**Resultado esperado y evaluación.** El ensayo debe concluir con una recomendación ejecutable, sus dependencias, una explicación de por qué se eligió y qué evidencia podría refutarla. La evaluación del aprendizaje considerará precisión conceptual, razonamiento causal, viabilidad, evidencia, límites y comunicación. La relación con las otras unidades de GM-24 debe hacerse explícita: la estrategia y el gobierno del riesgo condicionan la arquitectura; la operación produce observaciones; la respuesta y la recuperación aportan lecciones para revisar el programa. El valor de «Comunicación Crisis» se demuestra cuando mejora una decisión y una capacidad verificable, no cuando aumenta la cantidad de documentos, herramientas o reuniones. La pregunta abierta es qué cambiaría la recomendación ante un incidente, un nuevo requisito o una dependencia inesperada.

**Pregunta generadora:** ¿Qué decisión y qué evidencia demostrarían la utilidad de «Comunicación Crisis» en una organización concreta?

---

### 215. M5.2-K05 — Post-Mortem

**Unidad:** M5.2 · **Palabras:** 404 · **Estado:** idea central propuesta.

**Tesis central.** El post-mortem identifica fallas sistémicas y decisiones mejorables sin reducir el aprendizaje a asignar culpas individuales. En el contexto del Programa Ejecutivo TheNextCISO, «Post-Mortem» no debe abordarse como una etiqueta de producto ni como una lista de pasos aislados. El ensayo debe explicar qué capacidad necesita desarrollar quien lidera la seguridad, cuál es su propósito empresarial y qué relación mantiene con el riesgo. Es esencial distinguir el mandato de gobierno —apetito, prioridades, responsabilidades y autoridad— de la gestión que diseña, opera y verifica la práctica. Esta distinción permite analizar decisiones sin atribuir automáticamente al CISO la ejecución de cada control.

**Problema y controversia.** El escenario que conviene examinar es el siguiente: el cierre del incidente no modifica controles ni procesos. El lector debe reconocer que una solución aparentemente correcta puede introducir nuevos riesgos, costos o dependencias. La discusión debe explorar al menos dos alternativas y sus efectos sobre personas, procesos, datos, tecnología y terceros. También debe separar hechos de hipótesis, controles configurados de controles probados, y señales de alerta de incidentes confirmados. Cuando intervengan agentes de IA, se analizarán permisos, límites de autonomía, supervisión y trazabilidad, sin convertir la automatización en sustituto del juicio responsable.

**Aplicación formativa.** El participante trabajará un caso realista y elaborará informe de lecciones, causas y acciones. Tendrá que definir el alcance, identificar activos y procesos afectados, documentar supuestos, asignar responsables y describir condiciones de entrada, éxito y reversión. La propuesta debe poder explicarse tanto a especialistas técnicos como a responsables de negocio. Para evitar soluciones decorativas, deberá incluir una prueba, simulación o procedimiento de revisión que permita observar resultados. Cuando el riesgo residual exceda los límites autorizados, se exigirá escalamiento a la autoridad correspondiente y registro de la decisión.

**Resultado esperado y evaluación.** El ensayo debe concluir con una recomendación ejecutable, sus dependencias, una explicación de por qué se eligió y qué evidencia podría refutarla. La evaluación del aprendizaje considerará precisión conceptual, razonamiento causal, viabilidad, evidencia, límites y comunicación. La relación con las otras unidades de GM-24 debe hacerse explícita: la estrategia y el gobierno del riesgo condicionan la arquitectura; la operación produce observaciones; la respuesta y la recuperación aportan lecciones para revisar el programa. El valor de «Post-Mortem» se demuestra cuando mejora una decisión y una capacidad verificable, no cuando aumenta la cantidad de documentos, herramientas o reuniones. La pregunta abierta es qué cambiaría la recomendación ante un incidente, un nuevo requisito o una dependencia inesperada.

**Pregunta generadora:** ¿Qué decisión y qué evidencia demostrarían la utilidad de «Post-Mortem» en una organización concreta?

---

### 216. M5.2-K06 — Forense Digital

**Unidad:** M5.2 · **Palabras:** 409 · **Estado:** idea central propuesta.

**Tesis central.** La forense digital preserva y analiza evidencia de manera íntegra, contextual y trazable para reconstruir hechos y apoyar decisiones. En el contexto del Programa Ejecutivo TheNextCISO, «Forense Digital» no debe abordarse como una etiqueta de producto ni como una lista de pasos aislados. El ensayo debe explicar qué capacidad necesita desarrollar quien lidera la seguridad, cuál es su propósito empresarial y qué relación mantiene con el riesgo. Es esencial distinguir el mandato de gobierno —apetito, prioridades, responsabilidades y autoridad— de la gestión que diseña, opera y verifica la práctica. Esta distinción permite analizar decisiones sin atribuir automáticamente al CISO la ejecución de cada control.

**Problema y controversia.** El escenario que conviene examinar es el siguiente: se alteran registros al responder sin cadena de custodia. El lector debe reconocer que una solución aparentemente correcta puede introducir nuevos riesgos, costos o dependencias. La discusión debe explorar al menos dos alternativas y sus efectos sobre personas, procesos, datos, tecnología y terceros. También debe separar hechos de hipótesis, controles configurados de controles probados, y señales de alerta de incidentes confirmados. Cuando intervengan agentes de IA, se analizarán permisos, límites de autonomía, supervisión y trazabilidad, sin convertir la automatización en sustituto del juicio responsable.

**Aplicación formativa.** El participante trabajará un caso realista y elaborará plan de adquisición, integridad y análisis. Tendrá que definir el alcance, identificar activos y procesos afectados, documentar supuestos, asignar responsables y describir condiciones de entrada, éxito y reversión. La propuesta debe poder explicarse tanto a especialistas técnicos como a responsables de negocio. Para evitar soluciones decorativas, deberá incluir una prueba, simulación o procedimiento de revisión que permita observar resultados. Cuando el riesgo residual exceda los límites autorizados, se exigirá escalamiento a la autoridad correspondiente y registro de la decisión.

**Resultado esperado y evaluación.** El ensayo debe concluir con una recomendación ejecutable, sus dependencias, una explicación de por qué se eligió y qué evidencia podría refutarla. La evaluación del aprendizaje considerará precisión conceptual, razonamiento causal, viabilidad, evidencia, límites y comunicación. La relación con las otras unidades de GM-24 debe hacerse explícita: la estrategia y el gobierno del riesgo condicionan la arquitectura; la operación produce observaciones; la respuesta y la recuperación aportan lecciones para revisar el programa. El valor de «Forense Digital» se demuestra cuando mejora una decisión y una capacidad verificable, no cuando aumenta la cantidad de documentos, herramientas o reuniones. La pregunta abierta es qué cambiaría la recomendación ante un incidente, un nuevo requisito o una dependencia inesperada.

**Pregunta generadora:** ¿Qué decisión y qué evidencia demostrarían la utilidad de «Forense Digital» en una organización concreta?

---

### 217. M5.2-K07 — Triaje

**Unidad:** M5.2 · **Palabras:** 409 · **Estado:** idea central propuesta.

**Tesis central.** El triaje prioriza señales e incidentes potenciales según evidencia, impacto, urgencia y recursos, evitando equiparar alerta con confirmación. En el contexto del Programa Ejecutivo TheNextCISO, «Triaje» no debe abordarse como una etiqueta de producto ni como una lista de pasos aislados. El ensayo debe explicar qué capacidad necesita desarrollar quien lidera la seguridad, cuál es su propósito empresarial y qué relación mantiene con el riesgo. Es esencial distinguir el mandato de gobierno —apetito, prioridades, responsabilidades y autoridad— de la gestión que diseña, opera y verifica la práctica. Esta distinción permite analizar decisiones sin atribuir automáticamente al CISO la ejecución de cada control.

**Problema y controversia.** El escenario que conviene examinar es el siguiente: un volumen de alertas consume la capacidad de respuesta sin criterios claros. El lector debe reconocer que una solución aparentemente correcta puede introducir nuevos riesgos, costos o dependencias. La discusión debe explorar al menos dos alternativas y sus efectos sobre personas, procesos, datos, tecnología y terceros. También debe separar hechos de hipótesis, controles configurados de controles probados, y señales de alerta de incidentes confirmados. Cuando intervengan agentes de IA, se analizarán permisos, límites de autonomía, supervisión y trazabilidad, sin convertir la automatización en sustituto del juicio responsable.

**Aplicación formativa.** El participante trabajará un caso realista y elaborará modelo de severidad, escalamiento y pruebas. Tendrá que definir el alcance, identificar activos y procesos afectados, documentar supuestos, asignar responsables y describir condiciones de entrada, éxito y reversión. La propuesta debe poder explicarse tanto a especialistas técnicos como a responsables de negocio. Para evitar soluciones decorativas, deberá incluir una prueba, simulación o procedimiento de revisión que permita observar resultados. Cuando el riesgo residual exceda los límites autorizados, se exigirá escalamiento a la autoridad correspondiente y registro de la decisión.

**Resultado esperado y evaluación.** El ensayo debe concluir con una recomendación ejecutable, sus dependencias, una explicación de por qué se eligió y qué evidencia podría refutarla. La evaluación del aprendizaje considerará precisión conceptual, razonamiento causal, viabilidad, evidencia, límites y comunicación. La relación con las otras unidades de GM-24 debe hacerse explícita: la estrategia y el gobierno del riesgo condicionan la arquitectura; la operación produce observaciones; la respuesta y la recuperación aportan lecciones para revisar el programa. El valor de «Triaje» se demuestra cuando mejora una decisión y una capacidad verificable, no cuando aumenta la cantidad de documentos, herramientas o reuniones. La pregunta abierta es qué cambiaría la recomendación ante un incidente, un nuevo requisito o una dependencia inesperada.

**Pregunta generadora:** ¿Qué decisión y qué evidencia demostrarían la utilidad de «Triaje» en una organización concreta?

---

### 218. M5.2-K08 — Gestión Narrativa

**Unidad:** M5.2 · **Palabras:** 410 · **Estado:** idea central propuesta.

**Tesis central.** La gestión narrativa en crisis busca coherencia y transparencia responsable entre hechos conocidos, hipótesis y compromisos de comunicación. En el contexto del Programa Ejecutivo TheNextCISO, «Gestión Narrativa» no debe abordarse como una etiqueta de producto ni como una lista de pasos aislados. El ensayo debe explicar qué capacidad necesita desarrollar quien lidera la seguridad, cuál es su propósito empresarial y qué relación mantiene con el riesgo. Es esencial distinguir el mandato de gobierno —apetito, prioridades, responsabilidades y autoridad— de la gestión que diseña, opera y verifica la práctica. Esta distinción permite analizar decisiones sin atribuir automáticamente al CISO la ejecución de cada control.

**Problema y controversia.** El escenario que conviene examinar es el siguiente: la organización promete certeza para controlar reputación y luego debe retractarse. El lector debe reconocer que una solución aparentemente correcta puede introducir nuevos riesgos, costos o dependencias. La discusión debe explorar al menos dos alternativas y sus efectos sobre personas, procesos, datos, tecnología y terceros. También debe separar hechos de hipótesis, controles configurados de controles probados, y señales de alerta de incidentes confirmados. Cuando intervengan agentes de IA, se analizarán permisos, límites de autonomía, supervisión y trazabilidad, sin convertir la automatización en sustituto del juicio responsable.

**Aplicación formativa.** El participante trabajará un caso realista y elaborará cronología factual y registro de mensajes. Tendrá que definir el alcance, identificar activos y procesos afectados, documentar supuestos, asignar responsables y describir condiciones de entrada, éxito y reversión. La propuesta debe poder explicarse tanto a especialistas técnicos como a responsables de negocio. Para evitar soluciones decorativas, deberá incluir una prueba, simulación o procedimiento de revisión que permita observar resultados. Cuando el riesgo residual exceda los límites autorizados, se exigirá escalamiento a la autoridad correspondiente y registro de la decisión.

**Resultado esperado y evaluación.** El ensayo debe concluir con una recomendación ejecutable, sus dependencias, una explicación de por qué se eligió y qué evidencia podría refutarla. La evaluación del aprendizaje considerará precisión conceptual, razonamiento causal, viabilidad, evidencia, límites y comunicación. La relación con las otras unidades de GM-24 debe hacerse explícita: la estrategia y el gobierno del riesgo condicionan la arquitectura; la operación produce observaciones; la respuesta y la recuperación aportan lecciones para revisar el programa. El valor de «Gestión Narrativa» se demuestra cuando mejora una decisión y una capacidad verificable, no cuando aumenta la cantidad de documentos, herramientas o reuniones. La pregunta abierta es qué cambiaría la recomendación ante un incidente, un nuevo requisito o una dependencia inesperada.

**Pregunta generadora:** ¿Qué decisión y qué evidencia demostrarían la utilidad de «Gestión Narrativa» en una organización concreta?

---

### 219. M5.2-K09 — Notificación Brechas

**Unidad:** M5.2 · **Palabras:** 411 · **Estado:** idea central propuesta.

**Tesis central.** La notificación de brechas depende de obligaciones, materialidad, plazos y hechos verificados, en coordinación con Legal y Privacidad. En el contexto del Programa Ejecutivo TheNextCISO, «Notificación Brechas» no debe abordarse como una etiqueta de producto ni como una lista de pasos aislados. El ensayo debe explicar qué capacidad necesita desarrollar quien lidera la seguridad, cuál es su propósito empresarial y qué relación mantiene con el riesgo. Es esencial distinguir el mandato de gobierno —apetito, prioridades, responsabilidades y autoridad— de la gestión que diseña, opera y verifica la práctica. Esta distinción permite analizar decisiones sin atribuir automáticamente al CISO la ejecución de cada control.

**Problema y controversia.** El escenario que conviene examinar es el siguiente: un equipo comunica demasiado tarde o afirma incumplimiento sin evaluación competente. El lector debe reconocer que una solución aparentemente correcta puede introducir nuevos riesgos, costos o dependencias. La discusión debe explorar al menos dos alternativas y sus efectos sobre personas, procesos, datos, tecnología y terceros. También debe separar hechos de hipótesis, controles configurados de controles probados, y señales de alerta de incidentes confirmados. Cuando intervengan agentes de IA, se analizarán permisos, límites de autonomía, supervisión y trazabilidad, sin convertir la automatización en sustituto del juicio responsable.

**Aplicación formativa.** El participante trabajará un caso realista y elaborará matriz de obligaciones y decisión de notificación. Tendrá que definir el alcance, identificar activos y procesos afectados, documentar supuestos, asignar responsables y describir condiciones de entrada, éxito y reversión. La propuesta debe poder explicarse tanto a especialistas técnicos como a responsables de negocio. Para evitar soluciones decorativas, deberá incluir una prueba, simulación o procedimiento de revisión que permita observar resultados. Cuando el riesgo residual exceda los límites autorizados, se exigirá escalamiento a la autoridad correspondiente y registro de la decisión.

**Resultado esperado y evaluación.** El ensayo debe concluir con una recomendación ejecutable, sus dependencias, una explicación de por qué se eligió y qué evidencia podría refutarla. La evaluación del aprendizaje considerará precisión conceptual, razonamiento causal, viabilidad, evidencia, límites y comunicación. La relación con las otras unidades de GM-24 debe hacerse explícita: la estrategia y el gobierno del riesgo condicionan la arquitectura; la operación produce observaciones; la respuesta y la recuperación aportan lecciones para revisar el programa. El valor de «Notificación Brechas» se demuestra cuando mejora una decisión y una capacidad verificable, no cuando aumenta la cantidad de documentos, herramientas o reuniones. La pregunta abierta es qué cambiaría la recomendación ante un incidente, un nuevo requisito o una dependencia inesperada.

**Pregunta generadora:** ¿Qué decisión y qué evidencia demostrarían la utilidad de «Notificación Brechas» en una organización concreta?

---

### 220. M5.2-K10 — Resiliencia Adaptativa

**Unidad:** M5.2 · **Palabras:** 407 · **Estado:** idea central propuesta.

**Tesis central.** La resiliencia adaptativa convierte incidentes en cambios de diseño, operación y gobierno para responder mejor a amenazas futuras. En el contexto del Programa Ejecutivo TheNextCISO, «Resiliencia Adaptativa» no debe abordarse como una etiqueta de producto ni como una lista de pasos aislados. El ensayo debe explicar qué capacidad necesita desarrollar quien lidera la seguridad, cuál es su propósito empresarial y qué relación mantiene con el riesgo. Es esencial distinguir el mandato de gobierno —apetito, prioridades, responsabilidades y autoridad— de la gestión que diseña, opera y verifica la práctica. Esta distinción permite analizar decisiones sin atribuir automáticamente al CISO la ejecución de cada control.

**Problema y controversia.** El escenario que conviene examinar es el siguiente: se restablece servicio pero persisten dependencias frágiles. El lector debe reconocer que una solución aparentemente correcta puede introducir nuevos riesgos, costos o dependencias. La discusión debe explorar al menos dos alternativas y sus efectos sobre personas, procesos, datos, tecnología y terceros. También debe separar hechos de hipótesis, controles configurados de controles probados, y señales de alerta de incidentes confirmados. Cuando intervengan agentes de IA, se analizarán permisos, límites de autonomía, supervisión y trazabilidad, sin convertir la automatización en sustituto del juicio responsable.

**Aplicación formativa.** El participante trabajará un caso realista y elaborará plan de mejora con pruebas de resiliencia. Tendrá que definir el alcance, identificar activos y procesos afectados, documentar supuestos, asignar responsables y describir condiciones de entrada, éxito y reversión. La propuesta debe poder explicarse tanto a especialistas técnicos como a responsables de negocio. Para evitar soluciones decorativas, deberá incluir una prueba, simulación o procedimiento de revisión que permita observar resultados. Cuando el riesgo residual exceda los límites autorizados, se exigirá escalamiento a la autoridad correspondiente y registro de la decisión.

**Resultado esperado y evaluación.** El ensayo debe concluir con una recomendación ejecutable, sus dependencias, una explicación de por qué se eligió y qué evidencia podría refutarla. La evaluación del aprendizaje considerará precisión conceptual, razonamiento causal, viabilidad, evidencia, límites y comunicación. La relación con las otras unidades de GM-24 debe hacerse explícita: la estrategia y el gobierno del riesgo condicionan la arquitectura; la operación produce observaciones; la respuesta y la recuperación aportan lecciones para revisar el programa. El valor de «Resiliencia Adaptativa» se demuestra cuando mejora una decisión y una capacidad verificable, no cuando aumenta la cantidad de documentos, herramientas o reuniones. La pregunta abierta es qué cambiaría la recomendación ante un incidente, un nuevo requisito o una dependencia inesperada.

**Pregunta generadora:** ¿Qué decisión y qué evidencia demostrarían la utilidad de «Resiliencia Adaptativa» en una organización concreta?

---

## M6.1 — Continuidad, DRP y Resiliencia Operativa

### 221. M6.1-K01 — Continuidad (BCP)

**Unidad:** M6.1 · **Palabras:** 408 · **Estado:** idea central propuesta.

**Tesis central.** La continuidad del negocio establece cómo sostener procesos críticos durante perturbaciones mediante prioridades y capacidades de operación alternativa. En el contexto del Programa Ejecutivo TheNextCISO, «Continuidad (BCP)» no debe abordarse como una etiqueta de producto ni como una lista de pasos aislados. El ensayo debe explicar qué capacidad necesita desarrollar quien lidera la seguridad, cuál es su propósito empresarial y qué relación mantiene con el riesgo. Es esencial distinguir el mandato de gobierno —apetito, prioridades, responsabilidades y autoridad— de la gestión que diseña, opera y verifica la práctica. Esta distinción permite analizar decisiones sin atribuir automáticamente al CISO la ejecución de cada control.

**Problema y controversia.** El escenario que conviene examinar es el siguiente: un plan enumera servidores sin contemplar procesos y personas. El lector debe reconocer que una solución aparentemente correcta puede introducir nuevos riesgos, costos o dependencias. La discusión debe explorar al menos dos alternativas y sus efectos sobre personas, procesos, datos, tecnología y terceros. También debe separar hechos de hipótesis, controles configurados de controles probados, y señales de alerta de incidentes confirmados. Cuando intervengan agentes de IA, se analizarán permisos, límites de autonomía, supervisión y trazabilidad, sin convertir la automatización en sustituto del juicio responsable.

**Aplicación formativa.** El participante trabajará un caso realista y elaborará BCP con procesos, roles y escenarios. Tendrá que definir el alcance, identificar activos y procesos afectados, documentar supuestos, asignar responsables y describir condiciones de entrada, éxito y reversión. La propuesta debe poder explicarse tanto a especialistas técnicos como a responsables de negocio. Para evitar soluciones decorativas, deberá incluir una prueba, simulación o procedimiento de revisión que permita observar resultados. Cuando el riesgo residual exceda los límites autorizados, se exigirá escalamiento a la autoridad correspondiente y registro de la decisión.

**Resultado esperado y evaluación.** El ensayo debe concluir con una recomendación ejecutable, sus dependencias, una explicación de por qué se eligió y qué evidencia podría refutarla. La evaluación del aprendizaje considerará precisión conceptual, razonamiento causal, viabilidad, evidencia, límites y comunicación. La relación con las otras unidades de GM-24 debe hacerse explícita: la estrategia y el gobierno del riesgo condicionan la arquitectura; la operación produce observaciones; la respuesta y la recuperación aportan lecciones para revisar el programa. El valor de «Continuidad (BCP)» se demuestra cuando mejora una decisión y una capacidad verificable, no cuando aumenta la cantidad de documentos, herramientas o reuniones. La pregunta abierta es qué cambiaría la recomendación ante un incidente, un nuevo requisito o una dependencia inesperada.

**Pregunta generadora:** ¿Qué decisión y qué evidencia demostrarían la utilidad de «Continuidad (BCP)» en una organización concreta?

---

### 222. M6.1-K02 — Recuperación (DRP)

**Unidad:** M6.1 · **Palabras:** 407 · **Estado:** idea central propuesta.

**Tesis central.** El plan de recuperación tecnológica define secuencia, dependencias, recursos y pruebas para restaurar sistemas de soporte al negocio. En el contexto del Programa Ejecutivo TheNextCISO, «Recuperación (DRP)» no debe abordarse como una etiqueta de producto ni como una lista de pasos aislados. El ensayo debe explicar qué capacidad necesita desarrollar quien lidera la seguridad, cuál es su propósito empresarial y qué relación mantiene con el riesgo. Es esencial distinguir el mandato de gobierno —apetito, prioridades, responsabilidades y autoridad— de la gestión que diseña, opera y verifica la práctica. Esta distinción permite analizar decisiones sin atribuir automáticamente al CISO la ejecución de cada control.

**Problema y controversia.** El escenario que conviene examinar es el siguiente: la restauración depende de identidades o claves inaccesibles. El lector debe reconocer que una solución aparentemente correcta puede introducir nuevos riesgos, costos o dependencias. La discusión debe explorar al menos dos alternativas y sus efectos sobre personas, procesos, datos, tecnología y terceros. También debe separar hechos de hipótesis, controles configurados de controles probados, y señales de alerta de incidentes confirmados. Cuando intervengan agentes de IA, se analizarán permisos, límites de autonomía, supervisión y trazabilidad, sin convertir la automatización en sustituto del juicio responsable.

**Aplicación formativa.** El participante trabajará un caso realista y elaborará DRP probado con dependencias y criterios. Tendrá que definir el alcance, identificar activos y procesos afectados, documentar supuestos, asignar responsables y describir condiciones de entrada, éxito y reversión. La propuesta debe poder explicarse tanto a especialistas técnicos como a responsables de negocio. Para evitar soluciones decorativas, deberá incluir una prueba, simulación o procedimiento de revisión que permita observar resultados. Cuando el riesgo residual exceda los límites autorizados, se exigirá escalamiento a la autoridad correspondiente y registro de la decisión.

**Resultado esperado y evaluación.** El ensayo debe concluir con una recomendación ejecutable, sus dependencias, una explicación de por qué se eligió y qué evidencia podría refutarla. La evaluación del aprendizaje considerará precisión conceptual, razonamiento causal, viabilidad, evidencia, límites y comunicación. La relación con las otras unidades de GM-24 debe hacerse explícita: la estrategia y el gobierno del riesgo condicionan la arquitectura; la operación produce observaciones; la respuesta y la recuperación aportan lecciones para revisar el programa. El valor de «Recuperación (DRP)» se demuestra cuando mejora una decisión y una capacidad verificable, no cuando aumenta la cantidad de documentos, herramientas o reuniones. La pregunta abierta es qué cambiaría la recomendación ante un incidente, un nuevo requisito o una dependencia inesperada.

**Pregunta generadora:** ¿Qué decisión y qué evidencia demostrarían la utilidad de «Recuperación (DRP)» en una organización concreta?

---

### 223. M6.1-K03 — Resiliencia Operativa

**Unidad:** M6.1 · **Palabras:** 405 · **Estado:** idea central propuesta.

**Tesis central.** La resiliencia operativa integra anticipación, absorción, adaptación y recuperación para mantener servicios dentro de tolerancias. En el contexto del Programa Ejecutivo TheNextCISO, «Resiliencia Operativa» no debe abordarse como una etiqueta de producto ni como una lista de pasos aislados. El ensayo debe explicar qué capacidad necesita desarrollar quien lidera la seguridad, cuál es su propósito empresarial y qué relación mantiene con el riesgo. Es esencial distinguir el mandato de gobierno —apetito, prioridades, responsabilidades y autoridad— de la gestión que diseña, opera y verifica la práctica. Esta distinción permite analizar decisiones sin atribuir automáticamente al CISO la ejecución de cada control.

**Problema y controversia.** El escenario que conviene examinar es el siguiente: una arquitectura redundante falla por dependencia compartida. El lector debe reconocer que una solución aparentemente correcta puede introducir nuevos riesgos, costos o dependencias. La discusión debe explorar al menos dos alternativas y sus efectos sobre personas, procesos, datos, tecnología y terceros. También debe separar hechos de hipótesis, controles configurados de controles probados, y señales de alerta de incidentes confirmados. Cuando intervengan agentes de IA, se analizarán permisos, límites de autonomía, supervisión y trazabilidad, sin convertir la automatización en sustituto del juicio responsable.

**Aplicación formativa.** El participante trabajará un caso realista y elaborará mapa de servicios críticos y pruebas de perturbación. Tendrá que definir el alcance, identificar activos y procesos afectados, documentar supuestos, asignar responsables y describir condiciones de entrada, éxito y reversión. La propuesta debe poder explicarse tanto a especialistas técnicos como a responsables de negocio. Para evitar soluciones decorativas, deberá incluir una prueba, simulación o procedimiento de revisión que permita observar resultados. Cuando el riesgo residual exceda los límites autorizados, se exigirá escalamiento a la autoridad correspondiente y registro de la decisión.

**Resultado esperado y evaluación.** El ensayo debe concluir con una recomendación ejecutable, sus dependencias, una explicación de por qué se eligió y qué evidencia podría refutarla. La evaluación del aprendizaje considerará precisión conceptual, razonamiento causal, viabilidad, evidencia, límites y comunicación. La relación con las otras unidades de GM-24 debe hacerse explícita: la estrategia y el gobierno del riesgo condicionan la arquitectura; la operación produce observaciones; la respuesta y la recuperación aportan lecciones para revisar el programa. El valor de «Resiliencia Operativa» se demuestra cuando mejora una decisión y una capacidad verificable, no cuando aumenta la cantidad de documentos, herramientas o reuniones. La pregunta abierta es qué cambiaría la recomendación ante un incidente, un nuevo requisito o una dependencia inesperada.

**Pregunta generadora:** ¿Qué decisión y qué evidencia demostrarían la utilidad de «Resiliencia Operativa» en una organización concreta?

---

### 224. M6.1-K04 — ISO 22301

**Unidad:** M6.1 · **Palabras:** 407 · **Estado:** idea central propuesta.

**Tesis central.** ISO 22301 proporciona requisitos de un sistema de gestión de continuidad que deben adaptarse a alcance, contexto y evidencia. En el contexto del Programa Ejecutivo TheNextCISO, «ISO 22301» no debe abordarse como una etiqueta de producto ni como una lista de pasos aislados. El ensayo debe explicar qué capacidad necesita desarrollar quien lidera la seguridad, cuál es su propósito empresarial y qué relación mantiene con el riesgo. Es esencial distinguir el mandato de gobierno —apetito, prioridades, responsabilidades y autoridad— de la gestión que diseña, opera y verifica la práctica. Esta distinción permite analizar decisiones sin atribuir automáticamente al CISO la ejecución de cada control.

**Problema y controversia.** El escenario que conviene examinar es el siguiente: la certificación se confunde con garantía de disponibilidad. El lector debe reconocer que una solución aparentemente correcta puede introducir nuevos riesgos, costos o dependencias. La discusión debe explorar al menos dos alternativas y sus efectos sobre personas, procesos, datos, tecnología y terceros. También debe separar hechos de hipótesis, controles configurados de controles probados, y señales de alerta de incidentes confirmados. Cuando intervengan agentes de IA, se analizarán permisos, límites de autonomía, supervisión y trazabilidad, sin convertir la automatización en sustituto del juicio responsable.

**Aplicación formativa.** El participante trabajará un caso realista y elaborará evaluación de continuidad y mejora. Tendrá que definir el alcance, identificar activos y procesos afectados, documentar supuestos, asignar responsables y describir condiciones de entrada, éxito y reversión. La propuesta debe poder explicarse tanto a especialistas técnicos como a responsables de negocio. Para evitar soluciones decorativas, deberá incluir una prueba, simulación o procedimiento de revisión que permita observar resultados. Cuando el riesgo residual exceda los límites autorizados, se exigirá escalamiento a la autoridad correspondiente y registro de la decisión.

**Resultado esperado y evaluación.** El ensayo debe concluir con una recomendación ejecutable, sus dependencias, una explicación de por qué se eligió y qué evidencia podría refutarla. La evaluación del aprendizaje considerará precisión conceptual, razonamiento causal, viabilidad, evidencia, límites y comunicación. La relación con las otras unidades de GM-24 debe hacerse explícita: la estrategia y el gobierno del riesgo condicionan la arquitectura; la operación produce observaciones; la respuesta y la recuperación aportan lecciones para revisar el programa. El valor de «ISO 22301» se demuestra cuando mejora una decisión y una capacidad verificable, no cuando aumenta la cantidad de documentos, herramientas o reuniones. La pregunta abierta es qué cambiaría la recomendación ante un incidente, un nuevo requisito o una dependencia inesperada.

**Pregunta generadora:** ¿Qué decisión y qué evidencia demostrarían la utilidad de «ISO 22301» en una organización concreta?

---

### 225. M6.1-K05 — Pruebas Continuidad

**Unidad:** M6.1 · **Palabras:** 409 · **Estado:** idea central propuesta.

**Tesis central.** Las pruebas de continuidad deben demostrar capacidades bajo escenarios relevantes y revelar brechas antes de una crisis real. En el contexto del Programa Ejecutivo TheNextCISO, «Pruebas Continuidad» no debe abordarse como una etiqueta de producto ni como una lista de pasos aislados. El ensayo debe explicar qué capacidad necesita desarrollar quien lidera la seguridad, cuál es su propósito empresarial y qué relación mantiene con el riesgo. Es esencial distinguir el mandato de gobierno —apetito, prioridades, responsabilidades y autoridad— de la gestión que diseña, opera y verifica la práctica. Esta distinción permite analizar decisiones sin atribuir automáticamente al CISO la ejecución de cada control.

**Problema y controversia.** El escenario que conviene examinar es el siguiente: el ejercicio se limita a revisar documentos sin activar equipos. El lector debe reconocer que una solución aparentemente correcta puede introducir nuevos riesgos, costos o dependencias. La discusión debe explorar al menos dos alternativas y sus efectos sobre personas, procesos, datos, tecnología y terceros. También debe separar hechos de hipótesis, controles configurados de controles probados, y señales de alerta de incidentes confirmados. Cuando intervengan agentes de IA, se analizarán permisos, límites de autonomía, supervisión y trazabilidad, sin convertir la automatización en sustituto del juicio responsable.

**Aplicación formativa.** El participante trabajará un caso realista y elaborará plan de ejercicios, resultados y correcciones. Tendrá que definir el alcance, identificar activos y procesos afectados, documentar supuestos, asignar responsables y describir condiciones de entrada, éxito y reversión. La propuesta debe poder explicarse tanto a especialistas técnicos como a responsables de negocio. Para evitar soluciones decorativas, deberá incluir una prueba, simulación o procedimiento de revisión que permita observar resultados. Cuando el riesgo residual exceda los límites autorizados, se exigirá escalamiento a la autoridad correspondiente y registro de la decisión.

**Resultado esperado y evaluación.** El ensayo debe concluir con una recomendación ejecutable, sus dependencias, una explicación de por qué se eligió y qué evidencia podría refutarla. La evaluación del aprendizaje considerará precisión conceptual, razonamiento causal, viabilidad, evidencia, límites y comunicación. La relación con las otras unidades de GM-24 debe hacerse explícita: la estrategia y el gobierno del riesgo condicionan la arquitectura; la operación produce observaciones; la respuesta y la recuperación aportan lecciones para revisar el programa. El valor de «Pruebas Continuidad» se demuestra cuando mejora una decisión y una capacidad verificable, no cuando aumenta la cantidad de documentos, herramientas o reuniones. La pregunta abierta es qué cambiaría la recomendación ante un incidente, un nuevo requisito o una dependencia inesperada.

**Pregunta generadora:** ¿Qué decisión y qué evidencia demostrarían la utilidad de «Pruebas Continuidad» en una organización concreta?

---

### 226. M6.1-K06 — Backups Inmutables

**Unidad:** M6.1 · **Palabras:** 407 · **Estado:** idea central propuesta.

**Tesis central.** Los backups inmutables reducen la posibilidad de alteración maliciosa, pero requieren aislamiento, claves, retención y pruebas de restauración. En el contexto del Programa Ejecutivo TheNextCISO, «Backups Inmutables» no debe abordarse como una etiqueta de producto ni como una lista de pasos aislados. El ensayo debe explicar qué capacidad necesita desarrollar quien lidera la seguridad, cuál es su propósito empresarial y qué relación mantiene con el riesgo. Es esencial distinguir el mandato de gobierno —apetito, prioridades, responsabilidades y autoridad— de la gestión que diseña, opera y verifica la práctica. Esta distinción permite analizar decisiones sin atribuir automáticamente al CISO la ejecución de cada control.

**Problema y controversia.** El escenario que conviene examinar es el siguiente: se presume recuperabilidad porque existe copia inmutable. El lector debe reconocer que una solución aparentemente correcta puede introducir nuevos riesgos, costos o dependencias. La discusión debe explorar al menos dos alternativas y sus efectos sobre personas, procesos, datos, tecnología y terceros. También debe separar hechos de hipótesis, controles configurados de controles probados, y señales de alerta de incidentes confirmados. Cuando intervengan agentes de IA, se analizarán permisos, límites de autonomía, supervisión y trazabilidad, sin convertir la automatización en sustituto del juicio responsable.

**Aplicación formativa.** El participante trabajará un caso realista y elaborará diseño de backup y prueba de restore. Tendrá que definir el alcance, identificar activos y procesos afectados, documentar supuestos, asignar responsables y describir condiciones de entrada, éxito y reversión. La propuesta debe poder explicarse tanto a especialistas técnicos como a responsables de negocio. Para evitar soluciones decorativas, deberá incluir una prueba, simulación o procedimiento de revisión que permita observar resultados. Cuando el riesgo residual exceda los límites autorizados, se exigirá escalamiento a la autoridad correspondiente y registro de la decisión.

**Resultado esperado y evaluación.** El ensayo debe concluir con una recomendación ejecutable, sus dependencias, una explicación de por qué se eligió y qué evidencia podría refutarla. La evaluación del aprendizaje considerará precisión conceptual, razonamiento causal, viabilidad, evidencia, límites y comunicación. La relación con las otras unidades de GM-24 debe hacerse explícita: la estrategia y el gobierno del riesgo condicionan la arquitectura; la operación produce observaciones; la respuesta y la recuperación aportan lecciones para revisar el programa. El valor de «Backups Inmutables» se demuestra cuando mejora una decisión y una capacidad verificable, no cuando aumenta la cantidad de documentos, herramientas o reuniones. La pregunta abierta es qué cambiaría la recomendación ante un incidente, un nuevo requisito o una dependencia inesperada.

**Pregunta generadora:** ¿Qué decisión y qué evidencia demostrarían la utilidad de «Backups Inmutables» en una organización concreta?

---

### 227. M6.1-K07 — Alta Disponibilidad

**Unidad:** M6.1 · **Palabras:** 407 · **Estado:** idea central propuesta.

**Tesis central.** La alta disponibilidad reduce interrupciones por fallas específicas, pero no reemplaza continuidad ni recuperación frente a corrupción o ataques. En el contexto del Programa Ejecutivo TheNextCISO, «Alta Disponibilidad» no debe abordarse como una etiqueta de producto ni como una lista de pasos aislados. El ensayo debe explicar qué capacidad necesita desarrollar quien lidera la seguridad, cuál es su propósito empresarial y qué relación mantiene con el riesgo. Es esencial distinguir el mandato de gobierno —apetito, prioridades, responsabilidades y autoridad— de la gestión que diseña, opera y verifica la práctica. Esta distinción permite analizar decisiones sin atribuir automáticamente al CISO la ejecución de cada control.

**Problema y controversia.** El escenario que conviene examinar es el siguiente: la replicación propaga datos cifrados por ransomware. El lector debe reconocer que una solución aparentemente correcta puede introducir nuevos riesgos, costos o dependencias. La discusión debe explorar al menos dos alternativas y sus efectos sobre personas, procesos, datos, tecnología y terceros. También debe separar hechos de hipótesis, controles configurados de controles probados, y señales de alerta de incidentes confirmados. Cuando intervengan agentes de IA, se analizarán permisos, límites de autonomía, supervisión y trazabilidad, sin convertir la automatización en sustituto del juicio responsable.

**Aplicación formativa.** El participante trabajará un caso realista y elaborará modelo de fallas, redundancia y recuperación. Tendrá que definir el alcance, identificar activos y procesos afectados, documentar supuestos, asignar responsables y describir condiciones de entrada, éxito y reversión. La propuesta debe poder explicarse tanto a especialistas técnicos como a responsables de negocio. Para evitar soluciones decorativas, deberá incluir una prueba, simulación o procedimiento de revisión que permita observar resultados. Cuando el riesgo residual exceda los límites autorizados, se exigirá escalamiento a la autoridad correspondiente y registro de la decisión.

**Resultado esperado y evaluación.** El ensayo debe concluir con una recomendación ejecutable, sus dependencias, una explicación de por qué se eligió y qué evidencia podría refutarla. La evaluación del aprendizaje considerará precisión conceptual, razonamiento causal, viabilidad, evidencia, límites y comunicación. La relación con las otras unidades de GM-24 debe hacerse explícita: la estrategia y el gobierno del riesgo condicionan la arquitectura; la operación produce observaciones; la respuesta y la recuperación aportan lecciones para revisar el programa. El valor de «Alta Disponibilidad» se demuestra cuando mejora una decisión y una capacidad verificable, no cuando aumenta la cantidad de documentos, herramientas o reuniones. La pregunta abierta es qué cambiaría la recomendación ante un incidente, un nuevo requisito o una dependencia inesperada.

**Pregunta generadora:** ¿Qué decisión y qué evidencia demostrarían la utilidad de «Alta Disponibilidad» en una organización concreta?

---

### 228. M6.1-K08 — Sitio Alternativo

**Unidad:** M6.1 · **Palabras:** 409 · **Estado:** idea central propuesta.

**Tesis central.** Un sitio alternativo permite sostener o recuperar servicios bajo condiciones de indisponibilidad del entorno principal, con dependencias probadas. En el contexto del Programa Ejecutivo TheNextCISO, «Sitio Alternativo» no debe abordarse como una etiqueta de producto ni como una lista de pasos aislados. El ensayo debe explicar qué capacidad necesita desarrollar quien lidera la seguridad, cuál es su propósito empresarial y qué relación mantiene con el riesgo. Es esencial distinguir el mandato de gobierno —apetito, prioridades, responsabilidades y autoridad— de la gestión que diseña, opera y verifica la práctica. Esta distinción permite analizar decisiones sin atribuir automáticamente al CISO la ejecución de cada control.

**Problema y controversia.** El escenario que conviene examinar es el siguiente: el sitio alternativo comparte la misma identidad o conectividad fallida. El lector debe reconocer que una solución aparentemente correcta puede introducir nuevos riesgos, costos o dependencias. La discusión debe explorar al menos dos alternativas y sus efectos sobre personas, procesos, datos, tecnología y terceros. También debe separar hechos de hipótesis, controles configurados de controles probados, y señales de alerta de incidentes confirmados. Cuando intervengan agentes de IA, se analizarán permisos, límites de autonomía, supervisión y trazabilidad, sin convertir la automatización en sustituto del juicio responsable.

**Aplicación formativa.** El participante trabajará un caso realista y elaborará plan de activación, pruebas y costos. Tendrá que definir el alcance, identificar activos y procesos afectados, documentar supuestos, asignar responsables y describir condiciones de entrada, éxito y reversión. La propuesta debe poder explicarse tanto a especialistas técnicos como a responsables de negocio. Para evitar soluciones decorativas, deberá incluir una prueba, simulación o procedimiento de revisión que permita observar resultados. Cuando el riesgo residual exceda los límites autorizados, se exigirá escalamiento a la autoridad correspondiente y registro de la decisión.

**Resultado esperado y evaluación.** El ensayo debe concluir con una recomendación ejecutable, sus dependencias, una explicación de por qué se eligió y qué evidencia podría refutarla. La evaluación del aprendizaje considerará precisión conceptual, razonamiento causal, viabilidad, evidencia, límites y comunicación. La relación con las otras unidades de GM-24 debe hacerse explícita: la estrategia y el gobierno del riesgo condicionan la arquitectura; la operación produce observaciones; la respuesta y la recuperación aportan lecciones para revisar el programa. El valor de «Sitio Alternativo» se demuestra cuando mejora una decisión y una capacidad verificable, no cuando aumenta la cantidad de documentos, herramientas o reuniones. La pregunta abierta es qué cambiaría la recomendación ante un incidente, un nuevo requisito o una dependencia inesperada.

**Pregunta generadora:** ¿Qué decisión y qué evidencia demostrarían la utilidad de «Sitio Alternativo» en una organización concreta?

---

### 229. M6.1-K09 — Gestión Crisis (Negocio)

**Unidad:** M6.1 · **Palabras:** 411 · **Estado:** idea central propuesta.

**Tesis central.** La gestión de crisis coordina decisiones empresariales, comunicación y prioridades durante perturbaciones más allá de la respuesta técnica. En el contexto del Programa Ejecutivo TheNextCISO, «Gestión Crisis (Negocio)» no debe abordarse como una etiqueta de producto ni como una lista de pasos aislados. El ensayo debe explicar qué capacidad necesita desarrollar quien lidera la seguridad, cuál es su propósito empresarial y qué relación mantiene con el riesgo. Es esencial distinguir el mandato de gobierno —apetito, prioridades, responsabilidades y autoridad— de la gestión que diseña, opera y verifica la práctica. Esta distinción permite analizar decisiones sin atribuir automáticamente al CISO la ejecución de cada control.

**Problema y controversia.** El escenario que conviene examinar es el siguiente: el SOC decide restauración sin consultar prioridades del negocio. El lector debe reconocer que una solución aparentemente correcta puede introducir nuevos riesgos, costos o dependencias. La discusión debe explorar al menos dos alternativas y sus efectos sobre personas, procesos, datos, tecnología y terceros. También debe separar hechos de hipótesis, controles configurados de controles probados, y señales de alerta de incidentes confirmados. Cuando intervengan agentes de IA, se analizarán permisos, límites de autonomía, supervisión y trazabilidad, sin convertir la automatización en sustituto del juicio responsable.

**Aplicación formativa.** El participante trabajará un caso realista y elaborará estructura de crisis y criterios de decisión. Tendrá que definir el alcance, identificar activos y procesos afectados, documentar supuestos, asignar responsables y describir condiciones de entrada, éxito y reversión. La propuesta debe poder explicarse tanto a especialistas técnicos como a responsables de negocio. Para evitar soluciones decorativas, deberá incluir una prueba, simulación o procedimiento de revisión que permita observar resultados. Cuando el riesgo residual exceda los límites autorizados, se exigirá escalamiento a la autoridad correspondiente y registro de la decisión.

**Resultado esperado y evaluación.** El ensayo debe concluir con una recomendación ejecutable, sus dependencias, una explicación de por qué se eligió y qué evidencia podría refutarla. La evaluación del aprendizaje considerará precisión conceptual, razonamiento causal, viabilidad, evidencia, límites y comunicación. La relación con las otras unidades de GM-24 debe hacerse explícita: la estrategia y el gobierno del riesgo condicionan la arquitectura; la operación produce observaciones; la respuesta y la recuperación aportan lecciones para revisar el programa. El valor de «Gestión Crisis (Negocio)» se demuestra cuando mejora una decisión y una capacidad verificable, no cuando aumenta la cantidad de documentos, herramientas o reuniones. La pregunta abierta es qué cambiaría la recomendación ante un incidente, un nuevo requisito o una dependencia inesperada.

**Pregunta generadora:** ¿Qué decisión y qué evidencia demostrarían la utilidad de «Gestión Crisis (Negocio)» en una organización concreta?

---

### 230. M6.1-K10 — Dependencias

**Unidad:** M6.1 · **Palabras:** 403 · **Estado:** idea central propuesta.

**Tesis central.** Las dependencias de servicios, datos, personas y terceros determinan qué puede recuperarse y en qué secuencia. En el contexto del Programa Ejecutivo TheNextCISO, «Dependencias» no debe abordarse como una etiqueta de producto ni como una lista de pasos aislados. El ensayo debe explicar qué capacidad necesita desarrollar quien lidera la seguridad, cuál es su propósito empresarial y qué relación mantiene con el riesgo. Es esencial distinguir el mandato de gobierno —apetito, prioridades, responsabilidades y autoridad— de la gestión que diseña, opera y verifica la práctica. Esta distinción permite analizar decisiones sin atribuir automáticamente al CISO la ejecución de cada control.

**Problema y controversia.** El escenario que conviene examinar es el siguiente: un componente pequeño bloquea múltiples servicios críticos. El lector debe reconocer que una solución aparentemente correcta puede introducir nuevos riesgos, costos o dependencias. La discusión debe explorar al menos dos alternativas y sus efectos sobre personas, procesos, datos, tecnología y terceros. También debe separar hechos de hipótesis, controles configurados de controles probados, y señales de alerta de incidentes confirmados. Cuando intervengan agentes de IA, se analizarán permisos, límites de autonomía, supervisión y trazabilidad, sin convertir la automatización en sustituto del juicio responsable.

**Aplicación formativa.** El participante trabajará un caso realista y elaborará grafo de dependencias y pruebas de recuperación. Tendrá que definir el alcance, identificar activos y procesos afectados, documentar supuestos, asignar responsables y describir condiciones de entrada, éxito y reversión. La propuesta debe poder explicarse tanto a especialistas técnicos como a responsables de negocio. Para evitar soluciones decorativas, deberá incluir una prueba, simulación o procedimiento de revisión que permita observar resultados. Cuando el riesgo residual exceda los límites autorizados, se exigirá escalamiento a la autoridad correspondiente y registro de la decisión.

**Resultado esperado y evaluación.** El ensayo debe concluir con una recomendación ejecutable, sus dependencias, una explicación de por qué se eligió y qué evidencia podría refutarla. La evaluación del aprendizaje considerará precisión conceptual, razonamiento causal, viabilidad, evidencia, límites y comunicación. La relación con las otras unidades de GM-24 debe hacerse explícita: la estrategia y el gobierno del riesgo condicionan la arquitectura; la operación produce observaciones; la respuesta y la recuperación aportan lecciones para revisar el programa. El valor de «Dependencias» se demuestra cuando mejora una decisión y una capacidad verificable, no cuando aumenta la cantidad de documentos, herramientas o reuniones. La pregunta abierta es qué cambiaría la recomendación ante un incidente, un nuevo requisito o una dependencia inesperada.

**Pregunta generadora:** ¿Qué decisión y qué evidencia demostrarían la utilidad de «Dependencias» en una organización concreta?

---

## M6.2 — Seguridad en Redes, Nube, Tecnologías Emergentes y SCRM

### 231. M6.2-K01 — C-SCRM (Cadena Suministro)

**Unidad:** M6.2 · **Palabras:** 410 · **Estado:** idea central propuesta.

**Tesis central.** La gestión del riesgo de cadena de suministro examina dependencias, integridad, contratos y continuidad de proveedores y componentes. En el contexto del Programa Ejecutivo TheNextCISO, «C-SCRM (Cadena Suministro)» no debe abordarse como una etiqueta de producto ni como una lista de pasos aislados. El ensayo debe explicar qué capacidad necesita desarrollar quien lidera la seguridad, cuál es su propósito empresarial y qué relación mantiene con el riesgo. Es esencial distinguir el mandato de gobierno —apetito, prioridades, responsabilidades y autoridad— de la gestión que diseña, opera y verifica la práctica. Esta distinción permite analizar decisiones sin atribuir automáticamente al CISO la ejecución de cada control.

**Problema y controversia.** El escenario que conviene examinar es el siguiente: una evaluación inicial no detecta cambios posteriores de subproveedores. El lector debe reconocer que una solución aparentemente correcta puede introducir nuevos riesgos, costos o dependencias. La discusión debe explorar al menos dos alternativas y sus efectos sobre personas, procesos, datos, tecnología y terceros. También debe separar hechos de hipótesis, controles configurados de controles probados, y señales de alerta de incidentes confirmados. Cuando intervengan agentes de IA, se analizarán permisos, límites de autonomía, supervisión y trazabilidad, sin convertir la automatización en sustituto del juicio responsable.

**Aplicación formativa.** El participante trabajará un caso realista y elaborará mapa de dependencias, contratos y controles. Tendrá que definir el alcance, identificar activos y procesos afectados, documentar supuestos, asignar responsables y describir condiciones de entrada, éxito y reversión. La propuesta debe poder explicarse tanto a especialistas técnicos como a responsables de negocio. Para evitar soluciones decorativas, deberá incluir una prueba, simulación o procedimiento de revisión que permita observar resultados. Cuando el riesgo residual exceda los límites autorizados, se exigirá escalamiento a la autoridad correspondiente y registro de la decisión.

**Resultado esperado y evaluación.** El ensayo debe concluir con una recomendación ejecutable, sus dependencias, una explicación de por qué se eligió y qué evidencia podría refutarla. La evaluación del aprendizaje considerará precisión conceptual, razonamiento causal, viabilidad, evidencia, límites y comunicación. La relación con las otras unidades de GM-24 debe hacerse explícita: la estrategia y el gobierno del riesgo condicionan la arquitectura; la operación produce observaciones; la respuesta y la recuperación aportan lecciones para revisar el programa. El valor de «C-SCRM (Cadena Suministro)» se demuestra cuando mejora una decisión y una capacidad verificable, no cuando aumenta la cantidad de documentos, herramientas o reuniones. La pregunta abierta es qué cambiaría la recomendación ante un incidente, un nuevo requisito o una dependencia inesperada.

**Pregunta generadora:** ¿Qué decisión y qué evidencia demostrarían la utilidad de «C-SCRM (Cadena Suministro)» en una organización concreta?

---

### 232. M6.2-K02 — Seguridad Nube

**Unidad:** M6.2 · **Palabras:** 409 · **Estado:** idea central propuesta.

**Tesis central.** La seguridad cloud combina responsabilidad compartida, identidad, configuración, datos y protección de workloads en arquitecturas dinámicas. En el contexto del Programa Ejecutivo TheNextCISO, «Seguridad Nube» no debe abordarse como una etiqueta de producto ni como una lista de pasos aislados. El ensayo debe explicar qué capacidad necesita desarrollar quien lidera la seguridad, cuál es su propósito empresarial y qué relación mantiene con el riesgo. Es esencial distinguir el mandato de gobierno —apetito, prioridades, responsabilidades y autoridad— de la gestión que diseña, opera y verifica la práctica. Esta distinción permite analizar decisiones sin atribuir automáticamente al CISO la ejecución de cada control.

**Problema y controversia.** El escenario que conviene examinar es el siguiente: se asume que el proveedor cubre todas las responsabilidades del cliente. El lector debe reconocer que una solución aparentemente correcta puede introducir nuevos riesgos, costos o dependencias. La discusión debe explorar al menos dos alternativas y sus efectos sobre personas, procesos, datos, tecnología y terceros. También debe separar hechos de hipótesis, controles configurados de controles probados, y señales de alerta de incidentes confirmados. Cuando intervengan agentes de IA, se analizarán permisos, límites de autonomía, supervisión y trazabilidad, sin convertir la automatización en sustituto del juicio responsable.

**Aplicación formativa.** El participante trabajará un caso realista y elaborará matriz de responsabilidades y controles por workload. Tendrá que definir el alcance, identificar activos y procesos afectados, documentar supuestos, asignar responsables y describir condiciones de entrada, éxito y reversión. La propuesta debe poder explicarse tanto a especialistas técnicos como a responsables de negocio. Para evitar soluciones decorativas, deberá incluir una prueba, simulación o procedimiento de revisión que permita observar resultados. Cuando el riesgo residual exceda los límites autorizados, se exigirá escalamiento a la autoridad correspondiente y registro de la decisión.

**Resultado esperado y evaluación.** El ensayo debe concluir con una recomendación ejecutable, sus dependencias, una explicación de por qué se eligió y qué evidencia podría refutarla. La evaluación del aprendizaje considerará precisión conceptual, razonamiento causal, viabilidad, evidencia, límites y comunicación. La relación con las otras unidades de GM-24 debe hacerse explícita: la estrategia y el gobierno del riesgo condicionan la arquitectura; la operación produce observaciones; la respuesta y la recuperación aportan lecciones para revisar el programa. El valor de «Seguridad Nube» se demuestra cuando mejora una decisión y una capacidad verificable, no cuando aumenta la cantidad de documentos, herramientas o reuniones. La pregunta abierta es qué cambiaría la recomendación ante un incidente, un nuevo requisito o una dependencia inesperada.

**Pregunta generadora:** ¿Qué decisión y qué evidencia demostrarían la utilidad de «Seguridad Nube» en una organización concreta?

---

### 233. M6.2-K03 — DevSecOps

**Unidad:** M6.2 · **Palabras:** 407 · **Estado:** idea central propuesta.

**Tesis central.** DevSecOps integra controles y evidencia de seguridad en desarrollo y entrega continua sin convertir cada pipeline en una barrera burocrática. En el contexto del Programa Ejecutivo TheNextCISO, «DevSecOps» no debe abordarse como una etiqueta de producto ni como una lista de pasos aislados. El ensayo debe explicar qué capacidad necesita desarrollar quien lidera la seguridad, cuál es su propósito empresarial y qué relación mantiene con el riesgo. Es esencial distinguir el mandato de gobierno —apetito, prioridades, responsabilidades y autoridad— de la gestión que diseña, opera y verifica la práctica. Esta distinción permite analizar decisiones sin atribuir automáticamente al CISO la ejecución de cada control.

**Problema y controversia.** El escenario que conviene examinar es el siguiente: un escaneo se considera garantía de código seguro. El lector debe reconocer que una solución aparentemente correcta puede introducir nuevos riesgos, costos o dependencias. La discusión debe explorar al menos dos alternativas y sus efectos sobre personas, procesos, datos, tecnología y terceros. También debe separar hechos de hipótesis, controles configurados de controles probados, y señales de alerta de incidentes confirmados. Cuando intervengan agentes de IA, se analizarán permisos, límites de autonomía, supervisión y trazabilidad, sin convertir la automatización en sustituto del juicio responsable.

**Aplicación formativa.** El participante trabajará un caso realista y elaborará pipeline con gates, excepciones y trazabilidad. Tendrá que definir el alcance, identificar activos y procesos afectados, documentar supuestos, asignar responsables y describir condiciones de entrada, éxito y reversión. La propuesta debe poder explicarse tanto a especialistas técnicos como a responsables de negocio. Para evitar soluciones decorativas, deberá incluir una prueba, simulación o procedimiento de revisión que permita observar resultados. Cuando el riesgo residual exceda los límites autorizados, se exigirá escalamiento a la autoridad correspondiente y registro de la decisión.

**Resultado esperado y evaluación.** El ensayo debe concluir con una recomendación ejecutable, sus dependencias, una explicación de por qué se eligió y qué evidencia podría refutarla. La evaluación del aprendizaje considerará precisión conceptual, razonamiento causal, viabilidad, evidencia, límites y comunicación. La relación con las otras unidades de GM-24 debe hacerse explícita: la estrategia y el gobierno del riesgo condicionan la arquitectura; la operación produce observaciones; la respuesta y la recuperación aportan lecciones para revisar el programa. El valor de «DevSecOps» se demuestra cuando mejora una decisión y una capacidad verificable, no cuando aumenta la cantidad de documentos, herramientas o reuniones. La pregunta abierta es qué cambiaría la recomendación ante un incidente, un nuevo requisito o una dependencia inesperada.

**Pregunta generadora:** ¿Qué decisión y qué evidencia demostrarían la utilidad de «DevSecOps» en una organización concreta?

---

### 234. M6.2-K04 — Seguridad IA

**Unidad:** M6.2 · **Palabras:** 411 · **Estado:** idea central propuesta.

**Tesis central.** La seguridad de IA protege modelos, datos, herramientas, agentes y procesos ante amenazas específicas y consecuencias de autonomía. En el contexto del Programa Ejecutivo TheNextCISO, «Seguridad IA» no debe abordarse como una etiqueta de producto ni como una lista de pasos aislados. El ensayo debe explicar qué capacidad necesita desarrollar quien lidera la seguridad, cuál es su propósito empresarial y qué relación mantiene con el riesgo. Es esencial distinguir el mandato de gobierno —apetito, prioridades, responsabilidades y autoridad— de la gestión que diseña, opera y verifica la práctica. Esta distinción permite analizar decisiones sin atribuir automáticamente al CISO la ejecución de cada control.

**Problema y controversia.** El escenario que conviene examinar es el siguiente: se protege solo el modelo y se ignoran permisos de herramientas. El lector debe reconocer que una solución aparentemente correcta puede introducir nuevos riesgos, costos o dependencias. La discusión debe explorar al menos dos alternativas y sus efectos sobre personas, procesos, datos, tecnología y terceros. También debe separar hechos de hipótesis, controles configurados de controles probados, y señales de alerta de incidentes confirmados. Cuando intervengan agentes de IA, se analizarán permisos, límites de autonomía, supervisión y trazabilidad, sin convertir la automatización en sustituto del juicio responsable.

**Aplicación formativa.** El participante trabajará un caso realista y elaborará modelo de amenazas y controles de agentes. Tendrá que definir el alcance, identificar activos y procesos afectados, documentar supuestos, asignar responsables y describir condiciones de entrada, éxito y reversión. La propuesta debe poder explicarse tanto a especialistas técnicos como a responsables de negocio. Para evitar soluciones decorativas, deberá incluir una prueba, simulación o procedimiento de revisión que permita observar resultados. Cuando el riesgo residual exceda los límites autorizados, se exigirá escalamiento a la autoridad correspondiente y registro de la decisión.

**Resultado esperado y evaluación.** El ensayo debe concluir con una recomendación ejecutable, sus dependencias, una explicación de por qué se eligió y qué evidencia podría refutarla. La evaluación del aprendizaje considerará precisión conceptual, razonamiento causal, viabilidad, evidencia, límites y comunicación. La relación con las otras unidades de GM-24 debe hacerse explícita: la estrategia y el gobierno del riesgo condicionan la arquitectura; la operación produce observaciones; la respuesta y la recuperación aportan lecciones para revisar el programa. El valor de «Seguridad IA» se demuestra cuando mejora una decisión y una capacidad verificable, no cuando aumenta la cantidad de documentos, herramientas o reuniones. La pregunta abierta es qué cambiaría la recomendación ante un incidente, un nuevo requisito o una dependencia inesperada.

**Pregunta generadora:** ¿Qué decisión y qué evidencia demostrarían la utilidad de «Seguridad IA» en una organización concreta?

---

### 235. M6.2-K05 — IoT/OT Security

**Unidad:** M6.2 · **Palabras:** 409 · **Estado:** idea central propuesta.

**Tesis central.** La seguridad IoT y OT debe preservar seguridad física, disponibilidad y control de procesos además de confidencialidad digital. En el contexto del Programa Ejecutivo TheNextCISO, «IoT/OT Security» no debe abordarse como una etiqueta de producto ni como una lista de pasos aislados. El ensayo debe explicar qué capacidad necesita desarrollar quien lidera la seguridad, cuál es su propósito empresarial y qué relación mantiene con el riesgo. Es esencial distinguir el mandato de gobierno —apetito, prioridades, responsabilidades y autoridad— de la gestión que diseña, opera y verifica la práctica. Esta distinción permite analizar decisiones sin atribuir automáticamente al CISO la ejecución de cada control.

**Problema y controversia.** El escenario que conviene examinar es el siguiente: un parche urgente interrumpe un proceso industrial crítico. El lector debe reconocer que una solución aparentemente correcta puede introducir nuevos riesgos, costos o dependencias. La discusión debe explorar al menos dos alternativas y sus efectos sobre personas, procesos, datos, tecnología y terceros. También debe separar hechos de hipótesis, controles configurados de controles probados, y señales de alerta de incidentes confirmados. Cuando intervengan agentes de IA, se analizarán permisos, límites de autonomía, supervisión y trazabilidad, sin convertir la automatización en sustituto del juicio responsable.

**Aplicación formativa.** El participante trabajará un caso realista y elaborará plan de segmentación, monitoreo y cambios. Tendrá que definir el alcance, identificar activos y procesos afectados, documentar supuestos, asignar responsables y describir condiciones de entrada, éxito y reversión. La propuesta debe poder explicarse tanto a especialistas técnicos como a responsables de negocio. Para evitar soluciones decorativas, deberá incluir una prueba, simulación o procedimiento de revisión que permita observar resultados. Cuando el riesgo residual exceda los límites autorizados, se exigirá escalamiento a la autoridad correspondiente y registro de la decisión.

**Resultado esperado y evaluación.** El ensayo debe concluir con una recomendación ejecutable, sus dependencias, una explicación de por qué se eligió y qué evidencia podría refutarla. La evaluación del aprendizaje considerará precisión conceptual, razonamiento causal, viabilidad, evidencia, límites y comunicación. La relación con las otras unidades de GM-24 debe hacerse explícita: la estrategia y el gobierno del riesgo condicionan la arquitectura; la operación produce observaciones; la respuesta y la recuperación aportan lecciones para revisar el programa. El valor de «IoT/OT Security» se demuestra cuando mejora una decisión y una capacidad verificable, no cuando aumenta la cantidad de documentos, herramientas o reuniones. La pregunta abierta es qué cambiaría la recomendación ante un incidente, un nuevo requisito o una dependencia inesperada.

**Pregunta generadora:** ¿Qué decisión y qué evidencia demostrarían la utilidad de «IoT/OT Security» en una organización concreta?

---

### 236. M6.2-K06 — Shadow AI

**Unidad:** M6.2 · **Palabras:** 414 · **Estado:** idea central propuesta.

**Tesis central.** Shadow AI surge cuando personas y equipos utilizan herramientas de IA fuera del gobierno previsto, generando exposición de datos y decisiones. En el contexto del Programa Ejecutivo TheNextCISO, «Shadow AI» no debe abordarse como una etiqueta de producto ni como una lista de pasos aislados. El ensayo debe explicar qué capacidad necesita desarrollar quien lidera la seguridad, cuál es su propósito empresarial y qué relación mantiene con el riesgo. Es esencial distinguir el mandato de gobierno —apetito, prioridades, responsabilidades y autoridad— de la gestión que diseña, opera y verifica la práctica. Esta distinción permite analizar decisiones sin atribuir automáticamente al CISO la ejecución de cada control.

**Problema y controversia.** El escenario que conviene examinar es el siguiente: se prohíbe IA sin ofrecer alternativas seguras y el uso oculto aumenta. El lector debe reconocer que una solución aparentemente correcta puede introducir nuevos riesgos, costos o dependencias. La discusión debe explorar al menos dos alternativas y sus efectos sobre personas, procesos, datos, tecnología y terceros. También debe separar hechos de hipótesis, controles configurados de controles probados, y señales de alerta de incidentes confirmados. Cuando intervengan agentes de IA, se analizarán permisos, límites de autonomía, supervisión y trazabilidad, sin convertir la automatización en sustituto del juicio responsable.

**Aplicación formativa.** El participante trabajará un caso realista y elaborará estrategia de descubrimiento, política y habilitación. Tendrá que definir el alcance, identificar activos y procesos afectados, documentar supuestos, asignar responsables y describir condiciones de entrada, éxito y reversión. La propuesta debe poder explicarse tanto a especialistas técnicos como a responsables de negocio. Para evitar soluciones decorativas, deberá incluir una prueba, simulación o procedimiento de revisión que permita observar resultados. Cuando el riesgo residual exceda los límites autorizados, se exigirá escalamiento a la autoridad correspondiente y registro de la decisión.

**Resultado esperado y evaluación.** El ensayo debe concluir con una recomendación ejecutable, sus dependencias, una explicación de por qué se eligió y qué evidencia podría refutarla. La evaluación del aprendizaje considerará precisión conceptual, razonamiento causal, viabilidad, evidencia, límites y comunicación. La relación con las otras unidades de GM-24 debe hacerse explícita: la estrategia y el gobierno del riesgo condicionan la arquitectura; la operación produce observaciones; la respuesta y la recuperación aportan lecciones para revisar el programa. El valor de «Shadow AI» se demuestra cuando mejora una decisión y una capacidad verificable, no cuando aumenta la cantidad de documentos, herramientas o reuniones. La pregunta abierta es qué cambiaría la recomendación ante un incidente, un nuevo requisito o una dependencia inesperada.

**Pregunta generadora:** ¿Qué decisión y qué evidencia demostrarían la utilidad de «Shadow AI» en una organización concreta?

---

### 237. M6.2-K07 — Responsabilidad Compartida

**Unidad:** M6.2 · **Palabras:** 407 · **Estado:** idea central propuesta.

**Tesis central.** La responsabilidad compartida exige asignar controles entre proveedor, cliente, integradores y operadores según servicio y contrato. En el contexto del Programa Ejecutivo TheNextCISO, «Responsabilidad Compartida» no debe abordarse como una etiqueta de producto ni como una lista de pasos aislados. El ensayo debe explicar qué capacidad necesita desarrollar quien lidera la seguridad, cuál es su propósito empresarial y qué relación mantiene con el riesgo. Es esencial distinguir el mandato de gobierno —apetito, prioridades, responsabilidades y autoridad— de la gestión que diseña, opera y verifica la práctica. Esta distinción permite analizar decisiones sin atribuir automáticamente al CISO la ejecución de cada control.

**Problema y controversia.** El escenario que conviene examinar es el siguiente: cada parte presume que la otra administra claves o incidentes. El lector debe reconocer que una solución aparentemente correcta puede introducir nuevos riesgos, costos o dependencias. La discusión debe explorar al menos dos alternativas y sus efectos sobre personas, procesos, datos, tecnología y terceros. También debe separar hechos de hipótesis, controles configurados de controles probados, y señales de alerta de incidentes confirmados. Cuando intervengan agentes de IA, se analizarán permisos, límites de autonomía, supervisión y trazabilidad, sin convertir la automatización en sustituto del juicio responsable.

**Aplicación formativa.** El participante trabajará un caso realista y elaborará RACI de controles y evidencias cloud. Tendrá que definir el alcance, identificar activos y procesos afectados, documentar supuestos, asignar responsables y describir condiciones de entrada, éxito y reversión. La propuesta debe poder explicarse tanto a especialistas técnicos como a responsables de negocio. Para evitar soluciones decorativas, deberá incluir una prueba, simulación o procedimiento de revisión que permita observar resultados. Cuando el riesgo residual exceda los límites autorizados, se exigirá escalamiento a la autoridad correspondiente y registro de la decisión.

**Resultado esperado y evaluación.** El ensayo debe concluir con una recomendación ejecutable, sus dependencias, una explicación de por qué se eligió y qué evidencia podría refutarla. La evaluación del aprendizaje considerará precisión conceptual, razonamiento causal, viabilidad, evidencia, límites y comunicación. La relación con las otras unidades de GM-24 debe hacerse explícita: la estrategia y el gobierno del riesgo condicionan la arquitectura; la operación produce observaciones; la respuesta y la recuperación aportan lecciones para revisar el programa. El valor de «Responsabilidad Compartida» se demuestra cuando mejora una decisión y una capacidad verificable, no cuando aumenta la cantidad de documentos, herramientas o reuniones. La pregunta abierta es qué cambiaría la recomendación ante un incidente, un nuevo requisito o una dependencia inesperada.

**Pregunta generadora:** ¿Qué decisión y qué evidencia demostrarían la utilidad de «Responsabilidad Compartida» en una organización concreta?

---

### 238. M6.2-K08 — Riesgo Terceros (TPRM)

**Unidad:** M6.2 · **Palabras:** 409 · **Estado:** idea central propuesta.

**Tesis central.** TPRM evalúa y supervisa riesgos de terceros durante selección, operación, cambios y salida, no solo al firmar contratos. En el contexto del Programa Ejecutivo TheNextCISO, «Riesgo Terceros (TPRM)» no debe abordarse como una etiqueta de producto ni como una lista de pasos aislados. El ensayo debe explicar qué capacidad necesita desarrollar quien lidera la seguridad, cuál es su propósito empresarial y qué relación mantiene con el riesgo. Es esencial distinguir el mandato de gobierno —apetito, prioridades, responsabilidades y autoridad— de la gestión que diseña, opera y verifica la práctica. Esta distinción permite analizar decisiones sin atribuir automáticamente al CISO la ejecución de cada control.

**Problema y controversia.** El escenario que conviene examinar es el siguiente: un proveedor crítico pierde controles sin activar revisión. El lector debe reconocer que una solución aparentemente correcta puede introducir nuevos riesgos, costos o dependencias. La discusión debe explorar al menos dos alternativas y sus efectos sobre personas, procesos, datos, tecnología y terceros. También debe separar hechos de hipótesis, controles configurados de controles probados, y señales de alerta de incidentes confirmados. Cuando intervengan agentes de IA, se analizarán permisos, límites de autonomía, supervisión y trazabilidad, sin convertir la automatización en sustituto del juicio responsable.

**Aplicación formativa.** El participante trabajará un caso realista y elaborará programa de due diligence y monitoreo. Tendrá que definir el alcance, identificar activos y procesos afectados, documentar supuestos, asignar responsables y describir condiciones de entrada, éxito y reversión. La propuesta debe poder explicarse tanto a especialistas técnicos como a responsables de negocio. Para evitar soluciones decorativas, deberá incluir una prueba, simulación o procedimiento de revisión que permita observar resultados. Cuando el riesgo residual exceda los límites autorizados, se exigirá escalamiento a la autoridad correspondiente y registro de la decisión.

**Resultado esperado y evaluación.** El ensayo debe concluir con una recomendación ejecutable, sus dependencias, una explicación de por qué se eligió y qué evidencia podría refutarla. La evaluación del aprendizaje considerará precisión conceptual, razonamiento causal, viabilidad, evidencia, límites y comunicación. La relación con las otras unidades de GM-24 debe hacerse explícita: la estrategia y el gobierno del riesgo condicionan la arquitectura; la operación produce observaciones; la respuesta y la recuperación aportan lecciones para revisar el programa. El valor de «Riesgo Terceros (TPRM)» se demuestra cuando mejora una decisión y una capacidad verificable, no cuando aumenta la cantidad de documentos, herramientas o reuniones. La pregunta abierta es qué cambiaría la recomendación ante un incidente, un nuevo requisito o una dependencia inesperada.

**Pregunta generadora:** ¿Qué decisión y qué evidencia demostrarían la utilidad de «Riesgo Terceros (TPRM)» en una organización concreta?

---

### 239. M6.2-K09 — SDLC Seguro

**Unidad:** M6.2 · **Palabras:** 407 · **Estado:** idea central propuesta.

**Tesis central.** El ciclo de desarrollo seguro integra requisitos, modelado de amenazas, implementación, pruebas y mantenimiento desde el diseño. En el contexto del Programa Ejecutivo TheNextCISO, «SDLC Seguro» no debe abordarse como una etiqueta de producto ni como una lista de pasos aislados. El ensayo debe explicar qué capacidad necesita desarrollar quien lidera la seguridad, cuál es su propósito empresarial y qué relación mantiene con el riesgo. Es esencial distinguir el mandato de gobierno —apetito, prioridades, responsabilidades y autoridad— de la gestión que diseña, opera y verifica la práctica. Esta distinción permite analizar decisiones sin atribuir automáticamente al CISO la ejecución de cada control.

**Problema y controversia.** El escenario que conviene examinar es el siguiente: la seguridad se revisa solo antes de producción. El lector debe reconocer que una solución aparentemente correcta puede introducir nuevos riesgos, costos o dependencias. La discusión debe explorar al menos dos alternativas y sus efectos sobre personas, procesos, datos, tecnología y terceros. También debe separar hechos de hipótesis, controles configurados de controles probados, y señales de alerta de incidentes confirmados. Cuando intervengan agentes de IA, se analizarán permisos, límites de autonomía, supervisión y trazabilidad, sin convertir la automatización en sustituto del juicio responsable.

**Aplicación formativa.** El participante trabajará un caso realista y elaborará modelo de SDLC con pruebas y responsables. Tendrá que definir el alcance, identificar activos y procesos afectados, documentar supuestos, asignar responsables y describir condiciones de entrada, éxito y reversión. La propuesta debe poder explicarse tanto a especialistas técnicos como a responsables de negocio. Para evitar soluciones decorativas, deberá incluir una prueba, simulación o procedimiento de revisión que permita observar resultados. Cuando el riesgo residual exceda los límites autorizados, se exigirá escalamiento a la autoridad correspondiente y registro de la decisión.

**Resultado esperado y evaluación.** El ensayo debe concluir con una recomendación ejecutable, sus dependencias, una explicación de por qué se eligió y qué evidencia podría refutarla. La evaluación del aprendizaje considerará precisión conceptual, razonamiento causal, viabilidad, evidencia, límites y comunicación. La relación con las otras unidades de GM-24 debe hacerse explícita: la estrategia y el gobierno del riesgo condicionan la arquitectura; la operación produce observaciones; la respuesta y la recuperación aportan lecciones para revisar el programa. El valor de «SDLC Seguro» se demuestra cuando mejora una decisión y una capacidad verificable, no cuando aumenta la cantidad de documentos, herramientas o reuniones. La pregunta abierta es qué cambiaría la recomendación ante un incidente, un nuevo requisito o una dependencia inesperada.

**Pregunta generadora:** ¿Qué decisión y qué evidencia demostrarían la utilidad de «SDLC Seguro» en una organización concreta?

---

### 240. M6.2-K10 — SBOM

**Unidad:** M6.2 · **Palabras:** 411 · **Estado:** idea central propuesta.

**Tesis central.** Un software bill of materials mejora visibilidad de componentes y dependencias, pero necesita calidad, actualización y procesos de respuesta a vulnerabilidades. En el contexto del Programa Ejecutivo TheNextCISO, «SBOM» no debe abordarse como una etiqueta de producto ni como una lista de pasos aislados. El ensayo debe explicar qué capacidad necesita desarrollar quien lidera la seguridad, cuál es su propósito empresarial y qué relación mantiene con el riesgo. Es esencial distinguir el mandato de gobierno —apetito, prioridades, responsabilidades y autoridad— de la gestión que diseña, opera y verifica la práctica. Esta distinción permite analizar decisiones sin atribuir automáticamente al CISO la ejecución de cada control.

**Problema y controversia.** El escenario que conviene examinar es el siguiente: el SBOM existe pero no se usa para priorizar riesgos reales. El lector debe reconocer que una solución aparentemente correcta puede introducir nuevos riesgos, costos o dependencias. La discusión debe explorar al menos dos alternativas y sus efectos sobre personas, procesos, datos, tecnología y terceros. También debe separar hechos de hipótesis, controles configurados de controles probados, y señales de alerta de incidentes confirmados. Cuando intervengan agentes de IA, se analizarán permisos, límites de autonomía, supervisión y trazabilidad, sin convertir la automatización en sustituto del juicio responsable.

**Aplicación formativa.** El participante trabajará un caso realista y elaborará inventario de componentes, dependencias y remediación. Tendrá que definir el alcance, identificar activos y procesos afectados, documentar supuestos, asignar responsables y describir condiciones de entrada, éxito y reversión. La propuesta debe poder explicarse tanto a especialistas técnicos como a responsables de negocio. Para evitar soluciones decorativas, deberá incluir una prueba, simulación o procedimiento de revisión que permita observar resultados. Cuando el riesgo residual exceda los límites autorizados, se exigirá escalamiento a la autoridad correspondiente y registro de la decisión.

**Resultado esperado y evaluación.** El ensayo debe concluir con una recomendación ejecutable, sus dependencias, una explicación de por qué se eligió y qué evidencia podría refutarla. La evaluación del aprendizaje considerará precisión conceptual, razonamiento causal, viabilidad, evidencia, límites y comunicación. La relación con las otras unidades de GM-24 debe hacerse explícita: la estrategia y el gobierno del riesgo condicionan la arquitectura; la operación produce observaciones; la respuesta y la recuperación aportan lecciones para revisar el programa. El valor de «SBOM» se demuestra cuando mejora una decisión y una capacidad verificable, no cuando aumenta la cantidad de documentos, herramientas o reuniones. La pregunta abierta es qué cambiaría la recomendación ante un incidente, un nuevo requisito o una dependencia inesperada.

**Pregunta generadora:** ¿Qué decisión y qué evidencia demostrarían la utilidad de «SBOM» en una organización concreta?

---

## Control de calidad y continuidad

- Conceptos incluidos: **30** (211–240).
- Extensión comprobada: **403–414 palabras** por idea central.
- Los conceptos y nombres se preservan en el orden del Documento Maestro GM-24.
- No se asignaron IDs de ensayos ni se aplicaron ChangeSets.

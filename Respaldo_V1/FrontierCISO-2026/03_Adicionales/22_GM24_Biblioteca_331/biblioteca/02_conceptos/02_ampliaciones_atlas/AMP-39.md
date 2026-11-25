<!-- generado-gm24 sha256:f50a35b5dad73800032c8acc8e47a7a6c814c1a230b93c43cfceaf8baf8036a6 -->
# AMP-39 — SOC agéntico

**Clase:** Ampliación Atlas propuesta · **Estado:** ampliación Atlas: título original; tesis propuesta [P], no aprobada · **Unidades:** M4.1.

## Enunciado y fuerza de la evidencia

El SOC agéntico redistribuye el trabajo: agentes que priorizan, investigan y proponen respuesta; personas que supervisan, ajustan y deciden, medidas por tiempo de respuesta y calidad.

**Importante:** en el Documento Maestro se documentó el **título** de `AMP-39`; la oración precedente es una **tesis propuesta [P]** en la matriz posterior, no una definición aprobada del programa.

## Desarrollo para el aprendizaje (derivación editorial)

Esta ampliación examina «SOC agéntico» en la unidad `M4.1` (Operaciones de Seguridad, Monitorización e Inteligencia). Su pregunta de diseño es qué cambiaría en la decisión de fijar qué triage se automatiza y cuándo la supervisión humana debe detenerlo al tomar en serio la tesis [P]. El vínculo `HC-019` —SOC agéntico con supervisión humana— aporta una lente vecina: «Integra XDR, SOAR, IA y decisiones de contención gobernadas». La relación no implica identidad de conceptos, aprobación del nuevo tema ni eficacia demostrada de una intervención.

En la organización ficticia del programa: El agente de triage reduce tiempo de cierre, pero su justificación oculta señales de intrusión que el analista raramente cuestiona. Una solución defendible debe contrastar estas alternativas: Aceptar recomendaciones con un clic frente a doble lectura de casos de alto impacto y muestreo ciego; las observaciones iniciales serían telemetría SIEM, registros de decisiones, falsos negativos y flujo de escalamiento. El estudiante separa lo observado, lo inferido y lo aún no verificable antes de sugerir cambios de arquitectura, gobierno u operación.

El producto de aprendizaje propuesto es «playbook SOC agéntico con medidas de calidad y control de overrides». Debe poder explicar por qué su recomendación es revisable y cómo verificaría que «No se usa el cierre de alertas como único indicador de calidad ni se asume supervisión efectiva por presencia humana nominal». La propuesta permanece abierta a revisión curricular y técnica.

## Ejercicio y criterio de evaluación

**Práctica:** Ante «El agente de triage reduce tiempo de cierre, pero su justificación oculta señales de intrusión que el analista raramente cuestiona», explica qué aporta «SOC agéntico» frente a las opciones «Aceptar recomendaciones con un clic frente a doble lectura de casos de alto impacto y muestreo ciego». Usa telemetría SIEM, registros de decisiones, falsos negativos y flujo de escalamiento y entrega playbook SOC agéntico con medidas de calidad y control de overrides. Distingue tesis [P] de evidencia obtenida y de supuestos de diseño.

**Validación:** Se acepta para revisión si identifica autoridad y límites, documenta fuentes y supuestos, compara al menos dos decisiones y demuestra «No se usa el cierre de alertas como único indicador de calidad ni se asume supervisión efectiva por presencia humana nominal». La rúbrica de la unidad es una propuesta docente, no un estándar aprobado.

La guía de unidad desarrolla el escenario longitudinal, las ocho modalidades de ejercicio y la rúbrica: [abrir unidad](../../01_unidades/M4.1/Unidad_M4.1.md).

## Preguntas del método y comprobación

**Preguntas originales consolidadas (si hay vínculo directo o de corpus):**
- `PC-191` (interrogativa): ¿Con qué criterios promovemos un agente de seguridad de piloto a producción (errores críticos, falsos positivos, reversibilidad, auditoría)? — vínculo `AMP-39`.
- `PA-096` (interrogativa): ¿Cómo vamos a reducir el volumen de alertas y el desgaste del equipo? — vínculo `AMP-39`.

**Ejemplos generados con plantillas mayéuticas documentadas:**
- `BM-1033` [Esencial]: ¿Qué problema de gobierno, riesgo o capacidad intenta resolver realmente «SOC agéntico», y qué decisión debería mejorar si se comprende correctamente?
- `BM-1034` [Tensión]: ¿Qué supuesto habitual sobre «SOC agéntico» podría ser falso o incompleto, y qué consecuencia tendría diseñar la seguridad como si fuera cierto?
- `BM-1035` [Validación]: ¿Cómo probaríamos que «SOC agéntico» funciona en condiciones reales, incluidas fallas, excepciones y dependencias, en lugar de asumir eficacia por configuración?

Las preguntas de banco son construcciones mediante plantilla; no se presentan como citas de entrevistas. Fuente original: [preguntas consolidadas](../../../Curado02/02_metodo_mayeutico/src-preguntas-consolidadas__37298ee439f0.json).

## Procedencia y límites

[Matriz de 331 pre-ensayos](../../../Curado02/01_noviembre_2026/src-ai-ciso-atlas-ensayos-thenextciso-x-core-accountabilities-fy27-2026-11-05__5528a05eb5dd.xlsx), `06Ensayos!A323:T323` (idea `[P]`: `06Ensayos!I323`); [registro de consulta y estado [P]](../../00_control/AMP_ideas_propuestas_2026-11.json).

El nombre del marco, su aparición en el corpus y una alineación temática no acreditan dominio profesional, cumplimiento ni aprobación formal. Las referencias bibliográficas individuales solo se atribuyen si la fuente las identifica; véase el documento maestro para bibliografía general de NIST e ISACA y para la condición propuesta de sus mapeos.

[Documento Maestro](../../../Curado02/01_noviembre_2026/src-thenextciso-gm-24-documento-maestro__9b8c53df319d.md), sección `M4.1` (línea 802).

<!-- generado-gm24 sha256:72d10d77b9d1c15fff021f30f3acc2eba2ed9adfbfb4a43ceff6d349e1eee83e -->
# AMP-33 — Identidades no humanas

**Clase:** Ampliación Atlas propuesta · **Estado:** ampliación Atlas: título original; tesis propuesta [P], no aprobada · **Unidades:** M2.2.

## Enunciado y fuerza de la evidencia

Las identidades no humanas ya superan a las humanas; sin inventario, dueño, credenciales gestionadas y caducidad son la superficie menos vigilada.

**Importante:** en el Documento Maestro se documentó el **título** de `AMP-33`; la oración precedente es una **tesis propuesta [P]** en la matriz posterior, no una definición aprobada del programa.

## Desarrollo para el aprendizaje (derivación editorial)

Esta ampliación examina «Identidades no humanas» en la unidad `M2.2` (Gestión de Identidad y Acceso (IAM) y Principios de Confianza Cero). Su pregunta de diseño es qué cambiaría en la decisión de asignar identidad por agente, limitar credenciales y registrar autorización por contexto al tomar en serio la tesis [P]. El vínculo `HC-009` —Gobierno de identidades no humanas— aporta una lente vecina: «Integra autorización, ciclo de vida, privilegios y accountability de servicios y agentes». La relación no implica identidad de conceptos, aprobación del nuevo tema ni eficacia demostrada de una intervención.

En la organización ficticia del programa: Cuentas de servicio de agentes mantienen tokens permanentes y el mismo permiso privilegiado en desarrollo y producción. Una solución defendible debe contrastar estas alternativas: Credencial compartida perpetua frente a identidad y permisos de menor privilegio con rotación y revocación; las observaciones iniciales serían inventario de identidades, roles, permisos, registros de acceso y break-glass. El estudiante separa lo observado, lo inferido y lo aún no verificable antes de sugerir cambios de arquitectura, gobierno u operación.

El producto de aprendizaje propuesto es «modelo IAM de agentes con ciclo de vida, controles y prueba de revocación». Debe poder explicar por qué su recomendación es revisable y cómo verificaría que «Autenticación fuerte no sustituye autorización para la acción concreta». La propuesta permanece abierta a revisión curricular y técnica.

## Ejercicio y criterio de evaluación

**Afirmación que exige verificación adicional:** La comparación cuantitativa entre identidades humanas y no humanas es una afirmación de la propuesta, no una medición validada aquí.

**Práctica:** Ante «Cuentas de servicio de agentes mantienen tokens permanentes y el mismo permiso privilegiado en desarrollo y producción», explica qué aporta «Identidades no humanas» frente a las opciones «Credencial compartida perpetua frente a identidad y permisos de menor privilegio con rotación y revocación». Usa inventario de identidades, roles, permisos, registros de acceso y break-glass y entrega modelo IAM de agentes con ciclo de vida, controles y prueba de revocación. Distingue tesis [P] de evidencia obtenida y de supuestos de diseño.

**Validación:** Se acepta para revisión si identifica autoridad y límites, documenta fuentes y supuestos, compara al menos dos decisiones y demuestra «Autenticación fuerte no sustituye autorización para la acción concreta». La rúbrica de la unidad es una propuesta docente, no un estándar aprobado.

La guía de unidad desarrolla el escenario longitudinal, las ocho modalidades de ejercicio y la rúbrica: [abrir unidad](../../01_unidades/M2.2/Unidad_M2.2.md).

## Preguntas del método y comprobación

**Preguntas originales consolidadas (si hay vínculo directo o de corpus):**
- `PC-132` (interrogativa): ¿Cómo evitamos que los agentes usen secretos estáticos (claves de API, contraseñas) y cómo los protegemos cuando no hay alternativa? — vínculo `AMP-33`.
- `PA-051` (interrogativa): ¿Cuántas identidades no humanas tenemos y cuál es su riesgo? — vínculo `AMP-33`.

**Ejemplos generados con plantillas mayéuticas documentadas:**
- `BM-1009` [Esencial]: ¿Qué problema de gobierno, riesgo o capacidad intenta resolver realmente «Identidades no humanas», y qué decisión debería mejorar si se comprende correctamente?
- `BM-1010` [Tensión]: ¿Qué supuesto habitual sobre «Identidades no humanas» podría ser falso o incompleto, y qué consecuencia tendría diseñar la seguridad como si fuera cierto?
- `BM-1011` [Validación]: ¿Cómo probaríamos que «Identidades no humanas» funciona en condiciones reales, incluidas fallas, excepciones y dependencias, en lugar de asumir eficacia por configuración?

Las preguntas de banco son construcciones mediante plantilla; no se presentan como citas de entrevistas. Fuente original: [preguntas consolidadas](../../../Curado02/02_metodo_mayeutico/src-preguntas-consolidadas__37298ee439f0.json).

## Procedencia y límites

[Matriz de 331 pre-ensayos](../../../Curado02/01_noviembre_2026/src-ai-ciso-atlas-ensayos-thenextciso-x-core-accountabilities-fy27-2026-11-05__5528a05eb5dd.xlsx), `06Ensayos!A317:T317` (idea `[P]`: `06Ensayos!I317`); [registro de consulta y estado [P]](../../00_control/AMP_ideas_propuestas_2026-11.json).

El nombre del marco, su aparición en el corpus y una alineación temática no acreditan dominio profesional, cumplimiento ni aprobación formal. Las referencias bibliográficas individuales solo se atribuyen si la fuente las identifica; véase el documento maestro para bibliografía general de NIST e ISACA y para la condición propuesta de sus mapeos.

[Documento Maestro](../../../Curado02/01_noviembre_2026/src-thenextciso-gm-24-documento-maestro__9b8c53df319d.md), sección `M2.2` (línea 679).

<!-- generado-gm24 sha256:6016b095ab5c27bcfd31b835fed331fba0ad4d6ba42897357da0f49522246ce2 -->
# AMP-34 — Identidad y autorización de agentes

**Clase:** Ampliación Atlas propuesta · **Estado:** ampliación Atlas: título original; tesis propuesta [P], no aprobada · **Unidades:** M2.2.

## Enunciado y fuerza de la evidencia

Cada agente necesita identidad propia, permisos mínimos, acceso condicional y ciclo de vida: es la base de un agente protegido.

**Importante:** en el Documento Maestro se documentó el **título** de `AMP-34`; la oración precedente es una **tesis propuesta [P]** en la matriz posterior, no una definición aprobada del programa.

## Desarrollo para el aprendizaje (derivación editorial)

Esta ampliación examina «Identidad y autorización de agentes» en la unidad `M2.2` (Gestión de Identidad y Acceso (IAM) y Principios de Confianza Cero). Su pregunta de diseño es qué cambiaría en la decisión de asignar identidad por agente, limitar credenciales y registrar autorización por contexto al tomar en serio la tesis [P]. El vínculo `M2.2-K03` —Autorización— aporta una lente vecina: «La autorización limita acciones y recursos conforme a propósito, contexto y mínimo privilegio, y debe revisarse a lo largo del ciclo de vida». La relación no implica identidad de conceptos, aprobación del nuevo tema ni eficacia demostrada de una intervención.

En la organización ficticia del programa: Cuentas de servicio de agentes mantienen tokens permanentes y el mismo permiso privilegiado en desarrollo y producción. Una solución defendible debe contrastar estas alternativas: Credencial compartida perpetua frente a identidad y permisos de menor privilegio con rotación y revocación; las observaciones iniciales serían inventario de identidades, roles, permisos, registros de acceso y break-glass. El estudiante separa lo observado, lo inferido y lo aún no verificable antes de sugerir cambios de arquitectura, gobierno u operación.

El producto de aprendizaje propuesto es «modelo IAM de agentes con ciclo de vida, controles y prueba de revocación». Debe poder explicar por qué su recomendación es revisable y cómo verificaría que «Autenticación fuerte no sustituye autorización para la acción concreta». La propuesta permanece abierta a revisión curricular y técnica.

## Ejercicio y criterio de evaluación

**Práctica:** Ante «Cuentas de servicio de agentes mantienen tokens permanentes y el mismo permiso privilegiado en desarrollo y producción», explica qué aporta «Identidad y autorización de agentes» frente a las opciones «Credencial compartida perpetua frente a identidad y permisos de menor privilegio con rotación y revocación». Usa inventario de identidades, roles, permisos, registros de acceso y break-glass y entrega modelo IAM de agentes con ciclo de vida, controles y prueba de revocación. Distingue tesis [P] de evidencia obtenida y de supuestos de diseño.

**Validación:** Se acepta para revisión si identifica autoridad y límites, documenta fuentes y supuestos, compara al menos dos decisiones y demuestra «Autenticación fuerte no sustituye autorización para la acción concreta». La rúbrica de la unidad es una propuesta docente, no un estándar aprobado.

La guía de unidad desarrolla el escenario longitudinal, las ocho modalidades de ejercicio y la rúbrica: [abrir unidad](../../01_unidades/M2.2/Unidad_M2.2.md).

## Preguntas del método y comprobación

**Preguntas originales consolidadas (si hay vínculo directo o de corpus):**
- `PC-127` (interrogativa): ¿Cada agente tiene una identidad propia, distinguible de la de personas y aplicaciones, que permita atribuirle sus acciones? — vínculo `AMP-34`.
- `PC-130` (interrogativa): ¿Los permisos de los agentes son temporales, se revisan periódicamente y pueden revocarse de inmediato? — vínculo `AMP-34`.
- `PC-135` (interrogativa): ¿Cómo verificamos la identidad de quien interactúa con nuestros agentes, sea una persona o un agente externo? — vínculo `AMP-34`.

**Ejemplos generados con plantillas mayéuticas documentadas:**
- `BM-1013` [Esencial]: ¿Qué problema de gobierno, riesgo o capacidad intenta resolver realmente «Identidad y autorización de agentes», y qué decisión debería mejorar si se comprende correctamente?
- `BM-1014` [Tensión]: ¿Qué supuesto habitual sobre «Identidad y autorización de agentes» podría ser falso o incompleto, y qué consecuencia tendría diseñar la seguridad como si fuera cierto?
- `BM-1015` [Validación]: ¿Cómo probaríamos que «Identidad y autorización de agentes» funciona en condiciones reales, incluidas fallas, excepciones y dependencias, en lugar de asumir eficacia por configuración?

Las preguntas de banco son construcciones mediante plantilla; no se presentan como citas de entrevistas. Fuente original: [preguntas consolidadas](../../../Curado02/02_metodo_mayeutico/src-preguntas-consolidadas__37298ee439f0.json).

## Procedencia y límites

[Matriz de 331 pre-ensayos](../../../Curado02/01_noviembre_2026/src-ai-ciso-atlas-ensayos-thenextciso-x-core-accountabilities-fy27-2026-11-05__5528a05eb5dd.xlsx), `06Ensayos!A318:T318` (idea `[P]`: `06Ensayos!I318`); [registro de consulta y estado [P]](../../00_control/AMP_ideas_propuestas_2026-11.json).

El nombre del marco, su aparición en el corpus y una alineación temática no acreditan dominio profesional, cumplimiento ni aprobación formal. Las referencias bibliográficas individuales solo se atribuyen si la fuente las identifica; véase el documento maestro para bibliografía general de NIST e ISACA y para la condición propuesta de sus mapeos.

[Documento Maestro](../../../Curado02/01_noviembre_2026/src-thenextciso-gm-24-documento-maestro__9b8c53df319d.md), sección `M2.2` (línea 679).

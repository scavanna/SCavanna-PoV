<!-- generado-gm24 sha256:e44292ef01c73f5f7c942d0e73a95c11bb5d94679ca009254b6247ad7de31037 -->
# AMP-50 — Seguridad de herramientas y conectores

**Clase:** Ampliación Atlas propuesta · **Estado:** ampliación Atlas: título original; tesis propuesta [P], no aprobada · **Unidades:** M6.2.

## Enunciado y fuerza de la evidencia

Conectores (incluido MCP) y herramientas amplían lo que un agente puede tocar: requieren inventario, autenticación, permisos mínimos y monitoreo.

**Importante:** en el Documento Maestro se documentó el **título** de `AMP-50`; la oración precedente es una **tesis propuesta [P]** en la matriz posterior, no una definición aprobada del programa.

## Desarrollo para el aprendizaje (derivación editorial)

Esta ampliación examina «Seguridad de herramientas y conectores» en la unidad `M6.2` (Seguridad en Redes, Nube, Tecnologías Emergentes y SCRM). Su pregunta de diseño es qué cambiaría en la decisión de gobernar supply chain de modelos, postura de nube y responsabilidades de terceros al tomar en serio la tesis [P]. El vínculo `M6.2-K04` —Seguridad IA— aporta una lente vecina: «La seguridad de IA protege modelos, datos, herramientas, agentes y procesos ante amenazas específicas y consecuencias de autonomía». La relación no implica identidad de conceptos, aprobación del nuevo tema ni eficacia demostrada de una intervención.

En la organización ficticia del programa: Un modelo externo y un conector MCP actualizan silenciosamente dependencias; el proveedor delega controles que la empresa creía incluidos. Una solución defendible debe contrastar estas alternativas: Aceptar atestados genéricos frente a exigir procedencia, SBOM, permisos y pruebas de actualización; las observaciones iniciales serían contrato cloud, SBOM, inventario de conectores, rutas de datos y licencias. El estudiante separa lo observado, lo inferido y lo aún no verificable antes de sugerir cambios de arquitectura, gobierno u operación.

El producto de aprendizaje propuesto es «expediente de tercero con matriz de responsabilidad y plan de verificación». Debe poder explicar por qué su recomendación es revisable y cómo verificaría que «Responsabilidad compartida y licencias no se infieren del nombre comercial del servicio». La propuesta permanece abierta a revisión curricular y técnica.

## Ejercicio y criterio de evaluación

**Práctica:** Ante «Un modelo externo y un conector MCP actualizan silenciosamente dependencias; el proveedor delega controles que la empresa creía incluidos», explica qué aporta «Seguridad de herramientas y conectores» frente a las opciones «Aceptar atestados genéricos frente a exigir procedencia, SBOM, permisos y pruebas de actualización». Usa contrato cloud, SBOM, inventario de conectores, rutas de datos y licencias y entrega expediente de tercero con matriz de responsabilidad y plan de verificación. Distingue tesis [P] de evidencia obtenida y de supuestos de diseño.

**Validación:** Se acepta para revisión si identifica autoridad y límites, documenta fuentes y supuestos, compara al menos dos decisiones y demuestra «Responsabilidad compartida y licencias no se infieren del nombre comercial del servicio». La rúbrica de la unidad es una propuesta docente, no un estándar aprobado.

La guía de unidad desarrolla el escenario longitudinal, las ocho modalidades de ejercicio y la rúbrica: [abrir unidad](../../01_unidades/M6.2/Unidad_M6.2.md).

## Preguntas del método y comprobación

**Preguntas originales consolidadas (si hay vínculo directo o de corpus):**
- `PC-123` (interrogativa): ¿Cómo inventariamos y aprobamos los servidores MCP y las herramientas que los agentes pueden invocar, sean internos o de terceros? — vínculo `AMP-50`.
- `PC-149` (interrogativa): ¿Qué controles tenemos contra el envenenamiento de herramientas y los cambios maliciosos en servidores MCP o complementos ya aprobados? — vínculo `AMP-50`.
- `PC-263` (interrogativa): ¿La autorización de cada llamada de un agente a una herramienta la decide una pasarela o el servidor MCP, y nunca el propio modelo? — vínculo `AMP-50`.

**Ejemplos generados con plantillas mayéuticas documentadas:**
- `BM-1077` [Esencial]: ¿Qué problema de gobierno, riesgo o capacidad intenta resolver realmente «Seguridad de herramientas y conectores», y qué decisión debería mejorar si se comprende correctamente?
- `BM-1078` [Tensión]: ¿Qué supuesto habitual sobre «Seguridad de herramientas y conectores» podría ser falso o incompleto, y qué consecuencia tendría diseñar la seguridad como si fuera cierto?
- `BM-1079` [Decisión]: ¿Qué alternativa concreta elegiríamos a partir de «Seguridad de herramientas y conectores», quién debería decidirla y qué señal obligaría a revisarla?

Las preguntas de banco son construcciones mediante plantilla; no se presentan como citas de entrevistas. Fuente original: [preguntas consolidadas](../../../Curado02/02_metodo_mayeutico/src-preguntas-consolidadas__37298ee439f0.json).

## Procedencia y límites

[Matriz de 331 pre-ensayos](../../../Curado02/01_noviembre_2026/src-ai-ciso-atlas-ensayos-thenextciso-x-core-accountabilities-fy27-2026-11-05__5528a05eb5dd.xlsx), `06Ensayos!A334:T334` (idea `[P]`: `06Ensayos!I334`); [registro de consulta y estado [P]](../../00_control/AMP_ideas_propuestas_2026-11.json).

El nombre del marco, su aparición en el corpus y una alineación temática no acreditan dominio profesional, cumplimiento ni aprobación formal. Las referencias bibliográficas individuales solo se atribuyen si la fuente las identifica; véase el documento maestro para bibliografía general de NIST e ISACA y para la condición propuesta de sus mapeos.

[Documento Maestro](../../../Curado02/01_noviembre_2026/src-thenextciso-gm-24-documento-maestro__9b8c53df319d.md), sección `M6.2` (línea 1007).

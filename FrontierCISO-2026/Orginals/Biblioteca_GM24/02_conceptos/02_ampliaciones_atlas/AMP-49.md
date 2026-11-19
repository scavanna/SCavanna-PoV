<!-- generado-gm24 sha256:bcd0714b74c18f2ff9671353f1069462f943e661d73c27a22d7acc36044c7529 -->
# AMP-49 — Supply chain de modelos

**Clase:** Ampliación Atlas propuesta · **Estado:** ampliación Atlas: título original; tesis propuesta [P], no aprobada · **Unidades:** M6.2.

## Enunciado y fuerza de la evidencia

Modelos y componentes de IA tienen cadena de suministro: procedencia, licencias, integridad y evaluación antes de su uso.

**Importante:** en el Documento Maestro se documentó el **título** de `AMP-49`; la oración precedente es una **tesis propuesta [P]** en la matriz posterior, no una definición aprobada del programa.

## Desarrollo para el aprendizaje (derivación editorial)

Esta ampliación examina «Supply chain de modelos» en la unidad `M6.2` (Seguridad en Redes, Nube, Tecnologías Emergentes y SCRM). Su pregunta de diseño es qué cambiaría en la decisión de gobernar supply chain de modelos, postura de nube y responsabilidades de terceros al tomar en serio la tesis [P]. El vínculo `HC-031` —Seguridad del software y confianza en componentes— aporta una lente vecina: «Relaciona SDLC, SBOM, controles y riesgo de suministro». La relación no implica identidad de conceptos, aprobación del nuevo tema ni eficacia demostrada de una intervención.

En la organización ficticia del programa: Un modelo externo y un conector MCP actualizan silenciosamente dependencias; el proveedor delega controles que la empresa creía incluidos. Una solución defendible debe contrastar estas alternativas: Aceptar atestados genéricos frente a exigir procedencia, SBOM, permisos y pruebas de actualización; las observaciones iniciales serían contrato cloud, SBOM, inventario de conectores, rutas de datos y licencias. El estudiante separa lo observado, lo inferido y lo aún no verificable antes de sugerir cambios de arquitectura, gobierno u operación.

El producto de aprendizaje propuesto es «expediente de tercero con matriz de responsabilidad y plan de verificación». Debe poder explicar por qué su recomendación es revisable y cómo verificaría que «Responsabilidad compartida y licencias no se infieren del nombre comercial del servicio». La propuesta permanece abierta a revisión curricular y técnica.

## Ejercicio y criterio de evaluación

**Práctica:** Ante «Un modelo externo y un conector MCP actualizan silenciosamente dependencias; el proveedor delega controles que la empresa creía incluidos», explica qué aporta «Supply chain de modelos» frente a las opciones «Aceptar atestados genéricos frente a exigir procedencia, SBOM, permisos y pruebas de actualización». Usa contrato cloud, SBOM, inventario de conectores, rutas de datos y licencias y entrega expediente de tercero con matriz de responsabilidad y plan de verificación. Distingue tesis [P] de evidencia obtenida y de supuestos de diseño.

**Validación:** Se acepta para revisión si identifica autoridad y límites, documenta fuentes y supuestos, compara al menos dos decisiones y demuestra «Responsabilidad compartida y licencias no se infieren del nombre comercial del servicio». La rúbrica de la unidad es una propuesta docente, no un estándar aprobado.

La guía de unidad desarrolla el escenario longitudinal, las ocho modalidades de ejercicio y la rúbrica: [abrir unidad](../../01_unidades/M6.2/Unidad_M6.2.md).

## Preguntas del método y comprobación

**Preguntas originales consolidadas (si hay vínculo directo o de corpus):**
- `PC-122` (interrogativa): ¿Mantenemos una lista de materiales de IA (modelos, versiones, conjuntos de datos, instrucciones de sistema, herramientas, dependencias) para cada sistema crítico? — vínculo `AMP-49`.
- `PC-148` (interrogativa): ¿Cómo aseguramos la cadena de suministro de IA: modelos de terceros, pesos, bibliotecas, conjuntos de datos, plantillas de agentes y servidores MCP? — vínculo `AMP-49`.
- `PC-209` (interrogativa): ¿Qué modelos, conjuntos de datos y bibliotecas de terceros usamos, de dónde vienen y quién los evaluó? — vínculo `AMP-49`.

**Ejemplos generados con plantillas mayéuticas documentadas:**
- `BM-1073` [Esencial]: ¿Qué problema de gobierno, riesgo o capacidad intenta resolver realmente «Supply chain de modelos», y qué decisión debería mejorar si se comprende correctamente?
- `BM-1074` [Tensión]: ¿Qué supuesto habitual sobre «Supply chain de modelos» podría ser falso o incompleto, y qué consecuencia tendría diseñar la seguridad como si fuera cierto?
- `BM-1075` [Decisión]: ¿Qué alternativa concreta elegiríamos a partir de «Supply chain de modelos», quién debería decidirla y qué señal obligaría a revisarla?

Las preguntas de banco son construcciones mediante plantilla; no se presentan como citas de entrevistas. Fuente original: [preguntas consolidadas](../../../Curado02/02_metodo_mayeutico/src-preguntas-consolidadas__37298ee439f0.json).

## Procedencia y límites

[Matriz de 331 pre-ensayos](../../../Curado02/01_noviembre_2026/src-ai-ciso-atlas-ensayos-thenextciso-x-core-accountabilities-fy27-2026-11-05__5528a05eb5dd.xlsx), `06Ensayos!A333:T333` (idea `[P]`: `06Ensayos!I333`); [registro de consulta y estado [P]](../../00_control/AMP_ideas_propuestas_2026-11.json).

El nombre del marco, su aparición en el corpus y una alineación temática no acreditan dominio profesional, cumplimiento ni aprobación formal. Las referencias bibliográficas individuales solo se atribuyen si la fuente las identifica; véase el documento maestro para bibliografía general de NIST e ISACA y para la condición propuesta de sus mapeos.

[Documento Maestro](../../../Curado02/01_noviembre_2026/src-thenextciso-gm-24-documento-maestro__9b8c53df319d.md), sección `M6.2` (línea 1007).

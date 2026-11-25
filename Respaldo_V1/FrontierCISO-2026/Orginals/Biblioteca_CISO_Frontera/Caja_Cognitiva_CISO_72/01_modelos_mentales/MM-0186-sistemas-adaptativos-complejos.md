<!-- generado-ciso-excel sha256:1e7456f48664ca120e4e4af4b3fc6175027db5fda21551d899f3cbabc571e590 -->
# Sistemas adaptativos complejos

**ID:** `MM-0186` · **Categoría:** Modelos mentales · **Prioridad editorial:** 15 · **Base de definición:** Apoyada por fuentes del catálogo

## Definición y alcance

Modelo de sistemas formados por agentes que se adaptan y cuyas interacciones pueden producir patrones no previstos por el comportamiento aislado.

**Límites:** Imponer límites de autonomía, observabilidad y parada del sistema completo. Fuente principal de inversiones: la aplicación CISO es una extrapolación profesional, no un resultado medido.

## Alias

- Complex Adaptive Systems

## Relevancia para el CISO

**Por qué:** Anticipa conductas emergentes de agentes que se adaptan e interactúan.

**Caso específico:** Dos agentes reducen sus propios errores, pero juntos generan una cascada de bloqueos.

**Pregunta guía:** ¿Qué no aparece en pruebas unitarias pero sí en el sistema completo?

**Dominios:** SOC agéntico, Trust Framework

**Casos CISO adicionales:**

- Gobernar un SOC con varios agentes que intercambian hipótesis y acciones.
- Definir límites cuando la optimización local altera el comportamiento conjunto.

## Aplicación para arquitectura, SOC agéntico y Trust Framework

**Arquitectura:**

- Probar interacciones entre agentes, operadores y herramientas en simulación.

**SOC agéntico — Alta:** Recomendación de diseño: Definir límites cuando la optimización local altera el comportamiento conjunto.

**Trust Framework — Alta:** Recomendación de assurance: Probar interacciones entre agentes, operadores y herramientas en simulación.

## Práctica y evaluación

**Ejercicios:**

- Simular un cambio de incentivos en un agente y rastrear efectos sistémicos.
- Repetir el ejercicio con una hipótesis rival y explicar por qué el control propuesto (imponer límites de autonomía, observabilidad y parada del sistema completo) se mantiene o cambia.

**Métodos de evaluación:**

- En un caso CISO controlado, medir número de fallos emergentes en pruebas multiagente no vistos en pruebas unitarias. y documentar línea base, criterios y resultado.
- Hacer revisión independiente de número de fallos emergentes en pruebas multiagente no vistos en pruebas unitarias. en al menos dos escenarios alternativos; registrar contradicciones.

**Controles o compensaciones:**

- Imponer límites de autonomía, observabilidad y parada del sistema completo.
- Registrar condiciones de aplicación y probar un modelo alternativo antes de institucionalizar esta recomendación.

## Pensadores y bibliografía identificados

**Personas y atribución documentada:**

- Anshul Khare — Coautor del libro que desarrolla el modelo (PDF p. 434); no se le atribuye invención.
- Vishal Khandelwal — Coautor del libro que desarrolla el modelo (PDF p. 434); no se le atribuye invención.

**Referencias bibliográficas mencionadas en el corpus:**

- Anshul Khare y Vishal Khandelwal, Mental Models, Investing, And You, Safal Niveshak (fecha no explícita en el PDF)

## Trazabilidad documental

**Documentos contabilizados en el catálogo:** 2. **Localizadores representativos listados:** 2.

- Mental_Models_Investing_and_You.pdf — chapter:24;pdf-page:200;printed-page:198 (Capítulo dedicado)
- Ensayo 20241117 -_.docx — line:32 (Mención de alias (no definición))

## Nota metodológica

La definición y las referencias se registran desde el catálogo; la prioridad, el caso concreto y la pregunta son adaptación editorial para el CISO, no evidencia experimental de eficacia. Aplicar como herramienta situada, no como explicación universal.

<!-- generado-ciso-excel sha256:cbaf5d39da49599814820f303a4339be615739a2379744df01b65570dff1b5d3 -->
# Historias alternativas

**ID:** `MM-0199` · **Categoría:** Modelos mentales · **Prioridad editorial:** 22 · **Base de definición:** Apoyada por fuentes del catálogo

## Definición y alcance

Modelo de comparar desenlaces alternativos plausibles a partir de una misma decisión, incluyendo el papel del azar.

**Límites:** Usar contrafactuales y probabilidades sin presentar escenarios como hechos. Fuente principal de inversiones: la aplicación CISO es una extrapolación profesional, no un resultado medido.

## Alias

- Alternative Histories

## Relevancia para el CISO

**Por qué:** Impide confundir una decisión bien razonada con un resultado favorable por suerte.

**Caso específico:** Una contención acertó; reconstruye cómo habría evolucionado el incidente con señales ligeramente distintas.

**Pregunta guía:** ¿Seguiríamos defendiendo esta decisión si el resultado hubiera cambiado?

**Dominios:** Crisis, Directorio

**Casos CISO adicionales:**

- Evitar juzgar una decisión de incidente solo por su resultado final.
- Examinar escenarios donde un control correcto falla o uno débil tiene suerte.

## Aplicación para arquitectura, SOC agéntico y Trust Framework

**Arquitectura:**

- Guardar premisas y posibles cadenas alternativas en el threat model.

**SOC agéntico — Alta:** Recomendación de diseño: Examinar escenarios donde un control correcto falla o uno débil tiene suerte.

**Trust Framework — Alta:** Recomendación de assurance: Guardar premisas y posibles cadenas alternativas en el threat model.

## Práctica y evaluación

**Ejercicios:**

- Reconstruir tres desenlaces para una decisión real sin cambiar su evidencia inicial.
- Repetir el ejercicio con una hipótesis rival y explicar por qué el control propuesto (usar contrafactuales y probabilidades sin presentar escenarios como hechos) se mantiene o cambia.

**Métodos de evaluación:**

- En un caso CISO controlado, medir calidad ex ante de la decisión frente a varios resultados simulados. y documentar línea base, criterios y resultado.
- Hacer revisión independiente de calidad ex ante de la decisión frente a varios resultados simulados. en al menos dos escenarios alternativos; registrar contradicciones.

**Controles o compensaciones:**

- Usar contrafactuales y probabilidades sin presentar escenarios como hechos.
- Registrar condiciones de aplicación y probar un modelo alternativo antes de institucionalizar esta recomendación.

## Pensadores y bibliografía identificados

**Personas y atribución documentada:**

- Anshul Khare — Coautor del libro que desarrolla el modelo (PDF p. 434); no se le atribuye invención.
- Vishal Khandelwal — Coautor del libro que desarrolla el modelo (PDF p. 434); no se le atribuye invención.

**Referencias bibliográficas mencionadas en el corpus:**

- Anshul Khare y Vishal Khandelwal, Mental Models, Investing, And You, Safal Niveshak (fecha no explícita en el PDF)

## Trazabilidad documental

**Documentos contabilizados en el catálogo:** 1. **Localizadores representativos listados:** 1.

- Mental_Models_Investing_and_You.pdf — chapter:47;pdf-page:392;printed-page:390 (Capítulo dedicado)

## Nota metodológica

La definición y las referencias se registran desde el catálogo; la prioridad, el caso concreto y la pregunta son adaptación editorial para el CISO, no evidencia experimental de eficacia. Aplicar como herramienta situada, no como explicación universal.

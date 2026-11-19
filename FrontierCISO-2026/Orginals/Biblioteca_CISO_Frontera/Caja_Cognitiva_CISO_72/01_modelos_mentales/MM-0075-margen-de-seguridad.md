<!-- generado-ciso-excel sha256:ee563205d3a290bebb0fa33e9c4ac129671e7e1b75b69409a4e24cdacccf7f7c -->
# Margen de seguridad

**ID:** `MM-0075` · **Categoría:** Modelos mentales · **Prioridad editorial:** 13 · **Base de definición:** Apoyada por fuentes del catálogo

## Definición y alcance

El margen de seguridad introduce un colchón entre la carga esperada y la capacidad disponible para absorber error e incertidumbre.

**Límites:** El margen tiene costo y no sustituye pruebas, monitoreo ni recuperación; debe dimensionarse según incertidumbre.

## Alias

- margin
  of safety
- margin of
  safety
- Margin of Safety
- margin of safety

## Relevancia para el CISO

**Por qué:** Introduce colchones frente al error de estimación, capacidad y tiempo.

**Caso específico:** La capacidad SOC proyectada alcanza para el promedio, pero no para un pico coordinado de alertas.

**Pregunta guía:** ¿Cuánto margen queda cuando fallan dos supuestos simultáneamente?

**Dominios:** Crisis, SOC agéntico

**Casos CISO adicionales:**

- Aplicar el modelo para reservar capacidad frente a errores de estimación y eventos adversos.
- Incluir una comprobación de carga esperada, capacidad disponible, incertidumbre y margen en decisiones de riesgo, estrategia o incidentes.

## Aplicación para arquitectura, SOC agéntico y Trust Framework

**Arquitectura:**

- Usar el modelo para incluir buffers de capacidad, tiempo, presupuesto y tolerancia a fallos.

**SOC agéntico — Alta:** Puede incorporarse como regla o bucle observable para reservar capacidad frente a errores de estimación y eventos adversos.

**Trust Framework — Alta:** Aporta directamente a trazabilidad, control o rendición de cuentas al usarlo para incluir buffers de capacidad, tiempo, presupuesto y tolerancia a fallos.

## Práctica y evaluación

**Ejercicios:**

- Resolver un caso breve aplicando el modelo para reservar capacidad frente a errores de estimación y eventos adversos y explicitar los supuestos.
- Reanalizar una decisión pasada, identificar carga esperada, capacidad disponible, incertidumbre y margen y describir qué habría cambiado.

**Métodos de evaluación:**

- Auditar 10 decisiones y registrar si quedó documentado lo siguiente: carga esperada, capacidad disponible, incertidumbre y margen.
- Comparar dos casos similares, con y sin aplicación explícita del modelo, mediante una métrica de resultado acordada.

**Controles o compensaciones:**

- Usar el modelo como lente, no como regla; contrastarlo con datos y con un modelo alternativo.
- Documentar las condiciones donde no aplica y someter la conclusión a revisión independiente.

## Pensadores y bibliografía identificados

**Personas y atribución documentada:**

- Charlie Munger — El extracto lo vincula explícitamente con la aplicación del margen de seguridad.

**Referencias bibliográficas mencionadas en el corpus:**

- No consta en los documentos analizados.

## Trazabilidad documental

**Documentos contabilizados en el catálogo:** 23. **Localizadores representativos listados:** 3.

- 20 Relevant Blog and Internet Posts on CISO Mental Models - OK.docx — paragraph:101;style:Normal (Pasaje directo identificado)
- 250824 - 500 Mental Models.docx — line:130 (Pasaje directo identificado)
- 250824 - Applying Mental Models to Cybersecurity(1).docx — line:287 (Revisión semántica localizada)

## Nota metodológica

La definición y las referencias se registran desde el catálogo; la prioridad, el caso concreto y la pregunta son adaptación editorial para el CISO, no evidencia experimental de eficacia. Aplicar como herramienta situada, no como explicación universal.

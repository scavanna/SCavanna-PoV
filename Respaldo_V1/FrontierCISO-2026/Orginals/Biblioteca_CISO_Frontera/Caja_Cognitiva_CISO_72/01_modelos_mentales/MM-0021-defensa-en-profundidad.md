<!-- generado-ciso-excel sha256:3aaaa28602779be3ef441b4903d740b67014e3fcf80f109dac0f90ffa09b8868 -->
# Defensa en profundidad

**ID:** `MM-0021` · **Categoría:** Modelos mentales · **Prioridad editorial:** 12 · **Base de definición:** Apoyada por fuentes del catálogo

## Definición y alcance

La defensa en profundidad distribuye múltiples capas de protección para que el fallo de una no deje el activo sin defensa.

**Límites:** Más capas no garantizan seguridad si comparten la misma dependencia, carecen de cobertura o añaden complejidad incontrolada.

## Alias

- defence in depth
- defense in depth

## Relevancia para el CISO

**Por qué:** Diseña controles independientes para que un único fallo no entregue todo el sistema.

**Caso específico:** La revisión humana del agente falla; límites de privilegio y rollback aún contienen el daño.

**Pregunta guía:** ¿Qué otra barrera permanece si esta capa se equivoca?

**Dominios:** Arquitectura, Trust Framework

**Casos CISO adicionales:**

- Aplicar el modelo para evitar puntos únicos de fallo en riesgos críticos.
- Incluir una comprobación de independencia de capas, cobertura, modo de fallo y control compensatorio en decisiones de riesgo, estrategia o incidentes.

## Aplicación para arquitectura, SOC agéntico y Trust Framework

**Arquitectura:**

- Usar el modelo para diseñar capas independientes de prevención, detección, respuesta y recuperación.

**SOC agéntico — Alta:** Puede incorporarse como regla o bucle observable para evitar puntos únicos de fallo en riesgos críticos.

**Trust Framework — Alta:** Aporta directamente a trazabilidad, control o rendición de cuentas al usarlo para diseñar capas independientes de prevención, detección, respuesta y recuperación.

## Práctica y evaluación

**Ejercicios:**

- Resolver un caso breve aplicando el modelo para evitar puntos únicos de fallo en riesgos críticos y explicitar los supuestos.
- Reanalizar una decisión pasada, identificar independencia de capas, cobertura, modo de fallo y control compensatorio y describir qué habría cambiado.

**Métodos de evaluación:**

- Auditar 10 decisiones y registrar si quedó documentado lo siguiente: independencia de capas, cobertura, modo de fallo y control compensatorio.
- Comparar dos casos similares, con y sin aplicación explícita del modelo, mediante una métrica de resultado acordada.

**Controles o compensaciones:**

- Usar el modelo como lente, no como regla; contrastarlo con datos y con un modelo alternativo.
- Documentar las condiciones donde no aplica y someter la conclusión a revisión independiente.

## Pensadores y bibliografía identificados

**Personas y atribución documentada:**

- No consta en los documentos analizados.

**Referencias bibliográficas mencionadas en el corpus:**

- No consta en los documentos analizados.

## Trazabilidad documental

**Documentos contabilizados en el catálogo:** 35. **Localizadores representativos listados:** 3.

- MMCB 202510-01 (2).xlsx — [sheet claudem] (Mención taxonómica (no definición))
- MMCB 202510-01.xlsx — [sheet claudem] (Mención taxonómica (no definición))
- MMCB 202604.xlsx — [sheet claudem] (Mención taxonómica (no definición))

## Nota metodológica

La definición y las referencias se registran desde el catálogo; la prioridad, el caso concreto y la pregunta son adaptación editorial para el CISO, no evidencia experimental de eficacia. Aplicar como herramienta situada, no como explicación universal.

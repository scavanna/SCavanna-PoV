<!-- generado-ciso-excel sha256:0534c5b41e2702c23d0f710cb0f0c5cabcb621a9ef0d3850d7f7457696965345 -->
# Modelado de amenazas

**ID:** `MM-0077` · **Categoría:** Modelos mentales · **Prioridad editorial:** 10 · **Base de definición:** Apoyada por fuentes del catálogo

## Definición y alcance

El modelado de amenazas es un proceso estructurado para identificar activos, adversarios, rutas de ataque y contramedidas durante el diseño y la evolución de un sistema.

**Límites:** El modelo queda obsoleto si no se actualiza y no sustituye pruebas o telemetría operativa.

## Alias

- modelo de amenazas
- threat modeling
- threat modelling

## Relevancia para el CISO

**Por qué:** Convierte la arquitectura en hipótesis explícitas sobre actores, activos y abuso.

**Caso específico:** Se habilita a un agente a modificar identidades; modela rutas de abuso y controles antes de producción.

**Pregunta guía:** ¿Quién puede hacer qué, contra qué activo y con qué precondiciones?

**Dominios:** Arquitectura, SOC agéntico

**Casos CISO adicionales:**

- Aplicar el modelo para priorizar amenazas y contramedidas según contexto y activos críticos.
- Incluir una comprobación de activos, supuestos, amenazas, rutas y mitigaciones trazables en decisiones de riesgo, estrategia o incidentes.

## Aplicación para arquitectura, SOC agéntico y Trust Framework

**Arquitectura:**

- Usar el modelo para integrar amenazas, límites de confianza y mitigaciones en decisiones de arquitectura.

**SOC agéntico — Alta:** Puede incorporarse como regla o bucle observable para priorizar amenazas y contramedidas según contexto y activos críticos.

**Trust Framework — Alta:** Aporta directamente a trazabilidad, control o rendición de cuentas al usarlo para integrar amenazas, límites de confianza y mitigaciones en decisiones de arquitectura.

## Práctica y evaluación

**Ejercicios:**

- Resolver un caso breve aplicando el modelo para priorizar amenazas y contramedidas según contexto y activos críticos y explicitar los supuestos.
- Reanalizar una decisión pasada, identificar activos, supuestos, amenazas, rutas y mitigaciones trazables y describir qué habría cambiado.

**Métodos de evaluación:**

- Auditar 10 decisiones y registrar si quedó documentado lo siguiente: activos, supuestos, amenazas, rutas y mitigaciones trazables.
- Comparar dos casos similares, con y sin aplicación explícita del modelo, mediante una métrica de resultado acordada.

**Controles o compensaciones:**

- Usar el modelo como lente, no como regla; contrastarlo con datos y con un modelo alternativo.
- Documentar las condiciones donde no aplica y someter la conclusión a revisión independiente.

## Pensadores y bibliografía identificados

**Personas y atribución documentada:**

- Bruce Schneier — El extracto relaciona explícitamente a Schneier con el uso y revisión de modelos de amenazas.

**Referencias bibliográficas mencionadas en el corpus:**

- ¿Qué es el modelado de amenazas? - Cloudflare, acceso: agosto 24, 2025, https://www.cloudflare.com/es-es/learning/security/glossary/what-is-threat-modeling/

## Trazabilidad documental

**Documentos contabilizados en el catálogo:** 35. **Localizadores representativos listados:** 3.

- BiaCodex_Reordenado.xlsx — [sheet biacodex_reordenado] (Mención taxonómica (no definición))
- Dutton_Fostering a cybersecurity mindset.pdf — [page 4] (Mención taxonómica (no definición))
- Hoja de cálculo sin título (3).xlsx — [sheet copia de biacodex] (Mención taxonómica (no definición))

## Nota metodológica

La definición y las referencias se registran desde el catálogo; la prioridad, el caso concreto y la pregunta son adaptación editorial para el CISO, no evidencia experimental de eficacia. Aplicar como herramienta situada, no como explicación universal.

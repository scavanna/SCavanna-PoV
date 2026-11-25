<!-- generado-ciso-excel sha256:c8d0b98e3ca1034a225f88f3e8b1f6d3e0c35eec594467ddb3535f3bf49a7d5f -->
# Actualización bayesiana

**ID:** `MM-0001` · **Categoría:** Modelos mentales · **Prioridad editorial:** 7 · **Base de definición:** Apoyada por fuentes del catálogo

## Definición y alcance

La actualización bayesiana revisa la probabilidad de una hipótesis al incorporar evidencia nueva, pasando de una creencia previa a una posterior.

**Límites:** Requiere probabilidades y evidencia razonablemente calibradas; no corrige datos sesgados ni modelos mal especificados.

## Alias

- bayes update
- bayesian inference
- bayesian updating

## Relevancia para el CISO

**Por qué:** Permite revisar confianza en una hipótesis al recibir evidencia nueva.

**Caso específico:** Un agente atribuye una alerta a malware; inteligencia posterior favorece error de configuración.

**Pregunta guía:** ¿Cuánto debe cambiar nuestra creencia y por qué?

**Dominios:** SOC agéntico, Crisis

**Casos CISO adicionales:**

- Aplicar el modelo para actualizar estimaciones de riesgo e hipótesis de amenaza con evidencia nueva.
- Incluir una comprobación de probabilidades previas, evidencia incorporada y probabilidades posteriores en decisiones de riesgo, estrategia o incidentes.

## Aplicación para arquitectura, SOC agéntico y Trust Framework

**Arquitectura:**

- Usar el modelo para diseñar motores de riesgo que conserven priors, evidencia y posteriores trazables.

**SOC agéntico — Alta:** Puede incorporarse como regla o bucle observable para actualizar estimaciones de riesgo e hipótesis de amenaza con evidencia nueva.

**Trust Framework — Alta:** Aporta directamente a trazabilidad, control o rendición de cuentas al usarlo para diseñar motores de riesgo que conserven priors, evidencia y posteriores trazables.

## Práctica y evaluación

**Ejercicios:**

- Resolver un caso breve aplicando el modelo para actualizar estimaciones de riesgo e hipótesis de amenaza con evidencia nueva y explicitar los supuestos.
- Reanalizar una decisión pasada, identificar probabilidades previas, evidencia incorporada y probabilidades posteriores y describir qué habría cambiado.

**Métodos de evaluación:**

- Auditar 10 decisiones y registrar si quedó documentado lo siguiente: probabilidades previas, evidencia incorporada y probabilidades posteriores.
- Comparar dos casos similares, con y sin aplicación explícita del modelo, mediante una métrica de resultado acordada.

**Controles o compensaciones:**

- Usar el modelo como lente, no como regla; contrastarlo con datos y con un modelo alternativo.
- Documentar las condiciones donde no aplica y someter la conclusión a revisión independiente.

## Pensadores y bibliografía identificados

**Personas y atribución documentada:**

- No consta en los documentos analizados.

**Referencias bibliográficas mencionadas en el corpus:**

- Bayesian Inference: An Introduction to Probabilistic Reasoning | Institute of Data, acceso: junio 22, 2025, https://www.institutedata.com/us/blog/bayesian-inference/

## Trazabilidad documental

**Documentos contabilizados en el catálogo:** 16. **Localizadores representativos listados:** 3.

- BiaCodex_Reordenado.xlsx — [sheet biacodex_reordenado] (Mención taxonómica (no definición))
- Hoja de cálculo sin título (3).xlsx — [sheet copia de biacodex] (Mención taxonómica (no definición))
- Mindsets.xlsx — [sheet debi] (Mención taxonómica (no definición))

## Nota metodológica

La definición y las referencias se registran desde el catálogo; la prioridad, el caso concreto y la pregunta son adaptación editorial para el CISO, no evidencia experimental de eficacia. Aplicar como herramienta situada, no como explicación universal.

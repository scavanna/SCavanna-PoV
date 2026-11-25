<!-- generado-ciso-excel sha256:badaee289ceaae16a8af597316b761321ba21223ed2cb7053e520031590df379 -->
# Pensamiento en grafos

**ID:** `MM-0112` · **Categoría:** Modelos mentales · **Prioridad editorial:** 11 · **Base de definición:** Síntesis conservadora derivada

## Definición y alcance

Estilo que modela entidades y relaciones como una red para razonar sobre caminos y dependencias. La fuente lo vincula con la perspectiva del atacante.

**Límites:** Adecuado para relaciones y rutas; no representa cantidades, tiempo o causalidad sin atributos adicionales.

## Alias

- No consta en los documentos analizados.

## Relevancia para el CISO

**Por qué:** Muestra conexiones y caminos laterales invisibles en inventarios lineales.

**Caso específico:** Un incidente conecta una identidad de servicio, dos agentes, datos sensibles y un tercero.

**Pregunta guía:** ¿Qué caminos existen entre privilegio inicial e impacto final?

**Dominios:** Arquitectura, SOC agéntico

**Casos CISO adicionales:**

- Visualizar caminos entre identidades, activos y privilegios.
- Detectar dependencias que un inventario oculta.

## Aplicación para arquitectura, SOC agéntico y Trust Framework

**Arquitectura:**

- Construir grafos de confianza, flujo y dependencia.

**SOC agéntico — Alta:** Los SOC agénticos dependen de relaciones entre entidades.

**Trust Framework — Alta:** Facilita procedencia si la semántica es confiable.

## Práctica y evaluación

**Ejercicios:**

- Convertir un incidente lineal en grafo.
- Comparar decisiones desde lista y grafo.

**Métodos de evaluación:**

- El grafo descubre rutas no visibles en tablas.
- Nodos y enlaces tienen semántica y fuente.

**Controles o compensaciones:**

- No inferir causalidad por conexión.
- Mantener el grafo actualizado y trazable.

## Pensadores y bibliografía identificados

**Personas y atribución documentada:**

- No consta en los documentos analizados.

**Referencias bibliográficas mencionadas en el corpus:**

- No consta en los documentos analizados.

## Trazabilidad documental

**Documentos contabilizados en el catálogo:** 3. **Localizadores representativos listados:** 3.

- Cybersecurity Paradigm Shift Essay_.docx — line:30 (Pasaje directo identificado)
- Cybersecurity Paradigm Shift Essay_.docx — line:30 (Registro de ocurrencia: 2026_MM_residual_review_match_old)
- Defenders Think in Lists, Attackers Think in Graphs.docx — line:26 (Mención de alias (no definición))

## Nota metodológica

La definición y las referencias se registran desde el catálogo; la prioridad, el caso concreto y la pregunta son adaptación editorial para el CISO, no evidencia experimental de eficacia. Aplicar como herramienta situada, no como explicación universal.

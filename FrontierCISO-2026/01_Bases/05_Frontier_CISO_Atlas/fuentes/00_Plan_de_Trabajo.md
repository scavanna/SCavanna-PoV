# Frontier CISO Atlas — Plan de trabajo

| Campo | Valor |
|---|---|
| Iniciativa | Frontier CISO Atlas 1.0, evolución del AI CISO Atlas |
| Fecha del plan | 15 de noviembre de 2026 |
| Solicitante y autoridad de aprobación | Santiago Cavanna |
| Línea base de partida | Taxonomía 5.3 · Core Ontology 1.0.0 · Curator 6.0 · TheNextCISO GM-24 V7.1 |
| Estado | Ejecutado el mismo día; el registro de lo hecho está en `docs/09_Bitacora_de_Tareas.md` |

## 1. Propósito

Construir una versión nueva del Atlas, llamada **Frontier CISO Atlas**, sobre lo ya construido. El cambio de nombre responde a una decisión de alcance: el Atlas deja de asociarse solo con la inteligencia artificial, que sigue siendo el principal motor de cambio, y pasa a describir el mapa completo de un tipo de CISO y de empresa: el que se para de frente al cambio tecnológico, lo incorpora y ajusta sus modelos mentales, sus capacidades y las de su oficina.

El Atlas responde una sola pregunta: **dónde estoy**. Para moverse por él hacen falta otras tres piezas, que este plan conecta pero no reemplaza:

- **TheNextCISO GM-24** (qué aprender y demostrar): 24 unidades y 379 conceptos en su versión 7.1.
- **MCCS**, el sistema metacognitivo del CISO (cómo pensar, sostener la decisión, ejecutar y evolucionar): pilares MM, OS, DO y NX.
- **H**, la dimensión de homeostasis evolutiva (en qué medio se navega): horizontes, fuerzas que aceleran, fuerzas que inhiben, mecanismos que estabilizan y contexto de ejecución.

## 2. Resultados esperados

1. Una **taxonomía revisada** (X territorios, Y dominios, Z funciones, H) con cada cambio de cantidad justificado por evidencia, y con cada «no cambio» también justificado.
2. Una **ontología actualizada** que represente lo que GM-24 V7.1 y sus anexos agregaron: producto-control, fuerza de trabajo híbrida, agentes, niveles de autonomía, instancias de dominio, medición, y el puente con MCCS y con H.
3. Un **grafo de conocimiento candidato**, construido con los pre-ensayos ya desarrollados y categorizados con la taxonomía nueva, más la lista precisa de lo que falta para convertirlo en grafo aprobado.
4. La **documentación** del Atlas nuevo y el **registro de las tareas realizadas**.

## 3. Alcance

**Dentro del alcance**

- Revisión de la taxonomía contra una base de referencia ampliada de organismos y artefactos, verificada en fuentes oficiales al 15 de noviembre de 2026.
- Unificación del corpus de pre-ensayos (GM-24 V7.1 y ampliaciones del Atlas) y su categorización completa.
- Ontología 2.0, catálogos en JSON, validadores y esquema de persistencia.
- Grafo candidato en SQLite, conjuntos de cambios propuestos y consultas de aceptación.
- Instrucciones actualizadas para el agente curador.

**Fuera del alcance**

- Redactar los ensayos finales: los pre-ensayos siguen siendo pre-ensayos.
- Asignar identificadores ESS, aprobar conjuntos de cambios o declarar un grafo aprobado: son decisiones humanas.
- Modificar el contenido del GM-24 V7.1 (plano A) o de las instancias de dominio (plano B).
- Regenerar los sitios web, libros de Excel y presentaciones de tareas anteriores con la taxonomía nueva (queda como trabajo derivado).

## 4. Principios de trabajo

Se conservan las decisiones de arquitectura vigentes: la taxonomía ubica, la ontología da significado, el grafo conserva relaciones aprobadas, el agente propone, el validador verifica y la autoridad humana aprueba. Se agregan cuatro reglas para este trabajo:

1. **Ningún código se renumera ni se reutiliza.** Lo nuevo recibe códigos nuevos; lo existente conserva código y nombre, y si cambia su alcance se dice.
2. **Cada cambio de cantidad pasa una prueba explícita** (sección 6). Lo que no la pasa queda en una lista de vigilancia con el criterio que no cumplió.
3. **Todo lo generado en este trabajo es candidato.** La categorización, las relaciones y el grafo quedan en estado propuesto hasta la revisión humana.
4. **Los silencios se declaran.** Lo que no se pudo verificar o no existe en las fuentes se registra como silencio y no se completa por inferencia.

## 5. Fases, actividades y entregables

| Fase | Actividades | Entregable | Criterio de terminado |
|---|---|---|---|
| F0 · Relevamiento | Leer la documentación y los catálogos del AI CISO Atlas; abrir el paquete maestro GM-24 (versión del 15-nov, la más completa); ubicar las definiciones de MCCS | Inventario de la línea base | Versiones y conteos de partida confirmados contra los archivos |
| F1 · Plan | Fijar objetivos, criterios de decisión, controles y entregables | Este documento | Plan escrito antes de modificar catálogos |
| F2 · Base de referencia | Verificar en fuentes oficiales versión, estado y estructura de primer nivel de los artefactos de cada organismo | Base de referencia y cinco informes de verificación | Cada artefacto con versión, fecha, estado, fuente y grado de verificación |
| F3 · Revisión de la taxonomía | Medir la presión del corpus sobre la taxonomía 5.3; cruzar los elementos de primer nivel de los artefactos con los dominios; aplicar las pruebas de admisión | Taxonomía 6.0 con decisiones justificadas, tabla de migración y lista de vigilancia | Cada candidato con decisión, evidencia y regla de frontera |
| F4 · Ontología | Extender tipos, relaciones y reglas a partir de GM-24 V7.1, sus anexos, MCCS y H; normalizar los predicados editoriales | Ontología 2.0 (cuatro diccionarios) y registro de cambios | Verificación de consistencia interna sin errores |
| F5 · Categorización del corpus | Unificar los pre-ensayos; asignar coordenadas X, Y, Z, H y pilar MCCS con justificación y nivel de confianza; validar de forma determinista | Corpus categorizado y tabla de cambios frente a 5.3 | 100 % de los pre-ensayos con registro válido; cambios de dominio revisados uno por uno |
| F6 · Grafo candidato | Cargar taxonomía, corpus, currículo, referencias, productos-control, agentes y tareas; generar conjuntos de cambios propuestos; validar contra la ontología; ejecutar consultas de aceptación | Base SQLite, exportaciones, conjuntos de cambios y resultados de consultas | Cero violaciones de tipo, dominio, rango y par permitido |
| F7 · Documentación | Redactar resumen, fundamentos, taxonomía, base de referencia, ontología, grafo, categorización, decisiones y bitácora | Documentos 01 a 10 | Cifras de los documentos generadas desde los datos |
| F8 · Verificación y cierre | Controles de integridad, empaquetado, publicación y memoria del proyecto | Paquete publicado y manifiesto | Controles en verde y manifiesto con huellas SHA-256 |

## 6. Pruebas de admisión para cambiar cantidades

**Dominio nuevo (eje Y).** Se admite si cumple las cinco condiciones:

- **C1 · Reconocimiento externo:** al menos cinco artefactos de al menos tres organismos lo tratan como elemento de primer nivel.
- **C2 · No representable:** no puede expresarse con un dominio existente, ni con una combinación de territorio y dominio, sin perder la identidad de la disciplina.
- **C3 · Presión o materialidad:** el corpus muestra ubicaciones forzadas, o existe un calendario normativo o tecnológico que lo vuelve material en el horizonte de planificación.
- **C4 · Permanencia:** es una disciplina estable, no un producto ni una moda.
- **C5 · Frontera clara:** se puede escribir una regla que lo separe de sus vecinos.

**Territorio nuevo (eje X).** Se admite si algún elemento de los marcos que describen el rol (certificaciones de dirección, perfiles de competencias, guías para directorios, ejes del GM-24, pilares de MCCS) queda sin territorio, o si el corpus acumula pre-ensayos sin territorio asignable.

**Función nueva (eje Z).** Las seis funciones son las oficiales de NIST CSF 2.0: solo cambian si cambia el marco. Las subfunciones son editoriales: se agrega una cuando una categoría oficial del marco no tiene subfunción con el mismo prefijo de función.

**Fuerzas y contexto (H).** Se agrega una fuerza, un mecanismo o un factor cuando las fuentes del proyecto lo describen y ninguno de los existentes lo contiene.

## 7. Controles de calidad

- Validación determinista de catálogos, de cada lote de categorización y de cada arista del grafo.
- Revisión individual de todo cambio de dominio primario hacia un dominio nuevo.
- Conteos de control entre fuentes (GM-24 V7.1, banco del Atlas, corpus unificado).
- Separación entre edición pública e información interna en los atributos del grafo.
- Manifiesto con huellas SHA-256 del paquete.

## 8. Riesgos y supuestos

| Riesgo o supuesto | Tratamiento |
|---|---|
| Los siete documentos canónicos de la taxonomía 5.3 y de la ontología 1.0 no están en el proyecto | Se trabaja con los catálogos JSON del proyecto; se declara como pendiente de recuperación |
| La categorización la proponen agentes de lectura | Queda como candidata, con confianza y justificación, y con revisión de los cambios |
| Algunas fuentes externas no permiten verificación completa | Se marca «parcial» o «no verificado» y se conserva el informe de verificación |
| Publicaciones inminentes (COBIT 7 el 19 de noviembre; Ignite del 17 al 20 de noviembre) | Se registran como revalidaciones pendientes |
| MCCS tiene dos lecturas del pilar OS en las notas de origen (persona y oficina) | Se adoptan como dos escalas del mismo pilar y se deja para confirmación |

## 9. Entregables

Paquete `Frontier_CISO_Atlas_v1.0` con: plan, diez documentos, catálogos de taxonomía y ontología, base de referencia, corpus categorizado, grafo candidato, conjuntos de cambios, guiones de construcción y validación, instrucciones del agente curador y manifiesto.

## 10. Decisiones que quedan en manos humanas

Aprobar o ajustar la taxonomía 6.0 y la ontología 2.0; validar la categorización; decidir la primera ola de ensayos; asignar identificadores ESS; aprobar conjuntos de cambios; decidir qué se publica y con qué licencia.

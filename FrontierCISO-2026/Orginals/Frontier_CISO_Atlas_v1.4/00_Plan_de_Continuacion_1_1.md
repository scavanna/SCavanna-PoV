# Frontier CISO Atlas — Plan de continuación (versión 1.1)

| Campo | Valor |
|---|---|
| Iniciativa | Frontier CISO Atlas 1.1, continuación de la versión 1.0 |
| Fecha del plan | 15 de noviembre de 2026 |
| Solicitante y autoridad de aprobación | Santiago Cavanna |
| Pedido | «Informar estatus y continuar» |
| Línea de partida | Frontier CISO Atlas 1.0 publicado: Taxonomía 6.0, Ontología 2.0.0, grafo candidato de 3.378 nodos, decisiones D-01 a D-07 abiertas |
| Estado | Ejecutado el mismo día; el registro está en `docs/09_Bitacora_de_Tareas.md`, fases 9 a 14 |

## 1. Punto de partida

- La versión 1.0 está publicada e íntegra. No hay decisiones registradas sobre D-01 a D-07.
- La 1.0 dejó nueve pendientes ordenados (`docs/10_Glosario_y_Continuidad.md`, sección 6 de esa versión).
- Dos hechos nuevos: el proyecto tiene un catálogo de indicadores más reciente, el del Modelo Operativo CISO 365 2.0; y existe una base de integración de la Biblioteca cognitiva que la 1.0 no había localizado.

## 2. Criterio para elegir qué continuar

Se continúa un pendiente solo si cumple las tres condiciones:

1. No depende de una decisión que te corresponde a vos.
2. No modifica un artefacto vigente: ni el GM-24, ni el banco de pre-ensayos, ni tu base de la Biblioteca, ni el catálogo de indicadores.
3. Su resultado puede quedar como propuesta, separado de lo ya entregado.

Con ese criterio entran los pendientes 4 a 7. Quedan fuera los pendientes 1 a 3 (decisiones, revisión del curador y redacción de ensayos), el 8 (revisión de D21 a D23, que es un cambio de taxonomía) y el 9 (edición pública).

## 3. Alcance

**Dentro del alcance**

- Incorporar la Biblioteca cognitiva al grafo candidato, a partir de tu base de integración.
- Incorporar el catálogo de indicadores 2.0, ubicar indicadores en PR06 y RC05 y proponer indicadores por variable homeostática.
- Revisar la propuesta de ontología en lo que haga falta para cargar ese contenido.
- Preparar la propuesta de remapeo del GM-24 a MITRE ATT&CK v20, MITRE ATLAS v2026.10 y CSA CCM v4.1.
- Leer todo el dominio D20 con la regla de alcance, para que la decisión D-03 tenga el impacto a la vista.
- Proponer pre-ensayos para las celdas sin contenido.
- Actualizar la documentación y registrar las tareas.

**Fuera del alcance**

- Cambiar la Taxonomía 6.0, la base de referencia o la categorización de los 739 pre-ensayos.
- Aplicar el remapeo, mover pre-ensayos de D20 o sumar pre-ensayos al corpus.
- Redactar ensayos, asignar identificadores de ensayo o aprobar conjuntos de cambios.
- Revalidar lo que depende de Ignite 2026 y de COBIT 7, que todavía no ocurrieron.
- Cargar las notas del MCCS y el Documento Maestro del CISO-OS, que son texto sin estructurar y necesitan curaduría.

## 4. Reglas de trabajo

Se mantienen las del plan original. Se agregan cinco:

1. **Lo entregado no se toca.** La versión 1.0 queda publicada como está. La 1.1 se publica aparte y la contiene.
2. **Las fuentes del autor se leen, no se modifican.** De tu base se respeta su estado («propuesta para revisión, no aplicada al grafo») y su advertencia sobre los vínculos débiles.
3. **Solo se carga lo que la fuente enuncia.** No se infieren vínculos entre prácticas y sesgos por conocimiento general.
4. **Lo que proponga yo se dice.** Los indicadores por variable homeostática, la lectura de D20 y los pre-ensayos nuevos son propuestas mías y así quedan marcadas.
5. **Sin agentes auxiliares.** Guiones deterministas y lectura directa.

## 5. Tareas y criterio de terminado

| Tarea | Entregable | Terminado cuando |
|---|---|---|
| Comprobar la versión 1.0 | Verificación del manifiesto | Todos los archivos coinciden con su huella |
| Revisar la ontología | Ontología 2.1.0 | Verificación de coherencia interna sin errores |
| Extraer y tipificar la Biblioteca | Extracto, catálogo y estadísticas | Los 1.404 conceptos tienen tipo por regla escrita |
| Incorporar la medición | Extracto, indicadores en el Atlas e indicadores por variable | Cada variable y cada subfunción tienen al menos un indicador |
| Preparar el remapeo | Tabla vínculo por vínculo | Cada vínculo afectado tiene propuesta y regla |
| Leer D20 | Tabla con lectura y fundamento | Los 71 pre-ensayos tienen lectura |
| Proponer pre-ensayos | Texto, coordenada y referencias | Los códigos validan contra la Taxonomía 6.0 |
| Reconstruir el grafo | Grafo candidato y conjuntos de cambios | Cero errores de validación; conjuntos 01 a 09 sin cambios |
| Documentar | Documentos actualizados y dos nuevos | Las cifras salen de los datos |
| Empaquetar y publicar | Paquete 1.1 | Regeneración desde los guiones sin diferencias |

## 6. Controles

- Huella de los archivos de operaciones de los conjuntos 01 a 09, igual a la de la versión 1.0.
- Validación determinista del grafo completo, incluida la regla nueva de medición.
- Validación de códigos y cardinalidades de los pre-ensayos propuestos.
- Lectura uno por uno de los vínculos entre prácticas y sesgos de confianza media.
- Regeneración del paquete desde sus propios guiones.

## 7. Riesgos y supuestos

| Riesgo o supuesto | Tratamiento |
|---|---|
| La regla de tipos por categoría puede tipificar mal conceptos de categorías mixtas | Los casos sin tipo claro quedan como `Concept`; el tipo original se conserva; decisión D-08 |
| Los vínculos entre prácticas y sesgos que salen de textos repetidos aportan poco | Llevan confianza baja y método declarado |
| Los indicadores por variable homeostática son una lectura mía | Marcados como propuesta de diseño; decisión D-09 |
| La versión del catálogo de indicadores puede cambiar | Se registran la versión y la huella del archivo usado |
| Sumar contenido al grafo puede leerse como aprobación | Todo sigue en estado «candidato» y los conjuntos, «propuesto» |

## 8. Entregables

Paquete `Frontier_CISO_Atlas_v1.1`, que contiene la versión 1.0 más: dos documentos nuevos, la ontología 2.1.0, el grafo candidato reconstruido con quince conjuntos de cambios, doce archivos de datos nuevos, las instrucciones 7.1 del agente curador y este plan.

## 9. Decisiones que quedan en tus manos

Las siete de la versión 1.0 y tres nuevas: cómo entra la Biblioteca al grafo (D-08), qué indicadores miden cada variable (D-09) y qué se hace con el remapeo y con los pre-ensayos propuestos (D-10).

# Frontier CISO Atlas — Plan de continuación (versión 1.3)

| Campo | Valor |
|---|---|
| Iniciativa | Frontier CISO Atlas 1.3: decisiones del autor, reglas adoptadas y relectura del corpus |
| Fecha | 16 de noviembre de 2026 |
| Punto de partida | Versión 1.2 publicada, con cuatro decisiones abiertas (D-14, D-11, D-13 y D-12) y la revisión humana pendiente |
| Pedido | Cuatro frases del autor: «Confirmo las siete.», «Acepto el cambio de reglas», «Confirmo el resto de los cambios.» y «No revisar la biblioteca». El autor no pidió una versión nueva con esas palabras: esta versión es la consecuencia que se le había anticipado al presentarle las decisiones (anotar sus respuestas, actualizar los estados y releer los pre-ensayos que alcanzan las reglas que adoptara) |
| Regla que obliga | ADR-027, que el autor confirmó: cada versión se revisa antes de publicarse |

## 1. Qué se planificó y cómo quedó

| N.º | Tarea | Resultado |
|---|---|---|
| 1 | Registrar las respuestas del autor, separando lo literal de lo leído en una frase general y de lo que no contestó | 7 respuestas literales, 10 leídas de una frase general, 2 sin respuesta. La columna de notas del autor queda vacía |
| 2 | Incorporar las reglas adoptadas a la taxonomía | 60 enunciados adoptados, 11 preguntas que siguen abiertas, 3 encargos hechos y 21 en cola. Definición de D03 y 34 definiciones de trabajo de subfunciones |
| 3 | Releer el corpus con las reglas adoptadas, con dos lecturas a ciegas | Primera lectura de 755 pre-ensayos; segunda, de 483 |
| 4 | Aplicar los cambios en que las dos lecturas coinciden y reconstruir el grafo | 260 coordenadas en 204 pre-ensayos del corpus y 10 en 8 de la serie APX; 312 casos quedan para el autor |
| 5 | Revisar la versión candidata antes de publicarla (ADR-027) | Cinco revisores automáticos sobre la versión candidata: 69 hallazgos (4 altos); 58 corregidos, 6 corregidos en parte y 5 documentados. Tercera lectura de 80 casos: en los 60 ejes que la versión candidata cambiaba, prefiere el valor nuevo en 52 y el anterior en 4. Después de la revisión se retiraron los cambios que dependen de seis puntos sin decidir |
| 6 | Documentar, verificar y publicar | Paquete 1.3 publicado; las versiones 1.0, 1.1 y 1.2 no se modificaron |

## 2. Qué no entró en esta versión

- Los 21 encargos en cola: el modelo de referencia del eje H, los criterios de admisión de dominios, las anclas del MCCS, las familias de dominios y el registro del plano en los nodos. Son trabajo de diseño sobre el modelo.
- La próxima revisión de la ontología (solicitud OCR-CAND-03). La Ontología 2.1.0 no cambió.
- La relectura de los indicadores, de las preguntas de la matriz y de la Biblioteca con las reglas adoptadas.
- La revisión humana. El autor no respondió sobre ella y sigue siendo una propuesta, rediseñada con la evidencia de la relectura.

## 3. Qué salió distinto de lo planificado

- **La regla de decisión quedó más estricta que la que el autor confirmó.** Además de las dos lecturas coincidentes, exige que ninguna haya declarado confianza baja. Se decidió con la primera lectura incompleta y antes de que existiera la segunda.
- **Apareció un defecto de la versión 1.2 publicada.** En su grafo, 394 aristas declaraban un cambio ocurrido en otro eje. Se corrigió en esta versión.
- **Hubo que precisar una afirmación de la versión 1.2.** La «regeneración en una copia limpia» regenera sobre una copia del paquete, no desde una carpeta vacía.
- **La segunda lectura necesitó un lote adicional.** Se había armado antes de que cerrara la primera.
- **El curador dio seis avisos falsos y detuvo cinco revisores sin necesidad.** Avisó que los lanzamientos llevaban una selección de modelo que el autor no había pedido; el registro de la sesión muestra que los 42 lanzamientos llevan solo los cinco campos admitidos. El detalle está en el documento 14, sección 9.

## 4. Entregables

Paquete `Frontier_CISO_Atlas_v1.3`: los documentos 01 a 14, la taxonomía con las reglas adoptadas, el corpus releído, el grafo candidato, 16 conjuntos de cambios en estado «propuesto», las instrucciones 7.3 del agente curador, el material de la relectura (`relectura_1_3/`), el de la revisión de esta versión (`revision_1_3/`) y este plan. El detalle está en `docs/14_Decisiones_y_relectura_1_3.md`.

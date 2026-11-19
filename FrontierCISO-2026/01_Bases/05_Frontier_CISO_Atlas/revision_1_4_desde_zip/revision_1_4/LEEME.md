# Revisión de la versión candidata 1.4

Antes de publicar, seis revisores automáticos que no habían participado en la versión trabajaron sobre una copia congelada del paquete candidato. Lo pide la decisión de arquitectura ADR-027, que el autor confirmó. El resumen está en `docs/15_Decisiones_delegadas_y_relectura_1_4.md`, sección 9.

## Qué hay

| Archivo o carpeta | Qué es |
|---|---|
| `ENCARGO_COMUN.md` | El contexto y las reglas que recibieron los seis revisores |
| `ENCARGO_V1.md` a `ENCARGO_V6.md` | La pregunta de cada revisor |
| `v1/` a `v6/` | Lo que dejó cada uno: sus hallazgos (por ejemplo, `revision_1_4/v1/hallazgos.jsonl`) y su nota de cierre (`revision_1_4/v1/cierre.md`), y los guiones de comprobación que guardó |
| `hallazgos_y_decisiones.csv` | Los 128 hallazgos, con la decisión del curador y la acción de cada uno |

| Revisor | Qué miró | Hallazgos | Altos |
|---|---|---|---|
| V1 | Si el registro dice lo que el autor dijo | 25 | 3 |
| V2 | Si las cifras son las de los datos | 15 | 0 |
| V3 | Si la vara se aplicó como dice y si las reglas son coherentes | 19 | 2 |
| V4 | Si lo que el paquete concluye está sostenido por lo que midió | 22 | 6 |
| V5 | Si la ontología y el grafo hacen lo que el paquete dice | 22 | 1 |
| V6 | Si el autor puede hacer lo que el paquete le pide | 25 | 3 |

## Cómo leer los resultados

- **Los hallazgos** son de revisores automáticos del mismo tipo que quien generó el paquete. Encuentran contradicciones, cifras que no coinciden y afirmaciones sin respaldo; no validan el contenido.
- **Las decisiones** son del curador: 98 corregidos, 16 corregidos en parte y 14 documentados. Lo que se corrigió a partir de esta revisión no tuvo otra lectura.
- Los hallazgos citan el paquete tal como estaba cuando se congeló. Después de las correcciones, una cita puede no coincidir con el texto publicado: la columna `accion` dice qué cambió.

## Lo que salió distinto de lo planeado

- El curador detuvo dos veces el lanzamiento de los revisores (ocho pedidos en total) por una lectura equivocada del registro: creyó que había pedido un modelo que el autor no eligió. No era así. Le dijo al autor que la revisión quedaba frenada y lo corrigió a los pocos minutos. Los seis revisores retomaron desde el principio con el mismo encargo y el mismo paquete.
- El curador empezó a corregir las fuentes mientras los revisores seguían leyendo. Los revisores leyeron el paquete congelado, que no cambió; pero las correcciones no esperaron al cierre de la revisión.
- Lo que se corrigió después no tuvo otra lectura independiente: lo comprueba solo la regresión.
- Al último revisor se le pidió cerrar cuando los otros cinco ya habían terminado: su nota de cierre dice qué no llegó a revisar.
- Ningún hallazgo quedó como «no se acepta». Eso no dice que todos estén resueltos: los que figuran como «documentado» o «corregido en parte» siguen abiertos y están en los pendientes declarados.

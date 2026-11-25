# Relectura del corpus con las reglas adoptadas · versión 1.3

Esta carpeta guarda lo que recibió y lo que devolvió cada lector de la relectura, y los guiones que la armaron y la integraron. El resultado y su lectura están en `docs/14_Decisiones_y_relectura_1_3.md`, sección 4.

## Qué hay

| Archivo o carpeta | Qué es |
|---|---|
| `REGLAS.md` | El texto de reglas que recibió cada lector: la Taxonomía 6.0, las ocho reglas base, los enunciados adoptados el 16 de noviembre de 2026, las definiciones de trabajo de las subfunciones y las seis preguntas abiertas que podía anotar |
| `ENCARGO.md` | El encargo: qué leer, qué asignar, en qué formato y con qué reglas de independencia |
| `lotes/` | Primera lectura: 19 lotes con 755 registros. `lotes/lote_NN.jsonl` es lo que recibió el lector y `lotes/DESPACHO_NN.md`, la instrucción con que arrancó |
| `salidas/` | Primera lectura: `salidas/salida_NN.jsonl` es lo que devolvió el lector y `salidas/cierre_NN.md`, su nota de cierre |
| `lotes2/` y `salidas2/` | Segunda lectura: 13 lotes con 483 registros, con la misma estructura |
| `segunda_lectura.json` | Cómo se armó la segunda lectura: los pre-ensayos en que la primera difiere de la coordenada vigente, los de la serie APX, la muestra de control y el complemento |
| `primera_lectura.sha256` y `segunda_lectura.sha256` | La huella SHA-256 de las salidas de cada lectura, concatenadas en orden de lote |
| `preparar.py`, `reglas13.py` | Son el registro de cómo se armaron las reglas para los lectores, el encargo y los lotes. Volver a ejecutar `preparar.py` los sobrescribe y no hace falta para reproducir la integración |
| `validar.py` | Comprueba el formato de una salida. Lo ejecutó cada lector y lo volvió a ejecutar el curador |
| `comparar.py` | Compara la primera lectura con la coordenada vigente. Con él se armó la segunda lectura |
| `integrar.py` | Decide eje por eje y escribe `scripts/datos_de_trabajo/ajustes_relectura_1_3.json`, el archivo desde el que entran los cambios |

## Qué recibió un lector

Cada registro de un lote trae el identificador, la serie, el título, la tesis y el texto del pre-ensayo. No trae la coordenada vigente, la de la Taxonomía 5.3 ni la lectura de otro lector. El despacho le pedía no abrir ningún archivo fuera de los suyos. Eso no se puede comprobar después: es lo que se pidió, no una garantía. Un lector de la primera lectura (lote 04) declaró en su cierre que ejecutó un listado de la carpeta de salidas.

Los lectores son automáticos y tienen la misma configuración que quien generó los artefactos del paquete. Que dos coincidan hace menos probable un desliz de lectura y no dice nada de un error que compartan.

## Cómo se decide

Un eje cambia cuando las dos lecturas coinciden entre sí y difieren del valor vigente, salvo que alguna haya anotado una pregunta abierta que afecta a ese eje, que alguna haya declarado confianza baja o que el cambio caiga en uno de los puntos que la revisión de la versión candidata dejó abiertos (`reglas13.py`, `PUNTOS_REVISION`). Las dos primeras salvedades están escritas en `integrar.py` y se fijaron antes de que existiera la segunda lectura. En cualquier otro caso el valor queda como estaba y el caso se informa con las dos lecturas.

Para reproducir la integración, desde la raíz del paquete: `python3 relectura_1_3/integrar.py`. Vuelve a escribir el archivo de ajustes a partir de las salidas.

## Lo que salió distinto de lo planeado

- **La segunda lectura se armó antes de tiempo.** Se armó con las 755 primeras lecturas escritas y validadas, pero cuando cuatro lectores todavía podían corregir su salida. Al cerrar la primera lectura, un pre-ensayo (APC-066) había pasado de coincidir a diferir y no estaba en la segunda. Se agregó el lote 13, con ese pre-ensayo y siete de control.
- **Un lector terminó sin escribir su salida.** El del lote 13 de la segunda lectura cerró su primer turno sin archivos; los escribió después de un mensaje que se lo pidió.
- **El curador avisó, sin razón, que los lectores se habían lanzado con una selección de modelo que el autor no pidió.** El registro de la sesión muestra que los 32 lanzamientos llevan solo los cinco campos admitidos. El detalle está en el documento 14, sección 9.
- **Faltó un código en el encargo.** Las definiciones de trabajo de las subfunciones remiten a fronteras que ninguna regla adoptada decide, y el lector no tenía cómo anotar que un caso dependía de una de ellas. Solo podía anotar las seis preguntas abiertas de `REGLAS.md`.
- **En los despachos se reemplazó la ruta de trabajo del entorno por la carpeta del paquete.** El resto del texto es literal.

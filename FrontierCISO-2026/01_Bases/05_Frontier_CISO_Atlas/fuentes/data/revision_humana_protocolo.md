# Revisión humana de la categorización · protocolo

Frontier CISO Atlas 1.4 · Este archivo no muestra ningún resultado de la relectura. Para leer a ciegas hay que leerlo, y leer la planilla, antes de abrir los documentos 15 y 18.

## Qué se revisa

Territorio primario, dominio primario y subfunción primaria de cada pre-ensayo de la muestra. El horizonte, las fuerzas y el pilar no entran.

## Quién

- El autor, o una persona con formación de CISO que él designe. El agente curador mantiene el paquete y no hace esta revisión.
- Con una sola persona, que además es el autor del banco, el resultado es «revisada por el autor en una muestra».
- Para decir «validada» hace falta una segunda persona, que lea al menos un tercio de la muestra sin ver la lectura de la primera. Se informa cuánto coinciden las dos.

## Con qué reglas

Con la Taxonomía 6.1 y sus reglas de asignación, revisión 3: las reglas base, los enunciados adoptados, las reglas decididas por delegación y las definiciones de trabajo de las 35 subfunciones (documento 16). El documento 16 trae las reglas decididas y las definiciones; el texto completo, con las reglas base y los enunciados adoptados, es el que recibieron los lectores automáticos: relectura_1_4/lectura_a/REGLAS.md. Las reglas decididas por el curador no las vio el autor: si al leer no está de acuerdo con una, conviene anotarlo en la columna de observaciones, porque eso también es un resultado.

## La muestra

193 pre-ensayos, sorteados en cuatro estratos. La planilla no dice de qué estrato es cada caso. Los 16 pre-ensayos de la serie APX no entran en el sorteo: son pocos y conviene leerlos todos, con data/ampliacion_celdas_en_blanco.csv.

| Estrato | Qué reúne | Pre-ensayos del corpus | En la muestra |
|---|---|---|---|
| R1 | Cambió con la relectura de la versión 1.4: en algún eje, las dos lecturas a ciegas coincidieron en otro valor con confianza alta y la tercera lo prefirió, o el cambio salió del nuevo alcance de RC04 | 87 | 39 |
| R2a | No cambió, y habría cambiado con la vara fijada antes de leer: en algún eje, las dos lecturas coincidieron en otro valor, la tercera lo prefirió y alguna de las dos declaró confianza media | 243 | 53 |
| R2b | Alguna lectura a ciegas apunta fuera de la coordenada y el cambio no entró por otro motivo: las lecturas no coinciden, una declaró confianza baja, la tercera lectura no prefirió el valor nuevo o el eje está protegido | 164 | 48 |
| R3 | Las dos lecturas a ciegas sostienen la coordenada en los tres ejes | 245 | 53 |

| Tanda | Qué | Pre-ensayos | Para qué alcanza |
|---|---|---|---|
| 1 | Los primeros 20 casos sorteados de cada estrato, mezclados. | 80 | Una primera estimación, con un margen amplio, y una primera mirada a si la relectura mejoró o empeoró lo que cambió |
| 2 | El resto de los casos sorteados. | 113 | Lleva la estimación al margen del diseño completo |

**Esfuerzo.** 5 minutos por pre-ensayo. Es un supuesto, no una medida: conviene cronometrar los primeros diez. El diseño completo son 193 pre-ensayos, unas 16,1 horas, con un margen de 6,4 puntos para la estimación de todo el corpus. El camino mínimo es la tanda 1: 80 pre-ensayos, unas 6,7 horas y un margen de 11,3 puntos. Da una estimación para todo el corpus con ese margen. Los resultados por estrato, de veinte casos cada uno, casi nunca concluyen.

## Pasos

1. **Fijar el umbral antes de abrir la clave.** Qué parte de coincidencia se considera suficiente: un umbral para los tres ejes, o uno por eje. Los umbrales los fija el autor, antes de mirar la clave. Este paquete no propone valores.
2. **Leer a ciegas.** La planilla trae el mismo registro que recibieron los lectores automáticos: el título, la tesis ya ubicada y de dónde se tomó, las oraciones que la preceden y el texto, con la oración de plantilla reemplazada por una marca donde la había. La muestra no trae identificadores ni coordenadas: cada caso lleva un número de orden y la clave lo une con su identificador, su estrato y sus valores en las versiones 1.2 y 1.4. Para leer a ciegas hay que leer la muestra antes de abrir la clave, los documentos 15 y 18 y los archivos de la relectura: esos documentos nombran pre-ensayos que están en la muestra y dicen qué lectura tuvo cada uno. El protocolo está aparte, en data/revision_humana_protocolo.md, y no muestra resultados. Si ya abriste el documento 15, sus tablas nombran con sus valores algunos pre-ensayos de la muestra (los casos de D20, los ejes protegidos y los cambios de RC04): esos casos ya no se leen a ciegas, y hay que decirlo al informar el resultado. Algunos textos nombran su unidad o su tema en el cuerpo: eso no se quitó.
3. **Anotar en una copia.** Copiar data/revision_humana_muestra.csv con otro nombre, fuera de la carpeta data/, y anotar en la copia. En cada celda va solo el código: por ejemplo T04, D12 o ID03. Una celda vacía deja ese eje sin evaluar en ese caso. Se guarda como CSV. El guion de cálculo rechaza, con un aviso, una anotación que no sea un código del catálogo.
4. **Calcular.** `python3 scripts/evaluar_revision_humana.py <la copia completada.csv> --umbral <valor entre 0 y 1>`. Con `--tanda 1` calcula solo el camino mínimo. scripts/evaluar_revision_humana.py lee la planilla completada, que se le pasa por argumento, y la clave, y calcula las medidas y sus intervalos. Los umbrales se le pasan como argumento: no trae valores por defecto.
5. **Decidir.** Cumple: El límite inferior del intervalo de coincidencia queda por encima del umbral. No cumple: El límite superior del intervalo queda por debajo del umbral. No concluyente: El umbral queda dentro del intervalo: la muestra no alcanza para decidir. El guion entrega un resultado por eje para todo el corpus y uno por eje para cada estrato. El del corpus responde si la categorización, en conjunto, cumple el umbral. El de cada estrato dice dónde están las diferencias: R1 es el de los ejes que la relectura cambió y R2a, el de los que habrían cambiado con la vara fijada antes de leer. Pueden no coincidir: si el corpus cumple y un estrato no, la categorización cumple en conjunto y ese estrato se relee. Si un estrato tiene menos de dos casos con un eje anotado, no hay resultado para el corpus en ese eje. Esta lectura la propone el curador: el autor puede fijar otra antes de abrir la clave.

| Resultado | Qué se hace |
|---|---|
| Cumple | La categorización pasa de «base de trabajo» a «revisada por el autor en una muestra», con la medida y su intervalo a la vista. Las diferencias del revisor se aplican. |
| No cumple | Los pre-ensayos del estrato que no cumple no se usan para redactar ensayos hasta que una persona los relea. Que los relea el mismo lector automático con las mismas reglas no alcanza: daría el acuerdo entre corridas que este paquete ya midió, y ese acuerdo no dice si la coordenada es correcta. Antes de releer se corrigen las reglas en que el revisor y las lecturas difieren, que es lo que la revisión deja a la vista. |
| No concluyente | Se amplía el sorteo o se acepta seguir con la categorización como base de trabajo. No se la llama revisada. |

## Las dos comparaciones

Hay dos comparaciones, y el guion da para cada una el conteo y un intervalo. En los ejes que cambiaron: si el intervalo queda entero del lado del valor de la versión 1.2, el revisor coincide más con el valor anterior y los cambios de la relectura quedan en duda. En los ejes que habrían cambiado con la vara fijada antes de leer: si el intervalo queda entero del lado del valor de las lecturas, el revisor coincide más con la vara fijada. Si el intervalo incluye la mitad, la muestra no alcanza para decidir entre las dos. Qué diferencia alcanza para cambiar de vara lo decide el autor antes de abrir la clave: este paquete no fija ese número. Los casos en que el revisor no coincide con ninguno de los dos se informan aparte y dicen cuánto queda sin resolver con cualquiera de las dos varas.

En la muestra hay 91 ejes, de 63 pre-ensayos, que sirven para comparar las dos varas; en la tanda 1 son 29, que no alcanzan para esa pregunta. Ejes de la muestra en que la vara fijada antes de leer daría un valor distinto del vigente. Son los que permiten comparar las dos varas con una lectura humana. El margen es el de una proporción estimada con esa cantidad de ejes, para los tres ejes juntos; por eje es mayor. Con el autor como único revisor la comparación no es neutral: el valor vigente de esos ejes es, en su mayoría, el que traía su propio banco.

## Qué se mide

- Por estrato y por eje: en qué parte de los pre-ensayos el revisor asigna el mismo primario que la coordenada vigente, con su intervalo de confianza del 95 %.
- Para todo el corpus: la misma medida, ponderada por el tamaño de cada estrato.
- En cada eje que la relectura cambió: si el revisor coincide con el valor nuevo, con el que tenía en la versión 1.2 o con ninguno de los dos. Dice si los cambios aplicados mejoraron o empeoraron la categorización.
- En cada eje que habría cambiado con la vara fijada antes de leer y no cambió: si el revisor coincide con el valor vigente, con el de las lecturas o con ninguno de los dos. Dice si convenía la vara que se aplicó o la que se había fijado.

## Límites

- La revisión mide el acuerdo entre el revisor y la categorización vigente. No prueba que la taxonomía ni sus reglas sean las correctas.
- Con un solo revisor, que es el autor del banco, la medida no es independiente de las coordenadas que él mismo asignó antes.
- El horizonte, las fuerzas y el pilar no entran en esta revisión.
- Los estratos salen de tres lecturas automáticas con la misma configuración: separan los casos en que esas lecturas dudan, no los casos en que se equivocan.
- La subfunción ID06 es nueva y RC04 cambió de alcance: en esos casos el valor de la versión 1.2 no se puede comparar sin más con el de la 1.4.

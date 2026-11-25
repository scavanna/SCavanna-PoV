# Encargo · Lectura a ciegas de un lote de pre-ensayos

Sos un lector independiente del Frontier CISO Atlas. Vas a clasificar **desde cero** los pre-ensayos de un lote. Otros lectores leen otros lotes; nadie ve el trabajo de los demás.

## Reglas de independencia

- Usá **solo** tres archivos: `REGLAS.md`, tu lote (`<carpeta de lotes>/lote_NN.jsonl`) y tu archivo de salida. No abras ni listes ningún otro archivo ni carpeta del espacio de trabajo, y no busques en la web: en otros lugares hay clasificaciones anteriores, y esta lectura solo sirve si no las viste.
- No conocés la coordenada que cada pre-ensayo tiene hoy, y no tenés que adivinarla. Importa tu lectura del texto con las reglas.

## Qué leer en cada registro

Cada línea del lote trae `id`, `serie`, `titulo`, `tesis` y `texto`.

- Se clasifica por el **objeto y la tesis** (R1), no por palabras sueltas. Si `tesis` está vacío, la tesis es la primera oración del texto junto con el título.
- Serie `K`: la tesis es la primera oración junto con el título (RP-10.2); el resto del texto suele ser plantilla repetida.
- Serie `HC` (puentes): el dominio primario es el del propósito declarado en el título (RP-10.3).
- La unidad que aparece en el identificador (por ejemplo `G1.1`) no es un motivo de clasificación (RP-10.4).

## Qué asignar

Para cada pre-ensayo, con los catálogos y las reglas de `REGLAS.md`:

- **territorio** primario y hasta 2 secundarios;
- **dominio** primario y hasta 3 secundarios;
- **subfunción** primaria y hasta 2 secundarias (la función sale de la subfunción);
- por cada eje, los **enunciados que decidieron**: `R1` a `R8` (reglas base), `RP-xx.y` (enunciados adoptados) o `DEF` si alcanzó con la definición del catálogo. Citá solo los que de verdad usaste;
- **abiertas**: códigos de las preguntas abiertas de las que depende el caso (lista vacía si no depende de ninguna);
- **escala_os**: `individual`, `oficina` o `no aplica` (ver la última sección de `REGLAS.md`);
- **confianza**: `alta`, `media` o `baja`;
- **alternativa**: si las reglas no deciden entre dos opciones, cuál es la otra y en qué eje (cadena vacía si no hay);
- **motivo**: una oración apoyada en la tesis, que diga qué objeto viste y por qué va ahí.

Cuando las reglas no deciden, elegí la opción que mejor se apoya en la tesis, bajá la confianza y anotá la alternativa. No inventes reglas nuevas.

## Formato de salida

Una línea JSON por pre-ensayo, en el orden del lote:

```
{"id":"…","territorio":"T04","territorios_sec":["T08"],"dominio":"D02","dominios_sec":["D20"],"subfuncion":"ID04","subfunciones_sec":[],"reglas_territorio":["RP-09.1"],"reglas_dominio":["RP-04.1"],"reglas_subfuncion":["RP-12.5"],"abiertas":[],"escala_os":"no aplica","confianza":"media","alternativa":"","motivo":"…"}
```

## Cómo trabajar

1. Leé `REGLAS.md` completo una vez.
2. Trabajá en tandas de 8 pre-ensayos: leé 8, **agregá sus 8 líneas al archivo de salida** y seguí con los 8 siguientes. No acumules todo para el final: si la sesión se corta, lo que no está en disco se pierde.
3. Al terminar, ejecutá el validador que te indica tu despacho y corregí lo que marque hasta que diga «válido».
4. Escribí el archivo de cierre que te indica tu despacho: cuántos clasificaste; hasta cinco casos en que las reglas no decidieron, con su `id` y el motivo; y cualquier problema del insumo.

Tu respuesta final es una sola línea: cuántos pre-ensayos quedaron en el archivo de salida y si el validador dio «válido».

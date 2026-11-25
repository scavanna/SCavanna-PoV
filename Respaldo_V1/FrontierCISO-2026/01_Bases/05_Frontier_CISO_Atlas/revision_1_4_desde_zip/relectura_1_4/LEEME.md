# Relectura del corpus con la vara de tres lecturas · versión 1.4

Esta carpeta guarda lo que recibió y lo que devolvió cada lector de la relectura de la versión 1.4, y los guiones que la armaron y la integraron. El resultado y su lectura están en `docs/15_Decisiones_delegadas_y_relectura_1_4.md`, secciones 3 y 4.

Todos los lectores son agentes automáticos del mismo tipo. Nada de esto es una revisión humana.

## Qué hay

| Carpeta o archivo | Qué es |
|---|---|
| `lectura_a/` y `lectura_b/` | Las dos lecturas a ciegas completas. Cada carpeta es lo que vio un lector: `REGLAS.md` (el mismo texto en las dos), `ENCARGO.md`, el validador, los catálogos, 19 lotes (`lotes/lote_NN.jsonl`), la instrucción con que arrancó cada lector (`despachos/DESPACHO_NN.md`), lo que devolvió (`salidas/salida_NN.jsonl`) y su nota de cierre (`salidas/cierre_NN.md`). Cada lectura tiene 755 registros, con repartos distintos |
| `tercera_lectura/` | La lectura de elección forzada: 14 lotes con 556 casos. En `clave/clave_r6.json` está la clave, que dice cuál de los dos valores de cada caso era el de la base. Los lectores no la tuvieron |
| `escala_os/` | La escala del pilar OS: dos lecturas completas de 147 pre-ensayos, en cuatro lotes cada una, y su consolidación (`resultado_os.json`) |
| `revision_previa/` | La revisión de las reglas antes de la lectura: el texto de reglas que se revisó, los 123 patrones contrastados, las 45 contradicciones anotadas, la muestra piloto de 30 pre-ensayos y sus 69 hallazgos, y las reglas y los vacíos tal como estaban antes de corregirlos |
| `notas_de_cierre/` | Las observaciones de las notas de cierre de las dos lecturas, ordenadas por un agente que no participó de la lectura, y un resumen de cada una |
| `encargos_en_linea/` | El texto con que se lanzó cada tipo de agente, tal como quedó en el registro de la sesión, con las rutas del paquete |
| `incidencias/` | Las dos tandas de lectura que se descartaron y por qué |
| `vara/` | Cuándo se escribió la vara y qué cambió después: la cronología con horas, los dos textos originales y el integrador en dos momentos (antes de lanzar las lecturas y justo antes del cambio de vara) |
| `integrar14.py` | El integrador: compara las dos lecturas con la base, arma la tercera lectura y, con ella, escribe el archivo de ajustes |
| `preparar14.py`, `tesis14.py`, `registros_a_ciegas.json`, `preparacion.json` | Cómo se armaron los lotes: los registros que vieron los lectores, sin coordenadas, y la ubicación de la tesis |
| `lectura_a.sha256`, `lectura_b.sha256`, `tercera_lectura.sha256` | La huella de las salidas de cada lectura al cerrar |

## Cómo se decide un cambio

Base: la coordenada de la versión 1.2 (los cambios que aplicó la 1.3 no se dan por buenos). Un eje (territorio, dominio o subfunción) cambia solo si se cumplen las cuatro condiciones: 1) las dos lecturas a ciegas (A y B) coinciden entre sí y difieren de la base; 2) las dos declaran confianza alta en ese eje: una regla o la definición decide y el lector no ve otro código defendible; 3) ninguna de las dos anota un vacío declarado (VC) de ese eje; 4) una tercera lectura de elección forzada, que no sabe cuál de los dos valores es el vigente, prefiere el valor nuevo. Los 37 cambios de la versión 1.2 que el autor confirmó (D-13.2) quedan protegidos: una lectura en contra se informa y no se aplica. En cualquier otro caso queda el valor de la base y el caso se lista con todas las lecturas.

Según el encargo de lectura, confianza media quiere decir que una regla decide pero otro código se puede defender. Cambiar una coordenada vigente cuando el propio lector ve otra lectura defendible no es corregirla: es preferir una lectura a otra. La condición se endureció a «las dos declaran confianza alta» después de leer, cuando los resultados mostraron cuántos cambios eran de ese tipo.

La cronología de lo que se escribió antes de leer y de lo que cambió después está en `vara/LEEME.md`. Además del cambio en la condición de la confianza, registra que la regla de los pre-ensayos que tenían RC04 se reescribió cinco minutos después de lanzar las lecturas, antes de que hubiera una salida.

## Qué se puede volver a ejecutar

Desde la carpeta del paquete, `python3 relectura_1_4/integrar14.py --final` vuelve a escribir `scripts/datos_de_trabajo/ajustes_relectura_1_4.json` a partir de las salidas guardadas, y también `scripts/datos_de_trabajo/ajustes_relectura_1_4_vara_fijada_antes_de_leer.json`, que trae los cambios de la vara que se había fijado antes de leer y no se aplicó. Los guiones que armaron los lotes se conservan como registro: volver a ejecutarlos no hace falta para regenerar el paquete.

## Rutas

Los lectores trabajaron en carpetas del entorno de trabajo. En los despachos y en los encargos, esas rutas se reemplazaron por las de este paquete. Las salidas de los lectores se copiaron byte a byte.

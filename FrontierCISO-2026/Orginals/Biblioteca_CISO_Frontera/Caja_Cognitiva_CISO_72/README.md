# Caja cognitiva del CISO — edición editable

Este paquete deriva de la edición consolidada `Consolidado_2026_MM_2026-11-11`.
Contiene [un índice navegable](00_Indice.md) y **72 fichas Markdown** distribuidas en:

| Carpeta | Contenido | Fichas iniciales |
|---|---|---:|
| `01_modelos_mentales` | Modelos mentales | 24 |
| `02_sesgos_cognitivos` | Sesgos cognitivos | 24 |
| `03_mindsets` | Mentalidades | 6 |
| `04_funciones_ejecutivas` | Funciones ejecutivas | 6 |
| `05_otras_capacidades` | Capacidades y prácticas adicionales | 12 |

`Catalogo_CISO_Editable.xlsx` es la **fuente editable** de este paquete. Las
fichas Markdown y el [segundo HTML](../../../Documents/Microsoft%20Scout/ciso-caja-cognitiva-excel.html)
son vistas derivadas. El HTML se guardó en
`C:\Users\scavanna\OneDrive - Microsoft\Documents\Microsoft Scout\ciso-caja-cognitiva-excel.html`;
el enlace relativo de arriba es orientativo y puede variar si se mueven carpetas.
La edición HTML original de 72 fichas sigue intacta.

## Estructura del Excel

- `Guia`: instrucciones y códigos admitidos.
- `Conceptos`: una fila por concepto; conserva ID, categoría, orden, contenido
  editorial, definiciones, aplicaciones, ejercicios, evaluación y controles.
  Los campos de lista se separan con **Alt+Entrar** (una entrada por línea).
- `Alias`, `Pensadores`, `Referencias` y `Fuentes`: filas relacionadas por el
  mismo ID. El nombre del documento y su localizador se registran en `Fuentes`.
  `cantidad_fuentes` cuenta todos los documentos del catálogo para una
  entrada; la hoja `Fuentes` incluye hasta tres **localizadores representativos**
  por concepto inicial, no los 37.106 registros de ocurrencias del corpus.

En total, las fichas iniciales incluyen **207 localizadores representativos**.
Cuando no consta un pensador o una referencia bibliográfica, se deja sin
atribución: no se inventan citas. El orden es una priorización editorial, no
una medida experimental de eficacia.

## Añadir un concepto y verlo en el HTML

1. Añade una fila en `Conceptos` con un ID único (por ejemplo `NEW-0001`),
   `categoria` igual a `modelos`, `sesgos`, `mindsets`, `ejecutivas` u `otras`,
   y un `nombre`. Deja `orden` vacío para colocarlo después de los existentes
   de esa categoría; si lo especificas, debe ser único dentro del grupo.
2. Completa definición, límites, justificación para el CISO, caso, pregunta,
   dominios, ejercicios, evaluaciones y controles. Los campos que falten
   aparecerán **señalados como pendientes**; no se atribuirá evidencia
   automáticamente a una entrada nueva.
3. Registra fuentes en `Fuentes` y, si existen, alias, pensadores y bibliografía
   en sus respectivas hojas. `source_supported` exige un documento con
   localizador; usa `conservative_derived` o `pending` según corresponda.
   `cantidad_fuentes` puede quedar vacía en una entrada nueva: se computará
   con las filas que añadas a `Fuentes`.
4. Guarda el `.xlsx`, abre localmente `ciso-caja-cognitiva-excel.html` en una
   versión reciente de Edge o Chrome y pulsa **Seleccionar archivo Excel**.
   La página reemplazará los datos visibles, recalculará los cinco recuentos
   y mostrará los nuevos conceptos junto a los 72 originales. No sube el
   archivo ni consulta servicios de red.

**Límite del navegador:** un HTML local no puede abrir ni vigilar sin permiso
un `.xlsx` del disco. Tras cada edición, debes volver a seleccionar el archivo;
esto no equivale a actualizarlo mediante recarga automática de la página.
Si el navegador no admite descompresión XLSX nativa, usa el script siguiente.

## Incorporar los cambios de forma permanente

Con Python y `openpyxl` instalados, desde esta carpeta ejecuta:

```powershell
python .\actualizar_desde_excel.py
```

El script vuelve a generar las fichas y **actualiza los datos incorporados en
el segundo HTML**; al abrirlo de nuevo verás los cambios aun sin seleccionar
el Excel. Si se mueve el HTML o se usa otro libro, indica rutas explícitas:

```powershell
python .\actualizar_desde_excel.py --excel "C:\ruta\Catalogo_CISO_Editable.xlsx" --html "C:\ruta\ciso-caja-cognitiva-excel.html"
```

El script no sobrescribe una ficha Markdown modificada manualmente: detiene
la regeneración y muestra la ruta afectada. El Excel es la fuente de verdad;
las fichas son copias generadas. Tampoco elimina automáticamente fichas de
conceptos borrados o renombrados en el Excel, para evitar pérdida de notas.
Revísalas de forma individual si cambias identificadores o títulos.

## Procedencia y límites de uso

Las definiciones, los límites, los autores registrados y las referencias
proceden del catálogo consolidado; la selección, la justificación, los
escenarios y las preguntas son adaptación editorial para el CISO moderno.
Los ejercicios, las evaluaciones y los controles son propuestas prácticas,
no demostraciones de eficacia. El entrenamiento no garantiza eliminar sesgos:
los controles compensatorios y la revisión independiente siguen siendo
necesarios.

Los archivos Markdown y HTML no heredan etiquetas de sensibilidad MIP de las
fuentes. Comprueba los permisos y la clasificación antes de compartirlos.

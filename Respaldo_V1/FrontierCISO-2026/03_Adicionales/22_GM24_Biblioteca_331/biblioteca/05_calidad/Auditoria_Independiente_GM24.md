# Control final independiente — biblioteca TheNextCISO GM-24

## Resultado

**Decisión:** **aprobado para consulta y desarrollo como biblioteca de
trabajo; no aprobado como currículo acreditado ni como grafo definitivo
del AI CISO Atlas.** Para el uso docente institucional se requieren las
aprobaciones y comprobaciones indicadas al final. No se ocultaron fuentes
inaccesibles ni se forzó la cifra previa de 330: las entradas verificadas
son **331**.

**Artefactos evaluados:** edición de noviembre de 2026 de
[`Biblioteca_GM24`](../Indice_Biblioteca_GM24.md), su paquete de fuentes
[`Curado02`](../../Curado02/00_control/Manifiesto_Curado02.json), las
24 guías, 331 fichas principales, 308 fichas derivadas AP, 25 Excel,
3 JSONL y el informe estructurado
[`Resultados_Auditoria.json`](Resultados_Auditoria.json).
El reporte estructurado separa clases, recuentos y reservas.

## Controles ejecutados

- [x] **Procedencia material:** 31 copias byte a byte comparadas por
  SHA-256 con los originales y con el manifiesto; un par HC idéntico
  consolidado sin borrar archivos de origen. El cribado cubrió el
  inventario de 1.705 archivos, **no una relectura completa de sus
  contenidos**.
- [x] **Estructura y recuentos:** 24 unidades; 240 ideas base en ocho
  lotes, 51 AMP [P], 40 HC candidatos; 331 entradas únicas y separadas
  de 308 tesis AP. El índice distingue HC multiunidad y 239 AP con
  unidad primaria explícita de 69 transversales/sin unidad primaria.
- [x] **Fidelidad de modalidad:** 543 textos de preguntas originales,
  incluidos cuatro imperativos; las 308 tesis AP mantienen pregunta
  fuente y estado propuesto. Las otras 235 preguntas se relacionan
  con entradas base, AMP o HC, sin que eso cree automáticamente
  nuevas tesis. Los 2.395 textos BM se identifican como construcciones
  de ocho plantillas, no como citas de entrevistados.
- [x] **Trazabilidad:** los localizadores de línea de las 240 ideas
  base y 40 HC remiten al identificador correcto; las 51 AMP
  conservan `06Ensayos!I285:I335`; las 308 tesis AP y los
  vínculos a preguntas resuelven por ID. Las relaciones candidatas
  no se tratan como causalidad ni aprobación ontológica.
- [x] **Persistencia y navegación:** 670 Markdown generados con marca
  de integridad; los enlaces locales internos comprobados resuelven; los 25
  Excel pudieron abrirse tras guardarse y contienen 331 conceptos,
  543 preguntas, 2.395 BM, 192 consignas y los módulos previstos.
- [x] **Datos estructurados:** 639 conceptos/pre-ensayos, 543
  preguntas y 2.395 BM validados contra
  [`Esquemas_GM24.json`](../00_control/Esquemas_GM24.json),
  Draft 2020-12; referencias cruzadas e IDs únicos.
- [x] **Carga propuesta:** 24 × 31 + 56 = **800 h**, de las cuales
  72 corresponden a 24 clases de tres horas; el diseño adicional
  carece de acreditación demostrada. Las 1.200 h del programa
  metacognitivo no se suman automáticamente.
- [x] **Legibilidad:** encabezados y estados están escritos en las
  fichas y en columnas Excel; ninguna distinción se comunica
  exclusivamente por color. Cada unidad tiene ocho modalidades,
  un producto y una regla crítica para revisión.

## Controles no aplicables o no ejecutables

- **Diseño visual:** no se encargó infografía ni deck nuevo; no
  corresponde evaluar codificación por flechas, color o composición.
  El JSON validado es el esquema de esta biblioteca, **no** el
  contrato visual `IGNAV-AC` de otros proyectos.
- **Excel curricular protegido sin sufijo:** WorkIQ devolvió
  `Result is protected`; no se lo descomprimió ni se supuso que
  igualaba a la variante `(2)` legible. Sus bytes se preservan,
  pero no sustentan ninguna diferencia curricular.
- **Excel histórico `20250604`:** la copia existe, pero WorkIQ no
  localizó el objeto exacto en OneDrive; no se atribuyen a él
  hojas, conceptos, horas o fecha editorial interna.
- **Video y acreditación:** existen enlaces audiovisuales
  observados en la otra biblioteca, pero no se verificó
  correspondencia, disponibilidad, duración, licencias ni
  accesibilidad por unidad GM-24. No hay constancia de
  aprobación de 51 AMP, 40 HC, rúbricas ni distribución de horas.

## Hallazgos y resolución

### QC-001 — Cerrado: cronología de 2025

**Problema detectado:** una síntesis inicial podía hacer creer que
GM-24 apareció por primera vez en noviembre de 2026. **Evidencia:**
el documento `The Next CISO - Curricula 202506 v3.docx` ya contiene
24 unidades y 240 conceptos, aunque conserva secciones de 32
unidades de un diseño anterior. **Corrección aplicada:** el
[registro de linaje](../00_control/Registro_Correcciones_Lineaje.md)
documenta la prueba, la interpretación y los archivos ajustados.
No se editaron definiciones originales.

### QC-002 — Reserva de versión: matriz protegida

**Severidad:** importante para una futura publicación autoritativa;
no bloquea esta biblioteca **de trabajo** porque el Documento
Maestro, ocho lotes, matriz `(2)` y libro de 331 concuerdan en
sus respectivos recuentos. **Impacto:** no se puede descartar
una diferencia interna no visible en el archivo protegido.
**Acción necesaria:** obtener, por los permisos habituales, una
versión accesible y comparar celdas y cambios antes de declararla
equivalente o preferente. No extraer el contenido local cifrado.

### QC-003 — Reserva de despliegue educativo

**Severidad:** importante para acreditación o enseñanza formal,
no para el uso como borrador. **Impacto:** las AMP son ideas [P],
los HC siguen siendo candidatos, las rúbricas/casos son
propuestas editoriales y no se verificaron videos por unidad.
**Acción necesaria:** revisión interdisciplinaria, selección de
bibliografía y audiovisuales por edición, pilotaje de los
192 ejercicios y aprobación explícita de carga y criterios.

## Decisión final

**Puede avanzar como cuerpo de conocimiento accionable y trazable
para revisión docente.** No presentarlo como 331 definiciones
formalmente aprobadas, como equivalencia oficial con NIST/ISACA
ni como programa de 800 horas acreditadas. La siguiente versión
debe conservar los IDs y registrar todo cambio editorial o
de definición antes de modificar el corpus.

# Biblioteca GM-24 — TheNextCISO, AI CISO Atlas y método metacognitivo

El punto de entrada de la biblioteca es
[`Indice_Biblioteca_GM24.md`](Indice_Biblioteca_GM24.md). Para trabajar
por unidad, abra `01_unidades\G1.1\Unidad_G1.1.md` y continúe hasta
`M6.2`. Cada unidad tendrá un libro Excel homónimo y enlaces a fichas
individuales con el desarrollo íntegro del borrador de idea central,
las fuentes, propuestas de ejercicio y evaluación.

**Corpus de trabajo**: 331 entradas en 24 unidades (240 conceptos base,
51 ampliaciones Atlas `[P]`, 40 híbridos HC candidatos y transversales).
La capa mayéutica conserva aparte 543 formulaciones originales, 308 tesis
editoriales AP ya redactadas en la fuente y 2.395 textos BM construidos
mediante ocho plantillas. El corpus mayéutico ampliado tiene **639**
registros (331 + 308), pero las 308 tesis **no** se cuentan como conceptos
base aprobados.

El libro `Mapa_GM24_331_y_Metodo.xlsx` es una **instantánea de publicación**
con hojas para conceptos, unidades, HC, AMP, AP, preguntas, banco BM,
192 ejercicios, plan y fuentes. Los Excel de unidad reproducen las
partes pertinentes. Las fichas Markdown y los libros se regeneran desde
`Curado02` mediante [`00_control\publicar_biblioteca.py`](00_control/publicar_biblioteca.py),
que verifica cobertura y se niega a sobrescribir una edición previa o
una ficha modificada manualmente. Para evolucionar fuentes se publica
una edición versionada; no se reescriben definiciones históricas sin
registro de cambios.

| Uso | Entrada estable |
|---|---|
| Lectura por unidad | [`Indice_Biblioteca_GM24.md`](Indice_Biblioteca_GM24.md) y `01_unidades\` |
| Conceptos del núcleo | Hoja `Conceptos_331` en [`Mapa_GM24_331_y_Metodo.xlsx`](Mapa_GM24_331_y_Metodo.xlsx); fichas en `02_conceptos\` |
| Corpus analítico 331 + 308 | [`00_control\Catalogo_GM24_639.jsonl`](00_control/Catalogo_GM24_639.jsonl) y su [esquema](00_control/Esquemas_GM24.json) |
| Preguntas y método | [`03_metodo_mayeutico\Banco_Preguntas_543.md`](03_metodo_mayeutico/Banco_Preguntas_543.md), [`Preguntas_Originales_543.jsonl`](03_metodo_mayeutico/Preguntas_Originales_543.jsonl) y [`Banco_Mayeutico_BM_2395.jsonl`](03_metodo_mayeutico/Banco_Mayeutico_BM_2395.jsonl) |

**Método de enseñanza:** comprensión conceptual → relaciones y contexto
→ aplicación → investigación → orquestación → análisis → decisión →
exposición. Cada modalidad exige evidencia, límites y responsabilidad
por la decisión. Una pregunta original no se transforma en hecho:
cuando existe una tesis AP se muestra como formulación **propuesta
y derivada**, conservando su ID de pregunta. Las otras **235**
formulaciones se vinculan a una idea base, AMP o HC existente y
requieren revisión humana si se desea redactar una tesis nueva.

**Carga horaria:** se documenta un escenario **propuesto de 800 horas**
GM-24 (24 unidades de 31 h más un capstone de 56 h), con 72 h
presenciales según el Documento Maestro. No hay constancia de
acreditación institucional para el resto. El programa de 1.200 h
de TheMetaCognitiveCISO en `Biblioteca_CISO_Frontera` es
**complementario**, no sumable automáticamente ni equivalente.

**Procedencia y límites:** consultar
[`Curado02\00_control\Manifiesto_Curado02.json`](../Curado02/00_control/Manifiesto_Curado02.json),
[`00_control\Contrato_Analisis_Fuentes.md`](00_control/Contrato_Analisis_Fuentes.md),
[`00_control\Referencias_WorkIQ.md`](00_control/Referencias_WorkIQ.md)
y [`05_calidad\Auditoria_Independiente_GM24.md`](05_calidad/Auditoria_Independiente_GM24.md).
Se preservan estados de borrador, candidato, propuesta `[P]`, relaciones
inferidas y bibliografía no verificada sin inventar autores ni lecturas.

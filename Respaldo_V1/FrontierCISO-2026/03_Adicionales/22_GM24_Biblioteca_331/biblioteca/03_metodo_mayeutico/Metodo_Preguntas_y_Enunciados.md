<!-- generado-gm24 sha256:623b9012f24d61a12b782d0669a88a1f641862701e62edb5ae7fe0fe3e85e97c -->
# Método mayéutico: preguntar, contrastar y formular hipótesis

## Cuatro conjuntos que no se deben confundir

| Capa | Registros | Significado |
|---|---:|---|
| Núcleo TheNextCISO GM-24 | 331 | 240 conceptos base, 51 ampliaciones Atlas propuestas [P], 40 HC candidatos incluidos |
| Preguntas originales consolidadas | 543 | 539 interrogativas y 4 peticiones en imperativo; conservar el texto y su procedencia |
| Tesis ampliadas desde preguntas | 308 | Identificadores `APC/APA/APN`; contienen tesis, tensión, desarrollo y producto de una fuente editorial; separadas del núcleo 331 |
| Preguntas BM generadas por plantilla | 2.395 | 639 series × 3–5 tipos; textos construidos a partir de título y plantilla, no citas de personas |

El corpus de pre-ensayos ampliado tiene **639 registros (331 + 308)**; sus tipos no elevan silenciosamente la línea base de 24 unidades. Los HC son candidatos incluidos por decisión del propietario del programa; las ampliaciones siguen siendo propuestas hasta aprobación. De las 543 formulaciones, 308 enlazan directamente con una tesis AP declarativa. Las otras 235 enlazan con 111 ideas base, 85 AMP y 39 HC: el vínculo permite debatir un enunciado ya existente, **no autoriza inventar una tesis adicional** ni presentar una pregunta como hecho.

## Procedimiento de enseñanza

1. Formular la pregunta original con su ID y ámbito sin convertir una interrogación en un hecho.
2. Identificar decisión, interesado, evidencia disponible, condición, negación y alternativa que podría refutar una respuesta.
3. Contrastar la tesis editorial AP, si existe, con la pregunta. Es una interpretación candidata, no la única respuesta correcta.
4. Producir un expediente de decisión y una prueba de resultado; clasificar observación, hipótesis, recomendación y laguna.
5. Revisar la respuesta ante un par y registrar qué evidencia la haría cambiar. Mantener el ID `PC/PA/PN` y el enlace AP o base.

## Ejemplos trazables de doble lectura

- - `PC-001`: ¿Qué resultados de negocio protege el programa de seguridad y dónde está escrito ese mandato?
  - Enunciado `[P]` relacionado: El programa de seguridad necesita un mandato aprobado por la alta dirección que nombre los resultados de negocio que protege, como continuidad de ingresos, confianza de clientes o cumplimiento de obligaciones reguladas, y que conste en un documento con dueño y vigencia. Sin ese texto, el CISO prioriza por intuición y no puede demostrar para qué existe el programa.
  - Relación: `preensayo_directo=APC-001`. El enunciado no sustituye ni prueba la pregunta.
- - `PC-004`: ¿Con qué frecuencia, formato y métricas supervisa el directorio el riesgo cibernético, y qué decisiones concretas tomó en los últimos doce meses?
  - Enunciado `[P]` relacionado: La supervisión del riesgo cibernético por el directorio se demuestra por las decisiones que produce, no por la cantidad de presentaciones recibidas. El CISO debe acordar una cadencia, un formato estable y pocas métricas ligadas al apetito de riesgo, y mantener un registro de decisiones que permita auditar qué cambió en el último año.
  - Relación: `preensayo_directo=APC-004`. El enunciado no sustituye ni prueba la pregunta.
- - `PC-006`: ¿Cómo se integra la seguridad en las decisiones de inversión, compras y portafolio, y qué ocurre cuando un proyecto no cumple los requisitos?
  - Enunciado `[P]` relacionado: La seguridad debe intervenir en cada decisión de inversión, contratación y gestión del portafolio como un requisito con consecuencias previstas, no como una opinión tardía. Cada punto de aprobación necesita criterios explícitos y una ruta definida para el incumplimiento, ya sea corregir, compensar con fecha, aceptar formalmente el riesgo o detener el proyecto, con un responsable de negocio que firme.
  - Relación: `preensayo_directo=APC-006`. El enunciado no sustituye ni prueba la pregunta.

## Ocho modalidades del banco

- `E` — **Esencial**: identifica la cuestión nuclear que el concepto intenta resolver. Plantilla: ¿Qué problema de gobierno, riesgo o capacidad intenta resolver realmente «{t}», y qué decisión debería mejorar si se comprende correctamente?
- `T` — **Tensión**: enfrenta supuestos, paradojas, trade-offs o falsas equivalencias. Plantilla: ¿Qué supuesto habitual sobre «{t}» podría ser falso o incompleto, y qué consecuencia tendría diseñar la seguridad como si fuera cierto?
- `EV` — **Evidencia**: pregunta cómo sabemos lo que afirmamos y qué límites tiene la prueba. Plantilla: ¿Qué evidencia sería suficiente para sostener una afirmación sobre «{t}», y qué evidencia aparentemente convincente no debería aceptarse como prueba?
- `D` — **Decisión**: obliga a elegir entre alternativas, explicitar autoridad y criterios de revisión. Plantilla: ¿Qué alternativa concreta elegiríamos a partir de «{t}», quién debería decidirla y qué señal obligaría a revisarla?
- `C` — **Consecuencia**: explora impacto, riesgo residual, tolerancias y costo de estar equivocado. Plantilla: ¿Qué ocurre si una decisión sobre «{t}» resulta equivocada, qué impacto es tolerable y quién tiene autoridad para aceptarlo?
- `V` — **Validación**: exige demostrar operación, cobertura, eficacia, resiliencia y condiciones de falla. Plantilla: ¿Cómo probaríamos que «{t}» funciona en condiciones reales, incluidas fallas, excepciones y dependencias, en lugar de asumir eficacia por configuración?
- `R` — **Reflexiva**: examina sesgos, incentivos, conducta, autoridad y juicio del decisor. Plantilla: ¿Qué sesgo, incentivo, límite de autoridad o comportamiento humano podría distorsionar una decisión relacionada con «{t}»?
- `I` — **Integración**: conecta conceptos que pierden significado cuando se analizan aisladamente. Plantilla: ¿Qué conceptos, capacidades o decisiones conecta «{t}» que normalmente se analizan por separado, y qué se pierde al separarlos?

## Controles de fidelidad

- Las cuatro formulaciones en imperativo no se etiquetan como preguntas interrogativas; conservan tipo de petición.
- Siete preguntas originales no poseen `preensayo_331`, aunque sí un vínculo `preensayo_directo`; no se asigna un ID faltante por proximidad.
- Siete tesis AP no especifican `especializa`; se conservan sus vínculos candidatos sin inventar unidad primaria.
- Un enlace `ESPECIALIZA`, `FUNDAMENTA` u otro predicado de la fuente no se convierte automáticamente en una arista aprobada del Atlas.
- Ninguna tesis propuesta acredita dominio adquirido ni eficacia de un control; la evaluación exige evidencia observada.

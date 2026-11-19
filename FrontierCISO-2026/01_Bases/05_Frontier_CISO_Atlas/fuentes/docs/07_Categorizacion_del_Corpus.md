> **Registro de la versión 1.3 (16 de noviembre de 2026).** Este documento se conserva tal como se publicó. Las cifras, los estados y los archivos que cita corresponden a esa versión. El estado vigente está en `docs/15_Decisiones_delegadas_y_relectura_1_4.md` y en los documentos 16 a 19.

# Categorización del corpus con el Frontier CISO Atlas

**Frontier CISO Atlas 1.3** · Taxonomía 6.0 (reglas de asignación, revisión 2) · Ontología 2.1.0 · GM-24 V7.1 · 16 de noviembre de 2026 · Estado: decisiones de diseño confirmadas por el autor; reglas adoptadas según la lectura del curador y corpus releído a ciegas por lectores automáticos, con una lectura para todos y dos donde la primera difería; contenido candidato, sin validación humana

Este documento tiene dos partes. Las secciones 1 a 6 describen la categorización vigente, después de la relectura de la versión 1.3. El anexo reproduce el documento 07 de la versión 1.2 tal como se publicó: describe cómo se clasificó el corpus, las segundas lecturas de esa versión, la decisión sobre D20 y la muestra a ciegas, con las cifras de entonces.

## 1. Resultado

Los **739 pre-ensayos** tienen una coordenada completa en la Taxonomía 6.0: territorio, dominio, función y subfunción, horizonte, fuerzas, mecanismos y pilar MCCS. Es una **categorización candidata**. La propusieron agentes clasificadores en la versión 1.0; la versión 1.2 le hizo segundas lecturas parciales y cambió 37 pre-ensayos; y la versión 1.3 la releyó completa a ciegas, con las reglas que quedaron adoptadas cuando el autor escribió «Acepto el cambio de reglas» el 16 de noviembre de 2026 (lectura del curador, a confirmar en D-15.1). No tiene revisión humana.

Cada uno de los 755 pre-ensayos (739 del corpus y 16 de la serie APX) tuvo una lectura automática a ciegas, sin la coordenada vigente a la vista. Los 483 en que hacía falta tuvieron una segunda, de otro lector: 430 en que la primera difiere de la coordenada vigente, 6 de la serie APX en que coincide y 47 de control. Un eje cambia solo si las dos lecturas coinciden entre sí, difieren del valor vigente, ninguna anotó una pregunta abierta que afecte a ese eje, ninguna declaró confianza baja y el cambio no cae en uno de los 6 puntos que la revisión de la versión candidata dejó abiertos.

Cambiaron 260 coordenadas primarias en 204 de los 739 pre-ensayos del corpus (27,6 %): 96 territorios, 87 dominios y 77 subfunciones. En la serie APX cambiaron 10 coordenadas en 8 de sus 16 pre-ensayos. No se aplicaron 312 casos en que las lecturas apuntan fuera de la coordenada vigente: 154 que caen en un punto que la revisión dejó abierto, 99 en que coinciden pero una declaró confianza baja, 22 frenados por una pregunta abierta y 37 en que las dos difieren de la vigente y entre sí. En otros 116, una lectura difiere y la otra sostiene la coordenada vigente.

El detalle de la relectura está en `14_Decisiones_y_relectura_1_3.md`, sección 4.

## 2. De dónde sale cada coordenada

| De dónde sale el valor | Territorio | Dominio | Subfunción |
|---|---|---|---|
| Conserva el valor que tenía en la Taxonomía 5.3 | 597 | 506 | 303 |
| Migró a un código nuevo de la Taxonomía 6.0 | 0 | 68 | 0 |
| No tenía valor y lo recibió del clasificador | 45 | 43 | 359 |
| Cambió en la versión 1.2 (decisión sobre D20 o revisión crítica) | 1 | 35 | 0 |
| Cambió con la relectura de la versión 1.3 | 96 | 87 | 77 |
| Total | 739 | 739 | 739 |

Un pre-ensayo que cambió en la versión 1.2 y volvió a cambiar en la 1.3 cuenta en la última fila. El origen de cada valor está en `data/categorizacion_739.csv` y en `data/corpus_frontier_739.json`.

Qué respaldo tiene hoy cada eje, según las lecturas a ciegas:

| Qué dicen las lecturas a ciegas de la versión 1.3 | Territorio | Dominio | Subfunción |
|---|---|---|---|
| Dos lecturas coinciden con el valor vigente | 218 | 280 | 220 |
| Una lectura, y coincide con el valor vigente | 272 | 272 | 272 |
| Dos lecturas coincidieron en otro valor, y el valor cambió | 96 | 87 | 77 |
| Las lecturas apuntan a otro valor y el cambio no entró | 115 | 73 | 124 |
| Una lectura difiere y la otra sostiene el valor vigente | 38 | 27 | 46 |

Estas cifras son de los 739 pre-ensayos del corpus; la serie APX va aparte. El horizonte, las fuerzas, los mecanismos y el pilar MCCS no se releyeron. Los secundarios que propusieron los lectores no se usaron: valen los que asignó el clasificador, salvo el secundario que resulta de cada cambio de primario.

## 3. Distribución

### Territorios

| Código | Territorio | Versión 1.2 | Versión 1.3 | Diferencia | Parte del corpus |
|---|---|---|---|---|---|
| T01 | SELF & JUDGMENT | 9 | 5 | -4 | 0,7 % |
| T02 | LEADERSHIP & ORGANIZATION | 70 | 90 | +20 | 12,2 % |
| T03 | STRATEGY & BUSINESS | 80 | 80 | 0 | 10,8 % |
| T04 | RISK & RESILIENCE | 136 | 139 | +3 | 18,8 % |
| T05 | SECURITY ARCHITECTURE | 104 | 88 | -16 | 11,9 % |
| T06 | SECURITY OPERATIONS | 80 | 84 | +4 | 11,4 % |
| T07 | AI & AUTONOMOUS SYSTEMS | 102 | 102 | 0 | 13,8 % |
| T08 | TRUST & ASSURANCE | 158 | 151 | -7 | 20,4 % |

### Dominios

| Código | Dominio | Versión 1.2 | Versión 1.3 | Diferencia | Parte del corpus |
|---|---|---|---|---|---|
| D01 | Cybersecurity Governance | 98 | 126 | +28 | 17,1 % |
| D02 | Cyber Risk Management | 85 | 94 | +9 | 12,7 % |
| D03 | Compliance & Regulatory Security | 39 | 42 | +3 | 5,7 % |
| D04 | Security Program & Investment Management | 63 | 52 | -11 | 7,0 % |
| D05 | Identity & Access Security | 29 | 30 | +1 | 4,1 % |
| D06 | Data Security & Information Protection | 26 | 20 | -6 | 2,7 % |
| D07 | Privacy & Data Protection Engineering | 16 | 7 | -9 | 0,9 % |
| D08 | Network & Infrastructure Security | 2 | 3 | +1 | 0,4 % |
| D09 | Endpoint & Workplace Security | 11 | 8 | -3 | 1,1 % |
| D10 | Cloud & Platform Security | 7 | 4 | -3 | 0,5 % |
| D11 | Application & Software Security | 8 | 7 | -1 | 0,9 % |
| D12 | Threat Intelligence & Threat Modeling | 23 | 24 | +1 | 3,2 % |
| D13 | Vulnerability & Exposure Management | 16 | 16 | 0 | 2,2 % |
| D14 | Security Monitoring & Detection | 23 | 23 | 0 | 3,1 % |
| D15 | Incident Response & Crisis Management | 38 | 42 | +4 | 5,7 % |
| D16 | Business Continuity & Cyber Recovery | 24 | 23 | -1 | 3,1 % |
| D17 | Third-Party & Supply Chain Security | 33 | 28 | -5 | 3,8 % |
| D18 | Operational Technology & Industrial Control Security | 4 | 4 | 0 | 0,5 % |
| D19 | IoT & Cyber-Physical Systems Security | 0 | 0 | 0 | 0,0 % |
| D20 | AI & Agent Security | 45 | 43 | -2 | 5,8 % |
| D21 | AI for Cyber Defense & Security Operations | 16 | 11 | -5 | 1,5 % |
| D22 | AI for Security Assessment & Testing | 3 | 3 | 0 | 0,4 % |
| D23 | AI for Security Engineering & Automation | 6 | 5 | -1 | 0,7 % |
| D24 | Security Workforce & Human Factors | 47 | 43 | -4 | 5,8 % |
| D25 | Enterprise Security Architecture & Zero Trust | 14 | 18 | +4 | 2,4 % |
| D26 | Cryptography, Key Management & Post-Quantum Readiness | 5 | 5 | 0 | 0,7 % |
| D27 | Physical, Environmental & Facility Security | 1 | 1 | 0 | 0,1 % |
| D28 | Security Assurance, Testing & Measurement | 57 | 57 | 0 | 7,7 % |

### Funciones

| Código | Función | Versión 1.2 | Versión 1.3 | Diferencia | Parte del corpus |
|---|---|---|---|---|---|
| GV | Gobernar | 369 | 366 | -3 | 49,5 % |
| ID | Identificar | 100 | 115 | +15 | 15,6 % |
| PR | Proteger | 162 | 151 | -11 | 20,4 % |
| DE | Detectar | 34 | 31 | -3 | 4,2 % |
| RS | Responder | 45 | 48 | +3 | 6,5 % |
| RC | Recuperar | 29 | 28 | -1 | 3,8 % |

### Subfunciones

| Código | Subfunción | Versión 1.2 | Versión 1.3 | Diferencia | Parte del corpus |
|---|---|---|---|---|---|
| GV01 | Contexto empresarial y estrategia | 23 | 18 | -5 | 2,4 % |
| GV02 | Estructura de gobierno y autoridad | 27 | 43 | +16 | 5,8 % |
| GV03 | Políticas y estándares | 56 | 58 | +2 | 7,8 % |
| GV04 | Apetito, tolerancia y aceptación de riesgo | 47 | 47 | 0 | 6,4 % |
| GV05 | Gobierno de programas, recursos e inversión | 38 | 39 | +1 | 5,3 % |
| GV06 | Obligaciones legales y contractuales | 37 | 32 | -5 | 4,3 % |
| GV07 | Supervisión y reporting ejecutivo | 40 | 34 | -6 | 4,6 % |
| GV08 | Assurance y revisión independiente | 47 | 46 | -1 | 6,2 % |
| GV09 | Gobierno de terceros y ecosistemas | 30 | 27 | -3 | 3,7 % |
| GV10 | Ética, cultura y rendición de cuentas | 24 | 22 | -2 | 3,0 % |
| ID01 | Inventario y clasificación de activos | 16 | 17 | +1 | 2,3 % |
| ID02 | Dependencias y criticidad del negocio | 8 | 6 | -2 | 0,8 % |
| ID03 | Amenazas, vulnerabilidades y exposición | 35 | 33 | -2 | 4,5 % |
| ID04 | Análisis de escenarios y cuantificación de riesgos | 22 | 33 | +11 | 4,5 % |
| ID05 | Evaluación de capacidades y brechas | 19 | 26 | +7 | 3,5 % |
| PR01 | Identidad y autorización | 35 | 36 | +1 | 4,9 % |
| PR02 | Protección de datos y privacidad por diseño | 31 | 28 | -3 | 3,8 % |
| PR03 | Hardening y arquitectura segura | 51 | 45 | -6 | 6,1 % |
| PR04 | Desarrollo seguro y gestión de cambios | 20 | 18 | -2 | 2,4 % |
| PR05 | Preparación de personas y procedimientos | 22 | 21 | -1 | 2,8 % |
| PR06 | Resiliencia de la infraestructura y protección física y ambiental | 3 | 3 | 0 | 0,4 % |
| DE01 | Telemetría y observabilidad | 6 | 5 | -1 | 0,7 % |
| DE02 | Ingeniería de detección y análisis | 16 | 16 | 0 | 2,2 % |
| DE03 | Hunting, validación y mejora de detecciones | 4 | 4 | 0 | 0,5 % |
| DE04 | Evaluación de cobertura y calidad de detección | 8 | 6 | -2 | 0,8 % |
| RS01 | Preparación y coordinación de respuesta | 20 | 22 | +2 | 3,0 % |
| RS02 | Contención, erradicación y preservación de evidencia | 12 | 13 | +1 | 1,8 % |
| RS03 | Comunicación de crisis y decisiones ejecutivas | 10 | 11 | +1 | 1,5 % |
| RS04 | Gestión de incidentes con terceros | 3 | 2 | -1 | 0,3 % |
| RC01 | Restauración y recuperación técnica | 7 | 7 | 0 | 0,9 % |
| RC02 | Continuidad y operación degradada | 7 | 6 | -1 | 0,8 % |
| RC03 | Validación de recuperación y retorno seguro | 5 | 5 | 0 | 0,7 % |
| RC04 | Aprendizaje, corrección y mejora continua | 10 | 10 | 0 | 1,4 % |
| RC05 | Comunicación de la recuperación y restitución de la confianza | 0 | 0 | 0 | 0,0 % |

Las celdas territorio × dominio vacías pasan de 132 a 136, de 224. La cifra no distingue las combinaciones que no pueden darse de las que no tienen contenido. Dominios sin pre-ensayos: D19. Subfunciones sin pre-ensayos: RC05. La matriz completa está en `data/matriz_territorio_dominio.csv`.

## 4. Lo que la relectura deja sin resolver

- **312 casos en que las lecturas apuntan fuera de la coordenada vigente y el cambio no entró**, contando la serie APX: `data/relectura_1_3_casos_para_el_autor.csv`.
- **6 puntos que la revisión de la versión candidata dejó abiertos.** Frenan 154 de esos casos: `14_Decisiones_y_relectura_1_3.md`, sección 3.3.
- **11 preguntas abiertas de las reglas.** Los lectores anotaron que 64 pre-ensayos dependen de alguna de las seis que podían marcar: `data/preguntas_abiertas_1_3.csv`.
- **Fronteras de subfunciones que ninguna regla adoptada decide.** 10 de las 34 definiciones de trabajo declaran una. Los lectores no tenían un código para anotarlas.
- **En 543 de las 755 primeras lecturas el lector anotó otra opción defendible.**

## 5. Límites

- La categorización no tiene revisión humana. La propuesta para hacerla está en el documento 14, sección 7.3.
- Los lectores son automáticos y comparten configuración con quien generó los artefactos: dos lecturas que coinciden no prueban que el valor sea correcto.
- La relectura cambió coordenadas que venían del banco del autor. Si esos cambios son mejores que lo que había lo mide la revisión humana.
- En buena parte del corpus el texto es plantilla repetida, y la lectura se apoya en el título y en la primera oración.
- 77 pre-ensayos del plano A nombran productos de un proveedor o al proveedor.

## 6. Archivos

- `data/corpus_frontier_739.json` y `data/categorizacion_739.csv`: la coordenada vigente de cada pre-ensayo, con su origen y sus cambios en las versiones 1.2 y 1.3.
- `data/estadisticas_corpus.json` y `data/matriz_territorio_dominio.csv`: las distribuciones.
- `data/relectura_1_3_por_eje.csv`, `data/relectura_1_3_resumen.json` y `data/relectura_1_3_casos_para_el_autor.csv`: la relectura.
- `data/cambios_1_2_a_1_3.csv` y `data/cambios_1_1_a_1_2.csv`: lo que cambió en cada versión.
- `data/evidencia_por_preensayo.csv`: las lecturas que tenía cada pre-ensayo hasta la versión 1.2.
- `relectura_1_3/`: lo que recibieron y lo que devolvieron los lectores.

## Anexo · El documento 07 de la versión 1.2, como se publicó

> Lo que sigue es el texto de la versión 1.2, sin cambios, con sus cifras. Donde dice «vigente», «hoy» o «queda a confirmar» habla del 16 de noviembre de 2026, antes de las decisiones del autor y de la relectura. La muestra para la revisión humana que describe fue reemplazada (documento 14, sección 7.3).

### 1. Resultado

Los **739 pre-ensayos** tienen una coordenada completa en la Taxonomía 6.0: territorio, dominio, función y subfunción, horizonte, fuerzas, mecanismos y pilar MCCS. Es una **categorización candidata**: la propusieron agentes clasificadores con reglas escritas y un validador determinista. Tu aceptación en bloque la alcanza como base de trabajo (decisión D-07), lo que no la valida: no tiene revisión humana. Desde la versión 1.2 tiene una segunda lectura automática sobre una parte, que se describe en las secciones 6 a 9.

- De dónde sale el dominio de cada pre-ensayo: 586 conservan el de la versión 5.3, 69 migran a un dominio nuevo, 48 no tenían coordenada y la reciben ahora, y 36 lo cambian por la decisión D-03 o por la vía de corrección. Las migraciones a dominios nuevos son 71 si se cuentan además las que la versión 1.2 produjo o conservó entre esos 36 cambios.
- Confianza declarada por el clasificador: alta en 503 (68 %), media en 229 y baja en 7. Es una declaración, no una medida.
- No queda ninguna sugerencia del clasificador sin tratar: las 18 de la versión 1.1 se aplicaron o se resolvieron con la segunda lectura.

### 2. El corpus

El corpus une dos fuentes: el GM-24 V7.1 (379 conceptos, todos con pre-ensayo) y el banco del Atlas (691 pre-ensayos). Comparten 331.

| Origen | Pre-ensayos |
|---|---|
| banco Atlas | 360 |
| GM-24 V7.1 + banco Atlas | 331 |
| GM-24 V7.1 | 48 |

| Clase | Qué es | Pre-ensayos | Parte del texto que es plantilla (mediana) | Palabras propias (mediana) |
|---|---|---|---|---|
| K | Concepto base del GM-24 | 245 | 71 % | 124 |
| APC | Ampliación por pregunta que hace el CISO | 156 | 0 % | 179 |
| APA | Ampliación por pregunta que le hacen al CISO | 111 | 0 % | 179 |
| AMP | Ampliación del GM-24 | 52 | 0 % | 185 |
| PA | Sub-plan PO-GAC del GM-24 (nuevo en V7.1) | 42 | 0 % | 284 |
| APN | Ampliación por pregunta de productividad individual | 41 | 0 % | 185 |
| HC | Híbrido del GM-24 | 40 | 70 % | 49 |
| APS | Ampliación por pregunta propuesta para temas vacíos de la agenda de IA | 28 | 0 % | 151 |
| APF | Ampliación por pregunta nueva de la agenda de IA 4.0 | 24 | 0 % | 160 |

**Cuánto contenido propio tiene cada clase.** Los pre-ensayos son ideas centrales, no ensayos, y no todos están igual de desarrollados. La tabla de arriba mide qué parte del texto de cada clase son oraciones que se repiten en cinco o más pre-ensayos. En las clases K y HC más de la mitad del texto es plantilla del módulo: son 285 pre-ensayos (39 % del corpus), cada uno con una oración o un párrafo propios. La cifra de 739 sobrestima el contenido desarrollado, y la clasificación de esos pre-ensayos descansa en el título y en muy poco texto.

**Productos de proveedor en el plano A.** 77 pre-ensayos nombran productos de un proveedor o al proveedor (39 de la clase PA, 33 de la clase AMP y 5 de la clase K); 5 nombran solo al proveedor y 3 lo hacen en el título. El plano A se propone agnóstico de proveedor: esos pre-ensayos quedaron marcados «revisar» en el grafo. Los más nombrados: Sentinel (26), Agent 365 (20), Foundry (19), Copilot Studio (17), Power Platform (14) y Purview (13).

### 3. Método

1. **Unificación.** Un registro por pre-ensayo con título, tesis, texto, unidad del GM-24, coordenada vigente en 5.3, vínculos editoriales y mapeo a marcos.
2. **Instrucciones escritas.** Un mismo documento para todos los clasificadores, con los catálogos de la 6.0, las reglas de frontera de los dominios nuevos y el formato de salida (`scripts/clasificacion/INSTRUCCIONES_DE_CLASIFICACION.md`). Varias reglas operativas de esas instrucciones no están en el catálogo de la taxonomía; la regla propuesta RP-10 pide llevarlas allí.
3. **Ocho lotes** de 88 a 93 pre-ensayos, cada uno con un agente clasificador que leyó título, tesis y texto.
4. **Validación determinista** de cada lote: códigos válidos, cardinalidades, función coherente con la subfunción y motivo obligatorio para todo cambio. Los ocho lotes validan.
5. **Política de migración.** La coordenada vigente en 5.3 se conserva salvo que el cambio lo cause (a) un dominio o una subfunción nuevos del catálogo 6.0, (b) un ajuste de alcance de la Taxonomía 6.0, como la regla 7, cuya aplicación a D20 se leyó como aceptada (decisión D-03, a confirmar), o (c) la vía de corrección: dos lecturas que coinciden, o una adjudicación escrita que se apoya en la tesis y en una regla explícita (ADR-028, que rige de forma provisoria). La sección 8 dice cuántos cambios cumplen esa regla en su forma estricta y cuántos no.
6. **Segundas lecturas (versión 1.2).** Fueron cuatro, y solo una fue a ciegas. En los 71 pre-ensayos de D20, el revisor sabía que estaban en ese dominio y conocía su territorio y su subfunción; no conocía la primera lectura. En las 73 migraciones a dominios nuevos, conocía el dominio 5.3, sabía que todos los casos habían migrado y elegía entre ese dominio y los nuevos. Una muestra de 87 pre-ensayos se clasificó a ciegas, desde cero. Y en 7 pre-ensayos un segundo lector respondió si aceptaba una sugerencia del clasificador que tenía a la vista. Todos recibieron el texto recortado a 1.100 caracteres y la tesis a 600. En total, 237 pre-ensayos tienen alguna lectura además de la del clasificador y 502 tienen una sola: `data/evidencia_por_preensayo.csv` lo dice para cada uno.

Cada clasificación guarda su método, su confianza, su justificación y la versión de taxonomía, y cada cambio de la versión 1.2 guarda además su origen y su motivo. La confianza es la que el clasificador declaró para su propia propuesta: en los 37 pre-ensayos que cambiaron de coordenada no vale para el valor cambiado, y el catálogo lo dice en la columna `nota_sobre_la_confianza`. En esos pre-ensayos la justificación empieza por el respaldo del cambio y conserva después el texto del clasificador, que se escribió para la coordenada anterior.

**Qué asignó quién.** Territorio y dominio venían informados en 691 pre-ensayos y la subfunción en 360; ahí la regla fue conservar. Horizonte, fuerzas, mecanismos, pilar MCCS y coordenadas secundarias son asignaciones nuevas para los 739. La subfunción es nueva para los 379 del GM-24. El pilar MCCS y el eje H no tienen segunda lectura.

### 4. Distribución

#### Territorios

| Código | Nombre | Pre-ensayos | Proporción |
|---|---|---|---|
| T01 | SELF & JUDGMENT | 9 | 1,2 % |
| T02 | LEADERSHIP & ORGANIZATION | 70 | 9,5 % |
| T03 | STRATEGY & BUSINESS | 80 | 10,8 % |
| T04 | RISK & RESILIENCE | 136 | 18,4 % |
| T05 | SECURITY ARCHITECTURE | 104 | 14,1 % |
| T06 | SECURITY OPERATIONS | 80 | 10,8 % |
| T07 | AI & AUTONOMOUS SYSTEMS | 102 | 13,8 % |
| T08 | TRUST & ASSURANCE | 158 | 21,4 % |

#### Dominios

La columna «Corpus 6.0» cuenta códigos de la 6.0 con el alojamiento heredado: solo D20 y los dominios nuevos tuvieron una lectura dedicada. Los ajustes de alcance de D09, D13, D17 y D24 no se aplicaron al corpus (regla propuesta RP-18).

| Código | Dominio | Corpus 5.3 | Corpus 6.0 (códigos 6.0, alojamiento heredado) | Proporción |
|---|---|---|---|---|
| D01 | Cybersecurity Governance | 74 | 98 | 13,3 % |
| D02 | Cyber Risk Management | 80 | 85 | 11,5 % |
| D03 | Compliance & Regulatory Security | 55 | 39 | 5,3 % |
| D04 | Security Program & Investment Management | 63 | 63 | 8,5 % |
| D05 | Identity & Access Security | 36 | 29 | 3,9 % |
| D06 | Data Security & Information Protection | 35 | 26 | 3,5 % |
| D07 | Privacy & Data Protection Engineering | 16 | 16 | 2,2 % |
| D08 | Network & Infrastructure Security | 2 | 2 | 0,3 % |
| D09 | Endpoint & Workplace Security | 10 | 11 | 1,5 % |
| D10 | Cloud & Platform Security | 11 | 7 | 0,9 % |
| D11 | Application & Software Security | 9 | 8 | 1,1 % |
| D12 | Threat Intelligence & Threat Modeling | 22 | 23 | 3,1 % |
| D13 | Vulnerability & Exposure Management | 18 | 16 | 2,2 % |
| D14 | Security Monitoring & Detection | 21 | 23 | 3,1 % |
| D15 | Incident Response & Crisis Management | 36 | 38 | 5,1 % |
| D16 | Business Continuity & Cyber Recovery | 24 | 24 | 3,2 % |
| D17 | Third-Party & Supply Chain Security | 29 | 33 | 4,5 % |
| D18 | Operational Technology & Industrial Control Security | 4 | 4 | 0,5 % |
| D19 | IoT & Cyber-Physical Systems Security | 0 | 0 | 0,0 % |
| D20 | AI & Agent Security | 76 | 45 | 6,1 % |
| D21 | AI for Cyber Defense & Security Operations | 15 | 16 | 2,2 % |
| D22 | AI for Security Assessment & Testing | 4 | 3 | 0,4 % |
| D23 | AI for Security Engineering & Automation | 7 | 6 | 0,8 % |
| D24 | Security Workforce & Human Factors | 44 | 47 | 6,4 % |
| D25 | Enterprise Security Architecture & Zero Trust | — | 14 | 1,9 % |
| D26 | Cryptography, Key Management & Post-Quantum Readiness | — | 5 | 0,7 % |
| D27 | Physical, Environmental & Facility Security | — | 1 | 0,1 % |
| D28 | Security Assurance, Testing & Measurement | — | 57 | 7,7 % |

#### Funciones

| Código | Nombre | Pre-ensayos | Proporción |
|---|---|---|---|
| GV | Govern | 369 | 49,9 % |
| ID | Identify | 100 | 13,5 % |
| PR | Protect | 162 | 21,9 % |
| DE | Detect | 34 | 4,6 % |
| RS | Respond | 45 | 6,1 % |
| RC | Recover | 29 | 3,9 % |

Subfunciones sin pre-ensayos: RC05. La distribución completa está en `03_Taxonomia_6_0.md`.

#### Horizontes

| Código | Nombre | Pre-ensayos | Proporción |
|---|---|---|---|
| H01 | Foundational | 341 | 46,1 % |
| H02 | Evolving | 240 | 32,5 % |
| H03 | Emerging | 123 | 16,6 % |
| H04 | Convergent | 22 | 3,0 % |
| indeterminado |  | 13 | 1,8 % |

#### Pilares MCCS

| Código | Nombre | Pre-ensayos | Proporción |
|---|---|---|---|
| MM | Modelos mentales | 48 | 6,5 % |
| OS | Sistema operativo | 144 | 19,5 % |
| DO | Entrega y operación | 487 | 65,9 % |
| NX | Evolución | 60 | 8,1 % |

#### Pilares MCCS por territorio

| Territorio | MM | OS | DO | NX | Total |
|---|---|---|---|---|---|
| T01 SELF & JUDGMENT | 7 | 2 | 0 | 0 | 9 |
| T02 LEADERSHIP & ORGANIZATION | 6 | 30 | 22 | 12 | 70 |
| T03 STRATEGY & BUSINESS | 4 | 13 | 47 | 16 | 80 |
| T04 RISK & RESILIENCE | 23 | 30 | 78 | 5 | 136 |
| T05 SECURITY ARCHITECTURE | 1 | 4 | 97 | 2 | 104 |
| T06 SECURITY OPERATIONS | 1 | 6 | 66 | 7 | 80 |
| T07 AI & AUTONOMOUS SYSTEMS | 1 | 25 | 67 | 9 | 102 |
| T08 TRUST & ASSURANCE | 5 | 34 | 110 | 9 | 158 |

#### Fuerzas y mecanismos

585 pre-ensayos (79 %) tratan al menos una fuerza o un mecanismo homeostático. Los más frecuentes: HOM09 Assurance y validación (164), HOM08 Gobierno y supervisión (134), HOM12 Gobierno de la autonomía (niveles, aprobación humana e interruptor probado) (69), CAT01 Innovación tecnológica (65), INH09 Limitaciones operativas (55), HOM01 Apetito y tolerancia al riesgo (54). Las fuerzas y los mecanismos nuevos del eje H aparecen así: CAT11 en 2, INH11 en 8, HOM11 en 18 y HOM12 en 69. HX08, el quinto elemento nuevo, es un factor de contexto y no se asigna a pre-ensayos.

### 5. Lecturas

- **Por función, la mitad del corpus es gobierno.** La función GV reúne 50 %; DE, RS y RC juntas, 15 %. La operación es lo menos desarrollado.
- **Por pilar, predomina DO.** Cerca de 66 % de los pre-ensayos lleva el pilar DO; MM, cerca de 6 %; NX, cerca de 8 %. El territorio T01 tiene 9 pre-ensayos. Si el CISO de frontera se define por cómo piensa y cómo se adapta, esos son los vacíos a cubrir primero; es una lectura condicionada a esa definición y a una asignación de pilar que no tiene segunda lectura.
- **La Biblioteca cognitiva no llena ese vacío por sí sola.** Sus conceptos son definiciones, no pre-ensayos, y no están vinculados con el corpus. Falta decidir cuáles se desarrollan.
- **Casi la mitad es práctica consolidada.** H01 reúne 46 % y H04 (convergente), 3 %. La frontera propiamente dicha (H03) es 17 %.
- **Hay 132 celdas territorio × dominio vacías sobre 224.** La cifra no distingue las combinaciones que no aplican de las que no tienen contenido: territorio y dominio están muy asociados, y muchas celdas son vacíos legítimos. Separarlas pide tu juicio. La lista está en `data/matriz_territorio_dominio.csv`.
- **Dominios sin contenido o con muy poco:** D08 (2), D18 (4), D19 (0), D22 (3), D27 (1). Para D19, D27 y la subfunción RC05 hay una capa de ampliación (sección 12).

### 6. Migraciones a dominios nuevos

| Dominio nuevo | Migran | Desde | Total en el dominio |
|---|---|---|---|
| D25 Enterprise Security Architecture & Zero Trust | 13 | D05 (5), D10 (4), D20 (2), D04 (1), D16 (1) | 14 |
| D26 Cryptography, Key Management & Post-Quantum Readiness | 5 | D06 (5) | 5 |
| D27 Physical, Environmental & Facility Security | 0 | — | 1 |
| D28 Security Assurance, Testing & Measurement | 53 | D03 (17), D20 (9), D13 (5), D01 (4), D04 (4), D02 (3), D05 (3), D14 (3), D06 (1), D15 (1), D17 (1), D22 (1), D23 (1) | 57 |

Las 71 migraciones, con el motivo de cada una, están en `data/categorizacion_739.csv`. Además, 6 conceptos nuevos del GM-24 V7.1 entraron directamente en dominios nuevos.

**Segunda lectura.** Un revisor volvió a decidir el dominio de las 73 migraciones de la versión 1.1, sin conocer el dominio al que se había migrado cada una, y coincidió en 69 (94,5 %). En las 4 restantes se adjudicó por escrito, con la tesis y la regla 6: HC-038 pasa de D25 a D28; APC-088 pasa de D28 a D02; APA-175 pasa de D28 a D02; APF-12 pasa de D28 a D05. El detalle está en `data/segunda_lectura_migraciones.csv`. La evidencia de corpus que sostiene a los dominios nuevos sigue siendo circular: cuenta pre-ensayos que movieron clasificadores que ya conocían la definición del dominio.

### 7. La decisión D-03, aplicada a D20

La regla 7 dice que el gobierno, el riesgo y el cumplimiento de la IA van a D01, D02 o D03 con territorio T07, y que D20 queda para proteger modelos, agentes, herramientas, datos y entorno de ejecución. La versión 1.1 preguntaba si aplicarla; tu aceptación en bloque se leyó como «sí», y esa lectura queda a confirmar (decisión D-14.2).

Un pre-ensayo salió de D20 en tres situaciones: cuando la primera lectura (versión 1.1) y una segunda lectura, que no conocía la primera, deciden el mismo destino; cuando la primera lo dejaba «a criterio del curador» y la segunda propone el destino; y cuando una adjudicación escrita se apoya en la tesis y en la regla. Solo la primera situación cumple en sentido estricto la regla de las dos lecturas. Donde las lecturas no coinciden, el pre-ensayo queda en D20 y se lista.

| Resolución | Pre-ensayos |
|---|---|
| Queda en D20: las dos lecturas coinciden | 34 |
| Queda en D20: la segunda lectura propone D28; sin coincidencia, a decisión del autor | 9 |
| Se movió a D01: las dos lecturas deciden lo mismo | 8 |
| Se movió a D01: la primera lectura lo dejaba a criterio del curador y la segunda propone ese destino | 6 |
| Se movió a D02: las dos lecturas deciden lo mismo | 4 |
| Se movió a D02: la primera lectura lo dejaba a criterio del curador y la segunda propone ese destino | 2 |
| Se movió a D17: coinciden la sugerencia del clasificador, la primera lectura y la segunda (fuera de D-03) | 1 |
| Queda en D20: la segunda lectura no acompaña el movimiento de la primera; a decisión del autor | 1 |
| Se movió a D28: la primera lectura lo dejaba a criterio del curador y la segunda propone ese destino | 1 |
| Se movió a D01: adjudicado en el triaje | 1 |
| Se movió a D17: adjudicado en el triaje | 1 |
| Se movió a D14: adjudicado en el triaje | 1 |
| Queda en D20: la segunda lectura propone D03; sin coincidencia, a decisión del autor | 1 |
| Se movió a D01: adjudicado en el triaje (destino discutido: la segunda lectura propone D28) | 1 |

- **Resultado.** De los 71 pre-ensayos, 26 salieron de D20 (16 a D01, 6 a D02, 2 a D17, 1 a D28 y 1 a D14) y 45 quedan. De los que salieron, en 13 las dos lecturas deciden el mismo destino, en 9 la primera lectura lo dejaba a criterio del curador y la segunda propone el destino, y 4 se adjudicaron por escrito; en tres de estos últimos la primera lectura decía «queda en D20». 22 fueron a los dominios que nombra la regla 7; los otros 4 (AMP-49 a D17, HC-012 a D28, APC-122 a D17 y APC-164 a D14), a otro dominio, porque la lectura vio otro objeto (terceros, aseguramiento o detección).
- **Sin coincidencia (11).** Quedan en D20 y esperan tu decisión: AMP-46, HC-010, APC-210, APC-212, APA-053, APA-068, APA-075, APA-108, APA-111, APA-113 y APA-158. En nueve, la segunda lectura propone D28: 8 de ellos llevan el territorio T08 y tratan de evidencia, pruebas o auditoría de sistemas de IA, y la regla 6 no dice si el aseguramiento de la IA es D28 o D20 (regla propuesta RP-02). HC-010 es uno de los 14 que la versión 1.1 daba por claros: la segunda lectura lo deja en D20. `data/casos_sin_coincidencia_D13.csv` trae una ficha de cada caso, con la tesis y las dos lecturas.
- **El territorio no se cambió.** La regla dice «con territorio T07», pero no aclara si es condición o consecuencia. 22 de los 26 que salieron ya tenían T07; los otros 4 conservan su territorio (regla propuesta RP-04).

**Qué se decidió en el fondo.** De los 71 pre-ensayos de D20, 53 llevaban la marca de IA dos veces: en el territorio (T07) y en el dominio (D20). La disciplina, gobierno o riesgo, solo aparecía en la subfunción. Con la regla, la marca de IA queda en el territorio y el dominio pasa a decir la disciplina. D20 deja de ser «todo lo de IA» y pasa a ser «la protección técnica de la IA».

La lista completa, con las dos lecturas y la resolución de cada caso, está en `data/analisis_D20_decision_D03.csv`.

### 8. Correcciones por la vía de corrección

Fuera de D20, la versión 1.2 aplicó 11 cambios de coordenada.

**7 sugerencias confirmadas.** Los clasificadores habían sugerido cambios que la política anterior no dejaba aplicar: 4 que el propio clasificador había llamado errores evidentes de la coordenada heredada y 3 que había llamado ajustes de alcance de la 6.0. Un segundo lector, que tenía a la vista la coordenada vigente, la sugerencia y su motivo, las aceptó. Es la confirmación de una propuesta conocida, no una segunda lectura independiente.

| Id | Pre-ensayo | Qué cambió | De | A | Motivo |
|---|---|---|---|---|---|
| G2.2-K06 | Aplicación (Enforcement) | dominio | D06 | D01 | Sugerencia del clasificador que la política de migración no aplicaba (error evidente en el dominio: el texto trata la aplicación de políticas (mecanismos técnicos, responsabilidades, supervisión y respuesta ante incumplimientos) y no la protección de datos, por lo que pasa de D06 a D01); un segundo lector, que tenía a la vista la coordenada vigente y la sugerencia, la acepta: La tesis define la aplicación de políticas como la combinación de mecanismos técnicos, responsabilidades, supervisión y respuesta ante incumplimientos, y pide situarla «en el ámbito del gobierno de la ciberseguridad»; nada en ella trata la protección de datos, de modo que D06 es un error de dominio y D01 es el que corresponde a su objeto. |
| G6.1-K07 | Gestión Expectativas | dominio | D14 | D04 | Sugerencia del clasificador que la política de migración no aplicaba (error evidente en D14: el objeto es el acuerdo de alcance, plazos y beneficios con el patrocinador (gestión del programa); el SIEM solo aparece como ejemplo del caso y D14 queda como secundario); un segundo lector, que tenía a la vista la coordenada vigente y la sugerencia, la acepta: La tesis trata de acordar alcance, restricciones, responsabilidades y resultados realistas antes de comprometer plazos o beneficios de seguridad, que es gestión del programa ante su patrocinador; el SIEM aparece solo como caso ilustrativo, por lo que D14 se asignó por una palabra suelta y D04 es coherente con el territorio T03 y la subfunción GV05 vigentes. |
| M2.1-K01 | Identificación Activos | dominio | D06 | D13 | Sugerencia del clasificador que la política de migración no aplicaba (ajuste de alcance 6.0: el inventario de activos generales va en D13; los datos son solo una clase de activo y D06 queda como secundario); un segundo lector, que tenía a la vista la coordenada vigente y la sugerencia, la acepta: La tesis define la identificación de activos como el reconocimiento de recursos, servicios, identidades, datos y dependencias, de los que los datos son solo una clase; D06 no describe ese objeto y la Taxonomía 6.0 ubica el inventario de activos en D13, aunque lo hace «como insumo de la exposición», un encuadre más estrecho que el de la tesis, que habla de lo que sostiene los resultados empresariales. |
| M2.1-K03 | Inventario | dominio | D06 | D13 | Sugerencia del clasificador que la política de migración no aplicaba (ajuste de alcance 6.0: el inventario de activos (recursos y relaciones, no datos) va en D13); un segundo lector, que tenía a la vista la coordenada vigente y la sugerencia, la acepta: La tesis define el inventario de activos como un registro vivo de recursos y relaciones que se mantiene con descubrimiento, asignación de dueños y validación periódica, y el caso es una CMDB que no refleja recursos de nube; no trata la protección de la información, y el inventario y el descubrimiento están en D13 según el ajuste 6.0. |
| M2.1-K04 | Ciclo de Vida Datos | territorio | T07 | T05 | Sugerencia del clasificador que la política de migración no aplicaba (error evidente en T07: la IA solo aparece como un uso mencionado en el problema; el objeto es el ciclo de vida de los datos y se alinea con T05 como el resto de la unidad); un segundo lector, que tenía a la vista la coordenada vigente y la sugerencia, la acepta: La tesis define el ciclo de vida de los datos, de la creación a la eliminación, bajo criterios de seguridad y privacidad, y la IA aparece una sola vez como uno de los usos en los que se pierde el control; T07 no se asigna por mera mención de IA, y T05 corresponde a un objeto que es el diseño de controles sobre los datos, razón que basta sin apoyarse en la alineación con el resto de la unidad que invoca el clasificador. |
| M4.2-K01 | Gestión Vulnerabilidades | dominio | D12 | D13 | Sugerencia del clasificador que la política de migración no aplicaba (error evidente en v53: el objeto es la gestión de vulnerabilidades y exposición (D13), no la inteligencia de amenazas (D12), que queda como secundario); un segundo lector, que tenía a la vista la coordenada vigente y la sugerencia, la acepta: La tesis define la gestión de vulnerabilidades como priorizar descubrimiento, evaluación, remediación y verificación según explotabilidad, exposición y consecuencias, lo que coincide casi literalmente con la definición de D13; no trata adversarios ni modelado de amenazas, por lo que D12 es un error de dominio. |
| M6.2-K10 | SBOM | dominio | D11 | D17 | Sugerencia del clasificador que la política de migración no aplicaba (ajuste de alcance 6.0: la cadena de suministro de software (componentes y dependencias) va en D17; D11 queda como secundario); un segundo lector, que tenía a la vista la coordenada vigente y la sugerencia, la acepta: La tesis presenta la lista de materiales de software como un medio de visibilidad de componentes y dependencias que requiere calidad, actualización y respuesta a vulnerabilidades; la Taxonomía 6.0 ubica de forma explícita la cadena de suministro de software y sus componentes en D17, y la práctica de desarrollo (D11) queda como dominio secundario. |

**4 migraciones adjudicadas.** Son las de la sección 6 en que la segunda lectura no acompañó la migración: se adjudicaron por escrito.

Con los 26 de D20, los cambios del corpus son 37. Este es el respaldo de cada uno:

| Respaldo | Cambios |
|---|---|
| Dos lecturas deciden lo mismo | 13 |
| La primera lectura no decidió y la segunda propone el destino | 9 |
| Sugerencia confirmada por un lector que la conocía | 7 |
| Adjudicación escrita | 8 |
| **Total** | 37 |

Solo la primera fila cumple en sentido estricto la regla «dos lecturas que coinciden». Todos están en `data/cambios_1_1_a_1_2.csv`, con su origen y su motivo, y se pueden confirmar o revertir (decisión D-13.2). Son además el estrato E1 de la revisión humana que propone el documento 13.

### 9. Cuánto coincide una lectura a ciegas con la categorización

**Qué mide.** El acuerdo entre una lectura automática a ciegas y la coordenada de la versión 1.1. En territorio y en dominio esa coordenada es casi siempre la heredada de la Taxonomía 5.3, que la política de migración mandaba conservar: la muestra mide sobre todo cuánto coincide un lector automático con la coordenada heredada, y no la reproducibilidad del método de clasificación. No es una revisión humana.

**Cómo se eligió.** Es una muestra estratificada sobre los 595 pre-ensayos que en la versión 1.1 no estaban en D20 ni eran migraciones a un dominio nuevo. Los estratos son la confianza que declaró el clasificador: alta (40 sorteados de 419), media (40 sorteados de 169) y baja (los 7, sin sorteo). No es un sorteo simple de todo el corpus.

| Eje | Confianza alta (419 en el marco) | Confianza media (169 en el marco) | Confianza baja (7 en el marco) | Estimación para los 595 del marco |
|---|---|---|---|---|
| Territorio | 31 de 40 (78 %; 62–88) | 26 de 40 (65 %; 50–78) | 2 de 7 | 73 % (64–83) |
| Dominio | 37 de 40 (93 %; 80–97) | 29 de 40 (73 %; 57–84) | 2 de 7 | 86 % (80–93) |
| Subfunción | 33 de 40 (83 %; 68–91) | 30 de 40 (75 %; 60–86) | 5 de 7 | 80 % (72–89) |
| Función | 37 de 40 (93 %; 80–97) | 35 de 40 (88 %; 74–95) | 7 de 7 | 91 % (85–97) |
| Los tres ejes a la vez | 25 de 40 (63 %; 47–76) | 16 de 40 (40 %; 26–55) | 0 de 7 | 55 % (45–66) |

Cada celda da los casos en que el segundo lector eligió el mismo primario, el porcentaje y, entre paréntesis, el intervalo de confianza del 95 %. La última columna pondera los tres estratos por su tamaño.

| Eje | Coordenada heredada de la Taxonomía 5.3 | Coordenada asignada por el clasificador |
|---|---|---|
| Territorio | 53 de 78 (68 %; 57–77) | 6 de 9 (67 %; 35–88) |
| Dominio | 60 de 78 (77 %; 66–85) | 8 de 9 (89 %; 56–98) |
| Subfunción | 18 de 27 (67 %; 48–81) | 50 de 60 (83 %; 72–91) |

- En territorio y en dominio, casi todo lo que se compara es coordenada heredada de la Taxonomía 5.3: la muestra dice sobre todo cuánto coincide un lector automático con la coordenada heredada.
- El dominio coincide más que el territorio, y el acuerdo baja con la confianza que declaró el clasificador. Con estos tamaños los intervalos se tocan: son tendencias probables, no seguras.
- En 46 de los 87 casos la lectura a ciegas difiere en algún eje. Ninguno se cambió por esa lectura: el desacuerdo no dice cuál de las dos lecturas se equivoca. 1 de ellos cambió por otra vía y está en el estrato E1; los otros 45 son el estrato E2 de la revisión humana.
- Los dos revisores señalaron reglas que no deciden. El territorio es el eje más afectado: las reglas no dicen de quién es la perspectiva (regla propuesta RP-09), y el gobierno no tiene territorio propio.

**Cómo leerlo.** Los dos lectores son agentes con la misma configuración. El acuerdo dice que una lectura automática llega a la coordenada vigente, no que la coordenada sea correcta, y un error que los dos comparten no aparece aquí.

**Muestra de control (versión 1.0).** Un clasificador volvió a categorizar 48 pre-ensayos con las mismas instrucciones. En 45 de los 48 casos el clasificador de control recibió el territorio y el dominio vigentes con la instrucción de conservarlos, de modo que el acuerdo en esos dos ejes no mide la reproducibilidad de la asignación. La muestra a ciegas de la versión 1.2 (data/muestra_a_ciegas_1_2.json) tampoco mide eso: mide el acuerdo de un lector automático, que clasificó desde cero, con la coordenada vigente, que en territorio y dominio es casi siempre la heredada. Sí mide el acuerdo en lo que el clasificador asignaba desde cero:

| Eje | Casos | Acuerdos | Acuerdo |
|---|---|---|---|
| Territorio primario (sin valor vigente) | 3 | 3 | 100,0 % |
| Dominio primario (sin valor vigente) | 3 | 3 | 100,0 % |
| Función (sin subfunción vigente) | 24 | 24 | 100,0 % |
| Subfunción (sin subfunción vigente) | 24 | 23 | 95,8 % |
| Horizonte | 48 | 45 | 93,8 % |
| Pilar MCCS | 48 | 42 | 87,5 % |
| Confianza declarada | 48 | 36 | 75,0 % |

### 10. Límites

- La categorización la hicieron agentes. No hay revisión humana.
- El acuerdo de un lector a ciegas con la coordenada vigente no mide acierto. Tampoco mide la reproducibilidad del método de clasificación, porque casi todo lo que se compara es coordenada heredada. Y los lectores comparten configuración.
- Las segundas lecturas recibieron los textos recortados. En 52 de los 87 registros (20 de 47 en la primera muestra y 32 de 40 en la complementaria), el campo «tesis» que recibió el lector repite el comienzo del texto y no es una tesis propia.
- 285 pre-ensayos son en su mayor parte plantilla: su clasificación descansa en muy poco texto.
- Los lotes agrupan clases de pre-ensayos, de modo que las diferencias entre lotes mezclan diferencias de contenido con diferencias de criterio. Un clasificador advirtió que su frontera entre H02 y H03 puede no coincidir con la de otros.
- La política de conservar la 5.3 arrastra sus errores. Solo D20, las migraciones, una muestra y siete sugerencias tuvieron otra lectura: 502 pre-ensayos tienen una sola.
- El horizonte, las fuerzas y el pilar no tuvieron segunda lectura en ningún pre-ensayo.
- El corpus no es neutral respecto de un proveedor: 77 pre-ensayos nombran sus productos o al proveedor.
- Las reglas de asignación dejan casos sin decidir: son las 18 reglas propuestas de la decisión D-11.

### 11. Revisión humana

El documento 13 (sección 8.5) propone una sola forma de hacerla, que reemplaza a la lista de prioridades de las versiones anteriores: una muestra de 246 pre-ensayos en cinco estratos, con una regla de decisión y un camino mínimo de 108. La revisa el autor o una persona que él designe.

| Estrato | Qué es | Pre-ensayos | En la muestra |
|---|---|---|---|
| E1 | Cambió en la versión 1.2, o es uno de los casos de D20 en que las dos lecturas no coinciden | 48 | 48 |
| E2 | La lectura a ciegas de un segundo lector automático difiere de la coordenada vigente en algún eje | 45 | 45 |
| E3 | Confianza media o baja del clasificador | 177 | 49 |
| E4 | Confianza alta, clases con mayoría de texto de plantilla (K y HC) | 160 | 48 |
| E5 | Confianza alta, demás clases | 309 | 56 |

Fuera de esa muestra quedan dos cosas que conviene mirar al redactar cada ensayo: los casos dudosos que cada clasificador dejó anotados (`anexos/A6_Notas_de_los_clasificadores.md`), y la frontera entre H02 y H03 y la asignación de pilar MCCS, que no tienen segunda lectura.

### 12. Celdas en blanco: capa de ampliación

Para las celdas sin pre-ensayos o con uno solo hay 16 pre-ensayos de la serie APX, de redacción asistida. Tu aceptación en bloque se leyó como un «sí» a incorporarlos (decisión D-10, a confirmar en D-14.3), y un revisor los leyó uno por uno: 4 quedaron como estaban y 12 se corrigieron. Entran al grafo como **capa de ampliación**: no integran el corpus de 739 ni sus estadísticas, y no cuentan como evidencia para admitir un dominio.

| Id | Celda | Título | Territorio | Dominio | Subfunción | Revisión |
|---|---|---|---|---|---|---|
| APX-01 | D19 | Inventario y propiedad de los dispositivos conectados que nadie gestiona | T05 | D19 | ID01 | sin cambios |
| APX-02 | D19 | Requisitos de seguridad en la compra de dispositivos conectados | T08 | D19 | GV09 | corregido |
| APX-03 | D19 | Aislar lo que no puede protegerse a sí mismo | T05 | D19 | PR03 | corregido |
| APX-04 | D19 | Actualización, fin de soporte y retiro de dispositivos conectados | T04 | D19 | GV04 | corregido |
| APX-05 | D19 | Vigilar por el comportamiento lo que no admite agente | T06 | D19 | DE01 | corregido |
| APX-06 | D19 | Cuando el incidente digital tiene efecto físico | T04 | D19 | RS01 | sin cambios |
| APX-07 | D19 | Modelar las amenazas del dispositivo antes de integrarlo | T05 | D19 | ID03 | corregido |
| APX-08 | D27 | Perímetros físicos por zonas y acceso verificable | T05 | D27 | PR06 | corregido |
| APX-09 | D27 | Energía, clima y entorno como condiciones del control | T04 | D27 | PR06 | sin cambios |
| APX-10 | D27 | Soportes y equipos: custodia, traslado, reutilización y destrucción | T05 | D27 | PR02 | sin cambios |
| APX-11 | D27 | Evidencia de la seguridad física de la nube y de la colocación | T08 | D27 | GV09 | corregido |
| APX-12 | D27 | El mantenimiento como vía de acceso | T06 | D27 | PR06 | corregido |
| APX-13 | RC05 | Informar el avance de la recuperación | T04 | D16 | RC05 | corregido |
| APX-14 | RC03 | Declarar el retorno a la normalidad con criterios y evidencia | T08 | D16 | RC03 | corregido |
| APX-15 | RC05 | Restituir la confianza después del incidente | T08 | D15 | RC05 | corregido |
| APX-16 | RC05 | Mensajes públicos de la recuperación: aprobados, coherentes y con una sola voz | T02 | D15 | RC05 | corregido |

Con la capa, D19 pasa de 0 a 7 pre-ensayos, D27 de 1 a 6 y la subfunción RC05 de 0 a 3. El texto completo está en `12_Ampliacion_Celdas_en_Blanco.md`.

### 13. Archivos

- `data/corpus_frontier_739.json`: el corpus con su coordenada 5.3, su coordenada 6.0, el origen de cada valor y los cambios de la versión 1.2.
- `data/categorizacion_739.csv`: lo mismo en una tabla.
- `data/estadisticas_corpus.json` y `data/matriz_territorio_dominio.csv`: distribuciones.
- `data/analisis_D20_decision_D03.csv` y `data/analisis_D20_decision_D03.json`: la decisión D-03 aplicada a D20, con las dos lecturas.
- `data/segunda_lectura_migraciones.csv`: la segunda lectura de las migraciones.
- `data/muestra_a_ciegas_1_2.csv` y `data/muestra_a_ciegas_1_2.json`: la muestra a ciegas, caso por caso y por estrato.
- `data/evidencia_por_preensayo.csv`: qué lecturas tuvo cada pre-ensayo, de qué tipo y con qué resultado.
- `data/casos_sin_coincidencia_D13.csv`: las fichas de los casos de D20 sin coincidencia.
- `data/revision_humana_muestra.csv`, `data/revision_humana_clave.csv` y `data/revision_humana_propuesta.json`: la muestra y la regla de decisión propuestas para la revisión humana.
- `data/muestra_de_control.json`: la muestra de control de la versión 1.0.
- `data/cambios_1_1_a_1_2.csv`: lo que cambió respecto de la versión 1.1.
- `data/ampliacion_celdas_en_blanco.csv` y `data/ampliacion_celdas_en_blanco.json`: la serie APX.

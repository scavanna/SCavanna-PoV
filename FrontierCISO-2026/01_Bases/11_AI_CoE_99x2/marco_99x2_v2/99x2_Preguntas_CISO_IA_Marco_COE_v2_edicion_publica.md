# 99 + 99 preguntas que un CISO tiene que hacer

## Marco de buenas prácticas, preludio de un centro de excelencia y postura de Microsoft para la seguridad en la era de la IA, los agentes y los sistemas cognitivos autónomos

| Ficha |  |
|---|---|
| Versión | 2.0 — 6 de noviembre de 2026 (incorpora las 9 preguntas nuevas del proceso inverso; reemplaza a la 1.0) |
| Autor | Santiago Cavanna, Principal Cloud Solution Architect Security — Microsoft MCSA |
| Estado | Propuesta de trabajo. No es un estándar certificado, una metodología validada estadísticamente ni asesoramiento legal. |
| Audiencia | CISOs, comités de riesgo y auditoría, arquitectos de seguridad, líderes de IA y datos, y directorios. |
| Base conceptual | AI CISO Atlas v3.0 (territorios, capacidades y artefactos), TheNextCISO (CISO-OS, CISO-DO, CISO-MM, CISO-NX) y el taller SAF «AI Security: Strategy and Governance Planning». |
| Cruce de marcos | NIST, CIS, The Open Group, ISACA y Cloud Security Alliance, con Microsoft Cloud Security Benchmark como puente. |
| Vigencia | Postura de Microsoft y versiones de marcos verificadas en fuentes oficiales al 6 de noviembre de 2026. Revalidar después de Microsoft Ignite 2026 (17 al 20 de noviembre) y del lanzamiento de COBIT 7 (19 de noviembre de 2026). |

## Contenido

- Resumen ejecutivo
- Novedades de la versión 2.0
- 1. Cómo usar este marco
- 2. Arquitectura del marco
- 3. La postura de Microsoft en doce mensajes
- 4. Parte A — Las 99 preguntas que todo CISO tiene que hacer
- 5. Parte B — Las 99 preguntas sobre IA, agentes y sistemas autónomos
- 6. Las 24 preguntas para el directorio
- 7. Del cuestionario al centro de excelencia (COE)
- 8. Cruce de marcos: cobertura y hallazgos
- 9. Silencios, límites y vigencia
- 10. Fuentes
- Anexo A — Equivalencia orientativa de escalas
- Anexo B — Glosario

## Resumen ejecutivo

Este documento propone **198 preguntas**: 99 sobre la agenda integral del CISO y 99 sobre la incorporación de inteligencia artificial, agentes y aplicaciones con capacidades cognitivas digitales, autónomas o semiautónomas. Están diseñadas para cumplir tres funciones a la vez:

1. **Marco de buenas prácticas.** Cada pregunta describe qué evidencia muestra una práctica madura. Responder con evidencia —no con intenciones— es aplicar el marco.
2. **Preludio de un centro de excelencia (COE).** Cada pregunta tiene una función del COE, un responsable sugerido y una ola de abordaje. Las preguntas sin respuesta verificable forman el backlog fundacional del COE.
3. **Vehículo de la postura de Microsoft.** Cada pregunta incluye la postura y las recomendaciones de Microsoft, las capacidades que la implementan y, cuando corresponde, el silencio: lo que Microsoft no publica como postura específica.

Cada pregunta se cruza con cinco familias de marcos y con el puente de Microsoft. La cobertura resultante es completa en los catálogos principales: **22 de 22** categorías de NIST CSF 2.0, **19 de 19** categorías del NIST AI RMF, **12 de 12** riesgos del perfil de IA generativa (NIST AI 600-1), **18 de 18** controles CIS v8.1, **40 de 40** objetivos de COBIT 2019, **17 de 17** dominios de CCM v4.1, **18 de 18** dominios de AICM v1.1, **7 de 7** capas de MAESTRO y **19 de 19** dominios y controles de Microsoft Cloud Security Benchmark (incluidos los siete controles de IA de la versión 2). The Open Group aporta referencias en 82 preguntas: su cuerpo de conocimiento se concentra en arquitectura, riesgo y Zero Trust, y todavía no tiene un estándar de IA publicado.

**Tesis del marco**

- La IA no reemplaza los fundamentos de seguridad: los amplifica. Si los datos están sobreexpuestos o las identidades sin gobierno, la IA lo hará visible —y explotable— más rápido.
- Los agentes son una nueva clase de identidad que actúa con autoridad delegada: necesitan identidad propia, dueño, mínimo privilegio, observabilidad y capacidad de detención probada.
- La supervisión humana debe ser proporcional al riesgo: ni aprobación manual para todo (que termina en trámite) ni autonomía sin límites técnicos.
- La confianza en la IA se demuestra con evidencia continua —pruebas, registros, indicadores— y no con declaraciones de principios.
- El CISO evoluciona hacia arquitecto de las condiciones de confianza, sin apropiarse de responsabilidades que corresponden al negocio, a Legal, a Riesgos o a Privacidad.

**Advertencias de vigencia.** COBIT 7 se lanza el 19 de noviembre de 2026 (COBIT 2019 sigue vigente hasta el 31 de diciembre de 2027); la AICM de CSA está en su versión 1.1 (junio de 2026); el Cyber AI Profile de NIST (IR 8596) es un borrador; Microsoft Cloud Security Benchmark v2 está en versión preliminar. Las capacidades de Microsoft cambian con frecuencia: el estado indicado debe revalidarse después de Microsoft Ignite 2026.

## Novedades de la versión 2.0

La versión 2.0 incorpora las **nueve preguntas** que el proceso inverso —la conversión de 99 enunciados de NIST, ISACA, ISC2, CIS, The Open Group y Cloud Security Alliance en preguntas— identificó como ausentes en la versión 1.0. Para conservar la arquitectura de **9 preguntas por dominio y 99 por parte**, cada pregunta nueva ocupa el lugar que deja una **fusión dentro del mismo dominio**: la pregunta absorbida no se elimina; su intención, su evidencia esperada, la postura de Microsoft y sus anclajes pasan a la pregunta que la absorbe. Las otras **180 preguntas conservan su identificador y su texto**.

**Criterios de la fusión.** (1) Mismo dominio y misma decisión de fondo. (2) La pregunta absorbida es la que tiene menos vínculos desde los documentos derivados (a igualdad, la de alcance más acotado). (3) Ninguna de las 24 preguntas prioritarias para el directorio fue absorbida. (4) Si la pregunta absorbida era relevante para el directorio, la que la absorbe hereda esa marca.

### Las nueve preguntas nuevas

| ID v2 | Tema | Pregunta | Origen (pareja, organismo, publicación) | Enunciado que la motivó |
|---|---|---|---|---|
| A01.9 | Gobierno y vigencia | Antes de reducir la dotación o el presupuesto de seguridad, ¿se evalúa y documenta el impacto en el riesgo, y quién acepta formalmente el riesgo residual? | IC05 · ISC2 — 2025 ISC2 Cybersecurity Workforce Study (4 de diciembre de 2025) | La mayoría de los profesionales advierte que reducir personal de ciberseguridad eleva significativamente el riesgo de brecha y que la organización debería rendir cuentas si sufre una tras recortar; solo poco más de la mitad cree tener recursos para afrontar incidentes. |
| A02.8 | Riesgo y cuantificación | ¿Nuestro análisis de riesgo considera el daño que podemos causar a terceros (clientes, ciudadanos, socios) y verifica que las salvaguardas no sean más gravosas que el riesgo que mitigan? | CI05 · CIS — CIS Risk Assessment Method (CIS RAM) v2.2 for CIS Controls v8.1 (Página fechada el 5 de diciembre de 2025) | CIS RAM, basado en el estándar DoCRA, exige considerar los intereses de todas las partes que podrían sufrir daño, reducir el riesgo a niveles aceptables para autoridades y afectados, y que las salvaguardas no pesen más que el riesgo que mitigan. |
| A02.9 | Riesgo y cuantificación | ¿Qué precisión necesita cada decisión de riesgo, y estamos invirtiendo esfuerzo de análisis que no cambiaría ninguna decisión? | OG07 · The Open Group — The Open Group Standard for Risk Analysis (O-RA), Open FAIR (O-RA 2.0.1; versión 2.1 anunciada en mayo de 2025) | O-RA propone estimaciones «útilmente precisas»: no buscar más precisión si no cambiaría la decisión, y descomponer el análisis de arriba hacia abajo solo cuando un control o el decisor lo requieran. |
| A08.6 | Personas y liderazgo | ¿Qué incidentes y configuraciones erróneas del último año se explican, al menos en parte, por falta de habilidades, y qué cambiamos en consecuencia (formación, automatización, valores seguros por defecto)? | IC07 · ISC2 — 2025 ISC2 Cybersecurity Workforce Study (4 de diciembre de 2025) | La escasez de habilidades ya produce consecuencias concretas: casi todas las organizaciones tienen al menos una carencia, la mayoría las califica de críticas y casi nueve de cada diez sufrió alguna consecuencia significativa, como sistemas mal configurados. |
| A10.6 | Gobierno y vigencia | ¿Qué versiones de los marcos de referencia usamos (COBIT, NIST, ISO, CIS, CCM) y qué plan de transición tenemos antes de que se retiren, empezando por COBIT 2019? | IS05 · ISACA — COBIT: COBIT Certificate and Exam Updates (artículo oficial de soporte sobre COBIT 7) (Actualizado el 30 de octubre de 2026) | COBIT 7 se lanza el 19 de noviembre de 2026; COBIT 2019 se retira el 31 de diciembre de 2027 y COBIT 5 se retiró el 26 de octubre de 2026. Adoptarlo a nivel organizacional requiere una licencia empresarial. |
| A10.7 | Riesgo y cuantificación | ¿Quién valida de forma independiente el modelo con el que cuantificamos el riesgo cibernético, y es lo bastante transparente, pertinente y simple para poder validarlo? | OG09 · The Open Group — Calculating Reserves for Cyber Risk: Vetting Cyber Risk Models (White Paper) (Tercer trimestre de 2022) | Los modelos de cuantificación de riesgo cibernético que usan el CRO, el CIO y el CISO deben poder validarse; para eso tienen que ser transparentes, pertinentes y parsimoniosos. |
| A11.8 | Personas y liderazgo | ¿Qué código de conducta profesional rige al equipo de seguridad, cómo se resuelven sus dilemas éticos (monitoreo de personas, divulgación de vulnerabilidades, uso de accesos privilegiados) y quién controla al que controla? | IC01 · ISC2 — ISC2 Code of Ethics (Versión vigente (sin fecha de revisión publicada)) | La seguridad y el bienestar de la sociedad, el bien común y los deberes con empleadores y colegas exigen una conducta ética ejemplar y visible; cumplir el Código es condición para conservar la certificación. |
| A11.9 | Personas y liderazgo | ¿Cómo evalúa el equipo de seguridad el liderazgo del CISO (comunicar el riesgo al directorio, sostener una visión, conseguir recursos) y qué hace el CISO con esa retroalimentación? | IC14 · ISC2 — Cybersecurity Professionals Want Leaders Who Have Been Through a Major Incident (28 de mayo de 2026) | Los equipos confían más en líderes de seguridad que comunican el riesgo al directorio, sostienen una visión estratégica y consiguen presupuesto; la pericia técnica queda última entre los rasgos valorados, y haber conducido un incidente grave aumenta la credibilidad. |
| B08.7 | Aseguramiento de la IA | ¿Qué controles de IA damos por eficaces sin garantías demostradas, y cómo compensamos ese límite con capas de defensa, monitoreo y pruebas continuas? | NI14 · NIST — Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations, NIST AI 100-2 E2025 (24 de marzo de 2025) | Muchas mitigaciones contra el aprendizaje automático adversarial son empíricas y limitadas: se adoptan porque parecen funcionar en la práctica, no porque ofrezcan garantías demostrables. |

**Lectura.** Por organismo: ISC2 4, The Open Group 2, CIS 1, ISACA 1, NIST 1. Por tema: riesgo y cuantificación 3, personas y liderazgo 3, gobierno y vigencia 2, aseguramiento de la IA 1. ISC2, el organismo centrado en los profesionales, aporta la mayor cantidad de preguntas nuevas: la versión 1.0 era más sólida en los controles que en las personas que los operan y en el propio liderazgo del CISO. La segunda concentración está en la calidad de la cuantificación del riesgo (precisión útil, validación independiente del modelo, daño a terceros), un terreno donde Microsoft no publica postura y que este marco declara como silencio.

### Las nueve fusiones

| Absorbe (ID v2) | Absorbida (ID v1) | Pregunta v1 absorbida | Vínculos derivados (absorbida / absorbente) | Por qué van juntas |
|---|---|---|---|---|
| A01.2 | A01.9 | ¿Qué modelo operativo tiene la función de seguridad (central, federado, BISO, servicios gestionados) y cómo se coordina con riesgo, privacidad, legal y negocio? | 0 / 3 | Línea de reporte y modelo operativo describen la misma decisión de diseño: cómo se organiza y a quién rinde cuentas la función. |
| A02.2 | A02.8 | ¿Qué adversarios y amenazas son relevantes para nuestro sector y país, y cómo actualiza esa visión la inteligencia de amenazas? | 3 / 4 | Los escenarios de pérdida se construyen con los adversarios relevantes: inteligencia y escenarios son un mismo análisis. |
| A02.5 | A02.9 | ¿Qué riesgo transferimos (seguros, contratos), en qué condiciones, y qué controles exige la aseguradora que hoy no podemos demostrar? | 1 / 7 | Aceptar y transferir son las dos formas de tratar el riesgo que no se mitiga; ambas exigen dueño, condiciones, vigencia y evidencia. |
| A08.5 | A08.6 | ¿Usamos la inteligencia de amenazas para priorizar y cazar, o solo para enriquecer alertas? | 0 / 0 | La inteligencia de amenazas es el insumo de la ingeniería de detección y de la cacería; separadas, ninguna cambia decisiones. |
| A10.1 | A10.7 | ¿Cómo nos preparamos para regulaciones de ciberseguridad y resiliencia operativa digital que nos alcanzan directa o indirectamente (por ejemplo, DORA, NIS2 o normas locales)? | 2 / 3 | La preparación para DORA, NIS2 o normas locales es un caso del mapa de obligaciones y de su plan de cumplimiento. |
| A10.3 | A10.6 | ¿Qué evidencia podríamos entregar en 48 horas a un regulador o auditor sobre un incidente o un control específico? | 2 / 5 | Poder entregar evidencia en 48 horas es la prueba práctica de que la evidencia es automática y continua. |
| A11.1 | A11.8 | ¿Reconocemos y premiamos la reducción de riesgo y la adopción segura, en lugar de premiar solo la velocidad o el bloqueo? | 1 / 3 | Conductas esperadas e incentivos son dos caras del mismo cambio de comportamiento. |
| A11.4 | A11.9 | ¿Cómo entrena el CISO su propio criterio (sesgos, diario de decisiones, disenso, mentores) para decidir bajo incertidumbre? | 2 / 4 | Bienestar y criterio sostienen juntos el rol del CISO: sin uno, el otro no alcanza. |
| B08.2 | B08.7 | ¿Cómo recogemos y procesamos los reportes de usuarios sobre fallas, sesgos o comportamientos indebidos de la IA? | 0 / 1 | Los reportes de usuarios son una fuente más del monitoreo en producción y deben llegar al mismo circuito de mejora. |

El texto completo de cada pregunta fusionada figura en su dominio, marcado como «Versión 2.0».

### Efecto en la arquitectura

| Indicador | Versión 1.0 | Versión 2.0 |
|---|---|---|
| Preguntas por dominio / por parte / total | 9 / 99 / 198 | 9 / 99 / 198 |
| Función del COE: Riesgo, cumplimiento y aseguramiento | 41 | 43 |
| Función del COE: Operaciones, detección y respuesta | 27 | 25 |
| Ola 1 (30–90 días) | 82 | 83 |
| Ola 2 (90–180 días) | 67 | 66 |
| Relevantes para el directorio (Parte A / Parte B) | 34 / 19 | 38 / 20 |
| Preguntas con silencio declarado de Microsoft | 6 | 9 |
| Preguntas con referencia a The Open Group | 80 | 82 |

Las funciones del COE y las olas que no figuran en la tabla no cambian. La función de riesgo, cumplimiento y aseguramiento pasa de 41 a 43 porque 5 de las preguntas nuevas le pertenecen; la de operaciones pasa de 27 a 25 porque las dos preguntas sobre inteligencia de amenazas se integraron en los escenarios de pérdida (A02.2) y en la ingeniería de detección (A08.5). Las relevantes para el directorio crecen porque cuatro preguntas nuevas lo son y tres fusiones heredan esa marca.

### Trazabilidad y efecto en los documentos derivados

Los documentos «99 preguntas que le harán al CISO» y «Del marco a la pregunta» se construyeron sobre la versión 1.0 y siguen siendo válidos con sus identificadores originales. Al leerlos junto con la versión 2.0, estos vínculos deben traducirse:

| Documento | Pregunta o pareja | Vínculo v1 | Equivalente v2 | Nota |
|---|---|---|---|---|
| 99 preguntas que le harán al CISO | C01.8 | A10.7 | A10.1 | En la v2, A10.7 es otra pregunta (nueva, origen OG09). |
| 99 preguntas que le harán al CISO | C02.8 | A02.8 | A02.2 | En la v2, A02.8 es otra pregunta (nueva, origen CI05). |
| 99 preguntas que le harán al CISO | C04.5 | A02.9 | A02.5 | En la v2, A02.9 es otra pregunta (nueva, origen OG07). |
| 99 preguntas que le harán al CISO | C05.3 | A10.6 | A10.3 | En la v2, A10.6 es otra pregunta (nueva, origen IS05). |
| 99 preguntas que le harán al CISO | C07.6 | A10.7 | A10.1 | En la v2, A10.7 es otra pregunta (nueva, origen OG09). |
| 99 preguntas que le harán al CISO | C09.2 | A10.6 | A10.3 | En la v2, A10.6 es otra pregunta (nueva, origen IS05). |
| 99 preguntas que le harán al CISO | C11.2 | A11.8 | A11.1 | En la v2, A11.8 es otra pregunta (nueva, origen IC01). |
| Del marco a la pregunta (proceso inverso) | IC02 | A11.9 | A11.4 | En la v2, A11.9 es otra pregunta (nueva, origen IC14). |
| Del marco a la pregunta (proceso inverso) | IC14 | A11.9 | A11.4 | En la v2, A11.9 es otra pregunta (nueva, origen IC14). |
| Del marco a la pregunta (proceso inverso) | OG06 | A02.8 | A02.2 | En la v2, A02.8 es otra pregunta (nueva, origen CI05). |
| Del marco a la pregunta (proceso inverso) | CS18 | A02.8 | A02.2 | En la v2, A02.8 es otra pregunta (nueva, origen CI05). |

Regla general de traducción: un identificador v1 absorbido se lee como su pregunta absorbente en la v2 (A01.9→A01.2, A02.8→A02.2, A02.9→A02.5, A08.6→A08.5, A10.6→A10.3, A10.7→A10.1, A11.8→A11.1, A11.9→A11.4, B08.7→B08.2); todos los demás identificadores no cambian.

### Las preguntas nuevas ya tienen quien las pida

Cada pregunta nueva nació de una pareja del proceso inverso, y esa pareja ya estaba vinculada con preguntas que le harán al CISO. Por lo tanto, la evidencia que pide la pregunta nueva es la que el CISO necesita para responderlas:

| Pregunta nueva (v2) | Pregunta al CISO | Quién la formula | Texto |
|---|---|---|---|
| A01.9 | C01.9 | Directorio | ¿Tenemos el CISO, el equipo y el presupuesto que este riesgo requiere? |
| A01.9 | C04.2 | CFO, finanzas y tesorería | ¿Qué retorno tuvo el presupuesto de seguridad que aprobamos el año pasado? |
| A02.8 | C02.2 | Comité de auditoría y riesgos | ¿Qué excepciones y aceptaciones de riesgo están vigentes, cuáles vencieron y quién las aprobó? |
| A02.9 | C04.2 | CFO, finanzas y tesorería | ¿Qué retorno tuvo el presupuesto de seguridad que aprobamos el año pasado? |
| A08.6 | C09.8 | Auditoría interna, auditoría externa y certificadores | ¿Qué hallazgos se repiten y qué dicen de la causa raíz? |
| A10.6 | C02.1 | Comité de auditoría y riesgos | ¿Qué controles clave tenemos y qué evidencia independiente demuestra que funcionan, no solo que existen? |
| A10.7 | C02.4 | Comité de auditoría y riesgos | ¿Cómo sabemos que los indicadores que nos presenta el CISO son confiables? |
| A11.8 | C07.3 | Legal, cumplimiento y privacidad | ¿El monitoreo de seguridad respeta la privacidad de los empleados? |
| A11.9 | C11.5 | Personas: colaboradores, RR. HH. y el equipo de seguridad | ¿Cuáles son nuestras tres prioridades y qué dejamos de hacer? |
| B08.7 | C02.5 | Comité de auditoría y riesgos | ¿Qué controles específicos tenemos sobre la IA y los agentes, y quién los audita? |

Con estos vínculos, **163 de las 198 preguntas** de la versión 2.0 preparan al menos una de las 99 preguntas que le harán al CISO (159 en la versión 1.0), y **35** quedan como trabajo invisible: sostienen las respuestas aunque ningún interlocutor las pida en forma directa.

## 1. Cómo usar este marco

### 1.1 Anatomía de cada pregunta

| Elemento | Contenido |
|---|---|
| Pregunta | Formulada para exigir evidencia: quién decide, cómo se sabe, cuándo se probó. |
| Por qué importa | La consecuencia de no tener respuesta. |
| Buena práctica (evidencia esperada) | Cómo se ve una respuesta de nivel 3 (probado) en la escala de evidencia. |
| Postura de Microsoft | Lo que Microsoft recomienda o hace, con la fuente que lo respalda; incluye silencios declarados. |
| Capacidades Microsoft | Productos, guías o programas que materializan la postura; verificar estado y licenciamiento antes de comunicarlos. |
| Cruce de marcos | Correspondencias temáticas con NIST, CIS, The Open Group, ISACA, CSA y Microsoft Cloud Security Benchmark (MCSB). |
| Anclaje propio | Territorio y capacidad del AI CISO Atlas, componente de TheNextCISO y disciplina de SAF. |
| COE | Función del COE, responsable sugerido, ola de abordaje y relevancia para el directorio. |

### 1.2 Escala de evidencia (AI CISO Atlas)

| Nivel | Nombre | Criterio |
|---|---|---|
| 0 | No definido | Sin dueño ni escenario. |
| 1 | Documentado | Políticas o diseños sin prueba suficiente. |
| 2 | Implementado | Controles y responsables identificables. |
| 3 | Probado | Escenarios y mecanismos ensayados con evidencia. |
| 4 | Adaptativo | Pruebas recurrentes, métricas, aprendizaje y cambios validados. |

La escala se aplica a cada pregunta con evidencia verificable. Un puntaje interno no equivale a una certificación ni demuestra cumplimiento jurídico.

### 1.3 Reglas de uso

1. Responder con evidencia, no con intención: una política sin prueba es nivel 1.
2. Una pregunta, un dueño: cada respuesta tiene un responsable con nombre y fecha de revisión.
3. No promediar: un cero en contención o recuperación no se compensa con un cuatro en otra pregunta (regla del AI CISO Atlas).
4. Distinguir la naturaleza de cada referencia: ley, estándar, guía, patrón técnico, hipótesis u opinión.
5. Los cruces de marcos son correspondencias temáticas, no equivalencias de control; para auditoría, verificar el texto del control.
6. Revalidar el estado de cada capacidad de Microsoft (disponibilidad general, versión preliminar, licenciamiento) antes de comunicarla a un cliente.
7. Reutilizar la evidencia entre marcos: se recolecta una vez y se mapea muchas veces.
8. Repetir la evaluación cada trimestre: la IA y las amenazas cambian más rápido que los ciclos anuales.

### 1.4 Cómo se ejecuta en la práctica

1. **Seleccionar** las preguntas por audiencia: directorio (sección 6), comité ejecutivo, consejo de IA y seguridad, o equipos técnicos.
2. **Responder con evidencia** y asignar un nivel de 0 a 4 por pregunta en la matriz operativa que acompaña este documento.
3. **Convertir cada brecha** en un ítem del backlog del COE con dueño, fecha y criterio de cierre.
4. **Mapear la evidencia** a los marcos que la organización debe demostrar (NIST, CIS, ISO, COBIT, CSA) usando las columnas de cruce.
5. **Repetir cada trimestre** y comunicar la tendencia, no un promedio.

## 2. Arquitectura del marco

### 2.1 Dos partes, 22 dominios, 198 preguntas

| Código | Dominio | Foco | Preguntas | Para el directorio | Funciones del COE principales |
|---|---|---|---|---|---|
| A01 | Mandato, gobierno y directorio | Quién manda, quién decide y cómo rinde cuentas la organización por el riesgo cibernético. | 9 | 7 | Gobierno, políticas y decisiones · Valor, métricas y comunicación ejecutiva |
| A02 | Riesgo, apetito, cuantificación y valor | Cómo se expresa, cuantifica, acepta y comunica el riesgo en el idioma en que decide el negocio. | 9 | 6 | Riesgo, cumplimiento y aseguramiento · Valor, métricas y comunicación ejecutiva |
| A03 | Arquitectura, estrategia técnica y Zero Trust | Qué arquitectura y qué principios hacen que la seguridad sea una propiedad del diseño y no un agregado. | 9 | 2 | Arquitectura y patrones seguros · Plataforma e ingeniería de controles |
| A04 | Identidad y acceso privilegiado | La identidad como plano de control: personas, administradores e identidades no humanas. | 9 | 1 | Plataforma e ingeniería de controles · Operaciones, detección y respuesta |
| A05 | Datos, privacidad y criptografía | Saber dónde está la información, quién accede y cómo se protege durante todo su ciclo de vida. | 9 | 2 | Plataforma e ingeniería de controles · Riesgo, cumplimiento y aseguramiento |
| A06 | Exposición: activos, configuración y vulnerabilidades | Reducir la ventana de exposición antes de que un adversario la aproveche. | 9 | 2 | Plataforma e ingeniería de controles · Valor, métricas y comunicación ejecutiva |
| A07 | Nube, aplicaciones, terceros y cadena de suministro | La seguridad que se hereda, se compra o se construye: nube, software, APIs y proveedores. | 9 | 2 | Arquitectura y patrones seguros · Riesgo, cumplimiento y aseguramiento |
| A08 | Operaciones de seguridad: detección, respuesta y caza | Ver, decidir y contener a la velocidad a la que operan los atacantes. | 9 | 2 | Operaciones, detección y respuesta · Cultura, talento y adopción |
| A09 | Resiliencia, continuidad, recuperación y crisis | Sostener los resultados del negocio cuando la prevención falla. | 9 | 5 | Plataforma e ingeniería de controles · Riesgo, cumplimiento y aseguramiento |
| A10 | Cumplimiento, regulación y aseguramiento continuo | Demostrar con evidencia, de forma continua y reutilizable, que los controles funcionan. | 9 | 5 | Riesgo, cumplimiento y aseguramiento · Gobierno, políticas y decisiones |
| A11 | Personas, cultura, talento y sostenibilidad del rol | Las personas que sostienen el programa, incluido el propio CISO. | 9 | 4 | Cultura, talento y adopción · Valor, métricas y comunicación ejecutiva |
| B01 | Estrategia, valor y apetito de riesgo de la IA | Para qué queremos la IA, cuánto riesgo aceptamos y cómo equilibramos oportunidad y exposición. | 9 | 6 | Gobierno, políticas y decisiones · Riesgo, cumplimiento y aseguramiento |
| B02 | Gobierno, roles, políticas y centro de excelencia de IA | Las estructuras, reglas y capacidades que convierten principios de IA responsable en práctica. | 9 | 2 | Gobierno, políticas y decisiones · Riesgo, cumplimiento y aseguramiento |
| B03 | Inventario, descubrimiento e IA no autorizada | No se puede gobernar lo que no se ve: modelos, agentes, herramientas y uso no autorizado. | 9 | 1 | Plataforma e ingeniería de controles · Arquitectura y patrones seguros |
| B04 | Identidad, autoridad y delegación de agentes | Los agentes como una nueva clase de identidad que actúa con autoridad delegada. | 9 | 0 | Plataforma e ingeniería de controles · Arquitectura y patrones seguros |
| B05 | Datos para la IA: exposición, protección y ciclo de vida | La IA amplifica lo bueno y lo malo de la gestión de datos existente. | 9 | 1 | Plataforma e ingeniería de controles · Riesgo, cumplimiento y aseguramiento |
| B06 | Amenazas a modelos, aplicaciones y agentes | Las formas nuevas en que los sistemas de IA pueden ser engañados, abusados o comprometidos. | 9 | 1 | Arquitectura y patrones seguros · Plataforma e ingeniería de controles |
| B07 | Autonomía, supervisión humana y contención | Cuánta autonomía otorgar, dónde intervenir y cómo detener a tiempo. | 9 | 3 | Riesgo, cumplimiento y aseguramiento · Arquitectura y patrones seguros |
| B08 | Evaluación, pruebas y aseguramiento continuo de la IA | La confianza en la IA como resultado de pruebas recurrentes y evidencia verificable. | 9 | 3 | Riesgo, cumplimiento y aseguramiento · Operaciones, detección y respuesta |
| B09 | Observabilidad, detección y respuesta a incidentes de IA | Registrar, detectar, investigar y responder cuando la IA o un agente se comporta mal. | 9 | 1 | Operaciones, detección y respuesta · Riesgo, cumplimiento y aseguramiento |
| B10 | Regulación, terceros y confianza | Obligaciones, proveedores y la confianza de clientes, empleados y reguladores. | 9 | 2 | Riesgo, cumplimiento y aseguramiento · Arquitectura y patrones seguros |
| B11 | IA para la seguridad: SOC agéntico y fuerza laboral digital | Usar IA y agentes para defender, sin perder criterio humano ni control. | 9 | 0 | Operaciones, detección y respuesta · Plataforma e ingeniería de controles |

### 2.2 Anclajes propios

| Anclaje | Qué aporta | Cómo se usa aquí |
|---|---|---|
| AI CISO Atlas v3.0 | Seis territorios (SELF, ORGANIZATION, RISK, TECHNOLOGY, AI & AGENTS, TRUST), cinco capacidades transversales (Anticipar, Limitar, Contener, Recuperar, Gobernar), la escala de evidencia 0–4 y los artefactos CDRR, ABRP, CTB y RRC. | Cada pregunta lleva su territorio y su capacidad primaria; los artefactos son entregables del COE. |
| TheNextCISO | CISO-OS (gobierno y estructura), CISO-DO (operación de dominios), CISO-MM (madurez multidimensional) y CISO-NX (nueva generación y habilitación del negocio). | Cada pregunta se ubica en el componente que la gobierna. |
| SAF — AI Security: Strategy and Governance Planning | Nueve disciplinas de seguridad, antipatrones y buenas prácticas, Zero Trust aplicado a la IA, modelo de responsabilidad compartida y hoja de ruta de gobierno y seguridad de IA en cinco niveles. | Disciplina SAF por pregunta y fuente principal de la postura de Microsoft. |

### 2.3 Cruce con marcos externos

Las correspondencias son **temáticas**: indican dónde cada marco trata el tema de la pregunta. Se trabajó a nivel de categoría, objetivo o dominio para evitar falsas equivalencias de control; donde el identificador de control es estable y verificable se indica la salvaguarda (por ejemplo, CIS 5.5).

| Familia | Marcos usados en el cruce | Versión vigente al 6-nov-2026 |
|---|---|---|
| NIST | CSF 2.0; AI RMF 1.0 y Playbook; AI 600-1; IR 8596 (borrador); COSIS; AI 100-2 E2025; SP 800-207 y 1800-35; SSDF y SP 800-218A; SP 800-61 Rev. 3; SP 800-161 Rev. 1; IR 8286 Rev. 1; FIPS 203–205 e IR 8547; Privacy Framework; iniciativas de agentes de CAISI y NCCoE | CSF 2.0 (feb-2024); AI RMF 1.0 en revisión sin borrador; IR 8547 final (27-oct-2026) |
| CIS | Critical Security Controls v8.1; guías complementarias de IA para LLM, agentes y MCP; AI Security Guidance Workbook; CIS Benchmarks; CIS RAM v2.2 | v8.1 (jun-2024), sin v9 publicada |
| The Open Group | TOGAF 10.ª edición (fases del ADM, gobierno y principios); guía G152 de riesgo y seguridad; Open FAIR (O-RT 3.0.1, O-RA 2.0.1); Zero Trust Commandments; Security Principles for Architecture; O-ESA; guía G268 de IA; borrador de roles de seguridad citado por SAF | Sin estándar de IA publicado |
| ISACA | COBIT 2019 (40 objetivos); Risk IT 2.ª ed.; DTEF; AI Audit Toolkit; dominios de AAISM | COBIT 2019 vigente; COBIT 7 el 19-nov-2026 |
| Cloud Security Alliance | CCM v4.1 y CAIQ; AICM v1.1; MAESTRO; STAR y STAR for AI; Agentic AI Red Teaming Guide; Agentic AI IAM | CCM v4.1 (ene-2026); AICM v1.1 (jun-2026) |
| Puente Microsoft | Microsoft Cloud Security Benchmark v1 (12 dominios) y v2 (dominio AI, controles AI-1 a AI-7); plantillas de Purview Compliance Manager | MCSB v2 en versión preliminar |

## 3. La postura de Microsoft en doce mensajes

Los doce mensajes resumen la postura de Microsoft verificada en fuentes oficiales al 6 de noviembre de 2026. Cada uno indica en qué preguntas se aplica. Las afirmaciones atribuidas a SAF provienen del material del taller «AI Security: Strategy and Governance Planning» del Security Adoption Framework de Microsoft.

### 3.1 La seguridad es la prioridad: por diseño, por defecto y en operaciones

Con la Secure Future Initiative, Microsoft se aplica a sí misma tres principios (seguro por diseño, por defecto y en operaciones) y seis pilares: identidades y secretos; inquilinos y aislamiento de producción; redes; sistemas de ingeniería; monitoreo y detección; respuesta y remediación. Desde 2024 gobierna el programa un consejo de Deputy CISOs, la compensación del liderazgo sénior está ligada a la seguridad y la seguridad forma parte de la evaluación de todos los empleados. El cuarto informe de progreso se publicó en julio de 2026.

*Dónde se aplica:* A01.1, A01.2, A01.8, A03.3, A11.5, A11.1. *Fuentes:* https://www.microsoft.com/en-us/trust-center/security/secure-future-initiative · https://www.microsoft.com/en-us/trust-center/security/secure-future-initiative/sfi-progress-report-july-2026

### 3.2 Zero Trust es la estrategia, también para la IA

Verificar explícitamente, usar mínimo privilegio y asumir compromiso. Aplicado a la IA, SAF lo traduce así: verificar todas las identidades que acceden a aplicaciones de IA, asegurar que la IA solo acceda a los datos necesarios y que los agentes tengan el mínimo privilegio, y asumir que cada prompt puede ser malicioso, que cada respuesta puede filtrar datos y que cada componente de IA puede tener vulnerabilidades. IA y Zero Trust tienen una relación simbiótica: la IA necesita Zero Trust y lo acelera.

*Dónde se aplica:* A03.2, B04.3, B04.9, B06.2, B07.3. *Fuentes:* https://learn.microsoft.com/en-us/security/zero-trust/adopt/zero-trust-adoption-overview · SAF (taller AI Security: Strategy and Governance Planning)

### 3.3 La identidad es el plano de control, incluidas las identidades no humanas y los agentes

El Microsoft Digital Defense Report 2026 confirma que la identidad es el plano de control primario y extiende la recomendación de MFA resistente al phishing, passkeys y acceso privilegiado a identidades no humanas y agentes. Según el informe 2025, la MFA resistente al phishing bloquea más del 99 % de los ataques de identidad. Microsoft aplica MFA obligatoria a todos los usuarios de Azure y ofrece Microsoft Entra Agent ID, disponible de forma general desde mayo de 2026.

*Dónde se aplica:* A04.1, A04.4, A04.6, B04.1, B04.5. *Fuentes:* https://www.microsoft.com/en-us/security/security-insider/threat-landscape/2026-digital-defense-report · https://learn.microsoft.com/en-us/entra/identity/authentication/concept-mandatory-multifactor-authentication · https://learn.microsoft.com/en-us/entra/agent-id/whats-new-agent-id

### 3.4 La IA amplifica los fundamentos: primero datos, identidad y exposición

SAF identifica como antipatrones ejecutar IA sin preparación, conceder autonomía sin control, descuidar los fundamentos de datos y seguridad, confiar a ciegas y aplicar solo controles clásicos. Como la IA facilita el descubrimiento de datos, la sobreexposición debe corregirse antes: Purview DSPM evalúa la sobreexposición y SharePoint Advanced Management, incluido con las licencias de Copilot, aporta Restricted Content Discovery e informes de permisos.

*Dónde se aplica:* B01.7, B05.1, A05.1, A05.2. *Fuentes:* https://learn.microsoft.com/en-us/purview/data-security-posture-management-learn-about · https://learn.microsoft.com/en-us/sharepoint/sharepoint-advanced-management-features-copilot-license

### 3.5 Sus datos son suyos

La protección de datos empresariales de Microsoft 365 Copilot se rige por el anexo de protección de datos y los Product Terms, con Microsoft como encargado del tratamiento: los prompts, las respuestas y los datos de Microsoft Graph no se usan para entrenar modelos fundacionales, y Copilot respeta permisos, etiquetas, retención y auditoría. Dos excepciones a revisar en cada contrato: las búsquedas web en Bing, donde Microsoft actúa como responsable independiente, y los modelos de Anthropic, que quedan fuera del EU Data Boundary.

*Dónde se aplica:* B05.3, B05.9, B10.3. *Fuentes:* https://learn.microsoft.com/en-us/microsoft-365/copilot/enterprise-data-protection

### 3.6 IA responsable como sistema de gobierno, no como declaración

Microsoft adoptó en 2018 seis principios (equidad; confiabilidad y seguridad; privacidad y seguridad; inclusión; transparencia; responsabilidad) y los hace operativos con su Responsible AI Standard, estructuras de gobierno, formación y herramientas. Su Responsible AI Transparency Report 2026 informa más de 450 revisiones de usos sensibles en un año, más del 30 % sobre IA agéntica.

*Dónde se aplica:* B01.6, B02.1, B10.2, B10.6. *Fuentes:* https://www.microsoft.com/en-us/ai/principles-and-approach · https://www.microsoft.com/en-us/corporate-responsibility/topics/responsible-ai/reports/transparency-report/

### 3.7 La responsabilidad es compartida, pero el uso, los datos, la identidad y la aprobación humana son del cliente

El modelo de responsabilidad compartida de IA de Microsoft distingue plataforma, aplicación y uso, y recomienda empezar por soluciones SaaS. Su versión para agentes agrega orquestación, herramientas y memoria, y deja claro que la aprobación humana de las acciones de alto impacto es siempre responsabilidad del cliente.

*Dónde se aplica:* A07.1, B01.3, B07.1, B07.3, B10.5. *Fuentes:* https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility-ai · https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility-ai-agent

### 3.8 Cada agente necesita identidad, dueño y gobierno; la organización rinde cuentas por sus agentes

SAF advierte que las organizaciones deben esperar rendir cuentas por todas las acciones y decisiones de sus agentes. Microsoft Agent 365, disponible de forma general desde el 1 de mayo de 2026, actúa como plano de control (registro, control de acceso, visualización, interoperabilidad y seguridad, con cuarentena de agentes no autorizados). Microsoft 365 E7 —The Frontier Suite— reúne Microsoft 365 Copilot, Microsoft 365 E5, Microsoft Entra Suite y Agent 365, e incluye Security Copilot.

*Dónde se aplica:* B02.5, B02.6, B03.1, B03.7, B07.5. *Fuentes:* https://learn.microsoft.com/en-us/microsoft-agent-365/overview · https://www.microsoft.com/en-us/security/blog/2026/05/01/microsoft-agent-365-now-generally-available-expands-capabilities-and-integrations/ · https://techcommunity.microsoft.com/blog/microsoft_365blog/microsoft-365-e7-and-agent-365-are-now-generally-available/4516295

### 3.9 Modelar amenazas y probar de forma adversaria toda IA, sin tercerizar el pensamiento crítico

SAF pide modelar las amenazas de todos los sistemas de IA con las cuatro preguntas del Threat Modeling Manifesto y la extensión STRIDER-TIM, y advierte: nunca tercerizar en la IA el pensamiento crítico. El AI Red Team de Microsoft publicó las lecciones de probar más de 100 productos de IA generativa y una taxonomía de modos de falla en sistemas agénticos; el AI Red Teaming Agent de Foundry automatiza parte de esas pruebas con PyRIT.

*Dónde se aplica:* B06.1, B06.6, B06.9, B08.4, B11.5. *Fuentes:* https://www.microsoft.com/en-us/security/blog/2025/01/13/3-takeaways-from-red-teaming-100-generative-ai-products/ · https://www.microsoft.com/en-us/security/blog/2025/04/24/new-whitepaper-outlines-the-taxonomy-of-failure-modes-in-ai-agents/ · https://learn.microsoft.com/en-us/azure/foundry/concepts/ai-red-teaming-agent

### 3.10 Proteger en ejecución, en capas

Prompt Shields detecta ataques directos y en documentos (en Foundry, la detección en documentos debe activarse); Defender for AI Services alerta sobre jailbreak, fuga de datos y robo de credenciales; Task Adherence y la protección en tiempo real de agentes (en versión preliminar) bloquean llamadas a herramientas riesgosas; la pasarela de IA de Azure API Management limita el consumo y gobierna servidores MCP. La guía de Microsoft para MCP pide tratar descripciones y salidas de herramientas como no confiables y fijar los esquemas aprobados.

*Dónde se aplica:* B06.2, B06.3, B06.5, B06.7, B07.6. *Fuentes:* https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection · https://learn.microsoft.com/en-us/azure/defender-for-cloud/ai-threat-protection · https://learn.microsoft.com/en-us/azure/developer/azure-mcp-server/security

### 3.11 IA para la seguridad con criterio humano: un SOC agéntico supervisado

Security Copilot está incluido en Microsoft 365 E5 y E7 (400 unidades de cómputo de seguridad por mes por cada 1.000 licencias, hasta 10.000) y ofrece agentes para clasificar alertas, priorizar alertas de DLP, optimizar el acceso condicional, preparar informes de inteligencia de amenazas y, en versión preliminar, remediar vulnerabilidades. SAF recomienda usar la IA donde es fuerte, no como reemplazo ciego de las personas; la interrupción automática de ataques contiene a velocidad de máquina con acciones reversibles.

*Dónde se aplica:* A08.3, B11.1, B11.2, B11.6, B11.7. *Fuentes:* https://learn.microsoft.com/en-us/copilot/security/security-copilot-inclusion · https://learn.microsoft.com/en-us/defender-xdr/automatic-attack-disruption

### 3.12 Prepararse para la escala y la próxima disrupción: exposición, resiliencia y poscuántica

Según el Microsoft Digital Defense Report 2026, la mediana hasta la explotación de una vulnerabilidad es menor a 24 horas frente a 30–60 días de remediación: hay que gestionar la exposición y medir el tiempo de mitigación. La guía contra el ransomware propone prepararse para recuperar sin pagar; Quick Machine Recovery mejora la recuperación de dispositivos; y el Quantum Safe Program fija criptografía poscuántica en productos y servicios críticos para 2029.

*Dónde se aplica:* A06.2, A06.7, A09.2, A09.7, A05.7. *Fuentes:* https://www.microsoft.com/en-us/security/security-insider/threat-landscape/2026-digital-defense-report · https://learn.microsoft.com/en-us/security/ransomware/human-operated-ransomware · https://www.microsoft.com/en-us/security/blog/2026/06/30/microsoft-advances-quantum-safe-security-as-the-risk-timeline-shifts/

## 4. Parte A — Las 99 preguntas que todo CISO tiene que hacer

La Parte A recorre la agenda completa del CISO moderno: gobierno, riesgo, arquitectura, identidad, datos, exposición, terceros, operaciones, resiliencia, cumplimiento y personas. Es la base sobre la que se apoya la Parte B: ninguna estrategia de IA segura compensa fundamentos débiles.

### A01 — Mandato, gobierno y directorio

*Quién manda, quién decide y cómo rinde cuentas la organización por el riesgo cibernético.*

#### A01.1 · ¿Qué resultados de negocio protege el programa de seguridad y dónde está escrito ese mandato?

- **Por qué importa:** Sin un mandato explícito, la seguridad se mide por actividad (alertas, herramientas, proyectos) y no por la continuidad de los resultados que el negocio necesita.
- **Buena práctica (evidencia esperada):** Existe una carta de la función de seguridad aprobada por el comité ejecutivo, con objetivos vinculados a funciones críticas y a la estrategia corporativa, revisada al menos una vez al año.
- **Postura de Microsoft:** Microsoft recomienda partir de escenarios de negocio y resultados deseados, no de productos (CISO Workshop, Zero Trust Adoption Framework, SAF). En su Secure Future Initiative (SFI) declaró la seguridad como prioridad por encima de cualquier otra cuando hay que elegir.
- **Capacidades Microsoft:** CISO Workshop; Zero Trust Adoption Framework; Security Adoption Framework (SAF); Secure Future Initiative
- **Cruce de marcos:** NIST — CSF GV.OC · GV.RM | CIS — sin referencia directa | The Open Group — TOGAF ADM Preliminar · Fase A | ISACA — COBIT EDM01 · APO02 | CSA — CCM GRC | MCSB — GS
- **Anclaje y COE:** Atlas — ORGANIZATION / Gobernar | TheNextCISO — CISO-OS (gobierno) | SAF — Estrategia, integración y gobierno | COE — Gobierno, políticas y decisiones | Responsable sugerido — CEO + CISO | Ola 0 (0–30 días) | relevante para el directorio

#### A01.2 · ¿A quién reporta el CISO, qué independencia real tiene respecto de TI, con qué modelo operativo funciona la seguridad (central, federado, BISO, servicios gestionados) y cómo se resuelven los conflictos entre velocidad y control?

- **Por qué importa:** Cuando la seguridad depende de quien optimiza plazos y costos de TI, los riesgos se subestiman o se escalan tarde; un modelo operativo implícito produce, además, duplicaciones, vacíos de responsabilidad y dependencia de personas clave.
- **Buena práctica (evidencia esperada):** Línea de reporte, acceso directo al CEO y al comité de auditoría y mecanismo de escalamiento formalizados; modelo operativo documentado con roles, RACI por proceso y acuerdos de servicio con proveedores gestionados; foro periódico de coordinación con riesgo, privacidad, legal y negocio; desacuerdos relevantes registrados con su resolución.
- **Postura de Microsoft:** En la Secure Future Initiative (SFI), Microsoft creó en 2024 un Cybersecurity Governance Council integrado por Deputy CISOs que, bajo el liderazgo del CISO, responden por el riesgo, la defensa y el cumplimiento de sus áreas: la responsabilidad se distribuye, pero converge en un único punto de gobierno. SAF propone un mapa de responsabilidades de seguridad para toda la organización y se apoya en un borrador de estándar de roles de seguridad de The Open Group.
- **Capacidades Microsoft:** Secure Future Initiative (modelo de gobierno); SAF (roles y responsabilidades); CISO Workshop
- **Cruce de marcos:** NIST — CSF GV.RR · GV.OV | CIS — sin referencia directa | The Open Group — TOGAF Gobierno de arquitectura · TOGAF Capacidad de arquitectura · Roles de seguridad (borrador citado por SAF) | ISACA — COBIT EDM01 · APO01 · APO08 | CSA — CCM GRC · HRS | MCSB — GS
- **Versión 2.0:** Integra la antigua A01.9 (fusión dentro del dominio).
- **Anclaje y COE:** Atlas — ORGANIZATION / Gobernar | TheNextCISO — CISO-OS (gobierno) | SAF — Estrategia, integración y gobierno | COE — Gobierno, políticas y decisiones | Responsable sugerido — CEO / Directorio | Ola 0 (0–30 días) | relevante para el directorio

#### A01.3 · ¿Qué decisiones de riesgo puede tomar el CISO por sí mismo, cuáles corresponden al comité ejecutivo y cuáles al directorio?

- **Por qué importa:** Sin derechos de decisión explícitos, los riesgos se aceptan por omisión o se escalan todos; ninguna de las dos cosas es gobierno.
- **Buena práctica (evidencia esperada):** Hay una matriz de derechos de decisión por umbral de impacto; cada aceptación de riesgo identifica autoridad competente, alcance, condiciones y vigencia (registro tipo CDRR del AI CISO Atlas).
- **Postura de Microsoft:** En el modelo de responsabilidades de SAF, el directorio supervisa la gestión del riesgo de seguridad y el CEO toma la decisión final en situaciones de alta consecuencia; la seguridad es un deporte de equipo, no un problema exclusivo del equipo de seguridad.
- **Capacidades Microsoft:** SAF (responsabilidades de seguridad en toda la organización)
- **Cruce de marcos:** NIST — CSF GV.RR · GV.RM | CIS — CIS RAM v2.2 | The Open Group — Open FAIR O-RA · TOGAF Gobierno de arquitectura | ISACA — COBIT EDM03 · APO12 · Risk IT | CSA — CCM GRC | MCSB — GS
- **Anclaje y COE:** Atlas — RISK / Gobernar | TheNextCISO — CISO-OS (gobierno) | SAF — Estrategia, integración y gobierno | COE — Gobierno, políticas y decisiones | Responsable sugerido — CISO + CRO | Ola 0 (0–30 días) | relevante para el directorio | pregunta prioritaria para el directorio

#### A01.4 · ¿Con qué frecuencia, formato y métricas supervisa el directorio el riesgo cibernético, y qué decisiones concretas tomó en los últimos doce meses?

- **Por qué importa:** Un directorio que solo recibe informes técnicos no ejerce supervisión; uno que no decide nada no está gobernando el riesgo.
- **Buena práctica (evidencia esperada):** Calendario anual de supervisión, tablero con pocos indicadores de riesgo en lenguaje de negocio, actas con decisiones y seguimiento, y al menos una sesión de formación o ejercicio al año.
- **Postura de Microsoft:** Microsoft recomienda contextualizar el riesgo ante la dirección con tendencias de amenazas como las del Microsoft Digital Defense Report (edición 2026, publicada el 1 de octubre de 2026) y medir la resiliencia como capacidad de sostener resultados de negocio.
- **Capacidades Microsoft:** Microsoft Digital Defense Report; CISO Workshop
- **Cruce de marcos:** NIST — CSF GV.OV · GV.RR | CIS — sin referencia directa | The Open Group — Open FAIR O-RA (comunicación cuantitativa) | ISACA — COBIT EDM05 · MEA01 | CSA — CCM GRC | MCSB — GS
- **Anclaje y COE:** Atlas — TRUST / Gobernar | TheNextCISO — CISO-OS (gobierno) | SAF — Estrategia, integración y gobierno | COE — Valor, métricas y comunicación ejecutiva | Responsable sugerido — Directorio + CISO | Ola 1 (30–90 días) | relevante para el directorio | pregunta prioritaria para el directorio

#### A01.5 · ¿Nuestras políticas de seguridad son pocas, vigentes, comprensibles y verificables, y cómo detectamos su incumplimiento?

- **Por qué importa:** Las políticas extensas y desactualizadas generan cumplimiento formal sin protección real.
- **Buena práctica (evidencia esperada):** Jerarquía clara (política, estándar, guía), revisión anual, dueño por documento, controles que verifican técnicamente cada requisito obligatorio y un indicador de desvíos.
- **Postura de Microsoft:** Microsoft promueve políticas expresadas como configuración verificable: seguro por defecto (SFI), Baseline Security Mode en Microsoft 365, Azure Policy y Microsoft Cloud Security Benchmark para medir desvíos de forma continua.
- **Capacidades Microsoft:** Baseline Security Mode; Azure Policy; Microsoft Cloud Security Benchmark; Microsoft Purview Compliance Manager
- **Cruce de marcos:** NIST — CSF GV.PO | CIS — CIS v8.1 (salvaguardas de la función Govern) | The Open Group — Security Principles for Architecture · O-ESA (marco de políticas) | ISACA — COBIT APO01 · MEA02 | CSA — CCM GRC | MCSB — GS
- **Anclaje y COE:** Atlas — ORGANIZATION / Gobernar | TheNextCISO — CISO-OS (gobierno) | SAF — Estrategia, integración y gobierno | COE — Gobierno, políticas y decisiones | Responsable sugerido — CISO | Ola 1 (30–90 días)

#### A01.6 · ¿Cómo se integra la seguridad en las decisiones de inversión, compras y portafolio, y qué ocurre cuando un proyecto no cumple los requisitos?

- **Por qué importa:** Incorporar la seguridad al final multiplica los costos y genera excepciones permanentes.
- **Buena práctica (evidencia esperada):** Requisitos de seguridad en las puertas de aprobación de proyectos y compras, criterios de bloqueo explícitos y excepciones con vencimiento.
- **Postura de Microsoft:** Seguro por diseño es el primer principio de SFI: la seguridad se incorpora desde la concepción del producto o servicio. SAF recomienda integrar la seguridad en todos los procesos de negocio y tecnología.
- **Capacidades Microsoft:** Secure Future Initiative; Security Development Lifecycle (SDL); SAF
- **Cruce de marcos:** NIST — CSF GV.RM · GV.SC | CIS — CIS 15 · CIS 16 | The Open Group — TOGAF Fases E–G · G152 | ISACA — COBIT APO05 · BAI01 · BAI02 · BAI11 | CSA — CCM GRC · STA | MCSB — GS
- **Anclaje y COE:** Atlas — ORGANIZATION / Limitar | TheNextCISO — CISO-OS (gobierno) | SAF — Estrategia, integración y gobierno | COE — Gobierno, políticas y decisiones | Responsable sugerido — CIO + CISO | Ola 1 (30–90 días)

#### A01.7 · ¿Cómo justificamos el presupuesto de seguridad por reducción de exposición y cómo evitamos la proliferación de herramientas superpuestas?

- **Por qué importa:** Sumar herramientas sin integración aumenta costos y puntos ciegos; la fragmentación es en sí misma un riesgo operativo.
- **Buena práctica (evidencia esperada):** Presupuesto vinculado a escenarios de riesgo priorizados, inventario de herramientas con solapamientos identificados y un plan de racionalización con indicadores de cobertura.
- **Postura de Microsoft:** Microsoft propone una plataforma integrada (identidad, endpoint, correo, nube, datos, SIEM y XDR) que comparte señales y reduce traspasos manuales, y recomienda medir el valor por resultados y no por cantidad de herramientas.
- **Capacidades Microsoft:** Microsoft Defender XDR; Microsoft Sentinel; Microsoft Purview; Microsoft Entra; Microsoft Security Exposure Management
- **Cruce de marcos:** NIST — CSF GV.RM · ID.IM | CIS — sin referencia directa | The Open Group — TOGAF Fase E | ISACA — COBIT APO06 · EDM04 | CSA — CCM GRC | MCSB — GS
- **Anclaje y COE:** Atlas — RISK / Gobernar | TheNextCISO — CISO-OS (gobierno) | SAF — Arquitectura de seguridad de extremo a extremo | COE — Valor, métricas y comunicación ejecutiva | Responsable sugerido — CISO + CFO | Ola 1 (30–90 días) | relevante para el directorio

#### A01.8 · ¿Cómo rinde cuentas la alta dirección por los objetivos de seguridad (metas, incentivos, evaluación de desempeño)?

- **Por qué importa:** Lo que no forma parte de la evaluación de los líderes compite en desventaja con las metas de ingresos y plazos.
- **Buena práctica (evidencia esperada):** Objetivos de seguridad en las metas de los ejecutivos de negocio y tecnología, con indicadores verificables y revisión anual.
- **Postura de Microsoft:** En SFI, Microsoft vinculó desde 2024 la compensación de su equipo de liderazgo sénior al desempeño en seguridad e incorporó la seguridad como prioridad central en la evaluación de desempeño de todos sus empleados.
- **Capacidades Microsoft:** Secure Future Initiative
- **Cruce de marcos:** NIST — CSF GV.RR · GV.OV | CIS — sin referencia directa | The Open Group — O-ESA (gobierno de seguridad) | ISACA — COBIT EDM01 · APO07 | CSA — CCM GRC · HRS | MCSB — GS
- **Anclaje y COE:** Atlas — ORGANIZATION / Gobernar | TheNextCISO — CISO-OS (gobierno) | SAF — Estrategia, integración y gobierno | COE — Gobierno, políticas y decisiones | Responsable sugerido — CEO + RR. HH. | Ola 2 (90–180 días) | relevante para el directorio | pregunta prioritaria para el directorio

#### A01.9 · Antes de reducir la dotación o el presupuesto de seguridad, ¿se evalúa y documenta el impacto en el riesgo, y quién acepta formalmente el riesgo residual?

- **Por qué importa:** Un recorte sin análisis convierte una decisión financiera en una aceptación de riesgo implícita, que nadie firmó y que reaparece después del primer incidente grave.
- **Buena práctica (evidencia esperada):** Análisis del impacto de cada recorte sobre capacidades, escenarios y tiempos de respuesta; aceptación formal del riesgo residual por la autoridad que corresponde según la matriz de derechos de decisión (A01.3); seguimiento posterior de los indicadores afectados.
- **Postura de Microsoft:** Silencio: Microsoft no publica una postura sobre cómo evaluar recortes de dotación o de presupuesto de seguridad. Lo más cercano son dos prácticas: en SFI vinculó la compensación de su liderazgo sénior al desempeño en seguridad, y Security Exposure Management mide la exposición con puntajes por iniciativa y genera eventos cuando un puntaje cae, lo que permite comparar la postura antes y después de una reducción.
- **Capacidades Microsoft:** Microsoft Security Exposure Management (iniciativas y eventos de caída de puntaje); Microsoft Secure Score
- **Cruce de marcos:** NIST — CSF GV.RR · GV.RM | CIS — sin referencia directa | The Open Group — Open FAIR O-RA | ISACA — COBIT EDM04 · APO06 · APO07 | CSA — CCM GRC · HRS | MCSB — GS
- **Versión 2.0:** Pregunta nueva (proceso inverso, pareja IC05). El contenido de la antigua A01.9 se integró en A01.2.
- **Anclaje y COE:** Atlas — RISK / Gobernar | TheNextCISO — CISO-OS (gobierno) | SAF — Estrategia, integración y gobierno | COE — Gobierno, políticas y decisiones | Responsable sugerido — CFO + CISO + CRO | Ola 1 (30–90 días) | relevante para el directorio

### A02 — Riesgo, apetito, cuantificación y valor

*Cómo se expresa, cuantifica, acepta y comunica el riesgo en el idioma en que decide el negocio.*

#### A02.1 · ¿Cuál es nuestro apetito y tolerancia de riesgo cibernético expresado en términos de negocio, y quién lo aprobó?

- **Por qué importa:** Sin un apetito explícito no hay criterio para priorizar inversiones ni para aceptar riesgos residuales.
- **Buena práctica (evidencia esperada):** Declaración de apetito aprobada por el directorio, con tolerancias por función crítica (por ejemplo, horas de interrupción o volumen de registros expuestos) y revisión anual.
- **Postura de Microsoft:** Microsoft recomienda tratar la seguridad como un riesgo de negocio integrado a la gestión de riesgo empresarial, con decisiones explícitas de la dirección (CISO Workshop, SAF).
- **Capacidades Microsoft:** CISO Workshop; SAF
- **Cruce de marcos:** NIST — CSF GV.RM · IR 8286 Rev. 1 | CIS — CIS RAM v2.2 | The Open Group — Open FAIR O-RA | ISACA — COBIT EDM03 · APO12 · Risk IT | CSA — CCM GRC | MCSB — GS
- **Anclaje y COE:** Atlas — RISK / Gobernar | TheNextCISO — CISO-OS (gobierno) | SAF — Estrategia, integración y gobierno | COE — Riesgo, cumplimiento y aseguramiento | Responsable sugerido — Directorio + CRO | Ola 0 (0–30 días) | relevante para el directorio | pregunta prioritaria para el directorio

#### A02.2 · ¿Cuáles son nuestras joyas de la corona (procesos, datos, sistemas e identidades) y qué escenarios de pérdida material las amenazan, según los adversarios relevantes para nuestro sector y país?

- **Por qué importa:** Proteger todo por igual diluye recursos, y un modelo de amenazas genérico lleva a defenderse de lo más mediático y no de lo más probable: los atacantes buscan los activos que producen mayor impacto.
- **Buena práctica (evidencia esperada):** Catálogo de activos críticos con dueño de negocio, dependencias y escenarios de pérdida documentados; perfil de amenazas sectorial y regional revisado cada trimestre que alimenta esos escenarios, la detección, las pruebas y el presupuesto; actualización tras cada cambio relevante.
- **Postura de Microsoft:** Proteger los datos sensibles del negocio es uno de los cinco escenarios de negocio del Zero Trust Adoption Framework; Security Exposure Management permite clasificar activos críticos y analizar las rutas de ataque hacia ellos. Microsoft recomienda una inteligencia de amenazas basada en comportamiento, infraestructura e identidad, no solo en nombres de grupos, y la publica en Microsoft Threat Intelligence y en el Microsoft Digital Defense Report.
- **Capacidades Microsoft:** Microsoft Security Exposure Management (activos críticos y rutas de ataque); Microsoft Purview; inteligencia de amenazas en Microsoft Defender XDR
- **Cruce de marcos:** NIST — CSF ID.AM · ID.RA | CIS — CIS 1 · CIS 3 | The Open Group — TOGAF Fase B · Open FAIR O-RT (frecuencia de eventos de amenaza) | ISACA — COBIT APO12 · BAI09 | CSA — CCM DSP · GRC · TVM | MCSB — AM · LT
- **Versión 2.0:** Integra la antigua A02.8 (fusión dentro del dominio).
- **Anclaje y COE:** Atlas — RISK / Anticipar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Gestión de la postura de seguridad | COE — Riesgo, cumplimiento y aseguramiento | Responsable sugerido — Dueños de negocio + CISO + inteligencia de amenazas | Ola 0 (0–30 días) | relevante para el directorio | pregunta prioritaria para el directorio

#### A02.3 · ¿Cuantificamos el riesgo con rangos y supuestos explícitos, o con matrices de colores que no permiten comparar inversiones?

- **Por qué importa:** Las matrices cualitativas ocultan la incertidumbre y no traducen el riesgo a la moneda en la que decide el negocio.
- **Buena práctica (evidencia esperada):** Análisis cuantitativo de los escenarios principales (frecuencia y magnitud de pérdida en rangos), con supuestos documentados, análisis de sensibilidad y sin falsa precisión.
- **Postura de Microsoft:** SAF recomienda estimar la pérdida de un incidente con Open FAIR o un método similar para priorizar controles e inversiones.
- **Capacidades Microsoft:** SAF (priorización de controles)
- **Cruce de marcos:** NIST — IR 8286 Rev. 1 · CSF GV.RM · ID.RA | CIS — CIS RAM v2.2 | The Open Group — Open FAIR O-RT · O-RA | ISACA — COBIT APO12 · Risk IT | CSA — CCM GRC | MCSB — GS
- **Anclaje y COE:** Atlas — RISK / Anticipar | TheNextCISO — CISO-MM (madurez) | SAF — Estrategia, integración y gobierno | COE — Riesgo, cumplimiento y aseguramiento | Responsable sugerido — CRO + CISO | Ola 2 (90–180 días)

#### A02.4 · ¿Cómo se integra el riesgo cibernético al registro de riesgos empresariales y con qué frecuencia se actualiza?

- **Por qué importa:** Si el riesgo cibernético vive en un registro aparte, compite mal por recursos y se desconecta de los riesgos operativos y financieros que provoca.
- **Buena práctica (evidencia esperada):** Riesgos cibernéticos expresados como riesgos de negocio en el registro corporativo, con dueño, tratamiento y actualización al menos trimestral.
- **Postura de Microsoft:** SAF aborda la integración con el riesgo empresarial y el negocio como parte de la estrategia, integración y gobierno: un proceso estructurado que reúne a dirección, riesgo, seguridad, tecnología y cumplimiento.
- **Capacidades Microsoft:** SAF; Microsoft Purview Compliance Manager
- **Cruce de marcos:** NIST — IR 8286 Rev. 1 · CSF GV.RM | CIS — CIS RAM v2.2 | The Open Group — Open FAIR O-RA | ISACA — COBIT EDM03 · APO12 · Risk IT | CSA — CCM GRC | MCSB — GS
- **Anclaje y COE:** Atlas — RISK / Gobernar | TheNextCISO — CISO-OS (gobierno) | SAF — Estrategia, integración y gobierno | COE — Riesgo, cumplimiento y aseguramiento | Responsable sugerido — CRO | Ola 1 (30–90 días)

#### A02.5 · ¿Cada aceptación de riesgo tiene dueño, alcance, evidencia, vencimiento y disparadores de revisión, y cada transferencia (seguros, contratos) cubre los escenarios reales con controles que podemos demostrar?

- **Por qué importa:** Las aceptaciones sin vencimiento se convierten en exenciones permanentes que nadie revisa, y una póliza que no cubre el escenario real, o que exige controles no implementados, da una falsa sensación de seguridad.
- **Buena práctica (evidencia esperada):** Registro de aceptaciones con autoridad competente, condiciones, controles compensatorios, vigencia máxima y disparadores (nueva amenaza, incidente, auditoría); pólizas revisadas contra los escenarios principales, exclusiones conocidas por el directorio y evidencia de los controles exigidos disponible antes de cada renovación.
- **Postura de Microsoft:** Las herramientas de Microsoft aplican este principio: las exenciones de recomendaciones en Defender for Cloud y las excepciones en Defender Vulnerability Management se registran con justificación y fecha de vencimiento. Microsoft no publica una postura sobre seguros cibernéticos; la evidencia de controles (Secure Score, Compliance Manager, Exposure Management) puede respaldar la negociación con la aseguradora.
- **Capacidades Microsoft:** Microsoft Defender for Cloud (exenciones); Microsoft Defender Vulnerability Management (excepciones); Microsoft Secure Score; Microsoft Purview Compliance Manager
- **Cruce de marcos:** NIST — CSF GV.RM · ID.RA | CIS — CIS RAM v2.2 | The Open Group — Open FAIR O-RA | ISACA — COBIT APO12 · APO10 | CSA — CCM GRC | MCSB — GS
- **Versión 2.0:** Integra la antigua A02.9 (fusión dentro del dominio).
- **Anclaje y COE:** Atlas — RISK / Gobernar | TheNextCISO — CISO-OS (gobierno) | SAF — Estrategia, integración y gobierno | COE — Riesgo, cumplimiento y aseguramiento | Responsable sugerido — CRO + CISO + CFO | Ola 1 (30–90 días) | relevante para el directorio

#### A02.6 · ¿Qué indicadores anticipan una pérdida material y cuáles se reportan al directorio?

- **Por qué importa:** Los indicadores de actividad (alertas, parches aplicados) no anticipan pérdidas; los de exposición sí.
- **Buena práctica (evidencia esperada):** Un conjunto reducido de indicadores de riesgo con umbrales y responsables: tiempo de exposición de activos críticos, rutas de ataque abiertas, cobertura de MFA resistente al phishing y tiempo de recuperación probado.
- **Postura de Microsoft:** El Microsoft Digital Defense Report 2026 recomienda pasar a la gestión de la exposición y medir el tiempo de mitigación, porque la mediana entre la divulgación de una vulnerabilidad y su explotación ya es menor a 24 horas, frente a 30–60 días de remediación típica.
- **Capacidades Microsoft:** Microsoft Security Exposure Management (iniciativas y métricas); Microsoft Secure Score
- **Cruce de marcos:** NIST — CSF GV.OV · ID.IM | CIS — CIS 7 | The Open Group — Open FAIR O-RT | ISACA — COBIT MEA01 · APO12 | CSA — CCM GRC | MCSB — PV
- **Anclaje y COE:** Atlas — RISK / Anticipar | TheNextCISO — CISO-MM (madurez) | SAF — Gestión de la postura de seguridad | COE — Valor, métricas y comunicación ejecutiva | Responsable sugerido — CISO | Ola 1 (30–90 días) | relevante para el directorio | pregunta prioritaria para el directorio

#### A02.7 · ¿Cómo demostramos el valor de la seguridad: pérdidas evitadas, exposición reducida y nuevas iniciativas de negocio habilitadas?

- **Por qué importa:** Si la seguridad solo se presenta como costo, cada presupuesto se negocia a la baja.
- **Buena práctica (evidencia esperada):** Caso de valor con hipótesis y evidencia: reducción de exposición, tiempos de respuesta, ahorro por consolidación y proyectos de negocio habilitados con seguridad.
- **Postura de Microsoft:** Microsoft define el éxito de la seguridad como el fracaso del atacante: aumentar su costo y fricción y reducir su tiempo de permanencia. SAF incluye la habilitación del negocio y la fricción para el usuario entre las métricas de excelencia operativa.
- **Capacidades Microsoft:** SAF (excelencia operativa); Microsoft Secure Score; Microsoft Security Exposure Management
- **Cruce de marcos:** NIST — CSF GV.OV · ID.IM | CIS — sin referencia directa | The Open Group — Open FAIR O-RA (valor como reducción de pérdida) | ISACA — COBIT EDM02 · MEA01 | CSA — CCM GRC | MCSB — GS
- **Anclaje y COE:** Atlas — SELF / Gobernar | TheNextCISO — CISO-NX (nueva generación) | SAF — Estrategia, integración y gobierno | COE — Valor, métricas y comunicación ejecutiva | Responsable sugerido — CISO + CFO | Ola 2 (90–180 días) | relevante para el directorio

#### A02.8 · ¿Nuestro análisis de riesgo considera el daño que podemos causar a terceros (clientes, ciudadanos, socios) y verifica que las salvaguardas no sean más gravosas que el riesgo que mitigan?

- **Por qué importa:** Un riesgo aceptable para la organización puede no serlo para quienes sufrirían el daño; supervisores y tribunales evalúan si la decisión fue razonable para todas las partes, y un control desproporcionado también tiene un costo.
- **Buena práctica (evidencia esperada):** Criterios de aceptación que incluyen el impacto en terceros y el deber de cuidado; análisis de proporcionalidad entre la carga de cada salvaguarda y el riesgo que reduce; decisiones registradas con su fundamento (método CIS RAM, basado en el estándar DoCRA).
- **Postura de Microsoft:** Silencio parcial: Microsoft no publica un método para ponderar el daño a terceros en el análisis de riesgo cibernético. Para la IA sí lo exige: su Responsible AI Standard v2 pide evaluar el impacto de cada sistema en personas, organizaciones y la sociedad antes de desarrollarlo, identificando partes interesadas y daños potenciales, y revisar esa evaluación al menos una vez al año.
- **Capacidades Microsoft:** Responsible AI Standard v2 (evaluación de impacto)
- **Cruce de marcos:** NIST — CSF GV.OC · GV.RM · ID.RA | CIS — CIS RAM v2.2 | The Open Group — Open FAIR O-RT (pérdida secundaria) | ISACA — COBIT EDM03 · EDM05 · APO12 | CSA — CCM GRC · DSP | MCSB — GS
- **Versión 2.0:** Pregunta nueva (proceso inverso, pareja CI05). El contenido de la antigua A02.8 se integró en A02.2.
- **Anclaje y COE:** Atlas — RISK / Gobernar | TheNextCISO — CISO-OS (gobierno) | SAF — Estrategia, integración y gobierno | COE — Riesgo, cumplimiento y aseguramiento | Responsable sugerido — CRO + Legal + CISO | Ola 2 (90–180 días) | relevante para el directorio

#### A02.9 · ¿Qué precisión necesita cada decisión de riesgo, y estamos invirtiendo esfuerzo de análisis que no cambiaría ninguna decisión?

- **Por qué importa:** La precisión tiene costo: perseguir cifras exactas demora decisiones, y una estimación útilmente precisa, con rangos honestos, suele bastar para elegir entre opciones.
- **Buena práctica (evidencia esperada):** Criterio de suficiencia definido por tipo de decisión; análisis de sensibilidad que muestra qué supuestos cambiarían la elección; descomposición del análisis solo hasta el nivel que el decisor o el control requieren (Open FAIR O-RA).
- **Postura de Microsoft:** Silencio: Microsoft no publica una postura sobre la precisión necesaria en la cuantificación del riesgo. SAF recomienda estimar la pérdida con Open FAIR o un método similar (A02.3), y Security Exposure Management aporta puntajes por iniciativa con metas configurables: insumos medibles, no una cuantificación financiera.
- **Capacidades Microsoft:** Microsoft Security Exposure Management (iniciativas y metas); Microsoft Secure Score
- **Cruce de marcos:** NIST — CSF GV.RM · ID.RA · IR 8286 | CIS — sin referencia directa | The Open Group — Open FAIR O-RA | ISACA — COBIT APO12 · Risk IT | CSA — CCM GRC | MCSB — GS
- **Versión 2.0:** Pregunta nueva (proceso inverso, pareja OG07). El contenido de la antigua A02.9 se integró en A02.5.
- **Anclaje y COE:** Atlas — RISK / Anticipar | TheNextCISO — CISO-MM (madurez) | SAF — Estrategia, integración y gobierno | COE — Riesgo, cumplimiento y aseguramiento | Responsable sugerido — CRO + CISO | Ola 2 (90–180 días)

### A03 — Arquitectura, estrategia técnica y Zero Trust

*Qué arquitectura y qué principios hacen que la seguridad sea una propiedad del diseño y no un agregado.*

#### A03.1 · ¿Tenemos una arquitectura de referencia de seguridad de extremo a extremo, conectada a la arquitectura empresarial y gobernada en cada cambio relevante?

- **Por qué importa:** Sin arquitectura de referencia, cada proyecto resuelve la seguridad a su manera y la deuda técnica crece.
- **Buena práctica (evidencia esperada):** Arquitectura de referencia vigente, principios obligatorios, revisión de arquitectura en los proyectos relevantes y decisiones registradas.
- **Postura de Microsoft:** Microsoft publica las Microsoft Cybersecurity Reference Architectures (MCRA) y, en SAF, trata la arquitectura de seguridad de extremo a extremo como la disciplina que coordina a todas las demás.
- **Capacidades Microsoft:** Microsoft Cybersecurity Reference Architectures (MCRA); SAF; Well-Architected Framework (pilar de seguridad)
- **Cruce de marcos:** NIST — CSF GV.PO · PR.PS · SP 800-207 | CIS — sin referencia directa | The Open Group — TOGAF ADM Fases A–D · G152 · Gobierno de arquitectura | ISACA — COBIT APO03 · BAI03 | CSA — CCM AIS · IVS | MCSB — GS
- **Anclaje y COE:** Atlas — TECHNOLOGY / Limitar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Arquitectura de seguridad de extremo a extremo | COE — Arquitectura y patrones seguros | Responsable sugerido — Arquitecto de seguridad | Ola 1 (30–90 días)

#### A03.2 · ¿Cuál es nuestra estrategia Zero Trust, qué escenarios de negocio prioriza y cómo medimos su avance?

- **Por qué importa:** Zero Trust sin escenarios ni métricas se convierte en un rótulo para proyectos sueltos.
- **Buena práctica (evidencia esperada):** Estrategia con escenarios priorizados, perfil actual y objetivo, iniciativas secuenciadas y métricas trimestrales.
- **Postura de Microsoft:** Microsoft organiza Zero Trust en cinco escenarios de negocio (Zero Trust Adoption Framework) y en guías de despliegue por pilar tecnológico (la antigua página de RaMP hoy redirige a ellas), sobre tres principios: verificar explícitamente, usar mínimo privilegio y asumir compromiso. Zero Trust Assessment prueba cientos de configuraciones alineadas con SFI.
- **Capacidades Microsoft:** Zero Trust Adoption Framework; Zero Trust Workshop; Zero Trust Assessment; guías de despliegue de Zero Trust por pilar
- **Cruce de marcos:** NIST — SP 800-207 · SP 1800-35 · CSF PR.AA · PR.IR | CIS — CIS 6 · CIS 12 | The Open Group — Zero Trust Commandments · ZT Reference Model (snapshot) | ISACA — COBIT APO02 · APO03 · APO13 | CSA — CCM IAM · IVS | MCSB — GS
- **Anclaje y COE:** Atlas — TECHNOLOGY / Limitar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Arquitectura de seguridad de extremo a extremo | COE — Arquitectura y patrones seguros | Responsable sugerido — CISO + Arquitectura | Ola 0 (0–30 días)

#### A03.3 · ¿Qué principios de seguridad son obligatorios en el diseño (mínimo privilegio, segmentación, asumir compromiso, seguro por defecto) y quién verifica su cumplimiento?

- **Por qué importa:** Los principios que no se verifican no cambian las decisiones de diseño.
- **Buena práctica (evidencia esperada):** Principios publicados con criterios verificables, revisión en las puertas de diseño y métricas de excepciones.
- **Postura de Microsoft:** SFI se apoya en tres principios: seguro por diseño, seguro por defecto y seguro en las operaciones. Microsoft los aplica a su ingeniería y los traduce en patrones y prácticas reutilizables para sus clientes.
- **Capacidades Microsoft:** Secure Future Initiative (patrones y prácticas)
- **Cruce de marcos:** NIST — CSF GV.PO · PR.PS · SP 800-218 | CIS — CIS 4 · CIS 16 | The Open Group — Security Principles for Architecture · TOGAF Principios de arquitectura | ISACA — COBIT APO03 · BAI03 | CSA — CCM AIS · CCC | MCSB — GS
- **Anclaje y COE:** Atlas — TECHNOLOGY / Limitar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Arquitectura de seguridad de extremo a extremo | COE — Arquitectura y patrones seguros | Responsable sugerido — Arquitecto de seguridad | Ola 1 (30–90 días)

#### A03.4 · ¿Cómo segmentamos redes, entornos y planos de administración para limitar el movimiento lateral?

- **Por qué importa:** Una red plana convierte cualquier intrusión inicial en un compromiso total.
- **Buena práctica (evidencia esperada):** Segmentación basada en riesgo, administración desde planos aislados, reglas mínimas y pruebas periódicas de movimiento lateral.
- **Postura de Microsoft:** El enterprise access model de Microsoft separa los planos de control, gestión y datos o cargas de trabajo, como evolución del modelo de niveles de Active Directory; se complementa con zonas de aterrizaje de Azure y acceso privado basado en identidad.
- **Capacidades Microsoft:** Enterprise access model; Azure landing zones; Microsoft Entra Private Access; Azure Firewall
- **Cruce de marcos:** NIST — CSF PR.IR · PR.AA · SP 800-207 | CIS — CIS 12 · CIS 13 | The Open Group — Zero Trust Commandments | ISACA — COBIT DSS05 | CSA — CCM IVS | MCSB — NS · PA
- **Anclaje y COE:** Atlas — TECHNOLOGY / Limitar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Seguridad de infraestructura | COE — Plataforma e ingeniería de controles | Responsable sugerido — Arquitectura + Redes | Ola 1 (30–90 días)

#### A03.5 · ¿Cómo gestionamos la deuda técnica y los sistemas heredados que no pueden actualizarse: aislar, reemplazar o aceptar?

- **Por qué importa:** Los sistemas imposibles de parchear acumulan exposición y suelen ser la puerta de entrada de incidentes graves.
- **Buena práctica (evidencia esperada):** Inventario de sistemas heredados con el costo de no actuar, plan de aislamiento o reemplazo y aceptaciones con vencimiento.
- **Postura de Microsoft:** SAF recomienda evaluar la deuda técnica comparando el costo de no actuar (incidentes) con el de aislar o reemplazar los sistemas imposibles de actualizar, una decisión que se vuelve urgente ante el aumento del flujo de vulnerabilidades.
- **Capacidades Microsoft:** SAF; Microsoft Defender Vulnerability Management; Microsoft Security Exposure Management
- **Cruce de marcos:** NIST — CSF ID.RA · PR.PS | CIS — CIS 2 (2.2) · CIS 7 | The Open Group — TOGAF Fase H | ISACA — COBIT BAI09 · APO12 | CSA — CCM TVM · CCC | MCSB — PV · AM
- **Anclaje y COE:** Atlas — TECHNOLOGY / Limitar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Gestión de la postura de seguridad | COE — Arquitectura y patrones seguros | Responsable sugerido — CIO + CISO | Ola 2 (90–180 días) | relevante para el directorio

#### A03.6 · ¿Cómo protegemos el acceso de personas que trabajan desde cualquier lugar sin depender del perímetro de red?

- **Por qué importa:** El perímetro tradicional ya no coincide con el lugar donde están los usuarios, los datos y las aplicaciones.
- **Buena práctica (evidencia esperada):** Acceso condicional basado en identidad, dispositivo y riesgo; acceso privado a aplicaciones internas; inspección del tráfico a internet según política.
- **Postura de Microsoft:** El trabajo híbrido seguro es uno de los cinco escenarios de negocio de Zero Trust de Microsoft; combina acceso condicional con Security Service Edge (Microsoft Entra Internet Access y Private Access, parte de Microsoft Entra Suite, disponible de forma general desde julio de 2024).
- **Capacidades Microsoft:** Microsoft Entra Conditional Access; Microsoft Entra Suite (Internet Access, Private Access); Microsoft Intune
- **Cruce de marcos:** NIST — CSF PR.AA · PR.IR · SP 800-207 | CIS — CIS 6 · CIS 12 · CIS 13 | The Open Group — Zero Trust Commandments | ISACA — COBIT DSS05 | CSA — CCM IAM · IVS | MCSB — IM · NS
- **Anclaje y COE:** Atlas — TECHNOLOGY / Limitar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Acceso e identidad | COE — Plataforma e ingeniería de controles | Responsable sugerido — Arquitectura + IAM | Ola 1 (30–90 días)

#### A03.7 · ¿Cuánto valor perdemos por la fragmentación de herramientas y datos de seguridad, y cuál es la arquitectura objetivo de la plataforma?

- **Por qué importa:** Cada traspaso manual entre consolas agrega tiempo y errores cuando el atacante opera a velocidad de máquina.
- **Buena práctica (evidencia esperada):** Mapa de herramientas e integraciones, medición de traspasos manuales y una arquitectura objetivo con plan de consolidación.
- **Postura de Microsoft:** Microsoft sostiene que la defensa debe ser continua, integrada y operable a velocidad de máquina, y ofrece una plataforma unificada de operaciones de seguridad que reúne XDR, SIEM, gestión de exposición e IA en un mismo portal.
- **Capacidades Microsoft:** Plataforma unificada de operaciones de seguridad (Defender XDR + Sentinel); Security Exposure Management; Security Copilot
- **Cruce de marcos:** NIST — CSF GV.RM · DE.CM · ID.IM | CIS — CIS 8 (8.9) | The Open Group — TOGAF Fases E–F | ISACA — COBIT APO03 · BAI03 | CSA — CCM LOG | MCSB — LT
- **Anclaje y COE:** Atlas — TECHNOLOGY / Contener | TheNextCISO — CISO-DO (operación de dominios) | SAF — Arquitectura de seguridad de extremo a extremo | COE — Arquitectura y patrones seguros | Responsable sugerido — CISO + Arquitectura | Ola 2 (90–180 días)

#### A03.8 · ¿Cómo protegemos los entornos OT e IoT y la convergencia entre tecnología operativa y TI?

- **Por qué importa:** En industrias críticas, un incidente en OT afecta la seguridad física, la producción y el ambiente, no solo los datos.
- **Buena práctica (evidencia esperada):** Inventario de activos OT/IoT, segmentación entre TI y OT, monitoreo pasivo, accesos remotos controlados y planes de respuesta conjuntos con operaciones.
- **Postura de Microsoft:** SAF incluye la seguridad de OT e IoT como disciplina propia; Microsoft ofrece descubrimiento y monitoreo de activos OT/IoT integrados con el resto de la plataforma de seguridad.
- **Capacidades Microsoft:** Microsoft Defender for IoT; SAF (OT e IoT)
- **Cruce de marcos:** NIST — CSF ID.AM · PR.IR · DE.CM | CIS — CIS 1 · CIS 12 · CIS 13 | The Open Group — sin referencia directa | ISACA — COBIT DSS05 · BAI09 | CSA — CCM IVS · UEM | MCSB — NS · AM
- **Anclaje y COE:** Atlas — TECHNOLOGY / Limitar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Seguridad OT e IoT | COE — Plataforma e ingeniería de controles | Responsable sugerido — CISO + Operaciones industriales | Ola 2 (90–180 días)

#### A03.9 · ¿Tenemos una hoja de ruta de seguridad a 12–36 meses priorizada por riesgo, con dependencias y criterios de éxito revisados cada trimestre?

- **Por qué importa:** Sin hoja de ruta, la agenda la fijan los incidentes y los proveedores.
- **Buena práctica (evidencia esperada):** Hoja de ruta basada en el perfil actual y objetivo, con iniciativas, dueños, dependencias, presupuesto y revisión trimestral.
- **Postura de Microsoft:** Microsoft recomienda planificar la adopción de capacidades por resultados y prioridad de riesgo (SAF y su taller SCAP) y apoyarse en las guías de despliegue de Zero Trust por pilar tecnológico (la página de RaMP hoy redirige a ellas).
- **Capacidades Microsoft:** SAF; Security Capability Adoption Planning (SCAP); guías de despliegue de Zero Trust por pilar
- **Cruce de marcos:** NIST — CSF ID.IM (perfiles actual y objetivo) | CIS — CIS IG1–IG3 | The Open Group — TOGAF Fases E–F | ISACA — COBIT APO02 · APO05 | CSA — CCM GRC | MCSB — GS
- **Anclaje y COE:** Atlas — ORGANIZATION / Gobernar | TheNextCISO — CISO-MM (madurez) | SAF — Estrategia, integración y gobierno | COE — Gobierno, políticas y decisiones | Responsable sugerido — CISO | Ola 1 (30–90 días) | relevante para el directorio

### A04 — Identidad y acceso privilegiado

*La identidad como plano de control: personas, administradores e identidades no humanas.*

#### A04.1 · ¿Qué porcentaje de usuarios, administradores y accesos externos usa autenticación multifactor resistente al phishing, y cuál es la fecha objetivo para el 100%?

- **Por qué importa:** La identidad es el plano de control principal: los atacantes prefieren iniciar sesión antes que forzar la entrada.
- **Buena práctica (evidencia esperada):** Cobertura medida por población (administradores primero), métodos resistentes al phishing (passkeys, FIDO2, Windows Hello para empresas, certificados) y excepciones con vencimiento.
- **Postura de Microsoft:** Microsoft recomienda desplegar ampliamente autenticación sin contraseña resistente al phishing —según el MDDR 2025, bloquea más del 99 % de los ataques de identidad— y aplica MFA obligatoria a todos los usuarios de Azure (portal desde octubre de 2024; CLI, PowerShell, API e infraestructura como código desde octubre de 2025), sin opción de exclusión.
- **Capacidades Microsoft:** Microsoft Entra ID (métodos sin contraseña resistentes al phishing, acceso condicional con fortaleza de autenticación; passkeys sincronizadas en versión preliminar)
- **Cruce de marcos:** NIST — CSF PR.AA | CIS — CIS 6 (6.3–6.5) | The Open Group — Zero Trust Commandments | ISACA — COBIT DSS05 | CSA — CCM IAM | MCSB — IM
- **Anclaje y COE:** Atlas — TECHNOLOGY / Limitar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Acceso e identidad | COE — Plataforma e ingeniería de controles | Responsable sugerido — IAM | Ola 0 (0–30 días) | relevante para el directorio | pregunta prioritaria para el directorio

#### A04.2 · ¿Cómo gestionamos el acceso privilegiado: cuentas separadas, elevación justo a tiempo, estaciones de administración protegidas y revisión continua?

- **Por qué importa:** Las cuentas privilegiadas permanentes son el objetivo preferido para convertir un incidente en una crisis.
- **Buena práctica (evidencia esperada):** Sin privilegios permanentes para roles críticos, elevación con aprobación y vencimiento, estaciones de administración dedicadas y revisiones periódicas.
- **Postura de Microsoft:** La estrategia de acceso privilegiado de Microsoft sostiene que el acceso privilegiado debe ser la máxima prioridad de seguridad, con el enterprise access model, cuentas y dispositivos dedicados a la administración y acceso justo a tiempo.
- **Capacidades Microsoft:** Microsoft Entra Privileged Identity Management; estaciones de acceso privilegiado; Microsoft Defender for Identity
- **Cruce de marcos:** NIST — CSF PR.AA · PR.PS | CIS — CIS 5 (5.4) · CIS 6 (6.5) | The Open Group — Zero Trust Commandments | ISACA — COBIT DSS05 · DSS06 | CSA — CCM IAM | MCSB — PA
- **Anclaje y COE:** Atlas — TECHNOLOGY / Limitar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Acceso e identidad | COE — Plataforma e ingeniería de controles | Responsable sugerido — IAM | Ola 0 (0–30 días)

#### A04.3 · ¿Las políticas de acceso condicional cubren a todos los usuarios, aplicaciones e identidades de carga de trabajo, y cómo detectamos sus brechas?

- **Por qué importa:** Una sola aplicación o grupo excluido puede anular toda la estrategia de identidad.
- **Buena práctica (evidencia esperada):** Cobertura medida por usuario y aplicación, exclusiones justificadas y revisadas, y pruebas en modo de solo informe antes de aplicar cambios.
- **Postura de Microsoft:** Microsoft usa el acceso condicional como motor de políticas de Zero Trust; su agente de optimización de acceso condicional (disponible de forma general desde julio de 2025) detecta usuarios, aplicaciones e identidades de agentes no cubiertos y recomienda o aplica correcciones.
- **Capacidades Microsoft:** Microsoft Entra Conditional Access; agente de optimización de acceso condicional (Security Copilot en Entra)
- **Cruce de marcos:** NIST — CSF PR.AA | CIS — CIS 6 (6.7) | The Open Group — Zero Trust Commandments | ISACA — COBIT DSS05 | CSA — CCM IAM | MCSB — IM
- **Anclaje y COE:** Atlas — TECHNOLOGY / Limitar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Acceso e identidad | COE — Plataforma e ingeniería de controles | Responsable sugerido — IAM | Ola 1 (30–90 días)

#### A04.4 · ¿Tenemos inventario y gobierno de las identidades no humanas (cuentas de servicio, principales de servicio, secretos, certificados) con dueño y vencimiento?

- **Por qué importa:** Las identidades no humanas superan en número a las humanas, rara vez tienen dueño y suelen tener privilegios excesivos.
- **Buena práctica (evidencia esperada):** Inventario completo, dueño asignado, credenciales sin secretos estáticos cuando es posible, rotación y revisión de permisos.
- **Postura de Microsoft:** Microsoft recomienda identidades administradas y federación de identidades de carga de trabajo para eliminar secretos, y aplicar acceso condicional y detección de riesgo también a esas identidades.
- **Capacidades Microsoft:** Microsoft Entra Workload ID; identidades administradas; gobierno de aplicaciones en Defender for Cloud Apps
- **Cruce de marcos:** NIST — CSF PR.AA · ID.AM | CIS — CIS 5 (5.5) | The Open Group — sin referencia directa | ISACA — COBIT DSS05 · BAI09 | CSA — CCM IAM | MCSB — IM
- **Anclaje y COE:** Atlas — TECHNOLOGY / Limitar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Acceso e identidad | COE — Plataforma e ingeniería de controles | Responsable sugerido — IAM | Ola 1 (30–90 días)

#### A04.5 · ¿Cómo gobernamos el ciclo de vida de las identidades (alta, cambio, baja) y las revisiones de acceso, incluidos terceros e invitados?

- **Por qué importa:** Los accesos acumulados por cambios de puesto y los invitados olvidados son una fuente constante de exposición.
- **Buena práctica (evidencia esperada):** Altas y bajas automatizadas desde la fuente de verdad, paquetes de acceso con vencimiento, revisiones periódicas y bajas verificadas de terceros.
- **Postura de Microsoft:** Microsoft recomienda automatizar el gobierno de identidades con flujos de trabajo de ciclo de vida, administración de derechos y revisiones de acceso.
- **Capacidades Microsoft:** Microsoft Entra ID Governance (flujos de trabajo de ciclo de vida, administración de derechos, revisiones de acceso)
- **Cruce de marcos:** NIST — CSF PR.AA | CIS — CIS 5 (5.1, 5.3) · CIS 6 (6.1, 6.2) | The Open Group — sin referencia directa | ISACA — COBIT DSS05 · APO07 | CSA — CCM IAM · HRS | MCSB — IM · PA
- **Anclaje y COE:** Atlas — TECHNOLOGY / Limitar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Acceso e identidad | COE — Plataforma e ingeniería de controles | Responsable sugerido — IAM + RR. HH. | Ola 1 (30–90 días)

#### A04.6 · ¿Cómo detectamos y respondemos al robo de tokens, sesiones y credenciales, y en cuánto tiempo revocamos un acceso comprometido?

- **Por qué importa:** Con la MFA extendida, los atacantes migran al robo de tokens y cookies para eludirla.
- **Buena práctica (evidencia esperada):** Detección de riesgo de usuario y de inicio de sesión, evaluación continua de acceso, protección de tokens y revocación automática medida en minutos.
- **Postura de Microsoft:** Microsoft combina protección de identidad basada en riesgo, evaluación continua de acceso e interrupción automática de ataques para contener cuentas comprometidas a velocidad de máquina.
- **Capacidades Microsoft:** Microsoft Entra ID Protection; evaluación continua de acceso; interrupción automática de ataques (Defender XDR); Microsoft Defender for Identity
- **Cruce de marcos:** NIST — CSF DE.CM · RS.MI · PR.AA | CIS — CIS 13 · CIS 17 | The Open Group — sin referencia directa | ISACA — COBIT DSS05 · DSS02 | CSA — CCM IAM · SEF | MCSB — IM · LT
- **Anclaje y COE:** Atlas — TECHNOLOGY / Contener | TheNextCISO — CISO-DO (operación de dominios) | SAF — Operaciones de seguridad (SecOps/SOC) | COE — Operaciones, detección y respuesta | Responsable sugerido — IAM + SOC | Ola 1 (30–90 días)

#### A04.7 · ¿Cómo protegemos los sistemas que gobiernan la identidad (proveedor de identidad, federación, Active Directory híbrido, cuentas de emergencia)?

- **Por qué importa:** Comprometer el sistema de identidad equivale a comprometer toda la organización.
- **Buena práctica (evidencia esperada):** Sistemas de identidad tratados como nivel 0, administración aislada, monitoreo específico y cuentas de emergencia protegidas y probadas.
- **Postura de Microsoft:** Microsoft trata los sistemas de identidad como activos de máxima criticidad y publica guías para proteger la sincronización híbrida, la federación y las cuentas de acceso de emergencia.
- **Capacidades Microsoft:** Microsoft Defender for Identity; guía de cuentas de acceso de emergencia de Microsoft Entra
- **Cruce de marcos:** NIST — CSF PR.AA · PR.PS | CIS — CIS 5 · CIS 6 (6.6) | The Open Group — sin referencia directa | ISACA — COBIT DSS05 | CSA — CCM IAM | MCSB — IM · PA
- **Anclaje y COE:** Atlas — TECHNOLOGY / Limitar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Acceso e identidad | COE — Plataforma e ingeniería de controles | Responsable sugerido — IAM | Ola 1 (30–90 días)

#### A04.8 · ¿Cómo verificamos la identidad de las personas en procesos críticos (alta de empleados, recuperación de cuentas, mesa de ayuda) frente a suplantaciones con IA?

- **Por qué importa:** La mesa de ayuda y los procesos de recuperación son la vía preferida para eludir controles técnicos mediante ingeniería social.
- **Buena práctica (evidencia esperada):** Verificación reforzada en altas y recuperaciones, validación fuera de banda para pedidos sensibles y procedimientos que no dependen solo de voz o video.
- **Postura de Microsoft:** SAF recomienda validar fuera de banda las comunicaciones sensibles o sospechosas ante suplantaciones de voz, video y estilo de escritura; Microsoft ofrece credenciales verificables con comprobación facial.
- **Capacidades Microsoft:** Microsoft Entra Verified ID (Face Check); métodos de autenticación sin contraseña
- **Cruce de marcos:** NIST — CSF PR.AA · PR.AT | CIS — CIS 14 · CIS 5 | The Open Group — sin referencia directa | ISACA — COBIT DSS05 · APO07 | CSA — CCM IAM · HRS | MCSB — IM
- **Anclaje y COE:** Atlas — ORGANIZATION / Anticipar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Acceso e identidad | COE — Plataforma e ingeniería de controles | Responsable sugerido — IAM + Mesa de ayuda | Ola 1 (30–90 días)

#### A04.9 · ¿Cómo medimos la madurez de identidad (cobertura de MFA, privilegios permanentes, cuentas inactivas, riesgo de identidad) y quién responde por cada indicador?

- **Por qué importa:** Sin indicadores con responsable, la deuda de identidad se acumula en silencio.
- **Buena práctica (evidencia esperada):** Tablero mensual con indicadores, metas y dueños; tendencia revisada en el comité de seguridad.
- **Postura de Microsoft:** Microsoft expone recomendaciones e indicadores de identidad en Microsoft Entra y en Microsoft Secure Score para medir el avance y priorizar acciones.
- **Capacidades Microsoft:** Recomendaciones de Microsoft Entra; Microsoft Secure Score
- **Cruce de marcos:** NIST — CSF ID.IM · PR.AA | CIS — CIS 5 · CIS 6 | The Open Group — sin referencia directa | ISACA — COBIT MEA01 | CSA — CCM IAM | MCSB — IM
- **Anclaje y COE:** Atlas — TECHNOLOGY / Gobernar | TheNextCISO — CISO-MM (madurez) | SAF — Acceso e identidad | COE — Valor, métricas y comunicación ejecutiva | Responsable sugerido — IAM | Ola 2 (90–180 días)

### A05 — Datos, privacidad y criptografía

*Saber dónde está la información, quién accede y cómo se protege durante todo su ciclo de vida.*

#### A05.1 · ¿Sabemos dónde están nuestros datos sensibles, quién accede a ellos y cuán sobreexpuestos están?

- **Por qué importa:** No se puede proteger lo que no se conoce; la sobreexposición es la principal fuente de fugas accidentales.
- **Buena práctica (evidencia esperada):** Descubrimiento automatizado de datos sensibles en la nube y en entornos locales, mapa de accesos y un indicador de sobreexposición con plan de reducción.
- **Postura de Microsoft:** Microsoft recomienda una estrategia de seguridad de datos centrada en descubrir, clasificar y proteger la información, y en gestionar de forma continua la postura de seguridad de los datos.
- **Capacidades Microsoft:** Microsoft Purview Data Security Posture Management (DSPM); Microsoft Purview Data Map; SharePoint Advanced Management (informes de sobreexposición)
- **Cruce de marcos:** NIST — CSF ID.AM · PR.DS | CIS — CIS 3 (3.1, 3.2) | The Open Group — TOGAF Fase C (datos) | ISACA — COBIT APO14 · BAI09 | CSA — CCM DSP | MCSB — DP
- **Anclaje y COE:** Atlas — TECHNOLOGY / Anticipar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Seguridad de datos | COE — Plataforma e ingeniería de controles | Responsable sugerido — Data Officer + CISO | Ola 0 (0–30 días)

#### A05.2 · ¿Tenemos una taxonomía de clasificación aprobada, aplicada automáticamente y comprensible para los usuarios?

- **Por qué importa:** Una clasificación que depende solo de la voluntad del usuario no escala ni se sostiene.
- **Buena práctica (evidencia esperada):** Taxonomía corta aprobada por el negocio, etiquetado automático y recomendado, cobertura medida y protección asociada a cada nivel.
- **Postura de Microsoft:** SAF propone como iniciativa temprana aprobar una taxonomía y clasificar y etiquetar los activos; Microsoft Purview aplica etiquetas de confidencialidad con etiquetado automático.
- **Capacidades Microsoft:** Microsoft Purview Information Protection (etiquetas de confidencialidad, etiquetado automático)
- **Cruce de marcos:** NIST — CSF PR.DS · ID.AM | CIS — CIS 3 (3.7) | The Open Group — TOGAF Fase C (datos) | ISACA — COBIT APO14 | CSA — CCM DSP | MCSB — DP
- **Anclaje y COE:** Atlas — TECHNOLOGY / Limitar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Seguridad de datos | COE — Plataforma e ingeniería de controles | Responsable sugerido — Data Officer | Ola 0 (0–30 días)

#### A05.3 · ¿Cómo prevenimos la pérdida de datos en correo, colaboración, endpoints, navegadores, nube e IA con políticas coherentes?

- **Por qué importa:** Políticas distintas por canal crean caminos alternativos para la fuga.
- **Buena práctica (evidencia esperada):** Política unificada por tipo de dato, aplicada en todos los canales, con un período previo en modo auditoría, métricas de incidentes y ajuste de falsos positivos.
- **Postura de Microsoft:** Microsoft Purview ofrece prevención de pérdida de datos unificada para Microsoft 365, endpoints, navegadores, nube y servicios de IA, administrada desde una sola consola.
- **Capacidades Microsoft:** Microsoft Purview Data Loss Prevention
- **Cruce de marcos:** NIST — CSF PR.DS | CIS — CIS 3 (3.13) | The Open Group — sin referencia directa | ISACA — COBIT DSS05 · APO14 | CSA — CCM DSP | MCSB — DP
- **Anclaje y COE:** Atlas — TECHNOLOGY / Limitar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Seguridad de datos | COE — Plataforma e ingeniería de controles | Responsable sugerido — Seguridad de datos | Ola 1 (30–90 días)

#### A05.4 · ¿Cómo gestionamos el riesgo interno, negligente o malicioso, con proporcionalidad y respeto por la privacidad de las personas?

- **Por qué importa:** Muchas fugas graves provienen de personas con acceso legítimo; vigilarlas sin reglas daña la confianza.
- **Buena práctica (evidencia esperada):** Programa con patrocinio de RR. HH. y Legal, indicadores de riesgo, seudonimización por defecto, investigación con roles separados y protección adaptativa.
- **Postura de Microsoft:** Microsoft aborda el riesgo interno con señales de comportamiento seudonimizadas por defecto y con protección adaptativa que ajusta los controles al nivel de riesgo de cada usuario.
- **Capacidades Microsoft:** Microsoft Purview Insider Risk Management; Adaptive Protection
- **Cruce de marcos:** NIST — CSF PR.DS · DE.CM | CIS — CIS 3 (3.14) · CIS 14 | The Open Group — sin referencia directa | ISACA — COBIT APO07 · DSS05 | CSA — CCM HRS · DSP | MCSB — DP · LT
- **Anclaje y COE:** Atlas — ORGANIZATION / Anticipar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Seguridad de datos | COE — Plataforma e ingeniería de controles | Responsable sugerido — CISO + RR. HH. + Legal | Ola 2 (90–180 días)

#### A05.5 · ¿Retenemos solo lo necesario, eliminamos lo obsoleto y podemos responder a requerimientos legales y de titulares de datos?

- **Por qué importa:** Los datos que no se necesitan solo aportan riesgo: aumentan el impacto de una fuga y el costo de cada investigación.
- **Buena práctica (evidencia esperada):** Políticas de retención por tipo de registro, eliminación defendible, retenciones legales controladas y búsquedas probadas para responder requerimientos.
- **Postura de Microsoft:** Microsoft integra en Purview la gestión del ciclo de vida, la gestión de registros y eDiscovery para conservar lo necesario y eliminar de forma defendible.
- **Capacidades Microsoft:** Microsoft Purview Data Lifecycle Management; Records Management; eDiscovery
- **Cruce de marcos:** NIST — CSF PR.DS · Privacy Framework 1.0 | CIS — CIS 3 (3.4, 3.5) | The Open Group — sin referencia directa | ISACA — COBIT APO14 · MEA03 | CSA — CCM DSP | MCSB — DP
- **Anclaje y COE:** Atlas — TECHNOLOGY / Limitar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Seguridad de datos | COE — Riesgo, cumplimiento y aseguramiento | Responsable sugerido — Compliance + Legal | Ola 2 (90–180 días)

#### A05.6 · ¿Cómo gestionamos claves, secretos y certificados (custodia, rotación, separación de funciones, módulos de seguridad de hardware)?

- **Por qué importa:** Una clave expuesta o un certificado vencido pueden comprometer o detener servicios críticos.
- **Buena práctica (evidencia esperada):** Inventario de claves y certificados, almacenamiento en bóvedas o HSM, rotación automatizada, separación de funciones y alertas de vencimiento.
- **Postura de Microsoft:** Microsoft recomienda centralizar secretos y claves en bóvedas administradas, evitar secretos en el código y usar claves administradas por el cliente cuando el riesgo lo justifique.
- **Capacidades Microsoft:** Azure Key Vault; Azure Key Vault Managed HSM; Customer Key (Microsoft 365); detección de secretos de GitHub
- **Cruce de marcos:** NIST — CSF PR.DS · PR.AA | CIS — CIS 3 (3.10, 3.11) | The Open Group — sin referencia directa | ISACA — COBIT DSS05 | CSA — CCM CEK | MCSB — DP
- **Anclaje y COE:** Atlas — TECHNOLOGY / Limitar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Seguridad de datos | COE — Plataforma e ingeniería de controles | Responsable sugerido — Seguridad de plataforma | Ola 1 (30–90 días)

#### A05.7 · ¿Tenemos un inventario criptográfico y una hoja de ruta hacia la criptografía poscuántica, con fechas y dependencias de proveedores?

- **Por qué importa:** Los datos de larga vida pueden capturarse hoy y descifrarse mañana; la transición criptográfica lleva años.
- **Buena práctica (evidencia esperada):** Inventario de algoritmos, protocolos y dependencias; priorización por vida útil de los datos; pruebas de agilidad criptográfica y compromisos de los proveedores.
- **Postura de Microsoft:** El Quantum Safe Program de Microsoft fijó en 2025 la adopción temprana para 2029 y la transición completa para 2033, y en junio de 2026 aceleró el objetivo: criptografía poscuántica en productos y servicios críticos para 2029, como requisito medido dentro de SFI. Recomienda empezar ya por el inventario y la agilidad criptográfica.
- **Capacidades Microsoft:** Microsoft Quantum Safe Program
- **Cruce de marcos:** NIST — FIPS 203 · 204 · 205 · IR 8547 · CSF PR.DS | CIS — CIS 3 (3.10, 3.11) | The Open Group — TOGAF Fases E–F (planificación de la migración) | ISACA — COBIT APO04 · BAI09 | CSA — CCM CEK | MCSB — DP
- **Anclaje y COE:** Atlas — TECHNOLOGY / Anticipar | TheNextCISO — CISO-NX (nueva generación) | SAF — Seguridad de datos | COE — Arquitectura y patrones seguros | Responsable sugerido — Arquitectura + Criptografía | Ola 2 (90–180 días) | relevante para el directorio

#### A05.8 · ¿Cómo cumplimos las leyes de protección de datos de cada país donde operamos y los requisitos de residencia de datos que nos aplican?

- **Por qué importa:** El incumplimiento de normas de privacidad tiene consecuencias legales y reputacionales independientes del incidente técnico.
- **Buena práctica (evidencia esperada):** Mapa de obligaciones por país, registro de tratamientos, evaluaciones de impacto donde corresponda y evidencia de residencia y transferencias.
- **Postura de Microsoft:** Microsoft ofrece plantillas regulatorias en Compliance Manager y compromisos contractuales de protección y residencia de datos para sus servicios en la nube.
- **Capacidades Microsoft:** Microsoft Purview Compliance Manager; Microsoft Products and Services Data Protection Addendum; opciones de residencia de datos
- **Cruce de marcos:** NIST — Privacy Framework 1.0 · CSF GV.OC | CIS — CIS 3 | The Open Group — TOGAF Gestión de requisitos | ISACA — COBIT MEA03 · APO14 | CSA — CCM DSP · GRC | MCSB — DP · GS
- **Anclaje y COE:** Atlas — TRUST / Gobernar | TheNextCISO — CISO-OS (gobierno) | SAF — Seguridad de datos | COE — Riesgo, cumplimiento y aseguramiento | Responsable sugerido — DPO + Legal | Ola 1 (30–90 días) | relevante para el directorio

#### A05.9 · ¿Qué indicadores muestran que la protección de datos funciona (cobertura de etiquetado, incidentes de DLP, sobreexposición corregida, tiempo de respuesta)?

- **Por qué importa:** Sin indicadores, la protección de datos se evalúa por la ausencia de incidentes conocidos, que es una señal engañosa.
- **Buena práctica (evidencia esperada):** Tablero con cobertura, tendencias y metas, revisado cada mes por el dueño de los datos y el CISO.
- **Postura de Microsoft:** Microsoft Purview reúne informes de postura de seguridad de datos y de actividad para medir la cobertura y la efectividad de los controles.
- **Capacidades Microsoft:** Microsoft Purview DSPM (informes); explorador de actividad de Purview
- **Cruce de marcos:** NIST — CSF ID.IM · PR.DS | CIS — CIS 3 | The Open Group — sin referencia directa | ISACA — COBIT MEA01 | CSA — CCM DSP | MCSB — DP
- **Anclaje y COE:** Atlas — TECHNOLOGY / Gobernar | TheNextCISO — CISO-MM (madurez) | SAF — Seguridad de datos | COE — Valor, métricas y comunicación ejecutiva | Responsable sugerido — Data Officer + CISO | Ola 2 (90–180 días)

### A06 — Exposición: activos, configuración y vulnerabilidades

*Reducir la ventana de exposición antes de que un adversario la aproveche.*

#### A06.1 · ¿Tenemos un inventario confiable y actualizado de dispositivos, cargas en la nube, aplicaciones SaaS, APIs y activos expuestos a internet?

- **Por qué importa:** Los activos desconocidos no tienen parches, monitoreo ni dueño, y son los preferidos por los atacantes.
- **Buena práctica (evidencia esperada):** Inventario conciliado desde varias fuentes, actualización continua, dueño por activo y descubrimiento periódico de la superficie externa.
- **Postura de Microsoft:** Microsoft recomienda una vista unificada de la superficie de ataque interna y externa, con descubrimiento de dispositivos, recursos en la nube e identidades, sobre la que Security Exposure Management analiza rutas de ataque.
- **Capacidades Microsoft:** Microsoft Security Exposure Management (inventario y superficie de ataque); Microsoft Defender for Endpoint (descubrimiento de dispositivos); Microsoft Defender for Cloud
- **Cruce de marcos:** NIST — CSF ID.AM | CIS — CIS 1 · CIS 2 | The Open Group — TOGAF Fase D | ISACA — COBIT BAI09 · BAI10 | CSA — CCM UEM · IVS | MCSB — AM
- **Anclaje y COE:** Atlas — TECHNOLOGY / Anticipar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Gestión de la postura de seguridad | COE — Plataforma e ingeniería de controles | Responsable sugerido — CIO + CISO | Ola 0 (0–30 días)

#### A06.2 · ¿Cuánto tiempo permanecen expuestos nuestros activos críticos a vulnerabilidades explotables y cuál es nuestra meta?

- **Por qué importa:** Los atacantes explotan vulnerabilidades en horas o días; lo que importa es la ventana de exposición, no el porcentaje de parches.
- **Buena práctica (evidencia esperada):** Medición del tiempo de exposición por criticidad, metas diferenciadas (horas para activos expuestos a internet) y controles compensatorios cuando no se puede parchear.
- **Postura de Microsoft:** Según el Microsoft Digital Defense Report 2026, la mediana hasta la explotación de una vulnerabilidad es menor a 24 horas, frente a 30–60 días de remediación; Microsoft recomienda priorizar por exposición real y criticidad, y medir el tiempo de mitigación en lugar del cierre de tickets.
- **Capacidades Microsoft:** Microsoft Defender Vulnerability Management; Microsoft Security Exposure Management
- **Cruce de marcos:** NIST — CSF ID.RA · PR.PS | CIS — CIS 7 (7.2–7.4) | The Open Group — Open FAIR O-RT | ISACA — COBIT APO12 · DSS05 | CSA — CCM TVM | MCSB — PV
- **Anclaje y COE:** Atlas — TECHNOLOGY / Limitar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Gestión de la postura de seguridad | COE — Plataforma e ingeniería de controles | Responsable sugerido — CISO + Infraestructura | Ola 0 (0–30 días) | relevante para el directorio | pregunta prioritaria para el directorio

#### A06.3 · ¿Priorizamos la remediación por explotabilidad, rutas de ataque y criticidad del activo, o solo por severidad nominal?

- **Por qué importa:** Una vulnerabilidad media en un activo expuesto puede ser más peligrosa que una crítica en un sistema aislado.
- **Buena práctica (evidencia esperada):** Priorización que combina explotación activa, rutas de ataque hacia activos críticos y exposición, con criterios documentados.
- **Postura de Microsoft:** Microsoft Security Exposure Management analiza rutas de ataque y puntos de estrangulamiento hacia los activos críticos para concentrar la remediación donde más reduce el riesgo.
- **Capacidades Microsoft:** Microsoft Security Exposure Management (rutas de ataque); Microsoft Defender Vulnerability Management
- **Cruce de marcos:** NIST — CSF ID.RA | CIS — CIS 7 (7.2) | The Open Group — Open FAIR O-RT | ISACA — COBIT APO12 | CSA — CCM TVM | MCSB — PV
- **Anclaje y COE:** Atlas — TECHNOLOGY / Anticipar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Gestión de la postura de seguridad | COE — Plataforma e ingeniería de controles | Responsable sugerido — Gestión de vulnerabilidades | Ola 1 (30–90 días)

#### A06.4 · ¿Están definidas y aplicadas configuraciones seguras de referencia, y cómo detectamos y corregimos los desvíos?

- **Por qué importa:** La mayoría de las intrusiones aprovecha configuraciones débiles conocidas, no vulnerabilidades desconocidas.
- **Buena práctica (evidencia esperada):** Líneas base aprobadas por tecnología, aplicación automatizada, medición de cumplimiento y corrección de desvíos con plazos.
- **Postura de Microsoft:** Microsoft aplica el principio de seguro por defecto: Baseline Security Mode cubre Microsoft 365 Apps, SharePoint y OneDrive, Teams, Exchange Online y Entra, y recomienda ejecutar informes de impacto antes de activar cada ajuste; se complementa con líneas base de Intune y Microsoft Cloud Security Benchmark.
- **Capacidades Microsoft:** Baseline Security Mode (Microsoft 365); líneas base de seguridad de Intune; Microsoft Cloud Security Benchmark; Microsoft Defender for Cloud
- **Cruce de marcos:** NIST — CSF PR.PS | CIS — CIS 4 · CIS Benchmarks (Microsoft 365 v7.0.0, Azure) | The Open Group — sin referencia directa | ISACA — COBIT BAI10 · DSS05 | CSA — CCM CCC · IVS | MCSB — PV · AM
- **Anclaje y COE:** Atlas — TECHNOLOGY / Limitar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Gestión de la postura de seguridad | COE — Plataforma e ingeniería de controles | Responsable sugerido — Infraestructura + Seguridad | Ola 0 (0–30 días)

#### A06.5 · ¿Cómo protegemos endpoints y servidores (detección y respuesta en modo bloqueo, reducción de superficie de ataque, control de aplicaciones)?

- **Por qué importa:** El endpoint sigue siendo el lugar donde se ejecuta la mayor parte de las cadenas de ataque.
- **Buena práctica (evidencia esperada):** Cobertura completa de EDR en modo bloqueo, reglas de reducción de la superficie de ataque, control de aplicaciones en sistemas críticos y medición de dispositivos sin protección.
- **Postura de Microsoft:** Microsoft recomienda EDR en modo bloqueo, reglas de reducción de la superficie de ataque y control de aplicaciones, integrados con la respuesta automática de Defender XDR.
- **Capacidades Microsoft:** Microsoft Defender for Endpoint; App Control for Business; Microsoft Intune
- **Cruce de marcos:** NIST — CSF PR.PS · DE.CM | CIS — CIS 10 · CIS 2 (2.5–2.7) | The Open Group — sin referencia directa | ISACA — COBIT DSS05 | CSA — CCM UEM | MCSB — ES
- **Anclaje y COE:** Atlas — TECHNOLOGY / Limitar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Seguridad de infraestructura | COE — Plataforma e ingeniería de controles | Responsable sugerido — Seguridad de endpoints | Ola 0 (0–30 días)

#### A06.6 · ¿Cómo gestionamos el correo y la navegación como vectores principales de phishing, fraude por correo corporativo y malware?

- **Por qué importa:** El phishing sigue siendo un vector dominante de acceso inicial y la IA lo hace más convincente.
- **Buena práctica (evidencia esperada):** Protección avanzada de correo y enlaces, autenticación de dominio (SPF, DKIM y DMARC en modo de rechazo), simulaciones periódicas y circuito de reporte de usuarios.
- **Postura de Microsoft:** Microsoft recomienda protección de correo y colaboración con análisis de enlaces y adjuntos, simulaciones de ataque y el agente de clasificación de alertas de seguridad de Security Copilot (antes agente de clasificación de phishing, disponible de forma general desde noviembre de 2025).
- **Capacidades Microsoft:** Microsoft Defender for Office 365; simulación de ataques; Security Alert Triage Agent (Security Copilot)
- **Cruce de marcos:** NIST — CSF PR.PS · DE.CM · PR.AT | CIS — CIS 9 · CIS 14 | The Open Group — sin referencia directa | ISACA — COBIT DSS05 | CSA — CCM TVM | MCSB — sin referencia directa
- **Anclaje y COE:** Atlas — TECHNOLOGY / Limitar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Seguridad de infraestructura | COE — Plataforma e ingeniería de controles | Responsable sugerido — Seguridad de mensajería | Ola 0 (0–30 días)

#### A06.7 · ¿Podríamos absorber un volumen de vulnerabilidades diez veces mayor al actual, ahora que atacantes y defensores las descubren con IA?

- **Por qué importa:** La IA acelera el descubrimiento y la explotación de vulnerabilidades; los procesos manuales de parcheo no escalan.
- **Buena práctica (evidencia esperada):** Capacidad modelada por escenarios de volumen, despliegue de parches automatizado, criterios de aislamiento y decisiones anticipadas sobre sistemas heredados.
- **Postura de Microsoft:** SAF plantea planificar para la escala (¿podemos procesar mil, diez mil o cien mil vulnerabilidades por mes?) porque la IA acelera el descubrimiento y la explotación; Microsoft ofrece un agente de remediación de vulnerabilidades en Intune (versión preliminar) que prioriza y guía la corrección con aprobación del administrador.
- **Capacidades Microsoft:** Agente de remediación de vulnerabilidades de Intune (versión preliminar); Windows Autopatch; Microsoft Defender Vulnerability Management
- **Cruce de marcos:** NIST — CSF ID.RA · PR.PS | CIS — CIS 7 | The Open Group — TOGAF Fase H | ISACA — COBIT APO12 · BAI04 | CSA — CCM TVM | MCSB — PV
- **Anclaje y COE:** Atlas — TECHNOLOGY / Anticipar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Gestión de la postura de seguridad | COE — Plataforma e ingeniería de controles | Responsable sugerido — CIO + CISO | Ola 2 (90–180 días) | relevante para el directorio

#### A06.8 · ¿Cómo medimos y comunicamos la postura (puntuación de seguridad, exposición, cumplimiento de configuraciones) sin convertirla en un fin en sí misma?

- **Por qué importa:** Una puntuación alta puede convivir con rutas de ataque críticas abiertas si se optimiza el indicador y no el riesgo.
- **Buena práctica (evidencia esperada):** Indicadores de postura vinculados a escenarios de riesgo, metas por activo crítico y análisis del impacto real de cada cambio de puntuación.
- **Postura de Microsoft:** Microsoft ofrece Secure Score y métricas de exposición y recomienda usarlos para priorizar acciones por riesgo, no como objetivo aislado.
- **Capacidades Microsoft:** Microsoft Secure Score; Microsoft Security Exposure Management (iniciativas y métricas)
- **Cruce de marcos:** NIST — CSF ID.IM · GV.OV | CIS — CIS 4 · CIS 7 | The Open Group — sin referencia directa | ISACA — COBIT MEA01 | CSA — CCM GRC · TVM | MCSB — PV
- **Anclaje y COE:** Atlas — TRUST / Gobernar | TheNextCISO — CISO-MM (madurez) | SAF — Gestión de la postura de seguridad | COE — Valor, métricas y comunicación ejecutiva | Responsable sugerido — CISO | Ola 1 (30–90 días)

#### A06.9 · ¿Hacemos pruebas ofensivas (pruebas de penetración, red team, purple team, simulación de ataques) y cómo cerramos el ciclo de los hallazgos?

- **Por qué importa:** Solo las pruebas realistas revelan si los controles funcionan juntos frente a un adversario.
- **Buena práctica (evidencia esperada):** Programa anual basado en escenarios, alcance que incluye identidad y nube, seguimiento de hallazgos hasta su cierre y repetición para verificar.
- **Postura de Microsoft:** SAF incluye la simulación de ataques (red y purple team, pruebas de penetración y ejercicios de mesa) como función de operaciones de seguridad que integra los aprendizajes en todos los procesos.
- **Capacidades Microsoft:** SAF (simulación de ataques); simulación de ataques de Defender for Office 365
- **Cruce de marcos:** NIST — CSF ID.IM · ID.RA | CIS — CIS 18 | The Open Group — sin referencia directa | ISACA — COBIT MEA02 · DSS05 | CSA — CCM TVM · A&A | MCSB — PV
- **Anclaje y COE:** Atlas — TECHNOLOGY / Anticipar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Operaciones de seguridad (SecOps/SOC) | COE — Operaciones, detección y respuesta | Responsable sugerido — Seguridad ofensiva | Ola 2 (90–180 días)

### A07 — Nube, aplicaciones, terceros y cadena de suministro

*La seguridad que se hereda, se compra o se construye: nube, software, APIs y proveedores.*

#### A07.1 · ¿Entendemos y documentamos el modelo de responsabilidad compartida de cada servicio en la nube que usamos?

- **Por qué importa:** Muchos incidentes en la nube se originan en controles que el cliente creía a cargo del proveedor.
- **Buena práctica (evidencia esperada):** Matriz de responsabilidades por servicio (IaaS, PaaS, SaaS), controles del lado del cliente implementados y evidencias del proveedor revisadas.
- **Postura de Microsoft:** Microsoft publica el modelo de responsabilidad compartida en la nube: en todos los modelos de servicio, el cliente conserva la responsabilidad sobre sus datos, identidades, dispositivos y cuentas.
- **Capacidades Microsoft:** Responsabilidad compartida en la nube (Microsoft Learn); Service Trust Portal; Microsoft Cloud Security Benchmark
- **Cruce de marcos:** NIST — CSF GV.SC · GV.RR | CIS — CIS 15 | The Open Group — G152 (requisitos y responsabilidades de seguridad) | ISACA — COBIT APO09 · APO10 | CSA — CCM STA (responsabilidad compartida) · DCS (a cargo del proveedor) · CAIQ v4.1 | MCSB — GS
- **Anclaje y COE:** Atlas — TRUST / Anticipar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Arquitectura de seguridad de extremo a extremo | COE — Arquitectura y patrones seguros | Responsable sugerido — Arquitectura cloud | Ola 0 (0–30 días)

#### A07.2 · ¿Cómo gestionamos la postura de seguridad y la protección de las cargas de trabajo en todas nuestras nubes?

- **Por qué importa:** Las configuraciones erróneas en la nube se explotan en horas y escalan rápido entre cuentas y suscripciones.
- **Buena práctica (evidencia esperada):** Gestión de postura multinube con políticas comunes, protección de cargas de trabajo, análisis de permisos y metas de corrección por criticidad.
- **Postura de Microsoft:** Microsoft Defender for Cloud ofrece gestión de postura y protección de cargas de trabajo para Azure, AWS y Google Cloud, alineada con Microsoft Cloud Security Benchmark.
- **Capacidades Microsoft:** Microsoft Defender for Cloud (gestión de postura y protección de cargas de trabajo)
- **Cruce de marcos:** NIST — CSF PR.PS · DE.CM | CIS — CIS 4 · CIS Benchmarks (proveedores cloud) | The Open Group — sin referencia directa | ISACA — COBIT DSS05 · BAI10 | CSA — CCM IVS · CCC | MCSB — PV · AM · LT
- **Anclaje y COE:** Atlas — TECHNOLOGY / Limitar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Seguridad de infraestructura | COE — Plataforma e ingeniería de controles | Responsable sugerido — Seguridad cloud | Ola 1 (30–90 días)

#### A07.3 · ¿Está integrada la seguridad en el ciclo de desarrollo (modelado de amenazas, análisis de código, secretos, dependencias, pruebas) con criterios de bloqueo?

- **Por qué importa:** Corregir en el diseño cuesta mucho menos que corregir en producción o después de un incidente.
- **Buena práctica (evidencia esperada):** Modelado de amenazas en los cambios relevantes, análisis automatizado en el pipeline, criterios de bloqueo por severidad y métricas de tiempo de corrección.
- **Postura de Microsoft:** Microsoft aplica desde hace dos décadas su Security Development Lifecycle y recomienda integrar la seguridad en el flujo del desarrollador con análisis de código, secretos y dependencias.
- **Capacidades Microsoft:** Security Development Lifecycle (SDL); GitHub Advanced Security; Microsoft Defender for Cloud (seguridad de DevOps)
- **Cruce de marcos:** NIST — SP 800-218 (SSDF) · CSF PR.PS | CIS — CIS 16 (16.14) | The Open Group — TOGAF Fase G · Security Design Patterns | ISACA — COBIT BAI03 · BAI07 | CSA — CCM AIS | MCSB — DS
- **Anclaje y COE:** Atlas — TECHNOLOGY / Limitar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Seguridad del desarrollo | COE — Arquitectura y patrones seguros | Responsable sugerido — Ingeniería + AppSec | Ola 1 (30–90 días)

#### A07.4 · ¿Cómo aseguramos la integridad de la cadena de suministro de software (componentes, SBOM, firmas, procedencia, repositorios y pipelines)?

- **Por qué importa:** Comprometer un componente o un pipeline permite llegar a miles de víctimas con una sola intrusión.
- **Buena práctica (evidencia esperada):** Inventario de componentes (SBOM) para el software crítico, verificación de procedencia y firmas, y protección de repositorios y pipelines con identidades dedicadas.
- **Postura de Microsoft:** La protección de los sistemas de ingeniería es un pilar de SFI; Microsoft recomienda inventariar dependencias, generar atestaciones de compilación y proteger los pipelines.
- **Capacidades Microsoft:** Secure Future Initiative (protección de sistemas de ingeniería); GitHub Advanced Security (dependencias); atestaciones de artefactos de GitHub
- **Cruce de marcos:** NIST — SP 800-218 · SP 800-161 Rev. 1 · CSF GV.SC | CIS — CIS 16 · CIS 2 | The Open Group — sin referencia directa | ISACA — COBIT BAI03 · APO10 | CSA — CCM STA · AIS | MCSB — DS
- **Anclaje y COE:** Atlas — TECHNOLOGY / Limitar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Seguridad del desarrollo | COE — Arquitectura y patrones seguros | Responsable sugerido — Ingeniería + AppSec | Ola 2 (90–180 días)

#### A07.5 · ¿Cómo evaluamos, contratamos y monitoreamos a los terceros críticos, incluidos los proveedores de nuestros proveedores?

- **Por qué importa:** Una parte creciente de los incidentes se origina en relaciones de confianza con terceros.
- **Buena práctica (evidencia esperada):** Inventario y clasificación de proveedores por criticidad, evaluación previa proporcional, monitoreo continuo y plan de salida.
- **Postura de Microsoft:** SAF recomienda actualizar la gestión del riesgo de entidades externas (terceros y n-ésimas partes); Microsoft publica su evidencia de cumplimiento en el Service Trust Portal para facilitar esas evaluaciones.
- **Capacidades Microsoft:** Service Trust Portal; SAF (riesgo de entidades externas)
- **Cruce de marcos:** NIST — CSF GV.SC · SP 800-161 Rev. 1 | CIS — CIS 15 (15.1–15.6) | The Open Group — sin referencia directa | ISACA — COBIT APO10 · APO09 | CSA — CCM STA · CAIQ v4.1 · STAR | MCSB — GS
- **Anclaje y COE:** Atlas — TRUST / Anticipar | TheNextCISO — CISO-OS (gobierno) | SAF — Estrategia, integración y gobierno | COE — Riesgo, cumplimiento y aseguramiento | Responsable sugerido — Compras + CISO | Ola 1 (30–90 días) | relevante para el directorio | pregunta prioritaria para el directorio

#### A07.6 · ¿Qué exigimos contractualmente a los proveedores (notificación de incidentes, derecho de auditoría, continuidad, subcontratistas, salida)?

- **Por qué importa:** Sin cláusulas adecuadas no hay información ni palanca cuando el proveedor sufre un incidente.
- **Buena práctica (evidencia esperada):** Cláusulas estándar por nivel de criticidad, plazos de notificación, derecho a evidencia y auditoría, y plan de salida probado para los proveedores críticos.
- **Postura de Microsoft:** Microsoft documenta sus compromisos de seguridad y privacidad en los términos de producto y en el anexo de protección de datos (DPA), que sirven como referencia de requisitos mínimos.
- **Capacidades Microsoft:** Microsoft Products and Services Data Protection Addendum; Microsoft Product Terms; Service Trust Portal
- **Cruce de marcos:** NIST — CSF GV.SC | CIS — CIS 15 (15.4) | The Open Group — sin referencia directa | ISACA — COBIT APO09 · APO10 | CSA — CCM STA · IPY (portabilidad y salida) | MCSB — GS
- **Anclaje y COE:** Atlas — TRUST / Limitar | TheNextCISO — CISO-OS (gobierno) | SAF — Estrategia, integración y gobierno | COE — Riesgo, cumplimiento y aseguramiento | Responsable sugerido — Legal + Compras | Ola 2 (90–180 días)

#### A07.7 · ¿Cómo gobernamos las aplicaciones SaaS y los permisos OAuth que los usuarios autorizan por su cuenta?

- **Por qué importa:** Las aplicaciones no gestionadas y los consentimientos excesivos abren caminos persistentes hacia los datos.
- **Buena práctica (evidencia esperada):** Descubrimiento continuo de aplicaciones, catálogo de autorizadas, consentimiento administrativo para permisos sensibles y revisión de aplicaciones OAuth.
- **Postura de Microsoft:** Microsoft ofrece descubrimiento de aplicaciones en la nube, gestión de postura SaaS y gobierno de aplicaciones OAuth para detectar permisos excesivos y comportamientos anómalos.
- **Capacidades Microsoft:** Microsoft Defender for Cloud Apps (descubrimiento, gobierno de aplicaciones, postura SaaS); flujo de consentimiento administrativo de Entra
- **Cruce de marcos:** NIST — CSF ID.AM · PR.AA | CIS — CIS 2 (2.3) · CIS 6 | The Open Group — sin referencia directa | ISACA — COBIT BAI09 · DSS05 | CSA — CCM IAM · AIS | MCSB — AM · IM
- **Anclaje y COE:** Atlas — TECHNOLOGY / Limitar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Gestión de la postura de seguridad | COE — Plataforma e ingeniería de controles | Responsable sugerido — IAM + Seguridad cloud | Ola 1 (30–90 días)

#### A07.8 · ¿Cómo protegemos las APIs y la lógica de negocio expuesta (autorización por objeto, límites de consumo, inventario)?

- **Por qué importa:** Las APIs exponen directamente datos y transacciones; los fallos de autorización son difíciles de detectar con herramientas genéricas.
- **Buena práctica (evidencia esperada):** Inventario de APIs, pasarela con autenticación y límites, pruebas de autorización por objeto y monitoreo de abuso.
- **Postura de Microsoft:** Microsoft ofrece protección del ciclo de vida de las APIs publicadas en Azure API Management, con inventario, postura y detección de amenazas.
- **Capacidades Microsoft:** Defender for APIs (Microsoft Defender for Cloud); Azure API Management
- **Cruce de marcos:** NIST — CSF PR.PS · DE.CM | CIS — CIS 16 · CIS 13 | The Open Group — TOGAF Fase C (aplicaciones) | ISACA — COBIT BAI03 · DSS05 | CSA — CCM AIS | MCSB — DS · NS
- **Anclaje y COE:** Atlas — TECHNOLOGY / Limitar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Seguridad del desarrollo | COE — Arquitectura y patrones seguros | Responsable sugerido — AppSec + Arquitectura | Ola 2 (90–180 días)

#### A07.9 · ¿Qué haríamos si un proveedor crítico de nube, software o servicios gestionados sufriera un incidente o una interrupción prolongada?

- **Por qué importa:** La concentración en pocos proveedores crea riesgo sistémico, y no todas las fallas son ataques.
- **Buena práctica (evidencia esperada):** Escenarios de falla de proveedor ensayados, dependencias mapeadas, alternativas o modos degradados definidos y comunicación acordada.
- **Postura de Microsoft:** Tras incidentes de alcance global, Microsoft impulsó la Windows Resiliency Initiative: Quick Machine Recovery (disponible desde julio de 2025) recupera equipos que no arrancan, y la plataforma de seguridad de endpoints de Windows permitirá ejecutar soluciones de seguridad fuera del kernel (disponibilidad no confirmada). Para cargas críticas recomienda zonas y regiones de disponibilidad.
- **Capacidades Microsoft:** Windows Resiliency Initiative (Quick Machine Recovery); zonas de disponibilidad de Azure; Azure Service Health
- **Cruce de marcos:** NIST — CSF GV.SC · RC.RP · PR.IR | CIS — CIS 15 · CIS 11 | The Open Group — sin referencia directa | ISACA — COBIT DSS04 · APO10 | CSA — CCM BCR · STA · IPY | MCSB — BR
- **Anclaje y COE:** Atlas — RISK / Recuperar | TheNextCISO — CISO-OS (gobierno) | SAF — Estrategia, integración y gobierno | COE — Riesgo, cumplimiento y aseguramiento | Responsable sugerido — CIO + Continuidad | Ola 2 (90–180 días) | relevante para el directorio

### A08 — Operaciones de seguridad: detección, respuesta y caza

*Ver, decidir y contener a la velocidad a la que operan los atacantes.*

#### A08.1 · ¿Qué cobertura de telemetría tiene el SOC (identidad, endpoint, correo, nube, SaaS, datos, red, OT) y qué puntos ciegos aceptamos de forma consciente?

- **Por qué importa:** Los atacantes se esconden en la actividad legítima; sin telemetría correlacionada, ese camuflaje funciona.
- **Buena práctica (evidencia esperada):** Mapa de fuentes por dominio con cobertura medida y puntos ciegos documentados y aceptados por la autoridad correspondiente.
- **Postura de Microsoft:** Microsoft unifica XDR y SIEM en el portal de Defender (Microsoft Sentinel está disponible allí incluso sin Defender XDR; el portal de Azure se retira el 31 de marzo de 2027) y ofrece el lago de datos de Sentinel, disponible de forma general desde septiembre de 2025, para retener telemetría a gran escala.
- **Capacidades Microsoft:** Microsoft Defender XDR; Microsoft Sentinel (incluido el lago de datos); plataforma unificada de operaciones de seguridad
- **Cruce de marcos:** NIST — CSF DE.CM | CIS — CIS 8 · CIS 13 | The Open Group — sin referencia directa | ISACA — COBIT DSS05 · DSS01 | CSA — CCM LOG | MCSB — LT
- **Anclaje y COE:** Atlas — TECHNOLOGY / Anticipar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Operaciones de seguridad (SecOps/SOC) | COE — Operaciones, detección y respuesta | Responsable sugerido — Líder SOC | Ola 0 (0–30 días)

#### A08.2 · ¿Cuáles son nuestros tiempos de detección, contención y recuperación para incidentes graves, y cómo evolucionan?

- **Por qué importa:** El daño de un incidente crece con el tiempo de permanencia del atacante; sin medir, no hay mejora.
- **Buena práctica (evidencia esperada):** Métricas por severidad con línea base, metas, tendencia trimestral y análisis de causa raíz de los incidentes mayores.
- **Postura de Microsoft:** Microsoft resume la meta en encontrar y expulsar rápido a los atacantes (reducir el tiempo de permanencia) y bloquear los ataques baratos y fáciles; SAF propone el tiempo de recuperación y el tiempo medio de remediación como métricas centrales.
- **Capacidades Microsoft:** Interrupción automática de ataques (Defender XDR); Microsoft Sentinel; Microsoft Security Copilot
- **Cruce de marcos:** NIST — CSF DE.AE · RS.MI · ID.IM | CIS — CIS 17 | The Open Group — sin referencia directa | ISACA — COBIT DSS02 · MEA01 | CSA — CCM SEF | MCSB — IR
- **Anclaje y COE:** Atlas — TECHNOLOGY / Contener | TheNextCISO — CISO-MM (madurez) | SAF — Operaciones de seguridad (SecOps/SOC) | COE — Operaciones, detección y respuesta | Responsable sugerido — Líder SOC | Ola 0 (0–30 días) | relevante para el directorio

#### A08.3 · ¿Qué acciones de contención están automatizadas, cuáles requieren aprobación humana y quién decide ese límite?

- **Por qué importa:** La automatización sin límites puede provocar interrupciones; la aprobación manual para todo llega tarde.
- **Buena práctica (evidencia esperada):** Catálogo de acciones con su nivel de autonomía, criterios basados en impacto y reversibilidad, registro de cada ejecución y revisión periódica.
- **Postura de Microsoft:** La interrupción automática de ataques de Defender XDR contiene activos comprometidos cuando la confianza es igual o superior al 99 %, con acciones reversibles; está disponible para Entra ID y Active Directory, y en versión preliminar para otros proveedores de identidad.
- **Capacidades Microsoft:** Interrupción automática de ataques (Defender XDR); playbooks de Microsoft Sentinel; agentes de Security Copilot
- **Cruce de marcos:** NIST — CSF RS.MI · RS.MA | CIS — CIS 17 | The Open Group — sin referencia directa | ISACA — COBIT DSS02 · DSS05 | CSA — CCM SEF | MCSB — IR
- **Anclaje y COE:** Atlas — ORGANIZATION / Contener | TheNextCISO — CISO-DO (operación de dominios) | SAF — Operaciones de seguridad (SecOps/SOC) | COE — Operaciones, detección y respuesta | Responsable sugerido — Líder SOC + CISO | Ola 1 (30–90 días)

#### A08.4 · ¿Tenemos un plan de respuesta a incidentes vigente y ensayado con la dirección, legal, comunicación y proveedores?

- **Por qué importa:** En una crisis no hay tiempo para definir roles, autoridades ni mensajes.
- **Buena práctica (evidencia esperada):** Plan alineado a SP 800-61 Rev. 3, roles y autoridades claros, contactos externos validados, ejercicios al menos anuales y mejoras registradas.
- **Postura de Microsoft:** La guía de respuesta a incidentes de Microsoft pide tener un plan probado, no causar daño adicional durante la respuesta, involucrar a Legal desde el inicio y acotar la recuperación; Microsoft ofrece además servicios de respuesta para incidentes graves.
- **Capacidades Microsoft:** Guía de respuesta a incidentes de Microsoft (Microsoft Learn); Microsoft Incident Response
- **Cruce de marcos:** NIST — SP 800-61 Rev. 3 · CSF RS.MA · RS.CO | CIS — CIS 17 (17.1–17.7) | The Open Group — sin referencia directa | ISACA — COBIT DSS02 · DSS04 | CSA — CCM SEF | MCSB — IR
- **Anclaje y COE:** Atlas — ORGANIZATION / Contener | TheNextCISO — CISO-DO (operación de dominios) | SAF — Operaciones de seguridad (SecOps/SOC) | COE — Operaciones, detección y respuesta | Responsable sugerido — CISO | Ola 0 (0–30 días) | relevante para el directorio | pregunta prioritaria para el directorio

#### A08.5 · ¿Gestionamos la detección como una disciplina de ingeniería guiada por inteligencia de amenazas (casos de uso basados en técnicas de ataque, cacería por hipótesis, pruebas, cobertura y mejora continua), o la inteligencia solo enriquece alertas?

- **Por qué importa:** Las reglas que nadie prueba se degradan, la cobertura real suele ser menor que la supuesta y la inteligencia que no cambia decisiones es un costo sin retorno.
- **Buena práctica (evidencia esperada):** Requerimientos de inteligencia definidos con el negocio; backlog de detecciones priorizado por amenazas y mapeado a MITRE ATT&CK; cacerías basadas en hipótesis; pruebas automatizadas y métricas de calidad (precisión y cobertura); resultados que modifican controles y prioridades.
- **Postura de Microsoft:** SAF asigna a la ingeniería de detección la tarea de traducir hipótesis sobre el adversario en detecciones automatizadas, y Microsoft ofrece mapeo de cobertura frente a MITRE ATT&CK. Su inteligencia de amenazas está integrada en el portal de Defender sin costo adicional (el portal independiente de Defender Threat Intelligence se retiró el 1 de agosto de 2026), con un agente de informes de inteligencia de amenazas disponible de forma general.
- **Capacidades Microsoft:** Reglas de análisis de Microsoft Sentinel; detecciones personalizadas de Defender XDR; cobertura MITRE ATT&CK en Sentinel; inteligencia de amenazas en el portal de Microsoft Defender; Threat Intelligence Briefing Agent (Security Copilot)
- **Cruce de marcos:** NIST — CSF DE.AE · ID.IM · ID.RA | CIS — CIS 8 (8.11) · CIS 13 | The Open Group — sin referencia directa | ISACA — COBIT DSS05 · BAI08 · APO12 | CSA — CCM LOG · TVM | MCSB — LT
- **Versión 2.0:** Integra la antigua A08.6 (fusión dentro del dominio).
- **Anclaje y COE:** Atlas — TECHNOLOGY / Anticipar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Operaciones de seguridad (SecOps/SOC) | COE — Operaciones, detección y respuesta | Responsable sugerido — Ingeniería de detección + inteligencia de amenazas | Ola 2 (90–180 días)

#### A08.6 · ¿Qué incidentes y configuraciones erróneas del último año se explican, al menos en parte, por falta de habilidades, y qué cambiamos en consecuencia (formación, automatización, valores seguros por defecto)?

- **Por qué importa:** La escasez de habilidades ya no es solo un problema de contratación: produce consecuencias concretas, como sistemas mal configurados, que el análisis de causa raíz suele atribuir a la tecnología o al proceso.
- **Buena práctica (evidencia esperada):** Análisis de causa raíz que registra el factor habilidades; tendencia de configuraciones erróneas por plataforma; acciones que combinan formación basada en roles, automatización y valores seguros por defecto; vínculo explícito con el plan de talento (A11.3).
- **Postura de Microsoft:** Microsoft reduce la dependencia de habilidades escasas con configuraciones seguras por defecto —principio de SFI que Baseline Security Mode aplica en Microsoft 365— y, en SFI, convirtió la seguridad en una prioridad central para todos sus empleados, con formación obligatoria y evaluación en el desempeño individual.
- **Capacidades Microsoft:** Baseline Security Mode (Microsoft 365); Microsoft Secure Score; recomendaciones de Microsoft Defender for Cloud
- **Cruce de marcos:** NIST — CSF RS.AN · ID.IM · PR.AT | CIS — CIS 14 · CIS 4 | The Open Group — sin referencia directa | ISACA — COBIT DSS03 · APO07 | CSA — CCM HRS · SEF | MCSB — IR · PV
- **Versión 2.0:** Pregunta nueva (proceso inverso, pareja IC07). El contenido de la antigua A08.6 se integró en A08.5.
- **Anclaje y COE:** Atlas — ORGANIZATION / Anticipar | TheNextCISO — CISO-MM (madurez) | SAF — Operaciones de seguridad (SecOps/SOC) | COE — Cultura, talento y adopción | Responsable sugerido — CISO + líderes de plataforma y operaciones | Ola 2 (90–180 días)

#### A08.7 · ¿Qué retención y calidad de registros necesitamos para investigaciones forenses, obligaciones regulatorias y caza retrospectiva, y a qué costo?

- **Por qué importa:** Muchas investigaciones fracasan porque los registros necesarios no se recolectaron o ya se borraron.
- **Buena práctica (evidencia esperada):** Requisitos de retención por fuente y obligación, niveles de almacenamiento según costo y pruebas periódicas de reconstrucción.
- **Postura de Microsoft:** Microsoft propone separar la telemetría de análisis activo de la retención de largo plazo en el lago de datos de Sentinel (disponible de forma general desde septiembre de 2025) y extender la auditoría de Microsoft 365 según la necesidad.
- **Capacidades Microsoft:** Microsoft Sentinel (lago de datos); Microsoft Purview Audit
- **Cruce de marcos:** NIST — CSF DE.CM · RS.AN | CIS — CIS 8 (8.1, 8.10) | The Open Group — sin referencia directa | ISACA — COBIT DSS05 · MEA03 | CSA — CCM LOG · SEF | MCSB — LT
- **Anclaje y COE:** Atlas — TECHNOLOGY / Recuperar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Operaciones de seguridad (SecOps/SOC) | COE — Operaciones, detección y respuesta | Responsable sugerido — Líder SOC + Compliance | Ola 1 (30–90 días)

#### A08.8 · ¿Cómo está organizado el SOC (roles, niveles, turnos, servicios gestionados) y cómo cuidamos la carga y el desgaste del equipo?

- **Por qué importa:** El agotamiento de los analistas degrada la calidad de la detección y aumenta la rotación.
- **Buena práctica (evidencia esperada):** Roles definidos, carga medida por analista, automatización de tareas repetitivas, rotación de turnos y plan de carrera.
- **Postura de Microsoft:** SAF define los roles de operaciones de seguridad (clasificación, investigación, caza, ingeniería de detección, inteligencia, coordinación de incidentes) e incluye el bienestar y la carrera del equipo entre las responsabilidades del gerente del SOC.
- **Capacidades Microsoft:** SAF (roles de SecOps); Microsoft Security Copilot
- **Cruce de marcos:** NIST — CSF GV.RR · DE.AE | CIS — CIS 17 (17.1) | The Open Group — Roles de seguridad (borrador citado por SAF) | ISACA — COBIT APO07 · DSS01 | CSA — CCM HRS · SEF | MCSB — IR
- **Anclaje y COE:** Atlas — ORGANIZATION / Gobernar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Operaciones de seguridad (SecOps/SOC) | COE — Cultura, talento y adopción | Responsable sugerido — Líder SOC | Ola 1 (30–90 días)

#### A08.9 · ¿Hemos definido cómo interactuamos con los CERT nacionales, reguladores, fuerzas de seguridad y pares sectoriales durante un incidente?

- **Por qué importa:** La coordinación externa improvisada retrasa la contención y puede incumplir obligaciones de notificación.
- **Buena práctica (evidencia esperada):** Contactos y acuerdos vigentes, criterios y plazos de notificación por regulador y participación en comunidades sectoriales de intercambio.
- **Postura de Microsoft:** Microsoft considera la colaboración con proveedores, CERT y pares sectoriales parte de una defensa continua e integrada, y publica inteligencia de amenazas para la comunidad.
- **Capacidades Microsoft:** Microsoft Threat Intelligence (publicaciones); Microsoft Digital Defense Report
- **Cruce de marcos:** NIST — CSF RS.CO · GV.OC | CIS — CIS 17 (17.2) | The Open Group — sin referencia directa | ISACA — COBIT DSS02 · MEA03 | CSA — CCM SEF | MCSB — IR
- **Anclaje y COE:** Atlas — TRUST / Contener | TheNextCISO — CISO-OS (gobierno) | SAF — Operaciones de seguridad (SecOps/SOC) | COE — Operaciones, detección y respuesta | Responsable sugerido — CISO + Legal | Ola 1 (30–90 días)

### A09 — Resiliencia, continuidad, recuperación y crisis

*Sostener los resultados del negocio cuando la prevención falla.*

#### A09.1 · ¿Cuáles son nuestras funciones críticas de negocio, sus tolerancias de interrupción y sus dependencias tecnológicas y de terceros?

- **Por qué importa:** La resiliencia se mide por la capacidad de sostener resultados de negocio, no por la recuperación de servidores.
- **Buena práctica (evidencia esperada):** Análisis de impacto vigente con tolerancias aprobadas por el negocio, mapa de dependencias (incluidos identidad y terceros) y revisión anual.
- **Postura de Microsoft:** Microsoft plantea la resiliencia como una disciplina de liderazgo: conocer los servicios críticos y sus dependencias, diseñar la continuidad antes del incidente y poder operar en modo degradado.
- **Capacidades Microsoft:** Microsoft Digital Defense Report; guía de resiliencia de Azure (Well-Architected Framework)
- **Cruce de marcos:** NIST — CSF GV.OC · ID.AM · PR.IR | CIS — CIS 11 (11.1) | The Open Group — TOGAF Fase B | ISACA — COBIT DSS04 · BAI04 | CSA — CCM BCR | MCSB — BR
- **Anclaje y COE:** Atlas — RISK / Recuperar | TheNextCISO — CISO-OS (gobierno) | SAF — Estrategia, integración y gobierno | COE — Riesgo, cumplimiento y aseguramiento | Responsable sugerido — Continuidad + Dueños de negocio | Ola 1 (30–90 días) | relevante para el directorio

#### A09.2 · ¿Podemos recuperar identidad, datos y servicios críticos tras un ransomware destructivo, y cuándo lo probamos de punta a punta por última vez?

- **Por qué importa:** Casi todas las organizaciones tienen copias; pocas tienen la capacidad probada de recuperar en el orden correcto.
- **Buena práctica (evidencia esperada):** Plan de recuperación ordenado por dependencias (la identidad primero), pruebas completas al menos anuales y tiempos medidos frente a las tolerancias.
- **Postura de Microsoft:** La guía de Microsoft contra el ransomware operado por humanos tiene tres fases: preparar un plan para recuperarse sin pagar, limitar el alcance del daño protegiendo los roles privilegiados y dificultar el acceso inicial.
- **Capacidades Microsoft:** Guía de protección contra ransomware operado por humanos (Microsoft Learn); Microsoft 365 Backup; Azure Backup
- **Cruce de marcos:** NIST — CSF RC.RP · PR.IR | CIS — CIS 11 (11.5) | The Open Group — sin referencia directa | ISACA — COBIT DSS04 | CSA — CCM BCR | MCSB — BR
- **Anclaje y COE:** Atlas — TECHNOLOGY / Recuperar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Seguridad de infraestructura | COE — Operaciones, detección y respuesta | Responsable sugerido — CIO + CISO | Ola 0 (0–30 días) | relevante para el directorio | pregunta prioritaria para el directorio

#### A09.3 · ¿Nuestras copias de seguridad son inmutables, aisladas, cifradas y están protegidas frente a administradores comprometidos?

- **Por qué importa:** Los atacantes buscan y destruyen las copias antes de cifrar; un administrador comprometido puede borrarlas.
- **Buena práctica (evidencia esperada):** Copias inmutables o aisladas lógicamente, autorización de varios usuarios para operaciones destructivas, cifrado y monitoreo de intentos de borrado.
- **Postura de Microsoft:** Microsoft ofrece almacenes de copias inmutables, eliminación temporal y autorización de varios usuarios para proteger las copias frente a borrados maliciosos.
- **Capacidades Microsoft:** Azure Backup (almacenes inmutables, eliminación temporal, autorización de varios usuarios); Microsoft 365 Backup
- **Cruce de marcos:** NIST — CSF PR.DS · PR.IR | CIS — CIS 11 (11.3, 11.4) | The Open Group — sin referencia directa | ISACA — COBIT DSS04 · DSS05 | CSA — CCM BCR · CEK | MCSB — BR
- **Anclaje y COE:** Atlas — TECHNOLOGY / Recuperar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Seguridad de infraestructura | COE — Plataforma e ingeniería de controles | Responsable sugerido — Infraestructura | Ola 0 (0–30 días)

#### A09.4 · ¿Tenemos un plan para recuperar el proveedor de identidad y operar si este falla o queda comprometido?

- **Por qué importa:** Sin identidad no hay acceso a nada, ni siquiera a las herramientas de recuperación.
- **Buena práctica (evidencia esperada):** Procedimiento de recuperación de Active Directory y de la identidad en la nube documentado y ensayado, cuentas de emergencia y canales alternativos de administración.
- **Postura de Microsoft:** Microsoft publica la guía de recuperación de bosques de Active Directory y recomienda cuentas de acceso de emergencia y planes de resiliencia de la identidad.
- **Capacidades Microsoft:** Guía de recuperación de bosques de Active Directory; cuentas de acceso de emergencia de Microsoft Entra
- **Cruce de marcos:** NIST — CSF RC.RP · PR.AA | CIS — CIS 11 · CIS 5 | The Open Group — sin referencia directa | ISACA — COBIT DSS04 | CSA — CCM BCR · IAM | MCSB — BR · IM
- **Anclaje y COE:** Atlas — TECHNOLOGY / Recuperar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Acceso e identidad | COE — Plataforma e ingeniería de controles | Responsable sugerido — IAM + Infraestructura | Ola 1 (30–90 días)

#### A09.5 · ¿Cómo se gestiona una crisis cibernética: comité, roles, decisiones difíciles (incluido el pago de rescates), comunicación y notificaciones?

- **Por qué importa:** Las decisiones más graves de una crisis no son técnicas y se toman con información incompleta.
- **Buena práctica (evidencia esperada):** Comité de crisis con autoridades definidas, criterios acordados de antemano para las decisiones críticas, asesoría legal y plantillas de comunicación por audiencia.
- **Postura de Microsoft:** La guía de Microsoft contra el ransomware propone prepararse para recuperar sin pagar el rescate; en el modelo de responsabilidades de SAF, el CEO toma la decisión final en situaciones de alta consecuencia, y los roles y planes se definen antes de la emergencia.
- **Capacidades Microsoft:** SAF (responsabilidades); guía de respuesta a incidentes de Microsoft
- **Cruce de marcos:** NIST — CSF RS.MA · RS.CO · RC.CO | CIS — CIS 17 | The Open Group — sin referencia directa | ISACA — COBIT DSS02 · DSS04 · EDM03 | CSA — CCM SEF · BCR | MCSB — IR
- **Anclaje y COE:** Atlas — ORGANIZATION / Contener | TheNextCISO — CISO-OS (gobierno) | SAF — Estrategia, integración y gobierno | COE — Gobierno, políticas y decisiones | Responsable sugerido — CEO + CISO + Legal | Ola 1 (30–90 días) | relevante para el directorio | pregunta prioritaria para el directorio

#### A09.6 · ¿Cuándo fue el último ejercicio de crisis con el comité ejecutivo y qué cambió como resultado?

- **Por qué importa:** Un ejercicio que no produce cambios es un evento, no una prueba.
- **Buena práctica (evidencia esperada):** Ejercicios anuales con escenarios realistas, hallazgos con dueño y fecha, y verificación de su cierre en el ejercicio siguiente.
- **Postura de Microsoft:** SAF incluye los ejercicios de mesa dentro de la simulación de ataques y recomienda integrar los aprendizajes en seguridad, tecnología y otros procesos.
- **Capacidades Microsoft:** SAF (simulación de ataques y ejercicios)
- **Cruce de marcos:** NIST — CSF ID.IM · RC.RP | CIS — CIS 17 (17.7) | The Open Group — sin referencia directa | ISACA — COBIT DSS04 · MEA01 | CSA — CCM BCR · SEF | MCSB — IR
- **Anclaje y COE:** Atlas — RISK / Recuperar | TheNextCISO — CISO-MM (madurez) | SAF — Estrategia, integración y gobierno | COE — Gobierno, políticas y decisiones | Responsable sugerido — CISO | Ola 1 (30–90 días) | relevante para el directorio

#### A09.7 · ¿Cómo aseguramos la resiliencia de endpoints y servidores ante fallas masivas (por ejemplo, una actualización defectuosa) y no solo ante ataques?

- **Por qué importa:** Una falla accidental de gran escala puede detener la operación igual que un ataque.
- **Buena práctica (evidencia esperada):** Despliegue escalonado de actualizaciones, anillos de prueba, capacidad de recuperación remota de dispositivos y plan de reversión.
- **Postura de Microsoft:** La Windows Resiliency Initiative incorpora Quick Machine Recovery (disponible desde julio de 2025 en Windows 11 24H2), que recupera equipos que no arrancan, y Windows 11 carga por defecto solo controladores firmados; la ejecución de soluciones de seguridad fuera del kernel no tiene disponibilidad confirmada.
- **Capacidades Microsoft:** Windows Resiliency Initiative (Quick Machine Recovery); Windows Autopatch (anillos de despliegue)
- **Cruce de marcos:** NIST — CSF PR.IR · RC.RP | CIS — CIS 4 · CIS 11 | The Open Group — sin referencia directa | ISACA — COBIT BAI06 · DSS04 | CSA — CCM BCR · CCC | MCSB — BR · ES
- **Anclaje y COE:** Atlas — TECHNOLOGY / Recuperar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Seguridad de infraestructura | COE — Plataforma e ingeniería de controles | Responsable sugerido — Infraestructura | Ola 2 (90–180 días)

#### A09.8 · ¿Podemos operar los procesos críticos con mecanismos manuales o alternativos durante varios días?

- **Por qué importa:** Algunas crisis duran semanas; la continuidad no puede depender de que la tecnología vuelva rápido.
- **Buena práctica (evidencia esperada):** Procedimientos alternativos documentados y ensayados para los procesos críticos, con capacidad y duración conocidas.
- **Postura de Microsoft:** Microsoft incluye la capacidad de operar en modo degradado entre los componentes de la resiliencia (conocer servicios críticos, aislar fallas, sostener la operación).
- **Cruce de marcos:** NIST — CSF RC.RP · GV.OC | CIS — sin referencia directa | The Open Group — TOGAF Fase B | ISACA — COBIT DSS04 · DSS06 | CSA — CCM BCR | MCSB — BR
- **Anclaje y COE:** Atlas — RISK / Recuperar | TheNextCISO — CISO-OS (gobierno) | SAF — Estrategia, integración y gobierno | COE — Riesgo, cumplimiento y aseguramiento | Responsable sugerido — Dueños de negocio + Continuidad | Ola 2 (90–180 días) | relevante para el directorio

#### A09.9 · ¿Convertimos los incidentes, cuasi incidentes y ejercicios en cambios de arquitectura verificados?

- **Por qué importa:** Recuperarse es resiliencia; aprender y cambiar el diseño es lo que evita la repetición.
- **Buena práctica (evidencia esperada):** Revisiones posteriores sin búsqueda de culpables, acciones con dueño, cambios de arquitectura verificados y seguimiento en el comité.
- **Postura de Microsoft:** Microsoft documenta públicamente los aprendizajes de SFI y los traduce en patrones y prácticas reutilizables; SAF exige retroalimentación, colaboración y mejora continua.
- **Capacidades Microsoft:** Secure Future Initiative (patrones y prácticas); SAF
- **Cruce de marcos:** NIST — CSF ID.IM · RC.RP | CIS — CIS 17 (17.8) | The Open Group — TOGAF Fase H | ISACA — COBIT DSS03 · BAI08 | CSA — CCM SEF | MCSB — IR
- **Anclaje y COE:** Atlas — RISK / Recuperar | TheNextCISO — CISO-MM (madurez) | SAF — Arquitectura de seguridad de extremo a extremo | COE — Arquitectura y patrones seguros | Responsable sugerido — CISO + Arquitectura | Ola 2 (90–180 días)

### A10 — Cumplimiento, regulación y aseguramiento continuo

*Demostrar con evidencia, de forma continua y reutilizable, que los controles funcionan.*

#### A10.1 · ¿Qué obligaciones legales, regulatorias y contractuales de seguridad nos aplican por país y sector, incluidas las de resiliencia operativa digital que nos alcanzan directa o indirectamente (DORA, NIS2 o normas locales), y quién mantiene ese mapa y el plan para cumplirlas?

- **Por qué importa:** Las obligaciones cambian rápido y difieren entre países; muchas regulaciones extranjeras alcanzan a filiales, proveedores o clientes de la región, y desconocerlas no exime de cumplirlas.
- **Buena práctica (evidencia esperada):** Registro de obligaciones con fuente, jurisdicción, fecha y responsable, revisado periódicamente con Legal; análisis de aplicabilidad por entidad para cada regulación nueva, con brechas priorizadas y plan con responsables y plazos.
- **Postura de Microsoft:** Microsoft ofrece plantillas de evaluación regulatoria en Compliance Manager —incluidas plantillas premium para la Ley de Resiliencia Operativa Digital (DORA) y la Directiva NIS2; las licencias E5 incluyen tres plantillas premium— y documenta en el Service Trust Portal cómo sus servicios apoyan esas regulaciones.
- **Capacidades Microsoft:** Microsoft Purview Compliance Manager; Service Trust Portal
- **Cruce de marcos:** NIST — CSF GV.OC · GV.SC | CIS — sin referencia directa | The Open Group — TOGAF Gestión de requisitos | ISACA — COBIT MEA03 | CSA — CCM GRC · A&A · STA | MCSB — GS
- **Versión 2.0:** Integra la antigua A10.7 (fusión dentro del dominio).
- **Anclaje y COE:** Atlas — TRUST / Gobernar | TheNextCISO — CISO-OS (gobierno) | SAF — Estrategia, integración y gobierno | COE — Riesgo, cumplimiento y aseguramiento | Responsable sugerido — Compliance + Legal | Ola 0 (0–30 días) | relevante para el directorio

#### A10.2 · ¿Cómo convertimos varios marcos y regulaciones en un único conjunto de controles con evidencia reutilizable?

- **Por qué importa:** Gestionar cada marco por separado multiplica auditorías y esfuerzo sin mejorar la seguridad.
- **Buena práctica (evidencia esperada):** Catálogo de controles comunes con mapeo a cada marco, evidencia recolectada una vez y reutilizada, y dueño por control.
- **Postura de Microsoft:** Microsoft publica correspondencias entre Microsoft Cloud Security Benchmark y marcos como CIS Controls y NIST SP 800-53, y Compliance Manager reutiliza acciones de mejora entre evaluaciones.
- **Capacidades Microsoft:** Microsoft Cloud Security Benchmark (correspondencias); Microsoft Purview Compliance Manager
- **Cruce de marcos:** NIST — CSF (referencias informativas) · SP 800-53 Rev. 5 | CIS — CIS Controls v8.1 (correspondencias oficiales) | The Open Group — TOGAF Gestión de requisitos | ISACA — COBIT MEA02 · MEA03 | CSA — CCM v4.1 (correspondencias) | MCSB — GS
- **Anclaje y COE:** Atlas — TRUST / Gobernar | TheNextCISO — CISO-OS (gobierno) | SAF — Estrategia, integración y gobierno | COE — Riesgo, cumplimiento y aseguramiento | Responsable sugerido — GRC | Ola 1 (30–90 días)

#### A10.3 · ¿Cuánta de nuestra evidencia de cumplimiento es automática y continua, cuánta depende de muestreos manuales y qué podríamos entregar en 48 horas a un regulador o auditor sobre un incidente o un control específico?

- **Por qué importa:** La recolección manual de evidencia consume capacidad y solo muestra el pasado; reconstruirla bajo presión genera errores, y la capacidad de demostrar es parte del cumplimiento.
- **Buena práctica (evidencia esperada):** Porcentaje de controles con evidencia automatizada y monitoreo continuo de desvíos; paquetes de evidencia predefinidos con registros íntegros y retención suficiente; simulacros de requerimiento; auditorías que reutilizan esa evidencia.
- **Postura de Microsoft:** Compliance Manager y Defender for Cloud permiten evaluar controles de forma continua y automatizada contra marcos regulatorios; Microsoft Purview Audit y eDiscovery, junto con Microsoft Sentinel, permiten preservar y exportar evidencia con cadena de custodia.
- **Capacidades Microsoft:** Microsoft Purview Compliance Manager (pruebas automatizadas); Microsoft Defender for Cloud (cumplimiento normativo); Microsoft Purview Audit; Microsoft Purview eDiscovery; Microsoft Sentinel
- **Cruce de marcos:** NIST — CSF GV.OV · ID.IM · RS.CO | CIS — CIS 8 | The Open Group — sin referencia directa | ISACA — COBIT MEA02 · MEA03 · MEA04 · DSS02 | CSA — CCM A&A · SEF | MCSB — GS · PV · LT · IR
- **Versión 2.0:** Integra la antigua A10.6 (fusión dentro del dominio).
- **Anclaje y COE:** Atlas — TRUST / Gobernar | TheNextCISO — CISO-OS (gobierno) | SAF — Gestión de la postura de seguridad | COE — Riesgo, cumplimiento y aseguramiento | Responsable sugerido — GRC + SOC | Ola 2 (90–180 días)

#### A10.4 · ¿Cómo se coordinan las líneas de aseguramiento (operación, riesgo, auditoría interna, revisores externos) para no duplicar esfuerzos ni dejar vacíos?

- **Por qué importa:** Sin coordinación se audita lo mismo varias veces mientras los riesgos nuevos quedan sin revisar.
- **Buena práctica (evidencia esperada):** Mapa de aseguramiento por riesgo y control, plan anual coordinado e independencia preservada.
- **Postura de Microsoft:** Silencio: Microsoft no publica un modelo propio de líneas de aseguramiento para clientes; su evidencia de cumplimiento (Service Trust Portal) alimenta la revisión de terceros.
- **Capacidades Microsoft:** Service Trust Portal
- **Cruce de marcos:** NIST — CSF GV.OV | CIS — sin referencia directa | The Open Group — sin referencia directa | ISACA — COBIT MEA04 · MEA02 | CSA — CCM A&A | MCSB — GS
- **Anclaje y COE:** Atlas — TRUST / Gobernar | TheNextCISO — CISO-MM (madurez) | SAF — Estrategia, integración y gobierno | COE — Riesgo, cumplimiento y aseguramiento | Responsable sugerido — Auditoría interna + CRO | Ola 2 (90–180 días) | relevante para el directorio

#### A10.5 · ¿Cómo gestionamos las excepciones a las políticas: quién las aprueba, por cuánto tiempo, con qué controles compensatorios y cómo se cierran?

- **Por qué importa:** Las excepciones son necesarias; las excepciones sin control son la forma más común de erosión del gobierno.
- **Buena práctica (evidencia esperada):** Flujo de excepciones con autoridad, vencimiento máximo, controles compensatorios, inventario visible y tasa de cierre a tiempo.
- **Postura de Microsoft:** Las herramientas de Microsoft permiten registrar exenciones con justificación y fecha de vencimiento (por ejemplo, en Defender for Cloud) para que las excepciones sean visibles y temporales.
- **Capacidades Microsoft:** Microsoft Defender for Cloud (exenciones); Microsoft Defender Vulnerability Management (excepciones)
- **Cruce de marcos:** NIST — CSF GV.PO · GV.RM | CIS — sin referencia directa | The Open Group — TOGAF Gobierno de arquitectura (dispensas) | ISACA — COBIT APO01 · APO12 | CSA — CCM GRC | MCSB — GS
- **Anclaje y COE:** Atlas — TRUST / Gobernar | TheNextCISO — CISO-OS (gobierno) | SAF — Estrategia, integración y gobierno | COE — Gobierno, políticas y decisiones | Responsable sugerido — CISO + GRC | Ola 1 (30–90 días)

#### A10.6 · ¿Qué versiones de los marcos de referencia usamos (COBIT, NIST, ISO, CIS, CCM) y qué plan de transición tenemos antes de que se retiren, empezando por COBIT 2019?

- **Por qué importa:** Un catálogo de controles anclado en versiones retiradas produce auditorías y certificaciones sobre referencias que ya no rigen; COBIT 7 se lanza el 19 de noviembre de 2026 y COBIT 2019 se retira el 31 de diciembre de 2027.
- **Buena práctica (evidencia esperada):** Inventario de marcos y versiones en uso, con dueño y fecha de revisión; plan de transición con hitos, impacto en el catálogo unificado de controles (A10.2) y licencias necesarias; seguimiento de los retiros anunciados por cada organismo.
- **Postura de Microsoft:** Compliance Manager mantiene plantillas por versión y conserva versiones anteriores junto a las vigentes (por ejemplo, ISO/IEC 27001:2013 y 2022, NIST SP 800-53 rev. 4 y rev. 5, NIST CSF y CSF 2.0, PCI DSS v3.2.1 y v4.0), y las actualiza cuando cambia la norma de base: elegir la versión vigente es decisión de la organización. Silencio: la lista publicada (última actualización, 6 de marzo de 2025) incluye COBIT 5, retirado por ISACA el 26 de octubre de 2026, y no incluye COBIT 2019 ni COBIT 7.
- **Capacidades Microsoft:** Microsoft Purview Compliance Manager (plantillas por versión); Microsoft Cloud Security Benchmark (correspondencias)
- **Cruce de marcos:** NIST — CSF GV.PO · ID.IM | CIS — sin referencia directa | The Open Group — TOGAF (10.ª edición) · Open FAIR (versiones vigentes y anunciadas) | ISACA — COBIT EDM01 · MEA03 · MEA04 | CSA — CCM GRC · A&A | MCSB — GS
- **Versión 2.0:** Pregunta nueva (proceso inverso, pareja IS05). El contenido de la antigua A10.6 se integró en A10.3.
- **Anclaje y COE:** Atlas — TRUST / Gobernar | TheNextCISO — CISO-OS (gobierno) | SAF — Estrategia, integración y gobierno | COE — Riesgo, cumplimiento y aseguramiento | Responsable sugerido — GRC + auditoría interna | Ola 1 (30–90 días) | relevante para el directorio

#### A10.7 · ¿Quién valida de forma independiente el modelo con el que cuantificamos el riesgo cibernético, y es lo bastante transparente, pertinente y simple para poder validarlo?

- **Por qué importa:** Las cifras de pérdida que llegan al directorio heredan los supuestos del modelo; un modelo opaco o sobredimensionado no puede auditarse y traslada su error a cada decisión.
- **Buena práctica (evidencia esperada):** Documentación del modelo, sus supuestos y sus fuentes de datos; validación independiente (auditoría interna, segunda línea o un tercero) con periodicidad definida; criterios de transparencia, pertinencia y parsimonia; registro de cambios del modelo.
- **Postura de Microsoft:** Silencio: Microsoft no publica un modelo de cuantificación financiera del riesgo cibernético ni criterios para validarlo; sus métricas de postura y exposición pueden alimentar un modelo, pero no lo reemplazan ni lo validan.
- **Cruce de marcos:** NIST — CSF GV.OV · GV.RM · IR 8286 | CIS — sin referencia directa | The Open Group — Open FAIR O-RA · O-RT | ISACA — COBIT MEA04 · APO12 · Risk IT | CSA — CCM A&A · GRC | MCSB — GS
- **Versión 2.0:** Pregunta nueva (proceso inverso, pareja OG09). El contenido de la antigua A10.7 se integró en A10.1.
- **Anclaje y COE:** Atlas — RISK / Gobernar | TheNextCISO — CISO-MM (madurez) | SAF — Estrategia, integración y gobierno | COE — Riesgo, cumplimiento y aseguramiento | Responsable sugerido — Auditoría interna + CRO | Ola 2 (90–180 días) | relevante para el directorio

#### A10.8 · ¿Cómo verificamos el cumplimiento de nuestros proveedores cloud y qué controles quedan siempre de nuestro lado?

- **Por qué importa:** Una certificación del proveedor no cubre los controles que debe operar el cliente.
- **Buena práctica (evidencia esperada):** Revisión anual de informes y certificaciones del proveedor, matriz de controles complementarios del cliente y evidencia de su operación.
- **Postura de Microsoft:** Microsoft publica informes de auditoría y certificaciones (por ejemplo, SOC, ISO/IEC 27001 y CSA STAR) en el Service Trust Portal, junto con las responsabilidades que corresponden al cliente.
- **Capacidades Microsoft:** Service Trust Portal; certificación CSA STAR de Azure
- **Cruce de marcos:** NIST — CSF GV.SC | CIS — CIS 15 (15.5) | The Open Group — sin referencia directa | ISACA — COBIT APO10 · MEA04 | CSA — CCM STA · A&A · DCS · STAR | MCSB — GS
- **Anclaje y COE:** Atlas — TRUST / Anticipar | TheNextCISO — CISO-OS (gobierno) | SAF — Estrategia, integración y gobierno | COE — Riesgo, cumplimiento y aseguramiento | Responsable sugerido — GRC + Compras | Ola 1 (30–90 días)

#### A10.9 · ¿Qué nivel de madurez queremos alcanzar por dominio y cómo medimos la distancia con evidencia y no con autoevaluaciones?

- **Por qué importa:** Las autoevaluaciones tienden a sobreestimar la madurez; sin perfil objetivo no hay dirección.
- **Buena práctica (evidencia esperada):** Perfil actual y objetivo por dominio, escala con criterios de evidencia, validación independiente de muestras y revisión anual.
- **Postura de Microsoft:** Microsoft usa escalas de madurez en sus marcos de adopción (Zero Trust, SAF) y recomienda medir el avance con evidencia de configuración y de operación.
- **Capacidades Microsoft:** Zero Trust Assessment; SAF / SCAP; Microsoft Secure Score
- **Cruce de marcos:** NIST — CSF perfiles y niveles (Tiers) · ID.IM | CIS — CIS IG1–IG3 | The Open Group — sin referencia directa | ISACA — COBIT (niveles de capacidad) · MEA01 | CSA — CCM v4.1 · STAR (niveles) | MCSB — GS
- **Anclaje y COE:** Atlas — TRUST / Gobernar | TheNextCISO — CISO-MM (madurez) | SAF — Estrategia, integración y gobierno | COE — Riesgo, cumplimiento y aseguramiento | Responsable sugerido — CISO | Ola 1 (30–90 días) | relevante para el directorio

### A11 — Personas, cultura, talento y sostenibilidad del rol

*Las personas que sostienen el programa, incluido el propio CISO.*

#### A11.1 · ¿Qué conductas de seguridad esperamos de cada rol, cómo medimos el cambio de comportamiento (no solo la finalización de cursos) y cómo reconocemos la reducción de riesgo y la adopción segura, en lugar de premiar solo la velocidad o el bloqueo?

- **Por qué importa:** Completar un curso no equivale a cambiar una conducta bajo presión, y los incentivos definen la conducta más que las políticas.
- **Buena práctica (evidencia esperada):** Conductas esperadas por rol, simulaciones realistas, métricas de reporte y de reincidencia; indicadores de adopción segura en los objetivos de los equipos, reconocimiento visible y revisión de los incentivos que premian atajos.
- **Postura de Microsoft:** Microsoft sostiene que la seguridad es parte del trabajo de todos y ofrece simulaciones de ataque y formación dirigida según el comportamiento observado; como parte de SFI, vinculó la seguridad a la evaluación de desempeño de sus empleados y a la compensación de su liderazgo.
- **Capacidades Microsoft:** Simulación de ataques de Microsoft Defender for Office 365; SAF; Secure Future Initiative
- **Cruce de marcos:** NIST — CSF PR.AT · GV.RR | CIS — CIS 14 | The Open Group — sin referencia directa | ISACA — COBIT APO07 · BAI05 · EDM01 | CSA — CCM HRS | MCSB — GS
- **Versión 2.0:** Integra la antigua A11.8 (fusión dentro del dominio).
- **Anclaje y COE:** Atlas — ORGANIZATION / Anticipar | TheNextCISO — CISO-OS (gobierno) | SAF — Estrategia, integración y gobierno | COE — Cultura, talento y adopción | Responsable sugerido — CISO + RR. HH. | Ola 1 (30–90 días) | relevante para el directorio

#### A11.2 · ¿Cómo preparamos a ejecutivos y áreas de alto riesgo (finanzas, tesorería, RR. HH., asistentes) frente a suplantaciones avanzadas, incluidas voz y video sintéticos?

- **Por qué importa:** Las suplantaciones con IA apuntan a quienes pueden autorizar pagos, accesos o cambios de datos.
- **Buena práctica (evidencia esperada):** Formación específica, protocolos de verificación fuera de banda para pedidos sensibles y ejercicios periódicos con escenarios realistas.
- **Postura de Microsoft:** SAF recomienda educar sobre la suplantación de voz, video y estilo de escritura con IA y establecer validación fuera de banda para las comunicaciones sensibles o sospechosas.
- **Capacidades Microsoft:** SAF; Microsoft Defender for Office 365
- **Cruce de marcos:** NIST — CSF PR.AT · PR.AA | CIS — CIS 14 (14.2) | The Open Group — sin referencia directa | ISACA — COBIT APO07 · DSS06 | CSA — CCM HRS | MCSB — GS
- **Anclaje y COE:** Atlas — ORGANIZATION / Anticipar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Estrategia, integración y gobierno | COE — Cultura, talento y adopción | Responsable sugerido — CISO + Finanzas | Ola 0 (0–30 días) | relevante para el directorio

#### A11.3 · ¿Tenemos un plan de talento de seguridad (brechas de habilidades, sucesión, rotación, carrera) y cómo usamos la IA para ampliar capacidades?

- **Por qué importa:** La escasez de talento es estructural; sin plan, cada renuncia abre una brecha de control.
- **Buena práctica (evidencia esperada):** Mapa de habilidades por rol, planes de sucesión para puestos críticos, presupuesto de formación y estrategia de automatización.
- **Postura de Microsoft:** SAF anticipa que los trabajos a realizar no cambian, pero el trabajo de seguridad sí: más carga por ataques y por la protección de la IA, y más eficiencia por automatización; Microsoft ofrece rutas de formación y certificación en Microsoft Learn.
- **Capacidades Microsoft:** Microsoft Learn (rutas y certificaciones de seguridad); Microsoft Security Copilot
- **Cruce de marcos:** NIST — CSF GV.RR · PR.AT | CIS — CIS 14 | The Open Group — Roles de seguridad (borrador citado por SAF) | ISACA — COBIT APO07 | CSA — CCM HRS | MCSB — GS
- **Anclaje y COE:** Atlas — ORGANIZATION / Gobernar | TheNextCISO — CISO-OS (gobierno) | SAF — Estrategia, integración y gobierno | COE — Cultura, talento y adopción | Responsable sugerido — CISO + RR. HH. | Ola 2 (90–180 días)

#### A11.4 · ¿Cómo prevenimos el desgaste del CISO y del equipo, qué indicadores de sostenibilidad observamos y cómo cultiva el CISO su criterio para decidir bajo incertidumbre (sesgos, diario de decisiones, disenso, mentores)?

- **Por qué importa:** Un rol con expectativas imposibles produce rotación, decisiones defensivas y pérdida de memoria institucional; y como las decisiones de seguridad se toman con información incompleta, el criterio es una capacidad que se cultiva.
- **Buena práctica (evidencia esperada):** Expectativas realistas acordadas con la dirección, cobertura de guardias, indicadores de carga y rotación, respaldo legal y de seguros para el rol; diario de decisiones con hipótesis y resultados, revisiones periódicas, espacios de disenso estructurado y red de pares.
- **Postura de Microsoft:** Silencio parcial: Microsoft no publica una guía específica sobre la sostenibilidad del rol del CISO ni sobre el desarrollo de su criterio; SAF asigna al gerente del SOC el bienestar y la carrera del equipo, promueve la automatización de tareas repetitivas y advierte no delegar el pensamiento crítico en la IA.
- **Capacidades Microsoft:** SAF; Microsoft Security Copilot
- **Cruce de marcos:** NIST — CSF GV.RR · ID.IM | CIS — sin referencia directa | The Open Group — sin referencia directa | ISACA — COBIT APO07 | CSA — CCM HRS | MCSB — GS
- **Versión 2.0:** Integra la antigua A11.9 (fusión dentro del dominio).
- **Anclaje y COE:** Atlas — SELF / Recuperar | TheNextCISO — CISO-OS (gobierno) | SAF — Estrategia, integración y gobierno | COE — Cultura, talento y adopción | Responsable sugerido — CEO + RR. HH. + CISO | Ola 2 (90–180 días) | relevante para el directorio

#### A11.5 · ¿La seguridad forma parte de la cultura de ingeniería y producto (referentes, revisiones de diseño, responsabilidad compartida)?

- **Por qué importa:** La seguridad que depende solo del equipo de seguridad no escala al ritmo del desarrollo.
- **Buena práctica (evidencia esperada):** Red de referentes de seguridad, revisiones de diseño integradas, objetivos de seguridad en los equipos de producto y reconocimiento de buenas prácticas.
- **Postura de Microsoft:** En SFI, Microsoft convirtió la seguridad en una prioridad central para todos sus empleados, con formación obligatoria y evaluación en el desempeño individual; el informe de progreso de julio de 2026 refuerza esas expectativas.
- **Capacidades Microsoft:** Secure Future Initiative; Security Development Lifecycle
- **Cruce de marcos:** NIST — CSF GV.RR · PR.AT | CIS — CIS 14 · CIS 16 | The Open Group — sin referencia directa | ISACA — COBIT APO07 · BAI05 | CSA — CCM HRS · AIS | MCSB — DS · GS
- **Anclaje y COE:** Atlas — ORGANIZATION / Limitar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Seguridad del desarrollo | COE — Cultura, talento y adopción | Responsable sugerido — CTO + CISO | Ola 2 (90–180 días)

#### A11.6 · ¿Cómo comunicamos el riesgo cibernético en lenguaje de negocio a cada audiencia (directorio, ejecutivos, empleados, clientes)?

- **Por qué importa:** Un riesgo bien analizado pero mal comunicado no cambia decisiones.
- **Buena práctica (evidencia esperada):** Mensajes y formatos por audiencia, pocas métricas con contexto, narrativa de escenarios y verificación de la comprensión.
- **Postura de Microsoft:** Microsoft recomienda traducir la seguridad a resultados de negocio (escenarios de Zero Trust, CISO Workshop) y usar las tendencias de amenazas como contexto para la dirección.
- **Capacidades Microsoft:** CISO Workshop; Microsoft Digital Defense Report
- **Cruce de marcos:** NIST — CSF GV.OV · GV.RR | CIS — sin referencia directa | The Open Group — Open FAIR O-RA (comunicación en términos financieros) | ISACA — COBIT EDM05 · APO08 | CSA — CCM GRC | MCSB — GS
- **Anclaje y COE:** Atlas — TRUST / Gobernar | TheNextCISO — CISO-NX (nueva generación) | SAF — Estrategia, integración y gobierno | COE — Valor, métricas y comunicación ejecutiva | Responsable sugerido — CISO | Ola 1 (30–90 días) | relevante para el directorio

#### A11.7 · ¿Qué capacidades críticas dependen de una sola persona o de un único proveedor, y cómo reducimos esa concentración?

- **Por qué importa:** La concentración de conocimiento o de autoridad es un punto único de falla y un riesgo de abuso.
- **Buena práctica (evidencia esperada):** Mapa de dependencias clave, documentación y suplencias, separación de funciones y rotación planificada.
- **Postura de Microsoft:** Microsoft recomienda la separación de funciones y el mínimo privilegio también en los roles administrativos y de seguridad (estrategia de acceso privilegiado).
- **Capacidades Microsoft:** Microsoft Entra Privileged Identity Management; Microsoft Entra ID Governance
- **Cruce de marcos:** NIST — CSF GV.RR · PR.AA | CIS — CIS 5 · CIS 6 | The Open Group — sin referencia directa | ISACA — COBIT APO07 · BAI08 | CSA — CCM HRS · IAM | MCSB — PA · GS
- **Anclaje y COE:** Atlas — ORGANIZATION / Limitar | TheNextCISO — CISO-OS (gobierno) | SAF — Estrategia, integración y gobierno | COE — Cultura, talento y adopción | Responsable sugerido — CISO | Ola 2 (90–180 días)

#### A11.8 · ¿Qué código de conducta profesional rige al equipo de seguridad, cómo se resuelven sus dilemas éticos (monitoreo de personas, divulgación de vulnerabilidades, uso de accesos privilegiados) y quién controla al que controla?

- **Por qué importa:** El equipo de seguridad tiene acceso privilegiado a sistemas, datos y comunicaciones; su legitimidad depende de una conducta íntegra, visible y verificable, no solo de su pericia.
- **Buena práctica (evidencia esperada):** Código de conducta aplicado al equipo (alineado, por ejemplo, con los códigos de ética de ISC2 o ISACA); canal para plantear dilemas y decisiones documentadas; accesos privilegiados del propio equipo bajo los mismos controles que el resto (justo a tiempo, aprobación, registro) y revisión independiente de su uso.
- **Postura de Microsoft:** Microsoft aplica a su propio personal lo que pide a sus clientes: con Customer Lockbox, sus ingenieros no acceden al contenido del cliente sin aprobación explícita, el acceso se revoca al vencer el plazo y cada acción queda en el registro de auditoría. Sigue además una política pública de divulgación coordinada de vulnerabilidades, e Insider Risk Management seudonimiza por defecto las señales de comportamiento de los usuarios.
- **Capacidades Microsoft:** Customer Lockbox; Microsoft Entra Privileged Identity Management; Microsoft Purview Insider Risk Management; política de divulgación coordinada de vulnerabilidades (MSRC)
- **Cruce de marcos:** NIST — CSF GV.RR · GV.PO · PR.AA | CIS — CIS 6 | The Open Group — sin referencia directa | ISACA — COBIT APO07 · EDM01 | CSA — CCM HRS · IAM | MCSB — PA · GS
- **Versión 2.0:** Pregunta nueva (proceso inverso, pareja IC01). El contenido de la antigua A11.8 se integró en A11.1.
- **Anclaje y COE:** Atlas — ORGANIZATION / Gobernar | TheNextCISO — CISO-OS (gobierno) | SAF — Estrategia, integración y gobierno | COE — Cultura, talento y adopción | Responsable sugerido — CISO + RR. HH. + comité de ética | Ola 1 (30–90 días)

#### A11.9 · ¿Cómo evalúa el equipo de seguridad el liderazgo del CISO (comunicar el riesgo al directorio, sostener una visión, conseguir recursos) y qué hace el CISO con esa retroalimentación?

- **Por qué importa:** La confianza del equipo sostiene la ejecución durante una crisis; los profesionales valoran esas capacidades más que la pericia técnica, y haber conducido un incidente grave aumenta la credibilidad del líder.
- **Buena práctica (evidencia esperada):** Retroalimentación de 360 grados periódica y anónima, con resultados compartidos y un plan de mejora; decisiones obtenidas del directorio comunicadas al equipo; mentoría o red de pares para el CISO.
- **Postura de Microsoft:** Silencio: Microsoft no publica criterios para evaluar el liderazgo del CISO desde la perspectiva de su equipo. El antecedente más cercano es SFI, que incorporó la seguridad a la evaluación de desempeño de todos los empleados y a la compensación del liderazgo sénior.
- **Cruce de marcos:** NIST — CSF GV.RR · ID.IM | CIS — sin referencia directa | The Open Group — sin referencia directa | ISACA — COBIT APO07 · APO08 | CSA — CCM HRS | MCSB — sin referencia directa
- **Versión 2.0:** Pregunta nueva (proceso inverso, pareja IC14). El contenido de la antigua A11.9 se integró en A11.4.
- **Anclaje y COE:** Atlas — SELF / Gobernar | TheNextCISO — CISO-MM (madurez) | SAF — Estrategia, integración y gobierno | COE — Cultura, talento y adopción | Responsable sugerido — CISO + RR. HH. | Ola 3 (180–365 días)

## 5. Parte B — Las 99 preguntas sobre IA, agentes y sistemas autónomos

La Parte B aborda la incorporación de IA generativa, agentes y aplicaciones con capacidades cognitivas autónomas o semiautónomas, en sus tres caras: la IA que hay que proteger, la IA que se usa para defender y la IA que usa el adversario.

### B01 — Estrategia, valor y apetito de riesgo de la IA

*Para qué queremos la IA, cuánto riesgo aceptamos y cómo equilibramos oportunidad y exposición.*

#### B01.1 · ¿Qué resultados de negocio esperamos de la IA y de los agentes, y qué riesgos estamos dispuestos a asumir para lograrlos?

- **Por qué importa:** Sin resultados esperados no hay forma de equilibrar oportunidad y riesgo; la adopción se convierte en una suma de pilotos.
- **Buena práctica (evidencia esperada):** Objetivos de IA vinculados a la estrategia, casos de uso priorizados con hipótesis de valor y de riesgo, y revisión trimestral en el comité ejecutivo.
- **Postura de Microsoft:** SAF identifica como antipatrón el «¡Fuego!… ¿apuntar?»: ejecutar IA sin preparación esperando resultados mágicos. El Cloud Adoption Framework para IA propone definir primero la estrategia y los resultados de negocio.
- **Capacidades Microsoft:** Cloud Adoption Framework para IA (estrategia); SAF – AI Security: Strategy and Governance Planning
- **Cruce de marcos:** NIST — AI RMF MAP 1 · MAP 3 · CSF GV.OC | CIS — sin referencia directa | The Open Group — TOGAF Fase A · G268 (IA en la transformación digital) | ISACA — COBIT EDM02 · APO02 · APO04 · AAISM D1 | CSA — AICM GRC | MCSB — GS
- **Anclaje y COE:** Atlas — ORGANIZATION / Gobernar | TheNextCISO — CISO-NX (nueva generación) | SAF — Estrategia, integración y gobierno | COE — Gobierno, políticas y decisiones | Responsable sugerido — CEO + Líder de IA + CISO | Ola 0 (0–30 días) | relevante para el directorio | pregunta prioritaria para el directorio

#### B01.2 · ¿Cuál es nuestro apetito de riesgo específico para la IA, por caso de uso, nivel de autonomía y tipo de dato, y quién lo aprobó?

- **Por qué importa:** El apetito general de riesgo no responde preguntas como cuánta autonomía dar a un agente que mueve dinero o datos personales.
- **Buena práctica (evidencia esperada):** Declaración de apetito para IA con límites por nivel de autonomía, criticidad y sensibilidad de los datos, aprobada por la dirección y revisada ante cambios materiales.
- **Postura de Microsoft:** SAF recuerda que el riesgo cero es imposible, pero que pueden anticiparse y evitarse muchos riesgos significativos, incluidos los riesgos compuestos de escenarios multiagente y de interacción con entidades externas.
- **Capacidades Microsoft:** SAF
- **Cruce de marcos:** NIST — AI RMF MAP 1.5 · GOVERN 1.3 · CSF GV.RM | CIS — CIS RAM v2.2 | The Open Group — Open FAIR O-RA | ISACA — COBIT EDM03 · APO12 · AAISM D2 | CSA — AICM GRC | MCSB — GS
- **Anclaje y COE:** Atlas — RISK / Gobernar | TheNextCISO — CISO-NX (nueva generación) | SAF — Estrategia, integración y gobierno | COE — Riesgo, cumplimiento y aseguramiento | Responsable sugerido — Directorio + CRO | Ola 0 (0–30 días) | relevante para el directorio | pregunta prioritaria para el directorio

#### B01.3 · ¿Qué portafolio de casos de uso tenemos (comprar, extender, construir) y cómo influyen el riesgo y la seguridad en su priorización?

- **Por qué importa:** Cada modelo de adopción traslada responsabilidades distintas; priorizar sin considerarlas genera deuda de seguridad.
- **Buena práctica (evidencia esperada):** Portafolio con criterios de valor, factibilidad y riesgo, clasificado por modelo de adopción (SaaS, plataforma, desarrollo propio) y con las responsabilidades asociadas.
- **Postura de Microsoft:** El modelo de responsabilidad compartida de IA de Microsoft distingue tres capas (plataforma, aplicación y uso) y recomienda empezar por soluciones SaaS, donde el proveedor gestiona más capas; el Cloud Adoption Framework para IA guía la priorización de casos de uso.
- **Capacidades Microsoft:** Cloud Adoption Framework para IA; modelo de responsabilidad compartida de IA
- **Cruce de marcos:** NIST — AI RMF MAP 1.1 · MAP 3.3 · GOVERN 6 | CIS — sin referencia directa | The Open Group — TOGAF Fase E · G268 (IA en la transformación digital) | ISACA — COBIT APO05 · APO04 | CSA — AICM GRC · STA | MCSB — GS
- **Anclaje y COE:** Atlas — ORGANIZATION / Gobernar | TheNextCISO — CISO-NX (nueva generación) | SAF — Estrategia, integración y gobierno | COE — Gobierno, políticas y decisiones | Responsable sugerido — Líder de IA | Ola 1 (30–90 días)

#### B01.4 · ¿Nuestra estrategia distingue las tres caras de la IA: la que usa el adversario, la que usamos para defendernos y la que debemos proteger?

- **Por qué importa:** Tratar las tres como un solo problema produce planes incompletos: se protege la IA propia y se ignora la del atacante, o al revés.
- **Buena práctica (evidencia esperada):** Estrategia con tres líneas de trabajo y responsables: proteger la IA propia, usar IA para la defensa y prepararse ante ataques potenciados por IA.
- **Postura de Microsoft:** SAF organiza la seguridad de la IA en dos movimientos, asegurar la tecnología de IA y usar la IA para la seguridad, frente a atacantes que la usan para mejorar y acelerar sus técnicas. El borrador del Cyber AI Profile de NIST propone una división equivalente.
- **Capacidades Microsoft:** SAF; Microsoft Security Copilot; Microsoft Defender
- **Cruce de marcos:** NIST — IR 8596 borrador (Secure · Defend · Thwart) · AI RMF GOVERN 1 | CIS — sin referencia directa | The Open Group — sin referencia directa | ISACA — COBIT APO02 · APO13 · AAISM D1 | CSA — AICM GRC | MCSB — GS
- **Anclaje y COE:** Atlas — AI & AGENTS / Anticipar | TheNextCISO — CISO-NX (nueva generación) | SAF — Estrategia, integración y gobierno | COE — Gobierno, políticas y decisiones | Responsable sugerido — CISO | Ola 0 (0–30 días) | relevante para el directorio

#### B01.5 · ¿Cómo medimos el valor y el riesgo de la IA de forma conjunta (beneficio, costo, incidentes, exposición) y quién revisa esos indicadores?

- **Por qué importa:** Medir solo la adopción oculta el riesgo; medir solo el riesgo oculta el valor y lleva a bloquear.
- **Buena práctica (evidencia esperada):** Tablero conjunto con indicadores de valor (tiempo ahorrado, resultados de negocio) y de riesgo (incidentes, exposición, excepciones), revisado por el comité de IA.
- **Postura de Microsoft:** SAF propone que, en el nivel más alto de madurez, la gobernanza de la IA sea un habilitador medible de la confianza, el riesgo y los resultados de negocio; Microsoft ofrece métricas de adopción e impacto de Copilot y de los agentes.
- **Capacidades Microsoft:** Copilot Analytics; Microsoft Agent 365 (métricas de agentes); análisis de Copilot Studio
- **Cruce de marcos:** NIST — AI RMF MAP 1.4 · MANAGE 2.2 · MEASURE 1 · AI 600-1 (Environmental Impacts) | CIS — sin referencia directa | The Open Group — sin referencia directa | ISACA — COBIT EDM02 · MEA01 | CSA — AICM GRC | MCSB — GS
- **Anclaje y COE:** Atlas — TRUST / Gobernar | TheNextCISO — CISO-MM (madurez) | SAF — Estrategia, integración y gobierno | COE — Valor, métricas y comunicación ejecutiva | Responsable sugerido — Líder de IA + CISO | Ola 2 (90–180 días) | relevante para el directorio

#### B01.6 · ¿Qué usos de IA están prohibidos o requieren aprobación reforzada por su impacto en personas, derechos o seguridad física?

- **Por qué importa:** Algunos usos generan daños difíciles de revertir y obligaciones legales específicas.
- **Buena práctica (evidencia esperada):** Lista de usos prohibidos y sensibles, criterio de escalamiento, revisión interdisciplinaria y registro de decisiones.
- **Postura de Microsoft:** El Responsible AI Standard exige revisión adicional para los usos sensibles (efectos en la situación legal u oportunidades de vida, daño físico o psicológico, amenazas a derechos humanos). Según su Responsible AI Transparency Report 2026, Microsoft hizo más de 450 revisiones de usos sensibles entre julio de 2025 y junio de 2026, más del 30 % sobre IA agéntica.
- **Capacidades Microsoft:** Microsoft Responsible AI Standard (usos sensibles); Responsible AI Transparency Report 2026
- **Cruce de marcos:** NIST — AI RMF MAP 5 · GOVERN 1.1 · AI 600-1 (CBRN Information or Capabilities; Dangerous, Violent, or Hateful Content) | CIS — sin referencia directa | The Open Group — sin referencia directa | ISACA — COBIT EDM03 · MEA03 · AAISM D2 | CSA — AICM GRC | MCSB — GS
- **Anclaje y COE:** Atlas — TRUST / Gobernar | TheNextCISO — CISO-NX (nueva generación) | SAF — Estrategia, integración y gobierno | COE — Gobierno, políticas y decisiones | Responsable sugerido — Comité de IA + Legal | Ola 0 (0–30 días) | relevante para el directorio | pregunta prioritaria para el directorio

#### B01.7 · ¿Cómo evitamos que la presión por adoptar IA rápido debilite los fundamentos de seguridad de los que la IA depende (identidad, datos, parches)?

- **Por qué importa:** La IA amplifica las debilidades existentes: si los datos están sobreexpuestos, la IA los encuentra.
- **Buena práctica (evidencia esperada):** Requisitos mínimos de fundamentos como condición para escalar la IA, con indicadores revisados antes de cada ola de despliegue.
- **Postura de Microsoft:** SAF señala como antipatrón descuidar los fundamentos de datos y seguridad, y afirma que la seguridad de la IA depende de la seguridad de los datos, la identidad, la infraestructura, el desarrollo y la tecnología operativa.
- **Capacidades Microsoft:** SAF; Baseline Security Mode (Microsoft 365); Microsoft Purview; Microsoft Entra
- **Cruce de marcos:** NIST — AI RMF GOVERN 1 · CSF GV.RM | CIS — CIS IG1 (higiene esencial) | The Open Group — sin referencia directa | ISACA — COBIT APO13 · APO12 | CSA — AICM GRC (dominios heredados de CCM) | MCSB — GS
- **Anclaje y COE:** Atlas — TECHNOLOGY / Limitar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Estrategia, integración y gobierno | COE — Plataforma e ingeniería de controles | Responsable sugerido — CISO + CIO | Ola 0 (0–30 días) | relevante para el directorio

#### B01.8 · ¿Qué postura adoptamos frente a la IA de consumo y a la IA que nuestros proveedores incorporan en productos que ya usamos?

- **Por qué importa:** Gran parte de la IA llega sin proyecto: por el navegador, por una actualización del proveedor o por una cuenta personal.
- **Buena práctica (evidencia esperada):** Política explícita para la IA de consumo y para las funciones de IA de los proveedores (activación, datos permitidos, exclusión), con inventario y revisión contractual.
- **Postura de Microsoft:** SAF pide definir la postura ante la IA que incorporan los proveedores y ante la IA externa; Defender for Cloud Apps ofrece un catálogo de aplicaciones de IA generativa con puntuación de riesgo (las no autorizadas se bloquean con Defender for Endpoint) y Purview DSPM cubre aplicaciones de IA de terceros detectadas por el navegador.
- **Capacidades Microsoft:** Microsoft Defender for Cloud Apps (categoría Generative AI); Microsoft Purview DSPM
- **Cruce de marcos:** NIST — AI RMF GOVERN 6 · MAP 4 · CSF GV.SC | CIS — CIS 2 (2.3) · CIS 15 | The Open Group — sin referencia directa | ISACA — COBIT APO10 · BAI09 | CSA — AICM STA | MCSB — AM
- **Anclaje y COE:** Atlas — RISK / Limitar | TheNextCISO — CISO-NX (nueva generación) | SAF — Estrategia, integración y gobierno | COE — Gobierno, políticas y decisiones | Responsable sugerido — CISO + Compras | Ola 1 (30–90 días)

#### B01.9 · ¿Cómo ajustamos estrategia, políticas y controles al ritmo de cambio de la IA sin rehacer el gobierno cada trimestre?

- **Por qué importa:** Las capacidades y amenazas de IA cambian en semanas; un gobierno rígido queda obsoleto y uno improvisado no da garantías.
- **Buena práctica (evidencia esperada):** Principios estables, estándares y controles versionados, un ciclo corto de revisión y un enfoque de permitir lo conocido, bloquear lo peligroso y evaluar lo inesperado.
- **Postura de Microsoft:** SAF propone adaptar estrategia, política y controles a la velocidad de la IA con un enfoque pragmático: permitir lo conocido y seguro, bloquear lo conocido y peligroso, y detectar y evaluar las variaciones inesperadas.
- **Capacidades Microsoft:** SAF
- **Cruce de marcos:** NIST — AI RMF GOVERN 1.5 · MEASURE 3 · CSF ID.IM | CIS — sin referencia directa | The Open Group — TOGAF Fase H | ISACA — COBIT APO04 · APO01 | CSA — AICM GRC | MCSB — GS
- **Anclaje y COE:** Atlas — ORGANIZATION / Anticipar | TheNextCISO — CISO-NX (nueva generación) | SAF — Estrategia, integración y gobierno | COE — Gobierno, políticas y decisiones | Responsable sugerido — Comité de IA | Ola 1 (30–90 días)

### B02 — Gobierno, roles, políticas y centro de excelencia de IA

*Las estructuras, reglas y capacidades que convierten principios de IA responsable en práctica.*

#### B02.1 · ¿Tenemos un marco de IA responsable publicado, patrocinado por la dirección y aplicado antes de cada despliegue?

- **Por qué importa:** Los principios sin mecanismos de aplicación no cambian lo que llega a producción.
- **Buena práctica (evidencia esperada):** Marco publicado, patrocinio ejecutivo visible, evaluación previa al despliegue con criterios y evidencia, y revisión anual.
- **Postura de Microsoft:** Microsoft adoptó en 2018 seis principios de IA responsable (equidad; confiabilidad y seguridad; privacidad y seguridad; inclusión; transparencia; responsabilidad), los hace operativos con su Responsible AI Standard y publicó en septiembre de 2026 su tercer Responsible AI Transparency Report anual.
- **Capacidades Microsoft:** Microsoft Responsible AI Standard (v2 pública); Responsible AI Transparency Report 2026
- **Cruce de marcos:** NIST — AI RMF GOVERN 1.2 · GOVERN 2.3 | CIS — sin referencia directa | The Open Group — sin referencia directa | ISACA — COBIT EDM01 · APO01 · AAISM D1 | CSA — AICM GRC | MCSB — GS
- **Anclaje y COE:** Atlas — TRUST / Gobernar | TheNextCISO — CISO-NX (nueva generación) | SAF — Estrategia, integración y gobierno | COE — Gobierno, políticas y decisiones | Responsable sugerido — CEO + Líder de IA | Ola 0 (0–30 días) | relevante para el directorio | pregunta prioritaria para el directorio

#### B02.2 · ¿Existe un consejo interdisciplinario de IA (negocio, seguridad, riesgo, legal, privacidad, datos) con mandato, umbrales de decisión y registro?

- **Por qué importa:** Los riesgos de la IA cruzan funciones; ninguna área puede gobernarlos sola.
- **Buena práctica (evidencia esperada):** Carta del consejo, integrantes con autoridad, umbrales de escalamiento, agenda periódica, actas y decisiones trazables.
- **Postura de Microsoft:** SAF recomienda un consejo interdisciplinario de gobierno de IA que revise las iniciativas, y un proceso estructurado de colaboración entre dirección ejecutiva, riesgo empresarial, seguridad, tecnología y cumplimiento.
- **Capacidades Microsoft:** SAF
- **Cruce de marcos:** NIST — AI RMF GOVERN 2.1 · MAP 1.2 | CIS — sin referencia directa | The Open Group — TOGAF Gobierno de arquitectura (junta de arquitectura) | ISACA — COBIT EDM01 · APO01 · AAISM D1 | CSA — AICM GRC | MCSB — GS
- **Anclaje y COE:** Atlas — ORGANIZATION / Gobernar | TheNextCISO — CISO-NX (nueva generación) | SAF — Estrategia, integración y gobierno | COE — Gobierno, políticas y decisiones | Responsable sugerido — Sponsor ejecutivo | Ola 0 (0–30 días) | relevante para el directorio | pregunta prioritaria para el directorio

#### B02.3 · ¿Qué rol cumple el CISO en el gobierno de la IA (dueño, asesor, revisor o habilitador) y está formalizado?

- **Por qué importa:** Si el rol del CISO no está definido, la seguridad llega tarde o asume responsabilidades que corresponden al negocio, a Legal o a Privacidad.
- **Buena práctica (evidencia esperada):** Rol escrito en la carta del consejo de IA, con derechos de decisión, puertas de revisión obligatorias y límites claros frente a otras funciones.
- **Postura de Microsoft:** SAF describe la evolución de responsabilidades: los dueños de producto diseñan y construyen sistemas resilientes, y seguridad evalúa y asesora sobre el riesgo, ayuda a prevenir y detectar y lidera la respuesta, en estrecha colaboración y con especial atención al alcance de la autonomía y los permisos.
- **Capacidades Microsoft:** SAF
- **Cruce de marcos:** NIST — AI RMF GOVERN 2.1 · CSF GV.RR | CIS — sin referencia directa | The Open Group — Roles de seguridad (borrador citado por SAF) | ISACA — COBIT APO01 · APO13 · AAISM D1 | CSA — AICM GRC | MCSB — GS
- **Anclaje y COE:** Atlas — SELF / Gobernar | TheNextCISO — CISO-OS (gobierno) | SAF — Estrategia, integración y gobierno | COE — Gobierno, políticas y decisiones | Responsable sugerido — CEO + CISO | Ola 0 (0–30 días)

#### B02.4 · ¿Tenemos una política de uso aceptable de IA que defina servicios autorizados y prohibidos, datos admitidos, uso de resultados y consecuencias?

- **Por qué importa:** Sin reglas claras, cada persona decide qué datos compartir y con qué servicio.
- **Buena práctica (evidencia esperada):** Política breve y comprensible, aceptada por los usuarios, con controles técnicos que la refuerzan y medición de su cumplimiento.
- **Postura de Microsoft:** SAF enumera los temas mínimos de política: uso aceptable y prohibido, servicios externos, aprobación y controles de apps y agentes internos, protección de datos y privacidad, explicabilidad de decisiones, supervisión humana y formación.
- **Capacidades Microsoft:** SAF; Microsoft Purview DSPM (políticas); Microsoft Defender for Cloud Apps (autorizar o bloquear aplicaciones)
- **Cruce de marcos:** NIST — AI RMF GOVERN 1.1 · GOVERN 1.4 | CIS — CIS 2 · CIS 14 | The Open Group — sin referencia directa | ISACA — COBIT APO01 · APO14 · AAISM D1 | CSA — AICM GRC · HRS | MCSB — GS
- **Anclaje y COE:** Atlas — ORGANIZATION / Limitar | TheNextCISO — CISO-NX (nueva generación) | SAF — Estrategia, integración y gobierno | COE — Gobierno, políticas y decisiones | Responsable sugerido — CISO + Legal + RR. HH. | Ola 0 (0–30 días)

#### B02.5 · ¿Existe un proceso único de ciclo de vida para agentes y aplicaciones de IA (propuesta, aprobación, registro, operación, cambio y retiro)?

- **Por qué importa:** Sin un ciclo de vida común, cada plataforma crea agentes con reglas distintas y nadie sabe cuáles siguen activos.
- **Buena práctica (evidencia esperada):** Proceso documentado con puertas de aprobación por nivel de riesgo, registro obligatorio, revisiones periódicas y retiro con evidencia.
- **Postura de Microsoft:** SAF pregunta si existe un proceso unificado de ciclo de vida de los agentes (aprobación, registro y retiro). Microsoft Agent 365, disponible de forma general desde el 1 de mayo de 2026, aporta registro, control de acceso, visualización, interoperabilidad y seguridad de agentes, incluida la cuarentena de agentes no autorizados; Copilot Studio suma entornos administrados y canalizaciones.
- **Capacidades Microsoft:** Microsoft Agent 365; Copilot Studio (entornos administrados, canalizaciones); inventario de Power Platform; aprobación de agentes en el centro de administración de Microsoft 365
- **Cruce de marcos:** NIST — AI RMF GOVERN 1.6 · GOVERN 1.7 · MANAGE 4.1 | CIS — CIS 2 · CIS 16 · guía CIS para agentes de IA | The Open Group — TOGAF ADM · Fase G | ISACA — COBIT BAI01 · BAI06 · BAI07 · AAISM D1 | CSA — AICM GRC · CCC | MCSB — GS · AM
- **Anclaje y COE:** Atlas — AI & AGENTS / Gobernar | TheNextCISO — CISO-NX (nueva generación) | SAF — Estrategia, integración y gobierno | COE — Gobierno, políticas y decisiones | Responsable sugerido — COE de IA | Ola 1 (30–90 días)

#### B02.6 · ¿Cada agente y aplicación de IA tiene dueño de negocio, patrocinador, responsable técnico y dueño de datos, con suplentes y fecha de revisión?

- **Por qué importa:** Un agente sin dueño no tiene a nadie que responda por sus acciones ni que decida su retiro.
- **Buena práctica (evidencia esperada):** Registro sin agentes huérfanos, suplentes definidos, revisión periódica de la titularidad y baja automática cuando el dueño deja la organización.
- **Postura de Microsoft:** Microsoft sostiene que las organizaciones deben esperar rendir cuentas por las acciones de sus agentes; en Microsoft Entra Agent ID cada agente tiene patrocinadores responsables de su ciclo de vida y su acceso, y propietarios técnicos; si el patrocinador deja la organización, la responsabilidad pasa a su responsable jerárquico.
- **Capacidades Microsoft:** Microsoft Entra Agent ID (patrocinadores y propietarios); Microsoft Agent 365
- **Cruce de marcos:** NIST — AI RMF GOVERN 2.1 · GOVERN 1.6 | CIS — CIS 5 (5.1, 5.5) · guía CIS para agentes de IA | The Open Group — sin referencia directa | ISACA — COBIT APO01 · BAI09 · AAISM D1 | CSA — AICM GRC · IAM | MCSB — AM · IM
- **Anclaje y COE:** Atlas — TRUST / Gobernar | TheNextCISO — CISO-NX (nueva generación) | SAF — Acceso e identidad | COE — Gobierno, políticas y decisiones | Responsable sugerido — Dueños de negocio | Ola 0 (0–30 días)

#### B02.7 · ¿Cómo clasificamos los sistemas de IA por nivel de riesgo y qué controles mínimos exige cada nivel?

- **Por qué importa:** Aplicar los mismos controles a un asistente personal y a un agente que ejecuta pagos es ineficiente o peligroso.
- **Buena práctica (evidencia esperada):** Niveles definidos (por ejemplo, personal, equipo, empresarial, misión crítica) según autonomía, datos, alcance y reversibilidad, con controles mínimos por nivel.
- **Postura de Microsoft:** Microsoft clasifica sus propios sistemas mediante evaluaciones de impacto de IA responsable y la revisión de usos sensibles; SAF exige delimitar cuidadosamente la autonomía y los permisos de cada agente.
- **Capacidades Microsoft:** Plantilla de evaluación de impacto de IA responsable (Microsoft); SAF
- **Cruce de marcos:** NIST — AI RMF MAP 2 · GOVERN 1.3 | CIS — sin referencia directa | The Open Group — Open FAIR O-RA | ISACA — COBIT APO12 · BAI02 · AAISM D2 | CSA — AICM GRC | MCSB — GS
- **Anclaje y COE:** Atlas — RISK / Limitar | TheNextCISO — CISO-NX (nueva generación) | SAF — Estrategia, integración y gobierno | COE — Riesgo, cumplimiento y aseguramiento | Responsable sugerido — Comité de IA | Ola 1 (30–90 días)

#### B02.8 · ¿Tenemos un centro de excelencia de IA segura que entregue patrones, entornos preaprobados y kits de inicio para que los equipos avancen rápido y seguros?

- **Por qué importa:** Si el camino seguro es más lento que el atajo, los equipos toman el atajo.
- **Buena práctica (evidencia esperada):** COE con catálogo de patrones de referencia, zonas de aterrizaje de IA, plantillas de evaluación, guardrails predeterminados y acompañamiento a los equipos.
- **Postura de Microsoft:** SAF recomienda iniciar un marco de IA responsable y un centro de excelencia y construir un kit de inicio; la guía de centro de excelencia de IA del Cloud Adoption Framework propone patrocinio ejecutivo, equipo multidisciplinario, integración con el centro de excelencia de nube y evolución de un modelo centralizado a uno asesor.
- **Capacidades Microsoft:** SAF; Cloud Adoption Framework (centro de excelencia de IA); zonas de aterrizaje de IA en Azure
- **Cruce de marcos:** NIST — AI RMF GOVERN 4 · GOVERN 2.2 | CIS — sin referencia directa | The Open Group — TOGAF Capacidad de arquitectura · Continuum empresarial | ISACA — COBIT APO04 · BAI08 · AAISM D1 | CSA — AICM GRC | MCSB — GS · DS
- **Anclaje y COE:** Atlas — ORGANIZATION / Limitar | TheNextCISO — CISO-NX (nueva generación) | SAF — Arquitectura de seguridad de extremo a extremo | COE — Arquitectura y patrones seguros | Responsable sugerido — Líder de IA + CISO | Ola 1 (30–90 días)

#### B02.9 · ¿Cómo formamos a cada audiencia (directorio, desarrolladores, usuarios, equipo de seguridad) sobre qué es y qué no es la IA, sus riesgos y su uso responsable?

- **Por qué importa:** La IA es nueva para todos: líderes, usuarios, desarrolladores, equipos de seguridad y reguladores.
- **Buena práctica (evidencia esperada):** Programa por audiencia con contenidos sobre capacidades, límites, riesgos y conductas; métricas de alcance y de cambio de conducta.
- **Postura de Microsoft:** SAF propone formación sobre IA para todos (qué es y qué no es) y advierte contra los antipatrones de percepción: creer que es una solución mágica, que es inútil o que todos los modelos son iguales.
- **Capacidades Microsoft:** SAF; Microsoft Learn (formación en IA y seguridad)
- **Cruce de marcos:** NIST — AI RMF GOVERN 2.2 · CSF PR.AT | CIS — CIS 14 | The Open Group — sin referencia directa | ISACA — COBIT APO07 · BAI05 | CSA — AICM HRS | MCSB — GS
- **Anclaje y COE:** Atlas — SELF / Anticipar | TheNextCISO — CISO-NX (nueva generación) | SAF — Estrategia, integración y gobierno | COE — Cultura, talento y adopción | Responsable sugerido — COE de IA + RR. HH. | Ola 1 (30–90 días)

### B03 — Inventario, descubrimiento e IA no autorizada

*No se puede gobernar lo que no se ve: modelos, agentes, herramientas y uso no autorizado.*

#### B03.1 · ¿Tenemos un inventario único de modelos, aplicaciones, copilotos, agentes, servidores MCP y conectores de IA, con dueño y criticidad?

- **Por qué importa:** No se puede gobernar, proteger ni retirar lo que no está inventariado.
- **Buena práctica (evidencia esperada):** Inventario consolidado desde varias fuentes, con dueño, nivel de riesgo, datos y herramientas accesibles, actualizado de forma automática.
- **Postura de Microsoft:** Microsoft Agent 365 provee un registro de agentes (con sincronización desde AWS Bedrock y Google Cloud en versión preliminar); Defender for Cloud descubre la lista de materiales de IA en Azure OpenAI, Foundry, Azure Machine Learning, Amazon Bedrock y Google Vertex AI (la postura a nivel de agente requiere Agent 365 desde julio de 2026); Purview DSPM muestra el uso de IA sobre los datos.
- **Capacidades Microsoft:** Microsoft Agent 365 (registro); Microsoft Defender for Cloud (gestión de postura de seguridad de IA); Microsoft Purview DSPM
- **Cruce de marcos:** NIST — AI RMF GOVERN 1.6 · CSF ID.AM | CIS — CIS 1 · CIS 2 · guía CIS para agentes de IA | The Open Group — TOGAF Continuum empresarial (repositorio) | ISACA — COBIT BAI09 · BAI10 · AAISM D3 | CSA — AICM MDS · DSP | MCSB — AM · AI-1
- **Anclaje y COE:** Atlas — AI & AGENTS / Anticipar | TheNextCISO — CISO-NX (nueva generación) | SAF — Gestión de la postura de seguridad | COE — Plataforma e ingeniería de controles | Responsable sugerido — COE de IA + CISO | Ola 0 (0–30 días) | relevante para el directorio | pregunta prioritaria para el directorio

#### B03.2 · ¿Cómo descubrimos el uso no autorizado de IA (aplicaciones web de IA generativa, extensiones de navegador, agentes locales, claves de API personales)?

- **Por qué importa:** El uso no autorizado de IA es inevitable; lo peligroso es no verlo.
- **Buena práctica (evidencia esperada):** Descubrimiento continuo en red, navegador y endpoint; catálogo de riesgo de aplicaciones de IA; alertas por aplicaciones nuevas y reporte periódico.
- **Postura de Microsoft:** Microsoft recomienda empezar por descubrir la IA existente: Microsoft Entra Internet Access detecta el uso de IA no autorizada (disponible de forma general desde mayo de 2026; la visibilidad de servidores MCP no autorizados está en versión preliminar), Defender for Cloud Apps puntúa el riesgo de las aplicaciones de IA generativa y Purview DSPM muestra las interacciones con IA de terceros.
- **Capacidades Microsoft:** Microsoft Entra Internet Access (descubrimiento de IA no autorizada); Microsoft Defender for Cloud Apps; Microsoft Purview DSPM; DLP de endpoint
- **Cruce de marcos:** NIST — AI RMF GOVERN 1.6 · CSF ID.AM · DE.CM | CIS — CIS 2 (2.3) · CIS 13 | The Open Group — sin referencia directa | ISACA — COBIT BAI09 · DSS05 · AAISM D3 | CSA — AICM DSP · LOG | MCSB — AM · LT
- **Anclaje y COE:** Atlas — RISK / Anticipar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Gestión de la postura de seguridad | COE — Plataforma e ingeniería de controles | Responsable sugerido — CISO | Ola 0 (0–30 días)

#### B03.3 · ¿Qué hacemos cuando descubrimos IA no autorizada: bloquear, migrar a una alternativa segura o regularizarla con dueño y controles?

- **Por qué importa:** Bloquear sin ofrecer alternativa empuja el uso hacia canales menos visibles.
- **Buena práctica (evidencia esperada):** Criterio documentado por nivel de riesgo, alternativas aprobadas disponibles, plazos de regularización y comunicación a los usuarios.
- **Postura de Microsoft:** Microsoft permite marcar aplicaciones de IA como no autorizadas para bloquearlas automáticamente mediante Defender for Endpoint, y ofrecer alternativas con protección de datos empresariales, como Microsoft 365 Copilot Chat con la cuenta corporativa.
- **Capacidades Microsoft:** Microsoft Defender for Cloud Apps (autorizar o bloquear); Microsoft 365 Copilot Chat (protección de datos empresariales)
- **Cruce de marcos:** NIST — AI RMF GOVERN 1.6 · MANAGE 1.3 | CIS — CIS 2 (2.3) | The Open Group — sin referencia directa | ISACA — COBIT APO12 · BAI09 · AAISM D2 | CSA — AICM GRC | MCSB — AM
- **Anclaje y COE:** Atlas — RISK / Limitar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Estrategia, integración y gobierno | COE — Gobierno, políticas y decisiones | Responsable sugerido — CISO + Líder de IA | Ola 1 (30–90 días)

#### B03.4 · ¿Sabemos qué agentes crean los usuarios con herramientas de bajo código y qué permisos, conectores y datos utilizan?

- **Por qué importa:** La creación de agentes por usuarios de negocio multiplica rápidamente la superficie de riesgo.
- **Buena práctica (evidencia esperada):** Inventario de agentes por entorno, políticas de conectores, entornos administrados para producción y revisión de los agentes compartidos ampliamente.
- **Postura de Microsoft:** El inventario de Power Platform ofrece una vista unificada de los agentes y permite bloquear agentes publicados; los entornos administrados limitan cómo se comparten, y las políticas de datos y de conectores avanzados controlan conectores y servidores MCP.
- **Capacidades Microsoft:** Inventario de Power Platform; entornos administrados; políticas de datos y de conectores avanzados; Microsoft Agent 365
- **Cruce de marcos:** NIST — AI RMF GOVERN 1.6 · CSF ID.AM | CIS — CIS 2 · CIS 3 · guía CIS para agentes de IA | The Open Group — sin referencia directa | ISACA — COBIT BAI09 · DSS05 · AAISM D3 | CSA — AICM DSP · IAM | MCSB — AM · DP
- **Anclaje y COE:** Atlas — AI & AGENTS / Anticipar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Gestión de la postura de seguridad | COE — Plataforma e ingeniería de controles | Responsable sugerido — Administración de plataforma + CISO | Ola 0 (0–30 días)

#### B03.5 · ¿Mantenemos una lista de materiales de IA (modelos, versiones, conjuntos de datos, instrucciones de sistema, herramientas, dependencias) para cada sistema crítico?

- **Por qué importa:** Sin saber qué compone un sistema de IA no se puede evaluar el impacto de una vulnerabilidad ni el del retiro de un modelo.
- **Buena práctica (evidencia esperada):** Lista de materiales por sistema crítico, actualizada en cada cambio y vinculada al inventario y a la evaluación de riesgo; nivel de detalle proporcional al riesgo.
- **Postura de Microsoft:** Defender for Cloud genera una lista de materiales de IA (AI BOM) para las cargas de trabajo de IA en la nube y la usa para detectar riesgos en sus componentes.
- **Capacidades Microsoft:** Microsoft Defender for Cloud (gestión de postura de seguridad de IA, AI BOM)
- **Cruce de marcos:** NIST — SP 800-218A · AI RMF MAP 4 · GOVERN 6 · AI 600-1 (Value Chain and Component Integration) | CIS — CIS 2 · guía CIS para LLM | The Open Group — sin referencia directa | ISACA — COBIT BAI10 · BAI03 · AAISM D3 | CSA — AICM STA · MDS | MCSB — AM · DS · AI-1
- **Anclaje y COE:** Atlas — TECHNOLOGY / Anticipar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Seguridad del desarrollo | COE — Arquitectura y patrones seguros | Responsable sugerido — Ingeniería de IA | Ola 2 (90–180 días)

#### B03.6 · ¿Cómo inventariamos y aprobamos los servidores MCP y las herramientas que los agentes pueden invocar, sean internos o de terceros?

- **Por qué importa:** Cada herramienta amplía lo que un agente puede hacer; una herramienta maliciosa o modificada puede secuestrar su comportamiento.
- **Buena práctica (evidencia esperada):** Catálogo de herramientas y servidores MCP aprobados, con dueño, permisos, versión fijada y revisión de cambios; bloqueo de los no aprobados.
- **Postura de Microsoft:** En Agent 365, el registro de herramientas del centro de administración de Microsoft 365 es la fuente de verdad de los servidores MCP (los servidores propios pasan por una pasarela, en versión preliminar). La guía de Microsoft para MCP pide OAuth 2.1 con PKCE, tokens ligados a su audiencia, mínimo privilegio, fijar los esquemas aprobados, inventariar servidores y usar Azure API Management como punto de control.
- **Capacidades Microsoft:** Microsoft Agent 365 (registro de herramientas); Azure API Management (servidores MCP); políticas de conectores avanzados de Power Platform
- **Cruce de marcos:** NIST — AI RMF MAP 4 · GOVERN 6.1 · CSF ID.AM | CIS — CIS 2 · CIS 16 · guía CIS para MCP · CIS MCP Server Benchmark | The Open Group — sin referencia directa | ISACA — COBIT BAI09 · APO10 · AAISM D3 | CSA — AICM STA · AIS · MAESTRO L3 · L7 | MCSB — AM · DS
- **Anclaje y COE:** Atlas — TECHNOLOGY / Limitar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Seguridad del desarrollo | COE — Arquitectura y patrones seguros | Responsable sugerido — Arquitectura + COE de IA | Ola 1 (30–90 días)

#### B03.7 · ¿Cómo detectamos agentes huérfanos, inactivos o cuyo dueño dejó la organización, y en cuánto tiempo los retiramos?

- **Por qué importa:** Los agentes huérfanos conservan permisos y acceso a datos sin que nadie los supervise.
- **Buena práctica (evidencia esperada):** Detección automática por inactividad y por baja del dueño, revisión periódica, plazo máximo de retiro y evidencia de desactivación.
- **Postura de Microsoft:** En Microsoft Entra Agent ID los patrocinadores responden por el ciclo de vida de cada agente y, si se van, la responsabilidad pasa a su responsable jerárquico; las tareas de patrocinio en Lifecycle Workflows están disponibles de forma general desde mayo de 2026. Las revisiones de acceso específicas para agentes no están confirmadas.
- **Capacidades Microsoft:** Microsoft Entra Agent ID; Microsoft Entra ID Governance (Lifecycle Workflows); Microsoft Agent 365
- **Cruce de marcos:** NIST — AI RMF GOVERN 1.7 · CSF PR.AA | CIS — CIS 5 (5.3) · guía CIS para agentes de IA | The Open Group — sin referencia directa | ISACA — COBIT BAI09 · DSS05 · AAISM D3 | CSA — AICM IAM | MCSB — IM · AM
- **Anclaje y COE:** Atlas — AI & AGENTS / Limitar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Acceso e identidad | COE — Plataforma e ingeniería de controles | Responsable sugerido — IAM + COE de IA | Ola 1 (30–90 días)

#### B03.8 · ¿Qué visibilidad tenemos del uso de IA en endpoints y entornos de desarrollo (asistentes de código, modelos locales, notebooks, agentes de escritorio)?

- **Por qué importa:** Los modelos y agentes locales operan con los permisos del usuario y fuera de los controles de la nube.
- **Buena práctica (evidencia esperada):** Inventario del software de IA en endpoints, políticas para asistentes de código, control de aplicaciones y monitoreo de comportamiento.
- **Postura de Microsoft:** Microsoft recomienda inventariar el software de los dispositivos y aplicar control de aplicaciones; GitHub Copilot ofrece políticas y registros de auditoría empresariales.
- **Capacidades Microsoft:** Microsoft Defender for Endpoint (inventario de software); App Control for Business; GitHub Copilot (políticas y auditoría empresariales)
- **Cruce de marcos:** NIST — AI RMF GOVERN 1.6 · CSF ID.AM · PR.PS | CIS — CIS 2 (2.5) · CIS 10 | The Open Group — sin referencia directa | ISACA — COBIT BAI09 · DSS05 | CSA — AICM UEM | MCSB — AM · ES
- **Anclaje y COE:** Atlas — TECHNOLOGY / Anticipar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Seguridad del desarrollo | COE — Plataforma e ingeniería de controles | Responsable sugerido — Seguridad de endpoints + Ingeniería | Ola 2 (90–180 días)

#### B03.9 · ¿Qué indicadores de cobertura usamos (agentes inventariados, con identidad, con dueño, con política, con monitoreo) y cuál es la meta del próximo trimestre?

- **Por qué importa:** La cobertura parcial genera una falsa sensación de control.
- **Buena práctica (evidencia esperada):** Indicadores de cobertura por plataforma con metas trimestrales y explicación de las brechas.
- **Postura de Microsoft:** Microsoft Agent 365 ofrece métricas de adopción, uso y riesgo de los agentes; SAF propone una hoja de ruta de gobierno y seguridad de IA en cinco niveles, desde «sin gobierno formal» hasta «IA confiable y auditable».
- **Capacidades Microsoft:** Microsoft Agent 365; Microsoft Purview DSPM (informes)
- **Cruce de marcos:** NIST — AI RMF MEASURE 1 · CSF ID.IM | CIS — CIS 1 · CIS 2 | The Open Group — sin referencia directa | ISACA — COBIT MEA01 | CSA — AICM GRC | MCSB — AM
- **Anclaje y COE:** Atlas — TRUST / Gobernar | TheNextCISO — CISO-MM (madurez) | SAF — Gestión de la postura de seguridad | COE — Valor, métricas y comunicación ejecutiva | Responsable sugerido — COE de IA | Ola 1 (30–90 días)

### B04 — Identidad, autoridad y delegación de agentes

*Los agentes como una nueva clase de identidad que actúa con autoridad delegada.*

#### B04.1 · ¿Cada agente tiene una identidad propia, distinguible de la de personas y aplicaciones, que permita atribuirle sus acciones?

- **Por qué importa:** Si un agente actúa con la identidad de una persona o con credenciales compartidas, no se puede saber quién hizo qué.
- **Buena práctica (evidencia esperada):** Identidad única por agente autónomo, registrada en el proveedor de identidad, con atributos de dueño, propósito y nivel de riesgo.
- **Postura de Microsoft:** Microsoft sostiene que cada agente necesita identidad y gobierno, y que toda acción de un agente debe estar autorizada y ser trazable. Microsoft Entra Agent ID está disponible de forma general desde mayo de 2026; aplicar a los agentes los controles de seguridad de Entra requiere Microsoft Agent 365 (incluido en Microsoft 365 E7).
- **Capacidades Microsoft:** Microsoft Entra Agent ID; Microsoft Agent 365
- **Cruce de marcos:** NIST — CSF PR.AA · AI RMF GOVERN 1.6 · NCCoE identidad y autorización de agentes (borrador) | CIS — CIS 5 (5.1) · guía CIS para agentes de IA | The Open Group — Zero Trust Commandments | ISACA — COBIT DSS05 · AAISM D3 | CSA — AICM IAM · Agentic AI IAM (CSA) | MCSB — IM
- **Anclaje y COE:** Atlas — AI & AGENTS / Limitar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Acceso e identidad | COE — Plataforma e ingeniería de controles | Responsable sugerido — IAM | Ola 0 (0–30 días)

#### B04.2 · ¿Cuándo actúa un agente en nombre de un usuario y cuándo con autoridad propia, y cómo queda registrada esa diferencia?

- **Por qué importa:** La responsabilidad, los permisos y la auditoría cambian según quién delega y qué se delega.
- **Buena práctica (evidencia esperada):** Patrones aprobados de delegación (en nombre del usuario o autónomo), registros que distinguen persona y agente en cada acción, y consentimientos auditables.
- **Postura de Microsoft:** SAF distingue la IA interactiva, que usa la identidad humana y plantea el desafío de saber si actuó la persona o el agente, de los agentes autónomos con identidad propia, cuyo desafío es gestionar todo el ciclo de vida de esa identidad.
- **Capacidades Microsoft:** Microsoft Entra Agent ID; Microsoft Entra ID (flujos en nombre del usuario)
- **Cruce de marcos:** NIST — CSF PR.AA · AI RMF GOVERN 3.2 · NCCoE identidad y autorización de agentes (borrador) | CIS — CIS 6 · guía CIS para agentes de IA | The Open Group — sin referencia directa | ISACA — COBIT DSS05 · DSS06 · AAISM D3 | CSA — AICM IAM · Agentic AI IAM (CSA) | MCSB — IM
- **Anclaje y COE:** Atlas — AI & AGENTS / Limitar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Acceso e identidad | COE — Arquitectura y patrones seguros | Responsable sugerido — IAM + Arquitectura | Ola 1 (30–90 días)

#### B04.3 · ¿Aplicamos mínimo privilegio y agencia mínima a los agentes: solo los datos, herramientas y acciones necesarios para su propósito?

- **Por qué importa:** Los modelos generativos tienen más capacidades de las que cualquier aplicación necesita; los permisos amplios convierten un error en un incidente.
- **Buena práctica (evidencia esperada):** Permisos definidos por propósito, separación entre lectura y escritura, operaciones sensibles con aprobación y pruebas que verifican lo que el agente no puede hacer.
- **Postura de Microsoft:** SAF exige aplicar estrictamente el mínimo privilegio a las identidades de agentes y aplicaciones y recuerda que, aunque el modelo pueda hacer algo, eso no significa que la aplicación deba permitirlo.
- **Capacidades Microsoft:** Microsoft Entra Agent ID; acceso condicional para agentes; paquetes de acceso de Microsoft Entra ID Governance
- **Cruce de marcos:** NIST — CSF PR.AA · AI RMF MAP 3.5 · MANAGE 1.3 | CIS — CIS 6 (6.8) · guía CIS para agentes de IA | The Open Group — Zero Trust Commandments | ISACA — COBIT DSS05 · AAISM D3 | CSA — AICM IAM | MCSB — PA · IM · AI-4
- **Anclaje y COE:** Atlas — AI & AGENTS / Limitar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Acceso e identidad | COE — Plataforma e ingeniería de controles | Responsable sugerido — IAM + Dueño del agente | Ola 0 (0–30 días)

#### B04.4 · ¿Los permisos de los agentes son temporales, se revisan periódicamente y pueden revocarse de inmediato?

- **Por qué importa:** Los permisos permanentes acumulan exposición; los que no se pueden revocar rápido impiden contener un incidente.
- **Buena práctica (evidencia esperada):** Asignaciones con vencimiento, revisiones de acceso periódicas que incluyen a los agentes y revocación probada con tiempos medidos.
- **Postura de Microsoft:** Microsoft Entra ID Governance permite asignar a los agentes paquetes de acceso con vencimiento, con aviso al patrocinador para extenderlos, y deshabilitar identidades de agentes; las revisiones de acceso específicas para agentes no están confirmadas.
- **Capacidades Microsoft:** Microsoft Entra ID Governance (paquetes de acceso); Microsoft Entra Agent ID
- **Cruce de marcos:** NIST — CSF PR.AA · AI RMF MANAGE 2.4 | CIS — CIS 6 (6.2) · guía CIS para agentes de IA | The Open Group — sin referencia directa | ISACA — COBIT DSS05 · AAISM D3 | CSA — AICM IAM | MCSB — PA · AI-4
- **Anclaje y COE:** Atlas — AI & AGENTS / Limitar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Acceso e identidad | COE — Plataforma e ingeniería de controles | Responsable sugerido — IAM | Ola 1 (30–90 días)

#### B04.5 · ¿Aplicamos acceso condicional y protección basada en riesgo a los agentes, como a cualquier otra identidad?

- **Por qué importa:** Una identidad de agente comprometida se comporta como cualquier cuenta robada, pero a velocidad de máquina.
- **Buena práctica (evidencia esperada):** Políticas de acceso condicional que incluyen identidades de agentes, detección de riesgo y bloqueo automático ante anomalías.
- **Postura de Microsoft:** Microsoft extiende el acceso condicional a las identidades de agentes, con plantillas como bloquear agentes de alto riesgo (requiere Microsoft 365 E7 o Agent 365 con Entra ID P1); la protección de identidad basada en riesgo para agentes está en versión preliminar.
- **Capacidades Microsoft:** Acceso condicional para agentes (Microsoft Entra); ID Protection para agentes (versión preliminar)
- **Cruce de marcos:** NIST — CSF PR.AA · DE.CM | CIS — CIS 6 · guía CIS para agentes de IA | The Open Group — Zero Trust Commandments | ISACA — COBIT DSS05 · AAISM D3 | CSA — AICM IAM | MCSB — IM
- **Anclaje y COE:** Atlas — AI & AGENTS / Contener | TheNextCISO — CISO-DO (operación de dominios) | SAF — Acceso e identidad | COE — Plataforma e ingeniería de controles | Responsable sugerido — IAM | Ola 1 (30–90 días)

#### B04.6 · ¿Cómo evitamos que los agentes usen secretos estáticos (claves de API, contraseñas) y cómo los protegemos cuando no hay alternativa?

- **Por qué importa:** Los secretos incrustados en agentes o instrucciones se filtran y no se rotan.
- **Buena práctica (evidencia esperada):** Identidades administradas o federadas por defecto, secretos en bóvedas con rotación y detección de secretos en código y configuraciones.
- **Postura de Microsoft:** Microsoft recomienda identidades administradas y credenciales federadas en lugar de secretos, almacenamiento en Azure Key Vault y detección de secretos en los repositorios.
- **Capacidades Microsoft:** Identidades administradas; Microsoft Entra Agent ID; Azure Key Vault; detección de secretos de GitHub
- **Cruce de marcos:** NIST — CSF PR.AA · PR.DS | CIS — CIS 3 (3.11) · CIS 16 | The Open Group — sin referencia directa | ISACA — COBIT DSS05 · AAISM D3 | CSA — AICM IAM · CEK | MCSB — IM · DP
- **Anclaje y COE:** Atlas — AI & AGENTS / Limitar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Seguridad del desarrollo | COE — Plataforma e ingeniería de controles | Responsable sugerido — Ingeniería + IAM | Ola 1 (30–90 días)

#### B04.7 · ¿Cómo controlamos la delegación entre agentes para que no se escalen privilegios ni se oculte quién originó una acción?

- **Por qué importa:** En los sistemas multiagente, cada salto puede ampliar permisos o perder trazabilidad.
- **Buena práctica (evidencia esperada):** Reglas de delegación entre agentes, alcance acotado por salto, propagación del contexto de identidad de origen y registro de la cadena completa.
- **Postura de Microsoft:** El modelo de responsabilidad compartida para agentes de IA de Microsoft agrega las capas de orquestación, herramientas y memoria; SAF advierte que los sistemas multiagente aumentan la complejidad y exige alcance y privilegios definidos, y acciones visibles y trazables.
- **Capacidades Microsoft:** Modelo de responsabilidad compartida para agentes de IA; Microsoft Entra Agent ID; Microsoft Agent 365
- **Cruce de marcos:** NIST — AI RMF MAP 4 · GOVERN 3.2 · CSF PR.AA · COSIS (casos multiagente) | CIS — CIS 6 · guía CIS para agentes de IA | The Open Group — sin referencia directa | ISACA — COBIT DSS05 · DSS06 · AAISM D3 | CSA — AICM IAM · MAESTRO L7 · Agentic AI IAM (CSA) | MCSB — IM · PA · AI-4
- **Anclaje y COE:** Atlas — AI & AGENTS / Limitar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Acceso e identidad | COE — Arquitectura y patrones seguros | Responsable sugerido — Arquitectura + IAM | Ola 2 (90–180 días)

#### B04.8 · ¿Separamos funciones entre quien construye un agente, quien aprueba sus permisos y quien lo pone en producción?

- **Por qué importa:** Concentrar las tres funciones en una persona elimina el control independiente sobre la autoridad del agente.
- **Buena práctica (evidencia esperada):** Roles separados en la plataforma, aprobación de permisos por un tercero, despliegue mediante canalización controlada y evidencia en cada versión.
- **Postura de Microsoft:** Los agentes publicados para toda la organización requieren aprobación del administrador en el centro de administración de Microsoft 365 (activada por defecto en inquilinos con Copilot), que puede limitar su audiencia; Copilot Studio permite separar roles por entorno y desplegar mediante canalizaciones.
- **Capacidades Microsoft:** Copilot Studio (roles y canalizaciones); centro de administración de Microsoft 365 (aprobación de agentes); flujo de consentimiento administrativo de Microsoft Entra
- **Cruce de marcos:** NIST — CSF PR.AA · GV.RR | CIS — CIS 6 (6.8) | The Open Group — TOGAF Fase G | ISACA — COBIT DSS06 · BAI06 · AAISM D1 | CSA — AICM IAM · CCC | MCSB — PA · DS
- **Anclaje y COE:** Atlas — ORGANIZATION / Limitar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Seguridad del desarrollo | COE — Gobierno, políticas y decisiones | Responsable sugerido — COE de IA | Ola 1 (30–90 días)

#### B04.9 · ¿Cómo verificamos la identidad de quien interactúa con nuestros agentes, sea una persona o un agente externo?

- **Por qué importa:** Un agente que no verifica a su interlocutor puede entregar datos o ejecutar acciones para un impostor.
- **Buena práctica (evidencia esperada):** Autenticación obligatoria para los agentes con acceso a datos o acciones, autorización por usuario y reglas explícitas para agentes externos.
- **Postura de Microsoft:** El principio de verificar explícitamente se aplica también a la IA: SAF pide verificar todas las identidades que acceden a aplicaciones de IA.
- **Capacidades Microsoft:** Microsoft Entra ID; Copilot Studio (autenticación de agentes); Microsoft Entra Agent ID
- **Cruce de marcos:** NIST — CSF PR.AA | CIS — CIS 6 (6.3) · guía CIS para agentes de IA | The Open Group — Zero Trust Commandments | ISACA — COBIT DSS05 · AAISM D3 | CSA — AICM IAM · AIS | MCSB — IM
- **Anclaje y COE:** Atlas — AI & AGENTS / Limitar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Acceso e identidad | COE — Plataforma e ingeniería de controles | Responsable sugerido — IAM + Dueño del agente | Ola 1 (30–90 días)

### B05 — Datos para la IA: exposición, protección y ciclo de vida

*La IA amplifica lo bueno y lo malo de la gestión de datos existente.*

#### B05.1 · ¿Corregimos la sobreexposición de datos (permisos excesivos, sitios abiertos, enlaces compartidos) antes de habilitar copilotos y agentes que la amplifican?

- **Por qué importa:** La IA facilita encontrar información; si los permisos son excesivos, encontrará lo que nadie debía ver.
- **Buena práctica (evidencia esperada):** Evaluación de sobreexposición antes del despliegue, corrección priorizada de sitios y permisos, restricciones temporales donde haga falta y medición continua.
- **Postura de Microsoft:** SAF advierte que la IA facilita el descubrimiento de datos, por lo que deben corregirse antes la clasificación y los permisos excesivos. Purview DSPM evalúa cada semana la sobreexposición de los sitios de SharePoint más usados, y SharePoint Advanced Management (incluido con licencias de Copilot) aporta Restricted Content Discovery, un control temporal que no cambia permisos, e informes de permisos.
- **Capacidades Microsoft:** Microsoft Purview DSPM (evaluaciones de sobreexposición); SharePoint Advanced Management (Restricted Content Discovery, informes y revisiones de acceso)
- **Cruce de marcos:** NIST — CSF PR.DS · PR.AA · AI RMF MAP 4 · AI 600-1 (Data Privacy) | CIS — CIS 3 (3.3) | The Open Group — sin referencia directa | ISACA — COBIT APO14 · DSS05 · AAISM D3 | CSA — AICM DSP | MCSB — DP
- **Anclaje y COE:** Atlas — TECHNOLOGY / Limitar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Seguridad de datos | COE — Plataforma e ingeniería de controles | Responsable sugerido — Data Officer + CISO | Ola 0 (0–30 días) | relevante para el directorio | pregunta prioritaria para el directorio

#### B05.2 · ¿Las etiquetas de confidencialidad y sus permisos de uso se respetan cuando la IA lee, resume o genera contenido?

- **Por qué importa:** Si la IA ignora las etiquetas, cualquier resumen se convierte en una vía de fuga.
- **Buena práctica (evidencia esperada):** Etiquetas aplicadas al contenido sensible, herencia de etiquetas en el contenido generado, pruebas de que la IA respeta los derechos de uso y DLP asociado.
- **Postura de Microsoft:** Con contenido cifrado, Microsoft 365 Copilot exige que el usuario tenga los derechos de uso VIEW y EXTRACT, muestra la etiqueta más restrictiva de sus fuentes y el contenido generado en Word, PowerPoint y Outlook hereda la etiqueta de mayor prioridad.
- **Capacidades Microsoft:** Microsoft Purview Information Protection; Microsoft 365 Copilot
- **Cruce de marcos:** NIST — CSF PR.DS | CIS — CIS 3 (3.7) | The Open Group — sin referencia directa | ISACA — COBIT APO14 · AAISM D3 | CSA — AICM DSP | MCSB — DP
- **Anclaje y COE:** Atlas — TECHNOLOGY / Limitar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Seguridad de datos | COE — Plataforma e ingeniería de controles | Responsable sugerido — Seguridad de datos | Ola 0 (0–30 días)

#### B05.3 · ¿Qué datos pueden usarse para entrenar, ajustar o fundamentar modelos y agentes, y cómo se aprueba cada fuente?

- **Por qué importa:** Los datos de entrenamiento y de fundamentación determinan la calidad de las respuestas y lo que la IA puede revelar.
- **Buena práctica (evidencia esperada):** Política de fuentes por clasificación, aprobación del dueño de los datos, registro de procedencia y revisión de los derechos de uso.
- **Postura de Microsoft:** SAF recomienda gobernar los datos de entrenamiento, ajuste y fundamentación (grounding) para mejorar la calidad y reducir imprecisiones; en Microsoft 365 Copilot, los prompts, las respuestas y los datos de Microsoft Graph no se usan para entrenar modelos fundacionales.
- **Capacidades Microsoft:** Microsoft Purview (Data Map, Unified Catalog); Microsoft Foundry
- **Cruce de marcos:** NIST — AI RMF MAP 4 · GOVERN 6.1 · MEASURE 2.10 | CIS — CIS 3 (3.1, 3.8) | The Open Group — TOGAF Fase C (datos) | ISACA — COBIT APO14 · BAI03 · AAISM D2 | CSA — AICM DSP · MAESTRO L2 | MCSB — DP
- **Anclaje y COE:** Atlas — AI & AGENTS / Limitar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Seguridad de datos | COE — Riesgo, cumplimiento y aseguramiento | Responsable sugerido — Data Officer | Ola 1 (30–90 días)

#### B05.4 · ¿Cómo evitamos que información sensible salga por prompts, respuestas, acciones de agentes o servicios de IA externos?

- **Por qué importa:** Los usuarios pegan datos en servicios de IA y los agentes pueden enviarlos a terceros sin intención maliciosa.
- **Buena práctica (evidencia esperada):** DLP aplicada a prompts y a servicios de IA externos, restricciones sobre contenido etiquetado, controles en el navegador y monitoreo de las acciones de los agentes.
- **Postura de Microsoft:** Purview DLP para Microsoft 365 Copilot impide que Copilot procese archivos y correos con las etiquetas elegidas, bloquea la búsqueda web cuando el prompt contiene información sensible y, en versión preliminar, bloquea prompts con tipos de información sensible; SAF pide asumir que cada respuesta puede filtrar datos.
- **Capacidades Microsoft:** Microsoft Purview DLP (ubicación Microsoft 365 Copilot y Copilot Chat, endpoint, navegador); Microsoft Purview DSPM
- **Cruce de marcos:** NIST — CSF PR.DS · AI RMF MANAGE 1.3 · AI 600-1 (Data Privacy) | CIS — CIS 3 (3.13) · guía CIS para LLM | The Open Group — sin referencia directa | ISACA — COBIT DSS05 · APO14 · AAISM D3 | CSA — AICM DSP | MCSB — DP
- **Anclaje y COE:** Atlas — AI & AGENTS / Limitar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Seguridad de datos | COE — Plataforma e ingeniería de controles | Responsable sugerido — Seguridad de datos | Ola 0 (0–30 días)

#### B05.5 · ¿Retenemos, auditamos y podemos buscar los prompts, respuestas y acciones de la IA según nuestras obligaciones legales?

- **Por qué importa:** Las interacciones con IA son registros de negocio: pueden ser requeridas en litigios, auditorías o investigaciones.
- **Buena práctica (evidencia esperada):** Políticas de retención para las interacciones de IA, auditoría habilitada, búsqueda y exportación probadas y acceso restringido a esos registros.
- **Postura de Microsoft:** Purview registra automáticamente las interacciones con Copilot y agentes en Audit (Standard), incluidos el identificador del agente y las detecciones de inyección indirecta y de jailbreak; ofrece ubicaciones de retención específicas para IA y búsqueda en eDiscovery. La auditoría de IA ajena a Microsoft usa facturación por consumo.
- **Capacidades Microsoft:** Microsoft Purview Audit; Data Lifecycle Management; eDiscovery
- **Cruce de marcos:** NIST — CSF DE.CM · RS.AN · AI RMF MANAGE 4.1 | CIS — CIS 8 | The Open Group — sin referencia directa | ISACA — COBIT MEA03 · APO14 | CSA — AICM LOG · SEF | MCSB — LT
- **Anclaje y COE:** Atlas — TRUST / Recuperar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Seguridad de datos | COE — Riesgo, cumplimiento y aseguramiento | Responsable sugerido — Compliance + Legal | Ola 1 (30–90 días)

#### B05.6 · ¿Cómo detectamos el uso riesgoso de IA por parte de personas internas (búsqueda de información sensible, exfiltración a través de la IA, uso de IA no autorizada)?

- **Por qué importa:** La IA facilita reunir y resumir información sensible a escala, para bien o para mal.
- **Buena práctica (evidencia esperada):** Indicadores de uso riesgoso de IA integrados al programa de riesgo interno, con seudonimización, investigación proporcional y protección adaptativa.
- **Postura de Microsoft:** SAF advierte que la IA amplifica el riesgo interno; Purview Insider Risk Management ofrece la plantilla de uso riesgoso de IA (y otra para agentes riesgosos, en versión preliminar), y Communication Compliance una plantilla para detectar interacciones con Copilot y agentes.
- **Capacidades Microsoft:** Microsoft Purview Insider Risk Management (uso riesgoso de IA); Communication Compliance; Adaptive Protection
- **Cruce de marcos:** NIST — CSF DE.CM · PR.DS | CIS — CIS 3 (3.14) · CIS 13 | The Open Group — sin referencia directa | ISACA — COBIT APO07 · DSS05 · AAISM D2 | CSA — AICM HRS · DSP | MCSB — DP · LT
- **Anclaje y COE:** Atlas — ORGANIZATION / Anticipar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Seguridad de datos | COE — Operaciones, detección y respuesta | Responsable sugerido — CISO + RR. HH. + Legal | Ola 2 (90–180 días)

#### B05.7 · ¿Protegemos la memoria persistente, el contexto compartido y los índices vectoriales de los agentes como datos sensibles?

- **Por qué importa:** La memoria de largo plazo hace más difícil predecir el comportamiento del agente y puede ser envenenada o filtrada.
- **Buena práctica (evidencia esperada):** Memoria e índices con control de acceso, cifrado, segmentación por usuario o caso, retención definida y capacidad de purga.
- **Postura de Microsoft:** SAF identifica la memoria y el contexto de largo plazo de los agentes como un factor que vuelve más difícil predecir su comportamiento y su riesgo; Microsoft recomienda aislar y proteger los almacenes de datos de las aplicaciones de IA con control de acceso y redes privadas.
- **Capacidades Microsoft:** Azure AI Search (seguridad); Microsoft Foundry (almacenes de agentes); Microsoft Defender for Cloud
- **Cruce de marcos:** NIST — CSF PR.DS · AI RMF MEASURE 2.7 | CIS — CIS 3 (3.3, 3.11) · guía CIS para agentes de IA | The Open Group — sin referencia directa | ISACA — COBIT DSS05 · APO14 · AAISM D3 | CSA — AICM DSP · MAESTRO L2 | MCSB — DP
- **Anclaje y COE:** Atlas — AI & AGENTS / Limitar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Seguridad de datos | COE — Arquitectura y patrones seguros | Responsable sugerido — Ingeniería de IA | Ola 2 (90–180 días)

#### B05.8 · ¿Cómo garantizamos la calidad, procedencia e integridad de los datos que alimentan a la IA para evitar envenenamiento y respuestas sin fundamento?

- **Por qué importa:** Los datos de mala calidad o manipulados producen respuestas erróneas con apariencia de certeza.
- **Buena práctica (evidencia esperada):** Controles de calidad e integridad sobre las fuentes, registro de procedencia, detección de respuestas sin fundamento y revisión de las fuentes de alto impacto.
- **Postura de Microsoft:** SAF recomienda evaluar las aplicaciones y agentes por riesgos de calidad y aplicar controles en ejecución contra respuestas sin fundamento. La detección de groundedness de Azure AI Content Safety se retira el 30 de abril de 2027; Microsoft orienta hacia las evaluaciones de Foundry o validaciones propias.
- **Capacidades Microsoft:** Evaluaciones de Microsoft Foundry; Azure AI Content Safety (detección de groundedness hasta abril de 2027)
- **Cruce de marcos:** NIST — AI RMF MEASURE 2.5 · MAP 2.3 · AI 100-2 E2025 · AI 600-1 (Confabulation) | CIS — CIS 3 | The Open Group — sin referencia directa | ISACA — COBIT APO14 · APO11 · AAISM D3 | CSA — AICM DSP · MDS | MCSB — DP
- **Anclaje y COE:** Atlas — AI & AGENTS / Anticipar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Seguridad de datos | COE — Arquitectura y patrones seguros | Responsable sugerido — Data Officer + Ingeniería de IA | Ola 2 (90–180 días)

#### B05.9 · ¿Qué compromisos contractuales tenemos de nuestros proveedores de IA sobre uso, residencia, retención y no entrenamiento con nuestros datos?

- **Por qué importa:** Sin compromisos escritos, los datos enviados a un servicio de IA pueden usarse para fines no previstos.
- **Buena práctica (evidencia esperada):** Cláusulas revisadas por proveedor, registro de compromisos, verificación periódica y alternativas si el proveedor cambia sus condiciones.
- **Postura de Microsoft:** La protección de datos empresariales de Microsoft 365 Copilot se rige por el anexo de protección de datos (DPA) y los Product Terms, con Microsoft como encargado del tratamiento; los prompts, las respuestas y los datos de Graph no entrenan modelos fundacionales. Excepciones a revisar: en las búsquedas web en Bing Microsoft actúa como responsable independiente, y los modelos de Anthropic quedan fuera del EU Data Boundary.
- **Capacidades Microsoft:** Protección de datos empresariales de Microsoft 365 Copilot; Microsoft Products and Services Data Protection Addendum; Product Terms
- **Cruce de marcos:** NIST — AI RMF GOVERN 6.1 · CSF GV.SC | CIS — CIS 15 (15.4) | The Open Group — sin referencia directa | ISACA — COBIT APO10 · APO09 · AAISM D2 | CSA — AICM STA · DSP | MCSB — GS · DP
- **Anclaje y COE:** Atlas — TRUST / Limitar | TheNextCISO — CISO-OS (gobierno) | SAF — Seguridad de datos | COE — Riesgo, cumplimiento y aseguramiento | Responsable sugerido — Legal + Compras + DPO | Ola 1 (30–90 días)

### B06 — Amenazas a modelos, aplicaciones y agentes

*Las formas nuevas en que los sistemas de IA pueden ser engañados, abusados o comprometidos.*

#### B06.1 · ¿Modelamos las amenazas de cada sistema de IA crítico, incluidos el engaño, el abuso de herramientas, la fuga de datos y el alcance de la autonomía?

- **Por qué importa:** Los sistemas de IA son nuevos para todos y aún no existen listas de verificación maduras como las de tecnologías conocidas.
- **Buena práctica (evidencia esperada):** Modelo de amenazas por sistema crítico, actualizado en cada cambio relevante, con participación de seguridad, desarrollo, negocio y especialistas en MCP.
- **Postura de Microsoft:** SAF pide modelar las amenazas de todos los sistemas de IA con las cuatro preguntas del Threat Modeling Manifesto y extiende STRIDE (STRIDER-TIM) con categorías como engaño, abuso interno y abuso de mantenimiento; también advierte no tercerizar en la IA el pensamiento crítico.
- **Capacidades Microsoft:** SAF (modelado de amenazas, STRIDER-TIM); Microsoft Threat Modeling Tool; Security Development Lifecycle
- **Cruce de marcos:** NIST — AI RMF MAP 4.1 · MEASURE 2.7 · CSF ID.RA | CIS — CIS 16 (16.14) · guía CIS para agentes de IA | The Open Group — Open FAIR O-RT (escenarios) | ISACA — COBIT APO12 · BAI03 · AAISM D2 | CSA — AICM MDS · AIS · MAESTRO (7 capas) | MCSB — DS
- **Anclaje y COE:** Atlas — AI & AGENTS / Anticipar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Seguridad del desarrollo | COE — Arquitectura y patrones seguros | Responsable sugerido — Arquitectura + AppSec | Ola 0 (0–30 días)

#### B06.2 · ¿Cómo nos protegemos de la inyección indirecta de instrucciones desde correos, documentos, páginas web o respuestas de herramientas?

- **Por qué importa:** Un agente que lee contenido externo puede recibir órdenes ocultas y actuar contra su propio usuario.
- **Buena práctica (evidencia esperada):** Separación entre instrucciones y datos, filtros de ataques en documentos, permisos acotados del agente y detección de desvíos de objetivo.
- **Postura de Microsoft:** SAF pide asumir que cada prompt puede tener intención maliciosa. Prompt Shields detecta ataques directos y en documentos —en Foundry la detección en documentos viene desactivada por defecto y debe activarse— y el análisis de respuestas de herramientas está en versión preliminar; Microsoft Entra Internet Access agrega protección contra inyección de prompts en la red.
- **Capacidades Microsoft:** Azure AI Content Safety (Prompt Shields; spotlighting en versión preliminar); Defender for AI Services; Microsoft Entra Internet Access (protección contra inyección de prompts)
- **Cruce de marcos:** NIST — AI RMF MEASURE 2.7 · AI 100-2 E2025 · CSF PR.PS · AI 600-1 (Information Security) | CIS — CIS 16 · guía CIS para LLM · guía CIS para agentes de IA | The Open Group — sin referencia directa | ISACA — COBIT DSS05 · BAI03 · AAISM D3 | CSA — AICM MDS · AIS | MCSB — DS · AI-2
- **Anclaje y COE:** Atlas — AI & AGENTS / Limitar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Seguridad del desarrollo | COE — Plataforma e ingeniería de controles | Responsable sugerido — AppSec + Ingeniería de IA | Ola 1 (30–90 días)

#### B06.3 · ¿Limitamos las capacidades del modelo a lo que el caso de uso necesita y validamos sus salidas antes de que desencadenen acciones?

- **Por qué importa:** Los modelos generativos son sobrecapaces: pueden hacer mucho más de lo que una aplicación debería permitir.
- **Buena práctica (evidencia esperada):** Restricción por defecto de temas y acciones, validación determinística de las salidas antes de ejecutar, listas de acciones permitidas y pruebas negativas.
- **Postura de Microsoft:** SAF caracteriza a la IA generativa como sobrecapaz y exige restricción por defecto con guardrails adicionales; la detección de adherencia a la tarea (Task Adherence, versión preliminar) identifica llamadas a herramientas que no coinciden con la intención del usuario para bloquearlas o escalarlas a una persona.
- **Capacidades Microsoft:** Microsoft Foundry (guardrails y filtros de contenido); Azure AI Content Safety (Task Adherence, versión preliminar)
- **Cruce de marcos:** NIST — AI RMF MAP 3.3 · MANAGE 1.3 · CSF PR.PS | CIS — CIS 16 · guía CIS para LLM | The Open Group — Security Principles for Architecture | ISACA — COBIT BAI03 · AAISM D3 | CSA — AICM AIS · MDS | MCSB — DS · AI-2 · AI-3
- **Anclaje y COE:** Atlas — AI & AGENTS / Limitar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Seguridad del desarrollo | COE — Arquitectura y patrones seguros | Responsable sugerido — Ingeniería de IA | Ola 1 (30–90 días)

#### B06.4 · ¿Cómo aseguramos la cadena de suministro de IA: modelos de terceros, pesos, bibliotecas, conjuntos de datos, plantillas de agentes y servidores MCP?

- **Por qué importa:** Un modelo o componente comprometido puede introducir puertas traseras difíciles de detectar.
- **Buena práctica (evidencia esperada):** Fuentes aprobadas, verificación de integridad y procedencia, análisis de componentes, lista de materiales y proceso de actualización controlado.
- **Postura de Microsoft:** SAF recomienda integrar modelos validados rigurosamente en seguridad, protección y adecuación al caso de uso; la gestión de postura de seguridad de IA de Defender for Cloud descubre los componentes de IA en Azure, AWS y Google Cloud y analiza rutas de ataque sobre ellos.
- **Capacidades Microsoft:** Catálogo de modelos de Microsoft Foundry; Microsoft Defender for Cloud (postura de IA); GitHub Advanced Security
- **Cruce de marcos:** NIST — SP 800-218A · AI RMF GOVERN 6 · MAP 4 · CSF GV.SC · AI 600-1 (Value Chain and Component Integration) | CIS — CIS 16 · CIS 2 · guía CIS para MCP | The Open Group — sin referencia directa | ISACA — COBIT APO10 · BAI03 · AAISM D3 | CSA — AICM STA · MDS · MAESTRO L1 | MCSB — DS · AI-1
- **Anclaje y COE:** Atlas — TECHNOLOGY / Limitar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Seguridad del desarrollo | COE — Arquitectura y patrones seguros | Responsable sugerido — Ingeniería de IA + AppSec | Ola 2 (90–180 días)

#### B06.5 · ¿Qué controles tenemos contra el envenenamiento de herramientas y los cambios maliciosos en servidores MCP o complementos ya aprobados?

- **Por qué importa:** Una descripción de herramienta modificada puede redirigir el comportamiento del agente sin cambiar su código.
- **Buena práctica (evidencia esperada):** Versiones fijadas, revisión de los cambios en metadatos y permisos, pasarela con políticas y autenticación, y monitoreo de invocaciones anómalas.
- **Postura de Microsoft:** La guía de Microsoft para MCP pide tratar las descripciones y salidas de las herramientas como no confiables, fijar los esquemas aprobados, inventariar los servidores, usar OAuth 2.1 con PKCE y tokens ligados a su audiencia, y gobernar el acceso con Azure API Management; el firewall de MCP de Global Secure Access está en versión preliminar.
- **Capacidades Microsoft:** Azure API Management (servidores MCP); políticas de conectores avanzados; Microsoft Entra (seguridad de servidores MCP)
- **Cruce de marcos:** NIST — AI RMF MEASURE 2.7 · MANAGE 3.1 · CSF PR.PS | CIS — CIS 16 · CIS 2 · guía CIS para MCP · CIS MCP Server Benchmark | The Open Group — sin referencia directa | ISACA — COBIT BAI06 · DSS05 · AAISM D3 | CSA — AICM AIS · STA · MAESTRO L3 | MCSB — DS · NS
- **Anclaje y COE:** Atlas — TECHNOLOGY / Limitar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Seguridad del desarrollo | COE — Plataforma e ingeniería de controles | Responsable sugerido — Arquitectura + AppSec | Ola 2 (90–180 días)

#### B06.6 · ¿Hacemos red teaming de IA antes de producción y después de cada cambio material de modelo, instrucciones, herramientas o datos?

- **Por qué importa:** Las fallas de la IA aparecen en la interacción; solo las pruebas adversarias realistas las revelan.
- **Buena práctica (evidencia esperada):** Red teaming proporcional al riesgo, automatizado donde se pueda y humano en los casos críticos, con hallazgos gestionados hasta su cierre.
- **Postura de Microsoft:** El AI Red Team de Microsoft publicó las lecciones de probar más de 100 productos de IA generativa (enero de 2025) y la herramienta abierta PyRIT; el AI Red Teaming Agent de Foundry, disponible de forma general en el portal, combina PyRIT con evaluadores de riesgo y mide la tasa de éxito de ataques, incluidos riesgos agénticos como acciones prohibidas e inyección indirecta.
- **Capacidades Microsoft:** PyRIT; AI Red Teaming Agent (Microsoft Foundry); SAF
- **Cruce de marcos:** NIST — AI RMF MEASURE 2.7 · MEASURE 1.3 | CIS — CIS 18 · guía CIS para agentes de IA | The Open Group — sin referencia directa | ISACA — COBIT MEA02 · BAI07 · AAISM D3 | CSA — Agentic AI Red Teaming Guide (CSA) · AICM A&A · TVM | MCSB — DS · AI-7
- **Anclaje y COE:** Atlas — AI & AGENTS / Anticipar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Seguridad del desarrollo | COE — Operaciones, detección y respuesta | Responsable sugerido — Seguridad ofensiva + Ingeniería de IA | Ola 1 (30–90 días)

#### B06.7 · ¿Cómo protegemos los modelos y los endpoints de IA contra robo, extracción, abuso de capacidad y consumo descontrolado de costos?

- **Por qué importa:** Los endpoints de IA son activos costosos y valiosos: su abuso genera pérdidas económicas y exposición de propiedad intelectual.
- **Buena práctica (evidencia esperada):** Acceso privado y autenticado, límites de consumo por cliente, monitoreo de uso anómalo y alertas de costos.
- **Postura de Microsoft:** Defender for AI Services, disponible de forma general, genera alertas de fuga y envenenamiento de datos, jailbreak y robo de credenciales e integra con Defender XDR; la pasarela de IA de Azure API Management aplica límites de tokens por consumidor.
- **Capacidades Microsoft:** Microsoft Defender for Cloud (protección contra amenazas para IA); Azure API Management (pasarela de IA); Microsoft Foundry (cuotas)
- **Cruce de marcos:** NIST — AI RMF MEASURE 2.7 · AI 100-2 E2025 · CSF PR.PS | CIS — CIS 12 · CIS 13 | The Open Group — sin referencia directa | ISACA — COBIT DSS05 · BAI04 · AAISM D3 | CSA — AICM MDS · IVS | MCSB — NS · DS
- **Anclaje y COE:** Atlas — TECHNOLOGY / Limitar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Seguridad de infraestructura | COE — Plataforma e ingeniería de controles | Responsable sugerido — Plataforma de IA | Ola 2 (90–180 días)

#### B06.8 · ¿Cómo nos defendemos de atacantes que usan IA (phishing personalizado, deepfakes, malware generado, descubrimiento acelerado de vulnerabilidades)?

- **Por qué importa:** La IA reduce el costo y el tiempo de los ataques y mejora su calidad.
- **Buena práctica (evidencia esperada):** Escenarios de ataque potenciados por IA en el modelo de amenazas, controles reforzados en identidad, correo y vulnerabilidades, y formación específica.
- **Postura de Microsoft:** Microsoft observa que los atacantes usan la IA en toda la cadena de ataque —según el MDDR 2025, el phishing potenciado con IA es tres veces más eficaz— y recomienda responder con identidad resistente al phishing y con detección, respuesta y recuperación automatizadas.
- **Capacidades Microsoft:** Microsoft Defender XDR; Microsoft Defender for Office 365; Microsoft Security Copilot
- **Cruce de marcos:** NIST — IR 8596 borrador (Thwart) · CSF ID.RA · DE.AE | CIS — CIS 9 · CIS 14 · CIS 7 | The Open Group — Open FAIR O-RT (capacidad de la amenaza) | ISACA — COBIT APO12 · DSS05 · AAISM D2 | CSA — AICM TVM | MCSB — LT · ES
- **Anclaje y COE:** Atlas — RISK / Anticipar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Operaciones de seguridad (SecOps/SOC) | COE — Operaciones, detección y respuesta | Responsable sugerido — CISO + Líder SOC | Ola 1 (30–90 días) | relevante para el directorio

#### B06.9 · ¿Conocemos los modos de falla propios de los sistemas agénticos (memoria envenenada, objetivos secuestrados, colusión entre agentes, fallos en cascada) y cuáles aplican a nuestros casos?

- **Por qué importa:** Los sistemas agénticos fallan de formas nuevas que los controles clásicos no contemplan.
- **Buena práctica (evidencia esperada):** Catálogo de modos de falla aplicables por sistema, pruebas específicas y controles asignados a cada uno.
- **Postura de Microsoft:** El AI Red Team de Microsoft publicó en abril de 2025 una taxonomía de modos de falla en sistemas de IA agéntica, que distingue fallas de seguridad y de protección, nuevas y existentes (por ejemplo, el envenenamiento de memoria), como referencia para diseñar y probar agentes.
- **Capacidades Microsoft:** Taxonomy of Failure Mode in Agentic AI Systems (Microsoft AI Red Team)
- **Cruce de marcos:** NIST — AI RMF MAP 4 · MEASURE 2.6 · MEASURE 2.7 · COSIS (agentes) | CIS — guía CIS para agentes de IA | The Open Group — sin referencia directa | ISACA — COBIT APO12 · AAISM D2 | CSA — MAESTRO · AICM MDS | MCSB — DS
- **Anclaje y COE:** Atlas — AI & AGENTS / Anticipar | TheNextCISO — CISO-NX (nueva generación) | SAF — Seguridad del desarrollo | COE — Arquitectura y patrones seguros | Responsable sugerido — Arquitectura + Seguridad ofensiva | Ola 2 (90–180 días)

### B07 — Autonomía, supervisión humana y contención

*Cuánta autonomía otorgar, dónde intervenir y cómo detener a tiempo.*

#### B07.1 · ¿Qué nivel de autonomía permitimos a cada agente (sugerir, ejecutar con aprobación, ejecutar y notificar, ejecutar sin supervisión) y con qué criterio se asigna?

- **Por qué importa:** La autonomía es la fuente del valor y del riesgo de los agentes; asignarla sin criterio es delegar sin gobierno.
- **Buena práctica (evidencia esperada):** Escala de autonomía documentada, criterios basados en impacto, reversibilidad, velocidad y precisión de los controles, y promoción de nivel solo con evidencia.
- **Postura de Microsoft:** SAF pide analizar qué puede hacer cada agente sin una persona que lo supervise; según el modelo de responsabilidad compartida para agentes de Microsoft, la aprobación humana de las acciones de alto impacto es siempre responsabilidad del cliente. Los flujos de agentes de Copilot Studio incluyen aprobaciones humanas (las aprobaciones multietapa están en versión preliminar).
- **Capacidades Microsoft:** Copilot Studio (aprobaciones humanas en flujos de agentes); agentes de Security Copilot (aprobación del administrador)
- **Cruce de marcos:** NIST — AI RMF MAP 3.5 · GOVERN 3.2 · MAP 2.2 · AI 600-1 (Human-AI Configuration) | CIS — guía CIS para agentes de IA | The Open Group — sin referencia directa | ISACA — COBIT APO01 · DSS06 · AAISM D1 | CSA — AICM GRC · MAESTRO L3 | MCSB — AI-5
- **Anclaje y COE:** Atlas — ORGANIZATION / Limitar | TheNextCISO — CISO-NX (nueva generación) | SAF — Estrategia, integración y gobierno | COE — Gobierno, políticas y decisiones | Responsable sugerido — Comité de IA + Dueño del agente | Ola 0 (0–30 días) | relevante para el directorio | pregunta prioritaria para el directorio

#### B07.2 · ¿Tenemos un perfil de radio de impacto por agente (datos, herramientas, transacciones, acciones irreversibles) y una estimación de la pérdida máxima creíble por escenario?

- **Por qué importa:** Sin conocer el radio de impacto no se puede decidir cuánta autonomía es tolerable.
- **Buena práctica (evidencia esperada):** Perfil por agente con identidad, alcance, operaciones de escritura, límites, dependencias y mecanismo de revocación, más una estimación por escenario con supuestos e incertidumbre (ABRP y AMCL del AI CISO Atlas).
- **Postura de Microsoft:** Microsoft recomienda delimitar el alcance de datos, herramientas y acciones de cada agente y analizar las rutas de ataque hacia los activos críticos; SAF recomienda estimar la pérdida con Open FAIR o un método similar.
- **Capacidades Microsoft:** Microsoft Security Exposure Management (rutas de ataque); Microsoft Agent 365
- **Cruce de marcos:** NIST — AI RMF MAP 5.1 · MANAGE 1.2 · CSF ID.RA | CIS — CIS RAM v2.2 · guía CIS para agentes de IA | The Open Group — Open FAIR O-RT · O-RA | ISACA — COBIT APO12 · AAISM D2 | CSA — AICM GRC · MAESTRO | MCSB — GS · AI-4
- **Anclaje y COE:** Atlas — AI & AGENTS / Limitar | TheNextCISO — CISO-NX (nueva generación) | SAF — Gestión de la postura de seguridad | COE — Riesgo, cumplimiento y aseguramiento | Responsable sugerido — Arquitectura + CRO | Ola 1 (30–90 días) | relevante para el directorio | pregunta prioritaria para el directorio

#### B07.3 · ¿Qué acciones nunca puede ejecutar un agente sin intervención humana, y cómo se garantiza técnicamente y no solo con instrucciones al modelo?

- **Por qué importa:** Las instrucciones al modelo pueden eludirse; los límites deben imponerse fuera de él.
- **Buena práctica (evidencia esperada):** Lista de acciones con aprobación obligatoria, impuesta mediante permisos, políticas y validación determinística, y pruebas que intentan eludirla.
- **Postura de Microsoft:** Según el modelo de responsabilidad compartida para agentes de Microsoft, la aprobación humana de acciones de alto impacto es responsabilidad del cliente; SAF exige restricción por defecto y el principio de asumir compromiso. Task Adherence y la protección en tiempo real de agentes (ambas en versión preliminar) pueden bloquear llamadas a herramientas riesgosas antes de ejecutarse.
- **Capacidades Microsoft:** Microsoft Entra (permisos); Azure AI Content Safety (Task Adherence, versión preliminar); protección en tiempo real de agentes de Copilot Studio (versión preliminar)
- **Cruce de marcos:** NIST — AI RMF MAP 3.5 · MANAGE 2.4 · CSF PR.AA | CIS — CIS 6 · guía CIS para agentes de IA | The Open Group — Security Principles for Architecture | ISACA — COBIT DSS06 · BAI03 · AAISM D3 | CSA — AICM IAM · AIS | MCSB — PA · DS · AI-4 · AI-5
- **Anclaje y COE:** Atlas — AI & AGENTS / Contener | TheNextCISO — CISO-DO (operación de dominios) | SAF — Seguridad del desarrollo | COE — Arquitectura y patrones seguros | Responsable sugerido — Arquitectura + Dueño del agente | Ola 1 (30–90 días)

#### B07.4 · ¿Cómo evitamos que la fatiga de aprobaciones y el sesgo de automatización conviertan la supervisión humana en un trámite?

- **Por qué importa:** Una persona que aprueba cientos de acciones por día deja de leerlas; la supervisión nominal da una falsa seguridad.
- **Buena práctica (evidencia esperada):** Aprobaciones solo donde agregan control, contexto suficiente para decidir, muestreo de calidad, métricas de tasa de rechazo y rotación de revisores.
- **Postura de Microsoft:** Microsoft publica guías de interacción humano-IA y estudios sobre la sobredependencia de la IA, y SAF advierte no delegar en la IA el pensamiento crítico.
- **Capacidades Microsoft:** Guidelines for Human-AI Interaction (Microsoft); SAF
- **Cruce de marcos:** NIST — AI RMF GOVERN 3.2 · MAP 3.4 · AI 600-1 (Human-AI Configuration) | CIS — CIS 14 | The Open Group — sin referencia directa | ISACA — COBIT APO07 · DSS06 · AAISM D2 | CSA — AICM HRS | MCSB — AI-5
- **Anclaje y COE:** Atlas — ORGANIZATION / Anticipar | TheNextCISO — CISO-NX (nueva generación) | SAF — Estrategia, integración y gobierno | COE — Cultura, talento y adopción | Responsable sugerido — Dueños de procesos + COE de IA | Ola 2 (90–180 días)

#### B07.5 · ¿Podemos suspender, aislar o revocar un agente, o todos los de una clase, en minutos, y lo hemos ensayado?

- **Por qué importa:** Ante un agente comprometido, cada minuto de autonomía puede ampliar el daño.
- **Buena práctica (evidencia esperada):** Procedimiento de suspensión por agente y por clase, responsables con autoridad, tiempos medidos en ejercicios y verificación de que la suspensión fue efectiva.
- **Postura de Microsoft:** Microsoft Entra permite deshabilitar o bloquear agentes en tres niveles: un agente, su plantilla (blueprint, que también impide crear nuevos) o todo el inquilino mediante acceso condicional, con deshabilitación masiva; Agent 365 pone en cuarentena agentes no autorizados y el inventario de Power Platform bloquea agentes publicados.
- **Capacidades Microsoft:** Microsoft Entra Agent ID; Microsoft Agent 365 (cuarentena); inventario de Power Platform
- **Cruce de marcos:** NIST — AI RMF MANAGE 2.4 · CSF RS.MI | CIS — CIS 17 · CIS 6 (6.2) · guía CIS para agentes de IA | The Open Group — sin referencia directa | ISACA — COBIT DSS02 · DSS05 · AAISM D3 | CSA — AICM SEF · IAM | MCSB — IR
- **Anclaje y COE:** Atlas — AI & AGENTS / Contener | TheNextCISO — CISO-DO (operación de dominios) | SAF — Operaciones de seguridad (SecOps/SOC) | COE — Operaciones, detección y respuesta | Responsable sugerido — Líder SOC + COE de IA | Ola 1 (30–90 días) | relevante para el directorio | pregunta prioritaria para el directorio

#### B07.6 · ¿Qué límites operativos (presupuesto, cantidad de llamadas, montos, frecuencia, alcance) actúan como cortacircuitos ante comportamientos anómalos o en cascada?

- **Por qué importa:** Los agentes pueden entrar en bucles o cascadas que agotan recursos o multiplican acciones en segundos.
- **Buena práctica (evidencia esperada):** Límites por agente y por transacción, umbrales de detención automática, alertas y revisión de cada activación.
- **Postura de Microsoft:** La pasarela de IA de Azure API Management aplica límites de tokens por minuto y cuotas por consumidor, y Microsoft Foundry aplica cuotas; ambos funcionan como cortacircuitos ante consumos anómalos.
- **Capacidades Microsoft:** Azure API Management (pasarela de IA, llm-token-limit); Microsoft Foundry (cuotas)
- **Cruce de marcos:** NIST — AI RMF MANAGE 2.4 · MANAGE 1.3 | CIS — guía CIS para agentes de IA | The Open Group — sin referencia directa | ISACA — COBIT BAI04 · DSS01 · AAISM D3 | CSA — AICM IVS · MAESTRO L4 | MCSB — NS
- **Anclaje y COE:** Atlas — AI & AGENTS / Contener | TheNextCISO — CISO-DO (operación de dominios) | SAF — Seguridad de infraestructura | COE — Plataforma e ingeniería de controles | Responsable sugerido — Plataforma de IA | Ola 2 (90–180 días)

#### B07.7 · ¿Podemos revertir los efectos de una acción autónoma (deshacer, compensar, conciliar) y qué acciones son irreversibles por diseño?

- **Por qué importa:** Una acción reversible tiene un perfil de riesgo menor; las irreversibles requieren más control.
- **Buena práctica (evidencia esperada):** Catálogo de acciones con su mecanismo de reversión, registros suficientes para reconstruir el estado previo y pruebas de reversión.
- **Postura de Microsoft:** Silencio parcial: Microsoft no publica una guía específica de reversibilidad para agentes; sus capacidades de versiones, papelera y copias de seguridad apoyan la recuperación de los datos afectados.
- **Capacidades Microsoft:** Microsoft 365 Backup; control de versiones de SharePoint; Azure Backup
- **Cruce de marcos:** NIST — AI RMF MANAGE 4.1 · CSF RC.RP | CIS — CIS 11 | The Open Group — sin referencia directa | ISACA — COBIT DSS04 · BAI06 | CSA — AICM BCR | MCSB — BR
- **Anclaje y COE:** Atlas — TECHNOLOGY / Recuperar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Seguridad de infraestructura | COE — Arquitectura y patrones seguros | Responsable sugerido — Arquitectura + Dueño del proceso | Ola 2 (90–180 días)

#### B07.8 · ¿Cuál es nuestro presupuesto de tiempo de contención para un agente comprometido, y es menor que el tiempo en que el daño se vuelve material?

- **Por qué importa:** La contención solo sirve si llega antes de que el impacto supere el umbral tolerable.
- **Buena práctica (evidencia esperada):** Descomposición del tiempo (detectar, clasificar, decidir, contener, verificar) por escenario, comparada con el umbral de daño, con banda de incertidumbre y ensayo (CTB del AI CISO Atlas).
- **Postura de Microsoft:** Microsoft promueve la contención a velocidad de máquina mediante la interrupción automática de ataques y la respuesta asistida por IA.
- **Capacidades Microsoft:** Interrupción automática de ataques (Defender XDR); Microsoft Security Copilot
- **Cruce de marcos:** NIST — CSF RS.MI · DE.AE · AI RMF MANAGE 2.3 | CIS — CIS 17 | The Open Group — Open FAIR O-RT (magnitud de pérdida) | ISACA — COBIT DSS02 · AAISM D2 | CSA — AICM SEF | MCSB — IR
- **Anclaje y COE:** Atlas — TECHNOLOGY / Contener | TheNextCISO — CISO-DO (operación de dominios) | SAF — Operaciones de seguridad (SecOps/SOC) | COE — Operaciones, detección y respuesta | Responsable sugerido — Líder SOC | Ola 2 (90–180 días)

#### B07.9 · ¿Cómo aplicamos los requisitos legales de supervisión humana (por ejemplo, el artículo 14 de la Ley de IA de la UE) solo donde corresponden, sin extenderlos ni omitirlos?

- **Por qué importa:** Extender una obligación a todos los agentes paraliza; omitirla donde aplica expone a sanciones.
- **Buena práctica (evidencia esperada):** Análisis de aplicabilidad por sistema y jurisdicción, rol de la organización (proveedor o implementador) y medidas documentadas para los sistemas alcanzados.
- **Postura de Microsoft:** Microsoft publica su enfoque de cumplimiento de la Ley de IA de la UE y ofrece una evaluación de esa ley en Compliance Manager.
- **Capacidades Microsoft:** Microsoft Purview Compliance Manager (evaluación de la Ley de IA de la UE); Microsoft Trust Center
- **Cruce de marcos:** NIST — AI RMF GOVERN 1.1 · MAP 3.5 | CIS — sin referencia directa | The Open Group — sin referencia directa | ISACA — COBIT MEA03 · AAISM D1 | CSA — AICM GRC (correspondencia con la Ley de IA de la UE) | MCSB — AI-5
- **Anclaje y COE:** Atlas — ORGANIZATION / Gobernar | TheNextCISO — CISO-NX (nueva generación) | SAF — Estrategia, integración y gobierno | COE — Riesgo, cumplimiento y aseguramiento | Responsable sugerido — Legal + Compliance | Ola 2 (90–180 días)

### B08 — Evaluación, pruebas y aseguramiento continuo de la IA

*La confianza en la IA como resultado de pruebas recurrentes y evidencia verificable.*

#### B08.1 · ¿Qué evaluaciones (calidad, fundamentación, seguridad, sesgo, cumplimiento de la tarea) son obligatorias antes de producción y con qué umbrales de aceptación?

- **Por qué importa:** Sin criterios previos, la decisión de pasar a producción depende de la impresión de quien hace la demostración.
- **Buena práctica (evidencia esperada):** Batería de evaluaciones por nivel de riesgo, umbrales aprobados, resultados archivados y decisión de puesta en producción registrada.
- **Postura de Microsoft:** Microsoft Foundry ofrece evaluadores de calidad, seguridad y comportamiento de agentes —precisión y selección de herramientas, y en versión preliminar finalización y adherencia a la tarea— para medir antes de desplegar.
- **Capacidades Microsoft:** Evaluaciones de Microsoft Foundry (evaluadores de agentes); AI Red Teaming Agent
- **Cruce de marcos:** NIST — AI RMF MEASURE 2 · MANAGE 1.1 · AI 600-1 (Obscene, Degrading, and/or Abusive Content) | CIS — CIS 16 · guía CIS para LLM | The Open Group — TOGAF Fase G (cumplimiento de arquitectura) | ISACA — COBIT BAI07 · APO11 · AAISM D3 · AI Audit Toolkit | CSA — AICM MDS · A&A | MCSB — DS
- **Anclaje y COE:** Atlas — TRUST / Anticipar | TheNextCISO — CISO-MM (madurez) | SAF — Seguridad del desarrollo | COE — Riesgo, cumplimiento y aseguramiento | Responsable sugerido — Ingeniería de IA + COE de IA | Ola 1 (30–90 días)

#### B08.2 · ¿Cómo monitoreamos en producción la deriva de comportamiento, calidad y seguridad de los modelos y agentes, y cómo recogemos y procesamos los reportes de usuarios sobre fallas, sesgos o comportamientos indebidos?

- **Por qué importa:** El comportamiento de la IA cambia con los datos, los usuarios y las actualizaciones de modelos, y los usuarios ven fallas que ninguna prueba previa anticipó.
- **Buena práctica (evidencia esperada):** Monitoreo continuo con métricas y umbrales, trazas de ejecución y alertas; canal de reporte simple, con clasificación y respuesta en plazos; revisión periódica de tendencias integrada con la mejora de los sistemas.
- **Postura de Microsoft:** Microsoft Foundry incluye observabilidad basada en OpenTelemetry: las trazas de agentes están disponibles de forma general y la monitorización continua figura en versión preliminar en la documentación vigente. La responsabilidad es uno de los principios de IA responsable de Microsoft y requiere mecanismos de retroalimentación; sus productos incluyen retroalimentación de usuarios y administradores.
- **Capacidades Microsoft:** Observabilidad de Microsoft Foundry (trazas); Azure Monitor / Application Insights; retroalimentación en Microsoft 365 Copilot y Copilot Studio
- **Cruce de marcos:** NIST — AI RMF MEASURE 2.4 · MEASURE 3.3 · MANAGE 4.1 · GOVERN 5 · CSF DE.CM | CIS — CIS 8 | The Open Group — sin referencia directa | ISACA — COBIT MEA01 · DSS01 · DSS02 · APO11 · AAISM D3 | CSA — AICM LOG · MDS · SEF · MAESTRO L5 | MCSB — LT · IR · AI-6
- **Versión 2.0:** Integra la antigua B08.7 (fusión dentro del dominio).
- **Anclaje y COE:** Atlas — AI & AGENTS / Anticipar | TheNextCISO — CISO-MM (madurez) | SAF — Gestión de la postura de seguridad | COE — Operaciones, detección y respuesta | Responsable sugerido — Plataforma de IA + COE de IA | Ola 2 (90–180 días)

#### B08.3 · ¿Qué cambios (modelo, versión, instrucciones de sistema, herramientas, datos, permisos) obligan a repetir las pruebas y la aprobación?

- **Por qué importa:** Un cambio menor en las instrucciones o en el modelo subyacente puede alterar por completo el comportamiento.
- **Buena práctica (evidencia esperada):** Matriz de cambios con el nivel de revisión requerido, versionado de todos los componentes y una canalización que bloquea despliegues sin evidencia.
- **Postura de Microsoft:** Microsoft recomienda gestionar el ciclo de vida con entornos separados y canalizaciones, y planificar el retiro de modelos: en Foundry, los modelos con disponibilidad general duran 18 meses (12 para algunos proveedores), con aviso mínimo de 60 días y sin prórrogas.
- **Capacidades Microsoft:** Copilot Studio (canalizaciones); Microsoft Foundry (política de retiro de modelos)
- **Cruce de marcos:** NIST — AI RMF MANAGE 4.1 · GOVERN 1.5 | CIS — CIS 4 · CIS 16 | The Open Group — TOGAF Fase H | ISACA — COBIT BAI06 · BAI07 · AAISM D3 | CSA — AICM CCC | MCSB — DS
- **Anclaje y COE:** Atlas — TECHNOLOGY / Limitar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Seguridad del desarrollo | COE — Arquitectura y patrones seguros | Responsable sugerido — Ingeniería de IA | Ola 1 (30–90 días)

#### B08.4 · ¿Comprobamos de forma recurrente que los filtros y guardrails bloquean lo que deben y no bloquean lo legítimo?

- **Por qué importa:** Un control configurado no es un control efectivo; los atacantes buscan la brecha entre ambos.
- **Buena práctica (evidencia esperada):** Pruebas periódicas con casos conocidos y nuevos, métricas de efectividad y de falsos positivos, y registro de diseño, implementación y efectividad bajo estrés.
- **Postura de Microsoft:** Microsoft recomienda evaluar y probar de forma adversaria las aplicaciones de IA, incluidos sus filtros, con herramientas como PyRIT y el agente de red teaming de Foundry.
- **Capacidades Microsoft:** PyRIT; AI Red Teaming Agent (Microsoft Foundry); Azure AI Content Safety
- **Cruce de marcos:** NIST — AI RMF MEASURE 2.7 · MEASURE 2.13 | CIS — CIS 18 | The Open Group — sin referencia directa | ISACA — COBIT MEA02 · AAISM D3 · AI Audit Toolkit | CSA — AICM A&A · MDS | MCSB — DS · AI-2 · AI-7
- **Anclaje y COE:** Atlas — TRUST / Gobernar | TheNextCISO — CISO-MM (madurez) | SAF — Seguridad del desarrollo | COE — Riesgo, cumplimiento y aseguramiento | Responsable sugerido — AppSec + Seguridad ofensiva | Ola 2 (90–180 días)

#### B08.5 · ¿Qué evidencia de aseguramiento continuo tenemos sobre nuestros controles de IA y quién la revisa de forma independiente?

- **Por qué importa:** La confianza en la IA debe basarse en evidencia verificable, no en declaraciones.
- **Buena práctica (evidencia esperada):** Registro de evidencia por control (objetivo, prueba, resultado, limitaciones, fecha, dueño), revisión independiente y seguimiento de hallazgos.
- **Postura de Microsoft:** Compliance Manager ofrece evaluaciones para NIST AI RMF, ISO/IEC 42001, ISO/IEC 23894 y la Ley de IA de la UE, y Purview DSPM aporta evidencia sobre el uso y la protección de los datos en la IA.
- **Capacidades Microsoft:** Microsoft Purview Compliance Manager; Microsoft Purview DSPM
- **Cruce de marcos:** NIST — AI RMF MEASURE 1.3 · GOVERN 1.5 | CIS — sin referencia directa | The Open Group — sin referencia directa | ISACA — COBIT MEA02 · MEA04 · AI Audit Toolkit | CSA — AICM A&A · STAR for AI · MAESTRO L6 | MCSB — GS
- **Anclaje y COE:** Atlas — TRUST / Gobernar | TheNextCISO — CISO-MM (madurez) | SAF — Estrategia, integración y gobierno | COE — Riesgo, cumplimiento y aseguramiento | Responsable sugerido — Auditoría interna + GRC | Ola 2 (90–180 días)

#### B08.6 · ¿Vamos a implementar o certificar un sistema de gestión de IA (ISO/IEC 42001), y con qué alcance?

- **Por qué importa:** Un sistema de gestión ordena el ciclo de mejora; la certificación depende del alcance y de la auditoría, no es automática.
- **Buena práctica (evidencia esperada):** Decisión documentada sobre alcance y objetivo (implementar, certificar o solo alinear), análisis de brechas y plan.
- **Postura de Microsoft:** Microsoft certificó en ISO/IEC 42001 servicios de IA como Copilot Studio, Microsoft Foundry y Security Copilot, y comunicó en 2025 la certificación de Microsoft 365 Copilot (verificar alcance vigente en el Service Trust Portal); Compliance Manager ofrece una evaluación de ISO/IEC 42001.
- **Capacidades Microsoft:** Service Trust Portal; Microsoft Purview Compliance Manager
- **Cruce de marcos:** NIST — AI RMF (correspondencia con ISO/IEC 42001) | CIS — sin referencia directa | The Open Group — sin referencia directa | ISACA — COBIT APO01 · MEA03 · AAISM D1 | CSA — AICM (correspondencia con ISO/IEC 42001) · STAR for AI | MCSB — GS
- **Anclaje y COE:** Atlas — TRUST / Gobernar | TheNextCISO — CISO-NX (nueva generación) | SAF — Estrategia, integración y gobierno | COE — Riesgo, cumplimiento y aseguramiento | Responsable sugerido — GRC + Líder de IA | Ola 3 (180–365 días) | relevante para el directorio

#### B08.7 · ¿Qué controles de IA damos por eficaces sin garantías demostradas, y cómo compensamos ese límite con capas de defensa, monitoreo y pruebas continuas?

- **Por qué importa:** Muchas mitigaciones contra ataques a la IA son empíricas: se adoptan porque parecen funcionar, no porque ofrezcan garantías; tratarlas como infalibles crea una falsa sensación de seguridad que ningún directorio debería aceptar.
- **Buena práctica (evidencia esperada):** Inventario de controles de IA con su base de eficacia (garantía formal, evidencia empírica o supuesto); capas compensatorias independientes entre sí; red teaming y evaluaciones recurrentes; comunicación explícita del riesgo residual al directorio.
- **Postura de Microsoft:** Microsoft asume el mismo límite: su AI Red Team advierte que las mitigaciones no eliminan el riesgo por completo y que el red teaming es un proceso continuo. Frente a la inyección indirecta de instrucciones combina prevención (instrucciones de sistema reforzadas y spotlighting), detección (Prompt Shields) y mitigación del impacto (gobierno de datos, consentimiento del usuario y bloqueo determinístico de técnicas de exfiltración conocidas), con defensas probabilísticas y determinísticas.
- **Capacidades Microsoft:** Azure AI Content Safety (Prompt Shields; spotlighting); Defender for AI Services; AI Red Teaming Agent (Microsoft Foundry); PyRIT
- **Cruce de marcos:** NIST — AI RMF MEASURE 2.7 · MANAGE 1.3 · AI 100-2 · AI 600-1 (Information Security) | CIS — guía CIS para LLM · guía CIS para agentes de IA | The Open Group — sin referencia directa | ISACA — COBIT APO13 · MEA04 · AAISM D3 | CSA — AICM MDS · TVM · MAESTRO L5 | MCSB — AI-2 · AI-7
- **Versión 2.0:** Pregunta nueva (proceso inverso, pareja NI14). El contenido de la antigua B08.7 se integró en B08.2.
- **Anclaje y COE:** Atlas — AI & AGENTS / Limitar | TheNextCISO — CISO-NX (nueva generación) | SAF — Gestión de la postura de seguridad | COE — Riesgo, cumplimiento y aseguramiento | Responsable sugerido — CISO + responsable de IA | Ola 2 (90–180 días) | relevante para el directorio

#### B08.8 · ¿Qué indicadores de confianza en la IA presentamos al directorio (incidentes, bloqueos, desvíos, cobertura de pruebas, hallazgos abiertos)?

- **Por qué importa:** El directorio necesita saber si la IA está bajo control, no cuántos pilotos hay.
- **Buena práctica (evidencia esperada):** Pocos indicadores con tendencia y umbrales, narrativa de escenarios y decisiones solicitadas.
- **Postura de Microsoft:** SAF propone que, en el nivel más alto de madurez, el gobierno de la IA sea un habilitador medible del negocio, con impacto visible en la confianza, el riesgo y los resultados.
- **Capacidades Microsoft:** Microsoft Agent 365 (métricas); Microsoft Purview DSPM; Microsoft Defender XDR (alertas de IA)
- **Cruce de marcos:** NIST — AI RMF MEASURE 1 · GOVERN 2.3 | CIS — sin referencia directa | The Open Group — Open FAIR O-RA (comunicación cuantitativa) | ISACA — COBIT EDM05 · MEA01 · AAISM D1 | CSA — AICM GRC | MCSB — GS
- **Anclaje y COE:** Atlas — TRUST / Gobernar | TheNextCISO — CISO-MM (madurez) | SAF — Estrategia, integración y gobierno | COE — Valor, métricas y comunicación ejecutiva | Responsable sugerido — CISO + Líder de IA | Ola 2 (90–180 días) | relevante para el directorio | pregunta prioritaria para el directorio

#### B08.9 · ¿Cómo explicamos y justificamos una decisión apoyada por IA cuando un cliente, un empleado o un regulador lo pide?

- **Por qué importa:** Sin trazabilidad no es posible defender una decisión ni corregirla.
- **Buena práctica (evidencia esperada):** Registro de entradas, fuentes, versión del sistema y revisión humana para las decisiones relevantes; criterios de explicación por tipo de decisión.
- **Postura de Microsoft:** SAF pide asegurar que las decisiones de negocio apoyadas por IA queden registradas y sean defendibles en todas las jurisdicciones aplicables; la transparencia es uno de los principios de IA responsable de Microsoft.
- **Capacidades Microsoft:** Microsoft Purview Audit; notas de transparencia de Microsoft
- **Cruce de marcos:** NIST — AI RMF MEASURE 2.8 · MEASURE 2.9 | CIS — CIS 8 | The Open Group — sin referencia directa | ISACA — COBIT MEA03 · APO11 · AI Audit Toolkit (explicabilidad) | CSA — AICM GRC · LOG | MCSB — LT
- **Anclaje y COE:** Atlas — TRUST / Recuperar | TheNextCISO — CISO-NX (nueva generación) | SAF — Estrategia, integración y gobierno | COE — Riesgo, cumplimiento y aseguramiento | Responsable sugerido — Dueño del proceso + Legal | Ola 2 (90–180 días)

### B09 — Observabilidad, detección y respuesta a incidentes de IA

*Registrar, detectar, investigar y responder cuando la IA o un agente se comporta mal.*

#### B09.1 · ¿Registramos de forma correlacionable quién pidió qué, qué hizo el agente, con qué identidad, herramientas y datos, sin depender del razonamiento interno del modelo?

- **Por qué importa:** Sin registros correlacionados no hay detección, investigación ni rendición de cuentas.
- **Buena práctica (evidencia esperada):** Registro de interacciones, acciones, identidad, herramientas y datos con identificadores comunes, retención definida y acceso controlado.
- **Postura de Microsoft:** SAF exige que las actividades previstas y no deseadas estén definidas y sean detectables; Purview Audit registra las interacciones con IA con el identificador del agente y las detecciones de inyección y jailbreak, Defender XDR permite la búsqueda avanzada y Foundry ofrece trazas de los agentes.
- **Capacidades Microsoft:** Microsoft Purview Audit; Microsoft Defender XDR (búsqueda avanzada); Microsoft Agent 365 (observabilidad); trazas de Microsoft Foundry
- **Cruce de marcos:** NIST — CSF DE.CM · AI RMF MANAGE 4.1 · MEASURE 2.8 | CIS — CIS 8 (8.2, 8.9) · guía CIS para agentes de IA | The Open Group — sin referencia directa | ISACA — COBIT DSS05 · MEA01 · AAISM D3 | CSA — AICM LOG · MAESTRO L5 | MCSB — LT · AI-6
- **Anclaje y COE:** Atlas — AI & AGENTS / Anticipar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Operaciones de seguridad (SecOps/SOC) | COE — Operaciones, detección y respuesta | Responsable sugerido — Líder SOC + Plataforma de IA | Ola 0 (0–30 días)

#### B09.2 · ¿El SOC tiene detecciones específicas para la IA (inyección de instrucciones, jailbreak, exfiltración por agentes, uso anómalo de herramientas, abuso de credenciales de IA)?

- **Por qué importa:** Las detecciones clásicas no reconocen los patrones de ataque propios de la IA.
- **Buena práctica (evidencia esperada):** Casos de uso de detección para IA priorizados por riesgo, alertas integradas al flujo del SOC, pruebas y métricas de efectividad.
- **Postura de Microsoft:** Defender for AI Services envía a Defender XDR alertas de jailbreak, fuga de datos y robo de credenciales; la protección en tiempo real de agentes de Copilot Studio y las señales de riesgo de Defender y Purview en Agent 365 estaban en versión preliminar a la fecha de corte.
- **Capacidades Microsoft:** Defender for AI Services (Microsoft Defender for Cloud); Microsoft Defender XDR; Microsoft Sentinel
- **Cruce de marcos:** NIST — CSF DE.AE · DE.CM · AI RMF MEASURE 2.7 | CIS — CIS 13 | The Open Group — sin referencia directa | ISACA — COBIT DSS05 · AAISM D3 | CSA — AICM LOG · TVM | MCSB — LT · AI-6
- **Anclaje y COE:** Atlas — AI & AGENTS / Anticipar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Operaciones de seguridad (SecOps/SOC) | COE — Operaciones, detección y respuesta | Responsable sugerido — Ingeniería de detección | Ola 1 (30–90 días)

#### B09.3 · ¿Tenemos playbooks de respuesta para incidentes de IA (fuga por prompt, agente comprometido, acción indebida, contenido dañino, modelo o datos envenenados)?

- **Por qué importa:** Los incidentes de IA exigen decisiones nuevas: qué suspender, qué revertir y qué notificar.
- **Buena práctica (evidencia esperada):** Playbooks por tipo de incidente con roles, acciones de contención, criterios de escalamiento y ejercicios periódicos.
- **Postura de Microsoft:** La hoja de ruta de gobierno y seguridad de IA de SAF ubica los planes de respuesta a incidentes específicos de IA en el nivel de gobierno integrado.
- **Capacidades Microsoft:** Microsoft Defender XDR; Microsoft Security Copilot; Microsoft Sentinel (playbooks)
- **Cruce de marcos:** NIST — SP 800-61 Rev. 3 · AI RMF MANAGE 4.1 · MANAGE 2.3 · CSF RS.MA | CIS — CIS 17 · guía CIS para agentes de IA | The Open Group — sin referencia directa | ISACA — COBIT DSS02 · AAISM D3 | CSA — AICM SEF | MCSB — IR
- **Anclaje y COE:** Atlas — AI & AGENTS / Contener | TheNextCISO — CISO-DO (operación de dominios) | SAF — Operaciones de seguridad (SecOps/SOC) | COE — Operaciones, detección y respuesta | Responsable sugerido — Líder SOC + COE de IA | Ola 1 (30–90 días)

#### B09.4 · ¿Podemos reconstruir de forma forense una cadena de acciones de varios agentes y herramientas con evidencia válida?

- **Por qué importa:** Sin reconstrucción no es posible determinar el alcance, la causa ni la responsabilidad.
- **Buena práctica (evidencia esperada):** Registros íntegros y sincronizados en el tiempo, identificadores de correlación entre agentes, retención suficiente y ejercicios de reconstrucción.
- **Postura de Microsoft:** El lago de datos de Microsoft Sentinel (disponible de forma general desde septiembre de 2025) permite retener y correlacionar telemetría a largo plazo, y Purview Audit conserva las interacciones con IA para la investigación.
- **Capacidades Microsoft:** Microsoft Sentinel (lago de datos); Microsoft Purview Audit; Microsoft Defender XDR
- **Cruce de marcos:** NIST — CSF RS.AN · DE.CM | CIS — CIS 8 (8.10) | The Open Group — sin referencia directa | ISACA — COBIT DSS02 · MEA03 | CSA — AICM SEF · LOG | MCSB — LT · IR
- **Anclaje y COE:** Atlas — TECHNOLOGY / Recuperar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Operaciones de seguridad (SecOps/SOC) | COE — Operaciones, detección y respuesta | Responsable sugerido — Líder SOC + Forense | Ola 2 (90–180 días)

#### B09.5 · ¿Cómo equilibramos la observabilidad de prompts y respuestas con la privacidad de las personas y la minimización de datos?

- **Por qué importa:** Registrarlo todo puede crear un repositorio sensible y entrar en conflicto con obligaciones de privacidad.
- **Buena práctica (evidencia esperada):** Trazabilidad proporcional al riesgo, acceso restringido y auditado a los registros, seudonimización donde aplique y retención mínima necesaria.
- **Postura de Microsoft:** Microsoft Purview aplica seudonimización por defecto en sus soluciones de riesgo interno y control de acceso basado en roles para la revisión de interacciones.
- **Capacidades Microsoft:** Microsoft Purview Insider Risk Management; Communication Compliance; Microsoft Purview Audit (roles)
- **Cruce de marcos:** NIST — Privacy Framework 1.0 · AI RMF MEASURE 2.10 · CSF PR.DS | CIS — CIS 3 (3.14) | The Open Group — sin referencia directa | ISACA — COBIT APO14 · MEA03 | CSA — AICM DSP · LOG | MCSB — DP · LT
- **Anclaje y COE:** Atlas — TRUST / Limitar | TheNextCISO — CISO-OS (gobierno) | SAF — Seguridad de datos | COE — Riesgo, cumplimiento y aseguramiento | Responsable sugerido — DPO + CISO | Ola 1 (30–90 días)

#### B09.6 · ¿Integramos las señales de IA (datos, identidad, endpoint, nube, plataformas de agentes) en una vista unificada del SOC?

- **Por qué importa:** Las señales de IA aisladas en cada consola impiden ver ataques que cruzan dominios.
- **Buena práctica (evidencia esperada):** Señales de IA ingresadas al XDR o SIEM, correlación con identidad y datos, y tableros específicos.
- **Postura de Microsoft:** Microsoft reúne en el portal de Defender las señales de XDR, Sentinel, Purview, Entra y la protección de cargas de IA, con una gestión de exposición que incluye activos de IA.
- **Capacidades Microsoft:** Plataforma unificada de operaciones de seguridad; Microsoft Security Exposure Management
- **Cruce de marcos:** NIST — CSF DE.CM · DE.AE | CIS — CIS 8 (8.9) | The Open Group — sin referencia directa | ISACA — COBIT DSS05 | CSA — AICM LOG | MCSB — LT · AI-6
- **Anclaje y COE:** Atlas — TECHNOLOGY / Anticipar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Operaciones de seguridad (SecOps/SOC) | COE — Operaciones, detección y respuesta | Responsable sugerido — Líder SOC | Ola 1 (30–90 días)

#### B09.7 · ¿Qué umbral convierte un comportamiento anómalo de la IA en un incidente, quién lo declara y cuándo se notifica a reguladores o afectados?

- **Por qué importa:** Sin criterios, los incidentes de IA se tratan como fallas de calidad y no se escalan a tiempo.
- **Buena práctica (evidencia esperada):** Definición de incidente de IA, criterios de severidad, autoridad de declaración, obligaciones de notificación por jurisdicción y plantillas.
- **Postura de Microsoft:** Silencio parcial: Microsoft no publica una definición única de incidente de IA para clientes; su guía de respuesta a incidentes y su marco de IA responsable aplican de forma general.
- **Capacidades Microsoft:** Guía de respuesta a incidentes de Microsoft; Microsoft Responsible AI Standard
- **Cruce de marcos:** NIST — AI RMF MANAGE 4.3 · GOVERN 4.3 · CSF RS.MA · RS.CO | CIS — CIS 17 (17.4) | The Open Group — sin referencia directa | ISACA — COBIT DSS02 · MEA03 · AAISM D2 | CSA — AICM SEF | MCSB — IR
- **Anclaje y COE:** Atlas — TRUST / Gobernar | TheNextCISO — CISO-OS (gobierno) | SAF — Operaciones de seguridad (SecOps/SOC) | COE — Riesgo, cumplimiento y aseguramiento | Responsable sugerido — CISO + Legal | Ola 2 (90–180 días) | relevante para el directorio

#### B09.8 · ¿Aprendemos de los incidentes de IA propios y ajenos (bases públicas, avisos de proveedores, investigación) para ajustar los controles?

- **Por qué importa:** La experiencia acumulada en IA es escasa; aprender de otros acelera la madurez.
- **Buena práctica (evidencia esperada):** Revisión periódica de incidentes públicos y avisos, lecciones aplicadas a modelos de amenazas y controles, y participación en comunidades.
- **Postura de Microsoft:** Microsoft comparte públicamente las lecciones de su AI Red Team y de su programa de IA responsable, y sostiene que la seguridad de la IA exige aprendizaje continuo porque las capacidades cambian rápido.
- **Capacidades Microsoft:** Publicaciones del Microsoft AI Red Team; Responsible AI Transparency Report; Microsoft Security Response Center
- **Cruce de marcos:** NIST — AI RMF GOVERN 4.3 · MANAGE 4.2 · CSF ID.IM | CIS — sin referencia directa | The Open Group — TOGAF Fase H | ISACA — COBIT BAI08 · DSS03 | CSA — AICM SEF · TVM | MCSB — IR
- **Anclaje y COE:** Atlas — RISK / Recuperar | TheNextCISO — CISO-NX (nueva generación) | SAF — Operaciones de seguridad (SecOps/SOC) | COE — Operaciones, detección y respuesta | Responsable sugerido — COE de IA + Inteligencia | Ola 2 (90–180 días)

#### B09.9 · ¿Qué cobertura de detección y qué tiempos de respuesta tenemos hoy para los agentes en producción, y cuál es la meta?

- **Por qué importa:** Desplegar agentes más rápido de lo que se los puede vigilar acumula riesgo invisible.
- **Buena práctica (evidencia esperada):** Porcentaje de agentes con señales en el SOC, tiempos de detección y contención medidos, y metas trimestrales.
- **Postura de Microsoft:** Microsoft recomienda incorporar la IA a las operaciones de seguridad habituales (monitoreo, caza, gobierno y respuesta) y medir de forma continua.
- **Capacidades Microsoft:** Microsoft Defender XDR; Microsoft Agent 365; Microsoft Sentinel
- **Cruce de marcos:** NIST — AI RMF MEASURE 3.1 · CSF DE.CM · ID.IM | CIS — CIS 8 · CIS 17 | The Open Group — sin referencia directa | ISACA — COBIT MEA01 | CSA — AICM LOG | MCSB — LT · IR · AI-6
- **Anclaje y COE:** Atlas — TECHNOLOGY / Gobernar | TheNextCISO — CISO-MM (madurez) | SAF — Operaciones de seguridad (SecOps/SOC) | COE — Valor, métricas y comunicación ejecutiva | Responsable sugerido — Líder SOC | Ola 2 (90–180 días)

### B10 — Regulación, terceros y confianza

*Obligaciones, proveedores y la confianza de clientes, empleados y reguladores.*

#### B10.1 · ¿Qué leyes, regulaciones y guías de IA aplican en cada país donde operamos, y qué rol cumplimos en cada caso (proveedor, implementador, usuario)?

- **Por qué importa:** Las obligaciones dependen de la jurisdicción, del rol y del tipo de sistema; generalizarlas produce errores en ambos sentidos.
- **Buena práctica (evidencia esperada):** Registro de obligaciones de IA por país y sistema, con rol, fecha de vigencia y estado de cumplimiento, revisado cada trimestre con Legal.
- **Postura de Microsoft:** Microsoft publica su enfoque de cumplimiento regulatorio de la IA en el Trust Center y ofrece evaluaciones regulatorias de IA en Compliance Manager.
- **Capacidades Microsoft:** Microsoft Purview Compliance Manager; Microsoft Trust Center
- **Cruce de marcos:** NIST — AI RMF GOVERN 1.1 · CSF GV.OC | CIS — sin referencia directa | The Open Group — TOGAF Gestión de requisitos | ISACA — COBIT MEA03 · AAISM D1 | CSA — AICM GRC | MCSB — GS
- **Anclaje y COE:** Atlas — RISK / Gobernar | TheNextCISO — CISO-NX (nueva generación) | SAF — Estrategia, integración y gobierno | COE — Riesgo, cumplimiento y aseguramiento | Responsable sugerido — Legal + Compliance | Ola 1 (30–90 días) | relevante para el directorio | pregunta prioritaria para el directorio

#### B10.2 · ¿Evaluamos el impacto de los sistemas de IA sobre las personas y sus derechos antes de desplegarlos, y quién firma esa evaluación?

- **Por qué importa:** Algunos impactos (discriminación, exclusión, daño) no aparecen en un análisis de seguridad tradicional.
- **Buena práctica (evidencia esperada):** Evaluación de impacto para los sistemas relevantes, con participación interdisciplinaria, medidas de mitigación y aprobación de la autoridad correspondiente.
- **Postura de Microsoft:** Microsoft exige evaluaciones de impacto de IA responsable para sus sistemas y publica una plantilla y una guía para realizarlas.
- **Capacidades Microsoft:** Plantilla y guía de evaluación de impacto de IA responsable (Microsoft)
- **Cruce de marcos:** NIST — AI RMF MAP 5 · MAP 1.1 · AI 600-1 (Harmful Bias and Homogenization) | CIS — sin referencia directa | The Open Group — sin referencia directa | ISACA — COBIT EDM03 · APO12 · AAISM D2 | CSA — AICM GRC | MCSB — GS
- **Anclaje y COE:** Atlas — RISK / Anticipar | TheNextCISO — CISO-NX (nueva generación) | SAF — Estrategia, integración y gobierno | COE — Riesgo, cumplimiento y aseguramiento | Responsable sugerido — Comité de IA + DPO | Ola 1 (30–90 días)

#### B10.3 · ¿Cómo evaluamos a los proveedores de modelos, plataformas y agentes de IA (seguridad, privacidad, continuidad, transparencia, indemnización)?

- **Por qué importa:** La dependencia de los proveedores de IA es alta y sus prácticas son heterogéneas.
- **Buena práctica (evidencia esperada):** Cuestionario específico para IA, evidencia independiente, cláusulas sobre uso de datos e indemnización, y revisión periódica.
- **Postura de Microsoft:** SAF propone preguntar a cada proveedor con qué datos entrenó el modelo, qué indemnización ofrece, si recopila datos del cliente y si avisará de cambios de modelo; Microsoft ofrece el Customer Copyright Commitment, sujeto a condiciones, y notas de transparencia de sus servicios.
- **Capacidades Microsoft:** Customer Copyright Commitment (Microsoft); notas de transparencia; Service Trust Portal
- **Cruce de marcos:** NIST — AI RMF GOVERN 6.1 · MANAGE 3.1 · CSF GV.SC | CIS — CIS 15 (15.5) | The Open Group — sin referencia directa | ISACA — COBIT APO10 · AAISM D2 | CSA — AICM STA · AI-CAIQ · STAR for AI | MCSB — GS
- **Anclaje y COE:** Atlas — TRUST / Anticipar | TheNextCISO — CISO-OS (gobierno) | SAF — Estrategia, integración y gobierno | COE — Riesgo, cumplimiento y aseguramiento | Responsable sugerido — Compras + CISO + Legal | Ola 1 (30–90 días)

#### B10.4 · ¿Qué haríamos si un proveedor cambia, retira o degrada un modelo del que depende un proceso crítico, o cambia sus políticas de datos?

- **Por qué importa:** Los modelos tienen ciclos de vida cortos; un retiro o un cambio puede alterar resultados o detener procesos.
- **Buena práctica (evidencia esperada):** Inventario de dependencias por modelo, monitoreo de avisos de retiro, pruebas con modelos alternativos y plan de contingencia.
- **Postura de Microsoft:** SAF plantea preguntar qué ocurre si el proveedor cambia o retira el modelo, quiebra, cambia sus políticas o es comprometido; la política de Foundry fija 18 meses de vida para modelos con disponibilidad general, aviso mínimo de 60 días y fechas de retiro sin prórroga.
- **Capacidades Microsoft:** Microsoft Foundry (ciclo de vida y retiro de modelos); SAF
- **Cruce de marcos:** NIST — AI RMF GOVERN 6.2 · MANAGE 3.2 · CSF GV.SC | CIS — CIS 15 | The Open Group — sin referencia directa | ISACA — COBIT APO10 · DSS04 · AAISM D2 | CSA — AICM STA · BCR · IPY | MCSB — GS
- **Anclaje y COE:** Atlas — RISK / Recuperar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Estrategia, integración y gobierno | COE — Riesgo, cumplimiento y aseguramiento | Responsable sugerido — Líder de IA + Continuidad | Ola 2 (90–180 días)

#### B10.5 · ¿Cómo aplicamos el modelo de responsabilidad compartida de la IA (SaaS, PaaS, IaaS) para saber qué controles son nuestros?

- **Por qué importa:** En la IA, la responsabilidad del cliente sobre uso, datos, identidad y agentes persiste aunque el proveedor gestione el modelo.
- **Buena práctica (evidencia esperada):** Matriz de responsabilidades por sistema y modelo de servicio, con controles del cliente asignados y verificados.
- **Postura de Microsoft:** El modelo de responsabilidad compartida de IA de Microsoft distingue plataforma, aplicación y uso, y su versión para agentes agrega orquestación, herramientas y memoria: el cliente conserva siempre el uso, la formación, el gobierno de datos, la identidad y la aprobación humana de las acciones de alto impacto.
- **Capacidades Microsoft:** Modelo de responsabilidad compartida de IA; modelo de responsabilidad compartida para agentes de IA (Microsoft Learn)
- **Cruce de marcos:** NIST — AI RMF GOVERN 6 · CSF GV.SC · GV.RR | CIS — CIS 15 | The Open Group — G152 (requisitos y responsabilidades de seguridad) | ISACA — COBIT APO09 · APO10 | CSA — AICM STA (responsabilidad compartida; roles MP, OSP, AP, AIC y CSP) · DCS | MCSB — GS
- **Anclaje y COE:** Atlas — TRUST / Gobernar | TheNextCISO — CISO-OS (gobierno) | SAF — Arquitectura de seguridad de extremo a extremo | COE — Arquitectura y patrones seguros | Responsable sugerido — Arquitectura + CISO | Ola 0 (0–30 días)

#### B10.6 · ¿Somos transparentes con clientes y empleados sobre cuándo interactúan con IA o reciben contenido generado por IA?

- **Por qué importa:** La transparencia sostiene la confianza y es una obligación en varias jurisdicciones.
- **Buena práctica (evidencia esperada):** Política de divulgación, avisos en las interfaces, marcado del contenido sintético cuando aplique y verificación periódica.
- **Postura de Microsoft:** La transparencia es un principio de IA responsable de Microsoft, que publica notas de transparencia de sus servicios y agrega credenciales de contenido a las imágenes generadas por IA en varios productos.
- **Capacidades Microsoft:** Notas de transparencia; credenciales de contenido (C2PA) en productos de Microsoft
- **Cruce de marcos:** NIST — AI RMF MEASURE 2.8 · MAP 5 · AI 600-1 (Information Integrity) | CIS — sin referencia directa | The Open Group — sin referencia directa | ISACA — COBIT EDM05 · MEA03 | CSA — AICM GRC | MCSB — GS
- **Anclaje y COE:** Atlas — TRUST / Gobernar | TheNextCISO — CISO-NX (nueva generación) | SAF — Estrategia, integración y gobierno | COE — Gobierno, políticas y decisiones | Responsable sugerido — Comunicación + Legal + Líder de IA | Ola 2 (90–180 días)

#### B10.7 · ¿Cómo gestionamos los riesgos de propiedad intelectual y derechos de autor en los datos de entrenamiento y en el contenido generado?

- **Por qué importa:** El uso de material protegido puede generar reclamos y el contenido generado puede tener titularidad incierta.
- **Buena práctica (evidencia esperada):** Política sobre fuentes y sobre el uso del contenido generado, controles de detección de material protegido y revisión legal de los casos de alto impacto.
- **Postura de Microsoft:** El Customer Copyright Commitment de Microsoft defiende frente a reclamos de propiedad intelectual sobre contenido generado, con condiciones: en Copilot, usar los guardrails integrados; en Azure OpenAI, un metaprompt contra infracciones, pruebas documentadas y, según el caso, filtros de material protegido y de jailbreak.
- **Capacidades Microsoft:** Customer Copyright Commitment; Azure AI Content Safety (detección de material protegido)
- **Cruce de marcos:** NIST — AI RMF MAP 4.1 · GOVERN 6.1 · AI 600-1 (Intellectual Property) | CIS — sin referencia directa | The Open Group — sin referencia directa | ISACA — COBIT MEA03 · AAISM D2 | CSA — AICM GRC · DSP | MCSB — GS
- **Anclaje y COE:** Atlas — TRUST / Limitar | TheNextCISO — CISO-NX (nueva generación) | SAF — Estrategia, integración y gobierno | COE — Riesgo, cumplimiento y aseguramiento | Responsable sugerido — Legal | Ola 2 (90–180 días)

#### B10.8 · ¿Cómo demostramos a clientes, auditores y reguladores que nuestra IA es confiable (centro de confianza, atestaciones, certificaciones, informes)?

- **Por qué importa:** La confianza externa requiere evidencia accesible; las afirmaciones genéricas no alcanzan.
- **Buena práctica (evidencia esperada):** Centro de confianza con políticas, controles y evidencias de IA, atestaciones independientes donde aplique y respuestas preparadas para cuestionarios.
- **Postura de Microsoft:** Microsoft publica su Responsible AI Transparency Report (2026) y sus certificaciones y auditorías en el Service Trust Portal; según CSA, Microsoft estuvo entre las primeras organizaciones certificadas en STAR for AI Nivel 2 (noviembre de 2025).
- **Capacidades Microsoft:** Service Trust Portal; Responsible AI Transparency Report; CSA STAR for AI
- **Cruce de marcos:** NIST — AI RMF GOVERN 4.2 · MEASURE 2.8 | CIS — sin referencia directa | The Open Group — sin referencia directa | ISACA — COBIT EDM05 · MEA04 | CSA — STAR for AI · AICM A&A | MCSB — GS
- **Anclaje y COE:** Atlas — TRUST / Gobernar | TheNextCISO — CISO-NX (nueva generación) | SAF — Estrategia, integración y gobierno | COE — Valor, métricas y comunicación ejecutiva | Responsable sugerido — CISO + Comunicación | Ola 3 (180–365 días) | relevante para el directorio

#### B10.9 · ¿Cómo alineamos nuestro marco de IA con NIST AI RMF, ISO/IEC 42001, la AICM de CSA y COBIT sin multiplicar auditorías?

- **Por qué importa:** Cada marco aporta una perspectiva; gestionarlos por separado duplica el trabajo.
- **Buena práctica (evidencia esperada):** Catálogo único de controles de IA con correspondencias a cada marco, evidencia reutilizable y un responsable por control.
- **Postura de Microsoft:** Compliance Manager permite gestionar varias evaluaciones de IA sobre controles comunes; la AICM de CSA publica correspondencias con ISO/IEC 42001, la Ley de IA de la UE y NIST.
- **Capacidades Microsoft:** Microsoft Purview Compliance Manager
- **Cruce de marcos:** NIST — AI RMF · AI 600-1 · CSF (perfiles) | CIS — CIS AI Security Guidance Workbook | The Open Group — TOGAF Gestión de requisitos | ISACA — COBIT MEA02 · MEA03 · AAISM D1 | CSA — AICM v1.1 (correspondencias) · MAESTRO L6 | MCSB — GS
- **Anclaje y COE:** Atlas — TRUST / Gobernar | TheNextCISO — CISO-MM (madurez) | SAF — Estrategia, integración y gobierno | COE — Riesgo, cumplimiento y aseguramiento | Responsable sugerido — GRC | Ola 2 (90–180 días)

### B11 — IA para la seguridad: SOC agéntico y fuerza laboral digital

*Usar IA y agentes para defender, sin perder criterio humano ni control.*

#### B11.1 · ¿Qué tareas de seguridad automatizamos con IA (clasificación, investigación, caza, vulnerabilidades, políticas) y cuáles reservamos al juicio humano?

- **Por qué importa:** Delegar sin criterio erosiona la capacidad del equipo; no delegar desperdicia la ventaja defensiva de la IA.
- **Buena práctica (evidencia esperada):** Matriz de delegación por tarea con criterios de impacto, reversibilidad y confianza, revisada según los resultados.
- **Postura de Microsoft:** SAF recomienda usar la IA donde es fuerte y no como reemplazo ciego de las personas. Agentes de Security Copilot: clasificación de alertas de seguridad (disponible de forma general), clasificación de alertas de DLP (disponible de forma general), optimización de acceso condicional (disponible de forma general), informes de inteligencia de amenazas (disponible de forma general) y remediación de vulnerabilidades en Intune (versión preliminar).
- **Capacidades Microsoft:** Agentes de Microsoft Security Copilot
- **Cruce de marcos:** NIST — IR 8596 borrador (Defend) · AI RMF MAP 3.5 · CSF DE.AE | CIS — CIS 17 | The Open Group — sin referencia directa | ISACA — COBIT DSS02 · APO07 · AAISM D3 | CSA — AICM GRC | MCSB — LT · IR
- **Anclaje y COE:** Atlas — SELF / Limitar | TheNextCISO — CISO-NX (nueva generación) | SAF — Operaciones de seguridad (SecOps/SOC) | COE — Operaciones, detección y respuesta | Responsable sugerido — Líder SOC + CISO | Ola 1 (30–90 días)

#### B11.2 · ¿Con qué criterios promovemos un agente de seguridad de piloto a producción (errores críticos, falsos positivos, reversibilidad, auditoría)?

- **Por qué importa:** La precisión promedio no alcanza: un solo error crítico puede ser inaceptable.
- **Buena práctica (evidencia esperada):** Puertas de promoción con métricas de errores críticos, eficacia, impacto, falsos positivos, reversibilidad y auditabilidad, y un período supervisado antes de ampliar la autonomía.
- **Postura de Microsoft:** Los agentes de Security Copilot explican sus decisiones y aprenden de la retroalimentación de los administradores, lo que permite evaluar su desempeño antes de ampliar su autonomía.
- **Capacidades Microsoft:** Agentes de Microsoft Security Copilot
- **Cruce de marcos:** NIST — AI RMF MEASURE 2 · MANAGE 1.1 | CIS — sin referencia directa | The Open Group — TOGAF Fase G | ISACA — COBIT BAI07 · DSS02 · AAISM D3 | CSA — AICM A&A | MCSB — IR · AI-5
- **Anclaje y COE:** Atlas — ORGANIZATION / Gobernar | TheNextCISO — CISO-MM (madurez) | SAF — Operaciones de seguridad (SecOps/SOC) | COE — Operaciones, detección y respuesta | Responsable sugerido — Líder SOC | Ola 2 (90–180 días)

#### B11.3 · ¿Cómo gobernamos a los propios agentes de seguridad (identidad, permisos, aprobación de acciones, registro) para que no se conviertan en un nuevo vector de ataque?

- **Por qué importa:** Un agente de seguridad tiene acceso privilegiado a la telemetría y capacidad de acción: es un blanco valioso.
- **Buena práctica (evidencia esperada):** Identidad propia, mínimo privilegio, acciones sensibles con aprobación, registro completo y revisión periódica de permisos.
- **Postura de Microsoft:** Los principios que Microsoft recomienda para cualquier agente (identidad propia, mínimo privilegio, trazabilidad) aplican también a los agentes de seguridad; verificar el modelo de identidad y permisos de cada agente de Security Copilot.
- **Capacidades Microsoft:** Microsoft Security Copilot (roles y permisos de agentes); Microsoft Entra Agent ID
- **Cruce de marcos:** NIST — CSF PR.AA · AI RMF GOVERN 1.6 | CIS — CIS 5 · CIS 6 · guía CIS para agentes de IA | The Open Group — sin referencia directa | ISACA — COBIT DSS05 · AAISM D3 | CSA — AICM IAM | MCSB — PA · IM · AI-4
- **Anclaje y COE:** Atlas — AI & AGENTS / Limitar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Operaciones de seguridad (SecOps/SOC) | COE — Plataforma e ingeniería de controles | Responsable sugerido — Líder SOC + IAM | Ola 1 (30–90 días)

#### B11.4 · ¿Cómo medimos el impacto de la IA en el SOC (tiempo de clasificación, tiempo de respuesta, calidad de la investigación, carga del analista) frente a una línea base previa?

- **Por qué importa:** Sin línea base no se puede distinguir una mejora real de una percepción.
- **Buena práctica (evidencia esperada):** Línea base previa, métricas comparables, análisis de la calidad además de la velocidad y revisión trimestral.
- **Postura de Microsoft:** Microsoft publica estudios sobre el efecto de Security Copilot en tareas de seguridad y recomienda medir resultados operativos, no solo el uso.
- **Capacidades Microsoft:** Microsoft Security Copilot (panel de uso)
- **Cruce de marcos:** NIST — AI RMF MEASURE 1 · MEASURE 4 · CSF ID.IM | CIS — CIS 17 | The Open Group — sin referencia directa | ISACA — COBIT MEA01 · EDM02 | CSA — AICM GRC | MCSB — IR
- **Anclaje y COE:** Atlas — TRUST / Gobernar | TheNextCISO — CISO-MM (madurez) | SAF — Operaciones de seguridad (SecOps/SOC) | COE — Valor, métricas y comunicación ejecutiva | Responsable sugerido — Líder SOC | Ola 2 (90–180 días)

#### B11.5 · ¿Cómo evitamos que los analistas pierdan habilidades críticas o confíen ciegamente en las conclusiones de la IA?

- **Por qué importa:** El sesgo de automatización lleva a aceptar conclusiones erróneas que parecen seguras.
- **Buena práctica (evidencia esperada):** Revisión de muestras, ejercicios sin IA, exigencia de evidencia en cada conclusión y formación continua.
- **Postura de Microsoft:** SAF es explícito: nunca tercerizar en la IA el pensamiento crítico; automatizar por completo procesos como el modelado de amenazas socava el aprendizaje y el pensamiento crítico humano.
- **Capacidades Microsoft:** SAF
- **Cruce de marcos:** NIST — AI RMF GOVERN 3.2 · MAP 3.4 · AI 600-1 (Human-AI Configuration) | CIS — CIS 14 | The Open Group — sin referencia directa | ISACA — COBIT APO07 | CSA — AICM HRS | MCSB — AI-5
- **Anclaje y COE:** Atlas — SELF / Anticipar | TheNextCISO — CISO-MM (madurez) | SAF — Operaciones de seguridad (SecOps/SOC) | COE — Cultura, talento y adopción | Responsable sugerido — Líder SOC | Ola 2 (90–180 días)

#### B11.6 · ¿Usamos IA para gestionar la postura y la exposición (políticas de acceso, configuraciones, priorización de vulnerabilidades) con aprobación humana?

- **Por qué importa:** La postura se degrada más rápido de lo que un equipo puede revisar manualmente.
- **Buena práctica (evidencia esperada):** Agentes de postura con recomendaciones revisadas, cambios aplicados con aprobación y registro, y medición del efecto sobre la exposición.
- **Postura de Microsoft:** SAF propone usar la IA para el descubrimiento, la priorización y la mitigación de vulnerabilidades; el agente de optimización de acceso condicional (disponible de forma general) y el de remediación de vulnerabilidades de Intune (versión preliminar) operan con aprobación del administrador.
- **Capacidades Microsoft:** Agente de optimización de acceso condicional; agente de remediación de vulnerabilidades de Intune (versión preliminar); Microsoft Security Exposure Management
- **Cruce de marcos:** NIST — CSF PR.PS · ID.RA · IR 8596 borrador (Defend) | CIS — CIS 4 · CIS 7 | The Open Group — sin referencia directa | ISACA — COBIT DSS05 · BAI10 | CSA — AICM TVM | MCSB — PV · IM
- **Anclaje y COE:** Atlas — TECHNOLOGY / Limitar | TheNextCISO — CISO-DO (operación de dominios) | SAF — Gestión de la postura de seguridad | COE — Plataforma e ingeniería de controles | Responsable sugerido — Gestión de postura | Ola 1 (30–90 días)

#### B11.7 · ¿Cómo gestionamos el costo y la capacidad de la IA de seguridad (unidades de cómputo, licencias, consumo de datos) frente al valor obtenido?

- **Por qué importa:** El consumo de IA puede crecer más rápido que el presupuesto si no se gobierna.
- **Buena práctica (evidencia esperada):** Presupuesto y alertas de consumo, asignación por caso de uso, revisión de valor por costo y criterios de retiro.
- **Postura de Microsoft:** Security Copilot está incluido en Microsoft 365 E5 y E7: se aprovisiona sin pasos del cliente con 400 unidades de cómputo de seguridad (SCU) por mes por cada 1.000 licencias, hasta 10.000; el despliegue comenzó en noviembre de 2025 y la finalización de la puesta a disposición no está confirmada.
- **Capacidades Microsoft:** Microsoft Security Copilot (inclusión en Microsoft 365 E5/E7; unidades de cómputo de seguridad)
- **Cruce de marcos:** NIST — AI RMF MANAGE 2.1 · MANAGE 2.2 | CIS — sin referencia directa | The Open Group — sin referencia directa | ISACA — COBIT APO06 · EDM04 | CSA — AICM GRC | MCSB — GS
- **Anclaje y COE:** Atlas — RISK / Gobernar | TheNextCISO — CISO-MM (madurez) | SAF — Operaciones de seguridad (SecOps/SOC) | COE — Valor, métricas y comunicación ejecutiva | Responsable sugerido — CISO + Finanzas | Ola 2 (90–180 días)

#### B11.8 · ¿Qué roles del equipo de seguridad cambian con la IA agéntica y cuál es el plan de reconversión y de nuevas habilidades?

- **Por qué importa:** La IA cambia el trabajo diario del equipo; sin plan aparecen resistencia o dependencia.
- **Buena práctica (evidencia esperada):** Mapa de impacto por rol, plan de formación, roles nuevos (por ejemplo, ingeniería de agentes de seguridad) y comunicación transparente.
- **Postura de Microsoft:** SAF señala que los trabajos a realizar no cambian, pero el trabajo de seguridad sí: aumenta la carga por ataques de mayor volumen y calidad y por la protección de las aplicaciones de IA, y aumenta la eficiencia al automatizar tareas de cada rol.
- **Capacidades Microsoft:** SAF; Microsoft Learn
- **Cruce de marcos:** NIST — CSF GV.RR · PR.AT · AI RMF GOVERN 2.2 | CIS — CIS 14 | The Open Group — Roles de seguridad (borrador citado por SAF) | ISACA — COBIT APO07 · BAI05 | CSA — AICM HRS | MCSB — GS
- **Anclaje y COE:** Atlas — ORGANIZATION / Gobernar | TheNextCISO — CISO-NX (nueva generación) | SAF — Operaciones de seguridad (SecOps/SOC) | COE — Cultura, talento y adopción | Responsable sugerido — CISO + RR. HH. | Ola 2 (90–180 días)

#### B11.9 · ¿Cómo usamos la IA para anticipar y simular ataques (inteligencia de amenazas, ejercicios, red teaming asistido) sin crear capacidades ofensivas fuera de control?

- **Por qué importa:** Las herramientas de simulación potenciadas por IA también son poderosas para el abuso.
- **Buena práctica (evidencia esperada):** Uso de la IA en inteligencia y simulación con alcance autorizado, entornos controlados, registro y aprobación de cada ejercicio.
- **Postura de Microsoft:** SAF propone usar la IA para mejorar la investigación, la caza y la simulación; Microsoft ofrece un agente de informes de inteligencia de amenazas y herramientas abiertas de red teaming como PyRIT, que deben usarse dentro de un alcance autorizado.
- **Capacidades Microsoft:** Agente de informes de inteligencia de amenazas (Security Copilot); PyRIT; simulación de ataques
- **Cruce de marcos:** NIST — IR 8596 borrador (Defend) · CSF ID.RA · ID.IM | CIS — CIS 18 | The Open Group — sin referencia directa | ISACA — COBIT APO12 · MEA02 | CSA — AICM TVM · Agentic AI Red Teaming Guide (CSA) | MCSB — LT · IR
- **Anclaje y COE:** Atlas — RISK / Anticipar | TheNextCISO — CISO-NX (nueva generación) | SAF — Operaciones de seguridad (SecOps/SOC) | COE — Operaciones, detección y respuesta | Responsable sugerido — Inteligencia + Seguridad ofensiva | Ola 3 (180–365 días)

## 6. Las 24 preguntas para el directorio

Selección de doce preguntas por parte, para una sesión de supervisión de 60 a 90 minutos. Las demás preguntas marcadas como «relevante para el directorio» sirven para sesiones temáticas.

### Agenda integral del CISO

| ID | Pregunta | Responde |
|---|---|---|
| A01.3 | ¿Qué decisiones de riesgo puede tomar el CISO por sí mismo, cuáles corresponden al comité ejecutivo y cuáles al directorio? | CISO + CRO |
| A01.4 | ¿Con qué frecuencia, formato y métricas supervisa el directorio el riesgo cibernético, y qué decisiones concretas tomó en los últimos doce meses? | Directorio + CISO |
| A01.8 | ¿Cómo rinde cuentas la alta dirección por los objetivos de seguridad (metas, incentivos, evaluación de desempeño)? | CEO + RR. HH. |
| A02.1 | ¿Cuál es nuestro apetito y tolerancia de riesgo cibernético expresado en términos de negocio, y quién lo aprobó? | Directorio + CRO |
| A02.2 | ¿Cuáles son nuestras joyas de la corona (procesos, datos, sistemas e identidades) y qué escenarios de pérdida material las amenazan, según los adversarios relevantes para nuestro sector y país? | Dueños de negocio + CISO + inteligencia de amenazas |
| A02.6 | ¿Qué indicadores anticipan una pérdida material y cuáles se reportan al directorio? | CISO |
| A04.1 | ¿Qué porcentaje de usuarios, administradores y accesos externos usa autenticación multifactor resistente al phishing, y cuál es la fecha objetivo para el 100%? | IAM |
| A06.2 | ¿Cuánto tiempo permanecen expuestos nuestros activos críticos a vulnerabilidades explotables y cuál es nuestra meta? | CISO + Infraestructura |
| A07.5 | ¿Cómo evaluamos, contratamos y monitoreamos a los terceros críticos, incluidos los proveedores de nuestros proveedores? | Compras + CISO |
| A08.4 | ¿Tenemos un plan de respuesta a incidentes vigente y ensayado con la dirección, legal, comunicación y proveedores? | CISO |
| A09.2 | ¿Podemos recuperar identidad, datos y servicios críticos tras un ransomware destructivo, y cuándo lo probamos de punta a punta por última vez? | CIO + CISO |
| A09.5 | ¿Cómo se gestiona una crisis cibernética: comité, roles, decisiones difíciles (incluido el pago de rescates), comunicación y notificaciones? | CEO + CISO + Legal |

### IA, agentes y sistemas autónomos

| ID | Pregunta | Responde |
|---|---|---|
| B01.1 | ¿Qué resultados de negocio esperamos de la IA y de los agentes, y qué riesgos estamos dispuestos a asumir para lograrlos? | CEO + Líder de IA + CISO |
| B01.2 | ¿Cuál es nuestro apetito de riesgo específico para la IA, por caso de uso, nivel de autonomía y tipo de dato, y quién lo aprobó? | Directorio + CRO |
| B01.6 | ¿Qué usos de IA están prohibidos o requieren aprobación reforzada por su impacto en personas, derechos o seguridad física? | Comité de IA + Legal |
| B02.1 | ¿Tenemos un marco de IA responsable publicado, patrocinado por la dirección y aplicado antes de cada despliegue? | CEO + Líder de IA |
| B02.2 | ¿Existe un consejo interdisciplinario de IA (negocio, seguridad, riesgo, legal, privacidad, datos) con mandato, umbrales de decisión y registro? | Sponsor ejecutivo |
| B03.1 | ¿Tenemos un inventario único de modelos, aplicaciones, copilotos, agentes, servidores MCP y conectores de IA, con dueño y criticidad? | COE de IA + CISO |
| B05.1 | ¿Corregimos la sobreexposición de datos (permisos excesivos, sitios abiertos, enlaces compartidos) antes de habilitar copilotos y agentes que la amplifican? | Data Officer + CISO |
| B07.1 | ¿Qué nivel de autonomía permitimos a cada agente (sugerir, ejecutar con aprobación, ejecutar y notificar, ejecutar sin supervisión) y con qué criterio se asigna? | Comité de IA + Dueño del agente |
| B07.2 | ¿Tenemos un perfil de radio de impacto por agente (datos, herramientas, transacciones, acciones irreversibles) y una estimación de la pérdida máxima creíble por escenario? | Arquitectura + CRO |
| B07.5 | ¿Podemos suspender, aislar o revocar un agente, o todos los de una clase, en minutos, y lo hemos ensayado? | Líder SOC + COE de IA |
| B08.8 | ¿Qué indicadores de confianza en la IA presentamos al directorio (incidentes, bloqueos, desvíos, cobertura de pruebas, hallazgos abiertos)? | CISO + Líder de IA |
| B10.1 | ¿Qué leyes, regulaciones y guías de IA aplican en cada país donde operamos, y qué rol cumplimos en cada caso (proveedor, implementador, usuario)? | Legal + Compliance |

## 7. Del cuestionario al centro de excelencia (COE)

### 7.1 Por qué un COE conjunto de seguridad e IA

SAF recomienda iniciar un marco de IA responsable y un centro de excelencia, y construir un kit de inicio que permita a los equipos adoptar IA de forma rápida y segura; el Cloud Adoption Framework de Microsoft también propone un centro de excelencia de IA. Este marco sostiene que el COE debe ser **conjunto**: la seguridad de la IA depende de los mismos fundamentos que la seguridad general (identidad, datos, plataforma, operaciones), y separar ambos COE duplica el gobierno y deja vacíos entre ellos. Las preguntas de las dos partes comparten responsables, artefactos y evidencia.

### 7.2 Misión, alcance y principios

- **Misión:** habilitar la adopción rápida, segura y responsable de la IA y los agentes, y elevar de forma continua la postura de seguridad, con decisiones trazables y evidencia verificable.
- **Alcance:** seguridad para la IA, IA para la seguridad, defensa frente a adversarios que usan IA y fundamentos del programa de seguridad.
- **Principios:** evidencia antes que declaraciones; supervisión proporcional al riesgo; el camino seguro debe ser más rápido que el atajo; un dueño por decisión; evidencia reutilizable; nunca promediar para ocultar un cero; revisión trimestral.

### 7.3 Siete funciones del COE

| Función | Propósito | Entregables | Lidera | Preguntas A | Preguntas B |
|---|---|---|---|---|---|
| Gobierno, políticas y decisiones | Definir derechos de decisión, políticas, el consejo de IA y seguridad, y el flujo de excepciones. | Carta del COE; matriz de derechos de decisión; política de uso aceptable de IA; registro de decisiones (CDRR); registro de excepciones. | CISO + Líder de IA | 11 | 16 |
| Riesgo, cumplimiento y aseguramiento | Expresar el apetito, cuantificar escenarios, mapear obligaciones y sostener la evidencia. | Declaración de apetito (incluida la IA); registro de riesgos; mapa de obligaciones por país; registro de evidencia y aseguramiento; catálogo de controles comunes. | CRO / GRC | 22 | 21 |
| Arquitectura y patrones seguros | Definir la arquitectura de referencia, los patrones aprobados y los modelos de amenazas. | Arquitectura de referencia; catálogo de patrones y zonas de aterrizaje; modelos de amenazas (STRIDER-TIM, MAESTRO); perfiles de radio de impacto (ABRP). | Arquitecto de seguridad | 11 | 15 |
| Plataforma e ingeniería de controles | Implementar y medir los controles de identidad, datos, endpoint, nube y agentes. | Líneas base; inventarios de activos, agentes y servidores MCP; políticas técnicas; indicadores de cobertura. | Ingeniería de seguridad / IAM | 27 | 21 |
| Operaciones, detección y respuesta | Detectar, contener, investigar y recuperar, incluidos los incidentes de IA. | Playbooks (incluidos los de IA); presupuesto de tiempo de contención (CTB); métricas de detección y contención; ejercicios. | Líder SOC | 10 | 15 |
| Cultura, talento y adopción | Formar, desarrollar talento y sostener a las personas que operan el programa. | Programa por audiencia; plan de talento y reconversión; red de referentes; indicadores de conducta. | CISO + RR. HH. | 10 | 4 |
| Valor, métricas y comunicación ejecutiva | Medir valor y riesgo, y comunicar en lenguaje de negocio a la dirección y al directorio. | Tablero de indicadores de riesgo; informe trimestral; caso de valor; preguntas para el directorio. | CISO | 8 | 7 |

### 7.4 Foros, cadencias y responsabilidades

| Foro | Integrantes | Cadencia |
|---|---|---|
| Patrocinador ejecutivo | CEO o un miembro del comité ejecutivo con autoridad sobre negocio y tecnología. | Trimestral |
| Consejo de IA y seguridad | CISO, líder de IA (CAIO o CDO), CRO, CIO/CTO, Legal, Privacidad (DPO), Data Officer, representantes de negocio; Auditoría interna como observador. | Mensual |
| Núcleo del COE | Líderes de las siete funciones. | Semanal |
| Red de referentes | Referentes de seguridad e IA en las unidades de negocio y en los equipos de producto. | Quincenal |
| Directorio o comité de auditoría | Supervisión del riesgo, decisiones de alta consecuencia y apetito. | Trimestral o semestral |

**RACI mínimo (AI CISO Atlas)**

| Rol | Responsabilidad |
|---|---|
| Dueño de negocio | Define el resultado esperado y las tolerancias operativas. |
| Autoridad de riesgo | Decide la aceptación de riesgo residual dentro de sus facultades delegadas. |
| CISO / Seguridad | Asesora sobre exposición, controles, respuesta y evidencia; lidera la respuesta a incidentes. |
| Dueño del caso de uso de IA o producto | Responde por el caso de uso, su ciclo de vida y su operación. |
| Plataforma e Ingeniería | Implementa y prueba los límites técnicos. |
| Legal, Privacidad y Cumplimiento | Determina las obligaciones y condiciones aplicables. |
| Auditoría interna | Evalúa de forma independiente cuando corresponde. |

### 7.5 Artefactos mínimos del COE

| Artefacto | Origen | Contenido |
|---|---|---|
| CISO Decision & Resilience Record (CDRR) | AI CISO Atlas | Registro auditable de cada decisión de riesgo: supuestos, impacto, controles, riesgo residual, autoridad de aceptación, vigencia y disparadores. |
| Agent Blast-Radius Profile (ABRP) | AI CISO Atlas | Perfil de autoridad de cada agente: identidad, dueño, herramientas, datos, operaciones de escritura, acciones irreversibles, revocación y pruebas. |
| Containment Time Budget (CTB) | AI CISO Atlas | Tiempo de detectar, clasificar, decidir, contener y verificar, comparado con el umbral de daño material del escenario. |
| Risk & Resilience Contract (RRC) | AI CISO Atlas | Acuerdo operativo sobre funciones críticas, tolerancias, condiciones de autonomía, pruebas de continuidad y escalamiento. |
| Registro de evidencia y aseguramiento | AI CISO Atlas | Control, objetivo, prueba, resultado, limitaciones, fecha, evidencia, dueño y próxima prueba; distingue diseño, implementación y efectividad. |
| Diario de decisiones | AI CISO Atlas | Hipótesis, opciones descartadas, disenso, decisión, resultado y revisión. |
| Mapa del patrimonio de IA y agentes | Este marco | Modelos, aplicaciones, copilotos, agentes, servidores MCP y conectores, con dueño, nivel de riesgo y datos accesibles. |
| Modelo de amenazas por sistema de IA | SAF / CSA | Cuatro preguntas del Threat Modeling Manifesto, categorías STRIDER-TIM de SAF y capas de MAESTRO. |
| Catálogo de controles comunes | Este marco | Controles con su correspondencia a NIST, CIS, The Open Group, ISACA, CSA y MCSB, para recolectar evidencia una sola vez. |
| Registro de excepciones | Este marco | Excepción, autoridad, controles compensatorios, vencimiento y estado de cierre. |

Los artefactos CDRR, ABRP, CTB y RRC son propuestas del AI CISO Atlas (nivel C: no validadas formalmente); conviene ensayarlos con casos autorizados antes de institucionalizarlos.

### 7.6 Plan por olas

| Ola | Preguntas | Foco | Criterio de salida |
|---|---|---|---|
| Ola 0 (0–30 días) | 45 | Constituir el COE y el consejo; responder las preguntas fundacionales: mandato, apetito (incluida la IA), joyas de la corona, inventario inicial de IA y agentes, política de uso aceptable, MFA resistente al phishing para administradores, sobreexposición de datos y plan de respuesta. | Carta del COE aprobada; dueño asignado a cada pregunta; línea base de evidencia de la ola 0. |
| Ola 1 (30–90 días) | 83 | Ciclo de vida e identidad de agentes, DLP para IA, detección de IA en el SOC, playbooks de incidentes de IA, catálogo de controles comunes y primeras métricas de exposición. | Registro de agentes con dueño e identidad; primeras evidencias de nivel 3; informe trimestral al comité ejecutivo. |
| Ola 2 (90–180 días) | 66 | Cuantificación de escenarios, red teaming de IA, aseguramiento continuo, métricas de valor, reversibilidad y presupuesto de tiempo de contención. | Indicadores de riesgo con tendencia; escenarios cuantificados; ejercicios de contención de agentes medidos. |
| Ola 3 (180–365 días) | 4 | Decisiones estructurales (sistema de gestión de IA, centro de confianza externo, desarrollo del criterio del CISO) y reevaluación completa de las 198 preguntas. | Perfil objetivo revisado; informe anual al directorio; plan del año siguiente. |

La ola indica cuándo el COE aborda la pregunta (evaluar, decidir y planificar), no cuándo debe estar resuelta la brecha.

### 7.7 Cómo se mide el COE

- Porcentaje de preguntas con dueño asignado y fecha de revisión.
- Porcentaje de preguntas con evidencia de nivel 3 o superior, por dominio (sin promediar).
- Cantidad de ceros en preguntas de contención y recuperación.
- Tiempo medio desde que se identifica una decisión hasta que se registra en el CDRR.
- Porcentaje de agentes inventariados con identidad propia, dueño, política y monitoreo.
- Excepciones vencidas y aceptaciones de riesgo sin revisión.
- Incidentes de IA, tiempo de contención y comparación con el presupuesto (CTB).
- Casos de negocio habilitados por el camino seguro del COE (patrones y kits de inicio).

## 8. Cruce de marcos: cobertura y hallazgos

### 8.1 Cobertura por catálogo

| Catálogo | Cobertura | Observación |
|---|---|---|
| NIST CSF 2.0 (categorías) | 22/22 | Ancla principal de la Parte A; la función Govern concentra el mayor número de preguntas. |
| NIST AI RMF 1.0 (categorías) | 19/19 | Ancla principal de la Parte B. |
| NIST AI 600-1 (riesgos de IA generativa) | 12/12 | Referenciados en las preguntas donde el riesgo aplica de forma directa. |
| CIS Controls v8.1 | 18/18 | Las guías complementarias de CIS para LLM, agentes y MCP aparecen en 33 preguntas de la Parte B. |
| COBIT 2019 (objetivos) | 40/40 | Revisar el cruce tras el lanzamiento de COBIT 7. |
| CSA CCM v4.1 (dominios, Parte A) | 17/17 | Nivel de dominio; los identificadores de control cambiaron entre versiones. |
| CSA AICM v1.1 (dominios, Parte B) | 18/18 | Incluye el dominio MDS (seguridad de modelos). |
| CSA MAESTRO (capas) | 7/7 | Útil para el modelado de amenazas de sistemas agénticos. |
| Microsoft Cloud Security Benchmark | 19/19 | 12 dominios de v1 y 7 controles de IA de v2 (versión preliminar). |
| The Open Group | 82/198 preguntas | Parte A: 51; Parte B: 31. Cobertura concentrada en gobierno, arquitectura, riesgo y Zero Trust. |

### 8.2 Hallazgos del cruce

- **NIST es la columna vertebral.** CSF 2.0 ordena la agenda general y el AI RMF la de IA. El borrador del Cyber AI Profile (IR 8596) organiza la seguridad de la IA sobre CSF 2.0 en tres áreas —Secure, Defend y Thwart— que coinciden con los tres frentes de este marco, y el proyecto COSIS desarrollará superposiciones de SP 800-53 para agentes únicos y multiagente.
- **CIS aporta la priorización operativa.** Los grupos de implementación IG1–IG3 y, desde abril de 2026, las guías complementarias para LLM, agentes y MCP son el puente más directo entre las preguntas de IA y controles verificables.
- **The Open Group aporta el «cómo» arquitectónico.** TOGAF y la guía G152 permiten insertar las decisiones del COE en el ciclo de arquitectura; Open FAIR permite cuantificar; los Zero Trust Commandments aportan principios. No tiene estándar de IA publicado: la falta de correspondencia en las preguntas de IA operativa es un hallazgo, no una omisión.
- **ISACA aporta el lenguaje de gobierno y aseguramiento.** Las preguntas cubren los 40 objetivos de COBIT 2019; para IA se usan los dominios de AAISM y el AI Audit Toolkit. COBIT 7 se lanza el 19 de noviembre de 2026 y el cruce deberá revisarse.
- **CSA aporta el catálogo de controles más granular.** CCM v4.1 para la nube, AICM v1.1 para la IA (18 dominios, incluido MDS, seguridad de modelos), MAESTRO para modelar amenazas agénticas y STAR for AI para el aseguramiento externo.
- **Microsoft Cloud Security Benchmark funciona como puente técnico.** La versión 1 se correlaciona con CIS Controls v8 y NIST SP 800-53; la versión 2 (preliminar) agrega siete controles de IA: modelos aprobados, filtrado de contenido en capas, metaprompts de seguridad, mínimo privilegio para funciones de agentes, intervención humana, monitoreo y detección, y red teaming continuo. Compliance Manager ofrece plantillas para NIST CSF 2.0, NIST AI RMF, ISO/IEC 42001, ISO/IEC 23894, la Ley de IA de la UE, CIS y CSA CCM, pero no para COBIT 2019.
- **Ninguna familia cubre sola las 198 preguntas.** El valor está en el catálogo de controles comunes del COE, que recolecta la evidencia una vez y la mapea a todos los marcos que la organización debe demostrar.

### 8.3 Referencias más frecuentes por dominio

| Dominio | Nombre | NIST | CIS | The Open Group | COBIT 2019 | CSA |
|---|---|---|---|---|---|---|
| A01 | Mandato, gobierno y directorio | GV.RM, GV.RR, GV.OV, GV.OC | CIS 15, CIS 16 | Open FAIR, O-ESA | EDM01, APO01, APO06, EDM04 | GRC, HRS, STA |
| A02 | Riesgo, apetito, cuantificación y valor | GV.RM, ID.RA, GV.OV, ID.IM | CIS 3, CIS 1, CIS 7 | Open FAIR, TOGAF Fase B | APO12, EDM03, MEA01, BAI09 | GRC, DSP, TVM |
| A03 | Arquitectura, estrategia técnica y Zero Trust | PR.IR, PR.PS, PR.AA, GV.PO | CIS 12, CIS 13, CIS 6 | Zero Trust Commandments, TOGAF Fases E–F | APO03, BAI03, DSS05, APO02 | IVS, AIS, IAM |
| A04 | Identidad y acceso privilegiado | PR.AA, PR.PS, ID.AM, RS.MI | CIS 6, CIS 5, CIS 17 | Zero Trust Commandments | DSS05, APO07, DSS06, BAI09 | IAM, HRS, SEF |
| A05 | Datos, privacidad y criptografía | PR.DS, ID.AM, DE.CM, PR.AA | CIS 3, CIS 14 | TOGAF Fase C, TOGAF Fases E–F | APO14, DSS05, BAI09, MEA03 | DSP, CEK, HRS |
| A06 | Exposición: activos, configuración y vulnerabilidades | PR.PS, ID.RA, DE.CM, ID.IM | CIS 7, CIS 2, CIS 4 | Open FAIR, TOGAF Fase D | DSS05, APO12, BAI10, BAI09 | TVM, UEM, IVS |
| A07 | Nube, aplicaciones, terceros y cadena de suministro | GV.SC, PR.PS, DE.CM, GV.RR | CIS 15, CIS 16, CIS 2 | G152, TOGAF Fase G | APO10, APO09, DSS05, BAI03 | STA, AIS, IPY |
| A08 | Operaciones de seguridad: detección, respuesta y caza | DE.AE, ID.IM, DE.CM, RS.MI | CIS 17, CIS 8, CIS 13 | Roles de seguridad | DSS05, DSS02, DSS01, APO07 | SEF, LOG, HRS |
| A09 | Resiliencia, continuidad, recuperación y crisis | RC.RP, PR.IR, GV.OC, ID.IM | CIS 11, CIS 17, CIS 5 | TOGAF Fase B, TOGAF Fase H | DSS04, BAI04, DSS05, EDM03 | BCR, SEF, CEK |
| A10 | Cumplimiento, regulación y aseguramiento continuo | GV.OV, ID.IM, GV.SC, GV.PO | CIS 8, CIS 15 | TOGAF Gestión de requisitos, Open FAIR | MEA04, MEA03, MEA02, APO12 | A&A, GRC, STA |
| A11 | Personas, cultura, talento y sostenibilidad del rol | GV.RR, PR.AT, PR.AA, ID.IM | CIS 14, CIS 6, CIS 16 | Roles de seguridad, Open FAIR | APO07, EDM01, BAI05, APO08 | HRS, IAM, AIS |
| B01 | Estrategia, valor y apetito de riesgo de la IA | GOVERN 1, MAP 1, MAP 3, GOVERN 6 | CIS 15, CIS 2 | G268, TOGAF Fase A | APO04, APO02, EDM02, EDM03 | GRC, STA |
| B02 | Gobierno, roles, políticas y centro de excelencia de IA | GOVERN 2, GOVERN 1, MAP 1, MANAGE 4 | CIS 14, CIS 2, CIS 16 | TOGAF Gobierno de arquitectura, Roles de seguridad | APO01, EDM01, APO13, APO14 | GRC, HRS, CCC |
| B03 | Inventario, descubrimiento e IA no autorizada | GOVERN 1, GOVERN 6, MAP 4, MANAGE 1 | CIS 2, CIS 1, CIS 13 | TOGAF Continuum empresarial | BAI09, DSS05, BAI10, APO12 | DSP, MDS, GRC |
| B04 | Identidad, autoridad y delegación de agentes | GOVERN 3, GOVERN 1, MANAGE 1, MAP 3 | CIS 6, CIS 5, CIS 3 | Zero Trust Commandments, TOGAF Fase G | DSS05, DSS06, BAI06 | IAM, CEK, CCC |
| B05 | Datos para la IA: exposición, protección y ciclo de vida | MEASURE 2, MAP 4, GOVERN 6, MANAGE 1 | CIS 3, CIS 8, CIS 13 | TOGAF Fase C | APO14, DSS05, BAI03, MEA03 | DSP, SEF, LOG |
| B06 | Amenazas a modelos, aplicaciones y agentes | MEASURE 2, MAP 4, MANAGE 1, MAP 3 | CIS 16, CIS 2, CIS 18 | Open FAIR, Security Principles for Architecture | BAI03, DSS05, APO12, APO10 | MDS, AIS, STA |
| B07 | Autonomía, supervisión humana y contención | MAP 3, MANAGE 2, GOVERN 3, MANAGE 1 | CIS 6, CIS 17, CIS 14 | Open FAIR, Security Principles for Architecture | DSS06, DSS02, APO01, APO12 | GRC, IAM, SEF |
| B08 | Evaluación, pruebas y aseguramiento continuo de la IA | MEASURE 2, MANAGE 1, MANAGE 4, GOVERN 1 | CIS 16, CIS 8, CIS 4 | TOGAF Fase G, TOGAF Fase H | APO11, BAI07, MEA01, MEA02 | MDS, A&A, LOG |
| B09 | Observabilidad, detección y respuesta a incidentes de IA | MANAGE 4, MEASURE 2, GOVERN 4, MANAGE 2 | CIS 8, CIS 17, CIS 13 | TOGAF Fase H | DSS05, DSS02, MEA03, MEA01 | LOG, SEF, TVM |
| B10 | Regulación, terceros y confianza | GOVERN 6, MAP 5, MANAGE 3, MEASURE 2 | CIS 15 | TOGAF Gestión de requisitos, G152 | MEA03, APO10, EDM05, EDM03 | GRC, STA, BCR |
| B11 | IA para la seguridad: SOC agéntico y fuerza laboral digital | MAP 3, MEASURE 2, MANAGE 1, GOVERN 1 | CIS 17, CIS 14, CIS 5 | TOGAF Fase G, Roles de seguridad | APO07, DSS02, DSS05, BAI07 | GRC, HRS, TVM |

## 9. Silencios, límites y vigencia

Siguiendo el criterio de declarar los silencios como hallazgo, se listan las afirmaciones que no pudieron confirmarse en fuentes oficiales al 6 de noviembre de 2026 y los límites del método.

### 9.1 Silencios de la postura de Microsoft

- **A01.9** — Silencio: Microsoft no publica una postura sobre cómo evaluar recortes de dotación o de presupuesto de seguridad. Lo más cercano son dos prácticas: en SFI vinculó la compensación de su liderazgo sénior al desempeño en seguridad, y Security Exposure Management mide la exposición con puntajes por iniciativa y genera eventos cuando un puntaje cae, lo que permite comparar la postura antes y después de una reducción.
- **A02.8** — Silencio parcial: Microsoft no publica un método para ponderar el daño a terceros en el análisis de riesgo cibernético. Para la IA sí lo exige: su Responsible AI Standard v2 pide evaluar el impacto de cada sistema en personas, organizaciones y la sociedad antes de desarrollarlo, identificando partes interesadas y daños potenciales, y revisar esa evaluación al menos una vez al año.
- **A02.9** — Silencio: Microsoft no publica una postura sobre la precisión necesaria en la cuantificación del riesgo. SAF recomienda estimar la pérdida con Open FAIR o un método similar (A02.3), y Security Exposure Management aporta puntajes por iniciativa con metas configurables: insumos medibles, no una cuantificación financiera.
- **A10.4** — Silencio: Microsoft no publica un modelo propio de líneas de aseguramiento para clientes; su evidencia de cumplimiento (Service Trust Portal) alimenta la revisión de terceros.
- **A10.7** — Silencio: Microsoft no publica un modelo de cuantificación financiera del riesgo cibernético ni criterios para validarlo; sus métricas de postura y exposición pueden alimentar un modelo, pero no lo reemplazan ni lo validan.
- **A11.4** — Silencio parcial: Microsoft no publica una guía específica sobre la sostenibilidad del rol del CISO ni sobre el desarrollo de su criterio; SAF asigna al gerente del SOC el bienestar y la carrera del equipo, promueve la automatización de tareas repetitivas y advierte no delegar el pensamiento crítico en la IA.
- **A11.9** — Silencio: Microsoft no publica criterios para evaluar el liderazgo del CISO desde la perspectiva de su equipo. El antecedente más cercano es SFI, que incorporó la seguridad a la evaluación de desempeño de todos los empleados y a la compensación del liderazgo sénior.
- **B07.7** — Silencio parcial: Microsoft no publica una guía específica de reversibilidad para agentes; sus capacidades de versiones, papelera y copias de seguridad apoyan la recuperación de los datos afectados.
- **B09.7** — Silencio parcial: Microsoft no publica una definición única de incidente de IA para clientes; su guía de respuesta a incidentes y su marco de IA responsable aplican de forma general.
- **A02.5** — Silencio parcial: Microsoft no publica una postura sobre seguros cibernéticos (contenido de la antigua A02.9, absorbida en la v2).
- **A10.6** — Silencio: la lista publicada de plantillas de Compliance Manager (última actualización, 6 de marzo de 2025) incluye COBIT 5, retirado por ISACA el 26 de octubre de 2026, y no incluye COBIT 2019 ni COBIT 7.
- Acceso condicional para agentes: no hay una declaración explícita de disponibilidad general de la función base.
- ID Protection para agentes: la documentación oficial es contradictoria (versión preliminar frente a disponibilidad general inminente).
- Revisiones de acceso específicas para identidades de agentes: no confirmadas.
- Inclusión de Security Copilot en Microsoft 365 E5/E7: no está confirmado que el despliegue por fases haya terminado.
- Agente de clasificación de alertas de riesgo interno y Microsoft Security Store: disponibilidad general no confirmada en fuentes oficiales.
- Protección en tiempo real de agentes de Copilot Studio: la disponibilidad general prevista para junio de 2026 no se refleja en la documentación vigente.
- Passkeys sincronizadas: versión preliminar pública; sin fecha oficial de disponibilidad general.
- Baseline Security Mode: disponible en todas las suscripciones, pero sin fecha oficial de disponibilidad general.
- Seguridad fuera del kernel en Windows: sin disponibilidad pública confirmada.
- Objetivo poscuántico: el anuncio de junio de 2026 fija 2029 para productos y servicios críticos, mientras una página de preguntas frecuentes de passkeys aún cita 2033.
- Cambios de nombre sin anuncio formal fechado: Microsoft 365 Copilot como «Microsoft Copilot», Copilot Control System como «Copilot controls» y DSPM for AI integrado en DSPM. Este documento conserva los nombres más reconocibles e indica el vigente cuando cambia el alcance.
- Responsible AI Standard: el rediseño con capítulos para desarrolladores e implementadores no tiene texto público.
- Seguridad de MCP: no existe un documento oficial único; la guía está repartida entre Azure MCP Server, Microsoft Entra, Azure API Management y Global Secure Access.
- Monitorización de Microsoft Foundry: anunciada como disponible de forma general en un blog de producto y marcada como versión preliminar en Learn.
- SFI: el informe de progreso de julio de 2026 no vuelve a mencionar explícitamente la compensación ligada a la seguridad.
- ISO/IEC 42001 de Microsoft 365 Copilot: fecha y organismo certificador no confirmados en dominios oficiales; Learn no lo lista literalmente entre los servicios en alcance.

### 9.2 Silencios de los marcos

- NIST AI RMF 1.0 está en revisión sin borrador público; podrían cambiar la redacción o los códigos de GOVERN 3.
- NIST IR 8596 (Cyber AI Profile) sigue como borrador preliminar; no hay versión pública inicial publicada.
- COSIS: los borradores de la serie IR 8605 no están confirmados. NIST adoptó la denominación «super intelligence» en sus comunicaciones tras una orden ejecutiva del 29 de septiembre de 2026; los identificadores publicados no cambian.
- SSDF 1.2 y Privacy Framework 1.1 siguen en borrador; FIPS 206 y el estándar para HQC no tienen borrador confirmado.
- CIS: no hay v9; el alcance de la denominación «v8.1.2» no está documentado oficialmente.
- TOGAF 10.ª edición: las fases del ADM se verificaron sobre el texto público de TOGAF 9, porque la publicación de la 10.ª edición bloquea la lectura automatizada.
- Open FAIR: la lista nominal de formas de pérdida no se confirmó.
- The Open Group: no hay estándar de IA o IA agéntica publicado; una guía de buenas prácticas para agentes está en preparación.
- COBIT 7: contenido no confirmado; lanzamiento el 19 de noviembre de 2026.
- AAISM: el nombre del dominio 2 difiere entre fuentes («AI Risk Management» en isaca.org).
- CSA: el cambio de IVS a I&S no figura en la página oficial; los identificadores de control de AICM se renumeraron entre v1.0 y v1.1, por lo que el cruce se hizo a nivel de dominio.
- MCSB: las páginas de v1 consultadas mapean a NIST SP 800-53 Rev. 4 y PCI DSS 3.2.1; v2 no tiene disponibilidad general.
- Puente The Open Group: el estándar de roles y glosario de seguridad citado por SAF es un borrador; su estado no se verificó.

### 9.3 Límites del método

- Las correspondencias con marcos son temáticas: no constituyen una declaración de cumplimiento ni sustituyen la lectura del control.
- La postura de Microsoft refleja documentación pública al 6 de noviembre de 2026; disponibilidad, nombres y licenciamiento cambian con frecuencia.
- Las leyes y regulaciones de IA y de protección de datos de cada país de la región no se enumeran: deben verificarse por jurisdicción con Legal.
- Los artefactos CDRR, ABRP, CTB y RRC son propuestas del AI CISO Atlas no validadas formalmente.
- La escala de evidencia 0–4 es un instrumento de trabajo; no equivale a una certificación.
- Las cifras del Microsoft Digital Defense Report describen tendencias globales; no son predicciones para una organización particular.
- Las salvaguardas de CIS se citan solo cuando su identificador es estable; en los demás casos se cita el control.

## 10. Fuentes

### 10.1 Postura y capacidades de Microsoft

- Secure Future Initiative — https://www.microsoft.com/en-us/trust-center/security/secure-future-initiative
- Informe de progreso de SFI, julio de 2026 — https://www.microsoft.com/en-us/trust-center/security/secure-future-initiative/sfi-progress-report-july-2026
- SFI en Microsoft Learn (correspondencia con Zero Trust y NIST CSF) — https://learn.microsoft.com/en-us/security/zero-trust/sfi/secure-future-initiative-overview
- Microsoft Digital Defense Report 2026 — https://www.microsoft.com/en-us/security/security-insider/threat-landscape/2026-digital-defense-report
- Microsoft Digital Defense Report 2025 — https://www.microsoft.com/en-us/security/security-insider/threat-landscape/microsoft-digital-defense-report-2025
- CISO Workshop — https://learn.microsoft.com/en-us/security/adoption/the-ciso-workshop
- Microsoft Cybersecurity Reference Architectures (MCRA) — https://learn.microsoft.com/en-us/security/adoption/mcra
- Zero Trust Adoption Framework — https://learn.microsoft.com/en-us/security/zero-trust/adopt/zero-trust-adoption-overview
- Zero Trust Assessment — https://learn.microsoft.com/en-us/security/zero-trust/assessment/overview
- Estrategia de acceso privilegiado — https://learn.microsoft.com/en-us/security/privileged-access-workstations/privileged-access-strategy
- Enterprise access model — https://learn.microsoft.com/en-us/security/privileged-access-workstations/privileged-access-access-model
- Ransomware operado por humanos — https://learn.microsoft.com/en-us/security/ransomware/human-operated-ransomware
- Respuesta a incidentes — https://learn.microsoft.com/en-us/security/operations/incident-response-overview
- MFA obligatoria para Azure — https://learn.microsoft.com/en-us/entra/identity/authentication/concept-mandatory-multifactor-authentication
- Autenticación sin contraseña resistente al phishing — https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-deploy-phishing-resistant-passwordless-authentication
- Microsoft Sentinel en el portal de Defender — https://learn.microsoft.com/en-us/azure/sentinel/microsoft-sentinel-defender-portal
- Interrupción automática de ataques — https://learn.microsoft.com/en-us/defender-xdr/automatic-attack-disruption
- Novedades de Security Exposure Management — https://learn.microsoft.com/en-us/security-exposure-management/whats-new
- Baseline Security Mode — https://learn.microsoft.com/en-us/microsoft-365/baseline-security-mode/baseline-security-mode-settings
- Quantum Safe Program (junio de 2026) — https://www.microsoft.com/en-us/security/blog/2026/06/30/microsoft-advances-quantum-safe-security-as-the-risk-timeline-shifts/
- Lista de regulaciones de Compliance Manager — https://learn.microsoft.com/en-us/purview/compliance-manager-regulations-list
- Microsoft Entra Agent ID — novedades — https://learn.microsoft.com/en-us/entra/agent-id/whats-new-agent-id
- Gobierno de identidades de agentes — https://learn.microsoft.com/en-us/entra/id-governance/agent-id-governance-overview
- Acceso condicional para agentes — https://learn.microsoft.com/en-us/entra/identity/conditional-access/agent-id
- Administrar identidades de agentes (deshabilitar y bloquear) — https://learn.microsoft.com/en-us/entra/agent-id/manage-agent-identities-admin
- Microsoft Agent 365 — https://learn.microsoft.com/en-us/microsoft-agent-365/overview
- Agent 365 disponible de forma general (1-may-2026) — https://www.microsoft.com/en-us/security/blog/2026/05/01/microsoft-agent-365-now-generally-available-expands-capabilities-and-integrations/
- Microsoft 365 E7 y Agent 365 disponibles de forma general — https://techcommunity.microsoft.com/blog/microsoft_365blog/microsoft-365-e7-and-agent-365-are-now-generally-available/4516295
- Inclusión de Security Copilot en Microsoft 365 E5 — https://learn.microsoft.com/en-us/copilot/security/security-copilot-inclusion
- Agente de optimización de acceso condicional — https://learn.microsoft.com/en-us/entra/security-copilot/conditional-access-agent-optimization
- Protección en tiempo real de agentes — https://learn.microsoft.com/en-us/defender-xdr/security-for-ai/ai-agent-real-time-protection
- Inventario de Power Platform — https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory
- Purview DSPM — https://learn.microsoft.com/en-us/purview/data-security-posture-management-learn-about
- DLP para Microsoft 365 Copilot — https://learn.microsoft.com/en-us/purview/dlp-microsoft365-copilot-location-learn-about
- Plantillas de Insider Risk Management — https://learn.microsoft.com/en-us/purview/insider-risk-management-policy-templates
- Auditoría de Copilot y agentes — https://learn.microsoft.com/en-us/purview/audit-copilot
- Purview para Microsoft 365 Copilot (etiquetas, eDiscovery) — https://learn.microsoft.com/en-us/purview/ai-m365-copilot
- SharePoint Advanced Management con licencias de Copilot — https://learn.microsoft.com/en-us/sharepoint/sharepoint-advanced-management-features-copilot-license
- Protección de datos empresariales de Microsoft 365 Copilot — https://learn.microsoft.com/en-us/microsoft-365/copilot/enterprise-data-protection
- Gestión de postura de seguridad de IA (Defender for Cloud) — https://learn.microsoft.com/en-us/azure/defender-for-cloud/ai-security-posture
- Protección contra amenazas para IA (Defender for Cloud) — https://learn.microsoft.com/en-us/azure/defender-for-cloud/ai-threat-protection
- Prompt Shields — https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection
- Task Adherence — https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/task-adherence
- Detección de groundedness (retiro en abril de 2027) — https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/groundedness
- Evaluadores de agentes de Foundry — https://learn.microsoft.com/en-us/azure/foundry/concepts/evaluation-evaluators/agent-evaluators
- AI Red Teaming Agent — https://learn.microsoft.com/en-us/azure/foundry/concepts/ai-red-teaming-agent
- Retiro de modelos en Foundry — https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/model-retirements
- Pasarela de IA de Azure API Management — https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities
- Servidores MCP en Azure API Management — https://learn.microsoft.com/en-us/azure/api-management/mcp-server-overview
- Seguridad de Azure MCP Server — https://learn.microsoft.com/en-us/azure/developer/azure-mcp-server/security
- Proteger servidores MCP con Microsoft Entra — https://learn.microsoft.com/en-us/entra/agent-id/secure-mcp-server-with-entra-id
- Modelo de responsabilidad compartida de IA — https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility-ai
- Modelo de responsabilidad compartida para agentes de IA — https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility-ai-agent
- Principios y enfoque de IA responsable — https://www.microsoft.com/en-us/ai/principles-and-approach
- Responsible AI Transparency Report — https://www.microsoft.com/en-us/corporate-responsibility/topics/responsible-ai/reports/transparency-report/
- Herramientas y prácticas de IA responsable (plantilla de evaluación de impacto) — https://www.microsoft.com/en-us/ai/tools-practices
- Customer Copyright Commitment — https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/openai/customer-copyright-commitment
- Guidelines for Human-AI Interaction — https://www.microsoft.com/en-us/research/publication/guidelines-for-human-ai-interaction/
- Cloud Adoption Framework para IA — https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai/strategy
- Centro de excelencia de IA (Cloud Adoption Framework) — https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai/center-of-excellence
- Agentes de IA (Cloud Adoption Framework) — https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/
- Lecciones de red teaming de 100 productos de IA generativa — https://www.microsoft.com/en-us/security/blog/2025/01/13/3-takeaways-from-red-teaming-100-generative-ai-products/
- Taxonomía de modos de falla en agentes de IA — https://www.microsoft.com/en-us/security/blog/2025/04/24/new-whitepaper-outlines-the-taxonomy-of-failure-modes-in-ai-agents/
- PyRIT — https://www.microsoft.com/en-us/security/blog/2024/02/22/announcing-microsofts-open-automation-framework-to-red-team-generative-ai-systems/
- Microsoft Cloud Security Benchmark v2 (versión preliminar) — learn.microsoft.com/security/benchmark/azure/overview
- ISO/IEC 42001 en Microsoft — learn.microsoft.com/compliance/regulatory/offering-iso-42001

**Fuentes agregadas en la versión 2.0**

- How Microsoft defends against indirect prompt injection attacks (MSRC, 29-jul-2025) — https://www.microsoft.com/en-us/msrc/blog/2025/07/how-microsoft-defends-against-indirect-prompt-injection-attacks
- 3 takeaways from red teaming 100 generative AI products (13-ene-2025) — https://www.microsoft.com/en-us/security/blog/2025/01/13/3-takeaways-from-red-teaming-100-generative-ai-products/
- Customer Lockbox requests (Microsoft Purview) — https://learn.microsoft.com/en-us/purview/customer-lockbox-requests
- Customer Lockbox for Microsoft Azure — https://learn.microsoft.com/en-us/azure/security/fundamentals/customer-lockbox-overview
- Microsoft's Approach to Coordinated Vulnerability Disclosure (MSRC) — https://www.microsoft.com/en-us/msrc/cvd
- Microsoft Responsible AI Standard v2 — General Requirements (junio de 2022) — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/final/en-us/microsoft-brand/documents/Microsoft-Responsible-AI-Standard-General-Requirements.pdf
- Microsoft Responsible AI Impact Assessment Guide (junio de 2022) — https://msblogs.thesourcemediaassets.com/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Guide.pdf
- Compliance Manager regulations list — https://learn.microsoft.com/en-us/purview/compliance-manager-regulations-list
- Review security initiatives in Microsoft Security Exposure Management — https://learn.microsoft.com/en-us/security-exposure-management/initiatives
- Exposure insights overview (Security Exposure Management) — https://learn.microsoft.com/en-us/security-exposure-management/exposure-insights-overview

**Publicaciones que originaron las preguntas nuevas**

- A01.9 (IC05) — ISC2: 2025 ISC2 Cybersecurity Workforce Study, Sección sobre factores económicos y recomendación final «Get Ready», 4 de diciembre de 2025 — https://www.isc2.org/insights/2025/12/2025-ISC2-Cybersecurity-Workforce-Study
- A02.8 (CI05) — CIS: CIS Risk Assessment Method (CIS RAM) v2.2 for CIS Controls v8.1, Blog oficial sobre CIS RAM, sección «The Principles» (estándar DoCRA), Página fechada el 5 de diciembre de 2025 — https://www.cisecurity.org/insights/blog/better-risk-assessment-outcome-cis-ram
- A02.9 (OG07) — The Open Group: The Open Group Standard for Risk Analysis (O-RA), Open FAIR, Secciones 4 y 5, etapa 2 (según la descripción oficial del Security Forum), O-RA 2.0.1; versión 2.1 anunciada en mayo de 2025 — https://blog.opengroup.org/2020/12/02/updates-to-the-open-fair-body-of-knowledge-part-2/
- A08.6 (IC07) — ISC2: 2025 ISC2 Cybersecurity Workforce Study, Sección «Skills Shortages Eclipse the Impact of Staff Shortages Alone», 4 de diciembre de 2025 — https://www.isc2.org/insights/2025/12/2025-ISC2-Cybersecurity-Workforce-Study
- A10.6 (IS05) — ISACA: COBIT: COBIT Certificate and Exam Updates (artículo oficial de soporte sobre COBIT 7), Secciones «COBIT 7 Launch Updates» y «COBIT 7 Licensing & Usage», Actualizado el 30 de octubre de 2026 — https://support.isaca.org/s/article/COBIT-Certificate-and-Exam-Updates
- A10.7 (OG09) — The Open Group: Calculating Reserves for Cyber Risk: Vetting Cyber Risk Models (White Paper), Boletín oficial del Security Forum, actualizaciones de los grupos de trabajo, Tercer trimestre de 2022 — https://www.opengroup.org/sites/default/files/Security_Forum_Newsletter_-_2Q2022%20ap%20update%20%2B%20JL.pdf
- A11.8 (IC01) — ISC2: ISC2 Code of Ethics, Preámbulo del Código, Versión vigente (sin fecha de revisión publicada) — https://www.isc2.org/ethics
- A11.9 (IC14) — ISC2: Cybersecurity Professionals Want Leaders Who Have Been Through a Major Incident, Secciones sobre confianza, rasgos de liderazgo y experiencia en incidentes, 28 de mayo de 2026 — https://www.isc2.org/Insights/2026/05/cybersecurity-pros-want-leaders-who-have-been-through-a-major-incident
- B08.7 (NI14) — NIST: Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations, NIST AI 100-2 E2025, Sección 1, «Introduction», 24 de marzo de 2025 — https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-2e2025.pdf

### 10.2 Marcos de referencia

| Familia | Marco | Versión y estado | Uso en este marco | Fuente oficial |
|---|---|---|---|---|
| NIST | Cybersecurity Framework (CSF) 2.0 — CSWP 29 | Final, 26-feb-2024 | Ancla de las 99 preguntas generales (22 categorías) y de los perfiles actual/objetivo | https://doi.org/10.6028/NIST.CSWP.29 |
| NIST | AI Risk Management Framework 1.0 — AI 100-1 | Final, 26-ene-2023; en revisión, sin borrador público | Ancla de las 99 preguntas de IA (GOVERN, MAP, MEASURE, MANAGE) | https://doi.org/10.6028/NIST.AI.100-1 |
| NIST | AI RMF Playbook | Vigente; se actualizará con la revisión del AI RMF | Acciones sugeridas por subcategoría | https://airc.nist.gov/airmf-resources/playbook/ |
| NIST | Generative AI Profile — AI 600-1 | Final, 26-jul-2024 (12 riesgos) | Riesgos específicos de IA generativa | https://doi.org/10.6028/NIST.AI.600-1 |
| NIST | Cyber AI Profile — IR 8596 | Borrador preliminar inicial, 16-dic-2025; en revisión de comentarios | Áreas Secure, Defend y Thwart sobre CSF 2.0 | https://csrc.nist.gov/pubs/ir/8596/iprd |
| NIST | COSIS (antes COSAiS): superposiciones de SP 800-53 para sistemas de IA | Documento conceptual ago-2025; esquema anotado ene-2026; renombrado 20-oct-2026 | Casos de uso de agente único y multiagente | https://csrc.nist.gov/projects/cosis |
| NIST | Adversarial Machine Learning — AI 100-2 E2025 | Final, 24-mar-2025 | Taxonomía de ataques a modelos | https://doi.org/10.6028/NIST.AI.100-2e2025 |
| NIST | AI Agent Standards Initiative (CAISI) | Lanzada el 17-feb-2026 | Estándares, protocolos e identidad de agentes | https://www.nist.gov/artificial-intelligence/ai-agent-standards-initiative |
| NIST | NCCoE — identidad y autorización de software y agentes de IA | Documento conceptual (borrador), 5-feb-2026 | Identidad y delegación de agentes | https://csrc.nist.gov/pubs/other/2026/02/05/accelerating-the-adoption-of-software-and-ai-agent/ipd |
| NIST | Zero Trust Architecture — SP 800-207 / SP 1800-35 | 800-207: 2020; 1800-35: final 10-jun-2025 | Arquitectura Zero Trust | https://doi.org/10.6028/NIST.SP.1800-35 |
| NIST | SSDF — SP 800-218 v1.1 y SP 800-218A | 800-218A final 26-jul-2024; SSDF 1.2 en borrador | Desarrollo seguro de software y de modelos | https://csrc.nist.gov/projects/ssdf |
| NIST | Incident Response — SP 800-61 Rev. 3 | Final, 3-abr-2025 (perfil comunitario de CSF 2.0) | Respuesta a incidentes | https://doi.org/10.6028/NIST.SP.800-61r3 |
| NIST | C-SCRM — SP 800-161 Rev. 1 | Final (actualización 1-nov-2024) | Cadena de suministro | https://doi.org/10.6028/NIST.SP.800-161r1-upd1 |
| NIST | Integración con ERM — IR 8286 Rev. 1 | Final, 18-dic-2025 | Riesgo cibernético en el riesgo empresarial | https://csrc.nist.gov/pubs/ir/8286/r1/final |
| NIST | SP 800-53 Rev. 5 | Release 5.2.0, 27-ago-2025 | Catálogo de controles (base de MCSB y COSIS) | https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final |
| NIST | Criptografía poscuántica — FIPS 203/204/205 e IR 8547 | FIPS ago-2024; IR 8547 final 27-oct-2026 (obsoletos después de 2030, prohibidos después de 2035) | Transición poscuántica | https://csrc.nist.gov/pubs/ir/8547/final |
| NIST | Privacy Framework | 1.0 vigente; 1.1 en borrador | Privacidad | https://www.nist.gov/privacy-framework |
| CIS | CIS Critical Security Controls v8.1 | 24-jun-2024; vigente (18 controles, 153 salvaguardas, IG1–IG3, función Govern) | Controles priorizados por grupo de implementación | https://www.cisecurity.org/controls/v8-1 |
| CIS | Controls v8.1 — AI LLM Companion Guide | 20-abr-2026 | Controles CIS aplicados a modelos de lenguaje | https://www.cisecurity.org/insights/white-papers/controls-v8-1-ai-llm-companion-guide |
| CIS | Controls v8.1 — AI Agents Companion Guide | 20-abr-2026 | Controles CIS aplicados a agentes | https://www.cisecurity.org/insights/white-papers/controls-v8-1-ai-agents-companion-guide |
| CIS | Controls v8.1 — MCP Companion Guide | 20-abr-2026 | Controles CIS aplicados a Model Context Protocol | https://www.cisecurity.org/insights/white-papers/controls-v8-1-model-context-protocol-companion-guide |
| CIS | AI Security Guidance Workbook (v8.1.2) | 27-jul-2026 | Libro de trabajo de seguridad de IA | https://www.cisecurity.org/insights/white-papers/controls-v8-1-2-ai-security-guidance-workbook |
| CIS | CIS Benchmarks — Microsoft 365 Foundations v7.0.0 y Azure Foundations v7.0.0 | M365 v7.0.0: may-2026 | Configuración segura de referencia | https://www.cisecurity.org/benchmark/microsoft_365 |
| CIS | CIS RAM v2.2 | Página del 5-dic-2025 | Método de evaluación de riesgo | https://www.cisecurity.org/insights/white-papers/cis-ram-risk-assessment-method |
| The Open Group | TOGAF Standard, 10th Edition (C220) | Vigente desde 25-abr-2022 | Fases del ADM, gobierno de arquitectura, principios | opengroup.org/togaf |
| The Open Group | TOGAF Series Guide G152 — Integrating Risk and Security within a TOGAF Enterprise Architecture | Rev. abr-2022 (con The SABSA Institute) | Riesgo y seguridad en la arquitectura empresarial | opengroup.org/togaf/series-guides |
| The Open Group | Open FAIR — O-RT 3.0.1 y O-RA 2.0.1 | Vigentes | Cuantificación del riesgo | opengroup.org/open-fair |
| The Open Group | Zero Trust Commandments (estándar) y ZT Reference Model (snapshot v1.0) | Commandments: estándar vigente; Reference Model: borrador | Principios Zero Trust | opengroup.org/forum/security/Zerotrust |
| The Open Group | Security Principles for Architecture; Security Design Patterns; O-ESA | O-ESA: 2011 | Principios y patrones de arquitectura de seguridad | opengroup.org/forum/security/architecture |
| The Open Group | Guía G268 — Artificial Intelligence (AI) in Digital Transformation; guía de uso de IA | Sin estándar de IA publicado al 6-nov-2026 | IA en la transformación digital | pubs.opengroup.org/standards-guide/g_guidance-for-ai-use/ |
| The Open Group | Security Roles and Glossary (borrador, citado por SAF) | Borrador | Roles y responsabilidades de seguridad | https://publications.opengroup.org/s252 |
| ISACA | COBIT 2019 (40 objetivos) | Vigente; COBIT 7 se lanza el 19-nov-2026; COBIT 2019 se retira el 31-dic-2027 | Objetivos de gobierno y gestión | isaca.org/resources/cobit |
| ISACA | Risk IT Framework, 2nd Edition | 25-jun-2020 | Gobierno y gestión del riesgo de I&T | isaca.org/resources/cobit |
| ISACA | Digital Trust Ecosystem Framework (DTEF) | Mar-2024 | Confianza digital | isaca.org/digital-trust |
| ISACA | Artificial Intelligence Audit Toolkit | 6-jun-2024 | Controles y evaluación de IA (explicabilidad) | isaca.org/store2/product/WAICAT |
| ISACA | AAISM — Advanced in AI Security Management | 19-ago-2025 (D1 Gobierno y programa; D2 Riesgo; D3 Tecnologías y controles) | Competencias de gestión de seguridad de IA | isaca.org/credentialing/aaism/aaism-exam-content-outline |
| ISACA | AAIA — Advanced in AI Audit | 19-may-2025 | Auditoría de IA | isaca.org/credentialing/aaia/aaia-exam-content-outline |
| CSA | Cloud Controls Matrix (CCM) v4.1 + CAIQ v4.1 | 27/28-ene-2026 (207 controles, 17 dominios) | Controles de nube para las 99 preguntas generales | cloudsecurityalliance.org/artifacts/cloud-controls-matrix-v4-1 |
| CSA | AI Controls Matrix (AICM) v1.1 | 22-jun-2026 (247 objetivos, 18 dominios: 17 de CCM + MDS) | Controles de IA para las 99 preguntas de IA | cloudsecurityalliance.org/artifacts/ai-controls-matrix-v1-1 |
| CSA | STAR y STAR for AI | STAR for AI: 23-oct-2025; Nivel 2 desde 20-nov-2025 | Aseguramiento y certificación | cloudsecurityalliance.org/star/ai/ |
| CSA | MAESTRO (modelado de amenazas para IA agéntica) | 6-feb-2025 (7 capas) | Amenazas por capa en sistemas agénticos | cloudsecurityalliance.org/blog/2025/02/06/agentic-ai-threat-modeling-framework-maestro |
| CSA | Agentic AI Red Teaming Guide | 28-may-2025 | Red teaming de agentes | cloudsecurityalliance.org/artifacts/agentic-ai-red-teaming-guide |
| CSA | Agentic AI Identity and Access Management: A New Approach | 18-ago-2025 | Identidad de agentes | cloudsecurityalliance.org/artifacts/agentic-ai-identity-and-access-management-a-new-approach |
| CSA | Security Guidance v5 | 15-jul-2024 (actualizada 26-ago-2025) | Guía de seguridad en la nube | cloudsecurityalliance.org/artifacts/security-guidance-v5 |
| Microsoft (puente) | Microsoft Cloud Security Benchmark v1 | Vigente (12 dominios; correspondencias con CIS v8, NIST SP 800-53 r4 y PCI DSS 3.2.1) | Puente entre capacidades Microsoft y marcos | learn.microsoft.com/security/benchmark/azure/overview-mcsb-v1 |
| Microsoft (puente) | Microsoft Cloud Security Benchmark v2 | Versión preliminar; agrega el dominio AI (AI-1 a AI-7) | Controles de IA de Microsoft | learn.microsoft.com/security/benchmark/azure/overview |
| Microsoft (puente) | Purview Compliance Manager — lista de regulaciones | Incluye EU AI Act, ISO/IEC 42001, ISO/IEC 23894, NIST AI RMF, NIST CSF 2.0, CIS IG1–3, CSA CCM, MCSB, NIST 800-207; no COBIT 2019 | Evaluación y evidencia | learn.microsoft.com/purview/compliance-manager-regulations-list |
| Microsoft (puente) | ISO/IEC 42001 — servicios de Microsoft en alcance | Copilot Studio, Microsoft Foundry, Security Copilot y otros; Microsoft 365 Copilot comunicado en 2025 | Sistema de gestión de IA | learn.microsoft.com/compliance/regulatory/offering-iso-42001 |
| Microsoft (puente) | Certificación CSA STAR (Azure) | Vigente (página de 2023 cita CCM v4) | Evidencia de terceros | learn.microsoft.com/azure/compliance/offerings/offering-csa-star-certification |

### 10.3 Documentos de trabajo propios

- AI CISO Atlas v3.0 — Estrategia maestra, arquitectura de conocimiento y programa de 60 ensayos (31 de octubre de 2026).
- Arquitectura Operativa y Marco de Conocimiento para el Proyecto TheNextCISO: CISO-OS, CISO-DO, CISO-MM y CISO-NX (3 de noviembre de 2026).
- SAF — AI Security: Strategy and Governance Planning (presentación del taller de Microsoft y ficha descriptiva).
- Análisis de seguridad, gobierno y observabilidad para Microsoft 365 Copilot y agentes de IA (21 de septiembre de 2026).
- Instrumentos de evaluación, modelos de madurez y bancos de preguntas (SAF, Unified y kits CSU/ATS).
- Microsoft Digital Defense Report 2026 — implicancias para CISOs y arquitectos de Latinoamérica (20 de octubre de 2026).

## Anexo A — Equivalencia orientativa de escalas

Equivalencia de trabajo, no oficial, para conversar con distintos marcos sin perder la escala de evidencia del AI CISO Atlas.

| AI CISO Atlas (evidencia) | TheNextCISO (CISO-MM) | NIST CSF 2.0 (Tiers) | SAF — hoja de ruta de gobierno y seguridad de IA |
|---|---|---|---|
| 0 — No definido | Nivel 1 — Ad hoc / reactivo | Tier 1 — Partial | 1 — Sin gobierno formal |
| 1 — Documentado | Nivel 2 — Repetible / informal | Tier 2 — Risk Informed | 2 — Lineamientos básicos |
| 2 — Implementado | Nivel 3 — Definido / formalizado | Tier 3 — Repeatable | 3 — Gobierno emergente |
| 3 — Probado | Nivel 3–4 (transición) | Tier 3–4 (transición) | 4 — Gobierno integrado |
| 4 — Adaptativo | Nivel 4 — Adaptativo / optimizado | Tier 4 — Adaptive | 5 — IA confiable y auditable |

## Anexo B — Glosario

| Sigla | Significado |
|---|---|
| ABRP | Agent Blast-Radius Profile (AI CISO Atlas). |
| AICM | AI Controls Matrix de Cloud Security Alliance. |
| AI RMF | AI Risk Management Framework de NIST. |
| AAISM | Advanced in AI Security Management (ISACA). |
| CCM | Cloud Controls Matrix de Cloud Security Alliance. |
| CDRR | CISO Decision & Resilience Record (AI CISO Atlas). |
| COE | Centro de excelencia. |
| CSF | Cybersecurity Framework de NIST. |
| CTB | Containment Time Budget (AI CISO Atlas). |
| DLP | Prevención de pérdida de datos. |
| DSPM | Gestión de la postura de seguridad de los datos. |
| MAESTRO | Marco de modelado de amenazas para IA agéntica de CSA (7 capas). |
| MCP | Model Context Protocol. |
| MCSB | Microsoft Cloud Security Benchmark. |
| Open FAIR | Estándares de The Open Group para taxonomía (O-RT) y análisis (O-RA) del riesgo. |
| RRC | Risk & Resilience Contract (AI CISO Atlas). |
| SAF | Security Adoption Framework de Microsoft. |
| SCAP | Security Capability Adoption Planning (taller de SAF). |
| SFI | Secure Future Initiative de Microsoft. |
| STRIDER-TIM | Extensión de STRIDE usada en SAF: suplantación, manipulación, denegación de respuesta, divulgación, denegación de servicio, elevación de privilegios, denegación de recuperación, engaño, abuso interno y abuso de mantenimiento. |
| TOGAF | Estándar de arquitectura empresarial de The Open Group (10.ª edición). |


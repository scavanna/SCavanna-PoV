# Las 99 preguntas que le harán al CISO

## Quién pregunta, qué quiere saber realmente y cómo responder con evidencia — complemento del marco «99 + 99 preguntas que un CISO tiene que hacer»

| Ficha |  |
|---|---|
| Versión | 1.1 — 6 de noviembre de 2026. Alineada con la versión 2.0 del marco 99 + 99 (la versión 1.0 se conserva como referencia) |
| Autor | Santiago Cavanna, Principal Cloud Solution Architect Security — Microsoft MCSA |
| Alcance | 99 preguntas que once interlocutores le harán al CISO; 34 sobre IA, agentes y sistemas autónomos |
| Relación con el marco 99 + 99 | Las 198 preguntas del marco son las que el CISO hace para gobernar; estas 99 son las que otros le harán para pedirle cuentas. Cada pregunta remite a las del marco que preparan su respuesta, con la numeración de la versión 2.0 |
| Base conceptual | AI CISO Atlas v3.0, TheNextCISO (marco integrado), Security Adoption Framework (SAF) de Microsoft — AI Security Strategy & Governance |
| Vigencia de la información de Microsoft | Verificada en fuentes oficiales al 6 de noviembre de 2026; revalidar después de Microsoft Ignite 2026 (17 al 20 de noviembre) |

## Contenido

- Novedades de la versión 1.1
- Resumen ejecutivo
- 1. Por qué un cuestionario invertido
- 2. Cómo usar este cuestionario
- 3. Anatomía de cada pregunta
- 4. Nueve reglas para responder
- 5. Los once interlocutores
- 6. Las 99 preguntas
- 7. Matriz de preparación: del marco 99 + 99 a las respuestas
- 8. Escala de preparación
- 9. Lo que Microsoft aporta para responder
- 10. Silencios, límites y vigencia
- 11. Fuentes

## Novedades de la versión 1.1

Esta versión alinea el cuestionario con la versión 2.0 del marco «99 + 99 preguntas que un CISO tiene que hacer». Las 99 preguntas al CISO, sus textos, sus interlocutores y su orden no cambian; cambian sus vínculos con el marco, que ahora usan la numeración 2.0.

- **7 vínculos traducidos.** Apuntaban a preguntas que la versión 2.0 fusionó dentro de su dominio; ahora apuntan a la pregunta que las absorbió. En 3 casos la pregunta absorbente ya estaba vinculada y el vínculo se unificó.
- **10 vínculos nuevos.** Las nueve preguntas nuevas de la versión 2.0 nacieron del proceso inverso «Del marco a la pregunta». Cada una se vincula con las preguntas al CISO que su pareja de origen ya respaldaba: la evidencia que pide la pregunta nueva es la que el CISO necesita para responderlas.
- **Cobertura.** Las preguntas del marco que preparan al menos una respuesta pasan de 159 a 163 de 198, y el trabajo invisible baja de 39 a 35 preguntas. Los vínculos pasan de 295 a 302.
- **Marcos heredados.** Los códigos de NIST, CIS, The Open Group, ISACA y CSA que cada pregunta hereda se recalcularon con los anclajes de la versión 2.0; cambian en 23 de las 99 preguntas.
- **Cómo leer los identificadores.** Todo identificador del marco se lee ahora con la numeración 2.0. Nueve identificadores cambiaron de contenido. Por ejemplo, A01.9 ya no es «¿Qué modelo operativo tiene la función de seguridad (central, federado, BISO, servicios gestion…» (ese contenido pasó a A01.2), sino «Antes de reducir la dotación o el presupuesto de seguridad, ¿se evalúa y documenta el impacto e…». La tabla completa de equivalencias está en el marco 2.0 (sección «Novedades de la versión 2.0») y en la hoja «Cambios_v2» de su matriz.

| Pregunta al CISO | Interlocutor | Cambio | Vínculo v1.0 | Vínculo v1.1 | Pregunta del marco (v2.0) | Nota |
|---|---|---|---|---|---|---|
| C01.8 | Directorio | Traducido | A10.7 | A10.1 | ¿Qué obligaciones legales, regulatorias y contractuales de seguridad nos aplican por país… | La pregunta absorbente ya estaba vinculada: el vínculo se unifica. |
| C01.9 | Directorio | Agregado | — | A01.9 | Antes de reducir la dotación o el presupuesto de seguridad, ¿se evalúa y documenta el impa… | Pregunta nueva de la v2.0 (pareja de origen IC05). |
| C02.1 | Comité de auditoría y riesgos | Agregado | — | A10.6 | ¿Qué versiones de los marcos de referencia usamos (COBIT, NIST, ISO, CIS, CCM) y qué plan… | Pregunta nueva de la v2.0 (pareja de origen IS05). |
| C02.2 | Comité de auditoría y riesgos | Agregado | — | A02.8 | ¿Nuestro análisis de riesgo considera el daño que podemos causar a terceros (clientes, ciu… | Pregunta nueva de la v2.0 (pareja de origen CI05). |
| C02.4 | Comité de auditoría y riesgos | Agregado | — | A10.7 | ¿Quién valida de forma independiente el modelo con el que cuantificamos el riesgo cibernét… | Pregunta nueva de la v2.0 (pareja de origen OG09). |
| C02.5 | Comité de auditoría y riesgos | Agregado | — | B08.7 | ¿Qué controles de IA damos por eficaces sin garantías demostradas, y cómo compensamos ese… | Pregunta nueva de la v2.0 (pareja de origen NI14). |
| C02.8 | Comité de auditoría y riesgos | Traducido | A02.8 | A02.2 | ¿Cuáles son nuestras joyas de la corona (procesos, datos, sistemas e identidades) y qué es… | La v2.0 integró A02.8 en A02.2. |
| C04.2 | CFO, finanzas y tesorería | Agregado | — | A01.9 | Antes de reducir la dotación o el presupuesto de seguridad, ¿se evalúa y documenta el impa… | Pregunta nueva de la v2.0 (pareja de origen IC05). |
| C04.2 | CFO, finanzas y tesorería | Agregado | — | A02.9 | ¿Qué precisión necesita cada decisión de riesgo, y estamos invirtiendo esfuerzo de análisi… | Pregunta nueva de la v2.0 (pareja de origen OG07). |
| C04.5 | CFO, finanzas y tesorería | Traducido | A02.9 | A02.5 | ¿Cada aceptación de riesgo tiene dueño, alcance, evidencia, vencimiento y disparadores de… | La v2.0 integró A02.9 en A02.5. |
| C05.3 | Negocio y producto | Traducido | A10.6 | A10.3 | ¿Cuánta de nuestra evidencia de cumplimiento es automática y continua, cuánta depende de m… | La v2.0 integró A10.6 en A10.3. |
| C07.3 | Legal, cumplimiento y privacidad | Agregado | — | A11.8 | ¿Qué código de conducta profesional rige al equipo de seguridad, cómo se resuelven sus dil… | Pregunta nueva de la v2.0 (pareja de origen IC01). |
| C07.6 | Legal, cumplimiento y privacidad | Traducido | A10.7 | A10.1 | ¿Qué obligaciones legales, regulatorias y contractuales de seguridad nos aplican por país… | La v2.0 integró A10.7 en A10.1. |
| C09.2 | Auditoría interna, auditoría externa y certificadores | Traducido | A10.6 | A10.3 | ¿Cuánta de nuestra evidencia de cumplimiento es automática y continua, cuánta depende de m… | La pregunta absorbente ya estaba vinculada: el vínculo se unifica. |
| C09.8 | Auditoría interna, auditoría externa y certificadores | Agregado | — | A08.6 | ¿Qué incidentes y configuraciones erróneas del último año se explican, al menos en parte,… | Pregunta nueva de la v2.0 (pareja de origen IC07). |
| C11.2 | Personas: colaboradores, RR. HH. y el equipo de seguridad | Traducido | A11.8 | A11.1 | ¿Qué conductas de seguridad esperamos de cada rol, cómo medimos el cambio de comportamient… | La pregunta absorbente ya estaba vinculada: el vínculo se unifica. |
| C11.5 | Personas: colaboradores, RR. HH. y el equipo de seguridad | Agregado | — | A11.9 | ¿Cómo evalúa el equipo de seguridad el liderazgo del CISO (comunicar el riesgo al director… | Pregunta nueva de la v2.0 (pareja de origen IC14). |

## Resumen ejecutivo

Un CISO no se evalúa solo por las preguntas que hace, sino por las que sabe responder. Este cuestionario reúne 99 preguntas que el directorio, el comité de auditoría, el CEO, el CFO, el negocio, los líderes de tecnología e IA, Legal, los reguladores, los auditores, los terceros externos y las personas de la organización le harán al CISO. Para cada una indica qué quiere saber realmente quien pregunta, qué contiene una respuesta sólida, qué respuesta debería encender una alarma, qué preguntas del marco 99 + 99 la preparan y qué aporta Microsoft como evidencia.

Cinco ideas ordenan el conjunto:

1. **Cada pregunta al CISO se responde con la evidencia que producen las preguntas que el CISO hizo antes.** Las 99 preguntas se vinculan con 163 de las 198 preguntas del marco (302 vínculos en total).
2. **La IA ya no es un tema de nicho.** 34 de las 99 preguntas tratan sobre IA, agentes o sistemas autónomos, y aparecen en los once interlocutores: del directorio al analista del SOC.
3. **Los interlocutores piden pocas cosas, una y otra vez:** tendencia de la exposición frente al apetito aprobado, recuperación probada, inventario de agentes con dueño, obligaciones de notificación por país, evidencia continua de que los controles funcionan y decisiones explícitas.
4. **Muchas respuestas no dependen de una herramienta.** En 14 preguntas la respuesta es una decisión de gobierno, un proceso o una cuestión de personas, y en 2 Microsoft no publica una postura específica. La tecnología produce evidencia; el gobierno produce respuestas.
5. **Hay trabajo que nadie le pedirá al CISO, pero que sostiene todas las respuestas.** 35 de las 198 preguntas del marco no aparecen como preparación de ninguna pregunta de los interlocutores (16 de la Parte A y 19 de la Parte B). Son el trabajo invisible de la función y no deben abandonarse por no ser visibles.

## 1. Por qué un cuestionario invertido

El marco «99 + 99 preguntas que un CISO tiene que hacer» mira desde el CISO hacia la organización: qué debe preguntar para gobernar la seguridad y la adopción de la IA. Este cuestionario invierte la dirección: mira desde quienes supervisan, financian, regulan, auditan, compran, aseguran, invierten o trabajan con la organización hacia el CISO. Las dos miradas se necesitan: el marco produce la evidencia y este cuestionario verifica si esa evidencia responde lo que los demás necesitan saber.

La inversión tiene tres efectos prácticos. Primero, prioriza: las preguntas del marco que preparan muchas respuestas merecen atención temprana. Segundo, alinea el lenguaje: cada interlocutor pregunta en su idioma (pérdida, plazo, obligación, cliente, carrera) y espera una respuesta en ese idioma. Tercero, revela vacíos: cuando no existe evidencia para responder, la brecha queda a la vista antes de que la descubra un supervisor, un auditor o un incidente.

## 2. Cómo usar este cuestionario

| Uso | Cómo |
|---|---|
| Simulacro trimestral | Elegir dos o tres preguntas por interlocutor, responderlas en voz alta frente a un par o al equipo, y registrar qué evidencia faltó. |
| Kit de respuesta | Preparar para cada pregunta una ficha breve: conclusión, evidencia, indicador con tendencia, decisión que se pide y riesgo de no decidir. |
| Matriz de preparación | Usar la sección 7 para saber qué preguntas del marco 99 + 99 hay que responder primero para poder contestar a cada interlocutor. |
| Medición | Calificar la preparación de cada respuesta con la escala 0–4 (sección 8) en la matriz de Excel y revisar la tendencia cada trimestre. |
| Consistencia | Asignar un dueño a cada indicador para que todas las audiencias reciban la misma versión de los hechos. |

## 3. Anatomía de cada pregunta

| Campo | Contenido |
|---|---|
| Quién pregunta y cuándo | El interlocutor concreto y el momento típico en que llega la pregunta. |
| Qué quiere saber realmente | La intención detrás de la pregunta: lo que debe quedar claro aunque no se diga. |
| Una respuesta sólida incluye | La evidencia, los indicadores y la decisión que convierten una opinión en una respuesta verificable. |
| Señal de alerta | La respuesta que debilita la confianza en la función de seguridad. |
| Cómo prepararse | Las preguntas del marco 99 + 99 que producen la evidencia necesaria (A = agenda del CISO; B = IA y agentes). |
| Apoyo de Microsoft | Capacidades, informes o marcos de trabajo de Microsoft que aportan evidencia, o el silencio cuando Microsoft no publica una postura específica. |
| Marcos (heredados) | Códigos de NIST, CIS, The Open Group, ISACA y CSA heredados de las preguntas de preparación: los más frecuentes, hasta tres por familia. |

## 4. Nueve reglas para responder

1. **Conclusión primero.** Empezar por la respuesta y por la decisión que se pide; el detalle va después.
2. **Evidencia y tendencia, no actividad.** Un indicador comparado con el período anterior y con el apetito aprobado vale más que una lista de proyectos.
3. **El idioma de quien pregunta.** Pérdida y probabilidad para el CFO, plazo y obligación para Legal, cliente y velocidad para el negocio.
4. **Distinguir diseño, implementación y eficacia.** Una política es nivel 1; un control probado es nivel 3 (escala del AI CISO Atlas).
5. **Una sola verdad.** La misma evidencia para todas las audiencias; las respuestas distintas a la misma pregunta destruyen la confianza.
6. **«No lo sabemos» es una respuesta válida** si viene con dueño, fecha y método para averiguarlo.
7. **No promediar.** Mostrar el peor caso relevante: un cero en recuperación no se compensa con un cuatro en otra área.
8. **Separar hechos, estimaciones y opiniones,** y aclarar la naturaleza de cada fuente: ley, estándar, guía, dato propio o hipótesis.
9. **Cerrar con el riesgo de no decidir.** Toda respuesta que pide una decisión debe mostrar qué pasa si la decisión no se toma.

## 5. Los once interlocutores

| Código | Interlocutor | Qué le preocupa | Frecuencia típica | Qué espera recibir | Preguntas sobre IA |
|---|---|---|---|---|---|
| C01 | Directorio | El directorio no gestiona la seguridad: la supervisa. Pregunta si la exposición está dentro del apetito aprobado, si la organización está preparada para lo peor y qué decisiones le corresponden. | Trimestral, más sesiones extraordinarias | Pocos indicadores con tendencia, escenarios materiales y decisiones explícitas | 2 |
| C02 | Comité de auditoría y riesgos | El comité busca aseguramiento: que los controles estén diseñados, implementados y funcionen, y que la información que llega al directorio sea confiable. | Trimestral | Evidencia, excepciones, hallazgos abiertos y criterios de materialidad | 2 |
| C03 | CEO y comité ejecutivo | El CEO pregunta por el negocio: qué protege la seguridad, cuánto frena o habilita, qué riesgo no se está tratando y si la organización resistiría una crisis. | Mensual y ante eventos | Conclusión primero, impacto en el negocio y una decisión concreta | 3 |
| C04 | CFO, finanzas y tesorería | El CFO traduce la seguridad a números: pérdidas esperadas, retorno de la inversión, transferencia de riesgo, fraude y control del gasto, incluido el de la IA. | Ciclo presupuestario y renovación de pólizas | Rangos cuantificados, supuestos explícitos y costo total | 2 |
| C05 | Negocio y producto | Las áreas de negocio preguntan qué pueden hacer, cuándo y con qué condiciones. Miden a seguridad por la velocidad y la claridad de sus respuestas. | Continua | Respuesta rápida, alternativa segura y condiciones claras | 4 |
| C06 | Tecnología, datos e IA | CIO, CTO, CDO, CAIO e ingeniería preguntan por arquitectura, plataforma, datos y fricción: qué controles impone seguridad, con qué costo operativo y cómo se integran en su forma de trabajar. | Continua y en cada decisión de arquitectura | Patrones, criterios técnicos y derechos de decisión compartidos | 5 |
| C07 | Legal, cumplimiento y privacidad | Legal, cumplimiento y privacidad preguntan qué debemos, a quién, en qué plazo y cómo lo demostramos, incluida la regulación emergente de IA. | Continua y ante incidentes | Obligaciones por país, plazos, evidencia y responsabilidad | 3 |
| C08 | Reguladores y supervisores | Los supervisores preguntan por gobierno, resiliencia, terceros, notificación y, cada vez más, por el uso de la IA en procesos que afectan a clientes. Esperan evidencia en plazos cortos. | Inspecciones, requerimientos y reportes periódicos | Responsables con nombre, evidencia verificable y tiempos medidos | 2 |
| C09 | Auditoría interna, auditoría externa y certificadores | Los auditores preguntan por el diseño y la eficacia de los controles sobre la población completa y durante todo el período, no por la intención. | Plan anual de auditoría y certificaciones | Población completa, evidencia continua y trazabilidad | 3 |
| C10 | Clientes, socios, aseguradoras e inversores | Los terceros externos preguntan si pueden confiar: compartir datos, integrarse, asegurar o invertir. Esperan respuestas consistentes, verificables y rápidas. | Contratación, renovación, due diligence e incidentes | Evidencia independiente y compromisos verificables | 3 |
| C11 | Personas: colaboradores, RR. HH. y el equipo de seguridad | Las personas preguntan qué pueden hacer, qué se espera de ellas y qué pasa con su trabajo. El equipo de seguridad pregunta por prioridades, carga y futuro profesional. | Continua | Claridad, coherencia y cuidado de las personas | 5 |

## 6. Las 99 preguntas

### C01 · Directorio

El directorio no gestiona la seguridad: la supervisa. Pregunta si la exposición está dentro del apetito aprobado, si la organización está preparada para lo peor y qué decisiones le corresponden.

#### C01.1 · ¿Estamos más o menos expuestos que hace un año, y cómo lo sabemos?

- **Quién pregunta:** Presidente del directorio · **Cuándo:** Sesión trimestral del directorio
- **Qué quiere saber realmente:** Quiere una tendencia de exposición con evidencia comparable en el tiempo, no un inventario de actividades.
- **Una respuesta sólida incluye:** Tres a cinco indicadores de riesgo con tendencia (exposición de activos críticos, cobertura de MFA resistente al phishing, tiempo de contención, sobreexposición de datos, agentes sin dueño), comparados con los umbrales del apetito; qué mejoró, qué empeoró y por qué, y qué confianza merecen los datos.
- **Señal de alerta:** Cantidad de alertas o ataques bloqueados, listas de proyectos o un puntaje sin contexto ni tendencia.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** A02.6 (¿Qué indicadores anticipan una pérdida material y cuáles se reportan a…) · A06.8 (¿Cómo medimos y comunicamos la postura (puntuación de seguridad, expos…) · A01.4 (¿Con qué frecuencia, formato y métricas supervisa el directorio el rie…) · B08.8 (¿Qué indicadores de confianza en la IA presentamos al directorio (inci…)
- **Apoyo de Microsoft:** Microsoft Security Exposure Management (métricas e iniciativas de exposición); Microsoft Secure Score; informes de Microsoft Defender XDR.
- **Marcos (heredados):** NIST — CSF GV.OV, CSF ID.IM, CSF GV.RR | CIS — CIS 7, CIS 4 | The Open Group — Open FAIR | ISACA — COBIT MEA01, COBIT EDM05, COBIT APO12 | CSA — CCM GRC, CCM TVM, AICM GRC

#### C01.2 · ¿Cuáles son los tres escenarios que podrían causarnos un daño material y qué tan preparados estamos para cada uno?

- **Quién pregunta:** Directorio · **Cuándo:** Planificación anual y sesión de riesgos
- **Qué quiere saber realmente:** Quiere entender la materialidad en términos de negocio y la distancia entre el riesgo y la preparación real.
- **Una respuesta sólida incluye:** Escenarios priorizados (por ejemplo, ransomware destructivo, fraude por suplantación con IA, falla de un proveedor crítico, agente con permisos excesivos), impacto estimado en rangos, controles clave, último ensayo y su resultado, brecha y decisión que se solicita.
- **Señal de alerta:** Escenarios genéricos sin impacto estimado ni ensayo reciente.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** A02.2 (¿Cuáles son nuestras joyas de la corona (procesos, datos, sistemas e i…) · A02.3 (¿Cuantificamos el riesgo con rangos y supuestos explícitos, o con matr…) · A09.2 (¿Podemos recuperar identidad, datos y servicios críticos tras un ranso…) · A09.5 (¿Cómo se gestiona una crisis cibernética: comité, roles, decisiones di…) · B07.2 (¿Tenemos un perfil de radio de impacto por agente (datos, herramientas…)
- **Apoyo de Microsoft:** Exposure Management (rutas de ataque hacia activos críticos); Microsoft Digital Defense Report 2026 como contexto de amenazas.
- **Marcos (heredados):** NIST — CSF ID.RA, CSF ID.AM, CSF GV.RM | CIS — CIS RAM, CIS 1, CIS 3 | The Open Group — Open FAIR, TOGAF | ISACA — COBIT APO12, COBIT DSS04, COBIT BAI09 | CSA — CCM GRC, CCM BCR, CCM DSP

#### C01.3 · ¿Nuestro riesgo cibernético está dentro del apetito que aprobamos? ¿Dónde no, y qué nos propone?

- **Quién pregunta:** Directorio · **Cuándo:** Sesión trimestral del directorio
- **Qué quiere saber realmente:** Quiere decidir: aceptar, invertir, transferir o evitar. Sin apetito aprobado no hay contra qué comparar.
- **Una respuesta sólida incluye:** Comparación explícita, indicador por indicador, contra los umbrales aprobados; desvíos con dueño, causa, plan y fecha; alternativas con costo y riesgo residual; decisión solicitada al directorio.
- **Señal de alerta:** No existe un apetito aprobado, o el CISO lo reinterpreta sin aprobación formal.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** A02.1 (¿Cuál es nuestro apetito y tolerancia de riesgo cibernético expresado…) · A02.5 (¿Cada aceptación de riesgo tiene dueño, alcance, evidencia, vencimient…) · A01.3 (¿Qué decisiones de riesgo puede tomar el CISO por sí mismo, cuáles cor…)
- **Apoyo de Microsoft:** Decisión de gobierno; los indicadores provienen de Exposure Management, Secure Score y Defender XDR.
- **Marcos (heredados):** NIST — CSF GV.RM, IR 8286, CSF ID.RA | CIS — CIS RAM | The Open Group — Open FAIR, TOGAF | ISACA — COBIT APO12, COBIT EDM03, Risk IT | CSA — CCM GRC

#### C01.4 · ¿Cómo supervisamos la IA y los agentes que ya operan en la compañía, y quién responde por ellos?

- **Quién pregunta:** Directorio · **Cuándo:** Sesión trimestral y aprobación de la estrategia de IA · **Tema:** IA y agentes
- **Qué quiere saber realmente:** Quiere saber si existe rendición de cuentas y visibilidad sobre un patrimonio que crece fuera de los proyectos formales.
- **Una respuesta sólida incluye:** Inventario con cobertura medida (agentes con identidad, dueño, política y monitoreo), consejo de IA con mandato, niveles de autonomía permitidos, incidentes y bloqueos del período, y las decisiones de alto impacto reservadas al directorio.
- **Señal de alerta:** «TI lo tiene controlado», sin inventario ni dueños con nombre.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** B02.2 (¿Existe un consejo interdisciplinario de IA (negocio, seguridad, riesg…) · B03.1 (¿Tenemos un inventario único de modelos, aplicaciones, copilotos, agen…) · B03.9 (¿Qué indicadores de cobertura usamos (agentes inventariados, con ident…) · B07.1 (¿Qué nivel de autonomía permitimos a cada agente (sugerir, ejecutar co…) · B08.8 (¿Qué indicadores de confianza en la IA presentamos al directorio (inci…) · B02.1 (¿Tenemos un marco de IA responsable publicado, patrocinado por la dire…)
- **Apoyo de Microsoft:** Microsoft Agent 365 (registro y control de agentes); Microsoft Entra Agent ID; Microsoft Purview DSPM.
- **Marcos (heredados):** NIST — AI RMF GOVERN 2, AI RMF GOVERN 1, AI RMF MEASURE 1 | CIS — CIS 1, CIS 2, guía CIS para agentes de IA | The Open Group — TOGAF, Open FAIR | ISACA — AAISM D1, COBIT APO01, COBIT EDM01 | CSA — AICM GRC, AICM MDS, AICM DSP

#### C01.5 · ¿Estamos adoptando IA a la velocidad correcta, o el miedo al riesgo nos está dejando atrás?

- **Quién pregunta:** Directorio · **Cuándo:** Estrategia anual y presión competitiva · **Tema:** IA y agentes
- **Qué quiere saber realmente:** Quiere saber si seguridad equilibra valor y riesgo, y si el apetito de IA guía decisiones concretas.
- **Una respuesta sólida incluye:** Portafolio de casos con valor y riesgo, tiempo de aprobación por el camino seguro del COE, casos detenidos y por qué, patrones preaprobados disponibles y el apetito específico de IA que orienta esas decisiones.
- **Señal de alerta:** Respuesta solo defensiva («lo bloqueamos todo») o solo entusiasta (sin límites ni criterios).
- **Cómo prepararse (marco 99 + 99, versión 2.0):** B01.1 (¿Qué resultados de negocio esperamos de la IA y de los agentes, y qué…) · B01.2 (¿Cuál es nuestro apetito de riesgo específico para la IA, por caso de…) · B01.3 (¿Qué portafolio de casos de uso tenemos (comprar, extender, construir)…) · B02.8 (¿Tenemos un centro de excelencia de IA segura que entregue patrones, e…) · B01.7 (¿Cómo evitamos que la presión por adoptar IA rápido debilite los funda…)
- **Apoyo de Microsoft:** Copilot controls; entornos administrados de Power Platform y Copilot Studio; evaluaciones y red teaming en Microsoft Foundry.
- **Marcos (heredados):** NIST — AI RMF MAP 1, AI RMF MAP 3, CSF GV.RM | CIS — CIS RAM, CIS IG1 | The Open Group — TOGAF, G268, Open FAIR | ISACA — COBIT APO04, AAISM D1, COBIT APO12 | CSA — AICM GRC, AICM STA

#### C01.6 · Si mañana sufrimos un ataque grave, ¿qué decisiones tendremos que tomar nosotros y estamos preparados para tomarlas?

- **Quién pregunta:** Directorio · **Cuándo:** Tras un incidente en el sector
- **Qué quiere saber realmente:** Quiere conocer su propio rol en una crisis antes de que ocurra.
- **Una respuesta sólida incluye:** Decisiones reservadas al directorio (divulgación de un incidente material, pago o no de un rescate, comunicación pública, suspensión de operaciones), criterios acordados de antemano, quién convoca y en cuánto tiempo, y fecha del último ejercicio con el directorio.
- **Señal de alerta:** El directorio nunca participó de un ejercicio; los criterios se definirían durante la crisis.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** A09.5 (¿Cómo se gestiona una crisis cibernética: comité, roles, decisiones di…) · A09.6 (¿Cuándo fue el último ejercicio de crisis con el comité ejecutivo y qu…) · A08.4 (¿Tenemos un plan de respuesta a incidentes vigente y ensayado con la d…) · A01.3 (¿Qué decisiones de riesgo puede tomar el CISO por sí mismo, cuáles cor…)
- **Apoyo de Microsoft:** Interrupción automática de ataques en Defender XDR para ganar tiempo de decisión; guía de respuesta del CISO Workshop.
- **Marcos (heredados):** NIST — CSF RS.MA, CSF RS.CO, CSF RC.CO | CIS — CIS 17, CIS RAM | The Open Group — TOGAF, Open FAIR | ISACA — COBIT DSS04, COBIT DSS02, COBIT EDM03 | CSA — CCM SEF, CCM BCR, CCM GRC

#### C01.7 · ¿Qué nos tiene que decir que no nos gustaría escuchar?

- **Quién pregunta:** Directorio (sesión sin la gerencia) · **Cuándo:** Sesión ejecutiva del directorio
- **Qué quiere saber realmente:** Pone a prueba la transparencia del CISO y la cultura de escalamiento de la organización.
- **Una respuesta sólida incluye:** Riesgos aceptados de hecho sin aprobación, excepciones vencidas, dependencias de una persona o de un proveedor, brechas de presupuesto o de talento, y el impacto concreto de no resolverlos.
- **Señal de alerta:** «Todo está bajo control»; varias sesiones seguidas sin malas noticias.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** A02.5 (¿Cada aceptación de riesgo tiene dueño, alcance, evidencia, vencimient…) · A10.5 (¿Cómo gestionamos las excepciones a las políticas: quién las aprueba,…) · A11.7 (¿Qué capacidades críticas dependen de una sola persona o de un único p…) · A01.2 (¿A quién reporta el CISO, qué independencia real tiene respecto de TI,…)
- **Apoyo de Microsoft:** Sin capacidad específica: es una cuestión de independencia y gobierno.
- **Marcos (heredados):** NIST — CSF GV.RM, CSF GV.RR, CSF ID.RA | CIS — CIS RAM, CIS 5, CIS 6 | The Open Group — TOGAF, Open FAIR, Roles de seguridad | ISACA — COBIT APO12, COBIT APO01, COBIT APO10 | CSA — CCM GRC, CCM HRS, CCM IAM

#### C01.8 · ¿Cómo se compara nuestra postura con la de nuestros pares y con lo que exigen los reguladores?

- **Quién pregunta:** Directorio · **Cuándo:** Planificación anual
- **Qué quiere saber realmente:** Busca una referencia externa para calibrar si el esfuerzo es suficiente.
- **Una respuesta sólida incluye:** Perfil actual y objetivo según NIST CSF 2.0, requisitos regulatorios aplicables y su grado de cumplimiento, y referencias sectoriales disponibles, sin convertir la comparación en el objetivo.
- **Señal de alerta:** Rankings sin metodología o «estamos mejor que el promedio» sin datos.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** A10.9 (¿Qué nivel de madurez queremos alcanzar por dominio y cómo medimos la…) · A10.1 (¿Qué obligaciones legales, regulatorias y contractuales de seguridad n…)
- **Apoyo de Microsoft:** Purview Compliance Manager (plantillas de DORA, NIS2 y marcos de IA); Secure Score (comparación con organizaciones similares).
- **Marcos (heredados):** NIST — CSF ID.IM, CSF GV.OC, CSF GV.SC | CIS — CIS IG1 | The Open Group — TOGAF | ISACA — COBIT MEA01, COBIT MEA03 | CSA — STAR, CCM GRC, CCM A&A

#### C01.9 · ¿Tenemos el CISO, el equipo y el presupuesto que este riesgo requiere?

- **Quién pregunta:** Directorio · **Cuándo:** Aprobación del presupuesto
- **Qué quiere saber realmente:** Quiere saber si los recursos son proporcionales a la exposición y si hay continuidad en el liderazgo.
- **Una respuesta sólida incluye:** Capacidades críticas cubiertas y descubiertas, dependencia de personas clave, plan de sucesión del CISO, presupuesto comparado con la exposición y efecto esperado de la IA en el equipo.
- **Señal de alerta:** Pedir más presupuesto sin vincularlo con reducción de exposición.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** A11.3 (¿Tenemos un plan de talento de seguridad (brechas de habilidades, suce…) · A11.7 (¿Qué capacidades críticas dependen de una sola persona o de un único p…) · A01.7 (¿Cómo justificamos el presupuesto de seguridad por reducción de exposi…) · B11.8 (¿Qué roles del equipo de seguridad cambian con la IA agéntica y cuál e…) · A01.9 (Antes de reducir la dotación o el presupuesto de seguridad, ¿se evalúa…) — nueva en la v2.0
- **Apoyo de Microsoft:** Security Copilot incluido en Microsoft 365 E5 y E7 como capacidad adicional del SOC.
- **Marcos (heredados):** NIST — CSF GV.RR, CSF PR.AT, CSF GV.RM | CIS — CIS 14, CIS 5, CIS 6 | The Open Group — Roles de seguridad, TOGAF, Open FAIR | ISACA — COBIT APO07, COBIT APO06, COBIT EDM04 | CSA — CCM HRS, CCM GRC, CCM IAM

### C02 · Comité de auditoría y riesgos

El comité busca aseguramiento: que los controles estén diseñados, implementados y funcionen, y que la información que llega al directorio sea confiable.

#### C02.1 · ¿Qué controles clave tenemos y qué evidencia independiente demuestra que funcionan, no solo que existen?

- **Quién pregunta:** Presidente del comité de auditoría · **Cuándo:** Plan anual de auditoría
- **Qué quiere saber realmente:** Distingue entre diseño, implementación y eficacia operativa.
- **Una respuesta sólida incluye:** Catálogo de controles clave con su nivel de evidencia (diseño, implementación, eficacia), última prueba, resultado y quién la hizo (primera, segunda o tercera línea).
- **Señal de alerta:** Evidencia limitada a políticas y capturas de pantalla.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** A10.2 (¿Cómo convertimos varios marcos y regulaciones en un único conjunto de…) · A10.3 (¿Cuánta de nuestra evidencia de cumplimiento es automática y continua,…) · A10.4 (¿Cómo se coordinan las líneas de aseguramiento (operación, riesgo, aud…) · B08.5 (¿Qué evidencia de aseguramiento continuo tenemos sobre nuestros contro…) · A10.6 (¿Qué versiones de los marcos de referencia usamos (COBIT, NIST, ISO, C…) — nueva en la v2.0
- **Apoyo de Microsoft:** Purview Compliance Manager (evaluaciones y acciones de mejora); Purview Audit.
- **Marcos (heredados):** NIST — CSF GV.OV, CSF ID.IM, SP 800-53 | CIS — CIS 8 | The Open Group — TOGAF, Open FAIR | ISACA — COBIT MEA02, COBIT MEA04, COBIT MEA03 | CSA — CCM A&A, CCM SEF, AICM A&A

#### C02.2 · ¿Qué excepciones y aceptaciones de riesgo están vigentes, cuáles vencieron y quién las aprobó?

- **Quién pregunta:** Comité de auditoría y riesgos · **Cuándo:** Sesión trimestral del comité
- **Qué quiere saber realmente:** Quiere saber si el riesgo residual se acepta con autoridad y si las excepciones se vuelven permanentes.
- **Una respuesta sólida incluye:** Registro de excepciones con dueño, alcance, controles compensatorios, autoridad que aprobó y vencimiento; vencidas con plan de cierre; tendencia trimestral.
- **Señal de alerta:** Excepciones sin fecha de vencimiento o aprobadas por quien no tiene facultades.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** A10.5 (¿Cómo gestionamos las excepciones a las políticas: quién las aprueba,…) · A02.5 (¿Cada aceptación de riesgo tiene dueño, alcance, evidencia, vencimient…) · A02.8 (¿Nuestro análisis de riesgo considera el daño que podemos causar a ter…) — nueva en la v2.0
- **Apoyo de Microsoft:** Sin capacidad específica: es un registro de gobierno (CDRR en el AI CISO Atlas).
- **Marcos (heredados):** NIST — CSF GV.RM, CSF ID.RA, CSF GV.PO | CIS — CIS RAM | The Open Group — Open FAIR, TOGAF | ISACA — COBIT APO12, COBIT APO01, COBIT APO10 | CSA — CCM GRC, CCM DSP

#### C02.3 · ¿Qué hallazgos de auditoría y de pruebas de seguridad siguen abiertos, y por qué?

- **Quién pregunta:** Comité de auditoría y riesgos · **Cuándo:** Sesión trimestral del comité
- **Qué quiere saber realmente:** Quiere ver la disciplina de cierre y las causas de los atrasos.
- **Una respuesta sólida incluye:** Hallazgos por severidad, antigüedad, dueño y fecha comprometida; reincidencias; causas raíz; recursos necesarios para cerrarlos.
- **Señal de alerta:** Hallazgos que se «cierran» con planes en lugar de evidencia, o que se reabren.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** A06.9 (¿Hacemos pruebas ofensivas (pruebas de penetración, red team, purple t…) · A09.9 (¿Convertimos los incidentes, cuasi incidentes y ejercicios en cambios…) · A10.9 (¿Qué nivel de madurez queremos alcanzar por dominio y cómo medimos la…)
- **Apoyo de Microsoft:** Exposure Management (iniciativas y seguimiento de la remediación).
- **Marcos (heredados):** NIST — CSF ID.IM, CSF ID.RA, CSF RC.RP | CIS — CIS 18, CIS 17, CIS IG1 | The Open Group — TOGAF | ISACA — COBIT MEA02, COBIT DSS05, COBIT DSS03 | CSA — CCM TVM, CCM A&A, CCM SEF

#### C02.4 · ¿Cómo sabemos que los indicadores que nos presenta el CISO son confiables?

- **Quién pregunta:** Comité de auditoría y riesgos · **Cuándo:** Revisión anual de indicadores
- **Qué quiere saber realmente:** Pone a prueba la integridad de la información de gestión.
- **Una respuesta sólida incluye:** Origen de cada indicador, método de cálculo, frecuencia, grado de automatización, revisión independiente y limitaciones conocidas.
- **Señal de alerta:** Indicadores calculados a mano sin trazabilidad, o cambios de método sin aviso.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** A06.8 (¿Cómo medimos y comunicamos la postura (puntuación de seguridad, expos…) · A10.3 (¿Cuánta de nuestra evidencia de cumplimiento es automática y continua,…) · A02.6 (¿Qué indicadores anticipan una pérdida material y cuáles se reportan a…) · A10.7 (¿Quién valida de forma independiente el modelo con el que cuantificamo…) — nueva en la v2.0
- **Apoyo de Microsoft:** Secure Score y Exposure Management como fuentes automatizadas; lago de datos de Microsoft Sentinel para conservar el histórico.
- **Marcos (heredados):** NIST — CSF GV.OV, CSF ID.IM, CSF RS.CO | CIS — CIS 7, CIS 4, CIS 8 | The Open Group — Open FAIR | ISACA — COBIT MEA01, COBIT MEA04, COBIT APO12 | CSA — CCM GRC, CCM A&A, CCM TVM

#### C02.5 · ¿Qué controles específicos tenemos sobre la IA y los agentes, y quién los audita?

- **Quién pregunta:** Comité de auditoría y riesgos · **Cuándo:** Plan anual de auditoría · **Tema:** IA y agentes
- **Qué quiere saber realmente:** Quiere saber si la IA tiene controles propios o se supone cubierta por los controles generales de TI.
- **Una respuesta sólida incluye:** Controles mínimos por nivel de riesgo de IA, evidencia (evaluaciones, red teaming, registros de actividad de agentes, revisiones de permisos), responsable del aseguramiento independiente y marcos de referencia (NIST AI RMF, ISO/IEC 42001, AICM de CSA).
- **Señal de alerta:** «Los controles generales de TI cubren la IA».
- **Cómo prepararse (marco 99 + 99, versión 2.0):** B02.7 (¿Cómo clasificamos los sistemas de IA por nivel de riesgo y qué contro…) · B08.1 (¿Qué evaluaciones (calidad, fundamentación, seguridad, sesgo, cumplimi…) · B08.5 (¿Qué evidencia de aseguramiento continuo tenemos sobre nuestros contro…) · B10.9 (¿Cómo alineamos nuestro marco de IA con NIST AI RMF, ISO/IEC 42001, la…) · B08.7 (¿Qué controles de IA damos por eficaces sin garantías demostradas, y c…) — nueva en la v2.0
- **Apoyo de Microsoft:** Purview Audit (actividad de Copilot y agentes); Compliance Manager (marcos de IA); evaluadores de agentes en Microsoft Foundry.
- **Marcos (heredados):** NIST — AI 600-1, AI RMF GOVERN 1, AI RMF MEASURE 2 | CIS — guía CIS para LLM, CIS 16, guía CIS para agentes de IA | The Open Group — TOGAF, Open FAIR | ISACA — AAISM D3, AI Audit Toolkit, COBIT MEA02 | CSA — MAESTRO, AICM MDS, AICM A&A

#### C02.6 · ¿Qué tenemos que divulgar sobre ciberseguridad y cómo se decide si un incidente es material?

- **Quién pregunta:** Comité de auditoría y riesgos · **Cuándo:** Cierre de estados financieros y tras un incidente
- **Qué quiere saber realmente:** Quiere criterios definidos antes del incidente y coherencia con la información financiera y de mercado.
- **Una respuesta sólida incluye:** Criterios de materialidad documentados, órgano que decide, plazos regulatorios por jurisdicción, coordinación con Legal y Finanzas, y ensayos del proceso.
- **Señal de alerta:** Criterios inexistentes o que se definirían durante el incidente.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** A09.5 (¿Cómo se gestiona una crisis cibernética: comité, roles, decisiones di…) · A10.1 (¿Qué obligaciones legales, regulatorias y contractuales de seguridad n…) · A08.9 (¿Hemos definido cómo interactuamos con los CERT nacionales, reguladore…) · B09.7 (¿Qué umbral convierte un comportamiento anómalo de la IA en un inciden…)
- **Apoyo de Microsoft:** Sin capacidad específica: es un proceso de gobierno y legal.
- **Marcos (heredados):** NIST — CSF RS.CO, CSF RS.MA, CSF GV.OC | CIS — CIS 17 | The Open Group — TOGAF | ISACA — COBIT DSS02, COBIT MEA03, COBIT DSS04 | CSA — CCM SEF, CCM BCR, CCM GRC

#### C02.7 · ¿Qué dependemos de terceros y cómo obtenemos aseguramiento sobre ellos?

- **Quién pregunta:** Comité de auditoría y riesgos · **Cuándo:** Ciclo anual de terceros
- **Qué quiere saber realmente:** Quiere saber si el riesgo de terceros se verifica o solo se declara.
- **Una respuesta sólida incluye:** Terceros críticos, informes de aseguramiento (SOC 2, ISO/IEC 27001, CSA STAR), derechos de auditoría, cobertura de los proveedores de nuestros proveedores, hallazgos y planes.
- **Señal de alerta:** Cuestionarios autodeclarados como única evidencia.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** A07.5 (¿Cómo evaluamos, contratamos y monitoreamos a los terceros críticos, i…) · A07.6 (¿Qué exigimos contractualmente a los proveedores (notificación de inci…) · A10.8 (¿Cómo verificamos el cumplimiento de nuestros proveedores cloud y qué…) · B10.3 (¿Cómo evaluamos a los proveedores de modelos, plataformas y agentes de…)
- **Apoyo de Microsoft:** Service Trust Portal (informes de auditoría de los servicios de Microsoft); programa CSA STAR.
- **Marcos (heredados):** NIST — CSF GV.SC, SP 800-161, AI RMF GOVERN 6 | CIS — CIS 15 | The Open Group — sin correspondencia directa | ISACA — COBIT APO10, COBIT APO09, COBIT MEA04 | CSA — CCM STA, STAR, CAIQ

#### C02.8 · ¿Qué cambió en el riesgo desde la última sesión que deberíamos saber?

- **Quién pregunta:** Comité de auditoría y riesgos · **Cuándo:** Cada sesión del comité
- **Qué quiere saber realmente:** Quiere un informe vivo, no una repetición del anterior.
- **Una respuesta sólida incluye:** Cambios en amenazas, en el negocio (adquisiciones, nuevos productos, IA), en la regulación y en la postura; incidentes y cuasi incidentes; decisiones necesarias.
- **Señal de alerta:** Informe idéntico al de la sesión anterior.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** A02.2 (¿Cuáles son nuestras joyas de la corona (procesos, datos, sistemas e i…) · A02.4 (¿Cómo se integra el riesgo cibernético al registro de riesgos empresar…) · B01.9 (¿Cómo ajustamos estrategia, políticas y controles al ritmo de cambio d…)
- **Apoyo de Microsoft:** Threat Intelligence Briefing Agent (Security Copilot); Microsoft Digital Defense Report 2026.
- **Marcos (heredados):** NIST — CSF ID.AM, CSF ID.RA, CSF GV.RM | CIS — CIS 1, CIS 3, CIS RAM | The Open Group — TOGAF, Open FAIR | ISACA — COBIT APO12, COBIT BAI09, COBIT EDM03 | CSA — CCM GRC, CCM DSP, CCM TVM

#### C02.9 · Si un regulador o un tribunal lo pide, ¿podemos explicar y reconstruir una decisión tomada o asistida por la IA?

- **Quién pregunta:** Comité de auditoría y riesgos · **Cuándo:** Tras un reclamo o un requerimiento · **Tema:** IA y agentes
- **Qué quiere saber realmente:** Quiere saber si la IA deja rastro suficiente para rendir cuentas.
- **Una respuesta sólida incluye:** Registros de prompts, respuestas, acciones e identidades de agentes; retención definida; cadena de custodia; capacidad de explicación por caso de uso y pruebas realizadas.
- **Señal de alerta:** Registros incompletos o no correlacionables, o retención no definida.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** B05.5 (¿Retenemos, auditamos y podemos buscar los prompts, respuestas y accio…) · B08.9 (¿Cómo explicamos y justificamos una decisión apoyada por IA cuando un…) · B09.1 (¿Registramos de forma correlacionable quién pidió qué, qué hizo el age…) · B09.4 (¿Podemos reconstruir de forma forense una cadena de acciones de varios…)
- **Apoyo de Microsoft:** Purview Audit; retención y eDiscovery de interacciones de IA en Purview.
- **Marcos (heredados):** NIST — CSF DE.CM, CSF RS.AN, AI RMF MANAGE 4 | CIS — CIS 8, guía CIS para agentes de IA | The Open Group — sin correspondencia directa | ISACA — COBIT MEA03, COBIT APO14, COBIT APO11 | CSA — AICM LOG, AICM SEF, AICM GRC

### C03 · CEO y comité ejecutivo

El CEO pregunta por el negocio: qué protege la seguridad, cuánto frena o habilita, qué riesgo no se está tratando y si la organización resistiría una crisis.

#### C03.1 · ¿Qué necesita de mí para que la seguridad funcione?

- **Quién pregunta:** CEO · **Cuándo:** Reunión individual
- **Qué quiere saber realmente:** Ofrece patrocinio; espera pedidos concretos y acotados.
- **Una respuesta sólida incluye:** Dos o tres decisiones o apoyos precisos (aprobar el apetito de IA, exigir MFA resistente al phishing al comité ejecutivo, incluir objetivos de seguridad en las metas, respaldar el retiro de sistemas heredados), con el riesgo de no hacerlo.
- **Señal de alerta:** Pedidos genéricos («más apoyo», «más presupuesto»).
- **Cómo prepararse (marco 99 + 99, versión 2.0):** A01.8 (¿Cómo rinde cuentas la alta dirección por los objetivos de seguridad (…) · A01.6 (¿Cómo se integra la seguridad en las decisiones de inversión, compras…) · A03.5 (¿Cómo gestionamos la deuda técnica y los sistemas heredados que no pue…) · A01.1 (¿Qué resultados de negocio protege el programa de seguridad y dónde es…)
- **Apoyo de Microsoft:** CISO Workshop de Microsoft (alineación con la dirección).
- **Marcos (heredados):** NIST — CSF GV.RM, CSF GV.RR, CSF GV.OV | CIS — CIS 15, CIS 16, CIS 2 | The Open Group — TOGAF, O-ESA, G152 | ISACA — COBIT EDM01, COBIT APO07, COBIT APO05 | CSA — CCM GRC, CCM HRS, CCM STA

#### C03.2 · ¿En cuánto tiempo podríamos volver a operar si un ransomware cifra todo mañana?

- **Quién pregunta:** CEO · **Cuándo:** Tras un incidente en el sector
- **Qué quiere saber realmente:** Quiere un tiempo de recuperación probado, no teórico.
- **Una respuesta sólida incluye:** Tiempos de recuperación probados por servicio crítico (identidad, datos, aplicaciones), último ensayo de punta a punta, brechas y operación manual alternativa.
- **Señal de alerta:** Tiempos teóricos de proveedores, sin ensayo con datos reales.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** A09.2 (¿Podemos recuperar identidad, datos y servicios críticos tras un ranso…) · A09.3 (¿Nuestras copias de seguridad son inmutables, aisladas, cifradas y est…) · A09.4 (¿Tenemos un plan para recuperar el proveedor de identidad y operar si…) · A09.8 (¿Podemos operar los procesos críticos con mecanismos manuales o altern…)
- **Apoyo de Microsoft:** Interrupción automática de ataques (Defender XDR); Quick Machine Recovery en Windows.
- **Marcos (heredados):** NIST — CSF RC.RP, CSF PR.IR, CSF PR.DS | CIS — CIS 11, CIS 5 | The Open Group — TOGAF | ISACA — COBIT DSS04, COBIT DSS05, COBIT DSS06 | CSA — CCM BCR, CCM CEK, CCM IAM

#### C03.3 · Nuestros competidores ya usan agentes. ¿Por qué nosotros tardamos?

- **Quién pregunta:** CEO · **Cuándo:** Comité ejecutivo · **Tema:** IA y agentes
- **Qué quiere saber realmente:** Quiere saber si seguridad es un freno o un habilitador, y qué falta para avanzar.
- **Una respuesta sólida incluye:** Estado del portafolio; fundamentos pendientes (sobreexposición de datos, identidad de agentes, inventario); plan con fechas para habilitar casos seguros; casos ya habilitados.
- **Señal de alerta:** Culpar a seguridad sin plan, o ceder sin controles mínimos.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** B01.7 (¿Cómo evitamos que la presión por adoptar IA rápido debilite los funda…) · B05.1 (¿Corregimos la sobreexposición de datos (permisos excesivos, sitios ab…) · B02.8 (¿Tenemos un centro de excelencia de IA segura que entregue patrones, e…) · B04.1 (¿Cada agente tiene una identidad propia, distinguible de la de persona…)
- **Apoyo de Microsoft:** SharePoint Advanced Management; Purview DSPM; Microsoft Agent 365.
- **Marcos (heredados):** NIST — AI RMF GOVERN 1, CSF PR.AA, CSF GV.RM | CIS — CIS IG1, CIS 3, CIS 5 | The Open Group — TOGAF, Zero Trust Commandments | ISACA — COBIT DSS05, AAISM D3, COBIT APO13 | CSA — AICM GRC, AICM DSP, AICM IAM

#### C03.4 · ¿Cuál es el riesgo más grande que hoy no estamos tratando?

- **Quién pregunta:** CEO · **Cuándo:** Reunión individual
- **Qué quiere saber realmente:** Pone a prueba la priorización y la honestidad del CISO.
- **Una respuesta sólida incluye:** El riesgo, por qué no se trata (costo, prioridad, dependencia), impacto estimado, opción mínima viable y decisión que se pide.
- **Señal de alerta:** No saber responder, o enumerar diez riesgos.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** A02.2 (¿Cuáles son nuestras joyas de la corona (procesos, datos, sistemas e i…) · A02.5 (¿Cada aceptación de riesgo tiene dueño, alcance, evidencia, vencimient…) · A03.9 (¿Tenemos una hoja de ruta de seguridad a 12–36 meses priorizada por ri…)
- **Apoyo de Microsoft:** Exposure Management (rutas de ataque y activos críticos).
- **Marcos (heredados):** NIST — CSF ID.RA, CSF ID.AM, CSF GV.RM | CIS — CIS 1, CIS 3, CIS RAM | The Open Group — TOGAF, Open FAIR | ISACA — COBIT APO12, COBIT BAI09, COBIT APO10 | CSA — CCM GRC, CCM DSP, CCM TVM

#### C03.5 · Si nos atacan, ¿quién habla con la prensa, los clientes y los empleados, y qué decimos?

- **Quién pregunta:** CEO y comité ejecutivo · **Cuándo:** Tras un incidente en el sector
- **Qué quiere saber realmente:** Quiere un plan de comunicación de crisis que no dependa de la improvisación.
- **Una respuesta sólida incluye:** Plan de comunicación de crisis con vocero, mensajes base, umbrales de activación, coordinación con Legal y reguladores, y ensayo reciente.
- **Señal de alerta:** Comunicación solo desde TI o mensajes improvisados.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** A09.5 (¿Cómo se gestiona una crisis cibernética: comité, roles, decisiones di…) · A11.6 (¿Cómo comunicamos el riesgo cibernético en lenguaje de negocio a cada…) · A08.4 (¿Tenemos un plan de respuesta a incidentes vigente y ensayado con la d…)
- **Apoyo de Microsoft:** Sin capacidad específica: es un proceso de gestión de crisis.
- **Marcos (heredados):** NIST — CSF RS.MA, CSF RS.CO, CSF RC.CO | CIS — CIS 17 | The Open Group — Open FAIR | ISACA — COBIT DSS02, COBIT DSS04, COBIT EDM03 | CSA — CCM SEF, CCM BCR, CCM GRC

#### C03.6 · ¿Cómo evitamos que un deepfake del CEO o del CFO nos haga transferir dinero?

- **Quién pregunta:** Comité ejecutivo · **Cuándo:** Tras un fraude en el sector · **Tema:** IA y agentes
- **Qué quiere saber realmente:** Quiere controles de proceso, no solo concientización.
- **Una respuesta sólida incluye:** Verificación fuera de banda para transacciones e instrucciones sensibles, límites y doble aprobación, formación de áreas de alto riesgo, simulaciones con suplantación y procedimientos de la mesa de ayuda.
- **Señal de alerta:** Confiar solo en la capacitación.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** A11.2 (¿Cómo preparamos a ejecutivos y áreas de alto riesgo (finanzas, tesore…) · A04.8 (¿Cómo verificamos la identidad de las personas en procesos críticos (a…) · B06.8 (¿Cómo nos defendemos de atacantes que usan IA (phishing personalizado,…)
- **Apoyo de Microsoft:** Microsoft Entra Verified ID con Face Check para verificar identidad en procesos críticos.
- **Marcos (heredados):** NIST — CSF PR.AT, CSF PR.AA, CSF ID.RA | CIS — CIS 14, CIS 5, CIS 9 | The Open Group — Open FAIR | ISACA — COBIT APO07, COBIT DSS05, COBIT DSS06 | CSA — CCM HRS, CCM IAM, AICM TVM

#### C03.7 · ¿La seguridad nos está frenando? ¿Dónde y cuánto?

- **Quién pregunta:** CEO · **Cuándo:** Revisión de desempeño de la función
- **Qué quiere saber realmente:** Quiere medir la fricción y ver qué hace seguridad para reducirla.
- **Una respuesta sólida incluye:** Tiempos de aprobación de proyectos, proveedores y casos de IA; cuellos de botella medidos; cambios hechos para acelerar (patrones preaprobados, autoservicio seguro); quejas y su resolución.
- **Señal de alerta:** No medir la fricción o considerar que frenar es el rol de seguridad.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** A01.6 (¿Cómo se integra la seguridad en las decisiones de inversión, compras…) · B02.8 (¿Tenemos un centro de excelencia de IA segura que entregue patrones, e…) · A11.5 (¿La seguridad forma parte de la cultura de ingeniería y producto (refe…)
- **Apoyo de Microsoft:** Entornos administrados de Power Platform y Copilot Studio para habilitar autoservicio con controles.
- **Marcos (heredados):** NIST — CSF GV.RM, CSF GV.SC, AI RMF GOVERN 4 | CIS — CIS 16, CIS 15, CIS 14 | The Open Group — TOGAF, G152 | ISACA — COBIT APO05, COBIT BAI01, COBIT BAI02 | CSA — CCM GRC, CCM STA, AICM GRC

#### C03.8 · ¿Qué tenemos que hacer cada uno de nosotros, personalmente?

- **Quién pregunta:** Comité ejecutivo · **Cuándo:** Comité ejecutivo
- **Qué quiere saber realmente:** Los ejecutivos son objetivos prioritarios; quieren conductas concretas.
- **Una respuesta sólida incluye:** Tres a cinco conductas por ejecutivo (MFA resistente al phishing, dispositivos administrados, verificación de pedidos inusuales, protección de sus asistentes, participación en ejercicios) y cómo se medirán.
- **Señal de alerta:** Excepciones para ejecutivos.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** A11.2 (¿Cómo preparamos a ejecutivos y áreas de alto riesgo (finanzas, tesore…) · A04.1 (¿Qué porcentaje de usuarios, administradores y accesos externos usa au…) · A01.8 (¿Cómo rinde cuentas la alta dirección por los objetivos de seguridad (…)
- **Apoyo de Microsoft:** Microsoft Entra (MFA resistente al phishing y acceso condicional).
- **Marcos (heredados):** NIST — CSF PR.AA, CSF PR.AT, CSF GV.RR | CIS — CIS 14, CIS 6 | The Open Group — Zero Trust Commandments, O-ESA | ISACA — COBIT APO07, COBIT DSS06, COBIT DSS05 | CSA — CCM HRS, CCM IAM, CCM GRC

#### C03.9 · Si un agente de IA comete un error grave con un cliente, ¿quién responde y qué hacemos?

- **Quién pregunta:** CEO · **Cuándo:** Lanzamiento de un agente orientado a clientes · **Tema:** IA y agentes
- **Qué quiere saber realmente:** Quiere saber si la responsabilidad por los agentes está asignada antes del error.
- **Una respuesta sólida incluye:** Dueño de negocio del agente, nivel de autonomía, límites y cortacircuitos, capacidad de suspender y revertir, playbook de incidente de IA y comunicación al cliente.
- **Señal de alerta:** «Es culpa del proveedor del modelo».
- **Cómo prepararse (marco 99 + 99, versión 2.0):** B02.6 (¿Cada agente y aplicación de IA tiene dueño de negocio, patrocinador,…) · B07.5 (¿Podemos suspender, aislar o revocar un agente, o todos los de una cla…) · B07.7 (¿Podemos revertir los efectos de una acción autónoma (deshacer, compen…) · B09.3 (¿Tenemos playbooks de respuesta para incidentes de IA (fuga por prompt…)
- **Apoyo de Microsoft:** Agent 365 (deshabilitar o bloquear agentes); Entra Agent ID; aprobaciones humanas en flujos de Copilot Studio.
- **Marcos (heredados):** NIST — AI RMF MANAGE 2, AI RMF MANAGE 4, AI RMF GOVERN 2 | CIS — guía CIS para agentes de IA, CIS 17, CIS 5 | The Open Group — sin correspondencia directa | ISACA — COBIT DSS02, AAISM D3, COBIT APO01 | CSA — AICM IAM, AICM SEF, AICM GRC

### C04 · CFO, finanzas y tesorería

El CFO traduce la seguridad a números: pérdidas esperadas, retorno de la inversión, transferencia de riesgo, fraude y control del gasto, incluido el de la IA.

#### C04.1 · ¿Cuánto podríamos perder en un incidente grave y con qué probabilidad?

- **Quién pregunta:** CFO · **Cuándo:** Planificación financiera anual
- **Qué quiere saber realmente:** Quiere rangos cuantificados y comparables con otras decisiones financieras.
- **Una respuesta sólida incluye:** Escenarios cuantificados en rangos (frecuencia y magnitud de pérdida) con supuestos explícitos, método (por ejemplo, Open FAIR), sensibilidad y cómo cambian con las inversiones propuestas.
- **Señal de alerta:** Un número único sin supuestos, o matrices de colores.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** A02.3 (¿Cuantificamos el riesgo con rangos y supuestos explícitos, o con matr…) · A02.2 (¿Cuáles son nuestras joyas de la corona (procesos, datos, sistemas e i…)
- **Apoyo de Microsoft:** Exposure Management aporta datos de exposición como insumo; la cuantificación es del cliente.
- **Marcos (heredados):** NIST — CSF ID.RA, CSF GV.RM, IR 8286 | CIS — CIS RAM, CIS 1, CIS 3 | The Open Group — Open FAIR, TOGAF | ISACA — COBIT APO12, Risk IT, COBIT BAI09 | CSA — CCM GRC, CCM DSP, CCM TVM

#### C04.2 · ¿Qué retorno tuvo el presupuesto de seguridad que aprobamos el año pasado?

- **Quién pregunta:** CFO · **Cuándo:** Ciclo presupuestario
- **Qué quiere saber realmente:** Quiere ver resultados, no gasto ejecutado.
- **Una respuesta sólida incluye:** Exposición reducida (indicadores con tendencia), pérdidas evitadas estimadas, eficiencias (consolidación, automatización), negocio habilitado, y lo que no rindió y se retira.
- **Señal de alerta:** Presentar solo el gasto ejecutado o las herramientas compradas.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** A02.7 (¿Cómo demostramos el valor de la seguridad: pérdidas evitadas, exposic…) · A01.7 (¿Cómo justificamos el presupuesto de seguridad por reducción de exposi…) · A01.9 (Antes de reducir la dotación o el presupuesto de seguridad, ¿se evalúa…) — nueva en la v2.0 · A02.9 (¿Qué precisión necesita cada decisión de riesgo, y estamos invirtiendo…) — nueva en la v2.0
- **Apoyo de Microsoft:** Secure Score y Exposure Management para mostrar la reducción de exposición.
- **Marcos (heredados):** NIST — CSF GV.RM, CSF ID.IM, CSF GV.OV | CIS — sin correspondencia directa | The Open Group — Open FAIR, TOGAF | ISACA — COBIT APO06, COBIT EDM04, COBIT EDM02 | CSA — CCM GRC, CCM HRS

#### C04.3 · ¿Podemos consolidar herramientas y proveedores de seguridad sin aumentar el riesgo?

- **Quién pregunta:** CFO · **Cuándo:** Ciclo presupuestario
- **Qué quiere saber realmente:** Busca eficiencia; necesita saber dónde hay superposición y qué riesgo implica cambiar.
- **Una respuesta sólida incluye:** Mapa de capacidades superpuestas, costo total, plan de consolidación por fases con criterios de riesgo, ahorro estimado e impacto en integración y operación.
- **Señal de alerta:** Consolidar solo por precio, o rechazar sin análisis.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** A03.7 (¿Cuánto valor perdemos por la fragmentación de herramientas y datos de…) · A01.7 (¿Cómo justificamos el presupuesto de seguridad por reducción de exposi…)
- **Apoyo de Microsoft:** Plataforma integrada de Microsoft Defender XDR y Microsoft Sentinel; capacidades incluidas en Microsoft 365 E5 y E7.
- **Marcos (heredados):** NIST — CSF GV.RM, CSF ID.IM, CSF DE.CM | CIS — CIS 8 | The Open Group — TOGAF | ISACA — COBIT APO03, COBIT BAI03, COBIT APO06 | CSA — CCM LOG, CCM GRC

#### C04.4 · ¿Estamos protegidos contra el fraude de pagos y la suplantación de proveedores?

- **Quién pregunta:** Tesorería · **Cuándo:** Tras un intento de fraude
- **Qué quiere saber realmente:** Quiere controles de proceso y tecnológicos sobre el flujo de pagos.
- **Una respuesta sólida incluye:** Controles sobre cambios de datos bancarios, verificación fuera de banda, segregación de funciones, monitoreo, simulaciones e incidentes del año.
- **Señal de alerta:** Depender solo del criterio del empleado.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** A06.6 (¿Cómo gestionamos el correo y la navegación como vectores principales…) · A11.2 (¿Cómo preparamos a ejecutivos y áreas de alto riesgo (finanzas, tesore…) · A04.8 (¿Cómo verificamos la identidad de las personas en procesos críticos (a…)
- **Apoyo de Microsoft:** Microsoft Defender for Office 365 (protección contra suplantación y fraude por correo).
- **Marcos (heredados):** NIST — CSF PR.AT, CSF PR.AA, CSF PR.PS | CIS — CIS 14, CIS 9, CIS 5 | The Open Group — sin correspondencia directa | ISACA — COBIT DSS05, COBIT APO07, COBIT DSS06 | CSA — CCM HRS, CCM TVM, CCM IAM

#### C04.5 · ¿Qué cubre realmente nuestro seguro cibernético y qué nos exige la aseguradora?

- **Quién pregunta:** CFO · **Cuándo:** Renovación de la póliza
- **Qué quiere saber realmente:** Quiere saber si la póliza respondería y si los controles declarados son demostrables.
- **Una respuesta sólida incluye:** Coberturas, exclusiones, sublímites, controles exigidos y evidencia de cumplimiento, brecha y costo de cerrarla.
- **Señal de alerta:** Declarar controles que no se pueden demostrar.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** A02.5 (¿Cada aceptación de riesgo tiene dueño, alcance, evidencia, vencimient…)
- **Apoyo de Microsoft:** Silencio: Microsoft no publica una postura específica sobre seguros; Secure Score y Compliance Manager pueden respaldar la evidencia.
- **Marcos (heredados):** NIST — CSF GV.RM, CSF ID.RA | CIS — CIS RAM | The Open Group — Open FAIR | ISACA — COBIT APO12, COBIT APO10 | CSA — CCM GRC

#### C04.6 · ¿Cuánto nos va a costar realmente la IA, incluida su seguridad?

- **Quién pregunta:** CFO · **Cuándo:** Ciclo presupuestario · **Tema:** IA y agentes
- **Qué quiere saber realmente:** Quiere el costo total, no solo las licencias.
- **Una respuesta sólida incluye:** Costo total (licencias, consumo, preparación de datos, controles, personas), costo de los controles mínimos por nivel de riesgo, consumo de la IA de seguridad y gobierno del gasto (límites y alertas).
- **Señal de alerta:** Ignorar el consumo variable o el costo de remediar la sobreexposición de datos.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** B01.5 (¿Cómo medimos el valor y el riesgo de la IA de forma conjunta (benefic…) · B11.7 (¿Cómo gestionamos el costo y la capacidad de la IA de seguridad (unida…) · B07.6 (¿Qué límites operativos (presupuesto, cantidad de llamadas, montos, fr…)
- **Apoyo de Microsoft:** Security Copilot incluido en E5 y E7 (400 SCU por mes por cada 1.000 licencias, hasta 10.000); licenciamiento de Agent 365; Microsoft 365 E7.
- **Marcos (heredados):** NIST — AI RMF MANAGE 2, AI RMF MAP 1, AI RMF MEASURE 1 | CIS — guía CIS para agentes de IA | The Open Group — sin correspondencia directa | ISACA — COBIT EDM02, COBIT MEA01, COBIT APO06 | CSA — AICM GRC, AICM IVS, MAESTRO

#### C04.7 · ¿Cuánto nos cuesta cumplir con tantas regulaciones y podemos reducirlo?

- **Quién pregunta:** CFO · **Cuándo:** Ciclo presupuestario
- **Qué quiere saber realmente:** Busca eficiencia en el cumplimiento.
- **Una respuesta sólida incluye:** Costo del cumplimiento por marco, duplicaciones, catálogo de controles comunes, automatización de la evidencia y ahorro estimado.
- **Señal de alerta:** Un equipo y un proceso distintos por regulación.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** A10.2 (¿Cómo convertimos varios marcos y regulaciones en un único conjunto de…) · A10.3 (¿Cuánta de nuestra evidencia de cumplimiento es automática y continua,…)
- **Apoyo de Microsoft:** Purview Compliance Manager (plantillas y evaluaciones reutilizables).
- **Marcos (heredados):** NIST — SP 800-53, CSF GV.OV, CSF ID.IM | CIS — CIS 8 | The Open Group — TOGAF | ISACA — COBIT MEA02, COBIT MEA03, COBIT MEA04 | CSA — CCM A&A, CCM SEF

#### C04.8 · ¿La IA para seguridad reemplaza personas o las potencia? ¿Cómo justificamos la inversión?

- **Quién pregunta:** CFO · **Cuándo:** Caso de negocio de la IA de seguridad · **Tema:** IA y agentes
- **Qué quiere saber realmente:** Quiere un caso de valor medido y realista.
- **Una respuesta sólida incluye:** Tareas automatizadas, tiempo ahorrado, calidad de las investigaciones, riesgos de dependencia y plan de reconversión, con indicadores medidos antes y después.
- **Señal de alerta:** Promesas de reducción de plantilla sin datos.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** B11.1 (¿Qué tareas de seguridad automatizamos con IA (clasificación, investig…) · B11.4 (¿Cómo medimos el impacto de la IA en el SOC (tiempo de clasificación,…) · B11.8 (¿Qué roles del equipo de seguridad cambian con la IA agéntica y cuál e…)
- **Apoyo de Microsoft:** Agentes de Security Copilot (Security Alert Triage Agent y Conditional Access Optimization Agent, disponibles de forma general).
- **Marcos (heredados):** NIST — CSF DE.AE, AI RMF MAP 3, IR 8596 | CIS — CIS 17, CIS 14 | The Open Group — Roles de seguridad | ISACA — COBIT APO07, COBIT DSS02, AAISM D3 | CSA — AICM GRC, AICM HRS

#### C04.9 · ¿Qué pasa con nuestros resultados si un proveedor crítico de tecnología falla durante una semana?

- **Quién pregunta:** CFO · **Cuándo:** Tras una interrupción masiva de un proveedor
- **Qué quiere saber realmente:** Quiere el impacto financiero de la dependencia tecnológica.
- **Una respuesta sólida incluye:** Dependencias críticas, impacto por día, alternativas, cláusulas contractuales, pruebas realizadas y cobertura del seguro.
- **Señal de alerta:** Suponer que la nube o el proveedor nunca fallan.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** A07.9 (¿Qué haríamos si un proveedor crítico de nube, software o servicios ge…) · A09.1 (¿Cuáles son nuestras funciones críticas de negocio, sus tolerancias de…) · B10.4 (¿Qué haríamos si un proveedor cambia, retira o degrada un modelo del q…)
- **Apoyo de Microsoft:** Quick Machine Recovery (Windows) para fallas masivas de equipos; Service Trust Portal para documentación de resiliencia.
- **Marcos (heredados):** NIST — CSF GV.SC, CSF PR.IR, CSF RC.RP | CIS — CIS 15, CIS 11 | The Open Group — TOGAF | ISACA — COBIT DSS04, COBIT APO10, COBIT BAI04 | CSA — CCM BCR, CCM STA, CCM IPY

### C05 · Negocio y producto

Las áreas de negocio preguntan qué pueden hacer, cuándo y con qué condiciones. Miden a seguridad por la velocidad y la claridad de sus respuestas.

#### C05.1 · ¿Puedo usar esta herramienta de IA con datos de clientes?

- **Quién pregunta:** Gerente de unidad de negocio · **Cuándo:** Continua · **Tema:** IA y agentes
- **Qué quiere saber realmente:** Necesita una respuesta rápida y una alternativa, no solo un «no».
- **Una respuesta sólida incluye:** Política de uso aceptable con herramientas autorizadas, tipos de datos admitidos, alternativa segura disponible, proceso rápido de aprobación y el motivo de cada condición.
- **Señal de alerta:** «No» sin alternativa, o «sí» sin evaluación.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** B02.4 (¿Tenemos una política de uso aceptable de IA que defina servicios auto…) · B03.3 (¿Qué hacemos cuando descubrimos IA no autorizada: bloquear, migrar a u…) · B05.4 (¿Cómo evitamos que información sensible salga por prompts, respuestas,…)
- **Apoyo de Microsoft:** Microsoft 365 Copilot con protección de datos empresariales; catálogo de aplicaciones de IA generativa en Defender for Cloud Apps; DLP para Copilot.
- **Marcos (heredados):** NIST — AI RMF GOVERN 1, AI RMF MANAGE 1, CSF PR.DS | CIS — CIS 2, CIS 14, CIS 3 | The Open Group — sin correspondencia directa | ISACA — COBIT APO14, COBIT APO01, AAISM D1 | CSA — AICM GRC, AICM HRS, AICM DSP

#### C05.2 · ¿Qué requisitos de seguridad tiene que cumplir nuestro producto digital antes de salir al mercado?

- **Quién pregunta:** Director de producto · **Cuándo:** Inicio de cada desarrollo
- **Qué quiere saber realmente:** Quiere requisitos claros y tempranos, no sorpresas al final.
- **Una respuesta sólida incluye:** Requisitos mínimos por nivel de riesgo, modelado de amenazas, pruebas, criterios de salida, quién aprueba y en cuánto tiempo.
- **Señal de alerta:** Requisitos que aparecen al final o revisiones sin plazo.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** A07.3 (¿Está integrada la seguridad en el ciclo de desarrollo (modelado de am…) · A07.8 (¿Cómo protegemos las APIs y la lógica de negocio expuesta (autorizació…) · A03.3 (¿Qué principios de seguridad son obligatorios en el diseño (mínimo pri…)
- **Apoyo de Microsoft:** Security Development Lifecycle (SDL) de Microsoft como referencia; seguridad de DevOps en Defender for Cloud.
- **Marcos (heredados):** NIST — CSF PR.PS, SP 800-218, CSF DE.CM | CIS — CIS 16, CIS 13, CIS 4 | The Open Group — TOGAF, Security Design Patterns, Security Principles for Architecture | ISACA — COBIT BAI03, COBIT BAI07, COBIT DSS05 | CSA — CCM AIS, CCM CCC

#### C05.3 · Un cliente grande nos mandó un cuestionario de seguridad de 300 preguntas. ¿Cuándo lo tenemos?

- **Quién pregunta:** Director comercial · **Cuándo:** Licitaciones y renovaciones
- **Qué quiere saber realmente:** El ciclo de venta depende de la velocidad de seguridad.
- **Una respuesta sólida incluye:** Biblioteca de respuestas y evidencia reutilizable, centro de confianza, plazo estándar, dueño, y uso de IA para responder con revisión humana.
- **Señal de alerta:** Cada cuestionario empieza de cero.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** B10.8 (¿Cómo demostramos a clientes, auditores y reguladores que nuestra IA e…) · A10.3 (¿Cuánta de nuestra evidencia de cumplimiento es automática y continua,…) · A10.2 (¿Cómo convertimos varios marcos y regulaciones en un único conjunto de…)
- **Apoyo de Microsoft:** Service Trust Portal para la evidencia de los servicios de Microsoft; cuestionario CAIQ de CSA.
- **Marcos (heredados):** NIST — AI RMF GOVERN 4, AI RMF MEASURE 2, CSF GV.OV | CIS — CIS 8 | The Open Group — TOGAF | ISACA — COBIT MEA04, COBIT MEA02, COBIT MEA03 | CSA — STAR, AICM A&A, CCM A&A

#### C05.4 · Quiero construir un agente que atienda clientes y ejecute operaciones. ¿Qué tengo que hacer para que lo aprueben?

- **Quién pregunta:** Gerente de negocio · **Cuándo:** Lanzamiento de un caso de IA · **Tema:** IA y agentes
- **Qué quiere saber realmente:** Quiere un camino conocido, con plazos.
- **Una respuesta sólida incluye:** Ciclo de vida del agente (propuesta, clasificación de riesgo, identidad, permisos mínimos, evaluaciones y red teaming, aprobación, monitoreo), plazos y patrones disponibles.
- **Señal de alerta:** Proceso inexistente, o de meses.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** B02.5 (¿Existe un proceso único de ciclo de vida para agentes y aplicaciones…) · B02.7 (¿Cómo clasificamos los sistemas de IA por nivel de riesgo y qué contro…) · B04.3 (¿Aplicamos mínimo privilegio y agencia mínima a los agentes: solo los…) · B08.1 (¿Qué evaluaciones (calidad, fundamentación, seguridad, sesgo, cumplimi…) · B06.6 (¿Hacemos red teaming de IA antes de producción y después de cada cambi…)
- **Apoyo de Microsoft:** Copilot Studio con entornos administrados; evaluaciones y AI Red Teaming Agent en Microsoft Foundry; Entra Agent ID.
- **Marcos (heredados):** NIST — AI RMF GOVERN 1, AI RMF MANAGE 1, AI RMF MEASURE 2 | CIS — guía CIS para agentes de IA, CIS 16, CIS 2 | The Open Group — TOGAF, Open FAIR, Zero Trust Commandments | ISACA — COBIT BAI07, AAISM D3, COBIT BAI01 | CSA — AICM GRC, AICM A&A, AICM CCC

#### C05.5 · ¿Por qué tengo que esperar a seguridad para contratar un proveedor SaaS?

- **Quién pregunta:** Gerente de negocio · **Cuándo:** Incorporación de un proveedor
- **Qué quiere saber realmente:** Cuestiona la proporcionalidad del proceso.
- **Una respuesta sólida incluye:** Evaluación proporcional al riesgo (datos y accesos), plazos por nivel, vía rápida para riesgo bajo y condiciones contractuales mínimas.
- **Señal de alerta:** La misma evaluación exhaustiva para todo.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** A07.5 (¿Cómo evaluamos, contratamos y monitoreamos a los terceros críticos, i…) · A07.7 (¿Cómo gobernamos las aplicaciones SaaS y los permisos OAuth que los us…) · A07.6 (¿Qué exigimos contractualmente a los proveedores (notificación de inci…)
- **Apoyo de Microsoft:** Catálogo y evaluación de riesgo de aplicaciones en Defender for Cloud Apps.
- **Marcos (heredados):** NIST — CSF GV.SC, SP 800-161, CSF ID.AM | CIS — CIS 15, CIS 2, CIS 6 | The Open Group — sin correspondencia directa | ISACA — COBIT APO10, COBIT APO09, COBIT BAI09 | CSA — CCM STA, CAIQ, STAR

#### C05.6 · ¿Los datos que ponemos en la IA se usan para entrenar modelos de otros?

- **Quién pregunta:** Gerente de negocio · **Cuándo:** Contratación de un servicio de IA · **Tema:** IA y agentes
- **Qué quiere saber realmente:** Quiere certeza contractual y técnica sobre el uso de los datos.
- **Una respuesta sólida incluye:** Compromisos contractuales de cada proveedor (uso, retención, residencia, no entrenamiento), configuración aplicada y forma de verificarla.
- **Señal de alerta:** Suponer sin leer los contratos.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** B05.9 (¿Qué compromisos contractuales tenemos de nuestros proveedores de IA s…) · B10.3 (¿Cómo evaluamos a los proveedores de modelos, plataformas y agentes de…) · B01.8 (¿Qué postura adoptamos frente a la IA de consumo y a la IA que nuestro…)
- **Apoyo de Microsoft:** Protección de datos empresariales de Microsoft 365 Copilot; principio «sus datos son suyos» de Microsoft.
- **Marcos (heredados):** NIST — CSF GV.SC, AI RMF GOVERN 6, AI RMF MANAGE 3 | CIS — CIS 15, CIS 2 | The Open Group — sin correspondencia directa | ISACA — COBIT APO10, AAISM D2, COBIT APO09 | CSA — AICM STA, AICM DSP, STAR

#### C05.7 · Si seguridad aísla un sistema durante un incidente, ¿qué pasa con mi operación?

- **Quién pregunta:** Gerente de operaciones · **Cuándo:** Tras un incidente
- **Qué quiere saber realmente:** Quiere previsibilidad y participación en las decisiones de contención.
- **Una respuesta sólida incluye:** Criterios de contención acordados, impacto por sistema, autorización previa para contenciones automáticas, comunicación y procedimientos alternativos.
- **Señal de alerta:** Contenciones sin acuerdo previo, o miedo a contener.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** A08.3 (¿Qué acciones de contención están automatizadas, cuáles requieren apro…) · A09.1 (¿Cuáles son nuestras funciones críticas de negocio, sus tolerancias de…) · A09.8 (¿Podemos operar los procesos críticos con mecanismos manuales o altern…)
- **Apoyo de Microsoft:** Interrupción automática de ataques en Defender XDR, con límites configurables.
- **Marcos (heredados):** NIST — CSF GV.OC, CSF RS.MI, CSF RS.MA | CIS — CIS 17, CIS 11 | The Open Group — TOGAF | ISACA — COBIT DSS04, COBIT DSS02, COBIT DSS05 | CSA — CCM BCR, CCM SEF

#### C05.8 · Mi equipo ya usa IA gratuita por su cuenta. ¿Es grave?

- **Quién pregunta:** Gerente de negocio · **Cuándo:** Continua · **Tema:** IA y agentes
- **Qué quiere saber realmente:** Quiere entender el riesgo real y qué alternativa ofrecer.
- **Una respuesta sólida incluye:** Datos de uso no autorizado (descubrimiento), riesgos concretos (fuga de datos, propiedad intelectual, decisiones sin control), alternativa autorizada, controles en el navegador y DLP, y comunicación.
- **Señal de alerta:** Prohibir sin alternativa, o ignorar.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** B03.2 (¿Cómo descubrimos el uso no autorizado de IA (aplicaciones web de IA g…) · B03.3 (¿Qué hacemos cuando descubrimos IA no autorizada: bloquear, migrar a u…) · B05.4 (¿Cómo evitamos que información sensible salga por prompts, respuestas,…)
- **Apoyo de Microsoft:** Defender for Cloud Apps; Microsoft Entra Internet Access; Purview DSPM y DLP.
- **Marcos (heredados):** NIST — AI RMF GOVERN 1, AI RMF MANAGE 1, CSF ID.AM | CIS — CIS 2, CIS 13, CIS 3 | The Open Group — sin correspondencia directa | ISACA — COBIT BAI09, COBIT DSS05, AAISM D3 | CSA — AICM DSP, AICM LOG, AICM GRC

#### C05.9 · ¿Cómo les explicamos a nuestros clientes que sus datos están seguros con nosotros?

- **Quién pregunta:** Director de experiencia del cliente · **Cuándo:** Comunicación a clientes
- **Qué quiere saber realmente:** Necesita un mensaje veraz y verificable.
- **Una respuesta sólida incluye:** Centro de confianza con políticas, certificaciones, prácticas de IA y canal de reporte; lenguaje simple; no prometer lo que no se puede demostrar.
- **Señal de alerta:** Afirmaciones absolutas («100 % seguro»).
- **Cómo prepararse (marco 99 + 99, versión 2.0):** B10.8 (¿Cómo demostramos a clientes, auditores y reguladores que nuestra IA e…) · B10.6 (¿Somos transparentes con clientes y empleados sobre cuándo interactúan…) · A11.6 (¿Cómo comunicamos el riesgo cibernético en lenguaje de negocio a cada…)
- **Apoyo de Microsoft:** Service Trust Portal y el informe de transparencia de IA responsable de Microsoft como referencias de práctica.
- **Marcos (heredados):** NIST — AI RMF MEASURE 2, AI RMF GOVERN 4, AI RMF MAP 5 | CIS — sin correspondencia directa | The Open Group — Open FAIR | ISACA — COBIT EDM05, COBIT MEA04, COBIT MEA03 | CSA — STAR, AICM A&A, AICM GRC

### C06 · Tecnología, datos e IA

CIO, CTO, CDO, CAIO e ingeniería preguntan por arquitectura, plataforma, datos y fricción: qué controles impone seguridad, con qué costo operativo y cómo se integran en su forma de trabajar.

#### C06.1 · ¿Qué arquitectura de seguridad objetivo propone y cómo encaja con la de TI?

- **Quién pregunta:** CIO · **Cuándo:** Planificación de arquitectura
- **Qué quiere saber realmente:** Quiere una arquitectura integrada, no paralela.
- **Una respuesta sólida incluye:** Arquitectura de referencia, principios, decisiones de plataforma, hoja de ruta conjunta y gobierno de arquitectura compartido.
- **Señal de alerta:** Una arquitectura de seguridad separada de la arquitectura empresarial.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** A03.1 (¿Tenemos una arquitectura de referencia de seguridad de extremo a extr…) · A03.9 (¿Tenemos una hoja de ruta de seguridad a 12–36 meses priorizada por ri…) · A03.7 (¿Cuánto valor perdemos por la fragmentación de herramientas y datos de…)
- **Apoyo de Microsoft:** Microsoft Cybersecurity Reference Architectures (MCRA); Security Adoption Framework (SAF).
- **Marcos (heredados):** NIST — CSF ID.IM, CSF GV.PO, CSF PR.PS | CIS — CIS IG1, CIS 8 | The Open Group — TOGAF, G152 | ISACA — COBIT APO03, COBIT BAI03, COBIT APO02 | CSA — CCM AIS, CCM IVS, CCM GRC

#### C06.2 · ¿Cuánto va a frenar Zero Trust a los equipos de ingeniería?

- **Quién pregunta:** CTO · **Cuándo:** Planificación de arquitectura
- **Qué quiere saber realmente:** Teme fricción y pérdida de productividad.
- **Una respuesta sólida incluye:** Plan por fases con impacto medido, automatización (políticas como código, pipelines seguros), excepciones temporales y métricas de productividad.
- **Señal de alerta:** Imponer controles sin medir su impacto.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** A03.2 (¿Cuál es nuestra estrategia Zero Trust, qué escenarios de negocio prio…) · A07.3 (¿Está integrada la seguridad en el ciclo de desarrollo (modelado de am…) · A11.5 (¿La seguridad forma parte de la cultura de ingeniería y producto (refe…)
- **Apoyo de Microsoft:** Zero Trust Adoption Framework de Microsoft.
- **Marcos (heredados):** NIST — CSF PR.AA, CSF PR.IR, SP 800-207 | CIS — CIS 16, CIS 6, CIS 12 | The Open Group — Zero Trust Commandments, TOGAF, Security Design Patterns | ISACA — COBIT APO02, COBIT APO03, COBIT APO13 | CSA — CCM AIS, CCM IAM, CCM IVS

#### C06.3 · ¿Qué datos puedo usar para entrenar o fundamentar modelos y agentes?

- **Quién pregunta:** CDO o CAIO · **Cuándo:** Diseño de un caso de IA · **Tema:** IA y agentes
- **Qué quiere saber realmente:** Necesita criterios previsibles, no decisiones caso por caso.
- **Una respuesta sólida incluye:** Criterios por clasificación, aprobación de fuentes, procedencia, minimización, privacidad y retención; proceso de aprobación con plazos.
- **Señal de alerta:** Decisiones caso por caso sin criterio.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** B05.3 (¿Qué datos pueden usarse para entrenar, ajustar o fundamentar modelos…) · B05.8 (¿Cómo garantizamos la calidad, procedencia e integridad de los datos q…) · A05.2 (¿Tenemos una taxonomía de clasificación aprobada, aplicada automáticam…)
- **Apoyo de Microsoft:** Clasificación, etiquetas de confidencialidad y DSPM en Microsoft Purview.
- **Marcos (heredados):** NIST — AI RMF MEASURE 2, AI RMF MAP 4, AI RMF GOVERN 6 | CIS — CIS 3 | The Open Group — TOGAF | ISACA — COBIT APO14, COBIT BAI03, AAISM D2 | CSA — AICM DSP, MAESTRO, AICM MDS

#### C06.4 · ¿Quién decide el nivel de autonomía de un agente: el dueño del caso de uso, el consejo de IA o el CISO?

- **Quién pregunta:** CAIO · **Cuándo:** Diseño de un caso de IA · **Tema:** IA y agentes
- **Qué quiere saber realmente:** Busca derechos de decisión claros.
- **Una respuesta sólida incluye:** Matriz de derechos de decisión por nivel de autonomía y radio de impacto, criterios técnicos (reversibilidad, montos, datos) y escalamiento.
- **Señal de alerta:** El CISO decide todo, o no decide nada.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** B07.1 (¿Qué nivel de autonomía permitimos a cada agente (sugerir, ejecutar co…) · B07.2 (¿Tenemos un perfil de radio de impacto por agente (datos, herramientas…) · B02.3 (¿Qué rol cumple el CISO en el gobierno de la IA (dueño, asesor, reviso…)
- **Apoyo de Microsoft:** Agent 365; aprobaciones humanas en flujos de agentes de Copilot Studio.
- **Marcos (heredados):** NIST — AI RMF MAP 3, AI RMF GOVERN 3, AI RMF MAP 2 | CIS — guía CIS para agentes de IA, CIS RAM | The Open Group — Open FAIR, Roles de seguridad | ISACA — COBIT APO01, AAISM D1, COBIT DSS06 | CSA — AICM GRC, MAESTRO

#### C06.5 · ¿Qué servidores MCP y herramientas pueden usar nuestros agentes?

- **Quién pregunta:** Arquitecto empresarial · **Cuándo:** Diseño de un caso de IA · **Tema:** IA y agentes
- **Qué quiere saber realmente:** Quiere un catálogo y criterios de aprobación.
- **Una respuesta sólida incluye:** Catálogo aprobado, criterios (origen, permisos, autenticación, firma, monitoreo), pasarela, revisión de cambios y retiro.
- **Señal de alerta:** Cada desarrollador conecta lo que quiere.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** B03.6 (¿Cómo inventariamos y aprobamos los servidores MCP y las herramientas…) · B06.5 (¿Qué controles tenemos contra el envenenamiento de herramientas y los…) · B06.4 (¿Cómo aseguramos la cadena de suministro de IA: modelos de terceros, p…)
- **Apoyo de Microsoft:** Registro de herramientas y servidores MCP en Agent 365 (versión preliminar); servidores MCP en Azure API Management; guía de seguridad para MCP.
- **Marcos (heredados):** NIST — AI RMF MAP 4, AI RMF GOVERN 6, CSF ID.AM | CIS — CIS 2, CIS 16, guía CIS para MCP | The Open Group — sin correspondencia directa | ISACA — AAISM D3, COBIT APO10, COBIT BAI09 | CSA — AICM STA, MAESTRO, AICM AIS

#### C06.6 · ¿Cuántas identidades no humanas tenemos y cuál es su riesgo?

- **Quién pregunta:** CIO · **Cuándo:** Revisión de identidad
- **Qué quiere saber realmente:** Sospecha que el número es mucho mayor que el de personas.
- **Una respuesta sólida incluye:** Inventario de cuentas de servicio, principales de servicio, secretos y agentes; cuántas sin dueño, con privilegios altos o con credenciales estáticas; plan de reducción.
- **Señal de alerta:** Desconocer el número.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** A04.4 (¿Tenemos inventario y gobierno de las identidades no humanas (cuentas…) · B04.6 (¿Cómo evitamos que los agentes usen secretos estáticos (claves de API,…) · B03.7 (¿Cómo detectamos agentes huérfanos, inactivos o cuyo dueño dejó la org…)
- **Apoyo de Microsoft:** Identidades de carga de trabajo en Microsoft Entra; Entra Agent ID.
- **Marcos (heredados):** NIST — CSF PR.AA, CSF ID.AM, CSF PR.DS | CIS — CIS 5, CIS 3, CIS 16 | The Open Group — sin correspondencia directa | ISACA — COBIT DSS05, COBIT BAI09, AAISM D3 | CSA — AICM IAM, CCM IAM, AICM CEK

#### C06.7 · ¿Qué hacemos con los sistemas heredados que no podemos actualizar?

- **Quién pregunta:** CIO · **Cuándo:** Planificación anual
- **Qué quiere saber realmente:** Necesita una decisión por sistema, con financiamiento.
- **Una respuesta sólida incluye:** Inventario, riesgo, decisión por sistema (aislar, reemplazar o aceptar con fecha), controles compensatorios y financiamiento.
- **Señal de alerta:** Aceptación indefinida.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** A03.5 (¿Cómo gestionamos la deuda técnica y los sistemas heredados que no pue…) · A03.4 (¿Cómo segmentamos redes, entornos y planos de administración para limi…)
- **Apoyo de Microsoft:** Exposure Management (activos críticos y rutas de ataque).
- **Marcos (heredados):** NIST — CSF ID.RA, CSF PR.PS, CSF PR.IR | CIS — CIS 2, CIS 7, CIS 12 | The Open Group — TOGAF, Zero Trust Commandments | ISACA — COBIT BAI09, COBIT APO12, COBIT DSS05 | CSA — CCM TVM, CCM CCC, CCM IVS

#### C06.8 · ¿Cómo probamos un agente antes de ponerlo en producción y cada vez que cambia?

- **Quién pregunta:** CTO · **Cuándo:** Pase a producción · **Tema:** IA y agentes
- **Qué quiere saber realmente:** Quiere un estándar de pruebas repetible.
- **Una respuesta sólida incluye:** Evaluaciones obligatorias (calidad, fundamentación, seguridad, cumplimiento de la tarea), red teaming, cambios que obligan a repetir pruebas, criterios de salida y monitoreo de deriva.
- **Señal de alerta:** Pruebas solo funcionales.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** B08.1 (¿Qué evaluaciones (calidad, fundamentación, seguridad, sesgo, cumplimi…) · B08.3 (¿Qué cambios (modelo, versión, instrucciones de sistema, herramientas,…) · B06.6 (¿Hacemos red teaming de IA antes de producción y después de cada cambi…) · B08.2 (¿Cómo monitoreamos en producción la deriva de comportamiento, calidad…)
- **Apoyo de Microsoft:** Evaluadores de agentes, AI Red Teaming Agent y observabilidad en Microsoft Foundry.
- **Marcos (heredados):** NIST — AI RMF MEASURE 2, AI RMF MANAGE 4, AI RMF MANAGE 1 | CIS — CIS 16, guía CIS para LLM, CIS 4 | The Open Group — TOGAF | ISACA — AAISM D3, COBIT BAI07, COBIT APO11 | CSA — AICM MDS, AICM A&A, AICM CCC

#### C06.9 · ¿Qué pasa si el proveedor retira o cambia el modelo del que depende un proceso crítico?

- **Quién pregunta:** CIO · **Cuándo:** Aviso de retiro de un modelo · **Tema:** IA y agentes
- **Qué quiere saber realmente:** Quiere gestionar la dependencia de modelos como cualquier otra dependencia crítica.
- **Una respuesta sólida incluye:** Inventario de dependencias de modelos, políticas de retiro de los proveedores, pruebas de regresión, alternativas y cláusulas contractuales.
- **Señal de alerta:** Ninguna previsión.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** B10.4 (¿Qué haríamos si un proveedor cambia, retira o degrada un modelo del q…) · B03.5 (¿Mantenemos una lista de materiales de IA (modelos, versiones, conjunt…)
- **Apoyo de Microsoft:** Política de retiro de modelos de Microsoft Foundry.
- **Marcos (heredados):** NIST — AI RMF GOVERN 6, CSF GV.SC, AI RMF MANAGE 3 | CIS — CIS 15, CIS 2, guía CIS para LLM | The Open Group — sin correspondencia directa | ISACA — COBIT APO10, COBIT DSS04, AAISM D2 | CSA — AICM STA, AICM BCR, AICM IPY

### C07 · Legal, cumplimiento y privacidad

Legal, cumplimiento y privacidad preguntan qué debemos, a quién, en qué plazo y cómo lo demostramos, incluida la regulación emergente de IA.

#### C07.1 · Ante un incidente, ¿a quién tenemos que notificar, en qué plazo y en cada país?

- **Quién pregunta:** Director legal · **Cuándo:** Revisión anual y tras un incidente
- **Qué quiere saber realmente:** Quiere una matriz lista antes del incidente.
- **Una respuesta sólida incluye:** Matriz de obligaciones de notificación por país y sector (regulador, titulares de datos, mercado, contrapartes), plazos, umbrales, responsables, plantillas y ensayo del proceso.
- **Señal de alerta:** Matriz inexistente o desactualizada.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** A10.1 (¿Qué obligaciones legales, regulatorias y contractuales de seguridad n…) · A08.9 (¿Hemos definido cómo interactuamos con los CERT nacionales, reguladore…) · B09.7 (¿Qué umbral convierte un comportamiento anómalo de la IA en un inciden…)
- **Apoyo de Microsoft:** Sin capacidad específica: es un proceso legal y regulatorio.
- **Marcos (heredados):** NIST — CSF GV.OC, CSF RS.CO, CSF GV.SC | CIS — CIS 17 | The Open Group — TOGAF | ISACA — COBIT MEA03, COBIT DSS02, AAISM D2 | CSA — CCM GRC, CCM A&A, CCM STA

#### C07.2 · Durante una investigación, ¿cómo preservamos la evidencia y el privilegio legal?

- **Quién pregunta:** Director legal · **Cuándo:** Durante un incidente
- **Qué quiere saber realmente:** Quiere evitar que la investigación técnica destruya evidencia o exponga a la organización.
- **Una respuesta sólida incluye:** Procedimiento de cadena de custodia, retención de registros, participación de abogados en la investigación, retención legal y proveedores forenses contratados de antemano.
- **Señal de alerta:** Investigación sin participación de Legal o registros sobrescritos.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** A08.7 (¿Qué retención y calidad de registros necesitamos para investigaciones…) · B09.4 (¿Podemos reconstruir de forma forense una cadena de acciones de varios…) · A05.5 (¿Retenemos solo lo necesario, eliminamos lo obsoleto y podemos respond…)
- **Apoyo de Microsoft:** eDiscovery y retención en Microsoft Purview; lago de datos de Microsoft Sentinel para conservar registros.
- **Marcos (heredados):** NIST — CSF DE.CM, CSF RS.AN, CSF PR.DS | CIS — CIS 8, CIS 3 | The Open Group — sin correspondencia directa | ISACA — COBIT MEA03, COBIT DSS05, COBIT DSS02 | CSA — CCM LOG, CCM SEF, AICM SEF

#### C07.3 · ¿El monitoreo de seguridad respeta la privacidad de los empleados?

- **Quién pregunta:** Responsable de protección de datos (DPO) · **Cuándo:** Despliegue de nuevas capacidades de monitoreo
- **Qué quiere saber realmente:** Quiere proporcionalidad, base legal y transparencia.
- **Una respuesta sólida incluye:** Base legal, proporcionalidad, minimización, transparencia, acceso restringido a los datos de monitoreo, evaluación de impacto y participación de RR. HH.
- **Señal de alerta:** Monitoreo sin evaluación de impacto ni límites.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** A05.4 (¿Cómo gestionamos el riesgo interno, negligente o malicioso, con propo…) · B09.5 (¿Cómo equilibramos la observabilidad de prompts y respuestas con la pr…) · A11.8 (¿Qué código de conducta profesional rige al equipo de seguridad, cómo…) — nueva en la v2.0
- **Apoyo de Microsoft:** Insider Risk Management de Microsoft Purview, con nombres de usuario seudonimizados por defecto.
- **Marcos (heredados):** NIST — CSF PR.DS, CSF DE.CM, AI RMF MEASURE 2 | CIS — CIS 3, CIS 14, CIS 6 | The Open Group — sin correspondencia directa | ISACA — COBIT APO07, COBIT DSS05, COBIT APO14 | CSA — CCM HRS, CCM DSP, AICM DSP

#### C07.4 · ¿Qué leyes de IA nos aplican y qué rol cumplimos en cada caso: proveedor, implementador o usuario?

- **Quién pregunta:** Director legal · **Cuándo:** Revisión regulatoria anual · **Tema:** IA y agentes
- **Qué quiere saber realmente:** Quiere un mapa regulatorio de IA, no supuestos.
- **Una respuesta sólida incluye:** Inventario regulatorio de IA por país (incluida la Ley de IA de la UE cuando aplique), rol por sistema, obligaciones, plazos y responsables.
- **Señal de alerta:** «En nuestro país todavía no hay ley», sin análisis.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** B10.1 (¿Qué leyes, regulaciones y guías de IA aplican en cada país donde oper…) · B07.9 (¿Cómo aplicamos los requisitos legales de supervisión humana (por ejem…)
- **Apoyo de Microsoft:** Compliance Manager (marcos de IA).
- **Marcos (heredados):** NIST — AI RMF GOVERN 1, CSF GV.OC, AI RMF MAP 3 | CIS — sin correspondencia directa | The Open Group — TOGAF | ISACA — COBIT MEA03, AAISM D1 | CSA — AICM GRC

#### C07.5 · Si la IA genera contenido que infringe derechos de autor o difunde datos personales, ¿quién responde?

- **Quién pregunta:** Director legal · **Cuándo:** Lanzamiento de un caso de IA generativa · **Tema:** IA y agentes
- **Qué quiere saber realmente:** Quiere saber qué riesgo legal asume la organización y qué controles lo reducen.
- **Una respuesta sólida incluye:** Análisis de riesgo de propiedad intelectual y privacidad por caso de uso, controles (detección de material protegido, filtros, revisión humana), compromisos contractuales de los proveedores y procedimiento de respuesta.
- **Señal de alerta:** Suponer que la responsabilidad es solo del proveedor.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** B10.7 (¿Cómo gestionamos los riesgos de propiedad intelectual y derechos de a…) · B05.4 (¿Cómo evitamos que información sensible salga por prompts, respuestas,…) · B10.6 (¿Somos transparentes con clientes y empleados sobre cuándo interactúan…)
- **Apoyo de Microsoft:** Detección de material protegido en Azure AI Content Safety (solo inglés); Customer Copyright Commitment de Microsoft, sujeto a sus condiciones.
- **Marcos (heredados):** NIST — AI 600-1, AI RMF MAP 4, AI RMF GOVERN 6 | CIS — CIS 3, guía CIS para LLM | The Open Group — sin correspondencia directa | ISACA — COBIT MEA03, AAISM D2, COBIT DSS05 | CSA — AICM GRC, AICM DSP

#### C07.6 · ¿Cumplimos las regulaciones de ciberseguridad y de resiliencia operativa digital que nos alcanzan?

- **Quién pregunta:** Responsable de cumplimiento · **Cuándo:** Entrada en vigor de una regulación
- **Qué quiere saber realmente:** Quiere el grado de cumplimiento con evidencia, no declaraciones.
- **Una respuesta sólida incluye:** Brechas por requisito, plan, dueños, evidencia automatizada y terceros alcanzados.
- **Señal de alerta:** Cumplimiento declarativo.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** A10.1 (¿Qué obligaciones legales, regulatorias y contractuales de seguridad n…) · A10.2 (¿Cómo convertimos varios marcos y regulaciones en un único conjunto de…)
- **Apoyo de Microsoft:** Compliance Manager (plantillas premium de DORA y NIS2).
- **Marcos (heredados):** NIST — CSF GV.OC, CSF GV.SC, SP 800-53 | CIS — sin correspondencia directa | The Open Group — TOGAF | ISACA — COBIT MEA03, COBIT MEA02 | CSA — CCM GRC, CCM A&A, CCM STA

#### C07.7 · ¿Nuestros contratos con proveedores nos protegen ante un incidente de ellos?

- **Quién pregunta:** Director legal · **Cuándo:** Contratación y renovación
- **Qué quiere saber realmente:** Quiere saber si los contratos críticos tienen cláusulas mínimas de seguridad.
- **Una respuesta sólida incluye:** Cláusulas mínimas (notificación, auditoría, continuidad, subcontratación, responsabilidad, salida), cobertura de los contratos críticos y brechas.
- **Señal de alerta:** Contratos estándar sin revisión de seguridad.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** A07.6 (¿Qué exigimos contractualmente a los proveedores (notificación de inci…) · B05.9 (¿Qué compromisos contractuales tenemos de nuestros proveedores de IA s…)
- **Apoyo de Microsoft:** Service Trust Portal; adenda de protección de datos de productos y servicios de Microsoft (DPA).
- **Marcos (heredados):** NIST — CSF GV.SC, AI RMF GOVERN 6 | CIS — CIS 15 | The Open Group — sin correspondencia directa | ISACA — COBIT APO09, COBIT APO10, AAISM D2 | CSA — CCM STA, CCM IPY, AICM STA

#### C07.8 · ¿Guardamos los prompts y las respuestas de la IA? ¿Por cuánto tiempo y quién puede verlos?

- **Quién pregunta:** Responsable de protección de datos (DPO) · **Cuándo:** Despliegue de IA generativa · **Tema:** IA y agentes
- **Qué quiere saber realmente:** Quiere una decisión explícita que equilibre obligación legal y privacidad.
- **Una respuesta sólida incluye:** Política de retención de interacciones de IA, acceso restringido, eDiscovery, derechos de los titulares y equilibrio con la privacidad.
- **Señal de alerta:** Retención indefinida, o nula, sin decisión documentada.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** B05.5 (¿Retenemos, auditamos y podemos buscar los prompts, respuestas y accio…) · B09.5 (¿Cómo equilibramos la observabilidad de prompts y respuestas con la pr…)
- **Apoyo de Microsoft:** Retención y eDiscovery de interacciones de IA en Microsoft Purview.
- **Marcos (heredados):** NIST — CSF DE.CM, CSF RS.AN, AI RMF MANAGE 4 | CIS — CIS 8, CIS 3 | The Open Group — sin correspondencia directa | ISACA — COBIT MEA03, COBIT APO14 | CSA — AICM LOG, AICM SEF, AICM DSP

#### C07.9 · ¿Cuántas políticas tenemos y cuántas se cumplen de verdad?

- **Quién pregunta:** Responsable de cumplimiento · **Cuándo:** Revisión anual de políticas
- **Qué quiere saber realmente:** Sospecha de un cuerpo normativo extenso y poco verificable.
- **Una respuesta sólida incluye:** Inventario de políticas, vigencia, cumplimiento medido mediante controles técnicos, excepciones y plan de simplificación.
- **Señal de alerta:** Políticas extensas sin medición.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** A01.5 (¿Nuestras políticas de seguridad son pocas, vigentes, comprensibles y…) · A10.5 (¿Cómo gestionamos las excepciones a las políticas: quién las aprueba,…)
- **Apoyo de Microsoft:** Compliance Manager; Secure Score.
- **Marcos (heredados):** NIST — CSF GV.PO, CSF GV.RM | CIS — sin correspondencia directa | The Open Group — Security Principles for Architecture, O-ESA, TOGAF | ISACA — COBIT APO01, COBIT MEA02, COBIT APO12 | CSA — CCM GRC

### C08 · Reguladores y supervisores

Los supervisores preguntan por gobierno, resiliencia, terceros, notificación y, cada vez más, por el uso de la IA en procesos que afectan a clientes. Esperan evidencia en plazos cortos.

#### C08.1 · ¿Quién es responsable de la seguridad de la información ante el directorio y cómo la supervisa el directorio?

- **Quién pregunta:** Supervisor sectorial · **Cuándo:** Inspección
- **Qué quiere saber realmente:** Verifica la estructura de gobierno y su funcionamiento real.
- **Una respuesta sólida incluye:** Estructura de gobierno, línea de reporte, actas, indicadores reportados y decisiones tomadas por el directorio.
- **Señal de alerta:** Actas sin discusión del riesgo cibernético.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** A01.2 (¿A quién reporta el CISO, qué independencia real tiene respecto de TI,…) · A01.4 (¿Con qué frecuencia, formato y métricas supervisa el directorio el rie…)
- **Apoyo de Microsoft:** Sin capacidad específica: es una cuestión de gobierno.
- **Marcos (heredados):** NIST — CSF GV.RR, CSF GV.OV | CIS — sin correspondencia directa | The Open Group — TOGAF, Roles de seguridad, Open FAIR | ISACA — COBIT EDM01, COBIT APO01, COBIT APO08 | CSA — CCM GRC, CCM HRS

#### C08.2 · Muéstrennos el último ejercicio de continuidad y recuperación ante un ciberataque y sus resultados.

- **Quién pregunta:** Supervisor sectorial · **Cuándo:** Inspección o requerimiento
- **Qué quiere saber realmente:** Quiere evidencia de capacidad probada.
- **Una respuesta sólida incluye:** Alcance, escenario, participantes, tiempos logrados frente a las tolerancias, hallazgos y acciones cerradas con evidencia.
- **Señal de alerta:** Solo ejercicios de escritorio, sin pruebas técnicas.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** A09.2 (¿Podemos recuperar identidad, datos y servicios críticos tras un ranso…) · A09.6 (¿Cuándo fue el último ejercicio de crisis con el comité ejecutivo y qu…) · A09.9 (¿Convertimos los incidentes, cuasi incidentes y ejercicios en cambios…)
- **Apoyo de Microsoft:** Sin capacidad específica: es evidencia de ejercicios del cliente.
- **Marcos (heredados):** NIST — CSF RC.RP, CSF ID.IM, CSF PR.IR | CIS — CIS 17, CIS 11 | The Open Group — TOGAF | ISACA — COBIT DSS04, COBIT MEA01, COBIT DSS03 | CSA — CCM BCR, CCM SEF

#### C08.3 · ¿Cuál es su concentración en proveedores tecnológicos críticos y cuál es su estrategia de salida?

- **Quién pregunta:** Supervisor sectorial · **Cuándo:** Inspección o requerimiento
- **Qué quiere saber realmente:** Preocupación sistémica por concentración y dependencia.
- **Una respuesta sólida incluye:** Registro de terceros críticos, concentración, planes de salida y portabilidad, pruebas y cláusulas contractuales.
- **Señal de alerta:** Ninguna estrategia de salida documentada.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** A07.5 (¿Cómo evaluamos, contratamos y monitoreamos a los terceros críticos, i…) · A07.9 (¿Qué haríamos si un proveedor crítico de nube, software o servicios ge…) · B10.4 (¿Qué haríamos si un proveedor cambia, retira o degrada un modelo del q…)
- **Apoyo de Microsoft:** Service Trust Portal (informes y documentación de los servicios de Microsoft).
- **Marcos (heredados):** NIST — CSF GV.SC, SP 800-161, CSF RC.RP | CIS — CIS 15, CIS 11 | The Open Group — sin correspondencia directa | ISACA — COBIT APO10, COBIT DSS04, COBIT APO09 | CSA — CCM STA, CAIQ, STAR

#### C08.4 · ¿En cuánto tiempo pueden detectar, clasificar y notificarnos un incidente grave?

- **Quién pregunta:** Supervisor sectorial · **Cuándo:** Inspección o tras un incidente
- **Qué quiere saber realmente:** Quiere tiempos medidos y criterios alineados con la norma.
- **Una respuesta sólida incluye:** Tiempos medidos de detección, clasificación y notificación, criterios de clasificación alineados con la norma, ensayos y casos reales.
- **Señal de alerta:** Tiempos no medidos.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** A08.2 (¿Cuáles son nuestros tiempos de detección, contención y recuperación p…) · A08.9 (¿Hemos definido cómo interactuamos con los CERT nacionales, reguladore…) · B09.7 (¿Qué umbral convierte un comportamiento anómalo de la IA en un inciden…)
- **Apoyo de Microsoft:** Métricas de detección y respuesta de Defender XDR y Microsoft Sentinel.
- **Marcos (heredados):** NIST — CSF RS.CO, CSF DE.AE, CSF RS.MI | CIS — CIS 17 | The Open Group — sin correspondencia directa | ISACA — COBIT DSS02, COBIT MEA03, COBIT MEA01 | CSA — CCM SEF, AICM SEF

#### C08.5 · ¿Qué sistemas de IA usan en procesos que afectan a clientes y cómo controlan sus riesgos?

- **Quién pregunta:** Supervisor sectorial · **Cuándo:** Inspección o requerimiento · **Tema:** IA y agentes
- **Qué quiere saber realmente:** La supervisión de IA empieza por el inventario.
- **Una respuesta sólida incluye:** Inventario de IA en procesos con impacto en clientes, evaluación de impacto, controles, supervisión humana, capacidad de explicación e incidentes.
- **Señal de alerta:** Inventario incompleto.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** B03.1 (¿Tenemos un inventario único de modelos, aplicaciones, copilotos, agen…) · B10.2 (¿Evaluamos el impacto de los sistemas de IA sobre las personas y sus d…) · B08.9 (¿Cómo explicamos y justificamos una decisión apoyada por IA cuando un…) · B07.9 (¿Cómo aplicamos los requisitos legales de supervisión humana (por ejem…)
- **Apoyo de Microsoft:** Agent 365; Purview DSPM; Compliance Manager (marcos de IA).
- **Marcos (heredados):** NIST — AI RMF GOVERN 1, CSF ID.AM, AI RMF MAP 5 | CIS — CIS 1, CIS 2, guía CIS para agentes de IA | The Open Group — TOGAF | ISACA — COBIT MEA03, COBIT BAI09, COBIT BAI10 | CSA — AICM GRC, AICM MDS, AICM DSP

#### C08.6 · ¿Cómo gestionan las vulnerabilidades críticas y en qué plazos las corrigen?

- **Quién pregunta:** Supervisor sectorial · **Cuándo:** Inspección
- **Qué quiere saber realmente:** Quiere ver cumplimiento de plazos y tratamiento de excepciones.
- **Una respuesta sólida incluye:** Política de remediación por criticidad y explotabilidad, cumplimiento de plazos, excepciones formales y exposición actual.
- **Señal de alerta:** Plazos incumplidos sin excepción formal.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** A06.2 (¿Cuánto tiempo permanecen expuestos nuestros activos críticos a vulner…) · A06.3 (¿Priorizamos la remediación por explotabilidad, rutas de ataque y crit…)
- **Apoyo de Microsoft:** Microsoft Defender Vulnerability Management; Exposure Management.
- **Marcos (heredados):** NIST — CSF ID.RA, CSF PR.PS | CIS — CIS 7 | The Open Group — Open FAIR | ISACA — COBIT APO12, COBIT DSS05 | CSA — CCM TVM

#### C08.7 · ¿Cómo protegen los datos de los clientes y cómo saben quién accede a ellos?

- **Quién pregunta:** Supervisor de protección de datos · **Cuándo:** Inspección o reclamo
- **Qué quiere saber realmente:** Quiere visibilidad del acceso, no solo políticas.
- **Una respuesta sólida incluye:** Inventario de datos sensibles, controles de acceso, registros, revisiones, DLP e incidentes.
- **Señal de alerta:** Sin visibilidad de quién accede.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** A05.1 (¿Sabemos dónde están nuestros datos sensibles, quién accede a ellos y…) · A05.3 (¿Cómo prevenimos la pérdida de datos en correo, colaboración, endpoint…) · A04.5 (¿Cómo gobernamos el ciclo de vida de las identidades (alta, cambio, ba…)
- **Apoyo de Microsoft:** Microsoft Purview (DSPM, DLP y Audit).
- **Marcos (heredados):** NIST — CSF PR.DS, CSF ID.AM, CSF PR.AA | CIS — CIS 3, CIS 5, CIS 6 | The Open Group — TOGAF | ISACA — COBIT APO14, COBIT DSS05, COBIT BAI09 | CSA — CCM DSP, CCM IAM, CCM HRS

#### C08.8 · ¿Cómo evitan que un agente de IA ejecute operaciones no autorizadas en nombre de un cliente?

- **Quién pregunta:** Supervisor sectorial · **Cuándo:** Inspección o lanzamiento de un servicio con agentes · **Tema:** IA y agentes
- **Qué quiere saber realmente:** Preocupación por la autoridad delegada a sistemas autónomos.
- **Una respuesta sólida incluye:** Identidad propia del agente, permisos mínimos, límites de transacción, aprobación humana para acciones irreversibles, registro y monitoreo, y capacidad de suspensión.
- **Señal de alerta:** Agentes que operan con credenciales de usuario compartidas.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** B04.2 (¿Cuándo actúa un agente en nombre de un usuario y cuándo con autoridad…) · B07.3 (¿Qué acciones nunca puede ejecutar un agente sin intervención humana,…) · B07.6 (¿Qué límites operativos (presupuesto, cantidad de llamadas, montos, fr…) · B09.1 (¿Registramos de forma correlacionable quién pidió qué, qué hizo el age…)
- **Apoyo de Microsoft:** Entra Agent ID; aprobaciones humanas en flujos de agentes; Agent 365.
- **Marcos (heredados):** NIST — CSF PR.AA, AI RMF MANAGE 2, AI RMF GOVERN 3 | CIS — guía CIS para agentes de IA, CIS 6, CIS 8 | The Open Group — Security Principles for Architecture | ISACA — AAISM D3, COBIT DSS05, COBIT DSS06 | CSA — AICM IAM, MAESTRO, AICM AIS

#### C08.9 · ¿Cómo aseguran que el personal clave tiene las competencias necesarias y que no dependen de una sola persona?

- **Quién pregunta:** Supervisor sectorial · **Cuándo:** Inspección
- **Qué quiere saber realmente:** Mira la resiliencia de las personas, no solo de la tecnología.
- **Una respuesta sólida incluye:** Plan de competencias, certificaciones, sucesión, cobertura de funciones críticas y servicios gestionados.
- **Señal de alerta:** Conocimiento concentrado en una persona.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** A11.3 (¿Tenemos un plan de talento de seguridad (brechas de habilidades, suce…) · A11.7 (¿Qué capacidades críticas dependen de una sola persona o de un único p…)
- **Apoyo de Microsoft:** Sin capacidad específica: es gestión de talento.
- **Marcos (heredados):** NIST — CSF GV.RR, CSF PR.AT, CSF PR.AA | CIS — CIS 14, CIS 5, CIS 6 | The Open Group — Roles de seguridad | ISACA — COBIT APO07, COBIT BAI08 | CSA — CCM HRS, CCM IAM

### C09 · Auditoría interna, auditoría externa y certificadores

Los auditores preguntan por el diseño y la eficacia de los controles sobre la población completa y durante todo el período, no por la intención.

#### C09.1 · Entrégueme la lista completa de usuarios con privilegios y la evidencia de su última revisión.

- **Quién pregunta:** Auditor interno · **Cuándo:** Auditoría anual
- **Qué quiere saber realmente:** Prueba la población completa, incluidos servicios y agentes.
- **Una respuesta sólida incluye:** Inventario de privilegios (personas, servicios y agentes), privilegios permanentes frente a elevación justo a tiempo, revisiones con evidencia y acciones tomadas.
- **Señal de alerta:** Lista manual incompleta o revisiones aprobadas en bloque.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** A04.2 (¿Cómo gestionamos el acceso privilegiado: cuentas separadas, elevación…) · A04.5 (¿Cómo gobernamos el ciclo de vida de las identidades (alta, cambio, ba…) · B04.4 (¿Los permisos de los agentes son temporales, se revisan periódicamente…)
- **Apoyo de Microsoft:** Microsoft Entra ID Governance (revisiones de acceso) y Privileged Identity Management.
- **Marcos (heredados):** NIST — CSF PR.AA, CSF PR.PS, AI RMF MANAGE 2 | CIS — CIS 6, CIS 5, guía CIS para agentes de IA | The Open Group — Zero Trust Commandments | ISACA — COBIT DSS05, COBIT DSS06, COBIT APO07 | CSA — CCM IAM, CCM HRS, AICM IAM

#### C09.2 · ¿Cómo demuestran que los controles funcionaron durante todo el período y no solo hoy?

- **Quién pregunta:** Auditor externo · **Cuándo:** Auditoría anual
- **Qué quiere saber realmente:** Busca evidencia de eficacia operativa continua.
- **Una respuesta sólida incluye:** Evidencia continua (registros, informes automáticos, pruebas periódicas), muestreo, excepciones y desviaciones con su tratamiento.
- **Señal de alerta:** Evidencia puntual preparada para la auditoría.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** A10.3 (¿Cuánta de nuestra evidencia de cumplimiento es automática y continua,…)
- **Apoyo de Microsoft:** Compliance Manager; Purview Audit; lago de datos de Microsoft Sentinel.
- **Marcos (heredados):** NIST — CSF GV.OV, CSF ID.IM, CSF RS.CO | CIS — CIS 8 | The Open Group — sin correspondencia directa | ISACA — COBIT MEA02, COBIT MEA03, COBIT MEA04 | CSA — CCM A&A, CCM SEF

#### C09.3 · ¿Qué agentes de IA están en producción, quién los aprobó y qué permisos tienen?

- **Quién pregunta:** Auditor interno · **Cuándo:** Auditoría de IA · **Tema:** IA y agentes
- **Qué quiere saber realmente:** Prueba la población completa de agentes, incluidos los creados por usuarios.
- **Una respuesta sólida incluye:** Registro de agentes con dueño, aprobación, nivel de riesgo, permisos y última revisión; agentes huérfanos detectados y retirados.
- **Señal de alerta:** Registro incompleto; agentes creados por usuarios fuera del inventario.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** B03.1 (¿Tenemos un inventario único de modelos, aplicaciones, copilotos, agen…) · B03.4 (¿Sabemos qué agentes crean los usuarios con herramientas de bajo códig…) · B03.7 (¿Cómo detectamos agentes huérfanos, inactivos o cuyo dueño dejó la org…) · B04.4 (¿Los permisos de los agentes son temporales, se revisan periódicamente…)
- **Apoyo de Microsoft:** Agent 365; inventario de Power Platform; aprobación de agentes en el centro de administración de Microsoft 365.
- **Marcos (heredados):** NIST — AI RMF GOVERN 1, CSF ID.AM, CSF PR.AA | CIS — guía CIS para agentes de IA, CIS 2, CIS 1 | The Open Group — TOGAF | ISACA — AAISM D3, COBIT BAI09, COBIT DSS05 | CSA — AICM IAM, AICM DSP, AICM MDS

#### C09.4 · ¿Cómo se gestionan los cambios en los sistemas críticos y quién los aprueba?

- **Quién pregunta:** Auditor interno · **Cuándo:** Auditoría anual
- **Qué quiere saber realmente:** Verifica segregación de funciones y control de cambios.
- **Una respuesta sólida incluye:** Proceso de cambios, segregación de funciones, cambios de emergencia, registro y conciliación entre cambios autorizados y realizados.
- **Señal de alerta:** Cambios fuera de proceso detectados después.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** A06.4 (¿Están definidas y aplicadas configuraciones seguras de referencia, y…) · B08.3 (¿Qué cambios (modelo, versión, instrucciones de sistema, herramientas,…) · B04.8 (¿Separamos funciones entre quien construye un agente, quien aprueba su…)
- **Apoyo de Microsoft:** Detección de desvíos de configuración en Defender for Cloud.
- **Marcos (heredados):** NIST — CSF PR.PS, AI RMF MANAGE 4, AI RMF GOVERN 1 | CIS — CIS 4, CIS Benchmarks, CIS 16 | The Open Group — TOGAF | ISACA — COBIT BAI06, COBIT BAI10, COBIT DSS05 | CSA — AICM CCC, CCM CCC, CCM IVS

#### C09.5 · ¿Cómo validan que los filtros y controles de la IA funcionan como esperan?

- **Quién pregunta:** Auditor de IA · **Cuándo:** Auditoría de IA · **Tema:** IA y agentes
- **Qué quiere saber realmente:** No acepta la configuración por defecto como evidencia.
- **Una respuesta sólida incluye:** Pruebas recurrentes de los guardrails (bloqueos esperados y falsos positivos), red teaming, resultados, umbrales y cambios aplicados.
- **Señal de alerta:** Confiar en la configuración por defecto sin pruebas.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** B08.4 (¿Comprobamos de forma recurrente que los filtros y guardrails bloquean…) · B06.6 (¿Hacemos red teaming de IA antes de producción y después de cada cambi…)
- **Apoyo de Microsoft:** Prompt Shields (la detección en documentos está desactivada por defecto en Foundry y conviene revisarla); AI Red Teaming Agent.
- **Marcos (heredados):** NIST — AI RMF MEASURE 2, AI RMF MEASURE 1 | CIS — CIS 18, guía CIS para agentes de IA | The Open Group — sin correspondencia directa | ISACA — COBIT MEA02, AAISM D3, AI Audit Toolkit | CSA — AICM A&A, AICM MDS, AICM TVM

#### C09.6 · ¿Cuál es el alcance del sistema de gestión y cómo decidieron qué queda afuera?

- **Quién pregunta:** Certificador (ISO/IEC 27001 o 42001) · **Cuándo:** Certificación o recertificación
- **Qué quiere saber realmente:** Verifica que el alcance proteja lo importante y no solo lo fácil de certificar.
- **Una respuesta sólida incluye:** Alcance justificado, interfaces, exclusiones con motivo, declaración de aplicabilidad y riesgos asociados.
- **Señal de alerta:** Un alcance diseñado para aprobar, no para proteger.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** B08.6 (¿Vamos a implementar o certificar un sistema de gestión de IA (ISO/IEC…) · A10.9 (¿Qué nivel de madurez queremos alcanzar por dominio y cómo medimos la…)
- **Apoyo de Microsoft:** Service Trust Portal (certificaciones de Microsoft como insumo para la parte en la nube).
- **Marcos (heredados):** NIST — CSF ID.IM | CIS — CIS IG1 | The Open Group — sin correspondencia directa | ISACA — COBIT APO01, COBIT MEA03, AAISM D1 | CSA — STAR

#### C09.7 · ¿Qué registros conservan, por cuánto tiempo, y pueden reconstruir un incidente de hace seis meses?

- **Quién pregunta:** Auditor externo · **Cuándo:** Auditoría anual
- **Qué quiere saber realmente:** Prueba la capacidad forense y el cumplimiento de retención.
- **Una respuesta sólida incluye:** Política de retención por fuente, cobertura, integridad y pruebas de reconstrucción.
- **Señal de alerta:** Retención corta decidida por costo, sin análisis de riesgo.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** A08.7 (¿Qué retención y calidad de registros necesitamos para investigaciones…) · B09.4 (¿Podemos reconstruir de forma forense una cadena de acciones de varios…) · A08.1 (¿Qué cobertura de telemetría tiene el SOC (identidad, endpoint, correo…)
- **Apoyo de Microsoft:** Lago de datos de Microsoft Sentinel (retención de largo plazo a menor costo).
- **Marcos (heredados):** NIST — CSF DE.CM, CSF RS.AN | CIS — CIS 8, CIS 13 | The Open Group — sin correspondencia directa | ISACA — COBIT DSS05, COBIT MEA03, COBIT DSS02 | CSA — CCM LOG, CCM SEF, AICM SEF

#### C09.8 · ¿Qué hallazgos se repiten y qué dicen de la causa raíz?

- **Quién pregunta:** Auditor interno · **Cuándo:** Informe anual de auditoría
- **Qué quiere saber realmente:** Busca problemas estructurales detrás de los síntomas.
- **Una respuesta sólida incluye:** Análisis de reincidencias, causas raíz (procesos, recursos, arquitectura) y acciones estructurales.
- **Señal de alerta:** Cerrar síntomas.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** A09.9 (¿Convertimos los incidentes, cuasi incidentes y ejercicios en cambios…) · A10.9 (¿Qué nivel de madurez queremos alcanzar por dominio y cómo medimos la…) · A08.6 (¿Qué incidentes y configuraciones erróneas del último año se explican,…) — nueva en la v2.0
- **Apoyo de Microsoft:** Sin capacidad específica: es análisis de gestión.
- **Marcos (heredados):** NIST — CSF ID.IM, CSF RC.RP, CSF RS.AN | CIS — CIS 17, CIS IG1, CIS 14 | The Open Group — TOGAF | ISACA — COBIT DSS03, COBIT BAI08, COBIT MEA01 | CSA — CCM SEF, STAR, CCM HRS

#### C09.9 · Cuando un agente ejecutó una acción en nombre de un usuario, ¿pueden demostrar quién hizo qué?

- **Quién pregunta:** Auditor de IA · **Cuándo:** Auditoría de IA · **Tema:** IA y agentes
- **Qué quiere saber realmente:** Prueba la atribución y la trazabilidad de las acciones delegadas.
- **Una respuesta sólida incluye:** Registros correlacionables (usuario solicitante, identidad del agente, herramienta, datos y resultado), atribución, retención y pruebas.
- **Señal de alerta:** Acciones registradas solo con la cuenta del usuario o con una cuenta de servicio genérica.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** B04.1 (¿Cada agente tiene una identidad propia, distinguible de la de persona…) · B04.2 (¿Cuándo actúa un agente en nombre de un usuario y cuándo con autoridad…) · B09.1 (¿Registramos de forma correlacionable quién pidió qué, qué hizo el age…)
- **Apoyo de Microsoft:** Entra Agent ID; Purview Audit (actividad de Copilot y agentes).
- **Marcos (heredados):** NIST — CSF PR.AA, AI RMF GOVERN 1, AI RMF GOVERN 3 | CIS — guía CIS para agentes de IA, CIS 5, CIS 6 | The Open Group — Zero Trust Commandments | ISACA — COBIT DSS05, AAISM D3, COBIT DSS06 | CSA — AICM IAM, AICM LOG, MAESTRO

### C10 · Clientes, socios, aseguradoras e inversores

Los terceros externos preguntan si pueden confiar: compartir datos, integrarse, asegurar o invertir. Esperan respuestas consistentes, verificables y rápidas.

#### C10.1 · ¿Qué certificaciones e informes independientes pueden compartirnos?

- **Quién pregunta:** Cliente corporativo · **Cuándo:** Contratación y renovación
- **Qué quiere saber realmente:** Quiere evidencia de terceros, no autodeclaraciones.
- **Una respuesta sólida incluye:** Certificaciones vigentes con su alcance, informes de aseguramiento, cartas puente y centro de confianza.
- **Señal de alerta:** Certificaciones con un alcance que no cubre el servicio contratado.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** B10.8 (¿Cómo demostramos a clientes, auditores y reguladores que nuestra IA e…) · A10.8 (¿Cómo verificamos el cumplimiento de nuestros proveedores cloud y qué…)
- **Apoyo de Microsoft:** Service Trust Portal; programa CSA STAR, incluido STAR for AI.
- **Marcos (heredados):** NIST — AI RMF GOVERN 4, AI RMF MEASURE 2, CSF GV.SC | CIS — CIS 15 | The Open Group — sin correspondencia directa | ISACA — COBIT MEA04, COBIT EDM05, COBIT APO10 | CSA — STAR, AICM A&A, CCM STA

#### C10.2 · ¿Usan IA con nuestros datos? ¿Cómo los protegen?

- **Quién pregunta:** Cliente corporativo · **Cuándo:** Contratación y renovación · **Tema:** IA y agentes
- **Qué quiere saber realmente:** Quiere transparencia y controles concretos.
- **Una respuesta sólida incluye:** Casos de uso con datos de clientes, controles (aislamiento, etiquetas, DLP, no entrenamiento), contratos con los proveedores de IA y transparencia.
- **Señal de alerta:** Respuestas genéricas o contradictorias entre áreas.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** B10.6 (¿Somos transparentes con clientes y empleados sobre cuándo interactúan…) · B05.2 (¿Las etiquetas de confidencialidad y sus permisos de uso se respetan c…) · B05.9 (¿Qué compromisos contractuales tenemos de nuestros proveedores de IA s…)
- **Apoyo de Microsoft:** Protección de datos empresariales de Microsoft 365 Copilot; etiquetas de confidencialidad aplicadas a Copilot.
- **Marcos (heredados):** NIST — AI RMF MEASURE 2, AI RMF MAP 5, AI 600-1 | CIS — CIS 3, CIS 15 | The Open Group — sin correspondencia directa | ISACA — COBIT EDM05, COBIT MEA03, COBIT APO14 | CSA — AICM DSP, AICM GRC, AICM STA

#### C10.3 · ¿Tienen MFA en todos los accesos remotos y administrativos, copias de seguridad inmutables y EDR en todos los equipos?

- **Quién pregunta:** Aseguradora · **Cuándo:** Renovación de la póliza
- **Qué quiere saber realmente:** Quiere cobertura medida de los controles que más reducen los siniestros.
- **Una respuesta sólida incluye:** Cobertura medida de cada control (porcentaje y excepciones) y evidencia exportable.
- **Señal de alerta:** Declarar «sí» sin medir u ocultar excepciones.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** A04.1 (¿Qué porcentaje de usuarios, administradores y accesos externos usa au…) · A09.3 (¿Nuestras copias de seguridad son inmutables, aisladas, cifradas y est…) · A06.5 (¿Cómo protegemos endpoints y servidores (detección y respuesta en modo…) · A06.1 (¿Tenemos un inventario confiable y actualizado de dispositivos, cargas…)
- **Apoyo de Microsoft:** Secure Score; informes de métodos de autenticación de Entra; cobertura de Microsoft Defender for Endpoint.
- **Marcos (heredados):** NIST — CSF PR.AA, CSF PR.DS, CSF PR.IR | CIS — CIS 2, CIS 6, CIS 11 | The Open Group — Zero Trust Commandments, TOGAF | ISACA — COBIT DSS05, COBIT DSS04, COBIT BAI09 | CSA — CCM UEM, CCM IAM, CCM BCR

#### C10.4 · ¿Cómo gobiernan el riesgo cibernético y qué incidentes materiales tuvieron?

- **Quién pregunta:** Inversor o agencia de calificación · **Cuándo:** Reporte anual y calificación
- **Qué quiere saber realmente:** Evalúa la calidad del gobierno y la consistencia de la información pública.
- **Una respuesta sólida incluye:** Estructura de gobierno, experiencia del directorio, procesos, incidentes divulgados y consistencia con los informes públicos.
- **Señal de alerta:** Divulgaciones genéricas o inconsistentes.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** A01.4 (¿Con qué frecuencia, formato y métricas supervisa el directorio el rie…) · A09.5 (¿Cómo se gestiona una crisis cibernética: comité, roles, decisiones di…) · A11.6 (¿Cómo comunicamos el riesgo cibernético en lenguaje de negocio a cada…)
- **Apoyo de Microsoft:** Sin capacidad específica: es información de gobierno corporativo.
- **Marcos (heredados):** NIST — CSF GV.OV, CSF GV.RR, CSF RS.MA | CIS — CIS 17 | The Open Group — Open FAIR | ISACA — COBIT EDM05, COBIT MEA01, COBIT DSS02 | CSA — CCM GRC, CCM SEF, CCM BCR

#### C10.5 · Si nos conectamos a sus sistemas o APIs, ¿qué controles nos exigen y qué nos garantizan?

- **Quién pregunta:** Socio de negocio · **Cuándo:** Integración con un socio
- **Qué quiere saber realmente:** Quiere reglas claras y recíprocas para la integración.
- **Una respuesta sólida incluye:** Requisitos de integración (autenticación, mínimo privilegio, cifrado, monitoreo), responsabilidades, notificación mutua y pruebas.
- **Señal de alerta:** Integraciones con credenciales compartidas.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** A07.8 (¿Cómo protegemos las APIs y la lógica de negocio expuesta (autorizació…) · A07.6 (¿Qué exigimos contractualmente a los proveedores (notificación de inci…)
- **Apoyo de Microsoft:** Identidades externas en Microsoft Entra; Azure API Management.
- **Marcos (heredados):** NIST — CSF PR.PS, CSF DE.CM, CSF GV.SC | CIS — CIS 16, CIS 13, CIS 15 | The Open Group — TOGAF | ISACA — COBIT BAI03, COBIT DSS05, COBIT APO09 | CSA — CCM AIS, CCM STA, CCM IPY

#### C10.6 · Si sufren un incidente que afecta nuestros datos, ¿cuándo y cómo nos enteramos?

- **Quién pregunta:** Cliente · **Cuándo:** Contratación
- **Qué quiere saber realmente:** Quiere compromisos de notificación concretos.
- **Una respuesta sólida incluye:** Compromisos de notificación con plazos, contenido y canales, y ejemplos de cómo se aplicaron.
- **Señal de alerta:** Compromisos vagos.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** A08.4 (¿Tenemos un plan de respuesta a incidentes vigente y ensayado con la d…) · A07.6 (¿Qué exigimos contractualmente a los proveedores (notificación de inci…)
- **Apoyo de Microsoft:** Sin capacidad específica: es un compromiso contractual.
- **Marcos (heredados):** NIST — CSF RS.MA, CSF RS.CO, SP 800-61 | CIS — CIS 17, CIS 15 | The Open Group — sin correspondencia directa | ISACA — COBIT DSS02, COBIT DSS04, COBIT APO09 | CSA — CCM SEF, CCM STA, CCM IPY

#### C10.7 · ¿Qué riesgos de seguridad conocidos siguen sin resolver y qué incidentes tuvieron en los últimos años?

- **Quién pregunta:** Inversor en un proceso de due diligence · **Cuándo:** Fusión, adquisición o inversión
- **Qué quiere saber realmente:** Busca pasivos ocultos que afecten la valuación.
- **Una respuesta sólida incluye:** Riesgos aceptados y su vencimiento, incidentes y su resolución, hallazgos abiertos, deuda técnica y plan de remediación.
- **Señal de alerta:** Ocultar o minimizar riesgos conocidos.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** A02.5 (¿Cada aceptación de riesgo tiene dueño, alcance, evidencia, vencimient…) · A09.9 (¿Convertimos los incidentes, cuasi incidentes y ejercicios en cambios…) · A03.5 (¿Cómo gestionamos la deuda técnica y los sistemas heredados que no pue…)
- **Apoyo de Microsoft:** Exposure Management y Secure Score como evidencia de postura.
- **Marcos (heredados):** NIST — CSF ID.RA, CSF GV.RM, CSF ID.IM | CIS — CIS RAM, CIS 17, CIS 2 | The Open Group — TOGAF, Open FAIR | ISACA — COBIT APO12, COBIT APO10, COBIT DSS03 | CSA — CCM GRC, CCM SEF, CCM TVM

#### C10.8 · ¿Sus agentes de IA pueden interactuar con los nuestros de forma segura?

- **Quién pregunta:** Cliente corporativo · **Cuándo:** Integración con un socio · **Tema:** IA y agentes
- **Qué quiere saber realmente:** Anticipa ecosistemas de agentes entre empresas.
- **Una respuesta sólida incluye:** Autenticación mutua, autorización, límites, registro, protocolos (MCP y agente a agente) y responsabilidades de cada parte.
- **Señal de alerta:** Integración sin verificar la identidad del agente externo.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** B04.9 (¿Cómo verificamos la identidad de quien interactúa con nuestros agente…) · B04.7 (¿Cómo controlamos la delegación entre agentes para que no se escalen p…) · B06.2 (¿Cómo nos protegemos de la inyección indirecta de instrucciones desde…)
- **Apoyo de Microsoft:** Entra Agent ID; guía de seguridad para MCP.
- **Marcos (heredados):** NIST — CSF PR.AA, AI RMF MAP 4, AI RMF GOVERN 3 | CIS — guía CIS para agentes de IA, CIS 6, CIS 16 | The Open Group — Zero Trust Commandments | ISACA — COBIT DSS05, AAISM D3, COBIT DSS06 | CSA — AICM IAM, AICM AIS, MAESTRO

#### C10.9 · ¿Qué controles tienen sobre la IA y los agentes que podrían generar reclamos?

- **Quién pregunta:** Aseguradora · **Cuándo:** Renovación de la póliza · **Tema:** IA y agentes
- **Qué quiere saber realmente:** Las aseguradoras empiezan a preguntar por la IA como fuente de siniestros.
- **Una respuesta sólida incluye:** Inventario, gobierno, controles técnicos, incidentes y transparencia.
- **Señal de alerta:** No tener respuesta.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** B01.6 (¿Qué usos de IA están prohibidos o requieren aprobación reforzada por…) · B07.2 (¿Tenemos un perfil de radio de impacto por agente (datos, herramientas…) · B08.8 (¿Qué indicadores de confianza en la IA presentamos al directorio (inci…)
- **Apoyo de Microsoft:** Silencio parcial: Microsoft no publica una postura sobre seguros; Agent 365 y Purview aportan evidencia.
- **Marcos (heredados):** NIST — AI RMF MAP 5, AI RMF GOVERN 1, AI 600-1 | CIS — guía CIS para agentes de IA, CIS RAM | The Open Group — Open FAIR | ISACA — AAISM D2, COBIT EDM03, COBIT MEA03 | CSA — AICM GRC, MAESTRO

### C11 · Personas: colaboradores, RR. HH. y el equipo de seguridad

Las personas preguntan qué pueden hacer, qué se espera de ellas y qué pasa con su trabajo. El equipo de seguridad pregunta por prioridades, carga y futuro profesional.

#### C11.1 · ¿Qué herramientas de IA puedo usar en mi trabajo y con qué datos?

- **Quién pregunta:** Colaborador · **Cuándo:** Comunicación interna · **Tema:** IA y agentes
- **Qué quiere saber realmente:** Quiere reglas simples y una herramienta autorizada.
- **Una respuesta sólida incluye:** Lista clara de herramientas autorizadas, ejemplos de datos permitidos y prohibidos, canal de consulta y alternativas.
- **Señal de alerta:** Una política extensa e incomprensible.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** B02.4 (¿Tenemos una política de uso aceptable de IA que defina servicios auto…) · B02.9 (¿Cómo formamos a cada audiencia (directorio, desarrolladores, usuarios…)
- **Apoyo de Microsoft:** Microsoft 365 Copilot y Copilot Chat con protección de datos empresariales.
- **Marcos (heredados):** NIST — AI RMF GOVERN 1, CSF PR.AT, AI RMF GOVERN 2 | CIS — CIS 14, CIS 2 | The Open Group — sin correspondencia directa | ISACA — COBIT APO01, COBIT APO14, AAISM D1 | CSA — AICM HRS, AICM GRC

#### C11.2 · Si cometo un error, como hacer clic en un enlace malicioso, ¿me van a sancionar?

- **Quién pregunta:** Colaborador · **Cuándo:** Comunicación interna
- **Qué quiere saber realmente:** Necesita confianza para reportar rápido.
- **Una respuesta sólida incluye:** Cultura de reporte sin culpa, canal rápido, qué pasa después, y cuándo hay consecuencias (negligencia reiterada o intención).
- **Señal de alerta:** Una cultura punitiva que oculta incidentes.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** A11.1 (¿Qué conductas de seguridad esperamos de cada rol, cómo medimos el cam…)
- **Apoyo de Microsoft:** Sin capacidad específica: es cultura y política de personas.
- **Marcos (heredados):** NIST — CSF PR.AT, CSF GV.RR | CIS — CIS 14 | The Open Group — sin correspondencia directa | ISACA — COBIT APO07, COBIT BAI05, COBIT EDM01 | CSA — CCM HRS

#### C11.3 · ¿Cómo participan seguridad y RR. HH. en las altas, cambios y bajas de personas?

- **Quién pregunta:** Director de RR. HH. · **Cuándo:** Revisión de procesos de RR. HH.
- **Qué quiere saber realmente:** Quiere un proceso integrado que no deje accesos ni agentes huérfanos.
- **Una respuesta sólida incluye:** Proceso integrado del ciclo de vida de identidades, plazos de revocación, cambios de rol, salidas de alto riesgo y reasignación de los agentes cuyo dueño se va.
- **Señal de alerta:** Accesos activos de ex empleados o agentes huérfanos.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** A04.5 (¿Cómo gobernamos el ciclo de vida de las identidades (alta, cambio, ba…) · B03.7 (¿Cómo detectamos agentes huérfanos, inactivos o cuyo dueño dejó la org…) · A05.4 (¿Cómo gestionamos el riesgo interno, negligente o malicioso, con propo…)
- **Apoyo de Microsoft:** Flujos de ciclo de vida de Entra ID Governance; tareas de patrocinio de agentes.
- **Marcos (heredados):** NIST — CSF PR.AA, AI RMF GOVERN 1, CSF PR.DS | CIS — CIS 5, CIS 6, guía CIS para agentes de IA | The Open Group — sin correspondencia directa | ISACA — COBIT DSS05, COBIT APO07, COBIT BAI09 | CSA — CCM HRS, CCM IAM, AICM IAM

#### C11.4 · ¿La IA va a reemplazar mi puesto?

- **Quién pregunta:** Analista del SOC · **Cuándo:** Adopción de IA en el SOC · **Tema:** IA y agentes
- **Qué quiere saber realmente:** Necesita claridad sobre su futuro profesional.
- **Una respuesta sólida incluye:** Tareas que cambian, nuevas habilidades, plan de reconversión, criterios de supervisión humana y carrera.
- **Señal de alerta:** Silencio o promesas vacías.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** B11.8 (¿Qué roles del equipo de seguridad cambian con la IA agéntica y cuál e…) · B11.5 (¿Cómo evitamos que los analistas pierdan habilidades críticas o confíe…) · A11.3 (¿Tenemos un plan de talento de seguridad (brechas de habilidades, suce…)
- **Apoyo de Microsoft:** Agentes de Security Copilot para tareas repetitivas; SAF advierte no delegar el pensamiento crítico en la IA.
- **Marcos (heredados):** NIST — CSF GV.RR, CSF PR.AT, AI RMF GOVERN 2 | CIS — CIS 14 | The Open Group — Roles de seguridad | ISACA — COBIT APO07, COBIT BAI05 | CSA — AICM HRS, CCM HRS

#### C11.5 · ¿Cuáles son nuestras tres prioridades y qué dejamos de hacer?

- **Quién pregunta:** Equipo de seguridad · **Cuándo:** Planificación anual del equipo
- **Qué quiere saber realmente:** Quiere foco y permiso para no hacerlo todo.
- **Una respuesta sólida incluye:** Prioridades vinculadas al riesgo, lo que se deja de hacer o se automatiza, y los criterios de esa decisión.
- **Señal de alerta:** Todo es prioridad.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** A03.9 (¿Tenemos una hoja de ruta de seguridad a 12–36 meses priorizada por ri…) · A08.8 (¿Cómo está organizado el SOC (roles, niveles, turnos, servicios gestio…) · A11.9 (¿Cómo evalúa el equipo de seguridad el liderazgo del CISO (comunicar e…) — nueva en la v2.0
- **Apoyo de Microsoft:** Sin capacidad específica: es liderazgo.
- **Marcos (heredados):** NIST — CSF ID.IM, CSF GV.RR, CSF DE.AE | CIS — CIS IG1, CIS 17 | The Open Group — TOGAF, Roles de seguridad | ISACA — COBIT APO07, COBIT APO02, COBIT APO05 | CSA — CCM HRS, CCM GRC, CCM SEF

#### C11.6 · ¿Cómo vamos a reducir el volumen de alertas y el desgaste del equipo?

- **Quién pregunta:** Analista del SOC · **Cuándo:** Revisión del SOC · **Tema:** IA y agentes
- **Qué quiere saber realmente:** La sostenibilidad del equipo es un riesgo operativo.
- **Una respuesta sólida incluye:** Ingeniería de detección, automatización, agentes de clasificación supervisados, turnos e indicadores de carga y bienestar.
- **Señal de alerta:** Aceptar el desgaste como normal.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** A08.8 (¿Cómo está organizado el SOC (roles, niveles, turnos, servicios gestio…) · A11.4 (¿Cómo prevenimos el desgaste del CISO y del equipo, qué indicadores de…) · B11.1 (¿Qué tareas de seguridad automatizamos con IA (clasificación, investig…)
- **Apoyo de Microsoft:** Security Alert Triage Agent (disponible de forma general); interrupción automática de ataques.
- **Marcos (heredados):** NIST — CSF GV.RR, CSF DE.AE, CSF ID.IM | CIS — CIS 17 | The Open Group — Roles de seguridad | ISACA — COBIT APO07, COBIT DSS01, COBIT DSS02 | CSA — CCM HRS, CCM SEF, AICM GRC

#### C11.7 · ¿Puedo usar asistentes de código con IA y qué controles hay sobre el código que generan?

- **Quién pregunta:** Desarrollador · **Cuándo:** Adopción de asistentes de código · **Tema:** IA y agentes
- **Qué quiere saber realmente:** Quiere usar la herramienta sin asumir riesgos ocultos.
- **Una respuesta sólida incluye:** Herramientas autorizadas, revisión de código, análisis de seguridad, gestión de secretos, licencias y responsabilidad del desarrollador.
- **Señal de alerta:** Código generado sin revisión.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** B03.8 (¿Qué visibilidad tenemos del uso de IA en endpoints y entornos de desa…) · A07.3 (¿Está integrada la seguridad en el ciclo de desarrollo (modelado de am…) · B10.7 (¿Cómo gestionamos los riesgos de propiedad intelectual y derechos de a…)
- **Apoyo de Microsoft:** Seguridad de DevOps en Defender for Cloud.
- **Marcos (heredados):** NIST — CSF PR.PS, CSF ID.AM, AI RMF GOVERN 1 | CIS — CIS 2, CIS 10, CIS 16 | The Open Group — TOGAF, Security Design Patterns | ISACA — COBIT BAI09, COBIT DSS05, COBIT BAI03 | CSA — AICM UEM, CCM AIS, AICM GRC

#### C11.8 · ¿Cómo me doy cuenta de que un correo, una llamada o un video es un deepfake?

- **Quién pregunta:** Colaborador · **Cuándo:** Comunicación interna · **Tema:** IA y agentes
- **Qué quiere saber realmente:** Necesita un procedimiento práctico, no solo señales técnicas.
- **Una respuesta sólida incluye:** Señales de alerta, procedimiento de verificación fuera de banda, palabras clave para transacciones, reporte y ejercicios.
- **Señal de alerta:** Delegar todo en la tecnología.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** A11.2 (¿Cómo preparamos a ejecutivos y áreas de alto riesgo (finanzas, tesore…) · B06.8 (¿Cómo nos defendemos de atacantes que usan IA (phishing personalizado,…)
- **Apoyo de Microsoft:** Microsoft Defender for Office 365 (protección contra suplantación).
- **Marcos (heredados):** NIST — CSF PR.AT, CSF PR.AA, CSF ID.RA | CIS — CIS 14, CIS 9, CIS 7 | The Open Group — Open FAIR | ISACA — COBIT APO07, COBIT DSS06, COBIT APO12 | CSA — CCM HRS, AICM TVM

#### C11.9 · ¿Qué pasa si el CISO no está? ¿Quién decide?

- **Quién pregunta:** Miembro del equipo de seguridad · **Cuándo:** Ejercicio de crisis
- **Qué quiere saber realmente:** Pregunta por la resiliencia del liderazgo.
- **Una respuesta sólida incluye:** Suplencias, delegación de facultades, documentación y ejercicios con los suplentes.
- **Señal de alerta:** Decisiones concentradas en una persona.
- **Cómo prepararse (marco 99 + 99, versión 2.0):** A11.7 (¿Qué capacidades críticas dependen de una sola persona o de un único p…) · A01.3 (¿Qué decisiones de riesgo puede tomar el CISO por sí mismo, cuáles cor…) · A11.4 (¿Cómo prevenimos el desgaste del CISO y del equipo, qué indicadores de…)
- **Apoyo de Microsoft:** Sin capacidad específica: es gobierno de la función.
- **Marcos (heredados):** NIST — CSF GV.RR, CSF PR.AA, CSF GV.RM | CIS — CIS 5, CIS 6, CIS RAM | The Open Group — TOGAF, Open FAIR | ISACA — COBIT APO07, COBIT BAI08, COBIT EDM03 | CSA — CCM HRS, CCM IAM, CCM GRC

## 7. Matriz de preparación: del marco 99 + 99 a las respuestas

### 7.1 Las preguntas del marco que más respuestas preparan

Responder primero estas preguntas del marco tiene el mayor efecto multiplicador: cada una alimenta varias respuestas a distintos interlocutores.

| Pregunta del marco | Texto | Respuestas que prepara | Interlocutores |
|---|---|---|---|
| A02.5 | ¿Cada aceptación de riesgo tiene dueño, alcance, evidencia, vencimiento y disparadores de revisión, y cada transferencia (seguros, contratos) cubre los escenarios reales con controles que podemos demostrar? | 6 | C01 Directorio, C02 Comité de auditoría y riesgos, C03 CEO y comité ejecutivo, C04 CFO, finanzas y tesorería, C10 Clientes, socios, aseguradoras e inversores |
| A07.6 | ¿Qué exigimos contractualmente a los proveedores (notificación de incidentes, derecho de auditoría, continuidad, subcontratistas, salida)? | 5 | C02 Comité de auditoría y riesgos, C05 Negocio y producto, C07 Legal, cumplimiento y privacidad, C10 Clientes, socios, aseguradoras e inversores |
| A09.5 | ¿Cómo se gestiona una crisis cibernética: comité, roles, decisiones difíciles (incluido el pago de rescates), comunicación y notificaciones? | 5 | C01 Directorio, C02 Comité de auditoría y riesgos, C03 CEO y comité ejecutivo, C10 Clientes, socios, aseguradoras e inversores |
| A10.3 | ¿Cuánta de nuestra evidencia de cumplimiento es automática y continua, cuánta depende de muestreos manuales y qué podríamos entregar en 48 horas a un regulador o auditor sobre un incidente o un control específico? | 5 | C02 Comité de auditoría y riesgos, C04 CFO, finanzas y tesorería, C05 Negocio y producto, C09 Auditoría interna, auditoría externa y certificadores |
| A02.2 | ¿Cuáles son nuestras joyas de la corona (procesos, datos, sistemas e identidades) y qué escenarios de pérdida material las amenazan, según los adversarios relevantes para nuestro sector y país? | 4 | C01 Directorio, C02 Comité de auditoría y riesgos, C03 CEO y comité ejecutivo, C04 CFO, finanzas y tesorería |
| A09.9 | ¿Convertimos los incidentes, cuasi incidentes y ejercicios en cambios de arquitectura verificados? | 4 | C02 Comité de auditoría y riesgos, C08 Reguladores y supervisores, C09 Auditoría interna, auditoría externa y certificadores, C10 Clientes, socios, aseguradoras e inversores |
| A10.1 | ¿Qué obligaciones legales, regulatorias y contractuales de seguridad nos aplican por país y sector, incluidas las de resiliencia operativa digital que nos alcanzan directa o indirectamente (DORA, NIS2 o normas locales), y quién mantiene ese mapa y el plan para cumplirlas? | 4 | C01 Directorio, C02 Comité de auditoría y riesgos, C07 Legal, cumplimiento y privacidad |
| A10.2 | ¿Cómo convertimos varios marcos y regulaciones en un único conjunto de controles con evidencia reutilizable? | 4 | C02 Comité de auditoría y riesgos, C04 CFO, finanzas y tesorería, C05 Negocio y producto, C07 Legal, cumplimiento y privacidad |
| A10.9 | ¿Qué nivel de madurez queremos alcanzar por dominio y cómo medimos la distancia con evidencia y no con autoevaluaciones? | 4 | C01 Directorio, C02 Comité de auditoría y riesgos, C09 Auditoría interna, auditoría externa y certificadores |
| A11.2 | ¿Cómo preparamos a ejecutivos y áreas de alto riesgo (finanzas, tesorería, RR. HH., asistentes) frente a suplantaciones avanzadas, incluidas voz y video sintéticos? | 4 | C03 CEO y comité ejecutivo, C04 CFO, finanzas y tesorería, C11 Personas: colaboradores, RR. HH. y el equipo de seguridad |
| A11.7 | ¿Qué capacidades críticas dependen de una sola persona o de un único proveedor, y cómo reducimos esa concentración? | 4 | C01 Directorio, C08 Reguladores y supervisores, C11 Personas: colaboradores, RR. HH. y el equipo de seguridad |
| A01.3 | ¿Qué decisiones de riesgo puede tomar el CISO por sí mismo, cuáles corresponden al comité ejecutivo y cuáles al directorio? | 3 | C01 Directorio, C11 Personas: colaboradores, RR. HH. y el equipo de seguridad |
| A01.4 | ¿Con qué frecuencia, formato y métricas supervisa el directorio el riesgo cibernético, y qué decisiones concretas tomó en los últimos doce meses? | 3 | C01 Directorio, C08 Reguladores y supervisores, C10 Clientes, socios, aseguradoras e inversores |
| A01.7 | ¿Cómo justificamos el presupuesto de seguridad por reducción de exposición y cómo evitamos la proliferación de herramientas superpuestas? | 3 | C01 Directorio, C04 CFO, finanzas y tesorería |
| A03.5 | ¿Cómo gestionamos la deuda técnica y los sistemas heredados que no pueden actualizarse: aislar, reemplazar o aceptar? | 3 | C03 CEO y comité ejecutivo, C06 Tecnología, datos e IA, C10 Clientes, socios, aseguradoras e inversores |

### 7.2 Cobertura por interlocutor

| Interlocutor | Preguntas de la Parte A que lo preparan | Preguntas de la Parte B | Total distinto |
|---|---|---|---|
| C01 Directorio | 20 | 13 | 33 |
| C02 Comité de auditoría y riesgos | 21 | 12 | 33 |
| C03 CEO y comité ejecutivo | 18 | 9 | 27 |
| C04 CFO, finanzas y tesorería | 15 | 7 | 22 |
| C05 Negocio y producto | 12 | 14 | 26 |
| C06 Tecnología, datos e IA | 10 | 16 | 26 |
| C07 Legal, cumplimiento y privacidad | 10 | 10 | 20 |
| C08 Reguladores y supervisores | 16 | 10 | 26 |
| C09 Auditoría interna, auditoría externa y certificadores | 9 | 13 | 22 |
| C10 Clientes, socios, aseguradoras e inversores | 14 | 10 | 24 |
| C11 Personas: colaboradores, RR. HH. y el equipo de seguridad | 12 | 9 | 21 |

### 7.3 El trabajo invisible: preguntas del marco que ningún interlocutor pide

35 de las 198 preguntas del marco no aparecen como preparación de ninguna pregunta de los interlocutores. No significa que sobren: sostienen la capacidad de responder en el futuro (arquitectura, ingeniería de detección, cultura, desarrollo del criterio del CISO) y suelen ser las primeras en postergarse cuando nadie las reclama. Conviene revisarlas una vez por semestre con el núcleo del COE.

| Dominio | Preguntas no demandadas |
|---|---|
| A03 Arquitectura, estrategia técnica y Zero Trust | A03.6, A03.8 |
| A04 Identidad y acceso privilegiado | A04.3, A04.6, A04.7, A04.9 |
| A05 Datos, privacidad y criptografía | A05.6, A05.7, A05.8, A05.9 |
| A06 Exposición: activos, configuración y vulnerabilidades | A06.7 |
| A07 Nube, aplicaciones, terceros y cadena de suministro | A07.1, A07.2, A07.4 |
| A08 Operaciones de seguridad: detección, respuesta y caza | A08.5 |
| A09 Resiliencia, continuidad, recuperación y crisis | A09.7 |
| B01 Estrategia, valor y apetito de riesgo de la IA | B01.4 |
| B04 Identidad, autoridad y delegación de agentes | B04.5 |
| B05 Datos para la IA: exposición, protección y ciclo de vida | B05.6, B05.7 |
| B06 Amenazas a modelos, aplicaciones y agentes | B06.1, B06.3, B06.7, B06.9 |
| B07 Autonomía, supervisión humana y contención | B07.4, B07.8 |
| B09 Observabilidad, detección y respuesta a incidentes de IA | B09.2, B09.6, B09.8, B09.9 |
| B10 Regulación, terceros y confianza | B10.5 |
| B11 IA para la seguridad: SOC agéntico y fuerza laboral digital | B11.2, B11.3, B11.6, B11.9 |

### 7.4 Vínculo con las 24 preguntas prioritarias para el directorio

Las preguntas del directorio (C01) y del comité de auditoría y riesgos (C02) se apoyan en 17 de las 24 preguntas que el marco 99 + 99 marca como prioritarias para el directorio: A01.3, A01.4, A02.1, A02.2, A02.6, A07.5, A08.4, A09.2, A09.5, B01.1, B01.2, B02.1, B02.2, B03.1, B07.1, B07.2, B08.8. Las demás preguntas prioritarias preparan respuestas para otros interlocutores o anticipan temas que el directorio todavía no formula.

## 8. Escala de preparación

La matriz de Excel permite calificar cada respuesta con una escala de cinco niveles, alineada con la escala de evidencia del AI CISO Atlas. Como en el marco, los niveles no se promedian: se muestran el mínimo, los ceros y la proporción en nivel 3 o superior.

| Nivel | Nombre | Criterio |
|---|---|---|
| 0 | Sin respuesta | No hay respuesta preparada ni evidencia. |
| 1 | Respuesta declarativa | Existe una respuesta verbal o documental, sin evidencia que la respalde. |
| 2 | Con evidencia parcial | La respuesta tiene evidencia, pero incompleta, manual o desactualizada. |
| 3 | Ensayada y verificable | La respuesta tiene evidencia completa y fue ensayada frente a un par o en un simulacro. |
| 4 | Sostenida | La evidencia se produce de forma continua y la respuesta es consistente entre audiencias. |

## 9. Lo que Microsoft aporta para responder

Microsoft no responde por el CISO, pero varias de sus capacidades producen la evidencia que las respuestas necesitan. La tabla agrupa las capacidades citadas en el cuestionario por el tipo de evidencia que aportan. El estado de cada capacidad (disponibilidad general, versión preliminar, licenciamiento) está verificado al 6 de noviembre de 2026 en el marco 99 + 99 y debe revalidarse antes de comunicarlo a un cliente.

| Tipo de evidencia | Preguntas | Dónde se cita |
|---|---|---|
| Exposición y postura | 15 | C01.1, C01.2, C01.3, C01.8, C02.3, C02.4, C03.4, C04.1, C04.2, C04.5, C06.7, C07.9, C08.6, C10.3, C10.7 |
| Identidad y agentes | 20 | C01.4, C03.3, C03.6, C03.8, C03.9, C04.6, C05.4, C05.8, C06.4, C06.5, C06.6, C08.5, C08.8, C09.1, C09.3, C09.9, C10.5, C10.8, C10.9, C11.3 |
| Datos e IA | 29 | C01.4, C01.5, C01.8, C02.1, C02.5, C02.9, C03.3, C03.7, C03.9, C04.7, C05.1, C05.4, C05.8, C06.3, C06.4, C06.8, C06.9, C07.2, C07.3, C07.5, C07.8, C08.5, C08.7, C09.2, C09.3, C09.5, C09.9, C10.9, C11.1 |
| Operaciones de seguridad | 26 | C01.1, C01.3, C01.6, C01.9, C02.4, C02.8, C03.2, C04.3, C04.4, C04.6, C04.8, C05.1, C05.2, C05.5, C05.7, C05.8, C07.2, C08.4, C09.2, C09.4, C09.7, C10.3, C11.4, C11.6, C11.7, C11.8 |
| Cumplimiento y confianza | 18 | C01.8, C02.1, C02.5, C02.7, C04.5, C04.7, C04.9, C05.3, C05.9, C07.4, C07.6, C07.7, C07.9, C08.3, C08.5, C09.2, C09.6, C10.1 |
| Marcos de trabajo y referencia | 8 | C01.2, C01.6, C02.8, C03.1, C05.2, C06.1, C06.2, C11.4 |

En 14 preguntas la respuesta no depende de una capacidad tecnológica sino de una decisión de gobierno, un proceso legal o una práctica de personas: C01.7, C02.2, C02.6, C03.5, C07.1, C08.1, C08.2, C08.9, C09.8, C10.4, C10.6, C11.2, C11.5, C11.9. En 2 preguntas Microsoft no publica una postura específica y el cuestionario lo declara como silencio: C04.5, C10.9.

## 10. Silencios, límites y vigencia

- **Seguros cibernéticos.** Microsoft no publica una postura específica sobre seguros; la evidencia de controles puede respaldar la negociación con la aseguradora (C04.5 y C10.9).
- **Preguntas sin respaldo tecnológico.** Las respuestas sobre gobierno, comunicación de crisis, notificación legal, competencias y sucesión dependen de decisiones de la organización; ninguna capacidad las reemplaza.
- **Interlocutores y regulación por país.** Las preguntas de reguladores y de Legal son genéricas: cada país y sector de México, Centroamérica y Sudamérica tiene normas y plazos propios que deben verificarse con Legal.
- **Disponibilidad de las capacidades.** Algunas capacidades citadas están en versión preliminar (por ejemplo, el registro de servidores MCP propios en Agent 365) o tienen la disponibilidad general sin confirmar (acceso condicional para agentes). Revalidar después de Microsoft Ignite 2026.
- **Marcos heredados.** Los códigos de NIST, CIS, The Open Group, ISACA y CSA se heredan de las preguntas de preparación; son correspondencias temáticas, no equivalencias de control. The Open Group no tiene correspondencia en una parte de las preguntas porque no publica un estándar de seguridad de IA.
- **Método.** Las preguntas surgen de la práctica de asesoramiento a CISOs y de los documentos base; no provienen de una encuesta a interlocutores. El proceso inverso desde los marcos (NIST, ISACA, ISC2, CIS, The Open Group y CSA) es un trabajo complementario.

## 11. Fuentes

**Documentos base:** AI CISO Atlas v3.0; TheNextCISO — marco integrado; Security Adoption Framework (SAF) — AI Security Strategy & Governance; marco «99 + 99 preguntas que un CISO tiene que hacer» (versión 2.0, 6 de noviembre de 2026; la versión 1.0 se conserva como referencia), que contiene la verificación completa de la postura de Microsoft y de los marcos.

**Fuentes oficiales de Microsoft citadas:**

- CISO Workshop: https://learn.microsoft.com/en-us/security/adoption/the-ciso-workshop
- Microsoft Cybersecurity Reference Architectures (MCRA): https://learn.microsoft.com/en-us/security/adoption/mcra
- Zero Trust Adoption Framework: https://learn.microsoft.com/en-us/security/zero-trust/adopt/zero-trust-adoption-overview
- Microsoft Digital Defense Report 2026: https://www.microsoft.com/en-us/security/security-insider/threat-landscape/2026-digital-defense-report
- Novedades de Security Exposure Management: https://learn.microsoft.com/en-us/security-exposure-management/whats-new
- Interrupción automática de ataques: https://learn.microsoft.com/en-us/defender-xdr/automatic-attack-disruption
- Microsoft Sentinel en el portal de Defender: https://learn.microsoft.com/en-us/azure/sentinel/microsoft-sentinel-defender-portal
- Microsoft Entra Agent ID — novedades: https://learn.microsoft.com/en-us/entra/agent-id/whats-new-agent-id
- Gobierno de identidades de agentes: https://learn.microsoft.com/en-us/entra/id-governance/agent-id-governance-overview
- Microsoft Agent 365: https://learn.microsoft.com/en-us/microsoft-agent-365/overview
- Agent 365 disponible de forma general (1-may-2026): https://www.microsoft.com/en-us/security/blog/2026/05/01/microsoft-agent-365-now-generally-available-expands-capabilities-and-integrations/
- Microsoft 365 E7 y Agent 365 disponibles de forma general: https://techcommunity.microsoft.com/blog/microsoft_365blog/microsoft-365-e7-and-agent-365-are-now-generally-available/4516295
- Inclusión de Security Copilot en Microsoft 365 E5: https://learn.microsoft.com/en-us/copilot/security/security-copilot-inclusion
- Inventario de Power Platform: https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory
- Purview DSPM: https://learn.microsoft.com/en-us/purview/data-security-posture-management-learn-about
- DLP para Microsoft 365 Copilot: https://learn.microsoft.com/en-us/purview/dlp-microsoft365-copilot-location-learn-about
- Auditoría de Copilot y agentes: https://learn.microsoft.com/en-us/purview/audit-copilot
- Purview para Microsoft 365 Copilot (etiquetas, eDiscovery): https://learn.microsoft.com/en-us/purview/ai-m365-copilot
- Protección de datos empresariales de Microsoft 365 Copilot: https://learn.microsoft.com/en-us/microsoft-365/copilot/enterprise-data-protection
- SharePoint Advanced Management con licencias de Copilot: https://learn.microsoft.com/en-us/sharepoint/sharepoint-advanced-management-features-copilot-license
- Prompt Shields: https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection
- Evaluadores de agentes de Foundry: https://learn.microsoft.com/en-us/azure/foundry/concepts/evaluation-evaluators/agent-evaluators
- AI Red Teaming Agent: https://learn.microsoft.com/en-us/azure/foundry/concepts/ai-red-teaming-agent
- Retiro de modelos en Foundry: https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/model-retirements
- Servidores MCP en Azure API Management: https://learn.microsoft.com/en-us/azure/api-management/mcp-server-overview
- Lista de regulaciones de Compliance Manager: https://learn.microsoft.com/en-us/purview/compliance-manager-regulations-list
- Customer Copyright Commitment: https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/openai/customer-copyright-commitment
- Responsible AI Transparency Report: https://www.microsoft.com/en-us/corporate-responsibility/topics/responsible-ai/reports/transparency-report/
- Plantillas de Insider Risk Management: https://learn.microsoft.com/en-us/purview/insider-risk-management-policy-templates
- Microsoft Entra Verified ID con Face Check: https://learn.microsoft.com/en-us/entra/verified-id/whats-new
- Quick Machine Recovery (Windows): https://techcommunity.microsoft.com/blog/windows-itpro-blog/resilience-in-action-for-windows-devices/4434571
- Microsoft Entra Internet Access (Global Secure Access): https://techcommunity.microsoft.com/blog/microsoft-entra-blog/lock-down-ai-web-and-private-apps-what%E2%80%99s-new-in-internet-access-and-private-acce/3847825
- Defender for Cloud Apps: aplicaciones de IA generativa: https://learn.microsoft.com/en-us/copilot/manage/manage-generative-ai-apps
- Security Alert Triage Agent (Defender): https://learn.microsoft.com/en-us/defender-xdr/phishing-triage-agent
- Conditional Access Optimization Agent (Entra): https://learn.microsoft.com/en-us/entra/security-copilot/conditional-access-agent-optimization
- Threat Intelligence Briefing Agent: https://techcommunity.microsoft.com/blog/microsoftthreatprotectionblog/monthly-news---january-2026/4484885
- Lago de datos de Microsoft Sentinel: https://www.microsoft.com/en-us/security/blog/2025/09/30/empowering-defenders-in-the-era-of-agentic-ai-with-microsoft-sentinel/
- Entornos administrados (Power Platform y Copilot Studio): https://learn.microsoft.com/en-us/power-platform/admin/managed-environment-overview
- Aprobación de agentes en el centro de administración de Microsoft 365: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-requests?view=o365-worldwide
- Aprobaciones humanas en flujos de agentes (Copilot Studio): https://learn.microsoft.com/en-us/microsoft-copilot-studio/flows-advanced-approvals
- Registro de herramientas y servidores MCP (Agent 365): https://learn.microsoft.com/en-us/microsoft-agent-365/tooling-servers-overview
- Guía de seguridad para MCP: https://learn.microsoft.com/en-us/azure/developer/azure-mcp-server/security
- Observabilidad de Microsoft Foundry: https://learn.microsoft.com/en-us/azure/foundry/concepts/observability
- Detección de material protegido (Azure AI Content Safety): https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/protected-material
- Retención y eDiscovery de interacciones de IA: https://learn.microsoft.com/en-us/purview/retention-policies-copilot
- Copilot controls (antes Copilot Control System): https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-controls/copilot-controls-overview
- Licenciamiento de Agent 365: https://www.microsoft.com/licensing/faqs/122
- Deshabilitar o bloquear agentes: https://learn.microsoft.com/en-us/entra/agent-id/manage-agent-identities-admin
- Microsoft Secure Score: https://learn.microsoft.com/en-us/defender-xdr/microsoft-secure-score
- Microsoft Defender Vulnerability Management: https://learn.microsoft.com/en-us/defender-vulnerability-management/defender-vulnerability-management
- Microsoft Defender for Endpoint: https://learn.microsoft.com/en-us/defender-endpoint/microsoft-defender-endpoint
- Microsoft Defender for Office 365: https://learn.microsoft.com/en-us/defender-office-365/mdo-about
- Seguridad de DevOps en Defender for Cloud: https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-devops-introduction
- Privileged Identity Management: https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-configure
- Flujos de ciclo de vida (Entra ID Governance): https://learn.microsoft.com/en-us/entra/id-governance/what-are-lifecycle-workflows
- Service Trust Portal: https://learn.microsoft.com/en-us/compliance/assurance/stp-get-started
- Security Development Lifecycle (SDL): https://www.microsoft.com/en-us/securityengineering/sdl/
- Adenda de protección de datos de productos y servicios de Microsoft (DPA): https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA?lang=1

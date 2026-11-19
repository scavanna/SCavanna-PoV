> **Registro de la versión 1.3 (16 de noviembre de 2026).** Este documento se conserva tal como se publicó. Las cifras, los estados y los archivos que cita corresponden a esa versión. El estado vigente está en `docs/15_Decisiones_delegadas_y_relectura_1_4.md` y en los documentos 16 a 19.

# Base de referencia del Frontier CISO Atlas

**Frontier CISO Atlas 1.3** · Taxonomía 6.0 (reglas de asignación, revisión 2) · Ontología 2.1.0 · GM-24 V7.1 · 16 de noviembre de 2026 · Estado: decisiones de diseño confirmadas por el autor; reglas adoptadas según la lectura del curador y corpus releído a ciegas por lectores automáticos, con una lectura para todos y dos donde la primera difería; contenido candidato, sin validación humana

## 1. Para qué sirve

La taxonomía se justifica contra lo que publican los organismos que definen el oficio. Esta base reúne esos organismos y sus artefactos, con la versión vigente, la fecha, el estado y la fuente, tal como se verificaron el 15 de noviembre de 2026. Cumple tres funciones:

1. **Justificar la taxonomía.** Los elementos de primer nivel de cada artefacto se cruzaron con territorios, dominios y funciones (`03_Taxonomia_6_0.md`).
2. **Dar versión a cada cruce.** Cada mapeo declara la versión contra la que el GM-24 dice haberlo hecho. Donde el GM-24 no la declara (MITRE ATT&CK, ATLAS y D3FEND), la propiedad lo dice en lugar de suponerla, y cada elemento de marco guarda la versión de la que procede su código y su nombre.
3. **Avisar cuando algo envejece.** Las discrepancias entre lo que usa el GM-24 V7.1 y lo que rige hoy quedan registradas en lugar de corregirse en silencio.

## 2. Cómo se construyó

- Cinco verificaciones contra las páginas del organismo emisor, cuyos informes completos están en `anexos/` (A1 a A5).
- Solo fuentes oficiales. Cuando un dato salió de una fuente secundaria, la entrada dice «parcial».
- Las vistas previas privadas quedaron fuera.
- Lo que no se pudo verificar se declara como silencio; no se completó de memoria.
- **Segunda verificación (versión 1.2).** Segunda verificación independiente de 35 puntos que sostienen decisiones de la taxonomía o del remapeo (32 afirmaciones y 3 preguntas abiertas: 9 puntos sobre ATT&CK, ATLAS y CCM y 26 sobre otras normas y marcos), hecha contra las páginas de los organismos emisores durante la revisión crítica de la versión 1.2. Resultado: Sin errores que cambien una decisión de la taxonomía. Se corrigieron dos registros (las versiones de Open FAIR y la identificación de las áreas de CyBOK), se confirmaron dos cambios de nombre de proyectos de NIST que estaban a revalidar y se precisaron cinco fichas. Cuatro conteos no se pudieron confirmar en fuente oficial pública: los controles de ISO/IEC 27002 y del Anexo A de ISO/IEC 42001, los 32 controles de Swift CSCF y las 11 áreas de competencia de NICE. El informe está en `anexos/A7_Revision_critica_verificacion_externa.md`.

Estados de verificación: **si** = verificado en fuente oficial; **parcial** = verificado en parte o en fuente secundaria; **no verificado** = citado por el GM-24, fuera de esta revisión; **fuente interna** = material del proyecto.

## 3. Números

- **42 organismos** y **146 artefactos**: 99 verificados, 37 verificados en parte, 2 no verificados y 8 de fuente interna.
- **Concentración.** De los 42 organismos, 41 son externos y uno es el propio proyecto (TheNextCISO, con 8 artefactos de fuente interna). El organismo con más artefactos es un proveedor de tecnología: Microsoft, con 23 artefactos. Le siguen National Institute of Standards and Technology (22), ISO/IEC JTC 1 (10) y Reguladores de México, Centroamérica y Sudamérica (9). La base no es neutral respecto de ese proveedor, y conviene leer con esa reserva los cruces que lo usan.
- **469 elementos de primer nivel** registrados.
- **Cruces:** 327 elementos de 29 artefactos (en 30 conjuntos de elementos) con dominios; 80 elementos de 12 marcos del rol con territorios; 54 elementos de 11 modelos funcionales con funciones.

| Clase de artefacto | Cantidad |
|---|---|
| norma | 17 |
| regulación | 15 |
| guía | 12 |
| marco de proveedor | 8 |
| informe de evidencia | 8 |
| plataforma (contexto del plano B) | 7 |
| lista de riesgos | 6 |
| catálogo de controles | 5 |
| marco | 5 |
| arquitectura de referencia | 5 |
| certificación del rol | 5 |
| modelo de madurez | 4 |
| perfil | 3 |
| marco de competencias | 3 |
| taxonomía de amenazas | 3 |
| especificación | 3 |
| marco de riesgo | 2 |
| iniciativa | 2 |
| modelo | 2 |
| regulación en trámite | 2 |
| documento (fuente interna) | 2 |
| marco de ciberseguridad | 1 |
| guía de ingeniería | 1 |
| guía de medición | 1 |
| guía de transición | 1 |
| metas de desempeño | 1 |
| directiva | 1 |
| estrategia | 1 |
| marco de gobierno | 1 |
| guía de gobierno corporativo | 1 |
| cuerpo de conocimiento | 1 |
| norma sectorial | 1 |
| marco sectorial | 1 |
| marco de evaluación | 1 |
| ontología defensiva | 1 |
| modelo de amenazas | 1 |
| norma de verificación | 1 |
| concepto de proveedor | 1 |
| herramienta de evaluación | 1 |
| programa de proveedor | 1 |
| principios de supervisión | 1 |
| formato | 1 |
| corpus curricular (fuente interna) | 1 |
| sub-plan (fuente interna) | 1 |
| sistema (fuente interna) | 1 |
| índice (fuente interna) | 1 |
| línea base (fuente interna) | 1 |
| catálogo (fuente interna) | 1 |

Los artefactos de clase «plataforma (contexto del plano B)» son productos. Están en la base porque las instancias del plano B los usan, pero no cuentan como respaldo de la taxonomía.

## 4. Lo que cambió y afecta al Atlas

**Estructura estable.**

- NIST CSF 2.0 no cambió su núcleo: 6 funciones y 22 categorías. SP 800-61 Rev. 3, CISA CPG 2.0 y el borrador de SP 800-82 Rev. 4 se alinean a él.
- ISO/IEC 27002:2022 conserva 93 controles en 4 temas; el tema físico tiene 14. El conteo sale de fuentes secundarias coincidentes: la norma es de pago y la segunda verificación no pudo confirmarlo en una fuente oficial pública.

**Novedades con efecto en la taxonomía.**

- **Criptografía poscuántica con fechas.** NIST IR 8547 quedó final el 27-oct-2026 y fija dos hitos, «deprecated after 2030» y «disallowed after 2035», para los algoritmos de clave pública vulnerables a la computación cuántica (firmas ECDSA, EdDSA y RSA; establecimiento de claves con Diffie-Hellman, MQV y RSA). El calendario obliga a los sistemas federales de Estados Unidos y es una referencia para los demás; la verificación no contrastó a qué niveles de seguridad alcanza cada hito. Sostiene la admisión de D26 por materialidad.
- **Medición.** NIST SP 800-55 Vol. 1 y Vol. 2 (dic-2024) reemplazan la guía de 2008. Sostiene D28.
- **Vulnerabilidades por exposición.** CISA BOD 26-04 (10-jun-2026) revoca BOD 22-01 y prioriza por exposición del activo, estado en el catálogo KEV, automatización del exploit e impacto técnico. Sostiene el ajuste de D13.
- **Seguridad de la IA con estructura propia.** ISO/IEC 27090:2026, ETSI EN 304 223, la AI Controls Matrix v1.1 de CSA, el Top 10 de OWASP para aplicaciones agénticas y el borrador del Cyber AI Profile de NIST, con tres áreas: asegurar, defender y frustrar.
- **Protocolos de agentes.** MCP (especificación del 28-jul-2026) y A2A (v1.0.1) están bajo la Linux Foundation. Quedan aclarados en el alcance de D20.
- **Arquitectura en los marcos del rol.** El esquema 2026 de CISM suma arquitectura empresarial y de seguridad. Sostiene D25.
- **Geopolítica y soberanía.** El Cloud Adoption Framework de Microsoft trata la soberanía como escenario; la reforma propuesta de NIS2 pide políticas nacionales de migración poscuántica. Sostiene CAT11.

**Novedades que obligan a revalidar.**

- MITRE ATT&CK v20 (la versión exacta vigente es la v20.1) tiene 15 tácticas y ATLAS v2026.10 tiene 16; el mapeo del GM-24 V7.1 usa 14 y 14.
- CSA CCM v4.1 (27-ene-2026) renombra un dominio. El cruce propio del Atlas ya usa la v4.1; el mapeo del GM-24 conserva la v4.
- COBIT 7 se lanza el 19-nov-2026; CISSP cambia de esquema el 15-abr-2027.
- El benchmark de seguridad en la nube de Microsoft v2 sigue en versión preliminar.

## 5. Evidencia usada para las fuerzas del eje H

| Fuente | Dato | Elemento del Atlas que sostiene |
|---|---|---|
| WEF Global Cybersecurity Outlook 2026 | 64 % de las organizaciones contempla ciberataques de motivación geopolítica | CAT11 |
| ENISA Threat Landscape 2026 | 57,3 % de los incidentes registrados fue de motivación ideológica. Es un conteo de incidentes, no una medida de impacto | CAT11 |
| Estudio de IDC de 2026 citado por Microsoft. El grupo se define como el 10 % superior de una escala de madurez de IA; los datos son declarados; la edición de 2025 fue encargada por el proveedor | 87 % de las empresas de frontera dice tener un proceso para gobernar agentes; 51 % de las rezagadas | Contexto de HOM12; no es su justificación |
| Cloud Security Alliance (informe encargado por un proveedor; verificación parcial) | 47 % de las organizaciones reporta un incidente de seguridad con un agente de IA | HOM12, HV02 |
| IBM Cost of a Data Breach 2026 | 68 % de las organizaciones vulneradas no tenía gobierno para gestionar la IA o detectar IA no autorizada | HOM08, HOM12 |
| Verizon DBIR 2026 | 48 % de las brechas tuvo participación de terceros | CAT08, alcance de D17 |
| Mandiant M-Trends 2026 | El tiempo medio estimado hasta la explotación es de −7 días: ocurre antes del parche | CAT04, alcance de D13 |
| ISC2 Cybersecurity Workforce Study 2025 (verificación parcial) | 59 % califica su carencia de habilidades de crítica o significativa | INH03 |
| Microsoft Work Trend Index 2026 | Los factores organizacionales pesan más del doble que los individuales en el impacto de la IA (67 % frente a 32 %) | HX08, T02 y T03 |
| Microsoft Digital Defense Report 2026 | 5,3 horas en promedio hasta que una carga de trabajo expuesta en la nube fue atacada | CAT04, HV01 |

Las cifras son de los informes citados y describen sus propias muestras; no son mediciones del Atlas.

## 6. Plazos de aviso de incidentes en México, Centroamérica y Sudamérica

Sirven de contexto para D03 y para la subfunción RS03. El estado de verificación de cada país está en el anexo A5.

| País | Plazo | Norma |
|---|---|---|
| Argentina | BCRA: aviso inicial dentro de la primera hora; cierre en no más de 5 días corridos | Com. «A» 8280 |
| Chile | CMF: 30 minutos; ANCI: alerta temprana en 3 horas e informe final en 15 días corridos | RAN 20-8; Ley 21.663 |
| Uruguay | CERTuy: 24 horas (sectores críticos); URCDP: 72 horas (datos personales) | Decreto 66/025; Decreto 64/020 |
| Perú | 48 horas desde que se toma conocimiento (datos personales) | DS 016-2024-JUS |
| Panamá | 72 horas desde que se conoce el incidente (datos personales) | Decreto Ejecutivo 285 de 2021 |
| Ecuador | 72 horas desde la detección (entidades públicas e infraestructura crítica digital) | Ley Orgánica para el Fortalecimiento de la Ciberseguridad |
| Colombia | 15 días hábiles para reportar a la SIC (datos personales) | Ley 1581 de 2012 |
| México | Aviso «de forma inmediata» al titular, sin plazo en horas | LFPDPPP (2025) |
| Costa Rica | Plazos en lineamientos no extraídos | Acuerdo CONASSIF 5-24 |

## 7. Discrepancias registradas

| Id | Tema | Hallazgo | Acción |
|---|---|---|---|
| DSC-01 | MITRE ATT&CK | El mapeo del GM-24 V7.1 usa 14 tácticas; la v20 tiene 15: en la v19 (28-abr-2026) Defense Evasion se dividió en Stealth, que conserva el identificador TA0005, y Defense Impairment (TA0112). | Registrar la versión de artefacto del mapeo y remapear en la próxima versión del GM-24. No se remapea en silencio. |
| DSC-02 | MITRE ATLAS | El mapeo usa 14 tácticas y «AI Attack Staging»; la v2026.10 tiene 16 («AI Attack Adaptation», Command and Control y Lateral Movement). | Igual que DSC-01. |
| DSC-03 | CSA CCM | El GM-24 rotula «CCM v4»; rige la v4.1 (27-ene-2026), que renombra IVS como I&S y tiene 207 objetivos. | Actualizar el rótulo y el código del dominio en el mapeo. La versión 1.2 ya lo corrigió en el cruce propio del Atlas con dominios (conjunto «CSA CCM v4.1», dominio I&S); el mapeo del GM-24 V7.1 conserva «CCM v4» e IVS hasta su próxima versión. |
| DSC-04 | Open FAIR | La primera verificación encontró O-RA 2.0.1 y O-RT 3.0.1, que son las versiones de la certificación; la memoria del proyecto (9-nov-2026) registra O-RT 3.1 y O-RA 2.1, que The Open Group anunció el 22-may-2025. | Resuelta en la versión 1.2 con la segunda verificación: valen O-RA 2.1 y O-RT 3.1. La memoria del proyecto estaba en lo cierto. |
| DSC-05 | CISA BOD 22-01 | Revocada por BOD 26-04 (10-jun-2026); el catálogo KEV sigue vigente. | Ningún pre-ensayo cita BOD 22-01 por número; revisar los ensayos al redactarlos. |
| DSC-06 | Nombres de proyectos de NIST | El informe de verificación registra el cambio de «AI» por «Super Intelligence (SI)» en proyectos de NIST (COSAiS como COSIS, «Cyber SI Profile»). Los documentos ya emitidos conservan «AI». | Guardar ambos nombres como alias. La segunda verificación (15-nov-2026) confirmó el renombre de COSAiS a COSIS, del 20-oct-2026, y el nombre «Cyber SI Profile» del proyecto del NCCoE. |
| DSC-07 | COBIT | El cruce usa los 5 dominios de COBIT 2019; ISACA anuncia COBIT 7 para el 19-nov-2026. | Revalidar el cruce después del lanzamiento. El pre-ensayo APC-223 cita COBIT 2019. |
| DSC-08 | Zero Trust | Microsoft Learn enuncia «assume compromise»; los blogs de 2026 siguen diciendo «assume breach». | Usar el enunciado de Learn y conservar el anterior como alias. |
| DSC-09 | Microsoft cloud security benchmark | La v2 sigue en versión preliminar; agrega el dominio de IA y no lista Governance and Strategy. | Revalidar después de Ignite 2026 (17 al 20-nov-2026). |
| DSC-10 | Reglamento de IA de la UE | Modificado por (UE) 2026/1744: el alto riesgo pasa al 2-dic-2027 (Anexo III) y al 2-ago-2028 (Anexo I). | Revisar las fechas en los ensayos que traten alto riesgo. |
| DSC-11 | CMMC | Fase II suspendida el 13-jul-2026; el programa queda en Fase 1. | Tratarlo como artefacto inestable. |
| DSC-12 | Microsoft Purview | «DSPM for AI» ya no es el nombre vigente; el pre-ensayo AMP-31 lo usa. | Actualizar el nombre al redactar el ensayo. |
| DSC-13 | CISSP | El cruce usa el esquema de 2024; ISC2 anuncia uno nuevo desde el 15-abr-2027. | Revalidar en abril de 2027. |
| DSC-14 | Chile, Ley 21.719 | El informe la da vigente desde el 1-dic-2026; la memoria del proyecto registra una postergación en trámite. | Revalidar el 1-dic-2026. |
| DSC-15 | CyBOK | Las versiones 1.0 y 1.1 de este paquete citaban las áreas de CyBOK con códigos «KA01» a «KA21», que eran un orden interno y no una numeración de CyBOK; «KA18 Cyber Physical Systems» corresponde en realidad a Cyber-Physical Systems Security, capítulo 21 de CyBOK 1.2.0. | Corregido en la versión 1.2: las áreas se citan por su nombre. La segunda verificación detectó el error. |
| DSC-16 | MITRE ATLAS | Trece conceptos del GM-24 V7.1 que no tratan de IA llevan un vínculo con las tácticas «AI Attack Staging» y «AI Model Access». La segunda verificación no halló en ATLAS ningún criterio que respalde vincular esas tácticas con conceptos de gestión. | La propuesta de remapeo pide retirar esos 26 vínculos en la próxima versión del GM-24. El mapeo del GM-24 V7.1 no se modificó. |

### Propuesta de remapeo

Para las discrepancias DSC-01, DSC-02 y DSC-03 hay una propuesta escrita, que tu aceptación en bloque alcanzó como pedido para la próxima versión del GM-24 (decisión D-10, que era una pregunta: se leyó como «sí» y la confirmaste el 16 de noviembre de 2026, D-14.3). El mapeo del GM-24 V7.1 no se modificó. Alcanza a 91 vínculos existentes de 74 conceptos, agrega 7 y propone retirar 26. La versión 1.1 dejaba casos «a revisar»; la verificación externa de la versión 1.2 los resolvió y no queda ninguno.

| Marco | Tipo de cambio | Vínculos |
|---|---|---|
| CSA CCM v4.1 | Cambia el nombre o el código | 51 |
| MITRE ATLAS v2026.10 | Se agrega un vínculo | 2 |
| MITRE ATLAS v2026.10 | Cambia el nombre o el código | 9 |
| MITRE ATLAS v2026.10 | Se propone retirar el vínculo | 26 |
| MITRE ATT&CK v20 | Se agrega un vínculo | 5 |
| MITRE ATT&CK v20 | Cambia el nombre o el código | 5 |

Reglas usadas:

- **R1.** ATT&CK: la táctica Defense Evasion se dividió en la v19 (28-abr-2026); TA0005 conserva el identificador y pasa a llamarse Stealth.
- **R2.** ATT&CK: un vínculo a Defense Evasion suma TA0112 Defense Impairment, porque la definición anterior abarcaba las dos conductas. Es un criterio de este paquete: ninguna fuente oficial prescribe el vínculo de estos conceptos con una táctica.
- **R3.** ATLAS: AI Attack Staging pasa a llamarse AI Attack Adaptation.
- **R4.** ATLAS: los vínculos de conceptos que no son de IA y solo llevan el par por defecto (AI Attack Staging y AI Model Access) se proponen para retiro: la verificación externa no halló en ATLAS un criterio que los respalde.
- **R5.** ATLAS: un concepto que cubre la matriz suma Command and Control y Lateral Movement.
- **R6.** CCM: IVS pasa a I&S; el rótulo del artefacto pasa de «CCM v4» a «CCM v4.1» en los 855 vínculos.

Tres cosas a tener en cuenta:

- **MITRE ATT&CK.** Los cinco vínculos a «Defense Evasion» son de conceptos de inteligencia de amenazas y de búsqueda de amenazas. En la v19 esa táctica se dividió en Stealth, que conserva el identificador TA0005, y Defense Impairment (TA0112). Ninguna fuente oficial prescribe con cuál de las dos se vincula un concepto de inteligencia: la propuesta conserva el vínculo con TA0005 y agrega TA0112, y lo declara como criterio de este paquete.
- **MITRE ATLAS.** 26 vínculos pertenecen a 13 conceptos que no son de IA (gobierno, riesgo y continuidad, entre otros) y llevan el mismo par, «AI Attack Staging» y «AI Model Access», con fuerza «fuerte». La verificación externa no halló en ATLAS ningún criterio que respalde vincular esas tácticas con conceptos de gestión: la propuesta pide retirarlos.
- **CSA CCM.** Además del cambio de código en 51 vínculos, el rótulo «CCM v4» debería pasar a «CCM v4.1» en los 855 vínculos de ese marco.

La lista vínculo por vínculo está en `data/propuesta_remapeo_gm24.csv`.

## 8. Silencios declarados

| Id | Ámbito | Silencio |
|---|---|---|
| SIL-01 | GM-24 | No existe una versión posterior a la V7.1 (la V8 solo se menciona como futura). |
| SIL-02 | GM-24 | Los híbridos HC-041 a HC-080 no están en el paquete V7.1: el corpus trae 40 conceptos HC. |
| SIL-03 | Fuentes | Los libros de Excel del proyecto guardados en OneDrive llevan etiqueta de confidencialidad y no se pudieron leer; se usaron sus exportaciones JSON y CSV. |
| SIL-04 | Fuentes | Varias normas ISO e IEC son de pago: su estructura interna quedó verificada de forma parcial contra la ficha pública. |
| SIL-05 | Calendario | Ignite 2026 (17 al 20-nov-2026) y COBIT 7 (19-nov-2026) todavía no ocurrieron. |
| SIL-06 | Regulación | CIRCIA no tiene regla final; el proyecto de ley británico no tiene sanción real; las normas de Ecuador, Panamá, Colombia, Perú, México y Costa Rica quedaron verificadas de forma parcial. |
| SIL-07 | IA | El Cyber AI Profile de NIST es un borrador preliminar y el Responsible AI Standard rediseñado de Microsoft no tiene texto público. |
| SIL-08 | Taxonomía | En el corpus base, D19 no tiene pre-ensayos y D08, D10, D18, D22 y D27 tienen menos de cinco; la capa de ampliación (serie APX, de redacción asistida) cubre D19, D27 y RC05 y no cuenta en las estadísticas del corpus. Las variables homeostáticas no tienen respaldo normativo externo. Ningún indicador del catálogo CISO 365 2.0 mide la protección física y ambiental: la subfunción PR06 no tiene indicadores. |
| SIL-09 | MCCS | La Biblioteca cognitiva del CISO de frontera (1.404 conceptos) está cargada en el grafo candidato desde la versión 1.1, pero no integra el corpus de pre-ensayos: en el corpus, T01 sigue subrepresentado. Sus territorios son un valor por categoría de la base y no se afirman como clasificación (decisión D-12); una de cada cuatro definiciones no está respaldada por una fuente. |
| SIL-10 | Grafo | No hay ensayos aprobados ni instancias de organizaciones. Los sesgos y los vínculos de indicadores con variables homeostáticas existen desde la versión 1.1 como propuesta, sin validación humana. La revisión crítica 1.2 fue hecha por revisores automáticos con la misma configuración que el autor de los artefactos: reduce el error aleatorio, no el sistemático. |
| SIL-11 | Línea base | Los siete documentos canónicos de la Taxonomía 5.3 y de la Ontología 1.0.0 no están en el proyecto; se trabajó con sus catálogos JSON y con los doce documentos de arquitectura. |

## 9. Catálogo de artefactos

### Marcos, catálogos de controles y normas (38)

| Id | Artefacto | Organismo | Versión | Fecha | Estado | Verificado |
|---|---|---|---|---|---|---|
| NIST-CSF-2.0 | [NIST Cybersecurity Framework (CSF) 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) | National Institute of Standards and Technology | 2.0 (CSWP 29) | 2024-02-26 | final; Core sin cambios | si |
| NIST-IR-8596 | [NIST IR 8596 Cyber AI Profile](https://csrc.nist.gov/pubs/ir/8596/iprd) | National Institute of Standards and Technology | Initial Preliminary Draft | 2025-12-16 | borrador preliminar; en revisión de comentarios | si |
| NIST-SP-800-53 | [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) | National Institute of Standards and Technology | Rev. 5, Release 5.2.0 | 2025-08-27 | final | si |
| NIST-COSAIS | [Control Overlays for Securing AI Systems (COSAiS), renombrado COSIS el 20-oct-2026](https://csrc.nist.gov/projects/cosis) | National Institute of Standards and Technology | sin overlay publicado | 2025-08-14 | en desarrollo | si |
| NIST-SP-800-37 | [NIST SP 800-37 Rev. 2 (Risk Management Framework)](https://csrc.nist.gov/pubs/sp/800/37/r2/final) | National Institute of Standards and Technology | Rev. 2 | 2018-12 | final | si |
| NIST-AI-RMF | [NIST AI Risk Management Framework 1.0 (AI 100-1)](https://www.nist.gov/itl/ai-risk-management-framework) | National Institute of Standards and Technology | 1.0 | 2023-01-26 | final; en revisión | parcial |
| NIST-AI-600-1 | [NIST AI 600-1 Generative AI Profile](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf) | National Institute of Standards and Technology | única | 2024-07-26 | final | si |
| NIST-PF | [NIST Privacy Framework](https://www.nist.gov/privacy-framework) | National Institute of Standards and Technology | 1.0 (1.1 en borrador) | 2020-01-16 | final | si |
| NIST-SSDF | [NIST SP 800-218 Secure Software Development Framework](https://csrc.nist.gov/pubs/sp/800/218/final) | National Institute of Standards and Technology | v1.1 (v1.2 en borrador) | 2022-02 | final | si |
| NIST-FIPS-PQC | [NIST FIPS 203, 204 y 205](https://csrc.nist.gov/projects/post-quantum-cryptography) | National Institute of Standards and Technology | ML-KEM, ML-DSA y SLH-DSA | 2024-08-13 | finales | parcial |
| ISO-27001 | [ISO/IEC 27001:2022](https://www.iso.org/standard/27001) | ISO/IEC JTC 1 | Edición 3 con Amd 1:2024 | 2022-10 | vigente | parcial |
| ISO-27002 | [ISO/IEC 27002:2022](https://www.iso.org/standard/75652.html) | ISO/IEC JTC 1 | Edición 3 | 2022-02 | vigente | parcial |
| ISO-27005 | [ISO/IEC 27005:2022](https://www.iso.org/standard/80585.html) | ISO/IEC JTC 1 | Edición 4 | 2022-10 | vigente | parcial |
| ISO-31000 | [ISO 31000:2018](https://www.iso.org/standard/31000) | ISO/IEC JTC 1 | Edición 2 | 2018-02 | vigente; en revisión | si |
| ISO-27701 | [ISO/IEC 27701:2025](https://www.iso.org/standard/27701) | ISO/IEC JTC 1 | Edición 2 | 2025-10 | vigente | parcial |
| ISO-27014 | [ISO/IEC 27014:2020](https://www.iso.org/standard/74046.html) | ISO/IEC JTC 1 | Edición 2 | 2020-12 | vigente; en revisión | si |
| ISO-27035 | [ISO/IEC 27035 (serie)](https://www.iso.org/standard/78973.html) | ISO/IEC JTC 1 | por parte | 2023 | vigente | si |
| ISO-22301 | [ISO 22301:2019](https://www.iso.org/standard/88412.html) | ISO/IEC JTC 1 | Edición 2 con Amd 1:2024 | 2019 | vigente; en revisión | parcial |
| ISO-42001 | [ISO/IEC 42001:2023](https://www.iso.org/standard/42001) | ISO/IEC JTC 1 | Edición 1 | 2023-12 | vigente | parcial |
| ISO-AI-OTRAS | [ISO/IEC 42005:2025, 42006:2025 y 27090:2026](https://www.iso.org/standard/42005) | ISO/IEC JTC 1 | varias | 2025–2026 | vigentes | si |
| IEC-62443 | [ISA/IEC 62443 (serie)](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards) | ISA / IEC | por parte | 2007–2025 | vigente | parcial |
| ETSI-303645 | [ETSI EN 303 645](https://www.etsi.org/deliver/etsi_en/303600_303699/303645/03.01.03_60/en_303645v030103p.pdf) | European Telecommunications Standards Institute | V3.1.3 | 2024-09 | vigente | si |
| ETSI-304223 | [ETSI EN 304 223](https://www.etsi.org/deliver/etsi_en/304200_304299/304223/02.01.01_60/en_304223v020101p.pdf) | European Telecommunications Standards Institute | V2.1.1 | 2025-12 | vigente | si |
| ISACA-COBIT | [COBIT 2019](https://www.isaca.org/resources/cobit) | ISACA | COBIT 2019 | 2018–2019 | vigente; COBIT 7 anunciado para el 19-nov-2026 | parcial |
| ISACA-DTEF | [Digital Trust Ecosystem Framework](https://www.isaca.org/resources/news-and-trends/newsletters/atisaca/2024/volume-5/digital-trust-ecosystem-framework-to-steer-organizations-toward-sturdier-relationships) | ISACA | edición 2024 | 2024-03 | vigente | parcial |
| TOG-OPENFAIR | [Open FAIR Body of Knowledge](https://www.opengroup.org/open-fair) | The Open Group | O-RA 2.1 y O-RT 3.1 | 2025-05-22 | vigente | si |
| PCI-DSS | [PCI DSS](https://www.pcisecuritystandards.org/standards/pci-dss/) | PCI Security Standards Council | v4.0.1 | 2024-06 | vigente | parcial |
| SWIFT-CSCF | [Swift Customer Security Controls Framework](https://www.swift.com/myswift/services/training/swift-training-catalogue/swift-customer-security-programme-v2026) | Swift | v2026 (v2027 publicado) | 2025-07-01 | vigente | parcial |
| NCSC-CAF | [NCSC Cyber Assessment Framework](https://www.ncsc.gov.uk/collection/cyber-assessment-framework) | National Cyber Security Centre | 4.0 | 2025-08-06 | vigente | si |
| MITRE-ENGAGE | [MITRE Engage](https://engage.mitre.org/matrix/) | MITRE | 1.0 | 2022-02-28 | vigente | si |
| OWASP-ASVS | [OWASP ASVS](https://asvs.owasp.org/) | OWASP Foundation | 5.0.0 | 2025-05-30 | vigente | si |
| CIS-CONTROLS | [CIS Critical Security Controls](https://www.cisecurity.org/controls/cis-controls-list) | Center for Internet Security | v8.1 | 2024-06-25 | vigente | si |
| CSA-CCM | [CSA Cloud Controls Matrix](https://cloudsecurityalliance.org/artifacts/cloud-controls-matrix-v4-1) | Cloud Security Alliance | v4.1 | 2026-01-27 | vigente | si |
| CSA-AICM | [CSA AI Controls Matrix](https://cloudsecurityalliance.org/artifacts/ai-controls-matrix-v1-1) | Cloud Security Alliance | v1.1 | 2026-06-22 | vigente | si |
| FIRST-CVSS | [CVSS](https://www.first.org/cvss/) | Forum of Incident Response and Security Teams | v4.0 | 2023-11 | vigente | parcial |
| FIRST-TLP | [Traffic Light Protocol](https://www.first.org/tlp/) | Forum of Incident Response and Security Teams | 2.0 | 2022-08 | vigente | si |
| FIRST-CSIRT | [FIRST CSIRT Services Framework](https://www.first.org/standards/frameworks/csirts/csirt_services_framework_v2.1) | Forum of Incident Response and Security Teams | v2.1 | — | vigente | si |
| MS-MCSB | [Microsoft cloud security benchmark](https://learn.microsoft.com/en-us/security/benchmark/azure/overview) | Microsoft | v2 (versión preliminar); v1 heredada | 2026-01-15 | v2 en versión preliminar | si |

### Guías, arquitecturas y modelos (36)

| Id | Artefacto | Organismo | Versión | Fecha | Estado | Verificado |
|---|---|---|---|---|---|---|
| NIST-AGENT-STD | [AI Agent Standards Initiative (NIST/CAISI)](https://www.nist.gov/super-intelligence/si-agent-standards-initiative) | National Institute of Standards and Technology | sin guía final sobre agentes | 2026-02-17 | en curso | si |
| NIST-SP-800-207 | [NIST SP 800-207 Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final) | National Institute of Standards and Technology | SP 800-207 y 800-207A | 2020-08 | final | si |
| NIST-SP-800-61 | [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) | National Institute of Standards and Technology | Rev. 3 | 2025-04 | final | si |
| NIST-SP-800-160V2 | [NIST SP 800-160 Vol. 2 Rev. 1](https://csrc.nist.gov/pubs/sp/800/160/v2/r1/final) | National Institute of Standards and Technology | Vol. 2 Rev. 1 | 2021-12 | final | si |
| NIST-SP-800-161 | [NIST SP 800-161 Rev. 1 (C-SCRM)](https://csrc.nist.gov/pubs/sp/800/161/r1/upd1/final) | National Institute of Standards and Technology | Rev. 1 Update 1 | 2022-05 | final | si |
| NIST-SP-800-55 | [NIST SP 800-55 Vol. 1 y Vol. 2 (medición)](https://csrc.nist.gov/pubs/sp/800/55/v1/final) | National Institute of Standards and Technology | Vol. 1 y Vol. 2 | 2024-12-04 | final | si |
| NIST-SP-800-82 | [NIST SP 800-82 Rev. 3 (OT)](https://csrc.nist.gov/pubs/sp/800/82/r3/final) | National Institute of Standards and Technology | Rev. 3 (Rev. 4 en borrador del 21-sep-2026) | 2023-09 | final | si |
| NIST-IR-8547 | [NIST IR 8547 Transition to Post-Quantum Cryptography Standards](https://csrc.nist.gov/pubs/ir/8547/final) | National Institute of Standards and Technology | final | 2026-10-27 | final | si |
| NIST-SP-800-63 | [NIST SP 800-63-4 Digital Identity Guidelines](https://csrc.nist.gov/pubs/sp/800/63/4/final) | National Institute of Standards and Technology | Revision 4 | 2025-07-31 | final | si |
| CISA-ZTMM | [CISA Zero Trust Maturity Model](https://www.cisa.gov/zero-trust-maturity-model) | Cybersecurity and Infrastructure Security Agency | 2.0 | 2023-04 | final; página archivada | si |
| CISA-CPG | [CISA Cross-Sector Cybersecurity Performance Goals](https://www.cisa.gov/cross-sector-cybersecurity-performance-goals) | Cybersecurity and Infrastructure Security Agency | 2.0 | 2025-12-11 | final | si |
| CISA-BOD-26-04 | [CISA BOD 26-04 y catálogo KEV](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) | Cybersecurity and Infrastructure Security Agency | BOD 26-04 | 2026-06-10 | vigente; revoca BOD 19-02 y BOD 22-01 | si |
| DOD-ZT | [DoD Zero Trust Strategy](https://dodcio.defense.gov/Portals/0/Documents/Library/DoD-ZTStrategy.pdf) | U.S. Department of Defense | v1.0 | 2022-10-21 | vigente | parcial |
| TOG-TOGAF | [TOGAF Standard, 10th Edition](https://www.opengroup.org/togaf) | The Open Group | 10th Edition | — | vigente | parcial |
| TOG-ZT | [Zero Trust y arquitectura de seguridad (The Open Group)](https://www.opengroup.org/forum/security-forum-0/zerotrustsecurityarchitecture) | The Open Group | no verificada | — | parcial | parcial |
| SABSA | [SABSA Matrix](https://sabsa.org/sabsa-executive-summary/) | The SABSA Institute | no verificada | — | vigente | parcial |
| FAIR-CAM | [FAIR Controls Analytics Model (FAIR-CAM)](https://www.fairinstitute.org/fair-controls-analytics-model) | FAIR Institute | 1.0 | 2025-01-15 | vigente | si |
| FAIR-AIR | [FAIR-AIR Approach Playbook](https://www.fairinstitute.org/hubfs/FAIR-AIR%20Approach%20Playbook.pdf) | FAIR Institute | no verificada | — | vigente | parcial |
| DOE-C2M2 | [Cybersecurity Capability Maturity Model (C2M2)](https://www.energy.gov/ceser/cybersecurity-capability-maturity-model-c2m2) | U.S. Department of Energy | 2.1 | 2022-06 | vigente | si |
| ASD-E8 | [Essential Eight Maturity Model](https://www.cyber.gov.au/publication/essential-eight-maturity-model) | Australian Signals Directorate | noviembre de 2023 | 2023-11-27 | vigente | si |
| OWASP-SAMM | [OWASP SAMM](https://owaspsamm.org/model/) | OWASP Foundation | v2 (core v2.2.0) | — | vigente | parcial |
| OWASP-AI-OTROS | [Otros proyectos de IA de OWASP (AI Exchange, AIVSS, MCP Top 10 en beta)](https://owaspai.org/) | OWASP Foundation | varias | — | en curso | si |
| CSA-MAESTRO | [CSA MAESTRO y guías de IA agéntica](https://cloudsecurityalliance.org/blog/2026/10/15/i-love-google-s-agentic-ai-security-roadmap-adding-maestro-will-make-it-more-powerful-an-open-letter-to-google) | Cloud Security Alliance | sin versión | 2025-02 | vigente | parcial |
| FIRST-EPSS | [EPSS](https://www.first.org/epss/) | Forum of Incident Response and Security Teams | v5 | 2026-06-15 | vigente | parcial |
| SLSA | [SLSA](https://slsa.dev/spec/) | Open Source Security Foundation | v1.2 | — | aprobada | si |
| CISA-SBOM | [CISA 2026 Minimum Elements for a Software Bill of Materials](https://content.govdelivery.com/accounts/USDHSCISA/bulletins/422a7eb) | Cybersecurity and Infrastructure Security Agency | v2.1 | 2026-07-29 | final | si |
| COSAI | [Coalition for Secure AI (CoSAI)](https://www.coalitionforsecureai.org/) | OASIS Open (CoSAI) | sin versión | — | activa | si |
| MCP | [Model Context Protocol](https://modelcontextprotocol.io/specification/2026-07-28) | Linux Foundation (Agentic AI Foundation) | 2026-07-28 | 2026-07-28 | vigente | si |
| A2A | [Agent2Agent (A2A)](https://a2a-protocol.org/latest/) | Linux Foundation (Agentic AI Foundation) | v1.0.1 | 2026-05-26 | vigente | si |
| MS-MCRA | [Microsoft Cybersecurity Reference Architectures (MCRA)](https://learn.microsoft.com/en-us/security/zero-trust/microsoft-reference-architecture) | Microsoft | junio de 2026 | 2026-06 | vigente | si |
| MS-ZTW | [Zero Trust Workshop](https://learn.microsoft.com/en-us/security/zero-trust/workshop-zero-trust-overview) | Microsoft | sin versión | 2026-11-06 | vigente | si |
| MS-AI-DEFENSE | [AI Defense Capabilities for Enterprise AI Security](https://learn.microsoft.com/en-us/security/zero-trust/catalog-ai-defense-capabilities/catalog-ai-defense-capabilities) | Microsoft | páginas del 1-ago-2026 | 2026-08-01 | vigente | si |
| BCBS-OPRES | [Principles for operational resilience (Comité de Basilea)](https://www.bis.org/publications/202103-guidelines-principles-operational-resilience) | Comité de Supervisión Bancaria de Basilea | marzo de 2021 | 2021-03-31 | vigente | si |
| FSB-FIRE | [Format for Incident Reporting Exchange (FIRE)](https://www.fsb.org/2025/04/format-for-incident-reporting-exchange-fire-final-report/) | Financial Stability Board | informe final | 2025-04-15 | publicado; adopción voluntaria | si |
| NIST-SP-800-30 | [NIST SP 800-30 (evaluación de riesgos)](https://csrc.nist.gov) | National Institute of Standards and Technology | la citada por el GM-24 V7.1 | — | no verificado en esta revisión | no verificado |
| NIST-SP-800-84 | [NIST SP 800-84 (pruebas, entrenamiento y ejercicios)](https://csrc.nist.gov) | National Institute of Standards and Technology | la citada por el GM-24 V7.1 | — | no verificado en esta revisión | no verificado |

### Marcos del rol, competencias y cuerpos de conocimiento (10)

| Id | Artefacto | Organismo | Versión | Fecha | Estado | Verificado |
|---|---|---|---|---|---|---|
| NIST-NICE | [NICE Framework (SP 800-181 Rev. 1 y Components v2.2.0)](https://www.nist.gov/itl/applied-cybersecurity/nice/nice-framework-resource-center/current-version/change-logs) | National Institute of Standards and Technology | Components v2.2.0 | 2026-04-28 | final | si |
| ISACA-CISM | [CISM, esquema de examen 2026](https://www.isaca.org/credentialing/cism/cism-exam-content-outline) | ISACA | 2026 | 2026-11-03 | vigente | si |
| ISACA-CRISC | [CRISC, esquema de examen 2025](https://www.isaca.org/credentialing/crisc/crisc-exam-content-outline) | ISACA | 2025 | 2025-11-03 | vigente | si |
| ISACA-AAISM | [AAISM (Advanced in AI Security Management)](https://www.isaca.org/credentialing/aaism/aaism-exam-content-outline) | ISACA | vigente | — | vigente | si |
| ISACA-AI-OTRAS | [AAIA, AAIR y AAIG (ISACA)](https://www.isaca.org/credentialing/aaia/aaia-exam-content-outline) | ISACA | varias | — | AAIG en beta | parcial |
| ISC2-CISSP | [CISSP, esquema de examen 2024](https://www.isc2.org/certifications/cissp/cissp-certification-exam-outline) | ISC2 | 2024 | 2024-04-15 | vigente; nuevo esquema desde el 15-abr-2027 | si |
| SFIA | [SFIA 9](https://sfia-online.org/en/sfia-9) | SFIA Foundation | 9 | 2024-10 | vigente | si |
| ENISA-ECSF | [European Cybersecurity Skills Framework (ECSF)](https://www.enisa.europa.eu/topics/skills-and-competences/skills-development/european-cybersecurity-skills-framework-ecsf) | Agencia de la Unión Europea para la Ciberseguridad | septiembre de 2022 | 2022-09-19 | vigente | si |
| NACD-ISA | [Director's Handbook on Cyber-Risk Oversight, 5.ª edición](https://www.nacdonline.org/globalassets/public-pdfs/2026_directors-handbook-cyber-risk_accessible.pdf) | NACD e Internet Security Alliance | Fifth Edition | 2026 | vigente | si |
| CYBOK | [CyBOK 1.2](https://www.cybok.org/knowledgebase1_2/) | CyBOK (Universidad de Bristol) | 1.2 | 2026-09 | vigente | si |

### Amenazas y listas de riesgos (11)

| Id | Artefacto | Organismo | Versión | Fecha | Estado | Verificado |
|---|---|---|---|---|---|---|
| MITRE-ATTACK | [MITRE ATT&CK (Enterprise)](https://attack.mitre.org/resources/updates/) | MITRE | v20 | 2026-10-13 | vigente | si |
| MITRE-ATLAS | [MITRE ATLAS](https://github.com/mitre-atlas/atlas-data/releases) | MITRE | v2026.10 | 2026-10 | vigente | si |
| MITRE-D3FEND | [MITRE D3FEND](https://d3fend.mitre.org/changelog/) | MITRE | ontología 1.6.0 | 2026-08-31 | vigente | parcial |
| MITRE-EMB3D | [MITRE EMB3D](https://emb3d.mitre.org/) | MITRE | 2.0.2 | 2026-06-01 | vigente | si |
| MITRE-CWE25 | [CWE Top 25](https://cwe.mitre.org/top25/) | MITRE | 2025 | 2025-12-11 | vigente | si |
| OWASP-TOP10 | [OWASP Top 10:2025](https://top10.owasp.org/2025/) | OWASP Foundation | 2025 | 2025 | vigente | si |
| OWASP-API | [OWASP API Security Top 10](https://owasp.org/projects/api-security-project) | OWASP Foundation | 2023 | 2023 | vigente | si |
| OWASP-LLM | [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) | OWASP Foundation | 2025 | 2025 | vigente | si |
| OWASP-ASI | [OWASP Top 10 for Agentic Applications](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) | OWASP Foundation | 2026 | 2025-12-09 | vigente | si |
| OWASP-NHI | [OWASP Non-Human Identities Top 10](https://owasp.github.io/www-project-non-human-identities-top-10/2025/top-10-2025/) | OWASP Foundation | 2025 | 2025 | vigente | si |
| MS-AIRT-TAX | [Taxonomy of Failure Modes in Agentic AI Systems](https://www.microsoft.com/en-us/security/blog/2026/06/04/updating-taxonomy-failure-modes-agentic-ai-systems-year-red-teaming-taught-us/) | Microsoft | v2.0 | 2026-04 | vigente | si |

### Regulación (17)

| Id | Artefacto | Organismo | Versión | Fecha | Estado | Verificado |
|---|---|---|---|---|---|---|
| DOD-CMMC | [Cybersecurity Maturity Model Certification (CMMC)](https://dodcio.defense.gov/CMMC/About/) | U.S. Department of Defense | Model Overview v2.13 | 2024-09 | en Fase 1; Fase II suspendida el 13-jul-2026 | parcial |
| SEC-CYBER | [Reglas de divulgación de ciberseguridad de la SEC](https://www.sec.gov/rules-regulations/2023/07/s7-09-22) | U.S. Securities and Exchange Commission | Release 33-11216 | 2023-07-26 | vigente | si |
| UE-AI-ACT | [Reglamento de IA de la UE](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng) | Unión Europea | (UE) 2024/1689, modificado por (UE) 2026/1744 | 2024-08-01 | vigente, con calendario escalonado | si |
| UE-NIS2 | [Directiva NIS2 y Reglamento de Ejecución (UE) 2024/2690](https://eur-lex.europa.eu/eli/dir/2022/2555/oj/eng) | Unión Europea | (UE) 2022/2555 y (UE) 2024/2690 | 2024-10-18 | vigente | si |
| UE-DORA | [Reglamento de resiliencia operativa digital (DORA)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022R2554) | Unión Europea | (UE) 2022/2554 | 2025-01-17 | vigente | si |
| UE-CRA | [Reglamento de Ciberresiliencia (CRA)](https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act) | Unión Europea | (UE) 2024/2847 | 2024-12-10 | vigente, en aplicación parcial | si |
| UK-CSR-BILL | [Cyber Security and Resilience (Network and Information Systems) Bill](https://bills.parliament.uk/bills/4035) | Parlamento del Reino Unido | Bill 175 2026-27 | 2026-11-03 | proyecto sin sanción real | si |
| US-CIRCIA | [CIRCIA, regla de notificación de incidentes](https://www.reginfo.gov/public/do/eAgendaViewRule?RIN=1670-AA04&pubId=202504) | Cybersecurity and Infrastructure Security Agency | propuesta de 2024 | 2024-04-04 | sin regla final | parcial |
| REG-AR | [Argentina: BCRA «A» 7724 y «A» 8280; Ley 25.326](https://www.bcra.gob.ar/archivos/Pdfs/comytexord/A7724.pdf) | Reguladores de México, Centroamérica y Sudamérica | textos ordenados vigentes | 2025-07-17 | vigentes | si |
| REG-CL | [Chile: Ley 21.663, Ley 21.719 y RAN 20-10 y 20-8](https://anci.gob.cl/preguntas-frecuentes/preguntas-frecuentes-portal-anci/) | Reguladores de México, Centroamérica y Sudamérica | textos vigentes | 2024-04-08 | Ley 21.719 rige desde el 1-dic-2026 | si |
| REG-CO | [Colombia: Circulares Externas 007 de 2018 y 033 de 2020; Ley 1581](https://www.superfinanciera.gov.co/loader.php?lServicio=Tools2&lTipo=descargas&lFuncion=descargar&idFile=1031904) | Reguladores de México, Centroamérica y Sudamérica | vigentes | 2020-11 | vigentes | parcial |
| REG-MX | [México: LFPDPPP (2025), disposiciones de la CNBV y política federal de ciberseguridad](https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPDPPP.pdf) | Reguladores de México, Centroamérica y Sudamérica | vigentes | 2025-03-20 | vigentes | parcial |
| REG-PE | [Perú: DS 016-2024-JUS y DS 126-2025-PCM](https://www3.congreso.gob.pe/Docs/DGP/DIDP/files/ds_016-2024-jus.pdf) | Reguladores de México, Centroamérica y Sudamérica | vigentes | 2024-11-30 | vigentes | parcial |
| REG-UY | [Uruguay: Decreto 66/025, Decreto 64/020 y Circular BCU 2497](https://www.impo.com.uy/bases/decretos/66-2025) | Reguladores de México, Centroamérica y Sudamérica | vigentes | 2025-03-14 | vigentes | si |
| REG-CR | [Costa Rica: Acuerdo CONASSIF 5-24 y Ley 8968](https://www.sugef.fi.cr/normativa/normativa_transversal/documentos/CONASSIF%205-24%20%28v03%2015%20julio%202025%29.pdf) | Reguladores de México, Centroamérica y Sudamérica | vigentes | 2024-07-22 | vigentes | parcial |
| REG-PA | [Panamá: Ley 81 de 2019 y Decreto Ejecutivo 285 de 2021](https://antai.gob.pa/wp-content/uploads/2021/05/Reglamentacio%CC%81n-de-Ley-81-de-Proteccio%CC%81n-de-Datos-Personales.pdf) | Reguladores de México, Centroamérica y Sudamérica | vigentes | 2021-05-28 | vigentes; ley marco en proyecto | parcial |
| REG-EC | [Ecuador: Ley Orgánica para el Fortalecimiento de la Ciberseguridad y LOPDP](https://www.pbplaw.com/es/publicaciones/ley-organica-para-el-fortalecimiento-de-la-ciberseguridad-1/) | Reguladores de México, Centroamérica y Sudamérica | vigentes | 2026-05-22 | vigentes | parcial |

### Informes de evidencia (8)

| Id | Artefacto | Organismo | Versión | Fecha | Estado | Verificado |
|---|---|---|---|---|---|---|
| MS-MDDR | [Microsoft Digital Defense Report](https://www.microsoft.com/en-us/corporate-responsibility/topics/cybersecurity/reports/microsoft-digital-defense-report/) | Microsoft | 2026 | 2026-10-01 | última edición | si |
| EV-DBIR | [Verizon Data Breach Investigations Report](https://www.verizon.com/business/resources/T5d3/reports/2026-dbir-data-breach-investigations-report.pdf) | Verizon | 2026 (19.ª edición) | 2026-05-19 | última edición | si |
| EV-WEF-GCO | [WEF Global Cybersecurity Outlook](https://www.weforum.org/publications/global-cybersecurity-outlook-2026) | World Economic Forum | 2026 | 2026 | última edición | parcial |
| EV-ENISA-ETL | [ENISA Threat Landscape](https://www.enisa.europa.eu/sites/default/files/2026-09/ENISA%20Threat%20Landscape%202026_Final.pdf) | Agencia de la Unión Europea para la Ciberseguridad | 2026 | 2026-09 | última edición | si |
| EV-IBM-CODB | [IBM Cost of a Data Breach Report](https://www.ibm.com/reports/data-breach) | IBM (Ponemon Institute) | 2026 | 2026 | última edición | si |
| EV-ISC2-WF | [ISC2 Cybersecurity Workforce Study](https://www.isc2.org/research) | ISC2 | 2025 | — | última edición listada | parcial |
| EV-MTRENDS | [M-Trends](https://cloud.google.com/blog/topics/threat-intelligence/m-trends-2026/) | Mandiant (Google Cloud) | 2026 | 2026-03-23 | última edición | si |
| EV-MCK-AI | [McKinsey The State of AI: Global Survey](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai) | McKinsey | 2026 | 2026-08-25 | última edición | si |

### Marcos y programas de proveedor (11)

| Id | Artefacto | Organismo | Versión | Fecha | Estado | Verificado |
|---|---|---|---|---|---|---|
| GOOGLE-SAIF | [Google Secure AI Framework (SAIF)](https://saif.google/) | Google | sin versión | — | vigente | si |
| MS-FRONTIER-FIRM | [Frontier Firm (Work Trend Index 2025 y 2026)](https://www.microsoft.com/en-us/worklab/work-trend-index/2025-the-year-the-frontier-firm-is-born) | Microsoft | Work Trend Index 2026 | 2026-05-05 | vigente | si |
| MS-SAF | [Microsoft Security Adoption Framework (SAF)](https://learn.microsoft.com/en-us/security/zero-trust/security-adoption-model) | Microsoft | sin versión; página del 6-nov-2026 | 2026-11-06 | vigente | si |
| MS-ZT | [Zero Trust (principios) y Zero Trust for AI](https://learn.microsoft.com/en-us/security/zero-trust/zero-trust-overview) | Microsoft | sin versión | 2026-08-04 | vigente | si |
| MS-ZTA | [Zero Trust Assessment](https://learn.microsoft.com/en-us/security/zero-trust/assessment/overview) | Microsoft | 2.6.0 | 2026-08 | vigente (proyecto comunitario) | si |
| MS-CAF | [Cloud Adoption Framework: fases y Secure](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/overview) | Microsoft | sin versión | 2026-09-04 | vigente | si |
| MS-CAF-AI | [Cloud Adoption Framework: adopción de IA](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai/strategy) | Microsoft | sin versión | 2026-10-15 | vigente | si |
| MS-CAF-AGENTS | [Cloud Adoption Framework: agentes de IA](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/) | Microsoft | sin versión | 2025-12-03 | vigente | si |
| MS-SFI | [Secure Future Initiative (SFI)](https://www.microsoft.com/en-us/trust-center/security/secure-future-initiative) | Microsoft | informe de julio de 2026 | 2026-07 | vigente | si |
| MS-SDL | [Microsoft Security Development Lifecycle (SDL)](https://www.microsoft.com/en-us/securityengineering/sdl/practices) | Microsoft | 10 prácticas; SDL for AI | 2026-02-03 | vigente | si |
| MS-RAI | [Principios de IA responsable y Responsible AI Standard](https://www.microsoft.com/en-us/ai/principles-and-approach) | Microsoft | v2 público (2022); rediseño de 2026 sin texto público | 2026-09-01 | parcial | parcial |

### Plataformas (contexto del plano B) (7)

| Id | Artefacto | Organismo | Versión | Fecha | Estado | Verificado |
|---|---|---|---|---|---|---|
| MS-AGENT365 | [Microsoft Agent 365](https://learn.microsoft.com/en-us/microsoft-agent-365/overview) | Microsoft | disponibilidad general | 2026-05-01 | vigente | si |
| MS-ENTRA-AGENTID | [Microsoft Entra Agent ID](https://learn.microsoft.com/en-us/entra/agent-id/what-is-microsoft-entra-agent-id) | Microsoft | disponibilidad general | 2026 | vigente | si |
| MS-E7 | [Microsoft 365 E7: The Frontier Suite](https://blogs.microsoft.com/blog/2026/03/09/introducing-the-first-frontier-suite-built-on-intelligence-trust/) | Microsoft | disponibilidad general | 2026-05-01 | vigente | si |
| MS-SC-AGENTS | [Agentes de Security Copilot](https://learn.microsoft.com/en-us/copilot/security/agents-overview) | Microsoft | mixto por agente | 2026-04-01 | parcial | parcial |
| MS-PURVIEW-DSPM | [Microsoft Purview Data Security Posture Management](https://learn.microsoft.com/en-us/purview/data-security-posture-management-learn-about) | Microsoft | versión actual unificada | 2025-11-18 | parcial | parcial |
| MS-DEFENDER-AI | [Defender for AI Services (Defender for Cloud)](https://learn.microsoft.com/en-us/azure/defender-for-cloud/ai-threat-protection) | Microsoft | disponibilidad general | 2026-06-17 | vigente | si |
| MS-SENTINEL | [Microsoft Sentinel (data lake, graph y MCP server)](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-lake-overview) | Microsoft | disponibilidad general | 2025-11-18 | vigente | si |

### Fuentes internas del proyecto (8)

| Id | Artefacto | Organismo | Versión | Fecha | Estado | Verificado |
|---|---|---|---|---|---|---|
| TNC-GM24 | TheNextCISO GM-24 | TheNextCISO | V7.1 | 2026-11 | vigente | fuente interna |
| TNC-POGAC | GM-24 V7.1 · sub-plan PO-GAC (dueño de producto-control y gerente de agentes) | TheNextCISO | V7.1 | 2026-11 | vigente | fuente interna |
| TNC-MCCS | Meta-Cognitive CISO System (MCCS) | TheNextCISO | notas de trabajo 2026 | 2026 | en desarrollo | fuente interna |
| TNC-CISOOS | CISO-OS, Documento Maestro Consolidado | TheNextCISO | agosto de 2026 | 2026-08 | vigente | fuente interna |
| TNC-BIBLIOTECA | Biblioteca del CISO de frontera (índice) | TheNextCISO | 2026 | 2026 | vigente | fuente interna |
| ATLAS-5.3 | AI CISO Atlas: Taxonomía 5.3 y Core Ontology 1.0.0 | TheNextCISO | 5.3 y 1.0.0 | 2026 | reemplazada por la propuesta 6.0 y 2.1.0 cuando se apruebe | fuente interna |
| ATLAS-3P | Agenda de IA del CISO: tres pilares (v4.0) | TheNextCISO | 4.0 | 2026 | vigente | fuente interna |
| TNC-CISO365 | Modelo Operativo CISO 365: catálogo de indicadores, objetivos y gobierno | TheNextCISO | 2.0 | 2026-11 | vigente | fuente interna |

## 10. Archivos

- `data/base_de_referencia.json`: organismos, artefactos, elementos, discrepancias y silencios.
- `data/propuesta_remapeo_gm24.csv` y `data/propuesta_remapeo_gm24.json`: la propuesta de remapeo, con los casos resueltos en la versión 1.2.
- `data/base_de_referencia_artefactos.csv`: el catálogo en una tabla.
- `data/cobertura_dominios_artefactos.csv`: matriz de dominios por artefacto (P = elemento primario, s = secundario).
- `anexos/A1` a `A5`: informes de verificación completos.
- `anexos/A7_Revision_critica_verificacion_externa.md`: los tres informes de la segunda verificación.

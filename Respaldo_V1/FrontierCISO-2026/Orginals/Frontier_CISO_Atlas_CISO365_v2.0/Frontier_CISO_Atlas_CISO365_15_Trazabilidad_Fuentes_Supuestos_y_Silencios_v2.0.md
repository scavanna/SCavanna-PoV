# Trazabilidad, fuentes, supuestos provisorios y silencios

**Frontier CISO Atlas · Modelo Operativo CISO 365 · versión 2.0, revisión 2** · documento 15 de 16 · 15 de noviembre de 2026 · @SCavanna

> Propuesta de base, sujeta a validación y a calibración en cada organización. La ejecución se puede contratar; la rendición de cuentas, no.

## 1. Trazabilidad con TheNextCISO GM-24 V7.1

GM-24 V7.1 tiene 379 conceptos: 245 K, 52 AMP, 40 HC y 42 PA. Cada función de gobierno y de gestión corresponde a una unidad; cada servicio de operación tiene una unidad de referencia. Los conceptos puente HC se cuentan en cada unidad que conectan.

| Unidad | Título en GM-24 V7.1 | Funciones del modelo | K | AMP | HC | PA |
|---|---|---|:--:|:--:|:--:|:--:|
| G1.1 | Principios de Gobierno, Contexto Organizacional y Arquetipos CISO | GOB-G1.1 | 10 | 3 | 3 | 1 |
| G1.2 | Desarrollo de Estrategia y Alineación con el Negocio | GOB-G1.2 | 10 | 3 | 7 | 1 |
| G2.1 | Selección e Integración de Marcos y Estándares | GOB-G2.1 | 11 | 2 | 0 | 2 |
| G2.2 | Ciclo de Vida de Políticas, Estándares y Procedimientos | GOB-G2.2 | 10 | 2 | 6 | 3 |
| G3.1 | Requisitos Legales, Regulatorios y Contractuales | GOB-G3.1 | 10 | 2 | 6 | 1 |
| G3.2 | Gestión del Cumplimiento y Aseguramiento Continuo | GOB-G3.2 | 10 | 2 | 7 | 1 |
| G4.1 | Gobernanza del Riesgo: Marcos y Estructuras | GOB-G4.1 | 10 | 2 | 3 | 2 |
| G4.2 | Definición y Comunicación del Apetito de Riesgo | GOB-G4.2 | 10 | 2 | 6 | 1 |
| G5.1 | Supervisión de la Evaluación y Análisis | GOB-G5.1 | 10 | 2 | 4 | 0 |
| G5.2 | Supervisión del Tratamiento y Aceptación | GOB-G5.2 | 10 | 2 | 3 | 0 |
| G6.1 | Comunicación Estratégica | GOB-G6.1 | 10 | 2 | 8 | 1 |
| G6.2 | Liderazgo Ético y Medición de Efectividad | GOB-G6.2 | 10 | 3 | 5 | 1 |
| M1.1 | Desarrollo, Gestión y Operaciones del Programa de Seguridad | GES-M1.1 | 10 | 2 | 4 | 3 |
| M1.2 | Gestión Financiera, Liderazgo de Equipo y Capacitación | GES-M1.2 · OPE-PR-10 | 10 | 2 | 5 | 3 |
| M2.1 | Gestión de Activos y Seguridad del Ciclo de Vida de los Datos | GES-M2.1 · OPE-ID-01 · OPE-ID-06 · OPE-PR-06 | 10 | 2 | 5 | 1 |
| M2.2 | Gestión de Identidad y Acceso (IAM) y Principios de Confianza Cero | GES-M2.2 · OPE-PR-01 · OPE-PR-02 · OPE-PR-03 | 10 | 2 | 5 | 1 |
| M3.1 | Arquitectura de Seguridad, Ingeniería y Diseño (Incl. Zero Trust) | GES-M3.1 · OPE-PR-08 | 12 | 2 | 10 | 2 |
| M3.2 | Selección, Implementación y Evaluación de Controles | GES-M3.2 · OPE-ID-03 · OPE-PR-04 · OPE-PR-05 · OPE-PR-11 | 10 | 3 | 12 | 3 |
| M4.1 | Operaciones de Seguridad, Monitorización e Inteligencia | GES-M4.1 · OPE-DE-01 · OPE-DE-02 · OPE-DE-03 · OPE-DE-05 · OPE-DE-06 | 11 | 2 | 8 | 6 |
| M4.2 | Gestión de Amenazas, Vulnerabilidades y Riesgos Emergentes | GES-M4.2 · OPE-ID-02 · OPE-ID-05 · OPE-DE-04 | 11 | 2 | 4 | 2 |
| M5.1 | Planificación y Preparación (Incl. BIA) | GES-M5.1 · OPE-RS-05 | 10 | 2 | 7 | 1 |
| M5.2 | Ejecución, Post-Mortem y Comunicación | GES-M5.2 · OPE-RS-01 · OPE-RS-02 · OPE-RS-03 · OPE-RS-04 · OPE-RC-05 | 10 | 2 | 4 | 2 |
| M6.1 | Continuidad, DRP y Resiliencia Operativa | GES-M6.1 · OPE-RC-01 · OPE-RC-02 · OPE-RC-03 · OPE-RC-04 | 10 | 2 | 7 | 1 |
| M6.2 | Seguridad en Redes, Nube, Tecnologías Emergentes y SCRM | GES-M6.2 · OPE-ID-04 · OPE-ID-07 · OPE-PR-07 · OPE-PR-09 · OPE-PR-12 | 10 | 3 | 9 | 3 |

### Conceptos incorporados entre GM-24 V5 y V7.1

| Unidad | Conceptos |
|---|---|
| G1.1 | AMP-01 Metacognición del CISO; AMP-02 Sesgos y límites cognitivos; AMP-03 Autoridad frente a responsabilidad; G1.1-PA01 Rol dual especialista/manager y Product Owner de control |
| G1.2 | AMP-04 Estrategia adaptativa; AMP-05 Evolución contextual H; AMP-06 Gobierno de la IA; G1.2-PA01 Economía unitaria de agentes: caso de negocio y TCO |
| G2.1 | AMP-07 NIST CSF 2.0 Govern; AMP-08 Referencias informativas y no equivalencia; G2.1-K11 CSF 2.0 completo: funciones, categorías y perfiles organizacionales; G2.1-PA01 Grilla de ownership: NIST CSF 2.0 × dominios Zero Trust; G2.1-PA02 Marcos de gobierno de IA aplicados: NIST AI RMF e ISO/IEC 42001 |
| G2.2 | AMP-09 Policy-as-code; AMP-10 Gobierno de excepciones automatizadas; G2.2-PA01 Política de uso y gobierno de agentes; G2.2-PA02 Estándar de ficha de agente (charter) y runbooks de agentes; G2.2-PA03 Baseline, excepciones y overrides de un control técnico |
| G3.1 | AMP-11 Soberanía de datos; AMP-12 Responsabilidad por agentes; G3.1-PA01 Panorama regulatorio de IA y agentes |
| G3.2 | AMP-13 Evidencia continua; AMP-14 Aseguramiento de decisiones de IA; G3.2-PA01 Aseguramiento continuo de la configuración del control (deriva) |
| G4.1 | AMP-15 Riesgo sistémico; AMP-16 Homeostasis y fuerzas de cambio; G4.1-PA01 Tres líneas de defensa para la flota de agentes; G4.1-PA02 Taxonomía y registro de riesgos de agentes |
| G4.2 | AMP-17 Autoridad delegada; AMP-18 Límites de autonomía; G4.2-PA01 KRIs de la flota de agentes y umbrales de intervención |
| G5.1 | AMP-19 Calidad epistemológica de evidencia; AMP-20 Riesgo de modelos de IA |
| G5.2 | AMP-21 Decisiones reversibles; AMP-22 Aceptación de riesgo de agentes |
| G6.1 | AMP-23 Narrativa de riesgo basada en evidencia; AMP-24 Comunicación de incertidumbre; G6.1-PA01 Reporte ejecutivo del producto-control y de la fuerza de trabajo híbrida |
| G6.2 | AMP-25 Ética de autonomía; AMP-26 Supervisión humana efectiva; AMP-52 Content safety y riesgos de contenido generado; G6.2-PA01 Métricas de efectividad del gobierno de la flota |
| M1.1 | AMP-27 CISO-OS; AMP-28 Orquestación de agentes; M1.1-PA01 Diseño organizativo híbrido: roles, RACI y span of control; M1.1-PA02 Portafolio de productos-control con owners; M1.1-PA03 Modelo operativo por cadencias y excelencia operacional como requisito del programa |
| M1.2 | AMP-29 Competencias humanas y agentes; AMP-30 Adopción responsable de IA; M1.2-PA01 FinOps de agentes: presupuesto, costo por tarea y alertas de consumo; M1.2-PA02 Requisitos de IA y agentes en contratos de servicios gestionados; M1.2-PA03 Itinerario de desarrollo: de analista a PO-GAC |
| M2.1 | AMP-31 DSPM; AMP-32 Gobierno de datos para RAG; M2.1-PA01 Registro de agentes como clase de activo |
| M2.2 | AMP-33 Identidades no humanas; AMP-34 Identidad y autorización de agentes; M2.2-PA01 Permisos de humanos y agentes en el control: RBAC unificado, roles y conectores |
| M3.1 | AMP-35 Arquitectura de sistemas agénticos; AMP-36 Límites de herramientas y permisos; M3.1-K11 Arquitectura empresarial y arquitectura de seguridad de la información; M3.1-K12 Seguridad física, ambiental y mantenimiento como dependencias del control; M3.1-PA01 Arquitectura de referencia del SOC agéntico con control plane; M3.1-PA02 Arquitectura de protección del dominio Zero Trust |
| M3.2 | AMP-37 Evaluación adversarial de agentes; AMP-38 Pruebas de controles autónomos; AMP-52 Content safety y riesgos de contenido generado; M3.2-PA01 El control como producto: objetivo → configuración → evidencia; M3.2-PA02 Catálogo de controles de gobierno y gestión de agentes (AGC); M3.2-PA03 Evaluación de calidad de agentes: datasets dorados, regresión y criterios de aceptación |
| M4.1 | AMP-39 SOC agéntico; AMP-40 Human-in-the-loop; M4.1-K11 Deception y señuelos como control detectivo; M4.1-PA01 Modelo operativo del producto-control por cadencias; M4.1-PA02 Gestión de incidentes y alertas en Defender XDR; M4.1-PA03 Gestión de la calidad de detección del dominio: FP/FN, tuning, listas, indicadores y supresiones; M4.1-PA04 Hunting y detecciones personalizadas; M4.1-PA05 Observabilidad de la flota de agentes: telemetría, trazas y tableros; M4.1-PA06 Gestión del desempeño de agentes: revisión periódica y drift |
| M4.2 | AMP-41 Prompt injection; AMP-42 Envenenamiento de datos y modelos; M4.2-K11 Escalamiento de privilegios en identidades humanas y no humanas como táctica adversaria; M4.2-PA01 Amenazas del dominio Zero Trust; M4.2-PA02 Catálogos de amenazas a sistemas agénticos aplicados a la flota |
| M5.1 | AMP-43 Tabletop de incidentes con agentes; AMP-44 Kill switch y escalamiento; M5.1-PA01 Playbooks de incidentes de correo con roles humano/agente |
| M5.2 | AMP-45 Forense de agentes; AMP-46 Trazabilidad de decisiones autónomas; M5.2-PA01 Ejecución de respuesta en correo: AIR, acciones manuales y acciones de agentes con aprobación; M5.2-PA02 Mejora gobernada de agentes: del post-mortem al ChangeSet con regresión |
| M6.1 | AMP-47 Recuperación de servicios de IA; AMP-48 Dependencias de modelos; M6.1-PA01 Operación degradada del SOC sin agentes ni modelos |
| M6.2 | AMP-49 Supply chain de modelos; AMP-50 Seguridad de herramientas y conectores; AMP-51 Postura de IA en nube; M6.2-PA01 Plataformas y rutas de construcción de agentes y responsabilidad compartida en IA; M6.2-PA02 AgentOps / ALM de agentes; M6.2-PA03 Bases multiplataforma, multicloud y multimodelo |

## 2. Trazabilidad con las versiones anteriores

| Elemento | Origen | Tratamiento en la versión 2.0 |
|---|---|---|
| K01 a K64 | Catálogo de KPIs y OKR 1.2 | Sin cambios de definición ni de umbrales; se agregan función, categoría del marco, dominio Zero Trust y código de externalización |
| KSG01 a KSG06 | Catálogo 1.1 | Sin cambios |
| 142 actividades | Paquete integral del 13 de noviembre de 2026 | Ubicadas en las etapas nuevas, hoja «Actividades v1.0» |
| Seis objetivos anuales | Versión 1.0 | Cada objetivo de ciclo indica a cuál contribuye |
| Hitos H30 a H365 | Versión 1.0 | H30 y H60 caen en el diagnóstico, dentro del ciclo 1; el informe de los 100 días pasa al día 90 y cierra el ciclo 1; H180, H270 y H365 cierran los ciclos 2, 3 y 4 |
| 56 entrevistas y 54 rituales | Versión 1.0 | Vigentes; no se revisaron en esta versión |

## 3. Fuentes

| ID | Tipo | Fuente | Fecha | Dónde está |
|:--:|---|---|---|---|
| F01 | Corpus | TheNextCISO GM-24 V7.1 · paquete maestro (379 conceptos con pre-ensayo, 24 unidades, mapeo a 17 marcos) | 2026-11-15 | Archivos del proyecto |
| F02 | Corpus | TheNextCISO GM-24 V7.1 · Anexo PO-GAC y sub-plan (documentos 00 a 11): producto-control, gobierno de agentes, escala de autonomía | 2026-11-14 | Archivos del proyecto |
| F03 | Corpus | TheNextCISO GM-24 V7.1 · Estrategia de anexos tecnológicos y separación de planos; siete instancias de dominio | 2026-11-14 | Archivos del proyecto |
| F04 | Corpus | Formación «Gobierno y Gestión de la Ciberseguridad – The Next CISO», estructura de 24 clases (edición 7.1) | 2026-11-14 | Archivos del proyecto |
| F05 | Atlas | Modelo Operativo CISO 365 v1.0: tres libros y documentos 00 a 08 | 2026-11-10 | Carpeta de resultados de esta tarea |
| F06 | Atlas | Catálogo de KPIs y OKRs del CISO de empresa de frontera v1.2 (64 indicadores y 6 del sistema de gestión) | 2026-11-10 | Carpeta de resultados de esta tarea |
| F07 | Atlas | Paquete 1 «Integral del CISO» v1.0: 142 actividades del plan | 2026-11-13 | Archivos del proyecto |
| F08 | Atlas | «El CISO y la IA: tres pilares» v4.0, documento 08: SAF, Zero Trust para la IA y COE de IA | 2026-11-13 | Archivos del proyecto |
| F09 | Investigación | Zero Trust y su aplicación a la IA según NIST, The Open Group y Microsoft (informe con 39 fuentes) | 2026-11-15 | zero_trust_ia_investigacion.md |

Las 34 fuentes de Zero Trust (29 verificadas en su origen) están en el documento 07 «Zero Trust y Zero Trust para la IA».

## 4. Supuestos provisorios

| ID | Tema | Supuesto | En qué se apoya | A qué afecta | Qué lo haría revisar |
|---|---|---|---|---|---|
| SUP-01 | Zero Trust para la IA | No existe un estándar formal dedicado a «Zero Trust para la IA» en NIST ni en The Open Group; solo Microsoft usa esa denominación. Los seis criterios de IA y agentes del diagnóstico toman lo que coincide entre las fuentes: identidad propia por agente, mínimo privilegio por tarea, política aplicada fuera del modelo, registro independiente y aprobación humana para acciones de alto impacto. | Borradores de NIST (documento conceptual de identidad de agentes, 5-feb-2026; perfil Cyber AI IR 8596, borrador preliminar, 16-dic-2025; superposiciones de control COSIS, sin borrador público) y guía de Microsoft (19-mar-2026 y 4-ago-2026). | 6 criterios Zero Trust del dominio IA y agentes (ZT-IA-1 a ZT-IA-6). | Publicación final de cualquiera de los documentos de NIST sobre agentes, o de un estándar de The Open Group que trate la IA. |
| SUP-02 | Principios de diseño para agentes | Los diez principios de diseño para agentes que NIST propuso el 27-oct-2026 son una entrada de blog, no una publicación formal. Se usan como referencia, no como requisito. | Blog de NIST, 27-oct-2026. | Criterios ZT-IA y servicios OPE-ID-07, OPE-PR-11 y OPE-DE-06. | Publicación de los principios en un documento de NIST con proceso de comentarios. |
| SUP-03 | The Open Group | Los Zero Trust Commandments figuran como estándar en el listado oficial, pero su texto no pudo consultarse; los nombres de los mandamientos provienen de una presentación de los copresidentes del grupo de trabajo. El modelo de referencia sigue en Snapshot 1.0. | Listado oficial de The Open Group; presentación del grupo de trabajo. | Principios y criterios Zero Trust de los dominios no relacionados con la IA: se apoyan en NIST SP 800-207, que es final; The Open Group se usa como contraste. | Acceso al texto del estándar o publicación del modelo de referencia en versión final. |
| SUP-04 | Indicadores y resultados clave de IA y agentes | Los 16 indicadores de IA y agentes y los 12 resultados clave del frente F6 son provisorios: miden prácticas que los marcos aún no fijaron. | Las fuentes de SUP-01 y SUP-02; pre-ensayos de GM-24 V5 a V7.1. | K49 a K56, K88, K98, K108, K165, K166, K167, K175 y K187; resultados clave C1-F6 a C4-F6. | Los mismos de SUP-01, y el cierre del ciclo 2, cuando ya exista una línea base propia. |
| SUP-05 | Umbrales y metas de los indicadores nuevos | Los umbrales de estadio (E2 a E5) y las metas de los 154 indicadores nuevos son propuestas del modelo, sin referencia externa. Los 64 indicadores del catálogo 1.2 y los KSG conservan sus umbrales. | Modelo Operativo CISO 365 versión 2.0. | K65 a K196 y KX01 a KX22. | Línea base del diagnóstico (día 60) y revisión al cierre de cada ciclo. |
| SUP-06 | Conceptos nuevos de GM-24 | Los 99 pre-ensayos incorporados entre GM-24 V5 y V7.1 tienen pendiente su asignación de evidencia y sustento (ESS). El modelo usa sus ideas operativas, no sus cifras. | TheNextCISO GM-24 V7.1. | Funciones, criterios de externalización y gobierno de agentes derivados de los conceptos PA y AMP nuevos. | Aprobación curricular de V7.1 o publicación de V8. |
| SUP-07 | Estructura temporal | El año se organiza en cuatro ciclos trimestrales de 90 días (el último, de 95); el diagnóstico ocupa los primeros 60 días del ciclo 1 y el informe de los 90 días lo cierra. Las metas del ciclo 1 presuponen que las correcciones que no admiten espera empiezan antes de cerrar el diagnóstico; si no es posible, la parte no alcanzada de K33, K46, K41 y K28 pasa al ciclo 2. Es una convención del modelo: las duraciones se cambian en Parámetros. | Modelo Operativo CISO 365 versión 2.0. | Calendario, criterios de salida y metas por ciclo. | Decisión del CISO y de su sponsor al adoptar el plan; calendario de OKR de la organización, si es otro. |
| SUP-08 | Catálogo, no tablero | Los 224 indicadores son un catálogo para elegir, no un tablero. El modelo propone 12 indicadores principales para el directorio, 14 para la dirección ejecutiva y 16 para tecnología. | Modelo Operativo CISO 365 versión 2.0. | Selección de indicadores en el libro de KPIs y tablero. | Primera rendición de cuentas a cada audiencia (ciclo 1). |

El estado de cada supuesto se sigue en la hoja «Supuestos» del libro `Frontier_CISO_Atlas_CISO365_KPIs_y_Tablero_v2.0.xlsx`.

## 5. Silencios

Lo que el modelo no cubre, o no pudo verificar, se declara como hallazgo.

1. **Zero Trust para la IA no tiene un estándar formal.** Los criterios de IA y agentes toman lo que coincide entre borradores y guía de un proveedor.
2. **El texto oficial de los Zero Trust Commandments de The Open Group no pudo consultarse.** Los nombres de los mandamientos provienen de una presentación de los copresidentes del grupo de trabajo.
3. **Los umbrales y las metas de los 154 indicadores nuevos no tienen referencia externa.** Son propuestas del modelo.
4. **No hay valores de referencia de dotación ni de presupuesto.** El modelo da categorías, roles y método.
5. **No se relevaron normas de un país ni de un sector.** La función GOB-G3.1 pide ese relevamiento.
6. **Los 99 pre-ensayos incorporados entre GM-24 V5 y V7.1 tienen pendiente su aprobación curricular.** El modelo usa sus ideas operativas, no sus cifras.
7. **Los documentos de GM-24 V7.1 guardados con etiqueta de confidencialidad no pudieron leerse.** Se trabajó con el paquete maestro del proyecto, del 15 de noviembre de 2026.
8. **La tecnología operacional tiene un solo servicio** (OPE-PR-12). Una organización industrial necesita ampliarlo.
9. **Las 56 entrevistas y los 54 rituales de la versión 1.0 no se revisaron** frente a los temas nuevos; las 24 preguntas del libro de diagnóstico cubren esa diferencia en parte.
10. **Los archivos HTML se comprobaron con el validador y con pruebas automáticas de su lógica**, que dieron los mismos resultados que los libros. No se probaron en un navegador durante la construcción.
11. **El modelo no se aplicó todavía en una organización.** Es una propuesta de base.

---

*Frontier CISO Atlas · Modelo Operativo CISO 365 · versión 2.0, revisión 2 · 15 de noviembre de 2026 · propuesta sujeta a validación · @SCavanna*

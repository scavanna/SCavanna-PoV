# TheNextCISO GM-24 — Pre-ensayos (archivos de inicialización), lote AMP-03_V7-01 (V7.1)

> **GM-24 V7.1 · The Next CISO + Sub-plan PO-GAC** · 2026-11-14. Catálogo: 379 conceptos (245 K · 52 AMP · 40 HC · 42 PA), todos con pre-ensayo íntegro y mapeados a 17 marcos (NIST/ISACA/MITRE/OWASP/CIS/CSA). V7.1 = ChangeSet editorial CS-GM24-V7.1-001 (4 títulos generalizados; sin cambio de IDs, cantidad ni mapeo). Plano A (corpus académico). Referencias DD/K4x/R/eo:OP/COE: marco interno.

**Estado:** ideas centrales para desarrollo editorial; IDs curriculares (asignar `ESS-######` desde el registro SQLite). Estructura de los lotes GM-24 + práctica, próximos pasos y relación con la unidad.

## Inventario

| N.º | ID | Tipo | Unidad | Concepto |
|---|---|---|---|---|
| 091 | AMP-49 | AMP | M6.2 | Supply chain de modelos |
| 092 | AMP-50 | AMP | M6.2 | Seguridad de herramientas y conectores |
| 093 | AMP-51 | AMP | M6.2 | Postura de IA en nube |
| 094 | AMP-52 | AMP | G6.2 · M3.2 | Content safety y riesgos de contenido generado |
| 095 | G2.1-K11 | K | G2.1 | CSF 2.0 completo: funciones, categorías y perfiles organizacionales |
| 096 | M3.1-K11 | K | M3.1 | Arquitectura empresarial y arquitectura de seguridad de la información |
| 097 | M3.1-K12 | K | M3.1 | Seguridad física, ambiental y mantenimiento como dependencias del control |
| 098 | M4.1-K11 | K | M4.1 | Deception y señuelos como control detectivo |
| 099 | M4.2-K11 | K | M4.2 | Escalamiento de privilegios en identidades humanas y no humanas como táctica adversaria |

---

### 091. AMP-49 — Supply chain de modelos

**Unidad:** M6.2 Seguridad en Redes, Nube, Tecnologías Emergentes y SCRM · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 188 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** Modelos y componentes de IA tienen cadena de suministro: procedencia (quién lo entrenó y con qué), licencias (qué uso permiten), integridad (que el artefacto no fue alterado) y evaluación (que se comporta como se declara) antes de su uso.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** Modelos y componentes de IA tienen cadena de suministro: procedencia (quién lo entrenó y con qué), licencias (qué uso permiten), integridad (que el artefacto no fue alterado) y evaluación (que se comporta como se declara) antes de su uso. La tesis es que el owner necesita un AI BOM —inventario de modelos, conectores, servidores MCP, bibliotecas y fuentes— equivalente al SBOM, y criterios de aceptación por componente.

**Tensión y límites.** La tensión es la opacidad de los proveedores (datos de entrenamiento no divulgados) y la velocidad de cambio (versiones frecuentes). Otra tensión es la cadena indirecta: un conector de un tercero que llama a otro modelo. El ensayo debe proponer qué exigir y qué aceptar como no verificable.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: C-SCRM (SP 800-161), SBOM/AI BOM, OWASP LLM03/ASI04. Implementación: AI BOM de la flota (modelos del catálogo de Foundry con sus fichas, conectores certificados, servidores MCP aprobados, bibliotecas), criterios de aceptación y revisión ante cambios.

**Evidencia y evaluación.** Evidencia: AI BOM completo con procedencia, licencia, integridad y evaluación por componente. Se evalúa la cobertura de componentes indirectos.

**Puentes.** Se apoya en HC-031 (cadena de suministro de software); se relaciona con AMP-20, AMP-42 y AMP-50; sostiene AGC-20.

**Recomendaciones de práctica y ejercitación.**
1. Construir el AI BOM de la flota (modelos, conectores, MCP, bibliotecas, fuentes).
2. Definir criterios de aceptación por tipo de componente.
3. Identificar componentes indirectos y su riesgo.

**Próximos pasos.**
- Registrar como AGC-20.
- Revisar ante cambios de versión.
- Conectar con el anexo contractual (M1.2-PA02).

**Relación con los conceptos de la(s) unidad(es) M6.2.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M6.2-K01 | K | C-SCRM (Cadena Suministro) | misma unidad |
| M6.2-K02 | K | Seguridad Nube | misma unidad |
| M6.2-K03 | K | DevSecOps | misma unidad |
| M6.2-K04 | K | Seguridad IA | misma unidad |
| M6.2-K05 | K | IoT/OT Security | misma unidad |
| M6.2-K06 | K | Shadow AI | misma unidad |
| M6.2-K07 | K | Responsabilidad Compartida | misma unidad |
| M6.2-K08 | K | Riesgo Terceros (TPRM) | misma unidad |
| M6.2-K09 | K | SDLC Seguro | misma unidad |
| M6.2-K10 | K | SBOM | misma unidad |
| AMP-50 | AMP | Seguridad de herramientas y conectores | misma unidad |
| AMP-51 | AMP | Postura de IA en nube | misma unidad |
| HC-008 | HC | Cadena de confianza en terceros | misma unidad |
| HC-011 | HC | Seguridad de datos en la IA empresarial | misma unidad |
| HC-023 | HC | Riesgo de concentración tecnológica | misma unidad |
| HC-024 | HC | Cumplimiento y privacidad por diseño | misma unidad |
| HC-029 | HC | Aseguramiento de terceros y cadena de suministro | misma unidad |
| HC-030 | HC | Seguridad industrial y continuidad de negocio | misma unidad |
| HC-031 | HC | Seguridad del software y confianza en componentes | misma unidad |
| HC-032 | HC | Evaluación adversarial de sistemas autónomos | misma unidad |
| HC-033 | HC | Seguridad y soberanía de datos distribuidos | misma unidad |
| M6.2-PA01 | PA | Plataformas y rutas de construcción de agentes y responsabilidad compartida en IA | misma unidad |
| M6.2-PA02 | PA | AgentOps / ALM de agentes | misma unidad |
| M6.2-PA03 | PA | Bases multiplataforma, multicloud y multimodelo | misma unidad |

**Pregunta generadora:** ¿De cuántos componentes de terceros depende su agente más crítico, y de cuántos conoce la procedencia?

---

### 092. AMP-50 — Seguridad de herramientas y conectores

**Unidad:** M6.2 Seguridad en Redes, Nube, Tecnologías Emergentes y SCRM · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Referencias por ID (V7-C09):** OWASP ASI04/ASI02 (2026 v2.01); CSA AICM AIS-11 · **Extensión:** 198 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** Conectores (incluido MCP) y herramientas amplían lo que un agente puede tocar: cada uno es una puerta hacia un sistema con sus propios permisos.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** Conectores (incluido MCP) y herramientas amplían lo que un agente puede tocar: cada uno es una puerta hacia un sistema con sus propios permisos. Requieren inventario (qué conectores existen y cuáles usa cada agente), autenticación propia (identidad del agente, no del constructor), permisos mínimos por operación y monitoreo de invocaciones. La tesis es que la seguridad de un agente se decide en sus conectores tanto como en su modelo.

**Tensión y límites.** La tensión es la riqueza del ecosistema (miles de conectores) frente a la capacidad de revisar cada uno. Otra tensión es MCP: un protocolo abierto que facilita integrar y también facilita que un servidor malicioso o comprometido inyecte herramientas. El ensayo debe proponer una lista de servidores MCP aprobados.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: gestión de integraciones, OAuth2, OWASP ASI04/ASI02, allowlists. Implementación: inventario de conectores y servidores MCP aprobados (Sentinel MCP en preview, Microsoft MCP Server for Enterprise solo lectura, Learn Docs MCP), políticas de datos de Power Platform, permisos por operación, registro de invocaciones.

**Evidencia y evaluación.** Evidencia: inventario de conectores/MCP aprobados con permisos y estado; política de datos aplicada. Se evalúa que ningún agente use conectores fuera de la lista.

**Puentes.** Extiende M6.2-K04; se relaciona con AMP-36, AMP-49 y M6.2-PA01; sostiene AGC-06 y AGC-20.

**Recomendaciones de práctica y ejercitación.**
1. Inventariar conectores y servidores MCP en uso y definir la lista aprobada.
2. Aplicar la política de datos de Power Platform que bloquea el resto.
3. Revisar permisos por operación y registro de invocaciones de los conectores de escritura.

**Próximos pasos.**
- Registrar como AGC-06/AGC-20.
- Incluir MCP en el AI BOM (AMP-49).
- Revisar al agregar conectores (ChangeSet).

**Relación con los conceptos de la(s) unidad(es) M6.2.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M6.2-K01 | K | C-SCRM (Cadena Suministro) | misma unidad |
| M6.2-K02 | K | Seguridad Nube | misma unidad |
| M6.2-K03 | K | DevSecOps | misma unidad |
| M6.2-K04 | K | Seguridad IA | misma unidad |
| M6.2-K05 | K | IoT/OT Security | misma unidad |
| M6.2-K06 | K | Shadow AI | misma unidad |
| M6.2-K07 | K | Responsabilidad Compartida | misma unidad |
| M6.2-K08 | K | Riesgo Terceros (TPRM) | misma unidad |
| M6.2-K09 | K | SDLC Seguro | misma unidad |
| M6.2-K10 | K | SBOM | misma unidad |
| AMP-49 | AMP | Supply chain de modelos | misma unidad |
| AMP-51 | AMP | Postura de IA en nube | misma unidad |
| HC-008 | HC | Cadena de confianza en terceros | misma unidad |
| HC-011 | HC | Seguridad de datos en la IA empresarial | misma unidad |
| HC-023 | HC | Riesgo de concentración tecnológica | misma unidad |
| HC-024 | HC | Cumplimiento y privacidad por diseño | misma unidad |
| HC-029 | HC | Aseguramiento de terceros y cadena de suministro | misma unidad |
| HC-030 | HC | Seguridad industrial y continuidad de negocio | misma unidad |
| HC-031 | HC | Seguridad del software y confianza en componentes | misma unidad |
| HC-032 | HC | Evaluación adversarial de sistemas autónomos | misma unidad |
| HC-033 | HC | Seguridad y soberanía de datos distribuidos | misma unidad |
| M6.2-PA01 | PA | Plataformas y rutas de construcción de agentes y responsabilidad compartida en IA | misma unidad |
| M6.2-PA02 | PA | AgentOps / ALM de agentes | misma unidad |
| M6.2-PA03 | PA | Bases multiplataforma, multicloud y multimodelo | misma unidad |

**Pregunta generadora:** Si un servidor MCP que usan sus agentes fuera comprometido, ¿qué podría hacer en su tenant y cómo lo notaría?

---

### 093. AMP-51 — Postura de IA en nube

**Unidad:** M6.2 Seguridad en Redes, Nube, Tecnologías Emergentes y SCRM · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 179 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** La postura de IA en la nube descubre modelos, endpoints, datos y configuraciones riesgosas en servicios como Foundry u OpenAI —endpoints públicos, claves expuestas, modelos sin filtros, recursos sin dueño— y prioriza su corrección.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** La postura de IA en la nube descubre modelos, endpoints, datos y configuraciones riesgosas en servicios como Foundry u OpenAI —endpoints públicos, claves expuestas, modelos sin filtros, recursos sin dueño— y prioriza su corrección. La tesis es que los recursos de IA son recursos de nube con riesgos adicionales y que la gestión de postura (AI-SPM) debe incluirlos con la misma cadencia que el resto.

**Tensión y límites.** La tensión es la proliferación de recursos de IA fuera del control del SOC (equipos de datos, desarrollo). Otra tensión es la novedad de los hallazgos: el equipo de postura puede no saber interpretarlos. El ensayo debe conectar la postura de IA con el inventario de agentes.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: CSPM/AI-SPM, CIS Benchmarks, configuración segura. Implementación: Defender for Cloud (postura de IA) sobre los recursos de Foundry del alcance, informe AI-SPM, conexión con el inventario de agentes y con Secure Score.

**Evidencia y evaluación.** Evidencia: informe AI-SPM del alcance con hallazgos priorizados y corregidos. Se evalúa la cobertura de todos los recursos que usa la flota.

**Puentes.** Extiende M6.2-K02 (seguridad nube); se relaciona con AMP-50 y M2.1-PA01; sostiene AGC-14.

**Recomendaciones de práctica y ejercitación.**
1. Ejecutar la evaluación de postura de IA sobre los recursos de Foundry del alcance.
2. Reconciliar los recursos con el inventario de agentes.
3. Corregir los tres hallazgos de mayor severidad.

**Próximos pasos.**
- Incorporar a la cadencia de postura (MDO-W05).
- Alimentar el registro de agentes (M2.1-PA01).
- Revisar al crear recursos nuevos.

**Relación con los conceptos de la(s) unidad(es) M6.2.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M6.2-K01 | K | C-SCRM (Cadena Suministro) | misma unidad |
| M6.2-K02 | K | Seguridad Nube | misma unidad |
| M6.2-K03 | K | DevSecOps | misma unidad |
| M6.2-K04 | K | Seguridad IA | misma unidad |
| M6.2-K05 | K | IoT/OT Security | misma unidad |
| M6.2-K06 | K | Shadow AI | misma unidad |
| M6.2-K07 | K | Responsabilidad Compartida | misma unidad |
| M6.2-K08 | K | Riesgo Terceros (TPRM) | misma unidad |
| M6.2-K09 | K | SDLC Seguro | misma unidad |
| M6.2-K10 | K | SBOM | misma unidad |
| AMP-49 | AMP | Supply chain de modelos | misma unidad |
| AMP-50 | AMP | Seguridad de herramientas y conectores | misma unidad |
| HC-008 | HC | Cadena de confianza en terceros | misma unidad |
| HC-011 | HC | Seguridad de datos en la IA empresarial | misma unidad |
| HC-023 | HC | Riesgo de concentración tecnológica | misma unidad |
| HC-024 | HC | Cumplimiento y privacidad por diseño | misma unidad |
| HC-029 | HC | Aseguramiento de terceros y cadena de suministro | misma unidad |
| HC-030 | HC | Seguridad industrial y continuidad de negocio | misma unidad |
| HC-031 | HC | Seguridad del software y confianza en componentes | misma unidad |
| HC-032 | HC | Evaluación adversarial de sistemas autónomos | misma unidad |
| HC-033 | HC | Seguridad y soberanía de datos distribuidos | misma unidad |
| M6.2-PA01 | PA | Plataformas y rutas de construcción de agentes y responsabilidad compartida en IA | misma unidad |
| M6.2-PA02 | PA | AgentOps / ALM de agentes | misma unidad |
| M6.2-PA03 | PA | Bases multiplataforma, multicloud y multimodelo | misma unidad |

**Pregunta generadora:** ¿Cuántos endpoints de modelos existen hoy en su suscripción de Azure, y cuántos sabe quién los creó?

---

### 094. AMP-52 — Content safety y riesgos de contenido generado

**Unidad:** G6.2 · M3.2 Liderazgo Ético y Medición de Efectividad · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V7 (V7-C07, cierra INC-03) · **Extensión:** 214 palabras · **Estado:** Idea central desarrollada (lote V7-01); ID curricular, no ESS.

**Definición / idea central.** Los sistemas generativos pueden producir contenido dañino, abusivo o engañoso aunque el objetivo sea legítimo; los guardrails de salida son un control de seguridad y de ética, con alcance declarado (qué riesgos de contenido quedan fuera del rol).

**Origen.** V7 (V7-C07, cierra INC-03)

**Tesis y sentido para el rol.** Los sistemas generativos pueden producir contenido dañino, abusivo, engañoso u ofensivo aunque su objetivo sea legítimo: un agente que redacta concientización o reportes puede generar texto inapropiado, inventar hechos o reproducir sesgos. Los guardrails de salida —filtros de contenido, validación de formato, revisión humana de lo publicable— son a la vez control de seguridad y control ético. La tesis es que el owner debe declarar qué riesgos de contenido trata (dañino, abusivo, desinformación) y cuáles quedan fuera del rol (CBRN, impacto ambiental), para no prometer coberturas que no gobierna.

**Tensión y límites.** La tensión es que los filtros de contenido afectan la utilidad (falsos positivos en lenguaje de seguridad: 'ataque', 'explotar') y que la desinformación generada (confabulación) no se filtra con listas. El ensayo debe combinar filtros, formato fijo y revisión humana según el destino de la salida.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: NIST AI 600-1 (contenido peligroso, abusivo, integridad de la información), OWASP LLM05/LLM09, IA responsable. Implementación: Azure AI Content Safety/Prompt Shields en Foundry, formato fijo de salida (SK-06), publicación solo humana para AG-12, etiquetado epistemológico (AMP-19); declaración de alcance de riesgos de contenido.

**Evidencia y evaluación.** Evidencia: configuración de guardrails verificada y declaración de alcance aprobada. Se evalúa la honestidad sobre lo que queda fuera.

**Puentes.** Se relaciona con AMP-25, AMP-26 y AMP-19; sostiene AGC-08 y M3.2-PA02. Nuevo en V7 (cierra INC-03).

**Recomendaciones de práctica y ejercitación.**
1. Configurar y probar guardrails de salida para AG-12 y AG-05.
2. Redactar la declaración de alcance de riesgos de contenido del rol.
3. Probar casos límite (lenguaje de seguridad legítimo vs. contenido dañino).

**Próximos pasos.**
- Registrar como AGC-08.
- Incluir en la política de agentes.
- Revisar con cambios de modelo.

**Relación con los conceptos de la(s) unidad(es) G6.2 · M3.2.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| G6.2-K01 | K | Liderazgo Ético | misma unidad |
| G6.2-K02 | K | Conducta Profesional | misma unidad |
| G6.2-K03 | K | Conflictos Interés | misma unidad |
| G6.2-K04 | K | Debida Diligencia | misma unidad |
| G6.2-K05 | K | Métricas Gobierno | misma unidad |
| G6.2-K06 | K | Efectividad Programa | misma unidad |
| G6.2-K07 | K | Mejora Continua | misma unidad |
| G6.2-K08 | K | Aseguramiento | misma unidad |
| G6.2-K09 | K | Balance Riesgo-Valor | misma unidad |
| G6.2-K10 | K | Rendición Cuentas | misma unidad |
| M3.2-K01 | K | Controles de Seguridad | misma unidad |
| M3.2-K02 | K | NIST SP 800-53 | misma unidad |
| M3.2-K03 | K | Selección y Adaptación | misma unidad |
| M3.2-K04 | K | Evaluación (Assess) | misma unidad |
| M3.2-K05 | K | Implementación | misma unidad |
| M3.2-K06 | K | Pentesting | misma unidad |
| M3.2-K07 | K | Controles Compensatorios | misma unidad |
| M3.2-K08 | K | Familias de Controles | misma unidad |
| M3.2-K09 | K | Pruebas de Efectividad | misma unidad |
| M3.2-K10 | K | POA&M | misma unidad |
| AMP-25 | AMP | Ética de autonomía | misma unidad |
| AMP-26 | AMP | Supervisión humana efectiva | misma unidad |
| AMP-37 | AMP | Evaluación adversarial de agentes | misma unidad |
| AMP-38 | AMP | Pruebas de controles autónomos | misma unidad |
| HC-002 | HC | Apetito de riesgo convertido en arquitectura | misma unidad |
| HC-003 | HC | Riesgo residual y aceptación verificable | misma unidad |
| HC-004 | HC | Política como código gobernado | misma unidad |
| HC-005 | HC | Cumplimiento continuo orientado a resultados | misma unidad |
| HC-006 | HC | Valor de seguridad y medición causal | misma unidad |
| HC-012 | HC | Confianza verificable en decisiones de IA | misma unidad |
| HC-015 | HC | Gobierno y operación de Zero Trust | misma unidad |
| HC-018 | HC | Observabilidad y aseguramiento de controles | misma unidad |
| HC-021 | HC | Recuperación como prueba de confianza | misma unidad |
| HC-026 | HC | Ética, cultura y controles internos | misma unidad |
| HC-027 | HC | Métricas que no engañan | misma unidad |
| HC-028 | HC | Gestión de excepciones y compensaciones | misma unidad |
| HC-031 | HC | Seguridad del software y confianza en componentes | misma unidad |
| HC-032 | HC | Evaluación adversarial de sistemas autónomos | misma unidad |
| HC-034 | HC | Decisiones reversibles y riesgo de transición | misma unidad |
| HC-036 | HC | Portafolio de controles y capacidades | misma unidad |
| HC-038 | HC | Aseguramiento de la arquitectura Zero Trust | misma unidad |
| G6.2-PA01 | PA | Métricas de efectividad del gobierno de la flota | misma unidad |
| M3.2-PA01 | PA | El control como producto: objetivo → configuración → evidencia | misma unidad |
| M3.2-PA02 | PA | Catálogo de controles de gobierno y gestión de agentes (AGC) | misma unidad |
| M3.2-PA03 | PA | Evaluación de calidad de agentes: datasets dorados, regresión y criterios de aceptación | misma unidad |

**Pregunta generadora:** ¿Qué contenido podría generar hoy un agente suyo que usted no querría ver publicado con el logo de la organización?

---

### 095. G2.1-K11 — CSF 2.0 completo: funciones, categorías y perfiles organizacionales

**Unidad:** G2.1 Selección e Integración de Marcos y Estándares · **Tipo:** K · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V7 (V7-C01, cierra INC-09) · **Extensión:** 251 palabras · **Estado:** Idea central desarrollada (lote V7-01); ID curricular, no ESS.

**Definición / idea central.** NIST CSF 2.0 solo gobierna cuando se usa entero: las seis funciones y sus 22 categorías como lenguaje común de resultados, y los perfiles (actual/objetivo) como instrumento de decisión; enseñar solo Govern deja a ID/PR/DE/RS/RC implícitos y sin dueño.

**Origen.** V7 (V7-C01, cierra INC-09)

**Tesis y sentido para el rol.** NIST CSF 2.0 solo gobierna cuando se usa entero. Las seis funciones (Govern, Identify, Protect, Detect, Respond, Recover) y sus 22 categorías son un lenguaje común de resultados de seguridad; los perfiles organizacionales (actual y objetivo) convierten ese lenguaje en decisiones de inversión; los niveles (tiers) describen el rigor del gobierno del riesgo. Enseñar solo Govern (AMP-07) deja a las otras cinco funciones implícitas en las unidades de gestión y sin dueño explícito. La tesis es que el CISO debe dominar el CSF completo como mapa de ownership y de conversación con la dirección, y usar perfiles —no listas de controles— para decidir.

**Tensión y límites.** La tensión es que el CSF no es un estándar de cumplimiento ni un catálogo de controles: es un marco de resultados que requiere referencias informativas a otros (SP 800-53, ISO 27001, CIS). Confundirlo con un checklist lo degrada. Otra tensión es la de los perfiles: construirlos exige datos y acuerdo que muchas organizaciones no tienen.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: NIST CSF 2.0 (funciones, categorías, subcategorías, perfiles, tiers, referencias informativas). Implementación: grilla de ownership del control de correo con las 22 categorías (G2.1-PA01), perfil actual/objetivo del dominio productividad, y uso de las referencias informativas para elegir controles concretos.

**Evidencia y evaluación.** Evidencia: perfil actual/objetivo del dominio con brechas priorizadas y la grilla de ownership completa. Se evalúa el uso correcto de categorías y la distinción entre marco y catálogo.

**Puentes.** Completa G2.1-K04 (NIST CSF) y AMP-07 (Govern); es la base de G2.1-PA01; se relaciona con HC-015, HC-038 y AMP-08. Nuevo en V7 (cierra INC-09).

**Recomendaciones de práctica y ejercitación.**
1. Construir el perfil actual/objetivo del dominio productividad con las 22 categorías.
2. Completar la grilla de ownership (G2.1-PA01) y detectar categorías sin dueño.
3. Elegir, vía referencias informativas, los controles concretos para tres brechas.

**Próximos pasos.**
- Presentar el perfil al comité como base de inversión.
- Repetir el perfil anualmente.
- Extender a los demás dominios Zero Trust.

**Relación con los conceptos de la(s) unidad(es) G2.1.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| G2.1-K01 | K | Marcos de Gobierno | misma unidad |
| G2.1-K02 | K | COBIT | misma unidad |
| G2.1-K03 | K | ISO 27001 (SGSI) | misma unidad |
| G2.1-K04 | K | NIST CSF | misma unidad |
| G2.1-K05 | K | Estándares Relevantes | misma unidad |
| G2.1-K06 | K | Adaptación (Tailoring) | misma unidad |
| G2.1-K07 | K | Interoperabilidad | misma unidad |
| G2.1-K08 | K | Medición de Madurez | misma unidad |
| G2.1-K09 | K | Tendencias en Marcos | misma unidad |
| G2.1-K10 | K | Evolución Histórica | misma unidad |
| AMP-07 | AMP | NIST CSF 2.0 Govern | misma unidad |
| AMP-08 | AMP | Referencias informativas y no equivalencia | misma unidad |
| G2.1-PA01 | PA | Grilla de ownership: NIST CSF 2.0 × dominios Zero Trust | misma unidad |
| G2.1-PA02 | PA | Marcos de gobierno de IA aplicados: NIST AI RMF e ISO/IEC 42001 | misma unidad |

**Pregunta generadora:** Si tuviera que explicar a su directorio en una página dónde está hoy la organización y dónde debería estar, ¿podría hacerlo con las 22 categorías del CSF?

---

### 096. M3.1-K11 — Arquitectura empresarial y arquitectura de seguridad de la información

**Unidad:** M3.1 Arquitectura de Seguridad, Ingeniería y Diseño (Incl. Zero Trust) · **Tipo:** K · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V7 (V7-C02, cierra INC-07) · **Extensión:** 249 palabras · **Estado:** Idea central desarrollada (lote V7-01); ID curricular, no ESS.

**Definición / idea central.** La arquitectura de seguridad de la información es una vista de la arquitectura empresarial: sin ese vínculo los controles se diseñan contra sistemas y no contra capacidades de negocio; CISM 2026 lo incorpora como contenido examinable.

**Origen.** V7 (V7-C02, cierra INC-07)

**Tesis y sentido para el rol.** La arquitectura de seguridad de la información es una vista de la arquitectura empresarial: describe cómo las capacidades de seguridad sirven a las capacidades de negocio, qué principios las gobiernan y cómo evolucionan con la organización. Sin ese vínculo, los controles se diseñan contra sistemas aislados y no contra lo que el negocio necesita proteger. CISM 2026 incorpora la arquitectura empresarial y de seguridad como contenido examinable, reconociendo que el CISO debe hablar el lenguaje de los arquitectos. La tesis es que el programa de seguridad necesita una arquitectura de referencia propia, trazable a la arquitectura empresarial y a los pilares Zero Trust.

**Tensión y límites.** La tensión es que la arquitectura empresarial suele ser débil o inexistente, y la de seguridad se construye en el vacío. Otra tensión es la de los marcos (TOGAF, SABSA): pesados para programas pequeños. El ensayo debe proponer una arquitectura mínima viable: capacidades, principios, vistas y decisiones registradas.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: TOGAF/SABSA (principios), SP 800-207, modelos de capacidades. Implementación: arquitectura de referencia del programa con vistas de negocio (capacidades protegidas), de seguridad (pilares Zero Trust y productos-control) y de tecnología (Microsoft Security stack), más el SOC agéntico (M3.1-PA01) como vista operativa; registro de decisiones de arquitectura (ADR).

**Evidencia y evaluación.** Evidencia: arquitectura de referencia en tres vistas con ADRs y trazabilidad a capacidades de negocio. Se evalúa la conexión real con el negocio y no solo con la tecnología.

**Puentes.** Extiende M3.1-K01/K02 (arquitectura, TOGAF) y G1.2-K01 (estrategia); se relaciona con HC-015, M3.1-PA01 y M1.1-PA02. Nuevo en V7 (cierra INC-07, CISM 2026).

**Recomendaciones de práctica y ejercitación.**
1. Dibujar la arquitectura de referencia del programa en tres vistas (negocio, seguridad, tecnología).
2. Escribir tres ADRs de decisiones recientes.
3. Trazar el control de correo a una capacidad de negocio.

**Próximos pasos.**
- Someterla al equipo de arquitectura empresarial.
- Usarla en el portafolio de productos-control (M1.1-PA02).
- Revisarla anualmente.

**Relación con los conceptos de la(s) unidad(es) M3.1.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M3.1-K01 | K | Arquitectura de Seguridad | misma unidad |
| M3.1-K02 | K | Ingeniería de Seguridad | misma unidad |
| M3.1-K03 | K | Zero Trust (Arquitectura) | misma unidad |
| M3.1-K04 | K | Diseño Seguro (SbD) | misma unidad |
| M3.1-K05 | K | TOGAF y Seguridad | misma unidad |
| M3.1-K06 | K | ZTNA (Acceso) | misma unidad |
| M3.1-K07 | K | Microsegmentación | misma unidad |
| M3.1-K08 | K | Defensa en Profundidad | misma unidad |
| M3.1-K09 | K | Mínimo Privilegio (Arquitectura) | misma unidad |
| M3.1-K10 | K | Resiliencia (Diseño) | misma unidad |
| AMP-35 | AMP | Arquitectura de sistemas agénticos | misma unidad |
| AMP-36 | AMP | Límites de herramientas y permisos | misma unidad |
| HC-002 | HC | Apetito de riesgo convertido en arquitectura | misma unidad |
| HC-010 | HC | Autonomía delegada y límites de acción | misma unidad |
| HC-013 | HC | Deuda de seguridad como riesgo de transformación | misma unidad |
| HC-014 | HC | Arquitectura de riesgo empresarial | misma unidad |
| HC-015 | HC | Gobierno y operación de Zero Trust | misma unidad |
| HC-023 | HC | Riesgo de concentración tecnológica | misma unidad |
| HC-030 | HC | Seguridad industrial y continuidad de negocio | misma unidad |
| HC-034 | HC | Decisiones reversibles y riesgo de transición | misma unidad |
| HC-038 | HC | Aseguramiento de la arquitectura Zero Trust | misma unidad |
| HC-040 | HC | Homeostasis organizacional de seguridad | misma unidad |
| M3.1-K12 | K | Seguridad física, ambiental y mantenimiento como dependencias del control | misma unidad |
| M3.1-PA01 | PA | Arquitectura de referencia del SOC agéntico con control plane | misma unidad |
| M3.1-PA02 | PA | Arquitectura de protección del dominio Zero Trust (instancias: correo y colaboración · detección y respuesta unificada · endpoints · identidades · datos) | misma unidad |

**Pregunta generadora:** ¿Qué capacidad de negocio protege el control de correo de su organización, y figura en algún mapa de arquitectura que alguien fuera de seguridad haya visto?

---

### 097. M3.1-K12 — Seguridad física, ambiental y mantenimiento como dependencias del control

**Unidad:** M3.1 Arquitectura de Seguridad, Ingeniería y Diseño (Incl. Zero Trust) · **Tipo:** K · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V7 (V7-C08, cierra INC-01) · **Extensión:** 249 palabras · **Estado:** Idea central desarrollada (lote V7-01); ID curricular, no ESS.

**Definición / idea central.** Ningún control lógico sobrevive a una sala de servidores sin control de acceso, a un centro de datos sin energía o a un sistema sin mantenimiento; aunque el CISO rara vez los opere, debe gobernarlos como dependencias y exigir evidencia a quien los opera.

**Origen.** V7 (V7-C08, cierra INC-01)

**Tesis y sentido para el rol.** Ningún control lógico sobrevive a una sala de servidores sin control de acceso, a un centro de datos sin energía o a un sistema sin mantenimiento. Aunque el CISO rara vez opere la seguridad física, ambiental y el mantenimiento, debe gobernarlos como dependencias: saber quién los opera, qué evidencia producen y qué pasa cuando fallan. En la nube, la dependencia se traslada al proveedor (responsabilidad compartida) y la evidencia a sus certificaciones. La tesis es que el programa debe declarar explícitamente estas dependencias y su evidencia, o declarar su exclusión; lo que no puede es ignorarlas.

**Tensión y límites.** La tensión es que son dominios de otros (facilities, TI, proveedores) y el CISO no quiere invadirlos; pero SP 800-53 PE y MA, ISO 27001 A.7 y los auditores sí los miran. Otra tensión es la nube: 'lo hace Microsoft' es cierto para el centro de datos, no para el dispositivo del analista ni para el mantenimiento de los sistemas propios.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: SP 800-53 PE y MA, ISO 27001 controles físicos, CCM DCS, responsabilidad compartida. Implementación: matriz de dependencias físicas y de mantenimiento del control (centros de datos de Microsoft vía certificaciones; dispositivos del SOC; mantenimiento de integraciones y agentes) con dueño y evidencia; declaración de alcance.

**Evidencia y evaluación.** Evidencia: matriz de dependencias con dueño, evidencia (certificaciones, informes) y exclusiones declaradas. Se evalúa la honestidad sobre lo que el programa no gobierna.

**Puentes.** Extiende M3.1-K08 (defensa en profundidad) y M6.1-K10 (dependencias); se relaciona con HC-030 (OT/IoT) y M6.2-K07 (responsabilidad compartida). Nuevo en V7 (cierra INC-01).

**Recomendaciones de práctica y ejercitación.**
1. Construir la matriz de dependencias físicas y de mantenimiento del control.
2. Recolectar la evidencia del proveedor (certificaciones) y la propia (dispositivos, mantenimiento).
3. Redactar la declaración de alcance y exclusiones.

**Próximos pasos.**
- Incorporar a la ficha de producto-control.
- Incluir en el plan de continuidad (M6.1).
- Revisar con auditoría interna.

**Relación con los conceptos de la(s) unidad(es) M3.1.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M3.1-K01 | K | Arquitectura de Seguridad | misma unidad |
| M3.1-K02 | K | Ingeniería de Seguridad | misma unidad |
| M3.1-K03 | K | Zero Trust (Arquitectura) | misma unidad |
| M3.1-K04 | K | Diseño Seguro (SbD) | misma unidad |
| M3.1-K05 | K | TOGAF y Seguridad | misma unidad |
| M3.1-K06 | K | ZTNA (Acceso) | misma unidad |
| M3.1-K07 | K | Microsegmentación | misma unidad |
| M3.1-K08 | K | Defensa en Profundidad | misma unidad |
| M3.1-K09 | K | Mínimo Privilegio (Arquitectura) | misma unidad |
| M3.1-K10 | K | Resiliencia (Diseño) | misma unidad |
| AMP-35 | AMP | Arquitectura de sistemas agénticos | misma unidad |
| AMP-36 | AMP | Límites de herramientas y permisos | misma unidad |
| HC-002 | HC | Apetito de riesgo convertido en arquitectura | misma unidad |
| HC-010 | HC | Autonomía delegada y límites de acción | misma unidad |
| HC-013 | HC | Deuda de seguridad como riesgo de transformación | misma unidad |
| HC-014 | HC | Arquitectura de riesgo empresarial | misma unidad |
| HC-015 | HC | Gobierno y operación de Zero Trust | misma unidad |
| HC-023 | HC | Riesgo de concentración tecnológica | misma unidad |
| HC-030 | HC | Seguridad industrial y continuidad de negocio | misma unidad |
| HC-034 | HC | Decisiones reversibles y riesgo de transición | misma unidad |
| HC-038 | HC | Aseguramiento de la arquitectura Zero Trust | misma unidad |
| HC-040 | HC | Homeostasis organizacional de seguridad | misma unidad |
| M3.1-K11 | K | Arquitectura empresarial y arquitectura de seguridad de la información | misma unidad |
| M3.1-PA01 | PA | Arquitectura de referencia del SOC agéntico con control plane | misma unidad |
| M3.1-PA02 | PA | Arquitectura de protección del dominio Zero Trust (instancias: correo y colaboración · detección y respuesta unificada · endpoints · identidades · datos) | misma unidad |

**Pregunta generadora:** Si la sala donde trabajan sus analistas quedara sin acceso controlado durante un fin de semana, ¿quién lo sabría y qué evidencia se perdería?

---

### 098. M4.1-K11 — Deception y señuelos como control detectivo

**Unidad:** M4.1 Operaciones de Seguridad, Monitorización e Inteligencia · **Tipo:** K · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V7 (V7-C05, cierra INC-02) · **Referencias por ID (V7-C09):** MITRE D3FEND Deceive (D3-DO, D3-DE); MITRE Engage · **Extensión:** 230 palabras · **Estado:** Idea central desarrollada (lote V7-01); ID curricular, no ESS.

**Definición / idea central.** El engaño defensivo (honeytokens, cuentas y buzones señuelo, credenciales trampa) produce detecciones de alta fidelidad porque nadie legítimo debería tocarlos; en un SOC con agentes, los señuelos también detectan agentes que exceden su alcance.

**Origen.** V7 (V7-C05, cierra INC-02)

**Tesis y sentido para el rol.** El engaño defensivo —honeytokens, cuentas y buzones señuelo, credenciales trampa, documentos cebo— produce detecciones de alta fidelidad porque nadie legítimo debería tocarlos: cualquier interacción es señal. En un SOC con agentes, los señuelos cumplen una segunda función: detectan agentes que exceden su alcance (un agente que lee un buzón señuelo está haciendo algo que su ficha no autoriza). La tesis es que deception es el control detectivo de mejor relación señal/ruido y que su ausencia en el programa es una brecha frente a D3FEND Deceive.

**Tensión y límites.** La tensión es ética y legal (engañar, registrar), operativa (mantener señuelos creíbles cuesta) y de alcance (no confundir deception con entrampar a empleados). Otra tensión es que los agentes propios pueden disparar señuelos por diseño si se les da acceso amplio; eso es precisamente la señal útil.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: MITRE D3FEND Deceive (decoy objects, decoy environments), MITRE Engage, detección de alta fidelidad. Implementación: buzones y cuentas señuelo en el tenant con alertas en Sentinel, honeytokens en fuentes de conocimiento de agentes, detección personalizada de acceso a señuelos; política que prohíbe a los agentes tocarlos.

**Evidencia y evaluación.** Evidencia: tres señuelos desplegados con detecciones probadas y una prueba con un agente que excede su alcance. Se evalúa la fidelidad de la señal y el marco legal/ético.

**Puentes.** Extiende M4.1-K07 (hunting) y K02 (monitorización); se relaciona con HC-017 (inteligencia y detección) y M4.1-PA05 (observabilidad de agentes). Nuevo en V7 (cierra INC-02).

**Recomendaciones de práctica y ejercitación.**
1. Desplegar un buzón señuelo y un honeytoken en una knowledge source de prueba.
2. Escribir las detecciones personalizadas y probarlas.
3. Hacer que un agente de prueba exceda su alcance y verificar la alerta.

**Próximos pasos.**
- Incorporar los señuelos al modelo operativo (revisión semanal).
- Registrar el marco legal/ético con Legal.
- Extender a identidades y documentos.

**Relación con los conceptos de la(s) unidad(es) M4.1.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M4.1-K01 | K | SOC Moderno | misma unidad |
| M4.1-K02 | K | Monitorización Continua | misma unidad |
| M4.1-K03 | K | Threat Intelligence (CTI) | misma unidad |
| M4.1-K04 | K | SIEM | misma unidad |
| M4.1-K05 | K | SOAR | misma unidad |
| M4.1-K06 | K | XDR | misma unidad |
| M4.1-K07 | K | Threat Hunting | misma unidad |
| M4.1-K08 | K | IA en SecOps | misma unidad |
| M4.1-K09 | K | Ciclo Vida Inteligencia | misma unidad |
| M4.1-K10 | K | TTPs | misma unidad |
| AMP-39 | AMP | SOC agéntico | misma unidad |
| AMP-40 | AMP | Human-in-the-loop | misma unidad |
| HC-001 | HC | Gobierno de decisiones basadas en evidencia | misma unidad |
| HC-005 | HC | Cumplimiento continuo orientado a resultados | misma unidad |
| HC-010 | HC | Autonomía delegada y límites de acción | misma unidad |
| HC-012 | HC | Confianza verificable en decisiones de IA | misma unidad |
| HC-017 | HC | Inteligencia que modifica decisiones | misma unidad |
| HC-018 | HC | Observabilidad y aseguramiento de controles | misma unidad |
| HC-019 | HC | SOC agéntico con supervisión humana | misma unidad |
| HC-040 | HC | Homeostasis organizacional de seguridad | misma unidad |
| M4.1-PA01 | PA | Modelo operativo del producto-control por cadencias (instancias: Defender for Office 365 · Defender XDR · Defender for Endpoint · Defender for Identity/Entra · Purview · Sentinel · Defender for Cloud) | misma unidad |
| M4.1-PA02 | PA | Gestión de incidentes y alertas en Defender XDR | misma unidad |
| M4.1-PA03 | PA | Gestión de la calidad de detección del dominio: FP/FN, tuning, listas, indicadores y supresiones (instancias: MDO · XDR · MDE · MDI/ID Protection · Purview DLP · Sentinel) | misma unidad |
| M4.1-PA04 | PA | Hunting y detecciones personalizadas | misma unidad |
| M4.1-PA05 | PA | Observabilidad de la flota de agentes: telemetría, trazas y tableros | misma unidad |
| M4.1-PA06 | PA | Gestión del desempeño de agentes: revisión periódica y drift | misma unidad |

**Pregunta generadora:** ¿Qué objeto de su tenant, si alguien lo tocara, le daría la certeza de que algo anda mal, y existe hoy?

---

### 099. M4.2-K11 — Escalamiento de privilegios en identidades humanas y no humanas como táctica adversaria

**Unidad:** M4.2 Gestión de Amenazas, Vulnerabilidades y Riesgos Emergentes · **Tipo:** K · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V7 (V7-C06, cierra INC-04) · **Referencias por ID (V7-C09):** MITRE ATT&CK TA0004; OWASP ASI03; OWASP NHI Top 10 · **Extensión:** 233 palabras · **Estado:** Idea central desarrollada (lote V7-01); ID curricular, no ESS.

**Definición / idea central.** El escalamiento de privilegios es la táctica que convierte un acceso inicial en control del entorno; con agentes e identidades no humanas, el abuso de permisos de conectores y tokens es su versión más nueva y menos vigilada.

**Origen.** V7 (V7-C06, cierra INC-04)

**Tesis y sentido para el rol.** El escalamiento de privilegios es la táctica que convierte un acceso inicial en control del entorno: de un buzón comprometido a una cuenta administrativa, de un token de aplicación a permisos de directorio. Con agentes e identidades no humanas, el escalamiento adquiere formas nuevas: abuso de permisos de conectores, tokens de agentes con alcance excesivo, servidores MCP que exponen herramientas privilegiadas. La tesis es que el programa debe enseñar el escalamiento como táctica (ATT&CK TA0004, ASI03) y no solo como principio de IAM, porque la defensa se diseña contra el camino del adversario.

**Tensión y límites.** La tensión es que el escalamiento se previene desde IAM (M2.2) pero se detecta desde el SOC (M4.1); si nadie lo trata como táctica, cae entre dos unidades. Otra tensión es la de los agentes: sus permisos se otorgan para que sean útiles y cada permiso es un peldaño potencial.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: MITRE ATT&CK TA0004 y técnicas asociadas, OWASP ASI03 y NHI Top 10, D3FEND Harden. Implementación: mapa de caminos de escalamiento en el tenant (buzón → cuenta → rol; agente → conector → Graph), detecciones en Sentinel/Defender for Identity, revisión de permisos de agentes (M2.2-PA01), honeytokens de credenciales (M4.1-K11).

**Evidencia y evaluación.** Evidencia: mapa de caminos de escalamiento con detecciones y mitigaciones por camino. Se evalúa la inclusión de caminos agénticos.

**Puentes.** Extiende M4.2-K02 (modelado de amenazas) y M2.2-K04 (PAM); se relaciona con AMP-33, AMP-34, HC-009 y M2.2-PA01. Nuevo en V7 (cierra INC-04).

**Recomendaciones de práctica y ejercitación.**
1. Mapear tres caminos de escalamiento humanos y tres agénticos en el tenant.
2. Escribir una detección por camino y probarla.
3. Revisar permisos de conectores de los agentes como peldaños potenciales.

**Próximos pasos.**
- Incorporar al modelo de amenazas de la flota (M4.2-PA02).
- Alimentar la matriz de permisos (M2.2-PA01).
- Revisar al agregar herramientas.

**Relación con los conceptos de la(s) unidad(es) M4.2.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M4.2-K01 | K | Gestión Vulnerabilidades | misma unidad |
| M4.2-K02 | K | Modelado de Amenazas | misma unidad |
| M4.2-K03 | K | Amenaza Interna | misma unidad |
| M4.2-K04 | K | RaaS (Ransomware) | misma unidad |
| M4.2-K05 | K | Priorización por Riesgo | misma unidad |
| M4.2-K06 | K | Superficie de Ataque | misma unidad |
| M4.2-K07 | K | Riesgos Emergentes | misma unidad |
| M4.2-K08 | K | Economía del Cibercrimen | misma unidad |
| M4.2-K09 | K | STRIDE | misma unidad |
| M4.2-K10 | K | IoC (Indicadores) | misma unidad |
| AMP-41 | AMP | Prompt injection | misma unidad |
| AMP-42 | AMP | Envenenamiento de datos y modelos | misma unidad |
| HC-016 | HC | Superficie de ataque contextualizada | misma unidad |
| HC-026 | HC | Ética, cultura y controles internos | misma unidad |
| HC-031 | HC | Seguridad del software y confianza en componentes | misma unidad |
| HC-032 | HC | Evaluación adversarial de sistemas autónomos | misma unidad |
| M4.2-PA01 | PA | Amenazas del dominio Zero Trust (instancias: correo y colaboración · cross-domain · endpoints · identidades · datos) | misma unidad |
| M4.2-PA02 | PA | Catálogos de amenazas a sistemas agénticos aplicados a la flota | misma unidad |

**Pregunta generadora:** Desde el agente menos privilegiado de su flota, ¿cuántos pasos lo separan de un permiso de administrador, y quién detectaría cada paso?

---

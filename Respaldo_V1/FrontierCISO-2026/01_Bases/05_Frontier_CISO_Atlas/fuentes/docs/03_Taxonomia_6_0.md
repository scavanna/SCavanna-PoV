> **Registro de la versión 1.3 (16 de noviembre de 2026).** Este documento se conserva tal como se publicó. Las cifras, los estados y los archivos que cita corresponden a esa versión. El estado vigente está en `docs/15_Decisiones_delegadas_y_relectura_1_4.md` y en los documentos 16 a 19.

# Taxonomía 6.0 del Frontier CISO Atlas

**Frontier CISO Atlas 1.3** · Taxonomía 6.0 (reglas de asignación, revisión 2) · Ontología 2.1.0 · GM-24 V7.1 · 16 de noviembre de 2026 · Estado: decisiones de diseño confirmadas por el autor; reglas adoptadas según la lectura del curador y corpus releído a ciegas por lectores automáticos, con una lectura para todos y dos donde la primera difería; contenido candidato, sin validación humana

## 1. Resultado de la revisión

La pregunta era si tenía sentido ampliar territorios, dominios o funciones al contemplar más organismos y más artefactos. La respuesta, con su justificación:

| Eje | 5.3 | 6.0 | Qué cambió |
|---|---|---|---|
| Territorios (X) | 8 | 8 | Sin cambio de cantidad; cinco alcances explicitados |
| Dominios (Y) | 24 | 28 | Cuatro nuevos (D25–D28), seis ajustes de alcance, una aclaración (D20) y siete notas de alcance en dominios vigentes |
| Funciones (Z) | 6 | 6 | Sin cambio: son las de NIST CSF 2.0 |
| Subfunciones (Z) | 32 | 34 | Dos nuevas (PR06 y RC05) |
| Horizontes (H) | 4 | 4 | Sin cambio |
| Catalizadores (H) | 10 | 11 | Uno nuevo (CAT11) |
| Inhibidores (H) | 10 | 11 | Uno nuevo (INH11) |
| Mecanismos homeostáticos (H) | 10 | 12 | Dos nuevos (HOM11 y HOM12) |
| Factores de contexto (H) | 7 | 8 | Uno nuevo (HX08) |
| Variables homeostáticas (H) | 0 | 6 | Concepto nuevo (HV01–HV06) |

Regla general de la revisión: **se amplía lo que se justifica con evidencia externa y con el corpus**, y lo que no se admite queda escrito con el criterio que no cumple. Tres casos se apartan de esa regla y están declarados: D27 se admite por completitud, D26 por materialidad y en el eje H las seis variables homeostáticas son una propuesta de diseño sin respaldo externo, y tres de los elementos nuevos (INH11, HOM11 y HOM12) se justifican con marcos del propio autor. Ningún código se renumera ni se reutiliza.

**Estado en la versión 1.3.** El autor aceptó la Taxonomía 6.0 el 15 de noviembre de 2026 y lo confirmó el 16. Ese día aceptó también las reglas que proponía la revisión crítica: los 60 enunciados que tenían texto listo quedaron adoptados y son las reglas de asignación, revisión 2 (sección 8.1). Ningún código ni ninguna cardinalidad cambió. Cambiaron la definición de D03 y las reglas, y las 34 subfunciones tienen ahora una definición de trabajo (sección 5.1). Siguen abiertas 11 preguntas (sección 8.2).

## 2. El modelo

- **X.** Territorio: la perspectiva o responsabilidad desde la que se mira.
- **Y.** Dominio: la disciplina o el objeto.
- **Z.** Función de NIST CSF 2.0 y subfunción editorial del Atlas: lo que se busca lograr.
- **H.** Horizonte, fuerzas, contexto y variables homeostáticas: cómo cambia y qué lo mantiene estable.
- **Lentes.** Vistas que no son ejes: pilar MCCS, plano (A académico, B capacidades contratadas) y pilar de la agenda de IA.

## 3. Territorios (eje X): se mantienen 8

**Decisión.** Se mantienen 8. No se agrega, fusiona ni renombra ninguno.

**Justificación.**

- Los 80 elementos de primer nivel de 12 marcos del rol (CISM, CRISC, AAISM, CISSP, NACD–ISA, ECSF, NICE, disciplinas del SAF, ejes del GM-24, dominios de competencia del PO-GAC, pilares MCCS y capas del CISO-OS) encuentran territorio: no quedó ninguno huérfano.
- La frontera no es un territorio: es el borde H de todos los territorios. Crear un territorio para la tecnología de frontera repetiría el error que el cambio de nombre corrige (atar el Atlas a una tecnología).
- T07 no se renombra ni se amplía: sigue siendo la perspectiva de la autoridad no humana. Otras tecnologías de frontera (poscuántica, soberanía) se expresan con H, con D26 y con CAT11.
- T01 solo tiene respaldo de primer nivel en MCCS y CISO-OS. Es el territorio propio del Atlas, no una carencia: ningún marco del rol trata el juicio individual como objeto.

| Código | Territorio | Alcance | Precisión en 6.0 | Pre-ensayos |
|---|---|---|---|---|
| T01 | SELF & JUDGMENT | Criterio individual, metacognición, sesgos y decisiones. | Explicita el sistema operativo personal del líder (energía, atención, carga cognitiva) y la higiene de decisión. Ancla de MCCS-MM y de MCCS-OS a escala individual. | 5 (0,7 %) |
| T02 | LEADERSHIP & ORGANIZATION | Personas, incentivos, roles, cultura, liderazgo y accountability. | Incluye la fuerza de trabajo híbrida (personas, agentes y proveedores), la distribución de autoridad y la gestión de agentes como equipo. | 90 (12,2 %) |
| T03 | STRATEGY & BUSINESS | Outcomes, estrategia, inversión y priorización empresarial. | Incluye el sistema operativo de la oficina del CISO, el producto-control como unidad de valor y la economía de la automatización (costo por tarea, capacidad liberada). | 80 (10,8 %) |
| T04 | RISK & RESILIENCE | Exposición, escenarios, apetito, continuidad y riesgo de transición. | Incluye riesgo sistémico y de concentración, y el riesgo de las transiciones tecnológicas (IA, agentes, criptografía poscuántica). | 139 (18,8 %) |
| T05 | SECURITY ARCHITECTURE | Diseño de controles, Zero Trust, ingeniería y fronteras técnicas. | Sin cambio de significado. Su disciplina transversal ahora tiene dominio propio (D25). | 88 (11,9 %) |
| T06 | SECURITY OPERATIONS | SOC, monitoreo, investigación, respuesta y operación. | Incluye la operación por cadencias de productos-control y el SOC agéntico (humanos y agentes en la misma cola). | 84 (11,4 %) |
| T07 | AI & AUTONOMOUS SYSTEMS | Modelos, agentes, autonomía, herramientas y autoridad no humana. | Sin cambio de significado. No se asigna por mera mención de IA. No absorbe otras tecnologías de frontera: esas se expresan con H. | 102 (13,8 %) |
| T08 | TRUST & ASSURANCE | Evidencia, auditoría, legitimidad, confiabilidad y transparencia. | Sin cambio de significado. Su disciplina transversal ahora tiene dominio propio (D28). | 151 (20,4 %) |

**Candidatos descartados.**

- **Territorio de tecnologías de frontera.** Es una condición evolutiva (H), no una perspectiva de responsabilidad.
- **Territorio de ecosistema y terceros.** Es un objeto: D17, mirado desde T04 o T03.
- **Territorio de datos y privacidad.** Es un objeto: D06 y D07.
- **Territorio de directorio y partes interesadas.** Se reparte entre T02 (autoridad y rendición de cuentas) y T08 (confianza y evidencia).

**Cruce con marcos del rol.** Cada elemento de primer nivel de los marcos que describen el rol se proyectó sobre un territorio primario; los pilares OS y DO del MCCS, sobre dos, como dicen las anclas de la lente. La tabla cuenta, por territorio, cuántos elementos lo tienen como primario, de cuántos marcos provienen y cuántos son de marcos externos o de marcos del propio autor (los ejes del GM-24, los dominios de competencia del PO-GAC, los pilares del MCCS y las capas del CISO-OS). El detalle está en `data/cruce_elementos_territorios.csv`.

**Cómo leer este cruce.** Es una comprobación de cobertura, no una prueba de validez: con categorías amplias y elementos que pueden proyectarse sobre varios territorios, ningún elemento puede quedar sin lugar. 29 de los 80 elementos son de marcos propios y 35 llevan más de un territorio. Como esos dos pilares cuentan en dos territorios, las columnas de la tabla suman 82 elementos y 31 de marcos propios, y no 80 y 29. T01 no tiene respaldo externo de primer nivel. El cruce no incluye a SFIA ni a CyBOK, que están en la base de referencia: la afirmación de que ningún marco del rol trata el juicio individual como objeto no está comprobada contra todos ellos. Una prueba que pueda fallar es el encargo RP-16.7, aceptado y en cola.

| Territorio | Elementos con ese territorio primario | Marcos de los que provienen | De marcos externos | De marcos propios |
|---|---|---|---|---|
| T01 | 3 | 2 | 0 | 3 |
| T02 | 6 | 5 | 2 | 4 |
| T03 | 12 | 9 | 6 | 6 |
| T04 | 12 | 7 | 8 | 4 |
| T05 | 19 | 7 | 16 | 3 |
| T06 | 15 | 8 | 10 | 5 |
| T07 | 7 | 4 | 3 | 4 |
| T08 | 8 | 4 | 6 | 2 |

## 4. Dominios (eje Y): de 24 a 28

**Decisión.** Pasan de 24 a 28. Se admiten D25, D26, D27 y D28; se ajusta el alcance de D03, D06, D09, D13, D17 y D24; se aclara D20. Ningún código se renumera ni se reutiliza.

### 4.1 Criterios de admisión

Un dominio nuevo se admite si cumple los cinco criterios; si no cumple alguno, la excepción se declara.

| Código | Criterio | Prueba |
|---|---|---|
| C1 | Respaldo externo | Al menos 5 artefactos de al menos 3 organismos lo tratan como elemento de primer nivel o le dedican un artefacto completo. |
| C2 | No representable | No puede expresarse como combinación de categorías existentes (X × Y × Z) sin perder el objeto. |
| C3 | Presión del corpus o materialidad emergente | Al menos 10 pre-ensayos alojados a la fuerza en otros dominios, o una obligación o un plazo externo verificable. |
| C4 | Permanencia | Disciplina estable, presente en ediciones sucesivas de los artefactos; no es un producto ni una moda. |
| C5 | Frontera clara | La regla de precedencia frente a cada dominio vecino se escribe en una oración. |

**Diferencias con el plan de trabajo.** Los criterios que se aplicaron no son idénticos a los que fijó el plan antes de ejecutar: C1 sumó la vía del artefacto dedicado, C2 pasó de «un dominio o una combinación de territorio y dominio» a «X × Y × Z», C3 recibió el umbral de 10 pre-ensayos y C5 pasó de «una regla» a «cada dominio vecino». La ampliación de C2 al eje Z es el argumento con que se rechaza al candidato W02. La revisión crítica observó además que C2 se aplicó con más exigencia a W02 que a D28, que C4 se evaluó sin evidencia escrita y que la evidencia de C3 es circular: cuenta pre-ensayos que los clasificadores movieron cuando ya conocían la definición del dominio nuevo, y por eso es provisional hasta que un curador revise la categorización. Reescribir los criterios es el encargo RP-16, aceptado y en cola.

### 4.2 Dominios admitidos

#### D25 Enterprise Security Architecture & Zero Trust — Admitido

Arquitectura empresarial de seguridad, principios y modelos de referencia, estrategia Zero Trust, seguro por diseño y por defecto, e ingeniería de resiliencia.

| Criterio | Evaluación |
|---|---|
| C1 | Sí: 8 artefactos de 6 organismos lo tratan como elemento de primer nivel; 7 artefactos completos dedicados. |
| C2 | Sí: T05 es una perspectiva; faltaba el objeto «arquitectura». |
| C3 | Sí: 15 pre-ensayos migran desde 6 dominios (D05: 5, D10: 4, D04: 2, D20: 2, D02: 1, D16: 1); el dominio queda con 18. |
| C4 | Sí. |
| C5 | Sí: el principio transversal es D25; el control de un pilar concreto queda en el dominio del pilar. |

Elementos de primer nivel que lo respaldan: NIST CSF 2.0: PR.IR Technology Infrastructure Resilience; ISC2 CISSP: CISSP-3 Security Architecture and Engineering; C2M2: ARCHITECTURE Cybersecurity Architecture; NCSC CAF: B5 Resilient Networks and Systems; OWASP Top 10: A06:2025 Insecure Design; Microsoft SAF: SAF-ARQ Security Architecture; Microsoft SDL: SDL 3 Perform security design review and threat modeling; NIST NICE (áreas de competencia): NF-COM-RE Cyber Resiliency.

Artefactos dedicados: NIST SP 800-207 (`NIST-SP-800-207`); NIST SP 800-160 Vol. 2 Rev. 1 (`NIST-SP-800-160V2`); CISA Zero Trust Maturity Model 2.0 (`CISA-ZTMM`); DoD Zero Trust Strategy (`DOD-ZT`); TOGAF Standard, 10th Edition (`TOG-TOGAF`); SABSA (`SABSA`); Microsoft Cybersecurity Reference Architectures (jun-2026) (`MS-MCRA`).

#### D26 Cryptography, Key Management & Post-Quantum Readiness — Admitido por materialidad

Inventario criptográfico, PKI y certificados, gestión de claves y secretos, agilidad criptográfica y transición poscuántica.

| Criterio | Evaluación |
|---|---|
| C1 | Sí: 6 artefactos de 6 organismos lo tratan como elemento de primer nivel; 2 artefactos completos dedicados. |
| C2 | Sí: la disciplina criptográfica no es un control de datos. |
| C3 | Parcial: 5 pre-ensayos migran desde 2 dominios (D06: 4, D05: 1); el dominio queda con 5. No alcanza el umbral de 10; se admite por materialidad emergente: NIST IR 8547 final (27-oct-2026) fija los hitos «deprecated after 2030» y «disallowed after 2035» para los algoritmos de clave pública vulnerables a la computación cuántica (firmas ECDSA, EdDSA y RSA; establecimiento de claves con Diffie-Hellman, MQV y RSA). El calendario obliga a los sistemas federales de Estados Unidos y es una referencia para los demás; la verificación no contrastó a qué niveles de seguridad alcanza cada hito. |
| C4 | Sí. |
| C5 | Sí: el cifrado como control sobre los datos queda en D06. |

Elementos de primer nivel que lo respaldan: CSA CCM v4.1: CEK Cryptography, Encryption & Key Management; CyBOK: Cryptography; CyBOK: Applied Cryptography; OWASP Top 10: A04:2025 Cryptographic Failures; Microsoft SDL: SDL 4 Define and use cryptography standards; NIS2 art. 21(2): 21(2)(h) Policies and procedures regarding the use of cryptography and, where appropriate, encryption; NIS2 Reglamento de Ejecución (UE) 2024/2690 (anexo): Anexo 9 Cryptography; NIST NICE (áreas de competencia): NF-COM-CR Cryptography.

Artefactos dedicados: NIST FIPS 203, 204 y 205 (`NIST-FIPS-PQC`); NIST IR 8547 (final, 27-oct-2026) (`NIST-IR-8547`).

No cuentan como dedicados: NIST SP 800-227 (no está registrado como artefacto en la base de referencia).

#### D27 Physical, Environmental & Facility Security — Admitido con reserva (espacio en blanco)

Seguridad física de instalaciones y centros de datos, protección ambiental, mantenimiento y soportes, y su evidencia como dependencia del control (incluida la del proveedor de nube).

| Criterio | Evaluación |
|---|---|
| C1 | Sí: 7 artefactos de 7 organismos lo tratan como elemento de primer nivel. |
| C2 | Sí: la seguridad física no tenía dominio; D08 es red e infraestructura lógica. |
| C3 | No por corpus: un solo pre-ensayo (M3.1-K12, nuevo en el GM-24 V7.1). Se admite como dominio de espacio en blanco: la completitud es el propósito declarado del cambio de nombre. |
| C4 | Sí. |
| C5 | Sí: instalaciones, ambiente, mantenimiento y soportes; la continuidad queda en D16 y la planta industrial en D18. |

Elementos de primer nivel que lo respaldan: NIST SP 800-53: MA Maintenance; NIST SP 800-53: MP Media Protection; NIST SP 800-53: PE Physical and Environmental Protection; CSA CCM v4.1: DCS Datacenter Security; ISO/IEC 27002: OC05 Physical security; PCI DSS: PCI 9 Restrict physical access to cardholder data; Swift CSCF: CSCF 3 Physically Secure the Environment; NIS2 Reglamento de Ejecución (UE) 2024/2690 (anexo): Anexo 13 Environmental and physical security; DoD CMMC: MA Maintenance; DoD CMMC: MP Media Protection; DoD CMMC: PE Physical Protection.

#### D28 Security Assurance, Testing & Measurement — Admitido

Evaluación de controles, pruebas técnicas (pruebas de penetración, equipos rojo y púrpura, validación continua), auditoría y atestaciones, métricas, indicadores y evidencia de eficacia.

| Criterio | Evaluación |
|---|---|
| C1 | Sí: 12 artefactos de 10 organismos lo tratan como elemento de primer nivel; 1 artefacto completo dedicado. |
| C2 | Sí: T08 es una perspectiva y GV08 una función; faltaba el objeto «aseguramiento, pruebas y medición». |
| C3 | Sí: 53 pre-ensayos migran desde 13 dominios (D03: 17, D20: 9, D13: 5, D01: 4, D04: 4, D02: 3, D05: 3, D14: 3, D06: 1, D15: 1, D17: 1, D22: 1, D23: 1); el dominio queda con 57. |
| C4 | Sí. |
| C5 | Sí: la obligación y su conformidad son D03; el método para demostrar eficacia es D28; la IA como instrumento de prueba es D22. |

Elementos de primer nivel que lo respaldan: NIST CSF 2.0: ID.IM Improvement; NIST SP 800-53: CA Assessment, Authorization, and Monitoring; CIS Controls v8.1: CIS 18 Penetration Testing; CSA CCM v4.1: A&A Audit & Assurance; ISO/IEC 27002: OC15 Information security assurance; ISC2 CISSP: CISSP-6 Security Assessment and Testing; PCI DSS: PCI 11 Test security of systems and networks regularly; COBIT 2019: MEA Monitor, Evaluate and Assess; Microsoft SDL: SDL 7 Perform security testing; NIS2 art. 21(2): 21(2)(f) Policies and procedures to assess the effectiveness of cybersecurity risk-management measures; DORA: DORA-3 Digital operational resilience testing; NIS2 Reglamento de Ejecución (UE) 2024/2690 (anexo): Anexo 7 Policies and procedures to assess the effectiveness of cybersecurity risk-management measures; DoD CMMC: CA Security Assessment.

Artefactos dedicados: NIST SP 800-55 Vol. 1 y Vol. 2 (dic-2024) (`NIST-SP-800-55`).

No cuentan como dedicados: DORA, capítulo IV (pruebas de resiliencia) (es una parte de un artefacto de la base, no un artefacto completo).

### 4.3 Dominios con alcance ajustado

| Dominio | Ajuste |
|---|---|
| D03 Compliance & Regulatory Security | AJUSTE: se delimita a las obligaciones (legales, regulatorias, contractuales) y su conformidad. La evidencia de eficacia, las pruebas y la medición pasan a D28. |
| D06 Data Security & Information Protection | AJUSTE: el cifrado como control sobre los datos permanece; la disciplina criptográfica (claves, PKI, agilidad, transición poscuántica) pasa a D26. |
| D09 Endpoint & Workplace Security | AJUSTE: el puesto de trabajo incluye de forma explícita el correo, la colaboración y la navegación. |
| D13 Vulnerability & Exposure Management | AJUSTE: explicita el inventario de activos, la configuración segura y la postura como insumos de la exposición. |
| D17 Third-Party & Supply Chain Security | AJUSTE: explicita la cadena de suministro de software y de IA (componentes, modelos, conectores) y el riesgo de concentración. |
| D24 Security Workforce & Human Factors | AJUSTE: explicita la fuerza de trabajo híbrida (personas y agentes), las competencias y el riesgo humano. |
| D20 AI & Agent Security | Nota de alcance: cede a D01, D02 y D03 el gobierno, el riesgo y el cumplimiento de la IA (regla 7); incluye los protocolos y pasarelas de agentes (MCP, A2A) y la memoria de agentes como superficie. |

Además, siete dominios que figuran como vigentes llevan una nota de alcance 6.0 en el catálogo: D01, D02, D04, D05, D12, D14 y D22. Las de D01 y D02 son el cambio de alcance que aplica la regla 7. Hasta la versión 1.2, los ajustes de D09, D13, D17 y D24 no se habían aplicado al corpus con una lectura dedicada. La relectura de la versión 1.3 leyó todo el corpus con las reglas adoptadas (encargo RP-18.1).

### 4.4 Lista de vigilancia: candidatos no admitidos

| Código | Candidato | Criterio que no cumple | Motivo y destino |
|---|---|---|---|
| W01 | Gobierno, riesgo y cumplimiento de la IA como dominio propio | C2 | Se expresa como T07 × D01, D02 o D03. La AI Controls Matrix de CSA agrega un solo dominio (Model Security) a los 17 de la CCM; ISO/IEC 42001 es un sistema de gestión. |
| W02 | Gestión de activos, configuración y cambios | C2 | Tiene respaldo externo amplio (ID.AM, CIS 1, 2 y 4, C2M2 ASSET, CCM CCC), pero en el Atlas es una función (ID01, PR04) que cruza dominios: en el corpus, los 16 títulos que nombran el inventario o los activos se reparten por tipo de activo (D20: 5, D13: 3, D26: 2, D01: 1, D02: 1, D03: 1, D11: 1, D16: 1, D28: 1). El alcance de D13 lo explicita como insumo de la exposición. La revisión crítica 1.2 observó que este criterio se aplicó aquí con más exigencia que en D28; la reevaluación queda en la decisión D-11. |
| W03 | Seguridad del correo y la colaboración | C1 | Solo CIS 9 lo trata en primer nivel. Se explicita en el alcance de D09. |
| W04 | Fraude y confianza digital | C1 | Ningún artefacto de la base lo trata en primer nivel, aunque hay indicios de materialidad (WEF 2026: 73 % de los encuestados dijo haber sido afectado, él o alguien de su red, por fraude cibernético en 2025; es una experiencia declarada, no una proporción de organizaciones). Queda en vigilancia. |
| W05 | Protocolos e interoperabilidad de agentes (MCP, A2A) | C4 | Especificaciones de 2026 todavía en movimiento. Se aclara en el alcance de D20. |
| W06 | Soberanía digital y geopolítica | C2 | No es una disciplina sino una fuerza: se incorpora como CAT11 y se lee con HX02. |
| W07 | Resiliencia operativa como dominio | C2 | Se expresa como T04 × D16, D17 y D28 (DORA, principios de Basilea). |
| W08 | Identidades no humanas y de agentes como dominio | C2 | Es D05 con alcance explícito. |
| W09 | Consolidar D21, D22 y D23 (IA para la seguridad) | C1 por separado | Los artefactos externos tratan la IA para la defensa como un bloque (área Defend del Cyber AI Profile de NIST, todavía borrador). En 6.0 no se consolidan: los códigos son estables y 19 pre-ensayos los usan. Revisar en 6.1. |

### 4.5 La decisión sobre D20, aplicada

La regla «gobierno, riesgo y cumplimiento de la IA van en D01, D02 o D03 con territorio T07» queda explícita en 6.0. La decisión D-03 estaba planteada como pregunta; la versión 1.2 leyó la aceptación en bloque del autor (15-nov-2026) como un «sí» y la aplicó; el autor lo confirmó el 16-nov-2026 (D-14.2). Salieron de D20 los pre-ensayos en que las dos lecturas deciden el mismo destino, aquellos en que la primera lo dejaba a criterio del curador y la segunda propone el destino, y los adjudicados por escrito; los casos sin coincidencia quedaron en D20, registrados. La relectura de la versión 1.3 volvió a leer el dominio (documento 14, sección 4.7). El detalle de la versión 1.2 está en el anexo del documento 07 y en `data/analisis_D20_decision_D03.csv`.

El autor confirmó esta decisión el 16 de noviembre de 2026 (D-14.2). Después de la relectura de la versión 1.3, D20 tiene 43 pre-ensayos (documento 14, sección 4.7). Resultado en la versión 1.2: de los 71 pre-ensayos que estaban en D20, 26 salieron (16 a D01, 6 a D02, 2 a D17, 1 a D28 y 1 a D14) y 45 quedaron. De los que salieron, en 13 las dos lecturas deciden el mismo destino, en 9 la primera lo dejaba a criterio del curador y la segunda propone el destino, y 4 se adjudicaron por escrito; 22 fueron a los dominios que nombra la regla 7 y 4 a otros (AMP-49 a D17, HC-012 a D28, APC-122 a D17 y APC-164 a D14), por reglas de alcance distintas. El territorio no se cambió: la regla nombra T07, pero ningún pre-ensayo se llevó a T07 por esta vía.

### 4.6 Catálogo completo y evidencia

Columnas de evidencia: **primer nivel** = artefactos y organismos que tratan el dominio como elemento de primer nivel, sobre 29 artefactos de la base de referencia cruzados en 30 conjuntos de elementos (327 elementos; la Directiva NIS2 y su Reglamento de Ejecución son un solo artefacto); **dedicados** = artefactos completos de la base dedicados al dominio que no figuran ya en su primer nivel; **corpus** = pre-ensayos con ese dominio primario antes y después de la migración. La columna «Corpus 6.0» trae el dominio primario vigente en la versión 1.3, después de la relectura con las reglas adoptadas.

| Código | Dominio | Familia | Estado | Primer nivel (artefactos / organismos) | Dedicados | Corpus 5.3 | Corpus 6.0 |
|---|---|---|---|---|---|---|---|
| D01 | Cybersecurity Governance | Gobierno | vigente | 12 / 11 | 2 | 74 | 126 |
| D02 | Cyber Risk Management | Gobierno | vigente | 11 / 8 | 6 | 80 | 94 |
| D03 | Compliance & Regulatory Security | Gobierno | ajustado | 3 / 3 | 4 | 55 | 42 |
| D04 | Security Program & Investment Management | Gobierno | vigente | 4 / 4 | 0 | 63 | 52 |
| D05 | Identity & Access Security | Protección | vigente | 21 / 16 | 2 | 36 | 30 |
| D06 | Data Security & Information Protection | Protección | ajustado | 14 / 11 | 0 | 35 | 20 |
| D07 | Privacy & Data Protection Engineering | Protección | vigente | 2 / 2 | 2 | 16 | 7 |
| D08 | Network & Infrastructure Security | Protección | vigente | 15 / 11 | 0 | 2 | 3 |
| D09 | Endpoint & Workplace Security | Protección | ajustado | 8 / 7 | 0 | 10 | 8 |
| D10 | Cloud & Platform Security | Protección | vigente | 5 / 4 | 1 | 11 | 4 |
| D11 | Application & Software Security | Protección | vigente | 17 / 13 | 4 | 9 | 7 |
| D12 | Threat Intelligence & Threat Modeling | Operaciones | vigente | 3 / 3 | 5 | 22 | 24 |
| D13 | Vulnerability & Exposure Management | Operaciones | ajustado | 16 / 13 | 3 | 18 | 16 |
| D14 | Security Monitoring & Detection | Operaciones | vigente | 21 / 16 | 0 | 21 | 23 |
| D15 | Incident Response & Crisis Management | Operaciones | vigente | 13 / 11 | 4 | 36 | 42 |
| D16 | Business Continuity & Cyber Recovery | Operaciones | vigente | 9 / 8 | 1 | 24 | 23 |
| D17 | Third-Party & Supply Chain Security | Ecosistemas | ajustado | 14 / 10 | 3 | 29 | 28 |
| D18 | Operational Technology & Industrial Control Security | Ecosistemas | vigente | 3 / 3 | 2 | 4 | 4 |
| D19 | IoT & Cyber-Physical Systems Security | Ecosistemas | vigente | 1 / 1 | 3 | 0 | 0 |
| D20 | AI & Agent Security | Ecosistemas | vigente | 6 / 4 | 8 | 76 | 43 |
| D21 | AI for Cyber Defense & Security Operations | Ecosistemas | vigente | 1 / 1 | 0 | 15 | 11 |
| D22 | AI for Security Assessment & Testing | Ecosistemas | vigente | 0 / 0 | 0 | 4 | 3 |
| D23 | AI for Security Engineering & Automation | Ecosistemas | vigente | 2 / 2 | 0 | 7 | 5 |
| D24 | Security Workforce & Human Factors | Personas | ajustado | 11 / 10 | 4 | 44 | 43 |
| D25 | Enterprise Security Architecture & Zero Trust | Protección | nuevo | 8 / 6 | 7 | — | 18 |
| D26 | Cryptography, Key Management & Post-Quantum Readiness | Protección | nuevo | 6 / 6 | 2 | — | 5 |
| D27 | Physical, Environmental & Facility Security | Protección | nuevo | 7 / 7 | 0 | — | 1 |
| D28 | Security Assurance, Testing & Measurement | Gobierno | nuevo | 12 / 10 | 1 | — | 57 |

**Hallazgos.**

- Dominios sin pre-ensayos: D19. Con menos de cinco: D08 (3), D10 (4), D18 (4), D22 (3), D27 (1). Son espacios en blanco del corpus, no de la taxonomía.
- D21, D22 y D23 son una descomposición propia del Atlas; su respaldo externo de primer nivel es débil.

### 4.7 La prueba de respaldo externo y de corpus, aplicada a los 28 dominios

La versión 1.1 aplicó los criterios solo a los dominios nuevos y a los candidatos. La tabla aplica C1 (al menos 5 artefactos de al menos 3 organismos, por primer nivel o sumando los dedicados) y la vía de corpus de C3 (al menos 10 pre-ensayos) a todos. Se listan los que no alcanzan alguna de las dos; el detalle completo está en `data/prueba_C1_C3_dominios.csv`.

| Dominio | Estado | Primer nivel (artefactos / organismos) | Dedicados | C1 por primer nivel | C1 con dedicados | Corpus 6.0 | C3 por corpus |
|---|---|---|---|---|---|---|---|
| D04 Security Program & Investment Management | vigente | 4 / 4 | 0 | no | no | 52 | sí |
| D07 Privacy & Data Protection Engineering | vigente | 2 / 2 | 2 | no | no | 7 | no |
| D08 Network & Infrastructure Security | vigente | 15 / 11 | 0 | sí | sí | 3 | no |
| D09 Endpoint & Workplace Security | ajustado | 8 / 7 | 0 | sí | sí | 8 | no |
| D10 Cloud & Platform Security | vigente | 5 / 4 | 1 | sí | sí | 4 | no |
| D11 Application & Software Security | vigente | 17 / 13 | 4 | sí | sí | 7 | no |
| D18 Operational Technology & Industrial Control Security | vigente | 3 / 3 | 2 | no | sí | 4 | no |
| D19 IoT & Cyber-Physical Systems Security | vigente | 1 / 1 | 3 | no | no | 0 | no |
| D21 AI for Cyber Defense & Security Operations | vigente | 1 / 1 | 0 | no | no | 11 | sí |
| D22 AI for Security Assessment & Testing | vigente | 0 / 0 | 0 | no | no | 3 | no |
| D23 AI for Security Engineering & Automation | vigente | 2 / 2 | 0 | no | no | 5 | no |
| D26 Cryptography, Key Management & Post-Quantum Readiness | nuevo | 6 / 6 | 2 | sí | sí | 5 | no |
| D27 Physical, Environmental & Facility Security | nuevo | 7 / 7 | 0 | sí | sí | 1 | no |

Advertencias sobre el conteo de C1:

- La independencia entre artefactos no está establecida: DoD CMMC y NIST SP 800-53 comparten familias, y cuatro de los 29 artefactos cruzados son de un mismo proveedor.
- Para ISO/IEC 27002 se tomaron como elementos de primer nivel los 15 valores del atributo «capacidades operativas», no los cuatro temas de la norma.
- Los pilares de automatización y orquestación de los modelos de Zero Trust son el único respaldo de primer nivel de D23 y no son específicos de la IA.

## 5. Funciones y subfunciones (eje Z): 6 funciones, 34 subfunciones

**Decisión sobre funciones.** Se mantienen 6: las funciones oficiales de NIST CSF 2.0.

- El Core de CSF 2.0 no cambió (6 funciones, 22 categorías) y los artefactos nuevos se alinean a él: SP 800-61 Rev. 3, CISA CPG 2.0, el borrador de SP 800-82 Rev. 4 y el Cyber AI Profile.
- Los 54 elementos de 11 modelos funcionales (AI RMF, D3FEND, CAF del NCSC, ISO/IEC 27035, FIRST, cláusulas de ISO/IEC 27001, SP 800-160, Privacy Framework, entre otros) se proyectan sobre las 6 sin residuo.
- Adaptar o evolucionar no es una séptima función: es el eje H.

**Cómo leer el cruce de funciones.** Es una comprobación de compatibilidad, no una prueba: 17 de los 54 elementos se proyectan sobre dos o más funciones, y tres de los once modelos cruzados (los conceptos de ciberseguridad de ISO/IEC 27002, CISA CPG 2.0 y NIST SP 800-61 Rev. 3) reproducen las funciones del propio CSF o son un perfil de él.

**Candidatos descartados.**

- **Función «Adaptar» o «Evolucionar».** Es el eje H (horizontes, fuerzas y homeostasis).
- **Función «Asegurar».** Es GV08 más ID05, y ahora el dominio D28.
- **Función «Anticipar» (SP 800-160).** Se reparte entre ID y PR.
- **GV11 Gobierno de la autonomía.** Es HOM12 más GV02 y GV03 vistos desde T07.

**Decisión sobre subfunciones.** Pasan de 32 a 34. Se agregan PR06 y RC05. Regla aplicada: Toda categoría oficial de CSF 2.0 debe tener al menos una subfunción editorial con el mismo prefijo de función.

| Categoría de CSF 2.0 | Antes | Ahora |
|---|---|---|
| PR.IR Technology Infrastructure Resilience | Solo aparecía compartida en PR03. | PR06 |
| RC.CO Incident Recovery Communication | Sin subfunción. | RC05 |

Efecto: El catálogo de indicadores K01–K64 cubre las 32 subfunciones anteriores. Con el catálogo CISO 365 2.0, RC05 tiene un indicador (K189) y PR06 no tiene ninguno: la revisión crítica 1.2 devolvió a PR03 los cuatro que la versión 1.1 había ubicado en PR06, porque miden segmentación y acceso de red.

| Código | Función | Subfunción | Categorías de CSF 2.0 | Estado | Pre-ensayos |
|---|---|---|---|---|---|
| GV01 | GV | Contexto empresarial y estrategia | GV.OC | vigente | 18 |
| GV02 | GV | Estructura de gobierno y autoridad | GV.RR | vigente | 43 |
| GV03 | GV | Políticas y estándares | GV.PO | vigente | 58 |
| GV04 | GV | Apetito, tolerancia y aceptación de riesgo | GV.RM | vigente | 47 |
| GV05 | GV | Gobierno de programas, recursos e inversión | GV.RR · GV.OV | vigente | 39 |
| GV06 | GV | Obligaciones legales y contractuales | GV.OC | vigente | 32 |
| GV07 | GV | Supervisión y reporting ejecutivo | GV.OV | vigente | 34 |
| GV08 | GV | Assurance y revisión independiente | GV.OV | vigente | 46 |
| GV09 | GV | Gobierno de terceros y ecosistemas | GV.SC | vigente | 27 |
| GV10 | GV | Ética, cultura y rendición de cuentas | GV.RR · GV.OC | vigente | 22 |
| ID01 | ID | Inventario y clasificación de activos | ID.AM | vigente | 17 |
| ID02 | ID | Dependencias y criticidad del negocio | ID.AM · GV.OC | vigente | 6 |
| ID03 | ID | Amenazas, vulnerabilidades y exposición | ID.RA | vigente | 33 |
| ID04 | ID | Análisis de escenarios y cuantificación de riesgos | ID.RA | vigente | 33 |
| ID05 | ID | Evaluación de capacidades y brechas | ID.IM | vigente | 26 |
| PR01 | PR | Identidad y autorización | PR.AA | vigente | 36 |
| PR02 | PR | Protección de datos y privacidad por diseño | PR.DS | vigente | 28 |
| PR03 | PR | Hardening y arquitectura segura | PR.PS · PR.IR | vigente | 45 |
| PR04 | PR | Desarrollo seguro y gestión de cambios | PR.PS | vigente | 18 |
| PR05 | PR | Preparación de personas y procedimientos | PR.AT | vigente | 21 |
| PR06 | PR | Resiliencia de la infraestructura y protección física y ambiental | PR.IR | nuevo | 3 |
| DE01 | DE | Telemetría y observabilidad | DE.CM | vigente | 5 |
| DE02 | DE | Ingeniería de detección y análisis | DE.AE | vigente | 16 |
| DE03 | DE | Hunting, validación y mejora de detecciones | DE.AE · DE.CM | vigente | 4 |
| DE04 | DE | Evaluación de cobertura y calidad de detección | DE.AE · ID.IM | vigente | 6 |
| RS01 | RS | Preparación y coordinación de respuesta | RS.MA | vigente | 22 |
| RS02 | RS | Contención, erradicación y preservación de evidencia | RS.MI · RS.AN | vigente | 13 |
| RS03 | RS | Comunicación de crisis y decisiones ejecutivas | RS.CO | vigente | 11 |
| RS04 | RS | Gestión de incidentes con terceros | RS.CO · GV.SC | vigente | 2 |
| RC01 | RC | Restauración y recuperación técnica | RC.RP | vigente | 7 |
| RC02 | RC | Continuidad y operación degradada | RC.RP | vigente | 6 |
| RC03 | RC | Validación de recuperación y retorno seguro | RC.RP | vigente | 5 |
| RC04 | RC | Aprendizaje, corrección y mejora continua | ID.IM | vigente | 10 |
| RC05 | RC | Comunicación de la recuperación y restitución de la confianza | RC.CO | nuevo | 0 |

Las subfunciones son editoriales del Atlas. No son categorías oficiales de NIST. Tienen nombre y categoría de CSF 2.0, y 13 de las 22 categorías de CSF están repartidas entre dos o más subfunciones. Desde la versión 1.3 cada una tiene una definición de trabajo (sección 5.1). Notas de la versión 1.2 sobre cuatro de ellas:

- **PR03.** Arquitectura segura, hardening y segmentación. Comparte la categoría PR.IR con PR06; la frontera propuesta está en la regla RP-12.
- **PR06.** El ancla PR.IR cubre la resiliencia de la infraestructura (PR.IR-03 y PR.IR-04) y la protección frente a amenazas ambientales (PR.IR-02). En NIST CSF 2.0, el acceso físico está en PR.AA-06, la vigilancia del entorno físico en DE.CM-02 y el mantenimiento del hardware en PR.PS-03: la protección física del nombre de PR06 no queda cubierta por su ancla.
- **RS01.** En NIST CSF 2.0, RS.MA-01 es la ejecución del plan de respuesta una vez declarado el incidente. La preparación (planes, roles y ejercicios) está en GV, ID.IM y PR. RS01 reúne preparación y coordinación por una decisión editorial heredada de la versión 5.3.
- **RC04.** Su única categoría de CSF 2.0 es ID.IM, que pertenece a la función Identificar. El Atlas cuenta como recuperación contenido de mejora continua; la opción de cambiarlo está en la regla RP-13.

### 5.1 Definiciones de trabajo de las subfunciones

Cada definición dice qué incluye la subfunción, qué excluye y, en 10 de las 34, qué frontera no decide ninguna regla adoptada. Las redactó el curador con el nombre, la categoría de CSF 2.0 y los enunciados adoptados de la regla RP-12 (encargo RP-12.1). El autor no las revisó, y se usaron en la relectura del corpus.

| Código | Subfunción | Incluye | Excluye | Frontera sin decidir | Fuente |
|---|---|---|---|---|---|
| GV01 | Contexto empresarial y estrategia | El contexto del negocio (misión, objetivos, partes interesadas) y la estrategia de seguridad que se deriva de él. | Las obligaciones legales y contractuales (GV06) y la criticidad y las dependencias del negocio (ID02). | — | nombre y GV.OC |
| GV02 | Estructura de gobierno y autoridad | La estructura de gobierno: roles, responsabilidades, autoridad y derechos de decisión; para los agentes, quién supervisa y con qué nivel de autonomía. | Las sesiones de órganos con acta y decisiones (GV07) y la gestión del programa y de sus recursos (GV05). | El liderazgo y el diseño de roles del equipo en D24, que hoy se reparte entre GV02, GV10 y PR05 (hallazgo C4d-014). | GV.RR; RP-12.8 y RP-12.10 |
| GV03 | Políticas y estándares | Las políticas, los estándares y las normas internas: su aprobación, comunicación y actualización; para los agentes, la política que fija los niveles de autonomía y el interruptor. | Las obligaciones externas (GV06). | El procedimiento, que también nombra PR05 (hallazgo C4d-010). | GV.PO; RP-12.10 |
| GV04 | Apetito, tolerancia y aceptación de riesgo | La estrategia de gestión del riesgo: apetito, tolerancia y aceptación. | La identificación de amenazas y exposición (ID03) y el análisis y la cuantificación del riesgo con el seguimiento de su tratamiento (ID04). | La elección de la respuesta al riesgo (mitigar, transferir, seleccionar controles), que ninguna subfunción nombra (hallazgo C4d-001). | GV.RM; RP-12.5 |
| GV05 | Gobierno de programas, recursos e inversión | El gobierno del programa de seguridad: portafolio, recursos, presupuesto e inversión, y las cadencias de gestión del programa. | Las sesiones de órganos con acta y decisiones (GV07). | — | GV.RR · GV.OV; RP-12.8 |
| GV06 | Obligaciones legales y contractuales | La identificación y la gestión de las obligaciones legales, regulatorias y contractuales. | El contexto del negocio y la estrategia (GV01) y las notificaciones obligatorias de un incidente (RS03). | — | GV.OC; RP-12.7 |
| GV07 | Supervisión y reporting ejecutivo | La supervisión por la dirección y por los órganos de gobierno: sesiones con acta y decisiones, informes ejecutivos y revisión del desempeño de la estrategia. | Las cadencias de gestión del programa (GV05) y la revisión independiente (GV08). | — | GV.OV; RP-12.8 |
| GV08 | Assurance y revisión independiente | El aseguramiento y la revisión independiente: auditoría interna y externa, atestaciones y evaluación por terceros. | El informe ejecutivo de gestión (GV07). | La prueba o la medición de eficacia que no es independiente ni de detección ni de recuperación: ID05 o GV08 (hallazgo C4d-012). | GV.OV |
| GV09 | Gobierno de terceros y ecosistemas | El gobierno de proveedores, terceros y ecosistemas: estrategia, requisitos, contratos y supervisión de la cadena de suministro. | La coordinación de un incidente con terceros (RS04). | — | GV.SC; RP-12.7 |
| GV10 | Ética, cultura y rendición de cuentas | La ética, la cultura de seguridad y la rendición de cuentas. | La estructura formal de roles y autoridad (GV02) y la formación de las personas (PR05). | El liderazgo y la calidad de la decisión individual en D24 (hallazgo C4d-014). | GV.RR · GV.OC |
| ID01 | Inventario y clasificación de activos | El inventario, la clasificación y la propiedad de los activos: equipos, software, datos, servicios, identidades y sistemas de IA. | La criticidad y las dependencias del negocio (ID02). | — | ID.AM |
| ID02 | Dependencias y criticidad del negocio | Las dependencias, la criticidad y el impacto en el negocio de los activos y los servicios. | El inventario (ID01) y el análisis de escenarios de riesgo (ID04). | — | ID.AM · GV.OC |
| ID03 | Amenazas, vulnerabilidades y exposición | La identificación de amenazas, vulnerabilidades y exposición técnica; el escenario de amenaza, con el adversario y sus técnicas. | El análisis y la cuantificación del riesgo (ID04). | — | ID.RA; RP-12.5 y RP-10.5 |
| ID04 | Análisis de escenarios y cuantificación de riesgos | El análisis y la cuantificación del riesgo, el escenario de riesgo con la pérdida y su probabilidad, y el seguimiento del tratamiento. | La identificación de amenazas y exposición (ID03) y la decisión de apetito, tolerancia y aceptación (GV04). | — | ID.RA; RP-12.5 y RP-10.5 |
| ID05 | Evaluación de capacidades y brechas | La evaluación de capacidades, de madurez y de brechas, y las mejoras que identifica. | La evaluación de la detección (DE04) y la validación de la recuperación (RC03). | La mejora continua que no nace de un incidente (pregunta RP-13 y hallazgo C4d-002) y la prueba de eficacia que no es independiente (hallazgo C4d-012). | ID.IM |
| PR01 | Identidad y autorización | La gestión de identidades, la autenticación, la autorización y el control de acceso de personas, cargas de trabajo y agentes. | El acceso físico a las instalaciones (PR06). | — | PR.AA; RP-12.2 |
| PR02 | Protección de datos y privacidad por diseño | La protección de los datos en reposo, en tránsito y en uso, y la privacidad por diseño. | El control de acceso (PR01). | Los respaldos, que caben también en RC01 (hallazgo C4d-015). | PR.DS |
| PR03 | Hardening y arquitectura segura | La arquitectura segura, el hardening y la segmentación (PR.PS y PR.IR-01). | La resiliencia de la infraestructura y la protección física y ambiental (PR06) y el desarrollo seguro y la gestión de cambios (PR04). | — | PR.PS · PR.IR; RP-12.2 |
| PR04 | Desarrollo seguro y gestión de cambios | El desarrollo seguro de software y la gestión de cambios y de configuración a lo largo del ciclo de vida. | El hardening y la arquitectura (PR03). | — | PR.PS |
| PR05 | Preparación de personas y procedimientos | La concientización, la formación y la preparación de las personas, y los procedimientos que usan quienes ejecutan. | La cultura y la rendición de cuentas (GV10). | El procedimiento como documento normativo, que también cabe en GV03 (hallazgo C4d-010). | PR.AT |
| PR06 | Resiliencia de la infraestructura y protección física y ambiental | La resiliencia de la infraestructura y la protección física y ambiental: las medidas previas al evento (PR.IR-02 a PR.IR-04, con PR.AA-06, DE.CM-02 y PR.PS-03 como referencias de subcategoría). | La operación degradada durante el incidente (RC02) y la segmentación (PR03). | — | PR.IR; RP-12.2 y RP-12.3 |
| DE01 | Telemetría y observabilidad | La telemetría, el monitoreo continuo y la observabilidad de redes, sistemas, personas, proveedores y agentes. | La construcción y la operación de las detecciones (DE02). | — | DE.CM |
| DE02 | Ingeniería de detección y análisis | Construir y operar la detección: reglas, analítica, correlación y análisis de eventos adversos. | Ponerla a prueba y buscar lo que no detecta (DE03) y medir su cobertura y su calidad (DE04). | — | DE.AE; RP-12.4 |
| DE03 | Hunting, validación y mejora de detecciones | Poner a prueba la detección y buscar lo que no detecta: hunting, validación y mejora de las detecciones. | Construirla y operarla (DE02) y medir su cobertura y su calidad (DE04). | — | DE.AE · DE.CM; RP-12.4 |
| DE04 | Evaluación de cobertura y calidad de detección | Medir la cobertura y la calidad de la detección. | La evaluación general de capacidades (ID05). | — | DE.AE · ID.IM; RP-12.4 |
| RS01 | Preparación y coordinación de respuesta | La preparación y la coordinación de la respuesta: plan, roles, triaje y priorización de incidentes. | La contención y la erradicación (RS02) y la comunicación de crisis (RS03). | — | RS.MA; RP-12.9 |
| RS02 | Contención, erradicación y preservación de evidencia | El análisis del incidente, la contención, la erradicación y la preservación de la evidencia. | El triaje y la priorización (RS01). | — | RS.MI · RS.AN; RP-12.9 |
| RS03 | Comunicación de crisis y decisiones ejecutivas | La comunicación de crisis, las decisiones ejecutivas durante el incidente y las notificaciones obligatorias. | La coordinación con terceros y las notificaciones contractuales (RS04) y la comunicación de la recuperación (RC05). | — | RS.CO; RP-12.7 |
| RS04 | Gestión de incidentes con terceros | La coordinación del incidente con terceros, incluidas las notificaciones contractuales. | El gobierno de terceros fuera del incidente (GV09). | — | RS.CO · GV.SC; RP-12.7 |
| RC01 | Restauración y recuperación técnica | La capacidad técnica de restaurar, con sus objetivos de tiempo y de punto de recuperación. | La continuidad durante la perturbación (RC02) y la validación del retorno (RC03). | Los respaldos como protección del dato, que caben también en PR02 (hallazgo C4d-015). | RC.RP; RP-12.6 |
| RC02 | Continuidad y operación degradada | La continuidad del negocio y la operación degradada durante la perturbación. | Las medidas de resiliencia previas al evento (PR06) y la restauración técnica (RC01). | — | RC.RP; RP-12.3 y RP-12.6 |
| RC03 | Validación de recuperación y retorno seguro | La validación de la recuperación y del retorno seguro a la operación. | La restauración (RC01). | — | RC.RP; RP-12.6 |
| RC04 | Aprendizaje, corrección y mejora continua | El aprendizaje posterior al incidente, la corrección y la mejora continua. | — | Si la mejora continua queda bajo la función Recuperar (pregunta RP-13) y a qué subfunción va la que no nace de un incidente (hallazgo C4d-002). | ID.IM |
| RC05 | Comunicación de la recuperación y restitución de la confianza | La comunicación de la recuperación a las partes interesadas y la restitución de la confianza. | La comunicación durante la crisis (RS03). | — | RC.CO |

## 6. Eje H: horizontes, fuerzas, contexto y variables

**Decisión.** Horizontes: 4, sin cambio. Catalizadores 10 → 11, inhibidores 10 → 11, mecanismos homeostáticos 10 → 12, factores de contexto 7 → 8. Se introduce el concepto de variable homeostática (HV01–HV06).

### 6.1 Horizontes

| Código | Horizonte | Definición | Pre-ensayos |
|---|---|---|---|
| H01 | Foundational | Práctica consolidada y vigente; no significa madurez baja. | 341 (46,1 %) |
| H02 | Evolving | Práctica existente modificada por fuerzas de transformación. | 240 (32,5 %) |
| H03 | Emerging | Práctica o capacidad nueva o en consolidación; no implica superioridad. | 123 (16,6 %) |
| H04 | Convergent | Integración de disciplinas o capacidades; no es una etapa obligatoria. | 22 (3,0 %) |
| — | Indeterminado | El texto no da evidencia evolutiva. | 13 (1,8 %) |

H describe evolución y equilibrio; no es madurez. El horizonte «indeterminado» es una respuesta válida.

### 6.2 Fuerzas de aceleración: catalizadores

| Código | Nombre | Qué es | Estado | Pre-ensayos que la tratan |
|---|---|---|---|---|
| CAT01 | Innovación tecnológica | Capacidades técnicas nuevas (IA generativa y agéntica, nube, automatización) que habilitan o exigen prácticas nuevas. | vigente | 65 |
| CAT02 | Presión competitiva | Pares o competidores que adoptan antes y vuelven costoso esperar. | vigente | 1 |
| CAT03 | Presión regulatoria | Obligaciones nuevas o plazos regulatorios que fuerzan el cambio. | vigente | 21 |
| CAT04 | Evolución de amenazas | Adversarios que cambian de técnica, de escala o de velocidad. | vigente | 40 |
| CAT05 | Transformación empresarial | Cambios del modelo de negocio o de operación que arrastran a la seguridad. | vigente | 14 |
| CAT06 | Presión económica | Exigencia de eficiencia, de costo por resultado o de retorno demostrable. | vigente | 4 |
| CAT07 | Incidentes y crisis | Eventos propios o ajenos que abren una ventana de cambio. | vigente | 6 |
| CAT08 | Proveedores y ecosistema | Hojas de ruta de proveedores, plataformas y socios que empujan la adopción. | vigente | 16 |
| CAT09 | Expectativas de clientes | Clientes y contrapartes que exigen garantías o evidencia. | vigente | 10 |
| CAT10 | Patrocinio ejecutivo | Directorio o alta dirección que impulsa y financia el cambio. | vigente | 1 |
| CAT11 | Geopolítica y soberanía digital | Tensiones entre Estados, sanciones, requisitos de localización y control soberano de datos, infraestructura y proveedores. | nuevo | 2 |

### 6.3 Fuerzas de inhibición: inhibidores

| Código | Nombre | Qué es | Estado | Pre-ensayos que la tratan |
|---|---|---|---|---|
| INH01 | Deuda tecnológica | Sistemas heredados y complejidad acumulada que encarecen el cambio. | vigente | 13 |
| INH02 | Presupuesto | Fondos insuficientes o no asignados. | vigente | 16 |
| INH03 | Déficit de capacidades | Faltan habilidades o personas para ejecutar. | vigente | 21 |
| INH04 | Silos organizacionales | Fronteras entre áreas que impiden decidir u operar en conjunto. | vigente | 33 |
| INH05 | Restricciones regulatorias | Normas que limitan o demoran la adopción. | vigente | 4 |
| INH06 | Concentración y lock-in | Dependencia de pocos proveedores que reduce las opciones. | vigente | 15 |
| INH07 | Calidad insuficiente de datos | Datos incompletos, sin dueño o sin clasificar. | vigente | 25 |
| INH08 | Resistencia cultural | Hábitos, incentivos y temores que frenan la adopción. | vigente | 19 |
| INH09 | Limitaciones operativas | Capacidad operativa saturada: no hay margen para cambiar mientras se opera. | vigente | 55 |
| INH10 | Incertidumbre tecnológica | Madurez, estándares o rumbo todavía inestables. | vigente | 15 |
| INH11 | Carga cognitiva y fatiga de decisión | Exceso de alertas, decisiones y contexto que degrada el juicio de las personas y de quienes supervisan agentes. | nuevo | 8 |

### 6.4 Mecanismos homeostáticos

| Código | Nombre | Qué es | Estado | Pre-ensayos que la tratan |
|---|---|---|---|---|
| HOM01 | Apetito y tolerancia al riesgo | Límites declarados que indican cuánto riesgo se acepta mientras se cambia. | vigente | 54 |
| HOM02 | Gestión de cambios | Control de qué cambia, cuándo y con qué reversibilidad. | vigente | 48 |
| HOM03 | Segregación de funciones | Separación entre quien propone, quien aprueba y quien ejecuta. | vigente | 23 |
| HOM04 | Monitoreo continuo | Observación permanente que detecta los desvíos a tiempo. | vigente | 52 |
| HOM05 | Respuesta a incidentes | Capacidad de contener y corregir cuando el desvío ocurre. | vigente | 47 |
| HOM06 | Continuidad | Sostener los servicios críticos durante la perturbación. | vigente | 25 |
| HOM07 | Rollback y recuperación | Volver a un estado conocido y bueno. | vigente | 34 |
| HOM08 | Gobierno y supervisión | Órganos y cadencias que revisan y corrigen el rumbo. | vigente | 134 |
| HOM09 | Assurance y validación | Prueba independiente de que los controles funcionan. | vigente | 164 |
| HOM10 | Aprendizaje organizacional | Convertir incidentes y resultados en cambios de práctica. | vigente | 26 |
| HOM11 | Metacognición y revisión de supuestos | Práctica deliberada de revisar cómo se decide: supuestos, sesgos y modelos mentales. | nuevo | 18 |
| HOM12 | Gobierno de la autonomía (niveles, aprobación humana e interruptor probado) | Niveles de autonomía, aprobación humana registrada e interruptor probado para agentes. | nuevo | 69 |

### 6.5 Contexto de ejecución

| Código | Factor | Qué describe | Estado |
|---|---|---|---|
| HX01 | Industria | Sector y modelo de negocio. | vigente |
| HX02 | Jurisdicción | Países y regímenes regulatorios aplicables. | vigente |
| HX03 | Postura tecnológica | Plataformas, nube y deuda técnica de partida. | vigente |
| HX04 | Criticidad | Criticidad de los servicios y de los datos afectados. | vigente |
| HX05 | Dependencia | Dependencia de terceros, plataformas y proveedores. | vigente |
| HX06 | Presión de adopción | Urgencia con que el negocio pide adoptar. | vigente |
| HX07 | Preparación | Preparación de personas, procesos y datos. | vigente |
| HX08 | Configuración de la fuerza de trabajo (humana, híbrida, operada por agentes) | Cómo se reparte el trabajo entre personas y agentes. | nuevo |

Valores de HX08: personas con asistente; equipos de personas y agentes; dirigida por personas y operada por agentes. Fuente: Fases de la Frontier Firm, Microsoft Work Trend Index 2025 (no son lineales).

### 6.6 Variables homeostáticas (nuevo concepto)

Una variable homeostática es lo que la organización necesita mantener dentro de límites aceptables mientras cambia. Cada mecanismo homeostático regula al menos una variable; 17 de las 22 fuerzas presionan al menos una y CAT08, INH02, INH04, INH05 e INH10 no presionan ninguna. La tabla es un modelo de referencia; en una organización concreta se verifica con evidencia. La relación «presiona» no tiene todavía signo ni dice sobre qué término de la variable actúa, y «regula» no distingue el papel de cada mecanismo: completar el modelo es el encargo RP-15, aceptado y en cola.

| Código | Variable | Qué significa | Mecanismos que la regulan | Fuerzas que la presionan |
|---|---|---|---|---|
| HV01 | Exposición residual frente al apetito de riesgo | La exposición que queda después de los controles se mantiene dentro de la tolerancia que se deriva del apetito declarado. | HOM01, HOM04, HOM09, HOM08 | CAT04, CAT01, INH01 |
| HV02 | Autoridad delegada frente a capacidad de supervisión | Lo que se delega a personas, proveedores y agentes no supera lo que se puede supervisar y revertir. | HOM12, HOM03, HOM08, HOM04 | CAT01, CAT06, INH03 |
| HV03 | Ritmo de cambio frente a capacidad de absorción | La organización cambia a la velocidad que puede absorber sin perder el control. | HOM02, HOM07, HOM10 | CAT02, CAT05, CAT10, INH08, INH09 |
| HV04 | Confianza de las partes interesadas sostenida por evidencia | La confianza del directorio, los reguladores, los clientes y el equipo se apoya en evidencia vigente. | HOM09, HOM08, HOM05 | CAT03, CAT09, CAT07, INH07 |
| HV05 | Carga cognitiva frente a capacidad de decisión | La demanda de atención y de decisión no supera la capacidad de quienes deciden. | HOM11, HOM10 | INH11, INH03, CAT04 |
| HV06 | Continuidad de los servicios críticos | Los servicios críticos se mantienen dentro de sus tolerancias de impacto. | HOM06, HOM05, HOM07 | CAT07, CAT11, INH06 |

### 6.7 Justificación de los elementos nuevos

| Elemento | Justificación |
|---|---|
| CAT11 | WEF Global Cybersecurity Outlook 2026: 64 % de las organizaciones contempla ciberataques de motivación geopolítica. ENISA Threat Landscape 2026: 57,3 % de los incidentes registrados fue de motivación ideológica (es un conteo de incidentes, no una medida de impacto ni de soberanía). El Cloud Adoption Framework de Microsoft trata la soberanía como escenario propio. |
| INH11 | El pilar OS del MCCS y el CISO-OS tratan la energía, la atención y la carga cognitiva como condición de la decisión; la supervisión de agentes agrega decisiones por hora. No estaba en el catálogo. |
| HOM11 | El MCCS es un sistema metacognitivo: sin un mecanismo que revise supuestos y sesgos, el Atlas no podía representar su propio método de navegación. |
| HOM12 | El sub-plan PO-GAC del GM-24 V7.1 define niveles de autonomía L0 a L3, aprobación humana registrada e interruptor probado (L4 es una extensión del Atlas que el sub-plan no prevé). El mecanismo se justifica por el control que describe. Como contexto, y no como prueba: el estudio de IDC de 2026 que cita Microsoft informa que 87 % de las «Frontier Firms» tiene un proceso para gobernar agentes frente a 51 % de los rezagados; el grupo se define como el 10 % superior de una escala de madurez de IA, los datos son declarados por los encuestados y la edición de 2025 fue encargada por el proveedor. |
| HX08 | Las tres fases de la Frontier Firm describen cómo se reparte el trabajo entre personas y agentes; es contexto de ejecución, no madurez. |
| HV01–HV06 | La versión 5.3 nombraba mecanismos homeostáticos pero no decía qué mantienen estable. Las variables lo explicitan: cada mecanismo regula al menos una variable y 17 de las 22 fuerzas presionan al menos una (CAT08, INH02, INH04, INH05 e INH10 no presionan ninguna en este modelo de referencia). Es una propuesta de diseño, sin respaldo normativo externo. |

## 7. Lentes

Las lentes son vistas que no forman parte de la coordenada.

- **Pilar MCCS.** Un pilar por pre-ensayo: MM, OS, DO o NX. Anclas en territorios: MM en T01; OS en T01, T03; DO en T05, T06; NX en T07. Las anclas son una hipótesis de diseño: dicen dónde se espera que viva cada pilar. En el corpus, la parte de los pre-ensayos de cada pilar cuyo territorio primario es un ancla primaria es: MM, 4 de 48; OS, 14 de 144; DO, 155 de 487; NX, 9 de 60.
- **Plano.** A (corpus académico) o B (capacidades contratadas). Correspondencia de las instancias del plano B con dominios: productividad en D09; XDR en D14; endpoints en D09; identidades en D05; datos en D06; SIEM en D14; nube en D10.
- **Pilar de la agenda de IA.** Seguridad de la IA (D20); IA para la seguridad (D21, D22, D23); IA adversaria (D12).

## 8. Reglas de asignación

1. La tesis manda: se clasifica por el objeto y la tesis, no por palabras sueltas. La mera mención de IA no lleva a T07 ni a D20–D23.
2. Cardinalidad: un territorio primario y hasta 2 secundarios; un dominio primario y hasta 3 secundarios; una subfunción primaria y hasta 2 secundarias; un horizonte o «indeterminado»; como máximo 1 catalizador, 1 inhibidor y 2 mecanismos homeostáticos, solo si el texto los nombra; un pilar MCCS.
3. D25 cuando el objeto es la arquitectura o un principio transversal; si es el control de un pilar concreto, queda en el dominio del pilar.
4. D26 cuando el objeto es la disciplina criptográfica; el cifrado como un control más de protección de datos queda en D06.
5. D27 cuando el objeto es la seguridad física, ambiental o de instalaciones, o el mantenimiento como dependencia del control.
6. D28 cuando el objeto es el método para demostrar o medir la eficacia; la obligación y su conformidad quedan en D03; el riesgo con la métrica como medio queda en D02; la IA como instrumento de prueba queda en D22.
7. Gobierno, riesgo y cumplimiento de la IA: D01, D02 o D03 con territorio T07.
8. Plano B: una instancia de dominio se ubica en el dominio del Atlas que indica lentes.plano_b y no se usa como evidencia del corpus académico.

### 8.1 Enunciados adoptados el 16 de noviembre de 2026 (reglas de asignación, revisión 2)

Las ocho reglas de arriba son las reglas base de la Taxonomía 6.0. Los revisores de la versión 1.2 encontraron casos que esas reglas no deciden y propusieron 18 reglas, con 95 enunciados. El 16 de noviembre de 2026 el autor escribió «Acepto el cambio de reglas», y el curador lo leyó como la adopción de las 18 reglas; esa lectura espera su confirmación (decisión D-15.1). Con ella, los 60 enunciados que tenían texto listo quedan adoptados: precisan las reglas base y, donde las precisan, prevalecen. Con ellos se releyó el corpus (documento 14, sección 4).

| Enunciado | Se aplica a | Texto adoptado |
|---|---|---|
| RP-01.1 | dominio | Cuando la tesis aplica una disciplina (gobierno, riesgo, cumplimiento, monitoreo, respuesta, continuidad o aseguramiento) a un objeto que tiene dominio propio (identidad, datos, nube, OT, IoT o IA), el dominio primario es el de la disciplina y el del objeto queda como secundario. |
| RP-01.2 | dominio | El dominio del objeto es primario cuando la tesis trata el control técnico propio de ese objeto. |
| RP-02.1 | dominio | D28 es primario cuando la tesis discute la validez del método de prueba, de medición o de evidencia. |
| RP-02.2 | dominio | Si lo que se prueba o se mide es la eficacia de una capacidad concreta que tiene dominio propio, queda en el dominio de esa capacidad con D28 como secundario. |
| RP-02.3 | dominio | El destinatario del texto («ante el auditor», «debe poder demostrar») no cambia el dominio. |
| RP-02.4 | dominio | La evidencia de cumplimiento de una obligación queda en D03; la gestión de la evidencia como disciplina es D28. |
| RP-02.5 | dominio | La auditoría de la gestión del riesgo es D28; la validación de un modelo de cuantificación queda en D02. |
| RP-02.6 | dominio | El aseguramiento de una arquitectura o de un principio es D28; su diseño es D25. |
| RP-02.7 | dominio | La evidencia sobre controles físicos es D27 cuando el objeto es el control y D28 cuando es el método. |
| RP-03.1 | dominio (definición de D03) | Definición de D03: «Obligaciones aplicables y su conformidad, incluida la auditoría de conformidad con una obligación». |
| RP-03.2 | dominio | La auditoría como disciplina, con sus atestaciones, es D28. |
| RP-04.1 | dominio | Gobierno, riesgo y cumplimiento de la IA: D01 cuando la tesis decide quién autoriza, por qué ruta y con qué límites; D02 cuando identifica, cuantifica, acepta o transfiere el riesgo; D03 cuando trata una obligación. |
| RP-04.2 | territorio | El territorio es T07 salvo que la tesis adopte otra perspectiva: T07 es la consecuencia habitual de la regla, no su condición. |
| RP-04.3 | dominio | El mecanismo técnico que hace cumplir la autonomía (interruptor, límites de lote, compuertas en el entorno de ejecución) queda en D20. |
| RP-04.4 | dominio | El aseguramiento de la IA (pruebas, evaluación y evidencia de sus controles) es D28; la IA como instrumento de prueba es D22 cuando la tesis trata lo que la IA aporta a la prueba. |
| RP-04.5 | dominio | D21 y D23 llevan frente a D14, D15, D11 y D13 la misma precedencia que D22 frente a D28. |
| RP-04.6 | dominio y territorio | La regla de uso de herramientas de IA por los empleados es D01 con T07; su control técnico es D06 o D09. |
| RP-04.7 | subfunción | Cuando el dominio cambia por esta regla, la subfunción se revisa con él. |
| RP-05.1 | dominio | «Pilar» designa un dominio de protección o de ecosistema con objeto propio (D05 a D11 y D18 a D20). |
| RP-05.2 | dominio | Son principios transversales Zero Trust, seguro por diseño y por defecto, defensa en profundidad, mínimo privilegio como principio y resiliencia por diseño. |
| RP-05.3 | dominio | La arquitectura de referencia es D25 aunque su alcance sea un solo dominio; el control que la implementa queda en el pilar. |
| RP-05.4 | dominio | En el acceso Zero Trust, el control que decide quién accede va a D05 y el que define por dónde va a D08. |
| RP-05.5 | dominio | La ingeniería de seguridad de sistemas es D25. |
| RP-06.1 | dominio | Las claves, los certificados y los secretos como material criptográfico son D26. |
| RP-06.2 | dominio | La identidad de máquina que los usa es D05. |
| RP-06.3 | dominio | La detección de la fuga de secretos es D06 o D11. |
| RP-06.4 | dominio | El cifrado de red como control queda en D08 y el cifrado de datos como control, en D06. |
| RP-07.1 | dominio | Frente a D08, D27 es la instalación y D08 la infraestructura lógica. |
| RP-07.2 | dominio | Frente a D06, el destino y la sanitización de los soportes es D27 y la protección de los datos que contienen es D06. |
| RP-07.3 | dominio | La evidencia física del proveedor es D27 cuando el objeto es el control físico y D17 cuando es la relación con el proveedor. |
| RP-07.4 | dominio | Los sistemas de edificio conectados son D19 cuando el objeto es el dispositivo y D27 cuando es la instalación. |
| RP-08.1 | dominio | El inventario como insumo de la exposición es D13. |
| RP-08.2 | dominio | El inventario de un tipo de activo queda en el dominio de ese activo. |
| RP-08.3 | dominio | La configuración es D13 cuando la postura es transversal a los entornos y D10 cuando es específica de la plataforma de nube. |
| RP-09.1 | territorio | El territorio sigue al objeto de la tesis; el interlocutor ante quien responde el CISO no lo cambia. |
| RP-09.2 | territorio | T02 cuando lo que se diseña es el rol, la carga o la competencia de las personas que supervisan agentes; T07 cuando es la autoridad del agente. |
| RP-09.3 | territorio | Para D01 fuera de la IA: T02 si la tesis es quién decide y quién responde, T03 si es cómo opera la oficina y T08 si es cómo se demuestra. |
| RP-09.4 | territorio | Para D17: T04 cuando la tesis es qué dependencia o exposición existe y T08 cuando es cómo se evalúa al tercero. |
| RP-09.5 | territorio (indicadores) | Para indicadores: el estado del control (cobertura, conformidad, diseño) va en T05 y su operación en el tiempo (plazos, cadencias, corrección), en T06. |
| RP-09.6 | territorio | T01 cubre el juicio de una persona; la oportunidad y la calidad de la decisión de un órgano van en T02. |
| RP-09.7 | territorio | Las cadencias de los controles van en T06 y las de la oficina, en T03. |
| RP-10.1 | territorio y dominio | Prueba de sustitución: si la tesis sigue siendo válida al reemplazar «IA» por «sistema», la IA es contexto y no objeto. |
| RP-10.2 | método de lectura | En la serie K, la tesis es la primera oración junto con el título. |
| RP-10.3 | dominio | En los puentes, el dominio primario es el del propósito declarado en el título. |
| RP-10.4 | método de lectura | La alineación con el resto de la unidad no es un motivo de clasificación. |
| RP-10.5 | dominio y subfunción | El escenario de amenaza (el adversario y sus técnicas) es D12 con ID03; el escenario de riesgo (la pérdida y su probabilidad) es D02 con ID04. |
| RP-10.6 | dominio | Un marco como sistema de gestión va a D01 y la obligación de certificarlo, a D03; falta decidir el dominio del catálogo de controles como modelo. |
| RP-10.7 | dominio | La obligación legal de privacidad va a D03 con D07 como secundario; la ingeniería de privacidad, a D07. |
| RP-10.8 | dominio | Cuando la tesis declarada habla del programa de formación, se clasifica por la práctica de seguridad que el programa enseña. |
| RP-11.1 | subfunción | Cuando la tesis prescribe dos funciones, la subfunción primaria es la de la primera prescripción. |
| RP-11.2 | subfunción (indicadores) | La coordenada de un indicador admite hasta dos subfunciones secundarias, como la de un pre-ensayo. |
| RP-12.2 | subfunción | Delimitaciones propuestas por los revisores: PR03 es arquitectura segura, hardening y segmentación (PR.PS y PR.IR-01) y PR06 es resiliencia de la infraestructura y protección física y ambiental (PR.IR-02 a PR.IR-04, con PR.AA-06, DE.CM-02 y PR.PS-03 como referencias de subcategoría). |
| RP-12.3 | subfunción | PR06 reúne las medidas previas y RC02 la operación degradada durante el incidente. |
| RP-12.4 | subfunción | DE02 construye y opera la detección; DE03 la pone a prueba y busca lo que no detecta; DE04 mide su cobertura y su calidad. |
| RP-12.5 | subfunción | ID03 identifica amenazas, vulnerabilidades y exposición técnica; ID04 analiza y cuantifica el riesgo y sigue su tratamiento. |
| RP-12.6 | subfunción | RC01 es la capacidad técnica de restaurar con sus objetivos; RC02 es la continuidad durante la perturbación; RC03 valida el retorno. |
| RP-12.7 | subfunción | RS03 es la comunicación de crisis y las notificaciones obligatorias; RS04 es la coordinación con terceros, incluidas las notificaciones contractuales. |
| RP-12.8 | subfunción | Las sesiones de órganos con acta y decisiones van a GV07 y las cadencias de gestión del programa, a GV05. |
| RP-12.9 | subfunción | El triaje y la priorización de incidentes van a RS01. |
| RP-12.10 | subfunción | La supervisión humana de agentes, los niveles de autonomía y el interruptor se expresan con GV02 o GV03 y con el mecanismo HOM12. |

### 8.2 Preguntas que siguen abiertas

Una aceptación no las contesta. Mientras no tengan respuesta vale lo que estaba. En la relectura, los lectores podían anotar seis de ellas en un caso concreto, y el cambio de ese eje no se aplicó donde alguno la anotó; el freno depende de que el lector la haya visto. La revisión de la versión candidata encontró además seis puntos sin decidir, que frenan otros cambios (documento 14, sección 3.3).

| Enunciado | Afecta a | Pregunta |
|---|---|---|
| RP-08.4 | dominio | ¿Dónde van el catálogo y el ciclo de vida de los controles: D01, D28 o un dominio nuevo (candidato W02)? |
| RP-14.3 | pilar MCCS | ¿En qué pilar van el liderazgo de personas y la gestión de equipos? |
| RP-17.1 | lente de IA | ¿A qué tipo de elemento se asigna la lente de la agenda de IA y con qué regla? |
| RP-17.4 | plano | Los pre-ensayos que desarrollan un producto de un proveedor, ¿pasan al plano B o se reescriben sin marca? |
| RP-18.2 | dominio | ¿Dónde está la frontera entre D18 y D19, o se consolidan? |
| RP-18.4 | dominio | ¿Dónde van la carga y la capacidad del equipo? |
| RP-18.5 | Biblioteca | ¿Los conceptos de la Biblioteca llevan dominio? |
| RP-18.6 | modelo | ¿Qué eje expresa el aseguramiento, que hoy se marca en cuatro (T08, D28, GV08 y HOM09)? |
| RP-18.7 | dominio | ¿En qué dominio va la automatización de seguridad que no usa IA? |
| RP-13 (dos opciones que se excluyen) | subfunción | ¿La mejora continua pasa a la función Identificar con un código nuevo y RC04 queda para las lecciones de la recuperación (RP-13.1, opción a), o se mantiene RC04 y el Atlas cuenta como recuperación el aprendizaje posterior al incidente (RP-13.2, opción b)? |
| RP-10.6 (cláusula final) | dominio | ¿En qué dominio va el catálogo de controles como modelo? |

### 8.3 Encargos de trabajo

El autor los aceptó. 3 se hicieron en la versión 1.3 y 21 quedan en cola.

| Enunciado | Encargo | Estado |
|---|---|---|
| RP-12.1 | Dar a cada subfunción una definición de una línea con lo que incluye y lo que excluye. | Hecho en la versión 1.3: 34 definiciones de trabajo, redactadas con el nombre, la categoría de CSF 2.0 y los enunciados adoptados; donde ninguna regla adoptada fija la frontera, la definición lo dice. Las redactó el curador y el autor no las vio (decisión D-15.7); la revisión de la versión candidata señaló que algunas se pisan sin criterio de desempate. |
| RP-14.1 | Derivar las anclas de los elementos de la definición de cada pilar. | En cola para la próxima iteración: trabajo de diseño sobre las anclas del MCCS |
| RP-14.2 | Registrar la escala, individual o de oficina, de cada pre-ensayo del pilar OS. | En cola para la próxima iteración: hecho en parte: la relectura registró la escala que vio cada lector, pero la mayoría de los pre-ensayos del pilar OS quedó sin escala y las dos lecturas no se conciliaron (documento 14, sección 4.9) |
| RP-15.1 | Vincular con una variable las cinco fuerzas que hoy no presionan ninguna o declararlas fuera del modelo. | En cola para la próxima iteración: trabajo de diseño sobre el modelo de referencia del eje H |
| RP-15.2 | Definir INH11 como causa (volumen de alertas y de decisiones) y no como el estado que mide HV05. | En cola para la próxima iteración: trabajo de diseño sobre el modelo de referencia del eje H |
| RP-15.3 | Dar a «presiona» el sentido del efecto y el término de la variable sobre el que actúa (demanda o capacidad). | En cola para la próxima iteración: trabajo de diseño sobre el modelo de referencia del eje H |
| RP-15.4 | Dar a «regula» el papel de cada mecanismo: referencia, sensor, decisor o efector. | En cola para la próxima iteración: trabajo de diseño sobre el modelo de referencia del eje H |
| RP-15.5 | Distinguir contexto (condición de partida medible) de fuerza (cambio en curso). | En cola para la próxima iteración: trabajo de diseño sobre el modelo de referencia del eje H |
| RP-15.6 | Separar la convergencia del horizonte o admitir dos valores. | En cola para la próxima iteración: trabajo de diseño sobre el modelo de referencia del eje H |
| RP-15.7 | Evaluar una variable de calidad de la decisión y otra de equilibrio económico del programa. | En cola para la próxima iteración: trabajo de diseño sobre el modelo de referencia del eje H |
| RP-15.8 | Fijar en el glosario si «fuerza» incluye a los mecanismos. | En cola para la próxima iteración: trabajo de diseño sobre el modelo de referencia del eje H |
| RP-15.9 | Dar valores a los factores de contexto HX01 a HX07. | En cola para la próxima iteración: trabajo de diseño sobre el modelo de referencia del eje H |
| RP-16.1 | Reescribir C2 con una prueba verificable y aplicarla del mismo modo a todos los candidatos. | En cola para la próxima iteración: trabajo de diseño sobre los criterios de admisión de dominios; puede reabrir la cantidad de dominios |
| RP-16.2 | Incorporar la completitud como criterio explícito o retirar el argumento. | En cola para la próxima iteración: trabajo de diseño sobre los criterios de admisión de dominios; puede reabrir la cantidad de dominios |
| RP-16.3 | Evaluar C3 y C4 sobre el mismo objeto. | En cola para la próxima iteración: trabajo de diseño sobre los criterios de admisión de dominios; puede reabrir la cantidad de dominios |
| RP-16.4 | Documentar la evidencia de C4. | En cola para la próxima iteración: trabajo de diseño sobre los criterios de admisión de dominios; puede reabrir la cantidad de dominios |
| RP-16.5 | Definir qué es un artefacto independiente y qué es «primer nivel» en cada norma. | En cola para la próxima iteración: trabajo de diseño sobre los criterios de admisión de dominios; puede reabrir la cantidad de dominios |
| RP-16.6 | Publicar para los nueve candidatos la misma tabla de cinco criterios que tienen los admitidos. | En cola para la próxima iteración: trabajo de diseño sobre los criterios de admisión de dominios; puede reabrir la cantidad de dominios |
| RP-16.7 | Agregar al cruce de territorios una prueba que pueda fallar, por ejemplo la proporción de elementos externos que necesitan dos o más territorios. | En cola para la próxima iteración: trabajo de diseño sobre los criterios de admisión de dominios; puede reabrir la cantidad de dominios |
| RP-16.8 | Medir C3 con un criterio que no dependa de la migración, por ejemplo los pre-ensayos cuya coordenada 5.3 los clasificadores marcaron como forzada. | En cola para la próxima iteración: trabajo de diseño sobre los criterios de admisión de dominios; puede reabrir la cantidad de dominios |
| RP-17.2 | Registrar el plano como propiedad del nodo. | En cola para la próxima iteración: incluye una decisión de alcance: a qué tipos de nodo se les registra el plano. Hoy lo llevan, como vínculo con la lente, los 755 pre-ensayos y los 7 productos-control, y como propiedad solo esos 7 |
| RP-17.3 | Definir las familias de dominios (Gobierno, Protección, Operaciones, Ecosistemas, Personas) y su criterio, o quitar el campo. | En cola para la próxima iteración: incluye una elección: definir las familias de dominios o quitar el campo |
| RP-18.1 | Aplicar al corpus, con una lectura dedicada, los ajustes de alcance de D09, D13, D17 y D24. | Hecho en la versión 1.3 con la relectura general y no con una lectura dedicada, como pedía el encargo: los lectores recibieron los alcances ajustados de D09, D13, D17 y D24. El efecto en esos cuatro dominios está en el documento 14, sección 3.4. |
| RP-18.3 | Revisar el alojamiento en D10 de los pre-ensayos de red antes de tratar a D08 como espacio en blanco. | Hecho en la versión 1.3 con la relectura general: los pre-ensayos de red alojados en D10 se volvieron a leer con el resto del corpus. |

### 8.4 Las reglas como se propusieron

La tabla conserva el texto con que cada regla se le presentó al autor en la versión 1.2, con las cifras de entonces, y agrega su estado. En tres (RP-13, RP-14 y RP-16) la versión 1.2 ya había hecho, como corrección, una parte de lo que pedían los hallazgos; el autor confirmó esos cambios en bloque. El texto completo, con los hallazgos de origen, está en `data/reglas_propuestas_D11.csv`.

| Código | Tema | Texto propuesto | Por qué | Ya hecho en la 1.2 | Estado en la 1.3 |
|---|---|---|---|---|---|
| RP-01 | Precedencia general entre disciplina y objeto | Cuando la tesis aplica una disciplina (gobierno, riesgo, cumplimiento, monitoreo, respuesta, continuidad o aseguramiento) a un objeto que tiene dominio propio (identidad, datos, nube, OT, IoT o IA), el dominio primario es el de la disciplina y el del objeto queda como secundario. El dominio del objeto es primario cuando la tesis trata el control técnico propio de ese objeto. | Las reglas 6 y 7 ya aplican este criterio a dos casos; falta la regla general. Si se adopta, seis de los siete pre-ensayos APX alojados en D19 cambiarían de dominio y el corpus necesita una lectura dedicada. | — | 2 adoptados. |
| RP-02 | Regla 6: cláusula de pilar y fronteras de D28 | D28 es primario cuando la tesis discute la validez del método de prueba, de medición o de evidencia. Si lo que se prueba o se mide es la eficacia de una capacidad concreta que tiene dominio propio, queda en el dominio de esa capacidad con D28 como secundario. El destinatario del texto («ante el auditor», «debe poder demostrar») no cambia el dominio. La evidencia de cumplimiento de una obligación queda en D03; la gestión de la evidencia como disciplina es D28. La auditoría de la gestión del riesgo es D28; la validación de un modelo de cuantificación queda en D02. El aseguramiento de una arquitectura o de un principio es D28; su diseño es D25. La evidencia sobre controles físicos es D27 cuando el objeto es el control y D28 cuando es el método. | Las 53 migraciones a D28 llegaron desde 13 dominios y la regla 6 solo nombra tres. Sin la cláusula, objetos casi gemelos quedaron en dominios distintos. | — | 7 adoptados. |
| RP-03 | La auditoría en D03 y en D28 | Definición de D03: «Obligaciones aplicables y su conformidad, incluida la auditoría de conformidad con una obligación». La auditoría como disciplina, con sus atestaciones, es D28. | Hoy la palabra «auditoría» figura en las dos definiciones y el ajuste 6.0 de D03 no la menciona. Cuatro revisores lo señalaron por separado. | — | 2 adoptados. |
| RP-04 | Regla 7: desempate, territorio y alcance | Gobierno, riesgo y cumplimiento de la IA: D01 cuando la tesis decide quién autoriza, por qué ruta y con qué límites; D02 cuando identifica, cuantifica, acepta o transfiere el riesgo; D03 cuando trata una obligación. El territorio es T07 salvo que la tesis adopte otra perspectiva: T07 es la consecuencia habitual de la regla, no su condición. El mecanismo técnico que hace cumplir la autonomía (interruptor, límites de lote, compuertas en el entorno de ejecución) queda en D20. El aseguramiento de la IA (pruebas, evaluación y evidencia de sus controles) es D28; la IA como instrumento de prueba es D22 cuando la tesis trata lo que la IA aporta a la prueba. D21 y D23 llevan frente a D14, D15, D11 y D13 la misma precedencia que D22 frente a D28. La regla de uso de herramientas de IA por los empleados es D01 con T07; su control técnico es D06 o D09. Cuando el dominio cambia por esta regla, la subfunción se revisa con él. | La versión 1.2 aplicó la regla 7 solo donde dos lecturas coincidieron. Los casos en que no coincidieron dependen de estos desempates. | — | 7 adoptados. |
| RP-05 | Regla 3: qué es un pilar y qué es un principio transversal | «Pilar» designa un dominio de protección o de ecosistema con objeto propio (D05 a D11 y D18 a D20). Son principios transversales Zero Trust, seguro por diseño y por defecto, defensa en profundidad, mínimo privilegio como principio y resiliencia por diseño. La arquitectura de referencia es D25 aunque su alcance sea un solo dominio; el control que la implementa queda en el pilar. En el acceso Zero Trust, el control que decide quién accede va a D05 y el que define por dónde va a D08. La ingeniería de seguridad de sistemas es D25. | La regla 3 depende de la palabra «pilar», que la taxonomía no define, y da solo dos ejemplos. | — | 5 adoptados. |
| RP-06 | Regla 4: fronteras de D26 | Las claves, los certificados y los secretos como material criptográfico son D26. La identidad de máquina que los usa es D05. La detección de la fuga de secretos es D06 o D11. El cifrado de red como control queda en D08 y el cifrado de datos como control, en D06. | La versión 1.2 ya reasignó a D06 el requisito 4 de PCI DSS en el cruce con dominios, por la regla 4 vigente. | — | 4 adoptados. |
| RP-07 | Regla 5: fronteras de D27 | Frente a D08, D27 es la instalación y D08 la infraestructura lógica. Frente a D06, el destino y la sanitización de los soportes es D27 y la protección de los datos que contienen es D06. La evidencia física del proveedor es D27 cuando el objeto es el control físico y D17 cuando es la relación con el proveedor. Los sistemas de edificio conectados son D19 cuando el objeto es el dispositivo y D27 cuando es la instalación. | La regla 5 solo separa D27 de D16 y de D18. | — | 4 adoptados. |
| RP-08 | Inventario, activos, configuración y ciclo de vida de los controles | El inventario como insumo de la exposición es D13. El inventario de un tipo de activo queda en el dominio de ese activo. La configuración es D13 cuando la postura es transversal a los entornos y D10 cuando es específica de la plataforma de nube. Falta decidir dónde va el catálogo y el ciclo de vida de los controles: D01, D28 o el candidato W02 de la lista de vigilancia. | Ningún pre-ensayo de inventario está hoy en D13, y D13 aloja de hecho el ciclo de vida de los controles sin que su definición lo diga. | — | 3 adoptados, 1 preguntas abiertas. |
| RP-09 | Territorios: de quién es la perspectiva y desempates | El territorio sigue al objeto de la tesis; el interlocutor ante quien responde el CISO no lo cambia. T02 cuando lo que se diseña es el rol, la carga o la competencia de las personas que supervisan agentes; T07 cuando es la autoridad del agente. Para D01 fuera de la IA: T02 si la tesis es quién decide y quién responde, T03 si es cómo opera la oficina y T08 si es cómo se demuestra. Para D17: T04 cuando la tesis es qué dependencia o exposición existe y T08 cuando es cómo se evalúa al tercero. Para indicadores: el estado del control (cobertura, conformidad, diseño) va en T05 y su operación en el tiempo (plazos, cadencias, corrección), en T06. T01 cubre el juicio de una persona; la oportunidad y la calidad de la decisión de un órgano van en T02. Las cadencias de los controles van en T06 y las de la oficina, en T03. | Los revisores encontraron casos en que las reglas no dicen de quién es la perspectiva, y el gobierno no tiene un territorio propio. En la muestra a ciegas el territorio es además el eje que menos coincide con la coordenada vigente, aunque con esos tamaños la diferencia con el dominio no es concluyente. | — | 7 adoptados. |
| RP-10 | Regla 1: pruebas de aplicación | Prueba de sustitución: si la tesis sigue siendo válida al reemplazar «IA» por «sistema», la IA es contexto y no objeto. En la serie K, la tesis es la primera oración junto con el título. En los puentes, el dominio primario es el del propósito declarado en el título. La alineación con el resto de la unidad no es un motivo de clasificación. El escenario de amenaza (el adversario y sus técnicas) es D12 con ID03; el escenario de riesgo (la pérdida y su probabilidad) es D02 con ID04. Un marco como sistema de gestión va a D01 y la obligación de certificarlo, a D03; falta decidir el dominio del catálogo de controles como modelo. La obligación legal de privacidad va a D03 con D07 como secundario; la ingeniería de privacidad, a D07. Cuando la tesis declarada habla del programa de formación, se clasifica por la práctica de seguridad que el programa enseña. | En 20 de los 47 textos de la muestra a ciegas el campo «tesis» no contiene una tesis utilizable. | — | 8 adoptados. |
| RP-11 | Regla 2: desempates de cardinalidad | Cuando la tesis prescribe dos funciones, la subfunción primaria es la de la primera prescripción. La coordenada de un indicador admite hasta dos subfunciones secundarias, como la de un pre-ensayo. | En 4 de los 47 textos de la muestra a ciegas la diferencia entre lecturas fue solo cuál de dos subfunciones es la primaria. | — | 2 adoptados. |
| RP-12 | Subfunciones: definición y delimitación | Dar a cada subfunción una definición de una línea con lo que incluye y lo que excluye. Delimitaciones propuestas por los revisores: PR03 es arquitectura segura, hardening y segmentación (PR.PS y PR.IR-01) y PR06 es resiliencia de la infraestructura y protección física y ambiental (PR.IR-02 a PR.IR-04, con PR.AA-06, DE.CM-02 y PR.PS-03 como referencias de subcategoría). PR06 reúne las medidas previas y RC02 la operación degradada durante el incidente. DE02 construye y opera la detección; DE03 la pone a prueba y busca lo que no detecta; DE04 mide su cobertura y su calidad. ID03 identifica amenazas, vulnerabilidades y exposición técnica; ID04 analiza y cuantifica el riesgo y sigue su tratamiento. RC01 es la capacidad técnica de restaurar con sus objetivos; RC02 es la continuidad durante la perturbación; RC03 valida el retorno. RS03 es la comunicación de crisis y las notificaciones obligatorias; RS04 es la coordinación con terceros, incluidas las notificaciones contractuales. Las sesiones de órganos con acta y decisiones van a GV07 y las cadencias de gestión del programa, a GV05. El triaje y la priorización de incidentes van a RS01. La supervisión humana de agentes, los niveles de autonomía y el interruptor se expresan con GV02 o GV03 y con el mecanismo HOM12. | Las 34 subfunciones tienen solo un nombre y una categoría de CSF 2.0, y 13 de las 22 categorías están repartidas entre dos o más subfunciones sin regla que las separe. | — | 1 encargos hechos en la 1.3, 9 adoptados. |
| RP-13 | RC04 bajo la función Recuperar | Opción a: llevar la mejora continua a la función Identificar con un código nuevo, sin reutilizar RC04, y limitar RC04 a las lecciones de la recuperación. Opción b: mantener RC04 y declarar que el Atlas cuenta como recuperación el aprendizaje posterior al incidente. | La única categoría de CSF 2.0 de RC04 es ID.IM, que pertenece a Identificar; por eso la distribución por función cuenta como recuperación contenido de mejora y de auditoría. | La tabla de subfunciones candidatas de los indicadores ya trae las correspondencias que cruzan de función (ID02 para GV.OC, RS04 para GV.SC, DE04 y RC04 para ID.IM). A confirmar con la decisión D-13. | 2 preguntas abiertas. |
| RP-14 | Anclas del MCCS y escala del pilar OS | Derivar las anclas de los elementos de la definición de cada pilar. Registrar la escala, individual o de oficina, de cada pre-ensayo del pilar OS. Decidir en qué pilar va el liderazgo de personas y la gestión de equipos. | Las anclas primarias reúnen entre el 10 % y el 33 % de los pre-ensayos de cada pilar: no describen el corpus. | Las anclas ya se declaran como hipótesis de diseño, con su medición en el corpus, y las filas del MCCS del cruce de territorios ya se generan a partir de ellas. A confirmar con la decisión D-13. | 2 encargos en cola, 1 preguntas abiertas. |
| RP-15 | Eje H: completar el modelo de referencia | Vincular con una variable las cinco fuerzas que hoy no presionan ninguna o declararlas fuera del modelo. Definir INH11 como causa (volumen de alertas y de decisiones) y no como el estado que mide HV05. Dar a «presiona» el sentido del efecto y el término de la variable sobre el que actúa (demanda o capacidad). Dar a «regula» el papel de cada mecanismo: referencia, sensor, decisor o efector. Distinguir contexto (condición de partida medible) de fuerza (cambio en curso). Separar la convergencia del horizonte o admitir dos valores. Evaluar una variable de calidad de la decisión y otra de equilibrio económico del programa. Fijar en el glosario si «fuerza» incluye a los mecanismos. Dar valores a los factores de contexto HX01 a HX07. | El modelo de referencia es una propuesta de diseño sin respaldo normativo externo; la revisión halló que no cierra en varios puntos. | — | 9 encargos en cola. |
| RP-16 | Criterios de admisión de dominios | Reescribir C2 con una prueba verificable y aplicarla del mismo modo a todos los candidatos. Incorporar la completitud como criterio explícito o retirar el argumento. Evaluar C3 y C4 sobre el mismo objeto. Documentar la evidencia de C4. Definir qué es un artefacto independiente y qué es «primer nivel» en cada norma. Publicar para los nueve candidatos la misma tabla de cinco criterios que tienen los admitidos. Agregar al cruce de territorios una prueba que pueda fallar, por ejemplo la proporción de elementos externos que necesitan dos o más territorios. Medir C3 con un criterio que no dependa de la migración, por ejemplo los pre-ensayos cuya coordenada 5.3 los clasificadores marcaron como forzada. | La versión 1.2 publica la prueba de C1 y C3 aplicada a los 28 dominios y corrige los conteos, pero no reevalúa a los candidatos. | Los cruces de territorios y de funciones ya se presentan como comprobación de cobertura y no de validez, con el respaldo externo separado del propio. A confirmar con la decisión D-13. | 8 encargos en cola. |
| RP-17 | Lentes y agrupaciones | Decir a qué tipo de elemento se asigna la lente de la agenda de IA y con qué regla, y expresar sus anclas por coordenada. Registrar el plano como propiedad del nodo. Definir las familias de dominios (Gobierno, Protección, Operaciones, Ecosistemas, Personas) y su criterio, o quitar el campo. Decidir si los pre-ensayos que desarrollan una instancia de producto de un proveedor pertenecen al plano B o se reescriben sin marca. | La lente de IA ancla «IA adversaria» en D12, que no es específico de IA. En el corpus, 77 pre-ensayos del plano A nombran productos de un proveedor o al proveedor; la versión 1.2 los marcó «revisar». | — | 2 preguntas abiertas, 2 encargos en cola. |
| RP-18 | Fronteras y alcances heredados | Aplicar al corpus, con una lectura dedicada, los ajustes de alcance de D09, D13, D17 y D24. Decidir la frontera entre D18 y D19 o su consolidación. Revisar el alojamiento en D10 de los pre-ensayos de red antes de tratar a D08 como espacio en blanco. Decir dónde van la carga y la capacidad del equipo. Decir si los conceptos de la Biblioteca llevan dominio. Decidir qué eje expresa el aseguramiento, que hoy se marca en cuatro (T08, D28, GV08 y HOM09). Decidir en qué dominio va la automatización de seguridad que no usa IA, que hoy es el único respaldo externo de D23. | La columna «Corpus 6.0» cuenta códigos de la 6.0 con el alojamiento heredado: solo D20 tuvo una lectura completa. | — | 2 encargos hechos en la 1.3, 5 preguntas abiertas. |

## 9. Gobierno de la taxonomía

- Los códigos no se renumeran ni se reutilizan. Un código retirado queda como «retirado» con su sucesor.
- Todo cambio de catálogo exige una decisión de arquitectura (ADR), un conjunto de cambios propuesto y aprobación humana.
- Las subfunciones, las fuerzas, las variables y las lentes son editoriales del Atlas; no son categorías oficiales de NIST ni de ningún otro organismo.
- La clasificación asistida por agentes es siempre una propuesta: lleva método, confianza y versión de taxonomía, y la aprueba un curador.
- Revisión de la taxonomía: al menos una vez por año y cada vez que cambie un artefacto estructural de la base (CSF, ISO/IEC 27002, CCM, CIS Controls).
- Política de migración: la coordenada vigente se conserva salvo que el cambio lo cause (a) un dominio o una subfunción nuevos del catálogo 6.0, (b) un ajuste de alcance o una regla que el autor haya aceptado, o (c) la vía de corrección.
- Vía de corrección (ADR-028, aceptada): una coordenada se corrige cuando dos lecturas coinciden en el destino, o cuando una adjudicación escrita se apoya en la tesis y en una regla explícita. En la relectura de la versión 1.3 las dos lecturas fueron a ciegas, y el cambio no entró si alguna dependía de una pregunta abierta o declaraba confianza baja. Cada corrección queda registrada con su origen y su motivo, y el autor puede revertirla.
- Revisión crítica (ADR-027, aceptada): antes de publicar una versión, revisores con contexto independiente leen el paquete congelado y cada hallazgo recibe una decisión escrita.

## 10. Correcciones de la versión 1.2

Textos y conteos que la revisión crítica encontró en desacuerdo con los datos y que se corrigieron sin cambiar códigos ni cardinalidades.

| Dónde | Qué cambió | Por qué | Hallazgos |
|---|---|---|---|
| HV01, definición | «dentro del apetito declarado» pasa a «dentro de la tolerancia que se deriva del apetito declarado». | El riesgo residual se contrasta con la tolerancia, que se deriva del apetito (NIST IR 8286r1). | C8-026 |
| Variables homeostáticas, justificación | «cada fuerza presiona al menos una» pasa a «17 de las 22 fuerzas presionan al menos una». | Cinco fuerzas no presionan ninguna variable en el modelo de referencia. | C1-001, C2-033, C8-007 |
| Respaldo externo de los dominios | Los artefactos se cuentan por su identificador en la base de referencia: la Directiva NIS2 y su Reglamento de Ejecución son un solo artefacto. Son 29 artefactos y 30 conjuntos de elementos. | El documento 03 y la matriz de cobertura daban cifras distintas en nueve dominios. | C1-002, C1-003, C2-014 |
| Artefactos dedicados | Cada dedicado lleva el identificador de su artefacto en la base. No cuentan las partes de un artefacto, los documentos que no están en la base, el contenido ya contado en el primer nivel del mismo dominio ni el artefacto compartido con otro dominio. | La lista estaba escrita a mano y contaba dos veces algunos contenidos. | C1-027, C2-015 |
| Cruce con dominios: PCI DSS, requisito 4 | Dominio primario D06, con D26 como secundario. | La regla 4 deja en D06 el cifrado como control sobre los datos. | C2-011 |
| Cruce con dominios: NIST CSF 2.0, PR.PS | Dominio primario D13 por ajuste de alcance, con D11 y D10 como secundarios. | Las subcategorías de PR.PS tratan la configuración, el mantenimiento y el desarrollo seguro de cualquier plataforma, no la nube; el propio eje Z las lee así. | C2-013 |
| Cruce con dominios: CSA CCM | El conjunto pasa a «CSA CCM v4.1» y el dominio IVS a «I&S Infrastructure Security». El par de la v4 queda en la base como el elemento que usa el mapeo del GM-24. | El paquete no había aplicado a su propio cruce la corrección que propone para el currículo. | C1-041, C2-075 |
| Cruce con territorios: pilares del MCCS | Las cuatro filas se generan a partir de las anclas de la lente; OS cuenta en T01 y en T03, y DO en T05 y en T06. | Las filas no coincidían con las anclas. | C2-047 |
| Cruce con dominios: Reglamento de Ejecución de NIS2 | Los códigos del CSV pasan a «Anexo 1» … «Anexo 13», iguales a los de la base. | No se podían unir por código. | C1-035 |
| D26, criterio C3 | Se precisa qué fija NIST IR 8547, a quién obliga y qué no se contrastó. | El texto era más amplio y más firme que la verificación que lo sostiene. | C8-015 |
| D28, criterio C3 | Se retira «T08 es el territorio más poblado y no tenía dominio propio». | El argumento supone que a cada territorio le corresponde un dominio, lo que contradice la separación entre perspectiva y objeto. | C2-051 |
| W02, motivo | La cifra y los dominios se calculan desde el corpus con un criterio escrito (títulos que nombran el inventario o los activos). | La cifra publicada no se reproducía y nombraba a D13, que en la versión 1.1 no tenía ningún pre-ensayo de inventario. | C1-026, C2-003 |
| W04 y CAT11, justificación | Las cifras del WEF y de ENISA se citan con lo que miden. | Sostenían más de lo que miden. | C8-014 |
| HOM12, justificación | El sub-plan define L0 a L3; L4 es una extensión del Atlas. La cifra de IDC se cita con su origen y como contexto. | El texto decía L0–L4 y usaba una encuesta ligada al proveedor como prueba. | C2-078, C8-013 |
| Subfunciones | PR06 queda sin indicadores; se agregan notas sobre las anclas de PR03, PR06, RS01 y RC04. | Dos revisores coinciden en que los cuatro indicadores ubicados en PR06 miden segmentación y acceso de red. | C6c-001, C8-009, C8-010, C2-030, C2-026 |
| Lentes del MCCS | Las anclas se declaran como hipótesis de diseño y se publica su medición en el corpus. | El glosario las presentaba como descripción. | C2-042, C8-022 |
| Catálogo en CSV | Incluye los 137 códigos: se agregan las dos lentes de plano y las tres de la agenda de IA. | Tenía 132. | C1-023, C2-077 |

## 11. Cambios de la versión 1.3

- Las reglas de asignación pasan a la revisión 2: 60 enunciados adoptados (sección 8.1).
- La definición de D03 pasa de «Obligaciones aplicables, auditoría y conformidad» a «Obligaciones aplicables y su conformidad, incluida la auditoría de conformidad con una obligación» (enunciado RP-03.1).
- Las 34 subfunciones tienen una definición de trabajo (sección 5.1).
- Ningún código, catálogo ni cardinalidad cambió.

## 12. Archivos

- `data/taxonomia_v6_0.json`: catálogos, decisiones, cruces y reglas; el bloque `revision_1_2`, con las correcciones y las reglas como se propusieron; y el bloque `revision_1_3`, con la decisión del autor, el estado de cada enunciado y las preguntas abiertas.
- `data/reglas_propuestas_D11.csv`: las 18 reglas como se propusieron, con su estado en la versión 1.3.
- `data/reglas_propuestas_D11_enunciados.csv`: los 95 enunciados, con su estado.
- `data/preguntas_abiertas_1_3.csv`: las preguntas que siguen abiertas.
- `data/prueba_C1_C3_dominios.csv`: la prueba de respaldo externo y de corpus sobre los 28 dominios.
- `data/taxonomia_v6_0_catalogo.csv`: los 137 códigos en una tabla.
- `data/cruce_elementos_dominios.csv`, `data/cruce_elementos_territorios.csv` y `data/cruce_elementos_funciones.csv`: los cruces completos.
- `data/cobertura_dominios_artefactos.csv`: matriz de dominios por artefacto.

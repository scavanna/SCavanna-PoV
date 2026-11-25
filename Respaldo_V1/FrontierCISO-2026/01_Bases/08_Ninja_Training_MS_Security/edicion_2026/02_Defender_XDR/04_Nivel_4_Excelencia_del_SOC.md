# Nivel 4 · Excelencia del SOC · Operación de clase mundial

*Microsoft Defender XDR Ninja Training · Edición 2026*

[← Nivel 3 · Avanzado](03_Nivel_3_Avanzado.md) · [Índice del programa](README.md) · [Comunidad →](05_Comunidad.md)

<a id="excelencia"></a>

Modelo operativo, procesos, métricas, madurez, ingeniería de detección como proceso, automatización e IA con supervisión humana, y gobierno, sobre la versión pública del Security Adoption Framework y marcos abiertos. Para líderes de SOC y equipos que apuntan al 1 % superior.

*L300–L400 · 7 módulos · ~40 horas · 64 recursos*

**Módulos de este nivel:** [S1 Modelo operativo](#s1) · [S2 Procesos e incidentes](#s2) · [S3 Métricas y tableros](#s3) · [S4 Madurez y ejercicios](#s4) · [S5 Detección como proceso](#s5) · [S6 Automatización e IA](#s6) · [S7 Gobierno y reporte](#s7)

<a id="s1"></a>

## S1 · Modelo operativo del SOC moderno

*L300–L400 · ~6 h · Origen: Nuevo en esta edición (versión pública de la disciplina de operaciones de seguridad del Security Adoption Framework)*

La tecnología no salva a un SOC mal organizado. El **Security Adoption Framework** (SAF) de Microsoft define la misión de las operaciones de seguridad —limitar el impacto de negocio de los ciberataques detectando, investigando y respondiendo rápido— con tres resultados: respuesta rápida, inteligencia compartida y descubrimiento proactivo. Un SOC puede ser una persona o un equipo global 24x7, y puede tercerizarse parcial o totalmente; lo que no cambia es la necesidad de roles claros y de alineación con el negocio.

SAF describe roles basados en el estándar de The Open Group —triage (T1), investigación (T2), caza (T3), ingeniería de detección, plataforma y datos, inteligencia, coordinación de incidentes, simulación de ataques y forense— en un modelo de **especialización, no jerarquía**: el triage aporta volumen y velocidad, la investigación y la caza manejan la complejidad, los ingenieros mejoran el sistema y el liderazgo asegura la alineación. El caso del propio SOC de Microsoft muestra cómo crecer más de 100 % en incidentes con personal casi constante gracias a la automatización.

**Por qué importa**

Un modelo operativo explícito reduce la dependencia de héroes, hace predecible el escalamiento y permite justificar cada contratación o servicio tercerizado con una función concreta. Es el punto de partida de cualquier plan de excelencia: sin roles y relaciones claras, las métricas ([S3](#s3)) y la mejora continua ([S4](#s4)) no tienen dueño.

**Qué vas a lograr**

- Describir la misión, los resultados y los roles de SecOps según SAF.
- Diseñar un modelo de roles en capas con RACI hacia TI, legal, comunicaciones y riesgo.
- Identificar antipatrones del SOC y su efecto en la fatiga del analista.
- Ejecutar con tu equipo el taller autoguiado de SecOps de SAF.

> **Consejo Ninja.** Misión de SecOps según el SAF: limitar el impacto de negocio de los ciberataques detectando, investigando y respondiendo rápido, con tres resultados —respuesta rápida, inteligencia compartida y descubrimiento proactivo—. Un SOC puede ir de una persona a una operación global 24×7 y tercerizarse en parte o del todo ([disciplina SecOps del SAF](https://learn.microsoft.com/en-us/security/zero-trust/security-adoption-discipline-security-operations)).

> **Novedad.** Roles del SAF, basados en el estándar de roles de The Open Group: gerente de SecOps, triage (T1), investigación (T2), threat hunter (T3), ingeniería de detección, ingeniería de plataforma y datos, inteligencia de amenazas, coordinación y gestión de incidentes, simulación de ataques y forense. El modelo es en capas: el triage aporta volumen y velocidad; la investigación y el hunting, manejo de la complejidad; la ingeniería, mejora del sistema, y el liderazgo, alineación ([roles de SecOps](https://learn.microsoft.com/en-us/security/zero-trust/security-adoption-discipline-security-operations-roles)).

> **Atención.** Los talleres guiados del SAF se entregan como engagements de Microsoft Unified y requieren ese contrato; este programa usa solo sus versiones públicas y autoguiadas en Learn, como el taller de SecOps, el CISO Workshop y la MCRA ([talleres del SAF](https://learn.microsoft.com/en-us/security/zero-trust/workshop-business-overview)). El taller de SecOps insiste en «especialización, no jerarquía» y en tratar el burnout: trabajo manual repetitivo, propiedad poco clara y modo crisis constante ([taller de SecOps](https://learn.microsoft.com/en-us/security/zero-trust/workshop-business-security-operations)).

> **Consejo Ninja.** El caso del SOC de Microsoft (CDOC) sigue siendo una referencia: un modelo de fusion center con piso compartido, un SOC corporativo de tres niveles con automatización y un crecimiento de más de 100 % en incidentes en tres años con un equipo casi constante ([parte 1](https://www.microsoft.com/en-us/security/blog/2019/02/21/lessons-learned-from-the-microsoft-soc-part-1-organization/)); la gestión de incidentes con el negocio, Legal y privacidad está separada de los analistas técnicos ([parte 2a](https://www.microsoft.com/en-us/security/blog/2019/04/23/lessons-learned-microsoft-soc-part-2-organizing-people/)).

**¿Tienes poco tiempo?**

- [Use the Microsoft security adoption model to modernize SecOps (Establish a SecOps discipline)](https://learn.microsoft.com/en-us/security/zero-trust/security-adoption-discipline-security-operations) · Documentación
- [Understand SecOps roles in the Microsoft security adoption model.](https://learn.microsoft.com/en-us/security/zero-trust/security-adoption-discipline-security-operations-roles) · Documentación
- [Learn about the Microsoft business planning SecOps workshop (Run a SecOps adoption workshop)](https://learn.microsoft.com/en-us/security/zero-trust/workshop-business-security-operations) · Documentación
- [Avoid common issues in SecOps modernization (Avoid antipatterns in SecOps modernization)](https://learn.microsoft.com/en-us/security/zero-trust/security-adoption-discipline-security-operations-common-issues) · Documentación

### Documentación, cursos y credenciales

- [Review Microsoft Cybersecurity Reference Architectures (MCRA)](https://learn.microsoft.com/en-us/security/zero-trust/microsoft-reference-architecture) · Documentación · Oficial · Nuevo · Microsoft Learn · 3 nov 2026. Página de descarga de las MCRA (versión junio 2026) con diagramas de arquitectura de SecOps/SOC, funciones organizativas de seguridad y mapeo de capacidades Microsoft.
- [Use the Microsoft security adoption model to modernize SecOps (Establish a SecOps discipline)](https://learn.microsoft.com/en-us/security/zero-trust/security-adoption-discipline-security-operations) · Documentación · Oficial · Nuevo · Microsoft Learn · 31 may 2026. Define la misión, resultados, roles, colaboradores y alineación con Zero Trust de la disciplina SecOps dentro del Security Adoption Framework (SAF), la base pública del ADS 'Modern Security Operations'.
- [Understand SecOps roles in the Microsoft security adoption model.](https://learn.microsoft.com/en-us/security/zero-trust/security-adoption-discipline-security-operations-roles) · Documentación · Oficial · Nuevo · Microsoft Learn · 31 may 2026. Describe los roles del SOC (triage T1, investigación T2, threat hunter T3, ingeniero de detección, ingeniero de plataforma y datos, inteligencia de amenazas, coordinación de incidentes, simulación de ataques, forense) basados en el estándar de roles de The Open Group y sus socios internos.
- [Avoid common issues in SecOps modernization (Avoid antipatterns in SecOps modernization)](https://learn.microsoft.com/en-us/security/zero-trust/security-adoption-discipline-security-operations-common-issues) · Documentación · Oficial · Nuevo · Microsoft Learn · 31 may 2026. Cataloga antipatrones del SOC (sin telemetría, recolectar no es detectar, no compartir lecciones, solo red, 'no inventado aquí', objeto brillante, una sola herramienta, Toolapalooza) con prácticas para corregirlos y reducir la fatiga del analista.
- [Learn about the Microsoft business planning SecOps workshop (Run a SecOps adoption workshop)](https://learn.microsoft.com/en-us/security/zero-trust/workshop-business-security-operations) · Documentación · Oficial · Nuevo · Microsoft Learn · 31 may 2026. Guía para ejecutar un taller de planificación de modernización del SOC: participantes, agenda (misión, estado actual, antipatrones, burnout, modelo operativo, IA y Zero Trust, arquitectura de referencia) y próximos pasos.
- [Microsoft security adoption workshops](https://learn.microsoft.com/en-us/security/zero-trust/workshop-business-overview) · Documentación · Oficial · Nuevo · Microsoft Learn · 31 may 2026. Resume los talleres SAF; el 'Security ADS Module 3 - Modern Security Operations' cubre estrategia alineada al negocio, estate 'hybrid of everything', burnout, procesos y métricas, XDR+SIEM+data lake, caso Microsoft, funciones avanzadas, outsourcing y planificación.
- [Planning Guidance for Unified Security Operations in the Microsoft Defender Portal](https://learn.microsoft.com/en-za/unified-secops/overview-plan) · Documentación · Oficial · Microsoft Learn. Guía para planificar las operaciones de seguridad unificadas en el portal de Defender: requiere Defender XDR y Sentinel como base y suma Exposure Management, Security Copilot y otros servicios no incluidos en Defender XDR.
- [Microsoft Defender Experts overview](https://learn.microsoft.com/en-us/defender-xdr/defender-experts/defender-experts-overview) · Documentación · Oficial · Microsoft Learn. Panorama de la suite Defender Experts: MDR (planes 1 y 2), Hunting (XDR y Servers), for Servers, Threat Intelligence y Cybersecurity Incident Response.
- [Deploy Microsoft Security Services for Unified Security Operations](https://learn.microsoft.com/en-au/unified-secops/overview-deploy) · Documentación · Oficial · Microsoft Learn. Orden recomendado de despliegue (MDI, MDO, MDE, MDVM/IoT, MDCA), Entra ID Protection, Defender for Cloud, Security Copilot, workspace de Sentinel, RBAC y onboarding al portal de Defender.
- [Security Adoption Resources](https://learn.microsoft.com/en-us/security/adoption/adoption) · Documentación · Oficial · Microsoft Learn. Índice de recursos SAF (CISO Workshop, MCRA, guías de negocio y PDF de antipatrones) para modernizar la seguridad en un estate 'hybrid of everything'.
- [Microsoft Cybersecurity Defense Operations Center](https://learn.microsoft.com/en-us/security/engineering/fy18-strategy-brief) · Documentación · Oficial · Legado aún útil · Microsoft Learn. Brief sobre el Cyber Defense Operations Center (CDOC): instalación 24x7 que reúne especialistas y científicos de datos, conectada con más de 3.500 profesionales de seguridad, con enfoque proteger-detectar-responder. *Nota:* Documento 'FY18'; cifras históricas. La versión es-es traduce mal la inversión (dice 100 millones en lugar de más de 1.000 millones de USD)

### Anuncios y blogs oficiales

- [CISO Series: Lessons learned from the Microsoft SOC—Part 2a: Organizing people](https://www.microsoft.com/en-us/security/blog/2019/04/23/lessons-learned-microsoft-soc-part-2-organizing-people/) · Blog oficial · Empleado de Microsoft · Legado aún útil · Mark Simos, Kristina Laidler, John Dellinger · Microsoft Security Blog · 23 abr 2019. Describe el modelo de equipos y niveles del SOC de Microsoft (inteligencia de amenazas, gestión de incidentes separada, analistas T1-T3) y la automatización como empoderamiento humano, no reemplazo. *Nota:* DART se renombró Microsoft Incident Response; la idea de 'automatización para empoderar humanos' se mantiene en la guía SAF 2026
- [CISO Series: Lessons learned from the Microsoft SOC—Part 1: Organization](https://www.microsoft.com/en-us/security/blog/2019/02/21/lessons-learned-from-the-microsoft-soc-part-1-organization/) · Blog oficial · Empleado de Microsoft · Legado aún útil · Mark Simos, John Dellinger, Kristina Laidler · Microsoft Security Blog · 21 feb 2019. Caso Microsoft: el SOC corporativo opera como 'fusion center' (CDOC) con tres niveles más automatización, propósito orientado a limitar tiempo y acceso del atacante y cuatro puntos de integración con el negocio. *Nota:* Serie CDOC 2019-2020 (sigue siendo el caso de estudio público del ADS). Menciona DART, hoy Microsoft Incident Response
- [Microsoft Defender Experts MDR (página de producto)](https://www.microsoft.com/en-us/security/business/services/microsoft-defender-experts-mdr) · Blog oficial · Oficial · Microsoft Security. Página comercial del servicio MDR 24x7 de Microsoft: triage, investigación, respuesta gestionada, chat con expertos y recomendaciones de postura; diferencia MDR vs Hunting.
- [Mark Simos, Author at Microsoft Security Blog (índice de la serie 'Lessons learned from the Microsoft SOC')](https://www.microsoft.com/en-us/security/blog/author/mark-simos/page/2/) · Blog oficial · Empleado de Microsoft · Legado aún útil · Mark Simos · Microsoft Security Blog. Índice de autor que enlaza todas las partes de la serie del SOC de Microsoft (1, 2a, 2b carreras y preparación, 3a herramientas, 3b y 3c un día en la vida) además de MCRA. *Nota:* Usar como punto de navegación de la serie CDOC 2019-2020

### Laboratorios, GitHub y herramientas

- [Cloud SOC functions (cloud-security-operations-center.md)](https://github.com/MicrosoftDocs/cloud-adoption-framework/blob/master/docs/organize/cloud-security-operations-center.md) · GitHub · Oficial · Legado aún útil · martinekuan · MicrosoftDocs (GitHub) · 15 may 2020. Fuente del artículo CAF sobre funciones del SOC en la nube: métricas MTTA/MTTR, hunting por hipótesis, gestión formal de incidentes y relaciones clave (TI, legal/RR. HH., comunicaciones, riesgo). *Nota:* Contenido de 2020; enlaza la serie CDOC 'Lessons learned from the Microsoft SOC'. Útil para RACI

### Comunidad: blogs, libros, newsletters y eventos

- [Microsoft Defender XDR - SOC/SecOps: Excelencia Operacional (V01) - Essay Collections](https://es.linkedin.com/pulse/microsoft-defender-xdr-socsecops-excelencia-qh7vf) · Blog · Empleado de Microsoft · ES · Santiago Cavanna · LinkedIn (serie Microsoft Security MCSA CSU) · 1 abr 2026. Serie de 12 infografías en español sobre excelencia operacional del SOC con Defender XDR: ecosistema M365 E5, tríptico NIST CSF 2.0/Zero Trust/MITRE ATT&CK y prácticas de gobierno.

**Manos a la obra**

1. `Laboratorio` Ejecuta con tu equipo el [taller autoguiado de SecOps](https://learn.microsoft.com/en-us/security/zero-trust/workshop-business-security-operations): misión, estado actual, antipatrones, burnout, modelo operativo y arquitectura. Evidencia: minuta con tres mejoras inmediatas, cada una con dueño y fecha.
2. `Laboratorio` Mapea a las personas de tu SOC con los [roles del SAF](https://learn.microsoft.com/en-us/security/zero-trust/security-adoption-discipline-security-operations-roles) e identifica brechas y puntos únicos de falla (las personas «héroe»). Evidencia: matriz de roles con riesgos y plan de cobertura.
3. `Laboratorio` Construye el RACI del SOC con operaciones de TI, inteligencia de amenazas, arquitectura de seguridad, el programa de riesgo interno, Legal y RR. HH., Comunicaciones y la organización de riesgo, como propone el [Cloud Adoption Framework](https://github.com/MicrosoftDocs/cloud-adoption-framework/blob/master/docs/organize/cloud-security-operations-center.md). Evidencia: RACI validado por al menos dos áreas.
4. `Laboratorio` Haz un autodiagnóstico de [antipatrones de SecOps](https://learn.microsoft.com/en-us/security/zero-trust/security-adoption-discipline-security-operations-common-issues) y de las causas de fatiga del equipo. Evidencia: lista priorizada con el efecto de cada antipatrón en la operación.
5. `Laboratorio` Define tu modelo de cobertura —24×7 propio, MDR de Defender Experts o híbrido— con criterios de riesgo, costo y talento, apoyándote en la [planificación de operaciones unificadas](https://learn.microsoft.com/en-za/unified-secops/overview-plan). Evidencia: borrador de decisión que completarás en [S7](#s7).
6. `Solo producción` Pilota el nuevo modelo operativo durante un trimestre y mide la carga por rol y la rotación. Requiere personas y turnos reales. Cómo hacerlo seguro: métricas agregadas y nunca individuales, consulta previa con RR. HH. y revisión mensual con el equipo antes de ajustar.

**¿Quieres profundizar?**

- [Microsoft Defender XDR - SOC/SecOps: Excelencia Operacional (V01) - Essay Collections](https://es.linkedin.com/pulse/microsoft-defender-xdr-socsecops-excelencia-qh7vf) · Blog

<a id="s2"></a>

## S2 · Procesos: triage, escalamiento, gestión de incidentes y crisis

*L300–L400 · ~6 h · Origen: Nuevo en esta edición (SAF: planificar la respuesta a incidentes; NIST SP 800-61 Rev. 3)*

Los procesos son lo que el SOC hace cuando nadie está mirando: cómo se toma una alerta, cuándo se escala, quién declara un incidente mayor y cómo se coordina con el negocio. SAF propone principios claros: **no dañar** (preservar evidencia y no alertar al atacante con remediaciones parciales), involucrar a **legal temprano**, usar un sistema de comando de incidentes y elegir entre «limpiar sobre la marcha» en incidentes tempranos o una remediación coordinada a gran escala cuando el adversario está atrincherado.

Para crisis, SAF recomienda planificar con la mitad del personal operando a la mitad de su capacidad por el estrés, buscar la recuperación en 24 horas, no restablecer todas las contraseñas a la vez y tener roles definidos: líder técnico, enlace de comunicaciones, registro del incidente, planificador y relaciones públicas. Este módulo convierte esos principios, los playbooks de [A1](03_Nivel_3_Avanzado.md#a1) y NIST SP 800-61 Rev. 3 en el proceso escrito de tu SOC.

**Por qué importa**

Un proceso explícito de triage y escalamiento reduce el MTTA y la variabilidad entre turnos; un proceso de crisis ensayado evita las decisiones más caras de un incidente mayor, como apagar sistemas y destruir evidencia o comunicar tarde a los reguladores. Es también la base para tercerizar con SLA verificables.

**Qué vas a lograr**

- Escribir el proceso de triage y escalamiento con criterios por severidad y puntaje.
- Definir roles y cadencias de un incidente mayor según el modelo de comando de incidentes.
- Elegir entre limpieza progresiva y remediación coordinada.
- Alinear el proceso con NIST SP 800-61 Rev. 3 y con los playbooks oficiales.

> **Consejo Ninja.** El SAF define MTTA como el tiempo para reconocer una alerta o un incidente desde que se genera, y MTTR como el tiempo para corregirlo después de reconocerlo: el MTTA termina cuando un analista toma el incidente ([planificar la respuesta a incidentes](https://learn.microsoft.com/en-us/security/zero-trust/security-adoption-discipline-security-operations-incidents)). Escribe en tu proceso qué evento inicia y qué evento detiene cada reloj.

> **Atención.** Decide entre limpiar sobre la marcha (incidentes tempranos) y una remediación coordinada a gran escala (adversario atrincherado): la remediación parcial alerta al atacante. Para incidentes mayores, planifica con la mitad del personal rindiendo a la mitad por el estrés, busca recuperar en 24 horas, no restablezcas todas las contraseñas a la vez y colabora fuera de banda, como el SOC de Microsoft, que usa un inquilino no productivo ([planificar la respuesta a incidentes](https://learn.microsoft.com/en-us/security/zero-trust/security-adoption-discipline-security-operations-incidents)).

> **Novedad.** Roles de crisis recomendados: Technical Incident Leader, Communications Liaison, Incident Recorder, Forward Planner y Relaciones Públicas, con un playbook de privacidad conjunto que contempla una expectativa de notificación de 72 horas ([prepararse para la respuesta](https://learn.microsoft.com/en-us/security/zero-trust/security-operations-incident-response-readiness)). Los plazos legales dependen de cada jurisdicción: define el proceso con Legal y privacidad.

> **Qué cambió.** NIST SP 800-61 Rev. 3 (abril de 2025) reemplaza a la Rev. 2 (agosto de 2012) y alinea la respuesta a incidentes con el CSF 2.0 ([SP 800-61r3](https://csrc.nist.gov/pubs/sp/800/61/r3/final)). En el portal, la cola de incidentes con su puntaje de prioridad ya figura como experiencia heredada frente a los casos ([priorizar incidentes](https://learn.microsoft.com/en-us/defender-xdr/incident-queue)).

**¿Tienes poco tiempo?**

- [Plan for incident response in the security adoption model. (Plan incident response)](https://learn.microsoft.com/en-us/security/zero-trust/security-adoption-discipline-security-operations-incidents) · Documentación
- [Incident response playbooks overview](https://learn.microsoft.com/en-us/security/zero-trust/security-operations-incident-response-playbooks) · Documentación
- [SP 800-61 Rev. 3, Incident Response Recommendations and Considerations for Cybersecurity Risk Management: A CSF 2.0 Community Profile](https://csrc.nist.gov/pubs/sp/800/61/r3/final) · Documentación
- [Prioritize incidents in the Microsoft Defender portal (Legacy)](https://learn.microsoft.com/en-us/defender-xdr/incident-queue) · Documentación

### Documentación, cursos y credenciales

- [Plan for incident response in the security adoption model. (Plan incident response)](https://learn.microsoft.com/en-us/security/zero-trust/security-adoption-discipline-security-operations-incidents) · Documentación · Oficial · Nuevo · Microsoft Learn · 3 nov 2026. Estrategia y proceso de respuesta a incidentes del SOC: MTTA/MTTR, principios (no dañar, legal temprano), ICS, recuperación 'Big Bang', capacidad reducida bajo estrés y limpieza post-incidente.
- [Incident response playbooks overview](https://learn.microsoft.com/en-us/security/zero-trust/security-operations-incident-response-playbooks) · Documentación · Oficial · Nuevo · Microsoft Learn · 3 nov 2026. Índice de playbooks de Microsoft Incident Response (phishing, password spray, consentimiento de apps, apps comprometidas, robo de tokens) con prerequisitos, flujo, checklist y pasos de investigación.
- [SP 800-61 Rev. 3, Incident Response Recommendations and Considerations for Cybersecurity Risk Management: A CSF 2.0 Community Profile](https://csrc.nist.gov/pubs/sp/800/61/r3/final) · Documentación · Comunidad · Alexander Nelson, Sanjay Rekhi, Murugiah Souppaya, Karen Scarfone · NIST CSRC · abr 2025. Guía de NIST que integra la respuesta a incidentes en la gestión de riesgos como perfil comunitario del CSF 2.0 (Govern, Identify, Protect, Detect, Respond, Recover) y sustituye a la Rev. 2 de 2012.
- [Prioritize incidents in the Microsoft Defender portal (Legacy)](https://learn.microsoft.com/en-us/defender-xdr/incident-queue) · Documentación · Oficial · Legado aún útil · Microsoft Learn. Cola de incidentes con Defender Queue Assistant: puntaje de prioridad 0-100 por ML (rojo >85, naranja 15-85, gris <15) basado en disrupción, severidad, MITRE, criticidad del activo y rareza; exporta hasta 10.000 registros CSV. *Nota:* La página quedó marcada como experiencia 'legacy': los 'incident cases' (preview) son ahora la experiencia recomendada
- [Incident response overview](https://learn.microsoft.com/en-us/security/operations/incident-response-overview) · Documentación · Oficial · Microsoft Learn. Visión general de respuesta a incidentes como parte de SecOps, con buenas prácticas técnicas y operativas y vínculo con MTTA/MTTR.

**Manos a la obra**

1. `Laboratorio` Escribe el procedimiento de triage y escalamiento: umbrales por severidad y puntaje de prioridad, tiempos objetivo, criterios para pasar a T2 o al gestor de incidentes y qué se documenta en cada paso. Evidencia: procedimiento de dos páginas aplicado a tres incidentes de prueba.
2. `Laboratorio` Define los roles de un incidente mayor y sus cadencias (actualizaciones de estado, reuniones y relevos) con la guía para [prepararse para la respuesta](https://learn.microsoft.com/en-us/security/zero-trust/security-operations-incident-response-readiness). Evidencia: tarjeta de roles con titulares y suplentes.
3. `Laboratorio` Construye un árbol de decisión entre limpieza progresiva y remediación coordinada y aplícalo a dos casos: un phishing aislado y un compromiso de dominio ([planificar la respuesta](https://learn.microsoft.com/en-us/security/zero-trust/security-adoption-discipline-security-operations-incidents)). Evidencia: árbol y justificación de cada caso.
4. `Laboratorio` Diseña el canal de colaboración fuera de banda para incidentes mayores: espacio no productivo, cuentas separadas y lista de contactos impresa. Evidencia: documento y una prueba de acceso registrada.
5. `Laboratorio` Arma la matriz tipo de incidente → playbook con el [resumen de playbooks oficiales](https://learn.microsoft.com/en-us/security/zero-trust/security-operations-incident-response-playbooks) y la tabla [Playbooks de respuesta a incidentes](00_Programa.md#playbooks-ir). Evidencia: matriz publicada en el wiki del SOC.
6. `Solo producción` Mide durante un mes la adherencia real al proceso: calidad de la clasificación y tiempos de escalamiento en una muestra de 20 incidentes. Requiere incidentes reales. Cómo hacerlo seguro: rol de solo lectura, resultados agregados, sin señalar a personas y con las mejoras acordadas con el equipo.

<a id="s3"></a>

## S3 · Métricas y tableros del SOC

*L300–L400 · ~6 h · Origen: Nuevo en esta edición (SAF, métricas de incidentes de Sentinel y MDDR 2026)*

Lo que no se mide no mejora, pero lo que se mide mal empeora. El Cloud Adoption Framework describe la evolución del «tiempo para detectar» hacia **MTTA** (capacidad de respuesta) y **MTTR** (velocidad de remediación); Sentinel calcula «time to triage» como `FirstModifiedTime − CreatedTime` y «time to closure» como `ClosedTime − CreatedTime` sobre la tabla `SecurityIncident`, por percentiles, con el workbook «Security operations efficiency». SOC optimization agrega cobertura por amenaza y valor de los datos.

La segunda mitad es elegir métricas que cambien decisiones. El MDDR 2026 pide pasar de métricas de actividad («parches desplegados») a métricas de resultado: **exposición reducida, cobertura de detección aumentada y tiempo de mitigación comprimido**. Este módulo construye un tablero con definiciones explícitas, fórmulas reproducibles y pares velocidad-calidad para no premiar comportamientos perversos. La tabla completa está en [Métricas del SOC](00_Programa.md#metricas-soc).

**Por qué importa**

Las métricas son el idioma entre el SOC y la dirección: sin ellas, el presupuesto se discute con anécdotas. Con definiciones explícitas y percentiles por severidad, el SOC puede demostrar mejoras reales, detectar fatiga antes de que se vaya la gente y priorizar inversiones en detección o automatización donde más reducen el riesgo.

**Qué vas a lograr**

- Definir MTTD, MTTA, MTTR y MTTC con su fuente de datos y el evento que detiene cada reloj.
- Calcular métricas por percentiles y severidad con KQL sobre SecurityIncident.
- Emparejar cada métrica de velocidad con una métrica de calidad.
- Construir un tablero operativo y otro ejecutivo con métricas de resultado.

> **Atención.** El workbook de Sentinel calcula «time to triage» como `FirstModifiedTime − CreatedTime` y «time to closure» como `ClosedTime − CreatedTime`, por percentiles. Como cada actualización de un incidente crea una fila nueva en `SecurityIncident`, deduplica con `arg_max(TimeGenerated, *) by IncidentNumber` antes de calcular ([métricas de incidentes](https://learn.microsoft.com/en-us/azure/sentinel/manage-soc-with-incident-metrics), [SecurityIncident](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/securityincident)).

> **Atención.** El MTTR no significa lo mismo en todas partes: el SAF lo mide desde el reconocimiento hasta la corrección y el workbook de Sentinel, desde la creación hasta el cierre. Publica siempre la definición junto al número ([planificar la respuesta](https://learn.microsoft.com/en-us/security/zero-trust/security-adoption-discipline-security-operations-incidents)). La tabla [Métricas del SOC](00_Programa.md#metricas-soc) propone definiciones y fórmulas.

> **Novedad.** SOC optimization muestra la cobertura por amenaza: alta (más de 75 % de las reglas recomendadas activas), media (30–74 %) y baja (0–29 %) ([SOC optimization](https://learn.microsoft.com/en-us/azure/sentinel/soc-optimization/soc-optimization-access)); sus recomendaciones de valor de datos solo consideran tablas facturables con ingesta en los últimos 30 días ([referencia](https://learn.microsoft.com/en-us/azure/sentinel/soc-optimization/soc-optimization-reference)).

> **Consejo Ninja.** El MDDR 2026 pide pasar de métricas de actividad, como los parches desplegados, a resultados: exposición reducida, cobertura de detección aumentada y tiempo de mitigación comprimido ([MDDR](https://www.microsoft.com/en-us/corporate-responsibility/topics/cybersecurity/reports/microsoft-digital-defense-report/)). Reporta mediana y p90 por severidad, empareja cada métrica de velocidad con una de calidad y nunca premies tickets cerrados.

**¿Tienes poco tiempo?**

- [Manage your SOC better with incident metrics](https://learn.microsoft.com/en-us/azure/sentinel/manage-soc-with-incident-metrics) · Documentación
- [Azure Monitor Logs reference - SecurityIncident](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/securityincident) · Documentación
- [Optimize security operations (Optimize your security operations)](https://learn.microsoft.com/en-us/azure/sentinel/soc-optimization/soc-optimization-access) · Documentación
- [Microsoft Digital Defense Report 2026](https://www.microsoft.com/en-us/corporate-responsibility/topics/cybersecurity/reports/microsoft-digital-defense-report/) · Libro

### Documentación, cursos y credenciales

- [Azure Monitor Logs reference - SecurityIncident](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/securityincident) · Documentación · Oficial · Nuevo · Microsoft Learn · 27 ago 2026. Esquema de la tabla SecurityIncident (CreatedTime, FirstActivityTime, FirstModifiedTime, ClosedTime, Classification, Owner, ModifiedBy, Tasks, etc.) que alimenta los cálculos de MTTA, MTTR y falsos positivos.
- [SOC optimization recommendations types (reference)](https://learn.microsoft.com/en-us/azure/sentinel/soc-optimization/soc-optimization-reference) · Documentación · Oficial · Microsoft Learn. Referencia de recomendaciones de SOC optimization: valor de datos, cobertura basada en amenazas, etiquetado MITRE con IA (preview) y riesgos de negocio.
- [Manage your SOC better with incident metrics](https://learn.microsoft.com/en-us/azure/sentinel/manage-soc-with-incident-metrics) · Documentación · Oficial · Microsoft Learn. Explica la tabla SecurityIncident, consultas KQL de tiempo de triage (FirstModifiedTime-CreatedTime) y de cierre (ClosedTime-CreatedTime) por percentiles y el workbook 'Security operations efficiency'.
- [Optimize security operations (Optimize your security operations)](https://learn.microsoft.com/en-us/azure/sentinel/soc-optimization/soc-optimization-access) · Documentación · Oficial · Microsoft Learn. Cómo acceder y usar SOC optimization en el portal de Defender, con métricas de valor reciente, datos ingeridos y cobertura de amenazas Alta (>75%), Media (30-74%) y Baja (0-29%) de reglas recomendadas activadas.

### Anuncios y blogs oficiales

- [2025 Microsoft Digital Defense Report (MDDR) | Security Insider](https://www.microsoft.com/en-us/security/security-insider/threat-landscape/microsoft-digital-defense-report-2025) · Blog oficial · Oficial · Microsoft Threat Intelligence · Microsoft Security Insider. Resumen del MDDR 2025: acceso inicial por phishing/ingeniería social (28%), activos web sin parchear (18%) y servicios remotos expuestos (12%); solo 4% motivado por espionaje; llama a detección más rápida y respuesta automatizada.

### Comunidad: blogs, libros, newsletters y eventos

- [Microsoft Digital Defense Report 2026](https://www.microsoft.com/en-us/corporate-responsibility/topics/cybersecurity/reports/microsoft-digital-defense-report/) · Libro · Oficial · Nuevo · Microsoft Threat Intelligence · Microsoft · oct 2026. Página del MDDR 2026 con 10 conclusiones; recomienda que las métricas reportadas pasen de 'parches desplegados' a exposición reducida, cobertura de detección aumentada y tiempo de mitigación comprimido.

**Manos a la obra**

1. `Laboratorio parcial` En un workspace de Sentinel de prueba, calcula la mediana y el p90 del time to triage, del time to closure y de una aproximación del MTTD, y la tasa de falsos positivos sobre `SecurityIncident` ([métricas de incidentes](https://learn.microsoft.com/en-us/azure/sentinel/manage-soc-with-incident-metrics)). Limitación: con pocos incidentes los percentiles no son significativos; genera incidentes con reglas de prueba. En producción, usa el rol Microsoft Sentinel Reader y solo consultas. Evidencia: consultas guardadas y su resultado por severidad.
2. `Laboratorio` Escribe el diccionario de métricas del SOC: para cada métrica, el evento que inicia y detiene el reloj, la fuente de datos, el dueño y la métrica de calidad con la que se empareja, a partir de la tabla [Métricas del SOC](00_Programa.md#metricas-soc). Evidencia: diccionario aprobado por el líder del SOC.
3. `Laboratorio` Verifica qué valores toma `ModifiedBy` en tu inquilino para las acciones de automatización y de interrupción antes de calcular la tasa de automatización ([SecurityIncident](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/securityincident)). Evidencia: consulta con los valores encontrados.
4. `Laboratorio parcial` Revisa SOC optimization y la cobertura MITRE: registra el nivel de cobertura por escenario y las reglas recomendadas ([SOC optimization](https://learn.microsoft.com/en-us/azure/sentinel/soc-optimization/soc-optimization-access)). Limitación: las recomendaciones de valor de datos y de organizaciones similares requieren volumen real de ingesta. En producción, revisa con solo lectura y aplica los cambios por control de cambios. Evidencia: tabla de cobertura por escenario.
5. `Laboratorio` Diseña dos tableros: uno operativo (cola, MTTA p50 y p90 por severidad y backlog) y otro ejecutivo (tendencia de exposición, cobertura validada y tiempo de mitigación). Evidencia: maqueta o workbook de cada uno.
6. `Solo producción` Toma una línea base de 90 días de métricas reales y fija metas. Requiere datos de producción. Cómo hacerlo seguro: consultas de solo lectura, resultados agregados, sin rankings individuales y revisión con el equipo antes de publicar.

<a id="s4"></a>

## S4 · Madurez, mejora continua y ejercicios

*L300–L400 · ~6 h · Origen: Nuevo en esta edición (SOC-CMM, NIST CSF 2.0, «11 Strategies» de MITRE y SAF)*

La excelencia es un proceso, no un estado. Para saber dónde estás, los marcos públicos ayudan: **SOC-CMM** v2.4 evalúa 5 dominios y 27 aspectos con niveles de madurez de 0 (inexistente) a 5 (optimizando) y de capacidad de 0 a 3; el **NIST CSF 2.0** agrega la función Gobernar y ofrece perfiles y niveles; y las **11 Strategies of a World-Class Cybersecurity Operations Center** de MITRE empiezan por «conoce qué proteges y por qué».

Para mejorar hacen falta ejercicios y aprendizaje institucional: ejercicios de mesa periódicos con decisores reales (la guía de respuesta de Azure sugiere una cadencia trimestral), purple teaming recurrente, revisiones post-incidente breves y sin culpables, y un registro visible de mitigaciones. El informe SOC-CMM 2025 advierte que la sobreestimación en las autoevaluaciones frena la madurez: mide con evidencias y, si puedes, con un tercero.

**Por qué importa**

Una evaluación de madurez honesta convierte la intuición en un plan priorizado y defendible ante la dirección, y los ejercicios regulares descubren fallas de proceso cuando todavía cuestan poco. Los SOC que más mejoran no son los que más compran, sino los que aprenden de cada incidente y de cada ejercicio.

**Qué vas a lograr**

- Autoevaluar el SOC con SOC-CMM y el CSF 2.0 usando evidencias.
- Fijar metas de madurez por dominio con un plan de 12 meses.
- Diseñar un calendario de ejercicios de mesa y de purple team.
- Conducir revisiones post-incidente que produzcan cambios medibles.

> **Consejo Ninja.** SOC-CMM v2.4 evalúa 5 dominios y 27 aspectos, con madurez de 0 (inexistente) a 5 (optimizando) y capacidad de 0 a 3 ([SOC-CMM](https://www.soc-cmm.com/img/upload/files/37-advancing-soc-capability-and-maturity.pdf)); su informe de 2025 concluye que la sobreestimación en las autoevaluaciones frena el crecimiento de la madurez ([informe 2025](https://www.soc-cmm.com/img/upload/files/30-socmaturityreport2025.pdf)). Pide evidencias y una validación externa.

> **Novedad.** Marcos complementarios: el NIST CSF 2.0 (26 de febrero de 2024) agrega la función Gobernar y ofrece perfiles y niveles ([CSF 2.0](https://doi.org/10.6028/NIST.CSWP.29)), y las «11 Strategies» de MITRE (2022) empiezan por conocer qué proteges y por qué ([resumen](https://www.mitre.org/sites/default/files/2022-04/11-strategies-world-class-csoc-highlights.pdf)).

> **Consejo Ninja.** Ensaya con cadencia: ejercicios de mesa trimestrales de ransomware, exfiltración y amenaza interna ([respuesta a incidentes en Azure](https://learn.microsoft.com/en-us/azure/security/fundamentals/incident-response-overview)) y decisiones tomadas antes del ataque —pagar o no un rescate, notificar a reguladores y a la junta, quién puede apagar cargas críticas— ([prepararse para la respuesta](https://learn.microsoft.com/en-us/security/zero-trust/security-operations-incident-response-readiness)).

> **Consejo Ninja.** Haz revisiones post-incidente breves y multifuncionales, con un registro visible de mitigaciones y tiempo reservado para reflexionar antes de cambiar de prioridad ([antipatrones](https://learn.microsoft.com/en-us/security/zero-trust/security-adoption-discipline-security-operations-common-issues)). En el SOC de Microsoft, los hunters rotan por ejercicios de red y purple team, y cada actividad termina con una revisión compartida con el SOC y con ingeniería ([Zen and the art of threat hunting](https://www.microsoft.com/en-us/security/blog/2020/06/25/zen-and-the-art-of-threat-hunting/)).

**¿Tienes poco tiempo?**

- [SOC-CMM® best practice: Advancing SOC capability and maturity](https://www.soc-cmm.com/img/upload/files/37-advancing-soc-capability-and-maturity.pdf) · Documentación
- [The NIST Cybersecurity Framework (CSF) 2.0 (CSWP 29)](https://doi.org/10.6028/NIST.CSWP.29) · Documentación
- [Prepare for incident response](https://learn.microsoft.com/en-us/security/zero-trust/security-operations-incident-response-readiness) · Documentación
- [11 Strategies of a World-Class Cybersecurity Operations Center](https://www.mitre.org/sites/default/files/2022-04/11-strategies-of-a-world-class-cybersecurity-operations-center.pdf) · Libro

### Documentación, cursos y credenciales

- [SOC-CMM® best practice: Advancing SOC capability and maturity](https://www.soc-cmm.com/img/upload/files/37-advancing-soc-capability-and-maturity.pdf) · Documentación · Comunidad · SOC-CMM. Explica el modelo SOC-CMM v2.4 (5 dominios, 27 aspectos), los 6 niveles de madurez (0 inexistente a 5 optimizando) y los 4 niveles de capacidad, con cómo avanzar entre niveles.
- [Prepare for incident response](https://learn.microsoft.com/en-us/security/zero-trust/security-operations-incident-response-readiness) · Documentación · Oficial · Microsoft Learn. Checklist SAF de preparación: ejercicios de mesa periódicos, decisiones y decisores previos al ataque (rescate, reguladores, junta), privilegio legal, roles del incidente, playbook de privacidad (72 h), pentest y red/blue/purple/green team.
- [The NIST Cybersecurity Framework (CSF) 2.0 (CSWP 29)](https://doi.org/10.6028/NIST.CSWP.29) · Documentación · Comunidad · NIST · 26 feb 2024. Marco CSF 2.0 con seis funciones (Gobernar, Identificar, Proteger, Detectar, Responder, Recuperar), perfiles organizacionales y niveles (Tiers) útiles para medir la madurez del SOC.
- [Secure Overview - Cloud Adoption Framework](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/secure/overview) · Documentación · Oficial · Microsoft Learn. Metodología Secure del CAF: ciclo de vida de incidentes de extremo a extremo, simulaciones de mesa, reducción de falsos positivos para acelerar MTTD y retrospectivas que alimentan el backlog.
- [Incident response overview for Azure](https://learn.microsoft.com/en-us/azure/security/fundamentals/incident-response-overview) · Documentación · Oficial · Microsoft Learn. Respuesta a incidentes en Azure alineada a las fases de NIST SP 800-61: contactos 24/7, notificaciones automáticas con escalamiento por tiempo y ejercicios de mesa trimestrales.

### Anuncios y blogs oficiales

- [Lessons learned from the Microsoft SOC—Part 3d: Zen and the art of threat hunting](https://www.microsoft.com/en-us/security/blog/2020/06/25/zen-and-the-art-of-threat-hunting/) · Blog oficial · Empleado de Microsoft · Legado aún útil · Mark Simos, John Dellinger, David Fosth · Microsoft Security Blog · 25 jun 2020. Cómo caza amenazas el SOC de Microsoft: investigación proactiva por hipótesis, rotación en red/purple teaming con revisiones transparentes y apoyo a incidentes mayores. *Nota:* Útil también para S4 (cadencia purple team) y S1 (función de hunting)

### Laboratorios, GitHub y herramientas

- [Maturity Report | SOC-CMM (SOC Maturity Report 2025 y 2026)](https://www.soc-cmm.com/products/report) · Herramienta · Comunidad · Rob van Os · SOC-CMM. Página de los informes anuales de madurez SOC-CMM (2025 y 2026) con benchmarks por región, sector y tamaño, y descargas del modelo de autoevaluación bajo licencia CC BY-SA 4.0.

### Comunidad: blogs, libros, newsletters y eventos

- [11 Strategies of a World-Class Cybersecurity Operations Center](https://www.mitre.org/sites/default/files/2022-04/11-strategies-of-a-world-class-cybersecurity-operations-center.pdf) · Libro · Comunidad · Legado aún útil · Kathryn Knerler, Ingrid Parker, Carson Zimmerman · MITRE · abr 2022. Libro gratuito de MITRE con 11 estrategias para un SOC de clase mundial (contexto de misión, estructura, personal, inteligencia, métricas, automatización, etc.). *Nota:* Edición 2022, sigue siendo referencia; coautor Carson Zimmerman trabaja en Microsoft (equipo de investigaciones de M365)
- [Highlights: 11 Strategies of a World-Class Cybersecurity Operations Center](https://www.mitre.org/sites/default/files/2022-04/11-strategies-world-class-csoc-highlights.pdf) · Libro · Comunidad · Legado aún útil · MITRE · abr 2022. Folleto resumen de las 11 estrategias del SOC de MITRE, empezando por 'conoce qué proteges y por qué' en cinco áreas de conciencia situacional. *Nota:* Ideal como lectura previa de 30 minutos

**Manos a la obra**

1. `Solo producción` Haz la autoevaluación SOC-CMM con evidencias ([SOC-CMM](https://www.soc-cmm.com/img/upload/files/37-advancing-soc-capability-and-maturity.pdf)). Requiere procesos, personas y datos reales. Cómo hacerlo seguro: evidencias anonimizadas, acceso restringido al resultado y validación por un tercero para evitar la sobreestimación.
2. `Laboratorio` Mapea el estado actual de tu SOC a las funciones del [CSF 2.0](https://doi.org/10.6028/NIST.CSWP.29) (Gobernar, Identificar, Proteger, Detectar, Responder y Recuperar) con un nivel por función. Evidencia: matriz con brechas priorizadas.
3. `Laboratorio` Conduce un ejercicio de mesa de ransomware con matriz de decisiones: usa la lista de verificación de [preparación](https://learn.microsoft.com/en-us/security/zero-trust/security-operations-incident-response-readiness) para definir quién decide sobre el rescate, los reguladores y la junta, y los roles de crisis. Evidencia: registro de decisiones y brechas encontradas.
4. `Laboratorio` Arma el calendario anual de ejercicios: mesas trimestrales (ransomware, exfiltración e insider) y purple team semestral, cada uno con dueño y objetivo medible. Evidencia: calendario aprobado.
5. `Laboratorio` Escribe la plantilla de revisión post-incidente —sin culpables, multifuncional y con registro de mitigaciones— y aplícala al caso de [A8](03_Nivel_3_Avanzado.md#a8). Evidencia: revisión completa con tareas y dueños.
6. `Laboratorio` Define metas de madurez por dominio para los próximos 12 meses, con hitos trimestrales e indicadores. Evidencia: plan de mejora de una página.

**¿Quieres profundizar?**

- [Maturity Report | SOC-CMM (SOC Maturity Report 2025 y 2026)](https://www.soc-cmm.com/products/report) · Herramienta
- [Highlights: 11 Strategies of a World-Class Cybersecurity Operations Center](https://www.mitre.org/sites/default/files/2022-04/11-strategies-world-class-csoc-highlights.pdf) · Libro

<a id="s5"></a>

## S5 · Ingeniería de detección como proceso

*L300–L400 · ~6 h · Origen: Nuevo en esta edición (SAF: funciones avanzadas del SOC e ingeniería de detección)*

En [A5](03_Nivel_3_Avanzado.md#a5) aprendiste la técnica; aquí la conviertes en un proceso del SOC. La ingeniería de detección como proceso tiene entradas (solicitudes desde hunting, inteligencia, incidentes y purple team), un backlog priorizado por riesgo, un ciclo de vida —diseñar, probar, revisar, desplegar, medir, ajustar y retirar— y dueños. En la plataforma unificada, las detecciones personalizadas son la vía para las reglas nuevas, entran en la correlación por defecto y se pueden gestionar como código con Sentinel Repositories.

SAF advierte contra el antipatrón del «no inventado aquí»: configura lo que el producto ya trae antes de personalizar y mide el costo de mantener contenido propio. Este módulo define el flujo de trabajo, los criterios de calidad de una regla y los indicadores que dicen si el programa de detección mejora: cobertura validada, precisión por regla, tiempo de la idea a producción y reglas retiradas.

**Por qué importa**

Sin proceso, la ingeniería de detección se vuelve una colección de reglas huérfanas que nadie mantiene y que generan ruido. Con proceso, cada regla tiene propósito, prueba y dueño, y la organización puede demostrar cómo su cobertura crece con el panorama de amenazas mientras baja la fatiga del analista.

**Qué vas a lograr**

- Definir el ciclo de vida de una detección con entradas, criterios de calidad y dueños.
- Priorizar el backlog de detecciones por amenaza y por riesgo.
- Implementar revisión por pares y despliegue como código.
- Medir el programa con indicadores de cobertura, precisión y velocidad.

> **Qué cambió.** Las detecciones personalizadas son ahora la vía unificada para crear reglas nuevas en Sentinel y Defender XDR ([ajuste de detecciones](https://learn.microsoft.com/en-us/azure/sentinel/detection-tuning)); entran en la correlación de incidentes por defecto y puedes excluir una regla si lo necesitas ([gestionar detecciones](https://learn.microsoft.com/en-us/defender-xdr/custom-detection-manage)).

> **Novedad.** Sentinel Repositories admite hasta 5 conexiones por workspace y 800 despliegues por grupo de recursos, y el repositorio pasa a ser la única fuente de verdad ([contenido como código](https://learn.microsoft.com/en-us/azure/sentinel/ci-cd-custom-content)). Desplegar detecciones personalizadas como código exige una licencia que incluya Defender XDR, como E5, y el workspace incorporado al portal de Defender ([desplegar desde el repositorio](https://learn.microsoft.com/en-us/azure/sentinel/ci-cd)).

> **Consejo Ninja.** Evita el antipatrón «no inventado aquí»: configura lo que ya existe antes de personalizar y mide el costo de mantener contenido propio ([antipatrones](https://learn.microsoft.com/en-us/security/zero-trust/security-adoption-discipline-security-operations-common-issues)). Para afinar, los insights de ajuste analizan 14 días y sugieren entidades que excluir por su correlación con falsos positivos, en vista previa ([ajuste de detecciones](https://learn.microsoft.com/en-us/azure/sentinel/detection-tuning)).

> **Atención.** Contar reglas no es probar cobertura: la página MITRE de Sentinel (vista previa) solo considera reglas activas ([cobertura MITRE](https://learn.microsoft.com/en-us/azure/sentinel/mitre-coverage)). Mide la cobertura validada con emulación, como en [A5](03_Nivel_3_Avanzado.md#a5).

**¿Tienes poco tiempo?**

- [Custom detections overview](https://learn.microsoft.com/en-us/defender-xdr/custom-detections-overview) · Documentación
- [Manage content as code with Microsoft Sentinel repositories (incl. Deploy custom detection rules as code - Preview)](https://learn.microsoft.com/en-us/azure/sentinel/ci-cd-custom-content) · Documentación
- [Get fine-tuning recommendations for your analytics rules in Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/detection-tuning) · Documentación
- [View MITRE ATT&CK framework coverage in Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/mitre-coverage) · Documentación

### Documentación, cursos y credenciales

- [Custom detections overview](https://learn.microsoft.com/en-us/defender-xdr/custom-detections-overview) · Documentación · Oficial · Nuevo · Microsoft Learn · 6 jul 2026. Introduce las detecciones personalizadas basadas en consultas de búsqueda avanzada que generan alertas y acciones de respuesta automáticas, incluida su gestión como código (preview).
- [Manage content as code with Microsoft Sentinel repositories (incl. Deploy custom detection rules as code - Preview)](https://learn.microsoft.com/en-us/azure/sentinel/ci-cd-custom-content) · Documentación · Oficial · Microsoft Learn. Describe cómo desplegar contenido de Sentinel (reglas de análisis, automatización, detecciones personalizadas en preview, hunting, parsers, playbooks, workbooks) desde GitHub o Azure DevOps como fuente única de verdad (CI/CD).
- [View MITRE ATT&CK framework coverage in Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/mitre-coverage) · Documentación · Oficial · Vista previa · Microsoft Learn. Explica la matriz de cobertura MITRE ATT&CK de Sentinel en el portal Defender (detecciones activas, simuladas y por escenario de amenaza). *Nota:* Alineada a MITRE ATT&CK v18; página en preview
- [Manage custom detection rules in Microsoft Defender XDR](https://learn.microsoft.com/en-us/defender-xdr/custom-detection-manage) · Documentación · Oficial · Microsoft Learn. Cómo revisar estado de ejecución, alertas disparadas, acciones, correlación y clasificación (verdadero/falso) de cada regla, incluidas las reglas analíticas de Sentinel en el portal unificado.
- [Deploy Custom Content from your Repository (Deploy content as code from your repository)](https://learn.microsoft.com/en-us/azure/sentinel/ci-cd) · Documentación · Oficial · Microsoft Learn. Pasos para conectar repositorios; para detecciones personalizadas como código exige licencia que incluya Defender XDR (p. ej., M365 E5) y workspace incorporado al portal de Defender.
- [Get fine-tuning recommendations for your analytics rules in Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/detection-tuning) · Documentación · Oficial · Vista previa · Microsoft Learn. Insights de ajuste por regla (alertas por incidente, entidades a excluir correlacionadas con falsos positivos, entidades dominantes) y aviso de que las detecciones personalizadas son ahora la vía unificada para nuevas reglas. *Nota:* Detection tuning sigue en preview

**Manos a la obra**

1. `Laboratorio` Define el ciclo de vida de una detección —solicitud, triage, especificación, revisión por pares, prueba, despliegue como código, ajuste y retiro— con criterios de entrada y salida y un RACI. Evidencia: proceso documentado en el wiki del SOC.
2. `Laboratorio` Prioriza el backlog de detecciones por amenaza y por riesgo con un puntaje simple; por ejemplo, considera que la ejecución por el usuario y las cuentas válidas explican el 30 % y el 20 % del acceso inicial según el [MDDR 2026](https://www.microsoft.com/en-us/security/security-insider/threat-landscape/2026-digital-defense-report). Evidencia: backlog con puntaje y justificación.
3. `Laboratorio parcial` Implementa revisión por pares y despliegue como código con GitHub y Sentinel Repositories, con una lista de verificación de calidad en cada pull request ([desplegar desde el repositorio](https://learn.microsoft.com/en-us/azure/sentinel/ci-cd)). Limitación: funciones en vista previa y duración de la prueba. En producción, usa una rama de pruebas, un workspace secundario y revisión por pares. Evidencia: pull request con la lista completada.
4. `Laboratorio` Define los indicadores del programa: cobertura validada, falsos positivos por regla, tiempo desde la solicitud hasta producción y porcentaje de reglas con dueño y prueba. Evidencia: ficha de indicadores con su fuente.
5. `Laboratorio parcial` Usa los insights de ajuste de 14 días sobre una regla de análisis para proponer exclusiones ([ajuste de detecciones](https://learn.microsoft.com/en-us/azure/sentinel/detection-tuning)). Limitación: requiere falsos positivos reales para que las sugerencias sean útiles. Evidencia: propuesta de exclusión con su riesgo.
6. `Solo producción` Haz una revisión trimestral para retirar reglas sin valor. Requiere el historial real de alertas. Cómo hacerlo seguro: análisis de solo lectura, deshabilitar antes de borrar, control de cambios y reversión documentada.

<a id="s6"></a>

## S6 · Automatización e IA en el SOC con supervisión humana

*L300–L400 · ~6 h · Origen: Nuevo en esta edición (SAF, visión del SOC agéntico de Microsoft y ficha de IA responsable de los agentes)*

La filosofía del SOC de Microsoft desde 2019 es que la automatización no está para quitar humanos sino para empoderarlos. En 2026 Microsoft la formula como un **SOC agéntico en dos capas**: una capa de disrupción determinista, acotada por políticas —como la interrupción automática de ataques—, y una capa de agentes que razonan y coordinan investigaciones, mientras las personas conservan el juicio, el riesgo y las prioridades.

Este módulo diseña la gobernanza de esa combinación: qué se automatiza sin aprobación, qué requiere aprobación humana y qué nunca se delega; cómo se gestionan exclusiones, acciones pendientes y reversiones; cómo se identifica y limita a cada agente (identidad dedicada, permisos mínimos); y cómo se mide si la IA realmente mejora el SOC: precisión, tiempo ahorrado, acciones revertidas y consumo de SCU.

**Por qué importa**

La automatización y los agentes son la única forma de escalar un SOC sin escalar en la misma proporción el personal, y también la forma más rápida de cometer un error a escala. Una política explícita de supervisión humana permite aprovechar la velocidad con controles que un auditor, un regulador o un comité de riesgos pueden revisar.

**Qué vas a lograr**

- Clasificar las acciones de respuesta según el nivel de autonomía permitido.
- Gobernar exclusiones, acciones pendientes y reversiones de la automatización.
- Definir identidad, permisos, alcance y revisión de cada agente.
- Medir el valor y el riesgo de la automatización y de la IA.

> **Consejo Ninja.** Microsoft describe el SOC agéntico en dos capas: una interrupción determinista y acotada por políticas en la plataforma, y agentes que razonan y coordinan investigaciones, mientras las personas conservan el juicio y las prioridades ([el SOC agéntico](https://www.microsoft.com/en-us/security/blog/2026/04/09/the-agentic-soc-rethinking-secops-for-the-next-decade/)). La filosofía del SOC de Microsoft lo resume: la automatización no busca quitar personas, sino potenciarlas ([parte 2a](https://www.microsoft.com/en-us/security/blog/2019/04/23/lessons-learned-microsoft-soc-part-2-organizing-people/)).

> **Atención.** Gobierno de agentes: identidad de agente dedicada (Entra Agent ID) en lugar de credenciales de usuario, permisos acotados, acciones que requieren aprobación y consumo de SCU monitoreado ([ficha de IA responsable](https://learn.microsoft.com/en-us/copilot/security/security-copilot-application-card-agents), [conceptos de agentes](https://learn.microsoft.com/en-us/copilot/security/agents-overview)).

> **Atención.** Microsoft desaconseja excluir activos de la interrupción automática porque reduce su eficacia: documenta y revisa cada exclusión, como las cuentas de emergencia o los servidores críticos ([exclusiones](https://learn.microsoft.com/en-us/defender-xdr/automatic-attack-disruption-exclusions)). En MDE, las acciones pendientes de AIR vencen a los 7 días ([niveles de automatización](https://learn.microsoft.com/en-us/defender-endpoint/automation-levels)).

> **Novedad.** Datos publicados por Microsoft, para contrastar en tu inquilino: el Security Alert Triage Agent identificó 6,5 veces más alertas maliciosas con 77 % más de precisión de veredicto en evaluaciones controladas ([Ignite 2025](https://techcommunity.microsoft.com/blog/MicrosoftDefenderforOffice365Blog/microsoft-ignite-2025-transforming-phishing-response-with-agentic-innovation/4470791)), y un estudio propio sobre el Dynamic Threat Detection Agent reporta 80,1 % de precisión en 120 días ([arXiv](https://arxiv.org/abs/2605.20896)).

**¿Tienes poco tiempo?**

- [The agentic SOC—Rethinking SecOps for the next decade](https://www.microsoft.com/en-us/security/blog/2026/04/09/the-agentic-soc-rethinking-secops-for-the-next-decade/) · Blog oficial
- [Application card for Microsoft Security Copilot agents](https://learn.microsoft.com/en-us/copilot/security/security-copilot-application-card-agents) · Documentación
- [Overview of the Action center in Microsoft Defender XDR](https://learn.microsoft.com/en-us/defender-xdr/m365d-action-center) · Documentación
- [Exclude assets from automated response in attack disruption](https://learn.microsoft.com/en-us/defender-xdr/automatic-attack-disruption-exclusions) · Documentación

### Documentación, cursos y credenciales

- [Configure automatic attack disruption in Microsoft Defender XDR](https://learn.microsoft.com/en-us/defender-xdr/configure-attack-disruption) · Documentación · Oficial · Microsoft Learn. Requisitos de licencias (p. ej., M365 E5, E3 + Defender Suite, MDE P2, MDO P2), despliegue, permisos y versión mínima del sensor Sense (v10.8470) para la interrupción automática.
- [Application card for Microsoft Security Copilot agents](https://learn.microsoft.com/en-us/copilot/security/security-copilot-application-card-agents) · Documentación · Oficial · Microsoft Learn. Ficha de IA responsable de los agentes de Security Copilot: usos previstos, limitaciones, identidad y RBAC del agente, acciones acotadas que requieren aprobación y certificación ISO 42001.
- [Overview of the Action center in Microsoft Defender XDR](https://learn.microsoft.com/en-us/defender-xdr/m365d-action-center) · Documentación · Oficial · Microsoft Learn. El Action center unifica acciones pendientes (aprobar/rechazar) e historial auditable con opción de deshacer para dispositivos, correo e identidades.
- [MC1261596 - Notice: Security Copilot will be included as part of your Microsoft 365 E5 plan soon](https://mc.merill.net/message/MC1261596) · Documentación · Oficial · Microsoft (Message Center) · Microsoft 365 Message Center Archive (merill.net) · 25 mar 2026. Aviso del Message Center: Security Copilot se incluye en Microsoft 365 E5 con despliegue por fases del 20-abr al 30-jun-2026, 400 SCU por 1.000 usuarios y costos extra para capacidades fuera del núcleo.
- [Security Copilot agents in Microsoft 365 E5](https://www.microsoft.com/en-us/security/security-copilot-in-microsoft-365-e5) · Documentación · Oficial · Microsoft Security · nov 2025. Página oficial del beneficio: clientes elegibles de Microsoft 365 E5 reciben 400 SCU/mes por cada 1.000 licencias (máximo 10.000 SCU/mes) y agentes de Security Copilot en Defender, Entra, Intune y Purview sin costo adicional.
- [Microsoft Security Copilot Security Alert Triage Agent in Microsoft Defender (Preview)](https://learn.microsoft.com/en-us/defender-xdr/security-alert-triage-agent) · Documentación · Oficial · Vista previa · Microsoft Learn. Documenta el agente autónomo de triage (antes Phishing Triage Agent): GA para correos reportados por usuarios y preview para alertas de nube/contenedores e identidad, con razonamiento transparente y aprendizaje por feedback. *Nota:* Requiere SCU de Security Copilot, RBAC unificado activo y desactivar reglas de ajuste que auto-resuelvan las alertas a triar; el feedback solo aplica a alertas de correo
- [Exclude assets from automated response in attack disruption](https://learn.microsoft.com/en-us/defender-xdr/automatic-attack-disruption-exclusions) · Documentación · Oficial · Microsoft Learn. Cómo excluir usuarios, grupos de dispositivos e IP de las respuestas automáticas, con la advertencia de Microsoft de que excluir activos reduce la eficacia de la interrupción.
- [Microsoft Security Copilot agents overview](https://learn.microsoft.com/en-us/copilot/security/agents-overview) · Documentación · Oficial · Microsoft Learn · 18 mar 2026. Conceptos de agentes (trigger, permisos, identidad con Entra Agent ID o cuenta de usuario, plugins); los agentes consumen SCU y aprenden con feedback manteniendo el control humano.

### Anuncios y blogs oficiales

- [Reimagining the SOC for the agentic era in Microsoft Defender](https://www.microsoft.com/en-us/security/blog/2026/09/23/reimagining-the-soc-for-the-agentic-era-in-microsoft-defender/) · Blog oficial · Empleado de Microsoft · Nuevo · Rob Lefferts · Microsoft Security Blog · 23 sep 2026. Visión de Microsoft del SOC agéntico: ISOC como base de señales, contexto y actuadores, con el bucle de protección integrado ejemplificado por attack disruption.
- [The agentic SOC—Rethinking SecOps for the next decade](https://www.microsoft.com/en-us/security/blog/2026/04/09/the-agentic-soc-rethinking-secops-for-the-next-decade/) · Blog oficial · Empleado de Microsoft · Rob Lefferts, David Weston · Microsoft Security Blog · 9 abr 2026. Define el SOC agéntico en dos capas: disrupción determinista y acotada por políticas en la plataforma, y agentes que razonan y coordinan investigaciones mientras los analistas se enfocan en juicio y riesgo.
- [Microsoft Ignite 2025: Transforming Phishing Response with Agentic Innovation](https://techcommunity.microsoft.com/blog/MicrosoftDefenderforOffice365Blog/microsoft-ignite-2025-transforming-phishing-response-with-agentic-innovation/4470791) · Blog oficial · Empleado de Microsoft · Jeffrey Pinkston · Microsoft Tech Community · 18 nov 2025. Anuncia la GA del Security Alert Triage Agent (antes Phishing Triage Agent) con resultados reportados de 6,5x más alertas maliciosas identificadas y +77% de precisión de veredictos.
- [Microsoft named an overall leader in KuppingerCole Analyst's 2026 Emerging AI Security Operations Center (SOC) report](https://www.microsoft.com/en-us/security/blog/2026/05/06/microsoft-named-an-overall-leader-in-kuppingercole-analysts-2026-emerging-ai-security-operations-center-soc-report/) · Blog oficial · Empleado de Microsoft · Nuevo · Rob Lefferts · Microsoft Security Blog · 6 may 2026. Resume capacidades de automatización e IA del SOC (interrupción automática, agente de triage, priorización de incidentes 0-100, generador de playbooks, Sentinel MCP) con acción bajo supervisión humana al superar umbrales de confianza.

**Manos a la obra**

1. `Laboratorio` Clasifica las acciones de respuesta de tu SOC por nivel de autonomía: automática (interrupción), automática con aviso, con aprobación y nunca automatizada. Evidencia: matriz de autonomía aprobada por el líder del SOC.
2. `Laboratorio parcial` Configura grupos de dispositivos con automatización completa y semiautomática y practica aprobar, rechazar y deshacer en el [Action center](https://learn.microsoft.com/en-us/defender-xdr/m365d-action-center). Limitación: desde el 1 de septiembre de 2026 el AIR de MDE ya no se dispara manualmente. En producción, usa un grupo piloto y revisa a diario las acciones pendientes, que vencen a los 7 días. Evidencia: historial con las tres decisiones.
3. `Laboratorio` Crea el registro de exclusiones de la interrupción automática: activo, motivo, dueño, fecha de revisión y riesgo aceptado ([exclusiones](https://learn.microsoft.com/en-us/defender-xdr/automatic-attack-disruption-exclusions)). Evidencia: registro con su primera revisión.
4. `Laboratorio` Escribe la ficha de gobierno de cada agente que uses: identidad, permisos, alcance, aprobaciones, botón de apagado, métricas y dueño ([ficha de IA responsable](https://learn.microsoft.com/en-us/copilot/security/security-copilot-application-card-agents)). Evidencia: fichas aprobadas.
5. `Solo producción` Mide la concordancia entre los veredictos del Security Alert Triage Agent y los de tus analistas en una muestra de correos reportados. Requiere volumen real y SCU pagas. Cómo hacerlo seguro: grupo piloto, doble revisión, ningún cierre automático hasta alcanzar el umbral de concordancia acordado y excedente limitado.
6. `Solo producción` Valida la interrupción automática ante un incidente real. Requiere señales reales de alta confianza. Cómo hacerlo seguro: exclusiones mínimas documentadas, revisión con roles de solo lectura y un ejercicio de mesa sobre la contención de un usuario VIP ([configurar la interrupción](https://learn.microsoft.com/en-us/defender-xdr/configure-attack-disruption)).

<a id="s7"></a>

## S7 · Gobierno, riesgo y reporte ejecutivo del SOC

*L300–L400 · ~4 h · Origen: Nuevo en esta edición (SAF: estrategia, integración y gobierno; CISO Workshop; MDDR 2026)*

El SOC existe para reducir el riesgo del negocio, y eso hay que poder explicarlo en una página. La disciplina de **estrategia, integración y gobierno** del SAF define prioridades, métricas y criterios de éxito del SOC; el **CISO Workshop** dedica un módulo a las métricas críticas y a los puntos de contacto con los líderes del negocio; y el SOC de Microsoft describe cuatro puntos de integración con el negocio, entre ellos el contexto de negocio hacia el SOC, los ejercicios conjuntos y las actualizaciones de incidentes mayores.

El **Microsoft Digital Defense Report 2026** (1 de octubre) da el contexto: la mediana entre el descubrimiento de una vulnerabilidad y su explotación baja de 24 horas mientras las empresas tardan de 30 a 60 días en remediar, y la ejecución por parte de usuarios y las cuentas válidas explican buena parte del acceso inicial en los casos de Defender Experts. Este módulo te enseña a construir el reporte ejecutivo con métricas de resultado, la decisión de tercerizar y el gobierno de la IA.

**Por qué importa**

Un SOC que no se explica no se financia. Reportar exposición reducida, cobertura validada y tiempo de mitigación —en lugar de alertas procesadas— alinea al SOC con el apetito de riesgo de la organización y convierte el presupuesto de seguridad en una decisión de negocio informada.

**Qué vas a lograr**

- Definir con la dirección la misión, las prioridades y las métricas de éxito del SOC.
- Redactar un reporte ejecutivo de una página con métricas de resultado.
- Fundamentar la decisión de tercerizar (MDR) con criterios de riesgo, costo y talento.
- Integrar el gobierno de la IA y de la automatización en el reporte de riesgo.

> **Novedad.** El MDDR 2026 (1 de octubre de 2026) aporta contexto para la dirección: la mediana entre el descubrimiento y la explotación de una vulnerabilidad baja de 24 horas, mientras la remediación empresarial tarda entre 30 y 60 días; además, en los casos de Defender Experts, la ejecución por parte del usuario explica el 30 % del acceso inicial y las cuentas válidas, el 20 % ([MDDR 2026](https://www.microsoft.com/en-us/security/security-insider/threat-landscape/2026-digital-defense-report), [resumen ejecutivo](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/msc/documents/presentations/CSR/2026-Microsoft-DDR-Exec-Summary.pdf)).

> **Consejo Ninja.** La disciplina de estrategia, integración y gobierno del SAF define las prioridades, las métricas y los criterios de éxito del SOC ([disciplina SecOps](https://learn.microsoft.com/en-us/security/zero-trust/security-adoption-discipline-security-operations)), y el módulo de operaciones de seguridad del CISO Workshop trata las métricas críticas y los puntos de contacto con el negocio ([CISO Workshop](https://learn.microsoft.com/en-us/security/adoption/the-ciso-workshop)).

> **Consejo Ninja.** El SOC de Microsoft define puntos de integración con el negocio: el contexto del negocio hacia el SOC, los ejercicios conjuntos de respuesta con los líderes y las actualizaciones de incidentes mayores hacia la dirección ([parte 1](https://www.microsoft.com/en-us/security/blog/2019/02/21/lessons-learned-from-the-microsoft-soc-part-1-organization/)). Las iniciativas de Exposure Management dan una tendencia objetiva para reportar la reducción de exposición ([iniciativas](https://learn.microsoft.com/en-us/security-exposure-management/initiatives)).

> **Atención.** Para decidir sobre la tercerización: Defender Experts MDR Plan 1 cubre las cargas de Defender y el Plan 2 suma fuentes de terceros vía Sentinel; Hunting, Servers, Threat Intelligence e Incident Response se contratan por separado ([Defender Experts](https://learn.microsoft.com/en-us/defender-xdr/defender-experts/defender-experts-overview)). Compara con tu costo de cobertura 24×7, tu riesgo y tu talento disponible, y valida los precios con tu equipo de cuenta.

**¿Tienes poco tiempo?**

- [2026 Digital Defense Report | Security Insider](https://www.microsoft.com/en-us/security/security-insider/threat-landscape/2026-digital-defense-report) · Blog oficial
- [The Chief Information Security Officer (CISO) Workshop](https://learn.microsoft.com/en-us/security/adoption/the-ciso-workshop) · Video
- [Review security initiatives in Microsoft Security Exposure Management](https://learn.microsoft.com/en-us/security-exposure-management/initiatives) · Documentación
- [Microsoft Security Adoption Framework (SAF)](https://learn.microsoft.com/en-us/security/zero-trust/security-adoption-model) · Documentación

### Documentación, cursos y credenciales

- [Microsoft Security Adoption Framework (SAF)](https://learn.microsoft.com/en-us/security/zero-trust/security-adoption-model) · Documentación · Oficial · Microsoft Learn. Presenta el modelo estructurado de adopción de seguridad (escenarios de negocio, disciplinas de seguridad y pilares tecnológicos) para conectar prioridades del negocio con operaciones medibles.
- [Overview - Security disciplines](https://learn.microsoft.com/en-us/security/zero-trust/security-adoption-discipline-overview) · Documentación · Oficial · Microsoft Learn. Explica las disciplinas SAF (planificación y supervisión, estrategia técnica, operacionales) y cómo la disciplina de Estrategia, Integración y Gobierno define prioridades y métricas de éxito.
- [Review security initiatives in Microsoft Security Exposure Management](https://learn.microsoft.com/en-us/security-exposure-management/initiatives) · Documentación · Oficial · Microsoft Learn. Iniciativas de seguridad con puntaje, objetivo configurable, tendencia de 14 días, historial y métricas: base para un reporte ejecutivo orientado a exposición reducida.
- [Exposure insights overview in Microsoft Security Exposure Management](https://learn.microsoft.com/en-us/security-exposure-management/exposure-insights-overview) · Documentación · Oficial · Microsoft Learn. Explica iniciativas (por carga, amenaza horizontal como ransomware/BEC, threat analytics, Zero Trust, EASM), métricas y eventos para que CISOs y dueños de riesgo prioricen inversión.

### Anuncios y blogs oficiales

- [2026 Digital Defense Report | Security Insider](https://www.microsoft.com/en-us/security/security-insider/threat-landscape/2026-digital-defense-report) · Blog oficial · Empleado de Microsoft · Nuevo · Tanmay Ganacharya, Wes Malaby · Microsoft Security Insider · 1 oct 2026. Resumen del MDDR 2026: la IA cambia la 'física' de la ciberseguridad; la mediana entre descubrimiento y weaponización de vulnerabilidades baja de 24 h mientras la remediación empresarial tarda 30-60 días; ejecución por usuario 30% y cuentas válidas 20% del acceso inicial (datos Defender Experts).
- [Insights from the 2026 Microsoft Digital Defense Report](https://www.microsoft.com/en-us/security/blog/2026/10/01/insights-from-the-2026-microsoft-digital-defense-report/) · Blog oficial · Empleado de Microsoft · Nuevo · Terrell Cox · Microsoft Security Blog · 1 oct 2026. Lectura del Deputy CISO de Microsoft sobre el MDDR 2026: IA en el panorama de amenazas, agentes como parte del sistema empresarial y valor de conectar señales entre dominios.

### Webinars, videos y podcasts

- [The Chief Information Security Officer (CISO) Workshop](https://learn.microsoft.com/en-us/security/adoption/the-ciso-workshop) · Video · Oficial · Microsoft Learn. Videos (~4 h) y diapositivas del CISO Workshop; su módulo Security Operations trata métricas críticas de éxito, puntos de contacto con líderes del negocio y cultura del SOC.

### Comunidad: blogs, libros, newsletters y eventos

- [Digital Defense Report 2026 Executive Summary (PDF)](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/msc/documents/presentations/CSR/2026-Microsoft-DDR-Exec-Summary.pdf) · Libro · Oficial · Nuevo · Microsoft Threat Intelligence · Microsoft · oct 2026. Resumen ejecutivo del MDDR 2026: la resiliencia es disciplina de liderazgo, los defensores deberán confiar autonomía creciente a agentes y la correlación de señales es la variable estratégica clave.
- [Microsoft Digital Defense Report 2025 (PDF)](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/security/Microsoft-Digital-Defense-Report-2025.pdf) · Libro · Oficial · Microsoft Threat Intelligence · Microsoft. Informe anual completo con panorama de amenazas, 10 recomendaciones principales, casos como un ransomware detenido en menos de dos minutos y capítulos de defensa con IA.

**Manos a la obra**

1. `Laboratorio` Redacta un reporte ejecutivo de una página con datos simulados, basado en exposición reducida, cobertura validada y tiempo de mitigación, no en tickets cerrados ([MDDR](https://www.microsoft.com/en-us/corporate-responsibility/topics/cybersecurity/reports/microsoft-digital-defense-report/)). Evidencia: reporte revisado por alguien ajeno a seguridad.
2. `Laboratorio` Escribe la carta del SOC: misión, alcance, prioridades, métricas de éxito y decisiones que requieren a la dirección, con la [disciplina SecOps del SAF](https://learn.microsoft.com/en-us/security/zero-trust/security-adoption-discipline-security-operations) como guía. Evidencia: carta de una página.
3. `Laboratorio` Prepara el memorando de decisión sobre tercerización: riesgo, costo, talento, horas de cobertura, fuentes de datos (Plan 1 o Plan 2), RACI y SLA ([Defender Experts](https://learn.microsoft.com/en-us/defender-xdr/defender-experts/defender-experts-overview)). Evidencia: memorando con una recomendación.
4. `Laboratorio` Integra la IA y la automatización en el registro de riesgos: acciones autónomas erróneas, exceso de consumo de SCU, exposición de datos y dependencia de un proveedor, cada una con controles y dueño. Evidencia: entradas del registro de riesgos.
5. `Laboratorio` Arma la vista de exposición para la dirección con una iniciativa de Exposure Management y su tendencia de 14 días ([iniciativas](https://learn.microsoft.com/en-us/security-exposure-management/initiatives)). Evidencia: captura y una narrativa de tres líneas.
6. `Solo producción` Presenta el reporte al comité de riesgos con datos reales. Requiere métricas de producción y la agenda del comité. Cómo hacerlo seguro: valida las cifras con sus dueños, sin métricas individuales, con definiciones y limitaciones explícitas y con una sola decisión clara que pedir.

**¿Quieres profundizar?**

- [Digital Defense Report 2026 Executive Summary (PDF)](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/msc/documents/presentations/CSR/2026-Microsoft-DDR-Exec-Summary.pdf) · Libro
- [Microsoft Digital Defense Report 2025 (PDF)](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/security/Microsoft-Digital-Defense-Report-2025.pdf) · Libro

<a id="reto-excelencia"></a>

## Reto del nivel

**Plan de excelencia a 12 meses ante el comité.** Presenta a un comité simulado el modelo operativo (roles y RACI), el proceso de incidentes mayores, el diccionario de métricas con su línea base, la autoevaluación de madurez con metas por dominio, la política de autonomía para la automatización y los agentes, y la decisión sobre tercerización. Formato: diez minutos de exposición y un reporte ejecutivo de una página con métricas de resultado —exposición, cobertura validada y tiempo de mitigación—, no de actividad.

<a id="quiz-excelencia"></a>

## Evaluación del nivel

Responde y compara con [Evaluaciones y respuestas](06_Evaluaciones_y_respuestas.md#eval-excelencia). Con 80 % o más, ¡nivel aprobado! (En la versión web puedes corregir en línea y generar tu certificado).

1. ¿Qué taller del Security Adoption Framework cubre el burnout, la estrategia XDR + SIEM + data lake, la tercerización y la planificación del SOC?
   - a) El CISO Workshop
   - b) El resumen de la MCRA
   - c) Security ADS Module 3 · Modern Security Operations
   - d) El taller de identidades y acceso

2. Según el taller de SecOps del SAF, el modelo de roles del SOC se basa en…
   - a) especialización, no jerarquía
   - b) una jerarquía estricta por antigüedad
   - c) la rotación aleatoria de funciones
   - d) la tercerización total

3. En el SAF, ¿cuándo termina el MTTA?
   - a) Al cerrar el incidente
   - b) Al contener la amenaza
   - c) Al crearse la alerta
   - d) Cuando un analista toma el incidente

4. Ante un adversario atrincherado, ¿qué riesgo tiene una remediación parcial?
   - a) Ninguno, si se hace rápido
   - b) Alerta al atacante, que puede cambiar de táctica o de acceso
   - c) Solo aumenta el costo de licencias
   - d) Obliga a reinstalar Defender

5. ¿Cómo calcula el workbook de Sentinel el «time to triage»?
   - a) ClosedTime − CreatedTime
   - b) FirstModifiedTime − CreatedTime
   - c) LastActivityTime − FirstActivityTime
   - d) CreatedTime − FirstActivityTime

6. ¿Por qué hay que deduplicar SecurityIncident por IncidentNumber antes de calcular métricas?
   - a) Porque cada actualización de un incidente crea una fila nueva
   - b) Porque la tabla mezcla alertas e incidentes
   - c) Porque los incidentes se borran a los 30 días
   - d) Porque IncidentNumber cambia al cerrar

7. En SOC optimization, una cobertura «media» frente a una amenaza significa que tienes activas…
   - a) más del 75 % de las reglas recomendadas
   - b) entre el 0 y el 29 %
   - c) exactamente la mitad
   - d) entre el 30 y el 74 % de las reglas recomendadas

8. ¿En qué escala mide SOC-CMM la madurez?
   - a) De 1 a 3
   - b) De 0 a 5
   - c) De la A a la F
   - d) Sí o no por control

9. Según el informe SOC-CMM de 2025, ¿qué frena el crecimiento de la madurez?
   - a) La falta de herramientas de IA
   - b) El uso de marcos públicos
   - c) La sobreestimación en las autoevaluaciones
   - d) El trabajo remoto

10. ¿Qué exige desplegar detecciones personalizadas como código mediante Sentinel Repositories?
   - a) Solo Sentinel en el portal de Azure
   - b) Una licencia que incluya Defender XDR (por ejemplo, E5) y el workspace incorporado al portal de Defender
   - c) Un contrato de Defender Experts
   - d) Nada adicional

11. ¿Por qué la página MITRE ATT&CK de Sentinel no basta para afirmar que tienes cobertura?
   - a) Porque solo muestra técnicas de Windows
   - b) Porque se actualiza una vez al año
   - c) Porque requiere Defender Experts
   - d) Porque solo considera reglas activas: contar reglas no prueba que detecten; hay que validar con emulación

12. ¿Qué recomienda Microsoft sobre excluir activos de la interrupción automática de ataques?
   - a) La desaconseja porque reduce la eficacia; cada exclusión debe justificarse
   - b) Excluir todos los servidores críticos por defecto
   - c) Excluir a todos los ejecutivos
   - d) No es posible excluir activos

13. En el modelo de SOC agéntico que Microsoft describió en abril de 2026, ¿qué conservan las personas?
   - a) Solo la aprobación de licencias
   - b) Nada: los agentes deciden todo
   - c) El juicio y las prioridades, mientras la plataforma interrumpe y los agentes razonan
   - d) Solo el triage de nivel 1

14. Según el MDDR 2026, ¿cuál es la mediana entre el descubrimiento de una vulnerabilidad y su explotación?
   - a) 7 días
   - b) Entre 30 y 60 días
   - c) Menos de 24 horas
   - d) 90 días

15. ¿Qué recomienda el MDDR 2026 reportar a la dirección?
   - a) Parches desplegados
   - b) Tickets cerrados por analista
   - c) Alertas totales recibidas
   - d) Exposición reducida, cobertura de detección y tiempo de mitigación

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

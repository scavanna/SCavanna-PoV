# Nivel 3 · Avanzado · Respuesta, automatización e ingeniería

*Microsoft Defender XDR Ninja Training · Edición 2026*

[← Nivel 2 · Intermedio](02_Nivel_2_Intermedio.md) · [Índice del programa](README.md) · [Nivel 4 · Excelencia del SOC →](04_Nivel_4_Excelencia_del_SOC.md)

<a id="avanzado"></a>

Playbooks de respuesta, automatización con Sentinel y Logic Apps, hunting con inteligencia, APIs, ingeniería de detecciones y purple teaming, Security Copilot y agentes, y operación multi-inquilino. Cierra con un proyecto integrador de un phishing a la contención de identidad y endpoint.

*L400 · 8 módulos · ~74 horas · 77 recursos*

**Módulos de este nivel:** [A1 Playbooks de respuesta](#a1) · [A2 Automatización y Logic Apps](#a2) · [A3 Hunting e inteligencia](#a3) · [A4 APIs](#a4) · [A5 Ingeniería y purple team](#a5) · [A6 Security Copilot y agentes](#a6) · [A7 Multi-inquilino y MDR](#a7) · [A8 Proyecto integrador](#a8)

<a id="a1"></a>

## A1 · Playbooks de respuesta a incidentes

*L400 · ~10 h · Origen: Ninja oficial de Defender XDR, Expert (incidentes) e Incident Response Ninja Hub*

Un playbook de respuesta convierte la experiencia de los mejores respondedores en un procedimiento repetible: prerrequisitos (qué registros deben existir antes del incidente), flujo de decisión, lista de verificación y pasos de investigación, contención, erradicación y recuperación. Microsoft Incident Response publica playbooks de **phishing**, **password spray**, **concesión ilícita de consentimiento**, **aplicaciones comprometidas** y **robo de tokens**, además de guías para **ransomware** y **buzón comprometido (BEC)**.

En 2026 los de phishing, password spray y consentimiento pasaron a la disciplina de operaciones de seguridad del **Security Adoption Framework**: el de phishing se reescribió el 31 de mayo como guía neutral con Defender XDR y Sentinel como implementación de referencia, y los de password spray y consentimiento se actualizaron el 3 de noviembre con flujos descargables. Este módulo los adapta a tu organización, los alinea con **NIST SP 800-61 Rev. 3** y los prueba con ejercicios de mesa. El resumen está en [Playbooks de respuesta a incidentes](00_Programa.md#playbooks-ir).

**Por qué importa**

En un incidente mayor no hay tiempo para improvisar: los equipos con playbooks probados contienen más rápido, cometen menos errores irreversibles —como borrar evidencia o alertar al atacante con una remediación parcial— y coordinan mejor con legal, comunicaciones y negocio. Además, un playbook documentado es el insumo directo para automatizar en [A2](#a2).

**Qué vas a lograr**

- Adaptar los playbooks oficiales a tu entorno con roles, herramientas y criterios de escalamiento.
- Ejecutar la contención por producto en el orden correcto para cada escenario.
- Alinear el proceso de respuesta con NIST SP 800-61 Rev. 3 y el CSF 2.0.
- Diseñar y conducir un ejercicio de mesa con informe posterior.
- Redactar un procedimiento operativo (SOP) para identidad comprometida.

> **Qué cambió.** En 2026, los playbooks de phishing, password spray y consentimiento de aplicaciones pasaron a la disciplina SecOps del Security Adoption Framework (Zero Trust). El de phishing se reescribió el 31 de mayo de 2026 como guía neutral con Defender XDR y Sentinel como implementación de referencia ([phishing](https://learn.microsoft.com/en-us/security/zero-trust/security-operations-playbook-phishing)), y los de password spray y consentimiento se actualizaron el 3 de noviembre de 2026 con flujos descargables en PDF y Visio y listas de verificación en Excel ([password spray](https://learn.microsoft.com/en-us/security/zero-trust/security-operations-playbook-password-spray)). El índice de 2024 todavía no lo refleja ([índice](https://learn.microsoft.com/en-us/security/operations/incident-response-playbooks)).

> **Novedad.** NIST SP 800-61 Rev. 3 (3 de abril de 2025) es un perfil comunitario del CSF 2.0 y reemplaza a la Rev. 2 de 2012: la preparación se apoya en Gobernar, Identificar y Proteger; la detección y el análisis, en Detectar; la contención y la erradicación, en Responder, y la recuperación y las lecciones aprendidas, en Recuperar y la mejora continua ([SP 800-61r3](https://csrc.nist.gov/pubs/sp/800/61/r3/final)).

> **Consejo Ninja.** El [playbook de robo de tokens](https://learn.microsoft.com/en-us/security/operations/token-theft-playbook), que incluye AiTM y se actualizó en marzo de 2024, sigue siendo la guía oficial. El caso de AiTM y BEC que Microsoft publicó en enero de 2026 lo confirma: contener exige revocar las cookies de sesión y eliminar las reglas de buzón, no solo cambiar la contraseña ([caso de 2026](https://www.microsoft.com/en-us/security/blog/2026/01/21/multistage-aitm-phishing-bec-campaign-abusing-sharepoint/)).

> **Consejo Ninja.** Para ensayar sin tocar sistemas, CISA ofrece más de 100 paquetes de ejercicios de mesa (CTEP) con plantillas de planificación y de informe posterior alineadas a HSEEP ([CTEP](https://www.cisa.gov/resources-tools/services/cisa-tabletop-exercise-packages)); para documentar, Microsoft publica una plantilla de procedimiento operativo para identidad comprometida ([plantilla SOP](https://learn.microsoft.com/en-us/defender-xdr/sop-documentation-template)). La tabla [Playbooks de respuesta a incidentes](00_Programa.md#playbooks-ir) resume la contención por producto.

**¿Tienes poco tiempo?**

- [Phishing investigation playbook](https://learn.microsoft.com/en-us/security/zero-trust/security-operations-playbook-phishing) · Documentación
- [Password spray investigation](https://learn.microsoft.com/en-us/security/zero-trust/security-operations-playbook-password-spray) · Documentación
- [Token theft playbook](https://learn.microsoft.com/en-us/security/operations/token-theft-playbook) · Documentación
- [SP 800-61 Rev. 3, Incident Response Recommendations and Considerations for Cybersecurity Risk Management: A CSF 2.0 Community Profile](https://csrc.nist.gov/pubs/sp/800/61/r3/final) · Documentación

### Documentación, cursos y credenciales

- [Password spray investigation](https://learn.microsoft.com/en-us/security/zero-trust/security-operations-playbook-password-spray) · Documentación · Oficial · Nuevo · Microsoft Learn · 3 nov 2026. Guía para detectar e investigar ataques de password spray (ADFS, Entra ID, Identity Protection, Defender for Cloud Apps) con disparadores, checklist, consultas, mitigaciones y recuperación.
- [App consent grant investigation](https://learn.microsoft.com/en-us/security/zero-trust/security-operations-playbook-app-consent) · Documentación · Oficial · Nuevo · Microsoft Learn · 3 nov 2026. Playbook para investigar concesiones ilícitas de consentimiento OAuth: permisos de riesgo, inventario de apps con Graph PowerShell, señales de ataque en auditoría, deshabilitación de la app y defensas (flujo de consentimiento de administrador, step-up basado en riesgo).
- [Phishing investigation playbook](https://learn.microsoft.com/en-us/security/zero-trust/security-operations-playbook-phishing) · Documentación · Oficial · Nuevo · Microsoft Learn · 31 may 2026. Playbook reescrito de investigación de phishing: prerrequisitos (auditoría de buzones, message trace, UAL, logs de Entra), flujo en cinco etapas, checklist y pasos de contención y recuperación.
- [Responding to ransomware attacks (Microsoft Defender XDR)](https://learn.microsoft.com/en-us/defender-xdr/playbook-responding-ransomware-m365-defender) · Documentación · Oficial · Microsoft Learn. Playbook genérico de respuesta a ransomware con Defender XDR: alcance del incidente, preservación de sistemas, prevención de propagación con KQL, erradicación y recuperación.
- [Respond to a compromised cloud email account (Business Email Compromise)](https://learn.microsoft.com/en-us/defender-office-365/responding-to-a-compromised-email-account) · Documentación · Oficial · Microsoft Learn. Síntomas de cuentas de correo comprometidas (BEC) y pasos para recuperar el control: deshabilitar usuario, restablecer contraseña, eliminar reglas y reenvíos sospechosos e investigar.
- [SP 800-61 Rev. 3, Incident Response Recommendations and Considerations for Cybersecurity Risk Management: A CSF 2.0 Community Profile](https://csrc.nist.gov/pubs/sp/800/61/r3/final) · Documentación · Comunidad · Alexander Nelson, Sanjay Rekhi, Murugiah Souppaya, Karen Scarfone · NIST CSRC · abr 2025. Guía de NIST que integra la respuesta a incidentes en la gestión de riesgos como perfil comunitario del CSF 2.0 (Govern, Identify, Protect, Detect, Respond, Recover) y sustituye a la Rev. 2 de 2012.
- [Compromised and malicious applications investigation](https://learn.microsoft.com/en-us/security/operations/incident-response-playbook-compromised-malicious-app) · Documentación · Oficial · Microsoft Learn · 12 mar 2025. Playbook oficial para investigar y contener aplicaciones comprometidas o maliciosas en Entra ID, usando riesgo de workload identities y gobernanza de apps.
- [Incident response playbooks](https://learn.microsoft.com/en-us/security/operations/incident-response-playbooks) · Documentación · Oficial · Legado aún útil · Microsoft Incident Response · Microsoft Learn · 24 oct 2024. Índice oficial de los playbooks de respuesta a incidentes de Microsoft Incident Response (phishing, password spray, consentimiento de apps, apps comprometidas y maliciosas) con prerrequisitos, flujo, checklist y pasos de investigación. *Nota:* Página índice sin actualizar desde 2024; varios playbooks se movieron a la sección Zero Trust / Security Adoption Framework (SecOps) en 2026
- [Token theft playbook](https://learn.microsoft.com/en-us/security/operations/token-theft-playbook) · Documentación · Oficial · Legado aún útil · Microsoft Learn · 7 mar 2024. Playbook y árbol de decisión para investigar robo y reproducción de tokens (incl. AiTM): disparadores de Entra ID Protection y MDE, consultas KQL, contención y recuperación. *Nota:* Última actualización 2024; complementar con Token Protection de Acceso Condicional y la interrupción automática de ataques AiTM
- [Password spray investigation](https://learn.microsoft.com/en-us/security/operations/incident-response-playbook-password-spray) · Documentación · Oficial · Microsoft Learn. Playbook oficial de respuesta a incidentes para identificar, investigar y remediar ataques de password spray (prerrequisitos de registro, flujo, checklist, recuperación).
- [Token theft playbook](https://learn.microsoft.com/en-us/security/zero-trust/security-operations-playbook-token-theft) · Documentación · Oficial · Microsoft Learn. Playbook oficial con árbol de decisión para investigar, contener y recuperarse de robo y repetición de tokens de Entra ID.
- [Create a compromised identity incident response SOP template](https://learn.microsoft.com/en-us/defender-xdr/sop-documentation-template) · Documentación · Oficial · Microsoft Learn. Plantilla oficial de procedimiento operativo para incidentes de identidad comprometida (triaje, contención, investigación, remediación y prevención) con consultas KQL de ejemplo sobre SigninLogs.
- [Microsoft Incident Response ransomware approach and best practices](https://learn.microsoft.com/en-us/security/ransomware/incident-response-playbook-dart-ransomware-approach) · Documentación · Oficial · Microsoft Incident Response (antes DART/CRSP) · Microsoft Learn. Describe cómo el equipo Microsoft Incident Response investiga ransomware operado por humanos con Defender for Endpoint, Identity, Office 365 y Cloud Apps, y sus recomendaciones.

### Laboratorios, GitHub y herramientas

- [CISA Tabletop Exercise Packages](https://www.cisa.gov/resources-tools/services/cisa-tabletop-exercise-packages) · Herramienta · Comunidad · CISA Exercises · CISA. Colección de más de 100 paquetes de ejercicios de mesa personalizables (objetivos, escenarios, preguntas y plantillas de informe post-acción) con escenarios de ransomware, phishing y amenaza interna.
- [Cybersecurity Scenarios (CISA CTEP situation manuals)](https://www.cisa.gov/resources-tools/resources/cybersecurity-scenarios) · Herramienta · Comunidad · CISA Exercises · CISA · 15 ago 2023. Manuales de situación descargables para ejercicios de mesa de ciberseguridad por sector y vector (ransomware, insider, cadena de suministro, ejecutivos).

**Manos a la obra**

1. `Laboratorio` Adapta el [playbook oficial de phishing](https://learn.microsoft.com/en-us/security/zero-trust/security-operations-playbook-phishing) a tu organización: asigna cada paso a un rol, a una herramienta (MDO, Entra ID, MDE) y a un criterio de escalamiento, con apoyo de la tabla [Playbooks de respuesta a incidentes](00_Programa.md#playbooks-ir). Evidencia: playbook adaptado con su RACI.
2. `Laboratorio` Redacta el procedimiento operativo para identidad comprometida con la [plantilla oficial](https://learn.microsoft.com/en-us/defender-xdr/sop-documentation-template). Evidencia: SOP revisado por el responsable de identidad.
3. `Laboratorio` Recorre la lista de verificación del [playbook de password spray](https://learn.microsoft.com/en-us/security/zero-trust/security-operations-playbook-password-spray) y comprueba en tu inquilino de prueba cada prerrequisito de registro y de detección (registros de inicio de sesión, auditoría y alertas de ID Protection). Evidencia: lista con brechas y su plan de cierre.
4. `Laboratorio` Registra una aplicación de prueba multiinquilino que pida permisos mínimos, dale consentimiento como usuario de prueba, investígala con el evento «Consent to application» de la auditoría y deshabilítala sin borrarla, como indica el [playbook de consentimiento](https://learn.microsoft.com/en-us/security/zero-trust/security-operations-playbook-app-consent). Evidencia: línea de tiempo y estado final de la aplicación.
5. `Laboratorio` Simula en un ejercicio de mesa la contención de ransomware del [playbook de Defender XDR](https://learn.microsoft.com/en-us/defender-xdr/playbook-responding-ransomware-m365-defender): aislar sin apagar, cuarentena e indicadores, suspensión de cuentas privilegiadas y desconexión de las copias de seguridad en línea. Evidencia: registro de decisiones con hora y responsable.
6. `Laboratorio` Mapea tu proceso de respuesta a las funciones del CSF 2.0 según [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final). Evidencia: matriz proceso-función con las brechas marcadas.
7. `Solo producción` Conduce un ejercicio de mesa ejecutivo de ransomware con un paquete [CTEP de CISA](https://www.cisa.gov/resources-tools/services/cisa-tabletop-exercise-packages) y mide el MTTR real de tu SOC. Requiere participantes reales (Legal, Comunicaciones y Dirección) y datos operativos. Cómo hacerlo seguro: ejercicio solo de discusión, sin tocar sistemas, con informe posterior y plan de mejora.

**¿Quieres profundizar?**

- [CISA Tabletop Exercise Packages](https://www.cisa.gov/resources-tools/services/cisa-tabletop-exercise-packages) · Herramienta

<a id="a2"></a>

## A2 · Automatización de respuesta con Sentinel y Logic Apps

*L400 · ~10 h · Origen: Ninja oficial de Defender XDR, Intermediate (AIR) y Expert (integración), ampliado a SOAR*

Cuando la respuesta nativa no alcanza —hay que avisar a un dueño de negocio, abrir un ticket, pedir una aprobación o actuar en un sistema de terceros— entra la orquestación. En el portal de Defender, las **reglas de automatización** de Sentinel asignan, etiquetan y cierran incidentes y ejecutan **playbooks de Azure Logic Apps** con conectores de Defender for Endpoint, Entra ID, Teams o tu ITSM. Para alertas de XDR se usa el **Enhanced Alert Trigger**: el disparador de alerta clásico solo actúa sobre alertas de Sentinel.

ISOC suma, en vista previa, automatización nativa sin workspace: reglas mejoradas sobre alertas y casos y un **Playbook Generator** que crea playbooks en Python a partir de lenguaje natural. Este módulo cubre los patrones que funcionan —enriquecer, aprobar y contener con reversión— con los playbooks oficiales de GitHub y las precauciones de identidad, permisos y costo. La profundidad en Logic Apps está en el programa de Sentinel (módulo X1).

**Por qué importa**

La automatización bien diseñada reduce el tiempo de contención y el trabajo repetitivo que quema analistas; mal diseñada, aísla al servidor equivocado a las tres de la mañana. Un catálogo de playbooks con aprobación humana, reversión probada y métricas de ejecución es lo que separa a un SOC que escala de uno que acumula deuda técnica.

**Qué vas a lograr**

- Diseñar reglas de automatización con el disparador correcto en el portal de Defender.
- Desplegar playbooks oficiales de contención con identidad administrada y aprobación humana.
- Evaluar la automatización nativa de ISOC y sus límites.
- Medir y gobernar la automatización: ejecuciones, errores, reversiones y costo.

> **Atención.** En el portal de Defender, las reglas de automatización con disparador de alerta solo actúan sobre alertas de Sentinel: para alertas de Defender XDR usa el Enhanced Alert Trigger. La latencia puede llegar a 10 minutos y no se pueden lanzar playbooks manuales sobre alertas o entidades ([automatización en Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/automation/automation)).

> **Atención.** El conector de Logic Apps de MDE todavía se llama «Microsoft Defender ATP»: permite aislar, restringir la ejecución, analizar con el antivirus y usar live response, con un límite de 100 llamadas por minuto por conexión. Su acción «Advanced Hunting» se retira el **1 de febrero de 2027**: migra a Microsoft Graph ([conector](https://learn.microsoft.com/en-us/connectors/wdatp/)).

> **Novedad.** ISOC (vista previa) trae un Playbook Generator que crea playbooks en Python a partir de lenguaje natural, con límites de 100 playbooks por inquilino, 10 minutos por ejecución, 500 reglas activas y una acción por regla, y con permisos «Automation» en el RBAC unificado ([automatización con ISOC](https://learn.microsoft.com/en-us/defender-xdr/siem-defender-automation)).

> **Consejo Ninja.** Parte de playbooks oficiales en vez de escribir desde cero: para MDE, Isolate/Unisolate, Restrict app execution, bloqueo de dominio, hash, IP o URL y Run antivirus ([playbooks de MDE](https://github.com/Azure/Azure-Sentinel/tree/master/Solutions/MicrosoftDefenderForEndpoint/Playbooks)); para Entra ID, Block-AADUser, Revoke-AADSignInSessions, Reset-AADUserPassword y Prompt-User ([playbooks de Entra ID](https://github.com/Azure/Azure-Sentinel/tree/master/Solutions/Microsoft%20Entra%20ID/Playbooks)). Logic Apps se paga aparte aunque tengas Security Copilot incluido en E5 ([MC1261596](https://mc.merill.net/message/MC1261596)).

**¿Tienes poco tiempo?**

- [Automation in Microsoft Sentinel: Security orchestration, automation, and response (SOAR)](https://learn.microsoft.com/en-us/azure/sentinel/automation/automation) · Documentación
- [Microsoft Defender ATP - Connectors (Logic Apps / Power Automate connector reference)](https://learn.microsoft.com/en-us/connectors/wdatp/) · Documentación
- [Azure-Sentinel/Solutions/MicrosoftDefenderForEndpoint/Playbooks](https://github.com/Azure/Azure-Sentinel/tree/master/Solutions/MicrosoftDefenderForEndpoint/Playbooks) · GitHub
- [Automation with ISOC in Microsoft Defender (preview)](https://learn.microsoft.com/en-us/defender-xdr/siem-defender-automation) · Documentación

### Documentación, cursos y credenciales

- [Automation in Microsoft Sentinel: Security orchestration, automation, and response (SOAR)](https://learn.microsoft.com/en-us/azure/sentinel/automation/automation) · Documentación · Oficial · Nuevo · Microsoft Learn · 28 jun 2026. Explica reglas de automatización y playbooks de Sentinel y las diferencias de comportamiento al operar en el portal Defender (desencadenadores, latencias, campos eliminados y acciones no soportadas).
- [Microsoft Defender ATP - Connectors (Logic Apps / Power Automate connector reference)](https://learn.microsoft.com/en-us/connectors/wdatp/) · Documentación · Oficial · Microsoft Learn. Referencia del conector de Defender for Endpoint para Logic Apps/Power Automate con acciones de aislamiento, restricción de ejecución, antivirus, paquete de investigación, live response, alertas y etiquetado de máquinas.
- [Automation with ISOC in Microsoft Defender (preview)](https://learn.microsoft.com/en-us/defender-xdr/siem-defender-automation) · Documentación · Oficial · Vista previa · Microsoft Learn. Describe la automatización nativa del Integrated SOC en Defender: reglas de automatización, playbooks de Logic Apps, Playbook Generator con IA (playbooks en Python), perfiles de integración y enhanced alert trigger. *Nota:* Límites: 100 playbooks generados por tenant, 10 min por ejecución, 500 reglas activas; permisos URBAC 'Automation' (Admin Execution Low/Medium/High); sin workspace de Sentinel para datos de Microsoft
- [Create and use Microsoft Sentinel automation rules to manage response](https://learn.microsoft.com/en-us/azure/sentinel/create-manage-use-automation-rules) · Documentación · Oficial · Microsoft Learn. Guía para diseñar y crear reglas de automatización de Sentinel (disparadores de incidente y alerta, condiciones, acciones, orden y auditoría).
- [Create automation rules with ISOC in Microsoft Defender (preview)](https://learn.microsoft.com/en-us/defender-xdr/siem-defender-create-automation-rules) · Documentación · Oficial · Vista previa · Microsoft Learn. Procedimiento para crear reglas de automatización estándar (incidentes, playbooks de Logic Apps) y mejoradas (alertas y casos, playbooks generados) en el portal Defender. *Nota:* Disponible en español (es-es)

### Laboratorios, GitHub y herramientas

- [Azure-Sentinel/Solutions/MicrosoftDefenderForEndpoint/Playbooks](https://github.com/Azure/Azure-Sentinel/tree/master/Solutions/MicrosoftDefenderForEndpoint/Playbooks) · GitHub · Oficial · Nuevo · Microsoft y comunidad · GitHub - Azure/Azure-Sentinel · oct 2026. Playbooks oficiales de Logic Apps para Defender for Endpoint: Isolate/Unisolate-MDEMachine, Restrict-MDEAppExecution, Restrict-MDEDomain/FileHash/IPAddress/Url y Run-MDEAntivirus.
- [Azure-Sentinel/Solutions/Microsoft Entra ID/Playbooks](https://github.com/Azure/Azure-Sentinel/tree/master/Solutions/Microsoft%20Entra%20ID/Playbooks) · GitHub · Oficial · Legado aún útil · Microsoft y comunidad · GitHub - Azure/Azure-Sentinel · mar 2026. Playbooks oficiales de Logic Apps para identidad: Block-AADUser (deshabilitar usuario), Revoke-AADSignInSessions (revocar sesiones), Reset-AADUserPassword y Prompt-User (confirmación del usuario). *Nota:* Los nombres conservan el prefijo AAD (Azure AD → Microsoft Entra ID); último cambio hace ~8 meses
- [Azure-Sentinel/Solutions/Microsoft Defender XDR](https://github.com/Azure/Azure-Sentinel/tree/master/Solutions/Microsoft%20Defender%20XDR) · GitHub · Oficial · Nuevo · Microsoft y comunidad · GitHub - Azure/Azure-Sentinel · oct 2026. Solución oficial de Defender XDR para Sentinel con reglas de análisis, consultas de hunting, workbooks XDR y el playbook AttackSimulatorTrainingNonReporters.
- [Azure-Sentinel/Solutions/Microsoft Defender for Office 365](https://github.com/Azure/Azure-Sentinel/tree/master/Solutions/Microsoft%20Defender%20for%20Office%20365) · GitHub · Oficial · Nuevo · Microsoft y comunidad · GitHub - Azure/Azure-Sentinel · oct 2026. Solución de Sentinel para Defender for Office 365 con conector, workbooks XDR y carpeta de playbooks para respuesta de correo.
- [Azure/Security-Copilot (repositorio oficial de la comunidad de Security Copilot)](https://github.com/Azure/Security-Copilot) · GitHub · Oficial · Legado aún útil · Microsoft y comunidad · GitHub - Azure · feb 2026. Repositorio oficial con plugins, promptbooks, talleres técnicos y ejemplos de Logic Apps que integran Security Copilot en flujos de respuesta. *Nota:* Último commit hace ~9 meses; la carpeta Logic Apps no se actualiza desde 2025 (Copilot for Security → Security Copilot)

**Manos a la obra**

1. `Laboratorio parcial` Despliega Isolate-MDEMachine y Block-AADUser desde GitHub, agrega una tarjeta de aprobación en Teams y dispáralos con una regla de automatización sobre un incidente de prueba ([playbooks de MDE](https://github.com/Azure/Azure-Sentinel/tree/master/Solutions/MicrosoftDefenderForEndpoint/Playbooks)). Limitación: Logic Apps genera costo en Azure y el conector de Teams requiere usuarios con licencia en el inquilino de prueba. En producción, la aprobación humana es obligatoria y el alcance se limita a un grupo piloto. Evidencia: ejecución con la aprobación registrada.
2. `Laboratorio` Prueba la reversión: ejecuta Unisolate-MDEMachine sobre el equipo aislado y verifica que vuelve a comunicarse. Evidencia: historial de ambas ejecuciones y del Action center.
3. `Laboratorio` Crea una regla de automatización que se dispare por etiqueta y no por título, y otra con el Enhanced Alert Trigger para alertas de Defender XDR ([reglas de automatización](https://learn.microsoft.com/en-us/azure/sentinel/create-manage-use-automation-rules)). Evidencia: configuración de ambas y su historial de ejecución.
4. `Laboratorio` Configura la identidad administrada del playbook con solo los permisos de API que usa cada acción y elimina las conexiones con cuentas de usuario. Evidencia: asignaciones de permisos documentadas.
5. `Laboratorio` Busca en tus Logic Apps la acción «Advanced Hunting» del conector de MDE y planifica su migración a `runHuntingQuery` de Graph antes del 1 de febrero de 2027 ([conector](https://learn.microsoft.com/en-us/connectors/wdatp/)). Evidencia: inventario de flujos afectados con fecha de migración.
6. `Laboratorio` Mide la automatización durante una semana: ejecuciones, fallas, tiempo ahorrado estimado y costo en el análisis de costos de Azure. Evidencia: informe de una página con una mejora propuesta.
7. `Solo producción` Evalúa la automatización de ISOC y su Playbook Generator ([automatización con ISOC](https://learn.microsoft.com/en-us/defender-xdr/siem-defender-automation)). Requiere un inquilino elegible sin workspace de Sentinel activo. Cómo hacerlo seguro: inquilino secundario elegible, revisión humana del código Python generado antes de activarlo y una sola regla piloto con su reversión.

**¿Quieres profundizar?**

- [Azure-Sentinel/Solutions/Microsoft Entra ID/Playbooks](https://github.com/Azure/Azure-Sentinel/tree/master/Solutions/Microsoft%20Entra%20ID/Playbooks) · GitHub
- [Azure-Sentinel/Solutions/Microsoft Defender XDR](https://github.com/Azure/Azure-Sentinel/tree/master/Solutions/Microsoft%20Defender%20XDR) · GitHub

<a id="a3"></a>

## A3 · Hunting avanzado e inteligencia de amenazas

*L400 · ~8 h · Origen: Ninja oficial de Defender XDR, Fundamentals (inteligencia de amenazas) y Expert (hunting)*

La inteligencia de amenazas le da dirección a la caza. En el portal de Defender, **threat analytics** publica informes de actores, campañas y vulnerabilidades con los incidentes relacionados, los activos expuestos, las acciones recomendadas e indicadores; **Intel explorer** permite buscar, crear, relacionar y exportar inteligencia, incluida la de Sentinel. Desde el 1 de agosto de 2026 el portal independiente de Defender Threat Intelligence está retirado y los datos públicos de Microsoft Threat Intelligence se incluyen sin costo adicional para clientes de Defender XDR.

En este nivel cazas como un equipo: **Hunts** de Sentinel para campañas de caza por hipótesis con marcadores, métricas y conversión en reglas; el **hunting graph** para ver rutas hacia activos críticos; y técnicas de identidad de la comunidad —password spray, AiTM, robo de PRT, abuso de Microsoft Graph— con el Attack and Defense Playbook for Microsoft Entra y los blogs de MVP especializados en detección de amenazas de identidad (ITDR).

**Por qué importa**

Cazar a ciegas consume horas y produce poco; cazar a partir de inteligencia sobre actores que atacan tu sector y tu región enfoca el esfuerzo donde está el riesgo. Además, documentar los hunts con hipótesis, evidencia y resultado convierte la caza en un activo medible del SOC ([S3](04_Nivel_4_Excelencia_del_SOC.md#s3) y [S5](04_Nivel_4_Excelencia_del_SOC.md#s5)).

**Qué vas a lograr**

- Usar threat analytics e Intel explorer para priorizar hipótesis.
- Gestionar una campaña de caza con Hunts: hipótesis, marcadores y conversión en reglas.
- Usar el hunting graph para analizar rutas hacia activos críticos.
- Cazar técnicas de identidad (spray, AiTM, robo de tokens) con tablas de Entra y de MDI.

> **Qué cambió.** Los datos públicos de Microsoft Threat Intelligence están disponibles sin costo adicional para clientes de Defender XDR, y el portal independiente de MDTI y el Intel explorer heredado se retiraron el 1 de agosto de 2026 ([Intel explorer](https://learn.microsoft.com/en-us/defender-xdr/threat-intelligence-explorer)). La convergencia se anunció el 22 de julio de 2025 ([anuncio](https://techcommunity.microsoft.com/blog/microsoftthreatprotectionblog/mdti-is-converging-into-microsoft-sentinel-and-defender-xdr/4427991)).

> **Atención.** Threat analytics requiere licencia de al menos un producto Defender (MDE P1 no da acceso) y su pestaña Indicators (vista previa) exige un inquilino verificado ([threat analytics](https://learn.microsoft.com/en-us/defender-xdr/threat-analytics)). Desde noviembre de 2025, los clientes de Sentinel reciben alertas «Microsoft Threat Intelligence» sobre actores estatales y ransomware ([novedades](https://learn.microsoft.com/en-us/defender-xdr/whats-new)).

> **Novedad.** **Hunts** organiza la caza por hipótesis con marcadores, métricas y conversión en reglas o incidentes, y requiere Microsoft Sentinel Contributor ([Hunts](https://learn.microsoft.com/en-us/azure/sentinel/hunts)); el **hunting graph** requiere el data lake de Sentinel y lectura en Exposure Management ([hunting graph](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-graph)).

> **Consejo Ninja.** Para la caza de identidad, el Attack and Defense Playbook for Microsoft Entra, de Thomas Naunheim y Sami Lamppu, sumó un capítulo de identidades de agentes y migró sus consultas a `EntraIdSignInEvents` ([AzureAD-Attack-Defense](https://github.com/Cloud-Architekt/AzureAD-Attack-Defense)), y Fabian Bader muestra cómo detectar amenazas con `GraphAPIAuditEvents` ([Cloudbrothers](https://cloudbrothers.info/en/detect-threats-graphapiauditevents-part-3/)).

**¿Tienes poco tiempo?**

- [Threat analytics in Microsoft Defender](https://learn.microsoft.com/en-us/defender-xdr/threat-analytics) · Documentación
- [Use Intel explorer in Microsoft Defender](https://learn.microsoft.com/en-us/defender-xdr/threat-intelligence-explorer) · Documentación
- [Conduct end-to-end proactive threat hunting in Microsoft Sentinel (Hunts)](https://learn.microsoft.com/en-us/azure/sentinel/hunts) · Documentación
- [Attack and Defense Playbook for Microsoft Entra (AzureAD-Attack-Defense)](https://github.com/Cloud-Architekt/AzureAD-Attack-Defense) · GitHub

### Documentación, cursos y credenciales

- [Threat analytics in Microsoft Defender](https://learn.microsoft.com/en-us/defender-xdr/threat-analytics) · Documentación · Oficial · Nuevo · Microsoft Learn · 26 may 2026. Describe los informes de threat analytics (resumen, informe del analista, incidentes relacionados, activos impactados, exposición, acciones recomendadas e indicadores IOC en preview) y sus requisitos de licencia y permisos.
- [Use Intel explorer in Microsoft Defender](https://learn.microsoft.com/en-us/defender-xdr/threat-intelligence-explorer) · Documentación · Oficial · Microsoft Learn. Guía de Intel explorer en el portal Defender para buscar, crear (STIX), etiquetar, relacionar, enriquecer y exportar inteligencia de amenazas, incluida la de Sentinel.
- [Conduct end-to-end proactive threat hunting in Microsoft Sentinel (Hunts)](https://learn.microsoft.com/en-us/azure/sentinel/hunts) · Documentación · Oficial · Microsoft Learn. Describe la experiencia 'Hunts' para hunting basado en hipótesis (comportamiento sospechoso, campañas nuevas, brechas MITRE) con bookmarks, comentarios, métricas y creación de reglas o incidentes.
- [Hunt for threats using the hunting graph](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-graph) · Documentación · Oficial · Microsoft Learn. Explica el hunting graph de búsqueda avanzada, que renderiza escenarios predefinidos (rutas a activos críticos, relaciones de entidades, acceso a key vaults) como grafos interactivos.
- [Threat intelligence in Microsoft Defender](https://learn.microsoft.com/en-us/defender-xdr/defender-threat-intelligence) · Documentación · Oficial · Vista previa · Microsoft Learn. Panorama de la experiencia de inteligencia de amenazas integrada en Defender (Overview, Intel explorer, enriquecimiento en páginas de entidad, threat analytics, Copilot y Threat Intelligence Agent). *Nota:* Algunas capacidades en preview; con ISOC se requiere un workspace ISOC

### Anuncios y blogs oficiales

- [MDTI is Converging into Microsoft Sentinel and Defender XDR](https://techcommunity.microsoft.com/blog/microsoftthreatprotectionblog/mdti-is-converging-into-microsoft-sentinel-and-defender-xdr/4427991) · Blog oficial · Empleado de Microsoft · Legado aún útil · Mike Browning · Microsoft Tech Community - Microsoft Defender XDR Blog · 22 jul 2025. Anuncia la convergencia de Microsoft Defender Threat Intelligence en Defender XDR y Sentinel sin costo adicional, con informes terminados, IOC vinculados a actores y TTP de MITRE en threat analytics. *Nota:* Anuncio de julio de 2025; la convergencia se completó y el portal MDTI heredado se retiró el 2026-08-01 (ver Intel explorer en Learn)

### Laboratorios, GitHub y herramientas

- [Attack and Defense Playbook for Microsoft Entra (AzureAD-Attack-Defense)](https://github.com/Cloud-Architekt/AzureAD-Attack-Defense) · GitHub · MVP · Nuevo · Thomas Naunheim y Sami Lamppu (con Christopher Brumm, Fabian Bader y otros) · GitHub - Cloud-Architekt · oct 2026. Playbook comunitario de ataque y defensa para Entra ID (password spray, consent grant, PRT, AiTM, Entra Connect, Agent ID) con detecciones KQL, mitigaciones y mapeo MITRE ATT&CK.
- [Hunting-Queries-Detection-Rules / Defender For Identity](https://github.com/Bert-JanP/Hunting-Queries-Detection-Rules/tree/main/Defender%20For%20Identity) · GitHub · MVP · Bert-Jan Pals · GitHub - Bert-JanP. Colección de consultas KQL de detección y hunting para Defender for Identity (LDAP anómalo, downgrade Kerberos, nuevas LMP a cuentas sensibles, device code, grupos sensibles).

### Comunidad: blogs, libros, newsletters y eventos

- [ITDR | Chris Brumm's Blog](https://chris-brumm.com/categories/itdr/) · Blog · MVP · Nuevo · Christopher Brumm · Chris Brumm's Blog · 24 oct 2026. Categoría ITDR del blog con artículos recientes sobre prevención, detección y respuesta a device code phishing y AuthCodeFix (ConsentFix) en Entra ID.
- [Now You See Me: AADGraphActivityLogs](https://cloudbrothers.info/en/aadgraphactivitylogs/) · Blog · MVP · Nuevo · Fabian Bader · Cloudbrothers · 10 may 2026. Uso de la nueva fuente AADGraphActivityLogs (mayo 2026) para cazar herramientas como ROADtools y AADInternals que abusan de Azure AD Graph.
- [Detect threats using GraphAPIAuditEvents - Part 3](https://cloudbrothers.info/en/detect-threats-graphapiauditevents-part-3/) · Blog · MVP · Fabian Bader · Cloudbrothers · 14 ago 2025. Detecciones de reconocimiento (AzureHound) con la tabla GraphAPIAuditEvents del portal Defender, correlación con IdentityInfo y logs de inicio de sesión.

**Manos a la obra**

1. `Laboratorio` Elige un informe de [threat analytics](https://learn.microsoft.com/en-us/defender-xdr/threat-analytics) relevante para tu sector, revisa la exposición y los activos afectados y escribe una hipótesis de caza con sus fuentes de datos. Evidencia: plan de hunting de una página.
2. `Laboratorio` Toma un indicador de la [campaña «code of conduct»](https://www.microsoft.com/en-us/security/blog/2026/05/04/breaking-the-code-multi-stage-code-of-conduct-phishing-campaign-leads-to-aitm-token-compromise/) (4 de mayo de 2026), búscalo en el [Intel explorer](https://learn.microsoft.com/en-us/defender-xdr/threat-intelligence-explorer) y pivota hacia tus datos con la búsqueda avanzada. Evidencia: consulta y conclusión, aunque el resultado sea vacío.
3. `Laboratorio` Caza AiTM y robo de tokens con las consultas del [Attack and Defense Playbook](https://github.com/Cloud-Architekt/AzureAD-Attack-Defense) sobre `EntraIdSignInEvents` y `CloudAppEvents`, adaptadas a tu laboratorio. Evidencia: dos consultas documentadas con sus supuestos.
4. `Laboratorio` Desde una aplicación de prueba, enumera usuarios con Microsoft Graph y detecta esa actividad en `GraphAPIAuditEvents` siguiendo la [serie de Cloudbrothers](https://cloudbrothers.info/en/detect-threats-graphapiauditevents-part-3/). Evidencia: consulta con la actividad de la aplicación.
5. `Laboratorio parcial` Crea un hunt en Sentinel con hipótesis, consultas y marcadores, y convierte un hallazgo en una regla ([Hunts](https://learn.microsoft.com/en-us/azure/sentinel/hunts)). Limitación: requiere el workspace de [M8](02_Nivel_2_Intermedio.md#m8) y el rol Microsoft Sentinel Contributor, y el volumen del laboratorio es bajo. Evidencia: hunt con sus métricas y la regla creada.
6. `Laboratorio parcial` Usa el [hunting graph](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-graph) para analizar las rutas hacia el controlador de dominio del laboratorio. Limitación: requiere el data lake de Sentinel, con su costo, y permisos de lectura de Exposure Management. Evidencia: captura de la ruta y la corrección que propones.

**¿Quieres profundizar?**

- [Hunting-Queries-Detection-Rules / Defender For Identity](https://github.com/Bert-JanP/Hunting-Queries-Detection-Rules/tree/main/Defender%20For%20Identity) · GitHub
- [ITDR | Chris Brumm's Blog](https://chris-brumm.com/categories/itdr/) · Blog
- [Now You See Me: AADGraphActivityLogs](https://cloudbrothers.info/en/aadgraphactivitylogs/) · Blog
- [Detect threats using GraphAPIAuditEvents - Part 3](https://cloudbrothers.info/en/detect-threats-graphapiauditevents-part-3/) · Blog

<a id="a4"></a>

## A4 · APIs y automatización programática

*L400 · ~8 h · Origen: Ninja oficial de Defender XDR, Expert (APIs) y Ninja de Defender for Endpoint (APIs)*

Todo lo que haces en el portal se puede hacer por código. La **API de seguridad de Microsoft Graph** concentra hoy incidentes y alertas (`alerts_v2`), búsqueda avanzada (`runHuntingQuery`), detecciones personalizadas (`detectionRules`, en beta), remediación de correo (`analyzedEmail: remediate`), simulaciones de ataque e identidades de MDI; la API de Defender for Endpoint mantiene acciones de dispositivo como **live response**.

2026 trae fechas que rompen integraciones: la API de alertas heredada de Graph se retiró el **15 de octubre de 2026**, las propiedades `isEnabled`, `detectorId` y `lastRunDetails` de `detectionRule` se eliminaron el 1 de octubre y las APIs antiguas de búsqueda avanzada dejan de devolver datos el **1 de febrero de 2027**. Este módulo te enseña a automatizar con las APIs vigentes, con permisos mínimos y respetando los límites.

**Por qué importa**

Las APIs son el puente entre el SOC y el resto de la organización: ITSM, CMDB, herramientas propias, informes y SOAR de terceros. Migrarlas a tiempo evita apagones silenciosos de integraciones críticas, y diseñarlas con permisos de aplicación mínimos reduce el riesgo de que una credencial de automatización se vuelva la llave maestra del atacante.

**Qué vas a lograr**

- Autenticar una aplicación con permisos mínimos para la API de seguridad de Graph.
- Ejecutar búsquedas avanzadas por API respetando cuotas y límites.
- Gestionar detecciones personalizadas y remediar correos por API.
- Usar live response por API de forma controlada.
- Inventariar y migrar las integraciones afectadas por los retiros de 2026 y 2027.

> **Atención.** `runHuntingQuery` de Microsoft Graph consulta 30 días y devuelve hasta 100.000 filas, con al menos 45 llamadas por minuto por inquilino, un tiempo límite de 3 minutos y 50 MB. Las API antiguas de búsqueda avanzada de MDE y de Defender XDR dejan de devolver datos el **1 de febrero de 2027** ([API de seguridad de Graph](https://learn.microsoft.com/en-us/graph/api/resources/security-api-overview?view=graph-rest-1.0)).

> **Qué cambió.** La API heredada de alertas de Graph (`/security/alerts`) se retiró el 15 de octubre de 2026: migra a `alerts_v2` e `incidents` ([API de seguridad de Graph](https://learn.microsoft.com/en-us/graph/api/resources/security-api-overview?view=graph-rest-1.0)). En `detectionRule` (beta), que usa el permiso `CustomDetection.ReadWrite.All`, las propiedades `isEnabled`, `detectorId` y `lastRunDetails` se eliminaron el 1 de octubre de 2026: usa `status` ([detectionRule](https://learn.microsoft.com/en-us/graph/api/resources/security-detectionrule?view=graph-rest-beta)).

> **Novedad.** `analyzedEmail: remediate` (v1.0) permite borrar de forma recuperable o definitiva y mover a correo no deseado, a la bandeja de entrada o a elementos eliminados desde tu SOAR; solo admite el permiso de aplicación `SecurityAnalyzedMessage.ReadWrite.All` y cada acción se sigue en el Action center ([remediate](https://learn.microsoft.com/en-us/graph/api/security-analyzedemail-remediate?view=graph-rest-1.0)).

> **Atención.** La API de live response de MDE admite 10 llamadas por minuto y 50 sesiones simultáneas, deja una sesión en cola hasta 2 horas, corta `RunScript` a los 10 minutos y requiere el permiso `Machine.LiveResponse` ([live response por API](https://learn.microsoft.com/en-us/defender-endpoint/api/run-live-response)). Diseña reintentos y colas en lugar de llamadas en ráfaga.

**¿Tienes poco tiempo?**

- [Use the Microsoft Graph security API](https://learn.microsoft.com/en-us/graph/api/resources/security-api-overview?view=graph-rest-1.0) · Documentación
- [detectionRule resource type (Microsoft Graph beta)](https://learn.microsoft.com/en-us/graph/api/resources/security-detectionrule?view=graph-rest-beta) · Documentación
- [analyzedEmail: remediate (Microsoft Graph v1.0)](https://learn.microsoft.com/en-us/graph/api/security-analyzedemail-remediate?view=graph-rest-1.0) · Documentación
- [Run live response commands on a device (Defender for Endpoint API)](https://learn.microsoft.com/en-us/defender-endpoint/api/run-live-response) · Documentación

**Retiros y cambios de API que afectan tus integraciones**

| Fecha | Qué cambia | Qué hacer | Fuente |
|---|---|---|---|
| 1 de julio de 2026 | La tabla AIAgentsInfo deja de estar accesible | Migra consultas y detecciones a AgentsInfo | [Novedades de Defender XDR](https://learn.microsoft.com/en-us/defender-xdr/whats-new) |
| 1 de octubre de 2026 | detectionRule (beta) elimina isEnabled, detectorId y lastRunDetails | Usa la propiedad status en scripts y pipelines | [detectionRule](https://learn.microsoft.com/en-us/graph/api/resources/security-detectionrule?view=graph-rest-beta) |
| 15 de octubre de 2026 | Se retira la API heredada de alertas de Graph (/security/alerts) | Migra a alerts_v2 e incidents | [API de seguridad de Graph](https://learn.microsoft.com/en-us/graph/api/resources/security-api-overview?view=graph-rest-1.0) |
| 19 de octubre de 2026 | EntraIdSignInEvents reemplaza a AADSignInEventsBeta | Revisa scripts externos y reglas gestionadas como código | [EntraIdSignInEvents](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-entraidsigninevents-table) |
| 1 de febrero de 2027 | Las API antiguas de búsqueda avanzada de MDE y Defender XDR dejan de devolver datos y se retira la acción «Advanced Hunting» del conector de MDE | Migra a runHuntingQuery de Microsoft Graph | [API de seguridad de Graph](https://learn.microsoft.com/en-us/graph/api/resources/security-api-overview?view=graph-rest-1.0) y [conector de MDE](https://learn.microsoft.com/en-us/connectors/wdatp/) |
| 31 de marzo de 2027 | Sentinel deja de estar soportado en el portal de Azure | Opera desde el portal de Defender y revisa automatizaciones que dependan del portal de Azure | [Nuevo calendario de Sentinel](https://techcommunity.microsoft.com/blog/microsoftsentinelblog/update-new-timeline-for-transitioning-sentinel-experience-to-defender-portal/4490464) |

Fechas verificadas al 6 de noviembre de 2026. Revisa las novedades después de Microsoft Ignite (17 al 20 de noviembre de 2026).

### Documentación, cursos y credenciales

- [Use the Microsoft Graph security API](https://learn.microsoft.com/en-us/graph/api/resources/security-api-overview?view=graph-rest-1.0) · Documentación · Oficial · Nuevo · Microsoft Learn · 2 nov 2026. Panorama de la API de seguridad de Microsoft Graph (runHuntingQuery, detecciones personalizadas, alerts_v2 e incidentes, attack simulation, identidades MDI, threat intelligence) con cuotas y guías de migración.
- [analyzedEmail: remediate (Microsoft Graph v1.0)](https://learn.microsoft.com/en-us/graph/api/security-analyzedemail-remediate?view=graph-rest-1.0) · Documentación · Oficial · Microsoft Learn. API de Graph para remediar correos (mover a junk/inbox/elementos eliminados, soft delete, hard delete) desde playbooks y SOAR, con seguimiento en el Action center.
- [Run live response commands on a device (Defender for Endpoint API)](https://learn.microsoft.com/en-us/defender-endpoint/api/run-live-response) · Documentación · Oficial · Microsoft Learn · 31 dic 2025. Referencia de la API de live response de MDE (PutFile, RunScript, GetFile) con sistemas soportados, límites de tasa y sesiones, y permisos Machine.LiveResponse.
- [detectionRule resource type (Microsoft Graph beta)](https://learn.microsoft.com/en-us/graph/api/resources/security-detectionrule?view=graph-rest-beta) · Documentación · Oficial · Vista previa · Microsoft Learn. Recurso de Graph para gestionar reglas de detección personalizadas (list, create, get, update, delete) con consulta KQL, programación, estado y acciones de respuesta. *Nota:* Propiedades isEnabled, detectorId y lastRunDetails obsoletas y eliminadas desde 2026-10-01 (usar 'status'); permiso CustomDetection.ReadWrite.All
- [Create detectionRule (Microsoft Graph beta)](https://learn.microsoft.com/en-us/graph/api/security-rulesroot-post-detectionrules?view=graph-rest-beta) · Documentación · Oficial · Vista previa · Microsoft Learn. Ejemplo de creación de una regla de detección personalizada vía Graph (POST /security/rules/detectionRules) con roles URBAC requeridos. *Nota:* Base práctica para detection-as-code vía API además de Bicep/Repositories
- [List servicePrincipalRiskDetections - Microsoft Graph v1.0](https://learn.microsoft.com/en-us/graph/api/identityprotectionroot-list-serviceprincipalriskdetections?view=graph-rest-1.0) · Documentación · Oficial · Microsoft Learn - Microsoft Graph. Referencia de la API para listar detecciones de riesgo de principales de servicio (workload identities).

### Laboratorios, GitHub y herramientas

- [Identify and remediate risk by using ID Protection APIs (Microsoft Graph tutorial)](https://learn.microsoft.com/en-us/graph/tutorial-riskdetection-api) · Laboratorio · Oficial · Microsoft Learn - Microsoft Graph. Tutorial práctico con Graph para generar un inicio de sesión riesgoso de prueba, listar riskDetections, crear acceso condicional con MFA y descartar el riesgo de usuario.

**Manos a la obra**

1. `Laboratorio` Registra una aplicación con el permiso `ThreatHunting.Read.All` y ejecuta `runHuntingQuery` desde PowerShell o Python con reintentos que respeten los límites ([API de seguridad de Graph](https://learn.microsoft.com/en-us/graph/api/resources/security-api-overview?view=graph-rest-1.0)). Evidencia: script versionado en tu repositorio y su salida.
2. `Laboratorio` Migra una integración de prueba que use `/security/alerts` a `alerts_v2` e `incidents` y compara los campos disponibles. Evidencia: diferencias del código y una ejecución exitosa.
3. `Laboratorio` Crea y actualiza por API una detección personalizada usando `status` en lugar de las propiedades eliminadas ([crear detectionRule](https://learn.microsoft.com/en-us/graph/api/security-rulesroot-post-detectionrules?view=graph-rest-beta)). Evidencia: JSON de creación y de actualización.
4. `Laboratorio` Remedia por API los mensajes de la campaña de Attack simulation training con `analyzedEmail: remediate` en modo de borrado recuperable desde una aplicación registrada ([remediate](https://learn.microsoft.com/en-us/graph/api/security-analyzedemail-remediate?view=graph-rest-1.0)) y verifica la acción en el Action center. Evidencia: respuesta de la API y entrada del Action center.
5. `Laboratorio` Sube un script a la biblioteca de live response y ejecútalo por API con `RunScript` y `GetFile` en la VM de prueba, respetando 10 llamadas por minuto ([live response por API](https://learn.microsoft.com/en-us/defender-endpoint/api/run-live-response)). Evidencia: salida del script y archivo recuperado.
6. `Laboratorio` Lista detecciones de riesgo y confirma como comprometido a un usuario de prueba con la [API de ID Protection](https://learn.microsoft.com/en-us/graph/tutorial-riskdetection-api). Evidencia: llamadas y cambio del nivel de riesgo del usuario.
7. `Solo producción` Inventaria las integraciones productivas (conectores de SIEM, scripts y flujos de SOAR) que usan las API antiguas de búsqueda avanzada, la acción «Advanced Hunting» del conector o la API heredada de alertas. Requiere acceso a la configuración real. Cómo hacerlo seguro: revisión de solo lectura de los registros de aplicaciones y de los inicios de sesión de sus entidades de servicio, sin cambios, con un plan de migración priorizado antes del 1 de febrero de 2027.

**¿Quieres profundizar?**

- [Identify and remediate risk by using ID Protection APIs (Microsoft Graph tutorial)](https://learn.microsoft.com/en-us/graph/tutorial-riskdetection-api) · Laboratorio

<a id="a5"></a>

## A5 · Ingeniería de detecciones y purple teaming

*L400 · ~10 h · Origen: Nuevo en esta edición (amplía las detecciones personalizadas del Ninja de Defender for Endpoint)*

La ingeniería de detecciones trata las reglas como software: hipótesis basada en amenazas, consulta, pruebas con emulación, revisión por pares, despliegue como código, medición de precisión y retiro cuando dejan de servir. En la plataforma unificada, las detecciones personalizadas se gestionan como código (vista previa) con la extensión **Microsoft Security** de Bicep vía **Sentinel Repositories** o la CLI; la matriz **MITRE ATT&CK** de Sentinel (alineada a v18, en vista previa) muestra cobertura activa y simulada, y **SOC optimization** recomienda reglas por escenario de amenaza.

El **purple teaming** cierra el ciclo: el equipo ofensivo ejecuta técnicas reales en un entorno controlado y el defensivo verifica qué se detectó, qué no y por qué. Para hacerlo bien con Defender hay que seguir las guías de Microsoft para pruebas de penetración y simulación de brechas (BAS), simular historias de ataque completas contra MDI y usar bibliotecas como Atomic Red Team solo en laboratorio. Dato de contexto: Microsoft no participó en las MITRE ATT&CK Evaluations Enterprise 2025, así que la validación propia es aún más importante.

**Por qué importa**

Contar reglas no es tener cobertura. Un ciclo de ingeniería con pruebas de emulación demuestra qué técnicas detectas realmente, reduce falsos positivos antes de que lleguen al analista y permite reportar cobertura validada al comité de riesgos en lugar de un número de reglas activas.

**Qué vas a lograr**

- Diseñar detecciones a partir de técnicas de ATT&CK priorizadas por amenaza.
- Gestionar detecciones como código con repositorios, revisión por pares y CI/CD.
- Planificar y ejecutar un ejercicio de purple team seguro.
- Medir la cobertura validada y la precisión por regla.

> **Novedad.** La matriz MITRE ATT&CK de Sentinel en el portal de Defender está alineada a ATT&CK v18 y sigue en vista previa ([cobertura MITRE](https://learn.microsoft.com/en-us/azure/sentinel/mitre-coverage)); SOC optimization suma recomendaciones de cobertura por amenaza y etiquetado MITRE con IA, también en vista previa ([SOC optimization](https://learn.microsoft.com/en-us/azure/sentinel/soc-optimization/soc-optimization-reference)).

> **Novedad.** Detecciones como código (vista previa): las detecciones personalizadas se gestionan en GitHub o Azure DevOps con la extensión de Bicep «Microsoft Security», mediante Sentinel Repositories o la CLI de Bicep, con un máximo de 5 conexiones de repositorio por workspace; el repositorio sobrescribe los cambios hechos en el portal ([contenido como código](https://learn.microsoft.com/en-us/azure/sentinel/ci-cd-custom-content)).

> **Atención.** Antes de una prueba de penetración o de BAS contra MDE: protección contra alteraciones, ASR y network protection en bloqueo, protección en la nube activa y ninguna exclusión para las herramientas de BAS ([guía de pruebas](https://learn.microsoft.com/en-us/defender-endpoint/guidance-for-pen-testing-and-bas)). Contra MDI, simula historias de ataque completas, no técnicas sueltas, y verifica la salud de los sensores ([pruebas con MDI](https://learn.microsoft.com/en-us/defender-for-identity/security-testing-best-practices)).

> **Consejo Ninja.** Microsoft no participó en las MITRE ATT&CK Evaluations Enterprise 2025, según se anunció en junio de 2025 ([Infosecurity](https://www.infosecurity-magazine.com/news/cyber-vendors-pull-out-mitre/)): mide tu cobertura con tu propia emulación. [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team) sigue activo como biblioteca de pruebas mapeadas a ATT&CK, y [FalconFriday](https://github.com/FalconForceTeam/FalconFriday) publica detecciones con su lógica explicada.

**¿Tienes poco tiempo?**

- [Manage content as code with Microsoft Sentinel repositories (incl. Deploy custom detection rules as code - Preview)](https://learn.microsoft.com/en-us/azure/sentinel/ci-cd-custom-content) · Documentación
- [redcanaryco/atomic-red-team](https://github.com/redcanaryco/atomic-red-team) · GitHub
- [Guidance for penetration testing and breach-and-attack-simulation scenarios with Microsoft Defender for Endpoint](https://learn.microsoft.com/en-us/defender-endpoint/guidance-for-pen-testing-and-bas) · Documentación
- [View MITRE ATT&CK framework coverage in Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/mitre-coverage) · Documentación

### Documentación, cursos y credenciales

- [Manage content as code with Microsoft Sentinel repositories (incl. Deploy custom detection rules as code - Preview)](https://learn.microsoft.com/en-us/azure/sentinel/ci-cd-custom-content) · Documentación · Oficial · Microsoft Learn. Describe cómo desplegar contenido de Sentinel (reglas de análisis, automatización, detecciones personalizadas en preview, hunting, parsers, playbooks, workbooks) desde GitHub o Azure DevOps como fuente única de verdad (CI/CD).
- [Guidance for penetration testing and breach-and-attack-simulation scenarios with Microsoft Defender for Endpoint](https://learn.microsoft.com/en-us/defender-endpoint/guidance-for-pen-testing-and-bas) · Documentación · Oficial · Microsoft Learn. Lista de configuraciones de MDE/Defender Antivirus que deben estar activas antes de pruebas de penetración o BAS y cómo enviar posibles falsos negativos.
- [SOC optimization recommendations types (reference)](https://learn.microsoft.com/en-us/azure/sentinel/soc-optimization/soc-optimization-reference) · Documentación · Oficial · Microsoft Learn. Referencia de recomendaciones de SOC optimization: valor de datos, cobertura basada en amenazas, etiquetado MITRE con IA (preview) y riesgos de negocio.
- [View MITRE ATT&CK framework coverage in Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/mitre-coverage) · Documentación · Oficial · Vista previa · Microsoft Learn. Explica la matriz de cobertura MITRE ATT&CK de Sentinel en el portal Defender (detecciones activas, simuladas y por escenario de amenaza). *Nota:* Alineada a MITRE ATT&CK v18; página en preview
- [Best Practices before Offensive Security Testing for Microsoft Defender for Identity](https://learn.microsoft.com/en-us/defender-for-identity/security-testing-best-practices) · Documentación · Oficial · Microsoft Learn. Checklist previo a pruebas ofensivas contra MDI: sensores en todos los DC/AD FS/AD CS, salud, auditoría de eventos, NNR y simulación de historias de ataque completas.

### Laboratorios, GitHub y herramientas

- [redcanaryco/atomic-red-team](https://github.com/redcanaryco/atomic-red-team) · GitHub · Comunidad · Nuevo · Red Canary y comunidad · GitHub - Red Canary · nov 2026. Biblioteca de pruebas atómicas mapeadas a MITRE ATT&CK para validar de forma reproducible la cobertura de detección en laboratorio.
- [FalconForceTeam/FalconFriday](https://github.com/FalconForceTeam/FalconFriday) · GitHub · MVP · FalconForce (Olaf Hartong y equipo) · GitHub - FalconForce. Colección de consultas de hunting KQL para MDE y Sentinel enfocadas en técnicas avanzadas (inyección, ADCS, NTLM relay, PRT) vinculadas a MITRE ATT&CK con documentación de trade-offs.

### Comunidad: blogs, libros, newsletters y eventos

- [Blogs - FalconForce (Knowledge center)](https://falconforce.nl/blogs/) · Blog · MVP · Nuevo · Olaf Hartong y equipo FalconForce · FalconForce · 11 sep 2026. Blog de FalconForce sobre ingeniería de detección para Defender XDR y Sentinel: reglas NRT (FalconFriday 0xFF26), mantenimiento de detecciones, internos de MDE y la herramienta FalconDash de tuning.
- [I'm in your logs now: deceiving analysts and blinding EDRs](https://falconforce.nl/in-your-logs-now/) · Blog · MVP · Nuevo · Olaf Hartong · FalconForce · 26 ago 2026. Investigación sobre ETW que muestra cómo generar telemetría falsa o saturar buffers para engañar a analistas y cegar EDR como MDE, con implicaciones para validar detecciones.
- [Cyber Threat Detection Vendors Pull Out of MITRE Evaluations Test](https://www.infosecurity-magazine.com/news/cyber-vendors-pull-out-mitre/) · Blog · Comunidad · Kevin Poireault · Infosecurity Magazine · 22 sep 2025. Noticia sobre la retirada de Microsoft (anunciada en junio de 2025), SentinelOne y Palo Alto de las evaluaciones MITRE ATT&CK Enterprise 2025.
- [Custom Detection Rules as Code in Sentinel Repositories: What Your Pipeline Owns Now](https://techcommunity.microsoft.com/discussions/microsoft-security/custom-detection-rules-as-code-in-sentinel-repositories-what-your-pipeline-owns-/4536196) · Blog · Comunidad · Vista previa · Nuevo · Marcel Graewer · Microsoft Tech Community - Microsoft Security Community Forum · 12 jul 2026. Análisis comunitario del despliegue de detecciones personalizadas como código con el recurso Microsoft.Security/detectionRules en Bicep y del riesgo de que el repositorio no reciba las migraciones automáticas de nombres de tablas. *Nota:* Ejemplo: AIAgentsInfo dejó de estar accesible el 2026-07-01 (reemplazada por AgentsInfo); las reglas gestionadas como código no se migran solas

**Manos a la obra**

1. `Laboratorio` Prioriza diez técnicas de ATT&CK según tu modelo de amenazas (threat analytics y el MDDR 2026) y mapea qué detección existente cubre cada una. Evidencia: matriz técnica-detección con brechas.
2. `Laboratorio` Escribe la especificación de una detección: hipótesis, fuente de datos, consulta, mapeo de entidades, prueba atómica que la valida, falsos positivos esperados, dueño y criterio de retiro. Evidencia: especificación en tu repositorio.
3. `Laboratorio parcial` Haz un ejercicio de purple team con [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team): ejecuta cinco técnicas en una VM aislada, revisa las alertas de MDE y la [matriz MITRE](https://learn.microsoft.com/en-us/azure/sentinel/mitre-coverage) de Sentinel y documenta las brechas. Limitación: la matriz solo cuenta reglas activas de Sentinel y las pruebas atómicas nunca se ejecutan fuera del laboratorio. Evidencia: tabla técnica, alerta esperada y alerta obtenida.
4. `Laboratorio parcial` Conecta un repositorio de GitHub a Sentinel Repositories y despliega una detección personalizada en Bicep ([contenido como código](https://learn.microsoft.com/en-us/azure/sentinel/ci-cd-custom-content)). Limitación: está en vista previa, requiere Owner del grupo de recursos y el workspace incorporado, y todavía no admite frecuencia ni detalles personalizados. En producción, conecta primero un workspace no productivo y exige pull requests con revisión. Evidencia: pull request aprobado y regla desplegada.
5. `Laboratorio` Sigue las [buenas prácticas de pruebas con MDI](https://learn.microsoft.com/en-us/defender-for-identity/security-testing-best-practices): reproduce una historia completa (reconocimiento, robo de credenciales y movimiento lateral) en el laboratorio y verifica la salud de los sensores antes y después. Evidencia: línea de tiempo y alertas obtenidas.
6. `Solo producción` Ejecuta un purple team en producción. Requiere autorización, dispositivos reales y coordinación con los dueños de los sistemas. Cómo hacerlo seguro: aprobación por escrito, alcance limitado a un grupo piloto etiquetado, cuentas de prueba, ventana de cambio, la [guía de BAS de MDE](https://learn.microsoft.com/en-us/defender-endpoint/guidance-for-pen-testing-and-bas), alertas clasificadas como prueba de seguridad y plan de reversión.

**¿Quieres profundizar?**

- [Blogs - FalconForce (Knowledge center)](https://falconforce.nl/blogs/) · Blog
- [FalconForceTeam/FalconFriday](https://github.com/FalconForceTeam/FalconFriday) · GitHub

<a id="a6"></a>

## A6 · Security Copilot y agentes en Defender XDR

*L400 · ~8 h · Origen: Nuevo en esta edición (se profundiza en el programa de Security Copilot)*

**Security Copilot** está integrado en el portal de Defender: resume incidentes, propone respuestas guiadas, analiza scripts y archivos, traduce lenguaje natural a KQL y redacta informes. Desde Ignite 2025 se incluye en **Microsoft 365 E5**: 400 SCU al mes por cada 1.000 licencias pagas, con un tope de 10.000 SCU mensuales, desplegado por fases entre el 20 de abril y el 30 de junio de 2026; el data lake de Sentinel, Logic Apps y los agentes de terceros se pagan aparte.

Los **agentes** llevan la IA de la asistencia a la autonomía supervisada. En Defender, el **Security Alert Triage Agent** —llamado Phishing Triage Agent (nombre usado hasta Ignite 2025)— está en GA para correos reportados por usuarios y en vista previa para alertas de identidad y nube; el **Dynamic Threat Detection Agent**, el **Threat Hunting Agent** y el **Security Analyst Agent** están en vista previa, y **Project Perception**, un sistema multiagente, está en vista previa limitada por invitación. Este módulo cubre qué hace cada uno, cómo se licencia y cómo supervisarlo.

**Por qué importa**

La IA rinde cuando se usa con criterio: un agente que clasifica correos reportados libera horas de analista cada día, pero sin supervisión puede cerrar lo que no debía. Medir precisión, consumo de SCU y tiempo ahorrado, y definir qué decisiones nunca se delegan, es lo que convierte a Security Copilot en una ventaja operativa y no en un riesgo nuevo.

**Qué vas a lograr**

- Usar Security Copilot embebido en incidentes, búsqueda avanzada y análisis de scripts.
- Explicar la inclusión en E5, el cálculo de SCU y qué se paga aparte.
- Habilitar y supervisar el Security Alert Triage Agent con retroalimentación.
- Distinguir el estado (GA o vista previa) y el costo de cada agente de Defender.
- Definir la política de supervisión humana para agentes.

> **Novedad.** Security Copilot está incluido en Microsoft 365 E5 desde Ignite 2025: 400 SCU al mes por cada 1.000 licencias, con un tope de 10.000, y agentes en Defender, Entra, Intune y Purview sin costo adicional ([Security Copilot en E5](https://www.microsoft.com/en-us/security/security-copilot-in-microsoft-365-e5)). El despliegue fue por fases entre el 20 de abril y el 30 de junio de 2026; el data lake de Sentinel, Logic Apps y los agentes de terceros se pagan aparte ([MC1261596](https://mc.merill.net/message/MC1261596)).

> **Atención.** El **Security Alert Triage Agent** está en GA para correos reportados por usuarios y en vista previa para alertas de nube, contenedores e identidad. Requiere SCU, el RBAC unificado activo y desactivar las reglas de ajuste que resuelven solas las alertas que debe clasificar, y su aprendizaje por retroalimentación solo aplica al correo ([agente de triage](https://learn.microsoft.com/en-us/defender-xdr/security-alert-triage-agent)). Desde junio de 2026, los agentes de triage usan permisos de mínimo privilegio ([novedades en español](https://learn.microsoft.com/es-es/defender-xdr/whats-new)).

> **Atención.** Estados a noviembre de 2026: el Dynamic Threat Detection Agent está en vista previa, siempre activo y gratis, pero consumirá SCU en GA ([DTDA](https://learn.microsoft.com/en-us/defender-xdr/dynamic-threat-detection-agent)); el Security Analyst Agent, en vista previa pública desde abril de 2026 ([novedades de Security Copilot](https://learn.microsoft.com/en-us/copilot/security/whats-new-copilot-security)); el Threat Hunting Agent de la búsqueda avanzada, en vista previa ([Threat Hunting Agent](https://learn.microsoft.com/en-nz/defender-xdr/advanced-hunting-security-copilot-threat-hunting-agent)), y Project Perception, en vista previa limitada por invitación ([Perception](https://learn.microsoft.com/en-us/security/agentic-security/triage-agent)). Ignite (17 al 20 de noviembre de 2026) puede cambiar estos estados.

> **Consejo Ninja.** Gobierna cada agente como una identidad privilegiada: Microsoft recomienda una identidad de agente dedicada (Entra Agent ID) en lugar de heredar credenciales de usuario, acciones acotadas que requieren aprobación y revisión de la retroalimentación; Security Copilot cuenta con la certificación ISO 42001 ([ficha de IA responsable](https://learn.microsoft.com/en-us/copilot/security/security-copilot-application-card-agents), [conceptos de agentes](https://learn.microsoft.com/en-us/copilot/security/agents-overview)). Las cifras de Microsoft —6,5 veces más alertas maliciosas identificadas y 77 % más de precisión en evaluaciones controladas— son una referencia, no tu meta ([Ignite 2025](https://techcommunity.microsoft.com/blog/MicrosoftDefenderforOffice365Blog/microsoft-ignite-2025-transforming-phishing-response-with-agentic-innovation/4470791)).

**¿Tienes poco tiempo?**

- [Security Copilot agents in Microsoft 365 E5](https://www.microsoft.com/en-us/security/security-copilot-in-microsoft-365-e5) · Documentación
- [Microsoft Security Copilot Security Alert Triage Agent in Microsoft Defender (Preview)](https://learn.microsoft.com/en-us/defender-xdr/security-alert-triage-agent) · Documentación
- [What's new in Microsoft Security Copilot?](https://learn.microsoft.com/en-us/copilot/security/whats-new-copilot-security) · Documentación
- [Microsoft Security Copilot Dynamic Threat Detection Agent](https://learn.microsoft.com/en-us/defender-xdr/dynamic-threat-detection-agent) · Documentación

**Agentes de Security Copilot en Defender XDR (noviembre de 2026)**

| Agente | Qué hace | Estado | Costo | Requisitos y notas | Fuente |
|---|---|---|---|---|---|
| Security Alert Triage Agent | Clasifica alertas con razonamiento transparente y aprende de tu retroalimentación en el correo | GA para correos reportados por usuarios; vista previa para alertas de nube, contenedores e identidad | Consume SCU | RBAC unificado activo; desactivar las reglas de ajuste que resuelven solas sus alertas; permisos de mínimo privilegio desde junio de 2026 | [Agente de triage](https://learn.microsoft.com/en-us/defender-xdr/security-alert-triage-agent) |
| Dynamic Threat Detection Agent | Correlaciona alertas, eventos, anomalías e inteligencia para generar alertas dinámicas con MITRE y pasos de remediación, sin configuración | Vista previa, siempre activo | Gratis en vista previa; consumirá SCU en GA | Fuentes comunitarias difieren sobre su GA; prevalece Learn | [DTDA](https://learn.microsoft.com/en-us/defender-xdr/dynamic-threat-detection-agent) |
| Threat Hunting Agent | Convierte preguntas en lenguaje natural en KQL, ejecuta la consulta, explica la lógica y sugiere seguimientos | Vista previa | Consume SCU | Se usa desde la búsqueda avanzada | [Threat Hunting Agent](https://learn.microsoft.com/en-nz/defender-xdr/advanced-hunting-security-copilot-threat-hunting-agent) |
| Security Analyst Agent | Análisis de varios pasos sobre Defender XDR, Sentinel o el data lake para priorizar riesgos con evidencia y visualizaciones | Vista previa pública desde abril de 2026 | Consume SCU | Se configura con la identidad del usuario; alterna con el Threat Hunting Assistant | [Security Analyst Agent](https://learn.microsoft.com/en-us/defender-xdr/security-analyst-agent) |
| Threat Intelligence Briefing Agent | Prepara informes de inteligencia de amenazas relevantes para la organización | GA según las noticias mensuales de enero de 2026 | Consume SCU | Útil para el hunting guiado por inteligencia del módulo A3 | [Noticias mensuales](https://techcommunity.microsoft.com/tag/ninja%20training) |
| Identity Risk Management Agent (Entra) | Investiga usuarios en riesgo, resume hallazgos y sugiere remediaciones con aprobación manual | Vista previa | Consume SCU | Entra ID P2; hasta 100 usuarios por ejecución; solo usuarios; sin remediación automática | [Agente de riesgo de identidad](https://learn.microsoft.com/en-us/entra/id-protection/identity-risk-management-agent-get-started) |
| Project Perception | Sistema multiagente para el SOC agéntico; no confundir con el agente de triage de Defender | Vista previa limitada por invitación, anunciada en julio de 2026 | No consta | Requiere invitación; revisa su estado después de Ignite | [Triage Agent de Perception](https://learn.microsoft.com/en-us/security/agentic-security/triage-agent) |

Estados al 6 de noviembre de 2026; Microsoft Ignite (17 al 20 de noviembre de 2026) puede cambiarlos. Inclusión en E5: 400 SCU al mes por cada 1.000 licencias pagas, hasta 10.000 ([Security Copilot en E5](https://www.microsoft.com/en-us/security/security-copilot-in-microsoft-365-e5)). Los agentes se profundizan en el programa de Security Copilot. «No consta» significa que la investigación no encontró una fuente oficial.

### Documentación, cursos y credenciales

- [What's new in Microsoft Security Copilot?](https://learn.microsoft.com/en-us/copilot/security/whats-new-copilot-security) · Documentación · Oficial · Microsoft Learn · abr 2026. Cronología oficial de Security Copilot: inclusión en M365 E5 y 12 agentes Microsoft nuevos (nov-2025), Security Analyst Agent en preview (abr-2026), integración con data lake y MCP (sep-2025).
- [MC1261596 - Notice: Security Copilot will be included as part of your Microsoft 365 E5 plan soon](https://mc.merill.net/message/MC1261596) · Documentación · Oficial · Microsoft (Message Center) · Microsoft 365 Message Center Archive (merill.net) · 25 mar 2026. Aviso del Message Center: Security Copilot se incluye en Microsoft 365 E5 con despliegue por fases del 20-abr al 30-jun-2026, 400 SCU por 1.000 usuarios y costos extra para capacidades fuera del núcleo.
- [Security Copilot agents in Microsoft 365 E5](https://www.microsoft.com/en-us/security/security-copilot-in-microsoft-365-e5) · Documentación · Oficial · Microsoft Security · nov 2025. Página oficial del beneficio: clientes elegibles de Microsoft 365 E5 reciben 400 SCU/mes por cada 1.000 licencias (máximo 10.000 SCU/mes) y agentes de Security Copilot en Defender, Entra, Intune y Purview sin costo adicional.
- [Microsoft Security Copilot Security Alert Triage Agent in Microsoft Defender (Preview)](https://learn.microsoft.com/en-us/defender-xdr/security-alert-triage-agent) · Documentación · Oficial · Vista previa · Microsoft Learn. Documenta el agente autónomo de triage (antes Phishing Triage Agent): GA para correos reportados por usuarios y preview para alertas de nube/contenedores e identidad, con razonamiento transparente y aprendizaje por feedback. *Nota:* Requiere SCU de Security Copilot, RBAC unificado activo y desactivar reglas de ajuste que auto-resuelvan las alertas a triar; el feedback solo aplica a alertas de correo
- [Microsoft Security Copilot Dynamic Threat Detection Agent](https://learn.microsoft.com/en-us/defender-xdr/dynamic-threat-detection-agent) · Documentación · Oficial · Vista previa · Microsoft Learn · 23 feb 2026. Agente siempre activo que correlaciona alertas, eventos, anomalías e inteligencia para generar alertas dinámicas (fuente 'Security Copilot') con MITRE y pasos de remediación, sin configuración. *Nota:* Gratis en preview; consumirá SCU al llegar a GA (fuentes comunitarias apuntan a GA a finales de 2026, no confirmado oficialmente)
- [Microsoft Security Copilot Threat Hunting Agent in advanced hunting (preview)](https://learn.microsoft.com/en-nz/defender-xdr/advanced-hunting-security-copilot-threat-hunting-agent) · Documentación · Oficial · Vista previa · Microsoft Learn. Agente conversacional de hunting que convierte preguntas en lenguaje natural en KQL, ejecuta la consulta, explica la lógica y sugiere seguimientos y acciones. *Nota:* URL en variante regional en-nz (contenido en inglés idéntico)
- [Microsoft Security Copilot Security Analyst Agent overview](https://learn.microsoft.com/en-us/defender-xdr/security-analyst-agent) · Documentación · Oficial · Vista previa · Microsoft Learn. Agente de análisis multi-paso (Python) sobre Defender XDR, Sentinel Log Analytics o data lake para priorizar riesgos con evidencia, visualizaciones y conversación. *Nota:* Preview pública desde marzo/abril-2026; se configura por identidad del usuario; alterna con el Threat Hunting Assistant
- [GenAI-Driven Threat Detection with Microsoft Security Copilot (arXiv 2605.20896)](https://arxiv.org/abs/2605.20896) · Documentación · Empleado de Microsoft · Nuevo · Scott Freitas, Amir Gharib · arXiv · 22 may 2026. Paper de Microsoft Security Research con métricas de producción del Dynamic Threat Detection Agent: 80,1% de precisión en 120 días y alertas nuevas en ~15% de incidentes investigados.
- [Triage Agent (Project Perception)](https://learn.microsoft.com/en-us/security/agentic-security/triage-agent) · Documentación · Oficial · Vista previa · Microsoft Learn. Describe el Triage Agent dentro de Project Perception, sistema multi-agente de Microsoft para SOC agéntico, hoy en Limited Public Preview por invitación. *Nota:* Project Perception se anunció en jul-2026; no confundir con el Security Alert Triage Agent embebido en Defender

### Webinars, videos y podcasts

- [Fight AI with AI | Multi-Agent Security Defense (Project Perception)](https://www.youtube.com/watch?v=afXHGzGNAtM) · Video · Empleado de Microsoft · Vista previa · Nuevo · Dave Weston · YouTube - Microsoft Mechanics · oct 2026. Demo de Project Perception con agentes rojo, azul y verde que confirman vulnerabilidades alcanzables, crean detecciones KQL y remedian con aprobación humana. *Nota:* Project Perception en Limited Public Preview por invitación
- [Agent 365 | Security Operations in Defender](https://www.youtube.com/watch?v=DMzkIq_DzhE) · Video · Empleado de Microsoft · Nuevo · Spencer Berg · YouTube - Microsoft Mechanics · jul 2026. Muestra cómo el SOC investiga agentes de IA en Defender: inventario unificado, bloqueo en tiempo real, revocación con acceso condicional y hunting de agentes sobreprivilegiados.

### Comunidad: blogs, libros, newsletters y eventos

- [Operational Notes on Microsoft Security Copilot Agents in Defender XDR and Microsoft Entra ID](https://techcommunity.microsoft.com/discussions/microsoftthreatprotection/operational-notes-on-microsoft-security-copilot-agents-in-defender-xdr-and-micro/4525826) · Blog · Comunidad · Nuevo · klianos · Microsoft Tech Community (foro) · 5 jun 2026. Notas operativas de los agentes en Defender: identidades agénticas, roles URBAC creados automáticamente, monitoreo de uso de SCU y consultas KQL sobre CloudAppEvents.
- [Security Copilot Agents in Defender XDR: where things actually stand](https://techcommunity.microsoft.com/discussions/microsoft-security/security-copilot-agents-in-defender-xdr-where-things-actually-stand/4514689) · Blog · Comunidad · Marcel Graewer · Microsoft Tech Community (foro) · 25 abr 2026. Análisis comunitario del estado GA/preview de los agentes de Defender y de la inclusión en E5 (400 SCU/1.000 licencias, sin rollover, 6 USD/SCU de excedente) con consejos operativos.

**Manos a la obra**

1. `Laboratorio parcial` Usa Security Copilot integrado en el portal de Defender: resumen de un incidente, respuesta guiada, análisis de un script y una consulta KQL generada desde lenguaje natural. Limitación: la prueba de E5 no incluye SCU; crea una capacidad temporal de 1 SCU como indica el anexo ([incorporación manual](https://learn.microsoft.com/en-us/copilot/security/manual-onboarding)) y bórrala al terminar, porque se factura por hora. Evidencia: las cuatro salidas y tu validación de cada una.
2. `Laboratorio parcial` Habilita el Security Alert Triage Agent para correos reportados ([agente de triage](https://learn.microsoft.com/en-us/defender-xdr/security-alert-triage-agent)); requiere SCU, MDO P2, RBAC unificado y la política de correos reportados por usuarios. Limitación: la inclusión de E5 no aplica a licencias de prueba. En producción, empieza con un grupo piloto de usuarios que reportan, revisa los veredictos y da retroalimentación antes de confiar en cierres automáticos. Evidencia: tres veredictos revisados con tu retroalimentación.
3. `Laboratorio` Calcula las SCU incluidas para tu organización y el consumo esperado de los agentes que planeas activar, y define la capacidad y el límite de excedente ([uso de SCU](https://learn.microsoft.com/en-us/copilot/security/manage-usage)). Evidencia: hoja de cálculo con supuestos y umbrales de alerta.
4. `Laboratorio` Completa para tu organización la tabla de agentes de este módulo con estado, costo, identidad, permisos, aprobación requerida y dueño de cada agente. Evidencia: registro de agentes aprobado por el líder del SOC.
5. `Laboratorio` Escribe la política de supervisión humana: decisiones que nunca se delegan (por ejemplo, deshabilitar cuentas ejecutivas o borrar datos), umbrales de aprobación, botón de apagado y revisión semanal de la retroalimentación, con apoyo de la [ficha de IA responsable](https://learn.microsoft.com/en-us/copilot/security/security-copilot-application-card-agents). Evidencia: política de una página.
6. `Solo producción` Mide el valor de los agentes en producción: concordancia con los veredictos de los analistas en una muestra, tiempo ahorrado y SCU consumidas. Requiere volumen real y la inclusión de E5 activa. Cómo hacerlo seguro: alcance piloto, identidad de agente de solo lectura, aprobación manual de cada recomendación, excedente limitado y revisión semanal del consumo.

**¿Quieres profundizar?**

- [Fight AI with AI | Multi-Agent Security Defense (Project Perception)](https://www.youtube.com/watch?v=afXHGzGNAtM) · Video

<a id="a7"></a>

## A7 · Multi-inquilino, MSSP y Defender Experts

*L400 · ~6 h · Origen: Ninja oficial de Defender XDR, Fundamentals (partners) e Intermediate (Defender Experts for XDR, hoy Defender Experts MDR)*

Muchas organizaciones de MCSA operan varios inquilinos —por país, por empresa del grupo o por fusiones— y muchas tercerizan parte del SOC. La **gestión multi-inquilino** (MTO) del portal de Defender unifica incidentes, alertas, casos, búsqueda avanzada, reglas de detección y gestión de vulnerabilidades de hasta 100 inquilinos, con grupos de inquilinos y acceso por **GDAP** o **Entra B2B** para datos de Defender y solo por B2B para datos de Sentinel; las consultas entre workspaces usan Azure Lighthouse.

Del lado de los servicios, **Defender Experts** es la familia de servicios gestionados de Microsoft: **MDR** Plan 1 (antes Defender Experts for XDR) para cargas de Defender y Plan 2 con telemetría de terceros en Sentinel, **Hunting** para XDR y servidores, **for Servers**, **Threat Intelligence** e **Incident Response**, que requiere contrato aparte. Ninguno está incluido en Microsoft 365 E5. Este módulo te ayuda a diseñar el modelo de acceso y a decidir qué tercerizar.

**Por qué importa**

Un modelo multi-inquilino mal diseñado multiplica cuentas privilegiadas y deja zonas sin monitoreo; uno bien diseñado da visibilidad central con mínimo privilegio. Y decidir con criterio qué tercerizar —cobertura nocturna, caza experta, respuesta a incidentes mayores— permite que el SOC interno se concentre en lo que solo él puede aportar: el contexto del negocio.

**Qué vas a lograr**

- Diseñar el acceso multi-inquilino con GDAP o B2B y mínimo privilegio.
- Operar incidentes y búsqueda avanzada entre inquilinos.
- Comparar los servicios de Defender Experts y sus planes.
- Definir RACI, SLA y métricas compartidas con un MSSP o un MDR.

> **Atención.** La gestión multiinquilino (MTO) usa GDAP o Entra B2B para los datos de Defender, solo B2B para los de Sentinel (sin GDAP) y Azure Lighthouse para las consultas entre workspaces; admite hasta 100 inquilinos y grupos de inquilinos, y Microsoft recomienda confiar en la MFA entre inquilinos para no perder datos ([requisitos de MTO](https://learn.microsoft.com/en-us/defender-xdr/mto-requirements), [MTO](https://learn.microsoft.com/en-us/defender-xdr/mto-overview)).

> **Qué cambió.** Defender Experts MDR Plan 1 es el antiguo Defender Experts for XDR y cubre las cargas de Defender; el Plan 2 suma telemetría de terceros a través de Sentinel. El enriquecimiento con señales de red de terceros del Plan 1 quedó obsoleto el 1 de septiembre de 2026 ([Defender Experts MDR](https://learn.microsoft.com/en-us/defender-xdr/defender-experts/defender-experts-mdr-overview)), y las páginas comerciales todavía usan el nombre anterior.

> **Novedad.** La familia Defender Experts reúne MDR, Hunting (XDR y Servers), Defender Experts for Servers, Threat Intelligence y Cybersecurity Incident Response; se vende por separado de las licencias de Defender y la respuesta a incidentes requiere un contrato aparte ([Defender Experts](https://learn.microsoft.com/en-us/defender-xdr/defender-experts/defender-experts-overview)). Los servicios de inteligencia y MDR se ampliaron en julio de 2026 ([novedades de julio](https://www.microsoft.com/en-us/security/blog/2026/07/30/whats-new-in-microsoft-security-july-2026/)).

> **Consejo Ninja.** Si eres proveedor de servicios, Microsoft publica una guía para implementar el modelo MSSP en el portal de Defender: multiinquilino, distribución de contenido y operación diaria ([guía MSSP](https://learn.microsoft.com/en-us/defender-xdr/playbook-managed-security)). Valida el soporte de GDAP en cada función antes de diseñar el acceso (ver [Metodología y fuentes](08_Cierre_glosario_y_fuentes.md#metodologia)).

**¿Tienes poco tiempo?**

- [Microsoft Defender multitenant management](https://learn.microsoft.com/en-us/defender-xdr/mto-overview) · Documentación
- [Set up Microsoft Defender multitenant management](https://learn.microsoft.com/en-us/defender-xdr/mto-requirements) · Documentación
- [Microsoft Defender Experts overview](https://learn.microsoft.com/en-us/defender-xdr/defender-experts/defender-experts-overview) · Documentación
- [What is Microsoft Defender Experts MDR?](https://learn.microsoft.com/en-us/defender-xdr/defender-experts/defender-experts-mdr-overview) · Documentación

**Acceso multiinquilino por tipo de dato**

| Necesidad | Mecanismo | Notas |
|---|---|---|
| Incidentes, alertas y búsqueda avanzada de Defender XDR de cada cliente | GDAP o Entra B2B | Hasta 100 inquilinos; conviene confiar en la MFA entre inquilinos para no perder datos |
| Datos de Microsoft Sentinel de cada cliente | Solo Entra B2B | GDAP no está soportado para Sentinel |
| Consultas entre workspaces de varios clientes | Azure Lighthouse | Complementa a la gestión multiinquilino en el SIEM |
| Organizar clientes por región, contrato o nivel de servicio | Grupos de inquilinos | Útil para un MSSP con clientes en varios países |
| Contenido común (detecciones y playbooks) y operación diaria | Guía MSSP del portal de Defender | Define la distribución de contenido antes de sumar clientes |

Fuentes: [requisitos de MTO](https://learn.microsoft.com/en-us/defender-xdr/mto-requirements), [gestión multiinquilino](https://learn.microsoft.com/en-us/defender-xdr/mto-overview) y [guía MSSP](https://learn.microsoft.com/en-us/defender-xdr/playbook-managed-security).

### Documentación, cursos y credenciales

- [Microsoft Defender multitenant management](https://learn.microsoft.com/en-us/defender-xdr/mto-overview) · Documentación · Oficial · Microsoft Learn. Vista unificada multi-inquilino de incidentes, alertas, casos, hunting, reglas de detección y DVM para SOC y MSSP, incluyendo grupos de tenants y workspaces de Sentinel.
- [Set up Microsoft Defender multitenant management](https://learn.microsoft.com/en-us/defender-xdr/mto-requirements) · Documentación · Oficial · Microsoft Learn. Requisitos de MTO: acceso por GDAP o Entra B2B a datos de Defender, B2B (no GDAP) para datos de Sentinel, Azure Lighthouse para consultas cross-workspace y límite de 100 tenants.
- [Microsoft Defender Experts overview](https://learn.microsoft.com/en-us/defender-xdr/defender-experts/defender-experts-overview) · Documentación · Oficial · Microsoft Learn. Panorama de la suite Defender Experts: MDR (planes 1 y 2), Hunting (XDR y Servers), for Servers, Threat Intelligence y Cybersecurity Incident Response.
- [What is Microsoft Defender Experts MDR?](https://learn.microsoft.com/en-us/defender-xdr/defender-experts/defender-experts-mdr-overview) · Documentación · Oficial · Microsoft Learn. Explica Defender Experts MDR: Plan 1 (antes Defender Experts for XDR) para cargas de Defender y Plan 2 que extiende la cobertura a telemetría de terceros en Sentinel.
- [What is Microsoft Defender Experts Hunting offering](https://learn.microsoft.com/en-us/defender-xdr/defender-experts/defender-experts-hunting-overview) · Documentación · Oficial · Nuevo · Microsoft Learn · 1 jul 2026. Servicio de caza proactiva gestionada por Microsoft (Hunting - XDR y Hunting - Servers) con notificaciones como incidentes, 'Ask Defender Experts' e informes.

### Anuncios y blogs oficiales

- [Elevate your protection with expanded Microsoft Defender Experts coverage](https://techcommunity.microsoft.com/blog/microsoft-defender-experts/elevate-your-protection-with-expanded-microsoft-defender-experts-coverage/4439134) · Blog oficial · Empleado de Microsoft · Legado aún útil · Henry Yan, Sylvie Liu · Microsoft Tech Community (Microsoft Defender Experts Blog) · 4 ago 2025. Anuncio de la cobertura 24/7 de Defender Experts para servidores híbridos y multinube y del SKU independiente Defender Experts for Servers. *Nota:* El enriquecimiento con señales de Palo Alto/Zscaler/Fortinet que menciona fue declarado obsoleto en Plan 1 desde sep-2026 (ahora vía Plan 2 + Sentinel)

**Manos a la obra**

1. `Laboratorio` Diseña la matriz de acceso de un MSSP: por cliente y tipo de dato (Defender y Sentinel), mecanismo (GDAP, B2B o Lighthouse), roles, confianza de MFA entre inquilinos y baja del cliente ([requisitos de MTO](https://learn.microsoft.com/en-us/defender-xdr/mto-requirements)). Evidencia: matriz revisada por el responsable de identidad.
2. `Laboratorio` Redacta el RACI y los SLA con un proveedor de MDR: quién clasifica, quién contiene, quién comunica, tiempos de escalamiento y métricas compartidas como el MTTA nocturno y el cumplimiento del SLA. Evidencia: anexo operativo de dos páginas.
3. `Laboratorio` Compara los servicios de Defender Experts (MDR Plan 1 y Plan 2, Hunting, Servers, Threat Intelligence e Incident Response) con las brechas de tu SOC ([Defender Experts](https://learn.microsoft.com/en-us/defender-xdr/defender-experts/defender-experts-overview)). Evidencia: tabla comparativa con una recomendación.
4. `Laboratorio` Revisa el servicio de caza gestionada ([Defender Experts Hunting](https://learn.microsoft.com/en-us/defender-xdr/defender-experts/defender-experts-hunting-overview)) y define qué hallazgos esperarías y cómo entrarían en tu proceso de ingeniería de detección. Evidencia: flujo de integración de una página.
5. `Solo producción` Monta MTO con dos o más inquilinos mediante GDAP o B2B y Lighthouse. Requiere varios inquilinos con relación de partner o B2B y licencias reales. Cómo hacerlo seguro: empieza con roles de solo lectura (Security Reader) y un grupo de inquilinos piloto, y documenta la baja de accesos.
6. `Solo producción` Haz un ejercicio conjunto con tu proveedor de MDR sobre un incidente nocturno. Requiere el contrato y los equipos reales. Cómo hacerlo seguro: ejercicio solo de discusión, sin acciones sobre sistemas, con revisión de los tiempos del SLA y un plan de mejora compartido.

<a id="a8"></a>

## A8 · Proyecto integrador: de un phishing a la contención de identidad y endpoint

*L400 · ~14 h · Origen: Nuevo en esta edición (equivale a la evaluación práctica final)*

El cierre técnico del programa es un caso completo, basado en campañas reales documentadas por Microsoft en 2026: un **phishing AiTM** —un enlace en SharePoint o un supuesto «código de conducta»— roba la sesión de un usuario, el atacante crea reglas de buzón para ocultarse, intenta un fraude BEC y se mueve hacia un endpoint y hacia Active Directory. Tu trabajo es detectarlo, investigarlo, contenerlo en identidad, correo y endpoint, erradicarlo y documentarlo en tu laboratorio, con todo lo aprendido.

No se evalúa cuántas funciones usas sino el criterio: qué contener primero, por qué revocar sesiones no alcanza sin eliminar las reglas de buzón, qué automatizar y dónde poner a una persona, cómo se ve el incidente en Sentinel y qué le dirías al comité. El proyecto se organiza en fases con entregables verificables y produce un portafolio reutilizable: detecciones como código, playbook con aprobación, consultas de caza, informe técnico y resumen ejecutivo.

**Por qué importa**

Los incidentes reales cruzan dominios: correo, identidad y endpoint en la misma hora. Practicar el recorrido completo en un entorno controlado es la mejor forma de descubrir brechas de proceso, permisos y automatización antes de que las descubra un atacante, y de demostrar a la organización que el SOC puede contener un compromiso de identidad de punta a punta.

**Qué vas a lograr**

- Reproducir en laboratorio una cadena phishing → identidad → endpoint con detecciones verificables.
- Contener en el orden correcto: sesiones, reglas de buzón, credenciales y dispositivo.
- Automatizar los pasos repetibles con aprobación humana y reversión.
- Documentar el incidente con línea de tiempo, consultas, métricas y lecciones aprendidas.

> **Novedad.** Un caso real para inspirar el proyecto: en enero de 2026, Microsoft describió una campaña de AiTM que abusaba de SharePoint, creaba reglas de buzón y terminaba en BEC; la contención exigió revocar las cookies de sesión y eliminar las reglas, además de cambiar la contraseña ([caso de AiTM y BEC](https://www.microsoft.com/en-us/security/blog/2026/01/21/multistage-aitm-phishing-bec-campaign-abusing-sharepoint/)).

> **Novedad.** El 4 de mayo de 2026, Microsoft publicó la campaña «code of conduct»: phishing en varias etapas con AiTM contra más de 35.000 usuarios de 13.000 organizaciones, con consultas de hunting e indicadores que puedes adaptar ([caso «code of conduct»](https://www.microsoft.com/en-us/security/blog/2026/05/04/breaking-the-code-multi-stage-code-of-conduct-phishing-campaign-leads-to-aitm-token-compromise/)).

> **Consejo Ninja.** Usa el mapa de detección por paso —MDO, MDE, Entra ID Protection y Defender for Cloud Apps— para decidir qué evidencia esperas en cada etapa ([Zero Trust con Sentinel y Defender XDR](https://learn.microsoft.com/en-us/security/zero-trust/siem-xdr-implement)). El caso de Storm-1167 de 2023 definió la contención moderna: revocar sesiones y revertir los cambios en la MFA ([caso de 2023](https://www.microsoft.com/en-us/security/blog/2023/06/08/detecting-and-mitigating-a-multi-stage-aitm-phishing-and-bec-campaign/)).

> **Atención.** Ética del laboratorio: usa solo cuentas de prueba, Attack simulation training o infraestructura propia, nunca kits de phishing reales contra terceros ni datos de producción, y documenta cada acción. La interrupción automática no se puede forzar en el laboratorio: si no aparece, no es un fallo de tu proyecto.

**¿Tienes poco tiempo?**

- [Resurgence of a multi-stage AiTM phishing and BEC campaign abusing SharePoint](https://www.microsoft.com/en-us/security/blog/2026/01/21/multistage-aitm-phishing-bec-campaign-abusing-sharepoint/) · Blog oficial
- [Breaking the code: Multi-stage 'code of conduct' phishing campaign leads to AiTM token compromise](https://www.microsoft.com/en-us/security/blog/2026/05/04/breaking-the-code-multi-stage-code-of-conduct-phishing-campaign-leads-to-aitm-token-compromise/) · Blog oficial
- [Zero Trust security with Microsoft Sentinel and Defender XDR](https://learn.microsoft.com/en-us/security/zero-trust/siem-xdr-implement) · Documentación
- [Detecting and mitigating a multi-stage AiTM phishing and BEC campaign](https://www.microsoft.com/en-us/security/blog/2023/06/08/detecting-and-mitigating-a-multi-stage-aitm-phishing-and-bec-campaign/) · Blog oficial

### Documentación, cursos y credenciales

- [Zero Trust security with Microsoft Sentinel and Defender XDR](https://learn.microsoft.com/en-us/security/zero-trust/siem-xdr-implement) · Documentación · Oficial · Microsoft Learn · 12 feb 2025. Recorre un ataque típico (phishing, malware, robo de credenciales, movimiento lateral, exfiltración) indicando qué producto Defender detecta cada paso y cómo responder en el portal unificado.

### Anuncios y blogs oficiales

- [Breaking the code: Multi-stage 'code of conduct' phishing campaign leads to AiTM token compromise](https://www.microsoft.com/en-us/security/blog/2026/05/04/breaking-the-code-multi-stage-code-of-conduct-phishing-campaign-leads-to-aitm-token-compromise/) · Blog oficial · Oficial · Nuevo · Microsoft Defender Security Research Team y Microsoft Threat Intelligence · Microsoft Security Blog · 4 may 2026. Análisis de una campaña de phishing AiTM de abril de 2026 con detecciones de Defender, consultas de hunting e IOC listos para reproducir en laboratorio.
- [Resurgence of a multi-stage AiTM phishing and BEC campaign abusing SharePoint](https://www.microsoft.com/en-us/security/blog/2026/01/21/multistage-aitm-phishing-bec-campaign-abusing-sharepoint/) · Blog oficial · Oficial · Microsoft Defender Security Research Team · Microsoft Security Blog · 21 ene 2026. Caso real 2026 de phishing AiTM vía SharePoint seguido de reglas de buzón y BEC, con guía de mitigación que exige revocar cookies de sesión y eliminar reglas además de resetear contraseñas.
- [Detecting and mitigating a multi-stage AiTM phishing and BEC campaign](https://www.microsoft.com/en-us/security/blog/2023/06/08/detecting-and-mitigating-a-multi-stage-aitm-phishing-and-bec-campaign/) · Blog oficial · Oficial · Legado aún útil · Microsoft Threat Intelligence · Microsoft Security Blog · 8 jun 2023. Caso clásico de AiTM con proxy indirecto y BEC que enseña por qué hay que revocar sesiones y revertir cambios de MFA, además de resetear contraseñas. *Nota:* Usa nombres de 2023; la contención hoy se complementa con interrupción automática de ataques y Token Protection

**Manos a la obra**

1. `Laboratorio` Prepara el escenario: tres usuarios de prueba, el controlador de dominio con MDI, dos clientes con MDE, el workspace de [M8](02_Nivel_2_Intermedio.md#m8) y los playbooks de [A2](#a2). Escribe la hipótesis, los criterios de éxito y las reglas de ética del ejercicio. Evidencia: plan de prueba aprobado por tu líder.
2. `Laboratorio` Etapa de phishing: lanza una campaña de Attack simulation training con Credential Harvest a los tres usuarios, en la que uno ingresa sus credenciales, y caza la cadena en `EmailEvents` y `UrlClickEvents` ([AST](https://learn.microsoft.com/en-us/defender-office-365/attack-simulation-training-get-started)). Evidencia: consultas y primera parte de la línea de tiempo.
3. `Laboratorio` Etapa de identidad: desde la cuenta víctima inicia sesión por Tor para disparar una detección de ID Protection y crea una regla de buzón sospechosa. Evidencia: detección de riesgo, alerta de la regla y consulta en `EntraIdSignInEvents`.
4. `Laboratorio` Etapa de endpoint: en el equipo de la víctima, una VM aislada, ejecuta una prueba atómica de PowerShell codificado y verifica que la alerta se correlaciona en el mismo incidente. Evidencia: incidente con alertas de las tres etapas.
5. `Laboratorio` Contén en el orden correcto y mide los tiempos: revoca sesiones, deshabilita la cuenta, elimina reglas de buzón, restablece contraseña y métodos de MFA, aísla el equipo y elimina los correos de forma recuperable ([robo de tokens](https://learn.microsoft.com/en-us/security/operations/token-theft-playbook), [BEC](https://learn.microsoft.com/en-us/defender-office-365/responding-to-a-compromised-email-account)). Evidencia: historial del Action center con la hora de cada acción para calcular el MTTC.
6. `Laboratorio parcial` Automatiza los pasos repetibles con aprobación: una regla de automatización por etiqueta que lance Revoke-AADSignInSessions e Isolate-MDEMachine con tarjeta de aprobación en Teams y su reversión probada ([playbooks de Entra ID](https://github.com/Azure/Azure-Sentinel/tree/master/Solutions/Microsoft%20Entra%20ID/Playbooks)). Limitación: Logic Apps tiene costo, Teams requiere usuarios con licencia y la interrupción automática no se dispara en el laboratorio. Evidencia: ejecución aprobada y su reversión.
7. `Laboratorio` Documenta el caso: informe técnico (línea de tiempo, consultas, detecciones y brechas), métricas (MTTD aproximado, MTTA, MTTC y MTTR con su definición), lecciones aprendidas y un resumen ejecutivo de una página. Evidencia: los dos documentos y las detecciones nuevas en tu repositorio.
8. `Solo producción` Repite el caso como ejercicio de mesa con el negocio (Legal, Comunicaciones, mesa de ayuda y dueños de aplicaciones). Requiere personas reales y el contexto productivo. Cómo hacerlo seguro: ejercicio solo de discusión, sin cambios en sistemas, con informe posterior y tareas con dueño.

<a id="reto-avanzado"></a>

## Reto del nivel

**Respuesta automatizada con control humano, como código.** Toma el proyecto integrador [A8](#a8) y conviértelo en un paquete reutilizable: playbook de robo de tokens adaptado a tu organización, detecciones desplegadas como código desde tu repositorio, playbooks de contención con aprobación en Teams y reversión probada, scripts de Microsoft Graph para cazar y remediar, y la ficha de gobierno de los agentes que usarías. Valídalo con un ejercicio de purple team en el laboratorio y documenta pruebas, dueños y criterios de retiro de cada pieza.

<a id="quiz-avanzado"></a>

## Evaluación del nivel

Responde y compara con [Evaluaciones y respuestas](06_Evaluaciones_y_respuestas.md#eval-avanzado). Con 80 % o más, ¡nivel aprobado! (En la versión web puedes corregir en línea y generar tu certificado).

1. ¿Qué documento reemplazó en abril de 2025 a NIST SP 800-61 Rev. 2?
   - a) NIST CSF 1.1
   - b) ISO/IEC 27035
   - c) SP 800-61 Rev. 3, perfil comunitario del CSF 2.0
   - d) SP 800-84

2. Según el playbook de consentimiento de aplicaciones, ¿qué haces con una aplicación maliciosa confirmada?
   - a) La deshabilitas sin borrarla
   - b) La borras de inmediato
   - c) Solo cambias la contraseña del usuario que dio el consentimiento
   - d) La dejas activa para observar al atacante

3. En el portal de Defender, ¿cómo automatizas la respuesta a alertas de Defender XDR (no de Sentinel)?
   - a) Con una regla que use el disparador de alerta clásico
   - b) Con Microsoft incident creation rules
   - c) Con Fusion
   - d) Con el Enhanced Alert Trigger

4. ¿Hasta cuándo funciona la acción «Advanced Hunting» del conector de Logic Apps de Defender for Endpoint?
   - a) Hasta el 31 de marzo de 2027
   - b) Hasta el 1 de febrero de 2027; después hay que usar Microsoft Graph
   - c) Indefinidamente
   - d) Hasta el 15 de octubre de 2026

5. ¿Qué pasó con el portal independiente de Microsoft Defender Threat Intelligence?
   - a) Se retiró el 1 de agosto de 2026 y la inteligencia pública se ofrece sin costo adicional en Defender
   - b) Pasó a requerir una licencia premium por usuario
   - c) Se integró solo en Sentinel en el portal de Azure
   - d) Sigue igual que en 2024

6. ¿Qué requiere el hunting graph?
   - a) Solo una licencia de MDE P1
   - b) El data lake de Sentinel y permisos de lectura en Exposure Management
   - c) Un contrato de Defender Experts Hunting
   - d) Una capacidad dedicada de Security Copilot

7. ¿Qué API de Microsoft Graph quedó retirada el 15 de octubre de 2026?
   - a) alerts_v2
   - b) incidents
   - c) runHuntingQuery
   - d) La API heredada de alertas (/security/alerts)

8. ¿Qué permiso requiere analyzedEmail: remediate?
   - a) Mail.ReadWrite delegado
   - b) ThreatHunting.Read.All
   - c) SecurityAnalyzedMessage.ReadWrite.All de aplicación
   - d) CustomDetection.ReadWrite.All

9. Antes de una prueba de BAS contra Defender for Endpoint, ¿qué recomienda Microsoft?
   - a) Desactivar la protección contra alteraciones para que la herramienta funcione
   - b) Excluir la herramienta de BAS del antivirus
   - c) Poner ASR en Audit para no interferir
   - d) Protección contra alteraciones, ASR y network protection en bloqueo, protección en la nube activa y sin exclusiones para la herramienta

10. ¿Qué pasa con los cambios hechos en el portal a una detección gestionada desde Sentinel Repositories?
   - a) Se sincronizan de vuelta al repositorio
   - b) El repositorio los sobrescribe en el siguiente despliegue
   - c) Bloquean el despliegue
   - d) Se guardan como una nueva versión

11. ¿Cuál es el estado del Dynamic Threat Detection Agent según Learn en noviembre de 2026?
   - a) GA y consume SCU
   - b) Retirado
   - c) Vista previa gratuita que consumirá SCU al llegar a GA
   - d) Solo disponible dentro de Project Perception

12. ¿Qué requiere el Security Alert Triage Agent para clasificar alertas?
   - a) SCU de Security Copilot, el RBAC unificado activo y desactivar las reglas de ajuste que resuelven solas esas alertas
   - b) Solo una licencia de MDO Plan 1
   - c) Un workspace de Sentinel con UEBA
   - d) Un contrato de Defender Experts MDR

13. En la gestión multiinquilino de Defender, ¿cómo se accede a los datos de Microsoft Sentinel de los inquilinos gestionados?
   - a) Con GDAP
   - b) Con Entra B2B, porque GDAP no está soportado para Sentinel
   - c) Con una cuenta compartida
   - d) Con una clave de API

14. ¿Qué agrega Defender Experts MDR Plan 2 respecto del Plan 1?
   - a) Caza de amenazas en servidores
   - b) Respuesta a incidentes sin contrato aparte
   - c) Licencias de Microsoft 365 E5
   - d) Cobertura de telemetría de terceros a través de Sentinel

15. En el caso de AiTM y BEC que Microsoft publicó en enero de 2026, ¿qué exigió la contención además del cambio de contraseña?
   - a) Reinstalar todos los equipos de la organización
   - b) Desactivar Safe Links
   - c) Revocar las cookies de sesión y eliminar las reglas de buzón creadas por el atacante
   - d) Bloquear SharePoint para toda la organización

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

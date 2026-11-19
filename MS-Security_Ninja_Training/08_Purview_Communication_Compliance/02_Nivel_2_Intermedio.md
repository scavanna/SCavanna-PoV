# Nivel 2 · Intermedio · IA, barreras, privacidad e integración

*Microsoft Purview Communication Compliance e Information Barriers Ninja Training · Edición 2026*

[← Nivel 1 · Inicial](01_Nivel_1_Inicial.md) · [Índice del programa](README.md) · [Nivel 3 · Avanzado →](03_Nivel_3_Avanzado.md)

<a id="intermedio"></a>

Copilot y las apps de IA como canales (y su pago por uso), Information Barriers de punta a punta, privacidad y control de acceso, y la integración con Insider Risk Management y eDiscovery. Terminas con barreras de prueba verificadas y un circuito de escalamiento aprobado.

*L300 · 4 módulos · ~16 horas · 20 recursos*

**Módulos de este nivel:** [M1 Copilot y apps de IA](#m1) · [M2 Information Barriers](#m2) · [M3 Privacidad y roles](#m3) · [M4 Insider Risk y eDiscovery](#m4)

<a id="m1"></a>

## M1 · Communication Compliance para Copilot y la IA generativa

*L300 · ~4 h · Origen: Nuevo en esta edición (el Ninja oficial no cubre Copilot ni la IA)*

La IA generativa es el canal de comunicación que más creció. Communication Compliance detecta las interacciones de **Microsoft 365 Copilot y Copilot Chat** por su clase de elemento (`IPM.SkypeTeams.Message.Copilot.*`) y las evalúa con la plantilla de interacciones de Copilot, que aplica Prompt Shields a los prompts (intentos de jailbreak o de inyección) y Protected material a las respuestas (texto protegido por derechos de autor o de marca). Para Microsoft 365 Copilot no hay cargos de pago por uso, pero sí hace falta la licencia de Copilot además de E5 o Purview Suite.

Más allá de Microsoft 365, CC cubre tres categorías: otros Copilots (Copilot Studio, Copilot en Fabric y Security Copilot, este último con un permiso explícito para que Purview procese los datos), apps de IA empresariales registradas en Entra o conectadas —ChatGPT Enterprise y, desde agosto de 2026, Anthropic Claude Enterprise mediante un conector en vista previa— y otras apps de IA detectadas por navegador o red a partir del catálogo de IA generativa de Defender for Cloud Apps. Todas requieren pago por uso, con un medidor premium cuando aplicas los clasificadores de odio, autolesión, violencia, contenido sexual, Prompt Shields o material protegido.

Supervisar prompts es supervisar a personas que piensan en voz alta: la decisión necesita aprobación de Legal y privacidad, alcance piloto y seudonimización. Las políticas de un clic que crea DSPM para IA y la protección de las interacciones de Copilot se profundizan en el programa de DSPM y seguridad de datos para IA (módulos I2 y M1); los agentes de Foundry y Agent 365, en su módulo M2.

**Por qué importa**

Sin supervisión, el uso de la IA queda fuera del perímetro de conducta: jailbreaks, generación de contenido protegido o prompts con lenguaje de acoso no aparecen en ningún reporte. Con Communication Compliance sobre Copilot y otras IA, la organización demuestra control sobre un canal nuevo, con costos previsibles si diseña el alcance y elige a conciencia el medidor estándar o el premium.

**Qué vas a lograr**

- Crear una política para interacciones de Microsoft 365 Copilot y explicar sus requisitos de licencia.
- Distinguir las tres categorías de IA que no es de Microsoft 365 y su facturación por pago por uso.
- Estimar el costo mensual de una política de IA con los medidores estándar y premium.
- Definir los controles de privacidad y de aprobación previos a supervisar prompts.

> **Novedad.** Ignite 2024 (19 de noviembre de 2024) anunció CC para Security Copilot, Copilot en Fabric, Copilot Studio y ChatGPT Enterprise en vista previa, junto con los clasificadores Prompt Shields (solo prompts) y Protected material (solo respuestas) e indicadores de CC en Insider Risk ([anuncio](https://techcommunity.microsoft.com/blog/microsoft-security-blog/new-purview-communication-compliance-features-for-copilot-and-insider-risk-manag/4296775)). La documentación actual ya los trata como canales con pago por uso.

> **Novedad.** Desde agosto de 2026, la compatibilidad de Purview con Anthropic Claude Enterprise incluye Communication Compliance; el conector sigue en vista previa y requiere pago por uso, y DLP y etiquetas no aplican a esas interacciones ([Claude Enterprise](https://learn.microsoft.com/en-us/purview/ai-claude-enterprise), [novedades](https://learn.microsoft.com/en-us/purview/whats-new)). Algunas copias localizadas aún muestran CC como no compatible.

> **Atención.** Para Security Copilot, CC exige activar en Security Copilot el permiso para que Purview procese los datos, además del pago por uso ([Security Copilot](https://learn.microsoft.com/en-us/purview/ai-security-copilot)). Copilot en Fabric también requiere pago por uso, y otros Copilots de Fabric y Fabric Data Agent siguen en vista previa ([Copilot en Fabric](https://learn.microsoft.com/en-us/purview/ai-copilot-fabric)).

> **Atención.** Agentes: la descripción de servicio indica que las capacidades de Purview para agentes de Microsoft Foundry y apps de IA conectadas a Entra se soportan con Microsoft 365 E7 y Agent 365, mientras la página de canales trata las apps conectadas con pago por uso; confirma con tu equipo de licenciamiento qué aplica a CC ([descripción de servicio](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)).

**¿Tienes poco tiempo?**

- [Configure a Communication Compliance policy to detect generative AI interactions](https://learn.microsoft.com/en-us/purview/communication-compliance-copilot) · Documentación
- [New Purview Communication Compliance features for Copilot and Insider Risk Management](https://techcommunity.microsoft.com/blog/microsoft-security-blog/new-purview-communication-compliance-features-for-copilot-and-insider-risk-manag/4296775) · Blog oficial
- [Use Microsoft Purview to manage data security & compliance for Anthropic Claude (Enterprise)](https://learn.microsoft.com/en-us/purview/ai-claude-enterprise) · Documentación
- [Use Microsoft Purview to manage data security & compliance for Microsoft Security Copilot](https://learn.microsoft.com/en-us/purview/ai-security-copilot) · Documentación

### Documentación, cursos y credenciales

- [Configure a Communication Compliance policy to detect generative AI interactions](https://learn.microsoft.com/en-us/purview/communication-compliance-copilot) · Documentación · Oficial · Microsoft Learn. Cómo detectar prompts y respuestas en Microsoft 365 Copilot, agentes de Copilot Studio, apps de IA conectadas y otras apps de IA, con roles requeridos y remediación.
- [Use Microsoft Purview to manage data security & compliance for Microsoft 365 Copilot & Microsoft 365 Copilot Chat](https://learn.microsoft.com/en-us/purview/ai-m365-copilot) · Documentación · Oficial · Microsoft Learn. Matriz de capacidades de Purview para Copilot (incluye Communication Compliance) y políticas de un clic de DSPM for AI como 'Detect risky AI usage' y 'Unethical behavior in AI apps'.
- [Use Microsoft Purview to manage data security & compliance for Microsoft Security Copilot](https://learn.microsoft.com/en-us/purview/ai-security-copilot) · Documentación · Oficial · Microsoft Learn. Capacidades de Purview sobre interacciones con Security Copilot (DSPM, auditoría, clasificación, IRM, Communication Compliance, eDiscovery, DLM) y políticas de un clic en DSPM for AI.
- [Use Microsoft Purview to manage data security & compliance for Anthropic Claude (Enterprise)](https://learn.microsoft.com/en-us/purview/ai-claude-enterprise) · Documentación · Oficial · Vista previa · Nuevo · Microsoft Learn · ago 2026. Matriz de capacidades de Purview para Claude Enterprise vía conector (preview): auditoría, clasificación, IRM, Communication Compliance, eDiscovery, DLM y Compliance Manager; DLP y etiquetas no aplican. *Nota:* Requiere facturación pay-as-you-go; la compatibilidad con CC se añadió en agosto de 2026 (What's new). Algunas copias localizadas o espejos antiguos aún muestran CC como no compatible
- [Use Microsoft Purview to manage data security & compliance for Copilot in Fabric](https://learn.microsoft.com/en-us/purview/ai-copilot-fabric) · Documentación · Oficial · Microsoft Learn. Indica que Communication Compliance soporta interacciones de Copilot en Fabric (Power BI) y que requiere facturación pay-as-you-go.

### Anuncios y blogs oficiales

- [New Purview Communication Compliance features for Copilot and Insider Risk Management](https://techcommunity.microsoft.com/blog/microsoft-security-blog/new-purview-communication-compliance-features-for-copilot-and-insider-risk-manag/4296775) · Blog oficial · Empleado de Microsoft · Legado aún útil · Erica Toelle · Microsoft Tech Community · 19 nov 2024. Anuncio de Ignite 2024: cobertura de más apps de GenAI (Security Copilot, Copilot en Fabric, Copilot Studio, ChatGPT Enterprise) en preview, clasificadores Prompt Shields y Protected Material, políticas en DSPM for AI e indicadores de CC en Insider Risk. *Nota:* Varias funciones anunciadas en preview ya figuran en la documentación vigente; la IA no Microsoft 365 hoy requiere pay-as-you-go

**Manos a la obra**

1. `Laboratorio parcial` Crea la política «Detect Microsoft 365 Copilot and Microsoft 365 Copilot Chat interactions» para un grupo piloto. Limitación: el análisis de Copilot requiere licencias de Microsoft 365 Copilot, que la prueba de E5 no incluye. Práctica segura en producción: aplícala solo a cuentas de prueba con Copilot y a revisores Analyst con seudonimización, con aprobación previa de Legal y privacidad ([IA generativa](https://learn.microsoft.com/en-us/purview/communication-compliance-copilot), [descripción de servicio](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)).
2. `Laboratorio parcial` Habilita el pago por uso con una suscripción de Azure del mismo tenant (crédito de Visual Studio Enterprise, sin garantía de que cubra los medidores de Purview) y agrega «Other AI apps» o Copilot Studio a una política piloto. Limitaciones: genera costos por registro de texto y requiere actividad real de navegador o de dispositivos incorporados. Práctica segura: presupuesto y alertas de costo en Azure, alcance mínimo, y pausa o eliminación de la política como reversión ([modelos de facturación](https://learn.microsoft.com/en-us/purview/purview-billing-models), [canales](https://learn.microsoft.com/en-us/purview/communication-compliance-channels)).
3. `Laboratorio` Estima el costo mensual de supervisar los prompts de un agente de Copilot Studio con el medidor estándar frente al premium, con tus supuestos de volumen y longitud, y documenta qué clasificadores activan el premium ([modelos de facturación](https://learn.microsoft.com/en-us/purview/purview-billing-models)).
4. `Laboratorio` Redacta la ficha de aprobación para supervisar prompts de IA: finalidad, población, canales, clasificadores, seudonimización, conservación, costos y responsables; preséntala en una revisión simulada con Legal y privacidad ([IA generativa](https://learn.microsoft.com/en-us/purview/communication-compliance-copilot)).
5. `Laboratorio` Revisa la matriz de capacidades de Purview para Microsoft 365 Copilot e identifica qué políticas de un clic de DSPM para IA crean políticas de CC; anota cuáles mantendrías y con qué alcance ([Purview para Copilot](https://learn.microsoft.com/en-us/purview/ai-m365-copilot)).
6. `Solo producción` Supervisa interacciones con Security Copilot o con Claude Enterprise. Por qué: requiere licencias pagas de Security Copilot o un contrato de Claude Enterprise, el permiso de procesamiento para Purview o el conector en vista previa, y pago por uso. Práctica segura: alcance de 2 a 5 cuentas de prueba, presupuesto de Azure con alertas al 50, 75 y 90 %, revisión de costos a las 48 horas y desactivación de la política o del conector como reversión ([Security Copilot](https://learn.microsoft.com/en-us/purview/ai-security-copilot), [Claude Enterprise](https://learn.microsoft.com/en-us/purview/ai-claude-enterprise)).

<a id="m2"></a>

## M2 · Information Barriers: segmentos, políticas, modos y verificación

*L300 · ~6 h · Origen: Nuevo en esta edición (Information Barriers no tiene un Ninja oficial propio)*

Information Barriers (IB) impide que grupos que no deben comunicarse —por ejemplo, Investigación y Banca de Inversión, o dos equipos que atienden a clientes en competencia— se encuentren, chateen, llamen, se reúnan, compartan pantalla o colaboren en archivos. La restricción es **bidireccional** y aplica en Teams, SharePoint y OneDrive, y en Planner solo para planes básicos. **No restringe el correo de Exchange Online**: para eso se usan reglas de flujo de correo. Se diseña con segmentos basados en atributos de directorio, como Department, y con políticas de bloqueo o de permiso.

Hay tres modos: Legacy (un segmento por usuario y hasta 250 segmentos, y hay que eliminar antes las directivas de libreta de direcciones existentes), segmento único y multisegmento (hasta 10 segmentos por usuario y 5.000 en total, sin depender de las libretas de direcciones). En SharePoint y OneDrive, cada sitio tiene un modo —Open, Owner Moderated, Implicit (lo fija Teams) o Explicit— que gobierna acceso, uso compartido y membresía. La aplicación de políticas arranca en unos 30 minutos y procesa unos 5.000 usuarios por hora, y Teams necesita la búsqueda de directorio con ámbito.

Desde septiembre de 2026, el reporte de cumplimiento de políticas de IB detecta sitios, OneDrive y contenedores de SharePoint Embedded con segmentos incompatibles después de cambiar una política. Este módulo cubre el diseño, el despliegue por etapas, la verificación, la solución de problemas y la reversión.

**Por qué importa**

En el sector financiero y en cualquier organización con conflictos de interés estructurales, una barrera ética mal implementada es un hallazgo regulatorio, y una barrera demasiado amplia corta la colaboración del negocio. Information Barriers, bien diseñada y verificada con su reporte de cumplimiento, deja evidencia técnica de la separación y reduce el riesgo de filtraciones entre áreas.

**Qué vas a lograr**

- Explicar qué restringe Information Barriers, en qué aplicaciones y por qué no aplica al correo.
- Elegir entre los modos Legacy, segmento único y multisegmento.
- Definir segmentos y políticas bidireccionales y aplicarlos con PowerShell.
- Configurar y verificar los modos de sitio en SharePoint y OneDrive.
- Ejecutar el reporte de cumplimiento de IB y documentar la reversión.

> **Atención.** Information Barriers **no** restringe el correo de Exchange Online: para impedir correos entre segmentos usa reglas de flujo de correo (página actualizada el 17 de septiembre de 2026, [Information Barriers](https://learn.microsoft.com/en-us/purview/information-barriers)). Un libro de terceros de 2025 afirma lo contrario; prevalece la documentación oficial.

> **Novedad.** Septiembre de 2026: el reporte de cumplimiento de políticas de IB (`Start-SPOInformationBarriersPolicyComplianceReport`) cubre sitios, OneDrive y contenedores de SharePoint Embedded propiedad de usuarios, que se corrigen con `-UpdateUserOwnedContainerSegments`; solo hace falta después de cambiar políticas ([reporte de cumplimiento](https://learn.microsoft.com/en-us/purview/information-barriers-sharepoint-report)).

> **Consejo Ninja.** Planifica los tiempos: la aplicación de políticas arranca en unos 30 minutos y procesa unos 5.000 usuarios por hora; la búsqueda de directorio con ámbito de Teams necesita 24 horas según la guía de inicio y «algunas horas» según la página de Teams ([guía de inicio](https://learn.microsoft.com/en-us/purview/information-barriers-policies), [IB en Teams](https://learn.microsoft.com/en-us/purview/information-barriers-teams)).

> **Qué cambió.** En modo Legacy hay que eliminar las directivas de libreta de direcciones existentes antes de habilitar IB; en segmento único y multisegmento, IB ya no depende de ellas. Multisegmento admite hasta 10 segmentos por usuario y 5.000 en total; Legacy, un segmento por usuario y hasta 250 ([multisegmento](https://learn.microsoft.com/en-us/purview/information-barriers-multi-segment)).

**¿Tienes poco tiempo?**

- [Learn about Information Barriers](https://learn.microsoft.com/en-us/purview/information-barriers) · Documentación
- [Get started with Information Barriers](https://learn.microsoft.com/en-us/purview/information-barriers-policies) · Documentación
- [Use Information Barriers with SharePoint](https://learn.microsoft.com/en-us/purview/information-barriers-sharepoint) · Documentación
- [Create an Information Barriers policy compliance report](https://learn.microsoft.com/en-us/purview/information-barriers-sharepoint-report) · Documentación

**Modos de Information Barriers**

| Modo | Segmentos por usuario | Segmentos en total | Libretas de direcciones (ABP) | Cuándo considerarlo |
|---|---|---|---|---|
| Legacy | 1 | Hasta 250 | Hay que eliminar las ABP existentes antes de habilitar IB | Solo si ya lo usas; planifica la migración |
| Segmento único | 1 | Hasta 5.000 | IB no depende de las ABP | Cada persona pertenece a un solo grupo de conflicto |
| Multisegmento | Hasta 10 | Hasta 5.000 | IB no depende de las ABP | Personas que pertenecen a varios grupos (por ejemplo, un área y un proyecto) |

Fuentes: [Information Barriers](https://learn.microsoft.com/en-us/purview/information-barriers), [multisegmento](https://learn.microsoft.com/en-us/purview/information-barriers-multi-segment) y [guía de inicio](https://learn.microsoft.com/en-us/purview/information-barriers-policies). La columna «Cuándo considerarlo» es una orientación de esta guía.

### Documentación, cursos y credenciales

- [Create an Information Barriers policy compliance report](https://learn.microsoft.com/en-us/purview/information-barriers-sharepoint-report) · Documentación · Oficial · Nuevo · Microsoft Learn · sep 2026. Cómo ejecutar con SharePoint Online Management Shell el reporte de cumplimiento de políticas de IB que identifica sitios, OneDrive y contenedores SharePoint Embedded propiedad de usuarios con segmentos incompatibles tras cambiar políticas.
- [Learn about Information Barriers](https://learn.microsoft.com/en-us/purview/information-barriers) · Documentación · Oficial · Nuevo · Microsoft Learn · 17 sep 2026. Conceptos de Information Barriers: restricción bidireccional en Teams, SharePoint, OneDrive y Planner, sin efecto sobre correo, y diferencias de libretas de direcciones (ABP) entre modos Legacy y single/multi-segment.
- [Use multi-segment support in Information Barriers](https://learn.microsoft.com/en-us/purview/information-barriers-multi-segment) · Documentación · Oficial · Microsoft Learn. Explica el modo multisegmento: hasta 10 segmentos por usuario y 5.000 segmentos fuera del modo Legacy, políticas solo con lista de permitidos y ejemplo con PowerShell.
- [Information Barriers in Microsoft Teams](https://learn.microsoft.com/en-us/purview/information-barriers-teams) · Documentación · Oficial · Microsoft Learn. Comportamiento de IB en Teams (miembros, chats, reuniones, pantalla compartida, llamadas, canales privados y compartidos), rol IB Compliance Management y antecedente regulatorio FINRA 15-31.
- [Use Information Barriers with SharePoint](https://learn.microsoft.com/en-us/purview/information-barriers-sharepoint) · Documentación · Oficial · Microsoft Learn. Modos de IB para sitios (Open, Owner Moderated, Implicit, Explicit), su efecto en compartir, acceso y membresía, administración de segmentos con SharePoint PowerShell, auditoría y cómo suspender IB en SharePoint y OneDrive.
- [Get started with Information Barriers](https://learn.microsoft.com/en-us/purview/information-barriers-policies) · Documentación · Oficial · Microsoft Learn · 22 abr 2026. Guía de configuración en 7 pasos (prerrequisitos, segmentos, políticas block/allow, aplicación, SharePoint/OneDrive, modos, descubribilidad) con referencia completa de cmdlets de PowerShell.
- [Resolve communication issues in Information Barriers](https://learn.microsoft.com/en-us/troubleshoot/microsoft-365/purview/information-barriers/information-barriers-troubleshooting) · Documentación · Oficial · Microsoft Learn (Troubleshooting) · 5 may 2025. Guía de solución de problemas de IB: usuarios bloqueados o no bloqueados en Teams, quitar un usuario de una política, aplicación lenta o no aplicada, con cmdlets de diagnóstico.

**Manos a la obra**

1. `Laboratorio` Diseña en papel la matriz de segmentos y políticas para un caso (Investigación, Banca de Inversión, Ventas y Legal): atributo de directorio, modo elegido (por ejemplo, multisegmento) y políticas de bloqueo o permiso; justifica por qué el correo se resuelve con reglas de flujo ([Information Barriers](https://learn.microsoft.com/en-us/purview/information-barriers), [multisegmento](https://learn.microsoft.com/en-us/purview/information-barriers-multi-segment)).
2. `Laboratorio parcial` Configura IB de prueba: segmentos por Department en cuentas de prueba, políticas de bloqueo bidireccionales y `Start-InformationBarriersPoliciesApplication`; valida búsqueda, chat y llamadas en Teams. Limitaciones: esperas de hasta 24 horas para la búsqueda de directorio con ámbito y procesamiento por lotes, y necesitas varios usuarios con licencia para probar ambos sentidos. Práctica segura en producción: modela primero en el laboratorio, usa segmentos piloto y deja documentada la reversión ([guía de inicio](https://learn.microsoft.com/en-us/purview/information-barriers-policies)).
3. `Laboratorio parcial` Crea sitios de SharePoint en modo Owner Moderated y Explicit, intenta compartir con un usuario de un segmento bloqueado y verifica que los vínculos «Cualquier persona» y «Toda la empresa» quedan deshabilitados. Limitación: requiere IB habilitada en SharePoint y OneDrive y tiempo de procesamiento, con pocos usuarios de prueba ([IB en SharePoint](https://learn.microsoft.com/en-us/purview/information-barriers-sharepoint)).
4. `Laboratorio parcial` Tras modificar una política en el tenant de prueba, ejecuta el reporte de cumplimiento de IB y corrige los segmentos de OneDrive con `-UpdateOneDriveSegments`; guarda el reporte como evidencia. Limitación: necesitas IB ya configurada con segmentos de prueba y SharePoint Online Management Shell, y el volumen de sitios del laboratorio es pequeño ([reporte de cumplimiento](https://learn.microsoft.com/en-us/purview/information-barriers-sharepoint-report)).
5. `Laboratorio parcial` Simula un usuario que no queda bloqueado y diagnostícalo con la guía de solución de problemas (`Get-InformationBarrierRecipientStatus` y `Get-ExoInformationBarrierRelationship`); documenta qué cmdlet te dio la respuesta. Limitación: necesitas varias cuentas con licencia y esperar la aplicación de políticas ([solución de problemas](https://learn.microsoft.com/en-us/troubleshoot/microsoft-365/purview/information-barriers/information-barriers-troubleshooting)).
6. `Solo producción` Despliega Information Barriers en toda la organización. Por qué: afecta a todos los usuarios, puede sacar personas de chats y equipos y cambia la libreta de direcciones. Práctica segura: inventario de libretas de direcciones, aprobación de cumplimiento, Legal y dueños de negocio, piloto por segmentos, comunicación previa, reporte de cumplimiento después de cada cambio y procedimiento documentado para suspender IB en SharePoint y OneDrive ([Information Barriers](https://learn.microsoft.com/en-us/purview/information-barriers), [IB en SharePoint](https://learn.microsoft.com/en-us/purview/information-barriers-sharepoint)).

<a id="m3"></a>

## M3 · Privacidad, seudonimización y control de acceso

*L300 · ~3 h · Origen: Ninja oficial de CC · Getting Started (privacidad y permisos)*

Communication Compliance e Insider Risk Management comparten un principio de **privacidad por diseño**: los nombres se seudonimizan por defecto, el acceso se controla con roles, el administrador debe optar explícitamente por cada función y todo queda auditado. Un administrador global no ve las alertas de CC si no tiene un rol de la solución. Los permisos se organizan en seis grupos de roles —entre ellos Communication Compliance, Communication Compliance Admins, Analysts, Investigators y Viewers—, que tardan hasta 30 minutos en aplicarse y deben asignarse con separación entre quien administra, quien analiza y quien investiga.

Para organizaciones con presencia en varios países de MCSA, las **unidades administrativas** de Entra limitan qué políticas y alertas ve un administrador o un revisor según su región o departamento, con dos matices: no aplican a los reportes y no se pueden combinar con ámbitos adaptables en CC. Las asignaciones con vencimiento (julio de 2026) completan el esquema para revisores temporales, y PIM para grupos, que se profundiza en el programa de Entra (módulo M3), agrega activación justo a tiempo. Lo que aprendas aquí es la base técnica de las decisiones de gobierno del track de operación.

**Por qué importa**

La confianza de los empleados y la defensa legal de la supervisión dependen de demostrar que solo personas autorizadas vieron solo lo necesario. Seudonimización, separación de funciones y unidades administrativas reducen el riesgo de abuso de privilegios, ayudan a cumplir los principios de minimización de las leyes de datos de la región y simplifican la revisión periódica de accesos.

**Qué vas a lograr**

- Describir los controles de privacidad por diseño de Communication Compliance y sus valores predeterminados.
- Asignar grupos de roles con separación entre administración, análisis e investigación.
- Acotar revisores por país o región con unidades administrativas y reconocer sus límites.
- Evitar el riesgo de quedarse sin administradores de la solución.

> **Consejo Ninja.** Privacidad por diseño: seudonimización por defecto, control de acceso por roles, opt-in explícito del administrador y registros de auditoría. Los administradores globales no tienen acceso por defecto a Communication Compliance ni a Insider Risk Management, y los indicadores vienen desactivados ([guía de privacidad](https://learn.microsoft.com/en-us/purview/insider-risk-solution-privacy)).

> **Atención.** Las unidades administrativas limitan las políticas y alertas que ve cada administrador o revisor, pero no aplican a los reportes y no se pueden combinar con ámbitos adaptables en CC ([permisos de CC](https://learn.microsoft.com/en-us/purview/communication-compliance-permissions), [reportes](https://learn.microsoft.com/en-us/purview/communication-compliance-reports-audits)).

> **Atención.** Evita quedarte sin administradores: la matriz de permisos advierte del riesgo de que la solución quede con «cero administradores». Los grupos de roles tardan hasta 30 minutos en aplicarse ([permisos en español](https://learn.microsoft.com/es-es/purview/communication-compliance-permissions)).

**¿Tienes poco tiempo?**

- [Microsoft Purview Insider Risk Management and Communication Compliance privacy guide](https://learn.microsoft.com/en-us/purview/insider-risk-solution-privacy) · Documentación
- [Assign permissions in Communication Compliance](https://learn.microsoft.com/en-us/purview/communication-compliance-permissions) · Documentación
- [Administrative units in Microsoft Purview](https://learn.microsoft.com/en-us/purview/purview-admin-units) · Documentación

### Documentación, cursos y credenciales

- [Assign permissions in Communication Compliance](https://learn.microsoft.com/en-us/purview/communication-compliance-permissions) · Documentación · Oficial · Microsoft Learn. Matriz de acciones por grupo de roles (Communication Compliance, Admins, Analysts, Investigators, Viewers), riesgo de 'cero administradores' y uso de unidades administrativas para acotar revisores por región o departamento.
- [Administrative units in Microsoft Purview](https://learn.microsoft.com/en-us/purview/purview-admin-units) · Documentación · Oficial · Microsoft Learn. Cómo las unidades administrativas de Entra restringen la gestión de políticas y la investigación de alertas de CC a usuarios de una región o departamento.
- [Microsoft Purview Insider Risk Management and Communication Compliance privacy guide](https://learn.microsoft.com/en-us/purview/insider-risk-solution-privacy) · Documentación · Oficial · Microsoft Learn. Guía de privacidad por diseño de IRM y CC: seudonimización, control de acceso por roles, opt-in explícito del administrador y registros de auditoría, con separación entre administradores e investigadores.

**Manos a la obra**

1. `Laboratorio` Asigna los grupos de roles con separación de funciones a tres cuentas de prueba (administrador, analista e investigador) y verifica con la matriz de acciones qué puede hacer cada una; guarda la tabla de resultados ([permisos de CC](https://learn.microsoft.com/en-us/purview/communication-compliance-permissions)).
2. `Laboratorio` Confirma que la seudonimización está activa, abre la misma alerta como analista y como investigador y documenta qué ve cada rol ([guía de privacidad](https://learn.microsoft.com/en-us/purview/insider-risk-solution-privacy), [configurar CC](https://learn.microsoft.com/en-us/purview/communication-compliance-configure)).
3. `Laboratorio` Crea dos unidades administrativas por país (por ejemplo, México y Chile) con cuentas de prueba, asigna un revisor a cada una y verifica que solo ve las alertas de su unidad; comprueba también que los reportes no se filtran ([unidades administrativas](https://learn.microsoft.com/en-us/purview/purview-admin-units)).
4. `Laboratorio` Revisa en el registro de auditoría qué acciones de revisión hizo cada cuenta durante la última semana y prepara el informe mensual de accesos para privacidad ([actividades de auditoría](https://learn.microsoft.com/en-us/purview/audit-log-activities)).
5. `Laboratorio` Documenta el procedimiento para evitar «cero administradores»: al menos dos administradores de la solución con asignación permanente, revisión trimestral y asignaciones con vencimiento para revisores temporales ([permisos en español](https://learn.microsoft.com/es-es/purview/communication-compliance-permissions)).

<a id="m4"></a>

## M4 · Integración con Insider Risk Management y eDiscovery

*L300 · ~3 h · Origen: Ninja oficial de CC · integración con otras herramientas (Insider Risk y eDiscovery Premium)*

Communication Compliance no trabaja sola. Cuando creas una política de Insider Risk Management (IRM) con las plantillas «Data leaks by risky users» o «Security policy violations by risky users» y eliges CC como desencadenante, se crea automáticamente la política **Insider risk trigger**, con los clasificadores Threat, Harassment y Discrimination: quien envíe 5 o más mensajes de riesgo en 24 horas entra en el alcance de IRM, algo que puede tardar hasta 48 horas. IRM también consume indicadores de CC: texto financiero de riesgo, imágenes y contenido inapropiado, tipos de información confidencial e indicadores de IA generativa como Prompt Shields y Protected material.

En el otro sentido, «Escalar para investigación» convierte una alerta de CC en un caso de eDiscovery (Premium) con hasta 100 mensajes, donde Legal preserva, revisa y exporta con cadena de custodia. Este módulo te enseña a conectar las piezas sin duplicar esfuerzos: el diseño de políticas e indicadores de IRM se profundiza en el programa de Insider Risk Management (módulos I2, M1 y M4) y la gestión de casos y la exportación, en el de eDiscovery y Audit (módulos M2 y M4).

**Por qué importa**

Las señales de conducta solas rara vez cuentan la historia completa. Integrar Communication Compliance con Insider Risk Management y eDiscovery permite priorizar a quienes combinan comunicaciones de riesgo con actividad sospechosa sobre los datos, y llevar la evidencia a un proceso legal controlado sin copiar mensajes a mano ni romper la cadena de custodia.

**Qué vas a lograr**

- Configurar el desencadenante de CC en una política de IRM y verificar la política Insider risk trigger.
- Identificar qué indicadores de CC consume IRM, incluidos los de IA generativa.
- Escalar una alerta a un caso de eDiscovery (Premium) y documentar el traspaso a Legal.
- Definir criterios de escalamiento acordados con RR. HH. y Legal.

> **Novedad.** Indicadores de CC disponibles en Insider Risk Management: texto financiero de riesgo, imágenes y contenido inapropiado, tipos de información confidencial e indicadores de IA generativa (Prompt Shields y Protected material); algunos indicadores de IRM requieren pago por uso ([indicadores de IRM](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-policy-indicators)).

> **Atención.** La política «Insider risk trigger» se crea automáticamente con Threat, Harassment y Discrimination. Como Discrimination solo funciona en inglés, en español el desencadenante depende sobre todo de Threat y Harassment. La persona entra en el alcance de IRM con 5 o más mensajes de riesgo en 24 horas, y puede tardar hasta 48 horas ([políticas](https://learn.microsoft.com/en-us/purview/communication-compliance-policies)).

> **Consejo Ninja.** El video de Microsoft Mechanics sobre riesgo interno y Communication Compliance tiene unos cuatro años y la interfaz cambió, pero sigue explicando bien la privacidad por diseño compartida ([Mechanics](https://www.youtube.com/watch?v=Ynkfu8OF0wQ)). Para decidir cuándo escalar señales de CC, revisa las plantillas de IRM ([plantillas de IRM](https://learn.microsoft.com/en-us/purview/insider-risk-management-policy-templates)).

**¿Tienes poco tiempo?**

- [Configure policy indicators in Insider Risk Management](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-policy-indicators) · Documentación
- [Manage Data Risks from Employee Insiders with Microsoft Purview (Microsoft Mechanics)](https://www.youtube.com/watch?v=Ynkfu8OF0wQ) · Video
- [Learn about Insider Risk Management policy templates](https://learn.microsoft.com/en-us/purview/insider-risk-management-policy-templates) · Documentación

### Documentación, cursos y credenciales

- [Configure policy indicators in Insider Risk Management](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-policy-indicators) · Documentación · Oficial · Microsoft Learn. Tipos de eventos e indicadores de IRM (desencadenantes, globales y de política), incluidos los que requieren pay-as-you-go, base para usar señales de Communication Compliance en Insider Risk.
- [Create and manage Insider Risk Management policies](https://learn.microsoft.com/en-us/purview/insider-risk-management-policies) · Documentación · Oficial · Microsoft Learn. Panel de políticas de IRM con políticas de usuario y de agente (Copilot Studio y Foundry) y la métrica 'Policy alert effectiveness' (alertas confirmadas sobre acciones tomadas).
- [Learn about Insider Risk Management policy templates](https://learn.microsoft.com/en-us/purview/insider-risk-management-policy-templates) · Documentación · Oficial · Microsoft Learn. Plantillas de IRM (robo de datos por empleados salientes, fugas de datos, etc.) y su relación con desencadenantes, útil para decidir cuándo escalar señales de CC a IRM.

### Webinars, videos y podcasts

- [Manage Data Risks from Employee Insiders with Microsoft Purview (Microsoft Mechanics)](https://www.youtube.com/watch?v=Ynkfu8OF0wQ) · Video · Oficial · Legado aún útil · Talhah Mir y Jeremy Chapman · Microsoft Mechanics (YouTube). Episodio oficial que muestra cómo IRM y Communication Compliance trabajan juntos con privacidad por diseño, incluido un segmento sobre cumplimiento de comunicaciones internas. *Nota:* Video de hace unos 4 años (fecha aproximada); la interfaz y los nombres de portal cambiaron, pero Learn aún lo enlaza como referencia de la integración IRM+CC

**Manos a la obra**

1. `Laboratorio parcial` Crea una política de IRM «Data leaks by risky users» con CC como desencadenante y verifica la política «Insider risk trigger» creada automáticamente. Limitación: para ver a una persona entrar en el alcance de IRM necesitas 5 o más mensajes de riesgo en 24 horas y esperar hasta 48 horas, y en español Discrimination no coincide. Práctica segura en producción: alcance piloto con cuentas de prueba y revisión humana obligatoria ([políticas](https://learn.microsoft.com/en-us/purview/communication-compliance-policies), [configurar IRM](https://learn.microsoft.com/en-us/purview/insider-risk-management-configure)).
2. `Laboratorio` Revisa la configuración de indicadores de IRM y marca cuáles provienen de CC, incluidos los de IA generativa; documenta cuáles habilitarías, con qué justificación y quién lo aprueba ([indicadores de IRM](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-policy-indicators)).
3. `Laboratorio` Escala una alerta de CC de prueba a investigación y abre el caso de eDiscovery (Premium) resultante; documenta qué mensajes llegaron y quién tiene acceso al caso ([investigar y remediar](https://learn.microsoft.com/en-us/purview/communication-compliance-investigate-remediate)).
4. `Laboratorio` Redacta los criterios de escalamiento de CC hacia IRM, RR. HH. y Legal (qué, cuándo y quién decide) y contrástalos con las plantillas de IRM y con el panel de políticas ([plantillas de IRM](https://learn.microsoft.com/en-us/purview/insider-risk-management-policy-templates), [políticas de IRM](https://learn.microsoft.com/en-us/purview/insider-risk-management-policies)).

<a id="reto-intermedio"></a>

## Reto del nivel

**Barrera ética y supervisión de IA con privacidad.** Implementa en el laboratorio una barrera entre dos segmentos de prueba (Investigación y Ventas) con modos de sitio verificados y el reporte de cumplimiento; diseña una política de CC para interacciones de IA (si no tienes Copilot, documenta el diseño y el costo estimado con pago por uso); configura unidades administrativas por país y el desencadenante de Insider Risk. Entrega la matriz de segmentos y políticas, la ficha de aprobación de la supervisión de IA y el circuito de escalamiento hacia IRM y eDiscovery.

<a id="quiz-intermedio"></a>

## Evaluación del nivel

Responde y compara con [Evaluaciones y respuestas](06_Evaluaciones_y_respuestas.md#eval-intermedio). Con 80 % o más, ¡nivel aprobado! (En la versión web puedes corregir en línea y generar tu certificado).

1. ¿Qué interacciones requieren habilitar el pago por uso en Communication Compliance?
   - a) Chats y canales de Teams con adjuntos
   - b) Microsoft 365 Copilot y Copilot Chat
   - c) Copilot Studio, Copilot en Fabric y Security Copilot
   - d) Viva Engage en modo nativo

2. ¿Qué detectan Prompt Shields y Protected material?
   - a) Ambos analizan solo correo de Exchange y sus adjuntos
   - b) Prompt Shields: jailbreak o inyección en prompts; Protected material: texto protegido en respuestas
   - c) Prompt Shields: imágenes en los prompts; Protected material: adjuntos de las respuestas
   - d) Ambos detectan lenguaje soez y amenazas en 12 idiomas

3. ¿Desde cuándo incluye la compatibilidad de Purview con Claude Enterprise a Communication Compliance, y en qué estado está el conector?
   - a) Desde mayo de 2026, con el conector en GA y sin pago por uso
   - b) Desde agosto de 2026; el conector sigue en vista previa y requiere pago por uso
   - c) Desde Ignite 2024, incluido en E5 sin pago por uso
   - d) No es compatible: Purview solo aplica DLP y etiquetas a Claude

4. ¿Qué paso adicional exige Communication Compliance para supervisar interacciones con Security Copilot?
   - a) Ninguno: basta con la licencia E5 de los usuarios
   - b) Una licencia de Microsoft 365 Copilot para cada analista del SOC
   - c) Un conector de partner aprovisionado con una entidad de servicio
   - d) Habilitar en Security Copilot el permiso para que Purview procese los datos, además del pago por uso

5. Un banco quiere impedir los correos entre Investigación y Banca de Inversión. ¿Qué usa?
   - a) Una política de Information Barriers
   - b) Reglas de flujo de correo de Exchange
   - c) Una política de Communication Compliance
   - d) Unidades administrativas

6. ¿Qué modo de IB en SharePoint fija Teams y no puede administrar el administrador de SharePoint?
   - a) Open
   - b) Owner Moderated
   - c) Implicit
   - d) Explicit

7. ¿Cuántos segmentos admite el modo multisegmento de Information Barriers?
   - a) Hasta 10 por usuario y 5.000 en total
   - b) Uno por usuario y 250 en total
   - c) Ilimitados por usuario y en total
   - d) Hasta 3 por usuario y 1.000 en total

8. ¿Qué cubre el reporte de cumplimiento de Information Barriers actualizado en septiembre de 2026?
   - a) Solo buzones de Exchange
   - b) Chats y reuniones de Teams
   - c) Sitios, OneDrive y contenedores de SharePoint Embedded propiedad de usuarios
   - d) Planes premium de Planner

9. ¿En qué aplicaciones restringe Information Barriers la comunicación y la colaboración?
   - a) Exchange Online, Outlook y Teams
   - b) Solo Teams, en chats y reuniones
   - c) Teams, Viva Engage y Exchange Online
   - d) Teams, SharePoint y OneDrive, y Planner solo en planes básicos

10. ¿Cuál es el comportamiento de privacidad por defecto en Communication Compliance?
   - a) El administrador global ve todas las alertas con los nombres reales
   - b) Seudonimización activa y sin acceso por defecto para los administradores globales
   - c) Los indicadores vienen activados y los nombres visibles para analistas
   - d) Los nombres solo se ocultan en las exportaciones a eDiscovery

11. ¿Qué limitación tienen las unidades administrativas en Communication Compliance?
   - a) No aplican a los reportes y no se combinan con ámbitos adaptables
   - b) Solo funcionan para Information Barriers, no para políticas de CC
   - c) Requieren pago por uso por cada unidad administrativa
   - d) Desactivan la seudonimización para los revisores de la unidad

12. En la integración entre Insider Risk Management y CC, ¿cuándo entra una persona en el alcance de IRM?
   - a) Con 1 mensaje de riesgo
   - b) Con 10 mensajes de riesgo en una semana
   - c) Cuando lo decide RR. HH.
   - d) Con 5 o más mensajes de riesgo en 24 horas

13. ¿Qué clasificadores usa la política «Insider risk trigger» que se crea automáticamente?
   - a) Threat, Harassment y Discrimination
   - b) Los seis clasificadores financieros
   - c) Prompt Shields y Protected material
   - d) Adult y Racy

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. No constituye asesoría legal ni laboral: las decisiones sobre supervisión de comunicaciones, privacidad, avisos a empleados y relaciones laborales corresponden a tus áreas de Legal, RR. HH. y privacidad. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

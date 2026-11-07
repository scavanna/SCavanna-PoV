# Nivel 2 · Intermedio · Proteger

*Seguridad de Microsoft 365 Copilot, agentes y Copilot Studio Ninja Training · Edición 2026*

[← Nivel 1 · Inicial](01_Nivel_1_Inicial.md) · [Índice del programa](README.md) · [Nivel 3 · Avanzado →](03_Nivel_3_Avanzado.md)

<a id="intermedio"></a>

SharePoint Advanced Management, DSPM para IA, etiquetas, DLP para Copilot, gobierno de agentes en Microsoft 365, entornos y directivas de datos de Copilot Studio y shadow AI. Terminas con barreras de datos, identidad y agentes configuradas en simulación para un grupo piloto.

*L300 · 8 módulos · ~52 horas · 101 recursos*

**Módulos de este nivel:** [M1 SharePoint Advanced Management](#m1) · [M2 DSPM para IA](#m2) · [M3 Etiquetas y cifrado](#m3) · [M4 DLP para Copilot](#m4) · [M5 Agentes en Microsoft 365](#m5) · [M6 Entornos de Copilot Studio](#m6) · [M7 Directivas de datos y acceso](#m7) · [M8 Shadow AI e IA de terceros](#m8)

<a id="m1"></a>

## M1 · SharePoint Advanced Management para Copilot

*L300 · ~7 h · Origen: Guía «Get ready for Microsoft 365 Copilot and agents with SharePoint Advanced Management» y ruta de Learn «Prepare security and compliance to support Microsoft 365 Copilot» (SharePoint Advanced Management)*

SharePoint Advanced Management (SAM) es la caja de herramientas de SharePoint contra la sobreexposición y la proliferación de sitios. Con **al menos una licencia de Copilot asignada** quedan incluidas casi todas sus funciones para Copilot, en las nubes WW, GCC, GCC High y DoD: directivas de propiedad, sitios inactivos y atestación (en simulación y en modo activo), evaluación de gestión de contenido, bloqueo de descarga (incluidas grabaciones de Teams), insights de apps y de agentes, acceso condicional por contexto de autenticación, RAC y RCD, informes DAG con revisión de acceso del sitio, catálogo, historial de cambios de 180 días y acciones recientes. Siguen requiriendo **SAM Plan 1** la restricción de creación de sitios por apps y el renombrado avanzado de tenants con más de 10.000 sitios.

Microsoft propone preparar Copilot con SAM en cinco pasos: ejecutar la evaluación de gestión de contenido y repetirla cada 30 días; gobernar el ciclo de vida de los sitios y archivar con Microsoft 365 Archive (Copilot no usa el contenido archivado); prevenir la sobreexposición endureciendo el uso compartido; apoyarse en el **SharePoint Admin Agent**; y asegurar las copias de seguridad. Las piezas de contención son **RCD**, que oculta un sitio de la búsqueda organizacional y de Copilot sin cambiar permisos y además quita del sitio los puntos de entrada de IA, y **RAC**, que limita el acceso a miembros de hasta 10 grupos. Ambos se administran desde el centro de administración de SharePoint o con PowerShell.

Los informes DAG son tu línea base: instantáneas trimestrales y actividad mensual, revisiones de acceso delegadas a los dueños y un informe de estado de permisos que se repite cada 30 días con `Start-SPODataAccessGovernanceInsight`. El SharePoint Admin Agent evalúa y remedia riesgos de contenido sin acciones destructivas y requiere el rol de Entra **SharePoint Advanced Management Administrator**, que conviene asignar a pocas personas. Lo que hagas aquí alimenta las evaluaciones de [M2](#m2) y las etiquetas de [M3](#m3); la relación entre SAM y DSPM se profundiza en el programa de Purview DSPM y seguridad de datos para IA, módulo M4.

**Por qué importa**

SAM convierte el plan contra la sobreexposición en acciones repetibles: informes que muestran dónde está el problema, contención temporal sin romper permisos y políticas que obligan a los dueños a hacerse cargo. Como una sola licencia de Copilot lo desbloquea, es la palanca de mayor retorno antes de ampliar el despliegue y la fuente de las métricas de sobreexposición del tablero del comité.

**Qué vas a lograr**

- Identificar qué funciones de SAM incluye la licencia de Copilot y cuáles siguen requiriendo SAM Plan 1.
- Generar e interpretar informes DAG e instantáneas de permisos, y delegar revisiones de acceso a los dueños.
- Aplicar RCD y RAC con criterio, probarlos con cuentas de control y documentar la reversión.
- Configurar directivas de ciclo de vida de sitios en simulación antes de activarlas.
- Operar el SharePoint Admin Agent y la evaluación de gestión de contenido con mínimo privilegio.

> **Novedad.** La tabla de funciones de SAM incluidas con la licencia de Copilot se actualizó el 18 de agosto de 2026: basta **una** licencia de Copilot asignada para desbloquearlas en WW, GCC, GCC High y DoD. El informe DAG de etiquetas en archivos requiere además E5 o G5, y siguen exigiendo SAM Plan 1 la restricción de creación de sitios por apps y el renombrado avanzado con más de 10.000 sitios ([SAM con licencia de Copilot](https://learn.microsoft.com/en-us/sharepoint/sharepoint-advanced-management-features-copilot-license)).

> **Qué cambió.** RCD se actualizó el 11 de octubre de 2026: además de ocultar el sitio de la búsqueda organizacional y de Copilot sin cambiar permisos ni sacarlo del índice, quita del sitio los puntos de entrada de IA (botón de Copilot, crear agentes y crear páginas con IA); no aplica a OneDrive y en sitios con más de 500.000 elementos puede tardar más de una semana ([RCD](https://learn.microsoft.com/en-us/sharepoint/restricted-content-discovery)). El 30 de julio de 2026 los informes DAG sumaron el de grupos especiales EEEU y Everyone ([informes DAG](https://learn.microsoft.com/en-us/sharepoint/data-access-governance-reports)).

> **Atención.** RAC no corrige permisos: niega el acceso a quien no está en los grupos de control aunque tenga permisos, y la búsqueda y Copilot lo respetan. Se habilita en el tenant con `Set-SPOTenant -EnableRestrictedAccessControl $true` (hasta 1 hora), admite hasta 10 grupos por sitio y los sitios de canales compartidos y privados de Teams necesitan su propia directiva ([RAC](https://learn.microsoft.com/en-us/sharepoint/restricted-access-control)). En OneDrive, RCD no aplica pero RAC sí, y el dueño debe estar en el grupo ([RAC en OneDrive](https://learn.microsoft.com/en-us/sharepoint/onedrive-site-access-restriction)).

> **Consejo Ninja.** El SharePoint Admin Agent evalúa y remedia riesgos de contenido (sobreexposición, ciclo de vida, revisiones de acceso, RAC, RCD y copias de seguridad) y requiere SAM y el rol SharePoint Advanced Management Administrator ([SharePoint Admin Agent](https://learn.microsoft.com/en-us/sharepoint/content-governance-agent)). Un resumen de un MVP de 2026 indica que se lanzó con 15 a 20 acciones y sin acciones destructivas, y que SAM llegó a las nubes soberanas en febrero de 2026 ([novedades de SAM](https://vladtalkstech.com/microsoft-365/sharepoint/sharepoint-advanced-management-2026/)).

**¿Tienes poco tiempo?**

- [SharePoint Advanced Management features in Microsoft Copilot licenses](https://learn.microsoft.com/en-us/sharepoint/sharepoint-advanced-management-features-copilot-license) · Documentación
- [Restrict discovery of SharePoint sites and content (Restricted Content Discovery)](https://learn.microsoft.com/en-us/sharepoint/restricted-content-discovery) · Documentación
- [Restrict SharePoint site access with Microsoft 365 groups and Microsoft Entra security groups (Restricted access control)](https://learn.microsoft.com/en-us/sharepoint/restricted-access-control) · Documentación
- [Data access governance reports for SharePoint and OneDrive sites](https://learn.microsoft.com/en-us/sharepoint/data-access-governance-reports) · Documentación

**Qué desbloquea la licencia de Copilot en SharePoint Advanced Management**

| Función | Para qué sirve frente a la sobreexposición | Licencia | Nota |
|---|---|---|---|
| Restricted Content Discovery (RCD) | Ocultar sitios de la búsqueda organizacional y de Copilot sin cambiar permisos | Al menos una licencia de Copilot | No aplica a OneDrive; más de una semana en sitios con más de 500.000 elementos |
| Restricted Access Control (RAC) | Limitar un sitio o una OneDrive a miembros de hasta 10 grupos | Al menos una licencia de Copilot | Habilitación en el tenant de hasta 1 hora; canales compartidos y privados aparte |
| Informes DAG de instantánea (permisos de sitios, por usuario y EEEU o Everyone) | Línea base de permisos | Al menos una licencia de Copilot | Cadencia trimestral sugerida |
| Informe DAG de etiquetas en archivos | Ubicar archivos etiquetados por sitio | Licencia de Copilot más E5 o G5 | — |
| Informes DAG de actividad (vínculos y EEEU, 28 días) | Tendencia del uso compartido | Con E5 sin SAM, hasta 10.000 sitios; completos con licencia de Copilot | La referencia del cmdlet dice que requiere SAM: verifica en tu tenant |
| Revisión de acceso del sitio | Delegar la corrección a los dueños | Al menos una licencia de Copilot | Se inicia desde los informes DAG |
| Directivas de propiedad, sitios inactivos y atestación | Que cada sitio tenga dueños y se recertifique | Al menos una licencia de Copilot | Primero en modo simulación |
| Evaluación de gestión de contenido | Diagnóstico del estado del tenant | Al menos una licencia de Copilot | Repetir cada 30 días |
| Bloqueo de descarga | Impedir descargas en sitios sensibles, incluidas grabaciones de Teams | Al menos una licencia de Copilot | — |
| Insights de apps empresariales, de IA y de agentes en SharePoint | Ver qué apps y agentes acceden al contenido | Al menos una licencia de Copilot | — |
| Acceso condicional por contexto de autenticación | Exigir controles más fuertes en sitios sensibles | Al menos una licencia de Copilot | Requiere además Entra ID P1 |
| Historial de cambios (180 días) y acciones recientes (30 días) | Trazabilidad de cambios de configuración | Al menos una licencia de Copilot | — |
| SharePoint Admin Agent | Evaluar y remediar riesgos de contenido con IA | SAM y rol SharePoint Advanced Management Administrator | Sin acciones destructivas |
| Restricción de creación de sitios por apps | Evitar sitios creados por aplicaciones | SAM Plan 1 | No incluida con la licencia de Copilot |
| Renombrado avanzado de tenant con más de 10.000 sitios | Cambio de dominio de SharePoint a gran escala | SAM Plan 1 | No incluido con la licencia de Copilot |

Fuentes: [SAM con licencia de Copilot](https://learn.microsoft.com/en-us/sharepoint/sharepoint-advanced-management-features-copilot-license) (18 de agosto de 2026), [visión general de SAM](https://learn.microsoft.com/en-us/sharepoint/advanced-management), [informes DAG](https://learn.microsoft.com/en-us/sharepoint/data-access-governance-reports), [RCD](https://learn.microsoft.com/en-us/sharepoint/restricted-content-discovery), [RAC](https://learn.microsoft.com/en-us/sharepoint/restricted-access-control) y [SharePoint Admin Agent](https://learn.microsoft.com/en-us/sharepoint/content-governance-agent).

### Documentación, cursos y credenciales

- [Restrict discovery of SharePoint sites and content (Restricted Content Discovery)](https://learn.microsoft.com/en-us/sharepoint/restricted-content-discovery) · Documentación · Oficial · Nuevo · Microsoft Learn · 11 oct 2026. RCD es un ajuste por sitio que oculta su contenido de la búsqueda organizacional y del descubrimiento de Copilot (sin cambiar permisos ni sacarlo del índice) y además quita del sitio los puntos de entrada de IA (botón Copilot, crear agentes, crear páginas con IA); no aplica a OneDrive.
- [SharePoint Advanced Management features in Microsoft Copilot licenses](https://learn.microsoft.com/en-us/sharepoint/sharepoint-advanced-management-features-copilot-license) · Documentación · Oficial · Nuevo · Microsoft Learn · 18 ago 2026. Tabla oficial de funciones de SAM que se desbloquean al asignar al menos una licencia de Copilot (control de proliferación, de sobreexposición y de ciclo de vida) en WW, GCC, GCC High y DoD, y lo que sigue requiriendo el complemento SAM Plan 1.
- [Data access governance reports for SharePoint and OneDrive sites](https://learn.microsoft.com/en-us/sharepoint/data-access-governance-reports) · Documentación · Oficial · Nuevo · Microsoft Learn · 30 jul 2026. Describe los informes DAG: instantáneas (permisos de sitios de toda la organización, permisos por usuario, sitios y archivos compartidos vía grupos especiales EEEU/Everyone, etiquetas en archivos) y de actividad de 28 días (vínculos de uso compartido y EEEU), con acciones de remediación (RAC, historial de cambios, revisión de acceso del sitio).
- [Manage Data access governance reports by using SharePoint Online PowerShell](https://learn.microsoft.com/en-us/sharepoint/powershell-for-data-access-governance) · Documentación · Oficial · Microsoft Learn. Cómo generar por PowerShell el informe de estado de permisos de sitios (línea base de sobreexposición), el de permisos por usuario, etiquetas, vínculos y EEEU, y ejecutar acciones de remediación a escala.
- [Restrict SharePoint site access with Microsoft 365 groups and Microsoft Entra security groups (Restricted access control)](https://learn.microsoft.com/en-us/sharepoint/restricted-access-control) · Documentación · Oficial · Microsoft Learn. Restricted access control limita un sitio (con grupo, de Teams, sin grupo) a los miembros de hasta 10 grupos de Microsoft 365 o de seguridad de Entra; la búsqueda y Copilot respetan la directiva y los usuarios fuera del grupo no ven el contenido aunque tengan permiso directo.
- [SharePoint Advanced Management overview](https://learn.microsoft.com/en-us/sharepoint/advanced-management) · Documentación · Oficial · Microsoft Learn. Lista actual de capacidades de SAM agrupadas en proliferación (propiedad, sitios inactivos, atestación), ciclo de vida (catálogo, historial de cambios de 180 días, cambios recientes, restricción de creación de sitios por apps) y sobreexposición (acceso condicional por contexto de autenticación, RAC, evaluación de gestión de contenido, bloqueo de descarga, insights de apps, AI insights, insights de agentes en SharePoint, RCD e informes DAG).
- [Start-SPODataAccessGovernanceInsight (Microsoft.Online.SharePoint.PowerShell)](https://learn.microsoft.com/en-us/powershell/module/microsoft.online.sharepoint.powershell/start-spodataaccessgovernanceinsight?view=sharepoint-ps) · Documentación · Oficial · Microsoft Learn. Referencia del cmdlet que genera los informes DAG (vínculos, EEEU, etiquetas, sitios con demasiados usuarios como línea base y permisos por usuario); indica que requiere licencia de SAM.
- [Restrict access to a user's OneDrive content to people in a group](https://learn.microsoft.com/en-us/sharepoint/onedrive-site-access-restriction) · Documentación · Oficial · Microsoft Learn. Aplica restricted access control a la OneDrive de un usuario con Set-SPOSite -RestrictedAccessControl y grupos permitidos, y opcionalmente bloquea compartir fuera de esos grupos (Set-SPOTenant -AllowSharingOutsideRestrictedAccessControlGroups $false).
- [SharePoint Admin Agent overview](https://learn.microsoft.com/en-us/sharepoint/content-governance-agent) · Documentación · Oficial · Microsoft Learn. Agente de IA para administradores que evalúa y remedia riesgos de contenido en SharePoint y OneDrive con lenguaje natural (sobreexposición, ciclo de vida, revisiones de acceso, RAC, RCD, Baseline Security Mode, Backup); se abre desde la app Copilot, el centro de administración de SharePoint o Teams.

### Comunidad: blogs, libros, newsletters y eventos

- [SharePoint Advanced Management: what's new for 2026](https://vladtalkstech.com/microsoft-365/sharepoint/sharepoint-advanced-management-2026/) · Blog · MVP · Nuevo · Vlad Catrinescu · Vlad Talks Tech · 16 jun 2026. Entrevista con el PM principal de SAM: el SharePoint Admin Agent (15-20 acciones al lanzamiento, meta de unas 150, sin acciones destructivas), gestión de catálogo, correos agrupados a dueños de sitio, el nuevo rol SAM Administrator para informes de sobreexposición a nivel de archivo y soporte en nubes soberanas desde febrero de 2026.

**Manos a la obra**

1. `Laboratorio parcial` RCD y RAC en sitios de alto riesgo: aplica `Set-SPOSite -RestrictContentOrgWideSearch $true` en PRUEBA-Finanzas-Nomina y RAC en PRUEBA-Legal-Contratos (`Set-SPOTenant -EnableRestrictedAccessControl $true` más un grupo de control) ([RCD](https://learn.microsoft.com/en-us/sharepoint/restricted-content-discovery), [RAC](https://learn.microsoft.com/en-us/sharepoint/restricted-access-control)). Prueba con una cuenta con permisos pero fuera del grupo: acceso denegado con RAC y ausencia en la búsqueda y en Copilot con RCD. Limitación: requiere al menos una licencia de Copilot (sandbox) y el laboratorio tiene pocos sitios. Reversión documentada: `-RestrictContentOrgWideSearch $false` y `-ClearRestrictedAccessControl`. Evidencia: informe de `Get-SPORestrictedContentDiscoverabilityReport` y capturas de la prueba.
2. `Laboratorio parcial` Instantáneas DAG y revisión de acceso: genera el informe de permisos de sitios de toda la organización y el de grupos especiales EEEU y Everyone, e inicia una revisión de acceso para el dueño del sitio con más hallazgos ([informes DAG](https://learn.microsoft.com/en-us/sharepoint/data-access-governance-reports)). Limitación: requiere SAM desbloqueado con una licencia de Copilot y los datos del laboratorio son pocos. Evidencia: CSV de los informes y revisión cerrada.
3. `Laboratorio parcial` Línea base de estado de permisos con PowerShell: con el módulo 16.0.25409 o posterior, conéctate sin `-Credential` y ejecuta `Start-SPODataAccessGovernanceInsight -ReportEntity PermissionedUsers -ReportType Snapshot` ([PowerShell para DAG](https://learn.microsoft.com/en-us/sharepoint/powershell-for-data-access-governance)). Limitación: el primer informe tarda hasta 5 días y requiere SAM. Evidencia: CSV con usuarios únicos por sitio y fecha de la próxima ejecución (cada 30 días).
4. `Laboratorio parcial` Directivas de ciclo de vida en simulación: crea una directiva de propiedad (mínimo dos dueños), una de sitios inactivos y una de atestación, todas en modo simulación, y revisa a quién notificarían ([funciones de SAM](https://learn.microsoft.com/en-us/sharepoint/sharepoint-advanced-management-features-copilot-license)). Limitación: el laboratorio tiene pocos sitios y dueños. Cómo hacerlo en producción: simulación, alcance acotado y aviso previo a los dueños antes del modo activo. Evidencia: informe de simulación con la decisión de activar o ajustar.
5. `Laboratorio parcial` RAC en OneDrive: restringe la OneDrive de una cuenta de prueba crítica a un grupo que incluya a su dueño y, si lo necesitas, bloquea el uso compartido fuera del grupo ([RAC en OneDrive](https://learn.microsoft.com/en-us/sharepoint/onedrive-site-access-restriction)). Limitación: requiere SAM desbloqueado. Evidencia: configuración aplicada y prueba con una cuenta fuera del grupo.
6. `Solo producción` Evaluación de gestión de contenido y SharePoint Admin Agent en el tenant real: ejecuta la evaluación y pide al agente la lista de sitios sobrecompartidos y su nivel de riesgo ([SharePoint Admin Agent](https://learn.microsoft.com/en-us/sharepoint/content-governance-agent)). Por qué en producción: necesita volumen real de sitios y dueños. Cómo hacerlo seguro: rol SharePoint Advanced Management Administrator en PIM para un único operador, solo lectura y ninguna remediación sin acuerdo de los dueños. Evidencia: informe con fecha y plan priorizado.
7. `Solo producción` Campaña de remediación por dueños: envía revisiones de acceso del sitio a los dueños de los 20 sitios con más hallazgos y mide el cierre a 30 días ([informes DAG](https://learn.microsoft.com/en-us/sharepoint/data-access-governance-reports)). Por qué en producción: depende de dueños reales y de permisos heredados. Cómo hacerlo seguro: comunicación previa, RCD temporal en los sitios críticos mientras dura la revisión y retiro de RCD al cerrar cada caso. Evidencia: tablero de avance con sitios corregidos y pendientes.

**¿Quieres profundizar?**

- [SharePoint Advanced Management: what's new for 2026](https://vladtalkstech.com/microsoft-365/sharepoint/sharepoint-advanced-management-2026/) · Blog

<a id="m2"></a>

## M2 · DSPM para IA: visibilidad, evaluaciones y políticas de un clic

*L300 · ~7 h · Origen: Ruta SC-401 «Secure AI interactions and environments with Microsoft Purview» (DSPM y auditoría) y ruta «Secure and govern Microsoft 365 Copilot interactions with Microsoft Purview»*

DSPM (Data Security Posture Management) es el tablero de Purview para la seguridad de los datos, y su nueva experiencia está en GA desde mayo de 2026. Se organiza por **objetivos**: «Prevent data exposure in Microsoft 365 Copilot and Microsoft Copilot interactions», «Prevent oversharing of sensitive data», «Prevent exfiltration to risky locations» y «Discover sensitive data», cada uno con métricas, acciones priorizadas y políticas de un clic. Suma Posture con tendencia de 30 días, Asset explorer, la vista Apps and agents con los 20 agentes usados más recientemente, el explorador de actividad con la pestaña AI activities y las evaluaciones de riesgo de datos. Los datos accionables aparecen alrededor de un día después de aceptar las tareas iniciales.

Las experiencias **DSPM for AI (classic)** y DSPM (classic) se retiran a fines de enero de 2027, según MC1481315 actualizado el 27 de octubre de 2026, aunque las guías de inicio por app todavía parten de ellas. Sus prerrequisitos siguen siendo una buena lista de control: auditoría activa, licencia de Copilot para ver Copilot y sus agentes, directiva de configuración de Edge, dispositivos incorporados con la extensión del navegador para sitios de IA de terceros, SDK de Purview para apps registradas en Entra y pago por uso para las apps de IA que no son Microsoft 365 Copilot. Leer el contenido de prompts y respuestas exige el rol Content Explorer Content Viewer.

Las **políticas de un clic** son el atajo de DSPM: detectan información sensible que se pega o se sube a sitios de IA (DLP en solo auditoría), visitas a sitios de IA y uso riesgoso de IA (Insider Risk), conducta no ética en apps de IA (Communication Compliance), capturan interacciones con directivas de colección, bloquean con Protección adaptativa e impiden que Copilot procese contenido etiquetado. Lo que **no** se enseña aquí es AI observability ni Insider Risk para agentes: según MC1280556 requieren Microsoft 365 E7 o Agent 365. Se profundiza en el programa de Purview DSPM y seguridad de datos para IA, módulos I2, M1 y M2.

**Por qué importa**

Sin visibilidad, la conversación sobre IA se basa en anécdotas. DSPM muestra qué datos sensibles aparecen en prompts y respuestas, qué apps de IA se usan y qué sitios exponen más, y propone políticas que pasan de observar a proteger con un modo inicial seguro. Es el tablero que el comité de IA necesita para priorizar y para medir el efecto de cada control.

**Qué vas a lograr**

- Navegar la nueva DSPM y su objetivo para Copilot, y planificar la transición desde las experiencias classic antes de fines de enero de 2027.
- Verificar los prerrequisitos de DSPM para Copilot, Copilot Studio y apps de IA de terceros.
- Desplegar las políticas de un clic en su modo inicial y documentar qué solución genera cada una.
- Controlar con roles de Purview quién puede leer prompts y respuestas.
- Separar lo disponible sin Agent 365 de AI observability y Risky Agents, que quedan fuera de alcance.

> **Qué cambió.** MC1481315, actualizado el 27 de octubre de 2026, aplazó a fines de enero de 2027 el retiro de DSPM (classic) y DSPM for AI (classic), antes previsto para noviembre y diciembre de 2026 ([MC1481315](https://mc.merill.net/message/MC1481315)). Las políticas creadas cuando el producto se llamaba AI Hub conservan el prefijo «Microsoft AI Hub» ([consideraciones de DSPM for AI](https://learn.microsoft.com/en-us/purview/dspm-for-ai-considerations)).

> **Atención.** Fuera de alcance: DSPM AI observability e Insider Risk para agentes llegaron a GA entre mediados de junio y fines de julio de 2026 y, según MC1280556, no están disponibles sin Microsoft 365 E7 o Agent 365 ([MC1280556](https://message.cengizyilmaz.net/message/mc1280556-microsoft-purview-for-agents-ai-observability-and-insider-risk-management-now-generally-available)). Dentro del alcance quedan Discover > Apps and agents (los 20 agentes usados más recientemente), la pestaña AI activities, los informes «Copilot experiences & agents» de DSPM for AI hasta su retiro y la auditoría con AgentId ([A1](03_Nivel_3_Avanzado.md#a1)).

> **Atención.** Privacidad desigual: el rol Content Explorer Content Viewer permite leer prompts y respuestas ([Purview para Copilot](https://learn.microsoft.com/en-us/purview/ai-m365-copilot)), mientras Purview Data Security AI Admin edita la DLP de Copilot sin leerlos ([DLP para Copilot](https://learn.microsoft.com/en-us/purview/dlp-microsoft365-copilot-location-learn-about)). Insider Risk y Communication Compliance seudonimizan por defecto, pero las alertas DLP y el explorador de actividad muestran nombres reales: define con Legal y privacidad quién ve qué (esto no es asesoría legal).

> **Novedad.** En mayo de 2026 llegó a GA la nueva DSPM, con soporte de unidades administrativas y la pausa del procesamiento de datos de Microsoft 365 en tenants inactivos más de 60 días; el Data Security Posture Agent sigue en preview según Learn ([novedades de Purview](https://learn.microsoft.com/en-us/purview/whats-new)), aunque MC1318248 anunció su GA ([MC1318248](https://mc.merill.net/message/MC1318248)). Las interacciones de Cowork aparecen en el explorador de actividad, pero no en Apps and agents ([Cowork en Purview](https://learn.microsoft.com/es-es/purview/ai-copilot-cowork)).

**¿Tienes poco tiempo?**

- [Learn about Microsoft Purview Data Security Posture Management (DSPM)](https://learn.microsoft.com/en-us/purview/data-security-posture-management-learn-about) · Documentación
- [Considerations for deploying Microsoft Purview DSPM for AI (classic)](https://learn.microsoft.com/en-us/purview/dspm-for-ai-considerations) · Documentación
- [Use Microsoft Purview to manage data security & compliance for Microsoft 365 Copilot & Copilot Chat](https://learn.microsoft.com/en-us/purview/ai-m365-copilot) · Documentación
- [Secure AI interactions and environments with Microsoft Purview (SC-401 learning path)](https://learn.microsoft.com/en-us/training/paths/purview-protect-ai/) · Curso

**Políticas de un clic de DSPM para IA**

| Política | Solución que la implementa | Qué hace | Modo inicial |
|---|---|---|---|
| DSPM for AI: Detect sensitive info added to AI sites | DLP (endpoint y navegador) | Descubre contenido sensible pegado o subido a sitios de IA en Edge, Chrome y Firefox | Solo auditoría, para todos los usuarios |
| DSPM for AI - Detect when users visit AI sites | Insider Risk Management | Detecta visitas a sitios de IA desde el navegador | Política de detección (modo no indicado) |
| DSPM for AI - Detect risky AI usage | Insider Risk Management (Risky AI usage) | Calcula el riesgo del usuario por prompts y respuestas riesgosos en Copilot, agentes y otras apps de IA | Detección y alertas |
| DSPM for AI - Unethical behavior in AI apps | Communication Compliance | Detecta información sensible en prompts y respuestas de Copilot, agentes y otras apps de IA | Activa para todos los usuarios, para revisión |
| DSPM for AI - Capture interactions for Copilot experiences | Directiva de colección | Captura prompts y respuestas de Copilot en Fabric y Security Copilot para eDiscovery y ciclo de vida | Captura de contenido activada |
| DSPM for AI - Capture interactions for enterprise AI apps | Directiva de colección | Captura prompts y respuestas de ChatGPT Enterprise y de apps conectadas por Entra o Foundry | Captura de contenido activada |
| DSPM for AI - Detect sensitive info shared in AI prompts in Edge | Directiva de colección | Detecta prompts con información sensible enviados a apps de IA en Edge | Solo auditoría, sin captura de contenido |
| DSPM for AI - Block sensitive info from AI sites | DLP (endpoint) con Protección adaptativa | Bloqueo con anulación para usuarios de riesgo elevado que pegan o suben datos sensibles | Modo prueba |
| DSPM for AI - Block sensitive info from AI apps in Edge | DLP en línea en Edge | Detecta tipos de información comunes y bloquea el envío del prompt | No indicado: verifícalo en el tenant |
| DSPM for AI - Protect sensitive data from Copilot processing | DLP (ubicación Microsoft 365 Copilot) | Impide que Copilot y los agentes procesen elementos con las etiquetas elegidas | No indicado: verifícalo en el tenant |
| Information Protection - Sensitivity labels and policies | Information Protection | Crea etiquetas y políticas predeterminadas; se omite si ya existen | No aplica |
| Default DLP policy - Protect sensitive M365 Copilot interactions (automática, no es de un clic) | DLP (ubicación Microsoft 365 Copilot) | Detecta más de 100 tipos de información en prompts y genera una alerta y un correo de baja severidad | Simulación |

Fuentes: [consideraciones de DSPM for AI](https://learn.microsoft.com/en-us/purview/dspm-for-ai-considerations) (1 de mayo de 2026) y [política DLP predeterminada](https://learn.microsoft.com/en-us/purview/dlp-microsoft365-copilot-location-default-policy). Las políticas que usan Protección adaptativa la activan con niveles predeterminados si no estaba activa; con unidades administrativas, solo un administrador sin restricciones puede crearlas.

### Documentación, cursos y credenciales

- [Use Microsoft Purview to manage data security & compliance for AI agents](https://learn.microsoft.com/en-us/purview/ai-agents) · Documentación · Oficial · Nuevo · Microsoft Learn · 27 may 2026. Matriz de capacidades de Purview por tipo de agente (Microsoft 365 Copilot, Security Copilot, Fabric, Copilot Studio, Foundry, Entra-registered, ChatGPT/Claude Enterprise), indicando dónde aplica DLP.
- [Use Microsoft Purview to manage data security & compliance for Microsoft Copilot Studio](https://learn.microsoft.com/en-us/purview/ai-copilot-studio) · Documentación · Oficial · Nuevo · Microsoft Learn · 1 may 2026. Capacidades de Purview soportadas para agentes de Copilot Studio (DSPM, auditoría, clasificación, etiquetas, DLP, IRM, eDiscovery, retención) y pasos recomendados.
- [Learn about Microsoft Purview Data Security Posture Management (DSPM)](https://learn.microsoft.com/en-us/purview/data-security-posture-management-learn-about) · Documentación · Oficial · Microsoft Learn. Página principal de la versión actual (unificada) de DSPM: objetivos de seguridad de datos, observabilidad de IA, cobertura de Microsoft 365, Azure, Fabric y SaaS/IaaS de terceros con integraciones de socios.
- [Use Microsoft Purview to manage data security & compliance for Microsoft 365 Copilot & Copilot Chat](https://learn.microsoft.com/en-us/purview/ai-m365-copilot) · Documentación · Oficial · Microsoft Learn. Tabla de capacidades de Purview para Microsoft 365 Copilot y Copilot Chat y lista de políticas de un clic (etiquetas, uso riesgoso de IA, comportamiento no ético, protección de datos etiquetados).
- [Secure and govern Microsoft 365 Copilot interactions with Microsoft Purview (learning path)](https://learn.microsoft.com/en-us/training/paths/purview-secure-govern-copilot-interactions/) · Curso · Oficial · Microsoft Learn. Ruta de 7 módulos (6 h 8 min) que integra auditoría, etiquetas, DLP, Insider Risk y Communication Compliance para gobernar las interacciones con Copilot.
- [Considerations for deploying Microsoft Purview DSPM for AI (classic)](https://learn.microsoft.com/en-us/purview/dspm-for-ai-considerations) · Documentación · Oficial · Legado aún útil · Nuevo · Microsoft Learn · 1 may 2026. Consideraciones de DSPM for AI (classic): prerrequisitos (auditoría, licencia de Microsoft 365 Copilot, PAYG para IA no Microsoft), lista de políticas de un clic con su modo inicial y eventos del explorador de actividad (AI interaction, AI website visit, DLP rule match, Sensitive info types). *Nota:* Página classic (01-may-2026) pero es la única que documenta en detalle las políticas de un clic y sus modos (auditoría/prueba). Retiro de la experiencia classic: fines de enero de 2027 (MC1481315)
- [Permissions for Microsoft Purview Data Security Posture Management](https://learn.microsoft.com/en-us/purview/data-security-posture-management-permissions) · Documentación · Oficial · Microsoft Learn. Matriz de permisos de la nueva DSPM: roles de edición, roles de solo lectura (Data Security AI Viewer, AI Content Viewer, Data Security Viewers) y roles adicionales para Security Copilot, Sentinel y DSI.
- [Considerations for deploying Microsoft Purview Data Security Posture Management](https://learn.microsoft.com/en-us/purview/data-security-posture-management-considerations) · Documentación · Oficial · Microsoft Learn. Prerrequisitos de la DSPM actual para IA (licencia de Copilot, directiva de colección, configuración de Edge, SDK de Purview, Security Copilot), soporte de unidades administrativas y eventos del explorador de actividad.
- [Microsoft Purview data security and compliance protections for generative AI apps](https://learn.microsoft.com/en-us/purview/ai-microsoft-purview) · Documentación · Oficial · Microsoft Learn. Panorama oficial de cómo Purview (DSPM, etiquetas, DLP, IRM, cumplimiento) protege Copilot, agentes y apps de IA empresariales y de terceros, con la categorización de apps soportadas.
- [Secure AI interactions and environments with Microsoft Purview (SC-401 learning path)](https://learn.microsoft.com/en-us/training/paths/purview-protect-ai/) · Curso · Oficial · Microsoft Learn. Ruta oficial de 4 módulos (3 h 30 min) alineada a SC-401: proteger datos de IA con DSPM y auditoría, interacciones de Copilot, apps de IA empresariales y de navegador, y entornos de desarrollo (Foundry, Copilot Studio, Fabric).
- [Protección de las interacciones y entornos de IA con Microsoft Purview (SC-401) – ruta en español](https://learn.microsoft.com/es-es/training/paths/purview-protect-ai/) · Curso · Oficial · ES · Microsoft Learn. Versión en español de la ruta oficial de SC-401 sobre protección de datos en Copilot, apps de IA y entornos de desarrollo con Purview.
- [Overview of Microsoft Purview APIs (Microsoft Graph)](https://learn.microsoft.com/en-us/purview/developer/microsoft-purview-sdk-documentation-overview) · Documentación · Oficial · Microsoft Learn. Resume las APIs de Purview en Graph (protectionScopes, processContent, contentActivities y sensitivityLabels) para que apps de IA y de negocio apliquen DLP, IRM, etiquetas y auditoría.
- [userDataSecurityAndGovernance: processContent](https://learn.microsoft.com/en-us/graph/api/userdatasecurityandgovernance-processcontent?view=graph-rest-1.0) · Documentación · Oficial · Microsoft Learn (Microsoft Graph). API de Graph v1.0 que permite a una app empresarial o de IA enviar texto (prompts, mensajes) para evaluarlo contra las directivas de Purview y recibir la acción a aplicar.
- [Secure and govern Microsoft 365 Copilot agents](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-sc-agents-deployment) · Documentación · Oficial · Microsoft Learn · 3 abr 2026. Modelo de despliegue oficial en 4 pasos para asegurar agentes de Microsoft 365 Copilot: descubrir riesgos, proteger datos de grounding (incluye DLP para Copilot), proteger interacciones y gobernarlas.
- [Step 1: Discover risks and identify gaps - Secure and govern Microsoft 365 Copilot agents](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-sc-agents-step1) · Documentación · Oficial · Microsoft Learn · 3 abr 2026. Primer paso del modelo para agentes: activar auditoría, evaluar sobreexposición, descubrir datos sensibles en Dataverse con Unified Catalog, revisar el informe de apps y agentes y brechas regulatorias con Compliance Manager.
- [Learn about Data Security Posture Management for AI (classic)](https://learn.microsoft.com/en-us/purview/dspm-for-ai) · Documentación · Oficial · Legado aún útil · Microsoft Learn. Describe DSPM for AI clásico: políticas de un clic, informes de actividad de IA, evaluación semanal automática de los 100 sitios de SharePoint más usados y controles de cumplimiento para Copilot y apps de IA de terceros. *Nota:* Reemplazado por la nueva DSPM con soporte para apps y agentes de IA
- [Microsoft Purview middleware – Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/integrations/by-component/middleware/purview) · Documentación · Oficial · Microsoft Learn. Muestra cómo añadir el middleware de directivas de Purview a agentes de Agent Framework (C#, Python) para bloquear contenido sensible en línea con DLP y registrar interacciones para auditoría y cumplimiento.
- [tenantDataSecurityAndGovernance: processContent](https://learn.microsoft.com/en-us/graph/api/tenantdatasecurityandgovernance-processcontent?view=graph-rest-beta) · Documentación · Oficial · Vista previa · Nuevo · Microsoft Learn (Microsoft Graph) · 23 oct 2026. Variante beta a nivel de tenant para evaluar interacciones de agentes (incluidas agente-a-herramienta) contra directivas DLP de Purview y devolver acciones como bloquear. *Nota:* API beta no soportada en producción; requiere Content.Process.All con consentimiento de administrador; usa metadatos de Entra Agent ID

### Anuncios y blogs oficiales

- [From Oversharing to Enforcement: A Practical Guide to AI Data Security with Microsoft Purview](https://techcommunity.microsoft.com/blog/microsoft-purview-blog/from-oversharing-to-enforcement-a-practical-guide-to-ai-data-security-with-micro/4513727) · Blog oficial · Empleado de Microsoft · George Smyrlis · Microsoft Purview Blog (Tech Community) · 23 abr 2026. Guía práctica oficial para pasar de la visibilidad a la aplicación de controles: DLP a nivel de prompt, descubrimiento de IA en la sombra, objetivos de DSPM y un modelo de madurez por fases.

### Webinars, videos y podcasts

- [AI and Agent Data Security Controls in Microsoft Purview (Microsoft Mechanics)](https://www.youtube.com/watch?v=4BcVWkSTZ3I) · Video · Empleado de Microsoft · Legado aún útil · Shilpa Ranganathan · Microsoft Mechanics. Demostración de DSPM for AI: registro de actividad, monitoreo de riesgos, ChatGPT Enterprise, barreras para agentes, sobreexposición y registros de auditoría. *Nota:* Grabado sobre DSPM for AI (hoy classic); los conceptos siguen vigentes en la nueva DSPM. YouTube muestra "hace 1 año" (2025, mes no visible)

### Laboratorios, GitHub y herramientas

- [MC1481315 – Retirement of DSPM classic and DSPM for AI classic experiences (archivo, versión actualizada)](https://mc.merill.net/message/MC1481315) · Herramienta · Comunidad · Nuevo · Microsoft (archivado por Merill Fernando) · Microsoft 365 Message Center Archive (merill.net) · 27 oct 2026. Anuncia el retiro de DSPM (classic) y DSPM for AI (classic), aplazado el 27-oct-2026 para iniciar y completarse a finales de enero de 2027, por lo que todo flujo debe migrar a la DSPM actual.
- [MC1280556 – Microsoft Purview for agents: AI observability and insider risk management now generally available (archivo)](https://message.cengizyilmaz.net/message/mc1280556-microsoft-purview-for-agents-ai-observability-and-insider-risk-management-now-generally-available) · Herramienta · Comunidad · Nuevo · Microsoft (archivado por Cengiz Yilmaz) · Microsoft 365 Message Center Archive (cengizyilmaz.net) · 21 may 2026. MC1280556 (Roadmap 516032): DSPM – AI Observability e Insider Risk Management para agentes pasan a GA mundial entre mediados de junio y fines de julio de 2026, y no estarán disponibles sin suscripciones Microsoft 365 E7 o Agent 365.
- [MC1191257 – New Microsoft Purview data security posture management experience (archivo Message Center)](https://message.cengizyilmaz.net/message/mc1191257-new-microsoft-purview-data-security-posture-management-experience) · Herramienta · Comunidad · Microsoft (archivado por Cengiz Yilmaz) · Microsoft 365 Message Center Archive (cengizyilmaz.net) · 10 abr 2026. Cronología oficial de la nueva DSPM: preview desde diciembre de 2025 y GA en mayo de 2026, con DSPM (classic) y DSPM for AI (classic) aún accesibles y migración automática de la incorporación.
- [microsoft/purview-api-samples](https://github.com/microsoft/purview-api-samples) · GitHub · Oficial · GitHub (Microsoft). Repositorio oficial de muestras de la plataforma de desarrollo de Purview: colección Postman de APIs Graph, app .NET, agente multicloud en AWS Bedrock y script para DLP de apps de IA personalizadas.

### Comunidad: blogs, libros, newsletters y eventos

- [Microsoft Purview DSPM para IA: guía de despliegue](https://jpmarquez.com/es/blog/microsoft-purview-dspm-ia-guia-despliegue-copilot/) · Blog · Comunidad · Nuevo · ES · JP Márquez · jpmarquez.com · 28 jul 2026. Guía en español para desplegar DSPM para IA antes de Copilot: evaluación predeterminada, políticas de un clic prioritarias y plan por semanas, con límites prácticos.

**Manos a la obra**

1. `Laboratorio` Recorrido de DSPM orientado a IA: con la auditoría activa, entra a DSPM, acepta las tareas iniciales y, un día después, documenta el objetivo «Prevent data exposure in Microsoft 365 Copilot and Microsoft Copilot interactions», Discover > Apps and agents, la pestaña AI activities del explorador de actividad y Reports ([DSPM](https://learn.microsoft.com/en-us/purview/data-security-posture-management-learn-about)). Marca AI observability como fuera de alcance. Evidencia: notas con capturas y una lista de tres acciones priorizadas.
2. `Laboratorio parcial` Inventario de políticas de un clic: crea «Detect risky AI usage», «Unethical behavior in AI apps» y «Protect sensitive data from Copilot processing», y registra en la tabla de este módulo la solución que genera cada una y su modo inicial ([consideraciones de DSPM for AI](https://learn.microsoft.com/en-us/purview/dspm-for-ai-considerations)). Limitación: sin licencias de Copilot no habrá interacciones que analizar, y las políticas de navegador requieren dispositivos incorporados, la extensión y pago por uso. Cómo hacerlo en producción: grupo piloto, modo auditoría o prueba y revisión con Legal antes de capturar contenido. Evidencia: tabla completada.
3. `Laboratorio parcial` Explorador de actividad: genera interacciones de Copilot Chat con datos sintéticos (por ejemplo, una CURP o un DNI inventados) y filtra los eventos AI interaction, Sensitive info types y DLP rule match ([Purview para Copilot](https://learn.microsoft.com/en-us/purview/ai-m365-copilot)). Limitación: con poco volumen y sin licencia de Copilot verás pocos eventos, y los usuarios sin buzón de Exchange Online no muestran el prompt. Evidencia: exportación filtrada y una interacción explicada.
4. `Laboratorio` Roles: asigna Purview Data Security AI Admin a quien opera la DLP de Copilot y Content Explorer Content Viewer solo a un revisor autorizado, y comprueba que el operador no puede leer prompts ([permisos de DSPM](https://learn.microsoft.com/en-us/purview/data-security-posture-management-permissions)). Evidencia: matriz de roles y prueba del operador.
5. `Laboratorio` Plan de transición desde las experiencias classic: lista lo que hoy usas de DSPM for AI (classic) —informes, políticas con prefijo «Microsoft AI Hub» y consulta de transcripciones de agentes— y su equivalente en la nueva DSPM antes de fines de enero de 2027 ([MC1481315](https://mc.merill.net/message/MC1481315)). Evidencia: plan con dueño y fecha por elemento.
6. `Solo producción` Informes «Copilot experiences & agents» con datos reales: revisa interacciones totales, interacciones sensibles por app, etiquetas más referenciadas y uso riesgoso de IA ([Purview para Copilot](https://learn.microsoft.com/en-us/purview/ai-m365-copilot)). Por qué en producción: requiere usuarios con licencia y actividad real. Cómo hacerlo seguro: roles de solo lectura, datos agregados, aprobación de Legal y privacidad antes de abrir el contenido de prompts y acta mensual. Evidencia: resumen mensual para el comité.

**¿Quieres profundizar?**

- [AI and Agent Data Security Controls in Microsoft Purview (Microsoft Mechanics)](https://www.youtube.com/watch?v=4BcVWkSTZ3I) · Video
- [MC1481315 – Retirement of DSPM classic and DSPM for AI classic experiences (archivo, versión actualizada)](https://mc.merill.net/message/MC1481315) · Herramienta
- [MC1280556 – Microsoft Purview for agents: AI observability and insider risk management now generally available (archivo)](https://message.cengizyilmaz.net/message/mc1280556-microsoft-purview-for-agents-ai-observability-and-insider-risk-management-now-generally-available) · Herramienta
- [Microsoft Purview DSPM para IA: guía de despliegue](https://jpmarquez.com/es/blog/microsoft-purview-dspm-ia-guia-despliegue-copilot/) · Blog

<a id="m3"></a>

## M3 · Etiquetas de confidencialidad, cifrado y derechos de uso con Copilot

*L300 · ~6 h · Origen: Ruta de Learn «Secure and govern Microsoft 365 Copilot interactions with Microsoft Purview» (etiquetas) y modelo de despliegue «Secure and govern Microsoft 365 Copilot agents», pasos 2 y 3*

Las etiquetas de confidencialidad viajan con el dato, y Copilot las respeta. Solo resume o cita contenido al que el usuario tiene acceso; si el archivo está cifrado, el usuario necesita los derechos de uso **VIEW y EXTRACT**, y Copilot verifica también el cifrado de Azure RMS sin etiqueta. Copilot Chat muestra la etiqueta de mayor prioridad de los datos usados, y el contenido nuevo que Copilot crea en Word, PowerPoint y Outlook, o con «Edit in Pages» desde Copilot Chat, hereda esa etiqueta con sus marcas de contenido, aunque el usuario puede reemplazarla. La protección sigue vigente fuera del tenant, según la página de arquitectura actualizada el 3 de noviembre de 2026.

Conviene conocer los casos especiales antes de diseñar. Copilot no devuelve correos S/MIME y no está disponible en Outlook con uno abierto; los documentos con contraseña solo se usan si ya están abiertos; el contenido con Customer Key o BYOK sí se admite; Double Key Encryption y los **permisos definidos por el usuario** bloquean a Copilot y a los agentes. Si no habilitaste las etiquetas en SharePoint y OneDrive, Copilot solo usa archivos cifrados abiertos en las apps de Office para Windows. En Copilot Pages las etiquetas son manuales y en Notebooks no se aplican. Desde junio de 2026, el ajuste de etiqueta que impide las experiencias conectadas que analizan contenido se extiende a macOS, iOS y Android (preview).

Con agentes, Copilot Studio admite etiquetas cuando el conocimiento está en SharePoint (incluido OneDrive) o en Dataverse con etiquetado automático del Data Map; el cifrado solo se admite con etiquetas y solo en SharePoint. Los agentes muestran la etiqueta más alta en la respuesta y en las citas, y la vista «View sensitivity labels in agent responses» está en preview. La estrategia práctica combina **etiquetas de contenedor** y etiqueta predeterminada de biblioteca como vía rápida, etiquetado automático **en simulación** antes de forzarlo y una matriz de etiquetas frente a Copilot. Se profundiza en el programa de Purview Information Protection, módulo A1.

**Por qué importa**

Las etiquetas son el control que acompaña al archivo: definen si Copilot puede usarlo, qué etiqueta hereda lo que genera y si la protección sigue fuera del tenant. Bien diseñadas, reducen la sobreexposición sin depender de que cada permiso esté perfecto; mal diseñadas, dejan a Copilot ciego ante contenido legítimo o le permiten leer lo que no debería.

**Qué vas a lograr**

- Explicar los derechos VIEW y EXTRACT y cómo Copilot hereda y muestra la etiqueta de mayor prioridad.
- Identificar los casos especiales: S/MIME, contraseña, Double Key Encryption, permisos definidos por el usuario, Customer Key y BYOK.
- Aplicar etiquetas de contenedor y etiquetas predeterminadas de biblioteca como vía rápida contra la sobreexposición.
- Planificar el etiquetado automático en simulación antes de ampliar Copilot.
- Describir cómo las etiquetas protegen el conocimiento y las respuestas de los agentes de Copilot Studio.

> **Novedad.** La página de arquitectura de protección de datos de Copilot se actualizó el 3 de noviembre de 2026: con cifrado, el usuario necesita VIEW y EXTRACT; Copilot verifica también el cifrado de Azure RMS sin etiqueta, y Copilot Chat muestra la etiqueta de mayor prioridad, que el contenido nuevo hereda cuando el escenario lo admite ([arquitectura de protección de datos](https://learn.microsoft.com/en-us/copilot/plan/architecture-data-protection-auditing)). Repasa los derechos en [derechos de uso de Rights Management](https://learn.microsoft.com/en-us/purview/rights-management-usage-rights).

> **Atención.** Los permisos definidos por el usuario y Double Key Encryption bloquean a Copilot y a los agentes ([DKE](https://learn.microsoft.com/en-us/purview/double-key-encryption)): sirven para el contenido más crítico, pero ese contenido queda fuera de cualquier respuesta. Copilot no devuelve correos S/MIME y los documentos con contraseña solo se usan si ya están abiertos; Customer Key y BYOK sí se admiten ([Purview para Copilot](https://learn.microsoft.com/en-us/purview/ai-m365-copilot)).

> **Novedad.** Desde junio de 2026 (preview en despliegue), el ajuste de etiqueta que impide las experiencias conectadas que analizan contenido bloquea todas esas experiencias en Word, Excel y PowerPoint para Windows y se extiende a macOS, iOS y Android ([novedades de Purview](https://learn.microsoft.com/en-us/purview/whats-new), [análisis de un MVP](https://office365itpros.com/2026/06/08/blockcontentanalysisservices-label/)). En agosto de 2026 Learn documentó la simulación del etiquetado automático y la pestaña Insights de cada política.

> **Atención.** Copilot Studio: la vista «View sensitivity labels in agent responses» está en preview y activa por defecto, con orígenes como SharePoint, OneDrive, Dataverse, SQL y Azure Blob ([etiquetas en respuestas de agentes](https://learn.microsoft.com/en-us/microsoft-copilot-studio/sensitivity-label-copilot-studio)). El plan de lanzamiento de las etiquetas de Dataverse, con GA prevista para junio de 2026, está archivado y no confirma la GA ([plan de lanzamiento](https://learn.microsoft.com/en-us/power-platform/release-plan/2026wave1/power-platform-governance-administration/view-sensitivity-labels-copilot-studio)). En Copilot Pages y Notebooks, las etiquetas aplican solo a Pages ([cumplimiento de Pages y Notebooks](https://learn.microsoft.com/en-us/microsoft-365/loop/cpcn-compliance-summary?view=o365-worldwide)).

**¿Tienes poco tiempo?**

- [How data is protected and audited in Microsoft 365 and Microsoft Copilot (data protection architecture)](https://learn.microsoft.com/en-us/copilot/plan/architecture-data-protection-auditing) · Documentación
- [Use Microsoft Purview to manage data security & compliance for Microsoft 365 Copilot & Copilot Chat](https://learn.microsoft.com/en-us/purview/ai-m365-copilot) · Documentación
- [Step 3: Protect interactions - Secure and govern Microsoft 365 Copilot agents](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-sc-agents-step3) · Documentación
- [View sensitivity labels in agent responses (preview) - Microsoft Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/sensitivity-label-copilot-studio) · Documentación

### Documentación, cursos y credenciales

- [How data is protected and audited in Microsoft 365 and Microsoft Copilot (data protection architecture)](https://learn.microsoft.com/en-us/copilot/plan/architecture-data-protection-auditing) · Documentación · Oficial · Nuevo · Microsoft Learn · 3 nov 2026. Explica que con cifrado el usuario necesita derechos VIEW y EXTRACT para que Copilot use el contenido, que se hereda la etiqueta de mayor prioridad, que los permisos definidos por el usuario bloquean a los agentes y dónde quedan los datos de interacción para auditoría, retención y eDiscovery.
- [Double Key Encryption (DKE)](https://learn.microsoft.com/en-us/purview/double-key-encryption) · Documentación · Oficial · Nuevo · Microsoft Learn · 27 oct 2026. Explica DKE (una clave bajo control del cliente y otra en Azure), cuándo adoptarlo (solo ~5% de datos altamente sensibles) y qué servicios de Microsoft 365 pierden visibilidad del contenido.
- [Summary of governance, lifecycle, and compliance capabilities for Copilot Pages and Copilot Notebooks](https://learn.microsoft.com/en-us/microsoft-365/loop/cpcn-compliance-summary?view=o365-worldwide) · Documentación · Oficial · Microsoft Learn. Tabla de capacidades de gobierno para Pages y Notebooks (guardados en un contenedor de SharePoint Embedded del usuario compartido con Loop): Cloud Policy, eDiscovery, retención vía «All SharePoint Sites», etiquetas solo en Pages, DLP con sugerencias, Customer Lockbox, y límites como acceso condicional solo a nivel de app, sin Information Barriers ni papelera para Notebooks.
- [Step 3: Protect interactions - Secure and govern Microsoft 365 Copilot agents](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-sc-agents-step3) · Documentación · Oficial · Microsoft Learn · 3 abr 2026. Paso 3 del modelo de despliegue para agentes de Microsoft 365 Copilot: herencia automática de etiquetas desde SharePoint y Dataverse en conversaciones con agentes, DLP para impedir el procesamiento de archivos sensibles y política Risky AI usage de IRM.
- [View sensitivity labels in agent responses (preview) - Microsoft Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/sensitivity-label-copilot-studio) · Documentación · Oficial · Vista previa · Nuevo · Microsoft Learn · 3 oct 2026. Explica cómo los agentes de Copilot Studio muestran un escudo con la etiqueta de mayor prioridad y la etiqueta de cada cita cuando usan conocimiento de SharePoint, OneDrive, SQL, Dataverse, Cosmos, Azure Blob Storage, Word, Excel, Outlook y grupos/usuarios de Office; con cifrado exige VIEW y EXTRACT. *Nota:* Página de preview (03-oct-2026); las etiquetas están activas por defecto para agentes con orígenes de conocimiento compatibles. Complementa la matriz de Purview para Copilot Studio (cifrado solo con etiquetas y solo en SharePoint)
- [Configure usage rights for the Azure Rights Management service](https://learn.microsoft.com/en-us/purview/rights-management-usage-rights) · Documentación · Oficial · Microsoft Learn. Tabla de derechos de uso de Rights Management (VIEW, DOCEDIT, EDIT, EXPORT, EXTRACT, FORWARD, etc.), niveles de permiso, opciones Do Not Forward y Encrypt-Only y conceptos de emisor/propietario y licencia de uso.
- [Use sensitivity labels with Microsoft Loop](https://learn.microsoft.com/en-us/purview/sensitivity-labels-loop) · Documentación · Oficial · Microsoft Learn. Etiquetas en componentes y páginas de Loop (incluidas Copilot Pages) y en áreas de trabajo de Loop como contenedores, con herencia de la etiqueta de la página y de archivos referenciados por Copilot.
- [Learn about the default sensitivity labels and policies to protect your data](https://learn.microsoft.com/en-us/purview/default-sensitivity-labels-policies) · Documentación · Oficial · Microsoft Learn. Describe las etiquetas, la política de publicación y las políticas de auto-etiquetado (cliente y servicio) que Purview crea por defecto para clientes nuevos o que se activan desde DSPM.
- [Step 2: Protect sensitive info in grounding data - Secure and govern Microsoft 365 Copilot agents](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-sc-agents-step2) · Documentación · Oficial · Microsoft Learn · 3 abr 2026. Paso del modelo de despliegue para agentes: etiquetar SharePoint y Dataverse, reducir datos obsoletos con retención, excluir archivos etiquetados con DLP para Copilot y políticas de datos de Dataverse.
- [View sensitivity labels in Microsoft Copilot Studio (Power Platform 2026 release wave 1)](https://learn.microsoft.com/en-us/power-platform/release-plan/2026wave1/power-platform-governance-administration/view-sensitivity-labels-copilot-studio) · Documentación · Oficial · Nuevo · Microsoft Learn (release plan) · 27 ago 2026. Plan de lanzamiento: las columnas de Dataverse autoetiquetadas por el Data Map de Purview muestran su etiqueta al elegir Dataverse como conocimiento y en las citas de Copilot Studio; preview pública 30-nov-2025 y GA prevista jun-2026.

### Comunidad: blogs, libros, newsletters y eventos

- [Microsoft Extends Sensitivity Label Block for Connected Services (BlockContentAnalysisServices)](https://office365itpros.com/2026/06/08/blockcontentanalysisservices-label/) · Blog · MVP · Nuevo · Tony Redmond · Office 365 for IT Pros · 8 jun 2026. Explica la configuración avanzada BlockContentAnalysisServices (solo PowerShell) que impide que Microsoft 365 Copilot y otras experiencias conectadas analicen archivos con cierta etiqueta, ampliada en MC1297982 (may-2026).
- [Container Sensitivity Labels: The Purview “Hack” That Fixes Copilot Oversharing Fast](https://nikkichapple.com/m365-copilot-oversharing-container-labels/) · Blog · MVP · Nuevo · Nikki Chapple · nikkichapple.com · 16 may 2026. Guía comunitaria para usar etiquetas de confidencialidad de contenedor (sitios, grupos y Teams) como control rápido de privacidad, acceso de invitados y uso compartido antes de ampliar Copilot.

**Manos a la obra**

1. `Laboratorio parcial` VIEW y EXTRACT: crea dos etiquetas con cifrado, una que no conceda EXTRACT a un usuario de prueba y otra que sí, aplícalas a dos archivos sintéticos y pide a Copilot Chat que resuma ambos; verifica qué responde y qué etiqueta muestra en la respuesta y en las citas ([arquitectura de protección de datos](https://learn.microsoft.com/en-us/copilot/plan/architecture-data-protection-auditing)). Limitación: con Copilot Chat sin licencia trabajas con archivos que subes al chat, y la herencia en Word, PowerPoint y Outlook requiere licencia de Copilot. Evidencia: capturas y explicación del resultado.
2. `Laboratorio` Etiquetas de contenedor: crea una etiqueta de contenedor (sitio privado, sin invitados y con uso compartido restringido), aplícala a PRUEBA-RRHH-Expedientes y configura una etiqueta predeterminada en la biblioteca de PRUEBA-Legal-Contratos ([etiquetas de contenedor contra la sobreexposición](https://nikkichapple.com/m365-copilot-oversharing-container-labels/)). Evidencia: configuración del sitio y archivos nuevos etiquetados automáticamente.
3. `Laboratorio` Etiquetado automático en simulación: crea una directiva del lado del servicio para tipos de información sintéticos de tu país (por ejemplo, CURP, RUT o DNI) en los sitios PRUEBA-, déjala en simulación y revisa la pestaña Insights ([novedades de Purview](https://learn.microsoft.com/en-us/purview/whats-new)). Evidencia: resultados de la simulación y decisión de ajuste.
4. `Laboratorio` Matriz de etiquetas frente a Copilot: para cada etiqueta registra si cifra, qué derechos concede a cada grupo (VIEW, EXTRACT), si usa permisos definidos por el usuario o Double Key Encryption y el comportamiento esperado de Copilot: usa el contenido, hereda la etiqueta, la muestra o no puede leer ([derechos de uso](https://learn.microsoft.com/en-us/purview/rights-management-usage-rights)). Evidencia: matriz revisada por protección de datos.
5. `Laboratorio parcial` Agente con conocimiento etiquetado: crea en Copilot Studio un agente con un sitio de SharePoint que tenga archivos etiquetados como conocimiento, pruébalo y verifica el escudo con la etiqueta y las citas ([etiquetas en respuestas de agentes](https://learn.microsoft.com/en-us/microsoft-copilot-studio/sensitivity-label-copilot-studio)); luego busca en la auditoría BotCreate y CopilotInteraction ([auditoría de Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-logging-copilot-studio)). Limitación: la prueba de Copilot Studio no publica (para Teams necesitas pago por uso) y la vista de etiquetas está en preview. Evidencia: capturas y registros de auditoría.
6. `Laboratorio parcial` Herencia en Word y PowerPoint: con una cuenta del anillo 0 con licencia de Copilot (comprada en el sandbox), genera un borrador a partir de un documento «Confidencial» y verifica la etiqueta heredada y sus marcas de contenido ([Purview para Copilot](https://learn.microsoft.com/en-us/purview/ai-m365-copilot)). Limitación: requiere licencia de Copilot. Cómo hacerlo en producción: cuentas piloto y documentos sintéticos. Evidencia: documento generado con la etiqueta heredada.
7. `Solo producción` Despliegue del etiquetado automático: después de la simulación, activa la directiva para un área piloto y mide los falsos positivos durante dos semanas ([modelo de despliegue para agentes, paso 2](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-sc-agents-step2)). Por qué en producción: necesitas volumen real de documentos. Cómo hacerlo seguro: simulación previa, alcance por sitios piloto, comunicación a los dueños de los datos y reversión desactivando la directiva. Evidencia: informe de efectividad y aprobación de la ampliación.

**¿Quieres profundizar?**

- [Microsoft Extends Sensitivity Label Block for Connected Services (BlockContentAnalysisServices)](https://office365itpros.com/2026/06/08/blockcontentanalysisservices-label/) · Blog
- [Container Sensitivity Labels: The Purview “Hack” That Fixes Copilot Oversharing Fast](https://nikkichapple.com/m365-copilot-oversharing-container-labels/) · Blog

<a id="m4"></a>

## M4 · DLP para Microsoft 365 Copilot y Copilot Chat

*L300 · ~6 h · Origen: Ruta SC-401 «Secure AI interactions and environments with Microsoft Purview» (interacciones de Copilot) y documentación de la ubicación de DLP para Copilot*

La DLP de Purview tiene una ubicación propia, **Microsoft 365 Copilot and Copilot Chat**, que cubre Copilot, Copilot Chat, Cowork y Copilot en Word, Excel y PowerPoint. Ofrece cuatro controles: bloquear la búsqueda web cuando el prompt contiene tipos de información confidencial (SIT); bloquear prompts con SIT; impedir que Copilot procese archivos y correos etiquetados (que igual aparecen en las citas); y excluir el correo externo del grounding, en preview y pensado contra la inyección de prompts. La DLP de prompts está disponible para todos los usuarios de Copilot y Copilot Chat, incluidos E3 y Business; la exclusión por etiquetas exige E5, A5, Purview Suite, E5 Information Protection & Governance u Office 365 E5.

Microsoft crea además la política **«Default DLP policy - Protect sensitive M365 Copilot interactions»**, que detecta más de 100 SIT en prompts (incluidos el DNI y el CUIT o CUIL de Argentina, la cédula de Chile, la de Colombia y la CURP de México), cubre a todos los usuarios, arranca en **modo simulación** y genera una alerta y un correo de baja severidad, sin sugerencias al usuario. Antes de pasar a bloqueo conoce los límites: la ubicación solo existe en la plantilla personalizada, no combina SIT y etiquetas en la misma regla, cubre correos desde el 1 de enero de 2025, no analiza archivos subidos al prompt y los cambios tardan hasta 4 horas.

La protección se extiende más allá del chat. Las políticas de Copilot se aplican a Cowork desde octubre de 2026, solo sobre el texto y no sobre los archivos subidos; Copilot Chat en la web admite Endpoint DLP para bloquear el pegado de contenido sensible; si el conocimiento está en SharePoint, la ubicación de Copilot impide que los agentes de Copilot Studio procesen contenido con ciertas etiquetas; y la DLP de búsqueda web alcanza a los agentes publicados en Microsoft 365 Copilot. Cuando la DLP no llega a evaluar a tiempo, la auditoría lo marca con `DLPEvaluationDeferred`. Se profundiza en el programa de Purview DLP, módulo M3.

**Por qué importa**

Las etiquetas protegen el contenido; la DLP para Copilot protege la conversación. Evita que un prompt con datos personales viaje a la web, que Copilot procese archivos con la etiqueta más restrictiva o que un correo externo envenenado entre al grounding. Empezar en simulación con la política predeterminada da una medición objetiva del riesgo antes de bloquear y reduce la fricción con los usuarios.

**Qué vas a lograr**

- Configurar la ubicación Microsoft 365 Copilot and Copilot Chat con sus cuatro controles y sus límites.
- Revisar y ajustar la política DLP predeterminada antes de pasarla de simulación a bloqueo.
- Decidir qué controles están disponibles con E3 y cuáles requieren E5 o Purview Suite.
- Interpretar alertas, eventos DLP rule match y el campo DLPEvaluationDeferred de la auditoría.
- Extender la protección a Cowork, a Copilot Chat en la web y a los agentes publicados en Microsoft 365.

> **Atención.** Estado de la DLP de prompts: el blog oficial del 21 de abril de 2026 dice que «entra en GA» para todos los usuarios de Copilot y Copilot Chat ([blog de DLP para Copilot](https://techcommunity.microsoft.com/blog/microsoft-security-blog/safeguarding-sensitive-data-in-microsoft-365-copilot-interactions-dlp-for-micros/4512497)), pero la página de Learn del 27 de octubre de 2026 la sigue rotulando como preview en despliegue ([DLP para Copilot](https://learn.microsoft.com/en-us/purview/dlp-microsoft365-copilot-location-learn-about)). Enséñala como «disponible en despliegue» y verifica en tu tenant que la acción aparece.

> **Novedad.** La política predeterminada «Default DLP policy - Protect sensitive M365 Copilot interactions» (MC1182689 y MC1181998) detecta más de 100 SIT, incluidos el DNI y el CUIT o CUIL de Argentina, la cédula de Chile, la de Colombia y la CURP de México; cubre a todos los usuarios, arranca en simulación y genera una alerta y un correo de baja severidad, sin sugerencias ([política predeterminada](https://learn.microsoft.com/en-us/purview/dlp-microsoft365-copilot-location-default-policy)).

> **Qué cambió.** Desde octubre de 2026 las políticas de Copilot se aplican a Cowork, y la DLP de prompts y de búsqueda web solo evalúa el texto, no los archivos subidos ([MC1477182](https://mc.merill.net/message/MC1477182)). La exclusión de correo externo está en preview, solo evalúa el dominio del remitente y tiene GA prevista para fines de enero de 2027 ([análisis de un MVP](https://office365itpros.com/2026/07/29/dlp-external-email-copilot/)).

> **Consejo Ninja.** Para automatizar, `New-DlpComplianceRule` incluye el parámetro RestrictWebGrounding y `New-DlpCompliancePolicy` admite la ubicación de Copilot en -Locations con JSON ([New-DlpComplianceRule](https://learn.microsoft.com/en-us/powershell/module/exchangepowershell/new-dlpcompliancerule?view=exchange-ps)). La ubicación de Copilot solo ofrece condiciones de etiquetas, SIT y correo externo, sin condición de nivel de riesgo de Protección adaptativa ([consideraciones de DSPM for AI](https://learn.microsoft.com/en-us/purview/dspm-for-ai-considerations)). Investigar alertas DLP en Defender XDR requiere licencias E5 o equivalentes ([alertas DLP en Defender XDR](https://learn.microsoft.com/en-us/defender-xdr/dlp-investigate-alerts-defender)).

**¿Tienes poco tiempo?**

- [Learn about using Microsoft Purview DLP to protect interactions with Microsoft 365 Copilot, Copilot Chat, and Cowork](https://learn.microsoft.com/en-us/purview/dlp-microsoft365-copilot-location-learn-about) · Documentación
- [Learn about the default DLP policy for Microsoft 365 Copilot location](https://learn.microsoft.com/en-us/purview/dlp-microsoft365-copilot-location-default-policy) · Documentación
- [Safeguarding Sensitive Data in Microsoft 365 Copilot Interactions: DLP for Microsoft 365 Copilot](https://techcommunity.microsoft.com/blog/microsoft-security-blog/safeguarding-sensitive-data-in-microsoft-365-copilot-interactions-dlp-for-micros/4512497) · Blog oficial
- [How to Deploy Microsoft Purview DLP for Copilot and Generative AI](https://nikkichapple.com/microsoft-purview-dlp-copilot-genai-setup-guide/) · Blog

**Controles de la ubicación Microsoft 365 Copilot and Copilot Chat**

| Control | Qué evita | Licencia | Estado al 6 de noviembre de 2026 | Límite clave |
|---|---|---|---|---|
| Bloquear prompts con SIT | Datos sensibles escritos en el prompt | Todos los usuarios de Copilot y Copilot Chat, incluidos E3 y Business | Preview en despliegue según Learn (27 de octubre de 2026); GA según el blog del 21 de abril de 2026 | No analiza archivos subidos al prompt |
| Bloquear la búsqueda web con SIT | Que prompts sensibles se envíen a Bing | Probablemente igual que la DLP de prompts: confírmalo en la descripción del servicio | Sin rótulo de preview en Learn; preview pública en el blog de abril | Se extiende a agentes de Copilot Studio publicados en Microsoft 365 Copilot |
| Impedir el procesamiento de archivos y correos etiquetados | Que Copilot use contenido con ciertas etiquetas | E5 o A5, Purview Suite, E5 Information Protection & Governance u Office 365 E5, más Copilot | GA desde noviembre de 2024 | Los elementos siguen apareciendo en las citas; no se combina con SIT en la misma regla |
| Excluir correo externo | Correos de remitentes externos en el grounding (inyección de prompts) | No confirmada en las fuentes | Preview; GA prevista a fines de enero de 2027 | Solo evalúa el dominio del remitente |
| Política predeterminada | Más de 100 SIT en prompts, incluidos los de Argentina, Chile, Colombia y México | Igual que la DLP de prompts | Simulación por defecto | Alerta y correo de baja severidad, sin sugerencias al usuario |
| Endpoint DLP en Copilot Chat web | Pegado de contenido sensible y archivos etiquetados | E5 (Endpoint DLP; indicativo) | Disponible | Solo la versión web y en dispositivos incorporados |
| Agentes con conocimiento en SharePoint | Que agentes de Copilot Studio para Teams, SharePoint y Microsoft 365 Copilot procesen contenido etiquetado | Igual que la exclusión por etiquetas | Disponible | Solo cuando el conocimiento está en SharePoint |

Fuentes: [DLP para Copilot](https://learn.microsoft.com/en-us/purview/dlp-microsoft365-copilot-location-learn-about), [política predeterminada](https://learn.microsoft.com/en-us/purview/dlp-microsoft365-copilot-location-default-policy), [descripción del servicio de Purview](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description), [blog del 21 de abril de 2026](https://techcommunity.microsoft.com/blog/microsoft-security-blog/safeguarding-sensitive-data-in-microsoft-365-copilot-interactions-dlp-for-micros/4512497), [correo externo](https://office365itpros.com/2026/07/29/dlp-external-email-copilot/), [Purview para Copilot](https://learn.microsoft.com/en-us/purview/ai-m365-copilot) y [Purview para Copilot Studio](https://learn.microsoft.com/en-us/purview/ai-copilot-studio).

### Documentación, cursos y credenciales

- [Learn about using Microsoft Purview DLP to protect interactions with Microsoft 365 Copilot, Copilot Chat, and Cowork](https://learn.microsoft.com/en-us/purview/dlp-microsoft365-copilot-location-learn-about) · Documentación · Oficial · Nuevo · Microsoft Learn · 27 oct 2026. Referencia de la ubicación DLP «Microsoft 365 Copilot and Copilot Chat» (incluye Cowork y Copilot en Word, Excel y PowerPoint): bloquear la búsqueda web con SIT, bloquear prompts con SIT (preview en despliegue), impedir procesar archivos y correos etiquetados y excluir correo externo (preview).
- [Learn about the default DLP policy for Microsoft 365 Copilot location](https://learn.microsoft.com/en-us/purview/dlp-microsoft365-copilot-location-default-policy) · Documentación · Oficial · Microsoft Learn · 24 mar 2026. Política predeterminada «Default DLP policy - Protect sensitive M365 Copilot interactions»: detecta más de 100 SIT en prompts (incluidos DNI y CUIT/CUIL de Argentina, cédula de Chile y de Colombia y CURP de México), cubre a todos los usuarios y arranca en modo simulación, generando alerta y correo de baja severidad sin sugerencias al usuario.
- [MC1477182 - Microsoft Purview: Data Loss Prevention for Microsoft Cowork](https://mc.merill.net/message/MC1477182) · Documentación · Oficial · Nuevo · Microsoft 365 Message Center Archive (mc.merill.net) · 22 sep 2026. MC1477182 (Roadmap 570845): las directivas DLP de Microsoft Copilot se aplican automáticamente a Microsoft Cowork (etiquetas en grounding, bloqueo de prompts y de búsqueda web con SIT); preview desde fines de sep-2026 y GA mundial de mediados a fines de oct-2026.
- [Help dynamically mitigate risks with Adaptive Protection](https://learn.microsoft.com/en-us/purview/insider-risk-management-adaptive-protection) · Documentación · Oficial · Nuevo · Microsoft Learn · 26 jun 2026. Explica Adaptive Protection: niveles de riesgo interno (Elevated, Moderate, Minor) calculados por IRM que aplican dinámicamente controles de DLP, gestión del ciclo de vida de datos (preview) y Acceso condicional (preview).
- [Investigate data loss prevention alerts with Microsoft Defender XDR](https://learn.microsoft.com/en-us/defender-xdr/dlp-investigate-alerts-defender) · Documentación · Oficial · Microsoft Learn. Explica la investigación de alertas DLP en la cola unificada de incidentes de Defender XDR, con licencias, roles mínimos, resumen con Security Copilot y búsqueda avanzada.

### Anuncios y blogs oficiales

- [Safeguarding Sensitive Data in Microsoft 365 Copilot Interactions: DLP for Microsoft 365 Copilot](https://techcommunity.microsoft.com/blog/microsoft-security-blog/safeguarding-sensitive-data-in-microsoft-365-copilot-interactions-dlp-for-micros/4512497) · Blog oficial · Empleado de Microsoft · Aaron Thorp · Microsoft Security Community Blog · 21 abr 2026. Explica la GA de DLP para prompts de Microsoft 365 Copilot y Copilot Chat (incluida para todos sus usuarios), el control por etiquetas desde noviembre de 2024 y la preview de bloqueo de búsqueda web con SIT.

### Laboratorios, GitHub y herramientas

- [MC1304291 - Microsoft Purview: Data loss prevention inline controls for prompts in Microsoft Foundry apps and agents](https://mc.merill.net/message/MC1304291) · Herramienta · Oficial · Nuevo · Microsoft 365 Message Center (archivo mc.merill.net) · 17 jun 2026. Anuncia DLP en línea para prompts de apps y agentes de Microsoft Foundry: preview desde mediados de mayo de 2026 y GA de octubre de 2026; requiere activar Purview en Foundry y una suscripción de pago por uso.

### Comunidad: blogs, libros, newsletters y eventos

- [How to Deploy Microsoft Purview DLP for Copilot and Generative AI](https://nikkichapple.com/microsoft-purview-dlp-copilot-genai-setup-guide/) · Blog · Comunidad · Nuevo · Nikki Chapple · nikkichapple.com · 16 may 2026. Guía práctica con los seis controles DLP de mayor valor para Copilot e IA generativa (prompts, búsqueda web, contenido etiquetado, pegar/subir a sitios de IA, Edge) y estrategia de despliegue.
- [DLP Policy for Copilot Can Block Web Searches](https://office365itpros.com/2026/04/16/dlp-policy-for-copilot-web/) · Blog · MVP · Tony Redmond · Office 365 for IT Pros · 16 abr 2026. Análisis de la acción DLP que impide a Copilot realizar búsquedas web cuando el prompt contiene SIT, y de la directiva predeterminada "Protect sensitive M365 Copilot interactions".
- [New DLP Rule to Block Copilot from Processing External Email](https://office365itpros.com/2026/07/29/dlp-external-email-copilot/) · Blog · MVP · Vista previa · Nuevo · Tony Redmond · Office 365 for IT Pros · 29 jul 2026. Prueba práctica del control (preview) que excluye correos de dominios externos del grounding de Copilot para reducir inyección de prompts, con su efecto retroactivo sobre mensajes existentes. *Nota:* Según MC1301714, GA prevista a fines de enero de 2027; depende de la lista de dominios aceptados del tenant
- [DLP Policy for Copilot Extends to All Storage Locations](https://office365itpros.com/2026/02/24/dlp-policy-for-copilot-storage/) · Blog · MVP · Tony Redmond · Office 365 for IT Pros · 24 feb 2026. Explica cómo la directiva DLP para Copilot pasó a cubrir archivos Office etiquetados en cualquier almacenamiento (local u otras nubes) gracias al Augmentation Loop de Office.

**Manos a la obra**

1. `Laboratorio parcial` Revisa la política predeterminada en simulación: localízala, revisa sus SIT (incluidos los de tu país), su alcance y sus acciones, genera actividad con prompts sintéticos en Copilot Chat y analiza las coincidencias ([política predeterminada](https://learn.microsoft.com/en-us/purview/dlp-microsoft365-copilot-location-default-policy)). Limitación: la simulación puede tardar hasta 15 días en dar resultados representativos y el laboratorio tiene poco volumen. Evidencia: informe de simulación con los ajustes que harías.
2. `Laboratorio` Política personalizada con dos reglas en la ubicación de Copilot: una para el SIT «Argentina National Identity (DNI) Number» (o el de tu país) con la acción de bloquear búsquedas web y otra para bloquear el procesamiento de prompts; prueba con Copilot Chat y revisa la alerta y el evento DLP rule match ([DLP para Copilot](https://learn.microsoft.com/en-us/purview/dlp-microsoft365-copilot-location-learn-about)). Los cambios tardan hasta 4 horas y el bloqueo de prompts puede no haber llegado aún a tu tenant. Evidencia: captura del bloqueo y del evento.
3. `Laboratorio parcial` Exclusión de contenido etiquetado: crea una regla que impida a Copilot procesar archivos y correos con tu etiqueta más restrictiva y comprueba que Copilot no los resume, aunque sigan apareciendo en las citas; recuerda que no se mezclan SIT y etiquetas en la misma regla. Limitación: requiere E5 y una licencia de Copilot (sandbox) ([descripción del servicio de Purview](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)). Evidencia: prueba con y sin la regla.
4. `Laboratorio` Endpoint DLP para Copilot Chat en la web: en la VM Windows 11 incorporada crea una regla que bloquee pegar contenido sensible en Copilot Chat y prueba con datos sintéticos ([Purview para Copilot](https://learn.microsoft.com/en-us/purview/ai-m365-copilot)). Evidencia: notificación de bloqueo y evento en el explorador de actividad.
5. `Laboratorio` DLP como código: exporta la configuración de tus políticas y revisa con PowerShell la ubicación de Copilot y el parámetro RestrictWebGrounding ([New-DlpComplianceRule](https://learn.microsoft.com/en-us/powershell/module/exchangepowershell/new-dlpcompliancerule?view=exchange-ps), [New-DlpCompliancePolicy](https://learn.microsoft.com/en-us/powershell/module/exchangepowershell/new-dlpcompliancepolicy?view=exchange-ps)). Evidencia: script versionado que recrea la política del laboratorio.
6. `Laboratorio parcial` Evaluaciones diferidas: busca en la auditoría registros CopilotInteraction con DLPEvaluationDeferred y DLPEvaluationDeferredReason, e interpreta la máscara de bits (Prompt=1, Response=2, Grounding=4, WebGrounding=8) ([auditoría de Copilot](https://learn.microsoft.com/en-us/purview/audit-copilot)). Limitación: son eventos raros y quizá no aparezcan en el laboratorio. Evidencia: consulta guardada y procedimiento de revisión.
7. `Solo producción` De simulación a bloqueo: aplica la DLP de prompts en simulación a un grupo piloto con Copilot, revisa dos semanas de coincidencias con el dueño del proceso y pasa a bloqueo con sugerencias y una URL de cumplimiento propia ([DLP para Copilot](https://learn.microsoft.com/en-us/purview/dlp-microsoft365-copilot-location-learn-about)). Por qué en producción: necesitas prompts reales para medir falsos positivos. Cómo hacerlo seguro: simulación previa, grupo piloto informado, aprobación de privacidad y reversión inmediata desactivando la regla. Evidencia: informe de simulación y aprobación del cambio.

**¿Quieres profundizar?**

- [New DLP Rule to Block Copilot from Processing External Email](https://office365itpros.com/2026/07/29/dlp-external-email-copilot/) · Blog
- [DLP Policy for Copilot Can Block Web Searches](https://office365itpros.com/2026/04/16/dlp-policy-for-copilot-web/) · Blog

<a id="m5"></a>

## M5 · Gobierno de agentes en Microsoft 365: inventario, tienda, conectores y permisos

*L300 · ~6 h · Origen: Ruta de Learn «Explore Microsoft 365 Copilot and agent administration» (ciclo de vida, aprobación y permisos de agentes) y guía de administración de agentes de Microsoft 365*

El centro de administración de Microsoft 365 es el registro central de agentes. Allí aparecen los agentes declarativos y de motor personalizado de Copilot Studio, los de Agent Builder, los de SharePoint, los de Microsoft Foundry y los del Agents Toolkit. Los usuarios los encuentran en la **Agent Store**, con categorías como publicados por la organización (requieren aprobación del administrador), compartidos por su creador, de Microsoft, de socios y Frontier. El administrador puede habilitar, asignar, bloquear o quitar cada agente, y el panel **Agents > Overview** (20 de octubre de 2026) resume solicitudes pendientes, agentes sin dueño, agentes en riesgo y agentes con excepciones. Solo AI Administrator o Global Administrator aprueban solicitudes y asignan dueños.

Lo que un agente puede leer y hacer depende de piezas que se gobiernan por separado. Los **conectores de Copilot** (antes Graph connectors) se habilitan o bloquean en el centro de administración, y su administración puede delegarse al AI Administrator. La **carga de paquetes avanzados** decide quién sube agentes declarativos con acciones o servidores MCP: todos, nadie o grupos específicos. Los agentes de SharePoint dependen de la licencia de Copilot o de un grupo ligado al pago por uso y respetan los permisos sobre sus fuentes. Ojo: bloquear un plugin no revoca el consentimiento, no borra los datos indexados por un conector ni detiene un servidor MCP remoto.

La frontera con Agent 365 importa. Según la descripción del servicio del 1 de octubre de 2026, los planes de Microsoft 365 incluyen el inventario del Agent Registry, las acciones básicas (publicar, desplegar, bloquear, eliminar, aprobar, asignar y reasignar dueño), las reglas de ciclo de vida y la sincronización desde plataformas externas. Requieren Agent 365 o E7 las plantillas de políticas, la observabilidad, el control de herramientas y servidores MCP a nivel de tenant, la Graph API del registro y los controles de Entra, Purview, Defender e Intune para agentes. Como parte de la documentación vive bajo Agent 365, valida en tu tenant qué ves sin esa licencia. El ciclo de vida completo llega en [O3](04_Nivel_4_Gobierno_y_operacion_continua.md#o3).

**Por qué importa**

Cada usuario con Copilot puede crear y compartir agentes, y cada agente amplía la superficie: datos que lee, acciones que ejecuta y conectores que indexa. Gobernar el catálogo desde el centro de administración —quién publica, quién sube paquetes con acciones, qué conectores existen y quién usa qué— evita la proliferación sin dueño con herramientas incluidas en Microsoft 365, sin depender de Agent 365.

**Qué vas a lograr**

- Inventariar los agentes del tenant por tipo, creador, dueño y estado en el Agent Registry.
- Configurar la aprobación de agentes publicados por la organización y su disponibilidad por usuarios y grupos.
- Restringir la carga de paquetes avanzados (acciones y servidores MCP) a creadores aprobados.
- Gobernar conectores de Copilot, plugins y agentes de SharePoint, sabiendo qué no revierte un bloqueo.
- Delimitar qué funciones del centro de administración están incluidas en Microsoft 365 y cuáles requieren Agent 365.

> **Atención.** ¿Qué parte del centro de administración es Agent 365? La documentación de agentes también se publica bajo /microsoft-agent-365/ y la de plugins se titula «Manage plugins with Microsoft Agent 365» ([plugins](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/govern-plugins)), pero la descripción del servicio del 1 de octubre de 2026 dice que el inventario, las acciones básicas, las reglas de ciclo de vida y la sincronización están incluidos en los planes de Microsoft 365 ([descripción del servicio](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-agent-365/microsoft-agent-365)). Valida en tu tenant qué ves sin licencias de Agent 365 antes de documentar el procedimiento; la tabla [Qué queda fuera](00_Programa.md#fuera-de-alcance) resume cada capacidad y su alternativa.

> **Consejo Ninja.** Bloquear un plugin no revoca el consentimiento, no borra los datos que indexó un conector ni detiene un servidor MCP remoto: cada objeto (paquete, agente, skill, servidor MCP, conector, conexión y servicio externo) tiene su propio control ([guía de plugins](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/administrator-guide), [administrar plugins](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/manage)). Tu procedimiento de contención debe cubrir todas esas capas; el playbook completo llega en [A8](03_Nivel_3_Avanzado.md#a8).

> **Novedad.** El panel Agents > Overview (20 de octubre de 2026) muestra métricas de 30 días y tarjetas de solicitudes pendientes, agentes sin dueño, agentes en riesgo y agentes con excepciones; las métricas de agentes de terceros requieren Agent 365 ([Agents > Overview](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-365-overview?view=o365-worldwide)). Las reglas de gestión permiten reasignar al gerente del creador los agentes de Agent Builder sin dueño y bloquear agentes sin dueño ni uso ([ajustes de agentes](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-settings?view=o365-worldwide)).

> **Atención.** Researcher y Analyst: la página de administración de agentes dice que no quedan sujetos a los ajustes de agentes ([administrar agentes](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-copilot-agents-integrated-apps?view=o365-worldwide)), mientras el FAQ de Researcher dice que el administrador puede bloquearlos ([FAQ de Researcher](https://learn.microsoft.com/en-us/copilot/manage/faq-researcher)). Verifícalo en tu tenant antes de comprometerte con un control.

**¿Tienes poco tiempo?**

- [Manage agents in the Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-copilot-agents-integrated-apps?view=o365-worldwide) · Documentación
- [Agents admin guide for Microsoft 365](https://learn.microsoft.com/en-us/microsoft-365/copilot/agent-essentials/m365-agents-admin-guide) · Documentación
- [Manage advanced package uploads for Microsoft Copilot](https://learn.microsoft.com/en-us/copilot/manage/configure-copilot-advanced-package-uploads) · Documentación
- [Microsoft Agent 365 - Service Descriptions](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-agent-365/microsoft-agent-365) · Documentación

### Documentación, cursos y credenciales

- [Manage advanced package uploads for Microsoft Copilot](https://learn.microsoft.com/en-us/copilot/manage/configure-copilot-advanced-package-uploads) · Documentación · Oficial · Nuevo · Microsoft Learn · 3 nov 2026. Ajuste de Copilot > Settings > All settings > Advanced package uploads para decidir quién puede subir paquetes avanzados (agentes declarativos con acciones o servidores MCP): todos, nadie o usuarios/grupos específicos; los paquetes básicos (solo instrucciones) siguen permitidos.
- [Manage agents in the Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-copilot-agents-integrated-apps?view=o365-worldwide) · Documentación · Oficial · Microsoft Learn. Describe la gestión de agentes (habilitar, deshabilitar, asignar, bloquear, quitar) en el Agent Registry, los tipos de agentes (publicados por la organización, compartidos por su creador, de Microsoft, de socios y Frontier) y el flujo de envío y aprobación hacia la Agent Store.
- [Agents admin guide for Microsoft 365](https://learn.microsoft.com/en-us/microsoft-365/copilot/agent-essentials/m365-agents-admin-guide) · Documentación · Oficial · Microsoft Learn. Guía para administradores que compara tres escenarios (Copilot Chat sin facturación por uso, Copilot Chat con facturación por uso y Microsoft Copilot con licencia) y cubre creación, políticas, ciclo de vida, asignación y seguridad de agentes.
- [Manage access to agents in SharePoint](https://learn.microsoft.com/en-us/sharepoint/manage-access-agents-in-sharepoint) · Documentación · Oficial · Microsoft Learn. Cómo controlar quién usa los agentes de SharePoint (licencia de Copilot, plan de servicio «Microsoft Copilot for SharePoint» por usuario o grupos de la directiva PAYG), qué datos ven (permisos del sitio, archivos .agent, Restricted Access Control) y dónde están disponibles.
- [Administer Microsoft 365 Copilot plugins](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/administrator-guide) · Documentación · Oficial · Microsoft Learn. Guía del ciclo de vida de plugins (paquete, agente incluido, skill, servidor MCP, conector, conexión y servicio externo) que subraya que cada objeto puede tener su propio control y que bloquear uno no gobierna automáticamente sus dependencias.
- [Grant administrative rights to AI Administrators to manage Microsoft 365 Copilot connectors](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/connector-admin-delegation) · Documentación · Oficial · Microsoft Learn. Cómo delegar al AI Administrator el registro de aplicaciones y el consentimiento de los permisos ExternalItem.ReadWrite.OwnedBy y ExternalConnection.ReadWrite.OwnedBy para crear e indexar conectores de Copilot sin depender del Global Administrator (script Connector.Cmd 1.4+).

**Manos a la obra**

1. `Laboratorio parcial` Gobierno de agentes sin Agent 365: en Agents > All agents > Registry identifica los agentes compartidos por su creador, bloquea uno de prueba y crea la regla que bloquea agentes sin dueño ni uso ([acciones sobre agentes](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-actions?view=o365-worldwide), [ajustes de agentes](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-settings?view=o365-worldwide)). Limitación: con solo Copilot Chat ves agentes con datos web, y las plantillas («Apply template») quedan fuera de alcance. Evidencia: estado «Blocked» en el registro y en una conversación nueva.
2. `Laboratorio` Carga de paquetes avanzados: configura «Specific users or groups» con el grupo de creadores aprobados y comprueba que una cuenta fuera del grupo no puede subir un agente declarativo con acciones ([carga de paquetes avanzados](https://learn.microsoft.com/en-us/copilot/manage/configure-copilot-advanced-package-uploads)). Evidencia: configuración y error documentado de la cuenta no autorizada.
3. `Laboratorio parcial` Aprobación de un agente de la organización: crea un agente con datos web, envíalo al catálogo de la organización y apruébalo en Agents > All agents > Requests con una audiencia limitada a un grupo ([solicitudes de agentes](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-requests?view=o365-worldwide)). Limitación: aprobar exige AI Administrator o Global Administrator, y con solo Copilot Chat los agentes usan datos web. Evidencia: solicitud aprobada, audiencia y visibilidad en la Agent Store solo para el grupo.
4. `Laboratorio` Inventario de agentes: exporta el registro a Excel desde el centro de administración y completa por agente tipo, creador, dueño, audiencia, conocimiento, acciones, conectores y última actualización; marca los que no tienen dueño ([registro de agentes](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-registry?view=o365-worldwide)). Evidencia: inventario v1 con hallazgos.
5. `Laboratorio` Conectores de Copilot: revisa los conectores habilitados, bloquea uno que no esté aprobado y delega su administración al AI Administrator con el script Connector.Cmd 1.4 o posterior ([delegación de conectores](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/connector-admin-delegation)). Evidencia: estado de los conectores y permisos delegados.
6. `Laboratorio parcial` Agentes de SharePoint y pago por uso: asocia una directiva de facturación de pago por uso a un grupo piloto, crea un agente de SharePoint en un sitio de prueba y verifica que una cuenta sin licencia y fuera del grupo no puede usarlo y que RAC restringe el sitio ([acceso a agentes de SharePoint](https://learn.microsoft.com/en-us/sharepoint/manage-access-agents-in-sharepoint)). Limitación: genera consumo y el presupuesto no lo corta. Evidencia: prueba con ambas cuentas e informe de consumo.
7. `Laboratorio` Procedimiento de contención de un plugin o agente: bloqueo en el centro de administración, revocación del consentimiento en Entra, eliminación de la conexión y de los datos indexados del conector y bloqueo del endpoint del servidor MCP ([administrar plugins](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/manage)). Evidencia: runbook revisado por el SOC con tiempos objetivo.
8. `Solo producción` Revisión mensual de Agents > Overview: solicitudes pendientes, agentes sin dueño, en riesgo y con excepciones, con asignación de dueños y decisiones de bloqueo ([Agents > Overview](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-365-overview?view=o365-worldwide)). Por qué en producción: necesita agentes y uso reales. Cómo hacerlo seguro: AI Administrator activado por PIM solo durante la revisión, decisiones registradas y aviso al creador antes de bloquear. Evidencia: acta mensual.

<a id="m6"></a>

## M6 · Copilot Studio: estrategia de entornos y Managed Environments

*L300 · ~7 h · Origen: Ruta de Learn «Evaluate, publish, and manage agents in Microsoft Copilot Studio» (estrategia de gobierno y seguridad) y guía de gobierno por zonas de Copilot Studio*

En Copilot Studio, el **entorno** de Power Platform es el perímetro de seguridad: define quién crea, qué conectores existen, dónde viven los datos y qué reglas aplican. Todos los empleados acceden al **entorno predeterminado**, y Microsoft recomienda endurecerlo: limitar el rol Power Platform Administrator con PIM, renombrarlo como entorno de productividad personal, publicar contenido de bienvenida, activar Managed Environments, límites de uso compartido, una directiva de datos y aislamiento entre tenants. Compartir con «Everyone», que incluye a los invitados, está desactivado por defecto y debe seguir así. Para producción se usa un entorno propio: la guía de ALM propone desarrollo y prueba como sandbox y producción como production, cada uno restringido con un grupo de Entra.

La guía de gobierno por **zonas** ordena la estrategia: zona 1 para desarrollo ciudadano (solo conectores de Microsoft 365 y Power Platform, entornos de desarrollador con enrutamiento y sin compartir), zona 2 para creadores aprobados (grupos de entornos, políticas avanzadas de conectores, ALM y aprobación de TI para publicar) y zona 3 para desarrollo profesional con los controles más estrictos. Las herramientas son los **Managed Environments** (grupos de entornos, límites de uso compartido, usage insights, directivas de datos, canalizaciones, solution checker, firewall de IP, CMK, Lockbox y VNet) y las **reglas de grupos de entornos** (28 en la página del 15 de octubre de 2026), que cada entorno del grupo hereda sin excepciones. Su uso activo exige licencias independientes o el medidor de pago por uso.

Dos cambios de calendario afectan a todos. El **enrutamiento de entornos**, desactivado por defecto, envía a cada creador a su entorno de desarrollador administrado; en cambio, el enrutamiento de Copilot Managed Runtime (preview) está activo en todos los tenants y no se puede desactivar. Y los entornos de desarrollador **no administrados** se retiran: no se crean nuevos desde el 15 de noviembre de 2026, se suspenden desde el 15 de diciembre de 2026 y se eliminan desde el 15 de enero de 2027, con sus agentes; el Developer Plan no incluye derechos de Managed Environments. Por último, la tarjeta «Generative AI features» de cada entorno decide si los datos pueden moverse entre regiones, algo que debes revisar con privacidad.

**Por qué importa**

En Copilot Studio el entorno es el perímetro. Una estrategia por zonas con Managed Environments evita que el entorno predeterminado se convierta en producción de facto, aplica reglas que ningún creador puede saltar y protege a la organización de la retirada de los entornos de desarrollador, que desde el 15 de enero de 2027 puede llevarse agentes que nadie inventarió.

**Qué vas a lograr**

- Endurecer el entorno predeterminado según la guía de Microsoft.
- Diseñar una estrategia de entornos por zonas con grupos de entornos y reglas.
- Explicar qué aporta Managed Environments y qué licencias exige su uso.
- Configurar el enrutamiento de entornos y planificar la retirada de los entornos de desarrollador no administrados.
- Decidir el movimiento de datos entre regiones y los controles de cifrado y red para producción.

> **Qué cambió.** Retiro de los entornos de desarrollador no administrados: sin entornos nuevos desde el 15 de noviembre de 2026, suspensión desde el 15 de diciembre de 2026 y eliminación desde el 15 de enero de 2027, incluidos sus agentes; solo quedarán entornos de desarrollador administrados, uno por usuario ([Developer Plan](https://learn.microsoft.com/en-us/power-platform/developer/plan), [cambios importantes](https://learn.microsoft.com/en-us/power-platform/important-changes-coming)). Dataverse for Teams tampoco crea entornos nuevos desde el 15 de noviembre de 2026.

> **Atención.** Licencias de Managed Environments: el derecho viene en las licencias independientes (Power Apps, Power Automate, Copilot Studio y su pago por uso, Power Pages y Dynamics 365) y en «Copilot Studio para Microsoft 365 Copilot» solo para funciones de Copilot Studio; al activarlo, todo uso activo del entorno requiere licencia independiente o medidor. Los avisos de cumplimiento empezaron en junio de 2026 y desde febrero de 2027 se bloquea la apertura de apps a usuarios sin licencia ([licencias de Managed Environments](https://learn.microsoft.com/en-us/power-platform/admin/managed-environment-licensing)).

> **Atención.** Movimiento de datos entre regiones: en la tarjeta «Generative AI features» de cada entorno se consiente el movimiento de datos entre regiones, Bing, los servicios de Microsoft 365 y el flex routing. Para entornos en regiones como Brasil, Canadá o Japón, Azure OpenAI y Bing se procesan en EE. UU., y algunos modelos pueden procesar fuera de la región aun con la restricción ([movimiento de datos](https://learn.microsoft.com/en-us/power-platform/admin/geographical-availability-copilot)). Revísalo con privacidad para cada país de MCSA.

> **Qué cambió.** El CoE Starter Kit dejó de mantenerse el 7 de mayo de 2026: sus escenarios pasan a Inventory, Usage, Monitor y Actions del centro de administración de Power Platform ([CoE Starter Kit](https://learn.microsoft.com/en-us/power-platform/guidance/coe/starter-kit)), y el Power CAT Copilot Studio Kit se llama ahora Copilot Agent Kit ([Copilot Agent Kit](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/kit-overview)). Los nombres de las zonas varían: Learn las describe por tipo de desarrollo y el whitepaper v3.2 las llama productividad personal, colaboración de equipo y gestionada por la empresa ([whitepaper v3.2](https://techcommunity.microsoft.com/blog/copilot-studio-blog/new-updates-administering-and-governing-agents-whitepaper-v3-2/4517044)).

**¿Tienes poco tiempo?**

- [Implement a zoned governance strategy - Microsoft Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/sec-gov-phase2) · Documentación
- [Secure the default environment - Power Platform](https://learn.microsoft.com/en-us/power-platform/guidance/adoption/secure-default-environment) · Documentación
- [Managed environments overview - Power Platform](https://learn.microsoft.com/en-us/power-platform/admin/managed-environment-overview) · Documentación
- [Rules for environment groups - Power Platform](https://learn.microsoft.com/en-us/power-platform/admin/environment-groups-rules) · Documentación

**Estrategia de entornos por zonas para Copilot Studio**

| Zona o entorno | Para quién | Entornos | Conectores y datos | Uso compartido y canales | Publicación y ALM |
|---|---|---|---|---|---|
| Entorno predeterminado | Todos los empleados; no es zona de construcción | Renombrado como productividad personal, administrado y con contenido de bienvenida | Directiva de datos estricta: sin chat sin autenticación, sin Direct Line ni Skills; HTTP solo con filtrado | Sin compartir con «Everyone»; límites de uso compartido | No se publica desde aquí; el enrutamiento lleva a cada creador a su entorno personal |
| Zona 1 · Productividad personal (desarrollo ciudadano) | Cualquier creador; Agent Builder y agentes de SharePoint | Entornos de desarrollador administrados creados por enrutamiento | Solo conectores de Microsoft 365 y Power Platform; conocimiento del propio usuario | Sin compartir, o solo con personas y con tope de visores | Sin publicación para la organización |
| Zona 2 · Colaboración de equipo (creadores aprobados) | Creadores capacitados y aprobados | Sandbox y producción administrados dentro de un grupo de entornos con reglas | ACP con lista de permitidos de la zona, servidores MCP aprobados y credenciales del usuario final | Editor solo personas; Visor por grupos con tope; solo Teams y Microsoft 365 | ALM con soluciones, aprobación de TI antes de publicar y aprobación del administrador en Microsoft 365 |
| Zona 3 · Gestionada por la empresa (desarrollo profesional) | TI y desarrolladores profesionales | Desarrollo, prueba y producción separados, con grupos de Entra; CMK y VNet donde aplique | Lista de permitidos estricta y excepciones documentadas (canales externos, agentes autónomos) | Canales externos solo con autenticación y revisión; agentes públicos como excepción aprobada | Canalizaciones con despliegue delegado, revisión de seguridad y evaluaciones antes de cada versión |
| Entornos Trial | Ejercicios cortos | Vencen a los 30 días y borran sus agentes | Igual que la zona 1 | Sin compartir | No publican: exporta antes de que venzan |

Fuentes: [gobierno por zonas](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/sec-gov-phase2), [proteger el entorno predeterminado](https://learn.microsoft.com/en-us/power-platform/guidance/adoption/secure-default-environment), [reglas de grupos de entornos](https://learn.microsoft.com/en-us/power-platform/admin/environment-groups-rules), [ALM de Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/alm), [entornos](https://learn.microsoft.com/en-us/microsoft-copilot-studio/environments-first-run-experience) y [whitepaper v3.2](https://techcommunity.microsoft.com/blog/copilot-studio-blog/new-updates-administering-and-governing-agents-whitepaper-v3-2/4517044) (nombres de las zonas). Es un punto de partida: ajústalo a tu organización.

### Documentación, cursos y credenciales

- [Important changes (deprecations) coming in Power Platform](https://learn.microsoft.com/en-us/power-platform/important-changes-coming) · Documentación · Oficial · Nuevo · Microsoft Learn · 2 nov 2026. Registro oficial de retiradas de Power Platform, incluidas la de entornos de Dataverse for Teams y la de entornos de desarrollador no administrados y el Developer Plan.
- [Managed environments overview - Power Platform](https://learn.microsoft.com/en-us/power-platform/admin/managed-environment-overview) · Documentación · Oficial · Nuevo · Microsoft Learn · 16 oct 2026. Enumera las capacidades premium de Managed Environments: grupos de entornos, límites de uso compartido, usage insights, directivas de datos, canalizaciones, contenido de bienvenida, solution checker, IP firewall, IP cookie binding, CMK, Lockbox, copia extendida, VNet, enrutamiento y acceso condicional por app.
- [Rules for environment groups - Power Platform](https://learn.microsoft.com/en-us/power-platform/admin/environment-groups-rules) · Documentación · Oficial · Nuevo · Microsoft Learn · 15 oct 2026. Catálogo de las 28 reglas que se aplican en bloque a grupos de entornos administrados, entre ellas transcripciones de Copilot Studio, políticas avanzadas de conectores, ajustes de IA generativa, fuentes de conocimiento, modelos externos y en preview, uso compartido de agentes como editor/visor, skills, solution checker, retención de copias y usage insights.
- [Environment routing - Power Platform](https://learn.microsoft.com/en-us/power-platform/admin/default-environment-routing) · Documentación · Oficial · Microsoft Learn. Función premium que envía a cada maker de Copilot Studio, Power Apps o Power Automate a su propio entorno de desarrollador administrado (con reglas múltiples por grupo de seguridad y grupo de entornos) en lugar del entorno predeterminado.
- [Implement a zoned governance strategy - Microsoft Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/sec-gov-phase2) · Documentación · Oficial · Microsoft Learn (Copilot Studio guidance). Modelo de tres zonas (desarrollo ciudadano, asociado y profesional) con controles por inquilino, entorno y agente: directivas de datos, Bing, IA generativa, red aislada, orquestación, autenticación y seguridad del canal web.
- [Move data across regions for Copilots, AI agents, and generative AI features - Power Platform](https://learn.microsoft.com/en-us/power-platform/admin/geographical-availability-copilot) · Documentación · Oficial · Microsoft Learn. Tabla de regiones donde se procesan los datos de IA generativa y Bing por región del entorno, y procedimiento para consentir por entorno el movimiento de datos entre regiones, Bing, servicios de Microsoft 365 y flex routing.
- [Secure your Copilot Studio projects](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/sec-gov-phase3) · Documentación · Oficial · Microsoft Learn (Copilot Studio guidance). Recomendaciones: licencias y acceso por grupos de Entra, roles de seguridad de Dataverse para autoría y transcripciones, directivas de datos estrictas en desarrollo personal y más amplias en test/producción, secretos en Key Vault y despliegue con compuertas.
- [Secure the default environment - Power Platform](https://learn.microsoft.com/en-us/power-platform/guidance/adoption/secure-default-environment) · Documentación · Oficial · Microsoft Learn (Power Platform adoption guidance) · 14 may 2025. Recomendaciones para el entorno predeterminado al que acceden todos los empleados: roles de administrador con PIM, renombrarlo como entorno de productividad personal, contenido de bienvenida, Managed Environments, límites de uso compartido, directiva de datos e aislamiento entre inquilinos.
- [Power Apps Developer Plan Guide: Features and Benefits - Power Platform](https://learn.microsoft.com/en-us/power-platform/developer/plan) · Documentación · Oficial · Nuevo · Microsoft Learn · 26 oct 2026. Funciones y límites del Developer Plan (750 ejecuciones de flujo/mes, 2 GB de base de datos) y calendario de suspensión de los entornos de desarrollador no administrados.
- [Create a Developer Environment with the Power Apps Developer Plan - Power Platform](https://learn.microsoft.com/en-us/power-platform/developer/create-developer-environment) · Documentación · Oficial · Nuevo · Microsoft Learn · 16 oct 2026. Procedimiento para obtener un entorno de desarrollador y un inquilino de prueba, con el aviso de que los entornos de desarrollador no administrados quedan obsoletos.
- [Work with Power Platform environments - Microsoft Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/environments-first-run-experience) · Documentación · Oficial · Microsoft Learn. Cómo crear y elegir entornos para agentes, con la recomendación de usar un entorno de producción distinto del predeterminado y el aviso de que los entornos de prueba expiran a los 30 días y borran sus agentes.
- [Environment routing for Microsoft Copilot Managed Runtime - Power Platform](https://learn.microsoft.com/en-us/power-platform/admin/default-environment-routing-copilot-managed-runtime) · Documentación · Oficial · Vista previa · Microsoft Learn. Explica que el enrutamiento para Copilot Managed Runtime está activado en todos los inquilinos y no se puede desactivar, creando una regla «Everyone» y entornos de desarrollador personales administrados sin Dataverse. *Nota:* La creación de apps en Copilot Studio por esta vía se controla en el Microsoft 365 admin center (Apps > Set up app creation spaces); la regla «Everyone» no se puede eliminar y debe ir al final
- [Configure data movement across geographic locations for generative AI - Microsoft Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/manage-data-movement-outside-us) · Documentación · Oficial · Legado aún útil · Microsoft Learn · 19 nov 2024. Aviso de que usar IA generativa de Copilot Studio fuera de EE. UU. implica movimiento de datos entre regiones, que solo administradores globales o de Power Platform pueden habilitar y que no se revierte al retirar el consentimiento. *Nota:* Página de 2024; la configuración actual está en la tarjeta «Generative AI features» de cada entorno (ver geographical-availability-copilot)

### Comunidad: blogs, libros, newsletters y eventos

- [Power Apps Developer Plan environments are being switched off: what to do before 15 December](https://vantage365.com/power-apps-developer-plan-unmanaged-environments/) · Blog · Comunidad · Nuevo · Matt Weston · Vantage 365 · 25 oct 2026. Resume las tres fases de la retirada de los entornos de desarrollador no administrados (15-nov, 15-dic-2026 y 15-ene-2027) y un plan de auditoría con el filtro Tipo=Developer y Managed=No.

**Manos a la obra**

1. `Laboratorio parcial` Endurece el entorno predeterminado: renómbralo como entorno de productividad personal, publica contenido de bienvenida para creadores, verifica que compartir con «Everyone» sigue desactivado, aplícale una directiva de datos estricta y limita Power Platform Administrator con PIM ([proteger el entorno predeterminado](https://learn.microsoft.com/en-us/power-platform/guidance/adoption/secure-default-environment)). Limitación: activar Managed Environments en el entorno predeterminado exige licencias para sus usuarios activos. Evidencia: capturas de la configuración y registro del cambio.
2. `Laboratorio` Diseña tu estrategia de zonas con la tabla de este módulo: clasifica 10 casos de uso (un agente personal de Agent Builder, un agente de preguntas frecuentes de un equipo, un agente de RR. HH. con Dataverse, un agente web para clientes y un agente autónomo con desencadenador de eventos, entre otros) por zona, tipo de entorno, conectores, uso compartido, canales y aprobación ([gobierno por zonas](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/sec-gov-phase2)). Evidencia: matriz de zonas aprobada por el CoE.
3. `Laboratorio parcial` Grupo de entornos con reglas: crea un grupo con dos sandbox administrados y publica reglas de uso compartido de agentes (Editor solo personas y Visor con tope), transcripciones, fuentes de conocimiento, skills, IA generativa, solution checker y retención de copias; verifica la herencia en cada entorno ([reglas de grupos de entornos](https://learn.microsoft.com/en-us/power-platform/admin/environment-groups-rules)). Limitación: Managed Environments exige licencias premium o de prueba para los usuarios activos. Evidencia: reglas publicadas y bloqueadas en ambos entornos.
4. `Laboratorio parcial` Enrutamiento de entornos: actívalo para Copilot Studio solo para un grupo de seguridad piloto hacia el grupo de entornos con reglas estrictas y comprueba que un creador aterriza en su entorno de desarrollador administrado ([enrutamiento](https://learn.microsoft.com/en-us/power-platform/admin/default-environment-routing)). Revisa también la regla «Everyone» de Copilot Managed Runtime ([enrutamiento de Copilot Managed Runtime](https://learn.microsoft.com/en-us/power-platform/admin/default-environment-routing-copilot-managed-runtime)). Limitación: un entorno de desarrollador administrado por usuario y licencias premium para ejecutar recursos. Evidencia: entorno creado y regla aplicada.
5. `Laboratorio` Datos entre regiones y publicación con IA generativa: revisa la tarjeta «Generative AI features» de cada entorno del laboratorio y documenta la decisión sobre movimiento de datos, Bing, servicios de Microsoft 365 y flex routing ([movimiento de datos](https://learn.microsoft.com/en-us/power-platform/admin/geographical-availability-copilot)); define también cuándo habilitar el ajuste de tenant «Publish bots with AI features» ([guía de licencias de Copilot Studio](https://www.microsoft.com/licensing/guidance/microsoft-copilot-studio)). Evidencia: registro de decisiones revisado por privacidad.
6. `Solo producción` Entornos de desarrollador no administrados: filtra en el centro de administración de Power Platform los entornos de tipo Developer no administrados antes del 15 de diciembre de 2026 y decide convertir o exportar cada uno ([Developer Plan](https://learn.microsoft.com/en-us/power-platform/developer/plan)). Por qué en producción: solo allí existen los entornos y agentes de tus creadores. Cómo hacerlo seguro: inventario con un rol de solo lectura, exportación de soluciones antes de cualquier cambio y aviso a cada dueño. Evidencia: lista con decisión y fecha por entorno.
7. `Solo producción` Activación de Managed Environments en entornos existentes: inventaría las licencias de los usuarios activos antes de activarlo y empieza por entornos nuevos o de bajo uso ([licencias de Managed Environments](https://learn.microsoft.com/en-us/power-platform/admin/managed-environment-licensing)). Por qué en producción: el riesgo es bloquear a usuarios sin licencia premium. Cómo hacerlo seguro: piloto en un entorno, comunicación a los creadores y plan de licencias aprobado. Evidencia: plan de activación por entorno.

<a id="m7"></a>

## M7 · Copilot Studio: directivas de datos, autenticación y uso compartido

*L300 · ~7 h · Origen: Ruta de Learn «Evaluate, publish, and manage agents in Microsoft Copilot Studio» (gobierno y publicación) y documentación de directivas de datos, autenticación y uso compartido de Copilot Studio*

Las **directivas de datos** (la DLP de Power Platform) son obligatorias para todos los agentes de Copilot Studio desde principios de 2025 (MC973179), sin exenciones. Se aplican en tiempo real: las opciones bloqueadas aparecen deshabilitadas para el creador y el botón Publicar se desactiva ante una infracción. Copilot Studio tiene conectores propios que conviene clasificar uno por uno: «Chat without Microsoft Entra ID authentication in Copilot Studio», «Direct Line channels in Copilot Studio» (permitido por defecto), «Skills with Copilot Studio», los canales de Teams, SharePoint, Facebook o WhatsApp y el conector «Microsoft Copilot Studio», que habilita desencadenadores de eventos. El filtrado de endpoints limita HTTP y los sitios usados como conocimiento, y bloquear un conector también bloquea las herramientas MCP que lo usan.

Las **políticas avanzadas de conectores** (ACP) suman una lista de permitidos estricta: deniegan por defecto, bloquean los conectores nuevos, controlan acciones y desencadenadores y pueden bloquear servidores MCP completos, por entorno o por grupo de entornos. Todavía no cubren conectores personalizados ni HTTP, y los conectores virtuales de Copilot Studio siguen en las directivas clásicas. La autenticación es la otra mitad: «Authenticate with Microsoft» es el valor por defecto y es obligatorio para Teams y Microsoft 365; «No authentication» crea un agente público con el que cualquiera que tenga el enlace puede conversar; «Authenticate manually» admite Entra ID V2 con credenciales federadas o certificados. Pide solo los ámbitos imprescindibles.

El riesgo más subestimado son las **credenciales del creador**: si un conector usa las credenciales del maker, cada usuario del agente actúa con los permisos del autor. Dos controles de entorno lo resuelven: «Control maker credential options» fuerza las credenciales del usuario final (los agentes autónomos o programados fallarán) y «Sharing agents with embedded maker credentials» en «Safe sharing enforced» impide compartir agentes con conexiones no compartibles. Completan el cuadro los **límites de uso compartido** (Editor solo a personas y Visor con tope, aplicados en hasta una hora y sin retirar accesos previos) y la publicación en Teams y Microsoft Copilot con aprobación del administrador, que exige reenviar cada cambio.

**Por qué importa**

La mayoría de los incidentes con agentes de Copilot Studio nace de tres decisiones del creador: publicar sin autenticación, usar sus propias credenciales en los conectores y compartir con toda la organización. Las directivas de datos, las opciones de credenciales y los límites de uso compartido convierten esas decisiones en reglas del entorno, aplicadas en tiempo real y auditables, en lugar de depender de cada creador.

**Qué vas a lograr**

- Diseñar directivas de datos para los conectores propios de Copilot Studio, con filtrado de endpoints.
- Combinar las directivas clásicas con las políticas avanzadas de conectores (ACP) conociendo sus huecos.
- Elegir el método de autenticación del agente y forzar credenciales del usuario final cuando corresponda.
- Configurar límites de uso compartido y el flujo de aprobación para publicar en Teams y Microsoft Copilot.
- Tratar los agentes públicos como excepciones documentadas y auditadas.

> **Qué cambió.** La aplicación de directivas de datos a Copilot Studio es obligatoria en todos los tenants desde principios de 2025 (MC973179), ya no admite exenciones y se aplica en tiempo real: ante una infracción, Publicar se deshabilita y el creador puede descargar el detalle ([directivas de datos para agentes](https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-data-loss-prevention)). Con `Set-PowerAppDlpErrorSettings` agregas un correo de contacto y un enlace a tu guía interna en el mensaje de error.

> **Atención.** Estado de las políticas avanzadas de conectores: la versión en inglés no dice «preview», admite configuración por entorno y los modos mixto o solo ACP, mientras copias regionales siguen en preview, solo por grupo de entornos y con Managed Environments obligatorio; la regla «Advanced connector policies only» figura en preview ([ACP](https://learn.microsoft.com/en-us/power-platform/admin/advanced-connector-policies), [reglas](https://learn.microsoft.com/en-us/power-platform/admin/environment-groups-rules)). ACP aún no cubre conectores personalizados ni HTTP, y los conectores virtuales de Copilot Studio siguen en las directivas clásicas.

> **Atención.** Hay dos mecanismos para bloquear canales: los conectores de canal de la directiva de datos (Direct Line está permitido por defecto) y el control en preview «Agent access channels», donde la política del grupo prevalece y bloquear un canal ya publicado provoca fallos en tiempo de ejecución ([canales y agentes conectados](https://learn.microsoft.com/en-us/power-platform/admin/security/configure-channel-connected-agent-publishing)). Define cuál es tu fuente de verdad. Y ojo con «Skills»: el conector «Skills with Copilot Studio» gobierna las skills de Azure Bot Service, no las skills agénticas, que se controlan con la regla «Skills in Copilot Studio».

> **Consejo Ninja.** Antes de publicar, Copilot Studio ejecuta un análisis de seguridad que advierte, sin bloquear, si el agente usa «No authentication», si conectores o flujos usan credenciales del creador o si se comparte con toda la organización ([análisis de seguridad](https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-scan)). Trata cada advertencia como criterio de rechazo en tu revisión; la seguridad avanzada de conocimiento, herramientas y MCP se profundiza en [A6](03_Nivel_3_Avanzado.md#a6).

**¿Tienes poco tiempo?**

- [Configure data policies for agents - Microsoft Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-data-loss-prevention) · Documentación
- [Configure user authentication in Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/configuration-end-user-authentication) · Documentación
- [Control maker-provided credentials for authentication - Microsoft Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/configure-no-maker-authentication) · Documentación
- [Control how agents are shared - Microsoft Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-sharing-controls-limits) · Documentación

**Conectores de Copilot Studio en las directivas de datos**

| Conector (nombre en el centro de administración) | Qué habilita | Clasificación recomendada |
|---|---|---|
| Chat without Microsoft Entra ID authentication in Copilot Studio | Publicar agentes sin autenticación: cualquiera con el enlace puede conversar | Bloqueado en todos los entornos salvo uno aprobado para agentes públicos, para evitar la exposición anónima de conocimiento y herramientas |
| Direct Line channels in Copilot Studio | Sitio de demostración, webs personalizadas, apps móviles y otros canales Direct Line (permitido por defecto) | Bloqueado en las zonas 1 y 2; Business solo en entornos aprobados, con acceso seguro y rotación de secretos |
| Microsoft Teams + Microsoft 365 Channel in Copilot Studio | Publicar en Teams y Microsoft Copilot | Business: canal interno recomendado, con «Authenticate with Microsoft» y aprobación del administrador |
| SharePoint channel in Copilot Studio | Publicar en SharePoint | Business si hay caso de uso; si no, bloqueado para reducir la superficie |
| Facebook channel in Copilot Studio y WhatsApp channel in Copilot Studio | Canales de consumidor externos | Bloqueados salvo en entornos de atención al cliente aprobados, porque los datos salen del perímetro corporativo |
| Omnichannel in Copilot Studio | Canal de Dynamics 365 Customer Service | Business solo en entornos de centro de contacto; bloqueado en el resto |
| HTTP | Nodo de solicitud HTTP en los temas | Bloqueado, o Business con filtrado de endpoints (lista de permitidos); ACP todavía no lo cubre |
| Skills with Copilot Studio | Skills de Azure Bot Service (código externo) | Bloqueado salvo en la zona 3 con revisión de código |
| Application Insights in Copilot Studio | Enviar la telemetría del agente a Application Insights | Business en las zonas 2 y 3, apuntando solo a recursos corporativos |
| Microsoft Copilot Studio | Desencadenadores de eventos (agentes autónomos) y evaluaciones automatizadas autenticadas | Bloqueado en la zona 1, porque los desencadenadores usan credenciales del creador; Business en entornos aprobados |
| Conectores de Power Platform usados como herramientas | Acciones del agente contra sistemas de negocio | Clasificar uno por uno; los personalizados siguen en la directiva clásica y bloquearlos también bloquea las herramientas MCP basadas en conectores |
| Servidores MCP | Herramientas expuestas por servidores MCP | Lista de permitidos con ACP (bloqueo por servidor); solo servidores con OAuth o Entra y descripciones de herramientas revisadas |
| Fuentes de conocimiento (SharePoint y sitios públicos) | Conocimiento para respuestas generativas | Permitidas con filtrado de endpoints; sin sitios públicos en agentes internos sensibles |

Fuentes: [directivas de datos para agentes](https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-data-loss-prevention) (22 de octubre de 2026), [políticas avanzadas de conectores](https://learn.microsoft.com/en-us/power-platform/admin/advanced-connector-policies), [servidores MCP en Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/mcp-add-existing-server-to-agent) y [gobierno por zonas](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/sec-gov-phase2). Las clasificaciones son una recomendación de este programa; el resto de los controles está en la tabla [Controles de Copilot Studio y Power Platform](00_Programa.md#controles-copilot-studio).

### Documentación, cursos y credenciales

- [Configure data policies for agents - Microsoft Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-data-loss-prevention) · Documentación · Oficial · Nuevo · Microsoft Learn · 22 oct 2026. Guía de referencia para clasificar o bloquear en las directivas de datos del Power Platform admin center los conectores propios de Copilot Studio (chat sin autenticación, HTTP, skills, canales, desencadenadores, Application Insights) y verificar su aplicación en tiempo real.
- [Configure user authentication in Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/configuration-end-user-authentication) · Documentación · Oficial · Nuevo · Microsoft Learn · 21 oct 2026. Opciones de autenticación de agentes (sin autenticación, Authenticate with Microsoft y manual con Entra ID V2 con credenciales federadas, certificados o secretos, o OAuth 2 genérico) y su efecto en quién puede chatear y en el uso compartido.
- [Advanced connector policies - Power Platform](https://learn.microsoft.com/en-us/power-platform/admin/advanced-connector-policies) · Documentación · Oficial · Microsoft Learn. Nueva generación de directivas de conectores con lista de permitidos estricta (denegar por defecto), visibilidad por acción, bloqueo de servidores MCP completos, aplicación en tiempo de diseño y modos mixto o solo ACP por entorno o grupo de entornos.
- [Control maker-provided credentials for authentication - Microsoft Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/configure-no-maker-authentication) · Documentación · Oficial · Microsoft Learn. Control de entorno o grupo de entornos («Control maker credential options») para impedir que las herramientas de los agentes usen credenciales del maker y forzar credenciales del usuario final.
- [Configure sharing agents with embedded maker credentials - Microsoft Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/configure-sharing-agents-embedded-maker-credentials) · Documentación · Oficial · Microsoft Learn. Control por entorno con dos modos (All sharing allowed / Safe sharing enforced) que avisa o impide compartir o publicar agentes cuyas conexiones usan credenciales del maker no compartibles.
- [Control how agents are shared - Microsoft Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-sharing-controls-limits) · Documentación · Oficial · Microsoft Learn. Límites de uso compartido de agentes como control de Managed Environments (entorno o grupo): permitir editores, permitir visores y grupos de seguridad, solo individuos y número máximo de visores.
- [Key concepts - Copilot Studio security and governance](https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance) · Documentación · Oficial · Microsoft Learn. Inventario de controles de seguridad de Copilot Studio: directivas de datos (autenticación de makers y usuarios, conectores, HTTP, canales, desencadenadores), análisis automático de seguridad, auditoría en Purview y Sentinel, e integración con Agent 365.
- [Share agents with other users and makers (GitHub Copilot) - Microsoft Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/authoring-share-agent) · Documentación · Oficial · Microsoft Learn. Uso compartido en el nuevo arnés: solo derechos de visualización a personas, grupos de seguridad o toda la organización (End user access), con requisito de Authenticate with Microsoft y publicación en Teams + Microsoft 365.
- [Configure channel publishing and connected agent access (preview) - Power Platform](https://learn.microsoft.com/en-us/power-platform/admin/security/configure-channel-connected-agent-publishing) · Documentación · Oficial · Vista previa · Nuevo · Microsoft Learn · 16 jun 2026. Controles en Security > Identity and access > Agent access channels para limitar por grupo de entornos o entorno los canales de publicación, y ajuste para permitir o impedir agentes conectados entre entornos. *Nota:* Las políticas a nivel de grupo de entornos prevalecen; si se bloquea un canal ya publicado, las llamadas fallan en tiempo de ejecución
- [Controlar cómo se comparten los agentes (es-es)](https://learn.microsoft.com/es-es/microsoft-copilot-studio/admin-sharing-controls-limits) · Documentación · Oficial · ES · Microsoft Learn. Versión en español de los límites de uso compartido de agentes con roles Editor y Visor en Managed Environments.

**Manos a la obra**

1. `Laboratorio` Directiva de datos para Copilot Studio: en un entorno sandbox bloquea «Chat without Microsoft Entra ID authentication in Copilot Studio», «Direct Line channels in Copilot Studio» y «Skills with Copilot Studio», y configura el filtrado de endpoints de HTTP con un solo dominio permitido ([directivas de datos para agentes](https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-data-loss-prevention)). Verifica el banner de error en un agente de prueba, Publicar deshabilitado, el archivo de detalles y el evento de cambio de la directiva en la auditoría de Purview ([actividad de administración de Power Platform](https://learn.microsoft.com/en-us/power-platform/admin/activity-logging-auditing/activity-logs-power-platform-admin)). Evidencia: capturas y registro de auditoría.
2. `Laboratorio` Credenciales del creador: en un entorno fija «Control maker credential options» en solo credenciales del usuario final y «Sharing agents with embedded maker credentials» en «Safe sharing enforced»; comprueba que un agente con desencadenador autónomo falla y que no puedes compartir un agente con una conexión del creador ([credenciales del creador](https://learn.microsoft.com/en-us/microsoft-copilot-studio/configure-no-maker-authentication), [uso compartido seguro](https://learn.microsoft.com/en-us/microsoft-copilot-studio/configure-sharing-agents-embedded-maker-credentials)). Revierte al terminar. Evidencia: errores capturados y configuración final documentada.
3. `Laboratorio parcial` Análisis de seguridad y autenticación: en el sandbox con pago por uso crea un agente, cámbialo a «No authentication», agrega una herramienta con credenciales del creador y compártelo con toda la organización; intenta publicar y captura las tres advertencias ([análisis de seguridad](https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-scan)). Luego vuelve a «Authenticate with Microsoft» con credenciales del usuario final ([autenticación](https://learn.microsoft.com/en-us/microsoft-copilot-studio/configuration-end-user-authentication)). Limitación: la prueba de Copilot Studio no publica; necesitas pago por uso o capacidad. Evidencia: advertencias capturadas y agente corregido.
4. `Laboratorio parcial` Límites de uso compartido: en un entorno administrado configura Editor solo para personas, sin grupos de seguridad para Visor y un máximo de cinco visores; verifica después de una hora que se aplican y que los accesos ya concedidos no se retiraron ([límites de uso compartido](https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-sharing-controls-limits)). Limitación: requiere Managed Environments con licencias. Evidencia: intento de compartir rechazado y lista de accesos previos.
5. `Laboratorio parcial` Políticas avanzadas de conectores: en el grupo de entornos crea una lista de permitidos para la zona 2 en modo mixto, bloquea un servidor MCP no aprobado y comprueba que el creador no puede agregarlo ([ACP](https://learn.microsoft.com/en-us/power-platform/admin/advanced-connector-policies)). Limitación: requiere Managed Environments, algunos modos están en preview y HTTP y los conectores personalizados siguen en la directiva clásica. Evidencia: regla publicada e intento bloqueado.
6. `Laboratorio parcial` Canales: configura en preview «Agent access channels» para permitir solo Teams y Microsoft 365 en el grupo de entornos y compáralo con los conectores de canal de tu directiva de datos ([canales y agentes conectados](https://learn.microsoft.com/en-us/power-platform/admin/security/configure-channel-connected-agent-publishing)). Limitación: función en preview; bloquear un canal ya publicado rompe el agente en ejecución. Evidencia: decisión escrita sobre la fuente de verdad.
7. `Solo producción` Aprobación de agentes de la organización en Microsoft Copilot: envía un agente a aprobación, revísalo (capacidades, conectores, autenticación y conocimiento) y publícalo solo para un grupo piloto; prueba luego el bloqueo y la retirada ([publicar en Teams y Microsoft Copilot](https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-add-bot-to-microsoft-teams), [asignar y desplegar agentes](https://learn.microsoft.com/en-us/microsoft-365/copilot/agent-essentials/agent-lifecycle/agent-assign-deploy)). Por qué en producción: requiere usuarios con licencia de Copilot y el catálogo real. Cómo hacerlo seguro: audiencia limitada, cuentas de prueba y reversión bloqueando el agente. Evidencia: solicitud revisada y aprobada con su lista de verificación.

<a id="m8"></a>

## M8 · Shadow AI y aplicaciones de IA de terceros

*L300 · ~6 h · Origen: Modelo de despliegue de Purview «Prevent data leak to shadow AI» (pasos 1 y 2) y laboratorio de IA del Zero Trust Workshop*

La IA en la sombra (shadow AI) es la IA que tu organización no aprobó: apps de consumo, extensiones de navegador o el Copilot de consumo con cuentas personales, donde los usuarios pegan contratos, código o datos de clientes. Prohibirla sin ofrecer alternativa no funciona. El enfoque de Microsoft combina una **alternativa sancionada** (Copilot Chat con protección de datos empresariales), **descubrimiento**, **bloqueo** de las apps no autorizadas y **DLP en línea** para lo que sigue permitido. El modelo de despliegue de Purview «Prevent data leak to shadow AI» lo ordena en dos pasos: descubrir las apps de IA en uso y bloquear el acceso a las no autorizadas.

Para descubrir, **Defender for Cloud Apps** evalúa más de 33.000 apps con más de 90 factores de riesgo y da visibilidad sobre más de 1.000 apps de IA generativa: en el portal de Defender filtras el catálogo por la categoría «Generative AI», revisas la puntuación de riesgo, creas una política que alerte por apps nuevas y desautorizas las que no apruebes, con bloqueo en los dispositivos incorporados a Defender for Endpoint. Viene en Microsoft 365 E5 y en Microsoft Defender Suite. Para proteger datos, **Edge for Business** aplica DLP en línea de Purview a prompts y archivos hacia IA no autorizada, incluso en dispositivos no administrados si el usuario inició sesión con Entra, y Endpoint DLP con la extensión del navegador cubre otros navegadores.

Atención a las licencias: proteger en Edge el flujo de un dispositivo administrado hacia una app no administrada es pago por uso, gestionar interacciones con IA de terceros en Purview también lo es, y la DLP de red con Global Secure Access exige E7 o Purview E5 más Entra Internet Access, que no viene en E5. Y atención al límite de Agent 365: desde el 1 de julio de 2026 la seguridad de agentes de Copilot Studio y Foundry en Defender exige esa licencia, igual que el bloqueo avanzado de agentes locales. Dentro del alcance quedan Defender for Cloud Apps, app governance para apps OAuth y la DLP de Purview. Se profundiza en el programa de Purview DSPM y seguridad de datos para IA, módulo M3.

**Por qué importa**

Bloquear la IA sin ofrecer alternativa empuja a los usuarios a evadir controles; permitirla sin visibilidad expone datos en servicios que la organización no controla. Descubrir qué apps se usan, sancionar Copilot Chat con protección de datos empresariales y bloquear o limitar el resto con DLP en el navegador y en la red reduce la fuga hacia la IA de consumo con métricas verificables.

**Qué vas a lograr**

- Descubrir y puntuar las apps de IA generativa en uso con Defender for Cloud Apps.
- Sancionar, desautorizar y bloquear apps de IA en dispositivos incorporados a Defender for Endpoint.
- Aplicar DLP en Edge for Business y en los endpoints a prompts y archivos hacia IA no autorizada, sabiendo qué se cobra por uso.
- Evaluar Global Secure Access (descubrimiento, filtrado de contenido, Prompt Injection Protection y DLP de red) y su licencia.
- Distinguir lo que requiere Agent 365 (agentes locales y seguridad de agentes en Defender) de las alternativas dentro del alcance.

> **Novedad.** En RSAC 2026 (23 de marzo), Microsoft anunció DLP en línea de Purview en Edge for Business para auditar o bloquear prompts y archivos hacia herramientas de IA no autorizadas, con redirección a Microsoft 365 Copilot, en dispositivos administrados y no administrados si el usuario inició sesión en Edge con Entra ([anuncio de Edge](https://blogs.windows.com/msedgedev/2026/03/23/protect-your-enterprise-from-shadow-ai-and-more-announcements-at-rsac-2026/)). En el mismo evento se anunció el inventario de Intune con las apps habilitadas para IA ([RSAC 2026](https://www.microsoft.com/en-us/security/blog/2026/03/20/secure-agentic-ai-end-to-end/)).

> **Atención.** Licencias: proteger en Edge el flujo de un dispositivo administrado hacia una app no administrada es pago por uso, mientras los escenarios con apps registradas en Entra entran en E5 ([descripción del servicio de Purview](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)). Gestionar interacciones con IA de terceros en Purview requiere pago por uso y, salvo red y Edge, la extensión del navegador ([otras apps de IA](https://learn.microsoft.com/en-us/purview/ai-other-apps)). La DLP de red con Global Secure Access exige E7 o Purview E5 más Entra Internet Access; con un SASE de terceros, Purview E5 y pago por uso ([Network Data Security](https://learn.microsoft.com/en-us/purview/dlp-network-data-security-learn)).

> **Atención.** Límite de Agent 365: desde el 1 de julio de 2026, la postura, la detección de amenazas y la protección en tiempo real de agentes de Copilot Studio y Foundry en Defender exigen Agent 365, aunque la misma [página de transición](https://learn.microsoft.com/en-us/defender-xdr/security-for-ai/transition-agent-security-to-agent-365) dice que la protección en tiempo real vía Defender for Cloud Apps «sigue sin cambios» para quien ya la usaba. En un AMA del 12 de mayo de 2026, Microsoft indicó que ver agentes en la sombra requiere E3, que el descubrimiento y los controles básicos requieren E5 y que el bloqueo avanzado de agentes locales requiere Agent 365 ([AMA de Agent 365](https://techcommunity.microsoft.com/event/microsoft365-events/live-ama-microsoft-agent-365/4511700)). Trata la seguridad de agentes en Defender como fuera de alcance.

> **Consejo Ninja.** La fecha de GA del descubrimiento de shadow AI en Entra Internet Access difiere entre fuentes: RSAC 2026 la ubica el 31 de marzo y el blog de Entra del 1 de mayo de 2026 la presenta como recién disponible ([blog de Entra](https://techcommunity.microsoft.com/blog/microsoft-entra-blog/lock-down-ai-web-and-private-apps-what%E2%80%99s-new-in-internet-access-and-private-acce/3847825)). Sea cual sea la fecha, Entra Internet Access no viene en E5. Para las apps OAuth con permisos excesivos, app governance de Defender for Cloud Apps sigue dentro del alcance ([app governance](https://learn.microsoft.com/en-us/defender-cloud-apps/app-governance-manage-app-governance)).

**¿Tienes poco tiempo?**

- [Manage generative AI apps for your organization](https://learn.microsoft.com/en-us/copilot/manage/manage-generative-ai-apps) · Documentación
- [Step 1: Discover AI apps - Prevent data leak to shadow AI](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-data-leak-shadow-ai-step1) · Documentación
- [Step 2: Block access to unsanctioned AI apps - Prevent data leak to shadow AI](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-data-leak-shadow-ai-step2) · Documentación
- [Protect your enterprise from shadow AI and more: Announcements at RSAC 2026](https://blogs.windows.com/msedgedev/2026/03/23/protect-your-enterprise-from-shadow-ai-and-more-announcements-at-rsac-2026/) · Blog oficial

### Documentación, cursos y credenciales

- [Learn about Data Loss Prevention for Cloud Apps in Edge for Business](https://learn.microsoft.com/en-us/purview/dlp-browser-dlp-learn) · Documentación · Oficial · Nuevo · Microsoft Learn · 15 sep 2026. DLP integrado en Edge for Business sin incorporar el dispositivo: protege apps gestionadas (SSO Entra) en dispositivos gestionados y no gestionados, y apps no gestionadas/IA (ChatGPT, Gemini, DeepSeek, Copilot consumer, etc.) desde dispositivos Intune.
- [Manage generative AI apps for your organization](https://learn.microsoft.com/en-us/copilot/manage/manage-generative-ai-apps) · Documentación · Oficial · Microsoft Learn. Explica cómo combinar DSPM para IA, Defender for Cloud Apps (catálogo Generative AI, políticas y bloqueo) y Defender CSPM para gobernar apps de IA de Microsoft y de terceros.
- [Step 1: Discover AI apps - Prevent data leak to shadow AI](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-data-leak-shadow-ai-step1) · Documentación · Oficial · Microsoft Learn · 3 abr 2026. Primer paso del modelo contra la IA en la sombra: descubrir apps con Defender for Cloud Apps, interacciones con DSPM e IRM antes de bloquear.
- [Step 2: Block access to unsanctioned AI apps - Prevent data leak to shadow AI](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-data-leak-shadow-ai-step2) · Documentación · Oficial · Microsoft Learn · 3 abr 2026. Bloquea apps de IA no autorizadas con Defender for Cloud Apps, Entra Internet Access, Protección adaptable con acceso condicional e Intune.
- [Learn about Microsoft Purview Network Data Security](https://learn.microsoft.com/en-us/purview/dlp-network-data-security-learn) · Documentación · Oficial · Nuevo · Microsoft Learn · 16 sep 2026. Seguridad de datos de red: integra Purview con Entra Global Secure Access y con SASE/navegadores seguros de terceros (Security Store) para descubrir, alertar y bloquear contenido sensible enviado a apps no gestionadas e IA.
- [Use Microsoft Purview to manage data security & compliance for other AI apps](https://learn.microsoft.com/en-us/purview/ai-other-apps) · Documentación · Oficial · Nuevo · Microsoft Learn · 1 may 2026. Tabla de capacidades de Purview para sitios de IA de terceros (ChatGPT, Gemini, DeepSeek) vía navegador, endpoint y red; requiere pay-as-you-go y no admite etiquetas de sensibilidad.
- [Microsoft Defender for Cloud Apps (página de producto)](https://www.microsoft.com/en-us/security/business/siem-and-xdr/microsoft-defender-cloud-apps) · Documentación · Oficial. Presenta Defender for Cloud Apps con visibilidad sobre más de 1.000 apps de IA generativa, un catálogo de más de 33.000 apps evaluadas con más de 90 factores de riesgo y el precio de Defender Suite.

### Anuncios y blogs oficiales

- [Protect your enterprise from shadow AI and more: Announcements at RSAC 2026](https://blogs.windows.com/msedgedev/2026/03/23/protect-your-enterprise-from-shadow-ai-and-more-announcements-at-rsac-2026/) · Blog oficial · Empleado de Microsoft · Arunesh Chandra · Microsoft Edge Blog · 23 mar 2026. Anuncia la ampliación de la protección en línea de Purview en Edge for Business para auditar o bloquear prompts y cargas de archivos a herramientas de IA no autorizadas, incluso en dispositivos no administrados, con redirección a Microsoft 365 Copilot.
- [Secure agentic AI end-to-end (RSAC 2026)](https://www.microsoft.com/en-us/security/blog/2026/03/20/secure-agentic-ai-end-to-end/) · Blog oficial · Empleado de Microsoft · Vasu Jakkal · Microsoft Security Blog · 20 mar 2026. Anuncios de Microsoft para RSAC 2026: asegurar agentes, cimientos y defender con agentes y expertos; confirma que E7 incluye Agent 365, Microsoft 365 Copilot, Entra Suite y E5.
- [New in Edge for Business: AI for work, safe from day one](https://blogs.windows.com/msedgedev/2026/05/20/new-in-edge-for-business-ai-for-work-safe-from-day-one/) · Blog oficial · Empleado de Microsoft · Vista previa · Nuevo · Lindsay Kubasik · Microsoft Edge Blog · 20 may 2026. Presenta la navegación agéntica con Copilot en Edge for Business (preview limitada) con controles de TI por directiva, sitios permitidos y aplicación de DLP de Purview mientras Copilot navega. *Nota:* La navegación agéntica requiere licencia de Microsoft 365 Copilot y no está disponible en el Espacio Económico Europeo; tratarla como nueva superficie de riesgo en el modelo de amenazas

### Webinars, videos y podcasts

- [New Security Controls in Edge for Business (Microsoft Mechanics)](https://techcommunity.microsoft.com/blog/microsoftmechanicsblog/new-security-controls-in-edge-for-business/4531027) · Video · Empleado de Microsoft · Nuevo · Jeremy Chapman · Microsoft Mechanics · 26 jun 2026. Demostración de controles de Edge for Business: bloqueo de datos sensibles hacia IA no autorizada, perfiles de trabajo con directivas de protección de aplicaciones de Intune en dispositivos no administrados, controles de portapapeles y gestión de extensiones.

### Laboratorios, GitHub y herramientas

- [Block Access to Unsanctioned AI Apps with Defender for Cloud Apps (Zero Trust Workshop – AI)](https://microsoft.github.io/zerotrustassessment/docs/workshop-guidance/AI/AI_099) · Laboratorio · Oficial · Microsoft Zero Trust Workshop (GitHub Pages). Tarea del taller Zero Trust que explica cómo pasar del descubrimiento de IA en la sombra al bloqueo por app en Defender for Cloud Apps, complementando el filtrado por categoría de Global Secure Access.

### Comunidad: blogs, libros, newsletters y eventos

- [How to Govern Shadow AI with Microsoft Purview, Defender and DSPM](https://nikkichapple.com/govern-shadow-ai-microsoft-purview-defender-dspm/) · Blog · Comunidad · Nuevo · Nikki Chapple · nikkichapple.com · 31 may 2026. Simplifica el modelo oficial Prevent data leak to shadow AI en dos capas (controlar apps y controlar datos) con pasos de descubrimiento, evaluación, bloqueo, DLP y auditoría.

**Manos a la obra**

1. `Laboratorio` Shadow AI con Defender for Cloud Apps y Defender for Endpoint: filtra el catálogo por la categoría «Generative AI», crea una política que alerte por apps de IA generativa nuevas, marca una app como no autorizada y comprueba el bloqueo en la VM Windows 11 incorporada a Defender for Endpoint con la protección de red en modo bloqueo ([apps de IA generativa](https://learn.microsoft.com/en-us/copilot/manage/manage-generative-ai-apps), [bloquear apps no autorizadas](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-data-leak-shadow-ai-step2)). El bloqueo tarda hasta 3 horas. Evidencia: navegación bloqueada y evento en el portal.
2. `Laboratorio parcial` Informe de descubrimiento: revisa en Cloud Discovery las apps de IA generativa con más usuarios y tráfico, su puntuación de riesgo y su categoría, y propone una lista de sancionar, supervisar o bloquear ([descubrir apps de IA](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-data-leak-shadow-ai-step1)). Limitación: en el laboratorio el tráfico es mínimo. Cómo hacerlo en producción: rol de solo lectura y datos agregados. Evidencia: lista de decisiones con dueño de negocio.
3. `Laboratorio parcial` DLP en Edge for Business: crea una política que primero audite y luego bloquee prompts con un SIT sintético hacia una app de IA no autorizada, con redirección a Copilot ([DLP en Edge for Business](https://learn.microsoft.com/en-us/purview/dlp-browser-dlp-learn)). Limitación: el flujo de dispositivo administrado a app no administrada se cobra por uso; configura un presupuesto de Azure y limita la prueba a una cuenta. Evidencia: bloqueo en el navegador y evento en el explorador de actividad.
4. `Laboratorio parcial` Endpoint DLP y extensión del navegador: activa la política de un clic «Detect sensitive info added to AI sites» (solo auditoría), instala la extensión de Purview en la VM incorporada y pega datos sintéticos en un sitio de IA de terceros ([otras apps de IA](https://learn.microsoft.com/en-us/purview/ai-other-apps)). Limitación: la auditoría de apps de IA de terceros es de pago por uso. Evidencia: eventos «AI website visit» y de DLP en el explorador de actividad.
5. `Laboratorio parcial` Global Secure Access: con una prueba de Entra Internet Access habilita el descubrimiento de shadow AI y el filtrado de contenido para bloquear subidas de archivos a una app de IA no autorizada, solo para un grupo piloto ([novedades de Internet Access](https://techcommunity.microsoft.com/blog/microsoft-entra-blog/lock-down-ai-web-and-private-apps-what%E2%80%99s-new-in-internet-access-and-private-acce/3847825)). Limitación: requiere esa licencia de prueba y el cliente de Global Secure Access en una VM unida a Entra. Evidencia: subida bloqueada y registro de tráfico.
6. `Laboratorio` Alternativa sancionada: redacta la guía de uso aceptable que nombra Copilot Chat con protección de datos empresariales como herramienta aprobada, explica cómo pedir una app de IA nueva y enlaza esa guía desde la página de bloqueo o de redirección ([modelo de despliegue contra shadow AI](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-data-leak-shadow-ai-step2)). Evidencia: guía publicada y prueba de la redirección.
7. `Solo producción` Ciclo mensual de gobierno de shadow AI: revisa el descubrimiento, decide con los dueños de negocio qué sancionar o bloquear, comunica la alternativa y bloquea primero en el anillo 1 ([apps de IA generativa](https://learn.microsoft.com/en-us/copilot/manage/manage-generative-ai-apps)). Por qué en producción: el uso real de IA solo se ve con usuarios reales. Cómo hacerlo seguro: datos agregados, aviso previo, excepciones con fecha de vencimiento y casos de Insider Risk solo con RR. HH. y Legal involucrados (no es asesoría legal). Evidencia: informe mensual con la tendencia de apps y bloqueos.

**¿Quieres profundizar?**

- [New Security Controls in Edge for Business (Microsoft Mechanics)](https://techcommunity.microsoft.com/blog/microsoftmechanicsblog/new-security-controls-in-edge-for-business/4531027) · Video
- [How to Govern Shadow AI with Microsoft Purview, Defender and DSPM](https://nikkichapple.com/govern-shadow-ai-microsoft-purview-defender-dspm/) · Blog
- [Block Access to Unsanctioned AI Apps with Defender for Cloud Apps (Zero Trust Workshop – AI)](https://microsoft.github.io/zerotrustassessment/docs/workshop-guidance/AI/AI_099) · Laboratorio

<a id="reto-intermedio"></a>

## Reto del nivel

**Copilot y agentes con barreras, en piloto.** Para un grupo piloto configura y documenta: RCD y RAC sobre dos sitios PRUEBA- con prueba de reversión; la DLP para Copilot en simulación (prompts, búsqueda web y exclusión de contenido etiquetado) y la revisión de la política predeterminada; etiquetas de contenedor y etiquetado automático en simulación; la carga de paquetes avanzados restringida y la aprobación de un agente con audiencia limitada; en Copilot Studio, la matriz de zonas, un grupo de entornos con reglas, una directiva de datos que bloquee el chat sin autenticación y Direct Line, y los controles de credenciales del creador; y en shadow AI, la política de apps de IA generativa con una app bloqueada. Entrega una matriz de evidencias (control, licencia requerida, modo, evidencia, responsable y reversión) y un resumen de riesgos de una página para el comité de IA.

<a id="quiz-intermedio"></a>

## Evaluación del nivel

Responde y compara con [Evaluaciones y respuestas](06_Evaluaciones_y_respuestas.md#eval-intermedio). Con 80 % o más, ¡nivel aprobado! (En la versión web puedes corregir en línea y generar tu certificado).

1. ¿Cuál de estas afirmaciones sobre Restricted Content Discovery (RCD) es correcta?
   - a) Cambia los permisos del sitio para quitar a EEEU
   - b) Aplica también a las OneDrive de los usuarios
   - c) Oculta el sitio de la búsqueda organizacional y de Copilot y quita sus puntos de entrada de IA, sin cambiar permisos
   - d) Saca el contenido del índice y desactiva eDiscovery

2. ¿Qué vista de DSPM no está disponible sin Microsoft 365 E7 o Agent 365?
   - a) AI observability
   - b) La pestaña AI activities del explorador de actividad
   - c) Las evaluaciones de riesgo de datos
   - d) Reports

3. ¿En qué modo se crea la política de un clic «DSPM for AI: Detect sensitive info added to AI sites»?
   - a) Bloqueo
   - b) Prueba con anulación
   - c) Deshabilitada
   - d) Solo auditoría, para todos los usuarios

4. ¿Qué derechos de uso necesita un usuario para que Copilot use contenido cifrado?
   - a) EDIT y PRINT
   - b) OWNER
   - c) VIEW y EXTRACT
   - d) FORWARD y REPLY

5. ¿Qué contenido no devuelve Copilot?
   - a) Correos protegidos con S/MIME
   - b) Archivos cifrados con Customer Key
   - c) Archivos etiquetados sin cifrado
   - d) Archivos cifrados con BYOK

6. ¿Cómo arranca la política «Default DLP policy - Protect sensitive M365 Copilot interactions»?
   - a) Forzada, con sugerencias al usuario
   - b) Desactivada
   - c) Solo para administradores
   - d) En simulación, con una alerta y un correo de baja severidad

7. Un usuario sube a Copilot un PDF con números de tarjeta y escribe un prompt sin datos sensibles. ¿Qué evalúa la DLP de la ubicación de Copilot?
   - a) El contenido del PDF
   - b) Solo el texto escrito en el prompt
   - c) Ambos
   - d) Ninguno

8. ¿Qué controla el ajuste «Advanced package uploads» del centro de administración?
   - a) Quién puede subir agentes declarativos con acciones o servidores MCP
   - b) El tamaño máximo de los archivos en Copilot
   - c) La publicación en la tienda de socios
   - d) La subida de documentos a Notebooks

9. Bloqueas en el centro de administración un plugin que usa un conector de Copilot y un servidor MCP remoto. ¿Qué ocurre?
   - a) Se revoca automáticamente el consentimiento de la app en Entra
   - b) Los usuarios dejan de poder usarlo, pero el consentimiento, los datos indexados por el conector y el servidor MCP remoto siguen intactos
   - c) Se borran los datos que el conector indexó
   - d) Se detiene el servidor MCP remoto

10. ¿Qué sucede desde el 15 de diciembre de 2026 con un entorno de desarrollador no administrado de Power Platform?
   - a) Se convierte automáticamente en administrado
   - b) Se mueve a un sandbox
   - c) Se suspende y sus apps, flujos y agentes dejan de estar disponibles; se elimina desde el 15 de enero de 2027
   - d) Se borra de inmediato

11. ¿Qué afirmación sobre el enrutamiento de entornos es correcta?
   - a) Está activado por defecto para Copilot Studio
   - b) Envía a cada creador a su propio entorno de desarrollador administrado
   - c) Lo bloquea el ajuste «Environment assignment: Developer»
   - d) No requiere Managed Environments

12. Para impedir que los creadores publiquen agentes sin autenticación, ¿qué conector bloqueas en la directiva de datos?
   - a) HTTP
   - b) Direct Line channels in Copilot Studio
   - c) Chat without Microsoft Entra ID authentication in Copilot Studio
   - d) Microsoft Copilot Studio

13. ¿Qué efecto tiene forzar las credenciales del usuario final en «Control maker credential options»?
   - a) Ninguno sobre los agentes existentes
   - b) Solo afecta a los agentes nuevos
   - c) Bloquea la publicación en Teams
   - d) Las herramientas exigen el inicio de sesión del usuario y fallan los agentes autónomos o programados

14. ¿Dónde encuentras las apps de IA generativa en Defender for Cloud Apps?
   - a) En el Cloud app catalog, con la categoría «Generative AI»
   - b) En App governance
   - c) En Exposure Management
   - d) En el Action center

15. ¿Qué licencia exige la DLP de red de Purview (Network Data Security) con Global Secure Access?
   - a) Solo Microsoft 365 E3
   - b) Microsoft 365 E7, o Purview E5 más Entra Internet Access
   - c) Defender for Cloud Apps
   - d) Agent 365

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. El contenido regulatorio y de privacidad es una referencia y no constituye asesoría legal ni laboral: las decisiones sobre captura de prompts, monitoreo, retención y normativa corresponden a tus áreas de Legal, privacidad y RR. HH. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

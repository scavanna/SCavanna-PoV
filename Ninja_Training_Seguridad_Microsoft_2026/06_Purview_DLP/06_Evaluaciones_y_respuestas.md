# Evaluaciones y respuestas

*Microsoft Purview Data Loss Prevention Ninja Training · Edición 2026*

[← Comunidad](05_Comunidad.md) · [Índice del programa](README.md) · [Laboratorio y práctica en producción →](07_Laboratorio_y_practica_en_produccion.md)

<a id="respuestas"></a>

Cada evaluación tiene preguntas de opción múltiple. Con 80 % o más el nivel se considera aprobado. Es una autoevaluación de esta guía, no una certificación de Microsoft.

<a id="eval-inicial"></a>

## Nivel 1 · Inicial · Fundamentos

**1. ¿Qué licencia otorga derecho a DLP para chats y canales de Microsoft Teams?**

- a) Microsoft 365 E3
- b) Exchange Online Plan 2
- c) Microsoft 365 E5, Microsoft Purview Suite o E5 Information Protection & Governance  ✅
- d) Microsoft 365 Business Premium

*Respuesta: c).* La descripción de servicio limita la DLP de Teams a E5/A5/G5, Purview Suite, E5 IP&G u Office 365 E5, con el plan «Microsoft Communications DLP» habilitado. E3 cubre Exchange, SharePoint y OneDrive, y los archivos compartidos en Teams se protegen vía SharePoint y OneDrive. [Fuente](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description) · Repasa [I1](01_Nivel_1_Inicial.md#i1)

**2. ¿Qué ocurre con la ubicación «Instances» de Defender for Cloud Apps en DLP?**

- a) Pasó a disponibilidad general en 2026
- b) Se fusiona con la ubicación de red
- c) Seguirá sin cambios
- d) Se retira el 6 de enero de 2027 y sus directivas deben recrearse como apps no Microsoft conectadas  ✅

*Respuesta: d).* Su retiro acompaña al de las directivas de archivos de Defender for Cloud Apps; el reemplazo, las apps no Microsoft conectadas, está en vista previa desde agosto de 2026. [Fuente](https://learn.microsoft.com/en-us/purview/dlp-use-policies-non-microsoft-cloud-apps) · Repasa [I1](01_Nivel_1_Inicial.md#i1)

**3. ¿Cuántas reglas DLP admite un tenant?**

- a) 100
- b) 600  ✅
- c) 10.000
- d) Ilimitadas

*Respuesta: b).* La referencia de directivas fija 600 reglas DLP por tenant; 10.000 es el máximo combinado de directivas de Information Protection y de gobierno (MIP+MIG). [Fuente](https://learn.microsoft.com/en-us/purview/dlp-policy-reference) · Repasa [I2](01_Nivel_1_Inicial.md#i2)

**4. ¿Qué afirmación sobre el modo de simulación es correcta?**

- a) Sus alertas llegan a Defender XDR como incidentes de severidad baja
- b) Aplica las acciones solo al grupo piloto
- c) «Stop processing more rules» funciona igual que en modo activo
- d) No aplica acciones y sus alertas no llegan al panel de alertas DLP ni a Defender  ✅

*Respuesta: d).* La simulación evalúa sin aplicar acciones, «Stop processing more rules» no funciona y sus alertas solo se ven en el panel de simulación. Para practicar triage necesitas una directiva activa sin bloqueo. [Fuente](https://learn.microsoft.com/en-us/purview/dlp-simulation-mode-learn) · Repasa [I2](01_Nivel_1_Inicial.md#i2)

**5. ¿En cuál de estos clientes NO se muestran sugerencias de directiva DLP?**

- a) Outlook en la web
- b) SharePoint en la web
- c) Cliente de escritorio de OneDrive  ✅
- d) Nuevo Outlook

*Respuesta: c).* No hay sugerencias en los clientes de escritorio de SharePoint y OneDrive, en las apps móviles de Office, en apps de terceros ni on-premises; en Teams no se muestran para archivos. [Fuente](https://learn.microsoft.com/en-us/purview/dlp-policy-tips-reference) · Repasa [I2](01_Nivel_1_Inicial.md#i2)

**6. ¿Dónde aplican las directivas de Edge for Business para apps de IA no gestionadas?**

- a) En cualquier dispositivo con Edge
- b) En Windows 10/11 gestionados por Intune, en todos los perfiles de Edge  ✅
- c) Solo en el perfil de trabajo de dispositivos no gestionados
- d) Solo en Mac gestionados con JAMF

*Respuesta: b).* Las apps no gestionadas se protegen solo en Windows 10/11 gestionados por Intune y en todos los perfiles (trabajo, personal e InPrivate); las apps gestionadas, en dispositivos gestionados y no gestionados, solo en el perfil de trabajo. [Fuente](https://learn.microsoft.com/en-us/purview/dlp-browser-dlp-learn) · Repasa [I3](01_Nivel_1_Inicial.md#i3)

**7. ¿Qué es cierto sobre la protección just-in-time de Endpoint DLP?**

- a) Protege las salidas mientras se clasifica un archivo no evaluado y no genera eventos DLPRuleMatch ni alertas  ✅
- b) Genera eventos DLPRuleMatch y alertas como cualquier regla
- c) Solo funciona en macOS
- d) Requiere pago por uso

*Respuesta: a).* JIT cubre archivos no evaluados o con clasificación obsoleta, requiere el cliente antimalware 4.18.23080 o posterior y se despliega por fases con una acción de reserva. [Fuente](https://learn.microsoft.com/en-us/purview/endpoint-dlp-learn-about-jit) · Repasa [I3](01_Nivel_1_Inicial.md#i3)

**8. ¿Qué cambió en Endpoint DLP en octubre de 2026?**

- a) Se retiró el soporte para macOS
- b) Se retiró la extensión de Purview para Chrome
- c) Llegó a disponibilidad general el control de transferencias FTP y SFTP  ✅
- d) El alcance por grupos de dispositivos volvió a vista previa

*Respuesta: c).* Según las novedades de Purview, el monitoreo y la restricción de FTP y SFTP llegaron a disponibilidad general en octubre de 2026; la actividad no viene activa por defecto. [Fuente](https://learn.microsoft.com/en-us/purview/whats-new) · Repasa [I3](01_Nivel_1_Inicial.md#i3)

**9. Quieres impedir con Edge for Business que, desde equipos gestionados, se peguen datos sensibles en una app de IA no gestionada. ¿Cómo se licencia ese escenario?**

- a) Está incluido en Microsoft 365 E3
- b) Solo requiere Entra ID P1
- c) Requiere obligatoriamente Microsoft 365 E7
- d) Es pago por uso, facturado mediante una suscripción de Azure  ✅

*Respuesta: d).* La descripción de servicio indica que el flujo de dispositivo gestionado a app no gestionada es pago por uso; los escenarios con apps gestionadas registradas en Entra están incluidos en E5 o equivalente. [Fuente](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description) · Repasa [I3](01_Nivel_1_Inicial.md#i3)

**10. ¿Qué rol de mínimo privilegio permite editar las directivas DLP de la ubicación Copilot sin leer prompts ni respuestas?**

- a) Global Administrator
- b) Compliance Administrator
- c) Purview Data Security AI Admin  ✅
- d) Security Reader

*Respuesta: c).* Purview Data Security AI Admin administra la DLP de Copilot sin acceso al contenido de las interacciones. [Fuente](https://learn.microsoft.com/en-us/purview/dlp-microsoft365-copilot-location-learn-about) · Repasa [P0](01_Nivel_1_Inicial.md#p0)

**11. ¿Qué condición debe cumplir un tenant para iniciar la prueba de Microsoft Purview Suite?**

- a) Tener Microsoft 365 E3, u Office 365 E3 con EMS E3, y no tener E5  ✅
- b) Tener Microsoft 365 E5
- c) Estar en una nube de Government
- d) Tener al menos 300 usuarios

*Respuesta: a).* La prueba da 25 licencias por 90 días, ampliables, a tenants con E3 (u Office 365 E3 + EMS E3); no está disponible en Government. [Fuente](https://learn.microsoft.com/en-us/purview/purview-trial) · Repasa [P0](01_Nivel_1_Inicial.md#p0)

**12. ¿Qué ofrece la ruta Ninja oficial de Purview en Microsoft Learn?**

- a) Un examen final con certificado al 80 %
- b) Cinco módulos con evaluación por módulo y una insignia  ✅
- c) Un tenant de laboratorio incluido
- d) Una certificación de Microsoft

*Respuesta: b).* La ruta tiene cinco módulos (1 h 57 min) con un module assessment cada uno y otorga una insignia; no tiene examen final ni certificado al 80 %, que es lo que agrega este programa. [Fuente](https://learn.microsoft.com/en-us/training/paths/purview-ninja-safeguard-data/) · Repasa [I0](01_Nivel_1_Inicial.md#i0)

**13. ¿Qué es cierto sobre DLP para Fabric y Power BI?**

- a) Solo admite áreas de trabajo en capacidad Fabric o Premium y solo la plantilla personalizada  ✅
- b) Admite EDM y clasificadores entrenables
- c) Admite modelos DirectQuery y live connection
- d) La evaluación no consume capacidad

*Respuesta: a).* Las consideraciones excluyen EDM, clasificadores entrenables, DirectQuery y live connection, y la evaluación consume capacidad de Fabric. [Fuente](https://learn.microsoft.com/en-us/purview/dlp-powerbi-get-started) · Repasa [I1](01_Nivel_1_Inicial.md#i1)

**14. ¿Qué afirmación sobre el pago por uso de Purview es correcta?**

- a) Reemplaza a la licencia por usuario
- b) Se suma a la licencia por usuario y se factura mediante una suscripción de Azure  ✅
- c) Solo aplica a Microsoft 365 Copilot
- d) Es gratuito mientras la función esté en vista previa

*Respuesta: b).* Los dos modelos son complementarios: licencia por usuario para Microsoft 365 y endpoints, y pago por uso vía Azure para la red, las apps y agentes de IA y los datos fuera de Microsoft 365. [Fuente](https://learn.microsoft.com/en-us/purview/purview-billing-models) · Repasa [I1](01_Nivel_1_Inicial.md#i1)

**15. Asignaste un rol de Purview mediante PIM para grupos. ¿Cuánto pueden tardar los permisos en hacerse efectivos?**

- a) Se aplican al instante
- b) 24 horas
- c) 7 días
- d) Hasta 2 horas  ✅

*Respuesta: d).* La documentación del portal indica que, con PIM para grupos, los permisos pueden tardar hasta dos horas en aplicarse. [Fuente](https://learn.microsoft.com/en-us/purview/purview-portal) · Repasa [P0](01_Nivel_1_Inicial.md#p0)

<a id="eval-intermedio"></a>

## Nivel 2 · Intermedio · Ajustar, investigar y extender

**1. En los tipos de información confidencial, ¿qué valores corresponden a los niveles de confianza baja, media y alta?**

- a) ≤65, 75 y 85  ✅
- b) 50, 70 y 90
- c) 25, 50 y 75
- d) 60, 80 y 100

*Respuesta: a).* El catálogo de definiciones mapea baja a 65 o menos, media a 75 y alta a 85. Los valores 50, 70 y 90 son umbrales típicos de las huellas digitales con coincidencia parcial. [Fuente](https://learn.microsoft.com/en-us/purview/sit-sensitive-information-type-entity-definitions) · Repasa [M1](02_Nivel_2_Intermedio.md#m1)

**2. ¿Qué advierte la guía oficial sobre la clasificación bajo demanda?**

- a) Solo funciona en modo de simulación
- b) Puede disparar acciones de directivas activas sobre el contenido reclasificado  ✅
- c) No admite SIT personalizados
- d) Requiere pago por uso

*Respuesta: b).* No es una simulación: si hay directivas activas, la reclasificación puede desencadenar sus acciones. Revisa las directivas activas antes de ejecutarla. [Fuente](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-reduce-false-positives-step1) · Repasa [M1](02_Nivel_2_Intermedio.md#m1)

**3. ¿Qué es cierto sobre la analítica DLP (vista previa)?**

- a) Genera recomendaciones en tiempo real
- b) Se actualiza cada semana y da sus primeras recomendaciones a los 7 días sobre 30 días de datos  ✅
- c) Activa directivas en modo de bloqueo de forma automática
- d) Puede activarla cualquier rol de solo lectura

*Respuesta: b).* Es opcional, solo la activan Global Administrator o Compliance Administrator, y las directivas que crea se versionan para poder revertir. [Fuente](https://learn.microsoft.com/en-us/purview/dlp-analytics-get-started) · Repasa [M1](02_Nivel_2_Intermedio.md#m1)

**4. ¿Qué estado tiene el diagnóstico guiado de DLP al corte de noviembre de 2026?**

- a) Retirado
- b) Vista previa privada
- c) Solo para tenants de Government
- d) Disponible en general desde octubre de 2026; sus recomendaciones de Security Copilot requieren E5 y licencia de Copilot elegible  ✅

*Respuesta: d).* Según MC1293479, entró en vista previa en septiembre de 2026 y está en disponibilidad general desde octubre. [Fuente](https://mc.merill.net/message/MC1293479) · Repasa [M1](02_Nivel_2_Intermedio.md#m1)

**5. Según la página general de DLP, ¿cuánto tiempo se conservan las alertas DLP?**

- a) 30 días en Defender y 6 meses en Purview
- b) Un año en ambos portales
- c) 6 meses en el portal de Defender y 30 días en el panel de alertas DLP de Purview  ✅
- d) 90 días en ambos portales

*Respuesta: c).* La página general indica esos plazos y que los administradores acotados por unidad administrativa solo ven sus alertas. Desde octubre de 2026, muchas señales llegan a Defender como behaviors. [Fuente](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp) · Repasa [M2](02_Nivel_2_Intermedio.md#m2)

**6. ¿Cuál es el intervalo de agregación de las alertas DLP con E5 frente a E3?**

- a) 1 minuto con E5 y 15 minutos con E3  ✅
- b) 15 minutos con E5 y 1 hora con E3
- c) 5 minutos en ambos casos
- d) 1 hora con E5 y 24 horas con E3

*Respuesta: a).* Con E5 la agregación es de 1 minuto y puedes crear alertas agregadas por umbral; con E3 es de 15 minutos. [Fuente](https://learn.microsoft.com/en-us/purview/dlp-alerts-get-started) · Repasa [M2](02_Nivel_2_Intermedio.md#m2)

**7. ¿Qué es cierto sobre el explorador de actividad?**

- a) Muestra la actividad en tiempo real
- b) Muestra 30 días, con 60 a 90 minutos de demora en los servicios principales  ✅
- c) Conserva un año de datos
- d) Solo muestra actividad de endpoints

*Respuesta: b).* No es tiempo real y, para endpoints, solo muestra la regla más restrictiva. [Fuente](https://learn.microsoft.com/en-us/purview/data-classification-activity-explorer) · Repasa [M2](02_Nivel_2_Intermedio.md#m2)

**8. ¿Qué afirmación sobre la ubicación Microsoft 365 Copilot y Copilot Chat es correcta?**

- a) DLP escanea los archivos subidos al prompt
- b) Se pueden combinar SIT y etiquetas en la misma regla
- c) Solo está en la plantilla personalizada y no se combina con otras ubicaciones  ✅
- d) Los cambios se aplican al instante

*Respuesta: c).* La ubicación solo existe en la plantilla personalizada y no se combina con otras; no mezcla SIT y etiquetas en una regla, no escanea los archivos subidos al prompt y los cambios tardan hasta 4 horas. [Fuente](https://learn.microsoft.com/en-us/purview/dlp-microsoft365-copilot-location-learn-about) · Repasa [M3](02_Nivel_2_Intermedio.md#m3)

**9. Para la seguridad de datos de red con Global Secure Access, ¿qué licencia indica la página de red de Purview?**

- a) Solo pago por uso
- b) Microsoft 365 E3
- c) Un SASE de terceros obligatorio
- d) Microsoft 365 E7, o Purview E5 más Entra Internet Access, sin pago por uso  ✅

*Respuesta: d).* La página de red (16 de septiembre de 2026) indica esas combinaciones y reserva el pago por uso para los socios SASE; la descripción de servicio, en cambio, lista la DLP de red como pago por uso: valida con tu equipo de cuenta. [Fuente](https://learn.microsoft.com/en-us/purview/dlp-network-data-security-learn) · Repasa [M3](02_Nivel_2_Intermedio.md#m3)

**10. ¿Quiénes pueden usar la DLP que bloquea prompts con SIT en Copilot?**

- a) Solo los clientes con E5
- b) Solo los clientes con E7
- c) Todos los usuarios de Microsoft 365 Copilot y Copilot Chat  ✅
- d) Solo los clientes con Purview Suite

*Respuesta: c).* Según la descripción de servicio, la DLP de prompts está disponible para todos los usuarios de Copilot y Copilot Chat; impedir que Copilot procese contenido etiquetado, en cambio, requiere E5 o equivalente. [Fuente](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description) · Repasa [M3](02_Nivel_2_Intermedio.md#m3)

**11. Según la matriz de agentes de Purview (mayo de 2026), ¿qué agentes no admiten DLP?**

- a) Los de Copilot Studio
- b) Los de Microsoft Foundry
- c) El Channel Agent de Teams
- d) Los de ChatGPT Enterprise y Claude Enterprise  ✅

*Respuesta: d).* Los agentes de ChatGPT Enterprise solo admiten clasificación e Insider Risk y los de Claude Enterprise, ninguna protección; Copilot Studio, Foundry y Channel Agent sí admiten DLP. [Fuente](https://learn.microsoft.com/en-us/purview/ai-agents) · Repasa [M3](02_Nivel_2_Intermedio.md#m3)

**12. ¿Qué ubicaciones admite hoy la DLP adaptativa?**

- a) Todas las ubicaciones
- b) Exchange, Teams y dispositivos  ✅
- c) Solo SharePoint y OneDrive
- d) Solo Copilot

*Respuesta: b).* Aunque agregues otras ubicaciones, la protección adaptativa solo actúa en Exchange, Teams y dispositivos. [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-adaptive-protection) · Repasa [M4](02_Nivel_2_Intermedio.md#m4)

**13. ¿Qué directivas DLP crea la configuración rápida de la protección adaptativa?**

- a) Dos directivas en modo de prueba: bloqueo para Elevated y auditoría para Moderate y Minor  ✅
- b) Una directiva en bloqueo para todos los niveles
- c) Ninguna: solo crea una directiva de Acceso condicional en modo activo
- d) Directivas de red para Global Secure Access

*Respuesta: a).* Crea una directiva para Teams y Exchange y otra para dispositivos, en modo de prueba, junto con una directiva de Acceso condicional en solo informe y una de retención; tarda hasta 72 horas. [Fuente](https://learn.microsoft.com/en-us/purview/dlp-adaptive-protection-learn) · Repasa [M4](02_Nivel_2_Intermedio.md#m4)

**14. En la protección adaptativa, ¿dónde aparecen los nombres reales de las personas aunque Insider Risk los seudonimice?**

- a) En ningún lugar
- b) Solo en los informes de RR. HH.
- c) En las alertas DLP y en el explorador de actividad  ✅
- d) Solo en Defender for Endpoint

*Respuesta: c).* La seudonimización de Insider Risk no se conserva en DLP: inclúyelo en la evaluación de impacto de privacidad. [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-adaptive-protection) · Repasa [M4](02_Nivel_2_Intermedio.md#m4)

**15. ¿Qué acciones admite la seguridad de datos de red?**

- a) Solo auditar o bloquear  ✅
- b) Cifrar y poner en cuarentena
- c) Bloquear con invalidación y justificación
- d) Etiquetar de forma automática

*Respuesta: a).* La red solo audita o bloquea, no aplica a invitados B2B y tiene límites en línea de 4 MB para texto y 3 MB para archivos. [Fuente](https://learn.microsoft.com/en-us/purview/dlp-network-data-security-learn) · Repasa [M3](02_Nivel_2_Intermedio.md#m3)

<a id="eval-avanzado"></a>

## Nivel 3 · Avanzado · Código, SOC y clasificación a escala

**1. Desde inicios de octubre de 2026, ¿qué ocurre por defecto con las señales DLP en Defender XDR?**

- a) Se eliminan
- b) Solo se envían a Sentinel
- c) Se convierten en casos de Insider Risk
- d) Una regla integrada de ajuste las registra como behaviors y no crean incidentes  ✅

*Respuesta: d).* La regla integrada se puede deshabilitar o acotar en Settings > Microsoft Defender XDR > Alert tuning. [Fuente](https://learn.microsoft.com/en-us/defender-xdr/dlp-investigate-alerts-defender) · Repasa [A2](03_Nivel_3_Avanzado.md#a2)

**2. ¿Cuándo dejó de devolver datos la API heredada /security/alerts de Microsoft Graph?**

- a) 1 de julio de 2026
- b) 15 de octubre de 2026  ✅
- c) 6 de enero de 2027
- d) 31 de marzo de 2027

*Respuesta: b).* La guía de migración fija el 15 de octubre de 2026 y recomienda alerts_v2 e incidents. El 6 de enero de 2027 es la fecha de retiro de «Instances». [Fuente](https://learn.microsoft.com/en-us/graph/alertsv1-alertsv2-migration) · Repasa [A2](03_Nivel_3_Avanzado.md#a2)

**3. ¿Qué limitación tiene alerts_v2 de Microsoft Graph respecto de las alertas DLP?**

- a) No incluye alertas de DLP
- b) Solo devuelve alertas de los últimos 7 días
- c) No devuelve las alertas suprimidas por reglas de ajuste  ✅
- d) Requiere Microsoft 365 E7

*Respuesta: c).* alerts_v2 e incidents incluyen DLP e Insider Risk, pero no devuelven las alertas ajustadas: si la regla integrada convierte las señales en behaviors, tu integración no las verá como alertas. [Fuente](https://learn.microsoft.com/en-us/graph/alertsv1-alertsv2-migration) · Repasa [A2](03_Nivel_3_Avanzado.md#a2)

**4. ¿Dónde se deshabilita o acota la regla integrada que convierte las señales DLP en behaviors?**

- a) En Purview > Data loss prevention > Settings
- b) En Settings > Microsoft Defender XDR > Alert tuning, en el portal de Defender  ✅
- c) En el centro de administración de Entra
- d) En la configuración del workspace de Sentinel

*Respuesta: b).* Es una regla de ajuste de alertas de Defender XDR y se administra desde su portal. [Fuente](https://learn.microsoft.com/en-us/defender-xdr/dlp-investigate-alerts-defender) · Repasa [A2](03_Nivel_3_Avanzado.md#a2)

**5. ¿Cómo se crean las directivas DLP para apps registradas en Entra?**

- a) Solo con PowerShell  ✅
- b) Desde el portal de Purview con una plantilla
- c) Con Power Automate
- d) Desde el centro de administración de Entra

*Respuesta: a).* La guía de las APIs de Purview indica que esas directivas solo se crean con PowerShell (New-DlpComplianceRule) y que no hay APIs para extraer datos de Purview. [Fuente](https://learn.microsoft.com/en-us/purview/developer/use-the-api) · Repasa [A1](03_Nivel_3_Avanzado.md#a1)

**6. ¿Qué plano de aplicación reemplaza al obsoleto «Entra» en la DLP de apps de IA personalizadas?**

- a) Endpoint
- b) Network
- c) Browser
- d) Application  ✅

*Respuesta: d).* El script de muestra para la DLP de apps de IA personalizadas usa el plano «Application», que reemplaza al plano «Entra». [Fuente](https://github.com/microsoft/purview-api-samples) · Repasa [A1](03_Nivel_3_Avanzado.md#a1)

**7. ¿Qué es cierto sobre Power Automate como acción de una regla DLP?**

- a) Requiere una licencia adicional de Purview
- b) Funciona en Exchange, SharePoint y OneDrive, y Windows 24H2 o posterior, sin licencia adicional de Purview  ✅
- c) Solo funciona en Teams
- d) En SharePoint se dispara también con contenido existente sin cambios

*Respuesta: b).* No requiere licencia adicional de Purview, aunque los conectores premium requieren un plan de Power Automate; en SharePoint y OneDrive solo se dispara con contenido nuevo o modificado. [Fuente](https://learn.microsoft.com/en-us/purview/dlp-powerautomate-int-get-started) · Repasa [A1](03_Nivel_3_Avanzado.md#a1)

**8. ¿Cuál es el estado de la variante de tenant de processContent para interacciones de agentes?**

- a) Disponible en general desde mayo de 2026
- b) Retirada
- c) Beta desde el 23 de octubre de 2026, sin soporte para producción  ✅
- d) Disponible solo en nubes de Government

*Respuesta: c).* La variante de tenant está en beta; la versión por usuario de processContent está en v1.0. [Fuente](https://learn.microsoft.com/en-us/graph/api/tenantdatasecurityandgovernance-processcontent?view=graph-rest-beta) · Repasa [A1](03_Nivel_3_Avanzado.md#a1)

**9. Para un SIT EDM preciso, ¿qué elemento primario recomienda la guía?**

- a) Un SIT estrictamente definido  ✅
- b) Un nombre completo
- c) Una dirección postal
- d) Una expresión regular amplia

*Respuesta: a).* Los SIT laxos —nombres, direcciones o expresiones regulares amplias— degradan el rendimiento y causan falsos negativos. [Fuente](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-reduce-false-positives-step2) · Repasa [A3](03_Nivel_3_Avanzado.md#a3)

**10. ¿Qué limitación tienen los clientes E3 con las huellas digitales de documentos?**

- a) No pueden usarlas en Exchange
- b) Solo pueden usar coincidencia exacta
- c) Deben pagarlas por uso
- d) Desde abril de 2023 no pueden crear ni modificar huellas nuevas  ✅

*Respuesta: d).* La documentación de huellas digitales lo indica; para crearlas y gestionarlas se recomienda E5. [Fuente](https://learn.microsoft.com/en-us/purview/sit-document-fingerprinting) · Repasa [A3](03_Nivel_3_Avanzado.md#a3)

**11. ¿Cómo se factura el OCR de Purview?**

- a) Está incluido en E3
- b) Por pago por uso, por imagen o por página  ✅
- c) Con SCU de Security Copilot
- d) Con la licencia de Microsoft 365 Copilot

*Respuesta: b).* El OCR para DLP, etiquetado automático e Insider Risk se factura por pago por uso y requiere vincular una suscripción de Azure; acota el alcance por ubicación para controlar el costo. [Fuente](https://learn.microsoft.com/en-us/purview/ocr-learn-about) · Repasa [A3](03_Nivel_3_Avanzado.md#a3)

**12. ¿Qué es cierto sobre el agente de triage de DLP?**

- a) Tría alertas de directivas en simulación
- b) Se administra desde el portal de Defender
- c) Requiere licencia DLP, pago por uso y SCU, y tría Exchange, Teams, SharePoint, OneDrive y dispositivos  ✅
- d) Analiza archivos de cualquier tamaño

*Respuesta: c).* Solo tría directivas activas, analiza archivos de hasta 2 MB, mira hasta 30 días atrás y se gestiona solo desde Purview, aunque se despliegue desde Defender. [Fuente](https://learn.microsoft.com/en-us/purview/copilot-in-purview-triage-dlp-agent-get-started) · Repasa [A4](03_Nivel_3_Avanzado.md#a4)

**13. Según el Centro de mensajes, ¿cuándo se espera la disponibilidad general de los resúmenes del agente de triage en las alertas DLP de Defender XDR?**

- a) Octubre de 2026
- b) Diciembre de 2026
- c) Ya están en disponibilidad general
- d) Agosto de 2027  ✅

*Respuesta: d).* MC1255406 pospuso la GA de agosto de 2026 a agosto de 2027; mientras tanto siguen en vista previa. [Fuente](https://mc.merill.net/message/MC1255406) · Repasa [A4](03_Nivel_3_Avanzado.md#a4)

**14. ¿Cuántas SCU de Security Copilot incluye Microsoft 365 E5?**

- a) 400 SCU al mes por cada 1.000 licencias pagas, hasta 10.000  ✅
- b) 100 SCU fijas por tenant
- c) Ninguna
- d) SCU ilimitadas

*Respuesta: a).* La inclusión aplica a licencias pagas, por lo que una prueba no la habilita; el agente de triage consume esas SCU. [Fuente](https://learn.microsoft.com/en-us/copilot/security/security-copilot-inclusion) · Repasa [A4](03_Nivel_3_Avanzado.md#a4)

<a id="eval-operacion"></a>

## Nivel 4 · Operación · Modelo operativo, métricas y gobierno

**1. Según la guía de planificación de DLP, ¿cómo suelen repartirse las necesidades de protección?**

- a) Cerca de 85 % regulatorias y 15 % de propiedad intelectual  ✅
- b) 50 % regulatorias y 50 % de propiedad intelectual
- c) 15 % regulatorias y 85 % de propiedad intelectual
- d) 100 % regulatorias

*Respuesta: a).* La guía lo usa para priorizar partes interesadas, categorías de información y objetivos. [Fuente](https://learn.microsoft.com/en-us/purview/dlp-overview-plan-for-dlp) · Repasa [O1](04_Nivel_4_Operacion.md#o1)

**2. ¿Qué permite el modelo «cercado» (ring-fenced) con unidades administrativas?**

- a) Eliminar el equipo central
- b) Que cada país administre e investigue lo suyo mientras el equipo central mantiene el gobierno  ✅
- c) Compartir alertas con otros tenants
- d) Prescindir de las licencias E5

*Respuesta: b).* Las tres arquitecturas de referencia de abril de 2026 muestran cómo descentralizar la operación por región o por población sensible sin perder el gobierno central. [Fuente](https://techcommunity.microsoft.com/blog/microsoft-purview-blog/deploy-scalable-ring%E2%80%91fenced-purview-operations-with-administrative-units/4512556) · Repasa [O1](04_Nivel_4_Operacion.md#o1)

**3. ¿Qué pieza de DLP no admite unidades administrativas y debe quedar en el equipo central?**

- a) Las directivas de Exchange
- b) Las alertas de Endpoint DLP
- c) La DLP de apps no Microsoft conectadas (vista previa)  ✅
- d) Los SIT integrados

*Respuesta: c).* La ubicación de apps no Microsoft conectadas no admite unidades administrativas, sugerencias, invalidaciones ni simulación. [Fuente](https://learn.microsoft.com/en-us/purview/dlp-non-microsoft-connected-applications) · Repasa [O1](04_Nivel_4_Operacion.md#o1)

**4. ¿Qué limitación tienen los reportes de postura de Information Protection y DLP?**

- a) Muestran un año de datos
- b) Incluyen las directivas en simulación
- c) Solo se exportan a Excel
- d) Usan una ventana móvil de 30 días y no incluyen directivas en simulación  ✅

*Respuesta: d).* Están en vista previa; exporta a PDF para conservar el histórico. [Fuente](https://learn.microsoft.com/en-us/purview/purview-reports) · Repasa [O2](04_Nivel_4_Operacion.md#o2)

**5. ¿Qué KPI de DSPM mide la cobertura de DLP?**

- a) Número de directivas creadas
- b) Porcentaje de activos sensibles protegidos por al menos una directiva DLP  ✅
- c) Cantidad de alertas por día
- d) Número de personas bloqueadas

*Respuesta: b).* La guía de DSPM lo propone como indicador de cobertura y recomienda revisar las recomendaciones al menos cada 30 días. [Fuente](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-dspm-step3) · Repasa [O2](04_Nivel_4_Operacion.md#o2)

**6. ¿Qué datos ofrece el panel de salud de dispositivos de Purview?**

- a) Solo el inventario de licencias
- b) El contenido de los archivos bloqueados
- c) Las alertas de Defender for Endpoint
- d) Cobertura de incorporación, dispositivos en riesgo de no recibir actualizaciones y preparación para JIT, con 30 días de datos  ✅

*Respuesta: d).* Se actualiza cada hora y es la fuente del KPI de cobertura de endpoints. [Fuente](https://learn.microsoft.com/en-us/purview/device-onboarding-health-reports-dashboard) · Repasa [O2](04_Nivel_4_Operacion.md#o2)

**7. ¿Cómo conservas el histórico de los reportes de postura, que solo muestran 30 días?**

- a) No es posible conservarlo
- b) Activando una retención de un año en el reporte
- c) Exportándolos a PDF de forma periódica  ✅
- d) Pidiendo un respaldo a soporte

*Respuesta: c).* La documentación recomienda exportar a PDF para mantener el histórico. [Fuente](https://learn.microsoft.com/en-us/purview/purview-reports) · Repasa [O2](04_Nivel_4_Operacion.md#o2)

**8. ¿Qué ciclo propone Data Security Workbench para las alertas DLP?**

- a) Observar, explicar, mejorar y probar  ✅
- b) Bloquear, notificar y cerrar
- c) Detectar, contener, erradicar y recuperar
- d) Planificar, comprar y desplegar

*Respuesta: a).* Es un proyecto de código abierto publicado por un empleado de Microsoft para pasar del volumen de alertas a una calidad de detección medible; no es un producto soportado. [Fuente](https://techcommunity.microsoft.com/blog/microsoft-security-blog/from-dlp-alert-volume-to-measurable-detection-assurance/4545973) · Repasa [O2](04_Nivel_4_Operacion.md#o2)

**9. ¿Qué identificadores agregó el catálogo de SIT en junio de 2026?**

- a) RFC y CURP de México
- b) RUT de Chile
- c) La cédula y el número de identificación tributaria de Colombia  ✅
- d) DNI de Perú

*Respuesta: c).* Según las novedades de Purview de junio de 2026, se sumaron identificadores de Colombia; para los países sin SIT integrado, crea SIT personalizados. [Fuente](https://learn.microsoft.com/en-us/purview/whats-new) · Repasa [O3](04_Nivel_4_Operacion.md#o3)

**10. ¿Qué recomienda la guía sobre las cuentas de almacenamiento para la evidencia de endpoints?**

- a) Una sola cuenta compartida por todas las áreas
- b) Compartimentarlas por población y limitar quién descarga  ✅
- c) Usar almacenamiento público para facilitar las auditorías
- d) No definir retención

*Respuesta: b).* La evidencia contiene copias completas de archivos: compartimentar (por ejemplo, RR. HH. y ejecutivos) y limitar las descargas reduce el riesgo de privacidad. [Fuente](https://learn.microsoft.com/en-us/purview/dlp-copy-matched-items-get-started) · Repasa [O3](04_Nivel_4_Operacion.md#o3)

**11. Con un SASE de terceros para la DLP de red, ¿qué debe revisar privacidad?**

- a) Nada, porque el socio no recibe datos
- b) Solo el precio por solicitud
- c) Que el socio reemplaza a Purview
- d) Que el socio puede acceder a parte de la configuración, incluidos identificadores de usuario, y almacenarla  ✅

*Respuesta: d).* La página de red lo advierte; inclúyelo en la evaluación de impacto y en el contrato con el socio. [Fuente](https://learn.microsoft.com/en-us/purview/dlp-network-data-security-learn) · Repasa [O3](04_Nivel_4_Operacion.md#o3)

**12. ¿Dónde se define en Purview la captura de prompts y respuestas de IA?**

- a) En las directivas de recopilación  ✅
- b) En las etiquetas de retención
- c) En Defender for Cloud Apps
- d) En el centro de administración de Teams

*Respuesta: a).* Las directivas de recopilación definen qué actividades y contenidos se capturan; revisa con Legal y privacidad antes de capturar contenido. [Fuente](https://learn.microsoft.com/en-us/purview/collection-policies-policy-reference) · Repasa [O3](04_Nivel_4_Operacion.md#o3)

**13. Según la hoja «Normativa MCSA», ¿desde cuándo rige la Ley 21.719 de protección de datos personales de Chile?**

- a) 1 de enero de 2025
- b) 1 de diciembre de 2026  ✅
- c) 20 de marzo de 2025
- d) Rige desde 2012

*Respuesta: b).* Fue publicada en diciembre de 2024 y entra en vigencia el 1 de diciembre de 2026; las implicancias para tu programa debe evaluarlas Legal. [Fuente](https://www.leychile.cl/leychile/Navegar?idNorma=1209272&idParte=1) · Repasa [O3](04_Nivel_4_Operacion.md#o3)

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. No constituye asesoría legal ni laboral: las decisiones sobre monitoreo, evidencias, privacidad y normativa corresponden a tus áreas de Legal, RR. HH. y privacidad. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

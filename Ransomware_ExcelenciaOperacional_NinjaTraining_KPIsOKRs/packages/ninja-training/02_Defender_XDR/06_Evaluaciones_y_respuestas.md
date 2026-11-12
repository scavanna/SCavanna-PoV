# Evaluaciones y respuestas

*Microsoft Defender XDR Ninja Training · Edición 2026*

[← Comunidad](05_Comunidad.md) · [Índice del programa](README.md) · [Laboratorio y práctica en producción →](07_Laboratorio_y_practica_en_produccion.md)

<a id="respuestas"></a>

Cada evaluación tiene preguntas de opción múltiple. Con 80 % o más el nivel se considera aprobado. Es una autoevaluación de esta guía, no una certificación de Microsoft.

<a id="eval-inicial"></a>

## Nivel 1 · Inicial · Fundamentos

**1. ¿Qué dominio tiene más peso en el examen SC-200 según las habilidades medidas del 21 de octubre de 2026?**

- a) Búsqueda de amenazas (20–25 %)
- b) Responder a incidentes (35–40 %)
- c) Gestionar el entorno de operaciones de seguridad (40–45 %)  ✅
- d) Configurar Microsoft Purview (30 %)

*Respuesta: c).* Gestionar el entorno de operaciones de seguridad pesa 40–45 %; responder a incidentes, 35–40 %, y la búsqueda de amenazas, 20–25 %. Purview no es un dominio del examen. [Fuente](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-200) · Repasa [I0](01_Nivel_1_Inicial.md#i0)

**2. ¿Cómo evalúa el avance el Ninja oficial de Defender XDR?**

- a) Con un examen supervisado al final del programa
- b) Con un knowledge check al final de cada nivel  ✅
- c) Con una insignia de Credly del examen SC-200
- d) No tiene evaluación

*Respuesta: b).* Cada nivel (Fundamentals, Intermediate y Expert) incluye un knowledge check. La certificación formal es el examen SC-200, que es otra credencial. [Fuente](https://learn.microsoft.com/en-us/defender-xdr/microsoft-365-defender-train-security-staff) · Repasa [I0](01_Nivel_1_Inicial.md#i0)

**3. ¿Quién puede usar la vista previa de ISOC en Microsoft Defender desde el 23 de septiembre de 2026?**

- a) Cualquier cliente con un workspace de Sentinel
- b) Solo los clientes de Microsoft 365 E7
- c) Solo los proveedores de servicios gestionados
- d) Clientes de Defender Suite, Microsoft 365 E5 o E7 sin un workspace de Sentinel activo  ✅

*Respuesta: d).* ISOC está pensado para clientes elegibles que todavía no tienen un workspace de Sentinel activo; tenerlo no te hace elegible, y E7 no es el único plan que califica. [Fuente](https://learn.microsoft.com/en-us/defender-xdr/isoc-overview) · Repasa [I1](01_Nivel_1_Inicial.md#i1)

**4. Desde el 1 de julio de 2026, ¿qué incluye Microsoft 365 E3 respecto de Defender for Office 365?**

- a) El Plan 1: Safe Links, Safe Attachments, anti-phishing y Real-time detections  ✅
- b) El Plan 2 completo, con Threat Explorer y AIR
- c) Solo Exchange Online Protection
- d) Solo Attack simulation training

*Respuesta: a).* E3 incluye el Plan 1 desde esa fecha; Threat Explorer, AIR y Attack simulation training siguen en el Plan 2 (E5, A5, G5 o Defender Suite). [Fuente](https://learn.microsoft.com/en-us/office365/servicedescriptions/office-365-advanced-threat-protection-service-description) · Repasa [I2](01_Nivel_1_Inicial.md#i2)

**5. Un inquilino tiene 4.000 licencias pagas de Microsoft 365 E5. ¿Cuántas SCU de Security Copilot al mes recibe por la inclusión?**

- a) 400
- b) 1.600  ✅
- c) 4.000
- d) 10.000

*Respuesta: b).* La inclusión otorga 400 SCU por cada 1.000 licencias pagas, con un tope de 10.000 al mes: 4 × 400 = 1.600. [Fuente](https://www.microsoft.com/en-us/security/security-copilot-in-microsoft-365-e5) · Repasa [I2](01_Nivel_1_Inicial.md#i2)

**6. Según la guía de inicio de Defender for Office 365, ¿qué conviene resolver antes de ajustar las políticas de amenazas?**

- a) Lanzar una campaña de Attack simulation training
- b) Crear reglas de flujo de correo personalizadas
- c) La autenticación del correo: SPF, DKIM y DMARC  ✅
- d) Desactivar la protección integrada

*Respuesta: c).* La guía empieza por SPF, DKIM y DMARC y recomienda corregir la autenticación antes de ajustar políticas; la simulación de ataques llega más adelante. [Fuente](https://learn.microsoft.com/en-us/defender-office-365/mdo-deployment-guide) · Repasa [I3](01_Nivel_1_Inicial.md#i3)

**7. ¿Qué recomienda Microsoft para incorporar servidores a Defender for Endpoint?**

- a) Defender for Servers Plan 2  ✅
- b) Una licencia independiente de MDE P1
- c) Una licencia independiente de MDE P2
- d) Microsoft 365 E3

*Respuesta: a).* Defender for Servers Plan 2 trae incorporación automática, gestión de vulnerabilidades premium y 500 MB diarios de ingesta incluidos; las licencias independientes de MDE P1 y P2 no cubren servidores. [Fuente](https://learn.microsoft.com/en-us/defender-endpoint/onboard-server) · Repasa [I4](01_Nivel_1_Inicial.md#i4)

**8. ¿Qué cuenta usa el sensor v3.x de Defender for Identity para leer Active Directory y ejecutar acciones?**

- a) Una cuenta de servicio de directorio (DSA)
- b) Una gMSA
- c) La cuenta de servicio de Entra Connect
- d) LocalSystem del servidor  ✅

*Respuesta: d).* El v3.x solo admite LocalSystem; si la cuenta de acción queda en gMSA tras migrar, las acciones de respuesta dejan de funcionar. [Fuente](https://learn.microsoft.com/en-us/defender-for-identity/deploy/deploy-sensor-v3) · Repasa [I5](01_Nivel_1_Inicial.md#i5)

**9. ¿Cuál de estas NO es una limitación del sensor v3.x de Defender for Identity?**

- a) No integra VPN
- b) Requiere Npcap  ✅
- c) No envía notificaciones syslog
- d) Tiene limitaciones con ExpressRoute

*Respuesta: b).* Npcap lo usaba el sensor v2.x y puede retirarse después de migrar; las otras tres opciones sí son limitaciones documentadas del v3.x. [Fuente](https://learn.microsoft.com/en-us/defender-for-identity/deploy/deploy-sensor-v3) · Repasa [I5](01_Nivel_1_Inicial.md#i5)

**10. ¿Cuándo se dispara la detección «Password spray» de Entra ID Protection?**

- a) Ante cualquier intento fallido de inicio de sesión
- b) Cuando se bloquea una cuenta por intentos fallidos
- c) Cuando el atacante valida con éxito la contraseña de un usuario del inquilino  ✅
- d) Cuando se usa autenticación heredada

*Respuesta: c).* Según el catálogo oficial, la detección se dispara cuando el ataque logra validar una contraseña; los intentos fallidos por sí solos no la generan. [Fuente](https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-risks) · Repasa [I6](01_Nivel_1_Inicial.md#i6)

**11. Sin licencia Entra ID P2, ¿cómo ves las detecciones Premium de ID Protection?**

- a) Con el detalle completo de cada detección
- b) No ves nada: no se registra ningún riesgo
- c) Solo como detecciones fuera de línea
- d) Solo como «Additional risk detected»  ✅

*Respuesta: d).* El catálogo separa detecciones Premium y no Premium: sin P2, las Premium aparecen como «Additional risk detected». [Fuente](https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-risks) · Repasa [I6](01_Nivel_1_Inicial.md#i6)

**12. ¿Cuántas filas puede devolver como máximo una consulta de búsqueda avanzada en el portal de Defender?**

- a) 10.000
- b) 50.000
- c) 1.000.000
- d) 100.000  ✅

*Respuesta: d).* El límite documentado es de 100.000 filas por consulta, con 10 minutos de ejecución y 64 MB de resultado. [Fuente](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-overview) · Repasa [I7](01_Nivel_1_Inicial.md#i7)

**13. ¿Qué tabla reemplazó a AIAgentsInfo en la búsqueda avanzada?**

- a) AgentsInventory
- b) AgentsInfo  ✅
- c) CloudAppEvents
- d) BehaviorInfo

*Respuesta: b).* AIAgentsInfo fue accesible hasta el 1 de julio de 2026; las consultas y detecciones deben migrar a AgentsInfo. [Fuente](https://learn.microsoft.com/en-us/defender-xdr/whats-new) · Repasa [I7](01_Nivel_1_Inicial.md#i7)

**14. ¿Qué pasa con los datos que viven solo en el data lake de Sentinel?**

- a) No se consultan desde la búsqueda avanzada; se usan la exploración del data lake o los search jobs  ✅
- b) Se consultan directamente en la búsqueda avanzada
- c) Se copian solos al nivel de análisis
- d) Solo se consultan por API

*Respuesta: a).* La página de búsqueda avanzada aclara que esos datos no se consultan desde ahí; para eso existen la exploración del data lake y los search jobs. [Fuente](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-overview) · Repasa [I7](01_Nivel_1_Inicial.md#i7)

**15. ¿Qué licencia requiere Attack simulation training completo?**

- a) Microsoft 365 E3 sin complementos
- b) Exchange Online Plan 2
- c) Microsoft 365 E5 o Defender for Office 365 Plan 2  ✅
- d) Defender for Endpoint P2

*Respuesta: c).* AST requiere Microsoft 365 E5 o MDO Plan 2; E3 solo tiene una prueba limitada con el payload Credential Harvest y dos experiencias de formación. [Fuente](https://learn.microsoft.com/en-us/defender-office-365/attack-simulation-training-get-started) · Repasa [I8](01_Nivel_1_Inicial.md#i8)

<a id="eval-intermedio"></a>

## Nivel 2 · Intermedio · Operar, investigar y responder

**1. En el RBAC unificado, ¿qué permiso te deja gestionar casos de incidente (asignar, clasificar y cerrar)?**

- a) Security Data Read
- b) Security Data Manage  ✅
- c) Security settings (manage)
- d) System settings (read)

*Respuesta: b).* Ver casos requiere Security Data Read y gestionarlos, Security Data Manage; los permisos de configuración no habilitan la gestión de casos. [Fuente](https://learn.microsoft.com/en-us/defender-xdr/manage-incident-cases) · Repasa [M1](02_Nivel_2_Intermedio.md#m1)

**2. Durante la investigación de un buzón comprometido (BEC), ¿cuál es la acción preferida según Microsoft?**

- a) Deshabilitar la cuenta  ✅
- b) Borrar el buzón
- c) Enviar un aviso a todos los contactos
- d) Esperar a que termine la investigación de AIR

*Respuesta: a).* Deshabilitar la cuenta es la acción preferida mientras investigas; luego se cambia la contraseña y se revisan reglas de buzón, reenvíos y delegaciones. [Fuente](https://learn.microsoft.com/en-us/defender-office-365/responding-to-a-compromised-email-account) · Repasa [M2](02_Nivel_2_Intermedio.md#m2)

**3. En un despliegue de reglas ASR, ¿cuáles pueden pasar directamente a Block o Warn sin una fase de auditoría?**

- a) Todas
- b) Ninguna
- c) Solo las reglas de Office
- d) Las reglas de protección estándar  ✅

*Respuesta: d).* Solo las reglas de protección estándar pueden ir directo a Block o Warn; las demás se prueban primero en Audit, que registra el evento 1122. [Fuente](https://learn.microsoft.com/en-us/defender-endpoint/attack-surface-reduction-rules-deployment) · Repasa [M3](02_Nivel_2_Intermedio.md#m3)

**4. Con el antivirus de Defender en modo pasivo y EDR en modo bloqueo, ¿qué capacidad NO funciona?**

- a) La remediación de detecciones de EDR
- b) Las reglas ASR  ✅
- c) Las alertas de EDR
- d) El Action center

*Respuesta: b).* En modo pasivo no funcionan la protección en tiempo real, ASR, network protection ni los indicadores; EDR en modo bloqueo sí remedia detecciones de comportamiento. [Fuente](https://learn.microsoft.com/en-us/defender-endpoint/edr-in-block-mode) · Repasa [M3](02_Nivel_2_Intermedio.md#m3)

**5. ¿Por qué los mapas de rutas de movimiento lateral de Defender for Identity dejaron de actualizarse?**

- a) Por el retiro del portal clásico de MDI
- b) Por la migración al sensor v3.x
- c) Porque desde mayo de 2025 MDI dejó de recolectar administradores locales por SAM-R  ✅
- d) Por falta de licencia de Exposure Management

*Respuesta: c).* MC1073068 anunció que MDI dejaría de recolectar por SAM-R a mediados de mayo de 2025; los reemplazos son la pestaña Attack paths e Identity Explorer. [Fuente](https://mc.merill.net/message/MC1073068) · Repasa [M4](02_Nivel_2_Intermedio.md#m4)

**6. Si después de migrar al sensor v3.x la cuenta de acción sigue configurada como gMSA, ¿qué ocurre?**

- a) Nada: el v3.x la convierte solo
- b) La migración falla y vuelve al v2.x
- c) Se desactiva el sensor
- d) Las acciones de respuesta, incluida la interrupción automática, no funcionan  ✅

*Respuesta: d).* El v3.x solo admite LocalSystem; con gMSA, las acciones de respuesta y la interrupción automática dejan de funcionar. [Fuente](https://learn.microsoft.com/en-us/defender-for-identity/deploy/migrate-to-sensor-v3) · Repasa [M4](02_Nivel_2_Intermedio.md#m4)

**7. ¿Cuándo se retiraron las directivas de riesgo heredadas de Entra ID Protection?**

- a) El 1 de octubre de 2026  ✅
- b) El 1 de julio de 2025
- c) El 19 de octubre de 2026
- d) Siguen vigentes

*Respuesta: a).* Se retiraron el 1 de octubre de 2026 y deben recrearse como directivas de acceso condicional, primero en modo solo informe. El 19 de octubre es la fecha del cambio de tabla en la búsqueda avanzada. [Fuente](https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-configure-risk-policies) · Repasa [M5](02_Nivel_2_Intermedio.md#m5)

**8. ¿Qué agrega automáticamente el control «Require risk remediation» en una directiva de riesgo de usuario?**

- a) Bloqueo de acceso y dispositivo conforme
- b) Ubicación de confianza y MFA por SMS
- c) Authentication strength y sign-in frequency «Every time»  ✅
- d) Nada más

*Respuesta: c).* Al elegir «Require risk remediation», Entra agrega authentication strength y sign-in frequency «Every time» para forzar una reautenticación segura. [Fuente](https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-configure-risk-policies) · Repasa [M5](02_Nivel_2_Intermedio.md#m5)

**9. ¿Qué capacidad de Defender Vulnerability Management NO viene con MDE P2 sin el complemento?**

- a) El inventario de software
- b) La evaluación de vulnerabilidades
- c) La priorización por riesgo
- d) La evaluación de líneas base de seguridad  ✅

*Respuesta: d).* Las líneas base de seguridad, el bloqueo de aplicaciones vulnerables, las extensiones, los certificados y el firmware son capacidades premium; el núcleo viene con MDE P2. [Fuente](https://learn.microsoft.com/en-us/defender-vulnerability-management/defender-vulnerability-management-capabilities) · Repasa [M6](02_Nivel_2_Intermedio.md#m6)

**10. ¿Con qué nivel de confianza actúa la interrupción automática de ataques al contener?**

- a) 80 %
- b) 90 %
- c) Al menos 99 %  ✅
- d) 100 % garantizado

*Respuesta: c).* Microsoft documenta una confianza de al menos 99 % para las acciones de contención, que además son reversibles. [Fuente](https://learn.microsoft.com/en-us/defender-xdr/automatic-attack-disruption) · Repasa [M7](02_Nivel_2_Intermedio.md#m7)

**11. Desde el 1 de septiembre de 2026, ¿qué cambió en AIR?**

- a) Desapareció en todo Defender
- b) En MDE deja de ser una experiencia separada y no se dispara manualmente; en MDO sigue disponible  ✅
- c) Solo funciona con MDO Plan 1
- d) Requiere Defender Experts

*Respuesta: b).* El cambio aplica a Defender for Endpoint, cuyas capacidades pasan a la pila antivirus. El AIR de MDO sigue disponible y el Action center conserva aprobación, historial y deshacer. [Fuente](https://learn.microsoft.com/en-us/defender-xdr/m365d-action-center) · Repasa [M7](02_Nivel_2_Intermedio.md#m7)

**12. Al incorporar un workspace al portal de Defender con licencia de Defender XDR, ¿qué pasa con el conector independiente de MDE en Sentinel?**

- a) Se desconecta automáticamente  ✅
- b) Sigue activo y duplica alertas
- c) Se replica en los workspaces secundarios
- d) Se convierte en un conector del data lake

*Respuesta: a).* Se desconectan los conectores independientes de Defender for Cloud Apps (alertas), MDE, MDI, MDO y Entra ID Protection para evitar duplicados; el conector de Defender XDR se configura solo. [Fuente](https://learn.microsoft.com/en-us/azure/sentinel/microsoft-365-defender-sentinel-integration) · Repasa [M8](02_Nivel_2_Intermedio.md#m8)

**13. ¿Qué tabla reemplazó a AADSignInEventsBeta el 19 de octubre de 2026?**

- a) SigninLogs
- b) IdentityLogonEvents
- c) IdentityAccountInfo
- d) EntraIdSignInEvents  ✅

*Respuesta: d).* EntraIdSignInEvents la reemplazó con migración automática de consultas y detecciones, y requiere Entra ID P2. [Fuente](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-entraidsigninevents-table) · Repasa [M9](02_Nivel_2_Intermedio.md#m9)

**14. ¿Qué impide que una detección personalizada use la frecuencia Continuous (NRT)?**

- a) Usar un join  ✅
- b) Usar una sola tabla
- c) Proyectar ReportId
- d) Consultar DeviceEvents

*Respuesta: a).* NRT exige una sola tabla, sin join, union ni externaldata, y solo columnas GA. [Fuente](https://learn.microsoft.com/en-us/defender-xdr/custom-detection-rules) · Repasa [M10](02_Nivel_2_Intermedio.md#m10)

**15. En el ajuste de alertas, ¿qué acción solo aplica a alertas de Defender for Endpoint?**

- a) Resolve alert
- b) Set as behavior
- c) Hide alert  ✅
- d) Add tag

*Respuesta: c).* Hide solo aplica a MDE; Resolve está disponible en general y Set as behavior no aplica a MDO ni a Defender for Cloud. [Fuente](https://learn.microsoft.com/en-us/defender-xdr/investigate-alerts) · Repasa [M10](02_Nivel_2_Intermedio.md#m10)

<a id="eval-avanzado"></a>

## Nivel 3 · Avanzado · Respuesta, automatización e ingeniería

**1. ¿Qué documento reemplazó en abril de 2025 a NIST SP 800-61 Rev. 2?**

- a) NIST CSF 1.1
- b) ISO/IEC 27035
- c) SP 800-61 Rev. 3, perfil comunitario del CSF 2.0  ✅
- d) SP 800-84

*Respuesta: c).* La Rev. 3, publicada el 3 de abril de 2025, alinea la respuesta a incidentes con las funciones del CSF 2.0 y reemplaza a la Rev. 2 de 2012. [Fuente](https://csrc.nist.gov/pubs/sp/800/61/r3/final) · Repasa [A1](03_Nivel_3_Avanzado.md#a1)

**2. Según el playbook de consentimiento de aplicaciones, ¿qué haces con una aplicación maliciosa confirmada?**

- a) La deshabilitas sin borrarla  ✅
- b) La borras de inmediato
- c) Solo cambias la contraseña del usuario que dio el consentimiento
- d) La dejas activa para observar al atacante

*Respuesta: a).* La guía indica deshabilitar la aplicación, no borrarla, revisar los permisos concedidos y reportarla a Microsoft; borrarla destruye evidencia. [Fuente](https://learn.microsoft.com/en-us/security/zero-trust/security-operations-playbook-app-consent) · Repasa [A1](03_Nivel_3_Avanzado.md#a1)

**3. En el portal de Defender, ¿cómo automatizas la respuesta a alertas de Defender XDR (no de Sentinel)?**

- a) Con una regla que use el disparador de alerta clásico
- b) Con Microsoft incident creation rules
- c) Con Fusion
- d) Con el Enhanced Alert Trigger  ✅

*Respuesta: d).* El disparador de alerta clásico solo actúa sobre alertas de Sentinel, y las Microsoft incident creation rules no existen en el portal de Defender. [Fuente](https://learn.microsoft.com/en-us/azure/sentinel/automation/automation) · Repasa [A2](03_Nivel_3_Avanzado.md#a2)

**4. ¿Hasta cuándo funciona la acción «Advanced Hunting» del conector de Logic Apps de Defender for Endpoint?**

- a) Hasta el 31 de marzo de 2027
- b) Hasta el 1 de febrero de 2027; después hay que usar Microsoft Graph  ✅
- c) Indefinidamente
- d) Hasta el 15 de octubre de 2026

*Respuesta: b).* La acción se retira el 1 de febrero de 2027, junto con las API antiguas de búsqueda avanzada; la alternativa es runHuntingQuery de Graph. El 31 de marzo de 2027 es la fecha de Sentinel en el portal de Azure. [Fuente](https://learn.microsoft.com/en-us/connectors/wdatp/) · Repasa [A2](03_Nivel_3_Avanzado.md#a2)

**5. ¿Qué pasó con el portal independiente de Microsoft Defender Threat Intelligence?**

- a) Se retiró el 1 de agosto de 2026 y la inteligencia pública se ofrece sin costo adicional en Defender  ✅
- b) Pasó a requerir una licencia premium por usuario
- c) Se integró solo en Sentinel en el portal de Azure
- d) Sigue igual que en 2024

*Respuesta: a).* El portal de MDTI y el Intel explorer heredado se retiraron el 1 de agosto de 2026; los datos públicos de inteligencia están disponibles sin costo adicional para clientes de Defender XDR. [Fuente](https://learn.microsoft.com/en-us/defender-xdr/threat-intelligence-explorer) · Repasa [A3](03_Nivel_3_Avanzado.md#a3)

**6. ¿Qué requiere el hunting graph?**

- a) Solo una licencia de MDE P1
- b) El data lake de Sentinel y permisos de lectura en Exposure Management  ✅
- c) Un contrato de Defender Experts Hunting
- d) Una capacidad dedicada de Security Copilot

*Respuesta: b).* El hunting graph se apoya en el data lake de Sentinel y requiere permisos de lectura en Exposure Management. [Fuente](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-graph) · Repasa [A3](03_Nivel_3_Avanzado.md#a3)

**7. ¿Qué API de Microsoft Graph quedó retirada el 15 de octubre de 2026?**

- a) alerts_v2
- b) incidents
- c) runHuntingQuery
- d) La API heredada de alertas (/security/alerts)  ✅

*Respuesta: d).* La API heredada de alertas se retiró; las integraciones deben migrar a alerts_v2 e incidents. [Fuente](https://learn.microsoft.com/en-us/graph/api/resources/security-api-overview?view=graph-rest-1.0) · Repasa [A4](03_Nivel_3_Avanzado.md#a4)

**8. ¿Qué permiso requiere analyzedEmail: remediate?**

- a) Mail.ReadWrite delegado
- b) ThreatHunting.Read.All
- c) SecurityAnalyzedMessage.ReadWrite.All de aplicación  ✅
- d) CustomDetection.ReadWrite.All

*Respuesta: c).* Solo se admite el permiso de aplicación SecurityAnalyzedMessage.ReadWrite.All, y cada acción se sigue en el Action center. [Fuente](https://learn.microsoft.com/en-us/graph/api/security-analyzedemail-remediate?view=graph-rest-1.0) · Repasa [A4](03_Nivel_3_Avanzado.md#a4)

**9. Antes de una prueba de BAS contra Defender for Endpoint, ¿qué recomienda Microsoft?**

- a) Desactivar la protección contra alteraciones para que la herramienta funcione
- b) Excluir la herramienta de BAS del antivirus
- c) Poner ASR en Audit para no interferir
- d) Protección contra alteraciones, ASR y network protection en bloqueo, protección en la nube activa y sin exclusiones para la herramienta  ✅

*Respuesta: d).* La guía pide probar la configuración real de protección: bloqueo activo y ninguna exclusión para las herramientas de BAS; de lo contrario, el resultado no refleja tu defensa. [Fuente](https://learn.microsoft.com/en-us/defender-endpoint/guidance-for-pen-testing-and-bas) · Repasa [A5](03_Nivel_3_Avanzado.md#a5)

**10. ¿Qué pasa con los cambios hechos en el portal a una detección gestionada desde Sentinel Repositories?**

- a) Se sincronizan de vuelta al repositorio
- b) El repositorio los sobrescribe en el siguiente despliegue  ✅
- c) Bloquean el despliegue
- d) Se guardan como una nueva versión

*Respuesta: b).* El repositorio pasa a ser la única fuente de verdad y sobrescribe los cambios del portal; por eso todo cambio debe ir por pull request. [Fuente](https://learn.microsoft.com/en-us/azure/sentinel/ci-cd-custom-content) · Repasa [A5](03_Nivel_3_Avanzado.md#a5)

**11. ¿Cuál es el estado del Dynamic Threat Detection Agent según Learn en noviembre de 2026?**

- a) GA y consume SCU
- b) Retirado
- c) Vista previa gratuita que consumirá SCU al llegar a GA  ✅
- d) Solo disponible dentro de Project Perception

*Respuesta: c).* Learn lo describe como vista previa, siempre activa y gratuita, que consumirá SCU en GA; algunas fuentes comunitarias mencionan otras fechas sin confirmación oficial. [Fuente](https://learn.microsoft.com/en-us/defender-xdr/dynamic-threat-detection-agent) · Repasa [A6](03_Nivel_3_Avanzado.md#a6)

**12. ¿Qué requiere el Security Alert Triage Agent para clasificar alertas?**

- a) SCU de Security Copilot, el RBAC unificado activo y desactivar las reglas de ajuste que resuelven solas esas alertas  ✅
- b) Solo una licencia de MDO Plan 1
- c) Un workspace de Sentinel con UEBA
- d) Un contrato de Defender Experts MDR

*Respuesta: a).* El agente consume SCU, necesita el RBAC unificado y no puede clasificar alertas que una regla de ajuste ya resolvió; su aprendizaje por retroalimentación aplica al correo. [Fuente](https://learn.microsoft.com/en-us/defender-xdr/security-alert-triage-agent) · Repasa [A6](03_Nivel_3_Avanzado.md#a6)

**13. En la gestión multiinquilino de Defender, ¿cómo se accede a los datos de Microsoft Sentinel de los inquilinos gestionados?**

- a) Con GDAP
- b) Con Entra B2B, porque GDAP no está soportado para Sentinel  ✅
- c) Con una cuenta compartida
- d) Con una clave de API

*Respuesta: b).* Los datos de Defender admiten GDAP o B2B, pero Sentinel solo admite B2B; las consultas entre workspaces usan Azure Lighthouse. [Fuente](https://learn.microsoft.com/en-us/defender-xdr/mto-requirements) · Repasa [A7](03_Nivel_3_Avanzado.md#a7)

**14. ¿Qué agrega Defender Experts MDR Plan 2 respecto del Plan 1?**

- a) Caza de amenazas en servidores
- b) Respuesta a incidentes sin contrato aparte
- c) Licencias de Microsoft 365 E5
- d) Cobertura de telemetría de terceros a través de Sentinel  ✅

*Respuesta: d).* El Plan 1 (antes Defender Experts for XDR) cubre las cargas de Defender; el Plan 2 suma fuentes de terceros vía Sentinel. Hunting e Incident Response se contratan aparte. [Fuente](https://learn.microsoft.com/en-us/defender-xdr/defender-experts/defender-experts-mdr-overview) · Repasa [A7](03_Nivel_3_Avanzado.md#a7)

**15. En el caso de AiTM y BEC que Microsoft publicó en enero de 2026, ¿qué exigió la contención además del cambio de contraseña?**

- a) Reinstalar todos los equipos de la organización
- b) Desactivar Safe Links
- c) Revocar las cookies de sesión y eliminar las reglas de buzón creadas por el atacante  ✅
- d) Bloquear SharePoint para toda la organización

*Respuesta: c).* Con AiTM, el atacante reutiliza la sesión robada: sin revocar sesiones y borrar las reglas de buzón, el cambio de contraseña no basta. [Fuente](https://www.microsoft.com/en-us/security/blog/2026/01/21/multistage-aitm-phishing-bec-campaign-abusing-sharepoint/) · Repasa [A8](03_Nivel_3_Avanzado.md#a8)

<a id="eval-excelencia"></a>

## Nivel 4 · Excelencia del SOC · Operación de clase mundial

**1. ¿Qué taller del Security Adoption Framework cubre el burnout, la estrategia XDR + SIEM + data lake, la tercerización y la planificación del SOC?**

- a) El CISO Workshop
- b) El resumen de la MCRA
- c) Security ADS Module 3 · Modern Security Operations  ✅
- d) El taller de identidades y acceso

*Respuesta: c).* Es el ADS de operaciones de seguridad del catálogo de talleres del SAF; su versión guiada requiere Microsoft Unified, pero hay versiones públicas autoguiadas. [Fuente](https://learn.microsoft.com/en-us/security/zero-trust/workshop-business-overview) · Repasa [S1](04_Nivel_4_Excelencia_del_SOC.md#s1)

**2. Según el taller de SecOps del SAF, el modelo de roles del SOC se basa en…**

- a) especialización, no jerarquía  ✅
- b) una jerarquía estricta por antigüedad
- c) la rotación aleatoria de funciones
- d) la tercerización total

*Respuesta: a).* El taller lo explicita: las capas (triage, investigación, ingeniería y liderazgo) se definen por especialización y no por jerarquía. [Fuente](https://learn.microsoft.com/en-us/security/zero-trust/workshop-business-security-operations) · Repasa [S1](04_Nivel_4_Excelencia_del_SOC.md#s1)

**3. En el SAF, ¿cuándo termina el MTTA?**

- a) Al cerrar el incidente
- b) Al contener la amenaza
- c) Al crearse la alerta
- d) Cuando un analista toma el incidente  ✅

*Respuesta: d).* El MTTA mide el tiempo hasta el reconocimiento: termina cuando un analista toma la propiedad del incidente. [Fuente](https://learn.microsoft.com/en-us/security/zero-trust/security-adoption-discipline-security-operations-incidents) · Repasa [S2](04_Nivel_4_Excelencia_del_SOC.md#s2)

**4. Ante un adversario atrincherado, ¿qué riesgo tiene una remediación parcial?**

- a) Ninguno, si se hace rápido
- b) Alerta al atacante, que puede cambiar de táctica o de acceso  ✅
- c) Solo aumenta el costo de licencias
- d) Obliga a reinstalar Defender

*Respuesta: b).* El SAF advierte que la remediación parcial alerta al atacante; ante un adversario atrincherado conviene una remediación coordinada a gran escala. [Fuente](https://learn.microsoft.com/en-us/security/zero-trust/security-adoption-discipline-security-operations-incidents) · Repasa [S2](04_Nivel_4_Excelencia_del_SOC.md#s2)

**5. ¿Cómo calcula el workbook de Sentinel el «time to triage»?**

- a) ClosedTime − CreatedTime
- b) FirstModifiedTime − CreatedTime  ✅
- c) LastActivityTime − FirstActivityTime
- d) CreatedTime − FirstActivityTime

*Respuesta: b).* Time to triage es FirstModifiedTime − CreatedTime y time to closure, ClosedTime − CreatedTime, ambos calculados por percentiles. [Fuente](https://learn.microsoft.com/en-us/azure/sentinel/manage-soc-with-incident-metrics) · Repasa [S3](04_Nivel_4_Excelencia_del_SOC.md#s3)

**6. ¿Por qué hay que deduplicar SecurityIncident por IncidentNumber antes de calcular métricas?**

- a) Porque cada actualización de un incidente crea una fila nueva  ✅
- b) Porque la tabla mezcla alertas e incidentes
- c) Porque los incidentes se borran a los 30 días
- d) Porque IncidentNumber cambia al cerrar

*Respuesta: a).* Cada cambio del incidente agrega una fila; arg_max(TimeGenerated, *) by IncidentNumber deja la versión más reciente de cada uno. [Fuente](https://learn.microsoft.com/en-us/azure/sentinel/manage-soc-with-incident-metrics) · Repasa [S3](04_Nivel_4_Excelencia_del_SOC.md#s3)

**7. En SOC optimization, una cobertura «media» frente a una amenaza significa que tienes activas…**

- a) más del 75 % de las reglas recomendadas
- b) entre el 0 y el 29 %
- c) exactamente la mitad
- d) entre el 30 y el 74 % de las reglas recomendadas  ✅

*Respuesta: d).* Alta es más de 75 %, media entre 30 y 74 % y baja entre 0 y 29 % de las reglas recomendadas activas. [Fuente](https://learn.microsoft.com/en-us/azure/sentinel/soc-optimization/soc-optimization-access) · Repasa [S3](04_Nivel_4_Excelencia_del_SOC.md#s3)

**8. ¿En qué escala mide SOC-CMM la madurez?**

- a) De 1 a 3
- b) De 0 a 5  ✅
- c) De la A a la F
- d) Sí o no por control

*Respuesta: b).* SOC-CMM usa niveles de madurez de 0 (inexistente) a 5 (optimizando); la capacidad usa una escala de 0 a 3. [Fuente](https://www.soc-cmm.com/img/upload/files/37-advancing-soc-capability-and-maturity.pdf) · Repasa [S4](04_Nivel_4_Excelencia_del_SOC.md#s4)

**9. Según el informe SOC-CMM de 2025, ¿qué frena el crecimiento de la madurez?**

- a) La falta de herramientas de IA
- b) El uso de marcos públicos
- c) La sobreestimación en las autoevaluaciones  ✅
- d) El trabajo remoto

*Respuesta: c).* El informe concluye que la sobreestimación en las autoevaluaciones frena la mejora; por eso conviene pedir evidencias y una validación externa. [Fuente](https://www.soc-cmm.com/img/upload/files/30-socmaturityreport2025.pdf) · Repasa [S4](04_Nivel_4_Excelencia_del_SOC.md#s4)

**10. ¿Qué exige desplegar detecciones personalizadas como código mediante Sentinel Repositories?**

- a) Solo Sentinel en el portal de Azure
- b) Una licencia que incluya Defender XDR (por ejemplo, E5) y el workspace incorporado al portal de Defender  ✅
- c) Un contrato de Defender Experts
- d) Nada adicional

*Respuesta: b).* La documentación de despliegue lo exige; además, el repositorio pasa a ser la única fuente de verdad. [Fuente](https://learn.microsoft.com/en-us/azure/sentinel/ci-cd) · Repasa [S5](04_Nivel_4_Excelencia_del_SOC.md#s5)

**11. ¿Por qué la página MITRE ATT&CK de Sentinel no basta para afirmar que tienes cobertura?**

- a) Porque solo muestra técnicas de Windows
- b) Porque se actualiza una vez al año
- c) Porque requiere Defender Experts
- d) Porque solo considera reglas activas: contar reglas no prueba que detecten; hay que validar con emulación  ✅

*Respuesta: d).* La página (vista previa, alineada a ATT&CK v18) cuenta reglas activas; la cobertura real se valida con emulación, como en un purple team. [Fuente](https://learn.microsoft.com/en-us/azure/sentinel/mitre-coverage) · Repasa [S5](04_Nivel_4_Excelencia_del_SOC.md#s5)

**12. ¿Qué recomienda Microsoft sobre excluir activos de la interrupción automática de ataques?**

- a) La desaconseja porque reduce la eficacia; cada exclusión debe justificarse  ✅
- b) Excluir todos los servidores críticos por defecto
- c) Excluir a todos los ejecutivos
- d) No es posible excluir activos

*Respuesta: a).* La página de exclusiones advierte que excluir activos reduce la eficacia de la interrupción; las exclusiones se limitan a casos documentados, como las cuentas de emergencia. [Fuente](https://learn.microsoft.com/en-us/defender-xdr/automatic-attack-disruption-exclusions) · Repasa [S6](04_Nivel_4_Excelencia_del_SOC.md#s6)

**13. En el modelo de SOC agéntico que Microsoft describió en abril de 2026, ¿qué conservan las personas?**

- a) Solo la aprobación de licencias
- b) Nada: los agentes deciden todo
- c) El juicio y las prioridades, mientras la plataforma interrumpe y los agentes razonan  ✅
- d) Solo el triage de nivel 1

*Respuesta: c).* El modelo tiene dos capas —interrupción determinista acotada por políticas y agentes que razonan— y deja a las personas el juicio y las prioridades. [Fuente](https://www.microsoft.com/en-us/security/blog/2026/04/09/the-agentic-soc-rethinking-secops-for-the-next-decade/) · Repasa [S6](04_Nivel_4_Excelencia_del_SOC.md#s6)

**14. Según el MDDR 2026, ¿cuál es la mediana entre el descubrimiento de una vulnerabilidad y su explotación?**

- a) 7 días
- b) Entre 30 y 60 días
- c) Menos de 24 horas  ✅
- d) 90 días

*Respuesta: c).* La mediana baja de 24 horas, mientras la remediación empresarial tarda entre 30 y 60 días: por eso hay que priorizar por explotación y criticidad. [Fuente](https://www.microsoft.com/en-us/security/security-insider/threat-landscape/2026-digital-defense-report) · Repasa [S7](04_Nivel_4_Excelencia_del_SOC.md#s7)

**15. ¿Qué recomienda el MDDR 2026 reportar a la dirección?**

- a) Parches desplegados
- b) Tickets cerrados por analista
- c) Alertas totales recibidas
- d) Exposición reducida, cobertura de detección y tiempo de mitigación  ✅

*Respuesta: d).* El informe pide pasar de métricas de actividad a resultados: exposición reducida, cobertura de detección aumentada y tiempo de mitigación comprimido. [Fuente](https://www.microsoft.com/en-us/corporate-responsibility/topics/cybersecurity/reports/microsoft-digital-defense-report/) · Repasa [S7](04_Nivel_4_Excelencia_del_SOC.md#s7)

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

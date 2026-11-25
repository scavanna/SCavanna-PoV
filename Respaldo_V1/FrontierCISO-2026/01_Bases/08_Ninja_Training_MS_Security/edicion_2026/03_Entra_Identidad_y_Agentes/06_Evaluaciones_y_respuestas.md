# Evaluaciones y respuestas

*Microsoft Entra Ninja Training: identidad y acceso para la era de los agentes de IA · Edición 2026*

[← Comunidad](05_Comunidad.md) · [Índice del programa](README.md) · [Laboratorio y práctica en producción →](07_Laboratorio_y_practica_en_produccion.md)

<a id="respuestas"></a>

Cada evaluación tiene preguntas de opción múltiple. Con 80 % o más el nivel se considera aprobado. Es una autoevaluación de esta guía, no una certificación de Microsoft.

<a id="eval-inicial"></a>

## Nivel 1 · Inicial · Fundamentos

**1. ¿Qué plan de Microsoft Entra incluye Microsoft 365 E5?**

- a) Entra Suite
- b) Entra ID P2  ✅
- c) Entra ID Governance completo
- d) Internet Access

*Respuesta: b).* E5 incluye Entra ID P2. Entra Suite —con ID Governance, Private Access e Internet Access— viene en Microsoft 365 E7 o se compra aparte. [Fuente](https://learn.microsoft.com/en-us/entra/fundamentals/licensing) · Repasa [I1](01_Nivel_1_Inicial.md#i1)

**2. ¿Qué licencia necesita el perfil de tráfico de Microsoft de Global Secure Access?**

- a) Entra Suite
- b) Internet Access
- c) Workload ID Premium
- d) Entra ID P1 o P2  ✅

*Respuesta: d).* El perfil de tráfico de Microsoft solo requiere P1 o P2, así que está disponible con E3 y E5; Private Access e Internet Access requieren su propia licencia, Entra Suite o E7. [Fuente](https://learn.microsoft.com/en-us/entra/global-secure-access/concept-traffic-forwarding) · Repasa [I1](01_Nivel_1_Inicial.md#i1)

**3. ¿Qué se necesita para aplicar acceso condicional a los agentes de IA?**

- a) Solo Entra ID P1
- b) Workload ID Premium
- c) Microsoft 365 E7, o Agent 365 más al menos P1 o E3  ✅
- d) Nada adicional: Agent ID es gratuito para todos

*Respuesta: c).* Agent ID está disponible para todos los clientes de Entra, pero el acceso condicional para agentes requiere E7, o Agent 365 más al menos Entra ID P1 o Microsoft 365 E3. [Fuente](https://learn.microsoft.com/en-us/entra/identity/conditional-access/agent-id) · Repasa [I1](01_Nivel_1_Inicial.md#i1)

**4. ¿A qué operaciones afecta la fase 2 del MFA obligatorio de Azure, vigente desde el 1 de octubre de 2025?**

- a) Crear, actualizar y borrar recursos de Azure por CLI, PowerShell, IaC, REST y SDK  ✅
- b) Solo el inicio de sesión en el portal de Azure
- c) Las identidades administradas y los service principals
- d) Solo las lecturas de la API

*Respuesta: a).* La fase 1 cubrió los portales de administración; la fase 2 alcanza la gestión de Azure desde herramientas y código. Las workload identities no se ven afectadas. [Fuente](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-mandatory-multifactor-authentication) · Repasa [I2](01_Nivel_1_Inicial.md#i2)

**5. ¿Qué método recomienda Microsoft para proteger las cuentas de emergencia?**

- a) SMS
- b) Llamada de voz
- c) Passkey FIDO2  ✅
- d) Ninguno: deben quedar sin MFA

*Respuesta: c).* Las cuentas de emergencia también deben cumplir el MFA obligatorio; Microsoft recomienda passkey FIDO2 (o CBA) y monitorear cada uso. [Fuente](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/security-emergency-access) · Repasa [I2](01_Nivel_1_Inicial.md#i2)

**6. Asocias una acción protegida a una política de acceso condicional que está en modo solo informe. ¿Qué ocurre?**

- a) Protege igual que una política activa
- b) Bloquea a todos los administradores
- c) Solo resta puntos en Identity Secure Score
- d) No protege la acción: la política debe estar activada  ✅

*Respuesta: d).* Para que una acción protegida funcione, la política asociada a su contexto de autenticación debe estar activada; en solo informe no exige nada. [Fuente](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/protected-actions-add) · Repasa [I2](01_Nivel_1_Inicial.md#i2)

**7. ¿Cuándo deja Microsoft de entregar SMS y voz a los Global Administrators activos y a los usuarios externos?**

- a) 1 de febrero de 2027
- b) 1 de julio de 2027  ✅
- c) 1 de septiembre de 2026
- d) 7 de abril de 2027

*Respuesta: b).* Según el documento vigente de Learn, el retiro general es el 1 de febrero de 2027 y el de Global Administrators activos y usuarios externos, el 1 de julio de 2027. El blog de julio de 2026 daba una sola fecha. [Fuente](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sms-voice-retirement) · Repasa [I3](01_Nivel_1_Inicial.md#i3)

**8. Desde el 30 de septiembre de 2025, ¿dónde se gestionan los métodos de autenticación?**

- a) En la política de métodos de autenticación  ✅
- b) En la configuración de MFA por usuario
- c) En la política heredada de SSPR
- d) En los valores predeterminados de seguridad

*Respuesta: a).* Desde esa fecha ya no se pueden gestionar métodos en las políticas heredadas de MFA y SSPR; solo las preguntas de seguridad siguen en la configuración heredada de SSPR. [Fuente](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-methods-manage) · Repasa [I3](01_Nivel_1_Inicial.md#i3)

**9. ¿Qué método NO satisface la fortaleza de autenticación «MFA resistente al phishing»?**

- a) Llave de seguridad FIDO2
- b) CBA multifactor
- c) Temporary Access Pass  ✅
- d) Windows Hello for Business

*Respuesta: c).* TAP solo satisface la fortaleza MFA; la resistente al phishing admite Windows Hello o la credencial de plataforma, FIDO2 y CBA multifactor. [Fuente](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-strengths) · Repasa [I3](01_Nivel_1_Inicial.md#i3)

**10. Una política de acceso condicional administrada por Microsoft se crea en solo informe. ¿Cuándo se activa?**

- a) Al menos 30 días después de crearse, con aviso dos semanas antes  ✅
- b) De inmediato
- c) A los 7 días
- d) Nunca, salvo que la actives tú

*Respuesta: a).* Microsoft las activa automáticamente tras al menos 30 días en solo informe y avisa dos semanas antes; no se pueden renombrar ni borrar. [Fuente](https://learn.microsoft.com/en-us/entra/identity/conditional-access/managed-policies) · Repasa [I4](01_Nivel_1_Inicial.md#i4)

**11. ¿Qué NO evalúa la herramienta What If de acceso condicional?**

- a) Inicios de sesión de usuarios
- b) Service principals
- c) Identidades de agente (vista previa)
- d) Dependencias de servicio, como la de Teams con Exchange Online  ✅

*Respuesta: d).* What If usa la API What If Evaluation de Microsoft Graph y simula usuarios, service principals e identidades de agente, pero no evalúa las dependencias de servicio. [Fuente](https://learn.microsoft.com/en-us/entra/identity/conditional-access/what-if-tool) · Repasa [I4](01_Nivel_1_Inicial.md#i4)

**12. ¿Qué necesita Entra Connect Sync para seguir sincronizando después del 7 de abril de 2027?**

- a) La versión 2.5.79.0
- b) Migrar a AD FS
- c) La versión 2.6.84.0 o superior con autenticación basada en aplicación  ✅
- d) Activar Connect Health

*Respuesta: c).* El aviso vigente exige 2.6.84.0 o superior con autenticación basada en aplicación; el aviso anterior pedía 2.5.79.0 antes del 30 de septiembre de 2026. [Fuente](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/reference-connect-version-history) · Repasa [I5](01_Nivel_1_Inicial.md#i5)

**13. ¿Por qué conviene activar la sincronización de hash de contraseñas aunque uses PTA o federación?**

- a) Porque reemplaza a Cloud Sync
- b) Porque la detección de credenciales filtradas de ID Protection la necesita  ✅
- c) Porque elimina la necesidad de MFA
- d) Porque es obligatoria desde 2026

*Respuesta: b).* PHS es la opción más simple y resiliente, y algunas capacidades, como la detección de credenciales filtradas, la requieren aunque uses otro método. [Fuente](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/choose-ad-authn) · Repasa [I5](01_Nivel_1_Inicial.md#i5)

**14. ¿Cuánto dura por defecto un token de acceso de Microsoft Entra?**

- a) 5 minutos
- b) 24 horas
- c) 90 días
- d) 1 hora  ✅

*Respuesta: d).* Un token de acceso dura una hora por defecto; CAE acorta la reacción ante eventos críticos en los servicios compatibles. [Fuente](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-continuous-access-evaluation) · Repasa [P0](01_Nivel_1_Inicial.md#p0)

**15. Lanzas el laboratorio de la credencial Applied Skills de identidades y acceso y no lo terminas. ¿Qué ocurre?**

- a) Debes esperar 72 horas para relanzarlo  ✅
- b) Puedes relanzarlo de inmediato
- c) Pierdes tu certificación SC-300
- d) Debes pagar un nuevo intento

*Respuesta: a).* La evaluación es un laboratorio interactivo de 2 horas y, una vez lanzado, hay que esperar 72 horas para volver a lanzarlo. [Fuente](https://learn.microsoft.com/en-us/credentials/applied-skills/get-started-with-identities-and-access-using-microsoft-entra/) · Repasa [I0](01_Nivel_1_Inicial.md#i0)

<a id="eval-intermedio"></a>

## Nivel 2 · Intermedio · Proteger, gobernar y observar

**1. La protección de tokens para apps nativas está en disponibilidad general en:**

- a) Solo Windows
- b) Windows, iOS/iPadOS y macOS  ✅
- c) Solo navegadores
- d) Android y Linux

*Respuesta: b).* Está en GA para apps nativas en Windows, iOS/iPadOS y macOS; las apps de navegador hacia Azure Resource Manager siguen en vista previa. La propia página aún muestra «Apple (Preview)» en una sección. [Fuente](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-token-protection) · Repasa [M1](02_Nivel_2_Intermedio.md#m1)

**2. ¿Qué valores puede tomar un contexto de autenticación?**

- a) C1 a C99  ✅
- b) A1 a A9
- c) R1 a R25
- d) Cualquier texto libre

*Respuesta: a).* Los contextos de autenticación usan identificadores de C1 a C99, que las apps, PIM o las acciones protegidas solicitan para exigir una política más estricta. [Fuente](https://learn.microsoft.com/en-us/entra/identity-platform/developer-guide-conditional-access-authentication-context) · Repasa [M1](02_Nivel_2_Intermedio.md#m1)

**3. Desde septiembre de 2024, una política de flujos de autenticación dirigida a «All resources» también aplica a:**

- a) Las identidades administradas
- b) Los agentes de Copilot Studio
- c) El Device Registration Service  ✅
- d) Las cuentas de emergencia

*Respuesta: c).* Desde septiembre de 2024 esas políticas también aplican al Device Registration Service: revisa su impacto en el registro de dispositivos. [Fuente](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-authentication-flows) · Repasa [M1](02_Nivel_2_Intermedio.md#m1)

**4. ¿Cuándo se retiraron las políticas de riesgo heredadas de ID Protection?**

- a) 30 de septiembre de 2025
- b) 1 de marzo de 2027
- c) 1 de octubre de 2026  ✅
- d) No se retiraron

*Respuesta: c).* Se retiraron el 1 de octubre de 2026; la vía soportada son las políticas de acceso condicional basadas en riesgo. [Fuente](https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-configure-risk-policies) · Repasa [M2](02_Nivel_2_Intermedio.md#m2)

**5. Con «Require risk remediation», ¿qué ocurre con un usuario sin contraseña que tiene riesgo de usuario alto?**

- a) Debe cambiar la contraseña
- b) Queda bloqueado hasta que un administrador lo libere
- c) No ocurre nada
- d) Se revocan sus sesiones y debe volver a iniciar sesión  ✅

*Respuesta: d).* El control adapta la remediación: cambio seguro de contraseña para usuarios con contraseña, revocación de sesiones para usuarios sin contraseña y deshabilitación del dispositivo si lo agregó un atacante. [Fuente](https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-policies) · Repasa [M2](02_Nivel_2_Intermedio.md#m2)

**6. ¿Cuánto pueden tardar en aparecer las detecciones de riesgo fuera de línea?**

- a) 5 minutos
- b) Hasta 48 horas  ✅
- c) 30 días
- d) 6 meses

*Respuesta: b).* Las detecciones en tiempo real aparecen en 5 a 10 minutos y las fuera de línea, hasta en 48 horas; seis meses es lo que tarda en caducar el riesgo bajo. [Fuente](https://learn.microsoft.com/en-us/entra/id-protection/concept-risk-detection-types) · Repasa [M2](02_Nivel_2_Intermedio.md#m2)

**7. ¿Qué rol mínimo necesitas para configurar las opciones de un rol de Entra en PIM?**

- a) Security Administrator
- b) Global Reader
- c) Privileged Role Administrator  ✅
- d) User Administrator

*Respuesta: c).* Configurar la duración de activación, la aprobación o el contexto de autenticación de un rol requiere al menos Privileged Role Administrator. [Fuente](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-how-to-change-default-settings) · Repasa [M3](02_Nivel_2_Intermedio.md#m3)

**8. Si vence la licencia que habilita PIM, ¿qué pasa con las asignaciones?**

- a) No pasa nada
- b) Se eliminan las elegibles y las activas temporales pasan a permanentes  ✅
- c) Se eliminan todas
- d) Todas pasan a elegibles

*Respuesta: b).* Es un riesgo poco conocido: sin licencia, las asignaciones elegibles se eliminan y las activas temporales quedan como permanentes. [Fuente](https://learn.microsoft.com/en-us/entra/id-governance/licensing-fundamentals) · Repasa [M3](02_Nivel_2_Intermedio.md#m3)

**9. ¿Qué función de gobernanza NO está incluida en Microsoft 365 E5?**

- a) PIM for Groups
- b) Revisiones de acceso de roles de Entra
- c) Controles de acceso condicional en PIM
- d) Lifecycle Workflows  ✅

*Respuesta: d).* Lifecycle Workflows requiere ID Governance o Entra Suite; PIM, PIM for Groups y las revisiones básicas vienen con P2. [Fuente](https://learn.microsoft.com/en-us/entra/id-governance/licensing-fundamentals) · Repasa [M4](02_Nivel_2_Intermedio.md#m4)

**10. ¿Qué licencia requiere sincronizar grupos entre tenants?**

- a) Entra ID P1
- b) Entra ID P2
- c) ID Governance o Entra Suite  ✅
- d) Workload ID Premium

*Respuesta: c).* La sincronización de usuarios entre tenants requiere P1; la de grupos, en GA desde junio de 2026, requiere ID Governance o Entra Suite. [Fuente](https://learn.microsoft.com/en-us/entra/identity/multi-tenant-organizations/cross-tenant-synchronization-configure) · Repasa [M4](02_Nivel_2_Intermedio.md#m4)

**11. Una empresa con dirección de facturación en México, ¿puede usar App governance?**

- a) Sí, con Microsoft 365 E5
- b) No: México está entre los países excluidos  ✅
- c) Sí, con Purview Suite
- d) Solo en vista previa

*Respuesta: b).* App governance no está disponible si la dirección de facturación está en México, Singapur, Polonia, Italia, Qatar, Israel, España o Taiwán. [Fuente](https://learn.microsoft.com/en-us/defender-cloud-apps/app-governance-get-started) · Repasa [M5](02_Nivel_2_Intermedio.md#m5)

**12. Desde junio de 2026, el bloqueo de propiedades de instancia:**

- a) Está retirado
- b) Solo aplica a apps SAML
- c) Requiere Workload ID Premium
- d) Viene habilitado por defecto en apps nuevas, single-tenant y multitenant  ✅

*Respuesta: d).* El bloqueo viene habilitado por defecto en las apps nuevas desde junio de 2026 y ya no se limita a las apps multitenant. [Fuente](https://learn.microsoft.com/en-us/entra/identity-platform/howto-configure-app-instance-property-locks) · Repasa [M5](02_Nivel_2_Intermedio.md#m5)

**13. ¿Qué se necesita para recibir las alertas de monitoreo de salud de Entra?**

- a) P1 o P2 que no sea de prueba y al menos 100 usuarios activos al mes  ✅
- b) Solo la edición gratuita
- c) Microsoft Sentinel
- d) ID Governance

*Respuesta: a).* Las alertas de salud, en vista previa, exigen P1 o P2 que no sean de prueba y al menos 100 usuarios activos al mes; un tenant nuevo tarda unos 30 días en generarlas. [Fuente](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-investigate-health-scenario-alerts) · Repasa [M6](02_Nivel_2_Intermedio.md#m6)

**14. ¿Cuál es un requisito de Platform SSO para macOS?**

- a) Windows Hello for Business
- b) AD FS
- c) Workload ID Premium
- d) Company Portal 5.2404.0 o posterior  ✅

*Respuesta: d).* Platform SSO requiere macOS 13 o superior (se recomienda 14) y Company Portal 5.2404.0 o posterior, y se configura con el catálogo de Intune. [Fuente](https://learn.microsoft.com/en-us/entra/identity/devices/macos-psso) · Repasa [M7](02_Nivel_2_Intermedio.md#m7)

**15. ¿En qué orden evalúa el cliente de Global Secure Access los perfiles de reenvío?**

- a) Microsoft, Private Access, Internet Access  ✅
- b) Internet Access, Private Access, Microsoft
- c) Private Access, Microsoft, Internet Access
- d) Todos en paralelo

*Respuesta: a).* El orden es perfil de tráfico de Microsoft, luego Private Access y luego Internet Access; el perfil de sistema de tráfico de Entra se activa con cualquiera de ellos. [Fuente](https://learn.microsoft.com/en-us/entra/global-secure-access/concept-traffic-forwarding) · Repasa [M8](02_Nivel_2_Intermedio.md#m8)

<a id="eval-avanzado"></a>

## Nivel 3 · Avanzado · Cargas de trabajo, amenazas y arquitectura

**1. ¿Cómo se licencia Workload ID Premium?**

- a) Incluido en Microsoft 365 E5
- b) Incluido en Entra ID P2
- c) SKU independiente de 3 USD por identidad al mes  ✅
- d) Gratis para las identidades administradas

*Respuesta: c).* Es un SKU independiente, no incluido en E5, E7 ni en otros planes; las identidades administradas ni siquiera entran en el alcance de su acceso condicional. [Fuente](https://learn.microsoft.com/en-us/entra/workload-id/workload-identities-faqs) · Repasa [A1](03_Nivel_3_Avanzado.md#a1)

**2. ¿A qué se aplica el acceso condicional para workload identities?**

- a) A identidades administradas
- b) A service principals de un solo tenant asignados directamente a la política  ✅
- c) A apps SaaS multitenant
- d) A grupos que contienen service principals

*Respuesta: b).* Solo cubre service principals de un solo tenant registrados en tu tenant; si la política apunta a un grupo que los contiene, no se aplica. [Fuente](https://learn.microsoft.com/en-us/entra/identity/conditional-access/workload-identity) · Repasa [A1](03_Nivel_3_Avanzado.md#a1)

**3. ¿Qué vida máxima para certificados de aplicación recomienda el tutorial de políticas de administración de apps?**

- a) 180 días  ✅
- b) 30 días
- c) 90 días
- d) 2 años

*Respuesta: a).* La recomendación es deshabilitar secretos y limitar los certificados a 180 días, con rotación automática en Key Vault. [Fuente](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/tutorial-enforce-secret-standards) · Repasa [A1](03_Nivel_3_Avanzado.md#a1)

**4. ¿En qué condiciones funciona CAE para workload identities?**

- a) Contra cualquier recurso y sin licencia
- b) Solo con identidades administradas
- c) Solo en apps multitenant
- d) Contra Microsoft Graph, si la app declara la capacidad cp1 y con Workload ID Premium  ✅

*Respuesta: d).* CAE para workload identities revoca casi en tiempo real tokens de hasta 24 horas, pero solo contra Microsoft Graph, con apps que declaran cp1 y con Workload ID Premium. [Fuente](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-continuous-access-evaluation-workload) · Repasa [A1](03_Nivel_3_Avanzado.md#a1)

**5. ¿Cuál es la latencia máxima típica de CAE ante eventos críticos, como deshabilitar una cuenta?**

- a) Instantánea
- b) 1 hora
- c) 24 horas
- d) Hasta 15 minutos  ✅

*Respuesta: d).* Los eventos críticos se aplican en hasta 15 minutos; los cambios de ubicación IP, al instante en los servicios compatibles. [Fuente](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-continuous-access-evaluation) · Repasa [A2](03_Nivel_3_Avanzado.md#a2)

**6. La interrupción automática de ataques de Defender deshabilita usuarios en Entra ID y AD cuando la confianza es de al menos:**

- a) 50 %
- b) 75 %
- c) 99 %  ✅
- d) 100 %, con aprobación manual

*Respuesta: c).* Actúa con una confianza de al menos 99 % y ya soporta Okta y AWS en vista previa. [Fuente](https://learn.microsoft.com/en-us/defender-xdr/automatic-attack-disruption) · Repasa [A2](03_Nivel_3_Avanzado.md#a2)

**7. ¿Qué tabla de la búsqueda avanzada reemplazó a AADSignInEventsBeta el 19 de octubre de 2026?**

- a) IdentityLogonEvents
- b) EntraIdSignInEvents  ✅
- c) SigninLogs
- d) AgentsInfo

*Respuesta: b).* EntraIdSignInEvents reemplazó a AADSignInEventsBeta y requiere Entra ID P2. [Fuente](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-entraidsigninevents-table) · Repasa [A2](03_Nivel_3_Avanzado.md#a2)

**8. ¿Cuál es el estado de EntraExporter en noviembre de 2026?**

- a) En disponibilidad general
- b) En vista previa
- c) Integrado en Entra PowerShell
- d) Archivado desde el 22 de octubre de 2026  ✅

*Respuesta: d).* El repositorio quedó archivado; para instantáneas y deriva se usan Tenant Governance o Microsoft365DSC. [Fuente](https://github.com/microsoft/EntraExporter/blob/main/README.md) · Repasa [A3](03_Nivel_3_Avanzado.md#a3)

**9. ¿Qué versión de Maester conviene fijar en un pipeline en noviembre de 2026?**

- a) La 2.3.0, porque la 3.0 está en vista previa  ✅
- b) La 3.0, porque es la única compatible
- c) La 1.0
- d) Siempre la última disponible

*Respuesta: a).* Maester 3.0 está en vista previa y rompe compatibilidad; la recomendación es fijar la 2.3.0 hasta que la 3.0 sea estable. [Fuente](https://maester.dev/blog/maester-3-0) · Repasa [A3](03_Nivel_3_Avanzado.md#a3)

**10. ¿Qué incluye Tenant Governance con licencias P1 o P2?**

- a) Monitoreo ilimitado
- b) Hasta 30 monitores y 800 recursos por día  ✅
- c) Solo instantáneas manuales
- d) Nada: requiere ID Governance

*Respuesta: b).* Con P1 o P2 hay hasta 30 monitores y 800 recursos por día, y 20.000 recursos al mes en instantáneas; ID Governance amplía los límites. [Fuente](https://learn.microsoft.com/en-us/entra/id-governance/tenant-governance/licensing) · Repasa [A3](03_Nivel_3_Avanzado.md#a3)

**11. En el modelo de acceso empresarial, ¿en qué se convierte el antiguo Tier 0?**

- a) En el plano de datos y cargas de trabajo
- b) En el acceso de usuarios
- c) En el plano de control  ✅
- d) En el plano de aplicaciones

*Respuesta: c).* El Tier 0 pasa a ser el plano de control; el Tier 1 se divide en plano de administración y de datos y cargas, y el Tier 2 en acceso de usuarios y de aplicaciones. [Fuente](https://learn.microsoft.com/en-us/security/privileged-access-workstations/privileged-access-access-model) · Repasa [A4](03_Nivel_3_Avanzado.md#a4)

**12. ¿Qué NO puede hacer Entra Backup and Recovery?**

- a) Restaurar una política de acceso condicional modificada
- b) Generar un informe de diferencias
- c) Recuperar objetos por tipo o por ID
- d) Recuperar objetos eliminados definitivamente  ✅

*Respuesta: d).* No recupera objetos eliminados definitivamente ni los que tienen su origen de autoridad en AD local; por eso conviene proteger el borrado definitivo con acciones protegidas. [Fuente](https://learn.microsoft.com/en-us/entra/backup/overview) · Repasa [A5](03_Nivel_3_Avanzado.md#a5)

**13. Ante una cuenta híbrida comprometida, ¿qué combinación recomienda Microsoft?**

- a) Deshabilitarla, restablecer la contraseña dos veces en AD, revocar los tokens de actualización y deshabilitar sus dispositivos  ✅
- b) Solo borrar la cuenta
- c) Esperar a que expire el token de acceso
- d) Cambiarle la licencia

*Respuesta: a).* La revocación de emergencia combina varias acciones; recuerda además que Entra ID no revoca las cookies de sesión de las aplicaciones. [Fuente](https://learn.microsoft.com/en-us/entra/identity/users/users-revoke-access) · Repasa [A5](03_Nivel_3_Avanzado.md#a5)

**14. ¿Dónde viven ahora los playbooks de respuesta a incidentes de Microsoft?**

- a) En el Ninja de Defender XDR
- b) En la disciplina SecOps del Security Adoption Framework  ✅
- c) En la página de licencias de Entra
- d) Solo en GitHub

*Respuesta: b).* Pasaron a las rutas security/zero-trust/security-operations-playbook-* de la disciplina SecOps del Security Adoption Framework. [Fuente](https://learn.microsoft.com/en-us/security/zero-trust/security-operations-playbook-password-spray) · Repasa [A5](03_Nivel_3_Avanzado.md#a5)

<a id="eval-agentes"></a>

## Nivel 4 · Identidad para agentes de IA · Preparar el tenant para agentes

**1. ¿Cuándo anunció Microsoft Entra Agent ID?**

- a) 18 de noviembre de 2025
- b) 19 de mayo de 2025  ✅
- c) 1 de mayo de 2026
- d) 14 de julio de 2025

*Respuesta: b).* Se anunció el 19 de mayo de 2025; en Ignite 2025 llegaron Agent 365 y el acceso condicional para agentes en vista previa, y la GA llegó en mayo de 2026. [Fuente](https://learn.microsoft.com/en-us/security/security-for-ai/whats-new) · Repasa [X1](04_Nivel_4_Identidad_para_agentes_de_IA.md#x1)

**2. Sin una política de acceso condicional «bloquear salvo aprobado», las solicitudes de token de un agente…**

- a) Se permiten por defecto  ✅
- b) Se bloquean por defecto
- c) Requieren la aprobación del sponsor
- d) Requieren MFA del agente

*Respuesta: a).* El pilar de IA del Zero Trust Assessment advierte que, sin esa política, toda solicitud de token de un agente se permite por defecto. [Fuente](https://learn.microsoft.com/en-us/security/zero-trust/assessment/ai-pillar) · Repasa [X1](04_Nivel_4_Identidad_para_agentes_de_IA.md#x1)

**3. ¿Dónde residen las credenciales de una identidad de agente?**

- a) En la identidad de agente
- b) En la cuenta de usuario del agente
- c) En el blueprint  ✅
- d) En Key Vault, automáticamente

*Respuesta: c).* La identidad de agente no tiene credenciales propias: se autentica con las del blueprint (credenciales federadas, certificados o secretos). [Fuente](https://learn.microsoft.com/en-us/entra/agent-id/agent-identities) · Repasa [X2](04_Nivel_4_Identidad_para_agentes_de_IA.md#x2)

**4. ¿Qué relación administrativa es obligatoria en Agent ID?**

- a) Owner
- b) Manager
- c) Ninguna
- d) Sponsor  ✅

*Respuesta: d).* Cada identidad de agente y cada blueprint necesitan al menos un sponsor, responsable de negocio; los owners son opcionales. [Fuente](https://learn.microsoft.com/en-us/entra/agent-id/agent-owners-sponsors-managers) · Repasa [X2](04_Nivel_4_Identidad_para_agentes_de_IA.md#x2)

**5. ¿Cuál de estos roles impide Entra asignar a una identidad de agente?**

- a) Privileged Role Administrator  ✅
- b) Ninguno: los agentes pueden recibir cualquier rol
- c) Solo los roles de Azure RBAC
- d) Solo los roles personalizados

*Respuesta: a).* Las salvaguardas impiden asignar a agentes roles como Global Administrator, Privileged Role Administrator o User Administrator, y que pertenezcan a grupos asignables a roles. [Fuente](https://learn.microsoft.com/en-us/entra/agent-id/authorization-agent-id) · Repasa [X2](04_Nivel_4_Identidad_para_agentes_de_IA.md#x2)

**6. Un agente actúa en nombre de un usuario (OBO). ¿A qué apunta la política de acceso condicional?**

- a) A la identidad de agente
- b) Al blueprint
- c) A los usuarios y grupos  ✅
- d) A la cuenta de usuario del agente

*Respuesta: c).* En OBO el sujeto del token es el usuario; en modo autónomo es la identidad de agente o su blueprint, y con cuenta de usuario del agente, «Agent Users». [Fuente](https://learn.microsoft.com/en-us/entra/identity/conditional-access/agent-id) · Repasa [X3](04_Nivel_4_Identidad_para_agentes_de_IA.md#x3)

**7. ¿En cuál de estos casos NO protege el acceso condicional a un agente?**

- a) Cuando actúa de forma autónoma con su identidad
- b) Cuando accede a un recurso con una clave de API  ✅
- c) Cuando actúa en nombre de un usuario
- d) Cuando el tenant tiene Microsoft 365 E7

*Respuesta: b).* El acceso condicional no protege los recursos a los que se accede con claves de API, y tampoco se aplica si los valores predeterminados de seguridad están activos. [Fuente](https://learn.microsoft.com/en-us/entra/identity/conditional-access/agent-id) · Repasa [X3](04_Nivel_4_Identidad_para_agentes_de_IA.md#x3)

**8. Al proteger un servidor MCP con Entra ID, ¿qué paso se omite con más frecuencia?**

- a) Habilitar MFA para el servidor
- b) Crear un secreto de cliente
- c) Configurar requestedAccessTokenVersion en 2  ✅
- d) Desactivar el acceso condicional

*Respuesta: c).* Sin tokens v2 no se puede usar la URL del servidor como Application ID URI; además hay que publicar los metadatos RFC 9728 y validar con librerías probadas. [Fuente](https://learn.microsoft.com/en-us/entra/agent-id/secure-mcp-server-with-entra-id) · Repasa [X3](04_Nivel_4_Identidad_para_agentes_de_IA.md#x3)

**9. ¿Cuándo llegó Agent 365 a disponibilidad general y a qué precio independiente?**

- a) 18 de noviembre de 2025, 30 USD por usuario
- b) 14 de julio de 2025, incluido en E5
- c) Enero de 2026, por agente
- d) 1 de mayo de 2026, 15 USD por usuario al mes o incluido en E7  ✅

*Respuesta: d).* Agent 365 y Microsoft 365 E7 llegaron a GA el 1 de mayo de 2026; por separado, Agent 365 cuesta 15 USD por usuario al mes. [Fuente](https://techcommunity.microsoft.com/blog/microsoft_365blog/microsoft-365-e7-and-agent-365-are-now-generally-available/4516295) · Repasa [X4](04_Nivel_4_Identidad_para_agentes_de_IA.md#x4)

**10. ¿Qué necesitas para ver el inventario completo de agentes en el centro de administración de Microsoft 365?**

- a) Una licencia de Agent 365
- b) Solo el rol AI Reader o AI Administrator  ✅
- c) Global Administrator y E7
- d) Entra ID P2

*Respuesta: b).* Ver el inventario no requiere licencia; aplicar acceso condicional o gobernanza a los agentes, sí. [Fuente](https://learn.microsoft.com/en-us/entra/agent-id/agent-registry-convergence) · Repasa [X4](04_Nivel_4_Identidad_para_agentes_de_IA.md#x4)

**11. ¿Qué tabla de Defender reemplazó a AIAgentsInfo?**

- a) AgentsInfo  ✅
- b) IdentityInfo
- c) EntraIdSignInEvents
- d) CloudAppEvents

*Respuesta: a).* AgentsInfo reemplazó a AIAgentsInfo, que siguió accesible hasta el 1 de julio de 2026: hay que migrar las consultas. [Fuente](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-agentsinfo-table) · Repasa [X4](04_Nivel_4_Identidad_para_agentes_de_IA.md#x4)

**12. ¿Qué requiere el agente de optimización de acceso condicional?**

- a) Entra ID P2 y Microsoft 365 E7
- b) Agent 365
- c) Nada adicional
- d) Entra ID P1 y SCU disponibles  ✅

*Respuesta: d).* Requiere P1 y SCU de Security Copilot; por defecto no crea políticas y, si se lo autorizas, las crea en solo informe. [Fuente](https://learn.microsoft.com/en-us/entra/security-copilot/conditional-access-agent-optimization) · Repasa [X5](04_Nivel_4_Identidad_para_agentes_de_IA.md#x5)

**13. ¿Quién puede emitir tokens con el Agent ID de un agente de Copilot Studio?**

- a) El Global Administrator
- b) El maker que creó el agente
- c) Cualquier Application Administrator
- d) Nadie del tenant: lo gestiona un blueprint de Microsoft con credenciales federadas  ✅

*Respuesta: d).* La identidad la gestiona un blueprint propiedad de Microsoft con credenciales federadas; nadie del tenant, ni siquiera un administrador, puede emitir tokens con ella. [Fuente](https://learn.microsoft.com/en-us/microsoft-copilot-studio/govern-agents-identities-overview) · Repasa [X6](04_Nivel_4_Identidad_para_agentes_de_IA.md#x6)

**14. En Microsoft Foundry, ¿qué permisos recibe una identidad de agente recién creada?**

- a) Contributor sobre la suscripción
- b) Ninguno: hay que concederlos con Azure RBAC de mínimo privilegio  ✅
- c) Los permisos de quien la creó
- d) Los de un secreto de cliente compartido

*Respuesta: b).* Foundry crea el blueprint y la identidad con credencial federada, pero no asigna permisos de Azure RBAC automáticamente. [Fuente](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/agent-identity) · Repasa [X6](04_Nivel_4_Identidad_para_agentes_de_IA.md#x6)

**15. ¿Qué cubre el pilar de IA del Zero Trust Workshop, guion del proyecto integrador?**

- a) Solo las licencias de Copilot
- b) Solo la configuración de Copilot Studio
- c) Mapear el riesgo de IA, registrar agentes, asegurar autenticación, red y datos, construir agentes seguros y detectar y responder  ✅
- d) Solo el entrenamiento de modelos

*Respuesta: c).* Es el guion del proyecto integrador y se complementa con las verificaciones automáticas del pilar de IA del Zero Trust Assessment. [Fuente](https://learn.microsoft.com/en-us/security/zero-trust/workshop-zero-trust-ai-security) · Repasa [X7](04_Nivel_4_Identidad_para_agentes_de_IA.md#x7)

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

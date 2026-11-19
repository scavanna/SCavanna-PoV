# Cierre, glosario y fuentes

*Microsoft Entra Ninja Training: identidad y acceso para la era de los agentes de IA · Edición 2026*

[← Laboratorio y práctica en producción](07_Laboratorio_y_practica_en_produccion.md) · [Índice del programa](README.md)

<a id="cierre"></a>

## ¿Y ahora?

Ser Ninja no es un estado, es un hábito. Entra publica novedades cada mes y 2027 trae fechas que no se pueden perder —el fin de SMS y voz entregados por Microsoft y la actualización obligatoria de Connect Sync—. Dedica media hora por semana a la rutina de [C3](05_Comunidad.md#c3), vuelve a esta guía cuando un cambio afecte a tu operación y repasa las tablas de [licencias](00_Programa.md#licencias) y de [preparación para agentes](00_Programa.md#preparacion-agentes) después de Ignite y de los webinars de profundización de Entra del 15 al 17 de diciembre de 2026.

Próximos pasos: el examen SC-300 y la credencial Applied Skills de identidades y acceso; el programa de **Defender XDR** para operar ITDR desde el SOC; el de **Sentinel** para los datos y las detecciones de identidad; el de **Security Copilot** para el parque de agentes de seguridad; y el de **Purview DSPM** para los datos que usan los agentes. Si encuentras un enlace roto o un dato desactualizado, regístralo y compártelo con tu equipo: la guía está pensada para revisarse después de cada Ignite, como los Ninja oficiales.

<a id="glosario"></a>

## Glosario

| Término | Definición |
|---|---|
| Acción protegida | Permiso sensible de Entra (editar el acceso condicional, el acceso entre tenants o las ubicaciones con nombre, o borrar de forma definitiva) que exige cumplir una política de acceso condicional mediante un contexto de autenticación. |
| Agent 365 | Plano de control de Microsoft para observar, gobernar y proteger agentes; GA el 1 de mayo de 2026, incluido en Microsoft 365 E7 o como complemento por usuario. |
| AiTM | Adversario en el medio: phishing con un proxy que roba la cookie de sesión después del MFA; se mitiga con credenciales resistentes al phishing y con protección de la sesión. |
| Blueprint de identidad de agente | Plantilla y contenedor de credenciales de un tipo de agente; sus permisos se heredan en todas sus identidades de agente. |
| CAE | Continuous access evaluation: evaluación continua que revoca sesiones casi en tiempo real ante eventos críticos (hasta 15 minutos) y aplica al instante los cambios de ubicación en servicios compatibles. |
| Contexto de autenticación | Etiqueta (C1 a C99) que una aplicación, PIM o una acción protegida solicitan para exigir una política de acceso condicional más estricta. |
| Cuenta de emergencia | Cuenta solo en la nube con Global Administrator, protegida con passkey FIDO2 o CBA, excluida de las políticas que bloquean y monitoreada; se recomiendan al menos dos. |
| Entra Agent ID | Marco de identidad y seguridad de Entra para agentes de IA: blueprints, identidades de agente y usuarios de agente. |
| Entra Suite | Paquete de Private Access, Internet Access, ID Governance, ID Protection y Verified ID premium; se vende aparte (requiere P1) o viene en Microsoft 365 E7. |
| Fortaleza de autenticación | Control de acceso condicional que define qué combinaciones de métodos se aceptan: MFA, MFA sin contraseña, MFA resistente al phishing o una personalizada. |
| Global Secure Access | Servicio de borde de seguridad (SSE) de Microsoft: perfil de tráfico de Microsoft, Private Access e Internet Access. |
| Identidad administrada | Service principal especial cuyas credenciales gestiona Azure; puede estar asignada por el sistema o por el usuario. |
| Identidad de agente | Service principal especial, de un solo tenant y sin credenciales propias, que representa a un agente de IA. |
| ITDR | Identity threat detection and response: disciplina de detectar y responder a ataques contra identidades en Active Directory y en la nube. |
| MCP | Model Context Protocol: estándar abierto para que los agentes descubran y usen herramientas; Entra puede actuar como su servidor de autorización. |
| OBO | On-behalf-of: flujo en el que un agente o una API actúa en nombre de un usuario; el sujeto del token es el usuario. |
| PAW | Estación de trabajo de acceso privilegiado: dispositivo aislado y endurecido, reservado para tareas administrativas. |
| Passkey | Credencial FIDO2 resistente al phishing; puede estar vinculada al dispositivo (llave de seguridad o Authenticator) o sincronizada entre los dispositivos del usuario. |
| PHS | Sincronización de hash de contraseñas: el método de autenticación híbrida más simple y resiliente, necesario para detectar credenciales filtradas. |
| PIM | Privileged Identity Management: asignaciones elegibles y activación de roles justo a tiempo, con aprobación, MFA y auditoría. |
| PRT | Primary Refresh Token: artefacto de inicio de sesión único en Windows, macOS, iOS, Android y Linux que transporta las reclamaciones del dispositivo. |
| RMAU | Unidad administrativa de administración restringida: solo los administradores con ámbito en ella pueden modificar sus objetos. |
| SCU | Security Compute Unit: unidad de capacidad de Security Copilot. |
| Sponsor | Persona responsable de negocio de un blueprint o de una identidad de agente; es obligatoria en Agent ID. |
| TAP | Temporary Access Pass: código temporal para el arranque y la recuperación de credenciales; solo cuenta como MFA. |
| Tenant Governance | Capacidad de Entra (GA el 10 de agosto de 2026) para líneas base, deriva de configuración, instantáneas y relaciones de administración delegada entre tenants. |
| Usuario de agente | Cuenta de usuario opcional, 1:1 con una identidad de agente, para escenarios con buzón o Teams; solo en tenants del programa Frontier. |
| Workload ID Premium | SKU de 3 USD por identidad al mes para acceso condicional, ID Protection y CAE de workload identities; no está incluido en E5 ni en E7. |
| Workload identity federation | Confianza en tokens de un proveedor externo (GitHub, Kubernetes, AWS, Google Cloud) para eliminar los secretos de apps e identidades administradas. |
| Zero Trust Assessment | Herramienta de solo lectura que evalúa el tenant en siete pilares, incluido el de IA; proyecto comunitario mantenido por empleados de Microsoft. |

<a id="metodologia"></a>

## Metodología y fuentes

Esta guía se construyó con líneas de investigación en paralelo sobre fuentes públicas: la forma y la historia del Ninja oficial, cada nivel técnico, la operación y la comunidad. Cada enlace se registró solo si apareció literalmente en un resultado de búsqueda o en una página leída, y luego se consolidó, se depuró y se verificó. Se descartaron recursos retirados, alojados en espacios no públicos o duplicados. Fecha de corte: 6 de noviembre de 2026.

Puntos a confirmar en fuentes oficiales antes de recomendarlos:

- **No hay Ninja oficial de Entra.** La [etiqueta ninja training](https://techcommunity.microsoft.com/tag/ninja%20training) y los rastreadores comunitarios no muestran uno al 6 de noviembre de 2026. El certificado de participación al 80 % de la familia Ninja se describe en resúmenes comunitarios ([MS Cloud Explorers](https://mscloudexplorers.com/learn/)) y no se reverificó en una fuente oficial.
- **Ponderación del SC-300.** La misma [guía de estudio](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-300) asigna 25–30 % al dominio «Implement authentication and access management» en el resumen y 20–25 % en el detalle.
- **Retiro de SMS y voz.** El [blog del 13 de julio de 2026](https://www.microsoft.com/en-us/security/blog/2026/07/13/microsoft-entra-id-security-updates-passkeys-are-the-default-authentication-method-in-entra-id/) fija una sola fecha (1 de febrero de 2027, sin opt-out); el [documento de Learn](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sms-voice-retirement) y el aviso [MC1426371](https://mc.merill.net/message/MC1426371) (actualizado el 15 de septiembre de 2026) agregan el 1 de julio de 2027 para Global Administrators activos y usuarios externos y una exclusión temporal de la habilitación automática. Esta guía usa la versión más reciente; según la [FAQ](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sms-voice-retirement-faq), un Global Administrator solo elegible en PIM sigue la fecha de febrero.
- **Licencia de las políticas administradas.** Su [página](https://learn.microsoft.com/en-us/entra/identity/conditional-access/managed-policies) pide «P2 o Business Premium» como requisito, mientras la [página de licencias](https://learn.microsoft.com/en-us/entra/fundamentals/licensing) indica que el acceso condicional requiere P1.
- **Protección de tokens en Apple.** La tabla de plataformas de la [página de protección de tokens](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-token-protection) marca iOS/iPadOS y macOS como GA, pero su sección de dispositivos aún dice «Apple (Preview)» y la versión en español sigue en vista previa.
- **Fecha límite de Connect Sync.** Avisos anteriores exigían la versión 2.5.79.0 antes del 30 de septiembre de 2026; el aviso vigente exige 2.6.84.0 con autenticación basada en aplicación antes del 7 de abril de 2027 ([historial de versiones](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/reference-connect-version-history)).
- **Credencial de plataforma de macOS.** La [guía de prerrequisitos passwordless](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-plan-prerequisites-phishing-resistant-passwordless-authentication) la etiqueta «(preview)» mientras Platform SSO se documenta como soportado: verifica el estado en tu tenant.
- **Applied Skills.** La evaluación [APL-0501](https://learn.microsoft.com/en-us/credentials/applied-skills/resources/study-guides/apl-0501) aún evalúa el MFA por usuario heredado, aunque Microsoft recomienda convertirlo a acceso condicional.
- **Nombre comercial en la guía de Global Secure Access.** La [guía del perfil de tráfico de Microsoft](https://learn.microsoft.com/en-us/entra/architecture/gsa-deployment-guide-microsoft-traffic) menciona «Microsoft Entra Secure Access Essentials», un nombre que no aparece en la página de licencias.
- **Estado del Zero Trust Assessment.** A veces se lo presenta como un módulo de Microsoft, pero su [README](https://github.com/microsoft/zerotrustassessment) aclara que es un proyecto comunitario mantenido por empleados, sin soporte oficial; un resultado de búsqueda antiguo lo mostraba como archivado, pero el repositorio verificado está activo.
- **Rol de Merill Fernando.** Su [sitio personal](https://merill.net/about/) indica que dejó Microsoft en 2026 para fundar Jozra; la [página «About» de Entra.News](https://entra.news/about) y la de autores de Maester aún lo presentan como gerente de producto de Microsoft.
- **Historial de Backup and Recovery.** Learn indica 7 días ([visión general](https://learn.microsoft.com/en-us/entra/backup/overview)) y la [API de Graph](https://learn.microsoft.com/en-us/graph/api/resources/entrarecoveryservices-backup-recovery-overview?view=graph-rest-1.0) 5 días: planifica con el valor menor.
- **PIM for Groups.** Un [sitio de asesoría de licencias](https://microsoftnegotiations.com/blog/microsoft-identity-governance-licensing) afirma que requiere ID Governance; la [documentación oficial](https://learn.microsoft.com/en-us/entra/id-governance/licensing-fundamentals) lo incluye en P2. Esta guía sigue la oficial.
- **Bloqueo de propiedades de instancia.** Versiones anteriores de la [guía](https://learn.microsoft.com/en-us/entra/identity-platform/howto-configure-app-instance-property-locks) decían que aplicaba solo a apps multitenant o creadas en el portal; la vigente (2 de octubre de 2026) lo aplica a single-tenant y multitenant.
- **Tenant Governance.** Según fuentes comunitarias, sus APIs de Graph seguían en beta y el descubrimiento de tenants relacionados es una acción de un solo sentido ([anuncio de GA](https://techcommunity.microsoft.com/blog/microsoft-entra-blog/microsoft-entra-tenant-governance-is-now-generally-available/4543638), [transición desde Microsoft365DSC](https://github.com/Microsoft365DSC/Microsoft365DSC/blob/Dev/docs/docs/blog/2026/utcm-transition/utcm-transition.md)): pruébalo primero sobre recursos no críticos.
- **Fecha de Agent ID en Copilot Studio.** La [página en inglés](https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-use-entra-agent-identities) dice mayo de 2026; [versiones localizadas anteriores](https://learn.microsoft.com/bs-latn-ba/microsoft-copilot-studio/admin-use-entra-agent-identities) dicen julio de 2026 y que desde entonces no hay opt-out.
- **Licencia de ID Protection para agentes.** «Pronto requerirá Agent 365» ([riesgo de agentes](https://learn.microsoft.com/en-us/entra/id-protection/concept-risky-agents)) frente a «Entra ID P2 durante la vista previa» ([administración de agentes](https://learn.microsoft.com/es-es/entra/agent-id/manage-agent-identities-admin)) frente a la [descripción de servicio de Agent 365](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-agent-365/microsoft-agent-365), que la ubica en E7 o Agent 365.
- **Licencia del Identity Risk Management Agent.** Su [página](https://learn.microsoft.com/en-us/entra/id-protection/identity-risk-management-agent-get-started) pide Entra ID P2; el [catálogo de agentes de Entra](https://learn.microsoft.com/en-us/entra/security-copilot/entra-agents) indica «Microsoft Entra Agent ID».
- **Licencia del acceso condicional para agentes.** Una versión anterior de la [página](https://learn.microsoft.com/en-us/entra/identity/conditional-access/agent-id) pedía P1 o P2 más Agent 365 por usuario, con un «enforcement coming soon»; la vigente (30 de septiembre de 2026) pide E7, o Agent 365 más P1 o E3.
- **Agente de optimización de acceso condicional.** La misma página de [configuración](https://learn.microsoft.com/en-us/entra/security-copilot/conditional-access-agent-optimization-settings) dice que las ejecuciones por actividad ocurren como máximo cada seis horas y luego describe un enfriamiento de cuatro horas.
- **Páginas localizadas desactualizadas.** La versión eu-es de [gobernanza de identidades de agente](https://learn.microsoft.com/eu-es/entra/id-governance/agent-id-governance-overview) aún dice vista previa o Frontier, y varias páginas en español de Agent ID, MCP, Foundry y Copilot Studio son traducciones automáticas: prevalece la versión en inglés.
- **Licenciamiento de Workload ID Premium.** La [FAQ](https://learn.microsoft.com/en-us/entra/workload-id/workload-identities-faqs) dice que hay que licenciar cada identidad elegible y, a la vez, que una licencia en el tenant desbloquea las funciones para todas: distingue la habilitación técnica del cumplimiento contractual y confírmalo con tu equipo de cuenta.
- **Fecha de EntraIdSignInEvents.** Versiones localizadas antiguas daban el 9 de diciembre de 2025 para el reemplazo de AADSignInEventsBeta; la versión en inglés vigente dice 19 de octubre de 2026 ([tabla](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-entraidsigninevents-table)).
- **App governance en MCSA.** No está disponible si la dirección de facturación está en México (ni en Singapur, Polonia, Italia, Qatar, Israel, España o Taiwán), según la [guía de activación](https://learn.microsoft.com/en-us/defender-cloud-apps/app-governance-get-started) y la [FAQ](https://learn.microsoft.com/en-us/defender-cloud-apps/app-governance-faq); confirma con tu equipo de cuenta la situación de cada país de la región.
- **Infraestructura como código.** La investigación no verificó guías oficiales vigentes de Terraform o Bicep para Entra; el módulo [A3](03_Nivel_3_Avanzado.md#a3) se apoya en Microsoft Graph, Tenant Governance, Microsoft365DSC y Maester. Tampoco encontró libros sobre Entra actualizados a 2026.
- **Estados por confirmar tras Ignite.** Microsoft Ignite (17 al 20 de noviembre de 2026) puede cambiar estados de vista previa y licencias de Agent 365, ID Protection para agentes, CAE universal, Hard Deletion Protection y las alertas de salud. El [laboratorio 3B](https://github.com/MicrosoftLearning/mslearn-sec-identity/blob/master/Instructions/Labs/Supplemental_Lab-3B-Secure-Entra-AgentID.md) es un trabajo en curso con pasos válidos al 30 de junio de 2026, y el [TechLab de Entra Suite](https://github.com/microsoft/TechLab-Entra-Suite-for-Frontier-Transformation/) está pensado para un formato interno: úsalo como guion en tu tenant de prueba.

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

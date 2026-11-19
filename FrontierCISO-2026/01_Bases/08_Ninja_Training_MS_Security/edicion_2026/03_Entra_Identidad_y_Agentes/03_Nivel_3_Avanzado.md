# Nivel 3 · Avanzado · Cargas de trabajo, amenazas y arquitectura

*Microsoft Entra Ninja Training: identidad y acceso para la era de los agentes de IA · Edición 2026*

[← Nivel 2 · Intermedio](02_Nivel_2_Intermedio.md) · [Índice del programa](README.md) · [Nivel 4 · Identidad para agentes de IA →](04_Nivel_4_Identidad_para_agentes_de_IA.md)

<a id="avanzado"></a>

Identidades de carga de trabajo, detección y respuesta a amenazas de identidad, automatización e identidad como código, arquitectura de acceso privilegiado y respuesta a incidentes. Terminas con controles versionados, un modelo de acceso empresarial y playbooks ensayados.

*L400 · 5 módulos · ~50 horas · 54 recursos*

**Módulos de este nivel:** [A1 Identidades de carga](#a1) · [A2 ITDR](#a2) · [A3 Identidad como código](#a3) · [A4 Arquitectura y privilegios](#a4) · [A5 Respuesta a incidentes](#a5)

<a id="a1"></a>

## A1 · Identidades de carga de trabajo: service principals, identidades administradas y federación

*L400 · ~8 h · Origen: SC-300 · Plan and implement workload identities*

Las **identidades de carga de trabajo** —aplicaciones, service principals e identidades administradas— ya superan en número a las personas en muchos tenants, y no tienen MFA. Una **identidad administrada** es un service principal especial cuyas credenciales gestiona Azure: la asignada por el sistema vive y muere con su recurso y sirve para auditar qué recurso actuó; la asignada por el usuario se reutiliza en más escenarios. Las identidades del sistema eliminadas siguen contando contra el límite hasta purgarse a los 30 días.

La higiene de credenciales es el primer control: Microsoft recomienda deshabilitar secretos de cliente y claves simétricas y limitar los certificados a **180 días** con rotación automática en Key Vault, aplicándolo con políticas de administración de apps. Mejor aún, eliminar el secreto con **federación de identidades de carga de trabajo**: GitHub Actions, Kubernetes, Google Cloud, AWS o SPIFFE presentan su propio token y Entra confía en él. Las credenciales federadas flexibles, en vista previa, admiten expresiones de coincidencia de reclamaciones.

**Workload ID Premium** —SKU independiente de 3 USD por identidad al mes, no incluido en E5 ni en E7— agrega acceso condicional, ID Protection completo y CAE para workload identities, revisiones de acceso de service principals privilegiados y recomendaciones de salud de apps. Crear identidades, usar identidades administradas, la federación, los registros y las políticas de apps son gratuitos. Este módulo es la base del track de agentes: una identidad de agente es un service principal especial ([X2](04_Nivel_4_Identidad_para_agentes_de_IA.md#x2)).

**Por qué importa**

Las credenciales de apps filtradas en repositorios o pipelines son una de las vías más rápidas hacia el tenant. Eliminar secretos con federación e identidades administradas quita la credencial que se puede robar, y las políticas de apps impiden que vuelvan. Métricas: service principals con secretos, credenciales que vencen en 30 días y pipelines con federación.

**Qué vas a lograr**

- Inventariar service principals, identidades administradas y sus credenciales con Microsoft Graph PowerShell.
- Aplicar políticas de administración de apps que bloqueen secretos y limiten certificados.
- Federar pipelines de GitHub Actions sin secretos y elegir el tipo de identidad administrada adecuado.
- Proteger workload identities con acceso condicional, CAE e ID Protection.
- Distinguir las funciones gratuitas de las de Workload ID Premium.

> **Atención.** Workload ID Premium es un SKU independiente de 3 USD por identidad al mes y no viene en E5 ni en E7. Tiene prueba gratuita de 90 días (30 en el canal Modern; no disponible en Azure Government). La FAQ dice a la vez que hay que licenciar cada identidad elegible y que una licencia en el tenant desbloquea las funciones: aclara el cumplimiento contractual con tu equipo de cuenta ([FAQ de Workload ID](https://learn.microsoft.com/en-us/entra/workload-id/workload-identities-faqs)).

> **Consejo Ninja.** Acceso condicional para workload identities: solo service principals de un solo tenant registrados en tu tenant; no cubre apps multitenant ni identidades administradas; si asignas la política a un grupo que contiene al service principal, **no se aplica** (asígnalo directamente); el único control es Bloquear y existe modo solo informe ([acceso condicional para workload identities](https://learn.microsoft.com/en-us/entra/identity/conditional-access/workload-identity)).

> **Novedad.** CAE para workload identities admite tokens de hasta 24 horas revocables casi en tiempo real (deshabilitación, eliminación o riesgo alto), solo contra Microsoft Graph y si la app declara la capacidad `cp1`; requiere Workload ID Premium ([CAE para workload identities](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-continuous-access-evaluation-workload)). En GitHub, los repositorios creados desde el 15 de julio de 2026 usan un claim `sub` inmutable con los IDs de owner y repositorio ([OIDC de GitHub en Azure](https://docs.github.com/actions/how-tos/security-for-github-actions/security-hardening-your-deployments/configuring-openid-connect-in-azure)).

> **Consejo Ninja.** Para cazar actividad de workload identities a partir de tokens, la función KQL MicrosoftCloudWorkloadActivity de Thomas Naunheim combina CloudAppEvents, GraphAPIAuditEvents y los inicios de sesión, y detecta tokens emitidos antes de una contención ([hunting por tokens](https://www.cloud-architekt.net/token-hunting-workload-identity-activity/)).

**¿Tienes poco tiempo?**

- [Frequently asked questions about Microsoft Entra Workload ID](https://learn.microsoft.com/en-us/entra/workload-id/workload-identities-faqs) · Documentación
- [Workload identity federation](https://learn.microsoft.com/en-us/entra/workload-id/workload-identity-federation) · Documentación
- [Microsoft Entra Conditional Access for workload identities](https://learn.microsoft.com/en-us/entra/identity/conditional-access/workload-identity) · Documentación
- [Tutorial: Enforce secret and certificate standards using application management policies](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/tutorial-enforce-secret-standards) · Laboratorio

### Documentación, cursos y credenciales

- [Configure restrictions on how applications can be configured (app management policies)](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/configure-app-management-policies) · Documentación · Oficial. Guía para aplicar políticas de administración de aplicaciones que bloquean secretos, limitan la vida de certificados y contraseñas, bloquean apps multitenant/consumidor y exigen CA de confianza.
- [Microsoft Entra Conditional Access for workload identities](https://learn.microsoft.com/en-us/entra/identity/conditional-access/workload-identity) · Documentación · Oficial. Cómo crear políticas de Acceso condicional basadas en ubicación o riesgo para service principals de un solo tenant, con modo solo informe y revisión en los registros de inicio de sesión.
- [What are workload identities?](https://learn.microsoft.com/en-us/entra/workload-id/workload-identities-overview) · Documentación · Oficial · Microsoft Learn. Introduce aplicaciones, service principals e identidades administradas como identidades de carga de trabajo y los escenarios clave de protección, detección y ciclo de vida, incluida la relación con identidades de agente.
- [Managed identity best practice recommendations](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/managed-identity-best-practice-recommendations) · Documentación · Oficial · Microsoft Learn. Criterios para elegir identidades administradas asignadas por el usuario o por el sistema, límites de creación, mínimo privilegio y mantenimiento.
- [Securing workload identities with Microsoft Entra ID Protection](https://learn.microsoft.com/en-us/entra/id-protection/concept-workload-identity-risk) · Documentación · Oficial · 6 ago 2025. Explica las detecciones de riesgo para service principals (credenciales filtradas, actividad anómala, tráfico API sospechoso, aplicaciones maliciosas) y cómo investigarlas y remediarlas.
- [Workload identity federation](https://learn.microsoft.com/en-us/entra/workload-id/workload-identity-federation) · Documentación · Oficial · Microsoft Learn · 9 abr 2025. Explica cómo una app registrada o una identidad administrada asignada por el usuario confía en tokens de un IdP externo (GitHub, Kubernetes, Google Cloud, AWS, SPIFFE) para eliminar secretos.
- [Frequently asked questions about Microsoft Entra Workload ID](https://learn.microsoft.com/en-us/entra/workload-id/workload-identities-faqs) · Documentación · Oficial · 18 mar 2025. Aclara qué funciones de identidades de carga son gratuitas (políticas de administración de apps, identidades administradas, federación) y cuáles requieren Workload ID Premium (Acceso condicional y ID Protection para workload identities, revisiones de acceso de service principals privilegiados, recomendaciones de salud de apps).
- [Configuring OpenID Connect in Azure (GitHub Actions)](https://docs.github.com/actions/how-tos/security-for-github-actions/security-hardening-your-deployments/configuring-openid-connect-in-azure) · Documentación · Comunidad · GitHub · GitHub Docs. Procedimiento de GitHub para que los workflows obtengan tokens de Azure vía OIDC y federación de identidad, sin guardar secretos de larga duración.
- [Continuous access evaluation for workload identities](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-continuous-access-evaluation-workload) · Documentación · Oficial · Microsoft Learn. Describe CAE para service principals: tokens de hasta 24 h revocables en tiempo casi real ante deshabilitación, eliminación o riesgo alto, solo contra Microsoft Graph.
- [Securing managed identities in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/architecture/service-accounts-managed-identities) · Documentación · Oficial · Microsoft Learn (Entra architecture). Guía de arquitectura para encontrar, evaluar y endurecer identidades administradas, con consultas de Graph para inventariarlas y revisar sus permisos.

### Laboratorios, GitHub y herramientas

- [Tutorial: Enforce secret and certificate standards using application management policies](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/tutorial-enforce-secret-standards) · Laboratorio · Oficial · Microsoft Learn. Tutorial con Graph PowerShell para leer y actualizar la política de administración de apps del tenant, bloqueando secretos y limitando certificados a 180 días.
- [Set up a Flexible Federated identity credential (preview)](https://learn.microsoft.com/en-us/entra/workload-id/workload-identities-set-up-flexible-federated-identity-credential) · Laboratorio · Oficial · Vista previa · Microsoft Learn. Guía para crear credenciales federadas flexibles con expresiones de coincidencia de claims (por ejemplo, ramas comodín de GitHub) atadas a identificadores inmutables del repositorio. *Nota:* Para GitHub exige además repository_id o repository_owner_id; está en preview

**Manos a la obra**

1. `Laboratorio` Inventaria con Microsoft Graph PowerShell los service principals, las identidades administradas (filtro `servicePrincipalType eq 'ManagedIdentity'`) y las credenciales con su fecha de vencimiento; marca los secretos que vencen en 30 días ([proteger identidades administradas](https://learn.microsoft.com/en-us/entra/architecture/service-accounts-managed-identities)).
2. `Laboratorio` Respalda la política de administración de apps del tenant y aplica una que bloquee secretos nuevos y limite los certificados a 180 días; prueba que un secreto nuevo falla ([tutorial](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/tutorial-enforce-secret-standards)).
3. `Laboratorio` Federa un workflow de GitHub Actions con una identidad administrada asignada por el usuario, sin secretos, y despliega un recurso de prueba; luego crea una credencial federada flexible atada a `repository_id` ([credencial flexible](https://learn.microsoft.com/en-us/entra/workload-id/workload-identities-set-up-flexible-federated-identity-credential), [OIDC de GitHub](https://docs.github.com/actions/how-tos/security-for-github-actions/security-hardening-your-deployments/configuring-openid-connect-in-azure)).
4. `Laboratorio parcial` Activa la prueba de Workload ID Premium y crea CA14 para un service principal propio, primero en solo informe, revisando los inicios de sesión de service principals. Limitación: la prueba dura 90 días; en producción, usa un service principal piloto ([acceso condicional para workload identities](https://learn.microsoft.com/en-us/entra/identity/conditional-access/workload-identity)).
5. `Laboratorio parcial` Revisa el informe de workload identities riesgosas y prepara el runbook de respuesta para credenciales filtradas. Limitación: en un tenant de prueba es raro ver detecciones reales; sin Premium el detalle es limitado ([riesgo de workload identities](https://learn.microsoft.com/en-us/entra/id-protection/concept-workload-identity-risk)).
6. `Solo producción` Elimina los secretos de los service principals de producción por oleadas, migrando a certificados o federación. Cómo hacerlo seguro: inventario de dependencias con los dueños, ventana de cambio, prueba del nuevo método antes de borrar el secreto y reversión documentada.

**¿Quieres profundizar?**

- [Set up a Flexible Federated identity credential (preview)](https://learn.microsoft.com/en-us/entra/workload-id/workload-identities-set-up-flexible-federated-identity-credential) · Laboratorio

<a id="a2"></a>

## A2 · Detección y respuesta a amenazas de identidad (ITDR)

*L400 · ~12 h · Origen: Ninja de Defender for Identity (2021–2024) y Attack & Defense Playbook de Entra; se profundiza en el programa de Defender XDR*

Los atacantes entran por la identidad: phishing de adversario en el medio (AiTM) que roba la sesión, phishing con código de dispositivo, password spray, fatiga de MFA, robo y reproducción de tokens, abuso de consentimiento y ataques a Kerberos en AD. Una campaña de AiTM de abril de 2026 alcanzó a más de 35.000 usuarios en 13.000 organizaciones. **ITDR** es la disciplina de detectar y responder a estos ataques en el AD local y en la nube, con las señales correlacionadas.

En el ecosistema de Microsoft, ID Protection aporta el riesgo en la nube; **Defender for Identity** vigila controladores de dominio, AD CS, AD FS y Entra Connect; Defender for Cloud Apps aporta la actividad en las aplicaciones; y **Defender XDR** correlaciona todo y ejecuta la **interrupción automática de ataques**, que deshabilita usuarios en Entra ID y AD con una confianza de al menos 99 %. En octubre de 2026, Defender for Identity activó automáticamente el sensor v3.x para clientes existentes (con 30 días para excluirse) y sumó alertas sobre Entra ID.

Aquí trabajarás la mirada centrada en identidad: CAE, consultas sobre EntraIdSignInEvents, GraphAPIAuditEvents y registros de Graph, y el **Attack & Defense Playbook** comunitario. El despliegue de Defender for Identity, sus alertas y la interrupción automática se profundizan en el programa de Defender XDR (módulos I5, M4 y M7).

**Por qué importa**

Según el Microsoft Digital Defense Report 2026, las cuentas válidas explican cerca del 20 % de los accesos iniciales observados por Defender Experts. Detectar y contener un compromiso de identidad en minutos, y no en días, es la diferencia entre un incidente y una crisis. Métricas: tiempo de detección y de contención, cobertura de sensores en DC, AD CS, AD FS y Connect, e incidentes contenidos automáticamente.

**Qué vas a lograr**

- Describir las técnicas actuales de ataque a identidades y sus señales.
- Relacionar las señales de ID Protection, Defender for Identity, Defender for Cloud Apps y Defender XDR.
- Cazar amenazas de identidad con KQL sobre tablas de Entra y de Defender.
- Gobernar la interrupción automática de ataques sobre identidades, incluidas sus exclusiones.
- Usar el Attack & Defense Playbook para mapear detecciones y mitigaciones.

> **Novedad.** Defender for Identity, octubre de 2026: activación automática del sensor v3.x y de la auditoría de Windows para clientes existentes (con 30 días para excluirse), GA del sensor v3.x sin Defender for Endpoint en Windows Server 2019 y posteriores, y nuevas alertas sobre Entra ID: registro malicioso de MFA, inicio de sesión sospechoso con TAP y robo de cookies de sesión ([novedades de Defender for Identity](https://learn.microsoft.com/en-us/defender-for-identity/whats-new)). El despliegue se profundiza en el programa de Defender XDR (módulos I5 y M4).

> **Novedad.** Abril de 2026: una campaña con señuelos de «código de conducta», CAPTCHA y robo de tokens por AiTM alcanzó a más de 35.000 usuarios en 13.000 organizaciones; el análisis incluye consultas de búsqueda avanzada ([Microsoft Threat Intelligence](https://www.microsoft.com/en-us/security/blog/2026/05/04/breaking-the-code-multi-stage-code-of-conduct-phishing-campaign-leads-to-aitm-token-compromise/)). Sigue la [etiqueta AiTM del blog de seguridad](https://www.microsoft.com/en-us/security/blog/tag/adversary-in-the-middle/) para casos como el phishing de código de dispositivo de septiembre de 2026.

> **Consejo Ninja.** La interrupción automática de ataques deshabilita usuarios en Entra ID y AD con una confianza de al menos 99 % y ya soporta Okta y AWS en vista previa ([interrupción automática](https://learn.microsoft.com/en-us/defender-xdr/automatic-attack-disruption)). GraphAPIAuditEvents, en Defender, es una alternativa más económica a MicrosoftGraphActivityLogs para detectar herramientas como AzureHound ([GraphAPIAuditEvents](https://cloudbrothers.info/en/detect-threats-graphapiauditevents-part-3/)).

> **Consejo Ninja.** El Attack & Defense Playbook comunitario mapea password spray, consentimiento ilícito, PRT, AiTM, Entra Connect, EIDSCA e identidades de agente a detecciones, mitigaciones y MITRE ATT&CK, con consultas ya actualizadas a EntraIdSignInEvents ([playbook](https://github.com/Cloud-Architekt/AzureAD-Attack-Defense)). Para el phishing de código de dispositivo, lee la guía de prevención, detección y respuesta de octubre de 2026 de Christopher Brumm ([ITDR](https://chris-brumm.com/categories/itdr/)).

**¿Tienes poco tiempo?**

- [Defending against evolving identity attack techniques](https://www.microsoft.com/en-us/security/blog/2025/05/29/defending-against-evolving-identity-attack-techniques/) · Blog oficial
- [Attack and Defense Playbook for Microsoft Entra (AzureAD-Attack-Defense)](https://github.com/Cloud-Architekt/AzureAD-Attack-Defense) · GitHub
- [What's new in Microsoft Defender for Identity](https://learn.microsoft.com/en-us/defender-for-identity/whats-new) · Documentación
- [Breaking the code: Multi-stage 'code of conduct' phishing campaign leads to AiTM token compromise](https://www.microsoft.com/en-us/security/blog/2026/05/04/breaking-the-code-multi-stage-code-of-conduct-phishing-campaign-leads-to-aitm-token-compromise/) · Blog oficial

### Documentación, cursos y credenciales

- [What's new in Microsoft Defender for Identity](https://learn.microsoft.com/en-us/defender-for-identity/whats-new) · Documentación · Oficial · Nuevo · oct 2026. Novedades mensuales de Defender for Identity: sensor v3.x con activación automática, nuevas alertas sobre Entra ID (registro malicioso de MFA, inicio de sesión sospechoso con TAP, robo de cookies de sesión), AD CS, Kerberos y Okta.
- [Continuous access evaluation](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-continuous-access-evaluation) · Documentación · Oficial · Microsoft Learn. Explica la evaluación continua de acceso (basada en CAEP) que revoca sesiones casi en tiempo real ante eventos críticos y aplica políticas de ubicación en Exchange, SharePoint, Teams y Graph.
- [Alert classification for password spray attacks - Microsoft Defender XDR](https://learn.microsoft.com/en-us/defender-xdr/alert-classification-password-spray-attack) · Documentación · Oficial. Guía de clasificación de alertas de password spray en Defender XDR con pasos de investigación, consultas de búsqueda avanzada y acciones recomendadas para distinguir verdaderos de falsos positivos.

### Anuncios y blogs oficiales

- [Defending against evolving identity attack techniques](https://www.microsoft.com/en-us/security/blog/2025/05/29/defending-against-evolving-identity-attack-techniques/) · Blog oficial · Empleado de Microsoft · Igor Sakhnov · Microsoft Security Blog · 29 may 2025. Panorama de técnicas de compromiso de identidades en la nube (AiTM con kits como Evilginx, device code phishing, phishing fuera del correo, ataques post-compromiso) y defensas recomendadas con Entra y Defender.
- [Breaking the code: Multi-stage 'code of conduct' phishing campaign leads to AiTM token compromise](https://www.microsoft.com/en-us/security/blog/2026/05/04/breaking-the-code-multi-stage-code-of-conduct-phishing-campaign-leads-to-aitm-token-compromise/) · Blog oficial · Oficial · Nuevo · Microsoft Defender Security Research Team; Microsoft Threat Intelligence · Microsoft Security Blog · 4 may 2026. Análisis de una campaña AiTM de abril de 2026 contra más de 35.000 usuarios en 13.000 organizaciones, con señuelos de 'código de conducta', CAPTCHA y robo de tokens, incluyendo detecciones y consultas de hunting.
- [Adversary-in-the-middle (AiTM) News and Insights (Microsoft Security Blog tag)](https://www.microsoft.com/en-us/security/blog/tag/adversary-in-the-middle/) · Blog oficial · Oficial · Microsoft Security Blog. Índice actualizado de investigaciones de Microsoft Threat Intelligence sobre AiTM, phishing de código de dispositivo (EvilTokens, sep-2026), Tycoon2FA y campañas de robo de tokens.

### Laboratorios, GitHub y herramientas

- [Attack and Defense Playbook for Microsoft Entra (AzureAD-Attack-Defense)](https://github.com/Cloud-Architekt/AzureAD-Attack-Defense) · GitHub · MVP · Nuevo · Sami Lamppu; Thomas Naunheim (con revisores como Christopher Brumm, Fabian Bader, Joosua Santasalo, Nestori Syynimaa) · GitHub (Cloud-Architekt) · oct 2026. Publicación comunitaria con capítulos de ataque, detección (Defender XDR, Sentinel, ID Protection), mitigación y mapeo MITRE ATT&CK para password spray, consent grant, PRT, AiTM, Entra Connect, EIDSCA, identidades de agentes y movimiento lateral desde AD.

### Comunidad: blogs, libros, newsletters y eventos

- [Chris Brumm's Blog - ITDR](https://chris-brumm.com/categories/itdr/) · Blog · MVP · Nuevo · Christopher Brumm · Chris Brumm's Blog · 24 oct 2026. Categoría ITDR del blog con 'Device Code Phishing: Prevention, Detection and Response' (oct-2026), sobre cómo funciona el ataque, qué detecta Microsoft y qué debe construir el defensor.
- [Analyzing Workload Identity Activity Through Token-Based Hunting](https://www.cloud-architekt.net/token-hunting-workload-identity-activity/) · Blog · MVP · Thomas Naunheim · cloud-architekt.net · 30 ene 2026. Introduce la función KQL MicrosoftCloudWorkloadActivity para cazar actividad basada en tokens de identidades de carga (CloudAppEvents, GraphAPIAuditEvents y registros de inicio de sesión) y detectar uso anómalo o tokens emitidos antes de una contención.
- [Detect threats using GraphAPIAuditEvents - Part 3](https://cloudbrothers.info/en/detect-threats-graphapiauditevents-part-3/) · Blog · MVP · Fabian Bader · Cloudbrothers · 14 ago 2025. Muestra cómo detectar herramientas de reconocimiento como AzureHound usando la tabla GraphAPIAuditEvents de Defender XDR (alternativa más económica a MicrosoftGraphActivityLogs) con consultas KQL normalizadas.

**Manos a la obra**

1. `Laboratorio` Arma tu mapa de señales: para password spray, AiTM, phishing de código de dispositivo, consentimiento ilícito y robo de PRT, indica qué fuente lo detecta (ID Protection, Defender for Identity, Defender for Cloud Apps o Defender XDR) y qué tabla consultarías ([técnicas de ataque a identidades](https://www.microsoft.com/en-us/security/blog/2025/05/29/defending-against-evolving-identity-attack-techniques/)).
2. `Laboratorio parcial` Provoca unos pocos inicios de sesión fallidos controlados sobre cuentas de prueba y sigue la guía de clasificación de alertas de password spray. Limitación: un intento de laboratorio no siempre dispara la detección ([clasificación de password spray](https://learn.microsoft.com/en-us/defender-xdr/alert-classification-password-spray-attack)).
3. `Laboratorio parcial` Despliega el sensor v3.x de Defender for Identity en el controlador de dominio del laboratorio y revisa las recomendaciones de postura. Limitación: requiere la VM de AD con Windows Server 2019 o posterior y costo de cómputo ([novedades de Defender for Identity](https://learn.microsoft.com/en-us/defender-for-identity/whats-new)).
4. `Laboratorio` Importa dos consultas del [Attack & Defense Playbook](https://github.com/Cloud-Architekt/AzureAD-Attack-Defense) y las del análisis de la [campaña AiTM de abril de 2026](https://www.microsoft.com/en-us/security/blog/2026/05/04/breaking-the-code-multi-stage-code-of-conduct-phishing-campaign-leads-to-aitm-token-compromise/) a la búsqueda avanzada, adáptalas a EntraIdSignInEvents y documenta qué devuelven.
5. `Laboratorio` Revoca la sesión de un usuario de prueba con clientes compatibles abiertos y mide el efecto de CAE frente a un cliente que no lo admite ([CAE](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-continuous-access-evaluation)).
6. `Solo producción` Caza AiTM y robo de tokens con telemetría real y revisa la configuración de la interrupción automática. Cómo hacerlo seguro: consultas de solo lectura con Security Reader, un ejercicio de mesa con el [playbook de robo de tokens](https://learn.microsoft.com/en-us/security/zero-trust/security-operations-playbook-token-theft) y la revisión de exclusiones con el SOC ([interrupción automática](https://learn.microsoft.com/en-us/defender-xdr/automatic-attack-disruption)).

**¿Quieres profundizar?**

- [Chris Brumm's Blog - ITDR](https://chris-brumm.com/categories/itdr/) · Blog
- [Analyzing Workload Identity Activity Through Token-Based Hunting](https://www.cloud-architekt.net/token-hunting-workload-identity-activity/) · Blog
- [Detect threats using GraphAPIAuditEvents - Part 3](https://cloudbrothers.info/en/detect-threats-graphapiauditevents-part-3/) · Blog

<a id="a3"></a>

## A3 · Automatización e identidad como código

*L400 · ~12 h · Origen: Nuevo en esta edición*

La base de toda automatización de identidad es **Microsoft Graph**: la API y el SDK de PowerShell. El módulo **Microsoft Entra PowerShell**, construido sobre el SDK de Graph, es más de 98 % compatible con el antiguo módulo AzureAD y alcanza cerca de 80 % de paridad con MSOnline mediante alias (`Enable-EntraAzureADAlias`), lo que facilita migrar scripts de módulos obsoletos. Para gobernanza, las APIs de Graph cubren revisiones de acceso, entitlement management, Lifecycle Workflows y PIM: usa v1.0 en producción, porque beta no tiene soporte productivo.

Llevar la configuración a código significa poder versionarla, compararla y restaurarla. **Tenant Governance** (GA el 10 de agosto de 2026) ofrece líneas base y monitoreo de deriva para Entra, Defender, Exchange, Intune, Purview y Teams; **Microsoft365DSC** sigue activo con su versión mayor de octubre de 2026 (PowerShell 7.6 y cambios incompatibles); y **EntraExporter** fue archivado el 22 de octubre de 2026. Terraform y Bicep también se usan para identidad, pero esta investigación no verificó guías oficiales vigentes para Entra: si ya los usas, aplica los mismos principios de revisión por pares y pruebas.

Las pruebas cierran el círculo: **Maester** ejecuta cientos de controles (CIS, CISA SCuBA, EIDSCA y el Zero Trust Assessment) en GitHub Actions o Azure DevOps; su versión 3.0 está en vista previa, así que conviene fijar la 2.3.0. Y como el MFA obligatorio alcanza a la automatización con cuentas de usuario, tus pipelines deben usar identidades de carga federadas ([A1](#a1)).

**Por qué importa**

Los cambios manuales en el portal no dejan historial ni se pueden revertir con confianza. Llevar la configuración de identidad a código y a pruebas automatizadas permite detectar deriva, revisar cambios por pares y reconstruir el tenant tras un incidente. Métricas: políticas de acceso condicional versionadas, pruebas de Maester aprobadas por semana y deriva detectada y corregida.

**Qué vas a lograr**

- Automatizar tareas de identidad con Microsoft Graph PowerShell y Entra PowerShell sin módulos obsoletos.
- Monitorear la deriva de configuración con Tenant Governance o Microsoft365DSC.
- Integrar Maester en un pipeline de CI/CD con versión fijada y federación.
- Extender Lifecycle Workflows y entitlement management con Logic Apps.
- Elegir la herramienta adecuada según soporte, licencia y madurez.

> **Qué cambió.** EntraExporter fue archivado el 22 de octubre de 2026 y queda solo como referencia histórica ([README](https://github.com/microsoft/EntraExporter/blob/main/README.md)). Para instantáneas y deriva usa Tenant Governance o Microsoft365DSC, cuya versión mayor de octubre de 2026 exige PowerShell 7.6 y trae cambios incompatibles ([Microsoft365DSC](https://microsoft365dsc.com/blog/october-2026-major-release/)).

> **Novedad.** Tenant Governance llegó a GA el 10 de agosto de 2026 con descubrimiento de tenants relacionados, relaciones de administración delegada de mínimo privilegio, líneas base con monitoreo de deriva para Entra, Defender, Exchange Online, Intune, Purview y Teams, y creación segura de tenants. Con P1 o P2 tienes hasta 30 monitores, 800 recursos por día y 20.000 recursos al mes en instantáneas ([anuncio](https://techcommunity.microsoft.com/blog/microsoft-entra-blog/microsoft-entra-tenant-governance-is-now-generally-available/4543638), [licencias](https://learn.microsoft.com/en-us/entra/id-governance/tenant-governance/licensing)).

> **Atención.** Maester trae unos 890 controles (CIS, CISA SCuBA, EIDSCA, ORCA y AD) e integra el Zero Trust Assessment, pero es un proyecto comunitario sin soporte de producto; su versión 3.0 está en vista previa, así que fija la 2.3.0 en tus pipelines ([Maester](https://maester.dev/), [Maester 3.0](https://maester.dev/blog/maester-3-0)).

> **Consejo Ninja.** Microsoft Entra PowerShell es más de 98 % compatible con AzureAD y alcanza cerca de 80 % de paridad con MSOnline gracias a `Enable-EntraAzureADAlias`; funciona en Windows PowerShell 5.1 y en PowerShell 7 ([Entra PowerShell](https://learn.microsoft.com/en-us/powershell/entra-powershell/overview?view=entra-powershell)). Para gobernanza como código, usa las APIs v1.0 de Graph: beta no tiene soporte productivo ([APIs de ID Governance](https://learn.microsoft.com/en-us/graph/api/resources/identitygovernance-overview?view=graph-rest-1.0)).

**¿Tienes poco tiempo?**

- [What is Microsoft Entra PowerShell?](https://learn.microsoft.com/en-us/powershell/entra-powershell/overview?view=entra-powershell) · Documentación
- [Overview of Microsoft Entra ID Governance using Microsoft Graph](https://learn.microsoft.com/en-us/graph/api/resources/identitygovernance-overview?view=graph-rest-1.0) · Documentación
- [Maester: open-source security testing for Microsoft 365](https://maester.dev/) · Herramienta
- [Microsoft Entra Tenant Governance is now generally available](https://techcommunity.microsoft.com/blog/microsoft-entra-blog/microsoft-entra-tenant-governance-is-now-generally-available/4543638) · Blog oficial

### Documentación, cursos y credenciales

- [Overview of Microsoft Entra ID Governance using Microsoft Graph](https://learn.microsoft.com/en-us/graph/api/resources/identitygovernance-overview?view=graph-rest-1.0) · Documentación · Oficial. Describe las APIs de Microsoft Graph para revisiones de acceso, entitlement management, lifecycle workflows, PIM y términos de uso, base para automatizar la gobernanza como código.
- [What is Microsoft Entra PowerShell?](https://learn.microsoft.com/en-us/powershell/entra-powershell/overview?view=entra-powershell) · Documentación · Oficial. Presenta el módulo Microsoft Entra PowerShell, construido sobre el SDK de Microsoft Graph PowerShell, orientado a escenarios y con alias de compatibilidad (Enable-EntraAzureADAlias) para migrar scripts de AzureAD/MSOnline.
- [Lifecycle Workflows custom task extension (Workflow Extensibility)](https://learn.microsoft.com/en-us/entra/id-governance/lifecycle-workflow-extensibility) · Documentación · Oficial. Explica cómo extender Lifecycle Workflows con extensiones de tareas personalizadas que invocan Azure Logic Apps (consumo) en modo 'launch and continue' o 'launch and wait', con autorización por identidad administrada.
- [Trigger Logic Apps with custom extensions in entitlement management](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-logic-apps-integration) · Documentación · Oficial. Cómo vincular Logic Apps a catálogos y políticas de paquetes de acceso para ejecutar automatizaciones al crear, aprobar, asignar, retirar o antes de expirar una asignación.
- [Licensing for Microsoft Entra Tenant Governance](https://learn.microsoft.com/en-us/entra/id-governance/tenant-governance/licensing) · Documentación · Oficial · Microsoft Learn. Describe la licencia de Tenant Governance, con monitoreo de deriva de configuración (hasta 800 recursos diarios) y snapshots incluidos desde P1, y capacidad adicional con ID Governance.

### Anuncios y blogs oficiales

- [Microsoft Entra Tenant Governance is now generally available](https://techcommunity.microsoft.com/blog/microsoft-entra-blog/microsoft-entra-tenant-governance-is-now-generally-available/4543638) · Blog oficial · Empleado de Microsoft · Nuevo · CindyCrane · Microsoft Entra Blog (Tech Community) · 10 ago 2026. Anuncio de disponibilidad general de Tenant Governance: descubrimiento de tenants relacionados, relaciones de gobierno con administración delegada de menor privilegio, gestión de configuración con líneas base y deriva, y creación segura de tenants.

### Laboratorios, GitHub y herramientas

- [Maester: open-source security testing for Microsoft 365](https://maester.dev/) · Herramienta · Empleado de Microsoft · Nuevo · Merill Fernando y equipo Maester (Fabian Bader, Thomas Naunheim, Mike Soule, Sam Erde y comunidad) · Maester (proyecto open source) · 2 nov 2026. Framework open source (MIT) de pruebas de seguridad para Microsoft 365, Entra, Azure y AD con 890 controles integrados (CIS, CISA SCuBA, EIDSCA, ORCA, AD) más el Zero Trust Assessment de Microsoft, automatizable en GitHub Actions o Azure DevOps.
- [Maester releases (GitHub maester365/maester)](https://github.com/maester365/maester/releases) · GitHub · Comunidad · Nuevo · Merill Fernando y colaboradores · GitHub (maester365) · nov 2026. Historial de versiones de Maester con cambios recientes (pruebas de Entra como MT.1260 para usuarios de alto riesgo sin remediar, integración del Zero Trust Assessment).

### Comunidad: blogs, libros, newsletters y eventos

- [Thomas Naunheim - Blog posts](https://www.cloud-architekt.net/blog/) · Blog · MVP · Nuevo · Thomas Naunheim · cloud-architekt.net · 29 sep 2026. Blog de investigación sobre identidad privilegiada (EntraOps, RMAU, Tenant Governance, identidades de carga de trabajo y robo de tokens) del co-creador del Azure AD Attack & Defense Playbook.
- [Microsoft365DSC – October 2026 Major Release (version 2.26.1007.1)](https://microsoft365dsc.com/blog/october-2026-major-release/) · Blog · Comunidad · Nuevo · Fabien Tschanz · Microsoft365DSC · 4 oct 2026. Detalla la versión mayor de octubre de 2026 de Microsoft365DSC (recursos basados en clases, PowerShell 7.6 obligatorio, nuevos permisos de Graph y cambios incompatibles) para gestionar la configuración de Entra y M365 como código DSC.
- [Moving from Microsoft365DSC to Tenant Configuration Management APIs](https://github.com/Microsoft365DSC/Microsoft365DSC/blob/Dev/docs/docs/blog/2026/utcm-transition/utcm-transition.md) · Blog · Comunidad · Equipo Microsoft365DSC · Microsoft365DSC (GitHub docs). Guía de transición desde Microsoft365DSC hacia las APIs oficiales de Tenant Configuration Management en Graph (snapshots JSON y monitoreo de deriva), con ejemplos de llamadas para Acceso condicional y ubicaciones con nombre.
- [Maester 3.0: a new test engine, and a heads-up for preview users](https://maester.dev/blog/maester-3-0) · Blog · Empleado de Microsoft · Vista previa · Nuevo · Merill Fernando · Maester blog · 7 oct 2026. Explica los cambios de Maester 3.0 (pruebas nativas con atributo [MaesterTest], Pester opcional, PowerShell 7.4+) y cómo fijar la versión 2.3.0 en pipelines para evitar cambios incompatibles. *Nota:* Recomendación operativa: en automatización fijar versión (Install-Module Maester -RequiredVersion 2.3.0) hasta que 3.0 sea release

**Manos a la obra**

1. `Laboratorio` Migra un script heredado de AzureAD o MSOnline a Microsoft Graph PowerShell o Entra PowerShell y ejecútalo con una identidad de carga de trabajo federada, no con una cuenta de usuario ([Entra PowerShell](https://learn.microsoft.com/en-us/powershell/entra-powershell/overview?view=entra-powershell)).
2. `Laboratorio` Exporta tus políticas de acceso condicional a JSON con Microsoft Graph, versiónalas en un repositorio y aprueba un cambio mediante pull request con revisión por pares.
3. `Laboratorio` Ejecuta Maester en GitHub Actions con `Install-Module Maester -RequiredVersion 2.3.0` y publica el informe como artefacto del pipeline ([Maester 3.0 y cómo fijar versiones](https://maester.dev/blog/maester-3-0)).
4. `Laboratorio` Crea en Tenant Governance una instantánea y un monitor de deriva sobre una política de acceso condicional de prueba; modifícala y comprueba que la deriva se detecta ([anuncio de Tenant Governance](https://techcommunity.microsoft.com/blog/microsoft-entra-blog/microsoft-entra-tenant-governance-is-now-generally-available/4543638)).
5. `Laboratorio parcial` Extiende un flujo de Lifecycle Workflows con una Logic App («launch and continue») autorizada por identidad administrada. Limitación: requiere la prueba de ID Governance y una suscripción de Azure; el rol Logic App Operator no basta ([extensibilidad](https://learn.microsoft.com/en-us/entra/id-governance/lifecycle-workflow-extensibility)).
6. `Solo producción` Descubre los tenants relacionados y crea relaciones de gobierno con Tenant Governance. Cómo hacerlo seguro: según fuentes comunitarias el descubrimiento es una acción de un solo sentido; empieza con instantáneas y monitores sobre recursos no críticos, con aprobación del CISO y registro del cambio.

**¿Quieres profundizar?**

- [Thomas Naunheim - Blog posts](https://www.cloud-architekt.net/blog/) · Blog
- [Maester 3.0: a new test engine, and a heads-up for preview users](https://maester.dev/blog/maester-3-0) · Blog
- [Microsoft365DSC – October 2026 Major Release (version 2.26.1007.1)](https://microsoft365dsc.com/blog/october-2026-major-release/) · Blog
- [Moving from Microsoft365DSC to Tenant Configuration Management APIs](https://github.com/Microsoft365DSC/Microsoft365DSC/blob/Dev/docs/docs/blog/2026/utcm-transition/utcm-transition.md) · Blog

<a id="a4"></a>

## A4 · Arquitecturas de referencia y estrategia de acceso privilegiado

*L400 · ~8 h · Origen: Security Adoption Framework (versión pública en Learn), MCRA y Zero Trust Workshop · Identidad*

El **modelo de acceso empresarial** reemplaza el antiguo modelo de niveles (tiers) de Active Directory: el Tier 0 se convierte en el **plano de control**, el Tier 1 se divide en plano de **administración** y plano de **datos y cargas de trabajo**, y el Tier 2 en acceso de **usuarios** y de **aplicaciones**, con rutas de acceso privilegiado explícitas. La guía pública del **Security Adoption Framework** para la disciplina de identidades y acceso extiende ese diseño y suma la ruta de acceso de los **agentes de IA**, con identidades dedicadas.

La estrategia de acceso privilegiado se apoya en cuatro ideas: controlar explícitamente cada ruta, aislar el trabajo privilegiado en **estaciones de acceso privilegiado (PAW)**, eliminar el acceso permanente con PIM y monitorear de forma continua. Microsoft publica una hoja de ruta en cuatro etapas —24 a 48 horas, 2 a 4 semanas, 1 a 3 meses y más de 6 meses— y las **Microsoft Cybersecurity Reference Architectures (MCRA)** como mapa de capacidades.

En identidad, el Tier 0 incluye roles como Global Administrator y Privileged Role Administrator, los servidores de Entra Connect, AD FS y PKI y, según la comunidad, el rol AI Administrator. Herramientas como EntraOps clasifican privilegios por plano y detectan rupturas de nivel. La Secure Future Initiative de Microsoft sirve de caso de referencia: 99,97 % de sus pares usuario-dispositivo con MFA resistente al phishing y 1,4 millones de aplicaciones sin uso eliminadas.

**Por qué importa**

Sin un modelo explícito de planos y rutas, los privilegios se mezclan: una estación de uso diario administra el plano de control y un compromiso menor escala a todo el tenant. El modelo de acceso empresarial ordena la defensa por impacto y le da al CISO un lenguaje para priorizar. Métricas: activos Tier 0 identificados y protegidos, administradores que usan PAW y rupturas de nivel detectadas.

**Qué vas a lograr**

- Explicar el modelo de acceso empresarial y su relación con el modelo de niveles de AD.
- Identificar los activos Tier 0 de identidad, incluidos servidores híbridos y roles de IA.
- Diseñar rutas de acceso privilegiado con PAW, PIM, acceso condicional y unidades administrativas restringidas.
- Priorizar con la guía pública del SAF, la MCRA, el Zero Trust Workshop y el Zero Trust Assessment.

> **Consejo Ninja.** El modelo de acceso empresarial convierte el Tier 0 en plano de control, divide el Tier 1 en plano de administración y de datos y cargas de trabajo, y el Tier 2 en acceso de usuarios y de aplicaciones ([modelo de acceso empresarial](https://learn.microsoft.com/en-us/security/privileged-access-workstations/privileged-access-access-model)). La guía pública del Security Adoption Framework lo extiende con la ruta de acceso de los agentes de IA, con identidades dedicadas ([arquitectura de acceso empresarial](https://learn.microsoft.com/en-us/security/zero-trust/security-adoption-discipline-identity-access-enterprise-model)).

> **Novedad.** La hoja de ruta de acceso privilegiado de Entra tiene cuatro etapas —24 a 48 horas, 2 a 4 semanas, 1 a 3 meses y más de 6 meses— y supone P2 ([asegurar el acceso privilegiado](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/security-planning)). La MCRA de abril de 2025 agregó Exposure Management, Windows LAPS, passkeys y Verified ID, y retiró Entra Permissions Management ([MCRA](https://learn.microsoft.com/es-es/security/adoption/mcra)).

> **Novedad.** Secure Future Initiative, julio de 2026: MFA resistente al phishing en el 99,97 % de los pares usuario-dispositivo de Microsoft y 1,4 millones de aplicaciones sin uso eliminadas; el informe incluye guía accionable por pilares para clientes ([blog](https://www.microsoft.com/en-us/security/blog/2026/07/10/securing-our-future-july-2026-progress-report-on-microsofts-secure-future-initiative/), [informe](https://www.microsoft.com/en-us/trust-center/security/secure-future-initiative/sfi-progress-report-july-2026)).

> **Atención.** EntraOps (versión 1.0, septiembre de 2026) clasifica privilegios de Entra, Azure, Intune y Defender por plano y detecta rupturas de nivel, pero es un proyecto de investigación sin soporte de Microsoft que requiere PowerShell 7.4 o superior ([EntraOps](https://github.com/Cloud-Architekt/EntraOps)). El Zero Trust Assessment tampoco tiene soporte oficial ([repositorio](https://github.com/microsoft/zerotrustassessment)).

**¿Tienes poco tiempo?**

- [Securing privileged access - Enterprise access model](https://learn.microsoft.com/en-us/security/privileged-access-workstations/privileged-access-access-model) · Documentación
- [Design an enterprise access architecture (Security Adoption Framework - Identities and Access discipline)](https://learn.microsoft.com/en-us/security/zero-trust/security-adoption-discipline-identity-access-enterprise-model) · Documentación
- [Securing privileged access for hybrid and cloud deployments in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/security-planning) · Documentación
- [Microsoft Zero Trust Workshop - Identity](https://learn.microsoft.com/en-us/security/zero-trust/workshop-zero-trust-identity) · Documentación

### Documentación, cursos y credenciales

- [Securing privileged access - Enterprise access model](https://learn.microsoft.com/en-us/security/privileged-access-workstations/privileged-access-access-model) · Documentación · Oficial · Nuevo · 7 may 2026. Presenta el modelo de acceso empresarial (plano de control, de administración y de datos/cargas, más rutas de acceso de usuario, aplicación y privilegiadas) que evoluciona el antiguo modelo de niveles (tiers) de Active Directory.
- [Privileged access (Zero Trust overview - privileged access)](https://learn.microsoft.com/en-us/security/zero-trust/security-concept-privileged-access) · Documentación · Oficial. Explica por qué el acceso privilegiado debe controlarse explícitamente, aislarse en estaciones de trabajo privilegiadas (PAW), monitorearse continuamente y protegerse sin acceso permanente, centrado en el plano de control de identidad.
- [Design an enterprise access architecture (Security Adoption Framework - Identities and Access discipline)](https://learn.microsoft.com/en-us/security/zero-trust/security-adoption-discipline-identity-access-enterprise-model) · Documentación · Oficial. Guía de arquitectura del Security Adoption Framework (SAF) para diseñar una arquitectura de acceso empresarial Zero Trust que unifica acceso general, privilegiado y de agentes de IA con identidades dedicadas.
- [Securing identity with Zero Trust (Identity, the first pillar of a Zero Trust security architecture)](https://learn.microsoft.com/en-us/security/zero-trust/deploy/identity) · Documentación · Oficial. Guía de despliegue Zero Trust para identidad con objetivos iniciales (federación, Acceso condicional, analítica) y posteriores (gobernanza, análisis en tiempo real, integración de señales de amenazas).
- [Microsoft Zero Trust Workshop - Identity](https://learn.microsoft.com/en-us/security/zero-trust/workshop-zero-trust-identity) · Documentación · Oficial. Describe el pilar de identidad del Zero Trust Workshop con áreas de implementación priorizadas (inventario, Acceso condicional, menor privilegio, PIM, identidades de carga, ciclo de vida, externos, SecOps de identidad).
- [Securing privileged access for hybrid and cloud deployments in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/security-planning) · Documentación · Oficial. Hoja de ruta en cuatro etapas (24-48 h, 2-4 semanas, 1-3 meses, 6+ meses) para asegurar el acceso privilegiado en Entra ID, incluyendo PIM, cuentas de emergencia y procedimiento 'break glass'.
- [Arquitecturas de referencia de ciberseguridad de Microsoft (MCRA)](https://learn.microsoft.com/es-es/security/adoption/mcra) · Documentación · Oficial · ES · abr 2025. Página de las Microsoft Cybersecurity Reference Architectures (MCRA), componente del Security Adoption Framework, con descarga de la versión de abril de 2025 y diagramas de acceso de usuario Zero Trust, SecOps y capacidades de Microsoft.
- [SFI Progress Report July 2026 (Microsoft Trust Center)](https://www.microsoft.com/en-us/trust-center/security/secure-future-initiative/sfi-progress-report-july-2026) · Documentación · Oficial · Nuevo · Microsoft Trust Center · jul 2026. Página del informe de progreso SFI de julio de 2026 con descarga del informe completo y guía accionable por pilares (identidades y secretos, aislamiento de tenants, ingeniería).

### Anuncios y blogs oficiales

- [Securing our future: July 2026 progress report on Microsoft's Secure Future Initiative](https://www.microsoft.com/en-us/security/blog/2026/07/10/securing-our-future-july-2026-progress-report-on-microsofts-secure-future-initiative/) · Blog oficial · Empleado de Microsoft · Nuevo · Salim Chawro · Microsoft Security Blog · 10 jul 2026. Resumen del cuarto informe de progreso de la Secure Future Initiative con métricas internas de Microsoft sobre MFA resistente al phishing, eliminación de aplicaciones sin uso y aislamiento de credenciales.

### Laboratorios, GitHub y herramientas

- [microsoft/zerotrustassessment](https://github.com/microsoft/zerotrustassessment) · GitHub · Empleado de Microsoft · Nuevo · Equipo de Microsoft (proyecto comunitario) · GitHub (Microsoft) · oct 2026. Módulo de PowerShell de solo lectura que evalúa el inquilino frente a la guía Zero Trust en siete pilares (identidad, dispositivos, red, datos, infraestructura, SecOps e IA) y genera un informe priorizado.
- [EntraOps (Privileged EAM) - Management and Monitoring of Enterprise Access Model](https://github.com/Cloud-Architekt/EntraOps) · GitHub · MVP · Nuevo · Thomas Naunheim · GitHub (Cloud-Architekt) · oct 2026. Proyecto comunitario que clasifica privilegios de Entra, Azure, Intune y Defender según el Enterprise Access Model (planos de control/administración), detecta rupturas de tier, alimenta watchlists de Sentinel y protege activos privilegiados con grupos de Acceso condicional y RMAU.

**Manos a la obra**

1. `Laboratorio` Clasifica los roles y grupos privilegiados de tu laboratorio en planos de control, administración y datos con [EntraOps](https://github.com/Cloud-Architekt/EntraOps) o con una hoja propia, y marca las rupturas de nivel.
2. `Laboratorio` Diseña las rutas de acceso privilegiado: PAW o equivalente, PIM con contexto de autenticación, la política CA10 y una unidad de administración restringida para las cuentas Tier 0. Entregable: diagrama y matriz de controles ([acceso privilegiado](https://learn.microsoft.com/en-us/security/zero-trust/security-concept-privileged-access)).
3. `Laboratorio` Ejecuta el Zero Trust Assessment y mapea sus hallazgos de identidad a las cuatro etapas de la [hoja de ruta de acceso privilegiado](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/security-planning).
4. `Laboratorio` Recorre el [Zero Trust Workshop · Identidad](https://learn.microsoft.com/en-us/security/zero-trust/workshop-zero-trust-identity) y prioriza tres áreas de implementación para tu organización con su justificación.
5. `Solo producción` Inventario Tier 0 real: Global Administrators, Privileged Role Administrators, servidores de Entra Connect, AD FS y PKI, y el rol AI Administrator. Cómo hacerlo seguro: inventario de solo lectura, acceso restringido al documento y validación con los dueños antes de cambiar nada.

**¿Quieres profundizar?**

- [microsoft/zerotrustassessment](https://github.com/microsoft/zerotrustassessment) · GitHub
- [EntraOps (Privileged EAM) - Management and Monitoring of Enterprise Access Model](https://github.com/Cloud-Architekt/EntraOps) · GitHub

<a id="a5"></a>

## A5 · Respuesta a incidentes de identidad

*L400 · ~10 h · Origen: Playbooks de respuesta a incidentes de Microsoft (disciplina SecOps del SAF); se coordina con el programa de Defender XDR*

Cuando una identidad se compromete, el orden de las acciones importa. Microsoft publica **playbooks** para password spray, robo de tokens (incluido AiTM), concesión ilícita de consentimiento y aplicaciones comprometidas o maliciosas, que ahora viven en la disciplina de operaciones de seguridad del Security Adoption Framework. Cada uno trae requisitos previos, flujo, lista de verificación, pasos de investigación y recuperación.

La **revocación de emergencia** combina varias acciones: deshabilitar la cuenta, restablecer la contraseña dos veces en AD si la cuenta es híbrida, revocar los tokens de actualización (`Revoke-MgUserSignInSession`) y deshabilitar dispositivos. Recuerda que un token de acceso dura una hora por defecto, que Entra ID no revoca las cookies de sesión de las aplicaciones y que CAE acorta la ventana en los servicios compatibles.

Para recuperar la configuración, **Entra Backup and Recovery** hace una copia diaria de usuarios, grupos, apps, service principals, políticas de acceso condicional, ubicaciones con nombre y políticas de autenticación, y permite generar un informe de diferencias antes de restaurar. Requiere P1 o P2 y no recupera objetos eliminados definitivamente. La coordinación con el SOC y la interrupción automática se ven también en el programa de Defender XDR (módulos A1 y A8).

**Por qué importa**

En un incidente de identidad cada minuto cuenta: un token robado sigue siendo válido hasta que se revoca y una política de acceso condicional borrada abre la puerta a todos. Playbooks probados, revocación ensayada y respaldo de la configuración reducen el tiempo de contención y de recuperación. Métricas: tiempo de contención, tiempo de restauración y simulacros realizados por trimestre.

**Qué vas a lograr**

- Aplicar los playbooks de Microsoft para password spray, robo de tokens, consentimiento ilícito y apps comprometidas.
- Ejecutar una revocación de emergencia completa en entornos solo nube e híbridos.
- Recuperar configuración y objetos con Entra Backup and Recovery y conocer sus límites.
- Coordinar la respuesta de identidad con el SOC y con la interrupción automática de ataques.

> **Qué cambió.** Los playbooks de respuesta a incidentes de Microsoft pasaron a la disciplina SecOps del Security Adoption Framework (rutas security/zero-trust/security-operations-playbook-*); la ruta anterior del de password spray sigue accesible ([password spray](https://learn.microsoft.com/en-us/security/zero-trust/security-operations-playbook-password-spray)).

> **Atención.** Revocación: los tokens de acceso duran una hora por defecto y Entra ID no revoca las cookies de sesión de las aplicaciones; en cuentas híbridas, restablece la contraseña dos veces en AD. Para revocar cuentas de administrador necesitas Privileged Authentication Administrator ([revocar el acceso](https://learn.microsoft.com/en-us/entra/identity/users/users-revoke-access)).

> **Atención.** Backup and Recovery hace una copia diaria con 7 días de historial según Learn (5 según la API de Graph), ejecuta un solo trabajo a la vez, no recupera objetos eliminados definitivamente ni los que tienen su origen de autoridad en AD local, y sus recuperaciones no se deshacen solas: genera siempre un informe de diferencias. Hard Deletion Protection está en vista previa ([visión general](https://learn.microsoft.com/en-us/entra/backup/overview), [recuperar objetos](https://learn.microsoft.com/en-us/entra/backup/recover-objects), [API](https://learn.microsoft.com/en-us/graph/api/resources/entrarecoveryservices-backup-recovery-overview?view=graph-rest-1.0)).

> **Consejo Ninja.** Para aplicaciones comprometidas, el playbook recomienda el módulo Microsoft Entra Incident Response PowerShell y requiere P2 para las señales de ID Protection ([apps comprometidas o maliciosas](https://learn.microsoft.com/en-us/security/zero-trust/security-operations-playbook-compromised-malicious-app)). La coordinación con el SOC se ve en el programa de Defender XDR (módulos A1 y A8).

**¿Tienes poco tiempo?**

- [Token theft playbook](https://learn.microsoft.com/en-us/security/zero-trust/security-operations-playbook-token-theft) · Documentación
- [Revoke user access in an emergency in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/users/users-revoke-access) · Documentación
- [Microsoft Entra Backup and Recovery overview](https://learn.microsoft.com/en-us/entra/backup/overview) · Documentación
- [App consent grant investigation (incident response playbook)](https://learn.microsoft.com/en-us/security/zero-trust/security-operations-playbook-app-consent) · Documentación

**Revocación de emergencia de un usuario comprometido**

| Paso | Acción | Cómo | Ten en cuenta |
|---|---|---|---|
| 1 | Deshabilitar la cuenta | En Entra ID y, si es híbrida, también en AD | Impide nuevos inicios de sesión |
| 2 | Restablecer la contraseña | Dos veces en AD si la cuenta es híbrida | Invalida las credenciales robadas |
| 3 | Revocar los tokens de actualización | `Revoke-MgUserSignInSession` con Microsoft Graph PowerShell | Para cuentas de administrador necesitas Privileged Authentication Administrator |
| 4 | Deshabilitar los dispositivos del usuario | Centro de administración de Entra o Microsoft Graph | Evita que un dispositivo comprometido siga obteniendo tokens |
| 5 | Revisar métodos registrados y consentimientos | Información de seguridad del usuario y auditoría de consentimientos | Un atacante pudo registrar un método de MFA o consentir una app |
| 6 | Cerrar la ventana de los tokens vigentes | CAE en los servicios compatibles; el token de acceso dura una hora por defecto | Entra ID no revoca las cookies de sesión de las aplicaciones: ciérralas en cada app |

Fuentes: [revocar el acceso en una emergencia](https://learn.microsoft.com/en-us/entra/identity/users/users-revoke-access), [CAE](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-continuous-access-evaluation) y [playbook de robo de tokens](https://learn.microsoft.com/en-us/security/zero-trust/security-operations-playbook-token-theft).

### Documentación, cursos y credenciales

- [Microsoft Entra Backup and Recovery overview](https://learn.microsoft.com/en-us/entra/backup/overview) · Documentación · Oficial · Nuevo · 5 nov 2026. Explica la solución integrada que respalda diariamente usuarios, grupos, apps, service principals, políticas de Acceso condicional, ubicaciones con nombre y políticas de autenticación para recuperarlos a un estado conocido tras cambios accidentales o compromisos.
- [App consent grant investigation (incident response playbook)](https://learn.microsoft.com/en-us/security/zero-trust/security-operations-playbook-app-consent) · Documentación · Oficial. Playbook oficial para identificar, investigar, contener y remediar ataques de concesión ilícita de consentimiento (consent phishing), con flujo, lista de verificación, pasos de investigación y mitigaciones.
- [Token theft playbook](https://learn.microsoft.com/en-us/security/zero-trust/security-operations-playbook-token-theft) · Documentación · Oficial. Playbook oficial con árbol de decisión para investigar, contener y recuperarse de robo y reproducción de tokens (incluido AiTM) usando registros de Entra, Defender for Cloud Apps, Sentinel y detecciones de ID Protection.
- [Password spray investigation](https://learn.microsoft.com/en-us/security/zero-trust/security-operations-playbook-password-spray) · Documentación · Oficial. Playbook para identificar e investigar ataques de password spray (incluida configuración de auditoría de AD FS y Connect Health), con flujo, lista de verificación, acciones inmediatas y recuperación.
- [Compromised and malicious applications investigation](https://learn.microsoft.com/en-us/security/zero-trust/security-operations-playbook-compromised-malicious-app) · Documentación · Oficial. Playbook para investigar, contener y recuperar aplicaciones y service principals comprometidos o maliciosos, usando riesgo de workload identities, registros de auditoría, Graph y App governance.
- [Revoke user access in an emergency in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/users/users-revoke-access) · Documentación · Oficial. Procedimiento para revocar todo el acceso de un usuario comprometido en entornos híbridos y solo nube: deshabilitar cuenta, restablecer contraseña dos veces en AD, revocar tokens de actualización, deshabilitar dispositivos y apoyarse en CAE.
- [Automatic attack disruption in Microsoft Defender](https://learn.microsoft.com/en-us/defender-xdr/automatic-attack-disruption) · Documentación · Oficial. Describe cómo Defender XDR correlaciona señales para contener automáticamente activos comprometidos (deshabilitar usuario en Entra ID y AD, contener dispositivos/IP) durante ataques como ransomware, BEC o AiTM, con exclusiones y reversión.
- [Recover objects using Microsoft Entra Backup and Recovery](https://learn.microsoft.com/en-us/entra/backup/recover-objects) · Documentación · Oficial · Nuevo · 30 jun 2026. Procedimiento para recuperar objetos desde un informe de diferencias o directamente desde un backup, con filtros por tipo u ID y cancelación de trabajos.
- [Overview of Microsoft Entra Backup and Recovery APIs - Microsoft Graph v1.0](https://learn.microsoft.com/en-us/graph/api/resources/entrarecoveryservices-backup-recovery-overview?view=graph-rest-1.0) · Documentación · Oficial. Referencia de las APIs de Graph para listar snapshots, crear trabajos de vista previa (dry-run) y de recuperación, y revisar cambios fallidos, útil para automatizar la recuperación del tenant.

**Manos a la obra**

1. `Laboratorio` Simulacro de revocación sobre un usuario de prueba: deshabilitar, restablecer la contraseña, `Revoke-MgUserSignInSession` y deshabilitar dispositivos; mide cuánto tardan Outlook y Teams en perder acceso ([revocar el acceso](https://learn.microsoft.com/en-us/entra/identity/users/users-revoke-access)).
2. `Laboratorio` Con Backup and Recovery, modifica una política de acceso condicional de prueba, genera el informe de diferencias y recupérala ([recuperar objetos](https://learn.microsoft.com/en-us/entra/backup/recover-objects)).
3. `Laboratorio` Haz un ejercicio de mesa con el [playbook de robo de tokens](https://learn.microsoft.com/en-us/security/zero-trust/security-operations-playbook-token-theft): árbol de decisión, quién hace qué y en cuánto tiempo.
4. `Laboratorio` Investiga una concesión ilícita simulada (una app de prueba con permisos excesivos consentida por un usuario de prueba) siguiendo el [playbook de consentimiento](https://learn.microsoft.com/en-us/security/zero-trust/security-operations-playbook-app-consent) y documenta la contención.
5. `Laboratorio` Protege con una acción protegida el borrado definitivo de objetos, para que un atacante no pueda eliminar lo que Backup and Recovery no recupera ([acciones protegidas](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/protected-actions-add)).
6. `Solo producción` Simulacro integral con el SOC en producción. Cómo hacerlo seguro: cuentas de prueba creadas para el ejercicio, aviso previo al SOC y a la mesa de ayuda, criterios de parada y revisión posterior con lecciones aprendidas.

<a id="reto-avanzado"></a>

## Reto del nivel

**Simulacro de compromiso de identidad de punta a punta.** Con cuentas y apps de prueba, simula una cadena: consentimiento ilícito a una app con permisos excesivos, credencial agregada a un service principal y cambio no autorizado en una política de acceso condicional. Detecta cada paso con KQL, contén con el playbook que corresponda (revocación, deshabilitación de la app y recuperación de la política con Backup and Recovery) y deja como código lo que evitaría que se repita: política de apps sin secretos, acción protegida y una prueba de Maester. Entrega: línea de tiempo, tiempos de detección y contención, y lecciones aprendidas.

<a id="quiz-avanzado"></a>

## Evaluación del nivel

Responde y compara con [Evaluaciones y respuestas](06_Evaluaciones_y_respuestas.md#eval-avanzado). Con 80 % o más, ¡nivel aprobado! (En la versión web puedes corregir en línea y generar tu certificado).

1. ¿Cómo se licencia Workload ID Premium?
   - a) Incluido en Microsoft 365 E5
   - b) Incluido en Entra ID P2
   - c) SKU independiente de 3 USD por identidad al mes
   - d) Gratis para las identidades administradas

2. ¿A qué se aplica el acceso condicional para workload identities?
   - a) A identidades administradas
   - b) A service principals de un solo tenant asignados directamente a la política
   - c) A apps SaaS multitenant
   - d) A grupos que contienen service principals

3. ¿Qué vida máxima para certificados de aplicación recomienda el tutorial de políticas de administración de apps?
   - a) 180 días
   - b) 30 días
   - c) 90 días
   - d) 2 años

4. ¿En qué condiciones funciona CAE para workload identities?
   - a) Contra cualquier recurso y sin licencia
   - b) Solo con identidades administradas
   - c) Solo en apps multitenant
   - d) Contra Microsoft Graph, si la app declara la capacidad cp1 y con Workload ID Premium

5. ¿Cuál es la latencia máxima típica de CAE ante eventos críticos, como deshabilitar una cuenta?
   - a) Instantánea
   - b) 1 hora
   - c) 24 horas
   - d) Hasta 15 minutos

6. La interrupción automática de ataques de Defender deshabilita usuarios en Entra ID y AD cuando la confianza es de al menos:
   - a) 50 %
   - b) 75 %
   - c) 99 %
   - d) 100 %, con aprobación manual

7. ¿Qué tabla de la búsqueda avanzada reemplazó a AADSignInEventsBeta el 19 de octubre de 2026?
   - a) IdentityLogonEvents
   - b) EntraIdSignInEvents
   - c) SigninLogs
   - d) AgentsInfo

8. ¿Cuál es el estado de EntraExporter en noviembre de 2026?
   - a) En disponibilidad general
   - b) En vista previa
   - c) Integrado en Entra PowerShell
   - d) Archivado desde el 22 de octubre de 2026

9. ¿Qué versión de Maester conviene fijar en un pipeline en noviembre de 2026?
   - a) La 2.3.0, porque la 3.0 está en vista previa
   - b) La 3.0, porque es la única compatible
   - c) La 1.0
   - d) Siempre la última disponible

10. ¿Qué incluye Tenant Governance con licencias P1 o P2?
   - a) Monitoreo ilimitado
   - b) Hasta 30 monitores y 800 recursos por día
   - c) Solo instantáneas manuales
   - d) Nada: requiere ID Governance

11. En el modelo de acceso empresarial, ¿en qué se convierte el antiguo Tier 0?
   - a) En el plano de datos y cargas de trabajo
   - b) En el acceso de usuarios
   - c) En el plano de control
   - d) En el plano de aplicaciones

12. ¿Qué NO puede hacer Entra Backup and Recovery?
   - a) Restaurar una política de acceso condicional modificada
   - b) Generar un informe de diferencias
   - c) Recuperar objetos por tipo o por ID
   - d) Recuperar objetos eliminados definitivamente

13. Ante una cuenta híbrida comprometida, ¿qué combinación recomienda Microsoft?
   - a) Deshabilitarla, restablecer la contraseña dos veces en AD, revocar los tokens de actualización y deshabilitar sus dispositivos
   - b) Solo borrar la cuenta
   - c) Esperar a que expire el token de acceso
   - d) Cambiarle la licencia

14. ¿Dónde viven ahora los playbooks de respuesta a incidentes de Microsoft?
   - a) En el Ninja de Defender XDR
   - b) En la disciplina SecOps del Security Adoption Framework
   - c) En la página de licencias de Entra
   - d) Solo en GitHub

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

# Nivel 2 · Intermedio · Proteger, gobernar y observar

*Microsoft Entra Ninja Training: identidad y acceso para la era de los agentes de IA · Edición 2026*

[← Nivel 1 · Inicial](01_Nivel_1_Inicial.md) · [Índice del programa](README.md) · [Nivel 3 · Avanzado →](03_Nivel_3_Avanzado.md)

<a id="intermedio"></a>

Acceso condicional avanzado, ID Protection, PIM, gobernanza e identidades externas, aplicaciones y consentimiento, monitoreo, dispositivos y Global Secure Access. Terminas operando la identidad con el riesgo, los privilegios y los accesos bajo control y con evidencia en los registros.

*L300 · 8 módulos · ~70 horas · 84 recursos*

**Módulos de este nivel:** [M1 Acceso condicional avanzado](#m1) · [M2 ID Protection](#m2) · [M3 PIM: roles, grupos y alertas](#m3) · [M4 Gobernanza y externos](#m4) · [M5 Apps y consentimiento](#m5) · [M6 Monitoreo y registros](#m6) · [M7 Dispositivos e identidad](#m7) · [M8 Global Secure Access](#m8)

<a id="m1"></a>

## M1 · Acceso condicional avanzado: contexto, fortalezas, protección de tokens y CAE

*L300 · ~10 h · Origen: SC-300 · Implement authentication and access management (profundización)*

Con la línea base en marcha, el siguiente nivel es la precisión. El **contexto de autenticación** (valores C1 a C99) exige autenticación reforzada justo donde está el riesgo: al activar un rol en PIM, al ejecutar una acción protegida o al abrir datos sensibles dentro de una aplicación. Las **fortalezas personalizadas** restringen qué métodos valen en cada caso, los **filtros de dispositivo** apuntan a equipos concretos —como las estaciones de acceso privilegiado— y la condición de **flujos de autenticación** controla el device code flow y la transferencia de autenticación.

La otra mitad es proteger la sesión. La **protección de tokens** solo acepta tokens de sesión vinculados al dispositivo mediante el PRT: está en disponibilidad general para apps nativas en Windows, iOS/iPadOS y macOS (Exchange, SharePoint y Teams, más Azure Virtual Desktop y Windows 365 en Windows) y en vista previa para apps de navegador hacia Azure Resource Manager. **CAE** revoca sesiones casi en tiempo real; su modo estricto de ubicación sigue en vista previa y en octubre de 2026 llegó, también en vista previa, la CAE universal con señales de dispositivo en Global Secure Access.

Cierras con escala y gobierno: políticas para invitados con confianza explícita entre tenants, el puente hacia identidades de carga de trabajo ([A1](03_Nivel_3_Avanzado.md#a1)) y agentes ([X3](04_Nivel_4_Identidad_para_agentes_de_IA.md#x3)) y el agente de optimización de acceso condicional de Security Copilot, que detecta brechas de cobertura y propone políticas en solo informe ([X5](04_Nivel_4_Identidad_para_agentes_de_IA.md#x5)).

**Por qué importa**

Los atacantes ya no adivinan contraseñas: roban tokens y sesiones. Las políticas avanzadas reducen la ventana de reutilización de un token robado, exigen reautenticación fuerte donde está el riesgo y evitan la proliferación de políticas difíciles de mantener. Métricas: usuarios de alto valor con protección de tokens, acciones sensibles bajo contexto de autenticación y número total de políticas.

**Qué vas a lograr**

- Usar contexto de autenticación y fortalezas personalizadas para proteger acciones y datos sensibles.
- Desplegar protección de tokens en solo informe e interpretar los registros interactivos y no interactivos.
- Explicar CAE, su modo estricto de ubicación y su interacción con Global Secure Access.
- Aplicar filtros de dispositivo y la condición de flujos de autenticación.
- Diseñar políticas para invitados con confianza explícita entre tenants.

> **Novedad.** Protección de tokens: GA para apps nativas en Windows, iOS/iPadOS y macOS (Exchange, SharePoint y Teams, más Azure Virtual Desktop y Windows 365 en Windows) y vista previa para apps de navegador hacia Azure Resource Manager. Ojo: la tabla de plataformas marca Apple como GA, pero la sección de dispositivos aún dice «Apple (Preview)» y la versión en español sigue en vista previa ([protección de tokens](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-token-protection)).

> **Atención.** El modo estricto de ubicación de CAE (vista previa) bloquea si la IP que ve el recurso no está permitida. Cuidado al combinarlo con Global Secure Access y túneles divididos: usa antes el workbook de CAE para detectar desajustes de IP ([CAE estricto](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-continuous-access-evaluation-strict-enforcement)).

> **Qué cambió.** Desde septiembre de 2024, las políticas de flujos de autenticación que apuntan a «All resources» también aplican al Device Registration Service ([flujos de autenticación](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-authentication-flows)). En junio de 2026 llegó, en vista previa, el acceso condicional para cuentas de usuario de agentes, y en octubre, la CAE universal con señales de dispositivo en Global Secure Access ([What's new](https://learn.microsoft.com/en-us/entra/fundamentals/whats-new)).

> **Consejo Ninja.** Cuando evalúes varias fortalezas a la vez, recuerda el patrón de usar TAP solo para la acción de registro de información de seguridad desde dispositivos conformes ([cómo funcionan las fortalezas](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-strength-how-it-works)). El agente de optimización de acceso condicional (P1 más SCU; hasta 300 usuarios y 150 apps por ejecución) propone políticas en solo informe y se configura en [X5](04_Nivel_4_Identidad_para_agentes_de_IA.md#x5) ([agente de optimización](https://learn.microsoft.com/en-us/entra/security-copilot/conditional-access-agent-optimization)).

**¿Tienes poco tiempo?**

- [Token Protection in Microsoft Entra Conditional Access](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-token-protection) · Documentación
- [Developer guide to Conditional Access authentication context](https://learn.microsoft.com/en-us/entra/identity-platform/developer-guide-conditional-access-authentication-context) · Documentación
- [Continuous access evaluation](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-continuous-access-evaluation) · Documentación
- [Conditional Access: Authentication flows](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-authentication-flows) · Documentación

### Documentación, cursos y credenciales

- [Token Protection in Microsoft Entra Conditional Access](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-token-protection) · Documentación · Oficial · Nuevo · Microsoft Learn · 20 ago 2026. Explica la protección de tokens, que solo acepta tokens de sesión vinculados al dispositivo (PRT) para Exchange, SharePoint, Teams, AVD y Windows 365, con plataformas soportadas y despliegue en solo informe.
- [Microsoft Entra Conditional Access Optimization Agent](https://learn.microsoft.com/en-us/entra/security-copilot/conditional-access-agent-optimization) · Documentación · Oficial · Microsoft Learn. Agente de Security Copilot que detecta usuarios, apps e identidades de agente no cubiertos por acceso condicional y propone o crea políticas en solo informe y consolidaciones; aquí solo como enlace (otro investigador cubre agentes).
- [Continuous access evaluation](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-continuous-access-evaluation) · Documentación · Oficial · Microsoft Learn. Explica la evaluación continua de acceso (basada en CAEP) que revoca sesiones casi en tiempo real ante eventos críticos y aplica políticas de ubicación en Exchange, SharePoint, Teams y Graph.
- [Conditional Access: Authentication flows](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-authentication-flows) · Documentación · Oficial · Microsoft Learn. Explica la condición de flujos de autenticación (device code flow y transferencia de autenticación), el seguimiento de protocolo y su aplicación al Device Registration Service desde septiembre de 2024.
- [Developer guide to Conditional Access authentication context](https://learn.microsoft.com/en-us/entra/identity-platform/developer-guide-conditional-access-authentication-context) · Documentación · Oficial · Microsoft Learn. Explica cómo las aplicaciones solicitan un contexto de autenticación (C1-C99) para exigir autenticación reforzada en acciones o datos sensibles dentro de la aplicación.
- [How Conditional Access authentication strengths work](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-strength-how-it-works) · Documentación · Oficial · Microsoft Learn. Detalla cómo se evalúan varias fortalezas de autenticación a la vez y el patrón de usar TAP solo para la acción de registro de información de seguridad desde dispositivos conformes.
- [Strictly enforce location policies using continuous access evaluation (preview)](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-continuous-access-evaluation-strict-enforcement) · Documentación · Oficial · Vista previa · Microsoft Learn. Describe el modo de aplicación estricta de ubicación de CAE, que bloquea si la IP vista por el recurso no está permitida, y el uso del workbook de CAE para detectar desajustes de IP. *Nota:* Advertencia sobre su combinación con Global Secure Access y túneles divididos

### Comunidad: blogs, libros, newsletters y eventos

- [Nathan McNulty - Blog (Sign-in Frequency, device code flow, RMAU)](https://nathanmcnulty.com/blog/) · Blog · MVP · Nuevo · Nathan McNulty · 13 oct 2026. Blog con artículos sobre frecuencia de inicio de sesión, auditoría previa al bloqueo de device code flow, unidades administrativas de administración restringida y el cambio a passkeys por defecto.
- [Cloudbrothers (Fabian Bader)](https://cloudbrothers.info/en/) · Blog · MVP · Nuevo · Fabian Bader · Cloudbrothers · 10 may 2026. Blog con análisis de bypasses de acceso condicional, brokers de tokens alternativos y detección con registros de actividad de Graph y AAD Graph.
- [Building a Conditional Access Analyzer That Works Entirely Offline](https://danielchronlund.com/tag/Microsoft%20Entra) · Blog · MVP · Nuevo · Daniel Chronlund · Daniel Chronlund Tech Blog · 29 oct 2026. Etiqueta Entra del blog de Chronlund con su analizador offline de acceso condicional y artículos de 2026 sobre Zero Trust para agentes y Agent 365.

**Manos a la obra**

1. `Laboratorio` Crea un contexto de autenticación (C1), asígnalo a una política que exija MFA resistente al phishing y úsalo en la activación de un rol de PIM; valida con un usuario de prueba y guarda el registro de inicio de sesión ([contexto de autenticación](https://learn.microsoft.com/en-us/entra/identity-platform/developer-guide-conditional-access-authentication-context)).
2. `Laboratorio parcial` Despliega la protección de tokens (CA09) en solo informe con una VM Windows 11 unida a Entra y revisa los inicios de sesión interactivos y no interactivos. Limitación: la compatibilidad real de las apps solo se ve con los dispositivos de los usuarios; en producción, solo informe y un piloto ([protección de tokens](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-token-protection)).
3. `Laboratorio` Crea una política con filtro de dispositivo que solo permita administrar desde equipos marcados como PAW (por ejemplo, con un atributo de extensión) y pruébala en solo informe y con What If.
4. `Laboratorio parcial` Configura el acceso entre tenants para confiar en el MFA de un socio de prueba y crea la política CA12 para invitados; verifica el resultado en los registros. Limitación: necesitas un segundo tenant de prueba que haga de socio ([acceso entre tenants](https://learn.microsoft.com/en-us/entra/external-id/cross-tenant-access-overview)).
5. `Laboratorio parcial` Habilita el workbook de CAE y compara las IP que ve Entra con las que ven los recursos antes de considerar el modo estricto de ubicación. Limitación: requiere Log Analytics y tráfico desde redes variadas ([CAE estricto](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-continuous-access-evaluation-strict-enforcement)).
6. `Solo producción` Ejecuta el agente de optimización de acceso condicional y revisa sus sugerencias sin aplicarlas; requiere SCU facturadas y datos reales. Cómo hacerlo seguro: creación de políticas desactivada, revisión con Security Reader y aprobación solo de políticas en solo informe ([agente de optimización](https://learn.microsoft.com/en-us/entra/security-copilot/conditional-access-agent-optimization)).

**¿Quieres profundizar?**

- [Nathan McNulty - Blog (Sign-in Frequency, device code flow, RMAU)](https://nathanmcnulty.com/blog/) · Blog
- [Cloudbrothers (Fabian Bader)](https://cloudbrothers.info/en/) · Blog

<a id="m2"></a>

## M2 · Entra ID Protection: riesgo de usuarios e inicios de sesión

*L300 · ~6 h · Origen: SC-300 · ID Protection; se complementa con el programa de Defender XDR (módulos I6 y M5)*

**ID Protection** analiza señales de Microsoft para calcular el riesgo de cada usuario y de cada inicio de sesión: password spray, token anómalo, adversario en el medio, adición sospechosa de credenciales y decenas de detecciones más. Las detecciones en tiempo real aparecen en 5 a 10 minutos y las fuera de línea hasta en 48 horas; el riesgo bajo caduca a los seis meses y el medio o alto persiste hasta que se remedia o se descarta. Sin P2 solo verás «Additional risk detected», sin detalle.

El gran cambio de 2026: **las políticas de riesgo heredadas configuradas en ID Protection se retiraron el 1 de octubre de 2026**. La única vía soportada son las políticas de acceso condicional basadas en riesgo. La recomendación vigente es exigir **Require risk remediation** ante riesgo de usuario alto —que agrega una fortaleza de autenticación y la frecuencia de inicio de sesión «cada vez»— y MFA con frecuencia «cada vez» ante riesgo de inicio de sesión medio o alto, siempre en políticas separadas.

También vas a operar: informes de usuarios, inicios de sesión y detecciones riesgosas, roles para confirmar o descartar riesgo, Microsoft Graph PowerShell para acciones en bloque y la experiencia de autorremediación que verá el usuario. El riesgo de identidades de carga y de agentes se ve en [A1](03_Nivel_3_Avanzado.md#a1) y [X3](04_Nivel_4_Identidad_para_agentes_de_IA.md#x3); la investigación con Security Copilot, en [X5](04_Nivel_4_Identidad_para_agentes_de_IA.md#x5); y la mirada del SOC, en el programa de Defender XDR (módulos I6 y M5).

**Por qué importa**

Las políticas de riesgo convierten detecciones en acciones automáticas: un usuario con credenciales filtradas se remedia solo, sin ticket a la mesa de ayuda. Tras el retiro de las políticas heredadas, un tenant sin políticas de acceso condicional basadas en riesgo se queda sin respuesta automática. Métricas: usuarios de riesgo alto sin remediar (meta: cero), tiempo medio de remediación y porcentaje de autorremediación.

**Qué vas a lograr**

- Interpretar detecciones de riesgo de usuario y de inicio de sesión, su latencia y su licencia.
- Migrar las políticas heredadas a acceso condicional basado en riesgo.
- Configurar «Require risk remediation» y explicar su comportamiento con usuarios sin contraseña.
- Investigar, confirmar o descartar riesgo desde el portal y con Microsoft Graph PowerShell.

> **Qué cambió.** Las políticas de riesgo heredadas configuradas en ID Protection se retiraron el 1 de octubre de 2026: la vía soportada son las políticas de acceso condicional basadas en riesgo, creadas en solo informe y luego activadas. Requieren P2, incluido en Microsoft 365 E5 ([configurar políticas de riesgo](https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-configure-risk-policies)).

> **Consejo Ninja.** «Require risk remediation» remedia el riesgo de usuario (no el de inicio de sesión) y no aplica a invitados ni externos: con contraseña exige un cambio seguro; a un usuario sin contraseña le revoca las sesiones y le pide iniciar sesión de nuevo; y si un atacante agregó un dispositivo, lo deshabilita ([políticas basadas en riesgo](https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-policies)).

> **Atención.** Latencias: las detecciones en tiempo real aparecen en 5 a 10 minutos y las fuera de línea, hasta en 48 horas; el riesgo bajo caduca a los seis meses. Sin P2 solo verás «Additional risk detected», y algunas detecciones dependen de Defender for Cloud Apps ([tipos de detección](https://learn.microsoft.com/en-us/entra/id-protection/concept-risk-detection-types), [catálogo de detecciones](https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-risks)).

> **Consejo Ninja.** Para comunicar el cambio a usuarios y mesa de ayuda, usa la página de autorremediación, que incluye el caso del técnico de alto riesgo de un proveedor de servicios ([experiencia del usuario](https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-user-experience)). Security Operator puede confirmar o descartar riesgo y Conditional Access Administrator crea las políticas ([visión general](https://learn.microsoft.com/en-us/entra/id-protection/overview-identity-protection)).

**¿Tienes poco tiempo?**

- [Configure and enable risk policies (Risk policies - Microsoft Entra ID Protection)](https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-configure-risk-policies) · Documentación
- [Microsoft Entra ID Protection risk-based access policies](https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-policies) · Documentación
- [What are risk detections? - Microsoft Entra ID Protection](https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-risks) · Documentación

### Documentación, cursos y credenciales

- [What are risk detections? - Microsoft Entra ID Protection](https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-risks) · Documentación · Oficial · Nuevo · oct 2026. Catálogo de referencia de las detecciones de riesgo de usuario y de inicio de sesión (riskEventType, tiempo real vs. fuera de línea y requisito de licencia) como Password spray, Anomalous token, Attacker in the Middle o Suspicious credential addition.
- [Microsoft Entra ID Protection risk-based access policies](https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-policies) · Documentación · Oficial. Explica las condiciones de riesgo de usuario y de inicio de sesión en Acceso condicional y el control 'Require risk remediation' que adapta la remediación a usuarios con contraseña, sin contraseña o con dispositivo agregado por un atacante.
- [What is Microsoft Entra ID Protection?](https://learn.microsoft.com/en-us/entra/id-protection/overview-identity-protection) · Documentación · Oficial. Visión general de ID Protection: detección, investigación (informes de detecciones, inicios de sesión y usuarios riesgosos), remediación automática o manual, exportación a SIEM y roles requeridos.
- [Configure and enable risk policies (Risk policies - Microsoft Entra ID Protection)](https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-configure-risk-policies) · Documentación · Oficial · 28 abr 2026. Guía oficial para crear políticas de riesgo de usuario y de inicio de sesión en Acceso condicional (recomendación: 'Require risk remediation' para riesgo de usuario alto y MFA para riesgo de inicio de sesión medio/alto) y para migrar las políticas heredadas de ID Protection.
- [Securing workload identities with Microsoft Entra ID Protection](https://learn.microsoft.com/en-us/entra/id-protection/concept-workload-identity-risk) · Documentación · Oficial · 6 ago 2025. Explica las detecciones de riesgo para service principals (credenciales filtradas, actividad anómala, tráfico API sospechoso, aplicaciones maliciosas) y cómo investigarlas y remediarlas.
- [Risk detection types and levels - Microsoft Entra ID Protection](https://learn.microsoft.com/en-us/entra/id-protection/concept-risk-detection-types) · Documentación · Oficial. Describe los niveles de riesgo (bajo, medio, alto), la diferencia entre detecciones en tiempo real y fuera de línea y cuánto tardan en aparecer en los informes.
- [Require remediation for risky users (Conditional Access policy)](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-risk-based-user) · Documentación · Oficial · 24 mar 2026. Paso a paso para desplegar en modo solo informe la política de Acceso condicional que exige remediación de riesgo de usuario alto con exclusión de cuentas de emergencia.
- [User self-remediation with Microsoft Entra ID Protection](https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-user-experience) · Documentación · Oficial · 25 mar 2026. Muestra la experiencia del usuario final al auto-remediar riesgo (MFA, cambio seguro de contraseña, remediación adaptativa) y el caso del técnico de alto riesgo de un MSP/CSP.

### Comunidad: blogs, libros, newsletters y eventos

- [Entra ID – Sam's Corner (Sami Lamppu)](https://samilamppu.com/category/entra-id/) · Blog · MVP · Legado aún útil · Sami Lamppu · Sam's Corner · 20 oct 2024. Categoría de Entra ID del blog de Sami Lamppu con 'Entra ID Protection – Remediate User Risks from Hybrid Users' y la retrospectiva del Entra ID Attack & Defense Playbook. *Nota:* Contenido 2023-2024 aún útil para remediación de riesgo en usuarios híbridos; considerar el retiro de políticas heredadas (oct-2026) al aplicarlo. MVP (Security Copilot, SIEM & XDR) verificado en perfil MVP

**Manos a la obra**

1. `Laboratorio` Crea CA06 (riesgo de inicio de sesión medio o alto) y CA07 (riesgo de usuario alto con «Require risk remediation») en solo informe, con exclusión de las cuentas de emergencia, y revisa su impacto durante una semana ([configurar políticas de riesgo](https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-configure-risk-policies)).
2. `Laboratorio parcial` Simula detecciones de riesgo (por ejemplo, navegador Tor o propiedades desconocidas) con un usuario de prueba y sigue la detección hasta el informe. Limitación: solo algunas detecciones se pueden simular ([simular riesgo](https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-simulate-risk)).
3. `Laboratorio` Lista con Microsoft Graph PowerShell los usuarios riesgosos (`Get-MgRiskyUser`), confirma o descarta el riesgo de un usuario de prueba y documenta qué rol usaste ([visión general de ID Protection](https://learn.microsoft.com/en-us/entra/id-protection/overview-identity-protection)).
4. `Laboratorio` Recorre como usuario la autorremediación (MFA y cambio seguro de contraseña) y redacta la comunicación para la mesa de ayuda ([experiencia del usuario](https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-user-experience)).
5. `Solo producción` Verifica que tu tenant real tenga políticas de acceso condicional basadas en riesgo que reemplacen a las heredadas retiradas el 1 de octubre de 2026, y mide los usuarios de riesgo alto sin remediar. Cómo hacerlo seguro: solo informe primero, grupo piloto, exclusión de las cuentas de emergencia y revisión diaria de los informes con Security Reader.

<a id="m3"></a>

## M3 · Privileged Identity Management: roles, grupos, aprobaciones y alertas

*L300 · ~8 h · Origen: SC-300 · Plan and automate identity governance (PIM)*

**Privileged Identity Management (PIM)** convierte los privilegios permanentes en privilegios justo a tiempo. Un administrador recibe una asignación **elegible** y, cuando la necesita, la activa por un tiempo acotado —de 1 a 24 horas— con MFA, justificación, aprobación y, en el diseño recomendado, **contexto de autenticación** con una fortaleza resistente al phishing. Funciona para roles de Entra, roles de Azure y grupos: **PIM for Groups**, que hasta enero de 2023 se llamaba Privileged Access Groups.

Las buenas prácticas son claras: cero asignaciones activas permanentes, salvo las dos cuentas de emergencia; menos de cinco Global Administrators y menos de diez asignaciones privilegiadas; grupos asignables a roles con aprobación cuando un grupo otorga roles de Entra. Los service principals no pueden ser elegibles. Y un detalle de licencias que conviene conocer: si la licencia de PIM vence, las asignaciones elegibles se eliminan y las activas temporales pasan a permanentes.

Completan el módulo las **alertas de seguridad** —roles sin MFA en la activación, administradores que no usan sus roles, cuentas obsoletas o asignaciones hechas fuera de PIM—, las revisiones de acceso de roles y una novedad que conecta con el track de agentes: PIM ya permite seleccionar identidades de agente como destinatarias de roles, algo que conviene restringir con criterio ([X3](04_Nivel_4_Identidad_para_agentes_de_IA.md#x3)).

**Por qué importa**

Las cuentas con privilegios permanentes son el objetivo número uno de un atacante. Con PIM, un token robado de un administrador vale mucho menos: el rol no está activo, activarlo exige autenticación resistente y todo queda auditado. Métricas: asignaciones permanentes activas (meta: solo emergencia), número de Global Administrators, activaciones con aprobación y alertas de PIM abiertas.

**Qué vas a lograr**

- Diseñar asignaciones elegibles y activas con duración, aprobación y justificación.
- Exigir contexto de autenticación y fortalezas en la activación de roles.
- Usar PIM for Groups con grupos asignables a roles.
- Configurar y atender las alertas de seguridad de PIM para roles de Entra y de Azure.
- Planificar revisiones de acceso periódicas de roles privilegiados.

> **Consejo Ninja.** Configura cada rol con una duración máxima de activación de 1 a 24 horas y, en los privilegiados, «On activation, require Conditional Access authentication context» con una fortaleza resistente al phishing; necesitas al menos Privileged Role Administrator ([configuración de roles](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-how-to-change-default-settings)).

> **Atención.** Si la licencia de PIM (P2 o ID Governance) vence, las asignaciones elegibles se eliminan y las activas temporales pasan a permanentes: vigila las renovaciones ([licencias de ID Governance](https://learn.microsoft.com/en-us/entra/id-governance/licensing-fundamentals)). Los service principals no pueden ser elegibles, solo activos con límite de tiempo ([plan de despliegue](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-deployment-plan)).

> **Qué cambió.** La alerta de cuentas obsoletas en roles privilegiados ya no usa la fecha de cambio de contraseña, sino los días sin inicio de sesión (1 a 365). En roles de Azure, la alerta de roles asignados fuera de PIM solo se dispara a nivel de suscripción ([alertas de roles de Entra](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-how-to-configure-security-alerts), [alertas de roles de Azure](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-resource-roles-configure-alerts)).

> **Novedad.** PIM ya permite seleccionar identidades de agente como destinatarias de roles; una asignación no puede durar menos de 5 minutos. Úsalo con criterio: la mayoría de los agentes no necesita roles de directorio ([asignar roles en PIM](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-how-to-add-role-to-user)).

**¿Tienes poco tiempo?**

- [What is Microsoft Entra Privileged Identity Management?](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-configure) · Documentación
- [Configure Microsoft Entra role settings in Privileged Identity Management](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-how-to-change-default-settings) · Documentación
- [Privileged Identity Management (PIM) for Groups](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/concept-pim-for-groups) · Documentación
- [Privileged Identity Management (PIM) | SC-300 | Episode 24](https://www.youtube.com/watch?v=odJLJH8jfTU) · Video

### Documentación, cursos y credenciales

- [Best practices for Microsoft Entra roles](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/best-practices) · Documentación · Oficial · Nuevo · 1 jun 2026. Diez buenas prácticas de RBAC en Entra: menor privilegio, PIM justo a tiempo, MFA para administradores, revisiones de acceso, menos de 5 Global Admins, menos de 10 asignaciones privilegiadas, grupos y cuentas nativas de nube.
- [Privileged Identity Management (PIM) for Groups](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/concept-pim-for-groups) · Documentación · Oficial. Explica cómo PIM for Groups otorga membresía o propiedad justo a tiempo de grupos de seguridad o de Microsoft 365 con aprobación, MFA y duración máxima, y su relación con los grupos asignables a roles.
- [Configure security alerts for Microsoft Entra roles in Privileged Identity Management](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-how-to-configure-security-alerts) · Documentación · Oficial. Lista las alertas de seguridad de PIM para roles de Entra (roles sin MFA en activación, administradores que no usan sus roles, cuentas obsoletas en roles privilegiados, asignaciones fuera de PIM) con su corrección y prevención.
- [What is Microsoft Entra Privileged Identity Management?](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-configure) · Documentación · Oficial. Visión general de PIM: activación justo a tiempo y con aprobación, asignaciones elegibles/activas y temporales, MFA y justificación, notificaciones, revisiones de acceso y auditoría para roles de Entra, Azure y PIM for Groups.
- [Configure Microsoft Entra role settings in Privileged Identity Management](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-how-to-change-default-settings) · Documentación · Oficial. Cómo configurar por rol la duración máxima de activación (1-24 h), MFA, contexto de autenticación de Acceso condicional, justificación, aprobación y notificaciones en PIM.
- [Plan a Privileged Identity Management deployment](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-deployment-plan) · Documentación · Oficial. Plan de despliegue de PIM: tipos de asignación, menor privilegio, pruebas y reversión, y diseño para roles de Entra, roles de Azure y PIM for Groups.
- [Assign Microsoft Entra roles in Privileged Identity Management](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-how-to-add-role-to-user) · Documentación · Oficial. Procedimiento para crear asignaciones elegibles o activas (permanentes o con fecha) de roles de Entra en PIM, incluidas asignaciones con ámbito de unidad administrativa y vía Graph.
- [Configure security alerts for Azure roles in Privileged Identity Management](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-resource-roles-configure-alerts) · Documentación · Oficial · 23 abr 2026. Describe las alertas de PIM para roles de Azure (demasiados propietarios, propietarios permanentes, roles duplicados y roles asignados fuera de PIM) y cómo ajustarlas.

### Webinars, videos y podcasts

- [Privileged Identity Management (PIM) | SC-300 | Episode 24](https://www.youtube.com/watch?v=odJLJH8jfTU) · Video · Oficial · Microsoft Learn (YouTube) · ene 2026. Episodio de la serie oficial SC-300 que cubre estrategia de acceso privilegiado, configuración de PIM para roles de Entra y Azure, solicitudes, aprobación y cuentas de emergencia.
- [Microsoft Entra on Microsoft Mechanics (YouTube playlist)](https://www.youtube.com/playlist?list=PLXtHYVsvn_b_YGak6Ol8Z-HrNjXW7Zm-n) · Video · Oficial · Legado aún útil · Microsoft Mechanics · 18 nov 2025. Lista oficial de demos de Microsoft Mechanics sobre Entra: Entra Suite, automatización de altas/bajas con Lifecycle Workflows, ITDR de on-prem a la nube y el agente de optimización de Acceso condicional. *Nota:* Varios videos son de 2023-2024 (legacy-still-valid: algunos nombres de portal cambiaron); última actualización de la lista 18-nov-2025

**Manos a la obra**

1. `Laboratorio` Haz elegible a un usuario de prueba para User Administrator con aprobación, justificación, MFA y contexto de autenticación; actívalo y revisa la auditoría de la activación ([configuración de roles en PIM](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-how-to-change-default-settings)).
2. `Laboratorio` Crea un grupo asignable a roles, gestiónalo con PIM for Groups con aprobación, asígnale un rol de Entra y programa una revisión de acceso del rol ([PIM for Groups](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/concept-pim-for-groups)).
3. `Laboratorio` Configura las alertas de seguridad de PIM y provoca una (por ejemplo, una asignación hecha fuera de PIM) para ver su corrección ([alertas de seguridad](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-how-to-configure-security-alerts)).
4. `Laboratorio` Crea una asignación elegible con ámbito de unidad administrativa y verifica que solo aplica a los objetos de esa unidad ([asignar roles en PIM](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-how-to-add-role-to-user)).
5. `Solo producción` Convierte las asignaciones permanentes de tu tenant en elegibles, por oleadas. Cómo hacerlo seguro: empieza por roles de bajo impacto, deja las dos cuentas de emergencia como únicas permanentes, designa aprobadores de respaldo, comunica antes y documenta la reversión (reasignar como activa temporal) ([plan de despliegue](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-deployment-plan)).

**¿Quieres profundizar?**

- [Microsoft Entra on Microsoft Mechanics (YouTube playlist)](https://www.youtube.com/playlist?list=PLXtHYVsvn_b_YGak6Ol8Z-HrNjXW7Zm-n) · Video

<a id="m4"></a>

## M4 · Gobernanza de identidades e identidades externas

*L300 · ~12 h · Origen: SC-300 · Plan and automate identity governance; documentación de External ID y organizaciones multitenant*

Gobernar es asegurar que cada persona tenga el acceso correcto, durante el tiempo correcto, y poder demostrarlo. **Entitlement management** agrupa recursos en catálogos y **paquetes de acceso** con aprobación, expiración y separación de funciones; las **revisiones de acceso** certifican periódicamente grupos, aplicaciones, paquetes y roles; y **Lifecycle Workflows** automatizan altas, cambios y bajas (joiner, mover, leaver) a partir de atributos de RR. HH., como la fecha de ingreso.

Licencias: las funciones que eran GA en P2 siguen en Microsoft 365 E5, pero Microsoft no agregará funciones IGA nuevas a P2. Lifecycle Workflows (hasta 50 flujos y 100 extensiones de tareas), las revisiones asistidas por aprendizaje automático, solo de inactivos o por catálogo, las extensiones personalizadas con Logic Apps, la asignación automática, Account Discovery y la sincronización de grupos entre tenants requieren **ID Governance** (o Entra Suite, incluida en E7). La gobernanza de invitados se factura por usuarios activos mensuales.

La otra mitad son las **identidades externas**: por defecto, B2B collaboration está habilitado y B2B direct connect bloqueado, y no se confía en el MFA ni en las reclamaciones de dispositivo de otro tenant salvo que lo configures. Configurarás el acceso entre tenants, la **sincronización entre tenants** (usuarios con P1; grupos con ID Governance, GA desde junio de 2026) y la organización multitenant, y verás las novedades de 2026: modo what-if en Lifecycle Workflows, solicitudes de paquetes desde ServiceNow y limpieza de invitados sin patrocinador en vista previa.

**Por qué importa**

Sin gobernanza, los accesos se acumulan: personas que cambiaron de área, invitados de proyectos terminados y cuentas de ex empleados. Eso es riesgo y es hallazgo de auditoría. Paquetes de acceso con expiración y revisiones periódicas reducen accesos huérfanos y el esfuerzo de las certificaciones. Métricas: invitados sin patrocinador, accesos vencidos removidos por ciclo y tiempo de alta y de baja.

**Qué vas a lograr**

- Diseñar catálogos y paquetes de acceso con aprobación, expiración y revisión.
- Configurar revisiones de acceso para grupos, aplicaciones, invitados y roles.
- Automatizar altas, cambios y bajas con Lifecycle Workflows y su modo what-if.
- Configurar el acceso entre tenants, B2B y la sincronización entre tenants.
- Distinguir qué funciones requieren ID Governance frente a Entra ID P2.

> **Atención.** Las funciones GA en P2 siguen en Microsoft 365 E5, pero Microsoft no agregará funciones IGA nuevas a P2. Lifecycle Workflows (hasta 50 flujos y 100 extensiones de tareas), las revisiones asistidas por aprendizaje automático, solo de inactivos o por catálogo, las extensiones con Logic Apps, la asignación automática y Account Discovery requieren ID Governance o Entra Suite ([licencias de ID Governance](https://learn.microsoft.com/en-us/entra/id-governance/licensing-fundamentals), [Lifecycle Workflows](https://learn.microsoft.com/en-us/entra/id-governance/what-are-lifecycle-workflows)).

> **Novedad.** Novedades de 2026: sincronización de grupos entre tenants y Account Discovery en GA (junio); modo what-if, cancelación de ejecuciones y tarea de actualización de atributos de Lifecycle Workflows en GA, y limpieza automática de invitados sin patrocinador en vista previa (agosto); y solicitudes de paquetes de acceso desde ServiceNow en GA (octubre) ([junio](https://techcommunity.microsoft.com/blog/microsoft-entra-blog/whats-new-in-microsoft-entra-june-2026/4517885), [agosto](https://techcommunity.microsoft.com/blog/microsoft-entra-blog/whats-new-in-microsoft-entra-august-2026/4545172), [octubre](https://techcommunity.microsoft.com/blog/microsoft-entra-blog/what%E2%80%99s-new-in-microsoft-entra-october-2026/4556460)). Las revisiones centradas en el usuario llegaron a GA en septiembre y requieren ID Governance ([revisiones de acceso](https://learn.microsoft.com/entra/id-governance/access-reviews-overview)).

> **Consejo Ninja.** Por defecto, B2B collaboration está habilitado y B2B direct connect bloqueado, y no se confía en el MFA ni en las reclamaciones de dispositivo de otro tenant salvo que lo configures. La sincronización entre tenants solo sincroniza miembros internos del origen, el destino puede detenerla y necesitas Security Administrator para el acceso entre tenants e Hybrid Identity Administrator para la sincronización ([acceso entre tenants](https://learn.microsoft.com/en-us/entra/external-id/cross-tenant-access-overview), [configurar la sincronización](https://learn.microsoft.com/en-us/entra/identity/multi-tenant-organizations/cross-tenant-synchronization-configure)).

> **Atención.** Investigación comunitaria de septiembre de 2026: un propietario de catálogo de entitlement management puede escalar privilegios si el catálogo contiene recursos sensibles. Trata a esos propietarios como cuentas privilegiadas ([blog de Thomas Naunheim](https://www.cloud-architekt.net/blog/)).

**¿Tienes poco tiempo?**

- [Microsoft Entra ID Governance licensing fundamentals](https://learn.microsoft.com/en-us/entra/id-governance/licensing-fundamentals) · Documentación
- [What is entitlement management? (Entitlement management overview)](https://learn.microsoft.com/entra/id-governance/entitlement-management-overview) · Documentación
- [What are access reviews? (Access reviews overview)](https://learn.microsoft.com/entra/id-governance/access-reviews-overview) · Documentación
- [What are lifecycle workflows? - Microsoft Entra ID Governance](https://learn.microsoft.com/en-us/entra/id-governance/what-are-lifecycle-workflows) · Documentación

### Documentación, cursos y credenciales

- [Microsoft Entra licensing](https://learn.microsoft.com/en-us/entra/fundamentals/licensing) · Documentación · Oficial · Nuevo · Microsoft Learn · 28 jul 2026. Página de referencia que detalla qué funciones de Entra cubren Free, P1, P2, ID Governance, Entra Suite, Agent 365 y Microsoft 365 E5/E7, incluidos roles, unidades administrativas, PIM, acceso condicional y Agent ID.
- [What is cross-tenant synchronization in Microsoft Entra ID?](https://learn.microsoft.com/en-us/entra/identity/multi-tenant-organizations/cross-tenant-synchronization-overview) · Documentación · Oficial. Explica cómo la sincronización entre tenants automatiza el alta, actualización y baja de usuarios y grupos B2B en organizaciones con varios tenants, con configuración push desde el tenant origen.
- [Cross-tenant access overview - Microsoft Entra External ID](https://learn.microsoft.com/en-us/entra/external-id/cross-tenant-access-overview) · Documentación · Oficial. Describe la configuración de acceso entre tenants (entrante/saliente, confianza en MFA y dispositivos de otras organizaciones, B2B direct connect, tenant restrictions y configuración entre nubes).
- [What are lifecycle workflows? - Microsoft Entra ID Governance](https://learn.microsoft.com/en-us/entra/id-governance/what-are-lifecycle-workflows) · Documentación · Oficial. Introduce los flujos de ciclo de vida (joiner, mover, leaver) basados en tareas y condiciones de ejecución sobre atributos como employeeHireDate, extensibles con Logic Apps y gestionables con Security Copilot.
- [What are access reviews? (Access reviews overview)](https://learn.microsoft.com/entra/id-governance/access-reviews-overview) · Documentación · Oficial. Introducción a las revisiones de acceso para grupos, aplicaciones, paquetes de acceso y roles privilegiados, con revisores, recurrencia y aplicación automática de resultados.
- [What is entitlement management? (Entitlement management overview)](https://learn.microsoft.com/entra/id-governance/entitlement-management-overview) · Documentación · Oficial. Introducción a entitlement management: catálogos y paquetes de acceso con aprobación, expiración, separación de funciones y organizaciones conectadas para usuarios internos e invitados.
- [Microsoft Entra ID Governance licensing fundamentals](https://learn.microsoft.com/en-us/entra/id-governance/licensing-fundamentals) · Documentación · Oficial · Microsoft Learn. Explica los seis productos de ID Governance, sus prerrequisitos (P1 o P2) y cómo Entra Suite y Agent 365 aportan capacidades de gobernanza para personas y agentes.
- [Configure cross-tenant synchronization](https://learn.microsoft.com/en-us/entra/identity/multi-tenant-organizations/cross-tenant-synchronization-configure) · Documentación · Oficial. Tutorial de 14 pasos para configurar la sincronización entre tenants (misma nube o entre nubes), con canje automático de invitaciones, ámbito, mapeo de atributos, aprovisionamiento a demanda y monitoreo.
- [Governance and cross-tenant synchronization](https://learn.microsoft.com/en-us/entra/identity/multi-tenant-organizations/cross-tenant-synchronization-governance) · Documentación · Oficial. Muestra cómo combinar sincronización entre tenants con lifecycle workflows, paquetes de acceso con asignación automática y revisiones de acceso para gobernar usuarios de una organización multitenant.
- [Understanding lifecycle workflows](https://learn.microsoft.com/en-us/entra/id-governance/understanding-lifecycle-workflows) · Documentación · Oficial. Detalla las partes de un flujo (información general, tareas, condiciones de ejecución), plantillas, desencadenadores, ámbito, programación, historial y versionado, con el rol Lifecycle Workflows Administrator.
- [Microsoft Entra ID Governance documentation (hub)](https://learn.microsoft.com/en-us/entra/id-governance/) · Documentación · Oficial. Punto de entrada oficial a la documentación de ID Governance: entitlement management, revisiones de acceso, lifecycle workflows, Tenant Governance, PIM y términos de uso, con tutoriales en portal y Graph.
- [What is a multitenant organization in Microsoft Entra ID?](https://learn.microsoft.com/en-us/entra/identity/multi-tenant-organizations/multi-tenant-organization-overview) · Documentación · Oficial. Explica cómo definir un límite de organización multitenant para colaborar en Teams y Viva Engage, diferenciar externos internos de externos ajenos y gobernar pares de tenants con cross-tenant access settings.
- [Multitenant organization capabilities in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/multi-tenant-organizations/overview) · Documentación · Oficial. Compara las capacidades multitenant de Entra (B2B collaboration, B2B direct connect, cross-tenant access settings, sincronización entre tenants, organización multitenant) según escenarios de fusiones, subsidiarias o tenants de prueba.

### Anuncios y blogs oficiales

- [What’s new in Microsoft Entra: October 2026](https://techcommunity.microsoft.com/blog/microsoft-entra-blog/what%E2%80%99s-new-in-microsoft-entra-october-2026/4556460) · Blog oficial · Oficial · Nuevo · Yina Arenas · Microsoft Entra Blog (Tech Community) · 12 oct 2026. Resumen mensual organizado por resultados que destaca la CAE universal con señales de dispositivo, la herramienta guiada de migración de Connect Sync a Cloud Sync (GA) y el acceso B2B con Global Secure Access.
- [Microsoft Entra deep dives: Join our December 15–17 webinar series](https://techcommunity.microsoft.com/blog/microsoft-entra-blog/microsoft-entra-deep-dives-join-our-december-15%E2%80%9317-webinar-series/4448760) · Blog oficial · Empleado de Microsoft · Nuevo · Laura Viarengo · Microsoft Entra Blog (Tech Community) · 4 nov 2026. Anuncia la serie de webinars post-Ignite (15-17 dic 2026) sobre acceso adaptativo sin proliferación de políticas, gobernanza/PIM/Tenant Governance/Backup and Recovery y seguridad de identidades de agentes.
- [What's New in Microsoft Entra: August 2026](https://techcommunity.microsoft.com/blog/microsoft-entra-blog/whats-new-in-microsoft-entra-august-2026/4545172) · Blog oficial · Oficial · Nuevo · Yina Arenas · Microsoft Entra Blog (Tech Community) · 10 ago 2026. Resumen mensual con la sincronización de dispositivos de AD mediante Cloud Sync (preview), la reescritura de atributos de Exchange Online y el control de solicitudes de SSO en Windows.
- [What's New in Microsoft Entra: June 2026](https://techcommunity.microsoft.com/blog/microsoft-entra-blog/whats-new-in-microsoft-entra-june-2026/4517885) · Blog oficial · Oficial · Nuevo · Martin Coetzer · Microsoft Entra Blog (Tech Community) · 1 jun 2026. Resumen mensual que anuncia MFA resistente al phishing en escritorios Linux, autenticación preferida por el sistema para primer y segundo factor y campañas de registro para passkeys.

### Webinars, videos y podcasts

- [Microsoft Entra Suite hands-on tour of identity and network access protections](https://www.youtube.com/watch?v=81rnazsINB4) · Video · Empleado de Microsoft · Nuevo · John Damon · Microsoft Mechanics (YouTube) · 15 jul 2026. Demo de Mechanics que recorre Entra Suite (Lifecycle Workflows, Face Check, Global Secure Access, DLP de red y protección contra inyección de prompts) y cómo se obtiene con Microsoft 365 E7.
- [Strengthen governance, privileged access, and resilience across every identity and tenant (Microsoft Entra deep dive webinar)](https://techcommunity.microsoft.com/event/microsoft-security-events/strengthen-governance-privileged-access-and-resilience-across-every-identity-and/4569719) · Webinar · Empleado de Microsoft · Vista previa · Nuevo · Ilya Lushnikov; Hien Nguyen; Yash Singh · Microsoft Security Community (Tech Community events) · 16 dic 2026. Webinar demostrativo post-Ignite sobre novedades de ID Governance, PIM, Tenant Governance y Microsoft Entra Backup and Recovery, con sesión de preguntas al equipo de producto. *Nota:* Evento programado para el 16-dic-2026, 9:00 PT (posterior a la fecha de corte): registrar y revisar la grabación para actualizar M3/M4/A5 tras Ignite

**Manos a la obra**

1. `Laboratorio` Crea un catálogo y un paquete de acceso para los invitados de un proyecto, con aprobación, expiración a 90 días y revisión trimestral ([entitlement management](https://learn.microsoft.com/entra/id-governance/entitlement-management-overview)).
2. `Laboratorio` Configura una revisión de acceso de un grupo con aplicación automática de resultados y un revisor de prueba; documenta la decisión y su efecto ([revisiones de acceso](https://learn.microsoft.com/entra/id-governance/access-reviews-overview)).
3. `Laboratorio parcial` Activa la prueba de ID Governance y crea un flujo de alta y otro de baja en Lifecycle Workflows a partir de employeeHireDate; ejecútalos en modo what-if. Limitación: la prueba se activa una sola vez por tenant ([Lifecycle Workflows](https://learn.microsoft.com/en-us/entra/id-governance/what-are-lifecycle-workflows)).
4. `Laboratorio parcial` Configura la sincronización entre tenants de usuarios y aprovisiona a demanda un usuario de prueba. Limitación: necesitas dos tenants de prueba y los grupos requieren ID Governance ([configurar la sincronización](https://learn.microsoft.com/en-us/entra/identity/multi-tenant-organizations/cross-tenant-synchronization-configure)).
5. `Laboratorio` Revisa la configuración predeterminada de acceso entre tenants y documenta con qué socio confiarías en el MFA y en las reclamaciones de dispositivo, y por qué ([acceso entre tenants](https://learn.microsoft.com/en-us/entra/external-id/cross-tenant-access-overview)).
6. `Solo producción` Identifica en tu tenant los invitados sin patrocinador y sin actividad y diseña su limpieza. Cómo hacerlo seguro: inventario con Global Reader, revisión de acceso con los dueños de negocio antes de borrar y un período de deshabilitación previo.

**¿Quieres profundizar?**

- [Microsoft Entra Suite hands-on tour of identity and network access protections](https://www.youtube.com/watch?v=81rnazsINB4) · Video
- [Strengthen governance, privileged access, and resilience across every identity and tenant (Microsoft Entra deep dive webinar)](https://techcommunity.microsoft.com/event/microsoft-security-events/strengthen-governance-privileged-access-and-resilience-across-every-identity-and/4569719) · Webinar

<a id="m5"></a>

## M5 · Aplicaciones empresariales y gobierno del consentimiento

*L300 · ~8 h · Origen: SC-300 · Plan and implement workload identities; Ninja de Defender for Cloud Apps (App governance)*

Cada aplicación integrada a Entra es una puerta. El **registro de aplicación** define la app y el **service principal** —la aplicación empresarial— es su instancia en tu tenant, con sus permisos, propietarios y credenciales. Los permisos llegan por **consentimiento**: Microsoft recomienda permitir el consentimiento de usuarios solo para apps de editores verificados y permisos de bajo riesgo, y canalizar el resto por el **flujo de consentimiento de administrador**, con revisores, notificaciones y expiración de solicitudes.

El endurecimiento se completa con las **políticas de administración de aplicaciones** —bloquear secretos, limitar la vida de certificados y contraseñas, bloquear apps multitenant o de cuentas personales y exigir autoridades de certificación de confianza—, que según la FAQ de Workload ID no requieren licencia premium, y con el **bloqueo de propiedades de instancia**, habilitado por defecto en las apps nuevas desde junio de 2026 para impedir que alguien agregue credenciales a tu app en otro tenant.

Para vigilar apps OAuth, **App governance** de Defender for Cloud Apps está incluido en Microsoft 365 E5, pero **no está disponible si la dirección de facturación está en México** (ni en Singapur, Polonia, Italia, Qatar, Israel, España o Taiwán). Para esos clientes verás alternativas con registros de Entra, búsqueda avanzada y el playbook oficial de consentimiento ([A5](03_Nivel_3_Avanzado.md#a5)).

**Por qué importa**

El consentimiento ilícito da a un atacante acceso persistente al correo y los archivos sin robar contraseñas, y sobrevive a un cambio de contraseña. Controlar quién consiente, a qué apps y con qué credenciales reduce esa superficie. Métricas: apps con permisos de alto riesgo, apps con secretos frente a certificados o federación y solicitudes de consentimiento atendidas en plazo.

**Qué vas a lograr**

- Configurar el consentimiento de usuarios y el flujo de consentimiento de administrador.
- Aplicar políticas de administración de aplicaciones y verificar el bloqueo de propiedades de instancia.
- Inventariar apps y permisos de riesgo con Microsoft Graph PowerShell.
- Evaluar App governance y sus alternativas cuando no está disponible por país de facturación.

> **Atención.** Para clientes de MCSA: App governance se incluye con Defender for Cloud Apps en Microsoft 365 E5, pero **no está disponible si la dirección de facturación está en México** (ni en Singapur, Polonia, Italia, Qatar, Israel, España o Taiwán), y su activación puede tardar hasta 10 horas ([activar App governance](https://learn.microsoft.com/en-us/defender-cloud-apps/app-governance-get-started), [FAQ](https://learn.microsoft.com/en-us/defender-cloud-apps/app-governance-faq)).

> **Qué cambió.** Desde junio de 2026, el bloqueo de propiedades de instancia viene habilitado por defecto en las apps nuevas y aplica a apps single-tenant y multitenant; protege las credenciales de firma y verificación y el tokenEncryptionKeyId para que nadie los agregue en otro tenant ([bloqueo de propiedades de instancia](https://learn.microsoft.com/en-us/entra/identity-platform/howto-configure-app-instance-property-locks)).

> **Consejo Ninja.** En el flujo de consentimiento del administrador, solo los Global Administrators pueden aprobar apps que piden permisos de aplicación de Microsoft Graph; designar revisores no les eleva privilegios y el flujo puede tardar hasta una hora en activarse ([flujo de consentimiento](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/configure-admin-consent-workflow)). Configurar el consentimiento de usuarios requiere Privileged Role Administrator ([consentimiento de usuarios](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/configure-user-consent)).

> **Novedad.** Las políticas de administración de apps ya permiten bloquear apps multitenant y de cuentas personales, con exclusiones por atributos de seguridad personalizados, y bloquear secretos en service principals con la política predeterminada vía Graph ([apps multitenant y de consumidor](https://janbakker.tech/block-or-limit-multi-tenant-and-consumer-applications-in-entra-id/), [service principals sin secretos](https://janbakker.tech/your-service-principals-probably-dont-need-secrets/)). Según la FAQ de Workload ID, son una función gratuita.

**¿Tienes poco tiempo?**

- [Configure how users consent to applications](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/configure-user-consent) · Documentación
- [Configure the admin consent workflow](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/configure-admin-consent-workflow) · Documentación
- [How to configure app instance property lock in your applications](https://learn.microsoft.com/en-us/entra/identity-platform/howto-configure-app-instance-property-locks) · Documentación
- [Turn on app governance in Microsoft Defender for Cloud Apps](https://learn.microsoft.com/en-us/defender-cloud-apps/app-governance-get-started) · Documentación

### Documentación, cursos y credenciales

- [How to configure app instance property lock in your applications](https://learn.microsoft.com/en-us/entra/identity-platform/howto-configure-app-instance-property-locks) · Documentación · Oficial · Nuevo · 2 oct 2026. Explica cómo bloquear propiedades sensibles del service principal (credenciales de firma y verificación, tokenEncryptionKeyId) para impedir que un atacante agregue credenciales en otros tenants.
- [App governance in Microsoft Defender for Cloud Apps and Microsoft Defender XDR](https://learn.microsoft.com/en-us/defender-cloud-apps/app-governance-manage-app-governance) · Documentación · Oficial · Nuevo · 29 sep 2026. Describe App governance: visibilidad, políticas, detección de amenazas y remediación para apps OAuth registradas en Entra ID, Google y Salesforce, con alertas integradas en Defender XDR.
- [Turn on app governance in Microsoft Defender for Cloud Apps](https://learn.microsoft.com/en-us/defender-cloud-apps/app-governance-get-started) · Documentación · Oficial · Nuevo · 11 ago 2026. Requisitos, roles y pasos para activar App governance desde la configuración de Defender XDR, incluido el conector de Microsoft 365 para hunting de actividades OAuth.
- [Configure how users consent to applications](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/configure-user-consent) · Documentación · Oficial. Cómo restringir o deshabilitar el consentimiento de usuarios a aplicaciones desde el portal, Graph PowerShell o Graph API, entendiendo authorizationPolicy y las directivas de concesión de permisos.
- [Configure restrictions on how applications can be configured (app management policies)](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/configure-app-management-policies) · Documentación · Oficial. Guía para aplicar políticas de administración de aplicaciones que bloquean secretos, limitan la vida de certificados y contraseñas, bloquean apps multitenant/consumidor y exigen CA de confianza.
- [Microsoft Entra Conditional Access for workload identities](https://learn.microsoft.com/en-us/entra/identity/conditional-access/workload-identity) · Documentación · Oficial. Cómo crear políticas de Acceso condicional basadas en ubicación o riesgo para service principals de un solo tenant, con modo solo informe y revisión en los registros de inicio de sesión.
- [Configure the admin consent workflow](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/configure-admin-consent-workflow) · Documentación · Oficial · 19 ene 2026. Cómo habilitar el flujo de solicitud de consentimiento de administrador con revisores, notificaciones, recordatorios y expiración de solicitudes, también configurable vía adminConsentRequestPolicy en Graph.
- [Frequently asked questions about Microsoft Entra Workload ID](https://learn.microsoft.com/en-us/entra/workload-id/workload-identities-faqs) · Documentación · Oficial · 18 mar 2025. Aclara qué funciones de identidades de carga son gratuitas (políticas de administración de apps, identidades administradas, federación) y cuáles requieren Workload ID Premium (Acceso condicional y ID Protection para workload identities, revisiones de acceso de service principals privilegiados, recomendaciones de salud de apps).
- [Frequently asked questions about app governance](https://learn.microsoft.com/en-us/defender-cloud-apps/app-governance-faq) · Documentación · Oficial. Responde qué apps cubre App governance, cómo se obtiene, qué detecta (alertas de amenaza y de política), acciones de desactivación e integración con Defender XDR y Sentinel.
- [Microsoft Defender for Cloud Apps Ninja Training](https://aka.ms/MDCANinjaTraining) · Curso · Oficial · Ninja original · Microsoft Tech Community. Ruta Ninja oficial de Defender for Cloud Apps que incluye App governance, políticas, controles de sesión y detección de amenazas, con verificación de conocimientos y certificado. *Nota:* No existe (a la fecha) un Ninja oficial dedicado a Entra; este Ninja cubre la parte de gobierno de apps OAuth del módulo M5. Enlace obtenido de un listado comunitario de Ninjas

### Comunidad: blogs, libros, newsletters y eventos

- [Your service principals probably don't need secrets](https://janbakker.tech/your-service-principals-probably-dont-need-secrets/) · Blog · MVP · Jan Bakker · JanBakker.tech · 20 abr 2026. Muestra cómo bloquear la adición de secretos a service principals mediante la política de administración de apps por defecto en Graph (servicePrincipalRestrictions) y cómo revertirlo.
- [Block or limit multi-tenant and consumer applications in Entra ID](https://janbakker.tech/block-or-limit-multi-tenant-and-consumer-applications-in-entra-id/) · Blog · MVP · Jan Bakker · JanBakker.tech · 15 abr 2026. Explica las nuevas restricciones de Application policies para bloquear apps multitenant y apps de cuentas personales, con exclusiones basadas en atributos de seguridad personalizados.

**Manos a la obra**

1. `Laboratorio` Restringe el consentimiento de usuarios a editores verificados y permisos de bajo riesgo, habilita el flujo de consentimiento del administrador con dos revisores y aprueba la solicitud de una app de prueba ([consentimiento de usuarios](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/configure-user-consent), [flujo de consentimiento](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/configure-admin-consent-workflow)).
2. `Laboratorio` Respalda la política de administración de apps actual, aplica una que bloquee secretos nuevos y limite la vida de los certificados, y comprueba que agregar un secreto falla ([políticas de administración de apps](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/configure-app-management-policies)).
3. `Laboratorio` Crea una app nueva y verifica que el bloqueo de propiedades de instancia está habilitado por defecto ([bloqueo de propiedades](https://learn.microsoft.com/en-us/entra/identity-platform/howto-configure-app-instance-property-locks)).
4. `Laboratorio` Inventaria con Microsoft Graph PowerShell las apps con permisos de aplicación de alto riesgo (por ejemplo, de lectura y escritura de correo o del directorio) y las que usan secretos en lugar de certificados o federación. Entregable: lista priorizada con dueño.
5. `Laboratorio parcial` Activa App governance y revisa sus políticas predefinidas. Limitación: no está disponible con facturación en México y otros países, y la activación puede tardar hasta 10 horas; en producción, solo alertas, sin «Disable app» hasta validar ([activar App governance](https://learn.microsoft.com/en-us/defender-cloud-apps/app-governance-get-started)).
6. `Solo producción` Si tu facturación excluye App governance, arma la alternativa con consultas sobre la auditoría de consentimientos y el [playbook de concesión ilícita de consentimiento](https://learn.microsoft.com/en-us/security/zero-trust/security-operations-playbook-app-consent). Cómo hacerlo seguro: consultas de solo lectura y revisión con los dueños de las apps antes de revocar permisos.

**¿Quieres profundizar?**

- [Your service principals probably don't need secrets](https://janbakker.tech/your-service-principals-probably-dont-need-secrets/) · Blog

<a id="m6"></a>

## M6 · Monitoreo, registros y salud de identidad

*L300 · ~8 h · Origen: SC-300 (monitoreo e informes) y Zero Trust Workshop · Identidad (operaciones de seguridad de identidad)*

Entra registra inicios de sesión interactivos y no interactivos, de service principals y de identidades administradas, además de auditoría, aprovisionamiento y riesgo. Sin exportar, esos registros se consultan **30 días** en el portal o por Graph. Para conservarlos más tiempo, una **configuración de diagnóstico** los envía a Log Analytics o Microsoft Sentinel —al hacerlo se habilita el conector de Entra en Sentinel—, a una cuenta de almacenamiento o a Event Hubs para otro SIEM. Los registros de inicio de sesión en Sentinel requieren P1 o P2.

En 2026 aparecieron fuentes nuevas: **AADGraphActivityLogs**, con la actividad de la API heredada AAD Graph, disponible para todos los clientes desde mayo, y en la búsqueda avanzada de Defender la tabla **EntraIdSignInEvents**, que reemplazó a AADSignInEventsBeta el 19 de octubre de 2026 y requiere P2. La tabla SigninLogs ya incluye una columna para los inicios de sesión de agentes. Aprenderás a consultar todo con KQL y a estimar costos midiendo uno o dos días de ingesta.

La salud del tenant se mide con **Identity Secure Score** (gratuito, recalculado cada 24 horas y ahora con acciones de AD local y AD CS), las **recomendaciones** diarias de Entra y las **alertas de monitoreo de salud**, en vista previa, que detectan anomalías en MFA, acceso condicional, dispositivos administrados o SAML. Workbooks como el de información de acceso condicional completan el tablero.

**Por qué importa**

No puedes defender ni auditar lo que no registras. Con 30 días de retención por defecto, un incidente descubierto tarde se queda sin evidencia. Un diseño de registros con retención y costo controlados es la base de ITDR, de la respuesta a incidentes y de las auditorías. Métricas: fuentes de Entra conectadas, días de retención, alertas de salud atendidas y costo mensual por GB.

**Qué vas a lograr**

- Enviar los registros de Entra a Log Analytics o Sentinel con una configuración de diagnóstico.
- Consultar inicios de sesión y auditoría con KQL, incluidas las tablas de búsqueda avanzada de Defender.
- Estimar y optimizar el costo de ingesta de los registros de identidad.
- Usar Identity Secure Score, recomendaciones y alertas de salud para operar el tenant.

> **Novedad.** Fuentes nuevas de 2026: AADGraphActivityLogs (la API heredada AAD Graph) disponible para todos desde mayo, con un retraso mediano de unos 7 minutos ([AADGraphActivityLogs](https://cloudbrothers.info/en/aadgraphactivitylogs/)); EntraIdSignInEvents, que reemplazó a AADSignInEventsBeta en la búsqueda avanzada el 19 de octubre de 2026 y requiere P2 ([EntraIdSignInEvents](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-entraidsigninevents-table)); y una columna de agente en SigninLogs ([SigninLogs](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/signinlogs)).

> **Atención.** Sin exportar, los registros se consultan solo 30 días. Al crear la configuración de diagnóstico hacia Log Analytics se habilita automáticamente el conector de Entra en Sentinel; necesitas al menos Security Administrator. Mide uno o dos días de ingesta antes de estimar costos y usa transformaciones para reducirlos ([opciones de integración](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-log-monitoring-integration-options-considerations), [integrar con Azure Monitor](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-integrate-activity-logs-with-azure-monitor-logs)).

> **Atención.** Las alertas de monitoreo de salud siguen en vista previa: exigen P1 o P2 que no sea de prueba y al menos 100 usuarios activos al mes, y un tenant nuevo tarda unos 30 días en generarlas; Reports Reader es el rol mínimo para verlas ([alertas de salud](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-investigate-health-scenario-alerts)). Su API está en Graph beta, sin soporte productivo ([recurso de alertas](https://learn.microsoft.com/en-us/graph/api/resources/healthmonitoring-alert?view=graph-rest-beta)).

> **Consejo Ninja.** Las recomendaciones de Entra se procesan cada día (pueden tardar hasta 72 horas), algunas requieren P2 y se consultan por Graph con el permiso DirectoryRecommendations.Read.All ([recomendaciones](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/overview-recommendations)).

**¿Tienes poco tiempo?**

- [Integrate Microsoft Entra logs with Azure Monitor logs](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-integrate-activity-logs-with-azure-monitor-logs) · Documentación
- [What are the Microsoft Entra activity log integration options?](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-log-monitoring-integration-options-considerations) · Documentación
- [Now You See Me: AADGraphActivityLogs](https://cloudbrothers.info/en/aadgraphactivitylogs/) · Blog
- [What is Identity Secure Score?](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-identity-secure-score) · Documentación

### Documentación, cursos y credenciales

- [Integrate Microsoft Entra logs with Azure Monitor logs](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-integrate-activity-logs-with-azure-monitor-logs) · Documentación · Oficial · Nuevo · 15 jun 2026. Pasos para crear una configuración de diagnóstico que envíe registros de inicio de sesión, auditoría, aprovisionamiento y riesgo de Entra a un área de trabajo de Log Analytics para consultas KQL, workbooks y alertas.
- [Microsoft Entra releases and announcements (What's new)](https://learn.microsoft.com/en-us/entra/fundamentals/whats-new) · Documentación · Oficial · Microsoft Learn. Registro mensual oficial de novedades, cambios y retiradas de toda la familia Entra de los últimos seis meses, con fuente RSS para suscribirse.
- [What is Identity Secure Score?](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-identity-secure-score) · Documentación · Oficial · Microsoft Learn. Describe la puntuación de seguridad de identidad, recalculada cada 24 horas, y las acciones de mejora incluidas (MFA para roles administrativos, bloqueo de autenticación heredada, PHS si es híbrido, cuentas de Connect, etc.).
- [What are Microsoft Entra recommendations?](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/overview-recommendations) · Documentación · Oficial · Microsoft Learn. Explica las recomendaciones diarias de Entra con plan de acción y recursos impactados, ahora integradas con Identity Secure Score, y los roles de lectura o actualización necesarios.
- [How to investigate Microsoft Entra Health monitoring alerts (Preview)](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-investigate-health-scenario-alerts) · Documentación · Oficial · Vista previa. Guía para investigar alertas de salud del tenant (anomalías en MFA, dispositivos administrados/compatibles, Acceso condicional, SAML) usando métricas, entidades afectadas, registros y diagnóstico de inicio de sesión. *Nota:* En preview a la fecha: requiere P1/P2 no trial y al menos 100 usuarios activos mensuales para alertas; tenants nuevos pueden tardar ~30 días en generar alertas; Reports Reader es el rol mínimo para ver
- [What are the Microsoft Entra activity log integration options?](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-log-monitoring-integration-options-considerations) · Documentación · Oficial. Compara opciones para conservar y analizar registros de Entra (portal/Graph hasta 30 días, cuenta de almacenamiento, Event Hubs hacia SIEM de terceros, Log Analytics/Sentinel) con consideraciones de costo.
- [alert resource type (healthMonitoring) - Microsoft Graph beta](https://learn.microsoft.com/en-us/graph/api/resources/healthmonitoring-alert?view=graph-rest-beta) · Documentación · Oficial · Vista previa · Nuevo · 19 ago 2026. Referencia del recurso de alertas de salud de Entra en Graph beta con tipos de alerta (mfaSignInFailure, conditionalAccessBlockedSignIn, samlSignInFailure, conectividad de Global Secure Access) y estados. *Nota:* API beta (sin soporte productivo); admite notificaciones de cambio para integrar con automatizaciones

### Comunidad: blogs, libros, newsletters y eventos

- [Now You See Me: AADGraphActivityLogs](https://cloudbrothers.info/en/aadgraphactivitylogs/) · Blog · MVP · Nuevo · Fabian Bader · Cloudbrothers · 10 may 2026. Presenta la nueva fuente AADGraphActivityLogs (Azure AD Graph) habilitable desde la configuración de diagnóstico, su esquema y consultas KQL para detectar reconocimiento con ROADtools o AADInternals.

**Manos a la obra**

1. `Laboratorio` Crea una configuración de diagnóstico que envíe a Log Analytics los inicios de sesión interactivos y no interactivos, de service principals y de identidades administradas, la auditoría, el aprovisionamiento y los registros de riesgo ([integrar con Azure Monitor](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-integrate-activity-logs-with-azure-monitor-logs)).
2. `Laboratorio` Escribe cinco consultas KQL: autenticación heredada (`SigninLogs` por `ClientAppUsed`), resultados de solo informe, cambios en políticas de acceso condicional (`AuditLogs`), consentimientos a aplicaciones y fallos de MFA por método. Entregable: consultas comentadas en un repositorio.
3. `Laboratorio` Habilita AADGraphActivityLogs y busca patrones de reconocimiento con herramientas como ROADtools o AADInternals usando las consultas del [artículo de Fabian Bader](https://cloudbrothers.info/en/aadgraphactivitylogs/).
4. `Laboratorio` Mide la ingesta de dos días con la tabla `Usage`, proyecta el costo mensual por tabla y propone qué tablas podrían ir a niveles más económicos ([opciones de integración](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-log-monitoring-integration-options-considerations)).
5. `Laboratorio` Revisa Identity Secure Score y las recomendaciones de Entra; marca una acción como «riesgo aceptado» con justificación y otra como planeada con fecha ([Identity Secure Score](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-identity-secure-score)).
6. `Solo producción` Activa las alertas de monitoreo de salud, que exigen P1 o P2 no de prueba y al menos 100 usuarios activos al mes. Cómo hacerlo seguro: rol Reports Reader, notificaciones a un grupo de prueba y umbrales revisados para evitar la fatiga de alertas ([alertas de salud](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-investigate-health-scenario-alerts)).

<a id="m7"></a>

## M7 · Dispositivos e identidad: unión a Entra, cumplimiento de Intune y Platform SSO

*L300 · ~8 h · Origen: Nuevo en esta edición (documentación de dispositivos de Entra e Intune)*

El dispositivo es una señal de identidad. Un equipo puede estar **registrado** en Entra (BYOD), **unido a Entra** (Windows 10 u 11 con TPM 2.0 compatible) o con **unión híbrida** a AD y Entra, que no se admite en controladores de dominio ni en Server Core. El PRT transporta el estado del dispositivo al acceso condicional y, con **Intune** —incluido en Microsoft 365 E3 y E5—, puedes exigir que el dispositivo sea **conforme** con tus políticas antes de conceder acceso.

En macOS, **Platform SSO** ofrece tres métodos —clave en Secure Enclave, tarjeta inteligente o contraseña—, requiere macOS 13 o superior (se recomienda 14) y Company Portal 5.2404.0 o posterior, y se configura con el catálogo de configuración de Intune. La clave de Secure Enclave funciona como credencial de plataforma resistente al phishing. En Windows, la actualización de julio de 2026 dio a los administradores control para aceptar automáticamente las solicitudes de SSO.

También planificarás el despliegue —qué tipo de unión usar en cada escenario y qué endpoints excluir de la inspección TLS— y la limpieza de dispositivos obsoletos, con la eliminación temporal de dispositivos que llegó en vista previa con Entra Backup and Recovery.

**Por qué importa**

Exigir un dispositivo administrado y conforme corta de raíz muchos ataques de robo de credenciales: aunque el atacante tenga la contraseña o la sesión, no tiene el dispositivo. Además, un SSO bien implementado mejora la experiencia del usuario. Métricas: inicios de sesión desde dispositivos conformes, dispositivos obsoletos y Macs con Platform SSO.

**Qué vas a lograr**

- Elegir entre registro, unión a Entra y unión híbrida según el escenario.
- Explicar cómo el PRT lleva el estado del dispositivo al acceso condicional.
- Usar el cumplimiento de Intune como control de acceso condicional.
- Configurar Platform SSO para macOS con Intune.

> **Novedad.** Platform SSO para macOS ofrece tres métodos (clave en Secure Enclave, tarjeta inteligente y contraseña), requiere macOS 13 o superior (se recomienda 14) y Company Portal 5.2404.0 o posterior, y se configura con el catálogo de configuración de Intune, incluido en todos sus planes ([Platform SSO](https://learn.microsoft.com/en-us/entra/identity/devices/macos-psso), [configurar con Intune](https://learn.microsoft.com/en-us/intune/device-configuration/settings-catalog/configure-platform-sso-macos)). El AAGUID de la credencial de plataforma de macOS, útil para restricciones de claves, es 7FD635B3-2EF9-4542-8D9D-164F2C771EFC.

> **Atención.** La guía passwordless etiqueta la credencial de plataforma de macOS como «(preview)» mientras Platform SSO se documenta como soportado: verifica el estado en tu tenant antes de exigirla en una fortaleza ([credencial de plataforma para macOS](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-platform-credential-for-macos)).

> **Consejo Ninja.** Excluye de la inspección TLS los endpoints de registro de dispositivos (enterpriseregistration) y recuerda que la unión híbrida no se admite en controladores de dominio ni en Server Core ([planificar dispositivos](https://learn.microsoft.com/en-us/entra/identity/devices/plan-device-deployment), [unión híbrida](https://learn.microsoft.com/en-us/entra/identity/devices/hybrid-join-plan)).

> **Novedad.** La actualización de julio de 2026 permite a los administradores aceptar automáticamente las solicitudes de SSO en Windows (GA), y desde mayo la eliminación temporal de dispositivos está en vista previa con Backup and Recovery ([novedades de agosto](https://techcommunity.microsoft.com/blog/microsoft-entra-blog/whats-new-in-microsoft-entra-august-2026/4545172), [What's new](https://learn.microsoft.com/en-us/entra/fundamentals/whats-new)).

**¿Tienes poco tiempo?**

- [Plan your Microsoft Entra device deployment](https://learn.microsoft.com/en-us/entra/identity/devices/plan-device-deployment) · Documentación
- [Understanding Primary Refresh Token (PRT)](https://learn.microsoft.com/en-us/entra/identity/devices/concept-primary-refresh-token) · Documentación
- [macOS Platform Single Sign-on (PSSO) overview](https://learn.microsoft.com/en-us/entra/identity/devices/macos-psso) · Documentación
- [Configure Platform SSO for macOS devices in Microsoft Intune](https://learn.microsoft.com/en-us/intune/device-configuration/settings-catalog/configure-platform-sso-macos) · Laboratorio

### Documentación, cursos y credenciales

- [macOS Platform Single Sign-on (PSSO) overview](https://learn.microsoft.com/en-us/entra/identity/devices/macos-psso) · Documentación · Oficial · Microsoft Learn. Describe Platform SSO para macOS con sus tres métodos (clave en Secure Enclave, tarjeta inteligente y contraseña), requisitos (macOS 14 recomendado, Company Portal 5.2404.0+) y uso como credencial resistente al phishing.
- [Understanding Primary Refresh Token (PRT)](https://learn.microsoft.com/en-us/entra/identity/devices/concept-primary-refresh-token) · Documentación · Oficial · Microsoft Learn. Explica qué es el Primary Refresh Token, cómo se emite, usa, renueva, protege con TPM e invalida en Windows, iOS/macOS, Android y Linux, y cuándo obtiene la reclamación de MFA.
- [Plan your Microsoft Entra device deployment](https://learn.microsoft.com/en-us/entra/identity/devices/plan-device-deployment) · Documentación · Oficial · Microsoft Learn. Plan de despliegue que compara registro, unión a Entra y unión híbrida, con partes interesadas, piloto y requisitos de red para el registro de dispositivos.
- [Plan your Microsoft Entra join implementation](https://learn.microsoft.com/en-us/entra/identity/devices/device-join-plan) · Documentación · Oficial · Microsoft Learn. Guía para planificar la unión directa a Entra ID de Windows 10/11, con requisitos de identidad (administrada o federada), aprovisionamiento y acceso condicional.
- [Architecture and authentication flow for macOS Platform SSO with Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/devices/macos-platform-sso-architecture) · Documentación · Oficial · Microsoft Learn. Artículo de arquitectura que explica las responsabilidades de MDM, macOS, el plug-in Enterprise SSO y Entra ID, y cómo se emite el PRT de Platform SSO con claves protegidas en Secure Enclave.
- [Plan your Microsoft Entra hybrid join implementation](https://learn.microsoft.com/en-us/entra/identity/devices/hybrid-join-plan) · Documentación · Oficial · Microsoft Learn. Planificación de la unión híbrida de equipos unidos a AD, con dispositivos soportados, escenarios no soportados, consideraciones de imágenes y estado dual registrado/híbrido.

### Laboratorios, GitHub y herramientas

- [Configure Platform SSO for macOS devices in Microsoft Intune](https://learn.microsoft.com/en-us/intune/device-configuration/settings-catalog/configure-platform-sso-macos) · Laboratorio · Oficial · Microsoft Learn (Intune). Procedimiento paso a paso para configurar Platform SSO con el catálogo de configuración de Intune, desplegar Company Portal, registrar el dispositivo y validar la configuración.
- [Configure Microsoft Entra hybrid join](https://learn.microsoft.com/en-us/entra/identity/devices/how-to-hybrid-join) · Laboratorio · Oficial · Microsoft Learn. Procedimiento para configurar la unión híbrida con Entra Connect en dominios administrados o federados, con requisitos de conectividad y proxy.

**Manos a la obra**

1. `Laboratorio` Une a Entra una VM Windows 11 de laboratorio, inscríbela en Intune, crea una política de cumplimiento y verifica el estado del dispositivo y del PRT con `dsregcmd /status` ([planificar la unión a Entra](https://learn.microsoft.com/en-us/entra/identity/devices/device-join-plan)).
2. `Laboratorio` Despliega CA08 (dispositivo conforme) en solo informe y analiza los resultados por plataforma ([solo informe](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-report-only)).
3. `Laboratorio parcial` Configura Platform SSO con la clave de Secure Enclave en un Mac de prueba inscrito en Intune. Limitación: requiere hardware Apple; en producción, piloto con Company Portal 5.2404.0 o posterior y macOS 14 ([configurar Platform SSO](https://learn.microsoft.com/en-us/intune/device-configuration/settings-catalog/configure-platform-sso-macos)).
4. `Laboratorio` Documenta el árbol de decisión de tu organización: qué equipos van con registro, con unión a Entra o con unión híbrida, y por qué ([planificar dispositivos](https://learn.microsoft.com/en-us/entra/identity/devices/plan-device-deployment)).
5. `Solo producción` Limpia los dispositivos obsoletos de tu tenant. Cómo hacerlo seguro: exporta primero, deshabilita antes de eliminar, acuerda un umbral de inactividad con los dueños y prueba la eliminación temporal (vista previa) solo en un subconjunto.

**¿Quieres profundizar?**

- [Configure Microsoft Entra hybrid join](https://learn.microsoft.com/en-us/entra/identity/devices/how-to-hybrid-join) · Laboratorio

<a id="m8"></a>

## M8 · Global Secure Access y Zero Trust de red

*L300 · ~10 h · Origen: SC-300 · Global Secure Access; episodio del Virtual Ninja Show sobre Private Access (2024)*

**Global Secure Access** es el servicio de borde de seguridad (SSE) de Microsoft: reúne **Internet Access** y **Private Access** sobre una red de 70 regiones y más de 190 ubicaciones de borde, y lleva el acceso condicional a la capa de red. El cliente reenvía el tráfico según **perfiles** —tráfico de Microsoft, Private Access e Internet Access, evaluados en ese orden—, y el perfil de sistema de tráfico de Entra se activa con cualquiera de ellos.

La licencia marca el alcance. El **perfil de tráfico de Microsoft solo requiere P1 o P2**, así que lo tienes con Microsoft 365 E5 (y con E3): con él validas que el acceso a Microsoft 365 venga de una **red conforme**, aplicas restricciones universales de inquilino y restauras la IP de origen. **Private Access** (reemplazo de VPN por aplicación) e **Internet Access** (filtrado web, DLP de red con Purview y protección contra inyección de prompts) requieren su licencia, Entra Suite o E7; desde el 2 de noviembre de 2026 también se venden juntos como «Microsoft Entra Global Secure Access».

En 2026 llegaron Private Access para Windows personal registrado en Entra (GA en junio) y, en vista previa, perfiles personalizados de Private Access, acceso de invitados B2B con Global Secure Access y CAE universal con señales de dispositivo. Desplegarás por oleadas y con plan de reversión, como recomienda la guía oficial.

**Por qué importa**

El acceso ya no pasa por la red corporativa y las VPN tradicionales dan acceso amplio a redes enteras. Global Secure Access permite validar que el tráfico venga de una red conforme, impedir el uso de tokens robados fuera de ella y reemplazar la VPN por acceso por aplicación. Métricas: tráfico de Microsoft 365 por Global Secure Access, aplicaciones privadas sin VPN y sesiones bloqueadas por red no conforme.

**Qué vas a lograr**

- Explicar los perfiles de reenvío de Global Secure Access, su orden de evaluación y su licencia.
- Desplegar el perfil de tráfico de Microsoft con red conforme y restricciones universales de inquilino.
- Diseñar el reemplazo de VPN con Private Access.
- Evaluar Internet Access, la DLP de red y la protección contra inyección de prompts.

> **Atención.** Licencia: el perfil de tráfico de Microsoft solo requiere P1 o P2, así que lo tienes con E5 (y con E3); Private Access e Internet Access requieren su licencia, Entra Suite o E7, y desde el 2 de noviembre de 2026 se venden también juntos como «Microsoft Entra Global Secure Access» ([perfiles de reenvío](https://learn.microsoft.com/en-us/entra/global-secure-access/concept-traffic-forwarding), [oferta conjunta](https://techcommunity.microsoft.com/blog/microsoft-entra-blog/global-secure-access-private-access-and-internet-access-in-one-offering/4569098)).

> **Consejo Ninja.** Para habilitar el perfil de tráfico de Microsoft necesitas los roles Global Secure Access Administrator y Application Administrator, y el cliente revisa el perfil cada 5 minutos. Despliega por oleadas y valida la restauración de la IP de origen antes de exigir red conforme ([tutorial](https://learn.microsoft.com/en-us/entra/global-secure-access/tutorial-microsoft-traffic-enable-profile), [guía de despliegue](https://learn.microsoft.com/en-us/entra/architecture/gsa-deployment-guide-microsoft-traffic)).

> **Novedad.** En 2026 llegaron Private Access para Windows personal registrado en Entra (GA en junio), perfiles personalizados de Private Access (hasta 10, en vista previa) y, en octubre, el acceso de invitados B2B con Global Secure Access y la CAE universal con señales de dispositivo, ambos en vista previa ([What's new](https://learn.microsoft.com/en-us/entra/fundamentals/whats-new), [novedades de octubre](https://techcommunity.microsoft.com/blog/microsoft-entra-blog/what%E2%80%99s-new-in-microsoft-entra-october-2026/4556460)).

> **Consejo Ninja.** Para la red conforme, la protección contra la reproducción de tokens y las restricciones universales de inquilino, sigue la serie de Christopher Brumm sobre el perfil de tráfico de Microsoft ([blog](https://chris-brumm.com/tags/entra/)). La DLP de red con Purview y el tráfico hacia apps de IA se ven en el [webinar de Global Secure Access y Purview](https://www.youtube.com/watch?v=I3NCk1oHkbo) y requieren Internet Access.

**¿Tienes poco tiempo?**

- [What is Global Secure Access?](https://learn.microsoft.com/en-us/entra/global-secure-access/overview-what-is-global-secure-access) · Documentación
- [Global Secure Access traffic forwarding profiles](https://learn.microsoft.com/en-us/entra/global-secure-access/concept-traffic-forwarding) · Documentación
- [Microsoft Global Secure Access deployment guide for Microsoft Traffic](https://learn.microsoft.com/en-us/entra/architecture/gsa-deployment-guide-microsoft-traffic) · Documentación
- [Tutorial: Enable the Microsoft traffic profile](https://learn.microsoft.com/en-us/entra/global-secure-access/tutorial-microsoft-traffic-enable-profile) · Laboratorio

### Documentación, cursos y credenciales

- [Global Secure Access traffic forwarding profiles](https://learn.microsoft.com/en-us/entra/global-secure-access/concept-traffic-forwarding) · Documentación · Oficial · Microsoft Learn. Explica los perfiles de reenvío de Microsoft, Private Access, Internet Access y el perfil de sistema de tráfico de Entra, incluyendo el orden de evaluación y la licencia de cada uno.
- [Microsoft Global Secure Access deployment guide for Microsoft Traffic](https://learn.microsoft.com/en-us/entra/architecture/gsa-deployment-guide-microsoft-traffic) · Documentación · Oficial · Microsoft Learn. Guía paso a paso para planificar, pilotar y desplegar por oleadas el perfil de tráfico de Microsoft con red compatible, restricciones universales de inquilino y restauración de IP de origen.
- [What is Global Secure Access?](https://learn.microsoft.com/en-us/entra/global-secure-access/overview-what-is-global-secure-access) · Documentación · Oficial · Microsoft Learn. Introduce el SSE de Microsoft (Internet Access, Private Access e Internet Access para servicios de Microsoft) y sus capacidades clave sobre la red global de Microsoft.

### Anuncios y blogs oficiales

- [Global Secure Access: Private Access and Internet Access in one offering](https://techcommunity.microsoft.com/blog/microsoft-entra-blog/global-secure-access-private-access-and-internet-access-in-one-offering/4569098) · Blog oficial · Empleado de Microsoft · Nuevo · Yair Tor · Microsoft Entra Blog (Tech Community) · 2 nov 2026. Anuncia la oferta comercial Microsoft Entra Global Secure Access (Private + Internet Access juntos) desde el 2-nov-2026, incluida en Entra Suite y por tanto en Microsoft 365 E7, y novedades como Cloud Firewall para el cliente (preview).

### Webinars, videos y podcasts

- [Purview Data Security and Entra Global Secure Access Deep Dive](https://www.youtube.com/watch?v=I3NCk1oHkbo) · Webinar · Empleado de Microsoft · Mahantesh Hurkadli, Brendon Lee · Microsoft Security Community (YouTube) · 15 ene 2026. Webinar de la comunidad de seguridad de Microsoft sobre cómo GSA y Purview extienden la prevención de pérdida de datos a la red, incluido tráfico hacia apps de IA, con demo y configuración.
- [Announcing new capabilities to protect on-premises resources with MFA via Microsoft Entra Private Access](https://learn.microsoft.com/en-us/shows/microsoft-sentinel-defender-xdr-virtual-ninja-training/announcing-new-capabilities-to-protect-on-premises-resources-with-mfa-via-microsoft-entra-private-access) · Video · Empleado de Microsoft · Legado aún útil · Heike Ritter, Ashish Jain, Navi Beesetti · Microsoft Learn Shows (Virtual Ninja Training) · 8 mar 2024. Episodio del Virtual Ninja Show que muestra cómo Entra Private Access aplica MFA y acceso condicional a recursos locales como reemplazo de VPN, con demo. *Nota:* Grabado en 2024; la licencia y capacidades de Private Access han evolucionado (BYOD GA en 2026, perfiles personalizados)

### Laboratorios, GitHub y herramientas

- [Tutorial: Enable the Microsoft traffic profile](https://learn.microsoft.com/en-us/entra/global-secure-access/tutorial-microsoft-traffic-enable-profile) · Laboratorio · Oficial · Microsoft Learn. Tutorial práctico para habilitar el perfil de tráfico de Microsoft, asignarlo a un grupo piloto, instalar el cliente de Windows y verificar las reglas de reenvío.

### Comunidad: blogs, libros, newsletters y eventos

- [Chris Brumm's Blog - Entra (Microsoft Traffic Profile series)](https://chris-brumm.com/tags/entra/) · Blog · MVP · Nuevo · Christopher Brumm · Chris Brumm's Blog · 24 oct 2026. Serie de 2026 sobre el perfil de tráfico de Microsoft en GSA (comprobación de red conforme, protección contra replay de tokens, restricciones universales de inquilino) y phishing por device code.

**Manos a la obra**

1. `Laboratorio parcial` Habilita el perfil de tráfico de Microsoft para un grupo piloto, instala el cliente en una VM Windows 11 y verifica las reglas de reenvío. Limitación: Private Access e Internet Access requieren la prueba de Entra Suite ([tutorial](https://learn.microsoft.com/en-us/entra/global-secure-access/tutorial-microsoft-traffic-enable-profile)).
2. `Laboratorio parcial` Activa la restauración de la IP de origen y la condición de red conforme, y crea CA13 en solo informe. Limitación: el laboratorio no reproduce el volumen ni la diversidad de redes de producción ([guía de despliegue](https://learn.microsoft.com/en-us/entra/architecture/gsa-deployment-guide-microsoft-traffic)).
3. `Laboratorio parcial` Configura las restricciones universales de inquilino y comprueba que, desde el dispositivo con cliente, un usuario no puede iniciar sesión en un tenant ajeno. Limitación: necesitas una cuenta de otro tenant para probar el bloqueo.
4. `Laboratorio parcial` Con la prueba de Entra Suite, publica con Private Access una app interna de la VM de AD (por ejemplo, RDP) y exígele MFA con acceso condicional, como en el [episodio del Virtual Ninja Show](https://learn.microsoft.com/en-us/shows/microsoft-sentinel-defender-xdr-virtual-ninja-training/announcing-new-capabilities-to-protect-on-premises-resources-with-mfa-via-microsoft-entra-private-access). Limitación: requiere la prueba de Entra Suite y un conector en una VM.
5. `Solo producción` Plan de despliegue por oleadas del perfil de tráfico de Microsoft en producción. Cómo hacerlo seguro: grupos por oleada, plan de reversión probado, monitoreo de conectividad y validación de la restauración de la IP de origen antes de exigir red conforme ([guía de despliegue](https://learn.microsoft.com/en-us/entra/architecture/gsa-deployment-guide-microsoft-traffic)).

**¿Quieres profundizar?**

- [Chris Brumm's Blog - Entra (Microsoft Traffic Profile series)](https://chris-brumm.com/tags/entra/) · Blog
- [Purview Data Security and Entra Global Secure Access Deep Dive](https://www.youtube.com/watch?v=I3NCk1oHkbo) · Webinar

<a id="reto-intermedio"></a>

## Reto del nivel

**Privilegios, riesgo y accesos bajo control.** Convierte los roles privilegiados del laboratorio en elegibles en PIM con contexto de autenticación, activa CA06 y CA07 después de medir su impacto, crea un paquete de acceso para invitados con expiración y revisión, restringe el consentimiento con el flujo del administrador, envía los registros a Log Analytics y despliega el perfil de tráfico de Microsoft con red conforme para un piloto. Entrega: un tablero con cinco métricas —asignaciones permanentes, usuarios de riesgo alto sin remediar, invitados sin patrocinador, apps con secretos y cobertura de acceso condicional— y las consultas KQL que las calculan.

<a id="quiz-intermedio"></a>

## Evaluación del nivel

Responde y compara con [Evaluaciones y respuestas](06_Evaluaciones_y_respuestas.md#eval-intermedio). Con 80 % o más, ¡nivel aprobado! (En la versión web puedes corregir en línea y generar tu certificado).

1. La protección de tokens para apps nativas está en disponibilidad general en:
   - a) Solo Windows
   - b) Windows, iOS/iPadOS y macOS
   - c) Solo navegadores
   - d) Android y Linux

2. ¿Qué valores puede tomar un contexto de autenticación?
   - a) C1 a C99
   - b) A1 a A9
   - c) R1 a R25
   - d) Cualquier texto libre

3. Desde septiembre de 2024, una política de flujos de autenticación dirigida a «All resources» también aplica a:
   - a) Las identidades administradas
   - b) Los agentes de Copilot Studio
   - c) El Device Registration Service
   - d) Las cuentas de emergencia

4. ¿Cuándo se retiraron las políticas de riesgo heredadas de ID Protection?
   - a) 30 de septiembre de 2025
   - b) 1 de marzo de 2027
   - c) 1 de octubre de 2026
   - d) No se retiraron

5. Con «Require risk remediation», ¿qué ocurre con un usuario sin contraseña que tiene riesgo de usuario alto?
   - a) Debe cambiar la contraseña
   - b) Queda bloqueado hasta que un administrador lo libere
   - c) No ocurre nada
   - d) Se revocan sus sesiones y debe volver a iniciar sesión

6. ¿Cuánto pueden tardar en aparecer las detecciones de riesgo fuera de línea?
   - a) 5 minutos
   - b) Hasta 48 horas
   - c) 30 días
   - d) 6 meses

7. ¿Qué rol mínimo necesitas para configurar las opciones de un rol de Entra en PIM?
   - a) Security Administrator
   - b) Global Reader
   - c) Privileged Role Administrator
   - d) User Administrator

8. Si vence la licencia que habilita PIM, ¿qué pasa con las asignaciones?
   - a) No pasa nada
   - b) Se eliminan las elegibles y las activas temporales pasan a permanentes
   - c) Se eliminan todas
   - d) Todas pasan a elegibles

9. ¿Qué función de gobernanza NO está incluida en Microsoft 365 E5?
   - a) PIM for Groups
   - b) Revisiones de acceso de roles de Entra
   - c) Controles de acceso condicional en PIM
   - d) Lifecycle Workflows

10. ¿Qué licencia requiere sincronizar grupos entre tenants?
   - a) Entra ID P1
   - b) Entra ID P2
   - c) ID Governance o Entra Suite
   - d) Workload ID Premium

11. Una empresa con dirección de facturación en México, ¿puede usar App governance?
   - a) Sí, con Microsoft 365 E5
   - b) No: México está entre los países excluidos
   - c) Sí, con Purview Suite
   - d) Solo en vista previa

12. Desde junio de 2026, el bloqueo de propiedades de instancia:
   - a) Está retirado
   - b) Solo aplica a apps SAML
   - c) Requiere Workload ID Premium
   - d) Viene habilitado por defecto en apps nuevas, single-tenant y multitenant

13. ¿Qué se necesita para recibir las alertas de monitoreo de salud de Entra?
   - a) P1 o P2 que no sea de prueba y al menos 100 usuarios activos al mes
   - b) Solo la edición gratuita
   - c) Microsoft Sentinel
   - d) ID Governance

14. ¿Cuál es un requisito de Platform SSO para macOS?
   - a) Windows Hello for Business
   - b) AD FS
   - c) Workload ID Premium
   - d) Company Portal 5.2404.0 o posterior

15. ¿En qué orden evalúa el cliente de Global Secure Access los perfiles de reenvío?
   - a) Microsoft, Private Access, Internet Access
   - b) Internet Access, Private Access, Microsoft
   - c) Private Access, Microsoft, Internet Access
   - d) Todos en paralelo

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

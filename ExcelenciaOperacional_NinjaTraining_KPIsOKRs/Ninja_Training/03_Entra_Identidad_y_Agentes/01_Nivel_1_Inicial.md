# Nivel 1 · Inicial · Fundamentos

*Microsoft Entra Ninja Training: identidad y acceso para la era de los agentes de IA · Edición 2026*

[← Programa](00_Programa.md) · [Índice del programa](README.md) · [Nivel 2 · Intermedio →](02_Nivel_2_Intermedio.md)

<a id="inicial"></a>

Protocolos, licencias, administración del tenant, autenticación resistente al phishing, acceso condicional esencial e identidad híbrida, con tu laboratorio armado. Terminas con una línea base en solo informe, dos cuentas de emergencia y un plan de passkeys con fechas.

*L100–L200 · 8 módulos · ~59 horas · 64 recursos*

**Módulos de este nivel:** [P0 Protocolos y tokens](#p0) · [I0 Cómo aprender Entra](#i0) · [I1 Entra hoy y licencias E5](#i1) · [I2 Administración del tenant](#i2) · [I3 Autenticación sin phishing](#i3) · [I4 Acceso condicional esencial](#i4) · [I5 Identidad híbrida](#i5) · [I6 Laboratorios de práctica](#i6)

<a id="p0"></a>

## P0 · Prerrequisitos: protocolos, tokens y conceptos de identidad

*L100–L200 · ~5 h · Origen: Sin Ninja oficial de Entra: base conceptual del SC-300 y de la plataforma de identidad de Microsoft*

Antes de configurar una sola política conviene entender qué viaja por la red cuando alguien inicia sesión. Microsoft Entra ID es un proveedor de identidad que habla **OAuth 2.0** y **OpenID Connect (OIDC)** con las aplicaciones modernas y **SAML 2.0** con buena parte de las aplicaciones empresariales. En OAuth intervienen cuatro roles —servidor de autorización, cliente, propietario del recurso y servidor de recursos— y circulan tres tipos de token: de acceso, de ID y de actualización (los dos primeros, en formato JWT). Saber quién emite cada token, para qué audiencia y cuánto dura es la base de todo lo que sigue.

Hay dos piezas más que aparecen en casi todos los módulos. El **Primary Refresh Token (PRT)** es el artefacto central del inicio de sesión único en Windows, macOS, iOS, Android y Linux, y transporta las reclamaciones del dispositivo que evalúa el acceso condicional. La **evaluación continua de acceso (CAE)** acorta la reacción ante eventos críticos, porque un token de acceso dura una hora por defecto. Con estos conceptos entenderás por qué la protección de tokens, la revocación de sesiones y el robo de tokens son hoy el centro de la defensa de identidad.

También repasarás el vocabulario de objetos —usuarios, grupos, roles, registros de aplicación y service principals— y los dos flujos que usan los agentes de IA: **en nombre de un usuario (on-behalf-of, OBO)** y **credenciales de cliente** para actuar de forma autónoma. Si los dominas aquí, el track de agentes ([X3](04_Nivel_4_Identidad_para_agentes_de_IA.md#x3)) te resultará natural.

**Por qué importa**

La mayoría de los errores de diseño en acceso condicional, en integraciones de aplicaciones y en la respuesta a robo de tokens nacen de no saber qué token se está evaluando. Dominar los protocolos reduce el tiempo de diagnóstico de inicios de sesión fallidos, evita excepciones innecesarias en las políticas y prepara al equipo para razonar sobre los tokens de los agentes de IA, que son el nuevo perímetro.

**Qué vas a lograr**

- Explicar los roles de OAuth 2.0 y la función de los tokens de acceso, de ID y de actualización.
- Distinguir un inicio de sesión OIDC de una federación SAML 2.0 y reconocer sus mensajes.
- Describir cómo se emite y usa el PRT y qué reclamaciones aporta al acceso condicional.
- Explicar qué cambia la evaluación continua de acceso frente a la vida útil de un token.
- Diferenciar usuario, grupo, rol, registro de aplicación y service principal.

> **Consejo Ninja.** Antes de diseñar políticas, aprende a leer un token: emisor, audiencia, scopes o roles y fecha de expiración responden la mayoría de las preguntas de diagnóstico. OAuth 2.0 define cuatro roles —servidor de autorización, cliente, propietario y servidor de recursos— y Entra emite tokens de acceso, de ID y de actualización ([protocolos de la plataforma de identidad](https://learn.microsoft.com/en-us/entra/identity-platform/v2-protocols)).

> **Atención.** CAE no es instantáneo para todo: los eventos críticos (usuario deshabilitado, cambio de contraseña, revocación de tokens, riesgo alto) tardan hasta 15 minutos, la ubicación IP se aplica al instante en los servicios compatibles y esas apps pueden recibir tokens de hasta 28 horas. SharePoint Online no admite los eventos de riesgo de usuario ([CAE](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-continuous-access-evaluation)).

> **Novedad.** El PRT es el artefacto central del inicio de sesión único también en Linux, y su documentación explica cómo se emite, se renueva, se protege con TPM, se invalida y cuándo obtiene la reclamación de MFA: la base para entender la protección de tokens y Platform SSO ([PRT](https://learn.microsoft.com/en-us/entra/identity/devices/concept-primary-refresh-token)).

> **Consejo Ninja.** Los agentes usan los mismos protocolos: en nombre de un usuario (OBO) el sujeto del token es el usuario y en modo autónomo es la identidad del agente. Por eso el acceso condicional para agentes se asigna según el sujeto del token ([acceso condicional para agentes](https://learn.microsoft.com/en-us/entra/identity/conditional-access/agent-id)).

**¿Tienes poco tiempo?**

- [OAuth 2.0 and OpenID Connect (OIDC) authentication flow in the Microsoft identity platform](https://learn.microsoft.com/en-us/entra/identity-platform/v2-protocols) · Documentación
- [Understanding Primary Refresh Token (PRT)](https://learn.microsoft.com/en-us/entra/identity/devices/concept-primary-refresh-token) · Documentación
- [Continuous access evaluation](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-continuous-access-evaluation) · Documentación

### Documentación, cursos y credenciales

- [OAuth 2.0 and OpenID Connect (OIDC) authentication flow in the Microsoft identity platform](https://learn.microsoft.com/en-us/entra/identity-platform/v2-protocols) · Documentación · Oficial · Microsoft Learn. Introduce los roles de OAuth 2.0 (servidor de autorización, cliente, propietario y servidor de recursos), los tokens de acceso, ID y actualización en formato JWT, el registro de aplicaciones y los endpoints.
- [Single sign-on SAML protocol](https://learn.microsoft.com/en-us/entra/identity-platform/single-sign-on-saml-protocol) · Documentación · Oficial · Microsoft Learn. Explica las solicitudes AuthnRequest y respuestas SAML 2.0 que admite Entra ID para el inicio de sesión único, con formatos de NameID y contexto de autenticación solicitado.
- [Protocolo SAML de inicio de sesión único](https://learn.microsoft.com/es-es/entra/identity-platform/single-sign-on-saml-protocol) · Documentación · Oficial · ES · Microsoft Learn. Versión en español de la referencia del protocolo SAML 2.0 en Entra ID, útil para nivelar conceptos de federación antes de I5 y M5.

**Manos a la obra**

1. `Laboratorio` Registra una app de prueba, inicia sesión con OIDC y decodifica el token de ID y el de acceso con una herramienta local o un script: anota emisor (`iss`), audiencia (`aud`), scopes (`scp`) y expiración (`exp`). Evidencia: captura con los claims anotados ([protocolos](https://learn.microsoft.com/en-us/entra/identity-platform/v2-protocols)).
2. `Laboratorio` Configura una aplicación empresarial SAML de prueba, captura la AuthnRequest y la respuesta con las herramientas del navegador e identifica NameID, audiencia y firma. Evidencia: archivo HAR anotado ([protocolo SAML](https://learn.microsoft.com/en-us/entra/identity-platform/single-sign-on-saml-protocol)).
3. `Laboratorio` En una VM Windows 11 unida a Entra con tus créditos de Azure ([inicio de sesión en VM con Entra ID](https://learn.microsoft.com/en-us/entra/identity/devices/howto-vm-sign-in-azure-ad-windows)), ejecuta `dsregcmd /status` y documenta el estado del dispositivo y del PRT ([PRT](https://learn.microsoft.com/en-us/entra/identity/devices/concept-primary-refresh-token)).
4. `Laboratorio` Revoca las sesiones de un usuario de prueba con `Revoke-MgUserSignInSession` mientras tiene Outlook en la web abierto y mide cuánto tarda en pedir credenciales; compáralo con la vida del token de acceso ([revocar acceso](https://learn.microsoft.com/en-us/entra/identity/users/users-revoke-access)).
5. `Laboratorio` Crea un usuario, un grupo, una asignación de rol, un registro de app y su service principal, y explica con capturas qué objeto recibe cada permiso. Entregable: tu glosario de objetos de una página.

<a id="i0"></a>

## I0 · Cómo aprender Microsoft Entra y dónde pedir ayuda

*L100–L200 · ~3 h · Origen: Guía de estudio del SC-300 y Applied Skills de identidad (no existe un Ninja oficial de Entra)*

A diferencia de Sentinel o Defender XDR, Microsoft Entra no tiene un Ninja Training oficial: el índice «ninja training» de Tech Community lista Ninjas vigentes de Defender XDR, Defender for Endpoint y Purview eDiscovery, pero ninguno de Entra. Por eso este programa se apoya en las rutas formales: el examen **SC-300: Microsoft Identity and Access Administrator**, cuyas habilidades medidas se actualizaron el 28 de octubre de 2026; la credencial **Applied Skills** «Get started with identities and access using Microsoft Entra», que se evalúa en un laboratorio real de dos horas; y el centro de formación de Entra en Microsoft Learn.

Entra cambia todos los meses, así que aprender también es mantenerse al día. Tu radar oficial es la página de novedades de Entra (seis meses de historial y fuente RSS) y el resumen mensual del blog de Entra, que desde octubre de 2026 se organiza por resultados. En la comunidad, **Entra.News** resume cada semana lo que publican Microsoft y los MVP. Para dudas puntuales, Microsoft Q&A y los foros de Tech Community suelen responder más rápido que cualquier curso. Y recuerda que Microsoft Ignite se realiza del 17 al 20 de noviembre de 2026 y puede cambiar varios estados de vista previa.

**Por qué importa**

En 2026 cambiaron las licencias (Microsoft 365 E7), la autenticación (passkeys por defecto) y la identidad de los agentes (Agent ID en disponibilidad general). Un equipo sin rutina de actualización toma decisiones con información vencida. Este módulo te da el mapa de credenciales y fuentes para que el aprendizaje sea continuo, medible y alineado con una certificación reconocida.

**Qué vas a lograr**

- Identificar las credenciales formales de identidad (SC-300 y Applied Skills) y su estado a noviembre de 2026.
- Configurar tus fuentes de novedades: la página What's new con RSS, el blog mensual de Entra y Entra.News.
- Mapear las habilidades medidas del SC-300 a los módulos de esta guía.
- Armar un plan de estudio personal con horas, entregables y fechas de evaluación.

> **Novedad.** Las habilidades medidas del SC-300 se actualizaron el 28 de octubre de 2026, con cambios menores en autenticación, Global Secure Access y acceso privilegiado. Se aprueba con 700, la renovación anual es gratuita y la nueva Practice Assessment está en AI Skills Navigator; la de Learn ya no se actualiza ([guía del SC-300](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-300)).

> **Atención.** La versión en español del examen se actualiza unas ocho semanas después de la inglesa ([guía en español](https://learn.microsoft.com/es-es/credentials/certifications/resources/study-guides/sc-300)), y la guía en inglés se contradice en el peso del dominio de autenticación y acceso: 25–30 % en el resumen y 20–25 % en el detalle.

> **Consejo Ninja.** La credencial Applied Skills «Get started with identities and access using Microsoft Entra» se evalúa en un laboratorio real de 2 horas; si lo lanzas y no terminas, debes esperar 72 horas para relanzarlo ([Applied Skills](https://learn.microsoft.com/en-us/credentials/applied-skills/get-started-with-identities-and-access-using-microsoft-entra/)). Repasa antes su [guía de estudio](https://learn.microsoft.com/en-us/credentials/applied-skills/resources/study-guides/apl-0501), que todavía evalúa el MFA por usuario heredado.

> **Novedad.** Desde octubre de 2026, el resumen mensual del blog de Entra se organiza por resultados ([octubre de 2026](https://techcommunity.microsoft.com/blog/microsoft-entra-blog/what%E2%80%99s-new-in-microsoft-entra-october-2026/4556460)); la página [What's new](https://learn.microsoft.com/en-us/entra/fundamentals/whats-new) conserva seis meses de historial con RSS, y [Entra.News](https://entra.news/) resume cada semana lo que publican Microsoft y la comunidad.

**¿Tienes poco tiempo?**

- [Study guide for Exam SC-300: Microsoft Identity and Access Administrator](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-300) · Credencial
- [Training for Microsoft Entra ID (Microsoft Learn hub)](https://learn.microsoft.com/en-us/training/entra/) · Curso
- [Microsoft Entra releases and announcements (What's new)](https://learn.microsoft.com/en-us/entra/fundamentals/whats-new) · Documentación
- [Entra.News - Your weekly dose of Microsoft Entra](https://entra.news/) · Newsletter

### Documentación, cursos y credenciales

- [Study guide for Exam SC-300: Microsoft Identity and Access Administrator](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-300) · Credencial · Oficial · Nuevo · Microsoft Learn · 30 ago 2026. Guía oficial del examen SC-300 con las habilidades medidas vigentes desde el 28 de octubre de 2026, que ya incluyen Global Secure Access, claves de acceso, autenticación de Kerberos de Entra y acciones protegidas.
- [Microsoft Entra releases and announcements (What's new)](https://learn.microsoft.com/en-us/entra/fundamentals/whats-new) · Documentación · Oficial · Microsoft Learn. Registro mensual oficial de novedades, cambios y retiradas de toda la familia Entra de los últimos seis meses, con fuente RSS para suscribirse.
- [Training for Microsoft Entra ID (Microsoft Learn hub)](https://learn.microsoft.com/en-us/training/entra/) · Curso · Oficial · Microsoft Learn. Portal de formación de Microsoft Learn para Entra con rutas de inicio, cursos dirigidos por instructor, certificación SC-300 y Virtual Training Days gratuitos.
- [Implement an identity management solution using Microsoft Entra ID](https://learn.microsoft.com/en-us/training/paths/implement-identity-management-solution/) · Curso · Oficial · Microsoft Learn. Ruta de aprendizaje (4 h 16 min, alineada con SC-300) sobre configuración inicial del inquilino, usuarios y grupos, identidades externas e identidad híbrida con Entra Connect.
- [Microsoft Applied Skills: Get started with identities and access using Microsoft Entra](https://learn.microsoft.com/en-us/credentials/applied-skills/get-started-with-identities-and-access-using-microsoft-entra/) · Credencial · Oficial · Microsoft Learn (Credentials). Credencial Applied Skills de nivel principiante evaluada en un laboratorio interactivo de 2 horas sobre usuarios, grupos, protección de contraseñas, SSPR, MFA y acceso condicional.
- [Study guide for the Applied Skills assessment lab: Get started with identities and access using Microsoft Entra](https://learn.microsoft.com/en-us/credentials/applied-skills/resources/study-guides/apl-0501) · Credencial · Oficial · Nuevo · Microsoft Learn (Credentials) · 2 oct 2026. Guía de estudio con las tareas exactas del laboratorio Applied Skills de identidad, incluida la revisión de una política de acceso condicional con What If.
- [Guía de estudio para el examen SC-300: Administrador de identidad y acceso de Microsoft](https://learn.microsoft.com/es-es/credentials/certifications/resources/study-guides/sc-300) · Credencial · Oficial · Nuevo · ES · Microsoft Learn · 30 ago 2026. Versión en español de la guía del SC-300 útil para el público hispanohablante, aunque la versión localizada del examen se actualiza unas ocho semanas después que la inglesa.

### Anuncios y blogs oficiales

- [What’s new in Microsoft Entra: October 2026](https://techcommunity.microsoft.com/blog/microsoft-entra-blog/what%E2%80%99s-new-in-microsoft-entra-october-2026/4556460) · Blog oficial · Oficial · Nuevo · Yina Arenas · Microsoft Entra Blog (Tech Community) · 12 oct 2026. Resumen mensual organizado por resultados que destaca la CAE universal con señales de dispositivo, la herramienta guiada de migración de Connect Sync a Cloud Sync (GA) y el acceso B2B con Global Secure Access.
- [What's New in Microsoft Entra: August 2026](https://techcommunity.microsoft.com/blog/microsoft-entra-blog/whats-new-in-microsoft-entra-august-2026/4545172) · Blog oficial · Oficial · Nuevo · Yina Arenas · Microsoft Entra Blog (Tech Community) · 10 ago 2026. Resumen mensual con la sincronización de dispositivos de AD mediante Cloud Sync (preview), la reescritura de atributos de Exchange Online y el control de solicitudes de SSO en Windows.

### Comunidad: blogs, libros, newsletters y eventos

- [Entra.News - Your weekly dose of Microsoft Entra](https://entra.news/) · Newsletter · Comunidad · Nuevo · Merill Fernando, Joshua Fernando · Entra.News (Substack) · 1 nov 2026. Boletín semanal gratuito que resume las novedades de Entra de Microsoft y la comunidad, con el podcast Entra.Chat de entrevistas a gerentes de producto y profesionales.
- [About Merill Fernando](https://merill.net/about/) · Blog · Comunidad · Merill Fernando · merill.net. Perfil del ex-PM de Entra que recopila sus herramientas gratuitas (Maester, cmd.ms, Graph X-Ray, idPowerToys, Entra Exporter, Zero Trust Assessment) y canales (Entra.News, Entra.Chat).
- [Christopher Brumm | Most Valuable Professionals](https://mvp.microsoft.com/en-US/MVP/profile/cad9c18c-40fe-475d-b9d9-dbec9bce58c3) · Blog · MVP · Christopher Brumm · Microsoft MVP Program. Perfil MVP oficial que acredita a Christopher Brumm (glueckkanja AG, Alemania) en Security con foco en identidad y acceso e ITDR.
- [Nathan McNulty | Most Valuable Professionals](https://mvp.microsoft.com/en-US/MVP/profile/58f4fa40-eb0e-4336-8d27-25e506e4ee2c) · Blog · MVP · Nathan McNulty · Microsoft MVP Program. Perfil MVP oficial de Nathan McNulty (Patriot Consulting, EE. UU.) en Security con foco en identidad y acceso, con su Conditional Access Masterclass.

**Manos a la obra**

1. `Laboratorio` Lee la [guía del SC-300](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-300) y arma una tabla «habilidad medida → módulo de esta guía → semana prevista»; súmala a tu plan.
2. `Laboratorio` Suscribe la página [What's new](https://learn.microsoft.com/en-us/entra/fundamentals/whats-new) por RSS y [Entra.News](https://entra.news/), y crea un canal o carpeta donde el equipo registre cada novedad con la acción que implica.
3. `Laboratorio` Completa la ruta de Learn [Implement an identity management solution](https://learn.microsoft.com/en-us/training/paths/implement-identity-management-solution/) (unas 4 horas) y guarda el registro de finalización.
4. `Laboratorio` Agenda la evaluación [Applied Skills](https://learn.microsoft.com/en-us/credentials/applied-skills/get-started-with-identities-and-access-using-microsoft-entra/) para cuando termines I2 a I4; el laboratorio lo provee Microsoft, así que no necesitas tenant propio.

**¿Quieres profundizar?**

- [About Merill Fernando](https://merill.net/about/) · Blog

<a id="i1"></a>

## I1 · Microsoft Entra hoy y qué incluye Microsoft 365 E5

*L100–L200 · ~4 h · Origen: SC-300 (contexto de producto) y la página oficial de licencias de Microsoft Entra*

Microsoft Entra es una familia de productos. **Entra ID** —el servicio que antes se llamaba Azure AD (Azure Active Directory)— gestiona identidades, autenticación y acceso condicional; **ID Protection** detecta riesgo; **ID Governance** gobierna el ciclo de vida y los accesos; **Verified ID** emite credenciales verificables; **Global Secure Access** lleva la identidad a la red con Internet Access y Private Access; **Workload ID** protege aplicaciones y service principals; y **Agent ID** da identidad propia a los agentes de IA.

Microsoft 365 E3 incluye Entra ID P1 y Microsoft 365 E5 incluye Entra ID P2, que suma ID Protection, PIM y las funciones de gobernanza que ya eran GA en P2. **Lo que E5 no incluye**: Entra ID Governance completo (complemento, o incluido en Entra Suite), Entra Suite (Private Access, Internet Access, ID Governance, ID Protection y Verified ID premium con Face Check), Workload ID Premium (SKU independiente por identidad) y Agent 365, necesario para extender el acceso condicional, ID Protection y la gobernanza a los agentes.

**Microsoft 365 E7**, en disponibilidad general desde el 1 de mayo de 2026, reúne E5, Microsoft 365 Copilot, Agent 365 y Entra Suite. Microsoft Defender Suite, antes Microsoft 365 E5 Security, también incluye P2. Con este mapa podrás leer cualquier propuesta comercial y saber qué control queda cubierto y cuál requiere un complemento; la tabla completa está en [Licencias de identidad](00_Programa.md#licencias).

**Por qué importa**

Las decisiones de licencias definen qué controles puedes aplicar. Confundir P2 con ID Governance, o asumir que E5 incluye Private Access o el acceso condicional para agentes, produce proyectos que se frenan en compras. Una matriz de licencias por capacidad evita sorpresas, permite justificar complementos con riesgos concretos y alinea a arquitectura, compras y la dirección de seguridad.

**Qué vas a lograr**

- Ubicar cada producto de la familia Entra y su función.
- Distinguir qué incluyen Microsoft 365 E3, E5 y E7 frente a los complementos.
- Explicar qué requieren Entra ID Governance, Entra Suite, Workload ID Premium y Agent 365.
- Construir la matriz de licencias de tu tenant y detectar brechas de control.

> **Qué cambió.** Microsoft 365 E7 se presentó en marzo de 2026 y llegó a disponibilidad general el 1 de mayo: E5 más Microsoft 365 Copilot, Agent 365 y Entra Suite, a 99 USD por usuario al mes en la lista de EE. UU. (90,45 USD sin Teams); los precios varían por país ([Microsoft 365 E7](https://www.microsoft.com/en-us/microsoft-365/enterprise/e7), [anuncio para partners](https://microsoftpartners.microsoft.com/abs/Blog/?title=Introducing+Microsoft+365+E7%3A+The+Frontier+Suite)).

> **Atención.** Entra ID Governance **no** está en Microsoft 365 E5: se compra como complemento (o «Step Up for P2») o llega con Entra Suite o E7, y existen seis SKU que solo difieren en sus prerrequisitos ([licencias de ID Governance](https://learn.microsoft.com/en-us/entra/id-governance/licensing-fundamentals)). Si vencen las licencias de acceso condicional, las políticas no se borran ni se desactivan, pero ya no se pueden editar ([licencias de Entra](https://learn.microsoft.com/en-us/entra/fundamentals/licensing)).

> **Novedad.** Desde el 2 de noviembre de 2026, Private Access e Internet Access también se venden juntos como «Microsoft Entra Global Secure Access»; Entra Suite y E7 ya los incluyen. No es un producto nuevo, sino una forma de compra conjunta ([anuncio](https://techcommunity.microsoft.com/blog/microsoft-entra-blog/global-secure-access-private-access-and-internet-access-in-one-offering/4569098)).

> **Consejo Ninja.** Agent ID está disponible para todos los clientes de Entra, pero el acceso condicional, ID Protection y la gobernanza para agentes requieren Agent 365 (incluido en E7; complemento de 15 USD por usuario al mes). Antes de prometer controles para agentes, revisa la [descripción de servicio de Agent 365](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-agent-365/microsoft-agent-365).

**¿Tienes poco tiempo?**

- [Microsoft Entra licensing](https://learn.microsoft.com/en-us/entra/fundamentals/licensing) · Documentación
- [Microsoft Entra ID Governance licensing fundamentals](https://learn.microsoft.com/en-us/entra/id-governance/licensing-fundamentals) · Documentación
- [Microsoft 365 E7 for Enterprise](https://www.microsoft.com/en-us/microsoft-365/enterprise/e7) · Documentación
- [Microsoft Entra Suite hands-on tour of identity and network access protections](https://www.youtube.com/watch?v=81rnazsINB4) · Video

### Documentación, cursos y credenciales

- [Microsoft Entra licensing](https://learn.microsoft.com/en-us/entra/fundamentals/licensing) · Documentación · Oficial · Nuevo · Microsoft Learn · 28 jul 2026. Página de referencia que detalla qué funciones de Entra cubren Free, P1, P2, ID Governance, Entra Suite, Agent 365 y Microsoft 365 E5/E7, incluidos roles, unidades administrativas, PIM, acceso condicional y Agent ID.
- [Microsoft Entra ID Governance licensing fundamentals](https://learn.microsoft.com/en-us/entra/id-governance/licensing-fundamentals) · Documentación · Oficial · Microsoft Learn. Explica los seis productos de ID Governance, sus prerrequisitos (P1 o P2) y cómo Entra Suite y Agent 365 aportan capacidades de gobernanza para personas y agentes.
- [Microsoft 365 E7 for Enterprise](https://www.microsoft.com/en-us/microsoft-365/enterprise/e7) · Documentación · Oficial. Página comercial de Microsoft 365 E7, que agrupa Microsoft 365 E5, Microsoft 365 Copilot, Microsoft Agent 365 y Microsoft Entra Suite por 99 USD por usuario al mes.
- [Licensing for Microsoft Entra Tenant Governance](https://learn.microsoft.com/en-us/entra/id-governance/tenant-governance/licensing) · Documentación · Oficial · Microsoft Learn. Describe la licencia de Tenant Governance, con monitoreo de deriva de configuración (hasta 800 recursos diarios) y snapshots incluidos desde P1, y capacidad adicional con ID Governance.

### Anuncios y blogs oficiales

- [Introducing Microsoft 365 E7: The Frontier Suite](https://microsoftpartners.microsoft.com/abs/Blog/?title=Introducing+Microsoft+365+E7%3A+The+Frontier+Suite) · Blog oficial · Oficial · AI Business Solutions Partner Marketing Team · Microsoft Partner (AI Business Solutions) · 5 mar 2026. Anuncio para partners de Microsoft 365 E7, presentado el 9 de marzo de 2026 con disponibilidad general el 1 de mayo de 2026, que combina E5, Copilot, Agent 365 y Entra Suite.

### Webinars, videos y podcasts

- [Microsoft Entra Suite hands-on tour of identity and network access protections](https://www.youtube.com/watch?v=81rnazsINB4) · Video · Empleado de Microsoft · Nuevo · John Damon · Microsoft Mechanics (YouTube) · 15 jul 2026. Demo de Mechanics que recorre Entra Suite (Lifecycle Workflows, Face Check, Global Secure Access, DLP de red y protección contra inyección de prompts) y cómo se obtiene con Microsoft 365 E7.
- [Microsoft Entra Webinar Series 2026 (iC Consult)](https://ic-consult.com/es/events/live-webinar/microsoft-entra-webinar-series/) · Webinar · Comunidad · Nuevo · iC Consult y ponentes de Microsoft · iC Consult · nov 2026. Serie de seis webinars de partner (oct-dic 2026) sobre aprovechar licencias E5/E7, agentes, Zero Trust, migración de IGA y AD FS con ponentes de Microsoft.

**Manos a la obra**

1. `Laboratorio` En tu laboratorio, lista las licencias y planes de servicio activos (Entra ID P1/P2, Intune, Defender) y regístralos en la tabla de [Licencias de identidad](00_Programa.md#licencias). Evidencia: hoja con plan, cantidad y fecha de vencimiento.
2. `Laboratorio` Exporta las SKU del tenant con `Get-MgSubscribedSku` (Microsoft Graph PowerShell) y marca qué capacidades de este programa quedan cubiertas y cuáles requieren complemento ([licencias de Entra](https://learn.microsoft.com/en-us/entra/fundamentals/licensing)).
3. `Laboratorio` Mira la [demostración de Entra Suite de Microsoft Mechanics](https://www.youtube.com/watch?v=81rnazsINB4) y anota qué capacidades viste que no están en Microsoft 365 E5.
4. `Solo producción` Construye la matriz de brechas de tu organización: por cada riesgo prioritario (phishing, privilegios, invitados, workload identities y agentes), el control, la licencia necesaria y si la tienes. Cómo hacerlo seguro: lee las licencias con Global Reader, sin cambiar asignaciones, y valida los supuestos con tu equipo de cuenta antes de presentarlos.

<a id="i2"></a>

## I2 · Fundamentos de administración del tenant: roles, delegación y cuentas de emergencia

*L100–L200 · ~9 h · Origen: SC-300 · Implement and manage user identities; Zero Trust Workshop · Identidad*

Administrar bien un tenant empieza por definir quién puede hacer qué. Los **roles integrados** de Entra son gratuitos; los **roles personalizados** requieren P1 por cada usuario asignado; y las **unidades administrativas** permiten delegar por país, filial o área de negocio: crearlas es gratis, pero cada administrador con ámbito en una unidad necesita P1, igual que cada miembro si la membresía es dinámica. Las **unidades administrativas de administración restringida** protegen objetos sensibles —por ejemplo, cuentas Tier 0— para que solo los administradores asignados en esa unidad puedan modificarlos.

La red de seguridad tiene tres piezas. Las **cuentas de emergencia**: al menos dos, solo en la nube, con Global Administrator, protegidas con passkey FIDO2 o autenticación basada en certificados, excluidas de las políticas que bloquean y monitoreadas. Las **acciones protegidas**, que exigen cumplir una política de acceso condicional —vía contexto de autenticación— para editar políticas de acceso condicional, la configuración entre tenants o las ubicaciones con nombre, o para borrar objetos de forma definitiva. Y el **MFA obligatorio** de Microsoft para los portales de administración y, desde el 1 de octubre de 2025, para operaciones de Azure por CLI, PowerShell, IaC, REST y SDK.

Por último, vas a medir. **Identity Secure Score** se recalcula cada 24 horas; las **recomendaciones** de Entra proponen planes de acción; y dos herramientas de código abierto de solo lectura, **Maester** y el **Zero Trust Assessment**, verifican cientos de controles. **Tenant Governance**, en disponibilidad general desde el 10 de agosto de 2026, agrega monitoreo de deriva de configuración, instantáneas y relaciones de administración delegada entre tenants.

**Por qué importa**

La mayoría de los incidentes graves de identidad terminan en un rol privilegiado. Delegar con unidades administrativas y roles mínimos reduce el radio de impacto; las cuentas de emergencia evitan quedarse fuera del tenant por una política mal hecha; y las acciones protegidas impiden que un atacante con una sesión robada desactive tus controles. Métricas: menos de cinco Global Administrators, menos de diez asignaciones privilegiadas y pruebas de Maester aprobadas.

**Qué vas a lograr**

- Diseñar un modelo de delegación con roles integrados, roles personalizados y unidades administrativas, incluidas las de administración restringida.
- Crear, proteger y monitorear cuentas de emergencia según la guía de Microsoft.
- Proteger cambios críticos con acciones protegidas y contexto de autenticación.
- Explicar el MFA obligatorio de Microsoft y los valores predeterminados de seguridad.
- Medir la postura del tenant con Identity Secure Score, recomendaciones, Maester y Zero Trust Assessment.

> **Qué cambió.** MFA obligatorio de Microsoft: la fase 1 (portal de Azure, centros de administración de Entra e Intune desde el segundo semestre de 2024 y de Microsoft 365 desde febrero de 2025) llegó al 100 % de los tenants en marzo de 2025; la fase 2 exige MFA desde el 1 de octubre de 2025 para crear, actualizar o borrar recursos de Azure por CLI, PowerShell, app móvil, IaC, REST y SDK, con opción de aplazar. Las workload identities no se ven afectadas; usa Azure CLI 2.76 y Az PowerShell 14.3 o superiores ([MFA obligatorio](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-mandatory-multifactor-authentication), [fase 2](https://azure.microsoft.com/en-us/blog/azure-mandatory-multifactor-authentication-phase-2-starting-in-october-2025/)).

> **Atención.** Las cuentas de emergencia también deben cumplir el MFA obligatorio: protégelas con passkey FIDO2 (recomendado) o CBA, nunca con SMS. Las políticas en solo informe no requieren excluirlas, pero toda política activa que pueda bloquear sí ([cuentas de emergencia](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/security-emergency-access)).

> **Consejo Ninja.** Una acción protegida solo funciona si la política de acceso condicional asociada a su contexto de autenticación está **activada**: en solo informe no protege nada. Requiere P1 o P2 y el rol Conditional Access Administrator o Security Administrator ([agregar acciones protegidas](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/protected-actions-add), [qué son](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/protected-actions-overview)).

> **Novedad.** Identity Secure Score se recalcula cada 24 horas, está disponible en ediciones gratuitas y de pago y ya incluye acciones de AD local y AD CS que provienen de Defender for Identity; las recomendaciones de Entra incluyen convertir el MFA por usuario a acceso condicional ([Identity Secure Score](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-identity-secure-score), [recomendaciones](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/overview-recommendations)). Tenant Governance llegó a GA el 10 de agosto de 2026 ([anuncio](https://techcommunity.microsoft.com/blog/microsoft-entra-blog/microsoft-entra-tenant-governance-is-now-generally-available/4543638)).

**¿Tienes poco tiempo?**

- [Manage emergency access accounts in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/security-emergency-access) · Documentación
- [What are protected actions in Microsoft Entra ID?](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/protected-actions-overview) · Documentación
- [Mandatory multifactor authentication for Azure and admin portals](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-mandatory-multifactor-authentication) · Documentación
- [maester365/maester](https://github.com/maester365/maester) · GitHub

### Documentación, cursos y credenciales

- [Mandatory multifactor authentication for Azure and admin portals](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-mandatory-multifactor-authentication) · Documentación · Oficial · Microsoft Learn. Describe las dos fases del MFA obligatorio de Microsoft: portales de administración desde 2024-2025 y operaciones de gestión de Azure por CLI, PowerShell, SDK, IaC y API desde el 1 de octubre de 2025.
- [Manage emergency access accounts in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/security-emergency-access) · Documentación · Oficial · Microsoft Learn. Recomienda al menos dos cuentas de emergencia solo en la nube (*.onmicrosoft.com) con Global Administrator, protegidas con passkey FIDO2 o CBA, excluidas de políticas de CA que bloqueen y con monitoreo y validación periódica.
- [What are protected actions in Microsoft Entra ID?](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/protected-actions-overview) · Documentación · Oficial · Microsoft Learn. Explica las acciones protegidas, que exigen cumplir una política de acceso condicional (vía contexto de autenticación) al ejecutar permisos sensibles como editar políticas de CA, acceso entre inquilinos, ubicaciones con nombre o borrado definitivo.
- [What is Identity Secure Score?](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-identity-secure-score) · Documentación · Oficial · Microsoft Learn. Describe la puntuación de seguridad de identidad, recalculada cada 24 horas, y las acciones de mejora incluidas (MFA para roles administrativos, bloqueo de autenticación heredada, PHS si es híbrido, cuentas de Connect, etc.).
- [What are Microsoft Entra recommendations?](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/overview-recommendations) · Documentación · Oficial · Microsoft Learn. Explica las recomendaciones diarias de Entra con plan de acción y recursos impactados, ahora integradas con Identity Secure Score, y los roles de lectura o actualización necesarios.
- [Security defaults in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/fundamentals/security-defaults) · Documentación · Oficial · Microsoft Learn. Describe los valores predeterminados de seguridad (registro de MFA, MFA para administradores, bloqueo de autenticación heredada y de device code flow) pensados para inquilinos sin licencias premium.
- [Configurar los valores predeterminados de seguridad para Microsoft Entra ID](https://learn.microsoft.com/es-es/entra/fundamentals/security-defaults) · Documentación · Oficial · ES · Microsoft Learn. Versión en español del artículo de valores predeterminados de seguridad, útil para comunicar el cambio a equipos hispanohablantes.

### Anuncios y blogs oficiales

- [Azure mandatory multifactor authentication: Phase 2 starting in October 2025](https://azure.microsoft.com/en-us/blog/azure-mandatory-multifactor-authentication-phase-2-starting-in-october-2025/) · Blog oficial · Empleado de Microsoft · Joy Shah, Neha Kulkarni · Microsoft Azure Blog · 5 sep 2025. Anuncia la fase 2 del MFA obligatorio en la capa de Azure Resource Manager desde el 1 de octubre de 2025, aplicada gradualmente vía Azure Policy, y recomienda Azure CLI 2.76 y PowerShell 14.3 o superiores.

### Laboratorios, GitHub y herramientas

- [maester365/maester](https://github.com/maester365/maester) · GitHub · Comunidad · Nuevo · Merill Fernando, Fabian Bader, Thomas Naunheim, Mike Soule y comunidad · GitHub (Maester) · nov 2026. Marco de pruebas automatizadas de código abierto que verifica a diario la configuración de seguridad de Entra y Microsoft 365 (acceso condicional, métodos de autenticación, roles) y exporta informes.
- [microsoft/zerotrustassessment](https://github.com/microsoft/zerotrustassessment) · GitHub · Empleado de Microsoft · Nuevo · Equipo de Microsoft (proyecto comunitario) · GitHub (Microsoft) · oct 2026. Módulo de PowerShell de solo lectura que evalúa el inquilino frente a la guía Zero Trust en siete pilares (identidad, dispositivos, red, datos, infraestructura, SecOps e IA) y genera un informe priorizado.
- [Add, test, or remove protected actions in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/protected-actions-add) · Laboratorio · Oficial · Microsoft Learn. Laboratorio paso a paso para crear un contexto de autenticación, asociarlo a una política de CA activa y proteger permisos como la edición de políticas de acceso condicional.

### Comunidad: blogs, libros, newsletters y eventos

- [Thomas Naunheim - Blog posts](https://www.cloud-architekt.net/blog/) · Blog · MVP · Nuevo · Thomas Naunheim · cloud-architekt.net · 29 sep 2026. Blog de investigación sobre identidad privilegiada (EntraOps, RMAU, Tenant Governance, identidades de carga de trabajo y robo de tokens) del co-creador del Azure AD Attack & Defense Playbook.

**Manos a la obra**

1. `Laboratorio parcial` Crea dos cuentas de emergencia solo en la nube (*.onmicrosoft.com) con Global Administrator, protégelas con passkey FIDO2 y configura una alerta de inicio de sesión en Log Analytics. Evidencia: inicio de sesión de prueba y alerta recibida. Limitación: necesitas una llave FIDO2 o un dispositivo con Authenticator y un workspace con costo ([cuentas de emergencia](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/security-emergency-access)).
2. `Laboratorio` Crea una unidad administrativa por país (por ejemplo, México y Colombia), delega User Administrator con ámbito en una de ellas y prueba que ese administrador no puede modificar usuarios de la otra. Luego crea una unidad de administración restringida con una cuenta Tier 0 de prueba y verifica que un administrador con rol a nivel de tenant no puede editarla.
3. `Laboratorio` Crea un contexto de autenticación, asócialo a una política **activa** que exija MFA resistente al phishing y protege con él la actualización de políticas de acceso condicional; intenta editar una política con y sin cumplirla ([acciones protegidas](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/protected-actions-add)).
4. `Laboratorio` Ejecuta [Maester](https://github.com/maester365/maester) (versión 2.3.0) y el [Zero Trust Assessment](https://github.com/microsoft/zerotrustassessment) en solo lectura, compáralos con Identity Secure Score y prioriza cinco acciones con dueño y fecha.
5. `Laboratorio` Consulta el estado de los valores predeterminados de seguridad con `Get-MgPolicyIdentitySecurityDefaultEnforcementPolicy`; desactívalos solo cuando tu línea base de acceso condicional esté lista y documenta la decisión ([valores predeterminados](https://learn.microsoft.com/en-us/entra/fundamentals/security-defaults)).
6. `Solo producción` Inventaria los Global Administrators y las asignaciones privilegiadas permanentes de tu tenant y compáralos con las metas (menos de 5 y menos de 10). Cómo hacerlo seguro: usa Global Reader, exporta con Microsoft Graph en modo lectura y presenta el plan de reducción antes de quitar asignaciones ([buenas prácticas de roles](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/best-practices)).

**¿Quieres profundizar?**

- [microsoft/zerotrustassessment](https://github.com/microsoft/zerotrustassessment) · GitHub
- [Thomas Naunheim - Blog posts](https://www.cloud-architekt.net/blog/) · Blog
- [Add, test, or remove protected actions in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/protected-actions-add) · Laboratorio

<a id="i3"></a>

## I3 · Autenticación moderna y resistente al phishing: passkeys, Windows Hello, FIDO2 y certificados

*L100–L200 · ~12 h · Origen: SC-300 · Implement authentication and access management*

La contraseña sigue siendo el punto débil, y el MFA basado en SMS, voz o notificaciones no detiene el phishing de adversario en el medio (AiTM). Las credenciales **resistentes al phishing** de Entra son las **passkeys** (FIDO2) —en llaves de seguridad o en Microsoft Authenticator, vinculadas al dispositivo, o **sincronizadas** entre los dispositivos del usuario—, **Windows Hello for Business** y la credencial de plataforma de macOS, y la **autenticación basada en certificados (CBA)** multifactor. El **Temporary Access Pass (TAP)** sirve para el arranque y la recuperación, pero solo cuenta como MFA.

Todo se gestiona desde la **política de métodos de autenticación**: desde el 30 de septiembre de 2025 ya no se pueden administrar métodos en las políticas heredadas de MFA y SSPR (las preguntas de seguridad siguen en SSPR heredado). Los **perfiles de passkey** y las passkeys sincronizadas llegaron a disponibilidad general en marzo de 2026, y las **fortalezas de autenticación** (P1) llevan el método al acceso condicional: MFA, MFA sin contraseña y MFA resistente al phishing, además de las fortalezas personalizadas.

El calendario manda: desde el 1 de septiembre de 2026 las passkeys son el método predeterminado, y Microsoft deja de entregar SMS y voz el 1 de febrero de 2027 para casi todos los usuarios y el 1 de julio de 2027 para Global Administrators activos y usuarios externos. Quien quiera seguir usándolos deberá contratar un proveedor telefónico. Este módulo te deja un plan por persona, con versiones mínimas de sistema operativo y fechas.

**Por qué importa**

Moverse a credenciales resistentes al phishing es la medida con mayor reducción de riesgo de identidad: Microsoft informa que ya protege así el 99,97 % de sus propios pares usuario-dispositivo. En 2027 dejará de ser opcional para quien dependa de SMS y voz de Microsoft. Métricas: usuarios con método resistente registrado, inicios de sesión con fortaleza resistente y usuarios que aún dependen de SMS o voz.

**Qué vas a lograr**

- Migrar las políticas heredadas de MFA y SSPR a la política de métodos de autenticación.
- Configurar perfiles de passkey (vinculadas y sincronizadas) y TAP para el arranque.
- Planificar Windows Hello for Business, la credencial de plataforma de macOS y CBA por persona.
- Aplicar fortalezas de autenticación integradas y personalizadas en el acceso condicional.
- Diseñar el plan de retiro de SMS y voz con fechas, alternativas y comunicación.

> **Novedad.** Desde el 1 de septiembre de 2026 las passkeys son el método predeterminado: se habilitan automáticamente para los usuarios con SMS o voz y la campaña de registro pasa a estado administrado por Microsoft. Desde el 30 de octubre puedes elegir un proveedor telefónico en Microsoft Security Store (los primeros fueron Soprano y Telesign, en vista previa privada) ([passkeys por defecto y retiro de SMS y voz](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sms-voice-retirement), [anuncio del 13 de julio](https://www.microsoft.com/en-us/security/blog/2026/07/13/microsoft-entra-id-security-updates-passkeys-are-the-default-authentication-method-in-entra-id/)).

> **Atención.** Fechas de retiro: 1 de febrero de 2027 para casi todos y 1 de julio de 2027 para Global Administrators activos y usuarios externos (los invitados internos y los Global Administrators solo elegibles en PIM siguen la fecha de febrero); después, el registro de passkey se vuelve obligatorio. Configura el proveedor al menos cuatro semanas antes. El blog de julio daba una sola fecha: prevalece el documento de Learn ([MC1426371](https://mc.merill.net/message/MC1426371), [FAQ](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sms-voice-retirement-faq)).

> **Qué cambió.** Los perfiles de passkey y las passkeys sincronizadas llegaron a GA en marzo de 2026, y la configuración FIDO2 se migró automáticamente (mayo y junio) a un «Default passkey profile» con la propiedad passkeyType: con atestación aplicada solo se admiten passkeys vinculadas al dispositivo; sin atestación, vinculadas y sincronizadas ([MC1221452](https://mc.merill.net/message/MC1221452)).

> **Consejo Ninja.** Versiones mínimas para credenciales resistentes al phishing: Windows 10 22H2 (Windows Hello for Business), Windows 11 22H2, macOS 13, iOS 17 y Android 14 ([plan de despliegue](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-deploy-phishing-resistant-passwordless-authentication)). En junio de 2026 llegó a GA el MFA resistente al phishing en escritorios Linux (Ubuntu 24.04 y 26.04, RHEL 8 a 10) y las campañas de registro ya admiten passkeys ([novedades de junio](https://techcommunity.microsoft.com/blog/microsoft-entra-blog/whats-new-in-microsoft-entra-june-2026/4517885)).

**¿Tienes poco tiempo?**

- [Passkeys by default and retirement of Microsoft-provided SMS and voice authentication](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sms-voice-retirement) · Documentación
- [Conditional Access authentication strengths](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-strengths) · Documentación
- [Plan a phishing-resistant passwordless authentication deployment in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-deploy-phishing-resistant-passwordless-authentication) · Documentación
- [Synced Passkeys in Microsoft Entra for Phishing-resistant MFA](https://www.youtube.com/watch?v=36nIaSBJ7_U) · Video

**Calendario de passkeys y retiro de SMS y voz**

| Fecha | Hito | Qué hacer |
|---|---|---|
| 30 de septiembre de 2025 | Ya no se gestionan métodos en las políticas heredadas de MFA y SSPR | Completa la migración a la política de métodos de autenticación |
| Marzo de 2026 | GA de los perfiles de passkey y de las passkeys sincronizadas | Diseña perfiles por persona: vinculadas con atestación para administradores y sincronizadas para usuarios |
| Mayo y junio de 2026 | Migración automática de la configuración FIDO2 al «Default passkey profile» | Revisa el perfil predeterminado y su propiedad passkeyType |
| 1 de septiembre de 2026 | Passkeys por defecto: habilitación automática para usuarios con SMS o voz y campaña administrada por Microsoft | Decide si usas la exclusión temporal y comunica el cambio |
| 30 de octubre de 2026 | Selección de proveedor telefónico en Microsoft Security Store | Evalúa el costo de un proveedor si vas a mantener SMS o voz |
| Al menos cuatro semanas antes del 1 de febrero de 2027 | Plazo recomendado para configurar el proveedor | Configura y prueba el proveedor con un grupo piloto |
| 1 de febrero de 2027 | Fin de SMS y voz entregados por Microsoft para casi todos, incluidos los invitados internos y los Global Administrators solo elegibles en PIM | Usuarios con passkey o con el proveedor activo |
| 1 de julio de 2027 | Fin para Global Administrators activos y usuarios externos; después, registro de passkey obligatorio | Administradores con passkey, Windows Hello for Business o CBA |

Fuentes: [passkeys por defecto y retiro de SMS y voz](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sms-voice-retirement), [FAQ](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sms-voice-retirement-faq), [MC1221452](https://mc.merill.net/message/MC1221452) y [MC1426371](https://mc.merill.net/message/MC1426371). Fechas para la nube pública.

### Documentación, cursos y credenciales

- [MC1221452 - Microsoft Entra ID: General Availability of passkey profiles and migration for existing Passkeys (FIDO2) tenants](https://mc.merill.net/message/MC1221452) · Documentación · Oficial · Nuevo · Microsoft (archivo mantenido por Merill Fernando) · Microsoft 365 Message Center Archive (mc.merill.net) · 30 oct 2026. Aviso del Centro de mensajes que fija la disponibilidad general de perfiles de passkey y passkeys sincronizadas (marzo de 2026) y la migración automática de la configuración FIDO2 a un perfil predeterminado con la propiedad passkeyType.
- [MC1426371 - Microsoft Entra: Passkeys by default and retirement of Microsoft-provided SMS and voice authentication](https://mc.merill.net/message/MC1426371) · Documentación · Oficial · Nuevo · Microsoft (archivo mantenido por Merill Fernando) · Microsoft 365 Message Center Archive (mc.merill.net) · 15 sep 2026. Aviso del Centro de mensajes que confirma el inicio del despliegue el 1-sep-2026, la campaña de registro en estado administrado por Microsoft y las fechas de retiro de SMS y voz de 2027.
- [Manage authentication methods for Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-methods-manage) · Documentación · Oficial · Microsoft Learn. Explica cómo conviven la política de métodos de autenticación y las políticas heredadas, y confirma que desde el 30 de septiembre de 2025 ya no se pueden gestionar métodos en las políticas heredadas de MFA y SSPR.
- [Get started with a phishing-resistant passwordless authentication deployment in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-plan-prerequisites-phishing-resistant-passwordless-authentication) · Documentación · Oficial · Microsoft Learn. Guía de prerrequisitos para el proyecto passwordless resistente al phishing que enumera las credenciales soportadas (passkeys sincronizadas y vinculadas, Windows Hello, Entra passkey en Windows, CBA) y los roles necesarios.
- [Plan a phishing-resistant passwordless authentication deployment in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-deploy-phishing-resistant-passwordless-authentication) · Documentación · Oficial · Microsoft Learn. Plan de despliegue por personas (administradores, usuarios regulados, no administradores) con versiones mínimas de SO, credenciales portables y locales, y fases de registro, uso y cumplimiento.
- [Passkeys by default and retirement of Microsoft-provided SMS and voice authentication](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sms-voice-retirement) · Documentación · Oficial · Microsoft Learn. Documento oficial con la cronología vigente: passkeys habilitadas por defecto desde el 1-sep-2026, retiro de SMS/voz de Microsoft el 1-feb-2027 para casi todos y el 1-jul-2027 para Global Administrators y usuarios externos.
- [Conditional Access authentication strengths](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-strengths) · Documentación · Oficial · Microsoft Learn. Explica las fortalezas de autenticación integradas (MFA, MFA sin contraseña y MFA resistente al phishing) y personalizadas, con la tabla de combinaciones de métodos que satisface cada una.
- [FAQ for Microsoft-provided SMS and voice retirement](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sms-voice-retirement-faq) · Documentación · Oficial · Microsoft Learn. Preguntas frecuentes sobre el retiro de SMS y voz: costos de proveedores, efecto en SSPR, B2B, External ID, métodos externos de MFA y elegibilidad de Global Administrator vía PIM.
- [Platform Credential for macOS authentication method in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-platform-credential-for-macos) · Documentación · Oficial · Microsoft Learn · 18 nov 2025. Explica la credencial de plataforma para macOS, una clave vinculada al hardware en Secure Enclave que permite inicio de sesión sin contraseña y resistente al phishing, incluido el uso en desafíos WebAuthn.

### Anuncios y blogs oficiales

- [Microsoft Entra ID security updates: Passkeys are the default authentication method in Entra ID](https://www.microsoft.com/en-us/security/blog/2026/07/13/microsoft-entra-id-security-updates-passkeys-are-the-default-authentication-method-in-entra-id/) · Blog oficial · Empleado de Microsoft · Nuevo · Nadim Abdo (CVP Identity and Network Access) · Microsoft Security Blog · 13 jul 2026. Anuncia que desde el 1 de septiembre de 2026 las passkeys pasan a ser el método predeterminado en Entra ID y que el 1 de febrero de 2027 Microsoft deja de proveer la entrega telefónica de SMS y voz.
- [What's New in Microsoft Entra: June 2026](https://techcommunity.microsoft.com/blog/microsoft-entra-blog/whats-new-in-microsoft-entra-june-2026/4517885) · Blog oficial · Oficial · Nuevo · Martin Coetzer · Microsoft Entra Blog (Tech Community) · 1 jun 2026. Resumen mensual que anuncia MFA resistente al phishing en escritorios Linux, autenticación preferida por el sistema para primer y segundo factor y campañas de registro para passkeys.

### Webinars, videos y podcasts

- [Synced Passkeys in Microsoft Entra for Phishing-resistant MFA](https://www.youtube.com/watch?v=36nIaSBJ7_U) · Video · Empleado de Microsoft · Jarred Boone · Microsoft Mechanics (YouTube) · dic 2025. Video que muestra el registro y uso de passkeys sincronizadas y vinculadas al dispositivo, su configuración por el administrador, la recuperación con Verified ID y su uso en acceso condicional.

### Laboratorios, GitHub y herramientas

- [How to migrate MFA and SSPR policy settings to the Authentication methods policy for Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-authentication-methods-manage) · Laboratorio · Oficial · Microsoft Learn. Procedimiento guiado (asistente automático o manual) para consolidar los métodos de las políticas heredadas de MFA y SSPR en la política de métodos de autenticación, de forma reversible.

### Comunidad: blogs, libros, newsletters y eventos

- [JanBakker.tech – sharing is caring](https://janbakker.tech/) · Blog · MVP · Nuevo · Jan Bakker · JanBakker.tech · 3 nov 2026. Blog práctico con guías recientes sobre asegurar el registro de passkeys con acceso condicional, configurar SMS y voz con proveedor propio y bucles de políticas con fortalezas de autenticación.
- [Improving passkey registration experiences](https://nathanmcnulty.com/blog/2025/09/improving-passkey-registration-experiences/) · Blog · MVP · Nathan McNulty · 9 sep 2025. Explica cómo evitar que las políticas de dispositivo conforme o protección de apps bloqueen el registro de passkeys en Authenticator mediante una exclusión acotada y compensada.

**Manos a la obra**

1. `Laboratorio` Migra los métodos de las políticas heredadas de MFA y SSPR a la política de métodos con el asistente y habilita passkeys y TAP para un grupo piloto. Evidencia: migración marcada como completada y política exportada ([migrar a la política de métodos](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-authentication-methods-manage)).
2. `Laboratorio parcial` Crea dos perfiles de passkey —vinculadas al dispositivo con atestación para administradores y sincronizadas para usuarios— y lanza una campaña de registro para el piloto. Limitación: registrar passkeys exige un teléfono o un PC reales ([MC1221452](https://mc.merill.net/message/MC1221452)).
3. `Laboratorio` Crea una fortaleza de autenticación personalizada y comprueba con What If y con un inicio de sesión real qué métodos la satisfacen; confirma que TAP solo satisface la fortaleza MFA ([fortalezas](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-strengths)).
4. `Laboratorio parcial` Registra para la misma cuenta de prueba una passkey en Microsoft Authenticator y otra en una llave de seguridad, y verifica en los registros de inicio de sesión qué método usó cada acceso. Limitación: requiere teléfono y llave reales.
5. `Laboratorio` Diseña tu plan por persona con la [guía de despliegue](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-deploy-phishing-resistant-passwordless-authentication): administradores, usuarios regulados y el resto, con credencial portable o local, versiones mínimas de sistema operativo y fases de registro, uso y cumplimiento.
6. `Solo producción` Plan de retiro de SMS y voz: ejecuta el script oficial para encontrar usuarios que dependen de SMS o voz, clasifícalos por persona y decide entre passkeys y proveedor telefónico. Cómo hacerlo seguro: lectura con Reports Reader o Global Reader, una política en solo informe con fortaleza resistente al phishing para medir el impacto, comunicación previa y oleadas por grupo ([retiro de SMS y voz](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sms-voice-retirement)).

**¿Quieres profundizar?**

- [JanBakker.tech – sharing is caring](https://janbakker.tech/) · Blog
- [Improving passkey registration experiences](https://nathanmcnulty.com/blog/2025/09/improving-passkey-registration-experiences/) · Blog
- [How to migrate MFA and SSPR policy settings to the Authentication methods policy for Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-authentication-methods-manage) · Laboratorio

<a id="i4"></a>

## I4 · Acceso condicional esencial: línea base, solo informe y What If

*L100–L200 · ~8 h · Origen: SC-300 · Implement authentication and access management; Applied Skills APL-0501*

El **acceso condicional** es el motor de políticas de Zero Trust de Entra: evalúa señales —usuario o identidad, recurso, dispositivo, ubicación, riesgo, plataforma, flujo de autenticación— y decide si bloquea, concede con controles o limita la sesión. Requiere P1. Una línea base mínima bloquea la autenticación heredada (más del 99 % del password spray la usa) y el device code flow donde no se necesite, exige MFA —mejor, una fortaleza— a todos, MFA resistente al phishing a los administradores y protege el registro de información de seguridad.

Microsoft ya despliega por ti **políticas administradas**: las crea en modo solo informe y las activa al menos 30 días después, con aviso dos semanas antes. En 2026 incluyen, entre otras, bloquear agentes de alto riesgo (vista previa), bloquear autenticación heredada y device code flow, MFA para administradores y para todos, políticas de riesgo y MFA resistente al phishing para administradores del modo de seguridad de línea base (Baseline security mode). No se pueden renombrar ni borrar: revisa en cada una su estado y sus exclusiones.

El método de trabajo es siempre el mismo: plantilla o diseño propio, **modo solo informe**, simulación con **What If** —que usa la API What If Evaluation de Microsoft Graph y ya simula service principals e identidades de agente en vista previa—, medición con la vista de impacto y el workbook de información, y activación por oleadas, con las cuentas de emergencia excluidas. La línea base completa está en [Línea base de acceso condicional](00_Programa.md#acceso-condicional-base).

**Por qué importa**

Una línea base bien desplegada bloquea la mayoría de los ataques automatizados de identidad con muy poco costo, y el modo solo informe permite medir el impacto antes de afectar a nadie. Métricas: porcentaje de inicios de sesión cubiertos por al menos una política, inicios de sesión con autenticación heredada (meta: cero) y excepciones activas con fecha de vencimiento.

**Qué vas a lograr**

- Explicar los componentes de una política: asignaciones, condiciones, controles de concesión y de sesión.
- Desplegar una línea base en modo solo informe con exclusión de cuentas de emergencia.
- Validar el impacto con What If, la vista de impacto de políticas y el workbook de información.
- Gestionar las políticas administradas por Microsoft y su calendario de activación.

> **Novedad.** Las políticas administradas por Microsoft de 2026 incluyen bloquear agentes de alto riesgo (vista previa), autenticación heredada y device code flow; MFA para administradores, para todos y para usuarios con MFA por usuario; políticas de riesgo; y MFA resistente al phishing para administradores del Baseline security mode. Se crean en solo informe, se activan al menos 30 días después con aviso dos semanas antes y no se pueden renombrar ni borrar ([políticas administradas](https://learn.microsoft.com/en-us/entra/identity/conditional-access/managed-policies)).

> **Atención.** Contradicción de licencia: la página de políticas administradas pide «P2 o Business Premium», mientras la de [licencias](https://learn.microsoft.com/en-us/entra/fundamentals/licensing) indica que el acceso condicional requiere P1. Si tu tenant solo tiene E3, verifica en el portal cuáles se crearon.

> **Consejo Ninja.** What If usa la API What If Evaluation de Microsoft Graph y ya simula service principals e identidades de agente (vista previa), pero no evalúa dependencias de servicio: Teams depende de Exchange Online ([What If](https://learn.microsoft.com/en-us/entra/identity/conditional-access/what-if-tool)). En solo informe, una política que exige dispositivo conforme puede mostrar avisos de certificado en macOS, iOS y Android ([solo informe](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-report-only)).

> **Qué cambió.** «All cloud apps» ahora se llama «All resources». Más del 99 % de los ataques de password spray usan protocolos heredados: bloquearlos es la política con mejor relación costo-beneficio ([bloquear autenticación heredada](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-block-legacy-authentication)).

**¿Tienes poco tiempo?**

- [Microsoft-managed Conditional Access policies](https://learn.microsoft.com/en-us/entra/identity/conditional-access/managed-policies) · Documentación
- [Analyze Conditional Access policy impact (report-only mode)](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-report-only) · Documentación
- [Troubleshoot Conditional Access policies with the What If tool](https://learn.microsoft.com/en-us/entra/identity/conditional-access/what-if-tool) · Laboratorio
- [Block legacy authentication with Conditional Access](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-block-legacy-authentication) · Laboratorio

### Documentación, cursos y credenciales

- [Microsoft-managed Conditional Access policies](https://learn.microsoft.com/en-us/entra/identity/conditional-access/managed-policies) · Documentación · Oficial · Nuevo · Microsoft Learn · 8 ago 2026. Describe las políticas de acceso condicional que Microsoft crea en modo solo informe y activa tras al menos 30 días, incluidas MFA para administradores y usuarios, bloqueo de autenticación heredada y de device code flow, y políticas de riesgo.
- [Conditional Access insights and reporting workbook](https://learn.microsoft.com/en-us/entra/identity/conditional-access/howto-conditional-access-insights-reporting) · Documentación · Oficial · Microsoft Learn. Explica cómo usar el workbook de información e informes de acceso condicional sobre Log Analytics para medir el impacto de políticas activas o en solo informe hasta 90 días.
- [Analyze Conditional Access policy impact (report-only mode)](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-report-only) · Documentación · Oficial · Microsoft Learn. Describe el modo solo informe, sus resultados posibles (éxito, fallo, acción de usuario requerida, no aplicado) y las vistas de impacto de políticas, registros y workbooks para validar antes de aplicar.

### Laboratorios, GitHub y herramientas

- [Block legacy authentication with Conditional Access](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-block-legacy-authentication) · Laboratorio · Oficial · Microsoft Learn. Guía para identificar en los registros el uso de autenticación heredada y bloquearla mediante una política de acceso condicional o plantilla, empezando en solo informe.
- [Troubleshoot Conditional Access policies with the What If tool](https://learn.microsoft.com/en-us/entra/identity/conditional-access/what-if-tool) · Laboratorio · Oficial · Microsoft Learn. Explica la herramienta What If, basada en la API What If Evaluation de Microsoft Graph, para simular inicios de sesión de usuarios, identidades de agente (preview) o service principals y ver qué políticas aplican.
- [Block authentication flows with Conditional Access policy](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-block-authentication-flows) · Laboratorio · Oficial · Microsoft Learn · 7 abr 2026. Procedimiento para auditar y bloquear device code flow y transferencia de autenticación con acceso condicional, empezando en modo solo informe y excluyendo cuentas de emergencia.

### Comunidad: blogs, libros, newsletters y eventos

- [Entra ID Conditional Access Policy Design Baseline with Automatic Deployment Support](https://danielchronlund.com/category/conditional-access/page/11/) · Blog · MVP · Legado aún útil · Daniel Chronlund · Daniel Chronlund Cloud Security Blog · 26 nov 2024. Línea base de diseño de acceso condicional con nomenclatura por capas (BLOCK, GRANT, SESSION) desplegable en solo informe con el módulo DCToolbox. *Nota:* Versión 15 (2024-11-26); revisar contra las políticas administradas por Microsoft de 2026. Evidencia MVP: entrada propia 'A Security MVP's Take on Cloud Security in 2023'

**Manos a la obra**

1. `Laboratorio` Despliega CA01 a CA05 de la [línea base](00_Programa.md#acceso-condicional-base) en modo solo informe —parte de las plantillas de acceso condicional cuando existan, como la de bloqueo de autenticación heredada— con las cuentas de emergencia excluidas en las que puedan bloquear. Evidencia: exportación JSON de las políticas ([bloquear autenticación heredada](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-block-legacy-authentication)).
2. `Laboratorio` Simula con [What If](https://learn.microsoft.com/en-us/entra/identity/conditional-access/what-if-tool) tres escenarios —usuario con autenticación heredada, administrador desde un equipo no administrado y cuenta de emergencia— y guarda el resultado de cada uno.
3. `Laboratorio` Revisa durante una semana la pestaña de solo informe de los registros y la vista de impacto de políticas; clasifica los resultados en éxito, fallo, acción de usuario requerida y no aplicado ([solo informe](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-report-only)).
4. `Laboratorio` Audita quién usa device code flow antes de bloquearlo y documenta las excepciones legítimas, como salas de reuniones ([bloquear flujos de autenticación](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-block-authentication-flows)).
5. `Laboratorio parcial` Habilita el [workbook de información e informes](https://learn.microsoft.com/en-us/entra/identity/conditional-access/howto-conditional-access-insights-reporting) sobre Log Analytics y mide el impacto de dos políticas. Limitación: Log Analytics tiene costo de ingesta y el laboratorio genera poco volumen; en producción, usa Security Reader, retención acotada y de 2 a 4 semanas de análisis.
6. `Solo producción` Revisa las políticas administradas por Microsoft de tu tenant antes de su activación automática: estado, exclusiones y fecha. Cómo hacerlo seguro: Security Reader o Global Reader, comparación con tu línea base y una decisión documentada de mantener, ajustar o reemplazar cada una ([políticas administradas](https://learn.microsoft.com/en-us/entra/identity/conditional-access/managed-policies)).

**¿Quieres profundizar?**

- [Entra ID Conditional Access Policy Design Baseline with Automatic Deployment Support](https://danielchronlund.com/category/conditional-access/page/11/) · Blog
- [Block authentication flows with Conditional Access policy](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-block-authentication-flows) · Laboratorio

<a id="i5"></a>

## I5 · Identidad híbrida: Connect Sync, Cloud Sync, PHS y Kerberos de Entra

*L100–L200 · ~10 h · Origen: SC-300 · Implement and manage user identities (identidad híbrida)*

La mayoría de las grandes organizaciones de MCSA siguen con Active Directory local. **Entra Connect Sync** o **Entra Cloud Sync** sincronizan las identidades, y la autenticación puede resolverse con **sincronización de hash de contraseñas (PHS)**, autenticación de paso a través (PTA) o federación con AD FS. Microsoft recomienda PHS como la opción más simple y resiliente, y algunas capacidades —como la detección de credenciales filtradas de ID Protection— la necesitan aunque uses otro método.

**Cloud Sync es la dirección estratégica**: el aprovisionamiento de grupos hacia AD y la gestión del origen de autoridad (Source of Authority) se desarrollan principalmente allí. La herramienta guiada de migración desde Connect Sync llegó a disponibilidad general en octubre de 2026 y la sincronización de dispositivos con Cloud Sync está en vista previa desde agosto. Si sigues en Connect Sync, hay una fecha que no puedes perder: versión 2.6.84.0 o superior con autenticación basada en aplicación antes del 7 de abril de 2027, o la sincronización se detiene.

También verás cómo salir de AD FS con **staged rollout**, cómo reemplazar las tarjetas inteligentes de AD FS con **CBA nativo** y qué aporta **Kerberos de Entra** (Microsoft Entra Kerberos), que permite a Entra ID emitir tickets Kerberos para que credenciales sin contraseña lleguen a recursos locales y a servicios como Azure Files. Y por qué el servidor de sincronización debe tratarse como **Tier 0**.

**Por qué importa**

El servidor de sincronización es una puerta al tenant y una actualización omitida puede detener la sincronización de toda la organización en abril de 2027. Elegir PHS y planificar la salida de AD FS reduce dependencias locales, mejora la resiliencia ante caídas y habilita detecciones de credenciales filtradas. Métricas: versión de Connect, días hasta la fecha límite y porcentaje de usuarios con autenticación en la nube.

**Qué vas a lograr**

- Elegir el método de autenticación híbrida con el árbol de decisión de Microsoft.
- Comparar Connect Sync y Cloud Sync y evaluar la migración guiada.
- Planificar la actualización obligatoria de Connect Sync antes del 7 de abril de 2027.
- Diseñar la salida de AD FS con staged rollout y CBA nativo.
- Proteger el servidor de sincronización y las cuentas híbridas como activos Tier 0.

> **Atención.** Fecha que no puedes perder: Connect Sync debe estar en la versión 2.6.84.0 o superior, con autenticación basada en aplicación, antes del 7 de abril de 2027, o la sincronización se detiene. Las versiones 1.x ya no funcionan, cada 2.x se retira 12 meses después de la siguiente y el instalador solo se descarga del centro de administración de Entra (requiere .NET 4.7.2 y TLS 1.2; las últimas listadas son 2.6.91.0 y 2.6.92.0) ([historial de versiones](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/reference-connect-version-history)).

> **Novedad.** La herramienta guiada de migración de Connect Sync a Cloud Sync llegó a GA en octubre de 2026 y la sincronización de dispositivos para unión híbrida con Cloud Sync está en vista previa desde agosto ([novedades de octubre](https://techcommunity.microsoft.com/blog/microsoft-entra-blog/what%E2%80%99s-new-in-microsoft-entra-october-2026/4556460), [novedades de agosto](https://techcommunity.microsoft.com/blog/microsoft-entra-blog/whats-new-in-microsoft-entra-august-2026/4545172)).

> **Consejo Ninja.** PHS es la opción más simple y resiliente, y conviene activarla aunque uses PTA o federación: la detección de credenciales filtradas de ID Protection la necesita ([elegir el método](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/choose-ad-authn), [resiliencia híbrida](https://learn.microsoft.com/en-us/entra/architecture/resilience-in-hybrid)).

> **Consejo Ninja.** Al salir de AD FS, usa staged rollout como prueba temporal con grupos piloto, mantén AD FS como respaldo y prepara la reversión: convertir un dominio federado a administrado puede tardar hasta 60 minutos. Para tarjetas inteligentes, migra a CBA nativo con reglas de certificateUserIds y trata el servidor de Entra Connect como Tier 0 ([migrar desde federación](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/migrate-from-federation-to-cloud-authentication), [migrar a CBA](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-certificate-based-authentication-migration)).

**¿Tienes poco tiempo?**

- [Microsoft Entra Connect: Version release history](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/reference-connect-version-history) · Documentación
- [Migrate from Microsoft Entra Connect Sync to Cloud Sync: decision guide](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/connect-to-cloud-sync-decision-guide) · Documentación
- [Choose the right authentication method for your Microsoft Entra hybrid identity solution](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/choose-ad-authn) · Documentación
- [Migrate from federation to cloud authentication](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/migrate-from-federation-to-cloud-authentication) · Documentación

### Documentación, cursos y credenciales

- [Migrate from Microsoft Entra Connect Sync to Cloud Sync: decision guide](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/connect-to-cloud-sync-decision-guide) · Documentación · Oficial · Microsoft Learn. Guía de decisión que presenta Cloud Sync como dirección estratégica de Microsoft para la sincronización híbrida, compara capacidades con Connect Sync y ofrece evaluación de preparación para migrar.
- [Choose the right authentication method for your Microsoft Entra hybrid identity solution](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/choose-ad-authn) · Documentación · Oficial · Microsoft Learn. Árbol de decisión y comparación entre sincronización de hash de contraseña, autenticación de paso a través y federación, independiente de usar Connect Sync o Cloud Sync.
- [Microsoft Entra Connect: Version release history](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/reference-connect-version-history) · Documentación · Oficial · Microsoft Learn. Historial oficial de versiones de Entra Connect Sync con la política de retiro a 12 meses, las versiones 1.x no funcionales y la actualización obligatoria a 2.6.84.0+ con autenticación basada en aplicación antes del 7 de abril de 2027.
- [Migrate from federation to cloud authentication](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/migrate-from-federation-to-cloud-authentication) · Documentación · Oficial · Microsoft Learn. Guía completa para pasar de AD FS a PHS o PTA con planificación, comunicación, ventana de mantenimiento, plan de reversión y desmantelamiento de AD FS.
- [Build resilience in your hybrid architecture](https://learn.microsoft.com/en-us/entra/architecture/resilience-in-hybrid) · Documentación · Oficial · Microsoft Learn. Guía de resiliencia que recomienda PHS como opción más simple y resistente, explica dependencias de PTA y federación y propone CBA para eliminar AD FS.
- [Migrate from federation to Microsoft Entra certificate-based authentication (CBA)](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-certificate-based-authentication-migration) · Documentación · Oficial · Microsoft Learn. Describe cómo trasladar la autenticación con certificados de AD FS a CBA nativo de Entra mediante staged rollout y reglas de sincronización de certificateUserIds.

### Laboratorios, GitHub y herramientas

- [Migrate to cloud authentication using Staged Rollout](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-staged-rollout) · Laboratorio · Oficial · Microsoft Learn. Explica el despliegue por etapas para probar autenticación en la nube con grupos piloto antes de convertir dominios federados, con escenarios soportados y no soportados.

**Manos a la obra**

1. `Laboratorio` Recorre el árbol de decisión de métodos de autenticación con los datos de tu organización y documenta la elección (PHS, PTA o federación) con sus dependencias ([elegir el método](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/choose-ad-authn)).
2. `Laboratorio parcial` Despliega un AD de laboratorio en una VM de Azure, instala el agente de Cloud Sync, sincroniza una OU piloto y prueba el umbral de borrado accidental. Limitación: no reproduce la complejidad de un bosque real ([guía de decisión de Cloud Sync](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/connect-to-cloud-sync-decision-guide)).
3. `Laboratorio parcial` Instala Connect Sync en otra VM del laboratorio, ejecuta la evaluación de preparación y prueba la herramienta guiada de migración a Cloud Sync. Limitación: el laboratorio no tiene las reglas personalizadas de un servidor real; en producción, usa el servidor en modo staging y migra por OU piloto.
4. `Laboratorio` Inventaria los activos Tier 0 de tu identidad híbrida (servidores de Connect, AD FS y PKI, y las cuentas que los administran) y verifica que las cuentas privilegiadas de Entra sean solo de nube.
5. `Solo producción` Actualiza Connect Sync a 2.6.84.0 o superior con autenticación basada en aplicación antes del 7 de abril de 2027. Cómo hacerlo seguro: actualiza primero el servidor en modo staging, respalda y exporta la configuración, usa una ventana de cambio y deja documentada la reversión ([historial de versiones](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/reference-connect-version-history)).
6. `Solo producción` Staged rollout de AD FS a PHS con un grupo piloto pequeño. Cómo hacerlo seguro: mantén AD FS como respaldo, comunica al piloto, monitorea los inicios de sesión fallidos y documenta la reversión antes de convertir el dominio ([staged rollout](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-staged-rollout)).

**¿Quieres profundizar?**

- [Migrate to cloud authentication using Staged Rollout](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-staged-rollout) · Laboratorio

<a id="i6"></a>

## I6 · Laboratorios de práctica: tu tenant de identidad

*L100–L200 · ~8 h · Origen: Applied Skills APL-0501, ruta de Learn de identidad y TechLab de Entra Suite*

El Ninja siempre fue práctico: leer no alcanza. Tu entorno base es una prueba de **Microsoft 365 E5** —que incluye Entra ID P2— más una suscripción de Azure con créditos de Visual Studio Enterprise para Log Analytics, máquinas virtuales de Active Directory y Logic Apps. Sobre esa base activarás pruebas por tiempo limitado cuando el módulo lo pida: Entra Suite, ID Governance (una sola vez por tenant) y Workload ID Premium (90 días).

Hay laboratorios oficiales listos para usar: la evaluación **Applied Skills** de identidades y acceso, la ruta de Learn «Implement an identity management solution» y el **TechLab de Entra Suite**, de cuatro horas, que puedes usar como guion. **Maester** y el **Zero Trust Assessment** te dan una verificación automática de la configuración desde el primer día.

Cuida los costos y la limpieza: alertas de presupuesto en Azure, retención mínima en Log Analytics y eliminación de máquinas virtuales al terminar. Recuerda además lo que el laboratorio no reproduce —volumen real, detecciones que dependen de comportamiento, varios tenants, la inclusión de Security Copilot en licencias pagas—; para eso está la estrategia de práctica segura en producción de cada ejercicio.

**Por qué importa**

Un laboratorio reproducible permite equivocarse sin consecuencias: probar políticas que bloquean, revocar sesiones o romper la sincronización sin afectar a nadie. También acelera la validación de cambios de Microsoft, como la activación de políticas administradas, antes de que lleguen a producción. Métrica: porcentaje de cambios de identidad probados en laboratorio antes de aplicarse.

**Qué vas a lograr**

- Armar un tenant de práctica con E5, pruebas complementarias y una suscripción de Azure con presupuesto.
- Completar la evaluación Applied Skills de identidades y acceso.
- Automatizar una verificación diaria de la configuración con Maester.
- Controlar costos y limpiar los recursos del laboratorio.

> **Consejo Ninja.** La combinación recomendada para la serie es un tenant nuevo con la prueba comercial de Microsoft 365 E5 más la suscripción de Azure de Visual Studio Enterprise en el mismo tenant. La prueba de E5 dura un mes y pide tarjeta: prepara todo antes de activarla (anexo común) y encadena después la [prueba de Entra Suite](https://learn.microsoft.com/en-us/entra/fundamentals/try-microsoft-entra-suite) y la de Workload ID Premium (90 días).

> **Novedad.** El TechLab «Entra Suite for Frontier Transformation» (octubre de 2026) propone cuatro horas de práctica: ciclo de vida, Private Access, acceso a tiempo con revisiones, filtrado de contenido, descubrimiento de tráfico MCP y protección contra inyección de prompts para personas y agentes. Está pensado para un formato interno, pero sirve como guion en tu tenant de prueba ([TechLab](https://github.com/microsoft/TechLab-Entra-Suite-for-Frontier-Transformation/)).

> **Atención.** Maester 3.0 está en vista previa desde el 8 de octubre de 2026 (requiere PowerShell 7.4 o superior y rompe compatibilidad): en automatización fija la versión estable con `Install-Module Maester -RequiredVersion 2.3.0` hasta que 3.0 sea definitiva ([Maester 3.0](https://maester.dev/blog/maester-3-0)).

**¿Tienes poco tiempo?**

- [Microsoft Applied Skills: Get started with identities and access using Microsoft Entra](https://learn.microsoft.com/en-us/credentials/applied-skills/get-started-with-identities-and-access-using-microsoft-entra/) · Credencial
- [Implement an identity management solution using Microsoft Entra ID](https://learn.microsoft.com/en-us/training/paths/implement-identity-management-solution/) · Curso
- [Maester: open-source security testing for Microsoft 365](https://maester.dev/) · Herramienta
- [TechLab: Entra Suite for Frontier Transformation](https://github.com/microsoft/TechLab-Entra-Suite-for-Frontier-Transformation/) · Laboratorio

**Manos a la obra**

1. `Laboratorio` Arma tu laboratorio según el anexo común: prueba de Microsoft 365 E5, suscripción de Azure con presupuesto y alertas, convención de nombres y un administrador separado de tu cuenta de uso diario. Evidencia: captura del presupuesto y lista de pruebas con su fecha de vencimiento.
2. `Laboratorio` Crea diez usuarios de prueba en tres departamentos y dos países, con atributos de RR. HH. como employeeHireDate, que reutilizarás en M4 y X4.
3. `Laboratorio` Programa [Maester](https://maester.dev/) en GitHub Actions o Azure DevOps con la versión 2.3.0 fijada y un informe diario.
4. `Laboratorio` Completa la evaluación [Applied Skills](https://learn.microsoft.com/en-us/credentials/applied-skills/get-started-with-identities-and-access-using-microsoft-entra/) de identidades y acceso y guarda la credencial.
5. `Laboratorio parcial` Usa el [TechLab de Entra Suite](https://github.com/microsoft/TechLab-Entra-Suite-for-Frontier-Transformation/) como guion con la prueba de Entra Suite activa. Limitación: el TechLab pide datos de un formato interno; adapta los pasos a tu tenant.
6. `Laboratorio` Define y prueba tu rutina de limpieza: apagar VMs, revisar Cost Management y registrar la fecha de vencimiento de cada prueba para cancelarla a tiempo.

<a id="reto-inicial"></a>

## Reto del nivel

**Tu tenant con línea base en una semana.** En tu laboratorio, crea dos cuentas de emergencia con passkey FIDO2 y alerta de uso, migra los métodos a la política de métodos con passkeys y TAP, despliega CA01 a CA07 de la [línea base](00_Programa.md#acceso-condicional-base) en solo informe, protege la edición del acceso condicional con una acción protegida y ejecuta Maester antes y después. Entrega: informe de una página con capturas de What If para tres escenarios, el resultado de Maester y tu plan de retiro de SMS y voz con fechas y responsables.

<a id="quiz-inicial"></a>

## Evaluación del nivel

Responde y compara con [Evaluaciones y respuestas](06_Evaluaciones_y_respuestas.md#eval-inicial). Con 80 % o más, ¡nivel aprobado! (En la versión web puedes corregir en línea y generar tu certificado).

1. ¿Qué plan de Microsoft Entra incluye Microsoft 365 E5?
   - a) Entra Suite
   - b) Entra ID P2
   - c) Entra ID Governance completo
   - d) Internet Access

2. ¿Qué licencia necesita el perfil de tráfico de Microsoft de Global Secure Access?
   - a) Entra Suite
   - b) Internet Access
   - c) Workload ID Premium
   - d) Entra ID P1 o P2

3. ¿Qué se necesita para aplicar acceso condicional a los agentes de IA?
   - a) Solo Entra ID P1
   - b) Workload ID Premium
   - c) Microsoft 365 E7, o Agent 365 más al menos P1 o E3
   - d) Nada adicional: Agent ID es gratuito para todos

4. ¿A qué operaciones afecta la fase 2 del MFA obligatorio de Azure, vigente desde el 1 de octubre de 2025?
   - a) Crear, actualizar y borrar recursos de Azure por CLI, PowerShell, IaC, REST y SDK
   - b) Solo el inicio de sesión en el portal de Azure
   - c) Las identidades administradas y los service principals
   - d) Solo las lecturas de la API

5. ¿Qué método recomienda Microsoft para proteger las cuentas de emergencia?
   - a) SMS
   - b) Llamada de voz
   - c) Passkey FIDO2
   - d) Ninguno: deben quedar sin MFA

6. Asocias una acción protegida a una política de acceso condicional que está en modo solo informe. ¿Qué ocurre?
   - a) Protege igual que una política activa
   - b) Bloquea a todos los administradores
   - c) Solo resta puntos en Identity Secure Score
   - d) No protege la acción: la política debe estar activada

7. ¿Cuándo deja Microsoft de entregar SMS y voz a los Global Administrators activos y a los usuarios externos?
   - a) 1 de febrero de 2027
   - b) 1 de julio de 2027
   - c) 1 de septiembre de 2026
   - d) 7 de abril de 2027

8. Desde el 30 de septiembre de 2025, ¿dónde se gestionan los métodos de autenticación?
   - a) En la política de métodos de autenticación
   - b) En la configuración de MFA por usuario
   - c) En la política heredada de SSPR
   - d) En los valores predeterminados de seguridad

9. ¿Qué método NO satisface la fortaleza de autenticación «MFA resistente al phishing»?
   - a) Llave de seguridad FIDO2
   - b) CBA multifactor
   - c) Temporary Access Pass
   - d) Windows Hello for Business

10. Una política de acceso condicional administrada por Microsoft se crea en solo informe. ¿Cuándo se activa?
   - a) Al menos 30 días después de crearse, con aviso dos semanas antes
   - b) De inmediato
   - c) A los 7 días
   - d) Nunca, salvo que la actives tú

11. ¿Qué NO evalúa la herramienta What If de acceso condicional?
   - a) Inicios de sesión de usuarios
   - b) Service principals
   - c) Identidades de agente (vista previa)
   - d) Dependencias de servicio, como la de Teams con Exchange Online

12. ¿Qué necesita Entra Connect Sync para seguir sincronizando después del 7 de abril de 2027?
   - a) La versión 2.5.79.0
   - b) Migrar a AD FS
   - c) La versión 2.6.84.0 o superior con autenticación basada en aplicación
   - d) Activar Connect Health

13. ¿Por qué conviene activar la sincronización de hash de contraseñas aunque uses PTA o federación?
   - a) Porque reemplaza a Cloud Sync
   - b) Porque la detección de credenciales filtradas de ID Protection la necesita
   - c) Porque elimina la necesidad de MFA
   - d) Porque es obligatoria desde 2026

14. ¿Cuánto dura por defecto un token de acceso de Microsoft Entra?
   - a) 5 minutos
   - b) 24 horas
   - c) 90 días
   - d) 1 hora

15. Lanzas el laboratorio de la credencial Applied Skills de identidades y acceso y no lo terminas. ¿Qué ocurre?
   - a) Debes esperar 72 horas para relanzarlo
   - b) Puedes relanzarlo de inmediato
   - c) Pierdes tu certificación SC-300
   - d) Debes pagar un nuevo intento

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

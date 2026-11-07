# Nivel 1 · Inicial · Fundamentos con privacidad por diseño

*Microsoft Purview Insider Risk Management Ninja Training · Edición 2026*

[← Programa](00_Programa.md) · [Índice del programa](README.md) · [Nivel 2 · Intermedio →](02_Nivel_2_Intermedio.md)

<a id="inicial"></a>

Purview y sus prerrequisitos, privacidad por diseño, licencias, indicadores, conectores y el triage en la cola unificada. Terminas con tu primera política de prueba, alertas clasificadas con criterio y un caso abierto con su evidencia.

*L100–L200 · 5 módulos · ~18 horas · 32 recursos*

**Módulos de este nivel:** [P0 Prerrequisitos y auditoría](#p0) · [I0 Cómo aprender](#i0) · [I1 Privacidad y licencias](#i1) · [I2 Indicadores y conectores](#i2) · [I3 Triage y casos](#i3)

<a id="p0"></a>

## P0 · Prerrequisitos: Microsoft Purview, auditoría y permisos

*L100 · ~3 h · Origen: Ninja oficial de IRM · «Getting Started» (prerrequisitos y permisos), actualizado al portal de Microsoft Purview*

Insider Risk Management (IRM) se administra desde el portal de Microsoft Purview y depende de piezas que conviene tener listas antes de crear la primera política. La principal es el **registro de auditoría unificado**: IRM lo usa para sus políticas y analíticas. Viene activado por defecto en la mayoría de los tenants empresariales, pero no en licencias para pymes ni en tenants no administrados con pruebas gratuitas, que es justo el caso típico de un laboratorio; activarlo tarda hasta 60 minutos y la búsqueda está disponible horas después. Además, IRM solo está disponible en tenants hospedados en regiones con las dependencias de Azure soportadas: verifica la de tu tenant antes de prometer la capacidad a un país de MCSA.

La segunda pieza son los **permisos**. Purview usa grupos de roles propios, roles de Entra ID y, como práctica recomendada, PIM para grupos. En riesgo interno esto no es un detalle: un administrador global no ve IRM por defecto, y quién configura, quién clasifica alertas y quién ve contenido deben ser personas distintas. Desde julio de 2026, las asignaciones a grupos de roles de Purview admiten fecha de vencimiento (de 1 día a 2 años), ideal para investigadores temporales. Por último, la configuración global —privacidad, indicadores, exclusiones, grupos de detección, ventanas de política y notificaciones— aplica a todas las políticas, sin importar la plantilla.

**Por qué importa**

Sin auditoría, IRM no ve nada; sin separación de funciones, una herramienta pensada para proteger datos se convierte en un riesgo para la privacidad de los empleados. Dejar listos el día 0 la auditoría, los roles con vencimiento y la convención de nombres ahorra semanas: las analíticas tardan hasta 48 horas, las primeras alertas unas 24 horas y los nombres de las políticas no se pueden cambiar después de crearlas.

**Qué vas a lograr**

- Verificar y, si hace falta, activar el registro de auditoría unificado del tenant, dejando evidencia.
- Comprobar la disponibilidad de IRM según la región de hospedaje del tenant.
- Diseñar una matriz de grupos de roles con mínimo privilegio y asignaciones con vencimiento.
- Ubicar los ajustes globales de IRM y explicar por qué afectan a todas las políticas.
- Definir una convención de nombres para políticas, grupos y casos de práctica.

> **Atención.** La auditoría no viene activada por defecto en licencias para pymes ni en tenants no administrados con pruebas gratuitas de licencias empresariales, que es el caso típico de un laboratorio con la prueba de Microsoft 365 E5; activarla puede tardar hasta 60 minutos ([activar o desactivar la auditoría](https://learn.microsoft.com/en-us/purview/audit-log-enable-disable)). IRM usa ese registro para sus políticas y analíticas ([Get started](https://learn.microsoft.com/en-us/purview/insider-risk-management-configure)).

> **Novedad.** Desde julio de 2026, las asignaciones a grupos de roles de Purview admiten fecha de vencimiento, de 1 día a 2 años, salvo eDiscovery Administrator y eDiscovery Manager ([What's new in Microsoft Purview](https://learn.microsoft.com/en-us/purview/whats-new)). Úsalas para investigadores temporales y para auditorías puntuales.

> **Atención.** IRM solo está disponible en tenants hospedados en regiones y países con las dependencias de Azure soportadas ([Get started](https://learn.microsoft.com/en-us/purview/insider-risk-management-configure)). Antes de comprometer la capacidad en un país de MCSA, verifica dónde está hospedado tu tenant.

> **Consejo Ninja.** Los administradores globales no tienen acceso a IRM por defecto y los indicadores vienen desactivados: la privacidad por diseño empieza en los permisos ([privacidad en la solución](https://learn.microsoft.com/en-us/purview/insider-risk-solution-privacy)). Purview recomienda mínimo privilegio y PIM para grupos ([permisos del portal de Purview](https://learn.microsoft.com/en-us/purview/purview-permissions)). Y como los nombres de las políticas de IRM no se pueden cambiar después de crearlas, define tu convención de nombres antes de empezar.

**¿Tienes poco tiempo?**

- [Get started with Insider Risk Management](https://learn.microsoft.com/en-us/purview/insider-risk-management-configure) · Documentación
- [Turn auditing on or off](https://learn.microsoft.com/en-us/purview/audit-log-enable-disable) · Documentación
- [Assign permissions in Insider Risk Management](https://learn.microsoft.com/en-us/purview/insider-risk-management-permissions) · Documentación
- [Permissions in the Microsoft Purview portal](https://learn.microsoft.com/en-us/purview/purview-permissions) · Documentación

### Documentación, cursos y credenciales

- [Turn auditing on or off](https://learn.microsoft.com/en-us/purview/audit-log-enable-disable) · Documentación · Oficial · Microsoft Learn. Cómo verificar y activar el registro de auditoría unificado, prerrequisito obligatorio de las políticas y analíticas de IRM.
- [Get started with auditing solutions](https://learn.microsoft.com/en-us/purview/audit-get-started) · Documentación · Oficial · Microsoft Learn. Pasos para Audit (Standard/Premium): licencias, roles Audit Reader/Manager, retención y búsqueda, base de evidencia para investigaciones de riesgo interno.
- [Permissions in the Microsoft Purview portal](https://learn.microsoft.com/en-us/purview/purview-permissions) · Documentación · Oficial · Microsoft Learn. Modelo RBAC del portal Microsoft Purview (roles, grupos de roles, roles de Entra, PIM para grupos y alcance) que sustenta la separación de funciones de IRM.

### Laboratorios, GitHub y herramientas

- [Microsoft Security Workshop - Insider Risk Management (laboratorio)](https://indra-pr.github.io/msft-security-workshop/purview/data-security/insider-risk-management/) · Laboratorio · Comunidad · Autor no identificado · GitHub Pages (Microsoft Security Workshop). Laboratorio comunitario guiado (~3 h) para crear una política de robo de datos por usuarios salientes, triagear alertas y activar Protección adaptativa.

**Manos a la obra**

1. `Laboratorio` En tu prueba de Microsoft 365 E5, verifica en el portal de Purview si el registro de auditoría unificado está activo; si no lo está, actívalo siguiendo [la guía oficial](https://learn.microsoft.com/en-us/purview/audit-log-enable-disable) y anota la hora. Evidencia: captura del estado y, unas horas después, una búsqueda de auditoría con resultados de tu propia actividad.
2. `Laboratorio` Crea cuatro cuentas de prueba y asígnales los grupos IRM Admins, IRM Analysts, IRM Investigators e IRM Approvers con fecha de vencimiento ([permisos de IRM](https://learn.microsoft.com/en-us/purview/insider-risk-management-permissions)). Comprueba que una cuenta con Global Administrator y sin rol de IRM no ve las alertas. Evidencia: matriz cuenta–grupo–vencimiento y captura del acceso denegado.
3. `Laboratorio` Define la convención de nombres `PRUEBA-IRM-<objetivo>-v<n>-<AAAAMM>` para políticas, grupos, casos y conectores, y regístrala en un documento de cambios: los nombres de las políticas de IRM no se pueden cambiar después de crearlas ([Get started](https://learn.microsoft.com/en-us/purview/insider-risk-management-configure)). Evidencia: convención publicada en el registro de cambios del laboratorio.
4. `Laboratorio` Recorre los ajustes globales de IRM (privacidad, indicadores, ventanas de política, detecciones inteligentes, notificaciones y exclusiones globales) y documenta el valor por defecto de cada uno antes de tocar nada ([ajustes de IRM](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings)). Evidencia: tabla de línea base con fecha.
5. `Solo producción` Inventaría quién tiene hoy acceso a IRM en producción, incluidos los roles de Entra que lo otorgan y los grupos de roles de Purview. Cómo hacerlo seguro: revisión de solo lectura con un rol de auditor, sin cambios hasta que el CISO y privacidad aprueben la nueva matriz; después, migra a PIM para grupos con aprobación y vencimiento ([permisos del portal de Purview](https://learn.microsoft.com/en-us/purview/purview-permissions)).

<a id="i0"></a>

## I0 · Cómo aprender Insider Risk Management y dónde pedir ayuda

*L100 · ~2 h · Origen: Ninja oficial de IRM (leyenda de recursos y knowledge checks) y ruta oficial de SC-401*

Este entrenamiento sigue un guion y no puede profundizar en cada pantalla; por eso cada módulo enlaza a la documentación de referencia. La puerta formal es la ruta de Microsoft Learn **Implement and manage Microsoft Purview Insider Risk Management**, alineada con el examen **SC-401** (que reemplazó a SC-400): cinco módulos, unas cuatro horas, con un ejercicio guiado de investigación de robo de datos y unidades nuevas sobre agentes de IA y Defender XDR. Está disponible en español, lo que la vuelve ideal para que RR. HH. y Legal compartan el vocabulario con el equipo técnico.

IRM cambia casi todos los meses, así que el segundo hábito es el radar: la página «What's new in Microsoft Purview» (actualizada el 16 de octubre de 2026), los avisos del Centro de mensajes —que puedes consultar en archivos públicos como mc.merill.net—, el blog de seguridad de Microsoft y la serie oficial de SC-401 en YouTube. El portal de adopción de Purview agrega guías interactivas de IRM y de Protección adaptativa para quien todavía no tiene tenant. Y para dudas puntuales, Tech Community y los referentes de la sección de comunidad suelen responder rápido.

**Por qué importa**

Un equipo formado con el material de 2024 busca la pestaña «Alerts (classic)», que ya no se usa, ignora el Triage Agent y no sabe que la IA y los agentes también son fuentes de riesgo interno. Una rutina de actualización de 30 minutos al mes evita configurar sobre supuestos vencidos y mantiene alineados a RR. HH., Legal y el SOC.

**Qué vas a lograr**

- Mapear las habilidades medidas de SC-401 sobre riesgo interno a los módulos de este programa.
- Completar los módulos introductorios de la ruta oficial de Learn y su ejercicio guiado.
- Armar un radar mensual de novedades con What's new, el Centro de mensajes y el blog de seguridad.
- Distinguir recursos oficiales, de empleados de Microsoft, de MVP y de la comunidad.

> **Novedad.** La guía de estudio de SC-401 se actualizó el 28 de octubre de 2026. Su dominio «Manage risks, alerts, and activities» (30–35 %) cubre roles, conectores, la integración con Defender for Endpoint, indicadores, plantillas, evidencia forense, Protección adaptativa, alertas, casos y avisos de IRM; se aprueba con 700 puntos ([guía de estudio SC-401](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-401)).

> **Qué cambió.** SC-400 se retiró el 31 de mayo de 2025 y SC-401 es hoy el examen de referencia para IRM ([guía comunitaria de SC-401](https://charbelnemnom.com/sc-401-exam-study-guide/)). Si tu equipo conserva material de SC-400, contrástalo con la guía vigente.

> **Consejo Ninja.** La ruta oficial en español ([Implementar y administrar Administración de riesgos internos](https://learn.microsoft.com/es-es/training/paths/purview-implement-insider-risk-management/)) es una traducción automática: úsala con RR. HH. y Legal, pero confirma fechas y estados en la [versión en inglés](https://learn.microsoft.com/en-us/training/paths/purview-implement-insider-risk-management/).

> **Consejo Ninja.** El portal de adopción de Purview reúne guías interactivas de IRM y de Protección adaptativa, demos de Mechanics y comunidades: sirven para mostrar la herramienta a RR. HH. sin abrir un tenant ([Microsoft Adoption · Purview](https://adoption.microsoft.com/en-us/microsoft-security/purview/)).

**¿Tienes poco tiempo?**

- [Implement and manage Microsoft Purview Insider Risk Management (SC-401)](https://learn.microsoft.com/en-us/training/paths/purview-implement-insider-risk-management/) · Curso
- [Study guide for Exam SC-401: Administering Information Security in Microsoft 365](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-401) · Credencial
- [Implement and manage Microsoft Purview Insider Risk Management | SC-401 | Episode 8](https://www.youtube.com/watch?v=v_j4zDVHphU) · Video
- [What's new in Microsoft Purview](https://learn.microsoft.com/en-us/purview/whats-new) · Documentación

### Documentación, cursos y credenciales

- [Study guide for Exam SC-401: Administering Information Security in Microsoft 365](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-401) · Credencial · Oficial · Nuevo · Microsoft Learn · 28 oct 2026. Guía oficial del examen SC-401 cuyo dominio "Manage risks, alerts, and activities" (30-35 %) cubre roles, conectores, integración con Defender for Endpoint, indicadores, plantillas, evidencia forense, Protección adaptativa, alertas, casos y avisos de IRM.
- [Implement and manage Microsoft Purview Insider Risk Management (SC-401)](https://learn.microsoft.com/en-us/training/paths/purview-implement-insider-risk-management/) · Curso · Oficial · Microsoft Learn. Ruta oficial de Microsoft Learn (5 módulos, ~4 h, 4900 XP) alineada con SC-401 que recorre fundamentos, preparación, políticas, investigación de alertas (con Security Copilot, agentes y Defender XDR) y Protección adaptativa.

### Webinars, videos y podcasts

- [Implement and manage Microsoft Purview Insider Risk Management | SC-401 | Episode 8](https://www.youtube.com/watch?v=v_j4zDVHphU) · Video · Oficial · Microsoft Learn (YouTube). Episodio oficial de la serie SC-401 sobre indicadores, flujos con privacidad, RBAC, conectores (RR. HH., endpoint, apps en la nube) y Protección adaptativa.
- [Insider Risk Management in Microsoft Purview (playlist)](https://www.youtube.com/playlist?list=PLXtHYVsvn_b9elAcF4WnjAYHFn0jRzX0Q) · Video · Oficial · Legado aún útil · Microsoft Mechanics. Lista de reproducción de Microsoft Mechanics con 5 videos de IRM, Protección adaptativa y DLP. *Nota:* Videos de 2022-2024; útiles como introducción visual, verificar interfaz actual

### Laboratorios, GitHub y herramientas

- [Microsoft Purview - Microsoft Adoption](https://adoption.microsoft.com/en-us/microsoft-security/purview/) · Herramienta · Oficial · Microsoft Adoption. Portal de adopción de Purview con enlaces a guías interactivas de IRM y Protección adaptativa, agentes de triage, demos de Mechanics y comunidades.

### Comunidad: blogs, libros, newsletters y eventos

- [Exam SC-401 Study Guide: Administering Information Security in Microsoft 365 (Charbel Nemnom)](https://charbelnemnom.com/sc-401-exam-study-guide/) · Blog · MVP · Nuevo · Charbel Nemnom · charbelnemnom.com · 29 jun 2026. Guía comunitaria del SC-401 con experiencia real del examen (duración, tipo de preguntas) y cronología del reemplazo de SC-400.

**Manos a la obra**

1. `Laboratorio` Descarga la [guía de estudio de SC-401](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-401) y arma una matriz habilidad medida → módulo de este programa para el dominio de riesgo interno. Evidencia: hoja de cálculo con cada habilidad cubierta y las brechas que detectes.
2. `Laboratorio` Completa el módulo [Understand Microsoft Purview Insider Risk Management](https://learn.microsoft.com/en-us/training/modules/purview-explore-insider-risk-management/) (28 minutos) y el ejercicio guiado «Investigate potential data theft using Insider Risk Management» de la [ruta oficial](https://learn.microsoft.com/en-us/training/paths/purview-implement-insider-risk-management/). Evidencia: progreso o insignia en tu perfil de Learn.
3. `Laboratorio` Crea tu radar de novedades: guarda [What's new in Microsoft Purview](https://learn.microsoft.com/en-us/purview/whats-new) en favoritos y registra en una tabla tres avisos del Centro de mensajes —[MC1430536](https://mc.merill.net/message/MC1430536), [MC1438568](https://mc.merill.net/message/MC1438568) y [MC1200579](https://mc.merill.net/message/MC1200579)— con fecha, impacto y módulo afectado. Evidencia: tabla del radar con su primera revisión.
4. `Laboratorio` Mira el [episodio 8 de la serie SC-401](https://www.youtube.com/watch?v=v_j4zDVHphU) y anota cinco conceptos que vas a configurar en I2: indicadores, RBAC, conectores, privacidad y Protección adaptativa. Evidencia: nota de una página con una pregunta abierta por concepto.

**¿Quieres profundizar?**

- [Microsoft Purview - Microsoft Adoption](https://adoption.microsoft.com/en-us/microsoft-security/purview/) · Herramienta

<a id="i1"></a>

## I1 · Insider Risk Management hoy: privacidad por diseño y licencias

*L100 · ~3 h · Origen: Ninja oficial de IRM · «Why do I need Insider Risk Management?», «Overview» y licencias*

El riesgo interno no es sinónimo de empleado malicioso: incluye la fuga accidental de datos, el robo de información por quien se va de la organización, las violaciones de políticas de seguridad en el dispositivo y, cada vez más, el uso riesgoso de la IA generativa y de los agentes. Insider Risk Management correlaciona señales de la auditoría de Microsoft 365, los dispositivos, el navegador, DLP, Defender for Endpoint, Communication Compliance y conectores como el de RR. HH. para detectar patrones y llevarlos por un flujo de detectar, clasificar, investigar y actuar.

Lo que hace aceptable a una herramienta así es la **privacidad por diseño**: los usuarios aparecen seudonimizados por defecto, el acceso se controla con grupos de roles, los indicadores vienen apagados hasta que alguien decide encenderlos y cada acción queda en el registro de auditoría. Microsoft es explícito en algo más: el cliente es el único responsable de usar IRM conforme a la ley aplicable y debe hacer su propia investigación completa, sin basarse solo en las conclusiones de la herramienta. Por eso este programa no da asesoría legal ni laboral: te indica cuándo involucrar a Legal, RR. HH. y privacidad.

En licencias, IRM viene en Microsoft 365 E5/A5/G5, en **Microsoft Purview Suite** (así se llama Microsoft 365 E5 Compliance desde el 1 de octubre de 2025; se agrega a Microsoft 365 E3 o a Office 365 E3 más EMS E3) y en el complemento de componente de IRM. Microsoft 365 E3 por sí sola no lo incluye, y **Microsoft Defender Suite** (antes E5 Security) tampoco. Algunas piezas se pagan aparte: los indicadores de pago por uso, la evidencia forense como complemento, las SCU del Triage Agent y la cobertura de agentes, que depende de Microsoft 365 E7 o Agent 365.

**Por qué importa**

Elegir mal la licencia es caro: comprar Defender Suite esperando IRM, o activar indicadores de pago por uso sin presupuesto, son errores frecuentes. Y entender la privacidad por diseño es lo que vuelve defendible el programa frente a RR. HH., Legal, la representación de los trabajadores y, llegado el caso, una autoridad de protección de datos.

**Qué vas a lograr**

- Explicar qué es el riesgo interno y el flujo de trabajo de IRM con un ejemplo de cada escenario.
- Describir los controles de privacidad por diseño: seudonimización, roles, indicadores apagados y auditoría.
- Determinar qué planes otorgan derechos de uso de IRM (E5, Purview Suite, complemento) y cuáles no (E3 sola, Defender Suite).
- Identificar qué capacidades requieren pago por uso, el complemento de evidencia forense, SCU o E7 / Agent 365.
- Explicar la cláusula de responsabilidad del cliente y a quién involucrar antes de monitorear personas.

> **Qué cambió.** Desde el 1 de octubre de 2025, Microsoft 365 E5 Compliance se llama **Microsoft Purview Suite** y Microsoft 365 E5 Security, **Microsoft Defender Suite**, sin cambio de servicio, funcionalidad ni precio. Purview Suite cuesta USD 12 por usuario al mes con pago anual y requiere Microsoft 365 E3 u Office 365 E3 más EMS E3 ([precios de Microsoft Security](https://www.microsoft.com/en-us/security/pricing-overview); [anuncios de Partner Center de octubre de 2025](https://learn.microsoft.com/en-us/partner-center/announcements/2025-october)).

> **Atención.** Microsoft Defender Suite **no** incluye IRM: cubre Defender for Endpoint P2, Defender for Office 365 P2, Defender for Identity, Defender for Cloud Apps y Entra ID P2 ([HBS](https://www.hbs.net/blog/microsoft-365-security-smbs)). Los SKU de componente, como «Microsoft 365 E5 Insider Risk Management», no cambiaron de nombre, y los Product Terms mezclaron nombres viejos y nuevos durante la transición: confirma el SKU exacto con tu revendedor ([SAMexpert](https://samexpert.com/microsoft-365-defender-purview-renames/)). Todo usuario que se beneficia del servicio necesita licencia ([descripción del servicio](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)).

> **Atención.** Microsoft indica que el cliente es el único responsable de usar IRM conforme a la ley aplicable y que debe hacer su propia investigación completa, sin basarse solo en las conclusiones de la herramienta ([Get started](https://learn.microsoft.com/en-us/purview/insider-risk-management-configure)). Esta guía no es asesoría legal: comparte la cláusula con Legal, RR. HH. y privacidad antes de cualquier piloto.

> **Novedad.** Microsoft 365 E7 y Agent 365 llegaron a disponibilidad general el 1 de mayo de 2026: E7 cuesta USD 99 por usuario al mes e incluye Microsoft 365 Copilot, Microsoft 365 E5, Entra Suite y Agent 365, que también se vende aparte por USD 15 ([anuncio](https://techcommunity.microsoft.com/blog/microsoft_365blog/microsoft-365-e7-and-agent-365-are-now-generally-available/4516295)). La descripción del servicio de Purview indica que las capacidades para agentes de Microsoft Foundry y apps de IA conectadas a Entra se soportarán con E7 y Agent 365 ([descripción del servicio](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)).

**¿Tienes poco tiempo?**

- [Learn about Insider Risk Management](https://learn.microsoft.com/en-us/purview/insider-risk-management) · Documentación
- [Microsoft Purview service description](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description) · Documentación
- [Manage username privacy in Insider Risk Management](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-privacy) · Documentación
- [Understand Microsoft Purview Insider Risk Management](https://learn.microsoft.com/en-us/training/modules/purview-explore-insider-risk-management/) · Curso

### Documentación, cursos y credenciales

- [Manage username privacy in Insider Risk Management](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-privacy) · Documentación · Oficial · Nuevo · Microsoft Learn · 26 jun 2026. Explica la seudonimización de nombres de usuario (activa por defecto) y sus efectos en grafo de riesgo, perfiles, exportaciones y el Triage Agent.
- [Learn about Insider Risk Management](https://learn.microsoft.com/en-us/purview/insider-risk-management) · Documentación · Oficial · Microsoft Learn. Página de entrada a IRM: riesgos que cubre, principios de privacidad por diseño, analíticas, acciones recomendadas y flujo de trabajo.
- [Microsoft Purview service description](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description) · Documentación · Oficial · Microsoft Learn. Descripción oficial de servicio con las licencias que habilitan IRM y su add-on de Forensic Evidence, y quién necesita licencia.
- [Partner Center announcements (índice mensual)](https://learn.microsoft.com/en-us/partner-center/announcements/) · Documentación · Oficial · Nuevo · Microsoft Learn (Partner Center) · 5 nov 2026. Índice oficial de anuncios comerciales que fecha hitos de licenciamiento como Security Copilot con Microsoft 365 E5 (dic-2025), Microsoft 365 E7 (mar-2026) y su GA junto a Agent 365 (1-may-2026).
- [Understand Microsoft Purview Insider Risk Management](https://learn.microsoft.com/en-us/training/modules/purview-explore-insider-risk-management/) · Curso · Oficial · Microsoft Learn. Módulo introductorio (28 min) que define el riesgo interno y presenta políticas, señales, analíticas, paneles y herramientas de investigación de IRM.
- [Microsoft Purview Suite](https://www.microsoft.com/en-sg/security/microsoft-purview-suite) · Documentación · Oficial. Página comercial de Microsoft Purview Suite (USD 12 usuario/mes, requiere Microsoft 365 E3 u Office 365 E3 + EMS E3), que incluye Insider Risk Management.
- [Implement Microsoft Purview Insider Risk Management (MS-102)](https://learn.microsoft.com/en-us/training/modules/implement-insider-risk-management/) · Curso · Oficial · Microsoft Learn. Módulo de la ruta MS-102 que resume funcionalidad, planificación, políticas, alertas y casos de IRM para administradores de Microsoft 365.
- [Insider Risk Management (solution overview)](https://learn.microsoft.com/en-us/purview/insider-risk-management-solution-overview) · Documentación · Oficial · Microsoft Learn · 26 sep 2025. Página índice que ordena el recorrido de configuración: aprender, planificar y licenciar, ajustar configuración, permisos y conectores, y crear políticas.

### Webinars, videos y podcasts

- [Manage Data Risks from Employee Insiders with Microsoft Purview](https://www.youtube.com/watch?v=Ynkfu8OF0wQ) · Video · Empleado de Microsoft · Legado aún útil · Talhah Mir y Jeremy Chapman · Microsoft Mechanics. Episodio de Microsoft Mechanics donde el líder de ingeniería de IRM muestra detección con ML, privacidad y flujo de trabajo. *Nota:* Video de ~2022 (portal de cumplimiento anterior); los conceptos siguen vigentes pero la interfaz cambió al portal unificado de Purview

### Comunidad: blogs, libros, newsletters y eventos

- [Microsoft 365 E5 Security and Microsoft 365 E5 Compliance renamed](https://www.schneider.im/microsoft-365-e5-security-and-microsoft-365-e5-compliance-renamed/) · Blog · Comunidad · SCHNEIDER IT MANAGEMENT · 8 oct 2025. Nota de partner que documenta que desde el 1-oct-2025 Microsoft 365 E5 Compliance se llama Microsoft Purview Suite (y E5 Security, Microsoft Defender Suite), sin cambio funcional.

**Manos a la obra**

1. `Laboratorio` Arma un mapa de licencias para tres poblaciones de tu organización (usuarios con E5, con E3 y de primera línea): qué plan les da IRM —E5, Purview Suite o el complemento de IRM— y cuál no (E3 sola, Defender Suite), usando la [descripción del servicio](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description) y la [página de precios](https://www.microsoft.com/en-us/security/pricing-overview). Evidencia: tabla con una fuente por fila.
2. `Laboratorio` En tu laboratorio, abre la configuración de privacidad de IRM, confirma que la seudonimización está activa y documenta qué oculta (nombres en alertas y casos, perfil de usuario, grafo de riesgo) y qué no (el panel del Triage Agent y la exportación por API) ([privacidad de nombres de usuario](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-privacy)). Evidencia: captura y nota de una página.
3. `Laboratorio` Redacta una carta de intención del programa para Legal, RR. HH. y privacidad: finalidades, poblaciones, señales, responsables y la cláusula de responsabilidad del cliente, apoyándote en la [guía de planificación](https://learn.microsoft.com/en-us/purview/insider-risk-management-plan) y en [Get started](https://learn.microsoft.com/en-us/purview/insider-risk-management-configure). Evidencia: borrador versionado listo para revisión (no es un documento legal).
4. `Laboratorio` Mira [Manage Data Risks from Employee Insiders with Microsoft Purview](https://www.youtube.com/watch?v=Ynkfu8OF0wQ) y anota qué cambió desde 2022 en la interfaz y en los nombres (del portal de cumplimiento al portal de Purview, de la cola clásica a la unificada). Evidencia: lista de diferencias con su fuente actual.
5. `Solo producción` Concilia licencias en producción: compara los usuarios que quedarían en el alcance de tus políticas con los que tienen derechos de IRM, porque todo usuario que se beneficia necesita licencia ([descripción del servicio](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)). Cómo hacerlo seguro: informe de solo lectura desde el centro de administración, sin cambiar asignaciones, validado con el equipo de licenciamiento.

**¿Quieres profundizar?**

- [Microsoft 365 E5 Security and Microsoft 365 E5 Compliance renamed](https://www.schneider.im/microsoft-365-e5-security-and-microsoft-365-e5-compliance-renamed/) · Blog

<a id="i2"></a>

## I2 · Configuración: indicadores, conectores y usuarios prioritarios

*L200 · ~6 h · Origen: Ninja oficial de IRM · «Getting Started» (analíticas y configuración), ampliado con indicadores de pago por uso y conectores*

Antes de la primera política conviene separar tres conceptos que se confunden a menudo: el **evento desencadenante** pone a un usuario en el alcance de una política (por ejemplo, una renuncia informada por RR. HH.), el **indicador global** define qué actividad se recolecta y el **indicador de política** define qué actividad puntúa en esa política. Todos los indicadores globales vienen desactivados, y hay que activar al menos uno para crear una política. Los de dispositivo requieren equipos incorporados (Windows 10 1809 o posterior y las tres versiones más recientes de macOS) y Edge para detectar subidas a la nube, y no incluyen archivos .exe ni .dll.

Sobre esa base se afina la detección: **variantes** de indicador (hasta 10 por indicador y 100 en total), **exfiltración acumulativa** (los últimos 30 días del usuario contra la organización y contra su grupo de pares), **boosters** de riesgo (actividad inusual, caso previo confirmado, grupo prioritario y usuario de alto impacto), grupos de usuarios prioritarios y exclusiones globales. Algunos indicadores —nube de terceros, red, Microsoft Fabric y varias experiencias de IA— solo funcionan con **pago por uso** vinculado a una suscripción de Azure; los de Microsoft 365 están incluidos.

Los **conectores** traen contexto que Microsoft 365 no tiene: el de RR. HH. (renuncias, cambios de nivel, evaluaciones, planes de mejora y perfil de empleado en vista previa), el de acceso físico, el de registros de salud y el conector Insider Risk Indicators (vista previa) para detecciones de terceros ya agregadas en un SIEM. Las **analíticas** completan el cuadro: un escaneo con resultados agregados y anonimizados que estima el riesgo antes de crear políticas.

**Por qué importa**

La calidad de las alertas depende de las señales que activas: un indicador innecesario genera ruido y exposición de datos personales; uno faltante deja ciego un escenario completo. Cada indicador es a la vez una decisión técnica, de privacidad y, en algunos casos, de costo, y el conector de RR. HH. es un acuerdo de intercambio de datos con otra área que debe quedar por escrito.

**Qué vas a lograr**

- Distinguir evento desencadenante, indicador global e indicador de política.
- Activar un conjunto justificado de indicadores, incluidos los de dispositivo y navegador.
- Configurar el conector de RR. HH. con datos sintéticos y verificar la carga.
- Definir grupos de usuarios prioritarios, grupos de detección y exclusiones globales.
- Identificar los indicadores de pago por uso y presupuestar su consumo.
- Ejecutar las analíticas e interpretar sus resultados antes de crear políticas.

> **Atención.** Todos los indicadores globales vienen desactivados y hay que activar al menos uno para crear una política. Distingue el evento desencadenante (pone al usuario en el alcance), el indicador global (qué se recolecta) y el indicador de política (qué puntúa). Los indicadores de Entra ID Protection solo evalúan riesgos en estado ConfirmedCompromised o Remediated ([indicadores de política](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-policy-indicators)).

> **Atención.** Requieren **pago por uso**: almacenamiento en la nube (Box, Dropbox, Google Drive), servicios en la nube (Amazon S3, Azure), red de terceros, Microsoft Fabric (Power BI y Lakehouse), Copilot experiences con datos que no son de Microsoft 365, Enterprise AI apps y Other AI apps; Microsoft 365 Copilot no tiene cargo de pago por uso ([indicadores](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-policy-indicators)). Se activan vinculando una suscripción de Azure del mismo tenant y el consumo se controla en el Usage center ([modelos de facturación](https://learn.microsoft.com/en-us/purview/purview-billing-models); [Usage center](https://learn.microsoft.com/en-us/purview/purview-billing-usage)).

> **Novedad.** La guía del conector de RR. HH. se actualizó el 30 de marzo de 2026: admite renuncias, cambios de nivel, evaluaciones de desempeño, planes de mejora y perfil de empleado (vista previa). Límites: 500 registros por CSV en cada carga, LastWorkingDate entre 6 meses atrás y 1 año adelante, acceso a `webhook.ingestion.office.com` y rol Data Connector Admin; los perfiles de empleado se borran si no se actualizan en 30 días ([conector de RR. HH.](https://learn.microsoft.com/en-us/purview/import-hr-data)).

> **Consejo Ninja.** Ejecuta las analíticas antes de la primera política: usan hasta 10 días de actividad, entregan resultados agregados y anonimizados en hasta 48 horas y recomiendan umbrales en tiempo real ([analíticas](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-analytics)). Los grupos de usuarios prioritarios son obligatorios para las plantillas «by priority users» y no se combinan con unidades administrativas, y las cuentas de invitado no se admiten en el alcance de las políticas ([Get started](https://learn.microsoft.com/en-us/purview/insider-risk-management-configure)).

**¿Tienes poco tiempo?**

- [Configure policy indicators in Insider Risk Management](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-policy-indicators) · Documentación
- [Set up a connector to import HR data](https://learn.microsoft.com/en-us/purview/import-hr-data) · Documentación
- [Learn about Insider Risk Management settings](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings) · Documentación
- [Enable analytics in Insider Risk Management](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-analytics) · Documentación

**Indicadores: incluidos frente a pago por uso (noviembre de 2026)**

| Familia de indicadores | Ejemplos o alcance | Requisito | Licencia | Estado |
|---|---|---|---|---|
| Office (Microsoft 365) | Descargas y uso compartido en SharePoint y OneDrive, correo y Teams | Auditoría activa | Incluido con IRM | Disponible |
| Dispositivo | Copia a USB o a la nube, impresión y copia a recursos de red; Windows 10 1809 o posterior y las tres últimas versiones de macOS | Equipo incorporado; Edge para subidas a la nube; no incluye .exe ni .dll | Incluido con IRM | Disponible |
| Navegación riesgosa | Sitios de phishing, malware o contenido para adultos | Extensión de navegador en Windows 10 x64 1809 o posterior | Incluido con IRM | Vista previa |
| Defender for Endpoint | Alertas de MDE (malware, software no deseado, evasión de controles) importadas a diario | Suscripción de MDE e integración en sus funciones avanzadas | Incluido con IRM; MDE viene en Microsoft 365 E5 y en Defender Suite | Vista previa |
| Entra ID Protection | Riesgos de usuario en estado ConfirmedCompromised o Remediated | Entra ID Protection | Incluido con IRM | Disponible |
| Communication Compliance | Estresores y conducta inapropiada; hasta 30 tipos de información sensible en mensajes | Política de CC «Insider risk indicator»; los IRM Investigators quedan como revisores | Incluido con IRM | Vista previa |
| Acceso físico | Accesos no autorizados o fuera de horario a activos físicos prioritarios | Conector de acceso físico (JSON) y, para salidas, conector de RR. HH. | Incluido con IRM | Disponible |
| Registros de salud | Acceso, cambio o exportación indebidos de historias clínicas | Conector Microsoft Healthcare o Epic y conector de RR. HH. | Incluido con IRM | Vista previa (plantilla Patient data misuse) |
| Indicadores personalizados | Detecciones de terceros agregadas, por ejemplo de Salesforce o Dropbox vía Sentinel o Splunk | Conector Insider Risk Indicators; esperar 24 h tras cada cambio | Incluido con IRM | Vista previa |
| Nube de terceros | Box, Dropbox, Google Drive, Amazon S3 y Azure (SQL, Storage) | Apps conectadas en Microsoft Defender; suscripción de Azure del mismo tenant | Pago por uso | Vista previa |
| Red de terceros | Actividad de red hacia destinos externos | Collection policy de red; suscripción de Azure | Pago por uso | No confirmado en las fuentes revisadas |
| Microsoft Fabric | Power BI y Lakehouse | Suscripción de Azure | Pago por uso | Lakehouse en disponibilidad general desde marzo de 2026 |
| IA: Microsoft 365 Copilot | Prompts y respuestas con información sensible | Licencia de Microsoft 365 Copilot | Sin cargo de pago por uso | Vista previa (indicadores de IA) |
| IA: otras experiencias | Copilot experiences con datos que no son de Microsoft 365, Enterprise AI apps y Other AI apps | Extensión de navegador para Other AI apps; selección de apps desde junio de 2026 | Pago por uso | Vista previa (indicadores de IA) |
| Risky Agents | Agentes de Copilot Studio, Microsoft Foundry y del SDK P4AI | Política activa por defecto con licencias compatibles | Microsoft 365 E7 o Agent 365, según MC1280556 | Vista previa en Learn; disponibilidad general anunciada para junio–julio de 2026 |

Fuentes: [indicadores de política](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-policy-indicators) · [Get started](https://learn.microsoft.com/en-us/purview/insider-risk-management-configure) · [MC1280556](https://message.cengizyilmaz.net/message/mc1280556-microsoft-purview-for-agents-ai-observability-and-insider-risk-management-now-generally-available) · [What's new](https://learn.microsoft.com/en-us/purview/whats-new). Confirma el estado de cada indicador en tu tenant.

### Documentación, cursos y credenciales

- [Configure policy indicators in Insider Risk Management](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-policy-indicators) · Documentación · Oficial · Microsoft Learn. Referencia de eventos desencadenantes, indicadores globales y de política, indicadores personalizados y onboarding de dispositivos Windows/macOS.
- [Learn about Insider Risk Management settings](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings) · Documentación · Oficial · Microsoft Learn. Tabla de todos los ajustes globales de IRM: notificaciones, analíticas, uso compartido de datos, grupos de detección, exclusiones globales, detecciones inteligentes, Teams, indicadores, ventanas de política y Power Automate.
- [Set up a connector to import HR data](https://learn.microsoft.com/en-us/purview/import-hr-data) · Documentación · Oficial · Microsoft Learn. Guía del conector de RR. HH. (CSV + app de Entra + script programado) para importar renuncias, cambios de nivel, evaluaciones de desempeño, planes de mejora y perfil de empleado.
- [Get started with Insider Risk Management](https://learn.microsoft.com/en-us/purview/insider-risk-management-configure) · Documentación · Oficial · Microsoft Learn · 14 nov 2025. Guía paso a paso: permisos, auditoría, analíticas, prerrequisitos de políticas, configuración global y primera política.
- [Prepare for Microsoft Purview Insider Risk Management](https://learn.microsoft.com/en-us/training/modules/purview-prepare-insider-risk-management/) · Curso · Oficial · Microsoft Learn. Módulo (36 min) sobre planificación con partes interesadas, prerrequisitos, configuración de privacidad y conexión de fuentes de datos para IRM.
- [Set up a connector to import physical badging data](https://learn.microsoft.com/en-us/purview/import-physical-badging-data) · Documentación · Oficial · Microsoft Learn. Conector que importa eventos de acceso físico (JSON vía API) para correlacionar accesos a activos físicos prioritarios con actividad de riesgo.

### Webinars, videos y podcasts

- [From Zero to first Signal Insider Risk](https://www.youtube.com/watch?v=-SWX3R2ECPA) · Webinar · Comunidad · Sathish Veerapandian · Microsoft Security Community (YouTube). Demo comunitaria sobre las bases necesarias (Entra ID, Intune, Defender for Endpoint y DLP) para que IRM genere sus primeras señales y alertas.

**Manos a la obra**

1. `Laboratorio` Activa las analíticas, espera hasta 48 horas y revisa Informes > Analíticas; guarda los principales hallazgos y crea una política de prueba desde una recomendación ([analíticas](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-analytics); [informes](https://learn.microsoft.com/en-us/purview/insider-risk-management-reports)). Evidencia: captura de los hallazgos agregados y nombre de la política creada.
2. `Laboratorio` Conector de RR. HH. con datos sintéticos: registra la app en Entra, crea el conector y prepara un CSV con UserPrincipalName, ResignationDate y LastWorkingDate (formato ISO 8601) para tres usuarios de prueba, con menos de 500 filas y fechas dentro de la ventana permitida; cárgalo con el script y verifica RecordsSaved ([conector de RR. HH.](https://learn.microsoft.com/en-us/purview/import-hr-data)). Evidencia: salida del script y captura del conector. Borra el CSV al terminar.
3. `Laboratorio` Indicadores de dispositivo: incorpora una VM Windows 11 en Azure, activa los indicadores de dispositivo y genera actividad con una cuenta de prueba —subida a la nube con Edge, impresión y copia a un recurso de red— ([indicadores](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-policy-indicators)). Evidencia: eventos en el explorador de actividad. Ten en cuenta que las VM en la nube no tienen USB: para probar la copia a medios extraíbles necesitas un equipo físico incorporado.
4. `Laboratorio` Crea un grupo de usuarios prioritarios (`PRUEBA-IRM-Finanzas`), un grupo de detección y una exclusión global justificada, por ejemplo el dominio de un proveedor aprobado ([Get started](https://learn.microsoft.com/en-us/purview/insider-risk-management-configure); [detecciones inteligentes](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-intelligent-detections)). Evidencia: registro con el motivo de cada exclusión y quién la aprobó.
5. `Laboratorio parcial` Conector de acceso físico con un JSON sintético de tres eventos fuera de horario y un activo físico prioritario ([conector de acceso físico](https://learn.microsoft.com/en-us/purview/import-physical-badging-data)). Evidencia: eventos importados. Limitación: para correlacionarlo con usuarios que se van también necesitas el conector de RR. HH.; sin él, solo se procesa el acceso físico no autorizado.
6. `Laboratorio parcial` Indicador de pago por uso: vincula una suscripción de Azure del mismo tenant ([habilitar el pago por uso](https://learn.microsoft.com/en-us/purview/purview-payg-subscription-based-enablement)), activa un solo indicador de nube con alcance piloto y fija presupuesto y alertas al 50, 75 y 90 %; revisa el [Usage center](https://learn.microsoft.com/en-us/purview/purview-billing-usage) a las 48 horas. Limitación: requiere conectar la app en Microsoft Defender, y no está confirmado que el crédito de Visual Studio cubra los medidores de Purview.
7. `Solo producción` Conector de registros de salud (EMR) y Patient data misuse: requieren un sistema clínico real (conector Microsoft Healthcare o Epic) y el perfil de empleado del conector de RR. HH. ([Get started](https://learn.microsoft.com/en-us/purview/insider-risk-management-configure)). Cómo hacerlo seguro: piloto con un grupo pequeño aprobado por privacidad y Legal, analistas con acceso de solo lectura, columnas mínimas y revisión mensual de accesos.

**¿Quieres profundizar?**

- [From Zero to first Signal Insider Risk](https://www.youtube.com/watch?v=-SWX3R2ECPA) · Webinar

<a id="i3"></a>

## I3 · Triage de alertas en la cola unificada y gestión de casos

*L200 · ~4 h · Origen: Ninja oficial de IRM · alertas y casos, actualizado a la experiencia unificada de octubre de 2026*

Las primeras alertas llegan unas 24 horas después de crear una política. El triage consiste en revisar la cola, priorizar por severidad, entender la actividad con el resumen, el explorador de actividad y el grafo de riesgo de datos (que no se usa con la seudonimización activa), y decidir: confirmar la alerta y abrir un caso, o descartarla con un motivo. La severidad de una alerta puede cambiar si nadie la clasifica, por lo que el tiempo en «Needs review» es la métrica que más importa.

En 2026 cambió el lugar de trabajo. La **experiencia unificada de alertas** reúne la cola clásica y la del Triage Agent con una columna de categorización del agente, la vista «Needs attention», vistas previas del contenido y acciones sin salir de la cola. Entró en vista previa a fines de junio y llegó a disponibilidad general entre inicios y mediados de octubre de 2026; la pestaña «Alerts (classic)» se deprecó el 1 de octubre de 2026 en la nube comercial (el 31 de octubre en las nubes de gobierno) y se retiró Alert Spotlight. También llegaron, en vista previa, el perfil de usuario ampliado con datos de Entra y las notas en alertas y casos, incluidas notas automáticas del sistema.

Un **caso** se centra en un usuario y concentra la investigación: actividad, contenido, notas, avisos al usuario y acciones como resolverlo como benigno, compartirlo con ServiceNow o por correo, o escalarlo a eDiscovery (Premium). Con unidades administrativas, solo se asignan casos de usuarios dentro del alcance.

**Por qué importa**

El triage es donde se deciden el costo y la proporcionalidad del programa: cada alerta mal confirmada expone a una persona a una investigación innecesaria y cada alerta ignorada puede ser una fuga real. Un procedimiento de triage consistente reduce el tiempo en revisión, documenta los motivos de descarte y prepara casos que RR. HH. y Legal pueden usar.

**Qué vas a lograr**

- Navegar la cola unificada y filtrar por severidad, política y categoría del agente.
- Aplicar un procedimiento de triage con criterios para confirmar o descartar y motivos documentados.
- Crear, asignar y documentar un caso con notas.
- Explicar el retiro de «Alerts (classic)» y de Alert Spotlight y su impacto en los procedimientos.
- Reconocer qué muestra el perfil de usuario con y sin seudonimización.

> **Qué cambió.** Según [MC1430536](https://mc.merill.net/message/MC1430536), la cola unificada reúne las alertas clásicas y las del Triage Agent; la pestaña «Alerts (classic)» se deprecó el 1 de octubre de 2026 en la nube comercial y el 31 de octubre en las nubes de gobierno, y se retiró Alert Spotlight. La disponibilidad general se desplegó entre inicios y mediados de octubre de 2026 ([RM564621](https://mc.merill.net/message/RM564621); [anuncio del equipo de producto](https://techcommunity.microsoft.com/blog/microsoft-security-blog/introducing-a-unified-alert-experience-for-microsoft-purview-insider-risk-manage/4530714)).

> **Atención.** El propio MC1430536 dice que ambas experiencias convivirían «al menos 60 días» con soporte «hasta el 31 de agosto de 2026», una fecha anterior a la disponibilidad general y a la depreciación; además, [What's new](https://learn.microsoft.com/en-us/purview/whats-new) solo registra la vista previa de julio. Verifica en tu tenant qué ves hoy y actualiza los procedimientos que mencionen la pestaña clásica.

> **Novedad.** Desde julio de 2026 (vista previa): perfil de usuario ampliado con datos de Entra (ubicación, tipo de empleado, departamento, último día laboral), oculto si la seudonimización está activa, y notas en alertas y casos, incluidas notas automáticas del sistema; la disponibilidad general de las notas se anunció entre fines de septiembre y mediados de octubre de 2026 ([MC1430534](https://mc.merill.net/message/MC1430534); [Petri](https://petri.com/microsoft-purview-insider-risk-management-unified-alert/)). Antes llegaron, en vista previa, la creación de casos sin descargar contenido (marzo) y la vista previa del contenido durante el triage (abril) ([What's new](https://learn.microsoft.com/en-us/purview/whats-new)).

> **Consejo Ninja.** Cada caso se centra en un usuario; sus acciones incluyen enviar un aviso, resolverlo como benigno, compartirlo con ServiceNow o por correo y escalarlo a eDiscovery (Premium), y los informes de casos cubren los últimos 30 días ([gestionar casos](https://learn.microsoft.com/en-us/purview/insider-risk-management-cases)). La severidad cambia si una alerta no se clasifica: mide el tiempo en «Needs review» desde el primer día ([investigar actividades](https://learn.microsoft.com/en-us/purview/insider-risk-management-activities)).

**¿Tienes poco tiempo?**

- [Investigate Microsoft Purview Insider Risk Management activities](https://learn.microsoft.com/en-us/purview/insider-risk-management-activities) · Documentación
- [Take action on Insider Risk Management cases](https://learn.microsoft.com/en-us/purview/insider-risk-management-cases) · Documentación
- [Introducing a unified alert experience for Microsoft Purview Insider Risk Management](https://techcommunity.microsoft.com/blog/microsoft-security-blog/introducing-a-unified-alert-experience-for-microsoft-purview-insider-risk-manage/4530714) · Blog oficial
- [Use workflows, alerts, and cases | SC-401 | Episode 9](https://www.youtube.com/watch?v=4lrr7KPza5w) · Video

### Documentación, cursos y credenciales

- [MC1430536 - Microsoft Purview: Insider Risk Management - Unified alert queue](https://mc.merill.net/message/MC1430536) · Documentación · Oficial · Nuevo · Microsoft 365 Message Center (archivo mc.merill.net) · 17 jul 2026. Aviso oficial que unifica la cola clásica de alertas y la del Triage Agent en una sola vista, retira Alert Spotlight y depreca la pestaña Alerts (classic).
- [Investigate Microsoft Purview Insider Risk Management activities](https://learn.microsoft.com/en-us/purview/insider-risk-management-activities) · Documentación · Oficial · Microsoft Learn. Procedimiento oficial de triage: revisar paneles, priorizar por severidad, usar resumen de Copilot, Activity explorer y Data risk graph, y confirmar o descartar alertas.
- [Take action on Insider Risk Management cases](https://learn.microsoft.com/en-us/purview/insider-risk-management-cases) · Documentación · Oficial · Microsoft Learn. Guía de gestión de casos: panel de casos, asignación, investigación y acciones (aviso al usuario, resolver como benigno, compartir con ServiceNow o correo y escalar a eDiscovery Premium).

### Anuncios y blogs oficiales

- [Introducing a unified alert experience for Microsoft Purview Insider Risk Management](https://techcommunity.microsoft.com/blog/microsoft-security-blog/introducing-a-unified-alert-experience-for-microsoft-purview-insider-risk-manage/4530714) · Blog oficial · Empleado de Microsoft · Nuevo · Michelle Slotwinski (MSlotwinski) · Microsoft Tech Community (Microsoft Security Community Blog) · 30 jun 2026. Anuncio del equipo de producto sobre la nueva experiencia unificada de alertas de IRM que reúne contexto, agente de triage y detalles de usuario en un solo flujo.

### Webinars, videos y podcasts

- [Use workflows, alerts, and cases | SC-401 | Episode 9](https://www.youtube.com/watch?v=4lrr7KPza5w) · Video · Oficial · Microsoft Learn (YouTube). Episodio oficial que recorre el flujo de IRM (detectar, analizar, investigar, notificar y remediar), paneles de usuarios y alertas, casos e integración con Defender XDR.

**Manos a la obra**

1. `Laboratorio` Con una política de prueba activa desde hace al menos 24 horas, filtra la cola unificada por severidad y por categoría del agente y clasifica tres alertas: confirma una, descarta otra con motivo y deja la tercera en revisión ([investigar actividades](https://learn.microsoft.com/en-us/purview/insider-risk-management-activities)). Evidencia: registro de triage con fecha, decisión y motivo.
2. `Laboratorio` Crea un caso desde la alerta confirmada, asígnalo a la cuenta de IRM Investigators, agrega una nota del investigador y verifica las notas automáticas del sistema ([casos](https://learn.microsoft.com/en-us/purview/insider-risk-management-cases); [MC1430534](https://mc.merill.net/message/MC1430534)). Evidencia: captura del caso con sus notas.
3. `Laboratorio` Redacta la versión 0 de tu procedimiento de triage (una página): criterios para confirmar o descartar, motivos de descarte estandarizados, tiempo máximo en «Needs review», quién puede ver identidades y qué evidencia se guarda ([investigar actividades](https://learn.microsoft.com/en-us/purview/insider-risk-management-activities)). Evidencia: documento versionado.
4. `Laboratorio` Con la seudonimización activa, entra con la cuenta de IRM Analysts y luego con la de IRM Investigators y compara qué ve cada una en la alerta, el perfil de usuario y el explorador de contenido ([permisos](https://learn.microsoft.com/en-us/purview/insider-risk-management-permissions); [privacidad](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-privacy)). Evidencia: tabla de diferencias por rol.
5. `Solo producción` Migración desde «Alerts (classic)»: inventaría filtros guardados, manuales y procedimientos que mencionen la pestaña clásica o Alert Spotlight y actualízalos a la cola unificada ([MC1430536](https://mc.merill.net/message/MC1430536)). Cómo hacerlo seguro: revisión documental con el equipo de triage, sin cambiar políticas ni alertas, y una semana de operación del procedimiento nuevo con revisión diaria del líder.

<a id="reto-inicial"></a>

## Reto del nivel

**Tu primera señal con privacidad por diseño.** En tu laboratorio: verifica la auditoría, asigna los grupos IRM Admins, Analysts, Investigators y Approvers con vencimiento a cuatro cuentas distintas, confirma la seudonimización, ejecuta las analíticas y configura el conector de RR. HH. con un CSV sintético para tres usuarios de prueba. Crea una política Data theft by departing users acotada a ellos, genera actividad, clasifica las alertas en la cola unificada con motivos documentados y abre un caso. Entrega un informe de dos páginas con capturas, el registro de triage y un mapa de licencias que explique qué plan cubre IRM en tu organización y por qué Microsoft Defender Suite no lo hace.

<a id="quiz-inicial"></a>

## Evaluación del nivel

Responde y compara con [Evaluaciones y respuestas](06_Evaluaciones_y_respuestas.md#eval-inicial). Con 80 % o más, ¡nivel aprobado! (En la versión web puedes corregir en línea y generar tu certificado).

1. ¿Cuál de estas combinaciones **no** otorga derechos de uso de Insider Risk Management?
   - a) Microsoft 365 E5
   - b) Microsoft 365 E3 con Microsoft Purview Suite (antes E5 Compliance)
   - c) Microsoft 365 E3 con el complemento Microsoft 365 E5 Insider Risk Management
   - d) Microsoft 365 E3 con Microsoft Defender Suite (antes E5 Security)

2. ¿Qué cambió el 1 de octubre de 2025 con Microsoft 365 E5 Compliance?
   - a) Pasó a llamarse Microsoft Purview Suite, sin cambios de servicio, funcionalidad ni precio
   - b) Se fusionó con Microsoft Defender Suite en un único SKU de seguridad y cumplimiento
   - c) Pasó a incluir Microsoft 365 Copilot y subió de precio para los clientes nuevos
   - d) Dejó de requerir Microsoft 365 E3 como base y se vende como plan independiente

3. Vas a practicar con una prueba de Microsoft 365 E5 en un tenant nuevo no administrado. ¿Qué debes verificar antes de crear políticas de IRM?
   - a) Que haya SCU de Security Copilot aprovisionadas, porque IRM las usa para puntuar el riesgo
   - b) Que el registro de auditoría unificado esté activo, porque en esos tenants puede venir apagado
   - c) Que la solución de IRM de Sentinel esté instalada, porque IRM guarda allí sus alertas
   - d) Que la seudonimización esté desactivada, porque impide que las políticas generen alertas

4. Desde julio de 2026, ¿qué admiten las asignaciones a grupos de roles de Purview?
   - a) Aprobación obligatoria de dos administradores para cualquier grupo de roles de Purview
   - b) Asignación exclusiva mediante unidades administrativas, sin asignaciones a todo el tenant
   - c) Fecha de vencimiento de 1 día a 2 años, salvo eDiscovery Administrator y eDiscovery Manager
   - d) Herencia automática desde los roles de Entra ID, sin necesidad de una asignación explícita

5. ¿Qué examen cubre hoy Insider Risk Management dentro de su dominio «Manage risks, alerts, and activities»?
   - a) SC-400
   - b) SC-200
   - c) MS-102
   - d) SC-401

6. Según Microsoft, ¿quién es responsable de que el uso de IRM cumpla la ley aplicable?
   - a) Microsoft, porque la herramienta seudonimiza a los usuarios por defecto
   - b) El cliente, que además debe hacer su propia investigación sin basarse solo en IRM
   - c) El revendedor que vendió la licencia y configuró el tenant inicial
   - d) La autoridad de protección de datos del país donde está hospedado el tenant

7. ¿En qué estado vienen los indicadores globales de IRM al empezar?
   - a) Todos desactivados; hay que activar al menos uno para crear una política
   - b) Todos activados, incluidos los de pago por uso, hasta que alguien los apague
   - c) Solo los de dispositivo activados; los de Office se activan al crear una política
   - d) Activados según la plantilla elegida, sin posibilidad de cambiarlos globalmente

8. ¿Cuál de estos indicadores requiere activar el pago por uso?
   - a) Indicadores de Office, como descargas y uso compartido en SharePoint
   - b) Interacciones de los usuarios con Microsoft 365 Copilot en sus aplicaciones
   - c) Almacenamiento en la nube de terceros, como Box, Dropbox o Google Drive
   - d) Booster de riesgo por pertenencia a un grupo de usuarios prioritarios

9. ¿Cuál es un límite real del conector de RR. HH.?
   - a) Solo acepta renuncias; los cambios de nivel y las evaluaciones requieren otro conector
   - b) Requiere el rol Global Administrator en cada carga, además de la app registrada en Entra
   - c) Admite hasta 5.000 registros por archivo, cargados solo de forma manual desde el portal
   - d) Hasta 500 registros por CSV en cada carga; los perfiles sin actualizar se borran a los 30 días

10. ¿Qué acepta el conector Insider Risk Indicators (vista previa)?
   - a) Señales crudas de cualquier SIEM, que IRM agrega y normaliza por su cuenta
   - b) Detecciones de terceros ya agregadas y procesadas, por ejemplo desde Sentinel o Splunk
   - c) Solo datos de RR. HH. en CSV, como alternativa al conector de RR. HH.
   - d) Registros de historias clínicas exportados desde un sistema de salud

11. Según MC1430536, ¿qué se retira con la experiencia unificada de alertas?
   - a) La seudonimización de los nombres en la cola de alertas
   - b) Los casos, que pasan a gestionarse dentro de la cola
   - c) La pestaña «Alerts (classic)» y Alert Spotlight
   - d) El Triage Agent, que se reemplaza por reglas de prioridad

12. ¿Cuánto tardan, aproximadamente, las primeras alertas después de crear una política?
   - a) Unas 24 horas
   - b) Aparecen de inmediato
   - c) 7 días
   - d) 30 días

13. ¿Qué ocurre con el perfil de usuario ampliado (datos de Entra) cuando la seudonimización está activa?
   - a) Muestra todos los datos de Entra
   - b) Se envía automáticamente a RR. HH.
   - c) Muestra solo el departamento
   - d) Queda oculto

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. No constituye asesoría legal ni laboral: usar Insider Risk Management sobre personas reales exige la evaluación previa de tus áreas de Legal, RR. HH. y privacidad y, cuando corresponda, de la representación de los trabajadores. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

# Nivel 1 · Inicial · Fundamentos

*Microsoft Purview Compliance Manager Ninja Training · Edición 2026*

[← Programa](00_Programa.md) · [Índice del programa](README.md) · [Nivel 2 · Intermedio →](02_Nivel_2_Intermedio.md)

<a id="inicial"></a>

Purview y su portal, Compliance Manager hoy, cómo se calcula la puntuación, qué incluye cada licencia, plantillas regulatorias y acciones de mejora con evidencias. Terminas con la Data Protection Baseline trabajada, roles de mínimo privilegio y una decisión documentada sobre tus tres cupos premium.

*L100–L200 · 5 módulos · ~17 horas · 24 recursos*

**Módulos de este nivel:** [P0 Purview y el portal](#p0) · [I0 Cómo aprender](#i0) · [I1 Puntuación y licencias](#i1) · [I2 Plantillas regulatorias](#i2) · [I3 Acciones y evidencias](#i3)

<a id="p0"></a>

## P0 · Prerrequisitos: Microsoft Purview, el portal unificado y el Service Trust Portal

*L100 · ~3 h · Origen: Ninja oficial de 2023, nivel Basic (lugar de Compliance Manager en el ecosistema de Microsoft 365)*

Compliance Manager es una de las soluciones de **Microsoft Purview** y vive en el portal unificado de Purview, que llegó a disponibilidad general en julio de 2024 y reemplazó al portal de cumplimiento clásico, retirado entre noviembre y diciembre de ese año. Antes de evaluar regulaciones conviene dominar tres cosas: cómo se navega el portal y qué ves según tus permisos y licencias, cómo se combinan los roles de Microsoft Entra ID con los grupos de roles de Purview, y qué significa el **modelo de responsabilidad compartida**: hay controles que gestiona Microsoft, controles que gestionas tú y controles compartidos.

El segundo prerrequisito es saber de dónde sale la evidencia. Para los controles de Microsoft, el **Service Trust Portal** publica informes de auditoría (ISO, SOC, PCI y otros) que descargas tras iniciar sesión y aceptar los términos de confidencialidad. Para los tuyos, la evidencia nace en otras soluciones —etiquetas, DLP, retención, auditoría— que se profundizan en los programas hermanos de Purview. No necesitas ser experto en cada una: con un nivel equivalente a SC-900 y el módulo de Learn sobre cumplimiento en Microsoft 365 tendrás la base.

**Por qué importa**

Sin esta base, los equipos asignan Global Administrator a los auditores, confunden los puntos de Microsoft con avance propio y piden a TI evidencias que Microsoft ya publica. Entender el portal, los permisos y el Service Trust Portal acorta la preparación de cada auditoría y evita el error más caro de un programa de cumplimiento: creer que un control está cubierto porque aparece en verde.

**Qué vas a lograr**

- Ubicar Compliance Manager en el portal de Microsoft Purview y recorrer sus páginas principales.
- Explicar la responsabilidad compartida: controles de Microsoft, del cliente y compartidos.
- Distinguir roles de Entra ID, grupos de roles de Purview y roles propios de Compliance Manager.
- Descargar un informe de auditoría del Service Trust Portal y relacionarlo con un control de Microsoft.
- Preparar el inquilino de práctica con una convención de nombres y evidencias sintéticas.

> **Qué cambió.** El portal de Microsoft Purview llegó a disponibilidad general en julio de 2024 ([MC807798](https://mc.merill.net/message/MC807798)) y el portal de cumplimiento clásico se retiró entre el 14 de noviembre y el 14 de diciembre de 2024 ([MC939918](https://mc.merill.net/message/MC939918)). El Ninja oficial de 2023 y los videos de esa época muestran la interfaz anterior; incluso la página de la prueba premium describía en 2024 el portal clásico ([versión de 2024](https://learn.microsoft.com/sk-sk/purview/purview-compliance-manager-assessments-trial)).

> **Atención.** En el portal unificado, lo que ves depende de tus permisos y licencias; con PIM para grupos asignados a grupos de roles de Purview, los permisos pueden tardar hasta dos horas en aplicarse ([portal de Purview](https://learn.microsoft.com/en-us/purview/purview-portal)). El modelo completo de roles y grupos de roles está en [permisos de Purview](https://learn.microsoft.com/en-us/purview/purview-permissions); los roles propios de Compliance Manager se ven en [I1](#i1) y [O1](04_Nivel_4_Operacion.md#o1).

> **Qué cambió.** Desde el 1 de octubre de 2025, Microsoft 365 E5 Compliance se llama **Microsoft Purview Suite** y Microsoft 365 E5 Security, **Microsoft Defender Suite**, sin cambios de funciones ni de precio ([anuncio a partners](https://learn.microsoft.com/en-us/partner-center/announcements/2025-october), [precios](https://www.microsoft.com/en-us/security/pricing-overview)).

> **Consejo Ninja.** El Service Trust Portal pide iniciar sesión con una cuenta de Entra ID y aceptar los términos de confidencialidad para descargar informes de auditoría (ISO, SOC, PCI y otros) y recursos por industria, incluidos servicios financieros: son la evidencia de los controles que gestiona Microsoft ([Service Trust Portal](https://learn.microsoft.com/en-ie/purview/get-started-with-service-trust-portal?view=o365-worldwide)).

**¿Tienes poco tiempo?**

- [Explore compliance in Microsoft 365 (MS-102 module)](https://learn.microsoft.com/en-us/training/modules/explore-plan-compliance-microsoft-365/) · Curso
- [Microsoft Purview Compliance Manager (overview)](https://learn.microsoft.com/en-us/purview/compliance-manager) · Documentación
- [Get started with the Microsoft Service Trust Portal](https://learn.microsoft.com/en-ie/purview/get-started-with-service-trust-portal?view=o365-worldwide) · Documentación

### Documentación, cursos y credenciales

- [Explore compliance in Microsoft 365 (MS-102 module)](https://learn.microsoft.com/en-us/training/modules/explore-plan-compliance-microsoft-365/) · Curso · Oficial · Microsoft Learn. Módulo de 49 minutos que recorre el portal de Purview, Compliance Manager, su panel y el cálculo de la puntuación de cumplimiento.
- [Get started with the Microsoft Service Trust Portal](https://learn.microsoft.com/en-ie/purview/get-started-with-service-trust-portal?view=o365-worldwide) · Documentación · Oficial · Microsoft Learn · 24 feb 2025. Cómo acceder al Service Trust Portal para descargar informes de auditoría (ISO, SOC, PCI, etc.), whitepapers y recursos por industria, incluido servicios financieros.
- [MS-102 Implement compliance in Microsoft 365 (learning path)](https://learn.microsoft.com/en-us/training/paths/implement-compliance-microsoft-365/) · Curso · Oficial · Microsoft Learn. Ruta de aprendizaje de unas 4 horas que arranca con Compliance Manager y continúa con Insider Risk, Information Barriers y DLP.

**Manos a la obra**

1. `Laboratorio` Prepara tu inquilino de práctica con una prueba de Microsoft 365 E5 siguiendo el anexo común de entorno de práctica, entra al portal de Purview y abre Compliance Manager. Evidencia: captura del panel con la puntuación inicial y la fecha.
2. `Laboratorio` Completa el módulo de Learn [Explore compliance in Microsoft 365](https://learn.microsoft.com/en-us/training/modules/explore-plan-compliance-microsoft-365/) (49 minutos) y arma una tabla con cinco familias de acciones del panel y la solución de Purview que las implementa (etiquetas, DLP, retención, auditoría, riesgo interno).
3. `Laboratorio` Crea los grupos de seguridad `PRUEBA-CM-Lectores`, `PRUEBA-CM-Evaluadores` y `PRUEBA-CM-Administradores` y documenta qué rol de Entra ID, grupo de roles de Purview y rol de Compliance Manager recibirá cada uno, según [permisos de Purview](https://learn.microsoft.com/en-us/purview/purview-permissions) y la [configuración de Compliance Manager](https://learn.microsoft.com/en-us/purview/compliance-manager-setup).
4. `Laboratorio` En el [Service Trust Portal](https://learn.microsoft.com/en-ie/purview/get-started-with-service-trust-portal?view=o365-worldwide), descarga un informe de auditoría de Microsoft 365 (por ejemplo, ISO/IEC 27001) y vincúlalo con un control gestionado por Microsoft de la Data Protection Baseline: anota el identificador del control y la sección del informe que lo respalda.
5. `Laboratorio` Define la convención de nombres `PRUEBA-CM-<objetivo>-v<n>-<AAAAMM>` para evaluaciones, grupos y plantillas, crea una carpeta de evidencias sintéticas (sin datos personales) y regístralo en tu bitácora de laboratorio.

<a id="i0"></a>

## I0 · Cómo aprender Compliance Manager y dónde pedir ayuda

*L100 · ~2 h · Origen: Ninja oficial de 2023, Welcome/Introduction y sección New Features*

Compliance Manager no tiene una certificación propia. La única credencial vigente que lo evalúa de forma explícita es **SC-900**, cuyo dominio de soluciones de cumplimiento pesa entre 20 y 25 % e incluye describir Compliance Manager, los usos de la puntuación, el Service Trust Portal y conceptos de gobierno, riesgo y cumplimiento (habilidades al 21 de octubre de 2026). **SC-401** (habilidades al 28 de octubre de 2026) se centra en protección de información, DLP, retención, riesgo interno, auditoría y DSPM para IA, sin objetivos explícitos de Compliance Manager; su antecesor, SC-400, se retiró el 31 de mayo de 2025.

Por eso, mantenerse al día pesa más que aprobar un examen. Las fuentes que conviene seguir son la página **What's new in Microsoft Purview**, los avisos del Message Center (por ejemplo, MC1192260 sobre plantillas generadas con IA), el resumen mensual **What's new in Microsoft Security** y los resúmenes de la comunidad. Para dudas puntuales, Microsoft Q&A y Tech Community responden rápido, pero cada respuesta debe contrastarse con Learn. Este módulo también presenta el Ninja oficial de 2023: sigue siendo útil para los conceptos, aunque su interfaz y sus licencias cambiaron.

**Por qué importa**

Compliance Manager cambia cada mes: en 2026 llegaron las plantillas generadas desde el PDF de una norma, el soporte para Claude Enterprise y nuevas evaluaciones de IA. Un equipo sin rutina de actualización opera con supuestos de licencia viejos y plantillas desactualizadas, y no puede responder al auditor qué cambió desde la última revisión.

**Qué vas a lograr**

- Identificar qué credenciales evalúan Compliance Manager y qué cubre cada una.
- Armar una rutina mensual de actualización basada en fuentes oficiales.
- Contrastar una respuesta de la comunidad con la documentación de Learn antes de aplicarla.
- Situar esta guía frente al Ninja oficial de 2023 y sus límites.

> **Novedad.** La guía de SC-900 tiene habilidades al 21 de octubre de 2026: el dominio de soluciones de cumplimiento pesa entre 20 y 25 % e incluye describir Compliance Manager, los usos de la puntuación, el Service Trust Portal y conceptos de GRC ([guía SC-900](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-900)).

> **Qué cambió.** SC-400 se retiró el 31 de mayo de 2025 y Microsoft indicó que no crearía una certificación nueva para roles de cumplimiento. SC-401 (habilidades al 28 de octubre de 2026) cubre protección de información, DLP, retención, riesgo interno, auditoría y DSPM para IA, sin objetivos explícitos de Compliance Manager ([guía SC-401](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-401)).

> **Consejo Ninja.** Tu radar mensual: [What's new in Microsoft Purview](https://learn.microsoft.com/en-us/purview/whats-new) (actualizada el 16 de octubre de 2026), el resumen oficial [What's new in Microsoft Security](https://www.microsoft.com/en-us/security/blog/2026/09/24/whats-new-in-microsoft-security-september-2026/) y el [roadmap de Microsoft 365](https://www.microsoft.com/en-us/microsoft-365/roadmap). Contrasta toda respuesta de foros con Learn: un [hilo de Microsoft Q&A](https://learn.microsoft.com/en-gb/answers/questions/2081811/what-api-or-powershell-cmdlet-can-be-used-to-colle) sobre la puntuación remite a Graph de forma genérica, mientras la documentación de Purview aclara que no hay APIs de extracción ([APIs de Purview](https://learn.microsoft.com/en-us/purview/developer/use-the-api)).

> **Atención.** Microsoft Ignite se realiza del 17 al 20 de noviembre de 2026 y puede cambiar estados de vista previa (evaluaciones personalizadas, preparación previa al despliegue, informes de postura). Revisa las novedades antes de cambiar un procedimiento del equipo.

**¿Tienes poco tiempo?**

- [Study guide for Exam SC-900: Microsoft Security, Compliance, and Identity Fundamentals](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-900) · Credencial
- [What's new in Microsoft Purview](https://learn.microsoft.com/en-us/purview/whats-new) · Documentación
- [Microsoft Purview Compliance Manager (MSPCM) Ninja Training: Q1 2023](https://techcommunity.microsoft.com/blog/microsoft-security-blog/microsoft-purview-compliance-manager-mspcm-ninja-training-q1-2023/3181322) · Curso

### Documentación, cursos y credenciales

- [Study guide for Exam SC-900: Microsoft Security, Compliance, and Identity Fundamentals](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-900) · Credencial · Oficial · Nuevo · Microsoft Learn · 21 oct 2026. Guía oficial del SC-900 (habilidades al 21-oct-2026) que incluye describir Compliance Manager, los usos de la puntuación de cumplimiento, el Service Trust Portal y conceptos GRC.
- [What's new in Microsoft Purview](https://learn.microsoft.com/en-us/purview/whats-new) · Documentación · Oficial · Nuevo · Microsoft Learn · 16 oct 2026. Registro mensual de novedades de Purview, útil para seguir cambios de Compliance Manager y del resto de soluciones.
- [Study guide for Exam SC-401: Administering Information Security in Microsoft 365](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-401) · Credencial · Oficial · Nuevo · Microsoft Learn · 28 oct 2026. Guía del SC-401 (habilidades al 28-oct-2026) centrada en protección de información, DLP, retención, riesgos internos, auditoría y DSPM para IA, sin objetivos explícitos de Compliance Manager.

### Anuncios y blogs oficiales

- [What's new in Microsoft Security: September 2026](https://www.microsoft.com/en-us/security/blog/2026/09/24/whats-new-in-microsoft-security-september-2026/) · Blog oficial · Empleado de Microsoft · Nuevo · Alym Rayani · Microsoft Security Blog · 24 sep 2026. Resumen mensual oficial de novedades de seguridad (Purview, Defender, Entra) útil para la rutina de actualización del equipo de cumplimiento.

**Manos a la obra**

1. `Laboratorio` Lee la [guía de estudio de SC-900](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-900) y, para cada habilidad relacionada con Compliance Manager, el Service Trust Portal y GRC, anota el módulo de esta guía que la cubre. Evidencia: matriz habilidad–módulo.
2. `Laboratorio` Configura tu rutina mensual: [What's new in Microsoft Purview](https://learn.microsoft.com/en-us/purview/whats-new), el [roadmap de Microsoft 365](https://www.microsoft.com/en-us/microsoft-365/roadmap), los avisos del Message Center sobre Compliance Manager (por ejemplo, [MC1192260](https://mc.merill.net/message/MC1192260)) y el resumen [What's new in Microsoft Security de noviembre de 2026](https://www.microsoft.com/en-us/security/blog/2026/11/05/whats-new-in-microsoft-security-november-2026/). Crea una bitácora con fecha, fuente, cambio, impacto y módulo afectado.
3. `Laboratorio` Lee el [hilo de Microsoft Q&A](https://learn.microsoft.com/en-gb/answers/questions/2081811/what-api-or-powershell-cmdlet-can-be-used-to-colle) sobre cómo extraer la puntuación y contrástalo con el [tutorial de APIs de Purview](https://learn.microsoft.com/en-us/purview/developer/use-the-api); escribe tu conclusión en tres líneas citando ambas fuentes.
4. `Laboratorio` Recorre el [Ninja oficial de 2023](https://techcommunity.microsoft.com/blog/microsoft-security-blog/microsoft-purview-compliance-manager-mspcm-ninja-training-q1-2023/3181322) y marca, con la tabla [Qué cambió](00_Programa.md#cambios), qué secciones siguen vigentes y cuáles cambiaron (portal, licencias, multinube, IA).

<a id="i1"></a>

## I1 · Compliance Manager hoy: puntuación, evaluaciones, roles y licencias

*L100–L200 · ~4 h · Origen: Ninja oficial de 2023, nivel Basic (recorrido por la herramienta)*

Compliance Manager te ayuda a gestionar requisitos regulatorios con cuatro piezas: **controles** (de Microsoft, tuyos o compartidos), **evaluaciones** que agrupan los controles de una regulación para uno o varios servicios, **regulaciones** o plantillas —más de 360— y **acciones de mejora** que traducen cada control en trabajo concreto. Sobre ellas calcula una **puntuación de cumplimiento basada en riesgo**: cada acción suma puntos según sea preventiva, detectiva o correctiva, y obligatoria o discrecional. Al entrar por primera vez, la puntuación inicial se apoya en la Data Protection Baseline.

La puntuación mide avance en acciones, no cumplimiento legal: los cambios se reflejan en hasta 24 horas, las acciones técnicas cuentan una vez por inquilino y las no técnicas una vez por grupo, así que el total no es el promedio de tus evaluaciones. Del lado de las licencias, Compliance Manager está disponible con Office 365 y Microsoft 365 (incluido Business Premium); todas las suscripciones traen la Data Protection Baseline, E5, A5 y G5 suman tres plantillas premium a elección y el resto se compra por plantilla. El acceso se controla con cuatro roles: Reader, Contribution, Assessor y Administration.

**Por qué importa**

La puntuación es la cifra más visible del programa y la más malinterpretada. Leerla bien evita presentar al comité un «78 %» como si fuera cumplimiento, y conocer las licencias evita comprar lo que ya tienes o gastar un cupo premium en una prueba. Los roles definen la segregación entre quien implementa y quien prueba, que es lo primero que revisa un auditor.

**Qué vas a lograr**

- Explicar qué mide la puntuación de cumplimiento, cómo se calcula y qué no significa.
- Separar los puntos de Microsoft de los que dependen de tu organización.
- Describir qué incluye cada licencia (E3, E5, Purview Suite y E7) y qué se compra por plantilla.
- Asignar los roles de Compliance Manager con mínimo privilegio y acceso por evaluación.
- Explicar por qué la puntuación global difiere del promedio de las evaluaciones.

> **Atención.** Licencias según Learn: todas las suscripciones incluyen la Data Protection Baseline y A5, E5 y G5 pueden usar **tres** plantillas premium sin costo; el resto se compra por plantilla, con licencia de un año que se renueva automáticamente y aparece en el inquilino en hasta 48 horas ([lista de regulaciones](https://learn.microsoft.com/en-us/purview/compliance-manager-regulations-list), [regulaciones](https://learn.microsoft.com/en-us/purview/compliance-manager-regulations)). Un blog de licenciamiento de 2026 afirma que E5 o E5 Compliance dan acceso a «300+ plantillas premium»: prevalece Learn ([blog](https://microsoftnegotiations.com/blog/microsoft-compliance-manager-licensing)).

> **Qué cambió.** Desde diciembre de 2022, E5, A5 y G5 eligen hasta tres plantillas premium en lugar de un conjunto fijo: seguir usando NIST 800-53, ISO 27001 o GDPR, antes incluidas, cuenta contra esos tres cupos, y las plantillas de una misma familia (por ejemplo, CMMC niveles 1 a 5) cuentan como una ([FAQ, actualizada el 21 de mayo de 2026](https://learn.microsoft.com/en-us/purview/compliance-manager-faq)).

> **Atención.** La descripción del servicio dice que Compliance Manager está disponible con licencias de Office 365 y Microsoft 365, incluido Business Premium, y que la disponibilidad de evaluaciones depende del contrato; no menciona Purview Suite (antes E5 Compliance) ni E7 al hablar de las plantillas premium. Confírmalo con tu equipo de licencias antes de planificar los cupos ([descripción del servicio](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)).

> **Consejo Ninja.** La puntuación global no es el promedio de tus evaluaciones: las acciones técnicas cuentan una vez por inquilino, las no técnicas una vez por grupo y los cambios tardan hasta 24 horas en verse ([puntuación](https://learn.microsoft.com/en-us/purview/compliance-manager-scoring)). Al reportar, separa tus puntos de los de Microsoft, como propone un laboratorio comunitario de 2026 ([laboratorio](https://techcertguide.blog/microsoft-purview-compliance-manager/)).

**¿Tienes poco tiempo?**

- [Microsoft Purview Compliance Manager (overview)](https://learn.microsoft.com/en-us/purview/compliance-manager) · Documentación
- [Compliance Manager scoring](https://learn.microsoft.com/en-us/purview/compliance-manager-scoring) · Documentación
- [Microsoft Purview Compliance Manager FAQ](https://learn.microsoft.com/en-us/purview/compliance-manager-faq) · Documentación
- [Simplify regulatory compliance with Microsoft Purview Compliance Manager (Microsoft Mechanics)](https://www.youtube.com/watch?v=OIVciVRwwZI) · Video

**Puntos por tipo de acción de mejora**

| Tipo de acción | Obligatoria | Discrecional |
|---|---|---|
| Preventiva | 27 | 9 |
| Detectiva | 3 | 1 |
| Correctiva | 3 | 1 |

Fuente: [Learn · puntuación de Compliance Manager](https://learn.microsoft.com/en-us/purview/compliance-manager-scoring). Las acciones técnicas cuentan una vez por inquilino y las no técnicas una vez por grupo; la puntuación mide avance, no cumplimiento legal.

### Documentación, cursos y credenciales

- [Microsoft Purview Compliance Manager FAQ](https://learn.microsoft.com/en-us/purview/compliance-manager-faq) · Documentación · Oficial · Nuevo · Microsoft Learn · 21 may 2026. Preguntas frecuentes: licenciamiento, uso con productos no Microsoft, el cambio de licencias de plantillas de diciembre de 2022 y por qué una puntuación alta no equivale a cumplimiento.
- [Compliance Manager scoring](https://learn.microsoft.com/en-us/purview/compliance-manager-scoring) · Documentación · Oficial · Microsoft Learn. Metodología de la puntuación de cumplimiento: puntos por acción de mejora según sea obligatoria o discrecional y preventiva, detectiva o correctiva, actualización en 24 horas y cálculo por suscripción para Defender for Cloud.
- [Microsoft Purview Compliance Manager (overview)](https://learn.microsoft.com/en-us/purview/compliance-manager) · Documentación · Oficial · Microsoft Learn. Visión general de Compliance Manager: controles (de Microsoft, propios y compartidos), evaluaciones, regulaciones (más de 360 plantillas) y acciones de mejora con puntuación basada en riesgo.
- [Microsoft Purview service description](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description) · Documentación · Oficial · Microsoft Learn (Service Descriptions). Descripción de servicio y licenciamiento de Purview por plan, con la sección de Compliance Manager y las reglas de quién necesita licencia.
- [Describe the data compliance solutions of Microsoft Purview (SC-900 module)](https://learn.microsoft.com/en-us/training/modules/describe-purview-risk-compliance-governance/) · Curso · Oficial · Microsoft Learn. Módulo introductorio que describe el portal de Purview y Compliance Manager junto con Communication Compliance, eDiscovery, Audit y gestión del ciclo de vida.
- [Glossary of terms for Microsoft Purview Compliance Manager](https://learn.microsoft.com/en-us/purview/compliance-manager-glossary) · Documentación · Oficial · Microsoft Learn · 4 feb 2025. Glosario oficial de términos (evaluación, control, acción de mejora, licencia, regulación, servicio, instancia de servicio, suscripción, recursos virtuales).

### Webinars, videos y podcasts

- [Simplify regulatory compliance with Microsoft Purview Compliance Manager (Microsoft Mechanics)](https://www.youtube.com/watch?v=OIVciVRwwZI) · Video · Empleado de Microsoft · Legado aún útil · Daniel Hidalgo y Jeremy Chapman · Microsoft Mechanics. Recorrido de 14 minutos por evaluaciones, acciones, permisos, alertas, exportación para auditores y actualización de regulaciones en Compliance Manager. *Nota:* Video de hace ~4 años (aprox. 2022): menciona 'más de 350 regulaciones' y el portal de cumplimiento antiguo; hoy se usa el portal unificado de Purview

### Laboratorios, GitHub y herramientas

- [Microsoft Purview Compliance Manager: Hands-On Lab (2026)](https://techcertguide.blog/microsoft-purview-compliance-manager/) · Laboratorio · Comunidad · Nuevo · Lokesh M · techcertguide.blog · 10 jul 2026. Laboratorio paso a paso del panel, evaluaciones, acciones, biblioteca de regulaciones y creación de una regulación propia, con foco en interpretar 'tus puntos' frente a los de Microsoft.

### Comunidad: blogs, libros, newsletters y eventos

- [Microsoft Compliance Manager Licensing: What's Included (2026)](https://microsoftnegotiations.com/blog/microsoft-compliance-manager-licensing) · Blog · Comunidad · Fredrik Filipsson · Microsoft Negotiations · mar 2026. Análisis comercial de licenciamiento que advierte que la puntuación no equivale a cumplimiento, pero afirma que E5 Compliance da acceso a todas las plantillas premium.
- [Microsoft Purview Compliance Manager: A Complete Guide for Modern Compliance Management](https://blog.apps4.pro/microsoft-purview-compliance-guide) · Blog · MVP · Narasima Perumal Chandramohan · Apps4.Pro · 17 dic 2025. Guía introductoria de Compliance Manager (puntuación, evaluaciones, plantillas, buenas prácticas) escrita por un MVP con enfoque de gobierno.

**Manos a la obra**

1. `Laboratorio` En tu prueba de E5, abre la evaluación de la Data Protection Baseline y anota la puntuación global, los puntos obtenidos y alcanzables, y cuántos provienen de acciones de Microsoft frente a las tuyas ([configuración](https://learn.microsoft.com/en-us/purview/compliance-manager-setup)). Evidencia: captura fechada.
2. `Laboratorio` Elige tres acciones de mejora (una preventiva obligatoria, una detectiva y una correctiva) y explica con la tabla de puntos de este módulo por qué valen distinto ([puntuación](https://learn.microsoft.com/en-us/purview/compliance-manager-scoring)).
3. `Laboratorio` Implementa una acción técnica sencilla de la línea base que se pruebe de forma automática y verifica el cambio de puntos al día siguiente; registra cuánto tardó en reflejarse (hasta 24 horas).
4. `Laboratorio` Asigna el rol Compliance Manager Reader a una cuenta de prueba y comprueba qué puede ver y qué no puede editar; anota qué rol de Entra ID daría un acceso equivalente ([configuración](https://learn.microsoft.com/en-us/purview/compliance-manager-setup)).
5. `Laboratorio` Redacta la ficha de licencias de tu organización con la tabla [Licencias](00_Programa.md#licencias): plan (E3, E5, Purview Suite o E7), cupos premium disponibles, plantillas activadas y fecha de renovación; marca las dudas para tu equipo de licencias ([FAQ](https://learn.microsoft.com/en-us/purview/compliance-manager-faq)).
6. `Solo producción` Explica al gestor de GRC la puntuación real de tu organización. Motivo: requiere los datos y las evaluaciones reales. Cómo hacerlo seguro: usa una cuenta con rol Reader, no modifiques acciones, exporta el informe y acompaña la cifra con la fecha de corte y las actualizaciones de plantillas aceptadas.

**¿Quieres profundizar?**

- [Microsoft Purview Compliance Manager: Hands-On Lab (2026)](https://techcertguide.blog/microsoft-purview-compliance-manager/) · Laboratorio

<a id="i2"></a>

## I2 · Plantillas regulatorias, cupos premium y la prueba de 90 días

*L200 · ~4 h · Origen: Ninja oficial de 2023, nivel Intermediate (plantillas y sus actualizaciones)*

Una plantilla (o regulación) es el contenido que Microsoft mantiene para una norma o un estándar: controles, acciones de mejora y su mapeo. La página **Regulations** las agrupa en cuatro bloques: *Sub-service compliance readiness* (vista previa, sin licencia), *Included templates*, *Premium AI templates* y *Premium templates*. Cada plantilla tiene además una **versión universal** para servicios no Microsoft, con implementación y pruebas manuales, y una licencia de regulación permite crear evaluaciones ilimitadas de sus distintas versiones. El tamaño varía mucho: ISO/IEC 27001:2022 tiene cientos de acciones y GDPR, unas decenas.

Para MCSA la oferta es corta: hay plantillas para México (protección de datos y protección al consumidor), Argentina (Ley 25.326), Colombia (Decreto 1377/2013, Circular Externa 007 de 2018 y Ley 1266/2008) y Perú (Ley 29733), y ninguna para Chile, Ecuador, Uruguay, Costa Rica, Panamá ni el resto de Centroamérica. Además, la plantilla de México sigue la ley de 2010, reemplazada en marzo de 2025. Para explorar antes de comprar existe una **prueba de evaluaciones premium**: 25 plantillas durante 90 días, una sola vez por inquilino.

**Por qué importa**

Los tres cupos premium de E5 son una decisión de gobierno con impacto plurianual: usarlos en una prueba o en una norma que no te aplica cuesta una licencia por plantilla por año. Saber qué existe para tu región evita comprar una plantilla que refleja una ley reemplazada y te obliga a planificar desde el inicio qué normas irán por plantilla propia.

**Qué vas a lograr**

- Navegar la página de regulaciones y distinguir sus cuatro agrupaciones.
- Decidir y documentar qué tres plantillas premium usar, con criterios de negocio.
- Planificar la prueba de 25 plantillas por 90 días sin perder trabajo al terminar.
- Identificar qué normas de MCSA tienen plantilla vigente, desactualizada o ninguna.
- Usar la versión universal de una plantilla para un servicio no Microsoft.

> **Novedad.** La página Regulations agrupa hoy las plantillas en *Sub-service compliance readiness* (vista previa, sin licencia), *Included templates*, **Premium AI templates** y *Premium templates*; Learn habla de más de 360 plantillas ([regulaciones](https://learn.microsoft.com/en-us/purview/compliance-manager-regulations), [evaluaciones](https://learn.microsoft.com/en-us/purview/compliance-manager-assessments)) y un laboratorio comunitario contó 391 en su inquilino en julio de 2026 ([laboratorio](https://techcertguide.blog/microsoft-purview-compliance-manager/)).

> **Atención.** La prueba de evaluaciones premium es única por inquilino: 25 plantillas premium durante 90 días. Al terminar, las plantillas usadas dejan de recibir actualizaciones y Microsoft recomienda borrar las evaluaciones que no compres ([prueba premium](https://learn.microsoft.com/en-us/purview/purview-compliance-manager-assessments-trial)). Exporta los informes antes de que venza.

> **Atención.** Plantillas de MCSA: México, Argentina, Colombia y Perú tienen plantilla; Chile, Ecuador, Uruguay, Costa Rica, Panamá y el resto de Centroamérica no. La de México corresponde a la ley de 2010, reemplazada por la nueva LFPDPPP publicada el 20 de marzo de 2025, y la lista no se actualiza desde el 6 de marzo de 2025 ([lista](https://learn.microsoft.com/en-us/purview/compliance-manager-regulations-list), [LFPDPPP](https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPDPPP.pdf)). Detalle en [Plantillas para MCSA](00_Programa.md#plantillas-mcsa).

> **Consejo Ninja.** Mide el tamaño antes de elegir: según un análisis comunitario de octubre de 2026, ISO/IEC 27001:2022 tiene 265 acciones (110 tuyas y 155 de Microsoft, 4.220 puntos) y su mapeo se actualizó por última vez el 18 de octubre de 2023, mientras GDPR tiene 49 acciones ([análisis de plantillas](https://informasjonsbeskyttelse.no/en/premium-templates)). Una licencia de regulación permite evaluaciones ilimitadas de sus versiones ([glosario](https://learn.microsoft.com/en-us/purview/compliance-manager-glossary)).

**¿Tienes poco tiempo?**

- [Learn about regulations in Microsoft Purview Compliance Manager](https://learn.microsoft.com/en-us/purview/compliance-manager-regulations) · Documentación
- [Microsoft Purview Compliance Manager regulations list](https://learn.microsoft.com/en-us/purview/compliance-manager-regulations-list) · Documentación
- [Learn about the Microsoft Purview Compliance Manager premium assessments trial](https://learn.microsoft.com/en-us/purview/purview-compliance-manager-assessments-trial) · Documentación

### Documentación, cursos y credenciales

- [Learn about regulations in Microsoft Purview Compliance Manager](https://learn.microsoft.com/en-us/purview/compliance-manager-regulations) · Documentación · Oficial · Microsoft Learn. Explica disponibilidad y licenciamiento de regulaciones: línea base incluida, plantillas premium y premium de IA compradas por plantilla por un año, hasta tres premium gratis según contrato y prueba de 25 plantillas por 90 días.
- [Learn about the Microsoft Purview Compliance Manager premium assessments trial](https://learn.microsoft.com/en-us/purview/purview-compliance-manager-assessments-trial) · Documentación · Oficial · Microsoft Learn. Explica la prueba única de evaluaciones premium: 25 plantillas regulatorias premium a elección durante 90 días, roles que pueden iniciarla y qué pasa con las plantillas al terminar.
- [Microsoft Purview Compliance Manager regulations list](https://learn.microsoft.com/en-us/purview/compliance-manager-regulations-list) · Documentación · Oficial · Microsoft Learn · 6 mar 2025. Lista completa de plantillas regulatorias de Compliance Manager por región e industria, incluidas las de IA y las de México, Argentina, Colombia y Perú, y qué se incluye por licencia.

### Comunidad: blogs, libros, newsletters y eventos

- [Regulatory Templates](https://informasjonsbeskyttelse.no/en/premium-templates) · Blog · Comunidad · Nuevo · Roy Allan Hansen · Data Protection with Microsoft Purview (informasjonsbeskyttelse.no) · 22 oct 2026. Recorrido práctico y actualizado de la página Regulations: cuatro agrupaciones, contador de licencias, familias que cuentan como una sola plantilla y tamaño real de plantillas como ISO 27001:2022 y GDPR.

**Manos a la obra**

1. `Laboratorio` En la página Regulations, filtra las cuatro agrupaciones y anota cuántas plantillas ves en cada una y cuántas licencias llevas usadas; guarda la captura ([regulaciones](https://learn.microsoft.com/en-us/purview/compliance-manager-regulations)).
2. `Laboratorio` Construye una matriz de decisión para tus tres cupos premium (obligación legal, exigencia del supervisor, contratos con clientes, esfuerzo estimado, familias que cuentan como una) y deja la recomendación firmada por el gestor de GRC ([FAQ](https://learn.microsoft.com/en-us/purview/compliance-manager-faq)).
3. `Laboratorio parcial` Activa la [prueba de evaluaciones premium](https://learn.microsoft.com/en-us/purview/purview-compliance-manager-assessments-trial) y crea evaluaciones ISO/IEC 27001:2022 y NIST CSF 2.0 en un grupo de prueba. Limitación: la prueba es única por inquilino (25 plantillas, 90 días) y las plantillas usadas dejan de actualizarse al terminar; exporta los informes antes del día 90.
4. `Laboratorio parcial` Abre la plantilla de una norma de MCSA (por ejemplo, la Ley 29733 de Perú o la Circular Externa 007 de 2018 de Colombia) y compara diez controles con el texto oficial vigente; anota los requisitos que faltan. Limitación: consume un cupo premium o parte de la prueba ([lista de regulaciones](https://learn.microsoft.com/en-us/purview/compliance-manager-regulations-list)).
5. `Laboratorio` Crea una evaluación de la Data Protection Baseline para un servicio ficticio agregado como «nuevo servicio» y documenta qué acciones pasan a implementación y prueba manuales con la versión universal ([multinube](https://learn.microsoft.com/en-us/purview/compliance-manager-multicloud)).
6. `Solo producción` Activa en producción las tres plantillas premium elegidas. Motivo: compromete cupos del contrato real. Cómo hacerlo seguro: aprobación previa del comité, evaluación inicial en un grupo piloto, nada de copiar plantillas premium «para probar» y registro de la fecha de activación para controlar la renovación anual.

**¿Quieres profundizar?**

- [Regulatory Templates](https://informasjonsbeskyttelse.no/en/premium-templates) · Blog

<a id="i3"></a>

## I3 · Acciones de mejora, pruebas y evidencias

*L200 · ~4 h · Origen: Ninja oficial de 2023, nivel Intermediate (acciones de mejora)*

Las acciones de mejora son el lugar donde el cumplimiento se convierte en trabajo. Cada una indica qué hacer, quién es responsable según el modelo de responsabilidad compartida, cómo se prueba y qué evidencia la respalda. La prueba puede ser automática por cuatro vías —integración con soluciones de Purview y Priva, **Secure Score**, **Defender for Cloud** y conectores— o manual, a cargo de tu equipo. Desde cada acción puedes asignar responsables, registrar el estado de implementación y de prueba, agregar notas y adjuntar documentos.

A escala, el trabajo se hace en bloque: exportas las acciones a Excel, actualizas estado, pruebas, responsables, notas y evidencias, y vuelves a cargar el archivo. Solo aplica a acciones gestionadas por tu organización que ya estén asociadas a una evaluación, y el mapeo de controles exportado no se puede modificar. Recuerda el alcance: una acción técnica actualizada impacta todas las evaluaciones de todos los grupos; una no técnica, solo las de su grupo. Y cuida lo que subes: una evidencia nunca debe contener datos personales ni secretos.

**Por qué importa**

Sin responsables, fechas y evidencias, la puntuación es una métrica de vanidad. Una buena disciplina de evidencias reduce el costo de cada auditoría, evita repetir el mismo trabajo para varias regulaciones y permite que auditoría interna pruebe de forma independiente lo que TI declara implementado.

**Qué vas a lograr**

- Explicar los cuatro tipos de prueba automática y cuándo la prueba es manual.
- Asignar acciones, registrar estados y adjuntar evidencias útiles y seguras.
- Actualizar acciones en bloque con Excel sin romper el mapeo.
- Acordar con auditoría interna criterios de evidencia aceptable.

> **Consejo Ninja.** Las acciones se prueban de forma automática por cuatro vías —integración con Purview y Priva, Secure Score, Defender for Cloud y conectores— o de forma manual. Las evaluadas por Defender for Cloud no pueden pasar a prueba manual: si no estás de acuerdo con el resultado, ajusta la evaluación en Defender for Cloud ([acciones de mejora](https://learn.microsoft.com/en-us/purview/compliance-manager-improvement-actions)).

> **Atención.** La carga masiva desde Excel solo aplica a acciones gestionadas por tu organización y ya asociadas a una evaluación; el mapeo de controles exportado no se puede modificar ([actualizar acciones](https://learn.microsoft.com/en-us/purview/compliance-manager-update-actions)).

> **Atención.** Una acción técnica que actualizas impacta todas las evaluaciones de todos los grupos; una no técnica, solo las de su grupo ([evaluaciones](https://learn.microsoft.com/en-us/purview/compliance-manager-assessments)). Antes de marcar una acción técnica como implementada, avisa a los dueños de las otras evaluaciones.

> **Consejo Ninja.** Una regla de supervisor que sirve para cualquier auditoría: si no hay evidencia razonable, el control no se marca como cumplido. El Banco Central del Uruguay valida, observa o rechaza cada evidencia referenciada en las autoevaluaciones de su Marco de Ciberseguridad ([nota metodológica del BCU, abril de 2026](https://www.bcu.gub.uy/Comunicados/Anexo%201%20-%20Nota%20metodologica%20V2.pdf)).

**¿Tienes poco tiempo?**

- [Working with improvement actions in Microsoft Purview Compliance Manager](https://learn.microsoft.com/en-us/purview/compliance-manager-improvement-actions) · Documentación
- [Update improvement actions and bring compliance data into Microsoft Purview Compliance Manager](https://learn.microsoft.com/en-us/purview/compliance-manager-update-actions) · Documentación
- [Compliance Manager - Microsoft Security Workshop (lab)](https://indra-pr.github.io/msft-security-workshop/purview/data-compliance/compliance-manager/) · Laboratorio

### Documentación, cursos y credenciales

- [Working with improvement actions in Microsoft Purview Compliance Manager](https://learn.microsoft.com/en-us/purview/compliance-manager-improvement-actions) · Documentación · Oficial · Microsoft Learn. Acciones de mejora: modelo de responsabilidad compartida, cuatro tipos de automatización (integrada con Purview/Priva, Secure Score, Defender for Cloud y conectores), pruebas manuales o automáticas, evidencias, notas, asignación y exportación.

### Laboratorios, GitHub y herramientas

- [Compliance Manager - Microsoft Security Workshop (lab)](https://indra-pr.github.io/msft-security-workshop/purview/data-compliance/compliance-manager/) · Laboratorio · Comunidad · indra-pr · GitHub Pages (msft-security-workshop). Laboratorio de 1,5-2 horas: roles de mínimo privilegio, evaluación de línea base, evaluación de regulación, evaluación personalizada y conectores.

### Comunidad: blogs, libros, newsletters y eventos

- [How to Use Compliance Manager for Microsoft 365](https://configcobra.com/blog/how-to-use-compliance-manager-microsoft-365) · Blog · Comunidad · Robert Kiss · ConfigCobra · 16 feb 2026. Guía práctica de navegación, evaluaciones, controles, evidencias y plantillas personalizadas con relación a benchmarks CIS.

**Manos a la obra**

1. `Laboratorio` Exporta a Excel las acciones de mejora de tu evaluación de práctica, completa estado, responsable, fecha y notas de cinco acciones y vuelve a cargar el archivo; verifica los cambios en el portal ([actualizar acciones](https://learn.microsoft.com/en-us/purview/compliance-manager-update-actions)).
2. `Laboratorio` Asigna una acción a una cuenta de prueba y adjunta como evidencia un documento sintético (sin datos personales ni secretos), con fecha y responsable en el nombre del archivo ([acciones de mejora](https://learn.microsoft.com/en-us/purview/compliance-manager-improvement-actions)).
3. `Laboratorio` Identifica en tu evaluación una acción probada por Secure Score, otra por la integración con Purview y otra de prueba manual; documenta quién es responsable de cada prueba.
4. `Laboratorio` Con dos grupos de evaluaciones, marca como implementada una acción no técnica en uno y comprueba que no cambia en el otro; repite con una acción técnica y documenta el efecto ([evaluaciones](https://learn.microsoft.com/en-us/purview/compliance-manager-assessments)).
5. `Laboratorio` Redacta con auditoría interna una guía de evidencia aceptable (qué se adjunta, formato, fecha, responsable y retención) con tres ejemplos aceptables y tres rechazables, inspirada en la [nota metodológica del BCU](https://www.bcu.gub.uy/Comunicados/Anexo%201%20-%20Nota%20metodologica%20V2.pdf).
6. `Solo producción` Migra a Compliance Manager el seguimiento de controles que hoy vive en planillas, con la carga masiva. Motivo: requiere acciones, responsables y evidencias reales. Cómo hacerlo seguro: piloto con una sola evaluación, copia del archivo original, revisión de los cambios por una segunda persona y validación de una muestra en el portal antes de cargar el resto.

<a id="reto-inicial"></a>

## Reto del nivel

**Tu línea base defendible.** En tu laboratorio, asigna los roles de Compliance Manager a cuentas de prueba, trabaja la evaluación de la Data Protection Baseline hasta implementar cinco acciones con evidencia sintética y exporta el informe antes y después. Entrega una nota de una página que explique la puntuación (tus puntos frente a los de Microsoft, fecha de corte y actualizaciones aceptadas) y un memorando de decisión sobre tus tres cupos premium, con la ficha de licencias de tu organización.

<a id="quiz-inicial"></a>

## Evaluación del nivel

Responde y compara con [Evaluaciones y respuestas](06_Evaluaciones_y_respuestas.md#eval-inicial). Con 80 % o más, ¡nivel aprobado! (En la versión web puedes corregir en línea y generar tu certificado).

1. ¿Qué plantillas puede usar sin costo adicional una organización con Microsoft 365 E5?
   - a) Todas las plantillas premium de la biblioteca
   - b) Solo ISO 27001, NIST 800-53 y GDPR
   - c) La Data Protection Baseline y hasta tres plantillas premium a elección
   - d) Ninguna: todas requieren compra

2. ¿Qué ofrece la prueba de evaluaciones premium?
   - a) 10 plantillas durante 30 días, renovable
   - b) 25 plantillas premium durante 90 días, una sola vez por inquilino
   - c) Plantillas ilimitadas durante un año
   - d) Solo las plantillas de IA durante 60 días

3. Una organización con E5 usa CMMC niveles 1 y 2. ¿Cuántos cupos premium consume?
   - a) Uno, porque las plantillas de una misma familia cuentan como una
   - b) Dos, uno por nivel
   - c) Ninguno, porque CMMC está incluido para todos
   - d) Cinco, uno por cada nivel de la familia

4. ¿Qué mide la puntuación de cumplimiento de Compliance Manager?
   - a) El cumplimiento legal certificado de la organización
   - b) La postura de seguridad comparada con organizaciones similares
   - c) La cantidad de alertas de DLP resueltas
   - d) El avance en acciones de mejora, con puntos ponderados por tipo de acción

5. ¿Por qué la puntuación global puede diferir del promedio de tus evaluaciones?
   - a) Porque Microsoft redondea cada regulación
   - b) Porque las acciones técnicas cuentan una vez por inquilino y las no técnicas una vez por grupo
   - c) Porque las evaluaciones premium pesan el doble
   - d) Porque solo cuenta la última evaluación creada

6. ¿Qué tipo de acción de mejora otorga más puntos?
   - a) Detectiva obligatoria
   - b) Correctiva obligatoria
   - c) Preventiva obligatoria
   - d) Preventiva discrecional

7. ¿Qué país de MCSA tiene plantilla en Compliance Manager para su ley general de datos personales?
   - a) Chile
   - b) Uruguay
   - c) Panamá
   - d) Perú

8. ¿Qué problema tiene hoy la plantilla de México sobre datos personales?
   - a) Corresponde a la ley de 2010, reemplazada por la nueva LFPDPPP publicada el 20 de marzo de 2025
   - b) Solo está disponible para nubes de gobierno
   - c) No existe: México no tiene plantilla
   - d) Cubre solo al sector público

9. ¿A qué acciones aplica la actualización masiva desde Excel?
   - a) A todas, incluidas las gestionadas por Microsoft
   - b) Solo a las acciones gestionadas por tu organización que ya están asociadas a una evaluación
   - c) Solo a las acciones probadas por Defender for Cloud
   - d) A las acciones de cualquier inquilino del mismo contrato

10. No estás de acuerdo con el resultado de una acción probada por Defender for Cloud. ¿Qué haces?
   - a) La cambias a prueba manual en Compliance Manager
   - b) Borras la acción y la vuelves a crear
   - c) Ajustas la configuración o la evaluación en Defender for Cloud
   - d) Pides a Microsoft que cambie la puntuación

11. Marcas como implementada una acción técnica en una evaluación del grupo A. ¿Qué ocurre?
   - a) Solo cambia en la evaluación donde la marcaste
   - b) Cambia en las evaluaciones del grupo A, pero no en las de otros grupos
   - c) No cambia nada hasta que auditoría interna la pruebe
   - d) Impacta todas las evaluaciones de todos los grupos

12. ¿Para qué sirve el Service Trust Portal en un programa de cumplimiento?
   - a) Para descargar informes de auditoría de Microsoft que evidencian los controles que gestiona Microsoft
   - b) Para crear evaluaciones de Compliance Manager
   - c) Para comprar plantillas premium
   - d) Para configurar conectores de AWS y GCP

13. ¿Qué credencial vigente evalúa Compliance Manager de forma explícita?
   - a) SC-400
   - b) SC-401
   - c) SC-900
   - d) MS-101

14. ¿Cuándo se retiró el portal de cumplimiento clásico?
   - a) En julio de 2024, el mismo día de la disponibilidad general del nuevo portal
   - b) Entre el 14 de noviembre y el 14 de diciembre de 2024
   - c) El 1 de octubre de 2025
   - d) Sigue disponible hasta 2027

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. No constituye asesoría legal: la normativa citada es material de referencia y las decisiones de aplicabilidad corresponden a tus áreas de Legal, privacidad y, cuando aplique, RR. HH. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

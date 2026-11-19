# Nivel 4 · Operación · Modelo operativo, métricas y gobierno

*Microsoft Purview DSPM y seguridad de datos para IA Ninja Training · Edición 2026*

[← Nivel 3 · Avanzado](03_Nivel_3_Avanzado.md) · [Índice del programa](README.md) · [Comunidad →](05_Comunidad.md)

<a id="operacion"></a>

Cómo se organiza un programa continuo de preparación de datos para la IA: responsabilidades, ciclo mensual, métricas, costos, privacidad y normativa de MCSA, sin interpretar la ley. Terminas con un RACI, un tablero mensual y un procedimiento de derechos de los titulares sobre interacciones de IA.

*L300–L400 · 3 módulos · ~11 horas · 15 recursos*

**Módulos de este nivel:** [O1 Modelo operativo](#o1) · [O2 Métricas y mejora continua](#o2) · [O3 Gobierno y privacidad MCSA](#o3)

<a id="o1"></a>

## O1 · Modelo operativo del equipo y responsabilidades

*L300–L400 · ~4 h · Origen: Modelo de despliegue de DSPM de Microsoft Learn y guía «Protect sensitive data to get ready for AI»*

DSPM no es un proyecto con fecha de cierre: es un **modelo operativo**. El modelo de despliegue oficial tiene cuatro pasos (fundamentos, acceso y analítica, entender los riesgos, y actuar e investigar con Security Copilot) y un **ciclo mensual** de revisión de recomendaciones. La guía de Microsoft para preparar los datos para la IA plantea esa preparación como un trabajo continuo en tres fases: entender y reducir la exposición, proteger las interacciones, e investigar y demostrar cumplimiento.

Los roles se reparten así. El **líder de seguridad de datos** es dueño de la postura y de los objetivos. El **centro de excelencia o comité de gobierno de IA** aprueba casos de uso, apps y agentes. Los **administradores de Microsoft 365 y SharePoint** ejecutan las remediaciones con los propietarios de sitios. El **SOC** atiende alertas e investigaciones, y **privacidad y Legal** deciden sobre captura de contenido, derechos de los titulares y evaluaciones de impacto. El **CISO** fija prioridades y presupuesto.

La supervisión humana es parte del diseño. La IA de DSPM puede quitar vínculos públicos, aplicar DLP o revocar permisos, pero lo hace bajo supervisión, y las acciones de los agentes se revisan, aprueban y siempre se auditan. Para la adopción de agentes, FastTrack ofrece asistencia remota con Agent 365.

**Por qué importa**

Sin responsables claros, los hallazgos de DSPM se acumulan. ¿Quién desactiva un vínculo? ¿Quién aprueba un agente? ¿Quién puede leer un prompt? Este módulo define un RACI, cadencias y flujos de aprobación (incluida la de privacidad) para que la postura mejore mes a mes. También fija reglas de supervisión humana para las remediaciones que propone la IA.

**Qué vas a lograr**

- Definir responsabilidades (RACI) entre seguridad de datos, gobierno de IA, administración de Microsoft 365, SOC, privacidad y propietarios de datos.
- Establecer el ciclo mensual de revisión de objetivos y recomendaciones.
- Diseñar el flujo de aprobación para remediaciones asistidas por IA y acciones de agentes.
- Planificar la adopción de agentes con el apoyo de FastTrack y del taller Zero Trust.

> **Consejo Ninja.** El modelo de despliegue de DSPM propone cuatro pasos (fundamentos, acceso y analítica, entender los riesgos, y actuar e investigar con Security Copilot) y un ciclo mensual de revisión de recomendaciones ([modelo de despliegue](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-dspm-intro)). El paso 3 recomienda revisar las recomendaciones al menos cada 30 días ([paso 3](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-dspm-step3)).

> **Atención.** La IA de DSPM puede actuar sobre los riesgos (quitar vínculos públicos, aplicar DLP o revocar permisos) bajo supervisión, y las acciones de los agentes se revisan, aprueban y siempre se auditan ([DSPM](https://learn.microsoft.com/en-us/purview/data-security-posture-management-learn-about)). Define por escrito qué acciones requieren aprobación humana y de quién.

> **Novedad.** FastTrack ofrece asistencia remota para Agent 365: inventario de agentes, identidad, controles base en Entra, Defender y Purview, y flujos de monitoreo y respuesta (página del 16 de octubre de 2026) ([FastTrack para Agent 365](https://learn.microsoft.com/en-us/microsoft-365/fasttrack/microsoft-agent-365)).

> **Consejo Ninja.** La guía oficial «From Oversharing to Enforcement» (23 de abril de 2026) propone un modelo de madurez por fases que va de la visibilidad a la aplicación de controles. Sirve para acordar con el comité de IA qué fase se alcanza cada trimestre ([guía práctica](https://techcommunity.microsoft.com/blog/microsoft-purview-blog/from-oversharing-to-enforcement-a-practical-guide-to-ai-data-security-with-micro/4513727)).

**¿Tienes poco tiempo?**

- [Deploy and use Data Security Posture Management (deployment model)](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-dspm-intro) · Documentación
- [Protect sensitive data to get ready for AI (Microsoft Purview security imperative)](https://learn.microsoft.com/en-us/purview/protect-sensitive-data-to-get-ready-for-ai) · Documentación
- [From Oversharing to Enforcement: A Practical Guide to AI Data Security with Microsoft Purview](https://techcommunity.microsoft.com/blog/microsoft-purview-blog/from-oversharing-to-enforcement-a-practical-guide-to-ai-data-security-with-micro/4513727) · Blog oficial

**RACI de referencia del programa de seguridad de datos para IA**

| Actividad | Seguridad de datos | Gobierno de IA (CoE) | Administración de Microsoft 365 y SharePoint | SOC | Privacidad y Legal | Dueños de datos y sitios | CISO |
|---|---|---|---|---|---|---|---|
| Configurar DSPM, roles y tareas iniciales | A/R | I | C | I | C | — | I |
| Revisión mensual de objetivos y recomendaciones | A/R | C | C | C | I | I | I |
| Evaluaciones de riesgo de datos y priorización de sitios | A | I | R | — | I | C | I |
| Remediación de permisos (SAM, vínculos, RCD y RAC) | C | I | A/R | — | — | R | I |
| Aprobar, sancionar o bloquear apps y agentes de IA | R | A | C | C | C | I | I |
| DLP para Copilot e IA de terceros (diseño, simulación y activación) | A/R | C | C | I | C | C | I |
| Captura de prompts y directivas de colección | R | C | — | I | A | — | I |
| Triaje de alertas de DLP e Insider Risk y escalamiento | C | I | — | A/R | C | — | I |
| Agentes de Security Copilot (SCU, identidades y aprobaciones) | A | C | — | R | C | — | C |
| Solicitudes de derechos sobre interacciones de IA | R | I | C | I | A | — | I |
| Licencias y presupuesto de pago por uso y SCU | R | C | C | C | — | — | A |
| Reporte al comité de IA y a la dirección | R | R | I | C | C | I | A |

R: responsable de ejecutar · A: aprueba y rinde cuentas · C: consultado · I: informado. Es un punto de partida, no una norma: ajústalo a tu estructura con el [modelo de despliegue de DSPM](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-dspm-intro) y la guía [Protect sensitive data to get ready for AI](https://learn.microsoft.com/en-us/purview/protect-sensitive-data-to-get-ready-for-ai).

### Documentación, cursos y credenciales

- [Copilot controls security and governance](https://learn.microsoft.com/en-us/copilot/implement/copilot-controls-security-governance) · Documentación · Oficial · Microsoft Learn. Marco de controles de seguridad y gobierno para Copilot y agentes que separa controles fundamentales (E3 + SAM) de optimizados (E5: DSPM, autoetiquetado, IRM, Defender for Cloud Apps).
- [Protect sensitive data to get ready for AI (Microsoft Purview security imperative)](https://learn.microsoft.com/en-us/purview/protect-sensitive-data-to-get-ready-for-ai) · Documentación · Oficial · Microsoft Learn. Guía estratégica que plantea la preparación de datos para IA como modelo operativo continuo en tres fases: entender y reducir exposición, proteger interacciones e investigar y demostrar cumplimiento.
- [Deploy and use Data Security Posture Management (deployment model)](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-dspm-intro) · Documentación · Oficial · Microsoft Learn · 3 abr 2026. Modelo de despliegue en cuatro pasos (fundamentos, acceso y analítica, entender riesgos, actuar e investigar con Security Copilot) con ciclo mensual de revisión de recomendaciones.
- [Microsoft Agent 365 - FastTrack](https://learn.microsoft.com/en-us/microsoft-365/fasttrack/microsoft-agent-365) · Documentación · Oficial · Nuevo · Microsoft Learn · 16 oct 2026. Detalla la asistencia remota de FastTrack para Agent 365: inventario de agentes, identidad, controles base en Entra, Defender y Purview y flujos de monitoreo y respuesta.

### Anuncios y blogs oficiales

- [From Oversharing to Enforcement: A Practical Guide to AI Data Security with Microsoft Purview](https://techcommunity.microsoft.com/blog/microsoft-purview-blog/from-oversharing-to-enforcement-a-practical-guide-to-ai-data-security-with-micro/4513727) · Blog oficial · Empleado de Microsoft · George Smyrlis · Microsoft Purview Blog (Tech Community) · 23 abr 2026. Guía práctica oficial para pasar de la visibilidad a la aplicación de controles: DLP a nivel de prompt, descubrimiento de IA en la sombra, objetivos de DSPM y un modelo de madurez por fases.

### Laboratorios, GitHub y herramientas

- [Deploy Risky AI and Risky Agents Policies (Zero Trust Workshop – AI)](https://microsoft.github.io/zerotrustassessment/docs/workshop-guidance/AI/AI_061) · Laboratorio · Oficial · Microsoft Zero Trust Workshop (GitHub Pages). Tarjeta del taller Zero Trust (pilar IA) que guía el despliegue de las directivas Risky AI usage y Risky Agents con esfuerzo e impacto bajos y enlaces de referencia.

**Manos a la obra**

1. `Laboratorio` RACI: completa la tabla RACI de este módulo para tu organización y valídala con cada área. Evidencia: RACI aprobado.
2. `Laboratorio` Calendario operativo: define la cadencia semanal (alertas y SCU), mensual (objetivos y recomendaciones de DSPM) y trimestral (comité de IA, licencias y presupuesto) siguiendo el [modelo de despliegue de DSPM](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-dspm-intro). Evidencia: invitaciones y agendas tipo.
3. `Laboratorio` Aprobación de remediaciones con IA: documenta qué acciones del Posture Agent o de DSPM (quitar vínculos, aplicar DLP o revocar permisos) se ejecutan solo con aprobación humana y quién aprueba cada una. Evidencia: procedimiento firmado.
4. `Laboratorio` Plan de despliegue de las políticas de riesgo de IA: usa la tarjeta del taller Zero Trust para Risky AI usage y Risky Agents como plan de implementación, con esfuerzo, impacto y responsables ([taller Zero Trust](https://microsoft.github.io/zerotrustassessment/docs/workshop-guidance/AI/AI_061)). Evidencia: plan con fechas.
5. `Solo producción` Primer ciclo mensual: revisa con los responsables los objetivos y recomendaciones de producción, asigna cada hallazgo y mide su cierre a 30 días. Cómo hacerlo seguro: roles de solo lectura durante la revisión y cambios por ticket con aprobación. Evidencia: acta y tablero de seguimiento.

**¿Quieres profundizar?**

- [Deploy Risky AI and Risky Agents Policies (Zero Trust Workshop – AI)](https://microsoft.github.io/zerotrustassessment/docs/workshop-guidance/AI/AI_061) · Laboratorio

<a id="o2"></a>

## O2 · Métricas, reportes y mejora continua

*L300–L400 · ~3 h · Origen: Nuevo en esta edición*

La página *Posture* muestra métricas clave, objetivos priorizados por riesgo y una **tendencia de 30 días**; las tarjetas de objetivo miden la cobertura de políticas y los incidentes de compartición riesgosa. El paso 3 del modelo de despliegue propone un indicador simple: el **porcentaje de activos sensibles protegidos por al menos una política DLP**. El **Usage center** (en preview) muestra el consumo de pago por uso por función y los usuarios en alcance sin licencia. Para la dirección, el Security Dashboard for AI resume inventario, riesgos y recomendaciones de IA.

Como referencia externa, el **Data Security Index 2026** indica que el 32 % de los incidentes de datos involucra IA generativa y que solo el 47 % de las organizaciones aplica controles específicos de IA. Úsalo con criterio: la encuesta reunió a más de 1.700 profesionales de 10 mercados y representa a Latinoamérica solo con Brasil. Tu mejor línea base es la tuya, medida el primer mes y comparada cada mes.

**Por qué importa**

Lo que no se mide no mejora, y los comités de IA necesitan tendencias, no capturas de pantalla. Un conjunto corto de métricas con fuente, responsable y frecuencia convierte DSPM en un programa de mejora continua. También justifica inversiones (E5 frente a E7, pago por uso o SCU) con datos.

**Qué vas a lograr**

- Definir un tablero mensual con métricas de exposición, cobertura, IA, operación, costo y privacidad.
- Usar la tendencia de 30 días y los informes de DSPM como fuente principal.
- Medir el costo de pago por uso y de SCU por capacidad.
- Comparar tu línea base con el Data Security Index 2026 sin extrapolar conclusiones a MCSA.

> **Novedad.** Data Security Index 2026 (29 de enero de 2026): el 32 % de los incidentes de datos involucra IA generativa y solo el 47 % de las organizaciones aplica controles específicos de IA ([resumen](https://www.microsoft.com/en-us/security/blog/2026/01/29/new-microsoft-data-security-index-report-explores-secure-ai-adoption-to-protect-sensitive-data/)). La muestra, de más de 1.700 profesionales en 10 mercados, representa a Latinoamérica solo con Brasil: úsalo como referencia, no como línea base regional ([informe](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/security/Data-Security-Index-Unifying-Data-Protection.pdf)).

> **Consejo Ninja.** La página Posture muestra métricas clave, objetivos priorizados por riesgo y una tendencia de 30 días; las tarjetas de objetivo miden la cobertura de políticas y los incidentes de compartición riesgosa ([DSPM](https://learn.microsoft.com/en-us/purview/data-security-posture-management-learn-about)). El paso 3 del modelo de despliegue propone el indicador de porcentaje de activos sensibles protegidos por al menos una política DLP ([paso 3](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-dspm-step3)).

> **Atención.** El Usage center de Purview está en preview: muestra el consumo de pago por uso por función y los usuarios en alcance sin licencia ([Usage center](https://learn.microsoft.com/en-us/purview/purview-billing-usage)). Revísalo cada semana mientras haya pilotos de IA de terceros o de red.

**¿Tienes poco tiempo?**

- [New Microsoft Data Security Index report explores secure AI adoption to protect sensitive data](https://www.microsoft.com/en-us/security/blog/2026/01/29/new-microsoft-data-security-index-report-explores-secure-ai-adoption-to-protect-sensitive-data/) · Blog oficial
- [Manage pay-as-you-go and per-user licensing usage (Usage center)](https://learn.microsoft.com/en-us/purview/purview-billing-usage) · Documentación
- [Assess your organization's AI risk with Microsoft Security Dashboard for AI](https://learn.microsoft.com/en-us/security/security-for-ai/security-dashboard-for-ai) · Documentación

**Métricas del tablero mensual**

| Métrica | Qué mide | Fuente de datos | Frecuencia | Responsable |
|---|---|---|---|---|
| Sitios sobrecompartidos abiertos | Exposición | Evaluaciones de riesgo de datos de DSPM | Semanal | Administración de SharePoint |
| Vínculos amplios y grupos de toda la organización corregidos | Exposición | Desactivación masiva de vínculos en DSPM e informes DAG de SAM | Mensual | Administración de SharePoint |
| Porcentaje de activos sensibles protegidos por al menos una política DLP | Cobertura | DSPM (indicador del paso 3 del modelo de despliegue) | Mensual | Seguridad de datos |
| Porcentaje de archivos sensibles etiquetados en los sitios prioritarios | Cobertura | Informes de etiquetado y explorador de contenido | Mensual | Information Protection |
| Tendencia de 30 días por objetivo de seguridad de datos | Postura | Página Posture de DSPM | Mensual | Seguridad de datos |
| Interacciones de IA con datos sensibles | IA | AI observability y explorador de actividad | Semanal | Seguridad de datos |
| Apps de IA sancionadas frente a no autorizadas con uso | IA | Defender for Cloud Apps y AI observability | Mensual | Gobierno de IA |
| Agentes de riesgo alto y agentes sin propietario | IA (agentes) | AI observability y Risky Agents (E7 o Agent 365) | Mensual | Gobierno de IA |
| Tiempo medio de remediación de hallazgos | Operación | Tickets y DSPM | Mensual | Seguridad de datos |
| Alertas de DLP e Insider Risk de IA triadas y tiempo de triaje | Operación | Defender XDR y Data Security Triage Agent | Semanal | SOC |
| Consumo de pago por uso por función | Costo | Usage center (preview) y Azure Cost Management | Semanal durante pilotos | Dueño del presupuesto |
| SCU consumidas por agente | Costo | Uso de Security Copilot y rendimiento de cada agente | Semanal | SOC y seguridad de datos |
| Solicitudes de derechos sobre interacciones de IA atendidas en plazo | Privacidad | Casos de eDiscovery y registro de solicitudes | Mensual | Privacidad |

Fuentes: [DSPM](https://learn.microsoft.com/en-us/purview/data-security-posture-management-learn-about), [modelo de despliegue](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-dspm-intro), [Usage center](https://learn.microsoft.com/en-us/purview/purview-billing-usage) y [Security Dashboard for AI](https://learn.microsoft.com/en-us/security/security-for-ai/security-dashboard-for-ai). Define la meta de cada métrica después de medir la línea base del primer mes.

### Documentación, cursos y credenciales

- [Assess your organization's AI risk with Microsoft Security Dashboard for AI](https://learn.microsoft.com/en-us/security/security-for-ai/security-dashboard-for-ai) · Documentación · Oficial · Microsoft Learn. Tablero ejecutivo que agrega señales de Entra, Defender y Purview sobre inventario de IA (Copilot, agentes, Foundry, Gemini, ChatGPT, servidores MCP), riesgos y recomendaciones asignables, con Security Reader como rol mínimo.
- [Data Security Index 2026: Unifying Data Protection and AI Innovation (informe PDF)](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/security/Data-Security-Index-Unifying-Data-Protection.pdf) · Documentación · Oficial · Microsoft (estudio de Hypothesis Group) · Microsoft · ene 2026. Informe completo de la encuesta a más de 1.700 profesionales de seguridad de datos en 10 mercados sobre consolidación de herramientas, IA generativa y DSPM.
- [Manage pay-as-you-go and per-user licensing usage (Usage center)](https://learn.microsoft.com/en-us/purview/purview-billing-usage) · Documentación · Oficial · Vista previa · Microsoft Learn · 19 nov 2025. Explica el Usage center de Purview para ver consumo PAYG por función (incluida la protección en tránsito hacia apps de IA y en la capa de red) y detectar usuarios en alcance sin licencia. *Nota:* Usage center en preview

### Anuncios y blogs oficiales

- [New Microsoft Data Security Index report explores secure AI adoption to protect sensitive data](https://www.microsoft.com/en-us/security/blog/2026/01/29/new-microsoft-data-security-index-report-explores-secure-ai-adoption-to-protect-sensitive-data/) · Blog oficial · Oficial · Herain Oberoi · Microsoft Security Blog · 29 ene 2026. Resume el Data Security Index 2026: 32% de los incidentes de datos involucran IA generativa, solo 47% aplica controles específicos de IA y más del 80% implementa o desarrolla estrategias de DSPM.

**Manos a la obra**

1. `Laboratorio` Tablero: construye el tablero mensual con las métricas de la tabla de este módulo, indicando fuente, frecuencia y responsable. Evidencia: tablero publicado.
2. `Laboratorio parcial` Mide en el laboratorio el porcentaje de activos sensibles protegidos por DLP, los sitios sobrecompartidos y el consumo de pago por uso, y repite la medición a los 30 días ([paso 3 del modelo de despliegue](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-dspm-step3)). Limitación: el volumen sintético no refleja tu organización. Evidencia: dos mediciones comparadas.
3. `Solo producción` Primer informe al comité: con datos de producción en solo lectura, presenta la tendencia de 30 días, los cinco riesgos principales y las decisiones que necesitas. Cómo hacerlo seguro: datos agregados y sin nombres de personas salvo aprobación de privacidad. Evidencia: presentación y acta.

<a id="o3"></a>

## O3 · Gobierno, privacidad y cumplimiento normativo en MCSA

*L300–L400 · ~4 h · Origen: Nuevo en esta edición*

Los prompts y las respuestas pueden contener datos personales, y una directiva de colección con captura de contenido los almacena. Eso activa obligaciones de privacidad. Purview trae piezas de **privacidad por diseño**: Insider Risk para agentes y Communication Compliance seudonimizan a los usuarios por defecto y se apoyan en RBAC y auditoría, y las directivas de colección filtran eventos por región. Microsoft se compromete a que Copilot no use los prompts ni los datos de Graph para entrenar modelos fundacionales, y lista a Anthropic y OpenAI como subprocesadores.

Las **solicitudes de los titulares** (derechos ARCO o de supresión) y los derrames de datos en la IA tienen un procedimiento oficial. Los prompts y respuestas se guardan en el buzón del usuario: se buscan con eDiscovery (grupo eDiscovery Manager) y se eliminan con Graph Explorer (rol Search And Purge). El límite es de 10 elementos por buzón por ejecución, y hay que retirar y luego reaplicar las retenciones y los holds.

En MCSA, el **Perú** reglamentó su Ley 31814 de IA con el D.S. 115-2025-PCM, y **Colombia** aplica la Ley 1581 de 2012 a la IA mediante la Circular Externa 002 de 2024 de la SIC. A eso se suman leyes de protección de datos con plazos de notificación de incidentes en casi todos los países; la hoja «Normativa MCSA» del libro de Excel las reúne. Esta guía **no es asesoría legal**: resume fuentes oficiales para que Legal, privacidad y RR. HH. decidan cómo aplican.

**Por qué importa**

En MCSA, los programas de IA suelen frenarse por confianza más que por tecnología: trabajadores, reguladores y clientes preguntan qué pasa con los prompts. Con una finalidad documentada, captura mínima, seudonimización, retención acotada y un procedimiento probado de derechos de los titulares, Purview se vuelve evidencia de responsabilidad demostrada. Sin esas piezas, la misma herramienta se percibe como vigilancia.

**Qué vas a lograr**

- Identificar qué capacidades de Purview capturan datos personales en las interacciones de IA y cómo minimizarlos.
- Diseñar el procedimiento de solicitudes de derechos sobre interacciones de IA con eDiscovery y Graph Explorer.
- Mapear normas de IA y de protección de datos de MCSA a evidencias técnicas, sin interpretarlas.
- Acordar con Legal, privacidad y RR. HH. las aprobaciones para capturar contenido y monitorear el uso de IA.

> **Atención.** Esta guía no es asesoría legal. El resumen regional es una referencia para conversar con Legal y privacidad, que deciden cómo aplica cada norma. La hoja «Normativa MCSA» del libro de Excel reúne normas de privacidad, ciberseguridad y sector financiero con sus fuentes oficiales.

> **Novedad.** Perú: el D.S. 115-2025-PCM aprobó el Reglamento de la Ley 31814 sobre IA y se publicó el 9 de septiembre de 2025, con 6 títulos, 36 artículos y 6 disposiciones complementarias finales ([gob.pe](https://www.gob.pe/institucion/pcm/normas-legales/7133522-115-2025-pcm)). Según el resumen de un estudio jurídico, entró en vigor el 22 de enero de 2026 y clasifica los usos de IA en uso indebido (prohibido), riesgo alto y riesgo aceptable ([Cuatrecasas](https://www.cuatrecasas.com/resources/que-establece-el-reglamento-de-la-ley-de-inteligencia-artificial-68c19ecd38db6505769013.pdf)). Colombia: la Circular Externa 002 de 2024 de la SIC aplica la Ley 1581 de 2012 al desarrollo, despliegue y uso de IA ([SIC](https://normograma.mintic.gov.co/mintic/compilacion/docs/circular_superindustria_0002_2024.htm)).

> **Consejo Ninja.** Derechos sobre interacciones de IA: los prompts y respuestas se guardan en el buzón del usuario. Se buscan con eDiscovery (grupo eDiscovery Manager) y se eliminan con Graph Explorer (rol Search And Purge), con un máximo de 10 elementos por buzón por ejecución y retirando y luego reaplicando retenciones y holds ([buscar y eliminar datos de IA](https://learn.microsoft.com/en-us/purview/edisc-search-copilot-data), [en español](https://learn.microsoft.com/es-es/purview/edisc-search-copilot-data)).

> **Consejo Ninja.** Privacidad por diseño: Insider Risk para agentes y Communication Compliance seudonimizan a los usuarios por defecto ([MC1280556](https://message.cengizyilmaz.net/message/mc1280556-microsoft-purview-for-agents-ai-observability-and-insider-risk-management-now-generally-available)), y las directivas de colección filtran eventos por región ([directivas de colección](https://learn.microsoft.com/en-us/purview/collection-policies-solution-overview)). Copilot no usa los prompts ni los datos de Graph para entrenar modelos fundacionales y lista a Anthropic y OpenAI como subprocesadores ([privacidad de Copilot](https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-privacy)).

**¿Tienes poco tiempo?**

- [Search for and delete AI application data in eDiscovery](https://learn.microsoft.com/en-us/purview/edisc-search-copilot-data) · Documentación
- [Data, Privacy, and Security for Microsoft Copilot](https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-privacy) · Documentación
- [Collection Policies solution overview](https://learn.microsoft.com/en-us/purview/collection-policies-solution-overview) · Documentación
- [Decreto Supremo N.° 115-2025-PCM – Reglamento de la Ley N.° 31814 (inteligencia artificial, Perú)](https://www.gob.pe/institucion/pcm/normas-legales/7133522-115-2025-pcm) · Documentación

**Normas de IA y datos personales en MCSA: evidencias técnicas que Purview puede aportar**

| País | Norma | Qué destaca la fuente | Evidencias de Purview para que Legal evalúe | Fuente |
|---|---|---|---|---|
| Perú | Ley 31814 y su Reglamento (D.S. 115-2025-PCM, publicado el 9 de septiembre de 2025) | Enfoque basado en riesgos: uso indebido (prohibido), riesgo alto y riesgo aceptable; políticas y capacitación para el sector privado; transparencia algorítmica, registros y supervisión humana para el riesgo alto (resumen de Cuatrecasas) | Inventario de IA (AI observability), registros de interacciones (Audit), aprobación humana de acciones de agentes e Insider Risk para agentes | [gob.pe](https://www.gob.pe/institucion/pcm/normas-legales/7133522-115-2025-pcm) · [Cuatrecasas](https://www.cuatrecasas.com/resources/que-establece-el-reglamento-de-la-ley-de-inteligencia-artificial-68c19ecd38db6505769013.pdf) |
| Perú | Ley 29733 y su Reglamento (D.S. 016-2024-JUS, vigente desde el 31 de marzo de 2025) | Refuerza la seguridad, introduce el oficial de datos personales para ciertas organizaciones y obliga a notificar incidentes | Audit y DSI para reconstruir incidentes; DLP para Copilot como control preventivo | [Reglamento](https://cdn.www.gob.pe/uploads/document/file/7756037/6554453-reglamento-de-la-ley-n-29733.pdf?v=1741726731) |
| Colombia | Circular Externa 002 de 2024 de la SIC (21 de agosto de 2024) | Aplica la Ley 1581 de 2012 al desarrollo, despliegue y uso de IA, con responsabilidad demostrada y privacidad desde el diseño | Evaluaciones de riesgo de datos, auditoría de interacciones, DLP para Copilot y directivas de colección acotadas | [SIC](https://normograma.mintic.gov.co/mintic/compilacion/docs/circular_superindustria_0002_2024.htm) |
| Colombia | Ley 1581 de 2012 y Decreto 1377 de 2013 | Autorización del titular, políticas de tratamiento, registro de bases de datos y reporte de incidentes a la SIC (15 días hábiles según la hoja Normativa MCSA) | eDiscovery y Graph Explorer para solicitudes de titulares; DSI y Audit para incidentes | [Ley 1581](http://www.secretariasenado.gov.co/senado/basedoc/ley_1581_2012.html) |
| México | Nueva LFPDPPP (DOF 20 de marzo de 2025) | Aviso de privacidad, medidas de seguridad proporcionales al riesgo y aviso inmediato al titular ante vulneraciones que afecten de forma significativa sus derechos (art. 19) | Evaluaciones de riesgo de datos y DLP como medidas técnicas; Audit y DSI para documentar vulneraciones | [LFPDPPP](https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPDPPP.pdf) |
| Chile | Ley 21.719 (vigente desde el 1 de diciembre de 2026) | Reforma integral tipo RGPD: bases de licitud, derechos, modelo de prevención de infracciones y deber de reportar vulneraciones a la Agencia | Procedimiento de derechos sobre interacciones de IA, seudonimización y evaluación de impacto de la captura de prompts | [Ley 21.719](https://www.leychile.cl/leychile/Navegar?idNorma=1209272&idParte=1) |
| Ecuador | LOPDP, su Reglamento y la norma técnica de notificación (septiembre de 2026) | Deberes de seguridad, evaluaciones de impacto y notificación de vulneraciones a la SPDP en 5 días | Evaluación de impacto de la captura de prompts; Audit y DSI para la notificación | [LOPDP](https://www.gob.ec/sites/default/files/regulations/2025-01/01%20Ley%20Org%C3%A1nica%20de%20Protecci%C3%B3n%20de%20Datos%20Personales.pdf) |
| Panamá | Ley 81 de 2019 y Decreto Ejecutivo 285 de 2021 | Derechos ARCO, deber de seguridad y notificación de incidentes en 72 horas | Procedimiento de derechos con eDiscovery; Audit para el registro de vulneraciones | [Reglamentación](https://antai.gob.pa/wp-content/uploads/2021/05/Reglamentacio%CC%81n-de-Ley-81-de-Proteccio%CC%81n-de-Datos-Personales.pdf) |
| Uruguay | Ley 18.331, Ley 19.670 y Decreto 64/020 | Responsabilidad proactiva, delegado de protección de datos para ciertos responsables, evaluaciones de impacto y notificación a la URCDP en 72 horas | Evidencias de DSPM como responsabilidad proactiva; evaluación de impacto de la captura | [Decreto 64/020](https://www.impo.com.uy/bases/decretos/64-2020/4) |
| Paraguay | Ley 7593/2025 (plena vigencia prevista para fines de noviembre de 2027) | Bases de licitud, oficial de protección de datos, evaluaciones de impacto y notificación de incidentes en 72 horas | Inventario de IA, evaluaciones de riesgo de datos y procedimiento de derechos preparados con anticipación | [Ley 7593/2025](https://www.bacn.gov.py/leyes-paraguayas/12924/ley-n-75932025--de-proteccin-de-datos-personales-en-la-repblica-del-paraguay) |
| Argentina | Ley 25.326 y Resolución AAIP 47/2018 | Principios de calidad, consentimiento, confidencialidad y seguridad; medidas de seguridad recomendadas y gestión documentada de incidentes, sin plazo legal específico de notificación | DLP, etiquetas y Audit como medidas de seguridad documentadas | [Ley 25.326](https://www.argentina.gob.ar/normativa/nacional/norma-64790/actualizacion) · [Res. AAIP 47/2018](https://www.argentina.gob.ar/normativa/nacional/norma-312662/texto) |
| Costa Rica | Ley 8968 y su Reglamento | Consentimiento informado, medidas de seguridad y aviso al titular de las vulneraciones en 5 días hábiles | Procedimiento de derechos e investigación con Audit y DSI | [Ley 8968](http://pgrweb.go.cr/TextoCompleto/NORMAS/1/VIGENTE/D/2010-2019/2010-2014/2012/12270/74352_115361-3.html) |
| El Salvador | Ley para la Protección de Datos Personales (Decreto Legislativo 144) | Principios de tratamiento, medidas de seguridad y notificación de vulneraciones en 72 horas a la Agencia de Ciberseguridad del Estado, la Fiscalía y los titulares | Audit y DSI para documentar; DLP como control preventivo | [Decreto 144](https://www.asamblea.gob.sv/sites/default/files/documents/decretos/F6986BF6-25C7-428B-9B74-325A6760AC2C.pdf) |

Resumen de la hoja «Normativa MCSA» y de la investigación de este programa, sin interpretación jurídica: las obligaciones, los plazos y su aplicación a tu organización los define tu área de Legal con el texto oficial vigente.

### Documentación, cursos y credenciales

- [Data, Privacy, and Security for Microsoft Copilot](https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-privacy) · Documentación · Oficial · Microsoft Learn. Compromisos de privacidad de Copilot: no entrena modelos fundacionales con prompts ni datos de Graph, respeta permisos, residencia de datos, EU Data Boundary y modelos de Anthropic y OpenAI como subprocesadores.
- [Search for and delete AI application data in eDiscovery](https://learn.microsoft.com/en-us/purview/edisc-search-copilot-data) · Documentación · Oficial · Microsoft Learn. Flujo oficial de siete pasos para localizar con eDiscovery y eliminar con Graph Explorer prompts y respuestas de Copilot y otras apps de IA, útil para atender solicitudes de supresión de titulares y derrames de datos.
- [Microsoft Purview Compliance Manager regulations list](https://learn.microsoft.com/en-us/purview/compliance-manager-regulations-list) · Documentación · Oficial · Microsoft Learn. Lista de plantillas regulatorias de Compliance Manager, con secciones de Latinoamérica y Sudamérica y plantillas premium de IA (EU AI Act, ISO/IEC 23894, ISO/IEC 42001, NIST AI RMF); E5 permite usar tres plantillas premium sin costo.
- [Decreto Supremo N.° 115-2025-PCM – Reglamento de la Ley N.° 31814 (inteligencia artificial, Perú)](https://www.gob.pe/institucion/pcm/normas-legales/7133522-115-2025-pcm) · Documentación · Comunidad · ES · Presidencia del Consejo de Ministros del Perú · Presidencia del Consejo de Ministros (gob.pe) · 9 sep 2025. Reglamento peruano de la Ley 31814 que define principios, una clasificación de riesgo de sistemas de IA y obligaciones de gobierno, transparencia, registro y supervisión humana para entidades públicas y privadas.
- [Circular Externa 002 de 2024 SIC – Lineamientos sobre el tratamiento de datos personales en sistemas de inteligencia artificial (Colombia)](https://normograma.mintic.gov.co/mintic/compilacion/docs/circular_superindustria_0002_2024.htm) · Documentación · Comunidad · ES · Superintendencia de Industria y Comercio · MinTIC – Compilación Jurídica (texto de la SIC) · 21 ago 2024. Lineamientos de la autoridad colombiana de protección de datos que aplican la Ley 1581 de 2012 al desarrollo, despliegue y uso de sistemas de IA, con responsabilidad demostrada y privacidad desde el diseño.

**Manos a la obra**

1. `Laboratorio parcial` Buscar y eliminar datos de IA: genera interacciones de Copilot Chat con una cuenta de prueba, crea un caso de eDiscovery, busca con la condición de actividad de Copilot y elimina hasta 10 elementos con Graph Explorer ([buscar y eliminar datos de IA](https://learn.microsoft.com/en-us/purview/edisc-search-copilot-data)). Limitación: la búsqueda Premium de interacciones de Copilot requiere E5 + Copilot. Evidencia: búsqueda antes y después y registro de la eliminación.
2. `Laboratorio parcial` Directiva de colección con privacidad por diseño: crea una directiva sin captura de contenido para un grupo piloto y documenta la finalidad, la región y la retención; luego evalúa si se justifica capturar contenido ([crear directivas de colección](https://learn.microsoft.com/en-us/purview/collection-policies-create-deploy-policy)). Limitación: la IA de terceros requiere pago por uso. Evidencia: ficha del tratamiento.
3. `Laboratorio` Mapa normativo: con la hoja «Normativa MCSA» y la tabla de este módulo arma, para tu país, una matriz de requisitos y evidencias de Purview y marca qué debe validar Legal. Evidencia: matriz revisada por Legal.
4. `Solo producción` Procedimiento de derechos sobre interacciones de IA: con Legal y el oficial de privacidad, pruébalo con una cuenta de prueba en producción, registra la solicitud y reaplica las retenciones y los holds al terminar. Cómo hacerlo seguro: aprobación previa, registro de la solicitud y cuentas de prueba. Evidencia: procedimiento aprobado y registro.
5. `Solo producción` Evaluación de impacto para capturar prompts: antes de activar la captura de contenido en producción, prepara con privacidad la evaluación de impacto (finalidad, minimización, retención, acceso con AI Content Viewer y seudonimización). Cómo hacerlo seguro: sin captura hasta la aprobación y con retención acotada. Evidencia: evaluación aprobada.

<a id="reto-operacion"></a>

## Reto del nivel

**Programa de preparación de datos para IA ante el comité.** Adapta la tabla [Plan de preparación de datos para Copilot y agentes](00_Programa.md#preparacion-ia) a tu organización y preséntala como ante el comité de IA: RACI, tablero mensual con su línea base, decisión de licencias (E5 frente a E7 o Agent 365, más pago por uso), salvaguardas de privacidad validadas con Legal y el oficial de privacidad (captura de contenido, seudonimización y procedimiento de derechos sobre interacciones de IA) y hoja de ruta de 90 días. Formato: diez minutos de exposición y una página de resumen ejecutivo.

<a id="quiz-operacion"></a>

## Evaluación del nivel

Responde y compara con [Evaluaciones y respuestas](06_Evaluaciones_y_respuestas.md#eval-operacion). Con 80 % o más, ¡nivel aprobado! (En la versión web puedes corregir en línea y generar tu certificado).

1. ¿Qué propone el modelo de despliegue oficial de DSPM?
   - a) Cuatro pasos y un ciclo mensual de revisión de recomendaciones
   - b) Dos pasos y una revisión anual
   - c) Seis pasos y una revisión semanal obligatoria
   - d) Un único paso de activación sin ciclo de revisión

2. ¿Cómo se tratan las acciones de los agentes en DSPM?
   - a) Se ejecutan sin registro para no generar ruido
   - b) Solo se auditan si fallan
   - c) Se revisan, aprueban y siempre se auditan
   - d) Solo se registran con Microsoft 365 E7

3. ¿Qué ofrece FastTrack para Agent 365?
   - a) Licencias gratuitas de Agent 365
   - b) Asistencia remota para inventario de agentes, identidad, controles base en Entra, Defender y Purview, y flujos de monitoreo y respuesta
   - c) Asesoría legal sobre normativa de IA
   - d) Soporte de producción 24×7 para incidentes

4. Según el Data Security Index 2026, ¿qué porcentaje de los incidentes de datos involucra IA generativa?
   - a) 12 %
   - b) 47 %
   - c) 80 %
   - d) 32 %

5. ¿Qué período cubre la tendencia de la página Posture de DSPM?
   - a) 7 días
   - b) 30 días
   - c) 90 días
   - d) 1 año

6. ¿Qué muestra el Usage center de Purview y en qué estado está?
   - a) El consumo de pago por uso por función y los usuarios en alcance sin licencia; está en preview
   - b) Solo las SCU de Security Copilot; está en GA
   - c) La puntuación de Secure Score; fue retirado
   - d) El inventario de agentes; requiere Agent 365

7. Al eliminar prompts y respuestas con eDiscovery y Graph Explorer, ¿cuál es el límite por ejecución?
   - a) 100 elementos por buzón
   - b) 10 elementos por buzón
   - c) 1.000 elementos por buzón
   - d) Sin límite

8. ¿Qué permisos se necesitan para buscar y para eliminar interacciones de IA?
   - a) Global Administrator para ambas tareas
   - b) AI Content Viewer para ambas tareas
   - c) Compliance Administrator para buscar y Data Security AI Viewer para eliminar
   - d) El grupo eDiscovery Manager para buscar y el rol Search And Purge para eliminar

9. ¿Cuándo se publicó el D.S. 115-2025-PCM, Reglamento de la Ley 31814 de IA del Perú?
   - a) 21 de agosto de 2024
   - b) 9 de septiembre de 2025
   - c) 22 de enero de 2026
   - d) 1 de diciembre de 2026

10. ¿Qué hace la Circular Externa 002 de 2024 de la SIC de Colombia?
   - a) Aplica la Ley 1581 de 2012 al desarrollo, despliegue y uso de sistemas de IA
   - b) Regula la ciberseguridad de los bancos
   - c) Crea una autoridad nacional de IA
   - d) Fija la retención de los correos electrónicos

11. ¿Qué soluciones de Purview seudonimizan a los usuarios por defecto en el contexto de IA?
   - a) DLP y Audit
   - b) eDiscovery y retención
   - c) Insider Risk para agentes y Communication Compliance
   - d) Restricted Content Discovery

12. Al eliminar interacciones de IA de un buzón sujeto a retención, ¿qué debes hacer?
   - a) Nada especial
   - b) Eliminar el buzón completo
   - c) Retirar y luego reaplicar las retenciones y los holds
   - d) Desactivar la auditoría del inquilino

13. ¿Qué compromiso de privacidad documenta Microsoft para Copilot?
   - a) Usa los prompts para entrenar los modelos fundacionales
   - b) Solo procesa datos en Estados Unidos
   - c) Requiere consentimiento individual para cada prompt
   - d) No usa los prompts ni los datos de Graph para entrenar modelos fundacionales

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. No constituye asesoría legal ni laboral: las decisiones sobre privacidad, captura de contenido, monitoreo y normativa corresponden a tus áreas de Legal, RR. HH. y privacidad. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

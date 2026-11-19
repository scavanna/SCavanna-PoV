# Nivel 4 · Operación · Programa, métricas y gobierno

*Microsoft Purview Information Protection Ninja Training: clasificación, etiquetado y cifrado · Edición 2026*

[← Nivel 3 · Avanzado](03_Nivel_3_Avanzado.md) · [Índice del programa](README.md) · [Comunidad →](05_Comunidad.md)

<a id="operacion"></a>

Modelo operativo y adopción, métricas y mejora continua, y gobierno con Legal y Privacidad frente a la normativa de MCSA. Terminas con un programa de protección de la información que puedes defender ante un comité o una auditoría.

*L300–L400 · 3 módulos · ~11 horas · 15 recursos*

**Módulos de este nivel:** [O1 Modelo operativo y adopción](#o1) · [O2 Métricas y mejora continua](#o2) · [O3 Gobierno y normativa MCSA](#o3)

<a id="o1"></a>

## O1 · Modelo operativo, responsabilidades y adopción

*L300–L400 · ~4 h · Origen: Nuevo en esta edición (modelo de despliegue secure by default de Microsoft)*

Information Protection es un programa, no un proyecto. Necesita **dueños de datos** en las áreas de negocio que decidan qué es sensible, un **equipo de protección de la información** que configure, **administradores de Exchange, SharePoint y Teams** que operen contenedores y bibliotecas, un **SOC** que vigile los eventos de etiquetas, un área de **cumplimiento** que aporte el marco regulatorio junto con Legal y Privacidad, y un **líder de adopción** que logre que las personas entiendan y usen las etiquetas. La guía de despliegue de Microsoft organiza el trabajo en conocer, proteger y prevenir, y recomienda arrancar desde DSPM con las etiquetas y políticas predeterminadas.

El modelo **secure by default** del equipo de ingeniería propone cuatro pasos: empezar con etiquetado predeterminado (por ejemplo, Confidencial/Todos los empleados), atender primero los archivos más sensibles con etiquetas de sitio y de biblioteca, extender la protección a todo el patrimonio con auto-etiquetado y operar con acciones retroactivas. Su idea central es enseñar a las personas a gestionar excepciones en lugar de decidir cuándo proteger.

La gestión del cambio completa el modelo: un proceso formal para crear, modificar o retirar etiquetas, campeones por área, guiones para la mesa de ayuda, comunicación antes de cada oleada y un circuito de retroalimentación que alimente la mejora continua del módulo O2.

**Por qué importa**

La mayoría de los programas de Information Protection se estancan por razones que no son técnicas: nadie es dueño de la taxonomía, las excepciones se acumulan en la mesa de ayuda y las áreas ven las etiquetas como burocracia de TI. Un RACI claro, un proceso de cambios con piloto y reversión y un plan de adopción con campeones aceleran la cobertura, reducen las bajadas justificadas y mantienen el programa alineado con el riesgo del negocio.

**Qué vas a lograr**

- Definir un RACI entre protección de la información, dueños de datos, cumplimiento, administradores de colaboración, SOC y adopción.
- Aplicar los cuatro pasos del modelo secure by default a un plan de despliegue por fases.
- Diseñar un proceso de cambios para la taxonomía y las políticas con piloto y reversión.
- Construir un plan de adopción con comunicación, capacitación y campeones.

> **Consejo Ninja.** El modelo secure by default propone proteger por defecto (por ejemplo, Confidencial/Todos los empleados), derivar las etiquetas de los archivos desde los sitios y enseñar a las personas a gestionar excepciones en lugar de decidir cuándo proteger ([introducción](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-secure-by-default-intro), [paso 1](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-secure-by-default-step1)).

> **Consejo Ninja.** Prioriza los sitios críticos con etiqueta de sitio y etiqueta predeterminada de biblioteca, auto-etiqueta todas las credenciales como Altamente confidencial y usa DLP para el contenido sin etiqueta ([paso 2](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-secure-by-default-step2)).

> **Atención.** La guía de despliegue recomienda arrancar desde DSPM con las etiquetas y políticas predeterminadas y exigir justificación para bajar una etiqueta ([desplegar Information Protection](https://learn.microsoft.com/en-us/purview/information-protection-solution)). Cualquier cambio de etiquetas tarda hasta 24 horas en propagarse: planifica ventanas y comunicación antes de cada oleada.

> **Consejo Ninja.** Para la adopción, una guía en español recomienda pocas etiquetas con fronteras claras, separar clasificación, protección y retención y pilotar con documentos reales ([guía de adopción](https://msadvance.com/sensitivity-labels-purview-clasificar-documentos/)).

**¿Tienes poco tiempo?**

- [Deploy an information protection solution with Microsoft Purview](https://learn.microsoft.com/en-us/purview/information-protection-solution) · Documentación
- [Introduction to secure by default with Microsoft Purview](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-secure-by-default-intro) · Documentación
- [Step 1: Start with default labeling - Secure by default with Microsoft Purview](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-secure-by-default-step1) · Documentación

### Documentación, cursos y credenciales

- [Deploy an information protection solution with Microsoft Purview](https://learn.microsoft.com/en-us/purview/information-protection-solution) · Documentación · Oficial · Microsoft Learn. Guía de despliegue por fases (conocer, proteger, prevenir) con taxonomía de ejemplo, política de etiquetas por defecto y recomendación de usar DSPM para arrancar con etiquetas y políticas predeterminadas.
- [Introduction to secure by default with Microsoft Purview](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-secure-by-default-intro) · Documentación · Oficial · Microsoft Learn - Purview deployment models. Modelo de despliegue 'secure by default' del equipo de ingeniería: proteger por defecto (p. ej., Confidential\All Employees), derivar etiquetas de archivos desde sitios y enseñar a los usuarios a gestionar excepciones en lugar de cuándo proteger.
- [Step 1: Start with default labeling - Secure by default with Microsoft Purview](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-secure-by-default-step1) · Documentación · Oficial · Microsoft Learn - Purview deployment models. Taxonomía recomendada (Public, General, Confidential y Highly Confidential con subetiquetas All Employees, Specific People e Internal exception) y su configuración de cifrado, marcas y DLP.
- [Data classification and sensitivity label taxonomy (Microsoft Service Assurance)](https://learn.microsoft.com/en-us/compliance/assurance/assurance-data-classification-and-labels) · Documentación · Oficial · Microsoft Learn - Service Assurance. Guía para diseñar un marco de clasificación con 3-5 niveles, nombres autoexplicativos y controles por nivel, recomendando no más de 5 etiquetas principales con 5 subetiquetas.
- [Step 2: Address files with the highest sensitivity - Secure by default with Microsoft Purview](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-secure-by-default-step2) · Documentación · Oficial · Microsoft Learn - Purview deployment models. Prioriza sitios críticos con etiqueta de sitio y etiqueta predeterminada de biblioteca, auto-etiquetado de credenciales, DLP para contenido no etiquetado y Adaptive Protection.

**Manos a la obra**

1. `Laboratorio` Redacta el RACI del programa con al menos ocho actividades (taxonomía, publicación, auto-etiquetado, cifrado y superusuario, contenedores, alertas del SOC, excepciones y métricas) y los seis roles de esta guía; valídalo con un dueño de datos.
2. `Laboratorio` Aplica los cuatro pasos del modelo secure by default a tu organización: qué haces en cada paso, con qué licencia y en qué semana ([paso 1](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-secure-by-default-step1), [paso 4](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-secure-by-default-step4)).
3. `Laboratorio` Diseña el proceso de cambios de etiquetas: solicitud, evaluación de impacto (cifrado, Copilot y contenedores), aprobación, piloto, comunicación y reversión; incluye la regla de no eliminar nunca una etiqueta que cifra.
4. `Laboratorio` Arma el kit de adopción: mensaje del patrocinador, guía de una página por etiqueta con ejemplos del área, guion para la mesa de ayuda y encuesta de comprensión a los 30 días.
5. `Solo producción` Programa de campeones: recluta un campeón por área, dale acceso anticipado a la política piloto y recoge sus casos de excepción durante dos semanas. Forma segura: piloto acotado con voluntarios informados, sin cifrado en la primera oleada y retroalimentación registrada antes de ampliar.

<a id="o2"></a>

## O2 · Métricas, reportes y mejora continua

*L300–L400 · ~4 h · Origen: Nuevo en esta edición*

Lo que no se mide no mejora. Un programa de Information Protection necesita pocos indicadores ligados al riesgo: cobertura de etiquetado por carga de trabajo y por sitio, origen de las etiquetas (manual, predeterminada o automática), bajadas y eliminaciones con justificación, tasa de fallas del auto-etiquetado, cobertura de contenedores, uso del superusuario y adopción. Las fuentes son los **informes de postura** (vista previa, ventana móvil de 30 días), la pestaña **Insights** del auto-etiquetado, el **explorador de actividades**, el **explorador de contenido** y, fuera de Microsoft 365, el informe clásico de etiquetas de Unified Catalog.

Como casi todas esas vistas cubren 30 días, las series históricas se construyen exportando: `Export-ActivityExplorerData` y `Export-ContentExplorerData`, programados a diario hacia un almacén propio o Power BI. El paso 4 del modelo secure by default agrega rutinas operativas —revisar sitios sin etiqueta, detectar desalineaciones entre la etiqueta del sitio y la de la biblioteca con Graph y vigilar etiquetas sin protección— que convierten las métricas en acciones.

La mejora continua cierra el ciclo con una revisión mensual de indicadores, una revisión trimestral de la taxonomía y de los SIT y el retiro ordenado de lo que no se usa.

**Por qué importa**

Sin métricas, el programa no puede demostrar valor ni encontrar dónde falla. Un conjunto pequeño de indicadores ligados al riesgo —cobertura de sitios sensibles, bajadas de etiqueta, auto-etiquetado fallido— permite decidir dónde invertir, muestra a los reguladores un control continuo y detecta desvíos, como un sitio cuyo propietario quitó la etiqueta de contenedor, antes de que se conviertan en incidentes.

**Qué vas a lograr**

- Definir indicadores de cobertura, calidad, adopción y riesgo con fuente, frecuencia y responsable.
- Construir series históricas exportando datos más allá de la ventana de 30 días.
- Usar los informes de postura, la pestaña Insights y el informe de etiquetas de Unified Catalog.
- Instalar rutinas mensuales y trimestrales de mejora continua.

> **Atención.** Los informes de postura de Information Protection (distribución y adopción de etiquetas, cobertura de auto-etiquetado y actividad) y los informes personalizados están en vista previa y usan una ventana móvil de 30 días: guarda en PDF lo que quieras conservar ([informes](https://learn.microsoft.com/en-us/purview/purview-reports)).

> **Consejo Ninja.** Para tendencias, programa exportaciones diarias del explorador de actividades —eventos como LabelApplied, LabelChanged, LabelRemoved, AutoLabelingSimulation o CopilotInteraction— hacia un almacén propio o Power BI ([Export-ActivityExplorerData](https://learn.microsoft.com/en-us/powershell/module/exchangepowershell/export-activityexplorerdata?view=exchange-ps)), y del explorador de contenido por etiqueta, SIT y carga de trabajo para medir la cobertura por sitio o buzón ([Export-ContentExplorerData](https://learn.microsoft.com/en-us/powershell/module/exchangepowershell/export-contentexplorerdata?view=exchange-ps)). El parámetro -Aggregate está en vista previa privada.

> **Consejo Ninja.** Rutinas del paso 4 de secure by default: revisar sitios sin etiqueta y desalineaciones entre la etiqueta del sitio y la de la biblioteca con Graph, DLP para etiquetas sin protección y seguimiento de usuarios de riesgo con Insider Risk ([paso 4](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-secure-by-default-step4)). Fuera de Microsoft 365, el informe clásico de etiquetas de Unified Catalog solo muestra datos si extendiste las etiquetas al Data Map ([informe](https://learn.microsoft.com/en-us/purview/unified-catalog-reports-classic-sensitivity-labels)).

**¿Tienes poco tiempo?**

- [Microsoft Purview posture reports overview](https://learn.microsoft.com/en-us/purview/purview-reports) · Documentación
- [Step 4: Operate, expand, and retroactive actions - Secure by default with Microsoft Purview](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-secure-by-default-step4) · Documentación
- [Export-ContentExplorerData (ExchangePowerShell)](https://learn.microsoft.com/en-us/powershell/module/exchangepowershell/export-contentexplorerdata?view=exchange-ps) · Documentación

**Indicadores sugeridos para el programa de Information Protection**

| Indicador | Cómo se calcula | Fuente de datos | Frecuencia | Decisión que habilita |
|---|---|---|---|---|
| Cobertura de etiquetado por carga de trabajo | Elementos con etiqueta sobre elementos con SIT detectados, en Exchange, SharePoint, OneDrive y Teams | Export-ContentExplorerData o Data explorer | Mensual | Dónde invertir en auto-etiquetado |
| Cobertura de contenedores | Equipos y sitios con etiqueta de contenedor, y sitios sensibles con etiqueta predeterminada de biblioteca | PowerShell y Microsoft Graph | Mensual | Reducir la sobreexposición antes de ampliar Copilot |
| Origen de las etiquetas | Porcentaje de etiquetas manuales, predeterminadas y automáticas | Export-ActivityExplorerData | Mensual | Madurez de la automatización |
| Bajadas y eliminaciones con justificación | Eventos por cada 1.000 personas y las diez justificaciones más frecuentes | Explorador de actividades o tabla MicrosoftPurviewInformationProtection | Semanal | Ajustar la taxonomía o detectar abuso |
| Fallas del auto-etiquetado | Archivos fallidos sobre etiquetados y las tres causas principales | Pestaña Insights | Semanal durante cada oleada | Corregir antes de ampliar el alcance |
| Precisión de la simulación | Coincidencias correctas sobre una muestra revisada con el dueño de los datos | Revisión de muestras de la simulación | Por política | Activar, ajustar o descartar la política |
| Etiquetas cifrantes compatibles con los servicios | Etiquetas que conceden VIEW y EXTRACT a las personas previstas sobre el total de etiquetas cifrantes | Inventario de etiquetas con PowerShell | Trimestral | Evitar sorpresas con Copilot, búsqueda y eDiscovery |
| Hallazgos del escáner | Archivos con SIT descubiertos y etiquetados por repositorio | Informes del escáner y explorador de actividades | Por ciclo de escaneo | Priorizar repositorios locales |
| Uso del superusuario | Activaciones y accesos registrados | Get-AipServiceAdminLog | Mensual | Control del acceso privilegiado |
| Adopción | Personas que aplicaron al menos una etiqueta en 30 días y resultado de la encuesta de comprensión | Explorador de actividades y encuesta | Mensual | Reforzar la capacitación por área |
| Costo por uso | Consumo de Data Map y de la clasificación bajo demanda frente al presupuesto | Usage center de Purview y Azure Cost Management | Mensual | Ajustar el alcance de las políticas con pago por uso |

Fuentes: [informes de postura](https://learn.microsoft.com/en-us/purview/purview-reports), [Insights](https://learn.microsoft.com/en-us/purview/auto-label-insights-tab), [Export-ActivityExplorerData](https://learn.microsoft.com/en-us/powershell/module/exchangepowershell/export-activityexplorerdata?view=exchange-ps), [Export-ContentExplorerData](https://learn.microsoft.com/en-us/powershell/module/exchangepowershell/export-contentexplorerdata?view=exchange-ps), [paso 4 de secure by default](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-secure-by-default-step4) y [uso y licencias](https://learn.microsoft.com/en-us/purview/purview-billing-usage). Las metas numéricas dependen de cada organización y no se proponen aquí.

### Documentación, cursos y credenciales

- [Step 4: Operate, expand, and retroactive actions - Secure by default with Microsoft Purview](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-secure-by-default-step4) · Documentación · Oficial · Microsoft Learn - Purview deployment models. Rutinas operativas: revisar sitios sin etiqueta y desalineaciones sitio/biblioteca vía Graph, DLP para etiquetas sin protección, usuarios de riesgo con IRM y escenarios avanzados (multi-tenant, proyectos 'tented', 5x5 etiquetas).
- [Export-ActivityExplorerData (ExchangePowerShell)](https://learn.microsoft.com/en-us/powershell/module/exchangepowershell/export-activityexplorerdata?view=exchange-ps) · Documentación · Oficial · Microsoft Learn. Cmdlet de Security & Compliance PowerShell para exportar en JSON o CSV, con paginación por PageCookie, los eventos del explorador de actividades (LabelApplied, LabelChanged, LabelRemoved, AutoLabelingSimulation, CopilotInteraction, etc.) y construir series históricas de métricas de etiquetado más allá de la ventana de 30 días.
- [Use the Insights tab to analyze auto-labeling policies in Microsoft Purview](https://learn.microsoft.com/en-us/purview/auto-label-insights-tab) · Documentación · Oficial · Microsoft Learn. Explica la pestaña Insights de cada directiva de auto-etiquetado: resumen de simulación y, en modo de aplicación, métricas de 30 días (archivos etiquetados vs. fallidos, tres principales causas de falla, top 10 de SIT y desglose por SharePoint/OneDrive).
- [Microsoft Purview posture reports overview](https://learn.microsoft.com/en-us/purview/purview-reports) · Documentación · Oficial · Vista previa · Microsoft Learn. Describe los informes de postura de Information Protection (distribución y adopción de etiquetas, cobertura de auto-etiquetado y actividad de etiquetas) y sus roles de acceso, con ventana móvil de 30 días. *Nota:* Los informes de postura y los informes personalizados están en preview; exportar a PDF para conservar histórico de métricas
- [Classic Sensitivity Labels Report in Unified Catalog](https://learn.microsoft.com/en-us/purview/unified-catalog-reports-classic-sensitivity-labels) · Documentación · Oficial · Microsoft Learn. Describe el informe de etiquetas de confidencialidad del Unified Catalog (Health Management > Reports) con fuentes y archivos/tablas etiquetados, etiquetas principales y tendencia de 30 días para activos del Data Map (Azure, SQL, Amazon S3/RDS, Power BI).
- [Export-ContentExplorerData (ExchangePowerShell)](https://learn.microsoft.com/en-us/powershell/module/exchangepowershell/export-contentexplorerdata?view=exchange-ps) · Documentación · Oficial · Microsoft Learn. Cmdlet para exportar por etiqueta o SIT y por carga de trabajo (Exchange, SharePoint, OneDrive, Teams) los conteos y detalles del explorador de contenido, base para medir cobertura de etiquetado por sitio o buzón.

**Manos a la obra**

1. `Laboratorio` Exporta 30 días del explorador de actividades y los conteos por etiqueta del explorador de contenido a CSV y construye un tablero en Power BI o Excel con cobertura, origen de las etiquetas y bajadas ([actividades](https://learn.microsoft.com/en-us/powershell/module/exchangepowershell/export-activityexplorerdata?view=exchange-ps), [contenido](https://learn.microsoft.com/en-us/powershell/module/exchangepowershell/export-contentexplorerdata?view=exchange-ps)).
2. `Laboratorio` Define tus diez indicadores con la tabla de este módulo: fórmula, fuente, frecuencia, responsable y decisión que habilita; preséntalos en una página.
3. `Laboratorio` Guarda en PDF los informes de postura del mes y crea la carpeta de evidencias del programa, con fecha ([informes](https://learn.microsoft.com/en-us/purview/purview-reports)).
4. `Laboratorio parcial` Revisa la pestaña Insights de una política de auto-etiquetado activa y registra archivos etiquetados, fallidos y las tres causas principales de falla ([Insights](https://learn.microsoft.com/en-us/purview/auto-label-insights-tab)). Limitación: con poco volumen las métricas no son representativas; en producción, mídelas cada semana durante cada oleada.
5. `Solo producción` Revisión trimestral del programa: con tres meses de datos reales, identifica etiquetas sin uso, SIT con más falsos positivos y sitios sensibles sin etiqueta, y propone cambios al comité. Forma segura: análisis con roles de lectura, cambios por el proceso del módulo O1 y comunicación previa a los dueños de datos.

<a id="o3"></a>

## O3 · Gobierno, privacidad y cumplimiento normativo en MCSA

*L300–L400 · ~3 h · Origen: Nuevo en esta edición*

La clasificación y el etiquetado son la forma en que las leyes de datos personales se vuelven controles concretos: categorías de datos, medidas de seguridad proporcionales al riesgo, control de acceso y evidencia. En MCSA (México, Centroamérica y Sudamérica) el mapa normativo se está moviendo: en Chile, la Ley 21.719 entra en vigencia el 1 de diciembre de 2026 y crea la Agencia de Protección de Datos Personales; en México rige la nueva LFPDPPP publicada el 20 de marzo de 2025; en Perú, el nuevo reglamento de la Ley 29733 (Decreto Supremo 016-2024-JUS) se publicó el 30 de noviembre de 2024. El libro de Excel incluye la hoja «Normativa MCSA» con 45 normas de privacidad, ciberseguridad y sector financiero de la región.

Esta guía **no da asesoría legal**. El papel del equipo de Information Protection es traducir requisitos que Legal y Privacidad ya validaron en SIT, etiquetas, cifrado y evidencias, y documentar las decisiones. Las plantillas regulatorias de Compliance Manager ayudan a mapear controles (se profundizan en el programa de Compliance Manager de esta serie) y DKE apoya los requisitos de custodia o residencia de claves cuando una norma realmente los exige.

**Por qué importa**

Los reguladores de la región pasan de «tener una política» a «demostrar el control»: medidas de seguridad proporcionales, notificación de vulneraciones y agencias con poder sancionador. Vincular cada etiqueta y cada SIT con la categoría de dato que protege una ley da a Legal y al responsable de privacidad evidencia verificable, evita sobreproteger y romper procesos, y prepara a la organización para auditar sin improvisar.

**Qué vas a lograr**

- Identificar las normas de protección de datos de MCSA relevantes para clasificar y etiquetar, con su fuente oficial.
- Traducir categorías de datos validadas por Legal y Privacidad en SIT, etiquetas y controles.
- Usar plantillas de Compliance Manager para mapear controles de etiquetado y cifrado.
- Documentar con las áreas responsables las decisiones de custodia de claves y de privacidad.

> **Atención.** Esta guía no es asesoría legal. Las fechas y los requisitos se toman de fuentes oficiales y deben validarse con Legal, Privacidad y, cuando aplique, RR. HH. antes de decidir controles. La hoja «Normativa MCSA» del libro de Excel resume 45 normas de privacidad, ciberseguridad y sector financiero de la región.

> **Novedad.** Chile: la Ley 21.719, publicada el 13 de diciembre de 2024, entra en vigencia el 1 de diciembre de 2026 y crea la Agencia de Protección de Datos Personales ([Ley 21.719](https://www.leychile.cl/leychile/navegar?idNorma=1209272)). México: la nueva LFPDPPP se publicó en el DOF el 20 de marzo de 2025 y su última reforma es del 14 de noviembre de 2025 ([LFPDPPP](https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPDPPP.pdf?Sid=1)). Perú: el nuevo reglamento de la Ley 29733 (Decreto Supremo 016-2024-JUS) se publicó el 30 de noviembre de 2024 ([reglamento](https://www.gob.pe/institucion/anpd/normas-legales/6554453-n-016-2024-jus)).

> **Consejo Ninja.** Compliance Manager incluye plantillas regulatorias con secciones de América Latina y Sudamérica, y las licencias A5, E5 y G5 permiten usar tres regulaciones premium sin costo además de la línea base de Microsoft ([lista de regulaciones](https://learn.microsoft.com/es-es/purview/compliance-manager-regulations-list)). La plantilla de México se diseñó para la ley de 2010, por lo que conviene extenderla con los cambios de 2025; el tema se profundiza en el programa de Compliance Manager.

> **Consejo Ninja.** DKE apoya los requisitos de custodia y residencia de claves cuando una regulación los exige ([DKE](https://learn.microsoft.com/en-us/purview/double-key-encryption)); confirma con Legal que el requisito existe antes de asumir su costo funcional (módulo A3).

**¿Tienes poco tiempo?**

- [Lista de regulaciones del Administrador de cumplimiento de Microsoft Purview](https://learn.microsoft.com/es-es/purview/compliance-manager-regulations-list) · Documentación
- [Ley 21.719 - Regula la protección y el tratamiento de los datos personales y crea la Agencia de Protección de Datos Personales (Chile)](https://www.leychile.cl/leychile/navegar?idNorma=1209272) · Documentación
- [Ley Federal de Protección de Datos Personales en Posesión de los Particulares (México, nueva ley 2025)](https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPDPPP.pdf?Sid=1) · Documentación
- [Decreto Supremo N.° 016-2024-JUS - Reglamento de la Ley N.° 29733, Ley de Protección de Datos Personales (Perú)](https://www.gob.pe/institucion/anpd/normas-legales/6554453-n-016-2024-jus) · Documentación

**Normas de datos personales de MCSA: aspectos a considerar en la clasificación (referencia, no asesoría legal)**

| País | Norma y estado | Autoridad | Aspectos a considerar en el diseño (validar con Legal y Privacidad) | Fuente |
|---|---|---|---|---|
| México | Nueva LFPDPPP (DOF 20 de marzo de 2025) | Secretaría Anticorrupción y Buen Gobierno | Medidas de seguridad proporcionales al riesgo y control sobre quienes tratan los datos; la plantilla de Compliance Manager se diseñó para la ley de 2010 y conviene extenderla | [Texto vigente](https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPDPPP.pdf) |
| Colombia | Ley 1581 de 2012 y Decreto 1377 de 2013 | Superintendencia de Industria y Comercio | Autorización del titular, políticas de tratamiento, registro de bases de datos y reporte de incidentes a la autoridad | [Ley 1581](http://www.secretariasenado.gov.co/senado/basedoc/ley_1581_2012.html) |
| Perú | Ley 29733 y nuevo reglamento (Decreto Supremo 016-2024-JUS, vigente desde el 31 de marzo de 2025) | Autoridad Nacional de Protección de Datos Personales | Refuerza la seguridad, introduce el oficial de datos personales para ciertas organizaciones y obliga a notificar incidentes | [Reglamento](https://www.gob.pe/institucion/anpd/normas-legales/6554453-n-016-2024-jus) |
| Chile | Ley 21.719 (vigente desde el 1 de diciembre de 2026) | Agencia de Protección de Datos Personales | Reforma integral: bases de licitud, modelo de prevención de infracciones, sanciones elevadas y deber de reportar vulneraciones | [Ley 21.719](https://www.leychile.cl/leychile/navegar?idNorma=1209272) |
| Ecuador | LOPDP, reglamento y norma técnica de notificación de vulneraciones (septiembre de 2026) | Superintendencia de Protección de Datos Personales | Deberes de seguridad, evaluaciones de impacto y notificación de vulneraciones con plazos detallados | [LOPDP](https://www.gob.ec/sites/default/files/regulations/2025-01/01%20Ley%20Org%C3%A1nica%20de%20Protecci%C3%B3n%20de%20Datos%20Personales.pdf) |
| Argentina | Ley 25.326 y Resolución AAIP 47/2018 | Agencia de Acceso a la Información Pública | Confidencialidad, seguridad y registro de bases de datos; la resolución recomienda medidas de seguridad organizativas y técnicas | [Resolución 47/2018](https://www.argentina.gob.ar/normativa/nacional/norma-312662/texto) |
| Uruguay | Ley 18.331 y Decreto 64/020 | Unidad Reguladora y de Control de Datos Personales | Responsabilidad proactiva, delegado de protección de datos para ciertos responsables, evaluaciones de impacto y notificación de vulneraciones | [Decreto 64/020](https://www.impo.com.uy/bases/decretos/64-2020/4) |
| Costa Rica | Ley 8968 y su reglamento (reforma en trámite) | PRODHAB | Consentimiento informado, medidas de seguridad y gestión de vulneraciones | [Ley 8968](http://pgrweb.go.cr/TextoCompleto/NORMAS/1/VIGENTE/D/2010-2019/2010-2014/2012/12270/74352_115361-3.html) |
| Panamá | Ley 81 de 2019 y Decreto Ejecutivo 285 de 2021 | ANTAI | Deber de seguridad, derechos ARCO y registro y notificación de incidentes | [Reglamentación](https://antai.gob.pa/wp-content/uploads/2021/05/Reglamentacio%CC%81n-de-Ley-81-de-Proteccio%CC%81n-de-Datos-Personales.pdf) |
| Paraguay | Ley 7593/2025 (24 meses de adecuación; plena vigencia prevista a fines de noviembre de 2027) | Agencia Nacional de Protección de Datos Personales (en creación) | Bases de licitud, oficial de protección de datos, evaluaciones de impacto y notificación de incidentes | [Ley 7593/2025](https://www.bacn.gov.py/leyes-paraguayas/12924/ley-n-75932025--de-proteccin-de-datos-personales-en-la-repblica-del-paraguay) |

Resumen de la hoja «Normativa MCSA» del libro de Excel (45 normas de privacidad, ciberseguridad y sector financiero). Es una referencia para conversar con Legal y Privacidad, no una interpretación de la ley: confirma vigencia, alcance y plazos en el texto oficial antes de decidir controles.

### Documentación, cursos y credenciales

- [Lista de regulaciones del Administrador de cumplimiento de Microsoft Purview](https://learn.microsoft.com/es-es/purview/compliance-manager-regulations-list) · Documentación · Oficial · ES · Microsoft Learn. Lista de plantillas regulatorias de Compliance Manager (incluidas secciones de América Latina y Sudamérica) e indica que A5/E5/G5 permite usar tres regulaciones premium sin costo además de la línea base de Microsoft.
- [Ley 21.719 - Regula la protección y el tratamiento de los datos personales y crea la Agencia de Protección de Datos Personales (Chile)](https://www.leychile.cl/leychile/navegar?idNorma=1209272) · Documentación · Comunidad · ES · Congreso Nacional de Chile · Biblioteca del Congreso Nacional de Chile · 5 feb 2026. Nueva ley chilena de datos personales (publicada 13-dic-2024) que entra en vigencia el 1-dic-2026 y crea la Agencia de Protección de Datos Personales.
- [Ley Federal de Protección de Datos Personales en Posesión de los Particulares (México, nueva ley 2025)](https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPDPPP.pdf?Sid=1) · Documentación · Comunidad · ES · Congreso de la Unión · Cámara de Diputados de México · 14 nov 2025. Texto vigente de la nueva LFPDPPP publicada en el DOF el 20-mar-2025, que define datos personales sensibles y derechos ARCO aplicables a la clasificación de información.
- [Decreto Supremo N.° 016-2024-JUS - Reglamento de la Ley N.° 29733, Ley de Protección de Datos Personales (Perú)](https://www.gob.pe/institucion/anpd/normas-legales/6554453-n-016-2024-jus) · Documentación · Comunidad · ES · Ministerio de Justicia y Derechos Humanos · Autoridad Nacional de Protección de Datos Personales (Perú) · 30 nov 2024. Nuevo reglamento peruano de protección de datos personales publicado el 30-nov-2024, base para definir categorías de datos y medidas de seguridad a etiquetar.

**Manos a la obra**

1. `Laboratorio` Con la hoja «Normativa MCSA» del libro de Excel, elige las normas de los países donde opera tu organización y arma una tabla: categoría de dato que protegen, SIT o clasificador que la detecta, etiqueta mínima y evidencia que generarías. Márcala como borrador para validar con Legal.
2. `Laboratorio` Crea en Compliance Manager una evaluación con la plantilla de tu país o la más cercana y vincula las acciones de mejora de etiquetado y cifrado ([plantillas regulatorias](https://learn.microsoft.com/es-es/purview/compliance-manager-regulations-list)). En el laboratorio, usa solo plantillas incluidas para no consumir cupos.
3. `Laboratorio` Crea los SIT personalizados que tu tabla necesita y que no cubre un SIT integrado, y pruébalos con datos sintéticos como en el módulo I2.
4. `Solo producción` Presenta a Legal y Privacidad la tabla de normas y controles y la propuesta de taxonomía, y obtén su aprobación escrita antes de aplicar etiquetas cifrantes a datos personales. Forma segura: sesiones documentadas, decisiones registradas con fecha y responsable, y ningún cambio técnico sin aprobación.

<a id="reto-operacion"></a>

## Reto del nivel

**Un programa defendible ante una auditoría.** Integra el RACI, el proceso de cambios de etiquetas, el kit de adopción, el tablero con diez indicadores alimentado con 30 días de datos exportados y la tabla de normas y controles de los países donde operas, marcada como borrador para validar con Legal y Privacidad. Cierra con una hoja de ruta de seis meses y un resumen ejecutivo de una página para el comité de riesgos.

<a id="quiz-operacion"></a>

## Evaluación del nivel

Responde y compara con [Evaluaciones y respuestas](06_Evaluaciones_y_respuestas.md#eval-operacion). Con 80 % o más, ¡nivel aprobado! (En la versión web puedes corregir en línea y generar tu certificado).

1. ¿Cuál es el primer paso del modelo secure by default de Microsoft Purview?
   - a) Aplicar DKE a todo el contenido
   - b) Empezar con etiquetado predeterminado
   - c) Bloquear todo el correo externo
   - d) Auto-etiquetar los buzones en reposo

2. ¿Qué propone enseñar a las personas el modelo secure by default?
   - a) A decidir cuándo proteger cada archivo
   - b) A configurar Rights Management
   - c) A gestionar las excepciones
   - d) A escribir consultas KQL

3. En el paso 2 del modelo secure by default, ¿qué se recomienda auto-etiquetar como Altamente confidencial?
   - a) Todas las credenciales
   - b) Todas las presentaciones
   - c) Todos los PDF
   - d) Todos los correos externos

4. Publicaste cambios en una política de etiquetas dirigida a un grupo recién creado. ¿Cuándo conviene empezar a diagnosticar?
   - a) De inmediato, porque los cambios son instantáneos
   - b) A los 5 minutos, cuando termina la sincronización
   - c) A los 30 días, cuando se renueva la licencia de uso
   - d) Después de 24 a 48 horas

5. ¿Desde dónde recomienda la guía de despliegue de Microsoft arrancar un programa de Information Protection?
   - a) Desde DSPM, con las etiquetas y políticas predeterminadas
   - b) Desde el escáner local, inventariando primero los recursos compartidos
   - c) Desde Customer Key, cifrando primero todos los buzones
   - d) Desde el portal clásico de cumplimiento

6. Los informes de postura de Information Protection…
   - a) Están en disponibilidad general y conservan un año de historial
   - b) Están en vista previa, usan una ventana móvil de 30 días y conviene guardarlos en PDF
   - c) Solo existen con Microsoft 365 E3
   - d) Requieren Microsoft Sentinel

7. Necesitas la tendencia anual de bajadas de etiqueta. ¿Qué haces?
   - a) Pides al soporte que amplíe la retención del explorador
   - b) Usas el informe de etiquetas de Unified Catalog, que guarda un año de tendencia
   - c) Exportas periódicamente con Export-ActivityExplorerData hacia un almacén propio
   - d) Cambias a 365 días la ventana del informe de postura en su configuración

8. ¿Cuándo muestra datos el informe clásico de etiquetas de Unified Catalog?
   - a) Siempre, para todo el contenido de Microsoft 365 y del Data Map
   - b) Solo en tenants con Microsoft 365 E3 sin Purview Suite
   - c) Solo para el correo de Exchange
   - d) Solo si extendiste las etiquetas al Data Map

9. ¿Cuál de estas es una rutina operativa del paso 4 del modelo secure by default?
   - a) Revisar sitios sin etiqueta y desalineaciones entre la etiqueta del sitio y la de la biblioteca con Graph
   - b) Eliminar cada mes las etiquetas que cifran y crearlas de nuevo con permisos actualizados
   - c) Desactivar la auditoría unificada fuera del horario laboral para ahorrar costos
   - d) Reentrenar cada semana los clasificadores integrados con documentos del tenant

10. ¿Qué fuente usarías para medir las bajadas de etiqueta con su justificación?
   - a) El Usage center de Purview, que registra cada cambio de etiqueta
   - b) Compliance Manager, en las acciones de mejora de etiquetado
   - c) El explorador de actividades o la tabla MicrosoftPurviewInformationProtection
   - d) El informe clásico de etiquetas de Unified Catalog

11. ¿Desde cuándo rige la Ley 21.719 de protección de datos personales de Chile?
   - a) Desde el 13 de diciembre de 2024
   - b) Desde el 1 de diciembre de 2026
   - c) Desde el 20 de marzo de 2025
   - d) Desde el 30 de noviembre de 2024

12. ¿Cuántas regulaciones premium sin costo, además de la línea base de Microsoft, permiten usar las licencias A5, E5 y G5 en Compliance Manager?
   - a) Una
   - b) Diez
   - c) Todas
   - d) Tres

13. Ante el requisito de una ley de datos personales, ¿cuál es el papel del equipo de Information Protection?
   - a) Traducir los requisitos que Legal y Privacidad validaron en SIT, etiquetas, cifrado y evidencias
   - b) Interpretar la ley por su cuenta y decidir los controles sin consultar a otras áreas
   - c) Esperar la primera auditoría del regulador para decidir qué controles aplicar
   - d) Aplicar DKE a todos los datos personales para cumplir cualquier norma de la región

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. No es asesoría legal: las decisiones sobre datos personales deben validarse con Legal y Privacidad. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026
